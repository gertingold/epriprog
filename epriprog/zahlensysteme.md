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

(anhang_zahlensysteme)=
# Anhang: Zahlensysteme

Im Alltag sind wir es gewohnt, Zahlen im Dezimalsystems anzugeben, das zehn
Ziffern benötigt. Da ein Computer Information nur in Form von Bits, die die
Werte Null oder Eins annehmen können, speichern kann, stehen zunächst nur zwei
Ziffern zur Verfügung. Dann ist es besser, im Dualsystem zu arbeiten, das wir
im {numref}`dualsystem` besprechen werden.

In der Praxis ist es häufig praktisch, einige Bits zusammenzufassen. In der
Praxis hat sich das Hexadezimalsystem bewährt, bei dem vier aufeinanderfolgende
Bits durch eine von insgesamt sechzehn Ziffern dargestellt werden. Dem
Hexadezimalsystem werden wir uns im {numref}`hexadezimalsystem` zuwenden. 

Häufig beschränken Programmiersprachen die Zahl der Bits, die verwendet werden,
um ein Integer darzustellen. Dadurch wird der darstellbare Zahlenbereich mehr
oder weniger eingeschränkt, und es kann durch eine Überschreitung des zulässigen
Zahlenbereichs zu Problemen durch einen so genannten *overflow* kommen. Obwohl
dies in Python diese Problematik bei Integers im Prinzip nicht kennt, muss man
sich ihrer bewusst sein, wenn man in Python Programmpakete wie NumPy oder SciPy
verwendet, die auch auf in C oder Fortran geschriebenen Programmen basieren.
Daher werden wir uns in {numref}`integertypes` verschiedene Arten von Integers
und die zugehörigen Zahlenbereiche ansehen.

(dualsystem)=
## Dualsystem

Bevor wir uns mit dem Dualsystem beschäftigen, ist es sinnvoll, sich noch einmal
die Funktionsweise des gewohnten Dezimalsystems zu vergegenwärtigen. Die durch
Ziffern markierten Stellen entsprechen von hinten nach vorne gelesen den Einern,
Zehnern, Hundertern usw. Ein Beispiel soll das verdeutlichen:

$$1234 = 1\cdot10^3+2\cdot10^2+3\cdot10^1+4\cdot10^0
       = 1\cdot1000+2\cdot100+3\cdot10+4\cdot1$$

Im Dualsystem werden die Zehnerpotenzen durch Zweierpotenzen ersetzt. Im folgenden
Beispiel geben die Indizes 2 und 10 das jeweilige Zahlensystem an.

$$\begin{align}
123_{10} &= 1\cdot10^2+2\cdot10^1+3\cdot10^0\\
 &= 1\cdot2^6+1\cdot2^5+1\cdot2^4+1\cdot2^3+0\cdot2^2+1\cdot2^1+1\cdot2^0\\
 &= 1\cdot64+1\cdot32+1\cdot16+1\cdot8+0\cdot4+1\cdot2+1\cdot1\\
 &= 1111011_2
\end{align}$$

Um diese Zerlegung zu erhalten, sucht man zunächst die höchste Zweierpotenz, die kleiner
gleich der vorgegebenen Zahl ist. Im Beispiel ist dies $64 = 2^6$. Nachdem man diese
Zahl abgezogen hat, geht man sukzessive zu kleineren Potenzen und erhält als Ziffer eine
0 oder 1 je nachdem ob die jeweilige Zweierpotenz größer als die betreffende Zahl ist oder
nicht. Man kann diese Aufgabe aber auch einfach Python überlassen. Die Umrechnung einer
Dezimalzahl in eine Dualzahl erfolgt mit Hilfe der {func}`bin`-Funktion. Unser Beispiel
würde man dann folgendermaßen umrechnen:

```{code-cell} python
bin(123)
```
Im Ergebnis deutet die führenden Null an, dass es sich um eine Zahl handelt, während das
`b` darauf hinweist, dass die Zahl im Dual- oder Binärsystem zu interpretieren ist. Gibt
man eine Binärzahl in die Codezelle eines Jupyter-Notebooks ein, so wird als Ausgabe die
entsprechende Dezimaldarstellung erzeugt.

```{code-cell} Python
0b1111011
```

Bis jetzt haben wir nur ganze Zahlen betrachtet. Genauso wie im Dezimalsystem kann man
aber auch im Dualsystem reelle Zahlen darstellen. Im Dezimalsystem werden nach dem Komma
die Zehnerpotenzen mit negativen Potenzen fortgesetzt. Es ist also beispielsweise

$$3{,}14 = 3\cdot10^0+1\cdot10^{-1}+4\cdot10^{-2} = 3\cdot1+1\cdot0{,}1+4\cdot0{,}01$$

Entsprechend haben wir im Dualsystem

$$0{,}11_2 = 1\cdot2^{-1}+1\cdot2^{-2} = 1\cdot 0{,}5+1\cdot0{,}25 = 0.75_{10}$$

Zu beachten ist, dass eine endliche Zahl von Nachkommastellen im Dezimalsystem im Allgemeinen
nicht bedeutet, dass auch im Dualsystem die Zahl der Nachkommastellen endlich ist, wie dieses
Beispiel verdeutlicht:

$$0{,}1_{10} = 0{,}0\overline{0011}_2$$

Hier deutet der Überstrich eine periodische Wiederholung der letzten vier Ziffern an. Da der
Computer nicht beliebig viele Stellen berücksichtigen kann, führt das Abschneiden von
Nachkommastellen zu Fehlern, den so genannten Rundungsfehlern, wie wir an anderer Stelle
noch sehen werden.

```{admonition} Aufgabe
Zeigen Sie, dass die angegebene Dualdarstellung der Dezimalzahl $0{,}1$ korrekt ist. 
Dabei kann es nützlich sein, an geometrische Reihen zu denken.
```

(hexadezimalsystem)=
## Hexadezimalsystem

In der Praxis hat das Dualsystem den Nachteil, dass die Zahlen relativ schwer lesbar sind.
Zum einen enthalten Binärzahlen lediglich die Ziffern 0 und 1 und zudem sind sie etwa
3,3-mal so lang wie die entsprechende Dezimaldarstellung. Daher fasst man häufig vier Bits
zusammen, die dann die Ziffern von 0 bis 15 darstellen können. Auf diese Weise erhält man
das Hexadezimalsystem, das die Basis 16 benutzt. In diesem System benutzt man wie gewohnt
die Ziffern 0 bis 9 und fährt dann mit den Buchstaben a bis f fort. Dabei spielt es 
keine Rolle, ob diese Buchstaben klein- oder großgeschrieben sind. 

| Dualsystem | Dezimalsystem | Hexadezimalsystem |
|:----------:| :-----------: |:-----------------:|
|   0000     |       0       |         0         |
|   0001     |       1       |         1         |
|   0010     |       2       |         2         |
|   0011     |       3       |         3         |
|   0100     |       4       |         4         |
|   0101     |       5       |         5         |
|   0110     |       6       |         6         |
|   0111     |       7       |         7         |
|   1000     |       8       |         8         |
|   1001     |       9       |         9         |
|   1010     |       10      |         a         |
|   1011     |       11      |         b         |
|   1100     |       12      |         c         |
|   1101     |       13      |         d         |
|   1110     |       14      |         e         |
|   1111     |       15      |         f         |

(integertypes)=
## Verschiedene Arten von Integers
