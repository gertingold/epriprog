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

(zusgdatentypen)=
# Zusammengesetzte Datentypen

```{admonition} Hinweis
:class: warning
Dieses Kapitel befindet sich noch in Bearbeitung.
```

(listen)=
## Listen

Bei der Lösung numerischer Probleme spielen die Zahlentypen, die wir im {numref}`datentypen`
kennengelernt haben, also Integers, Gleitkommazahlen oder Floats sowie komplexe Zahlen eine
zentrale Rolle. Insbesondere in den Natur- und Ingenieurwissenschaften sind diese Daten aber
Bestandteile von komplexeren Datentypen wie Vektoren oder Matrizen. Man spricht in diesem
Zusammenhang von zusammengesetzten Datentypen, die wir im Folgenden behandeln wollen. Dabei
müssen die Bestandteile nicht unbedingt numerischer Natur sein. Ein Beispiel hierfür wären
Zeichenketten.

Bei den zusammengesetzten Datentypen ist es sinnvoll, eine Unterscheidung vorzunehmen, die
die Art der einzelnen Bestandteile betrifft. In Programmiersprachen wie Fortran oder C
kennt man den Datentyp des Arrays, das eine ein- oder mehrdimensionale Ansammlung von
Zahlen des gleichen Datentyps umfasst. Jedes Element nimmt im Speicher gleich viel Platz
in Anspruch und die aufeinanderfolgende Elemente schließen im Speicher nahtlos aneinander
an. Da die Anordnung der Elemente im Speicher immer eindimensional ist, gibt es für die
Speicherung mehrdimensionaler Array unterschiedliche Zugänge und tatsächlich unterscheiden
sich Fortran und C in dieser Hinsicht. Die homogene Struktur von Arrays hat zur Folge,
dass der Ort eines durch einen Index oder auch mehrere Indizes addressierten Elements im
Speicher ausgehend von der Startadresse unmittelbar berechnet werden kann. Dadurch kann
man sehr effizient auf Elemente des Arrays zugreifen.

In Python dagegen stehen solche homogenen Datenansammlungen in Form von Arrays nicht im
Standardsprachumfang zur Verfügung. Sie werden aber durch die Programmbibliothek NumPy,
die die Basis für wissenschaftliche Numerik in Python bildet und die wir im
{numref}`scipy` besprechen werden, bereitgestellt. Python stellt stattdessen standardmäßig
den Datentyp einer Liste zur Verfügung, die Objekte verschiedener Datentypen enthalten
kann, aber nicht muss. Die größere Flexibilität der Liste gegenüber den Arrays bezahlt man
mit einem höheren Aufwand beim Zugriff auf einzelne Elemente. Wir werden im Folgenden
Listen als Datentyp in Python besprechen. Viele Aspekte werden wir später auf die von
NumPy zur Verfügung gestellten Arrays übertragen können.

Listen sind uns beispielsweise bereits in {numref}`forloop` begegnet, wo wir die
{func}`range`-Funktion verwendet hatten, um einen Schleifenzähler mit Werten zu versorgen.
Dabei werden die benötigten Werte nur bei Bedarf erzeugt. Um alle Werte auf einmal zu
sehen, hatten wir die {func}`list`-Funktion verwendet und dabei eine Liste erzeugt.
```{code-cell} python
meine_liste = list(range(20))
print(meine_liste)
print(type(meine_liste))
```
Mit der zweiten Ausgabezeile wird hier nachgewiesen, dass der Datentyp des Objekts
`meine_liste` tatsächlich eine Liste ist.

Wenn man die Länge einer Liste nicht kennt, kann man diese mit Hilfe der {func}`len`-Funktion
bestimmen.
```{code-cell} python
liste1 = list(range(1, 17, 3))
print(f'Länge der ersten Liste:  {len(liste1)} Elemente')
liste2 = ['Stein', 'Papier', 'Schere']
print(f'Länge der zweiten Liste: {len(liste2)} Elemente')
```

Eine wichtige Eigenschaft von Listen besteht darin, dass man einzelne Listenelement oder auch
Ausschnitte aus der Liste adressieren kann und diese auch verändern kann. Wir demonstrieren
dies zunächst an einem einzelnen Listenelement.
```{code-cell} python
meine_liste = [1, 17, 3]
print(meine_liste[1])
```
Das Ergebnis zeigt, dass die Zählung in Python bei 0 beginnt, wie es beispielsweise auch in
der Programmiersprache C der Fall ist. Diese Wahl lässt sich dadurch motivieren, dass die Position
des ersten Elements einer Liste relativ zum Beginn der Liste im Speicherplatz durch einen Offset
von 0 gegeben ist. Man könnte aber auch argumentieren, dass das erste Element durch den Index 1
addressiert werden sollte. Diese Wahl wurde in der Programmiersprache Fortran getroffen. Man muss
sich also diesbezüglich informieren, welche Konvention in der verwendeten Programmiersprache gilt.

Eine Veränderung eines Listenelements ist durch eine Zuweisung für das betreffende Listenelement
möglich.
```{code-cell} python
meine_liste[1] = 2
print(meine_liste)
```

(tupel)=
## Tupel

(strings)=
## Zeichenketten

(dictionaries)=
## Dictionaries
