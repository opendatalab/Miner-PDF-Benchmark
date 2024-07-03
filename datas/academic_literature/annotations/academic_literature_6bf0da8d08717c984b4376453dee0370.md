# On Regression in Extreme Regions 

Stephan Clémençon, Nathan Huet, Anne Sabourin

April 11, 2024


#### Abstract

In the classic regression problem, the value of a real-valued random variable $Y$ is to be predicted based on the observation of a random vector $X$. The statistical learning problem consists in building a predictive function $\hat{f}$ based on independent copies of $(X, Y)$ so that $Y$ is approximated by $\hat{f}(X)$ with minimum (squared) error. Motivated by various applications, special attention is paid here to the case of extreme (i.e. very large) observations $X$. Because of their rarity, the contributions of such observations to the (empirical) error is negligible, and the predictive performance of empirical risk minimizers can be consequently very poor in extreme regions. In this paper, we develop a general framework for regression on extremes. Under appropriate regular variation assumptions regarding the pair $(X, Y)$, we show that an asymptotic notion of risk can be tailored to summarize appropriately predictive performance in extreme regions. It is also proved that minimization of an empirical and nonasymptotic version of this 'extreme risk', based on a fraction of the largest observations solely, yields good generalization capacity. In addition, numerical results providing strong empirical evidence of the relevance of the approach proposed are displayed.


## Contents

| 1 | Introduction | 2 |
| :--- | :--- | :--- |

2 A Regular Variation Framework for Regression 3

2.1 Least Squares Minimization on Extremes - Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 Background on Multivariate Regular Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.3 Regular Variation with respect to the First Component . . . . . . . . . . . . . . . . . . . . . . . . . 5

| 3 | Regression on Extremes - Main Results | 8 |
| :--- | :--- | :--- |

3.1 Structural Analysis of Minimizers: Conditional, Asymptotic and Extreme Risks . . . . . . . . . . . . 8

3.2 Statistical Learning Guarantees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

4 Numerical Experiments 12

4.1 Simulated data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

4.2 Real data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

5 Conclusion 15

| A Multivariate Regular Variation w.r.t. the First Component | 17 |
| :--- | :--- |


| B Proofs for Section 2 | 18 |
| :--- | :--- | :--- |

