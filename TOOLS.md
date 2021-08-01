# Tools

Für dieses Projekt werden im Wesentlichen `pandoc` und `make` verwendet. Außerdem wird `pdflatex` benötigt gemeinsam mit einigen Paketen, die in `texlive`, `texlive-latex-extra`, `texlive-lang-german` und `texlive-science` enthalten sein sollten (wobei ich mir nicht sicher bin, wie viel von `texlive-latex-extra` benötigt wird). Mit dem folgendem Befehl können die nötigen Programme unter Debian-Distributionen bequem installiert werden:

~~~
apt install make pandoc pdflatex texlive texlive-latex-extra texlive-lang-german texlive-science imagemagick
~~~

Für andere Linux-Distributionen stehen meistens vergleichbare Paket-Manager zur Verfügung.

## Pandoc / Markdown

Geschrieben werden die Zusammenfassungen und Formelsammlungen in Markdown -- einer besonderns einfachen markup-Sprache -- weil es sehr einsteigerfreundlich ist und dennoch gut formatierte Ausgaben erzeugen kann. Um sich einen schnellen Überblick über die Markdown-Syntax zu verschaffen ist das [Markdown Quick Reference Cheat 
Sheet](https://wordpress.com/support/markdown-quick-reference/) von Wordpress empfehlenswert. Es gibt jedoch viele "Dialekte" von Markdown. In diesem Projekt wird derjenige von Pandoc verwendet. Alle Informationen dazu sind in der [Dokumentation von Pandoc-Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) zu finden. Insbesondere lohnt es sich, den Abschnitt über Metadata Blocks zu überfliegen.

Um die Markdown-Files schließlich zu PDF zu parsen, wird Pandoc verwendet. Idealerweise ist es nie nötig, sich näher mit den Befehlen von Pandoc vertraut zu machen, da das Kompilieren durch Make automatisiert sein sollte. Beim Kompilieren wird Pandoc zusätzlich zu den Mardkdown-Files auch ein Metadata-File übergeben, das einige Standardeinstellungen und Standardwerte beinhaltet. Änderungen, die alle Dokumente betreffen, können darin vorgenommen werden. (Während des Kompilierens erzeugt Pandoc aus den Markdown-Files zuerst LaTeX-Files, die anschließend zu PDFs kompiliert werden. Darin begründet sich auch die Notwendigkeit von `pdflatex` samt einiger Pakete.)

## Make

Make wird dazu verwendet um, das kompilieren der Markdown-Files zu automatisieren. Im Makefile können alle möglichen Pandoc-Extensions ergänzt werden, die benötigt werden. Außerdem müssen dort die Markdown-Files hinzugefügt werden, die dazu bestimmt sind, kompiliert zu werden. Mit dem Befehl `make all` können dann alle Markdown-Files auf einmal kompiliert werden. Mit `make clean` können die Kompilate wieder entfernt werden.

