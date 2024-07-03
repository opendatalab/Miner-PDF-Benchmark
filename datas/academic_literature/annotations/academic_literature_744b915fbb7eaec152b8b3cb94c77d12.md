# SELF-ADJOINT AND MARKOVIAN EXTENSIONS OF INFINITE QUANTUM GRAPHS 

ALEKSEY KOSTENKO, DELIO MUGNOLO, AND NOEMA NICOLUSSI


#### Abstract

We investigate the relationship between one of the classical notions of boundaries for infinite graphs, graph ends, and self-adjoint extensions of the minimal Kirchhoff Laplacian on a metric graph. We introduce the notion of finite volume for ends of a metric graph and show that finite volume graph ends is the proper notion of a boundary for Markovian extensions of the Kirchhoff Laplacian. In contrast to manifolds and weighted graphs, this provides a transparent geometric characterization of the uniqueness of Markovian extensions, as well as of the self-adjointness of the Gaffney Laplacian - the underlying metric graph does not have finite volume ends. If however finitely many finite volume ends occur (as is the case of edge graphs of normal, locally finite tessellations or Cayley graphs of amenable finitely generated groups), we provide a complete description of Markovian extensions upon introducing a suitable notion of traces of functions and normal derivatives on the set of graph ends.


Contents

\author{

1. Introduction <br> Notation <br> 2. Quantum graphs <br> 2.1. Combinatorial and metric graphs <br> 2.2. Graph ends <br> 2.3. Kirchhoff Laplacian <br> 2.4. Deficiency indices <br> 3. Graph ends and $H^{1}(\mathcal{G})$ <br> 3.1. $\quad H^{1}(\mathcal{G})$ and boundary values <br> 3.2. Nontrivial and finite volume ends <br> 3.3. Description of $H_{0}^{1}(\mathcal{G})$ <br> 4. Deficiency indices <br> 4.1. Deficiency indices and graph ends <br> 4.2. Proof of Theorem 4.1 <br> 5. Properties of self-adjoint extensions <br> 6. Finite energy self-adjoint extensions <br> 6.1. Normal derivatives at graph ends <br> 6.2. Properties of the trace and normal derivatives <br> 6.3. Description of self-adjoint extensions <br> 7. Deficiency indices of antitrees <br> 7.1. Antitrees
}

2020 Mathematics Subject Classification. Primary 34B45 Secondary 47B25 81Q10

Key words and phrases. Quantum graph, graph end, self-adjoint extension, Markovian extension, harmonic function.

Research supported by the Austrian Science Fund (FWF) under Grants No. P 28807 (A.K. and N.N.) and W 1245 (N.N.), by the German Research Foundation (DFG) under Grant No. 397230547 (D.M.), and by the Slovenian Research Agency (ARRS) under Grant No. J1-1690 (A.K.). The authors would like to acknowledge that this article is based upon work from COST Action CA18232 MAT-DYN-NET, supported by COST (European Cooperation in Science and Technology). arXiv:1911.04735

J. London Math. Soc., to appear; doi: 10.1112/jlms. 12539

## 1. INTRODUCTION

