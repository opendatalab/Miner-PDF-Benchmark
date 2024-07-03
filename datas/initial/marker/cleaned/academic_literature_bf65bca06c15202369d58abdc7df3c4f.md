# Permutation Testing For Monotone Trend

Joseph P. Romano∗
Departments of Statistics and Economics Stanford University romano@stanford.edu Marius A. Tirlea†
Department of Statistics Stanford University mtirlea@stanford.edu April 11, 2024

## Abstract

In this paper, we consider the fundamental problem of testing for monotone trend in a time series. While the term "trend" is commonly used and has an intuitive meaning, it is first crucial to specify its exact meaning in a hypothesis testing context. A commonly used well-known test is the Mann-Kendall test, which we show does not offer Type 1 error control even in large samples. On the other hand, by an appropriate studentization of the Mann-Kendall statistic, we construct permutation tests that offer asymptotic error control quite generally, but retain the exactness property of permutation tests for i.i.d. observations. We also introduce "local" Mann-Kendall statistics as a means of testing for local rather than global trend in a time series. Similar properties of permutation tests are obtained for these tests as well.

Key Words:. Hypothesis Testing, Mann-Kendall Test, Permutation Test, Time Series, Trend.

## 1 Introduction

In both theoretical and applied time series analysis, the issue of determining whether or not a given sequence of observations exhibits monotone trend is a crucial element of understanding 1 the process under study. An important nonparametric method used for testing monotone trend is the Mann-Kendall trend test (see Mann (1945) and Kendall (1990)), which tests the hypothesis

## Hmk : X1, . . . , Xn I.I.D.

using a rank statistic (defined in (3.1)). Under the null hypothesis HMK, the Mann-Kendall test of nominal level α is exact in finite samples and asymptotically valid. However, while it is the case that an i.i.d. sequence of random variables {Xi: i ∈ [n]} *should* intuitively be described as exhibiting no monotone trend, it is also intuitively reasonable that a non-i.i.d.

sequence {Xi: i ∈ [n]} may also exhibit a lack of monotone trend. Indeed, in the time series contexts in which such problems are usually considered, there is an implicit dependence structure in time of the sequence under examination, in which case the null hypothesis HMK
is not the null hypothesis intended to be under consideration. On account of this, significant problems of error control may arise, since the null hypotheses of i.i.d. and "no monotone trend" are quite different. This may lead to issues of Type 1 and Type 3 (or directional) error control analogous to those described in Romano and Tirlea (2022) for testing autocorrelations.

In the context of this paper, the issue is that one can reject the null hypothesis and conclude that there exists a monotone trend not because there does truly exist some monotone trend, but on account of the test only controlling Type 1 error for i.i.d. sequences, and not for weakly dependent sequences exhibiting no monotone trend.

We propose two nonparametric testing procedures for the hypothesis

## H : {Xi: I ∈ N} Exhibits No Monotone Trend,

where several precise definitions of the null hypothesis H are considered. In particular, we define the notions of *global* and *local* monotone trend, and consider permutation testing procedures based on the full, or global, Mann-Kendall statistic. We also introduce a novel statistic, termed the local Mann-Kendall statistic, which is used for testing the null hypothesis of a lack of local monotone trend.

In the broader context of testing for and estimation of monotone trend, Dietz and Killeen
(1981) provide a multivariate test of trend with application to a pharmaceutical setting, Zhao and Woodroofe (2012) consider isotonic estimators of sequences with monotone trend under stationarity, and Han and Qian (2018) extend the Mann-Kendall test to the setting of independent, but not necessarily i.i.d. sequences. In a more applied setting, Yue et al. (2002)
discuss application of the Mann-Kendall and Spearman's ρ test to hydrological time series, Hamed (2008) considers a modification of the Mann-Kendall test under scaling, and Wang et al. (2020) consider the power of different versions of the Mann-Kendall test in a simulation study. Permutation tests of trend based on OLS regression are discussed in Romano and Tirlea (2024).

There has been a resurgence in the use of permutation and randomization tests, as they offer the prospect of valid inference in complex settings. However, they can often fail (even in large samples) without careful implementation. Indeed, this paper is part of a growing body of work that shows how permutation tests can indeed be constructed that offer exact finite-sample validity under a restricted null hypothesis, but also offer asymptotic validity in much more generality. Many such instances of this phenomenon are given in Romano and Tirlea (2022).

