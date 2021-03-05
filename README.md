# Sammlung von Zusammenfassungen und anderen Materialien

Die Idee ist, eine Plattform zur Verfügung zu stellen, auf der alle Interessierten Zusammenfassungen von LVAs, Formelsammlungen oder Ausarbeitungen von Prüfungen erstellen und weiterentwickeln können. Hier sollen sie zwar 
entwickelt werden, aber schlussendlich sollen die so entstandenen Dokumente im [VoWi](https://vowi.fsinf.at/wiki/TU_Wien/Informatik) veröffentlicht werden.

## Style Guide

### Header und Metadaten
Pandoc unterstützt Yaml-Metadaten-Header. Diese sollen auch genutzt werden, um den Titel des Dokuments anzugeben, vorzugsweise fett geschrieben. Standarmäßig wird automatisch ein Inhaltsverzeichnis erstellt. Sollte das nicht erwünscht sein, kann im Metadaten-Header `toc: false` angegeben werden. Damit möglichst viele Benutzer*innen des VoWis dazu animiert werden, auch an den Zusammenfassungen mitzuschreiben, empfiehlt es sich, nach dem Inhaltsverzeichnis -- i.e. direkt nach dem Metadaten-Header -- einen kurzen Disclaimer zwischen horizontalen Linien einzufügen, der zum Mitmachen auffordert und auf auf das Git-Repo verweist. Ein Dokument könnte also einen Header wie den folgenden haben:

```
---
title: "**<Titel der Zusammenfassung>**"
...

---

An dieser Zusammenfassung und der zugehörigen Formelsammlung kann gerne auf [Github](https://github.com/cornhead/zusammenfassungen.git) mitgewirkt werden!

---
```

Falls in einem Dokument Links auf andere Stellen im gleichen Dokument verwendet werden, müssen diese durch geeignete Formatierung hervorgehoben werden, denn standardmäßig erscheinen sie genau so wie der Fließtext.

## Tools

Die empfohlenen Tools sind `pandoc` und `make`.

Geschrieben werden die Zusammenfassungen und Formelsammlungen in Markdown, weil es sehr einsteigerfreundlich ist und dennoch gut formatierte Ausgaben erzeugen kann -- empfehlenswert ist das [Markdown Quick Reference Cheat 
Sheet](https://wordpress.com/support/markdown-quick-reference/) von Wordpress. Um die Markdown-Files schließlich zu PDF zu parsen, wird Pandoc verwendet. Idealerweise wird Make verwendet um diesen Vorgang zu automatisieren.

## Todo:

Momentan könnten folgende Punkte noch verbessert werden:
* Rechtschreibung (insbesondere am Anfang habe ich auf Groß-/Kleinschreibung gänzlich verzichtet...)
* Bilder: falls jemand eine gute Möglichkeit findet, Bilder und Skizzen einzubinden, wäre es bestimmt cool wenn neben all den erwähnten Schaltungen auch ein entsprechendes Bild zu sehen wäre.
* Formelsammlung ergänzen: Ich habe gegen Ende vernachlässigt die Formeln auch in die Formelsammlung zu kopieren
