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

## Lesen und Schreiben von Dateien
