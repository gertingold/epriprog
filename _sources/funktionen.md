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

# Funktionen

```{admonition} Hinweis
:class: warning
Dieses Kapitel befindet sich noch in Bearbeitung.
```

Funktionen im mathematischen Sinne sind uns in den Natur- und Ingenieurwissenschaften
wohlbekannt. Dass solche Funktionen auch von Programmiersprachen zur Verfügung gestellt
werden, hatten wir unter anderem im {numref}`mathfunc` gesehen. Allerdings ist der 
Begriff der Funktionen in Programmiersprachen wesentlich weiter gefasst. So muss eine
Funktion nicht unbedingt ein Argument besitzen, und sie muss auch nicht unbedingt ein
Ergebnis zurückgeben. In manchen Programmiersprachen wird nach diesem letzten Kriterium
unterschieden. So kennt Fortran *functions*, die ein Resultat zurückgeben, und *subroutines*,
bei denen dies nicht der Fall ist.

Wozu sind Funktionen gut, wenn man davon absieht, dass sie uns aus der Mathematik vertraut
sind? Zunächst einmal können Funktionen wesentlich dabei helfen, ein Programm zu strukturieren.
Lagert man eine bestimmte Funktionalität in eine Funktion mit einem gut gewählten Namen aus,
so kann man die Komplexität im Innern der Funktion verstecken. Bei der Suche nach Fehlern
kann dies ein entscheidender Vorteil sein, da man sich entweder nur mit dem Innern der Funktion
beschäftigt und untersucht, ob diese korrekt implementiert ist, oder aber sich auf deren
Korrektheit verlässt und die Details bei der Untersuchung des restlichen Programms nicht im
Blick haben muss.

Funktionen eignen sich auch sehr gut dazu, Programmcode, der an mehreren Stellen im Programm
auftreten würde, an einer einzigen Stelle unterzubringen. Auch dieser Aspekt trägt, zusammen
mit einem gut gewählten Funktionsnamen, dazu bei, ein Programm lesbarer zu machen. Zum 
anderen verbessert sich die Wartbarkeit des Codes erheblich, da Korrekturen nur an einer 
Stelle vorgenommen werden müssen. Ohne die Verwendung von Funktionen müssten man darauf achten,
Korrekturen zum Code an verschiedenen Stellen der Programms in konsistenter Weise vorzunehmen.

Stellt man beim Programmieren fest, dass sich Code wiederholt, so sollte man sich also überlegen,
ob es nicht sinnvoll wäre, für die betreffende Aufgabe eine Funktion zu definieren. Auch dann
wenn Code nicht identisch wiederholt wird, sondern nur in ähnlicher Weise, ist eine Auslagerung
in eine Funktion denkbar, wenn man geeignete Funktionsargumente einführt. Grundsätzlich sollte
man beim Programmieren daran denken, sich nicht unnötig zu wiederholen und stattdessen entweder
eine der in {numref}`forloop` und {numref}`whileloop` besprochenen Schleifenvarianten zu verwenden
oder aber eine Funktion zu implementieren.

Schließlich ist die Verwendung von Funktionen auch dann angebracht, wenn man die gleiche
Funktionalität in verschiedenen Programmen benötigt. Man kann solche Funktionen in einem 
Modul sammeln und dann bei Bedarf importieren, wie wir es schon mit dem {mod}`math`-Modul
und den darin enthaltenen Funktionen getan haben. 

## Funktionsdefinitionen

Betrachten wir zunächst eine Funktion, die keine Argumente besitzt. Was die Funktion tut, ist
also festgelegt und kann nicht durch Parameter verändert werden.
```{code-cell} python
def f():
    print("Hallo!")

print("** Anfang")
f()
print("** Ende")
```
In diesem einfachen Beispiel ist die Funktion durch die ersten beiden Zeilen definiert. Dabei 
besitzt die erste Zeile eine Struktur wie wir sie ähnlich von Schleifen und Verzweigungen kennen.
Die Zeile beginnt nämlich ebenfalls mit einem Schlüsselwort, das hier `def` heißt und andeutet,
dass hier eine Funktion definiert wird. Des Weiteren wird die erste Zeile mit einem Doppelpunkt
beendet. Der Funktionsname ist hier `f`, wobei hier im Allgemeinen eine Name gewählt werden sollte,
der besser beschreibt, was die Funktion tut. Wichtig ist das Klammerpaar, das auch dann nicht
weggelassen werden darf, wenn die Funktion überhaupt keine Argumente besitzt.

