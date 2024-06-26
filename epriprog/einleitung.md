(einleitung)=
# Einleitung

## Warum Programmieren lernen?

Viele Geräte, mit denen wir es im modernen Leben zu tun haben, werden von
Computern gesteuert, seien es Autos, Fernseher oder Smartphones, um nur ein
paar Beispiele zu nennen. Um Auto fahren zu können, benötigt man sicherlich
keine Computerkenntnisse und muss keine Programmiersprache beherrschen.
Ein Smartphone kann man benutzen ohne selbst die zugehörigen Apps zu
programmieren, auch wenn dies durchaus eine interessante und produktive
Tätigkeit sein kann.

Ein weiteres Alltagsgerät, das nicht ohne Computer auskommt, ist die Digitalkamera,
ganz gleich ob als eigenständiger Fotoapparat oder als Teil eines Smartphones.
Man kann sich vorstellen, dass man das digitale Bild weiterbearbeiten möchte.
Für viele Bildbearbeitungsaufgaben sind geeignete Programme verfügbar, aber
es kann auch Fälle geben, in denen man selbst programmieren muss, zum Beispiel
wenn man eine Exponentialfunktion auf einen Waschbären anwenden möchte
({numref}`fig:exponential_raccoon`).

```{figure} images/einleitung/exponential_raccoon.png
---
width: 10cm
name: fig:exponential_raccoon
---
Originalbild eines Waschbärs (links) und nach Anwendung einer Exponentialfunktion
(rechts).
```

````{margin}
```{admonition} Tipp
:class: tip
Eine größere Darstellung von Abbildung können Sie durch Klicken auf das
entsprechende Bild erhalten.
```
````

Das Beispiel der Digitalkamera schlägt die Brücke vom Alltag ins Labor. Im
Grunde genommen ist eine Digitalkamera nichts anderes als ein Messgerät, das
optische Information in digitale Daten umwandelt und zur Verfügung stellt, sei
es als Rohdaten oder in einer vorverarbeiteten Form. Im Labor wird es erforderlich
sein, mit dem Messgerät zu kommunizieren, um Messdaten herunterzuladen. Häufig
geschieht dies mit einem vom Hersteller zur Verfügung gestellten Programm, aber
man kann sich auch vorstellen, dass man die Schnittstelle des Messgeräts, über
die die Messdaten zur Verfügung gestellt werden, mit eigenem Programm anspricht.

Selbst wenn das Messgerät einen ersten Verarbeitungsschritt der Rohdaten durchführen
sollte, sind im Allgemeinen weitere Auswertungen der Daten erforderlich, um 
wissenschaftlich relevante Informationen zu extrahieren. Hierfür stehen
unter Umständen Softwarelösungen, meistens kommerzieller Art, zur Verfügung. 
Andererseits ist es häufig sinnvoll oder sogar erforderlich, die Verarbeitung
der Daten mit einem eigenen Programm vorzunehmen. Damit hat man den Workflow
unter Kontrolle. Gerade mit der in dieser Vorlesung verwendeten Programmiersprache
Python steht mit dem Jupyter-Notebook auch ein Werkzeug zur Verfügung, dass für
die Dokumentation der Datenanalyse hervorragend geeignet ist.

Ein solches Vorgehen, bei dem man selbst programmiert, schließt keineswegs aus,
dass man auf Bausteine von anderen zurückgreift. Es ist nicht nötig und meistens
auch nicht sinnvoll, das Rad neu zu erfinden. Will man beispielsweise seine
Daten graphisch darstellen, so wird man ein Programm schreiben, um die Daten
geeignet aufzubereiten und die Abbildung in der gewünschten Form zu erhalten,
aber man wird deswegen nicht gleich ein eigenes Programmpaket zur Erzeugung
von Abbildungen schreiben. Wir werden im Lauf der Vorlesung ein paar ausgewählte
Programmpakete ansprechen, die im wissenschaftlichen Bereich häufig genutzt
werden.

