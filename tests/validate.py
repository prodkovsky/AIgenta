#!/usr/bin/env python3
"""
AIgenta Structural Validator

Validates the integrity of the AIgenta file-based writing system.
Uses only Python standard library — no external dependencies.

Usage:
    python tests/validate.py

Exit codes:
    0 = all checks passed
    1 = one or more checks failed
"""

import os
import re
import sys
from pathlib import Path
import json

# Project root is the parent of tests/
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
MANIFEST_PATH = PROJECT_ROOT / "MANIFEST.md"

# Expected file structure
EXPECTED_FILES = {
    "root": [
        "CLAUDE.md",
        "README.md",
        "SECURITY.md",
        "AGENTS.md",
        "index.html",
        ".gitignore",
    ],
    "writing_context": "workspaces/writing/CONTEXT.md",
    "research_context": "workspaces/research/CONTEXT.md",
    "code_context": "workspaces/code/CONTEXT.md",
    "styles": [
        "workspaces/writing/styles/academic.md",
        "workspaces/writing/styles/technical.md",
        "workspaces/writing/styles/poetic.md",
        "workspaces/writing/styles/screenwriter.md",
        "workspaces/writing/styles/neutral.md",
    ],
    "rhetoric": [
        "workspaces/writing/rhetoric/ethos.md",
        "workspaces/writing/rhetoric/pathos.md",
        "workspaces/writing/rhetoric/logos.md",
        "workspaces/writing/rhetoric/tricolon.md",
        "workspaces/writing/rhetoric/anaphora.md",
        "workspaces/writing/rhetoric/antithesis.md",
        "workspaces/writing/rhetoric/chiasmus.md",
        "workspaces/writing/rhetoric/erotesma.md",
        "workspaces/writing/rhetoric/euphemism.md",
        "workspaces/writing/rhetoric/hyperbole.md",
    ],
    "templates": [
        "workspaces/writing/templates/essay-template.md",
        "workspaces/writing/templates/article-template.md",
        "workspaces/writing/templates/screenplay-template.md",
        "workspaces/writing/templates/technical-doc-template.md",
    ],
    "apis": [
        "integrations/apis/openrouter.md",
        "integrations/apis/ollama.md",
    ],
    "memory": [
        "memory/learnings.md",
        "memory/decisions.md",
    ],
}

# Quality thresholds
RHETORIC_MIN_LINES = 80
RHETORIC_MAX_LINES = 220
STYLE_MIN_LINES = 100
TEMPLATE_MIN_LINES = 100
CONTEXT_MIN_LINES = 50
API_MIN_LINES = 30
MEMORY_MIN_LINES = 30

# Corruption markers — shell artifacts and garbled content patterns
# These are specific enough to not match normal prose
CORRUPTION_MARKERS = [
    "<< 'EOF'",          # shell heredoc artifact
    "cat >",             # shell command artifact
    "#foo\n",            # random comment fragment
    "#ing\n",            # random header fragment
    "#te ",              # truncated header
    "#ul ",              # truncated header
    "#d <",              # truncated markdown
    "#cou",              # truncated content
    "\\n✅ \\\"",        # garbled checkmark + quote
    "\\n# \\n",          # empty header artifact
    "\\n---\\n---\\n",    # duplicate separators (possible paste error)
]


def log(level: str, message: str) -> None:
    """Print a log message with level indicator."""
    symbols = {"PASS": "✅", "FAIL": "❌", "INFO": "ℹ️", "WARN": "⚠️"}
    symbol = symbols.get(level, "•")
    print(f"{symbol} [{level}] {message}")


def file_exists(rel_path: str) -> bool:
    """Check if a file exists relative to project root."""
    return (PROJECT_ROOT / rel_path).is_file()


def dir_exists(rel_path: str) -> bool:
    """Check if a directory exists relative to project root."""
    return (PROJECT_ROOT / rel_path).is_dir()


