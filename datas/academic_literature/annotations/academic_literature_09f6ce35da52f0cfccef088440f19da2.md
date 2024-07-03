# A Copula Graphical Model for Multi-Attribute Data using Optimal Transport 

Qi Zhang, Bing Li, and Lingzhou Xue<br>Department of Statistics, The Pennsylvania State University


#### Abstract

Motivated by modern data forms such as images and multi-view data, the multiattribute graphical model aims to explore the conditional independence structure among vectors. Under the Gaussian assumption, the conditional independence between vectors is characterized by blockwise zeros in the precision matrix. To relax the restrictive Gaussian assumption, in this paper, we introduce a novel semiparametric multiattribute graphical model based on a new copula named Cyclically Monotone Copula. This new copula treats the distribution of the node vectors as multivariate marginals and transforms them into Gaussian distributions based on the optimal transport theory. Since the model allows the node vectors to have arbitrary continuous distributions, it is more flexible than the classical Gaussian copula method that performs coordinatewise Gaussianization. We establish the concentration inequalities of the estimated covariance matrices and provide sufficient conditions for selection consistency of the group graphical lasso estimator. For the setting with high-dimensional attributes, a Projected Cyclically Monotone Copula model is proposed to address the curse of dimensionality issue that arises from solving high-dimensional optimal transport problems. Numerical results based on synthetic and real data show the efficiency and flexibility of our methods.


Keywords: Multi-attribute data; Non-Gaussian data; Optimal transport.

## 1 Introduction

The undirected graphical model is commonly used to study the conditional independence relations among a set of random variables. Given a $p$-dimensional random vector $X$, the
goal is to estimate the undirected graph $\mathcal{G}=(V, E)$, where $V$ is the node set of cardinality $p$, corresponding to the indices components of $X, E$ is the edge set indicating whether two nodes are connected, which happens if and only if the two random variables on the nodes are conditionally dependent. For multivariate Gaussian $X \sim N(\mu, \Sigma)$, the precision matrix $\Theta=\Sigma^{-1}$ fully characterizes the conditional independence relations, making sparse precision matrix estimation the main approach for high-dimensional graph estimation. Methods for this include the neighborhood selection (Meinshausen and Bühlmann, 2006), Graphical Lasso (Yuan and Lin, 2007; Friedman et al., 2008), constrained $\ell_{1}$-minimization (Cai et al. 2011), and penalized D-trace loss (Zhang and Zou, 2014; Tao et al., 2024). To relax the Gaussian assumption, Liu et al. (2009) proposed a Copula Gaussian Graphical Model (Copula-GGM), which assumes that $p$ marginal transformations can transform the data to multivariate Gaussian. The model coincides with the Gaussian copula when the transformations are monotone. Rank-based correlation estimators for the Copula-GGM are proposed by Liu et al. (2012) and Xue and Zou (2012). A comprehensive review of this direction is available in Lafferty et al. (2012). The advantage of the copula approach is it retains the simplicity of the conditional independence structure while allowing the marginal distribution to be arbitrary.

The classical undirected graphical model only considers scalar random variables on nodes. However, in modern applications, there is a need for a graphical model with nodes representing multi-attribute entities or random vectors. Kolar et al. (2013, 2014) developed the multi-attribute graphical model where nodes correspond to vectors representing multiattribute entities and edges encode the conditional dependence between vectors. The model has been successfully applied in various domains, including uncovering gene regulatory networks from gene and protein profiles (Chiquet et al., 2019), inferring the brain connectivity graph from positron emission tomography data (Kolar et al., 2014), and inferring color image graphs by modeling the dependence between pixels (Tugnait, 2021).

In the multi-attribute graphical model, when the data follows a multivariate Gaussian distribution, conditional independence can still be inferred from the corresponding block in the precision matrix. To relax the Gaussian assumption, we may still apply a coordinatewise monotone transformation as we did for classical Gaussian graphical model. However, the coordinatewise Gaussianization is unnecessarily strong in the multi-attribute setting. To see the situation clearly, consider the following assumptions:

1. after transforming every element of $X$ to Gaussian, $X$ is jointly Gaussian;
2. after transforming every node vector of $X$ to Gaussian, $X$ is jointly Gaussian.

By logic, the first assumption implies the second. The first statement is what underlies the current copula Gaussian graphical models; the second uderlies the the new copula model we propose. To provide more intuition, in Figure 1 we plot three scenarios: a cross-shaped distribution, a v-shaped distribution, and a triangle-shaped distribution. In all cases, the two elements are marginally distributed as Gaussian, but jointly the vectors are strongly nonGaussian. If we have three node vectors having these three distributions, then no marginal transformation can lead to joint Gaussian distribution $X$. This motivates us to develop more
![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-03.jpg?height=536&width=1658&top_left_y=724&top_left_x=230)

Figure 1: Visualization of jointly non-Gaussianity among 2-dimensional data

flexible semiparametric models that link multi-dimensional marginals in a graph.

More rigorously, a multi-attribute graphical model can be viewed as a random vector $X=\left(X_{1}^{\top}, X_{2}^{\top}, \ldots, X_{p}^{\top}\right)^{\top} \in \oplus_{j=1}^{p} \mathbb{R}^{d_{j}}$ along with a graph $\mathcal{G}$ of $p$ nodes, where nodes $j$ and $k$ are connected if and only if $X_{j}$ and $X_{k}$ are conditionally dependent given $X_{-(j, k)}=\left\{X_{\ell}\right.$, $\ell \neq j, k\}$. To link the multivariate marginals, we introduce a copula, called the Cyclically Monotone Copula, based on optimal transport theory. Specifically, we solve an optimal transport problem from the distribution of each node vector to a Gaussian distribution, and assume that optimal transport maps $\left\{T_{j}\right\}_{j=1}^{p}$ transform the entire $X$ to joint Gaussian. The name Cyclically Monotone describes the geometric structure of the optimal transport map based on the result of Brenier (1991). This copula model is very flexible, as it allows the multivariate marginals to be arbitrary continuous distributions, including the scenario described in Figure 1 .

Our approach is inspired by the multivariate ranks introduced by Chernozhukov et al. (2017), which have been used for multivariate independence test (Ghosal and Sen, 2022. Deb and Sen, 2023; Shi et al. 2022), vector quantile regression (Carlier et al., 2016), among others. Two related works include the semiparametric CCA model developed by Bryan et al. (2021) based on a generalized Gaussian copula, and the vector copula based on measure
transportation proposed in Fan and Henry (2023). In this paper, we use the proposed copula to estimate high-dimensional graphical models.

Estimating the cyclically monotone transformations $\left\{T_{j}\right\}_{j=1}^{p}$ directly requires solving discrete-to-discrete optimal transport problems, which suffers from the curse of dimensionality issue with a minimax rate of $O\left(n^{-1 / d}\right.$ ) Fournier and Guillin, 2015, Niles-Weed and Rigollet, 2022). This can result in an inaccurate estimation of the graph structure, especially when the numbers of attributes on some nodes are large. To address this, we propose a projected cyclically monotone copula (PCMC) for the multi-attribute graphical model with large-dimensional attributes. We assume that the non-Gaussianity of the $d$-dimensional attributes only appears in a low-dimensional subspace. After properly estimate the lowdimensional non-Gaussian subspace and perform Gaussianization within it, the data can be efficiently transformed into a Gaussian distribution. This idea stems from the recent developments of projection-based techniques for solving high-dimensional optimal transport problems, such as the slicing approach (Deshpande et al., 2018), projection pursuit approach (Meng et al., 2019), and projection robust method (Paty and Cuturi, 2019). A comprehensive review of this direction is provided in Zhang et al. (2022).

The rest of the paper is organized as follows. In Section 3, we introduce the cyclically monotone copula Gaussian graphical model (CMC-GGM) for multi-attribute data and extend it to the composition cyclically monotone copula Gaussian graphical model (CCMCGGM). Estimation methods are developed, and their consistency and convergence rates established, in Sections 4 and 5. In Section 6, we propose the projected cyclically monotone copula Gaussian graphical Model (PCMC-GGM) to avoid the curse of dimensionality arising from solving optimal transport problems. In Section 7, we present simulation results that compare our methods with Gaussian graphical models and copula Gaussian graphical models for multi-attributes data. Finally, in Section 8, we apply the CMC-GGM to estimate the gene and protein regulatory network and color texture graph.

## 2 Background

### 2.1 Multi-Attribute Graphical Model

Consider $p$ random vectors $X_{j} \in \mathbb{R}^{d_{j}}$ for $j=1, \ldots, p$. We assume $d=d_{1}=\cdots=d_{p}$ for notational simplicity, but the model can be easily extended to cover distinct $d$ 's. We let $X=\left(X_{1}^{\top}, X_{2}^{\top}, \ldots, X_{p}^{\top}\right)^{\top} \in \mathbb{R}^{d p}$. Let $\mathcal{G}(V, E)$ be the undirected graph with node set $V=\{1$, $2, \ldots, p\}$ and edge set $E \subseteq\{(j, k) \in V \times V: j \neq k\}$. We say $X$ follows a multi-attribute
graphical model with the graph $\mathcal{G}(V, E)$ if the edge set $E$ is determined by the conditional independence structure among $X_{1}, \ldots, X_{p}$ in the following way:

$$
X_{j} \Perp X_{k} \mid X_{-(j, k)} \text { if and only if }(j, k) \notin E
$$

where $X_{-(j, k)}=\left\{X_{\ell}, \ell \neq j, k\right\}$. We call $X_{1}, \ldots, X_{p}$ the node vectors. If, furthermore, $X$ follows a multivariate Gaussian distribution $N(0, \Sigma)$, where $\Sigma$ and $\Theta=\Sigma^{-1}$ have block structures

$$
\Sigma=\left(\begin{array}{cccc}
\Sigma_{11} & \Sigma_{12} & \ldots & \Sigma_{1 p} \\
\Sigma_{21} & \Sigma_{22} & \ldots & \Sigma_{2 p} \\
\vdots & \vdots & \ddots & \vdots \\
\Sigma_{p 1} & \Sigma_{p 2} & \cdots & \Sigma_{p p}
\end{array}\right) \text { and } \Theta=\left(\begin{array}{cccc}
\Theta_{11} & \Theta_{12} & \ldots & \Theta_{1 p} \\
\Theta_{21} & \Theta_{22} & \ldots & \Theta_{2 p} \\
\vdots & \vdots & \ddots & \vdots \\
\Theta_{p 1} & \Theta_{p 2} & \cdots & \Theta_{p p}
\end{array}\right)
$$

then we refer to the model as the Gaussian Graphical Model (GGM) for multi-attributes data. Under the Gaussian assumption, the conditional independence in (1) can be replaced by $\Theta_{j k}=0$; that is, there is an edge between $j$ and $k$ iff $\Theta_{j k} \neq 0$.

Compared with the single-attribute graphical model, the multi-attribute graphical model has a dependence structure within each node, parametrized by sub-precision matrices $\Theta_{j j}$, $j=1, \ldots, p$ on the diagonal of $\Theta$. However, to infer the edge set $E$ of the graph, we only need to consider the conditional dependence relations across different node vectors. Therefore, any one-to-one transformations on $\left\{X_{j}\right\}_{j=1}^{p}$ that preserves the conditional dependence structure can be applied. For instance, there exist orthogonal matrices $\Gamma_{j} \in \mathbb{R}^{d \times d}$ such that $\Gamma_{j} X_{j} \sim$ $N\left(0, I_{d}\right)$ for $j=1, \ldots, p$. Let $\Gamma=\left(\Gamma_{1}, \ldots, \Gamma_{p}\right)$ and $\tilde{X}=\Gamma X$. The graph estimated using $X$ is equivalent to that of $\tilde{X}$. Therefore, without loss of generality, we can always assume the diagonal blocks $\left\{\Sigma_{j j}\right\}_{j=1}^{p}$ to be the identity matrices.

### 2.2 Optimal Transport and Cyclical Monotonicity

