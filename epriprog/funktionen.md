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

(fdef)=
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
`f` definiert. Sie wird zu diesem Zeitpunkt jedoch nicht ausgeführt. Es erfolgt als insbesondere
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
kennengelernt hatten, wo `help(math)` die Dokumentation für das {mod}`math`-Modul ausgab.
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
Vorsicht geboten ist. Auf die Besonderheiten von Listen werden in {numref}`zusgdatentypen`
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

Darf man in einer Funktion die Funktion selbst wieder aufrufen? In Sprachen wie Python, C und
modernen Versionen von Fortran ist dies möglich. In Fortran 77 musste man dafür noch in die
Trickkiste greifen. Eine Funktion, die in sich selbst wieder aufgerufen wird, wenn auch mit 
anderen Werten für die Argumente, nennt man eine rekursive Funktion. Zur Erläuterung betrachten
wir zunächst ein mathematisches Beispiel.

Die Fakultät $n!$ einer ganzen Zahl $n$ ist definiert als das Produkt der ganzen Zahlen von $1$ bis
$n$, also

$$n! = \prod_{k=1}^n k = 1\cdot 2\cdot\ldots\cdot(n-1)\cdot n\,.$$

Alternativ kann man die Fakultät auch rekursiv definieren als

$$n! = n\cdot(n-1)!\,,\ 1!=1\,.$$

Hierbei wird die Auswertung der Fakultät auf die Auswertung der Fakultät für eine um Eins kleinere
Zahl reduziert. So lässt sich sukzessive das Argument der auszuwertenden Fakultät reduzieren, was
natürlich nur etwas nützt, wenn diese Folge irgendwann abbricht. In unserem Fall geschieht dies
dadurch, dass die Fakultät von $1$ zu $1$ definiert wird.

Wir setzen diese mathematischen Formeln nun in Programmcode um und beginnen mit der expliziten
Produktdarstellung.

```{code-cell} python
def fakultaet(n):
    produkt = 1
    for k in range(2, n+1):
        produkt = produkt*k
    return produkt

for n in range(1, 10):
    print(n, fakultaet(n))
```

Alternativ kann man die Fakultät rekursiv implementieren.
```{code-cell} python
def fakultaet_rekursiv(n):
    if n > 1:
        return n*fakultaet_rekursiv(n-1)
    elif n == 1:
        return 1
    else:
        raise ValueError("Das Argument muss größer als Null sein.")

for n in range(1, 10):
    print(n, fakultaet_rekursiv(n))
```
Sehen wir uns diese Implementierung etwas genauer an. So lange das Argument `n` größer als Eins ist,
wird einfach die Rekursionsformel implementiert. Es wird als Ergebnis also einfach `n` mal die Fakultät
von `n-1` zurückgegeben. Dabei muss aber zunächst diese Fakultät berechnet werden. Auf diese Weise
arbeitet man sich sukzessive zu immer kleineren Argumenten bis `n` den Wert `1` erreicht. In diesem Fall
bricht die Rekursion ab, und es wird direkt das Resultat `1` zurückgegeben. Nachdem dieser Wert erhalten
wurde, können sukzessive die Resultate der einzelnen Funktionsaufrufe bestimmt werden bis am Ende das
gewünschte Ergebnis erhalten wird. Diesen Vorgang werden wir gleich noch etwas genauer veranschaulichen.

Zuvor wollen wir aber noch darauf hinweisen, dass unsere Funktion noch eine Fehlerbehandlung
durchführt, die verhindert, dass die Rekursion nie zu Ende kommt. Sollte das Argument `n` nämlich
kleiner gleich Null sein oder keine ganze Zahl sein, würde man nie die Abbruchbedingung erreichen,
bei der `n` gleich Eins ist.  Damit wären wir in einer Endlosschleife gefangen. Bei rekursiven
Funktionen ist es also immer essentiell wichtig, darauf zu achten, dass die Abbruchbedingung korrekt
implementiert ist. 

