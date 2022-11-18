---
summary-type: zusammenfassung
title: "**Lecture Notes: Discrete Mathematics**"
...

:::comment
	---------------------------------------------------------
	------------------ lecture 1 ----------------------------
	---------------------------------------------------------
:::

# Graph Theory

:::comment
	---------------------------------------------------------
	------------------ lecture 2 ----------------------------
	---------------------------------------------------------
:::


:::definition Walk, Trail, Path
TODO
:::

:::theorem
TODO
:::

:::lemma Handshaking Lemma
$\sum\limits_{v\in V} deg(v) = 2\cdot |E|$
:::

:::definition Eularian Trail
A Eulerian Trail is a trail that uses every edge exactly once.
:::

:::theorem
A connected graph has a Eulerian circuit if and only if all its vertices have even degree.
:::

\begin{figure}[h!]
\centering
\begin{tikzpicture}[node distance={15mm}, thick, main/.style = {draw, circle}]
\centering
\node[main] (1)              {}; 
\node[main] (2) [below of=1] {};
\node[main] (3) [below of=2] {}; 
\node[main] (4) [right of=2] {};
\draw [bend left=20]  (1) edge (2)  ; 
\draw [bend left=20] (2) edge (1) ; 
\draw [bend left=30] (1) edge (4); 
\draw [bend left=30] (4) edge (3); 
\draw [bend left=20] (2) edge (3); 
\draw [bend left=20] (3) edge (2); 
\draw [bend left=0] (2) edge (4);
\end{tikzpicture}
\caption{no eulerian circuit as every vertex has odd degree}
\end{figure}

:::proof
$\Rightarrow:$ In any circuit every vertex is entered as often as it serves as a point of departure.

$\Leftarrow$: Induction on the number of edges

\begin{itemize}
\item if the graph $G$ has no edges $G$ = $(V = {1}, E = \emptyset)$
\item otherwise let $W$ be any circuit in G ( this exists: start anywhere, choose any edge unused so far, continue until you hit starting vertex)
\item let $G^\prime = (V(G), E(G)\backslash E(W))$, all vertices in $G^\prime$ have even degree and $G^\prime$ need not be connected.
\item let $G^\prime_1, ... G^\prime_c$ be the connected components of $G^\prime$. In each component of $G^\prime_i$ find a Eulerian circuit $W_i$. $W_i$ and $W$ have atleast one vertex in common, because $G$ is connected and removing $W$ produces the components.
\item therefore $W_1, ... W_c$ and $W$ can be combined to a Eulerian circuit. 
\end{itemize}
:::

## Trees and Forests
:::definition
\begin{itemize}
\item A \emph{forest} is a graph without cylces (=acyclic).
\item A \emph{tree} is a connected forest.
\item A \emph{leaf} is a vertex of degree 1.
\end{itemize}
:::

:::lemma
If $T$ is a tree and has two vertices it has at least 2 leafs.
:::

:::proof
$V(T)$ and $E(T)$ are finite $\Rightarrow$ $T$ contains a maximal path and this path has two leafs (because it is maximal).
:::

:::definition Spanning subgraphs
A subgraph $H$ of a graph $G$ is spanning if $V(H) = V(G)$.
:::

:::theorem
Let $T$ be a graph, then the following are equivalent:
\begin{enumerate}
\item $T$ is a tree.
\item Any 2 vertices are connected with a unique path.
\item $T$ is connected and every edge is a bridge (min. connected).
\item $T$ has no cycles and adding any edge yields a cycle (maximal acyclic)
\end{enumerate}
:::

:::proof
\begin{itemize}
\item $1 \Rightarrow 2$: otherwise $T$ would not be connected or $T$ would have a cylce.
\item $2 \Rightarrow 3$: A unique path from $u$ to $v$ exists, which means every edge has to be a bridge.
\item $3 \Rightarrow 4$: An edge in a cycle would not be a bridge $\Rightarrow$ $T$ has no cycles, adding an edge would yield a cyle because T is connected.
\item $4 \rightarrow 1$: adding any edge $(u,v)$ yields a cycle $= T$ is connected.
\end{itemize}
:::

:::theorem
A connected graph $G$ has a spanning tree.
:::

:::proof
As long as there is a non-bridge, remove it, and use 3. of the previous theorem.
:::