B. 1 Proof of Proposition 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
B. 2 Proofs and Additional Results regarding Example 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B. 3 Proofs regarding Example 2 [ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

C Proofs for Section 3 , 25
C. 1 Proof of Theorem|1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C. 2 Proof of Theorem 2 2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C. 3 Proof of Proposition 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

## 1 Introduction

Regression is a predictive problem of crucial importance in statistical learning, covering a wide variety of applications. In the standard setup, $(X, Y)$ is a pair of random variables defined on the same probability space $(\Omega, \mathcal{A}, \mathbb{P})$ with distribution $P$, where the target $Y$ is a square integrable real-valued random variable (the output) and the predictor (or covariable) $X$ is a random vector with marginal distribution $\rho$ taking its values in some measurable space $\mathcal{X}$ modeling some input information hopefully useful to predict $Y$. The predictive learning problem consists in building, from a training dataset $\mathcal{D}_{n}=\left\{\left(X_{1}, Y_{1}\right), \ldots,\left(X_{n}, Y_{n}\right)\right\}$ composed of $n \geq 1$ independent copies of $(X, Y)$, a mapping $f: \mathcal{X} \rightarrow \mathbb{R}$ in order to compute a 'good' prediction $f(X)$ for $Y$, with the quadratic risk

$$
R_{P}(f)=\mathbb{E}\left[(Y-f(X))^{2}\right]
$$

as close as possible to that of $f^{*}(X)=\mathbb{E}[Y \mid X]$, which obviously minimizes (1) over the space $L_{2}(\rho)$ of square integrable functions of $X: R_{P}^{*}:=\min _{f \in L_{2}(\rho)} R_{P}(f)=R_{P}\left(f^{*}\right)$. A natural strategy consists in solving the Empirical Risk Minimization problem (ERM in abbreviated form) $\min _{f \in \mathcal{F}} R_{\hat{P}_{n}}(f)$, where $\mathcal{F} \subset L_{2}(\rho)$ is a closed and convex class of functions sufficiently rich to include a reasonable approximant of $f^{*}$ and $\hat{P}_{n}$ is an empirical version of $P$ based on $\mathcal{D}_{n}$.

The performance of predictive functions $\hat{f}$ obtained this way, by least-square regression, has been extensively investigated in the statistical learning literature [31, 40. Under the assumption that the tails of the random pairs $(f(X), Y)$ are subgaussian and appropriate complexity conditions are satisfied by the class $\mathcal{F}$, confidence upper bounds for the excess of quadratic risk $R_{P}(\hat{f})-R_{P}^{*}=\mathbb{E}\left[(Y-\hat{f}(X))^{2} \mid \mathcal{D}_{n}\right]-R_{P}^{*}$ have been established in [36] by means of concentration inequalities for empirical processes [6].

Here we consider the problem of building prediction functions which would be reliable in a a 'crisis scenario' where the covariates vector takes unusually large values and thus belongs to regions where few or even no such large examples have been observed in the past. Notice incidentally that it could be thus viewed as a specific, never tackled yet, few shot learning problem, see e.g. [56. We place ourselves in a finite-dimensional setting, $\mathcal{X} \subset \mathbb{R}^{d}$. The distribution of $X$ is not subgaussian and in particular its support is unbounded. Covariates are considered as extreme when their norm $\|X\|$ exceeds some (asymptotically) large threshold $t>0$. The choice of the norm is unimportant in theory, and is typically determined by the application context.

The threshold $t$ depends on the observations, since 'large' should be naturally understood as large with respect to the vast majority of data observed. Hence, extreme observations are rare by nature and severely underrepresented in the training dataset with overwhelming probability. Consequently, the impact of prediction errors in extreme regions of the input space on the global regression error of $\hat{f}$ is generally negligible. Indeed, the law of total probability yields

$$
R_{P}(f)=\mathbb{P}\{\|X\| \geq t\} \mathbb{E}\left[(Y-f(X))^{2} \mid\|X\| \geq t\right]+\mathbb{P}\{\|X\|<t\} \mathbb{E}\left[(Y-f(X))^{2} \mid\|X\|<t\right]
$$

The above decomposition involves a conditional error term relative to excesses of $\|x\|$ above $t$, which we term Conditional quadratic risk (or simply Conditional risk)

$$
R_{t}(f):=\mathbb{E}\left[(Y-f(X))^{2} \mid\|X\| \geq t\right]
$$

It is the purpose of the subsequent analysis to construct a predictive function $\hat{f}$ that (approximately) minimizes $R_{t}(f)$ for all $t>t_{0}$, with $t_{0}$ being a large threshold. It is important to note that an approximate minimizer of $R_{t}$ might not be suitable for minimizing $R_{t^{\prime}}$ when $t^{\prime}>t$. To ensure robust extrapolation performance for our learned function, we focus on obtaining a prediction function, $\hat{f}$, that minimizes the asymptotic conditional quadratic risk defined as

$$
R_{\infty}(f):=\limsup _{t \rightarrow+\infty} R_{t}(f)=\limsup _{t \rightarrow+\infty} \mathbb{E}\left[(Y-f(X))^{2} \mid\|X\| \geq t\right]
$$

It is immediate to see that any function that coincides with the regression function $f^{*}(x)=\mathbb{E}[Y \mid X=x]$ on the region $\{x \in \mathcal{X},\|x\| \geq t\}$ minimizes the risk functional $R_{t}$, for all $t>0$, and thus also $R_{\infty}$. In other words $R_{\infty}^{*}:=\inf _{f} R_{\infty}(f)=R_{\infty}\left(f^{*}\right)$. However, even though $f^{*}$ provides a straightforward theoretical solution, $f^{*}$ is of course unknown.

In view of Equation (2) it is evident that an estimate $\hat{f}$ of $f^{*}$ produced by an ERM strategy with good overall empirical performances, may not necessarily enjoy good performances when restricted to extreme regions. Put another way, there is no guarantee that the conditional risk $R_{t}(\hat{f})$ (or $R_{\infty}(\hat{f})$ ) would be small. However, accurate
prediction in extreme regions turns out to be crucial in certain practical (safety) applications, in environmental sciences, dietary risk analysis or finance/insurance for instance.

To summarize, the Regression Problem on Extremes refers here to the the task of constructing a prediction function $\hat{f}$ based on $\mathcal{D}_{n}$ which approximately minimizes $R_{\infty}$. Notice that our choice of the squared error is motivated by simplicity and for illustrative purpose, extensions to other losses may be achieved at the price of additional (minor) technicalities.

In order to develop a specific ERM framework relative to $R_{\infty}$ with provable guarantees, regularity assumptions are required regarding the tail behavior of the pair $(X, Y)$, with respect to the first component. Multivariate regular variation hypotheses are very flexible in the sense that they correspond to a large nonparametric class of heavytailed distributions. These assumptions, or slightly weaker ones such as Maximum domain of attraction conditions are at the heart of Extreme Value Analysis (EVA) (e.g., the monographs [5, 18, 49). They are frequently used in applications where the impact of extreme observations should be enhanced, or not neglected at the minimum.

Statistical learning approaches in EVA have recently garnered significant interest, particularly in unsupervised learning contexts. Examples include dimensionality reduction through multiple subspace clustering in 28, 29, 13, 50, 43, 44, as well as Principal Component Analysis in [15, 20. In addition, there has been notable exploration in clustering methods [35, 55, graphical models [24, and applications such as Anomaly Detection [12, 54, to name just a few. In the supervised setting, unlike the current study, the predominant focus in the literature revolves around predicting extreme values of the target variable $Y[3]$ or tackling extreme quantile regression through methods such as gradient boosting [53] or random forests [26].

The work which is most related to ours is that of [34] (see also [14]), where an ERM framework for the (easier) binary classification problem on extreme covariates is developed. Precisely, it is assumed therein that the two class distributions are multivariate regularly varying with the same tail index (see (5) in the background section 2.2), and risk functionals $R_{t}, R_{\infty}$ are defined similarly with the 0-1 loss. One of the primary objectives of this paper is to establish sufficient and reasonable conditions for extending the results of 34 to a broader context encompassing statistical regression with a continuous target and an appropriate real-valued loss. It must be noted that the continuous nature of the target in the regression problem considered here requires fundamentally different assumptions and proof techniques compared with the binary classification setting. In particular one natural generalization of the assumptions made in the cited reference would be to assume regular variation of the conditional distributions $\mathcal{L}(X \mid Y=y)$, almost everywhere. This somewhat intricate generalization leads to measure theoretic complications and is difficult to verify in practice and also on theoretical examples. We propose to bypass this issue by requiring instead a joint form of regular variation of the pair $(X, Y)$, see our Assumption 2 We show that this condition is satisfied in various examples worked out in Section 2.3 Another major improvement of the present work upon [34, with implications for applications related to climate extremes, is to offer a novel perspective upon extreme value prediction within regularly varying random vectors, see Example 2 .

The paper is organized as follows. The algorithmic approach we propose for Regression on Extremes is detailed in Section 2, extending 34's framework in order to handle continuous targets. Key notions pertaining to multivariate extreme value theory (MEVT) are also briefly recalled for clarity's sake and the probability framework we consider for regression in extreme regions is described at length therein. In Section 3, we show that a predictive rule using the angular information only i.e. of the form $f(X)=h(X /\|X\|)$, where $h$ is a real-valued function defined the hypersphere $\mathbb{S}=\left\{x \in \mathbb{R}^{d}:\|x\|=1\right\}$ reaches the best possible performances w.r.t. the asymptotic risk. Subsequently, we study the performance of a predictive rule based on a training sample $\left\{\left(X_{1}, Y_{1}\right), \ldots,\left(X_{n}, Y_{n}\right)\right\}$ composed of $n \geq 1$ independent copies of the pair ( $X, Y$ ) and learned by minimizing an empirical version of (3) based on a fraction $k / n$ of the training dataset, those corresponding to the largest $\| X_{i} \mid$ 's. Nonasymptotic bounds for the excess of asymptotic risk of such an empirical (preasymptotic) risk minimizer are established, demonstrating its near optimality. Beyond these theoretical guarantees, the performance of empirical risk minimization on extreme covariates is supported by various numerical experiments displayed in Section 4. Some concluding remarks are collected in Section 5 In order to enhance readability, certain technical details are postponed to the Appendix section.

## 2 A Regular Variation Framework for Regression

In this section, we propose a probabilistic framework in which Regression on Extremes may be addressed, together with a dedicated algorithmic approach, the latter being analyzed next in the subsequent sections. Here and throughout, $(X, Y)$ is a pair of random variables defined on a probability space $(\Omega, \mathcal{A}, \mathbb{P})$ with distribution $P$, where $Y$ is real-valued with marginal distribution $G$ and $X=\left(X^{(1)}, \ldots, X^{(d)}\right)$ takes its values in $\mathbb{R}^{d}, d \geq 1$. We sometimes denote by $\mathcal{L}(Z)$ the distribution of a random variable $Z$. Recall from the Introduction section that $\|\cdot\|$ is any
norm on $\mathbb{R}^{d}$. We denote by $\mathbb{S}$ the unit sphere for this norm and by $\mathbb{B}:=\left\{x \in \mathbb{R}^{d},\|x\| \leq 1\right\}$ the unit ball. Let $E=\mathbb{R}^{d} \backslash\left\{0_{\mathbb{R}^{d}}\right\}$ be the punctured Euclidean space. For any measurable subset $A$ of $\mathbb{R}^{d}$ we denote by $\mathcal{B}(A)$ the trace Borel $\sigma$-field on $A$. The boundary and the closure of $A$ are respectively denoted by $\partial A$ and $\bar{A}$, and we set $t A=\{t x: x \in A\}$ for all $t \in \mathbb{R}$. By $\mathbb{1}\{\mathcal{E}\}$ is meant the indicator function of any event $\mathcal{E}$ and the integer part of any $u \in \mathbb{R}$ is denoted by $\lfloor u\rfloor$.

### 2.1 Least Squares Minimization on Extremes - Algorithm

In order to help the reader understand the general workflow of the paper, we begin immediately by introducing the algorithm that we promote to solve the Regression Problem on Extremes stated in the Introduction, formulated as the minimization of the risk functional $R_{\infty}$ defined in (3). The remainder of this work aims at developing a framework that fully justifies Algorithm 1 below.

## Algorithm 1 Least Squares Minimization on Extremes

INPUT: Training dataset $\mathcal{D}_{n}=\left\{\left(X_{1}, Y_{1}\right), \ldots,\left(X_{n}, Y_{n}\right)\right\}$ with $\left(X_{i}, Y_{i}\right) \in[0,+\infty)^{d} \times \mathbb{R}, i=1, \ldots, n$; class $\mathcal{H}$ of predictive functions $h: \mathbb{S} \rightarrow \mathbb{R}$; number $k \leq n$ of 'extreme' observations among training data.

Truncation: Sort the training data by decreasing order of magnitude of the input information $\left\|X_{(1)}\right\| \geq \ldots \geq$ $\left\|X_{(n)}\right\|$ and form a set of $k$ extreme training observations

$$
\left\{\left(X_{(1)}, Y_{(1)}\right), \ldots,\left(X_{(k)}, Y_{(k)}\right)\right\}
$$

Empirical quadratic risk minimization: based on the extreme training dataset, solve the optimization problem

$$
\min _{h \in \mathcal{H}} \frac{1}{k} \sum_{i=1}^{k}\left(Y_{(i)}-h\left(\theta\left(X_{(i)}\right)\right)\right)^{2}
$$

where $\theta(x)=x /\|x\|$ is the angular component of any point $x \in \mathbb{R}^{d} \backslash\{0\}$.

OUTPUT: Solution $\hat{h}$ to problem (4) and predictive function $\widehat{f}(x)=(\hat{h} \circ \theta)(x)$ to be used for predictions of $Y$ based on new examples $X$ such that $\|X\| \geq\left\|X_{(k)}\right\|$.

Notice that any algorithm for quadratic risk minimization can be used to solve [4], refer to e.g., 31]. The study of dedicated numerical techniques is beyond the scope of the present paper.

A key feature of Algorithm 1 is that its training step involves the angular component of extremes solely. It returns a prediction function $f$ which only depends on the angular component $\theta(X)$ of a new input $X$. This apparently arbitrary choice turns out to be fully justified under regular variation assumptions, which are introduced and discussed in the following subsections. To wit, the main theoretical advantage of considering angular prediction function is to ensure the convergence of the conditional risk $R_{t}$, as $t \rightarrow+\infty$. In practice, rescaling all extremes (in the training set and in new examples) onto a bounded set allows a drastic increase in the density of available training examples and a clear extrapolation method beyond the envelope of observed examples.

After recalling some background on multivariate regular variation in subsection 2.2, we introduce a modified version of the standard framework (regular variation with respect to the first component) in subsection 2.3 which is suitable for the regression problem considered here, in the sense that Algorithm 1 turns out to enjoy probabilistic and statistical guarantees in this context. We thoroughly discuss the relevance of our assumptions by working out several sufficient conditions and examples. We state our main probabilistic results in subsection 3.1, establishing connections between different risks and their corresponding minimizers, thus bringing a first (probabilistic) justification regarding the angular nature of the prediction function in Algorithm 1. Statistical guarantees are deferred to subsection 3.2

### 2.2 Background on Multivariate Regular Variation

The goal of heavy-tail analysis is to study phenomena that are not ruled by averaging effects but determined by extreme values. To investigate the behavior of a random vector $X$ far from the center of its mass, an usual assumption is that $X$ 's distribution is multivariate regularly varying with tail index $\alpha>0$, i.e. there exist a nonzero Borel measure $\mu$ on $E$, finite on all Borel measurable subsets of $E$ bounded away from zero and a regularly varying function $b(t)$ with index $\alpha$, i.e. $b(t x) / b(t) \rightarrow x^{\alpha}$ as $t \rightarrow+\infty$, such that

$$
b(t) \mathbb{P}\{X \in t A\} \rightarrow \mu(A) \text { as } t \rightarrow+\infty
$$

for any Borel measurable set $A \subset E$ bounded away from zero and such that $\mu(\partial A)=0$. The latter convergence is referred to as vague convergence in $[-\infty,+\infty]^{d} \backslash\left\{0_{\mathbb{R}^{d}}\right\}$ (see [49, sec. 3.4), or equivalently as $\mathbb{M}_{0}$-convergence in $E$ (see [33, 38]). The limit measure $\mu$ is provably homogeneous of degree $-\alpha: \mu(t A)=t^{-\alpha} \mu(A)$ for all $t>0$ and Borel set $A \subset E$ bounded away from the origin. One may refer to [49] for alternative formulations/characterizations of the regular variation property and its application to MEVT. It follows from the homogeneity property that the pushforward measure of $\mu$ by the polar coordinates transformation $x \in E \mapsto(\|x\|, \theta(x))$ is the tensor product given by:

$$
\mu\{x \in E:\|x\| \geq r, \theta(x) \in B\}=r^{-\alpha} \Phi(A)
$$

for all $B \in \mathcal{B}(\mathbb{S})$ and $r \geq 1$, where $\Phi$ is a finite positive measure on $\mathbb{S}$, referred to as the angular measure of the limit measure $\mu$. The regular variation assumption (5) implies that the conditional distribution of $(\|X\| / t, \theta(X))$ given $\|X\| \geq t$ converges as $t \rightarrow+\infty$ : for all $r \geq 1$ and $B \in \mathcal{B}(\mathbb{S})$ with $\Phi(\partial B)=0$, we have

$$
\mathbb{P}\left\{t^{-1}\|X\| \geq r, \theta(X) \in B \mid\|X\| \geq t\right\} \underset{t \rightarrow+\infty}{\longrightarrow} c r^{-\alpha} \Phi(B)
$$

where $c=\Phi(\mathbb{S})^{-1}=\mu(E \backslash \mathbb{B})^{-1}$ Hence, the radial and angular components of the random variable $X$ are asymptotically independent with standard Pareto distribution of parameter $\alpha$ and normalized angular measure $c \Phi$ as respective asymptotic marginal distributions. The angular measure $\Phi$ describes exhaustively the dependence structure of the components $X^{(j)}$ 's given that $\|X\|$ is large, i.e. the directions $\theta(X)$ in which extremes occur with largest probability.

Heavy-tailed models have been the subject of much attention in the statistical machine-learning literature. Among many other works, the regular variation assumption is used in 46 for rare event probability estimation, in [10 or [1] in the context of stochastic bandit problems, in 27] for the statistical recovery of the dependence structure in the extremes, in [29] for dimensionality reduction in extreme regions and in [8] for predictive problems with heavy-tailed losses.

### 2.3 Regular Variation with respect to the First Component

We now describe rigorously the framework we consider for regression in extreme regions, which may be seen as a natural, 'one-component' extension of standard multivariate regular variation assumptions recalled in Section 2.2

For simplicity, we suppose that $Y$ is bounded through this paper. This assumption can be naturally relaxed at the price of additional technicalities (i.e. tail decay hypotheses).

Assumption 1 The random variable $Y$ is bounded: there exists $M \in(0,+\infty)$ such that with probability one, $Y \in I=[-M, M]$.

The following hypothesis concerns the asymptotics, as $t \rightarrow+\infty$, of the conditional distribution of the pair $(X, Y)$ given that $\|X\|>t$. It may be viewed as one-component extension of (5).

Assumption 2 There exists a non null Borel measure $\mu$ on $\mathbb{O}=E \times I$, which is finite on sets bounded away from $\mathbb{C}=\{0\} \times I$, and a regularly varying function $b(t)$ with index $\alpha>0$ such that

$$
\lim _{t \rightarrow+\infty} b(t) \mathbb{P}\left\{t^{-1} X \in A, Y \in C\right\}=\mu(A \times C)
$$

for all $A \in \mathcal{B}(E)$ bounded away from zero and $C \in \mathcal{B}(I)$ such that $\mu(\partial(A \times C))=0$.

Assumption 2 could be understood as a multivariate extension of the One-Component Regular Variation framework developed in [32]. It should be noticed that Assumption 2 fits into the framework if Regular Variation in $\mathbb{M}_{\mathbb{O}}$ developed in [38] as an extension of [33], where $\mathbb{O}=E \times I=\left(\mathbb{R}^{d} \times I\right) \backslash(\{0\} \times I)$ and where the scalar multiplication is defined as $\lambda(x, y)=(\lambda x, y)$. More details regarding the connections between Assumption 2and [38] are provided in the Supplementary Material, Section A.

Remark 1 (Pre-Processing) Because the goal of this paper is to explain main ideas to tackle the problem of regression on extremes, the input are assumed to be regularly varying with same marginal index while in practice, this condition may be satisfied only after some marginal standardization. This is a recurrent theme in multivariate extreme value theory. For binary-valued $Y$, in the classification setting, [14] consider a marginal standardization based on ranks, following [21, 22]. They prove an upper bound on the statistical error term induced by this transformation which is of the same order of magnitude as the error when marginal distributions are known, a simplified case considered in [34]. In our experiments with real data, this pre-processing step is not necessary. We leave this technical question outside the scope of this paper.

In the sequel we refer to the limit measure $\mu$ as the joint limit measure of $(X, Y)$. Under Assumption 2, $X$ 's marginal distribution is regularly varying with marginal limit measure

$$
\mu_{X}(A)=\lim _{t \rightarrow+\infty} b(t) \mathbb{P}\{X \in t A\}=\lim _{t \rightarrow+\infty} b(t) \mathbb{P}\{X \in t A, Y \in I\}=\mu(A \times I)
$$

with $A \in \mathcal{B}(E)$ bounded away from zero and such that $\mu(\partial(A \times I))=0$. We also naturally introduce the joint angular measure of $(X, Y)$ denoted by $\Phi$, which is a finite measure on $\mathbb{S} \times I$ given by

$$
\Phi(B \times C)=\mu\{(x, y) \in E \times I:\|x\| \geq 1, \theta(x) \in B, y \in C\}
$$

With this notation, under Assumption 2 it holds that

$$
\frac{\mathbb{P}\{\theta(X) \in B, Y \in C,\|X\| \geq t r\}}{\mathbb{P}\{\|X\| \geq t\}} \underset{t \rightarrow+\infty}{\longrightarrow} c r^{-\alpha} \Phi(B \times C)
$$

where $c=\Phi(\mathbb{S} \times I)^{-1}=\mu((E \backslash \mathbb{B}) \times I)^{-1}$, for all $C \in \mathcal{B}(I), B \in \mathcal{B}(\mathbb{S})$, such that $\Phi(\partial(B \times A))=0$ and $r \geq 1$. The latter statement is proved in the Supplementary Material, Section A, Theorem A. 1 To lighten the notation, we assume without loss of generality that $b$ is chosen so that $\mu((E \backslash \mathbb{B}) \times I)=1$ and thus $c=1$ and $\Phi$ is a probability measure on $\mathbb{S} \times I$. In particular, the joint limit measure $\mu$ and the joint angular measure $\Phi$ are linked through the relation

$$
\mu(\{x \in E:\|x\| \geq r, \theta(x) \in B\} \times C)=r^{-\alpha} \Phi(B \times C)
$$

for all $C \in \mathcal{B}(I), B \in \mathcal{B}(\mathbb{S})$ and $r>0$. Observe that

$$
\lim _{t \rightarrow+\infty} \frac{\mathbb{P}\{\theta(X) \in B, Y \in C,\|X\| \geq t\}}{\mathbb{P}\{\|X\| \geq t\}}=\Phi(B \times C)
$$

for all $B \in \mathcal{B}(\mathbb{S}), C \in \mathcal{B}(I)$, such that $\Phi(\partial(B \times C))=0$. In words, $\Phi$ is the asymptotic joint probability distribution of $(\theta(X), Y)$ given that $\|X\| \geq t$ as $t \rightarrow+\infty$. Notice also that $X$ 's angular (probability) measure writes $\Phi_{\theta}(B)=$ $\Phi(B \times I)$.

Let $P_{\infty}$ denote the limit conditional distribution on $E \backslash \mathbb{B} \times I$ of the pair $(X / t, Y)$ given that $\|X\| \geq t$, i.e.

$$
P_{\infty}(A \times C)=\lim _{t \rightarrow+\infty} \mathbb{P}\{X / t \in A, Y \in C \mid\|X\| \geq t\}
$$

for all $A \in \mathcal{B}(E \backslash \mathbb{B})$ and $C \in \mathcal{B}(I)$ such that $\mu(\partial(A \times C))=0$, and let $\left(X_{\infty}, Y_{\infty}\right)$ denote a random pair with distribution $P_{\infty}$. It follows immediately from (8) and from our choice $c=1$, that $P_{\infty}$ indeed exists and is determined by $(\Phi, \alpha)$, namely

$$
\begin{aligned}
P_{\infty}\{(x, y):\|x\|>r, \theta(x) \in B, y \in C\} & =\lim _{t \rightarrow+\infty} \mathbb{P}\{\|X\| / t \geq r, \theta(X) \in B, Y \in C \mid\|X\| \geq t\} \\
& =r^{-\alpha} \Phi(B \times C)
\end{aligned}
$$

where $B, C, r$ are as in Equation (8). In other words, if $T$ denotes the pseudo-polar transformation with respect to the first component $T(x, y)=(\|x\|, \theta(x), y)$ on $E \backslash \mathbb{B} \times I$, and if $\nu_{\alpha}$ is the Pareto measure $\nu_{\alpha}([x, \infty))=x^{-\alpha}$, then the following tensor product decomposition holds true in polar coordinates,

$$
P_{\infty} \circ T^{-1}=\nu_{\alpha} \otimes \Phi
$$

Observe that, under Assumptions 1 and 2 the random variable $Y_{\infty}$ is almost-surely bounded in amplitude by $M<+\infty$.

Equipped with these notations, it is natural to consider the squared error loss of a prediction function $f$, under the distribution $P_{\infty}$. We call this key quantity the extreme quadratic risk, denoted by $R_{P_{\infty}}$, defined as

$$
R_{P_{\infty}}(f):=\mathbb{E}\left[\left(Y_{\infty}-f\left(X_{\infty}\right)\right)^{2}\right]
$$

for $f \in \mathcal{F}$ a class of real-valued bounded Borel-measurable functions defined on $E \backslash \mathbb{B}$. As will become clear in the subsequent analysis, although our objective $R_{\infty}$ and the extreme risk $R_{P_{\infty}}$ are two different functionals, they turn out to be connected through their minimizers under an additional technical assumption stated below. In the sequel we let $f_{P_{\infty}}^{*}$ denote the minimizer pf $R_{P_{\infty}}$ among all measurable functions. Standard arguments from statistical learning theory show immediately that $f_{P_{\infty}}^{*}$ is defined (up to a negligible set) by a conditional expectation, $f_{P_{\infty}}^{*}\left(X_{\infty}\right)=\mathbb{E}\left[Y_{\infty} \mid X_{\infty}\right]$.

Remark 2 (Heavy-tailed input vs heavy-tailed output) Attention should be paid to the fact that the heavytail assumption is here on the distribution of the input/explanatory random variable $X$, in contrast to other works devoted to regression such as [8], [42] or [39] where it is the loss/response that is supposedly heavy-tailed. In the EVT literature, similarly, the vast majority of existing works in a regression context are concerned with extreme values of the target, in particular for extreme quantiles regression ([23, 16, 11, 17])

Assumption 3 The extreme regression function $f_{P_{\infty}}^{*}$ is continuous on $\mathbb{R}^{d} \backslash\left\{0_{\mathbb{R}^{d}}\right\}$ and as $t$ tends to infinity,

$$
\mathbb{E}\left[\left|f^{*}(X)-f_{P_{\infty}}^{*}(X)\right| \mid\|X\| \geq t\right] \rightarrow 0
$$

The next proposition highlights the weakness of Assumption 3, as long as Assumptions 11 and 22are satisfied.

Proposition 1 (Sufficient conditions for Assumption 3) Let (X,Y) satisfy Assumptions 1 and 2. Then Assumption 3 also holds if one of the three conditions (i), (ii), (iii) below holds

(i) The regression function $f^{*}$ is continuous on $\left\{x \in \mathbb{R}^{d}:\|x\| \geq 1\right\}$ and as $t \rightarrow+\infty$,

$$
\sup _{\|x\| \geq t}\left|f^{*}(x)-f_{P_{\infty}}^{*}(x)\right| \rightarrow 0
$$

(ii) The conditional distributions of $Y$ given $X=x$ (resp. $Y_{\infty}$ given $X_{\infty}=x$ ) admit densities $p_{Y \mid x}(y)$ (resp. $\left.p_{Y \mid x}^{\infty}(y)\right)$ w.r.t. the Lebesgue measure on $I$, for all $x \neq 0$. In addition for all $y \in I$, the mapping $x \mapsto p_{Y \mid x}(y)$ (resp. $\quad x \mapsto p_{Y \mid x}(y)$ ) is continuous, and $\sup _{\|x\| \geq 1, y \in I} \max p_{Y \mid x}(y), p_{Y \mid x}^{\infty}(y)<+\infty$. Finally the following uniform convergence holds true,

$$
\sup _{\|x\| \geq t, y \in I}\left|p_{Y \mid x}(y)-p_{Y \mid x}^{\infty}(y)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

(iii) The random pair $(X, Y)$ (resp. $\left(X_{\infty}, Y_{\infty}\right)$ ) has a continuous density $p$ (resp. q) w.r.t. the Lebesgue measure, and the densities converge uniformly, in the sense that

$$
\sup _{(\omega, y) \in \mathbb{S} \times I}\left|b(t) t^{d} p(t \omega, y)-q(\omega, y)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

where $b(t)=\mathbb{P}\{\|X\| \geq t\}^{-1}$. In addition, $q$ is uniformly lower bounded on the unit sphere by a positive constant,

$$
\inf _{\omega \in \mathbb{S}, y \in I} q(\omega, y)>0
$$

It should be noticed that Condition (iii) in Proposition 1 is a 'one-component variant' of standard assumptions regarding regular variations of densities ([19, 9]), further discussed in Example 2 below. We refer to Section B.1 in the Supplementary Material for a proof of Proposition 1.

We now work out several examples of regression settings in which our Assumptions 1,2 and 3 are satisfied.

Example 1 (Noise model with heavy-tailed random design) Suppose that $X$ is a regularly varying random vector in $\mathbb{R}^{d}$, independent from a real-valued random variable $\varepsilon$ modeling some noise and consider a target

$$
Y=g(X, \varepsilon)
$$

where $g: \mathbb{R}^{d} \times \mathbb{R} \rightarrow \mathbb{R}$ is a bounded, continuous mapping. Assume also that there exists a function $g_{\theta}: \mathbb{S} \times \mathbb{R} \rightarrow \mathbb{R}$ such that, for all $z \in \mathbb{R}$

$$
\sup _{\|x\| \geq t}\left|g(x, z)-g_{\theta}(x /\|x\|, z)\right| \rightarrow 0
$$

as $t \rightarrow+\infty$. Then, the random pair $(X, Y)$ fulfills Assumptions 1 , 2 and 3 .

The proof of the claim made in Example 1 is deferred to the Supplementary Material, Section B. 2 Concrete examples arise within the broader context of this generic example, such as the additive noise model $Y=\tilde{g}(X)+\varepsilon$ and the multiplicative noise model $Y=\varepsilon \tilde{g}(X)$. In both cases, Condition 14) holds true whenever $\tilde{g}$ satisfies the similar condition

$$
\sup _{\|x\| \geq t}\left|\tilde{g}(x)-\tilde{g}_{\theta}(\theta(x))\right| \rightarrow 0
$$

for some angular function $\tilde{g}_{\theta}$, with minor additional regularity assumptions. We work out the details of these two sub-examples in Section B.2. Propositions B.2 and B.3, from the Supplementary Material.

Example 2 (Predicting a missing component in a regularly varying random vector)) In this example, we show that our assumptions are met when considering a random vector $\tilde{X}$ with a regularly varying density, where the target $Y$ is one missing component from the vector, or more precisely a normalized version of that missing component. The normalization allows to satisfy our boundedness constraint Assumption 1, We believe this example could be particularly useful in applications, for imputation of missing data with heavy tails.

Let $\tilde{X} \in \mathbb{R}^{d+1}$ have continuous density $p$, and $b(t)=\mathbb{P}\{\|\tilde{X}\| \geq t\}^{-1}$, where $\|\cdot\|$ is the $L^{p}$ norm on $\mathbb{R}^{d+1}$ for some $p \in[1,+\infty)$. Assume that $b$ is regularly varying with index $\alpha$ for some $\alpha>0$, and that there exists a positive function $q$ on $\mathbb{R}^{d+1}$ such that for all $\tilde{x} \neq 0_{\mathbb{R}^{d+1}}$,

$$
t^{d+1} b(t) p(t \tilde{x})-q(\tilde{x}) \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

Assume in addition that the convergence is uniform on the sphere,

$$
\sup _{\omega \in \mathbb{S}_{d+1}}\left|t^{d+1} b(t) p(t \omega)-q(\omega)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

where $\mathbb{S}_{d+1}$ denotes the unit sphere of $\mathbb{R}^{d+1}$. This assumption is used in [19, 9]. It is shown in these references that (15) and 16) imply that $\tilde{X}$ is regularly varying with index $\alpha$. More precisely with $\mu(A)=\int_{A} q(\tilde{x}) \mathrm{d} \tilde{x}$ for any measurable set $A \subset E$, we have $b(t) \mathbb{P}\{\tilde{X} / t \in \cdot\} \rightarrow \mu(\cdot)$ in the sense of vague convergence. Necessarily $q$ is homogeneous of order $-\alpha-d-1$. Also the continuity of $p$ implies that of $q$. Assume finally that

$$
\min _{\omega \in \mathbb{S}_{d+1}} q(\omega)>0
$$

Another useful feature of this setting is that, if (15) and (16) hold, then also

$$
\sup _{\|\tilde{x}\| \geq 1}\left|p(t \tilde{x}) t^{d+1} b(t)-q(\tilde{x})\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

Let $X=\left(\tilde{X}_{1}, \ldots, \tilde{X}_{d}\right)$ and $Y=\tilde{X}_{d+1} /\|\tilde{X}\|$. The norm $\|x\|$ also denotes the $L^{p}$ norm in $\mathbb{R}^{d}$ when it is clear from the context that $x \in \mathbb{R}^{d}$. Then

(i) The pair (X,Y) satisfies Assumptions 1, 2 and 3;

(ii) The limit pair $\left(X_{\infty}, Y_{\infty}\right)$ for $(X, Y)$ defined in (9) has distribution

$$
\mathcal{L}\left(\left.\left(\tilde{X}_{\infty, 1: d}, \frac{\tilde{X}_{\infty, d+1}}{\left\|\tilde{X}_{\infty}\right\|}\right) \right\rvert\,\left\|\tilde{X}_{\infty, 1: d}\right\| \geq 1\right)
$$

where $\tilde{X}_{\infty, 1: d}$ denotes the d-dimensional vector $\left(\tilde{X}_{\infty, 1}, \ldots, \tilde{X}_{\infty, d}\right)$.

It is important to observe that predicting $Y$ allows to predict $\tilde{X}_{d+1}$, as

$$
Y=\frac{\tilde{X}_{d+1}}{\|\tilde{X}\|_{p}} \quad \Longleftrightarrow \quad \tilde{X}_{d+1}=\frac{Y\|X\|_{p}}{\left(1-|Y|^{p}\right)^{1 / p}}
$$

In our experiments with real data we consider this prediction example on a financial dataset.

As will be shown in the forthcoming sections, Assumptions 1,2 and 3 provide sufficient regularity and stability conditions allowing to justify the angular ERM approach taken in Algorithm 1.

## 3 Regression on Extremes - Main Results

### 3.1 Structural Analysis of Minimizers: Conditional, Asymptotic and Extreme Risks

The main purposes of this subsection are to show that under the assumptions previously listed, $(i)$ the extreme quadratic risk $R_{P_{\infty}}$ is minimized by angular prediction functions, that is functions depending on the input through the angle only ; (ii) Although $R_{\infty}$ and $R_{P_{\infty}}$ are different risk functionals, they are connected through their respective minimizers and minimum values.

The first objective $(i)$ above is easily tackled. Indeed, the discussion below Equation (9) shows that, under Assumption 2, letting $\Theta_{\infty}=\theta\left(X_{\infty}\right)$ denote the angular component of $X_{\infty}$, the random pair $\left(\Theta_{\infty}, Y_{\infty}\right)$ is independent
from the norm $\left\|X_{\infty}\right\|$, and in particular $Y_{\infty}$ and $\left\|X_{\infty}\right\|$ are independent. Hence, the only useful piece of information carried by $X_{\infty}$ to predict $Y_{\infty}$ is its angular component $\Theta_{\infty}$. As a consequence the Bayes regression function satisfies $f_{P_{\infty}}^{*}\left(X_{\infty}\right)=\mathbb{E}\left[Y_{\infty} \mid X_{\infty}\right]=\mathbb{E}\left[Y_{\infty} \mid \Theta_{\infty}\right]$ almost-surely. As a consequence we may write $f_{P_{\infty}}^{*}=h_{\infty} \circ \theta$ for some function $h_{\infty}$ defined on the sphere $\mathbb{S}$. Finally, Assumption 3 ensures that $h_{\infty}$ may be chosen as a continuous function. We summarize the discussion:

Lemma 1 Under Assumptions 1, 2, 3, the extreme risk $R_{P_{\infty}}$ has a minimizer (among all measurable functions) which may be written as $f_{P_{\infty}}^{*}(x)=h_{\infty} \circ \theta(x)$ where $h_{\infty}: \mathbb{S} \rightarrow I$ is a bounded, continuous function.

The next result brings answers regarding the objective (ii) outlined above, by establishing a key connection between the (seemingly) different problems of minimizing $R_{\infty}$ on the one hand, and minimizing $R_{P_{\infty}}$ on the other hand. Recall from Section 2.3 that the extreme risk $R_{P_{\infty}}(f)=\mathbb{E}\left[\left(f\left(X_{\infty}\right)-Y_{\infty}\right)^{2}\right]$ and the asymptotic risk

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-09.jpg?height=55&width=1734&top_left_y=669&top_left_x=190)
is only defined as a minimizer of the extreme risk $R_{P_{\infty}}$ and not the asymptotic risk $R_{\infty}$. In the sequel we denote by $R_{P_{\infty}}^{*}$ the minimum value of the extreme risk, i.e. $R_{P_{\infty}}^{*}:=\inf _{f \text { measurable }} R_{P_{\infty}}(f)=R_{P_{\infty}}\left(f_{P_{\infty}}^{*}\right)$.

Theorem 1 Under Assumptions 1 and 2 , we have

(i) For any angular function of the kind $f(x)=h \circ \theta(x)$, where $h$ is a continuous function defined on $\mathbb{S}$, the conditional risk converges to the extreme risk, i.e.

$$
R_{t}(f) \underset{t \rightarrow \infty}{\longrightarrow} R_{P_{\infty}}(f)
$$

Thus for such prediction functions, $R_{\infty}(f)=\lim _{t \rightarrow+\infty} R_{t}(f)=R_{P_{\infty}}(f)$.

If in addition Assumption 3 is satisfied, then the following assertions hold true.

(ii) As $t \rightarrow+\infty$ : the minimum value of $R_{t}$ converges to that of $R_{P_{\infty}}$, i.e. $R_{t}^{*} \underset{t \rightarrow+\infty}{\longrightarrow} R_{P_{\infty}}^{*}$.

(iii) The minimum values of $R_{\infty}$ and $R_{P_{\infty}}$ coincide, i.e. $R_{\infty}^{*}=R_{P_{\infty}}^{*}$.

(iv) The regression function $f_{P_{\infty}}^{*}$ minimizes the asymptotic conditional quadratic risk:

$$
R_{\infty}^{*}=R_{\infty}\left(f_{P_{\infty}}^{*}\right)
$$

The proof is deferred to Section C.1 in the Supplementary Material. Observe that Theorem 1 does not assert that $R_{t}(f)$ converges to $R_{P_{\infty}}(f)$ for all $f$, but the convergence holds true for angular predictors $f=h \circ \theta$ (Property $(i)$ in the statement). Property (iv) discloses that the solution $f_{P_{\infty}}^{*}$ of the extreme risk minimization problem, which is of angular type, is also a minimizer of the asymptotic conditional quadratic risk $R_{\infty}$ (and that the minima coincide). Because $f_{P_{\infty}}^{*}=h_{\infty} \circ \theta$ is of angular type, we thus obtain, under Assumptions 1,2 and 3

$$
\inf _{f \text { measurable }} R_{\infty}(f)=\inf _{h \text { measurable }} R_{\infty}(h \circ \theta)
$$

In other words, the search for minimizers of $R_{\infty}$ may indeed be restricted to angular prediction functions, which provides a first heuristic justification for Algorithm 1. However in order to provide rigorous guarantees regarding minimizers of the empirical criterion (4) from Algorithm 1 , further assumptions regarding the class $\mathcal{H}$ of angular predictors are needed. In particular these additional assumptions ensure uniformity of the convergence result $(i)$ from Theorem 1. This is the focus of the next section.

### 3.2 Statistical Learning Guarantees

This section provides a nonasymptotic analysis of the approach proposed for regression on extremes. An upper confidence bound for the excess of $R_{\infty}$-risk of a solution of (4) is established, when the class $\mathcal{H}$ over which empirical minimization is performed is of controlled complexity, see Assumption 4 below.

The rationale behind the approach proposed in Algorithm 1 is to find an angular predictive function that nearly minimizes the asymptotic conditional quadratic risk $R_{\infty}$ (3). Our ERM strategy thus consists in solving an empirical version of the nonasymptotic optimization problem

$$
\min _{h \in \mathcal{H}} R_{t}(h \circ \theta)
$$

Recall that a heuristic justification for considering angular classifiers is given by Identity (18), which is itself a consequence of Theorem 1. The radial threshold $t$ is chosen as a relatively high quantile of the empirical distribution of the radii $\left\|X_{i}\right\|$. In particular, let $t_{n, k}$ denote the $1-k / n$ quantile of the norm $\|X\|$, where $k \ll n$ is large enough so that a statistical analysis remains realistic, but small enough so that the the distribution of $(X, Y)$ given that $\|X\|>t_{n, k}$ is close to the limit $P_{\infty}$, see (9). Then an empirical version of $t_{n, k}$ is $\hat{t}_{n, k}=\left\|X_{(k)}\right\|$, the $k^{t h}$ largest order statistic of the norm already introduced in Algorithm 1. In practice the number $k$ of retained extreme values statistics in a recurrent issue in Extreme Value Analysis, for which no definite theoretical answer exists, but which is a standard bias/variance compromise. In our experiments, following standard practice we choose $k$ by inspection of stability regions in Hill plots. In addition, in a regression setting we consider feature importance summaries relative to the radial variable, see Section 4 for details.

Summarizing, the objective minimized in Algorithm 1 may be viewed as an empirical version of the conditional risk $R_{t_{n, k}}$ for a predictive mapping of the form $h \circ \theta$. In the sequel we denote by $\hat{R}_{k}$ this empirical objective,

$$
\hat{R}_{k}(f)=\frac{1}{k} \sum_{i=1}^{k}\left(Y_{(i)}-f\left(X_{(i)}\right)\right)^{2}
$$

We point out that the statistic above is not an average of independent random variables, as it involves extreme order statistics of the norm. Thus investigating its concentration properties is far from straightforward. The minimum is taken over a class $\mathcal{H}$ of continuous bounded functions on $\mathbb{S}$ of controlled complexity but hopefully rich enough to contain a reasonable approximant of $h_{\infty}$ introduced in Lemma 11 The following assumption regarding $\mathcal{H}$ will turn out to be sufficient to obtain a control of the deviations of the empirical risk. In order to avoid measurability issues regarding supremum deviations over the class $\mathcal{H}$, it is assumed throughout that $\mathcal{H}$ is pointwise measurable (see [52], Example 2.3.4), i.e. that there exists a countable family $\mathcal{H}_{0} \subset \mathcal{H}$, such that for all $\omega \in \mathbb{S}$ and all $h \in \mathcal{H}$, there is a sequence $\left(h_{i}\right)_{i \geq 1} \in \mathcal{H}_{0}$ such that $h_{i}(\omega) \rightarrow h(\omega)$. This mild condition is satisfied in most practical cases, in particular by parametric classes $\mathcal{H}$, i.e. classes indexed by a finite dimensional parameter $\beta \in \mathbb{R}^{p}$, which depend continously on the parameter, i.e. such that $\left\|h_{\beta}-h_{\beta_{n}}\right\|_{\infty, \mathbb{S}} \rightarrow 0$ as $\beta_{n} \rightarrow \beta$.

Assumption 4 The pointwise measurable class $\mathcal{H}$ is a family of continuous, real-valued functions defined on $\mathbb{S}$; of $\mathrm{VC}$ dimension $V_{\mathcal{H}}<+\infty$, and uniformly bounded by the same constant as the target $Y$ (see Assumption 1), $\forall h \in \mathcal{H}, \forall \omega \in \mathbb{S},|h(\omega)| \leq M$.

Under the complexity hypothesis above, the following result provides an upper confidence bound for the maximal deviations between the conditional quadratic risk $R_{t_{n, k}}$ and its empirical version $\hat{R}_{k}$, uniformly over the class $\mathcal{H}$.

Notice that a similar result is obtained in 2 (Lemma A.3) in the more complex setting of cross validation. For the sake of completeness, we provide a detailed proof in Section $\overline{C .2}$ of the Supplementary Material.

Theorem 2 Suppose that Assumptions 11 and 4 are satisfied. Let $\delta \in(0,1)$. We have with probability larger than $1-\delta$ :

$$
\sup _{h \in \mathcal{H}}\left|\hat{R}_{k}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right| \leq \frac{8 M^{2} \sqrt{2 \log (3 / \delta)}+C \sqrt{V_{\mathcal{H}}}}{\sqrt{k}}+\frac{16 M^{2} \log (3 / \delta) / 3+4 M^{2} V_{\mathcal{H}}}{k}
$$

where $C$ is a universal constant.

Notice that Theorem 2 controls only the statistical deviations between the sub-asymptotic risk $R_{t_{n, k}}$ and its empirical version $\hat{R}_{k}$. A control of the bias term $R_{t_{n, k}}-R_{\infty}$ is given next, under appropriate complexity assumptions controlling the complexity of class $\mathcal{H}$. In particular Assumption 4 can be traded against a total boundedness assumption (Case 1. in Proposition 2 below) which is further discussed below (Remark 3). Regarding the second set of assumption (Case 2.), notice that for $t \geq 1$, the conditional distribution $\Phi_{\theta, t}=\mathcal{L}(\theta(X) \mid\|X\| \geq t)$ is absolutely continuous w.r.t. $\Phi_{\theta, 1}=\mathcal{L}(\theta(X) \mid\|X\| \geq 1)$. Indeed for any measurable set $A \subset \mathbb{S}$, if $\mathbb{P}\{\Theta \in A \mid\|X\| \geq 1\}=0$ then also for any $t \geq 1, \mathbb{P}\{\Theta \in A \mid\|X\| \geq t\}=0$. Denote by $\phi_{\theta, t}$ the probability density of the former angular distribution with respect to the latter.

Proposition 2 Suppose that Assumptions 1 and 2 are satisfied. Let $\mathcal{H}$ be a class of real-valued, continuous functions on $\mathbb{S}$. Assume that one out of the two following conditions is satisfied.

1. $\mathcal{H}$ is totally bounded in the space $\left(\mathcal{C}(\mathbb{S}),\|\cdot\|_{\infty}\right)$ of continuous functions on $\mathbb{S}$ endowed with the supremum norm, or
2. $\mathcal{H}$ fulfills Assumption 4 and in addition, suppose that the conditional densities $\phi_{t}$ introduced above the statement satisfy

$$
\sup _{t \geq 1, \omega \in \mathbb{S}} \phi_{\theta, t}(\omega)=D
$$

for some $0<D<\infty$.

Then, as t tends to infinity, we have

$$
\sup _{h \in \mathcal{H}}\left|R_{t}(h \circ \theta)-R_{\infty}(h \circ \theta)\right| \rightarrow 0
$$

The proof of Proposition 2 is deferred to Section C. 3 of the Supplementary Material.

Remark 3 (Totally bounded family of regression functions) Relying on a topological assumption on a set of regression functions such as total boundedness (i.e. $\mathcal{H}$ may be covered by finitely many balls of radius $\varepsilon$, for any $\varepsilon>0)$ is rather uncommon in statistical learning. However it turns out that this condition encompasses several standard algorithms. Namely, if $\mathcal{H}$ is a parametric family indexed by a bounded parameter set, i.e. $\mathcal{H}=\left\{h_{\beta}, \beta \in B\right\}$ for some $B \subset \mathbb{R}^{p}$ of finite diameter, and if $h_{\beta}$ is Lipschitz-continuous with respect to $\beta$, i.e. for some $C>0$, $\left\|h_{\beta}-h_{\gamma}\right\|_{\infty} \leq C\|\beta-\gamma\|$ for all $\beta, \gamma \in B$, then $\mathcal{H}$ satisfies Condition 1. from Proposition 2. As an example let $p=d$ and for $\omega \in \mathbb{S}$, let $h_{\beta}(\omega)=\langle\beta, \omega\rangle$, with a bounded parameter set $B=\left\{\beta \in \mathbb{R}^{d}:\|\beta\|_{q} \leq \lambda\right\}$ for some fixed $\lambda>0$, where $\|\cdot\|$ is the $L^{q}$ norm on $\mathbb{R}^{d}, q \geq 1$. The case $q=2$ (resp. $q=1$ ) corresponds to a constrained Ridge (resp. Lasso) regression.

Remark 4 (Bounded angular densities) The second condition in Proposition 2 implies that the angular measure $\Phi_{\theta, t}$ for large $t$ may not concentrate around sets that are negligible with respect to the 'bulk' angular measure $\Phi_{\theta, 1}$. This excludes situations where the limit angular measure $\Phi_{\theta}$ concentrates on lower dimensional subcones of $\mathbb{R}^{d}$, whereas $\Phi_{\theta, 1}$ does not necessarily do so. This concentration phenomenon as $t \rightarrow+\infty$ is precisely the framework considered in recent works on unsupervised dimension reduction for extremes where the goal is to uncover sparsity patterns in the limit angular measure $\Phi_{\theta}$ which may not be representative of the bulk behavior ([28, 29, 43, 43, [13, 20, 15]). How to relax Condition 2. in order to encompass such frameworks even though the family $\mathcal{H}$ does not satisfy Condition 1. is left to future research.

The corollary below summarizes the main results of Sections 3.1 and 3.2 in the form of an upper confidence bound for the excess of $R_{\infty}$-risk for any solution $\hat{f}_{k}$ of the problem

$$
\min _{h \in \mathcal{H}} \hat{R}_{k}(h \circ \theta)
$$

Corollary 1 (Summary) Let $\hat{f}_{k}=\hat{h}_{k} \circ \theta$ be the prediction function issued by Algorithm 1, Let Assumptions 1, 2. 3 and 4 be satisfied. Recall $h_{\infty}$ from Lemma 1] and that, from Theorem 1, $R_{\infty}\left(h_{\infty} \circ \theta\right)=\inf _{h}$ measurable $R_{\infty}(h \circ \theta)=R_{\infty}^{*}$.

For any $\delta>0$, with probability at least $1-\delta$, the excess $R_{\infty}$-risk of $\hat{f}_{k}$ satisfies

$$
R_{\infty}\left(\hat{f}_{k}\right)-R_{\infty}^{*} \leq D_{k}+B_{1}\left(t_{n, k}\right)+B_{2}(\mathcal{H})
$$

where $D_{k}, B_{1}, B_{2}$ are respectively a deviation term and two bias terms,

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-11.jpg?height=216&width=1038&top_left_y=1816&top_left_x=538)

The first bias term $B_{1}\left(t_{n, k}\right)$ in the above bound converges to zero as $n \rightarrow+\infty, k \rightarrow+\infty, k / n \rightarrow 0$ whenever the conditions of Proposition 2 are met.

PROOF. Assume for simplicity that the infimum of the $R_{\infty}$-risk over the class $\mathcal{H}$ is reached, i.e. $\exists h_{\mathcal{H}} \in \mathcal{H}$ : $R_{\infty}\left(h_{\mathcal{H}} \circ \theta\right)=\inf \left\{R_{\infty}(h \circ \theta), h \in \mathcal{H}\right\}$ (if this is not the case, consider an $\varepsilon$-minimizer $h_{\varepsilon}$ for arbitrarily small $\varepsilon$, and proceed). Thus

$$
\begin{aligned}
R_{\infty}\left(\hat{f}_{k}\right)-R_{\infty}^{*} & \leq R_{\infty}\left(\hat{h}_{k} \circ \theta\right)-R_{t_{n, k}}\left(\hat{h}_{k} \circ \theta\right)+R_{t_{n, k}}\left(\hat{h}_{k} \circ \theta\right)-\hat{R}_{k}\left(\hat{h}_{k} \circ \theta\right) \\
& +\hat{R}_{k}\left(\hat{h}_{k} \circ \theta\right)-\hat{R}_{k}\left(h_{\mathcal{H}} \circ \theta\right)+\hat{R}_{k}\left(h_{\mathcal{H}} \circ \theta\right)-R_{t_{n, k}}\left(h_{\mathcal{H}} \circ \theta\right) \\
& +R_{t_{n, k}}\left(h_{\mathcal{H}} \circ \theta\right)-R_{\infty}\left(h_{\mathcal{H}} \circ \theta\right)+R_{\infty}\left(h_{\mathcal{H}} \circ \theta\right)-\inf _{h \text { measurable }} R_{\infty}(h \circ \theta) \\
& +\inf _{h \text { measurable }} R_{\infty}(h \circ \theta)-\inf _{f \text { measurable }} R_{\infty}(f)
\end{aligned}
$$

Because $\hat{h}_{k} \circ \theta$ minimizes $\hat{R}_{k}$ and considering identity (18) (which holds because of Assumptions 1, 2, 3), the above decomposition simplifies into

$$
R_{\infty}\left(\hat{f}_{k}\right)-R_{\infty}^{*} \leq 2 \sup _{h \in \mathcal{H}}\left|R_{\infty}-R_{t_{n, k}}\right|(h \circ \theta)+2 \sup _{h \in \mathcal{H}}\left|R_{t_{n, k}}-\hat{R}_{k}\right|(h \circ \theta)+R_{\infty}\left(h_{\mathcal{H}} \circ \theta\right)-\inf _{h \text { measurable }} R_{\infty}(h \circ \theta)
$$

The result follows by plugging in the deviation bound from Theorem 2

As it is generally the case in statistics of extremes, two types of bias terms are involved in the upper bound 20 ) of Corollary 1. The first bias term $B_{1}(t)$ results from the substitution of the conditional quadratic risk $R_{t_{n, k}}$ for its asymptotic limit $R_{\infty}$. While the weak additional assumptions of Proposition 2 ensure that this bais term vanishes fas $k / n \rightarrow 0$, a quantification of its decay rate would require second-order conditions, e.g. by extending the second order regular variation setting of 48 to our context of joint regular variation.

The second bias term is a model bias, induced by restricting the family of all measurable functions on $\mathbb{S}$ to the class $\mathcal{H}$ of controlled combinatorial complexity. It should be noted that under the conditions of the statement, Identity (18) ensures that restricting to angular predictors does not induce any additional bias term compared with considering a standard class for predictors taking the full covariate (including the radius) as input.

Remark 5 (Rate of convergence) To establish the concentration bound stated in Theorem Q, we employ general concentration results that are not ideally tailored for a regression context. A more detailed investigation might yield a bound on the stochastic error term of order $O(\log (k) / k)$, as suggested by standard concentration results (refer to [31], sec. 11). This refined study is left to future work.

Remark 6 (Extensions) This article presents a rigorous formulation and investigation of the regression problem involving an output variable confronted to a heavy-tailed input variable, a so far unexplored topic in academic research. Subsequently, we anticipate that the straightforward adaptation of the proposed methodology to incorporate regularized risk formulations or diverse cost functions holds the potential for practical utility and improvements. These extensions lie outside the scope of this paper and are deferred to further works.

Remark 7 (Alternative to ERM) In the case where the output/response variable $Y$ is heavy-tailed (or possibly contaminated by a heavy-tailed noise), robust alternatives to the ERM approach exist and are preferable ([39]). Extension of these robust alternatives to the present context of heavy-tailed input is beyond the scope of this paper but will be the subject of further research.

## 4 Numerical Experiments

We now investigate the performance of the approach previously described and theoretically analyzed for regression on extremes from an empirical perspective on several simulated and real datasets. The code used to run our experiments is available at https://bitbucket.org/nathanhuet/extremeregression. The MSE in extreme regions of angular regression functions output by specific implementations of Algorithm 1]are compared to those of the classic regression functions, learned in a standard fashion. On this occasion we propose a simple graphical diagnostic procedure allowing to check visually whether the data meet our assumptions, in particular Assumption 2 which is central in our work. More precisely we inspect the relative importance of the radial variable $\|X\|$ for predicting $Y$ above increasing radial thresholds. We consider in Section 4.1 simulated data in the additive and multiplicative models which are particular instances of Example 1. In Section 4.2 we consider a real-life financial dataset which has already been studied in an EVA context [44.

### 4.1 Simulated data

Experimental Setting. As a first go, we focus on predictive performance of Algorithm 1 in terms of Mean Squared Error (MSE), with simulated data respectively from an additive noise model and from a multiplicative noise model with heavy-tailed design, $Y=\tilde{g}_{0}(X)+\varepsilon_{0}$, and $Y=\varepsilon_{1} \tilde{g}_{1}(X)$, where $\|\cdot\|=\|\cdot\|_{2}, \tilde{g}_{0}(x)=\beta^{T} \theta(x)(1+1 /\|x\|)$, and $\tilde{g}_{1}(x)=\cos (1 /\|x\|) \sum_{i=1}^{d / 2}\left(\theta(x)_{2 i-1}-1 /\|x\|^{2}\right) \sin \left(\left(\theta(x)_{2 i}-1 /\|x\|^{2}\right) \pi\right)$, for $x \in \mathbb{R}^{d}$.

Both models satisfy our assumptions (see Proposition B.2 in the Supplementary Material). In the additive model (resp. in the multiplicative model) the design $X$ is generated according to a multivariate extreme value distribution from the logistic family [51] with dependence parameter $\xi=1$, which means that extreme observations occur very close to the axes (resp. $\xi=0.7$, meaning that the angular component of extreme observations is relatively spread-out in the positive orthant of the unit sphere). The input 1-d marginals are standard Pareto with shape parameter $\alpha=1$ (resp. $\alpha=3$ ) and the noise $\varepsilon_{0}$ is defined as a truncated Gaussian variable on

Table 1: Average MSE (and standard deviation) for regression functions trained using all observations, extreme observations and angles of extreme observations, over 10 independent replications of the dataset generated in the additive and the multiplicative noise models.

| Methods/Models | Train on $X$ | TRain on $X \mid\\|X\\|$ LARGe | TRaIN ON $\Theta \mid\\|X\\|$ LARGE |
| :---: | :---: | :---: | :---: |
| Add.: OLS | $23 \pm 29$ | $3 \pm 6$ | $\mathbf{0 . 0 0 3} \pm \mathbf{0 . 0 0 1}$ |
| SVR | $0.13 \pm 0.01$ | $0.05 \pm 0.02$ | $\mathbf{0 . 0 0 3} \pm \mathbf{0 . 0 0 1}$ |
| RF | $0.012 \pm 0.004$ | $0.007 \pm 0.002$ | $\mathbf{0 . 0 0 4} \pm \mathbf{0 . 0 0 1}$ |
| Mult.: OLS | $0.006 \pm 0.001$ | $0.003 \pm 0.001$ | $\mathbf{0 . 0 0 1} \pm \mathbf{0 . 0 0 1}$ |
| SVR | $0.0041 \pm 0.0002$ | $0.0038_{ \pm 0.0004}$ | $\mathbf{0 . 0 0 3 4} \pm \mathbf{0 . 0 0 0 3}$ |
| RF | $0.0020 \pm 0.0001$ | $0.0013 \pm 0.0001$ | $\mathbf{0 . 0 0 0 4} \pm \mathbf{0 . 0 0 0 1}$ |

$[-1,1]$ with zero mean and standard deviation $\sigma_{0}=0.1$, i.e. $\varepsilon_{0}$ admits the probability density $f_{\varepsilon_{0}}(x)=\mathbb{1}\{|x| \leq$ $1\} \exp \left(-x^{2} /\left(2 \sigma_{0}^{2}\right)\right) / \int_{-1}^{1} \exp \left(-z^{2} /\left(2 \sigma_{0}^{2}\right)\right) d z$. For the multiplicative model, $\varepsilon_{1}$ is again a truncated Gaussian variable on $[0,2]$ with mean $\mu=1$ and standard deviation $\sigma_{1}=0.1$, i.e. $\varepsilon_{1}$ has density $f_{\varepsilon_{1}}(x)=\mathbb{1}\{0 \leq x \leq 2\} \exp (-(x-$ $\left.\mu)^{2} /\left(2 \sigma_{1}^{2}\right)\right) / \int_{0}^{2} \exp \left(-(z-\mu)^{2} /\left(2 \sigma_{1}^{2}\right)\right) d z$.

The simulated data are of dimension $d=7$ (resp. $d=14$ ). For both models, the size of the training dataset is $n_{\text {train }}=10000$, and the number of extreme observations retained for training Algorithm 1 is set to $k_{\text {train }}=1000$ $\left(=n_{\text {train }} / 10\right)$. The size of the test dataset is $n_{\text {test }}=100000$ and the $k_{\text {test }}=10000\left(=n_{\text {test }} / 10\right)$ largest instances are used to evaluate predictive performance on extreme covariates. We consider three different regression algorithms implemented in the scikit-learn library [47] with the default parameters, namely Ordinary Least Squares (OLS), Support Vector Regression (SVR), and Random Forest (RF). Predictive functions are learned using respectively (i) the full training dataset, (ii) a reduced dataset composed of the $k_{\text {train }}$ largest observations $X_{(1)}, \ldots X_{\left(k_{t r a i n}\right)}$, and (iii) an angular dataset $\Theta_{(1)}, \ldots \Theta_{\left(k_{\text {train }}\right)}$ consisting of the angles of the $k_{\text {train }}$ largest observations. These three options correspond respectively to (i) the default strategy (using the full dataset), (ii) a 'reasonable' naive strategy (training on extreme covariates for the purpose of predicting from extreme covariates), (iii) the strategy that we promote in this paper, corresponding to Algorithm 1. We evaluate the performance of the outputs using the MSE computed on the test set. Table 1) shows the average MSE's when repeating this experiment across $E=10$ independent replications of the dataset. For the additive model the regression parameter $\beta$ is randomly chosen for each replication, namely each entry of $\beta$ is drawn uniformly at random over the interval $[0,1]$.

With both models, the approach we promote for regression on extremes clearly outperforms its competitors, no matter the algorithm (i.e. the model bias) considered. This paper being the first to consider regression on extremes (see Remark 7 for a description of regression problems of different nature with heavy-tailed data), no other alternative approach is documented in the literature.

Besides prediction performance, we propose to assess the validity of our main modeling assumption (Assumption 2 by inspecting the variable importance (a.k.a. feature importance, see e.g. 30] and the references therein) of the radial variable $\|X\|$ compared with the angular variables $\Theta_{j}, j \leq d$, for the purpose of predicting the target $Y$. Indeed, under Assumption 2, the variables $Y$ and $\|X\|$ are asymptotically independent conditional on $\|X\|>t$ as $t \rightarrow+\infty$, so that the variable importance of $\|X\|$, when restricting the training set to regions above increasingly large radial thresholds, should in principle vanish.

We consider here two widely used measures of feature importance, Gini importance (or Mean Decrease of Impurity, [45, 7]) and Permutation feature importance [4] in the context of Random Forest prediction, as implemented in the scikit-learn library. Gini importance measures a mean decrease of impurity in a forest of trees, between parent nodes involving a split on the considered variables, and their child nodes. Permutation importance compares the prediction performance of the original input dataset with the same dataset where the values of the considered variable have been randomly shuffled. Both scores are normalized so that the sum of all importance scores across variables equals 1 . A large score indicates a high predictive value of the variable.

The aim of this second experiment is to illustrate the decrease of the radial feature importance for reduced datasets involving increasingly (relatively) large inputs. To cancel out the perturbation effect of reduced sample sizes, we fix a training size $k_{i m p}=1000$ and we simulate increasingly large datasets of size

$$
n_{i m p} \in\left\{k_{i m p}, 2 k_{i m p}, \ldots, 10 k_{i m p}\right\}
$$

in the additive and multiplicative models described above. Then for $j \in\{1, \ldots, 10\}$ the $k_{i m p}$ largest observations in terms of $\|X\|$ among $n_{i m p}=j k_{i m p}$ are retained, a random forest is fitted with input variables $\left(\|X\|, \Theta_{1}, \ldots, \Theta_{d}\right)$,
and the Gini and Permutation scores are computed. Figure 1 shows the average scores obtained over 10 independent experiments, together with interquantile ranges, as a function of the full sample size $n_{i m p}$. In both models, the decrease of both scores is obvious. In particular in terms of Gini measure, the relative importance of the radius decreases from $38 \%$ to $1 \%$ for the additive model and from $6 \%$ to $<1 \%$ for the multiplicative model.

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-14.jpg?height=456&width=1656&top_left_y=428&top_left_x=213)

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-14.jpg?height=382&width=727&top_left_y=438&top_left_x=230)

