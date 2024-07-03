# A NEW WAY TO EVALUATE G-WISHART NORMALISING CONSTANTS VIA FOURIER ANALYSIS 

By Ching Wong ${ }^{1, a}$, GiUSi MofFA ${ }^{1, b}$, ANd JACK KUiPers ${ }^{2, c}$<br>${ }^{1}$ Department of Mathematics and Computer Science, University of Basel, ${ }^{\mathrm{a}}$ ching.wong @ unibas.ch; ${ }^{\mathrm{b}}$ giusi.moffa @unibas.ch<br>${ }^{2}$ Department of Biosystems Science and Engineering, ETH Zurich, ${ }^{c}$ jack.kuipers@bsse.ethz.ch

The $\mathcal{G}$-Wishart distribution is an essential component for the Bayesian analysis of Gaussian graphical models as the conjugate prior for the precision matrix. Evaluating the marginal likelihood of such models usually requires computing high-dimensional integrals to determine the $\mathcal{G}$-Wishart normalising constant. Closed-form results are known for decomposable or chordal graphs, while an explicit representation as a formal series expansion has been derived recently for general graphs. The nested infinite sums, however, do not lend themselves to computation, remaining of limited practical value. Borrowing techniques from random matrix theory and Fourier analysis, we provide novel exact results well suited to the numerical evaluation of the normalising constant for a large class of graphs beyond chordal graphs. Furthermore, they open new possibilities for developing more efficient sampling schemes for Bayesian inference of Gaussian graphical models.

1. Introduction. The Wishart distribution [43] plays a key role in Bayesian statistics [9] as the conjugate prior for the precision (inverse covariance) matrix of multivariate Gaussians. Given independently drawn observations from a centred multivariate normals, the product of the data matrix and its transpose constitute a sample matrix from a Wishart distribution, which represents the distribution of scatter or sample covariance matrices. Since the sample data is itself a random matrix, the Wishart distribution is a classical distribution in random matrix theory [27, 24], where it is known as the Wishart-Laguerre, or Laguerre ensemble (which also extends beyond the real case to complex and quaternionic data matrices).

Random matrices were first used by Wigner [42] as simple models of complex quantum systems, like nuclear reactions, where physical observables are related to the eigenvalue spectrum. The random matrix approach is predicted to be applicable when the underlying classical dynamics are chaotic, and the inverse eigenvalues from the Wishart-Laguerre ensemble correspond to the Wigner time delays in quantum chaotic scattering [3]. Agreement between statistics of a random matrix and quantum spectra can be derived through diagrammatic perturbation theory [20] and understood via intermediate matrix integrals [31]. For the related problem of quantum transport and the Jacobi ensemble (which can be obtained from a combination of two Wisharts), full equivalence has been proven [2]. The Wishart-Laguerre ensemble is also a key model for quantum chromodynamics [39] and entanglement [26], while the eigenvalue distribution is also important for principal component analysis [16].

For high-dimensional statistics, the Wishart distribution is instrumental in aiding the modelling of multivariate continuous data with probabilistic graphical models. These are popular and powerful tools [22, 17] for compactly representing data and their dependencies with a graph, where each node encodes a variable and the edges encode conditional independence relationships. The most common types are Markov random fields, represented as undirected graphs, and Bayesian networks, represented as directed acyclic graphs (DAGs). Evaluating the marginal likelihood of each structure is a key ingredient to enable Bayesian analyses.

MSC2020 subject classifications: Primary 62H05, 60E05; secondary 62F15.

Keywords and phrases: Graphical Models, G-Wishart integrals, Bayesian inference, Multivariate distributions.

The factorisation of Bayesian networks into components involving each child and its parents, allows us to leverage the properties of the conjugate Wishart prior to easily evaluate the Gaussian integrals, and express them as ratios of the graph normalising constants of the prior and posterior distributions [8, 19]. Increasingly efficient MCMC schemes have been developed to create Bayesian samplers $[25,10,14,18,21]$ and exact samplers have been built for smaller networks [36]. With the current advances in Bayesian sampling of DAGs, we can propagate the uncertainty in both structure and parameters to obtain, for example, the posterior distribution of causal intervention effects in fully Bayesian analyses [28, 40].

In contrast, Bayesian inference for undirected graphical models has been hampered by the intractability of the marginal likelihood integrals, which we now introduce.

1.1. The $\mathcal{G}$-Wishart normalising constant. We denote by $\mathbb{S}^{n}$ the set of all $n$ by $n$ real symmetric matrices, and by $\mathbb{S}_{++}^{n}$ the set of all symmetric positive definite matrices in $\mathbb{R}^{n \times n}$. For a graph $\mathcal{G}=(\mathcal{V}(\mathcal{G}), \mathcal{E}(\mathcal{G}))$ with vertex set $\mathcal{V}(\mathcal{G})=\left\{v_{1}, \ldots, v_{n}\right\}$, let

$$
\mathbb{S}_{++}^{n}(\mathcal{G}):=\left\{M \in \mathbb{S}_{++}^{n}:\left\{v_{\mu}, v_{\nu}\right\} \notin \mathcal{E}(\mathcal{G}) \Longrightarrow m_{\mu, \nu}=0\right\}
$$

be the set of $n$ by $n$ real symmetric positive definite matrices whose entries corresponding to a pair of non-adjacent vertices are zero. The Gaussian graphical model with respect to $\mathcal{G}$ is

$$
\mathcal{M}_{\mathcal{G}}=\left\{\mathcal{N}_{n}(0, \Sigma): \Sigma^{-1} \in \mathbb{S}_{++}^{n}(\mathcal{G})\right\}
$$

the set of $n$-variate Gaussian distributions with mean zero and variance $\Sigma$ such that the precision matrix $K=\Sigma^{-1}$ is in $\mathbb{S}_{++}^{n}(\mathcal{G})$. A common choice for the prior distribution for $K \in \mathbb{S}_{++}^{n}(\mathcal{G})$ is

$$
f(K \mid \mathcal{G}) \sim \operatorname{det}(K)^{\frac{\delta-2}{2}} e^{-\frac{\operatorname{tr}(K D)}{2}}, \quad \text { where } \delta>0 \text { and } D \in \mathbb{S}_{++}^{n}
$$

as it is conjugate [35]. Let $Z \in \mathbb{R}^{n \times N}$ be a dataset with $N$ samples and $n$ variables, the marginal likelihood for the Gaussian graphical model above is then

$$
p(Z \mid \mathcal{G})=\frac{2^{-\left(\begin{array}{l}
n \\
2
\end{array}\right)}}{(2 \pi)^{\frac{n N}{2}}} \frac{\mathcal{C}_{\mathcal{G}}(\delta+N, U+D)}{\mathcal{C}_{\mathcal{G}}(\delta, D)}, \quad U=\sum_{j=1}^{N}\left(\boldsymbol{z}_{j}-\overline{\boldsymbol{z}}\right)\left(\boldsymbol{z}_{j}-\overline{\boldsymbol{z}}\right)^{\top}
$$

where $U$ is the scatter matrix (an unnormalised sample covariance), and

$$
\mathcal{C}_{\mathcal{G}}(\delta, D):=\int_{\mathbb{S}_{++}^{n}(\mathcal{G})} \operatorname{det}(K)^{\frac{\delta-2}{2}} e^{-\frac{\operatorname{tr}(K D)}{2}} \mathrm{~d} K, \quad \text { for } \delta>0 \text { and } D \in \mathbb{S}_{++}^{n}
$$

is the $\mathcal{G}$-Wishart normalising constant. As in [38], a change of variables $K \rightarrow 2 K$ allows us to simplify

$$
\mathcal{C}_{\mathcal{G}}(\delta, D)=2^{\frac{n \delta}{2}+|\mathcal{E}(\mathcal{G})|} \mathcal{I}_{\mathcal{G}}\left(\frac{\delta-2}{2}, D\right)
$$

where

$$
\mathcal{I}_{\mathcal{G}}(\beta, D):=\int_{\mathbb{S}_{++}^{n}(\mathcal{G})} \operatorname{det}(K)^{\beta} e^{-\operatorname{tr}(K D)} \mathrm{d} K, \quad \text { for } \beta>-1 \text { and } D \in \mathbb{S}_{++}^{n}
$$

Evaluating the integral $\mathcal{I}_{\mathcal{G}}(\beta, D)$ for a general graph $\mathcal{G}$ is challenging. Roverato [35] proved that the normalising constant for $\mathcal{G}$ can be factorised according to the prime components of $\mathcal{G}$, see equation (5) in Section 2 . Consequently, we only need to evaluate $\mathcal{I}_{\mathcal{G}}(\beta, D)$ for prime graphs $\mathcal{G}$. Apart from this, the only progress has come more recently from Ulher et al. [38] as an iterative method for evaluating the integral, which is, however, highly intricate and the resulting nested infinite sums do not appear to offer a viable path for evaluation.

Currently the only approaches for evaluating the $\mathcal{G}$-Wishart normalising constant for general graphs are Monte Carlo algorithms [1, 35, 30], which become increasingly computationally intensive for larger networks. Interestingly though, Roverato [35] observed and conjectured that, for a graph $\mathcal{G}$ with $n$ vertices, $D \in \mathbb{S}_{++}^{n}$ and real number $\delta>0$,

$$
\mathcal{C}_{\mathcal{G}}(\delta, D)=2^{\frac{n}{2}} \operatorname{det}\left(\operatorname{Iss}_{\mathcal{G}}(\tilde{D})\right)^{-\frac{1}{2}} \operatorname{det}(\tilde{D})^{-\frac{\delta-2}{2}} \mathcal{C}_{\mathcal{G}}\left(\delta, I_{n}\right)
$$

where $\tilde{D} \in \mathbb{S}_{++}^{n}$ is the PD-completion of $D$ with respect to $\mathcal{G}$, and $\operatorname{Iss}_{\mathcal{G}}(\tilde{D})$ is the Isserlis matrix of $\tilde{D}$ with respect to $\mathcal{G}$. If this conjecture were proved, finding the $\mathcal{G}$-Wishart normalising constant when $D$ is the identity matrix (and $\mathcal{G}$ is prime) would suffice to evaluate the constant for general matrices $D$ (and general graphs $\mathcal{G}$ ).

1.2. Known results. There are a few classes of prime graphs for which the normalising constant is known explicitly. To describe them we need some graph theory terminology. An $n$-vertex graph is complete, denoted by $\mathcal{K}_{n}$, if every pair of vertices is adjacent. For $k \geq 2$, a graph is complete $k$-partite, denoted by $\mathcal{K}_{n_{1}, \ldots, n_{k}}$, if its vertex set can be partitioned into $k$ sets, $\mathcal{V}_{1}, \ldots, \mathcal{V}_{k}$, with $\left|\mathcal{V}_{\mu}\right|=n_{\mu}$ for $1 \leq \mu \leq k$, such that $v$ is adjacent to $u$ if and only if $v$ and $u$ belong to different parts $\mathcal{V}_{\mu}$ and $\mathcal{V}_{\nu}$. When $k=2$, it is complete bipartite. A graph is chordal if it does not possess any induced cycle of length longer than three. Note that every graph has a chordal completion (i.e., a chordal supergraph on the same vertex set), as the complete graphs are chordal. The minimum fill-in of a graph is the smallest number of edges that need to be added to turn it into a chordal graph.

If $\mathcal{G}$ is an $n$-vertex prime graph (see Section 2.1 for the definition) and $\beta>-1$ is a real number, an explicit formula (involving gamma functions) for $\mathcal{I}_{\mathcal{G}}(\beta, D)$ is known when

(A1) $\mathcal{G}$ is complete and $D \in \mathbb{S}_{++}^{n}$ [6], or

(A2) $\mathcal{G}$ has minimum fill-in 1 and $D=I_{n}$ [38], or

(A3) $\mathcal{G}$ is complete bipartite and $D=I_{n}$ [38].

1.3. Bayesian inference for undirected graphs. Efficient sampling methods exist for the restricted class of decomposable (complete) graphs [13, 11, 32], thanks to their known results (A1). For general undirected graphs, without a handle on evaluating the marginal likelihood and hence the posterior of each network, Bayesian approaches have progressed by avoiding evaluating $\mathcal{I}_{\mathcal{G}}(\beta, D)$ and working instead in the joint (un-marginalised) space of networks and elements of the precision matrices $[41,23,29]$. Due to the different sized parameter spaces for different networks, these approaches build on trans-dimensional MCMC [12]. Notably, Bayesian sampling [29] outperforms the simple point estimate which can be obtained from regularised optimisation [7]. Although current Bayesian methods avoid evaluating equation (1) directly, they still require the evaluation for the simpler case where $D=I_{n}$. As with the conjecture of Roverato [35], this highlights how the identity matrix case is a key bottleneck for further progress. Recently, approximations for $D=I_{n}$ were developed and shown to offer computational advantages for Bayesian inference for undirected networks [33].

1.4. Our contribution. Borrowing inspiration from random matrix theory [15] and using tools from Fourier analysis, we show how to transform the integral $\mathcal{I}_{\mathcal{G}}(\beta, D)$ in a way that enables us to derive an explicit formula (involving gamma functions and generalised hypergeometric functions ${ }_{3} F_{2}$ ) for the $\mathcal{G}$-Wishart normalising constant when

(B1) $\mathcal{G}$ has a chordal completion $\mathcal{G}^{*}$ in which every triangle contains at most one edge from $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$ and $D=I_{|\mathcal{V}(\mathcal{G})|}$ (Corollary 4.3), or

(B2) $\mathcal{G}$ has minimum fill-in 2 and $D=I_{|\mathcal{V}(\mathcal{G})|}$ (Section 4.4), or

(B3) $\mathcal{G}$ is complete $k$-partite and $D=I_{|\mathcal{V}(\mathcal{G})|}$ (Example 4.2).

Note that (B1) contains every Turán graph $\mathcal{T}(2 n, n)$, which is a prime graph with minimum fill-in $n-1$ when $n \geq 2$ (Example 4.4).

Moreover, we show that the integral of interest can be converted into a one-dimensional real integral when

(C1) $\mathcal{G}$ is isomorphic to some $\mathcal{G}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ (defined in Section 4.3), where $m \geq 4,3 \leq$

$\ell \leq m-1$ and $k_{1}, \ldots, k_{\ell} \geq 1$, and $D=I_{m+k_{1}+\cdots+k_{\ell}}$ (Corollary 4.8), or

(C2) $\mathcal{G}$ has a chordal completion with 3 added edges that form a triangle and $D=I_{|\mathcal{V}(\mathcal{G})|}$

(Section 5.1), or

(C3) $\mathcal{G}$ is the cycle of length 6 or its complement and $D=I_{6}$ (Example 3.1, Example 4.6).

We remark that in (C1), there are infinitely many prime graphs of any given minimum fill-in greater than 2. In Appendix C, we list all 24 connected prime graphs on 6 vertices, which belong to (B1), (B2), (B3) or (C3).

Furthermore, we show that the $\mathcal{G}$-Wishart normalising constant can be written as an integral of the form

(3) $\int_{\mathbb{R}^{T}} \prod_{\left\{\alpha_{1}, \ldots, \alpha_{k}\right\} \in \mathfrak{I}}\left(1+t_{\alpha_{1}}^{2}+\cdots+t_{\alpha_{k}}^{2}\right)^{-\gamma_{\alpha_{1}}, \ldots, \alpha_{k}} \mathrm{~d} t_{1} \cdots \mathrm{d} t_{\tau}, \quad$ where $\mathfrak{I} \subseteq \mathcal{P}(\{1, \ldots, \tau\})$,

when

(D1) $\mathcal{G}$ has starry fill-ins and $D=I_{|\mathcal{V}(\mathcal{G})|}$ (Corollary 4.7), or

(D2) $\mathcal{G}$ is a gear graph and $D=I_{|\mathcal{V}(\mathcal{G})|}$ (Corollary 5.1).

The definitions of starry fill-in and gear graphs can be found in Section 4.2 and Section 5.2, respectively. We remark that (D1) contains all the cycle graphs. An example of (3) is

$$
\int_{\mathbb{R}^{3}}\left(1+t_{1}^{2}\right)^{-\frac{1}{2}}\left(1+t_{2}^{2}\right)^{\frac{9}{2}}\left(1+t_{3}^{2}\right)^{-\frac{1}{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-5}\left(1+t_{2}^{2}+t_{3}^{2}\right)^{-5} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
$$

with $\tau=3$ and $\mathfrak{I}=\{\{1\},\{2\},\{3\},\{1,2\},\{2,3\}\}$, which we encounter later in Example 4.6 for the cycle of length 6 , before reducing it down to one dimension as in (C3).

Finally, for general $D$, we obtain a one-dimensional integral when

(E1) $\mathcal{G}$ has minimum fill-in 1 and $D \in \mathbb{S}_{++}^{|\mathcal{V}(\mathcal{G})|}$ (Section 6).

Together with the prime factorisation (Equation (5) later) due to Roverato [35], the above results simplify the computation for the $\mathcal{G}$-Wishart normalising constants for many graphs. For instance, for a 2 by $m$ grid (whose prime components are $m-1$ cycles of length 4 , each with minimum fill-in of 1) and a matrix $D \in \mathbb{S}_{++}^{2 m}$, the $\mathcal{G}$-Wishart normalising constant can be written as the product of $m-1$ one-dimensional integrals. Section 6 delves deeper into the details of such integrals.

All the results mentioned above have been built upon the following theorem, in which we transform the integral $\mathcal{I}_{\mathcal{G}}(\beta, D)$ over the restricted (relative to $\mathbb{R}^{|\mathcal{E}(\mathcal{G})|+|\mathcal{V}(\mathcal{G})|}$ ) space $\mathbb{S}_{++}^{|\mathcal{V}(\mathcal{G})|}(\mathcal{G})$ into an integral over the Euclidean space $\mathbb{R}^{\tau}$, where $\tau$ is the number of edges needed for a known chordal completion of $\mathcal{G}$. The matrix Dirac delta function (Fourier transform of 1), as used in [15], is employed. The proof of this result can be found in Section 3.

THEOREM 1.1. Let $\mathcal{G}$ be a proper subgraph of $\mathcal{G}^{*}$, both on the vertex set $\left\{v_{1}, \ldots, v_{n}\right\}$. Let $\beta>-1$ be a real number and $D \in \mathbb{S}_{++}^{n}$. Then,

$$
\mathcal{I}_{\mathcal{G}}(\beta, D)=\frac{1}{\pi^{\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \mathcal{I}_{\mathcal{G}^{*}}(\beta, D+i T) \mathrm{d} T
$$

where

$$
\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right):=\left\{T \in \mathbb{S}^{n}: \mu=\nu \text { or }\left\{v_{\mu}, v_{\nu}\right\} \in \mathcal{E}(\mathcal{G}) \text { or }\left\{v_{\mu}, v_{\nu}\right\} \notin \mathcal{E}\left(\mathcal{G}^{*}\right) \Longrightarrow t_{\mu, \nu}=0\right\}
$$

In particular, if $\mathcal{G}^{*}$ is a chordal completion of $\mathcal{G}$, then

$$
\mathcal{I}_{\mathcal{G}}(\beta, D)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left((D+i T)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left((D+i T)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \mathrm{~d} T
$$

where $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m} \subseteq \mathcal{V}(\mathcal{G})$ are the maximal cliques of $\mathcal{G}^{*}$ and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1} \subseteq \mathcal{V}(\mathcal{G})$ are the minimal separators (see Section 2 for definitions).

Note that $\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$ is the set of $n$ by $n$ symmetric real matrices, in which every entry is equal to zero unless it corresponds to an edge in $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$. Thus, the number of variables in $\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$ is $\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|$. It follows that an integral with domain $\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right.$ ) (Lebesgue measure) is the same as an integral over $\mathbb{R}^{\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|}$.

While the normalising constant can be factorised according to the prime components of a graph, under certain assumptions, the integral $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{|\mathcal{V}(\mathcal{G})|}\right)$ can be further factorised for some prime graphs $\mathcal{G}$, since $\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{|\mathcal{V}(\mathcal{G})|}+i T\right)$ can be written as the product of some separable functions. The following theorem characterises these graphs. In Section 4 we illustrate this result using a toy example (Example 4.1), while a formal proof is given in Appendix A.1.