Section 2 provides a precise definition of the null hypotheses of a lack of monotone trend under consideration. The main results for the global Mann-Kendall test are given in Section 3, in which we provide conditions for the asymptotic validity of the permutation test when
{Xn : n ∈ N} is a stationary, absolutely regular sequence, satisfying fairly standard mixing conditions. For instance, the results in this section may be applied freely to a large class of stationary ARMA sequences. Section 4 introduces the local Mann-Kendall statistic, and furnishes the main results for asymptotic validity of the permutation test when {Xn : n ∈ N}
is a stationary, α-mixing sequence. Section 5 provides simulation studies illustrating the results of the previous sections. The majority of the proofs are deferred to the supplement, owing to the length and technical requirements required to prove the results.

Most of our results require some notions of stationarity, weak dependence, and absolute regularity, whose definitions we now review. A sequence {Xn : n ∈ N} is called stationary if it is strongly stationary, i.e. if, for all k ∈ N, for all {ni: i ∈ [k]} ⊂ N, and for all m ∈ N,

$$\left(X_{n_{1}},\,\ldots,\,X_{n_{k}}\right)\stackrel{d}{=}\left(X_{m+n_{1}},\,\ldots,\,X_{m+n_{k}}\right)\,.$$

With these notational conventions, we turn to a brief discussion of the notion of weak dependence in a sequence of random variables.

Definition 1.1. Let {Xn : n ∈ N} be a sequence of (Ω, F, P)-measurable random variables. For each n ∈ N, let Fn = σ(Xm : m ≤ n), and let Gn = σ(Xm : m ≥ n). For n ∈ N, let αX(n)
be Rosenblatt's α-mixing coefficient,

$$\alpha_{X}(n)=\operatorname*{sup}_{m\in\mathbb{N}}\operatorname*{sup}_{A\in{\mathcal{F}}_{m},\,B\in{\mathcal{G}}_{m+n}}|\mathbb{P}(A\cap B)-\mathbb{P}(A)\mathbb{P}(B)|$$

We say that the sequence {Xn} is strongly mixing or α-mixing if αX(n) → 0 as n → ∞.

For n ∈ N, let βX(n) be the β-mixing or absolute regularity coefficient, defined as

$$\beta_{X}(n)=\operatorname*{sup}_{m\in\mathbb{N}}\mathbb{E}\left[\operatorname*{sup}_{B\in{\mathcal{G}}_{m+n}}|\mathbb{P}(B\,|\,{\mathcal{F}}_{m})-\mathbb{P}(B)|\right]\ .$$

We say that the sequence {Xn} is absolutely regular or β-mixing if βX(n) → 0 as n → ∞.

Remark 1.1. As discussed in Bradley (2005), we have that, for any sequence {Xn : n ∈ N}
of R
d-valued random variables, and for each n ∈ N,

$$2\alpha_{X}(n)\leq\beta_{X}(n)\ .$$

It follows that any β-mixing sequence is also α-mixing.

## 2 Defining Monotone Trend

We turn our attention to establishing the meaning of the expression "monotone trend" used in the remainder of this paper. In Mann (1945), it is the case that monotone trend is defined solely in contrast to the null of i.i.d., and is not explicitly defined in itself. However, appropriately defining this phrase, or, more pertinently, defining a lack of monotone trend, is essential in order to conduct a hypothesis test of a lack of monotone trend, since otherwise defining the null becomes impossible.

In this work, we restrict attention to consideration of weakly dependent sequences, as defined earlier. When considering the monotonicity (or lack thereof) of the sequence {Xn :
n ∈ N}, we provide some examples of the difficulties arising when using traditional notions of monotonicity, such as E[Xi] < E[Xj] for *i < j*.

Example 2.1. *(Positive local trend, negative global trend)* Let *c, ϵ >* 0. Consider the sequence
{Yn : n ∈ N} such that Y0 = 0, and, for all n ≥ 1,

$$Y_{n}=\sum_{i=1}^{n}X_{i}\ ,$$

where the Xi are i.i.d. such that

$$X_{i}=\begin{cases}1,\ \mathrm{with~probability~}1-\epsilon\ ,\\ -c,\ \mathrm{with~probability~}\epsilon\ .\end{cases}$$

Let δ > 0, and let M ∈ N. By letting ϵ = (1 − δ)
1/M and c be sufficiently large, we have that {Yn} is a (strictly) decreasing sequence in expectation, and so this sequence exhibits a negative *global* monotone trend with probability 1, since, by the strong law of large numbers,

