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

(oop)=
# Objektorientiertes Programmieren

```{admonition} Hinweis
:class: warning
Dieses Kapitel befindet sich noch in Bearbeitung.
```

Beim objektorientierten Programmieren handelt es sich um ein Paradigma, das man nutzen
kann, aber nicht muss. So war objektorientiertes Programmieren in älteren Versionen
von FORTRAN überhaupt nicht möglich und andererseits gibt es Programmiersprachen wie
zum Beispiel Java, in denen man nur objektorientiert programmieren kann. Python ermöglicht
zwar objektorientiertes Programmieren, erzwingt es aber nicht. Daher sollte man zumindest
eine Vorstellung davon haben, was die Grundideen des objektorientierten Programmierens
sind, um bei konkreten Problemstellungen erkennen zu können, ob und in welchem Maße es
sich lohnt, diesem Programmierparadigma zu folgen.

## Klassen, Attribute und Methoden

Tatsächlich ist Python objektorientiert konzipiert, so dass wir in den bisherigen Kapiteln
bereits Spuren von objektorientiertem Programmieren gesehen haben, ohne dass dies groß
thematisiert wurde. Für einen allerersten Einblick wollen wir das nun an ein paar Beispielen
nachholen. Als Einstieg dienen uns dabei der Datentyp der komplexen Zahlen. Aus Pythonsicht
gibt es die Klassendefinition der Klasse `complex`, die gewissermaßen den allgemeinen
Bauplan für komplexe Zahlen enthält. Eine konkrete komplexe Zahl ist dann eine Instanz dieser
Klasse.
```{code-cell} python
x = 2+1j
x.__class__.__name__
```
Objekte können Attribute haben, also Eigenschaften besitzen. Bei komplexen Zahlen sind dies
Real- und Imaginärteil, die, wie wir aus {numref}`complex` wissen, auf die folgende Weise
erhalten können.
```{code-cell} python
x.real, x.imag
```
Nach dem Namen der Instanz folgt also der durch einen Punkt abgetrennte Attributname.

Darüber hinaus kann es Methoden geben, also im Grunde genommen Funktionen, die mit den entsprechenden
Objekten verknüpft sind. So erfolgt die Umwandlung einer komplexen Zahl mit Hilfe der Methode
{func}`conjugate`.
```{code-cell} python
x.conjugate()
```
Auch hier folgt dem Namen der Instanz der durch einen Punkt abgetrennte Methodenname. Natürlich
können Methoden auch Argumente besitzen. Als Beispiel nennen wir die {func}`index`-Methode von
Listen.
```{code-cell} python
mylist = [1, 4, 7, 21]
mylist.index(7)
```

Das Beispiel der komplexen Zahlen verdeutlicht einen der wesentlichen Vorteile des objektorientierten
Programmierens. Die komplexe Zahl, in unserem Beispiel `x`, wird als ein Objekt verstanden und nicht
separat als Real- und Imaginärteil der betreffenden Zahl. Dies ermöglicht es uns, zum Beispiel die
komplexe Konjugation direkt auf die komplexe Zahl operieren zu lassen und nicht Real- und Imaginärteil
zu betrachten. Trotzdem kann man bei Bedarf jederzeit auf den Real- und den Imaginärteil zugreifen.
Weil man nun in diesen Objekten denkt, kann ein Programm, das diese Objekte verwendet, konzeptionell
deutlich übersichtlicher und leichter verständlich werden, was bei der Fehlersuche helfen kann.
Außerdem werden die Attribute gekapselt, so dass man sich nicht ständig um diese kümmern muss.

Nach diesen Vorbemerkungen müssen wir uns nun ansehen, wie sich eine Klasse mit ihren Attributen
und Methoden definieren lässt. Dies wollen wir anhand eines Beispiels tun, in dem eine Klasse
für Vektoren in zwei Dimensionen definiert wird. Am Ende können wir mit solchen Vektoren als
eigenständigen Objekten arbeiten. Eigenschaften wie die Vektorkomponenten können dabei, wie gerade
schon für die komplexen Zahlen besprochen, häufig im Hintergrund bleiben, wie wir gleich noch
sehen werden.

Wir werden die Klassendefinition für zweidimensionale Vektoren schrittweise aufbauen und dabei
verschiedene Aspekte besprechen. Unsere erste Version ist durch den folgenden Code gegeben.

