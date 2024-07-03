# A New Way To Evaluate G**-Wishart Normalising Constants** Via Fourier Analysis

BY CHING WONG1,a, GIUSI MOFFA1,b, AND JACK KUIPERS2,c 1Department of Mathematics and Computer Science, University of Basel, a*ching.wong@unibas.ch;*
b*giusi.moffa@unibas.ch* 2Department of Biosystems Science and Engineering, ETH Zurich, c*jack.kuipers@bsse.ethz.ch* The G-Wishart distribution is an essential component for the Bayesian analysis of Gaussian graphical models as the conjugate prior for the precision matrix. Evaluating the marginal likelihood of such models usually requires computing high-dimensional integrals to determine the G-Wishart normalising constant. Closed-form results are known for decomposable or chordal graphs, while an explicit representation as a formal series expansion has been derived recently for general graphs. The nested infinite sums, however, do not lend themselves to computation, remaining of limited practical value. Borrowing techniques from random matrix theory and Fourier analysis, we provide novel exact results well suited to the numerical evaluation of the normalising constant for a large class of graphs beyond chordal graphs.

Furthermore, they open new possibilities for developing more efficient sampling schemes for Bayesian inference of Gaussian graphical models.

1. Introduction. The Wishart distribution [43] plays a key role in Bayesian statistics [9]
as the conjugate prior for the precision (inverse covariance) matrix of multivariate Gaussians.

Given independently drawn observations from a centred multivariate normals, the product of the data matrix and its transpose constitute a sample matrix from a Wishart distribution, which represents the distribution of scatter or sample covariance matrices. Since the sample data is itself a random matrix, the Wishart distribution is a classical distribution in random matrix theory [27, 24], where it is known as the Wishart-Laguerre, or Laguerre ensemble (which also extends beyond the real case to complex and quaternionic data matrices).

Random matrices were first used by Wigner [42] as simple models of complex quantum systems, like nuclear reactions, where physical observables are related to the eigenvalue spectrum. The random matrix approach is predicted to be applicable when the underlying classical dynamics are chaotic, and the inverse eigenvalues from the Wishart-Laguerre ensemble correspond to the Wigner time delays in quantum chaotic scattering [3]. Agreement between statistics of a random matrix and quantum spectra can be derived through diagrammatic perturbation theory [20] and understood via intermediate matrix integrals [31]. For the related problem of quantum transport and the Jacobi ensemble (which can be obtained from a combination of two Wisharts), full equivalence has been proven [2]. The Wishart-Laguerre ensemble is also a key model for quantum chromodynamics [39] and entanglement [26], while the eigenvalue distribution is also important for principal component analysis [16].

For high-dimensional statistics, the Wishart distribution is instrumental in aiding the modelling of multivariate continuous data with probabilistic graphical models. These are popular and powerful tools [22, 17] for compactly representing data and their dependencies with a graph, where each node encodes a variable and the edges encode conditional independence relationships. The most common types are Markov random fields, represented as *undirected* graphs, and Bayesian networks, represented as *directed acyclic graphs (DAGs)*. Evaluating the marginal likelihood of each structure is a key ingredient to enable Bayesian analyses.

The factorisation of Bayesian networks into components involving each child and its parents, allows us to leverage the properties of the conjugate Wishart prior to easily evaluate the Gaussian integrals, and express them as ratios of the graph normalising constants of the prior and posterior distributions [8, 19]. Increasingly efficient MCMC schemes have been developed to create Bayesian samplers [25, 10, 14, 18, 21] and exact samplers have been built for smaller networks [36]. With the current advances in Bayesian sampling of DAGs, we can propagate the uncertainty in both structure and parameters to obtain, for example, the posterior distribution of causal intervention effects in fully Bayesian analyses [28, 40].

In contrast, Bayesian inference for undirected graphical models has been hampered by the intractability of the marginal likelihood integrals, which we now introduce.

1.1. The G*-Wishart normalising constant.* We denote by S
nthe set of all n by n real symmetric matrices, and by S
n++ the set of all symmetric positive definite matrices in R
n×n.

For a graph G = (V(G), E(G)) with vertex set V(G) = {v1*, . . ., v*n}, let

$$\mathbb{S}_{++}^{n}({\mathcal{G}}):=\{M\in\mathbb{S}_{++}^{n}:\{v_{\mu},v_{\nu}\}\not\in{\mathcal{E}}({\mathcal{G}})\implies m_{\mu,\nu}=0\}$$

be the set of n by n real symmetric positive definite matrices whose entries corresponding to a pair of non-adjacent vertices are zero. The *Gaussian graphical model* with respect to G is MG = {Nn(0,Σ) : Σ−1 ∈ S
n
++(G)},
the set of n-variate Gaussian distributions with mean zero and variance Σ such that the precision matrix K = Σ−1is in S
n++(G). A common choice for the prior distribution for K ∈ S
n++(G) is

$$f(K\,|\,{\mathcal{G}})\sim\operatorname*{det}(K)^{\frac{\delta-2}{2}}e^{-\frac{\mathrm{tr}(K D)}{2}},\quad{\mathrm{where~}}\delta>0{\mathrm{~and~}}D\in\mathbb{S}_{++}^{n},$$