$$\frac{1}{n}Y_{n}\stackrel{a.s.}{\rightarrow}\mathbb{E}[X_{1}]<0\ ,$$
$\mathbb{M}_{n}$ is a $n$-dimensional $\mathbb{M}(V_{n}\geq V_{n})$ at $1$ at $n$
from which it follows that, for *i < j*, as j − i → ∞, P(Yi > Yj ) → 1, and in fact, for any constant K ∈ R
+, P(Yi > Yj + K) → 1 as j − i → ∞.



However, such a sequence exhibits a *local* monotone trend in the opposite direction in the following sense: for any n ∈ N, we have that

$$\mathbb{P}(X_{n}<X_{n+1}<\cdots<X_{n+M-1})=1-\delta\ .$$

To conclude, since it is possible to construct such a sequence for any choice of δ and M, we may construct a sequence {Xn : n ∈ N} with the following property: for any i ∈ N, the sequence (Xi*, . . . , X*i+M−1) is strictly increasing with probability (1 − δ), but Xn *→ −∞*
with probability 1.

Example 2.1 indicates that some distinction is required between the notions of local and global monotone trend. In particular, as will be illustrated in Section 3, strictly stationary and weakly dependent (in particular, absolutely regular) sequences cannot, by definition, exhibit global trend, in the sense that, as |j − i*| → ∞*,

$$\mathbb{P}(X_{i}\leq X_{j})-\mathbb{P}(X_{i}\geq X_{j})\to0\ .$$

On account of this property of strictly stationary and weakly dependent sequences, it follows that any test of monotone trend in this context is, in fact, a test of stationarity, since one cannot disentangle the properties of stationarity and lack of monotone trend (see Remark 3.1). While there is an argument to be made that the restriction of stationarity is too strong in such a setting, this assumption is necessary to ensure some limiting behaviour of functions of the sequence {Xn : n ∈ N}; indeed, even without considering weakly dependent processes, there exist sequences of independent, uniformly bounded random variables for which, for example, the sample mean does not converge in distribution.

In light of this, we therefore consider a test of global monotone trend to test the null hypothesis

