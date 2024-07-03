On Regression in Extreme Regions Stephan Cl´emen¸con, Nathan Huet, Anne Sabourin April 11, 2024 Abstract In the classic regression problem, the value of a real-valued random variable Y is to be predicted based on the observation of a random vector X. The statistical learning problem consists in building a predictive function ˆf based on independent copies of (*X, Y* ) so that Y is approximated by ˆf(X) with minimum (squared)
error. Motivated by various applications, special attention is paid here to the case of extreme (*i.e.* very large) observations X. Because of their rarity, the contributions of such observations to the (empirical) error is negligible, and the predictive performance of empirical risk minimizers can be consequently very poor in extreme regions. In this paper, we develop a general framework for regression on extremes. Under appropriate regular variation assumptions regarding the pair (*X, Y* ), we show that an asymptotic notion of risk can be tailored to summarize appropriately predictive performance in extreme regions. It is also proved that minimization of an empirical and nonasymptotic version of this 'extreme risk', based on a fraction of the largest observations solely, yields good generalization capacity. In addition, numerical results providing strong empirical evidence of the relevance of the approach proposed are displayed.

## Contents 1

1 Introduction 2

| 2   | A Regular Variation Framework for Regression                                 | 3   |    |
|-----|------------------------------------------------------------------------------|-----|----|
| 2.1 | Least Squares Minimization on Extremes - Algorithm                           |     | 4  |
| 2.2 | Background on Multivariate Regular Variation                                 |     | 4  |
| 2.3 | Regular Variation with respect to the First Component                        |     | 5  |
| 3   | Regression on Extremes - Main Results                                        | 8   |    |
| 3.1 | Structural Analysis of Minimizers: Conditional, Asymptotic and Extreme Risks | 8   |    |
| 3.2 | Statistical Learning Guarantees                                              | 9   |    |
| 4   | Numerical Experiments                                                        | 12  |    |
| 4.1 | Simulated data                                                               |     | 12 |
| 4.2 | Real data                                                                    |     | 14 |
| 5   | Conclusion                                                                   | 15  |    |
| A   | Multivariate Regular Variation w.r.t. the First Component                    | 17  |    |
| B   | Proofs for Section 2                                                         | 18  |    |
| B.1 | Proof of Proposition 1                                                       |     | 18 |
| B.2 | Proofs and Additional Results regarding Example 1                            |     | 20 |
| B.3 | Proofs regarding Example 2                                                   | 21  |    |
| C   | Proofs for Section 3                                                         | 25  |    |
| C.1 | Proof of Theorem 1                                                           | 25  |    |
| C.2 | Proof of Theorem 2                                                           | 26  |    |
| C.3 | Proof of Proposition 2                                                       |     | 28 |

arXiv:2303.03084v2 [stat.ML] 10 Apr 2024

## 1 Introduction

Regression is a predictive problem of crucial importance in statistical learning, covering a wide variety of applications. In the standard setup, (*X, Y* ) is a pair of random variables defined on the same probability space (Ω, A, P)
with distribution P, where the target Y is a square integrable real-valued random variable (the output) and the predictor (or covariable) X is a random vector with marginal distribution ρ taking its values in some measurable space X modeling some input information hopefully useful to predict Y . The predictive learning problem consists in building, from a training dataset Dn = {(X1, Y1), . . . , (Xn, Yn)} composed of n ≥ 1 independent copies of (*X, Y* ),
a mapping f : X → R in order to compute a 'good' prediction f(X) for Y , with the quadratic risk

$$R_{P}(f)=\mathbb{E}\left[\left(Y-f(X)\right)^{2}\right]$$
$\left(1\right)$. 
h(Y − f(X))2i(1)
as close as possible to that of f
∗(X) = E[Y | X], which obviously minimizes (1) over the space L2(ρ) of square integrable functions of X: R∗P
:= minf∈L2(ρ) RP (f) = RP (f
∗). A natural strategy consists in solving the Empirical Risk Minimization problem (ERM in abbreviated form) minf∈F RPˆn
(f), where F ⊂ L2 (ρ) is a closed and convex class of functions sufficiently rich to include a reasonable approximant of f
∗ and Pˆn is an empirical version of P
based on Dn.

The performance of predictive functions ˆf obtained this way, by *least-square regression*, has been extensively investigated in the statistical learning literature [31, 40]. Under the assumption that the tails of the random pairs
(f(X), Y ) are subgaussian and appropriate complexity conditions are satisfied by the class F, confidence upper bounds for the excess of quadratic risk RP (
ˆf) − R∗P = E[(Y − ˆf(X))2| Dn] − R∗P have been established in [36] by means of concentration inequalities for empirical processes [6].

Here we consider the problem of building prediction functions which would be reliable in a a 'crisis scenario' where the covariates vector takes unusually large values and thus belongs to regions where few or even no such large examples have been observed in the past. Notice incidentally that it could be thus viewed as a specific, never tackled yet, *few shot learning problem*, see *e.g.* [56]. We place ourselves in a finite-dimensional setting, X ⊂ R
d.

The distribution of X is not subgaussian and in particular its support is unbounded. Covariates are considered as extreme when their norm ∥X∥ exceeds some (asymptotically) large threshold t > 0. The choice of the norm is unimportant in theory, and is typically determined by the application context.

The threshold t depends on the observations, since 'large' should be naturally understood as large with respect to the vast majority of data observed. Hence, extreme observations are rare by nature and severely underrepresented in the training dataset with overwhelming probability. Consequently, the impact of prediction errors in extreme regions of the input space on the global regression error of ˆf is generally negligible. Indeed, the law of total probability yields