```{admonition} Maximale Rekursionstiefe in Python
In Python ist die Rekursionstiefe standardmäßig auf 1000 begrenzt, wie sich mit Hilfe von 
{func}`sys.getrecursionlimit` verifizieren lässt. Damit ist einerseits die Gefahr von Endlosschleifen
etwas entschärft. In unserem Beispiel wäre aber die Größe des Arguments `n` dadurch begrenzt. Bei
Bedarf lässt sich die maximale Rekursionstiefe mit {func}`sys.setrecursionlimit` anpassen. Zuvor
sollte man aber sicherstellen, dass die Abbruchbedingung für die Rekursion tatsächlich korrekt
funktioniert.
```

Um den Ablauf der Rekursion zu veranschaulichen, modifizieren wir unser Programm noch ein klein
wenig.
```{code-cell} python
def fakultaet_rekursiv(n):
    print(f"** Aufruf mit Argument {n = }")
    if n > 1:
        ergebnis = n*fakultaet_rekursiv(n-1)
        print(f"-> {n}! = {ergebnis}")
        return ergebnis
    elif n == 1:
        ergebnis = 1
        print(f"-> {n}! = {ergebnis}")
        return ergebnis
    else:
        raise ValueError("Das Argument muss größer gleich Eins sein.")

fakultaet_rekursiv(5)
```
Hier wird deutlich, wie zunächst nacheinander die Funktion mit fallenden Argumenten aufgerufen
wird und dann sukzessive die Resultate aufgebaut werden, nachdem das Ende der Rekursion
erreicht wurde.

(fccfunc)=
## Funktionen als Bürger erster Klasse

````{margin}
```{admonition} Literaturverweis
Das Konzept von Objekten oder Bürgern erster Klasse wurde im Zusammenhang mit Programmiersprachen
1967 von Christopher Strachey eingeführt: C. Strachey, [Higher-order Symb. Comput. *13*, 11
(2000)](https://doi.org/10.1023/A:1010000313106)
```
````
In diesem Kapitel haben wir bis jetzt Funktionen definiert und diese aufgerufen. Die Funktion
wurde dann ausgeführt, und wir haben ein Ergebnis erhalten. Diese Möglichkeiten, mit Funktionen
zu arbeiten, kann man für alle Programmiersprachen erwarten. Es gibt jedoch Programmiersprachen,
zu denen auch Python gehört, in denen mit Funktionen genauso wie mit anderen Objekten, also zum
Beispiel Variablen umgegangen werden kann. Man spricht dann davon, dass Funktionen *first class
citizens*, also Bürger erster Klasse, sind, die im Vergleich zu anderen Objekten nicht in ihren
Möglichkeiten eingeschränkt sind.

Was sind also die zusätzlichen Möglichkeiten, die sich daraus ergeben, dass Funktionen *first class
objects* oder *first class citizens* sind? Funktionen können dann Variablen zugewiesen werden,
sie können als Argumente an Funktionen übergeben werden oder beispielsweise auch als Elemente in
Listen auftreten. Wir wollen dies an Beispielen illustrieren.
```{code-cell} python
from math import sin

funktion = sin
print(funktion(1), sin(1))
print(funktion)
print(sin)
```
Hier wird der Variablen `funktion` die Sinusfunktion `sin` aus dem {mod}`math`-Modul zugewiesen.
Wichtig ist an dieser Stelle, dass keine Klammer gesetzt werden, wie man es bei einem
Funktionsaufruf tun müsste. Nur dann bezieht man sich auf das Funktionsobjekt. Die Variable
`funktion` kann nun mit Argumenten genauso aufgerufen werden, wie das für `sin` möglich ist, und
wir stellen fest, dass sich erwartungsgemäß auch das gleiche Ergebnis ergibt. Übergibt man das
Funktionsobjekt, also nicht das Ergebnis einer Funktionsauswertung, an die {func}`print`-Funktion,
so wird ein beschreibender Text ausgegeben, der zeigt, dass `funktion` tatsächlich auf die
eingebaute Funktion `sin` verweist.

