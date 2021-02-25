# Digital Design - Materialien
---

Die Idee ist ganz einfach: Am Ende soll es eine gut verständliche, vollständige Zusammenfassung samt Abbildungen und Formelsammlung der VO Digital Design geben.

Geschrieben werden die Zusammenfassung und Formelsammlung in Mark-Down. Um das Mark-Down in PDF zu konvertieren, soll es zuerst in LaTeX geparst werden (z.B. mit Pandoc), sodass danach noch das Layout verfeinert werden kann.

Momentan könnten folgende Punkte noch verbessert werden:
* Rechtschreibung (insbesondere am Anfang habe ich auf Groß-/Kleinschreibung gänzlich verzichtet...)
* Bilder: falls jemand eine gute Möglichkeit findet, Bilder und Skizzen einzubinden, wäre es bestimmt cool wenn neben all den erwähnten Schaltungen auch ein entsprechendes Bild zu sehen wäre.
* Formelsammlung ergänzen: Ich habe gegen Ende vernachlässigt die Formeln auch in die Formelsammlung zu kopieren
* richtiges Parsing: Pandoc ist zwar prinzipiell gut geeignet um Markdown zu Latex oder PDF zu parsen, aber er parst die Latex-Formeln falsch
	* Metadaten: Ich weiß, dass man mit Yaml Metadaten für Pandoc angeben kann, aber bislang wollte Pandoc danach nie richtig parsen. Vielleicht möchte sich jemand damit herumspielen.