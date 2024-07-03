# A Copula Graphical Model For Multi-Attribute Data Using Optimal Transport

Qi Zhang, Bing Li, and Lingzhou Xue Department of Statistics, The Pennsylvania State University

## Abstract

Motivated by modern data forms such as images and multi-view data, the multiattribute graphical model aims to explore the conditional independence structure among vectors. Under the Gaussian assumption, the conditional independence between vectors is characterized by blockwise zeros in the precision matrix. To relax the restrictive Gaussian assumption, in this paper, we introduce a novel semiparametric multiattribute graphical model based on a new copula named Cyclically Monotone Copula.

This new copula treats the distribution of the node vectors as multivariate marginals and transforms them into Gaussian distributions based on the optimal transport theory. Since the model allows the node vectors to have arbitrary continuous distributions, it is more flexible than the classical Gaussian copula method that performs coordinatewise Gaussianization. We establish the concentration inequalities of the estimated covariance matrices and provide sufficient conditions for selection consistency of the group graphical lasso estimator. For the setting with high-dimensional attributes, a Projected Cyclically Monotone Copula model is proposed to address the curse of dimensionality issue that arises from solving high-dimensional optimal transport problems. Numerical results based on synthetic and real data show the efficiency and flexibility of our methods.

Keywords: Multi-attribute data; Non-Gaussian data; Optimal transport.

## 1 Introduction

The undirected graphical model is commonly used to study the conditional independence relations among a set of random variables. Given a p-dimensional random vector X, the goal is to estimate the undirected graph G = (*V, E*), where V is the node set of cardinality p, corresponding to the indices components of X, E is the edge set indicating whether two nodes are connected, which happens if and only if the two random variables on the nodes are conditionally dependent. For multivariate Gaussian X ∼ *N(µ,* Σ), the precision matrix Θ = Σ−1fully characterizes the conditional independence relations, making sparse precision matrix estimation the main approach for high-dimensional graph estimation. Methods for this include the neighborhood selection (Meinshausen and B¨uhlmann, 2006), Graphical Lasso (Yuan and Lin, 2007; Friedman et al., 2008), constrained ℓ1-minimization (Cai et al., 2011), and penalized D-trace loss (Zhang and Zou, 2014; Tao et al., 2024). To relax the Gaussian assumption, Liu et al. (2009) proposed a Copula Gaussian Graphical Model (Copula-GGM), which assumes that p marginal transformations can transform the data to multivariate Gaussian. The model coincides with the Gaussian copula when the transformations are monotone. Rank-based correlation estimators for the Copula-GGM are proposed by Liu et al. (2012) and Xue and Zou (2012). A comprehensive review of this direction is available in Lafferty et al. (2012). The advantage of the copula approach is it retains the simplicity of the conditional independence structure while allowing the marginal distribution to be arbitrary.

The classical undirected graphical model only considers scalar random variables on nodes.

However, in modern applications, there is a need for a graphical model with nodes representing multi-attribute entities or random vectors. Kolar et al. (2013, 2014) developed the multi-attribute graphical model where nodes correspond to vectors representing multiattribute entities and edges encode the conditional dependence between vectors. The model has been successfully applied in various domains, including uncovering gene regulatory networks from gene and protein profiles (Chiquet et al., 2019), inferring the brain connectivity graph from positron emission tomography data (Kolar et al., 2014), and inferring color image graphs by modeling the dependence between pixels (Tugnait, 2021).

In the multi-attribute graphical model, when the data follows a multivariate Gaussian distribution, conditional independence can still be inferred from the corresponding block in the precision matrix. To relax the Gaussian assumption, we may still apply a coordinatewise monotone transformation as we did for classical Gaussian graphical model. However, the coordinatewise Gaussianization is unnecessarily strong in the multi-attribute setting. To see the situation clearly, consider the following assumptions:
1. after transforming every element of X to Gaussian, X is jointly Gaussian; 2. after transforming every node vector of X to Gaussian, X is jointly Gaussian.

By logic, the first assumption implies the second. The first statement is what underlies the current copula Gaussian graphical models; the second uderlies the the new copula model we propose. To provide more intuition, in Figure 1 we plot three scenarios: a cross-shaped distribution, a v-shaped distribution, and a triangle-shaped distribution. In all cases, the two elements are marginally distributed as Gaussian, but jointly the vectors are strongly non- Gaussian. If we have three node vectors having these three distributions, then no marginal transformation can lead to joint Gaussian distribution X. This motivates us to develop more



flexible semiparametric models that link multi-dimensional marginals in a graph.

More rigorously, a multi-attribute graphical model can be viewed as a random vector X = (XT
1
, XT
2
, . . . , XT
p
)
T ∈ ⊕p j=1R
dj along with a graph G of p nodes, where nodes j and k are connected if and only if Xj and Xk are conditionally dependent given X−(j,k) = {Xℓ, ℓ ̸= *j, k*}. To link the multivariate marginals, we introduce a copula, called the Cyclically Monotone Copula, based on optimal transport theory. Specifically, we solve an optimal transport problem from the distribution of each node vector to a Gaussian distribution, and assume that optimal transport maps {Tj}
p j=1 transform the entire X to joint Gaussian.

The name Cyclically Monotone describes the geometric structure of the optimal transport map based on the result of Brenier (1991). This copula model is very flexible, as it allows the multivariate marginals to be arbitrary continuous distributions, including the scenario described in Figure 1.

Our approach is inspired by the multivariate ranks introduced by Chernozhukov et al.

(2017), which have been used for multivariate independence test (Ghosal and Sen, 2022; Deb and Sen, 2023; Shi et al., 2022), vector quantile regression (Carlier et al., 2016), among others. Two related works include the semiparametric CCA model developed by Bryan et al. (2021) based on a generalized Gaussian copula, and the vector copula based on measure transportation proposed in Fan and Henry (2023). In this paper, we use the proposed copula to estimate high-dimensional graphical models.

Estimating the cyclically monotone transformations {Tj}
p j=1 directly requires solving discrete-to-discrete optimal transport problems, which suffers from the curse of dimensionality issue with a minimax rate of O(n
−1/d) (Fournier and Guillin, 2015; Niles-Weed and Rigollet, 2022). This can result in an inaccurate estimation of the graph structure, especially when the numbers of attributes on some nodes are large. To address this, we propose a projected cyclically monotone copula (PCMC) for the multi-attribute graphical model with large-dimensional attributes. We assume that the non-Gaussianity of the d-dimensional attributes only appears in a low-dimensional subspace. After properly estimate the lowdimensional non-Gaussian subspace and perform Gaussianization within it, the data can be efficiently transformed into a Gaussian distribution. This idea stems from the recent developments of projection-based techniques for solving high-dimensional optimal transport problems, such as the slicing approach (Deshpande et al., 2018), projection pursuit approach (Meng et al., 2019), and projection robust method (Paty and Cuturi, 2019). A comprehensive review of this direction is provided in Zhang et al. (2022).

The rest of the paper is organized as follows. In Section 3, we introduce the cyclically monotone copula Gaussian graphical model (CMC-GGM) for multi-attribute data and extend it to the composition cyclically monotone copula Gaussian graphical model (CCMC- GGM). Estimation methods are developed, and their consistency and convergence rates established, in Sections 4 and 5. In Section 6, we propose the projected cyclically monotone copula Gaussian graphical Model (PCMC-GGM) to avoid the curse of dimensionality arising from solving optimal transport problems. In Section 7, we present simulation results that compare our methods with Gaussian graphical models and copula Gaussian graphical models for multi-attributes data. Finally, in Section 8, we apply the CMC-GGM to estimate the gene and protein regulatory network and color texture graph.

## 2 Background 2.1 Multi-Attribute Graphical Model

Consider p random vectors Xj ∈ R
djfor j = 1*, . . . , p*. We assume d = d1 = *· · ·* = dp for notational simplicity, but the model can be easily extended to cover distinct d's. We let X = (XT
1
, XT
2
, . . . , XT
p
)
T ∈ R
dp. Let G(*V, E*) be the undirected graph with node set V = {1, 2*, . . . , p*} and edge set E ⊆ {(*j, k*) ∈ V × V : j ̸= k}. We say X follows a multi-attribute graphical model with the graph G(*V, E*) if the edge set E is determined by the conditional independence structure among X1*, . . . , X*p in the following way:

$$X_{j}{\perp}{\!\!\!\!\perp}X_{k}|X_{-(j,k)}\mathrm{~if~and~only~if~}(j,k)\notin E,$$
Xj |=Xk|X−(j,k)if and only if (*j, k*) ∈/ E, (1)
where X−(j,k) = {Xℓ, ℓ ̸= *j, k*}. We call X1*, . . . , X*p the node vectors. If, furthermore, X
follows a multivariate Gaussian distribution *N(0,* Σ), where Σ and Θ = Σ−1 have block structures

$$\Sigma=\begin{pmatrix}\Sigma_{11}&\Sigma_{12}&\dots&\Sigma_{1p}\\ \Sigma_{21}&\Sigma_{22}&\dots&\Sigma_{2p}\\ \vdots&\vdots&\ddots&\vdots\\ \Sigma_{p1}&\Sigma_{p2}&\dots&\Sigma_{pp}\end{pmatrix}\text{and}\Theta=\begin{pmatrix}\Theta_{11}&\Theta_{12}&\dots&\Theta_{1p}\\ \Theta_{21}&\Theta_{22}&\dots&\Theta_{2p}\\ \vdots&\vdots&\ddots&\vdots\\ \Theta_{p1}&\Theta_{p2}&\dots&\Theta_{pp}\end{pmatrix},\tag{2}$$  to the model as the Gaussian Graphical Model (CGM) for multi-attributes.  

$$(1)$$

then we refer to the model as the Gaussian Graphical Model (GGM) for multi-attributes data. Under the Gaussian assumption, the conditional independence in (1) can be replaced by Θjk = 0; that is, there is an edge between j and k iff Θjk ̸= 0.

Compared with the single-attribute graphical model, the multi-attribute graphical model has a dependence structure within each node, parametrized by sub-precision matrices Θjj ,
j = 1*, . . . , p* on the diagonal of Θ. However, to infer the edge set E of the graph, we only need to consider the conditional dependence relations across different node vectors. Therefore, any one-to-one transformations on {Xj}
p j=1 that preserves the conditional dependence structure can be applied. For instance, there exist orthogonal matrices Γj ∈ R
d×dsuch that ΓjXj ∼
N(0, Id) for j = 1*, . . . , p*. Let Γ = (Γ1*, . . . ,* Γp) and X˜ = ΓX. The graph estimated using X
is equivalent to that of X˜. Therefore, without loss of generality, we can always assume the diagonal blocks {Σjj}
p j=1 to be the identity matrices.

## 2.2 Optimal Transport And Cyclical Monotonicity

Let P(R
d) be the set of probability measures on R
d and Pac(R
d) the set of probability measures absolutely continuous with respect to the Lebesgue measure. Let µ ∈ P(R
d) and ν ∈ P(R
d). A measurable map T : R
d → R
dis said to push µ to ν if for any measurable set A ⊆ Y , µ(T
−1(A)) = ν(A). This relation is frequently written as ν = T\#µ or ν = µ ◦ T
−1.