$$R_{P}(f)=\mathbb{P}\{\|X\|\geq t\}\mathbb{E}\left[(Y-f(X))^{2}\mid\|X\|\geq t\right]+\mathbb{P}\{\|X\|<t\}\mathbb{E}\left[(Y-f(X))^{2}\mid\|X\|<t\right].\tag{2}$$

The above decomposition involves a conditional error term relative to excesses of ∥x∥ above t, which we term Conditional quadratic risk (or simply *Conditional risk*)

$$R_{t}(f):=\mathbb{E}\left[\left(Y-f(X)\right)^{2}\mid\|X\|\geq t\right].$$

It is the purpose of the subsequent analysis to construct a predictive function ˆf that (approximately) minimizes Rt(f) for all *t > t*0, with t0 being a large threshold. It is important to note that an approximate minimizer of Rt might not be suitable for minimizing Rt
′ when t
′ > t. To ensure robust extrapolation performance for our learned function, we focus on obtaining a prediction function, ˆf, that minimizes the *asymptotic conditional quadratic risk* defined as R∞(f) := lim sup t→+∞
Rt(f) = lim sup t→+∞
E
-(Y − f(X))2| ∥X∥ ≥ t. (3)
It is immediate to see that any function that coincides with the regression function f
∗(x) = E [Y | X = x] on the region {x ∈ X , ∥x∥ ≥ t} minimizes the risk functional Rt, for all t > 0, and thus also R∞. In other words R∗∞ := inff R∞(f) = R∞(f
∗). However, even though f
∗ provides a straightforward theoretical solution, f
∗is of course unknown.

In view of Equation (2) it is evident that an estimate ˆf of f
∗ produced by an ERM strategy with good overall empirical performances, may not necessarily enjoy good performances when restricted to extreme regions. Put another way, there is no guarantee that the conditional risk Rt( ˆf) (or R∞(
ˆf)) would be small. However, accurate prediction in extreme regions turns out to be crucial in certain practical (safety) applications, in environmental sciences, dietary risk analysis or finance/insurance for instance.

To summarize, the *Regression Problem on Extremes* refers here to the the task of constructing a prediction function ˆf based on Dn which approximately minimizes R∞. Notice that our choice of the squared error is motivated by simplicity and for illustrative purpose, extensions to other losses may be achieved at the price of additional
(minor) technicalities.

In order to develop a specific ERM framework relative to R∞ with provable guarantees, regularity assumptions are required regarding the tail behavior of the pair (*X, Y* ), with respect to the first component. *Multivariate regular* variation hypotheses are very flexible in the sense that they correspond to a large nonparametric class of heavytailed distributions. These assumptions, or slightly weaker ones such as *Maximum domain of attraction* conditions are at the heart of Extreme Value Analysis (EVA) (*e.g.*, the monographs [5, 18, 49]). They are frequently used in applications where the impact of extreme observations should be enhanced, or not neglected at the minimum.

Statistical learning approaches in EVA have recently garnered significant interest, particularly in unsupervised learning contexts. Examples include dimensionality reduction through multiple subspace clustering in [28, 29, 13, 50, 43, 44], as well as Principal Component Analysis in [15, 20]. In addition, there has been notable exploration in clustering methods [35, 55], graphical models [24], and applications such as Anomaly Detection [12, 54], to name just a few. In the supervised setting, unlike the current study, the predominant focus in the literature revolves around predicting extreme values of the target variable Y [3] or tackling extreme quantile regression through methods such as gradient boosting [53] or random forests [26].

The work which is most related to ours is that of [34] (see also [14]), where an ERM framework for the (easier)
binary classification problem on extreme covariates is developed. Precisely, it is assumed therein that the two class distributions are multivariate regularly varying with the same tail index (see (5) in the background section 2.2),
and risk functionals Rt, R∞ are defined similarly with the 0-1 loss. One of the primary objectives of this paper is to establish sufficient and reasonable conditions for extending the results of [34] to a broader context encompassing statistical regression with a continuous target and an appropriate real-valued loss. It must be noted that the continuous nature of the target in the regression problem considered here requires fundamentally different assumptions and proof techniques compared with the binary classification setting. In particular one natural generalization of the assumptions made in the cited reference would be to assume regular variation of the conditional distributions L(X|Y = y), almost everywhere. This somewhat intricate generalization leads to measure theoretic complications and is difficult to verify in practice and also on theoretical examples. We propose to bypass this issue by requiring instead a joint form of regular variation of the pair (*X, Y* ), see our Assumption 2. We show that this condition is satisfied in various examples worked out in Section 2.3. Another major improvement of the present work upon [34],
with implications for applications related to climate extremes, is to offer a novel perspective upon extreme value prediction within regularly varying random vectors, see Example 2.

The paper is organized as follows. The algorithmic approach we propose for Regression on Extremes is detailed in Section 2, extending [34]'s framework in order to handle continuous targets. Key notions pertaining to multivariate extreme value theory (MEVT) are also briefly recalled for clarity's sake and the probability framework we consider for regression in extreme regions is described at length therein. In Section 3, we show that a predictive rule using the angular information only *i.e.* of the form f(X) = h(X/∥X∥), where h is a real-valued function defined the hypersphere S = {x ∈ R
d: ∥x∥ = 1} reaches the best possible performances w.r.t. the asymptotic risk.

Subsequently, we study the performance of a predictive rule based on a training sample {(X1, Y1), . . . , (Xn, Yn)}
composed of n ≥ 1 independent copies of the pair (*X, Y* ) and learned by minimizing an empirical version of (3) based on a fraction k/n of the training dataset, those corresponding to the largest ||Xi||'s. Nonasymptotic bounds for the excess of asymptotic risk of such an empirical (preasymptotic) risk minimizer are established, demonstrating its near optimality. Beyond these theoretical guarantees, the performance of empirical risk minimization on extreme covariates is supported by various numerical experiments displayed in Section 4. Some concluding remarks are collected in Section 5. In order to enhance readability, certain technical details are postponed to the Appendix section.

