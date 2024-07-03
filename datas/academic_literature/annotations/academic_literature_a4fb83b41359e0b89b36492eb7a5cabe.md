# MODULAR CURVES $X_{1}(n)$ AS MODULI SPACES OF POINT ARRANGEMENTS AND APPLICATIONS 

LEV BORISOV, XAVIER ROULLEAU


#### Abstract

For a complex elliptic curve $E$ and a point $p$ of order $n$ on it, the images of the points $p_{k}=k p$ under the Weierstrass embedding of $E$ into $\mathbb{C P}^{2}$ are collinear if and only if the sum of indices is divisible by $n$. Thus, it provides a realization of a certain matroid. We study this matroid in detail and prove that its realization space is isomorphic (over $\mathbb{C}$ ) to the modular curve $X_{1}(n)$, provided $n \geq 10$, which also provides an integral model of $X_{1}(n)$. In the process, we find a connection to the classical Ceva and Böröczky examples of special point and line configurations. We also discuss the situation for smaller values of $n$.


## 1. INTRODUCTION

For $n>4$ coprime to the characteristic of the base field, modular curves $X_{1}(n)$ were defined as the compactifications of the moduli spaces of pairs $(E, t)$, where $t$ is a point of order $n$ on an elliptic curve $E$. The first constructions of these curves were obtained over $\mathbb{C}$ by taking the compactification of the quotient $\mathcal{H} / \Gamma_{1}(n)$ of the upper half-plane by the modular group $\Gamma_{1}(n)$.

