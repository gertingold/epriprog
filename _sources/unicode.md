(appendixunicode)=
# Anhang: Unicode

## Kodierung von Schriftzeichen

Auch Schriftzeichen müssen im Computer binär kodiert werden. Zwar sind schon
bei Zahlen verschiedene Codierungsarten denkbar, aber grundlegende Aspekte des
Codes ergeben sich durch die Verwendung des Dualsystems in natürlicher Weise.
Bei Schriftzeichen ist dies dagegen überhaupt nicht der Fall, schon gar nicht,
wenn man sich von der angelsächsischen Sicht löst. Schon im europäischen
Sprachraum treten Modifikationen des lateinischen Alphabets mit Akzenten und
Umlauten auf, und natürlich gibt es weltweit eine Vielzahl von Schriftsystemen,
die in Gebrauch sind oder im Gebrauch waren, so dass eine konsistente Kodierung
über alle Grenzen hinweg eine große Herausforderung darstellt.

Historisch mussten die ersten Kodierungen von Schriftzeichen zur maschinellen
Verarbeitung zudem auf die mechanische Stabilität von Lochkarten, wie die in
{numref}`fig:lochkarte` gezeigte aus den späten 70er Jahren des letzten
Jahrhunderts, Rücksicht nehmen. Entsprechend wurden im Lauf der Zeit eine
Vielzahl unterschiedlicher Kodierungen entwickelt [^haralambous], die durch
Inkompatibilitäten den Informationsaustausch erschwerten. Erst in jüngerer Zeit
setzt sich mit Unicode ein umfassender Standard weitgehend durch, der auch in
Python seit der Version 3 konsequent unterstützt wird.

```{figure} images/unicode/lochkarte.png
---
width: 80%
name: fig:lochkarte
---
Lochkarte in einer auf der Codierung des Lochkartenlochermodells 026 von IBM
basierenden Codierung von Control Data Cooperation. Die dargestellte Lochkarte
enthält eine Zeile aus einem Fortran-Programm mit dem Inhalt `˽˽˽30˽IZ(J)=IZ(J+1)`
(Quelle: Gert-Ludwig Ingold).
```

