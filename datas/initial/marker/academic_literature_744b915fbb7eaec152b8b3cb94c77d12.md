arXiv:1911.04735v2 [math.SP] 19 Feb 2022

# Self-Adjoint And Markovian Extensions Of Infinite Quantum Graphs

ALEKSEY KOSTENKO, DELIO MUGNOLO, AND NOEMA NICOLUSSI
Abstract. We investigate the relationship between one of the classical notions of boundaries for infinite graphs, graph ends**, and self-adjoint extensions** of the minimal Kirchhoff Laplacian on a metric graph. We introduce the notion of finite volume **for ends of a metric graph and show that finite volume**
graph ends is the proper notion of a boundary for Markovian extensions of the Kirchhoff Laplacian. In contrast to manifolds and weighted graphs, this provides a transparent geometric characterization of the uniqueness of Markovian extensions, as well as of the self-adjointness of the Gaffney **Laplacian - the**
underlying metric graph does not have finite volume ends. If however finitely many finite volume ends occur (as is the case of edge graphs of normal, locally finite tessellations or Cayley graphs of amenable finitely generated groups), we provide a complete description of Markovian extensions upon introducing a suitable notion of traces of functions and normal derivatives on the set of graph ends.

Contents

1. Introduction 2

Notation 5

2. Quantum graphs 5 2.1. Combinatorial and metric graphs 5 2.2. Graph ends 6 2.3. Kirchhoff Laplacian 8 2.4. Deficiency indices 9

3. Graph ends and H1(G) 11 3.1. H1(G**) and boundary values** 11

3.2. Nontrivial and finite volume ends 14

3.3. Description of H1

0

(G) 15

4. Deficiency indices 17 4.1. Deficiency indices and graph ends 17

4.2. Proof of Theorem 4.1 18

5. Properties of self-adjoint extensions 21 6. Finite energy self-adjoint extensions 25 6.1. Normal derivatives at graph ends 26 6.2. Properties of the trace and normal derivatives 28 6.3. Description of self-adjoint extensions 30 7. Deficiency indices of antitrees 33

7.1. Antitrees 33

2020 Mathematics Subject Classification. **Primary 34B45; Secondary 47B25; 81Q10.**
Key words and phrases. **Quantum graph, graph end, self-adjoint extension, Markovian extension, harmonic function.**
Research supported by the Austrian Science Fund (FWF) under **Grants No. P 28807 (A.K.**
and N.N.) and W 1245 (N.N.), by the German Research Foundation (DFG) under Grant No.

397230547 (D.M.), and by the Slovenian Research Agency (ARRS) under Grant No. J1-1690 (A.K.). The authors would like to acknowledge that this article is based upon work from COST
Action CA18232 MAT-DYN-NET, supported by COST (European Cooperation in Science and Technology).

arXiv:1911.04735. J. London Math. Soc., to appear; doi: 10.1112/jlms.12539.

1

 $\begin{array}{ll}\mathbf{7.2.}&\text{Harmonic functions}\\ \mathbf{7.3.}&\text{Finite deficiency indices}\\ \mathbf{7.4.}&\text{Intutite deficiency indices}\\ \mathbf{7.5.}&\text{Proof Theorem7.1}\\ \text{Appendix A.}&\text{Linear relations in Hilbert spaces}\\ \text{Appendix B.}&\text{A rope ladder graph}\\ \text{Abewoledgments}&\\ \text{B.}&\text{Finite deficiency indices}\\ \end{array}$

![1_image_0.png](1_image_0.png)

References 44
$\begin{array}{c}34\\ 36\\ 38\\ 40\\ 41\\ 44\\ 44\\ 44\end{array}$

## 1. Introduction

This paper is concerned with developing extension theory for infinite **quantum**
graphs. Quantum graphs are Schr¨odinger operators on metric graphs**, that is combinatorial graphs where edges are considered as intervals with certain lengths. Motivated by a vast amount of applications in chemistry and physics, they have become**
a popular subject in the last decades (we refer to [8, 9, 26, 67] for **an overview and** further references). From the perspective of Dirichlet forms, quantum graphs play an important role as an intermediate setting between Laplacians on Riemannian manifolds and difference Laplacians on weighted graphs. On the one hand, being locally one-dimensional, quantum graphs allow to simplify considerations of complicated geometries. On the other hand, there is a close relationship between random walks on graphs and Brownian motion on metric graphs, however, in contrast to the discrete case, the corresponding quadratic form in the metric **case is a strongly** local Dirichlet form and in this situation more tools are available (see [7, **28, 58, 59]** for various manifestations of this point of view). Let us also mention **that metric** graphs can be seen as non-Archimedian analogs of Riemann surfaces, which finds numerous applications in algebraic geometry (see [2, 5, 6, 70] for further references).

