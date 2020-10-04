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

(vorschau)=
# Eine Vorschau

In diesem Kapitel wollen wir anhand eines konkreten Beispiels eine Vorstellung
von einigen Aspekten bekommen, die beim Programmieren eine Rolle spielen. Wir
werden diese Aspekte und noch einige mehr in den folgenden Kapiteln genauer
besprechen. Es geht hier also nicht darum, schon alles im Detail zu verstehen,
sondern vielmehr einen ersten Eindruck von der Struktur eines Programms zu
gewinnen.

Unser Beispiel implementiert das Spiel [»Schere, Stein,
Papier«](https://de.wikipedia.org/wiki/Schere,_Stein,_Papier), wobei der
Benutzer gegen den Computer spielt. Bei der folgenden Realisierung spielen
[psychologische Aspekte des
Spiels](https://de.wikipedia.org/wiki/Schere,_Stein,_Papier#Logik_und_Psychologie_des_Spiels)
keine Rolle. Bevor wir das Programm ausführen und dann anschließend einen
genaueren Blick auf den Code werfen, wollen wir kurz an die Spielregeln erinnern.
Spieler und Computer wählen eines der drei Objekte Schere, Stein oder Papier.
Die Schere schneidet das Papier, das Papier wickelt den Stein ein und der Stein
macht die Schere stumpf. Daher gewinnt die Schere gegen dem Papier, das Papier gegen
den Stein und der Stein wiederum gegen die Schere.

````{margin}
```{admonition} Tipp
:class: tip
Durch Klicken auf das Blattsymbol rechts oben im Codefeld kann man
leicht den gesamten Code in eine Datei kopieren.
```
````

```{code-block} python
---
linenos: true
---
import random

def get_result(n_self, n_other):
    result = (n_self - n_other) % 3
    if result == 0:
        return 'Das Spiel endete unentschieden.'
    elif result == 1:
        return 'Du hast gewonnen.'
    return 'Du hast leider verloren.'

objekte = ['Stein', 'Papier', 'Schere']
info_text = ('\n[0] Stein\n'
             '[1] Papier\n'
             '[2] Schere\n\n'
             'Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: ')

while True:
    n_benutzer = int(input(info_text))
    if 0 <= n_benutzer <= 2:
        n_computer = random.randrange(3)
        print('-'*40)
        print(f'Benutzer: {objekte[n_benutzer]}')
        print(f'Computer: {objekte[n_computer]}')
        print(get_result(n_benutzer, n_computer))
        print('-'*40)
    elif n_benutzer == -1:
        break
    else:
        print('\n*** ungültige Eingabe\n')
```

Bevor wir uns mit dem Programmcode beschäftigen, sehen wir uns zunächst eine
Beispiellauf an. Das Programm sei in einer Datei `schere_stein_papier.py`
abgespeichert, die jetzt unter der Kontrolle des Python-Interpreters ausgeführt
wird. Nach einem Informationstext kann der Benutzer durch Eingabe einer Zahl
zwischen 0 und 2 ein Objekt auswählen. Anschließend wählt der Computer ein
Objekt und gibt das Spielergebnis aus. Danach sind weitere Spielrunden möglich
bis der Benutzer die Zahl -1 eingibt.

```
$ python schere_stein_papier.py

[0] Stein
[1] Papier
[2] Schere

Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: 2
----------------------------------------
Benutzer: Schere
Computer: Papier
Du hast gewonnen.
----------------------------------------

[0] Stein
[1] Papier
[2] Schere

Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: 2
----------------------------------------
Benutzer: Schere
Computer: Schere
Das Spiel endete unentschieden.
----------------------------------------

[0] Stein
[1] Papier
[2] Schere

Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: -1
$
```

Schon ohne den Programmcode genau anzusehen, macht die Ausführung des Programms
deutlich, dass es möglich sein sollte, Daten einzugeben und die Resultate
wieder auszugeben. Vor allem ohne Letzteres wird man kaum auskommen, da das
Programm in irgendeiner Form eine Auswirkung haben sollte. Allerdings wird die
Eingabe häufig nicht über die Tastatur und die Ausgabe über den Bildschirm
erfolgen. Gerade umfangreichere Eingaben erfolgen durch das Einlesen einer oder
auch mehrerer Dateien, die beispielsweise experimentelle Daten enthalten. Auch
die Ausgabe wird häufig in Dateien erfolgen, zum Beispiel um die Daten für weitere
Schritte wie eine graphische Aufbereitung zur Verfügung zu haben.

Sehen wir uns an, wo in unserem Beispielprogramm die Ein- und Ausgabe erfolgt.
Die relevanten Zeilen sind farblich hervorgehoben.

```{code-block} python
---
linenos: true
emphasize-lines: 18,21-25,29
---
import random

def get_result(n_self, n_other):
    result = (n_self - n_other) % 3
    if result == 0:
        return 'Das Spiel endete unentschieden.'
    elif result == 1:
        return 'Du hast gewonnen.'
    return 'Du hast leider verloren.'

objekte = ['Stein', 'Papier', 'Schere']
info_text = ('\n[0] Stein\n'
             '[1] Papier\n'
             '[2] Schere\n\n'
             'Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: ')

while True:
    n_benutzer = int(input(info_text))
    if 0 <= n_benutzer <= 2:
        n_computer = random.randrange(3)
        print('-'*40)
        print(f'Benutzer: {objekte[n_benutzer]}')
        print(f'Computer: {objekte[n_computer]}')
        print(get_result(n_benutzer, n_computer))
        print('-'*40)
    elif n_benutzer == -1:
        break
    else:
        print('\n*** ungültige Eingabe\n')
```

Die {func}`input`-Funktion erlaubt das Einlesen von Information von der Tastatur.
Hinter dem Befehl steht hier in Klammern ein Argument, wie wir das von mathematischen
Funktion kennen. Dieses Argument, das hier `info_text` genannt wurde, enthält den Text,
der als Eingabeaufforderung ausgegeben wird. Nach einer Umwandlung der Texteingabe
in eine ganze Zahl wird die Eingabe hier der Variablen `n_benutzer` zugewiesen.

In den Zeilen 21 bis 25 und 29 sehen wir Aufrufe der {func}`print`-Funktion, die für
die Ausgabe von Information verantwortlich sind. Wie man die genaue Formatierung der
Ausgabe steuern kann, werden wir in einem späteren Kapitel sehen.

Weiter fällt bei der Ausführung des Programms auf, dass sich das Spiel wiederholen
lässt, im Prinzip beliebig oft bis der Benutzer -1 eingibt. Die Ausführung von
so genannten Schleifen ist in Programmen sehr häufig anzutreffen. Dabei kann die
Zahl der Schleifendurchläufe vorgegeben sein, wie es in Python bei einer `for`-Schleife
der Fall ist oder von einer Bedingung abhängen, wie in Python durch eine `while`-Schleife
realisiert.

In unserem Programm ist ab der Zeile 17 eine `while`-Schleife implementiert, die
eine etwas ungewöhnliche Form annimmt. Nach dem `while`-Befehl steht immer eine
Bedingung, die je nachdem ob sie erfüllt ist oder nicht, über die Fortsetzung der
Schleifendurchläufe entscheidet. Hier sorgt der Wahrheitswert `True` immer dafür,
dass die Bedingung erfüllt ist. Die Schleife wird also im Prinzip unendlich oft
durchlaufen. Allerdings haben wir in den Zeilen 26 und 27 eine Vorkehrung getroffen,
dass die Schleifendurchläufe bei einer Eingabe von -1 abgebrochen wird.

```{code-block} python
---
linenos: true
lineno-start: 17
---
while True:
    n_benutzer = int(input(info_text))
    if 0 <= n_benutzer <= 2:
        n_computer = random.randrange(3)
        print('-'*40)
        print(f'Benutzer: {objekte[n_benutzer]}')
        print(f'Computer: {objekte[n_computer]}')
        print(get_result(n_benutzer, n_computer))
        print('-'*40)
    elif n_benutzer == -1:
        break
    else:
        print('\n*** ungültige Eingabe\n')
```

Soeben sind wir einem weiteren typischen Programmierkonstrukt begegnet, nämlich
einer Verzweigung. Auch hier passiert wieder etwas in Abhängigkeit davon, ob 
eine Bedingung erfüllt ist. Allerdings geht es nicht um die Wiederholung eines
bestimmten Codes, sondern darum, welcher Code ausgeführt wird. Um die Struktur
dieser Konstruktion zu verstehen, sehen wir uns die im Folgenden markierten
Zeilen genauer an.

```{code-block} python
---
linenos: true
lineno-start: 17
emphasize-lines: 3, 10, 12
---
while True:
    n_benutzer = int(input(info_text))
    if 0 <= n_benutzer <= 2:
        n_computer = random.randrange(3)
        print('-'*40)
        print(f'Benutzer: {objekte[n_benutzer]}')
        print(f'Computer: {objekte[n_computer]}')
        print(get_result(n_benutzer, n_computer))
        print('-'*40)
    elif n_benutzer == -1:
        break
    else:
        print('\n*** ungültige Eingabe\n')
```

In Zeile 19 wird überprüft, ob die Eingabe durch den Benutzer im vorgegebenen
Intervall, also zwischen 0 und 2 liegt. In diesem Fall wird eine Spielrunde
durchgeführt, die durch die Einrückung verdeutlicht ist. Während andere
Programmiersprachen zur Begrenzung eines solchen Blocks häufig Klammern
verwenden, erwartet Python eine Einrückung. 

Liegt die Eingabe nicht im Intervall zwischen 0 und 2, so müssen wir noch den
Fall der Eingabe -1 überprüfen. `elif` in Zeile 26 steht als Abkürzung für
`else if`.  Falls also die Eingabe nicht zwischen 0 und 2 liegt, aber gleich -1
ist, so wird die `while`-Schleife in Zeile 27 abgebrochen. 

Ist keine der beiden vorgehenenden Fälle erfüllt, wird der `else`-Block ab
Zeile 28 relevant, der in unserem in einer Ausgabe darauf hinweist, dass keine
gültige Eingabe gemacht wurde.

Eine entsprechende Verzweigungsstrukturen findet man auch in den Zeilen 4 bis
9, wo auch drei Alternativen zu unterscheiden sind, nämlich gewonnen,
unentschieden und verloren. Es kann aber auch vorkommen, dass ein `if`-Block
alleine vorkommt oder nur in Kombination mit einem `else`-Block. Mehr hierzu
werden wir später noch erfahren.

Werfen wir ein genaueren Blick auf den ersten Teil des Programmcodes.

```{code-block} python
---
linenos: true
emphasize-lines: 3, 6, 8, 9, 24
---
import random

def get_result(n_self, n_other):
    result = (n_self - n_other) % 3
    if result == 0:
        return 'Das Spiel endete unentschieden.'
    elif result == 1:
        return 'Du hast gewonnen.'
    return 'Du hast leider verloren.'

objekte = ['Stein', 'Papier', 'Schere']
info_text = ('\n[0] Stein\n'
             '[1] Papier\n'
             '[2] Schere\n\n'
             'Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: ')

while True:
    n_benutzer = int(input(info_text))
    if 0 <= n_benutzer <= 2:
        n_computer = random.randrange(3)
        print('-'*40)
        print(f'Benutzer: {objekte[n_benutzer]}')
        print(f'Computer: {objekte[n_computer]}')
        print(get_result(n_benutzer, n_computer))
        print('-'*40)
    elif n_benutzer == -1:
        break
    else:
        print('\n*** ungültige Eingabe\n')
```

In den Zeilen 3 bis 9 ist eine Funkion definiert, die in Abhängigkeit der
von Benutzer und Computer gewählten Objekte entscheidet, wer das Spiel gewonnen
hat. Diese Funktion wird in Zeile 24 aufgerufen und dorthin wird mit Hilfe einer
der `return`-Anweisungen in den Zeilen 6, 8 und 10 auch das Ergebnis der Funktion
zurückgegeben. Im Prinzip könnte der Code im Funktionsblock auch direkt weiter
unten im Programm stehen. Hier wird vor durch die Definition einer Funktion vor
allem mehr Übersichtlichkeit erreicht.

Häufig kann man auch auf Funktionen zurückgreifen, die von einem anderen
Programmpaket bereitgestellt wird. In Python kann dies die sehr umfangreiche
[Standardbibliothek](https://docs.python.org/3/library/index.html) sein oder
ein anderes der unzähligen verfügbaren Programmpakete. In unserem Beispiel haben
wir zur Bestimmung der zufälligen Wahl des Objekts durch den Computer auf die
Python-Standardbibliothek zurückgegriffen. Dies ist sinnvoll, da die Berechnung
guter Zufallszahlen nicht ganz einfach ist. Daher ist es besser, auf bewährten und
gut geschriebenen Code zurückgreifen statt das Rad neu zu erfinden. In der Zeile
20 benutzen wir die {func}`randrange`-Funktion, um eines der drei Objekte zufällig
auszuwählen. Dies ist möglich, nachdem wir in Zeile 1 das {mod}`random`-Modul
importiert haben, das diese Funktion definiert.

```{code-block} python
---
linenos: true
emphasize-lines: 1, 20
---
import random

def get_result(n_self, n_other):
    result = (n_self - n_other) % 3
    if result == 0:
        return 'Das Spiel endete unentschieden.'
    elif result == 1:
        return 'Du hast gewonnen.'
    return 'Du hast leider verloren.'

objekte = ['Stein', 'Papier', 'Schere']
info_text = ('\n[0] Stein\n'
             '[1] Papier\n'
             '[2] Schere\n\n'
             'Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: ')

while True:
    n_benutzer = int(input(info_text))
    if 0 <= n_benutzer <= 2:
        n_computer = random.randrange(3)
        print('-'*40)
        print(f'Benutzer: {objekte[n_benutzer]}')
        print(f'Computer: {objekte[n_computer]}')
        print(get_result(n_benutzer, n_computer))
        print('-'*40)
    elif n_benutzer == -1:
        break
    else:
        print('\n*** ungültige Eingabe\n')
```

Bereits in diese relativ kurzen Programm haben wir viele Aspekte einer
Programmiersprache verwendet, die wir im Folgenden genauer besprechen werden.
Dadurch dass das Beispiel nicht aus dem naturwissenschaftlichen Bereich gewählt
war, kam allerdings ein Thema nicht zur Sprache, das uns ebenfalls noch
beschäftigen wird. In den Natur- und Ingenieurwissenschaften haben die meisten
Problemstellungen mit Zahlen zu tun, so dass sich Fragen stellen wie zum Beispiel
wie groß der Bereich der Zahlen ist, die in einem Computer verarbeitet werden 
kann, oder ob die gewählte Programmiersprache komplexe Zahlen zulässt. Auch
Vektoren oder Matrizen könnten von Interesse sein. In unserem Beispiel sieht man
in Zeile 11 ein Objekt, das an einen Vektor erinnert.

```{code-block} python
---
linenos: true
lineno-start: 11
emphasize-lines: 1, 1
---
objekte = ['Stein', 'Papier', 'Schere']
info_text = ('\n[0] Stein\n'
             '[1] Papier\n'
             '[2] Schere\n\n'
             'Gib eine Zahl zwischen 0 und 2 ein oder -1 zum Beenden: ')
```

Hierbei handelt es sich um eine Liste und es ist im Prinzip auch möglich,
Listen von Zahlen zu verwenden. Allerdings sind Listen nicht geeignet, um
Vektoren darzustellen und obwohl man Listen von Listen verwenden kann, eignen
sich diese nicht zur Darstellung von Matrizen. An dieser Stelle greift man
lieber auf das bereits in der {ref}`einleitung` erwähnte NumPy-Paket zurück,
das einem beispielsweise vielfältige Anwendungsmöglichkeiten im Bereich der
linearen Algebra bietet.