Der Funktionscode ist wie üblich in Python durch eine Einrückung kenntlich zu machen. Die dritte,
leere Zeile dient hier nur zur optischen Absetzung und ist für den Python-Interpreter völlig
irrelevant. Durch die Beendung der Einrückung sind die letzten drei Zeilen nicht mehr Bestandteil
der Funktion. Funktionsdefinitionen benötigen genauso wie Schleifen und Verzweigungen zwingend
einen eingerückten Codeblock. Wie schon bei den `for`-Schleifen in {numref}`forloop` kann auch hier
bei Bedarf der Befehl `pass` eingerückt verwendet werden.

Wenn der Python-Interpreter den Code des obigen Beispiels verarbeitet, wird zunächst die Funktion
`f` definiert. Sie wird zu diesem Zeitpunkt jedoch nicht ausgeführt. Es erfolgt als inbesondere
zu diesem Zeitpunkt nicht die Ausgabe des Textes `Hallo!`. Die Anweisung in Zeile 4 führt nun dazu,
dass der Text `** Anfang` ausgegeben wird. Anschließend wird die Funktion `f` ohne Argumente aufgerufen.
An dieser Stelle ein Argument anzugeben, das in der Funktionsdefinition nicht vorgesehen ist, würde
zu einem Fehler führen.
```{code-cell} python
---
tags: [raises-exception]
---
def f():
    print("Hallo!")

print("** Anfang")
f(1)
print("** Ende")
```
Rufen wir dagegen unsere Funktion `f` korrekt ohne ein Argument auf, so wird diese ausgeführt und
in diesem Fall `Hallo!` ausgegeben. Nachdem die Funktion ausgeführt wurde, wird die Programmausführung
direkt nach dem Funktionsaufruf fortgesetzt. Im Beispiel wird somit abschließend der Text `** Ende`
ausgegeben.

