---
file_format: mystnb
kernelspec:
  name: python3
---

(einausgabe)=
# Ein- und Ausgabe

Ein Programm, das eine sinnvolle Aufgabe bearbeitet, wird immer in irgendeiner Weise
kommunizieren, also Informationen entgegennehmen und insbesondere die Resultate
ausgeben. Für beiden Prozesse sind verschiedene Szenarien denkbar.

Im {numref}`vorschau` hatten wir bereits die {func}`input`-Funktion
kennengelernt, die es erlaubt, aus dem Programm heraus den Benutzer um eine
Eingabe zu bitten. Eine Alternative wäre die Angabe von Parametern direkt beim
Aufruf des Programms von der Kommandozeile. Auch die Verwendung eines
graphischen Benutzerinterfaces ist denkbar.

Bei komplexeren Problemstellungen ist es aber häufig nicht sinnvoll, alle
Parameter per Hand einzugeben, und vor allem diesen Prozess beim Programmstart
jedes Mal durchlaufen zu müssen. Dann ist es sinnvoller, vom Programm benötigte
Informationen in einer Datei zu hinterlegen und dann vom Programm einlesen zu
lassen. In manchen Fällen kann es auch sinnvoll oder erforderlich sein, Daten
aus dem Internet in das Programm zu laden.

Auch die Ausgabe von Ergebnissen kann auf verschiedene Weise erfolgen. In unseren
Beispielen haben wir bisher die Möglichkeit genutzt, Daten auf dem Bildschirm
auszugeben. Benutzt man ein graphisches Benutzerinterface, könnte man auch dort
Informationen ausgeben. Größere Datenmengen wird man dagegen in den meisten Fällen
in einer Datei abspeichern. Natürlich ist es auch möglich, die Ausgabe ins Internet
zu senden, eine Aufgabe, die jeder Webserver erledigt.

Gerade im natur- und ingenieurwissenschaftlichen Bereich, aber auch in anderen
Bereichen, die mit großen Datenmengen umgehen müssen, wird man die Daten oft
grafisch geeignet darstellen. Hier stellt sich häufig die Frage, ob man für die
Grafik benötigte Daten zunächst abspeichert oder aber direkt weiterverarbeitet.
Ein wesentlicher Faktor wird dabei der Aufwand für die Erzeugung der Daten sein.
Es ist sehr ärgerlich, die Ergebnisse einer mehrtägigen Rechnung nur deswegen
zu verlieren, weil man in der Auswertung oder der Erzeugung der Grafik einen Fehler
eingebaut hat. Können die Daten dagegen sehr schnell erzeugt werden, kann der
Weg über eine Zwischenspeicherung der Daten lästig sein, beispielsweise wenn
man schnell die Auswirkung von Parameteränderungen im Ergebnis ansehen möchte.

Wie schon aus diesen einleitenden Bemerkungen deutlich wird, kann die Ein- und Ausgabe
von Daten ein im Detail komplexes Thema sein. Wir wollen im Folgenden zunächst relativ
knapp auf die Eingabe über die Kommandozeile und die Tastatur eingehen und auch
noch einmal einen kurzen Blick auf die {func}`print`-Funktion werfen. Danach werden
wir uns vor allem mit dem Lesen und Schreiben von Dateien beschäftigen. Für speziellere
Aspekte werden wir in weiterführenden Hinweisen zeigen, dass Python für viele der
potentiell anfallenden Aufgaben nützliche Module in der Standardbibliothek bereit hält.

(commandline)=
## Eingabe über die Kommandozeile und die Tastatur

Wenn man Programme von der Kommandozeile aufruft, ist es nicht unüblich, dabei Parameter
zu übergeben. Programmiersprachen wie Fortran, C und Python bieten die Möglichkeit,
auf diese Parameter innerhalb des Programms zuzugreifen. Die Alternative, solche Parameter
im Programmcode selbst zu definieren, hat den Nachteil, dass man zur Änderung eines
Parameters den Code verändern muss, was im Allgemeinen keine gute Idee ist, unter anderem
weil man dabei vielleicht andere unbeabsichtigte Änderungen am Programm vornehmen könnte.