Wie schon erwähnt, können Funktionsobjekte auch als Elemente einer Liste auftreten. Dabei spielt
es keine Rolle, ob die betreffenden Funktionen importiert oder selbst definiert wurden.
```{code-cell} python
from math import cos, sin

def myfunc(x):
    return x**2 - 4*x + 4

for f in [cos, sin, myfunc]:
    print(f"{f.__name__:6s}: {f(1):8.6f}")
```
Für die Ausgabe des Funktionsnamens haben wir uns dabei des Attributs `__name__` bedient, wobei hier
vor und nach dem Text `name` jeweils zwei Unterstriche stehen.

Funktionen als Argumente an andere Funktionen übergeben zu können, eröffnet interessante
Möglichkeiten. Wir wollen dies an einem Beispiel demonstrieren, das numerisch näherungsweise die
Ableitung einer Funktion an einer vorgegebenen Stelle bestimmen soll.
```{code-cell} python
from math import cos, sin

def ableitung(f, x):
    h = 1e-7
    df = (f(x+h)-f(x-h))/(2*h)
    return df

print(f"{ableitung(sin, 0) = }")
print(f"{ableitung(cos, 0) = }")
```
Hier wird der Differenzenquotient für eine kleine, aber fest vorgegebene Schrittweite ausgewertet.
Als Argumente werden sowohl die Funktion, hier Sinus und Kosinus, sowie die Stelle, an der die
Ableitung auszuwerten ist, übergeben. Es sei noch einmal betont, dass bei der Übergabe des
Funktionsobjekts keine Klammern gesetzt werden dürfen.

Natürlich kann der Code für die Ableitung noch verbessert werden, zum Beispiel weil die Wahl einer
festen Schrittweite nicht unbedingt ideal ist. Immerhin kommen alle Verbesserung des Codes der
Auswertung der Ableitung von im Prinzip beliebigen Funktionen zugute. Im {numref}`kwargs` werden
wir dieses Beispiel noch weiter entwickeln.

(lambdafunktionen)=
## Lambda-Funktionen

Im {numref}`fdef` hatten wir Beispiele für Funktionen kennengelernt, bei denen die Bestimmung der
Ergebnisses in einer einzelnen Codezeile erfolgte. Bei machen Gelegenheiten erscheint dann die
vollständige Definition einer Funktion als unnötig aufwändig. Tatsächlich erlauben es die
sogenannten Lambda-Funktionen, eine Funktion in einer einzigen Zeile zu definieren. Der Name dieser
Funktionen stammt aus dem Lambda-Kalkül, in dem die Lambda-Funktionen einen wichtige Rolle spielen.
Dies erklärt auch, warum `lambda` zu den reservierten Schlüsselwörtern in Python gehört und nicht
als Variablenname verwendet werden kann. Ein Beispiel soll die Definition einer Lambda-Funktion 
illustrieren.
```{code-cell} python
quadrat = lambda x: x**2
potenz = lambda x, y: x**y
print(quadrat(9), potenz(3, 4))
```
Nach dem Schlüsselwort `lambda` folgt ein oder mehrere Argumente gefolgt von einem Doppelpunkt.
Der letzte Ausdruck gibt an, wie der Rückgabewert zu bestimmen ist. 