```{code-cell} python
from math import cos, sin

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def rotate(self, phi):
        x = cos(phi)*self.x - sin(phi)*self.y
        y = sin(phi)*self.x + cos(phi)*self.y
        return Vector2d(x, y)
```
Hier werden zunächst zwei trigonometrische Funktionen importiert, die wir benötigen werden,
um Vektoren in der Ebene zu drehen. Die eigentliche Klassendefinition beginnt dann in der
dritten Zeile mit dem Schlüsselwort. Der Name der Klasse, hier `Vector2d`, beginnt üblicherweise
mit einem Großbuchstaben und die Zeile wird ähnlich wie in einer Funktionsdefinition mit einem
Doppelpunkt abgeschlossen.

Es folgen drei Methoden, wobei die ersten beiden Namen tragen, die mit einem doppelten Unterstrich
beginnen und enden. Dadurch wird angedeutet, dass diese Methoden für Python eine besondere Bedeutung
haben. Die {func}`__init__`-Methode wird ausgeführt, wenn eine Instanz der Klasse erzeugt wird.
```{code-cell} python
v1 = Vector2d(2, 1)
v1
```
Wie wir sehen, hat die {func}`__init__`-Methode drei Argumente. Bei der Instantiierung ist aber ein
Argument weniger anzugeben, da das erste Argument der {func}`__init__`-Methode, das üblicherweise
`self` genannt wird, eine besondere Funktion erfüllt. Es steht gewissermaßen für die spezifische
Instanz und erlaubt es, diese Instanz den verschiedenen Methoden zugänglich zu machen, wie wir
noch genauer sehen werden. In der {func}`__init__`-Methode werden die übergebenen Parameter je
nach Bedarf verarbeitet und in Attributen gespeichert sowie weitere zu Beginn erforderlich
Operationen durchgeführt. In unserem speziellen Fall müssen wir nur dafür sorgen, dass die in
den Parametern `x` und `y` vorliegenden Vektorkomponenten anschließend über entsprechende Attribute
zugänglich sind. Dazu weisen wir sie `self.x` beziehungsweise `self.y` zu. Damit können
wir auch nach der erfolgten Instantiierung auf die Attribute zugreifen.
```{code-cell} python
print(v1.x, v1.y)
```
Die Verwandtschaft mit der Bestimmung des Real- und Imaginärteils komplexer Zahlen, die wir eingangs
betrachtet hatten, ist offensichtlich.

Eine nützliche Methode, die wir oben bereits definiert haben, ist die {func}`__str__`-Methode, die
von Python dann aufgerufen wird, wenn das Objekt in eine Zeichenkette umgewandelt werden muss, wie dies
beispielsweise durch die {func}`print`-Funktion geschieht. Wir lassen die Vektorkomponenten ausgeben,
um später leicht die Auswirkungen von weiteren Methoden unserer Klasse {class}`Vector2d` zu überprüfen. Da die
{func}`__str__`-Methode das Argument `self` besitzt, haben wir in dieser Methode Zugriff auf die
Attribute des Objekts, also in unserem Fall auf die Vektorkomponenten.
```{code-cell} python
print(v1)
```

Die dritte, oben definierte Methode {func}`rotate` soll es erlauben, den Vektor um einen Winkel `phi` in
der $x$--$y$-Ebene zu drehen.
```{code-cell} python
from math import pi

print(v1.rotate(pi/2))
```
Wie wir dem Code der {func}`rotate`-Methode entnehmen können, wird als Ergebnis eine neue Instanz der
{class}`Vector2d` erzeugt. Alternativ hätten wir die Vektorkomponenten nach der Drehung `self.x` und `self.y`
zuweisen können. Dann hätten wir lediglich die Attribute des Vektors geändert ohne einen neuen Vektor
zu erzeugen.

Der Wert von Attributen kann auch explizit durch Zuweisung geändert werden.
```{code-cell} python
print(v1)
v1.x = 4
print(v1)
```
Oft werden hierfür spezielle Methoden zur Verfügung gestellt, um überprüfen zu können, ob der neue Wert
gültig ist.

Für Vektoren wird man sicherlich auch eine Methode erwarten, die die Länge des Vektors bestimmt. Eine solche
Methode, die wir {func}`norm` nennen, lässt sich leicht mit Hilfe der {func}`hypot`-Funktion aus dem 
`math`-Modul implementieren. Die erweiterte Klassendefinition geben wir nachfolgend vollständig wieder.
```{code-cell} python
from math import cos, sin, hypot

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    @property
    def norm(self):
        return hypot(self.x, self.y)

    def rotate(self, phi):
        x = cos(phi)*self.x - sin(phi)*self.y
        y = sin(phi)*self.x + cos(phi)*self.y
        return Vector2d(x, y)
```
Würden wir die mit `@` beginnende Zeile, einen sogenannten Dekorator, weglassen, so würde es sich bei
{func}`norm` einfach um eine Methode handeln, wie wir sie von der {func}`rotate`-Methode her kennen. Der
Dekorator `@property` wandelt diese Methode jedoch in eine Eigenschaft um, auf deren Wert wir wie bei
einem Attribut zugreifen können.
```{code-cell} python
v1 = Vector2d(2, 1)
print(v1.norm)
```
Es ist jedoch nicht möglich, den Wert dieses Attributs zu setzen.
```{code-cell} python
---
tags: [raises-exception]
---
v1.norm = 10
```