This paper is concerned with developing extension theory for infinite quantum graphs. Quantum graphs are Schrödinger operators on metric graphs, that is combinatorial graphs where edges are considered as intervals with certain lengths. Motivated by a vast amount of applications in chemistry and physics, they have become a popular subject in the last decades (we refer to [8, 9, 26, 67, for an overview and further references). From the perspective of Dirichlet forms, quantum graphs play an important role as an intermediate setting between Laplacians on Riemannian manifolds and difference Laplacians on weighted graphs. On the one hand, being locally one-dimensional, quantum graphs allow to simplify considerations of complicated geometries. On the other hand, there is a close relationship between random walks on graphs and Brownian motion on metric graphs, however, in contrast to the discrete case, the corresponding quadratic form in the metric case is a strongly local Dirichlet form and in this situation more tools are available (see [7, 28, 58, 59] for various manifestations of this point of view). Let us also mention that metric graphs can be seen as non-Archimedian analogs of Riemann surfaces, which finds numerous applications in algebraic geometry (see [2, 5, 6, 70] for further references).

The most studied quantum graph operator is the Kirchhoff Laplacian, which provides the analog of the Laplace-Beltrami operator in the setting of metric graphs. Its spectral properties are crucial in connection with the heat equation and the Schrödinger equation and any further analysis usually relies on the self-adjointness of the Laplacian. Whereas on finite metric graphs the Kirchhoff Laplacian is always self-adjoint, the question is more subtle for graphs with infinitely many edges.

For instance, a uniform lower bound for the edge lengths guarantees self-adjointness (see [9, 67), but this commonly used condition is independent of the combinatorial graph structure and clearly excludes a number of interesting cases (the so-called fractal metric graphs). Moreover, most of the results on strongly local Dirichlet forms require completeness of a given metric space w.r.t. the "intrinsic" metric (cf., e.g., 74 ), which coincides with the natural path (geodesic) metric in the case of metric graphs. Geodesic completeness (w.r.t. the natural path metric) guarantees self-adjointness of the (minimal) Kirchhoff Laplacian, however, this result is far from being optimal (see [27, §4] and also Section [2.4 below). The search for self-adjointness criteria for infinite quantum graphs is an open and - in our opinion - rather difficult problem.

If the (minimal) Kirchhoff Laplacian is not self-adjoint, the natural next step is to ask for a description of its self-adjoint extensions, which corresponds to possible descriptions of the system in quantum mechanics or, if we speak about Markovian extensions, possible descriptions of Brownian motions. Naturally, this question is tightly related to finding appropriate boundary notions for infinite graphs. Our goal in this paper is to investigate the connection between extension theory and
one particular notion, namely graph ends, a concept which goes back to the work of Freudenthal [30] and Halin [38] and provides a rather refined way of compactifying graphs. However, the definition of graph ends is purely combinatorial and naturally must be modified to capture the additional metric structure of our setting. Based on the correspondence between graph ends and topological ends of metric graphs, we introduce the concept of ends of finite volume. First of all, it turns out that finite volume ends play a crucial role in describing the Sobolev spaces $H^{1}$ and $H_{0}^{1}$ on metric graphs. More specifically, we show that the presence of finite volume ends is the only reason for the strict inclusion $H_{0}^{1} \subsetneq H^{1}$ to hold. This in particular provides a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions of the minimal Kirchhoff Laplacian as well as the selfadjointness of the so-called Gaffney Laplacian (we are not aware of its analogs either in the manifold setting or in the context of weighted graph Laplacians, cf. [35, 37, 45, 52, 61, 62]). As yet another manifestation of the fact that finite volume graph ends represent the proper boundary for Markovian extensions of the Kirchhoff Laplacian, we provide a complete description of all finite energy extensions (i.e., self-adjoint extensions with domains contained in $H^{1}$, and all Markovian extensions clearly satisfy this condition), however, under the additional assumption that there are only finitely many finite volume ends. Let us stress that this class of graphs includes a wide range of interesting models (Cayley graphs of a large class of finitely generated groups, tessellating graphs, rooted antitrees etc. have exactly one end and in this case there are no finite volume ends exactly when the total volume of the corresponding metric graph is infinite). Moreover, we emphasize that in all those cases the dimension of the space of finite energy extensions is equal to the number of finite volume ends, however, for deficiency indices, i.e., the dimension of the space of self-adjoint extensions, this only gives a lower bound (for example, for Cayley graphs the dimension of the space of finite energy extensions is independent of the choice of a generating set, although deficiency indices do depend on this choice in a rather nontrivial way). On the other hand, it may happen that these dimensions coincide. The latter holds only if the maximal domain is contained in $H^{1}$, that is, if every self-adjoint extension is a finite energy extension. This is further equivalent to the validity of a certain non-trivial Sobolev-type inequality (see (1.1) below). The appearance of this condition demonstrates the mixed dimensional behavior of infinite metric graphs since the analogous estimate holds true in the one-dimensional situation, but usually fails in the PDE setting.

Let us now sketch the structure of the article and describe its content and our results in greater details.

In Section 2 we collect basic notions and facts about graphs and metric graphs (Section 2.1); graph ends (Section 2.2); the minimal and maximal Kirchhoff Laplacians (Section [2.3); deficiency indices and their connection with the spaces of $L^{2}$ harmonic and $\lambda$-harmonic functions (Section [2.4).

The core of the paper is Section 3 where we discuss the Sobolev spaces $H^{1}(\mathcal{G})$ and $H_{0}^{1}(\mathcal{G})$ and introduce the set of finite volume ends $\mathfrak{C}_{0}(\mathcal{G})$ (Definition (3.8). We show that $\mathfrak{C}_{0}(\mathcal{G})$ is the proper boundary for $H^{1}$ functions, which can also be seen as an ideal boundary by applying $C^{*}$-algebra techniques (see Remark 3.14). The central result of this section is Theorem [3.12 which shows that $H^{1}(\mathcal{G})=H_{0}^{1}(\mathcal{G})$ if and only if there are no finite volume ends. The latter also leads to a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions
of the Kirchhoff Laplacian (Corollary 5.5) as well as the self-adjointness of the Gaffney Laplacian $\mathbf{H}_{G}$ (see Remark 5.6(ii) for details and the definition of $\mathbf{H}_{G}$ ).

Section[4] contains further applications of the above considerations. Namely, Theorem 4.1 demonstrates that deficiency indices of the minimal Kirchhoff Laplacian can be estimated from below by the number of finite volume ends. This estimate is sharp (e.g., if there are infinitely many finite volume ends) and we also find necessary and sufficient conditions for the equality to hold. In particular, if there are only finitely many ends of finite volume, $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$, the latter is equivalent to the validity of the following Sobolev-type inequality (see Remark 4.2)

$$
\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})} \leq C\left(\|f\|_{L^{2}(\mathcal{G})}+\left\|f^{\prime \prime}\right\|_{L^{2}(\mathcal{G})}\right)
$$

for all $f$ in the maximal domain of the Kirchhoff Laplacian. Metric graphs are locally one-dimensional and the corresponding inequality is trivially satisfied in the onedimensional case, however, globally infinite metric graphs are more complex and hence (1.1) rather resembles the multi-dimensional setting of PDEs (in particular, (1.1) does not hold true if $\mathcal{G}$ has a non-free finite volume end, see Proposition 4.9).

In the next sections, we focus on a particular class of self-adjoint extensions whose domains are contained in $H^{1}$ (we call them finite energy extensions). These extensions have good properties and their importance stems from the fact that they contain the class of Markovian extensions (they also arise as self-adjoint restrictions of the Gaffney Laplacian). In Section 5 we show that (under some additional mild assumptions) their resolvents and heat semigroups are integral operators with continuous, bounded kernels and they belong to the trace class if $\mathcal{G}$ has finite total volume (Theorems 5.1 and 5.2).

In Section 6 we proceed further and show that finite volume ends is the proper boundary for this class of extensions. Namely, under the additional and rather restrictive assumption of finitely many ends with finite volume, in Sections 6.16.2. we introduce a suitable notion of a normal derivative at graph ends (as a by-product, this also gives an explicit description of the domain of the Neumann extension, see Corollary 6.7). Section 6.3 contains a complete description of finite energy extensions and also of Markovian extensions (Theorem 6.11). Let us stress that the case of infinitely many ends is incomparably more complicated and will be the subject of future work.

In general, the inequality in (1.1) is difficult to verify/contradict and even simple examples can exhibit rather complicated behavior (see Appendix B). The only reason for which (1.1) fails to hold is the presence of $L^{2}$ harmonic functions having infinite energy, that is, not belonging to $H^{1}$. Moreover, in order to compute deficiency indices of the Kirchhoff Laplacian one, roughly speaking, needs to find the dimension of the space of $L^{2}$ harmonic functions and description of self-adjoint extensions requires a thorough understanding of the behavior of $L^{2}$ harmonic functions at "infinity". Dictated by a distinguished role of harmonic functions in analysis, there is an enormous amount of literature dedicated to various classes of harmonic functions (positive, bounded etc.), which is further related to different notions of boundaries (metric completion, Poisson and Martin boundaries, Royden and Kuramochi boundaries etc.) and search for a suitable notion in this context (namely, $L^{2}$ harmonic functions) is a highly nontrivial problem, which seems not to be very well studied either in the context of incomplete manifolds (cf. [61, 62]) or in the case of weighted graphs (see [39, 45). We further illustrate this by considering the case of rooted antitrees, a special class of infinite graphs with a particularly high degree
of symmetry (see Section [7). Infinite rooted antitrees have exactly one graph end, which makes them a good toy model for our purposes. The above considerations show that the space of finite energy $L^{2}$ harmonic functions is nontrivial only if a given metric antitree has finite total volume and in this case the only such functions are constants. However, adjusting lengths in a suitable way for a concrete polynomially growing antitree (Figure 11) we can make the space of $L^{2}$ harmonic functions as large as we please (even infinite dimensional!).

Notation. $\mathbb{Z}, \mathbb{R}, \mathbb{C}$ have their usual meaning; $\mathbb{Z}_{\geq a}:=\mathbb{Z} \cap[a, \infty)$.

$z^{*}$ denotes the complex conjugate of $z \in \mathbb{C}$.

For a given set $S, \# S$ denotes its cardinality if $S$ is finite; otherwise we set $\# S=\infty$. If it is not explicitly stated otherwise, we shall denote by $\left(x_{n}\right)$ a sequence $\left(x_{n}\right)_{n=0}^{\infty}$. $C_{b}(X)$ is the space of bounded, continuous functions on a locally compact space $X$. $C_{0}(X)$ is the space of continuous functions vanishing at infinity.

For a finite or countable set $X, C(X)$ is the set of complex-valued functions on $X$. $\mathcal{G}_{d}=(\mathcal{V}, \mathcal{E})$ is a discrete graph (satisfying Hypothesis 2.1).

$\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$ is a metric graph (see p. 6).

$\varrho$ is the natural (geodesic) path metric on $\mathcal{G}$ (see p. 6).

$\varrho_{m}$ is the star metric on $\mathcal{V}$ corresponding to the star weight $m$ (see (2.13)).

$\Omega\left(\mathcal{G}_{d}\right)$ denotes the graph ends of $\mathcal{G}_{d}$ (see Definition 2.1).

$\mathfrak{C}(\mathcal{G})$ denotes the topological ends of a metric graph $\mathcal{G}$ (see Definition [2.2).

$\mathfrak{C}_{0}(\mathcal{G})$ stays for the finite volume topological ends of $\mathcal{G}$ (see Definition 3.8).

$\widehat{\mathcal{G}}$ is the end (Freudenthal) compactification of $\mathcal{G}$ (see p. 77).

$\mathbf{H}_{0}^{0}$ is the pre-minimal Kirchhoff Laplacian on $\mathcal{G}$ (see (2.9) ).

$\mathbf{H}_{0}$ is the minimal Kirchhoff Laplacian, the closure of $\mathbf{H}_{0}^{0}$ in $L^{2}(\mathcal{G})$ (see (2.9)).

$\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)$ are the deficiency indices of $\mathbf{H}_{0}$ (see (2.15) ).

$\mathbf{H}_{F}$ and $\mathbf{H}_{N}$ are the Friedrichs and Neumann extensions of $\mathbf{H}_{0}$ (see p. 12 and, respectively, p. [24).

$\mathbf{H}$ is the maximal Kirchhoff Laplacian on $\mathcal{G}$ (see (2.8)).

## 2. QUANTUM GRaphS

2.1. Combinatorial and metric graphs. In what follows, $\mathcal{G}_{d}=(\mathcal{V}, \mathcal{E})$ will be an unoriented graph with countably infinite sets of vertices $\mathcal{V}$ and edges $\mathcal{E}$. For two vertices $u, v \in \mathcal{V}$ we shall write $u \sim v$ if there is an edge $e_{u, v} \in \mathcal{E}$ connecting $u$ with $v$. For every $v \in \mathcal{V}$, we denote the set of edges incident to the vertex $v$ by $\mathcal{E}_{v}$ and

$$
\operatorname{deg}_{\mathcal{G}}(v):=\#\left\{e \mid e \in \mathcal{E}_{v}\right\}
$$

is called the degree (valency or combinatorial degree) of a vertex $v \in \mathcal{V}$. When there is no risk of confusion about which graph is involved, we shall simplify and write deg instead of $\operatorname{deg}_{\mathcal{G}}$. A path $\mathcal{P}$ of length $n \in \mathbb{Z}_{\geq 0} \cup\{\infty\}$ is a sequence of vertices $\left(v_{0}, v_{1}, \ldots, v_{n}\right)$ such that $v_{k-1} \sim v_{k}$ for all $k \in\{1, \ldots, n\}$.

The following assumption is imposed throughout the paper.

Hypothesis 2.1. $\mathcal{G}_{d}$ is infinite, locally finite $(\operatorname{deg}(v)<\infty$ for every $v \in \mathcal{V})$, connected (for any two vertices $u, v \in \mathcal{V}$ there is a path connecting $u$ and $v$ ), and simple (there are no loops or multiple edges).

Next, let us assign each edge $e \in \mathcal{E}$ a finite length $|e| \in(0, \infty)$. We can then naturally associate with $\left(\mathcal{G}_{d},|\cdot|\right)=(\mathcal{V}, \mathcal{E},|\cdot|)$ a metric space $\mathcal{G}$ : first, we identify
each edge $e \in \mathcal{E}$ with a copy of the interval $\mathcal{I}_{e}:=[0,|e|]$. The topological space $\mathcal{G}$ is then obtained by "gluing together" the ends of edges corresponding to the same vertex $v$ (in the sense of a topological quotient, see, e.g., [13, Chapter 3.2.2]). The topology on $\mathcal{G}$ is metrizable by the natural path metric $\varrho$ - the distance between two points $x, y \in \mathcal{G}$ is defined as the arc length of the "shortest path" connecting them (if $x$ or $y$ are not vertices, then we need to allow also paths which start or end in the middle of edges; the length of such paths is naturally defined by taking the corresponding portion of the interval). The metric space $\mathcal{G}$ arising from the above construction is called a metric graph (associated to $\left.\left(\mathcal{G}_{d},|\cdot|\right)=(\mathcal{V}, \mathcal{E},|\cdot|)\right)$.

Notice that, by definition, $(\mathcal{G}, \varrho)$ is a length space (see [13, Chapter 2.1] for definitions and further details). Moreover (see, e.g., 40, Chapter 1.1]), a metric graph $\mathcal{G}$ is a Hausdorff topological space with countable base and each $x \in \mathcal{G}$ has a neighborhood isometric to a star-shaped set $\mathcal{S}\left(\operatorname{deg}(x), r_{x}\right)$ of degree $\operatorname{deg}(x) \in \mathbb{Z}_{\geq 1}$,

$$
\mathcal{S}\left(\operatorname{deg}(x), r_{x}\right):=\left\{z=r \mathrm{e}^{2 \pi \mathrm{i} k / \operatorname{deg}(x)} \mid r \in\left[0, r_{x}\right), k=1, \ldots, \operatorname{deg}(x)\right\} \subset \mathbb{C}
$$

Notice that $\operatorname{deg}(x)$ in (2.2) coincides with the combinatorial degree if $x$ belongs to the vertex set, and $\operatorname{deg}(x)=2$ for every non-vertex point $x$ of $\mathcal{G}$.

Sometimes, we will consider $\mathcal{G}_{d}$ as a rooted graph with a fixed root $o \in \mathcal{V}$. In this case we denote by $S_{n}, n \in \mathbb{Z}_{>0}$ the $n$-th combinatorial sphere with respect to the order induced by $o$ (notice that $S_{0}=\{o\}$ ).

2.2. Graph ends. One possible definition of a boundary for an infinite graph is the notion of the so-called graph ends (see [30, 38] and [76, § 21]).

Definition 2.1. A sequence of distinct vertices $\left(v_{n}\right)_{n \in \mathbb{Z}_{\geq 0}}$ (resp., $\left.\left(v_{n}\right)_{n \in \mathbb{Z}}\right)$ such that $v_{n} \sim v_{n+1}$ for all $n \in \mathbb{Z}_{\geq 0}$ (resp., for all $n \in \mathbb{Z}$ ) is called a ray (resp., double ray). A subsequence of such a sequence is called a tail.

Two rays $\mathcal{R}_{1}, \mathcal{R}_{2}$ are called equivalent - and we write $\mathcal{R}_{1} \sim \mathcal{R}_{2}-$ if there is a third ray containing infinitely many vertices of both $\mathcal{R}_{1}$ and $\mathcal{R}_{2}$ An equivalence class of rays is called a graph end of $\mathcal{G}_{d}$ and the set of graph ends will be denoted by $\Omega\left(\mathcal{G}_{d}\right)$. Moreover, we will write $\mathcal{R} \in \omega$ whenever $\mathcal{R}$ is a ray belonging to the end $\omega \in \Omega\left(\mathcal{G}_{d}\right)$.

An important feature of graph ends is their relation to topological ends of a metric graph $\mathcal{G}$.

Definition 2.2. Consider sequences $\mathcal{U}=\left(U_{n}\right)_{n=0}^{\infty}$ of non-empty open connected subsets of $\mathcal{G}$ with compact boundaries and such that $U_{n+1} \subseteq U_{n}$ for all $n \geq 0$ and $\bigcap_{n \geq 0} \overline{U_{n}}=\emptyset$. Two such sequences $\mathcal{U}$ and $\mathcal{U}^{\prime}$ are called equivalent if for all $n \geq 0$ there exist $j$ and $k$ such that $U_{n} \supseteq U_{j}^{\prime}$ and $U_{n}^{\prime} \supseteq U_{k}$. An equivalence class $\gamma$ of sequences is called a topological end of $\mathcal{G}$ and $\mathfrak{C}(\mathcal{G})$ denotes the set of topological ends of $\mathcal{G}$.

For locally finite graphs, there is a bijection between topological ends of a metric graph $\mathfrak{C}(\mathcal{G})$ and graph ends $\Omega\left(\mathcal{G}_{d}\right)$ of the underlying combinatorial graph $\mathcal{G}_{d}$ (see 76 , $\S 21],[23, ~ \S 8.6$ and also p.277-278]; for the case of graphs which are not locally finite see $[18,24])$.[^0]

Theorem 2.3. For every topological end $\gamma \in \mathfrak{C}(\mathcal{G})$ of a locally finite metric graph $\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$ there exists a unique graph end $\omega_{\gamma} \in \Omega\left(\mathcal{G}_{d}\right)$ such that for every sequence $\mathcal{U}$ representing $\gamma$, each $U_{n}$ contains a ray from $\omega_{\gamma}$. Moreover, the map $\gamma \mapsto \omega_{\gamma}$ is a bijection between $\mathfrak{C}(\mathcal{G})$ and $\Omega\left(\mathcal{G}_{d}\right)$.

Therefore, we may identify topological ends of a metric graph $\mathcal{G}$ and graph ends of the underlying graph $\mathcal{G}_{d}$. We will simply speak of the ends of $\mathcal{G}$. One obvious advantage of this identification is the fact that the definition of $\Omega\left(\mathcal{G}_{d}\right)$ is purely combinatorial and does not depend on edge lengths.

Definition 2.4. An end $\omega$ of a graph $\mathcal{G}_{d}$ is called free if there is a finite set $X$ of vertices which separates $\omega$ from all other ends of the graph (i.e. the rays of all ends $\omega^{\prime} \neq \omega$ end up in different connected components of $\mathcal{V} \backslash X$ than the rays of $\left.\omega\right)$.

Remark 2.5. Let us mention several examples.

(i) $\mathbb{Z}$ has two ends both of which are free.

(ii) $\mathbb{Z}^{N}$ has one end for all $N \geq 2$.

(iii) A $k$-regular tree, $k \geq 3$, has uncountably many ends, none of which is free.

(iv) If $\mathcal{G}_{d}$ is a Cayley graph of a finitely generated infinite group $\mathrm{G}$, then the number of ends of $\mathcal{G}_{d}$ is independent of the generating set and $\mathcal{G}_{d}$ has either one, two, or infinitely many ends. Moreover, $\mathcal{G}_{d}$ has exactly two ends only if $\mathrm{G}$ is virtually infinite cyclic (it has a finite normal subgroup $\mathrm{N}$ such that the quotient group $\mathrm{G} / \mathrm{N}$ is isomorphic either to $\mathbb{Z}$ or $\mathbb{Z}_{2} * \mathbb{Z}_{2}$ ). These results are due to Freudenthal 30 and Hopf 42 (see also 75]). The classification of finitely generated groups with infinitely many ends is due to Stallings [73]. Let us mention that if G has infinitely many ends, then the result of Stallings implies that it contains a non-Abelian free subgroup and hence is nonamenable. For further details we refer to, e.g., [32, Chapter 13].

(v) Let us also mention that by Halin's theorem [38] every locally finite graph $\mathcal{G}_{d}$ with infinitely many ends contains at least one end which is not free.

One of the main features of graph ends is that they provide a rather refined way of compactifying graphs (see [29] and [23, § 8.6], [76]). Namely, we introduce a topology on $\widehat{\mathcal{G}}:=\mathcal{G} \cup \mathfrak{C}(\mathcal{G})$ as follows. For an open subset $U \subseteq \mathcal{G}$, denote its extension $\widehat{U}$ to $\widehat{\mathcal{G}}$ by

$$
\widehat{U}:=U \cup\left\{\gamma \in \mathfrak{C}(\mathcal{G}) \mid \exists \mathcal{U}=\left(U_{n}\right) \in \gamma \text { such that } U_{0} \subset U\right\}
$$

Now we can introduce a neighborhood basis of $\gamma \in \mathfrak{C}(\mathcal{G})$ as follows

$$
\{\widehat{U} \mid U \subseteq \mathcal{G} \text { is open, } \gamma \in \widehat{U}\}
$$

This turns $\widehat{\mathcal{G}}$ into a compact topological space, called the end (or Freudenthal) compactification of $\mathcal{G}$.

Remark 2.6. Notice that an end $\gamma \in \mathfrak{C}(\mathcal{G})$ is free exactly when $\{\gamma\}$ is open as a subset of $\mathfrak{C}(\mathcal{G})$ (here $\mathfrak{C}(\mathcal{G})$ carries the induced topology from $\widehat{\mathcal{G}})$. This is further equivalent to the existence of a connected subgraph $\mathcal{G}^{\gamma}$ with compact boundary $\partial \mathcal{G}^{\gamma}$ such that $U_{n} \subseteq \mathcal{G}^{\gamma}$ eventually for any sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ and $U_{n}^{\prime} \cap \mathcal{G}^{\gamma}=\varnothing$ eventually for all sequences $\mathcal{U}^{\prime}=\left(U_{n}^{\prime}\right)$ representing an end $\gamma^{\prime} \neq \gamma$.[^1]

Let us mention that topological ends can be obtained in a constructive way by means of compact exhaustions. Namely, a sequence of connected subgraphs $\left(\mathcal{F}_{n}\right)$ of $\mathcal{G}$ such that each $\mathcal{F}_{n}$ has finitely many vertices and edges, $\mathcal{F}_{n} \subseteq \mathcal{F}_{n+1}$ for all $n \geq 0$ and $\bigcup_{n} \mathcal{F}_{n}=\mathcal{G}$ is called a compact exhaustion of $\mathcal{G}$. Clearly, each $\mathcal{F}_{n}$ may be identified with a compact subset of $\mathcal{G}$. Now iteratively construct a sequence $\left(U_{n}\right)$ by choosing in each step a non-compact, connected component $U_{n}$ of $\mathcal{G} \backslash \mathcal{F}_{n}$ satisfying $U_{n} \subseteq U_{n-1}$. It is easy to check that each such sequence $\left(U_{n}\right)$ defines a topological end $\gamma \in \mathfrak{C}(\mathcal{G})$ and in fact all ends $\gamma \in \mathfrak{C}(\mathcal{G})$ are obtained by this construction. Notice also that the open subsets $U_{n}$ of such representations $\gamma \sim\left(U_{n}\right)$ (actually, their topological closures, since we need to add endpoints of edges which also belong to $\mathcal{V}\left(\mathcal{F}_{n}\right)$ ) can again be identified with connected subgraphs $\mathcal{G}_{n}(\gamma):=\overline{U_{n}}$ and we will frequently use this fact.

Let us finish this section with a few more notations. Suppose $\mathcal{R}$ is a ray or a finite path without self-intersections in $\mathcal{G}_{d}$. We may identify $\mathcal{R}$ with a subgraph of $\mathcal{G}_{d}$ and hence with a subset of $\mathcal{G}$, i.e., we can consider it as the union of all edges of $\mathcal{R}$. The latter can further be identified with the interval $I_{\mathcal{R}}:=[0,|\mathcal{R}|)$ of length $|\mathcal{R}|$, where

$$
|\mathcal{R}|:=\sum_{e \in \mathcal{R}}|e|
$$

Also, we need to consider paths - and in particular rays - in $\mathcal{G}$ starting or ending at a non-vertex point. In particular, given a path $\left(v_{0}, v_{1}, \ldots, v_{N}\right)$ and a point $x$ in the interior of some edge $e$ attached to $v_{0}, e \neq e_{v_{0}, v_{1}}$, we add the interval $\left[x, v_{0}\right] \subseteq e$ to $\left(v_{0}, v_{1}, \ldots, v_{N}\right)$. For the resulting set, we shall write $\left(x, v_{0}, v_{1}, \ldots, v_{N}\right)$ and call it a non-vertex path; and likewise for rays. The set of all non-vertex rays will be denoted by $\mathfrak{R}(\mathcal{G})$.

2.3. Kirchhoff Laplacian. Let $\mathcal{G}$ be a metric graph satisfying Hypothesis 2.1 . Upon identifying every $e \in \mathcal{E}$ with a copy of the interval $\mathcal{I}_{e}=[0,|e|]$, we denote by

$$
L^{2}(e):=L^{2}\left(\mathcal{I}_{e} ; d x_{e}\right)
$$

the $L^{2}$-space for the (unweighted) Lebesgue measure $d x_{e}$ on $\mathcal{I}_{e}$ and introduce the Hilbert space $L^{2}(\mathcal{G})$ of functions $f: \mathcal{G} \rightarrow \mathbb{C}$ such that

$$
L^{2}(\mathcal{G}):=\bigoplus_{e \in \mathcal{E}} L^{2}(e)=\left\{f=\left\{f_{e}\right\}_{e \in \mathcal{E}} \mid f_{e} \in L^{2}(e), \sum_{e \in \mathcal{E}}\left\|f_{e}\right\|_{L^{2}(e)}^{2}<\infty\right\}
$$

The subspace of compactly supported $L^{2}(\mathcal{G})$ functions will be denoted by

$$
L_{c}^{2}(\mathcal{G}):=\left\{f \in L^{2}(\mathcal{G}) \mid f \neq 0 \text { only on finitely many edges } e \in \mathcal{E}\right\}
$$

For every $e \in \mathcal{E}$ consider the maximal operator $\mathrm{H}_{e, \max }$ acting on functions $f \in H^{2}(e)$ as a negative second derivative. Here and below $H^{s}(e)$ for $s \geq 0$ denotes the usual Sobolev space on $e$ (see, e.g., [12, Chapter 8]). In particular, $H^{0}(e)=L^{2}(e)$ and

$$
H^{1}(e)=\left\{f \in A C(e) \mid f^{\prime} \in L^{2}(e)\right\}, \quad H^{2}(e)=\left\{f \in H^{1}(e) \mid f^{\prime} \in H^{1}(e)\right\}
$$

This defines the maximal operator on $L^{2}(\mathcal{G})$ by

$$
\mathbf{H}_{\max }:=\bigoplus_{e \in \mathcal{E}} \mathrm{H}_{e, \max }, \quad \mathrm{H}_{e, \max }=-\frac{\mathrm{d}^{2}}{\mathrm{~d} x_{e}^{2}}, \quad \operatorname{dom}\left(\mathrm{H}_{e, \max }\right)=H^{2}(e)
$$

If $v$ is a vertex of the edge $e \in \mathcal{E}$, then for every $f \in H^{2}(e)$ the following quantities

$$
f_{e}(v):=\lim _{x_{e} \rightarrow v} f\left(x_{e}\right), \quad \quad f_{e}^{\prime}(v):=\lim _{x_{e} \rightarrow v} \frac{f\left(x_{e}\right)-f(v)}{\left|x_{e}-v\right|}
$$

are well defined. Considering $\mathcal{G}$ as the union of all edges glued together at certain endpoints, let us equip a metric graph with the Laplace operator. The Kirchhoff (also called standard or Kirchhoff-Neumann) boundary conditions at every vertex $v \in \mathcal{V}$ are then given by

$$
\left\{\begin{array}{l}
f \text { is continuous at } v \\
\sum_{e \in \mathcal{E}_{v}} f_{e}^{\prime}(v)=0
\end{array}\right.
$$

Imposing these boundary conditions on the maximal domain dom $\left(\mathbf{H}_{\max }\right)$ yields the maximal Kirchhoff Laplacian

$$
\begin{aligned}
\mathbf{H} & :=\mathbf{H}_{\max } \upharpoonright \operatorname{dom}(\mathbf{H}) \\
\operatorname{dom}(\mathbf{H}) & =\left\{f \in \operatorname{dom}\left(\mathbf{H}_{\max }\right) \mid f \text { satisfies (2.7) for any } v \in \mathcal{V}\right\}
\end{aligned}
$$

Restricting further to compactly supported functions we end up with the preminimal operator

$$
\begin{aligned}
\mathbf{H}_{0}^{0} & :=\mathbf{H}_{\max } \upharpoonright \operatorname{dom}\left(\mathbf{H}_{0}^{0}\right) \\
\operatorname{dom}\left(\mathbf{H}_{0}^{0}\right) & =\left\{f \in \operatorname{dom}\left(\mathbf{H}_{\max }\right) \cap L_{c}^{2}(\mathcal{G}) \mid f \text { satisfies (2.7) for any } v \in \mathcal{V}\right\}
\end{aligned}
$$

Integrating by parts one obtains

$$
\left\langle\mathbf{H}_{0}^{0} f, f\right\rangle_{L^{2}(\mathcal{G})}=\int_{\mathcal{G}}\left|f^{\prime}(x)\right|^{2} d x, \quad f \in \operatorname{dom}\left(\mathbf{H}_{0}^{0}\right)
$$

and hence $\mathbf{H}_{0}^{0}$ is a non-negative symmetric operator. We call its closure $\mathbf{H}_{0}:=\overline{\mathbf{H}_{0}^{0}}$ in $L^{2}(\mathcal{G})$ the minimal Kirchhoff Laplacian. The following result is well-known (see, e.g., [16, Lemma 3.9]).

Lemma 2.7. Let $\mathcal{G}$ be a metric graph. Then

$$
\mathbf{H}_{0}^{*}=\mathbf{H}
$$

2.4. Deficiency indices. In the following we are interested in the question whether $\mathbf{H}_{0}$ is self-adjoint, or equivalently whether the equality $\mathbf{H}_{0}=\mathbf{H}$ holds true. Let us recall one sufficient condition. Define the star weight $m(v)$ of a vertex $v \in \mathcal{V}$ by

$$
m(v):=\sum_{e \in \mathcal{E}_{v}}|e|=\operatorname{vol}\left(\mathcal{E}_{v}\right)
$$

and also introduce the star path metric on $\mathcal{V}$ by

$$
\varrho_{m}(u, v):=\inf _{\substack{\left.\mathcal{P}=\left(v_{0}, \ldots, v_{n}\right) \\ u=v_{0}, v=v_{n}\right)}} \sum_{v_{k} \in \mathcal{P}} m\left(v_{k}\right)
$$

Theorem 2.8 ([్a]). If $\left(\mathcal{V}, \varrho_{m}\right)$ is complete as a metric space, then $\mathbf{H}_{0}^{0}$ is essentially self-adjoint and $\overline{\mathbf{H}_{0}^{0}}=\mathbf{H}_{0}=\mathbf{H}$.

If a symmetric operator is not (essentially) self-adjoint, then the degree of its nonself-adjointness is determined by its deficiency indices. Recall that the deficiency subspace $\mathcal{N}_{z}\left(\mathbf{H}_{0}\right)$ of $\mathbf{H}_{0}$ is defined by

$$
\mathcal{N}_{z}\left(\mathbf{H}_{0}\right):=\operatorname{ker}\left(\mathbf{H}_{0}^{*}-z\right)=\operatorname{ker}(\mathbf{H}-z), \quad z \in \mathbb{C}
$$

The numbers

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right):=\operatorname{dim} \mathcal{N}_{ \pm \mathrm{i}}\left(\mathbf{H}_{0}\right)=\operatorname{dim} \operatorname{ker}(\mathbf{H} \mp \mathrm{i})
$$

are called the deficiency indices of $\mathbf{H}_{0}$. Notice that $\mathrm{n}_{+}\left(\mathbf{H}_{0}\right)=\mathrm{n}_{-}\left(\mathbf{H}_{0}\right)$ since $\mathbf{H}_{0}$ is non-negative. Moreover, $\mathbf{H}_{0}$ is self-adjoint exactly when $\mathrm{n}_{+}\left(\mathbf{H}_{0}\right)=\mathrm{n}_{-}\left(\mathbf{H}_{0}\right)=0$.

Lemma 2.9. If 0 is a point of regular type for $\mathbf{H}_{0}$, then

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\operatorname{dim} \operatorname{ker}(\mathbf{H})
$$

Proof. The claim immediately follows from [1, § 78] or [69, Prop. 3.3]. Indeed, the set of regular points of $\mathbf{H}_{0}$ is an open subset of $\mathbb{C}$. Moreover, by the KrasnoselskiiKrein theorem (see, e.g., [1 § 78] or [69, Prop. 2.4]), $\operatorname{dim} \mathcal{N}_{z}\left(\mathbf{H}_{0}\right)$ is constant on each connected component of the set of regular type points of $\mathbf{H}_{0}$. Since $\mathbf{H}_{0}$ is symmetric, each $z \in \mathbb{C} \backslash \mathbb{R}$ is a point of regular type for $\mathbf{H}_{0}$. Therefore, if 0 is a point of regular type for $\mathbf{H}_{0}$, we immediately get

$$
\operatorname{dim} \operatorname{ker}(\mathbf{H})=\operatorname{dim} \mathcal{N}_{0}\left(\mathbf{H}_{0}\right)=\mathrm{n}_{+}\left(\mathbf{H}_{0}\right)=\mathrm{n}_{-}\left(\mathbf{H}_{0}\right)
$$

Using the Rayleigh quotient, define

$$
\lambda_{0}(\mathcal{G}):=\inf _{\substack{f \in \operatorname{dom}\left(\mathbf{H}_{0}\right) \\\|f\|=1}}\left\langle\mathbf{H}_{0} f, f\right\rangle_{L^{2}(\mathcal{G})}=\inf _{\substack{f \in \operatorname{dom}\left(\mathbf{H}_{0}\right) \\\|f\|=1}} \int_{\mathcal{G}}\left|f^{\prime}\right|^{2} d x
$$

Noting that the operator $\mathbf{H}_{0}$ is non-negative, 0 is a point of regular type for $\mathbf{H}_{0}$ if $\lambda_{0}(\mathcal{G})>0$. Thus, we arrive at the following result.

Corollary 2.10. If $\lambda_{0}(\mathcal{G})>0$, then (2.16) holds true.

The positivity of $\lambda_{0}(\mathcal{G})$ is known in the following simple situation.

Corollary 2.11. If $\mathcal{G}$ has finite total volume,

$$
\operatorname{vol}(\mathcal{G}):=\sum_{e \in \mathcal{E}}|e|<\infty
$$

then $\mathbf{H}_{0}$ is not self-adjoint and (2.16) holds true.

Proof. Indeed, by the Cheeger-type estimate [55, Corollary 3.5(iv)], we have

$$
\lambda_{0}(\mathcal{G}) \geq \frac{1}{4 \operatorname{vol}(\mathcal{G})^{2}}>0
$$

and hence (2.16) holds true by Corollary [2.10. Moreover, $\mathbb{1}_{\mathcal{G}} \in \operatorname{ker}(\mathbf{H})$, where $\mathbb{1}_{\mathcal{G}}$ denotes the constant function on $\mathcal{G}$, and hence

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\operatorname{dim}(\operatorname{ker} \mathbf{H}) \geq 1
$$

It remains to notice that $\mathbf{H}_{0}$ is self-adjoint exactly when $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=0$.

Remark 2.12. By [55, Theorem 3.4], $\lambda_{0}(\mathcal{G})>0$ holds true if the isoperimetric constant $\alpha(\mathcal{G})$ of the metric graph $\mathcal{G}$ is positive. For antitrees, the isoperimetric constant is tightly related to the structure of its combinatorial spheres (see [56, Theorem 7.1]). If $\mathcal{G}_{d}$ is the edge graph of a tessellation of $\mathbb{R}^{2}$, then positivity of $\alpha(\mathcal{G})$ can be deduced from certain curvature-type quantities [65].

On the other hand, by [55, Corollary $4.5(\mathrm{i})], \lambda_{0}(\mathcal{G})>0$ holds true if the combinatorial isoperimetric constant of $\mathcal{G}_{d}$ is positive and $\ell^{*}(\mathcal{G}):=\sup _{e \in \mathcal{E}}|e|<\infty$. For[^2]example, this holds true if $\mathcal{G}_{d}$ is an infinite tree without leaves [55, Lemma 8.1] or if $\mathcal{G}_{d}$ is a Cayley graph of a non-amenable finitely generated group [55, Lemma 8.12(i)].

Finally, let us remark that $\operatorname{ker}(\mathbf{H})=\mathbb{H}(\mathcal{G}) \cap L^{2}(\mathcal{G})$, where $\mathbb{H}(\mathcal{G})$ denotes the space of harmonic functions on $\mathcal{G}$, that is, the set of all "edgewise" affine functions satisfying Kirchhoff conditions (2.7) at each vertex $v \in \mathcal{V}$. Notice that every function $f \in \mathbb{H}(\mathcal{G})$ is uniquely determined by its vertex values $\mathbf{f}:=\left.f\right|_{\mathcal{V}}=(f(v))_{v \in \mathcal{V}}$. Recall also the following result (see, e.g., [55], eq. (2.32)]).

Lemma 2.13. Let $\mathcal{G}$ be a metric graph satisfying the assumptions in Hypothesis [2.1. If $f \in \mathbb{H}(\mathcal{G})$, then $f \in L^{2}(\mathcal{G})$ if and only if $\mathbf{f} \in \ell^{2}(\mathcal{V} ; m)$, that is,

$$
\sum_{v \in \mathcal{V}}|f(v)|^{2} m(v)<\infty
$$

Remark 2.14. The above considerations indicate that in order to understand the deficiency indices of the Kirchhoff Laplacian one needs to find the dimension of the space of $L^{2}$ harmonic (or, more carefully, $\lambda$-harmonic) functions. Moreover, in order to describe self-adjoint extensions one has to understand the behavior of $L^{2}$ harmonic functions at "infinity", that is, near a "boundary" of a given metric graph. However, graphs admit a lot of different notions of boundary (ends, Poisson and Martin boundaries, Royden and Kuramochi boundary etc.) and search for a suitable notion in this context (namely, $L^{2}$ harmonic functions) is a highly nontrivial problem, which seems to be not very well studied neither in the context of incomplete manifolds nor in the case of weighted graphs.

Let us also mention that recently there has been a tremendous amount of work devoted to the study of harmonic functions and self-adjoint extensions of Laplacians on weighted graph (we only refer to a brief selection of articles [19, 35, 39, 43, 44, $45,46,51)$.

## 3. Graph ends and $H^{1}(\mathcal{G})$

This section deals with the Sobolev space $H^{1}$ on metric graphs. Its importance stems, in particular, from the fact that it serves as a form domain for a large class of self-adjoint extensions of $\mathbf{H}_{0}$.

3.1. $H^{1}(\mathcal{G})$ and boundary values. First recall that

$$
H^{1}(\mathcal{G})=\left\{f \in L^{2}(\mathcal{G}) \cap C(\mathcal{G}) \mid f_{e} \in H^{1}(e) \text { for all } e \in \mathcal{E},\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2}<\infty\right\}
$$

where $C(\mathcal{G})$ is the space of continuous complex-valued functions on $\mathcal{G}$ and

$$
\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2}:=\sum_{e \in \mathcal{E}}\left\|f_{e}^{\prime}\right\|_{L^{2}(e)}^{2}
$$

Notice that $\left(H^{1}(\mathcal{G}),\|\cdot\|_{H^{1}}\right)$ is a Hilbert space when equipped with the standard norm

$$
\|f\|_{H^{1}(\mathcal{G})}^{2}:=\|f\|_{L^{2}(\mathcal{G})}^{2}+\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2}=\sum_{e \in \mathcal{E}}\left\|f_{e}\right\|_{H^{1}(e)}^{2}, \quad f \in H^{1}(\mathcal{G})
$$

Moreover, $\operatorname{dom}\left(\mathbf{H}_{0}^{0}\right) \subset H^{1}(\mathcal{G})$ and we define $H_{0}^{1}(\mathcal{G})$ as the closure of $\operatorname{dom}\left(\mathbf{H}_{0}^{0}\right)$ with respect to $\|\cdot\|_{H^{1}(\mathcal{G})}$.

Remark 3.1. If $\mathbf{H}_{0}^{0}$ is essentially self-adjoint, then $H^{1}(\mathcal{G})=H_{0}^{1}(\mathcal{G})$. However, the converse is not true in general. In fact this equality is tightly connected to the uniqueness of Markovian extensions of $\mathbf{H}_{0}$ and, as we shall see, it is possible to characterize it in terms of topological ends of $\mathcal{G}$ (see Corollary 5.5 below).

Notice also that $H_{0}^{1}(\mathcal{G})$ is the form domain of the Friedrichs extension $\mathbf{H}_{F}$ of $\mathbf{H}_{0}^{0}$ and $\lambda_{0}(\mathcal{G})$ defined by (2.17) is the bottom of the spectrum of $\mathbf{H}_{F}$.

By definition, $H^{1}(\mathcal{G})$ is densely and continuously embedded in $L^{2}(\mathcal{G})$.

Lemma 3.2. $H^{1}(\mathcal{G})$ is continuously embedded in $C_{b}(\mathcal{G})=C(\mathcal{G}) \cap L^{\infty}(\mathcal{G})$ and

$$
\|f\|_{\infty}:=\sup _{x \in \mathcal{G}}|f(x)| \leq C_{\mathcal{G}}\|f\|_{H^{1}(\mathcal{G})}
$$

holds for all $f \in H^{1}(\mathcal{G})$ with $C_{\mathcal{G}}:=\sqrt{\operatorname{coth}\left(\frac{1}{2} \sup _{\mathcal{R}}|\mathcal{R}|\right)}$, where the supremum is taken over all non-vertex paths without self-intersections.

Proof. For every interval $\mathcal{I} \subseteq \mathbb{R}$ the embedding of $H^{1}(\mathcal{I})$ into $L^{\infty}(\mathcal{I})$ is bounded and

$$
\sup _{x \in \mathcal{I}}|f(x)| \leq C_{|\mathcal{I}|}\|f\|_{H^{1}(\mathcal{I})}
$$

holds for all $f \in H^{1}(\mathcal{I})$ with $C_{|\mathcal{I}|}=\sqrt{\operatorname{coth}(|\mathcal{I}|)}$ (see $[60]$ ). Notice that we may identify the restriction $\left.f\right|_{\mathcal{R}}$ of $f \in H^{1}(\mathcal{G})$ to a (non-vertex) path without selfintersections $\mathcal{R}$ with a function on $\mathcal{I}_{\mathcal{R}}=[0,|\mathcal{R}|)$. It is easy to check that upon this identification $\left.f\right|_{\mathcal{R}} \in H^{1}\left(\mathcal{I}_{\mathcal{R}}\right)$ and $\left(\left.f\right|_{\mathcal{R}}\right)^{\prime}=\left.f^{\prime}\right|_{\mathcal{R}}$.

Suppose now that $\mathcal{R}$ is a fixed non-vertex path without self-intersections in $\mathcal{G}$. Then for every $x \in \mathcal{G}$, connecting $x$ and $\mathcal{R}$ by some finite non-vertex path $\mathcal{R}_{0}$, we see that there exists a non-vertex path without self-intersections $\mathcal{R}_{x}$ such that $x \in \mathcal{R}_{x}$ and $\left|\mathcal{R}_{x}\right| \geq|\mathcal{R}| / 2$ (if $x$ lies on $\mathcal{R}$ already, then the connecting argument is superfluous and we can simply take a portion of $\mathcal{R}$ ). Applying (3.3) to $\mathcal{R}_{x}$, we easily deduce the estimate (3.2).

Remark 3.3. The diameter of $\mathcal{G}$ (as a metric space $(\mathcal{G}, \varrho)$ ) is defined by

$$
\operatorname{diam}(\mathcal{G}):=\sup _{x, y \in \mathcal{G}} \varrho(x, y)
$$

Therefore, $\operatorname{diam}(\mathcal{G}) \leq \sup _{\mathcal{R}}|\mathcal{R}|$ and hence $C_{\mathcal{G}} \leq \sqrt{\operatorname{coth}\left(\frac{1}{2} \operatorname{diam}(\mathcal{G})\right)}$.

The above considerations, in particular, imply the following crucial property of $H^{1}$-functions: if $\mathcal{R}=\left(v_{n}\right)$ is a ray, then

$$
f\left(\gamma_{\mathcal{R}}\right):=\lim _{n \rightarrow \infty} f\left(v_{n}\right)
$$

exists. Indeed, upon the identification of $\mathcal{R}$ with the interval $\mathcal{I}_{\mathcal{R}}=[0,|\mathcal{R}|)$, the latter is an immediate corollary of the description of a Sobolev space $H^{1}$ in one dimension - for a bounded interval this follows from [12], Theorem 8.2] and in the unbounded case see [12, Corollary 8.9]. Moreover, this limit only depends on the equivalence class of $\mathcal{R}$ (indeed, for any two equivalent rays $\mathcal{R}$ and $\mathcal{R}^{\prime}$ there exists a third ray $\mathcal{R}^{\prime \prime}$ containing infinitely many vertices of both $\mathcal{R}$ and $\mathcal{R}^{\prime}$, which immediately implies that $\left.f\left(\gamma_{\mathcal{R}}\right)=f\left(\gamma_{\mathcal{R}^{\prime \prime}}\right)=f\left(\gamma_{\mathcal{R}^{\prime}}\right)\right)$. This enables us to introduce the following notion.

Definition 3.4. For every $f \in H^{1}(\mathcal{G})$ and a (topological) end $\gamma \in \mathfrak{C}(\mathcal{G})$, we define

$$
f(\gamma):=f\left(\gamma_{\mathcal{R}}\right)
$$

where $\mathcal{R} \in \omega_{\gamma}$ is any ray belonging to the corresponding graph end $\omega_{\gamma}$ (see Theorem [2.3). Sometimes we shall also write $f\left(\omega_{\gamma}\right):=f(\gamma)$.

It turns out that (3.5) enables us to obtain an extension by continuity of every function $f \in H^{1}(\mathcal{G})$ to the end compactification $\widehat{\mathcal{G}}$ of $\mathcal{G}$ (see Section (2.2)).

Lemma 3.5. Let $\mathcal{G}$ be a metric graph and $\gamma \in \mathfrak{C}(\mathcal{G})$. If $f \in H^{1}(\mathcal{G})$, then

$$
\lim _{n \rightarrow \infty} \sup _{x \in U_{n}}|f(x)-f(\gamma)|=0
$$

for every sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$.

Proof. Let $\gamma \in \mathfrak{C}(\mathcal{G})$ and let $\mathcal{U}=\left(U_{n}\right)$ be a sequence representing $\gamma$. Let also

$$
\mathfrak{R}_{n}(\gamma):=\left\{\mathcal{R} \in \mathfrak{R}(\mathcal{G}) \mid \mathcal{R} \subseteq U_{n}\right\}
$$

be the set of all non-vertex rays contained in $U_{n}, n \geq 0$.

We proceed by case distinction. First, assume that for $n$ sufficiently large, all rays in $\mathfrak{R}_{n}(\gamma)$ have length at most one. If $x \in U_{n}$, then there exists a (non-vertex) ray $\mathcal{R}_{x} \in \mathfrak{R}_{n}(\gamma)$ such that $\mathcal{R}_{x}=\left(x, v_{0}, \ldots\right)$ and its tail $\mathcal{R}:=\left(v_{0}, v_{1}, \ldots\right)$ (see Definition 2.1) belong to $\omega_{\gamma}$.

By our assumption, $\left|\mathcal{R}_{x}\right| \leq 1$ and hence

$$
|f(\gamma)-f(x)|=\left|f\left(\gamma_{\mathcal{R}_{x}}\right)-f(x)\right|=\left|\int_{\mathcal{R}_{x}} f^{\prime}(y) d y\right| \leq\left\|f^{\prime}\right\|_{L^{2}\left(\mathcal{R}_{x}\right)} \leq\left\|f^{\prime}\right\|_{L^{2}\left(U_{n}\right)}
$$

Since $x \in U_{n}$ is arbitrary, this implies

$$
\sup _{x \in U_{n}}|f(\gamma)-f(x)| \leq\left\|f^{\prime}\right\|_{L^{2}\left(U_{n}\right)}
$$

Since $\mathcal{U}=\left(U_{n}\right)$ represents $\gamma, \bigcap_{n} \overline{U_{n}}=\varnothing$ and hence $\lim _{n \rightarrow \infty}\left\|f^{\prime}\right\|_{L^{2}\left(U_{n}\right)}=0$. This implies (3.6).

Assume now that for every $n \in \mathbb{Z}_{\geq 0}$ there is a ray $\mathcal{R} \in \mathfrak{R}_{n}(\gamma)$ with $|\mathcal{R}|>1$. Take $n \geq 0$ and choose an $x \in U_{n}$. We can find a finite (non-vertex) path without self-intersections $\mathcal{R}_{x} \subseteq U_{n}$ such that $x \in \mathcal{R}_{x}$ and $\left|\mathcal{R}_{x}\right|=1 / 2$ (take into account that $U_{n}$ contains at least one ray of length greater than 1$)$. Hence we get

$$
|f(x)| \leq \sup _{y \in \mathcal{R}_{x}}|f(y)| \leq C_{1 / 2}\|f\|_{H^{1}\left(\mathcal{R}_{x}\right)} \leq C_{1 / 2}\|f\|_{H^{1}\left(U_{n}\right)}
$$

where $C_{1 / 2}=\sqrt{\operatorname{coth}(1 / 2)}$ is the constant from (3.3). Since $x \in U_{n}$ is arbitrary,

$$
\sup _{x \in U_{n}}|f(x)| \leq C_{1 / 2}\|f\|_{H^{1}\left(U_{n}\right)}
$$

However, $\bigcap_{n} \overline{U_{n}}=\varnothing$ and hence $\sup _{x \in U_{n}}|f(x)|=o(1)$ as $n \rightarrow \infty$. It remains to notice that $f(\gamma)=0$. Indeed, by Theorem [2.3, for every $n \geq 0$ there is a ray $\widetilde{\mathcal{R}}_{n} \in \omega_{\gamma}$ such that $\widetilde{\mathcal{R}}_{n} \subseteq U_{n}$ and hence

$$
|f(\gamma)|=\left|f\left(\gamma_{\widetilde{\mathcal{R}}_{n}}\right)\right| \leq \sup _{x \in U_{n}}|f(x)|=o(1)
$$

as $n \rightarrow \infty$. This finishes the proof.

Taking into account the topology on $\widehat{\mathcal{G}}=\mathcal{G} \cup \mathfrak{C}(\mathcal{G})$, the next result is a direct consequence of Lemma 3.2 and Lemma 3.5 .

Proposition 3.6. Each $f \in H^{1}(\mathcal{G})$ has a unique continuous extension to the end compactification $\widehat{\mathcal{G}}$ of $\mathcal{G}$ and this extension is given by (3.5). Moreover,

$$
\|f\|_{\infty}=\sup _{x \in \widehat{\mathcal{G}}}|f(x)| \leq C_{\mathcal{G}}\|f\|_{H^{1}(\mathcal{G})}
$$

3.2. Nontrivial and finite volume ends. Observe that some ends lead to trivial boundary values for $H^{1}$ functions. For example, $f(\gamma)=0$ for all $f \in H^{1}(\mathcal{G})$ if $\omega_{\gamma} \in \Omega\left(\mathcal{G}_{d}\right)$ contains a ray $\mathcal{R}$ with infinite length $|\mathcal{R}|=\infty$. On the other hand, it might happen that all rays have finite length, however, $f(\gamma)=0$ for all $f \in H^{1}(\mathcal{G})$ (see, e.g., the second step in the proof of Lemma 3.5).

Definition 3.7. A topological end $\gamma \in \mathfrak{C}(\mathcal{G})$ is called nontrivial if $f(\gamma) \neq 0$ for some $f \in H^{1}(\mathcal{G})$.

We also need the following notion.

Definition 3.8. A topological end $\gamma \in \mathfrak{C}(\mathcal{G})$ has finite volume (or, more precisely, finite volume neighborhood) if there is a sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that $\operatorname{vol}\left(U_{n}\right)<\infty$ for some $n$. Otherwise $\gamma$ has infinite volume. The set of all finite volume ends is denoted by $\mathfrak{C}_{0}(\mathcal{G})$. Here and below, $\operatorname{vol}(A)$ is the Lebesgue measure of a measurable set $A \subseteq \mathcal{G}$.

Remark 3.9. If $\mathfrak{C}(\mathcal{G})$ contains only one end, then this end has finite volume exactly when $\operatorname{vol}(\mathcal{G})<\infty$. Analogously, if $\gamma \in \mathfrak{C}(\mathcal{G})$ is a free end, then there is a finite set of vertices $X$ separating $\omega_{\gamma}$ from all other ends and hence this end has finite volume exactly when the corresponding connected component $\mathcal{G}_{\gamma}$ has finite total volume.

If $\gamma$ is not free, then the situation is more complicated. For example, for a rooted tree $\mathcal{G}=\mathcal{T}_{o}$ the ends are in one-to-one correspondence with the rays from the root $o$ and hence one may possibly confuse the notion of a finite/infinite volume of an end with the finite/infinite length of the corresponding ray. More specifically, let $\gamma$ be an end of $\mathcal{T}_{o}$ and let $\mathcal{R}_{\gamma}=\left(o, v_{1}, v_{2}, \ldots\right)$ be the corresponding ray. For each $n \geq 1$, let $\mathcal{T}_{n}$ be the subtree of $\mathcal{T}_{o}$ having its root at $v_{n}$ and containing all the "descendant" vertices of $v_{n}$. Then by definition $\gamma$ has finite volume (neighborhood) if and only if there is $n \geq 1$ such that the corresponding subtree $\mathcal{T}_{n}$ has finite total volume. In particular, this implies that $\mathcal{G}$ would have uncountably many finite volume ends in this case (here we assume for simplicity that all vertices are essential, that is, $\operatorname{deg}(v)>2$ for all $v \in \mathcal{V})$. In particular, $\left|\mathcal{R}_{\gamma}\right|<\infty$ is a necessary but not sufficient condition for $\gamma$ to have finite volume.

It turns out that nontrivial and finite volume ends are closely connected.

Theorem 3.10. Let $\mathcal{G}$ be a metric graph. Then $\gamma \in \mathfrak{C}(\mathcal{G})$ is nontrivial if and only if $\gamma$ has finite volume. Moreover, for any finite collection of distinct nontrivial ends $\left\{\gamma_{j}\right\}_{j=1}^{N}$ there exists $f \in H^{1}(\mathcal{G}) \cap \operatorname{dom}(\mathbf{H})$ such that $f\left(\gamma_{1}\right)=1$ and $f\left(\gamma_{2}\right)=\cdots=$ $f\left(\gamma_{N}\right)=0$.

Proof. It is not difficult to see that $f(\gamma)=0$ for all $f \in H^{1}(\mathcal{G})$ if $\gamma$ has infinite volume. Indeed, assuming that there is $f \in H^{1}(\mathcal{G})$ such that $f(\gamma) \neq 0$, Lemma 3.5 would imply that there exists $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that

$$
|f(x)| \geq|f(\gamma)| / 2>0
$$

for all $x \in U_{N}$ and some $N \in \mathbb{Z}_{\geq 0}$. However, since $\operatorname{vol}\left(U_{N}\right)=\infty$, we conclude that $f$ is not in $L^{2}(\mathcal{G})$ and this gives a contradiction.

Suppose now that $\gamma \in \mathfrak{C}(\mathcal{G})$ has finite volume. Take a sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ with $\operatorname{vol}\left(U_{0}\right)<\infty$. Pick a function $\phi \in H^{2}(0,1)$ such that $\phi(0)=\phi^{\prime}(0)=$ $\phi^{\prime}(1)=0$ and $\phi(1)=1$ and then define $f: \mathcal{G} \rightarrow \mathbb{C}$ by

$$
f\left(x_{e}\right)= \begin{cases}1, & x_{e} \in e \text { and both vertices of } e \text { are in } U_{0} \\ 0, & x_{e} \in e \text { and both vertices of } e \text { are not in } U_{0} \\ \phi\left(\frac{\left|x_{e}-u\right|}{|e|}\right), & x_{e} \in e=e_{u, v} \text { and } u \in \mathcal{V} \backslash U_{0}, v \in U_{0}\end{cases}
$$

Clearly, $f \in H^{2}(e)$ for every $e \in \mathcal{E}$. Moreover, it is straightforward to check that $f$ satisfies Kirchhoff conditions (2.7) at every $v \in \mathcal{V}$. By assumption, $\partial U_{0}$ is compact and hence it is contained in finitely many edges. Thus there are only finitely many edges $e \in \mathcal{E}$ such that one of its vertices belongs to $U_{0}$ and the other one does not belong to $U_{0}$. This implies that $f \in L^{2}(\mathcal{G})$ and, moreover, $f^{\prime} \not \equiv 0$ only on finitely many edges, which proves the inclusion $f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$. Taking into account that $f \equiv 1$ on $U_{n}$ for large enough $n$, we conclude that $f(\gamma)=1$ and hence $\gamma$ is nontrivial.

It remains to prove the second claim. Suppose that $\gamma_{1}, \ldots, \gamma_{N} \in \mathfrak{C}(\mathcal{G})$ are distinct nontrivial ends. Then we can find $\mathcal{U}^{j}=\left(U_{n}^{j}\right)$, sequences representing $\gamma_{j}$, $j \in\{1, \ldots, N\}$, such that $\operatorname{vol}\left(U_{0}^{1}\right)<\infty$ and $U_{0}^{1} \cap U_{0}^{j}=\emptyset$ for all $j=2, \ldots, N$ (see [29, Satz 3] or [24, Lemma 3.1]). Using the above procedure, we can construct a function $f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ such that $\operatorname{supp}(f) \subseteq U_{0}$ and $f(\gamma)=1$. The latter also implies that $f\left(\gamma_{2}\right)=\cdots=f\left(\gamma_{N}\right)=0$.

Remark 3.11. If $\operatorname{vol}(\mathcal{G})=\sum_{e \in \mathcal{E}}|e|<\infty$, then all ends have finite volume and the end compactification $\widehat{\mathcal{G}}$ of $\mathcal{G}$ coincides with several other spaces, among them the metric completion of $\mathcal{G}$ and the Royden compactification of a related discrete graph (see [35], Corollary 4.22] and also [34, p. 1526]). Notice that the natural path metric $\varrho$ can be extended to $\widehat{\mathcal{G}}=\mathcal{G} \cup \mathfrak{C}(\mathcal{G})$ (see [34]). That is, the distance $\varrho(x, \gamma)$ between a point $x \in \mathcal{G}$ and an end $\gamma \in \mathfrak{C}(\mathcal{G})$ is the infimum over all lengths of rays starting at $x$ and belonging to $\gamma$. Similarly, the distance $\varrho\left(\gamma, \gamma^{\prime}\right)$ between two ends is the infimum over the lengths of all double rays with one tail part in $\gamma$ and the other one in $\gamma^{\prime}$. Then $(\widehat{\mathcal{G}}, \varrho)$ is a metric completion of $\mathcal{G}$ and $\widehat{\mathcal{G}}$ is compact and homeomorphic to the end compactification of $\mathcal{G}$ (see 34] for further details).

The metric completion was considered in connection with quantum graphs in [16, 17; however, it can have a rather complicated structure if $\operatorname{vol}(\mathcal{G})=\infty$ and a further analysis usually requires additional assumptions. Moreover, there are clear indications that metric completion is not a good candidate for these purposes.

3.3. Description of $H_{0}^{1}(\mathcal{G})$. Recall that the space $H_{0}^{1}(\mathcal{G})$ is defined as the closure of $\operatorname{dom}\left(\mathbf{H}_{0}^{0}\right) \subset H^{1}(\mathcal{G})$ with respect to $\|\cdot\|_{H^{1}(\mathcal{G})}$. One can naturally conjecture that $H_{0}^{1}(\mathcal{G})$ consists of those $H^{1}$-functions which vanish on $\mathfrak{C}(\mathcal{G})$. In fact, the results of the previous two sections enable us to show that this is indeed the case.

Theorem 3.12. Let $\mathcal{G}$ be a metric graph and $\mathfrak{C}(\mathcal{G})$ be its ends. Then

$$
H_{0}^{1}(\mathcal{G})=\left\{f \in H^{1}(\mathcal{G}) \mid f(\gamma)=0 \text { for all } \gamma \in \mathfrak{C}(\mathcal{G})\right\}
$$

Proof. First of all, it immediately follows from Proposition 3.6 that $f \in H_{0}^{1}(\mathcal{G})$ vanishes at every end $\gamma \in \mathfrak{C}(\mathcal{G})$ (since this holds for each $f \in \operatorname{dom}\left(\mathbf{H}_{0}^{0}\right)$ ).

To prove the converse inclusion, we will follow the arguments of the proof of 35 , Theorem 4.14]. Namely, suppose that $f \in H^{1}(\mathcal{G})$ and $f(\gamma)=0$ for all $\gamma \in \mathfrak{C}(\mathcal{G})$.

Without loss of generality, we may assume that $f$ is real-valued and $f \geq 0$. To prove that $f \in H_{0}^{1}(\mathcal{G})$, it suffices to construct a sequence of compactly supported functions $f_{n} \in H^{1}(\mathcal{G})$ which converges to $f$ in $H^{1}(\mathcal{G})$. Define $\phi_{n}:[0, \infty) \rightarrow[0, \infty)$ by

$$
\phi_{n}(s):= \begin{cases}s-\frac{1}{n}, & \text { if } s \geq \frac{1}{n} \\ 0, & \text { if } s<\frac{1}{n}\end{cases}
$$

and then let $f_{n}: \mathcal{G} \rightarrow[0, \infty)$ be the composition $f_{n}:=\phi_{n} \circ f, n \geq 0$. Since $\phi_{n}(s) \leq s$ for all $s \geq 0$ and $\left|\phi_{n}(s)-\phi_{n}(t)\right| \leq|s-t|$ for all $s, t \geq 0,\left|f_{n}(x)\right| \leq|f(x)|$ and $\left|f_{n}^{\prime}(x)\right| \leq\left|f^{\prime}(x)\right|$ for almost every $x \in \mathcal{G}$. Hence $f_{n} \in H^{1}(\mathcal{G})$ and

$$
\left\|f_{n}\right\|_{H^{1}(\mathcal{G})} \leq\|f\|_{H^{1}(\mathcal{G})}
$$

for all $n$. Let us now show that $f_{n}$ has compact support. Indeed, assuming the converse, there exist infinitely many distinct edges $e_{k}$ in $\mathcal{E}$ such that $f_{n}$ is non-zero on each $e_{k}$. Taking into account (3.8), for each $k$ we can find a non-vertex point $x_{k}$ on $e_{k}$ such that $f_{n}\left(x_{k}\right)>\frac{1}{n}$. Since $\widehat{\mathcal{G}}$ is compact, the sequence $\left(x_{k}\right)$ has an accumulation point $x \in \widehat{\mathcal{G}}$. By construction each edge $e \in \mathcal{E}$ contains at most one of the $x_{k}$ 's. It follows that $x \notin \mathcal{G}$ and hence $x \in \widehat{\mathcal{G}}$ is an end. On the other hand, $f$ is continuous on $\widehat{\mathcal{G}}$ by Proposition 3.6 and thus $f(x) \geq \frac{1}{n}$, which contradicts our assumptions on $f$.

It remains to show that $f_{n}$ converges to $f$ in $H^{1}(\mathcal{G})$ as $n \rightarrow \infty$. Taking into account the above properties of $f_{n}$, we get

$$
\left\|f-f_{n}\right\|_{L^{2}}^{2}+\left\|f^{\prime}-f_{n}^{\prime}\right\|_{L^{2}}^{2} \leq 2\left(\|f\|_{L^{2}}^{2}+\left\|f_{n}\right\|_{L^{2}}^{2}+\left\|f^{\prime}\right\|_{L^{2}}^{2}+\left\|f_{n}^{\prime}\right\|_{L^{2}}^{2}\right) \leq 4\|f\|_{H^{1}}^{2}
$$

and hence by dominated convergence it is enough to show that $f_{n} \rightarrow f$ and $f_{n}^{\prime} \rightarrow f^{\prime}$ pointwise a.e. on $\mathcal{G}$. The first claim is clearly true since $\lim _{n \rightarrow \infty} \phi_{n}(s)=s$ for all $s \in[0, \infty)$. To prove the second claim, suppose that $f$ is differentiable at a nonvertex point $x \in \mathcal{G}$. If $f(x)>0$, then by continuity of $f$, there is a neighborhood $U$ of $x$ such that $f_{n}=f-\frac{1}{n}$ holds on $U$ for all sufficiently large $n>0$. Hence $f_{n}$ is differentiable at $x$ with $f_{n}^{\prime}(x)=f^{\prime}(x)$ for all large enough $n$. Finally, if $f(x)=0$, then for each $n$ there is a neighborhood $U_{n}$ of $x$ such that $f \leq \frac{1}{n}$ on $U_{n}$. Hence $f_{n} \equiv 0$ on $U_{n}$ and, in particular, $f_{n}$ is differentiable at $x$ with $f_{n}^{\prime}(x)=0$. However, since $f \geq 0$ on $\mathcal{G}$ and $f$ is differentiable at $x$, it follows that $f^{\prime}(x)=0$ as well. This finishes the proof.

Combining Theorem 3.12 with Theorem [3.10, we arrive at the following fact.

Corollary 3.13. The equality $H^{1}(\mathcal{G})=H_{0}^{1}(\mathcal{G})$ holds true if and only if all topological ends of $\mathcal{G}$ have infinite volume.

Remark 3.14. In the related setting of (weighted) discrete graphs, an important concept is the construction of boundaries by employing $C^{*}$-algebra techniques (this includes both Royden and Kuramochi boundaries, see [35, 48, 53, 64, 71 for further details and references). Finite volume graph ends can also be constructed by using this method. Indeed, $\mathcal{A}:=H^{1}(\mathcal{G}) \subset C_{b}(\mathcal{G})$ is a subalgebra by Lemma 3.2 and hence its $\|\cdot\|_{\infty}$-closure $\widetilde{\mathcal{A}}:=\overline{\mathcal{A}}^{\|\cdot\|_{\infty}}$ is isomorphic to $C_{0}(\widetilde{X})$, where $\widetilde{X}$ is the space of characters equipped with the weak*-topology with respect to $\widetilde{\mathcal{A}}$. In general, finding $\widetilde{X}$ for some concrete $C^{*}$-algebra is a rather complicated task. However, it turns out that in our situation $\widetilde{X}$ coincides with $\widetilde{\mathcal{G}}:=\mathcal{G} \cup \mathfrak{C}_{0}(\mathcal{G})$. Indeed, $\widetilde{\mathcal{G}}=\mathcal{G} \cup \mathfrak{C}_{0}(\mathcal{G})$
equipped with the induced topology of the end compactification $\widehat{\mathcal{G}}$ is a locally compact Hausdorff space. Proposition 3.6 together with Theorem 3.10 shows that each function $f \in H^{1}(\mathcal{G})$ has a unique continuous extension to $\widetilde{\mathcal{G}}$ and this extension belongs to $C_{0}(\widetilde{\mathcal{G}})$. Moreover, by Theorem $3.10, H^{1}(\mathcal{G})$ is point-separating and nowhere vanishing on $\widetilde{\mathcal{G}}$ and hence $\widetilde{\mathcal{A}}=C_{0}(\widetilde{\mathcal{G}})$ by the Stone-Weierstrass theorem. Thus the resulting boundary notion is precisely the space of finite volume graph ends.

Let us also mention that $\mathcal{G}$ is compact only if $\operatorname{vol}(\mathcal{G})<\infty$ and in this case one can show that the Royden compactification of $\mathcal{G}$ as well as its Kuramochi compactification coincide with the end compactification $\widehat{\mathcal{G}}$ (see [35, [48, Theorem 7.11], [49, p.215] and also [41, p.2] for the discrete case).

## 4. DEFICIENCY INDICES

Intuitively, deficiency indices should be linked to boundary notions for underlying combinatorial graphs. However, spectral properties of the operator $\mathbf{H}_{0}$ also depend on the edge lengths and this suggests that it is difficult to expect a purely combinatorial formula for the deficiency indices $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)$ of $\mathbf{H}_{0}$. Recall that throughout the paper we always assume that $\mathcal{G}$ satisfies Hypothesis 2.1.

4.1. Deficiency indices and graph ends. The main result of this section provides criteria which allow to connect $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)$ with the number of graph ends.

Theorem 4.1. Let $\mathcal{G}$ be a metric graph and let $\mathbf{H}_{0}$ be the corresponding minimal Kirchhoff Laplacian. Then

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right) \geq \# \mathfrak{C}_{0}(\mathcal{G})
$$

Moreover, the equality

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\# \mathfrak{C}_{0}(\mathcal{G})
$$

holds true if and only if either $\# \mathfrak{C}_{0}(\mathcal{G})=\infty$ or $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$.

Remark 4.2. Since the map

$$
\begin{array}{rllc}
D: \quad H^{1}(\mathcal{G}) & \rightarrow & L^{2}(\mathcal{G}) \\
f & \mapsto & f^{\prime}
\end{array}
$$

is bounded, the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ holds true if and only if there is a positive constant $C>0$ such that

$$
\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2} \leq C\left(\|f\|_{L^{2}(\mathcal{G})}^{2}+\left\|f^{\prime \prime}\right\|_{L^{2}(\mathcal{G})}^{2}\right)
$$