as it is conjugate [35]. Let Z ∈ R
n×N be a dataset with N samples and n variables, the marginal likelihood for the Gaussian graphical model above is then

$$p(Z\,|\,{\mathcal G})=\frac{2^{-\binom{n}{2}}}{(2\pi)^{\frac{n N}{2}}}\frac{{\mathcal G}_{{\mathcal G}}(\delta+N,U+D)}{{\mathcal C}_{{\mathcal G}}(\delta,D)},\qquad U=\sum_{j=1}^{N}({\mathbf z}_{j}-\overline{{{\mathbf z}}})({\mathbf z}_{j}-\overline{{{\mathbf z}}})^{\mathsf T},$$

where U is the scatter matrix (an unnormalised sample covariance), and

$${\mathcal{C}}_{{\mathcal{G}}}(\delta,D):=\int_{\mathbb{S}_{++}^{n}({\mathcal{G}})}\operatorname*{det}(K)^{\frac{\delta-2}{2}}e^{-{\frac{\operatorname{tr}(K D)}{2}}}\operatorname{d}\!K,\qquad\quad{\mathrm{for~}}\delta>0{\mathrm{~and~}}D\in\mathbb{S}_{++}^{n},$$

is the G*-Wishart normalising constant*. As in [38], a change of variables K → 2K allows us to simplify

$$\mathcal{C}_{\mathcal{G}}(\delta,D)=2^{\frac{nL}{2}+|\mathcal{E}(\mathcal{G})|}\mathcal{I}_{\mathcal{G}}\left(\frac{\delta-2}{2},D\right),$$  where  $$\mathcal{I}_{\mathcal{G}}(\beta,D):=\int_{\mathbb{S}^{n}_{++}(\mathcal{G})}\det(K)^{\beta}e^{-\operatorname{tr}(KD)}\,\mathrm{d}K,\qquad\text{for$\beta>-1$and$D\in\mathbb{S}^{n}_{++}$}.\tag{1}$$

Evaluating the integral IG(*β, D*) for a general graph G is challenging. Roverato [35]
proved that the normalising constant for G can be factorised according to the *prime components* of G, see equation (5) in Section 2. Consequently, we only need to evaluate IG(*β, D*)
for prime graphs G. Apart from this, the only progress has come more recently from Ulher et al. [38] as an iterative method for evaluating the integral, which is, however, highly intricate and the resulting nested infinite sums do not appear to offer a viable path for evaluation.

Currently the only approaches for evaluating the G-Wishart normalising constant for general graphs are Monte Carlo algorithms [1, 35, 30], which become increasingly computationally intensive for larger networks. Interestingly though, Roverato [35] observed and conjectured that, for a graph G with n vertices, D ∈ S
n++ and real number δ > 0,
(2) CG(*δ, D*) = 2 n 2 det(IssG(D˜))− 12 det(D˜)
−
δ−2 2 CG(*δ, I*n),
where D˜ ∈ S
n++ is the *PD-completion* of D with respect to G, and IssG(D˜) is the *Isserlis* matrix of D˜ with respect to G. If this conjecture were proved, finding the G-Wishart normalising constant when D is the identity matrix (and G is prime) would suffice to evaluate the constant for general matrices D (and general graphs G).

1.2. *Known results.* There are a few classes of prime graphs for which the normalising constant is known explicitly. To describe them we need some graph theory terminology. An n-vertex graph is *complete*, denoted by Kn, if every pair of vertices is adjacent. For k ≥ 2, a graph is complete k*-partite*, denoted by Kn1*,...,n*k, if its vertex set can be partitioned into k sets, V1*, . . . ,*Vk, with |Vµ| = nµ for 1 ≤ µ ≤ k, such that v is adjacent to u if and only if v and u belong to different parts Vµ and Vν . When k = 2, it is *complete bipartite*. A graph is chordal if it does not possess any induced cycle of length longer than three. Note that every graph has a *chordal completion* (i.e., a chordal supergraph on the same vertex set), as the complete graphs are chordal. The *minimum fill-in* of a graph is the smallest number of edges that need to be added to turn it into a chordal graph.

If G is an n-vertex *prime graph* (see Section 2.1 for the definition) and β > −1 is a real number, an explicit formula (involving gamma functions) for IG(*β, D*) is known when
(A1) G is complete and D ∈ S
n++ [6], or
(A2) G has minimum fill-in 1 and D = In [38], or
(A3) G is complete bipartite and D = In [38].

1.3. *Bayesian inference for undirected graphs.* Efficient sampling methods exist for the restricted class of decomposable (complete) graphs [13, 11, 32], thanks to their known results
(A1). For general undirected graphs, without a handle on evaluating the marginal likelihood and hence the posterior of each network, Bayesian approaches have progressed by avoiding evaluating IG(*β, D*) and working instead in the joint (un-marginalised) space of networks and elements of the precision matrices [41, 23, 29]. Due to the different sized parameter spaces for different networks, these approaches build on trans-dimensional MCMC [12]. Notably, Bayesian sampling [29] outperforms the simple point estimate which can be obtained from regularised optimisation [7]. Although current Bayesian methods avoid evaluating equation
(1) directly, they still require the evaluation for the simpler case where D = In. As with the conjecture of Roverato [35], this highlights how the identity matrix case is a key bottleneck for further progress. Recently, approximations for D = In were developed and shown to offer computational advantages for Bayesian inference for undirected networks [33].

