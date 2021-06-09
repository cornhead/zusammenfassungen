
title: "**Formelsammlung: Algebra und diskrete Mathematik**"
...

## Disclaimer

### Mach mit!
An dieser Formelsammlung und der zugehörigen Zusammenfassung kann gerne auf [Github](https://github.com/cornhead/zusammenfassungen.git) mitgewirkt werden!




# Elementare Zahlentheorie

## Teiler
$a$ ist Teiler von $b$:

$a\mid b \Leftrightarrow \exists c: b=a\cdot c$
bzw.
$\frac{a}{b} \in \mathbb{Z}$
($a, b, c \in \mathbb{Z}$)
	
## GGT (Größter gemeinsamer Teiler)
$d$ ist größter gemeinsamer Teiler von $a$ und $b$:

$d = ggT(a, b) \Leftrightarrow d\mid a \wedge d\mid b \wedge \forall t: (t\mid a \wedge t\mid b) \Rightarrow t\mid d$
$ggt(a, b) = d \Rightarrow \exists!e,f: e\cdot a + f\cdot b = d$
($d, e, f \in \mathbb{Z}$)
	
## Primzahlen
$p$ ist prim (eine Primzahl):

$p \in \mathbb{P} \Leftrightarrow 1\mid p \wedge p\mid p \wedge \not\exists a\in \mathbb{Z}\backslash\lbrace\pm1\rbrace:a\mid p$
$\forall n \in \mathbb{N} \exists! p _1 ,...,p _n \in \mathbb{P}: \prod_{i=1}^{n} p_i = n$ (eindeutige Darstellung als Produkt von Primzahlen)
$p^k\mid a \wedge p^{k+1}\nmid a \Leftrightarrow \nu_p (a) = k$
$a = \prod_{p\in \mathbb{P}} p^{\nu_p (a)}$
	
## Kongruzenz
$a$ ist kongruent $b$ (modulo $m$):

$a \equiv b \mod m \Leftrightarrow m\mid(b-a)$\newline
($a$ mod $m$: Rest, der bei Division von $a$ durch $m$ bleibt)
\newline\newline
	
Restklasse von $a$ mod $m$:}
$\overline{a} = a+m\cdot \mathbb{Z} = \lbrace a+m\cdot z | z \in \mathbb{Z}\rbrace = \lbrace b\in \mathbb{Z} | b \equiv a\rbrace$
$\overline{a} + \overline{b} = \overline{a+b}$
$\overline{a}\cdot \overline{b} = \overline{a\cdot b}$
$\exists\overline{a}^{-1} \Leftrightarrow ggT(a, m) = 1$

# Komplexe Zahlen

\textbf{Imaginäre Zahl $i$:}\newline
	$i^2 = -1$
	\newline\newline
	
	\textbf{kartesische Darstellung von $z \in \mathbb{C}$:}\newline
	$z = a + b\cdot i$\newline
	($a, b \in \mathbb{R}$)
	\newline\newline
	
	\textbf{Polardarstellung:}\newline
	$z = \left[ r; \phi \right]$\newline
	($r, \phi \in \mathbb{R}$)
	\newline\newline
	
	\textbf{Rechenregeln:}\newline
	$z_1 + z_2 = (a_1+a_2) + (b_1+b_2)\cdot i$ \newline
	$z_1\cdot z_2 = \left[ r_1\cdot r_2; \phi_1+\phi_2 \right]$\newline
	($z_1, z_2 \in \mathbb{C}, $\newline
	$z_1 = a_1+b_1\cdot i = \left[ r_1; \phi_1\right],$\newline
	$z_2 = a_2+b_2\cdot i = \left[ r_2; \phi_2\right]$)\newline
	Potenzen und Wurzeln siehe unten
	\newline\newline
	
	\textbf{Konjugium von $z$:}\newline
	$\overline{z} = a - b\cdot i$\newline
	$|z| = \sqrt{z\cdot \overline{z}}$\newline
	$\frac{1}{z} = \frac{\overline{z}}{z\cdot \overline{z}} = \frac{\overline{z}}{|z|^2}$
	\newline\newline
	
	\textbf{Potenzen und Wurzeln:}\newline
	$z^n = \left[ r^n; n\cdot \phi \right]$\newline
	$^n \sqrt{z} = w_{0,...,n-1}$\newline
	$w_k = \left[ ^n\sqrt{r}; \frac{\phi}{n}+\frac{2\cdot\pi\cdot k}{n}\right] $
	
# Relationen

