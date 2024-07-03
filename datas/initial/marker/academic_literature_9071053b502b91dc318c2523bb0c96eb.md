# High-Dimensional Copula-Based Wasserstein Dependence.

Steven De Keysera, Irene Gijbels `
a,∗
a*Department of Mathematics, KU Leuven, Celestijnenlaan 200B, B-3001 Leuven (Heverlee), Belgium*

## Abstract

We generalize 2-Wasserstein dependence coefficients to measure dependence between a finite number of random vectors. This generalization includes theoretical properties, and in particular focuses on an interpretation of maximal dependence and an asymptotic normality result for a proposed semi-parametric estimator under a Gaussian copula assumption. In addition, we discuss general axioms for dependence measures between multiple random vectors, other plausible normalizations, and various examples. Afterwards, we look into plug-in estimators based on penalized empirical covariance matrices in order to deal with high dimensionality issues and take possible marginal independencies into account by inducing (block) sparsity. The latter ideas are investigated via a simulation study, considering other dependence coefficients as well. We illustrate the use of the developed methods in two real data applications. Keywords: Copula, Normal scores rank correlation, Regularization, Sparsity, Wasserstein dependence 2020 MSC: Primary 62Axx, 62Hxx; Secondary 62Exx, 62Gxx.

## 1. Introduction

A prominent line of research in statistics considers measuring dependence between groups of variables. In case of two groups, greatly celebrated is the canonical correlation analysis of [27] relying on the Pearson correlation coefficient. To step away from the assumption of Gaussianity, concordance measures as studied in, e.g., [22, 37, 42]
among many others, are also used for quantifying general monotonic associations between two random vectors in
[23]. In [26], measures of association computed from collapsed random variables are used to measure the dependence between random vectors. Fundamental is copula theory (e.g., [38, 43]), allowing to split multivariate distributions into marginal distributions on the one hand, and a dependence structure described by the copula on the other hand. Especially when the marginals are continuous, the preference often goes to copula-based dependence measures since then, by Sklar's theorem [43], the copula is unique, and hence margin-free dependence can unequivocally be quantified.

Statistical independence between random vectors holds if and only if the true underlying copula is the product of the marginal copulas (where a one dimensional copula is basically a uniform distribution on [0, 1]), yielding zero dependence. However, the dependence measures mentioned above do not detect all types of departure from independence, meaning that they might vanish while the independence product copula is misspecified. Since the work of
[44], there has been a growing interest for dependence measures that completely characterize independence. Some recent developments are, e.g., the Hoeffding's Phi-Square measure of [35], the Φ-dependence measures of [11] (of which the Hellinger correlation [20] and essential dependence [51] are particular cases), the coefficient of Chatterjee
[1, 2, 8, 18], and the 2-Wasserstein coefficients of [36].

The aim of this article is to elaborate further on the optimal transport measures of [36]. First, the focus will be on extending their dependence coefficients from two to finitely many random vectors. We do this from a copula point of view. This includes generalizing the results of [36], and also verifying the axioms stated in [11] (see also Appendix A). Some additional examples, focusing on, e.g., the impact of the normalization, are provided as well. Afterwards, we dive into the Bures-Wasserstein dependence making a Gaussian copula assumption. This yields dependence measures that are attractive, and more amenable for estimation. The results are a far from straightforward extension of results of [36] to the case of a finite number of random vectors, and require significant mathematical care.

The proposed semi-parametric estimation approach of the Bures-Wasserstein coefficients relies on the sample matrix of normal scores rank correlations (see, e.g., [24]). Since we extend the theory to a general finite amount of groups of variables, high dimensional cases with a large number of variables compared to the sample size are of study interest as well. Acclaimed penalization techniques are known to significantly improve (inverse) covariance matrix estimation (see, e.g., [29] and references therein). We utilize these ideas in our Gaussian copula context in order to correct for high dimensionality bias and possibly enforce sparsity at the individual level or group level to take plausible marginal independencies into account.

The outline of this paper is the following. Section 2 explains how optimal transport theory is combined with copula theory in order to arrive at a dependence measure between multiple groups of random variables that completely characterizes independence and is invariant with respect to the univariate marginal distributions. The verification of the properties postulated in [11] for such dependence measures is also part of this section. The Gaussian copula approach is discussed in Section 3, with special attention to the meaning of maximal dependence, and asymptotic normality of the proposed semi-parametric estimator. Afterwards, different regularization techniques for Gaussian copula covariance matrices are discussed in Section 4. Next to an empirical illustration of the asymptotic normality result, simulations are performed in Section 5 to investigate the performance of these regularization techniques on various dependence coefficients for random vectors. Two real data applications are discussed in Section 6. All proofs are deferred to the Appendix. Any experiments reported can be reproduced via the source code available at https://github.com/StevenDeKeyser98/VecDep. Additional figures are included in the Supplementary Material.

## 2. General 2-Wasserstein Dependence

We consider a q-dimensional random vector X = (X1, . . . , Xk) defined on (R
q
, B(R
q), λq) consisting of k marginal random vectors Xi = (Xi1, . . . , Xidi
) for i = 1, . . . , k having di continuous univariate marginal random variables Xi j for j = 1, . . . , di. The numbers d1, . . . , dk ∈ Z>0 are such that q = d1+· · ·+dk, and λ q denotes the q-dimensional Lebesgue measure defined on B(R
q), the Borel sigma-algebra on R
q. Let P : B(R
q) → R be a probability measure. Our aim is to measure the dependence between X1, . . . , Xk. For I = [0, 1] and P(I
q) the set of Borel probability measures on I

q, the random vector X is assigned a copula probability law µC ∈ P(I
q) having corresponding marginal copula laws µCi ∈ P(I
di) of Xi for i = 1, . . . , k. Note that in case di = 1, the law µCi is that of a uniform distribution on I. We denote Γ(µC1, . . . , µCk
) for the set of measures γ ∈ P(I
q) such that

µCi
$\mu_{C_{i}}(B_{i})=\gamma\left(\mathbb{I}^{d_{1}}\times\cdots\times\mathbb{I}^{d_{i-1}}\times B_{i}\times\mathbb{I}^{d_{i+1}}\times\cdots\times\mathbb{I}^{d_{k}}\right)$
for all Bi ∈ B(I
di) and i = 1, . . . , k. This is a natural generalization of the set of coupling measures. Obviously, µC ∈
Γ(µC1, . . . , µCk
). Quantifying the intensity of relation between X1, . . . , Xk can be done by measuring the difference between µC and the product measure µC1 × · · · × µCk
. We use the 2-Wasserstein distance, whose square is, for certain measures π,eπ ∈ P(I
q) given by

$$W_{2}^{2}(\pi,\widetilde{\pi})=\operatorname*{inf}_{\gamma\in\Gamma(\pi,\widetilde{\pi})}\int_{\mathbb{P}^{q}}\|\mathbf{u}-\mathbf{v}\|^{2}d\gamma(\mathbf{u},\mathbf{v})=\operatorname*{inf}_{\begin{subarray}{c}\mathbf{U}-\pi\\ \mathbf{V}-\widetilde{\pi}\end{subarray}}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right).$$

||U − V||2. (1)
The interpretation of the metric (1) is optimal transport, see, e.g., [39]. It is the minimal effort (cost) required to transform the mass of π into the mass of eπ, i.e., for every (u, v) transport an infinitesimal amount of mass dγ(u, v)
from u to v at a distance cost of ||u − v||2. Aggregating the mass γ({u} × I
q) that leaves u gives π(u) and the total mass γ(I
q × {v}) that reaches v equals eπ(v). For certain non-degenerate (i.e. not Dirac delta distributions) reference laws νi ∈ P(I
di) for i = 1, . . . , k, we now define

$$T_{d_{1},\ldots,d_{k}}(\mu_{C};\nu_{1},\ldots,\nu_{k})=W_{2}^{2}(\mu_{C},\nu_{1}\times\cdots\times\nu_{k})-W_{2}^{2}(\mu_{C_{1}}\times\cdots\times\mu_{C_{k}},\nu_{1}\times\cdots\times\nu_{k})$$ $$=W_{2}^{2}(\mu_{C},\nu_{1}\times\cdots\times\nu_{k})-\sum_{i=1}^{k}W_{2}^{2}(\mu_{C_{i}},\nu_{i}),$$
$$(1)$$

where the second identity is known to be true (see, e.g., [39]). We call a subset A ⊂ P(I
q) W2-compact if every sequence in the metric space (A, W2) has a convergent subsequence with limit in A. Lemma 1 gives the main properties of Td1,...,dk
. Proofs of Lemma 1, and all other theoretical results of Section 2, can be found in Appendix B.

Lemma 1. It holds that
(a) Td1,...,dk
(µC; ν1, . . . , νk) ≥ 0
(b) Td1,...,dk
(µC1 × · · · × µCk
; ν1, . . . , νk) = 0
(c) If either µCi = νi*for all i* = 1, . . . , k or νi*is absolutely continuous (with respect to* λ di*) for all i* = 1, . . . , k, then Td1,...,dk
(µC; ν1, . . . , νk) = 0 *implies* µC = µC1 × · · · × µCk
(d) *The set* Γ(µC1, . . . , µCk
) is W2*-compact in* P(I
q) *and the mapping T*d1,...,dk
( · ; ν1, . . . , νk) : (Γ(µC1, . . . , µCk
), W2) →
(R, | · |) *is continuous.*

Its interpretation, together with its mathematical properties, make Td1,...,dk
(µC; ν1, . . . , νk) an appealing measure of
dependence between k random vectors X1, . . . , Xk. In what follows, we assume that νiis absolutely continuous for
i = 1, . . . , k, and let GC ⊂ Γ(µC1, . . . , µCk
) be a compact set such that µC ∈ GC. General axioms for dependence
measures between multiple random vectors are formulated in [11], see also Appendix A. Lemma 1 offers aid in
proving them here, see Proposition 1.
Proposition 1. *Consider Axioms (A1)-(A8) given in Appendix A, and a normalized version of T*d1,...,dk
(µC; ν1, . . . , νk)
given by
given by_  $$\mathcal{D}(\mu_{C};\nu_{1},\ldots,\nu_{k})=\frac{T_{d_{i\ldots d_{k}}}(\mu_{C};\nu_{1},\ldots,\nu_{k})}{\sup_{\mu_{C}\in\mathcal{U}_{d_{i\ldots d_{k}}}}T_{d_{i\ldots d_{k}}}(\mu_{C};\nu_{1},\ldots,\nu_{k})}.\tag{2}$$  _Then, $\mathcal{D}$ satisfies (A1)-(A3) and (A5)-(A7). Axioms (A4) and (A5) are satisfied by the non-normalized version $T_{d_{i\ldots d_{k}}}$._
Then, D *satisfies (A1)-(A3) and (A5)-(A7). Axioms (A4) and (A8) are satisfied by the non-normalized version T*d1,...,dk
.
$$(2)^{\frac{1}{2}}$$
The supremum in (2) is attained when GC is W2-compact (e.g., GC = Γ(µC1, . . . , µCk
)) because of (d) in Lemma 1.

It represents the case of maximal dependence, which characterization (and hence the overall behaviour of (2)), largely depends on GC. There is still freedom in choosing the normalization by picking the set GC. It might impose additional constraints (in addition to having marginals µCi
) on the π ∈ Γ(µC1, . . . , µCk
) that characterizes maximal dependence
(for example π should be in the same copula family as µC). Strictly speaking, we can have a different GC for every copula C, even if the marginals are the same.

Regarding axioms (A4) and (A8), we make the following remark.

Remark 1. While (2) does not satisfy axiom (A4) in general (that is for every possible choice of GC), there might still be some specific choices for GC such that (A4) is satisfied. We illustrate this further in Example 1.

Also, when considering Cn → C uniformly as n → ∞, axiom (A8) can be satisfied by (2) under some extra constraints. The numerator converges if GC is chosen such that C 7→ supπ∈GC
Td1,...,dk
(π; ν1, . . . , νk) is continuous
(considering the uniform metric on the space of copulas). In Section 3, we see that this holds in the class of Gaussian copulas when taking GC = Γ(µC1, . . . , µCk
).

We now arrive at a natural generalization of the Wasserstein dependence coefficients of [36], which come from (2)
with two particular choices of reference measures.

Definition 1. For m ∈ Z>0, let γm denote the measure of an m-variate Gaussian copula with identity correlation matrix
(i.e., the m-variate independence copula). For q = d1+· · ·+dk with d1, . . . , dk ∈ Z>0 and for µC ∈ GC ⊂ Γ(µC1, . . . , µCk
),
where GC is W2-compact and non-degenerate µCi ∈ P(I
di) for i = 1, . . . , k, define

D d1,...,dk 1(µC) = D(µC; γd1, . . . , γdk ) =W2 2 (µC, γq) −Pk i=1 W2 2 (µCi, γdi ) supπ∈GC W2 2 (π, γq) −Pk i=1 W2 2 (µCi, γdi ) D d1,...,dk 2(µC) = D(µC; µC1, . . . , µCk ) =W2 2 (µC, µC1 × · · · × µCk ) supπ∈GC W2 2 (π, µC1 × · · · × µCk ). 3
If the context is clear, we just write Dr(µC) for r ∈ {1, 2}, or also Dr(X1; · · · ; Xk) to emphasize that we are measuring the dependence between k random vectors (having joint copula C).

Let us consider an example illustrating that D does not necessarily satisfy Axiom (A4) in general.

Example 1. Consider a random vector (X1, X2, X3) having a trivariate Gaussian copula µC with correlation matrix

$$\mathbf{R}={\begin{pmatrix}1&\rho&0\\ \rho&1&0\\ 0&0&1\end{pmatrix}},\quad{\mathrm{~where~}}-1\leq\rho\leq1.$$
$-2\sqrt{3}$
Let µCi be the marginal copula measure of Xi for i = 1, 2, 3, which in this case is in fact the Lebesgue measure corresponding to a U[0, 1] distribution. The product measure µC1 ×µC2 ×µC3 is the three dimensional independence copula, being equal to the trivariate Gaussian copula with identity correlation matrix I3. Also note that X3 is independent of
(X1, X2). One can quickly check that (using (3), see further)

$$\mathcal{D}_{2}(X_{1};X_{2};X_{3})=\frac{W_{2}^{2}(\mu_{C};\mu_{C_{1}}\times\mu_{C_{2}}\times\mu_{C_{3}})}{\sup_{\pi\in G_{C}}W_{2}^{2}(\pi,\mu_{C_{1}}\times\mu_{C_{2}}\times\mu_{C_{3}})}=\frac{4-2\sqrt{1-\rho}-2\sqrt{1+\rho}}{\sup_{\pi\in G_{C}}W_{2}^{2}(\pi,\mu_{C_{1}}\times\mu_{C_{2}}\times\mu_{C_{3}})}.$$

The remaining question is what to pick for GC, i.e., which quantity do we put in the denominator and defines the maximal amount of dependence. Well, if GC = Γ(µC1, µC2, µC3
), we should find the squared 2-Wasserstein distance between the independence copula and any other trivariate distribution having µC1, µC2 and µC3 as marginals, that is every possible trivariate copula. This is, as far as we are concerned, an open problem. However, in this context, it is reasonable to restrict GC to the Gaussian copula family. Doing so, one has supπ∈GCW2 2
(π, µC1 × µC2 × µC3
) = W2 2
(µCco , µC1 × µC2 × µC3
) = 6 − 2
√
3, where µCco stands for the comonotonicity copula measure, i.e., the limit of an equicorrelated (R = (1 − ρ)I3 + ρ131 T 3
,
where 1 T
3
= (1, 1, 1) and ρ ∈ (−1/2, 1)) Gaussian copula with correlation ρ tending to 1. With this choice of GC,
(X1, X2, X3) can never reach the maximum dependence, since 4 − 2p1 − ρ − 2p1 + ρ ≤ 4 − 2
√
2 < 6 − 2
√
3.

Another way to put it, is that

 $\blacksquare$
$\huge1-2\sqrt{1-a}$ 3. 
$$\mathcal{D}_{2}(X_{1};X_{2};X_{3})=\frac{2-\sqrt{1-\rho}-\sqrt{1+\rho}}{3-\sqrt{3}}<\frac{2-\sqrt{1-\rho}-\sqrt{1+\rho}}{2-\sqrt{2}}=\mathcal{D}_{2}(X_{1};X_{2}),$$
where D2(X1; X2) is computed in a similar way, also restricting the couplings Γ(µC1, µC2
) to Gaussian ones. We thus see that, when adding an independent component X3 into consideration, the dependence has decreased and hence axiom (A4) is definitely not fulfilled. Taking a look at R, it is maybe more tempting to have maximal dependence when |ρ| = 1 and restrict GC further to only those π ∈ Γ(µC1, µC2, µC3
) that are Gaussian and furthermore satisfy π(B1 × B2 × B3) = π(B1 × B2 × I) · π(I × I × B3) for all B1, B2, B3 ∈ B(I). Then, it is quickly seen that supπ∈GCW2 2
(π, µC1 × µC2 × µC3
) = 2 −
√
2, and hence D2(X1; X2; X3) = D2(X1; X2), in harmony with axiom (A4). So, for actual computation, it is better to restrict GC to the Gaussian copula family, and if some additional information is given (like zeroes in the correlation matrix), incorporating this in GC can lead to a more interpretative dependence quantification.

Except for some families like normal distributions, computing the Wasserstein distance is very involved and tools and theory for statistical inference are still scarce. The authors of [36] give an overview of the literature so far, concluding that additional theory is still needed, and propose a quasi-Gaussian (based on covariance matrices) approach instead. We assume that the copula of X is Gaussian.

4

## 3. A Gaussian Copula Approach

In this section, we assume a Gaussian copula model for X, elaborate more on maximal dependence, and discuss statistical inference within this framework.

3.1. The Bures-Wasserstein distance The main incentive is the well-known formula for the squared 2-Wasserstein distance between Gaussian distributions, say with covariance matrices R and S, becoming the so-called squared Bures-Wasserstein distance (see, e.g.,
[45]) between R and S:
d 2 W (R, S) = tr(R) + tr(S) − 2tr R
1/2SR1/21/2, (3)
were tr stands for the trace of a matrix. We denote by S
q = {R ∈ R
q×q: R
T = R} the set of symmetric q × q matrices, S

q
≥ ⊂ S
qthe set of positive semi-definite ones and S
q
> ⊂ S
q
≥
the set of positive definite ones. Let again q = d1 + · · · + dk and consider Rii ∈ S
di
≥
for i = 1, . . . , k. We also define the set

$$\Gamma(\mathbf{R}_{11},\ldots,\mathbf{R}_{k k})=\left\{\mathbf{A}\in\mathbb{S}_{\geq}^{q}:\mathbf{A}={\begin{pmatrix}\mathbf{R}_{11}\\ \Psi_{12}^{\mathrm{T}}\\ \vdots\\ \Psi_{1k}^{\mathrm{T}}\end{pmatrix}}\right.$$
1k Ψ
$$\left.\begin{array}{l l l}{{\Psi_{12}}}&{{\cdots}}&{{\Psi_{1k}}}\\ {{\mathbf{R}_{22}}}&{{\cdots}}&{{\Psi_{2k}}}\\ {{\vdots}}&{{\ddots}}&{{\vdots}}\\ {{\Psi_{2k}^{\mathrm{T}}}}&{{\cdots}}&{{\mathbf{R}_{k k}}}\end{array}\right\}\ ,$$

as the set of all covariance matrices of random vectors Z = (Z1, . . . ,Zk) such that the covariance matrix of Zi, being Rii, remains fixed for all i = 1, . . . , k and

$$\mathbf{r}\left\{\left(\mathbf{R}^{1/2}\mathbf{SR}^{1/2}\right)^{1/2}\right\}$$
$$\mathbf{R}_{0}={\begin{pmatrix}\mathbf{R}_{11}\\ \mathbf{0}_{12}^{\mathrm{T}}\\ \vdots\\ \mathbf{0}_{1k}^{\mathrm{T}}\end{pmatrix}}$$

$$(4)$$

R11 012 . . . 01k
12 R22 . . . 02k
............
1k0
2k. . . Rkk
, (4)
$$\begin{array}{r l}{{\mathbf{0}_{12}}}&{{}}&{{}}\\ {\mathbf{R}_{22}}&{{}}&{{}}\\ {\vdots}&{{}}&{{}}\\ {\vdots}&{{}}&{{}}\\ {\mathbf{0}_{2k}^{\mathrm{T}}}&{{}}&{{}}\end{array}$$
$$\left.\begin{array}{c}{{{\bf0}_{1k}}}\\ {{{\bf0}_{2k}}}\\ {{\vdots}}\\ {{{\bf R}_{k k}}}\end{array}\right\},$$

with 0i j ∈ R
di×dj a matrix of zeroes, as the covariance matrix when the Zi are all independent.

Consider now a random vector X = (X1, . . . , Xk) having a Gaussian copula with covariance matrix

$$\mathbf{R}={\begin{pmatrix}\mathbf{R}_{11}&\mathbf{R}_{12}&\dots\\ \mathbf{R}_{12}^{\mathrm{T}}&\mathbf{R}_{22}&\dots\\ \vdots&\vdots&\ddots\\ \mathbf{R}_{1k}^{\mathrm{T}}&\mathbf{R}_{2k}^{\mathrm{T}}&\dots\end{pmatrix}}$$

$$(S)$$
2k. . . Rkk
. (5)
$$\begin{array}{c}{{\mathbf{R}_{1k}}}\\ {{\mathbf{R}_{2k}}}\\ {{\vdots}}\\ {{\vdots}}\\ {{\mathbf{R}_{k k}}}\end{array}\Biggr|.$$

This means that (5) is the usual covariance matrix of the random vector Z = (Z1, . . . ,Zk), with Zi = (Zi1, . . . , Zidi
)
and Zi j = (Φ−1 ◦ Fi j)(Xi j) for i = 1, . . . , k and j = 1, . . . , di, where Fi j is the marginal distribution of Xi j and Φ−1the univariate standard normal quantile function. Measuring the dependence between X1, . . . , Xk can be done by utilizing the 2-Wasserstein dependence coefficients of Definition 1, now taking dW for W2.

Definition 2. For q = d1 + · · · + dk with d1, . . . , dk ∈ Z>0, R ∈ Γ(R11, . . . , Rkk) with Rii ∈ S
di
≥
\ {0} for i = 1, . . . , k and a dW -compact set GR ⊂ Γ(R11, . . . , Rkk) with R ∈ GR, define

$$\mathcal{D}_{1}(\mathbf{R};d_{1},\ldots,d_{k})=\frac{d_{W}^{2}(\mathbf{R},\mathbf{I}_{q})-\sum_{i=1}^{k}d_{W}^{2}(\mathbf{R}_{ii},\mathbf{I}_{d_{i}})}{\sup_{\mathbf{A}\in G_{\mathbf{R}}}d_{W}^{2}(\mathbf{A},\mathbf{I}_{q})-\sum_{i=1}^{k}d_{W}^{2}(\mathbf{R}_{ii},\mathbf{I}_{d_{i}})}$$ $$\mathcal{D}_{2}(\mathbf{R};d_{1},\ldots,d_{k})=\frac{d_{W}^{2}(\mathbf{R},\mathbf{R}_{0})}{\sup_{\mathbf{A}\in G_{\mathbf{R}}}d_{W}^{2}(\mathbf{A},\mathbf{R}_{0})},$$
where R0 is the matrix given in (4). If the context is clear, we also write Dr(R) or Dr(X1; · · · ; Xk) for r ∈ {1, 2}.
5 If the true copula is indeed Gaussian, the adequacy of the Bures-Wasserstein dependence remains, and we obtain something way more easy to handle. In order to make them fully practically usable, that is to say suitably attractive for estimation, we ought to find explicit expressions for the suprema in the denominator of the dependence measures.

When GR = Γ(R11, . . . , Rkk) and k = 2, the authors of [36] found elegant solutions to this problem, which we generalize to general k. 3.2. Maximal Bures-Wasserstein dependence We need the definition of majorization of two vectors and its behaviour under convex functions, as studied in [33].

Definition 3. For two vectors x, y ∈ R
q, we say that y majorizes x, denoted as x ≺ y, if

$$\begin{array}{l l}{{\left\{\begin{array}{l l}{{\sum_{i=1}^{\ell}x_{[i]}\leq\sum_{i=1}^{\ell}y_{[i]}}}&{{\mathrm{for~}\ell=1,\ldots,q-1}}\\ {{\sum_{i=1}^{q}x_{[i]}=\sum_{i=1}^{q}y_{[i]}}}\end{array}\right.,}}\end{array}$$

where x[1] ≥ · · · ≥ x[q] are the components of x in decreasing order, and similarly for y.

When λ and µ are the vectors of eigenvalues of two correlation matrices, λ being majorized by µ means that the proportion of the total variance explained by the ℓ first principal components is larger for the correlation matrix with eigenvalues µ, for any ℓ ∈ {1, . . . , q − 1}, than for the correlation matrix with eigenvalues λ. Fixing k covariance matrices R11, . . . , Rkk with Rii ∈ S
di
≥
, the goal is now to find Rm ∈ Γ(R11, . . . , Rkk) whose ordered eigenvalues majorize those of any matrix A ∈ Γ(R11, . . . , Rkk). Together with Lemma 2 (see Proposition 3.C.1 in [33]), this will enable us to characterize maximal dependence between k random vectors in terms of covariance matrices.

Lemma 2. If g : I → R is convex, with I ⊂ R *an interval, then*

$$\mathbf{x}<\mathbf{y}\quad\Longrightarrow\quad\sum_{i=1}^{q}g(x_{i})\leq\sum_{i=1}^{q}g(y_{i})$$
$$\left(7\right)$$

for all x, y ∈ I
q.

Since the 2-Wasserstein dependence coefficients satisfy axiom (A1), we can assume that d1 ≤ d2 ≤ · · · ≤ dk without loss of generality. Suppose that Rii = UiiΛiiU
T
ii (6)
is the eigendecomposition of Rii, i.e., with Λii = diag(λ1,ii, λ2,ii, . . . , λdi,ii) the di × di diagonal matrix with di ordered eigenvalues λ1,ii ≥ λ2,ii ≥ · · · ≥ λdi,ii on the diagonal (counting multiplicities), and Uii an orthogonal matrix containing the corresponding eigenvectors for i = 1, . . . , k. The proof of Proposition 2, and all other theoretical results of Section 3, are provided in Appendix C.

Proposition 2. Let Rii ∈ S
di
≥
have eigendecomposition (6) *for i* = 1, . . . , *k. Define the matrix* Rm as

$$\mathbf{R}_{m}={\begin{pmatrix}\mathbf{R}_{11}&\mathbf{\Psi}_{12}&\dots&\mathbf{\Psi}_{1k}\\ \mathbf{\Psi}_{12}^{T}&\mathbf{R}_{22}&\dots&\mathbf{\Psi}_{2k}\\ \vdots&\vdots&\ddots&\vdots\\ \mathbf{\Psi}_{1k}^{T}&\mathbf{\Psi}_{2k}^{T}&\dots&\mathbf{R}_{k k}\end{pmatrix}}\in\mathbb{R}^{q\times q},$$

, (7)
_with $q=d_{1}+\cdots+d_{k}$ and $d_{1}\leq d_{2}\leq\cdots\leq d_{k}$, and off-diagonal blocks._
$$\Psi_{i j}=\mathbf{U}_{i i}\mathbf{A}_{i i}^{1/2}\Pi_{i j}\mathbf{A}_{j j}^{1/2}\mathbf{U}_{j j}^{T}\in\mathbb{R}^{d_{i}\times d_{j}},$$
$$\mathbf{f}_{0}$$
$$\mathbf{\Pi}_{i j}={\left(\begin{array}{l l}{\mathbf{I}_{d_{i}}}&{\mathbf{0}_{d_{i}\times(d_{j}-d_{i})}}\end{array}\right)}\in\mathbb{R}^{d_{i}\times d_{j}},$$
$$w/h e r e$$

the di × dj upper left block of Idi+dj for i = 1, . . . , k, j = i + 1, . . . , k (denoting 0di×(dj−di)for the di × (dj − di) matrix of zeroes). If we define λj,ii = 0 *for j* = di + 1, . . . , q, the eigenvalues of Rm are

$$\lambda(\mathbf{R}_{m})=(\lambda_{j,11}+\lambda_{j,22}+\cdots+\lambda_{j,k k})_{j=1}^{q}.$$
j=1. (8)
Furthermore, for any A ∈ Γ(R11, . . . , Rkk) *with eigenvalues* λ(A) = (λj)
q j=1
, it holds that λ(A) ≺ λ(Rm).

Example 2 gives the matrix Rm for some specific cases.

Example 2. Some expressions for Rm in case k = 2 can be found in [36]. If di = 1 with Rii = 1 for all i = 1, . . . , k, the matrix Rm is obviously given by 1q×q, a matrix full of ones. Consider next Zi = (Zi1, Zi2) for i = 1, . . . , k, i.e., k bivariate random vectors, with covariance matrix of (Zi1, Zi2) given by

$$\mathbf{R}_{i i}=\begin{pmatrix}1&\rho_{i}\\ \rho_{i}&1\end{pmatrix}.$$

ρi 1 Assuming ρi, ρj ≥ 0, one can check that Ψi j of Rm in (7) for i = 1, . . . , k − 1 and j = i + 1, . . . , k is given by

$$\Psi_{i j}=\left(\frac{\sqrt{1+\rho_{i}}\,\sqrt{1+\rho_{j}}+\sqrt{1-\rho_{i}}\,\sqrt{1-\rho_{j}}}{2}\quad\frac{\sqrt{1+\rho_{i}}\,\sqrt{1+\rho_{j}}-\sqrt{1-\rho_{i}}\,\sqrt{1-\rho_{j}}}{2}\right),$$
2
$$(9)$$
$$\frac{\mathrm{Corr}(Z_{i1},Z_{j1})}{\overline{{Z_{i2}}}}$$
$1_{+}\cdot\cdot\cdot\cdot$, $k-1$ and $j=i+1_{+}\cdot\cdot\cdot$, $k$ is given 
$(Z_3,\,Z_2)+$
2
The result is similar in case ρi ≤ 0 or ρj ≤ 0 up to some signs (orthogonal transformations, to which dW is invariant).

The principal components of (Zi1, Zi2) are

$$Y_{i1}=\frac{1}{\sqrt{2}}(Z_{i1}+Z_{i2})\;\;\mathrm{and}\;\;Y_{i2}=\frac{1}{\sqrt{2}}(Z_{i2}-Z_{i1}),$$

corresponding to the eigenvalues 1 + ρi ≥ 1 − ρi respectively, with

  ## 1 Introduction  The _Fractional State_ of the Universe is a fundamental problem in cosmology. The _Fractional State_ of the Universe is a fundamental problem in cosmology.  
Corr(Zi2, Zj2) + Corr(Zi2, Zj1) + Corr(Zi1, Zj2) + Corr(Zi1, Zj1)
√1 + Corr(Zi1, Zi2)p1 + Corr(Zj1, Zj2)
and
A quick check then verifies that if ((Z11, Z12), . . . ,(Zk1, Zk2)) has correlation matrix Rm with blocks (9), it holds that
Corr(Yi1, Yj1) = Corr(Yi2, Yj2) = 1 for all i = 1, . . . , k − 1 and j = i + 1, . . . , k, i.e., all first principal components are
$$\mathrm{Corr}(Y_{i2},Y_{j2})={\frac{\mathrm{Corr}(Z_{i2},Z_{j2})-\mathrm{Corr}(Z_{i2},Z_{j1})-\mathrm{Corr}(Z_{i1},Z_{j2})+\mathrm{Corr}(Z_{i1},Z_{j1})}{2\,{\sqrt{1-\mathrm{Corr}(Z_{i1},Z_{i2})}}\,{\sqrt{1-\mathrm{Corr}(Z_{j1},Z_{j2})}}}}.$$
perfectly correlated and all second principal components as well.

Proposition 3 states that the matrix Rm in (7) maximizes the intensity of dependence, i.e., D1(Rm) = D2(Rm) = 1 when taking GR = Γ(R11, . . . , Rkk) for fixed marginal covariance matrices R11, . . . , Rkk.

Proposition 3. *Let q* = d1 + · · · + dk and Rii ∈ S
di
≥
for i = 1, . . . , *k. The matrix* Rm in (7) maximizes dW (R,Iq) and dW (R, R0) with R0 *given in* (4) *among all* R ∈ Γ(R11, . . . , Rkk).

A general interpretation of Rm is given in Remark 2. .

Remark 2. Assuming again that d1 ≤ d2 ≤ · · · ≤ dk, the matrix Rm in (7) is the covariance matrix of

$$\left(\begin{array}{c}{{\mathbf{U}_{11}\mathbf{A}_{11}^{1/2}\mathbf{Z}_{1}}}\\ {{\mathbf{U}_{22}\mathbf{A}_{22}^{1/2}\mathbf{Z}_{2}}}\\ {{\vdots}}\\ {{\mathbf{U}_{k k}\mathbf{A}_{k k}^{1/2}\mathbf{Z}_{k}}}\end{array}\right)\in\mathbb{R}^{q\times1},$$
7
where Z1 = (Z11, . . . , Z1d1
)
T
,Z2 = (Z21, . . . , Z2d2
)
T
, . . . ,Zk = (Zk1, . . . , Zkdk
)
Tsuch that for all i = 1, . . . , k we have Zi ∼ Ndi
(0di,Idi
), and in addition Zi j = Z(i+1)j for all i = 1, . . . , k − 1, j = 1, . . . , di, i.e., Zi and Zj have the first min{di, dj} components in common for all i, j ∈ {1, . . . , k}. The correlation matrix of the principal components of U11Λ
1/2 11 Z1, . . . , UkkΛ
1/2 kk Zk is

$$\begin{array}{r l r l}{\left(\mathbf{I}_{d_{1}}^{\mathrm{T}}&{}&{}\mathbf{\Pi}_{12}&{}\ldots&{}\mathbf{\Pi}_{1k}\right)}\\ {\left(\mathbf{\Pi}_{12}^{\mathrm{T}}&{}\mathbf{I}_{d_{2}}&{}\ldots&{}\mathbf{\Pi}_{2k}\right)}\\ {\vdots}&{}&{{}\vdots}&{}&{{}\ddots}&{}\\ {\mathbf{\Pi}_{1k}^{\mathrm{T}}}&{}\mathbf{\Pi}_{2k}^{\mathrm{T}}&{}\ldots&{}\mathbf{\Pi}_{d_{k}}\end{array}\right),$$

with Πi j as in Proposition 2. Hence, if (X1, . . . , Xk) has a Gaussian copula with covariance matrix Rm, then for ℓ = 1, . . . , min{di, dj} the ℓ-th principal components of ((Φ−1◦Fi1)(Xi1), . . . ,(Φ−1◦Fidi
)(Xidi
)) and ((Φ−1◦Fj1)(Xj1), . . . ,
(Φ−1 ◦ Fjdj
)(Xjdj
)) are perfectly correlated for all i, j ∈ {1, . . . , k}. This is the interpretation of maximal dependence for the Bures-Wasserstein dependence measures.

In the upcoming section, we also assume that GR = Γ(R11, . . . , Rkk).

3.3. Statistical inference In practice, we have an i.i.d. sample X
(ℓ) = (X
(ℓ)
1, . . . , X
(ℓ)
k
) for ℓ = 1, . . . , n from X, where X
(ℓ)
i= (X
(ℓ)
i1, . . . , X
(ℓ)
idi
)
for ℓ = 1, . . . , n is a sample from Xi for i = 1, . . . , k. A natural estimator for the Gaussian copula covariance matrix is known as the matrix of sample normal scores rank correlation coefficients (see, e.g., [24]),

$$\widetilde{\mathbf{R}}_{n}=\begin{pmatrix}\widetilde{\mathbf{R}}_{11}&\widetilde{\mathbf{R}}_{12}&\cdots&\widetilde{\mathbf{R}}_{1k}\\ \widetilde{\mathbf{R}}_{11}^{T}&\widetilde{\mathbf{R}}_{22}&\cdots&\widetilde{\mathbf{R}}_{2k}\\ \vdots&\vdots&\ddots&\vdots\\ \widetilde{\mathbf{R}}_{1k}^{T}&\widetilde{\mathbf{R}}_{2k}^{T}&\cdots&\widetilde{\mathbf{R}}_{kk}\end{pmatrix}\ \ \text{with}\ \ (\widetilde{\mathbf{R}}_{nn})_{jk}=\widetilde{\rho}_{ij,nn}=\frac{\frac{1}{n}\sum_{t=1}^{n}\widetilde{Z}_{ij}^{(t)}\widetilde{Z}_{nn}^{(t)}}{\frac{1}{n}\sum_{t=1}^{n}\left(\Phi^{-1}\left(\frac{t}{n+1}\right)\right)^{2}},\tag{10}$$

defined by computing normal scores

$$\widehat{Z}_{i j}^{(\ell)}=\Phi^{-1}\left(\frac{n}{n+1}\widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)\right)$$

obtained through the empirical cdf Fbi j(xi j) =
1 n Pn ℓ=1 1{X
(ℓ)
i j ≤ xi j} for i = 1, . . . , k and j = 1, . . . , di. The quantity bρi j,mt is calculated as the conventional Pearson correlation of the bivariate scores ((Zb(1)
i j , Zb(1)
mt ), . . . ,(Zb(n)
i j , Zb(n)
mt )) and by observing that

$$\frac{1}{n}\sum_{\ell=1}^{n}\widetilde{Z}_{i j}^{(\ell)}=\frac{1}{n}\sum_{\ell=1}^{n}\Phi^{-1}\left(\frac{\ell}{n+1}\right)=0\ \ \mathrm{and}\ \ \frac{1}{n}\sum_{\ell=1}^{n}\left(\widetilde{Z}_{i j}^{(\ell)}\right)^{2}=\frac{1}{n}\sum_{\ell=1}^{n}\left\{\Phi^{-1}\left(\frac{\ell}{n+1}\right)\right\}^{2},$$

which holds because Φ−1(α) = −Φ−1(1−α) for α ∈ [0, 1] and nFbi j(X
(ℓ)
i j ) is the rank of X
(ℓ)
i j in the sample X
$\mathbf{z}\;X^{(1)}_{ij},\ldots,X^{(n)}_{ij}$
i j , . . . , X
(n)
i j .

A next natural step in estimating Dr(R) is to plug in Rbn for the unknown R. Define the map φ by φ(Σ) =
D
−1/2 ΣΣD
−1/2 Σfor Σ ∈ S
q, where DΣ is the diagonal matrix containing the diagonal of Σ, and let ||Σ||F = tr1/2(Σ
TΣ) be the Frobenius norm. Frechet di ´ fferentiability of the mapping
(S
q
, || · ||F) → (R, | · |) : Σ 7→ (Dr ◦ φ)(Σ)
on S
q
>suffices in order for the delta method to transform an asymptotic normality result for Rbn into an asymptotic normality result for Dr(Rbn). We first highlight some notation. We assume d1 ≤ d2 ≤ · · · ≤ dk, the matrix Rm is again defined by (7) based on the eigendecompositions Rii = UiiΛiiU
T
ii as in (6), and R0 is the matrix in (4). Further, let Pi =0di×d1
· · · 0di×di−1 Idi 0di×di+1
· · · 0di×dk
∈ R
di×q(11)
be the projection matrix onto the di coordinates, satisfying Rii = PiRPT
i
. Partition the matrix Λii as

$$\mathbf{\Lambda}_{ii}=\begin{pmatrix}\mathbf{\Lambda}_{ii,1}&\mathbf{0}_{d_{1}\times(d_{2}-d_{1})}&\cdots&\mathbf{0}_{d_{1}\times(d_{i}-d_{i-1})}\\ \mathbf{0}_{d_{1}\times(d_{2}-d_{1})}^{\mathsf{T}}&\mathbf{\Lambda}_{ii,2}&\cdots&\mathbf{0}_{(d_{2}-d_{1})\times(d_{2}-d_{i-1})}\\ \vdots&\vdots&\ddots&\vdots\\ \mathbf{0}_{d_{1}\times(d_{i}-d_{i-1})}^{\mathsf{T}}&\mathbf{0}_{(d_{2}-d_{1})\times(d_{i}-d_{i-1})}^{\mathsf{T}}&\cdots&\mathbf{\Lambda}_{ii,i}\end{pmatrix}\in\mathbb{R}^{d_{i}\times d_{i}},$$
$$\quad(12)$$
, (12)
with Λii, j ∈ R
(dj−dj−1)×(dj−dj−1)for j = 1, . . . , i and defining d0 = 0. Based on these partitions, further define
∆1 =Λ11,1 + Λ22,1 + · · · + Λkk,1−1/2∈ R d1×d1 e∆1 = Λ 2 11,1 + Λ 2 22,1 + · · · + Λ 2 kk,1 −1/2Λ11,1 ∈ R d1×d1 ∆i =  ∆i−1 0di−1×(di−di−1) 0 T di−1×(di−di−1)Λii,i + Λ(i+1)(i+1),i + · · · + Λkk,i−1/2 !∈ R di×di e∆i = e∆i−1Di 0di−1×(di−di−1) 0 T di−1×(di−di−1)Λ 2 ii,i + Λ 2 (i+1)(i+1),i + · · · + Λ 2 kk,i −1/2Λii,i  ∈ R di×di
$$(13)$$
$$(14)$$

for i = 2, . . . , k with Di = diag Λ
−1
(i−1)(i−1),1Λii,1, . . . , Λ
* [10] M. C. Gonzalez-Garcia, M. C. Gonzalez-Garcia, M.  
(i−1)(i−1),i−1Λii,i−1
di−1×di−1. Finally, we will need the matrices
$\mathbf{J}=\mathbf{R}_{0}^{-1/2}\left(\mathbf{R}_{0}^{1/2}\mathbf{R}\mathbf{R}_{0}^{1/2}\right)^{1/2}\mathbf{R}_{0}^{-1/2}=\begin{pmatrix}\mathbf{J}_{11}&\mathbf{J}_{12}&\cdots&\mathbf{J}_{1k}\\ \mathbf{J}_{21}&\mathbf{J}_{22}&\cdots&\mathbf{J}_{2k}\\ \vdots&\vdots&\ddots&\vdots\\ \mathbf{J}_{k1}&\mathbf{J}_{k2}&\cdots&\mathbf{J}_{kk}\end{pmatrix}\in\mathbb{R}^{q\times q}$
with Ji j ∈ R
di×dj and
J0 = diag(J11, . . . , Jkk) ∈ R
q×q
. (15)
Theorem 1 formally states an asymptotic normality result for the estimator Dr(Rbn).
Theorem 1. Let X *have a Gaussian copula with correlation matrix* R ∈ S
q
> with R , R0 *such that* Rii ∈ S
di
> has di
distinct eigenvalues, and let Rbn *be given by* (10) based on which the plug-in estimator Dbr,n = Dr(Rbn) *is constructed.*
Then for r ∈ {1, 2}*, it holds that*√n
$${\sqrt{n}}\left({\widehat{\mathcal{D}}}_{r,n}-{\mathcal{D}}_{r}(\mathbf{R})\right){\overset{d}{\to}}\,{\mathcal{N}}\left(\mathbf{0}_{q},\zeta_{r}^{2}\right)$$
as n → ∞*, with asymptotic variance* ζ 2 r = 2trhRMr − DMrR	2i, where DMrR is the diagonal matrix consisting of the diagonal of MrR*, and*

$${\bf M}_{1}=\frac{1}{2C_{1}}\left(-{\bf R}^{-1/2}+(1-{\cal D}_{1}({\bf R})){\bf R}_{0}^{-1/2}+{\cal D}_{1}({\bf R}){\bf Y}_{1}\right),\quad{\bf M}_{2}=\frac{1}{C_{2}}\left(-\frac{1}{2}\left({\bf J}_{0}+{\bf J}^{-1}\right)+(1-{\cal D}_{2}({\bf R}))\,{\bf I}_{\rm q}+{\cal D}_{2}({\bf R}){\bf Y}_{2}\right),$$
with
$$C_{1}=\sum_{i=1}^{k}t r\left(\mathbf{R}_{i i}^{1/2}\right)-t r\left(\mathbf{R}_{m}^{1/2}\right),\qquad\quad\mathbf{\Upsilon}_{1}=\begin{pmatrix}\mathbf{U}_{11}\mathbf{\Lambda}_{1}\mathbf{U}_{11}^{T}&\mathbf{\Phi}_{d_{1}\times d_{1}}&\cdots\\ \mathbf{\Phi}_{d_{1}\times d_{2}}^{T}&\mathbf{U}_{22}\mathbf{\Lambda}_{2}\mathbf{U}_{22}^{T}&\cdots\\ \vdots&\vdots&\vdots&\ddots\\ \mathbf{\Phi}_{d_{1}\times d_{k}}^{T}&\mathbf{\Phi}_{d_{2}\times d_{k}}^{T}&\cdots\end{pmatrix}$$
22 · · · 0d2×dk
d2×dk· · · Ukk∆kU
$$\begin{array}{c}{{{\bf0}_{d_{1}\times d_{k}}}}\\ {{{\bf0}_{d_{2}\times d_{k}}}}\\ {{\vdots}}\\ {{{\bf U}_{k k}{\bf\Lambda}_{k}{\bf U}_{k k}^{T}}}\end{array}$$

and

$$C_{2}=tr(\mathbf{R})-tr\left(\left(\mathbf{R}_{0}^{1/2}\mathbf{R}_{m}\mathbf{R}_{0}^{1/2}\right)^{1/2}\right),\mathbf{\Upsilon}_{2}=\begin{pmatrix}\mathbf{U}_{11}\widetilde{\mathbf{A}}_{1}\mathbf{U}_{11}^{T}&\mathbf{0}_{4\times24}&\cdots&\mathbf{0}_{4\times24}\\ \mathbf{0}_{4\times24}^{T}&\mathbf{U}_{22}\mathbf{A}_{2}\mathbf{U}_{22}^{T}&\cdots&\mathbf{0}_{6\times24}\\ \vdots&\vdots&\ddots&\vdots\\ \mathbf{0}_{4\times24}^{T}&\mathbf{0}_{4\times24}^{T}&\cdots&\mathbf{U}_{16}\widetilde{\mathbf{A}}_{4}\mathbf{U}_{46}^{T}\end{pmatrix}.\tag{17}$$
$$(16)$$

Remark 3. When R = R0, it holds that ζr = 0 and √nDbr,np−→ 0 for n → ∞. The higher-order delta method can however still provide a weak convergence result for nDbr,n. A detailed study of this is research in progress.

We look at another example, which is also studied in [12], but in the context of Φ-dependence measures.

Example 3. Consider a four dimensional random vector (X1, X2, X3, X4) having a Gaussian copula with covariance
matrix
$$\begin{pmatrix}1&\rho_{1}&\rho_{2}&\rho_{2}\\ \rho_{1}&1&\rho_{2}&\rho_{2}\\ \rho_{2}&\rho_{2}&1&\rho_{1}\\ \rho_{2}&\rho_{2}&\rho_{1}&1\end{pmatrix},\quad\text{where}\quad\rho_{1}\geq2|\rho_{2}|-1.\tag{1}$$
ρ2 ρ2 ρ1 1 Then one can check that (recall also Example 2 for finding the matrix Rm)

![9_image_0.png](9_image_0.png)

$$(18)$$
$$(19)$$
$$(20)$$
$$\mathcal{D}_{1}\left((X_{1},X_{2});(X_{3},X_{4})\right)=\frac{2(1+\rho_{1})^{1/2}-(\rho_{1}-2\rho_{2}+1)^{1/2}-(\rho_{1}+2\rho_{2}+1)^{1/2}}{\left(2-\sqrt{2}\right)\left[(1+\rho_{1})^{1/2}+(1-\rho_{1})^{1/2}\right]}$$
$$\mathcal{D}_{2}\left((X_{1},X_{2});(X_{3},X_{4})\right)=\frac{4-2\left|1-\rho_{1}\right|-\left(\rho_{1}^{2}+2\rho_{1}-2\rho_{1}\rho_{2}-2\rho_{2}+1\right)^{1/2}-\left(\rho_{1}^{2}+2\rho_{1}+2\rho_{1}\rho_{2}+2\rho_{2}+1\right)^{1/2}}{4-\sqrt{2}\left\{\left|1-\rho_{1}\right|+\rho_{1}+1\right\}}$$

2 {|1 − ρ1| + ρ1 + 1}. (20)
Fig. 1 shows how (19) and (20) depend on ρ2 for different values of ρ1. Clearly, independence holds if and only if ρ2 = 0, as it should. When ρ1 = 2|ρ2|−1, the second principal component of (Z1, Z2) = ((Φ−1 ◦F1)(X1), (Φ−1 ◦F2)(X2)) is perfectly correlated with the second principal component of (Z3, Z4) = ((Φ−1 ◦ F3)(X3), (Φ−1 ◦ F4)(X4)), where Fi is the marginal distribution of Xi for i = 1, 2, 3, 4, see also [12]. This causes the Φ-dependence measures studied in
[12] to reach their maximum value, because a singularity is attained. In particular, taking for instance ρ1 = −0.4 and ρ2 = 0.3, all (normalized) Φ-dependence measures equal 1, while D1 = 0.396 and D2 = 0.3. The reason for D1 and D2 still being small, is that ρ2 is pretty small and, recalling Remark 2, not both first and second principal components of (Z1, Z2) and (Z3, Z4) are perfectly correlated, only one of them is. Only when |ρ2| = 1 and thus also ρ1 = 1, we have D1 = D2 = 1. Maximal Bures-Wasserstein dependence is not attainable for the family (18) if ρ1 , 1, because it imposes additional restrictions on the correlations (i.e., not every element in Γ(R11, . . . , Rkk) is a member of (18)).

Picking a set GR ⊂ Γ(R11, . . . , Rkk) for a normalization that adjusts according to these restrictions, would lead to more cases of maximal dependence.

10 and