Wir demonstrieren das Vorgehen mit einem kleinen Beispielprogramme namens
`beispiel_1.py`, das einen vom Benutzer vorgegebenen Text mehrfach ausgeben kann. Das
erste Argument beim Aufruf soll der Text sein, das zweite Argument gibt dann die
Zahl der Wiederholungen an.
```{code-block}
---
linenos: true
---
# beispiel_1.py
import sys

print(sys.argv)
str = sys.argv[1]
nmax = int(sys.argv[2])
for n in range(nmax):
    print(str)
```
Wir verwenden hier das `argv`-Attribute aus dem `sys`-Modul der Python-Standardbibliothek.
Hierbei steht `argv` für *argument vector*. In Zeile 4 geben wir dieses Attribut zunächst
aus, um zu sehen, was es alles enthält. Anschließend bestimmen wir aus zwei Einträgen in
diesem Attribut in den Zeilen 5 und 6 den auszugebenden Text und die Zahl der Wiederholungen.

Führen wir das Programm `beispiel_1.py` mit den Parametern `hallo` und `3` aus, so erhalten wir die
folgende Ausgabe.
```{code-block}
---
linenos: true
---
$ python beispiel_1.py Hallo 3
['beispiel_1.py', 'Hallo', '3']
Hallo
Hallo
Hallo
```
Zeile 1 gibt nach dem $-Prompt nochmals die Eingabe an, und dann folgt in den Zeilen 2 bis 5
die erzeugte Ausgabe. In Zeile 2 sehen wir, dass `sys.argv` eine Liste enthält, deren erster
Eintrag dem Namen des Python-Skripts entspricht, dem sich in den folgenden Einträgen die
angegebenen Parameter anschließen. Wie wir sehen, sind die alle Einträge Zeichenketten. Damit
erklärt sich, warum wir in Zeile 6 unseres Beispielskripts eine Umwandlung in einen Integer
vornehmen mussten. Die obigen Zeilen 3 bis 5 enthalten dann die erwartete Ausgabe, nämlich
dreimal den Text `Hallo`.

```{admonition} Weiterführender Hinweis
Es kann vorkommen, dass die Zahl der Parameter deutlich größer ist als in unserem kleinen Beispiel
und dass für eine Reihe von Parametern Defaultwerte definiert sind. Man wird dann meistens nur
eine reduzierte Zahl von Parametern angeben, die entsprechend gekennzeichnet werden müssen, um
eine eindeutige Zuordnung zu erlauben. Diese Situation ähnelt dem was wir im {numref}`kwargs`
für Funktionsaufrufe mit Schlüsselworten und Defaultwerten kennengelernt hatten. In solchen
Fällen ist es ratsam, sich das [`argparse`-Modul](https://docs.python.org/3/library/argparse.html)
der Python-Standardbibliothek anzusehen. Da dieses Modul relativ komplexe Möglichkeiten bietet, steht
auch ein spezielles [Tutorial](https://docs.python.org/3/howto/argparse.html) zur Verfügung.
```

Alternativ zur Angabe von Parametern beim Programmaufruf kann man die Parameter auch durch
das Programm abrufen lassen. Hierzu dient die {func}`input`-Funktion, die wir bereits in
{numref}`vorschau` kennengelernt haben. Auch hier ist wieder zu beachten, dass die Eingaben
im Programm als Zeichenketten vorliegen und je nach Bedarf umgewandelt werden müssen.