Lambda-Funktionen werden auch als anonyme Funktionen bezeichnet, da sie nicht unbedingt einen
Namen tragen müssen. Dies kann zum Beispiel dann nützlich sein, wenn das Ergebnis einer Funktion
wiederum eine Funktion sein soll. Die Funktion {func}`potenz` gibt in Abhängigkeit von dem
übergebenen Argument eine Funktion zurück, die die entsprechende Potenz eines Arguments berechnet.
So werden hier das Quadrat (`square`) und die dritte Potenz (`cubic`) mit Hilfe der einen Funktion
`potenz` definiert.
```{code-cell} python
def potenz(exponent):
    return lambda x: x**exponent

square = potenz(2)
cubic = potenz(3)
print(square(5), cubic(5))
```
Auch bei Anwendungen der im {numref}`fccfunc` definierten Ableitungsfunktion können anonyme
Funktionen nützlich sein, wenn man die Ableitung einer selbst definierten Funktion numerisch
berechnen möchte. In dem folgenden Beispiel soll die Ableitung von $f(x)=x^3$ berechnet werden.
```{code-cell} python
def ableitung(f, x):
    h = 1e-7
    df = (f(x+h)-f(x-h))/(2*h)
    return df

print(ableitung(lambda x: x**3, 1))
```
Die ersten vier Zeilen enthalten die bereits zuvor verwendete Ableitungsfunktion. Beim Aufruf dieser
Funktion kann das erste Argument einfach in Form einer anonymen Funktion oder Lambda-Funktion
angegeben werden, ohne dass eine separate Funktion in der üblichen Weise definiert werden müsste.
Auf diese Weise erhalten wir hier eine numerische Näherung für die Ableitung der dritten Potenz an
der Stelle $1$.

(kwargs)=
## Schlüsselworte und Defaultwerte

Am Ende von {numref}`fdef` hatten wir gezeigt, dass bei Funktionsaufrufen mit mehreren Argumenten
die Zuordnung nicht nach dem Namen erfolgt, sondern zunächst einmal nach der Position der jeweiligen
Argumente.  Dies ist jedoch insbesondere in Fällen, in denen die Argumentliste sehr lange wird,
nicht praktisch und daher gibt es auch andere Möglichkeiten, Argumente zu übergeben.  Zur
Illustration dieser Problematik stellen wir uns eine Funktion vor, die es ermöglicht, vorgegebene
Daten graphisch darzustellen. Eine solche Funktion wird typischerweise relativ viele Argumente
haben, da man beispielsweise die Strichfarbe, die Strichdicke und die Strichart festlegen möchte.
Andererseits möchte man nicht unbedingt alle Argumente explizit angeben müssen, wenn man nur eine
schwarze durchgezogene Linie mittlerer Dicke darstellen möchte. Es sollte auch nicht so sein, dass
man, nur weil man die Stichart anpassen möchte, alle anderen Argumente, die vor dem betreffenden
Argument stehen, zwingend angeben muss.

In einem solchen Fall ist es sinnvoll, Argumente per Schlüsselwort zu übergeben. Um das Vorgehen
zu verdeutlichen, greifen wir auf die Funktion zurück, die wir am Ende des letzten Abschnitts zur
numerischen Berechnung von Ableitungen eingeführt hatten.
```{code-cell} python
def ableitung(f, x):
    h = 1e-7
    df = (f(x+h)-f(x-h))/(2*h)
    return df
```
In dem zuvor beschriebenen Funktionsaufruf
```{code-cell} python
ableitung(lambda x: x**3, 1)
```
wird das erste Argument der Variable `f` und das zweite Argument der Variable `x` in der Funktion 
zugeordnet. Alternativ kann man die Argumente mit den in der Funktion verwendeten Namen bezeichnen.
Ein mögliche Form des Funktionsaufrufs wäre dann
```{code-cell} python
ableitung(f=lambda x: x**3, x=1)
```
Hier stehen die Argumente zwar immer noch in der gleichen Reihenfolge, aber die Zuordnung erfolgt
nun über die angegebenen Bezeichner. Daher könnte man genauso gut die Reihenfolge der beiden
Argumente vertauschen.
```{code-cell} python
ableitung(x=1, f=lambda x: x**3)
```
```{admonition} Hinweis zur Formatierung
{pep}`8` empfiehlt, um Gleichheitszeichen in Zuweisungen Leerzeichen zu setzen. Anders
ist dies bei Schlüsselwortargumenten. Hier sollen um das Gleichheitszeichen keine Leerzeichen
gesetzt.
```
Beim den letzten beiden Funktionsaufrufen ist es wichtig, die verschiedenen `x` voneinander zu
unterscheiden. Die beiden `x` in der Lambdafunktion haben dabei nichts mit dem Schlüsselwort `x`
zu tun. Noch sorgfältiger muss man in dem folgenden Funktionsaufruf die verschiedenen `x`
unterscheiden.
```{code-cell} python
x = 1
ableitung(x=x, f=lambda x: x**3)
```
Im Funktionsaufruf bezeichnet das erste `x` ein Schlüsselwort, das mit einem Argumentbezeichner in 
der Funktionsdefinition übereinstimmen muss. Das zweite `x` verweist auf die Variable `x`, die nach
der Zuweisung in der ersten Zeile den Wert 1 besitzt. Die `x` im zweiten Argument bezeichnen eine
lokale Variable in der Lambdafunktion und haben nichts mit dem beiden `x` im ersten Argument zu tun.

