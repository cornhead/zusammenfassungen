
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

* $m \cdot \ddot{x}^i(t) = F^i(x^m(t))$
* also "Kraft ist Masse mal Beschleunigung"
* Sinn dahinter: bei gegebener Anfangsposition und Anfangsgeschwindigkeit kann Trajektorie eines Körpers aus seiner Kraft hergeleitet werden $\rightarrow$ lösen einer ODE zweiten Grades

// einfügen: Herleitung von $\dot{x}$ und $\ddot{x}$ aus gegebener Trajektorie

Geschwindigkeit ist Ortsänderung, Beschleunigung ist Geschwindigkeitsänderung

Setzt man $F^i(x^m)=0^i$, folgt $m \cdot \ddot{x}^i(t) = 0$. Für $m \neq 0$ folgt dann eine gerade, gleichförmige Bewegung $\rightarrow$ 1. Newtonsches Axiom

### Newtonsches Gravitations-Gesetz

$F_{grav}^i(x^m) = - G \frac{M \cdot m}{r^3} x^i = - G \frac{M \cdot m}{r^2} e_r^i$

Gravitationsgesetz erklärt sowohl die Umlaufbahn des Mondes, als auch das Fallen von Äpfeln auf berühmte Wissenschaftler $\rightarrow$ die gleichen Gesetze gelten für ganz große und ganz kleine Objekte (Griechen dachten noch, dass für Planeten eigene Gesetze gelten würden). Mit Gravitationsgesetz ließen sich auch Kometenbahnen verstehen lassen, die zuvor unerklärlich waren.

Wurfgesetz:

* Abstand zum Erdboden $y$; Erdradius $R$; $y \ll R$; Erdmasse $M$
* Dann lässt sich Berechnung der Gravitationskraft vereinfachen zu
* $|f_g| = G \frac{M \cdot m}{R^2} = m \cdot g$ mit  Erdbeschleunigung $g = \frac{G \cdot M}{R^2} \approx 9.81m/s^2$

Beobachtung: Setzt man Das Gravitationsgesetz in das Kraftgesetz ein ergibt sich
$m \cdot \ddot{x}^i(t) = - G \frac{M \cdot m}{r^3} x^i$ wobei sich $m$ herauskürzt.
Die Bewegung zur Folge der Gravitaionskraft ist nicht von der Masse des Objekts abhängig.
$\Rightarrow$ ist die Gravitationskraft überhaupt eine Kraft?

## Leibniz

(hat zeitglich mit Newton Infinitesimalrechnung entwickelt)

Für Leibniz war es unbefriedigend, dass sich durch Newtons Gravitationsgesetzt die Gezeiten dadurch erklären ließen, dass die Gravitation "durch die Erde durchgreift". Leibnizens Ansicht nach sollten sich physikalische Phänomene durch Wirkungen aus der unmittelbaren Umgebung erklären lassen, die sich dann womöglich fortpflanzen.



# Elektromagnetismus

## Elektrisches und Magnetisches Feld

Elektrische Kraft (zwischen zwei Ladungen):

* Materie verfügt über die Eigenschaft Ladung $q$.
* $F^i_{coul.}(x^m) = \frac{1}{4\pi \epsilon_0} \cdot \frac{Q\cdot q}{r^3} x^i$

Setzt man Coulomb'sches Gesetz in Newton'sche Bewegungsgleichung ein, kürzt sich die Masse nicht heraus, da ja die Masse eines Objekts und seine Ladung unabhängig gewählt werden können.

Strukturmäßig sieht die Coulomb'sche Kraft sehr so aus wie die Gravitationskraft. Es hat eine Zeit lang die Ansicht geherrscht, dass diese Art "gut" ist, um Kräfte zu beschreiben, und war bemüht alle Kräfte in eine ähnliche Form zu bringen.


Magnetische Kraft (zwischen zwei Strömen):

* $F^i_{amp.}(x^m) = \frac{\mu_0}{4\pi} \cdot \E_{i,j,k} I_1 {x'}_1^j(s_1) \E_{k,l,m} I_2 {x'}_2^l(s_2) \cdot \frac{x_1^m(s_1)-x_2^m(s_2)}{\left| x_1^m(s_1)-x_2^m(s_2) \right| ^3} \left(x_1(s_1) - x_2(s_2) \right)$ // todo: vervollständigen
* $(v \times w)^i = \E_{i,j,k} v^j w^k$ (Kreuzprodukt)