:::theorem
A graph is a tree if and only if it is connected and $|V| = |E| + 1$.
:::

:::proof
$\Rightarrow$: induction on $|V|: |V| = 1$

If $|V| \geq  2$: remove a leaf to obtain $T^\prime$, by induction $|V(T^\prime )|= |V(T)| - 1$ and $|E(T^\prime)| = |E(T)| - 1$

$|V(T)| = |V(T^\prime)| + 1 = |E(T^\prime)| + 1 + 1 = |E(T) + 1|$

\vspace{0.5cm}

$\Leftarrow$: Let $T^\prime$ be a spanning tree of $T$

$|V(T^\prime)|=|E(T^\prime)| + 1$

$|V(T)|=|E(T)| + 1$, $|V(T)|=|V(T^\prime)| \Rightarrow |E(T)|=|E(T^\prime)|\Rightarrow T=T^\prime$
:::

How many spanning trees are there?

\begin{figure}
\centering
\includegraphics[width=3cm]{./img/tex/discmath_drawings_spanning_trees_01.png}\\
Spanning trees of the above graph:\\
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_02.png} \hspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_03.png} \hspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_04.png} \hspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_05.png} \\\vspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_06.png} \hspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_07.png} \hspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_08.png} \hspace{0.5cm}
\includegraphics[width=2.5cm]{./img/tex/discmath_drawings_spanning_trees_09.png}
\end{figure}


:::definition
\begin{itemize}
\item $\tau(G)$ is the number of spanning trees of $G$.
\item $G\backslash e$ is the graph obtained by removing edge $e$.
\item $G / e$ is the graph obtained by contracting edge $e$.
\end{itemize}
:::

:::theorem Deletion Contraction Theorem
$\tau(G) = \tau(G\backslash e) + \tau(G/e)$
:::

:::example
\begin{equation}
\tau(\includegraphics[width=2cm]{./img/discmath_g.png}) = \tau(\includegraphics[width=2cm]{./img/discmath_g1.png}) + \tau(\includegraphics[width=2cm]{./img/discmath_g2.png}) = 4 + 4 = 8
\end{equation}
:::

:::proof
The set of spanning trees is the disjoint union of spanning trees containing $e$ and spanning trees not containing $e$.
:::

More generally: If $G$ is a weighted graph with $w: E(G) \rightarrow  \mathbb{R}$ and $H$ is a subgraph of G, then $w(H) = \prod_{e \in E(H)} w(e)$

For weighted graphs, $\tau(G)$ is the sum of the weights of the spanning trees of $G$

$$\tau(G) =  \sum\limits_T \prod_{e \in E(T)} w(e)$$

:::example
$$\tau(\includegraphics[width=2cm]{./img/discmath_1.png}) = \tau(\includegraphics[width=2cm]{./img/discmath_2.png}) + e \cdot \tau(\includegraphics[width=2cm]{./img/discmath_3.png}) = abc + abd +acd+bcd+e(a+d)(b+c)$$
:::

:::definition Degree Matrix
The degree matrix of a graph is 
$$D = \left( \begin{array}{ccccc} d(v_1) \\ & \cdot & & \text{\huge0} \\ & & \cdot \\ & \text{\huge0} & & \cdot \\ & & & & d(v_n) \end{array} \right)$$

(The degree of a vertex in a weighted graph is $d(u) = \sum\limits_{(u,v) \in E(G)} w(v,u)$)
:::

:::theorem
Let $n=|V(G)|$, let $\lambda_1,\dots,\lambda_n$ be the eigenvalues of $D-A$. One of these is $0$, w.l.o.g.\ $\lambda_1 = 0$

Then, $\tau(G)=\frac{1}{n} \cdot \lambda_2 \cdots \lambda_n$.

Equivalently: $\tau(G) = det((D-A)_{i,i})$, where $M_{i,i}$ is obtained by removing row and column i. $M=D-A$
:::