```{admonition} Warnhinweis
:class: warning
Man kann die über die {func}`input`-Funktion erhaltene Eingabe mit Hilfe der {func}`eval`-Funktion
auch als Python-Ausdruck auswerten lassen. Was auf den ersten Blick vielleicht vor allem
interessante Möglichkeiten verspricht, kann unter Umständen ein Sicherheitsrisiko sein.
Die unbesehene Ausführung von Code kann potentiell erheblichen Schaden anrichten, da es
aus einem Python-Programm heraus durchaus möglich ist, zum Beispiel Dateien zu löschen.
```

Sehen wir uns an, wie die {func}`input`-Funktion für eine alternative Implementierung unseres
Beispielprogramms genutzt werden kann.
```{code-block}
---
linenos: true
---
# beispiel_2.py
str = input('auszugebender Text: ')
nmax = int(input('Anzahl der Wiederholungen: '))
for n in range(nmax):
    print(str)
```
Nach dem Aufruf des Programms werden nun die Parameter abgefragt, wobei die Anzahl der
Wiederholungen wiederum in einen Integer umgewandelt werden muss. Anschließend erfolgt
die mehrfache Ausgabe des eingegebenen Textes.
```{code-block}
$ python beispiel_2.py
auszugebender Text: Hallo
Anzahl der Wiederholungen: 3
Hallo
Hallo
Hallo
```
Wir haben uns hier darauf beschränkt, das grundsätzliche Vorgehen zu demonstrieren. In der
Praxis wäre es natürlich in beiden Beispielen sinnvoll, Fehler abzufangen, zum Beispiel
für den Fall, dass sich die eingegebene Anzahl der Wiederholungen nicht in einen Integer
umwandeln lässt.

```{admonition} Weiterführender Hinweis
Möchte man Parameter nicht auf der Kommandozeile oder allgemein in einem Terminalfenster
eingeben, sondern über eine graphische Benutzeroberfläche, so kann man sich in Python
Unterstützung in der Standardbibliothek in Form des
[`tkinter`-Moduls](https://docs.python.org/3/library/tkinter.html) holen.
```

Nachdem wir uns bis jetzt auf die Eingabe konzentriert haben, wollen wir uns abschließend
noch kurz der Ausgabe mit Hilfe der {func}`print`-Funktion zuwenden. Diese Funktion 
haben wir schon bei verschiedensten Gelegenheiten verwendet. Im {numref}`formatierung`
hatten wir unter anderem auch gesehen, dass der standardmäßige Zeilenumbruch am Ende
der Ausgabe, durch den Parameter `end` durch eine andere Ausgabe ersetzt werden kann.

Wir wollen die print-Funktion nun nutzen, um einen allgemeinen Aspekt der
Ausgabe von Daten zu besprechen, der in der Praxis gelegentlich wichtig sein
kann.  Ein- und Ausgabeoperationen sind typischerweise sehr langsam im
Vergleich zu Rechenoperationen im Prozessor. Jede einzelne Ein- oder
Ausgabeoperation sofort auszuführen, würde daher die Abarbeitung des Programms
unnötig verzögern. Besser ist es zum Beispiel bei der Ausgabe von Daten, eine
gewisse Datenmenge in einem Puffer anzusammeln und dann den gesamten Datenblock
auszugeben. Praktisch bedeutet dies, dass man sich nicht darauf verlassen kann,
dass die von einer `print`-Anweisung angestoßene Ausgabeoperation sofort
vollständig ausgeführt wird. Für die `print`-Anweisung kann man eine sofortige
Ausführung jedoch erzwingen, indem man das Argument `flush` auf `True` setzt.

Da wir es hier mit zeitlichen Abläufen zu tun haben, illustrieren wir die Auswirkung
des Pufferns in einem Film. Wir verwenden dazu die `print`-Anweisung, aber
die Pufferung von Daten wird auch im nächsten Abschnitt noch einmal eine Rolle
spielen, wenn wir die Ausgabe von Daten in eine Datei besprechen.

<video width="640" height="360" controls>
  <source src="https://gertingold.github.io/resources/flush.webm" type="video/webm">
Ihr Browser unterstützt nicht das video-Tag.
</video> 