\textbf{Kartesisches Produkt zweier Mengen $A$ und $B$}\newline
	$A\times B = \lbrace (a, b) | a\in A, b\in B \rbrace$\newline\newline
	
	\textbf{Relation $R$ zwischen $A$ und $B$:}\newline
	$R \subset A \times B$\newline
	$(a, b)\in R \Leftrightarrow aRb$ ($a$ steht in Relation zu $b$)\newline
	$R$ heißt binär $\Leftrightarrow A = B$
	\newline\newline
	
	\textbf{Äquivalenzrelationen über $A$}\newline
	sind binäre Relationen mit folgenden Eigenschaften:
	\begin{enumerate}
		\item Reflexivität: $\forall a\in A: aRa$
		\item Symmetrie: $\forall a,b\in A: (aRb \Leftrightarrow bRa)$
		\item Transitivität: $\forall a, b, c\in A: \big( (aRb \wedge bRc) \Rightarrow aRc \big)$
	\end{enumerate}

	\textbf{Halbordnungen über $A$}\newline
	sind binäre Relationen mit folgenden Eigenschaften:
	\begin{enumerate}
		\item Reflexivität
		\item Antisymmetrie: $\forall a, b \in A: \big( (aRb \wedge bRa) \Rightarrow a=b \big)$
		\item Transitivität
	\end{enumerate}

	\textbf{Totalordnungen über $A$}\newline
	sind Halbordnungen mit folgender weiterer Eigenschaft:
	\begin{enumerate}
		\item[4.] Vergleichbarkeit: $\forall a, b\in A: (aRb \vee bRa)$
	\end{enumerate}

	\textbf{Funktionen von $A$ nach $b$ ($f: A \rightarrow B$)}\newline
	sind Relationen für die gilt
	\begin{itemize}
		\item $\forall x\in A \exists! y\in B: xRy$ (man schreibt $f(x)=y$)
	\end{itemize}
	$f$ heißt...
	\begin{itemize}
		\item surjektiv $\Leftrightarrow \forall y\in B\exists$ mindestens ein $x\in A: f(x)=y$
		\item injektiv $\Leftrightarrow \forall y\in B\exists$ höchstens ein $x\in A: f(x)=y$
		\item bijektiv $\Leftrightarrow \forall y\in B\exists$ genau ein $x\in A: f(x)=y \Leftrightarrow f$ surj. $\wedge$ $f$ inj.
	\end{itemize}


# Algebraische Strukturen

\textbf{Binäre Operationen $\circ$ auf $A$}\newline
	 sind Abbildungen $\circ: A\times A \rightarrow A$,\newline
	 die abgeschlossen sind auf $A$, d.h.:\newline
	 $\forall a, b \in A: (a\circ b)\in A$
	 \newline\newline
	 
	 \textbf{Gruppoide}\newline
	 sind ein Paar $(A, \circ)$ aus einer Menge $A$\newline
	 und einer binären Operation auf $A$
	 \newline\newline
	 
	 \textbf{Halbgruppen, Monoide und Gruppen}
	 \begin{itemize}
	 	\item Ist ein Gruppoid überdies auch noch\newline
	 		\underline{assoziativ}: $\forall a,b,c \in A: (a\circ b)\circ c = a \circ (b\circ c)$\newline
	 		nennt man es eine \underline{Halbgruppe}.
	 	\item Besitzt eine Halbgruppe überdies ein\newline
	 		\underline{neutrales Element}: $\exists e \in A \forall a\in A: e\circ a = a\circ e = a$\newline
	 		nennt man sie ein \underline{Monoid}.
	 	\item Besitzt ein Monoid überdies\newline
	 		\underline{inverse Elemente}: $\forall a\in A\exists a^{-1}\in A: a\circ a^{-1} = a^{-1}\circ a = e$\newline
	 		nennt man es eine \underline{Gruppe}.
	 \end{itemize}
 
 	\textbf{Untergruppen}\newline
 	$(U, \circ)$ heißt Untergruppe von $(G, \circ) \Leftrightarrow U \subset G \wedge (U, \circ)$ $Gruppe$\newline
 	Man schreibt dann $U \leqslant G$\newline
 	Untergruppenkriterium: $U\leqslant G \Leftrightarrow \forall a,b \in U: a\circ b^{-1} \in U$
 	\newline\newline
 	
 	\textbf{Ringe}\newline
 	$(A, +, \cdot)$ heißt Ring $\Leftrightarrow$
 	\begin{enumerate}
 		\item $(A, +)$ $komm.$ $Gruppe$
 		\item $(A, \cdot)$ $Halbgruppe$
 		\item Es gelten die Distributivgesetze:
 		\begin{itemize}
 			\item $\forall a,b,c\in A: a\cdot(b+c) = a\cdot b + a\cdot c$
 			\item $\forall a,b,c\in A: (a+b)\cdot c = a\cdot c+b\cdot c$
 		\end{itemize}
 	\end{enumerate}
 
 	\textbf{Körper}\newline
 	$(A,+, \cdot)$ heißt Körper $\Leftrightarrow$
 	\begin{enumerate}
 		\item $(A, +)$ $komm.$ $Gruppe$
 		\item $(A\backslash \lbrace 0\rbrace, \cdot)$ $komm.$ $Gruppe$
 		\item Es gelten die Distributivgesetze.
 	\end{enumerate}