THEOREM 1.2. Let $\mathcal{G}$ be a graph on $n$ vertices and let $\mathcal{G}^{*}$ be a chordal completion. Suppose that there exists a partition of the missing edges $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})=\mathcal{E}_{1} \sqcup \cdots \sqcup \mathcal{E}_{k}$ such that for $1 \leq \mu<\nu \leq k$, either

- $\mathcal{V}_{\mu} \cap \mathcal{V}_{\nu}=\emptyset$ or
- $\left|\mathcal{V}_{\mu} \cap \mathcal{V}_{\nu}\right|=1$ and there is no edge in $\mathcal{G}^{*}$ between the sets $\mathcal{V}_{\mu} \backslash \mathcal{V}_{\nu}$ and $\mathcal{V}_{\nu} \backslash \mathcal{V}_{\mu}$,

where $\mathcal{V}_{\xi} \subseteq \mathcal{V}(\mathcal{G})$ is the vertex set associated with the edges in $\mathcal{E}_{\xi}$, for $\xi=1, \ldots, k$.

Let $\beta>-1$ be a real number. Then,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)^{1-k} \prod_{\xi=1}^{k} \mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right)
$$

where $\mathcal{G}_{\xi}$ is the graph obtained from $\mathcal{G}^{*}$ by removing the edges in $\mathcal{E}_{\xi}$, for $1 \leq \xi \leq k$.

2. Preliminaries. In this paper, all graphs $\mathcal{G}=(\mathcal{V}(\mathcal{G}), \mathcal{E}(\mathcal{G}))$ are assumed to be simple and undirected. We denote by $\mathcal{N}_{\mathcal{G}}(v) \subseteq \mathcal{V}(\mathcal{G})$ the set of all the neighbours of the vertex $v$ in graph $\mathcal{G}$. A set $\mathrm{C} \subseteq \mathcal{V}(\mathcal{G})$ is a clique of $\mathcal{G}$ if two vertices $u$ and $v$ are adjacent whenever they are both in $\mathrm{C}$. A clique $\mathrm{C}$ of $\mathcal{G}$ is considered maximal if there is no clique in $\mathcal{G}$ that strictly contains $\mathrm{C}$. A graph $\mathcal{G}$ is connected if for any pair of vertices $u, v \in \mathcal{V}(\mathcal{G})$, one can travel from $u$ to $v$ via edges of $\mathcal{G}$. For a subset $\mathcal{V}^{\prime} \subseteq \mathcal{V}(\mathcal{G})$, we use $\mathcal{G}\left[\mathcal{V}^{\prime}\right]$ to denote the induced subgraph of $\mathcal{G}$ formed from the vertices in $\mathcal{V}^{\prime}$. A set $\mathrm{S} \subseteq \mathcal{V}(\mathcal{G})$ is a separator of a (connected) graph $\mathcal{G}$ if the induced subgraph $\mathcal{G}[\mathcal{V}(\mathcal{G}) \backslash \mathrm{S}]$ is not connected. A separator $\mathrm{S}$ is considered minimal if there is no separator in $\mathcal{G}$ that is strictly contained in $\mathrm{S}$. For a graph $\mathcal{G}$ with vertex set $\mathcal{V}(\mathcal{G})=\left\{v_{1}, \ldots, v_{n}\right\}$ and a matrix $D$ in $\mathbb{S}_{++}^{n}$, the matrix $D[\mathrm{C}] \in \mathbb{S}_{++}^{|\mathrm{C}|}$, where $\mathcal{C} \subseteq \mathcal{V}(\mathcal{G})$, is the submatrix of $D$ obtained by the corresponding rows and columns.

In this section, we highlight some definitions and known results about chordal graphs. For a comprehensive overview, we refer to [22].

2.1. Graph decomposition. A graph $\mathcal{G}$ is prime if it contains no separator that is a clique. Examples of prime graphs include complete graphs, cycle graphs and grid graphs. Given a non-prime graph $\mathcal{G}$, one can select a maximal clique $C$ that separates the graph into two nonempty sets $\mathrm{A}$ and $\mathrm{B}$. Then, we say that $\mathcal{G}$ is decomposed into two components $\mathcal{G}[\mathrm{A} \cup \mathrm{C}]$ and $\mathcal{G}[\mathrm{B} \cup \mathrm{C}]$. Continuing this process, the graph $\mathcal{G}$ can be uniquely decomposed into its prime components. For example, the 2 by $m$ grid can be decomposed into $m-1$ cycles of length 4 .

2.2. Perfect sequence of prime components. Let $\mathcal{G}$ be a graph with $m$ prime components. An ordering of the prime components of $\mathcal{G}$, say $\mathcal{G}\left[\mathrm{P}_{1}\right], \ldots, \mathcal{G}\left[\mathrm{P}_{m}\right]$, is a perfect sequence of prime components if, for every $1 \leq \mu \leq m-1$, there exists $\nu \leq \mu$ such that

$$
\left(\mathrm{P}_{1} \cup \cdots \cup \mathrm{P}_{\mu}\right) \cap \mathrm{P}_{\mu+1} \subseteq \mathrm{P}_{\nu}
$$

which is known as the running intersection property. For simplicity in notation, we slightly abuse the representation by referring to $\mathrm{P}_{1}, \ldots, \mathrm{P}_{m}$ as a perfect sequence of prime components, as opposed to using $\mathcal{G}\left[\mathrm{P}_{1}\right], \ldots, \mathcal{G}\left[\mathrm{P}_{m}\right]$. It is known that each graph possesses at least one perfect sequence of prime components.

Given a perfect sequence of prime components $\mathrm{P}_{1}, \ldots, \mathrm{P}_{m}$ of a graph $\mathcal{G}$, the sets

$$
\mathrm{S}_{\nu}:=\left(\mathrm{P}_{1} \cup \cdots \cup \mathrm{P}_{\nu}\right) \cap \mathrm{P}_{\nu+1}, \quad \text { where } 1 \leq \nu \leq m-1
$$

are the corresponding set of separators. It is well known that the induced subgraphs $\mathcal{G}\left[\mathrm{S}_{\nu}\right]$ are complete and that the multiset $\left\{\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}\right\}$ is invariant to the choice of the perfect sequence of prime components. In this paper, keeping in mind that some of these sets might be identical, we refer to the sets $S_{1}, \ldots, S_{m-1}$ as the minimal separators of $\mathcal{G}$.

2.3. Chordal graphs. A graph is considered decomposable if its prime components are all complete. These graphs can be characterised by their graphical properties; specifically, they are graphs in which all induced cycles have length 3. Equivalently, every cycle in these graphs with length greater than three contains at least one chord, which refers to an edge connecting two vertices within the cycle that is not part of the cycle itself. Thus, decomposable graphs are also known as chordal graphs, and here we will use the term chordal graphs.

For chordal graphs, we write perfect sequence of cliques $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ in place of perfect sequence of prime components $\mathrm{P}_{1}, \ldots, \mathrm{P}_{m}$, to emphasise that the vertex sets of the prime components are cliques. We remark that the prime components of a chordal graph are precisely its maximal cliques.

2.4. Chordal completion. Given any graph $\mathcal{G}$, a graph $\mathcal{G}^{*}$ on the same vertex set is a chordal completion of $\mathcal{G}$ if $\mathcal{G}^{*}$ is chordal, and $\mathcal{G}$ is a subgraph of $\mathcal{G}^{*}$. When there is no ambiguity, we refer to the edges $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$ the missing edges. Our results later rely heavily on finding a chordal completion (of a given graph) with some nice properties. In particular, the fewer the edges in the chordal completion, the lower the dimension of the integral in Theorem 1.1. Finding a chordal completion of a given graph with the minimum number of edges is known as the minimum chordal completion problem or the minimum fill-in problem, which is NP-complete [44]. Several linear-time algorithms, including Lexicographic BreadthFirst Search [4, 34] and Maximum Cardinality Search [37], have been proposed for finding chordal completions of graphs, though they do not always find one with minimum fill-in.

2.5. Factorisation of $\mathcal{G}$-Wishart normalising constant. For a complete graph $\mathcal{K}_{n}$, the $\mathcal{G}$ Wishart normalising constant is the normalising constant for a Wishart distribution:

$$
\mathcal{I}_{\mathcal{K}_{n}}(\beta, D)=\int_{\mathbb{S}_{++}^{n}} \operatorname{det}(K)^{\beta} e^{-\operatorname{tr}(K D)} \mathrm{d} K=\operatorname{det}(D)^{-\beta-\frac{n+1}{2}} \Gamma_{n}\left(\beta+\frac{n+1}{2}\right)
$$

where $\Gamma_{k}(a)$ is the multivariate gamma function

$$
\Gamma_{k}(a):=\pi^{\frac{k(k-1)}{4}} \prod_{\mu=1}^{k} \Gamma\left(a+\frac{1-\mu}{2}\right), \quad \text { for } a>\frac{k-1}{2}
$$

Let $\mathcal{G}^{*}$ be a chordal graph. Let $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ be the maximal cliques and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ be the minimal separators. Then, it is known [5] that the integral $\mathcal{I}_{\mathcal{G}^{*}}(\beta, D)$ can be factorised as

$$
\mathcal{I}_{\mathcal{G}^{*}}(\beta, D)=\frac{\prod_{\mu=1}^{m} \mathcal{I}_{\mathcal{G}^{*}\left[\mathrm{C}_{\mu}\right]}\left(\beta, D\left[\mathrm{C}_{\mu}\right]\right)}{\prod_{\nu=1}^{m-1} \mathcal{I}_{\mathcal{G}^{*}\left[\mathrm{~S}_{\nu}\right]}\left(\beta, D\left[\mathrm{~S}_{\nu}\right]\right)}=\frac{\prod_{\mu=1}^{m} \operatorname{det}\left(D\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}} \Gamma_{\left|\mathrm{C}_{\mu}\right|}\left(\beta+\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}\right)}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(D\left[\mathrm{~S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}} \Gamma_{\left|\mathrm{S}_{\nu}\right|}\left(\beta+\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}\right)}
$$

Roverato [35] generalised this factorisation to general graphs $\mathcal{G}$ :

$$
\mathcal{I}_{\mathcal{G}}(\beta, D)=\frac{\prod_{\mu=1}^{m} \mathcal{I}_{\mathcal{G}\left[\mathrm{P}_{\mu}\right]}\left(\beta, D\left[\mathrm{P}_{\mu}\right]\right)}{\prod_{\nu=1}^{m-1} \mathcal{I}_{\mathcal{G}\left[\mathrm{S}_{\nu}\right]}\left(\beta, D\left[\mathrm{~S}_{\nu}\right]\right)}=\frac{\prod_{\mu=1}^{m} \mathcal{I}_{\mathcal{G}\left[\mathrm{P}_{\mu}\right]}\left(\beta, D\left[\mathrm{P}_{\mu}\right]\right)}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(D\left[\mathrm{~S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}} \Gamma_{\left|\mathrm{S}_{\nu}\right|}\left(\beta+\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}\right)}
$$

where $\mathrm{P}_{1}, \ldots, \mathrm{P}_{m}$ are the prime components of $\mathcal{G}$ and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ are the minimal separators. This is why we only need to find the normalising constants for prime graphs. We remark that (5) can be easily derived from Theorem 1.1, by separating the variables.

3. Transforming the integral using Fourier analysis. We provide an example after proving Theorem 1.1.

PROOF OF THEOREM 1.1. We begin with a parametrised form of the domain $\mathbb{S}_{++}^{n}(\mathcal{G})$ in the integral $\mathcal{I}_{\mathcal{G}}(\beta, D)$ (defined in (1)) and write

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}(\beta, D) & =\int_{\mathbb{S}_{++}^{n}(\mathcal{G})} \operatorname{det}(K)^{\beta} e^{-\operatorname{tr}(K D)} \mathrm{d} K \\
& =\int_{\mathbb{R}^{|\mathcal{E}(\mathcal{G})|}} \int_{\rho_{1}(K)}^{\infty} \cdots \int_{\rho_{n}(K)}^{\infty} \operatorname{det}(K)^{\beta} e^{-\operatorname{tr}(K D)} \mathrm{d} k_{n, n} \cdots \mathrm{d} k_{1,1} \prod_{\substack{1 \leq \mu<\nu \leq n \\
\left\{v_{\mu}, v_{\nu}\right\} \in \mathcal{E}(\mathcal{G})}} \mathrm{d} k_{\mu, \nu}
\end{aligned}
$$

where $\rho_{1}(K)=0$, and for $2 \leq \mu \leq n$,

$$
\rho_{\mu}(K):=\left(k_{1, \mu} \cdots k_{\mu-1, \mu}\right)(K[1, \mu-1])^{-1}\left(\begin{array}{c}
k_{1, \mu} \\
\vdots \\
k_{\mu-1, \mu}
\end{array}\right) \geq 0
$$

Let $\tau=\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|$. We use the following version of the Fourier inversion theorem:

$$
f\left(\boldsymbol{k}^{\prime}, 0\right)=\int_{\mathbb{R}^{\tau}} \hat{f}\left(\boldsymbol{k}^{\prime}, \boldsymbol{t}\right) \mathrm{d} \boldsymbol{t}=\int_{\mathbb{R}^{\tau}} \int_{\boldsymbol{R}^{\tau}} f\left(\boldsymbol{k}^{\prime}, \boldsymbol{k}^{\prime \prime}\right) e^{2 \pi i \boldsymbol{k}^{\prime \prime} \cdot \boldsymbol{t}} \mathrm{d} \boldsymbol{k}^{\prime \prime} \mathrm{d} \boldsymbol{t}, \quad \forall \boldsymbol{k}^{\prime} \in \mathbb{R}^{\left(\begin{array}{c}
n \\
2
\end{array}\right)+n-\tau}
$$

Alternatively, this can be considered as an application of the Plancherel theorem applied to the integrand together with the $\tau$-dimensional Dirac delta function:

$$
\delta\left(\boldsymbol{k}^{\prime \prime}\right)=\int_{\mathbb{R}^{\tau}} e^{2 \pi i \boldsymbol{k}^{\prime \prime} \cdot \boldsymbol{t}} \mathrm{d} \boldsymbol{t}, \quad \forall \boldsymbol{k}^{\prime \prime} \in \mathbb{R}^{\tau}
$$

On the entries $k_{\mu, \nu}$, where $\left\{v_{\mu}, v_{\nu}\right\} \in \mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$, we use Equation (6) to obtain $\mathcal{I}_{\mathcal{G}}(\beta, D)$

$$
\begin{aligned}
& =\int_{\mathbb{R}^{\tau}} \int_{\mathbb{R}^{\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|}} \int_{\rho_{1}(K)}^{\infty} \cdots \int_{\rho_{n}(K)}^{\infty} \operatorname{det}(K)^{\beta} \exp \left(-\operatorname{tr}(K D)+2 \pi i \sum_{\substack{1 \leq \mu<\nu \leq n \\
\left\{v_{\mu}, v_{\nu}\right\} \in \mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})}} k_{\mu, \nu} t_{\mu, \nu}\right) \\
& \quad \mathrm{d} k_{n, n} \cdots \mathrm{d} k_{1,1} \prod_{\substack{1 \leq \mu \leq \nu \leq n \\
\left\{v_{\mu}, \nu_{\nu}\right\} \in \mathcal{\mathcal { E }}\left(\mathcal{G}^{*}\right)}} \mathrm{d} k_{\mu, \nu} \prod_{\substack{1 \leq \mu<\nu \leq n \\
\left\{v_{\mu}, v_{\nu}\right\} \in \mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})}} \mathrm{d} t_{\mu, \nu} \\
& =\frac{1}{\pi^{\tau}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \int_{\mathbb{S}_{++}^{n}\left(\mathcal{G}^{*}\right)} \operatorname{det}(K)^{\beta} e^{-\operatorname{tr}(K(D+i T))} \mathrm{d} K \mathrm{~d} T=\frac{1}{\pi^{\tau}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \mathcal{I}_{\mathcal{G}^{*}}(\beta, D+i T) \mathrm{d} T
\end{aligned}
$$

When the graph $\mathcal{G}^{*}$ is chordal, we use analytic continuation of (4) to write the integrand as

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}^{*}}(\beta, D+i T)= & \frac{\prod_{\mu=1}^{m} \operatorname{det}\left((D+i T)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}} \Gamma_{\left|\mathrm{C}_{\mu}\right|}\left(\beta+\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}\right)}{\prod_{\nu=1}^{m-1} \operatorname{det}\left((D+i T)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}} \Gamma_{\left|\mathrm{S}_{\nu}\right|}\left(\beta+\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}\right)} \\
= & \mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right) \frac{\prod_{\mu=1}^{m} \operatorname{det}\left((D+i T)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left((D+i T)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}}
\end{aligned}
$$

where $\operatorname{det}((D+i T)[\mathbb{C}])^{-\beta-\frac{|| c \mid+1}{2}} \in \mathbb{C}$ is taken to be continuous in $T$, and it is a real number when $T$ is the zero matrix, for any subset $\mathrm{C}$ of $\mathcal{V}\left(\mathcal{G}^{*}\right)$.

Let $\mathcal{G}$ be a graph on $n$ vertices, with a chordal completion $\mathcal{G}^{*}$ with $\tau$ added edges. Theorem 1.1 provides an alternative integral for the $\mathcal{G}$-Wishart normalising constant whose domain is $\mathbb{R}^{\tau}$. It may be possible to simplify the integral further (especially when $D=I_{n}$ ) into an even lower dimensional one, as shown in the following example.

EXAMPLE 3.1. Let $\mathcal{G}$ be the complement of the cycle of length 6, as shown in Figure 1a. $\mathcal{G}$ has minimum fill-in 3 , and an example chordal completion with 3 extra edges is also shown in the same figure. Let $\beta>-1$ be a real number. By Theorem 1.1, $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)$ is equal to

$$
\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{6}\right)}{\pi^{3}} \int_{\mathbb{R}^{3}}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}+t_{1}^{2} t_{3}^{2}\right)^{-\beta-\frac{5}{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\frac{1}{2}}\left(1+t_{2}^{2}+t_{3}^{2}\right)^{-\frac{1}{2}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
$$

which is a 3-dimensional integral. Substituting $t_{2} \rightarrow\left(1+t_{1}^{2}\right)^{\frac{1}{2}}\left(1+t_{3}^{2}\right)^{\frac{1}{2}} t_{2}$, we have

$$
\begin{gathered}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{6}\right)}{\pi^{3}} \int_{\mathbb{R}}\left(1+t_{2}^{2}\right)^{-\beta-\frac{5}{2}}\left(\int_{\mathbb{R}}\left(1+t_{1}^{2}\right)^{-\beta-\frac{7}{2}}\left(1+t_{2}^{2}\left(1+t_{1}^{2}\right)\right)^{-\frac{1}{2}} \mathrm{~d} t_{1}\right) \\
\left(\int_{\mathbb{R}}\left(1+t_{3}^{2}\right)^{-\beta-\frac{7}{2}}\left(1+t_{2}^{2}\left(1+t_{3}^{2}\right)\right)^{-\frac{1}{2}} \mathrm{~d} t_{3}\right) \mathrm{d} t_{2}
\end{gathered}
$$

An explicit formula for $\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{6}\right)$ can be found using (4). The integrals with respect to $t_{1}$ and $t_{3}$ can be solved using the integral representation of the hypergeometric function ${ }_{2} F_{1}$. Thus, we are left with a one-dimensional integral:

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)=\frac{\pi \Gamma_{4}\left(\beta+\frac{5}{2}\right) \Gamma\left(\beta+\frac{5}{2}\right)^{4}}{\Gamma(\beta+3)^{2}} \int_{0}^{1} t_{2}^{\beta+2}\left(1-t_{2}\right)^{-\frac{1}{2}}{ }_{2} F_{1}\left(\frac{1}{2}, \frac{1}{2} ; \beta+3 ; t_{2}\right)^{2} \mathrm{~d} t_{2}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-09.jpg?height=366&width=398&top_left_y=234&top_left_x=576)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-09.jpg?height=341&width=632&top_left_y=239&top_left_x=1061)

(b)

