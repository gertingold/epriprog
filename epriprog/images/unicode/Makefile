# requires change in /etc/ImageMagick-6/policy.xml
# <policy domain="coder" rights="none" pattern="PDF" />
# -> <policy domain="coder" rights="read|write" pattern="PDF" />
all:
	python create_unicode_tex.py
	xelatex unicode.tex
	pdfcrop unicode.pdf unicode_cropped.pdf
	pdfseparate -f 2 -l 2 unicode_cropped.pdf u0000.pdf
	pdfseparate -f 3 -l 3 unicode_cropped.pdf u0080.pdf
	pdfseparate -f 9 -l 9 unicode_cropped.pdf u0380.pdf
	pdfseparate -f 70 -l 70 unicode_cropped.pdf u2200.pdf
	convert -density 300 u0000.pdf u0000.png
	convert -density 300 u0080.pdf u0080.png
	convert -density 300 u0380.pdf u0380.png
	convert -density 300 u2200.pdf u2200.png

clean:
	rm unicode.tex unicode.aux unicode.log unicode.pdf unicode_cropped.pdf