Nicht nur im experimentellen Bereich sind Programmierkenntnisse erforderlich,
sondern auch in der theoretischen Arbeit. Will man als Ingenieur die Kräfte in
einem Bauteil bestimmen, so ist diese Aufgabe im Allgemeinen so komplex, dass
zu ihrer Lösung ein Programm geschrieben werden muss. Auch hier wird man auf
vorhandene Programmpakete, z.B. für Finite-Elemente-Methoden, zurückgreifen
können, aber das befreit einen nicht davon, auch selbst zu programmieren.
Auch die Eigenschaften von neuen Materialien werden zunehmend zunächst mit
Hilfe von Computern theoretisch berechnet. Die Bedeutung des Programmierens
im naturwissenschaftlichen Bereich wird unter anderem daran deutlich, dass
neben die Experimentalphysik und die Theoretische Physik inzwischen die
computergestützte Physik oder *Computational Physics* getreten ist.

Letztlich wird man im natur- und ingenieurwissenschaftlichen Bereich früher
oder später mit Programmieraufgaben konfrontiert sein und das Schreiben eines
Computerprogramms gehört genauso zum Handwerkszeug wie der Umgang mit Papier
und Bleistift. Nicht zuletzt werden Programmierkenntnisse auch an verschiedensten
Stellen in der Industrie vorausgesetzt, wie wir weiter unten noch sehen werden.

Programmieren zu können ist aber nicht nur eine Notwendigkeit für
Naturwissenschaftler, Programmieren kann auch einfach Spaß machen. So wie das
Knobeln an einer wissenschaftlichen Aufgabe (hoffentlich) Spaß macht, gilt dies
auch für die Suche nach einer eleganten und effizienten Lösung eines Problems
auf dem Computer [^euler]. Zugegeben: Es kann durchaus nerven, wenn der
Computer ständig Fehler anmahnt und dabei äußerst starrsinnig ist. Allerdings
hat er praktisch immer recht. Da hilft es nur, die Fehlermeldungen ernst zu
nehmen und ein bisschen Gelassenheit an den Tag zu legen. Dafür beschwert sich
der Computer auch nicht, wenn er uns lästige Arbeit abnehmen muss, indem er zum
Beispiel zuverlässig immer wieder die gleichen Programmanweisungen abarbeitet.