Let T (*µ, ν*) denote the class of all measurable functions T such that ν = T\#µ. Under the quadratic loss, Monge's optimal transport (MOT) seeks a member of T (*µ, ν*) that reaches the infimum:

$$\operatorname*{inf}_{T\in{\mathcal{T}}(\mu,\nu)}\left\{\int_{\mathbb{R}^{d}}\|x-T(x)\|^{2}\mu(x)\right\}.$$
$$\left({\mathrm{3}}\right)$$

If this infimum is achieved within T (*µ, ν*), then the minimizer is called an optimal transport map. However, the infimum may not be achievable within T (*µ, ν*) - indeed, T (*µ, ν*) can be an empty set in extreme cases. This limits the applicability of Monge's approach.

To address this limitation, Kantorovich (1948) introduced a relaxed version of Monge's problem by representing a transportation plan as a joint measure π with marginals µ and ν. Let Π(*µ, ν*) be the set of joint probability measures on R
d × R
d with marginals µ and ν.

The Kantorovich's problem seeks a π in Π(*µ, ν*) to minimize the total cost, that is,

$$W_{2}^{2}(\mu,\nu)=\operatorname*{inf}_{\pi}\left\{\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\|x-y\|^{2}d\pi(x,y):\pi\in\Pi(\mu,\nu)\right\}.$$
$$\quad(4)$$
$$\left({\bar{0}}\right)$$

The square root of the minimum value of (4) is defined as the 2-Wasserstein distance, and a solution to (4) is called an optimal transport plan. The existence of the solution to (4)
follows from Villani (2009, Theorem 4.1). Equivalently, we can express the square of the 2-Wasserstein distance as

$$W_{2}^{2}(\mu,\nu)=\int\|x\|^{2}d\mu(x)+\int\|y\|^{2}d\nu-2\operatorname*{min}_{\varphi\in{\mathcal{F}}}\left\{\int\varphi\,d\mu+\int\varphi^{*}d\nu\right\},$$
∗dν, (5)
where F is the space of L1(µ) convex function on R
d, and φ
∗is the Legendre-Fenchel conjugate of φ, given by,

$$\varphi^{*}(y)=\operatorname*{sup}_{x\in\mathbb{R}^{d}}\{\langle x,y\rangle-\varphi(x)\},\ y\in\mathbb{R}^{d}.$$
d. (6)
Thus, solving (4) is equivalent to solving the semi-dual problem

$$(6)$$

$$\operatorname*{min}_{\varphi\in{\mathcal{F}}}\int\left\{\varphi\,d\mu+\int\varphi^{*}d\nu\right\}.$$
$$\left(7\right)$$

The semi-dual problem (7) connects with the Monge problem (3) through Brenier's Theorem (Brenier, 1991), which establishes the existence, uniqueness, and intrinsic structure of the optimal transport map. McCann (1995) extended this result to relax the second-order moment assumptions.

PROPOSITION 1 (Brenier's Theorem). Let µ and ν *be two distributions on* R
d.

(1) If µ *is absolutely continuous with respect to the Lebesgue measure on* R
d, with support contained in a convex set U, then there exists a convex function φ : U → R ∪ {+∞}
such that (∇φ)\#µ = ν. The function ∇φ is unique µ-almost everywhere.

(2) If, in addition, ν *is absolutely continuous on* R
d *with support contained in a convex set* V *, then there exists a convex function* φ
∗: V → R∪{+∞} *such that* (∇φ
∗)\#ν = µ. The
function ∇φ
∗is unique ν*-almost everywhere and equal to* (∇φ)
−1 µ*-almost everywhere.*
That means, for almost every *x, y* ∈ U × V ,

$$(\nabla\varphi^{*}\circ\nabla\varphi)(x)=x,\quad(\nabla\varphi\circ\nabla\varphi^{*})(y)=y.$$

Proposition 1 implies that a unique transport map with the form ∇φ exists between any absolutely continuous distributions. We refer to such a convex function φ as the Brenier potential.

On the real line R, the gradients of convex functions are non-decreasing functions. When d ≥ 2, Rockafellar (1966) showed that the set of gradients of convex functions coincides with the set of cyclically monotonic functions defined below, which can be treated as a generalization of monotonicity to functions with more than one variables.

DEFINITION 1. Let U *be a nonempty subset of* R
d. A function f is called cyclically monotone if, for every set of points x1, . . . , xn+1 ∈ U with xn+1 = x1*, it holds that*

$$\sum_{k=1}^{n}\langle x_{k+1},f(x_{k+1})-f(x_{k})\rangle\geq0.$$  _Equivalently,_  $$\sum_{k=1}^{n}\langle x_{k},f(x_{k})\rangle\geq\sum_{k=1}^{n}\langle x_{k},f(x_{\sigma(k)})\rangle$$  _for any permutation $\sigma$ of $\{1,2,\ldots,n\}$._
As a special case, the linear function f(x) = Ax, where A ∈ R
d×d, is cyclically monotone if A is symmetric and positive definite. When d = 1, the definition above is equivalent to the usual notion of monotonicity.

## 3 Cyclically Monotone Copula Gaussian Graphical Model

The structure of the multi-attribute graphical model leads us to propose a flexible semiparametric model for non-Gaussian data. As we have observed, non-Gaussianity may occur in node vectors of X instead of occurring in the coordinates of X. Correspondingly, we let the transformations act jointly on the node vectors instead of coordinate-wise as in the classical copula transformation.

We define the Cyclically Monotone Copula Gaussian (CMCG) distribution as follows.

Let X = (XT
1
, XT
2
, . . . , XT
p
)
T where, for j = 1*, . . . , p,* Xj = (Xj1*, . . . , X*jd) is a random vector in R
d.

DEFINITION 2. We say X follows a cyclically monotone copula Gaussian (CMCG) distribution if there exist cyclically monotone functions {Tj: R
d → R
d}
p j=1*, such that* (T1(X1)
T,
. . . , Tp(Xp)
T)
T ∼ N(0, Σ), where Σ *has structure* (2) *with* Σjj = Id.

Let T = (T1*, . . . , T*p). We denote a random vector following CMCG distribution as X ∼ CMCG(T, Σ). The CMCG family covers the copula Gaussian distribution family in Liu et al. (2009) because the tensor product of univariate monotone functions is indeed a cyclically monotone function, as shown in the next proposition. In the following, for functions g1 : R → R*, . . . , g*d : R → R, let g1 *⊗ · · · ⊗* gd denote the function from R
d → R
dsuch that
(g ⊗ · · · ⊗ gd)(u1*, . . . , u*d) = (g1(u1*), . . . , g*d(ud))T. PROPOSITION 2. *If there exist monotone non-decreasing univariate functions* {fjs : s = 1, . . . d, j = 1, . . . , p} such that (f11(X11), . . . , fpd(Xpd)) ∼ N(0, Σ)*, then* X ∼ CMCG(T, Σ), where T = (T1, . . . , Tp) and Tj = fj1 ⊗ · · · ⊗ fjd for j = 1*, . . . , p*.

For j = 1*, . . . , p*, let Pj be the distribution of Xj. We assume Pj to be absolutely continuous on R
d. Then, by Brenier's theorem, there exists a unique cyclically monotone function Tj such that Tj (Xj ) ∼ N(0, Id). In other words, the CMCG family allows the multi-dimensional marginal distributions to be any absolutely continuous distributions. As a comparison, the copula Gaussian model requires the multi-dimensional marginal distribution to be copula Gaussian.

Let X ∼ CMCG(T, Σ). Suppose the precision matrix Θ = Σ−1 has the same block structure as (2). We say X follows a Cyclically Monotone Copula Gaussian Graphical Model
(CMC-GGM) G(*V, E*) if (1) holds.

The joint cumulative distribution function of X is given by:

$$F(x_{1},\ldots,x_{p})=\Phi_{\Sigma}(T_{1}(x_{1}),\ldots,T_{p}(x_{p})),$$
F(x1*, . . . , x*p) = ΦΣ(T1(x1)*, . . . , T*p(xp)), (8)
where ΦΣ is the multivariate normal cumulative distribution function with mean zero and covariance matrix Σ. If {Tj}
p j=1 are differentiable, the joint probability density function of X is given by:

$$p_{X}(x)=\frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}}\exp\left\{-\frac{1}{2}T(x)^{\mathsf{T}}\Sigma^{-1}T(x)\right\}\prod_{j=1}^{p}\operatorname*{det}(D_{T_{j}}(x_{j})),$$
$$\left({\mathcal{S}}\right)$$

where DTj is the Jacobian matrix of Tjfor j = 1*, . . . , p*. This implies that the conditional independence Xj |=Xk|X−(j,k) can still be characterized by Θjk = 0, which implies that relation (1) is equivalent to

$$\Theta_{j k}=0\Leftrightarrow(j,k)\notin E.$$

In fact, any one-to-one transformations of the node vectors will preserve the original graph structure. However, a large class of transformations will make the model non-identifiable, prohibiting inference on the precision matrix. This is also noticed by Bryan et al. (2021)
when designing semiparametric CCA models. The following proposition guarantees that the CMC-GGM is identifiable.

PROPOSITION 3. If two random vectors X ∼ CMCG(T, Σ) and X˜ ∼ CMCG(T , ˜ Σ) ˜ *have* the same distribution, then Σ = Σ˜, and T = T˜ *almost everywhere.*
The CMC-GGM model extends the Copula-GGM model by assigning a multivariate normal score to each node vector. To construct rank-based estimators, we can solve optimal transport problems between the distribution of Xj and the uniform distribution over the unit hypercube [0, 1]d. This is the same as the multivariate rank proposed in Ghosal and Sen (2022), Fan and Henry (2023), and among others. The c.d.f of X is given by

