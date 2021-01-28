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
Python diese Problematik bei Integers im Prinzip nicht kennt, muss man
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

```{code-cell} python
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
die Ziffern 0 bis 9 und fährt dann mit den Buchstaben A bis F fort. Dabei spielt es 
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
|   1010     |       10      |         A         |
|   1011     |       11      |         B         |
|   1100     |       12      |         C         |
|   1101     |       13      |         D         |
|   1110     |       14      |         E         |
|   1111     |       15      |         F         |

Im vorigen Abschnitt hatten wir gesehen, dass die kleinste Informationseinheit in einem Computer
ein Bit ist, das die Werte 0 oder 1 annehmen kann. Häufig fasst man mehrere Bits zu einem Byte
zusammen, das normalerweise acht Bits umfasst. Da eine Ziffer im Hexadezimalsystem vier Bits entspricht,
lässt sich also ein Byte kompakt durch zwei Ziffern im Hexadezimalsystem darstellen. So ist zum
Beispiel

$$11110011_2 = \mathrm{F}3_{16} = 15\cdot16^1 + 3\cdot16^0 = 243_{10}$$

Die Umwandlung von einer Dezimal- in eine Hexadezimalzahl kann man in Python mit Hilfe der 
{func}`hex`-Funktion vorgenommen werden.

```{code-cell} python
hex(243)
```

Dabei zeigt das `x` nach der führenden Null das Hexadezimalformat an.

Genauso wie man eine Binärzahl in eine Dezimalzahl umwandeln kann,

```{code-cell} python
int(0b11110011)
```

geht dies auch für eine Hexadezimalzahl

```{code-cell} python
int(0xf3)
```

Die Art der Zahl wird an dem `b` bzw. `x` erkannt. Dabei ist es irrelevant,
ob das `x` klein oder groß geschrieben ist. Gleiches gilt, wie schon gesagt,
auch für die Hexadezimalziffern.

```{code-cell} python
int(0xF3), int(0Xf3), int(0XF3)
```

Der Vollständigkeit halber sei erwähnt, dass Python auch mit Zahlen im Oktalsystem mit 
der Basis 8 arbeiten kann, in dem die Ziffern zwischen 0 und 7 liegen. Allerdings ist
das Hexadezimalsystem zur Angabe von Bytes am geeignetsten.

(integertypes)=
## Verschiedene Arten von Integers

Nachdem wir nun mit dem Dual- und dem Hexadezimalsystem vertraut sind, können wir uns
verschiedenen Arten von Integers und den von ihnen abgedeckten Zahlenbereichen zuwenden.

Zunächst kann man sich fragen, warum nicht alle Programmiersprachen zumindest
im Prinzip beliebig große Integers zulassen. Hierfür gibt es zwei wesentliche
Gründe. Ältere Programmiersprachen wurden zu einer Zeit entwickelt als Speicher
in Computern eine knappe Ressource war. Man hat damals also versucht, mit so wenig
Speicher auszukommen wie es von der entsprechenden Anwendung erfordert wurde.

Ein weiterer Grund wird vor allem dann relevant, wenn man eine ganze Reihe von Objekten
verarbeiten will. Gerade bei numerischen Problemen hat man es ja oft mit Vektoren oder
Matrizen zu tun. Wenn alle Einträge in einem Vektor oder einer Matrix die gleiche
Speichergröße erfordern, kann man sehr leicht ausrechnen, wo sich ein bestimmter Eintrag
im Speicher befindet, und damit schnell darauf zugreifen. Gerade in Sprachen wie Fortran
und C, die nicht wie Python den Code zeilenweise interpretieren, sondern den gesamten
Code mehr oder weniger genau analysieren, ist es mit der Kenntnis über die Größe von
Objekten im Speicher möglich, die Ausführungsgeschwindigkeit eines Programms zu optimieren.

Um das Prinzip zu verstehen, beginnen wir mit den kleinsten Integers und verzichten zunächst
auf negative Zahlen. Man spricht dann von »unsigned char«, die aus einem einzigen Byte bestehen.
Python erlaubt es uns, die interne Darstellung leicht zu bestimmen, wobei uns hier nur das
Ergebnis interessieren soll.

```{code-cell} python
from struct import pack
pack('>B', 123).hex()
```
Dieses Ergebnis lässt sich leicht nachvollziehen

$$\begin{align}
7\mathrm{b}_{16} &= 7\cdot16^1+11\cdot16^0\\
                 &= 112+11\\
                 &= 123
\end{align}$$

Die größte Zahl, die man mit einem Byte darstellen kann, ist $2^{8}-1=255$.
```{code-cell} python
pack('>B', 2**8-1).hex()
```
Was passiert, wenn man versucht, $2^{8}$ als »unsigned char« darzustellen?
```{code-cell} python
---
tags: [raises-exception]
---
pack('>B', 2**8).hex()
```
Diese Zahl ist nicht mehr in einem Byte darstellbar, sondern erfordert zwei
Bytes: `0x0100`.  Python bricht daher mit einer Fehlermeldung ab. Dieses
Verhalten ist jedoch nicht selbstverständlich.  In manchen Programmiersprachen
wird einfach die 1 im führenden Byte ignoriert, was zur Folge hat, dass $2^8$
stillschweigend auf $0$ abgebildet wird. Man spricht hier von einem Überlauf.
Diesen sollte man tunlichst vermeiden, da die Numerik sonst fehlerhafte
Ergebnisse liefert.

Neben dem gerade besprochenen Integerformat »unsigned char« gibt es auch
»signed char«, das auch negative Zahlen zulässt. Dabei wird das Vorzeichen im
höchsten Bit, in unserer Darstellung also ganz links, gespeichert.
Dementsprechend sind positive Zahlen von $0$ mit $2^{7}-1$ darstellbar.
```{code-cell} python
pack('>b', 2**7-1).hex()
```
Hier ist das vordere Bit gleich $0$, während alle anderen Bits gleich $1$ sind.
$2^7$ würde dazu führen, dass das erste Bit gleich $1$ wird, was aber eine
negative Zahl anzeigen würde.

Um die Darstellung negativer Zahlen besser zu verstehen, vergleichen wir die Art wie $1$ und $-1$
abgespeichert werden.
```{code-cell} python
pack('>b', 1).hex(), pack('>b', -1).hex()
```
Anders als man erwarten könnte, unterscheiden sich die beiden Darstellungen nicht einfach im führenden
Bit. Vielmehr ist die Darstellung so gewählt, dass sich beim Zusammenzählen tatsächlich Null ergibt.

      0000 0001
      1111 1111
    -----------
    1 0000 0000 

Hier muss man bei der Addition berücksichtigen, dass im Dualsystem $1+1 = 10_2$
gibt, also $0$ mit einem Übertrag von $1$. Die letzte Übertrag wird durch die
Beschränkung auf ein Byte einfach ignoriert, und wir erhalten somit als Ergebnis
Null, wie es auch sein muss.

Wie erhält man nun aus einer positiven Zahl die zugehörige negative Zahl? Die
Antwort ist das so genannte Zweierkomplement. Hierbei werden zunächst alle
Nullen durch Einsen ersetzt und umgekehrt. Dieses Zwischenergebnis wird
Einserkomplement genannt. Anschließend wird zu dem Ergebnis noch $1$ addiert.
Sehen wir uns das an einem Beispiel an. Betrachten wir als Beispiel die Zahl
mit der Hexadezimaldarstellung 7b, die, wie wir schon wissen, im Dezimalsystem
gleich 123 ist. Zunächst erhalten wir für das Einserkomplement

    0111 1011 → 1000 0100

und dann durch Addition von Eins

    1000 0100 → 1000 0101

Die Addition der beiden Zahlen ergibt erwartungsgemäß Null

      0111 1011
      1000 0101
    -----------
    1 0000 0000

Dass wir das Zweierkomplement richtig bestimmt haben, sieht man mit Hilfe von Python
wenn man in der folgenden Ausgabe entsprechend unserer vorigen Beschränkung auf
ein einziges Byte das vordere Byte ignoriert.
```{code-cell} python
pack('>b', 123).hex(), pack('>b', -123).hex()
```

```{admonition} Aufgabe

