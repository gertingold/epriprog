---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(scipy)=
# Numerische Programmbibliotheken am Beispiel von NumPy/SciPy

```{admonition} Hinweis
:class: warning
Dieses Kapitel befindet sich noch in Bearbeitung.
```

In den bisherigen Kapiteln hatten wir immer wieder Gelegenheit, auf
Möglichkeiten hinzuweisen, die die Python-Standardbibliothek bietet. Wenn man
die dort zur Verfügung gestellten Module verwendet, kann man sich Einiges an
Arbeit sparen und dabei auch den Code effizienter und übersichtlicher
gestalten.  Neben der Python-Standardbibliothek gibt es aber auch noch viele
interessante Programmpakete, die häufig über den [Python Package
Index](https://pypi.org/) zur Verfügung gestellt werden.

Gerade für Problemstellungen in den Natur- und Ingenieurwissenschaften gibt es
eine oft als *scientific ecosystem of Python* oder *scientific stack*
bezeichnete Sammlung von zentralen Paketen. Hierzu gehört als Basispaket
zunächst [NumPy](http://numpy.org/), das den Datentyp `ndarray` sowie Methoden
zur Verfügung stellt, um mit `ndarray`-Objekten zu arbeiten. Damit wird das
Rechnen mit Vektoren und Matrizen ermöglicht, das wir bei der Besprechung von
Listen in {numref}`listen` vermisst hatten.

Ein weiteres wichtiges Paket ist [SciPy](https://docs.scipy.org/doc/scipy/reference/), das vielfältige numerische Werkzeuge zur Verfügung stellt, beispielsweise
zur numerischen Integration oder der Lösung von Differentialgleichungssystemen,
zur Lösung von Optimierungsproblemen oder zur Berechnung von speziellen 
Funktion sowie vielem Anderem mehr. In diesem Kapitel werden wir einen
ersten Eindruck von den Möglichkeiten geben, die NumPy und SciPy bereitstellen.

Weitere zentrale Pakete, die in diesem Zusammenhang zu nennen sind, wären
[Matplotlib](http://matplotlib.org/) zur graphischen Darstellung von Daten,
[IPython](http://ipython.org/), eine interaktive Python-Konsole, die für das
[Projekt Jupyter](https://jupyter.org/), das unter anderem die Jupyter
Notebooks zur Verfügung stellt, von zentraler Bedeutung war und ist,
[SymPy](http://sympy.org/) für das symbolische Rechnen sowie das im
{numref}`readfile` bereits erwähnte [pandas](http://pandas.pydata.org/),
das fortgeschrittene Datenstrukturen und vielfältige Methoden zu einer
effizienten Datenanalyse bereithält.

Auf der Basis dieser Pakete haben einzelne wissenschaftliche Disziplinen
umfangreiche, auf ihre speziellen Bedürfnisse zugeschnittene Programmpakete
entwickelt. So kann [Astropy](https://www.astropy.org/) als Standard in der
Astronomie angesehen werden. [QuTiP](http://qutip.org/), die *Quantum Toolbox
in Python* erlaubt die Simulation von Qauntensystemen. Für Problemstellungen,
die sich mit finite-Elemente-Methoden lösen lassen, steht
[FEniCS](https://fenicsproject.org/) zur Verfügung. Diese Aufzählung könnte
fast beliebig fortgesetzt werden und soll nur dazu dienen, einen allerersten
Eindruck von der Vielfalt der zur Verfügung stehenden
Python-Programmbibliotheken zu geben.

````{margin}
```{seealso} 
Quellen für hier besprochene Programmpakete:
[NumPy auf Github](https://github.com/numpy/numpy),
[SciPy auf Github](https://github.com/scipy/scipy)
```
````

Nachdem die Benutzung professioneller Programmpakete gelegentlich mit hohen
Kosten verbunden sein kann, ist es erwähnenswert, dass die hier aufgeführten
Pakete frei verfügbar, aber dennoch von sehr hoher Qualität sind. Zwei Beispiele
prominenter Forschungsprojekte, deren Arbeit wesentlich auf einigen der hier
genannten Pakete, sind in {numref}`warumpython` genannt. Darüber hinaus ist
der Quellcode der Pakete verfügbar, so dass man sich bei Bedarf auch die
konkrete Implementierung ansehen sowie zur Weiterentwicklung beitragen kann.

## Installation

Da NumPy und SciPy nicht in der Python-Standardbibliothek enthalten sind, stehen
diese Programmpakete auch bei einer vorhandenen Python-Installation nicht
automatisch zur Verfügung. Dies lässt sich leicht überprüfen, indem man versucht,
die beiden Pakete zu importieren. Schlägt dies fehl, so erhält man einen
`ImportError`, der impliziert, dass Python die Pakete nicht finden kann.
Außerdem lässt sich die installierte Version anzeigen, was deswegen interessant
sein kann, weil gelegentlich neue Funktionalität zu den Paketen hinzugefügt
wird. Beachten Sie, dass vor und nach `version` jeweils zwei Unterstriche
stehen müssen.
```{code-cell} python
import numpy
import scipy

print(f'{numpy.__version__ = }')
print(f'{scipy.__version__ = }')
```
Eine einfache und empfehlenswerte Möglichkeit, NumPy und SciPy unter Windows,
MacOS oder Linuxvarianten wie Ubuntu verfügbar zu machen, besteht darin, die
[Anaconda-Distribution](https://www.anaconda.com/products/individual) zu
installieren. Dabei werden allerdings gleichzeitig zahlreiche andere, für
wissenschaftliche Zwecke interessante Programmpakete installiert.  Ist dies
nicht erwünscht, zum Beispiel wegen des relativ großen Bedarfs an
Speicherplatz, kann man NumPy und SciPy auch gezielt auf einem der Wege
installieren, die in der [Installationsanleitung für
NumPy](https://numpy.org/install/) und der [Installationsanleitung für
SciPy](https://www.scipy.org/install.html) beschrieben sind.

## Arrays und Anwendungen

## Numerische Integration

## Integration gewöhnlicher Differentialgleichungen
