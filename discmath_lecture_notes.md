---
summary-type: zusammenfassung
title: "**Lecture Notes: \linebreak Discrete Mathematics**"
...

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