Let $\mathcal{P}\left(\mathbb{R}^{d}\right)$ be the set of probability measures on $\mathbb{R}^{d}$ and $\mathcal{P}_{a c}\left(\mathbb{R}^{d}\right)$ the set of probability measures absolutely continuous with respect to the Lebesgue measure. Let $\mu \in \mathcal{P}\left(\mathbb{R}^{d}\right)$ and $\nu \in \mathcal{P}\left(\mathbb{R}^{d}\right)$. A measurable map $T: \mathbb{R}^{d} \rightarrow \mathbb{R}^{d}$ is said to push $\mu$ to $\nu$ if for any measurable set $A \subseteq Y, \mu\left(T^{-1}(A)\right)=\nu(A)$. This relation is frequently written as $\nu=T_{\#} \mu$ or $\nu=\mu \circ T^{-1}$. Let $\mathcal{T}(\mu, \nu)$ denote the class of all measurable functions $T$ such that $\nu=T_{\#} \mu$. Under the quadratic loss, Monge's optimal transport (MOT) seeks a member of $\mathcal{T}(\mu, \nu)$ that reaches the infimum:

$$
\inf _{T \in \mathcal{T}(\mu, \nu)}\left\{\int_{\mathbb{R}^{d}}\|x-T(x)\|^{2} \mu(x)\right\}
$$

If this infimum is achieved within $\mathcal{T}(\mu, \nu)$, then the minimizer is called an optimal transport map. However, the infimum may not be achievable within $\mathcal{T}(\mu, \nu)$ - indeed, $\mathcal{T}(\mu, \nu)$ can be an empty set in extreme cases. This limits the applicability of Monge's approach.

To address this limitation, Kantorovich (1948) introduced a relaxed version of Monge's problem by representing a transportation plan as a joint measure $\pi$ with marginals $\mu$ and $\nu$. Let $\Pi(\mu, \nu)$ be the set of joint probability measures on $\mathbb{R}^{d} \times \mathbb{R}^{d}$ with marginals $\mu$ and $\nu$. The Kantorovich's problem seeks a $\pi$ in $\Pi(\mu, \nu)$ to minimize the total cost, that is,

$$
W_{2}^{2}(\mu, \nu)=\inf _{\pi}\left\{\int_{\mathbb{R}^{d} \times \mathbb{R}^{d}}\|x-y\|^{2} d \pi(x, y): \pi \in \Pi(\mu, \nu)\right\}
$$

The square root of the minimum value of (4) is defined as the 2-Wasserstein distance, and a solution to (4) is called an optimal transport plan. The existence of the solution to (4) follows from Villani (2009, Theorem 4.1). Equivalently, we can express the square of the 2-Wasserstein distance as

$$
W_{2}^{2}(\mu, \nu)=\int\|x\|^{2} d \mu(x)+\int\|y\|^{2} d \nu-2 \min _{\varphi \in \mathcal{F}}\left\{\int \varphi d \mu+\int \varphi^{*} d \nu\right\}
$$

where $\mathcal{F}$ is the space of $L_{1}(\mu)$ convex function on $\mathbb{R}^{d}$, and $\varphi^{*}$ is the Legendre-Fenchel conjugate of $\varphi$, given by,

$$
\varphi^{*}(y)=\sup _{x \in \mathbb{R}^{d}}\{\langle x, y\rangle-\varphi(x)\}, y \in \mathbb{R}^{d}
$$

Thus, solving (4) is equivalent to solving the semi-dual problem

$$
\min _{\varphi \in \mathcal{F}} \int\left\{\varphi d \mu+\int \varphi^{*} d \nu\right\}
$$

The semi-dual problem (7) connects with the Monge problem (3) through Brenier's Theorem (Brenier, 1991), which establishes the existence, uniqueness, and intrinsic structure of the optimal transport map. McCann (1995) extended this result to relax the second-order moment assumptions.

Proposition 1 (Brenier's Theorem). Let $\mu$ and $\nu$ be two distributions on $\mathbb{R}^{d}$.

(1) If $\mu$ is absolutely continuous with respect to the Lebesgue measure on $\mathbb{R}^{d}$, with support contained in a convex set $U$, then there exists a convex function $\varphi: U \rightarrow \mathbb{R} \cup\{+\infty\}$ such that $(\nabla \varphi)_{\# \mu}=\nu$. The function $\nabla \varphi$ is unique $\mu$-almost everywhere.

(2) If, in addition, $\nu$ is absolutely continuous on $\mathbb{R}^{d}$ with support contained in a convex set $V$, then there exists a convex function $\varphi^{*}: V \rightarrow \mathbb{R} \cup\{+\infty\}$ such that $\left(\nabla \varphi^{*}\right)_{\#} \nu=\mu$. The
function $\nabla \varphi^{*}$ is unique $\nu$-almost everywhere and equal to $(\nabla \varphi)^{-1} \mu$-almost everywhere. That means, for almost every $x, y \in U \times V$,

$$
\left(\nabla \varphi^{*} \circ \nabla \varphi\right)(x)=x, \quad\left(\nabla \varphi \circ \nabla \varphi^{*}\right)(y)=y
$$

Proposition 1 implies that a unique transport map with the form $\nabla \varphi$ exists between any absolutely continuous distributions. We refer to such a convex function $\varphi$ as the Brenier potential.

On the real line $\mathbb{R}$, the gradients of convex functions are non-decreasing functions. When $d \geq 2$, Rockafellar (1966) showed that the set of gradients of convex functions coincides with the set of cyclically monotonic functions defined below, which can be treated as a generalization of monotonicity to functions with more than one variables.

DEFINITION 1. Let $U$ be a nonempty subset of $\mathbb{R}^{d}$. A function $f$ is called cyclically monotone if, for every set of points $x_{1}, \ldots, x_{n+1} \in U$ with $x_{n+1}=x_{1}$, it holds that

$$
\sum_{k=1}^{n}\left\langle x_{k+1}, f\left(x_{k+1}\right)-f\left(x_{k}\right)\right\rangle \geq 0
$$

Equivalently,

$$
\sum_{k=1}^{n}\left\langle x_{k}, f\left(x_{k}\right)\right\rangle \geq \sum_{k=1}^{n}\left\langle x_{k}, f\left(x_{\sigma(k)}\right)\right\rangle
$$

for any permutation $\sigma$ of $\{1,2, \ldots, n\}$.

As a special case, the linear function $f(x)=A x$, where $A \in \mathbb{R}^{d \times d}$, is cyclically monotone if $A$ is symmetric and positive definite. When $d=1$, the definition above is equivalent to the usual notion of monotonicity.

## 3 Cyclically Monotone Copula Gaussian Graphical Model

The structure of the multi-attribute graphical model leads us to propose a flexible semiparametric model for non-Gaussian data. As we have observed, non-Gaussianity may occur in node vectors of $X$ instead of occurring in the coordinates of $X$. Correspondingly, we let the transformations act jointly on the node vectors instead of coordinate-wise as in the classical copula transformation.

We define the Cyclically Monotone Copula Gaussian (CMCG) distribution as follows. Let $X=\left(X_{1}^{\top}, X_{2}^{\top}, \ldots, X_{p}^{\top}\right)^{\top}$ where, for $j=1, \ldots, p, X_{j}=\left(X_{j 1}, \ldots, X_{j d}\right)$ is a random vector in $\mathbb{R}^{d}$.

DEFINITION 2. We say $X$ follows a cyclically monotone copula Gaussian (CMCG) distribution if there exist cyclically monotone functions $\left\{T_{j}: \mathbb{R}^{d} \rightarrow \mathbb{R}^{d}\right\}_{j=1}^{p}$, such that $\left(T_{1}\left(X_{1}\right)^{\top}\right.$, $\left.\ldots, T_{p}\left(X_{p}\right)^{\top}\right)^{\top} \sim N(0, \Sigma)$, where $\Sigma$ has structure (2) with $\Sigma_{j j}=I_{d}$.

Let $T=\left(T_{1}, \ldots, T_{p}\right)$. We denote a random vector following CMCG distribution as $X \sim \operatorname{CMCG}(T, \Sigma)$. The CMCG family covers the copula Gaussian distribution family in Liu et al. (2009) because the tensor product of univariate monotone functions is indeed a cyclically monotone function, as shown in the next proposition. In the following, for functions $g_{1}: \mathbb{R} \rightarrow \mathbb{R}, \ldots, g_{d}: \mathbb{R} \rightarrow \mathbb{R}$, let $g_{1} \otimes \cdots \otimes g_{d}$ denote the function from $\mathbb{R}^{d} \rightarrow \mathbb{R}^{d}$ such that $\left(g \otimes \cdots \otimes g_{d}\right)\left(u_{1}, \ldots, u_{d}\right)=\left(g_{1}\left(u_{1}\right), \ldots, g_{d}\left(u_{d}\right)\right)^{\top}$.

PROPOSITION 2. If there exist monotone non-decreasing univariate functions $\left\{f_{j s}: s=1\right.$, $\ldots d, j=1, \ldots, p\}$ such that $\left(f_{11}\left(X_{11}\right), \ldots, f_{p d}\left(X_{p d}\right)\right) \sim N(0, \Sigma)$, then $X \sim \operatorname{CMCG}(T, \Sigma)$, where $T=\left(T_{1}, \ldots, T_{p}\right)$ and $T_{j}=f_{j 1} \otimes \cdots \otimes f_{j d}$ for $j=1, \ldots, p$.

For $j=1, \ldots, p$, let $P_{j}$ be the distribution of $X_{j}$. We assume $P_{j}$ to be absolutely continuous on $\mathbb{R}^{d}$. Then, by Brenier's theorem, there exists a unique cyclically monotone function $T_{j}$ such that $T_{j}\left(X_{j}\right) \sim N\left(0, I_{d}\right)$. In other words, the CMCG family allows the multi-dimensional marginal distributions to be any absolutely continuous distributions. As a comparison, the copula Gaussian model requires the multi-dimensional marginal distribution to be copula Gaussian.

Let $X \sim \operatorname{CMCG}(T, \Sigma)$. Suppose the precision matrix $\Theta=\Sigma^{-1}$ has the same block structure as (2). We say $X$ follows a Cyclically Monotone Copula Gaussian Graphical Model (CMC-GGM) $\mathcal{G}(V, E)$ if (1) holds.

The joint cumulative distribution function of $X$ is given by:

$$
F\left(x_{1}, \ldots, x_{p}\right)=\Phi_{\Sigma}\left(T_{1}\left(x_{1}\right), \ldots, T_{p}\left(x_{p}\right)\right)
$$

where $\Phi_{\Sigma}$ is the multivariate normal cumulative distribution function with mean zero and covariance matrix $\Sigma$. If $\left\{T_{j}\right\}_{j=1}^{p}$ are differentiable, the joint probability density function of $X$ is given by:

$$
p_{X}(x)=\frac{1}{(2 \pi)^{p / 2}|\Sigma|^{1 / 2}} \exp \left\{-\frac{1}{2} T(x)^{\top} \Sigma^{-1} T(x)\right\} \prod_{j=1}^{p} \operatorname{det}\left(D_{T_{j}}\left(x_{j}\right)\right)
$$

where $D_{T_{j}}$ is the Jacobian matrix of $T_{j}$ for $j=1, \ldots, p$. This implies that the conditional independence $X_{j} \Perp X_{k} \mid X_{-(j, k)}$ can still be characterized by $\Theta_{j k}=0$, which implies that relation (1) is equivalent to

$$
\Theta_{j k}=0 \Leftrightarrow(j, k) \notin E
$$

In fact, any one-to-one transformations of the node vectors will preserve the original graph structure. However, a large class of transformations will make the model non-identifiable, prohibiting inference on the precision matrix. This is also noticed by Bryan et al. (2021) when designing semiparametric CCA models. The following proposition guarantees that the CMC-GGM is identifiable.

Proposition 3. If two random vectors $X \sim C M C G(T, \Sigma)$ and $\tilde{X} \sim C M C G(\tilde{T}, \tilde{\Sigma})$ have the same distribution, then $\Sigma=\tilde{\Sigma}$, and $T=\tilde{T}$ almost everywhere.

The CMC-GGM model extends the Copula-GGM model by assigning a multivariate normal score to each node vector. To construct rank-based estimators, we can solve optimal transport problems between the distribution of $X_{j}$ and the uniform distribution over the unit hypercube $[0,1]^{d}$. This is the same as the multivariate rank proposed in Ghosal and Sen (2022), Fan and Henry (2023), and among others. The c.d.f of $X$ is given by

$$
F\left(x_{1}, \ldots, x_{p}\right)=\Phi_{\Sigma}\left(\Phi^{-1}\left(R_{1}\left(x_{1}\right)\right)^{\top}, \ldots, \Phi^{-1}\left(R_{p}\left(x_{p}\right)^{\top}\right)\right.
$$

where $\Phi_{\Sigma}(\cdot)$ is the c.d.f of $N(0, \Sigma), \Phi^{-1}\left(x_{j}\right)=\left(\Phi^{-1}\left(x_{j 1}\right), \ldots, \Phi^{-1}\left(x_{j d}\right)\right)^{\top}$, and $R_{j}(\cdot)$ is the optimal transport map between $P_{j}$ and $U\left([0,1]^{d}\right)$.

For a Gaussian graphical model with a single attribute, $R_{j}(\cdot)$ is the common distribution function, and $\Phi^{-1} \circ R_{j}$ is a monotonic non-decreasing function. Therefore, model (9) and CMC-GGM (8) are equivalent. However, this is not the case for the multi-attribute graphical model, as $\Phi^{-1} \circ R_{j}$ may not be a cyclically monotone function. In this paper, we focus on CMC-GGM because cyclically monotone functions offer the best transformations for preserving the relative information among data when transported to Gaussian. For further dicussions on Model (9), please see the Supplementary Material.

## 4 Estimation

The plug-in procedure provides a direct approach to estimating the CMC-GGM. This approach was also used Liu et al. (2009) for the Copula-GGM and Solea and Li (2022) for the
copula functional graphical model. In this paper, we develop a two-step plug-in procedure to estimate CMC-GGM: in step 1, we estimate the transformation $T$ nonparametrically by solving discrete-to-discrete optimal transport problems; in step 2, we use sparse estimation methods, including thresholding, group graphical lasso selection, and neighborhood vectoron-vector group lasso selection, to construct a sparse estimator of the blockwise precision matrix using transformed data.

### 4.1 Estimation of the CMC Transformation

Let $\mathcal{X}_{n}=\left\{X^{i}\right\}_{i=1}^{n}$ be i.i.d samples from $P_{X}$, where superscripts $i \in\{1, \ldots, n\}$ is the sample index and $X^{i}=\left\{X_{j}^{i}: j=1, \ldots, p\right\}$ where the subscript $j \in\{1, \ldots, p\}$ is subvector index. We estimate the cyclically monotone transformation $T_{j}$ between $P_{j}$, the distribution of $X_{j}^{i}$, and the $d$-dimensional standard Gaussian distribution $Q$ by solving the following discreteto-discrete OT problem. Let $\mathcal{Z}_{n}=\left\{Z^{1}, \ldots, Z^{n}\right\}$ be i.i.d samples drawn from $Q$. Define the empirical measures on $\mathcal{X}_{n}$ and $\mathcal{Z}_{n}$ as

$$
\hat{P}_{j}=\frac{1}{n} \sum_{i=1}^{n} \delta_{X_{j}^{i}}, \quad \hat{Q}=\frac{1}{n} \sum_{i=1}^{n} \delta_{Z^{i}}
$$

respectively. Solving the optimal transport problem between $\hat{P}_{j}$ and $\hat{Q}$ reduces to solving an assignment problem given by

$$
\hat{\sigma}_{j}=\operatorname{argmin}_{\sigma \in A_{n}} \sum_{i=1}^{n}\left\|X_{j}^{i}-Z^{\sigma(i)}\right\|^{2}
$$

where $A_{n}$ is the set of all permutations of $\{1,2, \ldots, n\}$. This is a combinatorial optimization problem and can be solved using the Hungarian algorithm (see, for example, Jonker and Volgenant (1988)) with the worst computational complexity $\mathcal{O}\left(n^{3}\right)$. The cyclically monotone transformation between $P_{j}$ and $Q$ is then estimated by $\hat{T}_{j}\left(X_{j}^{i}\right)=Z^{\sigma_{j}(i)}$ for $i=1, \ldots, n$.

To control the bias-variance trade-off in high-dimensional setting, we apply the Winsorization (or truncation) operator to the estimated transformation $\hat{T}_{j}$. Specifically, we define $\hat{T}_{j}^{(w)}\left(X_{j}\right)=\left(\hat{T}_{j 1}^{(w)}\left(X_{j 1}\right), \ldots, \hat{T}_{j d}^{(w)}\left(X_{j d}\right)\right)$, where

$$
\hat{T}_{j s}^{(w)}(x)=\hat{T}_{j s}(x) \mathbf{1}\left\{\left|\hat{T}_{j s}(x)\right| \leq \delta_{n}\right\}+\operatorname{sign}\left(\hat{T}_{j s}(x)\right) \delta_{n} \mathbf{1}\left\{\left|\hat{T}_{j s}(x)\right| \geq \delta_{n}\right\}
$$

is the 1-dimensional Winsorization operator with threshold $\delta_{n}$. In the classical copula graphical model, the winsorization operator is applied to the cumulative function $F(x)$, and the transformation is then estimated by $\Phi^{-1}\left(F^{(w)}(x)\right)$. For example, Klaassen and Wellner (1997)
consider using $\delta_{n}=n^{-1}$ and Liu et al. (2009) suggest using $\delta_{n}=\left(4 n^{1 / 4} \sqrt{\pi \log n}\right)^{-1}$. In (12), the winsorization operator is assigned to the transformed values of the estimated optimal transport map $\hat{T}$, which are samples from standard Gaussian. Therefore, we use the threshold $\delta_{n} \sqrt{2 \log n}$, which provides comparable thresholding effects as the copula Gaussian setting. This choice is justified by Abramovich et al. 2006, Lemma 12.3), which states that $\Phi^{-1}(1-1 / n) \leq \sqrt{2 \log n}$. This threshold enables us to derive the desired convergence rate in Section 5 .

We can also approximate the Gaussian distribution using the quasi-Monte Carlo methods (see Deb and Sen (2023) for more details). For example, we first take $\mathcal{C}_{n}=\left\{c_{1}, \ldots, c_{n}\right\}$ to be the $d$-dimensional Halton sequence of size $n$. The empirical distribution on $\mathcal{C}_{n}$ will be a discrete approximation of $U[0,1]^{d}$. Then the empirical distribution on $\left\{\Phi^{-1}\left(c_{i}\right), i=1\right.$, $\ldots, n\}$, where $\Phi^{-1}$ is applied coordinatewise, can be considered as a discrete approximation of $N\left(0, I_{d}\right)$. Since $\Phi^{-1}(\cdot)$ diverges very quickly when evaluated at a point close to 1 , we can also assign a Winsorization operator on the Halton sequence, resulting in the samples $\left\{Z^{i}=\Phi^{-1}\left(\left(c_{i}^{(w)}\right)\right)\right\}_{i=1}^{n}$. We do not find a significant difference between using quasi-Monte Carlo methods and the Monte Carlo method in simulation studies in Section 7.1.

### 4.2 Sparse Estimation of the Precision Matrix

In this subsection, we present methods for sparsely estimating the precision matrix using the estimated covariance matrix of the transformed data. Let $\hat{\Sigma}$ be the sample covariance matrices of the CMC-transformed data $\hat{T}^{(w)}(X)$ and $\hat{\Theta}$ be its inverse, with block structure

$$
\hat{\Sigma}=\left(\begin{array}{cccc}
\hat{\Sigma}_{11} & \hat{\Sigma}_{12} & \ldots & \hat{\Sigma}_{1 p} \\
\hat{\Sigma}_{21} & \hat{\Sigma}_{22} & \ldots & \hat{\Sigma}_{2 p} \\
\vdots & \vdots & \ddots & \vdots \\
\hat{\Sigma}_{p 1} & \hat{\Sigma}_{p 2} & \cdots & \hat{\Sigma}_{p p}
\end{array}\right) \text { and } \hat{\Theta}=\left(\begin{array}{cccc}
\hat{\Theta}_{11} & \hat{\Theta}_{12} & \ldots & \hat{\Theta}_{1 p} \\
\hat{\Theta}_{21} & \hat{\Theta}_{22} & \ldots & \hat{\Theta}_{2 p} \\
\vdots & \vdots & \ddots & \vdots \\
\hat{\Theta}_{p 1} & \hat{\Theta}_{p 2} & \cdots & \hat{\Theta}_{p p}
\end{array}\right)
$$

Here, the $(j, k)$-th block is

$$
\hat{\Sigma}_{j k}=E_{n}\left[\hat{T}_{j}^{(w)}\left(X_{j}\right) \hat{T}_{k}^{(w)}\left(X_{k}\right)^{\top}\right]-E_{n}\left[\hat{T}_{j}^{(w)}\left(X_{j}\right)\right] E_{n}\left[\hat{T}_{k}^{(w)}\left(X_{k}\right)\right]
$$

where $E_{n}[\cdot]$ is the empirical mean. We propose three ways to estimate the graph sparsely.

Thresholding. We begin by computing the Tychonoff-regularized precision matrix as

$$
\hat{\Theta}^{(r)}=\left(\hat{\Sigma}+\eta I_{d p}\right)^{-1}
$$

where $\eta$ is a tuning parameter, and superscript $r$ indicates regularization. We then estimate the edge set $E$ by

$$
\hat{E}\left(\epsilon_{n}\right)=\left\{(j, k) \in V \times V:\left\|\hat{\Theta}_{j k}^{(r)}\right\|_{\mathrm{F}}>\epsilon_{n}\right\}
$$

where $\left\{\epsilon_{n}\right\}$ is a positive sequence with $\epsilon_{n} \downarrow 0$ and $\|\cdot\|_{\mathrm{F}}$ denotes the Frobenius norm. The thresholding estimator is direct and easy to implement but less accurate than penalized estimation methods in most settings.

Group glasso. This approach minimizes the penalized negative Gaussian loglikelihood:

$$
L_{n}: \mathbb{R}^{d p \times d p} \rightarrow \mathbb{R}, \Theta \rightarrow-\log \operatorname{det}(\Theta)+\operatorname{trace}(\Theta \hat{\Sigma})+\lambda_{n} \sum_{k \neq j}\left\|\Theta_{j k}\right\|_{\mathrm{F}}
$$

where $\lambda_{n}$ is a tuning parameter. The precision matrix $\Theta$ is then estimated by minimizing $L_{n}(\cdot)$ over the set of all positive semidefinite $d p \times d p$ matrix. Several efficient algorithms have been developed to minimize the penalized negative Gaussian loglikelihood with group penalty, such as Kolar et al. (2014) and Tugnait (2021), among others. We adopt the block coordinate descent algorithm in Qiao et al. (2019) to solve (14).

Neighborhood vector-on-vector group lasso selection. We perform vector-on-vector regression separately for each $j=1,2, \ldots, p$, using $\hat{T}_{j}\left(X_{j}\right)$ as the response and $p-1$ remaining subvectors in $\hat{T}(X)$ as predictors. Let $\varsigma$ be a mapping that reorganizes the indices such that $\{\varsigma(1), \ldots, \varsigma(p-1)\}=\{1, \ldots, p\} /\{j\}$. For simplicity, we write $Y=\hat{T}_{j}\left(X_{j}\right) \in \mathbb{R}^{d}$ and $\tilde{X}=\left(\tilde{X}_{1}, \ldots, \tilde{X}_{p-1}\right)=\left(\hat{T}_{\varsigma(1)}\left(X_{\varsigma(1)}\right), \ldots, \hat{T}_{\varsigma(p-1)}\left(X_{\varsigma(p-1)}\right)\right) \in \mathbb{R}^{d \times(p-1) d}$. Let $B=\left(B_{1}^{\top}, \ldots\right.$, $\left.B_{p-1}^{\top}\right)^{\top} \in \mathbb{R}^{d(p-1) \times d}$, where $B_{k} \in \mathbb{R}^{d \times d}$ for $k=1, \ldots, p-1$. Then the vector-on-vector regression model can be written as:

$$
Y=\sum_{k=1}^{p-1} \tilde{X}_{k} B_{k}+\varepsilon=\tilde{X} B+\varepsilon
$$

where $\varepsilon \in \mathbb{R}^{d}$ is an error vector with mean 0 and is independent of $\tilde{X}$. After vectorization, (15) can be written as

$$
\operatorname{vec}(Y)=\left(I_{d} \otimes \tilde{X}\right) \cdot \operatorname{vec}(B)+\operatorname{vec}(\varepsilon)
$$

where $\operatorname{vec}(\cdot)$ vectorizes an $d \times d$ matrix by stacking the columns of the matrix into a $d^{2} \times 1$ vector and $\otimes$ is the Kronecker product. We then estimate regression parameters by minimizing the squared residuals with group lasso penalty, given by:

$$
\hat{B}=\underset{B \in \mathbb{R}^{d(p-1) \times d}}{\operatorname{argmin}}\left\{\frac{1}{2 n} \sum_{i=1}^{n}\left\|\operatorname{vec}\left(Y^{i}\right)-\left(I_{d} \otimes \tilde{X}^{i}\right) \operatorname{vec}(B)\right\|^{2}+\lambda_{n} \sum_{j=1}^{p-1}\left\|\operatorname{vec}\left(B_{k}\right)\right\|_{2}\right\}
$$

where $\lambda_{n}$ is a tuning parameter. We estimate the support set for node $j$ as:

$$
\hat{\mathcal{N}}_{j}=\left\{\sigma(k): k=1, \ldots, p-1,\left\|\hat{B}_{k}\right\|>0\right\}
$$

After estimating the neighborhood for each node, we construct an estimated edge set $\hat{E}$ by aggregating $\left\{\hat{\mathcal{N}}_{j}\right\}_{j=1}^{p}$ via intersection or union. We use the Groupwise Majorization Descent (GMD) algorithm in Yang and Zou (2015) to solve (17).

Selection of tuning parameters. All methods above require choosing tuning parameters to control the sparsity of the estimated graph. The sparsity level can be controlled by $\epsilon_{n}$ for thresholding, and by $\lambda_{n}$ for glasso and neighborhood selection. Common approaches for tuning parameter selection include the Akaike information criterion (AIC), Bayesian information criterion (BIC), cross-validation, and stability selection (Meinshausen and Bühlmann, 2010). In the synthetic data experiments, to ensure a fairer comparison among different methods, we fit each method over a range of tuning parameters and generate ROC curves. We then compute the associated area-under-curve (AUC) values. For the data applications, we suggest using the BIC to select tuning parameters for the group glasso method, which takes the following form:

$$
\operatorname{BIC}\left(\lambda_{n}\right)=\operatorname{trace}(\hat{\Sigma} \hat{\Theta})-\log |\hat{\Theta}|+\frac{\log (n)}{n} m^{2}\left(\frac{1}{2} \sum_{j \neq k} 1\left\{\hat{\Theta}_{j k} \neq 0\right\}+p\right)
$$

However, when the sample size is small, BIC may not lead to a reasonable graph. To address this issue, we suggest a method similar to the stability selection Meinshausen and Bühlmann, 2010). First, we fit a relatively dense graph with the sparsity chosen by cross-validation or domain knowledge. Next, we refit the model using bootstrap samples 50 times and select the stable edges that appeared in at least $90 \%$ of the replications.

## 5 Consistency and Convergence Rate

In this section, we establish the consistency and convergence rate for the estimator of the CMC-GGM. Recall that each $X_{j}$ in $X$ is distributed as $P_{j}$, which is dominated by the Lebesgue measure in $\mathbb{R}^{d}$. Let $Q=N\left(0, I_{d}\right)$. By Brenier's theorem, for each $j=1, \ldots, p$, there exists a convex potential function $\varphi_{j}$ such that the optimal transport map $T_{j}$ between $P_{j}$ and $Q$ can be written as $T_{j}=\nabla \varphi_{j}$. Let $\varphi_{j}^{*}$ be the Legendre-Fenchel dual of $\varphi_{j}$, as defined in (6). Then, $\nabla \varphi_{j}^{*}$ is the optimal transport map transporting $Q$ to $P_{j}$. Let $\hat{P}_{j}$ and $\hat{Q}$ be the empirical measures defined in (10). Let $\hat{T}_{j}$ be the estimates obtained from (11).

Several recent works, such as Deb and Sen (2023) and Hallin et al. (2021), focus on establishing the convergence rate of the discrete-to-discrete estimator of the optimal transport map. In our model, both the source and target distributions can have unbounded supports, where the results in Manole et al. (2021) and Deb and Sen (2023) cannot be directly applied. Similar to Manole et al. (2021), we introduce the following regularity condition on the Brenier potential functions $\left\{\varphi_{j}\right\}_{j=1}^{p}$ to give a stability bound of the estimated transformations. For $j=1, \ldots, p$, we assume

(A1) $\nabla \varphi_{j}$ is Lipschitz continuous with Lipschitz constant $\rho$;

(A2) $\varphi_{j}$ is strongly convex with parameter $1 / \rho$.

Assumptions (A1) and (A2) guarantee that for any two points $x, y \in \mathbb{R}^{d}$,

$$
\frac{1}{\rho}\|x-y\|^{2} \leq\left\langle\nabla \varphi_{j}(x)-\nabla \varphi_{j}(y), x-y\right\rangle \leq \rho\|x-y\|^{2}
$$

Remark 1. By Hiriart-Urruty and Lemaréchal (2004, Theorem 4.2.1, 4.2.2), the LegendreFenchel dual $\varphi_{j}^{*}(\cdot)$ is strongly convex with parameter $1 / \rho$ if and only if $\nabla \varphi_{j}(\cdot)$ is $\rho$-Lipschitz continuous. Therefore, assumption (A2) is equivalent to $\nabla \varphi_{j}^{*}$ being $\rho$-Lipschitz.

REMARK 2. We note that assumption (A1) implies (A2) when both source and target distributions are defined in a compact set and have densities that are bounded above and below. However, when the support of $P_{j}$ and $Q$ are unbounded, assumption (A2) becomes more restrictive. Nevertheless, under certain regularity conditions on the source distribution $P_{j}$, we can still guarantee (A2). For example, according to Caffarelli contraction theorem (Caffarelli, 2000), if $P_{j}$ is a uniformly log-concave measure of the form $e^{-V} d x$, where $V$ has Hessian matrix $\geq \alpha I_{d}$, then $\nabla \varphi_{j}^{*}$ is $\alpha^{-1 / 2}$-Lipschitz and hence $\varphi_{j}$ is $\alpha^{-1 / 2}$-strongly convex. For further extensions, see Colombo and Fathi (2021) and Manole and Niles-Weed (2021).

We first establish the following stability bound. A similar result for the semi-discrete OT setting is derived in Manole et al. (2021, Theorem 6) and Deb et al. (2021, Theorem 2.1).

LEMMA 1. Suppose assumption (A1) holds with constant $\rho>0$, then, for $j=1, \ldots, p$, we have

$$
\frac{1}{n} \sum_{i=1}^{n}\left\|\hat{T}_{j}\left(X_{j}^{i}\right)-T_{j}\left(X_{j}^{i}\right)\right\|^{2} \leq \rho\left\{W_{2}^{2}\left(\hat{P}_{j}, \hat{Q}\right)-W_{2}^{2}\left(\hat{P}_{j}, \bar{Q}_{j}\right)-\int g_{j} d\left(\hat{Q}-\bar{Q}_{j}\right)\right\}
$$

where $g_{j}(\cdot)=\|\cdot\|^{2}-2 \varphi_{j}^{*}(\cdot)$ and $\bar{Q}_{j}=\left(\nabla \varphi_{j}\right)_{\#}\left(\hat{P}_{j}\right)$. If, in addition, assumption (A2) holds, then

$$
\frac{1}{\rho^{2}} W_{2}^{2}\left(\hat{Q}, \bar{Q}_{j}\right) \leq \frac{1}{n} \sum_{i=1}^{n}\left\|\hat{T}_{j}\left(X_{j}^{i}\right)-T_{j}\left(X_{j}^{i}\right)\right\|^{2} \leq \rho^{2} W_{2}^{2}\left(\hat{Q}, \bar{Q}_{j}\right)
$$

Based on the stability bounds in Lemma 1, we establish a 0-concentration inequality for $\left\|\hat{T}_{j}-T_{j}\right\|_{L_{1}\left(\hat{P}_{j}\right)}$ in Lemma 2. Since we use Monte Carlo methods to generate discrete samples from $Q$, both the randomness of $X$ and $Z$ are considered in the concentration inequality. Throughout the following, we use $C$ to denote general constants independent of $n$ and $p$ but may change from one place to another. Let $\zeta_{d}=1 / 2$ if $d=4$ and 0 otherwise.

LEMMA 2. Under assumptions (A1) and (A2), for $j=1, \ldots, p$, we have

$$
\mathbb{P}\left(\frac{1}{n} \sum_{i=1}^{n}\left\|\hat{T}_{j}\left(X_{j}^{i}\right)-T_{j}\left(X_{j}^{i}\right)\right\| \geq \varepsilon\right) \leq \exp \left\{-C n\left[\left(\varepsilon-C n^{-\frac{1}{4 \vee d}}(\log n)^{\zeta_{d}}\right)_{+}\right]^{2}\right\}
$$

where $a_{+}=a I\{a>0\}$.

Let $T_{j}^{(w)}(x)$ and $\hat{T}_{j}^{(w)}(x)$ be the winsorized versions of $T_{j}(x)$ and $\hat{T}^{(w)}(x)$, respectively, with a threshold of $\sqrt{2 \log n}$. The concentration inequality in Lemma 2 applies to $\hat{T}^{(w)}$ and $T^{(w)}$ by the observation that $\left\|\hat{T}_{j}\left(X_{j}^{i}\right)-T\left(X_{j}^{i}\right)\right\| \geq\left\|\hat{T}_{j}^{(w)}\left(X_{j}^{i}\right)-T^{(w)}\left(X_{j}^{i}\right)\right\|$ for any $1 \leq i \leq n$.

COROLLARY 1. Under assumptions (A1) and (A2), for $j=1, \ldots, p$, we have

$$
\mathbb{P}\left(\frac{1}{n} \sum_{i=1}^{n}\left\|\hat{T}_{j}^{(w)}\left(X_{j}^{i}\right)-T^{(w)}\left(X_{j}^{i}\right)\right\| \geq \varepsilon\right) \leq \exp \left\{-C n\left[\left(\varepsilon-C n^{-\frac{1}{4 \vee d}}(\log n)^{\zeta_{d}}\right)_{+}\right]^{2}\right\}
$$

We now show that the estimator $\hat{\Sigma}$ converges to $\Sigma$ blockwise when $p$ grows at an exponential rate of $n$. Recall that $\hat{\Sigma}$ is an estimator after the winsorization.

THEOREM 1. For any $\varepsilon>0$, there exists a constant $C>0$ such that

$$
\mathbb{P}\left(\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}} \geq \varepsilon\right) \leq C \exp \left\{-C \frac{n}{d \log ^{2} n}\left[\left(\varepsilon-C n^{-\frac{1}{4 V d}}(\log n)^{\zeta_{d}+\frac{1}{2}}\right)_{+}\right]^{2}\right\}
$$

and consequently,

$$
\mathbb{P}\left(\max _{1 \leq j, k \leq p}\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}} \geq \varepsilon\right) \leq C p^{2} \exp \left\{-C \frac{n}{d \log ^{2} n}\left[\left(\varepsilon-C n^{-\frac{1}{4 \vee d}}(\log n)^{\zeta_{d}+\frac{1}{2}}\right)_{+}\right]^{2}\right\}
$$

