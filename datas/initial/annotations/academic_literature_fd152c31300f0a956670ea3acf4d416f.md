# The Projective Linear Supergroup and the SUSY-preserving automorphisms of $\mathbb{P}^{\mid 1}$ 

R. Fioresi ${ }^{\dagger}$, S. D. Kwok ${ }^{\star}$<br>${ }^{\dagger}$ Dipartimento di Matematica, Università di Bologna<br>Piazza di Porta S. Donato, 5. 40126 Bologna. Italy.<br>e-mail: rita.fioresi@UniBo.it<br>* Mathematics Research Unit, University of Luxembourg<br>6, Rue Richard Coudenhove-Kalergi, L-1359, Luxembourg<br>e-mail: stephen.kwok@uni.lu


#### Abstract

The purpose of this paper is to describe the projective linear supergroup, its relation with the automorphisms of the projective superspace and to determine the supergroup of SUSY preserving automorphisms of $\mathbb{P}^{|| 1}$.


## 1 Introduction

The works of Manin [13, 14] and more recently of Witten et al. [16, 44 have drawn attention to projective supergeometry and more specifically to SUSY curves and their moduli superspaces.

In this paper we study the automorphisms of the projective superspace $\mathbb{P}^{m \mid n}$ and its SUSY-preserving subsupergroup. We start by defining the projective linear supergroup $\mathrm{PGL}_{m \mid n}$, using the functor of points formalism, and then we show that this supergroup functor is indeed representable, that is, it is the functor of points of a superscheme. We achieve this by realizing $\mathrm{PGL}_{m \mid n}$ as a closed subsupergroup scheme of $\mathrm{GL}_{m^{2}+n^{2} \mid 2 m n}$, mimicking the ordinary procedure.

In relating this supergroup scheme to the automorphism supergroup of $\mathbb{P}^{m \mid n}$ we encounter a difficulty, not present in the ordinary setting, namely the fact that the Picard group of the projective superspace is not known in general and involves some difficulties. This is a consequence of the fact that the supergroup of automorphism of the projective superspace is larger than $\mathrm{PGL}_{m \mid n}$ for $n>1$. Neverthless, going to the special case of $n=1$, we are
able to give quite explicitly the projective linear supergroup and to prove it coincides with the automorphisms of the projective superspace.

The question of singling out the SUSY-preserving automorphisms inside this supergroup was already settled over the complex field by Manin [13] and Witten [16], we extend their considerations to an arbitrary algebraically closed field $k$, $\operatorname{char}(k) \neq 2$, and provide some extra details of their proofs.

The organization of this paper is as follows. In Sec. 2 we start by reviewing some generally known facts on the projective superspace and its functor of points to establish our notation. We then discuss line bundles and projective morphisms, proving, in Prop. [2.3, that the Picard group of $\mathbb{P}^{m \mid 1}$ is $\mathbb{Z}$. To our knowledge this result is new and gives insight into projective supergeometry. In Sec. 3 we define the projective linear supergroup in terms of functor of points and we prove its representability by realizing it as a closed subsuperscheme of the general linear supergroup. Then, in Sec. [4 we prove that the projective linear supergroup is the supergroup of automorphisms of the projective superspace in the case of one odd dimension. Though the approach in both Sec. 3 and 4 resembles closely the ordinary one, the results are novel in the supergeometric context. In Sec. [5, we use the machinery developed previously to prove that the subsupergroup of $\operatorname{Aut}\left(\mathbb{P}^{1} \mid 1\right)$ of SUSY preserving automorphisms of $\mathbb{P}^{1 \mid 1}$ consists precisely of the irreducible component $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$ of the 2|1-symplecticorthogonal supergroup $\mathrm{SpO}_{2 \mid 1}$ containing the identity. This section is a generalization of the claims made by Manin in [13] regarding complex supergeometry and provides proofs for such claims for a generic algebraically closed field.

Acknowledgements. We are indebted to Prof. D. Gaitsgory for clarifying to us the structure of line bundles over $\mathbb{P}_{A}^{n}$ in the ordinary setting. We also thank Prof. L. Migliorini for helpful discussions. We are also grateful to the anonymous Referee for his/her suggestions and remarks on the paper.

## 2 The projective superspace $\mathbb{P}^{m \mid n}$

In this section we want to recall different, but equivalent definitions of projective superspace and we describe the line bundles on it. For all of our notation and main definitions of supergeometry, we refer the reader to [14, 3, 1].

Let $k$ be our ground ring.

We recall that, by definition, the functor of points of a superscheme $X=$ $\left(|X|, \mathcal{O}_{X}\right)$ is the functor:

$X:(\text { sschemes })^{o} \longrightarrow($ sets $), \quad X(S)=\operatorname{Hom}_{\text {(sschemes) }}(S, X), \quad X(\phi)(f)=f \circ \phi$

where (sschemes) denotes the category of superschemes (it is customary to use the same letter for $X$ and its functor of points). Equivalently (see [1] Ch. 10), we can view the functor of points of $X$ as: $X:($ salg $) \longrightarrow$ (sets):

$$
X(R)=\operatorname{Hom}_{\text {(sschemes) }}(\underline{\operatorname{Spec}} R, X), \quad X(\phi)(f)=f \circ \underline{\operatorname{Spec}}(\phi)
$$

where (salg) denotes the category of superalgebras (over $k$ ), (we shall use the same letter also for this functor). In fact the functor of points of a superscheme is determined by its behaviour on the affine superscheme subcategory, which in turn is equivalent to the category of superalgebras (see [1] Ch. 10, Theorem 10.2.5). If $X=\underline{\operatorname{Spec}} \mathcal{O}(X)$, that is $X$ is affine, we have that

$$
X(R)=\operatorname{Hom}_{\text {(sschemes) }}(\underline{\operatorname{Spec}} R, X)=\operatorname{Hom}_{\text {(salg) }}(\mathcal{O}(X), R)
$$

where $\mathcal{O}(X)$ denotes the superalgebra of global sections of the sheaf of superalgebras $\mathcal{O}_{X}$. We say that $X(R)$ are the $R$-points of the superscheme $X$.

The algebraic superscheme $\mathbb{P}^{m \mid n}$ is defined as the patching of the $m+1$ affine superspaces $U_{i}=\underline{\operatorname{Spec}} \mathcal{O}\left(U_{i}\right)$, with $\mathcal{O}\left(U_{i}\right)=\underline{\operatorname{Spec}} k\left[x_{0}^{i}, \ldots, \widehat{x_{i}^{i}}, \ldots\right.$, $\left.x_{m}^{i}, \xi_{1}^{i}, \ldots, \xi_{n}^{i}\right]$ through the change of charts:

$$
\begin{array}{rlcc}
\phi_{i j}: \mathcal{O}\left(U_{j}\right)\left[\left(x_{i}^{j}\right)^{-1}\right] & \mapsto & \mathcal{O}\left(U_{i}\right)\left[\left(x_{j}^{i}\right)^{-1}\right] \\
x_{k}^{j} & \mapsto & x_{k}^{i} / x_{j}^{i} \\
x_{i}^{j} & \mapsto & 1 / x_{j}^{i} \\
\xi^{j} & \mapsto & \xi_{i}^{i} / x_{i}^{i}
\end{array}
$$

(as usual $\widehat{x_{i}^{i}}$ means that we are omitting the indeterminate $x_{i}^{i}$ ). Notice that $\mathcal{O}\left(U_{j}\right)\left[\left(x_{i}^{j}\right)^{-1}\right]$ is the superalgebra representing the open subscheme $U_{j} \cap U_{i}$ of $U_{j}$ (and similarly for $\mathcal{O}\left(U_{i}\right)\left[\left(x_{j}^{i}\right)^{-1}\right]$ ).

Proposition 2.1. The $R$-points of $\mathbb{P}^{m \mid n}, R \in(\mathrm{salg})$ are given equivalently by:

1. 

$$
\begin{gathered}
\mathbb{P}^{m \mid n}(R)=\left\{\alpha: R^{m+1 \mid n} \longrightarrow L, R \text {-linear, surjective }\right\} / \sim, \\
\mathbb{P}^{m \mid n}(\psi): R^{m+1 \mid n} \otimes_{R} T \longrightarrow L \otimes_{R} T
\end{gathered}
$$

where $L$ is locally free of rank $1 \mid 0, \psi: R \longrightarrow T$ and $\alpha: R^{m+1 \mid n} \longrightarrow$ $L \sim \alpha^{\prime}: R^{m+1 \mid n} \longrightarrow L^{\prime}$ if and only if $\operatorname{ker}(\alpha)=\operatorname{ker}\left(\alpha^{\prime}\right)$ (or equivalently, $\alpha \sim \alpha^{\prime}$ if they differ by an automorphism of $L$ by multiplication of an element in $\left.R^{\times}\right)$.

2. 

$$
\begin{gathered}
\mathbb{P}^{m \mid n}(R)=\left\{\alpha: L \hookrightarrow R^{m+1 \mid n} R \text {-linear, injective }\right\} \\
\mathbb{P}^{m \mid n}(\psi): L \otimes_{R} T \longrightarrow R^{m+1 \mid n} \otimes_{R} T
\end{gathered}
$$

where $L$ is locally free of rank $1 \mid 0$.

Let $\mathcal{O}_{S}^{m+1 \mid n}=\mathcal{O}_{S} \otimes k^{m+1 \mid n}$. The $S$-points of $\mathbb{P}^{m \mid n}, S \in$ (sschemes) are given equivalently by:

(a) $\mathbb{P}^{m \mid n}(S)=\left\{\alpha: \mathcal{O}_{S}^{m+1 \mid n} \longrightarrow \mathcal{L}\right.$, surjective $\} / \sim, \mathbb{P}^{m \mid n}(\psi):\left(\psi^{*} \mathcal{O}_{S}\right)^{m+1 \mid n} \longrightarrow$ $\psi^{*}(\mathcal{L})$ where $\psi: T \longrightarrow S, \mathcal{L}$ is a line bundle on $S$ (of rank $1 \mid 0$ ) and $\alpha: \mathcal{O}_{S}^{m+1 \mid n} \longrightarrow \mathcal{L} \sim \alpha^{\prime}: \mathcal{O}_{S}^{m+1 \mid n} \longrightarrow \mathcal{L}^{\prime}:$ if and only if $\operatorname{ker}(\alpha)=\operatorname{ker}\left(\alpha^{\prime}\right)$ (or equivalently, $\alpha \sim \alpha^{\prime}$ if they differ by an automorphism of $\mathcal{L}$ by multiplication of an element in $\left.\mathcal{O}_{S}^{\times}\right)$.

(b) $\mathbb{P}^{m \mid n}(S)=\left\{\alpha: \mathcal{L} \hookrightarrow \mathcal{O}_{S}^{m+1 \mid n}\right\}, \quad \mathbb{P}^{m \mid n}(\psi): \psi^{*} \mathcal{L} \longrightarrow\left(\psi^{*} \mathcal{O}_{S}\right)^{m+1 \mid n}$

Proof. The proof relative to (1) and (a) works as in the ordinary setting and it is detailed in [1] Ch. 10. The equivalence with (2) and (b) is immediate. The equivalence (1) and (2) is essentially the same as in the ordinary setting (see [5] Ch. III, Sec. 2 Prop. III-40, Cor. III-42).

For every $A \in(\mathrm{salg})$, let $(\mathrm{salg})_{A}$ denote the category of superalgebras over $A$. We will need to consider also $\mathbb{P}_{A}^{m \mid n}$ that is the projective superspace over a base $A \in(\mathrm{salg})$. This means that we are considering the superscheme obtained by patching the affine superspaces $U_{i}=A\left[x_{j}^{i}, \xi_{k}^{i}\right], i, j=0, \ldots, m$, $j \neq i, k=1, \ldots, n$ as above. For example, in the Case (2) of Prop. 2.1 each of the $T$-points, $T \in(\mathrm{salg})_{A}$, is identified with a morphisms $\alpha: L \longrightarrow T^{m+1 \mid n}$
of $A$-modules, where $L$ and $T^{m+1 \mid n}$ are $T$-modules which become $A$-modules via the $\operatorname{map} \phi: A \longrightarrow T$ :

![](https://cdn.mathpix.com/cropped/2024_05_09_d5a781ccd3019273404eg-05.jpg?height=88&width=1077&top_left_y=550&top_left_x=513)

Notice that the functor of points of $\mathbb{P}_{A}^{m \mid n}$ is defined on the category of $A$ superalgebras or equivalently on the category of $A$-superschemes (that is superschemes equipped with a morphism to the superscheme $\underline{\operatorname{Spec}} A$ and morphisms compatible with it).

We leave to the reader the generalization of the other cases of Prop. 2.1 since it is straightforward.

We end this section with some observations on line bundles and morphisms on $\mathbb{P}_{A}^{m \mid n}$. We start with a result completely similar to the ordinary counterpart, that we leave to the reader as a simple exercise (see also [1] Ch. $9)$.

Proposition 2.2. We have a bijective correspondence between the following:

1. The set of equivalence classes of $m+n+2$-tuples $\left(L, s_{0}, \ldots, s_{m}, \sigma_{1}, \ldots, \sigma_{n}\right)$, where $L$ is a line bundle on $\mathbb{P}_{A}^{m \mid n}$ globally generated by the global sections $s_{0}, \ldots, s_{m}, \sigma_{1}, \ldots, \sigma_{n}$ of $L$, under the relation $\left(L, s_{0}, \ldots s_{m}, \sigma_{1}, \ldots \sigma_{n}\right) \sim$ $\left(L, s_{0}^{\prime}, \ldots s_{m}^{\prime}, \sigma_{1}^{\prime}, \ldots \sigma_{n}^{\prime}\right)$ if and only if there exists some $c \in \mathcal{O}\left(\mathbb{P}_{A}^{m \mid n}\right)_{0}^{*}$ such that $s_{i}^{\prime}=c s_{i}, \sigma_{i}^{\prime}=c \sigma_{i}$ for all $i$.
2. The set of $A$-morphisms $\mathbb{P}_{A}^{m \mid n} \rightarrow \mathbb{P}_{A}^{m \mid n}$.

In the ordinary setting we have that a line bundle on $\mathbb{P}_{A}^{m}$ is of the form $\mathcal{O}(n) \otimes \mathcal{L}$, where $\mathcal{L}$ is a line bundle on $\operatorname{Spec} A$. This non trivial fact is still true in supergeometry for $\mathbb{P}_{A}^{m / 1}$, and it will turn out to be crucial in our treatment.

Proposition 2.3. Every line bundle on $\mathbb{P}_{A}^{m \mid 1}$ is isomorphic to $\mathcal{O}(n) \otimes \mathcal{L}$, where $\mathcal{L}$ is a line bundle on $\underline{\operatorname{Spec}} A$.

Proof. A line bundle on $\mathbb{P}_{A}^{m \mid 1}$ is determined once we know its transition functions, say $g_{i j} \in \mathcal{O}_{\mathbb{P}_{A}^{m \mid 1}}\left(U_{i} \cup U_{j}\right)_{0}^{*}$, which are even. We then need to prove that any such set of transition functions is equivalent, up to a coboundary, to a set of transition functions for a line bundle of the form $\mathcal{O}(n) \otimes \mathcal{L}$, for $\mathcal{L}$ a line bundle on $\operatorname{Spec} A$. In other words we need to show

$$
\left.\left.h_{i}\right|_{U_{i} \cap U_{j}} g_{i j} h_{j}^{-1}\right|_{U_{i} \cap U_{j}}=\left(x_{j}^{i}\right)^{n}, \quad h_{i} \in \mathcal{O}_{\mathbb{P}_{A}^{m \mid 1}}\left(U_{i}\right)_{0}^{*}
$$

Notice that

$$
\mathcal{O}_{\mathbb{P}_{A}^{m \mid 1}}\left(U_{p}\right)^{*}=\left(A\left[x_{k}^{p}, \xi^{p}\right]\right)_{0}^{*}=\left(A\left[\xi^{p}\right]\left[x_{k}^{p}\right]\right)_{0}^{*}, \quad p=i, j
$$

Since $\phi_{i j}\left(\xi^{j}\right)=\frac{\xi^{i}}{x_{j}^{i}}, \phi_{i j}\left(x_{i}^{j}\right)=1 / x_{j}^{i}$ and $\phi_{i j}\left(x_{k}^{j}\right)=\frac{x_{k}^{i}}{x_{j}^{i}}\left(\phi_{i j}\right.$ being the change of chart as in (II), we can view the restrictions of the $h_{p}$ 's $(p=i, j)$ to $U_{i} \cap U_{j}$, through this identification, as both belonging to $\left(A\left[\xi^{i}\right]\left[x_{j}^{i},\left(x_{j}^{i}\right)^{-1}\right]\right)_{0}^{*}$. We now apply the classical result and obtain $h_{p}^{\prime} \in\left(A\left[\xi^{i}\right]\left[x_{j}^{i},\left(x_{j}^{i}\right)^{-1}\right]\right)_{0}^{*}$ such that

$$
h_{i}^{\prime} g_{i j}\left(h_{j}^{\prime}\right)^{-1}=\left(x_{j}^{i}\right)^{n}
$$

The $h_{p}^{\prime}$ 's thus obtained are not yet the sections we want; since the odd dimension is one by hypothesis, the most general possible form for $h_{j}^{\prime}$ is

$$
h_{j}^{\prime}=a_{0}+\alpha_{0} \xi^{i}+\sum_{K} a_{K} x_{K}^{i}\left(x_{j}^{i}\right)^{-|K|}+\sum_{L} \alpha_{L} x_{L}^{i}\left(x_{j}^{i}\right)^{-|L|} \xi^{i}+\sum_{k} \beta_{k}\left(x_{j}^{i}\right)^{-k} \xi^{i}
$$

where $K$ and $L$ are multiindices, $K=\left(k_{1}, \ldots, k_{r}\right), k_{l} \neq j(r \in \mathbb{N})$ and $x_{K}^{i}:=$ $x_{k_{1}}^{i} \ldots x_{k_{r}}^{i}$ (similarly for $L$ ).

In order to eliminate the term $\alpha_{0} \xi^{i}$ which is not well defined on $U_{j}$, we define:

$$
h_{i}:=\left(a_{0}+\alpha_{0} \xi^{i}\right) h_{i}^{\prime}, \quad h_{j}:=\left(a_{0}^{-1}-a_{0}^{-2} \alpha_{0} \xi^{i}\right) h_{j}^{\prime}
$$

and this gives the required sections.

Notice that it was absolutely fundamental for our argument that there is only one odd dimension. This calculation will give us key information when we want to determine the automorphism supergroup of the projective linear supergroup.

## 3 The Projective Linear Supergroup

In this section we want to define the supergroup functor of the projective linear supergroup and to show it is representable by producing an embedding of it as a closed subgroup into the general linear supergroup.

Let $\underline{\mathrm{M}}_{m \mid n}(R)$ denote the associative superalgebra of supermatrices of order $m \mid n$ by $m \mid n$ with entries in a commutative superalgebra $R$. More intrinsically, $\underline{\mathrm{M}}_{m \mid n}(R)=\underline{\operatorname{End}}_{R}\left(R^{m \mid n}\right)$.

Definition 3.1. The automorphism supergroup of supermatrices is the supergroup functor $\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right):(\mathrm{salg}) \longrightarrow(\mathrm{grps})$

$$
\begin{aligned}
& {\left[\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)\right](R):=\left\{f: \underline{\mathrm{M}}_{m \mid n}(R) \rightarrow \underline{\mathrm{M}}_{m \mid n}(R) \mid\right.} \\
&f \text { is an } R \text {-superalgebra automorphism }\} .
\end{aligned}
$$

In analogy with the ordinary setting we also will call this supergroup functor the projective linear supergroup and denote it with $\operatorname{PGL}(m \mid n)$.

Since $\underline{\mathrm{M}}_{m \mid n}(R)$ is itself a free $R$-module of rank $M \mid N$, where $M=m^{2}+n^{2}$ and $N=2 m n$, $\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)$ is a subfunctor of $\mathrm{GL}_{M \mid N}$ in a natural way. We want to prove this is the functor of points of a closed subsuperscheme of $\mathrm{GL}_{M \mid N}$. Before proceeding we need a lemma characterizing the morphisms of the superalgebra of supermatrices.

Lemma 3.2. 1. An $R$-linear parity preserving map $\psi: \underline{\mathrm{M}}_{m \mid n}(R) \longrightarrow$ $\underline{\mathrm{M}}_{m \mid n}(R)$ is a morphism of the superalgebra of supermatrices $\underline{\mathrm{M}}_{m \mid n}(R)$ if and only if

(a) $\psi(\mathrm{id})=\mathrm{id}$

(b) $\psi\left(e_{i j}\right) \psi\left(e_{k l}\right)=\delta_{k j} \psi\left(e_{i l}\right)$,

where $e_{i j}$ are the elementary matrices in $\underline{\mathrm{M}}_{m \mid n}(R)$.

2. If $R$ is a local superalgebra, all of the automorphisms of the superalgebra $\underline{\mathrm{M}}_{m \mid n}(R)$ are of the form:

$$
\begin{aligned}
\mathrm{M}_{m \mid n}(R) & \longrightarrow \mathrm{M}_{m \mid n}(R) \\
(T, X) & \mapsto T X T^{-1}
\end{aligned}
$$

for a suitable $T \in \mathrm{GL}_{m \mid n}(R)$.
3. $\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)$ is a closed subsuperscheme of $\mathrm{GL}_{M \mid N}=\underline{\operatorname{Spec}} k\left[x_{i j, k l}\right]\left[d_{1}^{-1}, d_{2}^{-1}\right]$, $M=m^{2}+n^{2}$ and $N=2 m n$, defined by the equations:

$$
\sum_{k} x_{i j, k k}=\delta_{i j}, \quad \sum_{s} x_{r s, i j} x_{s t, k l}=\delta_{j k} x_{r t, i l},
$$

where $\mathrm{GL}_{M \mid N}(R)$ is identified with the parity preserving automorphisms of the free $R$-module $\underline{\mathrm{M}}_{m \mid n}(R)$.

Proof. (1). If $\psi$ is an $R$-superalgebra endomorphism of $\underline{\mathrm{M}}_{m \mid n}(R)$ then the two relations are obviously satisfied and vice-versa.

(2). Now assume $\psi$ is an automorphism of $\mathrm{M}_{m \mid n}(R), R$ local, which satisfies the relations $(a)$ and $(b)$. We need to find $T \in \mathrm{GL}_{m \mid n}(R)$ such that $\psi\left(e_{i j}\right)=$ $T e_{i j} T^{-1}$. This is an application of super Morita theory (see [12]), however we shall recall the main idea to make this proof self-contained. By (a) and (b) we have that

$$
\sum \psi\left(e_{i i}\right)=\mathrm{id}, \quad \psi\left(e_{i i}\right)^{2}=\psi\left(e_{i i}\right), \quad \psi\left(e_{i i}\right) \psi\left(e_{j j}\right)=0, i \neq j
$$

hence we can write

$$
R^{m \mid n}=\oplus \psi\left(e_{i i}\right) R^{m \mid n}
$$

Since by $(b) \psi\left(e_{j i}\right) \psi\left(e_{i i}\right)=\psi\left(e_{j i}\right)=\psi\left(e_{j j}\right) \psi\left(e_{j i}\right)$ we have that $\psi\left(e_{j i}\right)$ : $\psi\left(e_{i i}\right) R^{m \mid n} \longrightarrow \psi\left(e_{j j}\right) R^{m \mid n}$ (recall that $R$ is local so projective implies free). Hence there exists a basis $\left\{t_{i}\right\}$ of the free module $R^{m \mid n}$ such that

$$
\psi\left(e_{i i}\right) R^{m \mid n}=\operatorname{span}_{R}\left\{t_{i}\right\}
$$

and $\psi\left(e_{j i}\right) t_{i}=t_{j}$. Let $T$ be the matrix whose columns are the $t_{i}$ 's, $T=\sum t_{i} \otimes e_{i}^{*}$, $T^{-1}=\sum e_{i} \otimes t_{i}^{*}$. It is then immediate to verify $\psi\left(e_{i j}\right)=T e_{i j} T^{-1}$.

(3). This is immediate from (1).

Let us view the multiplicative algebraic supergroup $\mathbb{G}_{m}^{1 \mid 0}:(\mathrm{salg}) \longrightarrow$ (grps) as the following subsupergroup of $\mathrm{GL}_{m \mid n}$ :

$$
\mathbb{G}_{m}^{1 \mid 0}(R)=\left\{a I \mid a \in R_{0}^{*}\right\} \subset \mathrm{GL}_{m \mid n}(R)
$$

(Here $I$ denotes the identity matrix).

We shall not specify the definition on the arrows whenever it is clear, as in this case.

Definition 3.3. We define the supergroup functor: $\widehat{\mathrm{PGL}}_{m \mid n}:(\mathrm{salg}) \longrightarrow$ (grps)

$$
\widehat{\mathrm{PGL}}_{m \mid n}(R)=\mathrm{GL}_{m \mid n}(R) / \mathbb{G}_{m}^{1 \mid 0}(R)
$$

and we call its sheafification (as customary) $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$.

We wish to show that $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$ is representable and coincides with the projective linear supergroup, that is with the automorphism supergroup of supermatrices.

Definition 3.4. We say that a functor $F:(\operatorname{salg}) \longrightarrow(\mathrm{grps})$ is stalky if for any superalgebra $R$, the natural map

$$
\underset{f \notin \mathfrak{p}}{\lim } F\left(R_{f}\right) \longrightarrow F\left(R_{\mathfrak{p}}\right)
$$

is an isomorphism for any prime ideal $\mathfrak{p} \in R_{0}$.

The next two lemmas are standard and their proof is the same as in the ordinary case, see [15].

Lemma 3.5. $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$ and $\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)$ are stalky.

Lemma 3.6. Let $\mathcal{F}, \mathcal{G}$ be stalky Zariski sheaves $(\mathrm{salg}) \rightarrow(\operatorname{grps}), \alpha: \mathcal{F} \rightarrow \mathcal{G} a$ morphism. If $\alpha_{R}: \mathcal{F}(R) \rightarrow \mathcal{G}(R)$ is an isomorphism for all local superrings $R$, then $\alpha$ is an isomorphism of sheaves.

Proposition 3.7. The supergroup functor $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$ is representable and is realized as the closed subsupergroup $\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)$ of $\mathrm{GL}_{M \mid N}$ for $M=m^{2}+n^{2}$ and $N=2 m n$.