(readfile)=
## Lesen von Dateien

Für einfache wissenschaftliche Problemstellungen mag es ausreichen, Parameter über
die Kommandozeile oder auf Anfrage des Programms einzugeben und die resultierenden
Daten am Bildschirm anzusehen. Oft wird es aber so sein, dass dieses Vorgehen aufgrund
des Umfangs der Daten nicht mehr sinnvoll ist. So kann es bereits zu umständlich
sein, zehn oder zwanzig Parameter immer wieder per Hand einzugeben und in manchen
Fällen kann die Zahl der Eingabeparameter deutlich größer sein. Man denke zum Beispiel
an Strukturdaten für quantenchemische Rechnungen. Die erzeugten Daten sind häufig sehr
umfangreich, so dass man sie für eine weitere Analyse abspeichern möchte. Dies gilt
besonders dann, wenn die Erzeugung der Daten sehr zeitaufwändig ist.

Wir wollen uns zunächst dem Lesen von Daten aus Dateien zuwenden. Das grundsätzliche
Vorgehen ähnelt dem beim Lesen eines Buches. So wie man das Buch zum Lesen aufschlagen
muss, muss man eine Datei zum Lesen zunächst öffnen. Anschließend kann man im Buch lesen,
wobei wir uns hier auf die Situation beschränken wollen, in der beginnend am Anfang
gelesen wird. Wie in einem Buch ist es zwar im Prinzip auch in einer Datei möglich, direkt
zu einer bestimmten Stelle zu springen, aber dies kommt in der Praxis vor allem im
Zusammenhang mit binären Dateien vor. Hier wollen wir uns dagegen auf Textdateien
beschränken, wobei Text nicht ausschließt, dass die Datei ausschließlich oder zum
Teil numerische Information enthält.

Genauso wie man ein Buch, nachdem man Teile oder den gesamten Inhalt gelesen hat, wieder
zuschlägt, sollte man auch eine Datei schließen. Im Prinzip wird dies von modernen
Betriebssystemen notfalls erledigt, aber es ist keine gute Praxis darauf zu hoffen,
dass jemand anderes für einen die Aufräumarbeit erledigt. Problematisch würde dies vor
allem, wenn man viele Bücher gleichzeitig aufschlägt oder viele Dateien gleichzeitig
öffnet.

````{margin}
```{seealso}
[Wikipedia-Eintrag zu Foobar](https://en.wikipedia.org/wiki/Foobar).
```
````

Um eine Datei lesen zu können, muss diese Datei zunächst einmal existieren. Wir gehen
im Folgenden davon aus, dass es eine Datei mit dem Namen `foo.dat` im aktuellen Verzeichnis
gibt. Den Inhalt dieser Datei lassen wir uns hier mit einem sogenannten magischen Befehl
von Jupyter ausgeben.
```{code-cell} python
%cat foo.dat
```
Dann können wir diese Datei zum Lesen öffnen. Dabei erhalten wir ein Dateiobjekt zurück,
mit dem wir anschließend auf den Inhalt der Datei zugreifen können.
```{code-cell} python
datei = open('foo.dat')
print(datei)
```
Die `print`-Anweisung gibt hier nicht den Inhalt der Datei aus, die ja noch überhaupt nicht
gelesen wurde, sondern Information über das Dateiobjekt, das durch die Variable `datei`
repräsentiert wird. Wie wir sehen, erlaubt uns das Dateiobjekt tatsächlich Zugriff auf
unsere Datei `foo.dat`.

Der Zugriffsmodus ist `r`, was als Abkürzung für *read* andeutet, dass die
Datei zum Lesen geöffnet ist. Später werden wir noch andere Werte für den
Zugriffsmodus kennenlernen. Möchte man an dieser Stelle betonen, dass die Datei
nur zum Lesen geöffnet werden soll, kann man dies mit Hilfe des `mode`-Arguments
in der `open`-Anweisung tun. Da der Default aber der Lesezugriff ist, ist dies
nicht unbedingt erforderlich.