Gerade bei längeren Argumentlisten kann es sinnvoll sein, einen Teil der Argumente über ihre
Position in der Liste zuzuordnen und andere Argumente über das zugehörige Schlüsselwort. In einem
solchen Fall müssen die Argumente mit Schlüsselwort zwingend hinter den Argumenten kommen, die über
ihre Position zugeordnet werden. Andernfalls könnten die Argumente im Allgemeinen nicht
zweifelsfrei zugeordnet werden.

Ein Nachteil unserer Ableitungsfunktion, wie sie momentan implementiert ist, besteht darin, dass die
Schrittweite `h` in der Funktion fest vorgegeben ist. Der Wert von $10^{-7}$ mag zwar vernünftig 
gewählt sein, aber es wäre sinnvoll, wenn man diesen Wert bei Bedarf anpassen könnte. In einem
solchen Fall ist es möglich, einen so genannten Defaultwert zu definieren, der dann zum Tragen
kommt, wenn nichts anderes gesagt wird. Ein verbesserte Variante der Ableitungsfunktion könnte also
wie folgt aussehen.
```{code-cell} python
def ableitung(f, x, h=1e-7):
    df = (f(x+h)-f(x-h))/(2*h)
    return df
```
Diese Funktion kann nun in verschiedener Weise aufgerufen werden. Zum einen können wir die früheren
Aufrufe übernehmen, wobei dann der Wert für `h` gleich dem angegebenen Defaultwert ist. Python wird
sich also nicht darüber beschweren, dass `h` nicht definiert sei.
```{code-cell} python
ableitung(lambda x: x**3, 1)
```
Man kann aber auch den Wert von `h` vorgeben.
```{code-cell} python
for n in range(1, 8):
    print(ableitung(lambda x: x**3, 1, 10**-n))
```
In diesem Fall werden die Argumente über ihre Position übergeben. Natürlich könnte man stattdessen
auch Schlüsselwortargumente verwenden, zum Beispiel in der Form
```{code-cell} python
for n in range(1, 8):
    print(ableitung(lambda x: x**3, h=10**-n, x=1))
```
Es sei noch einmal betont, dass in diesem Fall das Schlüsselwort `x` im letzten Argument nicht
entfallen kann, da sonst die Zuordnung nicht eindeutig ist.
```{code-cell} python
---
tags: [raises-exception]
---
ableitung(lambda x: x**3, h=10**-n, 1)
```

Abschließend sehen wir uns zur Illustration noch ein Beispiel aus der Scipy-Bibliothek an, auf die wir 
im {numref}`scipy` noch etwas genauer eingehen werden. Diese Bibliothek stellt eine Funktion zur
numerischen Integration zur Verfügung, die 14 Argumente besitzt. Die ersten drei Argumente werden 
typischerweise über ihre Position übergeben, was sich unter anderem daraus ergibt, dass es sich
hierbei um essentielle Argumente wie den Integranden und die Integrationsgrenzen handelt. Für diese
Argumente gibt es keine sinnvollen Defaultwerte. Anders ist dies bei den restlichen elf Argumenten,
für die Defaultwerte definiert sind, die bei Bedarf abgeändert werden können.
```{code-cell} python
from scipy import integrate
help(integrate.quad)
```