Zeigen Sie, dass die Addition einer Zahl und ihres Zweierkomplements immer Null
ergibt, wenn man den Übertrag, der zum Überlauf führt, ignoriert.
```

Da das erste Bit für das Vorzeichen benötigt wird, ist die größte positive Zahl,
die sich mit einem »signed char« Integer darstellen lässt, gleich $2^7-1$. Die Zahl
$2^7$ kann dagegen nicht mehr dargestellt werden.
```{code-cell} python
---
tags: [raises-exception]
---
pack('>b', 2**7).hex()
```
Andererseits kann $-2^7$ gerade noch dargestellt werden:
```{code-cell} python
pack('>b', -2**7).hex()
```
Wenn man das Zweierkomplement bildet, stellt man fest, dass diese Zahl gleich
ihrem Negativen ist. Dabei handelt es sich um ein Artefakt des
Zweierkomplements. Im Einserkomplement hätte man dagegen unterschiedliche
Darstellungen für die Null und ihr Negatives. 

Durch den kleinen Zahlenbereich $-128\ldots127$ ist ein Byte selten für
numerische Arbeiten ausreichend. Typischerweise wird man dann zwei, vier oder
gar acht Bytes investieren, um Integers darzustellen. Damit wird der
darstellbare Zahlenbereich erheblich größer, wie die {numref}`table:ints`
zeigt. Die dort gezeigten Bezeichnungen werden so im
[struct-Modul](https://docs.python.org/3/library/struct.html) von Python
verwendet. Die einzelnen Bezeichnungen können in anderen Programmiersprachen
unter Umständen abweichend definiert sein.

```{list-table} Integerformate wie sie von Pythons [struct-Modul](https://docs.python.org/3/library/struct.html) verwendet werden
:header-rows: 1
:name: table:ints

* - Name
  - Format
  - Bytes
  - Minimalwert
  - Maximalwert
* - unsigned char
  - B
  - 1
  - 0
  - 255
* - signed char
  - b
  - 1
  - -128
  - 127
* - unsigned short
  - H
  - 2
  - 0
  - 65535
* - short
  - h
  - 2
  - -32768
  - 32767
* - unsigned int
  - I
  - 4
  - 0
  - 4294967295
* - int
  - i
  - 4
  - -2147483648
  - 2147483647
* - unsigned long
  - L
  - 4
  - 0
  - 4294967295
* - long
  - l
  - 4
  - -2147483648
  - 2147483647
* - unsigned long long
  - Q
  - 8
  - 0
  - 18446744073709551615
* - long long
  - q
  - 8
  - -9223372036854775808
  - 9223372036854775807
```


````{admonition} Weiterführender Hinweis
Das Größerzeichen `>` im ersten Argument der {func}`pack`-Funktion verlangt, dass die niedrigeren
Stellen des Ergebnisses wie gewohnt weiter rechts stehen. Tatsächlich ist dies auf den üblichen
Intelarchitekturen nicht der Fall. Davon kann man sich überzeugen, wenn man das `>` durch `@`
ersetzt. Dadurch dreht sich die Reihenfolge der Bytes, nicht der Bits, gegebenenfalls um.
````