1.4. *Our contribution.* Borrowing inspiration from random matrix theory [15] and using tools from Fourier analysis, we show how to transform the integral IG(*β, D*) in a way that enables us to derive an explicit formula (involving gamma functions and generalised hypergeometric functions 3F2) for the G-Wishart normalising constant when
(B1) G has a chordal completion G
∗in which every triangle contains at most one edge from E(G
∗) \ E(G) and D = I|V(G)|(Corollary 4.3), or
(B2) G has minimum fill-in 2 and D = I|V(G)|(Section 4.4), or (B3) G is complete k-partite and D = I|V(G)|(Example 4.2).

Note that (B1) contains every Turán graph T (2*n, n*), which is a prime graph with minimum fill-in n − 1 when n ≥ 2 (Example 4.4).

Moreover, we show that the integral of interest can be converted into a one-dimensional real integral when
(C1) G is isomorphic to some G(m; k1*, . . ., k*ℓ) (defined in Section 4.3), where m ≥ 4, 3 ≤
ℓ ≤ m − 1 and k1*, . . ., k*ℓ ≥ 1, and D = Im+k1+···+kℓ
(Corollary 4.8), or
(C2) G has a chordal completion with 3 added edges that form a triangle and D = I|V(G)|
(Section 5.1), or
(C3) G is the cycle of length 6 or its complement and D = I6 (Example 3.1, Example 4.6).

We remark that in (C1), there are infinitely many prime graphs of any given minimum fill-in greater than 2. In Appendix C, we list all 24 connected prime graphs on 6 vertices, which belong to (B1), (B2), (B3) or (C3).

Furthermore, we show that the G-Wishart normalising constant can be written as an integral of the form

3. $\int_{\mathbb{R}^{+}}\prod_{\{\alpha_{1},\ldots,\alpha_{k}\}\in\mathfrak{J}}(1+t_{\alpha_{1}}^{2}+\cdots+t_{\alpha_{k}}^{2})^{-\gamma_{\alpha_{1},\ldots,\alpha_{k}}}\,\mathrm{d}t_{1}\cdots\,\mathrm{d}t_{\tau},\quad\text{where}\mathfrak{J}\subseteq\mathcal{P}(\{1,\ldots,\tau\}),$
when
(D1) G has *starry fill-ins* and D = I|V(G)|(Corollary 4.7), or
(D2) G is a *gear graph* and D = I|V(G)|(Corollary 5.1).

The definitions of *starry fill-in* and *gear graphs* can be found in Section 4.2 and Section 5.2, respectively. We remark that (D1) contains all the cycle graphs. An example of (3) is

$$\int_{\mathbb{R}^{3}}(1+t_{1}^{2})^{-\frac{1}{2}}(1+t_{2}^{2})^{\frac{5}{2}}(1+t_{3}^{2})^{-\frac{1}{2}}(1+t_{1}^{2}+t_{2}^{2})^{-5}(1+t_{2}^{2}+t_{3}^{2})^{-5}\,\mathrm{d}t_{1}\,\mathrm{d}t_{2}\,\mathrm{d}t_{3},$$

with τ = 3 and I = {{1}, {2}, {3}, {1, 2}, {2, 3}}, which we encounter later in Example 4.6 for the cycle of length 6, before reducing it down to one dimension as in (C3).

Finally, for general D, we obtain a one-dimensional integral when
(E1) G has minimum fill-in 1 and D ∈ S
|V(G)|
++ (Section 6).

Together with the prime factorisation (Equation (5) later) due to Roverato [35], the above results simplify the computation for the G-Wishart normalising constants for many graphs.

For instance, for a 2 by m grid (whose prime components are m − 1 cycles of length 4, each with minimum fill-in of 1) and a matrix D ∈ S
2m
++, the G-Wishart normalising constant can be written as the product of m − 1 one-dimensional integrals. Section 6 delves deeper into the details of such integrals.

All the results mentioned above have been built upon the following theorem, in which we transform the integral IG(*β, D*) over the restricted (relative to R
|E(G)|+|V(G)|) space S
|V(G)|
++ (G)
into an integral over the Euclidean space R
τ, where τ is the number of edges needed for a known chordal completion of G. The matrix Dirac delta function (Fourier transform of 1), as used in [15], is employed. The proof of this result can be found in Section 3.

THEOREM 1.1. Let G *be a proper subgraph of* G
∗, both on the vertex set {v1*, . . ., v*n}.

Let β > −1 *be a real number and* D ∈ S
n++*. Then,*

$${\mathcal{I}}_{\mathcal{G}}(\beta,D)={\frac{1}{\pi|{\mathcal{E}}({\mathcal{G}}^{*})|-|{\mathcal{E}}({\mathcal{G}})|}}\int_{\mathbb{S}({\mathcal{G}},{\mathcal{G}}^{*})}{\mathcal{I}}_{{\mathcal{G}}^{*}}(\beta,D+i T)\,\mathrm{d}T,$$