$$F(x_{1},\ldots,x_{p})=\Phi_{\Sigma}(\Phi^{-1}(R_{1}(x_{1}))^{\top},\ldots,\Phi^{-1}(R_{p}(x_{p})^{\top}),\tag{9}$$

where ΦΣ(·) is the c.d.f of *N(0,* Σ), Φ−1(xj ) = (Φ−1(xj1)*, . . . ,* Φ
−1(xjd))T, and Rj (·) is the optimal transport map between Pj and U([0, 1]d).

For a Gaussian graphical model with a single attribute, Rj (·) is the common distribution function, and Φ−1 ◦ Rjis a monotonic non-decreasing function. Therefore, model (9) and CMC-GGM (8) are equivalent. However, this is not the case for the multi-attribute graphical model, as Φ−1 ◦ Rj may not be a cyclically monotone function. In this paper, we focus on CMC-GGM because cyclically monotone functions offer the best transformations for preserving the relative information among data when transported to Gaussian. For further dicussions on Model (9), please see the Supplementary Material.

## 4 Estimation

The plug-in procedure provides a direct approach to estimating the CMC-GGM. This approach was also used Liu et al. (2009) for the Copula-GGM and Solea and Li (2022) for the copula functional graphical model. In this paper, we develop a two-step plug-in procedure to estimate CMC-GGM: in step 1, we estimate the transformation T nonparametrically by solving discrete-to-discrete optimal transport problems; in step 2, we use sparse estimation methods, including thresholding, group graphical lasso selection, and neighborhood vectoron-vector group lasso selection, to construct a sparse estimator of the blockwise precision matrix using transformed data.

## 4.1 Estimation Of The Cmc Transformation

Let Xn = {Xi}
n i=1 be i.i.d samples from PX, where superscripts i ∈ {1*, . . . , n*} is the sample index and Xi = {Xi j
: j = 1*, . . . , p*} where the subscript j ∈ {1*, . . . , p*} is subvector index.

We estimate the cyclically monotone transformation Tj between Pj, the distribution of Xi j
,
and the d-dimensional standard Gaussian distribution Q by solving the following discreteto-discrete OT problem. Let Zn = {Z
1*, . . . , Z*n} be i.i.d samples drawn from Q. Define the empirical measures on Xn and Zn as

$$\hat{P_{j}}=\frac{1}{n}\sum_{i=1}^{n}\delta_{X_{j}^{i}},\quad\hat{Q}=\frac{1}{n}\sum_{i=1}^{n}\delta_{Z^{i}},$$
$$\left(10\right)$$
$$(11)$$

respectively. Solving the optimal transport problem between Pˆj and Qˆ reduces to solving an assignment problem given by

$$\hat{\sigma}_{j}=\operatorname{argmin}_{\sigma\in A_{n}}\sum_{i=1}^{n}\|X_{j}^{i}-Z^{\sigma(i)}\|^{2},$$

where An is the set of all permutations of {1, 2*, . . . , n*}. This is a combinatorial optimization problem and can be solved using the Hungarian algorithm (see, for example, Jonker and Volgenant (1988)) with the worst computational complexity O(n 3). The cyclically monotone transformation between Pj and Q is then estimated by Tˆj (Xi j
) = Z
σj (i)for i = 1*, . . . , n*.

To control the bias-variance trade-off in high-dimensional setting, we apply the Winsorization (or truncation) operator to the estimated transformation Tˆj. Specifically, we define Tˆ
(w)
j(Xj ) = (Tˆ
(w)
j1(Xj1)*, . . . ,* Tˆ
(w)
jd (Xjd)), where

$$\hat{T}^{(w)}_{js}(x)=\hat{T}_{js}(x)\mathds{1}\{|\hat{T}_{js}(x)|\leq\delta_{n}\}+\text{sign}(\hat{T}_{js}(x))\delta_{n}\mathds{1}\{|\hat{T}_{js}(x)|\geq\delta_{n}\},\tag{12}$$

is the 1-dimensional Winsorization operator with threshold δn. In the classical copula graphical model, the winsorization operator is applied to the cumulative function F(x), and the transformation is then estimated by Φ−1(F
(w)(x)). For example, Klaassen and Wellner (1997)
consider using δn = n
−1 and Liu et al. (2009) suggest using δn = (4n 1/4√π log n)
−1. In
(12), the winsorization operator is assigned to the transformed values of the estimated optimal transport map Tˆ, which are samples from standard Gaussian. Therefore, we use the threshold δn
√2 log n, which provides comparable thresholding effects as the copula Gaussian setting. This choice is justified by Abramovich et al. (2006, Lemma 12.3), which states that Φ
−1(1 − 1/n) ≤
√2 log n. This threshold enables us to derive the desired convergence rate in Section 5.

We can also approximate the Gaussian distribution using the quasi-Monte Carlo methods
(see Deb and Sen (2023) for more details). For example, we first take Cn = {c1*, . . . , c*n} to be the d-dimensional Halton sequence of size n. The empirical distribution on Cn will be a discrete approximation of U[0, 1]d. Then the empirical distribution on {Φ
−1(ci), i = 1,
. . . , n}, where Φ−1is applied coordinatewise, can be considered as a discrete approximation of *N(0, I*d). Since Φ−1(·) diverges very quickly when evaluated at a point close to 1, we can also assign a Winsorization operator on the Halton sequence, resulting in the samples
{Z
i = Φ−1((c
(w)
i))}
n i=1. We do not find a significant difference between using quasi-Monte Carlo methods and the Monte Carlo method in simulation studies in Section 7.1.

## 4.2 Sparse Estimation Of The Precision Matrix

In this subsection, we present methods for sparsely estimating the precision matrix using the estimated covariance matrix of the transformed data. Let Σ be the sample covariance ˆ matrices of the CMC-transformed data Tˆ(w)(X) and Θ be its inverse, with block structure ˆ

$${\hat{\Sigma}}={\begin{pmatrix}{\hat{\Sigma}}_{11}&{\hat{\Sigma}}_{12}&\dots&{\hat{\Sigma}}_{1p}\\ {\hat{\Sigma}}_{21}&{\hat{\Sigma}}_{22}&\dots&{\hat{\Sigma}}_{2p}\\ \vdots&\vdots&\ddots&\vdots\\ {\hat{\Sigma}}_{p1}&{\hat{\Sigma}}_{p2}&\dots&{\hat{\Sigma}}_{p p}\end{pmatrix}}{\mathrm{~and~}}{\hat{\Theta}}={\begin{pmatrix}{\hat{\Theta}}_{11}&{\hat{\Theta}}_{12}&\dots&{\hat{\Theta}}_{1p}\\ {\hat{\Theta}}_{21}&{\hat{\Theta}}_{22}&\dots&{\hat{\Theta}}_{2p}\\ \vdots&\vdots&\ddots&\vdots\\ {\hat{\Theta}}_{p1}&{\hat{\Theta}}_{p2}&\dots&{\hat{\Theta}}_{p p}\end{pmatrix}}.$$
$$\quad(13)$$
.
Here, the (*j, k*)-th block is

$$\dot{\Sigma}_{j k}=E_{n}[\hat{T}_{j}^{(w)}(X_{j})\hat{T}_{k}^{(w)}(X_{k})^{\intercal}]-E_{n}[\hat{T}_{j}^{(w)}(X_{j})]E_{n}[\hat{T}_{k}^{(w)}(X_{k})],$$
k(Xk)], (13)
where En[·] is the empirical mean. We propose three ways to estimate the graph sparsely.

Thresholding. We begin by computing the Tychonoff-regularized precision matrix as Θˆ (r) = (Σ +ˆ ηIdp)
−1, where η is a tuning parameter, and superscript r indicates regularization. We then estimate the edge set E by

$$\hat{E}(\epsilon_{n})=\{(j,k)\in V\times V:\|\hat{\Theta}_{j k}^{(r)}\|_{\mathrm{F}}>\epsilon_{n}\},$$

where {ϵn} is a positive sequence with ϵn ↓ 0 and *∥ · ∥*F denotes the Frobenius norm. The thresholding estimator is direct and easy to implement but less accurate than penalized estimation methods in most settings.

Group glasso. This approach minimizes the penalized negative Gaussian loglikelihood:

$$L_{n}:\mathbb{R}^{dp\times dp}\to\mathbb{R},\ \Theta\to-\log\det(\Theta)+\text{trace}(\Theta\hat{\Sigma})+\lambda_{n}\sum_{k\neq j}\|\Theta_{jk}\|_{\mathbb{F}},\tag{14}$$

where λn is a tuning parameter. The precision matrix Θ is then estimated by minimizing Ln(·) over the set of all positive semidefinite dp × dp matrix. Several efficient algorithms have been developed to minimize the penalized negative Gaussian loglikelihood with group penalty, such as Kolar et al. (2014) and Tugnait (2021), among others. We adopt the block coordinate descent algorithm in Qiao et al. (2019) to solve (14).

Neighborhood vector-on-vector group lasso selection. We perform vector-on-vector regression separately for each j = 1, 2*, . . . , p*, using Tˆj (Xj ) as the response and p−1 remaining subvectors in *Tˆ(X*) as predictors. Let ς be a mapping that reorganizes the indices such that
{ς(1), . . . , ς(p − 1)} = {1*, . . . , p*}/{j}. For simplicity, we write Y = Tˆj (Xj ) ∈ R
d and X˜ = (X˜1*, . . . ,* X˜p−1) = (Tˆς(1)(Xς(1))*, . . . ,* Tˆς(p−1)(Xς(p−1))) ∈ R
d×(p−1)d. Let B = (BT
1
, . . . ,
BT
p−1
)
T ∈ R
d(p−1)×d, where Bk ∈ R
d×dfor k = 1*, . . . , p* − 1. Then the vector-on-vector regression model can be written as:

$$Y=\sum_{k=1}^{p-1}\tilde{X}_{k}B_{k}+\varepsilon=\tilde{X}B+\varepsilon,\tag{1}$$

where ε ∈ R
dis an error vector with mean 0 and is independent of X˜. After vectorization,
(15) can be written as

$$\operatorname{vec}(Y)=(I_{d}\otimes{\tilde{X}})\cdot\operatorname{vec}(B)+\operatorname{vec}(\varepsilon),$$
vec(Y ) = (Id ⊗ X˜) · vec(B) + vec(ε), (16)
where vec(·) vectorizes an d×d matrix by stacking the columns of the matrix into a d 2×1 vector and ⊗ is the Kronecker product. We then estimate regression parameters by minimizing the squared residuals with group lasso penalty, given by:

$$\hat{B}=\operatorname*{argmin}_{B\in\mathbb{R}^{d(p-1)\times d}}\left\{\frac{1}{2n}\sum_{i=1}^{n}\left\|\text{vec}(Y^{i})-(I_{d}\otimes\hat{X}^{i})\text{vec}(B)\right\|^{2}+\lambda_{n}\sum_{j=1}^{p-1}\|\text{vec}(B_{k})\|_{2}\right\},\tag{17}$$
$$\left(15\right)$$
$$(16)$$

where λn is a tuning parameter. We estimate the support set for node j as:

$${\hat{N_{j}}}=\{\sigma(k):k=1,\ldots,p-1,\|{\hat{B}}_{k}\|>0\}.$$

After estimating the neighborhood for each node, we construct an estimated edge set Eˆ by aggregating {Nˆj}
p j=1 via intersection or union. We use the Groupwise Majorization Descent
(GMD) algorithm in Yang and Zou (2015) to solve (17).

Selection of tuning parameters. All methods above require choosing tuning parameters to control the sparsity of the estimated graph. The sparsity level can be controlled by ϵn for thresholding, and by λn for glasso and neighborhood selection. Common approaches for tuning parameter selection include the Akaike information criterion (AIC), Bayesian information criterion (BIC), cross-validation, and stability selection (Meinshausen and B¨uhlmann, 2010).

In the synthetic data experiments, to ensure a fairer comparison among different methods, we fit each method over a range of tuning parameters and generate ROC curves. We then compute the associated area-under-curve (AUC) values. For the data applications, we suggest using the BIC to select tuning parameters for the group glasso method, which takes the following form:

$$\text{BIC}(\lambda_{n})=\text{trace}(\hat{\Sigma}\hat{\Theta})-\log|\hat{\Theta}|+\frac{\log(n)}{n}m^{2}\left(\frac{1}{2}\sum_{j\neq k}1\{\hat{\Theta}_{jk}\neq0\}+p\right).\tag{18}$$