:::example
\includegraphics[width=3cm]{./img/discmath_graph.png}
\\
$\begin{aligned} det(D-A)_{4,4} &= \begin{pmatrix}
a+d & -a & 0 & \text{\st{-d}}\\
-a & a+b+e & -b & \text{\st{-e}}\\
0 & -b & b+c & \text{\st{-c}}\\
\text{\st{-d}} & \text{\st{-e}} & \text{\st{-c}} & \text{\st{c+d+e}}
\end{pmatrix} = \\
&= (a+d) 
\begin{vmatrix}
a+b+e & -b\\
-b & b+c
\end{vmatrix} + a 
\begin{vmatrix}
-a & 0\\
-b & b+c
\end{vmatrix} = \\
&= (a+d)((a+b+e)(b+c)-b^2)-a^2(b+c)
\end{aligned}$
:::


## Spanning Trees of Minimal Weight


Assume graph $G$ is connected.

Kruskal's Algorithm:

\begin{algorithm}
\begin{algorithmic}
\Require Sorted edges by weight: $w(e_1) \leq \dots \leq w(e_m)$.
\State $T_1 \gets \emptyset$
\For{$i$ in $1...m$}
\If{$E(T_i) \cup e_i$ is acyclic}
\State $E(T_{i+1}) \gets E(T_i) \sqcup e_i $
\Else
\State $E(T_{i+1}) \gets E(T_i) $
\EndIf
\If{$|E(T_{i+1}|+1=n-1$}
\State \textbf{return} $E(T) \gets E(T_{i+1}$)
\EndIf
\EndFor
\end{algorithmic}
\end{algorithm}


:::comment
	---------------------------------------------------------
	------------------ lecture 8 ----------------------------
	---------------------------------------------------------
:::

# Combinatorics

unfinished

## Balls in Boxes

We have $k$ balls and $n$ boxes. Balls and boxes could be labelled. Count any assignment $$f:[k] \rightarrow [n] ~ .$$ Notation: $[n] = \{1,\dots,n\}$. $f$ means ''put balls into boxes''. $f$ can be injective (no two balls in same box) or surjective (no empty box). How many \emph{arbitrary} functions from $[k]$ to $[n]$ are there? Answer: $n^k$. For injective case: $n\cdot (n-1) \cdots (n-k+1)$. For surjective case: not a nice formula.

Let the balls are unlabelled and the boxes are labelled. Injective case: $$\binom{n}{k} = \frac{n!}{k! (n-k)!}$$ because $k! \cdots \binom{n}{k} = n\cdot (n-1) \cdots (n-k+1)$. For the arbitrary case: $\binom{n+k-1}{k}$.

TODO{make table for these verbal descriptions}

\begin{table}
\begin{tabular}{cccc}
content...
\end{tabular}
\end{table}

Some identities:
\begin{itemize}
\item $(x+y)^n = \sum\limits_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$ means $n$ balls and 2 boxes. TODO{switch k and n} For instance, the term $2xy^3$ means two possibilities to put 1 ball in the x-box and 3 balls in the y-box.
\item $\sum\limits_{m=0}^{n} \binom{m}{k} = \binom{n+1}{k+1}$
\item $\sum\limits_{k=0}^{n} \binom{m+k}{k} = \binom{m+n+1}{n}$
\end{itemize}

:::lemma
$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k} \forall n \in \mathbb{C}$
:::

:::proof
left hand side is a polynomial in $n$. call it $p(n)$ with degree $k$. The right hand side is $q(n)$ with degree $max\{k-1, k\} = k$.

We have two polynomials with the same degree $\Rightarrow$ $p(x) = q(x) \forall x\in \mathbb{C}$ because $p(n) = q(n) \forall n \in \mathbb{N}$ (which is left as an exercise).
:::

:::theorem Vandermonde
$\binom{x+y}{n} = \sum\limits_{k=0}^{n} \binom{x}{k}\binom{y}{n-k}$
:::

:::proof
$x,y \in \mathbb{N}$: let $|X| = x$, $|Y| = y$, $X\cap Y = \varnothing$

$\binom{x+y}{n}$: \#subsets of $X\cup Y$ of size $n$

$\binom{x}{k}\binom{y}{n-k}$: \# subsets of $x\cup Y$ with $|X| = k$
:::

## Stirling Numbers

Every permutation of $[n]$ is a product of cycles: start at $1$, apply $\pi$, obtain $\pi(1)$, apply again, obtain $\pi(\pi(1))$, eventually we will reach $\pi^k(1) = 1$ again, which forms a cycle. Take any $i\in[n]$ that is not contained in the cycle and repeat.