holds for all $f \in \operatorname{dom}(\mathbf{H})$. It can be shown by examples that (4.3) may fail.

Before proving Theorem 4.1, let us first comment on some of its immediate consequences.

Corollary 4.3. If $\mathcal{G}$ is a metric graph with finite total volume $\operatorname{vol}(\mathcal{G})<\infty$, then

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right) \geq \# \Omega\left(\mathcal{G}_{d}\right)
$$

Moreover,

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\# \Omega\left(\mathcal{G}_{d}\right)
$$

if and only if either $\mathcal{G}$ contains a non-free end (and hence $\# \Omega\left(\mathcal{G}_{d}\right)=\infty$ in this case) or $\operatorname{ker}(\mathbf{H}) \subset H^{1}(\mathcal{G})$.

In fact, we only need to mention that by Halin's theorem [38] (see Remark[2.5(v)) and the finite total volume of $\mathcal{G}, \# \mathfrak{C}_{0}(\mathcal{G})=\infty$ only if $\mathcal{G}$ contains a non-free end.

Recall that for a finitely generated group G, the number of graph ends of a Cayley graph is independent of the generating set (see, e.g., [32]). Combining this fact with the above statement, we obtain the following result.

Corollary 4.4. Let $\mathcal{G}_{d}$ be a Cayley graph of a finitely generated group $\mathrm{G}$ with infinitely many ends If $\operatorname{vol}(\mathcal{G})<\infty$, then $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\infty$.

4.2. Proof of Theorem 4.1, The proof of Theorem4.1 is based on the following observation. Let $\mathbf{H}_{F}$ be the Friedrichs extension of $\mathbf{H}_{0}$. Then dom $(\mathbf{H})$ admits the following decomposition

$$
\operatorname{dom}(\mathbf{H})=\operatorname{dom}\left(\mathbf{H}_{F}\right) \dot{+} \operatorname{ker}(\mathbf{H}-z)=\operatorname{dom}\left(\mathbf{H}_{F}\right) \dot{+} \mathcal{N}_{z}\left(\mathbf{H}_{0}\right)
$$

for every $z$ in the resolvent set $\rho\left(\mathbf{H}_{F}\right)$ of $\mathbf{H}_{F}$ (see, e.g., [69, Proposition 14.11]). In particular, (4.6) holds for all $z \in\left(-\infty, \lambda_{0}(\mathcal{G})\right)$, where $\lambda_{0}(\mathcal{G}) \geq 0$ is defined by (2.17). Moreover, $\operatorname{dom}\left(\mathbf{H}_{F}\right) \subset H_{0}^{1}(\mathcal{G})$ and hence the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ depends only on the inclusion $\operatorname{ker}(\mathbf{H}-z) \subset H^{1}(\mathcal{G})$ for some (and hence for all) $z \in \rho\left(\mathbf{H}_{F}\right)$. Let us stress that $\mathcal{N}_{0}\left(\mathbf{H}_{0}\right)=\operatorname{ker}(\mathbf{H})=\mathbb{H}(\mathcal{G}) \cap L^{2}(\mathcal{G})$ and hence in the case $\lambda_{0}(\mathcal{G})>0$, one is interested in whether all $L^{2}$ harmonic functions belong to $H^{1}(\mathcal{G})$ or not, which is known to depend on the geometry of the underlying metric graph.

We also need the fact that functions in $\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ with $\lambda \in(-\infty, 0)$ can be considered as subharmonic functions and hence they should satisfy a maximum principle.

Lemma 4.5. Suppose $\mathcal{G}$ is a metric graph and let $\lambda \in(-\infty, 0)$.

(i) If $f \in \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)=\operatorname{ker}(\mathbf{H}-\lambda)$ is real-valued and $f\left(x_{0}\right)>0$ for some $x_{0} \in \mathcal{G}$, then

$$
\sup _{x \in \mathcal{G}} f(x)=\sup _{v \in \mathcal{V}} f(v)
$$

(ii) If additionally $f \in H^{1}(\mathcal{G})$, then

$$
\sup _{x \in \mathcal{G}} f(x)=\sup _{\gamma \in \mathfrak{C}(\mathcal{G})} f(\gamma)
$$

(iii) If (not necessarily real-valued) $f \in \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right) \cap H^{1}(\mathcal{G})$ satisfies

$$
f(\gamma)=0
$$

for all $\gamma \in \mathfrak{C}(\mathcal{G})$, then $f \equiv 0$.

Proof. (i) Let $f \in \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ be real-valued. If $x \in \mathcal{G}$ is such that $f(x)>0$ and $e \in \mathcal{E}$ is an edge with $x \in e$, then upon identifying $e$ with the interval $\mathcal{I}_{e}=[0,|e|]$ and taking into account that $-f^{\prime \prime}=\lambda f$ on $e$, we get

$$
f(y)=f(x) \cosh (\sqrt{-\lambda}(y-x))+\frac{f^{\prime}(x)}{\sqrt{-\lambda}} \sinh (\sqrt{-\lambda}(y-x))
$$

for all $y \in e$. If $f^{\prime}(x) \geq 0$, then obviously $f\left(e_{i}\right) \geq f(x)$, where $e_{i}$ is the vertex of $e$ identified with the right endpoint of $\mathcal{I}_{e}$. Similarly, $f\left(e_{o}\right) \geq f(x)$ for the other vertex $e_{o}$ of $e$ if $f^{\prime}(x)<0$. Hence $f$ attains its maximum on $e$ at the vertices of $e$, which clearly implies (4.7).[^3](ii) Now let $v \in \mathcal{V}$ be a vertex with $f(v)>0$. By (2.7), there is an edge $e \in \mathcal{E}_{v}$ such that $f_{e}^{\prime}(v) \geq 0$. If $u \in \mathcal{V}$ is the other vertex of $e$, then by (4.10) we get

$$
f(u)=f(v) \cosh (\sqrt{-\lambda}|e|)+\frac{f_{e}^{\prime}(v)}{\sqrt{-\lambda}} \sinh (\sqrt{-\lambda}|e|)>f(v)
$$

Observe that $f_{e}^{\prime}(u)<0$. Hence, setting $v_{0}=v$ and $v_{1}=u$ and using induction, we can construct a ray $\mathcal{R}=\left(v_{n}\right)$ such that $f\left(v_{n+1}\right)>f\left(v_{n}\right)$ for all $n \geq 0$. Since $f \in H^{1}(\mathcal{G})$, we get

$$
0<f(v)<\lim _{n \rightarrow \infty} f\left(v_{n}\right)=f\left(\gamma_{\mathcal{R}}\right) \leq \sup _{\gamma \in \mathfrak{C}(\mathcal{G})} f(\gamma)
$$

which proves (4.8).

(iii) By considering $\pm f$ (and splitting into real and imaginary part, if necessary), (4.9) clearly follows from (4.8).

Remark 4.6. Notice that the arguments used in the proof of Lemma 4.5(ii) in fact show that functions in $\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ with $\lambda \in(-\infty, 0)$ admitting positive values on $\mathcal{G}$ cannot attain global maxima in $\mathcal{G}$, that is, if $f$ attains a positive value at some $x \in \mathcal{G}$, then for every compact subgraph $\widetilde{\mathcal{G}} \subset \mathcal{G}$ the following holds