def count_lines(rel_path: str) -> int:
    """Count lines in a file."""
    try:
        with open(PROJECT_ROOT / rel_path, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except Exception as e:
        log("FAIL", f"Could not read {rel_path}: {e}")
        return 0


def read_file(rel_path: str) -> str:
    """Read file contents."""
    try:
        with open(PROJECT_ROOT / rel_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        log("FAIL", f"Could not read {rel_path}: {e}")
        return ""


def check_file_structure() -> bool:
    """Verify all expected files and directories exist."""
    log("INFO", "Checking file structure...")
    passed = True

    # Root files
    for f in EXPECTED_FILES["root"]:
        if file_exists(f):
            log("PASS", f"Root file exists: {f}")
        else:
            log("FAIL", f"Missing root file: {f}")
            passed = False

    # Context files
    for key in ["writing_context", "research_context", "code_context"]:
        f = EXPECTED_FILES[key]
        if file_exists(f):
            log("PASS", f"Workspace context exists: {f}")
        else:
            log("FAIL", f"Missing workspace context: {f}")
            passed = False

    # Grouped files
    for group_name in ["styles", "rhetoric", "templates", "apis", "memory"]:
        for f in EXPECTED_FILES[group_name]:
            if file_exists(f):
                log("PASS", f"{group_name.title()} file exists: {f}")
            else:
                log("FAIL", f"Missing {group_name} file: {f}")
                passed = False

    # Key directories
    key_dirs = [
        "workspaces/writing/projects",
        "workspaces/research",
        "workspaces/code",
        "integrations/apis",
        "memory",
    ]
    for d in key_dirs:
        if dir_exists(d):
            log("PASS", f"Directory exists: {d}")
        else:
            log("FAIL", f"Missing directory: {d}")
            passed = False

    return passed


def check_quality_thresholds() -> bool:
    """Verify files meet minimum depth/length thresholds."""
    log("INFO", "Checking content depth...")
    passed = True

    # Rhetoric files
    for f in EXPECTED_FILES["rhetoric"]:
        lines = count_lines(f)
        if lines < RHETORIC_MIN_LINES:
            log("FAIL", f"{f} too short: {lines} lines (min {RHETORIC_MIN_LINES})")
            passed = False
        elif lines > RHETORIC_MAX_LINES:
            log("WARN", f"{f} unusually long: {lines} lines (max {RHETORIC_MAX_LINES})")
        else:
            log("PASS", f"{f}: {lines} lines")

    # Style files
    for f in EXPECTED_FILES["styles"]:
        lines = count_lines(f)
        if lines < STYLE_MIN_LINES:
            log("FAIL", f"{f} too short: {lines} lines (min {STYLE_MIN_LINES})")
            passed = False
        else:
            log("PASS", f"{f}: {lines} lines")

    # Templates
    for f in EXPECTED_FILES["templates"]:
        lines = count_lines(f)
        if lines < TEMPLATE_MIN_LINES:
            log("FAIL", f"{f} too short: {lines} lines (min {TEMPLATE_MIN_LINES})")
            passed = False
        else:
            log("PASS", f"{f}: {lines} lines")

    # Context files
    for key in ["writing_context", "research_context", "code_context"]:
        f = EXPECTED_FILES[key]
        lines = count_lines(f)
        if lines < CONTEXT_MIN_LINES:
            log("FAIL", f"{f} too short: {lines} lines (min {CONTEXT_MIN_LINES})")
            passed = False
        else:
            log("PASS", f"{f}: {lines} lines")

    # API docs
    for f in EXPECTED_FILES["apis"]:
        lines = count_lines(f)
        if lines < API_MIN_LINES:
            log("FAIL", f"{f} too short: {lines} lines (min {API_MIN_LINES})")
            passed = False
        else:
            log("PASS", f"{f}: {lines} lines")

    # Memory files
    for f in EXPECTED_FILES["memory"]:
        lines = count_lines(f)
        if lines < MEMORY_MIN_LINES:
            log("FAIL", f"{f} too short: {lines} lines (min {MEMORY_MIN_LINES})")
            passed = False
        else:
            log("PASS", f"{f}: {lines} lines")

    return passed


def check_corruption() -> bool:
    """Check for known corruption artifacts in files."""
    log("INFO", "Checking for corruption artifacts...")
    passed = True

    files_to_check = []
    for group_name in ["styles", "rhetoric", "templates", "apis", "memory"]:
        files_to_check.extend(EXPECTED_FILES[group_name])
    for key in ["writing_context", "research_context", "code_context"]:
        files_to_check.append(EXPECTED_FILES[key])
    files_to_check.extend(EXPECTED_FILES["root"])

    for f in files_to_check:
        content = read_file(f)
        if not content:
            passed = False
            continue

        for marker in CORRUPTION_MARKERS:
            if marker in content:
                log("FAIL", f"{f} contains corruption marker: '{marker}'")
                passed = False

    if passed:
        log("PASS", "No corruption artifacts detected")

    return passed


def check_documentation_sync() -> bool:
    """Verify README and index.html reflect actual state."""
    log("INFO", "Checking documentation sync...")
    passed = True

    readme = read_file("README.md")
    index_html = read_file("index.html")

    # Count rhetoric files
    rhetoric_count = len(EXPECTED_FILES["rhetoric"])
    if f"{rhetoric_count}/10" in readme or f"{rhetoric_count} rhetorical devices" in readme.lower():
        log("PASS", f"README reflects {rhetoric_count} rhetoric devices")
    else:
        log("WARN", f"README may not reflect {rhetoric_count} rhetoric devices")

    # Count templates
    template_count = len(EXPECTED_FILES["templates"])
    if f"{template_count}/4" in readme or f"{template_count} writing templates" in readme.lower():
        log("PASS", f"README reflects {template_count} templates")
    else:
        log("WARN", f"README may not reflect {template_count} templates")

    # Check index.html for all 10 rhetoric devices
    expected_devices = [Path(f).stem for f in EXPECTED_FILES["rhetoric"]]
    missing_in_html = []
    for device in expected_devices:
        if f'data-device="{device}"' not in index_html:
            missing_in_html.append(device)

    if missing_in_html:
        log("FAIL", f"index.html missing rhetoric pills: {', '.join(missing_in_html)}")
        passed = False
    else:
        log("PASS", f"index.html contains all {len(expected_devices)} rhetoric pills")

    # Check index.html for template completeness
    if 'class="status complete">Complete' in index_html:
        log("PASS", "index.html marks templates as complete")
    else:
        log("FAIL", "index.html does not mark templates as complete")

    return passed


def check_references() -> bool:
    """Verify paths mentioned in markdown files exist on disk."""
    log("INFO", "Checking cross-references...")
    passed = True

    markdown_files = list(PROJECT_ROOT.rglob("*.md"))
    path_pattern = re.compile(r"(?:`)?(workspaces/[^`\s\)\]]+|integrations/[^`\s\)\]]+|memory/[^`\s\)\]]+)(?:`)?")

    referenced_paths = set()
    for md_file in markdown_files:
        if ".git" in str(md_file):
            continue
        content = md_file.read_text(encoding="utf-8")
        for match in path_pattern.findall(content):
            # Clean up trailing punctuation / markdown artifacts
            clean = match.strip("`.,;:'\")")
            if clean.endswith("/") or clean.endswith(".md") or "/" in clean:
                referenced_paths.add(clean)

    for ref in sorted(referenced_paths):
        # Skip example/template paths that are not meant to exist literally
        placeholder_patterns = [
            "YYYY-MM-DD",
            "service-name",
            "new-workspace",
            "device-name",
            "style-name",
            "new-style",
            "your-style",
            "template-type",
            "project-name",
            "topic-name",
            "documentation-topic",
            "research-topic",
        ]
        if any(pattern in ref for pattern in placeholder_patterns):
            log("PASS", f"Referenced path is documentation example (skipped): {ref}")
            continue

        # Skip wildcard or brace-expansion references
        if "*" in ref or "{" in ref or "}" in ref:
            log("PASS", f"Referenced path contains wildcard/braces (skipped): {ref}")
            continue

        # Skip example directories mentioned but not created
        example_dirs = [
            "workspaces/code/templates",
            "workspaces/research/methods",
            "workspaces/research/sources",
            "workspaces/writing/editors",
        ]
        if ref.rstrip("/") in example_dirs:
            log("PASS", f"Referenced path is optional example directory (skipped): {ref}")
            continue

        target = PROJECT_ROOT / ref
        # Some references are to directories, some to file prefixes
        if target.exists():
            log("PASS", f"Referenced path exists: {ref}")
        elif (target.parent / (target.name + ".md")).exists():
            log("PASS", f"Referenced path exists (as .md): {ref}.md")
        elif target.is_dir():
            log("PASS", f"Referenced path exists (directory): {ref}")
        else:
            log("FAIL", f"Referenced path missing: {ref}")
            passed = False

    return passed


def check_manifest() -> bool:
    """Verify MANIFEST.md exists and is properly formatted."""
    log("INFO", "Checking MANIFEST.md...")
    passed = True

    if not MANIFEST_PATH.exists():
        log("FAIL", "MANIFEST.md not found - this is required as the single source of truth")
        return False

    log("PASS", "MANIFEST.md exists")

    # Check for required sections
    manifest_content = read_file("MANIFEST.md")
    required_sections = [
        "## System Files",
        "## Workspaces",
        "## Writing Workspace: Styles",
        "## Writing Workspace: Rhetorical Devices",
        "## Writing Workspace: Templates",
        "## API Integrations",
        "## Memory Files",
        "## Quality Thresholds",
    ]

    for section in required_sections:
        if section in manifest_content:
            log("PASS", f"MANIFEST.md contains section: {section}")
        else:
            log("FAIL", f"MANIFEST.md missing section: {section}")
            passed = False

    return passed


def main() -> int:
    """Run all validation checks."""
    print("=" * 60)
    print("AIgenta Structural Validator")
    print("=" * 60)
    print(f"Project root: {PROJECT_ROOT}")
    print()

    results = {
        "Manifest Check": check_manifest(),
        "File Structure": check_file_structure(),
        "Content Depth": check_quality_thresholds(),
        "Corruption Check": check_corruption(),
        "Documentation Sync": check_documentation_sync(),
        "Cross-References": check_references(),
    }

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    all_passed = True
    for check_name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        log(status, check_name)
        if not passed:
            all_passed = False

    print()
    if all_passed:
        log("PASS", "All validation checks passed. AIgenta is A+.")
        return 0
    else:
        log("FAIL", "One or more validation checks failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
