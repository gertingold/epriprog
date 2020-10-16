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

(datentypen)=
# Einfache Datentypen, Variablen und Zuweisungen

In {numref}`vorschau` hatten wir bereits verschiedene Datentypen kennengelernt.
Hierzu gehören ganze Zahlen, die zum einen durch die explizite Umwandlung der
Benutzereingabe in eine ganze Zahl oder als Ergebnis der
{func}`randrange`-Funktion erzeugt wurden. Des Weiteren kamen Wahrheitswerte
vor. Ganz explizit war dies bei `True` der Fall, das zur Konstruktion einer
Dauerschleife verwendet wurde.

Diese beiden Datentypen, ganze Zahlen und Wahrheitswerte gehören zu den
einfachen Datentypen. Daneben gibt es auch zusammengesetzte Datentypen, für die
wir in {numref}`vorschau` ebenfalls schon Beispiele gesehen hatten. Dazu
gehören die Zeichenketten, zum Beispiel in den Zeilen 12 bis 15 des
Beispielprogramms, aber auch die durch eckige Klammern
gekennzeichnete Liste in Zeile 11.

In diesem Kapitel werden wir uns zunächst den einfachen Datentypen zuwenden und
die zusammengesetzten Datentypen in einem späteren Kapitel besprechen. Dabei
werden wir vor allem neben den ganzen Zahlen noch weitere numerische Datentypen
kennenlernen, die für natur- und ingenieurwissenschaftliche Anwendungen große
Bedeutung besitzen.

(integers)=
## Ganze Zahlen

Wir beginnen bei der Besprechung der numerischen Datentypen mit den ganzen
Zahlen, auf Englisch *integers*. Auf den ersten Blick könnte man denken, dass
in den Natur- und Ingenieurwissenschaften ganze Zahlen gegenüber den reellen
Zahlen eigentlich unwichtig sind. Auch wenn diese Einschätzung nicht ganz
falsch ist, verwenden wir auch in diesen Bereichen relativ oft ganze Zahlen,
zum Beispiel als Index für eine Vektor- oder Matrixkomponente. Beim
Programmieren spielen ganze Zahlen daher unter anderem eine große Rolle, sobald
etwas gezählt oder indiziert werden muss. Eine weitere Anwendung ganzer Zahlen
ergibt sich speziell in Python daraus, dass im Prinzip betragsmäßig beliebig
große ganze Zahlen dargestellt werden können. Dies ermöglicht es, Rechnungen
mit beliebiger Genauigkeit durchzuführen.

Die gerade angesprochene Frage, welche Zahlen überhaupt in einer Programmiersprache
dargestellt werden können, ist von großer Bedeutung. Es lohnt sich daher, sich
etwas genauer damit zu beschäftigen. Zahlen werden, wie andere Objekte auch, im
Computer intern immer mit Hilfe von Nullen und Einsen dargestellt. Begrenzt man
den Speicherplatz je Zahl, so ist der darstellbare Zahlenbereich eingeschränkt.
Daher werden wir im Folgenden statt von »ganzen Zahlen«, die wir für das mathematische
Objekt verwenden wollen, lieber von »Integers« sprechen, die sich auf die im
Computer realisierbaren Zahlen beziehen.

Die Frage nach den im Computer darstellbaren Zahlen ist insofern wichtig, als
ein Überschreiten des Zahlenbereichs zu Problemen führt. Bei den
Gleitkommazahlen, die wir im nächsten Kapitel besprechen werden, führt eine
begrenzte Zahl von Nachkommastellen zusätzlich zu dem Problem von
Rundungsfehlern.

Doch kommen wir zurück zu den Integers. Wenn Python im Prinzip betragsmäßig
beliebig große Zahlen erlaubt, könnte man meinen, dass man sich um die Größe
des Zahlenbereichs nicht weiter kümmern muss. Das ist allerdings nicht ganz
richtig.  Zum einen ist jeder reale Computerspeicher begrenzt, so dass der
Zahlenbereich letztlich doch eingeschränkt ist. In der Praxis spielt diese
Einschränkung kaum eine Rolle, sondern eher die Zeit, die eine Rechenoperation
mit sehr großen Integers benötigt. In anderen Programmiersprachen dagegen ist
der Bereich der möglichen Integers eingeschränkt. Da die für uns wichtigen
numerischen Programmbibliotheken NumPy und SciPy zu großen Teilen auf in C oder
Fortran geschriebenen Programmen basieren, werden dort auch unter Python die
Einschränkungen des Zahlenbereichs wichtig. Zu erwähnen wäre noch, dass die Integers,
die als Index zur Adressierung in Listen oder Zeichenketten verwendet werden
können, auch in Python beschränkt sind. Allerdings wird diese Beschränkung auf
modernen Computern selten ein Problem darstellen.

Wie ganze Zahlen im Computer dargestellt werden und was das für die
größenmäßige Einschränkung des Zahlenbereichs bedeutet, werden wir in einem
Anhang in {numref}`anhang_zahlensysteme` diskutieren.  Dort werden auch die
Grundlagen des Dualsystems erklärt, das der Darstellung von Zahlen mit Hilfe
von Nullen und Einsen zugrunde liegt. Hier wollen wir uns nun stärker der
praktischen Arbeit mit Integers zuwenden.

Als erstes wollen wir zeigen, dass Integers in Python tatsächlich sehr groß werden
können, indem wir die tausendste Potenz von 2 ausrechnen lassen. Der doppelte Stern
`**` steht dabei für den Exponentiationsoperator.

```{code-cell} python
2**1000
```

Das Ergebnis hat 302 Stellen. Genauso gut könnte man als Exponenten 100000 wählen
und würde dann ein Ergebnis mit 30103 Stellen erhalten.

Natürlich gibt es neben positiven Integers auch solche mit negativem Vorzeichen.

```{code-cell} python
2**100 - 2**101
```
Die Leerzeichen um das Minuszeichen der Eingabe spielen für den Pythoninterpreter
keine Rolle, sondern dienen hier der besseren Lesbarkeit.

In Python kann man auch mit Dual-, Oktal- und Hexadezimalzahlen arbeiten. Eine
Einführung in Zahlensysteme, insbesondere das Dual- und das Hexadezimalsystem
wird in {numref}`anhang_zahlensysteme` gegeben. Um zwischen den verschiedenen
Zahlensystemen unterscheiden zu können, werden Präfixe verwendet, und zwar
``0b`` oder ``0B`` für das Dualsystem, ``0o`` oder ``0O`` für das Oktalsystem
sowie ``0x`` oder ``0X`` für das Hexadezimalsystem. Die folgenden drei Darstellungen
sind jeweils äquivalent zur Zahl 25 im gewohnten Dezimalsystem

```{code-cell} python
0b11001, 0o31, 0x19
```

Die Umwandlung in das Binär-, Oktal- oder Hexadezimalformat erfolgt mit Hilfe der
Funktionen ``bin``, ``oct`` bzw. ``hex``:

```{code-cell} python
bin(25), oct(25), hex(25)
```
Das Ergebnis ist allerdings keine Zahl, sondern eine Zeichenkette, wie an den
einschließenden Hochkommas zu erkennen ist.

Bei den meisten grundlegenden mathematischen Operationen wie Addition, Subtraktion,
Multiplikation und Exponentiation ist gewährleistet, dass bei der Anwendung auf
ganze Zahlen das Ergebnis wieder eine ganze Zahl ist. Eine Ausnahme ist die Division,
da nicht klar ist, dass sich der Dividend durch den Divisor ohne Rest teilen lässt.

Um fehlerhafte Programme zu vermeiden, ist es daher wichtig zu wissen, wie die
verwendete Programmiersprache die Division handhabt. Prinzipiell gibt es zwei
Möglichkeiten. Eine Möglichkeit besteht darin, bei der Division von zwei ganzen
Zahlen wieder eine ganze Zahl zu erzeugen und einen eventuell entstehenden Rest
zu ignorieren. Bei der anderen Möglichkeit wird der Quotient als Gleitkommazahl
dargestellt. Keine der beiden Varianten ist besser als die andere, so dass es für 
eine Programmiersprache auch keine natürliche Wahl gibt. Tatsächlich hat sich
Python in der Version 2 an dieser Stelle anders verhalten als die Version 3, die
wir heute benutzen.

Sehen wir uns an, wie Python 3 mit der Division von zwei Integers umgeht.
```{code-cell} python
1/2
```
```{code-cell} python
15/3
```
Offenbar wird hier immer eine Gleitkommazahl erzeugt, was an dem Dezimalpunkt
ersichtlich ist. Dies gilt auch, wenn der Quotient wie im zweiten Fall im
Prinzip als ganze Zahl darstellbar wäre.

Gelegentlich benötigt man aber eine Ganzzahldivision. In Python 3 erhält man diese
mit einem doppelten Schrägstrich.
```{code-cell} python
1//2
```
```{code-cell} python
15//7
```
```{code-cell} python
-15//7
```

