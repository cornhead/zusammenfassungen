---
title: "**Zusammenfassung: Relativitätstheorie -- allgemeinveständlich**"
...

---

An dieser Zusammenfassung und der zugehörigen Formelsammlung kann gerne auf [Github](https://github.com/cornhead/zusammenfassungen.git) mitgewirkt werden!

---

* Spezielle Relativitätstheorie: 1905
* Allgemeine Relativitätstheorie: 1915
* Kernaussage: Es gibt weder die eine Zeite, die für alle gleich ist, noch den einen Raum, der für alle gleich ist.

## Galilei
Galileo Galilei; ~16. Jhd ([Wikipedia](https://de.wikipedia.org/wiki/Galileo_Galilei))

Griechen hatten bereits in der Antike fantastisches Wissen über die Statik von Objekten, aber nicht über deren Dynamik, vermutlich weil dafür die Methoden der Zeitmessung noch nicht forgeschritten Genug waren. Galileo weiß, dass Pendel sehr gleichmäßig schwingen und kann daher die Dynamik von Gegenständen besser untersuchen.



* Ptolemei'sches Weltbild (geozentrisch) $\rightarrow$ Platenbahnen beschreiben "Schlaufen" // Skizze einfügen
* Kopernikanisches Weltbild (heliozentrisch) $\rightarrow$ Planetenbahnen beschreiben Kreise
* Kepplersches Weltbild $\rightarrow$ Planetenbahnen beschreiben Ellipsen

wichtiges Kepplersches Gesetz: in gleicher Zeit überstreichen Planeten gleiche Flächen (heute bekannt als Drehimpulserhaltung)



Galileo beschreibt folgendes Gedankenexperiment: Man befindet sich in einem Schiffsrumpf ohne fenster. Im Raum sind außerdem ein paar Fliegen, ein Goldfischglas und eine aufgehängte Flasche, aus der Wasser in eine Schüssel tropft. Wenn das Schiff im Hafen steht, dann fliegen die Fliegen in alle Richtungen gleich mühelos, genauso wie der Goldfisch in alle Richtungen gleich schnell schwimmen kann und die Tropfen einfach in die Schüssel fallen. Und auch wenn das Schiff nun ausgelaufen ist und sich mit gleichbleibender Geschwindigkeit fortbewegt, werden Fliegen Richtung Bug und Richtung Heck gleich schnell fliegen können, genau wie der Fisch in alle Richtung gleich schnell schwimmen kann, und die Tropfen fallen nicht neben die Schüssel, sondern immer noch in sie hinein. Tatsächlich kann man ohne Fenster gar nicht sagen, ob das Schiff steht oder ob es sich gleichförmig geradlinig fortbewegt $\rightarrow$ Relativitätsprinzip

Galileo stellt fest, dass Kräft nicht direkt die Geschwindigkeit von Objekten beeinflusst, sondern deren Beschleunigung $\rightarrow$ geradlinig gleichförmige Bewegungen sind "Grundbewegungen"

Galileo entwickelt Fallgesetze: Holzkugel und Bleikugel fallen in gleicher Zeit von Schiefem Turm von Pisa.

Tatsächlich ist sich Galileo im Grunde wichtiger Konzepte bewusst, die heute als Newton'sche Axiome bekannt sind, bloß hat er sie nicht mathematisch beschrieben.

## Newton
Isaac Newton; ~17. Jhd ([Wikipedia](https://de.wikipedia.org/wiki/Isaac_Newton))

hebt Galileis Erkenntnisse auf mathematische Ebene

### 2. Newtonsches Axiom

* $m \cdot x"^i(t) = F^i(x^m(t))$
* also "Kraft ist Masse mal Beschleunigung"
* Sinn dahinter: bei gegebener Anfangsposition und Anfangsgeschwindigkeit kann Trajektorie eines Körpers aus seiner Kraft hergeleitet werden $\rightarrow$ lösen einer ODE zweiten Grades

// einfügen: Herleitung von x' und x" aus gegebener Trajektorie

Geschwindigkeit ist Ortsänderung, Beschleunigung ist Geschwindigkeitsänderung

Setzt man $F^i(x^m)=0^i$, folgt $m \cdot x"î(t) = 0$. Für $m \neq 0$ folgt dann eine gerade, gleichförmige Bewegung $\rightarrow$ 1. Newtonsches Axiom

### Newtonsches Gravitations-Gesetz

$F_{grav}^i(x^m) = - G \frac{M \cdot m}{r^3} x^i = - G \frac{M \cdot m}{r^2} e_r^i$

Gravitationsgesetz erklärt sowohl die Umlaufbahn des Mondes, als auch das Fallen von Äpfeln auf berühmte Wissenschaftler $\rightarrow$ die gleichen Gesetze gelten für ganz große und ganz kleine Objekte (Griechen dachten noch, dass für Planeten eigene Gesetze gelten würden)

Wurfgesetz:

* Abstand zum Erdboden $y$; Erdradius $R$; $y \ll R$; Erdmasse $M$
* Dann lässt sich Berechnung der Gravitationskraft vereinfachen zu
* $|f_g| = G \frac{M \cdot m}{R^2} = m \cdot g$ mit  Erdbeschleunigung $g = \frac{G \cdot M}{R^2} \approx 9.81m/s^2$

Beobachtung: Setzt man Das Gravitationsgesetz in das Kraftgesetz ein ergibt sich
$m \cdot x"^i(t) = - G \frac{M \cdot m}{r^3} x^i$ wobei sich $m$ herauskürzt.
Die Bewegung zur Folge der Gravitaionskraft ist nicht von der Masse des Objekts abhängig.
$\Rightarrow$ ist die Gravitationskraft überhaupt eine Kraft?