The proof of Theorem 1 can be found in the Supplemental Material. As can be seen from the proof, the tail bound of the mean concentration of $\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}$ has an order of $\log n / \sqrt{n}$, that is, $\left(\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}-\mathbb{E}\left[\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}\right]\right)=O_{p}(\log n / \sqrt{n})$. However, this rate is dominated by the convergence rate of the mean $\mathbb{E}\left[\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}\right]$, which has an order of $(\log n)^{\zeta_{d}+\frac{1}{2}} /\left(n \frac{1}{4 \mathrm{vd}}\right)$. We compare Theorem 1 with the convergence rate of the Copula-GGM. For example, see Mai et al. (2023, Theorem 3) for the convergence rate of the normal score estimator and winsorization estimator of the Copula-GGM. We see that the Winsorization estimator $\hat{\Sigma}$
of CMC-GGM has the same rate of tail bound as the Copula-GGM, but a slower rate of mean convergence, which is also of order $\log n / \sqrt{n}$ for Copula-GGM. This slower rate of mean convergence is due to the curse of dimensionality issue that arises when solving $d$-dimensional OT problems. Furthermore, when $\log p=o\left(n / \log ^{2} n\right)$, we have $\max _{1 \leq j, k \leq p}\left\|\hat{\Sigma}_{j k}-\Sigma_{j k}\right\|_{\mathrm{F}}=$ $O_{p}\left((\log n)^{\zeta_{d}+\frac{1}{2}} /\left(n \frac{1}{4 \mathrm{v} d}\right)\right)=o_{p}(1)$. This indicates that the dimension limit can be at $\log p=$ $O\left(n^{\tau}\right)$ with $0<\tau<1$.

