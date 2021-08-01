tex2pdf = pdflatex
pdf2png = convert -density 300 -colorspace rgb

targets = \
	digides_drawings \
	rta_drawings

.PHONY: %
%: %.tex
	@echo "compiling $< to pdf..."
	@$(tex2pdf) $< > .stdout.pdflatex
	@echo "extracting png's for $@..."
	@$(pdf2png) $(basename $<).pdf $(basename $@)_%d.png > .stdout.convert
	@rm -f *.pdf *.aux *.log *.synctex.gz

.PHONY: all	
all: $(targets)

.PHONY: clean
clean:
	rm -f *.png *.pdf *.aux *.log *.synctex.gz .stdout.*