Proof. We need to establish an isomorphism of sheaves between $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$ and a closed subsupergroup of $\mathrm{GL}_{M \mid N}$. We will first give a morphism of sheaves and then show it is an isomorphism on local superalgebras; since $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$ is a stalky sheaf, this will be enough. We start by giving a morphism of presheaves $\widehat{\mathrm{PGL}}_{m \mid n}$ and $\mathrm{GL}_{M \mid N}$; since $\mathrm{GL}_{M \mid N}$ is a sheaf then such a morphism will factor through the sheafification of $\overline{\mathrm{PGL}}_{m \mid n}$ thus giving us a sheaf morphism.

Consider the action of $\mathrm{GL}_{M \mid N}$ on supermatrices $\underline{\mathrm{M}}_{m \mid n}$, where $M=m^{2}+n^{2}$, $N=2 m n:$

$$
\begin{aligned}
\phi: \mathrm{GL}_{m \mid n}(R) \times \underline{\mathrm{M}}_{m \mid n}(R) & \longrightarrow \underline{\mathrm{M}}_{m \mid n}(R) \\
(T, X) & \mapsto \quad T X T^{-1}
\end{aligned}
$$

This clearly factors through $\mathbb{G}_{m}^{1 \mid 0}(R)$ hence gives a well defined action $\rho$ of $\widehat{\mathrm{PGL}}_{m \mid n}$ and then in turn of $\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}$ (see comments at the beginning of the proof). Since $X \mapsto T X T^{-1}, T \in\left(\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}\right)(R)$ is a parity preserving $R$-superalgebra morphism, it is immediate to verify we have a morphism of sheaves