where S(G,G
∗) := {T ∈ S
n: µ = ν or {vµ, vν} ∈ E(G) or {vµ, vν*} ̸∈ E*(G
∗) =⇒ tµ,ν = 0}.

In particular, if G
∗is a chordal completion of G*, then*

$$\mathcal{I}_{\mathcal{G}}(\beta,D)=\frac{\mathcal{I}_{\mathcal{G}^{*}}(\beta,I_{n})}{\pi^{|\mathcal{E}(\mathcal{G}^{*})|-|\mathcal{E}(\mathcal{G})|}}\int_{\mathbb{S}(\mathcal{G},\mathcal{G}^{*})}\frac{\prod_{\mu=1}^{m}\det((D+iT)[\mathcal{C}_{\mu}])^{-\beta-\frac{|\mathcal{G}_{\mu}|+1}{2}}}{\prod_{\nu=1}^{m}\det((D+iT)[\mathcal{S}_{\nu}])^{-\beta-\frac{|\mathcal{G}_{\nu}|+1}{2}}}\,\mathrm{d}T,$$

where C1, . . .,Cm ⊆ V(G) *are the maximal cliques of* G
∗ and S1, . . ., Sm−1 ⊆ V(G) are the minimal separators (see Section 2 *for definitions).*
Note that S(G,G
∗) is the set of n by n symmetric real matrices, in which every entry is equal to zero unless it corresponds to an edge in E(G
∗) \ E(G). Thus, the number of variables in S(G,G
∗) is |E(G
∗)*| − |E*(G)|. It follows that an integral with domain S(G,G
∗) (Lebesgue measure) is the same as an integral over R
|E(G
∗)*|−|E*(G)|.

While the normalising constant can be factorised according to the prime components of a graph, under certain assumptions, the integral IG(*β, I*|V(G)|) can be further factorised for some prime graphs G, since IG∗ (*β, I*|V(G)| + iT) can be written as the product of some separable functions. The following theorem characterises these graphs. In Section 4 we illustrate this result using a toy example (Example 4.1), while a formal proof is given in Appendix A.1.

THEOREM 1.2. Let G be a graph on n *vertices and let* G
∗ be a chordal completion.

Suppose that there exists a partition of the missing edges E(G
∗) \ E(G) = E1 ⊔ · ·· ⊔ Ek such that for 1 ≤ µ < ν ≤ k*, either*

$$\begin{array}{l}{{\bullet\;\;\mathcal{V}_{\mu}\cap\mathcal{V}_{\nu}=\emptyset,\,o r}}\\ {{\bullet\;\;|\mathcal{V}_{\mu}\cap\mathcal{V}_{\nu}|=1\;a.}}\end{array}$$

- |Vµ ∩ Vν| = 1 *and there is no edge in* G
∗ between the sets Vµ \ Vν and Vν \ Vµ, where Vξ ⊆ V(G) is the vertex set associated with the edges in Eξ*, for* ξ = 1, . . ., k.

Let β > −1 *be a real number. Then,*

$${\mathcal{I}}_{\mathcal{G}}(\beta,I_{n})={\mathcal{I}}_{\mathcal{G}^{\star}}(\beta,I_{n})^{1-k}\prod_{\xi=1}^{k}{\mathcal{I}}_{\mathcal{G}_{\xi}}(\beta,I_{n}),$$
$$e~s e t s~{\mathcal V}_{\mu}\setminus{\mathcal V}_{\nu}~a n d~{\mathcal V}_{\nu}\setminus{\mathcal V}_{\mu}$$
$${\hat{o}}r\;1\leq\xi\leq k$$

where Gξ *is the graph obtained from* G
∗ by removing the edges in Eξ*, for* 1 ≤ ξ ≤ k.

2. Preliminaries. In this paper, all graphs G = (V(G), E(G)) are assumed to be simple and undirected. We denote by N G(v) ⊆ V(G) the set of all the neighbours of the vertex v in graph G. A set C ⊆ V(G) is a *clique* of G if two vertices u and v are adjacent whenever they are both in C. A clique C of G is considered *maximal* if there is no clique in G that strictly contains C. A graph G is *connected* if for any pair of vertices u, v ∈ V(G), one can travel from u to v via edges of G. For a subset V
′ ⊆ V(G), we use G[V
′] to denote the *induced* subgraph of G formed from the vertices in V
′. A set S ⊆ V(G) is a *separator* of a (connected)
graph G if the induced subgraph G[V(G) \ S] is not connected. A separator S is considered minimal if there is no separator in G that is strictly contained in S. For a graph G with vertex set V(G) = {v1*, . . ., v*n} and a matrix D in S
n++, the matrix D[C] ∈ S
|C|
++, where C ⊆ V(G),
is the submatrix of D obtained by the corresponding rows and columns.

In this section, we highlight some definitions and known results about chordal graphs. For a comprehensive overview, we refer to [22].

2.1. *Graph decomposition.* A graph G is *prime* if it contains no separator that is a clique.