[^haralambous]: Eine ausführlichere Darstellung der Entwicklungsgeschichte von Zeichenkodierungen
    gibt Y. Haralambous, *Fonts & Encodings* (O'Reilly, 2007).

Bereits 1967 wurde der *American Standard Code for Information Interchange*
(ASCII) als Standard veröffentlicht, der heute noch eine wichtige Rolle spielt.
Auf Großrechnern waren damals aber auch andere Kodierungen in Gebrauch. Der
ASCII ist ein 7-Bit-Code und kann somit 128 Zeichen darstellen, die in
{numref}`fig:unicode0000` als Teil des Unicode-Standards gezeigt sind.  Die
grau unterlegten Akronyme stellen Steuerzeichen dar, wobei SP ein Leerzeichen
bezeichnet und damit auch zu den druckbaren Zeichen gerechnet werden kann.

Einige heute noch wichtige Steuerzeichen sind in {numref}`table:steuerzeichen`
aufgelistet. Ihnen ist ihr Ursprung in der Zeit der Fernschreiber deutlich
anzumerken. Dabei wurde die Übertragung auf Computer von verschiedenen 
Betriebssystemen nicht einheitlich gehandhabt, was sich zum Beispiel daran
zeigt, dass unterschiedliche Varianten mit LF und/oder CR in Gebrauch kamen,
um einen Zeilenumbruch anzuzeigen.

```{list-table} Ausgewählte Steuerzeichen im ASCII-Standard
:header-rows: 1
:name: table:steuerzeichen
* - Hexcode
  - Kürzel
  - Bedeutung
  - Tastenkombination
  - Escape-Sequenz
* - 08
  - BS
  - backspace
  - {kbd}`STRG-H`
  - `\b`
* - 09
  - HT
  - horizontal tabulation
  - {kbd}`STRG-I`
  - `\t`
* - 0A
  - LF
  - line feed (neue Zeile)
  - {kbd}`STRG-J`
  - `\n`
* - 0C
  - FF
  - form feed (neue Seite)
  - {kbd}`STRG-L`
  - `\f`
* - 0D
  - CR
  - carriage return (Wagenrücklauf)
  - {kbd}`STRG-M`
  - `\r`
* - 1B
  - ESC
  - escape
  - {kbd}`STRG-[`
  -  
```

Aus deutschsprachiger Sicht fällt bei der Betrachtung der ASCII-Codetabelle in
{numref}`fig:unicode0000` sofort das Fehlen von Umlauten auf. In einem ersten
Schritt liegt daher eine Erweiterung auf einen 8-Bit-Code nahe, der auch weitere
Zeichen aus dem europäischen Sprachraum aufnehmen kann. Hierfür existieren eine
ganze Reihe von Belegungen, die sich am Bedarf bestimmter Sprachen orientieren.

Von Bedeutung ist unter anderem die Normenfamilie ISO 8859. Für die deutsche
Sprache ist ISO-8859-1, auch bekannt als »Latin-1«, gebräuchlich. Die darin
vorhandenen, über ASCII hinausgehenden Zeichen sind, wenn man die Steuerzeichen
ignoriert, in {numref}`fig:unicode0080` dargestellt. Auch hier sind wieder
eine Reihe von Steuerzeichen vertreten, unter anderem ein `nonbreakable space`
(NBSP) und ein `soft hyphen` (SHY). Der zu den Zeichen gehörige Code ergibt
sich aus den letzten beiden Stellen des Unicode Codepoints, der an dem
vorangestellten ``U+`` erkenntlich ist.  Beispielsweise wird das »ä« durch
``0xEA`` kodiert. Da das Eurozeichen in ISO-8859-1 nicht enthalten ist, ist
auch die Norm ISO-8859-15 von Bedeutung, die sich an 8 Stellen von ISO-8859-1
unterscheidet.

In neuerer Zeit hat der [Unicode-Standard](http://www.unicode.org/) enorm an
Bedeutung gewonnen, da er das Ziel hat, alle weltweit gebräuchlichen Zeichen zu
kodieren. Hierzu gehören in neuerer Zeit beispielsweise auch
[Emoticons](https://www.unicode.org/charts/PDF/U1F600.pdf). Die aktuelle
[Version 15.1.0](http://www.unicode.org/versions/Unicode15.1.0/) umfasst 149.813
Zeichen und bietet noch genügend Platz für Erweiterungen. Jedes Zeichen ist
einem so genannten Codepoint zugeordnet, der Werte zwischen ``0x00`` und
``0x10FFFF`` annehmen kann. Da damit jedes Zeichen statt üblicherweise einem
Byte nun drei Byte benötigen würde, werden die Unicode-Zeichen geschickt
kodiert. Für westliche Sprachen ist die Kodierung UTF-8 besonders geeignet, da
die ASCII-Zeichen im Bereich ``0x00`` bis ``0x7F`` ihre Bedeutung beibehalten.
Wir beschränken uns daher im Folgenden auf die Erklärung dieser Kodierung.

## UTF-8-Kodierung

Im Unicode-Standard ist jedes Zeichen zunächst einmal mit einer Nummer
versehen, dem Unicode Codepoint, der in
{numref}`fig:unicode0000`‒{numref}`fig:unicode2200` blau hinterlegt ist und mit
`U+` beginnt. In dem darunter befindlichen grünen Feld ist die zugehörige
UTF-8-Kodierung angegeben. Dabei kommen in diesen Beispielen 1-, 2- und
3-Byte-Werte vor. Im Allgemeinen können sogar 4 Bytes auftreten.

Im Bereich ``0x00`` bis ``0x7f`` wird das letzte Byte des Codepoints
verwendet und auf diese Weise Übereinstimmung mit ASCII erreicht. Somit lassen
sich in einer westlichen Sprache verfasste Texte weitestgehend unabhängig von
der tatsächlichen Kodierung lesen. Außerdem wird die Mehrzahl der vorkommenden
Zeichen platzsparend kodiert. Alle Zeichen, die in mehr als einem Byte kodiert
sind, beginnen in UTF-8 mit einer `1`.

Im Bereich ``0x0080`` bis ``0x07FF`` werden zwei Bytes zur Kodierung verwendet.
Die elf relevanten Bytes aus dem Unicode-Codepoint werden dabei wie in
{numref}`fig:utf8_2byte` gezeigt auf die zwei Bytes verteilt. Man kann dieses
Übersetzungsschema natürlich auch umgekehrt anwenden, nachdem man festgestellt
hat, dass der UTF-8-Code mit `0xC` beginnt.

```{figure} images/unicode/utf8_2.png
---
height: 3cm
name: fig:utf8_2byte
---
Übersetzung des Unicodezeichens »é«in die UTF-8-Kodierung, die zwei Bytes
benötigt. Dabei wird der Codepoint ``0xE9`` nach dem gezeigten Schema auf
den UTF-8-Code ``0xC3A9`` abgebildet. 
```

```{admonition} Frage
Was würde ein Programm, das von einer Latin-1-Kodierung ausgeht, im Fall des
in {numref}`fig:utf8_2byte` gezeigten UTF-8-Codes `0xC3A9` anzeigen.
```

Beispiele von 2-Byte-Codes sind in den Codetabellen in
{numref}`fig:unicode0080` und {numref}`fig:unicode0380` zu sehen. Dabei handelt
es sich zum einen um die oberen 128 Zeichen der ISO-8859-1-Norm und zum anderen
um griechische und koptische Zeichen im Unicode-Standard.

Die in {numref}`fig:unicode2200` gezeigten mathematischen Symbole erfordern
einen 3-Byte-Code, der sich wie in {numref}`fig:unicode2200` für das Zeichen
»∞« gezeigt aus dem Unicode-Codepoint ergibt. In der UTF-8-Kodierung sind 
3-Byte-Codes daran erkennbar, dass sie mit `0xE` beginnen.

```{figure} images/unicode/utf8_3.png
---
height: 3cm
name: fig:utf8_3byte
---
Übersetzung des Unicodezeichens »∞« in die UTF-8-Kodierung, die drei Byte erfordert..
```

Aus 4 Bytes bestehende Codes ergeben sich durch entsprechende Verallgemeinerung
für Codepoints zwischen ``0x010000`` und ``0x10FFFF``, wobei der UTF-8-Code dann
mit ``0xF`` beginnt. 

## Ausgewählte Codeseiten aus dem Unicode-Standard

Die im Folgenden abgebildeten exemplarischen Codeseiten geben einen kleinen Eindruck
von der Vielfalt der vorhandenen Zeichen. Neben den im westlichen Sprachraum häufig
verbreiten Zeichen, die in {numref}`fig:unicode0000` und {numref}`fig:unicode0080` gezeigt
sind, werden als Beispiele in {numref}`fig:unicode0380` griechische und koptische Zeichen
sowie in {numref}`fig:unicode2200` mathematische Symbole gezeigt. Einen vollständigen
Überblick geben die [Unicode Character Code Charts](http://www.unicode.org/charts/).

```{figure} images/unicode/u0000.png
---
width: 80%
name: fig:unicode0000
---
Unicodezeichen im Bereich [0000‒007F](https://www.unicode.org/charts/PDF/U0000.pdf).
Der Unicode Codepoint sowie die UTF-8-Kodierung sind für jedes Zeichen blau bzw. grün
hinterlegt angegeben. Steuerzeichen sind grau hinterlegt. 
```

```{figure} images/unicode/u0080.png
---
width: 80%
name: fig:unicode0080
---
Unicodezeichen im Bereich [0080‒00FF](https://www.unicode.org/charts/PDF/U0080.pdf).
Der Unicode Codepoint sowie die UTF-8-Kodierung sind für jedes Zeichen blau bzw. grün
hinterlegt angegeben. Steuerzeichen sind grau hinterlegt. 
```

```{figure} images/unicode/u0380.png
---
width: 80%
name: fig:unicode0380
---
Unicodezeichen im Bereich [0380‒03FF](https://www.unicode.org/charts/PDF/U0370.pdf).
Der Unicode Codepoint sowie die UTF-8-Kodierung sind für jedes Zeichen blau bzw. grün
hinterlegt angegeben. Die grau hinterlegten Einträge sind derzeit nicht mit einem
Zeichen belegt.
```

```{figure} images/unicode/u2200.png
---
width: 80%
name: fig:unicode2200
---
Unicodezeichen im Bereich [2200‒227F](https://www.unicode.org/charts/PDF/U2200.pdf).
Der Unicode Codepoint sowie die UTF-8-Kodierung sind für jedes Zeichen blau bzw. grün
hinterlegt angegeben. 
```