$$
\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0} \rightarrow \operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)
$$

By the first part of Lemma 3.2, Aut $\left(\underline{\mathrm{M}}_{m \mid n}\right)$ is represented by the closed subsuperscheme $H$ of $\mathrm{GL}_{M \mid N}=\underline{\operatorname{Spec}} k\left[x_{i j, k l}\right]\left[d_{1}^{-1}, d_{2}^{-1}\right]$ defined by the equations:

$$
\sum_{k} x_{i j, k k}=\delta_{i j}, \quad \sum_{s} x_{r s, i j} x_{s t, k l}=\delta_{j k} x_{r t, i l}
$$

(Here $d_{i}$ denotes as usual the determinants of the diagonal blocks of indeterminates). We want to show that the group homomorphism $\left(\mathrm{GL}_{m \mid n} / \mathbb{G}^{1 \mid 0}\right)(R) \rightarrow$ $\left[\operatorname{Aut}\left(\underline{\mathrm{M}}_{m \mid n}\right)\right](R)$ is an isomorphism for $R$ local. $\psi \in \mathrm{GL}_{M \mid N}(R)$ belongs to $H(R)$ if and only its entries $\psi\left(e_{i j}\right)_{k l}$ satisfy the above relations (4) (where in our convention $x_{i j, k l}$ corresponds to $\left.\psi\left(e_{i j}\right)_{k l}\right)$. Hence by Lemma 3.2 we have the result for $R$ local. By Lemmas 3.5 and 3.6, it is true for any superalgebra $R$ and this concludes the proof.