Schließlich ist noch die Textkodierung festgelegt. Standardmäßig wird die vom
Betriebssystem bevorzugte Kodierung verwendet, die in unserem Fall die
UTF-8-Kodierung ist, wie es heutzutage auf den meisten Systemen der Fall sein
dürfte. Sollte der zu lesende Text in einer anderen Kodierung vorliegen, so muss
man das `encoding`-Argument in der `open`-Anweisung entsprechend setzen.

Der Versuch, eine Datei zum Lesen zu öffnen, die überhaupt nicht existiert, führt
zu einem `FileNotFoundError`.
```{code-cell} python
---
tags: [raises-exception]
---
open('nonexistent.dat')
```

Wir wollen nun aber das bereits zuvor erzeugte Dateiobjekt `datei` nutzen, um
die Datei `foo.dat` zu lesen. Angesichts des in modernen Rechnern zur Verfügung
stehenden großen Hauptspeichers ist es in den meisten Fällen möglich, den
Inhalt der gesamten Datei in diesen Speicher zu laden. Dies lässt sich in
Python auf zwei Arten bewerkstelligen. Zunächst verwenden wir die `read`-Methode
des Dateiobjekts.
```{code-cell} python
inhalt = datei.read()
inhalt
```
Wie wir sehen, wird der gesamte Inhalt in eine Zeichenkette geladen, wobei
die Zeilenumbrüche jeweils an dem Steuerzeichen `\n` erkennbar sind. Um diese
Steuerzeichen deutlich zu machen, haben wir hier nicht die {func}`print`-Funktion
zu Ausgabe verwendet.

Eine bequeme Methode, um diese Zeichenkette in einzelnen Zeilen zu zerlegen
stellt die {func}`splitlines`-Methode bereit.
```{code-cell} python
print(inhalt.splitlines())
```
Wir erhalten damit eine Liste, die die einzelnen Zeilen als Einträge enthält.

Was passiert nun, wenn wir versuchen, die Datei ein zweites Mal zu lesen?
```{code-cell} python
datei.read()
```
Das Ergebnis ist nun eine leere Zeichenkette. Wie lässt es sich erklären, dass
wir nicht unser voriges Ergebnis reproduzieren können? Man kann sich den Leseprozess
am besten veranschaulichen, wenn man sich das Lesen der Datei von einem 
historischen Datenspeicher, einem Magnetband, vorstellt. Dort bewegt sich
ein Lesekopf entlang des Magnetbandes. Ganz entsprechend gibt es auch heute
noch einen Zeiger, der auf die aktuelle Position in der Datei verweist. Zu
Beginn des Leseprozesses steht dieser Zeiger am Beginn der Datei und nach dem
Lesen an deren Ende. Versucht man dann weiterzulesen, so erhält man keine Daten
mehr. Im Prinzip kann man den Zeiger zwar beliebig in der Datei neu positionieren,
aber diese Möglichkeiten werden bei Textdateien eigentlich nicht benötigt, da
wir ja die gesamte Datei bereits eingelesen haben und damit arbeiten können.

Da wir noch weitere Möglichkeiten demonstrieren wollen, Daten einzulesen, schließen
wir zunächst die Datei wieder um sie dann erneut zu öffnen.
```{code-cell} python
datei.close()
print(datei.closed)
```
Mit der ersten Zeile schließen wir die Datei. In der zweiten Zeile haben wir
dann zur Illustration abgeprüft, ob die Datei wirklich geschlossen ist.

Vor allem bei größeren Dateien möchte man vielleicht nicht die gesamte Datei
auf einmal laden, sondern diese zeilenweise lesen und verarbeiten. Iteriert
man in einer `for`-Schleife über das Dateiobjekt, so erhält man die einzelnen
Zeilen.
```{code-cell} python
datei = open('foo.dat')
for zeile in datei:
    print(zeile)
datei.close()
```
An den ausgegebenen Leerzeilen erkennen wir, dass das Zeilenumbruchzeichen
am Ende der Zeile nicht entfernt wurde.