## 2 A Regular Variation Framework For Regression

In this section, we propose a probabilistic framework in which Regression on Extremes may be addressed, together with a dedicated algorithmic approach, the latter being analyzed next in the subsequent sections. Here and throughout, (*X, Y* ) is a pair of random variables defined on a probability space (Ω, A, P) with distribution P, where Y is real-valued with marginal distribution G and X = (X(1)*, . . . , X*(d)) takes its values in R
d, d ≥ 1. We sometimes denote by L(Z) the distribution of a random variable Z. Recall from the Introduction section that *∥ · ∥* is any norm on R
d. We denote by S the unit sphere for this norm and by B := {x ∈ R
d, ∥x∥ ≤ 1} the unit ball. Let E = R
d \ {0Rd } be the punctured Euclidean space. For any measurable subset A of R
d we denote by B(A) the trace Borel σ-field on A. The boundary and the closure of A are respectively denoted by ∂A and A¯, and we set tA = {tx : x ∈ A} for all t ∈ R. By 1{E} is meant the indicator function of any event E and the integer part of any u ∈ R is denoted by ⌊u⌋.

## 2.1 Least Squares Minimization On Extremes - Algorithm

In order to help the reader understand the general workflow of the paper, we begin immediately by introducing the algorithm that we promote to solve the Regression Problem on Extremes stated in the Introduction, formulated as the minimization of the risk functional R∞ defined in (3). The remainder of this work aims at developing a framework that fully justifies Algorithm 1 below.

## Algorithm 1 Least Squares Minimization On Extremes

INPUT: Training dataset Dn = {(X1, Y1), . . . , (Xn, Yn)} with (Xi, Yi) ∈ [0, +∞)
d × R, i = 1*, . . . , n*; class H
of predictive functions h : S → R; number k ≤ n of 'extreme' observations among training data.

Truncation: Sort the training data by decreasing order of magnitude of the input information ||X(1)|| ≥ . . . ≥
||X(n)|| and form a set of k *extreme training observations*

$$\left\{\left(X_{(1)},Y_{(1)}\right),\;\ldots,\;\left(X_{(k)},Y_{(k)}\right)\right\}.$$

Empirical quadratic risk minimization: based on the extreme training dataset, solve the optimization problem

$$\operatorname*{min}_{h\in\mathcal{H}}{\frac{1}{k}}\sum_{i=1}^{k}\left(Y_{(i)}-h\left(\theta\left(X_{(i)}\right)\right)\right)^{2},$$
k
$\left(4\right)$. 
2, (4)
where θ(x) = x/∥x∥ is the angular component of any point x ∈ R
d \ {0}.

OUTPUT: Solution hˆ to problem (4) and predictive function fb(x) = (hˆ ◦ θ)(x) to be used for predictions of Y
based on new examples X such that ∥X*∥ ≥ ∥*X(k)∥.

Notice that any algorithm for quadratic risk minimization can be used to solve (4), refer to *e.g.*, [31]. The study of dedicated numerical techniques is beyond the scope of the present paper.

A key feature of Algorithm 1 is that its training step involves the *angular* component of extremes solely.

It returns a prediction function fb which only depends on the angular component θ(X) of a new input X. This apparently arbitrary choice turns out to be fully justified under regular variation assumptions, which are introduced and discussed in the following subsections. To wit, the main theoretical advantage of considering angular prediction function is to ensure the convergence of the conditional risk Rt, as t → +∞. In practice, rescaling all extremes
(in the training set and in new examples) onto a bounded set allows a drastic increase in the density of available training examples and a clear extrapolation method beyond the envelope of observed examples.

After recalling some background on multivariate regular variation in subsection 2.2, we introduce a modified version of the standard framework (*regular variation with respect to the first component*) in subsection 2.3 which is suitable for the regression problem considered here, in the sense that Algorithm 1 turns out to enjoy probabilistic and statistical guarantees in this context. We thoroughly discuss the relevance of our assumptions by working out several sufficient conditions and examples. We state our main probabilistic results in subsection 3.1, establishing connections between different risks and their corresponding minimizers, thus bringing a first (probabilistic) justification regarding the angular nature of the prediction function in Algorithm 1. Statistical guarantees are deferred to subsection 3.2.

## 2.2 Background On Multivariate Regular Variation

The goal of heavy-tail analysis is to study phenomena that are not ruled by averaging effects but determined by extreme values. To investigate the behavior of a random vector X far from the center of its mass, an usual assumption is that X's distribution is *multivariate regularly varying* with tail index α > 0, *i.e.* there exist a nonzero Borel measure µ on E, finite on all Borel measurable subsets of E bounded away from zero and a *regularly varying* function b(t) with index α, *i.e.* b(tx)/b(t) → x α as t → +∞, such that for any Borel measurable set A ⊂ E bounded away from zero and such that µ(∂A) = 0. The latter convergence is referred to as vague convergence in [−∞, +∞]
d \ {0Rd } (see [49], sec. 3.4), or equivalently as M0-convergence in E
(see [33, 38]). The *limit measure* µ is provably homogeneous of degree −α: µ(tA) = t
−αµ(A) for all t > 0 and Borel set A ⊂ E bounded away from the origin. One may refer to [49] for alternative formulations/characterizations of the regular variation property and its application to MEVT. It follows from the homogeneity property that the pushforward measure of µ by the polar coordinates transformation x ∈ E 7→ (∥x∥, θ(x)) is the tensor product given by:
µ {x ∈ E : ∥x∥ ≥ *r, θ*(x) ∈ B} = r
−αΦ(A),
for all B ∈ B(S) and r ≥ 1, where Φ is a finite positive measure on S, referred to as the *angular measure* of the limit measure µ. The regular variation assumption (5) implies that the conditional distribution of (∥X∥*/t, θ*(X))
given ∥X∥ ≥ t converges as t → +∞: for all r ≥ 1 and B ∈ B(S) with Φ(∂B) = 0, we have