Additive model.

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-14.jpg?height=388&width=729&top_left_y=435&top_left_x=1121)

Multiplicative model.

Figure 1: Average permutation and Gini importance measures of the radial variable using the RF algorithm in the additive noise model (left) and the multiplicative noise model (right) over 10 replications, as a function of the total sample size $n_{i m p}$ for fixed extreme training size $k_{i m p}$. Solid black line: average Gini importance. Solid grey line: average Permutation importance. Dashed lines: empirical 0.8-interquantile ranges.

### 4.2 Real data

Encouraged by this first agreement between theoretical and numerical results, experiments on real data are conducted. We place ourselves in the setting of Example 2 where the target is one particular variable in a multivariate regularly varying random vector. We consider a financial dataset, namely 49 Industry Portfolios [Daily] from Kenneth R. French - Data Library (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library. html). A study of extremal clustering properties within this dataset has already been carried out by [44]. This dataset comprises daily returns of 49 industry portfolios, within the time span from January 5th, 1970 to October 31st, 2023. Rows containing any NA values are removed, resulting in a dataset of dimension $d=49$ and size $n=13577$. Figure 2 displays a Hill plot of the radial variable (w.r.t. $\|\cdot\|_{2}$ ), with a rather wide stability region, roughly between $k=500$ and $k=2000$, which suggests that regular variation is indeed present, with regular variation index $\alpha \approx 3.2$. We consider separately the first three variables as output (target) variables, namely AGRIC (i.e. "Agriculture"), FOOD (i.e. "Food Products"), and Soda (i.e. "Candy and Soda"). Each choice of a target variable yields a regression problem consisting of predicting the target based on a covariate vector of dimension $d=10$ composed of the 10 variables $\left(\tilde{X}_{1}, \ldots, \tilde{X}_{d}\right)$ which are the most correlated with the target $\tilde{X}_{d+1}$. Following the workflow of Example 2 as an intermediate step, Algorithm 1 is used to predict $Y=X_{d+1} /\|\tilde{X}\|$ where $\tilde{X}=\left(\tilde{X}_{1}, \ldots, \tilde{X}_{d+1}\right)$. The output $\hat{Y}$ of Algorithm 1 is then plugged in the formula $\tilde{X}_{d+1}=Y\|X\| / \sqrt{1-Y^{2}}$ where $X=\left(X_{1}, \ldots, X_{d}\right)$, which yields an estimate $\hat{X}_{d+1}$ for the target variable. The dataset is randomly split into a test set of size $n_{\text {test }}=4073$ ( $30 \%$ of the data), and a train set of size $n_{\text {train }}=9504=n-n_{\text {test }}$. As suggested by the Hill plot (Figure 2), the number $k_{\text {train }}$ of extreme observations used at the training step is set to $k_{\text {train }}=\left\lfloor n_{\text {train }} / 5\right\rfloor=1900$. On the other hand, at the testing step, to evaluate the extrapolation performance of our method, we fix $k_{\text {test }}$ to a smaller fraction of the test set, $k_{\text {test }}=\left\lfloor n_{\text {test }} / 10\right\rfloor=407$. In this setting, paralleling our experiments with simulated data, we compare the performance of regression functions learned using the full training dataset, the truncated version composed of the the $k_{\text {train }}$ largest observations and the angles of the truncated version. For the sake of realism, we report the MSE regarding prediction of the original target variable $\tilde{X}_{d+1}$, i.e. $\left(\tilde{X}_{d+1}-\hat{X}_{d+1}\right)^{2}$, which would be of greater interest in applications than the error in the transformed variable $(Y-\hat{Y})^{2}$. Notice that our theory provides guarantees for the latter, not the former. The results gathered in Table 2 are the average MSE's obtained when repeating 10 times the procedure described above with random splits of the dataset into a train and a test set. These results provide evidence that conditionally on the other (covariate) variables being large, our method ensures, in most cases, better reconstruction of the target variable than the default strategy (first column) and the intermediate strategy (second column). For predicting the SODA variable however, the default strategy with OLS obtains the best scores. This suggests that convergence of the conditional distribution of excesses towards its limit as in (5) is somewhat slower for the subvector $\left(\tilde{X}_{1}, \ldots, \tilde{X}_{d+1}\right)$ where $\tilde{X}_{d+1}$ is SODA and $\tilde{X}_{1}, \ldots, \tilde{X}_{d}$ are the 10 selected variables based on their correlation with SODA. This intuition is confirmed by the graphs of variable

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-15.jpg?height=756&width=1466&top_left_y=283&top_left_x=297)

