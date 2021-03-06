from pyx import canvas, color, deco, path, text, trafo

text.set(text.LatexRunner)
c = canvas.canvas()

markercolor = color.rgb(0.7, 0.5, 1.0)
utf8markercolor = color.rgb(1.0, 0.7, 0)
codecolor = color.rgb(0.7, 1, 0)


codepoint = 0x00221E
bits = 24

codepointbinary = [(codepoint & 2**n)/2**n for n in range(bits)]
codepointbinary.reverse()

size = 0.4
x0 = 0
y0 = 3
dy = 0.07
c.fill(path.rect(x0, y0, 8*size, size),
       [markercolor, deco.stroked([markercolor])])
c.stroke(path.rect(x0+8*size, y0, 4*size, size), [deco.filled([codecolor])])
c.stroke(path.rect(x0+12*size, y0, 6*size, size), [deco.filled([codecolor])])
c.stroke(path.rect(x0+18*size, y0, 6*size, size), [deco.filled([codecolor])])
for n in range(len(codepointbinary)):
    c.text(x0+(n+0.5)*size, y0+dy, r"\sffamily %i" % codepointbinary[n],
           [text.halign.center])

p = path.path(path.moveto(0.2*size, size+0.03),
              path.lineto(0.2*size, size+0.07),
              path.lineto(3.8*size, size+0.07),
              path.lineto(3.8*size, size+0.03))
for n in range(bits//4):
    c.stroke(p, [trafo.translate(4*n*size, y0)])
    c.text((4*n+2)*size, size+0.14+y0, r"\sffamily %X" %
           (codepoint >> (bits//4-n-1)*4 & 0x0f),
           [text.halign.center])

utf8code = 0xE08080 \
           + (((codepoint >> 12) & 0x0f) << 16) \
           + (((codepoint >> 6) & 0x3f) << 8) \
           + (codepoint & 0x3f)
utf8codebinary = [(utf8code & 2**n)/2**n for n in range(bits)]
utf8codebinary.reverse()

y1 = 2
c.fill(path.rect(x0, y1, 4*size, size),
       [utf8markercolor, deco.stroked([utf8markercolor])])
c.fill(path.rect(x0+8*size, y1, 2*size, size),
       [utf8markercolor, deco.stroked([utf8markercolor])])
c.fill(path.rect(x0+16*size, y1, 2*size, size),
       [utf8markercolor, deco.stroked([utf8markercolor])])
c.stroke(path.rect(x0+4*size, y1, 4*size, size), [deco.filled([codecolor])])
c.stroke(path.rect(x0+10*size, y1, 6*size, size), [deco.filled([codecolor])])
c.stroke(path.rect(x0+18*size, y1, 6*size, size), [deco.filled([codecolor])])
for n in range(len(utf8codebinary)):
    c.text(x0+(n+0.5)*size, y1+dy, r"\sffamily %i" % utf8codebinary[n],
           [text.halign.center])

p = path.path(path.moveto(0.2*size, -0.03),
              path.lineto(0.2*size, -0.07),
              path.lineto(3.8*size, -0.07),
              path.lineto(3.8*size, -0.03))
for n in range(bits//4):
    c.stroke(p, [trafo.translate(4*n*size, y1)])
    c.text((4*n+2)*size, -0.14+y1, r"\sffamily %X" %
           (utf8code >> (bits//4-n-1)*4 & 0x0f),
           [text.halign.center, text.valign.top])

c.stroke(path.line(10*size, y0-0.05, 6*size, y1+size+0.05),
         [deco.earrow.small])
c.stroke(path.line(15*size, y0-0.05, 13*size, y1+size+0.05),
         [deco.earrow.small])
c.stroke(path.line(21*size, y0-0.05, 21*size, y1+size+0.05),
         [deco.earrow.small])

c.writeGSfile("utf8_3.png", resolution=300)