$\mathbb{P}\Big{\{}t^{-1}\|X\|\geq r,\theta(X)\in B\mid\|X\|\geq t\Big{\}}\underset{t\to+\infty}{\longrightarrow}c^{r-\alpha}\Phi(B)$,

where c = Φ(S)
−1 = µ(E \ B)
−1 Hence, the radial and angular components of the random variable X are asymptotically independent with standard Pareto distribution of parameter α and normalized angular measure cΦ as respective asymptotic marginal distributions. The angular measure Φ describes exhaustively the dependence structure of the components X(j)'s given that ∥X∥ is large, *i.e.* the directions θ(X) in which extremes occur with largest probability.

Heavy-tailed models have been the subject of much attention in the statistical machine-learning literature.

Among many other works, the regular variation assumption is used in [46] for rare event probability estimation, in [10] or [1] in the context of stochastic bandit problems, in [27] for the statistical recovery of the dependence structure in the extremes, in [29] for dimensionality reduction in extreme regions and in [8] for predictive problems with heavy-tailed losses.

## 2.3 Regular Variation With Respect To The First Component

We now describe rigorously the framework we consider for regression in extreme regions, which may be seen as a natural, 'one-component' extension of standard multivariate regular variation assumptions recalled in Section 2.2.

For simplicity, we suppose that Y is bounded through this paper. This assumption can be naturally relaxed at the price of additional technicalities (*i.e.* tail decay hypotheses).

Assumption 1 The random variable Y is bounded: there exists M ∈ (0, +∞) *such that with probability one,*
Y ∈ I = [−*M, M*].

The following hypothesis concerns the asymptotics, as t → +∞, of the conditional distribution of the pair (*X, Y* )
given that ∥X∥ > t. It may be viewed as one-component extension of (5).

Assumption 2 There exists a non null Borel measure µ on O = E × I*, which is finite on sets bounded away from* C = {0} × I, and a regularly varying function b(t) with index α > 0 *such that*

$$\operatorname*{lim}_{t\to+\infty}b(t)\mathbb{P}\left\{t^{-1}X\in A,Y\in C\right\}=\mu(A\times C),$$

−1X ∈ *A, Y* ∈ C	= µ(A × C), (6)
for all A ∈ B(E) bounded away from zero and C ∈ B(I) *such that* µ(∂(A × C)) = 0.

Assumption 2 could be understood as a multivariate extension of the *One-Component Regular Variation* framework developed in [32]. It should be noticed that Assumption 2 fits into the framework if Regular Variation in MO

developed in [38] as an extension of [33], where O = E ×I = (R
d ×I) \ ({0} ×I) and where the scalar multiplication is defined as λ(*x, y*) = (*λx, y*). More details regarding the connections between Assumption 2 and [38] are provided in the Supplementary Material, Section A. Remark 1 (Pre-Processing) Because the goal of this paper is to explain main ideas to tackle the problem of regression on extremes, the input are assumed to be regularly varying with same marginal index while in practice, this condition may be satisfied only after some marginal standardization. This is a recurrent theme in multivariate extreme value theory. For binary-valued Y *, in the classification setting, [14] consider a marginal standardization* based on ranks, following [21, 22]. They prove an upper bound on the statistical error term induced by this transformation which is of the same order of magnitude as the error when marginal distributions are known, a simplified case considered in [34]. In our experiments with real data, this pre-processing step is not necessary. We leave this technical question outside the scope of this paper.

$$(6)$$

In the sequel we refer to the limit measure µ as the *joint limit measure* of (*X, Y* ). Under Assumption 2, X's marginal distribution is regularly varying with *marginal limit measure*

$\mu_{X}(A)=\lim_{t\to+\infty}b(t)\mathbb{P}\left\{X\in tA\right\}=\lim_{t\to+\infty}b(t)\mathbb{P}\left\{X\in tA,Y\in I\right\}=\mu(A\times I)$,
with A ∈ B(E) bounded away from zero and such that µ(∂(A × I)) = 0. We also naturally introduce the *joint* angular measure of (*X, Y* ) denoted by Φ, which is a finite measure on S × I given by

$$\Phi(B\times C)=\mu\{(x,y)\in E\times I:\|x\|\geq1,\theta(x)\in B,y\in C\}.$$
Φ(B × C) = µ{(x, y) ∈ E × I : ∥x∥ ≥ 1, θ(x) ∈ *B, y* ∈ C}. (7)
With this notation, under Assumption 2 it holds that