Im Zusammenhang mit dem Setzen von Attributen ist noch wichtig zu wissen, dass man auch den Wert
von nicht in der Klassendefinition vorkommenden Attributen im Prinzip setzen kann. Das kann bei
Tippfehlern zu unerwartetem Verhalten führen. Dieser Umstand zeigt nochmals, dass es sinnvoll sein
kann, explizite Methoden zum Setzen und auch zum Auslesen von Attributen zu implementieren.
```{code-cell} python
v1.z = -4
print(v1)
print(v1.z)
```

Um noch etwas deutlicher zu sehen, wie es das objektorientiertes Programmieren erlaubt, mit den Objekten
als eigene Einheit zu arbeiten, wollen wir unsere Beispielklasse ein letztes Mal erweitern.
Unser letztliches Ziel soll dabei sein, eine Methode zum Spiegeln eines Vektors an einem Normalenvektor,
der einen bestimmten Winkel mit der $x$-Achse einschließt, zu implementieren.

Dazu überlegen wir uns zunächst, wie wir diese allgemeine Spiegelung mathematisch bewerkstelligen
können. Dazu bezeichnen wir den ursprünglichen Vektor als $\vec v$, den gespiegelten Vektor als 
${\vec v}'$, und die Spiegelachse werde durch den Normalenvektor $\vec n$ spezifiziert. Dann können
wir $\vec v$ in den Anteil in Richtung von $\vec n$ sowie den dazu senkrechten Anteil zerlegen.
Es ist also

$$\begin{align}
   \vec v_\parallel &= \left(\vec v\cdot\vec n\right)\vec n\\
   \vec v_\perp &= \vec v-\vec v_\parallel\,.
\end{align}$$

Der gespiegelte Vektor ergibt sich dann zu

$${\vec v}' = \vec v_\parallel-\vec v_\perp = 2\left(\vec v\cdot\vec n\right)\vec n - \vec v\,.$$

Hieraus folgt, dass wir die Spiegelung alleine mit Hilfe der beteiligten Vektoren vornehmen
können, ohne die einzelnen Komponenten der Vektoren explizit ins Spiel bringen zu müssen. Dazu
müssen wir aber in der Lage sein Vektoren zu subtrahieren, mit reellen Zahlen zu multiplizieren
und ein Skalarprodukt auszuwerten.

Wir geben zunächst die vollständige, um einige Methoden ergänzte Klassendefinition von {class}`Vector2d`
an und besprechen anschließend die neu hinzugefügten Methoden.
```{code-cell} python
from math import cos, hypot, sin, pi

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vector2d(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2d(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2d):
             return self.x*other.x + self.y*other.y
        elif isinstance(other, float) or isinstance(other, int):
             return Vector2d(other*self.x, other*self.y)
        raise TypeError(f'Vector2d kann nicht mit {type(other)} multipliziert werden.')

    __rmul__ = __mul__

    @property
    def norm(self):
        return hypot(self.x, self.y)

    def rotate(self, phi):
        x = cos(phi)*self.x - sin(phi)*self.y
        y = sin(phi)*self.x + cos(phi)*self.y
        return Vector2d(x, y)

    def mirror(self, phi):
        n = Vector2d(cos(phi), sin(phi))
        parallel = (self*n)*n
        return 2*parallel - self

    def orthogonal(self):
        return self.rotate(0.5*pi)
```

Zunächst sehen wir uns die Methoden {func}`__add__` und {func}`__sub__` an, die
von Python unter anderem dann aufgerufen werden, wenn zwei Objekte mit einem Plus- 
beziehungsweise Minuszeichen verknüpft werden. Der erste Vektor entspricht dem Argument
`self` und das zweite Argument `other` entspricht dem zweiten Vektor. Die entsprechenden
Operationen haben wir entsprechend komponentenweise implementiert.
```{code-cell} python
v1 = Vector2d(1, 2)
v2 = Vector2d(-2, 3)
print(f'{v1+v2}   {v1-v2}')
```
Für eine bessere Implementation sollte man natürlich noch überprüfen, ob `other` wirklich eine
Instanz von {class}`Vector2d` ist. Dies werden wir in der nächsten Methode besser machen.