$$\mathbf{\partial}\colon\{X_{n}:n$$

## H0 : {Xn : N ∈ N} Is Stationary,

where, for methods developed later in this paper, we consider the power of such tests against alternatives the form of which is explicitly specified.

Fortunately, the issue of appropriately defining the notion of local monotone trend is a simpler one; in particular, local monotonicity is a property which is not directly tied to the stationarity of a sequence. For a simple example of a sequence with no local monotone trend, consider Xn being i.i.d. random variables drawn from a continuous distribution F. In this setting, which is the null setting of the original test of Mann (1945), any ordering of any local subsequence of this process (Xn*, . . . , X*n+M−1) is equally likely, and any definition of local monotone trend should exclude this example from exhibiting such a trend. In contrast, a sequence for which it should be said that a local monotone trend exists is given in the example below.

Example 2.2. *(Markov chain with local monotone trend)* Let M ∈ N, and let ϵ > 0. Let

π−M =
ϵ
1 − (1 − ϵ)
2M+1 .
$$\mathbf{r}=(1-\epsilon)\mathbf{a}\mathbf{u}+\mathbf{r}$$. 
For each i *∈ {−*M + 1*, . . . , M*}, let

$$\pi_{i}=\pi_{-M}\cdot(1-\epsilon)^{i+M}$$

Consider the Markov chain {Xn : n ∈ N} on the state space {−*M, . . . , M*} with initial distribution π, and transition matrix

$$P_{i,j}=\begin{cases}1-\epsilon,&j=i+1{\mathrm{~and~}}i\leq M-1\\ 1-\epsilon,&i=j=M\\ \epsilon,&j=-M\end{cases}$$

This is an irreducible, aperiodic Markov chain on a finite state space with stationary distribution π. In particular, by the weak Markov property, this sequence is strictly stationary, and is absolutely regular, as a consequence of standard convergence results for irreducible, aperiodic Markov chains on a finite state space (see Freedman (2011)). A sample path from such a process is shown below.





For an appropriate choice of ϵ and M, this process exhibits the same local behaviour as the process in Example 2.1; namely, for any arbitrary run length K ∈ N and any arbitrarily small δ > 0, one can construct such a process for which, for any n,

$$\mathbb{P}(X_{n}<X_{n+1}<\cdots<X_{n+K})\geq(1-\delta)\ ,$$

i.e. one may construct a sequence with arbitrarily strong local monotone trend.

In light of these examples, we proceed to define the null hypotheses of no global monotone trend and no local monotone trend. In order to test the hypothesis of no global monotone trend in the setting of weakly dependent sequences, we use the null hypothesis

$$H_{0}^{(g)}:\{X_{n}\}\ \exists$$

In order to test the hypothesis of no local monotone trend of order M in the setting of strictly stationary, weakly dependent sequences, we use the null hypothesis

$$H_{0,M}^{(l)}:\frac{2}{(n-M)M}\sum_{i<j\leq i+M}(\mathbb{P}(X_{i}<X_{j})-\mathbb{P}(X_{i}>X_{j}))=0\ .$$

Of course, under strict stationarity, this is equivalent to the null hypothesis

$$\tilde{H}_{0,M}^{(l)}:\sum_{i=2}^{M+1}(\mathbb{P}(X_{1}<X_{i})-\mathbb{P}(X_{1}>X_{i}))=0\ .$$  Does precisely defined, we may now begin construct 
With these null hypotheses precisely defined, we may now begin construction of appropriate permutation testing procedures for both global and local monotone trend.

## 3 Testing For Global Trend

In this section, we consider the problem of testing the null hypothesis

$$H_{0}^{(g)}:\{X_{i}:i\in[n]\}{\mathrm{~is~stationary}},$$

in the setting where the sequence {Xi: i ∈ [n]} is absolutely regular. When the distribution of (X1*, . . . , X*n) is invariant under permutation, i.e. the sequence is exchangeable, the randomization hypothesis holds, and so one may construct permutation tests of the hypothesis H
(g)
0 with exact level α. However, in the case of absolutely regular sequences, by Lemma S.3.1 in Romano and Tirlea (2022), exchangeability and i.i.d. are equivalent conditions. This implies that any permutation testing procedure will retain the property of exactness under the additional assumption that the Xi are i.i.d., and this is the only condition under which the randomization hypothesis holds in this setting.

However, if the realizations of the sequence {Xi: i ∈ [n]} are not independent or are not i.i.d., the test may not be valid even asymptotically, i.e. the rejection probability of a permutation test may not be equal to α or even close to α as n → ∞. Our goal is therefore to construct a testing procedure which has asymptotic rejection probability equal to α, but which also retains finite sample exactness under the additional assumption that the Xi are i.i.d., and so appropriate consideration of the asymptotic properties of the permutation distribution and the test statistic must be undertaken. We wish to consider a permutation test based on the Mann-Kendall statistic, and so we may begin by defining the Mann-Kendall statistic and analyzing the limiting behavior of the permutation distribution Rˆn based on this test statistic.

## 3.1 The Global Mann-Kendall Statistic

Definition 3.1. For X1*, . . . , X*n a sequence of random variables, let

$$U_{n}=U_{n}(X_{1},\,\ldots,\,X_{n})=\binom{n}{2}^{-1}\sum_{i=1}^{n}\sum_{j=i}^{n}\left(I\{X_{j}>X_{i}\}-I\{X_{i}>X_{j}\}\right)\.$$  be the (global) Mann-Kendall statistic.  
Theorem 3.1. Let {Xi: i ∈ N} *be a sequence of random variables such that, for all* i ̸= j, P(Xi = Xj ) = 0.

Let Rˆn be the permutation distribution, based on the test statistic √nUn*, with associated* group of transformations Sn, the symmetric group of order n. We have that, as n → ∞,

$$\operatorname*{sup}_{t\in\mathbb{R}}\left|{\hat{R}}_{n}(t)-\Phi(3t/2)\right|\ ,$$  $d$ *Gaussian c.d.f.*
where Φ is the standard Gaussian c.d.f.

Proof. Let Πn ∼ Unif(Sn), independent of {Xi, i ∈ [n]}. Let

$${\mathrm{dent~of~}}\{X_{i},\,i\in[n]\}.{\mathrm{~Let~}}$$
$\mathfrak{L}(G,\lambda)$ is $\lambda$. 
UΠn = Un(XΠn(1), . . . , XΠn(n)) .
Conditional on the sequence {Xi, i ∈ [n]}, we observe that, on account of the lack of ties, we have that each ordering of the XΠn(i)is equally likely. Since the distribution of Un only depends on the ranks of the sequence {Xi: i ∈ [n]}, the result follows by Mann (1945).

We observe that, other than the assumption of no ties among the {Xi}, no other conditions are required for the result of Theorem 3.1. This occurs since Un is a rank statistic, and, under the action of a random permutation Πn, the ranks of the {Xi} are uniformly distributed over the set of permutations Sn, and so the permutation distribution Rˆn is exactly equal to the distribution of Un under the when the Xi are independent and identically distributed.

In order to appropriately assess the asymptotic validity of the permutation test based on this statistic, we must turn our attention to determining the asymptotic distribution of Un.

## 3.2 Asymptotic Distribution Of The Mann-Kendall Statistic

Having determined the limiting behavior of the permutation distribution based on Un, we now consider the true unconditional limiting distribution of the test statistic, since consistency would require these limiting distributions be the same. Due to allowing quite general forms of weak dependence, the asymptotic distribution of the test statistic presents more of a challenge.

We proceed as follows: although Un is not a U-statistic, since the corresponding kernel h is antisymmetric, we may apply the same idea behind the projection method used to find the asymptotic distribution of U-statistics as in the original proof due to Hoeffding (1948),
i.e. we linearize the statistic Un. Note, however, the linearization is not based on the true
"projection" based on conditional expectations, but rather based on a "pseudo-projection",
which assumes the observations are i.i.d. In order to perform this linearization, we require the following definition, as well as the subsequent lemma.

Definition 3.2. For {ij: j ∈ [k]} ⊂ N, let {Xij
: j ∈ [k]} be a sequence of random variables.

For each j ∈ {1*, . . . , k* − 1}, let P
(k)
j be the probability measure defined by

$$\mathbb{P}_{j}^{(k)}(E^{(j)}\times E^{(k-j)})=\mathbb{P}((X_{i_{1}},\,\ldots,\,X_{i_{j}})\in E^{(j)})\mathbb{P}((X_{i_{j+1}},\,\ldots,\,X_{i_{k}})\in E^{(k-j)})\,$$  where $E^{(j)}$ and $E^{(k-j)}$ are Borel sets in $\mathbb{R}^{j}$ and $\mathbb{R}^{k-j}$, respectively. Also, let $\mathbb{P}_{0}^{k}$ be the 

probability measure defined by

$$\mathbb{P}_{0}^{k}(E^{(k)})=\mathbb{P}((X_{i_{1}},\,\ldots,\,X_{i_{k}})\in E^{(k)})\ ,$$  del set in $\mathbb{R}^{k}$.  

where E
(k)is a Borel set in R
Lemma 3.1. Let h : R
k → R be a Borel function such that |h| ≤ M*, for some* M ∈ R
+.

Then

$$\left|\int_{\mathbb{R}^{k}}h(x_{1},\,\ldots,\,x_{k})\mathrm{d}\mathbb{P}_{0}^{(k)}-\int_{\mathbb{R}^{k}}h(x_{1},\,\ldots,\,x_{k})\mathrm{d}\mathbb{P}_{j}^{(k)}\right|\leq2M\beta_{X}(i_{j+1}-i_{j})\ .$$

Proof. Let ν be the signed measure P
(k)
0 − P
(k)
j, and let |ν| denote its corresponding total variation measure. We have that

$$\left|\int_{\mathbb{R}^{k}}h(x_{1},\,\ldots,\,x_{k})\mathrm{d}\mathbb{P}_{0}^{(k)}-\int_{\mathbb{R}^{k}}h(x_{1},\,\ldots,\,x_{k})\mathrm{d}\mathbb{P}_{j}^{(k)}\right|=\left|\int_{\mathbb{R}^{k}}h(x_{1},\,\ldots,\,x_{k})\mathrm{d}\nu\right|$$ $$\leq\int_{\mathbb{R}^{k}}|h(x_{1},\,\ldots,\,x_{k})|\mathrm{d}|\nu|$$ $$\leq2M\cdot\mathrm{TV}\left(\mathbb{P}_{0}^{(k)},\,\mathbb{P}_{j}^{(k)}\right)$$ $$=2M\beta x(i_{j+1}-i_{j})\,$$  where TV denotes total variation distance, and the final equality follows by Voltonskii and 
Rozanov (1961).