Examples of prime graphs include complete graphs, cycle graphs and grid graphs. Given a non-prime graph G, one can select a maximal clique C that separates the graph into two nonempty sets A and B. Then, we say that G is *decomposed* into two components G[A ∪ C] and G[B ∪ C]. Continuing this process, the graph G can be uniquely decomposed into its prime components. For example, the 2 by m grid can be decomposed into m − 1 cycles of length 4.

2.2. *Perfect sequence of prime components.* Let G be a graph with m prime components.

An ordering of the prime components of G, say G[P1]*, . . .,*G[Pm], is a *perfect sequence of* prime components if, for every 1 ≤ µ ≤ m − 1, there exists ν ≤ µ such that
(P1 *∪ · · · ∪* Pµ) ∩ Pµ+1 ⊆ Pν, which is known as the *running intersection property*. For simplicity in notation, we slightly abuse the representation by referring to P1*, . . .,*Pm as a perfect sequence of prime components, as opposed to using G[P1]*, . . .,*G[Pm]. It is known that each graph possesses at least one perfect sequence of prime components.

Given a perfect sequence of prime components P1*, . . .,*Pm of a graph G, the sets Sν := (P1 *∪ · · · ∪* Pν) ∩ Pν+1, where 1 ≤ ν ≤ m − 1, are the corresponding set of separators. It is well known that the induced subgraphs G[Sν] are complete and that the multiset {S1*, . . .,* Sm−1} is invariant to the choice of the perfect sequence of prime components. In this paper, keeping in mind that some of these sets might be identical, we refer to the sets S1, . . ., Sm−1 as *the minimal separators* of G.

2.3. *Chordal graphs.* A graph is considered *decomposable* if its prime components are all complete. These graphs can be characterised by their graphical properties; specifically, they are graphs in which all induced cycles have length 3. Equivalently, every cycle in these graphs with length greater than three contains at least one *chord*, which refers to an edge connecting two vertices within the cycle that is not part of the cycle itself. Thus, decomposable graphs are also known as *chordal graphs*, and here we will use the term chordal graphs.

For chordal graphs, we write perfect sequence of cliques C1*, . . .,*Cm in place of *perfect* sequence of prime components P1*, . . .,*Pm, to emphasise that the vertex sets of the prime components are cliques. We remark that the prime components of a chordal graph are precisely its maximal cliques.

2.4. *Chordal completion.* Given any graph G, a graph G
∗ on the same vertex set is a chordal completion of G if G
∗is chordal, and G is a subgraph of G
∗. When there is no ambiguity, we refer to the edges E(G
∗)\ E(G) the *missing edges*. Our results later rely heavily on finding a chordal completion (of a given graph) with some nice properties. In particular, the fewer the edges in the chordal completion, the lower the dimension of the integral in Theorem 1.1. Finding a chordal completion of a given graph with the minimum number of edges is known as the *minimum chordal completion problem* or the *minimum fill-in problem*,
which is NP-complete [44]. Several linear-time algorithms, including Lexicographic BreadthFirst Search [4, 34] and Maximum Cardinality Search [37], have been proposed for finding chordal completions of graphs, though they do not always find one with minimum fill-in.

2.5. Factorisation of G*-Wishart normalising constant.* For a complete graph Kn, the GWishart normalising constant is the normalising constant for a Wishart distribution:

$${\mathcal{I}}_{K_{n}}(\beta,D)=\int_{\mathbb{S}_{++}^{n}}\operatorname*{det}(K)^{\beta}e^{-\operatorname{tr}(K D)}\;\mathrm{d}K=\operatorname*{det}(D)^{-\beta-{\frac{n+1}{2}}}\Gamma_{n}\left(\beta+{\frac{n+1}{2}}\right)$$

,
where Γk(a) is the *multivariate gamma function*

$$\Gamma_{k}(a):=\pi^{\frac{k(k-1)}{4}}\prod_{\mu=1}^{k}\Gamma\left(a+\frac{1-\mu}{2}\right),\qquad\mathrm{for}\;a>\frac{k-1}{2}.$$

Let G
∗ be a chordal graph. Let C1*, . . .,*Cm be the maximal cliques and S1*, . . .,* Sm−1 be the minimal separators. Then, it is known [5] that the integral IG∗ (*β, D*) can be factorised as

$$\mathcal{I}_{\mathcal{G}^{*}}(\beta,D)=\frac{\prod\limits_{\mu=1}^{m}\mathcal{I}_{\mathcal{G}^{*}|\mathbf{C}_{\mu}|}(\beta,D[\mathbf{C}_{\mu}])}{\prod\limits_{\nu=1}^{m-1}\mathcal{I}_{\mathcal{G}^{*}|\mathbf{S}_{\nu}|}(\beta,D[\mathbf{S}_{\nu}])}\quad\prod\limits_{\nu=1}^{m}\det(D[\mathbf{C}_{\mu}])^{-\beta-\frac{|\mathbf{S}_{\nu}|+1}{2}}\Gamma_{|\mathbf{C}_{\mu}|}\left(\beta+\frac{|\mathbf{C}_{\mu}|+1}{2}\right).\tag{4}$$

Roverato [35] generalised this factorisation to general graphs G:

$$\mathcal{I}_{\mathcal{G}}(\beta,D)=\frac{\prod\limits_{\mu=1}^{m}\mathcal{I}_{\mathcal{G}[\mathsf{P}_{\mu}]}(\beta,D[\mathsf{P}_{\mu}])}{\prod\limits_{\nu=1}^{m-1}\mathcal{I}_{\mathcal{G}[\mathsf{S}_{\nu}]}(\beta,D[\mathsf{P}_{\nu}])}=\frac{\prod\limits_{\mu=1}^{m}\mathcal{I}_{\mathcal{G}[\mathsf{P}_{\mu}]}(\beta,D[\mathsf{P}_{\mu}])}{\prod\limits_{\nu=1}^{m-1}\det(D[\mathsf{S}_{\nu}])^{-\beta-\frac{\left(\mathsf{S}_{\nu}\right)+1}{2}}\Gamma_{[\mathsf{S}_{\nu}]}\left(\beta+\frac{[\mathsf{S}_{\nu}]+1}{2}\right)},\tag{5}$$

where P1*, . . .,*Pm are the prime components of G and S1*, . . .,* Sm−1 are the minimal separators. This is why we only need to find the normalising constants for prime graphs. We remark that (5) can be easily derived from Theorem 1.1, by separating the variables.

## 3. Transforming The Integral Using Fourier Analysis. We Provide An Example After Proving Theorem 1.1.

PROOF OF THEOREM 1.1. We begin with a parametrised form of the domain S
n++(G) in the integral IG(*β, D*) (defined in (1)) and write

$$\mathcal{I}_{\mathcal{G}}(\beta,D)=\int_{S^{2}_{+}(\mathcal{G})}\det(K)^{\beta}e^{-\operatorname{tr}(KD)}\,\mathrm{d}K$$ $$=\int_{\mathbb{R}^{|\mathcal{E}(\beta)|}}\int_{\rho_{1}(K)}^{\infty}\cdots\int_{\rho_{n}(K)}^{\infty}\det(K)^{\beta}e^{-\operatorname{tr}(KD)}\,\mathrm{d}k_{n,n}\cdots\,\mathrm{d}k_{1,1}\prod_{\begin{subarray}{c}1\leq k\leq n\\ \{v_{\mu},v_{\nu}\}\in\mathcal{E}(\mathcal{G})\end{subarray}}\mathrm{d}k_{\mu,\nu},$$  where $(\mathcal{E})$ is a $\mathcal{E}$-function.  

where ρ1(K) = 0, and for 2 ≤ µ ≤ n,

$$\rho_{\mu}(K):=\left(k_{1,\mu}\cdots k_{\mu-1,\mu}\right)(K[1,\mu-1])^{-1}\left(\begin{array}{c}{{k_{1,\mu}}}\\ {{\vdots}}\\ {{k_{\mu-1,\mu}}}\end{array}\right)\geq0.$$

Let τ = |E(G
∗)*| − |E*(G)|. We use the following version of the Fourier inversion theorem:

$$f(\mathbf{k}^{\prime},0)=\int_{\mathbb{R}^{+}}\hat{f}(\mathbf{k}^{\prime},\mathbf{t})\,\mathrm{d}\mathbf{t}=\int_{\mathbb{R}^{+}}\int_{\mathbf{R}^{\prime}}f(\mathbf{k}^{\prime},\mathbf{k}^{\prime\prime})e^{2\pi\mathbf{i}\mathbf{k}^{\prime\prime}\cdot\mathbf{t}}\,\mathrm{d}\mathbf{k}^{\prime\prime}\,\mathrm{d}\mathbf{t},\quad\forall\,\mathbf{k}^{\prime}\in\mathbb{R}^{(\frac{\pi}{2})+n-\tau}.\tag{6}$$

Alternatively, this can be considered as an application of the Plancherel theorem applied to the integrand together with the τ -dimensional Dirac delta function:

$$\delta(\mathbf{k}^{\prime\prime})=\int_{\mathbb{R}^{\tau}}e^{2\pi i\mathbf{k}^{\prime\prime}\cdot t}\,\mathrm{d}t,\quad\forall\mathbf{k}^{\prime\prime}\in\mathbb{R}^{\tau}.$$

On the entries kµ,ν , where {vµ, vν*} ∈ E*(G
∗) \ E(G), we use Equation (6) to obtain IG(*β, D*)

ρ1(K) · · ·Z ∞ ρn(K) det(K) βexp  −tr(KD) + 2πi X 1≤µ<ν≤n {vµ,vν }∈E(G ∗)\E(G) kµ,νtµ,ν  R |E(G∗)| Z ∞ = Z R τ Z  dkn,n · · · dk1,1Y 1≤µ<ν≤n {vµ,vν }∈E(G ∗) dkµ,ν Y 1≤µ<ν≤n {vµ,vν }∈E(G ∗)\E(G) dtµ,ν =1 π τ Z S(G,G∗) Z S n ++(G∗) det(K) βe − tr(K(D+iT)) dK dT = 1 π τ Z S(G,G∗) IG∗ (β, D + iT) dT.