Fig 1: (a) Solid edges represent those in the complement of the cycle of length 6 . Dashed edges represent missing edges. (b) Violin plot of the estimates of the value of $\log \mathcal{C}_{\mathcal{G}}\left(20, I_{6}\right)$, using Monte Carlo integration [1, 30] with 1000 samples for 200 different seeds. They agree well with our result from evaluating (7) numerically, represented by the horizontal line, which has the benefit of avoiding stochastic noise and higher computational efficiency.

As a demonstration, we compare the numerical integration of (7) with the values obtained by Monte Carlo integration [1, 30] of Equation (1) in Figure 1b. While there is good agreement between these two approaches, ours is numerically exact (without stochastic noise) and much more computationally efficient.

4. Partitioning the missing edges, $\boldsymbol{D}=\boldsymbol{I}$. In Theorem 1.2, the integral $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{|\mathcal{V}(\mathcal{G})|}\right)$ is factorised into the product of some lower dimensional integrals for some graphs $\mathcal{G}$. We show the proof for a toy example here. A formal proof of this theorem is in Appendix A.1.

EXAMPLE 4.1. Let $\mathcal{G}$ be the graph shown in Figure 2a. A chordal completion $\mathcal{G}^{*}$ is also shown in the same figure. Notice that the 6 missing edges can be partitioned into 3 parts satisfying the assumptions in Theorem 1.2:

$$
\mathcal{E}_{1}=\left\{\left\{v_{1}, v_{6}\right\},\left\{v_{5}, v_{6}\right\}\right\}, \quad \mathcal{E}_{2}=\left\{\left\{v_{1}, v_{8}\right\},\left\{v_{7}, v_{8}\right\}\right\}, \quad \mathcal{E}_{3}=\left\{\left\{v_{2}, v_{3}\right\},\left\{v_{3}, v_{4}\right\}\right\}
$$

The three graphs $\mathcal{G}_{1}, \mathcal{G}_{2}, \mathcal{G}_{3}$ are shown in Figure 3. The maximal cliques of $\mathcal{G}^{*}$ are $\mathrm{C}_{1}=\left\{v_{1}, v_{2}, v_{3}, v_{7}, v_{8}\right\}$ and $\mathrm{C}_{2}=\left\{v_{1}, \ldots, v_{6}\right\}$, and the only minimal separator is $\mathrm{S}_{1}=$ $\left\{v_{1}, v_{2}, v_{3}\right\}$. Let $\beta>-1$ be a real number. By Theorem 1.1, we have

$\mathcal{I}_{\mathcal{G}}\left(\beta, I_{8}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{6}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\operatorname{det}\left((D+i T)\left[\mathrm{C}_{1}\right]\right)^{-\beta-\frac{\left|\mathrm{I}_{1}\right|+1}{2}} \operatorname{det}\left((D+i T)\left[\mathrm{C}_{2}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{2}\right|+1}{2}}}{\operatorname{det}\left((D+i T)\left[\mathrm{S}_{1}\right]\right)^{-\beta-\frac{\left|S_{1}\right|+1}{2}}} \mathrm{~d} T$.

We use the variables of the missing edges as shown in Figure 2a. The above integrand is

$$
\begin{aligned}
& \frac{\left(\left(1+r_{1}^{2}+r_{2}^{2}\right)\left(1+s_{1}^{2}\right)\right)^{-\beta-3}\left(\left(1+s_{1}^{2}+s_{2}^{2}\right)\left(1+t_{1}^{2}+t_{2}^{2}\right)\right)^{-\beta-\frac{7}{2}}}{\left(1+s_{1}^{2}\right)^{-\beta-2}} \\
= & \left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\beta-\frac{7}{2}} \times\left(1+r_{1}^{2}+r_{2}^{2}\right)^{-\beta-3} \times \frac{\left(1+s_{1}^{2}+s_{2}^{2}\right)^{-\beta-\frac{7}{2}}\left(1+s_{1}^{2}\right)^{-\beta-3}}{\left(1+s_{1}^{2}\right)^{-\beta-2}}
\end{aligned}
$$

which can be factorised into 3 separable functions. Notice that these three functions correspond exactly to the integrands of $\mathcal{I}_{\mathcal{G}_{\mu}}\left(\beta, I_{8}\right)$, for $\mu=1,2,3$. Indeed, by Theorem 1.1

$$
\mathcal{I}_{\mathcal{G}_{1}}\left(\beta, I_{8}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{2}} \int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\beta-\frac{7}{2}} \mathrm{~d} t_{1} \mathrm{~d} t_{2}=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{2}} \frac{\pi}{\beta+\frac{5}{2}}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-10.jpg?height=363&width=529&top_left_y=233&top_left_x=478)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-10.jpg?height=347&width=640&top_left_y=236&top_left_x=1016)

(b)

Fig 2: (a) Solid edges represent the graph $\mathcal{G}$ in Example 4.1. Dashed edges represent the missing edges, which are partitioned into 3 parts with different colours. (b) Violin plot of the estimates of the value of $\log \mathcal{C}_{\mathcal{G}}\left(20, I_{8}\right)$, using Monte Carlo integration [1, 30] with 1000 samples and for 200 different seeds. They align well with our exact result (horizontal line).

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-10.jpg?height=339&width=1333&top_left_y=950&top_left_x=385)

Fig 3: Solid edges represent the three graphs $\mathcal{G}_{1}, \mathcal{G}_{2}, \mathcal{G}_{3}$ (from left to right) in Example 4.1. Dashed edges represent missing edges.

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}_{2}}\left(\beta, I_{8}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{2}} \int_{\mathbb{R}^{2}}\left(1+r_{1}^{2}+r_{2}^{2}\right)^{-\beta-3} \mathrm{~d} r_{1} \mathrm{~d} r_{2}=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{2}} \frac{\pi}{\beta+2} \\
& \mathcal{I}_{\mathcal{G}_{3}}\left(\beta, I_{8}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{2}} \int_{\mathbb{R}^{2}} \frac{\left(1+s_{1}^{2}+s_{2}^{2}\right)^{-\beta-\frac{7}{2}}\left(1+s_{1}^{2}\right)^{-\beta-3}}{\left(1+s_{1}^{2}\right)^{-\beta-2}} \mathrm{~d} s_{1} \mathrm{~d} s_{2}=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{2}} \frac{\pi}{\beta+3}
\end{aligned}
$$

Hence, in line with Theorem 1.2, we have

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{8}\right) & =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{6}} \frac{\pi^{2} \mathcal{I}_{\mathcal{G}_{1}}\left(\beta, I_{8}\right)}{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)} \frac{\pi^{2} \mathcal{I}_{\mathcal{G}_{2}}\left(\beta, I_{8}\right)}{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)} \frac{\pi^{2} \mathcal{I}_{\mathcal{G}_{3}}\left(\beta, I_{8}\right)}{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)} \\
& =\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)^{-2} \mathcal{I}_{\mathcal{G}_{1}}\left(\beta, I_{8}\right) \mathcal{I}_{\mathcal{G}_{2}}\left(\beta, I_{8}\right) \mathcal{I}_{\mathcal{G}_{3}}\left(\beta, I_{8}\right)
\end{aligned}
$$

While for computing the result, we simplify as follows

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{8}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{8}\right)}{\pi^{6}} \frac{\pi}{\beta+\frac{5}{2}} \frac{\pi}{\beta+2} \frac{\pi}{\beta+3}=\frac{\pi^{\frac{1}{2}} \Gamma_{6}\left(\beta+\frac{7}{2}\right) \Gamma\left(\beta+\frac{5}{2}\right) \Gamma(\beta+3)}{\left(\beta+\frac{5}{2}\right)(\beta+2)(\beta+3)}
$$

Figure $2 \mathrm{~b}$ illustrates that the above result aligns well with the values obtained using Monte Carlo integration $[1,30]$.

We apply Theorem 1.2 to complete $k$-partite graphs and obtain an explicit formula for $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)$. This recovers a result in [38] (Proposition 2.1) in which the graph is complete bipartite $(k=2)$, and generalises it.

EXAMPLE 4.2. Let $\mathcal{G} \cong \mathcal{K}_{n_{1}, \ldots, n_{k}}$ be a complete $k$-partite graph on $n=n_{1}+\cdots+n_{k}$ vertices. Let $\mathcal{G}^{*} \cong \mathcal{K}_{n}$ be the complete graph on the same vertex set, which is a chordal completion of $\mathcal{G}$. Let $\beta>-1$ be a real number. For $1 \leq \xi \leq k$, let $\tau_{\xi}=\left(\begin{array}{c}n_{\xi} \\ 2\end{array}\right)$. Let $\tau=\tau_{1}+$ $\cdots+\tau_{k}$ be the total number of missing edges. By Theorem 1.2,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)^{1-k} \prod_{\xi=1}^{k} \mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right)
$$

where $\mathcal{G}_{\xi}$ is the graph obtained from the complete graph $\mathcal{K}_{n}$ by removing all edges whose end points both belong to some $n_{\xi}$ vertices. Since $\mathcal{G}^{*}$ is complete, we have

$$
\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)=\Gamma_{n}\left(\beta+\frac{n+1}{2}\right)
$$

It remains to find $\mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right)$. Let $\tilde{\mathcal{G}_{\xi}}$ be the empty graph on $n_{\xi}$ vertices. By Theorem 1.1,

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right) & =\frac{\mathcal{I}_{\mathcal{K}_{n}}\left(\beta, I_{n}\right)}{\pi^{\tau_{\xi}}} \int_{\mathbb{S}\left(\mathcal{G}_{\xi}, \mathcal{K}_{n}\right)} \operatorname{det}\left(I_{n}+i T\right)^{-\beta-\frac{n+1}{2}} \mathrm{~d} T \\
& =\frac{\mathcal{I}_{\mathcal{K}_{n}}\left(\beta, I_{n}\right)}{\pi^{\tau_{\xi}}} \int_{\mathbb{S}\left(\tilde{\mathcal{G}}_{\xi}, \mathcal{K}_{n_{\xi}}\right)} \operatorname{det}\left(I_{n_{\xi}}+i T\right)^{-\left(\beta+\frac{n-n_{\xi}}{2}\right)-\frac{n_{\xi}+1}{2}} \mathrm{~d} T \\
& =\frac{\mathcal{I}_{\mathcal{K}_{n}}\left(\beta, I_{n}\right)}{\pi^{\tau_{\xi}}} \frac{\mathcal{I}_{\tilde{\mathcal{G}}_{\xi}}\left(\beta+\frac{n-n_{\xi}}{2}, I_{n_{\xi}}\right) \pi^{\tau_{\xi}}}{\mathcal{I}_{\mathcal{K}_{n_{\xi}}}\left(\beta+\frac{n-n_{\xi}}{2}, I_{n_{\xi}}\right)} \\
& =\Gamma_{n}\left(\beta+\frac{n+1}{2}\right) \frac{\Gamma\left(\beta+\frac{n-n_{\xi}}{2}+1\right)^{n_{\xi}}}{\Gamma_{n_{\xi}}\left(\beta+\frac{n-n_{\xi}}{2}+\frac{n_{\xi}+1}{2}\right)}
\end{aligned}
$$

Altogether, we have

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\Gamma_{n}\left(\beta+\frac{n+1}{2}\right) \prod_{\xi=1}^{k} \frac{\Gamma\left(\beta+\frac{n-n_{\xi}}{2}+1\right)^{n_{\xi}}}{\Gamma_{n_{\xi}}\left(\beta+\frac{n+1}{2}\right)}
$$

4.1. No triangle contains two missing edges. For graphs $\mathcal{G}$ on $n$ vertices with minimum fill-in 1, a result in [38] (Theorem 2.5) states that, for real number $\beta>-1$,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\frac{1}{2}}} \frac{\Gamma\left(\beta+\frac{w+2}{2}\right)}{\Gamma\left(\beta+\frac{w+3}{2}\right)}
$$

where $\mathcal{G}^{*}$ is a chordal completion of $\mathcal{G}$ with one additional edge, and $w$ is the number of common neighbours of the end vertices of the added edge. We give an alternative proof of this result using Theorem 1.1 in Appendix A.2, and generalise to arbitrary $D$ in Section 6.

In this subsection, we combine Theorem 1.2 and (9) to write an explicit formula for $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{|\mathcal{V}(\mathcal{G})|}\right)$ for graphs $\mathcal{G}$ with a chordal completion $\mathcal{G}^{*}$ such that no triangle in $\mathcal{G}^{*}$ has more than one missing edge; i.e. in every clique of $\mathcal{G}^{*}$, the missing edges are vertex-disjoint.

COROLLary 4.3. Let $\mathcal{G}$ be a graph with vertex set $\mathcal{V}(\mathcal{G})=\left\{v_{1}, \ldots, v_{n}\right\}$. Let $\mathcal{G}^{*}$ be a chordal completion of $\mathcal{G}$. Suppose that every triangle in $\mathcal{G}^{*}$ contains at most one edge from $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$. Let $\beta>-1$ be a real number. Then,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\frac{\left.\mid \mathcal{G} \mathcal{G}^{*}\right)|-| \mathcal{G}(\mathcal{G}) \mid}{2}}} \prod_{e \in \mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})} \frac{\Gamma\left(\beta+\frac{w_{e}+2}{2}\right)}{\Gamma\left(\beta+\frac{w_{e}+3}{2}\right)}
$$

where $w_{e}$ is the number of common neighbours of the end vertices of the edge e in $\mathcal{G}^{*}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-12.jpg?height=347&width=398&top_left_y=236&top_left_x=576)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-12.jpg?height=357&width=634&top_left_y=220&top_left_x=1060)

(b)

Fig 4: (a) Solid edges are those in $\mathcal{G}$, the Turán graph $\mathcal{T}(6,3)$. Dashed edges represent missing edges. (b) Violin plot of the estimates of the value of $\log \mathcal{C}_{\mathcal{G}}\left(20, I_{6}\right)$, using Monte Carlo integration [1,30] with 1000 samples and for 200 different seeds. The horizontal line represents the exact value obtained using our formula (10).

PROOF. Notice that the assumptions stated in Theorem 1.2 are satisfied if we partition the missing edges into singletons. Let $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})=\left\{e_{1}\right\} \sqcup \cdots \sqcup\left\{e_{\tau}\right\}$. By Theorem 1.2

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right) \prod_{\xi=1}^{\tau} \frac{\mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right)}{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}
$$

where $\mathcal{G}_{\xi}$ is the graph obtained from $\mathcal{G}^{*}$ by removing the edge $e_{\xi}$, for $1 \leq \xi \leq \tau$. Since the graphs $\mathcal{G}_{\xi}$ have minimum fill-in 1, one can apply (9) and the proof is completed.

As an example, we find $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{2 n}\right)$, where $\mathcal{G}$ is the complete n-partite graph with 2 vertices in each part. In other words, it is a graph obtained by removing $n$ pairwise vertex-disjoint edges (i.e. a perfect matching) from the complete graph $\mathcal{K}_{2 n}$. This graph is also known as the Turán graph $\mathcal{T}(2 n, n)$. See Figure 4 a for $\mathcal{T}(6,3)$. We remark that, for $n \geq 2$, the graph $\mathcal{T}(2 n, n)$ is prime and has minimum fill-in $(n-1)$.

EXAMPLE 4.4. Let $\mathcal{G}$ be the Turán graph $\mathcal{T}(2 n, n)$, and let $\beta>-1$ be a real number. We apply Corollary 4.3 with $\mathcal{G}^{*}$ isomorphic to the complete graph $\mathcal{K}_{2 n}$. Then, for every missing edge $e, w_{e}=2 n-2$. Thus,

(10) $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{2 n}\right)=\frac{\mathcal{I}_{\mathcal{K}_{2 n}}\left(\beta, I_{2 n}\right)}{\pi^{\frac{n}{2}}} \frac{\Gamma\left(\beta+\frac{2 n}{2}\right)^{n}}{\Gamma\left(\beta+\frac{2 n+1}{2}\right)^{n}}=\pi^{-\frac{n}{2}} \Gamma_{2 n}\left(\beta+\frac{2 n+1}{2}\right) \frac{\Gamma(\beta+n)^{n}}{\Gamma\left(\beta+\frac{2 n+1}{2}\right)^{n}}$.

Figure $4 \mathrm{~b}$ illustrates for $n=3$ that the above formula aligns well with the values obtained using Monte Carlo integration [1, 30].

4.2. starry fill-ins. In graph theory, a star is a connected graph with at least 2 vertices, in which all but at most one vertex have degree 1. Equivalently, a star is isomorphic to the complete bipartite graph $\mathcal{K}_{1, m}$, for some $m \geq 1$. If the missing edges form a star, then the corresponding normalising constant is of the form of Equation (3).

LEMmA 4.5. Let $\mathcal{G}$ be a graph with vertex $\operatorname{set} \mathcal{V}(\mathcal{G})=\left\{v_{1}, \ldots, v_{n}\right\}$. Let $\mathcal{G}^{*}$ be a chordal completion of $\mathcal{G}$. Suppose that the missing edges $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$ form a star. Let $\beta>-1$ be a real number. Then, the integral $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)$ has the form of Equation (3).

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-13.jpg?height=345&width=396&top_left_y=234&top_left_x=580)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-13.jpg?height=336&width=634&top_left_y=233&top_left_x=1060)

(b)

Fig 5: (a) Solid edges represent those in the cycle of length 6. Dashed edges represent missing edges. (b) Violin plot of the estimates of the value of $\log \mathcal{C}_{\mathcal{G}}\left(20, I_{6}\right)$, using Monte Carlo integration $[1,30]$ with 1000 samples and for 200 different seeds. The horizontal line represents our computation of the value through one-dimensional numerical integration.

PROOF. Let $e_{1}, \ldots, e_{\tau}$ be the missing edges. By Theorem 1.1, we have

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\tau}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(\left(I_{n}+i T\right)\left[C_{\mu}\right]\right)^{-\beta-\frac{\left|C_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|S_{\nu}\right|+1}{2}}} \mathrm{~d} T
$$

where $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ are the maximal cliques of $\mathcal{G}^{*}$ and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ are the minimal separators. For a matrix $T \in \mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$, let $t_{\mu}$ be the two entries corresponding to the missing edge $e_{\mu}$, for $1 \leq \mu \leq \tau$. For a set $\mathrm{C} \subseteq\left\{v_{1}, \ldots, v_{n}\right\}$ containing missing edges $e_{\alpha_{1}}, \ldots, e_{\alpha_{k}}$, it is easy to see that

$$
\operatorname{det}\left(\left(I_{n}+i T\right)[\mathrm{C}]\right)=1+t_{\alpha_{1}}^{2}+\cdots+t_{\alpha_{k}}^{2}
$$

As an example, we find $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)$ for the cycle of length 6.

EXAMPLE 4.6. Let $\mathcal{G}$ be the cycle of length 6 and $\mathcal{G}^{*}$ be a chordal completion as shown in Figure 5a. The maximal cliques of $\mathcal{G}^{*}$ are

$$
\mathrm{C}_{1}=\left\{v_{1}, v_{2}, v_{3}\right\}, \quad \mathrm{C}_{2}=\left\{v_{1}, v_{3}, v_{4}\right\}, \quad \mathrm{C}_{3}=\left\{v_{1}, v_{4}, v_{5}\right\}, \quad \mathrm{C}_{4}=\left\{v_{1}, v_{5}, v_{6}\right\}
$$

and the corresponding separators are

$$
\mathrm{S}_{1}=\left\{v_{1}, v_{3}\right\}, \quad \mathrm{S}_{2}=\left\{v_{1}, v_{4}\right\}, \quad \mathrm{S}_{3}=\left\{v_{1}, v_{5}\right\}
$$

We write $t_{1}, t_{2}, t_{3}$ in place of $t_{1,3}, t_{1,4}, t_{1,5}$, respectively. Let $\beta>-1$ be a real number. Then,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)=\Gamma_{3}(\beta+2) \Gamma(\beta+2)^{3}
$$