$$\mathbf{r}\mathbf{\dot{j}}$$
$\mathbb{P}\{\theta(X)\in B,\,Y\in C,\,\|X\|\geq tr\}$$\mathbb{P}\{\|X\|\geq t\}$$\mathbb{P}\{\theta(X\times C),$  $\mathbb{P}\{\theta(X)\in B,\,Y\in C,\,\|X\|\geq tr\}$$\mathbb{P}\{\|X\|\geq t\}$$\mathbb{P}\{\theta(X\times C),$  $\mathbb{P}\{\theta(X)\in B,\,Y\in C,\,\|X\|\geq tr\}$$\mathbb{P}\{\|X\|\geq t\}$$\mathbb{P}\{\theta(X\times C),$ 
$$\mathbf{\Sigma}^{\dagger}$$

where c = Φ(S × I)
−1 = µ((E \ B) × I)
−1, for all C ∈ B(I), B ∈ B(S), such that Φ(∂(B × A)) = 0 and r ≥ 1. The latter statement is proved in the Supplementary Material, Section A, Theorem A.1. To lighten the notation, we assume without loss of generality that b is chosen so that µ((E \ B) × I) = 1 and thus c = 1 and Φ is a probability measure on S × I. In particular, the joint limit measure µ and the joint angular measure Φ are linked through the relation µ({x ∈ E : ∥x∥ ≥ r, θ(x) ∈ B} × C) = r
−αΦ(B × C)
for all C ∈ B(I), B ∈ B(S) and r > 0. Observe that

$$\operatorname*{lim}_{t\to+\infty}{\frac{\mathbb{P}\left\{\theta(X)\in B,Y\in C,\|X\|\geq t\right\}}{\mathbb{P}\left\{\|X\|\geq t\right\}}}=\Phi(B\times C),$$

for all B ∈ B(S), C ∈ B(I), such that Φ(∂(B × C)) = 0. In words, Φ is the asymptotic joint probability distribution of (θ(X), Y ) given that ∥X∥ ≥ t as t → +∞. Notice also that X's angular (probability) measure writes Φθ(B) =
Φ(B × I).

Let P∞ denote the limit conditional distribution on E \ B × I of the pair (*X/t, Y* ) given that ∥X∥ ≥ t, *i.e.*

$$P_{\infty}(\,A\times C\,)=\operatorname*{lim}_{t\to+\infty}\mathbb{P}\left\{X/t\in A\,,Y\in C\,\,\mid\|X\|\geq t\right\}$$
P {X/t ∈ A , Y ∈ C | ∥X∥ ≥ t} (9)
for all A ∈ B(E \ B) and C ∈ B(I) such that µ(∂(A × C)) = 0, and let (X∞, Y∞) denote a random pair with distribution P∞. It follows immediately from (8) and from our choice c = 1, that P∞ indeed exists and is determined by (Φ, α), namely

$$P_{\infty}\{(x,y):\|x\|>r,\theta(x)\in B,y\in C\}=\lim_{t\to+\infty}\mathbb{P}\left\{\|X\|/t\geq r,\theta(X)\in B,Y\in C\ |\ \|X\|\geq t\right\}$$ $$=r^{-\alpha}\Phi(B\times C),$$
$\left(\mathfrak{g}\right)_{\mathbb{Z}}$
where *B, C, r* are as in Equation (8). In other words, if T denotes the pseudo-polar transformation with respect to the first component T(*x, y*) = (∥x∥, θ(x), y) on E \ B × I, and if να is the Pareto measure να([x, ∞)) = x
−α, then the following tensor product decomposition holds true in polar coordinates, P∞ ◦ T
−1 = να ⊗ Φ.

Observe that, under Assumptions 1 and 2, the random variable Y∞ is almost-surely bounded in amplitude by M < +∞.

Equipped with these notations, it is natural to consider the squared error loss of a prediction function f, under the distribution P∞. We call this key quantity the *extreme quadratic risk*, denoted by RP∞, defined as

$$R_{P_{\infty}}(f):=\mathbb{E}\left[(Y_{\infty}-f(X_{\infty}))^{2}\right],$$

for f ∈ F a class of real-valued bounded Borel-measurable functions defined on E \ B. As will become clear in the subsequent analysis, although our objective R∞ and the extreme risk RP∞ are two different functionals, they turn out to be connected through their minimizers under an additional technical assumption stated below. In the sequel we let f
∗
P∞
denote the minimizer pf RP∞ among all measurable functions. Standard arguments from statistical learning theory show immediately that f
∗
P∞
is defined (up to a negligible set) by a conditional expectation, f
∗
P∞
(X∞) = E[Y∞ | X∞].

Remark 2 (Heavy-tailed input vs heavy-tailed output) Attention should be paid to the fact that the heavytail assumption is here on the distribution of the input/explanatory random variable X*, in contrast to other works* devoted to regression such as [8], [42] or [39] where it is the loss/response that is supposedly heavy-tailed. In the EVT literature, similarly, the vast majority of existing works in a regression context are concerned with extreme values of the target, in particular for extreme quantiles regression ([23, 16, 11, 17])

Assumption 3 *The extreme regression function* f
∗
P∞
is continuous on R
d \ {0Rd } and as t *tends to infinity,*
* [16] M. C.  
7
$$\mathbb{E}\left[|f^{*}(X)-f_{P_{\infty}}^{*}(X)|\mid\|X\|\geq t\right]\to0.$$
The next proposition highlights the weakness of Assumption 3, as long as Assumptions 1 and 2 are satisfied.

Proposition 1 (Sufficient conditions for Assumption 3) Let (X, Y ) *satisfy Assumptions 1 and 2. Then Assumption 3 also holds if one of the three conditions (i), (ii), (iii) below holds*
(i) *The regression function* f
∗*is continuous on* {x ∈ R
d: ∥x∥ ≥ 1} *and as* t → +∞,

$\mathbb{T}$ = $\mathbb{T}$. 
$\downarrow$ . 
$$\operatorname*{sup}_{\|x\|\geq t}|f^{*}(x)-f_{P_{\infty}}^{*}(x)|\to0,$$
$$(10)$$
$$(11)$$
(x)| → 0, (10)
(ii) The conditional distributions of Y *given* X = x ( resp. Y∞ given X∞ = x*) admit densities* pY |x(y) ( resp.

p∞
Y |x
(y)) w.r.t. the Lebesgue measure on I, for all x , 0. In addition for all y ∈ I*, the mapping* x 7→ pY |x(y)
( resp. x 7→ pY |x(y)*) is continuous, and* sup∥x∥≥1,y∈I max pY |x(y), p∞
Y |x
(y) < +∞*. Finally the following* uniform convergence holds true,

$$\operatorname*{sup}_{\|x\|\geq t,y\in I}|p_{Y|x}(y)-p_{Y|x}^{\infty}(y)|\underset{t\to+\infty}{\longrightarrow}0.$$
0. (11)
(iii) The random pair (X, Y ) (resp. (X∞, Y∞)) has a continuous density p (resp. q) w.r.t. the Lebesgue measure, and the densities converge uniformly, in the sense that

$$\operatorname*{sup}_{(\omega,y)\in\mathbb{S}\times I}\left|\,b(t)t^{d}p(t\omega,y)-q(\omega,y)\,\right|\mathop{\longrightarrow}_{t\to+\infty}0.$$
0. (12)
$$\left[\,\parallel X\parallel>t\,\right]^{-1}$$

where b(t) = P {∥X∥ ≥ t}
−1. In addition, q *is uniformly lower bounded on the unit sphere by a positive*

constant,
$$\operatorname*{inf}_{\omega\in\mathbb{S},y\in I}q(\omega,y)>0.$$
q(*ω, y*) > 0. (13)
It should be noticed that Condition (iii) in Proposition 1 is a 'one-component variant' of standard assumptions regarding regular variations of densities ([19, 9]), further discussed in Example 2 below. We refer to Section B.1 in the Supplementary Material for a proof of Proposition 1.

We now work out several examples of regression settings in which our Assumptions 1, 2 and 3 are satisfied.

Example 1 (Noise model with heavy-tailed random design) Suppose that X *is a regularly varying random* vector in R
d, independent from a real-valued random variable ε *modeling some noise and consider a target*

$\left(14\right)^{2}$
Y = g(*X, ε*),

where g : R
d × R → R *is a bounded, continuous mapping. Assume also that there exists a function* gθ : S × R → R
such that, for all z ∈ R
$$\operatorname*{sup}_{\|x\|\geq t}|g(x,z)-g_{\theta}(x/\|x\|,z)|\to0,$$
|g(x, z) − gθ(x/∥x∥, z)| → 0, (14)
 *as $t\to+\infty$. Then, the random pair $(X,Y)$ fulfills Assumptions 1, 2 and 3.*
The proof of the claim made in Example 1 is deferred to the Supplementary Material, Section B.2. Concrete examples arise within the broader context of this generic example, such as the additive noise model Y = ˜g(X) + ε and the multiplicative noise model Y = εg˜(X). In both cases, Condition (14) holds true whenever ˜g satisfies the similar condition sup
∥x∥≥t |g˜(x) − g˜θ(θ(x))| → 0, for some angular function ˜gθ, with minor additional regularity assumptions. We work out the details of these two sub-examples in Section B.2, Propositions B.2 and B.3, from the Supplementary Material.

Example 2 (Predicting a missing component in a regularly varying random vector)) In this example, we show that our assumptions are met when considering a random vector X˜ *with a regularly varying* density, where the target Y *is one missing component from the vector, or more precisely a normalized version of that missing component. The normalization allows to satisfy our boundedness constraint Assumption 1. We believe this* example could be particularly useful in applications, for imputation of missing data with heavy tails.

Let X˜ ∈ R
d+1 have continuous density p*, and* b(t) = P∥X˜∥ ≥ t	−1, where ∥ · ∥ *is the* L
p *norm on* R
d+1 for some p ∈ [1, +∞) . Assume that b is regularly varying with index α for some α > 0, and that there exists a positive function q on R
d+1 *such that for all* x˜ , 0Rd+1 ,

$$t^{d+1}b(t)p(t\tilde{x})-q(\tilde{x})\underset{t\rightarrow+\infty}{\longrightarrow}0.$$
$$(15)$$
0. (15)
Assume in addition that the convergence is uniform on the sphere,

$$\sup_{\omega\in\mathbb{S}_{d+1}}|t^{d+1}b(t)p(t\omega)-q(\omega)|\mathop{\longrightarrow}_{t\to+\infty}0,\tag{1}$$

where Sd+1 *denotes the unit sphere of* R
d+1. This assumption is used in [19, 9]. It is shown in these references that (15) and (16) imply that X˜ is regularly varying with index α*. More precisely with* µ(A) = RA
q(˜x) d˜x for any measurable set A ⊂ E, we have b(t)PX/t ˜ ∈ · 	→ µ(·) in the sense of vague convergence. Necessarily q is homogeneous of order −α − d − 1. Also the continuity of p implies that of q*. Assume finally that*

$$\left(16\right)$$
$$\operatorname*{min}_{\omega\in\mathbb{S}_{d+1}}q(\omega)>0.$$
 $if\ (15)\ and\ (16)\ hold,\ then\ also:$  . 
$$(17)$$

Another useful feature of this setting is that, if (15) *and (16) hold, then also*

$$\sup_{\|\hat{x}\|\geq1}|p(t\hat{x})t^{d+1}b(t)-q(\hat{x})|\underset{t\rightarrow+\infty}{\longrightarrow}0.\tag{1}$$

Let X = (X˜1, . . . , X˜d) and Y = X˜d+1/∥X˜∥. The norm ∥x∥ *also denotes the* L
p *norm in* R
d when it is clear from the context that x ∈ R
d. Then

$$(i)\;\;T h e\;p$$

(i) The pair (X, Y ) satisfies Assumptions 1, 2 and 3;
(ii) The limit pair (X∞, Y∞) for (X, Y ) *defined in* (9) *has distribution*

$\widehat{\mathbf{a}}\widehat{\mathbf{a}}$
where X˜∞,1:d denotes the d-dimensional vector (X˜∞,1, . . . , X˜∞,d).

It is important to observe that predicting Y allows to predict X˜d+1*, as*

$$Y=\frac{\tilde{X}_{d+1}}{\|\tilde{X}\|_{p}}\quad\Longleftrightarrow\quad\tilde{X}_{d+1}=\frac{Y\|X\|_{p}}{(1-|Y|p)^{1/p}}.$$
$\large{cial\ dataset}$. 
In our experiments with real data we consider this prediction example on a financial dataset.

As will be shown in the forthcoming sections, Assumptions 1, 2 and 3 provide sufficient regularity and stability conditions allowing to justify the *angular* ERM approach taken in Algorithm 1.

## 3 Regression On Extremes - Main Results 3.1 Structural Analysis Of Minimizers: Conditional, Asymptotic And Extreme Risks

The main purposes of this subsection are to show that under the assumptions previously listed, (i) the extreme quadratic risk RP∞ is minimized by angular prediction functions, that is functions depending on the input through the angle only ; (ii) Although R∞ and RP∞ are different risk functionals, they are connected through their respective minimizers and minimum values.

The first objective (i) above is easily tackled. Indeed, the discussion below Equation (9) shows that, under Assumption 2, letting Θ∞ = θ(X∞) denote the angular component of X∞, the random pair (Θ∞, Y∞) is independent

$${\mathcal{L}}\Big(\big(\tilde{X}_{\infty,1:d},\frac{\tilde{X}_{\infty,d+1}}{\|\tilde{X}_{\infty}\|}\big)\mid\|\tilde{X}_{\infty,1:d}\|\geq1\Big),$$  _sional vector $(\tilde{X}_{\infty,1},\ldots,\tilde{X}_{\infty,d})$._
from the norm ∥X∞∥, and in particular Y∞ and ∥X∞∥ are independent. Hence, the only useful piece of information carried by X∞ to predict Y∞ is its angular component Θ∞. As a consequence the Bayes regression function satisfies f
∗
P∞
(X∞) = E [Y∞ | X∞] = E [Y∞ | Θ∞] almost-surely. As a consequence we may write f
∗
P∞ = h∞ ◦ θ for some function h∞ defined on the sphere S. Finally, Assumption 3 ensures that h∞ may be chosen as a continuous function. We summarize the discussion:
Lemma 1 Under Assumptions 1, 2, 3, the extreme risk RP∞ has a minimizer (among all measurable functions)
which may be written as f
∗
P∞
(x) = h∞ ◦ θ(x) where h∞ : S → I *is a bounded, continuous function.*
The next result brings answers regarding the objective (ii) outlined above, by establishing a key connection between the (seemingly) different problems of minimizing R∞ on the one hand, and minimizing RP∞ on the other hand. Recall from Section 2.3 that the extreme risk RP∞(f) = E-(f(X∞) − Y∞)
2and the asymptotic risk R∞(f) = lim supt→+∞ E-(f(X) − Y )
2| ∥X∥ ≥ tare two different functionals, so that the regression function f
∗
P∞
is only defined as a minimizer of the extreme risk RP∞ and not the asymptotic risk R∞. In the sequel we denote by R∗P∞
the minimum value of the extreme risk, *i.e.* R∗P∞
:= inff measurable RP∞(f) = RP∞(f
∗
P∞
).

Theorem 1 *Under Assumptions 1 and 2, we have*
(i) *For any angular function of the kind* f(x) = h ◦ θ(x), where h is a continuous function defined on S, the conditional risk converges to the extreme risk, i.e.

$$R_{t}(f)\ {\xrightarrow[t\to\infty]{}}\ R_{P_{\infty}}(f).$$

Thus for such prediction functions, R∞(f) = limt→+∞ Rt(f) = RP∞(f).

If in addition Assumption 3 is satisfied, then the following assertions hold true.

(ii) As t → +∞: the minimum value of Rt converges to that of RP∞*, i.e.* R∗
t −→t→+∞
R∗P∞
.

(iii) The minimum values of R∞ and RP∞ *coincide, i.e.* R∗∞ = R∗P∞
.

(iv) *The regression function* f
∗
P∞ *minimizes the asymptotic conditional quadratic risk:*

$$R_{\infty}^{*}=R_{\infty}(f_{P_{\infty}}^{*}).$$
$$(18)$$

The proof is deferred to Section C.1 in the Supplementary Material. Observe that Theorem 1 does not assert that Rt(f) converges to RP∞(f) for all f, but the convergence holds true for angular predictors f = h◦θ (Property (i) in the statement). Property *(iv)* discloses that the solution f
∗
P∞
of the extreme risk minimization problem, which is of angular type, is also a minimizer of the asymptotic conditional quadratic risk R∞ (and that the minima coincide).

Because f
∗
P∞ = h∞ ◦ θ is of angular type, we thus obtain, under Assumptions 1, 2 and 3,

$$\operatorname*{inf}_{f\mathrm{measurable}}R_{\infty}(f)=\operatorname*{inf}_{h{\mathrm{~measurable}}}R_{\infty}(h\circ\theta).$$
R∞(h ◦ θ). (18)
In other words, the search for minimizers of R∞ may indeed be restricted to angular prediction functions, which provides a first heuristic justification for Algorithm 1. However in order to provide rigorous guarantees regarding minimizers of the empirical criterion (4) from Algorithm 1, further assumptions regarding the class H of angular predictors are needed. In particular these additional assumptions ensure uniformity of the convergence result (i) from Theorem 1. This is the focus of the next section.

## 3.2 Statistical Learning Guarantees

This section provides a nonasymptotic analysis of the approach proposed for regression on extremes. An upper confidence bound for the excess of R∞-risk of a solution of (4) is established, when the class H over which empirical minimization is performed is of controlled complexity, see Assumption 4 below.

The rationale behind the approach proposed in Algorithm 1 is to find an angular predictive function that nearly minimizes the asymptotic conditional quadratic risk R∞ (3). Our ERM strategy thus consists in solving an empirical version of the nonasymptotic optimization problem Recall that a heuristic justification for considering angular classifiers is given by Identity (18), which is itself a consequence of Theorem 1. The radial threshold t is chosen as a relatively high quantile of the empirical distribution of the radii ∥Xi∥. In particular, let tn,k denote the 1 − k/n quantile of the norm ∥X∥, where k ≪ n is large enough so that a statistical analysis remains realistic, but small enough so that the the distribution of (*X, Y* ) given that
∥X∥ > tn,k is close to the limit P∞, see (9). Then an empirical version of tn,k is tˆn,k = ∥X(k)∥, the k th largest order statistic of the norm already introduced in Algorithm 1. In practice the number k of retained extreme values statistics in a recurrent issue in Extreme Value Analysis, for which no definite theoretical answer exists, but which is a standard bias/variance compromise. In our experiments, following standard practice we choose k by inspection of stability regions in Hill plots. In addition, in a regression setting we consider feature importance summaries relative to the radial variable, see Section 4 for details.

Summarizing, the objective minimized in Algorithm 1 may be viewed as an empirical version of the conditional risk Rtn,k for a predictive mapping of the form h ◦ θ. In the sequel we denote by Rˆk this empirical objective,

$$\hat{R}_{k}(f)=\frac{1}{k}\sum_{i=1}^{k}\left(Y_{(i)}-f(X_{(i)})\right)^{2}.$$
$$(19)$$

2. (19)
We point out that the statistic above is not an average of independent random variables, as it involves extreme order statistics of the norm. Thus investigating its concentration properties is far from straightforward. The minimum is taken over a class H of continuous bounded functions on S of controlled complexity but hopefully rich enough to contain a reasonable approximant of h∞ introduced in Lemma 1. The following assumption regarding H will turn out to be sufficient to obtain a control of the deviations of the empirical risk. In order to avoid measurability issues regarding supremum deviations over the class H, it is assumed throughout that H is *pointwise measurable*
(see [52], Example 2.3.4), *i.e.* that there exists a countable family H0 ⊂ H, such that for all ω ∈ S and all h ∈ H,
there is a sequence (hi)i≥1 ∈ H0 such that hi(ω) → h(ω). This mild condition is satisfied in most practical cases, in particular by parametric classes H, *i.e.* classes indexed by a finite dimensional parameter β ∈ R
p, which depend continously on the parameter, *i.e.* such that ∥hβ − hβn
∥∞,S → 0 as βn → β.

Assumption 4 The pointwise measurable class H *is a family of continuous, real-valued functions defined on* S;
of VC dimension VH < +∞, and uniformly bounded by the same constant as the target Y *(see Assumption 1),*
∀h ∈ H, ∀ω ∈ S, |h(ω)| ≤ M.

Under the complexity hypothesis above, the following result provides an upper confidence bound for the maximal deviations between the conditional quadratic risk Rtn,k and its empirical version Rˆk, uniformly over the class H.

Notice that a similar result is obtained in [2] (Lemma A.3) in the more complex setting of cross validation. For the sake of completeness, we provide a detailed proof in Section C.2 of the Supplementary Material.

Theorem 2 Suppose that Assumptions 1 and 4 are satisfied. Let δ ∈ (0, 1)*. We have with probability larger than* 1 − δ:

$$\sup_{h\in\mathcal{H}}\left|\hat{R}_{k}(h\circ\theta)-R_{t_{n,\kappa}}(h\circ\theta)\right|\leq\frac{8M^{2}\sqrt{2\log(3/\delta)}+C\sqrt{V_{\mathcal{H}}}}{\sqrt{k}}+\frac{16M^{2}\log(3/\delta)/3+4M^{2}V_{\mathcal{H}}}{k},$$  _is a universal constant._
where C *is a universal constant.*
Notice that Theorem 2 controls only the statistical deviations between the sub-asymptotic risk Rtn,k and its empirical version Rˆk. A control of the bias term Rtn,k − R∞ is given next, under appropriate complexity assumptions controlling the complexity of class H. In particular Assumption 4 can be traded against a total boundedness assumption (Case 1. in Proposition 2 below) which is further discussed below (Remark 3). Regarding the second set of assumption (Case 2.), notice that for t ≥ 1, the conditional distribution Φθ,t = L(θ(X)| ∥X∥ ≥ t) is absolutely continuous w.r.t. Φθ,1 = L(θ(X)| ∥X∥ ≥ 1). Indeed for any measurable set A ⊂ S, if P {Θ ∈ A | ∥X∥ ≥ 1} = 0 then also for any t ≥ 1, P {Θ ∈ A | ∥X∥ ≥ t} = 0. Denote by ϕθ,t the probability density of the former angular distribution with respect to the latter.

Proposition 2 Suppose that Assumptions 1 and 2 are satisfied. Let H be a class of real-valued, continuous functions on S. Assume that one out of the two following conditions is satisfied.

1. H is totally bounded in the space (C(S), ∥ · ∥∞) of continuous functions on S endowed with the supremum norm, or