To further establish the consistency of the group glasso estimator (14) for graph estimation, we introduce a group version of the irrepresentable condition, which is also used in Kolar et al. (2014) and Qiao et al. (2019), as an extension of the irrepresentable condition in Ravikumar et al. (2011). Let $A=\left(A_{j k}\right)_{j, k=1}^{p}$ be an $\mathbb{R}^{p d \times p d}$ block matrix, where $A_{j k} \in$ $\mathbb{R}^{d \times d}$ for $j, k=1, \ldots, p$. We define the blockwise norms $\|A\|_{\infty}^{(d)}=\max _{1 \leq j \leq p} \sum_{k=1}^{p}\left\|A_{j k}\right\|_{\mathrm{F}}$, $\|A\|_{\max }^{(d)}=\max _{1 \leq j, k \leq p}\left\|A_{j k}\right\|_{\mathrm{F}}$, regarding them as the block versions of matrix $\ell_{\infty}$-norm and maximum norm, respectively. The superscript $(d)$ indicates the length of the block. Let $\tilde{E}=E \cup\{(1,1), \ldots,(p, p)\}$ be the augmented edge set and $\tilde{E}^{c}$ be its complement. Let $H=\Theta^{-1} \otimes \Theta^{-1} \in \mathbb{R}^{(p d)^{2} \times(p d)^{2}}$, where $\otimes$ is the Kronecker product. The matrix $H$ is the Hessian operator of the loglikelihood function evaluated at the true $\Theta$. For index set $J$, $J^{\prime} \subseteq\{1, \ldots, p\}$, let $H_{J J^{\prime}} \in \mathbb{R}^{d^{2}|J| \times d^{2}\left|J^{\prime}\right|}$ be the submatrix of $H$ with row and column blocks in $J$ and $J^{\prime}$. We assume that the following irrepresentable-type condition holds.

(A3) There exists a constant $0 \leq \alpha<1$ such that

$$
\left\|H_{\tilde{E}^{c} \tilde{E}}\left(H_{\tilde{E} \tilde{E}}\right)^{-1}\right\|_{\infty}^{\left(d^{2}\right)} \leq 1-\alpha
$$

Let $\kappa_{\Sigma}=\|\Sigma\|_{\infty}^{(d)}$ and $\kappa_{H}=\left\|H^{-1}\right\|_{\infty}^{\left(d^{2}\right)}$. Let $s$ be the maximal degree of nodes in $\mathcal{G}$. Define the following quantities:

$$
\delta_{1}(n)=\frac{s \sqrt{d \log p} \log n}{\sqrt{n}}, \text { and } \delta_{2}(n)=\frac{(\log n)^{\zeta_{d}+\frac{1}{2}}}{n^{\frac{1}{4 \vee d}}}
$$

Under conditions (A1), (A2), and (A3), we have the selection consistency of the CMC-GGM in the following theorem.

THEOREM 2. Let $\lambda_{n} \asymp \delta_{1}(n) \wedge \delta_{2}(n)$. Then, as $\delta_{1}(n) \wedge \delta_{2}(n) \rightarrow 0,\|\hat{\Theta}-\Theta\|_{\max }^{(d)}=o_{p}(1)$. Consequently, the estimated graph $\hat{G}$ agrees with the true graph $G$ with high probability, that is, $\mathbb{P}(\hat{G}=G) \rightarrow 1$.

In Theorem 2, we see that $\delta_{1}(n)$ corresponds to the tail bound while $\delta_{2}(n)$ corresponds to the mean error bound. When $\log p \prec n^{\left(1-\frac{2}{4 v d}\right)}(\log n)^{\left(2 \zeta_{d}-1\right)}, \delta_{1}(n) \prec \delta_{2}(n)$, indicating that
the mean error bound dominates the tail error bound. When $\log p \succ n^{\left(1-\frac{2}{4 v d}\right)}(\log n)^{\left(2 \zeta_{d}-1\right)}$, $\delta_{1}(n) \succ \delta_{2}(n)$, indicating that the tail error bound dominates the mean error bound, and the convergence rate is the same as copula Gaussian model in Mai et al. (2023, Theorem 4). The theorem also indicates that the dimension limit can be at $\operatorname{most} \log p=O\left(n / \log ^{2} n\right)$.