$$
\times \int_{\mathbb{R}^{3}} \frac{\left(1+t_{1}^{2}\right)^{-\frac{1}{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\beta-2}\left(1+t_{2}^{2}+t_{3}^{2}\right)^{-\beta-2}\left(1+t_{3}^{2}\right)^{-\frac{1}{2}}}{\left(1+t_{2}^{2}\right)^{-\beta-\frac{3}{2}}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
$$

As in Example 3.1, it can be written as a one-dimensional integral:

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)=\frac{\pi \Gamma_{3}(\beta+2) \Gamma(\beta+2)^{5}}{\Gamma\left(\beta+\frac{5}{2}\right)^{2}} \int_{0}^{1} t^{-\frac{1}{2}}(1-t)^{\beta+1}{ }_{2} F_{1}\left(\beta+2, \frac{1}{2} ; \beta+\frac{5}{2} ; t\right)^{2} \mathrm{~d} t .
$$

We compare our result evaluated through numerical integration with values obtained by Monte Carlo integration [1, 30] in Figure 5b. Again there is good agreement though ours is much more accurate and efficient.

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-14.jpg?height=393&width=393&top_left_y=215&top_left_x=432)

$\mathcal{G}_{1}$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-14.jpg?height=390&width=396&top_left_y=217&top_left_x=862)

$\mathcal{G}_{2}$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-14.jpg?height=461&width=382&top_left_y=217&top_left_x=1294)

Fig 6: Solid edges: All three graphs are star-complementary, with $\mathcal{F}\left(\mathcal{G}_{1}\right)=\mathcal{F}\left(\mathcal{G}_{2}\right)=$ $\left\{\left\{v_{1}, v_{2}, v_{3}, v_{4}\right\},\left\{v_{5}, v_{6}, v_{7}\right\}\right\}$ and $\mathcal{F}\left(\mathcal{G}_{3}\right)=\left\{\left\{v_{1}, v_{2}\right\},\left\{v_{3}, v_{4}\right\},\left\{v_{5}, v_{6}\right\},\left\{v_{7}, v_{8}\right\}\right\}$. Dashed edges represent those in the complement.

In light of Theorem 1.2, one can have more stars among the missing edges. Let $\mathcal{G}$ be a graph and let $\mathfrak{S}_{1}, \ldots, \mathfrak{S}_{k}$ be disjoint subsets of $\mathcal{V}(\mathcal{G})$, each of size at least 2 . We say that $\mathcal{G}$ is star-complementary (with respect to $\mathfrak{S}_{1}, \ldots, \mathfrak{S}_{k}$ ) if the complement of $\mathcal{G}$ is a disjoint union of star graphs with vertex sets $\mathfrak{S}_{1}, \ldots, \mathfrak{S}_{k}$, and we define $\mathcal{F}(\mathcal{G}):=\left\{\mathfrak{S}_{1}, \ldots, \mathfrak{S}_{k}\right\}$. Figure 6 shows some examples of these graphs. We say that a non-chordal graph $\mathcal{G}$ has starry fill-ins if $\mathcal{G}$ has a chordal completion $\mathcal{G}^{*}$ such that for every maximal clique $\mathrm{C}$ of $\mathcal{G}^{*}$, the induced subgraph $\mathcal{G}[\mathrm{C}]$ is star-complementary.

Note that the graph $\mathcal{G}$ in Example 4.1 has starry fill-ins, and the corresponding integral has the form of (3), see (8). The following result shows that this is true for all graphs with starry fill-ins. A formal proof is in Appendix A. 3.

COROLLARY 4.7. Let $\mathcal{G}$ be a graph with vertex set $\mathcal{V}(\mathcal{G})=\left\{v_{1}, \ldots, v_{n}\right\}$. Suppose that $\mathcal{G}$ has starry fill-ins with a chordal completion $\mathcal{G}^{*}$. Let $\beta>-1$ be a real number. Then,

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|}}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-14.jpg?height=281&width=1238&top_left_y=1643&top_left_x=449)

where $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ are the maximal cliques and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ the minimal separators of $\mathcal{G}^{*}$.

4.3. The graphs $\mathcal{G}\left(m ; k_{1}, \ldots, k_{\ell}\right)$. For integers $m \geq 4,3 \leq \ell \leq m-1$, and $k_{1}, \ldots, k_{\ell} \geq$ 1 , we define the graph $\mathcal{G}^{*}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ as follows. The vertex set of $\mathcal{G}^{*}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ is

$$
\left\{v_{0}, v_{1}, \ldots, v_{m-1}\right\} \sqcup\left\{u_{1}, u_{2}, \ldots, u_{k_{1}+\cdots+k_{\ell}}\right\}
$$

so there are $m+k_{1}+\cdots+k_{\ell}$ vertices. In this graph, the edges form complete subgraphs on each of the $\ell+1$ sets $\left\{v_{0}, v_{1}, \ldots, v_{m-1}\right\},\left\{v_{0}, v_{1}, u_{1}, \ldots, u_{k_{1}}\right\},\left\{v_{0}, v_{2}, u_{k_{1}+1}, \ldots, u_{k_{1}+k_{2}}\right\}$, $\ldots,\left\{v_{0}, v_{\ell}, u_{k_{1}+\cdots+k_{\ell-1}+1}, \ldots, u_{k_{1}+\cdots+k_{\ell}}\right\}$, and there is no other edge. With the same parameters, we define the graph $\mathcal{G}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ to be the graph obtained from $\mathcal{G}^{*}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ by removing the edges $\left\{v_{0}, v_{1}\right\}, \ldots,\left\{v_{0}, v_{\ell}\right\}$. Figure 7 gives an example of these graphs.

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-15.jpg?height=417&width=417&top_left_y=217&top_left_x=846)

Fig 7: Solid edges represent the graph $\mathcal{G}(5 ; 2,1,1)$. Together with the dashed ones, it is the graph $\mathcal{G}^{*}(5 ; 2,1,1)$.

Observe that the graph $\mathcal{G}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ is prime and has minimum fill-in $\ell$ and $\mathcal{G}^{*}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ is a chordal completion. Moreover, it has starry fill-ins and Corollary 4.7 implies that the integral of interest has the form of

$$
\int_{\mathbb{R}^{\tau}}\left(1+t_{1}^{2}+\cdots+t_{\tau}^{2}\right)^{-\gamma}\left(1+t_{1}^{2}\right)^{-r_{1}} \cdots\left(1+t_{\tau}^{2}\right)^{-r_{\tau}} \mathrm{d} t_{1} \cdots \mathrm{d} t_{\tau}
$$

which can be estimated efficiently using the fact that a Student $t$ is a compound distribution of a $\chi^{2}$ and a Gaussian. We show in Appendix A. 4 that this reduces to a one-dimensional real integral. For numerical accuracy, we map the one-dimensional integral to the cumulative density function space of the chi-squared distributions and integrate over the $(0,1)$ interval.

COROLLaRy 4.8. Let $m \geq 4,3 \leq \ell \leq m-1$ and $k_{1}, \ldots, k_{\ell} \geq 1$ be integers. Let $\mathcal{G}=$ $\mathcal{G}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ and $\beta>-1$ be a real number. Then,

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right) \\
= & \pi^{k_{1}+\cdots+k_{\ell}-\frac{\ell}{2}} \Gamma_{m}\left(\beta+\frac{m+1}{2}\right) \prod_{\mu=1}^{\ell} \Gamma_{k_{\mu}}\left(\beta+\frac{k_{\mu}+3}{2}\right) \\
& \times \frac{1}{\Gamma\left(\beta+\frac{m+1}{2}\right) 2^{\beta+\frac{m+1}{2}}} \int_{0}^{\infty} x^{\beta+\frac{m+1}{2}-1} e^{-\frac{x}{2}} \prod_{\mu=1}^{\ell} U\left(\frac{1}{2}, \frac{3}{2}-\frac{k_{\mu}}{2}, \frac{x}{2}\right) \mathrm{d} x \\
= & \pi^{k_{1}+\cdots+k_{\ell}-\frac{\ell}{2}} \Gamma_{m}\left(\beta+\frac{m+1}{2}\right) \prod_{\mu=1}^{\ell} \Gamma_{k_{\mu}}\left(\beta+\frac{k_{\mu}+3}{2}\right) \\
& \times \int_{0}^{1} \prod_{\mu=1}^{\ell} U\left(\frac{1}{2}, \frac{3}{2}-\frac{k_{\mu}}{2}, \frac{F_{\chi^{2}(2 \beta+m+1)}^{-1}(x)}{2}\right) \mathrm{d} x
\end{aligned}
$$

where $U(a, b, x)$ is the Tricomi's confluent hypergeometric function and $F_{\chi^{2}(\nu)}(x)$ is the $\mathrm{cu}$ mulative density function of a chi-squared distribution with $\nu$ degrees of freedom.

ExAmple 4.9. Let $\mathcal{G}=\mathcal{G}(4 ; 1,1,1)$ and $\mathcal{G}^{*}=\mathcal{G}^{*}(4 ; 1,1,1)$, as shown in Figure 8a. Let $\beta>-1$ be a real number. Then,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{7}\right)=\pi^{\frac{3}{2}} \Gamma_{4}\left(\beta+\frac{5}{2}\right) \Gamma(\beta+2)^{3} \int_{0}^{1} U\left(\frac{1}{2}, 1, \frac{F_{\chi^{2}(2 \beta+5)}^{-1}(x)}{2}\right)^{3} \mathrm{~d} x
$$

We again compare our result evaluated through numerical integration with the values obtained by Monte Carlo integration [1, 30] in Figure 8b.

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-16.jpg?height=347&width=398&top_left_y=236&top_left_x=576)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-16.jpg?height=334&width=634&top_left_y=234&top_left_x=1060)

(b)

Fig 8: (a) Solid edges represent those in graph $\mathcal{G}=\mathcal{G}(4 ; 1,1,1)$. Together with the dashed ones it is the chordal completion $\mathcal{G}^{*}=\mathcal{G}^{*}(4 ; 1,1,1)$. (b) Violin plot of the estimates of the value of $\log \mathcal{C}_{\mathcal{G}}\left(20, I_{7}\right)$, using Monte Carlo integration [1, 30] with 1000 samples and for 200 different seeds, which align with one-dimensional numerical integration of our result (12), shown as the horizontal line.

4.4. Two missing edges. In this subsection, we assume that $\mathcal{G}$ is a (prime) graph which has a chordal completion $\mathcal{G}^{*}$ with two extra edges. There are 3 possibilities regarding the adjacency of the two missing edges $\{u, v\},\{x, y\}$ :

1. they are vertex-disjoint, or
2. they share a vertex, say $u=x$, and $\{v, y\}$ is not an edge in $\mathcal{G}$, or
3. they share a vertex, say $u=x$, and $\{v, y\}$ is an edge in $\mathcal{G}$.

For the first two cases, Corollary 4.3 provides an explicit formula of the $\mathcal{G}$-Wishart normalising constant when $D$ is the identity matrix. For the last case, Corollary 4.7 implies that

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{2}} \int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\gamma}\left(1+t_{1}^{2}\right)^{-r}\left(1+t_{2}^{2}\right)^{-s} \mathrm{~d} t_{1} \mathrm{~d} t_{2}
$$

for some $r, s, \gamma$. By integrating, we obtain the following result. The details can be found in Appendix A.5.

COROLLARY 4.10. Let $\mathcal{G}$ be a prime graph on $n$ vertices with minimum fill-in at most 2. Let $\mathcal{G}^{*}$ be a chordal completion of $\mathcal{G}$ with 2 added edges. Suppose that these two added edges form a triangle with an edge of $\mathcal{G}$ in $\mathcal{G}^{*}$. Let $e_{1}=\left\{v_{1}, v_{3}\right\}, e_{2}=\left\{v_{2}, v_{3}\right\}$ be the two missing edges. Let $\beta>-1$ be a real number. Then,

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)= & \frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi} \frac{\Gamma\left(\beta+\frac{w_{1}+3}{2}\right) \Gamma\left(\beta+\frac{w_{2}+3}{2}\right)}{\Gamma\left(\beta+\frac{w_{1}+4}{2}\right) \Gamma\left(\beta+\frac{w_{2}+4}{2}\right)} \\
& \times{ }_{3} F_{2}\left(\beta+\frac{w+4}{2}, \frac{1}{2}, \frac{1}{2} ; \beta+\frac{w_{1}+4}{2}, \beta+\frac{w_{2}+4}{2} ; 1\right)
\end{aligned}
$$

where $w$ is the number of common neighbours of $v_{1}, v_{2}$ in $\mathcal{G}$, and for $\mu=1,2, w_{\mu}$ is the number of common neighbours of $v_{\mu}, v_{3}$ or $v_{1}, v_{2}$ in $\mathcal{G}$.

$$
\text { If } w_{1}=w_{2}=w+1, \text { Dixon's identity implies }
$$

$$
{ }_{3} F_{2}\left(\gamma, \frac{1}{2}, \frac{1}{2} ; \gamma+\frac{1}{2}, \gamma+\frac{1}{2} ; 1\right)=\frac{\Gamma\left(\frac{\gamma+2}{2}\right) \Gamma\left(\frac{\gamma}{2}\right) \Gamma\left(\gamma+\frac{1}{2}\right)^{2}}{\Gamma(\gamma+1) \Gamma(\gamma) \Gamma\left(\frac{\gamma+1}{2}\right)^{2}}
$$

We find $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{5}\right)$ for the cycle of length 5 as an example.

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-17.jpg?height=361&width=371&top_left_y=218&top_left_x=584)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-17.jpg?height=328&width=632&top_left_y=234&top_left_x=1061)

(b)

Fig 9: (a) Solid edges are those in $\mathcal{G}$ (the cycle of length 5). Dashed edges represent missing edges. (b) Violin plot of the estimates of the value of $\log \mathcal{C}_{\mathcal{G}}\left(20, I_{5}\right)$, using Monte Carlo integration [1, 30] with 1000 samples and for 200 different seeds. The horizontal line represents our exact value (13).

EXAMPLE 4.11. Let $\mathcal{G}$ be the cycle of length 5 , which is isomorphic to $\mathcal{G}(3 ; 1,1)$. Then,

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{5}\right) & =\pi \Gamma(\beta+2)^{2} \Gamma_{3}(\beta+2) \frac{\Gamma(\beta+2)^{2}}{\Gamma\left(\beta+\frac{5}{2}\right)^{2}}{ }_{3}\left(\beta+2, \frac{1}{2}, \frac{1}{2} ; \beta+\frac{5}{2}, \beta+\frac{5}{2} ; 1\right) \\
& =\frac{\pi \Gamma_{3}(\beta+2) \Gamma(\beta+2)^{3} \Gamma\left(\frac{\beta+4}{2}\right) \Gamma\left(\frac{\beta+2}{2}\right)}{\Gamma(\beta+3) \Gamma\left(\frac{\beta+3}{2}\right)^{2}}
\end{aligned}
$$

Figure 9b illustrates that the above result aligns well with Monte Carlo integration [1, 30].

5. Relating the normalising constants of different graphs, $D=I$. We continue with the assumption that $D=I$ in this Section and use Theorem 1.1 to express the $\mathcal{G}$-Wishart normalising constant of a graph in terms of that of another graph (sometimes with a different $\beta)$. This is useful when one of the constants has a simpler form than the other, and particularly useful for Bayesian samplers in the space of undirected graphs, since the acceptance probability of a move between graphs will just depend on their relative posterior probability.

In this Section, we give 2 examples. First, we show that the normalising constant of any graph with a chordal completion such that the missing edges form a triangle can be written as a one-dimensional integral, instead of three-dimensional. Second, we show that the normalising constant of any gear graph has the form of Equation (3), instead of an integral with complex integrand.

5.1. Triangular missing edges. Let $\mathcal{G}$ and $\mathcal{G}^{*}$ be the graphs as shown in Figure 10. Let $\beta>-1$ be a real number. By Theorem 1.1, we have

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{7}\right)=\Gamma_{4}\left(\beta+\frac{5}{2}\right) \Gamma(\beta+2)^{3}
$$

$$
\times \int_{\mathbb{R}^{3}}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\beta-\frac{5}{2}}\left(1+t_{1}^{2}\right)^{-\frac{1}{2}}\left(1+t_{2}^{2}\right)^{-\frac{1}{2}}\left(1+t_{3}^{2}\right)^{-\frac{1}{2}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
$$

Let $\mathcal{H}$ be the cycle of length 6 . Note that there are three different (up to isomorphism) chordal completions of $\mathcal{H}$ using 3 added edges; see Figure 11. When we apply Theorem 1.1 with $\mathcal{H}_{2}^{*}$ or $\mathcal{H}_{3}^{*}$, we get the same formula; see Example 4.6. However, if we apply Theorem 1.1 with

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-18.jpg?height=396&width=371&top_left_y=211&top_left_x=866)

Fig 10: Solid edges represent the graph $\mathcal{G}$ in Section 5.1. Together with the dashed ones it is the chordal completion $\mathcal{G}^{*}$. The graph $\mathcal{G}$ is also the gear graph $\mathcal{G}_{3}$ defined in Section 5.2.
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-18.jpg?height=354&width=1220&top_left_y=782&top_left_x=446)

Fig 11: Solid edges represent the graph $\mathcal{H}$, i.e., the cycle of length 6 . Together with the dashed edges, they are chordal completions of $\mathcal{H}$. Left: $\mathcal{H}_{1}^{*}$, middle: $\mathcal{H}_{2}^{*}$, right: $\mathcal{H}_{3}^{*}$.

$\mathcal{H}_{1}^{*}$, we get an integral very similar to the one appearing in Equation (14). Indeed, we have

$$
\mathcal{I}_{\mathcal{H}}\left(\beta, I_{6}\right)=\Gamma_{3}(\beta+2) \Gamma(\beta+2)^{3}
$$

$$
\times \int_{\mathbb{R}^{3}}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\beta-2}\left(1+t_{1}^{2}\right)^{-\frac{1}{2}}\left(1+t_{2}^{2}\right)^{-\frac{1}{2}}\left(1+t_{3}^{2}\right)^{-\frac{1}{2}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
$$

Hence, Equations (14) and (15) together imply that

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{7}\right) & =\Gamma_{4}\left(\beta+\frac{5}{2}\right) \Gamma(\beta+2)^{3} \frac{\mathcal{I}_{\mathcal{H}}\left(\beta+\frac{1}{2}, I_{6}\right)}{\Gamma_{3}\left(\beta+\frac{5}{2}\right) \Gamma\left(\beta+\frac{5}{2}\right)^{3}} \\
& =\frac{\pi^{\frac{3}{2}} \Gamma(\beta+2)^{3} \Gamma(\beta+1)}{\Gamma\left(\beta+\frac{5}{2}\right)^{3}} \mathcal{I}_{\mathcal{H}}\left(\beta+\frac{1}{2}, I_{6}\right)
\end{aligned}
$$

Now, if we use the result obtained from Example 4.6 in Equation (11), we have

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{7}\right)= & \frac{\Gamma_{4}\left(\beta+\frac{5}{2}\right) \Gamma\left(\beta+\frac{5}{2}\right)^{2} \Gamma(\beta+2)^{3}}{\pi \Gamma(\beta+3)^{2}} \\
& \times \int_{0}^{1} t^{-\frac{1}{2}}(1-t)^{\beta+\frac{3}{2}} 2 F_{1}\left(\beta+\frac{5}{2}, \frac{1}{2} ; \beta+3 ; t\right)^{2} \mathrm{~d} t
\end{aligned}
$$

The above argument works for any graph with a chordal completion such that the missing edges form a triangle. The details can be found in Appendix B.

5.2. Gear graphs. For integer $m \geq 3$, the gear graph with $2 m+1$ vertices, denoted by $\mathcal{G}_{m}$ in this section, has vertex set $\mathcal{V}\left(\mathcal{G}_{m}\right)=\left\{v_{1}, \ldots, v_{2 m+1}\right\}$ and edge set $\mathcal{E}\left(\mathcal{G}_{m}\right)$ is

$$
\left\{\left\{v_{2 m+1}, v_{\mu}\right\}: 1 \leq \mu \leq 2 m-1, \mu \text { is odd }\right\} \sqcup\left\{\left\{v_{\mu}, v_{\mu+1}\right\}: 1 \leq \mu \leq 2 m\right\} \sqcup\left\{\left\{v_{2 m}, v_{1}\right\}\right\}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-19.jpg?height=390&width=398&top_left_y=217&top_left_x=858)

