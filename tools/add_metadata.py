#!/usr/bin/env python3
"""
Add YAML frontmatter metadata to markdown files in AIgenta.
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Metadata schema definition
METADATA_SCHEMA = {
    'title': str,
    'type': str,  # rhetoric, style, template, method, pattern, project, context, api, memory
    'category': str,  # varies by type
    'tags': List[str],
    'created': str,  # YYYY-MM-DD
    'updated': str,  # YYYY-MM-DD
    'lines': int,
    'status': str,  # active, draft, archived
    'author': str,  # optional
    'version': str,  # optional
}

# Type-specific category mappings
TYPE_CATEGORIES = {
    'rhetoric': ['Aristotelian', 'Structural', 'Contrast', 'Inversion', 'Question', 'Language'],
    'style': ['Academic', 'Technical', 'Poetic', 'Creative', 'Screenwriter', 'Neutral'],
    'template': ['Academic', 'Blog', 'Creative', 'Technical'],
    'method': ['Research', 'Analysis', 'Synthesis'],
    'pattern': ['Documentation', 'Design', 'Architecture'],
    'project': ['Writing', 'Research', 'Code'],
    'context': ['Workspace'],
    'api': ['External', 'Local'],
    'memory': ['Decisions', 'Learnings'],
}


def infer_file_type(filepath: Path) -> str:
    """Infer file type from path."""
    path_str = str(filepath)
    
    if 'rhetoric/' in path_str:
        return 'rhetoric'
    elif 'styles/' in path_str:
        return 'style'
    elif 'templates/' in path_str:
        return 'template'
    elif 'methods/' in path_str:
        return 'method'
    elif 'patterns/' in path_str:
        return 'pattern'
    elif 'projects/' in path_str:
        return 'project'
    elif filepath.name == 'CONTEXT.md':
        return 'context'
    elif 'apis/' in path_str:
        return 'api'
    elif 'memory/' in path_str:
        return 'memory'
    else:
        return 'unknown'


def extract_title(content: str, filepath: Path) -> str:
    """Extract title from first heading or filename."""
    # Try to find first h1 heading
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()
    
    # Fall back to filename
    return filepath.stem.replace('-', ' ').replace('_', ' ').title()


def extract_category(content: str, file_type: str) -> Optional[str]:
    """Extract category from content or infer from type."""
    # Look for explicit category lines
    category_match = re.search(r'(?i)category:\s*(.+)', content)
    if category_match:
        return category_match.group(1).strip()
    
    # Try to infer from common patterns
    if file_type == 'rhetoric':
        type_match = re.search(r'(?i)type:\s*(.+)', content)
        if type_match:
            return type_match.group(1).strip()
    
    return None


def count_lines(filepath: Path) -> int:
    """Count non-empty lines in file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return len([line for line in f if line.strip()])


def generate_metadata(filepath: Path, existing_content: str) -> Dict:
    """Generate metadata for a file."""
    file_type = infer_file_type(filepath)
    title = extract_title(existing_content, filepath)
    line_count = count_lines(filepath)
    category = extract_category(existing_content, file_type)
    
    # Infer creation date from filename if possible (YYYY-MM-DD format)
    created_date = None
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filepath.stem)
    if date_match:
        created_date = date_match.group(1)
    else:
        created_date = "2026-06-08"  # Default project start date
    
    metadata = {
        'title': title,
        'type': file_type,
        'category': category,
        'tags': [],
        'created': created_date,
        'updated': datetime.now().strftime('%Y-%m-%d'),
        'lines': line_count,
        'status': 'active',
    }
    
    return metadata


def has_frontmatter(content: str) -> bool:
    """Check if file already has YAML frontmatter."""
    return content.startswith('---')


def add_frontmatter(filepath: Path, metadata: Dict) -> bool:
    """Add YAML frontmatter to file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_frontmatter(content):
            print(f"  ⏭️  Skipping (already has frontmatter): {filepath}")
            return False
        
        # Build frontmatter string
        frontmatter_lines = ['---']
        for key, value in metadata.items():
            if value is None or value == []:
                continue
            if isinstance(value, list):
                if value:
                    frontmatter_lines.append(f'{key}: {value}')
            else:
                frontmatter_lines.append(f'{key}: {value}')
        frontmatter_lines.append('---')
        frontmatter_lines.append('')
        
        # Write new content
        new_content = '\n'.join(frontmatter_lines) + content
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Added frontmatter: {filepath}")
        return True
    
    except Exception as e:
        print(f"  ❌ Error processing {filepath}: {e}")
        return False


def process_directory(root_dir: Path, dry_run: bool = False) -> Dict[str, int]:
    """Process all markdown files in directory."""
    stats = {
        'processed': 0,
        'skipped': 0,
        'errors': 0,
    }
    
    print(f"\n{'='*60}")
    print(f"Adding metadata to markdown files in: {root_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"{'='*60}\n")
    
    # Find all markdown files
    markdown_files = list(root_dir.rglob('*.md'))
    
    # Skip certain directories
    skip_dirs = {'.git', 'node_modules', '__pycache__', 'dist', 'build'}
    markdown_files = [f for f in markdown_files 
                      if not any(d in f.parts for d in skip_dirs)]
    
    print(f"Found {len(markdown_files)} markdown files\n")
    
    for filepath in sorted(markdown_files):
        # Skip if it's the IMPLEMENTATION_SUMMARY or METADATA_SCHEMA
        if filepath.name in ['IMPLEMENTATION_SUMMARY.md', 'METADATA_SCHEMA.md']:
            print(f"  ⏭️  Skipping (special file): {filepath}")
            stats['skipped'] += 1
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if has_frontmatter(content):
                print(f"  ⏭️  Skipping (already has frontmatter): {filepath.relative_to(root_dir)}")
                stats['skipped'] += 1
                continue
            
            metadata = generate_metadata(filepath, content)
            
            if dry_run:
                print(f"  📝 Would add metadata to: {filepath.relative_to(root_dir)}")
                print(f"     Title: {metadata['title']}")
                print(f"     Type: {metadata['type']}")
                stats['processed'] += 1
            else:
                if add_frontmatter(filepath, metadata):
                    stats['processed'] += 1
                else:
                    stats['skipped'] += 1
        
        except Exception as e:
            print(f"  ❌ Error: {filepath.relative_to(root_dir)} - {e}")
            stats['errors'] += 1
    
    return stats


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Add YAML frontmatter metadata to markdown files'
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to process (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--type',
        help='Only process files of this type (e.g., rhetoric, style, template)'
    )
    
    args = parser.parse_args()
    
    root_dir = Path(args.path).resolve()
    
    if not root_dir.exists():
        print(f"Error: Path does not exist: {root_dir}")
        sys.exit(1)
    
    if args.dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be modified\n")
    
    stats = process_directory(root_dir, dry_run=args.dry_run)
    
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"{'='*60}")
    print(f"✅ Processed: {stats['processed']}")
    print(f"⏭️  Skipped:   {stats['skipped']}")
    print(f"❌ Errors:    {stats['errors']}")
    print(f"{'='*60}")
    
    if stats['errors'] > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()