Um das Schließen der Datei unter allen Umständen, also selbst im Fehlerfall,
sicherzustellen, bedient man sich in Python normalerweise eines Kontext-Managers.
Das vorige Beispiel lässt sich dann folgendermaßen formulieren.
```{code-cell} python
with open('foo.dat') as datei:
    for zeile in datei:
        print(zeile)
```
Wir erkennen die gewohnte Struktur mit einem Schlüsselwort, das hier `with` lautet,
und einem Doppelpunkt am Ende der Zeile. Der darauf folgende eingerückte Block
läuft unter Kontrolle des Kontext-Managers, und es ist sichergestellt, dass am
Ende des Blocks die Datei geschlossen wird. Neu ist in der erste Zeile die
Konstruktion, die das Ergebnis der `open`-Anweisung mit Hilfe des Schlüsselworts
`as` der Variablen `datei` zuweist.

In unserem konkreten Beispiel möchte man sicherlich auf die einzelnen Gleitkommawerte
separat zugreifen, so dass man in der Praxis zunächst einmal die {func}`split`-Methode
auf jede Zeile anwendet. Dies funktioniert hier ohne Angabe eines Arguments, da
die Trennung dann an *white space*, also insbesondere Leerzeichen oder Tabulatorzeichen
erfolgt. Zudem werden solche Zeichen vollständig entfernt, und das schließt auch
das Steuerzeichen für den Zeilenumbruch mit ein.
```{code-cell} python
with open('foo.dat') as datei:
    for zeile in datei:
        print(zeile.split())
```
Allerdings zeigt das Ergebnis, dass beim Einlesen zunächst einmal ausschließlich
Zeichenketten vorliegen. Es ist hier also noch erforderlich, die einzelnen
Zeilenbestandteile in den richtigen Datentyp umzuwandeln, hier also in Gleitkommazahlen.
Natürlich könnte man dazu über jede einzelne Liste iterieren und nach der Umwandlung
mit der {func}`float`-Funktion neue Listen aufbauen. In Python lässt sich das leichter
und übersichtlicher mit der {func}`map`-Funktion erledigen, wobei die folgende 
`for`-Schleife lediglich zur Ausgabe dient.
```{code-cell} python
data = map(float, ['1.37', '2.59'])
for d in data:
    print(d, type(d))
```