Remark 3.8. The projective linear supergroup may also be obtained through the Chevalley supergroup recipe as detailed in [6, 7, 8]). It corresponds to the choice of the adjoint action of the Lie superalgebra $\mathfrak{s l}_{m \mid n}$. In fact one may readily check that the Lie superalgebra of $\mathrm{PGL}_{m \mid n}$ is indeed $\mathfrak{s l}_{m \mid n}$ and $\left(\mathrm{PGL}_{m \mid n}\right)_{0}=\mathrm{PGL}_{m} \times \mathrm{PGL}_{n} \times k^{\times}$.

## 4 The automorphisms of the projective superspace

We want to define the automorphism supergroup of the superscheme $\mathbb{P}^{m \mid n}$.

Definition 4.1. We define the supergroup functor of automorphisms of the projective superspace:

$$
\operatorname{Aut}\left(\mathbb{P}^{m \mid n}\right)(A):=\operatorname{Aut}_{A}\left(\mathbb{P}^{m \mid n} \times \underline{\operatorname{Spec}} A\right)=\operatorname{Aut}_{A} \mathbb{P}_{A}^{m \mid n}, \quad A \in(\mathrm{salg})
$$

Aut $\left(\mathbb{P}^{m \mid n}\right)$ is defined in an obvious way on the morphisms.

The equality in the definition is straightforward noticing that we can identify the $T$-points of $\mathbb{P}^{m \mid n} \times \operatorname{Spec} A$ and of $\mathbb{P}_{A}^{m \mid n}$. In fact a $T$-point of $\mathbb{P}^{m \mid n} \times \operatorname{Spec} A$ is a morphism $\phi: \overline{A \longrightarrow} T$ and a morphism of $A$-modules via $\phi, L \longrightarrow T^{m \mid n}$. This is exactly an element of $\mathbb{P}_{A}^{m \mid n}(T)$ and vice-versa.

An automorphism $\psi \in \operatorname{Aut}_{A} \mathbb{P}_{A}^{m \mid n}$ is a family of automorphisms $\psi_{T}$ for all $T \in(\operatorname{salg})_{A}$, which is functorial in $T . \psi_{T}: \mathbb{P}_{A}^{m \mid n}(T) \longrightarrow \mathbb{P}_{A}^{m \mid n}(T)$ must
assign to a $T$-point of $\mathbb{P}_{A}^{m \mid n}(T)$, that is a morphism $\alpha: L \longrightarrow T^{m \mid n}$, another morphism $\alpha^{\prime}: L^{\prime} \longrightarrow T^{m \mid n}$, where $L, L^{\prime}$ are projective rank $1 \mid 0 T$-modules, where the morphisms are interpreted as $A$-module morphisms. Similarly for the other characterizations of $T$-points as in Prop. 2.1.

We are now ready to relate the supergroup scheme $\mathrm{PGL}_{m \mid n}$ with the automorphisms of $\mathbb{P}^{m-1 \mid n}$.

Proposition 4.2. There is an embedding of supergroup functors $\mathrm{PGL}_{m \mid n} \rightarrow$ $\operatorname{Aut}\left(\mathbb{P}^{m-1 \mid n}\right)$.

Proof. We first establish a morphism $\phi^{\prime}: \mathrm{GL}_{m \mid n} \longrightarrow \operatorname{Aut}\left(\mathbb{P}^{m-1 \mid n}\right)$. If $X \in$ $\mathrm{GL}_{m \mid n}(A)$ and $\alpha \in \mathbb{P}_{A}^{m-1 \mid n}(T)=\left\{T^{m \mid n} \longrightarrow L\right\} / \sim, \psi: A \longrightarrow T$ we define

$$
\phi^{\prime}(X)=\alpha \circ \mathrm{GL}_{m \mid n}(\psi)(X)
$$

Clearly $\phi^{\prime}$ factors through $\mathbb{G}_{m}(A)$. Since $\operatorname{Aut}\left(\mathbb{P}^{m-1 \mid 1}\right)$ is a sheaf, we have defined a morphism

$$
\phi: \mathrm{PGL}_{m \mid n} \longrightarrow \operatorname{Aut}\left(\mathbb{P}^{m-1 \mid n}\right)
$$

The injectivity is clear.

Remark 4.3. In general we cannot expect to get an isomorphism between $\mathrm{PGL}_{m \mid n}$ and $\operatorname{Aut}\left(\mathbb{P}^{m-1 \mid n}\right)$ for $n>1$ and this is because of the peculiarity of the odd elements. Let us see this in a simple example: $\mathbb{P}^{1 / 2}$. Consider the morphism $\phi \in \mathbb{P}_{A}^{1 \mid 2}$ given on the affine pieces $U_{0}=\operatorname{Spec} A\left[u, \mu_{1}, \mu_{2}\right]$ and $U_{1}=A\left[v, \nu_{1}, \nu_{2}\right]$ by

$$
\left.\phi\right|_{U_{0}}\left(u, \mu_{1}, \mu_{2}\right)=\left(u+\mu_{1} \mu_{2}, \mu_{1}, \mu_{2}\right),\left.\quad \phi\right|_{U_{1}}\left(v, \nu_{1}, \nu_{2}\right)=\left(v-\nu_{1} \nu_{2}, \nu_{1}, \nu_{2}\right)
$$

As $\phi$ is invertible, $\phi \in \operatorname{Aut}\left(\mathbb{P}^{m \mid n}\right)(A)$, but is not obtained through an element of $\mathrm{PGL}_{2 \mid 2}(A)$. In fact the coefficient in $\left.\phi\right|_{U_{0}}$ of $\mu_{1} \mu_{2}$ in an automorphism induced by a $\mathrm{PGL}_{2 \mid 2}(A)$ transformation must be a nilpotent. Hence $\phi \notin \mathrm{PGL}_{2 \mid 2}(A)$.

We now want to show that we have an isomorphism between the projective linear supergroup and the automorphism of the super projective when $n=1$. The argument we give follows along the lines of the calculation of $\operatorname{Aut}\left(\mathbb{P}^{n}\right)$ given in [11] Ch. 2, Sec. 7.

Proposition 4.4. We have an isomorphism of supergroup functors:

$$
\mathrm{PGL}_{m+1 \mid 1} \cong \operatorname{Aut}\left(\mathbb{P}^{m \mid 1}\right)
$$

In particular, Aut $\left(\mathbb{P}^{m \mid 1}\right)$ is a supergroup scheme.

