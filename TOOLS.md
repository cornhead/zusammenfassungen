# Tools

Für dieses Projekt werden im Wesentlichen `pandoc`, `python`, `pdflatex` und `imagemagick` verwendet. Außerdem werden natürlich für LaTeX einige Pakete gebraucht, die aber alle in  `texlive`, `texlive-latex-extra`, `texlive-lang-german` und `texlive-science` enthalten sein sollten (wobei ich mir nicht sicher bin, wie viel von `texlive-latex-extra` benötigt wird). Auch Python braucht natürlich ein paar Pakete: `sys`, `os`, `re`, `subprocess`, `textwrap`. Mit dem folgendem Befehl können die nötigen Programme unter Debian-Distributionen bequem installiert werden:

~~~
apt install make pandoc python3 texlive texlive-latex-extra texlive-lang-german texlive-science imagemagick
pip install sys os re subprocess textwrap
~~~

Für andere Linux-Distributionen stehen meistens vergleichbare Paket-Manager zur Verfügung. Unter Windows dürfte die Installation etwas schwieriger werden. Die einfachste Möglichkeit, das Framework dennoch zu verwenden, ist, ein Linux-Subsystem zu installieren (frag einfach DuckDuckGo, wie das geht) oder ganz auf Linux umzusteigen.

## Pandoc / Markdown

Geschrieben werden die Zusammenfassungen und Formelsammlungen in Markdown -- einer besonderns einfachen markup-Sprache -- weil es sehr einsteigerfreundlich ist und dennoch gut formatierte Ausgaben erzeugen kann. Um sich einen schnellen Überblick über die Markdown-Syntax zu verschaffen ist das [Markdown Quick Reference Cheat Sheet](https://wordpress.com/support/markdown-quick-reference/) von Wordpress empfehlenswert. Es gibt jedoch viele "Dialekte" von Markdown. In diesem Projekt wird derjenige von Pandoc verwendet. Alle Informationen dazu sind in der [Dokumentation von Pandoc-Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) zu finden. Insbesondere lohnt es sich, den Abschnitt über Metadata Blocks zu überfliegen.

Um die Markdown-Files schließlich zu PDF zu parsen, wird Pandoc verwendet. Idealerweise ist es nie nötig, sich näher mit den Befehlen von Pandoc vertraut zu machen, da das Kompilieren durch Make und Python automatisiert sein sollte. Beim Kompilieren wird Pandoc zusätzlich zu den Mardkdown-Files auch ein Metadata-File übergeben, das einige Standardeinstellungen und Standardwerte beinhaltet. Änderungen, die alle Dokumente betreffen, können darin vorgenommen werden. (Während des Kompilierens erzeugt Pandoc aus den Markdown-Files zuerst LaTeX-Files, die anschließend zu PDFs kompiliert werden. Darin begründet sich auch die Notwendigkeit von `pdflatex` samt einiger Pakete.)

## Make

Make wird dazu verwendet um, das kompilieren der Markdown-Files zu automatisieren. Tatsächlich ist das Makefile aber nur ein Wrapper für ein Python-Skript, das im Wesentlichen die Funktionalität von Make übernimmt, aber einige weitere Features implementiert.