Figure 2: Hill plot for the radial variable of the 49 Industry Portfolio Daily dataset: estimation of the extreme value index $\gamma=1 / \alpha$ with the Hill estimator using the $k$ largest order statistics of $\|X\|$, as a function of $k$.

importance displayed in Figure 3, again paralleling the ones of Figure 1 and fully described in Section 4.1 In Figure 3. for simplicity, the importance scores are computed in a prediction task where the covariate vector includes all the available variables, except from the target (48 of them). Also the target variable for the RF algorithm is

the rescaled variable $Y=\tilde{X}_{d+1} /\|\tilde{X}\|$. Whereas the radial importances decreases monotonically when the target variable in AGRIC and FOOD, the third panel dedicated to the target variable SODA displays a local maximum in radial importance around $n=11000$. This value corresponds to a ratio $k / n \approx 1 / 12$ which is near the ratio $1 / 10$ considered for the testing step in our experimental results reported in Table 2 This may explain our comparatively poor results for this particular variable. However for all three target variables, overall, both Gini and Permutation importance score decrease significantly, as the ratio $k / n$ decreases. In particular for Gini importance, the relative radial importances are approximately $2 \% \approx 1 / 48$ when $n=k$, which is to be expected when all variables have equal importance. On the other hand when $n=10 k$, all three Gini importances are less than $1 \%$.

## 5 Conclusion

We have provided a sound ERM approach to the generic problem of statistical regression on extreme values. The asymptotic framework we have developed crucially relies on the (novel) notion of joint regular variation w.r.t. some multivariate component. When the distribution of the couple $(X, Y)$ is regularly varying w.r.t. $X$ 's component, the problem can be stated and analyzed in a rigorous manner. We have described the optimal solution and proved that it can be nearly recovered with nonasymptotic guarantees by implementing a variant of the ERM principle, based on the angular information carried by a fraction of the largest observations only. We have also carried out numerical experiments to support the approach promoted, highlighting the necessity of using a dedicated methodology to perform regression on extreme samples with guarantees.

Table 2: Average MSE (and standard deviation) for predictive functions learnt using all observations, extremes (10\%) and angles of the extreme observations with output variables AGRIC, FOOD and SODA over 10 random splits of each dataset.

| Methods/Models | Train on $X$ | TRain ON $X \mid\\|X\\|$ LARGe | TRAIN ON $\Theta \mid\\|X\\|$ LARGE |
| :---: | :---: | :---: | :---: |
| AGRIC: OLS | $3.30 \pm 0.47$ | $3.26 \pm 0.47$ | $\mathbf{3 . 2 5} \pm \mathbf{0 . 4 4}$ |
| SVR | $4.76 \pm 0.56$ | $3.98 \pm 0.51$ | $\mathbf{3 . 7 4} \pm \mathbf{0 . 5 0}$ |
| RF | $3.47 \pm 0.47$ | $3.48 \pm 0.47$ | $\mathbf{3 . 2 8} \pm \mathbf{0 . 5 2}$ |
| FOOD: OLS | $0.69 \pm 0.087$ | $\mathbf{0 . 6 7 8} \pm \mathbf{0 . 0 8 2}$ | $0.680 \pm 0.085$ |
| SVR | $1.8 \pm 0.4$ | $1.3 \pm 0.4$ | $\mathbf{0 . 8 7} \pm \mathbf{0 . 0 8}$ |
| RF | $0.70 \pm 0.13$ | $0.72 \pm 0.12$ | $\mathbf{0 . 6 3} \pm \mathbf{0 . 0 8}$ |
| SODA: OLS | $\mathbf{2 . 3 5} \pm \mathbf{0 . 2 1}$ | $2.37 \pm 0.21$ | $2.42 \pm 0.21$ |
| SVR | $4.0 \pm 0.5$ | $3.1 \pm 0.5$ | $\mathbf{2 . 8} \pm \mathbf{0 . 2}$ |
| RF | $2.46 \pm 0.28$ | $2.46 \pm 0.25$ | $\mathbf{2 . 3 4} \pm \mathbf{0 . 1 8}$ |

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-16.jpg?height=380&width=827&top_left_y=1260&top_left_x=172)

AGRIC

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-16.jpg?height=366&width=827&top_left_y=1275&top_left_x=1061)

FOOD