The most studied quantum graph operator is the Kirchhoff Laplacian, which provides the analog of the Laplace–Beltrami operator in the setting of **metric graphs.**
Its spectral properties are crucial in connection with the heat equation and the Schr¨odinger equation and any further analysis usually relies on the **self-adjointness**
of the Laplacian**. Whereas on finite metric graphs the Kirchhoff Laplacian is always** self-adjoint, the question is more subtle for **graphs with infinitely many edges**.

For instance, a uniform lower bound for the edge lengths guarantees self-adjointness (see [9, 67]), but this commonly used condition is independent of **the combinatorial graph structure and clearly excludes a number of interesting cases (the**
so-called fractal metric graphs**). Moreover, most of the results on strongly local** Dirichlet forms require completeness of a given metric space w.r.t. the "intrinsic" metric (cf., e.g., [74]), which coincides with the natural path (geodesic) metric in the case of metric graphs. Geodesic completeness (w.r.t. the natural path metric)
guarantees self-adjointness of the (minimal) Kirchhoff Laplacian, however, this result is far from being optimal (see [27, §**4] and also Section 2.4 below). The search**
for self-adjointness criteria for infinite quantum graphs is an open **and - in our** opinion - rather difficult problem.

If the (minimal) Kirchhoff Laplacian is not self-adjoint, the natural next step is to ask for a description of its self-adjoint extensions, which corresponds to possible descriptions of the system in quantum mechanics or, if we speak about Markovian extensions, possible descriptions of Brownian motions. Naturally, this question is tightly related to finding appropriate boundary notions for infinite graphs. Our goal in this paper is to investigate the connection between extension theory and EXTENSIONS OF QUANTUM GRAPHS 3 one particular notion, namely graph ends**, a concept which goes back to the work of** Freudenthal [30] and Halin [38] and provides a rather refined way of **compactifying** graphs. However, the definition of graph ends is purely combinatorial and naturally must be modified to capture the additional metric structure of our **setting. Based** on the correspondence between graph ends and topological ends **of metric graphs,** we introduce the concept of ends of finite volume**. First of all, it turns out that**
finite volume ends play a crucial role in describing the Sobolev spaces H1 and H1 0 on metric graphs. More specifically, we show that the presence of finite volume ends is the only reason for the strict inclusion H1 0 ( H1**to hold. This in particular**
provides a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions of the minimal Kirchhoff Laplacian as well as the selfadjointness of the so-called Gaffney Laplacian **(we are not aware of its analogs**
either in the manifold setting or in the context of weighted graph Laplacians, cf. [35, 37, 45, 52, 61, 62]). As yet another manifestation of the fact that finite volume graph ends represent the proper boundary for Markovian extensions of the Kirchhoff Laplacian, we provide a complete description of all finite energy extensions **(i.e.,**
self-adjoint extensions with domains contained in H1**, and all Markovian extensions**
clearly satisfy this condition), however, under the additional assumption that there are only finitely many finite volume ends. Let us stress that this class **of graphs** includes a wide range of interesting models (Cayley graphs of a large class of finitely generated groups, tessellating graphs, rooted antitrees etc. have exactly one end and in this case there are no finite volume ends exactly when the total volume of the corresponding metric graph is infinite). Moreover, we emphasize that in all those cases the dimension of the space of finite energy extensions is equal to the number of finite volume ends, however, for deficiency indices, i.e., the dimension of the space of self-adjoint extensions, this only gives a lower bound (for example, for Cayley graphs the dimension of the space of finite energy extensions is independent of the choice of a generating set, although deficiency indices do depend on **this choice in** a rather nontrivial way). On the other hand, it may happen that these dimensions coincide. The latter holds only if the maximal domain is contained in H1**, that is,**
if every self-adjoint extension is a finite energy extension. This is further equivalent to the validity of a certain non-trivial Sobolev-type inequality (see (1.1) below). The appearance of this condition demonstrates the mixed dimensional behavior of infinite metric graphs since the analogous estimate holds true in the one-dimensional situation, but usually fails in the PDE setting.

Let us now sketch the structure of the article and describe its content and our results in greater details.

In Section 2 we collect basic notions and facts about graphs and metric graphs
(Section 2.1); graph ends (Section 2.2); the minimal and maximal Kirchhoff Laplacians (Section 2.3); deficiency indices and their connection with the spaces of L
2 harmonic and λ**-harmonic functions (Section 2.4).**
The core of the paper is Section 3, where we discuss the Sobolev spaces H1(G)
and H1 0
(G) and introduce the set of finite volume ends C0(G**) (Definition 3.8). We**
show that C0(G) is the proper boundary for H1**functions, which can also be seen**
as an ideal boundary by applying C
∗**-algebra techniques (see Remark 3.14). The**
central result of this section is Theorem 3.12, which shows that H1(G) = H1 0
(G**) if**
and only if there are no finite volume ends. The latter also leads to a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions of the Kirchhoff Laplacian (Corollary 5.5) as well as the self-adjointness of the Gaffney Laplacian HG **(see Remark 5.6(ii) for details and the definition of** HG).

Section 4 contains further applications of the above considerations. Namely, Theorem 4.1 demonstrates that deficiency indices of the minimal Kirchhoff Laplacian can be estimated from below by the number of finite volume ends. This **estimate**
is sharp (e.g., if there are infinitely many finite volume ends) and we also **find necessary and sufficient conditions for the equality to hold. In particular, if there are**
only finitely many ends of finite volume, \#C0(G) < ∞**, the latter is equivalent to**
the validity of the following Sobolev-type inequality (see Remark 4.2)
kf
′kL2(G) ≤ C(kfkL2(G) + kf
′′kL2(G)**) (1.1)**
for all f **in the maximal domain of the Kirchhoff Laplacian. Metric graphs are locally**
one-dimensional and the corresponding inequality is trivially satisfied **in the onedimensional case, however, globally infinite metric graphs are more complex and**
hence (1.1) rather resembles the multi-dimensional setting of PDEs **(in particular,**
(1.1) does not hold true if G has a non-free **finite volume end, see Proposition 4.9).**
In the next sections, we focus on a particular class of self-adjoint **extensions**
whose domains are contained in H1(we call them finite energy extensions**). These**
extensions have good properties and their importance stems from **the fact that they**
contain the class of Markovian extensions (they also arise as self-adjoint restrictions of the Gaffney Laplacian). In Section 5 we show that (under some additional mild assumptions) their resolvents and heat semigroups are integral operators with continuous, bounded kernels and they belong to the trace class if G **has finite total**
volume (Theorems 5.1 and 5.2).

In Section 6 we proceed further and show that finite volume ends is the proper boundary for this class of extensions. Namely, under the additional and rather restrictive assumption of finitely many ends with finite volume**, in Sections 6.1–** 6.2, we introduce a suitable notion of a normal derivative **at graph ends (as a** by-product, this also gives an explicit description of the domain of the Neumann extension, see Corollary 6.7). Section 6.3 contains a complete description of finite energy extensions and also of Markovian extensions (Theorem 6.11). Let us stress that the case of infinitely many ends is incomparably more complicated **and will be** the subject of future work.

In general, the inequality in (1.1) is difficult to verify/contradict and even simple examples can exhibit rather complicated behavior (see Appendix B). The only reason for which (1.1) fails to hold is the presence of L
2 **harmonic functions having**
infinite energy, that is, not belonging to H1**. Moreover, in order to compute deficiency indices of the Kirchhoff Laplacian one, roughly speaking, needs to find the**
dimension of the space of L
2 **harmonic functions and description of self-adjoint extensions requires a thorough understanding of the behavior of** L
2 **harmonic functions**
at "infinity". Dictated by a distinguished role of harmonic functions in **analysis,** there is an enormous amount of literature dedicated to various classes of harmonic functions (positive, bounded etc.), which is further related to different notions of boundaries (metric completion, Poisson and Martin boundaries, Royden and Kuramochi boundaries etc.) and search for a suitable notion in this context (namely, L
2 harmonic functions) is a highly nontrivial problem, which seems not to **be very**
well studied either in the context of incomplete **manifolds (cf. [61, 62]) or in the case** of weighted graphs (see [39, 45]). We further illustrate this by considering the case of rooted antitrees, a special class of infinite graphs with a particularly high degree of symmetry (see Section 7). Infinite rooted antitrees have exactly one graph end, which makes them a good toy model for our purposes. The above considerations show that the space of finite energy L
2 **harmonic functions is nontrivial only if a**
given metric antitree has finite total volume and in this case the only such functions are constants. However, adjusting lengths in a suitable way for a concrete polynomially growing antitree (Figure 1) we can make the space of L
2 **harmonic functions**
as large as we please (even infinite dimensional!).

Notation. Z, R, C **have their usual meaning;** Z≥a := Z ∩ [a, ∞).

z
∗ **denotes the complex conjugate of** z ∈ C.

For a given set S, \#S denotes its cardinality if S **is finite; otherwise we set \#**S = ∞.

If it is not explicitly stated otherwise, we shall denote by (xn**) a sequence (**xn)∞
n=0.

Cb(X) is the space of bounded, continuous functions on a locally compact **space** X. C0(X**) is the space of continuous functions vanishing at infinity.**
For a finite or countable set X, C(X**) is the set of complex-valued functions on** X.

Gd = (V, E**) is a discrete graph (satisfying Hypothesis 2.1).** G = (Gd, | · |**) is a metric graph (see p. 6).** ̺ is the natural (geodesic) path metric on G **(see p. 6).** ̺m is the star metric on V corresponding to the star weight m **(see (2.13)).** Ω(Gd) denotes the graph ends of Gd **(see Definition 2.1).**
C(G) denotes the topological ends of a metric graph G **(see Definition 2.2).** C0(G) stays for the finite volume topological ends of G **(see Definition 3.8).**
Gb is the end (Freudenthal) compactification of G **(see p. 7).**
H00 is the pre-minimal Kirchhoff Laplacian on G **(see (2.9)).**
H0 **is the minimal Kirchhoff Laplacian, the closure of** H00 in L
2(G**) (see (2.9)).**
n±(H0) are the deficiency indices of H0 **(see (2.15)).**
HF and HN are the Friedrichs and Neumann extensions of H0 **(see p. 12 and,**
respectively, p. 24).

H is the maximal Kirchhoff Laplacian on G **(see (2.8)).**
2. Quantum graphs 2.1. Combinatorial and metric graphs. In what follows, Gd = (V, E**) will be**
an unoriented graph with countably infinite sets of vertices V and edges E**. For two**
vertices u, v ∈ V we shall write u ∼ v if there is an edge eu,v ∈ E connecting u **with** v. For every v ∈ V, we denote the set of edges incident to the vertex v by Ev and degG
(v) := \#{e| e ∈ Ev} **(2.1)**
is called the degree (valency or combinatorial degree) of a vertex v ∈ V**. When there**
is no risk of confusion about which graph is involved, we shall simplify and write deg instead of degG. A path P of length n ∈ Z≥0 ∪ {∞} **is a sequence of vertices** (v0, v1, . . . , vn) such that vk−1 ∼ vk for all k ∈ {1**, . . . , n**}.

The following assumption is imposed throughout the paper.

Hypothesis 2.1. Gd is infinite, locally finite (deg(v) < ∞ for every v ∈ V),
connected (for any two vertices u, v ∈ V there is a path connecting u and v**), and**
simple **(there are no loops or multiple edges).**
Next, let us assign each edge e ∈ E a finite length |e| ∈ (0, ∞**). We can then**
naturally associate with (Gd, | · |) = (V, E, | · |) a metric space G: first, we identify each edge e ∈ E with a copy of the interval Ie := [0, |e|**]. The topological space** G
is then obtained by "gluing together" the ends of edges corresponding to the same vertex v **(in the sense of a topological quotient, see, e.g., [13, Chapter 3.2.2]). The**
topology on G is metrizable by the natural path metric ̺ **— the distance between** two points x, y ∈ G **is defined as the arc length of the "shortest path" connecting**
them (if x or y **are not vertices, then we need to allow also paths which start or end** in the middle of edges; the length of such paths is naturally defined by **taking the**
corresponding portion of the interval). The metric space G **arising from the above** construction is called a metric graph (associated to (Gd, | · |) = (V, E, | · |)).

Notice that, by definition, (G, ̺) is a length space **(see [13, Chapter 2.1] for**
definitions and further details). Moreover (see, e.g., [40, Chapter **1.1]), a metric**
graph G is a Hausdorff topological space with countable base and each x ∈ G **has a** neighborhood isometric to a star-shaped set S(deg(x), rx**) of degree deg(**x) ∈ Z≥1, S(deg(x), rx**) :=** z = re 2πik/ deg(x)| r ∈ [0, rx), k = 1, . . . , **deg(**x)
	⊂ C. **(2.2)**
Notice that deg(x) in (2.2) coincides with the combinatorial degree if x **belongs to**
the vertex set, and deg(x**) = 2 for every non-vertex point** x of G.

Sometimes, we will consider Gd as a rooted graph with a fixed root o ∈ V**. In**
this case we denote by Sn, n ∈ Z≥0 the n**-th combinatorial sphere with respect to** the order induced by o **(notice that** S0 = {o}).

2.2. Graph ends. **One possible definition of a boundary for an infinite graph is** the notion of the so-called graph ends (see [30, 38] and [76, § **21]).**
Definition 2.1. **A sequence of distinct vertices (**vn)n∈Z≥0
(resp., (vn)n∈Z**) such**
that vn ∼ vn+1 for all n ∈ Z≥0 (resp., for all n ∈ Z) is called a ray (resp., **double**
ray). A subsequence of such a sequence is called a **tail**.

Two rays R1, R2 are called equivalent - and we write R1 ∼ R2 **– if there is a**
third ray containing infinitely many vertices of both R1 and R2.

† **An equivalence**
class of rays is called a graph end of Gd **and the set of graph ends will be denoted** by Ω(Gd). Moreover, we will write R ∈ ω whenever R **is a ray belonging to the end** ω ∈ Ω(Gd).

An important feature of graph ends is their relation to topological ends of a metric graph G.

Definition 2.2. Consider sequences U = (Un)∞
n=0 **of non-empty open connected**
subsets of G with compact boundaries and such that Un+1 ⊆ Un for all n ≥ **0 and**
Tn≥0 Un = ∅. Two such sequences U and U
′ are called equivalent **if for all** n ≥ 0 there exist j and k **such that** Un ⊇ U
′
j and U
′
n ⊇ Uk**. An equivalence class** γ of sequences is called a topological end of G and C(G**) denotes the set of topological**
ends of G.

For locally finite graphs, there is a bijection between topological ends of a metric graph C(G) and graph ends Ω(Gd) of the underlying combinatorial graph Gd **(see [76,**
§ 21], [23, § **8.6 and also p.277–278]; for the case of graphs which are not locally**
finite see [18, 24]).

Theorem 2.3. For every topological end γ ∈ C(G) **of a locally finite metric graph**
G = (Gd, |·|) there exists a unique graph end ωγ ∈ Ω(Gd) **such that for every sequence** U representing γ, each Un contains a ray from ωγ. Moreover, the map γ 7→ ωγ **is a**
bijection between C(G) and Ω(Gd).

Therefore, we may identify topological ends of a metric graph G **and graph ends**
of the underlying graph Gd. We will simply speak of the ends of G**. One obvious** advantage of this identification is the fact that the definition of Ω(Gd**) is purely**
combinatorial and does not depend on edge lengths.

Definition 2.4. An end ω of a graph Gd is called free **if there is a finite set** X of vertices which separates ω **from all other ends of the graph (i.e. the rays of all ends** ω
′ 6= ω end up in different connected components of V \ X **than the rays of** ω).

Remark 2.5. **Let us mention several examples.**
(i) Z **has two ends both of which are free.**
(ii) Z
N **has one end for all** N ≥ 2.

(iii) A k-regular tree, k ≥ **3, has uncountably many ends, none of which is free.**
(iv) If Gd is a Cayley graph of a finitely generated infinite group G**, then the**
number of ends of Gd is independent of the generating set and Gd **has either** one, two, or infinitely many ends. Moreover, Gd **has exactly two ends only if**
G is virtually infinite cyclic (it has a finite normal subgroup N **such that the**
quotient group G/N is isomorphic either to Z or Z2 ∗ Z2**). These results are**
due to Freudenthal [30] and Hopf [42] (see also [75]). The classification of finitely generated groups with infinitely many ends is due to Stallings [73].

Let us mention that if G **has infinitely many ends, then the result of Stallings**
implies that it contains a non-Abelian free subgroup and hence is nonamenable. For further details we refer to, e.g., [32, Chapter 13].

(v) Let us also mention that by Halin's theorem [38] every locally finite graph Gd **with infinitely many ends contains at least one end which is not free.**
One of the main features of graph ends is that they provide a rather refined way of compactifying graphs (see [29] and [23, § **8.6], [76]). Namely, we introduce**
a topology on Gb := G ∪ C(G) as follows. For an open subset U ⊆ G**, denote its**
extension Ub to Gb by Ub := U ∪ {γ ∈ C(G)| ∃ U = (Un) ∈ γ such that U0 ⊂ U}. **(2.3)**
Now we can introduce a neighborhood basis of γ ∈ C(G**) as follows**

$${\mathrm{od~basis~of~}}\gamma\in{\mathfrak{C}}({\mathcal{G}}){\mathrm{~as~follows~}}$$
$$\{{\hat{U}}\,|\,U\subseteq{\mathcal{G}}{\mathrm{~is~open}},\gamma\in{\hat{U}}\}.$$
$\left(2.4\right)^{2}$

{Ub |U ⊆ G is open, γ ∈ Ub}. **(2.4)**
This turns Gb into a compact topological space, called the **end (or Freudenthal)** compactification of G.

Remark 2.6. Notice that an end γ ∈ C(G) is free exactly when {γ} **is open as** a subset of C(G) (here C(G) carries the induced topology from Gb**). This is further**
equivalent to the existence of a connected subgraph G
γ **with compact boundary**†
∂G
γsuch that Un ⊆ Gγeventually for any sequence U = (Un) representing γ and U
′
n ∩ Gγ = ∅ **eventually for all sequences** U
′ = (U
′
n
) representing an end γ
′ 6= γ.

†Notice that for a subgraph Ge of G its boundary is ∂Ge = {v ∈ V(Ge)| degGe(v) < degG(v)} and hence ∂Ge is compact only if \#∂Ge < ∞.

Let us mention that topological ends can be obtained in a constructive way by means of compact exhaustions. Namely, a sequence of connected **subgraphs (**Fn) of G such that each Fn has finitely many vertices and edges, Fn ⊆ Fn+1 **for all**
n ≥ 0 and Sn Fn = G is called a compact exhaustion of G. Clearly, each Fn **may be**
identified with a compact subset of G. Now iteratively construct a sequence (Un**) by** choosing in each step a non-compact, connected component Un of G \ Fn **satisfying** Un ⊆ Un−1. It is easy to check that each such sequence (Un**) defines a topological**
end γ ∈ C(G) and in fact all ends γ ∈ C(G**) are obtained by this construction.**
Notice also that the open subsets Un of such representations γ ∼ (Un**) (actually,**
their topological closures, since we need to add endpoints of edges **which also belong**
to V(Fn)) can again be identified with connected subgraphs Gn(γ) := Un **and we**
will frequently use this fact.

Let us finish this section with a few more notations. Suppose R **is a ray or a**
finite path without self-intersections in Gd. We may identify R **with a subgraph of** Gd and hence with a subset of G**, i.e., we can consider it as the union of all edges** of R. The latter can further be identified with the interval IR := [0, |R|**) of length** |R|**, where**

$$|{\mathcal{R}}|:=\sum_{e\in{\mathcal{R}}}|e|.$$
$L^-(L_e;\theta)$
Also, we need to consider paths - and in particular rays - in G **starting or ending**
at a non-vertex point. In particular, given a path (v0, v1, . . . , vN **) and a point** x in the interior of some edge e attached to v0, e 6= ev0,v1, we add the interval [**x, v**0] ⊆ e to (v0, v1, . . . , vN ). For the resulting set, we shall write (x, v0, v1, . . . , vN **) and call**
it a non-vertex path**; and likewise for rays. The set of all non-vertex rays will be**
denoted by R(G).

2.3. Kirchhoff Laplacian. Let G **be a metric graph satisfying Hypothesis 2.1.**
Upon identifying every e ∈ E with a copy of the interval Ie = [0, |e|**], we denote by**
L
2(e**) :=** L
2(Ie; dxe)
the L
2-space for the (unweighted) Lebesgue measure dxe on Ie **and introduce the**
Hilbert space L
2(G) of functions f : G → C **such that**

$$L^{2}({\mathcal{G}}):=\bigoplus_{e\in{\mathcal{E}}}L^{2}(e)=\Big\{f=\{f_{e}\}_{e\in{\mathcal{E}}}\big|\,f_{e}\in L^{2}(e),\,\,\sum_{e\in{\mathcal{E}}}\|f_{e}\|_{L^{2}(e)}^{2}<\infty\Big\}.$$

The subspace of compactly supported L
2(G**) functions will be denoted by**
L
2 c
(G**) :=** f ∈ L
2(G)| f 6= 0 only on finitely many edges e ∈ E	.

For every e ∈ E consider the maximal operator He,max **acting on functions** f ∈ H2(e) as a negative second derivative. Here and below Hs(e) for s ≥ **0 denotes the usual**
Sobolev space on e (see, e.g., [12, Chapter 8]). In particular, H0(e) = L
2(e**) and**
H1(e) = {f ∈ AC(e)| f
′ ∈ L
2(e)}, H2(e) = {f ∈ H1(e)| f
′ ∈ H1(e)}.

This defines the maximal operator on L
2(G**) by**

$${\bf H}_{\rm max}:=\bigoplus_{e\in{\cal E}}{\bf H}_{e,{\rm max}},\qquad{\bf H}_{e,{\rm max}}=-\frac{{\rm d}^{2}}{{\rm d}x_{e}^{2}},\quad{\rm dom}({\bf H}_{e,{\rm max}})=H^{2}(e).\tag{2.5}$$
$${\mathrm{ery}}\ f\in H^{2}(e)$$

EXTENSIONS OF QUANTUM GRAPHS 9 If v is a vertex of the edge e ∈ E, then for every f ∈ H2(e**) the following quantities**

$$f_{e}(v):=\lim_{x_{e}\to v}f(x_{e}),\qquad\qquad f_{e}^{\prime}(v):=\lim_{x_{e}\to v}\frac{f(x_{e})-f(v)}{|x_{e}-v|},$$  for all $C$ and $D$, $\mathcal{C}$ are the points of all $v$ and $v$ in the set 
, **(2.6)**
are well defined. Considering G **as the union of all edges glued together at certain**
endpoints, let us equip a metric graph with the Laplace operator. The Kirchhoff
(also called standard or Kirchhoff–Neumann**) boundary conditions at every vertex**
v ∈ V **are then given by**

$$(2.6)$$

$$\begin{array}{l}{{f\mathrm{~is~continuous~at~}v,}}\\ {{\sum_{e\in{\mathcal{E}}_{v}}f_{e}^{\prime}(v)=0.}}\end{array}$$
$$(2.7)$$

$$\operatorname{max})\mid f{\mathrm{~sat}}$$
$$\mathrm{i}(\mathbf{H}_{\mathrm{m}}$$

′e(v) = 0.**(2.7)**
Imposing these boundary conditions on the maximal domain dom(Hmax**) yields the**
maximal Kirchhoff Laplacian H := Hmax ↾ **dom(**H),
dom(H) = {f ∈ dom(Hmax)| f satisfies (2.7) for any v **∈ V}**.

(2.8)

$$\mathbf{H})=\{f\in$$
Restricting further to compactly supported functions we end up with the preminimal operator
$$(2.9)$$
$\mathbf{H}_{0}^{v}:=\mathbf{H}_{\max}\upharpoonright\mathrm{dom}(\mathbf{H}_{0}^{v})$,  $\mathrm{dom}(\mathbf{H}_{0}^{0})=\{f\in\mathrm{dom}(\mathbf{H}_{\max})\cap L_{c}^{2}(\mathcal{G})|\,f\text{satisfies}(2.7)\text{for any}v\in\mathcal{V}\}$.  
Integrating by parts one obtains

$$\langle\mathbf{H}_{0}^{0}f,f\rangle_{L^{2}(\mathcal{G})}=\int_{\mathcal{G}}|f^{\prime}(x)|^{2}\ d x,\qquad f\in\mathrm{dom}(\mathbf{H}_{0}^{0}),$$
$\downarrow$ . 
$${\mathrm{y}}\ v\in{\mathcal{V}}\}.$$
$$\mathbf{s}\ (z,t\ )\ \mathbf{i}\mathbf{o}\mathbf{n}$$
$$(2.10)^{\frac{1}{2}}$$
), **(2.10)**
and hence H00**is a non-negative symmetric operator. We call its closure** H0 := H00 in L
2(G) the minimal Kirchhoff Laplacian**. The following result is well-known (see,**
e.g., [16, Lemma 3.9]).