```{admonition} Frage
Was macht der ``//``-Divisionsoperator in Python 3 tatsächlich, vor allem vor dem
Hintergrund des letzten Beispiels? [^gvr_blog]

[^gvr_blog]: Die Hintergründe für diese Wahl kann man in einem
    [Blog-Artikel](http://python-history.blogspot.de/2010/08/why-pythons-integer-division-floors.html)
    von Guido van Rossum nachlesen.
```

Um zu verdeutlichen, dass die in Python 3 getroffene Wahl nicht zwingend ist,
sehen wir uns zum Vergleich die Division in der Programmiersprache C an.
Hier liefert
```{code-block} C
#include <stdio.h>

int main(void) {
  printf("%d %d\n", 15/7, -15/7);
}
```
als Ergebnis
```
2 -2
```
Im Gegensatz zu Python 3 führt in C die Division zweier Integers wieder auf einen
Integer. Zudem wird hier zur Null hin abgeschnitten. Im zweiten Fall ergibt sich also
nicht -3 wie bei Python 3, sondern -2. Genauso verhält sich auch der entsprechende
Fortran-Code
```{code-block} fortran
program division
  write(*, *) 15/7, -15/7
  write(*, *) 1/2, 1.0/2
end program division
```
mit dem Ergebnis
```
           2          -2
           0  0.500000000
```
Die zweite Ausgabezeile illustriert, dass man hier eine Gleitkommadivision
erzwingen kann, indem man mindestens eine der beiden Zahlen zu einer Gleitkommazahl
macht.

Kommen wir nach diesem Ausflug zu anderen Programmiersprachen wieder zurück zu
Python. Oft ist man am Rest einer Integerdivision interessiert. Diesen könnte man
im Prinzip folgendermaßen erhalten
```{code-cell} python
zaehler = 15
nenner = 4
rest = zaehler - (zaehler//nenner)*nenner
print(rest)
```
Mit Hilfe des Modulo-Operators `%` von Python geht dies jedoch einfacher.
```{code-cell} python
zaehler = 15
nenner = 4
print(zaehler % nenner)
```
Eine häufige Anwendung ist der Test auf eine gerade oder ungerade Zahl.
```{code-cell} python
16 % 2
```
Ist die Zahl ohne Rest durch 2 teilbar, ist sie offenbar gerade, ansonsten ungerade.
```{code-cell} python
17 % 2
```
Benötigt man sowohl den Quotienten als auch den Rest, so kann man in Python beides
in einem Schritt mit Hilfe der {func}`divmod`-Funktion erhalten
```{code-cell} python
quotient, rest = divmod(42, 5)
print(quotient, rest)
```

Ein weiterer wichtiger Punkt, der hier für Integers zum ersten Mal auftritt, aber
viel weitreichendere Bedeutung hat, ist die Reihenfolge, in der Operationen 
ausgeführt werden. In dem folgenden Beispiel sehen wir, dass in Python ebenso wie
in C und Fortran die Regel Punkt vor Strich gilt.

```{code-cell} python
2+3*4
```
Der Ausdruck wird also nicht von links nach rechts abgearbeitet. Möchte man zuerst
die Addition ausführen, so muss man Klammern setzen.
```{code-cell} python
(2+3)*4
```

Die wichtigsten für Python geltenden Vorrangregeln sind in der {numref}`table:precedence`
dargestellt. Dabei haben die weiter oben stehenden Operationen Vorrang vor den nachfolgenden
Operationen [^precedence].

```{list-table} Die weiter oben in der Liste stehenden Operationen haben Vorrang vor den weiter unten stehenden.
:header-rows: 1
:name: table:precedence

* - Operatoren
  - Beschreibung
* - **
  - Exponentiation
* - +x, -x
  - Positives und negatives Vorzeichen
* - *, /, //, %
  - Multiplikation, Division, Modulo
* - +, -
  - Addition, Subtraktion
```