When the graph G
∗is chordal, we use analytic continuation of (4) to write the integrand as

IG∗ (β, D + iT) = Qm µ=1 det((D + iT)[Cµ])−β− |Cµ|+1 2 Γ|Cµ| β + |Cµ|+1 2  mQ−1 ν=1 det((D + iT)[Sν])−β− |Sν |+1 2 Γ|Sν | β + |Sν |+1 2  = IG∗ (β, In) Qm µ=1 det((D + iT)[Cµ])−β− |Cµ|+1 2 mQ−1 ν=1 det((D + iT)[Sν])−β− |Sν |+1 2 , |C|+1
where det((D + iT)[C])−β−
2 ∈ C is taken to be continuous in T , and it is a real number when T is the zero matrix, for any subset C of V(G
∗).

Let G be a graph on n vertices, with a chordal completion G
∗ with τ added edges. Theorem 1.1 provides an alternative integral for the G-Wishart normalising constant whose domain is R
τ. It may be possible to simplify the integral further (especially when D = In) into an even lower dimensional one, as shown in the following example.

EXAMPLE 3.1. Let G be the complement of the cycle of length 6, as shown in Figure 1a.

G has minimum fill-in 3, and an example chordal completion with 3 extra edges is also shown in the same figure. Let β > −1 be a real number. By Theorem 1.1, IG(*β, I*6) is equal to

$$\frac{\mathcal{I}_{\mathcal{G}^{*}}(\beta,I_{6})}{\pi^{3}}\!\int_{\mathbb{R}^{3}}\!(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}+t_{1}^{2}t_{3}^{2})^{-\beta-\frac{5}{2}}(1+t_{1}^{2}+t_{2}^{2})^{-\frac{1}{2}}(1+t_{2}^{2}+t_{3}^{2})^{-\frac{1}{2}}\,\mathrm{d}t_{1}\,\mathrm{d}t_{2}\,\mathrm{d}t_{3},$$

which is a 3-dimensional integral. Substituting t2 → (1 + t 21
)
1 2 (1 + t 23
)
1 2 t2, we have

$$\mathcal{I}_{\mathcal{G}}(\beta,I_{6})=\frac{\mathcal{I}_{\mathcal{G}}\!\cdot\!(\beta,I_{6})}{\pi^{3}}\int_{\mathbb{R}}(1+t_{2}^{2})^{-\beta-\frac{5}{2}}\left(\int_{\mathbb{R}}(1+t_{1}^{2})^{-\beta-\frac{7}{2}}(1+t_{2}^{2}(1+t_{1}^{2}))^{-\frac{1}{2}}\,\mathrm{d}t_{1}\right)$$ $$\left(\int_{\mathbb{R}}(1+t_{3}^{2})^{-\beta-\frac{7}{2}}(1+t_{2}^{2}(1+t_{3}^{2}))^{-\frac{1}{2}}\,\mathrm{d}t_{3}\right)\,\mathrm{d}t_{2}.$$

An explicit formula for IG∗ (*β, I*6) can be found using (4). The integrals with respect to t1 and t3 can be solved using the integral representation of the hypergeometric function 2F1.

Thus, we are left with a one-dimensional integral:

$$(7)\ \ {\mathcal{I}}_{G}(\beta,I_{6})={\frac{\pi\Gamma_{4}\left(\beta+{\frac{5}{2}}\right)\Gamma\left(\beta+{\frac{5}{2}}\right)^{4}}{\Gamma(\beta+3)^{2}}}\int_{0}^{1}t_{2}^{\beta+2}(1-t_{2})^{-{\frac{1}{2}}}{}_{2}F_{1}\left({\frac{1}{2}},{\frac{1}{2}};\beta+3;t_{2}\right)^{2}\mathrm{d}t_{2}.$$

![8_image_0.png](8_image_0.png)

As a demonstration, we compare the numerical integration of (7) with the values obtained by Monte Carlo integration [1, 30] of Equation (1) in Figure 1b. While there is good agreement between these two approaches, ours is numerically exact (without stochastic noise) and much more computationally efficient.

4. Partitioning the missing edges, D = I. In Theorem 1.2, the integral IG(*β, I*|V(G)|)
is factorised into the product of some lower dimensional integrals for some graphs G. We show the proof for a toy example here. A formal proof of this theorem is in Appendix A.1.

EXAMPLE 4.1. Let G be the graph shown in Figure 2a. A chordal completion G
∗is also shown in the same figure. Notice that the 6 missing edges can be partitioned into 3 parts satisfying the assumptions in Theorem 1.2:

$${\mathcal{E}}_{1}=\{\{v_{1},v_{6}\},\{v_{5},v_{6}\}\},\quad{\mathcal{E}}_{2}=\{\{v_{1},v_{8}\},\{v_{7},v_{8}\}\},$$
E1 = {{v1, v6}, {v5, v6}}, E2 = {{v1, v8}, {v7, v8}}, E3 = {{v2, v3}, {v3, v4}}.
The three graphs G1,G2,G3 are shown in Figure 3. The maximal cliques of G
∗are C1 = {v1, v2, v3, v7, v8} and C2 = {v1*, . . ., v*6}, and the only minimal separator is S1 =
{v1, v2, v3}. Let β > −1 be a real number. By Theorem 1.1, we have

