# Permutation Testing for Monotone Trend 

Joseph P. Romano*<br>Departments of Statistics and Economics<br>Stanford University<br>romano@stanford.edu

Marius A. Tirlea ${ }^{\dagger}$<br>Department of Statistics<br>Stanford University<br>mtirlea@stanford.edu

April 11, 2024


#### Abstract

In this paper, we consider the fundamental problem of testing for monotone trend in a time series. While the term "trend" is commonly used and has an intuitive meaning, it is first crucial to specify its exact meaning in a hypothesis testing context. A commonly used well-known test is the Mann-Kendall test, which we show does not offer Type 1 error control even in large samples. On the other hand, by an appropriate studentization of the Mann-Kendall statistic, we construct permutation tests that offer asymptotic error control quite generally, but retain the exactness property of permutation tests for i.i.d. observations. We also introduce "local" Mann-Kendall statistics as a means of testing for local rather than global trend in a time series. Similar properties of permutation tests are obtained for these tests as well.


Key Words: Hypothesis Testing, Mann-Kendall Test, Permutation Test, Time Series, Trend.

## 1 Introduction

In both theoretical and applied time series analysis, the issue of determining whether or not a given sequence of observations exhibits monotone trend is a crucial element of understanding

*Supported by NSF Grant MMS-1949845.

†Supported by NSF Grant MMS-1949845.
the process under study. An important nonparametric method used for testing monotone trend is the Mann-Kendall trend test (see Mann (1945) and Kendall (1990)), which tests the hypothesis

$$
H_{\mathrm{MK}}: X_{1}, \ldots, X_{n} \text { i.i.d. }
$$

using a rank statistic (defined in (3.1)). Under the null hypothesis $H_{\mathrm{MK}}$, the Mann-Kendall test of nominal level $\alpha$ is exact in finite samples and asymptotically valid. However, while it is the case that an i.i.d. sequence of random variables $\left\{X_{i}: i \in[n]\right\}$ should intuitively be described as exhibiting no monotone trend, it is also intuitively reasonable that a non-i.i.d. sequence $\left\{X_{i}: i \in[n]\right\}$ may also exhibit a lack of monotone trend. Indeed, in the time series contexts in which such problems are usually considered, there is an implicit dependence structure in time of the sequence under examination, in which case the null hypothesis $H_{\mathrm{MK}}$ is not the null hypothesis intended to be under consideration. On account of this, significant problems of error control may arise, since the null hypotheses of i.i.d. and "no monotone trend" are quite different. This may lead to issues of Type 1 and Type 3 (or directional) error control analogous to those described in Romano and Tirlea (2022) for testing autocorrelations. In the context of this paper, the issue is that one can reject the null hypothesis and conclude that there exists a monotone trend not because there does truly exist some monotone trend, but on account of the test only controlling Type 1 error for i.i.d. sequences, and not for weakly dependent sequences exhibiting no monotone trend.

We propose two nonparametric testing procedures for the hypothesis

$$
H:\left\{X_{i}: i \in \mathbb{N}\right\} \text { exhibits no monotone trend, }
$$

where several precise definitions of the null hypothesis $H$ are considered. In particular, we define the notions of global and local monotone trend, and consider permutation testing procedures based on the full, or global, Mann-Kendall statistic. We also introduce a novel statistic, termed the local Mann-Kendall statistic, which is used for testing the null hypothesis of a lack of local monotone trend.

In the broader context of testing for and estimation of monotone trend, Dietz and Killeen (1981) provide a multivariate test of trend with application to a pharmaceutical setting, Zhao and Woodroofe (2012) consider isotonic estimators of sequences with monotone trend under stationarity, and Han and Qian (2018) extend the Mann-Kendall test to the setting of independent, but not necessarily i.i.d. sequences. In a more applied setting, Yue et al. (2002) discuss application of the Mann-Kendall and Spearman's $\rho$ test to hydrological time series, Hamed (2008) considers a modification of the Mann-Kendall test under scaling, and Wang et al. (2020) consider the power of different versions of the Mann-Kendall test in a simulation
study. Permutation tests of trend based on OLS regression are discussed in Romano and Tirlea (2024).

There has been a resurgence in the use of permutation and randomization tests, as they offer the prospect of valid inference in complex settings. However, they can often fail (even in large samples) without careful implementation. Indeed, this paper is part of a growing body of work that shows how permutation tests can indeed be constructed that offer exact finite-sample validity under a restricted null hypothesis, but also offer asymptotic validity in much more generality. Many such instances of this phenomenon are given in Romano and Tirlea (2022).

Section 2 provides a precise definition of the null hypotheses of a lack of monotone trend under consideration. The main results for the global Mann-Kendall test are given in Section 3 , in which we provide conditions for the asymptotic validity of the permutation test when $\left\{X_{n}: n \in \mathbb{N}\right\}$ is a stationary, absolutely regular sequence, satisfying fairly standard mixing conditions. For instance, the results in this section may be applied freely to a large class of stationary ARMA sequences. Section 4 introduces the local Mann-Kendall statistic, and furnishes the main results for asymptotic validity of the permutation test when $\left\{X_{n}: n \in \mathbb{N}\right\}$ is a stationary, $\alpha$-mixing sequence. Section 5 provides simulation studies illustrating the results of the previous sections. The majority of the proofs are deferred to the supplement, owing to the length and technical requirements required to prove the results.

Most of our results require some notions of stationarity, weak dependence, and absolute regularity, whose definitions we now review. A sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ is called stationary if it is strongly stationary, i.e. if, for all $k \in \mathbb{N}$, for all $\left\{n_{i}: i \in[k]\right\} \subset \mathbb{N}$, and for all $m \in \mathbb{N}$,

$$
\left(X_{n_{1}}, \ldots, X_{n_{k}}\right) \stackrel{d}{=}\left(X_{m+n_{1}}, \ldots, X_{m+n_{k}}\right)
$$

With these notational conventions, we turn to a brief discussion of the notion of weak dependence in a sequence of random variables.

Definition 1.1. Let $\left\{X_{n}: n \in \mathbb{N}\right\}$ be a sequence of $(\Omega, \mathcal{F}, \mathbb{P})$-measurable random variables. For each $n \in \mathbb{N}$, let $\mathcal{F}_{n}=\sigma\left(X_{m}: m \leq n\right)$, and let $\mathcal{G}_{n}=\sigma\left(X_{m}: m \geq n\right)$. For $n \in \mathbb{N}$, let $\alpha_{X}(n)$ be Rosenblatt's $\alpha$-mixing coefficient,

$$
\alpha_{X}(n)=\sup _{m \in \mathbb{N}} \sup _{A \in \mathcal{F}_{m}, B \in \mathcal{G}_{m+n}}|\mathbb{P}(A \cap B)-\mathbb{P}(A) \mathbb{P}(B)|
$$

We say that the sequence $\left\{X_{n}\right\}$ is strongly mixing or $\alpha$-mixing if $\alpha_{X}(n) \rightarrow 0$ as $n \rightarrow \infty$.

For $n \in \mathbb{N}$, let $\beta_{X}(n)$ be the $\beta$-mixing or absolute regularity coefficient, defined as

$$
\beta_{X}(n)=\sup _{m \in \mathbb{N}} \mathbb{E}\left[\sup _{B \in \mathcal{G}_{m+n}}\left|\mathbb{P}\left(B \mid \mathcal{F}_{m}\right)-\mathbb{P}(B)\right|\right]
$$

We say that the sequence $\left\{X_{n}\right\}$ is absolutely regular or $\beta$-mixing if $\beta_{X}(n) \rightarrow 0$ as $n \rightarrow \infty$.

Remark 1.1. As discussed in Bradley (2005), we have that, for any sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ of $\mathbb{R}^{d}$-valued random variables, and for each $n \in \mathbb{N}$,

$$
2 \alpha_{X}(n) \leq \beta_{X}(n)
$$

It follows that any $\beta$-mixing sequence is also $\alpha$-mixing.

## 2 Defining monotone trend

We turn our attention to establishing the meaning of the expression "monotone trend" used in the remainder of this paper. In Mann (1945), it is the case that monotone trend is defined solely in contrast to the null of i.i.d., and is not explicitly defined in itself. However, appropriately defining this phrase, or, more pertinently, defining a lack of monotone trend, is essential in order to conduct a hypothesis test of a lack of monotone trend, since otherwise defining the null becomes impossible.

In this work, we restrict attention to consideration of weakly dependent sequences, as defined earlier. When considering the monotonicity (or lack thereof) of the sequence $\left\{X_{n}\right.$ : $n \in \mathbb{N}\}$, we provide some examples of the difficulties arising when using traditional notions of monotonicity, such as $\mathbb{E}\left[X_{i}\right]<\mathbb{E}\left[X_{j}\right]$ for $i<j$.

Example 2.1. (Positive local trend, negative global trend) Let $c, \epsilon>0$. Consider the sequence $\left\{Y_{n}: n \in \mathbb{N}\right\}$ such that $Y_{0}=0$, and, for all $n \geq 1$,

$$
Y_{n}=\sum_{i=1}^{n} X_{i}
$$

where the $X_{i}$ are i.i.d. such that