[^precedence]: Eine vollständige Liste, die auch noch nicht besprochene Operatoren umfasst, findet
    man unter dem Punkt [Operator precedence](http://docs.python.org/3/reference/expressions.html#operator-precedence)
    in der Python-Dokumentation. Beachten Sie, dass die dortige Tabelle umgekehrt geordnet ist, also
    weiter unten stehende Operatoren Vorrang haben.

Auch wenn das folgende Beispiel Gleitkommazahlen involviert, sei angemerkt,
dass falls der Exponentiationsoperator``**`` direkt von einem Plus oder Minus
gefolgt, das Vorzeichen stärker bindet.

```{code-block} python
>>> 2**-0.5
0.7071067811865476
```

Stehen Operatoren auf der gleichen Stufe, so wird der Ausdruck von links nach
rechts ausgewertet. Gegebenenfalls müssen Klammern verwendet werden, um die
gewünschte Reihenfolge sicherzustellen. Es spricht auch nichts dagegen, im
Zweifelsfall oder zur besseren Lesbarkeit Klammern zu setzen, selbst wenn diese
nicht zur korrekten Abarbeitung des Ausdrucks erforderlich sind.

```{admonition} Frage
Was ergibt ``-2*4+3**2``? Was ergibt ``6**4//2``?
```

(float)=
## Gleitkommazahlen

Eine zentrale Rolle in der wissenschaftlichen Numerik spielen Gleitkommazahlen,
die häufig auch mit dem englischen Begriff als *Floats* bezeichnet werden. 
Wir werden diesen Begriff gelegentlich verwenden, insbesondere um den Unterschied
zum mathematischen Begriff der reellen Zahlen deutlich zu machen. Wesentlich ist
dabei, dass sowohl der Zahlenbereich der Floats als auch die Zahl der
Nachkommastellen begrenzt sind.

Während man sich beim normalen Rechnen per Hand üblicherweise keine
Rechenschaft darüber ablegen muss, ob eine Zahl eine ganze Zahl oder eine
Gleitkommazahl ist, ist dies beim numerischen Arbeiten anders. Im {numref}`integers`
hatten wir ja schon gesehen, dass der Datentyp bei der Division durchaus eine Rolle
spielen kann.

An dieser Stelle müssen wir wieder einmal auf Unterschiede zwischen Programmiersprachen
hinweisen. In Sprachen wie C und Fortran muss der Datentyp einer Variable festgelegt
werden. Das Fortranprogramm
```{code-block} fortran
---
emphasize-lines: 6, 6
---
program datentyp
  integer :: n
  real:: x

  n = 2
  x = n
  write(*, *) n, x
end program datentyp
```
erzeugt die Ausgabe
```
           2   2.00000000
```
Gemäß der Deklaration zu Beginn des Programms handelt es sich bei der Variable `n` um
einen Integer, während `x` ein Float ist, der in Fortran mit `real` bezeichnet wird. In
der hervorgehobenen Zeile findet bei der Zuweisung automatisch die Umwandlung zwischen
den beiden Datentypen statt.

Im Gegensatz dazu ist eine Festlegung des Datentyps in Python nicht erforderlich.
Man spricht in diesem Zusammenhang auch von *duck typing*: »If it looks like a
duck and quacks like a duck, it must be a duck.« [^duck]

[^duck]: [docs.python.org/glossary.html#term-duck-typing](http://docs.python.org/glossary.html#term-duck-typing). Kritiker
    halten dem entgegen, dass sich auch ein Drache wie eine Ente verhalten kann.

Den Typ einer Variable kann man in Python mit Hilfe der {func}`type`-Funktion herausfinden.

```{code-cell} python
n = 2
print(type(n))
```
Eine Umwandlung von einem Integer zu einem Float lässt sich in Python mit Hilfe der 
{func}`float`-Funktion vornehmen, wobei wir in diesem Beispiel gleich überprüfen, ob
die Umwandlung tatsächlich stattgefunden hat.
```{code-cell} python
x = float(n)
print(type(x))
```
Die umgekehrte Umwandlung von Floats in Integers ist mit der {func}`int`-Funktion 
möglich, wobei der Nachkommaanteil einfach abgeschnitten wird:

```{code-cell} python
int(2.7)
```

Bereits das Anhängen eines Punktes genügt, damit Python die Zahl als Float
interpretiert:

```{code-cell} python
print(type(2.))
```

Für Floats gibt es zwei mögliche Schreibweisen. Zum einen die kann man die
Dezimalbruchschreibweise verwenden, bei der ein Dezimalpunkt erwartet wird.
Stehen vor oder nach dem Dezimalpunkt keine Ziffern, so wird der entsprechende
Anteil gleich Null gesetzt.
```{code-cell} python
5.
```
```{code-cell} python
.25
```
Es ist aber nicht möglich, im Sinne einer abkürzenden Schreibweise sowohl vor
als auch nach dem Dezimalpunkt auf Ziffern zu verzichten.
```{code-cell} python
---
tags: [raises-exception]
---
.
```

Für sehr kleine oder sehr große Zahlen ist die Exponentialschreibweise besser
geeignet. Die Zahl wird dabei mit Hilfe einer Mantisse, die nicht zwingend
einen Dezimalpunkt enthalten muss, und einem ganzzahligen Exponenten, der ein
Vorzeichen enthalten darf, dargestellt.  Zwischen Mantisse und Exponenten muss
dabei ein ``e`` oder ein ``E`` stehen.

```{code-cell} python
1e-2
```
```{code-cell} python
1.53e2
```
```{code-cell} python
1E-5
```

Da Dezimalzahlen im Allgemeinen keine endliche Binärdarstellung besitzen, kann
es bei der Umwandlung in die Binärdarstellung zu Rundungsfehlern kommen.
In {numref}`dualsystem` wurde festgestellt, dass $0{,}1_{10} = 0{,}0\overline{0011}_2$,
so dass diese Zahl im Dualsystem auf jeden Fall abgeschnitten werden muss.
Das Problem wird an dem folgenden Beispiel deutlich, das zudem zeigt, dass es
auf die Reihenfolge der Operationen ankommen kann.
```{code-cell} python
0.1+0.1+0.1-0.3
```
```{code-cell} python
0.1-0.3+0.1+0.1
```
Für die praktische Arbeit ist es wichtig, ein Gefühl dafür zu entwickeln, ob
zum Beispiel eine von Null verschiedene Zahl ein wichtiger Effekt ist oder lediglich
die Folge eines Rundungsfehlers.

Wie bereits gesagt, sind Floats in ihrer Größe begrenzt und sie können auch
nicht beliebig dicht liegen. Informationen hierzu lassen sich in Python abfragen.
Die größtmögliche Zahl, die sich als Float darstellen lässt lautet
```{code-cell} python
import sys
sys.float_info.max
```
Die Distanz zwischen der 1 und der nächsten darauf folgenden darstellbaren Zahl ist
```{code-cell} python
sys.float_info.epsilon
```
Die kleinste normalisierte Zahl ist
```{code-cell} python
sys.float_info.min
```
aber tatsächlich ist die kleinste darstellbare Zahl gleich `5e-324`. Es gibt also
um die Null herum eine Lücke, die jedoch deutlich kleiner ist als die Lücke zwischen
der Eins und der darauf folgenden Zahl.

```{admonition} Hinweis
:class: tip
Ab Python 3.9 lässt sich die kleinste darstellbare Zahl, also `5e-324`
mit Hilfe von `math.ulp(0)` erhalten.
```
Der Zahlenbereich für Floats sowie die Lücken um die Null und die Eins ergeben
sich aus dem verwendeten Zahlenformat, das im IEEE-Standard 754 definiert ist.
Einige Informationen dazu finden sich in {numref}`anhang_floats`.

Im Gegensatz zu Integers können Gleitkommazahlen also nicht beliebig groß
werden, sondern sind auf einen allerdings recht großzügig bemessenen Bereich
bis etwas über {math}`10^{308}` beschränkt. Sollte dieser Bereich sich als
nicht ausreichend herausstellen, ist es empfehlenswert, sich zunächst einmal
Gedanken darüber zu machen, ob man das verwendete numerische Verfahren geeignet
formuliert hat. Eventuell kann schon eine Skalierung der Variablen das Problem
beseitigen. Im schlimmsten Fall kann man in Python zum
[{mod}`mpmath`-Modul](http://mpmath.org/doc/current/) greifen, das es erlaubt,
mit mehr als den standardmäßigen 15 signifikanten Stellen zu rechnen.

Was passiert aber, wenn man den zulässigen Zahlenbereich von Floats überschreitet?
In diesem Fall setzt Python die entsprechende Zahl auf Unendlich oder `inf` vom
vom englischen *infinity*.
```{code-cell} python
sys.float_info.max*1.00000001
```
Dieses Unendlich ist zudem vorzeichenbehaftet.
```{code-cell} python
-sys.float_info.max*1.00000001
```
In manchen Situation kann man mit dem Ergebnis sogar noch weiterrechnen.
```{code-cell} python
x = sys.float_info.max*1.00000001
print(1/x)
```
Dies ist jedoch nicht der Fall, wenn man zweimal positiv Unendlich voneinander abziehen will.
```{code-cell} python
1e400 - 1e401
```
Hierbei steht `nan` für »not a number«. 

Anders als man nach dieser Diskussion vielleicht denke könnte, hat eine Division durch Null
nicht das Ergebnis `inf`. Vielmehr gibt es einen `ZeroDivisionError`.
```{code-cell} python
---
tags: [raises-exception]
---
1.5/0
```
Hierbei handelt es sich um eine so genannte Ausnahme oder Englisch *exception*, die man geeignet
behandeln kann, wie wir später noch sehen werden.

(mathfunc)=
## Funktionen für reelle Zahlen

In numerischen Anwendungen in den Natur- und Ingenieurwissenschaften wird man häufig
mathematische Funktionen auswerten wollen. Der Versuch, beispielsweise eine
Exponentialfunktion auszuwerten, führt jedoch nicht unmittelbar zum Erfolg.
```{code-cell} python
---
tags: [raises-exception]
---
exp(2)
```
Hierfür kann es im Wesentlichen zwei Gründe geben. Entweder hat die Exponentialfunktion
nicht den Namen `exp` oder die Exponentialfunktion ist nicht verfügbar, zumindest nicht
so unmittelbar, wie wir das hier annehmen. Tatsächlich muss man in Python, genauso wie
in C, ein klein wenig mehr tun, als nur die Exponentialfunktion aufzurufen.

Bevor wir uns das gleich genauer ansehen, wollen wir kurz auf zwei für das
wissenschaftliche Rechnen relevante Programmiersprachen hinweisen, bei denen
die Exponentialfunktion sowie eine ganze Reihe weiterer mathematischer
Funktionen direkt aufgerufen werden können. Eine dieser Sprachen ist Fortran,
eine relativ alte, aber im wissenschaftlichen Bereich immer noch häufig
eingesetzte Sprache, deren Name ursprünglich als Abkürzung für »Formula
Translation« stand. Damit kann man schon erwarten, dass sich iin Fortran
mathematische Funktionen sehr einfach verwenden lassen.

Eine moderne Sprache, in der dies ebenfalls der Fall ist, ist Julia.
Hierbei handelt es sich wie bei Python um eine interpretierte Sprache, so 
dass wir die Exponentiation einfach in der Julia-Shell ausprobieren können.
```{code-block} julia
$ julia
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.5.2 (2020-09-23)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

julia> exp(2)
7.38905609893065
```

Wesentlich komplizierter ist das Vorgehen in Python allerdings auch nicht. Man
muss nur daran denken, zunächst das Modul {mod}`math`, das Bestandteil der
Python-Standardbibliothek ist zu laden.
```{code-cell} python
import math
math.exp(2)
```

Zum Vergleich mit Python betrachten wir den folgenden Code, der die Verwendung
einer mathematischen Funktion in der Programmiersprache C illustriert:
```{code-block} c
---
emphasize-lines: 2, 2
---
#include <stdio.h>
#include <math.h>

int main(void) {
  double x = 2;
  printf("Die Exponentialfunktion von %f ist %f\n", x, exp(x));
}
```
Hier entspricht die hervorgehobene Zeile dem `import`-Befehl in Python. Zudem muss
man beim Kompilieren, also der Übersetzung des Programms in maschinenlesbaren Code
mit `-lm` noch die Mathematikbibliothek hinzulinken.
```{code-block} bash
$ cc -o bsp_exp bsp_exp.c -lm
$ ./bsp_exp
Die Exponentialfunktion von 2.000000 ist 7.389056
```
In der ersten Zeile wird mit `-o bsp_exp` festgelegt, dass die Ausgabedatei
den Namen `bsp_exp` heißen soll. Diese wird in der zweiten Zeile ausgeführt
und wir erhalten in der dritten Zeile die erwartete Ausgabe.

````{admonition} Weiterführendes (rechts aufklappen)
:class: toggle
Nach der Kompilierung des obigen C-Programms entsteht als Zwischenprodukt
ein so genanntes Assembler-Programm, das schon sehr maschinennah ist und
von einem Assembler in den von einem Computer les- und ausführbaren
Maschinencode umgewandelt wird.
```{code-block}
            .file   "bsp_exp.c"
            .text
            .section        .rodata
            .align 8
    .LC1:
            .string "Die Exponentialfunktion von %f ist %f\n"
            .text
            .globl  main
            .type   main, @function
    main:
    .LFB0:
            .cfi_startproc
            pushq   %rbp
            .cfi_def_cfa_offset 16
            .cfi_offset 6, -16
            movq    %rsp, %rbp
            .cfi_def_cfa_register 6
            subq    $32, %rsp
            movsd   .LC0(%rip), %xmm0
            movsd   %xmm0, -8(%rbp)
            movq    -8(%rbp), %rax
            movq    %rax, -24(%rbp)
            movsd   -24(%rbp), %xmm0
            call    exp@PLT
            movq    -8(%rbp), %rax
            movapd  %xmm0, %xmm1
            movq    %rax, -24(%rbp)
            movsd   -24(%rbp), %xmm0
            leaq    .LC1(%rip), %rdi
            movl    $2, %eax
            call    printf@PLT
            movl    $0, %eax
            leave
            .cfi_def_cfa 7, 8
            ret
            .cfi_endproc
    .LFE0:
            .size   main, .-main
            .section        .rodata
            .align 8
    .LC0:
            .long   0
            .long   1073741824
            .ident  "GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
            .section        .note.GNU-stack,"",@progbits
```
````

Kommen wir nach diesem Ausflug in andere Programmiersprachen zurück zum Import von
Funktionen aus dem {mod}`math`-Modul der Python-Standardbibliothek. Die obige Form
des Imports ist nur eine von mehrere möglichen Varianten, die Vor- und Nachteile haben.

In der ersten Variante, die wir weiter oben verwendet haben, wird das Modul, hier `math`
dem eigenen Code bekannt gemacht. Dies geschieht in unserem Beispiel mit `import math`.
Der Nachteil hiervon ist, dass man jedes Mal, wenn man sich auf ein Objekt aus dem Modul
beziehen will, den Modulnamen voranstellen muss. Deswegen mussten wir `math.exp` schreiben.
Diese Mehrarbeit lohnt sich aber unter Umständen, um im Code deutlich zu machen, aus
welchem Modul zum Beispiel eine Funktion stammt.

Alternativ hierzu kann man bestimmte Objekte, also Funktionen oder auch Attribute, 
importieren. Diese stehen dann wie in dem folgenden Beispiel zur Verfügung, ohne dass
der Modulname voranzustellen ist.
```{code-cell} python
from math import sin, cos
sin(0.5)**2+cos(0.5)**2
```

Schließlich gibt es noch die Möglichkeit,  sämtliche Objekte eines Moduls auf einmal
einbinden
```{code-cell} python
from math import *
log(10)
```

Dieses Vorgehen ist allerdings nicht ganz unproblematisch, da man auf diese
Weise einen unter Umständen großen Namensraum einbindet und damit potentiell
unabsichtlich Funktionen definiert oder umdefiniert, wodurch die Funktion
des Programms beeinträchtigt werden kann. Einer solchen Situation werden wir im nächsten
Abschnitt noch begegnen.

Jetzt wollen wir uns aber zunächst einen Überblick über die Funktionalität verschaffen,
die uns das {mod}`math`-Modul zur Verfügung stellt. Nachdem wir das Modul schon weiter
oben importiert haben, können wir uns eine Hilfetext ausgeben lassen, der alle definierten
Funktionen und Konstanten zusammen mit einem erläuternden Text aufführt. Wir werden im Folgenden
einige Aspekte diskutieren. Zuvor können Sie sich aber gerne anhand des Hilfetextes einen
ersten Überblick über die Möglichkeiten verschaffen, die das {mod}`math`-Modul bietet.
Beachten Sie dabei, dass das Modul im Laufe der Zeit weiterentwickelt wird. Es kann also sein,
dass einzelne Funktionen in älteren Python-Versionen noch nicht vorhanden sind.

```{code-cell} python
---
tags: ["output_scroll"]
---
help(math)
```    

Zunächst stellen wir fest, dass die wichtigsten Funktionsklassen wie
trigonometrische und hyperbolische Funktionen sowie ihre Inversen, Logarithmen
und die Exponentialfunktion vorhanden sind. Hinzu kommt noch eine kleine Zahl
speziellere Funktionen wie die Gamma- oder die Fehlerfunktion. Für andere
spezielle Funktionen, beispielsweise Besselfunktionen, steht die numerische Bibliothek
{program}`SciPy` zur Verfügung.

Bei den trigonometrischen Funktionen muss man sich immer die Frage stellen, ob Winkel
im Bogenmaß oder in Grad erwartet werden. Die trigonometrischen Funktionen aus dem
{mod}`math`-Modul erwarten Argumente im Bogenmaß. 
```{code-cell} python
from math import sin, pi
sin(90), sin(0.5*pi)
```
````{margin}
```{admonition} Tipp
:class: tip
Python stellt mit `math.tau` auch die Konstante 2π zur Verfügung, die gelegentlich
als [fundamentalere Zahl](https://tauday.com/tau-manifesto) angesehen wird.
```
````
Wie man sieht, liefert das Argument in Grad nicht das vielleicht erwartete
Ergebnis `1`.  Anders ist dies, wenn man das Argument im Bogenmaß einsetzt. In
diesem Beispiel haben wir übrigens auch ausgenutzt, dass das {mod}`math`-Modul
einige konstanten definiert, unter anderem eben die Kreiszahl π und die
eulersche Zahl e.

Die Umrechnung zwischen Bogenmaß und Grad kann explizit mit einem Faktor `180/π`
vornehmen oder die Funktionen {func}`degrees` und {func}`radians` heranziehen.
Letzteres kann für die Lesbarkeit hilfreich sein. Damit können wir unser obiges
Beispiel für Argumente in Grad anpassen.
```{code-cell} python
from math import radians
sin(radians(90))
```

```{admonition} Hinweis
Die Funktion {func}`sin` hatten wir bereits weiter oben importiert und brauchen
dies daher hier nicht mehr zu tun. In einem größeren Programm würde man
normalerweise alle benötigten `import`-Anweisungen an den Anfang des Programms
stellen.
```

Bei der Umrechnung zwischen kartesischen und Polarkoordinaten, deren Beziehung
durch

$$\begin{align}
x &= r\cos(\varphi)\\
y &= r\sin(\varphi)
\end{align}$$

gegeben ist, kann man den Arkustangens verwenden, um den zu den kartesischen Koordinaten
$(x,y)$ gehörigen Winkel

$$\varphi = \arctan\left(\frac{y}{x}\right)$$

zu berechnen. Dazu muss man zunächst einmal wissen, dass der Arkustangens in Python
durch die Funktion {func}`atan` berechnet wird.
```{code-cell} pathon
from math import atan, degrees, sqrt
x = 1
y = sqrt(3)
degrees(atan(y/x))
```
Wir erhalten also, bis auf einen Rundungsfehler, den erwarteten Winkel von $60^\circ$.

Allerdings gibt es zwei Probleme. Zum einen kann der Punkt auf der $y$-Achse liegen.
```{code-cell} python
---
tags: [raises-exception]
---
x = 0
y = 1
atan(y/x)
```
Hier kommt es überhaupt nicht zur Berechnung des Arkustangens, da schon die Division
fehlschlägt. Das andere Probleme besteht darin, dass man nicht zwischen einem Punkt
und dem am Ursprung gespiegelten Punkt unterscheiden kann.
```{code-cell} python
x = -1
y = -sqrt(3)
degrees(atan(y/x))
```
Obwohl der Punkt im dritten Quadranten liegt, erhalten wir wieder das Ergebnis $60^\circ$,
während das korrekte Ergebnis $240^\circ$ wäre.

Für solche Fälle stellt Python die Funktion {func}`atan2` zur Verfügung.
```{code-cell} python
from math import atan2
help(atan2)
```
Wichtig ist hier, dass das erste Argument der Zahl entspricht, die normalerweise im Zähler
des Bruches stehen würde, bei uns also `y`. Unsere Beispiel würde dann folgendermaßen 
aussehen:
```{code-cell} python
x = 0
y = 1
degrees(atan2(y, x))
```
```{code-cell} python
x = -1
y = -sqrt(3)
degrees(atan2(y, x))
```
Wir erhalten also die erwarteten Ergebnisse, da $-120^\circ$ äquivalent zu $240^\circ$ ist.

Im Zusammenhang mit der Umrechnung zwischen kartesischen und Polarkoordinaten hat man
bei der Berechnung des Abstands

$$r = \sqrt{x^2+y^2}$$

die Wahl, diesen Ausdruck explizit hinzuschreiben oder die in Python vorhandene
{func}`hypot`-Funktion zu verwenden. Letzteres kann unter anderem dazu dienen, den
Code lesbarer zu machen.
```{code-cell} python
x = 1
y = 2
sqrt(x**2 + y**2), hypot(x, y)
```
Der Name dieser Funktion erklört sich daraus, dass hier die Länge der Hypothenuse
berechnet wird. Verwandt hiermit ist die {func}`dist`-Funktion, die den Abstand
zweier Punkte berechnet. Sowohl {func}`dist` als auch {func}`hypot` funktionieren
auch in mehr als zwei Dimensionen.
```{code-cell} python
from math import dist
dist((1, 2, 3), (2, 1, 4))
```
In diesem Beispiel ergibt sich wie erwartet die Wurzel aus 3.

```{admonition} Hinweis
Die Verwendung von {func}`dist` sowie von {func}`hypot` in mehr als zwei Dimensionen
erfordert mindestens Python 3.8.
```

Eine weitere wichtige Klasse von Funktionen, die vom {mod}`math`-Modul zur Verfügung
gestellt werden, sind die Logarithmen und die Exponentialfunktion. Hier muss man 
vor allem zwischen dem natürlichen Logarithmus, der häufig als „ln‟ geschrieben wird,
und dem Zehner- oder dekadischen Logarithmus unterscheiden. In Python wird der natürliche
Logarithmus mit Hilfe der {func}`log`-Funktion berechnet und für den dekadischen Logarithmus
gibt es die {func}`log10`-Funktion. Die gleiche Namensbezeichnungen werden zum Beispiel
in C, Fortran und Julia verwendet.
```{code-cell} python
from math import e, log, log10
log(e**2), log10(10**-3)
```

```{admonition} Hinweis
Die {func}`log`-Funktion akzeptiert noch ein zweites Argument, das dann die Basis
angibt. Damit könnte man den dekadischen Logarithmus auch mit `log(x, 10)` berechnen,
was aber potentiell ungenauer ist als `log10(x)`.
```

Neben dem natürlichen Logarithmus {func}`log` und der Exponentialfunction {func}`exp` stellt
Python auch noch die Funktionen {func}`log1p` und {func}`expm1` zur Verfügung. Wozu diese
beiden Funktionen erforderlich sind, wollen wir uns nun ansehen.

Mathematisch stellen Quotienten zweier Funktionen ein Problem dar, wenn sie auf einen Ausdruck
der Form $0/0$ führen. Man muss dann eine geeignete Grenzwertbildung durchführen oder kann zum
Beispiel den Satz von l'Hôpital anwenden. Numerisch wird das Problem noch dadurch schwieriger,
dass Gleitkommazahlen nach einer gewissen Anzahl von Nachkommastellen abgeschnitten werden.

Wenn wir also beispielsweise den Grenzwert

$$\lim_{x\to 0} \frac{\mathrm{e}^x-1}{x}$$

numerisch bestimmen wollen, kann es für kleine Werte von $x$ zu Problemen kommen. Wir könnten
zwar für hinreichend kleine Werte von $x$ den Zähler mit Hilfe der Taylorreihe für die 
Exponentialfunktion

$$\mathrm{e}^x = \sum_{n=0}^\infty\frac{x^n}{n!}$$

annähern, aber
die {func}`expm1`-Funktion nimmt uns diese Arbeit ab.
```{code-cell} python
from math import expm1
x = 0.00001
exp(x)-1, expm1(x)
```
Mit Hilfe der führenden Terme der zugehörigen Taylorreihe wird deutlich, dass das Resultat
der {func}`expm1`-Funktion das richtige ist. Die weiteren Terme sind zu klein, um einen
Unterschied zu machen, und da sie positiv sind, würden Sie den Abstand zum Resultat der
{func}`exp`-Funktion ohnehin nur weiter vergrößern.
```{code-cell} python
x = 0.00001
x + x**2/2 + x**3/6
```

In {numref}`fig:expm1` ist der Unterschied der beiden Berechnungsweisen als Funktion von x
zu sehen. Die durchgezogene Linie ist mit der {func}`expm1`-Funktion berechnet. Sie läuft
in korrekter Weise gegen den Grenzwerten, was man in dieser Auftragung daran sieht, dass
die Abweichung $f(x)-1$ vom Grenzwert gegen Null geht. Die blauen Punkte sind dagegen mit
der {func}`exp`-Funktion berechnet. Hier sieht man deutliche Abweichungen unterhalb von
$x \lesssim 10^{-8}$, die in der Praxis das gesuchte Ergebnis unter Umständen entscheidend
verfälschen könnten.
```{figure} images/datentypen/expm1.png
---
height: 8cm
name: fig:expm1
---
Vergleich von `exp(x)-1` (Punkte) und `expm1(x)` (durchgezogene Linie) durch Betrachtung des
Grenzwerts von $f(x) = (\mathrm{e}^x-1)/x$.
```

Der Logarithmus geht für das Argument 1 durch Null, so dass dort Argumente in
der Nähe von 1 einer besonderen Behandlung bedürfen. Hierzu steht in Python für den
natürlichen Logarithmus die Funktion {func}`log1p` zur Verfügung.
```{code-cell} python
from math import log1p
x = 1e-5
log(1+x), log1p(x)
```
Auch hier kann man sich durch Auswertung der führenden Term der Taylorreihe von

$$\log(1+x) = \sum_{n=1}^\infty\frac{(-1)^{n+1}x^n}{n}$$

davon überzeugen, dass {func}`log1p` bis auf Rundungsfehler den korrekten Wert liefert.
```{code-cell} python
x = 1e-5
x - x**2/2 + x**3/3
```

## Komplexe Zahlen

Neben reellen Zahlen benötigt man immer wieder auch komplexe Zahlen. Dabei
erzeugt man einen Imaginärteil durch Anhängen des Zeichens ``j`` oder ``J``, das
Ingenieure häufig statt des in der Physik üblichen ``i`` verwenden.

```{code-cell} python
(1+0.5j)/(1-0.5j)
```
Alternativ kann man die Funktion {func}`complex` verwenden.
```{code-cell} python
z1 = complex(1, 0.5)
z2 = complex(1, -0.5)
z1/z2
```
Möchte man aus den Werten zweier Variablen eine komplexe Zahl
konstruieren, geht dies mit der zweiten der gerade genannten Methoden
sehr einfach
```{code-cell} python
x = 1
y = 2
z1 = complex(x, y)
z2 = complex(x, -y)
z1/z2
```

Falls man die Funktion ``complex()`` nicht verwenden möchte, muss man
beachten, dass die folgenden beiden Wege nicht zum Ziel führen.

```{code-cell} python
---
tags: [raises-exception]
---
x = 18
y = 9
z = x+yj
```
Hier geht Python davon aus, dass es sich bei `yj` um eine Variable handelt,
der aber noch kein Wert zugewiesen wurde, die also noch nicht definiert ist,
wie Python in der Fehlermeldung sagt. Diese Interpretation lässt sich
leicht überprüfen, wenn man Werte für `x` und `yj` setzt.
```{code-cell} python
yj = 24
x+yj
```

Entsprechendes gilt in dem zweiten Beispiel, in dem zwar `x` und `y` die
oben zugewiesenen Werte besitzen. Python muss aber davon ausgehen, dass
hier die Variable `y` mit der Variablen `j` multipliziert werden soll, und
`j` ist bis jetzt noch nicht definiert. Damit erklärt sich die Fehlermeldung.

```{code-cell} python
---
tags: [raises-exception]
---
z = x+y*j
```
Vielmehr muss die imaginäre Einheit explizit als ``1j`` geschrieben
werden. Den Grund hierfür werden wir noch genauer verstehen, wenn wir in
{numref}`variablen` besprechen, welche Namen für Variablen zugelassen
sind.

```{code-cell} python
z = x+y*1j
z
```
Dieses Resultat ergibt sich aus den weiter oben definierten Werten von `x` und `y`.

```{admonition} Aufgabe
Zeigen Sie an einem oder mehreren Beispielen, dass das Ergebnis einer Rechnung,
die komplexe Zahlen enthält, selbst dann als komplexe Zahl dargestellt wird, wenn
das Ergebnis reell ist.
```

Hat man eine komplexe Zahl einer Variablen zugewiesen, wie wir dies in {numref}`variablen`
noch genauer diskutieren werden, so lassen sich aus der Variablen wieder der Real- und
der Imaginärteil extrahieren.
```{code-cell} python
x = 1+0.5j
x.real, x.imag
```
Man kann sich auch die konjugiert komplexe Zahl beschaffen.
```{code-cell} python
x.conjugate()
```
Die Unterschiede in den Aufrufen ergeben sich daraus, dass bei Real- und
Imaginärteil auf Attribute, also Eigenschaften, der komplexen Zahl zugegriffen
wird, während bei der komplexen Konjugation eine Methode aufgerufen wird, die
etwas mit der komplexen Zahl macht. Es mag an dieser Stelle verwirren, dass man
nicht alternativ `conjugate(x)` verwenden kann. Die Hintergründe werden im
{numref}`oop` klarer werden, wo wir uns mit dem objektorientierten
Programmieren beschäftigen werden.

Natürlich wollen wir auch für komplexe Zahlen mathematische Funktionen
auswerten. Das Modul {mod}`math` hilft hier aber leider nicht weiter,
da es nur mit reellen Zahlen umgehen kann und erfolglos versucht, das
komplexe Argument in eine reelle Zahl umzuwandeln.
```{code-cell} python
---
tags: [raises-exception]
---
from math import exp, pi
exp(0.25j*pi)
```

Es gibt in der Python-Standardbibliothek ein Modul {mod}`cmath`, das mit komplexen
Zahlen umgehen kann.

```{code-cell} python
---
tags: ["output_scroll"]
---
import cmath
help(cmath)
```    
Damit können wir nun die Exponentialfunktion auf eine komplexe Zahl anwenden.
```{code-cell} python
from cmath import exp, pi
exp(0.25j*pi)
```

Dabei ist das Ergebnis immer eine komplexe Zahl. Daher kann es wünschenswert
sein, sowohl das Modul {mod}`math` als auch das Modul {mod}`cmath` zu
importieren:

```{code-block} python
>>> import math, cmath
>>> math.exp(2)
7.38905609893065
>>> cmath.exp(0.25j*math.pi)
(0.7071067811865476+0.7071067811865475j)
```

Eine andere Möglichkeit wäre

```{code-block} python
>>> from math import exp, pi
>>> from cmath import exp as cexp
>>> exp(2)
7.38905609893065
>>> cexp(0.25j*pi)
(0.7071067811865476+0.7071067811865475j)
```

```{admonition} Frage
Welche Funktion wird verwendet, wenn man nacheinander die Funktion
:func:`exp` aus dem Modul {mod}`math` und aus dem Modul {mod}`cmath` importiert?
```

(variablen)=

## Variablen und Zuweisungen

In einem Beispiel des letzten Abschnitts haben wir bereits eine Zahl einer
Variablen zugewiesen. Da dies in einem Programm der Normalfall ist, müssen wir
wissen, welche Namen für Variablen zugelassen sind. Ein Variablenname oder
allgemein ein Bezeichner besteht aus einer beliebigen Zahl von Zeichen, wobei
Buchstaben, der Unterstrich (`_`) und Ziffern zugelassen sind. Das erste Zeichen
darf jedoch keine Ziffer sein. Der Unterstrich zu Beginn und am Ende eines Bezeichners
impliziert üblicherweise eine spezielle Bedeutung, auf die wir später noch zurückkommen
werden. Daher sollte man es sich zur Regel machen, den Unterstrich höchstens innerhalb
eines Bezeichners zu verwenden, sofern man nicht bewusst den Unterstrich in anderer
Weise einsetzt.

Viel interessanter als Unterstriche sind Buchstaben. Diese umfassen zunächst
einmal die Großbuchstaben ``A-Z`` und Kleinbuchstaben ``a-z``. Wie sieht es
aber mit Umlauten oder gar mit Buchstaben aus anderen Schriftsystemen,
beispielsweise griechischen Buchstaben aus? In diesem Zusammenhang stellt sich
die Frage, wie Zeichen im Rechner überhaupt in einer binären Form dargestellt
werden. Es gibt hierfür zahlreiche Standards, unter anderem den ASCII-Standard,
der noch nicht einmal Umlaute kennt, den ISO-8859-1-Standard, der diesen
Mangel behebt, aber dennoch im Umfang sehr beschränkt ist, bis hin zum
Unicode-Standard, der mehr als hunderttausend Zeichen umfasst. Für den
Unicode-Standard gibt es wiederum verschiedene Codierungen, insbesondere die in
der westlichen Welt sinnvolle UTF-8-Kodierung. Etwas mehr Details zu diesem
Thema sind im Anhang {ref}`appendixunicode` zu finden. 

Aus dem vorigen Abschnitt ergibt sich vielleicht der Eindruck, dass die Kodierung
von Zeichen ein komplexeres Thema ist, und dieser Eindruck trügt nicht. Die gute
Nachricht ist allerdings, dass zum einen immer mehr Computerbetriebssysteme 
die UTF-8-Kodierung verwenden und für Python-3-Skripte standardmäßig die 
UTF-8-Kodierung angenommen wird. In Python 3 muss man sich, im Gegensatz zu
Python 2, über die Codierung in vielen Fällen keine großen Gedanken mehr machen,
sofern man nicht zum Beispiel eine Ausgabe in einer anderen Codierung haben möchte.

Die Verwendung der UTF-8-Kodierung impliziert, dass Buchstaben in Bezeichnern
alle Zeichen sein können, die im Unicode-Standard als Buchstaben angesehen
werden, also neben Umlauten zum Beispiel auch griechische Zeichen. Ob es
wirklich sinnvoll ist, Buchstaben von außerhalb des Bereichs ``A-Z`` und
``a-z`` zu verwenden, sollte man sich im Einzelfall gut überlegen. Man muss
sich nur vor Augen halten, was es für Folgen hätte, wenn man ein Programm
analysieren müsste, das unter Verwendung von chinesischen Schriftzeichen
geschrieben wurde. Dennoch ist zum Beispiel der folgende Code für Python 3 kein
Problem:

```{code-block} python
>>> from math import pi as π
>>> Radius = 2
>>> Fläche = π*Radius**2
>>> print(Fläche)
12.566370614359172
```

Es ist nicht selbstverständlich, dass solche Variablennamen in anderen
Programmiersprachen ebenfalls zugelassen sind.

Bei einer Programmiersprache ist immer die Frage zu klären, ob zwischen Groß-
und Kleinschreibung unterschieden wird. Python tut dies, so dass ``var``,
``Var`` und ``VAR`` verschiedene Variablen bezeichnen und für Python nichts
miteinander zu tun haben. Auch hier stellt sich im Einzelfall die Frage,
ob es sinnvoll ist, in einem Programm Variablennamen gleichzeitig in Groß-
und Kleinschreibung zu verwenden. Es ist jedoch wichtig zu wissen, dass eine
Fehlfunktion des Programms ihren Ursprung in einem Tippfehler haben kann,
bei dem Groß- und Kleinschreibung nicht beachtet wurden.

Es ist für die Verständlichkeit des Programmcodes angebracht, möglichst
aussagekräftige Bezeichner zu verwenden, auch wenn diese im Allgemeinen etwas
länger ausfallen. Dabei ist es häufig sinnvoll, einen Bezeichner aus mehreren
Wörtern zusammenzusetzen. Um die einzelnen Bestandteile erkennen zu können,
sind verschiedene Varianten üblich. Man kann zur Trennung einen Unterstrich
verwenden, z.B. ``sortiere_liste``. Alternativ kann man neue Worte mit einem
Großbuchstaben beginnen, wobei der erste Buchstabe des Bezeichners groß oder
klein geschrieben werden kann, z.B. ``sortiereListe`` oder ``SortiereListe``.
Im ersten Fall spricht man von *mixedCase*, im zweiten Fall von *CamelCase*, da
die Großbuchstaben an Höcker eines Kamels erinnern. Details zu den in Python
empfohlenen Konventionen für Bezeichner finden Sie im Python Enhancement Proposal {pep}`8`
mit dem Titel »Style Guide for Python Code« im Abschnitt *Naming Conventions*.

Die folgenden Schlüsselwörter sind in Python als Sprachelemente reserviert und dürfen
nicht für Bezeichner verwendet werden [^keywords]::

```{code-block} python
False     assert      continue   except    if        nonlocal  return
None      async       def        finally   import    not       try  
True      await       del        for       in        or        while 
and       break       elif       from      is        pass      with
as        class       else       global    lambda    raise     yield 
```

[^keywords]: Bei Bedarf kann die Liste der Schlüsselwörter mit Hilfe des ``keyword``-Moduls
    und Verwendung der Anweisung ``keyword.kwlist`` erhalten werden.

```{admonition} Wichtiger Hinweis
:class: warning
Da griechische Buchstaben in der Physik relativ häufig sind, ist 
insbesondere darauf zu achten, dass ``lambda`` reserviert ist. Den Grund hierfür
werden wir im Kapitel {ref}`lambdafunktionen` diskutieren.
```

Variablen kann nun ein Wert zugeordnet werden, wie folgende Beispiele zeigen:

```{code-block} python
>>> x = 1
>>> x = x + 1
>>> print(x)
2
```

Aus der zweiten Zeile wird klar, dass es sich hier trotz des
Gleichheitszeichens nicht um eine Gleichung handelt. Vielmehr wird die rechte
Seite ausgewertet und der auf der linken Seite stehenden Variablen zugewiesen.
Die zweite Zeile müsste also eigentlich als ``x`` → ``x+1`` gelesen werden.

```{code-block} python
---
linenos: true
---
>>> x = y = 1
>>> x, y
(1, 1)
>>> x, y = 2, 3
>>> x, y
(2, 3)
>>> x, y = y, x
>>> x, y
(3, 2)
```

In Python ist es möglich, mehreren Variablen gleichzeitig einen Wert zuzuordnen
(Zeile 1) oder mehreren Variablen in einer Anweisung verschiedene Werte
zuzuordnen (Zeile 4). Statt des Tupels auf der rechten Seite von Zeile 4 könnte
auch eine Liste mit zwei Elementen stehen.  Tupel und Liste sind Datentypen,
die mehrere Elemente enthalten und die wir im Kapitel {ref}`zusgdatentypen`
noch genauer ansehen werden.  Zeile 7 zeigt, wie man elegant die Werte zweier
Variablen vertauschen kann. Dieses Verfahren ist so nicht in jeder
Programmiersprache möglich. Dann muss man darauf achten, nicht einen der beiden
Werte zu verlieren:

```{code-block} python
---
linenos: true
---
>>> x, y = 1, 2
>>> x = y
>>> y = x
>>> x, y
(2, 2)
>>> x, y = 1, 2
>>> tmp = x
>>> x = y
>>> y = tmp
>>> x, y
(2, 1)
```

In Zeile 2 wird der Wert von ``x`` überschrieben und geht somit verloren. In
Zeile 7 wird dieser Wert dagegen in der Variablen ``tmp`` zwischengespeichert und
kann somit in Zeile 9 der Variablen ``y`` zugewiesen werden.

In den Codebeispielen haben wir vor und nach dem Gleichheitszeichen ein
Leerzeichen gesetzt. Dies ist nicht zwingend notwendig, verbessert aber die
Lesbarkeit des Codes und wird daher auch im bereits weiter oben erwähnten Python
Enhancement Proposal {pep}`8` empfohlen. Eine weitere Empfehlung lautet, eine
Zeilenlänge von 79 Zeichen nicht zu überschreiten. Bei überlangen Zeilen kann
man mit einem Backslash (``\``) am Zeilenende eine Fortsetzungszeile erzeugen.
In gewissen Fällen erkennt der Python-Interpreter, dass eine Fortsetzungszeile
folgen muss, so dass dann der Backslash entfallen kann. Dies ist insbesondere
der Fall, wenn in einer Zeile eine Klammer geöffnet wird, die dann erst in
einer Folgezeile wieder geschlossen wird. Es wird häufig empfohlen, den Backslash
zur Kennzeichnung einer Fortsetzungszeile zu vermeiden. Stattdessen sollte
eine Klammerung verwendet werden, selbst wenn diese ausschließlich zur impliziten
Markierung von Fortsetzungszeilen dient. Im folgenden Beispiel wird deutlich,
wie man die Klammerung einsetzen kann, auch wenn man die Addition kaum über zwei
Zeilen verteilen wird:

```{code-block} python
>>> 4+ # doctest: +SKIP
  File "<stdin>", line 1
    4+
     ^
SyntaxError: invalid syntax
>>> (4+
... 5)
9
```

Beim ersten Versuch kann Python nicht erkennen, dass eine Fortsetzungszeile
folgen soll, und beschwert sich entsprechend über die unvollständige Addition.
Im zweiten Versuch behebt die Klammerung das Problem.

## Wahrheitswerte

Im Kapitel {ref}`vorschau` hatten wir schon gesehen, dass man den Ablauf eines
Programms in Abhängigkeit davon beeinflussen kann, dass eine bestimmte Bedingung
erfüllt ist oder nicht. In diesem Zusammenhang spielen Wahrheitswerte oder so
genannte boolesche Variable eine Rolle.

Mit einem Wahrheitswert kann die Gültigkeit einer Aussage mit »wahr« oder
»falsch« spezifiziert werden.  Mögliche Werte in Python sind entsprechend
``True`` und ``False``, wobei die Großschreibung des ersten Zeichens wichtig
ist. Für die bis jetzt behandelten Datentypen (Integer, Float, Complex) gilt,
dass eine Null dem Wert ``False`` entspricht, während alle anderen Zahlenwerte
einem ``True`` entsprechen. Dies lässt sich durch eine explizite Umwandlung mit
Hilfe der Funktion {func}`bool` überprüfen:

```{code-block} python
>>> bool(0)
False
>>> bool(42)
True
```

Wichtige logische Operatoren sind ``not`` (Negation), ``and`` (logisches Und)
und ``or`` (logisches Oder):

```{code-block} python
>>> x = True
>>> y = False
>>> not x
False
>>> x and y
False
>>> x or y
True
```

Logische Ausdrücke werden in Python von links nach rechts ausgewertet und zwar
nur so weit, wie es für die Entscheidung über den Wahrheitswert erforderlich ist.
Dies wird in dem folgenden Beispiel illustriert:

```{code-block} python
>>> x = True
>>> y = 0
>>> x or 1/y
True
>>> x and 1/y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Bei der ``or``-Verknüpfung ist schon aufgrund der Tatsache, dass ``x`` den Wert
``True`` hat, klar, dass der gesamte Ausdruck diesen Wert besitzt. Die Division
wird daher nicht mehr ausgewertet. Bei der ``and``-Verknüpfung reicht die
Information über ``x`` dagegen nicht aus. Zusätzlich wird die Division ausgeführt,
die hier zu einer ``ZeroDivisionError``-Ausnahme führt.

Wahrheitswerte sind häufig das Ergebnis von Vergleichsoperationen, die in der 
folgenden Tabelle zusammengestellt sind.

|Operator |  Bedeutung             |
|---------|------------------------|
|``<``    |  kleiner               |
|``<=``   |  kleiner oder gleich   |
|``>``    |  größer                |
|``>=``   |  größer oder gleich    |
|``!=``   |  ungleich              |
|``==``   |  gleich                |

```{code-block} python
>>> 5 != 2
True
>>> 5 > 2
True
>>> 5 == 2
False
```

```{admonition} Wichtiger Hinweis
:class: warning
Ein beliebter Fehler besteht darin, beim Test auf Gleichheit nur eines
statt zwei Gleichheitszeichen zu verwenden.
```

Bei Gleitkommazahlen ist es normalerweise nicht sinnvoll, auf Gleichheit zu
prüfen, da Rundungsfehler leicht dazu führen können, dass das Ergebnis nicht
wie erwartet ausfällt.

```{code-block} python
>>> x = 3*0.1
>>> y = 0.3
>>> x == y
False
```

In solchen Fällen ist es besser zu überprüfen, ob die Differenz von zwei
Gleitkommazahlen eine vertretbare Schwelle unterschreitet.

```{code-block} python
>>> eps = 1e-12
>>> abs(x-y) < eps
True
```


(formatierung)=
## Formatierung von Ausgaben

Wenn man ein Programm ausführt, möchte man in den meisten Fällen eine Ausgabe haben,
die im einfachsten Fall auf dem Bildschirm erfolgen kann. Im Folgenden soll auf die
Formatierung, insbesondere von Zahlen, eingegangen werden. In Python 3 erfolgt die
Ausgabe auf dem Bildschirm mit Hilfe der ``print``-Funktion, die wir schon im Kapitel
{ref}`vorschau` erwähnt hatten.

```{code-block} python
>>> x = 1.5
>>> y = 3.14159
>>> print(x)
1.5
>>> print(x, y)
1.5 3.14159
>>> print("Dies ist eine Näherung für die Kreiszahl:", y)
Dies ist eine Näherung für die Kreiszahl: 3.14159
```

Wie diese Beispiele zeigen, kann man in einer Zeile mehrere Variablenwerte
ausgeben, unter denen auch Zeichenketten sein können. Im Moment genügt es zu
wissen, dass man Zeichenketten zum Beispiel durch umschließende
Anführungszeichen kennzeichnen kann.  Zeichenketten werden wir detaillierter im
Kapitel {ref}`strings` besprechen. Die letzten beiden ``print``-Aufrufe zeigen,
dass beim Ausdruck mehrerer Variablen automatisch ein Leerzeichen eingefügt
wird. Wenn man zwischen Zeichenketten das Komma weglässt, kann man dieses
Leerzeichen unterdrücken:

```{code-block} python
>>> print("Dies ist eine Näher" "ung für die Kreiszahl:", y)
Dies ist eine Näherung für die Kreiszahl: 3.14159
```

Dies ist besonders bei langen Zeichenketten nützlich, da diese damit problemlos
über mehrere Zeilen geschrieben werden können. Zu beachten ist, dass das Weglassen
des Kommas nur zwischen Zeichenketten erlaubt ist. Das noch vorhandene Komma ist
also erforderlich.

In Python ist es, wie in vielen anderen Programmiersprachen, möglich, die
Darstellung der Variablenwerte genauer festzulegen. Auch wenn die Details von
der Programmiersprache abhängig sind, gibt man typischerweise eine Zeichenkette
an, die neben Text auch Platzhalter für die auszugebenden Variablen beinhaltet.
Mit Hilfe dieser Platzhalter kann man auch genauer spezifizieren, wie die
Ausgabe aussehen soll. Beim Übergang von Python 2 zu Python 3 wurde hierzu eine
``format``-Methode eingeführt, die eine sehr flexible Formatierung erlaubt. Wir
beschränken uns daher im Folgenden auf diese Art der Formatierung. Einige der
damit verbundenen Möglichkeiten werden wir im weiteren Verlauf noch kennenlernen.

Bevor wir uns mit den Formatierungsmöglichkeiten von Integers und Gleitkommazahlen
beschäftigen, müssen wir uns zunächst die grundsätzliche Funktionsweise der
``format``-Methode ansehen.

Im einfachsten Fall hat man eine gewisse Anzahl von Variablen, die man ausgeben
möchte und die im Formatierungsausdruck durch in geschweifte Klammern eingeschlossene
Nummern angegeben werden.

```{code-block} python
>>> x = 2
>>> power = 3
2**3 = 8
>>> print("{0}**{1} = {2}. Ja, das Ergebnis ist {2}!".format(x, power, x**power))
2**3 = 8. Ja, das Ergebnis ist 8!
```

Wie die letzte Eingabe zeigt, können Platzhalter auch wiederholt werden. Ist eine
Wiederholung nicht gewünscht und gibt man die Variablen in der richtigen Reihenfolge
an, so kann auf die Nummerierung verzichtet werden.

```{code-block} python
>>> print("{}**{} = {}".format(x, power, x**power))
2**3 = 8
```

In unübersichtlichen Situationen oder wenn man die Reihenfolge später noch auf
einfache Weise ändern möchte kann man auch Namen vergeben.

```{code-block} python
>>> print("{basis}**{exponent} = {ergebnis}".format(basis=x,
...                                                 exponent=power,
...                                                 ergebnis=x**power))
2**3 = 8
```

Die drei Argumente stehen hier nur in eigenen Zeilen um den langen Ausdruck
geeignet umzubrechen. Wir erinnern uns daran, dass nach einer geöffneten Klammer,
also der Klammer vor ``basis``, bis zur schließenden Klammer weitergelesen wird.

Will man eine geschweifte Klammer im Ausgabetext unterbringen, so muss man diese
wie im folgenden Beispiel gezeigt verdoppeln.

```{code-block} python
>>> print("{}**{} = {}. Und das ist eine geschweifte Klammer: {{".format(
...                                                      x, power, x**power))
2**3 = 8. Und das ist eine geschweifte Klammer: {
```

Bis jetzt haben wir nur die Ausgabe von Variablen in einen Text eingebettet,
ohne die Ausgabe jeder Variable selbst beeinflussen zu können. Dies ist aber
beispielsweise bei Gleitkommazahlen wichtig. 

```{code-block} python
>>> from math import sqrt
>>> print(sqrt(2))
1.4142135623730951
```

Vielleicht wollen wir jedoch gar nicht so viele Nachkommastellen ausgeben. Dies können
wir mit Hilfe einer Formatspezifikation festlegen.

```{code-block} python
>>> print("|{0:5.2f}|".format(sqrt(2)))
| 1.41|
```

Nach der Argumentnummer, die man hier auch weglassen könnte, folgt durch einen
Doppelpunkt abgetrennt die Formatierungsangabe. Die Zahl vor dem Punkt gibt
die minimale Feldbreite an, während die Zahl nach dem Punkt die Anzahl der
Nachkommastellen angibt. Das abschließende ``f`` verlangt die Ausgabe in
einem Format mit fester Kommastelle. Die beiden senkrechten Striche sollen
nur dazu dienen, den Leerplatz vor der Zahl sichtbar zu machen, der dadurch
entsteht, dass die gesamte Feldbreite gleich ``5`` sein soll.

```{code-block} python
>>> print("|{0:.2f}|".format(sqrt(2)))
|1.41|
```

Lässt man die Spezifikation der Feldbreite weg, so wird die minimal benötigte
Breite belegt. Bei der mehrzeiligen Ausgabe von Zahlen ist dann jedoch keine
Ausrichtung nach dem Dezimalpunkt möglich. Bei der Ausrichtung ist auch das
Vorzeichen relevant. Hierbei kann man angeben, wie bei einer positiven Zahl
verfahren wird. Durch Eingabe eines Pluszeichens, eines Leerzeichens oder
eines Minuszeichens in der Formatierungsangabe wird ein Plus, ein Leerzeichen
bzw. gar nichts ausgegeben wie die folgenden Beispiele zeigen:

```{code-block} python
>>> print("|{:+4.2f}|".format(sqrt(2)))
|+1.41|
>>> print("|{:+4.2f}|".format(-sqrt(2)))
|-1.41|
>>> print("|{: 4.2f}|".format(sqrt(2)))
| 1.41|
>>> print("|{: 4.2f}|".format(-sqrt(2)))
|-1.41|
>>> print("|{:-4.2f}|".format(sqrt(2)))
|1.41|
>>> print("|{:-4.2f}|".format(-sqrt(2)))
|-1.41|
```

Hier haben wir bewusst die Feldbreite nur auf ``4`` gesetzt, um den Unterschied
zwischen der dritten und fünften Eingabe zu verdeutlichen.

Bei der Ausgabe von Gleitkommazahlen gibt es nun aber das Problem, dass bei sehr
kleinen oder sehr großen Zahlen eine feste Anzahl von Nachkommastellen nicht
unbedingt geeignet ist.

```{code-block} python
>>> print("{:10.8f}".format(sqrt(2)))
1.41421356
>>> print("{:10.8f}".format(sqrt(2)/10000000))
0.00000014
```

In der zweiten Eingabe sieht man, dass die Zahl der ausgegebenen signifikanten
Stellen dramatisch reduziert ist. In solchen Fällen bietet es sich an, eine
Ausgabe in Exponentialdarstellung zu verlangen, die man mit Hilfe des Buchstabens
``e`` statt ``f`` erhält.

```{code-block} python
>>> print("|{:10.8e}|".format(sqrt(2)))
|1.41421356e+00|
>>> print("|{:10.4e}|".format(sqrt(2)))
|1.4142e+00|
>>> print("|{:14.8e}|".format(sqrt(2)/10000000))
|1.41421356e-07|
>>> print("|{:20.8e}|".format(sqrt(2)))
|      1.41421356e+00|
```

Die erste Eingabe zeigt, wie man eine Exponentialdarstellung mit 8 Nachkommastellen
erhält. Der Exponent wird mit ausgegeben, obwohl er nur für {math}`10^0=1` steht.
Die Zahl der Nachkommastellen lässt sich, wie erwartet und wie in der zweiten
Eingabe zu sehen ist, bei Bedarf anpassen. In diesem Beispiel wird die Feldbreite
von 10 gerade ausgenutzt. Das dritte Beispiel zeigt, dass wir nun auch bei der
Ausgabe von kleinen Zahlen keine signifikanten Stellen verlieren. Entsprechendes
wäre bei großen Zahlen der Fall. Macht man wie in Eingabe 3 die Feldlänge größer, so
wird entsprechend viel Leerplatz auf der linken Seite ausgegeben.

```{admonition} Weiterführender Hinweis
Um etwas über die Möglichkeiten der Positionierung der Ausgabe
zu erfahren, können Sie im letzten Beispiel folgende Formatierungsspezifikationen
ausprobieren: ``{:<20.8e}``, ``{:=+20.8e}`` und ``{:^20.8e}``.
```

Häufig möchte man die Exponentialschreibweise nur verwenden, wenn die
auszugebende Zahl hinreichend groß oder klein ist. Ein solches Verhalten
erreicht man durch Angabe des Buchstabens ``g``.

```{code-block} python
>>> print("|{:15.8g}|".format(sqrt(2)/100000))
|  1.4142136e-05|
>>> print("|{:15.8g}|".format(sqrt(2)/10000))
|  0.00014142136|
>>> print("|{:15.8g}|".format(sqrt(2)*10000000))
|       14142136|
>>> print("|{:15.8g}|".format(sqrt(2)*100000000))
|  1.4142136e+08|
```

Hier wird durch den Wechsel der Darstellung insbesondere sichergestellt, dass 
immer die gleiche Anzahl von signifikanten Stellen ausgegeben wird. [^gformat]

[^gformat]: Die genaue Regel für die Umstellung der Darstellungsart kann man in der
     Dokumentation der Python-Standardbibliothek unter [6.1.3.1. Format Specification Mini-Language]
     (http://docs.python.org/3/library/string.html#formatspec)
     nachlesen.

Betrachten wir nun noch die Formatierung von Integers.

```{code-block} python
>>> n = 42
>>> print("|{0}|{0:5}|{0:05}|".format(n))
|42|   42|00042|
```

```{admonition} Frage
Warum kann man die ``0`` zur Kennzeichnung der einzusetzenden Variable
nicht weglassen?
```

Integers in Dezimaldarstellung benötigen keinen Buchstaben zur
Formatspezifikation. [^dezimal]  Man kann hier aber ähnlich wie bei den Gleitkommazahlen
die Feldbreite festlegen.  Gibt man vor der Feldbreite eine Null an, so wird
das Feld vor der auszugebenden Zahl mit Nullen aufgefüllt. Dies kann zum
Beispiel bei der Ausgabe in anderen Zahlensystemen interessant sein. Python
unterstützt insbesondere die Ausgabe im Binärformat (``b``), Oktalformat
(``o``) und im Hexadezimalformat (``x``).

[^dezimal]: Wenn man unbedingt möchte, kann man ``d`` für Dezimaldarstellung angeben.

```{code-block} python
>>> print("|{0:}|{0:8b}|{0:8o}|{0:8x}|{0:08b}|".format(n))
|42|  101010|      52|      2a|00101010|
```

```{admonition} Frage
Was ändert sich, wenn man ``b``, ``o`` und ``x`` durch die entsprechenden
Großbuchstaben ersetzt? Welche Auswirkungen hat ein ``#``, das vor der Feldbreite
inklusive einer eventuell vorhandenen Null steht?
```

Die hier besprochenen Formatierungsanweisungen decken bereits viele
Anwendungsfälle ab. Dennoch sind die von Python 3 zur Verfügung gestellten
Formatierungsmöglichkeiten noch vielfältiger. Für eine systematische und
vollständige Darstellung der möglichen Formatierungen verweisen wir auf den
[Abschnitt 6.1.3.1. Format Specification Mini-Language](http://docs.python.org/3/library/string.html#formatspec)
in der Dokumentation der Python-Standardbibliothek.

Abschließend sei noch angemerkt, dass die ``print``-Funktion standardmäßig
einen Zeilenumbruch an das Ende des auszugebenden Textes anhängt. Dies ist
jedoch nicht immer gewünscht und lässt sich mit Hilfe der Option ``end``
beeinflussen. Folgendes Beispiel zeigt die Funktionsweise. Die Befehle

```{code-block} python
print("x", end="..")
print("x", end="")
print("x")
```

erzeugen die Ausgabe ``x..xx`` sowie einen anschließenden Zeilenumbruch.
