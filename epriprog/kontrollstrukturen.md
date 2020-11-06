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

# Kontrollstrukturen

```{admonition} Hinweis
:class: warning
Dieses Kapitel befindet sich noch in Bearbeitung.
```

Im {numref}`vorschau` hatten wir bereits kurz die Möglichkeit angesprochen, den
Ablauf eines Programms zu beeinflussen, sei es dadurch, dass ein Programmteil
in einer Schleife mehrfach ausgeführt wird oder dass ein Programmteil nur dann
ausgeführt wird, wenn eine gewisse Bedingung erfüllt ist.  Solche
Kontrollstrukturen sind essentiell, um die Abarbeitung eines Programms zu
steuern. Wir werden in diesem Kapitel zwei Arten von Schleifen betrachten, die
`for`-Schleife und die `while`-Schleife, bei denen auf verschiedene Weise die
Zahl der Schleifendurchläufe kontrolliert wird. Anschließend werden wir uns mit
Verzweigungen der Form `if … else` beschäftigen und auch komplexere
Verzweigungen kennenlernen. Diese Programmkonstrukte finden sich in allen für
das wissenschaftliche Rechnen relevanten Programmiersprachen, auch wenn die
konkrete syntaktische Umsetzung unterschiedlich sein kann.

Wir hatten im vorigen Kapitel bereits gesehen, dass im Fehlerfall, zum Beispiel
bei der Division durch Null, Ausnahmen oder *exceptions* auftreten. Diese müssen
nicht zwingend zum Abbruch des Programms führen, sondern sie können geeignet
behandelt werden. Diesen Aspekt der Steuerung des Programmablaufs werden wir im
letzten Abschnitt dieses Kapitels kennenlernen.

(forloop)=
## For-Schleife

Sollen bestimmte Anweisungen mehrfach ausgeführt werden, wobei die Anzahl der
Wiederholungen zuvor bestimmt werden kann, bietet sich die Verwendung einer
`for`-Schleife an. Gegenüber der expliziten Wiederholung von Befehlen ergeben
sich eine Reihe von Vorteilen. Zunächst einmal spart man sich Tipparbeit und
verbessert erheblich die Lesbarkeit des Programms. Zudem ist eine explizite
Wiederholung nur möglich, wenn die Zahl der Wiederholungen bereits beim
Schreiben des Programms feststeht und nicht erst beim Ausführen des Programms
berechnet wird.

Wir verdeutlichen das anhand eines Beispiels, in dem wir einige Quadratzahlen
berechnen. In einer `for`-Schleife würde das für die Zahlen von 0 bis 4
folgendermaßen gehen.
```{code-cell} python
for n in range(5):
    print(f"{n:4} {n**2:4}")
```
Verzichtet man auf die Schleife, so wäre der folgende Code erforderlich.
```{code-cell} python
print(f"{0:4} {0**2:4}")
print(f"{1:4} {1**2:4}")
print(f"{2:4} {2**2:4}")
print(f"{3:4} {3**2:4}")
print(f"{4:4} {4**2:4}")
```
Es dürfte offensichtlich sein, dass die erste Variante zu bevorzugen ist.
Dies gilt insbesondere, wenn die Zahl der Durchläufe variable sein soll, wie
im folgenden Fall.
```{code-cell} python
nmax = 7
for n in range(nmax):
    print(f"{n:4} {n**2:4}")
```

Sehen wir uns den Aufbau der `for`-Schleife genauer an. Das Schlüsselwort `for`
kennzeichnet den Beginn einer Schleife. Dann folgt der Name der Variable, in
unserem Fall also `n`, die bei der Abarbeitung der Schleife vorgegebene Werte
annimmt, und im Rahmen der Schleife verwendet werden kann. Im Allgemeinen
können hier auch mehrere Variablennamen vorkommen, wie wir später im 
{numref}`zusgdatentypen` sehen werden. Die Werte, die die Variable `n` in
unserem Beispiel annehmen kann, werden durch die `range`-Anweisung bestimmt.
Zwar werden die Werte erst bei Bedarf generiert, aber wir können sie uns
ansehen, indem wir explizit eine Liste der Werte erzeugen lassen.
```{code-cell} python
list(range(5))
```

Es wird also eine Liste von aufeinanderfolgenden ganzen Zahlen erzeugt, die
hier fünf Elemente enthält. Zu beachten ist, dass die Liste mit Null beginnt
und nicht mit Eins. Wir werden uns diesen zusammengesetzten Datentyp im
{numref}`listen` noch genauer ansehen. Für den Moment genügt jedoch die
intuitive Vorstellung von einer Liste. In der ersten Zeile der
`for`-Schleife, die mit einem Doppelpunkt enden muss, wird also festgelegt,
welchen Wert die Schleifenvariable `n` bei den aufeinanderfolgenden
Schleifendurchläufen jeweils annimmt.