$$
X_{i}=\left\{\begin{array}{l}
1, \text { with probability } 1-\epsilon \\
-c, \text { with probability } \epsilon
\end{array}\right.
$$

Let $\delta>0$, and let $M \in \mathbb{N}$. By letting $\epsilon=(1-\delta)^{1 / M}$ and $c$ be sufficiently large, we have that $\left\{Y_{n}\right\}$ is a (strictly) decreasing sequence in expectation, and so this sequence exhibits a negative global monotone trend with probability 1 , since, by the strong law of large numbers,

$$
\frac{1}{n} Y_{n} \xrightarrow{\text { a.s. }} \mathbb{E}\left[X_{1}\right]<0,
$$

from which it follows that, for $i<j$, as $j-i \rightarrow \infty, \mathbb{P}\left(Y_{i}>Y_{j}\right) \rightarrow 1$, and in fact, for any constant $K \in \mathbb{R}^{+}, \mathbb{P}\left(Y_{i}>Y_{j}+K\right) \rightarrow 1$ as $j-i \rightarrow \infty$.



Figure 2.1: A sample path from the process described in Example 2.1, with $n=10^{5}, \epsilon=10^{-4}$, and $M=5 \cdot 10^{4}$.

However, such a sequence exhibits a local monotone trend in the opposite direction in the following sense: for any $n \in \mathbb{N}$, we have that

$$
\mathbb{P}\left(X_{n}<X_{n+1}<\cdots<X_{n+M-1}\right)=1-\delta
$$

To conclude, since it is possible to construct such a sequence for any choice of $\delta$ and $M$, we may construct a sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ with the following property: for any $i \in \mathbb{N}$, the sequence $\left(X_{i}, \ldots, X_{i+M-1}\right)$ is strictly increasing with probability $(1-\delta)$, but $X_{n} \rightarrow-\infty$ with probability 1 .

Example 2.1 indicates that some distinction is required between the notions of local and global monotone trend. In particular, as will be illustrated in Section 3, strictly stationary and weakly dependent (in particular, absolutely regular) sequences cannot, by definition, exhibit global trend, in the sense that, as $|j-i| \rightarrow \infty$,

$$
\mathbb{P}\left(X_{i} \leq X_{j}\right)-\mathbb{P}\left(X_{i} \geq X_{j}\right) \rightarrow 0
$$

On account of this property of strictly stationary and weakly dependent sequences, it follows
that any test of monotone trend in this context is, in fact, a test of stationarity, since one cannot disentangle the properties of stationarity and lack of monotone trend (see Remark 3.1). While there is an argument to be made that the restriction of stationarity is too strong in such a setting, this assumption is necessary to ensure some limiting behaviour of functions of the sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$; indeed, even without considering weakly dependent processes, there exist sequences of independent, uniformly bounded random variables for which, for example, the sample mean does not converge in distribution.

In light of this, we therefore consider a test of global monotone trend to test the null hypothesis

$$
H_{0}:\left\{X_{n}: n \in \mathbb{N}\right\} \text { is stationary, }
$$

where, for methods developed later in this paper, we consider the power of such tests against alternatives the form of which is explicitly specified.

Fortunately, the issue of appropriately defining the notion of local monotone trend is a simpler one; in particular, local monotonicity is a property which is not directly tied to the stationarity of a sequence. For a simple example of a sequence with no local monotone trend, consider $X_{n}$ being i.i.d. random variables drawn from a continuous distribution $F$. In this setting, which is the null setting of the original test of Mann (1945), any ordering of any local subsequence of this process $\left(X_{n}, \ldots, X_{n+M-1}\right)$ is equally likely, and any definition of local monotone trend should exclude this example from exhibiting such a trend. In contrast, a sequence for which it should be said that a local monotone trend exists is given in the example below.

Example 2.2. (Markov chain with local monotone trend) Let $M \in \mathbb{N}$, and let $\epsilon>0$. Let

$$
\pi_{-M}=\frac{\epsilon}{1-(1-\epsilon)^{2 M+1}}
$$

For each $i \in\{-M+1, \ldots, M\}$, let

$$
\pi_{i}=\pi_{-M} \cdot(1-\epsilon)^{i+M}
$$

Consider the Markov chain $\left\{X_{n}: n \in \mathbb{N}\right\}$ on the state space $\{-M, \ldots, M\}$ with initial distribution $\pi$, and transition matrix

$$
P_{i, j}= \begin{cases}1-\epsilon, & j=i+1 \text { and } i \leq M-1 \\ 1-\epsilon, & i=j=M \\ \epsilon, & j=-M\end{cases}
$$

This is an irreducible, aperiodic Markov chain on a finite state space with stationary distribution $\pi$. In particular, by the weak Markov property, this sequence is strictly stationary, and is absolutely regular, as a consequence of standard convergence results for irreducible, aperiodic Markov chains on a finite state space (see Freedman (2011)). A sample path from such a process is shown below.



Figure 2.2: A sample path from the process described in Example 2.2, with $n=10^{5}, \epsilon=10^{-4}$, and $M=10^{5}$.

For an appropriate choice of $\epsilon$ and $M$, this process exhibits the same local behaviour as the process in Example 2.1; namely, for any arbitrary run length $K \in \mathbb{N}$ and any arbitrarily small $\delta>0$, one can construct such a process for which, for any $n$,

$$
\mathbb{P}\left(X_{n}<X_{n+1}<\cdots<X_{n+K}\right) \geq(1-\delta)
$$

i.e. one may construct a sequence with arbitrarily strong local monotone trend.

In light of these examples, we proceed to define the null hypotheses of no global monotone trend and no local monotone trend. In order to test the hypothesis of no global monotone trend in the setting of weakly dependent sequences, we use the null hypothesis

$$
H_{0}^{(g)}:\left\{X_{n}\right\} \text { is strictly stationary. }
$$

In order to test the hypothesis of no local monotone trend of order $M$ in the setting of strictly stationary, weakly dependent sequences, we use the null hypothesis

$$
H_{0, M}^{(l)}: \frac{2}{(n-M) M} \sum_{i<j \leq i+M}\left(\mathbb{P}\left(X_{i}<X_{j}\right)-\mathbb{P}\left(X_{i}>X_{j}\right)\right)=0
$$

Of course, under strict stationarity, this is equivalent to the null hypothesis

$$
\tilde{H}_{0, M}^{(l)}: \sum_{i=2}^{M+1}\left(\mathbb{P}\left(X_{1}<X_{i}\right)-\mathbb{P}\left(X_{1}>X_{i}\right)\right)=0
$$

With these null hypotheses precisely defined, we may now begin construction of appropriate permutation testing procedures for both global and local monotone trend.

## 3 Testing for global trend

In this section, we consider the problem of testing the null hypothesis

$$
H_{0}^{(g)}:\left\{X_{i}: i \in[n]\right\} \text { is stationary }
$$

in the setting where the sequence $\left\{X_{i}: i \in[n]\right\}$ is absolutely regular. When the distribution of $\left(X_{1}, \ldots, X_{n}\right)$ is invariant under permutation, i.e. the sequence is exchangeable, the randomization hypothesis holds, and so one may construct permutation tests of the hypothesis $H_{0}^{(g)}$ with exact level $\alpha$. However, in the case of absolutely regular sequences, by Lemma S.3.1 in Romano and Tirlea (2022), exchangeability and i.i.d. are equivalent conditions. This implies that any permutation testing procedure will retain the property of exactness under the additional assumption that the $X_{i}$ are i.i.d., and this is the only condition under which the randomization hypothesis holds in this setting.

However, if the realizations of the sequence $\left\{X_{i}: i \in[n]\right\}$ are not independent or are not i.i.d., the test may not be valid even asymptotically, i.e. the rejection probability of a permutation test may not be equal to $\alpha$ or even close to $\alpha$ as $n \rightarrow \infty$. Our goal is therefore to construct a testing procedure which has asymptotic rejection probability equal to $\alpha$, but which also retains finite sample exactness under the additional assumption that the $X_{i}$ are i.i.d., and so appropriate consideration of the asymptotic properties of the permutation distribution and the test statistic must be undertaken. We wish to consider a permutation test based on the Mann-Kendall statistic, and so we may begin by defining the Mann-Kendall
statistic and analyzing the limiting behavior of the permutation distribution $\hat{R}_{n}$ based on this test statistic.

### 3.1 The global Mann-Kendall statistic

Definition 3.1. For $X_{1}, \ldots, X_{n}$ a sequence of random variables, let

$$
U_{n}=U_{n}\left(X_{1}, \ldots, X_{n}\right)=\left(\begin{array}{c}
n \\
2
\end{array}\right)^{-1} \sum_{i=1}^{n} \sum_{j=i}^{n}\left(I\left\{X_{j}>X_{i}\right\}-I\left\{X_{i}>X_{j}\right\}\right)
$$

be the (global) Mann-Kendall statistic.

Theorem 3.1. Let $\left\{X_{i}: i \in \mathbb{N}\right\}$ be a sequence of random variables such that, for all $i \neq j$, $\mathbb{P}\left(X_{i}=X_{j}\right)=0$.

Let $\hat{R}_{n}$ be the permutation distribution, based on the test statistic $\sqrt{n} U_{n}$, with associated group of transformations $S_{n}$, the symmetric group of order $n$. We have that, as $n \rightarrow \infty$,

$$
\sup _{t \in \mathbb{R}}\left|\hat{R}_{n}(t)-\Phi(3 t / 2)\right|
$$

where $\Phi$ is the standard Gaussian c.d.f.

Proof. Let $\Pi_{n} \sim \operatorname{Unif}\left(S_{n}\right)$, independent of $\left\{X_{i}, i \in[n]\right\}$. Let

$$
U_{\Pi_{n}}=U_{n}\left(X_{\Pi_{n}(1)}, \ldots, X_{\Pi_{n}(n)}\right)
$$

Conditional on the sequence $\left\{X_{i}, i \in[n]\right\}$, we observe that, on account of the lack of ties, we have that each ordering of the $X_{\Pi_{n}(i)}$ is equally likely. Since the distribution of $U_{n}$ only depends on the ranks of the sequence $\left\{X_{i}: i \in[n]\right\}$, the result follows by Mann (1945).

We observe that, other than the assumption of no ties among the $\left\{X_{i}\right\}$, no other conditions are required for the result of Theorem 3.1. This occurs since $U_{n}$ is a rank statistic, and, under the action of a random permutation $\Pi_{n}$, the ranks of the $\left\{X_{i}\right\}$ are uniformly distributed over the set of permutations $S_{n}$, and so the permutation distribution $\hat{R}_{n}$ is exactly equal to the distribution of $U_{n}$ under the when the $X_{i}$ are independent and identically distributed.

In order to appropriately assess the asymptotic validity of the permutation test based on this statistic, we must turn our attention to determining the asymptotic distribution of $U_{n}$.

### 3.2 Asymptotic distribution of the Mann-Kendall statistic

Having determined the limiting behavior of the permutation distribution based on $U_{n}$, we now consider the true unconditional limiting distribution of the test statistic, since consistency
would require these limiting distributions be the same. Due to allowing quite general forms of weak dependence, the asymptotic distribution of the test statistic presents more of a challenge. We proceed as follows: although $U_{n}$ is not a U-statistic, since the corresponding kernel $h$ is antisymmetric, we may apply the same idea behind the projection method used to find the asymptotic distribution of U-statistics as in the original proof due to Hoeffding (1948), i.e. we linearize the statistic $U_{n}$. Note, however, the linearization is not based on the true "projection" based on conditional expectations, but rather based on a "pseudo-projection", which assumes the observations are i.i.d. In order to perform this linearization, we require the following definition, as well as the subsequent lemma.

Definition 3.2. For $\left\{i_{j}: j \in[k]\right\} \subset \mathbb{N}$, let $\left\{X_{i_{j}}: j \in[k]\right\}$ be a sequence of random variables. For each $j \in\{1, \ldots, k-1\}$, let $\mathbb{P}_{j}^{(k)}$ be the probability measure defined by

$$
\mathbb{P}_{j}^{(k)}\left(E^{(j)} \times E^{(k-j)}\right)=\mathbb{P}\left(\left(X_{i_{1}}, \ldots, X_{i_{j}}\right) \in E^{(j)}\right) \mathbb{P}\left(\left(X_{i_{j+1}}, \ldots, X_{i_{k}}\right) \in E^{(k-j)}\right)
$$

where $E^{(j)}$ and $E^{(k-j)}$ are Borel sets in $\mathbb{R}^{j}$ and $\mathbb{R}^{k-j}$, respectively. Also, let $\mathbb{P}_{0}^{k}$ be the probability measure defined by

$$
\mathbb{P}_{0}^{k}\left(E^{(k)}\right)=\mathbb{P}\left(\left(X_{i_{1}}, \ldots, X_{i_{k}}\right) \in E^{(k)}\right)
$$

where $E^{(k)}$ is a Borel set in $\mathbb{R}^{k}$.

Lemma 3.1. Let $h: \mathbb{R}^{k} \rightarrow \mathbb{R}$ be a Borel function such that $|h| \leq M$, for some $M \in \mathbb{R}^{+}$. Then

$$
\left|\int_{\mathbb{R}^{k}} h\left(x_{1}, \ldots, x_{k}\right) \mathrm{d} \mathbb{P}_{0}^{(k)}-\int_{\mathbb{R}^{k}} h\left(x_{1}, \ldots, x_{k}\right) \mathrm{d} \mathbb{P}_{j}^{(k)}\right| \leq 2 M \beta_{X}\left(i_{j+1}-i_{j}\right)
$$

Proof. Let $\nu$ be the signed measure $\mathbb{P}_{0}^{(k)}-\mathbb{P}_{j}^{(k)}$, and let $|\nu|$ denote its corresponding total variation measure. We have that

$$
\begin{aligned}
\left|\int_{\mathbb{R}^{k}} h\left(x_{1}, \ldots, x_{k}\right) \mathrm{d} \mathbb{P}_{0}^{(k)}-\int_{\mathbb{R}^{k}} h\left(x_{1}, \ldots, x_{k}\right) \mathrm{d} \mathbb{P}_{j}^{(k)}\right| & =\left|\int_{\mathbb{R}^{k}} h\left(x_{1}, \ldots, x_{k}\right) \mathrm{d} \nu\right| \\
& \leq \int_{\mathbb{R}^{k}}\left|h\left(x_{1}, \ldots, x_{k}\right)\right| \mathrm{d}|\nu| \\
& \leq 2 M \cdot \mathrm{TV}\left(\mathbb{P}_{0}^{(k)}, \mathbb{P}_{j}^{(k)}\right) \\
& =2 M \beta_{X}\left(i_{j+1}-i_{j}\right)
\end{aligned}
$$

where TV denotes total variation distance, and the final equality follows by Volkonskii and Rozanov (1961).

We utilize this lemma as follows. Let $F$ be the marginal distribution of the $X_{i}$. In essence, we may not perform a true linearization, since, for $i \neq j$, the conditional expectation $\mathbb{P}\left(X_{i} \leq X_{j} \mid X_{j}\right)$ is not equal to $F\left(X_{j}\right)$, since the $X_{i}$ need not be independent. In spite of this, Lemma 3.1 provides an upper bound on the difference between the true projection

$$
\mathbb{P}\left(X_{i} \leq X_{j} \mid X_{j}\right)
$$

and the approximate projection $F\left(X_{j}\right)$, in terms of the $\beta$-mixing coefficients of the sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$. By requiring appropriate $\beta$-mixing conditions on the sequence $\left\{X_{i}\right\}$, we may bound the error term of this approximate linearization, and, using the central limit theorem due to Neumann (2013), we may conclude the following result.

Theorem 3.2. Let $\left\{X_{n}: n \in \mathbb{N}\right\}$ be a strictly stationary, absolutely regular sequence of realvalued random variables with marginal distribution $F$, such that, for all $i \neq j, \mathbb{P}\left(X_{i}=X_{j}\right)=0$. Suppose that the $\beta$-mixing coefficients of $\left\{X_{n}\right\}$ satisfy

$$
\sum_{n=1}^{\infty} \beta_{X}(n)<\infty
$$

For each $i \in[n]$, let $V_{i}=1-2 F\left(X_{i}\right)$. Let

$$
\sigma^{2}=\frac{4}{9}+\frac{8}{3} \sum_{k \geq 1} \operatorname{Cov}\left(V_{1}, V_{1+k}\right)
$$

Suppose that $\sigma^{2}>0$. As $n \rightarrow \infty$,

$$
\sqrt{n} U_{n} \xrightarrow{d} N\left(0, \sigma^{2}\right) .
$$

Remark 3.1. Note that, as a consequence of the proof of Theorem 3.2, we have that

$$
\mathbb{E}\left[\sqrt{n} U_{n}\right]=o(1)
$$

i.e. for any stationary, absolutely regular sequence satisfying the conditions laid out therein, the limiting mean of the test statistic is 0 . In particular, this motivates our choice of null hypothesis $H_{0}^{(g)}$, since this will be the case for any stationary sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ satisfying the requisite mixing conditions.

Remark 3.2. Since, for any sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$, we have that, for all $n$,

$$
\beta_{X}(n) \geq 2 \alpha_{X}(n)
$$

it follows that the condition (3.1) implies that

$$
\sum_{n \geq 1} \alpha_{X}(n)<\infty
$$

This condition is sufficient for Theorem 2.1 of Neumann (2013) to be applied in the above proof. It also follows that

$$
\sum_{k=1}^{\infty} \beta_{X}(k)<\infty \Longrightarrow \sum_{k=1}^{n} k \beta_{X}(k)=o(n)
$$

a proof of which is as follows. For $(k, l) \in \mathbb{N} \times(\mathbb{N} \cup\{\infty\})$ such that $k \leq l$, let

$$
S_{k, l}=\sum_{i=k}^{l} \beta_{X}(i)
$$

Let $\epsilon>0$. Without loss of generality, we may assume that $\epsilon<S_{1, \infty}$. There exists $N \in \mathbb{N}$ such that, for all $k \geq N$,

$$
S_{k, \infty}<\epsilon
$$

We have that, for $n \geq N$,

$$
\begin{aligned}
\sum_{k=1}^{n} k \beta_{X}(k) & =\sum_{k=1}^{n} S_{k, n} \\
& =\sum_{k=1}^{N-1} S_{k, n}+\sum_{k=N}^{n} S_{k, N} \\
& \leq(N-1) S_{1, \infty}+(n-N+1) \epsilon \\
& \leq 2 n \epsilon
\end{aligned}
$$

for all $n \geq N S_{1, \infty} / \epsilon$.

However, due to the above two implications, it may be seen that the condition (3.1) may be replaced with the weaker conditions

$$
\begin{gathered}
\sum_{k=1}^{\infty} \alpha_{X}(k)<\infty \\
\sum_{k=1}^{n} k \beta_{X}(k)=o(n)
\end{gathered}
$$

without affecting the result of Theorem 3.2.

Remark 3.3. The proof of Theorem 3.2 follows the same structure as the original proof of the limiting distribution of U-statistics found in Hoeffding (1948). The statistic in question is
split into a linearized term, formed by conditioning on one of the entries in the kernel $h$, and a remainder term. It is then shown that the remainder term converges to 0 in probability, and that the linearized term satisfies a central limit theorem.

There are two immediate issues with this approach in the case of the Mann-Kendall statistic for dependent data: firstly, the kernel $h$ is antisymmetric, hence the order of projection becomes relevant to the resulting linearized term. In the case of independent, but not necessarily i.i.d. random variables, this has been previously considered in Han and Qian (2018), with an application to the Mann-Kendall statistic.

The second, and more challenging, issue is that, in the case of dependent data, the conditional expectation

$$
\mathbb{E}\left[h\left(X_{i}, X_{j}\right) \mid X_{j}\right]
$$

depends not only on $X_{j}$, but also on the conditional distribution of $X_{i}$ given $X_{j}$. In particular, in the case of a strictly stationary sequence, (3.4) depends on both $X_{j}$ and $j-i$. This suggests that a true projection, formed by conditioning on the variables $\left\{X_{i}\right\}$, will not lead to a sum of $n$ random variables which is more amenable to the application of a central limit theorem.

However, as the proof of Theorem 3.2 demonstrates, one may take the approach of pseudoprojection: namely, we may rewrite the full statistic as a sum of linear terms which would be obtained by projection if the data were i.i.d., in addition to a remainder term. Heuristically, the reasoning behind this approach is as follows. By Lemma 3.1, the difference between the true projection and pseudo-projection for any given term in the Mann-Kendall statistic is

$$
\mathbb{E}\left[\left|\left(1-2 F\left(X_{j}\right)\right)-\mathbb{E}\left[h\left(X_{i}, X_{j}\right) \mid X_{j}\right]\right|\right]=O\left(\beta_{X}(j-i)\right)
$$

By Markov's inequality, the sum of the differences is therefore "small in probability" under the given conditions, and so a CLT may be applied to the sum of pseudo-projections without penalty.

While we have shown that a central limit theorem holds for the statistic $U_{n}$, we observe, that, in general, the limiting variance (3.2) of the global Mann-Kendall statistic is not, in general, equal to the limiting variance of the permutation distribution, as found in Theorem 3.1. In particular, this implies that a permutation test based on this statistic does not control the probability of a Type 1 error, even asymptotically. We therefore turn our attention to studentization, i.e. we wish to find an appropriate estimator of the variance (3.2). To this end, we provide the following theorem.

Theorem 3.3. Let $\left\{X_{n}: n \in \mathbb{N}\right\}$ be a sequence of random variables satisfying the conditions in Theorem 3.2. Let $\hat{F}_{n}$ be the empirical distribution of $\left\{X_{n}: n \in \mathbb{N}\right\}$. Let $\left\{b_{n}: n \in \mathbb{N}\right\} \subset \mathbb{N}$ be a sequence such that $b_{n}<n$ for all $n, b_{n}=o(\sqrt{n})$, and, as $n \rightarrow \infty, b_{n} \rightarrow \infty$. Let

$$
\hat{\sigma}_{n}^{2}=\frac{4}{9}+\frac{8}{3 n} \sum_{k=1}^{b_{n}} \sum_{j=1}^{n-k}\left(1-2 \hat{F}_{n}\left(X_{j}\right)\right)\left(1-2 \hat{F}_{n}\left(X_{j+k}\right)\right)
$$

Let $\sigma^{2}$ be as in Theorem 3.2. Then, as $n \rightarrow \infty$,

$$
\hat{\sigma}_{n}^{2} \xrightarrow{p} \sigma^{2} .
$$

Having constructed a consistent estimator of the variance, we may now studentize to obtain the following result.

Theorem 3.4. Let $\left\{X_{n}: n \in \mathbb{N}\right\}$ be a strictly stationary, absolutely regular sequence of random variables, with marginal distribution $F$, such that, for all $i \neq j, \mathbb{P}\left(X_{i}=X_{j}\right)=0$. Suppose that the $\beta$-mixing coefficients of $\left\{X_{n}\right\}$ satisfy

$$
\sum_{n=1}^{\infty} \beta_{X}(n)<\infty
$$

For each $i \in \mathbb{N}$, let $V_{i}=1-2 F\left(X_{i}\right)$. Let $\sigma^{2}$ be as in (3.2), and suppose that $\sigma^{2}>0$. Let $\left\{b_{n}: n \in \mathbb{N}\right\} \subset \mathbb{N}$ be a sequence such that $b_{n}<n$ for all $n, b_{n}=o(\sqrt{n})$, and, as $n \rightarrow \infty$, $b_{n} \rightarrow \infty$. Let

$$
\hat{\sigma}_{n}^{2}=\frac{4}{9}+\frac{8}{3 n} \sum_{k=1}^{b_{n}} \sum_{j=1}^{n-k}\left(1-2 \hat{F}_{n}\left(X_{j}\right)\right)\left(1-2 \hat{F}_{n}\left(X_{j+k}\right)\right)
$$

The following results hold.

(i) As $n \rightarrow \infty$,

$$
\frac{\sqrt{n} U_{n}}{\hat{\sigma}_{n}} \xrightarrow{d} N(0,1)
$$

(ii) Let $\hat{R}_{n}$ be the permutation distribution, with associated group of transformations $S_{n}$, the symmetric group of order $n$, based on the test statistic $\sqrt{n} U_{n} / \hat{\sigma}_{n}$. Then, as $n \rightarrow \infty$,

$$
\sup _{t \in \mathbb{R}}\left|\hat{R}_{n}(t)-\Phi(t)\right| \xrightarrow{\text { a.s. }} 0
$$

where $\Phi$ is the standard Gaussian c.d.f.

Proof. The result of (i) follows immediately from Theorem 3.2, Theorem 3.3, and Slutsky's theorem. We turn our attention to (ii).

Let $\Pi_{n}, \Pi_{n}^{\prime} \sim \operatorname{Unif}\left(S_{n}\right)$, with $\Pi_{n}, \Pi_{n}^{\prime}$, and $\left(X_{1}, \ldots, X_{n}\right)$ independent, and let $\mathbf{X}_{\Pi_{n}}, \mathbf{X}_{\Pi_{n}^{\prime}}$ denote the action of $\Pi_{n}$ and $\Pi_{n}^{\prime}$ on $\left(X_{1}, \ldots, X_{n}\right)$, respectively. Since $F$ is continuous, the ranks of the sequences $\mathbf{X}_{\Pi_{n}}$ and $\mathbf{X}_{\Pi_{n}^{\prime}}$ are uniformly distributed over the set of permutations of $[n]$ with probability 1. Also, since $\Pi_{n}$ and $\Pi_{n}^{\prime}$ are independent, the ranks of $\mathbf{X}_{\Pi_{n}}$ and $\mathbf{X}_{\Pi_{n}^{\prime}}$ are independent. Furthermore, note that, for each $i \in[n]$,

$$
\hat{F}_{\Pi_{n}}\left(X_{\Pi_{n}(i)}\right)=\frac{1}{n} r\left(X_{\Pi_{n}(i)}\right)
$$

for $r\left(X_{\Pi_{n}(i)}\right)$ the rank of $X_{\Pi_{n}(i)}$, i.e. $\hat{\sigma}_{\Pi_{n}}$ is also a rank statistic. In particular, it follows that, for

$$
U_{\Pi_{n}}=U_{n}\left(\mathbf{X}_{\Pi_{n}}\right)
$$

and for $U_{\Pi_{n}^{\prime}}$ defined analogously, $U_{\Pi_{n}} / \hat{\sigma}_{\Pi_{n}}$ and $U_{\Pi_{n}^{\prime}} / \hat{\sigma}_{\Pi_{n}^{\prime}}$ are i.i.d. random variables, each having the same distribution as

$$
\frac{U_{n}\left(\tilde{X}_{1}, \ldots, \tilde{X}_{n}\right)}{\hat{\sigma}_{n}\left(\tilde{X}_{1}, \ldots, \tilde{X}_{n}\right)}
$$

where $\left\{\tilde{X}_{i}: i \in[n]\right\}$ is a sequence of i.i.d. random variables, each having the marginal distribution $F$. It follows that, by (i), as $n \rightarrow \infty$,

$$
\left(\frac{\sqrt{n} U_{\Pi_{n}}}{\hat{\sigma}_{\Pi_{n}}}, \frac{\sqrt{n} U_{\Pi_{n}^{\prime}}}{\hat{\sigma}_{\Pi_{n}^{\prime}}}\right) \xrightarrow{d} N\left(0, I_{2}\right)
$$

where $I_{2}$ is the $2 \times 2$ identity matrix. Therefore, by Theorem 15.2 .3 of Lehmann and Romano (2022), the result of (ii) follows.

Remark 3.4. As a consequence of Theorem 3.4, a two-sided permutation test of the null hypothesis

$$
H_{0}^{(g)}:\left\{X_{n}: n \in \mathbb{N}\right\} \text { is stationary }
$$

which rejects for large values of $\sqrt{n} U_{n} / \hat{\sigma}_{n}$, is asymptotically valid under the stated conditions.

Remark 3.5. Since $\sqrt{n} U_{n} / \hat{\sigma}_{n}$ is a rank statistic, it follows that the permutation distribution $\hat{R}_{n}$ has no dependence on the underlying distribution of the $X_{i}$, as long as the marginal distribution $F$ is continuous. In particular, it follows that $\hat{R}_{n}$ retains a convenient property of the original null distribution of the Mann-Kendall test: namely, for a fixed choice of $n$
and the truncation parameter $b_{n}$ of the studentization factor, the permutation distribution is fixed, and so may be computed in advance and tabulated.

Having shown the asymptotic validity of the permutation test based on the studentized global Mann-Kendall statistic, we turn our attention to finding the local limiting power function of this test.

Theorem 3.5. Let $\left\{X_{i}: i \in[n]\right\}$ be a sequence of random variables satisfying the conditions of Theorem 3.2. Suppose further that $F$ is twice differentiable, with density $f$ with respect to Lebesgue measure, such that $f$ has uniformly bounded first derivative $f^{\prime}$, which is measurable (with respect to Lebesgue measure). Let $\left\{\mu_{n, i}: i \in[n]\right\} \subset \mathbb{R}$ be such that, as $n \rightarrow \infty$,

$$
\frac{1}{\sqrt{n}} \sum_{i=1}^{n} \mu_{n, i}^{2} \rightarrow 0
$$

Let

$$
\nu_{n}=\frac{1}{\sqrt{n}} \sum_{i=1}^{n} \frac{n+1-2 i}{n-1} \mu_{n, i}
$$

For each $i \in[n]$, let

$$
Y_{n, i}=X_{i}+\mu_{n, i}
$$

Let $\mathbb{P}_{n}, \mathbb{Q}_{n}$ be the measures such that, for $A \in \mathcal{B}\left(\mathbb{R}^{n}\right)$,

$$
\begin{aligned}
& \mathbb{P}_{n}(A)=\mathbb{P}\left(\left(X_{1}, \ldots, X_{n}\right) \in A\right) \\
& \mathbb{Q}_{n}(A)=\mathbb{P}\left(\left(Y_{n, 1}, \ldots, Y_{n, n}\right) \in A\right)
\end{aligned}
$$

Suppose that $\left\{\mathbb{Q}_{n}: n \in \mathbb{N}\right\}$ is contiguous to $\left\{\mathbb{P}_{n}: n \in \mathbb{N}\right\}$. Then, under $\mathbb{Q}_{n}$, as $n \rightarrow \infty$,

$$
\sqrt{n} U_{n}+\nu_{n} \xrightarrow{d} N\left(0, \sigma^{2}\right)
$$

where $\sigma^{2}$ is as defined in Theorem 3.2.

Remark 3.6. Note that the condition on $f^{\prime}$ implies that $f$ is uniformly bounded. Indeed, suppose the contrary. Let $\left\|f^{\prime}\right\|_{\infty}=k<\infty$. Then, for $N>\sqrt{\frac{1}{2 k}}$, for $x$ such that $f(x) \geq N+1$,

$$
\begin{aligned}
\int_{x}^{x+2 / N} f(t) \mathrm{d} t & \geq \int_{x}^{x+2 / N}(f(x)-k t) \mathrm{d} t \\
& =\frac{2 f(x)}{N}-k \cdot \frac{2}{N^{2}} \\
& >2+\frac{2}{N}-1 \\
& >1
\end{aligned}
$$

i.e. we have obtained a contradiction. Note also that this implies that the random variable $f\left(X_{1}\right)$ is bounded, and so, in particular, has finite moments of every order.

Corollary 3.1. Under the conditions of Theorem 3.5, for $\hat{\sigma}_{n}^{2}$ as defined in Theorem 3.3, we have that, under $\mathbb{Q}_{n}$,

$$
\frac{\sqrt{n} U_{n}+\nu_{n}}{\hat{\sigma}_{n}} \xrightarrow{d} N(0,1)
$$

Proof. The result follows immediately from Theorem 3.5, Theorem 3.3, the definition of contiguity, and Slutsky's theorem.

Remark 3.7. By Corollary 3.1, it follows that, as long as $\nu_{n} \rightarrow \nu \in[-\infty, \infty]$, for $\phi_{n}=$ $\phi_{n}\left(Y_{1}, \ldots, Y_{n}\right)$ the test function corresponding to the level $\alpha$ permutation test outlined in Theorem 3.4, the limiting power against the sequence of measures $\mathbb{Q}_{n}$ is given by

$$
\mathbb{E}_{\mathbb{Q}_{n}}\left[\phi_{n}\left(Y_{1}, \ldots, Y_{n}\right)\right] \rightarrow 1-\Phi\left(z_{1-\alpha}+\frac{\nu}{\sigma}\right)
$$


of the standard Gaussian distribution.

Example 3.1. (White noise process) Let $\left\{X_{n}: n \in \mathbb{N}\right\}$ be a standard Gaussian white noise process, i.e. $X_{n} \sim N(0,1)$. Let $h>0$. For each $n \in \mathbb{N}$, for each $i \in[n]$, let

$$
Y_{n, i}=X_{i}+\frac{h i}{n^{3 / 2}}
$$

i.e. in the setting of Theorem 3.5, we take

$$
\mu_{n, i}=\frac{h i}{n^{3 / 2}}
$$

Let $\mathbb{P}_{n}$ and $\mathbb{Q}_{n}$ be as in Theorem 3.5. We begin by showing that $\left\{\mathbb{Q}_{n}\right\}$ is contiguous to $\left\{\mathbb{P}_{n}\right\}$. We have that the log-likelihood ratio is given by

$$
\log L_{n}=-\frac{h^{2}}{2 n^{3}} \sum_{i=1}^{n} i^{2}+\frac{h}{n^{3 / 2}} \sum_{i=1}^{n} i X_{i}
$$

Let

$$
\mu_{n}=\frac{h^{2}}{6 n^{3}} n(n+1)(2 n+1)
$$

We have that

$$
\log L_{n} \sim N\left(-\frac{1}{2} \mu_{n}, \mu_{n}^{2}\right)
$$

and so, by Corollary 12.3 .1 of Lehmann and Romano (2022), $\left\{\mathbb{Q}_{n}\right\}$ and $\left\{\mathbb{P}_{n}\right\}$ are mutually contiguous. Also,

$$
\begin{aligned}
\frac{1}{\sqrt{n}} \sum_{i=1}^{n}\left(\frac{h i}{n^{3 / 2}}\right)^{2} & =\frac{h^{2}}{n^{7 / 2}} \sum_{i=1}^{n} i^{2} \\
& =\frac{h^{2} n(n+1)(2 n+1)}{n^{7 / 2}} \\
& =o(1)
\end{aligned}
$$

We may therefore apply Theorem 3.5, and so

$$
\sqrt{n} U_{n}+\nu_{n} \xrightarrow{d} N\left(0, \frac{4}{9}\right)
$$

By Remark 3.7, in order to compute the limiting power of the one-sided level $\alpha$ permutation test, it remains to compute the limit of the sequence $\left\{\nu_{n}\right\}$. We have that, as $n \rightarrow \infty$,

$$
\begin{aligned}
\frac{1}{\sqrt{n}} \sum_{i=1}^{n} \frac{n+1-2 i}{n-1} \cdot \frac{h i}{n^{3 / 2}} & =-\frac{h(n+1)}{6 n} \\
& \rightarrow-\frac{h}{6}
\end{aligned}
$$

Therefore the local limiting power function of the permutation test is given by

$$
\mathbb{E}_{\mathbb{Q}_{n}}\left[\phi_{n}\right] \rightarrow 1-\Phi\left(z_{1-\alpha}-\frac{h}{4}\right)
$$

where $\Phi$ is the standard Gaussian c.d.f.

Example 3.2. (AR(1) process) For $n \geq 1$, let $\left\{X_{n}: n \in \mathbb{Z}\right\}$ satisfy the equation, for $\rho \in \mathbb{R}$ such that $|\rho|<1$,

$$
X_{n+1}=\rho X_{n}+\epsilon_{n+1}
$$

where the $\epsilon_{k}$ are independent and identically distributed, with $\mathbb{E}\left[\epsilon_{k}\right]=0, \mathbb{E}\left[\epsilon_{k}^{2}\right]=1$, and, for some $\delta>0$,

$$
\mathbb{E}\left[\left|\epsilon_{k}\right|^{2+\delta}\right]<\infty
$$

i.e. $X$ is an $A R(1)$ process. Since $|\rho|<1$, there exists a unique stationary solution to (3.8). By Mokkadem (1988), Theorem 1, if the distribution of the $\epsilon_{k}$ is absolutely continuous with respect to Lebesgue measure, the conditions of Theorem 3.4 are satisfied. Therefore, asymptotically, the rejection probability of the permutation test applied to such a sequence will be equal to the nominal level $\alpha$.

Now, consider the triangular array of sequences given by, for $i \in[n]$,

$$
Y_{n, i}=X_{i}+\mu_{n, i}
$$

where

$$
\mu_{n, i}=\frac{h i}{n^{3 / 2}}
$$

Let $\mathbb{P}_{n}$ and $\mathbb{Q}_{n}$ be as in Theorem 3.5. We begin by showing that $\left\{\mathbb{Q}_{n}\right\}$ is contiguous to $\left\{\mathbb{P}_{n}\right\}$. We have that the log-likelihood ratio is given by

$$
\begin{aligned}
\log L_{n} & =-\frac{1}{2\left(1-\rho^{2}\right)} \sum_{i=1}^{n} \mu_{n, i}^{2}+\frac{1}{\left(1-\rho^{2}\right)} \sum_{i=1}^{n} \mu_{n, i}\left(X_{i}-\rho X_{i-1}\right) \\
& =-\frac{1}{2\left(1-\rho^{2}\right)} \sum_{i=1}^{n} \mu_{n, i}^{2}+\frac{1}{\left(1-\rho^{2}\right)} \sum_{i=1}^{n} \mu_{n, i} \epsilon_{i}
\end{aligned}
$$

Let $\mu_{n}$ be as in (3.7). We have that

$$
\begin{aligned}
\operatorname{Var}\left(\sum_{i=1}^{n} \mu_{n, i} \epsilon_{i}\right) & =\mu_{n}^{2} \\
& =\frac{h^{2}}{3}(1+o(1))
\end{aligned}
$$

Also, by an integral approximation,

$$
\begin{aligned}
\sum_{i=1}^{n} \mathbb{E}\left[\left|\mu_{n, i} \epsilon_{i}\right|^{2+\delta}\right] & =\mathbb{E}\left[\left|\epsilon_{1}\right|^{2+\delta}\right] \cdot \frac{h^{2+\delta}}{3 n^{3(2+\delta) / 2}} \sum_{i=1}^{n} i^{2+\delta} \\
& =\mathbb{E}\left[\left|\epsilon_{1}\right|^{2+\delta}\right] \cdot \frac{h^{2+\delta} \cdot n^{3+\delta}}{3 n^{3+3 \delta / 2}} \cdot \frac{1}{3+\delta}(1+o(1)) \\
& =o(1)
\end{aligned}
$$

In particular, it follows that the triangular array

$$
Z_{n, i}=\mu_{n, i} \epsilon_{i}
$$

satisfies the Lyapunov condition, and so, by the Lyapunov central limit theorem and Slutsky's theorem,

$$
\log L_{n} \xrightarrow{d} N\left(-\frac{h^{2}}{6}, \frac{h^{2}}{3}\right)
$$

Therefore, by Corollary 12.3 .1 of Lehmann and Romano (2022), $\left\{\mathbb{Q}_{n}\right\}$ and $\left\{\mathbb{P}_{n}\right\}$ are mutually contiguous. Hence, by the same argument as in Example 3.1, as long as the marginal
distribution of the $X_{i}$ satisfies the conditions of Theorem 3.5, the local limiting power of the one-sided level $\alpha$ permutation test is given by

$$
\mathbb{E}_{\mathbb{Q}_{n}}\left[\phi_{n}\right] \rightarrow 1-\Phi\left(z_{1-\alpha}-\frac{h}{6 \sigma}\right)
$$

where $\sigma$ is as in (3.2).

## 4 Tests of local trend

In this section, we discuss the problem of conducting a hypothesis test of local trend, i.e. of testing the null hypothesis, for a stationary sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ and some $M \in \mathbb{N}$,

$$
H_{0, M}^{(l)}: \frac{1}{(n-M) M} \sum_{i=1}^{n-M} \sum_{j=i+1}^{i+M}\left(\mathbb{P}\left(X_{i}<X_{j}\right)-\mathbb{P}\left(X_{i}>X_{j}\right)\right)=0
$$

Note that, if $H_{0, M}^{(l)}$ holds for all $M \in \mathbb{N}$, we have that, for all $i \neq j$,

$$
\mathbb{P}\left(X_{i}<X_{j}\right)=\mathbb{P}\left(X_{i}>X_{j}\right)
$$

i.e. the intersection of this countable family of null hypotheses results in a stronger condition on the sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ than $H_{0}^{(g)}$.

In order to construct an appropriate permutation test of $H_{0, M}^{(l)}$, we begin by defining a family of statistics, which we term the local Mann-Kendall statistics.

### 4.1 The local Mann-Kendall statistic

Definition 4.1. Let $n \in \mathbb{N}$, and let $\left\{X_{i}: i \in[n]\right\}$ be a sequence of random variables. Let $g(n) \in[n-1]$. Let

$$
V_{n}=V_{n}\left(X_{1}, \ldots, X_{n}\right)=\frac{1}{n g(n)} \sum_{i=1}^{n-g(n)} \sum_{j=i+1}^{i+g(n)}\left(I\left\{X_{i}<X_{j}\right\}-I\left\{X_{i}>X_{j}\right\}\right)
$$

be the local Mann-Kendall statistic of order $g(n)$.

Remark 4.1. A heuristic interpretation of the parameter $g(n)$ is that it functions as a choice of local bandwidth, i.e. a choice of larger values of $g(n)$ will increase the consideration of the ordering of values of the $X_{i}$ that are further apart in time.

While one may define the local Mann-Kendall statistic of order $g(n)$ for any value of $g(n)$ less than $(n-1)$, its primary use throughout this section will be to test hypotheses of a
lack of local monotone trend. In general, the two choices of $g: \mathbb{N} \rightarrow \mathbb{N}$ under consideration throughout the remainder of this section will be either $g(n)=M$ for all $n \in \mathbb{N}$, or $g$ being a nondecreasing function of $n$ such that $g(n) / n \rightarrow 0$ as $n \rightarrow \infty$.

With the definition of the local Mann-Kendall statistic in hand, we may begin consideration of a permutation test based on $V_{n}$. Under the additional assumption that the sequence $\left\{X_{i}: i \in[n]\right\}$ is i.i.d., the randomization hypothesis holds, and so the permutation test based on any test statistic will be exact in finite samples at the nominal level $\alpha$. However, in a weakly dependent setting, the randomization hypothesis does not hold, and so the permutation test based on may not be exact in finite samples or even asymptotically valid. In order to commence appropriately assessment of the validity of such a test, we provide the following result, which describes the limiting permutation distribution based on the test statistic $\sqrt{n g(n)} V_{n}$.

Theorem 4.1. Let $\left\{X_{i}: i \in \mathbb{N}\right\}$ be a sequence of random variables such that, for all $i \neq j$, $\mathbb{P}\left(X_{i}=X_{j}\right)=0$. Let $g: \mathbb{N} \rightarrow \mathbb{N}$ be such that $g(n)=o\left(n^{1 / 7}\right)$.

Let $\hat{R}_{n}$ be the permutation distribution, based on the test statistic $\sqrt{n g(n)} V_{n}$, with associated group of transformations $S_{n}$, the symmetric group of order $n$. For each $t \in \mathbb{R}$, we have that, as $n \rightarrow \infty$,

$$
\sup _{t \in \mathbb{R}}\left|\hat{R}_{n}(t)-\Phi(t \sqrt{3})\right| \rightarrow 0
$$

where $\Phi$ is the distribution of a standard Gaussian random variable.

Example 4.1. $(M A(2), g(n) \equiv 1)$ Consider the setting in which $g(n)=1$ for all $n \in \mathbb{N}$, and, for all $i$,

$$
X_{i}=\phi_{0} \epsilon_{i}+\phi_{1} \epsilon_{i-1}
$$

where the $\epsilon_{i}$ are i.i.d. random variables with a symmetric continuous distribution $F$. We have that

$$
V_{n}=\frac{1}{n} \sum_{i=1}^{n-1}\left(I\left\{X_{i+1}>X_{i}\right\}-I\left\{X_{i+1}<X_{i}\right\}\right)
$$

Let

$$
\begin{aligned}
& p_{1}=\mathbb{P}\left(X_{3}>X_{2}>X_{1}\right) \\
& p_{2}=\mathbb{P}\left(X_{3}<X_{2}<X_{1}\right)
\end{aligned}
$$

and let $r=2\left(p_{1}+p_{2}\right)-1$. We have that

$$
\begin{aligned}
& \operatorname{Var}\left(V_{n}\right) \\
& =\frac{1}{n^{2}}\left(n-1+2 \sum_{i=1}^{n-2} \operatorname{Cov}\left(I\left\{X_{i+2}>X_{i+1}\right\}-I\left\{X_{i+2}<X_{i+1}\right\}, I\left\{X_{i+1}>X_{i}\right\}-I\left\{X_{i+1}<X_{i}\right\}\right)\right) \\
& =\frac{1}{n^{2}}(n-1+2 r(n-2)) \\
& =\frac{1+2 r}{n}+o\left(\frac{1}{n}\right)
\end{aligned}
$$

It follows that the limiting variance of $\sqrt{n g(n)} V_{n}$ is given by

$$
\lim _{n \rightarrow \infty} \operatorname{Var}\left(\sqrt{n g(n)} V_{n}\right)=1+2 r
$$

In the setting in which the $X_{i}$ are i.i.d. with marginal distribution $F$, we have that $p_{1}=$ $p_{2}=1 / 6$, and so $r=-1 / 3$. However, since $r$ is, in general, not equal to $-1 / 3$ in the setting described above, this is not equal to the variance computed in Theorem 4.1.

As illustrated by Example 4.1, a permutation test based on $\sqrt{n g(n)} V_{n}$ will not be asymptotically valid, since the limiting variance of the permutation distribution and the limiting variance of the test statistic will not be equal in general. We may however proceed as usual, and find an appropriate estimator of the limiting variance of $V_{n}$ which is asymptotically consistent, and which, under the action of a random permutation, converges to 1 in probability.

Lemma 4.1. Let $\left\{X_{i}, i \in[n]\right\}$ be a stationary, $\alpha$-mixing sequence such that, for all $i \neq j$, $\mathbb{P}\left(X_{i}=X_{j}\right)=0$. Suppose also that

$$
\sum_{n \geq 1} \alpha_{X}(n)<\infty
$$

Let $g(n) \equiv G \in \mathbb{N}$ be constant. For each $i \in[n]$, let

$$
Y_{i}=\sum_{j=(i-G) \vee 1}^{i-1}\left(I\left\{X_{i}>X_{j}\right\}-I\left\{X_{i}<X_{j}\right\}\right)
$$

Let $b_{n} \in \mathbb{N}$ be such that $b_{n}=o(\sqrt{n})$ and, as $n \rightarrow \infty, b_{n} \rightarrow \infty$. Let

$$
\hat{\sigma}_{n}^{2}=\frac{1}{n} \sum_{i=1}^{n}\left(Y_{i}-\bar{Y}_{n}\right)^{2}+\frac{2}{n} \sum_{j=1}^{b_{n}} \sum_{i=1}^{n-j}\left(Y_{j}-\bar{Y}_{n}\right)\left(Y_{i+j}-\bar{Y}_{n}\right)
$$

Let

$$
\sigma^{2}=\operatorname{Var}\left(Y_{G+1}\right)+2 \sum_{k \geq 1} \operatorname{Cov}\left(Y_{G+1}, Y_{G+k+1}\right)
$$

We have that $\sigma^{2}<\infty$, and, as $n \rightarrow \infty$,

$$
\hat{\sigma}_{n}^{2} \xrightarrow{p} \sigma^{2}
$$

With the result of Lemma 4.1 in hand, we may now proceed to studentize the test statistic. By an application of Slutsky's theorem for randomization distributions, this studentization factor will have no effect on the limiting permutation distribution, but will result in the limiting distribution of the test statistic being asymptotically pivotal. Therefore, combining the previous results, we obtain the following.

Theorem 4.2. In the setting of Lemma 4.1, let $\mu=\mathbb{E} Y_{1+G}$. Let

$$
\hat{\tau}_{n}^{2}=\frac{1}{G} \hat{\sigma}_{n}^{2}
$$

and let $\nu=\mu / G$. We have the following:

(i) As $n \rightarrow \infty$,

$$
\frac{\sqrt{n G}\left(V_{n}-\nu\right)}{\hat{\tau}_{n}} \xrightarrow{d} N(0,1)
$$

(ii) Let $\hat{R}_{n}$ be the permutation distribution, with associated group of transformations $S_{n}$, the symmetric group of order $n$, based on the test statistic $\sqrt{n G} V_{n} / \hat{\tau}_{n}$. We have that, as $n \rightarrow \infty$,

$$
\sup _{t \in \mathbb{R}}\left|\hat{R}_{n}(t)-\Phi(t)\right| \xrightarrow{\text { a.s. }} 0
$$

where $\Phi$ is the distribution of a standard Gaussian random variable.

Proof. As in the proof of Lemma 4.1, let $Z_{i}=Y_{i+G}$, for $1 \leq i \leq n-G$. Let $m=n-G$. Since the $Y_{i}$ are uniformly bounded, we have that

$$
\begin{aligned}
\sqrt{n}\left(\bar{Y}_{n}-\mu\right) & =\sqrt{m}\left(\bar{Z}_{m}-\mu\right)(1+o(1))+\frac{1}{\sqrt{n}} \sum_{i=1}^{G} Y_{i} \\
& =\sqrt{m}\left(\bar{Z}_{m}-\mu\right)(1+o(1))+O\left(\frac{1}{\sqrt{n}}\right)
\end{aligned}
$$

In particular, by Ibragimov's central limit theorem (Ibragimov, 1962), Slutsky's theorem, and the result of Lemma 4.1, we have that

$$
\frac{\sqrt{n}\left(\bar{Y}_{n}-\mu\right)}{\hat{\sigma}_{n}} \xrightarrow{d} N(0,1)
$$

Since

$$
V_{n}=\frac{1}{g(n)} \bar{Y}_{n}
$$

the result of (i) follows.

Turning our attention to (ii), we observe that, since each $Y_{i}$ is a rank statistic, and, conditional on the data, under the action of $\Pi_{n} \sim \operatorname{Unif}\left(S_{n}\right)$, the ranks of the $X_{i}$ are uniformly distributed with probability 1 , the permutation distribution $\hat{R}_{n}$ is exactly equal to the unconditional distribution of the test statistic $\sqrt{n g(n)} V_{n} / \hat{\tau}_{n}$ in the case when the $X_{i}$ are i.i.d. with a continuous marginal distribution $F$. In this case, since $\mu=0$, the result of (ii) follows from that of (i).

Remark 4.2. As a result of Theorem 4.2, under the conditions laid out therein we have that a one-sided permutation test of the null hypothesis $H_{0, M}^{(l)}$, based on the test statistic $\sqrt{n M} V_{n} / \hat{\tau}_{n}$, where $V_{n}$ is the local Mann-Kendall statistic of order $M$, is asymptotically valid.

Remark 4.3. Let $M, r \in \mathbb{N}$ such that $M>r$. By an entirely analogous argument to the one presented in this section, one may construct permutation tests of the null hypothesis

$$
H_{0, M, r}^{(l)} \frac{1}{(n-M)\left(\begin{array}{c}
M \\
r
\end{array}\right)} \sum_{i_{1}<i_{2}<\cdots<i_{r} \leq i_{1}+M}\left(\mathbb{P}\left(X_{i_{1}}<\cdots<X_{i_{r}}\right)-\mathbb{P}\left(X_{i_{1}}>\cdots>X_{i_{r}}\right)\right)=0
$$

using a studentized version of the test statistic

$$
\frac{1}{(n-M)\left(\begin{array}{c}
M \\
r
\end{array}\right)} \sum_{i_{1}<i_{2}<\cdots<i_{r} \leq i_{1}+M}\left(I\left(X_{i_{1}}<\cdots<X_{i_{r}}\right)-I\left(X_{i_{1}}>\cdots>X_{i_{r}}\right)\right)
$$

## 5 Simulation results

In this section, we provide Monte Carlo simulations illustrating our results. Subsection 5.1 provides simulation results of the performance of the global Mann-Kendall permutation test, and Subsection 5.2 illustrates the performance of the local Mann-Kendall permutation test. In both sections, we consider one-sided tests, i.e. those rejecting for large values of the test statistic, conducted at the nominal level $\alpha=0.05$. The simulation results confirm that the two permutation tests are valid in that, in large samples, the rejection probability under the null hypothesis is approximately equal to $\alpha$.

### 5.1 Testing for global trend

We begin with a comparison of the performance of the studentized global Mann-Kendall permutation test against the classical Mann-Kendall test. As a review, the classical MannKendall test computes the statistic

$$
U_{n}=U_{n}\left(X_{1}, \ldots, X_{n}\right)=\left(\begin{array}{c}
n \\
2
\end{array}\right)^{-1} \sum_{i<j}\left(I\left\{X_{i}<X_{j}\right\}-I\left\{X_{i}>X_{j}\right\}\right)
$$

Under the null hypothesis that the sequence $\left\{X_{n}: n \in \mathbb{N}\right\}$ is i.i.d. and that $\mathbb{P}\left(X_{i}=X_{j}\right)=0$ for all $i \neq j$, the statistic $U_{n}$ has a fixed distribution $G_{n}$, and so the test compares $U_{n}$ to the $(1-\alpha)$ quantile of $G_{n}$ in order to reject or not reject the null hypothesis.

Note that, by the result of Theorem 3.1, the permutation distribution based on the unstudentized Mann-Kendall statistic converges weakly in probability to the same limiting distribution as the Mann-Kendall statistic under the additional assumption that the sequence is i.i.d. It follows that, for a fixed infinite-dimensional sequence $\left\{X_{n}: n \in \mathbb{N}\right\} \sim P$, the rejection probability of the classical Mann-Kendall test and the unstudentized global MannKendall permutation test will be asymptotically equal as $n \rightarrow \infty$. On account of this, in the following simulations, we present a comparison of the studentized global Mann-Kendall permutation test and the classical Mann-Kendall test.

In this simulation, we consider the following two settings: in Table 5.1, we consider processes of the following form. Let $m \in \mathbb{N}$. For $\left\{Z_{n}: n \in \mathbb{N}\right\}$ be i.i.d. standard Gaussian random variables, for each $n \in \mathbb{N}$, let

$$
X_{n}=\prod_{j=0}^{m-1} Z_{n+j}
$$

This sequence is $m$-dependent and stationary, and, for each $i \neq j, \mathbb{P}\left(X_{i} \neq X_{j}\right)=0$. Therefore $\left\{X_{n}: n \in \mathbb{N}\right\}$ satisfies the conditions of Theorem 3.4, and so the corresponding permutation test is asymptotically valid at the nominal level $\alpha$. Several distributions other than the standard Gaussian distribution were considered for the distribution of the $Z_{i}$, but these were observed to have little impact on the rejection probabilities of either the studentized global Mann-Kendall permutation test or the classical Mann-Kendall test.

We also consider more traditional autoregressive settings in Tables 5.2 and 5.3. Namely, we consider the following two examples. In Table 5.2, we consider the following processes: for $\left\{\epsilon_{n}: n \in \mathbb{N}\right\}$ a sequence of i.i.d. standard Gaussian random variables and some constant $\rho \in(-1,1)$, let $X_{1} \sim N\left(0,\left(1-\rho^{2}\right)^{-1}\right)$, independent of the $\epsilon_{i}$, and for each $n \geq 2$, let

$$
X_{n}=\rho X_{n-1}+\epsilon_{n}
$$

| $m$ | $n$ | 10 | 50 | 100 | 500 | 1000 |
| ---: | :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | Stud. Perm. | 0.045 | 0.059 | 0.047 | 0.047 | 0.054 |
|  | Classical M-K | 0.042 | 0.038 | 0.047 | 0.049 | 0.044 |
| 10 | Stud. Perm. | 0.054 | 0.061 | 0.062 | 0.057 | 0.055 |
|  | Classical M-K | 0.059 | 0.061 | 0.076 | 0.036 | 0.055 |
| 20 | Stud. Perm. | 0.036 | 0.082 | 0.063 | 0.051 | 0.045 |
|  | Classical M-K | 0.056 | 0.062 | 0.069 | 0.057 | 0.061 |
| 30 | Stud. Perm. | 0.056 | 0.085 | 0.077 | 0.052 | 0.046 |
|  | Classical M-K | 0.066 | 0.083 | 0.071 | 0.052 | 0.060 |

Table 5.1: Monte Carlo simulation results for null rejection probabilities for tests of $H_{0}^{(g)}$, in an $m$-dependent Gaussian product setting.

i.e. $\left\{X_{n}: n \in \mathbb{N}\right\}$ follows the unique distribution of the stationary $A R(1)$ process with standard Gaussian innovations.

| $\rho$ | $n$ | 10 | 50 | 100 | 500 | 1000 |
| :---: | :---: | ---: | ---: | ---: | ---: | ---: |
| -0.6 | Stud. Perm. | 0.047 | 0.192 | 0.039 | 0.074 | 0.043 |
|  | Classical M-K | 0.004 | 0.002 | 0.002 | 0.003 | 0.000 |
| -0.2 | Stud. Perm. | 0.043 | 0.072 | 0.058 | 0.046 | 0.057 |
|  | Classical M-K | 0.029 | 0.028 | 0.019 | 0.021 | 0.025 |
| 0.2 | Stud. Perm. | 0.030 | 0.053 | 0.046 | 0.042 | 0.058 |
|  | Classical M-K | 0.081 | 0.081 | 0.084 | 0.085 | 0.099 |
| 0.6 | Stud. Perm. | 0.035 | 0.052 | 0.068 | 0.042 | 0.049 |
|  | Classical M-K | 0.183 | 0.200 | 0.196 | 0.213 | 0.206 |

Table 5.2: Monte Carlo simulation results for null rejection probabilities for tests of $H_{0}^{(g)}$, in an $A R(1)$ setting.

Similarly, in Table 5.3, we consider processes of the following form: for $\rho \in(-1,1)$, let $\left\{Z_{n}: n \in \mathbb{N}\right\}$ and $\left\{Z_{n}^{\prime}: n \in \mathbb{N}\right\}$ be independent stationary $A R(1)$ processes with i.i.d. standard Gaussian innovations. For $n \in \mathbb{N} \cup\{0\}$, let

$$
\begin{aligned}
& X_{2 n+1}=Z_{n} \\
& X_{2 n+2}=Z_{n}^{\prime}
\end{aligned}
$$

Note that we may also express $\left\{X_{n}\right\}$ as the unique stationary process satisfying the autoregressive equation, for $n \geq 3$,

$$
X_{n}=\rho X_{n-2}+\eta_{n}
$$

for $\left\{\eta_{n}: n \in \mathbb{N}\right\}$ a sequence of i.i.d. standard Gaussian random variables, i.e. the $X_{i}$ follow an $A R(2)$ process.

As discussed in Example 3.2, the asymptotic rejection probability of the permutation test applied to such sequences is equal to the nominal level $\alpha$.

For each of the three situations, 1,000 simulations were performed. Within each simulation, the permutation test was calculated by randomly sampling 1,000 permutations.

| $\rho$ | $n$ | 10 | 50 | 100 | 500 | 1000 |
| :---: | :---: | ---: | ---: | ---: | ---: | ---: |
| -0.6 | Stud. Perm. | 0.148 | 0.354 | 0.024 | 0.188 | 0.033 |
|  | Classical M-K | 0.018 | 0.003 | 0.002 | 0.000 | 0.000 |
| -0.2 | Stud. Perm. | 0.074 | 0.092 | 0.059 | 0.052 | 0.039 |
|  | Classical M-K | 0.025 | 0.023 | 0.034 | 0.029 | 0.026 |
| 0.2 | Stud. Perm. | 0.030 | 0.048 | 0.048 | 0.037 | 0.055 |
|  | Classical M-K | 0.054 | 0.086 | 0.096 | 0.081 | 0.093 |
| 0.6 | Stud. Perm. | 0.009 | 0.104 | 0.060 | 0.059 | 0.067 |
|  | Classical M-K | 0.074 | 0.179 | 0.192 | 0.195 | 0.192 |

Table 5.3: Monte Carlo simulation results for null rejection probabilities for tests of $H_{0}^{(g)}$, in an $A R(2)$ setting.

We observe that, in the m-dependent Cauchy product setting of Table 5.1, both the studentized global Mann-Kendall permutation test and the classical Mann-Kendall test perform comparably, both controlling the rejection probability at (close to) the nominal level $\alpha$. However, in contrast, while the studentized global Mann-Kendall permutation test also exhibits Type 1 error control at the nominal level $\alpha$ in both the $A R(1)$ and $A R(2)$ settings of Tables 5.2 and 5.3, respectively, we observe the following phenomena. For $\rho>0$, we observe that the rejection probability of the classical Mann-Kendall test is significantly greater than $\alpha$, i.e. we do not have Type 1 error control. In addition, for $\rho<0$, we observe that the performance of the classical Mann-Kendall test is also unsatisfactory; namely, the rejection probabilities obtained are significantly below the nominal level $\alpha$, i.e. the test is overly conservative.

These issues may be explained as follows: since the limiting variance $\sigma^{2}$ of the MannKendall statistic is given by (3.2), for positively (negatively) autocorrelated sequences we have that $\sigma^{2}$ is greater than (less than) the limiting variance of the Mann-Kendall statistic under the additional assumption that the sequence is i.i.d. Heuristically, we have the interpretation
that the classical Mann-Kendall test "confuses" positive or negative autocorrelation with positive and negative trend, respectively, whereas the studentized global Mann-Kendall test does not succumb to this issue.

We observe several computational choices to be made when applying the permutation testing framework in practice. By the results of Theorems 3.3 and 3.4, for large values of $n$, the estimate $\hat{\sigma}_{n}^{2}$, as defined in (3.5), will be be strictly positive with high probability. However, for smaller values of $n$, it may be the case that a numerically negative value of $\hat{\sigma}_{n}^{2}$ is observed, either when computing the test statistic or the permutation distribution. A trivial solution to this issue is the truncate the estimate at some sufficiently small fixed lower bound $\epsilon>0$. Note that, for appropriately small choices of $\epsilon$, i.e. $\epsilon<\sigma^{2}$, the results of Theorems 3.3 and 3.4 still hold, i.e. inference based on this choice of studentization is still asymptotically valid. In practice, however, the suitability of a choice of $\epsilon$ for a particular numerical application is affected by the distribution of the $X_{i}$, and, in general, the estimated variance $\hat{\sigma}_{n}^{2}$ is bounded away from zero with high probability, on account of the additive constant 4/9 in the expression (3.5). For the above simulation, a constant value of $\epsilon=10^{-3}$ was used.

A further choice is that of the truncation sequence $\left\{b_{n}: n \in \mathbb{N}\right\}$ used in the definition of $\hat{\sigma}_{n}^{2}$. Any sequence $\left\{b_{n}\right\}$ such that, as $n \rightarrow \infty, b_{n} \rightarrow \infty$ and $b_{n}=o(\sqrt{n})$ is theoretically justified by Theorem 3.4, although, in a specific setting, some choices of $\left\{b_{n}\right\}$ will lead to more numerical stability than others. In practice, several choices of $\left\{b_{n}\right\}$ were implemented, but were found to make little difference to the rejection probabilities observed. In the simulations above, $\left\{b_{n}\right\}$ was taken to be $b_{n}=\left[n^{1 / 3}\right]$, where $[x]$ denotes the integer part of $x$.

### 5.2 Tests of local trend

We now turn our attention to simulations involving the local Mann-Kendall permutation test of the hypothesis $H_{0, M}^{(l)}$. Under the assumption that the sequence $\left\{X_{i}: i \in[n]\right\}$ is i.i.d., the randomization hypothesis holds, and so the unstudentized local Mann-Kendall permutation test will be exact in finite samples and asymptotically valid. However, in general, the randomization hypothesis does not hold under $H_{0, M}^{(l)}$, and so the unstudentized local Mann-Kendall permutation test will not be exact or even asymptotically valid. However, by the result of Theorem 4.2, the studentized local Mann-Kendall permutation test will be asymptotically valid at the nominal level $\alpha$.

In order to illustrate this behavior, we provide a comparison of the simulated rejection probabilities of the studentized and unstudentized local Mann-Kendall permutation tests in two different settings. In both of the settings described below, we consider the choice of $M=5$. For both of the following situations, 1,000 simulations were performed. Within each
simulation, the permutation test was calculated by randomly sampling 1,000 permutations.

In Table 5.4, we compare the simulated rejection probabilities of these two tests in the Gaussian product $m$-dependent setting described in Subsection 5.1.

| $m$ | $n$ | 20 | 50 | 100 | 500 | 1000 |
| ---: | :---: | ---: | ---: | ---: | ---: | ---: |
| 0 | Stud. Perm. | 0.049 | 0.047 | 0.051 | 0.046 | 0.058 |
|  | Unstud. Perm. | 0.060 | 0.062 | 0.061 | 0.057 | 0.058 |
| 1 | Stud. Perm. | 0.050 | 0.066 | 0.050 | 0.023 | 0.032 |
|  | Unstud. Perm. | 0.099 | 0.096 | 0.098 | 0.091 | 0.101 |
| 2 | Stud. Perm. | 0.057 | 0.078 | 0.065 | 0.009 | 0.021 |
|  | Unstud. Perm. | 0.115 | 0.129 | 0.131 | 0.164 | 0.138 |
| 3 | Stud. Perm. | 0.045 | 0.097 | 0.064 | 0.001 | 0.019 |
|  | Unstud. Perm. | 0.141 | 0.160 | 0.167 | 0.150 | 0.180 |

Table 5.4: Monte Carlo simulation results for null rejection probabilities for tests of $H_{0, M}^{(l)}$, for $M=5$, in an $m$-dependent Gaussian product setting.

We observe that, in Table 5.4, the studentized permutation test controls the rejection probability at the nominal level $\alpha$. However, in contrast, we observe that the unstudentized permutation test only has a rejection probability approximately equal to $\alpha$ in the case $m=0$, i.e. when the $X_{i}$ are i.i.d. and the randomization hypothesis holds. For $m>0$, the unstudentized permutation test visibly does not control the rejection probability at the nominal level $\alpha$.

In Table 5.5, we provide a comparison of the rejection probabilities of the studentized and unstudentized local Mann-Kendall permutation tests in the $A R(1)$ setting of Subsection 5.1.

We observe that, while the unstudentized permutation test somewhat surprisingly provides Type 1 error control at the nominal level $\alpha$ for negative values of $\rho$, it does not do so for positive values of $\rho$. For all values of $\rho$, the studentized permutation test has rejection probabilities below the nominal level $\alpha$.

As in Subsection 5.1, there are several computational choices to be made in practice. In particular, on account of the same numerical issues involving the studentization factor $\hat{\tau}_{n}^{2}$, we truncate the variance estimate at the lower bound $\epsilon=10^{-3}$. Similarly, we must choose a truncation sequence $\left\{b_{n}: n \in \mathbb{N}\right\}$ to be used in the definition of $\hat{\tau}_{n}^{2}$. In the above simulations, the choice $b_{n}=\left[n^{1 / 3}\right]$ was used.

| $\rho$ | $n$ | 20 | 50 | 100 | 500 | 1000 |
| :---: | :---: | ---: | ---: | ---: | ---: | ---: |
| -0.6 | Stud. Perm. | 0.048 | 0.182 | 0.050 | 0.055 | 0.044 |
|  | Unstud. Perm. | 0.021 | 0.028 | 0.036 | 0.049 | 0.042 |
| -0.2 | Stud. Perm. | 0.062 | 0.070 | 0.053 | 0.038 | 0.045 |
|  | Unstud. Perm. | 0.049 | 0.052 | 0.039 | 0.047 | 0.052 |
| 0.2 | Stud. Perm. | 0.037 | 0.029 | 0.033 | 0.078 | 0.061 |
|  | Unstud. Perm. | 0.085 | 0.072 | 0.071 | 0.087 | 0.066 |
| 0.6 | Stud. Perm. | 0.015 | 0.024 | 0.007 | 0.009 | 0.030 |
|  | Unstud. Perm. | 0.177 | 0.145 | 0.125 | 0.111 | 0.114 |

Table 5.5: Monte Carlo simulation results for null rejection probabilities for tests of $H_{0, M}^{(l)}$, for $M=5$, in an $A R(1)$ setting.

## 6 Conclusions

When the fundamental assumption of exchangeability does not necessarily hold, permutation tests are invalid unless strict conditions on underlying parameters of the problem are satisfied. For instance, the permutation test of $H_{0}^{(g)}$ based on the classical Mann-Kendall statistic is asymptotically valid only when $\sigma^{2}$ is as defined in (3.2), is equal to $4 / 9$. Hence rejecting the null must be interpreted correctly, since rejection of the null with this permutation test does not necessarily imply that the sequence truly does exhibit monotone trend, in the sense that the quantity

$$
\lim _{n \rightarrow \infty}\left(\begin{array}{l}
n \\
2
\end{array}\right)^{-1} \sum_{i<j}\left(\mathbb{P}\left(X_{i}<X_{j}\right)-\mathbb{P}\left(X_{i}>X_{j}\right)\right)
$$

may be equal to zero, and the Mann-Kendall test will still reject the null hypothesis. We provide a testing procedure that allows one to obtain asymptotic rejection probability $\alpha$ in a permutation test setting. A significant advantage of this test is that it retains the property of finite-sample exactness of the Mann-Kendall test under the assumption of i.i.d., as well as achieving asymptotic level $\alpha$ in a much wider range of settings than the aforementioned tests. This test also retains the convenient property of the classical Mann-Kendall test that the permutation distribution is fixed for a given sample size $n$. An analogous permutation testing procedure also permits for asymptotically valid inference for the newly-introduced notion of local monotone trend.

Correct implementation of a permutation test is crucial if one is interested in confirmatory inference via hypothesis testing; indeed, proper error control of Type 1,2 and 3 errors can be obtained for tests of global or local monotone trend by basing inference on test statistics
which are asymptotically pivotal. A framework has been provided for tests of both local and global monotone trend.

In this paper, we have defined specific notions of a lack of global monotone trend and a lack of local monotone trend of order $M$, and constructed asymptotically valid testing procedures of these null hypotheses. Future work will expand on the methods presented herein, in order to provide analogous permutation testing procedures in the context of other commonly-used tests for monotone trend.

## References

Bradley, R. C. (2005). Basic properties of strong mixing conditions. a survey and some open questions. Probab. Surveys, 2:107-144.

Dietz, E. J. and Killeen, T. J. (1981). A nonparametric multivariate test for monotone trend with pharamaceutical applications. Journal of the American Statistical Association, 76(373):169-174.

Freedman, D. (2011). Markov Chains. Springer, New York, NY.

Hamed, K. H. (2008). Trend detection in hydrologic data: The Mann-Kendall trend test under the scaling hypothesis. Journal of Hydrology, 349(3):350-363.

Han, F. and Qian, T. (2018). On inference validity of weighted U-statistics under data heterogeneity. Electronic Journal of Statistics, 12(2):2637 - 2708.

Hoeffding, W. (1948). A class of statistics with asymptotically normal distribution. The Annals of Mathematical Statistics, 19(3):293 - 325.

Ibragimov, I. A. (1962). Some limit theorems for stationary processes. Theory of Probability \&s Its Applications, 7(4):349-382.

Kendall, M. G. (1990). Rank Correlation Methods. Charles Griffin Book. Oxford University Press, London, England, 5 edition.

Lehmann, E. L. and Romano, J. P. (2022). Testing Statistical Hypotheses. Springer texts in statistics. Springer Nature, 4 edition.

Mann, H. B. (1945). Nonparametric tests against trend. Econometrica, 13(3):245-259.

Mokkadem, A. (1988). Mixing properties of ARMA processes. Stochastic Processes and their Applications, 29(2):309 - 315 .

Neumann, M. H. (2013). A central limit theorem for triangular arrays of weakly dependent random variables, with applications in statistics. ESAIM: PS, 17:120-134.

Romano, J. P. and Tirlea, M. A. (2022). Permutation testing for dependence in time series. Journal of Time Series Analysis, 43:781 - 807.

Romano, J. P. and Tirlea, M. A. (2024). Least squares-based permutation tests in time series. Technical Report, Department of Statistics, Stanford University.

Volkonskii, V. A. and Rozanov, Y. A. (1961). Some limit theorems for random functions. ii. Theory of Probability $\mathcal{G}$ Its Applications, 6(2):186-198.

Wang, F., Shao, W., Yu, H., Kan, G., He, X., Zhang, D., Ren, M., and Wang, G. (2020). Re-evaluation of the power of the Mann-Kendall test for detecting monotonic trends in hydrometeorological time series. Frontiers in Earth Science, 8.

Yue, S., Pilon, P., Phinney, B., and Cavadias, G. (2002). The influence of autocorrelation on the ability to detect trend in hydrological series. Hydrological Processes, 16(9):1807-1829.

Zhao, O. and Woodroofe, M. (2012). Estimating a monotone trend. Statistica Sinica, $22(1): 359-378$.