Die {func}`__mul__`-Methode wird von Python unter anderem dann aufgerufen, wenn zwei Objekte
mit dem Multiplikationsstern verknüpft werden. Für die Spiegelung eines Vektors müssen wir
dabei zwei Fälle unterscheiden, Während sichergestellt ist, dass `self` immer eine Instanz von
{class}`Vector2d` ist, soll das Verhalten der {func}`__mul__`-Methode davon abhängen, ob `other`
ebenfalls eine Instanz dieser Klasse ist oder aber eine Gleitkommazahl (`float`) oder ein 
Integer (`int`). Im ersten Fall haben wir ein Skalarprodukt implementiert und im zweiten Fall
multiplizieren wir die beiden Komponenten mit der betreffenden Zahl. Trifft keiner der beiden
Fälle zu, geben wir eine entsprechende Fehlermeldung aus.
```{code-cell} python
print(f'{v1}*{v2} = {v1*v2}')
print(f'{v1}*5 = {v1*5}')
```
Leider funktioniert die umgekehrte Reihenfolge noch nicht, was sich aber dadurch beheben lässt,
dass man eine Methode {func}`__rmul__` definiert, die von Python aufgerufen wird, wenn {func}`__mul__`
fehlschlägt, und das die beiden Argumente `self` und `other` vertauscht.
```{code-cell} python
print(f'5*{v1} = {5*v1}')
```
Nun ist es ein Leichtes, die Spiegelung entsprechend der zuvor hergeleiteten Formeln zu implementieren.
Wir überprüfen, ob die Spiegelungen an der $x$- und der $y$-Achse sowie an der ersten Winkelhalbierenden
die erwarteten Ergebnisse liefern.
```{code-cell} python
print(v1)
for phi in (0, pi/2, pi/4):
    print(v1.mirror(phi))
```

Ganz am Ende der Klassendefinition haben wir noch eine Methode hinzugefügt, die
mit der Spiegelung nichts zu tun hat, sondern demonstriert, wie man Methoden
innerhalb der Klassendefinition aufruft.  Die Methode {func}`orthogonal`
bestimmt einen zum gegebenen Vektor senkrechten Vektor. Auch wenn es nicht die
optimale Lösung darstellt, rotieren wir den Vektor dazu mit Hilfe der Methode
{func}`rotate` um $\pi/2$. Wir sehen hier, dass man beim Aufruf `self.` voranstellen
muss. Unterlässt man das, sucht Python nach einer Funktion mit entsprechendem Namen
außerhalb der Klassendefinition. Nachdem `self` bereits dem Methodennamen vorangestellt
wurde, muss es in der Liste der Argumente entfallen. Diese scheinbar unterschiedliche
Anzahl von Argumenten kann gerade am Anfang zu Verwirrung führen.

## Vererbung

Es kommt immer wieder vor, dass man man mehrere Klassen implementieren möchte, die
in einem hierarchischen Verhältnis zueinander stehen. Eine oberste Klasse hat dann
typischerweise nur wenige Attribute und Methoden definiert, die aber an eine
darunter stehende Klasse vererbt werden können. Diese zweite Klasse kann dann noch
eigene Attribute oder Methoden definieren oder auch Methoden der ersten Klasse 
überschreiben.

Als Beispiel betrachten wir einen Massenpunkt und eine ausgedehnte Masse, wobei wir
uns der Einfachheit halber auf den zweidimensionalen Fall beschränken wollen. Die
Lage des Massenpunktes ist dann durch zwei Koordinaten definiert und man kann eine
Methode definieren, die dazu dient den Massenpunkt zu verschieben. In der Realität
würde man vielleicht auch die Masse und die Geschwindigkeit des Massenpunkts
berücksichtigen, aber darauf wollen wir der Einfachheit halber hier verzichten.

Einer ausgedehnten Masse kann man im Gegensatz zum Massenpunkt noch eine Orientierung
zuordnen und genauso wie man den Massenpunkt oder die Masse verschieben kann, kann
man die Masse auch um einen Winkel drehen. 

In diesem Fall ist es also sinnvoll, zunächst eine Klasse für den Massenpunkt zu
definieren, die dann ihre Attribute und Methoden an die Klasse vererbt, die die
ausgedehnte Masse beschreibt.

