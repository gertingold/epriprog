---
file_format: mystnb
kernelspec:
  name: python3
---

(anhang_floats)=
# Anhang: 64-Bit-Gleitkommazahlen nach IEEE-Standard 754

In diesem Anhang soll kurz die Binärdarstellung von 64-Bit-Gleitkommazahlen
nach dem [IEEE Standard for Floating-Point Arithmetic IEEE Std
754–2008](http://dx.doi.org/10.1109/IEEESTD.2008.4610935) vorgestellt werden.
Dabei handelt es sich nur um einen sehr kleinen Ausschnitt dieses Standards,
der noch weitere Gleitkommazahlenformate sowie deren arithmetische Verarbeitung
definiert.

Wie in der folgenden Abbildung zu sehen ist, besteht eine 64-Bit-Gleitkommazahl aus drei
Anteilen: 1 Bit für das Vorzeichen, 11 Bits aus denen der Exponent bestimmt wird, sowie
52 Bits aus denen sich die Mantisse ergibt. Im zweiten und dritten Segment steht das 
höchstwertigste Bit (MSB – `most significant bit`) jeweils links und das niederwertigste 
Bit (LSB – `least significant bit`) rechts.

```{figure} images/ieee754/ieee754_64.png
---
height: 4cm
name: fig:ieee754
---
64-Bit-Gleitkommazahl nach IEEE-Standard 754.
```

Die Interpretation der 64 Bits hängt vom Wert des Exponenten E ab, der als Integer zu
verstehen ist und damit Werte zwischen $0$ und $2^{11}-1$ annehmen kann. 

Wir beginnen mit dem häufigsten Fall, dass E ungleich $0$ und ungleich
$2^{11}-1$ ist, also einen Wert zwischen $1$ und $2^{11}-2$ besitzt.
In diesem Fall liegt eine so genannte normalisierte Zahl vor, für die die 64
Bits in folgender Weise zu interpretieren sind. Ist das Vorzeichenbit gleich 0,
so handelt es sich um eine positive Zahl, andernfalls um eine negative Zahl. Um
den tatsächlichen Exponenten zu erhalten, muss man von E den Wert
$2^{10}-1=1023$ abziehen. Damit resultiert im Binärsystem ein Faktor, der
zwischen $2^{-1022}$ und $2^{1023}$ liegt. Die Mantisse ist als
Nachkommaanteil im Binärsystem zu interpretieren, wobei implizit eine führende
$1$ vor dem Komma steht. 

Ein Beispiel soll diese Kodierung verdeutlichen. Konkret sehen wir uns die Zahl
$-25{,}640625$ an, die wir mit Hilfe von Python in die gewünschte Codierung
umrechnen lassen können. Anschließend werden wir uns umgekehrt überlegen, dass
die Interpretation der Hexadezimaldarstellung tatsächlich die Ausgangszahl ergibt.
```{code-cell} python
from struct import pack
pack('>d', -25.640625).hex()
```

{numref}`fig:ieee_example` zeigt die entsprechenden Bits des Vorzeichens, des
Exponenten und der Mantisse, die farblich unterschiedlich hinterlegt sind.

```{figure} images/ieee754/ieee_example.png
---
name: fig:ieee_example
---
Bitweise Darstellung der Zahl $-25{,}640625$ nach dem IEEE-Standard 754. Das Vorzeichenbit,
die Bits des Exponenten und die Bits der Mantisse sind farblich orange, grün bzw.
violett hinterlegt.
```

````{margin}
```{admonition} Hinweis
Die Funktionsweise des Dualsystems ist in {numref}`dualsystem` beschrieben.
```
````

Das erste, orange hinterlegte Bit gibt an, dass es sich um eine negative Zahl handelt.
Die folgenden 11 Bit ergeben

$$2^{10}+2^1+2^0 = 1027\,.$$

Subtrahiert man $1023$, so ergibt sich für die kodierte Zahl ein Faktor
$2^4=16$. Die restlichen Bits ergeben die Mantisse mit dem Wert

$$2^{-1}+2^{-4}+2^{-5}+2^{-7}+2^{-10} = 0{,}6025390625\,.$$

Berücksichtigt man die führende implizite Eins bei normalisierten Zahlen, so
ergibt sich insgesamt $-16\times 1{,}6025390625 = -25{,}640625\,.$

Falls der Exponent E seinen Maximalwert, für 64-Bit-Gleitkommazahlen also 2047,
annimmt, hängt die Interpretation vom Mantissenfeld ab. Enthält dieses den Wert
Null, so ist die Zahl unter Berücksichtigung des Vorzeichenbits als +∞ oder -∞
zu interpretieren. Ist das Mantissenfeld dagegen ungleich Null, so ergibt sich
der Wert NaN (Not a Number).

Hat der Exponent E seinen Minimalwert Null und ist zugleich die Mantisse T
gleich Null, so liegt je nach Wert des Vorzeichenbits die Zahl 0 oder -0 vor.
Ist dagegen die Mantisse T von Null verschieden, so hat man es mit einer so
genannten denormalisierten Zahl zu tun. Denormalisierte Zahlen wurden
eingeführt, weil der Minimalwert einer normalisierten 64-Bit-Gleitkommazahl
betragsmäßig gleich $2^{-1022}\approx 2,225\cdot 10^{-308}$ ist. Zwischen
dieser Zahl und Null existiert somit eine Lücke, die man im Rahmen der
Möglichkeiten einer 64-Bit-Gleitkommazahl zu füllen versucht. Im Gegensatz zu
normalisierten Zahlen, bei denen eine implizite Eins vor den Nachkommaanteil zu
setzen war, steht bei denormalisierten Zahlen vor dem Komma eine Null. Da damit
der sich aus dem Mantissenfeld ergebende Faktor kleiner als Eins ist, eröffnet
sich die Möglichkeit Zahlen darzustellen, die kleiner als die kleinst mögliche
normalisierte Zahl sind. Allerdings geht dies auf Kosten der Anzahl
signifikanter Ziffern, die bei denormalisierten Zahlen kleiner ist als bei
normalisierten Zahlen. Damit die denormalisierten Zahlen nahtlos an die
normalisierten Zahlen anschließen, ist der sich normalerweise aus dem
Exponentenfeld ergebende Faktor gleich dem kleinsten Faktor für normalisierte
Zahlen, also $2^{1-1023} = 2^{-1022}$.

Wir charakterisieren abschließend die 64-Bit-Gleitkommazahlen durch einige ihrer
Eigenschaften. Die kleinste darstellbare Zahl größer als Null ist 
$2^{-1022}\times 2^{-52} = 2^{-1074} \approx 4,941\cdot 10^{-324}$.
Die größte darstellbare endliche Zahl ist

$$2^{1023}\times\big(1+(1-2^{-52})\big) \approx 1{,}798\cdot 10^{308}\,.$$

```{code-cell} python
import sys
sys.float_info.max
```

Der Abstand zwischen der Zahl Eins und der nächst größeren
darstellbaren Zahl beträgt

$$2^{-52} \approx 2{,}22\cdot 10^{-16}\,.$$

```{code-cell} python
sys.float_info.epsilon
```

Mit ``sys.float_info.min`` erhält man nicht die kleinste überhaupt darstellbare Zahl,
sondern die kleinste darstellbare normalisierte Zahl {math}`2^{-1022}`.

```{code-cell} python
sys.float_info.min
```