[^euler]: Wer Spaß am Programmieren und am Lösen mathematischer Probleme hat
     oder einfach die gelernten Programmierfähigkeiten ausprobieren möchte,
     sollte einen Blick auf [projecteuler.net](http://projecteuler.net/) werfen.

(warumpython)=
## Warum Python?

Das Ziel des Programmierens ist es, dem Computer zu erklären, was von ihm
erwartet wird. Leider verstehen Computer nur Nullen und Einsen. Auch wenn
es durchaus möglich ist, auf dieser Ebene ein Programm zu schreiben, ist es doch
recht mühsam. Stattdessen gibt es eine Vielzahl von Programmiersprachen
[^languages], die es für den Menschen mehr oder weniger leicht machen, ein
Programm zu schreiben. Dieses wird dann entweder mit Hilfe eines so genannten
Interpreters oder mit Hilfe eines Compilers in eine maschinenlesbare Form
übersetzt. 

[^languages]: Für eine Übersicht siehe z.B. die [Liste von Programmiersprachen
auf Wikipedia](https://de.wikipedia.org/wiki/Liste_von_Programmiersprachen).

Einige dieser Programmiersprachen, aber bei weitem nicht alle, sind im
naturwissenschaftlichen Bereich besonders gebräuchlich. Beispielhaft seien
Fortran, C, C++, Python und Julia genannt. Diesen Sprachen haben grundlegende
Sprachelemente gemeinsam, die zwar in den verschiedenen Sprachen unterschiedlich
dargestellt werden, aber die gleiche Funktionalität besitzen. Wir werden dies
später an einzelnen Beispielen noch sehen.

Zur Erläuterung grundlegender Prinzipien der Programmierung wird in dieser
Vorlesung die Programmiersprache *Python* herangezogen. Dabei liegt der Fokus
auf Konzepten, wie sie auch in den anderen gerade genannten Programmiersprachen
typischerweise existieren. Diese Vorlesung stellt also keinen
Python-Programmierkurs im engeren Sinne dar. Das Ziel ist es dennoch, auch
Studierende ohne oder mit nur wenig Programmiererfahrung in die Lage zu
versetzen, Problemstellungen mit Hilfe von *Python* zu lösen.

Gründe für diese Wahl der Programmiersprache sind unter anderem:

- Es handelt sich um eine relativ leicht zu erlernende Programmiersprache, die
  aber dennoch sehr mächtig ist.
- Python ist für die gängigen Betriebssysteme, insbesondere Linux, MacOSX und
  Windows, frei erhältlich und kann somit problemlos auf dem eigenen Rechner
  installiert werden.
- Es unterstützt das Schreiben gut lesbarer Programme.
- Als interpretierte Sprache erlaubt Python das schnelle Testen von
  Codesegmenten im Interpreter und unterstützt somit das Lernen durch Ausprobieren.
- Python besitzt eine umfangreiche Standardbibliothek (»Python comes with batteries
  included«) und das wissenschaftliche Rechnen wird durch eine Vielzahl freier
  Programmbibliotheken, wie {program}`NumPy/SciPy`, das wir im Kapitel {ref}`scipy`
  besprechen werden, unterstützt.
- Python hat sich in den letzten Jahren zu einer sehr populären Sprache
  entwickelt, unter anderem im Bereich der wissenschaftlichen Datenanalyse.

Bei den beiden physikalischen Beobachtungen, die in den letzten Jahren die
Aufmerksamkeit einer breiten Öffentlichkeit erregten, nämlich die Beobachtung
von Gravitationswellen [^prd93] und die Aufnahme des Abbilds eines schwarzen
Loches ({numref}`fig:eso1907a`) [^ApJL875L1], spielte Python bei der Datenanalyse
eine wichtige Rolle. Die Verarbeitung der Bilddaten des schwarzen Loches
erfolgte unter Verwendung wissenschaftlicher Programmpakete von Python wie
[NumPy](https://numpy.org/), [SciPy](https://www.scipy.org),
[Pandas](https://pandas.pydata.org), [Jupyter](https://jupyter.org), und
[Matplotlib](https://matplotlib.org) [^ApJL875L3].

[^prd93]: B. P. Abbott *et al.*, [Phys. Rev. D **93**, 122003
(2016)](https://doi.org/10.1103/PhysRevD.93.122003). Das Analysepaket PyCBC
basiert auf Python und auch das Analysepaket GstLAL enthält einige
Pythonskripte.
[^ApJL875L1]: The Event Horizon Telescope Collaboration, [Astrophys. J. Lett.
**875**, L1 (2019)](https://doi.org/10.3847/2041-8213/ab0ec7).
[^ApJL875L3]: The Event Horizon Telescope Collaboration, [Astrophys. J. Lett.
**875**, L3 (2019)](https://doi.org/10.3847/2041-8213/ab0c57).

```{figure} images/einleitung/eso1907a.jpg
---
width: 10cm
name: fig:eso1907a
---
Abbild eines schwarzen Lochs aus Aufnahmen des Event Horizon Telescopes.
(Urheber: EHT Collaboration)
```

Die folgenden Zitate zeigen, dass Python nicht nur zur Einführung in das
Programmieren taugt, sondern auch für große Projekte in führenden IT-Firmen,
Forschungseinrichtungen sowie der Finanz- und Filmindustrie verwendet wird [^psf]:

[^psf]: Zitiert nach [python, Case Studies & Success Stories, Vol. I (Python
     Software Foundation)](https://brochure.getpython.info/media/releases/psf-python-brochure-vol.-i-final-download.pdf/at_download/file)

- Peter Norvig, Google    
 
  «Python has been an important part of Google since the beginning, and remains
  so as the system grows and evolves. Today dozens of Google engineers use
  Python, and we're looking for more people with skills in this language.»

- Cuong Do, YouTube.com    
 
  «Python is fast enough for our site and allows us to produce maintainable
  features in record times, with a minimum of developers.»

- Benedikt Hegner, CERN    
 
  «Most developers in the CMS experiment are physics students looking
  for new physics in the data. Usually they don’t have any formal IT training.
  Python allows them to be productive from the very start and to dedicate
  most of their time on the research they want to carry out.»

- Holger Joukl, Manuela Kälberer, Rainer Kluger,
  Landesbank Baden-Württemberg IT Financial Markets

  «There are lots of other programming languages with outstanding features.
  We don’t know of any other programming language with features
  and a syntax as elegant and concise as Python, though.»

- Tommy Burnette, Lucasfilm    
 
  «Python plays a key role in our production pipeline. Without it a project
  the size of The Avengers would have been very difficult to pull off.
  From crowd rendering to batch processing to compositing, Python
  binds all things together.»

## Einige Zutaten

Um auf einem Computer programmieren zu können, ist es im Allgemeinen zunächst
erforderlich, die hierfür nötige Software zu installieren, sofern sie nicht
ohnehin schon vorhanden ist. Zum einen muss man die Möglichkeit haben, dem
Computer die eigenen Absichten mitzuteilen, also ein Programm einzugeben, und
zum anderen muss der Computer wissen, wie er die Hardware des Computers dazu
bringt, die Vorgaben des Programms umzusetzen.

Beginnen wir mit dem zweiten Punkt und nehmen wir an, dass wir den Programmcode,
der in unserem Fall in der Programmiersprache Python geschrieben ist, bereits
eingegeben haben. Damit der Computer hiermit etwas anfangen kann, bedarf es
bei Python eines sogenannten Interpreters, der den Programmcode interpretiert
und auf der Computerhardware ausführen lässt.

Grundsätzlich kann man die aktuellste Version des Python-Interpreters von der
[offiziellen Python-Webseite](http://www.python.org/)
herunterladen. Zum Zeitpunkt der Erstellung dieses Manuskripts war die Version
3.12.0 aktuell. Wie weiter unten noch kurz diskutiert wird, ist im Rahmen dieser
Vorlesung jede Version ab Python 3.8 brauchbar.

Neben dem eigentlichen Python-Interpreter werden wir für wissenschaftliche
Anwendungen häufig noch weitere Software benötigen, wie zum Beispiel die frei
verfügbaren numerischen Programmbibliotheken
[{program}`NumPy`](https://numpy.org/) und
[{program}`SciPy`](https://www.scipy.org), die wir im Kapitel {ref}`scipy`
besprechen werden. Es ist daher am einfachsten, eine Python-Distribution, also
eine Art Komplettpaket, das sowohl den Python-Interpreter als auch eine Reihe
von Programmbibliotheken enthält, zu installieren. Verzichtet man auf die
Installation einer geeigneten Distribution, so müssen die benötigten
Programmbibliotheken zusätzlich installiert werden.

Die aktuelle Standard-Distribution für Python im wissenschaftlichen Bereich ist
die [Anaconda-Distribution](https://www.anaconda.com/products/individual), die
für die gängigen Betriebssysteme Windows, MacOS und Linux frei verfügbar ist.
Damit erhält man auf sehr einfach Weise eine sehr umfangreiche Sammlung an
Programmpaketen, muss aber 3-4 GB freien Plattenplatz investieren. Alternativ
kann man sich [miniconda](https://docs.conda.io/en/latest/miniconda.html)
installieren, muss dann aber alle benötigten Programmpakete mit Hilfe von
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)
separat installieren.

Kommen wir nun zu dem oben als erstes genannten Punkt: Wie sage ich es meinem
Computer? Offenbar muss man das Python-Programm in irgendeiner Form dem
Computer mitteilen. Hierfür gibt es eine Reihe von Möglichkeiten, die je nach
Anwendungszweck geeignet sind und im Folgenden kurz beschrieben werden sollen.

Manchmal hat man es nur mit kurzen Codestücken zu tun. Dies ist vor allem der
Fall, wenn man schnell etwas ausprobieren möchte. Dann eignet sich die
Python-Shell, in der man zeilenweise Python-Code eingeben kann, der
anschließend ausgeführt wird. Sobald Python installiert ist, ist auch die
zugehörige Python-Shell verfügbar. {numref}`fig:pythonshell` zeigt die
Python-Shell in einem Konsolenfenster unter Linux.

```{figure} images/einleitung/pythonshell.png
---
width: 80%
name: fig:pythonshell
---
Programmierung von wenigen Zeilen direkt in der Python-Shell.
```

Allerdings ist die Python-Shell nicht sehr komfortabel. Da Tippfehler in den
vorhergehenden Zeilen nicht leicht korrigiert werden können, kann das Arbeiten
mit der Python-Shell schnell lästig werden.  Eine erheblich komfortablere
Variante der Python-Shell ist die [IPython-Shell](http://ipython.org/), die
beispielsweise bei der Anaconda-Distribution automatisch installiert wird.
Hier kann man alte Eingaben zurückholen, Befehle ergänzen lassen und vieles
mehr. In {numref}`fig:ipythonshell` ist auch zu sehen, dass diese Shell Teile der
Eingabe je nach ihrer Funktion einfärbt.  Man spricht hierbei von *Syntax
Highlighting*, das bei der Fehlersuche hilfreich sein kann. Es ist daher
sinnvoll, statt der Python-Shell grundsätzlich die IPython-Shell zu verwenden.

```{figure} images/einleitung/ipythonshell.png
---
width: 80%
name: fig:ipythonshell
---
Eine komfortablere Python-Shell bietet IPython, unter anderem mit *Syntax Highlighting*.
```

Interessant ist die Verwendung von so genannten Jupyter-Notebooks, die es
erlauben, interaktiv mit Python unter Verwendung von Jupyterlab in einem
Browser zu arbeiten. Wie die {numref}`fig:jupyterlab` zeigt, gibt es hier neben
Codezellen auch Textzellen, die sogar Formeln enthalten können, und von
ausgeführtem Code erzeugte Resultate werden ebenfalls in das Notebook
integriert. Dabei kann es sich, wie in {numref}`fig:jupyterlab`
dargestellt, beispielsweise auch um graphische Darstellungen handeln. Das
Jupyter-Notebook eignet sich unter anderem hervorragend dafür, die Schritte
einer Datenanalyse zu dokumentieren, um sie auch später nachvollziehen zu
können.

```{figure} images/einleitung/jupyterlab.png
---
width: 15cm
name: fig:jupyterlab
---
Beispiel eines Jupyter-Notebooks in Jupyterlab. Das graphische Ergebnis
einer der beiden Codezellen wird innerhalb des Notebooks dargestellt.
In Textzellen lassen sich auch Formeln einbetten.
```

Da Notebookzellen mehrzeiligen Code enthalten können, sind IPython-Notebooks
prinzipiell auch dafür geeignet, etwas umfangreicheren Code damit zu
entwickeln. Für größere Programmierprojekte bieten sich allerdings bessere
Werkzeuge an. Eine Möglichkeit ist die Verwendung von Editoren wie
[{program}`EMACS`](http://www.gnu.org/software/emacs/)
oder [{program}`Vim`](http://www.vim.org/), die zur Erstellung jeglicher Art von
Textdateien und damit auch zum Erstellen von Pythonprogrammen verwendbar sind.
Diese Editoren sind sehr mächtig und erfordern daher etwas Einarbeitung, die
sich aber auf längere Sicht durchaus lohnen kann. Wer die Mühe der Einarbeitung
scheut, kann für die Programmentwicklung auch zu einer der verschiedenen
verfügbaren graphischen Entwicklungsumgebungen greifen.

Python stellt eine relativ einfache Entwicklungsumgebung namens
[IDLE](https://docs.python.org/3/library/idle.html) zur Verfügung. Daneben gibt
es eine Reihe von freien wie auch von kostenpflichtigen Entwicklungsumgebungen.
In der Anaconda-Distribution wird die graphische Entwicklungsumgebung
[Spyder](https://www.spyder-ide.org/) [^spyder] mitgeliefert, die in {numref}`fig:spyder`
gezeigt ist.

[^spyder]: Spyder steht für «Scientific PYthon Development EnviRonment»

Das Spyder-Fenster besteht aus verschiedenen Teilfenstern. In dem in
{numref}`fig:spyder` gezeigten Beispiel befindet sich links ein Editorfenster,
in dem auch problemlos ein längeres Programm eingegeben werden kann. Rechts
unten erkennen wir ein IPython-Fenster, in dem, wie weiter oben beschrieben,
kürzere Codesegmente getestet werden können. Dies ist besonders hilfreich, wenn
man beim Programmieren nicht sicher ist, ob ein bestimmter Programmcode
wirklich das Beabsichtigte leistet. In dem IPython-Fenster erfolgt auch die
Ausgabe von Ergebnissen, wenn man den Code im linken Fenster ausführt.  Ein
weiteres Fenster dient unter anderem zur Anzeige von Dokumentation oder zur
Fehlersuche. Je nach Bedarf lässt sich das Spyder-Fenster anpassen, aber
zumindest zu Beginn sollte die Standardeinstellung angemessen sein. Wir können
an dieser Stelle keine ausführliche Einführung in Spyder geben und verweisen
stattdessen auf die zugehörige
[Dokumentation](https://docs.spyder-ide.org/current/index.html).

```{figure} images/einleitung/spyder.png
---
width: 15cm
name: fig:spyder
---
Python-Entwicklungsumgebung Spyder
```

## Literatur

- [www.python.org](http://www.python.org/)

  Dies ist die offizielle Python-Webseite. Dort gibt es z.B. die Software zum Herunterladen, 
  eine umfangreiche [Dokumentation der Programmiersprache](https://docs.python.org/3/), insbesondere ihrer
  [Standardbibliothek](https://docs.python.org/3/library/index.html) sowie
  Verweise auf [einführende Literatur](https://wiki.python.org/moin/PythonBooks) und einiges mehr.

- Michael Weigend, *Python GE-PACKT* (MITP-Verlag, 2020) 

   Dieses Buch eignet sich als kompaktes Nachschlagewerk. Die 8. Auflage berücksichtigt
   die Python-Version 3.8.

- Hans Petter Langtangen, *A Primer on Scientific Programming with Python* (Springer, 2012)

## Python-Version

Python befindet sich in aktiver Entwicklung, wobei jährlich eine neue Unterversion
veröffentlicht wird. Jede Version wird über fünf Jahre bei Bedarf mit Fehlerkorrekturen
versorgt. Aktuell ist Python 3.8 die älteste Version, die noch unterstützt wird. Von
ganz wenigen Ausnahmen abgesehen, auf die dann besonders hingewiesen wird, ist der
Code zu dieser Vorlesung unter Python 3.8 lauffähig, aber es spricht natürlich auch
nichts dagegen, eine neuere Version wie zum Beispiel Python 3.11 oder 3.12 zu verwenden.