```{admonition} Mehr Flexibilität in der range()-Funktion
:class: tip
Mit nur einem Argument erzeugt die {func}`range`-Funktion wie oben gesehen
ganze Zahlen von 0 bis ausschließlich dem angegebenen Wert. Gibt man zwei
Argumente an, so entsprechen diese dem Startwert und dem Wert, der gerade
nicht mehr angenommen wird. Gibt man ein drittes Argument an, so entspricht
dieses der Schrittweite, die übrigens auch negativ sein kann. Alle Argumente
müssen aber ganze Zahlen sein. Spielen Sie einfach mal ein bisschen mit
der {func}`range`-Funktion herum.
```

Der Codeteil, der im Rahmen der Schleife im Allgemeinen mehrfach ausgeführt
wird und im obigen Beispiel nur aus einer Zeile besteht, ist daran zu erkennen,
dass er eingerückt ist. Zur Verdeutlichung vergleichen wir zwei Beispiele,
die sich lediglich in der Einrückung der letzten Zeile unterscheiden.
Im ersten Beispiel ist die letzte Zeile Bestandteil der Schleife und wird
demnach zweimal ausgeführt.
```{code-cell} python
for n in range(2):
    print(f"Schleifendurchlauf {n+1}")
    print("Das war's.")
```
Rückt man die letzte Zeile dagegen aus, so wird sie erst ausgeführt nachdem
die Schleife zweimal durchlaufen wurde.
```{code-cell} python
for n in range(2):
    print(f"Schleifendurchlauf {n+1}")
print("Das war's.")
```
Im vorliegenden Beispiel ist sicher die zweite Variante adäquat.

Entscheidend für die Zugehörigkeit zur Schleife ist also die Einrückung, wobei
die Zahl der Leerstellen im Prinzip frei gewählt werden kann, aber innerhalb
des ganzen Schleifenkörpers konstant sein muss. Ein guter Kompromiss zwischen
kaum sichtbaren Einrückungen und zu großen Einrückungen, die bei geschachtelten
Schleifen schnell zu Platzproblemen führen, ist eine Einrückung von vier
Leerzeichen. So wird dies auch im {pep}`8` empfohlen, dem *Python Enhancement
Proposal*, das Empfehlungen zur Formatierung von in Python geschriebenem
Programmcode gibt. Diese Empfehlungen sind zwar nicht verpflichtend, aber die
wichtigsten Hinweise werden von den meisten Programmierern respektiert.

```{admonition} Weiterführender Hinweis
Im {pep}`8` wird auch eine maximale Zeilenlänge von 79 Zeichen empfohlen. Sehr
lange Zeilen sind unter Umständen schwer zu lesen und führen bei kleineren
Bildschirmen zu Problemen mit Zeilenumbrüchen. Da heutzutage oft größere
Monitore zum Einsatz kommen, geben manche Projekte eine Maximallänge von 99
Zeichen vor.
```

Da die Verwendung der Einrückung als syntaktisches Merkmal ungewöhnlich ist,
wollen wir kurz zwei Beispiele aus anderen Programmiersprachen besprechen. In
FORTRAN 90 könnte eine Schleife folgendermaßen aussehen:

```{code-block} fortran
PROGRAM Quadrat
DO n = 0, 4
   PRINT '(2I4)', n, n**2
END DO
END PROGRAM Quadrat
```

Hier wurde nur aus Gründen der Lesbarkeit eine Einrückung vorgenommen. Relevant
für das Ende der Schleife ist lediglich das abschließende `END DO`. Während
man sich hier selbst dazu zwingen muss, gut lesbaren Code zu schreiben, zwingt
Python den Programmierer durch seine Syntax dazu, übersichtlichen Code zu
produzieren.

Auch im folgenden C-Code sind die Einrückungen nur der Lesbarkeit wegen
vorgenommen worden. Der Inhalt der Schleife wird durch die öffnende
geschweifte Klammer in Zeile 6 und die schließende geschweifte Klammer in Zeile
9 definiert.
```{code-block} c
---
linenos: true
emphasize-lines: 7, 7
---
#include <stdio.h>

main(){
   int i;
   int quadrat;
   for(i = 0; i < 5; i++){
         quadrat = i*i;
         printf("%4i %4i\n", i, quadrat);
   }
}
```
Würde man auf die Klammern verzichten, so wäre nur die der `for`-Anweisung folgende
Zeile, also Zeile 7, Bestandteil der Schleife. Dagegen befände sich Zeile 8 trotz
der Einrückung nicht mehr im Schleifenkörper.