Notations:
\begin{itemize}
\item Two-line notation: $\left( \begin{array}{cccc}
1 & 2 & \cdots & n \\
\pi(1) & \pi(2) & \cdots & \pi(n)
\end{array}\right)$
\item Cycle Notation: $(1, \pi(1), \dots, \pi^k(1))(\dots)(\dots)$
\end{itemize}

:::example
$$\left( \begin{array}{ccccccccccc}
1 & 2 & 3 & 4 & 5 & 6 & 7  & 8 & 9 & 10 & 11\\
3 & 1 & 8 & 9 & 2 & 4 & 7 & 5 & 6 & 11 & 10
\end{array}\right)$$
is the same as
$$(10, 11)(1, 3, 8, 5, 2)(6, 4, 9)(7)$$
In this case, $(7)$ is called a fixed point and $(10, 11)$ is a transposition.
If a number is not written in the cycle notation, then it is a fixed point (by convention).
:::

Product:

$$(1, 3, 2)\cdot(2, 3, 4) = (1, 3, 4)(2)$$

:::definition Stirling Numbers (First Kind)
$s_{n,k}$ is the number of permutations in $\mathfrak{S}_n$ with $k$ cycles. It's called the Stirling number of the first kind.
:::

:::example
\begin{itemize}
\item $s_{n,1} = (n-1!)$
\item $s_{n,n-1} = \binom{n}{2}$
\item $s_{n,n} = 1$
\end{itemize}
:::

:::theorem
$s_{n,k} = s_{n-1,k-1} + (n-1)s_{n-1,k}$
:::

:::proof
\begin{itemize}
\item Case: $1$ is a fixed point, then $s_{n-1, k-1}$
\item otherwise: $s_{n-1,k}$ has $k$ cycles but element 1 is missing, put 1 before any of $\{2,\dots,n\}$
\end{itemize}
:::

:::definition Set Partition
A set partition of a finite set $A$ is a set of disjoint, non-empty sets with union $A$. The sets are called parts or blocks. (Block is more common.)
:::

:::definition Stirling Number (Second Kind)
$S_{n,k}$ is the number of set partitions of $[n]$ with $k$ parts. This is called the Stirling number of the second kind.
:::

:::example
\begin{itemize}
\item $S_{0,0} = 1$
\item $S_{n,0} = S_{0,n} = 0$ for $n>0$
\end{itemize}
:::

:::theorem
$S_{n,k} = S_{n-1, k-1} + k \cdot S_{n-1,k}$
:::

:::proof
\begin{itemize}
\item Case: $\{n\}$ is a singleton block. Then $S_{n-1, k-1}$
\item otherwise: put $n$ into one of the $k$ blocks: $k\cdot S_{n-1, k}$
\end{itemize}
:::

Notation: the standard way to write set partitions is to sort each set and then sort the sets by their minimal elements: $$\{5,9,3\}\{4,2,6\}\{7\} \rightarrow \{2,4,6\}\{3,5,9\}\{7\}$$

:::theorem
\begin{itemize}
\item $(x)_n := x^{\underline{n}} = x\cdot(x-1)\cdots(x-n+1) = \sum\limits_{k=0}^{n}(-1)^{n-k} \cdot s_{n,k} \cdot x^k$
\item $x^n = \sum\limits_{k=0}^{n} S_{n,k} \cdots x^{\underline{n}}$
\end{itemize}
:::

:::remark
$V_n = \{\}$ is a vector space. $\{1, x, \cdots, x^n\}$ is a basis of $V_n$ and $\{1, x, x^{\underline{2}}, \dots, x^{\underline{n}\}}$ is also a basis. The change of basis matrices are $(S_{n,k})_{n,k}$ and $( (-1)^{n-k} s_{n,k} )_{n,k}$
TODO: finish
:::

:::proof
Induction on $n$:
$x^{\underline{0}} = 1 = s_{0,0}\cdot x^0$

$x^{\underline{n}} = x^{\underline{n-1}} \cdot (x-n+1) = (x-n+1) \sum (-1)^{n-1+k} \cdot s_{n-1,k} \cdot x^k = \sum (-1)^{n-1+k} \cdot s_{n-1,k} \cdot x^{k+1} + (n-1)\sum (-1)^{n-1+k} \cdot s_{n-1,k} \cdot x^k =TODO$
:::

