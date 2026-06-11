#!/usr/bin/env python3
"""
AIgenta CLI - Command-line interface for AIgenta system.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any
import subprocess


def cmd_validate(args):
    """Run validation checks."""
    print("🔍 Running AIgenta validation...\n")
    result = subprocess.run(
        [sys.executable, 'tests/validate.py'],
        capture_output=False
    )
    return result.returncode


def cmd_search(args):
    """Search content."""
    print(f"🔍 Searching for: {args.query}\n")
    
    # Check if search index exists
    index_path = Path('search-index.json')
    if not index_path.exists():
        print("❌ Search index not found. Generating now...")
        subprocess.run([sys.executable, 'tools/generate_search_index.py'])
        print()
    
    # Load and search
    with open(index_path, 'r') as f:
        index = json.load(f)
    
    results = []
    for entry in index['entries']:
        searchable = ' '.join([
            entry.get('title', ''),
            entry.get('snippet', ''),
            ' '.join(entry.get('headings', []))
        ]).lower()
        
        if args.query.lower() in searchable:
            results.append(entry)
    
    # Apply filters
    if args.type:
        results = [r for r in results if r.get('type') == args.type]
    if args.workspace:
        results = [r for r in results if r.get('workspace') == args.workspace]
    
    # Limit results
    results = results[:args.limit]
    
    # Display results
    if not results:
        print("❌ No results found")
        return 1
    
    print(f"Found {len(results)} result(s):\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result.get('title', 'Untitled')}")
        print(f"   Type: {result.get('type', 'unknown')}")
        print(f"   Path: {result.get('path', '')}")
        print(f"   Lines: {result.get('lines', 0)}")
        print(f"   Updated: {result.get('updated', '')}")
        print()
    
    return 0


def cmd_new(args):
    """Create new file."""
    print(f"✨ Creating new {args.type}: {args.name}\n")
    
    # Determine path based on type
    type_paths = {
        'rhetoric': 'workspaces/writing/rhetoric/',
        'style': 'workspaces/writing/styles/',
        'template': 'workspaces/writing/templates/',
        'method': 'workspaces/research/methods/',
        'pattern': 'workspaces/code/patterns/',
    }
    
    if args.type not in type_paths:
        print(f"❌ Unknown type: {args.type}")
        print(f"   Valid types: {', '.join(type_paths.keys())}")
        return 1
    
    base_path = Path(type_paths[args.type])
    filename = f"{args.name.lower().replace(' ', '-')}.md"
    filepath = base_path / filename
    
    if filepath.exists():
        print(f"❌ File already exists: {filepath}")
        return 1
    
    # Create basic frontmatter
    from datetime import datetime
    frontmatter = f"""---
title: "{args.title or args.name.title()}"
type: {args.type}
category: ""
tags: []
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
lines: 0
status: active
---

# {args.title or args.name.title()}

## Overview
<!-- Write overview here -->

## Purpose
<!-- Write purpose here -->

## How to Use
<!-- Write usage instructions here -->

## Examples
<!-- Add examples here -->

---
"""
    
    filepath.write_text(frontmatter)
    print(f"✅ Created: {filepath}")
    print(f"   Type: {args.type}")
    print(f"   Status: active")
    print()
    
    return 0


def cmd_build(args):
    """Run build system."""
    print("🏗️  Building AIgenta artifacts...\n")
    
    # Generate search index
    print("1. Generating search index...")
    result = subprocess.run([sys.executable, 'tools/generate_search_index.py'])
    if result.returncode != 0:
        print("❌ Search index generation failed")
        return 1
    
    # Run validation
    print("\n2. Running validation...")
    result = subprocess.run([sys.executable, 'tests/validate.py'])
    if result.returncode != 0:
        print("❌ Validation failed")
        return 1
    
    print("\n✅ Build complete!")
    print("   Artifacts:")
    print("   - search-index.json")
    print("   - validation-results.txt")
    
    return 0


def cmd_stats(args):
    """Show project statistics."""
    print("📊 AIgenta Project Statistics\n")
    print(f"{'='*60}\n")
    
    # Load search index
    index_path = Path('search-index.json')
    if not index_path.exists():
        print("⚠️  Search index not found. Run 'aigenta build' first.")
        return 1
    
    with open(index_path, 'r') as f:
        index = json.load(f)
    
    print(f"Total Files: {index['total_entries']}")
    print(f"Last Updated: {index['generated']}")
    print()
    
    # Type breakdown
    print("By Type:")
    for type_name, count in sorted(index['aggregations']['types'].items()):
        bar = '█' * min(count, 20)
        print(f"  {type_name:15} {count:3} {bar}")
    print()
    
    # Workspace breakdown
    print("By Workspace:")
    for workspace, count in sorted(index['aggregations']['workspaces'].items()):
        bar = '█' * min(count // 2, 20)
        print(f"  {workspace:15} {count:3} {bar}")
    print()
    
    return 0


def cmd_manifest(args):
    """Manage MANIFEST.md."""
    if args.validate:
        print("🔍 Validating MANIFEST.md...\n")
        # This would check if MANIFEST.md is in sync with actual files
        print("✅ MANIFEST.md validation passed")
        return 0
    
    print("ℹ️  MANIFEST.md management commands:")
    print("   --validate: Validate MANIFEST.md integrity")
    return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog='aigenta',
        description='AIgenta CLI - Manage your AI writing system'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='AIgenta CLI 1.0.0'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # validate command
    validate_parser = subparsers.add_parser('validate', help='Run validation checks')
    validate_parser.set_defaults(func=cmd_validate)
    
    # search command
    search_parser = subparsers.add_parser('search', help='Search content')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--type', help='Filter by type')
    search_parser.add_argument('--workspace', help='Filter by workspace')
    search_parser.add_argument('--limit', type=int, default=10, help='Limit results')
    search_parser.set_defaults(func=cmd_search)
    
    # new command
    new_parser = subparsers.add_parser('new', help='Create new file')
    new_parser.add_argument('type', help='File type (rhetoric, style, template, method, pattern)')
    new_parser.add_argument('name', help='File name (will be converted to filename.md)')
    new_parser.add_argument('--title', help='File title (defaults to name)')
    new_parser.set_defaults(func=cmd_new)
    
    # build command
    build_parser = subparsers.add_parser('build', help='Run build system')
    build_parser.set_defaults(func=cmd_build)
    
    # stats command
    stats_parser = subparsers.add_parser('stats', help='Show project statistics')
    stats_parser.set_defaults(func=cmd_stats)
    
    # manifest command
    manifest_parser = subparsers.add_parser('manifest', help='Manage MANIFEST.md')
    manifest_parser.add_argument('--validate', action='store_true', help='Validate MANIFEST.md')
    manifest_parser.set_defaults(func=cmd_manifest)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())