$$
\sup _{x \in \mathcal{G}} f(x)=\sup _{x \in \mathcal{G} \backslash \widetilde{\mathcal{G}}} f(x)
$$

Clearly, analogous statements hold true for functions admitting negative values, however, then sup must be replaced with inf.

Lemma 4.7. Suppose $\mathcal{G}$ is a metric graph and let $\lambda \in(-\infty, 0)$. Then

$$
\operatorname{dim}\left(\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right) \cap H^{1}(\mathcal{G})\right)=\# \mathfrak{C}_{0}(\mathcal{G})
$$

Proof. Using (4.6) with $z=\lambda \in(-\infty, 0)$ and noting that $\operatorname{dom}\left(\mathbf{H}_{F}\right) \subset H_{0}^{1}(\mathcal{G})$, Theorem 3.10 and Theorem 3.12 imply that $\operatorname{dim}\left(\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right) \cap H^{1}(\mathcal{G})\right) \geq \# \mathfrak{C}_{0}(\mathcal{G})$. The converse inequality follows from Lemma 4.5 (iii), which shows that the mapping $f \mapsto(f(\gamma))_{\gamma \in \mathfrak{C}_{0}(\mathcal{G})}$ is injective on $\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right) \cap H^{1}(\mathcal{G})$.

After all these preparations, we are now in position to complete the proof of Theorem 4.1 .

Proof of Theorem 4.1. Observe that the inequality (4.1) immediately follows from (4.6) and 4.11) since $\mathrm{n}_{ \pm}(\mathbf{H})=\operatorname{dim}\left(\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)\right)$.

Clearly, the second claim is trivial if $\# \mathfrak{C}_{0}(\mathcal{G})=\infty$. Hence it remains to show that in the case $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$ equality (4.2) holds exactly when $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$. Applying (4.6) once again, the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ holds true exactly when $\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right) \subset H^{1}(\mathcal{G})$. Taking into account once again that $\mathrm{n}_{ \pm}(\mathbf{H})=\operatorname{dim} \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ and using (4.11), we arrive at the conclusion.

Remark 4.8. Let us mention that one can prove the second claim of Theorem 4.1 in a different way. Namely, if $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$, then it is possible to reduce the problem to the study of a finite volume graph with a single end.

Let us stress that in the proof of Theorem 4.1) the equivalence of equality (4.2) and the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ was proved in the case when all finite volume ends are free. The next result shows that the inclusion never holds if there is a finite volume end which is not free.

Proposition 4.9. Let $\mathcal{G}$ be a metric graph having a finite volume end which is not free. Then there exists a function $f \in \operatorname{dom}(\mathbf{H})$ which does not belong to $H^{1}(\mathcal{G})$.

Proof. First observe that we can restrict our considerations to the case of a metric graph $\mathcal{G}$ having finite total volume. Indeed, if $\gamma$ is a non-free finite volume end of $\mathcal{G}$, then there exists a sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that $\operatorname{vol}\left(U_{n}\right)<\infty$ for all $n$. By definition, each $U_{n}$ is open and has compact boundary. Choosing $\mathcal{G}_{0} \subset \mathcal{G}$ as the subgraph with vertex set $\mathcal{V}\left(\mathcal{G}_{0}\right)=\mathcal{V} \cap U_{0}$ and edge set $\mathcal{E}\left(\mathcal{G}_{0}\right)=\left\{e \in \mathcal{E} \mid e \subset U_{0}\right\}$, it is easy to see that $\mathcal{G}_{0}$ is a connected finite volume subgraph and $\gamma$ is a non-free end of $\mathcal{G}_{0}$ (see also the notion of graph representation of an end in Section 6.1). Moreover, by construction the set $\partial \mathcal{G}_{0}$ of boundary points (here, $\mathcal{G}_{0}$ is seen as a closed subset of $\mathcal{G}$ ) is finite.

Let $\widetilde{\mathcal{G}} \subset \mathcal{G}$ be a connected, compact subgraph and consider the finitely many connected components of $\mathcal{G} \backslash \widetilde{\mathcal{G}}$. Since $\mathcal{G}$ has infinitely many ends, there is a connected component $U$ which contains at least two distinct graph ends $\gamma, \gamma^{\prime} \in \mathfrak{C}(\mathcal{G})$. Following the proof of Theorem 3.10, we readily construct a real-valued function $f=f_{U} \in$ $\operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ with $f(\gamma)=0, f\left(\gamma^{\prime}\right)=1$ and $0 \leq f \leq 1$ on $\mathfrak{C}(\mathcal{G})$ (in fact, it suffices to choose the corresponding function $\phi$ with $0 \leq \phi \leq 1$ ). Taking into account Theorem 3.12 and decomposition (4.6), we can assume that $f$ belongs to $H^{1}(\mathcal{G}) \cap \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ for some (fixed) $\lambda \in(-\infty, 0)$. However, Lemma 4.5 (iii) implies that

$$
\|f\|_{\infty}=\sup _{x \in \mathcal{G}}|f(x)|=\sup _{x \in \mathcal{G}} f(x)=1
$$

On the other hand, there exist two rays $\mathcal{R}, \mathcal{R}^{\prime} \in \mathfrak{R}\left(\mathcal{G}_{d}\right)$ representing the ends $\gamma$ and, respectively, $\gamma^{\prime}$ such that both $\mathcal{R}, \mathcal{R}^{\prime}$ are contained in $U$ and have the same initial vertex $v_{0}$. This leads to another estimate

$$
\begin{aligned}
1 & =\left|f(\gamma)-f\left(\gamma^{\prime}\right)\right|=\left|f(\gamma)-f\left(v_{0}\right)+f\left(v_{0}\right)-f\left(\gamma^{\prime}\right)\right| \\
& =\left|\int_{\mathcal{R}} f^{\prime}(x) d x-\int_{\mathcal{R}^{\prime}} f^{\prime}(x) d x\right| \leq 2 \sqrt{\operatorname{vol}(U)}\left\|f^{\prime}\right\|_{L^{2}(U)} \leq 2 \sqrt{\operatorname{vol}(U)}\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}
\end{aligned}
$$

Assume now that (4.3) holds for all functions $g \in \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$. Then $\|\cdot\|_{\infty}$ and $\|\cdot\|_{H^{1}}$ are in fact equivalent norms on $\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$. Indeed, combining (4.3) and the finite volume property, we get

$$
\|g\|_{H^{1}}^{2} \leq C\left(\|g\|_{L^{2}}^{2}+\|\mathbf{H} g\|_{L^{2}}^{2}\right)=C\left(1+\lambda^{2}\right)\|g\|_{L^{2}}^{2} \leq C\left(1+\lambda^{2}\right) \operatorname{vol}(\mathcal{G})\|g\|_{\infty}^{2}
$$

for all $g \in \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$, whereas $\|g\|_{\infty} \leq C_{\mathcal{G}}\|g\|_{H^{1}}$ by Lemma 3.2 Choosing compact subgraphs $\widetilde{\mathcal{G}}_{\varepsilon}$ with $\operatorname{vol}\left(\mathcal{G} \backslash \widetilde{\mathcal{G}}_{\varepsilon}\right) \leq \varepsilon^{2}$ (which is possible since $\mathcal{G}$ has finite volume), we clearly get $\operatorname{vol}\left(U_{\varepsilon}\right) \leq \varepsilon^{2}$ and hence the above constructed function $f_{\varepsilon}:=f_{U_{\varepsilon}} \in$ $H^{1}(\mathcal{G}) \cap \mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ satisfies

$$
\left\|f_{\varepsilon}^{\prime}\right\|_{L^{2}(\mathcal{G})} \geq\left\|f_{\varepsilon}^{\prime}\right\|_{L^{2}\left(U_{\varepsilon}\right)} \geq \frac{1}{2 \sqrt{\operatorname{vol}\left(U_{\varepsilon}\right)}} \geq \frac{1}{2 \varepsilon}
$$

However, by construction, $\left\|f_{\varepsilon}\right\|_{\infty}=1$, which obviously contradicts to the equivalence of norms $\|\cdot\|_{\infty}$ and $\|\cdot\|_{H^{1}}$ on $\mathcal{N}_{\lambda}\left(\mathbf{H}_{0}\right)$ since $\varepsilon>0$ is arbitrary.

We conclude this section by mentioning some explicit examples.

Example 4.10 (Radially symmetric trees). Let $\mathcal{G}=\mathcal{T}$ be a radially symmetric (metric) tree: that is, a rooted tree $\mathcal{T}$ such that for each $n \geq 0$, all vertices in the combinatorial sphere $S_{n}$ have the same number of descendants $d_{n} \geq 2$ and all edges
between the combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length. It is wellknown that in this case $\mathbf{H}$ is self-adjoint if and only if $\operatorname{vol}(\mathcal{T})=\infty$ and deficiency indices are infinite, $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\infty$, otherwise (see, e.g., [15, 72]). Moreover, due to the symmetry assumptions, all graph ends are of finite volume simultaneously. Hence we arrive at the equality

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\# \mathfrak{C}_{0}(\mathcal{G})= \begin{cases}\infty, & \text { if } \operatorname{vol}(\mathcal{T})<\infty \\ 0, & \text { if } \operatorname{vol}(\mathcal{T})=\infty\end{cases}
$$

Moreover, by Theorem 4.1 and Proposition 4.9, the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ holds true if and only if $\operatorname{vol}(\mathcal{T})=\infty$.

Example 4.11 (Radially symmetric antitrees). Consider a metric antitree $\mathcal{G}=\mathcal{A}$ (see Section 7.1 for definitions) and additionally suppose that $\mathcal{A}$ is radially symmetric, that is, for each $n \geq 0$, all edges between the combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length. Combining [56. Theorem 4.1] (see also Corollary 7.3 below) with the fact that antitrees have exactly one graph end, $\# \mathbb{C}(\mathcal{A})=1$, we conclude that

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\# \mathfrak{C}_{0}(\mathcal{G})= \begin{cases}1, & \text { if } \operatorname{vol}(\mathcal{A})<\infty \\ 0, & \text { if } \operatorname{vol}(\mathcal{A})=\infty\end{cases}
$$

In particular, $\mathbf{H}$ is self-adjoint if and only if $\operatorname{vol}(\mathcal{A})=\infty$. Moreover, the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ holds true for all radially symmetric antitrees by Theorem 4.1 ,

Remark 4.12. Both radially symmetric trees and antitrees are particular examples of the so-called family preserving metric graphs (see [11] and also [10]) . Employing the results from [11], it is in fact possible to extend the conclusions in Example 4.10 and Example 4.11 to this general setting. More precisely, for each family preserving metric graph $\mathcal{G}$ without horizontal edges, the Kirchhoff Laplacian $\mathbf{H}$ is self-adjoint if and only if $\operatorname{vol}(\mathcal{G})=\infty$ and moreover

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\# \mathfrak{C}_{0}(\mathcal{G})= \begin{cases}\# \mathfrak{C}(\mathcal{G}), & \text { if } \operatorname{vol}(\mathcal{G})<\infty \\ 0, & \text { if } \operatorname{vol}(\mathcal{G})=\infty\end{cases}
$$

If in addition $\mathcal{G}$ has finitely many ends, then the inclusion $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ holds true. On the other hand, if $\mathcal{G}$ has infinitely many ends, then $\operatorname{dom}(\mathbf{H}) \subset H^{1}(\mathcal{G})$ holds true if and only if $\operatorname{vol}(\mathcal{G})=\infty$. The last two statements are again immediate consequences of Theorem 4.1 and Proposition 4.9

In conclusion, let us also emphasize that the example of the rope ladder graph in Appendix Bshows that the assumption on horizontal edges cannot be omitted. More precisely, the rope ladder graph is a family preserving graph in the sense of [10] with exactly one graph end. However, it possesses infinitely many horizontal edges (i.e., edges connecting vertices in the same combinatorial sphere) and ExampleB.5shows that in general $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)>\# \mathfrak{C}_{0}(\mathcal{G})$, even if the edge lengths are chosen symmetrically to the root, $\left|e_{n}^{+}\right|=\left|e_{n}^{-}\right|$for all $n \in \mathbb{Z}_{\geq 0}$.

## 5. Properties of Self-AdJoint extensions

The Sobolev space $H^{1}(\mathcal{G})$ plays a distinctive role in the study of self-adjoint extensions of the minimal operator $\mathbf{H}_{0}$. A self-adjoint extension $\widetilde{\mathbf{H}}$ of $\mathbf{H}_{0}$ is called a finite energy extension if its domain is contained in $H^{1}(\mathcal{G})$, that is, every function $f \in \operatorname{dom}(\widetilde{\mathbf{H}})$ has finite energy, $\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}<\infty$. The main result of this section
already indicates that finite energy self-adjoint extensions of the minimal operator (notice that among those are the Friedrichs extension and, as we will see later in this section, all Markovian extensions) possess a number of important properties.

Theorem 5.1. Let $\widetilde{\mathbf{H}}$ be a self-adjoint lower semi-bounded extension of $\mathbf{H}_{0}$. Assume that $z$ belongs to its resolvent set $\rho(\widetilde{\mathbf{H}})$. Then the following assertions hold.

(i) If the form domain of $\widetilde{\mathbf{H}}$ is contained in $H^{1}(\mathcal{G})$, then the resolvent $\mathcal{R}(z, \widetilde{\mathbf{H}})$ of $\widetilde{\mathbf{H}}$ is an integral operator whose kernel $\mathcal{K}_{z}$ is both of class $L^{\infty}(\mathcal{G} \times \mathcal{G})$ and jointly Hölder continuous of exponent $\beta=1 / 2$.

(ii) If additionally $\mathcal{G}$ has finite total volume, then $\mathcal{R}(z, \widetilde{\mathbf{H}})$ is of trace class.

Proof. (i) Let $\widetilde{\mathbf{H}}$ be a self-adjoint lower semi-bounded extension of $\mathbf{H}_{0}, \widetilde{\mathbf{H}} \geq c$ for some $c \in \mathbb{R}$. Without loss of generality we may assume $c=0$. Then we can consider its positive semi-definite square root $\widetilde{\mathbf{H}}^{1 / 2}$, which is again self-adjoint and whose domain agrees with the form domain of $\widetilde{\mathbf{H}}$. Accordingly, for all $z \in \mathbb{C} \backslash[0, \infty)$ and $\lambda=\sqrt{z}$ we get

$$
\left(\widetilde{\mathbf{H}}^{1 / 2}-\lambda\right)\left(\widetilde{\mathbf{H}}^{1 / 2}+\lambda\right)=\widetilde{\mathbf{H}}-z
$$

and hence

$$
\mathcal{R}(z, \widetilde{\mathbf{H}})=\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) \mathcal{R}\left(-\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)
$$

If the form domain of $\widetilde{\mathbf{H}}$ is contained in $H^{1}(\mathcal{G})$, and hence by Lemma 3.2 in $C_{b}(\mathcal{G})$, then $\mathcal{R}\left( \pm \lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)$ maps $L^{2}(\mathcal{G})$ into $L^{\infty}(\mathcal{G})$, and hence by duality also maps $L^{1}(\mathcal{G})$ into $L^{2}(\mathcal{G})$. Thus (5.1) implies that $\mathcal{R}(z, \widetilde{\mathbf{H}})$ maps $L^{1}(\mathcal{G})$ into $L^{\infty}(\mathcal{G})$ and hence, by the Kantorovich-Vulikh theorem (see, e.g., 44, Theorem 1.3] or [63, Theorem 1.1]), $\mathcal{R}(z, \widetilde{\mathbf{H}})$ is an integral operator with the $L^{\infty}$-kernel $\mathcal{K}(z ; \cdot, \cdot)$.

In order to prove the assertion about joint Hölder continuity, we need to take a closer look at the kernel $\mathcal{K}$ by adapting the proof of [3, Prop. 2.1]: as noticed before, the resolvent $\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)$ is bounded from $L^{2}(\mathcal{G})$ to $L^{\infty}(\mathcal{G})$ by Lemma 3.2 for any $\lambda$ in the resolvent set of $\widetilde{\mathbf{H}}^{1 / 2}$. Applying the Kantorovich-Vulikh theorem (see, e.g., [4, page 113]) once again, we see that

$$
\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) u(x)=\int_{\mathcal{G}} u(y) \kappa(\lambda ; x, y) d y=\left\langle u, \kappa(\lambda ; x, \cdot)^{*}\right\rangle_{L^{2}(\mathcal{G})}
$$

for all $x \in \mathcal{G}$ and some $\kappa(\lambda ; x, \cdot) \in L^{2}(\mathcal{G})$ such that $\sup _{x \in \mathcal{G}}\|\kappa(\lambda ; x, \cdot)\|_{L^{2}(\mathcal{G})}<\infty$. Moreover, observe that there exists $C=C(\lambda)>0$ such that

$$
\left\|\kappa(\lambda ; x, \cdot)-\kappa\left(\lambda ; x^{\prime}, \cdot\right)\right\|_{L^{2}(\mathcal{G})} \leq C \sqrt{\varrho\left(x, x^{\prime}\right)}
$$

for all $x, x^{\prime} \in \mathcal{G}$, where $\varrho\left(x, x^{\prime}\right)$ denotes the distance in the natural path metric on $\mathcal{G}$. Indeed, for any function $u \in L^{2}(\mathcal{G})$,

$$
\begin{aligned}
\left|\int_{\mathcal{G}} u(y)\left(\kappa(\lambda ; x, y)-\kappa\left(\lambda ; x^{\prime}, y\right)\right) d y\right| & =\left|\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) u(x)-\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) u\left(x^{\prime}\right)\right| \\
& \leq \sqrt{\varrho\left(x, x^{\prime}\right)}\left\|\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) u\right\|_{H^{1}} \\
& \leq C \sqrt{\varrho\left(x, x^{\prime}\right)}\|u\|_{L^{2}},
\end{aligned}
$$

where we have used the Cauchy-Schwarz inequality and the fact that the resolvent $\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)$ is a bounded operator from $L^{2}$ to the domain of $\widetilde{\mathbf{H}}^{1 / 2}$ equipped with the
graph norm, and (5.2) immediately follows. Now, taking into account the equalities (5.1) and $\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)^{*}=\mathcal{R}\left(\lambda^{*}, \widetilde{\mathbf{H}}^{1 / 2}\right)$, we conclude that

$$
\begin{aligned}
\mathcal{R}(z, \widetilde{\mathbf{H}}) u(x) & =\mathcal{R}\left(\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)\left(\mathcal{R}\left(-\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) u\right)(x) \\
& =\left\langle\mathcal{R}\left(-\lambda, \widetilde{\mathbf{H}}^{1 / 2}\right) u, \kappa(\lambda ; x, \cdot)^{*}\right\rangle_{L^{2}(\mathcal{G})} \\
& =\left\langle u, \mathcal{R}\left(-\lambda^{*}, \widetilde{\mathbf{H}}^{1 / 2}\right) \kappa(\lambda ; x, \cdot)^{*}\right\rangle_{L^{2}(\mathcal{G})} \\
& =\int_{\mathcal{G}} u(y) \int_{\mathcal{G}} \kappa(\lambda ; x, s) \kappa\left(-\lambda^{*} ; y, s\right)^{*} d s d y \\
& =: \int_{\mathcal{G}} u(y) \mathcal{K}(z ; x, y) d y
\end{aligned}
$$

for all $u \in L^{2}(\mathcal{G})$. It remains to prove that the mapping

$$
\mathcal{K}: \mathcal{G} \times \mathcal{G} \ni(x, y) \mapsto \int_{\mathcal{G}} \kappa(\lambda ; x, s) \kappa\left(-\lambda^{*} ; y, s\right)^{*} d s \in \mathbb{C}
$$

is jointly Hölder continuous. However, recalling that $\sup _{x \in \mathcal{G}}\|\kappa(\lambda, x ; \cdot)\|_{L^{2}(\mathcal{G})}<\infty$, this immediately follows from (5.2), since

$$
\begin{aligned}
\left|\mathcal{K}(x, y)-\mathcal{K}\left(x^{\prime}, y^{\prime}\right)\right| \leq & \left\|\kappa(\lambda ; x, \cdot)\left(\kappa\left(-\lambda^{*} ; y, \cdot\right)^{*}-\kappa\left(-\lambda^{*} ; y^{\prime}, \cdot\right)^{*}\right)\right\|_{L^{1}} \\
& +\left\|\kappa\left(-\lambda^{*} ; y^{\prime}, \cdot\right)^{*}\left(\kappa(\lambda ; x, \cdot)-\kappa\left(\lambda ; x^{\prime}, \cdot\right)\right)\right\|_{L^{1}}
\end{aligned}
$$

for all pairs $(x, y),\left(x^{\prime}, y^{\prime}\right) \in \mathcal{G} \times \mathcal{G}$.

(ii) If $\mathcal{G}$ has finite total volume, then $L^{\infty}(\mathcal{G} \times \mathcal{G}) \hookrightarrow L^{2}(\mathcal{G} \times \mathcal{G})$ and hence the resolvents $\mathcal{R}\left( \pm \lambda, \widetilde{\mathbf{H}}^{1 / 2}\right)$ are Hilbert-Schmidt operators. Thus, by (5.1) we conclude that $\mathcal{R}(z, \widetilde{\mathbf{H}})$ is of trace class.

Observe that the first step in the proof of Theorem 5.1 is the factorization (5.1), which has the natural counterpart for semigroups

$$
\mathrm{e}^{-z \widetilde{\mathbf{H}}} \mathrm{e}^{-z \widetilde{\mathbf{H}}}=\mathrm{e}^{-2 z \widetilde{\mathbf{H}}}, \quad \operatorname{Re} z>0
$$

Because the semigroup generated by a self-adjoint semi-bounded extension $\widetilde{\mathbf{H}}$ is analytic, it is a bounded operator from the Hilbert space into its generator's form domain whenever $\operatorname{Re} z>0$. A careful look at the proof of Theorem 5.1 shows that this is sufficient to establish that $\mathrm{e}^{-z \widetilde{\mathbf{H}}}$ is an integral operator; all further steps in the proof of Theorem 5.1 carry over almost verbatim to the study of semigroups. We can hence easily deduce the following result.

Theorem 5.2. Let $\widetilde{\mathbf{H}}$ be a self-adjoint lower semi-bounded extension of $\mathbf{H}_{0}$ and let $z \in \mathbb{C}$ with $\operatorname{Re} z>0$. Then the following assertions hold.

(i) If the domain of $\widetilde{\mathbf{H}}$ is contained in $H^{1}(\mathcal{G})$, then the semigroup $\mathrm{e}^{-z \widetilde{\mathbf{H}}}$ generated by $\widetilde{\mathbf{H}}$ is an integral operator whose kernel is both of class $L^{\infty}(\mathcal{G} \times \mathcal{G})$ and jointly Hölder continuous of exponent $\beta=1 / 2$.

(ii) If additionally $\mathcal{G}$ has finite total volume, then $\mathrm{e}^{-z \tilde{\mathbf{H}}}$ is of trace class.

Estimating as in (5.3) and using analyticity of $\mathrm{e}^{-z \tilde{\mathbf{H}}}$ yields the inequality

$$
\left|p_{t}(x, y)-p_{t}\left(x^{\prime}, y\right)\right| \leq \frac{C}{\sqrt{t}} \sqrt{\varrho\left(x, x^{\prime}\right)}, \quad t>0, x, y, x^{\prime} \in \mathcal{G}
$$

for the heat kernel $p_{t}(x, y)$ of a nonnegative extension $\widetilde{\mathbf{H}}$, where in contrast to (5.3) the constant $C>0$ is independent of $t>0$. Such Hölder estimates are known
to be related to Sobolev-type inequalities and also important for upper and lower Gaussian bounds (cf., e.g., [20], [66, Chapter 6]). However, we do not pursue this line of study here and this will be done elsewhere.

Remark 5.3. A few remarks are in order.

(i) If $\sup _{\mathcal{R}}|\mathcal{R}|<\infty$, where the supremum is taken over all non-vertex paths without self-intersections, then the path metric $\varrho$ has a natural extension $\widehat{\varrho}$ to the end compactification $\widehat{\mathcal{G}}$. Moreover, in this case $(\widehat{\mathcal{G}}, \widehat{\varrho})$ coincides with the metric completion of $(\mathcal{G}, \varrho)$. Indeed, the metric completion of $(\mathcal{G}, \varrho)$ is obtained by adding to $\mathcal{G}$ equivalence classes of rays of finite length (see 34, Section 2.3] for details) and the distance of $x \in \mathcal{G}$ to a boundary point is defined as the "shortest length" of a path in the corresponding equivalence class starting at $x$.

Therefore, Theorem5.1] and Theorem 5.2 imply that in this case the corresponding resolvent and semigroup kernels have a bounded and uniformly

![](https://cdn.mathpix.com/cropped/2024_05_09_c24bfdaabe9c629d87a0g-24.jpg?height=44&width=1138&top_left_y=1035&top_left_x=556)
case $\operatorname{vol}(\mathcal{G})<\infty$ (see Remark 3.11), the topology generated by $\widehat{\varrho}$ on $\widehat{\mathcal{G}}$ can differ from the end compactification topology if $\operatorname{vol}(\mathcal{G})=\infty$.

(ii) Discreteness of the spectrum of the Friedrichs extension $\mathbf{H}_{F}$ is a standard fact in the case of finite total volume (see, e.g., [16, Prop. 3.11] or [56, Corollary 3.5(iv)]). However, Theorem 5.1 (ii) implies the stronger assertion that the resolvent of $\mathbf{H}_{F}$ belongs to the trace class if $\operatorname{vol}(\mathcal{G})<\infty$. Let us also stress that it is not true in general that every self-adjoint extension of $\mathbf{H}$ will have a discrete spectrum if $\operatorname{vol}(\mathcal{G})<\infty$, since in case of infinite deficiency indices such a self-adjoint extension could have a domain large enough to make compactness of the embedding of $H^{1}(\mathcal{G})$ into $L^{2}(\mathcal{G})$ irrelevant.

Recall that a self-adjoint extension $\widetilde{\mathbf{H}}$ of $\mathbf{H}_{0}$ is called Markovian if $\widetilde{\mathbf{H}}$ is a nonnegative self-adjoint extension and the corresponding quadratic form is a Dirichlet form (for definitions and further details we refer to [31, Chapter 1]). Hence the associated semigroup $\mathrm{e}^{-t \widetilde{\mathbf{H}}}, t>0$, as well as resolvents $\mathcal{R}(-\lambda, \widetilde{\mathbf{H}}), \lambda>0$, are Markovian: i.e., are both positivity preserving (map non-negative functions to nonnegative functions) and $L^{\infty}$-contractive (map the unit ball of $L^{\infty}(\mathcal{G})$, and then by duality of $L^{p}(\mathcal{G})$ for all $p \in[1, \infty]$, into itself). Let us stress that the Friedrichs extension $\mathbf{H}_{F}$ of $\mathbf{H}_{0}$ is a Markovian extension. Consider also the following quadratic form in $L^{2}(\mathcal{G})$

$$
\mathfrak{t}_{N}[f]=\int_{\mathcal{G}}\left|f^{\prime}(x)\right|^{2} d x, \quad \operatorname{dom}\left(\mathfrak{t}_{N}\right)=H^{1}(\mathcal{G})
$$

This form is non-negative and closed, hence we can associate in $L^{2}(\mathcal{G})$ a self-adjoint operator with it, let us denote it by $\mathbf{H}_{N}$. We will refer to it as the Neumann extension. It is straightforward to check that $\mathfrak{t}_{N}$ is a Dirichlet form and $\mathbf{H}_{N}$ is also a Markovian extension of $\mathbf{H}_{0}$.

It turns out that Theorems 5.1 and 5.2 apply to all Markovian extensions of $\mathbf{H}_{0}$. More specifically, the analog of the results for discrete Laplacians [39, Theorem 5.2] and Laplacians in Euclidean domains [31, Chapter 3] and Riemannian manifolds [37, Theorem 1.7] holds true for quantum graphs as well.

Theorem 5.4. If $\widetilde{\mathbf{H}}$ is a Markovian extension of $\mathbf{H}_{0}$, then $\operatorname{dom}(\widetilde{\mathbf{H}}) \subset H^{1}(\mathcal{G})$ and, moreover,

$$
\mathbf{H}_{N} \leq \widetilde{\mathbf{H}} \leq \mathbf{H}_{F}
$$

where the inequalities are understood in the sense of forms

We omit the proof of Theorem [5.4 since the proofs of either [39, Theorem 5.2] or [37, Lemma 3.6] carry over verbatim to our setting (see also the proof of 31, Theorem 3.3.1]).

Let us finish this section with the following observation.

Corollary 5.5. The following are equivalent:

(i) $\mathbf{H}_{0}$ has a unique Markovian extension,

(ii) $H_{0}^{1}(\mathcal{G})=H^{1}(\mathcal{G})$,

(iii) all topological ends of $\mathcal{G}$ have infinite volume, $\mathfrak{C}_{0}(\mathcal{G})=\emptyset$.

Proof. The claimed equivalences follow from Theorem 5.4 and Corollary 3.13,

Remark 5.6. Let us finish this section with a few comments.

(i) The equivalence $(i) \Leftrightarrow(i i)$ in Corollary 5.5 is known for Riemannian manifolds [37, Theorem 1.7] (see also [31, Chapter 3], 62, Theorem 1]) as well as for weighted Laplacians on graphs [39, Corollary 5.6]. However, to the best of our knowledge these settings do not admit any further geometric characterization.