Proof. Proposition 4.2 gives us an embedding of supergroup functors $\mathrm{PGL}_{m+1 \mid 1}$ $\rightarrow \operatorname{Aut}\left(\mathbb{P}^{m \mid 1}\right)$. Now let $f \in \operatorname{Aut}\left(\mathbb{P}_{A}^{m \mid 1}\right)$ and let $g$ be its inverse. We want to show $f \in \operatorname{PGL}_{m+1 \mid 1}(A)$. The automorphism $f$ induces the two line bundle morphisms $f^{*} \mathcal{O}_{A}(1) \longrightarrow \mathcal{O}_{A}(1)$ and $g^{*} \mathcal{O}_{A}(1) \longrightarrow \mathcal{O}_{A}(1)$, where $\mathcal{O}_{A}(1):=$ $p_{1}^{*}(\mathcal{O}(1)), p_{1}: \mathbb{P}_{A}^{m / 1} \longrightarrow \mathbb{P}^{m \mid 1}$ being the natural projection. By Prop. [2.3, we know that $f^{*} \mathcal{O}_{A}(1)=\mathcal{O}(k) \otimes \mathcal{L}_{f}$ and $g^{*} \mathcal{O}_{A}(1)=\mathcal{O}(l) \otimes \mathcal{L}_{g}$. Let us choose a suitable open cover of $A$ in which both $\mathcal{L}_{f}$ and $\mathcal{L}_{g}$ are trivial. By a common abuse of notation we shall still write $A$ to denote the ring of global sections of an element of the open cover, so we in fact are replacing $A$ with its localization. With such a choice we have $f^{*} \mathcal{O}_{A}(1) \cong \mathcal{O}_{A}(k), g^{*} \mathcal{O}_{A}(1) \cong \mathcal{O}_{A}(l)$. Since $f$ and $g$ are mutually inverse, we have:

$$
\mathcal{O}_{A}(1)=\left(f^{*} \circ g^{*}\right)\left(\mathcal{O}_{A}(1)\right)=f^{*}\left(g^{*}\left(\mathcal{O}_{A}(1)\right)\right)=f^{*}\left(\mathcal{O}_{A}(l)\right)=\mathcal{O}_{A}(k l)
$$

Hence $k l=1$, whence $k=l=1$, because for $k=l=-1$ we do not have global sections.

So $f^{*}(\mathcal{O}(1)) \cong \mathcal{O}(1)$, and choosing an isomorphism $F: f^{*}(\mathcal{O}(1)) \rightarrow \mathcal{O}(1)$ yields an isomorphism of the global sections $\Gamma\left(\mathbb{P}^{m}, f^{*} \mathcal{O}_{A}(1)\right) \cong \Gamma\left(\mathbb{P}^{m}, \mathcal{O}_{A}(1)\right)$ By composing such an isomorphism with the natural isomorphism

$$
f^{*}: \Gamma\left(\mathbb{P}^{m}, \mathcal{O}_{A}(1)\right) \longrightarrow \Gamma\left(\mathbb{P}^{m}, f^{*} \mathcal{O}_{A}(1)\right)
$$

we obtain an $A$-linear automorphism

$$
T_{F}: \Gamma\left(\mathbb{P}^{m}, \mathcal{O}_{A}(1)\right) \longrightarrow \Gamma\left(\mathbb{P}^{m}, \mathcal{O}_{A}(1)\right)
$$

and identifying $\Gamma\left(\mathbb{P}^{m}, \mathcal{O}_{A}(1)\right)$ with $A^{m+1 \mid 1}$ we see that $T_{F} \in \mathrm{GL}_{m+1 \mid 1}(A)$. However, $T_{F}$ depends on $F$. Suppose $G: f^{*}(\mathcal{O}(1)) \rightarrow \mathcal{O}(1)$ is another isomorphism, then $F^{-1} \circ G$ is an automorphism of $\mathcal{O}(1)$. Since $\underline{\operatorname{Hom}}(L, L)=L^{*} \otimes L=$ $\mathcal{O}$ for any line bundle $L$, we see that an automorphism of $\mathcal{O}(1)$ is the same thing as an invertible even function on $\mathbb{P}_{A}^{m \mid 1}$, and $F$ and $G$ differ by composing with multiplication by such a function.

Therefore $f$ determines $T_{F}$ only up to multiplication by an invertible even function, i.e. $f$ uniquely determines an element $T:=\left[T_{F}\right]$ of $\operatorname{PGL}_{m+1 \mid 1}(A)$.

Now in suitable coordinates we have that $T$ induces (up to scalar multiplication) an automorphism of the $\mathbb{Z}$-graded superalgebra $A\left[z_{0}, \ldots, z_{m}, \zeta\right]$. We leave to the reader the check that $\phi(T)$ is indeed $f$.

## 5 The SUSY-preserving automorphisms of $\mathbb{P}_{k}^{1 / 1}$

In this section we want to consider those automorphisms of $\mathbb{P}_{k}^{1 \mid 1}$ which preserve its unique (up to isomorphism) SUSY structure. For all of the standard notation of supergeometry refer to [1].

Let $k$ be our ground field, $\operatorname{char}(k) \neq 2, k$ algebraically closed. All algebraic supergroups discussed below will be algebraic supergroups over $k$.

We recall that if, $X$ is a smooth algebraic supervariety over $k$ of dimension $1 \mid 1$, we define a SUSY structure on $X$ as a $0 \mid 1$ distribution $\mathcal{D}$ on $X$ such that the Frobenius map

$$
\begin{aligned}
& \mathcal{D} \otimes \mathcal{D} \longrightarrow T X / \mathcal{D} \\
& Y \otimes Z \mapsto[Y, Z] \bmod \mathcal{D}
\end{aligned}
$$

is an isomorphism (see, for example, [13] for the definition of SUSY-structure in the complex analytic case). If $X \rightarrow S$ is a smooth family of algebraic supervarieties of relative dimension $1 \mid 1$ over an algebraic $k$-supervariety $S$, then the notion of relative SUSY structure may be defined in the analogous way, as a relative distribution in the relative tangent sheaf $T X / S$. In this case we say that $X \rightarrow S$ is a relative SUSY family.

Our discussion is based on [16].

Let us start by interpreting $\mathbb{P}_{k}^{1 \mid 1}$ as a homogeneous superspace. Let $\underline{k}^{2 \mid 1}=$ $\left(k^{2}, \mathcal{O}_{\underline{k}^{2 \mid 1}}\right)$ denote the affine superspace canonically associated to the $k$-super vector space $k^{2 \mid 1}$. Let us consider the action of the algebraic group $\underline{k}^{\times}$on $\underline{k}^{2 \mid 1} \backslash\{0\}$, given in the functor of points notation by:

$$
t \cdot\left(z_{0}, z_{1}, \zeta\right)=\left(t z_{0}, t z_{1}, t \zeta\right)
$$

Consider the projection (as topological map):

$$
\pi: k^{2} \backslash\{0\} \longrightarrow k^{2} \backslash\{0\} / k^{\times} \cong \mathbb{P}^{1}
$$

Define the sheaf on the topological space $\mathbb{P}_{k}^{1}$ consisting of the $\underline{k}^{\times}$-invariant sections:

$$
\left.\mathcal{F}(U):=\mathcal{O}_{\underline{k}^{2 \mid 1}}\left(\pi^{-1}(U)\right)\right)^{\underline{\underline{k}}^{\times}}
$$

One can readily check that $\left(\mathbb{P}_{k}^{1}, \mathcal{F}\right)$ is the superscheme $\mathbb{P}_{k}^{1 \mid 1}$ as defined in Sec. 2.

Let $z_{0}, z_{1}, \zeta$ be global coordinates on $\underline{k}^{2 \mid 1}$. We now consider the Euler vector field $E=z_{0} \partial_{z_{0}}+z_{1} \partial_{z_{1}}+\zeta \partial_{\zeta}$, which represents (in the chosen coordinates) the infinitesimal generator for the $\underline{k}^{\times}$action on $\underline{k}^{2 \mid 1} \backslash\{0\}$. Since $E$ is everywhere nonsingular, it generates a trivial $1 \mid 0$ line bundle. As in the classical case, we have the Euler exact sequence of vector bundles on $\mathbb{P}_{k}^{1 / 1}$ :

$$
0 \rightarrow \mathcal{O}^{1 \mid 0} \xrightarrow{i} \mathcal{O}(1) \otimes \operatorname{Der}(S) \xrightarrow{j} T \mathbb{P}_{k}^{1 \mid 1} \rightarrow 0
$$

where $i$ is the inclusion of the trivial $1 \mid 0$ line bundle $\langle E\rangle$ with global basis the Euler vector field. Here $\operatorname{Der}(S)$ is the $k$-super vector space of $k$-linear derivations on $S:=\underline{\operatorname{Sym}}\left(\left(k^{2 \mid 1}\right)^{*}\right)$; it has as basis the derivations $\partial_{z_{i}}, \partial_{\zeta}$. Thus $\mathcal{O}(1) \otimes \operatorname{Der}(S)$ is the sheaf whose sections on $U$ are the linear vector fields on $\pi^{-1}(U)$. Any local section of $\mathcal{O}(1) \otimes \operatorname{Der}(S)$ induces a corresponding local $k$-linear derivation on $\mathcal{O}_{\mathbb{P}_{k}^{111}}$ by restricting it to act on $\underline{k}^{\times}$-invariant functions; this defines $j$. Injectivity of $i$ and the inclusion $\operatorname{im}(i) \subseteq \operatorname{ker}(j)$ follow from the fact that $E$ is nonsingular and the infinitesimal generator for the $\underline{k}^{\times}$-action; a standard calculation in the usual affine cells shows that $\operatorname{ker}(j) \subseteq \operatorname{im}(i)$ and that $j$ is surjective. Note that the sequence continues to remain exact on $\mathbb{P}_{A}^{1 / 1}$ after base change to any affine $k$-supervariety $\underline{\operatorname{Spec}(A) \text {, with } T \mathbb{P}_{k}^{111}}$ replaced by the relative tangent bundle $T \mathbb{P}_{A}^{1 / 1} / \operatorname{Spec}(A)$. We will denote the $A$-superalgebra $S \otimes_{k} A$ by $S_{A}$.

We now come to the SUSY structure.