:::comment
	---------------------------------------------------------
	------------------ lecture 9 ----------------------------
	---------------------------------------------------------
:::


## Generating Functions

Power series: a sequence $(a_n)_{n\in\mathbb{N}}, a_n\in\mathbb{C}$

Consider $\sum\limits_{n\geq 0} a_n z^n$ is the series with cofficients $a_n$.

Idea: Power series is useful for approximating functions.

$\sum a_n z^n$ may or may not converge for a given $z\in\mathbb{C}$.

:::definition Formal Power Series (FPS)
A formal power series (FPS), written $\sum a_n z^n$ is the same information as the sequence $(a_n)_{n\in\mathbb{N}}$
:::

Operations on FPS, like addition, multiplication, differentiation, etc.

$\sum\limits_{n=0}^{\infty} a_n z^n \overset{\tiny{powerset}}{:=} \lim\limits_{N\rightarrow \infty} \sum\limits_{n=0}^{N} a_n z^n$ is a limit of a sequence of complex numbers: $a_0, (a_0+a_1z), \dots$

:::theorem
$\lim\limits_{N\rightarrow\infty} \sum\limits_{n=0}^{N} a_n z^n$ exists, if $|z| < \frac{1}{\limsup\limits_{n\rightarrow\infty} \sqrt{|a_n|}} =: R$
TODO{it should be the nth root}

If $|z| > R$, the series diverges.

(If $|z| = R$, an ad hoc analysis is necessary.)
:::

:::remark
$\{z| \text{series converges}\}$ is the domain of convergence, essentially a circle centered at the origin
:::

:::example
\begin{itemize}
\item $\sum\limits_{n\geq0} z^n = \frac{1}{1-z}$ \dots geometric series, $R=1$
\item $\sum\limits_{n\geq0} \frac{z^n}{n!} = e^z$ \dots exponential series, $R=\infty$
\item $\sum\limits_{n\geq0} \binom{\alpha}{n} z^n = (1+z)^\alpha$, $\alpha\in\mathbb{C}$
\end{itemize}
:::

:::theorem Identity Theorem for Power Series
$f(z)=\sum a_n z^n$ converges for $|z| < R$ and $R>0$

$\Rightarrow a_n = \frac{f^{(n)(0)}}{n!}$
:::

Corollary:

$f(z) = \sum a_n z^n = \sum b_n z^n \Rightarrow a_n = b_n \forall n$ (if $|z| < R$)


### Operations on Formal Power Series

Let $A(z) = \sum a_n z^n, B(z) = \sum b_n z^n$, however, $z$ is not a complex number now.

Write $(a_n) \leftrightarrow A(z), (b_n) \leftrightarrow B(z)$

($(0,1,0,\dots) \leftrightarrow z$, $(1,0,0,\dots) \leftrightarrow 1$, $(0,0,0,\dots) \leftrightarrow 0$)

:::definition Operations on FPS
\begin{itemize}
\item $(\alpha a_n + \beta b_n)_{n\in\mathbb{N}} \leftrightarrow: \alpha A(z) + \beta B(z)$
\item $(\sum\limits_{k=0}^{n} a_k b_{n-k})_{n\in\mathbb{N}} \leftrightarrow: A(z) \cdot B(z)$
\item $(a_n \gamma^n)_{n\in\mathbb{N}} \leftrightarrow: A(\gamma z)$
\item $(a_{n-1})_{n\in\mathbb{N}_{\geq 1}} \leftrightarrow: zA(z)$
\item $(n a_n) \leftrightarrow: z A'(z)$
\end{itemize}
:::

:::note
We will use the term generating function for formal power series. Therefore, a generating function is \emph{not} a function
:::

:::example
\begin{itemize}
\item $\frac{1}{1+z} = \sum\limits_{n\geq 0} (-1)^n z^n$ is an equality of FPS
\item $\frac{z}{(1-z)^2} = z(\frac{1}{1-z})' = \sum n z^n$
\item $\frac{1}{(1-z)^k} = \sum\limits_{n\geq 0} \binom{n+k-1}{k-1} z^n$
\end{itemize}
:::

:::remark
if $A(z) = B(z)$ as FPS and $A(z)$ and $B(z)$ converge as power series for $|z| < R$, then $A(z)=B(z)$ as power series