The selection consistency using CMC transformed score can also be established with neighborhood group lasso selector, following the proof in, for example, Zhao et al. (2021). We skip this part due to space limitation.

## 6 Projected Cyclically Monotone Copula for High Dimensional Attributes

### 6.1 Projected Cyclically Monotone Copula

In Section 3.1, we show that estimating the CM transformations $\left\{T_{j}\right\}_{j=1}^{p}$ involves solving discrete-to-discrete OT problems. However, this estimation method suffers from curse of dimensionality. In fact, the minimax convergence rate of the estimated OT map between $d$-dimensional discrete measures is $O\left(n^{-1 / d}\right)$ Niles-Weed and Rigollet, 2022; Fournier and Guillin, 2015). Theorems 1 and 2 also indicate that the convergence rate of graph estimation is limited by the dimension of vectors on each node. However, when the dimension of the vector is high, it is reasonable to assume the non-Gaussianity only appears on a $r$ dimensional subspace, where $r<d$. Once the $r$-dimensional subspace is properly estimated, the convergence rate can be improved from $O\left(n^{-1 / d}\right)$ to $O\left(n^{-1 / r}\right)$. To achieve this, we adopt the idea in projection robust OT method (Paty and Cuturi, 2019) to develop a projected cyclically monotone copula model that improves the estimation accuracy.

For $j=1, \ldots, p$, we assume that there exists an orthogonal matrix $\Gamma_{j}=\left(U_{j}, V_{j}\right) \in \mathbb{R}^{d \times d}$, where $U_{j} \in \mathbb{R}^{d \times r}$ and $V_{j} \in \mathbb{R}^{d \times(d-r)}$, such that $P_{j}$ and $Q$ only differ on an $r$-dimensional subspace spanned by $U_{j}$. Let $Z \sim N\left(0, I_{d}\right)$. By Brenier's Theorem, the optimal transport between $\Gamma^{\top} X_{j}$ and $\Gamma^{\top} Z$ can be written as $\left(T_{j}, \mathrm{id}_{\mathbb{R}^{d-r}}\right)$, where $T_{j}: \mathbb{R}^{r} \rightarrow \mathbb{R}^{r}$ is the optimal transport from $U^{\top} X_{j}$ to $U^{\top} Z$. Thus, the induced transformation $S_{j}$ from $X_{j}$ to $Z$ can be written as

$$
S_{j}:=\Gamma \circ\left(T_{j}, \mathrm{id}_{\mathbb{R}^{d-r}}\right) \circ \Gamma^{\top}=U_{j} \circ T_{j} \circ U_{j}^{\top}+V_{j} V_{j}^{\top}
$$

We now define the Projected Cyclically Monotone Copula Gaussian (PCMCG) family.

DEFINITION 3. $A$ random vector $X=\left(X_{1}^{\top}, X_{2}^{\top}, \ldots, X_{p}^{\top}\right)^{\top} \in \mathbb{R}^{d p}$ with subvector $X_{j} \in \mathbb{R}^{d}$, follows a projected cyclically monotone copula Gaussian (PCMCG) distribution if there exist cyclically monotone functions $T=\left\{T_{j}: \mathbb{R}^{r} \rightarrow \mathbb{R}^{r}\right\}_{j=1}^{p}$ and orthogonal matrices $\Gamma=\left\{\Gamma_{j} \in\right.$ $\left.\mathbb{R}^{d \times d}: \Gamma_{j}=\left(U_{j}, V_{j}\right), U_{j} \in \mathbb{R}^{d \times r}, V_{j} \in \mathbb{R}^{d \times(d-r)}, \Gamma_{j}^{\top} \Gamma_{j}=\Gamma_{j} \Gamma_{j}^{\top}=I_{d}\right\}_{j=1}^{p}$ such that $\left(S_{1}\left(X_{1}\right)^{\top}\right.$, $\left.\ldots, S_{p}\left(X_{p}\right)^{\top}\right)^{\top} \sim N(0, \Sigma)$, where $S_{j}=U_{j} \circ T_{j} \circ U_{j}^{\top}+V_{j} V_{j}^{\top}$ and $\Sigma$ has structure (2) with $\Sigma_{j j}=I_{d}$.

Let $Z=S_{j}\left(X_{j}\right)$. By the fact that $Z \sim N\left(0, I_{d}\right)$, we know that $U_{j}^{\top} Z$ and $V_{j}^{\top} Z$ are independent, implying that $U_{j}^{\top} X_{j}$ and $V_{j}^{\top} X_{j}$ are independent. Since $S_{j}, j=1, \ldots, p$ are cyclically monotone functions, they are unique optimal transport transformations from $P_{j}$ to $Q$ almost surely. Hence, the PCMCG family can be treated as a special case of the CMCG family in Definition 2 .

Let $\mathcal{S}_{j}$ be the space spanned by $U_{j}$ and $\mathcal{S}_{j}^{\perp}$ be its orthogonal complement spanned by $V_{j}$. Denote by $P_{\mathcal{S}_{j}}=U_{j} U_{j}^{\top}$ the projection matrix onto the space spanned by $U_{j}$. We note that for a different choice of bases $U_{j}$, the function $T_{j}$ may change, but the composition map $U_{j} \circ T_{j} \circ U_{j}^{\top}$ will be invariant. This is guaranteed because $U_{j} \circ T_{j} \circ U_{j}^{\top}$ is the optimal transport from the distribution of $P_{S_{j}} X_{j}$ to the distribution of $P_{S_{j}} Z$. Similarly, $S_{j}$ is invariant because $S_{j}$ is the optimal transports from $P_{j}$ to $Q$. By Brenier theorem, they are unique almost surely.

Define an equivalence relation $T \sim \tilde{T}$, if and only if there exists an orthogonal matrix $A \in \mathbb{R}^{r \times r}$ such that $T=A \circ \tilde{T} \circ A^{\top}$. Let $[T]$ be the equivalence class of $T$ over the set of cyclically monotone functions. We define the map $P_{\mathcal{S}}([T])=A \circ T \circ A^{\top}$ as the projected cyclically montone transformation of $[T]$ onto subspace $\mathcal{S}$, where $A$ is any basis matrix spanning $\mathcal{S} . P_{\mathcal{S}}([T])$ is well-defined because it is invariant for the choice of basis $A$ and representative element $[T]$. Therefore, the transportation map defined in Definition 3 can be written as

$$
S_{j}=P_{\mathcal{S}_{j}}\left(\left[T_{j}\right]\right)+P_{\mathcal{S}_{j}^{\perp}}
$$

where $\mathcal{S}_{j}$ is the space spanned by $U_{j}$ and $P_{\mathcal{S}_{j}^{\perp}}$ is the usual projection matrix on subspace $\mathcal{S}_{j}^{\perp}$. Let $S=\left(S_{1}, \ldots, S_{p}\right)$ and $\mathcal{S}=\left(\mathcal{S}_{1}, \ldots, \mathcal{S}_{p}\right)$. Therefore, for a random vector $X$ defined by Definition (3), we write $X \sim \operatorname{PCMCG}(\mathcal{S}, S, \Sigma)$.

Similarly, for a radnom vector $X \sim \operatorname{PCMCG}(\mathcal{S}, S, \Sigma)$, we say it follows a CCMC-GGM with graph $\mathcal{G}=(V, E)$ when $\Theta_{j k}=0$ is equivalent to $(j, k) \notin E$. The following proposition guarantees that the PCMC-GGM is identifiable.

Proposition 4. If two random vectors $X \sim \operatorname{PCMCG}(\mathcal{S}, S, \Sigma)$ and $\tilde{X} \sim \operatorname{PCMCG}(\tilde{\mathcal{S}}, \tilde{S}, \tilde{\Sigma})$ have the same distribution, then $\mathcal{S}=\tilde{\mathcal{S}}, \Sigma=\tilde{\Sigma}$, and $S=\tilde{S}$ almost everywhere.

### 6.2 Estimation

Define $U^{*}: \mathbb{R}^{d} \rightarrow \mathbb{R}^{k}$ to be the linear transformation associated with $U$ by $U^{*}(x)=U^{\top} x$. To estimate the non-Gaussianity subspace $\mathcal{S}_{j}$, we consider the worst possible optimal transport cost over all possible $r$-dimensional subspace, that is,

$$
U_{j}=\operatorname{argmax}_{U \in \operatorname{St}(d, r)} W_{2}\left(U_{\#}^{*} P_{j}, U_{\#}^{*} Q\right)
$$

where $\operatorname{St}(d, r):=\left\{U \in \mathbb{R}^{d \times r}: U^{\top} U=I_{r}\right\}$ denotes the Stiefel manifold. At the sample level, we solve the max-min optimization problem

$$
\max _{U \in \mathrm{St}(d, r)} \min _{\pi \in \Pi} \sum_{s=1}^{n} \sum_{t=1}^{n} \pi_{s, t}\left\|U^{\top} X_{j}^{s}-U^{\top} Z^{t}\right\|^{2}
$$

where $\Pi:=\left\{\pi \in \mathbb{R}_{+}^{n \times n}: \pi 1_{n}=1_{n}, \pi^{\top} 1_{n}=1_{n}\right\}$ denotes the transportation polytope. Here, we take the Kontorovich formulation of the OT problem for computing efficiency. We denote the solution of (22) as $\hat{U}_{j}$ and $\hat{\pi}_{j}$. The optimal transport plan $\pi$ indeed defines an optimal transport map in the sense that

$$
\pi_{s t}=I\left\{t=\sigma_{j}(s)\right\} / n, \quad \text { for all } 1 \leq s, t \leq n
$$

where $\sigma_{j}(\cdot)$ is a permutation of $\{1, \ldots, n\}$. Define $\hat{T}_{j}\left(\hat{U}_{j} X_{j}^{i}\right)=\hat{U}_{j} Z^{\sigma_{j}(i)}, i=1, \ldots, n$. The final transformations are then estimated by:

$$
\hat{S}_{j}\left(X_{j}^{i}\right)=\hat{U}_{j} \hat{T}_{j}\left(\hat{U}_{j}^{\top} X_{j}^{i}\right)+\hat{V}_{j} \hat{V}_{j}^{\top} X_{j}^{i}, \quad \text { for } i=1, \ldots, n, j=1, \ldots, p
$$

Define $\hat{P}_{j}$ and $\hat{Q}$ same as in 10). Let $P_{j, \hat{U}_{j}}$ and $Q_{\hat{U}_{j}}$ be the distribution of $\hat{U}_{j}^{\top} X_{j}$ and $\hat{U}_{j}^{\top} Z$, respectively. Similarly, define the empirical measures as:

$$
\hat{P}_{j, \hat{U}_{j}}=\frac{1}{n} \sum_{i=1}^{n} \delta_{\hat{U}_{j}^{\top} X_{j}^{i}}, \quad \hat{Q}_{\hat{U}_{j}}=\frac{1}{n} \sum_{i=1}^{n} \delta_{\hat{U}_{j}^{\top} Z^{i}}
$$

Then $\hat{T}_{j}$ is the optimal transport from $\hat{P}_{j, \hat{U}_{j}}$ to $\hat{Q}_{\hat{U}_{j}}$. We note that $\hat{S}$ defined in (23) does not transform $\hat{P}_{j}$ to $\hat{Q}$. Instead, $\hat{S}$ is the optimal transport from $\hat{P}$ to $\hat{Q}^{*}$, where

$$
\hat{Q}^{*}=\frac{1}{n} \sum_{i=1}^{n} \delta_{\hat{U}_{j} \hat{U}_{j}^{\top} Z^{\sigma_{j}(i)}+\hat{V}_{j} \hat{V}_{j}^{\top} X^{i}}
$$

In practice, we first estimate the projection matrix $U_{j}$ by solving (22) with entropy penalty to speed computation, that is,

$$
\max _{U \in \mathrm{St}(d, k)} \min _{\pi \in \Pi} \sum_{s=1}^{n} \sum_{t=1}^{n} \pi_{s, t}\left\|U^{\top} X_{j}^{s}-U^{\top} Z^{t}\right\|^{2}-\eta H(\pi)
$$

where $\eta>0$ is a tuning parameter and $H(\pi):=-\left\langle\pi, \log (\pi)-1_{n} 1_{n}^{\top}\right\rangle$. To solve (24), we adopt the Riemannian block coordinate descent (RBCD) algorithm proposed in Huang et al. (2021). To avoid the bias of estimating $\pi$ due to the entropy penalty, we only obtain $\hat{U}_{j}, j=1, \ldots, p$ from 24) and then solve an exact OT problem using the projected data in a follow-up step.

### 6.3 Convergence Rate

We next develop the convergence rate of the PCMCG model for $r=1$, where there exists one principal non-Gaussian direction. For $j=1, \ldots, p$, we assume that $P_{j, U_{j}}$ is absolutely continuous to the Lebesgue measure, and thus, there exists a convex potential function $\psi_{j}$, such that $T_{j}=\nabla \psi_{j}$ is the optimal transport from $P_{j, U_{j}}$ to $Q_{U_{j}}$. Let $\psi_{j}^{*}$ be the LegendreFenchel dual of $\psi_{j}$, defined in (6). To ensure the consistency of estimating the projected subspace $U_{j}$, we introduce two additional regularity conditions. First, we introduce the $\log$ Sobolev inequality to characterize the tail behavior of $X$ as follows:

DEFINITION 4. A probability measure $\mu$ on $\mathbb{R}^{d}$ is said to satisfy a log Sobolev inequality with constant $\kappa^{2}$ if