Definition 5.1. Let $(X \rightarrow S, \mathcal{D})$ be a relative SUSY family. An $S$-automorphism $f: X \rightarrow X$ is SUSY structure-preserving (or simply SUSY-preserving) if and only if $\left(d f_{p}\right)\left(\mathcal{D}_{p}\right)=\mathcal{D}_{f(p)}$ for any $p \in X$.

We will consider SUSY structures given by sections of $\mathcal{O}_{A}(1) \otimes \Omega_{S / A}$. Here $\Omega_{S / A}$ denotes the $A$-module of Kähler differentials on $S_{A}$, i.e. the $A$-dual to $\operatorname{Der}\left(S_{A}\right)$; it has as basis the differentials $d z_{i}, d \zeta$. When we speak of the kernel of a section $\omega$ of $\mathcal{O}_{A}(1) \otimes \Omega_{S / A}$, we mean the kernel of $\omega$ when $\omega$ is interpreted as a morphism of sheaves of $\mathcal{O}_{\mathbb{P}_{A}^{111}}$ modules from $\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right) \rightarrow \mathcal{O}_{A}(2)$.

Proposition 5.2. Let $s:=z_{1} d z_{0}-z_{0} d z_{1}-\zeta d \zeta$. Then the image of $\operatorname{ker}(s)$ under $j$ is a SUSY structure on $\mathbb{P}_{k}^{1 \mid 1}$.

Proof. In the affine open subsupervariety $U_{1}:=\left\{z_{1} \neq 0\right\} \subset \mathbb{P}_{k}^{1 \mid 1}$, one calculates that the Euler vector field $E$ and the linear vector field $\widehat{Z}_{1}=\zeta \partial_{z_{0}}+z_{1} \partial_{\zeta}$ lie in
$\operatorname{ker}(s)$ and are linearly independent. At any point $p \in \mathbb{P}_{k}^{1 \mid 1}, s$ induces a linear map of super vector spaces $s_{p}:[\mathcal{O}(1) \otimes \operatorname{Der}(S)]_{p} \rightarrow[\mathcal{O}(2)]_{p}$ on the fibers. It is clear that $s$ is a basepoint-free section, hence $s_{p}$ is always surjective. By linear algebra, $\operatorname{ker}\left(s_{p}\right)$ is $1 \mid 1$ dimensional and hence $E_{p}$ and $\widehat{Z_{1}}, p$ span $\operatorname{ker}\left(s_{p}\right)$. By the super Nakayama's lemma, $E$ and $\widehat{Z_{1}}$ span $\operatorname{ker}(s)$ near $p$. Since $p$ was arbitrary, $E$ and $\widehat{Z_{1}}$ form a basis for $\operatorname{ker}(s)$ in $U_{1}$.

One sees that $Z_{1}:=j\left(\widehat{Z_{1}}\right)=\partial_{\eta}+\eta \partial_{w}$, where $w=z_{0} / z_{1}, \eta=\zeta / z_{1}$ are the usual affine coordinates in $U_{1} . Z_{1}^{2}=\partial_{w}$ and so $Z_{1}$ defines a SUSY structure in $U_{1}$. A similar calculation with the linear vector field $\widehat{Z}_{0}:=-\zeta \partial_{z_{1}}+z_{0} \partial_{\zeta}$ shows that $j(\operatorname{ker}(s))$ defines a SUSY structure on $U_{0}=\left\{z_{0} \neq 0\right\}$, hence the image of $\operatorname{ker}(s)$ under $j$ defines a SUSY structure on $\mathbb{P}_{k}^{1 \mid 1}$.

We note that by the considerations of [10], this is the unique SUSY structure on $\mathbb{P}_{k}^{1 \mid 1}$, up to SUSY-isomorphism.

We now need the following proposition. The proof is completely similar to the one in [10] Prop. 5.2, however since the context here is more general, we include it for completeness.

Lemma 5.3. Let $A$ be an affine $k$-superalgebra. Let $\omega, \omega^{\prime}$ be two global sections of $\mathcal{O}_{A}(1) \otimes \Omega_{S / A}$ such that $\mathcal{D}:=j(\operatorname{ker}(\omega)), \mathcal{D}^{\prime}:=j\left(\operatorname{ker}\left(\omega^{\prime}\right)\right)$ are $0 \mid 1$ distributions on $\mathbb{P}_{A}^{1 \mid 1}$. Suppose $\mathcal{D}=\mathcal{D}^{\prime}$. Then $\omega^{\prime}=h \omega$ for some even invertible function $h$ on $\mathbb{P}_{A}^{1 / 1}$.

Proof. Let $p \in \mathbb{P}_{A}^{1 \mid 1}$ be a point. Since $\mathcal{D}$ is locally a direct summand of $T \mathbb{P}_{A}^{1 \mid 1} / \underline{\operatorname{Spec}}(A)$, we have a local splitting $\left.\mathcal{D}\right|_{U} \oplus \mathcal{E}=\left.\left(T \mathbb{P}_{A}^{1 \mid 1} / \underline{\operatorname{Spec}}(A)\right)\right|_{U}$ in some neighborhood $U$ э p. Via the Euler exact sequence (base changed to $\operatorname{Spec}(A)$ ), we may lift $\left.\mathcal{D}\right|_{U}$ (resp. $\left.\mathcal{E}\right)$ uniquely to a rank $1 \mid 1$ (resp. $2 \mid 0$ ) submodule $\widehat{\mathcal{D}}$ (resp. $\mathcal{E}$ ) of $\left.\left[\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right)\right]\right|_{U}$ containing the $1 \mid 0$ line bundle $\langle E\rangle$ spanned by the Euler vector field, such that $\widehat{\mathcal{D}} \cap \widehat{\mathcal{E}}=\langle E\rangle$. We may therefore find local sections $\widehat{Z}($ resp. $\widehat{X})$ of $\widehat{\mathcal{D}}$ (resp $\widehat{\mathcal{E}}$ ) such that $\widehat{Z}, E$ (resp. $\widehat{X}, E)$ form a basis for $\widehat{\mathcal{D}}$ (resp. $\widehat{\mathcal{E}}$ ). Note that the condition $\widehat{\mathcal{D}} \cap \widehat{\mathcal{E}}=\langle E\rangle$ implies $\widehat{X}, \widehat{Z}, E$ form a basis of $\left.\left[\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right)\right]\right|_{U}$.

Viewing $\left.\omega\right|_{U}$ as an $\mathcal{O}_{\mathbb{P}_{A}^{111}}$-linear map from $\left.\left[\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right)\right]\right|_{U}$ to $\left.\mathcal{O}_{A}(2)\right|_{U}$, we have an induced linear map of super vector spaces

$$
\omega_{p}:\left(\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right)\right)_{p} \rightarrow\left(\mathcal{O}_{A}(2)\right)_{p}
$$

As $\operatorname{ker}\left(\omega_{p}\right)=\operatorname{span}\left\{\widehat{Z}_{p}, E_{p}\right\}$, we see by linear algebra that $\omega_{p}$ is a surjection, and that $\omega_{p}\left(\widehat{X}_{p}\right)$ is a basis for $\left(\mathcal{O}_{A}(2)\right)_{p}$; the analogous conclusion holds for
$\omega_{p}^{\prime}$ and $\omega_{p}^{\prime}\left(\widehat{X}_{p}\right)$. Hence by the super Nakayama's lemma, $\omega(\widehat{X})$ is a basis for $\left.\mathcal{O}_{A}(2)\right|_{U}$, and the same is true of $\omega^{\prime}(\widehat{X})$ (shrinking $U$ if necessary). Hence $\omega^{\prime}(\widehat{X}) / \omega(\widehat{X})$ is an invertible even function on $U$; let us denote it by $h$.

To show that $h$ is independent of the local complement $\mathcal{E}$ and the choice of basis element $\widehat{X}$, suppose $\mathcal{E}^{\prime}$ is another local complement to $\mathcal{D}$ on $U$, and let $\widehat{X}^{\prime}, E$ be a basis of the lift $\widehat{\mathcal{E}}^{\prime}$ of $\mathcal{E}^{\prime}$. Then we have $\widehat{X}^{\prime}=a \widehat{X}+b E+\alpha \widehat{Z}$ for some $a, b, \alpha \in \mathcal{O}_{\mathbb{P}_{A}^{111}}(U), a, b$ even and $\alpha$ odd. As $\widehat{X}, E, \widehat{Z}$ and $\widehat{X}^{\prime}, E, \widehat{Z}^{\prime}$ are both local bases for $\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right), a$ must be a unit.

Then we have

$$
\begin{aligned}
\omega^{\prime}\left(\widehat{X}^{\prime}\right) / \omega\left(\widehat{X}^{\prime}\right) & =\omega^{\prime}(a \widehat{X}+b E+\alpha \widehat{Z}) / \omega(a \widehat{X}+b E+\alpha \widehat{Z}) \\
& =\omega^{\prime}(\widehat{X}) / \omega(\widehat{X})
\end{aligned}
$$

since $\omega, \omega^{\prime}$ both annihilate $E$ and $\widehat{Z}$. This proves that the expression $\omega^{\prime}(\widehat{X}) / \omega(\widehat{X})$ is independent of all choices and hence $h$ is a well-defined function on all of $\mathbb{P}_{A}^{1 \mid 1}$. The equality $\omega^{\prime}=h \omega$ clearly holds locally, and since $h$ is now known to be globally defined, it holds globally.

