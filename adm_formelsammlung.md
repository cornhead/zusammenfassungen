
title: "**Formelsammlung: Algebra und diskrete Mathematik**"

...


# Elementare Zahlentheorie

## Teiler
$a$ ist Teiler von $b$:

$a\mid b \Leftrightarrow \exists c: b=a\cdot c$

bzw.

$\frac{a}{b} \in \mathbb{Z}$
($a, b, c \in \mathbb{Z}$)
	
## GGT (Größter gemeinsamer Teiler)
$d$ ist größter gemeinsamer Teiler von $a$ und $b$:

* $d = ggT(a, b) \Leftrightarrow d\mid a \wedge d\mid b \wedge \forall t: (t\mid a \wedge t\mid b) \Rightarrow t\mid d$
* $ggt(a, b) = d \Rightarrow \exists!e,f: e\cdot a + f\cdot b = d$

($d, e, f \in \mathbb{Z}$)
	
## Primzahlen
$p$ ist prim (eine Primzahl):

* $p \in \mathbb{P} \Leftrightarrow 1\mid p \wedge p\mid p \wedge \not\exists a\in \mathbb{Z}\backslash\lbrace\pm1\rbrace:a\mid p$
* $\forall n \in \mathbb{N} \exists! p _1 ,...,p _n \in \mathbb{P}: \prod_{i=1}^{n} p_i = n$ (eindeutige Darstellung als Produkt von Primzahlen)
* $p^k\mid a \wedge p^{k+1}\nmid a \Leftrightarrow \nu_p (a) = k$
* $a = \prod_{p\in \mathbb{P}} p^{\nu_p (a)}$
	
## Kongruenz
$a$ ist kongruent $b$ (modulo $m$):

$a \equiv b \mod m \Leftrightarrow m\mid(b-a)$\newline
($a$ mod $m$: Rest, der bei Division von $a$ durch $m$ bleibt)
\newline\newline
	
Restklasse von $a$ mod $m$:

* $\overline{a} = a+m\cdot \mathbb{Z} = \lbrace a+m\cdot z | z \in \mathbb{Z}\rbrace = \lbrace b\in \mathbb{Z} | b \equiv a\rbrace$
* $\overline{a} + \overline{b} = \overline{a+b}$
* $\overline{a}\cdot \overline{b} = \overline{a\cdot b}$
* $\exists\overline{a}^{-1} \Leftrightarrow ggT(a, m) = 1$

# Komplexe Zahlen

## Imaginäre Einheit

Imaginäre Einheit $i$:

$i^2 = -1$

## Darstellungen

kartesische Darstellung von $z \in \mathbb{C}$:

* $z = a + b\cdot i$ \hfill ( $a, b \in \mathbb{R}$ )

Polardarstellung:

* $z = \left[ r; \phi \right]$ \hfill ($r, \phi \in \mathbb{R}$)

## Rechenregeln

* $z_1 + z_2 = (a_1+a_2) + (b_1+b_2)\cdot i$
* $z_1\cdot z_2 = \left[ r_1\cdot r_2; \phi_1+\phi_2 \right]$
* $z_1 = a_1+b_1\cdot i = \left[ r_1; \phi_1\right]$

($z_1, z_2 \in \mathbb{C}$, $z_1 = a_1 + b_1 \cdot i$, $z_2 = a_2 + b_2 \cdot i$)

Potenzen und Wurzeln siehe unten

## Konjugium

Konjugium von $z$:

* $\overline{z} = a - b\cdot i$
* $|z| = \sqrt{z\cdot \overline{z}}$
* $\frac{1}{z} = \frac{\overline{z}}{z\cdot \overline{z}} = \frac{\overline{z}}{|z|^2}$

## Potenzen und Wurzeln

* $z^n = \left[ r^n; n\cdot \phi \right]$
* $^n \sqrt{z} = w_{0,...,n-1}$
* $w_k = \left[ ^n\sqrt{r}; \frac{\phi}{n}+\frac{2\cdot\pi\cdot k}{n}\right]$

# Relationen

## Relation zwischen zwei Mengen

Kartesisches Produkt zweier Mengen $A$ und $B$:

$A\times B = \left\{ (a, b) | a\in A, b\in B \right\}$

Relation $R$ zwischen $A$ und $B$:

* $R \subset A \times B$
* $(a, b)\in R \Leftrightarrow aRb$ ($a$ steht in Relation zu $b$)
* $R$ heißt binär $\Leftrightarrow A = B$

## Äquivalenzrelationen

Äquivalenzrelationen über $A$ sind binäre Relationen mit folgenden Eigenschaften:

#. Reflexivität: $\forall a\in A: aRa$
#. Symmetrie: $\forall a,b\in A: (aRb \Leftrightarrow bRa)$
#. Transitivität: $\forall a, b, c\in A: \big( (aRb \wedge bRc) \Rightarrow aRc \big)$

## Ordnungen

Halbordnungen über $A$ sind binäre Relationen mit folgenden Eigenschaften:

#. Reflexivität
#. Antisymmetrie: $\forall a, b \in A: \big( (aRb \wedge bRa) \Rightarrow a=b \big)$
#. Transitivität

Totalordnungen über $A$ sind Halbordnungen mit folgender weiterer Eigenschaft:
	
4. Vergleichbarkeit: $\forall a, b\in A: (aRb \vee bRa)$

## Funktionen

Funktionen von $A$ nach $b$ ($f: A \rightarrow B$) sind Relationen für die gilt

* $\forall x\in A \exists! y\in B: xRy$ (man schreibt $f(x)=y$)

$f$ heißt...

* surjektiv $\Leftrightarrow \forall y\in B\exists$ mindestens ein $x\in A: f(x)=y$
* injektiv $\Leftrightarrow \forall y\in B\exists$ höchstens ein $x\in A: f(x)=y$
* bijektiv $\Leftrightarrow \forall y\in B\exists$ genau ein $x\in A: f(x)=y \Leftrightarrow f$ surj. $\wedge$ $f$ inj.



# Algebraische Strukturen

## Binäre Operationen

Binäre Operationen $\circ$ auf $A$ sind Abbildungen $\circ: A\times A \rightarrow A$, die abgeschlossen sind auf $A$, d.h.:

$\forall a, b \in A: (a\circ b)\in A$

## Gruppoide

Gruppoide sind Paare $(A, \circ)$ aus einer Menge $A$ und einer binären Operation $\circ$ auf $A$

## Halbgruppen, Monoide und Gruppen

* Ist ein Gruppoid überdies auch noch\
  **assoziativ**: $\forall a,b,c \in A: (a\circ b)\circ c = a \circ (b\circ c)$\
  nennt man es eine **Halbgruppe**.

* Besitzt eine Halbgruppe überdies ein\
  **neutrales Element**: $\exists e \in A \forall a\in A: e\circ a = a\circ e = a$\
  nennt man sie ein **Monoid**.
* Besitzt ein Monoid überdies\
  **inverse Elemente**: $\forall a\in A\exists a^{-1}\in A: a\circ a^{-1} = a^{-1}\circ a = e$\
  nennt man es eine **Gruppe**.
  
## Übersicht -- div. algebraische Strukturen

-------------------------------------------------
     &nbsp;   assoz.   neutr. Elem.   inv. Elem.
-----------  -------- -------------- ------------
   Gruppoid
   
 Halbgruppe     X
 
     Monoid     X           X
     
     Gruppe     X           X             X
-------------------------------------------------

## Untergruppen

$(U, \circ)$ heißt Untergruppe von $(G, \circ) \Leftrightarrow U \subset G \wedge (U, \circ)$ $Gruppe$


Man schreibt dann $U \leqslant G$

Untergruppenkriterium: $U\leqslant G \Leftrightarrow \forall a,b \in U: a\circ b^{-1} \in U$

## Ringe

$(A, +, \cdot)$ heißt Ring $\Leftrightarrow$

* $(A, +)$ kommutative Gruppe
* $(A, \cdot)$ Halbgruppe
* Es gelten die Distributivgesetze:
	* $\forall a,b,c\in A: a\cdot(b+c) = a\cdot b + a\cdot c$
	* $\forall a,b,c\in A: (a+b)\cdot c = a\cdot c+b\cdot c$

## Körper

$(A,+, \cdot)$ heißt Körper $\Leftrightarrow$

* $(A, +)$ kommutative Gruppe
* $(A\backslash \lbrace 0\rbrace, \cdot)$ kommutative Gruppe
* Es gelten die Distributivgesetze.