$$
\int f^{2} \log f^{2} d \mu-\int f^{2} d \mu \log \left(\int f^{2} d \mu\right) \leq 2 \kappa^{2} \int\|\nabla f\|^{2} d \mu
$$

for all smooth function $f: \mathbb{R}^{d} \rightarrow \mathbb{R}$ such that the integration are finite.

The $\log$ Sobolev inequality holds for any strongly $\log$-concave measure on $\mathbb{R}^{d}$, that is, a measure of having density $e^{V(x)}$ and Hessian $\nabla^{2} V \succeq \alpha I_{d}(\alpha>0)$. The log Sobolev inequality indicates the following transport inequality:

$$
W_{2}^{2}(\nu, \mu) \leq \kappa^{2} \mathrm{KL}(\nu \mid \mu), \quad \text { for any } \nu \in \mathcal{P}\left(\mathbb{R}^{d}\right)
$$

where $\operatorname{KL}(\nu \mid \mu)$ is the Kullback-Leibler divergence. Please see Gozlan and Léonard (2010) for more details on transport inequalities. For $j=1, \ldots, p$, we assume the following regularity conditions:

(A3) $P_{j}$ satisfies the $\log$ Sobolev inequality with constant $\kappa^{2}$;

(A4) There exists $\tau>0$ such that $W_{2}\left(P_{j}, Q\right)>\tau$.

Assumption (A4) requires the non-Gaussianity signal to be significant. We then establish a 0 -concentration inequality for $\left\|\hat{S}_{j}-S_{j}\right\|_{L_{1}\left(\hat{P}_{j}\right)}$ in Lemma 3 .

LEMMA 3. For $j=1, \ldots, p$, assume $\psi_{j}, j=1, \ldots, p$ satisfy assumption (A1) and (A2). With assumptions (A3) and (A4), we have

$$
\mathbb{P}\left(\frac{1}{n} \sum_{i=1}^{n}\left\|\hat{S}_{j}\left(X_{j}^{i}\right)-S_{j}\left(X_{j}^{i}\right)\right\| \geq \varepsilon\right) \leq \exp \left\{-C n\left[\left(\varepsilon-C n^{-\frac{1}{4}}\right)_{+}\right]^{2}\right\}
$$

Similar to the CMC setting, let $S_{j}^{(w)}(x)$ and $\hat{S}_{j}^{(w)}(x)$ be a winsorized version of $S_{j}(x)$ and $\hat{S}_{j}(x)$ with threshold $\sqrt{2 \log n}$, respectively. The concentration inequality in Lemma 3 applies to $\hat{S}^{(w)}$ and $S^{(w)}$.

COROLLARY 2. With same assumptions in Lemma 3, we have

$$
\mathbb{P}\left(\frac{1}{n} \sum_{i=1}^{n}\left\|\hat{S}_{j}^{(w)}\left(X_{j}^{i}\right)-S^{(w)}\left(X_{j}^{i}\right)\right\| \geq \varepsilon\right) \leq \exp \left\{-C n\left[\left(\varepsilon-C n^{-\frac{1}{4}}\right)_{+}\right]^{2}\right\}
$$

Compared with the concentration inequalities in Lemma 2, the mean convergence rate is sharpened to $n^{-\frac{1}{4}}$ from $n^{-\frac{1}{4 v d}}(\log n)^{\zeta_{d}}$. Using Lemma 3, we can also obtain a sharper convergence rate for the covariance matrix estimation than Theorems 1 by replacing $n^{-\frac{1}{4 v d}}(\log n)^{\zeta_{d}}$ with $n^{-\frac{1}{4}}$. When the principal non-Gaussian dimension $r>1$, stronger assumptions are required to guarantee the consistency of the estimated subspace $\hat{U}_{j}$. We leave the investigation of such assumptions for future research.

## 7 Simulation

### 7.1 Graph Learning with Two Attributes

We evaluate the numerical performance of thresholding, group graphical lasso, and neighborhood group lasso estimators (with "and" rule) for CMC-GGM when the dimension on each node is 2 . We also compare the performances of the three estimation methods with the Gaussian Graphical Model (GGM) and Copula Gaussian Graphical Model (Copula-GGM). To design the experiments, we first generate $d \times p$-dimensional Gaussian random vectors with mean 0 and the following block precision matrix $\Theta$ :

(A) Banded precision matrix: For $j=1, \ldots, p, \Theta_{j, j}=I_{d}$; for $j \geq 2, \Theta_{j, j-1}=\Theta_{j-1, j}=0.4 I_{d}$; for $j \geq 3, \Theta_{j, j-2}=\Theta_{j-2, j}=0.2 I_{d}$.

(B) Random precision matrix: Divide the graph into two connected parts, that is, let $\Theta=\operatorname{diag}\left(\Theta^{1}, \Theta^{2}\right)$, where $\Theta^{\ell} \in \mathbb{R}^{p / 2 \times p / 2}$ for $\ell=1,2$. For any $j \neq k, \ell=1,2, \Theta_{j, k}^{\ell}=\xi I_{d}$, where $\xi=0.3$ with probability 0.1 and 0 otherwise; $\Theta_{j, j}=\delta \cdot I_{d}$, where $\delta$ is chosen to guarantee the positive definiteness of $\Theta$.

(C) Hub-connected precision matrix: Generate a graph's edge set $E$ as follows. First, for all $j<k$, we set $E_{j k}=1$ with probability 0.01 , and 0 otherwise. Next, we randomly select $h=2$ hub nodes and set the elements of the corresponding rows and columns of $E$ equal 1 with probability 0.5 and 0 otherwise. For $s=1, \ldots, M$, generate $p \times p$ matrix $\Omega_{s}$ by

$$
\Omega_{s, j k}=\Omega_{s, k j}= \begin{cases}\delta, & \text { if } j=k \\ 0, & \text { if } E_{j k}=0 \\ \xi, & \text { if } E_{j k}=1\end{cases}
$$

where $\xi \sim U([-0.75,-0.25] \cap[0.25,0.75])$ and $\delta$ is chosen to guarantee the positive definiteness of $\Omega_{s}$. Let $\Omega$ be the block diagonal matrix $\operatorname{diag}\left(\Omega_{1}, \ldots, \Omega_{d}\right)$. The precision matrix is rearranged as $\left(\Theta_{j k}\right)_{s t}=\left(\Omega_{s t}\right)_{j k}$ for all $1 \leq j, k \leq p$ and $1 \leq s, t \leq d$.

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-22.jpg?height=469&width=1304&top_left_y=1072&top_left_x=389)

Figure 2: Visualization of graph structures for Models (A), (B), and (C), from left to right.

Figure 2 shows the graph structure of Models (A), (B), and (C). Let $\Sigma=\Theta^{-1}$ be the covariance matrix, and $\operatorname{diag}(\Sigma)^{-1 / 2}=\operatorname{diag}\left(\Sigma_{11}^{-1 / 2}, \ldots, \Sigma_{p p}^{-1 / 2}\right)$ be the block diagonal matrix. We generate $Z=\left(Z_{1}^{\top}, \ldots, Z_{p}^{\top}\right)^{\top} \sim N\left(0, \operatorname{diag}(\Sigma)^{-1 / 2} \Theta^{-1} \operatorname{diag}(\Sigma)^{-1 / 2}\right)$, which ensures that the distributions of the node vectors are standard bivariate Gaussian. We refer to $Z$ as the oracle Gaussian data that determines the graph structure. We then consider the following three transformations from $Z$ to the observed data $X$ :

(i) $X=Z$, which correspnds to observing Gaussian data;

(ii) $X_{j s}=f_{j s}\left(Z_{j s}\right)$, for $j=1, \ldots, p$ and $s=1,2$, where $f_{j s}$ is the exponential transformation, defined by

$$
f_{j s}(z)=\sigma_{j s}\left(\frac{\exp (z)-E\left[\exp \left(Z_{j s}\right)\right]}{\sqrt{\operatorname{var}\left(\exp \left(Z_{j s}\right)\right)}}\right)
$$

where $\sigma_{j s}$ is the standard deviation of $Z_{j s}$.
(iii) For $j=1, \ldots, p$, define $f_{j}: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$ as $f_{j}=\left(f_{j 1}, f_{j 2}\right)$, where $f_{j s}, s=1,2$ are the same as in (ii). Define $g_{j}: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$ as $g_{j}(z)=U\left(f_{j}\left(U^{\top} z\right)\right)$, where $U=\left((1,-1)^{\top}(1\right.$, 1) $\left.)^{\top}\right) / \sqrt{2} \in \mathbb{R}^{2 \times 2}$. Let $X_{j}=g_{j}\left(Z_{j}\right)$.

We note that transformation (ii) is coordinatewise monotonic, which guarantees that the subvector $X_{j}$ follows a nonparanormal distribution but not a multivariate Gaussian. We design the marginal transformation $f_{j s}$ to preserve the marginal standard deviation of the transformed data. Transformation (iii) is not coordinate-wise monotonic but cyclically monotonic, which ensures that $X$ has a CMCG distribution. Similar models with transformation (iii) are considered in Bryan et al. (2021) for semiparametric CCA modeling.

|  | group-glasso |  |  | thresholding |  |  | nbd-group-lasso |  |  |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Models | CMC | Copula | Linear | CMC | Copula | Linear | CMC | Copula | Linear |
| A-i | 0.977 | 0.982 | 0.983 | 0.976 | 0.982 | 0.983 | 0.991 | 0.993 | $\mathbf{0 . 9 9 4}$ |
|  | $(0.004)$ | $(0.003)$ | $(0.003)$ | $(0.007)$ | $(0.005)$ | $(0.005)$ | $(0.002)$ | $(0.002)$ | $(0.001)$ |
| A-ii | 0.974 | 0.982 | 0.862 | 0.974 | 0.982 | 0.833 | 0.989 | $\mathbf{0 . 9 9 3}$ | 0.864 |
|  | $(0.004)$ | $(0.003)$ | $(0.011)$ | $(0.006)$ | $(0.005)$ | $(0.014)$ | $(0.003)$ | $(0.002)$ | $(0.013)$ |
| A-iii | 0.974 | 0.950 | 0.863 | 0.971 | 0.940 | 0.834 | $\mathbf{0 . 9 8 9}$ | 0.966 | 0.862 |
|  | $(0.004)$ | $(0.007)$ | $(0.011)$ | $(0.006)$ | $(0.008)$ | $(0.013)$ | $(0.003)$ | $(0.005)$ | $(0.011)$ |

Table 1: Means and standard errors (in parentheses) for AUC of Model A

|  | group-glasso |  |  | thresholding |  |  | nbd-group-lasso |  |  |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Models | CMC | Copula | Linear | CMC | Copula | Linear | CMC | Copula | Linear |
| B-i | 0.928 | 0.940 | $\mathbf{0 . 9 4 2}$ | 0.777 | 0.792 | 0.797 | 0.918 | 0.929 | 0.931 |
|  | $(0.012)$ | $(0.011)$ | $(0.011)$ | $(0.017)$ | $(0.017)$ | $(0.017)$ | $(0.013)$ | $(0.013)$ | $(0.013)$ |
| B-ii | 0.922 | $\mathbf{0 . 9 3 9}$ | 0.776 | 0.77 | 0.791 | 0.613 | 0.914 | 0.929 | 0.753 |
|  | $(0.016)$ | $(0.014)$ | $(0.02)$ | $(0.02)$ | $(0.021)$ | $(0.023)$ | $(0.013)$ | $(0.013)$ | $(0.018)$ |
| B-iii | $\mathbf{0 . 9 2 4}$ | 0.894 | 0.774 | 0.879 | 0.838 | 0.691 | 0.914 | 0.879 | 0.748 |
|  | $(0.013)$ | $(0.014)$ | $(0.016)$ | $(0.016)$ | $(0.016)$ | $(0.018)$ | $(0.014)$ | $(0.014)$ | $(0.017)$ |

Table 2: Means and standard errors (in parentheses) for AUC of Model B

We conducted simulations with a network size of $p=100$ and sample size of $n=300$, repeating each simulation 50 times. We calculated the true positive rate (TPR) and false positive rate (FPR) for 20 different threshold values $\epsilon_{n}$ or tuning parameters $\lambda_{n}$, with which we generated a receiver operating characteristic (ROC) curve. The means and standard

|  |  | group-glasso |  |  | thresholding |  |  | nbd-group-lasso |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| Models | CMC | Copula | Linear | CMC | Copula | Linear | CMC | Copula | Linear |  |
| C-i | 0.885 | 0.896 | $\mathbf{0 . 8 9 9}$ | 0.775 | 0.791 | 0.794 | 0.818 | 0.826 | 0.829 |  |
|  | $(0.019)$ | $(0.017)$ | $(0.017)$ | $(0.025)$ | $(0.025)$ | $(0.026)$ | $(0.023)$ | $(0.024)$ | $(0.024)$ |  |
| C-ii | 0.880 | $\mathbf{0 . 8 9 6}$ | 0.746 | 0.767 | 0.791 | 0.638 | 0.812 | 0.826 | 0.687 |  |
|  | $(0.018)$ | $(0.017)$ | $(0.028)$ | $(0.025)$ | $(0.025)$ | $(0.038)$ | $(0.023)$ | $(0.024)$ | $(0.029)$ |  |
| C-iii | $\mathbf{0 . 8 7 7}$ | 0.849 | 0.742 | 0.760 | 0.728 | 0.637 | 0.815 | 0.784 | 0.687 |  |
|  | $(0.019)$ | $(0.020)$ | $(0.028)$ | $(0.037)$ | $(0.032)$ | $(0.037)$ | $(0.023)$ | $(0.023)$ | $(0.030)$ |  |