$${\mathcal{I}}_{\mathcal{G}}(\beta,I_{\mathrm{S}})={\frac{{\mathcal{I}}_{\mathcal{G}}\cdot(\beta,I_{\mathrm{S}})}{\pi^{6}}}\int_{S(\theta,\mathcal{L}^{\prime})}{\frac{\det((D+i T)[\mathbf{C}_{1}])^{-\beta-{\frac{|\mathbf{C}_{1}|+i}{2}}}\det((D+i T)[\mathbf{C}_{2}])^{-\beta-{\frac{|\mathbf{C}_{2}|+i}{2}}}}{\det((D+i T)[\mathbf{S}_{1}])^{-\beta-{\frac{|\mathbf{C}_{1}|+i}{2}}}}}\,\mathrm{d}T.$$
$${\mathcal{E}}_{3}=\{\{v_{2},v_{3}\},\{v_{3},v_{4}\}\}.$$

We use the variables of the missing edges as shown in Figure 2a. The above integrand is

$$\begin{array}{r l}{{}}&{{}{\frac{((1+r_{1}^{2}+r_{2}^{2})(1+s_{1}^{2}))^{-\beta-3}((1+s_{1}^{2}+s_{2}^{2})(1+t_{1}^{2}+t_{2}^{2}))^{-\beta-{\frac{7}{2}}}}{(1+s_{1}^{2})^{-\beta-2}}}}\\ {{}}&{{}}\\ {{}}&{{}=(1+t_{1}^{2}+t_{2}^{2})^{-\beta-{\frac{7}{2}}}\times(1+r_{1}^{2}+r_{2}^{2})^{-\beta-3}\times{\frac{(1+s_{1}^{2}+s_{2}^{2})^{-\beta-{\frac{7}{2}}}(1+s_{1}^{2})^{-\beta-3}}{(1+s_{1}^{2})^{-\beta-2}}},}\end{array}$$

which can be factorised into 3 separable functions. Notice that these three functions correspond exactly to the integrands of IGµ
(*β, I*8), for µ = 1, 2, 3. Indeed, by Theorem 1.1

$${\mathcal{I}}_{{\mathcal{G}}_{1}}(\beta,I_{8})={\frac{{\mathcal{I}}_{{\mathcal{G}}^{*}}(\beta,I_{8})}{\pi^{2}}}\int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\beta-{\frac{7}{2}}}\mathrm{d}t_{1}\,\mathrm{d}t_{2}={\frac{{\mathcal{I}}_{{\mathcal{G}}^{*}}(\beta,I_{8})}{\pi^{2}}}{\frac{\pi}{\beta+{\frac{5}{2}}}},$$

![9_image_0.png](9_image_0.png)

![9_image_1.png](9_image_1.png)

Fig 3: Solid edges represent the three graphs G1,G2,G3 (from left to right) in Example 4.1.

Dashed edges represent missing edges.

 $\mathcal{I}_{\mathcal{G}_2}(\beta,I_8)=$  $\mathcal{I}_{\mathcal{G}_3}(\beta,I_8)=$  Hence, in . 
(β, I8) = IG∗ (β, I8) π 2 Z R2 (1 + r 2 1 + r 2 2 ) −β−3 dr1 dr2 = IG∗ (β, I8) π 2 π β + 2 , (β, I8) = IG∗ (β, I8) π 2 Z R2 (1 + s 21 + s 22 ) −β− 72 (1 + s 21 ) −β−3 (1 + s 21 )−β−2ds1 ds2 = IG∗ (β, I8) π 2 π β + 3 . Hence, in line with Theorem 1.2, we have
IG(β, I8) = IG∗ (β, I8) π 6 π 2IG1 (β, I8) IG∗ (β, I8) π 2IG2 (β, I8) IG∗ (β, I8) π 2IG3 (β, I8) IG∗ (β, I8) = IG∗ (β, I8) −2IG1 (β, I8)IG2 (β, I8)IG3 (β, I8).
While for computing the result, we simplify as follows

$$\mathcal{I}_{\mathcal{G}}(\beta,I_{8})=\frac{\mathcal{I}_{\mathcal{G}}\cdot(\beta,I_{8})}{\pi^{6}}\frac{\pi}{\beta+\frac{5}{2}}\frac{\pi}{\beta+2}\frac{\pi}{\beta+3}=\frac{\pi^{\frac{1}{2}}\Gamma_{6}\left(\beta+\frac{7}{2}\right)\Gamma\left(\beta+\frac{5}{2}\right)\Gamma(\beta+3)}{\left(\beta+\frac{5}{2}\right)(\beta+2)(\beta+3)}.$$  **re 2b** illustrates that the above result aligns well with the values obtained using M.  
Figure 2b illustrates that the above result aligns well with the values obtained using Monte Carlo integration [1, 30].

We apply Theorem 1.2 to complete k-partite graphs and obtain an explicit formula for IG(*β, I*n). This recovers a result in [38] (Proposition 2.1) in which the graph is complete bipartite (k = 2), and generalises it.