(ii) The list of equivalences in Corollary 5.5 can be extended by adding a claim on the self-adjointness of the so-called Gaffney Laplacian. Namely, since $H_{0}^{1}(\mathcal{G})$ and $H^{1}(\mathcal{G})$ are Hilbert spaces, the operators denoted by $\nabla_{D}$ and $\nabla_{N}$ and defined in $L^{2}(\mathcal{G})$ on the domains, respectively, $H_{0}^{1}(\mathcal{G})$ and $H^{1}(\mathcal{G})$ by $f \mapsto f^{\prime}$ are closed. Notice that with this notation at hand we have $\mathbf{H}_{F}=\nabla_{D}^{*} \nabla_{D}$ and $\mathbf{H}_{N}=\nabla_{N}^{*} \nabla_{N}$. Now we can introduce the Gaffney Laplacian $\mathbf{H}_{G}:=\nabla_{D}^{*} \nabla_{N}$ as the restriction of the maximal operator $\mathbf{H}$ onto the domain (compare with [37, p. 610] for the definition in the manifolds case)

$$
\operatorname{dom}\left(\mathbf{H}_{G}\right):=\left\{f \in H^{1}(\mathcal{G}) \mid \nabla_{N} f \in \operatorname{dom}\left(\nabla_{D}^{*}\right)\right\}
$$

Clearly, $\operatorname{dom}\left(\mathbf{H}_{F}\right) \subseteq \operatorname{dom}\left(\mathbf{H}_{G}\right)$, $\operatorname{dom}\left(\mathbf{H}_{N}\right) \subseteq \operatorname{dom}\left(\mathbf{H}_{G}\right)$, and $\mathbf{H}_{G}$ is not necessarily symmetric. It turns out that $\mathbf{H}_{G}$ is symmetric (and hence selfadjoint) if and only if the Kirchhoff Laplacian $\mathbf{H}_{0}$ has a unique Markovian extension. Moreover, in this case $\mathbf{H}_{F}=\mathbf{H}_{N}=\mathbf{H}_{G}$ (cf. [37, Theorem 1.7(ii)] in the manifold setting). Let us mention that the Markovian/finite energy extensions of $\mathbf{H}_{0}$ are exactly the Markovian/self-adjoint restrictions of $\mathbf{H}_{G}$ and hence the deficiency indices of $\mathbf{H}_{G}^{*}=\nabla_{N}^{*} \nabla_{D}$ are equal to $\# \mathfrak{C}_{0}(\mathcal{G})$.

## 6. Finite energy Self-AdJoint extensions

It turns out that finite volume (topological) ends provide the right notion of the boundary for metric graphs to deal with finite energy and also with Markovian extensions of the minimal Kirchhoff Laplacian $\mathbf{H}_{0}$. In particular, we are going to show that this end space is well-behaved as concerns the introduction of both traces and normal derivatives. More specifically, the goal of this section is to give a description[^4]of finite energy self-adjoint extensions of $\mathbf{H}_{0}$ in the case when the number of finite volume ends of $\mathcal{G}$ is finite, that is, $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$. Notice that in this case all finite volume ends are free.

6.1. Normal derivatives at graph ends. Let $\widetilde{\mathcal{G}}=(\widetilde{\mathcal{V}}, \widetilde{\mathcal{E}})$ be a (possibly infinite) connected subgraph of $\mathcal{G}$. Recall that its boundary $\partial \widetilde{\mathcal{G}}$ (w.r.t. the natural topology on $\mathcal{G}$, see Section [2.1) is given by

$$
\partial \widetilde{\mathcal{G}}=\left\{v \in \widetilde{\mathcal{V}} \mid \operatorname{deg}_{\widetilde{\mathcal{G}}}(v)<\operatorname{deg}_{\mathcal{G}}(v)\right\}
$$

For a function $f \in \operatorname{dom}(\mathbf{H})$, we define its (inward) normal derivative at $v \in \partial \widetilde{\mathcal{G}}$ by

$$
\frac{\partial f}{\partial n_{\tilde{\mathcal{G}}}}(v):=\sum_{e \in \mathcal{E}_{v} \cap \tilde{\mathcal{E}}} f_{e}^{\prime}(v)
$$

With this definition at hand, we end up with the following useful integration by parts formula.

Lemma 6.1. Let $\widetilde{\mathcal{G}}$ be a compact (not necessarily connected) subgraph of the metric graph $\mathcal{G}$. Then

$$
-\int_{\widetilde{\mathcal{G}}} f^{\prime \prime}(x) g(x) d x=\int_{\widetilde{\mathcal{G}}} f^{\prime}(x) g^{\prime}(x) d x+\sum_{v \in \partial \widetilde{\mathcal{G}}} g(v) \frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v)
$$

for all $f \in \operatorname{dom}(\mathbf{H})$ and $g \in H^{1}(\widetilde{\mathcal{G}})$. In particular,

$$
-\int_{\widetilde{\mathcal{G}}} f^{\prime \prime}(x) d x=\sum_{v \in \partial \widetilde{\mathcal{G}}} \frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v)
$$

Proof. The claim follows immediately from integrating by parts, taking into account that $f$ satisfies (2.7). Setting $g \equiv 1$ in (6.3), we arrive at (6.4).

In order to simplify our considerations, we need to introduce the following notion. Let $\gamma \in \mathfrak{C}(\mathcal{G})$ be a (topological) end of $\mathcal{G}$. Consider a sequence $\left(\mathcal{G}_{n}\right)$ of connected subgraphs of $\mathcal{G}$ such that $\mathcal{G}_{n} \supseteq \mathcal{G}_{n+1}$ and $\# \partial \mathcal{G}_{n}<\infty$ for all $n$. We say that the sequence $\left(\mathcal{G}_{n}\right)$ is a graph representation of the end $\gamma \in \mathfrak{C}(\mathcal{G})$ if there is a sequence of open sets $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that for each $n \geq 0$ there exist $j$ and $k$ such that $\mathcal{G}_{n} \supseteq U_{j}$ and $U_{n} \supseteq \mathcal{G}_{k}$. It is easily seen that all graphs $\mathcal{G}_{n}$ are infinite (they have infinitely many edges). Moreover, graph representations $\left(\mathcal{G}_{n}\right)$ of an end can be constructed with the help of compact exhaustions; in particular each graph end $\gamma \in \mathfrak{C}(\mathcal{G})$ has a representation by subgraphs (see Section 2.2).

Proposition 6.2. Let $\mathcal{G}$ be a metric graph and let $\gamma \in \mathfrak{C}(\mathcal{G})$ be a free end of finite volume. Then for every function $f \in \operatorname{dom}(\mathbf{H})$ and any sequence $\left(\mathcal{G}_{k}\right)$ of subgraphs representing $\gamma$, the limit

$$
\lim _{k \rightarrow \infty} \sum_{v \in \partial \mathcal{G}_{k}} \frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)
$$

exists and is independent of the choice of $\left(\mathcal{G}_{k}\right)$.

Proof. First of all, notice that uniqueness of the limit follows from the inclusion property in the definition of the graph representations of $\gamma$. Hence we only need to show that the limit in (6.5) indeed exists.

Let $\left(\mathcal{G}_{k}\right)$ be a graph representation of a free finite volume end $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$. Since $\gamma$ is free, we can assume that $\operatorname{vol}\left(\mathcal{G}_{0}\right)<\infty$ and that $\mathcal{G}_{0} \cap U_{k}=\varnothing$ eventually for every sequence $\mathcal{U}=\left(U_{k}\right)$ representing an end $\gamma^{\prime} \neq \gamma$. First observe that $\widetilde{\mathcal{G}}=\mathcal{G}_{k} \backslash \mathcal{G}_{j}$ can again be identified with a compact subgraph of $\mathcal{G}$ whenever $k \leq j$. Indeed, if $\widetilde{\mathcal{G}}$ has infinitely many edges $\left\{e_{n}\right\} \subset \mathcal{E}$, choose for each $n$ a point $x_{n}$ in the interior of the edge $e_{n}$. Since $\widehat{\mathcal{G}}=\mathcal{G} \cup \mathfrak{C}(\mathcal{G})$ is compact, the set $\left\{x_{n}\right\}$ has an accumulation point $x \in \widehat{\mathcal{G}}$. By construction, $x \notin \mathcal{G}$ and hence $x \in \widehat{\mathcal{G}} \backslash \mathcal{G}=\mathfrak{C}(\mathcal{G})$ is an end. However, we have that $x_{n} \notin \mathcal{G}_{j}$ and recalling (2.3) and (2.4), this implies that $x=\gamma^{\prime}$ for a topological end $\gamma^{\prime} \neq \gamma$. On the other hand, $x_{n} \in \mathcal{G}_{0}$ for all $n$ and using the properties of $\mathcal{G}_{0}$ and (2.3)-(2.4) once again, we arrive at a contradiction.

Now, using (6.1) it is straightforward to verify that

$$
\sum_{v \in \partial \mathcal{G}_{k}} \frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)-\sum_{v \in \partial \mathcal{G}_{j}} \frac{\partial f}{\partial n_{\mathcal{G}_{j}}}(v)=\sum_{v \in \partial \widetilde{\mathcal{G}}} \frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v)
$$

Hence by (6.4) and the Cauchy-Schwarz inequality, we get

$$
\left|\sum_{v \in \partial \mathcal{G}_{k}} \frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)-\sum_{v \in \partial \mathcal{G}_{j}} \frac{\partial f}{\partial n_{\mathcal{G}_{j}}}(v)\right|=\left|\int_{\mathcal{G}_{k} \backslash \mathcal{G}_{j}} f^{\prime \prime}(x) d x\right| \leq \sqrt{\operatorname{vol}\left(\mathcal{G}_{k}\right)}\|\mathbf{H} f\|_{L^{2}(\mathcal{G})}
$$

whenever $k \leq j$. This implies the existence of the limit in (6.5) since $\operatorname{vol}\left(\mathcal{G}_{k}\right)=o(1)$ as $k \rightarrow \infty$.

Proposition 6.2 now enables us to introduce a normal derivative at graph ends.

Definition 6.3. Let $\gamma \in \mathfrak{C}(\mathcal{G})$ be a free end of finite volume and let $\left(\mathcal{G}_{k}\right)$ be a graph representation of $\gamma$. Then for every $f \in \operatorname{dom}(\mathbf{H})$

$$
\partial_{n} f(\gamma):=\frac{\partial f}{\partial n}(\gamma):=\lim _{k \rightarrow \infty} \sum_{v \in \partial \mathcal{G}_{k}} \frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)
$$

is called the normal derivative of $f$ at $\gamma$.

Remark 6.4. In fact, it is not difficult to extend the definitions (6.2) and (6.7) to general sequences $\mathcal{U}=\left(U_{n}\right)$ of open sets representing the free end $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$. However, while the idea of the proof of Proposition 6.2 naturally carries over, the analysis becomes more technical and we restrict to the case of subgraphs for the sake of a clear exposition.

Let us mention that the normal derivative can also be expressed in terms of compact exhaustions.

Lemma 6.5. Let $\mathcal{G}$ be a metric graph having finite total volume and only one end $\gamma, \mathfrak{C}(\mathcal{G})=\{\gamma\}$. If $\left(\mathcal{F}_{k}\right)$ is a compact exhaustion of $\mathcal{G}$ and $f \in \operatorname{dom}(\mathbf{H})$, then

$$
\partial_{n} f(\gamma)=-\lim _{k \rightarrow \infty} \sum_{v \in \partial \mathcal{F}_{k}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v)
$$

The fact that we are not approximating $\gamma$ by its neighborhoods, but rather by compact subgraphs, is responsible for the different sign in (6.7) and (6.8).

Proof. First of all, notice that $\mathcal{G} \backslash \mathcal{F}_{k}$ can be identified with a subgraph of $\mathcal{G}$ and

$$
-\sum_{v \in \partial \mathcal{F}_{k}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v)=\sum_{v \in \partial\left(\mathcal{G} \backslash \mathcal{F}_{k}\right)} \frac{\partial f}{\partial n_{\mathcal{G} \backslash \mathcal{F}_{k}}}(v)
$$

for all $f \in \operatorname{dom}(\mathbf{H})$. If, moreover, $\mathcal{G} \backslash \mathcal{F}_{k}$ is a connected subgraph for all $k \geq 0$, then it is clear that $\left(\mathcal{G}_{k}\right)$ with $\mathcal{G}_{k}:=\mathcal{G} \backslash \mathcal{F}_{k}$ for all $k \geq 0$, is a graph representation of $\gamma$ and this proves (6.8) in this case.

If $\mathcal{G} \backslash \mathcal{F}_{k}$ is not connected, then it has only one infinite connected component $\mathcal{G}_{k}^{\gamma}$ and finitely many compact components (since $\mathfrak{C}(\mathcal{G})=\{\gamma\})$. Adding these compact components to $\mathcal{F}_{k}$, we obtain a compact exhaustion $\left(\mathcal{F}_{k}^{\prime}\right)$ with $\mathcal{G} \backslash \mathcal{F}_{k}^{\prime}=\mathcal{G}_{k}^{\gamma}$. Arguing as in the proof of Proposition 6.2 (see (6.6)), we get

$$
\left|\sum_{v \in \partial \mathcal{F}_{k}^{\prime}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}^{\prime}}}(v)-\sum_{v \in \partial \mathcal{F}_{k}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v)\right|=\left|\int_{\mathcal{F}_{k}^{\prime} \backslash \mathcal{F}_{k}} f^{\prime \prime}(x) d x\right|=o(1)
$$

as $k \rightarrow \infty$. Hence (6.8) holds true also in the general case.

6.2. Properties of the trace and normal derivatives. In this section, we collect some basic properties of the trace maps. We shall adopt the following notation. Since we shall always assume throughout this section that $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$, we set $\mathcal{H}:=\ell^{2}\left(\mathfrak{C}_{0}(\mathcal{G})\right)$, which can be further identified with $\mathbb{C}^{\# \mathfrak{C}_{0}(\mathcal{G})}$. Next, we introduce the maps $\Gamma_{0}: H^{1}(\mathcal{G}) \rightarrow \mathcal{H}$ and $\Gamma_{1}: \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G}) \rightarrow \mathcal{H}$ by

$$
\Gamma_{0}: f \mapsto(f(\gamma))_{\gamma \in \mathfrak{C}_{0}(\mathcal{G})}, \quad \Gamma_{1}: f \mapsto\left(\partial_{n} f(\gamma)\right)_{\gamma \in \mathfrak{C}_{0}(\mathcal{G})}
$$

where the boundary values and normal derivative of $f$ are defined by (3.4) and (6.7), respectively.

Proposition 6.6. Let $\mathcal{G}$ be a metric graph with $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$. Then:

(i) For every $\widehat{f} \in \mathcal{H}$, there exists $f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ such that

$$
\Gamma_{0} f=\widehat{f}, \quad \Gamma_{1} f=0
$$

(ii) Moreover, the Gauss-Green formula

$$
\langle\mathbf{H} f, g\rangle_{L^{2}(\mathcal{G})}=\left\langle f^{\prime}, g^{\prime}\right\rangle_{L^{2}(\mathcal{G})}-\left\langle\Gamma_{1} f, \Gamma_{0} g\right\rangle_{\mathcal{H}}
$$

holds true for every $f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ and $g \in H^{1}(\mathcal{G})$.

Proof. (i) Since $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$, each finite volume end $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$ is free. For every $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$, let $\mathcal{G}^{\gamma}$ be a subgraph with the properties as in Remark 2.6. We can also assume that $\operatorname{vol}\left(\mathcal{G}^{\gamma}\right)<\infty$. Following the proof of Theorem 3.10, we can construct for each end $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$ a function $f_{\gamma} \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ such that $f_{\gamma}$ is nonconstant only on finitely many edges (since $\left.\# \partial \mathcal{G}^{\gamma}<\infty\right), f_{\gamma}(\gamma)=1$ and $f_{\gamma}\left(\gamma^{\prime}\right)=0$ for all other ends $\gamma^{\prime} \in \mathfrak{C}_{0}(\mathcal{G}) \backslash\{\gamma\}$. Clearly, $\Gamma_{1} f_{\gamma}=0$ for every $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$. Thus, setting

$$
f=\sum_{\gamma \in \mathfrak{C}_{0}(\mathcal{G})} \widehat{f}(\gamma) f_{\gamma}
$$

for a given $\widehat{f} \in \mathcal{H}$, we clearly have $\Gamma_{0} f=\widehat{f}$ and $\Gamma_{1} f=0$.
(ii) Let us first show that (6.10) holds true for all $f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ if $g=f_{\gamma} \in H^{1}(\mathcal{G})$. Take a compact exhaustion $\left(\mathcal{F}_{k}\right)$ of $\mathcal{G}$. Then by Lemma 6.1,

$$
\begin{aligned}
\left\langle\mathbf{H} f, f_{\gamma}\right\rangle_{L^{2}(\mathcal{G})} & -\left\langle f^{\prime}, f_{\gamma}^{\prime}\right\rangle_{L^{2}(\mathcal{G})}=\lim _{k \rightarrow \infty}\left\langle\mathbf{H} f, f_{\gamma}\right\rangle_{L^{2}\left(\mathcal{F}_{k}\right)}-\left\langle f^{\prime}, f_{\gamma}^{\prime}\right\rangle_{L^{2}\left(\mathcal{F}_{k}\right)} \\
& =\lim _{k \rightarrow \infty} \sum_{v \in \partial \mathcal{F}_{k}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v) f_{\gamma}(v)^{*}=\lim _{k \rightarrow \infty} \sum_{v \in \partial \mathcal{F}_{k} \cap \mathcal{V}_{\gamma}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v)
\end{aligned}
$$

where $\mathcal{V}^{\gamma}$ is the set of vertices of $\mathcal{G}^{\gamma}$. Notice that the subgraph $\mathcal{G}^{\gamma}$ itself is a connected infinite graph having finite total volume and exactly one end, which can be identified with $\gamma$ in an obvious way. Moreover, setting $\mathcal{F}_{k}^{\gamma}:=\mathcal{F}_{k} \cap \mathcal{G}^{\gamma}$ for all $k \geq 0$ and noting that $\mathcal{F}_{k}^{\gamma}$ is connected for all sufficiently large $k$, the sequence $\left(\mathcal{F}_{k}^{\gamma}\right)$ provides a compact exhaustion of $\mathcal{G}^{\gamma}$. Since $\partial_{\mathcal{G}^{\gamma}} \mathcal{F}_{k}^{\gamma}=\partial \mathcal{F}_{k} \cap \mathcal{V}^{\gamma}$ and

$$
\frac{\partial f}{\partial n_{\mathcal{F}_{k}^{\gamma}}}(v)=\frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v), \quad v \in \partial_{\mathcal{G}^{\gamma}} \mathcal{F}_{k}^{\gamma}
$$

for all large enough $k \geq 0$, we get by applying Lemma 6.5

$$
\left\langle\mathbf{H} f, f_{\gamma}\right\rangle_{L^{2}(\mathcal{G})}-\left\langle f^{\prime}, f_{\gamma}^{\prime}\right\rangle_{L^{2}(\mathcal{G})}=\lim _{k \rightarrow \infty} \sum_{v \in \mathcal{F}_{k} \cap \mathcal{V}^{\gamma}} \frac{\partial f}{\partial n_{\mathcal{F}_{k}^{\gamma}}}(v)=-\frac{\partial f}{\partial n}(\gamma)
$$

Hence (6.10) holds true if $g=f_{\gamma} \in H^{1}(\mathcal{G})$.

Now observe that a simple integration by parts implies that (6.10) is valid for all compactly supported $g \in H^{1}(\mathcal{G})$. By continuity and Theorem 3.12 this extends further to all $g \in H_{0}^{1}(\mathcal{G})$. Finally, setting $\tilde{g}:=g-\sum_{\gamma \in \mathfrak{C}_{0}(\mathcal{G})} g(\gamma) f_{\gamma}$ for $g \in H^{1}(\mathcal{G})$, it is immediate to check that, by Theorem [3.12, $\tilde{g} \in H_{0}^{1}(\mathcal{G})$. It remains to use the linearity of $\Gamma_{0}$.

It turns out that the domain of the Neumann extension admits a simple description.

Corollary 6.7. Let $\mathcal{G}$ be a metric graph with $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$. Then the Neumann extension $\mathbf{H}_{N}$ is given as the restriction $\mathbf{H}_{N}=\left.\mathbf{H}\right|_{\operatorname{dom}\left(\mathbf{H}_{N}\right)}$ to the domain

$$
\operatorname{dom}\left(\mathbf{H}_{N}\right)=\left\{f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G}) \mid \Gamma_{1} f=0\right\}
$$

Proof. By the first representation theorem [50, Chapter VI.2.1], $\operatorname{dom}\left(\mathbf{H}_{N}\right)$ consists of all functions $f \in H^{1}(\mathcal{G})$ such that there exists $h \in L^{2}(\mathcal{G})$ with

$$
\left\langle f^{\prime}, g^{\prime}\right\rangle_{L^{2}(\mathcal{G})}=\langle h, g\rangle_{L^{2}(\mathcal{G})}, \quad \text { for all } g \in H^{1}(\mathcal{G})
$$

Moreover, in this case $\mathbf{H}_{N} f:=h$. Taking into account Proposition 6.6 and the fact that $\mathbf{H}_{N}$ is a restriction of $\mathbf{H}$, we immediately arrive at (6.11).

Our next goal is to prove surjectivity of the normal derivative map.

Proposition 6.8. If $\mathcal{G}$ is a metric graph with $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$, then the mapping $\Gamma_{1}$ is surjective.

In fact, Proposition 6.8 will follow from the following lemma.

Lemma 6.9. Suppose $\mathcal{G}$ is a metric graph with $\operatorname{vol}(\mathcal{G})<\infty$ and only one end, $\mathfrak{C}(\mathcal{G})=\{\gamma\}$. Then there exists $f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ such that

$$
\partial_{n} f(\gamma) \neq 0
$$

Proof. We will proceed by contradiction. Suppose that $\partial_{n} g(\gamma)=0$ for all $g \in$ $\operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$. Then, by Corollary 6.7, $\operatorname{dom}\left(\mathbf{H}_{F}\right) \subseteq \operatorname{dom}\left(\mathbf{H}_{N}\right)=\operatorname{dom}(\mathbf{H}) \cap$ $H^{1}(\mathcal{G})$. However, both $\mathbf{H}_{F}$ and $\mathbf{H}_{N}$ are self-adjoint restrictions of $\mathbf{H}$ and hence $\operatorname{dom}\left(\mathbf{H}_{F}\right)=\operatorname{dom}\left(\mathbf{H}_{N}\right)$. Therefore, $\mathbf{H}_{F}=\mathbf{H}_{N}$ and their quadratic forms also coincide, which implies that $H_{0}^{1}(\mathcal{G})=H^{1}(\mathcal{G})$. This contradicts Corollary 3.13 and hence completes the proof.

Proof of Proposition 6.8. Let $\mathcal{G}^{\gamma}, \gamma \in \mathfrak{C}_{0}(\mathcal{G})$ be the subgraphs of $\mathcal{G}$ constructed in the proof of Proposition 6.6 (i). Every $\mathcal{G}^{\gamma}$ is a connected graph with $\operatorname{vol}\left(\mathcal{G}^{\gamma}\right)<\infty$ and only one end, which can be identified with $\gamma$. Hence we can apply Lemma 6.9 to obtain a function $\tilde{g}_{\gamma} \in \operatorname{dom}\left(\mathbf{H}^{\gamma}\right) \cap H^{1}\left(\mathcal{G}^{\gamma}\right)$ such that $\partial_{n} \tilde{g}_{\gamma}(\gamma)=1$. Here $\mathbf{H}^{\gamma}$ denotes the Kirchhoff Laplacian on $\mathcal{G}^{\gamma}$.

Since $\# \partial \mathcal{G}^{\gamma}<\infty$, we can obviously extend $\tilde{g}_{\gamma}$ to a function $g_{\gamma}$ on $\mathcal{G}$ such that $g_{\gamma} \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ and $g_{\gamma}$ is identically zero on a neighborhood of each end $\gamma^{\prime} \neq$ $\gamma$ (see also the proof of Theorem 3.10). In particular, this implies that $\partial_{n} g_{\gamma}\left(\gamma^{\prime}\right)=0$ for all $\gamma^{\prime} \in \mathfrak{C}_{0}(\mathcal{G}) \backslash\{\gamma\}$. Upon identification of $\gamma$ with the single end of $\mathcal{G}^{\gamma}$ we also have that

$$
\partial_{n} g_{\gamma}(\gamma)=\partial_{n} \tilde{g}_{\gamma}(\gamma)=1
$$

This immediately implies surjectivity.

6.3. Description of self-adjoint extensions. Our next goal is a description of all finite energy self-adjoint extensions of $\mathbf{H}_{0}$, that is, self-adjoint extensions $\widetilde{\mathbf{H}}$ satisfying the inclusion $\operatorname{dom}(\widetilde{\mathbf{H}}) \subset H^{1}(\mathcal{G})$. We will be able to do this under the additional assumption that $\mathcal{G}$ has finitely many finite volume ends. Recall that in this case $\mathcal{H}=\ell^{2}\left(\mathfrak{C}_{0}(\mathcal{G})\right)$ is a finite dimensional Hilbert space.