Schleifen werden in Python häufig anders organisiert als dies in Sprachen wie
Fortran und C der Fall ist. Diesen Unterschied können wir durch zwei
Realisierungen der gleichen Problemstellung illustrieren. Im {numref}`vorschau`
hatten wir eine Implementation des Schere-Papier-Stein-Spiels in Python
besprochen. Darin kam unter anderem eine Liste der drei beteiligten Gegenstände
vor. An dieser Stelle ist nur wichtig, dass wir Elemente einer Liste durch
einen Index adressieren können, so wie wir das für die Komponenten eines
Vektors in der Mathematik gewohnt sind.

Stellen wir uns nun vor, dass wir eine Liste der drei Gegenstände ausgeben wollen.
Eine erste Variante besteht darin, mit Hilfe der {func}`range`-Funktion eine Schleife
über die Indizes zu programmieren, in der dann die Elemente der Liste adressiert und
ausgegeben werden. 
```{code-cell} python
objekte = ['Stein', 'Papier', 'Schere']
for idx in range(3):
    print(objekte[idx])
```
Eine solche Vorgehensweise ist für Sprachen wie Fortran und C typisch. Da der
Index in gleichmäßigen Schritten hochgezählt wird, ist es für den Computer möglich,
effizient auf die einzelnen Listenobjekte zuzugreifen. Dies gilt insbesondere, wenn
es sich bei den Listenobjekten um Zahlen handelt, die alle gleich viel Speicher
in Anspruch nehmen. Diese erste Variante wird in Python eigentlich nur in besonderen
Fällen verwendet, in denen die Rechengeschwindigkeit im Vordergrund steht.

In Python üblicher ist die zweite Variante, bei der direkt über die Liste iteriert
wird.
```{code-cell} python
for objekt in ['Stein', 'Papier', 'Schere']:
    print(objekt)
```
Aus der zweiten Zeile wird hier offensichtlich, dass die Schleife über alle Elemente
der Liste geht. Der Code ist insgesamt etwas leichter zu lesen und schneller zu
schreiben als der Code der ersten Variante und wird daher normalerweise von
Python-Programmierern bevorzugt.

Wir betrachten noch ein zweites Beispiel, das von seiner Struktur gerade beim
numerischen Arbeiten typisch ist. Dabei wollen wir die Kreiszahl π mit Hilfe
der Summendarstellung

$$\sum_{n=1}^\infty\frac{1}{n^2} = \frac{\pi^2}{6}$$

bestimmen. Dies geht allein schon deshalb nur näherungsweise, weil wir die Summe
bei einem wählbaren maximalen Index abschneiden müssen. Dabei fällt der Fehler
invers linear mit diesem maximalen Index. Betrachten wir nun den zugehörigen Python-Code.
```{code-cell} python
from math import sqrt

nmax = 100000
summe = 0
for n in range(nmax):
    summe = summe + 1/(n+1)**2
print(sqrt(6*summe))
```
Den maximalen Summationsindex hätten wir hier auch direkt in das Argument der
{func}`range`-Funktion schreiben können. Wollen wir diesen Wert aber ändern, so
ist die betreffende Stelle leichter zu finden, da der Variablenname `nmax` auf
die Bedeutung dieses Wert hinweist.

Zwei Aspekte wollen wir an diesem Beispiel betonen. Zum einen übersieht man leicht,
dass im Nenner nicht einfach `n**2` stehen darf. Dies würde zu einer Division durch
Null führen, da der erste Wert, der von der {func}`range`-Funktion geliefert wird,
gerade Null ist. Da die Summation bei 1 beginnt, müssen wir also im Nenner `(n+1)**2`
schreiben.

