.PHONY: all clean generate_drawio generate_py generate_md

# ========== Configuration ==========

# Draw.io setup
DOCPATH := documentation/
DRAWIOS := $(wildcard $(DOCPATH)*.drawio)
PNGS := $(DRAWIOS:.drawio=.png)

# Pyreverse setup
NAME := Ecosystem
SRCPATH := src/Eco/
PYFILES := $(wildcard $(SRCPATH)*.py)
CLASSES_IMG := $(DOCPATH)classes_$(NAME).png
PACKAGES_IMG := $(DOCPATH)packages_$(NAME).png

# pandoc setup
MDS := $(wildcard $(DOCPATH)*.md)
PDFS := $(MDS:.md=.pdf)

# ========== High-Level Targets ==========

# Default target: generate diagrams from drawio and Python
all: generate_drawio generate_py generate_md

# Only build drawio PNGs when drawio files changed
generate_drawio: $(PNGS)

# Build Python class diagrams from .py files if changed
generate_py: $(CLASSES_IMG) $(PACKAGES_IMG)

# Only build md to pdf when pdf files changed
generate_md: $(PDFS)

# ========== Draw.io Rules ==========

# Pattern rule: convert .drawio → .png
%.png: %.drawio
	@echo "*** Converting $< → $@"
	/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -o $@ $<

# ========== Pyreverse Rules ==========

# Rule: If any .py file changes, regenerate the .png diagrams
$(CLASSES_IMG) $(PACKAGES_IMG): $(PYFILES)
	@echo "*** Generating class diagrams with pyreverse..."
	pyreverse -ASmy -o png -d $(DOCPATH) -p $(NAME) $(SRCPATH)

# ========== Md Rules ==========

# Pattern rule: convert .md → .pdf
%.pdf: %.md
	@echo "*** Converting $< → $@"
	pandoc --resource-path=$(DOCPATH) $< -o $@

# ========== Cleanup ==========

clean:
	@echo "*** Removing generated files..."
	rm -f $(PNGS) $(CLASSES_IMG) $(PACKAGES_IMG) $(PDFS)
