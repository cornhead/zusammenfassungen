# Sammlung von Zusammenfassungen und anderen Materialien

Die Idee ist, eine Plattform zur Verfügung zu stellen, auf der alle Interessierten Zusammenfassungen von LVAs, Formelsammlungen oder Ausarbeitungen von Prüfungen erstellen und weiterentwickeln können. Hier sollen sie zwar 
entwickelt werden, aber schlussendlich sollen die so entstandenen Dokumente im [VoWi](https://vowi.fsinf.at/wiki/TU_Wien/Informatik) veröffentlicht werden.

Bevor Du etwas zu diesem Repo beiträgst, lies bitte den [Style-Guide](./STYLEGUIDE.md) und die [Einführung in die verwendeten Tools](./TOOLS.md)... oder überflieg sie zumindest.

## Tools

Die empfohlenen Tools sind `pandoc` und `make`. Außerdem wird `pdflatex` benötigt gemeinsam mit einigen Paketen, die in `texlive`, `texlive-latex-extra` und `texlive-lang-german` enthalten sein sollten (wobei ich mir nicht sicher bin, wie viel von `texlive-latex-extra` benötigt wird). Mit dem folgendem Befehl können die nötigen Programme unter Debian-Distributionen bequem installiert werden:

~~~
apt install make pandoc pdflatex texlive texlive-latex-extra texlive-lang-german
~~~

Geschrieben werden die Zusammenfassungen und Formelsammlungen in Markdown, weil es sehr einsteigerfreundlich ist und dennoch gut formatierte Ausgaben erzeugen kann -- empfehlenswert ist das [Markdown Quick Reference Cheat 
Sheet](https://wordpress.com/support/markdown-quick-reference/) von Wordpress. Um die Markdown-Files schließlich zu PDF zu parsen, wird Pandoc verwendet. Idealerweise wird Make verwendet um diesen Vorgang zu automatisieren.