Im Prinzip könnte man ähnlich vorgehen, wenn die einzelnen Einträge in einer
Zeile durch Kommas oder Semikolons getrennt sind. Solche Dateien begegnen einem
in der Praxis häufig, wenn Daten mit Excel erfasst wurden und dann im
CSV-Format abgespeichert wurden, wobei die Abkürzung CSV für *comma separated
values* steht. Anstatt das Einlesen selbst zu programmieren, bietet es sich
dann an, auf Funktionen aus der Python-Standardbibliothek zurückzugreifen, in
diesem Fall konkret auf das
[`csv`-Modul](https://docs.python.org/3/library/csv.html). Eine
Programmbibliothek, die diverse Eingabeformate einlesen kann und für das
Verarbeiten von strukturierten Daten in Python besonders gut geeignet ist, ist
[Pandas](https://pandas.pydata.org/).

```{admonition} Weiterführender Hinweis
Große Mengen strukturierter Daten werden heute häufig im HDF5-Format gespeichert.
Dieses kann von [Pandas](https://pandas.pydata.org/) gelesen werden. Wenn man
Pandas jedoch nicht zur Weiterverarbeitung der Daten verwenden möchte, ist es
sinnvoll, sich das [`h5py`-Paket](https://www.h5py.org/) anzusehen.

Anstatt Parameter wie in {numref}`commandline` beschrieben an ein Programm zu
übergeben, werden auch Konfigurationsdateien verwendet, wie man sie als `INI`-Dateien
in Windows kennt. Zum Lesen solcher Dateien stellt die Python-Standardbibliothek
das [`configparser`-Modul](https://docs.python.org/3/library/configparser.html)
zur Verfügung.

Beliebte Formate für den Datenaustausch sind unter anderem XML (*eXtensible
Markup Language*) und JSON (*JavaScript Object Notation*). Auch diese
unterstützt Python in der Standardbibliothek mit einer Reihe von [XML
verarbeitenden Modulen](https://docs.python.org/3/library/xml.html)
beziehungsweise dem
[`json`-Modul](https://docs.python.org/3/library/json.html).

Die genannten Pakete unterstützen nicht nur das Lesen der genannten Dateitypen,
sondern auch das Schreiben.
```

## Schreiben von Dateien

Genauso wie für das Lesen aus Dateien muss man zum Schreiben in eine
Datei diese zunächst öffnen. Hat man das Schreiben beendet, so sollte
die Datei wieder geschlossen werden. In Python macht man dies am Einfachsten
im Rahmen eines `with`-Kontexts, wie wir ihn schon beim Lesen aus Dateien
kennengelernt haben.

Im {numref}`readfile` hatten wir gesehen, dass eine Datei defaultmäßig
im Modus `r`, also zum Lesen, geöffnet wird. In diesem Modus ist es nicht
möglich, in die geöffnete Datei zu schreiben. Statt der {func}`read`-Methode zum
Lesen müssen wir hier die {func}`write`-Methode zum Schreiben verwenden, um das
Verhalten zu demonstrieren.
```{code-cell} python
---
tags: [raises-exception]
---
with open('foo.txt') as datei:
    datei.write('Dies ist ein Test.')
```
Wenn wir dagegen die Datei im Schreibmodus `w` öffnen, können wir die
Datei wie gewünscht schreiben.
```{code-cell} python
with open('foo.txt', mode='w') as datei:
    datei.write('Dies ist ein Test.')
```
Das Ergebnis können wir uns wie in {numref}`readfile` mit dem magischen
Befehl `%cat` in einer Notebook-Zelle ansehen.
```{code-cell} python
%cat foo.txt
```

Im Zusammenhang mit der {func}`write`-Methode ist allerdings zu beachten, dass
diese im Gegensatz zur {func}`print`-Funktion nicht automatisch einen
Zeilenumbruch anhängt. Im folgenden Beispiel verzichten wir darauf, beim
zweiten Argument das Schlüsselwort `mode` anzugeben, da dieses Argument
an der richtigen Position steht. Es spricht aber natürlich nichts dagegen,
das Schlüsselwort zur Verdeutlichung anzugeben.
```{code-cell} python
with open('foo.txt', 'w') as datei:
    for n in range(1, 4):
        datei.write(f'Zeile {n}')
```
```{code-cell} python
%cat foo.txt
```
Dieses Verhalten entspricht dem, was wir von der {func}`print`-Funktion kennen,
wenn wir `end=''` setzen. Wollen wir einen Zeilenumbruch erreichen, so müssen
wir das entsprechende Steuerzeichen explizit angeben.
```{code-cell} python
with open('foo.txt', 'w') as datei:
    for n in range(1, 4):
        datei.write(f'Zeile {n}\n')
```
```{code-cell} python
%cat foo.txt
```
Die Möglichkeiten der Formatierung in f-Strings hatten wir in einigem
Detail in {numref}`formatierung` besprochen, auf das wir an dieser Stelle
verweisen wollen.

Benutzt man den Modus `w` zum Öffnen einer Datei zum Schreiben, muss man sich
bewusst sein, dass eine eventuell bereits existierende Datei mit diesem Namen
zunächst gelöscht wird. Dies gilt zumindest, wenn man auf der Ebene des
Betriebssystems die Rechte dazu besitzt. Je nach Situation kann dies das
erwünschte Verhalten sein oder es stört einen zumindest nicht. Es gibt jedoch
Anwendungen, in denen man einen alternativen Modus verwenden wird.

Statt des Modus `w` kann man den Modus `x` verwenden, der die Datei nur dann
zum Schreiben öffnen wird, wenn eine Datei mit dem betreffenden Namen noch
nicht existiert. Dies können wir anhand der Datei `foo.txt` demonstrieren,
die wir ja gerade geschrieben hatten.
```{code-cell} python
---
tags: [raises-exception]
---
with open('foo.txt', 'x') as datei:
    for n in range(1, 4):
        datei.write(f'Zeile {n}\n')
```
Der Versuch, in eine existierende Datei zu schreiben, wird also beim Modus
`x` unterbunden.

Es kann aber auch vorkommen, dass man in einer bereits existierenden Datei
am Ende der Datei weiterschreiben möchte. Hierzu ist der Modus `a` für *append*
vorgesehen. Ein Anwendungsfall kann darin bestehen, Probleme durch das Puffern
der Ausgabe, die wir am Ende von {numref}`commandline` besprochen hatten, zu
umgehen. So könnte man bei einem Programm mit langer Laufzeit, bei dem in
größeren Abständen Daten geschrieben werden, die Datei nur unmittelbar zum
Schreiben der Daten wieder öffnen und anschließend wieder schließen. Bei einem
Programmabbruch gehen damit die bereits ausgegebenen Daten nicht verloren.
Dieses Vorgehen ist allerdings nur dann sinnvoll, wenn die Zeiten zwischen
den Schreibvorgängen nicht zu kurz sind, da sonst der Aufwand für das Öffnen
und Schließen der Datei das Programm ausbremsen würde.

Im folgenden Beispiel demonstrieren wir mit Hilfe einer Schleife außerhalb des
`with`-Kontexts das wiederholte Anhängen an eine Datei. Zudem überprüfen wir,
dass die Datei jeweils wieder geschlossen wurde.
```{code-cell} python
from datetime import datetime
from time import sleep

for n in range(1, 5):
    sleep(5)
    now = datetime.now()
    with open('spam.dat', 'a') as datei:
        msg = f'{now:%H:%M:%S} - Durchlauf {n}\n'
        datei.write(msg)
    if datei.closed:
        msg = f'{now:%H:%M:%S} - Datei geschlossen'
        print(msg)
```
```{code-cell} python
%cat spam.dat
```

Möchte man mehrere Dateien schreiben, weil man beispielsweise Rechnungen für
mehrere Parametersätze durchführen möchte, sollte man im Hinterkopf behalten,
dass es sich bei dem Namen, der beim Öffnen der Datei angegeben werden muss, 
einfach um eine Zeichenkette handelt, die entsprechend konstruiert werden 
kann. So hat man die Möglichkeit, entweder Parameter im Dateinamen unterzubringen
oder die Dateien durchzunummerieren. Wir wollen letzteres an einem Beispiel
demonstrieren.
```{code-cell} python
for n in range(1, 16):
    with open(f'mydata_{n:04}.dat', 'w') as datei:
        datei.write(f'Datei Nr. {n}\n')
```
```{code-cell}
%ls mydata*.dat
```
Um eine übersichtliche Sortierung der Dateien zu erzeugen, ist es sinnvoll,
für die Nummer der Datei ein hinreichend breites Feld vorzusehen und die
freien Stellen mit Nullen zu füllen.

Ganz unabhängig davon, wie man den Dateinamen wählt, ist es sinnvoll,
Informationen, die erforderlich sind um die Daten zu erzeugen, zu Beginn der
Datei abzuspeichern. Dazu gehören nicht nur die verwendeten Parameter, sondern
auch Information über die verwendete Programmversion. Damit lässt sich im Fall
eines Fehlers im Programm auch im Nachhinein entscheiden, ob die Daten hiervon
betroffen sind.