![](https://cdn.mathpix.com/cropped/2024_04_26_164b0b5dc42571e34fe0g-16.jpg?height=372&width=810&top_left_y=1752&top_left_x=625)

SODA

Figure 3: Average permutation and Gini importance measures of the radial variable for predicting AGRIC (top left), FOOD (top right) and SODA (bottom) variables using the RF over 10 randomly shuffled datasets. At each measurement, 1357 extreme observations are selected from a dataset whose total size increases from 1357 to 13570 with increments of 1357. Solid black line: average Gini importance. Solid grey line: average Permutation importance. Dashed lines: empirical 0.8-interquantile ranges.

## SUPPLEMENTARY MATERIAL

The Supplementary Material is structured as follows. In Section A, the Regular Variation with respect to the first component introduced in Assumption 2 is rephrased into equivalent conditions. Section B (resp. Section C) gathers the proofs of the results from Section 2 (resp. Section 3.2).

## A Multivariate Regular Variation w.r.t. the First Component

This section makes explicit the connection between Assumption 2 and the regular variation framework on a metric space developed in 38. We also provide alternative formulations of Assumption 2 Following whenever possible the notations of [38, let $\mathcal{Z}=\mathbb{R}^{d} \times I$ where we recall $I=[-M, M]$ (in [38 the ambient space $\mathcal{Z}$ is denoted by $\mathbb{S}$ which interferes with our notation for the unit sphere). The ambient space $\mathcal{Z}$ is endowed with the Euclidean product metric,

$$
d\left(\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right)\right)=\sqrt{\left\|x_{1}-x_{2}\right\|^{2}+\left(y_{1}-y_{2}\right)^{2}}
$$

so that $(\mathcal{Z}, d)$ is a complete separable metric space. Define a scalar 'multiplication' on $\mathcal{Z}$ as $\lambda .(x, y)=(\lambda x, y)$, $\lambda>0$, which is continuous and satisfies the associativity property $\lambda_{1} \cdot\left(\lambda_{2} . z\right)=\left(\lambda_{1} \lambda_{2}\right) . z$, and $1 . z=z$. This scalar multiplication induces a scaling operation on sets, $\lambda A=\{\lambda . z, z \in A\}$ for $A \subset \mathcal{Z}$. Consider the set $\mathbb{C}=\left\{0_{\mathbb{R}^{d}}\right\} \times I \subset \mathcal{Z}$. Then $\mathbb{C}$ is a closed set which is preserved by the above scaling operation, i.e. it is a closed cone. For $z=(x, y)$ we have $d(z, \mathbb{C})=\|x\|$, whence $d(x, \mathbb{C})<d(\lambda x, \mathbb{C})$ for $\lambda>1$. Thus Assumptions A1, A2, A3 in [38, Section 3, are satisfied. Let $\mathbb{O}=\mathcal{Z} \backslash \mathbb{C}$ and introduce $\mathbb{C}^{r}=\{z \in \mathbb{O}: d(z, \mathbb{C})>r\}, r \geq 0$. In [38, the class of Borel measures on $\mathbb{O}$ whose restriction to $\mathcal{Z} \backslash \mathbb{C}^{r}$ is finite for any $r>0$ is denoted by $\mathbb{M}_{0}$. Then convergence of a sequence of measures $\mu_{n} \in \mathbb{M}_{0}$ towards $\mu \in \mathbb{M}_{0}$ is defined as convergence of functional evaluations $\mu_{n}(f) \rightarrow \mu(f)$ for $f \in \mathcal{C}_{0}$, the class of continuous functions on $\mathcal{Z}$ which vanish on a neighborhood of $\mathbb{C}$, i.e. whose support is a subset of $\mathbb{C}^{r}$ for some $r>0$. A measure $\nu \in \mathbb{M}_{\mathbb{O}}$ is called regularly varying with limit measure $\mu \in \mathbb{M}_{0}$ and scaling sequence $b_{n} \in \mathbb{R}$, if $b_{n}$ is increasing, regularly varying in $\mathbb{R}$ and if the sequence of measures $b_{n} \nu(n \cdot)$ converges in $\mathbb{M}_{0}$ towards $\mu$ (see Definitions 3.1, 3.2 in [38]). From the Portmanteau Theorem 2.1 in [38] and the series of equivalences in Theorem 3.1 of the same reference, our Assumption 2 is equivalent to assuming that the distribution $P$ of the random pair $(X, Y)$ is regularly varying in $\mathbb{M}_{0}$ with scaling sequence $b_{n}$ and limit measure $\mu$, with the notations of Section 2.3

Theorem A. 1 Let $\mathbb{O}, \mathbb{C}$ be defined as above the statement, let $\mu \in \mathbb{M}_{\mathbb{O}}$ be a nonnull measure and let $b(t)$ be a regularly varying function on $\mathbb{R}^{+}$with index $\alpha>0$. Let $(X, Y) \sim P$ be a random pair valued in $\mathbb{R}^{d} \times I$. The following assertions are equivalent.

(i) The random pair $(X, Y)$ satisfies Assumption 2 from the main paper with limit measure $\mu$ and normalizing function $b$.

(ii) For any bounded and continuous function $h: \mathbb{O} \rightarrow \mathbb{R}$ that vanishes in a neighborhood of $\mathbb{C}$, i.e. whose support is included in $\mathbb{C}^{r}$ for some $r>0$,

$$
\lim _{t \rightarrow+\infty} b(t) \mathbb{E}\left[h\left(t^{-1} X, Y\right)\right]=\int_{\mathbb{O}} h \mathrm{~d} \mu
$$

(iii) There exists a finite measure $\Phi$ on $\mathbb{S} \times I$ such that

$$
\frac{\mathbb{P}\{\theta(X) \in B, Y \in A,\|X\| \geq t r\}}{\mathbb{P}\{\|X\| \geq t\}} \underset{t \rightarrow+\infty}{\longrightarrow} c r^{-\alpha} \Phi(B \times A)
$$

for all $r>0$ and $A \in \mathcal{B}(I), B \in \mathcal{B}(\mathbb{S})$ such that $\Phi(\partial(B \times A))=0$, with $c=\Phi(\mathbb{S} \times I)^{-1}$.

Proof. $(i)]($ ii $)$, Condition $\left[\right.$ (ii) in the statement is precisely Definition 3.2 of regular variation in $\mathbb{M}_{\mathbb{O}}$ of [38, regarding the measure $P$ restricted to $\mathbb{O}$. The equivalence with our Assumption 2 is a direct application of the Portmanteau theorem 2.1 in [38.

$($ iii) $\Leftrightarrow(i i)$. We generalize the argument of 38, Example 3.4 and we verify that we fit into the context of Example 3.5 of the same reference. The argument in Example 3.5 (see also Example 3.4) in 38] relies on a continuous mapping argument (Theorem 2.3 in the same reference). Introduce the 'polar coordinate transform' $T(x, y)=(\|x\|, \theta(x), y)$, for $(x, y) \in \mathbb{O}$, where we recall $\theta(x)=x /\|x\|$. Then $T$ is a homeomorphism from $\mathbb{O}$ onto $\mathbb{O}^{\prime}=\left(\mathbb{R}_{+} \backslash\{0\}\right) \times \mathbb{S} \times I=\mathcal{Z}^{\prime} \backslash \mathbb{C}^{\prime}$ with $\mathcal{Z}^{\prime}=\mathbb{R}_{+} \times \mathbb{S} \times I, \mathbb{C}^{\prime}=\{0\} \times \mathbb{S} \times I$. The space $\mathcal{Z}^{\prime}$ is endowed with a continuous
scalar multiplication $\lambda .(r, \omega, y)=(\lambda r, \omega, y)$ for $\lambda \geq 0$, which is compatible with the mapping $T$ in the sense that $\lambda . T(z)=T(\lambda . z)$. The scalar multiplication on $\mathcal{Z}^{\prime}$ satisfies the same associativity and monotonicity properties as the one on $\mathcal{Z}$. The mapping $T$ has the property that if $A^{\prime} \subset \mathbb{O}^{\prime}$ is bounded away from $\mathbb{C}^{\prime}$ then also $T^{-1}\left(A^{\prime}\right) \subset \mathbb{O}$ is bounded away from $\mathbb{C}$. The conditions of Example 3.5 in [38] are thus satisfied, so that regular variation of the joint distribution $P$ (restricted to $\mathbb{O}$ ) in $\mathbb{M}_{\circ}$ is equivalent to regular variation of the image measure $T_{\star} P$ (restricted to $\mathbb{O}^{\prime}$ ), with limit measure $\mu^{\prime}=T_{\star} \mu$, and with the same scaling function $b(t)$. In other words Condition (ii) is equivalent to the fact that for any measurable sets $B \subset \mathbb{S}, C \in I$ such that $\mu\left(\partial\left(\mathcal{C}_{B} \times C\right)\right)=0$, where $\mathcal{C}_{B}=\{t \omega, t \geq 1, \omega \in B\}$, we have

$$
\begin{aligned}
b(t) \mathbb{P}\{\|X\|>t r, \theta(X) \in B, Y \in C\} \underset{t \rightarrow+\infty}{\longrightarrow} & \mu\{(x, y):\|x\| \geq r, \theta(x) \in B, y \in C\} \\
& =\mu(r \cdot\{(x, y):\|x\| \geq 1, \theta(x) \in B, y \in C\}) \\
& =r^{-\alpha} \mu\{(x, y):\|x\| \geq 1, \theta(x) \in B, y \in C\}
\end{aligned}
$$

where the last identity follows from the homogeneity of $\mu$ (Theorem 3.1 in 38]). Define the angular measure $\Phi$ on $\mathbb{S} \times I$ as in (7) from the main paper, $\Phi(B \times C)=\mu\{(x, y) \in \mathbb{O}:\|x\| \geq 1, \theta(x) \in B, y \in C\}$. Then $\Phi$ is a finite measure and the latter display writes equivalently

$$
b(t) \mathbb{P}\{\|X\|>\operatorname{tr}, \theta(X) \in B, Y \in C\} \underset{t \rightarrow+\infty}{\longrightarrow} r^{-\alpha} \Phi(B \times C)
$$

for all measurable sets $B \subset \mathbb{S}, C \in I$ such that $\Phi(\partial(B \times C))=0$. If (21) holds then also, taking $B=\mathbb{S}, C=I, r=1$ we have

$$
b(t) \mathbb{P}\{\|X\|>t\} \underset{t \rightarrow+\infty}{\longrightarrow} \Phi(\mathbb{S} \times I)
$$

and taking the ratio of (21) with the latter displays yields Condition (iii) of the statement. Conversely if (iii) holds, then letting $b(t)=\Phi(\mathbb{S} \times I) / \mathbb{P}\{\|X\|>t\}$, we obtain (21), which is equivalent to Condition (ii),

## B Proofs for Section 2

This section gathers the proofs of Proposition 1 and of the claims in Examples 11 and 2, as well as the proof of Theorem 1 .

## B. 1 Proof of Proposition 1

We show that if Assumptions 1 and 2 both hold true, then each condition (i), (ii), or (iii) of the statement imply Assumption 3 In fact we show that $($ iii $) \Rightarrow($ ii $) \Rightarrow$ (i) $\Rightarrow$ Assumption 3

Condition (i) $\Rightarrow$ Assumption 3. The continuity of $f_{P_{\infty}}^{*}$ follows from the continuity of $f^{*}$ and the uniform convergence (10). Also, the convergence in Assumption 3 is a direct consequence of convergence (10).

Condition (ii) $\Rightarrow$ Condition (i). For $x \in \mathbb{R}^{d}$ such that $\|x\| \geq t \geq 1$, we have

$$
\begin{aligned}
\left|f^{*}(x)-f_{P_{\infty}}^{*}(x)\right| & =\left|\int_{y \in I} y p_{Y \mid x}(y) d y-\int_{y \in I} y p_{Y \mid x}^{\infty}(y) d y\right| \\
& \leq M^{2} \sup _{\|x\| \geq t, y \in I}\left|p_{Y \mid x}(y)-p_{Y \mid x}^{\infty}(y)\right|
\end{aligned}
$$

Thus, uniform convergence in (10) follows from (11). The continuity of $f^{*}$ is ensured by an application of the dominated convergence theorem to the parametric integral $f^{*}(x)=\int_{I} y p_{Y \mid x}(y) \mathrm{d} y$, using the fact that for all $y \in I$, $x \mapsto p_{Y \mid x}(y)$ is continuous and that $\sup _{\|x\| \geq 1, y \in I} p_{Y \mid x}(y)<+\infty$.

Condition (iii) $\Rightarrow$ Condition (ii). We first show that uniform convergence (11) holds true. Notice first that the density $q$ of $\mu$ is necessarily homogeneous in its first component, $q(t x, y)=t^{-\alpha-d} q(x, y)$ for $x \neq 0$ (This follows from the homogeneity of $\mu$ and a change of variable in the first component when integrating over a region $t A \times B$ where $A \subset \mathbb{R}^{d} \backslash\{0\}$ and $B \subset I$ ). Thus for $x \in \mathbb{R}^{d}$ with $\|x\| \geq 1$ and $y \in I$, we have

$$
p_{Y \mid x}(y)=\frac{p(x, y)}{p_{X}(x)} \quad \text { and } \quad p_{Y \mid x}^{\infty}(y)=\frac{q(x, y)}{q_{X}(x)}=\frac{q(x /\|x\|, y)}{q_{X}(x /\|x\|)}
$$

where we denote by $p_{X}$ (resp. $q_{X}$ ) the marginal density of $X$ (resp. $X_{\infty}$ ) given by $p_{X}(x)=\int_{I} p(x, y) d y$ (resp. $\left.q_{X}(x)=\int_{I} q(x, y) d y\right)$. Then, for $x \in \mathbb{R}^{d} \backslash\{0\}, y \in I$, introducing the function $h(t)=t^{d} b(t)$, the left-hand side in Equation (11) writes as

$$
\begin{aligned}
& \left|\frac{p(x, y)}{p_{X}(x)}-\frac{q(x /\|x\|, y)}{q_{X}(x /\|x\|)}\right|=\left|\frac{h(\|x\|) p(x, y)}{h(\|x\|) p_{X}(x)}-\frac{q(x /\|x\|, y)}{q_{X}(x /\|x\|)}\right| \\
& \leq \underbrace{h(\|x\|) p(x, y)\left|\frac{1}{h(\|x\|) p_{X}(x)}-\frac{1}{q_{X}(x /\|x\|)}\right|}_{A(x, y)}+\ldots \\
& \underbrace{\frac{|h(\|x\|) p(x, y)-q(x /\|x\|, y)|}{q_{X}(x /\|x\|)}}_{B(x, y)} .
\end{aligned}
$$

Regarding the numerator of the term $B(x, y)$ above, notice that for $\|x\| \geq t$,

$$
\begin{aligned}
|h(\|x\|) p(x, y)-q(x /\|x\|, y)| & =|h(t(\|x\| / t)) p(t(\|x\| / t)(x /\|x\|), y)-q(x /\|x\|, y)| \\
& \leq \sup _{s \geq t,(\omega, y) \in \mathbb{S} \times I}|h(s) p(s \omega, y)-q(\omega, y)| \rightarrow 0
\end{aligned}
$$

as $t$ tends to infinity, by uniform convergence (12). This, together with the lower bound (13) on $q$, implies that as $t \rightarrow \infty$

$$
\sup _{\|x\|>t, y \in I} B(x, y) \rightarrow 0
$$

Turning to the term $A(x, y)$ in 22 , observe first that

$$
A(x, y)=h(\|x\|) p(x, y)\left|\frac{h(\|x\|) p_{X}(x)-q_{X}(x /\|x\|)}{h(\|x\|) p_{X}(x) q_{X}(x /\|x\|)}\right|
$$

Notice that for $\|x\|>t$,

$$
\begin{aligned}
\left|h(\|x\|) p_{X}(x)-q_{X}(x /\|x\|)\right| & =\left|\int_{I}(h(\|x\|) p(x, y)-q(x /\|x\|, y)) d y\right| \\
& \leq 2 M \sup _{s \geq t,(\omega, y) \in \mathbb{S} \times I}|h(s) p(s \omega, y)-q(\omega, y)|:=U(t)
\end{aligned}
$$

where the upper bound $U(t)$ vanishes as $t \rightarrow \infty$ because of (12). Now, for $\|x\|>t$ and $y \in I$,

$$
A(x, y) \leq \frac{\sup _{\|x\| \geq t, y \in I} h(\|x\|) p(x, y)}{\inf _{\|x\|>t} h(\|x\|) p_{X}(x) \inf _{\omega \in \mathbb{S}} q_{X}(\omega)} U(t)
$$

Regarding the numerator of the above display, recall that the density function $q$ is continuous on the compact set $\mathbb{S}$, whence it is upper bounded. Because of uniform convergence (12), it is also true that $\sup _{\|x\| \geq t, y \in I} h(\|x\|) p(x, y)$ is upper bounded by a finite constant for $t$ large enough. In addition, our lower bound assumption (13) on $q$ together with uniform convergence (23) show that the denominator is ultimately (as $t \rightarrow \infty$ ) lower bounded by a positive constant. Summarizing, we have shown that $\sup _{\|x\|>t, y \in \mathbb{S}} A(x, y) \rightarrow 0$ as $t \rightarrow \infty$, finishing the proof of (11).

It remains to prove that for all $y \in I, x \mapsto p(x, y) / p_{X}(x)$ is continuous and that $p(x, y) / p_{X}(x)$ is uniformly bounded. For all $y \in I$, the continuity of $x \mapsto p(x, y) / p_{X}(x)$ follows from the continuity of $p$. Notice again that for $x \in \mathbb{R}^{d}$ and $y \in I$

$$
\frac{p(x, y)}{p_{X}(x)}=\frac{h(\|x\|) p(x, y)}{h(\|x\|) p_{X}(x)}
$$

The numerator uniformly converges to $q$, which is uniformly bounded. The denominator uniformly converges to $q_{X}$, which is uniformly lower bounded by Equation (13). Then $\sup _{\|x\| \geq 1, y \in I}\left(p(x, y) / p_{X}(x)\right)$ is finite, which concludes the proof.

## B. 2 Proofs and Additional Results regarding Example 1

In this section, we show that a generic heavy-tailed regression model (Example 11) satisfies the requirements of our assumptions. Subsequently, we establish that two widely used models, the additive and multiplicative noise models, constitute particular instances of that generic model.

Proposition B. 1 In the setting of Example 1, the random pair (X,Y) satisfies Assumption 1, 2 and 3. In particular, the limit distribution $P_{\infty}$ in Equation (9) is given by

$$
P_{\infty}=\mathcal{L}\left(X_{\infty}, g_{\theta}\left(X_{\infty} /\left\|X_{\infty}\right\|, \varepsilon\right)\right)
$$

where $X_{\infty}$ follows the limit distribution

$$
Q_{\infty}=\lim _{t \rightarrow \infty} \mathcal{L}\left(t^{-1} X \mid\|X\| \geq t\right)
$$

PROOF. Assumption 1 is obviously fulfilled with $M=\sup _{x, z \in \mathbb{R}^{d} \times \mathbb{R}}|g(x, z)|$. Regarding Assumption 2 and the limit distribution, we consider a bounded and Lipschitz function $l: \mathbb{R}^{d} \times \mathbb{R} \rightarrow \mathbb{R}$. For all $t>0$, writing $\Theta=\|X\|^{-1} X$, we have

$$
\begin{aligned}
\mathbb{E}\left[l\left(t^{-1} X, Y\right) \mid\|X\| \geq t\right]= & \mathbb{E}\left[l\left(t^{-1} X, g(X, \varepsilon)\right) \mid\|X\| \geq t\right] \\
& =\mathbb{E}\left[l\left(t^{-1} X, g_{\theta}(\Theta, \varepsilon)\right) \mid\|X\| \geq t\right]+\ldots \\
& \mathbb{E}\left[l\left(t^{-1} X, g(X, \varepsilon)\right)-l\left(t^{-1} X, g_{\theta}(\Theta, \varepsilon)\right) \mid\|X\| \geq t\right]
\end{aligned}
$$

Since $\varepsilon$ is independent from $X$, writing $\Theta_{\infty}=\left\|X_{\infty}\right\|^{-1} \Theta_{\infty}$, the regular variation of $X$ and continuity of $l$ and $g_{\theta}$ imply that

$$
\mathbb{E}\left[l\left(t^{-1} X, g_{\theta}(\Theta, \varepsilon)\right) \mid\|X\| \geq t\right] \rightarrow \mathbb{E}\left[l\left(X_{\infty}, g_{\theta}\left(\Theta_{\infty}, \varepsilon\right)\right)\right]
$$

Because $l$ is Lipschitz continuous (for some Lipschitz constant $C$ ) and $X$ and $\varepsilon$ are independent, we have

$$
\begin{aligned}
& \left|\mathbb{E}\left[l\left(t^{-1} X, g(X, \varepsilon)\right)-l\left(t^{-1} X, g_{\theta}(\Theta, \varepsilon)\right) \mid\|X\| \geq t\right]\right| \\
& \leq C \mathbb{E}\left[\left|g(X, \varepsilon)-g_{\theta}(\Theta, \varepsilon)\right| \mid\|X\| \geq t\right] \\
& \leq C \mathbb{E}\left[\sup _{\|x\| \geq t}\left|g(x, \varepsilon)-g_{\theta}(\theta(x), \varepsilon)\right|\right]
\end{aligned}
$$

The right-hand side tends to zero as $t \rightarrow+\infty$, from the dominated convergence theorem which applies because $\sup _{\|x\| \geq t}\left|g(x, \varepsilon)-g_{\theta}(x /\|x\|, \varepsilon)\right| \leq M$ and because of our model assumption (14). Thus Assumption 2 is satisfied and $P_{\infty}=\mathcal{L}\left(X_{\infty}, g_{\theta}\left(\Theta_{\infty}, \varepsilon\right)\right)$.

We now show that Assumption 3 also holds true by proving the stronger condition (i) from Proposition 1 For $x \in \mathbb{R}^{d}$ with $\|x\| \geq t$, we have by independence of $X$ and $\varepsilon$,

$$
\begin{aligned}
\left|f^{*}(x)-f_{P_{\infty}}^{*}(\theta(x))\right| & =\left|\mathbb{E}[g(x, \varepsilon)]-\mathbb{E}\left[g_{\theta}(\theta(x), \varepsilon)\right]\right| \\
& \leq \mathbb{E}\left[\sup _{\|x\| \geq t}\left|g(x, \varepsilon)-g_{\theta}(\theta(x), \varepsilon)\right|\right]
\end{aligned}
$$

which entails as in (24) that $\sup _{\|x\| \geq t}\left|f^{*}(x)-f_{P_{\infty}}^{*}(x /\|x\|)\right| \rightarrow 0$, as $t \rightarrow+\infty$. Since $g$ is assumed continuous and bounded, $f^{*}$ is continuous. Thus, the sufficient condition (i) from Proposition 1 is satisfied, which shows that Assumption 3 holds true.

We now turn to the two sub-examples given by the additive and multiplicative noise models mentioned after Example 1 from the main paper. We show that under mild assumptions, both sub-examples indeed satisfy the conditions specified in Proposition B. 1

Proposition B. 2 Consider the additive noise model

$$
Y=\tilde{g}(X)+\varepsilon
$$

where $X$ is a regularly varying random vector in $\mathbb{R}^{d}$ such that

$$
\mathcal{L}\left(t^{-1} X \mid\|X\| \geq t\right) \rightarrow \mathcal{L}\left(X_{\infty}\right)
$$

as $t \rightarrow+\infty, \varepsilon$ is a bounded real-valued random variable defined on the same probability space independent from $X$ and $\tilde{g}_{\theta}$ is a bounded, continuous function on $\mathbb{R}^{d}$ which converges uniformly to some angular mapping $\tilde{g}_{\theta}: \mathbb{S} \rightarrow \mathbb{R}$, in the sense that

$$
\sup _{\|x\| \geq t}\left|\tilde{g}(x)-\tilde{g}_{\theta}(\theta(x))\right| \rightarrow 0 \text { as } t \rightarrow+\infty
$$

Then, the random pair $(X, Y)$ satisfies the requirements of Proposition B. 1 with $M=\sup _{x \in \mathbb{R}^{d}}|\tilde{g}(x)|+\| \varepsilon||_{\infty}$. The limit distribution $P_{\infty}$ in Equation (9) is

$$
P_{\infty}=\mathcal{L}\left(X_{\infty}, \tilde{g}_{\theta}\left(\theta\left(X_{\infty}\right)\right)+\varepsilon\right)
$$

PROOF. Because $\varepsilon$ is almost surely bounded, there exists $m_{\varepsilon} \in \mathbb{R}_{+}$a nonnegative real-number such that $\varepsilon \stackrel{\text { a.s. }}{\in}$ $\left[-m_{\varepsilon},+m_{\varepsilon}\right]$. Consider the mapping $g:(x, z) \in \mathbb{R}^{d} \times\left[-m_{\varepsilon},+m_{\varepsilon}\right] \mapsto g(x)+z$ and $g_{\theta}:(\omega, z) \in \mathbb{S} \times\left[-m_{\varepsilon},+m_{\varepsilon}\right] \mapsto$ $\tilde{g}_{\theta}(\omega)+z$. The function $g$ is continuous and bounded by $M=\sup _{x \in \mathbb{R}^{d}}|\tilde{g}(x)|+m_{\varepsilon}$ and the pair $\left(g, g_{\theta}\right)$ satisfies Equation (14). Indeed for all $z \in\left[-m_{\varepsilon},+m_{\varepsilon}\right]$,

$$
\sup _{\|x\| \geq t}\left|g(x, z)-g_{\theta}(\theta(x), z)\right|=\sup _{\|x\| \geq t}\left|\tilde{g}(x)-\tilde{g}_{\theta}(\theta(x))\right| \rightarrow 0
$$

as $t \rightarrow+\infty$, which concludes the proof.

Proposition B. 3 Consider the multiplicative noise model

$$
Y=\varepsilon \tilde{g}(X)
$$

where $(X, \varepsilon)$ and $\tilde{g}$ are as in Proposition B.2. Then, the random pair $(X, Y)$ satisfies the requirements of Proposition B.1 with $M=\sup _{x \in \mathbb{R}^{d}}|\tilde{g}(x)| \times\|\varepsilon\|_{\infty}$ and the limit distribution $P_{\infty}$ in (9) is given by $P_{\infty}=\mathcal{L}\left(X_{\infty}, \varepsilon \tilde{g}_{\theta}\left(\theta\left(X_{\infty}\right)\right)\right.$, where $\tilde{g}_{\theta}$ and $X_{\infty}$ are as in Proposition B.2.

PROOF.

Consider the mapping $g(x, z)=z \tilde{g}(x)$ and $g_{\theta}(\omega, z)=z \tilde{g}_{\theta}(\omega)$. Let $m_{\varepsilon}$ be as in the proof of Proposition B.2. On the domain $\mathbb{R}^{d} \times\left[-m_{\varepsilon}, m_{\varepsilon}\right]$, the function $g$ is continuous and bounded by $M=m_{\varepsilon} \sup _{x \in \mathbb{R}^{d}}|\tilde{g}(x)|$. The pair $\left(g, g_{\theta}\right)$ satisfies (14) since for all $z \in\left[-m_{\varepsilon},+m_{\varepsilon}\right]$

$$
\sup _{\|x\| \geq t}\left|g(x, z)-g_{\theta}(x /\|x\|, z)\right| \leq m_{\varepsilon} \sup _{\|x\| \geq t}\left|\tilde{g}(x)-\tilde{g}_{\theta}(\theta(x))\right| \underset{t \rightarrow \infty}{\longrightarrow} 0
$$

which concludes the proof.

## B. 3 Proofs regarding Example 2

Let $\tilde{E}=\mathbb{R}^{d+1} \backslash\left\{0_{\mathbb{R}^{d+1}}\right\}, E=\mathbb{R}^{d} \backslash\left\{0_{\mathbb{R}^{d}}\right\}$. and for simplicity denote both by $\mathbb{B}_{d}$ the $d$-dimensional unit ball and its image by the canonical embedding $\mathbb{R}^{d} \rightarrow \mathbb{R}^{d+1}$, i.e. $\mathbb{B}_{d}=\left\{\tilde{x} \in \mathbb{R}^{d+1}:\left\|\left(\tilde{x}_{1}, \ldots, \tilde{x}_{d}\right)\right\| \leq 1, \tilde{x}_{d+1} \in \mathbb{R}\right\}$. For $\tilde{x} \in \mathbb{R}^{d+1}$ we denote by $x$ the first $d$ coordinates of $\tilde{x}, x=\left(\tilde{x}_{1}, \ldots, \tilde{x}_{d}\right)$. Denote by $\varphi$ the continuous mapping sending $\tilde{X}$ to $(X, Y)$, i.e.

$$
\begin{aligned}
\varphi: \quad E \times \mathbb{R} & \rightarrow E \times(-1,1) \\
\tilde{x}=(x, z) & \mapsto(x, y)=(x, z /\|(x, z)\|)
\end{aligned}
$$

Equipped with these notations, we may proceed with the proof.

(a) Assumption 1 is trivially satisfied because $|Y| \leq 1$.

(b) We now show that Assumption 2 holds with limit pair $\left(X_{\infty}, Y_{\infty}\right)$ as in the second part of the statement. Equipped with the notations introduced above, the pair defined in the statement may be written as $\left(X_{\infty}, Y_{\infty}\right)=$ $\varphi\left(\tilde{X}_{\infty}\right)$, where $\tilde{X}_{\infty}$ is well defined by regular variation of the full vector $\tilde{X}$. We need to show that for any bounded, continuous function $g$,

$$
\mathbb{E}[g(X / t, Y) \mid\|\tilde{X}\| \geq t] \rightarrow \mathbb{E}\left[g \circ \varphi\left(\tilde{X}_{\infty}\right) \mid\left\|\tilde{X}_{\infty, 1: d}\right\| \geq 1\right]
$$

However $(X / t, Y)=\varphi(\tilde{X} / t)$ and $\|X\| \geq t \Rightarrow\|\tilde{X}\| \geq t$. Thus

$$
\begin{aligned}
\mathbb{E}[g(X / t, Y) \mid\|X\| \geq t] & =\frac{\mathbb{E}[g \circ \varphi(\tilde{X} / t) \mathbb{1}\{\|X / t\| \geq 1\} \mathbb{1}\{\|\tilde{X} / t\| \geq 1\}]}{\mathbb{P}\{\|\tilde{X} / t\| \geq 1\}} \frac{\mathbb{P}\{\|\tilde{X} / t\| \geq 1\}}{\mathbb{P}\{\|X / t\| \geq 1\}} \\
& =\mathbb{E}[g \circ \varphi(\tilde{X} / t) \mathbb{1}\{\|X / t\| \geq 1\} \mid\|\tilde{X}\| \geq t] \frac{\mathbb{P}\{\|\tilde{X} / t\| \geq 1\}}{\mathbb{P}\{\|X / t\| \geq 1\}} \\
& \rightarrow \mathbb{E}\left[g \circ \varphi\left(\tilde{X}_{\infty}\right) \mathbb{1}\left\{\left\|\tilde{X}_{\infty, 1: d}\right\| \geq 1\right\}\right] \frac{1}{\mathbb{P}\left\{\left\|\tilde{X}_{\infty, 1: d}\right\| \geq 1\right\}}
\end{aligned}
$$

where the convergence of the first term in the latter expression is obtained by approaching the (discontinuous) function $\mathbb{1}\{\|z\| \geq 1\}$ by continuous ones and using the fact that the boundary of $\mathbb{B}_{d}$ in $\mathbb{R}^{d+1}$ is not a cone, whence it cannot carry any positive $\mu$-mass (a standard feature of radially homogeneous measures).

(c) We now prove that Assumption 3 holds true by proving the stronger condition 10 which rephrase in our setting as

$$
\sup _{\|x\|=1}\left|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

Indeed if 25 holds, then $\sup _{s \geq t} \sup _{\|x\|=1}\left|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0$, so that

$$
\sup _{\|x\| \geq t}\left|f^{*}(x)-f_{P_{\infty}}^{*}(x)\right|=\sup _{\|x\| \geq 1}\left|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)\right|=\sup _{s \geq t} \sup _{\|x\|=1}\left|f^{*}(s x)-f_{P_{\infty}}^{*}(s x)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

Notice first that for $x \in \mathbb{R}^{d}$ such that $\|x\| \geq 1, f^{*}(x)$ and $f_{P_{\infty}}^{*}(x)$ may be written in terms of integrals

$$
f^{*}(x)=\int_{z \in \mathbb{R}} \frac{z}{\|(x, z)\|} \frac{p(x, z)}{p(x)} \mathrm{d} z
$$

where for simplicity we denote by $p(x)$ the marginal density of the first $d$ components of $\tilde{X}$ at $x$, and also $p(x, z)$ the joint density at $\tilde{x}=(x, z)$.

In the present setting, $f_{P_{\infty}}^{*}$ is defined as $f_{P_{\infty}}^{*}\left(X_{\infty}\right)=\mathbb{E}\left[Y_{\infty} \mid X_{\infty}\right]$. Introduce $\tilde{Z}=\left(\tilde{Z}_{1}, \ldots, \tilde{Z}_{d+1}\right)$ distributed as $\mathcal{L}\left(\tilde{X}_{\infty} \mid\left\|\tilde{X}_{\infty, 1: d}\right\| \geq 1\right)$. Then $\tilde{Z}$ has density $C q(x, z)$ on $\mathbb{B}_{d}^{c} \times \mathbb{R}$, and marginal density for its first $d$ components, $C q(x):=\int_{\mathbb{R}} C q(x, z) \mathrm{d} z$. With these notations we have $\left(X_{\infty}, Y_{\infty}\right) \stackrel{d}{=}\left(\tilde{Z}_{1: d}, \tilde{Z}_{d+1} / \| \tilde{Z}_{1: d}\right)$, whence $f_{P_{\infty}}^{*}\left(\tilde{Z}_{1: d}\right)=$ $\mathbb{E}\left[\tilde{Z}_{d+1} /\|\tilde{Z}\| \mid \tilde{Z}_{1: d}\right]$ almost surely. We obtain, for $\|x\| \geq 1$,

$$
f_{P_{\infty}}^{*}(x)=\int_{\mathbb{R}} \frac{z}{\|(x, z)\|} \frac{C q(x, z)}{C q(x)} \mathrm{d} z=\int_{\mathbb{R}} \frac{z}{\|(x, z)\|} \frac{q(x, z)}{q(x)} \mathrm{d} z
$$

Combining the latter two displays we obtain

$$
\left|f^{*}(x)-f_{P_{\infty}}^{*}(x)\right| \leq \int_{z \in \mathbb{R}}\left|\frac{p(x, z)}{p(x)}-\frac{q(x, z)}{q(x)}\right| \mathrm{d} z
$$

Introduce as in Lemma 2 the function $h(t)=t^{d+1} / \mathbb{P}\{\|X\| \geq t\}$. For $\|x\|=1$, by a change of variable $r=z / t$ in 26 , we obtain

$$
\begin{aligned}
\left|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)\right| & \leq \int_{r \in \mathbb{R}}\left|\frac{p(t x, t r)}{p(t x)}-\frac{q(t x, t r)}{q(t)}\right| t \mathrm{~d} r \\
& =\int_{r \in \mathbb{R}}\left|\frac{h(t) p(t x, t r)}{t^{-1} h(t) p(t x)}-\frac{q(x, r)}{q(x)}\right| \mathrm{d} r
\end{aligned}
$$

since by homogeneity of $q$, it holds that $q(t x, t r)=t^{-d-1-\alpha} q(x, r)$ while $q(t x)=t^{-d-\alpha} q(x)$. Thus

$$
\sup _{\|x\|=1}\left|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)\right| \leq \int_{r \in \mathbb{R}} \underbrace{\sup _{\|x\|=1}\left|\frac{h(t) p(t x, t r)}{t^{-1} h(t) p(t x)}-\frac{q(x, r)}{q(x)}\right|}_{J(t, r)} \mathrm{d} r
$$

We have the following controls over the quantities in the latter integrand:

1. $q(x)$ is lower bounded by a positive constant (Lemma 3)
2. $\sup _{\|x\|=1}\left|h(t) t^{-1} p(t x)-q(x)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0$ (Lemma 22,
3. For all fixed $r$, because of (17), and since $\|(x, r)\| \geq\|x\|$,

$$
\sup _{\|x\|=1}|h(t) p(t x, t r)-q(x, r)| \leq \sup _{\substack{\|\tilde{u}\| \geq 1 \\ t \rightarrow+\infty}}|h(t) p(t \tilde{u})-q(\tilde{u})|
$$

Thus, combining 1., 2., 3. above, for fixed $r$, the integrand $J(t, r)$ in (27) converges to 0 as $t \rightarrow+\infty$. In order to apply the dominated convergence theorem, we verify that $J(t, r)$ is upper bounded by an integrable function of $r$. The argument is somewhat similar to the one in the proof of Lemma 2 We decompose the integrand as

$$
\begin{aligned}
J(t, r) & \leq \underbrace{\sup _{\|x\|=1} \frac{h(t)}{h(t\|(x, r)\|)}}_{A(t, r)} \underbrace{\sup _{\|x\|=1} \frac{h(t\|(x, r)\|) p(t\|(x, r)\| \theta(x, r))}{t^{-1} h(t) p(t x)}}_{B(t, r)}+\ldots \\
& \cdots \underbrace{\sup _{\|x\|=1} \frac{q(x, r)}{q(x)}}_{C(t, r)} \\
& =A(t, r) B(t, r)+C(t, r) .
\end{aligned}
$$

From the proof of Lemma 2 (see Equation (28) we have that for $t \geq t_{0}$ large enough, and for all $r \in \mathbb{R}$,

$$
A(t, r) \leq 2\|(x, r)\|^{-d-\alpha / 2-1} \leq 2\left(1+r^{p}\right)^{\frac{-d-\alpha / 2-1}{p}}
$$

an integrable function of $r$.

The numerator and the denominator in the definition of $B(t, r)$ converge as $t \rightarrow+\infty$, uniformly over $\|x\| \geq 1$ and $r \in \mathbb{R}$, respectively to $q(x, r)$ and $q(x)$. The latter quantity is lower bounded (Lemma 3) and $q(x, r)$ is uniformly bounded for $\|x\|=1$ (by homogeneity). Thus, for some constant $C>0$, for all $t \geq t_{1}$ with some large enough $t_{1} \geq t_{0}$, we have

$$
B(t, r) \leq C
$$

By homogeneity of $q$ and Lemma 3 again, we have

$$
C(t, r) \leq \sup _{\|x\|=1}\|(x, r)\|^{-\alpha-d-1} \frac{\max _{\omega \in \mathbb{S}_{d+1}} q(\omega)}{c}=\left(1+r^{p}\right)^{\frac{-\alpha-d-1}{p}} \frac{\max _{\omega \in \mathbb{S}_{d+1}} q(\omega)}{c}
$$

which is an integrable function of $r$.

Combining the bounds regarding $A(t, r), B(t, r), C(t, r)$, we have shown that $A(t, r) B(t, r)+C(t, r)$ is upper bounded by an integrable function of $r$. The proof of the condition $\sqrt{10}$ is complete. It remains to show that $f_{P_{\infty}}^{*}$ is continuous on $\|x\| \geq 1$. Recall that for $x \in \mathbb{R}^{d} \backslash\left\{0_{\mathbb{R}^{d}}\right\}$,

$$
f_{P_{\infty}}^{*}(x)=\frac{1}{q(x)} \int_{\mathbb{R}} \frac{z}{\|(x, z)\|} q(x, z) d z
$$

The continuity of $p$ implies that of $q$ by Equation (16). By homogeneity of $q$, we have

$$
\frac{z}{\|(x, z)\|} q(x, z) \leq q(x, z)=\|(x, z)\|^{-d-\alpha-1} q(\theta(x, z)) \leq\left(1+z^{p}\right)^{\frac{-d-\alpha-1}{p}} \max _{\omega \in \mathbb{S}_{d+1}} q(\omega)
$$

Since $z \mapsto\left(1+z^{p}\right)^{\frac{-d-\alpha-1}{p}}$ is integrable over $\mathbb{R}$, the dominated convergence theorem for continuity applies twice and entails that $x \mapsto \int_{\mathbb{R}} \frac{z}{\|(x, z)\|} q(x, z) d z$ and $x \mapsto \frac{1}{q(x)}$ are continuous and then $f_{P_{\infty}}^{*}$ is continuous. The proof is complete.

Lemma 2 (Uniform Convergence of marginals of $p$. ) Under the assumptions of Example 2, we have

$$
\begin{aligned}
& \sup _{\|x\|=1}\left|\int_{\mathbb{R}} t^{-1} h(t) p(t x, z) \mathrm{d} z-q(x)\right| \underset{t \rightarrow+\infty}{\longrightarrow} 0, \quad \text { where } \\
& q(x)=\int_{z} q(x, z) \mathrm{d} z, \quad \text { and } h(t)=t^{d+1} / \mathbb{P}\{\|\tilde{X}\| \geq t\}
\end{aligned}
$$

PROOF. We adapt the arguments of the proof of Theorem 2.1 of [19 to our context. With the notation $h$ from our statement, our uniform convergence assumption (16) becomes

$$
\sup _{\omega \in \mathbb{S}_{d+1}}|h(t) p(t \omega)-q(\omega)| \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

Now

$$
\int_{\mathbb{R}} t^{-1} h(t) p(t x, z) \mathrm{d} z=\int_{\mathbb{R}} h(t) p(t x, t r) \mathrm{d} r
$$

so that

$$
\sup _{\|x\|=1}\left|\int_{\mathbb{R}} t^{-1} h(t) p(t x, z) \mathrm{d} z-q(x)\right| \leq \int_{\mathbb{R}} \sup _{\|x\|=1}|h(t) p(t x, t r)-q(x, r)| \mathrm{d} r
$$

For fixed $r \in \mathbb{R}$, because $\|(x, r)\| \geq\|x\| \geq 1$, the integrand in the right-hand side is less than

$$
\sup _{\|\tilde{u}\| \geq 1}|h(t) p(t \tilde{u})-q(\tilde{u})|
$$

The latter display tends to zero as $t \rightarrow+\infty$ because of (17). To conclude, we need to upper bound the integrand by an integrable function of $r$, in order to apply dominated convergence. We thus write

$$
\begin{aligned}
& \sup _{\|x\|=1}|h(t) p(t x, t r)-q(x, r)| \\
& \leq \sup _{\|x\|=1} h(t) p(t x, t r)+\sup _{\|x\|=1} q(x, r) \\
& =\underbrace{\sup _{\|x\|=1} \frac{h(t)}{h(t\|(x, r)\|)}}_{A(t, r)} \underbrace{\sup _{\|x\|=1} h(t\|(x, r)\|) p(t\|(x, r)\| \theta(x, r))}_{B(t, r)}+\underbrace{\sup _{\|x\|=1} q(x, r)}_{C(t, r)}
\end{aligned}
$$

where $\theta(x, r) \in \mathbb{S}_{d+1}$.

- The function $h$ is regularly varying with positive index $d+1+\alpha$. By Karamata representation (Proposition 0.5 of [49]), for $t$ large enough (say $t \geq t_{0}$ ), for any $s \geq 1$, we have

$$
\frac{h(t)}{h(t s)} \leq 2 s^{-d-\frac{\alpha}{2}+1}
$$

Thus for $t \geq t_{0}$, for all $r \in \mathbb{R}$,

$$
A(t, r) \leq 2\|(x, r)\|^{-d-\alpha / 2-1} \leq 2\left(1+r^{p}\right)^{\frac{-d-\alpha / 2-1}{p}}
$$

which is an integrable function of $r$ for any $d \geq 1, \alpha>0$.

- because $\|(x, r)\| \geq\|x\| \geq 1$ we have for all $t \geq t_{0}$ large enough, uniformly over $x$ such that $\|x\|=1$ and $r \in \mathbb{R}$,

$$
|h(t\|(x, r)\|) p(t\|(x, r)\| \theta(x, r))-q(\theta(x, r))| \leq 1
$$

thus for $t \geq t_{0}$, for all $r$,

$$
B(t, r) \leq \sup _{\omega \in \mathbb{S}_{d+1}} q(\omega)+1
$$

which is a finite constant.

- We may also upper bound $C(t, r)$ by an integrable function of $r$, since by homogeneity of $q$,

$$
\begin{aligned}
C(t, r) & =\sup _{\|x\|=1}\|(x, r)\|^{-d-\alpha-1} q(\theta(x, r)) \\
& \leq \max _{\omega \in \mathbb{S}_{d+1}}(q(\omega))\left(1+r^{p}\right)^{\frac{-d-\alpha-1}{p}}
\end{aligned}
$$

which is integrable for $d \geq 1$ and $\alpha>0$.

As a consequence of the above three points, the quantity $A(t, r) B(t, r)+C(t, r)$ is upper bounded by an integrable function of $r$. The result follows by dominated convergence.

Lemma 3 (Upper and lower bounds for the marginals of $q$ ) Under the conditions of Example 2, there exists positive constants $c, C>0$ such that for all $x \in \mathbb{R}^{d}$ such that $\|x\|=1$,

$$
c \leq \int q(x, z) \mathrm{d} z \leq C
$$

PROOF. For $x \in \mathbb{R}^{d}$ such that $\|x\|=1$, and $z \in \mathbb{R}$ we have

$$
q(x, z)=\left(1+z^{p}\right)^{\frac{-\alpha-d-1}{p}} q(\theta(x, z))
$$

The results follows with $c=\left(\min _{\omega \in \mathbb{S}_{d+1}} q(\omega)\right) \int\left(1+z^{p}\right)^{\frac{-\alpha-d-1}{p}} \mathrm{~d} z$ and

$$
C=\left(\max _{\omega \in \mathbb{S}_{d+1}} q(\omega)\right) \int\left(1+z^{p}\right)^{\frac{-\alpha-d-1}{p}} \mathrm{~d} z
$$

## C Proofs for Section 3

## C. 1 Proof of Theorem 1

(i) In view of Characterization (iii) from Theorem A. 1 (see also (8) in the main paper), Assumption 2 implies that the conditional distribution

$$
\mathcal{L}(\Theta, Y,\|X\| / t \mid\|X\|>t)
$$

converges weakly to the distribution of $\left(\Theta_{\infty}, Y_{\infty},\left\|X_{\infty}\right\|\right)$. Now if $f=h \circ \theta$ is a prediction function on $\mathbb{R}^{d}$, where $h$ is a continuous function defined on $\mathbb{S}$, then by compactness of $\mathbb{S}$ the function $(\theta, y) \mapsto(h(\theta)-y)^{2}$ is automatically bounded and continuous on the domain $\mathbb{S} \times[-M, M]$. Thus by weak convergence we obtain as $t \rightarrow \infty$,

$$
R_{t}(f)=\mathbb{E}\left[(h(\Theta)-Y)^{2} \mid\|X\|>t\right] \rightarrow \mathbb{E}\left[\left(h\left(\Theta_{\infty}\right)-Y_{\infty}\right)^{2}\right]=R_{P_{\infty}}(f)
$$

(ii) Recall that $R_{t}^{*}=R_{t}\left(f^{*}\right)$ where $f^{*}$ is the regression function for the pair $(X, Y)$ and $R_{P_{\infty}}^{*}=R_{P_{\infty}}\left(f_{P_{\infty}}^{*}\right)$ where $f_{P_{\infty}}^{*}$ is the regression function for the pair $\left(X_{\infty}, Y_{\infty}\right)$ defined in Lemma 1 Now we decompose $R_{t}^{*}$ as

$$
\begin{aligned}
R_{t}^{*}= & \mathbb{E}\left[\left(Y-f^{*}(X)\right)^{2} \mid \| X \geq t\right] \\
= & \underbrace{\mathbb{E}\left[\left(Y-f_{P_{\infty}}^{*}(X)\right)^{2} \mid\|X\| \geq t\right]}_{A_{t}}+\underbrace{\mathbb{E}\left[\left(f_{P_{\infty}}^{*}(X)-f^{*}(X)\right)^{2} \mid\|X\| \geq t\right]}_{B_{t}}+\ldots \\
& \cdots \underbrace{2 \mathbb{E}\left[\left(Y-f_{P_{\infty}}^{*}(X)\right)\left(f_{P_{\infty}}^{*}(X)-f^{*}(X)\right) \mid\|X\| \geq t\right]}_{C_{t}}
\end{aligned}
$$

The first term $A_{t}$ is simply $R_{t}\left(f_{P_{\infty}}^{*}\right)$. From Lemma 1 f $f_{P_{\infty}}^{*}$ is an angular function, thus Property (i) of the statement implies that $A_{t} \rightarrow R_{P_{\infty}}\left(f_{P_{\infty}}^{*}\right)$, which is $R_{P_{\infty}}^{*}$.

We now show that the second and third terms $B_{t}, C_{t}$ vanish. We use that, as a consequence of Assumption 1 $\forall x \in \mathbb{R}^{d},\left|f_{P_{\infty}}^{*}(x)\right| \leq M$ and, $\left|f^{*}(x)\right| \leq M$. Thus

$$
B_{t} \leq 4 M^{2} \mathbb{E}\left[\left|f_{P_{\infty}}^{*}(X)-f^{*}(X)\right| \mid\|X\| \geq t\right]
$$

Assumption 3 ensures that the latter display converges to 0 as $t \rightarrow \infty$. Similarly, using Assumptions 1 and 3 again, we obtain

$$
\left|C_{t}\right| \leq 4 M^{2} \mathbb{E}\left[\left|f_{P_{\infty}}^{*}(X)-f^{*}(X)\right| \mid\|X\| \geq t\right] \underset{t \rightarrow+\infty}{\longrightarrow} 0
$$

We have proved that $R_{t}^{*} \underset{t \rightarrow+\infty}{\longrightarrow} R_{P_{\infty}}^{*}$.

(iii) Recall from the introduction that $R_{\infty}^{*}=R_{\infty}\left(f^{*}\right)=\lim \sup _{t} R_{t}\left(f^{*}\right)$. Because of (ii), in fact $R_{t}\left(f^{*}\right)$ converges to $R_{P_{\infty}}^{*}$. Thus

$$
\limsup _{t} R_{t}\left(f^{*}\right)=\lim _{t} R_{t}\left(f^{*}\right)=R_{P_{\infty}}^{*}
$$

and the result follows.

(iv) From Property (iii) of the statement, we have $R_{\infty}^{*}=R_{P_{\infty}}\left(f_{P_{\infty}}^{*}\right)$. Now, Property (i) of the statement and the angular nature of $f_{P_{\infty}}^{*}$ (Lemma 1) imply that $R_{P_{\infty}}\left(f_{P_{\infty}}^{*}\right)=R_{\infty}\left(f_{P_{\infty}}^{*}\right)$.

## C. 2 Proof of Theorem 2

We recall for convenience a Bernstein-type inequality due to C. McDiarmid (see Theorem 3.8 of [41]) which is a key ingredient of the proof of Theorem 2

Lemma 4 (Bernstein-type inequality, [41]) Let $X=\left(X_{1: n}\right)$ with $X_{i}$ taking values in a set $\mathcal{X}$ and let $f$ be a real-valued function defined on $\mathcal{X}^{n}$. Let $Z=f\left(X_{1: n}\right)$. Consider the positive deviation functions, defined for $1 \leq i \leq n$ and for $x_{1: i} \in \mathcal{X}^{i}$,

$$
g_{i}\left(x_{1: i}\right)=\mathbb{E}\left[Z \mid X_{1: i}=x_{1: i}\right]-\mathbb{E}\left[Z \mid X_{1: i-1}=x_{1: i-1}\right]
$$

Denote by $b$ the maximum deviation

$$
b=\max _{1 \leq i \leq n} \sup _{x_{1: i} \in \mathcal{X}^{i}} g_{i}\left(x_{1: i}\right)
$$

Let $\hat{v}$ be the supremum of the sum of conditional variances,

$$
\hat{v}=\sup _{\left(x_{1}, \ldots, x_{n}\right) \in \mathcal{X}^{n}} \sum_{i=1}^{n} \sigma_{i}^{2}\left(f, x_{1: i-1}\right)
$$

where $\left.\sigma_{i}^{2}\left(f, x_{1: i-1}\right)\right)=\operatorname{Var}\left[g_{i}\left(X_{1: i}\right) \mid X_{1: i-1}=x_{1: i-1}\right]$. If $b$ and $\hat{v}$ are both finite, then

$$
\mathbb{P}\{Z-\mathbb{E}[Z] \geq \varepsilon\} \leq \exp \left(\frac{-\varepsilon^{2}}{2(\hat{v}+b \varepsilon / 3)}\right)
$$

for $\varepsilon>0$.

Introduce an intermediate risk functional

$$
\tilde{R}_{t_{n, k}}(h \circ \theta)=\frac{1}{k} \sum_{i=1}^{n}\left(h\left(\theta\left(X_{i}\right)\right)-Y_{i}\right)^{2} \mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}
$$

and notice that $\mathbb{E}\left[\tilde{R}_{t_{n, k}}(h \circ \theta)\right]=R_{t_{n, k}}(h \circ \theta)$. Our proof is based on the following risk decomposition,

$$
\begin{aligned}
\sup _{h \in \mathcal{H}}\left|\hat{R}_{k}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right| \leq \sup _{h \in \mathcal{H}}\left|\hat{R}_{k}(h \circ \theta)-\tilde{R}_{t_{n, k}}(h \circ \theta)\right|+\ldots \\
\sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right| .
\end{aligned}
$$

Regarding the first term on the right-hand side of Inequality 29 ,

$$
\begin{aligned}
\sup _{h \in \mathcal{H}} \mid \hat{R}_{k}(h \circ \theta) & -\tilde{R}_{t_{n, k}}(h \circ \theta) \mid \\
& =\sup _{h \in \mathcal{H}} \frac{1}{k}\left|\sum_{i=1}^{n}\left(h \circ \theta\left(X_{i}\right)-Y_{i}\right)^{2}\left(\mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}-\mathbb{1}\left\{\left\|X_{i}\right\| \geq \| X_{(k)}\right\}\right)\right| \\
& \leq \frac{4 M^{2}}{k} \sum_{i=1}^{n}\left|\mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}-\mathbb{1}\left\{\left\|X_{i}\right\| \geq \| X_{(k)}\right\}\right|
\end{aligned}
$$

The number of nonzero terms inside the sum in the above display is the number of indices $i$ such that " $\left\|X_{i}\right\|<\left\|X_{(k)}\right\|$ and $\left\|X_{i}\right\| \geq t_{n, k}$, or the other way around. In other words

$$
\left\{\left|\mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}-\mathbb{1}\left\{\left\|X_{i}\right\| \geq \| X_{(k)}\right\}\right| \neq 0\right\} \subset\left(\left\{t_{n, k} \leq X_{i}<X_{(k)}\right\} \cup\left\{X_{(k)} \leq X_{i}<t_{n, k}\right\}\right)
$$

