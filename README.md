# Sammlung von Zusammenfassungen und anderen Materialien

Die Idee ist, eine Plattform zur Verfügung zu stellen, auf der alle Interessierten Zusammenfassungen von LVAs, Formelsammlungen oder Ausarbeitungen von Prüfungen erstellen und weiterentwickeln können. Hier sollen sie zwar 
entwickelt werden, aber schlussendlich sollen die so entstandenen Dokumente im [VoWi](https://vowi.fsinf.at/wiki/TU_Wien/Informatik) veröffentlicht werden.

## Style Guide

Im Allgemeinen sollten Zusammenfassungen kurz und bündig sein. Sie dienen ja dazu, auf einen Blick viel Information zu bekommen, und nicht wie Skripten, um sich detailliert mit etwas auseinanderzusetzen. Das ist natürlich nicht immer leicht. Dieses Ziel wird aber z.B. dadurch unterstützt, dass man sich in Form von Stichwörtern oder Halbsätzen in Bullet-Lists ausdrückt. Natürlich können können Zusammenfassungen auch in ganzen Sätzen formuliert sein, aber sie sollten eben nicht zu Skripten ausarten.

### Header und Metadaten

Dokumente sollten Überschriften haben im Format `<Dokumententyp>: <LVA-Name ohne LVA-Typ>`. So lautet etwa die Überschrift der Zusammenfassung der Vorlesung Digital Design "Zusammenfassung: Digital Design" und nicht "Zusammenfassung: VO Digital Design" und auch nicht "Digital Design -- Zusammenfassung".

Pandoc unterstützt Yaml-Metadaten-Header. Diese sollen auch genutzt werden, um den Titel des Dokuments anzugeben, vorzugsweise fett geschrieben. Standarmäßig wird automatisch ein Inhaltsverzeichnis erstellt. Sollte das nicht erwünscht sein, kann im Metadaten-Header `toc: false` angegeben werden. Damit möglichst viele Benutzer*innen des VoWis dazu animiert werden, auch an den Zusammenfassungen mitzuschreiben, empfiehlt es sich, nach dem Inhaltsverzeichnis -- i.e. direkt nach dem Metadaten-Header -- einen kurzen Disclaimer zwischen horizontalen Linien einzufügen, der zum Mitmachen auffordert und auf auf das Git-Repo verweist. Ein Dokument könnte also einen Header wie den folgenden haben:

~~~
---
title: "**<Titel der Zusammenfassung>**"
...

---

An dieser Zusammenfassung und der zugehörigen Formelsammlung kann gerne auf [Github](https://github.com/cornhead/zusammenfassungen.git) mitgewirkt werden!

---
~~~

Falls in einem Dokument Links auf andere Stellen im gleichen Dokument verwendet werden, müssen diese durch geeignete Formatierung hervorgehoben werden, denn standardmäßig erscheinen sie genau so wie der Fließtext.

## Tools

Die empfohlenen Tools sind `pandoc` und `make`. Außerdem wird `pdflatex` benötigt gemeinsam mit einigen Paketen, die in `texlive`, `texlive-latex-extra` und `texlive-lang-german` enthalten sein sollten (wobei ich mir nicht sicher bin, wie viel von `texlive-latex-extra` benötigt wird). Mit dem folgendem Befehl können die nötigen Programme unter Debian-Distributionen bequem installiert werden:

~~~
apt install make pandoc pdflatex texlive texlive-latex-extra texlive-lang-german
~~~

Geschrieben werden die Zusammenfassungen und Formelsammlungen in Markdown, weil es sehr einsteigerfreundlich ist und dennoch gut formatierte Ausgaben erzeugen kann -- empfehlenswert ist das [Markdown Quick Reference Cheat 
Sheet](https://wordpress.com/support/markdown-quick-reference/) von Wordpress. Um die Markdown-Files schließlich zu PDF zu parsen, wird Pandoc verwendet. Idealerweise wird Make verwendet um diesen Vorgang zu automatisieren.

