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

## Dokumentation von Funktionen

## Lokale und globale Variable

## Rekursive Funktionen

## Funktionen als Argumente von Funktionen

(lambdafunktionen)=
## Lambda-Funktionen

## Schlüsselworte und Defaultwerte