Considering separately the cases where $X_{(k)} \leq t_{n, k}$ and $X_{(k)}>t_{n, k}$ we obtain

$$
\sup _{h \in \mathcal{H}}\left|\hat{R}_{k}(h \circ \theta)-\tilde{R}_{t_{n, k}}(h \circ \theta)\right| \leq \frac{4 M^{2}}{k}\left|\sum_{i=1}^{n} \mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}-k\right|
$$

Notice that $\sum_{i=1}^{n} \mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}$ follows a Binomial distribution with parameters $(n, k / n)$. The (classical) Bernstein inequality as stated e.g., in [41], Theorem 2.7, yields

$$
\begin{aligned}
\mathbb{P}\left\{\sup _{h \in \mathcal{H}}\left|\hat{R}_{k}(h \circ \theta)-\tilde{R}_{t_{n, k}}(h \circ \theta)\right| \geq \varepsilon\right\} & \leq \mathbb{P}\left\{\left|\sum_{i=1}^{n} \mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}-k\right| \geq k \varepsilon /\left(4 M^{2}\right)\right\} \\
& \leq 2 \exp \left(\frac{-k \varepsilon^{2}}{32 M^{4}+8 M^{2} \varepsilon / 3}\right)
\end{aligned}
$$

We now turn to the second term of Inequality $\sqrt{29}$, and we apply Lemma 4 to the function