Fig 12: Solid edges represent the gear graph $\mathcal{G}_{4}$. Together with the dashed edges, it is the graph $\mathcal{G}_{4}^{*}$.

In words, the first $2 m$ vertices form an induced cycle and the last vertex $v_{2 m+1}$ is adjacent to alternate vertices in the cycle. The gear graph $\mathcal{G}_{3}$ is shown in Figure 10, and the integral $\mathcal{I}_{\mathcal{G}_{3}}\left(\beta, I_{7}\right)$ can be expressed as a one-dimensional integral, see Equation (16).

For $\mathcal{G}_{m}$, let $\mathcal{G}_{m}^{*}$ be a supergraph with added edges

$$
\left\{\left\{v_{2 \mu+1}, v_{2 \mu+3}\right\}: 0 \leq \mu \leq m-2\right\} \sqcup\left\{\left\{v_{1}, v_{\mu}\right\}: 5 \leq \mu \leq 2 m-1, \mu \text { is odd }\right\}
$$

In words, the neighbours of $v_{2 m+1}$ in $\mathcal{G}$ form a cycle (in the same ordering) and the vertex $v_{1}$ is connected to every vertex in this cycle. An example of $\mathcal{G}_{4}^{*}$ is shown in Figure 12. It is straightforward to verify that $\mathcal{G}_{m}^{*}$ is chordal.

COROLLARY 5.1. Let $m \geq 4$ be an integer. Let $\mathcal{G}_{m}$ be the gear graph on $2 m+1$ vertices and let $\mathcal{G}_{m}^{*}$ be a chordal completion defined above. Let $\beta>-1$ be a real number. Then,

$$
\mathcal{I}_{\mathcal{G}_{m}}\left(\beta, I_{2 m+1}\right)=\frac{\mathcal{I}_{\mathcal{G}_{m}^{*}}\left(\beta, I_{2 m+1}\right)}{\mathcal{I}_{\mathcal{H}_{m}^{*}}\left(\beta+\frac{1}{2}, I_{2 m}\right)} \mathcal{I}_{C_{2 m}}\left(\beta+\frac{1}{2}, I_{2 m}\right)
$$

where $C_{2 m}$ is the cycle graph on $2 m$ vertices, and $\mathcal{H}_{m}^{*}$ is the induced subgraph obtained from $\mathcal{G}_{m}^{*}$ by removing the vertex with degree $m$ ( $v_{2 m+1}$ in the above definition).

PROOF. Since $\mathcal{G}_{m}^{*}$ is chordal, the graph $\mathcal{H}_{m}^{*}$ is a chordal completion of the cycle $C_{2 m}$. We compare the integrals obtained from Theorem 1.1 using the pair $\mathcal{G}_{m}, \mathcal{G}_{m}^{*}$ and the pair $C_{2 m}$, $\mathcal{H}_{m}^{*}$. Note that a maximal clique $\mathrm{C}$ in $\mathcal{G}^{*}$ contains the vertex $v_{2 m+1}$ if and only if $\mathrm{C}$ contains more than 3 vertices. Similarly, a minimal separator $\mathrm{S}$ in $\mathcal{G}^{*}$ contains the vertex $v_{2 m+1}$ if and only if $S$ contains more than 2 vertices.

Following the same argument as in Section 5.1, it is easy to see that

$$
\mathcal{I}_{\mathcal{G}_{m}}\left(\beta, I_{2 m+1}\right)=\frac{\mathcal{I}_{\mathcal{G}_{m}^{*}}\left(\beta, I_{2 m+1}\right)}{\pi^{2 m-3}} \frac{\pi^{2 m-3} \mathcal{I}_{C_{2 m}}\left(\beta+\frac{1}{2}, I_{2 m}\right)}{\mathcal{I}_{\mathcal{H}_{m}^{*}}\left(\beta+\frac{1}{2}, I_{2 m}\right)}
$$

In the above result, both $\mathcal{I}_{\mathcal{G}_{m}^{*}}\left(\beta, I_{2 m+1}\right)$ and $\mathcal{I}_{\mathcal{H}_{m}^{*}}\left(\beta+\frac{1}{2}, I_{2 m}\right)$ have an explicit formula from Equation (4). Since $C_{2 m}$ has starry fill-ins, Corollary 4.7 implies that the integral $\mathcal{I}_{C_{2 m}}\left(\beta+\frac{1}{2}, I_{2 m}\right)$ has the form of Equation (3).

6. A new approach for graphs with minimum fill-in 1 , arbitrary $\boldsymbol{D}$. Let $\mathcal{G}$ be a graph with $n \geq 4$ vertices which has minimum fill-in 1 . For real number $\beta>-1$ and arbitrary matrix $D \in \mathbb{S}_{++}^{n}$, a complicated formula for $\mathcal{I}_{\mathcal{G}}(\beta, D)$ is given in [38] (Proposition 3.1 and Corollary 3.2). In this Section, we derive an efficient approach to evaluate the G-Wishart normalising constant by reducing it to a one-dimensional integral.

We order the vertices $\mathcal{V}(\mathcal{G})=\left\{v_{1}, \ldots, v_{n}\right\}$ such that the graph $\mathcal{G}^{*}$ obtained by adding an edge between $v_{n-1}$ and $v_{n}$ in $\mathcal{G}$ is chordal.

6.1. Three assumptions. For the sake of simplicity, we make a few assumptions.

First, we assume that $D \in \mathbb{S}_{++}^{n}$ has diagonal entries all equal to 1 since the transformation

$$
K \rightarrow \operatorname{diag}(D)^{-\frac{1}{2}} K \operatorname{diag}(D)^{-\frac{1}{2}}
$$

gives

$$
\mathcal{I}_{\mathcal{G}}(\beta, D)=\mathcal{I}_{\mathcal{G}}\left(\beta, \operatorname{diag}(D)^{-\frac{1}{2}} D \operatorname{diag}(D)^{-\frac{1}{2}}\right) \prod_{\mu=1}^{n}\left(d_{\mu, \mu}\right)^{-\frac{\operatorname{deg}_{\mathcal{G}}\left(v_{\mu}\right)}{2}-\beta-1}
$$

in which the diagonal elements of $\operatorname{diag}(D)^{-\frac{1}{2}} D \operatorname{diag}(D)^{-\frac{1}{2}} \in \mathbb{S}_{++}^{n}$ are 1 . Here, $\operatorname{deg}_{\mathcal{G}}\left(v_{\mu}\right):=$ $\left|\mathcal{N}_{\mathcal{G}}\left(v_{\mu}\right)\right|$ is the degree of $v_{\mu}$ in $\mathcal{G}$.

Second, we set $d_{\mu, \nu}=0$ whenever $\left\{v_{\mu}, v_{\nu}\right\} \notin \mathcal{E}(\mathcal{G})$. This can be justified since for $K \in$ $\mathbb{S}_{++}^{n}(\mathcal{G})$, the value of $\operatorname{tr}(K D)$, and hence $\mathcal{I}_{\mathcal{G}}(\beta, D)$, does not depend on those entries of $D$.

Third, we assume that $\mathcal{G}$ is a prime graph, see (5). It is then easy to see that both $v_{n-1}$ and $v_{n}$ are adjacent to $v_{\mu}$, for $1 \leq \mu \leq n-2$.

6.2. Derivation. Let $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ be the maximal cliques of $\mathcal{G}^{*}$, and let $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ be the separators. Notice that every $\mathrm{C}_{\mu}$, and hence every $\mathrm{S}_{\nu}$, contains the vertices $v_{n-1}$ and $v_{n}$.

By Theorem 1.1, we have

$$
\mathcal{I}_{\mathcal{G}}(\beta, D)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left((D+i T)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left((D+i T)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \mathrm{~d} T
$$

Recall that $T \in \mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$ is real symmetric and has entry $t_{\mu, \nu}=0$ unless $\mu$ and $\nu$ are exactly $n-1$ and $n$. We write $t_{n-1, n}=t_{n, n-1}=t$. Let $\mathrm{C}=\left\{v_{\alpha_{1}}, \ldots, v_{\alpha_{k}}, v_{n-1}, v_{n}\right\} \subseteq \mathcal{V}(\mathcal{G})$, and $T \in \mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$. Then,

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-20.jpg?height=326&width=1080&top_left_y=1431&top_left_x=514)

The Schur complement formula for the determinant of a 2 by 2 block matrix implies that

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}(\beta, D)= & \frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(D\left[\mathrm{C}_{\mu} \backslash\left\{v_{n-1}, v_{n}\right\}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(D\left[\mathrm{~S}_{\nu} \backslash\left\{v_{n-1}, v_{n}\right\}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \\
& \times \int_{\mathbb{R}} \frac{\prod_{\mu=1}^{m}\left(t^{2}+2 i y_{\mathrm{C}_{\mu}} t+x_{\mathrm{C}_{\mu}}\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1}\left(t^{2}+2 i y_{\mathrm{S}_{\nu}} t+x_{\mathrm{S}_{\nu}}\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \mathrm{~d} t
\end{aligned}
$$

where

$$
x_{\mathrm{C}}=\frac{\operatorname{det}(D[\mathrm{C}])}{\operatorname{det}\left(D\left[\mathrm{C} \backslash\left\{v_{n-1}, v_{n}\right\}\right]\right)}, \quad y_{\mathrm{C}}=\left(d_{\alpha_{1}, n-1} \cdots d_{\alpha_{k}, n-1}\right) D\left[\mathrm{C} \backslash\left\{v_{n-1}, v_{n}\right\}\right]^{-1}\left(\begin{array}{c}
d_{\alpha_{1}, n} \\
\vdots \\
d_{\alpha_{k}, n}
\end{array}\right)
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-21.jpg?height=562&width=458&top_left_y=215&top_left_x=367)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-21.jpg?height=252&width=263&top_left_y=218&top_left_x=931)

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-21.jpg?height=236&width=461&top_left_y=538&top_left_x=824)

(b)
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-21.jpg?height=560&width=442&top_left_y=218&top_left_x=1297)

Fig 13: (a) The graphs $\mathcal{G}_{1}, \mathcal{G}_{2}, \mathcal{G}_{3}$ (from left to right), are the non-chordal graphs for Fisher's Iris Virginica dataset. (b) Violin plots of the estimates of the values of $\log \left(p\left(Z \mid \mathcal{G}_{j}\right)\right)$ ), where $j=1,2,3$, using Monte Carlo integration $[1,30]$ with $10^{6}$ samples and for 200 different seeds. The horizontal lines represent the values obtained using our approach.

and both can be evaluated more efficiently from the Cholesky decomposition of $D[C \backslash$ $\left.\left\{v_{n-1}, v_{n}\right\}\right]$ and back-substitution, without evaluating the determinants and inverse directly.

6.3. Evaluation. The one dimensional integral in (17) has the form

$$
\begin{aligned}
\mathcal{J} & =\mathcal{J}\left(x_{1}, \ldots, x_{l} ; y_{1}, \ldots, y_{l} ; r_{1}, \ldots, r_{l}\right) \\
& =\int_{\mathbb{R}} \prod_{\mu=1}^{l}\left(t^{2}+2 i y_{\mu} t+x_{\mu}\right)^{r_{\mu}} \mathrm{d} t=\int_{\mathbb{R}}\left(1+t^{2}\right)^{r_{1}+\cdots+r_{l}} \prod_{\mu=1}^{l}\left(1+\frac{2 i y_{\mu} t+x_{\mu}-1}{1+t^{2}}\right)^{r_{\mu}} \mathrm{d} t
\end{aligned}
$$

where we extract the overall behaviour in $t$ as a prefactor and have correction terms which vanish as $D$ approaches the identity matrix. Next, the prefactor is related to a Student- $t$ distribution $F_{\mathrm{t}(\nu)}$ with $\nu=-1-2 \sum_{\mu} r_{\mu}$ degrees of freedom, and under the change of variable $t \rightarrow \phi(t)=F_{\mathrm{t}(\nu)}^{-1}(t) / \sqrt{\nu}$ we transform to a bounded integral suitable for numerical evaluation

$$
\mathcal{J}=\frac{\Gamma\left(\frac{\nu}{2}\right) \Gamma\left(\frac{1}{2}\right)}{\Gamma\left(\frac{\nu+1}{2}\right)} \int_{0}^{1} \prod_{\mu=1}^{l}\left(1+\frac{2 i y_{\mu} \phi(t)+x_{\mu}-1}{1+\phi(t)^{2}}\right)^{r_{\mu}} \mathrm{d} t
$$

6.4. Fisher's Iris Virginica data. As in $[1,35]$, we use Fisher's Iris Virginica dataset for illustration. This data provides measurements for four features of 50 Iris Virginica flowers: sepal length (SL), sepal width (SW), petal length (PL) and petal width (PW). There are $2\left(\begin{array}{l}4 \\ 2\end{array}\right)=$ 64 Gaussian graphical models with 4 features. To perform model selection, we need to find

$$
p(Z \mid \mathcal{G})=\frac{2^{-6}}{(2 \pi)^{100}} \frac{\mathcal{C}_{\mathcal{G}}(\delta+50, U+D)}{\mathcal{C}_{\mathcal{G}}(\delta, D)}, \quad U=\left(\begin{array}{rrrrr}
19.8128 & 4.5944 & 14.8612 & 2.4056 \\
4.5944 & 5.0962 & 3.4976 & 2.3338 \\
14.8612 & 3.4976 & 14.9248 & 2.3924 \\
2.4056 & 2.3338 & 2.3924 & 3.6962
\end{array}\right)
$$

where $U$ is the scatter matrix (sample covariance rescaled by 49) of the dataset $Z \in \mathbb{R}^{4 \times 50}$, and $\mathcal{G}$ is any of the 64 graphs on 4 vertices. In line with [1,35], we take $\delta=3$ and $D=I_{4}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-22.jpg?height=212&width=185&top_left_y=233&top_left_x=970)

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-22.jpg?height=185&width=196&top_left_y=463&top_left_x=455)
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-22.jpg?height=420&width=178&top_left_y=683&top_left_x=472)
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-22.jpg?height=640&width=196&top_left_y=463&top_left_x=711)
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-22.jpg?height=644&width=680&top_left_y=462&top_left_x=972)

Fig 14: Top 16 models for Fisher's Iris Virginica data with their posterior probabilities.

TABLE 1

Summary of the estimated values of $\log \left(p\left(Z \mid \mathcal{G}_{j}\right)\right)$, for $j=1,2,3$, using Monte Carlo integration [1,30] with $10^{6}$ samples and for 200 different seeds, and using our approach.

|  | $\log \left(p\left(Z \mid \mathcal{G}_{1}\right)\right)$ | $\log \left(p\left(Z \mid \mathcal{G}_{2}\right)\right)$ | $\log \left(p\left(Z \mid \mathcal{G}_{3}\right)\right)$ |
| :--- | :---: | :---: | :---: |
| $\min ($ MC) | -84.4427 | -85.8881 | -114.6686 |
| $\max ($ MC) | -84.4394 | -85.8834 | -111.0994 |
| $\operatorname{sd}($ MC) | 0.0006 | 0.0008 | 0.5142 |
| mean(MC) | -84.4413 | -85.8854 | -113.7590 |
| our method | -84.4412 | -85.8854 | -113.5226 |

TABLE 2

The average time (in milliseconds) needed to compute the normalising constant $\mathcal{C}_{\mathcal{G}_{j}}\left(53, U+I_{4}\right.$ ), for $j=1,2,3$.

|  | $\mathcal{C}_{\mathcal{G}_{1}}\left(53, U+I_{4}\right)$ | $\mathcal{C}_{\mathcal{G}_{2}}\left(53, U+I_{4}\right)$ | $\mathcal{C}_{\mathcal{G}_{3}}\left(53, U+I_{4}\right)$ |
| :---: | :---: | :---: | :---: |
| MC $[1,30]$ | 433.75 | 440.53 | 432.15 |
| our method | 0.51 | 0.66 | 1.45 |

The only non-chordal graphs on 4 vertices are the three 4-cycles, $\mathcal{G}_{1}, \mathcal{G}_{2}$, $\mathcal{G}_{3}$ (see Figure 13a), which have minimum fill-in 1. Thus, explicit formulae for the normalising constants of interest are known except for $\mathcal{C}_{\mathcal{G}_{j}}\left(53, U+I_{4}\right)$, where $j=1,2,3$.

We compare the performance of finding these three marginal likelihoods using our proposed method with the Monte Carlo method in [1] (as implemented in the gnorm function from the R package BDgraph [30] with $10^{6}$ samples, for 200 different seeds). The results are shown in Table 1 and Figure 13b. It can be seen, particularly for the last case, that the ratio of interest struggles to converge when using the Monte Carlo method, whereas our method gives an accurate estimate. Moreover, our approach is hundreds of times faster than the Monte Carlo method, as shown in Table 2. In Figure 14, we show the top 16 models for this dataset, each with its associated posterior probability for a uniform prior on graphs.

7. Conclusions. Efficiently estimating the $\mathcal{G}$-Wishart normalising constant $\mathcal{C}_{\mathcal{G}}(\delta, D)$ is essential for implementing Bayesian inference of Gaussian graphical models and performing Gaussian graphical model selection. Little is known about the form of this constant for general graphs, with available estimation methods resting on computational methods based on Monte Carlo integration. While an explicit representation of the $\mathcal{G}$-Wishart normalising constant for general graphs has been recently derived [38], its form is not well suited for practical computation.

In this paper, we provide practical results for evaluating the $\mathcal{G}$-Wishart normalising constant for a large collection of graphs, beyond the well-understood class of decomposable graphs. To do so we introduce, in Section 3, a transformation of $\mathcal{C}_{\mathcal{G}}(\delta, D)$ to an unconstrained integral, which is much easier to handle than its original form. After transformation, the tractibility of the normalising constant improves substantially under the assumption that $D$ is the identity matrix. If a conjecture of Roverato's [35] (see (2)), which appears likely to be true based on empirical evidence, were proved the identity case would be the only one needed to evaluate the constant for arbitrary $D$. Focusing on the identity matrix, we obtained closed formulae or provided numerically efficient results for $\mathcal{C}_{\mathcal{G}}\left(\delta, I_{|\mathcal{V}(\mathcal{G})|}\right)$ for a variety of graphs.

For many other graphs, we showed that the $\mathcal{G}$-Wishart normalising constant involves solving real integrals of the form of Equation (3), which can sometimes be simplified and expressed in terms of special functions, or otherwise be computed numerically. Studying integrals of this particular form would therefore constitute a valuable direction for future work.

Another promising direction for further developments follows from Section 5, where we establish a link between the constants $\mathcal{C}_{\mathcal{G}}\left(\delta, I_{|\mathcal{V}(\mathcal{G})|}\right)$ for different graphs (with different values of $\delta$ ). One might be able to connect a class of graphs with another class, whose normalising constants can be more efficiently estimated, and help speed up Bayesian samplers that move in the space of undirected graphs.

Even without assuming that $D$ is the identity matrix, our transformation can help the evaluation of the normalising constant. In Section 6, we propose an accurate and inexpensive approach for arbitrary $D$ for (prime) graphs with minimum fill-in 1 , and illustrate its performance on the Fisher's Iris Virginica data.

Finally, for general graphs, Theorem 1.1 may help devise new Monte Carlo integration approaches by constructing a chordal completion with relatively few edges. Such a strategy is expected to outperform current algorithms such as [1], if the number of missing edges is less than the sum of the number of edges and vertices in the graph, since the resulting integral would be lower dimensional. Taken together with the exact results presented here for a larger class of graphs than previously known, this avenue could enable faster Bayesian sampling schemes for general graphs and hence fully Bayesian analyses of larger Gaussian graphical models for practical applications.

## REFERENCES

[1] Atay-Kayis, A. and Massam, H. (2005). A Monte Carlo method for computing the marginal likelihood in nondecomposable Gaussian graphical models. Biometrika 92 317-335. https://doi.org/10.1093/ biomet/92.2.317

[2] Berkolaiko, G. and Kuipers, J. (2012). Universality in chaotic quantum transport: The concordance between random-matrix and semiclassical theories. Physical Review E 85 045201. https://doi.org/10. 1103/PhysRevE.85.045201