Deligne and Rapoport in [12 constructed these curves as representation of functors, using Deligne-Mumford stacks. Another approach was done by Katz-Mazur in 16 using Drinfeld modules. These two works have been unified by Conrad in 9 using Artin stacks. The main difficulties of the constructions of $X_{1}(n)$ are to find a model over the integers, to have a geometric interpretation of the points at the compactification (the cusps), and a geometric moduli interpretation of their reduction modulo $p$ when $p$ divides $n$.

We propose in this paper to give a geometric construction of the modular curves as (compactifications of) moduli spaces of realizations of certain matroids, i.e. as moduli spaces of line or points arrangements. Here a line (respectively a point) arrangement in the projective plane is a finite set of lines (respectively points). Such arrangement is said labeled if there is a set parametrizing its elements.

Let us recall that a matroid $\mathcal{T}$ (of rank 3) is a combinatorial structure which formally describes the intersection relations between the elements of a labeled line arrangement, or in the dual setting, $\mathcal{T}$ encodes the alignments

2000 Mathematics Subject Classification. Primary: 14N20, Secondary 14G35, 11G05, 14K10, 11Fxx.
between the points of a labeled point arrangement. The word "formally" here means that that given a matroid such a line (or point) arrangement does not always exist, and a matroid $\mathcal{T}$ (of rank 3 ) is said realizable over a field $K$ if there is indeed a labeled line (or point) arrangement over $K$ which has the same combinatorial data as $\mathcal{T}$. There is a well-defined notion of moduli space of realizations of a matroid, which moduli space is a scheme naturally defined over $\mathbb{Z}$, the realizations over the field $K$ being obtained by taking the fiber over $\operatorname{Spec}(K)$.

To a pair $(E, t)$ of an elliptic curve and an element $t$ of order $n$, let us associate the labeled point arrangement

$$
\mathcal{P}_{E, t}=(k t)_{k \in \mathbb{Z} / n \mathbb{Z}}
$$

where we fix an embedding $\iota: E \hookrightarrow \mathbb{P}^{2}$ sending the group identity to a flex point on the image and where we identify a point with its image. Up to projective transformations, $\mathcal{P}_{E, t}$ does not depend on the choice of $\iota$. Three distinct points $s_{1}=i t, s_{2}=j t, s_{3}=k t(i, j, k \in \mathbb{Z} / n \mathbb{Z})$ on $\mathcal{P}_{E, t}$ lie on a line if and only if $s_{1}+s_{2}+s_{3}=0$ on the elliptic curve $E$, thus if and only if $i+j+k=0$. Accordingly, the set of triples $\{i, j, k\} \subset \mathbb{Z} / n \mathbb{Z}$ such that $i+j+k=0$ defines the so-called non-bases of a matroid $\mathcal{T}_{n}$, and the point arrangement $\mathcal{P}_{E, t}$ is a realization of $\mathcal{T}_{n}$. Let $\mathcal{R}\left(\mathcal{T}_{n}\right)$ be the moduli space of realizations of $\mathcal{T}_{n}$ : this is the quotient of the space of all realization $\mathcal{P}=\left(p_{k}\right)_{k \in \mathbb{Z} / n \mathbb{Z}}$ of $\mathcal{T}_{n}$ by the action of the projective transformations $\gamma$ such that $\gamma . \mathcal{P}=\left(\gamma p_{k}\right)_{k \in \mathbb{Z} / n \mathbb{Z}}$. We denote the class of $\mathcal{P}$ in $\mathcal{R}\left(\mathcal{T}_{n}\right)$ by $[\mathcal{P}]$, so that $[\mathcal{P}]=\left\{\gamma \mathcal{P} \mid \gamma \in P G L_{2}\right\}$. We obtain:

Theorem 1. Suppose that the base field is an algebraically closed field of characteristic not dividing $n$. For $n \geq 7$, the map $\phi: X_{1}(n)^{\circ} \rightarrow \mathcal{R}\left(\mathcal{T}_{n}\right)$, $(E, t) \rightarrow\left[\mathcal{P}_{E, t}\right]$ is birational, where $X_{1}(n)^{\circ}$ is the complement of the cusps in $X_{1}(n)$.

For $n \geq 7$, there exists a natural compactification $\overline{\mathcal{R}\left(\mathcal{T}_{n}\right)}$ of $\mathcal{R}\left(\mathcal{T}_{n}\right)$ and the map $\phi$ extends to a morphism

$$
\phi: X_{1}(n) \rightarrow \overline{\mathcal{R}\left(\mathcal{T}_{n}\right)}
$$

Let us suppose that the base field is $\mathbb{C}$, and let

$$
\pi: \mathcal{H}^{*} \rightarrow X_{1}(n)=\mathcal{H}^{*} / \Gamma_{1}(n), \tau \mapsto \Gamma_{1}(n) \tau
$$

be the quotient map.

Theorem 2. Let be $n \geq 10$. The map $\phi$ is an isomorphism and the curve $\overline{\mathcal{R}\left(\mathcal{T}_{n}\right)}$ is contained in a projective space $\mathbb{P}$ of dimension $\left\lfloor\frac{n-3}{2}\right\rfloor$. The composite map $\mathcal{H}^{*} \rightarrow X_{1}(n) \rightarrow \mathbb{P}$ is obtained by weight one modular forms for the group $\Gamma_{1}(n)$.

Borisov, Gunnels and Popescu proved in [4, [6] that certain weight 1 Eisenstein series, obtained as log-derivatives of the Jacobi theta function at rational points, generate the ring of modular forms for $\Gamma_{1}(n)$ in sufficiently
high degree and thus provide an embedding $X_{1}(n) \rightarrow \mathbb{P}$. When $n \geq 5$ is prime, one can even find explicit relations that cut out $X_{1}(p)$ schemetheoretically in $\mathbb{P}^{\frac{p-3}{2}}$, see 5 .

In 23, Voight and Zureick-Brown study a generalization of Petri's Theorem about the quadratic relations defining the compactification of a curve $\mathcal{H} / \Gamma$, where $\mathcal{H}$ is the upper-half plane and $\Gamma$ is a modular group. In our situation, for a rank 3 matroid $M$, the ideal of the moduli space $\mathcal{R}(M)$ of realizations of $M$ is always generated by quadrics or linear forms with integral coefficients.

Let us describe the structure of the paper. In Section [2, we recall the basics of line arrangements and the notations of some operators acting on them defined in [19, which will be used later. We also recall the theory of matroids $\mathcal{T}$ and their moduli space of realizations $\mathcal{R}(\mathcal{T})$. We then introduce the matroid $\mathcal{T}_{n}$ and the map $X_{1}(n)^{\circ} \rightarrow \mathcal{R}\left(\mathcal{T}_{n}\right)$, where $X_{1}(n)^{\circ}$ is the open sub-scheme parametrizing pairs $(E, t)$, where $E$ is an elliptic curve and $t$ is a $n$-torsion point, the complement of the cusps points in $X_{1}(n)$.

In Section 3, we prove that $\mathcal{R}\left(\mathcal{T}_{n}\right)$ is one-dimensional and its generic point is the image of the map $\phi$. In Section 4, we prove several results on modular forms which are needed in the next section. In particular, we find explicit Eisenstein series for $\Gamma_{1}(n)$ which have zeros only at the cusps of $X_{1}(n)$. Their ratios could be used to study the cuspidal subgroup of the Jacobian of $X_{1}(n)$ (the finite subgroup generated by the differences of the cusps). Section 5 contains the proof of Theorem 2, Section 6 studies two natural compactifications of $\mathcal{R}\left(\mathcal{T}_{n}\right)$.

In the ancillary files of the first arXiv version of this paper, one can find a) the Magma algorithms used for computing the moduli space of realizations of a matroid, and the equations of the curves $X_{1}(n)$ for low $n$, b) the Mathematica computations used in Sections 3, 5 and 6.

Finally let us observe that a similar construction may be obtained for the modular curve $X(n)$. Also, using embedding of elliptic curves in $\mathbb{P}^{k-1}$ as degree $k$ curves, one may study the modular curves $X_{1}(n)$ as realization spaces of rank $k \geq 4$ matroids. That will be the subject of another paper.

Acknowledgements. The authors thank Lukas Kühne for useful discussions on matroids. We used the computer algebra systems OSCAR [11, Magma [7] and Mathematica [18]. X.R. acknowledges support from Centre Henri Lebesgue ANR-11-LABX-0020-01.

## 2. Preliminaries on matroids, operators and CUbic CURVEs

2.1. Point and line arrangements. A line arrangement $\mathcal{C}=\ell_{1}+\cdots+\ell_{n}$ is the union of a finite number of distinct lines in $\mathbb{P}^{2}$. A labeled line arrangement $\mathcal{C}=\left(\ell_{1}, \ldots, \ell_{n}\right)$ is a line arrangement with a choice of ordering of the lines.

We denote by $\mathcal{D}$ the duality operator which to a line arrangement $\mathcal{C}$ associates the set of the annihilators of the lines of $\mathcal{C}$ in the dual projective plane
$\check{\mathbb{P}}^{2}$. Concretely, we fix coordinates $x, y, z$ and then $\mathcal{D}(\ell)=(a: b: c)$ for the line $\ell:\{a x+b y+c z=0\}$, moreover $\mathcal{D}(a: b: c)=\ell$. By duality, one also has a natural notion of (labeled) point arrangements.

Recall that for a given line arrangement $\mathcal{C}$ in $\mathbb{P}^{2}$ and $m \geq 2$, an $m$-point of $\mathcal{C}$ is a point at which exactly $m$ lines of $\mathcal{C}$ meet. For $\mathfrak{m}$ a set of integers $m \geq 2$, let us denote by $\mathcal{P}_{\mathfrak{m}}(\mathcal{C})$ the union of the $m$-points of $\mathcal{C}$, over $m \in \mathfrak{m}$. For a given point arrangement $\mathcal{P}$ and $n \geq 2$, we define $\mathcal{L}_{\mathfrak{n}}(\mathcal{P})$ as the union of the lines that are $n$-rich, where an $n$-rich line is a line containing exactly $n$ points of $\mathcal{P}$. Of course, $\mathcal{P}_{\mathfrak{m}}(\mathcal{C})$ and $\mathcal{L}_{\mathfrak{n}}(\mathcal{P})$ could be empty. We denote by $\mathcal{D}_{\mathfrak{n}}(\mathcal{L})$ the line arrangement $\mathcal{D}\left(\mathcal{P}_{\mathfrak{n}}(\mathcal{L})\right)$ in the dual plane.

For $n \geq 2$, by abuse of notations, we denote by $\mathcal{L}_{n}(\mathcal{P})$ the line arrangement $\mathcal{L}_{\{\geq n\}}(\mathcal{P})$, and use a similar notation $\mathcal{P}_{n}(\mathcal{C})$ or $\mathcal{D}_{n}(\mathcal{C})$ for a line arrangement $\mathcal{C}$.

2.2. Matroids. Let us recall the following first definitions and results on matroids:

A matroid $M$ is a pair $M=(E, \mathcal{B})$, where $E$ is a finite set of elements called atoms and the elements of $\mathcal{B}$ are subsets of $E$, called basis (plural: bases), subject to the following properties:

- $\mathcal{B}$ is non-empty;
- if $A$ and $B$ are distinct members of $\mathcal{B}$ and $a \in A \backslash B$, then there exists $b \in B \backslash A$ such that $(A \backslash\{a\}) \cup\{b\} \in \mathcal{B}$.

The bases have the same order $k$, called the rank of $(E, \mathcal{B})$. An order $k$ subset of $E$ that is not a basis is called a non-basis.

As we will be only concerned with line or point arrangements in $\mathbb{P}^{2}$, we now suppose that the rank of $M$ is 3 . If $m$ is the order of $E$, we may identify $E$ with the set $\{1, \ldots, m\}$.

Matroids originated from the following kind of examples: If $\mathcal{C}=\left(\ell_{1}, \ldots, \ell_{m}\right)$ is a labeled line arrangement, the subsets $\{i, j, k\} \subset\{1, \ldots, m\}$ such that the lines $\ell_{i}, \ell_{j}, \ell_{k}$ meet in three distinct points are the bases of a matroid $M(\mathcal{C})$ over the set $\{1, \ldots, m\}$. We say that $M(\mathcal{C})$ is the matroid associated to $\mathcal{C}$. In the dual setting, if $\mathcal{P}=\left(p_{1}, \ldots, p_{m}\right)$ is a point arrangement, the order 3 subsets $\{i, j, k\} \subset\{1, \ldots, m\}$ such that $p_{i}, p_{j}, p_{k}$ are not collinear are the bases of a matroid $M(\mathcal{P})$. One has $M(\mathcal{D}(\mathcal{P}))=M(\mathcal{P})$.

A realization (over some field, and when that exists) of a matroid $M=$ $(E, \mathcal{B})$ is a converse operation to the application $\mathcal{L} \rightarrow M(\mathcal{L})$ or $\mathcal{P} \rightarrow M(\mathcal{P})$ : it is the data of a size $3 \times m$ matrix with non-zero columns $c_{1}, \ldots, c_{m}$, which are considered up to a multiplication by a scalar (thus as points in the projective plane, which points must be distinct), and such that any order 3 subset $\left\{i_{1}, i_{2}, i_{3}\right\}$ of $E$ is a non-basis if and only if the size 3 minor $\left|c_{i_{1}}, c_{i_{2}}, c_{i_{3}}\right|$ is zero. Then we denote by $\ell_{i}$ the line with normal vector the point $c_{i}$. The labeled line arrangement $\mathcal{C}=\left(\ell_{1}, \ldots, \ell_{m}\right)$ is such that three lines $\ell_{i_{1}}, \ell_{i_{2}}, \ell_{i_{3}}$ meet at a common point if and only if $\left\{i_{1}, i_{2}, i_{3}\right\}$ is a non-basis; it is a realization of $M(\mathcal{L})$. Dually, $\mathcal{P}=\left(c_{i}\right)_{1 \leq i \leq m}$ is a point realization of $M(\mathcal{P})$.

The space of realizations $\mathfrak{U}(M)$ of a matroid $M$ is therefore defined as follows: For $1 \leq j \leq m$, let $x_{1, j}, x_{2, j}, x_{3, j}$ be the coordinates of the $j^{\text {th }}$ term in the product $\left(\mathbb{P}^{2}\right)^{m}$. Consider the matrix $A=\left(x_{i, j}\right)_{1 \leq i \leq 3,1 \leq j<m}$. For a set $\mu=\{i, j, k\}$ of three elements in $E$, let $A_{\mu}$ be the $3 \times 3$ sub-matrix of $A$ obtained by taking columns $i, j, k$ and let $V_{\mu}$ be the sub-scheme of $\left(\mathbb{P}^{2}\right)^{m}$ defined by $\operatorname{det}\left(A_{\mu}\right)=0$. Consider

$$
V(M)=\cap_{\mu \in N B} V_{\mu}
$$

where the product runs over the non-bases of $M$ and

$$
W(M)=\cup_{\mu \in B} V_{\mu}
$$

where the union runs over the bases of $M$. The space of realizations $\mathfrak{U}(M)$ of $M$ is the scheme

$$
\mathfrak{U}(M)=V(M) \backslash W(M)
$$

We observe that this scheme $\mathfrak{U}(M)$ is naturally defined over $\mathbb{Z}$ as a subscheme of $\left(\mathbb{P}_{\mathbb{Z}}^{2}\right)^{m}$.

Suppose that the realization space $\mathfrak{U}_{/ k}$ is non-empty over some field $k$. For a realization $\mathcal{P}=\left(p_{1}, \ldots, p_{m}\right) \in \mathfrak{U}(k)$ of $M$ and $\gamma \in P G L_{3}(k)$, the point arrangement $\left(\gamma p_{1}, \ldots, \gamma p_{m}\right)$ is another realization. Let us denote by $[\mathcal{P}]$ the orbit of $\mathcal{P}$ under that action of $P G L_{3}$. The moduli space $\mathcal{R}(M)$ of realizations of $M$ is the quotient of $\mathfrak{U}$ by $P G L_{3}(k)$; we denote by

$$
q: \mathfrak{U}(M) \rightarrow \mathcal{R}(M), \mathcal{P} \rightarrow[\mathcal{P}]
$$

the quotient map. Suppose that there exist distinct elements $j_{1}, \ldots, j_{4} \in$ $\{1, \ldots, m\}$ such that every order 3 subset in $j_{1}, \ldots, j_{4}$ is a basis of the matroid $M$ (that will always be the case in this paper). Then any class $[\mathcal{C}]$ in $\mathcal{R}(M)$ has a unique representative $\mathcal{C}$ such that the points number $j_{1}, \ldots, j_{4}$ of $\mathcal{P}$ are the canonical basis

$$
(1: 0: 0),(0: 1: 0),(0: 0: 1),(1: 1: 1)
$$

That shows that the quotient map has a section

$$
s=s_{j_{1}, \ldots, j_{4}}: \mathcal{R}(M) \rightarrow \mathfrak{U}(M)
$$

sending a class to the unique representative such that the vectors number $j_{1}, \ldots, j_{4}$ are the canonical basis. Then one can identify, although noncanonically, $\mathcal{R}(M)$ with its image by $s$, so that any element of $\mathcal{R}(M)$ is not only a class but an actual realization. Let us fix such such a section: then $\mathcal{R}(M)$ is the intersection of $\mathfrak{U}(M)$ with the scheme defined by the ideal of the canonical basis at the points number $j_{1}, \ldots, j_{4}$. We note that $s(\mathcal{R}(M))$ then gets a scheme structure, defined over $\mathbb{Z}$. Let $j_{1}^{\prime}, \ldots, j_{4}^{\prime} \in\{1, \ldots, m\}$ be four other elements such that such that every order 3 subset in $j_{1}^{\prime}, \ldots, j_{4}^{\prime}$ is a basis of the matroid $M$. Define $s_{1}=s_{j_{1}, \ldots, j_{4}}, s_{2}=s_{j_{1}^{\prime}, \ldots, j_{4}^{\prime}}$. There exists a unique $3 \times 3$ matrix $P$ with coprime coefficients in

$$
\mathbb{Z}\left[\left(x_{i, j}\right) \mid 1 \leq i \leq 3, j \in\left\{j_{1}^{\prime}, \ldots, j_{4}^{\prime}\right\}\right]
$$

sending the columns $c_{j_{1}^{\prime}}, \ldots, c_{j_{4}^{\prime}}$ to the canonical basis, $P$ defines an isomorphism between $s_{1}\left(\mathcal{R}(M)\right.$ ) and $s_{2}(\mathcal{R}(M)$ ), thus $\mathcal{R}(M)$ is well-defined over $\mathbb{Z}$.

Definition 3. Once a section $s: \mathcal{R}(M) \rightarrow \mathfrak{U}(M)$ is fixed, we call the map $s \circ q$ the period map of $M$.

Very often the first four elements of the matroid are such that every order 3 subset is a basis of the matroid $M$, so that, when speaking of a period map, we implicitly refer to the section $s$ associated to these four elements. We then moreover identify $\mathcal{R}(M)$ with its image by $s$.

2.3. The matroid $\mathcal{T}_{n}$. For $n \geq 3$, let $\mathcal{T}_{n}$ be the matroid such that the atoms of $\mathcal{T}_{n}$ are the elements of $\mathbb{Z} / n \mathbb{Z}$ and the non-bases are the order three subsets $\{i, j, k\}$ of $\mathbb{Z} / n \mathbb{Z}$ such that

$$
i+j+k=0
$$

The automorphism group of $\mathcal{T}_{n}$ contains $(\mathbb{Z} / n \mathbb{Z})^{*}$ since the multiplication by an element of $(\mathbb{Z} / n \mathbb{Z})^{*}$ preserves the set of non-bases.

2.4. Cyclic torsion groups on elliptic curves and realizations of $\mathcal{T}_{n}$. Let $E$ be an elliptic curve with neutral element $O$, and let $T$ be a cyclic torsion subgroup of order $n$. Fix a plane model of $E$ so that $O$ is a flex point. For $t, t^{\prime}, t^{\prime \prime}$, three distinct elements of $T$, the points $t, t^{\prime}, t^{\prime \prime}$ are aligned if and only if

$$
t+t^{\prime}+t^{\prime \prime}=O
$$

By taking a generator $t \in T$, one gets a labeling $\mathbb{Z} / n \mathbb{Z} \rightarrow T, k \rightarrow k t$ of $T$.

Proposition 4. The labeled point arrangement $\mathcal{P}=(k t)_{k \in \mathbb{Z} / n \mathbb{Z}}$ associated to $(E, t)$ is a realization of the matroid $\mathcal{T}_{n}$. Up to projective automorphism, the point arrangement $\mathcal{P}$ is independent of the choice of the plane model of $E$ so that $O$ is a flex point.

Proof. The first assertion is clear. The second assertion is a direct consequence of [21, III, Proposition 3.1].

As we will see in the next sections, conversely, for $n \geq 7$, any realization of $\mathcal{T}_{n}$ comes from such torsion points on a (possibly singular) cubic curve. Moreover we will obtain that, knowing $\mathcal{P}$, one may recover - up to isomorphism- the cubic curve and the generator of the torsion group.

Let $X_{1}(n)^{\circ} \subset X_{1}(n)$ be the open subscheme of the modular curve which parametrizes pairs $(E, t)$ of elliptic curves with a torsion point of order $n$. Proposition 4 may be rephrased as:

Corollary 5. There exists a morphism

$$
\phi_{n}: X_{1}(n)^{\circ} \rightarrow \mathcal{R}\left(\mathcal{T}_{n}\right)
$$

which to a point $(E, t)$ associates the realization $(k t)_{k \in \mathbb{Z} / n \mathbb{Z}}$ up to projective automorphism.

## 3. Realization SPaCes OF $\mathcal{T}_{n}$.

The aim of this section is to further study realization spaces of $\mathcal{T}_{n}$ for $n \geq 5$. We will also be interested in their compactifications in $\left(\mathbb{P}^{2}\right)^{n-4}$. For simplicity, we will work over the field of complex numbers.

- Case $n=5$. We have points $p_{0}, \ldots, p_{4}$ with the non-bases $\{0,1,4\},\{0,2,3\}$ only. This means that we can make $p_{1}, \ldots, p_{4}$ to be canonical basis (2.1), which then forces $p_{0}=(0,1,1)$, so the realization scheme is a point and $\phi_{5}$ is constant.

Remark 3.1. It is possible to modify the matroid slightly to get an open subset of the modular curve $X_{1}(5)$. Namely, consider the pair $(E, \alpha)$, where $E$ is an elliptic curve and $\alpha$ is a 5-torsion element of $E$. Up to projective transformation, one may suppose that $E=E_{\theta}$ is the elliptic curve

$$
E_{\theta}: y^{2}+(1-\theta) x y-\theta y=y^{3}-\theta x^{2},\left(\theta \in \mathbb{P}^{1} \text { generic }\right)
$$

and $\alpha=\alpha_{\theta}=(0: 0: 1) ; E_{\theta}$ is the universal elliptic curve with a point of 5-torsion, see e.g. 1]. Let us associate to $\left(E_{\theta}, \alpha\right)$ the labeled line arrangement $\mathcal{C}=\mathcal{C}_{\theta}$ which is the union of the 5 tangent lines to the points in $T=(k \alpha)_{k \in \mathbb{Z} / 5 \mathbb{Z}}$ and the two lines in $\mathcal{L}_{2}(T)$ which are not the tangent lines, where $\mathcal{L}_{2}(T)$ is the union of the lines that contain at least two points of $T$ (see Section 2.1). Let $\mathcal{T}_{5}^{\prime}$ be the matroid with 7 atoms defined by the non-bases

$$
\{1,6,7\},\{2,3,7\},\{2,4,6\},\{3,5,6\},\{4,5,7\}
$$

The realization space $\mathcal{R}\left(\mathcal{T}_{5}^{\prime}\right)$ is smooth, 1-dimensional; the seven lines associated to a point in $\mathcal{R}\left(\mathcal{T}_{5}^{\prime}\right)$ have duals the canonical basis of $\mathbb{P}^{2}$ and

$$
\left(\theta+1: 1: 1-\theta^{2}\right),(\theta+1: 1: \theta+1),(0: 1: \theta+1)
$$

for $\theta \in \mathbb{P}^{1}, t \notin\{0, \pm 1\}$.

The line arrangement $\mathcal{C}_{\theta}$ is a realization of $\mathcal{T}_{5}^{\prime}$ and a direct computation shows that the rational map $\left(E_{\theta}, \alpha_{\theta}\right) \rightarrow \mathcal{C}_{\theta}$ from $X_{1}(5) \simeq \mathbb{P}^{1}$ to $\mathcal{R}\left(\mathcal{T}_{5}^{\prime}\right)$ has degree one.

- Case $n=6$. The matroid $\mathcal{T}_{6}$ has non-bases $\{0,1,5\},\{0,2,4\},\{1,2,3\}$ and $\{3,4,5\}$. We can put the points $p_{0}, p_{1}, p_{3}, p_{4}$ in the standard form (2.1), which forces

$$
p_{2}=(0,1,1), p_{5}=(1,1,0)
$$

So the realization scheme is again a point.

Remark 3.2. As in the $n=5$ case, we can find a matroid description for $X_{1}(6)$. The universal elliptic curve over $X_{1}(6) \simeq \mathbb{P}^{1}$ is given by

$$
E_{\theta}: y^{2}+(1-\theta) x y-\left(\theta^{2}+\theta\right) y=x^{3}-\left(\theta^{2}+\theta\right) x^{2}, \theta \in \mathbb{P}^{1} \text { generic }
$$

(see e.g. [1, 22]). The point $\alpha=(0: 0: 1)$ has order 6 . For $k \in \mathbb{Z} / 6 \mathbb{Z}$, let us denote by $p_{k \alpha}^{\prime}$ the dual of the line tangent to $E_{\theta}$ at the point $k \alpha$; this is a point in the dual plane. The line arrangement $\mathcal{C}_{\theta}=\mathcal{L}_{\{2\}}\left(\left(p_{k \alpha}^{\prime}\right)_{k \in \mathbb{Z} / 6 \mathbb{Z}}\right.$ ) (see notations in Section 2.1) is the union of 15 lines. We label these lines from 1 to

15 so that they correspond bijectively with the 15 pairs $(0,1),(0,2), \ldots,(4,5)$ : by that bijection the line corresponding to the pair $(i, j)$ is the line through the points $p_{i \alpha}^{\prime}$ and $p_{j \alpha}^{\prime}$.

Inspired by this, let $\mathcal{T}_{6}^{\prime}$ be the matroid with atoms $\{1, \ldots, 15\}$ and non-bases all the order three subsets of the following sets

$\{1,12,13\},\{3,6,15\},\{3,8,12\},\{5,8,10\},\{1,2,3,4,5\},\{1,6,7,8,9\}$, $\{2,6,10,11,12\},\{3,7,10,13,14\},\{4,8,11,13,15\},\{5,9,12,14,15\}$.

One computes that the moduli space $\mathcal{R}\left(\mathcal{T}_{6}^{\prime}\right)$ of realizations is 1-dimensional. Corresponding to the above description of the non-bases, a realization $\mathcal{C}$ is a union of 15 lines which has four triple points and six 5-points; moreover $\mathcal{C}$ has 33 double points. The six 5-points of a realization $\mathcal{C}_{\theta}$ in $\mathcal{R}\left(\mathcal{T}_{6}^{\prime}\right)$ are

$\mathcal{P}_{\theta}:(0: 0: 1),(0: 1: 0),(-1: 1: 1),(\theta: 0: 1),(-\theta: 1: 0),(-\theta-1: 1: 1)$, for $\theta \in \mathbb{P}^{1}$ not in the zero loci of the polynomials

$$
x+1, x, 2 x+1, x-1, x^{2}+x+1, x^{2}-x-1
$$

The line arrangement $\mathcal{L}_{\{2\}}\left(\mathcal{P}_{\theta}\right)$ is the realization $\mathcal{C}_{\theta}$ of $\mathcal{T}_{6}^{\prime}$. Then a direct computation shows that the map

$$
\left(E_{\theta}, \alpha\right) \rightarrow \mathcal{C}_{\theta}
$$

is a map from $X_{1}(6)^{\circ}$ to $\mathcal{R}\left(\mathcal{T}_{6}^{\prime}\right)$ and that this map has degree 1 (here $X_{1}(6)^{\circ}$ is the complement of the cusps). The curve $\mathcal{R}\left(\mathcal{T}_{6}^{\prime}\right)$ is smooth.

- Case $n=7$. When $n \geq 7$, we can take the points $p_{0}, \ldots, p_{3}$ to be the canonical basis. The moduli space $\mathcal{R}\left(\mathcal{T}_{7}\right)$ of realizations of $\mathcal{T}_{7}$ is one dimensional and irreducible. The seven points of a realization $\mathcal{C}$ of $\mathcal{T}_{7}$ are the four points of the canonical base and the points

$$
(0: 1: 1),(1: 0: t),(t-1, t, 0)
$$

for $t \notin\{0,1\}$. The universal elliptic curve with $\mathbb{Z} / 7 \mathbb{Z}$-torsion is

$$
E_{t}: y^{2}+\left(1+t-t^{2}\right) y x+\left(t^{2}-t^{3}\right) y=x^{3}+\left(t^{2}-t^{3}\right) x
$$

and $\alpha=(0: 0: 1)$ has order 7 (see e.g. [22]). Using the period map, one can check that the map $\phi: X_{1}(7)^{\circ} \rightarrow \mathcal{R}\left(\mathcal{T}_{7}\right)$ defined by

$$
\left(E_{t}, \alpha\right) \rightarrow(k \alpha)_{k \in \mathbb{Z} / 7 \mathbb{Z}}
$$

has degree 1 , where $X_{1}(7)^{\circ}$ is the complement of the cusps.

- Case $n=8$. The non-bases of the matroid $\mathcal{T}_{8}$ are

$$
\{0,1,7\},\{0,2,6\},\{0,3,5\},\{1,2,5\},\{1,3,4\},\{3,6,7\},\{4,5,7\}
$$

One computes that the moduli space $\mathcal{R}\left(\mathcal{T}_{8}\right)$ is one-dimensional and irreducible; the eight points of a realization $\mathcal{P}=\left(p_{i}\right)_{i \in \mathbb{Z} / 8 \mathbb{Z}}$ of $\mathcal{T}_{8}$ are

$$
\begin{aligned}
& (1: 0: 0),(0: 1: 0),(1: 1: 1),(0: 0: 1) \\
& (0: t:-1),(1: 0: 1),(1: t: t),(1: t: 0)
\end{aligned}
$$

for $t \notin\{0, \pm 1, \infty\}$. Using the universal elliptic curve with 8-torsion elements (see [1]), one can check that the map $(E, \alpha) \in X_{1}(8)^{\circ} \rightarrow(k \alpha)_{k \in \mathbb{Z} / 8 \mathbb{Z}} \in$ $\mathcal{R}\left(\mathcal{T}_{8}\right)$ is well-defined and has degree one onto its image, where $X_{1}(8)^{\circ}$ is the complement of the cusps.

- Case $n=9$. Up to a projective transformation, the 9 points of a realization of $\mathcal{T}_{9}$ are

$$
\begin{gathered}
(1: 0: 0),(0: 1: 0),(1: 1: 1),(0: 0: 1),(t: t: t-1) \\
\quad(0: t: t-1),(1: 0: 1),(1: t: t),(1: t: 0)
\end{gathered}
$$

for $t \notin\left\{0,1, \frac{1 \pm \sqrt{-3}}{2}, \infty\right\}$. As for $n=7,8$, one may use the universal elliptic curve to check that the map $\phi: X_{1}(9)^{\circ} \rightarrow \mathcal{R}\left(\mathcal{T}_{9}\right)$ has degree 1 .

- Case $n \geq 10$. We will now study $\mathcal{R}\left(\mathcal{T}_{n}\right)$ for $n \geq 10$. Here is an outline of our approach.

We begin by defining a sequence $\left(p_{k}\right)_{k \in \mathbb{Z}}$ of points in $\mathbb{P}^{2}$ such that $p_{0}, p_{1}, p_{2}$ are not on the same line, and for all sets $\{i, j, k\} \subset \mathbb{Z}$ of three distinct integers such that $i+j+k=0$, the points $p_{i}, p_{j}, p_{k}$ are on a line. We focus on which conditions that sequence becomes exactly $n$-periodic, so that this gives a realization of $\mathcal{T}_{n}$. We prove that the coordinates of the points $\left(p_{k}\right)_{k \in \mathbb{Z}}$ are parametrized by fractions of some variables $s, t$, which are subject to some relations and inequalities. Using that $n \geq 10$, one shows that there is a unique cubic curve $E$ that contains the points $\left(p_{k}\right)_{k \in \mathbb{Z}}$. In case that cubic curve is smooth, it proves that the realization $\left(p_{k}\right)_{k \in \mathbb{Z} / n \mathbb{Z}}$ is the image by $\phi$ of a point of the modular curve, namely the point corresponding to the pair $\left(E, p_{1}\right)$. We then focus to the case when $E$ is singular; then $E$ is a nodal cubic curve and the realization $\left(p_{k}\right)_{k \in \mathbb{Z} / n \mathbb{Z}}$ of $\mathcal{T}_{n}$ is a cyclic sub-group on the smooth part of $E$, for the natural group law with neutral element $p_{0}$.

From the hypothesis on the sequence $\left(p_{k}\right)_{k \in \mathbb{Z}}$, and up to projective transformation, one can suppose that

$$
p_{0}=(1: 0: 0), p_{1}=(0: 1: 0), p_{2}=(0: 0: 1), p_{3}=(1: 1: 1)
$$

Let us suppose moreover that the sequence is $n$-periodic; it will be convenient for us to think of the data of $p_{i}$ as an $n$-periodic size $\mathbb{Z} \times 3$ matrix with rows giving $p_{i}$, and we will now look at the consequences of the collinearity for $p_{a}, p_{b}, p_{c}$ for $a+b+c=0$. We will denote the three coordinates on $\mathbb{P}^{2}$ as $\left(x_{1}: x_{2}: x_{3}\right)$.

The line $\overline{p_{1} p_{2}}=\left\{x_{1}=0\right\}$ contains $p_{-3}=p_{n-3}$, but since no other points are on this line, we may assume that $p_{i}=\left(1: y_{i, 2}: y_{i, 3}\right)$ for all $i \notin\{-3,1,2\} \bmod n$. Also note that since $p_{-3} \notin \overline{p_{0} p_{2}}=\left\{x_{2}=0\right\}$, we have $p_{-3}=\left(0: 1: y_{-3,3}\right)$.

The realization space of $\mathcal{T}_{n}$ is given by periodicity and vanishing of the minors for rows $a, b, c$ with $a+b+c=0 \bmod n$, as well as nonvanishing of the rest of the $3 \times 3$ minors. Let us denote the minor of the rows labeled $a, b, c \in \mathbb{Z} / n \mathbb{Z}$ by $\operatorname{det}_{a, b, c}$.

The point $p_{-1}$ lies on the line $\overline{p_{0} p_{1}}=\left\{x_{3}=0\right\}$. On the other hand, it does not lie on $\overline{p_{0} p_{2}}=\left\{x_{2}=0\right\}$. Therefore,

$$
p_{-1}=(1: s: 0), s \neq 0
$$

To be more precise, the vanishing and nonvanishing of the appropriate determinants eliminates the entry $y_{-1,3}$ and forces $y_{-1,2} \neq 0$. Similarly, $p_{-3}$ lies on the intersection of the lines $\overline{p_{1} p_{2}}=\left\{x_{1}=0\right\}$ and $\overline{p_{0} p_{3}}=\left\{x_{2}=x_{3}\right\}$ so

$$
p_{-3}=(0: 1: 1)
$$

The vanishing of $\operatorname{det}_{-2,0,2}=-y_{-2,2}$ and $\operatorname{det}_{-2,-1,3}=s-y_{-2,2}+y_{-2,3}-s y_{-2,3}$ yields

$$
p_{-2}=\left(1: 0: \frac{s}{s-1}\right)
$$

where $s-1$ is invertible since $\operatorname{det}_{-1,2,3}=s-1$ is nonzero. We then compute det $_{-4,1,3}=1-y_{-4,3}$ and denote $t=y_{-4,2}$, so that

$$
p_{-4}=(1: t: 1)
$$

Then $\operatorname{det}_{-4,0,4}=y_{4,2}-t y_{4,3}=0$ and $\operatorname{det}_{-3,-1,4}=-s+y_{4,2}-y_{4,3}$ allows :us to solve for

$$
p_{4}=\left(1: \frac{s t}{t-1}: \frac{s}{t-1}\right)
$$

where we know that $t-1$ is invertible because it is equal to $\operatorname{det}_{-4,2,3}$. We can also compute $p_{5}$ by using det ${ }_{-3,-2,5}=\frac{s}{s-1}+y_{5,2}-y_{5,3}$ and $\operatorname{det}_{-4,-1,5}=$ $-s+y_{5,2}+s y_{5,3}-t y_{5,3}$. We get

$$
p_{5}=\left(1: \frac{(s(-1+t))}{(s-1)(1+s-t)}: \frac{s^{2}}{(s-1)(1+s-t)}\right)
$$

where $(1+s-t)$ is invertible because $\operatorname{det}_{-4,-3,4}=-1-s+t$.

We now observe that there is a unique up to scaling cubic curve that passes through 9 points $p_{-3}, \ldots, p_{5}$. (There was a dimension two space of cubics through $p_{-4}, \ldots, p_{4}$.) We used Mathematica to compute the size 9 minors of the matrix of the values of the 10 cubic monomials to see that one of them equals

$$
\frac{s^{8}(1-t+s t)}{(-1+s)^{4}(1+s-t)^{2}(-1+t)}
$$

We know that $1-t+s t$ is invertible because $\operatorname{det}_{-4,-3,5}=\frac{1-t+s t}{s-1}$. This implies that the matrix of values of the 10 cubic monomials at the above 9 points has rank 9 . Its nullspace is one-dimensional and gives a unique cubic through the 9 points. Explicitly, this cubic is

$$
\begin{gathered}
E=\left\{F_{s, t}=0\right\}=\left\{-s^{2} x_{1}^{2} x_{2}+s x_{1} x_{2}^{2}+s t x_{1}^{2} x_{3}+\left(s^{2}-s-t\right) x_{1} x_{2} x_{3}\right. \\
\left.+(1-s) x_{2}^{2} x_{3}+t(1-s) x_{1} x_{3}^{2}+(s-1) x_{2} x_{3}^{2}=0\right\}
\end{gathered}
$$

If the cubic $E$ is non-singular (which is generically the case), the $n$ points $p_{k}=k p_{1}, k \in \mathbb{Z} / n \mathbb{Z}$ on $E$ form a cyclic torsion sub-group (see also Remark 3.3 below).

Let us study when $E$ is singular and which singularities can occur. First note that the partial derivatives of $F_{s, t}$ at $p_{0}$ are $0,-s^{2}$, st respectively, which means that $E$ is smooth at $p_{0}$. We can also see that the line $s x_{2}=t x_{3}$ is triple-tangent to $E$ at $p_{0}$ unless $s=t$, which is impossible because $\operatorname{det}_{-2,1,4}=$ $\frac{s(s-t)}{(-1+s)(-1+t)}$. Moreover, the partial derivative $\frac{\partial F_{s, t}}{\partial x_{1}}$ is

$$
-\left(2 s x_{1}-x_{2}+(1-s) x_{3}\right)\left(s x_{2}-t x_{3}\right)
$$

so singular points can occur only at $2 s x_{1}-x_{2}+(1-s) x_{3}=0$. The restrictions of $\frac{\partial F_{s, t}}{\partial x_{2}}$ and $\frac{\partial F_{s, t}}{\partial x_{3}}$ to this line are respectively

$$
\begin{gathered}
3 s^{2} x_{1}^{2}+\left(5 s-5 s^{2}-t\right) x_{1} x_{3}+(-1+s)(-1+2 s) x_{3}^{2} \\
-s\left(-2 s+2 s^{2}+t\right) x_{1}^{2}+(-1+s)\left(s+3 s^{2}-t\right) x_{1} x_{3}-(-1+s)^{2}(1+s) x_{3}^{2}
\end{gathered}
$$

We can take a resultant and find that the cubic $E$ is singular if and only if (using the known nonzero factors)

$$
-9 s+3 s^{2}+5 s^{3}+s^{4}+t+10 s t-11 s^{2} t-t^{2}=0
$$

The singular point is given by

$$
\left(1: \frac{3 s+4 s^{2}+s^{3}+t-8 s t}{4-s+s^{2}-3 t}: \frac{5 s-6 s^{2}+s^{3}-t+2 s t}{(-1+s)\left(4-s+s^{2}-3 t\right)}\right)
$$

In particular, $E$ will have at most one singular point, a node or a cusp.

Remark 3.3. Whether or not $E$ is singular, it is clear that the points $p_{k}$ must form an order $n$ subgroup of the group of smooth points of $E$. Their coordinates can be computed inductively as rational functions in $s$ and $t$. (Indeed, from the property that if $i+j+k=0$ then the points $p_{i}, p_{j}, p_{k}$ are aligned, one may find the point $p_{k+1}\left(\right.$ or $\left.p_{-(k+1)}\right)$ as the intersection point of two lines passing through points in the set $\left\{p_{-k}, \ldots, p_{k}\right\}$.) Then $\mathcal{R}\left(\mathcal{T}_{n}\right)$ will be a closed subscheme of a Zariski open set in $\mathbb{C}^{2}$. The Zariski open set is given by the nonvanishing of the determinants, and the closed subscheme will be cut out by the $n$-periodicity conditions $p_{k}=p_{k+n}$.

The curve (3.1) is rational, and can be parameterized by

$$
(s, t)=\left(\frac{r^{2}-1}{5 r^{2}-1}, \frac{8\left(r-3 r^{2}+4 r^{4}\right)}{\left(5 r^{2}-1\right)^{2}}\right)
$$

In fact, we can also parameterize its double cover that picks the branches at the node as

$$
(s, t)=\left(\frac{\left(-1+w^{2}\right)\left(3+w^{2}\right)}{1+10 w^{2}+5 w^{4}}, \frac{32 w^{4}\left(1+w^{2}\right)\left(3+w^{2}\right)}{\left(1+10 w^{2}+5 w^{4}\right)^{2}}\right)
$$

Under this parameterization, the singularity occurs at

$$
\left(1: \frac{4 w^{2}\left(3+w^{2}\right)}{1+10 w^{2}+5 w^{4}}: \frac{3+w^{2}}{2\left(1+w^{2}\right)}\right)
$$

and one may that way obtain the equation of the curve $F_{s, t}$ in terms of $w$. We parameterize the smooth locus of the cubic curve by (generically)

$$
\begin{gathered}
\left(x_{1}: x_{2}: x_{3}\right)=\left(1: \frac{4(-1+v)(-1+w) w^{2}(1+w)\left(3+w^{2}\right)\left(-1+v-2 w-2 v w-w^{2}+v w^{2}\right)}{(1+v-w+v w)\left(-1-v-3 w+3 v w-3 w^{2}-3 v w^{2}-w^{3}+v w^{3}\right)\left(1+10 w^{2}+5 w^{4}\right)}\right. \\
\left.\quad: \frac{(-1+v)(-1+w)^{2}(1+w)^{2}(-1-v-w+v w)\left(3+w^{2}\right)}{2\left(1+w^{2}\right)\left(-1+v+2 w+2 v w-w^{2}+v w^{2}\right)\left(-1-v-3 w+3 v w-3 w^{2}-3 v w^{2}-w^{3}+v w^{3}\right)}\right)
\end{gathered}
$$

so that the tangent lines to branches at singular points correspond to $v=$ $0, \infty$ and $v=1$ gives $p_{0}$. Then $v=\frac{w-1}{w+1}$ gives $p_{1}$. The group law on the nodal cubic then implies that $p_{n}$ corresponds to $v=\left(\frac{w-1}{w+1}\right)^{n}$, so the $n$-periodicity and lack of smaller periods implies that the solutions correspond to

$$
\frac{w-1}{w+1}=\zeta^{a}
$$

where $\operatorname{gcd}(a, n)=1$ and $\zeta=\mathrm{e}^{2 \pi \mathrm{i} / n}$. We can compute the points $p_{k}$ for $k \neq-3,1,2 \bmod n$ to find

$$
p_{k}=\left(1: \frac{\left(1-\zeta^{2 a}\right)\left(1+\zeta^{3 a}\right)\left(1-\zeta^{a k}\right)\left(1-\zeta^{a(k+2)}\right)}{\left(1-\zeta^{5 a}\right)\left(1-\zeta^{a(k-1)}\right)\left(1-\zeta^{a(k+3)}\right)}: \frac{\left(1-\zeta^{a}+\zeta^{2 a}\right)\left(1-\zeta^{a k}\right)\left(1-\zeta^{a(k+1)}\right)}{\left(1+\zeta^{2 a}\right)\left(1-\zeta^{a(k-2)}\right)\left(1-\zeta^{a(k+3)}\right)}\right)
$$

with $p_{1}=(0: 1: 0), p_{2}=(0: 0: 1), p_{-3}=(0: 1: 1)$.

Remark 3.4. We will later see the above realizations of $\mathcal{T}_{n}$ as images of certain cusps of the modular curve $X_{1}(n)$.

Summarizing, we obtained that:

Proposition 3.5. For $n \geq 10$, the realization space $\mathcal{R}\left(\mathcal{T}_{n}\right)$ is set-theoretically equal to the union of the image $\phi_{n}\left(X_{1}(n)^{\circ}\right)$ of the complement of $X_{1}(n)^{\circ}$ of the cusps in the modular curve $X_{1}(n)$ and the points in Equation (3.2).

Proof. If $E$ is nonsingular, then we see that the configuration $\left\{p_{k}\right\}$ is in the image of $X_{1}(n)^{\circ}$, and the singular case has been computed above.

We will later prove that $\mathcal{R}\left(\mathcal{T}_{n}\right)$ is a smooth curve, but for now we will only argue that the tangent space to $\mathcal{R}\left(\mathcal{T}_{n}\right)$ at any configuration $\mathbf{p}=\left\{p_{k}\right\}$ is of dimension at most one.

Proposition 3.6. Let $\mathbf{p}=\left\{p_{k}\right\}$ be a specific realization of $\mathcal{T}_{n}$ over $\mathbb{C}$. Then the tangent space to $\mathcal{R}\left(\mathcal{T}_{n}\right)$ at $\mathbf{p}$ is at most one-dimensional.

Proof. We saw in Remark 3.3 that $\mathcal{R}\left(\mathcal{T}_{n}\right)$ is locally given by vanishing and non-vanishing of some polynomials in $(s, t)$. As above, we consider the cubic curve $E_{\mathbf{p}}$ passing through the points in $\mathbf{p}$. There is a group structure on the space of $\mathbb{C}[\varepsilon] /\left(\varepsilon^{2}\right)$-points in the smooth part of $E_{\mathbf{p}}$. Pick a nonzero deformation $p_{1}(\varepsilon)$ of $p_{1}=(0: 1: 0)$ and consider the $\mathbb{C}[\varepsilon] /\left(\varepsilon^{2}\right)$ matrix of size $\mathbb{Z} \times 3$ where $p_{k}$ is given by

$$
p_{k}=k p_{1}(\varepsilon) \bmod \varepsilon^{2}
$$

Note that this matrix will no longer be periodic, but it will satisfy the vanishing of $\operatorname{det}_{a_{1}, a_{2}, a_{3}}$ with $a_{1}+a_{2}+a_{3}=0$ modulo $\varepsilon^{2}$. We can multiply it by an invertible matrix with values in $\mathbb{C}[\varepsilon] /\left(\varepsilon^{2}\right)$ to get the points $p_{0}, \ldots, p_{3}$
into the standard form. This provides a tangent vector to $\mathbf{p}$ in the $\mathbb{C}^{2}$ with coordinates $(s, t)$ that is not tangent to $\mathcal{R}\left(\mathcal{T}_{n}\right)$, and the claim follows.

Remark 3.7. If we knew that the realization space is connected, the above Proposition 3.6 would imply that it is a smooth curve. We will prove it in Section 5 .

Remark 3.8. It is sensible to ask about the compactification of the realization space of $\mathcal{T}_{n}$ in $\left(\mathbb{P}^{2}\right)^{n-4}$. We will do it in the latter sections.

A priori, it is not obvious that the scheme-theoretic analog of the above Proposition 3.5 holds, although Proposition 3.6 comes pretty close. We will prove it in Section 5

## 4. LOG-DERIVATIVES OF THE THETA FUNCTION

In this section we recall some known results about log-derivatives of the theta functions that almost generate the ring of modular forms for the congruence subgroup $\Gamma_{1}(n)$.

We start with the Jacobi theta function $\theta: \mathbb{C} \times \mathbb{H} \rightarrow \mathbb{C}$ defined by

$$
\theta(z, \tau)=\mathrm{e}^{\frac{\pi \mathrm{i} \tau}{4}}(2 \sin \pi z) \prod_{l=1}^{\infty}\left(1-\mathrm{e}^{2 \pi \mathrm{i} l \tau}\right) \prod_{l=1}^{\infty}\left(1-\mathrm{e}^{2 \pi \mathrm{i}(l \tau+z)}\right) \prod_{l=1}^{\infty}\left(1-\mathrm{e}^{2 \pi \mathrm{i}(l \tau-z)}\right)
$$

The convergence of the product is clear, as are the transformation properties $\theta(-z, \tau)=-\theta(z, \tau), \theta(z+1, \tau)=\theta(z, \tau), \theta(z+\tau, \tau)=-\mathrm{e}^{-2 \pi \mathrm{i} z-\pi \mathrm{i} \tau} \theta(z, \tau)$.

It is also easy to show that for fixed $\tau$ the function $\theta(z, \tau)$ has a simple zero precisely at $z \in L=\mathbb{Z}+\mathbb{Z} \tau$. It is notably harder to prove, but $\theta$ also satisfies a nice functional equation under the Jacobi transformations

$$
(z, \tau) \rightarrow\left(\frac{z}{c z+d}, \frac{a \tau+b}{c \tau+d}\right)
$$

for $\left(\begin{array}{ll}a & b \\ c & d\end{array}\right) \in \mathrm{SL}(2, \mathbb{Z})$, see [8].

Let $n \geq 3$ be a positive integer. For integers $a$ not divisible by $n$ we introduce the functions

$$
r_{a}(z, \tau)=\frac{\theta\left(\frac{a}{n}+z, \tau\right) \theta_{z}(0, \tau)}{\theta(z, \tau) \theta\left(\frac{a}{n}, \tau\right)}
$$

where $\theta_{z}$ is the partial derivative with respect to $z$. We will routinely suppress their dependence on the variable $\tau$ in our notation. Properties of $\theta$ imply that functions $r_{a}(z)$ have a simple zero at $z=-\frac{a}{n} \bmod L$, a pole of order one at $L$ and the transformation properties

$$
r_{a}(z+1)=r_{a}(z), r_{a}(z+\tau)=\zeta_{n}^{-a} r_{a}(z)
$$

where $\zeta_{n}$ denotes $\mathrm{e}^{\frac{2 \pi \mathrm{i}}{n}}$. The $z$-independent factors of $r_{a}(z)$ are picked in a way to assure that the residue of $r_{a}(z)$ at $z=0$ is equal to 1 , so we have the Laurent expansion

$$
\frac{1}{z}+s_{a}+t_{a} z+u_{a} z^{2}+\ldots
$$

where $s_{a}, t_{a}, u_{a}$ are functions of $\tau$. In particular, the product expansion of $\theta$ implies that

$$
s_{a}(\tau)=\frac{\theta_{z}\left(\frac{a}{n}, \tau\right)}{\theta\left(\frac{a}{n}, \tau\right)}=2 \pi \mathrm{i}\left(\frac{\zeta_{n}^{a}+1}{2\left(\zeta_{n}^{a}-1\right)}-\sum_{d>0} \mathrm{e}^{2 \pi \mathrm{i} d \tau} \sum_{k \mid d}\left(\zeta_{n}^{k a}-\zeta_{n}^{-k a}\right)\right)
$$

The functions $s_{a}=s_{a}(\tau)$ are modular forms of weight 1 for the congruence subgroup $\Gamma_{1}(n) \subset \mathrm{S} L(2, \mathbb{Z})$. They depend on $a \bmod n$ only and satisfy $s_{-a}=$ $-s_{a}$. Similarly, $t_{a}$ and $u_{a}$ are modular forms of weight 2 and 3 respectively, and they satisfy $t_{-a}=t_{a}$ and $u_{-a}=-u_{a}$.

It has been shown in [4, 6] that $s_{a}$ almost generate the ring of modular forms for $\Gamma_{1}(n)$. Namely, any modular form of weight 3 or higher can be expressed as a polynomial in $s_{a}$. The situation is notably more complicated for weight 2 where the cuspidal part of the span of $s_{a} s_{b}$ is precisely the span of Hecke eigenforms of analytic rank zero, see [3. There is also a similar statement involving the Wronskians of $s_{a}$ and $s_{b}$, see [2].

In addition to the symmetry relations, the forms $s_{a}$ and $t_{a}$ satisfy the following.

Proposition 4.1. If $a, b, c$ are nonzero elements of $\mathbb{Z} / n \mathbb{Z}$ such that $a+b+c=$ $0 \bmod n$, then

$$
s_{a} s_{b}+s_{b} s_{c}+s_{c} s_{a}+t_{a}+t_{b}+t_{c}=0
$$

Proof. Since $\zeta_{n}^{a} \zeta_{n}^{b} \zeta_{n}^{c}=1$, the product $r_{a}(z) r_{b}(z) r_{c}(z)$ is elliptic with respect to $L$. Its only poles are at $z \in L$, thus the residue at $z=0$ must be zero. It remains to use the expansion (4.2).

Remark 4.2. For large enough n, these are not the only degree two relations on $s_{a}, t_{a}$ due to presence of Hecke eigenforms of positive analytic rank. However, for $n$ prime the above relations cut out $X_{1}(n)$ scheme-theoretically [5].

Recall that the Weierstrass $\mathcal{P}$ function defined as

$$
\mathcal{P}(z)=\frac{1}{z^{2}}+\sum_{l \in L, l \neq 0}\left(\frac{1}{(z-l)^{2}}-\frac{1}{l^{2}}\right)
$$

and its derivative $\mathcal{P}^{\prime}(z)$ can be used to embed $E=\mathbb{C} / L$ into $\mathbb{C P}^{2}$ by

$$
z \mapsto \begin{cases}\left(\mathcal{P}(z): \mathcal{P}^{\prime}(z): 1\right), & z \notin L \\ (0: 1: 0), & z \in L\end{cases}
$$

In what follows we find the expression for the values of the Weierstrass function and its derivative at $\frac{a}{n}$ in terms of $s, t, u$. The latter will not be used in the rest of the paper but is easy to get with the same method.

Proposition 4.3. Let $\mathcal{P}(z)$ be the Weierstrass function for the lattice $L$. Then

$$
\mathcal{P}\left(\frac{a}{n}\right)=s_{a}^{2}-2 t_{a}, \mathcal{P}^{\prime}\left(\frac{a}{n}\right)=-2 s_{a}^{3}+6 s_{a} t_{a}-6 u_{a}
$$

Proof. Consider

$r_{a}(z) r_{-a}(z)=\left(\frac{1}{z}+s_{a}+t_{a} z+\ldots\right)\left(\frac{1}{z}-s_{a}+t_{a} z+\ldots\right)=\frac{1}{z^{2}}-s_{a}^{2}+2 t_{a}+\ldots$

It is an elliptic function with only pole of order 2 at $z=0$. Moreover, since its Laurent power series has coefficient 1 at $z^{-2}$, it is equal to

$$
\mathcal{P}(z)-s_{a}^{2}+2 t_{a}
$$

because the Laurent expansion of $\mathcal{P}(z)$ has coefficients 1 and 0 at $z^{-2}$ and $z^{0}$ respectively. Since $r_{a}\left(\frac{a}{n}\right)=0$, we get $\mathcal{P}\left(\frac{a}{n}\right)=s_{a}^{2}-2 t_{a}$.

We can find the value of the derivative $\mathcal{P}^{\prime}\left(\frac{a}{n}\right)$ by a similar calculation. We consider

$$
\begin{array}{r}
r_{a}^{\prime}(z) r_{-a}(z)=\left(-\frac{1}{z^{2}}+t_{a}+2 u_{a} z+\ldots\right)\left(\frac{1}{z}-s_{a}+t_{a} z-u_{a} z^{2}+\ldots\right) \\
=-\frac{1}{z^{3}}+s_{a} \frac{1}{z^{2}}+\left(3 u_{a}-s_{a} t_{a}\right)+\ldots
\end{array}
$$

which is an elliptic function with pole of order 3 at $z=0$ and is therefore a linear combination of $\mathcal{P}^{\prime}(z), \mathcal{P}(z)$ and 1 . Since $\mathcal{P}^{\prime}$ and $\mathcal{P}$ do not have any constant terms in their Laurent expansions at $z=0$, we get

$$
r_{a}^{\prime}(z) r_{-a}(z)=\frac{1}{2} \mathcal{P}^{\prime}(z)+s_{a} \mathcal{P}(z)+\left(3 u_{a}-s_{a} t_{a}\right)
$$

As before, we get

so

$$
\frac{1}{2} \mathcal{P}^{\prime}\left(\frac{a}{n}\right)+s_{a} \mathcal{P}\left(\frac{a}{n}\right)+\left(3 u_{a}-s_{a} t_{a}\right)=0
$$

$$
\mathcal{P}^{\prime}\left(\frac{a}{n}\right)=-2 s_{a} \mathcal{P}\left(\frac{a}{n}\right)-6 u_{a}+2 s_{a} t_{a}=-2 s_{a}^{3}+6 s_{a} t_{a}-6 u_{a}
$$

We will now prove several relations on $s_{a}$ and $t_{a}$ that will be used later in the paper. They are also of independent interest. We start with a simple formula which relates the product of two $r$ functions with another $r$ function and its derivative.

Proposition 4.4. For $a, k \bmod n$ such that $a, k, a+k \neq 0 \bmod n$, we have

$$
r_{a}(z) r_{k}(z)=-r_{a+k}^{\prime}(z)+\left(s_{a}+s_{k}\right) r_{a+k}(z)
$$

Proof. The product $r_{a}(z) r_{k}(z)$ is an almost periodic function for $L$, with $\mathbb{Z} / n \mathbb{Z}$ character $-(a+k)$ and double pole at 0 . The space of such functions is two-dimensional, by the Riemann-Roch formula. Both $r_{a+k}^{\prime}$ and $r_{a+k}$ are in this space and they are linearly independent due to their Laurent
expansions at $z=0$. Finally, we can find the precise coefficients by looking at the Laurent expansion

$$
r_{a}(z) r_{k}(z)=\left(\frac{1}{z}+s_{a}+\ldots\right)\left(\frac{1}{z}+s_{k}+\ldots\right)=\frac{1}{z^{2}}+\left(s_{a}+s_{k}\right) \frac{1}{z}+\ldots
$$

Proposition 4.5. Let $a, b \bmod n$ be different nonzero elements of $\mathbb{Z} / n \mathbb{Z}$. Then for any $k \notin\{a-b, 0, a,-b\} \bmod n$ the product

$$
\left(s_{k+b-a}-s_{k}-s_{b}+s_{a}\right)\left(s_{k+b}-s_{k-a}-s_{b}-s_{a}\right)
$$

is the same. Specifically, it equals $s_{b}^{2}-s_{a}^{2}+2 t_{a}-2 t_{b}$.

Proof. After a rather miraculous rearrangement of the terms, the product is equal to

$$
\begin{array}{r}
s_{b}^{2}-s_{a}^{2}+\left(s_{k+b-a}\left(s_{k+b}-s_{a}\right)+s_{a} s_{k+b}\right)-\left(s_{k+b-a}\left(s_{k-a}+s_{b}\right)-s_{b} s_{k-a}\right) \\
-\left(s_{k}\left(s_{k+b}-s_{b}\right)+s_{b} s_{k+b}\right)+\left(s_{k}\left(s_{k-a}+s_{a}\right)-s_{a} s_{k-a}\right) \\
=s_{b}^{2}-s_{a}^{2}+\left(t_{k+b-a}+t_{k+b}+t_{a}\right)-\left(t_{k+b-a}+t_{k-a}+t_{b}\right)-\left(t_{k}+t_{k+b}+t_{b}\right) \\
+\left(t_{k}+t_{k-a}+t_{a}\right)=s_{b}^{2}-s_{a}^{2}+2 t_{a}-2 t_{b}
\end{array}
$$

Here we used relations $s_{i} s_{j}+s_{j} s_{k}+s_{i} s_{k}+t_{i}+t_{j}+t_{k}=0$ for $i+j+k=0 \bmod n$ proved in Proposition 4.1 and symmetry relations $s_{-i}=-s_{i}, t_{-j}=t_{j}$.

Corollary 4.6. If $a \neq \pm b \bmod n$ and $k \notin\{a-b, 0, a,-b\} \bmod n$ the weight one modular form $s_{k+b-a}-s_{k}-s_{b}+s_{a}$ has zeros only at the cusps of $X_{1}(n)$.

Proof. By Propositions 4.5 and 4.3 ,

$$
\left(s_{k+b-a}-s_{k}-s_{b}+s_{a}\right)\left(s_{k+b}-s_{k-a}-s_{b}-s_{a}\right)=\mathcal{P}\left(\frac{b}{n}\right)-\mathcal{P}\left(\frac{a}{n}\right)
$$

It remains to observe that $\mathcal{P}\left(\frac{a}{n}\right)=\mathcal{P}\left(\frac{b}{n}\right)$ implies that $\frac{a}{n} \in\left\{ \pm \frac{b}{n}\right\} \bmod L$.

Corollary 4.7. For $n \geq 7$ and $k \notin\{-3,-1,0,2\} \bmod n$, there holds

$$
\frac{s_{4}-2 s_{3}+s_{2}}{s_{k+1}-s_{k}+s_{2}-s_{3}}=\frac{s_{k+3}-s_{k-2}-s_{3}-s_{2}}{s_{6}-s_{3}-s_{2}-s_{1}}
$$

as an equality of modular functions for $\Gamma_{1}(n)$.

Proof. As a consequence of Proposition 4.5 for $a=2$ and $b=3$ there holds

$\left(s_{k+1}-s_{k}-s_{3}+s_{2}\right)\left(s_{k+3}-s_{k-2}-s_{3}-s_{2}\right)=\left(s_{4}-2 s_{3}+s_{2}\right)\left(s_{6}-s_{3}-s_{2}-s_{1}\right)$ because the right hand side is the value at $k=3$.

Corollary 4.8. For $n \geq 7$ and $k \notin\{-3,-2,0,1\} \bmod n$, there holds

$$
\frac{s_{5}-2 s_{3}+s_{1}}{s_{k+2}-s_{k}+s_{1}-s_{3}}=\frac{s_{k+3}-s_{k-1}-s_{3}-s_{1}}{s_{6}-s_{3}-s_{2}-s_{1}}
$$

as an equality of modular functions for $\Gamma_{1}(n)$.

Proof. As a consequence of Proposition 4.5 for $a=1$ and $b=3$, for any $k \notin\{-3,-2,0,1\} \bmod n$ there holds

$\left(s_{k+2}-s_{k}-s_{3}+s_{1}\right)\left(s_{k+3}-s_{k-1}-s_{3}-s_{1}\right)=\left(s_{5}-2 s_{3}+s_{1}\right)\left(s_{6}-s_{3}-s_{2}-s_{1}\right)$

because the right hand side is the value at $k=3$.

We will now also compute the values of $s_{k}$ at the cusps of $X_{1}(n)$. Every cusp of $X_{1}(n)$ can be represented by $\frac{a}{c} \in \mathbb{Q}$ and written as $\gamma(\mathrm{i} \infty)$ for some $\gamma=$ $\left(\begin{array}{ll}a & b \\ c & d\end{array}\right) \in S L(2, \mathbb{Z})$, so we need to understand $\lim _{\tau \rightarrow \mathrm{i \infty}}(c \tau+d)^{-1} s_{k}\left(\frac{a \tau+b}{c \tau+d}\right)$.

Proposition 4.9. If $\frac{k c}{n} \notin \mathbb{Z}$, the value of $s_{k}$ at the cusp $\frac{a}{c}$ is

$$
\lim _{\tau \rightarrow \mathrm{i} \infty}(c \tau+d)^{-1} s_{k}\left(\frac{a \tau+b}{c \tau+d}\right)=(2 \pi \mathrm{i})\left(\left\{\frac{k c}{n}\right\}-\frac{1}{2}\right)
$$

and if $\frac{k c}{n} \in \mathbb{Z}$ we get

$$
\lim _{\tau \rightarrow \mathrm{i} \infty}(c \tau+d)^{-1} s_{k}\left(\frac{a \tau+b}{c \tau+d}\right)=(2 \pi \mathrm{i})\left(-\frac{1}{2}-\frac{\zeta_{n}^{k d}}{1-\zeta_{n}^{k d}}\right)=(2 \pi \mathrm{i}) \frac{\zeta_{n}^{k d}+1}{2\left(\zeta_{n}^{k d}-1\right)}
$$

where $\zeta_{n}=\mathrm{e}^{2 \pi \mathrm{i} / n}$.

Proof. By [8], we have

$$
\theta\left(\frac{z}{c \tau+d}, \frac{a \tau+b}{c \tau+d}\right)=\xi(c \tau+d)^{\frac{1}{2}} \mathrm{e}^{\frac{\pi \mathrm{ic} z^{2}}{c \tau+d}} \theta(z, \tau)
$$

for some constant $\xi$, so we get

$$
\log \theta\left(\frac{z}{c \tau+d}, \frac{a \tau+b}{c \tau+d}\right)=f(\tau)+\frac{\pi \mathrm{i} c z^{2}}{c \tau+d}+\log \theta(z, \tau)
$$

We substitute $z(c \tau+d)$ for $z$ to get

$$
\log \theta\left(z, \frac{a \tau+b}{c \tau+d}\right)=f(\tau)+\pi \mathrm{i} c z^{2}(c \tau+d)+\log \theta(z(c \tau+d), \tau)
$$

Differentiation and plugging in $z=\frac{k}{n}$ yields

$$
(c \tau+d)^{-1} s_{k}\left(\frac{a \tau+b}{c \tau+d}\right)=2 \pi \mathrm{i} c \frac{k}{n}+\left(\frac{\partial}{\partial z} \log \theta\right)\left(\frac{k}{n}(c \tau+d), \tau\right)
$$

We use the product expansion (4.1) and $\sin (\pi z)=\frac{\mathrm{e}^{\pi \mathrm{i} z}-\mathrm{e}^{-\pi \mathrm{i} z}}{2 i}=-\frac{1}{2 \mathrm{i}} \mathrm{e}^{-\pi \mathrm{i} z}(1-$ $\left.\mathrm{e}^{2 \pi \mathrm{i} z}\right)$ to get

$$
\left(\frac{\partial}{\partial z} \log \theta\right)(z, \tau)=2 \pi \mathrm{i}\left(-\frac{1}{2}-\sum_{l=0}^{\infty} \frac{\mathrm{e}^{2 \pi \mathrm{i}(l \tau+z)}}{1-\mathrm{e}^{2 \pi \mathrm{i}(l \tau+z)}}+\sum_{l=1}^{\infty} \frac{\mathrm{e}^{2 \pi \mathrm{i}(l \tau-z)}}{1-\mathrm{e}^{2 \pi \mathrm{i}(l \tau-z)}}\right)
$$

Therefore,

$$
(c \tau+d)^{-1} s_{k}\left(\frac{a \tau+b}{c \tau+d}\right)=2 \pi \mathrm{i}\left(\frac{k c}{n}-\frac{1}{2}-\sum_{l=0}^{\infty} \frac{q^{l+\frac{k c}{n}} \zeta_{n}^{k d}}{1-q^{l+\frac{k c}{n}} \zeta_{n}^{k d}}+\sum_{l=1}^{\infty} \frac{q^{l-\frac{k c}{n}} \zeta_{n}^{-k d}}{1-q^{l-\frac{k c}{n}} \zeta_{n}^{-k d}}\right)
$$

where $\zeta_{n}=\mathrm{e}^{2 \pi \mathrm{i} / n}$ and $q^{\alpha}=\mathrm{e}^{2 \pi \mathrm{i} \alpha \tau}$. We observe that

$$
\lim _{\tau \rightarrow \mathrm{i} \infty} \frac{q^{l \pm \frac{k c}{n}} \zeta_{n}^{ \pm k d}}{1-q^{l \pm \frac{k c}{n}} \zeta_{n}^{ \pm k d}}= \begin{cases}0, & l \pm \frac{k c}{n}>0 \\ \frac{\zeta_{n}^{ \pm k d}}{1-\zeta_{n}^{ \pm k d}}, & l \pm \frac{k c}{n}=0 \\ -1, & l \pm \frac{k c}{n}<0\end{cases}
$$

which implies the claim.

## 5. ReAlization OF $\mathcal{T}_{n}$ IN TERMS OF MODULAR FORMS.

We will now use the results of Section 4 to compute the realizations explicitly in terms of modular forms on $X_{1}(n)$.

We can view the elliptic curve $E$ as $\mathbb{C} /(\mathbb{Z}+\mathbb{Z} \tau)$, with the torsion point $t=\frac{1}{n}$. The homogeneous coordinates of the images of the points $z=\frac{i}{n}$ for $i=0, \ldots, n-1$ under the standard embedding are given by the $n \times 3$ matrix

$$
\left(\begin{array}{ccc}
0 & 1 & 0 \\
\mathcal{P}\left(\frac{1}{n}\right) & \mathcal{P}^{\prime}\left(\frac{1}{n}\right) & 1 \\
\mathcal{P}\left(\frac{2}{n}\right) & \mathcal{P}^{\prime}\left(\frac{2}{n}\right) & 1 \\
\mathcal{P}\left(\frac{3}{n}\right) & \mathcal{P}^{\prime}\left(\frac{3}{n}\right) & 1 \\
\cdots & \cdots & \cdots \\
\mathcal{P}\left(\frac{k}{n}\right) & \mathcal{P}^{\prime}\left(\frac{k}{n}\right) & 1 \\
\cdots & \cdots & \cdots
\end{array}\right)
$$

This matrix is then reduced to the standard form by right multiplication by $\mathrm{GL}(3, \mathbb{C})$ and scaling of the rows

$$
\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 1 & 1 \\
\cdots & \cdots & \cdots \\
1 & a_{k} & b_{k} \\
\ldots & \cdots & \cdots
\end{array}\right)
$$

with the exception of the $(n-2)$-nd row where the point lies on the first coordinate line and thus the first coordinate can not be made 1 .

Remark 5.1. The $(n-2)$-nd row of (5.2) that corresponds to the point $\frac{n-3}{n}$ is $(0,1,1)$, because it lies on the intersection of the first coordinate line with the line on which the second and third coordinates are equal.

Proposition 5.2. There holds

$$
b_{k}=\frac{s_{k+3}-s_{k-2}-s_{3}-s_{2}}{s_{6}-s_{3}-s_{2}-s_{1}}
$$

for $k \neq 1,2,(n-3) \bmod n$.

Before the proof of Proposition 5.2, let us note the following

Remark 5.3. Recall from Corollary 4.0 that the modular form $s_{6}-s_{3}-s_{2}-s_{1}$ is nonvanishing on $X_{1}(n)^{\circ}$.

Remark 5.4. Note that Proposition 5 . 2 implies $b_{n-4}=1$.

Proof. Observe that ratios of minors which have each index appearing equally many times in the numerator and the denominator, stay invariant under the reduction from (5.1) to (5.2). Therefore,

$$
\frac{\operatorname{det}_{01 k} \operatorname{det}_{123}}{\operatorname{det}_{12 k} \operatorname{det}_{013}}
$$

must be the same for (5.1) and (5.2). Here it is convenient to index rows of the matrix starting from 0 . The value of this ratio in (5.2) is $b_{k}$, so we get a formula for it. Specifically we get $b_{k}=F\left(\frac{k}{n}\right)$ where

$$
F(z)=\frac{\operatorname{det}_{014} \operatorname{det}_{123}}{\operatorname{det}_{124} \operatorname{det}_{013}}
$$

of the matrix

$$
\left(\begin{array}{ccc}
0 & 1 & 0 \\
\mathcal{P}\left(\frac{1}{n}\right) & \mathcal{P}^{\prime}\left(\frac{1}{n}\right) & 1 \\
\mathcal{P}\left(\frac{2}{n}\right) & \mathcal{P}^{\prime}\left(\frac{2}{n}\right) & 1 \\
\mathcal{P}\left(\frac{3}{n}\right) & \mathcal{P}^{\prime}\left(\frac{3}{n}\right) & 1 \\
\mathcal{P}(z) & \mathcal{P}^{\prime}(z) & 1
\end{array}\right)
$$

We will now identify the elliptic function $F$ based on the following properties which determine it uniquely.

- $F(z)$ has simple poles at $z=\frac{2}{n}$ and $z=-\frac{3}{n}$. It has simple zeros at $z=0$ and $z=-\frac{1}{n}$.
- $F\left(\frac{3}{n}\right)=1$.

Indeed, $\operatorname{det}_{014}=\mathcal{P}(z)-\mathcal{P}\left(\frac{1}{n}\right)$ has simple zeros at $\frac{1}{n}$ and $-\frac{1}{n}$ and order two pole at $z=0$. Similarly $\operatorname{det}_{124}$ has simple zeros at $\frac{1}{n}, \frac{2}{n}$ and $-\frac{3}{n}$ and order three pole at $z=0$.

By the first property, we can write $F(z)$ up to constant as

$$
\frac{r_{1}(z)}{r_{-2}(z) r_{3}(z)}
$$

since it is an elliptic function with the same zeros and poles. By Proposition 4.4

$$
r_{-2}(z) r_{3}(z)=-r_{1}^{\prime}(z)+\left(-s_{2}+s_{3}\right) r_{1}(z)
$$

so

$$
F(z)=c \frac{1}{-\frac{r_{1}^{\prime}(z)}{r_{1}(z)}+\left(-s_{2}+s_{3}\right)}=\frac{1}{-\frac{\theta^{\prime}\left(z+\frac{1}{n}\right)}{\theta\left(z+\frac{1}{n}\right)}+\frac{\theta^{\prime}(z)}{\theta(z)}+\left(-s_{2}+s_{3}\right)}
$$

So we get

$$
F\left(\frac{k}{n}\right)=\frac{-c}{s_{k+1}-s_{k}+s_{2}-s_{3}}
$$

We then use the second property to conclude that

$$
b_{k}=\frac{s_{4}-2 s_{3}+s_{2}}{s_{k+1}-s_{k}+s_{2}-s_{3}}
$$

and the result follows from Corollary 4.7.

We will now find the values of $a_{k}$.

Proposition 5.5. There holds

$$
a_{k}=\frac{s_{k+3}-s_{k-1}-s_{3}-s_{1}}{s_{6}-s_{3}-s_{2}-s_{1}}
$$

for $k \neq 1,2,(n-3)$.

Proof. Let us use a similar approach to find it. We get $a_{k}=G\left(\frac{k}{n}\right)$ for

$$
G(z)=\frac{\operatorname{det}_{024} \operatorname{det}_{123}}{\operatorname{det}_{124} \operatorname{det}_{023}}
$$

for the matrix (5.3). Then $G\left(\frac{3}{n}\right)=1, G(z)$ has simple zeros at 0 and $-\frac{2}{n}$ and simple poles at $\frac{1}{n}$ and $-\frac{3}{n}$. We get

$G(z)=c \frac{r_{2}(z)}{r_{-1}(z) r_{3}(z)}=\frac{c}{-\frac{r_{2}^{\prime}(z)}{r_{2}(z)}+\left(-s_{1}+s_{3}\right)}=\frac{c}{-\frac{\theta^{\prime}\left(z+\frac{2}{n}\right)}{\theta\left(z+\frac{2}{n}\right)}+\frac{\theta^{\prime}(z)}{\theta(z)}+\left(-s_{1}+s_{3}\right)}$

and

$$
G\left(\frac{k}{n}\right)=\frac{-c}{s_{k+2}-s_{k}+s_{1}-s_{3}}
$$

which then leads to

$$
G\left(\frac{k}{n}\right)=\frac{s_{5}-2 s_{3}+s_{1}}{s_{k+2}-s_{k}+s_{1}-s_{3}}
$$

and we use Corollary 4.8.

Proposition 5.6. For $n \geq 10$ and any $i \neq 0 \bmod n$, the modular function

$$
\frac{s_{i}}{s_{6}-s_{3}-s_{2}-s_{1}}
$$

for $\Gamma_{1}(n)$ can be written as a constant linear combination of the $a_{k}$ and $b_{k}$, $k \in\{0, \ldots, n-1\}$.

Proof. In view of Propositions 5.2 and 5.5, we simply need to show that linear combinations of

$$
s_{k+3}-s_{k-2}-s_{3}-s_{2}, s_{k+3}-s_{k-1}-s_{3}-s_{1}
$$

for $k \neq 1,2,(n-3) \bmod n$ span the space of all $s_{i}$. Denote by $V$ the span of the above relations. Subtracting one from the other, we get

$$
s_{k-1}=s_{k-2}+\left(s_{2}-s_{1}\right) \bmod V
$$

for all $k \neq 1,2,(n-3) \bmod n$. This implies

$$
s_{k}=s_{1}+(k-1)\left(s_{2}-s_{1}\right) \bmod V
$$

for $k \in\{1,2, \ldots, n-5\}$.

Assume $n \geq 10$. We use (5.5) and (5.4) for $k=3$ to get

$$
s_{6}-s_{3}-s_{1}-s_{2}=(5-2)\left(s_{2}-s_{1}\right)-s_{1}-s_{2}=2 s_{2}-4 s_{1}=0 \bmod V
$$

We also use

$$
0=s_{5}+s_{n-5}=2 s_{1}+(n-2)\left(s_{2}-s_{1}\right)=(n-2) s_{2}-(n-4) s_{1} \bmod V
$$

The determinant $4(n-2)-2(n-4)=2 n$ is nonzero, which means that $s_{1}, s_{2}$ and hence all $s_{i}$ are in $V$.

Definition 5.7. Let $Y_{1}(n)$ be the open part of $X_{1}(n)$ on which the modular form

$$
s_{6}-s_{3}-s_{2}-s_{1}
$$

does not vanish. Then we define the morphism

$$
\tilde{\psi}_{n}: Y_{1}(n) \rightarrow M_{n \times 3}(\mathbb{C})
$$

by sending $\tau$ to the $n \times 3$ matrix (with rows counted from 0 )

$$
\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 1 & 1 \\
\cdots & \cdots & \cdots \\
1 & \frac{s_{k+3}-s_{k-1}-s_{3}-s_{1}}{s_{6}-s_{3}-s_{2}-s_{1}} & \frac{s_{k+3}-s_{k-2}-s_{3}-s_{2}}{s_{6}-s_{3}-s_{2}-s_{1}} \\
\ldots & \ldots & \ldots
\end{array}\right)
$$

and $k=n-3$ row is given by $(0,1,1)$.

Proposition 5.8. For $n \geq 10$, the map $\tilde{\psi}_{n}$ is a closed embedding of $Y_{1}(n)$ into $M_{n \times 3}(\mathbb{C})$.

Proof. This follows from Proposition 5.6 and the statement that any modular form for $\Gamma_{1}(n)$ of weight at least three can be written as a polynomial in $s_{k}$.

We are now ready to state and prove our main theorem.

Theorem 5.9. For $n \geq 10$, the realization space $\mathcal{R}\left(\mathcal{T}_{n}\right)$ is scheme-theoretically isomorphic to the open subset of $X_{1}(n)$ obtained by adding to $X_{1}(n)^{\circ}$ (the complement of the cusps) the $(\mathbb{Z} / n \mathbb{Z})^{*}$-orbit of the $\mathrm{i} \infty$ cusp.

Proof. In view of Propositions 5.2 and 5.5, the morphism $\tilde{\phi}_{n}$ extends the map $\phi_{n}: X_{1}(n)^{\circ} \rightarrow \mathcal{R}\left(\mathcal{T}_{n}\right)$ under the identification of the latter as a closed subset of the open subset of the matrices. In particular, for any cusp in $Y_{1}(n)$, the matrix (5.6) satisfies $\operatorname{det}_{i_{1}, i_{2}, i_{3}}=0$ for $i_{1}+i_{2}+i_{3}=0 \bmod n$.

We will now determine which of the cusps $\frac{a}{c}$ of $Y_{1}(n)$ map to $\mathcal{R}\left(\mathcal{T}_{n}\right)$, i.e. which cusps satisfy $\operatorname{det}_{i_{1}, i_{2}, i_{3}} \neq 0$ for $i_{1}+i_{2}+i_{3} \neq 0 \bmod n$.

Consider the cusps in the $(\mathbb{Z} / n \mathbb{Z})^{*}$-orbit of the $\mathrm{i} \infty$ cusp. In this case $c=0 \bmod n$ with $d$ coprime to $n$. Proposition 4.9 implies that the $k$-th row of the matrix (5.6) is, for $\alpha=\mathrm{e}^{2 \pi \mathrm{i} \frac{d}{n} \text {, }}$

$$
\begin{aligned}
& \left(1 \frac{\frac{\alpha^{k+3}+1}{\alpha^{k+3}-1}-\frac{\alpha^{k-1}+1}{\alpha^{k-1}-1}-\frac{\alpha^{3}+1}{\alpha^{3}-1}-\frac{\alpha+1}{\alpha-1}}{\frac{\alpha^{6}+1}{\alpha^{6}-1}-\frac{\alpha^{3}+1}{\alpha^{3}-1}-\frac{\alpha^{2}+1}{\alpha^{2}-1}-\frac{\alpha+1}{\alpha-1}}, \frac{\frac{\alpha^{k+3}+1}{\alpha^{k}-3-1}-\frac{\alpha^{k-2}+1}{\alpha^{k-2}-1}-\frac{\alpha^{3}+1}{\alpha^{3}-1}-\frac{\alpha^{2}+1}{\alpha^{2}-1}}{\frac{\alpha^{6}+1}{\alpha^{6}-1}-\frac{\alpha^{3}+1}{\alpha^{3}-1}-\frac{\alpha^{2}+1}{\alpha^{2}-1}-\frac{\alpha+1}{\alpha-1}}\right) \\
& =\left(1, \frac{\left(1-\alpha^{2}\right)\left(1+\alpha^{3}\right)\left(1-\alpha^{k}\right)\left(1-\alpha^{k+2}\right)}{\left(1-\alpha^{5}\right)\left(1-\alpha^{k-1}\right)\left(1-\alpha^{k+3}\right)}, \frac{\left(1-\alpha+\alpha^{2}\right)\left(1-\alpha^{k}\right)\left(1-\alpha^{k+1}\right)}{\left(1+\alpha^{2}\right)\left(1-\alpha^{k-2}\right)\left(1-\alpha^{k+3}\right)}\right)
\end{aligned}
$$

which is exactly the point in (3.2) for the appropriate choice of primitive $n$-th root of 1. It then follows from Proposition 3.5 that this is a configuration and that no other cusps map inside the configuration space. (The latter statement can be also seen directly from Proposition 4.9, we leave the details to the reader).

As a consequence, the realization space $\mathcal{R}\left(\mathcal{T}_{n}\right)$ does not contain the special points of (3.2) as isolated points, but rather as part of the smooth image of at open subset of $X_{1}(n)$. Then the scheme-theoretic equality follows from Proposition 3.6 .

## 6. Compactifications

In this section we discuss two natural compactifications of the configuration space $\mathcal{R}\left(\mathcal{T}_{n}\right)$ for $n \geq 10$.

First, observe that if we consider the $\mathcal{R}\left(\mathcal{T}_{n}\right)$ as a subset of $M_{n \times 3}(\mathbb{C})$, then the closure in the projective space $\mathbb{P}\left(M_{n \times 3}(\mathbb{C}) \oplus \mathbb{C}\right)$ is isomorphic to $X_{1}(n)$. Moreover, we have an embedding given precisely by the weight one forms $s_{k}(\tau)$. This was initially conjectured by X.R. based on numerical experiments for $10 \leq n \leq 42$, and which we can now confirm.

It is also interesting to study the compactification of $\mathcal{R}\left(\mathcal{T}_{n}\right)$ in the product of projective planes $\left(\mathbb{P}^{2}\right)^{n-4}$. Clearly, this means understanding the limits of (5.6) as $\tau$ approaches cusps in $X_{1}(n)$ that are not in the $(\mathbb{Z} / n \mathbb{Z})^{*}$ orbit of i $\infty$. Such limits exist and are unique by properness of $\mathbb{P}^{2}$. If $s_{6}-s_{3}-s_{2}-s_{1} \neq 0$, then we can get this relatively easily from Proposition 4.9, but if it is zero, then the calculations are more complicated. In any case, the resulting point configurations will satisfy vanishing of the determinants but not all of the non-vanishings.

We can state the condition of the cusp $\frac{a}{c}$ (with coprime $a$ and $c$ ) being in the orbit of i $\infty$ as $n / \operatorname{gcd}(c, n)=1$. As such, it is natural to next consider the case $n / \operatorname{gcd}(c, n)=2$, which means that $n=2 m, c=m \bmod n$ and $a$ is coprime to $c$. Then for even $k$ the value of $s_{k}$ at this cusp is

$$
(2 \pi \mathrm{i}) \frac{\zeta^{k d}+1}{2\left(\zeta^{k d}-1\right)}
$$

and for odd $k$ the value is 0 . Consequently, $s_{6}-s_{3}-s_{2}-s_{1}$ takes value

$$
(2 \pi \mathrm{i}) \frac{\zeta^{2 d}\left(1+\zeta^{2 d}\right)}{1-\zeta^{6 d}}
$$

For even and odd $k$, the $k$-th row of the matrix (5.6) is given by

$$
\left(1,0, \frac{\left(1-\zeta^{6 d}\right)\left(1-\zeta^{k d}\right)}{\zeta^{2 d}\left(1-\zeta^{4 d}\right)\left(1-\zeta^{(k-2) d}\right)}\right)
$$

and

$$
\left(1, \frac{\left(1-\zeta^{2 d}\right)\left(1-\zeta^{6 d}\right) \zeta^{(k-3) d}}{\left(1-\zeta^{(k-1) d}\right)\left(1-\zeta^{(k+3) d}\right)}, \frac{\left(1-\zeta^{6 d}\right)\left(1-\zeta^{(k+1) d}\right)}{\left(1-\zeta^{4 d}\right)\left(1-\zeta^{(k+3) d}\right)}\right)
$$

respectively. Note that the even $k$ points lie on the line $x_{2}=0$ and the odd $k$ points lie on the conic

$$
\begin{array}{r}
0=\left(x_{3}-x_{2}\right) x_{3} \zeta^{2 d}\left(1+\zeta^{2 d}\right)^{2}+x_{1}^{2}\left(1+\zeta^{2 d}+\zeta^{4 d}\right)^{2} \\
+x_{1} x_{2} \zeta^{2 d}\left(1+\zeta^{2 d}+\zeta^{4 d}\right)-x_{1} x_{3}\left(1+\zeta^{2 d}\right)^{2}\left(1+\zeta^{2 d}+\zeta^{2 d}\right)
\end{array}
$$

After a linear change of coordinates, this configuration of points in $\mathbb{C P}^{2}$ can be identified with the Böröczky example [10], which is important in real arrangements, see [15.

We will now consider the next case, that of $n / \operatorname{gcd}(c, n)=3$. In this case we have $n=3 m$ and $c$ can be either $m$ or $-m$ modulo $n$. Without loss of generality we may consider the case $c=m$. Then we have

$$
\lim _{\tau \rightarrow \mathrm{i} \infty}(c \tau+d)^{-1} s_{k}\left(\frac{a \tau+b}{c \tau+d}\right)= \begin{cases}(2 \pi \mathrm{i}) \frac{\zeta^{k d}+1}{2\left(\zeta^{k d}-1\right)}, & k=0 \bmod 3 \\ (2 \pi \mathrm{i})\left(-\frac{1}{6}\right), & k=1 \bmod 3 \\ (2 \pi \mathrm{i})\left(\frac{1}{6}\right), & k=2 \bmod 3\end{cases}
$$

Consequently, the $k$-th line of the matrix (5.6) is given by

$$
\begin{gathered}
\left(1, \frac{\left(1+\zeta^{3 d}\right) \zeta^{k d}}{\left(1-\zeta^{(k+3) d}\right)}, \frac{\left(1+\zeta^{3 d}\right) \zeta^{k d}}{\left(1-\zeta^{(k+3) d}\right)}\right) \\
\left(1, \frac{\left(1+\zeta^{-3 d}\right)\left(1-\zeta^{(k+2) d}\right)}{1-\zeta^{(k-1) d}}, 1+\zeta^{3 d}\right) \\
\left(1,1+\zeta^{-3 d}, \frac{\left(1+\zeta^{-3 d}\right)\left(1-\zeta^{(k+1) d}\right)}{1-\zeta^{(k-2) d}}\right)
\end{gathered}
$$

for $k=0,1,2 \bmod 3$ respectively. After a linear change of variables, we can reduce it to

$$
\left\{\left(1: 0:-\zeta^{3 l}\right),\left(0:-\zeta^{3 l}: 1\right),\left(-\zeta^{3 l}: 1: 0\right)\right\}, 0 \leq l<m
$$

which is the Ceva example, (see e.g. [13), a prominent example for ball quotient surfaces, see e.g. [14.

The next case to consider is $n=4 m$ and $c=m \bmod n$. We have

$$
\begin{aligned}
& \lim _{\tau \rightarrow \mathrm{i} \infty}(c \tau+d)^{-1}\left(s_{6}(\tau)-s_{3}(\tau)-s_{2}(\tau)-s_{1}(\tau)\right) \\
& =2 \pi \mathrm{i}\left(\left(\frac{2}{4}-\frac{1}{2}\right)-\left(\frac{3}{4}-\frac{1}{2}\right)-\left(\frac{2}{4}-\frac{1}{2}\right)-\left(\frac{1}{4}-\frac{1}{2}\right)\right)=0
\end{aligned}
$$

so the previous approach does not work. However, we can use the formulas

$$
a_{k}=\frac{s_{5}-2 s_{3}+s_{1}}{s_{k+2}-s_{k}+s_{1}-s_{3}}, b_{k}=\frac{s_{4}-2 s_{3}+s_{2}}{s_{k+1}-s_{k}+s_{2}-s_{3}}
$$

from the proof of Propositions 5.2 and 5.5, at least for some values of $k$. The numerator of $a_{k}$ gives limit

$$
\begin{gathered}
\lim _{\tau \rightarrow \mathrm{i \infty}}(c \tau+d)^{-1}\left(s_{5}(\tau)-2 s_{3}(\tau)+s_{1}(\tau)\right) \\
=2 \pi \mathrm{i}\left(\left(\frac{1}{4}-\frac{1}{2}\right)-2\left(\frac{3}{4}-\frac{1}{2}\right)+\left(\frac{1}{4}-\frac{1}{2}\right)\right)=-2 \pi \mathrm{i}
\end{gathered}
$$

The numerator of $b_{k}$ gives the limit $\frac{2 \pi \mathrm{i}}{\zeta^{4 d}-1}$, so both are nonzero. For $k=$ $0 \bmod 4$ and $k=3 \bmod 4$ we get $\left(1, a_{k}, b_{k}\right)$ equal $\left(1,1-\zeta^{-k d}, \frac{1-\zeta^{-k d}}{1-\zeta^{4 d}}\right)$ and $\left(1,1, \frac{1-\zeta^{(k+1) d}}{1-\zeta^{4 d}}\right)$ respectively. For $k=2 \bmod 4$ the denominator of $a_{k}$ equals $\frac{2 \pi \mathrm{i}}{\zeta^{(k+2) d}-1}$, and the denominator of $b_{k}$ tends to 0 , so the corresponding limit in $\mathbb{P}^{2}$ is $(0,0,1)$ for all $k=2 \bmod 4$. This approach does not work well for the remaining $k=1 \bmod 4$, because in this case both denominators of $a_{k}$ and $b_{k}$ go to 0 , so we can only deduce that $p_{k}$ has zero first coordinate. However, we can still determine these points, since collinearity is preserved in the limit. Indeed, $p_{k}$ will lie on the line $\overline{p_{n-k} p_{0}}$. This gives

$$
p_{k}=\left(0: 1: \frac{1-\zeta^{(1-k) d}}{1-\zeta^{4 d}}\right)
$$

This is a copy of the Ceva arrangement for $3 m$ points and one additional point on the intersection of two lines of the Ceva arrangement, repeated $m$ times.

In the general case, it is relatively easy to see what happens when

$$
\lim _{\tau \rightarrow \mathrm{i} \infty}(c \tau+d)^{-1}\left(s_{6}(\tau)-s_{3}(\tau)-s_{2}(\tau)-s_{1}(\tau)\right) \neq 0
$$

In this case, the values of $a_{k}$ and $b_{k}$ will lie in a finite list, except for when $k \in\{-3,1,2\} \bmod n / \operatorname{gcd}(c, n)$. Thus we expect it to be again related to the Ceva arrangement. If the above limit is zero, one could use the method of Proposition 4.9 to study the asymptotic behavior of $s_{6}-s_{3}-s_{2}-s_{1}$ near the cusp, although it does not appear straightforward.

## REFERENCES

[1] Baaziz H., Equations for the modular curve $X_{1}(N)$ and models of elliptic curves with torsion points, Math. Comp. 79 (2010), no. 272, 2371-2386

[2] Borisov L., On Wronskians of weight one Eisenstein series, J. Number Theory 121 (2006), no. 1, 132-152

[3] Borisov L., Gunnells P.E., Toric modular forms and nonvanishing of L -functions, J. Reine Angew. Math. 539 (2001), 149-165

[4] Borisov L., Gunnells P.E., Toric varieties and modular forms, Invent. Math. 144 (2001), no. 2, 297-325

[5] Borisov L., Gunnells P.E. Popescu S., Elliptic functions and equations of modular curves. Math. Ann. 321 (2001), no. 3, 553-568

[6] Borisov L., Gunnells P.E., Toric modular forms of higher weight, J. Reine Angew. Math. 560 (2003), 43-64

[7] Bosma W., Cannon J., Playoust C., The Magma algebra system. I. The user language, J. Symbolic Comput. 24, 1997, 3-4, 235-265

[8] Chandrasekharan K., Elliptic functions. Grundlehren Math. Wiss., 281[Fundamental Principles of Mathematical Sciences] Springer-Verlag, Berlin, 1985.

[9] Conrad B., Arithmetic moduli of generalized elliptic curves, J. Inst. Math. Jussieu 6 (2007), no. 2, 209-278.

[10] Crowe, D.W., McKee, T.A.: Sylvester's problem on collinear points. Math. Mag. 41, 30-34 (1968)

[11] Corey D., Kühne L., Schröter B., Matroids in OSCAR, arXiv:2311.08792

[12] Deligne, P.; Rapoport, M. Les schémas de modules de courbes elliptiques. Modular functions of one variable II, pp. 143-316, Lecture Notes in Math., Vol. 349, Springer, Berlin-New York, 1973.

[13] Eterović S., Figueroa F., Urzúa G., On the geography of line arrangements, Adv. Geom. 22 (2022), no. 2, 269-276.

[14] Hirzebruch, F. Arrangements of lines and algebraic surfaces, Arithmetic and geometry, Vol. II, 113-140, Progr. Math., 36, Birkhäuser, Boston, Mass., 1983.

[15] Green B., Tao T., On Sets Defining Few Ordinary Lines, Discrete Comput Geom (2013) 50, 409-468

[16] Katz N., Mazur B., Arithmetic moduli of elliptic curves, Annals of Mathematics Studies, 108. Princeton University Press, Princeton, NJ, 1985. xiv +514

[17] Kühne L., Roulleau X., Regular polygons, line operators, and elliptic modular surfaces, arXiv:2312.03470

[18] Wolfram Research, Inc., Mathematica, https://www.wolfram.com/mathematica

[19] Roulleau X., On some operators acting on line arrangements and their dynamics, arXiv:2306.01053

[20] Roulleau X., On the dynamics of the line operator $\Lambda_{2,3}$ on some arrangements of six lines, European Journal of Mathematics (2023) 9:105

[21] Silverman J., The arithmetic of elliptic curves, GTM 106, Springer-Verlag, New York, 1992. xii +400 pp.

[22] Top J., Yui N., Explicit equations of some elliptic modular surfaces, Rocky Mountain J. Math.37(2007), no.2, 663-687.

[23] Voight J., Zureick-Brown D., The canonical ring of a stacky curve, Mem. Amer. Math. Soc. 277 (2022), no. 1362.

Lev Borisov, Rutgers University, 110 Frelinghuysen Rd, Piscataway, NJ 08854, USA

borisov@math.rutgers.edu

Xavier Roulleau, Université d'Angers, CNRS, LAREMA, SFR MATHSTIC, F-49000 Angers, France

xavier.roulleau@univ-angers.fr