$$
f\left(\left(x_{1}, y_{1}\right), \ldots,\left(x_{n}, y_{n}\right)\right)=\sup _{h \in \mathcal{H}}\left|\frac{1}{k} \sum_{i=1}^{n}\left(h \circ \theta\left(x_{i}\right)-y_{i}\right)^{2} \mathbb{1}\left\{\left\|x_{i}\right\| \geq t_{n, k}\right\}-R_{t_{n, k}}(h \circ \theta)\right|
$$

so that $f\left(\left(X_{1}, Y_{1}\right), \ldots,\left(X_{n}, Y_{n}\right)\right)=\sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right|$. With the notations of Lemma 4 the maximum of the positive deviations and the maximum sum of variances satisfy respectively $b \leq 4 M^{2} / k$ and $\hat{v} \leq 16 M^{4} / k$. Thus

$$
\begin{gathered}
\mathbb{P}\left\{\sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right|-\mathbb{E}\left[\sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right|\right] \geq \varepsilon\right\} \\
\leq \exp \left(\frac{-k \varepsilon^{2}}{32 M^{4}+8 M^{2} \varepsilon / 3}\right)
\end{gathered}
$$

The last step consists in bounding from above the expected deviations in the above display, that is

$$
\mathbb{E} \sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right|
$$

Let $\varepsilon_{1}, \ldots, \varepsilon_{n}$ be $n$ independent, $\{0,1\}$-valued Rademacher random variables and introduce the Rademacher average

$$
\mathcal{R}_{k}^{\varepsilon}=\sup _{h \in \mathcal{H}} \frac{1}{k}\left|\sum_{i=1}^{n} \varepsilon_{i}\left(h \circ \theta\left(X_{i}\right)-Y_{i}\right)^{2} \mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\}\right|
$$

Following a standard symmetrization argument as e.g. in the proof of Lemma 13 in[27], we obtain

$$
\mathbb{E} \sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right| \leq 2 \mathbb{E}\left[\mathcal{R}_{k}^{\varepsilon}\right]
$$

Let $\left(X_{1}^{k}, Y_{1}^{k}\right), \ldots,\left(X_{n}^{k}, Y_{n}^{k}\right)$ be independent replicates, also independent from the $X_{i}, Y_{i}$ 's, such that $\mathcal{L}\left(X_{i}^{k}, Y_{i}^{k}\right)=$ $\mathcal{L}\left((X, Y) \mid\|X\| \geq t_{n, k}\right)$. By Lemma 2.1 of [37], we have

$$
\sum_{i=1}^{n} \varepsilon_{i}\left(h \circ \theta\left(X_{i}\right)-Y_{i}\right)^{2} \mathbb{1}\left\{\left\|X_{i}\right\| \geq t_{n, k}\right\} \stackrel{d}{=} \sum_{i=1}^{\mathcal{K}} \varepsilon_{i}\left(h \circ \theta\left(X_{i}^{k}\right)-Y_{i}^{k}\right)^{2}
$$

where $\mathcal{K} \sim \operatorname{Bin}(n, k / n)$ is independent from the $\varepsilon_{i}, X_{i}, Y_{i}$ 's. Then, write

$$
\mathbb{E}\left[\mathcal{R}_{k}^{\epsilon}\right]=\frac{1}{k} \mathbb{E}\left[\mathbb{E}\left[\sup _{h \in \mathcal{H}}\left|\sum_{i=1}^{\mathcal{K}} \varepsilon_{i}\left(h \circ \theta\left(X_{i}^{k}\right)-Y_{i}^{k}\right)^{2}\right| \mid \mathcal{K}\right]\right]
$$

We first control the conditional expectation in the above display for any fixed value $\mathcal{K}=m \leq n$. For this purpose, we apply Proposition 2.1 of [25] to the class of functions $\mathcal{G}=\left\{g(x, y)=(h \circ \theta(x)-y)^{2}, h \in \mathcal{H}\right\}$.

Notice first that for $g_{i}(x, y)=\left(h_{i} \circ \theta(x)-y\right)^{2}, i=1,2$ and $Q$ any probability measure on $\mathbb{R}^{d} \times[-M, M]$ we have

$$
\begin{aligned}
\left\|g_{1}-g_{2}\right\|_{L^{2}(Q)} & =\sqrt{\mathbb{E}_{Q}\left[\left(h_{1} \circ \theta(X)-h_{2} \circ \theta(X)\right)\left(h_{1} \circ \theta(X)+h_{2} \circ \theta(X)-2 Y\right)\right]^{2}} \\
& \leq 4 M\left\|h_{1}-h_{2}\right\|_{L^{2}\left(Q_{X} \circ \theta^{-1}\right)}
\end{aligned}
$$

where $Q_{X}$ is the marginal distribution of $Q$ regarding the first component $X \in \mathbb{R}^{d}$. Thus the covering number $\mathcal{N}\left(\mathcal{G}, L_{2}(Q), \tau\right)$ for the class $\mathcal{G}$, relative to any $L_{2}(Q)$ radius $\tau$ is always less than than $\mathcal{N}\left(\mathcal{H}, L_{2}(\tilde{Q}), \tau /(4 M)\right)$ for the class $\mathcal{H}$, where $\tilde{Q}=Q_{X} \circ \theta^{-1}$. Now the class $\mathcal{H}$ has envelope function $H=M \mathbb{1}_{\mathbb{S}}(\cdot)$ and has VC-dimension $V_{\mathcal{H}}<\infty$, thus Theorem 2.6.7 in [52] yields a control of its covering number,

$$
\mathcal{N}\left(\mathcal{H}, L_{2}(\tilde{Q}), \tau M\right) \leq(A / \tau)^{2 V_{\mathcal{H}}}
$$

for some universal constant $A>0$ not depending on $\tilde{Q}$ nor $\mathcal{H}$. We obtain

$$
\mathcal{N}\left(\mathcal{G}, L_{2}(Q), \tau\right) \leq\left(4 A M^{2} / \tau\right)^{2 V_{\mathcal{H}}}
$$

Now $\mathcal{G}$ has envelope function $G=4 M^{2} \mathbb{1}_{\mathbb{R}^{d} \times \mathbb{S}}$. The previous display writes equivalently

$$
\mathcal{N}\left(\mathcal{G}, L_{2}(Q), \tau\|G\|_{L^{2}(Q)}\right) \leq(A / \tau)^{2 V_{\mathcal{H}}}
$$

Inequality (34) is precisely the first step of the proof of Proposition 2.1 in [25] (see Inequality 2.2 in the cited references), so that their upper bound on the Rademacher process applies with $\mathrm{VC}$ constant $v=2 V_{\mathcal{H}}$. The upper bound of their statement involves $\sigma^{2}=\sup _{g} \mathbb{E} g^{2} \leq 16 M^{4}$ and $U=\sup _{g}\|g\|_{\infty} \leq 4 M^{2}$, thus we may take $\sigma=U=4 M^{2}$. We obtain