Let $C, D$ be two linear operators on $\mathcal{H}$ satisfying Rofe-Beketov conditions [68]:

$$
C D^{*}=D C^{*}, \quad \operatorname{rank}(C \mid D)=\operatorname{dim} \mathcal{H}=\# \mathfrak{C}_{0}(\mathcal{G})
$$

Consider the quadratic form $\mathfrak{t}_{C, D}$ defined by

$$
\mathfrak{t}_{C, D}[f]:=\int_{\mathcal{G}}\left|f^{\prime}(x)\right|^{2} d x+\left\langle D^{-1} C \Gamma_{0} f, \Gamma_{0} f\right\rangle_{\mathcal{H}}
$$

on the domain

$$
\operatorname{dom}\left(\mathfrak{t}_{C, D}\right):=\left\{f \in H^{1}(\mathcal{G}) \mid \Gamma_{0} f \in \operatorname{ran}\left(D^{*}\right)\right\}
$$

Here and in the following the mappings $\Gamma_{0}$ and $\Gamma_{1}$ are given by (6.9) and $D^{-1}: \operatorname{ran}(D) \rightarrow$ $\operatorname{ran}\left(D^{*}\right)$ denotes the inverse of the restriction $\left.D\right|_{\mathrm{ker}(D)^{\perp}}: \operatorname{ran}\left(D^{*}\right) \rightarrow \operatorname{ran}(D)$. In particular, (6.12) implies that $\mathfrak{t}_{C, D}[f]$ is well-defined for all $f \in \operatorname{dom}\left(\mathfrak{t}_{C, D}\right)$ (see also (A.4) $)$.

Remark 6.10. It is straightforward to check that $\mathfrak{t}_{I, 0}=\mathfrak{t}_{F}$ and $\mathfrak{t}_{0, I}=\mathfrak{t}_{N}$ are the quadratic forms corresponding to the Friedrichs extension $\mathbf{H}_{F}$ and, respectively, Neumann extension $\mathbf{H}_{N}$ (see Remark 3.1 and (5.5)).

Now we are in position to state the main result of this section.

Theorem 6.11. Let $\mathcal{G}$ be a metric graph with finitely many finite volume ends, $\# \mathfrak{C}_{0}(\mathcal{G})<\infty$. Let also $C, D$ be linear operators on $\mathcal{H}$ satisfying Rofe-Beketov conditions (6.12). Then:

(i) The form $\mathfrak{t}_{C, D}$ given by (6.13), (6.14) is closed and lower semi-bounded in $L^{2}(\mathcal{G})$.
(ii) The self-adjoint operator $\mathbf{H}_{C, D}$ associated with the form $\mathfrak{t}_{C, D}$ is a self-adjoint extension of $\mathbf{H}_{0}$ and its domain is explicitly given by

$$
\operatorname{dom}\left(\mathbf{H}_{C, D}\right)=\left\{f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G}) \mid C \Gamma_{0} f+D \Gamma_{1} f=0\right\}
$$

(iii) Conversely, if $\widetilde{\mathbf{H}}$ is a self-adjoint extension of $\mathbf{H}_{0}$ such that $\operatorname{dom}(\widetilde{\mathbf{H}}) \subset H^{1}(\mathcal{G})$, then there are $C, D$ satisfying (6.12) such that $\widetilde{\mathbf{H}}=\mathbf{H}_{C, D}$.

(iv) Moreover, $\widetilde{\mathbf{H}}=\mathbf{H}_{C, D}$ is a Markovian extension if and only if the corresponding quadratic form $\widehat{\mathfrak{t}}_{C, D}[y]=\left\langle D^{-1} C y, y\right\rangle_{\mathcal{H}}, \operatorname{dom}(\widehat{\mathfrak{t}})=\operatorname{ran}\left(D^{*}\right)$ is a Dirichlet form on $\mathcal{H}$ in the wide sense ${ }^{\Downarrow}$

Proof. (i) Since $\mathcal{H}$ is finite dimensional, it is straightforward to see that the form $\mathfrak{t}_{C, D}$ is closed and lower semi-bounded in $L^{2}(\mathcal{G})$ whenever $C$ and $D$ satisfy (6.12).

(ii) By the first representation theorem [50, Chapter VI.2.1], $\operatorname{dom}\left(\mathbf{H}_{C, D}\right)$ consists of all functions $f \in \operatorname{dom}\left(\mathfrak{t}_{C, D}\right) \subseteq H^{1}(\mathcal{G})$ for which there exists $h \in L^{2}(\mathcal{G})$ such that

$$
\left\langle f^{\prime}, g^{\prime}\right\rangle_{L^{2}(\mathcal{G})}+\left\langle D^{-1} C \Gamma_{0} f, \Gamma_{0} g\right\rangle_{\mathcal{H}}=\langle h, g\rangle_{L^{2}(\mathcal{G})}
$$

for all $g \in \operatorname{dom}\left(\mathfrak{t}_{C, D}\right)$. Moreover, in this case $\mathbf{H}_{C, D} f:=h$.

The Gauss-Green identity (6.10) implies that for any $f \in \operatorname{dom}\left(\mathbf{H}_{C, D}\right)$ and $g \in$ $\operatorname{dom}\left(\mathfrak{t}_{C, D}\right)$,

$$
\left\langle D^{-1} C \Gamma_{0} f, \Gamma_{0} g\right\rangle_{\mathcal{H}}=-\left\langle\Gamma_{1} f, \Gamma_{0} g\right\rangle_{\mathcal{H}} .
$$

Taking into account the surjectivity property in Proposition 6.6(i), the inclusion " $\subseteq$ " in (6.15) follows. The converse inclusion is then an immediate consequence of the Gauss-Green identity (6.10).

(iii) To prove the claim, it suffices to show that

$$
\Theta=\left\{\left(\Gamma_{0} f, \Gamma_{1} f\right) \mid f \in \operatorname{dom}(\widetilde{\mathbf{H}})\right\} \subseteq \mathcal{H} \times \mathcal{H}
$$

is a self-adjoint linear relation (for further details we refer to Appendix (A). By definition, $\Theta^{*}$ is given by

$$
\Theta^{*}=\left\{(g, h) \in \mathcal{H} \times \mathcal{H} \mid\left\langle\Gamma_{1} f, g\right\rangle_{\mathcal{H}}=\left\langle\Gamma_{0} f, h\right\rangle_{\mathcal{H}} \text { for all } f \in \operatorname{dom}(\widetilde{\mathbf{H}})\right\}
$$

The inclusion $\Theta \subseteq \Theta^{*}$ follows immediately from the Gauss-Green identity (6.10) and the self-adjointness of $\widetilde{\mathbf{H}}$. Indeed, we clearly have

$$
0=\langle\widetilde{\mathbf{H}} f, \tilde{f}\rangle_{L^{2}(\mathcal{G})}-\langle f, \widetilde{\mathbf{H}} \tilde{f}\rangle_{L^{2}(\mathcal{G})}=-\left\langle\Gamma_{1} f, \Gamma_{0} \tilde{f}\right\rangle_{\mathcal{H}}+\left\langle\Gamma_{0} f, \Gamma_{1} \tilde{f}\right\rangle_{\mathcal{H}}
$$

for all functions $f, \tilde{f} \in \operatorname{dom}(\widetilde{\mathbf{H}})$. On the other hand, by Proposition 6.8 and Proposition 6.6.6. for any $(g, h) \in \Theta^{*}$ there is a function $\tilde{f} \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G})$ such that $g=\Gamma_{0} \tilde{f}$ and $h=\Gamma_{1} \tilde{f}$. Employing the identity (6.10) once again, we see that

$$
\begin{aligned}
\langle\widetilde{\mathbf{H}} f, \tilde{f}\rangle_{L^{2}(\mathcal{G})} & =\left\langle f^{\prime}, \tilde{f}^{\prime}\right\rangle_{L^{2}(\mathcal{G})}-\left\langle\Gamma_{1} f, g\right\rangle_{\mathcal{H}} \\
& =\left\langle f^{\prime}, \tilde{f}^{\prime}\right\rangle_{L^{2}(\mathcal{G})}-\left\langle\Gamma_{0} f, h\right\rangle_{\mathcal{H}}=\langle f, \mathbf{H} \tilde{f}\rangle_{L^{2}(\mathcal{G})}
\end{aligned}
$$

for all $f \in \operatorname{dom}(\widetilde{\mathbf{H}})$. Hence, $\tilde{f} \in \operatorname{dom}(\widetilde{\mathbf{H}})$ and in particular $(g, h) \in \Theta$. Since $\Theta$ is self-adjoint, there are $C$ and $D$ in $\mathcal{H}$ satisfying Rofe-Beketov conditions (6.12) and such that $\Theta=\{(f, g) \in \mathcal{H} \times \mathcal{H} \mid C f+D g=0\}$.[^5](iv) The first direction of the equivalence is clear: since the quadratic form $\mathfrak{t}_{N}$ associated with the Neumann extension $\mathbf{H}_{N}$ is Markovian and

$$
\Gamma_{0}(\varphi \circ f)=((\varphi \circ f)(\gamma))_{\gamma \in \mathfrak{C}_{0}(\mathcal{G})}=: \varphi \circ\left(\Gamma_{0} f\right)
$$

for all functions $f \in H^{1}(\mathcal{G})$ and every normal contraction $\varphi$ the extension $\mathbf{H}_{C, D}$ is Markovian if $\widehat{\mathfrak{t}}_{C, D}$ is a Dirichlet form on $\mathcal{H}$ in the wide sense.

To prove the converse direction, let, for simplicity, $f \in \operatorname{dom}\left(\widehat{\mathfrak{t}}_{C, D}\right)$ be real-valued and fix some real-valued $\tilde{f} \in H^{1}(\mathcal{G})$ with $\Gamma_{0} \tilde{f}=f$ (the existence of such an $\tilde{f}$ follows from Proposition 6.6). For any (real-valued) normal contraction $\varphi: \mathbb{R} \rightarrow \mathbb{R}$, we can construct a continuous and piecewise affine function $\psi: \mathbb{R} \rightarrow \mathbb{R}$ (i.e., $\psi$ is affine on every component of $\mathbb{R} \backslash\left\{x_{1}, \ldots, x_{M}\right\}$ for finitely many points $\left.x_{1}, \ldots, x_{M}\right)$ such that $\psi(0)=0, \psi(f(\gamma))=\varphi(f(\gamma))$ for all $\gamma \in \mathfrak{C}_{0}(\mathcal{G})$ and $\left|\psi^{\prime}(x)\right|=1$ for almost every $x \in \mathbb{R}$ Notice that every function $\psi$ with the above properties is a normal contraction. Hence, if $\mathfrak{t}_{C, D}$ is Markovian, it follows that $\psi \circ \tilde{f} \in \operatorname{dom}\left(\mathfrak{t}_{C, D}\right)$. However, its boundary values are precisely given by

$$
\Gamma_{0}(\psi \circ \tilde{f})=\psi \circ f=\varphi \circ f
$$

and we conclude that $\varphi \circ f$ belongs to $\operatorname{dom}\left(\widehat{\mathfrak{t}}_{C, D}\right)$. Finally, the Markovian property of $\mathfrak{t}_{C, D}$ implies that

$$
\mathfrak{t}_{C, D}[\psi \circ \tilde{f}]=\int_{\mathcal{G}}\left|(\psi \circ \tilde{f})^{\prime}\right|^{2} d x+\widehat{\mathfrak{t}}_{C, D}[\varphi \circ f] \leq \mathfrak{t}_{C, D}[\tilde{f}]=\int_{\mathcal{G}}\left|\tilde{f}^{\prime}\right|^{2} d x+\widehat{\mathfrak{t}}_{C, D}[f]
$$

and noticing that $\left|(\psi \circ \tilde{f})^{\prime}\right|=\left|\tilde{f}^{\prime}\right|$ almost everywhere on $\mathcal{G}$, the proof is complete.

Let us demonstrate Theorem 6.11 by applying it to Cayley graphs.

Corollary 6.12. Let $\mathcal{G}_{d}$ be a Cayley graph of a finitely generated group $\mathrm{G}$ with one end. Then the Kirchhoff Laplacian $\mathbf{H}_{0}$ admits a unique Markovian extension if and only if the underlying metric graph $\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$ has infinite total volume, $\operatorname{vol}(\mathcal{G})=\infty$. Moreover, if $\mathcal{G}$ has finite total volume, then the set of all Markovian extensions of $\mathbf{H}_{0}$ forms a one-parameter family given explicitly by

$$
\operatorname{dom}\left(\mathbf{H}_{\theta}\right)=\left\{f \in \operatorname{dom}(\mathbf{H}) \cap H^{1}(\mathcal{G}) \mid \cos (\theta) \Gamma_{0} f+\sin (\theta) \Gamma_{1} f=0\right\}
$$

where $\theta \in[0, \pi / 2]$.

Taking into account that amenable groups have finitely many ends, the above result applies to amenable finitely generated groups, which are not virtually infinite cyclic (see Remark [2.5(iv)). In a similar way one can obtain a complete description of Markovian extensions in the case of virtually infinite cyclic groups, however, they have two ends and the corresponding description looks a little bit more cumbersome and we leave it to the reader (cf. [31, p.147]). The case of groups with infinitely many ends remains an open highly nontrivial problem.

Remark 6.13. A few remarks are in order.[^6](i) Let us mention that in the case when the domain of the maximal operator $\mathbf{H}$ is contained in $H^{1}(\mathcal{G})$ and $\mathcal{G}$ has finitely many finite volume ends (notice that by Theorem4.1 in this case $\left.\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\# \mathfrak{C}_{0}(\mathcal{G})<\infty\right)$, Proposition 6.11 provides a complete description of all self-adjoint extensions of $\mathbf{H}_{0}$. Let us also mention that Proposition 6.11 provides a complete description of all self-adjoint restrictions of the Gaffney Laplacian $\mathbf{H}_{G}$, see Remark [5.6(ii).

(ii) Some of the results of this section extend (to a certain extent) to the case of infinitely many ends. Let us stress that by Proposition 4.9 in the case when $\mathcal{G}$ has a finite volume end which is not free the above results would lead only to some (not all!) self-adjoint extensions of $\mathbf{H}_{0}$. In our opinion, even in the case of radially symmetric trees having finite total volume the description of all self-adjoint extensions of $\mathbf{H}_{0}$ is a difficult problem.

(iii) Similar relations between Markovian realizations of elliptic operators on domains or finite metric graphs (with general couplings at the vertices) on one hand, and Dirichlet property of the corresponding quadratic form's boundary term on the other hand, are of course well known in the literature (see, e.g., [14, Proposition 5.1], [47, Theorem 3.5], [57, Theorem 6.1]). However, the setting of infinite metric graphs additionally requires much more advanced considerations of combinatorial and topological nature. In particular, it seems noteworthy to us that the results of the previous sections provide the right notion of the boundary for metric graphs, namely, the set of finite volume ends, to deal with finite energy and also with Markovian extensions of the minimal Kirchhoff Laplacian. In particular, this end space is well-behaved as concerns the introduction of traces and normal derivatives.

(iv) Taking into account certain close relationships between quantum graphs and discrete Laplacians (see [27, § 4]), one can easily obtain the results analogous to Theorem4.1 and Theorem6.11 for a particular class of discrete Laplacians on $\mathcal{G}_{d}$ defined by the following expression

$$
(\tau f)(v):=\frac{1}{m(v)} \sum_{u \sim v} \frac{f(v)-f(u)}{\left|e_{u, v}\right|}, \quad v \in \mathcal{V}
$$

where $m$ is the star weight (2.12). Markovian extensions of weighted discrete Laplacians were considered also in [52]. On the other hand, [52] does not contain a finiteness assumption, however, the conclusion in our setting appears to be slightly stronger than in [52, Theorem 3.5], where the correspondence between Markovian extensions and Markovian forms on the boundary is in general not bijective.

## 7. DEficiency indices OF ANTITREES

The main aim of this section is to construct for any $N \in \mathbb{Z}_{\geq 1} \cup\{\infty\}$ a metric antitree such that the corresponding minimal Kirchhoff Laplacian $\mathbf{H}_{0}$ has deficiency indices $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=N$. Our motivation stems from the fact that every antitree has exactly one end and hence, according to considerations in the previous sections, $\mathbf{H}_{0}$ admits at most one-parameter family of Markovian extensions.

7.1. Antitrees. Let $\mathcal{G}_{d}=(\mathcal{V}, \mathcal{E})$ be a connected, simple combinatorial graph. Fix a root vertex $o \in \mathcal{V}$ and then order the graph with respect to the combinatorial spheres $S_{n}, n \geq 0$ (notice that $\left.S_{0}=\{o\}\right) . \mathcal{G}_{d}$ is called an antitree if every vertex in

![](https://cdn.mathpix.com/cropped/2024_05_09_c24bfdaabe9c629d87a0g-34.jpg?height=390&width=534&top_left_y=396&top_left_x=790)

Figure 1. Antitree with sphere numbers $s_{n}=n+1$.

$S_{n}, n \geq 1$, is connected to all vertices in $S_{n-1}$ and $S_{n+1}$ and no vertices in $S_{k}$ for all $|k-n| \neq 1$ (see Figure 11). Notice that each antitree is uniquely determined by its sequence of sphere numbers $\left(s_{n}\right), s_{n}:=\# S_{n}$ for $n \geq 0$.

While antitrees first appeared in connection with random walks [25, 54, 77], they were actively studied from various different perspectives in the last years (see 111 , 22, 56] for quantum graphs and [21, Section 2] for further references).

Let us enumerate the vertices in every combinatorial sphere $S_{n}$ by $\left(v_{i}^{n}\right)_{i=1}^{s_{n}}$ and denote the edge connecting $v_{i}^{n}$ with $v_{j}^{n+1}$ by $e_{i j}^{n}, 1 \leq i \leq s_{n}, 1 \leq j \leq s_{n+1}$. We shall always use $\mathcal{A}$ to denote (metric) antitrees.

It is clear that every (infinite) antitree has exactly one end. By Theorem 4.1 the deficiency indices of the corresponding minimal Kirchhoff Laplacian are at least 1 if $\operatorname{vol}(\mathcal{A})<\infty$. On the other hand, under the additional symmetry assumption that $\mathcal{A}$ is radially symmetric (that is, for each $n \geq 0$, all edges connecting combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length), it is known that the deficiency indices are at most 1 (see [56, Theorem 4.1] and Example 4.11). It turns out that upon removing the symmetry assumption it is possible to construct antitrees such that the corresponding minimal Kirchhoff Laplacian has arbitrary finite or infinite deficiency indices. More precisely, the main aim of this section is to prove the following result.

Theorem 7.1. Let $\mathcal{A}$ be the antitree with sphere numbers $s_{n}=n+1, n \geq 0$ (Figure 11). Then for each $N \in \mathbb{Z}_{\geq 1} \cup\{\infty\}$ there are edge lengths such that the corresponding minimal Kirchhoff Laplacian $\mathbf{H}_{0}$ has the deficiency indices $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=$ $N$.

7.2. Harmonic functions. As it was mentioned already, every harmonic function is uniquely determined by its values at the vertices. On the other hand, $\mathbf{f} \in C(\mathcal{V})$ defines a function $f \in \mathbb{H}(\mathcal{A})$ with $\left.f\right|_{\mathcal{V}}=\mathbf{f}$ if and only if the following conditions are satisfied:

$$
\sum_{j=1}^{s_{n+1}} \frac{f\left(v_{j}^{n+1}\right)-f\left(v_{k}^{n}\right)}{\left|e_{k j}^{n}\right|}+\sum_{i=1}^{s_{n-1}} \frac{f\left(v_{i}^{n-1}\right)-f\left(v_{k}^{n}\right)}{\left|e_{i k}^{n-1}\right|}=0
$$

at each $v_{k}^{n}, 1 \leq k \leq s_{n}$ with $n \geq 0$. We set $s_{-1}:=0$ for notational simplicity and hence the second summand in (7.1) is absent when $n=0$. We can put the above difference equations into the more convenient matrix form. Denote $\mathbf{f}_{n}:=\left.f\right|_{S_{n}}=$
$\left(f\left(v_{i}^{n}\right)\right)_{i=1}^{s_{n}}$ for all $n \in \mathbb{Z}_{\geq 0}$ and introduce matrices

$$
M_{n+1}:=\left(\begin{array}{cccc}
\frac{1}{\left|e_{11}^{n}\right|} & \frac{1}{\left|e_{12}^{n}\right|} & \cdots & \frac{1}{\left|e_{1 s_{n}+1}^{n}\right|} \\
\frac{1}{\left|e_{21}^{n}\right|} & \frac{1}{\left|e_{22}^{n}\right|} & \cdots & \frac{1}{\left|e_{2 s_{n+1}}^{n}\right|} \\
\cdots & \cdots & \cdots & \cdots \\
\frac{1}{\left|e_{s_{n} 1}^{n}\right|} & \frac{1}{\left|e_{s_{n} 2}^{n}\right|} & \cdots & \frac{1}{\left|e_{s_{n} s_{n+1}}^{n}\right|}
\end{array}\right) \in \mathbb{R}^{s_{n} \times s_{n+1}}
$$

and

$$
D_{n}:=\operatorname{diag}\left(d_{k}^{n}\right) \in \mathbb{R}^{s_{n} \times s_{n}}, \quad d_{k}^{n}:=\sum_{j=1}^{s_{n+1}} \frac{1}{\left|e_{k j}^{n}\right|}+\sum_{i=1}^{s_{n-1}} \frac{1}{\left|e_{i k}^{n-1}\right|}
$$

for all $n \in \mathbb{Z}_{\geq 0}$. Notice the following useful identity

$$
d_{1}^{0}=M_{1} \mathbb{1}_{s_{1}}, \quad\left(\begin{array}{c}
d_{1}^{n} \\
\vdots \\
d_{s_{n}}^{n}
\end{array}\right)=D_{n} \mathbb{1}_{s_{n}}=\left(M_{n+1} M_{n}^{*}\right)\binom{\mathbb{1}_{s_{n+1}}}{\mathbb{1}_{s_{n-1}}}, \quad n \geq 1
$$

where $\mathbb{1}_{s_{n}}:=(1, \ldots, 1)^{\top} \in \mathbb{R}^{s_{n}}$. Hence (7.1) can be written as follows

$$
\begin{aligned}
M_{1} \mathbf{f}_{1} & =\sum_{j=1}^{s_{1}} \frac{1}{\left|e_{1 j}^{0}\right|} \mathbf{f}_{0}=d_{1}^{0} \mathbf{f}_{0} \\
M_{n+1} \mathbf{f}_{n+1} & =D_{n} \mathbf{f}_{n}-M_{n}^{*} \mathbf{f}_{n-1}, \quad n \geq 1
\end{aligned}
$$

Since $D_{n}$ is invertible, we get

$$
\mathbf{f}_{n}=D_{n}^{-1}\left(\begin{array}{ll}
M_{n+1} & M_{n}^{*}
\end{array}\right)\binom{\mathbf{f}_{n+1}}{\mathbf{f}_{n-1}}
$$

for all $n \geq 1$. In particular, $\mathbf{f}_{n} \in \operatorname{ran}\left(D_{n}^{-1}\left(M_{n+1} M_{n}^{*}\right)\right)$ for all $n \geq 1$, which implies that the number of linearly independent solutions to the above difference equations (and hence the number of linearly independent harmonic functions) depends on the ranks of the matrices $\left(M_{n+1} M_{n}^{*}\right), n \geq 1$. Let us demonstrate this by considering the following example.

Lemma 7.2. Let $\mathcal{A}$ be a radially symmetric antitree. Then

$$
\mathbb{H}(\mathcal{A})=\operatorname{span}\left\{\mathbb{1}_{\mathcal{G}}\right\}
$$

Proof. Let for each $n \geq 0$, all edges connecting combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length, say $\ell_{n}>0$. Clearly, in this case

$$
\operatorname{ran}\left(M_{n+1}\right)=\operatorname{ran}\left(M_{n}^{*}\right)=\operatorname{span}\left\{\mathbb{1}_{s_{n}}\right\}
$$

for all $n \geq 1$. Moreover, each $D_{n}$ is a scalar multiple of the identity matrix $I_{s_{n}}$ and hence (7.7) implies that $\mathbf{f}_{n}=c_{n} \mathbb{1}_{s_{n}}$ with some $c_{n} \in \mathbb{C}$ for all $n \geq 0$. Plugging this into (7.5) $-(7.6)$, we get

$$
c_{1}=c_{0}, \quad c_{n+1}=c_{n}+\frac{s_{n-1} \ell_{n}}{s_{n+1} \ell_{n-1}}\left(c_{n}-c_{n-1}\right), \quad n \geq 1
$$

Hence $c_{n}=c_{0}=f(o)$ for all $n \geq 0$, which proves the claim.

The latter in particular implies the following statement (cf. [56, Theorem 4.1]).

Corollary 7.3. If $\mathcal{A}$ is a radial antitree with finite total volume, then $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=1$.

Proof. By Corollary 2.11, we only need to show that $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right) \leq 1$. However,

$$
\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\operatorname{dim}(\operatorname{ker}(\mathbf{H})) \leq \operatorname{dim}(\mathbb{H}(\mathcal{A}))=1
$$

7.3. Finite deficiency indices. We restrict our further considerations to a special case of polynomially growing antitrees. Namely, for every $N \in \mathbb{Z}_{\geq 1}$, the antitree $\mathcal{A}_{N}$ has sphere numbers $s_{0}=1$ and $s_{n}:=n+N$ for all $n \in \mathbb{Z}_{\geq 1}$. To define its lengths, pick a sequence of positive numbers $\left(\ell_{n}\right)$ and set

$$
\left|e_{i j}^{n}\right|:= \begin{cases}2 \ell_{n}, & \text { if } 1 \leq i=j \leq N \\ \ell_{n}, & \text { otherwise }\end{cases}
$$

for all $n \in \mathbb{Z}_{\geq 0}$.

Lemma 7.4. If a metric antitree $\mathcal{A}_{N}$ has lengths given by (7.9), then

$$
\operatorname{dim} \mathbb{H}\left(\mathcal{A}_{N}\right)=N+1
$$

Proof. Denoting

$$
B_{n, m}:=\left(\begin{array}{cccc}
1 & 1 & \ldots & 1 \\
1 & 1 & \ldots & 1 \\
\ldots & \ldots & \ldots & \ldots \\
1 & 1 & \ldots & 1
\end{array}\right) \in \mathbb{R}^{n \times m}, \quad B_{n}:=B_{n, n} \in \mathbb{R}^{n \times n}
$$

we get the following block-matrix form of the matrices $M_{n+1}$ :

$$
M_{n+1}=\frac{1}{\ell_{n}}\left(\begin{array}{cc}
B_{N}-\frac{1}{2} I_{N} & B_{N, n+1} \\
B_{n, N} & B_{n, n+1}
\end{array}\right)
$$

for all $n \geq 1$. Taking into account (7.3) and denoting

$$
d_{n}^{1}:=\frac{n+N-3 / 2}{\ell_{n-1}}+\frac{n+N+1 / 2}{\ell_{n}}, \quad d_{n}^{2}:=\frac{n+N-1}{\ell_{n-1}}+\frac{n+N+1}{\ell_{n}}
$$

we get

$$
D_{n}=\left(\begin{array}{cc}
d_{n}^{1} I_{N} & 0 \\
0 & d_{n}^{2} I_{n}
\end{array}\right)
$$

for all $n \geq 2$. Since $M_{1} \in \mathbb{C}^{1 \times(N+1)}$ and

$$
\operatorname{ran}\left(M_{n+1}\right)=\operatorname{ran}\left(M_{n}^{*}\right)=\operatorname{span}\left\{\left.\binom{\mathbf{f}_{N}}{\mathbb{1}_{n}} \right\rvert\, \mathbf{f}_{N} \in \mathbb{C}^{N}\right\}
$$

for all $n \geq 2$, (7.7) implies that every $\mathbf{f}$ solving (7.5)-(7.6) must be of the form

$$
\mathbf{f}_{n}=\binom{\mathbf{f}_{n}^{N}}{c_{n} \mathbb{1}_{n}} \in \mathbb{C}^{N+n}, \quad \mathbf{f}_{n}^{N} \in \mathbb{C}^{N}, \quad c_{n} \in \mathbb{C}
$$

for all $n \geq 1$. Plugging (7.15) into (7.6) and taking into account that

$$
B_{N} \mathbf{f}_{n}^{N}=\overline{\mathbf{f}}_{n}^{N} \mathbb{1}_{N}, \quad \overline{\mathbf{f}}_{n}^{N}:=\left\langle\mathbf{f}_{n}^{N}, \mathbb{1}_{N}\right\rangle=B_{1, N} \mathbf{f}_{n}^{N}
$$

we get after straightforward calculations

$$
\begin{aligned}
\frac{\overline{\mathbf{f}}_{n+1}^{N}+c_{n+1}(n+1)}{\ell_{n}} \mathbb{1}_{N}-\frac{1}{2 \ell_{n}} \mathbf{f}_{n+1}^{N} & =d_{n}^{1} \mathbf{f}_{n}^{N}-\frac{\overline{\mathbf{f}}_{n-1}^{N}+c_{n-1}(n-1)}{\ell_{n-1}} \mathbb{1}_{N}+\frac{1}{2 \ell_{n-1}} \mathbf{f}_{n-1}^{N} \\
\frac{\overline{\mathbf{f}}_{n+1}^{N}+c_{n+1}(n+1)}{\ell_{n}} & =c_{n} d_{n}^{2}-\frac{\overline{\mathbf{f}}_{n-1}^{N}+c_{n-1}(n-1)}{\ell_{n-1}}
\end{aligned}
$$

for all $n \geq 2$. Multiplying (7.17) with $\mathbb{1}_{N}$ and then subtracting (7.16), we end up with

$$
\mathbf{f}_{n+1}^{N}=2 \ell_{n}\left(c_{n} d_{n}^{2} \mathbb{1}_{N}-d_{n}^{1} \mathbf{f}_{n}^{N}\right)-\frac{\ell_{n}}{\ell_{n-1}} \mathbf{f}_{n-1}^{N}, \quad n \geq 2
$$

Next taking the inner product in (7.16) with $\mathbb{1}_{N}$ and then subtracting (7.17) multiplied by $N-1 / 2$, we finally get

$$
c_{n+1}=\frac{\ell_{n}}{n+1}\left(2 d_{n}^{1} \overline{\mathbf{f}}_{n}^{N}-(2 N-1) d_{n}^{2} c_{n}\right)-c_{n-1} \frac{(n-1) \ell_{n}}{(n+1) \ell_{n-1}}, \quad n \geq 2
$$

Taking into account that the value of $f$ at the root $o$ is determined by $\mathbf{f}_{1}$ via

$$
f(o)=\mathbf{f}_{0}=\frac{2 \ell_{0}}{2 N+1} M_{1} \mathbf{f}_{1}
$$

and noting that $\mathbf{f}_{2}^{N}$ and $c_{2}$ are also determined by $\mathbf{f}_{1}$, we conclude that (7.18)-7.19) define $\mathbf{f}$ uniquely once $\mathbf{f}_{1} \in \mathbb{C}^{N+1}$ is given.

