from math import exp, expm1
from pyx import color, deco, graph, style, text, unit

text.set(text.LatexEngine)
mypainter = graph.axis.painter.regular(innerticklength=None,
                                       outerticklength=graph.axis.painter.ticklength.normal)
g = graph.graphxy(width=8,
                  x=graph.axis.log(title="$x$",
                                   painter=mypainter),
                  y=graph.axis.lin(title=r"$f(x)-1$",
                                   min=-1.1e-6,
                                   max=1.1e-6,
                                   painter=mypainter,
                                   parter=graph.axis.parter.lin(tickdists=[1e-6])),
                  key=graph.key.key(pos="tr")
                 )
g.plot(graph.data.function("y(x)=(exp(x)-1)/x-1", min=1e-10, max=1e-6,
                           title=r"\textsf{\big(exp(x)-1\big)/x}"),
       [graph.style.symbol(symbol=graph.style.symbol.circle,
                           size=0.15*unit.v_cm,
                           symbolattrs=[deco.filled([color.rgb(0.2, 0.2, 1)]),
                                        deco.stroked([color.grey(1)])])])
g.plot(graph.data.function("y(x)=expm1(x)/x-1", min=1e-10, max=1e-6,
                           title=r"\textsf{expm1(x)/x}",
                           context={"expm1": expm1}),
       [graph.style.line([color.rgb(1, 0.5, 0), style.linewidth.Thick])])
g.writeGSfile("expm1.png", resolution=300)