In den meisten Fällen wird man die Funktion flexibler gestalten wollen und zu diesem Zweck ein oder
mehrere Argument übergeben wollen. Um den ursprünglichen Autor von Python,
[Guido von Rossum](https://de.wikipedia.org/wiki/Guido_van_Rossum), zu grüßen, können wir den Namen der
zu grüßenden Person als Argument übergeben.
```{code-cell} python
def f(name):
    print(f"Hallo, {name}!")

f("Guido")
```
Will man zusätzlich die Sprache zwischen Deutsch (de) und Englisch (en) wählen, so könnte man ein
weiteres Argument vorsehen.
```{code-cell} python
def f(name, lang):
    if lang == "en":
        print(f"Hello, {name}!")
    elif lang == "de":
        print(f"Hallo, {name}!")
    else:
        print(f"{name}!")

f("Guido", "en")
```

Das gewählte Beispiel ist insofern untypisch als die Funktion anscheinend keinen Rückgabewert zurückliefert.
Normalerweise würde man die sich ergebende Zeichenkette an den aufrufenden Programmteil übergeben, wo dann
entschieden werden kann, was mit dem Ergebnis zu tun ist. Eine alternative Variante unserer Funktion mit
einem Argument würde dann folgendermaßen aussehen.
```{code-cell} python
def f(name):
    s = f"Hallo, {name}!"
    return s

print(f("Guido"))
```
Das Ergebnis wird mit Hilfe der `return`-Anweisung zurückgegeben, wobei hier keine Klammern zu setzen sind.
Alternativ wäre es möglich, auf die Variable `s` zu verzichten und die sich ergebene Zeichenkette direkt
in die `return`-Anweisung zu schreiben.

Auch wenn man den Eindruck haben könnte, dass das Fehlen einer `return`-Anweisung dazu führt, dass überhaupt
kein Ergebnis zurückgibt, ist dies nicht ganz richtig.
```{code-cell} python
def f(name):
    print(f"Hallo, {name}!")

x = f("Guido")
print(f"Rückgabewert: {x}")
```
Die erste Ausgabezeile ergibt sich aus der `print`-Anweisung in der Funktion `f`. Der Rückgabewert aufgrund
des Funktionsaufrufs wird in der Variable `x` gespeichert, die anschließend ausgegeben wird. Wie wir sehen,
wird in diesem Fall als Ergebnis `None` zurückgegeben. Das gleiche Result hätten wir erhalten, wenn wir als
letzte Zeile explizit `return None` geschrieben hätten.
```{code-cell} python
def f(name):
    print(f"Hallo, {name}!")
    return None

x = f("Guido")
print(f"Rückgabewert: {x}")
```
```{admonition} Tipp
:class: tip
Eine vergessene `return`-Anweisung und der sich daraus ergebende Rückgabewert `None` können gelegentlich
zu überraschenden Fehlermeldung führen. Es lohnt sich daher bei Fehlern in Zusammenhang mit Funktionen zu
überprüfen, ob die `return`-Anweisung vorhanden ist.
```

Eine Funktion kann auch mehrere `return`-Anweisungen enthalten, wobei die Ausführung der Funktion beendet
wird, sobald sie bei einer `return`-Anweisung ankommt. Das folgende Beispiel illustriert dies an einem
sehr simplen Primzahltest.
```{code-cell} python
def is_prime(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

for n in range(2, 100):
    if is_prime(n):
        print(n, end=' ')
```
````{margin}
```{admonition} Weiterführende Frage
Dieser Primzahltest ist alles andere als effizient. Wie könnte man ihn verbessern?
```
````
Sobald `n` ohne Rest durch `divisor` teilbar ist, wird die Funktion mit der `return`-Anweisung beendet und
der Wert `False` zurückgegeben. Wird kein Teiler gefunden, so wird de Wert `True` zurückgegeben. Abhängig
vom Ergebnis der Funktion `is_prime` wird die betreffende Zahl ausgegeben oder nicht und auf diese Weise
eine Liste von Primzahlen erzeugt.

Eine Funktion kann auch mehr als einen Wert zurückgeben. Dazu werden die einzelnen Variablen durch Kommas
getrennt in der `return`-Anweisung aufgelistet.
```{code-cell} python
from math import cos, radians, sin

def spherical2cartesian(r, theta, phi):
    theta = radians(theta)
    phi = radians(phi)
    x = r*sin(theta)*cos(phi)
    y = r*sin(theta)*sin(phi)
    z = r*cos(theta)
    return x, y, z

pt1_r = 10
pt1_theta = 45
pt1_phi = 30
pt1_x, pt1_y, pt1_z = spherical2cartesian(pt1_r, pt1_theta, pt1_phi)
print(f"({pt1_x:5.3f}, {pt1_y:5.3f}, {pt1_z:5.3f})")
```
Vergleicht man in diesem Beispiel die Namen sowohl der Argumente als auch der
Rückgabewerte in der Funktionsdefinition mit den Namen, die im Funktionsaufruf
in der vorletzten Zeile verwendet werden, so stellt man fest, dass diese nicht
identisch sein müssen. Dies ist schon deswegen nicht der Fall, weil man statt der drei
Variablen im Funktionsaufruf auch direkt numerische Werte angeben könnte. Zudem
wäre es sonst erforderlich, die Variablennamen in Funktionen zu kennen, die man
aus einem Modul importiert. In unserem Beispiel erfolgt die Zuordnung der Argumente
und der Rückgabewerte einfach nach der Position. Die Möglichkeit, mit Hilfe von
Schlüsselworten eine Zuordnung der Funktionsargumente vorzunehmen, werden wir in
{numref}`kwargs` besprechen.

## Dokumentation von Funktionen

Wie generell beim Programmieren ist es auch in Funktionen sinnvoll, an eine
ausreichende Dokumentation zu denken. Dies könnte mit Hilfe von Kommentaren
erfolgen, die in Python mit einem `#` eingeleitet werden. Andere
Programmiersprachen verwenden hierfür häufig auch andere Markierungen. In
Python gibt es für Funktionen jedoch eine geeignetere Art der Dokumentation,
nämlich einen Dokumentationstext, den so genannten *docstring*, der direkt auf
die erste Zeile der Funktionsdefinition folgt.
```{code-cell} python
from math import sqrt

def mitternacht(a, b, c):
    """Berechne die beiden Lösungen einer quadratischen Gleichung ax²+bx+c=0

    Es wird die Mitternachtsformel verwendet.
    Achtung: Es wird stillschweigend vorausgesetzt, dass b^2-4ac>0.

    """
    diskriminante = sqrt(b**2-4*a*c)
    root1 = (-b+diskriminante)/(2*a)
    root2 = (-b-diskriminante)/(2*a)
    return root1, root2
```
Der *docstring* wird hier nicht nur mit einem, sondern mit drei Anführungszeichen begrenzt,
da auf diese Weise ein mehrzeiliger Text möglich ist. Der Vorteil dieser Dokumentationsweise
im Vergleich zu einfachen Kommentaren besteht bei Python darin, dass der *docstring* mit Hilfe
der {func}`help`-Funktion ausgegeben werden kann, ähnlich wie wir dies im {numref}`mathfunc`
kennengelernt hatten, wo `help(math)` die Dokumentation für das {mod}`math`-Modul ausgabe.
```{code-cell} python
help(mitternacht)
```
Hier wird man also in Python belohnt, wenn man sich einer guten Dokumentationspraxis bedient.

Weitere Hinweis zu *docstrings* sind in {pep}`257` zu finden.

## Lokale und globale Variable

Nicht selten kommt es vor, dass Variablen inner- und außerhalb einer Funktion den gleichen
Namen haben. Insbesondere bei Funktionen, die aus fremden Modulen, zum Beispiel aus der 
Python-Standardbibliothek, importiert werden, lassen sich solche Namensdoppelungen auch kaum
vermeiden. Daher stellt sich die Frage, auf welche Variable sich unter welchen Umständen
ein mehrfach verwendeter Variablenname bezieht.

In dem folgenden Beispiel sind außerhalb der Funktion {func}`f` die Variablen
`x` und `y` definiert. Innerhalb der Funktion {func}`f` gibt es eine Variable
`x`, die innerhalb der Funktion verändert wird. Außerdem geht der Wert der
Variable `y` in die Rechnung ein. Aus der Sicht der Funktion {func}`f` muss man
nun zwischen lokalen und globalen Variablen unterscheiden. Lokale Variablen sind
nur innerhalb der Funktion sichtbar, jedoch nicht von außerhalb der Funktion. Gibt
es keine lokale Variable mit dem vorgegebenen Namen, dafür aber eine passende globale
Variable, so wird deren Wert verwendet. Sollte es auch keine passende globale Variable
geben, so sucht Python schließlich auch noch in den eingebauten Python-Funktionen.

```{admonition} Tipp
:class: warning
Grundsätzlich sollte man den Bezug auf globale Variablen nach Möglichkeit vermeiden, da
hier eine große Gefahr für Fehler lauert. Meistens ist es besser, den Wert der globalen
Variable explizit über ein Funktionsargument zu übergeben. Unter Umständen kann auch 
objektorientiertes Programmieren nützlich sein, auf das wir in {numref}`oop` eingehen
werden.
```

Betrachten wir die Unterscheidung zwischen lokalen und globalen Variablen in einem
konkreten Beispiel.
```{code-cell} python
def f(x):
    x = x+1
    print(f"lokal:  x = {locals()['x']}")
    print(f"global: x = {globals()['x']}")
    print(f"global: y = {globals()['y']}")
    return x*y

x = 5
y = 2
print(f"{f(3) = }")
print(f"{x = }")
```
Außerhalb der Funktion {func}`f` sind die globalen Variablen `x` und `y` mit ihren Werten
5 und 2 definiert. In der vorletzten Zeile wird dann die Funktion {func}`f` mit dem Argument
3 aufgerufen. Damit hat die lokale Variable `x` im Innern der Funktion diesen Wert. In der
ersten Zeile des Funktionskörpers wird `x` dann auf den Wert 4 inkrementiert. Dabei nehmen
sowohl die linke als auch die rechte Seite Bezug auf die lokale Variable `x`, deren Wert
über das Funktionsargument gesetzt wurde. Die globale Variable `x` mit ihrem Wert 5 spielt
für die Rechnung keine Rolle, da die lokale Variable Vorrang hat.

Nach der Inkrementierung der Variablen `x` sehen wir uns die innerhalb der Funktion bekannten
lokalen und globalen Variablen an. Die lokale Variable `x` hat den Wert 4 und ein Bezug auf eine
Variable mit dem Namen `x` wird innerhalb der Funktion diesen Wert liefern, sofern nicht im
weiteren Verlauf ein anderer Wert zugewiesen wird. Ferner ist eine globale Variable `x` mit
dem Wert 5 bekannt, auf die aber nicht unter dem Namen `x` direkt zugegriffen werden kann.
Schließlich gibt es noch die globale Variable `y`, die den Wert 2 besitzt.

```{admonition} Hinweis
Die meisten globale Objekte können innerhalb einer Funktion nicht verändert werden. Eine 
Ausnahme sind Listen, so dass bei deren Modifikation innerhalb einer Funktion besondere
Vorstcht geboten ist. Auf die Besonderheiten von Listen werden in {numref}`zusgdatentypen`
genauer eingehen.
```

Der Rückgabewert der Funktion ergibt sich nun aus dem Produkt der lokalen Variable `x` und
der globalen Variable `y` zu 4 mal 2, also 8. Außerhalb der Funktion hat die Variable `x`
weiterhin den Wert 5. Dieser wurde durch die Inkrementierung der lokalen Variable `x` innerhalb
der Funktion also nicht berührt.

Betrachten wir abschließend noch eine abgewandelte Form des vorigen Beispiels, in der neben der
Variablen `x` auch die Variable `y` inkrementiert wird. Durch diesen Umstand wird `y` zu einer
lokalen Variablen, und zwar in der gesamten Funktion. Dies hat insbesondere zur Folge, dass
auf der rechten Seite der zweiten Zeile des Funktionskörpers der Wert der lokalen Variablen `y`
benötigt wird. Da diese aber nicht existiert, kommt es hierzu zu einem `UnboundLocalError`.

```{code-cell} python
---
tags: [raises-exception]
---
def f(x):
    x = x+1
    y = y+1
    return x*y

x = 5
y = 2
print(f"{f(3) = }")
```

## Rekursive Funktionen

## Funktionen als Argumente von Funktionen

(lambdafunktionen)=
## Lambda-Funktionen

(kwargs)=
## Schlüsselworte und Defaultwerte