Lemma 2.7. Let G **be a metric graph. Then**
H∗
0 = H. **(2.11)**
2.4. Deficiency indices. **In the following we are interested in the question whether**
H0 is self-adjoint, or equivalently whether the equality H0 = H **holds true. Let us**
recall one sufficient condition. Define the star weight m(v) of a vertex v ∈ V by
$$m(v):=\sum_{e\in{\mathcal{E}}_{v}}|e|=\operatorname{vol}({\mathcal{E}}_{v}),$$
|e| = vol(Ev), **(2.12)**
and also introduce the **star path metric** on V by

$\left(2.11\right)^{2}$

$$(2.12)$$
$$\varrho_{m}(u,v):=\operatorname*{inf}_{\mathcal{P}=(v_{0},\dots,v_{n})\atop u=v_{0},\ v=v_{n}}\sum_{v_{k}\in\mathcal{P}}m(v_{k}).$$
$$(2.13)^{\frac{1}{2}}$$
$\mathbf{a}\cdot\mathbf{a}=\mathbf{a}\cdot\mathbf{a}$. 
: on $\mathcal V$ by . 
$$-\,z),\quad\ z\in\mathbb{C}.$$
$$(2.)$$

m(vk). **(2.13)**
Theorem 2.8 ([27]). If (V, ̺m) **is complete as a metric space, then** H00 is essentially self-adjoint and H00 = H0 = H.