Ein zweiter Aspekt wird gerne übersehen. Im Schleifenkörper, der hier nur aus der
vorletzten Zeile besteht, wird wie bei jeder Zuweisung zunächst die rechte Seite
ausgewertet. Dabei erwartet der Pythoninterpreter schon beim ersten Durchlauf, dass
die Variable `summe` einen Wert besitzt. Auch wenn wir einen fehlenden Wert intuitiv
einfach auf Null setzen würden, ist es für Python ein großer Unterschied, ob eine
Variable den Wert Null hat oder überhaupt keinen Wert besitzt. Dies bedeutet, dass
unser Beispiel nicht mehr läuft, wenn wir die vierte Zeile weglassen. Aus technischen
Gründen entfernen wir die Variable hier explizit, da sie sonst ihren Wert aus der
obigen Zelle behält.
```{code-cell} python
del summe
```
Unser neuer Code hat nun die folgende Form.
```{code-cell} python
---
tags: [raises-exception]
---
from math import sqrt

nmax = 100000
for n in range(nmax):
    summe = summe + 1/(n+1)**2
print(sqrt(6*summe))
```
Wie erwartet schlägt die Ausführung fehl, weil die Variable `summe` beim allerersten
Schleifendurchlauf noch nicht definiert ist. Es ist also unbedingt erforderlich,
die Variable vor der Schleife zu definieren. Man spricht hier auch von einer
Initialisierung.

`for`-Schleifen können auch geschachtelt werden. Wir zeigen dies an einem Beispiel,
das die Wahrheitswerttabelle für die logische UND-Verknüpfung (`&`) und die logische
ODER-Verknüpfung (`|`) darstellt.
```{code-cell} python
print("  arg1   arg2   arg1 & arg2   arg1 | arg2 ")
print("------------------------------------------")
for arg1 in [False, True]:
    for arg2 in [False, True]:
        print(f" {arg1!s:5}  {arg2!s:5}   {arg1&arg2!s:^11}   {arg1|arg2!s:^11}")
```
```{admonition} Weiterführender Hinweis
Unter anderem für solche Situationen stellt in Python das
[{mod}`itertools`-Modul](https://docs.python.org/3/library/itertools.html) der
Standardbibliothek hilfreiche Funktionen zur Verfügung.
```
Wie man in den ersten beiden Spalten der Ausgabe sieht, wird zunächst in der äußeren
Schleife `arg1` auf `False` gesetzt. Anschließend wird die innere Schleife abgearbeitet,
in der `arg2` nacheinander die Werte `False` und `True` annimmt. Erst dann wird in der
äußeren Schleife `arg1` auf `True` gesetzt und danach wiederum die innere Schleife
abgearbeitet.

Gerade in einer doppelten Schleife ist die Einrückung wichtig, die darüber bestimmt,
in welcher Schleife eine Befehlszeile abgearbeitet wird. Da die `print`-Anweisung
relativ zur inneren Schleife eingerückt ist, wird sie in dieser ausgeführt. und
entsprechend werden zusätzlich zum Tabellenkopf vier Zeile ausgegeben. Würde man die
letzte Zeile nur vier Leerzeichen weit einrücken, würde sie in die äußere Schleife
wandern und nur zweimal ausgeführt werden.

Versucht man dies, gibt es zunächst allerdings ein Problem.
```{code-cell} python
---
tags: [raises-exception]
---
print("  arg1   arg2   arg1 & arg2   arg1 | arg2 ")
print("------------------------------------------")
for arg1 in [False, True]:
    for arg2 in [False, True]:
    print(f" {arg1!s:5}  {arg2!s:5}   {arg1&arg2!s:^11}   {arg1|arg2!s:^11}")
```
Jede Schleife erwartet nämlich einen eingerückten Block von mindestens einer Zeile
Länge. In unserem Fall ist es eigentlich nicht sinnvoll, die innere Schleife leer
zu lassen. Gerade bei der Programmentwicklung kann es aber vorkommen, dass man eine
Schleife schon mal anlegen, aber erst später mit Code füllen will. Häufiger kommt
dies bei Funktionen vor, in denen sich das gleiche Problem stellt. Dann hilft der
Befehl `pass` weiter, der Python signalisiert, dass es hier nichts zu tun gibt.
```{code-cell} python
print("  arg1   arg2   arg1 & arg2   arg1 | arg2 ")
print("------------------------------------------")
for arg1 in [False, True]:
    for arg2 in [False, True]:
        pass
    print(f" {arg1!s:5}  {arg2!s:5}   {arg1&arg2!s:^11}   {arg1|arg2!s:^11}")
```
Jetzt wird die `print`-Anweisung tatsächlich nur zweimal ausgeführt, nämlich jeweils
am Ende der Abarbeitung der äußeren Schleifendurchläufe. Außerdem kann man hier
noch feststellen, dass die Laufvariable `arg2` der inneren Schleife auch nach der
Abarbeitung der Schleife zur Verfügung steht. Sie hat dabei den Wert, der ihr zuletzt
zugewiesen wurde, in unserem Fall also `True`.


## While-Schleife

## Verzweigungen

## Abfangen von Ausnahmen
