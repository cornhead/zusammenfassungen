---
summary-type: zusammenfassung
title: "**Zusammenfassung: Relativitätstheorie -- allgemeinveständlich**"
...



# Von Statik zu Dynamik

## Galileo
Galileo Galilei; ~16. Jhd ([Wikipedia](https://de.wikipedia.org/wiki/Galileo_Galilei))

Die Griechen hatten bereits in der Antike umfassendes Wissen über die Statik von Objekten, aber nicht über deren Dynamik -- vermutlich weil dafür die Methoden der Zeitmessung noch nicht forgeschritten genug waren. Galileo jedoch wusste, dass Pendel sehr gleichmäßig schwingen und daher zur Zeitmessung verwendet werden können, und konnte daher die Dynamik von Gegenständen besser untersuchen.

* Ptolemei'sches Weltbild (geozentrisch) &rarr; Platenbahnen beschreiben "Schlaufen"
* Kopernikanisches Weltbild (heliozentrisch) &rarr; Planetenbahnen beschreiben Kreise
* Kepplersches Weltbild &rarr; Planetenbahnen beschreiben Ellipsen

:::comment TODO
	Bilder einfügen um Weltbilder zu illustrieren
:::

wichtiges Kepplersches Gesetz: in gleicher Zeit überstreichen Planeten gleiche Flächen (heute bekannt als Drehimpulserhaltung)

Galileo beschreibt folgendes Gedankenexperiment: Man befindet sich in einem Schiffsrumpf ohne Fenster. Im Raum sind außerdem ein paar Fliegen, ein Goldfischglas und eine aufgehängte Flasche, aus der Wasser in eine Schüssel tropft. Wenn das Schiff im Hafen steht, dann fliegen die Fliegen in alle Richtungen gleich mühelos, genauso wie der Goldfisch in alle Richtungen gleich schnell schwimmen kann und die Tropfen einfach in die Schüssel fallen. Und auch wenn das Schiff nun ausgelaufen ist und sich mit gleichbleibender Geschwindigkeit fortbewegt, werden Fliegen Richtung Bug und Richtung Heck gleich schnell fliegen können, genau wie der Fisch in alle Richtung gleich schnell schwimmen kann, und die Tropfen fallen nicht neben die Schüssel, sondern immer noch in sie hinein. Tatsächlich kann man ohne Fenster gar nicht feststellen, ob das Schiff steht oder ob es sich gleichförmig geradlinig fortbewegt &rarr; Dass die Gesetze der Physik für ruhende und für gleichmäßig geradlinig bewegte Bezugssysteme in unveränderter Weise gelten, nennt sich **Relativitätsprinzip**.

Galileo stellt fest, dass Kräfte nicht direkt die Geschwindigkeit von Objekten beeinflussen, sondern deren Beschleunigung $\rightarrow$ geradlinig gleichförmige Bewegungen sind "Grundbewegungen", d.h., wenn auf ein Objekt keine Kraft wirkt, bewegt es sich mit gleichbleibender Geschwindigkeit in dieselbe Richtung weiter. Die alten Griechen hätten noch angenommen, dass ein Objekt ohne Einwirken von Kraft einfach stehenbleibt.

Galileo entwickelt Fallgesetze: Eine Holzkugel und Bleikugel fallen brauchen die gleiche Zeit, um vom Schiefem Turm von Pisa zu fallen, obwohl man doch annehmen würde, dass schwerere Objekte schneller fallen sollten.

Tatsächlich ist sich Galileo im Grunde wichtiger Konzepte bewusst, die heute als Newton'sche Axiome bekannt sind, bloß konnte er sie nicht mathematisch beschreiben. (Dafür wären mathematische Werkzeuge nötig gewesen, die erst später für genau diesen Zweck entwickelt wurden &rarr; Infinitesimalrechnung, Differentialgleichungen, Analysis, \dots)


## Newton
Isaac Newton; ~17. Jhd ([Wikipedia](https://de.wikipedia.org/wiki/Isaac_Newton))

hebt Galileis Erkenntnisse auf mathematische Ebene

### 2. Newtonsches Axiom

* $m \cdot \ddot{x}^i(t) = F^i(x^m(t))$
* also "Kraft ist Masse mal Beschleunigung"
* Sinn dahinter: bei gegebener Anfangsposition und Anfangsgeschwindigkeit kann Trajektorie eines Körpers aus seiner Kraft hergeleitet werden &rarr; mathematisch entspricht das der Lösung einer ODE (ordinary differential equation) zweiten Grades, kann aber auch graphisch sehr schön veranschaulicht werden.

:::comment TODO
	hier bild einfügen, wie man graphisch die Trajektorie eines geworfenen Balles unter Einfluss der Schwerkraft herleitet.
:::

Geschwindigkeit ist Ortsänderung, Beschleunigung ist Geschwindigkeitsänderung

Setzt man $F^i(x^m)=0^i$, folgt $m \cdot \ddot{x}^i(t) = 0$. Für $m \neq 0$ folgt dann eine gerade, gleichförmige Bewegung. Dieser Sonderfall entspricht dem 1. Newtonsches Axiom.

### Newtonsches Gravitations-Gesetz

:::theorem Newton'sches Gravitationsgesetz
	$F_{grav}^i(x^m) = - G \frac{M \cdot m}{r^3} x^i = - G \frac{M \cdot m}{r^2} e_r^i$
:::

Das Gravitationsgesetz erklärt sowohl die Umlaufbahn des Mondes, als auch das Fallen von Äpfeln auf berühmte Wissenschaftler &rarr; Die gleichen Gesetze gelten für ganz große und ganz kleine Objekte. (Die Griechen dachten noch, dass für Planeten eigene Gesetze gelten müssten). Mit dem Gravitationsgesetz lassen sich auch Kometenbahnen verstehen lassen, die zuvor unerklärlich waren. (Roger Penrose stuft dieses Gesetz als superb ein, auch wenn es -- wie wir sehen werden -- nicht ganz akkurat ist.)

Wurfgesetz:

* Abstand zum Erdboden $y$; Erdradius $R$; $y \ll R$; Erdmasse $M$
* Dann lässt sich Berechnung der Gravitationskraft vereinfachen zu
* $|f_g| = G \frac{M \cdot m}{R^2} = m \cdot g$ mit  Erdbeschleunigung $g = \frac{G \cdot M}{R^2} \approx 9.81m/s^2$

:::note
	Setzt man das Gravitationsgesetz in das Kraftgesetz ein ergibt sich $$m \cdot \ddot{x}^i(t) = - G \frac{M \cdot m}{r^3} x^i$$ wobei sich $m$ wegkürzen lässt.
	
	Die Bewegung zur Folge der Gravitaionskraft ist nicht von der Masse des Objekts abhängig. $\Rightarrow$ ist die Gravitationskraft überhaupt eine Kraft?
:::

## Leibniz

(hat zeitglich mit Newton Infinitesimalrechnung entwickelt)

Für Leibniz war es unbefriedigend, dass sich durch Newtons Gravitationsgesetzt die Gezeiten dadurch erklären ließen, dass die Gravitation "durch die Erde durchgreift". Leibnizens Ansicht nach sollten sich physikalische Phänomene durch Wirkungen aus der unmittelbaren Umgebung erklären lassen, die sich dann womöglich fortpflanzen.



# Elektromagnetismus

## Elektrisches und Magnetisches Feld

:::theorem Coulomb'sches Gesetz (Elektrische Kraft zwischen zwei Ladungen)
	Materie verfügt über die Eigenschaft Ladung $q$.
	
	$F^i_{coul.}(x^m) = \frac{1}{4\pi \epsilon_0} \cdot \frac{Q\cdot q}{r^3} x^i$
:::

Setzt man Coulomb'sches Gesetz in Newton'sche Bewegungsgleichung ein, kürzt sich die Masse nicht heraus, da ja die Masse eines Objekts und seine Ladung unabhängig gewählt werden können.

Strukturell sieht die Coulomb'sche Kraft sehr so aus wie die Gravitationskraft. Es hat eine Zeit lang die Ansicht geherrscht, dass diese Struktur besonders "gut" oder "schön" ist, um Kräfte zu beschreiben, und man war daher bemüht, alle Kräfte in eine ähnliche Form zu bringen.


:::theorem Ampere'sches Gesetz (Magnetische Kraft zwischen zwei Strömen)
	
	$F^i_{amp.}(x^m) = \frac{\mu_0}{4\pi} \cdot \E_{i,j,k} I_1 {x'}_1^j(s_1) \E_{k,l,m} I_2 {x'}_2^l(s_2) \cdot \frac{x_1^m(s_1)-x_2^m(s_2)}{\left| x_1^m(s_1)-x_2^m(s_2) \right| ^3} \left(x_1(s_1) - x_2(s_2) \right)$ // todo: vervollständigen
	
	$(v \times w)^i = \E_{i,j,k} v^j w^k$ (Kreuzprodukt)

	wobei $I_n x'_n(s_n)$ den Strom repräsentiert. Dabei ist $I_n$ die Stromstärke und $x'_n(s_n)$ die Bewegungsrichtung (Ableitung der Position) parametriert über die Bogenlänge.
:::

Wenn man die Epsilon-Operatoren durch Kreuzprodukte ausdrückt (siehe unten), sieht man, dass auch die Ampere'sche Kraft die Form der Gravitationskraft hat, bloß mit Kreuzprodukten, um die Richtungen der Ströme richtig einzubeziehen.

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

Erkenntnis: Strom ist Bewegung von Ladung. Zusammenhang zwischen elektrischer und magnetischer Kraft? &rarr; **Elektromagnetismus**

Definitionen:

* $E^i = \lim \limits_{q_1\rightarrow 0} \frac{F^i_{coul.}}{q_1}$ ... elektrisches Feld
* $B^i = \frac{F^i_{amp.}}{I_1 {x'}_1^i(s_i)}$ ... magnetisches Feld

Die Stärke eines Feldes gibt die mögliche Kraft auf eine sehr kleine Testladung/Testsrom an, relativ zur stärke dieser Ladung/Strom. Damit ist eine Beschreibung durch Felder etwas abstrakter als eine Beschreibung durch Kräfte.

:::theorem Maxwell-Gleichungen
	#. $\partial_i E^i(x^m, t) = \frac{1}{\epsilon_0}\rho(x^m, t)$ ... Gauß-Gesetz
	#. $\E_{i,j,k} \partial_j E^k(x^m, t) + \dot{B}^i(x^m, t) = 0$ ... Faraday-Gesetz
	#. $\partial_i B^i(x^m, t) = 0$
	#. $\E_{i,j,k} \partial_j B^k(x^m, t) - \mu_0 \epsilon_0 \dot{E^i}(x^m, t) = \mu_0 J^i(x^m, t)$ ... Ampere-Maxwell-Gesetz
	
	mit

	* $\rho$ ... Ladungsdichte, Ladung pro Volumseinheit
	* $J^i$ ... Stromdichte, Strom pro Volumseinheit
	* $\partial_i f(x^m) = \frac{\partial f}{\partial x^i} (x^m)$
:::

Die Operatoren $\partial_i$ und $\E_{i,j,k}\partial_j$ werden in den folgenden Unterpunkten erläutert. (siehe [Fluss durch kleinen Würfel](#fdkw) für ersteren Operator und [Transportintegral entlang Rand eines kleinen Quadrates](#trkq) für zweiteren)

Das Gauß-Gesetz und das Faraday-Gesetz werden "elektrische Gesetze" genannt. Die verbleibenden beiden sind die "magnetischen Gesetze".

Die Maxwell-Gleichungen stellen ein System linearer Differentialgleichungen ersten Grades dar, wobei die Differentialgleichungen inhomogen sind. Sie werden daher auch die *inhomogenen* Maxwell-Gleichungen genannt, im Gegesatz zu den *homogenen*, die weiter unten besprochen werden.

Interpretation der Maxwell-Gleichungen:

#. Die Divergenz des elektrischen Feldes ist proportional zur Ladungsdichte $\rightarrow$ Ladung erzeugt das elektrische Feld
#. Eine Divergenz im elektrischen Feld bewirkt eine "entgegengesetzte" verwirbelung des magnetischen Feldes und andersherum $\rightarrow$ Induktion
#. Die Divergenz des magnetischen Feldes ist immer null $\rightarrow$ Das Magnetfeld hat keine Quellen und Senken
#. Strom erzeugt einen Wirbel im magnetischen Feld, dabei muss nicht nur der Leitungsstrom $J^i$, sondern auch der Verschiebungsstrom $\mu_0 \epsilon_0 \dot{E^i}$ berücksichtigt werden.

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

An stelle $x^m$ befindet sich der Mittelpunkt eines Würfels mit Kantenlänge $\epsilon$, der genau entlang der Koordinatenachsen ausgerichtet ist. $W_{x, \epsilon}$ bezeichnet Würfel, $\partial W_{x, \epsilon}$ bezeichnet nur seine Oberfläche/Rand

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

Wenn man das Quadrat auf einen Punkt schrumpft, bleibt nicht nur ebendieser Punkt über, sondern auch die Flächennormale, die gewissermaßen die ursprüngliche Orientierung des Quadrates repräsentiert.

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

$\Rightarrow$ Ladungserhaltung ist eine direkte Konsequenz der Maxwell-Gleichungen. Ladungsdichte kann sich also nur durch Zu- oder Abfluss von Strom ändern.

## Homogene Maxwell-Gleichungen

In Vakuum gilt $\rho = J^i = 0$. Setzt man diese Werte in die inhomogenen Maxwell-Gleichungen ein, ergeben sich die Vakuum-Maxwell-Gleichungen.

:::theorem Homogene Maxwellgleichungen
	#. $\partial_i E^i = 0$
	#. $\E_{i,j,k} \partial_j E^k + \dot{B}^i = 0$
	#. $\partial_i B^i = 0$
	#. $\E_{i,j,k} \partial_j B^k - \mu_0 \epsilon_0 \dot{E}^i = 0$
:::

Es fällt auf, dass alle rechten Seiten dieser gleichungen 0 sind. Somit stellen sie gewöhnliche lineare Differentialgleichungen ersten Grades dar, die zudem homogen sind. Die gleichungen werden daher auch als *homogene* Maxwell-Gleichungen bezeichnet.

## Licht

Die homogenen Maxwell-Gleichungen nehmen für die elektrischen und die magnetischen Gleichungen sehr Ähnliche Formen an. Man sieht daher schnell, dass $B^i = E^i = 0$ eine triviale Lösung des Gleichungssystems ist, doch eine große Erkenntnis von Maxwell ist, dass dies nicht die einzige Lösung ist.

Um das zu sehen, entkoppeln wir zuerst die Gleichungen. Hierzu Bilden wir zunächst die zeitliche Ableitung von (2)

$\E_{i,j,k} \partial_j \dot{E}^k + \ddot{B}^i = 0$

Der erste Term dieser Gleichung lässt sich aber auch leicht durch (4) ausdrücken. Man erhält dann

$\frac{1}{\mu_0 \epsilon_0} \E_{i,j,k} \partial_j \left(  \E_{k,l,m} \partial_l B^m \right) + \ddot{B}^i = 0$

was sich umstellen lässt zu 

$\ddot{B}^i + \frac{1}{\mu_0 \epsilon_0} \underbrace{\E_{i,j,k}\E_{k,l,m}}_{\delta_{lm}^{ij}} \partial_j \partial_l B^m = 0$

$\ddot{B}^i - \frac{1}{\mu_0 \epsilon_0} \partial^2 B^i = 0$ ... Wellengleichung

Dieselbe Wellengleichug ließe sich auch für $E^i$ herleiten. In dieser Gleichung beschreibt $\frac{1}{\mu_0 \epsilon_0}$ das Quadrat einer Ausbreitungsgeschwindigkeit. Es zeigt sich, dass $\frac{1}{\mu_0 \epsilon_0} = c^2$ mit $c \approx 3 \cdot 10^8$ m/s. Damit wurde Maxwell klar, dass Licht kein eigenständiges Phänomen ist, sondern lediglich eine elektromagnetische Welle.

Das Ausbreitungsmedium von elektromagnetischen Wellen sind also gewissermaßen das elektrische und magnetische Feld. Zuvor nahm man als Ausbreitungsmedium von Licht den sogenannten Lichtether an. Dieses Modell hatte jedoch große Probleme:

Wenn das Medium von Licht der Ether sein soll, dann stellt sich die Frage, mit welcher Geschwindigkeit wir uns gegenüber dem Lichtether bewegen. Um diese Frage zu klären wurde folgendes Experiment durchgeführt (Michelson–Morley-Experiment, 1877): Man messe die Ausbreitungsgeschwindigkeit von Licht in unterschiedliche Richtungen. Da sich die Erde vermutlich gegenüber dem Ether bewegt, müsste man einen Unterschied der Ausbreitungsgeschwindkeiten in die unterschiedlichen Richtungen messen. Doch bei der Durchführung war dies nicht der Fall! Nun wäre es natürlich denkbar, dass man sich in diesem Moment genau in Ruhe gegenüber dem Ether befand. Man wartete also ein halbes Jahr und führte das Experiment erneut durch. Da sich die Erde dann ja in die genau entgegengesetzte Richtung bewegt, hätte man zumindest dann einen Unterschied feststellen können müssen; doch wieder nichts.

Wie erklärt man nun dieses Phänomen? Dem Ether wurden zunehmend mehr Eigenschaften zugesprochen, die -- wie Einstein bemerkte -- nur den Zweck hatten, den Ether unbeobachtbar zu machen, was zutiefst unwissenschaftlich ist. Andere Folgerungen aus diesen Messungen könnten sein, dass entweder das Relativitätsprinzip nicht immer gilt, oder dass die Maxwell-Gleichungen falsch sind. Beides würde die Physik in gleich schwere Krisen werfen. Einstein schlägt nun in seiner **speziellen Relativitätstheorie** (1905) einen dritten Weg vor, der nicht verlangt, dass eines dieser etablierten Konzepte aufgegeben werden muss: Er stellt fest, dass die Zeit für unterschiedliche Beobachter nicht unbedingt gleich verlaufen muss.

# Spezielle Relativitätstheorie

Die Grundaussage der speziellen Relativitätstheorie ist, dass es weder den einen Raum, noch die eine Zeit gibt, die alle gleich wahrnehmen. Es gibt lediglich eine Raumzeit, die von verschiedenen Beobachtern unterschiedlich in räumliche und zeitliche Komponenten zerlegt werden kann. Die wichtigste Erkenntnis, um sich die spezielle Relativitätstheorie herzuleiten, steckt bereits in der Wellengleichung des Lichts, die aus den homogenen Maxwell-Gleichungen hervorgeht, und wird vom Michelson-Morley-Experiment noch einmal unterstrichen: Die Ausbreitungsgeschwindigkeit von Licht ist konstant, nämlich *egal für welchen Beobachter*!

## Minkowski-Raum

Um die Vorstellung von Raumzeit zu veranschaulichen, hat Minkowski das überaus nützliche Werkzeug des Minkowski-Raumes geschaffen: Er hat vier Dimensionen (drei räumliche, eine zeitliche) und gliedert sich in Gleichzeitebenen, die aus all jenen Punkten der Raumzeit bestehen, die *ein bestimmter Beobachter* als gleichzeitig wahrnimmt. Abbildung \ref{fig:gleichzeitebenen} soll das illustrieren. Da es schwer ist, vier dimensionen auf einem zweidimensionalen Medium abzubilden, beschränken wir uns hier auf drei Dimensionen und im Weiteren auf nur mehr zwei.

![Gleichzeitebenen im Minkowski-Raum \label{fig:gleichzeitebenen}](./img/tex/rta_drawings_gleichzeitebenen.png){width=75%}


Markiert man nun für ein bestimmtes Objekt dessen Position auf mehreren Gleichzeitebenen, so kann man einen zeitlichen Verlauf dessen Position sehen. Die Linie, die das Objekt dabei durch die Raumzeit zieht nennt man Weltlinie. In Abbildung \ref{fig:weltlinien_3d} sind genau solche Weltlinien für zwei Objekte abgebildet. Das eine Objekt bewegt sich geradlinig und gleichförmig. Seine Weltlinie entspricht daher einer Geraden. Für beschleunigte Objekte sind die Weltlinien jedoch gebogen. Im Allgemeinen können Weltlinien nahezu beliebig verlaufen (mit einigen Einschränkungen, wie wir sehen werden).

![Weltlinien von zwei Objekten \label{fig:weltlinien_3d}](./img/tex/rta_drawings_weltlinien_3d.png){width=45%}

Stellen wir uns nun folgende Situation vor: Ein Mensch wirft einen Stein in einen Teich. Von dem Punkt aus, an dem der Stein die Wasseroberfläche trifft, werden sich konzentrisch kreisförmige Wellen ausbreiten. Nach allen Richtungen hin wird die Wellenfront die gleiche Geschwindigkeit haben (relativ zum Mittelpunkt). Wenn wir uns die Weltlinien der Wellenfront überlegen, werden wir feststellen, dass sie einen Kegel im Minkowski-Raum aufspannen. Der analoge zweidimensionale Fall ist in Abbildung \ref{fig:gleichgeschwindigkeitskegel} dargestellt. (In diesem Fall degeneriert der Kegel zu einem Dreieck.) Je schneller sich die Wellen ausbreiten, desto flacher wird der Kegel sein. Der Öffnungswinkel (in der Abbildung durch $\alpha$ dargestellt) ist also gewisserweise ein Maß für die Ausbreitungsgeschwindigkeit.

![Gleichgeschwindigkeitskegel mit Öffnungswinkel $\alpha$ \label{fig:gleichgeschwindigkeitskegel}](./img/tex/rta_drawings_gleichgeschwindigkeitskegel.png){width=50%}


Stellen wir uns nun eine ganz ähnliche Situation vor: Auf unserem Schreibtisch steht eine Lampe. Zu einem bestimmten Zeitpunkt schalten wir diese Lampe ein, woraufhin sich Licht von dieser Lampe ausbreitet. Wir haben bereits festgestellt, dass Licht nichts anderes ist, als elektromagnetische Wellen, und so wie jede andere Welle auch besitzt Licht eine (endliche) Ausbreitungsgeschwindigkeit, nämlich die Lichtgeschwindigkeit. Wir können daher auch für Licht einen Gleichgeschwindigkeitskegel zeichnen. Da die Lichtgeschwindigkeit allerdings sehr groß ist, wird dieser Kegel unglaublich flach. Um dem entgegenzuwirken skalieren wir die räumlichen Dimensionen mit $1/c$. Dadurch wird der Gleichgeschwindigkeitskegel einen Öffnungswikel von genau 45° haben. Da sich in der Relativitätstheorie nahezu alles um den Gleichgeschwindigkeitskegel von Licht dreht, gibt man ihm verkürzt den Namen 'Lichtkegel'. Ein solcher Lichtkegel ist in Abbildung \ref{fig:lichtkegel} dargestellt. 

![Lichtkegel \label{fig:lichtkegel}](./img/tex/rta_drawings_lichtkegel.png){width=50%}

Stellen wir uns nun vor, was wir beobachten würden, wenn jemand diese Schreibtischlampe nun nehmen würde, und sich damit von uns entfernen würde. Wir wollen uns diese Situation zunächst unter dem Modell der *klassischen* Mechanik überlegen. Wenn sich die Person mit Geschwindigkeit $v$ von uns wegbewegt, dann müssten wir den Eindruck haben, dass sich der von uns weggerichtete Teil des Lichtkegels nicht mit der Geschwindigkeit $c$ ausbreitet, sondern mit $c+v$. Gleichermaßen würde uns das auf uns gerichtete Licht auch nicht mehr mit $c$ erreichen, sondern mit $c-v$. Der Lichtkegel müsste dann für uns so aussehen, wie in Abbildung \ref{fig:lichtkegel_beobachter_klassisch}. Wir selbst sind der Beobachter mit der roten Weltlinie, die Glühbirne besitzt die grüne Weltlinie. Nach dem klassischen Modell ist der Lichtkegel geneigt. Dass dieses Modell nicht der Wirklichkeit entspricht, zeigt das früher besprochene Michelson-Morley-Experiment.

![Eine sich von uns entfernende Lichtquelle im klassischen Modell \label{fig:lichtkegel_beobachter_klassisch}](./img/tex/rta_drawings_lichtkegel_beobachter_klassisch.png){width=60%}

Doch wie müsste der Lichtkegel nun tatsächlich aussehen? Wir haben bereits festgehalten, dass alle Beobachter die gleiche Lichtgeschwindigkeit wahrnehmen. Das bedeutet aber auch, dass alle Beobachter den gleichen Lichtkegel wahrnehmen. Die Antwort ist also, er müsste unverändert erscheinen. Und genau diese Erkenntnis führt zur speziellen Relativitätstheorie. Damit auch ein bewegter Beobachter den gleichen Lichtkegel wahrnimmt, wie ein unbewegter, müssen wir lediglich die Raumzeit anders in Raum und Zeit aufteilen. Was wir dazu tun, lässt sich intuitiv als Scherbewegung verstehen, sodass die Längen der Diagonalen erhalten bleiben. Mathematisch gesehen ist das eine Poincaré-Bewegung, wie sie in Abbildung \ref{fig:poincare} dargestellt ist (wenn auch nicht ganz präzise).

![Poincaré-Bewegung \label{fig:poincare}](./img/tex/rta_drawings_poincare.png){width=60%}

:::comment TODO
	die abbildung zur poincare-bewegung ist nicht wirklich richtig. sie sollte der abbildung nachempfunden sein von "the emperors new mind" auf seite 258
	momentan ließe sich mit dieser skizze zwar zeitdilatation verstehen, aber nicht längenkontraktion
:::

Mit der Poincaré-Bewegung lässt sich auch verstehen, was in Abbildung \ref{fig:lichtkegel_beobachter_relativistisch} zu sehen ist. Wieder bewegt sich unsere Schreibtischlampe von uns weg. Diesmal wenden wir jedoch die Poincaré-Bewegung an, um zu erreichen, dass sowohl der rote, als auch der grüne Beobachter den gleichen Lichtkegel wahrnehmen. (Man beachte, dass der rote Querstrich dieselbe Länge hat wie der grüne Querstrich.) Durch diese Poincaé-Bewegung verändern sich aber auch die Gleichzeitebenen. Genau das ist damit gemeint, dass verschiedene Beobachter die Raumzeit unterschiedlich in Raum und Zeit aufteilen. Zwei Punkte in der Raumzeit, die ein Beobachter als gleichzeitig wahrnimmt (also auf derselben Gleichzeitebene liegen) müssen für einen anderen Beobachter nicht notwendigerweise auch gleichzeitig sein. Dies kann sogar soweit gehen, dass die beiden Beobachter die Ereignisse in unterschiedlicher Reihenfolge wahrnehmen! In Abbildung \ref{fig:lichtkegel_beobachter_relativistisch} etwa nimmt der rote Beobachter zuerst das Ereignis $a$ wahr und dann das Ereignis $b$. Für den grünen Beobachter wirkt die Reihenfolge genau andersherum. In dieser einfachen Skizze sind bereits viele der wesentlichsten Implikationen der speziellen Relativitätstheorie zu finden.

![Eine sich von uns entfernende Lichtquelle im relativistischen Modell \label{fig:lichtkegel_beobachter_relativistisch}](./img/tex/rta_drawings_lichtkegel_beobachter_relativistisch.png){width=60%}

## Zeitdilatation

Eine dieser wesentlichen Implikationen ist die sogenannte Zeitdilatation, die umgangssprachlich besagt: "Bewegte Uhren gehen langsamer." Betrachten wir dazu wieder die beiden Punkte $a$ und $b$ in Abbildung \ref{fig:lichtkegel_beobachter_relativistisch}. Ihr zeitlicher Abstand aus Sicht des roten Beobachters beträgt zwei Einheiten, weil von einem Punkt zum anderen zwei Gleichzeitebenen des roten Beobachters überquert werden müssen. Man sieht dies etwas leichter, wenn man die Position des Punktes $b$ entlang der Gleichzeitebene verschiebt, sodass er direkt über Punkt $a$ zu liegen kommt, aber immer noch denselben zeitlichen Abstand hat. Genau das ist durch Punkt $c$ dargestellt. Wenn man ganz analog dazu den zeitlichen Abstand zwischen $a$ und $b$ aus Sicht des grünen Beobachters ermitteln möchte, kann man auf gleiche Weise Punkt $a$ bis zu Punkt $d$ entlang der gleichzeitebene dieses Beobachters verschieben. Dann wird man leicht sehen, dass aus Sicht des grünen Beobachters nur eine einzige Zeiteinheit vergeht, statt zwei. Für den grünen Beobachter wirkt es also so, als würde die Zeit langsamer vergehen.

Dieser Effekt kann auch sehr gut durch die Minkowski-Metrik hergeleitet werden. Eine Metrik gibt allgemein den Abstand zwischen zwei Punkten an. Die Minkowski-Metrik ist jedoch besonders interessant, weil die Abstände, die sie angibt, eine sehr einfache physikalische Interpreation haben: Sie gibt die *wahrgenommene*, vergangene Zeit an. Sie ist definiert als $$s^2 = t^2 - \Delta \vec{x}^\intercal \cdot \Delta \vec{x}$$. (Diese Definition ist "The Emperors New Mind" von Roger Penrose entnommen. In der VO sind die Vorzeichen jedoch getauscht.) Dabei ist $t$ der Abstand zwischen den Punkten auf der Zeitachse und $\Delta\vec{x}$ der Abstand (als Spaltenvektor) auf der Gleichzeitebene. Dieser Abstand auf der Gleichzeitebene zwischen zwei Punkten hängt direkt mit der Geschwindigkeit $v$ zwischen ihnen zusammen. Der Einfachheit halber geben wir diese Geschwindigkeit meist als Anteil an der Lichtgeschwindigkeit an: $\beta=\frac{v}{c}$. Für den Abstand kann man dann einsetzen $\Delta\vec{x}^\intercal \cdot \Delta\vec{x} = (\beta t)^2$ und kommt somit auf $$s^2 = t^2 - (\beta t)^2 = t^2\cdot(1-\beta^2)$$. Gemeinsam mit dem Wissen, dass $s$ die wahrgenommene Zeit angibt, kann man hier bereits erahnen, dass für schnelle Beobachter die Zeit langsamer vergeht. Man kann auch einfacher schreiben $$s=t\cdot \frac{1}{\gamma} \hspace{2cm} \gamma = \frac{1}{\sqrt{1-\beta^2}}$$. Dieser Faktor $\gamma$ nennt sich **Lorentz-Faktor** und spielt in nahezu allen relativistischen Effekten eine wichtige Rolle.

## Längenkontraktion

So wie es Zeitdilatation gibt, ist auch Längenkontraktion eine direkte Implikation der Relativitätstheorie. Und so wie Zeit für bewegte Beobachter mit dem Lorentz-Faktor gedehnt wird, werden Distanzen und Längen entlang der Bewegungsrichtung mit demselben Faktor gestaucht. (Das wird in der Skizze noch nicht richtig wiedergegeben, da die Poincaré-Bewegung nicht richtig dargestellt wird.)

Dass ein und dasselbe Objekt für unterschieldiche Beobachter unterschiedliche Längen hat, wirkt zunächst etwas befremdlich. Um sich zu veranschaulichen, wie das möglich ist, muss man sich zunächst überlegen, wie man denn Längen misst, z.B. eines Tisches: Wir gehen zum einen Ende des Tisches, merken uns die Position der Ecke, gehen zum anderen Ende des Tisches, ermitteln dessen Position und berechnen schlussendlich die Differenz der beiden Positionen. Damit diese Messung im Allgemeinen gültig ist, müssen die beiden Messungen *gleichzeitig* stattfinden. Ansonsten könnte es ja sein, dass jemand in der Zeit zwischen den beiden Messungen den Tisch verschiebt und somit unsere Messung verfälscht. Und genau darin liegt das Problem: Wenn ein Beobachter eine korrekte Messung ausführt -- also die beiden Positionsbestimmungen gleichzeitig durchführt -- und ein anderer, bewegter Beobachter dasselbe Objekt vermisst, wird er unterschiedliche Punkte der Raumzeit als gleichzeitig wahrnehmen. Jeder der beiden Beobachter wäre also der Meinung, dass die Messung des jeweils anderen unzulässig ist.


:::example Myonenzerfall
	Wenn kosmische Strahlung auf die Atmosphäre trifft, kommt es zu Stoßprozessen. Dadurch bilden sich in einer Höhe von etwa 10km sogenannte Myonen. Myonen sind Teilchen, die jedoch nur sehr kurzlebig sind: Ihre Halbwärtszeit beträgt 22$\mu$s. Bei der gegebenen Geschwindigkeit, mit der sie sich fortbewegen, würden nur sehr wenige von ihnen die Erdoberfläche erreichen. Wenn man die Anzahl der eintreffenden Myonen auf der Erdoberfläche misst, stellt man jedoch eine wesentlich höhere Anzahl fest. Wie kann das sein?
	
	Die Antwort liegt in der Zeitdilatation. Dadurch, dass sich die Myonen mit einem nicht vernachlässigbaren Teil der Lichtgeschwindigkeit bewegen machen sich relativitstische Effekte bemerkbar. Für die Myonen vergeht die Zeit anscheinend langsamer, daher können mehr von ihnen auf die Erdoberfläche treffen, bevor sie nach ihrer kurzen Lebenszeit zerfallen. Doch wie ist das aus Sicht des Myons selbst? Das Myon befindet sich ja relativ zu sich selbst in Ruhe. Wieso hat es daher nicht den Eindruck, schon in wesentlich größeren Höhen in der Atmosphäre zu zerfallen? Die Antwort darauf wiederum liegt in der Längenkontraktion. Es hat zwar den Eindruck, die Zeit würde "normal schnell" vergehen, aber da sich die Erdoberfläche sehr schnell auf das Myon zubewegt, wirkt die Distanz zu ihr verkürzt. Daher kann das Myon trotz der kurzen Halbwärtszeit mehr Strecke zurücklegen, als klassischerweise erwartet.
:::

## Energie

Wenn nun aber die Begriffe von Zeit und Länge neu definiert werden müssen, dann gilt das auch für alle Begriffe wie Impuls oder Energie. Der Fall für die kinetische Energie ist besonders interessant. In der klassischen Mechanik war die kinetische Energie jene Arbeit, die eine Kraft verrichten müsste, um ein Objekt auf eine bestimmte Geschwindigkeit zu beschleunigen. Diese Definition wollen wir beibehalten, jedoch müssen wir nun die relativistischen Effekte miteinbeziehen. Durch etwas mathematische Trickserei kommen wir auf $$E_{kin} = m \cdot c^2 \cdot (1-\gamma)$$. Diese Formel besteht nun aus einem geschwindigkeitsabhängigen und einem geschwindigkeitsunabhängigen Teil. Wir sehen bereits, dass der geschwindigkeitsunabhängige Teil zu $$E = m \cdot c^2$$ führt. Albert Einstein hat diese Erkenntnis, dass es sich bei Masse und Energie um dieselbe physikalische Entität handelt, für die wichtigste Implikation der speziellen Relativitätstheorie gehalten.

:::example Uranzerfall
	Wenn ein Uran-238-Atom in ein Thorium-234-Atom und ein Alphateilchen zerfällt, besitzen das Thorium-Atom und das Alphateilchen gemeinsam eine geringere Ruhemasse als zuvor das Uran-Atom. Die Massendifferenz geht gemäß der Formel $E = m \cdot c^2$ in Energie über. Diese Energie wird in Atomkraftwerken dazu genutzt, Strom zu erzeugen.
:::

:::comment TODO
	einfügen: ruhemasse?, energie-impuls-vierervektor?
:::

:::comment TODO
	einfügen: keinerlei information kann sich schneller ausbreiten als mit lichtgeschwindigkeit, da sich sonst ein paradoxon entwickeln ließe. sie emperors new mind, s. 273-275
:::


# Allgemeine Relativitätstheorie

Stellen wir uns folgende Situation vor: Eine Wissenschaftlerin wacht in einer Fahrstuhlkabine auf. Von außen können wir sagen, dass sich die Kabine im freien Fall befindet. Newton würde sagen, dass sowohl die Kabine, als auch die Wissenschaftlerin dieselbe Beschleunigung in Folge der Gravitationskraft erfahren. Die Wissenschaftlerin hätte jedoch nicht das Gefühl, es würde eine Kraft auf sie einwirken. Tatsächlich würde sie das Gefühl haben, schwerelos zu sein. Sie könnte kein Experiment durchführen, durch das sich festellen ließe, ob sie sich gerade im freien Fall oder in der Schwerelosigkeit befindet. Diese Beobachtung lässt sich zum sogenannten **Äquivalenzprinzip** verallgemeinern: Es gibt keine Möglichkeit zwischen einem homogenen Gravitationsfeld und einem gleichmäßig beschleunigten Bezugssystem zu unterscheiden. Sie sind vollkommen äquivalent.

Genau diese Vorstellung hat Einstein dazu veranlasst zu hinterfragen, ob Gravitation tatsächlich eine Kraft ist. In weiterer Folge hat er ein völlig neues Konzept von Gravitation entwickelt und dabei auch die Vorstellung von Raumzeit grundlegend verändert. Die Theorie, die aus seinen Überlegungen hervorging, ist die allgemeine Relativitätstheorie.

## Gekrümmte Raumzeit

Erinnern wir uns zurück an den Minkowski-Raum als Modell der Raumzeit. Diesen Raum haben wir in viele Gleichzeitebenen zerlegt. Viele Gleichzeitebenen übereinander ergeben die Raumzeit, durch die sich Objekte auf sogenannten Weltlinien bewegen. Als einen Sonderfall solcher Weltlinien haben wir gerade Weltlinien gesehen. Wenn eine Weltlinie gerade ist, dann bewegt sich das zugehörige Objekt mit konstanter Geschwindigkeit, bzw. ohne Beschleunigung. Das bedeutet, auf das Objekt wirkt keine Kraft!

Dieses Konzept soll beibehalten werden: Objekte, auf die keine Kraft wirkt, besitzen gerade Weltlinien. Wie wir oben festgestellt haben, hat die Wissenschaftlerin in der Aufzugkabine nicht das Gefühl, es würde eine Kraft auf sie wirken. Demnach müsste ihre Weltlinie gerade sein. Von außen betrachtet beschleunigt sie aber Richtung Erdboden und hat somit eine gekrümmte Weltlinie (, weil ihre Geschwindigkeit ja laufend zunimmt). Wie passt das zusammen?

Die Antwort, die uns die allgemeine Relativitätstheorie darauf gibt, ist, dass diese anscheinend gekrümmte Weltlinie tatsächlich gerade ist, aber die Raumzeit selbst gekrümmt ist! Gravitation hängt also mit der Krümmung der Raumzeit zusammen. Damit diese Theorie konsistent mit den Beobachtungen ist, die wir in Bezug auf Anziehungskraft gemacht haben, muss mehr Masse auch zu einer stärkeren Krümmung führen. Dieser Sachverhalt ist in einer der **Einstein'schen Feldgleichungen** erfasst: $$\textsf{Krümmung der Raumzeit} = G \cdot \textsf{Massendichte}$$ Es sollte klar sein, dass diese Darstellung der Formel nur zur Veranschaulichung dient. Die tatsächliche Mathematik hinter dieser Veranschaulichung erfordert einiges Wissen über analytische Geometrie und Tensoren. Für uns soll daher diese Darstellung genügen.

## Geodäten

Wir haben bereits festgehalten, dass die Weltlinien, auf denen sich Objekte im freien Fall bewegen, gekrümmt erscheinen, aber irgendwie gerade sind. Um zu verstehen, was damit gemeint ist, müssen wir den Begriff einer Geraden etwas allgemeiner definieren. 

Im Minkowski-Raum war eine Gerade noch das, was wir uns üblicherweise darunter vorstellen: eben ein gerader Strich. Das liegt daran, dass auf den flachen Gleichzeitebenen die gewohnte Euklidische Geometrie gilt. Im Rahmen der allgemeinen Relativitätstheorie nehmen wir jedoch nicht mehr an, dass diese flache Geometrie gilt. Stattdessen müssen wir uns mit gekrümmten Geometrien befassen.

Die anschaulichste Weise, Konzepte aus dem flachen Raum auf einen gekrümmten Raum zu übertragen, ist ein Vergleich zwischen einer Tischplatte und einem Ball. Stellen wir uns vor, eine Ameise würde sich auf einer Tischplatte von Punkt A nach Punkt B bewegen und dabei den kürzesten Weg wählen, also sich nicht nach links oder rechts wenden. Der Weg, den sie dabei beschreibt ist eben eine Gerade, wie wir sie uns gewöhnlicherweise vorstellen. Sie zeichnet sich durch dabei im Wesentlichen durch eine Eigenschaft aus, die keine andere Linie -- wie auch immer geartet -- auf diesem Tisch erfüllt: Sie ist eine Geodäte zwischen A und B, d.h. die kürzeste mögliche Verbindung. Wenn wir nun das Konzept von Geraden abstrahieren wollen, dann tun wir dies über ebendiesen Begriff der Geodäte. Dass Geodäten nicht immer gerade sein müssen, wird klar, wenn wir uns nun vorstellen, die Ameise würde die kürzeste Verbindung zwischen Punkten nicht auf einer Tischplatte sondern auf einem Ball suchen. Ihre Bewegungsfreiheit ist auf die Oberfläche des Balles beschränkt. Sie kann also nicht "durch den Ball durchgehen". Die kürzeste Verbindung, die sie finden kann, ist also nicht eine Gerade, sondern entlang der Oberfläche des Balles gekrümmt. In Abbildung \ref{fig:geodaeten} ist daher sehr schön zu sehen, dass sie die eigentlich Geodäte auf der Kugel von der geraden, strichlierten Linie unterscheidet.

![Geodäten in flachen und gekrümmten Geometrien \label{fig:geodaeten}](./img/tex/rta_drawings_geodaeten.png){width=60%}


## Gravitation

Nun, da wir Geodäten als Verallgemeinerung von Geraden kennen, können wir auch verstehen, wieso eine Krümmung der Raumzeit mit Gravitation gleichzusetzen ist. Dazu bemühen wir wieder einen ähnlichen Vergleich wie gerade eben. Stellen wir uns vor, auf einer Tischplatte würden zwei Ameisen krabbeln, nämlich entlang zweier paralleler Geraden bzw. Geodäten. Wenn sie am Ende des Tisches ankommen, dann wird ihr Abstand zu einander genau so groß sein, wie als sie vom andere Ende losgekrabbelt sind, schließlich entspricht das genau unserer Vorstellung von Parallelität in der Euklidischen Geometrie. Wenn die beiden Ameisen das gleiche auf einem Ball probieren, werden sie jedoch etwas überraschendes feststellen: Wenn sie wieder parallel zu einander krabbeln, werden sie feststellen, dass sie, obwohl beide immer nur geradeaus krabbeln und sich immer parallel zu einander bewegen, sie einander dennoch näherkommen, bis sie sich sogar überschneiden! Abbildung \ref{fig:gravitation} illustriert diesen Sachverhalt.

![Durch krümmung der Geometrie laufen parallele Geodäten dennoch zusammen \label{fig:gravitation}](./img/tex/rta_drawings_gravitation.png){width=60%}

Wenn diese Geodäten nun als Weltlinien in der Raumzeit interpretiert werden, dann lässt sich Gravitation ganz intuitiv verstehen. In Abwesenheit von Masse wäre die Raumzeit flach (etwa wie die Tischplatte) und zwei Punkte hätten keinen Grund jemals einander näherzukommen, solange keine externe Kraft auf sie wirkt. Wenn sich nun aber an einem der Punkte eine Masse befindet, die den Raum krümmt, dann würden die geodätischen Weltlinien anderer Punkte beginnen, sich in die Richtung dieser Masse zu krümmen. Wenn man so möchte, wird die zeitliche Komponente der Raumzeit zunehmend stärker in die räumliche gekrümmt. Das nehmen wir dann als Beschleunigung wahr. Und genau deshalb empfinden wir die Krümmung der Raumzeit als Gravitations"kraft".

## Lichtkegel

Dass die Beschleunigung zur Folge der Gravitation unabhängig von der Masse eines Objekts ist, wussten wir bereits von Newton. Jetzt wissen wir aber auch wieso das so ist. Und noch eine weitere interessante Beobachtung können wir machen: Nach dem Newton'schen Gravitationsgesetz existiert Gravitation nur zwischen Massen. Da wir aber nun wissen, dass Gravitation eine geometrische Eigenschaft der Raumzeit ist, folgt, dass auch Entitäten, die keine Masse besitzen, von der Gravitation beeinflusst werden. Insbesondere gilt das für Licht, also reine elektromagnetische Wellen!

Licht wird also genauso von der Gravitation angezogen, wie alles andere auch. Das bedeutet aber das wir das wichtigste Werkzeug der SRT für die ART auch noch einmal neu denken müssen: den Lichtkegel! Tatsächlich "kippt" der Lichtkegel in Richtung großer Massen. Nahe an der Sonne würde sich Licht also etwas schneller in Richtung Sonne ausbreiten als von ihr weg. In größerer Distanz zur Sonne, würde der Lichtkegel aber wieder fast vollständig "aufrecht" stehen. Graphisch veranschaulicht sieht man das in Abbildung \ref{fig:lichtkegel_gekippt}.

![Lichtkegel kippen in Folge der Gravitation \label{fig:lichtkegel_gekippt}](./img/tex/rta_drawings_lichtkegel_gekippt.png){width=80%}

## Schwarze Löcher

In der SRT haben wir festgestellt, dass sich nichts schneller bewegen als mit Lichtgeschwindigkeit -- nicht nur keine Masse, sondern tatsächlich keinerlei Formen von Energie oder Information. Gemeinsam mit der Tatsache, dass Lichtkegel unter Gravitation kippen, ergibt sich ein äußerst interessantes Phänomen: sogenannte schwarze Löcher, also Regionen von unglaublich hoher Massendichte und so starker Anziehungskraft, dass sie alles, was ihnen zu nahe kommt, schlucken und nichts -- nicht einmal Licht -- ihnen wieder entkommt.

Um zu verstehen, wie dieses Phänomen entsteht, nehmen wir einfach Abbildung \ref{fig:lichtkegel_gekippt} her und spinnen den Gedanken etwas weiter. Wenn wir eine wesentlich höhere Masse hernehmen, werden die Lichtkegel auch stärker kippen. Solange sich die Lichtkegel weit genug von der großen Masse fernhalten, könnte ein Beobachter jederzeit beschließen, sich weiter von der Masse zu entfernen, bis der Lichtkegel fast vollkommen aufrecht steht und der Beobachter vom schwarzen Loch in Ruhe gelassen wird. Begibt sich der Beobachter jedoch zu nah an die Masse heran, kann folgendes passieren: Der Lichtkegel kann so weit kippen, dass auch der Teil, der am weitesten weg von der Masse zeigt, gerade einmal aufrecht zeigt. Da sich der Beobachter immer nur innerhalb des Lichtkegels bewegen kann (weil sich nichts schneller ausbreiten kann als Licht) kann er höchstens seine Distanz zur Masse halten. Er wird sich jedoch nie wieder von der Masse entfernen können. Wenn er sich noch weiter an die Masse heranwagt, kippt der Lichtkegel noch stärker, sodass, egal was der Beobachter auch versucht, er immer stärker und stärker in dieses schwarze Loch eingesaugt wird. Die Stelle, aber der man dem schwarzen Loch so ausgeliefert ist, dass nicht einmal Licht mehr ihm entkommen kann, nennt sich **Ereignishorizont**. Abbildung \ref{fig:schwarzes_loch} soll dies veranschaulichen.

![Lichtkegel nahe eines schwarzen Lochs \label{fig:schwarzes_loch}](./img/tex/rta_drawings_schwarzes_loch.png){width=80%}


:::note Literaturempfehlung
	* "The Emperors New Mind" von Roger Penrose: Gute Erklärungen, wenn man bereits ein bisschen Vorwissen hat. Gut zum Nachlesen.
	* "General Relativity. A Geometric Approach" von Malcolm Ludvigsen: Sehr mathematisch, wenig intuitiv
	* "Physik" von Paul Tipler et al.: Kurze und präzise Erklärungen. Wenn man die mathematischen Teile wegblendet, bleiben recht intuitive Erklärungen übrig
	* "General Relativity from A to B" von Robert Geroch: Insbesondere für ART gut geeignet; ausführliche Erklärungen von schwarzen Löchern
:::