Table 3: Means and standard errors (in parentheses) for AUC of Model C

deviations (in parentheses) of the associated area-under-curve values (AUC) are reported in Tables 1, 2, and 3,

Our results indicate the following points: (a) when the data are generated from a Gaussian distribution (transformation (i)), linear transformation gives the most accurate estimation, but the difference among the three transformation methods is not significant; (b) when the data are generated from a copula Gaussian distribution (transformation (ii)), CMC-GGM and Copula-GGM give provide much more accurate estimation than GGM; (c) when the data are generated from a CMCG distribution, CMC-GGM significantly improves estimation accurate from Copula-GGM; (d) for Model A, the neighborhood group lasso provides higher AUC scores than the group glasso and thresholding; and (e) for the more challenging Models B and C, the group graphical lasso outperforms the neighborhood group lasso while thresholding performs poorly.

To visualize the comparison, in Figure 3 we display the average ROC curves of the methods estimated by graphical glasso and neighborhood group lasso. From the plot, we are further convinced that the CMC transformation methods (red curves) have the best overall performance when the data are generated from non-copula Gaussian distribution (right column).

To better illustrate why copula models fail under setting (iii), we show the copula and CMC transformation results in Figure 4. We generate $n=300$ samples from Model A-iii on one node. The green points are the oracle Gaussian data that we want to recover and use to estimate the precision matrix further. From left to right, the red points are observations, copula-transformed data, and CMC-transformed data, respectively. We see that in the middle panel, after the copula transformation, the red points are marginal Gaussian on both coordinates but jointly show a triangular shape, which deviates from the joint Gaussian
![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-25.jpg?height=1636&width=1662&top_left_y=228&top_left_x=229)

trans.methods - cmc - copula - linear methods - nbd-group-lasso $\cdots$ group-glasso

Figure 3: Comparison of average estimated ROC curves over 50 simulation runs: Model A-i, A-ii and A-iii (top row); Model B-i, B-ii, and B-iii (middle row); Model C-i, C-ii, and C-iii (bottom row).

distribution. Consequently, the values on both coordinates are estimated poorly, affecting the further estimation of the precision matrix. In contrast, the CMC transformation can better recover the underlying oracle points, as demonstrated in the right panel.
![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-26.jpg?height=526&width=1654&top_left_y=236&top_left_x=232)

Figure 4: Visualization of transformations for setting (iii): green points are oracle data, red points are data from (Left) observations; (Middle) copula transformation; (Right) CMC transformation.

### 7.2 Graph Learning with More Than Two Attributes

In this subsection, we compare the performance of Copula-GGM, CMC-GGM, and PCMCGGM when the number of attributes on each node is larger than 2 . We first generate Gaussian data from Model (A) in Section 7.1. For $j=1, \ldots, p$, define $f_{j}: \mathbb{R}^{r} \rightarrow \mathbb{R}^{r}$ by $f_{j}=\left(f_{j 1}, \cdots, f_{j r}\right)$, where $f_{j s}$ is univariate monotonic function. We consider two choices for $f_{j s}$ : the first one is the exponential map defined in Section 7.1 (ii); the second one is the cubic map defined by

$$
f_{j s}(z)=\sigma_{j s}\left(\frac{z^{3}-E\left[Z_{j s}^{3}\right]}{\sqrt{\operatorname{var}\left(Z_{j s}^{3}\right)}}\right)
$$

where $\sigma_{j s}$ is the standard deviation of $Z_{j s}$. Then we define $g_{j}: \mathbb{R}^{d} \rightarrow \mathbb{R}^{d}$ as $g_{j}(z)=$ $U\left(f_{j}\left(U^{\top} z\right)\right)+V V^{\top} z$, where $U \in \mathbb{R}^{d \times r}$ and $(U, V) \in \mathbb{R}^{d \times d}$ is a orthogonal matrix. Let $X_{j}=g_{j}\left(Z_{j}\right)$. Under this setting, the non-Gaussian observations $X_{j}$ and the oracle Gaussian data $Z_{j}$ only differ on a $r$-dimensional subspace spanned by $U$. To be consistent with the notations in Section 7.1, we call the models A-iv-exp and A-iv-cubic. Here, we use $n=300$, $p=50$, and $d \in\{3,5,7\}$. We let $r=1$ and $U=(1,1,0, \ldots, 0)^{\top} / \sqrt{2}$, that is, there is one non-Gaussian direction contained in $X_{j}$. More numerical results on $r>1$ can be found in the Supplementary Material.

For PCMC-GGM, we independently generate 10 samples and use the Riemannian block coordinate descent (RBCD) algorithm proposed in Huang et al. (2021) to solve $\hat{U}_{j}^{l}, j=1$, $\ldots, p, l=1, \ldots, 10$. We then take the extrinsic average of 10 repeats to obtain the estimator $\hat{U}_{j}$, which is the first eigenvector of $\sum_{l=1}^{10} \hat{U}_{j}^{l}\left(\hat{U}_{j}^{l}\right)^{\top}$. We assume that the true dimension 1 is
![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-27.jpg?height=1138&width=1674&top_left_y=244&top_left_x=230)

trans.methods - cmc - copula - pcmc est.methods - - group-glasso - nbd-group-lasso

Figure 5: Comparison of average estimated ROC curves over 50 simulation runs among PCMC-GGM, CMC-GGM, and Copula-GGM; First row: Model A-iv-exp; Second row: Model A-iv-cubic; Columns from left to right corresponds to $d=3,5$, and 7 .

known. Determining the dimension for the projected subspace distance in a more systematic way is beyond the scope of this paper. We then solve the OT problem between projected samples $\left\{\hat{U}_{j} X_{j}^{i}\right\}_{i=1}^{n}$ and $\left\{\hat{U}_{j} Z_{j}^{i}\right\}_{i=1}^{n}$ for $j=1, \ldots, p$ to get an estimate optimal transport $\hat{T}_{j}$. The PCMC transformation is then estimated by (23). After 50 repeats of the experiments, we plot the average ROC curves of the PCMC-GGM, CMC-GGM, and Copula-GGM in Figure 5. We also report the means and standard deviations (in parentheses) of the associated AUC scores in Table 4. We observe from the table that the accuracy of CMC-GGM drops sharply with the increase of the attribute dimension. Overall, PCMC-GGM outperforms Copula-GGM and CMC-GGM.

We provide a visualization of the Copula, CMC, and PCMC transformations in Figure 6. Specifically, we consider the data on one node in Model A-iv-cubic when $d=5$ and plot the data on the first two coordinates. The green points are the oracle Gaussian data. From left to right, the red points are the transformed data from Copula, CMC, and PCMC trans-

|  |  | group-glasso |  |  | nbd-group-lasso |  |  | thresholding |  |  |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Model | $d$ | CMC | Copula | PCMC | CMC | Copula | PCMC | CMC | Copula | PCMC |
|  | 3 | 0.921 | 0.920 | 0.942 | 0.949 | 0.944 | $\mathbf{0 . 9 7 0}$ | 0.917 | 0.915 | 0.949 |
|  |  | $(0.013)$ | $(0.014)$ | $(0.01)$ | $(0.009)$ | $(0.011)$ | $(0.007)$ | $(0.017)$ | $(0.014)$ | $(0.013)$ |
| A-iv-exp | 5 | 0.827 | 0.863 | 0.875 | 0.840 | 0.882 | $\mathbf{0 . 9 1 5}$ | 0.662 | 0.744 | 0.789 |
|  |  | $(0.018)$ | $(0.014)$ | $(0.052)$ | $(0.018)$ | $(0.014)$ | $(0.012)$ | $(0.028)$ | $(0.030)$ | $(0.026)$ |
|  | 7 | 0.747 | 0.820 | 0.845 | 0.744 | 0.834 | $\mathbf{0 . 8 6 0}$ | 0.593 | 0.696 | 0.739 |
|  |  | $(0.019)$ | $(0.016)$ | $(0.018)$ | $(0.019)$ | $(0.017)$ | $(0.015)$ | $(0.031)$ | $(0.024)$ | $(0.020)$ |
|  | 3 | 0.914 | 0.922 | 0.933 | 0.948 | 0.951 | $\mathbf{0 . 9 6 7}$ | 0.918 | 0.914 | 0.94 |
| A-iv-cubic |  | $(0.011)$ | $(0.013)$ | $(0.013)$ | $(0.009)$ | $(0.011)$ | $(0.008)$ | $(0.013)$ | $(0.019)$ | $(0.012)$ |
|  | 5 | 0.83 | 0.874 | 0.877 | 0.845 | 0.892 | $\mathbf{0 . 9 1 8}$ | 0.677 | 0.76 | 0.788 |
|  |  | $(0.019)$ | $(0.017)$ | $(0.027)$ | $(0.018)$ | $(0.015)$ | $(0.014)$ | $(0.028)$ | $(0.020)$ | $(0.022)$ |
|  | 7 | 0.758 | 0.833 | 0.826 | 0.755 | 0.849 | $\mathbf{0 . 8 6 7}$ | 0.602 | 0.715 | 0.739 |
|  | $(0.022)$ | $(0.020)$ | $(0.050)$ | $(0.020)$ | $(0.019)$ | $(0.016)$ | $(0.028)$ | $(0.029)$ | $(0.028)$ |  |

Table 4: Means and standard errors (in parentheses) for AUC for Models A-iv-exp and Aiv-cubic

formations, respectively. We observe that in the left panel, after the copula transformation, red points still show non-Gaussianity along direction $(1,1,0, \ldots, 0)^{\top}$. In the middle panel, after the CMC transformation, red points can not recover green points accurately due to the large estimation error arising from solving a high-dimensional OT problem. In contrast, the PCMC transformation can accurately recover the underlying oracle points, as shown in the right panel.
![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-28.jpg?height=512&width=1652&top_left_y=1706&top_left_x=236)

Figure 6: Visualization of transformations in Model A-iv-cubic: red points are oracle data, green points are data from (L) copula transformation; (M) CMC transformation; (R) PCMC transformation.

## 8 Real Applications

In this section, we consider two data applications where multi-attributes occur naturally. Since the ground truth is unknown in the data application, the goal of the analysis is only to visualize and explore the underlying dependency structures of the data. We will focus on showing the non-Guassianality of the data and compare the performance of GGM, CopulaGGM, and CMC-GGM. We use the group glasso to estimate the graph, which performs the best in the simulations.

### 8.1 Gene/Protein Regulatory Network Inference

We applied the CMC-GGM to reconstruct networks on breast cancer data sets from the National Cancer Institute (https://www.cancer.gov/), referred to as NCI-60 and analyzed in Katenka and Kolaczyk (2011); Kolar et al. (2014) and Chiquet et al. (2019). The data set contains protein profiles (reverse-phase lysate arrays for 92 antibodies) and gene profiles (normalized RNA microarray intensities from Human Genome U95 Affymetrix chip-set for about 9000 genes). Katenka and Kolaczyk (2011) constructed a 'concensus' data set containing $91(p=91)$ protein/gene profiles matched in pairs $(d=2)$ by common Entrez identifiers across $60(n=60)$ cancer cells.

|  | GGM | Copula-GGM | CMC-GGM |
| :--- | :---: | :---: | :---: |
| Number of edges | 299 | 309 | 168 |
| Number of shared edges with GGM | $* *$ | 183 | 129 |
| Avg Node Degree | 6.571 | 6.791 | 3.692 |
| Number of nodes with non-Gaussianity | 69 | 9 | 0 |

Table 5: Summary statistics for gene/protein networks estimated by GGM, Copula-GGM, and CMC-GGM

We begin by applying the group glasso for GGM to fit the gene/protein network and then compare it with the network constructed using the Copula-GGM and CMC-GGM. For each method, we use the 10 -fold cross-validation to select the tuning parameters, resulting in dense networks with a sparsity of about 0.4 . We then estimate the network 50 times based on bootstrap samples. The stable graph was then constructed from the edges that appeared in at least $90 \%$ of the bootstrap replications. Table 5 provides a few summary statistics for the estimated networks. To test the joint Gaussianity of the data on each node, we use
the energy statistics (Székely and Rizzo, 2013) with a permutation test of 499 replications. A node is identified to have non-Gaussian data if the p-value is less than 0.05. Among all 91 nodes, 69 have non-Gaussian data, and 9 still exhibit non-Gaussianity even after copula transformations. Figure 7 shows the graph fitted by GGM and CMC-GGM, where red cells represent the edge shared by the two methods, green cells represent the edges unique to GGM, and blue cells represent the edges unique to CMC-GGM. The differences in networks require a closer biological inspection based on domain knowledge.

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-30.jpg?height=589&width=591&top_left_y=730&top_left_x=450)

(a) GGM; sparsity 0.073 .

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-30.jpg?height=586&width=574&top_left_y=729&top_left_x=1098)

(b) CMC-GGM; sparsity 0.053 .

Figure 7: Gene/Protein network; Red cells represent edges shared by (a) and (b); green cells represent edges unique to (a); and blue cells represent edges unique to (b).

### 8.2 Color Texture Images

Pavez and Ortega (2016) and Pavez et al. (2018) built undirected graphs for grayscale images to infer the dependence of a pixel on neighboring pixels. Tugnait (2021) extended this idea to build a multi-attribute graphical model for colored images, where each node represents three attributes (RGB components) from a pixel.