However, when the sample size is small, BIC may not lead to a reasonable graph. To address this issue, we suggest a method similar to the stability selection (Meinshausen and B¨uhlmann, 2010). First, we fit a relatively dense graph with the sparsity chosen by cross-validation or domain knowledge. Next, we refit the model using bootstrap samples 50 times and select the stable edges that appeared in at least 90% of the replications.

## 5 Consistency And Convergence Rate

In this section, we establish the consistency and convergence rate for the estimator of the CMC-GGM. Recall that each Xjin X is distributed as Pj, which is dominated by the Lebesgue measure in R
d. Let Q = N(0, Id). By Brenier's theorem, for each j = 1*, . . . , p*,
there exists a convex potential function φj such that the optimal transport map Tj between Pj and Q can be written as Tj = ∇φj. Let φ
∗
j be the Legendre-Fenchel dual of φj, as defined in (6). Then, ∇φ
∗ j is the optimal transport map transporting Q to Pj. Let Pˆj and Qˆ be the empirical measures defined in (10). Let Tˆj be the estimates obtained from (11).

Several recent works, such as Deb and Sen (2023) and Hallin et al. (2021), focus on establishing the convergence rate of the discrete-to-discrete estimator of the optimal transport map. In our model, both the source and target distributions can have unbounded supports, where the results in Manole et al. (2021) and Deb and Sen (2023) cannot be directly applied.

Similar to Manole et al. (2021), we introduce the following regularity condition on the Brenier potential functions {φj}
p j=1 to give a stability bound of the estimated transformations.

For j = 1*, . . . , p*, we assume
(A1) ∇φjis Lipschitz continuous with Lipschitz constant ρ;
(A2) φjis strongly convex with parameter 1/ρ.

Assumptions (A1) and (A2) guarantee that for any two points *x, y* ∈ R
d,
$${\frac{1}{\rho}}\|x-y\|^{2}\leq\langle\nabla\varphi_{j}(x)-\nabla\varphi_{j}(y),x-y\rangle\leq\rho\|x-y\|^{2}.$$
REMARK 1. By Hiriart-Urruty and Lemar´echal (2004, Theorem 4.2.1, 4.2.2), the Legendre- Fenchel dual φ
∗ j
(·) is strongly convex with parameter 1/ρ if and only if ∇φj (·) is ρ-Lipschitz continuous. Therefore, assumption (A2) is equivalent to ∇φ
∗
j being ρ*-Lipschitz.*
REMARK 2. We note that assumption (A1) implies (A2) when both source and target distributions are defined in a compact set and have densities that are bounded above and below. However, when the support of Pj and Q *are unbounded, assumption (A2) becomes* more restrictive. Nevertheless, under certain regularity conditions on the source distribution Pj, we can still guarantee (A2). For example, according to Caffarelli contraction theorem
(Caffarelli, 2000), if Pj *is a uniformly log-concave measure of the form* e
−V dx, where V has Hessian matrix ≥ αId*, then* ∇φ
∗ j is α
−1/2*-Lipschitz and hence* φjis α
−1/2-strongly convex.

For further extensions, see Colombo and Fathi (2021) and Manole and Niles-Weed (2021).

We first establish the following stability bound. A similar result for the semi-discrete OT
setting is derived in Manole et al. (2021, Theorem 6) and Deb et al. (2021, Theorem 2.1). LEMMA 1. Suppose assumption (A1) holds with constant ρ > 0*, then, for* j = 1, . . . , p, we have

$$\frac{1}{n}\sum_{i=1}^{n}\|\hat{T}_{j}(X^{i}_{j})-T_{j}(X^{i}_{j})\|^{2}\leq\rho\left\{W_{2}^{2}(\hat{P}_{j},\hat{Q})-W_{2}^{2}(\hat{P}_{j},\bar{Q}_{j})-\int g_{j}\,d(\hat{Q}-\bar{Q}_{j})\right\},\tag{19}$$  $\sum_{i=1}^{n}\|\hat{T}_{j}(X^{i}_{j})-T_{j}(X^{i}_{j})\|^{2}\leq\rho\left\{W_{2}^{2}(\hat{P}_{j},\hat{Q})-W_{2}^{2}(\hat{P}_{j},\bar{Q}_{j})-\int g_{j}\,d(\hat{Q}-\bar{Q}_{j})\right\},$
where gj (·) = *∥ · ∥*2 − 2φ
∗ j
(·) and Q¯j = (∇φj )\#(Pˆj )*. If, in addition, assumption (A2) holds,*
then

$$\frac{1}{\rho^{2}}W_{2}^{2}(\hat{Q},\bar{Q}_{j})\leq\frac{1}{n}\sum_{i=1}^{n}\|\hat{T}_{j}(X_{j}^{i})-T_{j}(X_{j}^{i})\|^{2}\leq\rho^{2}W_{2}^{2}(\hat{Q},\bar{Q}_{j}).\tag{20}$$
$$14$$

Based on the stability bounds in Lemma 1, we establish a 0-concentration inequality for
∥Tˆj −Tj∥L1(Pˆj )
in Lemma 2. Since we use Monte Carlo methods to generate discrete samples from Q, both the randomness of X and Z are considered in the concentration inequality.

Throughout the following, we use C to denote general constants independent of n and p but may change from one place to another. Let ζd = 1/2 if d = 4 and 0 otherwise.

LEMMA 2. *Under assumptions (A1) and (A2), for* j = 1, . . . , p*, we have*

$$\mathbb{P}\left(\frac{1}{n}\sum_{i=1}^{n}\left\|\hat{T}_{j}(X_{j}^{i})-T_{j}(X_{j}^{i})\right\|\geq\varepsilon\right)\leq\exp\left\{-C n\left[\left(\varepsilon-C n^{-\frac{1}{4\sqrt{2}}}(\log n)^{\zeta_{d}}\right)_{+}\right]^{2}\right\},$$  $a_{\pm}=aUa>0$

where a+ = aI{a > 0}.

Let T
(w)
j(x) and Tˆ
(w)
j(x) be the winsorized versions of Tj (x) and Tˆ(w)(x), respectively, with a threshold of √2 log n. The concentration inequality in Lemma 2 applies to Tˆ(w) and T
(w) by the observation that ∥Tˆj (Xi j
) − T(Xi j
)*∥ ≥ ∥*Tˆ
(w)
j(Xi j
) − T
(w)(Xi j
)∥ for any 1 ≤ i ≤ n.

COROLLARY 1. *Under assumptions (A1) and (A2), for* j = 1, . . . , p*, we have*

$$\mathbb{P}\left(\frac{1}{n}\sum_{i=1}^{n}\left\|\hat{T}_{j}^{(u)}(X_{j}^{i})-T^{(u)}(X_{j}^{i})\right\|\geq\varepsilon\right)\leq\exp\left\{-C n\left[\left(\varepsilon-C n^{-\frac{1}{2b/2}}(\log n)^{\zeta_{i}}\right)_{+}\right]^{2}\right\}.$$

We now show that the estimator Σ converges to Σ blockwise when ˆ p grows at an exponential rate of n. Recall that Σ is an estimator after the winsorization. ˆ
THEOREM 1. For any ε > 0, there exists a constant C > 0 *such that*

$$\mathbb{P}\left(\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}\geq\varepsilon\right)\leq C\exp\left\{-C\frac{n}{d\log^{2}n}\left[(\varepsilon-C n^{-\frac{1}{d\log^{2}n}}(\log n)^{\zeta_{d}+\frac{1}{2}})_{+}\right]^{2}\right\},$$

and consequently,

$$\mathbb{P}\left(\max_{1\leq j,k\leq p}\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}\geq\varepsilon\right)\leq C p^{2}\exp\left\{-C\frac{n}{d\log^{2}n}\left[(\varepsilon-C n^{-\frac{1}{k+d}}(\log n)^{\zeta_{d}+\frac{1}{2}})_{+}\right]^{2}\right\}.$$

The proof of Theorem 1 can be found in the Supplemental Material. As can be seen from the proof, the tail bound of the mean concentration of ∥Σˆjk−Σjk∥F has an order of log n/√n, that is, (∥Σˆjk−Σjk∥F−E[∥Σˆjk−Σjk∥F]) = Op(log n/√n). However, this rate is dominated by the convergence rate of the mean E[∥Σˆjk − Σjk∥F], which has an order of (log n)
ζd+ 12 /(n 1 4∨d ).