[3] Brouwer, P., Frahm, K. and BeEnaKKer, C. (1997). Quantum mechanical time-delay matrix in chaotic scattering. Physical Review Letters 78 4737. https://doi.org/10.1103/PhysRevLett. 78.4737

[4] CorneIL, D. G. (2004). Lexicographic breadth first search—a survey. In Graph-theoretic concepts in computer science. Lecture Notes in Comput. Sci. 3353 1-19. Springer, Berlin. https://doi.org/10.1007/ 978-3-540-30559-0_1

[5] Dawid, A. P. and LaURitzen, S. L. (1993). Hyper-Markov laws in the statistical analysis of decomposable graphical models. Ann. Statist. 21 1272-1317. https://doi.org/10.1214/aos/1176349260

[6] Eaton, M. L. (2007). Multivariate statistics. Institute of Mathematical Statistics Lecture NotesMonograph Series 53. Institute of Mathematical Statistics, Beachwood, OH. https://doi.org/10.1214/ $\ln \mathrm{ms} / 1196285102$

[7] Friedman, J., Hastie, T. and Tibshirani, R. (2008). Sparse inverse covariance estimation with the graphical lasso. Biostatistics 9 432-441. https://doi.org/10.1093/biostatistics/kxm045

[8] Geiger, D. and Heckerman, D. (2002). Parameter priors for Directed Acyclic Graphical models and the characterization of several probability distributions. Annals of Statistics 30 1412-1440. https: //doi.org/10.1214/aos/1035844981

[9] Gelman, A., Carlin, J. B., Stern, H. S. and Rubin, D. B. (1995). Bayesian data analysis. Chapman and Hall/CRC. https://doi.org/10.1201/9780429258411

[10] Giudici, P. and Castelo, R. (2003). Improving Markov Chain Monte Carlo model search for data mining. Machine Learning 50 127-158. https://doi.org/10.1023/A:1020202028934

[11] GiUdiCI, P. and GrEen, P. (1999). Decomposable graphical Gaussian model determination. Biometrika 86 785-801. https://doi.org/10.1093/biomet/86.4.785

[12] Green, P. J. (2003). Trans-dimensional Markov Chain Monte Carlo. Oxford Statistical Science Series $179-198$.

[13] Green, P. J. and Thomas, A. (2013). Sampling decomposable graphs using a Markov chain on junction trees. Biometrika 100 91-110. https://doi.org/10.1093/biomet/ass052

[14] GrzegorCZyK, M. and Husmeier, D. (2008). Improving the structure MCMC sampler for Bayesian networks by introducing a new edge reversal move. Machine Learning 71 265-305. https://doi.org/ 10.1007/s10994-008-5057-7

[15] JANIK, R. A. and NOWAK, M. A. (2003). Wishart and anti-Wishart random matrices. Journal of Physics A: Mathematical and General 36 3629. https://doi.org/10.1088/0305-4470/36/12/343

[16] Johnstone, I. M. (2001). On the distribution of the largest eigenvalue in principal components analysis. The Annals of Statistics 29 295-327. https://doi.org/10.1214/aos/1009210544

[17] Koller, D. and Friedman, N. (2009). Probabilistic Graphical Models. The MIT Press.

[18] Kuipers, J. and Moffa, G. (2017). Partition MCMC for inference on acyclic digraphs. Journal of the American Statistical Association 112 282-299. https://doi.org/10.1080/01621459.2015.1133426

[19] Kuipers, J., Moffa, G. and Heckerman, D. (2014). Addendum on the scoring of Gaussian directed acyclic graphical models. Annals of Statistics 42 1689-1691. https://doi.org/10.1214/14-AOS1217

[20] Kuipers, J., Savin, D. V. and Sieber, M. (2014). Efficient semiclassical approach for time delays. New Journal of Physics 16 123018. https://doi.org/10.1088/1367-2630/16/12/123018

[21] Kuipers, J., Suter, P. and Moffa, G. (2022). Efficient sampling and structure learning of Bayesian networks. Journal of Computational and Graphical Statistics 31 639-650. https://doi.org/10.1080/ 10618600.2021 .2020127

[22] LAURITZEn, S. L. (1996). Graphical Models. Oxford University Press.

[23] LenkoskI, A. (2013). A direct sampler for G-Wishart variates. Stat 2 119-128. https://doi.org/10.1002/ sta4.23

[24] Livan, G., Novaes, M. and Vivo, P. (2018). Introduction to random matrices: Theory and practice. https://doi.org/10.1007/978-3-319-70885-0

[25] Madigan, D. and YorK, J. (1995). Bayesian graphical models for discrete data. International Statistical Review 63 215-232. https://doi.org/10.2307/1403615

[26] Majumdar, S. N. (2015). Extreme eigenvalues of Wishart matrices: application to entangled bipartite system. In The Oxford Handbook of Random Matrix Theory Oxford University Press. https://doi.org/ 10.1093/oxfordhb/9780198744191.013.37

[27] Mента, M. L. (2004). Random matrices. Elsevier.

[28] Moffa, G., Catone, G., Kuipers, J., Kuipers, E., Freeman, D., Marwaha, S., Lennox, B. R., Broome, M. R. and Bebbington, P. (2017). Using Directed Acyclic Graphs in epidemiological research in psychosis: An analysis of the role of bullying in psychosis. Schizophrenia Bulletin 43 1273-1279. https://doi.org/10.1093/schbul/sbx013

[29] Mohammadi, A. and WiT, E. C. (2015). Bayesian structure learning in sparse Gaussian graphical models. Bayesian Analysis 10109 - 138. https://doi.org/10.1214/14-BA889

[30] Mohammadi, R. and WiT, E. C. (2019). BDgraph: An R package for Bayesian structure learning in graphical models. Journal of Statistical Software 89 1-30. https://doi.org/10.18637/jss.v089. 03

[31] Novaes, M. (2023). Semiclassical calculation of time delay statistics in chaotic quantum scattering. Physica D: Nonlinear Phenomena 444 133611. https://doi.org/10.1016/j.physd.2022.133611

[32] Olsson, J., Pavlenko, T. and Rios, F. (2022). Sequential sampling of junction trees for decomposable graphs. Statistics and Computing 32. https://doi.org/10.1007/s11222-022-10113-2

[33] Reza Mohammadi, H. M. and Letac, G. (2023). Accelerating Bayesian structure learning in sparse Gaussian graphical models. Journal of the American Statistical Association 118 1345-1358. https: //doi.org/10.1080/01621459.2021.1996377

[34] Rose, D. J., Tarjan, R. E. and Lueker, G. S. (1976). Algorithmic aspects of vertex elimination on graphs. SIAM J. Comput. 5 266-283. https://doi.org/10.1137/0205021

[35] Roverato, A. (2002). Hyper inverse Wishart distribution for non-decomposable graphs and its application to Bayesian inference for Gaussian graphical models. Scand. J. Statist. 29 391-411. https://doi.org/ $10.1111 / 1467-9469.00297$

[36] Talvitie, T., VuoksenmaA, A. and Koivisto, M. (2020). Exact sampling of directed acyclic graphs from modular distributions. In Uncertainty in Artificial Intelligence 965-974. PMLR.

[37] Tarjan, R. E. and Yannakakis, M. (1984). Simple linear-time algorithms to test chordality of graphs, test acyclicity of hypergraphs, and selectively reduce acyclic hypergraphs. SIAM J. Comput. $13566-$ 579. https://doi.org/10.1137/0213035

[38] Uhler, C., Lenkoski, A. and Richards, D. (2018). Exact formulas for the normalizing constants of Wishart distributions for graphical models. Ann. Statist. 46 90-118. https://doi.org/10.1214/ 17-AOS1543

[39] Verbaarschot, J. J. and Wettig, T. (2000). Random matrix theory and chiral symmetry in QCD. Annual Review of Nuclear and Particle Science 50 343-410. https://doi.org/10.1146/annurev.nucl.50. 1.343

[40] Viinikka, J., Hyttinen, A., Pensar, J. and Koivisto, M. (2020). Towards scalable Bayesian learning of causal DAGs. Advances in Neural Information Processing Systems 33 6584-6594.

[41] WANG, H. and LI, S. Z. (2012). Efficient Gaussian graphical model determination under G-Wishart prior distributions. Electronic Journal of Statistics 6168 - 198. https://doi.org/10.1214/12-EJS669

[42] WignER, E. (1955). Characteristic vectors of bordered matrices with infinite dimensions. Annals of Mathematics 548-564. https://doi.org/10.2307/1970079

[43] WISHART, J. (1928). The generalised product moment distribution in samples from a normal multivariate population. Biometrika 32-52. https://doi.org/10.2307/2331939

[44] Yannakakis, M. (1981). Computing the minimum fill-in is NP-complete. SIAM J. Algebraic Discrete Methods 2 77-79. https://doi.org/10.1137/0602010

## APPENDIX A: TECHNICAL PROOFS

A.1. Proof of Theorem 1.2. For $1 \leq \xi \leq k$, let $\tau_{\xi}=\left|\mathcal{E}_{\xi}\right|$. Let $\tau=\tau_{1}+\cdots+\tau_{k}$. By Theorem 1.1, we have

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\tau}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathcal{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \mathrm{~d} T
$$

where $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ are the maximal cliques and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ the minimal separators of $\mathcal{G}^{*}$.

Within each clique $\mathrm{C} \in\left\{\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}, \mathrm{~S}_{1}, \ldots, \mathrm{S}_{m-1}\right\}$, the edge parts $\mathcal{E}_{\mu}$ and $\mathcal{E}_{\nu}$ are vertexdisjoint whenever $\mu \neq \nu$. For $T \in \mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$, we write $T=T_{1}+\cdots+T_{k}$, where each $T_{\xi}$ represents the entries corresponding to the missing edges in $\mathcal{E}_{\xi}$. Then,

$$
\operatorname{det}\left(\left(I_{n}+i T\right)[\mathrm{C}]\right)=\prod_{\xi=1}^{k} \operatorname{det}\left(\left(I_{n}+i T_{\xi}\right)[\mathrm{C}]\right)
$$

and hence

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\tau}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \prod_{\xi=1}^{k} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(\left(I_{n}+i T_{\xi}\right)\left[C_{\mu}\right]\right)^{-\beta-\frac{\left|\mathcal{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(\left(I_{n}+i T_{\xi}\right)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|S_{\nu}\right|+1}{2}}} \mathrm{~d} T \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\tau}} \prod_{\xi=1}^{k} \int_{\mathbb{S}\left(\mathcal{G}_{\xi}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(\left(I_{n}+i T_{\xi}\right)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathcal{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(\left(I_{n}+i T_{\xi}\right)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{||_{\nu} \mid+1}{2}}} \mathrm{~d} T_{\xi} \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\tau}} \prod_{\xi=1}^{k} \frac{\mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right) \pi^{\tau_{\xi}}}{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)} \\
& =\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right) \prod_{\xi=1}^{k} \frac{\mathcal{I}_{\mathcal{G}_{\xi}}\left(\beta, I_{n}\right)}{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}
\end{aligned}
$$

A.2. An alternative proof of (9). We first use the inclusion-exclusion principle to prove the following result, which establishes a relationship between the sizes of the maximal cliques and the minimal separators of a chordal graph.

Lemma A.1. Let $C_{1}, \ldots, C_{m}$ be subsets of $\{1, \ldots, n\}$ such that $C_{1} \cup \cdots \cup C_{m}=$ $\{1, \ldots, n\}$. Suppose that the sequence $C_{1}, \ldots, C_{m}$ satisfies the running intersection property. For $1 \leq \nu \leq m-1$, let $\mathrm{S}_{\nu}=\left(\mathrm{C}_{1} \cup \cdots \cup \mathrm{C}_{\nu}\right) \cap \mathrm{C}_{\nu+1}$. Then,

$$
\left|\mathrm{C}_{1}\right|+\cdots+\left|\mathrm{C}_{m}\right|-\left(\left|\mathrm{S}_{1}\right|+\cdots+\left|\mathrm{S}_{m-1}\right|\right)=n
$$

PROOF. By the inclusion-exclusion principle,

$$
\begin{aligned}
n= & \sum_{\mu=1}^{m}\left|\mathrm{C}_{\mu}\right|-\sum_{1 \leq \nu<\mu \leq m}\left|\mathrm{C}_{\nu} \cap \mathrm{C}_{\mu}\right|+\sum_{1 \leq \nu<\xi<\mu \leq m}\left|\mathrm{C}_{\nu} \cap \mathrm{C}_{\xi} \cap \mathrm{C}_{\mu}\right|-\cdots \\
& +(-1)^{m+1}\left|\mathrm{C}_{1} \cap \cdots \cap \mathrm{C}_{m}\right|
\end{aligned}
$$

$$
=\sum_{\mu=1}^{m}\left(P_{\mu, 1}+\cdots+P_{\mu, \mu}\right)
$$

where

$$
P_{\mu, \ell}=(-1)^{\ell+1} \sum_{1 \leq \nu_{1}<\cdots<\nu_{\ell-1}<\mu}\left|\mathrm{C}_{\nu_{1}} \cap \cdots \cap \mathrm{C}_{\nu_{\ell-1}} \cap \mathrm{C}_{\mu}\right|
$$

denotes the sum of the terms associated with the intersection of $\ell$ sets and $\mu$ is the largest index.

Fix $2 \leq \mu \leq m$, we first show that $P_{\mu, 1}+\cdots+P_{\mu, \mu}=\left|\mathrm{C}_{\mu}\right|-\left|\mathrm{S}_{\mu-1}\right|$. Let $\gamma \leq \mu-1$ be an index such that $\mathrm{S}_{\mu-1}=\mathrm{C}_{\gamma} \cap \mathrm{C}_{\mu}$. We further split $P_{\mu, \ell}$ into two parts, depending on the existence of $\mathrm{C}_{\gamma}$, i.e., $P_{\mu, \ell}=P_{\mu, \ell}^{+}+P_{\mu, \ell}^{-}$, where

$$
P_{\mu, \ell}^{+}=(-1)^{\ell+1} \sum_{\substack{1 \leq \nu_{1}<\cdots<\nu_{\ell-2}<\mu \\ \gamma \notin\left\{\nu_{1}, \ldots, \nu_{\ell-2}\right\}}}\left|\mathrm{C}_{\nu_{1}} \cap \cdots \cap \mathrm{C}_{\nu_{\ell-2}} \cap \mathrm{C}_{\gamma} \cap \mathrm{C}_{\mu}\right|
$$

and

$$
P_{\mu, \ell}^{-}=(-1)^{\ell+1} \sum_{\substack{1 \leq \nu_{1}<\cdots<\nu_{\ell-1}<\mu \\ \gamma \notin\left\{\nu_{1}, \ldots, \nu_{\ell-1}\right\}}}\left|\mathrm{C}_{\nu_{1}} \cap \cdots \cap \mathrm{C}_{\nu_{\ell-1}} \cap \mathrm{C}_{\mu}\right|
$$

For $1 \leq \nu_{1}<\cdots<\nu_{\ell-2}<\mu$ with $\gamma \notin\left\{\nu_{1}, \ldots, \nu_{\ell-2}\right\}$, the running intersection property implies that

$$
\mathrm{C}_{\nu_{1}} \cap \cdots \cap \mathrm{C}_{\nu_{\ell-2}} \cap \mathrm{C}_{\gamma} \cap \mathrm{C}_{\mu}=\mathrm{C}_{\nu_{1}} \cap \cdots \cap \mathrm{C}_{\nu_{\ell-2}} \cap \mathrm{C}_{\mu}
$$

Thus, $P_{\mu, \ell}^{+}=-P_{\mu, \ell-1}^{-}$, for $3 \leq \ell \leq \mu$. Altogether with the observation that both $P_{\mu, \mu}^{-}$and $P_{\mu, 1}^{+}$ are zero, we have

$$
P_{\mu, 1}+\cdots+P_{\mu, \mu}=P_{\mu, 1}^{-}+P_{\mu, 2}^{+}=\left|\mathrm{C}_{\mu}\right|-\left|\mathrm{C}_{\gamma} \cap \mathrm{C}_{\mu}\right|=\left|\mathrm{C}_{\mu}\right|-\left|\mathrm{S}_{\mu-1}\right|
$$

as claimed.

Finally, as desired, we have

$$
n=\left|\mathrm{C}_{1}\right|+\sum_{\mu=2}^{m}\left(\left|\mathrm{C}_{\mu}\right|-\left|\mathrm{S}_{\mu-1}\right|\right)
$$

Let $\mathcal{G}$ be a graph on $n$ vertices with minimum fill-in 1 , and let $\mathcal{G}^{*}$ be a minimum chordal completion of $\mathcal{G}$. By Theorem 1.1, we have

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|C_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \mathrm{~d} T
$$

where $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ are the maximal cliques of $\mathcal{G}^{*}$ and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1}$ are the minimal separators. Without loss of generality, assume that $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m}$ forms a perfect sequence of cliques.

Let $e=\left\{v_{r}, v_{s}\right\}$ be the missing edge. Note that all entries of a matrix $T \in \mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$ are zero, except $t_{r, s}=t_{s, r}=: t \in \mathbb{R}$. For a clique $C \subseteq \mathcal{V}\left(\mathcal{G}^{*}\right)$, we have

$$
\operatorname{det}\left(I_{n}+i T\right)[\mathrm{C}]= \begin{cases}1+t^{2}, & \text { if } e \text { belongs to the clique } \mathrm{C} \\ 1, & \text { otherwise }\end{cases}
$$

Now, we find the exponent of $1+t^{2}$ in the integrand. Suppose that the vertices $v_{r}$ and $v_{s}$ are contained in $k$ maximal cliques of $\mathcal{G}^{*}$, say $\mathrm{C}_{\alpha_{1}}, \ldots, \mathrm{C}_{\alpha_{k}}$, where $\alpha_{1}<\cdots<\alpha_{k}$. Then, the vertices $v_{r}$ and $v_{s}$ are contained in $\mathrm{S}_{\nu}$ if and only if $\nu+1 \in\left\{\alpha_{2}, \ldots, \alpha_{k}\right\}$. By Lemma A.1, the exponent of interest is

$$
-\beta-\frac{1}{2}-\frac{\left|\mathrm{C}_{\alpha_{1}}\right|+\cdots+\left|\mathrm{C}_{\alpha_{k}}\right|}{2}+\frac{\left|\mathrm{S}_{\alpha_{2}-1}\right|+\cdots+\left|\mathrm{S}_{\alpha_{k}-1}\right|}{2}=-\beta-\frac{w+3}{2}
$$

where $w$ is the number of common neighbours of the end vertices of $e$.

As a result,

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right) & =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi} \int_{\mathbb{R}}\left(1+t^{2}\right)^{-\beta-\frac{w+3}{2}} \mathrm{~d} t \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\frac{1}{2}}} \frac{\Gamma\left(\beta+\frac{w+2}{2}\right)}{\Gamma\left(\beta+\frac{w+3}{2}\right)}
\end{aligned}
$$

A.3. Proof of Corollary 4.7. By Theorem 1.1, we have

$$
\mathcal{I}_{\mathcal{G}}(\beta, D)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left((D+i T)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \operatorname{det}\left((D+i T)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}}} \mathrm{~d} T
$$

where $\mathrm{C}_{1}, \ldots, \mathrm{C}_{m} \subseteq \mathcal{V}(\mathcal{G})$ are the maximal cliques of $\mathcal{G}^{*}$ and $\mathrm{S}_{1}, \ldots, \mathrm{S}_{m-1} \subseteq \mathcal{V}(\mathcal{G})$ are the minimal separators. Let $T \in \mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)$. By assumption, the induced subgraph $\mathcal{G}\left[\mathrm{C}_{\mu}\right]$, where $1 \leq \mu \leq m$, is star-complementary with respect to the sets $\mathcal{F}\left(\mathcal{G}\left[\mathrm{C}_{\mu}\right]\right)$, and hence

$$
\operatorname{det}\left(I_{n}+i T\right)\left[\mathrm{C}_{\mu}\right]=\prod_{\mathfrak{S} \in \mathcal{F}\left(\mathcal{G}\left[\mathrm{C}_{\mu}\right]\right)} \operatorname{det}\left(I_{n}+i T\right)[\mathfrak{S}]
$$

