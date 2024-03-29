# Style Guide

Im Allgemeinen sollten Zusammenfassungen kurz und bündig sein. Sie dienen ja dazu, auf einen Blick viel Information zu bekommen, und nicht wie Skripten, um sich detailliert mit etwas auseinanderzusetzen. Es gelten die Sprichwörter: "Weniger ist mehr." und "In der Kürze liegt die Würze". Außerdem sollte Intuition im Vordergrund stehen. Zum Beispiel sollten komplexe Sachverhalte oder trockene Formeln so erläutert werden, dass man die dahinterstehenden Zusammenhänge begreift. 

## Überschriften, Header und Metadaten

Pandoc unterstützt Yaml-Metadaten-Header. Diese sollen auch genutzt werden, um den Titel des Dokuments anzugeben, vorzugsweise fett geschrieben. Die Yaml-Header sind jedoch noch wesentlich mächtiger. In ihnen kann eingestellt werden, ob ein Inhaltsverzeichnis erstellt werden soll, in welchem Format das PDF erstellt werden soll, ob weitere LaTeX-Pakete geladen werden soll und noch vieles mehr. Ein Blick in die [Dokumentation von Pandoc](https://pandoc.org/MANUAL.html#pandocs-markdown) zu diesem Thema kann sich auszahlen. Metadaten-Header beginnen mit einer Zeile `---` und enden mit einer Zeile `...`.

Dokumente sollten Überschriften haben im Format `<Dokumententyp>: <LVA-Name ohne LVA-Typ>`. So lautet etwa die Überschrift der Zusammenfassung der Vorlesung Digital Design "Zusammenfassung: Digital Design" und nicht "Zusammenfassung: VO Digital Design" und auch nicht "Digital Design -- Zusammenfassung". Wie eingangs erwähnt wird der Titel eines Dokuments im Yaml-Metadaten-Header angegeben. Um die Überschrift fett zu schreiben, soll sie zwischen doppelte Asteriske gestellt werden. Da die meisten Titel wohl Doppelpunkte enthalten werden, ist es nötig, den Titel zusätzlich zwischen Anführungsstriche zu stellen; ansonsten wäre das nicht nötig.

Standarmäßig wird automatisch ein Inhaltsverzeichnis erstellt. Sollte das nicht erwünscht sein, kann im Yaml-Metadaten-Header `toc: false` angegeben werden. Das Inhaltsverzeichnis beinhaltet Links zu den entsprechenden Kapiteln.

Es wird zwischen zwei Arten von Zusammenfassungen unterschieden: Die eine nennt sich `zusammenfassung` und ähnelt in ihrer Form einem typischen Skript. Sie wird also hochformatig im A4-Format dargestellt, hat eine Überschrift, ein Inhaltsverzeichnis, etc.. Die andere nennt sich `formula_sheet` und entspricht eher Lernkarten. (Entgegen ihres Namens dürfen aber auch gerne andere Lernkarten in diesem Format dargestellt werden, die nicht als Formelsammlung dienen.) Die gewünschte Art der Zusammenfassung wird im Metadata-Tag `summary-type` angegeben. Wird dieser Tag nicht angegeben oder wird dessen Inhalt falsch verstanden, wird das Dokument *nicht* übersetzt

Um zu erreichen, dass möglichst viele begeisterte Student*innen an den Zusammenfassungen mitwirken, wird automatisiert am Anfang des Dokuments ein Disclaimer eingefügt werden, der zum Mitmachen auffordert und auf das Github-Repo verweist.

Eine Zusammenfassung könnte also etwa einen Header haben wie den Folgenden haben:

~~~ 
---
summary-type: formula_sheet
title: "**<Titel der Zusammenfassung/Formelsammlung>**"
...

~~~


## Textgestaltung und Formatierung

### Fließtext

Langer Fließtext im Sinne von ausformulierten Sätzen sollten Sparsam verwendet werden. Wenn sich etwas in Stichwörtern oder Halbsätzen ausdrücken lässt, ist diese Variante zu bevorzugen, da sie einen zwingt, Texte auf Kernaussagen zu reduzieren und einem ermöglicht, sich mehr auf den Inhalt zu konzentrieren, statt nach passenden Formulierungen zu suchen.

Es bietet sich an, die einzelnen Stichwörter oder Halbsätze in Bullet-Lists zu Gruppieren und mit einem kleinen Header zu versehen, um Zusammengehörigkeiten besser darzustellen und außerdem den Text besser durchsuchbar zu machen. Zur Illustration, ein Ausschnitt aus der Zusammenfassung Digital Design:

> N- vs P-MOSFET:
>
> * n-mosfet gut in Sourceschaltung => treibt 0-er gut
> * p-mosfet gut in Sourcefolger => teibt 1-er gut
> * Kombination führt zu CMOS-Logik

Um einen einheitlichen Stil zu erreichen, wird gebeten die kleinen Header vor Bullet-Lists mit einem Doppelpunkt zu versehen.

### Links und Abbildungen

Links werden wie folgt erstellt:

~~~
Das ist ein [Link](http://meinewebsite/).
~~~

Links können auf eine URL verweisen, oder auch auf andere Stellen im Dokument, die mit einem entsprechenden Anker versehen sind:

~~~
Für nähere Informationen, siehe [Kapitel 3](#chap_3).
~~~

Auch Abbildungen können auf fast die gleiche Weise in Dokumente eingefügt werden:

~~~
![Bildbeschreibung](./img/meinbild.png){width=75%}
~~~

Beachte das führende Rufzeichen und *optionale*, nachgestellte Attribute. Für Bilder steht der Order `img` zur Verfügung. Bitte gebt den Bildern sinnvolle Namen! Sollte es nötig sein, selbst Abbildungen zu erstellen, etwa mit Tikz, sei auf den Punkt `Abbildungen erstellen` verwiesen

### Tabellen

Für eine ausführlichere Beschreibung, auf welche verschiedenen Arten man Tabellen in Markdown schreiben kann, sei auf die [Dokumentation von Pandoc-Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) verwiesen. Als Beispiel soll aber das folgende Snippet dienen:

~~~
--------------------------
 $A$   $B$   $A \wedge B$
----- ----- --------------
  0     0         0
  
  0     1         0
  
  1     0         0
  
  1     1         1
--------------------------

Table: Das ist eine Beispieltabelle
~~~

### Programm-Code

Blöcke mit Programm-Code werden zwischen zwei Zeilen mit je drei Tilden gestellt. Nach den "öffnenden" Tilden kann in geschwungenen Klammern die Sprache angegeben werden und die Zeilennummerierung aktiviert werden. Ein Beispiel wäre der folgende Code-Block:

```
~~~ {.c .number-lines}
int foo(){
	return 0;
}
~~~
```

### Hervorhebung durch farbige Markierung

Durch das LaTeX-Package `summary` werden drei Environments zur Verfügung gestellt, die dazu dienen, Abschnitte eines Textes durch farbige Markierungen hervorzuheben. Diese Environments heißen `note`, `example` und `theorem` und sind dazu gedacht genau das hervozuheben, was ihr Name bereits suggeriert. Der Titel eines solchen Abschnittes wird im einzigen Argument der Environments festgelegt. Dank des make.py-Skriptes ist es möglich, diese Umgebungen markdown-ähnlicher und benutzerfreundlicher einzubinden. Die Environments könnten also wie folgt verwendet werden:

~~~
:::theorem 2. Newtonsches Axiom
	$m \cdot \ddot{x}^i(t) = F^i(x^m(t))$
:::

:::note
Das ist eine Notiz ohne Titel
:::
~~~

Diese Umgebungen erhalten einen farbigen Balken am linken Rand der Seite. Dadurch ist es leicht möglich, besonders wichtige Aussagen hervorzuheben.

## Abbildungen erstellen

Um Abbildungen zu erstellen steht wie so oft LaTeX zur Verfügung. Im Ordner `./img/tex` können tex-Dateien erstellt werden, die zu PDFs übersetzt werden. Die einzelnen Seiten der PDFs werden als PNGs extrahiert. Standardmäßig werden die so erstellten Bilder einfach durchnummeriert. Alternativ kann aber auch ein Namenssuffix mit einem LaTeX-Power-Comment angegeben werden:

~~~
% output-name: my_awesome_name
~~~

(Dies ist eine weitere tolle Funktionalität des make.py-Skripts)