If a symmetric operator is not (essentially) self-adjoint, then the degree of its nonself-adjointness is determined by its deficiency indices. Recall that the **deficiency**
subspace Nz(H0) of H0 **is defined by**

$\frac{1}{2}$  . 
Nz(H0**) := ker(**H∗
0 − z) = ker(H − z), z ∈ C. (2.14)
The numbers n±(H0) := dim N±i(H0) = dim ker(H ∓ **i) (2.15)**
are called the deficiency indices of H0. Notice that n+(H0) = n−(H0**) since** H0 is non-negative. Moreover, H0 is self-adjoint exactly when n+(H0) = n−(H0**) = 0.**
Lemma 2.9. If 0 is a point of regular type for H0**, then**†
n±(H0) = dim ker(H). **(2.16)**
Proof. The claim immediately follows from [1, § **78] or [69, Prop. 3.3]. Indeed, the**
set of regular points of H0 is an open subset of C**. Moreover, by the Krasnoselskii–**
Krein theorem (see, e.g., [1, § 78] or [69, Prop. 2.4]), dim Nz(H0**) is constant on**
each connected component of the set of regular type points of H0**. Since** H0 is symmetric, each z ∈ C \ R is a point of regular type for H0**. Therefore, if 0 is a**
point of regular type for H0**, we immediately get**
dim ker(H) = dim N0(H0) = n+(H0**) = n**−(H0). 