To evaluate our method, we selected two images (Image 79 and Image 105) from the Colored Brodatz Texture Database (https://multibandtexture.recherche.usherbroo ke.ca/). We label image 79 as image 1 and image 105 as Image 2. Two images are read as a raster object with dimension $640 \times 640 \times 3$ in R. For image 1, we extracted rows 481 through 640 and columns 481 through 640 . For image 2, we extracted rows 321 through 480 and columns 1 through 160. This creates the $160 \times 160$ patches used to build image graphs, visualized in Figure 8(a) and (d). The patches were then partitioned into non-overlapping
$8 \times 8$ blocks and then vectorized into 64 -dimensional pixel vectors. For each node, we have three attributes associated with RGB decompositions. Therefore, we have a data set with sizes $n=400, p=64$, and $d=3$. We found that the data showed non-Gaussianity with p-values less than 0.05 from an energy test at all nodes. Even after copula transformations, non-Gaussianity still persisted. We compared the performance of GGM and CMC-GGM on this data set. We used the BIC-based method to select the tuning parameters. For image 1, CMC-GGM and GGM obtained graphs with sparsities of 0.162 and 0.174 , respectively. For image 2, CMC-GGM and GGM drive graphs with sparsities of 0.183 and 0.211 , respectively.

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-31.jpg?height=429&width=431&top_left_y=802&top_left_x=240)

(a) image 1

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-31.jpg?height=417&width=423&top_left_y=1320&top_left_x=249)

(d) image 2

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-31.jpg?height=415&width=525&top_left_y=801&top_left_x=754)

(b) GGM; sparsity 0.174.

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-31.jpg?height=418&width=528&top_left_y=1309&top_left_x=755)

(e) GGM; sparsity 0.203 .

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-31.jpg?height=412&width=526&top_left_y=802&top_left_x=1339)

(c) CMC-GGM; sparsity 0.160 .

![](https://cdn.mathpix.com/cropped/2024_04_26_9e813c1d020440870facg-31.jpg?height=428&width=531&top_left_y=1304&top_left_x=1336)

(f) CMC-GGM; sparsity 0.187.

Figure 8: Color texture graph

The estimated graphs are visualized in Figure 8. The color and width of the links indicate the edge weights, which are taken as the Frobenius norm of the block matrix $\left\|\hat{\Theta}_{j k}\right\|_{F}$. By comparing the estimated graphs with the raw texture images, we can observe that strong links capture the principle texture orientations. Specifically, for image 1, vertical and some horizontal directions are the primary orientation of the texture; for image 2, the horizontal direction is the primary orientation. By comparing the graph (b) and (d), and (e) and (f), we see that using CMC transformation helps to estimate more precise graphs that match the raw image. On the other hand, the GGM may retain more error signals, such as the vertical
signals on the upper left corner of graph (e).

## 9 Conclusion

This paper presents a new semiparametric copula graphical model for multi-attribute data based on the newly introduced cyclically monotone copula. The proposed model is more flexible than the existing copula Gaussian graphical model that only performs coordinatewise Gaussianization. We demonstrate both theoretical and numerical properties of the proposed methods. In future work, it will be interesting to study other types of graphical models such as Xue et al. (2012); Yang et al. (2015); Tao et al. (2024); Lee et al. (2022) using optimal transport theory.

## References

Abramovich, F., Benjamini, Y., Donoho, D. L. and Johnstone, I. M. (2006), 'Adapting to unknown sparsity by controlling the false discovery rate', The Annals of Statistics $\mathbf{3 4}(2), 584-653$.

Brenier, Y. (1991), 'Polar factorization and monotone rearrangement of vector-valued functions', Communications on Pure and Applied Mathematics 44(4), 375-417.

Bryan, J. G., Niles-Weed, J. and Hoff, P. D. (2021), 'The multirank likelihood and cyclically monotone monte carlo: a semiparametric approach to cca', arXiv preprint arXiv:2112.07465 .

Caffarelli, L. A. (2000), 'Monotonicity properties of optimal transportation and the fkg and related inequalities', Communications in Mathematical Physics 214, 547-563.

Cai, T., Liu, W. and Luo, X. (2011), 'A constrained 11 minimization approach to sparse precision matrix estimation', Journal of the American Statistical Association 106(494), 594607 .

Carlier, G., Chernozhukov, V. and Galichon, A. (2016), 'Vector quantile regression: an optimal transport approach', The Annals of Statistics 44(3), 1165-1192.

Chernozhukov, V., Galichon, A., Hallin, M. and Henry, M. (2017), 'Monge-kantorovich depth, quantiles, ranks and signs', The Annals of Statistics 45(1), 223-256.

Chiquet, J., Rigaill, G. and Sundqvist, M. (2019), 'A multiattribute gaussian graphical model for inferring multiscale regulatory networks: an application in breast cancer', Gene Regulatory Networks: Methods and Protocols pp. 143-160.

Colombo, M. and Fathi, M. (2021), 'Bounds on optimal transport maps onto log-concave measures', Journal of Differential Equations 271, 1007-1022.

Deb, N., Ghosal, P. and Sen, B. (2021), 'Rates of estimation of optimal transport maps using plug-in estimators via barycentric projections', Advances in Neural Information Processing Systems 34, 29736-29753.

Deb, N. and Sen, B. (2023), 'Multivariate rank-based distribution-free nonparametric testing using measure transportation', 118(541), 192-207.

Deshpande, I., Zhang, Z. and Schwing, A. G. (2018), Generative modeling using the sliced wasserstein distance, in 'Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition', pp. 3483-3491.

Fan, Y. and Henry, M. (2023), 'Vector copulas', Journal of Econometrics 234(1), 128-150.

Fournier, N. and Guillin, A. (2015), 'On the rate of convergence in wasserstein distance of the empirical measure', Probability Theory and Related Fields 162(3), 707-738.

Friedman, J., Hastie, T. and Tibshirani, R. (2008), 'Sparse inverse covariance estimation with the graphical lasso', Biostatistics 9(3), 432-441.

Ghosal, P. and Sen, B. (2022), 'Multivariate ranks and quantiles using optimal transport: Consistency, rates and nonparametric testing', The Annals of Statistics 50(2), 1012-1037.

Gozlan, N. and Léonard, C. (2010), 'Transport inequalities. a survey', arXiv preprint arXiv:1003.3852 .

Hallin, M., Del Barrio, E., Cuesta-Albertos, J. and Matrán, C. (2021), 'Distribution and quantile functions, ranks and signs in dimension d: A measure transportation approach', The Annals of Statistics 49(2), 1139-1165.

Hiriart-Urruty, J.-B. and Lemaréchal, C. (2004), Fundamentals of convex analysis, Springer Science \& Business Media.

Huang, M., Ma, S. and Lai, L. (2021), A riemannian block coordinate descent method for computing the projection robust wasserstein distance, in 'International Conference on Machine Learning', PMLR, pp. 4446-4455.

Jonker, R. and Volgenant, T. (1988), A shortest augmenting path algorithm for dense and sparse linear assignment problems, in 'DGOR/NSOR: Papers of the 16th Annual Meeting of DGOR in Cooperation with NSOR/Vorträge der 16. Jahrestagung der DGOR zusammen mit der NSOR', Springer, pp. 622-622.

Kantorovich, L. V. (1948), On a problem of monge, in 'CR (Doklady) Acad. Sci. URSS (NS)', Vol. 3, pp. 225-226.

Katenka, N. and Kolaczyk, E. (2011), 'Multi-attribute networks and the impact of partial information on inference and characterization', arXiv preprint arXiv:1109.3160 .

Klaassen, C. A. and Wellner, J. A. (1997), 'Efficient estimation in the bivariate normal copula model: normal margins are least favourable', Bernoulli pp. 55-77.

Kolar, M., Liu, H. and Xing, E. (2013), Markov network estimation from multi-attribute data, in 'International Conference on Machine Learning', PMLR, pp. 73-81.

Kolar, M., Liu, H. and Xing, E. P. (2014), 'Graph estimation from multi-attribute data', Journal of Machine Learning Research 15(1), 1713-1750.

Lafferty, J., Liu, H. and Wasserman, L. (2012), 'Sparse nonparametric graphical models', Statistical Science 27(4), 519-537.

Lee, K. H., Chen, Q., DeSarbo, W. S. and Xue, L. (2022), 'Estimating finite mixtures of ordinal graphical models', Psychometrika 87(1), 83-106.

Liu, H., Han, F., Yuan, M., Lafferty, J. and Wasserman, L. (2012), 'High-dimensional semiparametric gaussian copula graphical models', The Annals of Statistics 40(4), 2293-2326.

Liu, H., Lafferty, J. and Wasserman, L. (2009), 'The nonparanormal: Semiparametric estimation of high dimensional undirected graphs', Journal of Machine Learning Research 10(80), 2295-2328.

Mai, Q., He, D. and Zou, H. (2023), 'Coordinatewise gaussianization: Theories and applications', Journal of the American Statistical Association 118(544), 2329-2343.

Manole, T., Balakrishnan, S., Niles-Weed, J. and Wasserman, L. (2021), 'Plugin estimation of smooth optimal transport maps', arXiv preprint arXiv:2107.12364.

Manole, T. and Niles-Weed, J. (2021), 'Sharp convergence rates for empirical optimal transport with smooth costs', arXiv preprint arXiv:2106.13181 .

McCann, R. J. (1995), 'Existence and uniqueness of monotone measure-preserving maps', Duke Mathematical Journal 80(2), 309-323.

Meinshausen, N. and Bühlmann, P. (2006), 'High-dimensional graphs and variable selection with the lasso', The Annals of Statistics 34(3), 1436-1462.

Meinshausen, N. and Bühlmann, P. (2010), 'Stability selection', Journal of the Royal Statistical Society: Series B (Statistical Methodology) 72(4), 417-473.

Meng, C., Ke, Y., Zhang, J., Zhang, M., Zhong, W. and Ma, P. (2019), 'Large-scale optimal transport map estimation using projection pursuit', Advances in Neural Information Processing Systems 32.

Niles-Weed, J. and Rigollet, P. (2022), 'Estimation of wasserstein distances in the spiked transport model', Bernoulli 28(4), 2663-2688.

Paty, F.-P. and Cuturi, M. (2019), Subspace robust wasserstein distances, in 'International Conference on Machine Learning', PMLR, pp. 5072-5081.

Pavez, E., Egilmez, H. E. and Ortega, A. (2018), 'Learning graphs with monotone topology properties and multiple connected components', IEEE Transactions on Signal Processing 66(9), 2399-2413.

Pavez, E. and Ortega, A. (2016), Generalized laplacian precision matrix estimation for graph signal processing, in ' 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)', IEEE, pp. 6350-6354.

Qiao, X., Guo, S. and James, G. M. (2019), 'Functional graphical models', Journal of the American Statistical Association 114(525), 211-222.

Ravikumar, P., Wainwright, M. J., Raskutti, G. and Yu, B. (2011), 'High-dimensional covariance estimation by minimizing $\ell_{1}$-penalized log-determinant divergence', Electronic Journal of Statistics 5, 935-980.

Rockafellar, R. (1966), 'Characterization of the subdifferentials of convex functions', Pacific Journal of Mathematics 17(3), 497-510.

Shi, H., Drton, M. and Han, F. (2022), 'Distribution-free consistent independence tests via center-outward ranks and signs', Journal of the American Statistical Association 117(537), 395-410.

Solea, E. and Li, B. (2022), 'Copula gaussian graphical models for functional data', Journal of the American Statistical Association 117(538), 781-793.

Székely, G. J. and Rizzo, M. L. (2013), 'Energy statistics: A class of statistics based on distances', Journal of Statistical Planning and Inference 143(8), 1249-1272.

Tao, J., Li, B. and Xue, L. (2024), 'An additive graphical model for discrete data', Journal of the American Statistical Association 119(545), 368-381.

Tugnait, J. K. (2021), 'Sparse-group lasso for graph learning from multi-attribute data', IEEE Transactions on Signal Processing 69, 1771-1786.

Villani, C. (2009), Optimal Transport: Old and New, Vol. 338, Springer.

Xue, L. and Zou, H. (2012), 'Regularized rank-based estimation of high-dimensional nonparanormal graphical models', The Annals of Statistics 40(5), 2541-2571.

Xue, L., Zou, H. and Cai, T. (2012), 'Nonconcave penalized composite conditional likelihood estimation of sparse ising models', The Annals of Statistics 40(3), 1403-1429.

Yang, E., Ravikumar, P., Allen, G. I. and Liu, Z. (2015), 'Graphical models via univariate exponential family distributions', The Journal of Machine Learning Research 16(1), 38133847.

Yang, Y. and Zou, H. (2015), 'A fast unified algorithm for solving group-lasso penalize learning problems', Statistics and Computing 25, 1129-1141.

Yuan, M. and Lin, Y. (2007), 'Model selection and estimation in the gaussian graphical model', Biometrika 94(1), 19-35.

Zhang, J., Ma, P., Zhong, W. and Meng, C. (2022), 'Projection-based techniques for highdimensional optimal transport problems', Wiley Interdisciplinary Reviews: Computational Statistics p. e1587.

Zhang, T. and Zou, H. (2014), 'Sparse precision matrix estimation via lasso penalized d-trace loss', Biometrika 101(1), 103-120.

Zhao, B., Zhai, S., Wang, Y. S. and Kolar, M. (2021), 'High-dimensional functional graphical model structure learning via neighborhood selection approach', arXiv preprint arXiv:2105.02487.