Proposition 5.4. Let $f$ be an automorphism of $\mathbb{P}_{A}^{11}$. Then $f$ preserves the SUSY structure defined by $s$ if and only if for some (hence every) lift $\widetilde{f}$ of $f$ to $\mathrm{GL}_{2 \mid 1}(A), \widetilde{f}^{*}(s)=$ ts for some invertible function $t$.

Proof. We begin by noting that $\mathrm{GL}_{2 \mid 1}(A)$ preserves $A_{0}^{*}$-invariant open subsets of $\mathbb{A}_{A}^{2 \mid 1} \backslash\{0\}$, hence it acts naturally by pullback of functions on $\mathcal{O}_{A}(1) \otimes$ $\operatorname{Der}\left(S_{A}\right)$, where we interpret the latter as the sheaf assigning to any open subset $U \subseteq \mathbb{P}_{A}^{1 \mid 1}$ the linear vector fields on $\pi^{-1}(U) \subseteq \mathbb{A}_{A}^{2 \mid 1} \backslash\{0\}$.

The subsupergroup of invertible scalar matrices $\left\{c I: c \in A_{0}^{*}\right\}$ is central in $\mathrm{GL}_{2 \mid 1}(A)$, hence this $\mathrm{GL}_{2 \mid 1}(A)$-action preserves the subalgebra of $A_{0^{*}}^{*}$ invariant functions on any $A_{0}^{*}$-invariant open subset of $\mathbb{A}_{A}^{2 \mid 1} \backslash\{0\}$. Hence we have an induced $\mathrm{GL}_{2 \mid 1}(A)$-action on the sheaf $\mathcal{O}_{\mathbb{P}_{A}^{111}}$. Clearly, invertible scalar matrices act trivially on $\mathcal{O}_{\mathbb{P}_{A}^{111}}$, hence the $\mathrm{GL}_{2 \mid 1}(A)$-action on $\mathcal{O}_{\mathbb{P}_{A}^{111}}$ factors through $\mathrm{PGL}_{2 \mid 1}(A)$.

We see from the above that the action of $\mathrm{GL}_{2 \mid 1}(A)$ on $\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right)$ by pullback of functions induces naturally a $\mathrm{PGL}_{2 \mid 1}(A)$-action on $\mathcal{O}_{\mathbb{P}_{A}^{11}}$, hence on $T \mathbb{P}_{A}^{111} / \underline{\operatorname{Spec}}(A)$, also given by pullback of functions. But this is precisely
the $\mathrm{PGL}_{2 \mid 1}(A)$-action on $T \mathbb{P}_{A}^{1 \mid 1} / \underline{\operatorname{Spec}}(A)$ induced by the action of $\mathrm{PGL}_{2 \mid 1}(A)$ on $\mathbb{P}_{A}^{1 / 1}$ by automorphisms.

Recalling that the sheaf morphism $j: \mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right) \rightarrow T \mathbb{P}_{A}^{1 \mid 1} / \underline{\operatorname{Spec}}(A)$ is just given by restricting a linear vector field to act on $A_{0}^{*}$-invariant functions, we see $j$ is equivariant with respect to the $\mathrm{GL}_{2 \mid 1}(A)-$ and $\mathrm{PGL}_{2 \mid 1}(A)-$ actions previously defined.

We also have a $\mathrm{GL}_{2 \mid 1}(A)$-action on $\mathcal{O}_{A}(1) \otimes \Omega_{S / A}$ by the natural action on both factors, and for $\omega \in \Gamma\left(\mathcal{O}_{A}(1) \otimes \Omega_{S / A}\right)=\Gamma\left(\mathcal{O}_{A}(1)\right) \otimes \Omega_{S / A}$, we write $g^{*}(\omega)$ for $g \cdot \omega$.

Since the action of $\mathrm{GL}_{2 \mid 1}(A)$ on $\mathcal{O}_{A}(1) \otimes \operatorname{Der}\left(S_{A}\right)$ is the same as the natural action on the individual factors, and the $\mathrm{GL}_{2 \mid 1}(A)$-action on $\Omega_{S / A}$ is dual to that on $\operatorname{Der}\left(S_{A}\right)$, it follows that the evaluation pairing $\left[\mathcal{O}_{A}(1) \otimes\right.$ $\left.\operatorname{Der}\left(S_{A}\right)\right] \otimes\left[\mathcal{O}_{A}(1) \otimes \Omega_{S / A}\right] \rightarrow \mathcal{O}_{A}(2)$ is $\mathrm{GL}_{2 \mid 1}(A)$-equivariant, where $\mathcal{O}_{A}(2)$ is endowed with the natural $\mathrm{GL}_{2 \mid 1}(A)$-action.

From the preceding discussion, we see that $f$ is SUSY-preserving if and only if $j[\operatorname{ker}(\omega)]_{p}=j\left[\operatorname{ker}(\widetilde{f}(\omega)]_{p}\right.$ for any point $p$.

We claim this is true if and only if $j[\operatorname{ker}(\omega)]=j\left[\operatorname{ker}\left(\widetilde{f}^{*}(\omega)\right)\right]$. One direction is clear. For the other, suppose $j[\operatorname{ker}(\omega)]_{p}=j\left[\operatorname{ker}\left(\widetilde{f^{*}}(\omega)\right)\right]_{p}$ for any point $p$. Then by the super Nakayama's lemma $j[\operatorname{ker}(\omega)]=j\left[\operatorname{ker}\left(\widetilde{f^{*}}(\omega)\right)\right]$ in a neighborhood of $p$, hence globally. The claim then follows from Lemma 5.3 .

In order to determine the supergroup of SUSY-preserving automorphisms of $\mathbb{P}_{k}^{1 \mid 1}$ we must discuss various other supergroups. We follow closely the discussion in [13].

Definition 5.5. The 2|1-dimensional conformal symplecticorthogonal supergroup $\mathrm{C}_{2 \mid 1}$ is the subfunctor of $\mathrm{GL}_{2 \mid 1}$ that preserves, up to multiplication by an even invertible constant, the split nondegenerate supersymplectic form on $k^{2 \mid 1}$ given by $(v, w)=v^{t} H w$, where

$$
H:=\left(\begin{array}{ccc}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & -1
\end{array}\right)
$$

and ${ }^{t}$ denotes the super transpose of a matrix. More precisely, for every $k$-superalgebra $A, \mathrm{C}_{2 \mid 1}$ is the functor $(\mathrm{salg})_{\mathrm{k}} \rightarrow(\mathrm{grps})$ given by

$$
\mathrm{C}_{2 \mid 1}(A):=\left\{B \in \mathrm{GL}_{2 \mid 1}(A): B^{t} H B=Z(B) H\right\}
$$

where $Z: \mathrm{GL}_{2 \mid 1} \rightarrow \mathbb{G}_{m}^{1 \mid 0}$ is a fixed homomorphism.

The 2|1-dimensional projective conformal symplecticorthogonal supergroup $\mathrm{PC}_{2 \mid 1}$ is the image of $\mathrm{C}_{2 \mid 1}$ in $\mathrm{PGL}_{2 \mid 1}$, i.e, it is the sheafification of the groupvalued functor $A \rightarrow \mathrm{C}_{2 \mid 1}(A) /\left\{a I: a \in A_{0}^{*}\right\}$.

Proposition 5.6. $\mathrm{C}_{2 \mid 1}$ and $\mathrm{PC}_{2 \mid 1}$ are representable.

Proof. Taking the Berezinian of both sides of (7), one sees that $Z(B)=$ $\operatorname{Ber}(B)^{2}$. Thus, given

$$
B=\left(\begin{array}{lll}
a & b & \alpha \\
c & d & \beta \\
\gamma & \delta & e
\end{array}\right) \in \mathrm{GL}_{2 \mid 1}(A)
$$

a direct calculation shows that $B$ satisfies (7) if and only if the following equations hold:

$$
\begin{aligned}
& e^{2}+2 \alpha \beta=\operatorname{Ber}(B)^{2} \\
& a d-b c-\gamma \delta=\operatorname{Ber}(B)^{2} \\
& a \beta-c \alpha-e \gamma=0 \\
& b \beta-d \alpha-e \delta=0
\end{aligned}
$$

Thus these equations define $\mathrm{C}_{2 \mid 1}$ as a closed affine algebraic subsupergroup of $\mathrm{GL}_{2 \mid 1}$.

To prove that $\mathrm{PC}_{2 \mid 1}$ is representable, we use the trick of [13]. Let $\mathrm{SC}_{2 \mid 1}$ denote the functor $(\mathrm{salg})_{\mathrm{k}} \rightarrow($ grps $)$ given by

$$
\mathrm{SC}_{2 \mid 1}(A):=\left\{B \in \mathrm{C}_{2 \mid 1}(A): \operatorname{Ber}(B)=1\right\}
$$

Since its defining equations are those of $\mathrm{C}_{2 \mid 1}$ together with the equation $\operatorname{Ber}(B)=1, \mathrm{SC}_{2 \mid 1}$ is a closed affine algebraic subsupergroup of $\mathrm{GL}_{2 \mid 1}$. There is a short exact sequence of supergroups

$$
0 \rightarrow \mathrm{SC}_{2 \mid 1} \rightarrow \mathrm{C}_{2 \mid 1} \xrightarrow{\text { Ber }} \mathbb{G}_{m}^{1 \mid 0} \rightarrow 0 .
$$

There is a splitting of this sequence, given on $A$-points by sending $a \in A_{0}^{*}$ to $a I$, and the image of $\mathbb{G}_{m}^{1 \mid 0}$ under the splitting is clearly normal in $\mathrm{C}_{2 \mid 1}$, hence $\mathrm{C}_{2 \mid 1}$ is the internal direct product of $\mathrm{SC}_{2 \mid 1}$ and the subsupergroup $\left\{a I: a \in A_{0}^{*}\right\}$. This direct product decomposition allows us to naturally identify the functor $\mathrm{PC}_{2 \mid 1}$ with the functor of points of $\mathrm{SC}_{2 \mid 1}$; in particular, we see $\mathrm{PC}_{2 \mid 1}$ is an affine algebraic supergroup, isomorphic to $\mathrm{SC}_{2 \mid 1}$.

Definition 5.7. The 2|1-dimensional symplecticorthogonal supergroup $\mathrm{SpO}_{2 \mid 1}$ is the functor $(\mathrm{salg})_{\mathrm{k}} \rightarrow(\mathrm{grps})$

$$
\mathrm{SpO}_{2 \mid 1}(A):=\left\{B \in \mathrm{GL}_{2 \mid 1}(A): B^{t} H B=H\right\}
$$

Remark 5.8. $\mathrm{SpO}_{2 \mid 1}$ is well-known to be representable; the reader may readily write down defining equations for $\mathrm{SpO}_{2 \mid 1}$, completely analogous to those for $\mathrm{C}_{2 \mid 1}$, which show that $\mathrm{SpO}_{2 \mid 1}$ is a closed affine algebraic subsupergroup of $\mathrm{GL}_{2 \mid 1}$.

Proposition 5.9. $\mathrm{PC}_{2 \mid 1}$ is isomorphic to the irreducible component $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$ of $\mathrm{SpO}_{2 \mid 1}$ containing the identity.

Proof. Taking the Berezinian of both sides of (9) shows that $\operatorname{Ber}(B)= \pm 1$ for any $B \in \operatorname{SpO}_{2 \mid 1}(A)$. This yields a short exact sequence of supergroups

$$
0 \rightarrow \mathrm{SC}_{2 \mid 1} \rightarrow \mathrm{SpO}_{2 \mid 1} \xrightarrow{\text { Ber }}\{ \pm 1\} \rightarrow 0
$$

which is split by the morphism $\pm 1 \mapsto \pm I$ and $\{ \pm I\}$ is obviously normal in $\mathrm{SpO}_{2 \mid 1}$. Thus $\mathrm{SpO}_{2 \mid 1}$ is the internal direct product of $\{ \pm I\}$ and $\mathrm{SC}_{2 \mid 1}$. Note that $\mathrm{SC}_{2 \mid 1}$ is irreducible (one sees from its defining equations that its reduced algebraic group is $\mathrm{SL}_{2}$, which is known to be irreducible). Let $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$ denote the irreducible component of $\mathrm{SpO}_{2 \mid 1}$ that contains the identity. We claim $\mathrm{SC}_{2 \mid 1}=\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$. Since $I \in \mathrm{SC}_{2 \mid 1} \cap\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$, it is clear $\mathrm{SC}_{2 \mid 1} \subseteq\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$. Conversely, we see that $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0} \subseteq \mathrm{SC}_{2 \mid 1}$ : the restriction of the morphism Ber to the irreducible supervariety $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$ must be constant, hence equal to 1 . Since we previously showed $\mathrm{PC}_{2 \mid 1}$ is isomorphic to $\mathrm{SC}_{2 \mid 1}$, the proposition is proven.

