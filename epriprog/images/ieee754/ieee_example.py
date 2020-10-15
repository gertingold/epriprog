from struct import pack
from pyx import canvas, color, path, text

def get_bits(x):
    bytestring = pack('>d', x)
    for byte in bytestring[::-1]:
        for n in range(8):
            quotient, remainder = divmod(byte, 2)
            yield remainder
            byte = quotient

text.set(text.LatexRunner)

x = -25.640625
wd = 0.3
pos = 0
c = canvas.canvas()
c.fill(path.rect(-63*wd, 0, wd, wd), [color.rgb(1, 0.7, 0.2)])
c.fill(path.rect(-62*wd, 0, 11*wd, wd), [color.rgb(0.7, 1.0, 0.7)])
c.fill(path.rect(-51*wd, 0, 52*wd, wd), [color.rgb(0.9, 0.7, 1.0)])
for bit in get_bits(x):
    c.stroke(path.rect(pos, 0, wd, wd))
    c.text(pos+0.5*wd, 0.5*wd, fr'\textsf{{{bit}}}',
           [text.halign.center, text.valign.middle])
    pos = pos-wd

xoff = -63
for nr, s in enumerate(pack('>d', x).hex()):
    start = (xoff+4*nr)*wd
    end = (xoff+4*(nr+1))*wd
    c.text(start+2*wd, wd+0.3, fr'\textsf{{{s.upper()}}}', [text.halign.center])
    p = path.path(path.moveto(start+0.1*wd, wd+0.1),
                  path.lineto(start+0.1*wd, wd+0.2),
                  path.lineto(end-0.1*wd, wd+0.2),
                  path.lineto(end-0.1*wd, wd+0.1))
    c.stroke(p)
c.writeGSfile("ieee_example.png", resolution=300)