Since each separator $\mathrm{S}_{\nu}$, where $1 \leq \nu \leq m-1$, is the intersection of two maximal cliques, the induced subgraph $\mathcal{G}\left[\mathrm{S}_{\nu}\right]$ is also star-complementary, which implies

$$
\operatorname{det}\left(I_{n}+i T\right)\left[\mathrm{S}_{\nu}\right]=\prod_{\mathfrak{S} \in \mathcal{F}\left(\mathcal{G}\left[\mathrm{S}_{\nu}\right]\right)} \operatorname{det}\left(I_{n}+i T\right)[\mathfrak{S}]
$$

Now, let $\mathfrak{S} \in \mathcal{F}\left(\mathcal{G}\left[\mathrm{C}_{1}\right]\right) \cup \cdots \cup \mathcal{F}\left(\mathcal{G}\left[\mathrm{C}_{m}\right]\right) \cup \mathcal{F}\left(\mathcal{G}\left[\mathrm{S}_{1}\right]\right) \cup \cdots \cup \mathcal{F}\left(\mathcal{G}\left[\mathrm{S}_{m-1}\right]\right)$. Then the complement of the induced subgraph $\mathcal{G}[\mathfrak{S}]$ is a star. Consequently,

$$
\operatorname{det}\left(I_{n}+i T\right)[\mathfrak{S}]=1+\sum_{\substack{v_{r}, v_{s} \in \mathfrak{S} \\\left\{v_{r}, v_{s}\right\} \in \mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})}} t_{r, s}^{2}
$$

Let $\tau=\left|\mathcal{E}\left(\mathcal{G}^{*}\right)\right|-|\mathcal{E}(\mathcal{G})|$. By Theorem 1.1, (18), (19) and (20), we have

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)
$$

$$
\begin{aligned}
& =\frac{1}{\pi^{\tau}} \int_{\mathbb{S}\left(\mathcal{G}, \mathcal{G}^{*}\right)} \frac{\prod_{\mu=1}^{m} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{C}_{\mu}\right]\right)^{-\beta-\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}} \Gamma_{\left|\mathrm{C}_{\mu}\right|}\left(\beta+\frac{\left|\mathrm{C}_{\mu}\right|+1}{2}\right)}{\prod_{\nu=1}^{m-1} \operatorname{det}\left(\left(I_{n}+i T\right)\left[\mathrm{S}_{\nu}\right]\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}} \Gamma_{\left|\mathrm{S}_{\nu}\right|}\left(\beta+\frac{\left|\mathrm{S}_{\nu}\right|+1}{2}\right)} \mathrm{d} T \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{\tau}} \int_{\mathbb{R}^{\tau}} \frac{\prod_{\mu=1}^{m} \prod_{\mathfrak{S} \in \mathcal{F}\left(\mathrm{C}_{\mu}\right)}\left(\operatorname{det}\left(I_{n}+i T\right)[\mathfrak{S}]\right)^{-\beta-\frac{\left|\mathcal{C}_{\mu}\right|+1}{2}}}{\prod_{\nu=1}^{m-1} \prod_{\mathfrak{S} \in \mathcal{F}\left(\mathcal{S}_{\nu}\right)}\left(\operatorname{det}\left(I_{n}+i T\right)[\mathfrak{S}]\right)^{-\beta-\frac{\left|\mathfrak{S}_{\nu}\right|+1}{2}}} \mathrm{~d} T
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-29.jpg?height=300&width=1427&top_left_y=208&top_left_x=341)

A.4. Proof of Corollary 4.8. Let $\mathcal{G}^{*}=\mathcal{G}^{*}\left(m ; k_{1}, \ldots, k_{\ell}\right)$ be a chordal completion of $\mathcal{G}$ and it is clear that $\mathcal{G}$ has starry fill-ins. By Corollary 4.7,

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right) \\
= & \frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right)}{\pi^{\ell}} \\
& \times \int_{\mathbb{R}^{\ell}} \frac{\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right)^{-\beta-\frac{m+1}{2}}\left(1+t_{1}^{2}\right)^{-\beta-\frac{k_{1}+3}{2}} \cdots\left(1+t_{\ell}^{2}\right)^{-\beta-\frac{k_{\ell}+3}{2}}}{\left(1+t_{1}^{2}\right)^{-\beta-\frac{3}{2}} \cdots\left(1+t_{\ell}^{2}\right)^{-\beta-\frac{3}{2}}} \mathrm{~d} t_{1} \cdots \mathrm{d} t_{\ell} \\
= & \frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right)}{\pi^{\ell}} 2^{\ell} \\
& \times \int_{0}^{\infty} \cdots \int_{0}^{\infty}\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right)^{-\beta-\frac{m+1}{2}}\left(1+t_{1}^{2}\right)^{-\frac{k_{1}}{2}} \cdots\left(1+t_{\ell}^{2}\right)^{-\frac{k_{\ell}}{2}} \mathrm{~d} t_{1} \cdots \mathrm{d} t_{\ell}
\end{aligned}
$$

As $\mathcal{G}^{*}$ is chordal, we have

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right) \\
= & \pi^{k_{1}+\cdots+k_{\ell}} \Gamma_{k_{1}}\left(\beta+\frac{k_{1}+3}{2}\right) \cdots \Gamma_{k_{\ell}}\left(\beta+\frac{k_{\ell}+3}{2}\right) \Gamma_{m}\left(\beta+\frac{m+1}{2}\right) .
\end{aligned}
$$

Finally, we simplify the $\ell$-dimensional integral. For positive real numbers $t_{1}, \ldots, t_{\ell}$, we substitute

$$
y=\frac{\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right) x}{2}
$$

into the gamma function

$$
\Gamma\left(\beta+\frac{m+1}{2}\right)=\int_{0}^{\infty} y^{\beta+\frac{m+1}{2}-1} e^{-y} \mathrm{~d} y
$$

to obtain

$$
\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right)^{-\beta-\frac{m+1}{2}}=\int_{0}^{\infty} \frac{x^{\beta+\frac{m+1}{2}-1} e^{-\frac{\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right) x}{2}}}{\Gamma\left(\beta+\frac{m+1}{2}\right) 2^{\beta+\frac{m+1}{2}}} \mathrm{~d} x
$$

Hence,

$$
\begin{aligned}
& 2^{\ell} \int_{0}^{\infty} \cdots \int_{0}^{\infty}\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right)^{-\beta-\frac{m+1}{2}}\left(1+t_{1}^{2}\right)^{-\frac{k_{1}}{2}} \cdots\left(1+t_{\ell}^{2}\right)^{-\frac{k_{\ell}}{2}} \mathrm{~d} t_{1} \cdots \mathrm{d} t_{\ell} \\
= & 2^{\ell} \int_{0}^{\infty} \cdots \int_{0}^{\infty} \frac{x^{\beta+\frac{m+1}{2}-1} e^{-\frac{\left(1+t_{1}^{2}+\cdots+t_{\ell}^{2}\right) x}{2}}}{\Gamma\left(\beta+\frac{m+1}{2}\right) 2^{\beta+\frac{m+1}{2}}}\left(1+t_{1}^{2}\right)^{-\frac{k_{1}}{2}} \cdots\left(1+t_{\ell}^{2}\right)^{-\frac{k_{\ell}}{2}} \mathrm{~d} x \mathrm{~d} t_{1} \cdots \mathrm{d} t_{\ell} \\
= & \int_{0}^{\infty} \frac{x^{\beta+\frac{m+1}{2}-1} e^{-\frac{x}{2}}}{\Gamma\left(\beta+\frac{m+1}{2}\right) 2^{\beta+\frac{m+1}{2}}} \prod_{\mu=1}^{\ell}\left(2 \int_{0}^{\infty} e^{-\frac{t_{\mu}^{2} x}{2}}\left(1+t_{\mu}^{2}\right)^{-\frac{k_{\mu}}{2}} \mathrm{~d} t_{\mu}\right) \mathrm{d} x
\end{aligned}
$$

For $\mu=1, \ldots, \ell$, a change of variable $t_{\mu} \rightarrow \sqrt{t_{\mu}}$ gives

$$
2 \int_{0}^{\infty} e^{-\frac{t_{\mu}^{2} x}{2}}\left(1+t_{\mu}^{2}\right)^{-\frac{k_{\mu}}{2}} \mathrm{~d} t_{\mu}=\int_{0}^{\infty} e^{-\frac{t_{\mu} x}{2}}\left(1+t_{\mu}\right)^{-\frac{k_{\mu}}{2}} t_{\mu}^{-\frac{1}{2}} \mathrm{~d} t_{\mu}=\pi^{\frac{1}{2}} U\left(\frac{1}{2}, \frac{3}{2}-\frac{k_{\mu}}{2}, \frac{x}{2}\right)
$$

which implies

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right)= & \pi^{k_{1}+\cdots+k_{\ell}-\frac{\ell}{2}} \Gamma_{m}\left(\beta+\frac{m+1}{2}\right) \prod_{\mu=1}^{\ell} \Gamma_{k_{\mu}}\left(\beta+\frac{k_{\mu}+3}{2}\right) \\
& \times \int_{0}^{\infty} \frac{x^{\beta+\frac{m+1}{2}-1} e^{-\frac{x}{2}}}{\Gamma\left(\beta+\frac{m+1}{2}\right) 2^{\beta+\frac{m+1}{2}}} \prod_{\mu=1}^{\ell} U\left(\frac{1}{2}, \frac{3}{2}-\frac{k_{\mu}}{2}, \frac{x}{2}\right) \mathrm{d} x
\end{aligned}
$$

For computational purposes, we transform the domain of the integral into a bounded one using the fact that

$$
\frac{x^{\beta+\frac{m+1}{2}-1} e^{-\frac{x}{2}}}{\Gamma\left(\beta+\frac{m+1}{2}\right) 2^{\beta+\frac{m+1}{2}}}=f_{\chi^{2}(2 \beta+m+1)}(x)=F_{\chi^{2}(2 \beta+m+1)}^{\prime}(x)
$$

is the probability density function of chi-squared distribution with $(2 \beta+m+1)$ degrees of freedom. It follows that

$$
\begin{aligned}
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{m+k_{1}+\cdots+k_{\ell}}\right)= & \pi^{k_{1}+\cdots+k_{\ell}-\frac{\ell}{2}} \Gamma_{m}\left(\beta+\frac{m+1}{2}\right) \prod_{\mu=1}^{\ell} \Gamma_{k_{\mu}}\left(\beta+\frac{k_{\mu}+3}{2}\right) \\
& \times \int_{0}^{1} \prod_{\mu=1}^{\ell} U\left(\frac{1}{2}, \frac{3}{2}-\frac{k_{\mu}}{2}, \frac{F_{\chi^{2}(2 \beta+m+1)}^{-1}(x)}{2}\right) \mathrm{d} x
\end{aligned}
$$

A.5. Proof of Corollary 4.10. By assumption, $\left\{v_{1}, v_{2}\right\} \in \mathcal{E}(\mathcal{G})$. Let $\mathcal{G}_{0}$ be the induced subgraph $\mathcal{G}\left[\left(\mathcal{N}_{\mathcal{G}}\left(v_{1}\right) \cap \mathcal{N}_{\mathcal{G}}\left(v_{2}\right)\right) \cup\left\{v_{1}, v_{2}, v_{3}\right\}\right]$, obtained from the common neighbours of $v_{1}$ and $v_{2}$, together with vertices $v_{1}, v_{2}$ and $v_{3}$. Let $\mathcal{G}_{0}^{*}$ be the corresponding chordal completion by adding the edges $e_{1}$ and $e_{2}$. Let $C_{1}^{(0)}, \ldots, C_{m}^{(0)}$ be a perfect sequence of cliques of $\mathcal{G}_{0}^{*}$, and let $S_{1}^{(0)}, \ldots, S_{m-1}^{(0)}$ be the minimal separators.

For $\mu=1,2$, let $\mathcal{G}_{\mu}$ be the induced subgraph $\mathcal{G}\left[\left(\mathcal{N}_{\mathcal{G}}\left(v_{\mu}\right) \cap \mathcal{N}_{\mathcal{G}}\left(v_{3}\right)\right) \cup\left(\mathcal{N}_{\mathcal{G}}\left(v_{1}\right) \cap\right.\right.$ $\left.\left.\mathcal{N}_{\mathcal{G}}\left(v_{2}\right)\right) \cup\left\{v_{1}, v_{2}, v_{3}\right\}\right]$, obtained from the common neighbours of $v_{\mu}$ and $v_{3}$, and the common neighbours of $v_{1}$ and $v_{2}$, together with vertices $v_{1}, v_{2}$ and $v_{3}$. Let $\mathcal{G}_{\mu}^{*}$ be the corresponding chordal completion by adding the edges $e_{1}$ and $e_{2}$. Let $\mathrm{C}_{1}^{(0)}, \ldots, \mathrm{C}_{m}^{(0)}, \mathrm{C}_{1}^{(\mu)}, \ldots, \mathrm{C}_{k_{\mu}}^{(\mu)}$ be a perfect sequence of cliques of $\mathcal{G}_{\mu}^{*}$, and let $\mathrm{S}_{1}^{(0)}, \ldots, \mathrm{S}_{m-1}^{(0)}, \mathrm{S}_{1}^{(\mu)}, \ldots, \mathrm{S}_{k_{\mu}}^{(\mu)}$ be the minimal separators. (For any perfect sequence of cliques of $\mathcal{G}_{\mu}^{*}$, the running intersection property is not violated if $\mathrm{C}_{1}^{(0)}, \ldots, \mathrm{C}_{m}^{(0)}$ are moved to the front.)

Note that the assumption that $\mathcal{G}$ is prime implies that every maximal clique of $\mathcal{G}^{*}$ contains at least one of the two missing edges. Therefore, $\mathrm{C}_{1}^{(0)}, \ldots, \mathrm{C}_{m}^{(0)}, \mathrm{C}_{1}^{(1)}, \ldots, \mathrm{C}_{k_{1}}^{(1)}, \mathrm{C}_{1}^{(2)}, \ldots, \mathrm{C}_{k_{2}}^{(2)}$ is a perfect sequence of cliques of $\mathcal{G}^{*}$, and the minimal separators are $S_{1}^{(0)}, \ldots, S_{m-1}^{(0)}$, $\mathrm{S}_{1}^{(1)}, \ldots, \mathrm{S}_{k_{1}}^{(1)}, \mathrm{S}_{1}^{(2)}, \ldots, \mathrm{S}_{k_{2}}^{(2)}$. Then, by Corollary 4.7,

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{2}}
$$

$$
\begin{aligned}
& \times \int_{\mathbb{R}^{2}} \frac{\prod_{\nu=1}^{m}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\beta-\frac{\left|\mathrm{C}_{\nu}^{(0)}\right|+1}{2}} \prod_{\nu=1}^{k_{1}}\left(1+t_{1}^{2}\right)^{-\beta-\frac{\left|\mathrm{C}_{\nu}^{(1)}\right|+1}{2}} \prod_{\nu=1}^{k_{2}}\left(1+t_{2}^{2}\right)^{-\beta-\frac{\left|\mathrm{|l}_{\nu}^{(2)}\right|+1}{2}}}{\left.\prod_{\nu=1}^{2}+t_{2}^{2}\right)^{-\beta-\frac{\mathrm{S}_{\nu}^{(0)}}{2}+1+1}} \prod_{\nu=1}^{k_{1}}\left(1+t_{1}^{2}\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}^{(1)}\right|+1}{2}} \prod_{\nu=1}^{k_{2}}\left(1+t_{2}^{2}\right)^{-\beta-\frac{\mathbf{S S}_{\nu}^{(2)} \mid+1}{2}} \mathrm{~d} t_{2} \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{2}} \int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\gamma}\left(1+t_{1}^{2}\right)^{-r}\left(1+t_{2}^{2}\right)^{-s} \mathrm{~d} t_{1} \mathrm{~d} t_{2}
\end{aligned}
$$

where $r=\frac{1}{2} \sum_{\nu=1}^{k_{1}}\left(\left|\mathrm{C}_{\nu}^{(1)}\right|-\left|\mathrm{S}_{\nu}^{(1)}\right|\right), s=\frac{1}{2} \sum_{\nu=1}^{k_{2}}\left(\left|\mathrm{C}_{\nu}^{(2)}\right|-\left|\mathrm{S}_{\nu}^{(2)}\right|\right)$, and

$$
\gamma=\beta+\frac{1}{2}\left(\left|\mathrm{C}_{1}\right|+\cdots+\left|\mathrm{C}_{m}\right|-\left|\mathrm{S}_{1}\right|-\cdots-\left|\mathrm{S}_{m-1}\right|+1\right)
$$

We use Lemma A. 1 to write $r, s, \gamma$ in terms of $w, w_{1}, w_{2}$. With the graph $\mathcal{G}_{0}^{*}$, the lemma implies

$$
\left|\mathrm{C}_{1}^{(0)}\right|+\cdots+\left|\mathrm{C}_{m}^{(0)}\right|-\left|\mathrm{S}_{1}^{(0)}\right|-\cdots-\left|\mathrm{S}_{m-1}^{(0)}\right|=w+3
$$

and so $\gamma=\beta+\frac{w+4}{2}$. For $\mu=1,2$, we again apply Lemma A. 1 (with the graph $\mathcal{G}_{\mu}^{*}$ ) to obtain

$$
\sum_{\nu=1}^{m}\left|\mathbf{C}_{\nu}^{(0)}\right|+\sum_{\nu=1}^{k_{\mu}}\left|\mathbf{C}_{\nu}^{(\mu)}\right|-\sum_{\nu=1}^{m-1}\left|\mathbf{S}_{\nu}^{(0)}\right|-\sum_{\nu=1}^{k_{\mu}}\left|\mathbf{S}_{\nu}^{(\mu)}\right|=w_{\mu}+3
$$

which implies

$$
\sum_{\nu=1}^{k_{\mu}}\left|\mathrm{C}_{\nu}^{(\mu)}\right|-\sum_{\nu=1}^{k_{\mu}}\left|\mathrm{S}_{\nu}^{(\mu)}\right|=w_{\mu}-w
$$

Thus, $r=\frac{w_{1}-w}{2}$ and $s=\frac{w_{2}-w}{2}$.

It remains to solve the integral

$$
\int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\gamma}\left(1+t_{1}^{2}\right)^{-r}\left(1+t_{2}^{2}\right)^{-s} \mathrm{~d} t_{1} \mathrm{~d} t_{2}
$$

We use Euler's integral representation of the hypergeometric function ${ }_{2} F_{1}$ to obtain

$$
\begin{aligned}
& \int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\gamma}\left(1+t_{1}^{2}\right)^{-r}\left(1+t_{2}^{2}\right)^{-s} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \\
= & \frac{\Gamma\left(\gamma+r-\frac{1}{2}\right) \Gamma\left(\frac{1}{2}\right)}{\Gamma(\gamma+r)} \int_{0}^{1} t_{2}^{\gamma+s-\frac{3}{2}}\left(1-t_{2}\right)^{-\frac{1}{2}}{ }_{2} F_{1}\left(\gamma, \frac{1}{2} ; \gamma+r ; 1-t_{2}\right) \mathrm{d} t_{2}
\end{aligned}
$$

Finally, we substitute $1-t_{2} \rightarrow t_{2}$ and the integral representation of ${ }_{3} F_{2}$ implies

$$
\begin{aligned}
& \int_{\mathbb{R}^{2}}\left(1+t_{1}^{2}+t_{2}^{2}\right)^{-\gamma}\left(1+t_{1}^{2}\right)^{-r}\left(1+t_{2}^{2}\right)^{-s} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \\
= & \frac{\Gamma\left(\gamma+r-\frac{1}{2}\right) \Gamma\left(\frac{1}{2}\right)}{\Gamma(\gamma+r)} \int_{0}^{1} t_{2}^{-\frac{1}{2}}\left(1-t_{2}\right)^{\gamma+s-\frac{3}{2}}{ }_{2} F_{1}\left(\gamma, \frac{1}{2} ; \gamma+r ; t_{2}\right) \mathrm{d} t_{2} \\
= & \pi \frac{\Gamma\left(\gamma+r-\frac{1}{2}\right)}{\Gamma(\gamma+r)} \frac{\Gamma\left(\gamma+s-\frac{1}{2}\right)}{\Gamma(\gamma+s)}{ }_{3} F_{2}\left(\gamma, \frac{1}{2}, \frac{1}{2} ; \gamma+r, \gamma+s ; 1\right) .
\end{aligned}
$$