Wir beginnen also mit einem Massenpunkt und definieren die Klasse {class}`Massenpunkt`.
Wenn nichts anderes angegeben ist, liege der Massenpunkt anfänglich im Ursprung. 
Zudem erlaubt es die {func}`shift`-Methode, den Massenpunkt zu verschieben. Die
{func}`__str__`-Methode sorgt dafür, dass wir leicht die Position des Massenpunktes
ausgeben lassen können.

```{code-cell} python
class Massenpunkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Massenpunkt am Ort ({self.x}, {self.y})'

    def shift(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
```
Der folgende Code zeigt, wie man mit der gerade definierten Klasse arbeiten kann.
```{code-cell} python
m1 = Massenpunkt()
print(m1)
m1.shift(1, 2)
print(m1)
m1.shift(-2.5, 3)
print(m1)
```

Nun gehen wir zu einer ausgedehnten Masse über und definieren die Klasse
{class}`AusgedehnteMasse`, die von der Klasse {class}`Massenpunkt` abgeleitet
wird, also Attribute und Methoden erbt.  Entsprechend wird die Klasse
{class}`Massenpunkt`, die sogenannte Elternklasse, in Klammern angegeben. Es
ist zwar auch möglich, von mehreren Klassen zu erben, worauf wir an dieser
Stelle jedoch nicht eingehen können. In einem solchen Fall muss man sich dann
um Fragen kümmern wie von welcher Klasse eine bestimmte Methode geerbt wird.
Dies wird zum Beispiel dann relevant, wenn mehrere der Elternklassen eine
Methode mit gleichem Namen implementieren.

Die {func}`__init__`-Methode der Klasse {class}`AusgedehnteMasse` besitzt
nun drei statt nur zwei Argumente. Hinzugekommen ist ein Winkel in Grad,
der die Ausrichtung der Masse charakterisiert, und wiederum einen Defaultwert
besitzt. Der Wert des Winkels wird in einem Attribut gespeichert und dann
eine Methode {func}`normalise` aufgerufen, die sicherstellt, dass der Winkel
zwischen 0° und 360° liegt. Da der Winkel kein Integer sein muss, genügt
hier nicht eine einfache Modulooperation. Bei dieser Gelegenheit betonen
wir noch einmal, dass beim Aufruf einer in der Klasse definierten Methode
ein `self.` vor den Methodennamen gestellt werden muss und dafür das
Argument `self` in der Argumentliste entfällt. Die Verarbeitung der beiden
Argumente `x` und `y` überlassen wir der {func}`__init__`-Methode der
Elternklasse, die wir mit Hilfe der {func}`super`-Methode erhalten.

Die {func}`__str__`-Methode, die nützliche Information über eine Instanz
ausgeben soll, wird nicht aus der Elternklasse übernommen, sondern 
überschrieben, da zusätzlich die Ausrichtung der Masse ausgeben wollen.
Ein Methode, die diese Klasse neu definiert, ist {func}`rotate`, die die
Masse um einen gewissen Winkel um die durch den aktuellen Ort verlaufende
Achse senkrecht zur $x-y$-Ebene dreht.

```{code-cell} python
class AusgedehnteMasse(Massenpunkt):
    def __init__(self, x=0, y=0, phi_deg=0):
        self.phi_deg = phi_deg
        self.normalise()
        super().__init__(x, y)

    def normalise(self):
        self.phi_deg = self.phi_deg - (self.phi_deg // 360)*360

    def __str__(self):
        return f'Masse am Ort ({self.x}, {self.y}) mit Ausrichtung {self.phi_deg}°'

    def rotate(self, phi_deg):
        self.phi_deg = self.phi_deg + phi_deg
        self.normalise()
```
Die folgende Sequenz aus Verschiebungen und Drehungen zeigt, dass obwohl
die Klasse `AusgedehnteMasse` nicht selbst eine {func}`shift` implementiert,
diese aus der Elternklasse `Massenpunkt` geerbt wurde.
```{code-cell} python
m2 = AusgedehnteMasse()
print(m2)
m2.shift(1, 2)
print(m2)
m2.rotate(270)
print(m2)
m2.shift(-3, 2.5)
m2.rotate(100.5)
print(m2)
```
Außerdem zeigt die letzte Ausgabe, dass die Reduktion des Winkels auf das
Intervall von 0° bis 360° in der {func}`rotate`-Methode funktioniert. Wir
erwähnen nochmals, dass es wichtig ist, Methoden innerhalb der Klassendefinition
mit einem vorangestellten `self.` aufzurufen und dafür beim Aufruf das Argument
`self` wegzulassen.
