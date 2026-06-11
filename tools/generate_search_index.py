#!/usr/bin/env python3
"""
Generate search index from markdown files with YAML frontmatter.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any
import yaml


def parse_frontmatter(content: str) -> tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    # Find the end of frontmatter
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return {}, content
    
    frontmatter_str = content[3:end_idx]
    body = content[end_idx + 3:]
    
    try:
        metadata = yaml.safe_load(frontmatter_str)
        return metadata or {}, body
    except yaml.YAMLError:
        return {}, body


def extract_headings(content: str) -> List[str]:
    """Extract all headings from markdown content."""
    headings = []
    for line in content.split('\n'):
        if line.startswith('#'):
            # Remove # symbols and extra whitespace
            heading = re.sub(r'^#+\s*', '', line).strip()
            if heading:
                headings.append(heading)
    return headings


def extract_snippet(content: str, max_length: int = 200) -> str:
    """Extract a text snippet from content (first paragraph after headings)."""
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    # Skip headings
    non_headings = [line for line in lines if not line.startswith('#')]
    
    if non_headings:
        snippet = ' '.join(non_headings[:3])
        if len(snippet) > max_length:
            snippet = snippet[:max_length-3] + '...'
        return snippet
    
    return ''


def process_file(filepath: Path, root_dir: Path) -> Dict[str, Any]:
    """Process a single markdown file and extract search data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata, body = parse_frontmatter(content)
        headings = extract_headings(body)
        snippet = extract_snippet(body)
        
        # Get relative path
        rel_path = filepath.relative_to(root_dir)
        
        # Convert date objects to strings if present
        created = metadata.get('created', '')
        updated = metadata.get('updated', '')
        if hasattr(created, 'isoformat'):
            created = created.isoformat()
        if hasattr(updated, 'isoformat'):
            updated = updated.isoformat()
        
        return {
            'path': str(rel_path),
            'title': metadata.get('title', filepath.stem.replace('-', ' ').title()),
            'type': metadata.get('type', 'unknown'),
            'category': metadata.get('category', ''),
            'tags': metadata.get('tags', []),
            'created': str(created) if created else '',
            'updated': str(updated) if updated else '',
            'lines': metadata.get('lines', 0),
            'status': metadata.get('status', 'active'),
            'headings': headings,
            'snippet': snippet,
            'workspace': str(rel_path.parts[0]) if len(rel_path.parts) > 0 else 'root',
        }
    
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return None


def generate_search_index(root_dir: Path, output_file: Path) -> Dict[str, Any]:
    """Generate search index from all markdown files."""
    print(f"\n{'='*60}")
    print(f"Generating search index from: {root_dir}")
    print(f"{'='*60}\n")
    
    # Find all markdown files
    markdown_files = list(root_dir.rglob('*.md'))
    
    # Skip certain directories
    skip_dirs = {'.git', 'node_modules', '__pycache__', 'dist', 'build', 'archive'}
    markdown_files = [f for f in markdown_files 
                      if not any(d in f.parts for d in skip_dirs)]
    
    print(f"Found {len(markdown_files)} markdown files\n")
    
    # Process all files
    index_entries = []
    stats = {
        'total': len(markdown_files),
        'processed': 0,
        'skipped': 0,
        'errors': 0,
    }
    
    for filepath in sorted(markdown_files):
        # Skip special files
        if filepath.name in ['IMPLEMENTATION_SUMMARY.md', 'search-index.json']:
            stats['skipped'] += 1
            continue
        
        entry = process_file(filepath, root_dir)
        
        if entry:
            # Skip archived files from search
            if entry.get('status') == 'archived':
                stats['skipped'] += 1
                print(f"  ⏭️  Skipping (archived): {filepath.relative_to(root_dir)}")
            else:
                index_entries.append(entry)
                stats['processed'] += 1
                print(f"  ✅ Indexed: {filepath.relative_to(root_dir)}")
        else:
            stats['errors'] += 1
    
    # Build index with aggregations
    index = {
        'version': '1.0.0',
        'generated': __import__('datetime').datetime.now().isoformat(),
        'total_entries': len(index_entries),
        'entries': index_entries,
        'aggregations': {
            'types': {},
            'categories': {},
            'workspaces': {},
            'tags': {},
        },
    }
    
    # Build aggregations
    for entry in index_entries:
        # Type aggregation
        entry_type = entry.get('type', 'unknown')
        index['aggregations']['types'][entry_type] = \
            index['aggregations']['types'].get(entry_type, 0) + 1
        
        # Category aggregation
        category = entry.get('category', 'uncategorized')
        if category:
            index['aggregations']['categories'][category] = \
                index['aggregations']['categories'].get(category, 0) + 1
        
        # Workspace aggregation
        workspace = entry.get('workspace', 'root')
        index['aggregations']['workspaces'][workspace] = \
            index['aggregations']['workspaces'].get(workspace, 0) + 1
        
        # Tags aggregation
        for tag in entry.get('tags', []):
            index['aggregations']['tags'][tag] = \
                index['aggregations']['tags'].get(tag, 0) + 1
    
    # Write index to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"{'='*60}")
    print(f"✅ Processed: {stats['processed']}")
    print(f"⏭️  Skipped:   {stats['skipped']}")
    print(f"❌ Errors:    {stats['errors']}")
    print(f"📄 Index saved to: {output_file}")
    print(f"{'='*60}")
    
    # Print aggregations
    print("\nAggregations:")
    print(f"  Types: {len(index['aggregations']['types'])}")
    print(f"  Categories: {len(index['aggregations']['categories'])}")
    print(f"  Workspaces: {len(index['aggregations']['workspaces'])}")
    print(f"  Tags: {len(index['aggregations']['tags'])}")
    print(f"{'='*60}\n")
    
    return index


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate search index from markdown files'
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to process (default: current directory)'
    )
    parser.add_argument(
        '-o', '--output',
        default='search-index.json',
        help='Output file for search index (default: search-index.json)'
    )
    
    args = parser.parse_args()
    
    root_dir = Path(args.path).resolve()
    output_file = Path(args.output).resolve()
    
    if not root_dir.exists():
        print(f"Error: Path does not exist: {root_dir}")
        sys.exit(1)
    
    try:
        generate_search_index(root_dir, output_file)
        print("✅ Search index generation complete!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()