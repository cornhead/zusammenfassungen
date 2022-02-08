---
summary-type: formula_sheet
title: "**Formelsammlung: Digital Design**"
...


## Delay

Delay $=$ intrinsisch $+$ Kapazität $\cdot$ extrinsisch

## vereinfachte Wärmeleitgleichung
$T_{junction} = T_{ambient} + P * \theta_{JA}$

* $T_{junction}$ ... Temperator am Die
* $T_{ambient}$ ... Umgebungstemperatur
* $P$ ... Verlustleistung des Chips
* $\theta_{JA} = \theta_{JC}+\theta_{CA}$ ... Wärmewiderstand von Junction zu Ambient: Einheit K/W
	* $\theta_{JC}$ ... Wärmewiderstand von Junction zu Case
	* $\theta_{CA}$ ... Wärmewiderstand von Case zu Ambient
		
## Verlustleistung durch Ladeströme
$P_{lade} = C_{äqu} \cdot f \cdot V_{dd}^2$

* $P_{lade}$ ... Verlustleistung durch Ladeströme
* $C_{äqu}$ ... Ersatzkapazität
* $f$ ... Taktfrequenz
* $V_{dd}$ ... Versorgungsspannung
* Herleitung über $E_C = \frac{C\cdot U^2}{2}$

## Wahrscheinlichkeit für Verletzung des Set-Up & Hold-Windows
$P_{violate} = \frac{T_0}{T_{clk}} > 0$

* $P_{violate}$ ... Wahrscheinlichkeit für Verletzung des Set-Up & Hold-Windows
* $T_0$ ... Dauer des Set-Up & Hold-Windows
* $T_{clk}$ ... Taktperiode

## Resolution Time zwischen zwei Flip-Flops
$t_r = T_{clk} - t_{CO} - t_{comb} - t_{su}$

* $t_r$ ... Resolution Time
* $T_{clk}$ ... Taktperiode
* $t_{CO}$ ... Dauer von Clock zu Output
* $t_{comb}$ ... Dauer zum durchlaufen einer Logikwolke
* $t_{su}$ ... Set-Up-Zeit (ohne Hold-Zeit)

## MTBU (Mean Time Between Upset)
$MTBU = R_{upset}^{-1} = exp\left( \frac{t_r}{\tau_c}\right) \cdot \frac{1}{T_0 \cdot f_{clk} \cdot \lambda_{dat}}$

* $MTBU$ ... Mean Time Between Upset
* $R_{upset}$ ... Upset-Rate
* $t_r$ ... Resolution Time
* $\tau_c$ ... Bauteilparameter des Flip-Flops
* $T_0$ ... Decision-Window, vgl. Wahrscheinlichkeit für Setup-Hold-Violation
* $f_{clk}$ ... Taktfrequenz
* $\lambda_{dat}$ ... Datenrate am Eingang (doppelte Frequenz)
* Interpretation über $R_{upset} = \underbrace{exp\left( - \frac{t_r}{\tau_c} \right)}_{\substack{\text{Wahrscheinlichkeit, dass man aus}\\ \text{Metastabilität nicht rechtzeitig herauskommt}}} \cdot \underbrace{ \underbrace{ \frac{T_0}{T_{clk}} }_{P_{violate}} \cdot \lambda_{dat}}_{\substack{\text{Wahrscheinlichkeit, dass man}\\ \text{in Metastabilität hineinkommt}}}$

## Mean Time To Failure
$MTTF = \frac{A}{J^2}\cdot exp\left(\frac{E}{k\cdot T}\right)$

* $A$ ... Konstante
* $J$ ... Stromdichte, Einheit A/cm$^2$
* $E$ ... Aktivierungsenergie (Materialkonstante)
* $k$ ... Boltzmann-Konstante
* $T$ ... Temperatur (meistens in Kelvin)

## Arrhenius-Gleichung
Fehlerrate $F = C \cdot exp\left(-\frac{E_{act}}{k\cdot T}\right) \approx MTTF^{-1}$
