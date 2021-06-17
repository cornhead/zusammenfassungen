
title: "**Zusammenfassung: Relativitätstheorie -- allgemeinveständlich**"
...


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

Gravitationsgesetz erklärt sowohl die Umlaufbahn des Mondes, als auch das Fallen von Äpfeln auf berühmte Wissenschaftler $\rightarrow$ die gleichen Gesetze gelten für ganz große und ganz kleine Objekte (Griechen dachten noch, dass für Planeten eigene Gesetze gelten würden). Mit Gravitationsgesetz ließen sich auch Kometenbahnen verstehen lassen, die zuvor unerklärlich waren.

Wurfgesetz:

* Abstand zum Erdboden $y$; Erdradius $R$; $y \ll R$; Erdmasse $M$
* Dann lässt sich Berechnung der Gravitationskraft vereinfachen zu
* $|f_g| = G \frac{M \cdot m}{R^2} = m \cdot g$ mit  Erdbeschleunigung $g = \frac{G \cdot M}{R^2} \approx 9.81m/s^2$

Beobachtung: Setzt man Das Gravitationsgesetz in das Kraftgesetz ein ergibt sich
$m \cdot x"^i(t) = - G \frac{M \cdot m}{r^3} x^i$ wobei sich $m$ herauskürzt.
Die Bewegung zur Folge der Gravitaionskraft ist nicht von der Masse des Objekts abhängig.
$\Rightarrow$ ist die Gravitationskraft überhaupt eine Kraft?

## Leibniz

(hat zeitglich mit Newton Infinitesimalrechnung entwickelt)

Für Leibniz war es unbefriedigend, dass sich durch Newtons Gravitationsgesetzt die Gezeiten dadurch erklären ließen, dass die Gravitation "durch die Erde durchgreift". Leibnizens Ansicht nach sollten sich physikalische Phänomene durch Wirkungen aus der unmittelbaren Umgebung erklären lassen, die sich dann womöglich fortpflanzen.



# Elektrizität und Magnetismus

Elektrische Kraft:

* Materie verfügt über die Eigenschaft Ladung $q$.
* $F^i_{coul.}(x^m) = \frac{1}{4\pi \epsilon_0} \cdot \frac{Q\cdot q}{r^3} x^i$

Setzt man Coulomb'sches Gesetz in Newton'sche Bewegungsgleichung ein, kürzt sich die Masse nicht heraus, da ja die Masse eines Objekts und seine Ladung unabhängig gewählt werden können.


Magnetisches Kraftgesetz:

* $F^i_{amp.}(x^m) = \frac{\mu_0}{4\pi} \cdot E_{i,j,k} I$ // todo: vervollständigen
* $(v \times w)^i = E_{i,j,k} v^j w^k$ (Kreuzprodukt)

$E_{i,j,k}$ ist eine trilineare Funktion (linear in allen Argumenten) und total antisymmetrisch (egal welche Argumente man tauscht, das Vorzeichen ändert sich)

$\underbrace{(E_{i,j,k} v^i w^j)}_{(v\times w)} u^k \in \mathbb{R}$

$E_{x,y,z} = E_{1,2,3} = E_{i,j,k} e^i_x e^j_y e^k_z = 1$

## Maxwell'sche Gleichungen

1866

verbinden elektrische und magnetische Kräfte in einer Theorie $\rightarrow$ Elektromagnetismus

wichtige Erkenntnis: Licht ist eine elektromagnetische Welle (anscheinend)

* $E^i = \lim_{q_1\rightarrow 0} F^i_{coul.} / q_1$ ... elektrisches Feld
* $B^i$ ... magnetisches Feld


* $\partial_i E^i(x^m, t) = \frac{1}{\epsilon_0}\rho(x^m, t)$ ... Gauß-Gesetz
* $E_{i,j,k} \partial_j E^k(x^m, t) + \dot{B}^i(x^m, t) = 0$ ... Faraday
* // todo: ergänzen

* $\rho$ ... Ladungsdichte
* $J$ ... Stromdichte
* $\partial_i f(x^m) = \frac{\partial f}{\partial x^i} (x^m)$

Transportintegral: Wie viel Material wird entlang einer bestimmten Kurve geschoben

Flächenintegral: Wie viel Material wird durch eine bestimmte Fläche geschoben

Divergenz-Operator $\partial_i$ gibt an, wie viel Material in einen (kleinen) Volumswürfel hineinfließt oder aus ihm hinausfließt. Dass der Divergenzoperator des magnetischen Feldes überall null ergibt, bedeutet, dass es keine Quellen oder Senken gibt.