Lemma 7.4 immediately implies that $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right) \leq N+1$ if $\operatorname{vol}\left(\mathcal{A}_{N}\right)<\infty$, where $\mathbf{H}_{0}$ is the associated minimal operator. The next result shows that it can happen that $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=N+1$ upon choosing lengths $\ell_{n}$ with a sufficiently fast decay.

Proposition 7.5. Let $\mathcal{A}_{N}$ be the antitree as in Lemma 7.4. If $\left(\ell_{n}\right)$ is decreasing and

$$
\sqrt{\ell_{n}}=\mathcal{O}\left(\frac{1}{(6 \sqrt{N})^{n}(n+N+3)!}\right)
$$

as $n \rightarrow \infty$, then $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=N+1$.

Proof. It is immediate to see that $\operatorname{vol}\left(\mathcal{A}_{N}\right)<\infty$ if (7.21) is satisfied. Next, taking into account (7.9), observe that

$$
m(v)=\sum_{v \in \mathcal{E}_{v}}|e| \leq(n+N) \ell_{n-1}+(n+N+2) \ell_{n} \lesssim n \ell_{n-1}, \quad v \in S_{n}
$$

as $n \rightarrow \infty$. Suppose $f \in \mathbb{H}(\mathcal{A})$ and set $\mathbf{f}=\left.f\right|_{\mathcal{V}}$. Then $\mathbf{f}$ has the form (7.15) and hence

$$
\left\|\mathbf{f}_{n}\right\|^{2}=\sum_{v \in S_{n}}|f(v)|^{2}=\left\|\mathbf{f}_{n}^{N}\right\|^{2}+n\left|c_{n}\right|^{2}
$$

for all $n \geq 1$. This implies the following estimate

$$
\sum_{v \in \mathcal{V}}|f(v)|^{2} m(v)=\sum_{n \geq 0} \sum_{v \in S_{n}}|f(v)|^{2} m(v) \lesssim \sum_{n \geq 1} n^{2} \ell_{n-1}\left(\left\|\mathbf{f}_{n}^{N}\right\|^{2}+\left|c_{n}\right|^{2}\right)
$$

Next, (7.18)-(7.19) can be written as follows

$$
\binom{\mathbf{f}_{n+1}^{N}}{c_{n+1}}=A_{1, n}\binom{\mathbf{f}_{n}^{N}}{c_{n}}+A_{2, n}\binom{\mathbf{f}_{n-1}^{N}}{c_{n-1}}
$$

where the matrices $A_{1, n}, A_{2, n} \in \mathbb{R}^{(N+1) \times(N+1)}$ are given explicitly by

$$
A_{1, n}:=\left(\begin{array}{cc}
-2 \ell_{n} d_{n}^{1} I_{N} & 2 \ell_{n} d_{n}^{2} B_{N, 1} \\
\frac{2 \ell_{n} d_{n}^{1}}{n+1} B_{1, N} & -\frac{(2 N-1) \ell_{n} d_{n}^{2}}{n+1} I_{1}
\end{array}\right), \quad A_{2, n}:=-\frac{\ell_{n}}{\ell_{n-1}}\left(\begin{array}{cc}
I_{N} & 0 \\
0 & \frac{n-1}{n+1} I_{1}
\end{array}\right)
$$

for all $n \geq 2$. Since $\ell_{n-1} \leq \ell_{n}$ and

$$
d_{n}^{1}<d_{n}^{2}=\frac{n+N-1}{\ell_{n-1}}+\frac{n+N+1}{\ell_{n}} \leq \frac{2(n+N)}{\ell_{n}}
$$

for all $n \geq 2$, it is not difficult to get the following rough bounds

$$
\left\|A_{1, n}\right\| \leq 6 \sqrt{N}(n+N), \quad\left\|A_{2, n}\right\|=\frac{\ell_{n}}{\ell_{n-1}} \leq 1
$$

for all $n \geq 2 N$. Denoting

$$
F_{n}:=\binom{\mathbf{f}_{n}^{N}}{c_{n}}, \quad n \geq 1
$$

the recurrence relations (7.18)-7.19) can be written in the following matrix form

$$
\binom{F_{n+1}}{F_{n}}=\left(\begin{array}{cc}
A_{1, n} & A_{2, n} \\
I_{N+1} & 0_{N+1}
\end{array}\right)\binom{F_{n}}{F_{n-1}}=A_{n}\binom{F_{n}}{F_{n-1}}
$$

Taking into account (7.26), we get $\left\|A_{n}\right\| \leq 6 \sqrt{N}(n+N+1)$ for all $n \geq 2 N$, which implies the estimate

$$
\sqrt{\left\|\mathbf{f}_{n}^{N}\right\|^{2}+\left|c_{n}\right|^{2}}=\left\|F_{n}\right\| \leq C \prod_{k=1}^{n-1}\left\|A_{k}\right\| \lesssim(6 \sqrt{N})^{n}(n+N)!
$$

for all $n \geq 2$. Combining this bound with (7.21), it is easy to see that the series on the right hand side in (7.22) converges and hence by Lemma 2.13 we conclude that $\mathbb{H}\left(\mathcal{A}_{N}\right) \subset L^{2}(\mathcal{A})$. Thus $\operatorname{ker}(\mathbf{H})=\mathbb{H}\left(\mathcal{A}_{N}\right)$ and the use of Corollary 2.11 finishes the proof.

7.4. Infinite deficiency indices. Consider the antitree $\mathcal{A}$ with sphere numbers $s_{n}:=n+1, n \geq 0$. Next pick a sequence of positive numbers $\left(\ell_{n}\right)$ and define lengths as follows

$$
\left|e_{i j}^{n}\right|= \begin{cases}2 \ell_{n}, & 1 \leq i=j \leq n+1 \\ \ell_{n}, & \text { otherwise }\end{cases}
$$

for all $n \in \mathbb{Z}_{\geq 0}$. Thus, the corresponding matrix $M_{n+1}$ given by (7.2) has the form

$$
M_{n+1}=\frac{1}{\ell_{n}}\left(B_{n+1}-\frac{1}{2} I_{n+1} \quad B_{n+1,1}\right) \in \mathbb{R}^{(n+1) \times(n+2)}
$$

for all $n \geq 0$. Let us denote this antitree by $\mathcal{A}_{\infty}$.

Lemma 7.6. $\operatorname{dim}\left(\mathbb{H}\left(\mathcal{A}_{\infty}\right)\right)=\infty$.

Proof. Consider the difference equations (7.5)-(7.6). Clearly, the matrix $M_{n+1}$ has the maximal rank $n+1$ for every $n \geq 0$. Taking into account that

$$
\left(B_{n+1}-\frac{1}{2} I_{n+1}\right)^{-1}=\frac{4}{2 n+1} B_{n+1}-2 I_{n+1}=: C_{n}, \quad n \geq 0
$$

(7.6) then reads

$$
\left(I_{n+1} \quad \frac{2}{2 n+1} B_{n+1,1}\right) \mathbf{f}_{n+1}=\ell_{n} C_{n}\left(D_{n} \mathbf{f}_{n}-M_{n}^{*} \mathbf{f}_{n-1}\right)
$$[^7]for all $n \geq 1$. Observe that

$$
\left(\begin{array}{ll}
I_{n+1} & \frac{2}{2 n+1} B_{n+1,1}
\end{array}\right)\left(\begin{array}{c}
f_{1} \\
\vdots \\
f_{n+1} \\
0
\end{array}\right)=\left(\begin{array}{c}
f_{1} \\
\vdots \\
f_{n+1}
\end{array}\right)
$$

and hence for any $\mathbf{f}_{n} \in \mathbb{C}^{n+1}$ and $\mathbf{f}_{n-1} \in \mathbb{C}^{n}$ there always exists a unique $\mathbf{f}_{n+1}=$ $\left(f_{1}, \ldots, f_{n+1}, 0\right)^{\top}$ satisfying (7.31). Now pick a natural number $N$ and define $\mathbf{f}^{N} \in$ $C\left(\mathcal{A}_{\infty}\right)$ by setting $\mathbf{f}_{n}^{N}:=(0, \ldots, 0)^{\top} \in \mathbb{C}^{n+1}$ for all $n \in\{0, \ldots, N\}$,

$$
\mathbf{f}_{N+1}^{N}:=(1, \ldots, 1,-N-1 / 2)^{\top}
$$

and

$$
\mathbf{f}_{n+1}^{N}:=\binom{\ell_{n} C_{n}\left(D_{n} \mathbf{f}_{n}^{N}-M_{n}^{*} \mathbf{f}_{n-1}^{N}\right)}{0} \in \mathbb{C}^{n+2}
$$

for all $n \geq N+1$. Clearly, $\mathbf{f}^{N}$ satisfies (7.5)-(7.6) and hence defines a harmonic function $f^{N} \in \mathbb{H}\left(\mathcal{A}_{\infty}\right)$. Moreover, it is easy to see that $\operatorname{span}\left\{\mathbf{f}^{N}\right\}_{N \geq 1}$ is infinite dimensional, which proves the claim.

Proposition 7.7. Let $\mathbf{H}_{0}$ be the minimal Kirchhoff Laplacian associated with the antitree $\mathcal{A}_{\infty}$. If $\ell_{n}$ is decreasing and

$$
\sqrt{\ell_{n}}=\mathcal{O}\left(\frac{1}{6^{n}(n+3)!}\right)
$$

as $n \rightarrow \infty$, then $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=\infty$.

Proof. Clearly, it suffices to show that every $f^{N}$ constructed in the proof of Lemma 7.6 belongs to $L^{2}(\mathcal{G})$ if $\ell_{n}$ decays as in (7.33). To prove this we shall proceed as in the proof of Proposition [7.5, First, taking into account (7.29), observe that

$$
m(v) \lesssim n \ell_{n-1}, \quad v \in S_{n}
$$

as $n \rightarrow \infty$. Since $\left\|\mathbf{f}_{n}^{N}\right\|^{2}=\sum_{v \in S_{n}}\left|f^{N}(v)\right|^{2}$ for all $n \geq 0$, we get the estimate

$$
\sum_{v \in \mathcal{V}}\left|f^{N}(v)\right|^{2} m(v) \lesssim \sum_{n \geq N+1} \sum_{v \in S_{n}}\left|f^{N}(v)\right|^{2} m(v) \lesssim \sum_{n \geq N+1} n \ell_{n-1}\left\|\mathbf{f}_{n}^{N}\right\|^{2}
$$

Denoting $F_{n}:=\mathbf{f}_{n}^{N}$ for all $n \geq 1$, we can put (7.31) into the matrix form

$$
\binom{F_{n+1}}{F_{n}}=\left(\begin{array}{cc}
A_{1, n} & A_{2, n} \\
I_{n+1} & 0_{n+1, n}
\end{array}\right)\binom{F_{n}}{F_{n-1}}=A_{n}\binom{F_{n}}{F_{n-1}}
$$

for all $n \geq N+1$, where

$$
A_{1, n}:=\binom{\ell_{n} C_{n} D_{n}}{0_{1, n+1}} \in \mathbb{R}^{(n+2) \times(n+1)}, \quad A_{2, n}:=\binom{-\ell_{n} C_{n} M_{n}^{*}}{0_{1, n}} \in \mathbb{R}^{(n+2) \times n}
$$

Now observe that $\left\|C_{n}\right\|=2$ and $\left\|\ell_{n} D_{n}\right\| \leq 2(n+1)$ for all $n \geq 1$. Moreover, $\left\|\ell_{n} M_{n}^{*}\right\| \leq n+1$ for all $n \geq 1$, which immediately implies the following estimate

$$
\left\|A_{n}\right\| \leq \sqrt{\left\|\ell_{n} C_{n} D_{n}\right\|^{2}+1+\left\|\ell_{n} C_{n} M_{n}^{*}\right\|^{2}} \leq 6(n+1), \quad n \geq N+1
$$

Hence we get

$$
\left\|\mathbf{f}_{n+1}^{N}\right\| \leq C \prod_{k=N+1}^{n}\left\|A_{k}\right\| \leq C 6^{n-N} \frac{(n+1)!}{(N+1)!} \lesssim 6^{n}(n+1)!
$$

for all $n \geq N+1$. Combining this estimate with (7.34) and (7.33) and using Lemma 2.13, we conclude that $f^{N} \in L^{2}\left(\mathcal{A}_{\infty}\right)$ for each $N \geq 1$.

Remark 7.8. It is not difficult to show that $f^{N}$ does not belong to $H^{1}\left(\mathcal{A}_{\infty}\right)$ for the above choices of edge lengths. In fact, it follows from the maximum principle for $\mathbb{H}(\mathcal{A})$ that if $\operatorname{vol}(\mathcal{A})<\infty$, then $\mathbb{H}(\mathcal{A}) \cap H^{1}(\mathcal{A})$ consists only of constant functions.

7.5. Proof of Theorem 7.1, Clearly, the case of infinite deficiency indices follows from Proposition 7.7. On the other hand, since adding and/or removing finitely many edges and vertices to a graph does not change the deficiency indices of the minimal Kirchhoff Laplacian, Proposition 7.5 completes the proof of Theorem 7.1 . Indeed, every antitree $\mathcal{A}_{N}$ can be obtained from $\mathcal{A}$ by first removing all the edges between combinatorial spheres $S_{0}$ and $S_{N}$ and then adding $N+1$ edges connecting the root $o$ with the vertices in $S_{N}$.

Remark 7.9. Since every infinite antitree has exactly one end, Theorem 6.11(iv) implies that the Kirchhoff Laplacian $\mathbf{H}_{0}$ in Theorem 7.1 has a unique Markovian extension exactly when $\operatorname{vol}(\mathcal{A})=\infty$. If $\operatorname{vol}(\mathcal{A})<\infty$, then Markovian extensions of $\mathbf{H}_{0}$ form a one-parameter family explicitly given by (6.17). Notice that (6.17) looks similar to the description of self-adjoint extensions of the minimal Kirchhoff Laplacian on radially symmetric antitrees obtained recently in 56 .

Let us also emphasize that the antitree constructed in Proposition 7.7 has finite total volume and $\mathbf{H}_{0}$ has infinite deficiency indices, however, the set of Markovian extensions of $\mathbf{H}_{0}$ forms a one-parameter family.

Let us finish this section with one more comment. As it was proved, the dimension of the space of Markovian extensions depends only on the space of graph ends and, moreover, it is equal to the number of finite volume ends. However, deficiency indices (dimension of the space of self-adjoint extensions) are in general independent of graph ends and we can only provide a lower bound. Moreover, the above example of a polynomially growing antitree shows that the space of non-constant harmonic functions heavily depends on the choice of edge lengths (in particular, its dimension may vary between zero and infinity). In this respect let us also emphasize that in the case of Cayley graphs of finitely generated groups the end space is independent of the choice of a generating set, however, simple examples show that the space of harmonic functions does depend on this choice.

## Appendix A. Linear relations in Hilbert spaces

In this section we collect basic notions and facts on linear relations in Hilbert spaces, a very convenient concept of multi-valued linear operators. For simplicity, we shall assume that $\mathcal{H}$ is a finite dimensional Hilbert space, $N:=\operatorname{dim}(\mathcal{H})<\infty$.

A linear relation $\Theta$ in $\mathcal{H}$ is a linear subspace in $\mathcal{H} \times \mathcal{H}$. Linear operators become special linear relations (single valued) after identifying them with their graphs in $\mathcal{H} \times \mathcal{H}$. Consider linear relations in $\mathcal{H}$ having the form

$$
\Theta_{C, D}=\{(f, g) \in \mathcal{H} \times \mathcal{H} \mid C f=D g\}
$$

where $C, D$ are linear operators on $\mathcal{H}$. Notice that different $C$ and $D$ may define the same linear relation. The domain and the multi-valued part of $\Theta_{C, D}$ are given
by

$$
\begin{aligned}
\operatorname{dom}\left(\Theta_{C, D}\right) & =\{f \in \mathcal{H} \mid \exists g \in \mathcal{H}, C f=D g\}=\{f \in \mathcal{H} \mid C f \in \operatorname{ran}(D)\} \\
\operatorname{mul}\left(\Theta_{C, D}\right) & =\{g \in \mathcal{H} \mid D g=0\}=\operatorname{ker}(D)
\end{aligned}
$$

In particular, $\Theta_{C, D}$ is a graph of a linear operator only if $\operatorname{ker}(D)=\{0\}$.

The adjoint relation $\Theta_{C, D}^{*}$ to $\Theta_{C, D}$ is given by

$$
\begin{aligned}
\Theta_{C, D}^{*} & =\left\{(f, g) \in \mathcal{H} \times \mathcal{H} \mid\langle\widetilde{g}, f\rangle_{\mathcal{H}}=\langle\widetilde{f}, g\rangle_{\mathcal{H}} \forall(\widetilde{f}, \widetilde{g}) \in \Theta_{C, D}\right\} \\
& =\left\{\left(D^{*} f, C^{*} f\right) \mid f \in \mathcal{H}\right\}
\end{aligned}
$$

Thus, a linear relation $\Theta_{C, D}$ is self-adjoint, $\Theta_{C, D}=\Theta_{C, D}^{*}$, if and only if $C$ and $D$ satisfy the Rofe-Beketov conditions [68] (see also [69, Exercises 14.9.3-4]):

$$
C D^{*}=D C^{*}, \quad 0 \in \rho\left(C^{*} C+D^{*} D\right)
$$

Taking into account that every linear relation in $\mathcal{H}$ admits one of the forms (A.1) or (A.2), this provides a description of self-adjoint linear relations in $\mathcal{H}$. Notice also that the second condition in (A.3) is equivalent to the fact that the matrix $(C \mid D) \in \mathbb{C}^{N \times 2 N}$ has the maximal rank $N$.

Recall also that every self-adjoint linear relation admits the representation $\Theta=$ $\Theta_{\mathrm{op}} \oplus \Theta_{\mathrm{mul}}$, where $\Theta_{\mathrm{mul}}:=\{0\} \times \operatorname{mul}(\Theta)$ and $\Theta_{\mathrm{op}}$, called the operator part of $\Theta$, is a graph of a linear operator. In particular, for a self-adjoint linear relation $\Theta_{C, D}$ one has

$$
\operatorname{dom}\left(\Theta_{C, D}\right)=\operatorname{mul}\left(\Theta_{C, D}\right)^{\perp}=\operatorname{ker}(D)^{\perp}=\operatorname{ran}\left(D^{*}\right)
$$

For further details on linear relations we refer the reader to, e.g., [69, Chapter 14.1].

## Appendix B. A ROPE LadDER GRAPh

Let us introduce a rope ladder graph depicted on Figure 2, Let $\mathcal{G}_{d}=(\mathcal{V}, \mathcal{E})$ be a simple graph with the vertex set $\mathcal{V}:=\{o\} \cup \mathcal{V}^{+} \cup \mathcal{V}^{-}$, where $o=v_{0}$ is a root, $\mathcal{V}^{+}=\left(v_{n}^{+}\right)_{n \geq 1}$ and $\mathcal{V}^{-}=\left(v_{n}^{-}\right)_{n \geq 1}$ are two disjoint countably infinite sets of vertices. The edge set $\mathcal{E}$ is defined as follows:

- $o$ is connected to $v_{1}^{+}$and $v_{1}^{-}$by the "diagonal" edges $e_{0}^{+}$and $e_{0}^{-}$, respectively;
- for each $n \geq 1, v_{n}^{ \pm}$is connected to $v_{n+1}^{ \pm}$by the vertical edge $e_{n}^{ \pm}$;
- for each $n \geq 1, v_{n}^{+}$and $v_{n}^{-}$are connected by the horizontal edge $e_{n}$.

![](https://cdn.mathpix.com/cropped/2024_05_09_c24bfdaabe9c629d87a0g-41.jpg?height=439&width=620&top_left_y=1884&top_left_x=747)

Figure 2. The rope ladder graph.

By construction, $\operatorname{deg}(o)=2$ and $\operatorname{deg}\left(v_{n}^{+}\right)=\operatorname{deg}\left(v_{n}^{-}\right)=3$ for all $n \geq 1$. Moreover, an infinite rope ladder graph has exactly one end. Notice also that a similar example was studied in [46, Section 7] (see also [33, § 5]) in context with the construction of non-constant harmonic functions of finite energy.

Equip now $\mathcal{G}_{d}$ with edge lengths $|\cdot|: \mathcal{E} \rightarrow(0, \infty)$ and consider the corresponding minimal Kirchhoff Laplacian $\mathbf{H}_{0}$ on the metric graph $\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$. The next result immediately follows from Theorem 2.8 and Corollary 2.11 .

Corollary B.1. If

$$
\sum_{n \geq 1}\left|e_{n}^{+}\right|+\left|e_{n}\right|=\infty, \quad \text { and } \quad \sum_{n \geq 1}\left|e_{n}^{-}\right|+\left|e_{n}\right|=\infty
$$

then the Kirchhoff Laplacian $\mathbf{H}_{0}$ is self-adjoint. If

$$
\operatorname{vol}(\mathcal{G})=\sum_{n \geq 1}\left|e_{n}^{+}\right|+\left|e_{n}^{-}\right|+\left|e_{n}\right|<\infty
$$

then $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right) \geq 1$.

We omit the proof since it is easy to check that the first condition is equivalent to the geodesic completeness of $\left(\mathcal{V}, \varrho_{m}\right)$ (cf. Theorem 2.8). Due to the symmetry of the underlying combinatorial graph, the gap between the above two conditions is equivalent to the fact that the corresponding lengths satisfy

$$
\sum_{n \geq 1}\left|e_{n}^{+}\right|=\infty, \quad \sum_{n \geq 1}\left|e_{n}^{-}\right|+\left|e_{n}\right|<\infty
$$

Next, let us describe the space of harmonic functions $\mathbb{H}(\mathcal{G})$.

Lemma B.2. Let $a, b \in \mathbb{C}$. Then there is exactly one $f \in \mathbb{H}(\mathcal{G})$ such that

$$
f\left(v_{1}^{+}\right)=a, \quad f\left(v_{1}^{-}\right)=b
$$

Moreover, this function $f$ is recursively given by

$$
f(o)=\frac{b\left|e_{0}^{+}\right|+a\left|e_{0}^{-}\right|}{\left|e_{0}^{+}\right|+\left|e_{0}^{-}\right|}
$$

and

$$
f\left(v_{n+1}^{ \pm}\right)=\left(1+\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n-1}^{ \pm}\right|}+\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n}\right|}\right) f\left(v_{n}^{ \pm}\right)-\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n-1}^{ \pm}\right|} f\left(v_{n-1}^{ \pm}\right)-\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n}\right|} f\left(v_{n}^{\mp}\right)
$$

for all $n \in \mathbb{Z}_{\geq 1}$, where we use the notation $v_{0}^{+}:=v_{0}^{-}:=0$.

Proof. Suppose $a, b \in \mathbb{C}$ are given and $f \in \mathbb{H}(\mathcal{G})$ satisfies (B.4). Since $f$ is linear on every edge and satisfies (2.7) at $v=o$, we get

$$
0=f_{e_{0}^{+}}^{\prime}(o)+f_{e_{0}^{-}}^{\prime}(o)=\frac{f\left(v_{1}^{+}\right)-f(o)}{\left|e_{0}^{+}\right|}+\frac{f\left(v_{1}^{-}\right)-f(o)}{\left|e_{0}^{-}\right|}=\frac{a-f(o)}{\left|e_{0}^{+}\right|}+\frac{b-f(o)}{\left|e_{0}^{-}\right|}
$$