For instance, $\sum\limits_{n\geq 0} n! z^n$ is a FPS. It converges only at 0 as a power series
:::

Why are FPS useful?

:::example Towers of Hanoi
Discs of different sizes on three pegs. Goal: move discs to another peg, but no disc is allowed to be under a larger disc, and we may only move one disc at a time.

Recurrence for number of required moves $a_n$ to move $n$ discs to a different peg.

First move smaller $n-1$ discs to other peg, then move largest disc to third peg, and then move the $n-1$ discs on top of that.

$a_n = 2 a_{n-1} + 1$ and $a_0$ = 0, but we want an explicit formula for $a_n$:

\begin{itemize}
	\item $a_n = 2 a_{n-1} + 1 | z^n$
	\item $a_n z^n = 2 a_{n-1} z^n + z^n | \sum$
	\item $\underbrace{\sum a_n z^n}_{A(z)} = 2 \underbrace{\sum a_{n-1} z^n}_{zA(z)} + \underbrace{\sum z^n}_{\frac{1}{1-z}}$
	\item $A(z)-a_0 = 2zA(z) + \frac{1}{1-z} - 1$
	\item $A(z)(1-2z) = a_0 + \frac{1}{1-z}-1 = \frac{z}{1-z}$
	\item $A(z) = \frac{z}{(1-z)(1-2z)} = \frac{-1}{1-z} + \frac{1}{1-2z}$
	\item $A(z) = - \sum z^n + \sum 2^n z^n = \sum (2^n-1)z^n$
	\item $\Rightarrow a_n = 2^n -1$
\end{itemize}

:::

:::example Solving Recurrences with Generating Functions
$F_0 = 0, F_1 = 1, F_{n+2} = F_{n+1} + F_n$

\begin{itemize}
	\item $F(z) := \sum F_n z^n$
	\item $\sum F_{n+2}z^{n+2} = \sum F_{n+1}z^{n+2} + F_n z^{n+2}$
	\item $F(z) - F_0 -F_1z = z(F(z)-F_0) + z^2F(z)$
	\item $F(z)(1-z-z^2) = F_0 + z(F_1-F_0)$
\end{itemize}
:::

:::comment
	---------------------------------------------------------
	------------------ lecture 10 ---------------------------
	---------------------------------------------------------
:::

In general $a_{n+k} + q_1 a_{n+k-1} + \cdots q_k a_n = 0$ for $n\geq 0$, $a_0,\dots,a_{k-1}$ are given as initial conditions


\begin{align*}
	A(z) &= \sum\limits_{n\geq0} a_nz^z \\
	\sum\limits_{n\geq0} a_{n+k} z^{n+k} + q_1 \sum a_{n+k-1} z^{n+k} + \cdots + q_k \sum a_n z^{n+k} &= 0 \\
	A(z)-a_0-a_1z-\cdots-a_{k-1}z^{k-1} + q_1 z ( A(z) - \sum\limits_{i=0}^{k-2} a_i z^i) + \cdots q_k z^k  A(z) &= 0\\
	A(z)\underbrace{(1+q_1 z + \cdots q_k z^k)}\limits_{q(z)} &= p(z)
\end{align*}

with $p(z)$ a polynomial of degree at most $k-1$. Essentially, $p(z)$ contains the initial conditions while $q(z)$ describes the recurrence.

Then, $A(z) = \frac{p(z)}{q(z)}$, which is a reational function! (very nice)

Partial fraction decomposition:
\begin{enumerate}
	\item find roots of $q(z) = \prod\limits_{i=1}^{r} (z-z_i)^{\lambda_i}$, $\sum\lambda_i = l$
	\item Ansatz: $\frac{p(z)}{q(z)} = \sum\limits_{i=1}^{r} \sum\limits_{j=1}^{\lambda_i} \frac{\tilde{A}_{ij}}{(z-z_i)^j}$
	\item expand to generating function: $\sum\limits_{i=1}^{r} \sum\limits_{j=1}^{\lambda_i} \frac{A_{ij}}{(1-z/z_i)^j}$
	\item $\sum\limits_{n\geq 0} \underbrace{(A_{11} + \binom{n+1}{1} A_{12} + \cdots + \binom{n+\lambda_1 -1}{\lambda_1} A_{1\lambda_1})}\limits_{p_1(n)}(\frac{z}{z_1})^n + \cdots + \sum\dots$
	\item $ = \sum\underbrace{(p_1(n)(\frac{1}{z_1})^n + \cdots + p_r(n) (\frac{1}{z_r})^n)}\limits_{=a_n}z^n$
