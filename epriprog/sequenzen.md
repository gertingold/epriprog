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

In Python dagegen stehen solche homogenen Datenansammlungen in Form von Array nicht im
Standardsprachumfang zur Verfügung. Sie werden aber durch die Programmbibliothek NumPy,
die die Basis für wissenschaftliche Numerik in Python bildet und die wir im
{numref}`scipy` besprechen werden, bereitgestellt. Python stellt stattdessen standardmäßig
den Datentyp einer Liste zur Verfügung, die Objekte verschiedener Datentypen enthalten
kann, aber nicht muss. Die größere Flexibilität der Liste gegenüber den Arrays bezahlt man
mit einem höheren Aufwand beim Zugriff auf einzelne Elemente. Wir werden im Folgenden
Listen als Datentyp in Python besprechen. Viele Aspekte werden wir später auf die von
NumPy zur Verfügung gestellten Arrays übertragen können.


(tupel)=
## Tupel

(strings)=
## Zeichenketten

(dictionaries)=
## Dictionaries