which implies (B.5). Moreover, Kirchhoff conditions (2.7) at $v=v_{n}^{ \pm}, n \geq 1 \mathrm{read}$

$$
\frac{f\left(v_{n+1}^{ \pm}\right)-f\left(v_{n}^{ \pm}\right)}{\left|e_{n}^{ \pm}\right|}+\frac{f\left(v_{n-1}^{ \pm}\right)-f\left(v_{n}^{ \pm}\right)}{\left|e_{n-1}^{ \pm}\right|}+\frac{f\left(v_{n}^{\mp}\right)-f\left(v_{n}^{ \pm}\right)}{\left|e_{n}\right|}=0
$$

This implies that $f$ is given by (B.6). Hence there is at most one $f \in \mathbb{H}(\mathcal{G})$ satisfying (B.4) for given $a, b \in \mathbb{C}$. However, the same calculation shows that $f$ defined by (B.5) and (B.6) has this property. Thus, existence follows as well.

From Lemma B.2, it is clear that $\operatorname{dim}(\mathbb{H}(\mathcal{G}))=2$, and, moreover,

$$
\mathbb{H}(\mathcal{G})=\operatorname{span}\left\{\mathbb{1}_{\mathcal{G}}, g_{0}\right\}
$$

where $\mathbb{1}_{\mathcal{G}}$ denotes the constant function on $\mathcal{G}$ and $g_{0} \in \mathbb{H}(\mathcal{G})$ is the function defined, for example, by the following normalization

$$
g_{0}(0)=0, \quad g_{0}\left(v_{1}^{+}\right)=\left|e_{0}^{+}\right|, \quad g_{0}\left(v_{1}^{-}\right)=-\left|e_{0}^{-}\right|
$$

Notice that $g_{0}\left(v_{n}^{ \pm}\right), n \geq 1$ are then given recursively by (B.6).

Lemma B.3. If $\operatorname{vol}(\mathcal{G})<\infty$, then

$$
\mathbb{H}(\mathcal{G}) \cap H^{1}(\mathcal{G})=\operatorname{span}\left\{\mathbb{1}_{\mathcal{G}}\right\}
$$

The claim immediately follows from the fact that a rope ladder graph has exactly one end. However, let us present a direct proof based on the analysis of harmonic functions.

Proof. Taking into account (B.8), we only need to show that $g_{0} \notin H^{1}(\mathcal{G})$. First, observe that $\left(g_{0}\left(v_{n}^{+}\right)\right)_{n \geq 1}$ and $\left(g_{0}\left(v_{n}^{-}\right)\right)_{n \geq 1}$ are strictly increasing positive, respectively, strictly decreasing negative sequences. Indeed,

$$
-\left|e_{0}^{-}\right|=g_{0}\left(v_{1}^{-}\right)<0=g_{0}(o)<g_{0}\left(v_{1}^{+}\right)=\left|e_{0}^{+}\right|
$$

by the very definition of $g_{0}$. Let $n \geq 1$ and assume now that we have already shown that $\left(g_{0}\left(v_{k}^{+}\right)\right)_{k=1}^{n}$ is strictly increasing and $\left(g_{0}\left(v_{k}^{-}\right)\right)_{k=1}^{n}$ is strictly decreasing. Since $g_{0}(o)=0,($ B.6) implies

$$
\begin{aligned}
g_{0}\left(v_{n+1}^{+}\right) & =\left(1+\frac{\left|e_{n}^{+}\right|}{\left|e_{n-1}^{+}\right|}+\frac{\left|e_{n}^{+}\right|}{\left|e_{n}\right|}\right) g_{0}\left(v_{n}^{+}\right)-\frac{\left|e_{n}^{+}\right|}{\left|e_{n-1}^{+}\right|} g_{0}\left(v_{n-1}^{+}\right)-\frac{\left|e_{n}^{+}\right|}{\left|e_{n}\right|} g_{0}\left(v_{n}^{-}\right) \\
& >\left(1+\frac{\left|e_{n}^{+}\right|}{\left|e_{n}\right|}\right) g_{0}\left(v_{n}^{+}\right)+\frac{\left|e_{n}^{+}\right|}{\left|e_{n-1}^{+}\right|}\left(g_{0}\left(v_{n}^{+}\right)-g_{0}\left(v_{n-1}^{+}\right)\right)>g_{0}\left(v_{n}^{+}\right)
\end{aligned}
$$

A similar argument shows that $g_{0}\left(v_{n+1}^{-}\right)<g_{0}\left(v_{n}^{-}\right)$and hence the claim follows by induction. Now monotonicity immediately implies

$$
\begin{aligned}
\left\|g_{0}^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2} & =\sum_{e \in \mathcal{E}} \int_{e}\left|g_{0}^{\prime}\left(x_{e}\right)\right|^{2} d x_{e} \geq \sum_{n \geq 0} \int_{e_{n}}\left|g_{0}^{\prime}\left(x_{e}\right)\right|^{2} d x_{e} \\
& =\sum_{n=0}^{\infty} \frac{\left|g_{0}\left(v_{n}^{+}\right)-g_{0}\left(v_{n}^{-}\right)\right|^{2}}{\left|e_{n}\right|} \geq\left|g_{0}\left(v_{1}^{+}\right)-g_{0}\left(v_{1}^{-}\right)\right|^{2} \sum_{n=0}^{\infty} \frac{1}{\left|e_{n}\right|}=\infty
\end{aligned}
$$

since $\operatorname{vol}(\mathcal{G})<\infty$. Thus $g_{0} \notin H^{1}(\mathcal{G})$.

In particular, this also leads to the following result:

Corollary B.4. If $\operatorname{vol}(\mathcal{G})<\infty$, then $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right) \in\{1,2\}$. Moreover, $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=1$ if and only if $g_{0} \notin L^{2}(\mathcal{G})$.

Proof. The claim about the deficiency indices follows from Corollary 2.11 and the fact that $\mathbb{1}_{\mathcal{G}} \in L^{2}(\mathcal{G})$. The equivalences then follow from Lemma B. 3

As the next example shows, the inclusion $g_{0} \in L^{2}(\mathcal{G})$ heavily depends on the choice of edge lengths.

Example B.5. Fix $s>3$ and equip the rope ladder graph with edge lengths

$$
\left|e_{n}^{+}\right|=\left|e_{n}^{-}\right|:=\frac{1}{(n+1)^{s}}, \quad\left|e_{n}\right|:=\frac{2 n}{(n+1)^{s}-n^{s}}, \quad n \in \mathbb{Z}_{\geq 0}
$$

Then $\left|e_{n}\right| \sim n^{2-s}$ for large $n$ and hence $\operatorname{vol}(\mathcal{G})<\infty$. Moreover, for this particular choice of edge lengths we have $g_{0}\left(v_{n}^{ \pm}\right)= \pm n$ for all $n \geq 1$. Indeed, $g_{0}\left(v_{1}^{ \pm}\right)= \pm 1$ by (B.7). Assuming we have already proven that $g_{0}\left(v_{k}^{ \pm}\right)= \pm k$ for $k \leq n$ with some $n \geq 1$, we have by ( $\overline{\text { B. } 6})$ :

$$
\begin{aligned}
g_{0}\left(v_{n+1}^{+}\right) & =\left(1+\frac{n^{s}}{(n+1)^{s}}+\frac{1}{(n+1)^{s}\left|e_{n}\right|}\right) n-\frac{n^{s}(n-1)}{(n+1)^{s}}+\frac{n}{(n+1)^{s}\left|e_{n}\right|} \\
& =n+\frac{n^{s}}{(n+1)^{s}}+\frac{2 n}{(n+1)^{s}\left|e_{n}\right|}=n+\frac{n^{s}}{(n+1)^{s}}+\frac{(n+1)^{s}-n^{s}}{(n+1)^{s}}=n+1
\end{aligned}
$$

Analogously, $g_{0}\left(v_{n+1}^{-}\right)=-(n+1)$ and hence the claim follows by induction.

Applying Lemma B. 3 and using again that $\left|e_{n}\right| \sim n^{2-s}$ as $n \rightarrow \infty$, we conclude that $g_{0} \in L^{2}(\mathcal{G})$ exactly (see Lemma [2.13) when

$$
\sum_{n \geq 1}\left|g_{0}\left(v_{n}^{ \pm}\right)\right|^{2}\left(\left|e_{n-1}^{ \pm}\right|+\left|e_{n}^{ \pm}\right|\right)=\sum_{n \geq 1} n^{2}\left((n+1)^{-s}+n^{-s}\right)<\infty
$$

and

$$
\sum_{n \geq 1}\left|g_{0}\left(v_{n}^{ \pm}\right)\right|^{2}\left|e_{n-1}\right|=\sum_{n \geq 1} \frac{2 n^{3}}{(n+1)^{s}-n^{s}}<\infty
$$

Clearly, the latter holds only if $s>5$. Hence, by Lemma B.4, $\mathrm{n}_{ \pm}\left(\mathbf{H}_{0}\right)=2$ for all $s>5$. In particular, $\operatorname{ker}(\mathbf{H}) \subset H^{1}(\mathcal{G}) \Leftrightarrow s \leq 5$.

## ACKNOWLEDGMENTS

We thank Matthias Keller, Daniel Lenz, Primož Moravec, Andrea Posilicano and Wolfgang Woess for useful discussions and hints with respect to the literature. We also thank the referees for their comments which have helped us to improve the manuscript. N.N. appreciates the hospitality at the Institute of Mathematics, University of Potsdam, during a research stay funded by the OeAD (Marietta Blaugrant, ICM-2019-13386), where a part of this work was done.

## REFERENCES

[1] N. I. Akhiezer and I. M. Glazman, Theory of Linear Operators in Hilbert Spaces. Vol. II, Dover Publ., New York, 1993.

[2] O. Amini and L. Caporaso, Riemann-Roch theory for weighted graphs and tropical curves, Adv. Math. 240, 1-23 (2013).

[3] W. Arendt and A. F. M. ter Elst, Operators with continuous kernels, Integr. Equ. Oper. Theory 91, no. 5, Art. 45 (2019).

[4] W. Arendt and A. V. Bukhvalov, Integral representations of resolvents and semigroups, Forum. Math. 6, 111-135 (1994).

[5] M. Baker and S. Norine, Riemann-Roch and Abel-Jacobi theory on a finite graph, Adv. Math. 215, no. 2, 766-788 (2007).

[6] M. Baker and R. Rumely, Potential Theory and Dynamics on the Berkovich Projective Line, Math. Surv. Monographs, 159. Amer. Math. Soc., Providence, RI, 2010.

[7] M. T. Barlow and R. F. Bass, Stability of parabolic Harnack inequalities, Trans. Amer. Math. Soc. 356, no. 4, 1501-1533 (2004).

[8] G. Berkolaiko, R. Carlson, S. Fulling, and P. Kuchment, Quantum Graphs and Their Applications, Contemp. Math. 415, Amer. Math. Soc., Providence, RI, 2006.

[9] G. Berkolaiko and P. Kuchment, Introduction to Quantum Graphs, Amer. Math. Soc., Providence, RI, 2013.

[10] J. Breuer and M. Keller, Spectral analysis of certain spherically homogeneous graphs, Oper. Matrices 7, no. 4, 825-847 (2013).

[11] J. Breuer and N. Levi, On the decomposition of the Laplacian on metric graphs, Ann. Henri Poincaré 22, no. 2, 499-537 (2020).

[12] H. Brezis, Functional Analysis, Sobolev Spaces and Partial Differential Equations, Universitext, Springer, New York, 2011.

[13] D. Burago, Yu. Burago, and S. Ivanov, A Course in Metric Geometry, Graduate Stud. Math. 33, Amer. Math. Soc., Providence, RI, 2001.

[14] S. Cardanobile and D. Mugnolo, Parabolic systems with coupled boundary conditions, J. Differential Equations 247, 1229-1248 (2009).

[15] R. Carlson, Nonclassical Sturm-Liouville problems and Schrödinger operators on radial trees, Electr. J. Differential Equations 2000, no. 71, pp. 1-24 (2000).

[16] R. Carlson, Boundary value problems for infinite metric graphs, in [26].

[17] R. Carlson, Dirichlet to Neumann maps for infinite quantum graphs, Netw. Heterog. Media 7, no. 3, 483-501 (2012).

[18] D. I. Cartwright, P. M. Soardi, and W. Woess, Martin and end compactifications for nonlocally finite graphs, Trans. Amer. Math. Soc. 338, no 2, 679-693 (1993).

[19] Y. Colin de Verdière, N. Torki-Hamza, and F. Truc, Essential self-adjointness for combinatorial Schrödinger operators II-metrically non complete graphs, Math. Phys. Anal. Geom. 14, no. 1, 21-38 (2011).

[20] T. Coulhon, Off-diagonal heat kernel lower bounds without Poincaré, J. London Math. Soc. (2) $68,795-816(2003)$.

[21] D. Cushing, S. Liu, F. Münch, and N. Peyerimhoff, Curvature calculations for antitrees, in: M. Keller et. al. (Eds.), "Analysis and Geometry on Graphs and Manifolds", London Math. Soc. Lect. Notes Ser. 461, Cambridge Univ. Press, 2020.

[22] D. Damanik, L. Fang, and S. Sukhtaiev, Zero measure and singular continuous spectra for quantum graphs, Ann. Henri Poincaré 21, no. 7, 2167-2191 (2020).

[23] R. Diestel, Graph Theory, 5th edn., Grad. Texts in Math. 173, Springer-Verlag, Heidelberg, New York, 2017.

[24] R. Diestel and D. Kühn, Graph-theoretical versus topological ends of graphs, J. Combin. Theory, Ser. B 87, 197-206 (2003).

[25] J. Dodziuk and L. Karp, Spectral and function theory for combinatorial Laplacians, in: "Geometry of Random Motion" (Ithaca, N.Y., 1987), Contemp. Math. 73, Amer. Math. Soc., Providence, pp. 25-40 (1988).

[26] P. Exner, J. P. Keating, P. Kuchment, T. Sunada, and A. Teplyaev, Analysis on Graphs and Its Applications, Proc. Symp. Pure Math. 77, Providence, RI, Amer. Math. Soc., 2008.

[27] P. Exner, A. Kostenko, M. Malamud, and H. Neidhardt, Spectral theory of infinite quantum graphs, Ann. Henri Poincaré 19, no. 11, 3457-3510 (2018).

[28] M. Folz, Volume growth and stochastic completeness of graphs, Trans. Amer. Math. Soc. 366, 2089-2119 (2014).

[29] H. Freudenthal, Über die Enden topologischer Räume und Gruppen, Math. Z. 33, 692-713 $(1931)$.

[30] H. Freudenthal, Über die Enden diskreter Räume und Gruppen, Comment. Math. Helv. 17, 1-38 (1944).

[31] M. Fukushima, Y. Oshima, and M. Takeda, Dirichlet Forms and Symmetric Markov Processes, 2nd edn., De Gruyter, 2010.

[32] R. Geoghegan, Topological Methods in Group Theory, Grad. Texts in Math. 243, Springer, 2008.

[33] A. Georgakopoulos, Uniqueness of electrical currents in a network of finite total resistance, J. London Math. Soc. 82, 256-272 (2010).

[34] A. Georgakopoulos, Graph topologies induced by edge lengths, Discrete Math. 311, no. 15, $1523-1542(2011)$.

[35] A. Georgakopoulos, S. Haeseler, M. Keller, D. Lenz, and R. Wojciechowski, Graphs of finite measure, J. Math. Pures Appl. 103, S1093-S1131 (2015).

[36] G. Golub and C. F. Van Loan, Matrix Computations, 4th edn., The Johns Hopkins University Press, Baltimore, 2012.

[37] A. Grigor'yan and J. Masamune, Parabolicity and stochastic completeness of manifolds in terms of the Green formula, J. Math. Pures Appl. 100, 607-632 (2013).

[38] R. Halin, Über unendliche Wege in Graphen, Math. Ann. 157, 125-137 (1964).

[39] S. Haeseler, M. Keller, D. Lenz, and R. Wojciechowski, Laplacians on infinite graphs: Dirichlet and Neumann boundary conditions, J. Spectr. Theory 2, no. 4, 397-432 (2012).

[40] S. Haeseler, Analysis of Dirichlet forms on graphs, PhD thesis, Jena, 2014; arXiv: $1705.06322(2017)$.

[41] M. Hinz and M. Schwarz, A note on Neumann problems on graphs, preprint, arXiv:1803.08559 (2018).

[42] H. Hopf, Enden offener Räume und unendliche diskontinuierliche Gruppen, Comment. Math. Helv. 16, 81-100 (1943).

[43] B. Hua, Liouville theorem for bounded harmonic functions on manifolds and graphs satisfying non-negative curvature dimension condition, Calc. Var. Partial Differential Equations 58, no. 2, Art. 42 (2019).

[44] B. Hua and M. Keller, Harmonic functions of general graph Laplacians, Calc. Var. Partial Differential Equations 51, 343-362 (2014).

[45] X. Huang, M. Keller, J. Masamune, and R. Wojciechowski, A note on self-adjoint extensions of the Laplacian on weighted graphs, J. Funct. Anal. 265, 1556-1578 (2013).

[46] P. Jorgensen and E. Pearse, Gel'fand triples and boundaries of infinite networks, New York J. Math. 17, 745-781 (2011).

[47] U. Kant, T. Klauß, J. Voigt, and M. Weber, Dirichlet forms for singular one-dimensional operators and on graphs, J. Evol. Equ. 9, 637-659 (5009).

[48] A. Kasue, Convergence of metric graphs and energy forms, Rev. Mat. Iberoam. 26, no. 2, $367-448(2010)$.

[49] A. Kasue, Convergence of Dirichlet forms induced on boundaries of transient networks, Potential Anal. 47, no. 2, 189-233 (2017).

[50] T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer-Verlag, Berlin-New York, 1976.

[51] M. Keller and D. Lenz, Dirichlet forms and stochastic completeness of graphs and subgraphs, J. reine angew. Math. 666, 189-223 (2012).

[52] M. Keller, D. Lenz, M. Schmidt, and M. Schwarz, Boundary representation of Dirichlet forms on discrete spaces, J. Math. Pures Appl. 126, 109-143 (2019).

[53] M. Keller, D. Lenz, M. Schmidt, and R. K. Wojciechowski, Note on uniformly transient graphs, Rev. Mat. Iberoam. 33, no. 3, 831-860 (2017).

[54] M. Keller, D. Lenz, and R. K. Wojciechowski, Volume growth, spectrum and stochastic completeness of infinite graphs, Math. Z. 274, no. 3-4, 905-932 (2013).

[55] A. Kostenko and N. Nicolussi, Spectral estimates for infinite quantum graphs, Calc. Var. Partial Differential Equations 58, no. 1, Art. 15 (2019).

[56] A. Kostenko and N. Nicolussi, Quantum graphs on radially symmetric antitrees, J. Spectral Theory 11, no. 2, 411-460 (2021).

[57] V. Kostrykin, J. Potthoff, and R. Schrader, Contraction semigroups on metric graphs, in 26 .

[58] T. Lupu, From loop clusters and random interlacements to the free field, Ann. Probab. 44, 2117-2146 (2016).

[59] T. Lupu, Convergence of the two-dimensional random walk loop-soup clusters to CLE, J. Eur. Math. Soc. 21, 1201-1227 (2019).

[60] J. T. Marti, Evaluation of the least constant in Sobolev's inequality for $H^{1}(0, s)$, SIAM J. Numer. Anal. 20, 1239-1242 (1983).

[61] J. Masamune, Essential self-adjointness of Laplacians on Riemannian manifolds with fractal boundary, Commun. Partial Diff. Equ. 24, no. 3-4, 749-757 (1999).

[62] J. Masamune, Analysis of the Laplacian of an incomplete manifold with almost polar boundary, Rend. Mat. Appl. (7) 25, no. 1, 109-126 (2005).

[63] D. Mugnolo and R. Nittka, Properties of representations of operators acting between spaces of vector-valued functions, Positivity 15, 135-154 (2011).

[64] A. Murakami and M. Yamasaki, An introduction of Kuramochi boundary of an infinite network, Mem. Fac. Sci. Eng. Shimane Univ. Ser. B Math. Sci. 30, 57-89, 1997.

[65] N. Nicolussi, Strong isoperimetric inequality for tessellating quantum graphs, in: F. Fatihcan et. al. (Eds.), "Discrete and Continuous Models in the Theory of Networks", 271-290, Oper. Theory: Adv. Appl. 64, Birkhäuser, Basel, 2020.

[66] E. M. Ouhabaz, Analysis of Heat Equations on Domains, Princeton Univ. Press, Princeton and Oxford, 2005.

[67] O. Post, Spectral Analysis on Graph-Like Spaces, Lect. Notes in Math. 2039, SpringerVerlag, Berlin, Heidelberg, 2012

[68] F. S. Rofe-Beketov, Self-adjoint extensions of differential operators in a space of vectorvalued functions, Teor. Funkcii, Funkcional. Anal. i Priložen. 8, 3-24 (1969). (in Russian)

[69] K. Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space, Grad. Texts in Math. 265, Springer, Berlin, 2012.

[70] F. Shokrieh and C. Wu, Canonical measures on metric graphs and a Kazhdan's theorem, Invent. Math. 215, 819-862 (2019).

[71] P. M. Soardi, Potential Theory on Infinite Networks, Lect. Notes Math. 1590, Springer, Berlin, 1994

[72] M. Solomyak, On the spectrum of the Laplacian on regular metric trees, Waves Random Media 14, S155-S171 (2004).

[73] J. R. Stallings, Group Theory and Three-Dimensional Manifolds, Yale Univ. Press, New Haven, Connecticut, 1971.

[74] K.-T. Sturm, Analysis on local Dirichlet spaces I. Recurrence, conservativeness and $L^{p}$ Liouville properties, J. reine angew. Math. 456, 173-196 (1994).

[75] C. T. C. Wall, Poincaré complexes: I, Ann. of Math. 86, no. 2, 213-245 (1967).

[76] W. Woess, Random Walks on Infinite Graphs and Groups, Cambridge Univ. Press, Cambridge, 2000

[77] R. K. Wojciechowski, Stochastically incomplete manifolds and graphs, in: D. Lenz et al. (Eds.), "Random Walks, Boundaries and Spectra", 163-179, Progr. Probab. 64, Birkhäuser/Springer Basel AG, Basel, 2011.

Faculty of Mathematics and Physics, University of Ljubljana, Jadranska ul. 19, 1000 Ljubljana, Slovenia, and Institute for Analysis and Scientific Computing, Vienna University of Technology, Wiedner HauptStRASSe 8-10/101, 1040 VienNa, AUStria

Current address: Faculty of Mathematics and Physics, University of Ljubljana, Jadranska ul. 19, 1000 Ljubljana, Slovenia, and Faculty of Mathematics, University of Vienna, Oskar-MorgensternPlatz 1, 1090 Vienna, Austria

Email address: Aleksey.Kostenko@fmf.uni-lj.si

Lehrgebiet Analysis, Fakultät Mathematik und Informatik, FernUniversität in HaGen, Hagen, Germany

Email address: delio.mugnolo@fernuni-hagen.de

Faculty of Mathematics, University of Vienna, Oskar-Morgenstern-Platz 1, 1090 VIENNA, AUSTRIA

Email address: noema.nicolussi@univie.ac.at


[^0]:    ${ }^{\dagger}$ Equivalently, $\mathcal{R}_{1} \sim \mathcal{R}_{2}$ if and only if $\mathcal{R}_{1}$ and $\mathcal{R}_{2}$ cannot be separated by a finite vertex set, i.e., for every finite subset $X \subset \mathcal{V}$ the remaining tails of $\mathcal{R}_{1}$ and $\mathcal{R}_{2}$ in $\mathcal{V} \backslash X$ belong to the same connected component of $\mathcal{V} \backslash X$.

[^1]:    ${ }^{\dagger}$ Notice that for a subgraph $\widetilde{\mathcal{G}}$ of $\mathcal{G}$ its boundary is $\partial \widetilde{\mathcal{G}}=\left\{v \in \mathcal{V}(\widetilde{\mathcal{G}}) \mid \operatorname{deg}_{\widetilde{\mathcal{G}}}(v)<\operatorname{deg}_{\mathcal{G}}(v)\right\}$ and hence $\partial \widetilde{\mathcal{G}}$ is compact only if $\# \partial \widetilde{\mathcal{G}}<\infty$.

[^2]:    ${ }^{\dagger}$ For an operator $T$ with dense domain in a Hilbert space $\mathcal{H}, \lambda \in \mathbb{C}$ is called a point of regular type of $T$ if there exists $c=c_{\lambda}>0$ such that $\|(T-\lambda) f\| \geq c\|f\|$ for all $f \in \operatorname{dom}(T)$.

[^3]:    ${ }^{\dagger}$ A classification of groups having infinitely many ends is given in Stallings's ends theorem 73] (see also 32 Theorem 13.5.10] and Remark[2.5(iv)).

[^4]:    ${ }^{\dagger}$ We shall write $A \leq B$ for two non-negative self-adjoint operators $A$ and $B$ if their quadratic forms $\mathfrak{t}_{A}$ and $\mathfrak{t}_{B}$ satisfy $\operatorname{dom}\left(\mathfrak{t}_{B}\right) \subseteq \operatorname{dom}\left(\mathfrak{t}_{A}\right)$ and $\mathfrak{t}_{A}[f] \leq \mathfrak{t}_{B}[f]$ for every $f \in \operatorname{dom}\left(\mathfrak{t}_{B}\right)$.

[^5]:    ${ }^{\dagger}$ Here we do not assume that $\widehat{\mathfrak{t}}$ is densely defined, see [31 p.29]. We stress that in order for $\widehat{\mathfrak{t}}$ to be a Dirichlet form even merely in the wide sense, it is necessary that dom $(\mathfrak{t})$ is a sublattice of $\mathcal{H}$, hence that the orthogonal projector onto $\operatorname{ran}\left(D^{*}\right)$ is a positivity preserving operator.

[^6]:    ${ }^{\dagger}$ A normal contraction is a function $\varphi: \mathbb{C} \rightarrow \mathbb{C}$ such that $\varphi(0)=0$ and $|\varphi(x)-\varphi(y)| \leq|x-y|$ for all $x, y \in \mathbb{C}$.

    ${ }^{\ddagger}$ For instance, for any $s, L>0$ such that $s \leq L$, the function $\psi_{0}(x):=\frac{L+s}{2}-\left|x-\frac{L+s}{2}\right|$ satisfies $\psi_{0}(0)=0, \psi_{0}(L)=s$ and $\left|\psi_{0}^{\prime}\right| \equiv 1$. The construction in the general case follows easily from this example.

[^7]:    ${ }^{\dagger}$ Here and below to estimate norms, we use the equality $\|A\|=\sqrt{\left\|A^{*} A\right\|}$ and the following simple estimate for non-negative $2 \times 2$ block-matrices $A=\left(\begin{array}{ll}A_{11} & A_{12} \\ A_{12}^{*} & A_{22}\end{array}\right):\|A\| \leq\left\|A_{11}\right\|+\left\|A_{22}\right\|$. There are other estimates (e.g., [36, ineq. (2.3.8)]), however, they do not seem to work as good as the above approach.

