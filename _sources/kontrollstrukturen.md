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
Dies gilt inbesondere, wenn die Zahl der Durchläufe variable sein soll, wie
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


## While-Schleife

## Verzweigungen

## Abfangen von Ausnahmen