We complete the proof by plugging in $\gamma=\beta+\frac{w+4}{2}, r=\frac{w_{1}-w}{2}$ and $s=\frac{w_{2}-w}{2}$.

## APPENDIX B: MISSING EDGES FORM A TRIANGLE, $D=I$

Let $\mathcal{G}$ be a prime graph with $n$ vertices and let $\mathcal{G}^{*}$ be a chordal completion. Suppose that the missing edges form a triangle, say $e_{1}=\left\{v_{1}, v_{2}\right\}, e_{2}=\left\{v_{2}, v_{3}\right\}$ and $e_{3}=\left\{v_{3}, v_{1}\right\}$. In this section, we aim to write the integral $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)$ as a one-dimensional integral, for real number $\beta>-1$.

Since $\mathcal{G}$ is prime, every maximal clique of $\mathcal{G}^{*}$ contains either one missing edge or all three of them. Let $\mathrm{C}_{1}, \ldots, \mathrm{C}_{k}$ be the maximal cliques that contain all three missing edges. For $1 \leq \mu \leq 3$, let $\mathrm{C}_{1}^{(\mu)}, \ldots, \mathrm{C}_{k_{\mu}}^{(\mu)}$ be the maximal cliques that contains the edge $e_{\mu}$ but not the other two missing edges. Note that $k \geq 1$.

It is easy to see that among the minimal separators of $\mathcal{G}^{*}$, exactly $k-1$ of them (say $\mathrm{S}_{1}, \ldots, \mathrm{S}_{k-1}$ ) contain all three missing edges, and $k_{\mu}$ of them (say $\left.\mathrm{S}_{1}^{(\mu)}, \ldots, \mathrm{S}_{k_{\mu}}^{(\mu)}\right)$ contain the edge $e_{\mu}$ but not the other two missing edges, for $\mu=1,2,3$. By Theorem 1.1, we have

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right) \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{3}}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-32.jpg?height=234&width=1355&top_left_y=997&top_left_x=404)

$$
\begin{aligned}
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{3}} \\
& \times \int_{\mathbb{R}^{3}} \frac{\prod_{\nu=1}^{k}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\beta-\frac{\left|c_{\nu}\right|+1}{2}} \prod_{\mu=1}^{3} \prod_{\nu=1}^{k_{\mu}}\left(1+t_{\mu}^{2}\right)^{-\beta-\frac{\left|c_{\nu}^{(\mu)}\right|+1}{2}}}{\prod_{\nu=1}^{k-1}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\beta-\frac{\left|\mathrm{Ss}_{\nu}\right|+1}{2}} \prod_{\mu=1}^{3} \prod_{\nu=1}^{k_{\mu}}\left(1+t_{\mu}^{2}\right)^{-\beta-\frac{\left|\mathrm{S}_{\nu}^{(\mu)}\right|+1}{2}}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3} \\
& =\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right)}{\pi^{3}} \\
& \times \int_{\mathbb{R}^{3}}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\beta-\frac{\gamma}{2}}\left(1+t_{1}^{2}\right)^{-\frac{\gamma_{1}}{2}}\left(1+t_{2}^{2}\right)^{-\frac{\gamma_{2}}{2}}\left(1+t_{3}^{2}\right)^{-\frac{\gamma_{3}}{2}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
\end{aligned}
$$

where $\gamma=\sum_{\nu=1}^{k}\left(\left|\mathbf{C}_{\nu}\right|+1\right)-\sum_{\nu=1}^{k-1}\left(\left|\mathrm{~S}_{\nu}\right|+1\right)$ and $\gamma_{\mu}=\sum_{\nu=1}^{k_{\mu}}\left(\left|\mathbf{C}_{\nu}^{(\mu)}\right|+1\right)-\sum_{\nu=1}^{k_{\mu}}\left(\left|\mathbf{S}_{\nu}^{(\mu)}\right|+1\right)>0$, for $\mu=1,2,3$. We note that $\gamma \geq 4$ because $\left|\mathrm{C}_{1}\right| \geq 3$ and $\left|\mathrm{S}_{\nu}\right| \leq\left|\mathrm{C}_{\nu+1}\right|$ for all $1 \leq \nu \leq k-1$.

Now, we define a graph $\mathcal{H}_{1}^{*}=\mathcal{H}_{1}^{*}\left(\gamma_{1}, \gamma_{2}, \gamma_{3}\right)$ with vertex set

$$
\mathcal{V}\left(\mathcal{H}_{1}^{*}\right)=\left\{v_{1}, v_{2}, v_{3}\right\} \sqcup\left\{u_{\mu}: 1 \leq \mu \leq k_{1}\right\} \sqcup\left\{w_{\mu}: 1 \leq \mu \leq k_{2}\right\} \sqcup\left\{x_{\mu}: 1 \leq \mu \leq k_{3}\right\}
$$

and the edge set is defined by connecting pairs of vertices inside one of the following three sets: $\left\{u_{\mu}: 1 \leq \mu \leq \gamma_{1}\right\} \sqcup\left\{v_{1}, v_{2}\right\},\left\{w_{\mu}: 1 \leq \mu \leq \gamma_{2}\right\} \sqcup\left\{v_{2}, v_{3}\right\},\left\{x_{\mu}: 1 \leq\right.$ $\left.\mu \leq \gamma_{3}\right\} \sqcup\left\{v_{3}, v_{1}\right\}$. Furthermore, we define $\mathcal{H}=\mathcal{H}\left(\gamma_{1}, \gamma_{2}, \gamma_{3}\right)$ to be the graph obtained from $\mathcal{H}_{1}^{*}$ by removing the three edges $\left\{v_{1}, v_{2}\right\},\left\{v_{2}, v_{3}\right\},\left\{v_{3}, v_{1}\right\}$. We define one last graph $\mathcal{H}_{2}^{*}=\mathcal{H}_{2}^{*}\left(\gamma_{1}, \gamma_{2}, \gamma_{3}\right)$ on the same vertex set, by adding the edges $\left\{v_{1}, v_{2}\right\},\left\{v_{1}, v_{3}\right\}$ and $\left\{v_{1}, w_{1}\right\}, \ldots,\left\{v_{1}, w_{\gamma_{2}}\right\}$ to the graph $\mathcal{H}$. It is clear that both $\mathcal{H}_{1}^{*}$ and $\mathcal{H}_{2}^{*}$ are chordal completions of $\mathcal{H}$. Figure 15 gives an example of these graphs.
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-33.jpg?height=460&width=896&top_left_y=214&top_left_x=608)

Fig 15: For both graphs, the solid edges represent those in $\mathcal{H}(1,2,3)$. Together with the dashed edges, the graph on the left is $\mathcal{H}_{1}^{*}(1,2,3)$, the graph on the right is $\mathcal{H}_{2}^{*}(1,2,3)$.

As in Section 5.1, we find the integral $\mathcal{I}_{\mathcal{H}}\left(\tilde{\beta}_{2} I_{m}\right)$, where $m:=3+\gamma_{1}+\gamma_{2}+\gamma_{3}$, using these two chordal completions, for real number $\beta>-1$. First, we use Theorem 1.1 with $\mathcal{H}_{1}^{*}$ :

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{H}}\left(\tilde{\beta}, I_{m}\right) \\
= & \frac{\mathcal{I}_{\mathcal{H}_{1}^{*}}\left(\tilde{\beta}, I_{m}\right)}{\pi^{3}} \int_{\mathbb{R}^{3}} \frac{\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\beta-2} \prod_{\mu=1}^{3}\left(1+t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{\mu}+3}{2}}}{\prod_{\mu=1}^{3}\left(1+t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{3}{2}}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3} \\
= & \frac{\mathcal{I}_{\mathcal{H}_{1}^{*}}\left(\tilde{\beta}, I_{m}\right)}{\pi^{3}} \\
& \times \int_{\mathbb{R}^{3}}\left(1+t_{1}^{2}+t_{2}^{2}+t_{3}^{2}-2 i t_{1} t_{2} t_{3}\right)^{-\tilde{\beta}-2}\left(1+t_{1}^{2}\right)^{-\frac{\gamma_{1}}{2}}\left(1+t_{2}^{2}\right)^{-\frac{\gamma_{2}}{2}}\left(1+t_{3}^{2}\right)^{-\frac{\gamma_{3}}{2}} \mathrm{~d} t_{1} \mathrm{~d} t_{2} \mathrm{~d} t_{3}
\end{aligned}
$$

Comparing the above two integrals, we take $\tilde{\beta}=\beta+\frac{\gamma}{2}-2>-1$ and obtain

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)=\frac{\mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right) \mathcal{I}_{\mathcal{H}}\left(\beta+\frac{\gamma}{2}-2, I_{m}\right)}{\mathcal{I}_{\mathcal{H}_{1}^{*}}\left(\beta+\frac{\gamma}{2}-2, I_{m}\right)}
$$

Next, we find the integral $\mathcal{I}_{\mathcal{H}}\left(\beta, I_{m}\right)$ using Theorem 1.1 with $\mathcal{H}_{2}^{*}$ :

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{H}}\left(\tilde{\beta}, I_{m}\right) \\
= & \frac{\mathcal{I}_{\mathcal{H}_{2}^{*}}\left(\tilde{\beta}, I_{m}\right)}{\pi^{\gamma_{2}+2}} \\
& \times \int_{\mathbb{R}^{\gamma_{2}+2}} \frac{\left(1+\sum_{\mu=1}^{\gamma_{2}+1} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+3}{2}}\left(1+\sum_{\mu=2}^{\gamma_{2}+2} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+3}{2}}\left(1+t_{\gamma_{2}+2}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{3}+3}{2}}}{\left(1+t_{1}^{2}\right)^{-\tilde{\beta}-\frac{3}{2}}\left(1+t_{\gamma_{2}+2}^{2}\right)^{-\tilde{\beta}-\frac{3}{2}}\left(1+\sum_{\mu=2}^{\gamma_{2}+1} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+2}{2}}} \mathrm{t} \\
= & \frac{\mathcal{I}_{\mathcal{H}_{2}^{*}}\left(\tilde{\beta}, I_{m}\right)}{\pi^{\gamma_{2}+2}} \\
& \times \int_{\mathbb{R}^{\gamma_{2}}}\left(1+\sum_{\mu=2}^{\gamma_{2}+1} t_{\mu}^{2}\right)^{\tilde{\beta}+\frac{\gamma_{2}+2}{2}}\left(\int_{\mathbb{R}}\left(1+\sum_{\mu=1}^{\gamma_{2}+1} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+3}{2}}\left(1+t_{1}^{2}\right)^{-\frac{\gamma_{1}}{2}} \mathrm{~d} t_{1}\right)
\end{aligned}
$$

$$
\left(\int_{\mathbb{R}}\left(1+\sum_{\mu=2}^{\gamma_{2}+2} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+3}{2}}\left(1+t_{\gamma_{2}+2}^{2}\right)^{-\frac{\gamma_{3}}{2}} \mathrm{~d} t_{\gamma_{2}+2}\right) \mathrm{d} t_{2} \cdots \mathrm{d} t_{\gamma_{2}+1}
$$

By Euler's integral representation of the hypergeometric function ${ }_{2} F_{1}$, we have

$$
\begin{aligned}
& \int_{\mathbb{R}}\left(1+\sum_{\mu=1}^{\gamma_{2}+1} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+3}{2}}\left(1+t_{1}^{2}\right)^{-\frac{\gamma_{1}}{2}} \mathrm{~d} t_{1} \\
= & \frac{\pi^{\frac{1}{2}} \Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2}\right)}{\Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2}\right)} 2 F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2} ; \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2} ;-\sum_{\mu=2}^{\gamma_{2}+1} t_{\mu}^{2}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& \int_{\mathbb{R}}\left(1+\sum_{\mu=2}^{\gamma_{2}+2} t_{\mu}^{2}\right)^{-\tilde{\beta}-\frac{\gamma_{2}+3}{2}}\left(1+t_{\gamma_{2}+2}^{2}\right)^{-\frac{\gamma_{3}}{2}} \mathrm{~d} t_{\gamma_{2}+2} \\
= & \frac{\pi^{\frac{1}{2}} \Gamma\left(\tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+2}{2}\right)}{\Gamma\left(\tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2}\right)}{ }_{2} F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+2}{2} ; \tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2} ;-\sum_{\mu=2}^{\gamma_{2}+1} t_{\mu}^{2}\right) .
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{H}}\left(\tilde{\beta}, I_{m}\right) \\
= & \frac{\mathcal{I}_{\mathcal{H}_{2}^{*}}\left(\tilde{\beta}, I_{m}\right)}{\pi^{\gamma_{2}+1}} \frac{\Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2}\right)}{\Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2}\right)} \frac{\Gamma\left(\tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+2}{2}\right)}{\Gamma\left(\tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2}\right)} \\
& \left.\times \int_{\mathbb{R}^{\gamma_{2}}}\left(1+\sum_{\mu=2} t_{\mu}^{2}\right)^{\gamma_{2}+1} \frac{\tilde{\beta}+\frac{\gamma_{2}+2}{2}}{2} ;-\sum_{\mu=2} t_{\mu}^{2}\right) \\
& { }_{2} F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2} ; \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2} \gamma_{2}+\sum_{\mu=2}^{\gamma_{2}+1} t_{\mu}^{2}\right) \mathrm{d} t_{2} \cdots \mathrm{d} t_{\gamma_{2}+1} \\
= & \frac{\mathcal{I}_{\mathcal{H}_{2}^{*}}\left(\tilde{\beta}, I_{m}\right)}{\pi^{\gamma_{2}+1}} \frac{\Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2}\right)}{\Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2}\right)} \frac{\Gamma\left(\tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+2}{2}\right)}{\Gamma\left(\tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2}\right)} \frac{2 \pi^{\frac{\gamma_{2}}{2}}}{\Gamma\left(\frac{\gamma_{2}}{2}\right)} \\
& \times \int_{0}^{\infty}{ }_{r}{ }^{\gamma_{2}-1}\left(1+r^{2}\right)^{\tilde{\beta}+\frac{\gamma_{2}+2}{2}}{ }_{2} F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2} ; \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2} ;-r^{2}\right) \\
& { }_{2} F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2} ; \tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2} ;-r^{2}\right) \mathrm{d} r
\end{aligned}
$$

By (21), we have

$$
\begin{aligned}
& \mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right) \\
& =\frac{2 \mathcal{I}_{\mathcal{G}^{*}}\left(\beta, I_{n}\right) \mathcal{I}_{\mathcal{H}_{2}^{*}}\left(\beta+\frac{\gamma}{2}-2, I_{m}\right) \Gamma\left(\tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2}\right) \Gamma\left(\beta+\frac{\gamma+\gamma_{3}+\gamma_{2}-2}{2}\right)}{\pi^{\frac{\gamma_{2}}{2}+1} \mathcal{I}_{\mathcal{H}_{1}^{*}}\left(\beta+\frac{\gamma}{2}-2, I_{m}\right) \Gamma\left(\beta+\frac{\gamma+\gamma_{1}+\gamma_{2}-1}{2}\right) \Gamma\left(\beta+\frac{\gamma+\gamma_{3}+\gamma_{2}-1}{2}\right) \Gamma\left(\frac{\gamma_{2}}{2}\right)} \\
& \quad \times \int_{0}^{\infty} r^{\gamma_{2}-1}\left(1+r^{2}\right)^{\tilde{\beta}+\frac{\gamma_{2}+2}{2}}{ }_{2} F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+2}{2} ; \tilde{\beta}+\frac{\gamma_{1}+\gamma_{2}+3}{2} ;-r^{2}\right) \\
& \quad{ }_{2} F_{1}\left(\tilde{\beta}+\frac{\gamma_{2}+3}{2}, \tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+2}{2} ; \tilde{\beta}+\frac{\gamma_{3}+\gamma_{2}+3}{2} ;-r^{2}\right) \mathrm{d} r
\end{aligned}
$$

## APPENDIX C: PRIME GRAPHS WITH FEW VERTICES

We give a summary on the integrals $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)$, where $\beta>-1$ is a real number and $n \leq 6$ is the number of vertices in connected prime graphs $\mathcal{G}$. Recall from Section 1.4 that we obtain an explicit formula for the integral $\mathcal{I}_{\mathcal{G}}\left(\beta, I_{n}\right)$ for some graphs:

(B1) $\mathcal{G}$ has a chordal completion $\mathcal{G}^{*}$ in which every triangle contains at most one edge from $\mathcal{E}\left(\mathcal{G}^{*}\right) \backslash \mathcal{E}(\mathcal{G})$

(B2) $\mathcal{G}$ has minimum fill-in 2 ,

(B3) $\mathcal{G}$ is complete $k$-partite.

All connected prime graphs on at most 5 vertices have minimum fill-in at most 2 . Among the 24 connected prime graphs on 6 vertices, there are only 2 graphs which do no belong to the above classes, namely the cycle of length 6 and its complement. These two graphs both have minimum fill-in 3 , and we can write the corresponding integral as a one-dimensional integral. We use solid edges to represent the graphs. Dashed edges are the missing edges.

C.1. Two vertices. There is one graph and it is in (B1):

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-35.jpg?height=57&width=246&top_left_y=1511&top_left_x=934)

C.2. Three vertices. There is one graph and it is in (B1):

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-35.jpg?height=195&width=222&top_left_y=1667&top_left_x=949)

C.3. Four vertices. There are two graphs, both in (B1):
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-35.jpg?height=194&width=418&top_left_y=1958&top_left_x=846)

C.4. Five vertices. We have four graphs in (B1):
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-35.jpg?height=240&width=1052&top_left_y=2248&top_left_x=532)

We have one graph in (B2):

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-36.jpg?height=228&width=247&top_left_y=282&top_left_x=928)

C.5. Six vertices. We have 10 graphs with minimum fill-in at most 1 , all belong to (B1):
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-36.jpg?height=730&width=1088&top_left_y=604&top_left_x=514)

We have 4 graphs with minimum fill-in 2 and they also belong to (B1):
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-36.jpg?height=224&width=1088&top_left_y=1408&top_left_x=514)

The following 7 graphs have minimum fill-in 2 and belong to (B2):
![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-36.jpg?height=476&width=1086&top_left_y=1702&top_left_x=516)

The graph $\mathcal{K}_{3,3}$ has minimum fill-in 3, and it is in (B3):

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-36.jpg?height=225&width=244&top_left_y=2256&top_left_x=932)

Finally, there are two other graphs with minimum fill-in 3:

![](https://cdn.mathpix.com/cropped/2024_04_26_d0ce42242441d08e4f99g-37.jpg?height=222&width=244&top_left_y=279&top_left_x=932)

For the cycle of length 6, we have (by Example 4.6)

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)=\frac{\pi \Gamma_{3}(\beta+2) \Gamma(\beta+2)^{5}}{\Gamma\left(\beta+\frac{5}{2}\right)^{2}} \int_{0}^{1} t^{-\frac{1}{2}}(1-t)^{\beta+1}{ }_{2} F_{1}\left(\beta+2, \frac{1}{2} ; \beta+\frac{5}{2} ; t\right)^{2} \mathrm{~d} t
$$

For the complement of the cycle of length 6, we have (by Example 3.1)

$$
\mathcal{I}_{\mathcal{G}}\left(\beta, I_{6}\right)=\frac{\pi \Gamma_{4}\left(\beta+\frac{5}{2}\right)^{5} \Gamma\left(\beta+\frac{5}{2}\right)^{4}}{\Gamma(\beta+3)^{2}} \int_{0}^{1} t^{\beta+2}(1-t)^{-\frac{1}{2}}{ }_{2} F_{1}\left(\frac{1}{2}, \frac{1}{2} ; \beta+3 ; t\right)^{2} \mathrm{~d} t
$$