\end{enumerate}


:::definition Characteristic Polynomial
	$\chi(z) := z^k + q_1 z^{k-1} + \cdots + q_k$ is the characterisitc polynomial of the recurrence relation.

	($\chi(z) = q(z)|_{z^k n \rightarrow z^n-k}$)

	$\chi(z) = \prod\limits_{i = 1} ^r (z-\frac{1}{z_i})^{\lambda_i}$
:::

:::example Characteristic Polynomial of Fibonacci Sequence
	$a_n = \frac{1}{\sqrt{5}}$
	TODO{finish formula}
:::

## Unlabelled Enumeration

:::definition Binary Trees
	A binary tree is a rooted tree where each node has no successors or 2 successors.
:::

:::definition Set of all Binary Trees
	$\mathcal{B}$ is the set of all binary trees

	$\mathcal{B} = \{\cdot\} \cup \{\}$
	TODO{finish depiction}

	$\mathcal{B}(z) = \sum\limits_{n\geq0} b_n z^n$ where $b_n$ is the number of binary trees with $n$ internal nodes, $b_0 = 1$, $b_1 = 1$, $b_2 = 2$
:::


\begin{itemize}
	\item $\mathcal{B}(z) = 1 + z\mathcal{B}^2(z)$
	\item $\mathcal{B} = \frac{1-\sqrt{1-4z}}{2z} = 1+z+2z^2+5z^3 + 14z^4 + 42z^5 + \dots$
\end{itemize}

### Dictionary for unlabelled structures

:::definition
	$A(z) = \sum\limits_{n\geq0} \text{\#elements of size }n \cdot z^n$
:::

\begin{itemize}
	\item $(\mathcal{A} \cup \mathcal{B})(z) = A(z) + B(z)$
	\item $(A \times B)(z) = A(z)\cdots B(z)$, (size of $(a,b)$ is the size of $a$ plus size of $b$)
	\item $(sequences of objects in A)(z) = 1 + A(z) + A^2(z) + \cdots = \frac{1}{1-A(z)}$
\end{itemize}

:::example Sequences of Ones and Twos
	Ones have size 1, twos have size 2.

	\begin{itemize}
		\item $\varnothing$
		\item $1$
		\item ${\color{red}1+1}, 2$
		\item ${\color{blue}1+1+1}, {\color{red}1+2}, {\color{red}2+1}$
		\item ${\color{green}1+1+1+1}, {\color{blue}1+1+2}, {\color{blue}1+2+1}, {\color{blue}2+1+1}, {\color{red}2+2}$
		\item $\dots$
	\end{itemize}
	
	$1 + {\color{red}(z+z^2)^2} + {\color{blue}(z+z^2)^3} + {\color{green}(z+z^2)^4} + \cdots = \frac{1}{1-(z+z^2)}$
:::

:::example
	We have read, blue and yellow balls. $\underbrace{\text{2 or 3 red ones}}\limits_{r^2+r^3}$, $\underbrace{\text{at least one blue}}\limits_{b+b^2+b^3+\cdots = \frac{b}{1-b}}$ and $\underbrace{\text{at most one yellow}}\limits_{1+y}$. We have $n$ ball. How many possibilities are there?
	
	$\Rightarrow A(z) = ((rz)^2 + (rz)^3) \frac{bz}{1-bz}(1+yz)$
	
	We want to find $[z^n] A(z) = $ generating function in $r,b,y$
:::

:::example Combinations without Repetitions
	Balls $a_1, a_2, \dots, a_N$
	Select balls, but no ball twice, generating function:
	
	$(1+a_1)(1+a_2)\cdots(1+a_N)$, $a_i:= z$: $(1+z)^N = \sum\limits_n\geq0 \binom{N}{n} z^n$
	
	If we allow repetition: $(\sum a_1^n) (\sum a_2^n) \cdots (\sum a_N^n) \rightarrow (\frac{1}{1-z})^N = \sum\binom{n+N-1}{n} z^n$
:::