Theorem 5.10. The algebraic supergroup $\operatorname{Aut}_{\mathrm{SuSY}}\left(\mathbb{P}_{k}^{\mid 11}\right)$ of SUSY preserving automorphisms of $\mathbb{P}_{k}^{1 \mid 1}$ is isomorphic to $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}$.

![](https://cdn.mathpix.com/cropped/2024_05_09_d5a781ccd3019273404eg-20.jpg?height=63&width=1358&top_left_y=432&top_left_x=378)
lating Aut ${ }_{\text {SUSY }}\left(\mathbb{P}_{k}^{1 \mid 1}\right)(A)$ where $A$ is a $k$-superalgebra. For this, we note that $\mathbb{P}_{A}^{1 \mid 1}$ has the SUSY structure over $A$ induced by base change from $\mathbb{P}_{k}^{1 \mid 1}$, given by $s$.

Let $g \in \mathrm{PGL}_{2 \mid 1}(A)$ be an automorphism of $\mathbb{P}_{A}^{1 \mid 1}$, and $\widehat{g}$ a lift of $g$ to $\mathrm{GL}_{2 \mid 1}(A)$. Recall that we have a natural action of the group of $A$-points of $\mathrm{GL}_{2 \mid 1}(A)$ on $\Gamma\left(\mathcal{O}_{A}(1) \otimes \Omega_{S / A}\right)$. More concretely, in the given coordinates we have for any matrix $\widehat{g} \in \mathrm{GL}_{2 \mid 1}(A)$ :

$$
\widehat{g} \cdot\left(\begin{array}{c}
z_{0} \\
z_{1} \\
\zeta
\end{array}\right)=\widehat{g}\left(\begin{array}{c}
z_{0} \\
z_{1} \\
\zeta
\end{array}\right), \quad \widehat{g} \cdot\left(\begin{array}{c}
d z_{0} \\
d z_{1} \\
d \zeta
\end{array}\right)=\widehat{g}\left(\begin{array}{l}
d z_{0} \\
d z_{1} \\
d \zeta
\end{array}\right)
$$

where we write $z_{i}$ for $z_{i} \otimes 1$ and so on.

By Prop. 5.3, $g$ is SUSY-preserving if and only if $\widehat{g}$ sends

$$
s=z_{1} d z_{0}-z_{0} d z_{1}-\zeta d \zeta=\left(\begin{array}{lll}
z_{0} & z_{1} & \zeta
\end{array}\right) H\left(\begin{array}{l}
d z_{0} \\
d z_{1} \\
d \zeta
\end{array}\right), \quad H=\left(\begin{array}{ccc}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & -1
\end{array}\right)
$$

to a multiple of $s$ by an invertible even function. Hence

$$
\left(\begin{array}{lll}
z_{0} & z_{1} & \zeta
\end{array}\right) \widehat{g}^{t} H \widehat{g}\left(\begin{array}{l}
d z_{0} \\
d z_{1} \\
d \zeta
\end{array}\right)=\left(\begin{array}{lll}
z_{0} & z_{1} & \zeta
\end{array}\right) Z(\widehat{g}) H\left(\begin{array}{l}
d z_{0} \\
d z_{1} \\
d \zeta
\end{array}\right)
$$

i.e. $\widehat{g} \in \mathrm{C}_{2 \mid 1}(A)$. It follows from equation (8) that $g$ lies in $\operatorname{PC}_{2 \mid 1}(A)$, which is naturally identified with $\left(\mathrm{SpO}_{2 \mid 1}\right)^{0}(A)$ by Prop. 5.9.

## References

[1] C. Carmeli, L. Caston, R. Fioresi, Mathematical Foundation of Supersymmetry, with an appendix with I. Dimitrov, EMS Ser. Lect. Math., European Math. Soc., Zurich, 2011.

[2] L. Crane, J. Rabin, Super Riemann surfaces: uniformization and Teichmuller theory, Comm. Math. Phys. Vol. 113, no. 4, 601-623, 1988.

[3] J. Bernstein, notes by P. Deligne, J. Morgan, Notes on supersymmetry (following J. Bernstein), in: "Quantum Fields and Strings. A Course for Mathematicians", Vol. 1, AMS, 1999.

[4] R. Donagi, E. Witten, Supermoduli Space Is Not Projected, arXiv: 1304.7798 .

[5] D. Eisenbud and J. Harris, The geometry of schemes. Springer Verlag, New York, 2000.

[6] R. Fioresi, F. Gavarini, Algebraic supergroups with Lie superalgebras of classical type. J. Lie Theory 23 (2013), no. 1, 143-158.

[7] R. Fioresi, F. Gavarini, Chevalley supergroups. Mem. Amer. Math. Soc. 215 (2012), no. 1014.

[8] R. Fioresi, F. Gavarini, On the construction of Chevalley supergroups. Supersymmetry in mathematics and physics, 101-123, Lecture Notes in Math., 2027, Springer, Heidelberg, 2011.

[9] R. Fioresi, S. D. Kwok, On SUSY curves, in "Advances in Lie Superalgebras" M. Gorelik, Papi, P. (Eds.), Springer INdAM Series, 7 (2014).

[10] R. Fioresi, M. A. Lledo. The Minkowski and Conformal Superspaces, World Scientific Publishing, 2015.

[11] R. Hartshorne, Algebraic Geometry. Springer, 1997.

[12] S. D. Kwok, Super Morita Theory, submitted.

[13] Y. I. Manin, Topics in Noncommutative Geometry; Princeton University Press, 1991.

[14] Y. I. Manin, Gauge Field Theory and Complex Geometry; translated by N. Koblitz and J.R. King. Springer-Verlag, Berlin-New York, 1988.

[15] Y. Sun, $\mathrm{PGL}_{n}$ and automorphisms of projective space. www.math.harvard.edu/ gaitsgde/Schemes_2009/Yi-notes.pdf, 2009.

[16] E. Witten, Notes on super Riemann surfaces and their moduli, arXiv: 1209.2459 .