Using the Rayleigh quotient, define

Z H0f, fL2(G) = inf f∈dom(H0) kfk=1 G |f ′| 2dx. (2.17) λ0(G) := inf f∈dom(H0) kfk=1
$$(2.18)$$
Noting that the operator H0 **is non-negative, 0 is a point of regular type for** H0 if
λ0(G) > **0. Thus, we arrive at the following result.**
Corollary 2.10. If λ0(G) > 0, then (2.16) **holds true.**
The positivity of λ0(G**) is known in the following simple situation.**
Corollary 2.11. If G **has finite total volume,**
$$\operatorname{vol}({\mathcal{G}}):=\sum_{e\in{\mathcal{E}}}|e|<\infty,$$
|e| < ∞, **(2.18)**
then H0 is not self-adjoint and (2.16) **holds true.**
Proof. **Indeed, by the Cheeger-type estimate [55, Corollary 3.5(iv)], we have**

 $\ast t\;and\;(2,16)\;holds\;true$ . 
$$\lambda_{0}({\mathcal G})\geq{\frac{1}{4\operatorname{vol}({\mathcal G})^{2}}}>0,$$
1
4 vol(G)
> 0, **(2.19)**
and hence (2.16) holds true by Corollary 2.10. Moreover, 1G ∈ ker(H**), where** 1G
denotes the constant function on G**, and hence**
n±(H0**) = dim(ker** H) ≥ 1.

It remains to notice that H0 is self-adjoint exactly when n±(H0**) = 0.** 
Remark 2.12. By [55, Theorem 3.4], λ0(G) > **0 holds true if the isoperimetric**
constant α(G) of the metric graph G **is positive. For antitrees, the isoperimetric**
constant is tightly related to the structure of its combinatorial spheres (see [56, Theorem 7.1]). If Gd **is the edge graph of a tessellation of** R
2**, then positivity of**
α(G**) can be deduced from certain curvature-type quantities [65].**
On the other hand, by [55, Corollary 4.5(i)], λ0(G) > 0 holds true if the combinatorial isoperimetric constant of Gd **is positive and** ℓ
∗(G) := supe∈E |e| < ∞**. For**
†For an operator T with dense domain in a Hilbert space H, λ ∈ C is called a **point of regular**
type of T if there exists c = cλ > 0 such that k(T − λ)fk ≥ ckfk for all f ∈ dom(T).