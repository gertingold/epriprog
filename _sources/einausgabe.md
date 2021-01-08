(einausgabe)=
# Ein- und Ausgabe

```{admonition} Hinweis
:class: warning
Dieses Kapitel befindet sich noch in Bearbeitung.
```

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
---
linenos: true
---
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

## Lesen und Schreiben von Dateien