wobei $I_n x'_n(s_n)$ den Strom repräsentiert. Dabei ist $I_n$ die Stromstärke und $x'_n(s_n)$ die Bewegungsrichtung (Ableitung der Position) parametriert über die Bogenlänge.

Wenn man die Epsilon-Operatoren durch Kreuzprodukte ausdrückt (siehe unten), sieht man, dass auch die Ampere'sche Kraft die Form der Gravitationskraft hat, bloß mit Kreuzprodukten, um Richtungen der Ströme richtig einzubeziehen.


Der Operator $\E_{i,j,k}$ heißt Epsilon-Tensor. Im Folgenden seien seine wichtigsten Eigenschaften kurz umrissen:

* seien $v$ und $w$: Vektoren (z.b. aus $\mathbb{R}^3$)
* Delta-Tensor (für inneres Produkt): $\delta(v, w) = \delta_{ij} v^i w^j = v^i w^i = v \cdot w = v^1 w^1 + v^2 w^2 + v^3 w^3 \cdots$
	* bilinear
	* symmetrisch
* Epsilon-Tensor (für Kreuzprodukt): $\E_{i,j,k}v^j w^k = (v \times w)^i$
	* trilinear: linear in allen drei Argumenten
	* total antisymmetrisch: egal welche zwei Argumente man vertauscht, das Vorzeichen ändert sich
	* $\E_{i,j,k}$ergibt $0$, wenn zwei Indizes gleich sind
	* $\E_{x,y,z} = \E_{1,2,3} = \E_{i,j,k} e^i_x e^j_y e^k_z = 1$

## Inhomogene Maxwell-Gleichungen

1866

Erkenntnis: Strom ist Bewegung von Ladung. Zusammenhang zwischen elektrischer und magnetischer Kraft? $\rightarrow$ Elektromagnetismus

Definitionen:

* $E^i = \lim \limits_{q_1\rightarrow 0} \frac{F^i_{coul.}}{q_1}$ ... elektrisches Feld
* $B^i = \frac{F^i_{amp.}}{I_1 {x'}_1^i(s_i)}$ ... magnetisches Feld

Die Stärke eines Feldes gibt die mögliche Kraft auf eine sehr kleine Testladung/Testsrom an, relativ zur stärke dieser Ladung/Strom. Damit ist eine Beschreibung durch Felder etwas abstrakter als eine Beschreibung durch Kräfte.

Maxwell-Gleichungen:

#. $\partial_i E^i(x^m, t) = \frac{1}{\epsilon_0}\rho(x^m, t)$ ... Gauß-Gesetz
#. $\E_{i,j,k} \partial_j E^k(x^m, t) + \dot{B}^i(x^m, t) = 0$ ... Faraday-Gesetz
#. $\partial_i B^i(x^m, t) = 0$
#. $\E_{i,j,k} \partial_j B^k(x^m, t) - \mu_0 \epsilon_0 \dot{E^i}(x^m, t) = \mu_0 J^i(x^m, t)$ ... Ampere-Maxwell-Gesetz

mit

* $\rho$ ... Ladungsdichte, Ladung pro Volumseinheit
* $J^i$ ... Stromdichte, Strom pro Volumseinheit
* $\partial_i f(x^m) = \frac{\partial f}{\partial x^i} (x^m)$

Die Operatoren $\partial_i$ und $\E_{i,j,k}\partial_j$ werden in den folgenden Unterpunkten erläutert. (siehe [Fluss durch kleinen Würfel](#fdkw) für ersteren Operator und [Transportintegral entlang Rand eines kleinen Quadrates](#trkq) für zweiteren)

Das Gauß-Gesetz und das Faraday-Gesetz werden "elektrische Gesetze" genannt. Die verbleibenden beiden sind die "magnetischen Gesetze".

Die Maxwell-Gleichungen stellen ein System linearer Differentialgleichungen ersten Grades dar, wobei die Differentialgleichungen inhomogen sind. Sie werden daher auch *inhomogenen* Maxwell-Gleichungen genannt, im Gegesatz zu den *homogenen*, die weiter unten besprochen werden.

Interpretation der Maxwell-Gleichungen:

#. Die Divergenz des elektrischen Feldes ist proportional zur Ladungsdichte $\rightarrow$ Ladung erzeugt das elektrische Feld
#. Eine Divergenz im elektrischen Feld bewirkt eine "entgegengesetzte" verwirbelung des magnetischen Feldes und andersherum $\rightarrow$ Induktion
#. Die Divergenz des magnetischen Feldes ist immer null $\rightarrow$ Das Magnetfeld hat keine Quellen und Senken
#. Strom erzeugt einen Wirbel im magnetischen Feld

Divergenz-Operator $\partial_i$ gibt an, wie viel Material in einen (kleinen) Volumswürfel hineinfließt oder aus ihm hinausfließt. Dass der Divergenzoperator des magnetischen Feldes überall null ergibt, bedeutet, dass es keine Quellen oder Senken gibt.

## Transportintegral

Wie viel Material wird entlang einer bestimmten Kurve geschoben?

$v^i(x^m)$ ... Vektorfeld (entspricht Strömung)

$\Gamma(v^i, \gamma) = \int \limits_\gamma v^i(x^m)dx^i = \int\limits_{\lambda_0}^{\lambda_1} d\lambda v^i(x^m(\lambda))x'^i(\lambda)$

$\Gamma(v^i, \gamma)$ ... Transportintegral eines Feldes $v^i(x^m)$ entlang einer Kurve $\gamma$ (, die nach $\lambda$ parametriert werden kann)

## Flächenintegral

Wie viel Material wird durch eine bestimmte Fläche geschoben?

$Fl(v^i, F) = \int\limits_F d^1 f^i v^i$

$d^2 f^i = dAn^2$ ... Normalvektor auf Fläche $f$ mit Länge $1$

## Fluss durch einen kleinen Würfel, relativ zu Volumen {#fdkw}

An stelle $x^m$ befindet sich der Mittelpunkt eines Würfels mit Kantenlänge $\epsilon$, der genau entlang der Koordinatenachsen ausgerichtet ist. $W_{x, \epsilon}$ bezeichnet Würfel, $\partial W_{x, \epsilon}$ bezeichnet nur seine Oberfläche/Rand$

$\lim \limits_{\epsilon \rightarrow 0} \frac{1}{Vol(W_{x, \epsilon})} \int \limits_{W_{x, \epsilon}} d^2 f^i v^i$

$=\lim \limits_{\epsilon \rightarrow 0} \frac{1}{\epsilon^3} \left( \begin{array}{l} \pm e_z^i v^i(x^m\pm \frac{\epsilon}{2} e_z^m) \epsilon^2 \\  \pm e_y^i v^i(x^m\pm \frac{\epsilon}{2} e_y^m) \epsilon^2 \\  \pm e_x^i v^i(x^m\pm \frac{\epsilon}{2} e_x^m) \epsilon^2 \end{array}\right)$

$= \lim \limits_{\epsilon \rightarrow 0} \frac{1}{\epsilon}$ // vervollständigen

$= \partial_i v^i(x^m)$

$= \div v^i(x^m)$ ... Divergenz / Quellendichte von $v^i(x^m)$

## Transportintegral entlang des Randes eines kleinen Quadrates {#trkq}

Quadrat $Q_{x, \epsilon}$ und dessen Rand $\partial Q_{x, \epsilon}$

$\lim \limits_{\epsilon \rightarrow 0} \frac{1}{Ar(W_{x, \epsilon})} \int \limits_{\partial Q_{x, \epsilon}} v^i dx^i$

$= \lim \limits_{\epsilon \rightarrow 0} \frac{1}{\epsilon^2}  \cdot \left( \begin{array}{l} \pm e_y^i v^i (x^m \pm \frac{\epsilon}{2} e_x^m) \\ \mp e_x^i v^i (x^m \pm \frac{\epsilon}{2} e_y^m) \end{array}\right)$

$= \lim \limits_{\epsilon \rightarrow 0} \frac{1}{\epsilon^2} \cdot \left( \begin{array}{l} \pm v^y +{}+ \frac{\epsilon}{2} \partial_x v^y(x^m) + \mathcal{O}(\epsilon^2) \\ \mp v^x -{}- \frac{\epsilon}{2} \partial_y v^x(x^m) + \mathcal{O}(\epsilon^2) \end{array}\right)$

$= \partial_x v^y(x^m) - \partial_y v^x(x^m)$

$= e_z^i \E_{i,j,k} \partial_j v^k(x^m)$

$= \rot v^i(x^m)$ ... Rotor von $v^i(x^m)$

Wenn man das Quadrat auf einen Punkt schrumpft, bleibt nicht nur ebendieser Punkt über, sondern auch die Flachennormale, die gewissermaßen die ursprüngliche Orientierung des Quadrates repräsentiert.

## Ladungserhaltung

Durch intuitives Verständnis der Operatoren lassen sich die Maxwell-Gleichungen nun besser greifbar Machen: // vervollständigen

Zwei der Maxwell-Gleichungen sind besonders interessant, denn ihre rechte Seite ist ungleich 0. Leiten wir (1) nach der Zeit ab und wenden auf (4) den Divergenzoperator an:

* ad (1): $\partial_i \dot{E}^i(x^m, t) = \frac{1}{\epsilon_0} \dot{\rho}(x^m, t)$
* ad (4): $\E_{i,j,k} \partial_i \partial_j B^k(x^m, t) - \mu_0 \epsilon_0 \partial_i \dot{E}^i(x^m, t) = \mu_0 \partial_i J^i(x^m, t)$

Weiters multiplizieren wir (1) mit $\epsilon_0$ und dividieren (4) durch $\mu_0$:

* ad (1): $\epsilon_0 \partial_i \dot{E}^i(x^m, t) = \dot{\rho}(x^m, t)$
* ad (4): $\frac{1}{\mu_0} \E_{i,j,k} \partial_i \partial_j B^k(x^m, t) - \epsilon_0 \partial_i \dot{E}^i(x^m, t) = \partial_i J^i(x^m, t)$

Durch Addition der so erhaltenen Gleichungen folgt

$\frac{1}{\mu_0} \E_{i,j,k} \partial_i \partial_j B^k = \dot{\rho} + \partial_i J^i(x^m, t)$

Über die Eigenschaften des Epsilon- und des Delta-Tensors ergibt sich, dass die linke Seite dieser Gleichung gleich sein muss ihrer Negation. Daraus folgt, dass die linke Seite 0 sein muss. Also:

$\dot{\rho} + \partial_i J^i = 0$ ... Ladungserhaltung

$\Rightarrow$ Ladungserhaltung ist eine direkte Konsequenz der Maxwell-gleichungen. Ladungsdichte kann sich also nur durch Zu- oder Abfluss von Strom ändern.

## Homogene Maxwell-Gleichungen

In Vakuum gilt $\rho = J^i = 0$. Setzt man diese Werte in die inhomogenen Maxwell-Gleichungen ein, ergebn sich die Vakuum-Maxwell-Gleichungen.

#. $\partial_i E^i = 0$
#. $\E_{i,j,k} \partial_j E^k + \dot{B}^i = 0$
#. $\partial_i B^i = 0$
#. $\E_{i,j,k} \partial_j B^k - \mu_0 \epsilon_0 \dot{E}^i = 0$

Es fällt auf, dass alle rechten Seiten dieser gleichungen 0 sind. Somit stellen sie gewöhnliche lineare Differentialgleichungen ersten Grades dar, die zudem homogen sind. Die gleichungen werden daher auch als Homogene Maxwell-Gleichungen bezeichnet.

## Licht

Die homogenen Maxwell-Gleichungen nehmen für die elektrischen und die magnetischen Gleichungen sehr Ähnliche Formen an. Man sieht daher schnell, dass $B^i = E^i = 0$ eine triviale Lösung des Gleichungssystems ist, doch eine große Erkenntnis von Maxwell ist, dass dies nicht die einzige Lösung ist.

Um das zu sehen, entkoppeln wir zuerst die Gleichungen. Hierzu Bilden wir zunächst die zeitliche Ableitung von (2)

$\E_{i,j,k} \partial_j \dot{E}^k + \ddot{B}^i = 0$

Der erste Term dieser Gleichung lässt sich aber auch leicht durch (4) ausdrücken. Man erhält dann

$\frac{1}{\mu_0 \epsilon_0} \E_{i,j,k} \partial_j \left(  \E_{k,l,m} \partial_l B^m \right) + \ddot{B}^i = 0$

was sich umstellen lässt zu 

$\ddot{B}^i + \frac{1}{\mu_0 \epsilon_0} \underbrace{\E_{i,j,k}\E_{k,l,m}}_{\delta_{lm}^{ij}} \partial_j \partial_l B^m = 0$

$\ddot{B}^i - \frac{1}{\mu_0 \epsilon_0} \partial^2 B^i = 0$ ... Wellengleichung

Die gleiche Wellengleichug ließe sich auch für $E^i$ herleiten. In dieser Gleichung beschreibt $\frac{1}{\mu_0 \epsilon_0}$ das Quadrat einer Ausbreitungsgeschwindigkeit. Es zeigt sich, dass $\frac{1}{\mu_0 \epsilon_0} = c^2$ mit $c \approx 3 \cdot 10^8$ m/s. Damit wurde Maxwell klar, dass Licht kein eigenständiges Phänomen ist, sondern lediglich eine elektromagnetische Welle.

Das Ausbreitungsmedium von elektromagnetischen Wellen sind also gewissermaßen das elektrische und magnetische Feld. Zuvor nahm man als Ausbreitungsmedium von Licht den sogenannten Lichtether an. Es stellte sich nun die Frage, mit welcher Geschwindigkeit wir uns gegenüber dem Lichtether bewegen. Um diese Frage zu klären wurde folgendes Experiment durchgeführt: man messe die Ausbreitungsgeschwindigkeit von Licht in unterschiedliche Richtungen. Da man sich vermutlich gegenüber dem Ether bewegt, müsste man einen Unterschied der Ausbreitungsgeschwindkeiten in die unterschiedlichen Richtungen messen. Doch bei der Durchführung war dies nicht der Fall. Nun wäre es natürlich denkbar, dass man sich in diesem Moment genau in Ruhe gegenüber dem Ether befand. Man wartete also ein halbes Jahr und führte das Experiment erneut durch. Da sich die Erde dann ja in die genau entgegengesetzte Richtung bewegt, hätte man zumindest dann einen Unterschied feststellen können müssen; doch wieder nichts.

Wie erklärt man nun dieses Phänomen? Dem Ether wurden zunehmend mehr Eigenschaften zugesprochen, die -- wie Einstein bemerkte -- nur den Zweck hatten, den Ether unbeobachtbar zu machen, was zutiefst unwissenschaftlich ist. Andere Folgerungen aus diesen Messungen könnten sein, dass entweder das Relativitätsprinzip nicht immer gilt, oder dass die Maxwell-Gleichungen falsch sind. Beides würde die Physik in gleich schwere Krisen werfen. Einstein schlägt nun in seiner **speziellen Relativitätstheorie** (1905) einen dritten Weg vor, der nicht verlangt, dass eines dieser etablierten Konzepte aufgegeben werden muss: Er stellt fest, dass die Zeit für unterschiedliche Beobachter nicht unbedingt gleich verlaufen muss.

## Raumzeit

Minkowski, 1908

* Gleichzeit-Ebenen
* Weltlinien
* Gleichgeschwindigkeitskegel
	* Lichtkegel (wenn die ebenen $c\cdot t$ auseinander sind ist der Öffnungswinkel 45°)
	
nvarianz des Lichtkegels: konstruktion des kegels muss für alle bezugssysteme gleich sein -> bei geneigten weltlinien eines beobachters kippen auch gleichzeitigkeitsebenen -> zeitliche reihenfolge von ereignissen kann von beobachter abhängen, gleiches objekt wirkt als hätte es unterschiedliche längen je nachdem wer es beobachtet

minkowski metrik -> lichtartige, raumartige und zeitartige vektoren
