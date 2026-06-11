# AIgenta Makefile
# Convenient commands for common operations

.PHONY: help validate build search stats test clean install

# Default target
help:
	@echo "AIgenta - Makefile Commands"
	@echo ""
	@echo "Core Commands:"
	@echo "  make validate   - Run validation checks"
	@echo "  make build      - Run full build (validation + search index)"
	@echo "  make search     - Generate search index"
	@echo "  make stats      - Show project statistics"
	@echo "  make test       - Run all tests"
	@echo ""
	@echo "Metadata Commands:"
	@echo "  make metadata   - Add metadata to all files"
	@echo "  make metadata-dry-run  - Preview metadata addition"
	@echo ""
	@echo "CLI Commands (using tools/aigenta.py):"
	@echo "  make cli-validate     - CLI: Run validation"
	@echo "  make cli-search QUERY='text'  - CLI: Search content"
	@echo "  make cli-stats        - CLI: Show statistics"
	@echo "  make cli-new TYPE='type' NAME='name'  - CLI: Create new file"
	@echo ""
	@echo "Utility Commands:"
	@echo "  make clean      - Clean generated files"
	@echo "  make install    - Install dependencies"
	@echo ""

# Run validation
validate:
	@echo "🔍 Running validation..."
	@python tests/validate.py

# Full build
build: search validate
	@echo "✅ Build complete!"

# Generate search index
search:
	@echo "🔍 Generating search index..."
	@python tools/generate_search_index.py

# Show statistics
stats:
	@echo "📊 Project statistics:"
	@python tools/aigenta.py stats

# Run tests
test: validate
	@echo "✅ All tests passed!"

# Add metadata to all files
metadata:
	@echo "📝 Adding metadata to all files..."
	@python tools/add_metadata.py

# Preview metadata addition
metadata-dry-run:
	@echo "📝 Previewing metadata addition..."
	@python tools/add_metadata.py --dry-run

# CLI: Run validation
cli-validate:
	@python tools/aigenta.py validate

# CLI: Search content
cli-search:
	@if [ -z "$(QUERY)" ]; then \
		echo "❌ Error: QUERY parameter required"; \
		echo "Usage: make cli-search QUERY='your search term'"; \
		exit 1; \
	fi
	@python tools/aigenta.py search "$(QUERY)"

# CLI: Show statistics
cli-stats:
	@python tools/aigenta.py stats

# CLI: Create new file
cli-new:
	@if [ -z "$(TYPE)" ] || [ -z "$(NAME)" ]; then \
		echo "❌ Error: TYPE and NAME parameters required"; \
		echo "Usage: make cli-new TYPE='rhetoric' NAME='metaphor'"; \
		exit 1; \
	fi
	@python tools/aigenta.py new $(TYPE) $(NAME)

# Clean generated files
clean:
	@echo "🧹 Cleaning generated files..."
	@rm -f search-index.json
	@rm -f validation-results.txt
	@echo "✅ Clean complete!"

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	@pip install pyyaml
	@chmod +x tools/add_metadata.py
	@chmod +x tools/generate_search_index.py
	@chmod +x tools/aigenta.py
	@echo "✅ Installation complete!"

# Quick start
setup: install metadata build
	@echo "✅ AIgenta setup complete!"
	@echo "   Try: make search"
	@echo "   Or:  open search.html"