$$
\mathbb{E} \sup _{h \in \mathcal{H}}\left|\sum_{i=1}^{m} \varepsilon_{i}\left(h \circ \theta\left(X_{i}^{k}\right)-Y_{i}^{k}\right)^{2}\right| \leq C^{\prime}\left(4 M^{2} V_{\mathcal{H}}+\sqrt{m V_{\mathcal{H}}}\right)
$$

for some other universal constant $C^{\prime}$. Injecting the latter control into (33) yields, using the concavity of the squared root function and $\mathbb{E}[\mathcal{K}]=k$,

$$
\begin{aligned}
\mathbb{E}\left[\mathcal{R}_{k}^{\varepsilon}\right] & \leq \frac{1}{k} C^{\prime}\left(4 M^{2} V_{\mathcal{H}}+\mathbb{E}[\sqrt{\mathcal{K}}] \sqrt{V_{\mathcal{H}}}\right) \\
& \leq \frac{1}{k} C^{\prime}\left(4 M^{2} V_{\mathcal{H}}+\sqrt{k} \sqrt{V_{\mathcal{H}}}\right)
\end{aligned}
$$

Combining $(32)$ and $(35)$ we obtain

$$
\mathbb{E} \sup _{h \in \mathcal{H}}\left|\tilde{R}_{t_{n, k}}(h \circ \theta)-R_{t_{n, k}}(h \circ \theta)\right| \leq 2 \mathbb{E}\left[\mathcal{R}_{k}^{\epsilon}\right] \leq C\left(\frac{4 M^{2} V_{\mathcal{H}}}{k}+\sqrt{\frac{V_{\mathcal{H}}}{k}}\right)
$$

with $C=2 C^{\prime}$. Finally, combining Equations (30), (31) and (36) yields

$$
\begin{aligned}
& \mathbb{P}\left\{\sup _{h \in \mathcal{H}}\left|\hat{R}_{k}(h \circ \Theta)-R_{t_{n, k}}(h \circ \Theta)\right| \geq \varepsilon+C\left(\frac{4 M^{2} V_{\mathcal{H}}}{k}+\sqrt{\frac{V_{\mathcal{H}}}{k}}\right)\right\} \\
& \leq 3 \exp \left(\frac{-k \varepsilon^{2}}{16\left(8 M^{4}+M^{2} \varepsilon / 3\right)}\right)
\end{aligned}
$$

which concludes the proof after solving for $3 \exp \left(\frac{-k \varepsilon^{2}}{16\left(8 M^{4}+M^{2} \varepsilon / 3\right)}\right)=\delta$.

## C. 3 Proof of Proposition 2

1. For $t \geq 1$ and $h \in \mathcal{H}$, write $r_{t}(h)=R_{t}(h \circ \theta)$. For all $h_{1}, h_{2} \in \mathcal{H}$, and $t \geq 1$, we have

$$
\begin{aligned}
& \left|r_{t}\left(h_{1}\right)-r_{t}\left(h_{2}\right)\right|=\left|R_{t}\left(h_{1} \circ \theta\right)-R_{t}\left(h_{2} \circ \theta\right)\right| \\
& =\left|\mathbb{E}\left[h_{1}(X)^{2}-h_{2}(X)^{2}+2 Y\left(h_{1}(X)-h_{2}(X)\right) \mid\|X\| \geq t\right]\right| \\
& \leq \mathbb{E}\left[\left|\left(h_{1}(X)+h_{2}(X)\right)\left(h_{1}(X)-h_{2}(X)\right)\right| \mid\|X\| \geq t\right]+2 \mathbb{E}\left[\left|Y\left(h_{1}(X)-h_{2}(X)\right)\right| \mid\|X\| \geq t\right] \\
& \leq 4 M\left\|h_{1}-h_{2}\right\|_{\infty}
\end{aligned}
$$

where we have used Assumption 1 to obtain the last inequality. Similarly,

$$
\begin{aligned}
& R_{P_{\infty}}\left(h_{1} \circ \theta\right)-R_{P_{\infty}}\left(h_{2} \circ \theta\right) \\
& \leq \mathbb{E}\left|\left(h_{1}\left(\Theta_{\infty}\right)+h_{2}\left(\Theta_{\infty}\right)\right)\left(h_{1}\left(\Theta_{\infty}\right)-h_{2}\left(\Theta_{\infty}\right)\right)\right|+2 \mathbb{E}\left|Y_{\infty}\left(h_{1}\left(\Theta_{\infty}\right)-h_{2}\left(\Theta_{\infty}\right)\right)\right| \\
& \leq 4 M\left\|h_{1}-h_{2}\right\|_{\infty}
\end{aligned}
$$

Let $\varepsilon>0$. By total boundedness $\exists h_{1}, \ldots, h_{L} \in \mathcal{H}$ such that $\cup_{i=1, \ldots, L} B\left(h_{i}, \varepsilon\right) \supset \mathcal{H}$. Here $B(h, \varepsilon)$ denotes the ball of radius $\varepsilon$ in $(\mathcal{C}(\mathbb{S}),\|\cdots\|)$. Now because of Assumption 2 (see Theorem 1) (i)) we have $r_{t}\left(h_{i}\right) \rightarrow$ $R_{P_{\infty}}\left(h_{i} \circ \theta\right)$ as $t \rightarrow \infty$, for all fixed $i$. Thus there exists some $T>0$ such that for all $i \in\{1, \ldots, L\}$ $\left|r_{t}\left(h_{i}\right)-R_{P_{\infty}}\left(h_{i} \circ \theta\right)\right| \leq \varepsilon$. Now for any $h \in \mathcal{H}$ and $t \geq T$, using (37) and (39) there exists $i \leq L$ such that

$$
\max \left(\left|r_{t}(h)-r_{t}\left(h_{i}\right)\right|,\left|R_{P_{\infty}}(h \circ \theta)-R_{P_{\infty}}\left(h_{i} \circ \theta\right)\right| \leq 4 M \varepsilon\right.
$$

so that

$$
\begin{aligned}
\left|r_{t}(h)-R_{P_{\infty}}(h \circ \theta)\right| & \leq\left|r_{t}(h)-r_{t}\left(h_{i}\right)\right|+\left|r_{t}\left(h_{i}\right)-R_{P_{\infty}}\left(h_{i} \circ \theta\right)\right|+\left[R_{P_{\infty}}\left(h_{i} \circ \theta\right)-R_{P_{\infty}}(h \circ \theta) \mid\right. \\
& \leq 8 M \varepsilon+\varepsilon
\end{aligned}
$$

Because $R_{P_{\infty}}(h \circ \theta)=R_{\infty}(h \circ \theta)$ (Theorem 1-(i)), the proof is complete.

2. The VC-class property of $\mathcal{H}$ (Assumption (4) ensures that for any probability measure $Q$ on $\mathbb{S}$, and any $\varepsilon>0$, the covering number $\mathcal{N}\left(\varepsilon, \mathcal{H}, L_{1}(Q)\right)$ is finite (see e.g., [52], Section 2.6.2). Our first step is to build such a probability measure $Q$ which dominates both the $\Phi_{\theta, t}$ 's and $\Phi_{\theta}$, in such a way that $\mathbb{E}\left[\left|h_{1}-h_{2}\right|(\Theta) \mid\|X\|>t\right]$ and $\mathbb{E}\left[\left|h_{1}-h_{2}\right|\left(\Theta_{\infty}\right)\right]$ are both controlled by $\int_{\mathbb{S}}\left|h_{1}-h_{2}\right| \mathrm{d} Q=\left\|h_{1}-h_{2}\right\|_{L_{1}(Q)}$. Let $Q=\frac{1}{2}\left(\Phi_{\theta, 1}+\Phi_{\theta}\right)$. Then $\Phi_{\theta}$ is absolutely continuous with respect to $Q$, and so is each $\phi_{t}, t \geq 1$, in view of the discussion above the statement in the main paper. In addition we have $\sup _{\omega \in \mathbb{S}}\left|\mathrm{d} \Phi_{\theta} / \mathrm{d} Q(\omega)\right| \leq 2$ and from Condition 2. also $\sup _{\omega \in \mathbb{S}, t \geq 1}\left|\mathrm{~d} \Phi_{\theta, t} / \mathrm{d} Q(\omega)\right| \leq 2 D$.

For any $h_{1}, h_{2}$ in $\mathcal{H}$, following the argument leading to 37 we obtain

$$
\left|r_{t}\left(h_{1}\right)-r_{t}\left(h_{2}\right)\right| \leq 4 M \int_{\mathbb{S}}\left|h_{1}-h_{2}\right| \mathrm{d} \Phi_{t} \leq 8 M D \int_{\mathbb{S}}\left|h_{1}-h_{2}\right| \mathrm{d} Q=8 M D\left\|h_{1}-h_{2}\right\|_{L_{1}(Q)}
$$

Also,

$$
\begin{aligned}
\left|R_{P_{\infty}}\left(h_{1} \circ \theta\right)-R_{P_{\infty}}\left(h_{2} \circ \theta\right)\right| & \leq \mathbb{E}\left|\left(h_{1} g\left(\Theta_{\infty}\right)+h_{2}\left(\Theta_{\infty}\right)\right)\left(h_{1}\left(\Theta_{\infty}\right)-h_{2}\left(\Theta_{\infty}\right)\right)\right|+2 \mathbb{E}\left|Y_{\infty}\left(h_{1}\left(\Theta_{\infty}\right)-h_{2}\left(\Theta_{\infty}\right)\right)\right| \\
& \leq 4 M \mathbb{E}\left[\left|h_{1}-h_{2}\right|\left(\Theta_{\infty}\right)\right] \\
& \leq 8 M\left\|h_{1}-h_{2}\right\|_{L_{1}(Q)}
\end{aligned}
$$

Let $\varepsilon>0$. Since the covering number of the class $\mathcal{H}$ for the $L_{1}(Q)$-norm is finite, for some $L \leq \mathcal{N}\left(\varepsilon, \mathcal{H}, L_{1}(Q)\right)$ there exists $h_{1}, \ldots, h_{L} \in \mathcal{H}$ such that each $h \in \mathcal{H}$ is at $L_{1}(Q)$-distance at most $\varepsilon$ from one of the $h_{i}$ 's. The rest of the proof follows the same lines as the argument following (39), up to replacing the infinity norm with the $L_{1}(Q)$-norm on $\mathcal{H}$.

## References

[1] Mastane Achab, Stéphan Clémençon, Aurélien Garivier, Anne Sabourin, and Claire Vernade. Max K-Armed Bandit: On the ExtremeHunter Algorithm and Beyond. Machine Learning and Knowledge Discovery in Databases ECML PKDD 2017, pages 389-404, 2017.

[2] Anass Aghbalou, Patrice Bertail, François Portier, and Anne Sabourin. Cross validation for extreme value analysis. arXiv:2202.00488, 2023.

[3] Anass Aghbalou, François Portier, Anne Sabourin, and Chen Zhou. Tail inverse regression: Dimension reduction for prediction of extremes. Bernoulli, 30(1):503-533, 2024.

[4] André Altmann, Laura Toloşi, Oliver Sander, and Thomas Lengauer. Permutation importance: a corrected feature importance measure. Bioinformatics, 26(10):1340-1347, 2010.

[5] Jan Beirlant, Yuri Goegebeur, Johan Segers, and Jozef L Teugels. Statistics of extremes: theory and applications. John Wiley \& Sons, 2006.

[6] Stéphane Boucheron, Gábor Lugosi, and Pascal Massart. Concentration Inequalities: A Nonasymptotic Theory of Independence. Oxford University Press, 2013.

[7] L. Breiman. Random forests. Machine learning, 45:5-32, 2001.

[8] Christian Brownlees, Emilien Joly, and Gábor Lugosi. Empirical risk minimization for heavy-tailed losses. The Annals of Statistics, 43(6):2507-2536, 2015.

[9] Juan-Juan Cai, John H.J. Einmahl, and Laurens De Haan. Estimation of extreme risk regions under multivariate regular variation. The Annals of Statistics, 39(3):1803-1826, 2011.

[10] Alexandra Carpentier and Michal Valko. Extreme bandits. In Advances in Neural Information Processing Systems 27, pages 1089-1097. Curran Associates, Inc., 2014.

[11] Valerie Chavez-Demoulin, Paul Embrechts, and Sylvain Sardy. Extreme-quantile tracking for financial time series. Journal of Econometrics, 181(1):44-52, 2014.

[12] Maël Chiapino, Stéphan Clémençon, Vincent Feuillard, and Anne Sabourin. A multivariate extreme value theory approach to anomaly clustering and visualization. Computational Statistics, 35(2):607-628, 2020.

[13] Maël Chiapino, Anne Sabourin, and Johan Segers. Identifying groups of variables with the potential of being large simultaneously. Extremes, 22:193-222, 2019.

[14] Stéphan Clémençon, Hamid Jalalzai, Stéphane Lhaut, Anne Sabourin, and Johan Segers. Concentration bounds for the empirical angular measure with statistical learning applications. Bernoulli, 29(4):2797-2827, 2023.

[15] Daniel Cooley and Emeric Thibaud. Decompositions of dependence for high-dimensional extremes. Biometrika, 106(3):587-604, 2019.

[16] A. Daouia, L. Gardes, and S. Girard. On kernel smoothing for extremal quantile regression. Bernoulli, 19:2557-2589, 2013 .

[17] Abdelaati Daouia, Simone A Padoan, Gilles Stupfler, et al. Optimal weighted pooling for inference about the tail index and extreme quantiles. Bernoulli, 2023.

[18] L. De Haan and A. Ferreira. Extreme value theory: an introduction. Springer Science \& Business Media, 2007.

[19] Laurens De Haan and Sidney I. Resnick. On regular variation of probability densities. Stochastic processes and their applications, 25:83-93, 1987.

[20] Holger Drees and Anne Sabourin. Principal component analysis for multivariate extremes. Electronic Journal of Statistics, 15:908-943, 2021.

[21] J. H. J. Einmahl and J. Segers. Maximum empirical likelihood estimation of the spectral measure of an extreme-value distribution. Ann. Stat., 37:2953-2989, 2009.

[22] J. HJ Einmahl, L. de Haan, and V. I Piterbarg. Nonparametric estimation of the spectral measure of an extreme value distribution. Ann. Stat., 29:1401-1423, 2001.

[23] Jonathan El Methni, Laurent Gardes, Stéphane Girard, and Armelle Guillou. Estimation of extreme quantiles from heavy and light tailed distributions. Journal of Statistical Planning and Inference, 142(10):2735-2747, 2012 .

[24] Sebastian Engelke and Adrien S Hitz. Graphical models for extremes. Journal of the Royal Statistical Society Series B: Statistical Methodology, 82(4):871-932, 2020.

[25] Evarist Giné and Armelle Guillou. On consistency of kernel density estimators for randomly censored data: rates holding uniformly over adaptive intervals. Annales de l'IHP Probabilités et statistiques, 37(4):503-522, 2001.

[26] Nicola Gnecco, Edossa Merga Terefe, and Sebastian Engelke. Extremal random forests. arxiv:201.12865, 2022.

[27] Nicolas Goix, Anne Sabourin, and Stephan Clémençon. Learning the dependence structure of rare events: a non-asymptotic study. Conference on Learning Theory, pages 843-860, 2015.

[28] Nicolas Goix, Anne Sabourin, and Stephan Clémençon. Sparse representation of multivariate extremes with applications to anomaly ranking. Artificial Intelligence and Statistics, pages 75-83, 2016.

[29] Nicolas Goix, Anne Sabourin, and Stephan Clémençon. Sparse representation of multivariate extremes with applications to anomaly detection. Journal of Multivariate Analysis, 161:12-31, 2017.

[30] Ulrike Grömping. Variable importance in regression models. Wiley interdisciplinary reviews: Computational statistics, 7(2):137-152, 2015.

[31] László Györfi, Michael Kohler, Adam Krzyzak, and Harro Walk. A Distribution-Free Theory of Nonparametric Regression. Springer, 2002.

[32] Adrien Hitz and Robin Evans. One-component regular variation and graphical modeling of extremes. Journal of Applied Probability, 53(3):733-746, 2016.

[33] Henrik Hult and Filip Lindskog. Regular variation for measures on metric spaces. Publications de l'Institut Mathématique, 80(94):121-140, 2006.

[34] Hamid Jalalzai, Stephan Clémençon, and Anne Sabourin. On binary classification in extreme regions. In Advances in Neural Information Processing Systems, pages 3092-3100, 2018.

[35] Anja Janßen and Phyllis Wan. k-means clustering of extremes. Electronic Journal of Statistics, 14(1):12111233,2020 .

[36] Guillaume Lecué and Shahar Mendelson. Learning subgaussian classes : Upper and minimax bounds. arXiv:1305.4825, 2013.

[37] Stéphane Lhaut, Anne Sabourin, and Johan Segers. Uniform concentration bounds for frequencies of rare events. Statistics 83 Probability Letters, 189:109610, 2022.

[38] Filip Lindskog, Sidney I Resnick, and Joyjit Roy. Regularly varying measures on metric spaces: Hidden regular variation and hidden jumps. Probability Surveys, pages 270-314, 2014.

[39] Gabor Lugosi and Shahar Mendelson. Risk minimization by median-of-means tournaments. Journal of the European Mathematical Society, 22(3):925-965, 2019.

[40] Pascal Massart. Concentration Inequalities and Model Selection. Springer-Verlag, 2007.

[41] Colin McDiarmid. Concentration. Probabilistic methods for algorithmic discrete mathematics, pages 195-248, 1998.

[42] Shahar Mendelson. On aggregation for heavy-tailed classes. Probability Theory and Related Fields, 168(34):641-674, 2017 .

[43] Nicolas Meyer and Olivier Wintenberger. Sparse regular variation. Advances in Applied Probability, 53(4):1115$1148,2021$.

[44] Nicolas Meyer and Olivier Wintenberger. Multivariate sparse clustering for extremes. Journal of the American Statistical Association, 0(just-accepted):1-23, 2023.

[45] Stefano Nembrini, Inke R König, and Marvin N Wright. The revival of the gini importance? Bioinformatics, 34(21):3711-3718, 2018.

[46] Mesrob I. Ohannessian and Munther A. Dahleh. Rare probability estimation under regularly varying heavy tails. Conference on Learning Theory, pages 21.1-21.24, 2012.

[47] Fabian Pedregosa, Gael Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, Jake Vanderplas, Alexandre Passos, David Cournapeau, Matthieu Brucher, Matthieu Perrot, and Edouard Duchesnay. Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12:2825-2830, 2011.

[48] Sidney Resnick and Laurens de Haan. Second-order regular variation and rates of convergence in extreme-value theory. The Annals of Probability, 24(1):97 - 124, 1996.

[49] Sidney I. Resnick. Extreme values, regular variation and point processes. Springer, 2013.

[50] Emma S Simpson, Jennifer L Wadsworth, and Jonathan A Tawn. Determining the dependence structure of multivariate extremes. Biometrika, 107(3):513-532, 2020.

[51] Alec Stephenson. Simulating multivariate extreme value distributions of logistic type. Extremes, 6(1):49-59, 2003 .

[52] A. W. van der Vaart and Jon Wellner. Weak Convergence and Empirical Processes: With Applications to Statistics. Springer Series in Statistics. Springer-Verlag, New York, 1996.

[53] Jasper Velthoen, Clément Dombry, Juan-Juan Cai, and Sebastian Engelke. Gradient boosting for extreme quantile regression. Extremes, 0(0):1-29, 2023.

[54] Edoardo Vignotto and Sebastian Engelke. Extreme value theory for anomaly detection-the gpd classifier. Extremes, 23(4):501-520, 2020.

[55] Edoardo Vignotto, Sebastian Engelke, and Jakob Zscheischler. Clustering bivariate dependencies of compound precipitation and wind extremes over great britain and ireland. Weather and climate extremes, 32:100318, 2021.

[56] Yaqing Wang, Quanming Yao, James T. Kwok, and Lionel M. Ni. Generalizing from a few examples: A survey on few-shot learning. ACM Comput. Surv., 53(3), jun 2020.