We compare Theorem 1 with the convergence rate of the Copula-GGM. For example, see Mai et al. (2023, Theorem 3) for the convergence rate of the normal score estimator and winsorization estimator of the Copula-GGM. We see that the Winsorization estimator Σˆ
of CMC-GGM has the same rate of tail bound as the Copula-GGM, but a slower rate of mean convergence, which is also of order log n/√n for Copula-GGM. This slower rate of mean convergence is due to the curse of dimensionality issue that arises when solving d-dimensional OT problems. Furthermore, when log p = *o(n/* log2 n), we have max1≤j,k≤p ∥Σˆjk − Σjk∥F =
Op((log n)
ζd+ 12 /(n 1 4∨d )) = op(1). This indicates that the dimension limit can be at log p =
O(n τ) with 0 *< τ <* 1.

To further establish the consistency of the group glasso estimator (14) for graph estimation, we introduce a group version of the irrepresentable condition, which is also used in Kolar et al. (2014) and Qiao et al. (2019), as an extension of the irrepresentable condition in Ravikumar et al. (2011). Let A = (Ajk)
p j,k=1 be an R
pd×pd block matrix, where Ajk ∈
R

d×dfor *j, k* = 1*, . . . , p*. We define the blockwise norms ∥A∥
(d)
∞ = max1≤j≤pPpk=1 ∥Ajk∥F,
∥A∥
(d)
max = max1≤j,k≤p ∥Ajk∥F, regarding them as the block versions of matrix ℓ∞-norm and maximum norm, respectively. The superscript (d) indicates the length of the block. Let E˜ = E ∪ {(1, *1), . . . ,(p, p*)} be the augmented edge set and E˜c be its complement. Let H = Θ−1 ⊗ Θ−1 ∈ R
(pd)
2×(pd)
2, where ⊗ is the Kronecker product. The matrix H is the Hessian operator of the loglikelihood function evaluated at the true Θ. For index set J,
J
′⊆ {1*, . . . , p*}, let HJJ′ ∈ R
d 2|J|×d 2|J
′| be the submatrix of H with row and column blocks in J and J
′. We assume that the following irrepresentable-type condition holds.

(A3) There exists a constant 0 ≤ α < 1 such that

$$\|H_{\bar{E}^{c}\bar{E}}(H_{\bar{E}\bar{E}})^{-1}\|_{\infty}^{(d^{2})}\leq1-\alpha.$$

Let κΣ = ∥Σ∥
(d)
∞ and κH = ∥H−1∥
(d 2)
∞ . Let s be the maximal degree of nodes in G. Define the following quantities:

$$\delta_{1}(n)=\frac{s\sqrt{d\log p}\log n}{\sqrt{n}},\mathrm{~and~}\delta_{2}(n)=\frac{(\log n)^{\zeta_{d}+\frac{1}{2}}}{n^{\frac{1}{4\sqrt{d}}}}.$$

Under conditions (A1), (A2), and (A3), we have the selection consistency of the CMC-GGM
in the following theorem.

THEOREM 2. Let λn ≍ δ1(n) ∧ δ2(n)*. Then, as* δ1(n) ∧ δ2(n) → 0, ∥Θˆ − Θ∥
(d)
max = op(1).

Consequently, the estimated graph Gˆ agrees with the true graph G *with high probability, that* is, P(Gˆ = G) → 1.

In Theorem 2, we see that δ1(n) corresponds to the tail bound while δ2(n) corresponds to the mean error bound. When log p ≺ n
(1− 2 4∨d
)(log n)
(2ζd−1), δ1(n) ≺ δ2(n), indicating that the mean error bound dominates the tail error bound. When log p ≻ n
(1− 2 4∨d
)(log n)
(2ζd−1),
δ1(n) ≻ δ2(n), indicating that the tail error bound dominates the mean error bound, and the convergence rate is the same as copula Gaussian model in Mai et al. (2023, Theorem 4).

The theorem also indicates that the dimension limit can be at most log p = *O(n/* log2 n).

The selection consistency using CMC transformed score can also be established with neighborhood group lasso selector, following the proof in, for example, Zhao et al. (2021).

We skip this part due to space limitation.

## 6 Projected Cyclically Monotone Copula For High Dimensional Attributes 6.1 Projected Cyclically Monotone Copula

In Section 3.1, we show that estimating the CM transformations {Tj}
p j=1 involves solving discrete-to-discrete OT problems. However, this estimation method suffers from curse of dimensionality. In fact, the minimax convergence rate of the estimated OT map between d-dimensional discrete measures is O(n
−1/d) (Niles-Weed and Rigollet, 2022; Fournier and Guillin, 2015). Theorems 1 and 2 also indicate that the convergence rate of graph estimation is limited by the dimension of vectors on each node. However, when the dimension of the vector is high, it is reasonable to assume the non-Gaussianity only appears on a rdimensional subspace, where *r < d*. Once the r-dimensional subspace is properly estimated, the convergence rate can be improved from O(n
−1/d) to O(n
−1/r). To achieve this, we adopt the idea in projection robust OT method (Paty and Cuturi, 2019) to develop a projected cyclically monotone copula model that improves the estimation accuracy.

For j = 1*, . . . , p*, we assume that there exists an orthogonal matrix Γj = (Uj, Vj ) ∈ R
d×d, where Uj ∈ R
d×r and Vj ∈ R
d×(d−r), such that Pj and Q only differ on an r-dimensional subspace spanned by Uj. Let Z ∼ N(0, Id). By Brenier's Theorem, the optimal transport between ΓTXj and ΓTZ can be written as (Tj, idRd−r ), where Tj: R
r → R
ris the optimal transport from U
TXj to U
TZ. Thus, the induced transformation Sjfrom Xj to Z can be written as Sj:= Γ ◦ (Tj, idRd−r ) ◦ Γ
T = Uj ◦ Tj ◦ U
T
j + VjV
T
j
.

We now define the Projected Cyclically Monotone Copula Gaussian (PCMCG) family.

DEFINITION 3. *A random vector* X = (XT
1
, XT
2
, . . . , XT
p
)
T ∈ R
dp *with subvector* Xj ∈ R
d, follows a projected cyclically monotone copula Gaussian (PCMCG) distribution if there exist cyclically monotone functions T = {Tj: R
r → R
r}
p j=1 *and orthogonal matrices* Γ = {Γj ∈
R

d×d: Γj = (Uj, Vj ), Uj ∈ R
d×r, Vj ∈ R
d×(d−r), Γ
T
jΓj = ΓjΓ
T
j = Id}
p j=1 *such that* (S1(X1)
T,
. . . , Sp(Xp)
T)
T ∼ N(0, Σ)*, where* Sj = Uj ◦ Tj ◦ U
T
j + VjV
T
j and Σ *has structure* (2) *with* Σjj = Id.

Let Z = Sj (Xj ). By the fact that Z ∼ N(0, Id), we know that U
T
j Z and V
T
j Z are independent, implying that U
T
j Xj and V
T
j Xj are independent. Since Sj, j = 1*, . . . , p* are cyclically monotone functions, they are unique optimal transport transformations from Pj to Q almost surely. Hence, the PCMCG family can be treated as a special case of the CMCG family in Definition 2.

Let Sj be the space spanned by Uj and S
⊥
j be its orthogonal complement spanned by Vj. Denote by PSj = UjU
T
jthe projection matrix onto the space spanned by Uj. We note that for a different choice of bases Uj, the function Tj may change, but the composition map Uj ◦Tj ◦U
T
j will be invariant. This is guaranteed because Uj ◦Tj ◦U
T
j is the optimal transport from the distribution of PSjXj to the distribution of PSjZ. Similarly, Sjis invariant because Sjis the optimal transports from Pj to Q. By Brenier theorem, they are unique almost surely.

Define an equivalence relation T ∼ T˜, if and only if there exists an orthogonal matrix A ∈ R
r×rsuch that T = A ◦ T˜ ◦ AT. Let [T] be the equivalence class of T over the set of cyclically monotone functions. We define the map PS([T]) = A ◦ T ◦ AT as the projected cyclically montone transformation of [T] onto subspace S, where A is any basis matrix spanning S. PS([T]) is well-defined because it is invariant for the choice of basis A and representative element [T]. Therefore, the transportation map defined in Definition 3 can be written as

$$S_{j}=P s_{j}([T_{j}])+P_{s_{j}^{\perp}},$$
j
, (21)
where Sjis the space spanned by Uj and PS
⊥
j is the usual projection matrix on subspace S
⊥
j
. Let S = (S1*, . . . , S*p) and S = (S1*, . . . ,* Sp). Therefore, for a random vector X defined by Definition (3), we write X ∼ PCMCG(S*, S,* Σ).

Similarly, for a radnom vector X ∼ PCMCG(S*, S,* Σ), we say it follows a CCMC-GGM
with graph G = (*V, E*) when Θjk = 0 is equivalent to (*j, k*) ∈/ E. The following proposition guarantees that the PCMC-GGM is identifiable.

PROPOSITION 4. *If two random vectors* X ∼ PCMCG(S, S, Σ) and X˜ ∼ PCMCG(S˜, S, ˜ Σ) ˜
have the same distribution, then S = S˜, Σ = Σ˜, and S = S˜ *almost everywhere.*

## 6.2 Estimation

Define U
∗: R
d → R
kto be the linear transformation associated with U by U
∗(x) = U
Tx. To estimate the non-Gaussianity subspace Sj, we consider the worst possible optimal transport cost over all possible r-dimensional subspace, that is,

$$U_{j}=\operatorname{argmax}_{U\in\operatorname{St}(d,r)}W_{2}(U_{\#}^{*}P_{j},U_{\#}^{*}Q),$$

where St(*d, r*) := {U ∈ R
d×r: U
TU = Ir} denotes the Stiefel manifold. At the sample level, we solve the max-min optimization problem

$$\operatorname*{max}_{U\in\operatorname{St}(d,r)}\operatorname*{min}_{\pi\in\Pi}\sum_{s=1}^{n}\sum_{t=1}^{n}\pi_{s,t}\|U^{\intercal}X_{j}^{s}-U^{\intercal}Z^{t}\|^{2},$$
$$(22)$$

where Π := {π ∈ R
n×n
+ : π1n = 1n, πT1n = 1n} denotes the transportation polytope. Here, we take the Kontorovich formulation of the OT problem for computing efficiency. We denote the solution of (22) as Uˆj and ˆπj. The optimal transport plan π indeed defines an optimal transport map in the sense that

$$\pi_{s t}=I\{t=\sigma_{j}(s)\}/n,\quad\mathrm{for~all~}1\leq s,t\leq n,$$

where σj (·) is a permutation of {1*, . . . , n*}. Define Tˆj (UˆjXi j
) = UˆjZ
σj (i), i = 1*, . . . , n*. The final transformations are then estimated by:

$$\hat{S}_{j}(X_{j}^{i})=\hat{U}_{j}\hat{T}_{j}(\hat{U}_{j}^{\intercal}X_{j}^{i})+\hat{V}_{j}\hat{V}_{j}^{\intercal}X_{j}^{i},\quad\mbox{for}i=1,\ldots,n,\ j=1,\ldots,p.$$

Define Pˆj and Qˆ same as in (10). Let Pj,Uˆj and QUˆj be the distribution of Uˆ T
j Xj and Uˆ T
j Z, respectively. Similarly, define the empirical measures as:

$$\hat{P}_{j,\hat{U}_{j}}=\frac{1}{n}\sum_{i=1}^{n}\delta_{\hat{U}_{j}^{\intercal}X_{j}^{i}},\quad\hat{Q}_{\hat{U}_{j}}=\frac{1}{n}\sum_{i=1}^{n}\delta_{\hat{U}_{j}^{\intercal}Z^{i}}.$$
$$\left(23\right)$$

Then Tˆjis the optimal transport from Pˆj,Uˆj to QˆUˆj
. We note that Sˆ defined in (23) does not transform Pˆj to Qˆ. Instead, Sˆ is the optimal transport from Pˆ to Qˆ∗, where

$$\hat{Q}^{*}=\frac{1}{n}\sum_{i=1}^{n}\delta_{\hat{U}_{j}\hat{U}_{j}^{\mathsf{T}}Z^{\sigma_{j}(i)}+\hat{V}_{j}\hat{V}_{j}^{\mathsf{T}}X^{i}}.$$

In practice, we first estimate the projection matrix Uj by solving (22) with entropy penalty to speed computation, that is,

$$\operatorname*{max}_{U\in\operatorname{St}(d,k)}\operatorname*{min}_{\pi\in\Pi}\sum_{s=1}^{n}\sum_{t=1}^{n}\pi_{s,t}\|U^{\intercal}X_{j}^{s}-U^{\intercal}Z^{t}\|^{2}-\eta H(\pi),$$
$$\left(24\right)$$

where η > 0 is a tuning parameter and H(π) := −⟨π, log(π)−1n1 T
n
⟩. To solve (24), we adopt the Riemannian block coordinate descent (RBCD) algorithm proposed in Huang et al. (2021).

To avoid the bias of estimating π due to the entropy penalty, we only obtain Uˆj, j = 1*, . . . , p* from (24) and then solve an exact OT problem using the projected data in a follow-up step.

## 6.3 Convergence Rate

We next develop the convergence rate of the PCMCG model for r = 1, where there exists one principal non-Gaussian direction. For j = 1*, . . . , p*, we assume that Pj,Uj is absolutely continuous to the Lebesgue measure, and thus, there exists a convex potential function ψj, such that Tj = ∇ψjis the optimal transport from Pj,Uj to QUj
. Let ψ
∗
j be the LegendreFenchel dual of ψj, defined in (6). To ensure the consistency of estimating the projected subspace Uj, we introduce two additional regularity conditions. First, we introduce the log Sobolev inequality to characterize the tail behavior of X as follows:
DEFINITION 4. *A probability measure* µ on R
d*is said to satisfy a log Sobolev inequality* with constant κ 2if

$$\int f^{2}\log f^{2}\,d\mu-\int f^{2}\,d\mu\log\left(\int f^{2}\,d\mu\right)\leq2\kappa^{2}\int\|\nabla f\|^{2}\,d\mu,\tag{25}$$
$\text{or}\,\int\,\text{-}1\,\,\mathbb{D}\,d\,\implies\,\mathbb{D}\,\cdot\,\sigma$
for all smooth function f : R
d → R *such that the integration are finite.*
The log Sobolev inequality holds for any strongly log-concave measure on R
d, that is, a measure of having density e V (x) and Hessian ∇2V ⪰ αId *(α >* 0). The log Sobolev inequality indicates the following transport inequality:

$$W_{2}^{2}(\nu,\mu)\leq\kappa^{2}\mathrm{KL}(\nu|\mu),\quad\mathrm{for~any~}\nu\in{\mathcal{P}}(\mathbb{R}^{d}),$$

where KL(ν|µ) is the Kullback–Leibler divergence. Please see Gozlan and L´eonard (2010) for more details on transport inequalities. For j = 1*, . . . , p*, we assume the following regularity conditions:
(A3) Pj satisfies the log Sobolev inequality with constant κ

$${\mathrm{\boldmath~nt~}}\kappa^{2},$$

(A4) There exists τ > 0 such that W2(Pj, Q) > τ .

Assumption (A4) requires the non-Gaussianity signal to be significant. We then establish a 0-concentration inequality for ∥Sˆj − Sj∥L1(Pˆj )
in Lemma 3.

LEMMA 3. For j = 1, . . . , p, assume ψj, j = 1, . . . , p satisfy assumption (A1) and (A2).

With assumptions (A3) and (A4), we have

$$\mathbb{P}\left({\frac{1}{n}}\sum_{i=1}^{n}\left\|{\hat{S}}_{j}(X_{j}^{i})-S_{j}(X_{j}^{i})\right\|\geq\varepsilon\right)\leq\exp\left\{-C n\left[(\varepsilon-C n^{-{\frac{1}{4}}})_{+}\right]^{2}\right\}.$$

Similar to the CMC setting, let S
(w)
j(x) and Sˆ
(w)
j(x) be a winsorized version of Sj (x)
and Sˆj (x) with threshold √2 log n, respectively. The concentration inequality in Lemma 3 applies to Sˆ(w) and S
(w).

COROLLARY 2. *With same assumptions in Lemma 3, we have*

$$\mathbb{P}\left(\frac{1}{n}\sum_{i=1}^{n}\left\|\hat{S}_{j}^{(w)}(X_{j}^{i})-S^{(w)}(X_{j}^{i})\right\|\geq\varepsilon\right)\leq\exp\left\{-C n\left[(\varepsilon-Cn^{-\frac{1}{4}})_{+}\right]^{2}\right\}.$$  In both the numerator and denominator is $L_{\infty}=\infty$, the 

Compared with the concentration inequalities in Lemma 2, the mean convergence rate is sharpened to n
− 14 from n
− 1 4∨d (log n)
ζd. Using Lemma 3, we can also obtain a sharper convergence rate for the covariance matrix estimation than Theorems 1 by replacing n
− 1 4∨d (log n)
ζd with n
− 14 . When the principal non-Gaussian dimension r > 1, stronger assumptions are required to guarantee the consistency of the estimated subspace Uˆj. We leave the investigation of such assumptions for future research.

## 7 Simulation 7.1 Graph Learning With Two Attributes

We evaluate the numerical performance of thresholding, group graphical lasso, and neighborhood group lasso estimators (with "and" rule) for CMC-GGM when the dimension on each node is 2. We also compare the performances of the three estimation methods with the Gaussian Graphical Model (GGM) and Copula Gaussian Graphical Model (Copula-GGM).

To design the experiments, we first generate d × p-dimensional Gaussian random vectors with mean 0 and the following block precision matrix Θ:
(A) Banded precision matrix: For j = 1*, . . . , p*, Θj,j = Id; for j ≥ 2, Θj,j−1 = Θj−1,j = 0.4Id; for j ≥ 3, Θj,j−2 = Θj−2,j = 0.2Id.

(B) Random precision matrix: Divide the graph into two connected parts, that is, let Θ = diag(Θ1, Θ2), where Θℓ ∈ R
p/2×p/2for ℓ = 1, 2. For any j ̸= *k, ℓ* = 1, 2, Θℓ j,k = ξId, where ξ = 0.3 with probability 0.1 and 0 otherwise; Θj,j = δ · Id, where δ is chosen to guarantee the positive definiteness of Θ.
(C) Hub-connected precision matrix: Generate a graph's edge set E as follows. First, for all *j < k*, we set Ejk = 1 with probability 0.01, and 0 otherwise. Next, we randomly select h = 2 hub nodes and set the elements of the corresponding rows and columns of E equal 1 with probability 0.5 and 0 otherwise. For s = 1*, . . . , M*, generate p × p matrix Ωs by

$$\Omega_{s,j k}=\Omega_{s,k j}=\begin{cases}\delta,&\mathrm{if}\ j=k,\\ 0,&\mathrm{if}\ E_{j k}=0,\\ \xi,&\mathrm{if}\ E_{j k}=1,\end{cases}$$

where ξ ∼ U([−0.75, −0.25] ∩ [0.25, 0.75]) and δ is chosen to guarantee the positive definiteness of Ωs. Let Ω be the block diagonal matrix diag(Ω1*, . . . ,* Ωd). The precision



matrix is rearranged as (Θjk)st = (Ωst)jk for all 1 ≤ *j, k* ≤ p and 1 ≤ *s, t* ≤ d.

Figure 2 shows the graph structure of Models (A), (B), and (C). Let Σ = Θ−1 be the covariance matrix, and diag(Σ)−1/2 = diag(Σ−1/2 11 *, . . . ,* Σ
−1/2 pp ) be the block diagonal matrix.

We generate Z = (Z
T
1
, . . . , ZT
p
)
T ∼ N(0, diag(Σ)−1/2Θ−1diag(Σ)−1/2), which ensures that the distributions of the node vectors are standard bivariate Gaussian. We refer to Z as the oracle Gaussian data that determines the graph structure. We then consider the following three transformations from Z to the observed data X:
(i) X = Z, which correspnds to observing Gaussian data;

(ii) Xjs = fjs(Zjs), for j = 1*, . . . , p* and s = 1, 2, where fjs is the exponential transformation, defined by
where σjs is the standard deviation of Zjs.

$$f_{j s}(z)=\sigma_{j s}\left(\frac{\exp(z)-E[\exp(Z_{j s})]}{\sqrt{\operatorname{var}(\exp(Z_{j s}))}}\right),$$  and deviation of $Z_{j s}$.  
(iii) For j = 1*, . . . , p*, define fj: R
2 → R
2 as fj = (fj1, fj2), where fjs, s = 1, 2 are the same as in (ii). Define gj: R
2 → R
2 as gj (z) = U(fj (U
Tz)), where U = ((1, −1)T(1,

$$\mathbf{\tau}=\mathbf{a}_{1}(Z_{1}),\quad\mathbf{\tau}=\mathbf{a}_{2}(Z_{2}),$$
$\mathrm{ot}\_Y$ ... 
1)T)/
√2 ∈ R
2×2. Let Xj = gj (Zj ).

We note that transformation (ii) is coordinatewise monotonic, which guarantees that the subvector Xjfollows a nonparanormal distribution but not a multivariate Gaussian. We design the marginal transformation fjs to preserve the marginal standard deviation of the transformed data. Transformation (iii) is not coordinate-wise monotonic but cyclically monotonic, which ensures that X has a CMCG distribution. Similar models with transformation (iii) are considered in Bryan et al. (2021) for semiparametric CCA modeling.

group-glasso thresholding nbd-group-lasso

Models CMC Copula Linear CMC Copula Linear CMC Copula Linear

A-i

0.977 0.982 0.983 0.976 0.982 0.983 0.991 0.993 0.994 (0.004) (0.003) (0.003) (0.007) (0.005) (0.005) (0.002) (0.002) (0.001)

A-ii

0.974 0.982 0.862 0.974 0.982 0.833 0.989 0.993 0.864 (0.004) (0.003) (0.011) (0.006) (0.005) (0.014) (0.003) (0.002) (0.013)

A-iii

0.974 0.950 0.863 0.971 0.940 0.834 0.989 0.966 0.862

(0.004) (0.007) (0.011) (0.006) (0.008) (0.013) (0.003) (0.005) (0.011)

Table 1: Means and standard errors (in parentheses) for AUC of Model A

group-glasso thresholding nbd-group-lasso

Models CMC Copula Linear CMC Copula Linear CMC Copula Linear

B-i

0.928 0.940 0.942 0.777 0.792 0.797 0.918 0.929 0.931

(0.012) (0.011) (0.011) (0.017) (0.017) (0.017) (0.013) (0.013) (0.013)

B-ii

0.922 0.939 0.776 0.77 0.791 0.613 0.914 0.929 0.753 (0.016) (0.014) (0.02) (0.02) (0.021) (0.023) (0.013) (0.013) (0.018)

B-iii

0.924 0.894 0.774 0.879 0.838 0.691 0.914 0.879 0.748

(0.013) (0.014) (0.016) (0.016) (0.016) (0.018) (0.014) (0.014) (0.017)

We conducted simulations with a network size of p = 100 and sample size of n = 300, repeating each simulation 50 times. We calculated the true positive rate (TPR) and false positive rate (FPR) for 20 different threshold values ϵn or tuning parameters λn, with which we generated a receiver operating characteristic (ROC) curve. The means and standard

| group-glasso   | thresholding   | nbd-group-lasso   |         |         |         |         |         |         |         |
|----------------|----------------|-------------------|---------|---------|---------|---------|---------|---------|---------|
| Models         | CMC            | Copula            | Linear  | CMC     | Copula  | Linear  | CMC     | Copula  | Linear  |
| 0.885          | 0.896          | 0.899             | 0.775   | 0.791   | 0.794   | 0.818   | 0.826   | 0.829   |         |
| C-i            | (0.019)        | (0.017)           | (0.017) | (0.025) | (0.025) | (0.026) | (0.023) | (0.024) | (0.024) |
| 0.880          | 0.896          | 0.746             | 0.767   | 0.791   | 0.638   | 0.812   | 0.826   | 0.687   |         |
| C-ii           | (0.018)        | (0.017)           | (0.028) | (0.025) | (0.025) | (0.038) | (0.023) | (0.024) | (0.029) |
| 0.877          | 0.849          | 0.742             | 0.760   | 0.728   | 0.637   | 0.815   | 0.784   | 0.687   |         |
| C-iii          | (0.019)        | (0.020)           | (0.028) | (0.037) | (0.032) | (0.037) | (0.023) | (0.023) | (0.030) |

deviations (in parentheses) of the associated area-under-curve values (AUC) are reported in Tables 1, 2, and 3.

Our results indicate the following points: (a) when the data are generated from a Gaussian distribution (transformation (i)), linear transformation gives the most accurate estimation, but the difference among the three transformation methods is not significant; (b) when the data are generated from a copula Gaussian distribution (transformation (ii)), CMC-GGM
and Copula-GGM give provide much more accurate estimation than GGM; (c) when the data are generated from a CMCG distribution, CMC-GGM significantly improves estimation accurate from Copula-GGM; (d) for Model A, the neighborhood group lasso provides higher AUC scores than the group glasso and thresholding; and (e) for the more challenging Models B and C, the group graphical lasso outperforms the neighborhood group lasso while thresholding performs poorly.

To visualize the comparison, in Figure 3 we display the average ROC curves of the methods estimated by graphical glasso and neighborhood group lasso. From the plot, we are further convinced that the CMC transformation methods (red curves) have the best overall performance when the data are generated from non-copula Gaussian distribution
(right column).

To better illustrate why copula models fail under setting (iii), we show the copula and CMC transformation results in Figure 4. We generate n = 300 samples from Model A-iii on one node. The green points are the oracle Gaussian data that we want to recover and use to estimate the precision matrix further. From left to right, the red points are observations, copula-transformed data, and CMC-transformed data, respectively. We see that in the middle panel, after the copula transformation, the red points are marginal Gaussian on both coordinates but jointly show a triangular shape, which deviates from the joint Gaussian



distribution.  Consequently, the values on both coordinates are estimated poorly, affecting the further estimation of the precision matrix. In contrast, the CMC transformation can better recover the underlying oracle points, as demonstrated in the right panel.



## 7.2 Graph Learning With More Than Two Attributes

In this subsection, we compare the performance of Copula-GGM, CMC-GGM, and PCMC- GGM when the number of attributes on each node is larger than 2. We first generate Gaussian data from Model (A) in Section 7.1. For j = 1*, . . . , p*, define fj: R
r → R
r by fj = (fj1, · · · , fjr), where fjs is univariate monotonic function. We consider two choices for fjs: the first one is the exponential map defined in Section 7.1 (ii); the second one is the cubic map defined by

$$f_{j s}(z)=\sigma_{j s}\left(\frac{z^{3}-E[Z_{j s}^{3}]}{\sqrt{\operatorname{var}(Z_{j s}^{3})}}\right)$$

 ,
where σjs is the standard deviation of Zjs. Then we define gj: R
d → R
d as gj (z) =
U(fj (U
Tz)) + V V Tz, where U ∈ R
d×r and (*U, V* ) ∈ R
d×dis a orthogonal matrix. Let non-Gaussian direction contained in Xj. More numerical results on r > 1 can be found in the Supplementary Material.

For PCMC-GGM, we independently generate 10 samples and use the Riemannian block coordinate descent (RBCD) algorithm proposed in Huang et al. (2021) to solve Uˆl j
, j = 1,
. . . , p, l = 1*, . . . ,* 10. We then take the extrinsic average of 10 repeats to obtain the estimator Uˆj, which is the first eigenvector of P10 l=1 Uˆl j
(Uˆl j
)
T. We assume that the true dimension 1 is



known.  Determining the dimension for the projected subspace distance in a more systematic way is beyond the scope of this paper. We then solve the OT problem between projected samples { ˆ U j X j } [ 2 ] [ 
The PCMC transformation is then estimated by (23).  After 50 repeats of the experiments, we plot the average ROC curves of the PCMC-GGM, CMC-GGM, and Copula-GGM in Figure 5. We also report the means and standard deviations (in parentheses) of the associated AUC scores in Table 4. We observe from the table that the accuracy of CMC-GGM drops sharply with the increase of the attribute dimension.  Overall, PCMC-GGM outperforms Copula-GGM and CMC-GGM.

We provide a visualization of the Copula, CMC, and PCMC transformations in Figure 6. Specifically, we consider the data on one node in Model A-iv-cubic when d = 5 and plot the data on the first two coordinates. The green points are the oracle Gaussian data. From left to right, the red points are the transformed data from Copula, CMC, and PCMC trans-

| group-glasso   | nbd-group-lasso   | thresholding   |         |         |         |         |         |         |         |       |
|----------------|-------------------|----------------|---------|---------|---------|---------|---------|---------|---------|-------|
| Model          | d                 | CMC            | Copula  | PCMC    | CMC     | Copula  | PCMC    | CMC     | Copula  | PCMC  |
| 3              | 0.921             | 0.920          | 0.942   | 0.949   | 0.944   | 0.970   | 0.917   | 0.915   | 0.949   |       |
| (0.013)        | (0.014)           | (0.01)         | (0.009) | (0.011) | (0.007) | (0.017) | (0.014) | (0.013) |         |       |
| 5              | 0.827             | 0.863          | 0.875   | 0.840   | 0.882   | 0.915   | 0.662   | 0.744   | 0.789   |       |
| A-iv-exp       | (0.018)           | (0.014)        | (0.052) | (0.018) | (0.014) | (0.012) | (0.028) | (0.030) | (0.026) |       |
| 7              | 0.747             | 0.820          | 0.845   | 0.744   | 0.834   | 0.860   | 0.593   | 0.696   | 0.739   |       |
| (0.019)        | (0.016)           | (0.018)        | (0.019) | (0.017) | (0.015) | (0.031) | (0.024) | (0.020) |         |       |
| 3              | 0.914             | 0.922          | 0.933   | 0.948   | 0.951   | 0.967   | 0.918   | 0.914   | 0.94    |       |
| (0.011)        | (0.013)           | (0.013)        | (0.009) | (0.011) | (0.008) | (0.013) | (0.019) | (0.012) |         |       |
| A-iv-cubic     | 5                 | 0.83           | 0.874   | 0.877   | 0.845   | 0.892   | 0.918   | 0.677   | 0.76    | 0.788 |
| (0.019)        | (0.017)           | (0.027)        | (0.018) | (0.015) | (0.014) | (0.028) | (0.020) | (0.022) |         |       |
| 7              | 0.758             | 0.833          | 0.826   | 0.755   | 0.849   | 0.867   | 0.602   | 0.715   | 0.739   |       |
| (0.022)        | (0.020)           | (0.050)        | (0.020) | (0.019) | (0.016) | (0.028) | (0.029) | (0.028) |         |       |

formations, respectively. We observe that in the left panel, after the copula transformation, red points still show non-Gaussianity along direction (1, 1, *0, . . . ,* 0)T. In the middle panel, after the CMC transformation, red points can not recover green points accurately due to the large estimation error arising from solving a high-dimensional OT problem. In contrast, the PCMC transformation can accurately recover the underlying oracle points, as shown in the right panel.



## 8 Real Applications

In this section, we consider two data applications where multi-attributes occur naturally. Since the ground truth is unknown in the data application, the goal of the analysis is only to visualize and explore the underlying dependency structures of the data. We will focus on showing the non-Guassianality of the data and compare the performance of GGM, Copula-
GGM, and CMC-GGM. We use the group glasso to estimate the graph, which performs the best in the simulations.

## 8.1 Gene/Protein Regulatory Network Inference

We applied the CMC-GGM to reconstruct networks on breast cancer data sets from the National Cancer Institute (https://www.cancer.gov/), referred to as NCI-60 and analyzed in Katenka and Kolaczyk (2011); Kolar et al. (2014) and Chiquet et al. (2019). The data set contains protein profiles (reverse-phase lysate arrays for 92 antibodies) and gene profiles
(normalized RNA microarray intensities from Human Genome U95 Affymetrix chip-set for about 9000 genes). Katenka and Kolaczyk (2011) constructed a 'concensus' data set containing 91 (p = 91) protein/gene profiles matched in pairs (d = 2) by common Entrez identifiers across 60 (n = 60) cancer cells.

| GGM                                  | Copula-GGM   | CMC-GGM   |       |
|--------------------------------------|--------------|-----------|-------|
| Number of edges                      | 299          | 309       | 168   |
| Number of shared edges with GGM      | **           | 183       | 129   |
| Avg Node Degree                      | 6.571        | 6.791     | 3.692 |
| Number of nodes with non-Gaussianity | 69           | 9         | 0     |

Table 5: Summary statistics for gene/protein networks estimated by GGM, Copula-GGM,
and CMC-GGM
We begin by applying the group glasso for GGM to fit the gene/protein network and then compare it with the network constructed using the Copula-GGM and CMC-GGM. For each method, we use the 10-fold cross-validation to select the tuning parameters, resulting in dense networks with a sparsity of about 0.4. We then estimate the network 50 times based on bootstrap samples. The stable graph was then constructed from the edges that appeared in at least 90% of the bootstrap replications. Table 5 provides a few summary statistics for the estimated networks. To test the joint Gaussianity of the data on each node, we use the energy statistics (Sz´ekely and Rizzo, 2013) with a permutation test of 499 replications.

A node is identified to have non-Gaussian data if the p-value is less than 0.05. Among all 91 nodes, 69 have non-Gaussian data, and 9 still exhibit non-Gaussianity even after copula transformations. Figure 7 shows the graph fitted by GGM and CMC-GGM, where red cells represent the edge shared by the two methods, green cells represent the edges unique to GGM, and blue cells represent the edges unique to CMC-GGM. The differences in networks require a closer biological inspection based on domain knowledge.



## 8.2 Color Texture Images

Pavez and Ortega (2016) and Pavez et al. (2018) built undirected graphs for grayscale images to infer the dependence of a pixel on neighboring pixels. Tugnait (2021) extended this idea to build a multi-attribute graphical model for colored images, where each node represents three attributes (RGB components) from a pixel.

To evaluate our method, we selected two images (Image 79 and Image 105) from the Colored Brodatz Texture Database (https://multibandtexture.recherche.usherbroo ke.ca/). We label image 79 as image 1 and image 105 as Image 2. Two images are read as a raster object with dimension 640 × 640 × 3 in R. For image 1, we extracted rows 481 through 640 and columns 481 through 640. For image 2, we extracted rows 321 through 480 and columns 1 through 160. This creates the 160 × 160 patches used to build image graphs, visualized in Figure 8(a) and (d). The patches were then partitioned into non-overlapping 8 × 8 blocks and then vectorized into 64-dimensional pixel vectors. For each node, we have three attributes associated with RGB decompositions. Therefore, we have a data set with sizes n = 400, p = 64, and d = 3. We found that the data showed non-Gaussianity with p-values less than 0.05 from an energy test at all nodes. Even after copula transformations, non-Gaussianity still persisted. We compared the performance of GGM and CMC-GGM on this data set. We used the BIC-based method to select the tuning parameters. For image 1, CMC-GGM and GGM obtained graphs with sparsities of 0.162 and 0.174, respectively. For image 2, CMC-GGM and GGM drive graphs with sparsities of 0.183 and 0.211, respectively.





The estimated graphs are visualized in Figure 8. The color and width of the links indicate the edge weights, which are taken as the Frobenius norm of the block matrix ∥Θˆjk∥F . By comparing the estimated graphs with the raw texture images, we can observe that strong links capture the principle texture orientations. Specifically, for image 1, vertical and some horizontal directions are the primary orientation of the texture; for image 2, the horizontal direction is the primary orientation. By comparing the graph (b) and (d), and (e) and (f), we see that using CMC transformation helps to estimate more precise graphs that match the raw image. On the other hand, the GGM may retain more error signals, such as the vertical signals on the upper left corner of graph (e).

## 9 Conclusion

This paper presents a new semiparametric copula graphical model for multi-attribute data based on the newly introduced cyclically monotone copula. The proposed model is more flexible than the existing copula Gaussian graphical model that only performs coordinatewise Gaussianization. We demonstrate both theoretical and numerical properties of the proposed methods. In future work, it will be interesting to study other types of graphical models such as Xue et al. (2012); Yang et al. (2015); Tao et al. (2024); Lee et al. (2022) using optimal transport theory.

## References

Abramovich, F., Benjamini, Y., Donoho, D. L. and Johnstone, I. M. (2006), 'Adapting to unknown sparsity by controlling the false discovery rate', *The Annals of Statistics* 34(2), 584–653.

Brenier, Y. (1991), 'Polar factorization and monotone rearrangement of vector-valued functions', *Communications on Pure and Applied Mathematics* 44(4), 375–417.

Bryan, J. G., Niles-Weed, J. and Hoff, P. D. (2021), 'The multirank likelihood and cyclically monotone monte carlo: a semiparametric approach to cca', arXiv preprint arXiv:2112.07465 .
Caffarelli, L. A. (2000), 'Monotonicity properties of optimal transportation and the fkg and related inequalities', *Communications in Mathematical Physics* 214, 547–563.

Cai, T., Liu, W. and Luo, X. (2011), 'A constrained l 1 minimization approach to sparse precision matrix estimation', *Journal of the American Statistical Association* 106(494), 594–
607.
Carlier, G., Chernozhukov, V. and Galichon, A. (2016), 'Vector quantile regression: an optimal transport approach', *The Annals of Statistics* 44(3), 1165–1192.

Chernozhukov, V., Galichon, A., Hallin, M. and Henry, M. (2017), 'Monge–kantorovich depth, quantiles, ranks and signs', *The Annals of Statistics* 45(1), 223–256.

Chiquet, J., Rigaill, G. and Sundqvist, M. (2019), 'A multiattribute gaussian graphical model for inferring multiscale regulatory networks: an application in breast cancer', *Gene* Regulatory Networks: Methods and Protocols pp. 143–160.
Colombo, M. and Fathi, M. (2021), 'Bounds on optimal transport maps onto log-concave measures', *Journal of Differential Equations* 271, 1007–1022.

Deb, N., Ghosal, P. and Sen, B. (2021), 'Rates of estimation of optimal transport maps using plug-in estimators via barycentric projections', Advances in Neural Information Processing Systems 34, 29736–29753.
Deb, N. and Sen, B. (2023), 'Multivariate rank-based distribution-free nonparametric testing using measure transportation', 118(541), 192–207.

Deshpande, I., Zhang, Z. and Schwing, A. G. (2018), Generative modeling using the sliced wasserstein distance, in 'Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition', pp. 3483–3491.
Fan, Y. and Henry, M. (2023), 'Vector copulas', *Journal of Econometrics* 234(1), 128–150.

Fournier, N. and Guillin, A. (2015), 'On the rate of convergence in wasserstein distance of the empirical measure', *Probability Theory and Related Fields* 162(3), 707–738.

Friedman, J., Hastie, T. and Tibshirani, R. (2008), 'Sparse inverse covariance estimation with the graphical lasso', *Biostatistics* 9(3), 432–441.

Ghosal, P. and Sen, B. (2022), 'Multivariate ranks and quantiles using optimal transport:
Consistency, rates and nonparametric testing', *The Annals of Statistics* 50(2), 1012–1037.

Gozlan, N. and L´eonard, C. (2010), 'Transport inequalities. a survey', *arXiv preprint* arXiv:1003.3852 .

Hallin, M., Del Barrio, E., Cuesta-Albertos, J. and Matr´an, C. (2021), 'Distribution and quantile functions, ranks and signs in dimension d: A measure transportation approach',
The Annals of Statistics 49(2), 1139–1165.
Hiriart-Urruty, J.-B. and Lemar´echal, C. (2004), *Fundamentals of convex analysis*, Springer Science & Business Media.

Huang, M., Ma, S. and Lai, L. (2021), A riemannian block coordinate descent method for computing the projection robust wasserstein distance, in 'International Conference on Machine Learning', PMLR, pp. 4446–4455.

Jonker, R. and Volgenant, T. (1988), A shortest augmenting path algorithm for dense and sparse linear assignment problems, in 'DGOR/NSOR: Papers of the 16th Annual Meeting of DGOR in Cooperation with NSOR/Vortr¨age der 16. Jahrestagung der DGOR zusammen mit der NSOR', Springer, pp. 622–622.

Kantorovich, L. V. (1948), On a problem of monge, in 'CR (Doklady) Acad. Sci. URSS
(NS)', Vol. 3, pp. 225–226.

Katenka, N. and Kolaczyk, E. (2011), 'Multi-attribute networks and the impact of partial information on inference and characterization', *arXiv preprint arXiv:1109.3160* .

Klaassen, C. A. and Wellner, J. A. (1997), 'Efficient estimation in the bivariate normal copula model: normal margins are least favourable', *Bernoulli* pp. 55–77.

Kolar, M., Liu, H. and Xing, E. (2013), Markov network estimation from multi-attribute data, in 'International Conference on Machine Learning', PMLR, pp. 73–81.

Kolar, M., Liu, H. and Xing, E. P. (2014), 'Graph estimation from multi-attribute data',
Journal of Machine Learning Research 15(1), 1713–1750.

Lafferty, J., Liu, H. and Wasserman, L. (2012), 'Sparse nonparametric graphical models',
Statistical Science 27(4), 519–537.

Lee, K. H., Chen, Q., DeSarbo, W. S. and Xue, L. (2022), 'Estimating finite mixtures of ordinal graphical models', *Psychometrika* 87(1), 83–106.

Liu, H., Han, F., Yuan, M., Lafferty, J. and Wasserman, L. (2012), 'High-dimensional semiparametric gaussian copula graphical models', *The Annals of Statistics* 40(4), 2293–2326.

Liu, H., Lafferty, J. and Wasserman, L. (2009), 'The nonparanormal: Semiparametric estimation of high dimensional undirected graphs', *Journal of Machine Learning Research* 10(80), 2295–2328.

Mai, Q., He, D. and Zou, H. (2023), 'Coordinatewise gaussianization: Theories and applications', *Journal of the American Statistical Association* 118(544), 2329–2343.

Manole, T., Balakrishnan, S., Niles-Weed, J. and Wasserman, L. (2021), 'Plugin estimation of smooth optimal transport maps', *arXiv preprint arXiv:2107.12364* .

Manole, T. and Niles-Weed, J. (2021), 'Sharp convergence rates for empirical optimal transport with smooth costs', *arXiv preprint arXiv:2106.13181* .

McCann, R. J. (1995), 'Existence and uniqueness of monotone measure-preserving maps',
Duke Mathematical Journal 80(2), 309–323.

Meinshausen, N. and B¨uhlmann, P. (2006), 'High-dimensional graphs and variable selection with the lasso', *The Annals of Statistics* 34(3), 1436–1462.

Meinshausen, N. and B¨uhlmann, P. (2010), 'Stability selection', Journal of the Royal Statistical Society: Series B (Statistical Methodology) 72(4), 417–473.

Meng, C., Ke, Y., Zhang, J., Zhang, M., Zhong, W. and Ma, P. (2019), 'Large-scale optimal transport map estimation using projection pursuit', *Advances in Neural Information* Processing Systems 32.

Niles-Weed, J. and Rigollet, P. (2022), 'Estimation of wasserstein distances in the spiked transport model', *Bernoulli* 28(4), 2663–2688.

Paty, F.-P. and Cuturi, M. (2019), Subspace robust wasserstein distances, in 'International Conference on Machine Learning', PMLR, pp. 5072–5081.

Pavez, E., Egilmez, H. E. and Ortega, A. (2018), 'Learning graphs with monotone topology properties and multiple connected components', *IEEE Transactions on Signal Processing* 66(9), 2399–2413.

Pavez, E. and Ortega, A. (2016), Generalized laplacian precision matrix estimation for graph signal processing, in '2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)', IEEE, pp. 6350–6354.

Qiao, X., Guo, S. and James, G. M. (2019), 'Functional graphical models', Journal of the American Statistical Association 114(525), 211–222.

Ravikumar, P., Wainwright, M. J., Raskutti, G. and Yu, B. (2011), 'High-dimensional covariance estimation by minimizing ℓ1-penalized log-determinant divergence', Electronic Journal of Statistics 5, 935–980.

Rockafellar, R. (1966), 'Characterization of the subdifferentials of convex functions', *Pacific* Journal of Mathematics 17(3), 497–510.

Shi, H., Drton, M. and Han, F. (2022), 'Distribution-free consistent independence tests via center-outward ranks and signs', *Journal of the American Statistical Association* 117(537), 395–410.
Solea, E. and Li, B. (2022), 'Copula gaussian graphical models for functional data', *Journal* of the American Statistical Association 117(538), 781–793.

Sz´ekely, G. J. and Rizzo, M. L. (2013), 'Energy statistics: A class of statistics based on distances', *Journal of Statistical Planning and Inference* 143(8), 1249–1272.

Tao, J., Li, B. and Xue, L. (2024), 'An additive graphical model for discrete data', Journal of the American Statistical Association 119(545), 368–381.

Tugnait, J. K. (2021), 'Sparse-group lasso for graph learning from multi-attribute data',
IEEE Transactions on Signal Processing 69, 1771–1786.
Villani, C. (2009), *Optimal Transport: Old and New*, Vol. 338, Springer.

Xue, L. and Zou, H. (2012), 'Regularized rank-based estimation of high-dimensional nonparanormal graphical models', *The Annals of Statistics* 40(5), 2541–2571.

Xue, L., Zou, H. and Cai, T. (2012), 'Nonconcave penalized composite conditional likelihood estimation of sparse ising models', *The Annals of Statistics* 40(3), 1403–1429.

Yang, E., Ravikumar, P., Allen, G. I. and Liu, Z. (2015), 'Graphical models via univariate exponential family distributions', *The Journal of Machine Learning Research* 16(1), 3813– 3847.

Yang, Y. and Zou, H. (2015), 'A fast unified algorithm for solving group-lasso penalize learning problems', *Statistics and Computing* 25, 1129–1141.

Yuan, M. and Lin, Y. (2007), 'Model selection and estimation in the gaussian graphical model', *Biometrika* 94(1), 19–35.

Zhang, J., Ma, P., Zhong, W. and Meng, C. (2022), 'Projection-based techniques for highdimensional optimal transport problems', *Wiley Interdisciplinary Reviews: Computational* Statistics p. e1587.
Zhang, T. and Zou, H. (2014), 'Sparse precision matrix estimation via lasso penalized d-trace loss', *Biometrika* 101(1), 103–120.

Zhao, B., Zhai, S., Wang, Y. S. and Kolar, M. (2021), 'High-dimensional functional graphical model structure learning via neighborhood selection approach', arXiv preprint arXiv:2105.02487 .