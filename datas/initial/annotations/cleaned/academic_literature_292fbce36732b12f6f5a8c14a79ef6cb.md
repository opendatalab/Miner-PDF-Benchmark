# Just Wing It: Optimal Estimation of Missing Mass in a Markovian Sequence 

Ashwin Pananjady ${ }^{\star, \dagger}$, Vidya Muthukumar ${ }^{\dagger, \star}$, Andrew Thangaraj ${ }^{\ddagger}$<br>Schools of Industrial and Systems Engineering ${ }^{\star}$ and Electrical and Computer Engineering ${ }^{\dagger}$,<br>Georgia Institute of Technology<br>Department of Electrical Engineering $\ddagger$, IIT Madras

April 8, 2024


#### Abstract

We study the problem of estimating the stationary mass - also called the unigram massthat is missing from a single trajectory of a discrete-time, ergodic Markov chain. This problem has several applications - for example, estimating the stationary missing mass is critical for accurately smoothing probability estimates in sequence models. While the classical GoodTuring estimator from the 1950s has appealing properties for i.i.d. data, it is known to be biased in the Markov setting, and other heuristic estimators do not come equipped with guarantees. Operating in the general setting in which the size of the state space may be much larger than the length $n$ of the trajectory, we develop a linear-runtime estimator called Windowed GoodTuring (WINGIT) and show that its risk decays as $\widetilde{\mathcal{O}}\left(\mathrm{T}_{\text {mix }} / n\right)$, where $\mathrm{T}_{\text {mix }}$ denotes the mixing time of the chain in total variation distance. Notably, this rate is independent of the size of the state space and minimax-optimal up to a logarithmic factor in $n / T_{\text {mix }}$. We also present a bound on the variance of the missing mass random variable, which may be of independent interest. We extend our estimator to approximate the stationary mass placed on elements occurring with small frequency in $X^{n}$. Finally, we demonstrate the efficacy of our estimators both in simulations on canonical chains and on sequences constructed from a popular natural language corpus.


## 1 Introduction

Two classical problems in statistical analysis - relevant to both design of experiments and inference - are those of assessing sample coverage and discovery probability. Given a "training" sequence $X^{n}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ of random examples in some unknown sample space, the latter question concerns the probability with which an independent "test" observation $Y$ will be a discovery, in that it is an element of the sample space that was unseen at training time. Equivalently, we are interested in estimating the missing mass in the training sample $X^{n}$, i.e. $\operatorname{Pr}\left\{Y \notin\left\{X_{1}, \ldots, X_{n}\right\}\right\}$.

This problem has roots in statistical analysis for ecology (Fisher et al., 1943), and also has important applications across genomics (Favaro et al., 2012) as well as speech and language modeling (Church and Gale, 1991; Chen and Goodman, 1999). Let us give a few operational examples. For a first example from genomics (Lijoi et al., 2007), suppose we have performed genome sequencing on several genes of an organism as part of training data, and we are now interested in whether there is value in performing additional sequencing. Then the missing mass exactly measures the probability that we discover a new gene with additional sequencing, and an accurate estimate of this quantity can guide decisions about whether or not to sequence further. For a second example, consider the problem of building a probability model for a language corpus (Ney et al., 1994).

Many heuristic "smoothing" estimators have been developed for estimating these probability models (e.g., Ney et al., 1994; Jelinek, 1985; Gale and Sampson, 1995). A crucial component of these smoothing techniques is an estimate of the missing mass, since one would like to account for the (non-trivial) possibility that a word exists in the population corpus but has not yet been observed in the training data. Besides these two examples, estimates of the missing mass are also used in so-called competitive distribution estimation (Orlitsky and Suresh, 2015) and in estimating other functionals of distributions such as their entropy (Vu et al., 2007).

Many estimators with provable - and in fact minimax-optimal - guarantees exist for the case where the training data are exchangeable (Good, 1953; Lijoi et al., 2007; McAllester and Schapire, 2000). While the exchangeability assumption is reasonable in some applications, for example ecology (Shen et al., 2003; Colwell et al., 2012), it is clearly limiting in both genomics and speech or language applications, where temporal dependencies exist between the examples. The simplest form of such temporal dependence is Markovian structure, and, as articulated repeatedly in the literature (Hao et al., 2018; Chandra et al., 2021; Skorski, 2020), handling such structure in a principled fashion is an important first step for estimation of missing mass in temporally dependent training sequences. In spite of a significant body of work motivated by this topic, there still do not exist consistent estimators for missing mass functionals in general classes of Markovian sequences.

In this paper, we propose and theoretically analyze an estimator for the missing mass in a Markovian data sample, and variants for related problems. To make things concrete, suppose our stochastic process $X^{n}:=\left(X_{1}, \ldots, X_{n}\right)$ is modeled by a stationary Markov chain $(\boldsymbol{P}, \pi)$ on a finite but unknown state space $\mathcal{X}$. We will make no assumptions on the alphabet size $|\mathcal{X}|$, and will be interested in also capturing the practically relevant large-alphabet setting, i.e. where $|\mathcal{X}| \gg n$. Here $\pi=\left(\pi_{x}\right)_{x \in \mathcal{X}}$ denotes the unique stationary distribution of the chain, and the matrix $\boldsymbol{P} \in[0,1]^{|\mathcal{X}| \times|\mathcal{X}|}$ denotes the transition probability matrix of the Markov chain. We assume for convenience that $X_{1} \sim \pi$, but this assumption can be straightforwardly relaxed ${ }^{1}$.

As previously mentioned, our primary goal is to estimate the mass of the Markov chain that is missing from the random sample $X^{n}$. Motivated by the questions above, we focus on the stationary missing mass of the chain, given by

$$
M_{\pi}\left(X^{n}\right):=\sum_{x \in \mathcal{X}} \pi_{x} \cdot \mathbb{I}\left\{x \notin\left\{X_{1}, \ldots, X_{n}\right\}\right\}
$$

where $\pi_{x}$ is the probability assigned by the stationary distribution $\pi$ to element $x \in \mathcal{X}$. Note that $M_{\pi}\left(X^{n}\right)$ is a random functional, as it depends not only on the parameters of the chain but also the random sample $X^{n}$. An equivalent definition-which resembles the description above - is given by

$$
M_{\pi}\left(X^{n}\right)=\underset{\substack{Y \sim \pi \\ Y \Perp X^{n}}}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin\left\{X_{1}, \ldots, X_{n}\right\}\right\}\right]
$$

where $U \Perp V$ denotes that random variables $U$ and $V$ are independent.

The missing mass is not the only functional that is relevant to discovery probabilities. A closely related functional is the small-count stationary probability, which measures the probability of seeing an element that had a frequency at most $\zeta$ in the training sequence (Lijoi et al., 2007; Favaro et al., 2012). In particular, consider the estimand

$$
M_{\pi, \leq \zeta}\left(X^{n}\right)=\underset{\substack{Y \sim \pi \\ Y \Perp X^{n}}}{\mathbb{E}}\left[\mathbb{I}\left\{Y \text { appears at most } \zeta \text { times in }\left\{X_{1}, \ldots, X_{n}\right\}\right\}\right]
$$[^0]

We will present detailed results for estimating the functional $M_{\pi, \leq \zeta}$ in Section 5, focusing up until that point on the missing mass.

Our goal is to produce an estimator $\widehat{M}: \mathcal{X}^{n} \rightarrow[0,1]$ with minimum risk, where risk is measured using the mean squared error. In particular, for an estimand $M: \mathcal{X}^{n} \rightarrow[0,1]$ and estimator $\widehat{M}$, we write

$$
\operatorname{MSE}(\widehat{M}, M)=\underset{X^{n}}{\mathbb{E}}\left[\left|\widehat{M}\left(X^{n}\right)-M\left(X^{n}\right)\right|^{2}\right]
$$

Above, the expectation is taken over any other sources of randomness in $\widehat{M}$ in addition to the randomness in the sequence $X^{n}$.

To set up some additional notions, we let $\|\mu-\nu\|_{\text {TV }}$ denote the total variation distance between two probability measures $\mu$ and $\nu$ defined on the same space. Throughout, we assume that the Markov chain is ergodic and mixes in finite time. In particular, let $\mathrm{t}_{\text {mix }}(\epsilon)$ denote the mixing time of the chain to within total variation $\epsilon \in(0,1 / 2]$ of the stationary measure, i.e.

$$
\mathrm{t}_{\text {mix }}(\epsilon):=\min \left\{t \in \mathbb{N}: \max _{x \in \mathcal{X}}\left\|e_{x}^{\top} \boldsymbol{P}^{t}-\pi^{\top}\right\|_{\mathrm{TV}} \leq \epsilon\right\}
$$

where $e_{x}$ denotes the indicator vector on element $x \in \mathcal{X}$ and $\pi$ is viewed as a $|\mathcal{X}|$-dimensional column vector. The quantity $t_{\text {mix }}(1 / 4)$ is typically called the mixing time of the chain, and so we will write $\mathrm{T}_{\text {mix }}:=\mathrm{t}_{\text {mix }}(1 / 4)$. It is straightforward to show (see, e.g. Levin and Peres (2017)) that

$$
\mathrm{t}_{\text {mix }}(\epsilon) \leq \mathrm{T}_{\text {mix }} \cdot \log (1 / \epsilon) \text { for all } \epsilon<1 / 4
$$

### 1.1 Related work

The problem of estimating missing mass of a random sequence, where each element is drawn from an arbitrarily large sample space, was studied as far back as the 1800s by Laplace (1814), who proposed the first among the class of "add-constant" estimators. These estimators have seen a line of theoretical and empirical follow-up work (Krichevsky and Trofimov, 1981; Gale and Church, 1994), with special attention being paid to the add-1/2-estimator (Krichevsky and Trofimov, 1981). Instead of outputting the normalized empirical frequencies of elements as a maximum-likelihood estimator would, these estimators add a constant to the (un-normalized) empirical frequency prior to normalization. In the process, they output a non-zero missing mass probability.

A notable and groundbreaking result of Good (1953) - attributed also to Turing - moved away from the class of add-constant estimators and proposed to estimate the missing mass via the normalized frequency of elements appearing once in the sequence. In particular, letting $\phi_{s}\left(X^{n}\right)$ denote the number of distinct elements of $\mathcal{X}$ that have appeared $s$ times in the sample $X^{n}$, the celebrated Good-Turing estimator for the missing mass is given by

$$
\widehat{M}_{\mathrm{GT}}=\frac{\phi_{1}\left(X^{n}\right)}{n}
$$

The estimator has been applied to diverse areas (see, e.g., Song and Croft, 1999; Gale et al., 1992; Church and Gale, 1991) and has also seen intense theoretical study in the last three decades (see, e.g., McAllester and Schapire, 2000; Drukh and Mansour, 2005; Orlitsky et al., 2003). In particular, several analyses of fine-grained properties of the estimator now exist for the i.i.d. setting (see, e.g., Chandra et al., 2019; Rajaraman et al., 2017; Acharya et al., 2018), and variants of the estimator
have also been proposed and studied (Gandolfi and Sastri, 2004; Favaro et al., 2016; Painsky, 2022, 2023). While most analyses focus on additive error-e.g., the mean squared error of estimating the missing mass $M_{\pi}\left(X^{n}\right)$ - the multiplicative error metric has also been studied (Ohannessian and Dahleh, 2012; Mossel and Ohannessian, 2019; Ayed et al., 2021; Ben-Hamou et al., 2017; Grabchak and Zhang, 2017). Besides estimation, the missing mass random variable $M_{\pi}\left(X^{n}\right)$ has itself generated a lot of interest in the i.i.d. setting - its concentration properties have been thoroughly studied, and several analysis techniques have been developed along the way (McAllester and Ortiz, 2003; Berend and Kontorovich, 2012, 2013).

In contrast to the i.i.d. setting, the Markovian setting has received relatively sparse treatment, in spite of being the main setting - smoothing in language models - that motivated some of the initial papers on the theory of the subject (McAllester and Schapire, 2000, 2001). Some such papers include results for sticky Markov chains (Chandra et al., 2022) and rank-2 Markov chains (Chandra et al., 2021). These papers mainly study the performance of the Good-Turing estimator and/or certain scaled variants of it, and also give sufficient conditions under which Good-Turing can succeed for Markovian data. However, these conditions are restrictive, and it is not yet known if one can perform consistent, let alone minimax-optimal estimation of the missing mass in the general Markovian setting. Concentration of missing mass in the Markovian setting has also received some recent interest (Skorski, 2020) —-we will discuss this paper in greater detail in the sequel.

The problem of estimating the small-count probability (3) has also been studied in the literature (Lijoi et al., 2007), along with the related problem of estimating the exact count probability, i.e., the probability of elements occurring exactly $\zeta$ times (Good, 1953). Estimators of the count probability have been developed for i.i.d. samples, and several theoretical results are also available for this setting (McAllester and Schapire, 2001; Drukh and Mansour, 2005; Acharya et al., 2013). The Markovian case, however, does not seem to have been theoretically studied.

Finally, we mention that besides the missing mass and count probabilities, other estimation and prediction problems (Hao et al., 2018; Han et al., 2023; Wolfer and Kontorovich, 2019) and bounds on 'surprise' probabilities (Norris et al., 2017) have been studied for Markov chains. The size of the state space appears explicitly as a parameter in these results.

### 1.2 Contributions and organization

Our contributions are summarized below:

- In Section 3, we propose an estimator for stationary missing mass in the Markov setting called the Windowed Good-Turing, or WINGIT, estimator. Our estimator is based on the viewpoint of the Good-Turing estimator as a leave-one-out estimator, a perspective that we review (for the i.i.d. setting) and develop in Section 2.
- In Theorem 1 of Section 4, we provide a risk bound on the WingIt estimator, showing that it attains mean squared error on the order $T_{\text {mix }} / n$ up to a logarithmic factor in $n / T_{\text {mix }}$. This matches, up to this logarithmic factor, the minimax lower bound for missing mass estimation in mixing Markov chains (Chandra et al., 2022).
- Aside from providing an estimator for the missing mass, we also analyze the missing mass functional $M_{\pi}\left(X^{n}\right)$ as a random variable, and show in Theorem 2 that its variance is bounded on the order $\mathrm{T}_{\text {mix }} / n$ up to a logarithmic factor. This constitutes, to our knowledge, the first such result in the Markovian setting, complementing a one-sided bound due to Skorski (2020).
- In Section 5, we present an extension of our methodology for estimating the small-count probability (3). Note that this generalizes the problem of estimating the stationary missing mass, which corresponds to the case $\zeta=0$. This result, stated as Theorem 3, appears to improve analogous guarantees from the literature even for i.i.d. samples.
- In Section 6, we provide simulations on some synthetic Markov chains and on natural language text. These experiments corroborate our theory while showing how the WINGIT estimator can significantly outperform the vanilla Good-Turing estimator. We also explore an automatic and data-dependent tuning method for the window size in our WINGIT estimator.

Notation: For two real numbers $a$ and $b$, let $a \wedge b=\min \{a, b\}$ and $a \vee b=\max \{a, b\}$. Let $[n]$ denote the set of natural numbers less than or equal to $n$. For an index set $P \subseteq[n]$, let $\boldsymbol{X}_{P}=\left\{X_{i}\right\}_{i \in P}$ denote the set of random variables corresponding to that index set. The set $\boldsymbol{X}_{[n]}$ thus contains all random variables in the sequence $X^{n}$. With a slight abuse of notation, we let $X_{P}=\left(X_{i}\right)_{i \in P}$ denote the sequence of random variables with indices in $P$, ordered canonically. We use $\oplus$ to denote the concatenation of sequences, e.g., $\left(X_{1}, X_{2}\right) \oplus\left(X_{4}, X_{5}\right)=\left(X_{1}, X_{2}, X_{4}, X_{5}\right)$. For two sequences indexed by $u$, we use the notation $f(u) \lesssim g(u)$ to mean that there exists some absolute positive constant $C$ that is independent of all problem parameters, such that $f(u) \leq C \cdot g(u)$ for all $u$. We use the notation $f(u) \gtrsim g(u)$ when $g(u) \lesssim f(u)$. We write $f(u) \asymp g(u)$ if both relations $f(u) \gtrsim g(u)$ and $g(u) \lesssim f(u)$ hold. Logarithms are taken to the base $e$. We use $(c, C)$ to denote universal positive constants that could be different in each instantiation.

## 2 From i.i.d. to Markov: Revisiting Good-Turing

First, let us revisit the special case where the samples $X^{n}$ are i.i.d. and the stationary distribution $\pi$ corresponds to the probability mass function from which each sample is drawn. Here, the celebrated Good-Turing estimator (7) of $M_{\pi}\left(X^{n}\right)$ is given by the number of symbols that appear once in $X^{n}$ divided by the sample size $n$. As articulated by, e.g., McAllester and Schapire (2001), this quantity can be thought of as a leave-one-out estimate of the functional that repeatedly simulates a placeholder for $Y$ from the given sample and approximately evaluates the indicator in Eq. (2). In particular, consider the collection of estimators given by the random variables

$$
\widehat{M}^{(i)}=\mathbb{I}\left\{X_{i} \notin\left\{X_{1}, \ldots, X_{i-1}, X_{i+1}, \ldots, X_{n}\right\}\right\} \quad \text { for } \quad i=1, \ldots, n
$$

We can then equivalently write the Good-Turing estimator (7) as

$$
\widehat{M}_{\mathrm{GT}}=\frac{1}{n} \sum_{i=1}^{n} \widehat{M}^{(i)}
$$

Clearly, the random variable $X_{i}$ "simulates" drawing a fresh sample $Y$ from $\pi$ independently of the subsequence $\left(X_{1}, \ldots, X_{i-1}, X_{i+1}, \ldots, X_{n}\right.$ ), and inspecting Eq. (2) yields that $\widehat{M}^{(i)}$ is an unbiased estimator of $M_{\pi}\left(X_{1}, \ldots, X_{i-1}, X_{i+1}, \ldots, X_{n}\right)$. Using the i.i.d. nature of the observations, one can then show that (McAllester and Schapire, 2000)

$$
\left.\mid \mathbb{E}\left[M_{\pi}\left(\left(X_{1}, \ldots, X_{i-1}, X_{i+1}, \ldots, X_{n}\right)\right)\right]-M_{\pi}\left(X^{n}\right)\right] \mid \lesssim n^{-1}
$$

so that we have a near-unbiased estimator of the quantity $\mathbb{E}\left[M_{\pi}\left(X^{n}\right)\right]$. Coupling this observation with additional arguments that bound the variance of the estimator $\widehat{M}_{G T}$ and estimand
$M_{\pi}$ (McAllester and Schapire, 2000; McAllester and Ortiz, 2003), we obtain a bound on the meansquared error of the Good-Turing estimator.

It is instructive to re-examine the central pitfall of the Good-Turing estimator for a Markov chain, which is that strong local dependencies between adjacent samples in the Markov chain induce non-vanishing bias. This argument has been sketched before (see, e.g. Chandra et al. (2022)), but we nevertheless give a brief, self-contained illustrative example and a heuristic calculation of the bias below. Let $\mathcal{X}=[k]$ for some $k \gg n$ and consider transition kernels $\boldsymbol{P} \in[0,1]^{k \times k}$ of the form

$$
\boldsymbol{P}=(1-p) \boldsymbol{I}+p \mathbf{1} \pi^{\top}
$$

where $\boldsymbol{I}$ and $\mathbf{1}$ denote the identity matrix and all-1s column vector of suitable dimensions. Such a transition kernel gives rise to a so-called "sticky", or lazy, Markov chain having stationary distribution $\pi$ and mixing time $\frac{1}{2 p} \leq \mathrm{T}_{\text {mix }} \leq \frac{2}{p}$ for all $k \geq 2$ and $p \in(0,1 / 2]$ (see Lemma 1). Thus, as the probability $p$ becomes small, the mixing time becomes proportionally large.

Now suppose that $\pi=\frac{1}{k} \mathbf{1}$, so that the stationary distribution is the uniform distribution on $k$ elements. Due to the stickiness of the chain-i.e., its propensity to remain in its current state - we will see $K \asymp n p \asymp n / T_{\text {mix }}$ unique elements in a typical sample $\left(X_{1}, \ldots, X_{n}\right)$ of the chain. The stationary missing mass of the chain will hence be given, in expectation, by

$$
\mathbb{E}\left[M_{\pi}\left(X^{n}\right)\right]=\frac{k-\mathbb{E}[K]}{k} \geq \frac{k \mathrm{~T}_{\text {mix }}-C n}{k \mathrm{~T}_{\text {mix }}}
$$

for some universal constant $C$.

On the other hand, the Good-Turing estimator will obey $\mathbb{E}\left[\widehat{M}_{\mathrm{GT}}\left(X^{n}\right)\right] \leq p$. This is because for all $i \in[n]$, we have

$$
\mathbb{E}\left[\widehat{M}_{\mathrm{GT}}\left(X^{n}\right)\right]=\mathbb{E}\left[\widehat{M}^{(i)}\right]=\operatorname{Pr}\left\{X_{i} \notin\left\{X_{1}, \ldots, X_{i-1}, X_{i+1}, \ldots, X_{n}\right\} \leq \operatorname{Pr}\left\{X_{i} \neq X_{i-1}\right\}=p\right.
$$

Consequently, we have

$$
\left|\mathbb{E}\left[M_{\pi}\left(X^{n}\right)-\widehat{M}_{\mathrm{GT}}\left(X^{n}\right)\right]\right| \stackrel{(\mathrm{i})}{\stackrel{ }{2}}\left|\frac{k \mathrm{~T}_{\text {mix }}-\mathbb{E}[K]}{k \mathrm{~T}_{\text {mix }}}-\frac{2}{\mathrm{~T}_{\text {mix }}}\right| \stackrel{\text { (ii) }}{\geq} \frac{1}{4}
$$

where step (i) uses the fact that $p \in\left[\frac{1}{2 T_{\text {mix }}}, \frac{2}{T_{\text {mix }}}\right]$ and step (ii) holds as long as $k \geq C n / T_{\text {mix }}$ for a sufficiently large constant $C>0$ and $\mathrm{T}_{\text {mix }} \geq 8$. Applying Jensen's inequality yields the lower bound

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{GT}}, M_{\pi}\right) \geq\left|\mathbb{E}\left[M_{\pi}\left(X^{n}\right)-\widehat{M}_{\mathrm{GT}}\left(X^{n}\right)\right]\right|^{2} \geq 1 / 16
$$

thus illustrating that the Good-Turing estimator has constant, non-vanishing bias for sticky Markov chains in which the stationary distribution is uniform on a large state space. This phenomenon is also empirically illustrated in Figure 2 in Section 6.

While the biased nature of the Good-Turing estimator is unfortunate, we next build on some important design principles sketched here in order to develop an unbiased estimator.

## 3 Methodology: The Windowed Good-Turing estimator

In this section, we describe a natural modification of the Good-Turing estimator, interpreted through the leave-one-out lens (8), that mitigates the above issues and estimates the stationary missing mass at a minimax-optimal rate.

### 3.1 A first step: Modifying the "leave-one-out" estimator to reduce its bias

The central issue with the original leave-one-out estimator $\widehat{M}^{(i)}(8)$ when applied to Markov chains lay in the strong dependencies induced between adjacent samples of the chain: As demonstrated by Eq. (11), successive samples $X_{i}$ and $X_{i-1}$ are tightly coupled through the structure of the transition kernel and very far from being independent. To mitigate this issue, we modify the leaveone-out estimator to a "leave-a-window-out" estimator that removes the samples adjacent to $X_{i}$ before computing the corresponding estimator. We first illustrate the idea for $i=n$ for simplicity. Recall that $\widehat{M}^{(n)}=\mathbb{I}\left\{X_{n} \notin\left\{X_{1}, \ldots, X_{n-1}\right\}\right\}$. Instead of using the leave-one-out subsequence $\left(X_{1}, \ldots, X_{n-1}\right)$ as a proxy for $X^{n}$, we use the slightly smaller subsequence $\left(X_{1}, \ldots, X_{n-\tau}\right)$. As long as we choose $\tau \gg \mathrm{T}_{\text {mix }}$, we should expect that $\left(X_{1}, \ldots, X_{n-\tau}\right)$ is nearly independent of $X_{n}$. Accordingly, we define the estimator

$$
\widehat{M}_{\tau}^{(n)}:=\mathbb{I}\left\{X_{n} \notin\left\{X_{1}, \ldots, X_{n-\tau}\right\}\right\}
$$

To develop some quantitative intuition, suppose for the moment that $X_{n}$ were exactly independent of $\left(X_{1}, \ldots, X_{n-\tau}\right)$, and recall that the marginal distribution of $X^{n}$ is the stationary measure $\pi$. Then by construction, the random variable $\widehat{M}_{\tau}^{(n)}$ would be an unbiased estimator of $M_{\pi}\left(X^{n-\tau}\right)$, which one should expect, in turn, to be close to the desired missing mass $M_{\pi}\left(X^{n}\right)$. More formally, Lemmas 2 and 4 (referenced in the proof of Theorem 1) use an approximate-independence argument and show that for sufficiently large $\tau$, we have

$$
\mathbb{E}\left[M_{\pi}\left(X^{n-\tau}\right)-M_{\pi}\left(X^{n}\right)\right] \lesssim \frac{\tau}{n}
$$

Thus, the bias of $\widehat{M}_{\tau}^{(n)}$ now decays with the "effective" sample size $n_{0}:=n / \tau$.

### 3.2 WingIt: Averaging an ensemble of windowed leave-one-out estimators

Above, we have produced a single random variable $\widehat{M}_{\tau}^{(n)}$ with decaying bias. However, we still have

the issue of variance. How do we construct multiple estimators like $\widehat{M}_{\tau}^{(n)}$ and average over them as in Eq. (9)? The natural idea to construct the $i$-th such estimator is to inspect the definition (13), replace $X_{n}$ with $X_{i}$, and the set $\left\{X_{1}, \ldots, X_{n-\tau}\right\}$ with the portion of the sequence $X^{n}$ that should behave as nearly independent of $X_{i}$. Concretely, for each $i \in[n]$, define the index sets

$$
\mathcal{D}_{i}=\{k \in[n]:|k-i|<\tau\} \quad \text { and } \quad \mathcal{I}_{i}=[n] \backslash \mathcal{D}_{i}
$$

In words the set $\mathcal{D}_{i}$ contains indices that are close to $i$, so that if $\tau \gg \mathrm{t}_{\text {mix }}$ then we should expect $\boldsymbol{X}_{\mathcal{D}_{i}}$ to be the set of random variables in the sequence that depend on $X_{i}$. On the other hand, the complementary set $\mathcal{I}_{i}$ is the index set of random variables that are nearly independent of $X_{i}$. The above intuition then leads naturally to the estimator

$$
\widehat{M}_{\tau}^{(i)}:=\mathbb{I}\left\{X_{i} \notin \boldsymbol{X}_{\mathcal{I}_{i}}\right\}
$$

which generalizes $\widehat{M}_{\tau}^{(n)}$ to any index $i$. Finally, we combine these estimates to reduce variance. Letting $n_{0}:=\lfloor n / \tau\rfloor$, we create the final estimator

$$
\widehat{M}_{\mathrm{WINGIT}}(\tau)=\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \widehat{M}_{\tau}^{(j \tau)}
$$

Note that we have not used the random variables $\widehat{M}_{\tau}^{(i)}$ for all $i \in[n]$; instead, we have skipped samples at intervals of the window size $\tau$ to attempt to decorrelate the summands in Eq. (16) while still benefiting from averaging. Note that if $\tau=1$, then we recover the Good-Turing estimator (9). See Figure 5 later in the paper for an illustration of the windowing procedure.

### 3.3 Linear time implementation of WingIt

As presented in Eqs. (15) and (16), the WingIt estimator can be naively implemented in $\mathcal{O}\left(n^{2}\right)$ time, since each estimator $\widehat{M}_{\tau}^{(i)}$ can be computed by searching through the entire sequence. In this section, we show that, in fact, the entire estimator $\widehat{M}_{\mathrm{WINGIT}}(\tau)$ can be computed in time $\mathcal{O}(n)$ time for any value of the window size $\tau$. The computational complexity of the WINGIT estimator is thus comparable to that of the vanilla Good-Turing estimator (7). Given a sequence $X^{n}$ and a natural number $\tau$, the algorithm proceeds via two passes through the data:

1. Iterate through indices $i=1, \ldots, n$ while forming a dictionary locations with keys as elements in $\mathcal{X}$ and values as lists containing indices. If ' $X_{i}$ ' exists already as a key, append $i$ to its list value; otherwise create a key ' $X_{i}$ ' and associate to it a list containing $i$. Eventually, for each $x \in \boldsymbol{X}_{[n]}$, locations [' $x$ '] will contain a list of all indices at which $x$ appears in the sequence, sorted in increasing order.
2. Next, iterate through window indices $j=1, \ldots, n_{0}$. For each $j$, call the list locations [' $\left.X_{j \tau}{ }^{\prime}\right]$ and inspect its first element $\ell_{j}$ and last element $r_{j}$. Let $P_{j}=\mathbb{I}\left\{\left|j \tau-\ell_{j}\right|<\tau\right\} \cdot \mathbb{I}\left\{\left|r_{j}-j \tau\right|<\tau\right\}$.
3. Return the estimate $\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} P_{j}$.

Correctness: It suffices to show that in step 2 we have $P_{j}=\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j \tau}}\right\}=M_{\tau}^{(j \tau)}$ for all $j \in\left[n_{0}\right]$. To evaluate the indicator $\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j \tau}}\right\}$-or equivalently, the indicator $\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j \tau}}\right\}$ 一 we must check if there exists some index $k \in[n]$ such that $|k-j \tau| \geq \tau$ and $X_{k}=X_{j \tau}$. But note that by construction, the list locations [' $\left.X_{j \tau}{ }^{\prime}\right]$ contains indices $k \in[n]$ sorted in increasing order such that $X_{k}=X_{j \tau}$. Thus, we have

$$
\max _{k: X_{k}=X_{j \tau}}|j \tau-k|=\max \left\{\left|j \tau-\ell_{j}\right|,\left|r_{j}-j \tau\right|\right\}
$$

and it suffices to compare $j \tau$ with the first (i.e. smallest) and last (i.e., largest) element of the list locations [' $\left.X_{j \tau}{ }^{\prime}\right]$.

Running time: Step 1 requires a single pass through the data and $\mathcal{O}(n)$ time in total. In step 2, for each value of $j$, we access only the first and last element of the list locations [' $\left.X_{j \tau}{ }^{\prime}\right]$, which takes two operations in a Python implementation. The total running time of step 2 is therefore $\mathcal{O}(n)$ and step 3 also takes $\mathcal{O}\left(n_{0}\right)=\mathcal{O}(n)$ time, resulting in an overall algorithm that runs in linear time.

Memory: The memory requirement is dominated by the dictionary creation in step 1 . We create a list for each dictionary key, and the sum of sizes of all lists is equal to the number of elements observed, i.e., $n$. So the memory, assuming each element of $\mathcal{X}$ and $[n]$ can be stored in constant space, is $\mathcal{O}(n)$.

Having proved that the WINGIT estimator can be computed using linear time and space, we now turn to studying its estimation error properties.

## 4 Theoretical results on missing mass estimation

This section presents a risk guarantee for $\widehat{M}_{\mathrm{WINGIT}}$ and a variance bound on the estimand $M_{\pi}\left(X^{n}\right)$.

### 4.1 Risk guarantee for the WingIt estimator

We first provide a guarantee for the risk of the estimator $\widehat{M}_{\text {WINGIT }}$ (16). Recall the definition (5) of the mixing time up to arbitrary total variation $\mathrm{t}_{\text {mix }}(\epsilon)$ and that we write $\mathrm{T}_{\text {mix }}=\mathrm{t}_{\text {mix }}(1 / 4)$.

Theorem 1. Suppose we choose $\tau \geq \mathrm{t}_{\text {mix }}\left(\left(\mathrm{T}_{\text {mix }} / n\right)^{2} \wedge 1 / 4\right)$, and let $\widehat{M}_{\mathrm{WINGIT}}(\tau)$ denote the estimator defined in $E q$. (16). Then there is an absolute positive constant $C$ such that

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}}(\tau), M_{\pi}\right) \leq C \cdot \frac{\tau}{n} \wedge 1
$$

Before proceeding to our detailed discussion of the Markov case, we note in passing that the MSE guarantee (17) recovers existing guarantees (McAllester and Schapire, 2000; Rajaraman et al., 2017) for the Good-Turing estimator, since in the i.i.d. case the chain mixes in one step, our estimator specializes to Good-Turing, and we may set $\tau=1$ in Theorem 1 .

A few remarks on the general Markov case are now in order. We assume that $n \geq 2 T_{\text {mix }}$ in all the remarks below; if $n<2 T_{\text {mix }}$, then the RHS in Eq. (17) reduces to a universal constant and conversely, it is straightforward to show that consistent estimation is impossible (see footnote 3 below). Let us now proceed to our discussion.

First, observe that if $n \geq 2 T_{\text {mix }}$, it follows from the mixing condition in Eqs. (5) and (6) that $\mathrm{t}_{\text {mix }}\left(\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2} \wedge 1 / 4\right) \leq 2 \mathrm{~T}_{\text {mix }} \cdot \log \left(n / \mathrm{T}_{\text {mix }}\right)$. Therefore, if we know $\mathrm{T}_{\text {mix }}$ up to a universal constant factor - estimators for the mixing time are available in the literature for, e.g. for reversible Markov chains (Hsu et al., 2019)-then we can set the window size $\tau \asymp \mathrm{T}_{\text {mix }} \cdot \log \left(n / \mathrm{T}_{\text {mix }}\right)$ and obtain

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}}(\tau), M_{\pi}\right) \lesssim \frac{\mathrm{T}_{\text {mix }}}{n} \cdot \log \left(n / \mathrm{T}_{\text {mix }}\right)
$$

In practice, one would need to tune $\tau$, and we sketch a possible tuning method in Section 6.

Second, we remark on the issue of optimality. Chandra et al. (2022) proved a minimax lower bound of order $\Omega\left((n p)^{-1}\right)$ on the mean squared error of estimating missing mass in sticky chains of the form (10). As remarked on before (see Lemma 1), such chains have a mixing time $\mathrm{T}_{\text {mix }} \asymp p^{-1}$, so this yields a lower bound of $\Omega\left(\mathrm{T}_{\text {mix }} / n\right)$ for such chains. Theorem 1 matches this lower bound up to the $\operatorname{logarithmic}$ factor $\log \left(n / T_{\text {mix }}\right)$ and further holds for all chains of mixing time at most $T_{\text {mix }}$. More formally, define the class of Markov chains that mix in time at most $T$, as

$$
\mathcal{P}_{\text {mix }}(T):=\left\{\text { Markov chain }(\boldsymbol{P}, \pi): \text { mixing time of chain } \mathrm{T}_{\text {mix }} \text { is at most } T\right\}
$$

Theorem 1 implies that for a universal constant $C>0$, we have the worst-case upper bound

$$
\sup _{(\boldsymbol{P}, \pi) \in \mathcal{P}_{\text {mix }}(T)} \operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}}(2 T \log n), M_{\pi}\right) \leq C \cdot \frac{T \log (n / T)}{n}
$$

On the other hand, we may state ${ }^{2}$ the minimax lower bound (Chandra et al., 2022, Theorem 2) as the following: There is a universal constant $c>0$ such that if $n \geq 2 T \log n$ then for any estimator[^1]$\widehat{M}$ that is a measurable function of the observations $X^{n}$, we must have

$$
\sup _{(\boldsymbol{P}, \pi) \in \mathcal{P}_{\text {mix }}(T)} \operatorname{MSE}\left(\widehat{M}, M_{\pi}\right) \geq c \cdot \frac{T}{n}
$$

Taken together, Eqs. (18a) and (18b) thus imply that in the regime $n \gtrsim T \log n$, the WINGIT estimator is information-theoretically minimax optimal up to a logarithmic factor in $n$. Removing this logarithmic factor is an interesting open problem, and will likely require new ideas both in terms of algorithm design and analysis.

Finally, we comment on our analysis path, which is significantly different from the related literature on missing mass estimation from an i.i.d. sequence. As alluded to before, a natural and popular method to analyze estimators of the missing mass in the i.i.d. setting (McAllester and Schapire, 2000, 2001) is to exploit concentration of the estimand and write

$$
\operatorname{MSE}\left(\widehat{M}, M_{\pi}\right) \leq 3\left|\underset{X^{n}}{\mathbb{E}}\left[\widehat{M}\left(X^{n}\right)\right]-\underset{X^{n}}{\mathbb{E}}\left[M_{\pi}\left(X^{n}\right)\right]\right|^{2}+3 \operatorname{var}\left(\widehat{M}\left(X^{n}\right)\right)+3 \operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right)
$$

which can be obtained by adding and subtracting terms and using the elementary inequality $(a+$ $b+c)^{2} \leq 3\left(a^{2}+b^{2}+c^{2}\right)$. Operationally, therefore, analyzing the MSE of the estimator relies in itself on understanding the variance of the missing mass random variable $M_{\pi}\left(X^{n}\right)$, which has nothing to do with the estimator. In the Markovian case, it appears challenging to control $\operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right)$ by straightforward means. Other analysis techniques for missing mass estimation in the i.i.d. setting (e.g. Rajaraman et al., 2017; Chandra et al., 2019) work with an exact decomposition of the MSE expressed as a sum of weighted indicators over pairs of elements $x, x^{\prime} \in \mathcal{X}$, and use the i.i.d. assumption to bound these terms in a precise fashion. One such property that is used to show concentration is the negative associativity of certain random variables (McAllester and Ortiz, 2003), and we do not expect this property to hold for general Markov chains.

In contrast to these approaches, we begin with a nonstandard decomposition of the MSE by conditioning on the sequence $X^{n}$, and our argument deviates significantly from Eq. (19). Besides the nonstandard decomposition, we also call out a few other features of the proof. Throughout, owing to the structure of our estimator (16), we must compare our random sequence $X^{n}$ to suitably modified random sequences with windows of random variables left out; we do so by proving certain total variation bounds for Markov bridges, in Lemmas 6 and 7. Another important but delicate feature of our proof is that we are able to obtain the sharp near-linear dependence of the rate on $\mathrm{T}_{\text {mix }}$ - in order to do this, we bound a certain functional of hitting times in independent draws of a shorter Markov chain (Lemma 4) and show that our Markovian sequence $X^{n}$ can be approximated in some appropriate sense by such independent shorter Markovian draws via repeatedly restarting the chain at stationarity (Lemma 8).

### 4.2 Variance of missing mass functional $M_{\pi}\left(X^{n}\right)$

The analysis path that we sketched above circumvents needing to control the variance of the estimand, i.e. $\operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right)$. Nevertheless, and somewhat surprisingly, analyzing various properties of the estimator $\widehat{M}_{\text {WINGIT }}$ allows us to indirectly bound $\operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right)$. We state this result as the following theorem, which could be of independent interest.[^2]

Theorem 2. There is an absolute positive constant $C$ such that

$$
\operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right) \leq C \cdot \frac{\mathrm{T}_{\mathrm{mix}} \cdot \log \left(1+n / \mathrm{T}_{\mathrm{mix}}\right)}{n} \wedge 1
$$

Theorem 2 is proved in Section 7.2. En route, we control the bias and variance of the estimator $\widehat{M}_{\text {WINGIT }}$, which - owing to our nonstandard error decomposition - are related but distinct quantities from the MSE that was characterized in Theorem 1.

The most related result to Theorem 2 was proved by Skorski (2020), who showed a one-sided tail bound on $M_{\pi}\left(X^{n}\right)$ in terms of the hitting time of large sets of the Markov chain. Even though the hitting time of large sets is comparable to the mixing time (Oliveira, 2012; Peres and Sousi, 2015), the main result of Skorski (2020) cannot, strictly speaking, be compared with Theorem 2. On the one hand, Theorem 2 implies the two-sided polynomial tail bound

$$
\operatorname{Pr}\left\{\left|M_{\pi}\left(X^{n}\right)-\mathbb{E}\left[M_{\pi}\left(X^{n}\right)\right]\right| \geq \epsilon\right\} \leq C \cdot \frac{\mathrm{T}_{\text {mix }} \log \left(1+n / \mathrm{T}_{\text {mix }}\right)}{n \epsilon^{2}} \text { for all } \epsilon>0
$$

which can be obtained via direct application of Markov's inequality. On the other hand, Skorski (2020, Corollary 1) provides a stronger exponentially decaying bound, but only on the upper tail. In the result of Skorski (2020), the random variable $M_{\pi}\left(X^{n}\right)$ is also not centered at its expectation.

Having discussed estimation guarantees for the missing mass, we now turn to the problem of estimating small-count probabilities.

## 5 Estimating stationary mass of elements with frequency at most $\zeta$

In this section, we show that the idea behind the WINGIT estimator can be applied robustly to estimate not only the missing mass functional $M_{\pi}\left(X^{n}\right)$, but also the mass of all elements that occur at most $\zeta$ times (3). To define this functional formally, let $N_{x}\left(X_{P}\right)=N_{x}\left(\boldsymbol{X}_{P}\right):=\sum_{i \in P} \mathbb{I}\left\{X_{i}=x\right\}$ denote the number of occurrences of the element $x \in \mathcal{X}$ in the (sub)-sequence $X_{P}$ and subset $\boldsymbol{X}_{P}$. Then, the mass of all elements that occur exactly $\zeta$ times is defined as

$$
M_{\pi, \zeta}\left(X^{n}\right):=\sum_{x \in \mathcal{X}} \pi_{x} \cdot \mathbb{I}\left\{N_{x}\left(X^{n}\right)=\zeta\right\}
$$

We focus on the mass of all elements that occur at most $\zeta$ times (cf. the definition in Eq. (3))

$$
M_{\pi, \leq \zeta}\left(X^{n}\right):=\sum_{x \in \mathcal{X}} \pi_{x} \cdot \mathbb{I}\left\{N_{x}\left(X^{n}\right) \leq \zeta\right\}
$$

Clearly, both Eq. (21) and Eq. (22) recover the missing mass functional $M_{\pi}\left(X^{n}\right)$ when $\zeta=0$. For small $\zeta$, both of these functionals provide more fine-grained information about the mass placed by the stationary distribution on low-frequency elements of $X^{n}$. We now define a natural extension of the WINGIT estimator for the functional $M_{\pi, \leq \zeta}\left(X^{n}\right)$ that retains the leave-a-window-out principle. In particular, recalling our notation from Eq. (14), we generalize the missing mass estimator $\widehat{M}_{\tau}^{(i)}(15)$ via

$$
\widehat{M}_{\tau, \leq \zeta}^{(i)}:=\mathbb{I}\left\{N_{X_{i}}\left(\boldsymbol{X}_{\mathcal{I}_{i}}\right) \leq \zeta\right\}, \quad \text { and construct the estimator } \quad \widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau):=\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \widehat{M}_{\tau, \leq \zeta}^{(j \tau)}
$$

The following theorem shows that the estimator $\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau)$ has small MSE.

Theorem 3. Suppose we choose $\tau \geq \mathrm{t}_{\text {mix }}\left(\left(\mathrm{T}_{\text {mix }} / n\right)^{2} \wedge 1 / 4\right)$, and let $\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau)$ denote the estimator defined in Eq. (23). Then there is an absolute positive constant $C$ such that

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau), M_{\pi, \leq \zeta}\right) \leq C \cdot \frac{(\zeta+1) \tau}{n} \wedge 1
$$

Theorem 3 is proved in Section 7.3; a few remarks on the result follow. First, note that by setting $\zeta=0$, Theorem 3 recovers Theorem 1, our result for missing mass, since the estimator $\widehat{M}_{\text {WINGIT, } \leq 0}(\tau)$ coincides with the missing mass estimator $\widehat{M}_{\text {WINGIT }}(\tau)$. The main technical results that enable this generalization are given by Lemmas 3 and 5 ; the proof is otherwise structured similarly to the proof of Theorem 1. Second, note that $\widehat{M}_{\mathrm{WInGIT}, \leq \zeta}(\tau)$ is an estimate of the stationary mass of all elements occurring at most $\zeta$ times in the sample $X^{n}$, and corresponds to a notion of discovery probability (Favaro et al., 2012). In particular, setting $\tau \asymp \mathrm{T}_{\text {mix }} \log \left(1+n / \mathrm{T}_{\text {mix }}\right)$ yields

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau), M_{\pi, \leq \zeta}\right) \lesssim \frac{(\zeta+1) \mathrm{T}_{\mathrm{mix}}}{n} \cdot \log \left(1+n / \mathrm{T}_{\mathrm{mix}}\right)
$$

To our knowledge, a result equivalent to Eq. (25) with linear dependence on $\zeta+1$ is not directly available in the literature, even in the i.i.d. setting. In fact, it is instructive to revisit the i.i.d. setting for small-count probabilities and compare with the Good-Turing estimator (Good, 1953).

Remark 1. Recalling the notation $\phi_{s}\left(X^{n}\right)$ for the number of elements of the sample space $\mathcal{X}$ that occur $s$ times in $X^{n}$, the Good-Turing estimator for the functional $M_{\pi, \zeta}\left(X^{n}\right)(21)$ is given by $\widehat{M}_{\mathrm{GT}, \zeta}=$ $\frac{\zeta+1}{n} \cdot \phi_{\zeta+1}\left(X^{n}\right)$. The natural estimator for $M_{\pi, \leq \zeta}\left(X^{n}\right)$ is then given by $\widehat{M}_{\mathrm{GT}, \leq \zeta}=\sum_{s=0}^{\zeta} \widehat{M}_{\mathrm{GT}, s}$. Conversely, we obtain an estimator of the exact-count functional $M_{\pi, \zeta}$ from our estimator $\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}$. In particular, we can construct the estimator $\widehat{M}_{\mathrm{WINGIT}, \zeta}(\tau):=\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau)-\widehat{M}_{\mathrm{WINGIT}, \leq(\zeta-1)}(\tau)$, which can be interpreted as writing

$$
\widehat{M}_{\tau, \zeta}^{(i)}:=\mathbb{I}\left\{N_{X_{i}}\left(\boldsymbol{X}_{\mathcal{I}_{i}}\right)=\zeta\right\}, \quad \text { and constructing the estimator } \quad \widehat{M}_{\mathrm{WINGIT}, \zeta}(\tau)=\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \widehat{M}_{\tau, \zeta}^{(j \tau)}
$$

The leave-one-out perspective (McAllester and Schapire, 2001) then yields the following consequence for $\tau=1$ in our estimator: We have $\widehat{M}_{\mathrm{WINGIT}, \zeta}(1)=M_{\mathrm{GT}, \zeta}$, and therefore $\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(1)=M_{\mathrm{GT}, \leq \zeta}$.

Following up on the observation in Remark 1, one can ask if existing analyses of the GoodTuring estimator recover the guarantee of Theorem 3 in the special case of i.i.d. observations. Applying the result of Drukh and Mansour (2005) (which is for the MSE of $\widehat{M}_{\mathrm{GT}, \zeta}$ ) yields

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{GT}, \leq \zeta}, M_{\pi, \leq \zeta}\right) \stackrel{(\mathrm{i})}{\leq} \zeta \sum_{s=0}^{\zeta} \operatorname{MSE}\left(\widehat{M}_{\mathrm{GT}, s}, M_{\pi, s}\right)=\zeta \sum_{s=0}^{\zeta} \frac{\sqrt{s}}{n}+\left(\frac{s}{n}\right)^{2} \lesssim \frac{\zeta^{5 / 2}}{n} \wedge 1
$$

where step (i) follows from the inequality $\left(\sum_{s=0}^{\zeta} a_{s}\right)^{2} \leq \zeta \sum_{s=0}^{\zeta} a_{s}^{2}$. However, setting $\tau=1$ in Theorem 3, we see that Eq. (24) improves the guarantee (26) even in the i.i.d. case, showing that

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{GT}, \leq \zeta}, M_{\pi, \leq \zeta}\right) \stackrel{(\mathrm{i})}{=} \operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(1), M_{\pi, \leq \zeta}\right) \lesssim(\zeta+1) / n
$$

where step (i) follows from Remark 1. The problems of whether the rate (27) and its Markovian analog (25) are information-theoretically optimal for estimating the small-count ${ }^{4}$ probability $M_{\pi, \leq \zeta}$ are interesting and, to our knowledge, open, both in the i.i.d. and Markovian settings.[^3]

## 6 Numerical experiments

In this section, we provide a set of simulations on synthetically constructed Markov chains and on natural language text in order to corroborate our theoretical results, in particular Theorem 1. Before proceeding to the experiments themselves, we describe in Section 6.1 a data-dependent tuning procedure of the window size $\tau$ in the estimator $\widehat{M}_{\mathrm{WINGIT}}(\tau)$.

Code and the text used for the simulations are available at Thangaraj et al. (2024).

### 6.1 Data-dependent tuning of window size $\tau$

Theorem 1 prescribes that we choose the window size $\tau$ to be at least on the order $\mathrm{T}_{\text {mix }} \log (1+$ $\left.n / T_{\text {mix }}\right)$. An important question to address is how to choose the window size $\tau$ when we do not have access to a valid upper bound on $\mathrm{T}_{\text {mix }}$. We now propose a validation procedure to select $\tau$, and test this procedure in the experiments in the sequel. For this section, assume $n$ is divisible by 3 for notational convenience.

Given the sequence $X^{n}$, we choose a candidate window size $\widehat{\tau}$ via the following procedure. We first split the sequence into the first one-third $Z^{(1)}=\left(X_{1}, \ldots, X_{n / 3}\right)$ and the final one-third $Z^{(2)}=\left(X_{2 n / 3+1}, \ldots, X_{n}\right)$ and compute the random variable

$$
\widetilde{M}\left(Z^{(1)}\right)=\frac{1}{(n / 3)} \sum_{i=2 n / 3+1}^{n} \mathbb{I}\left\{X_{i} \notin\left\{X_{1}, \ldots, X_{n / 3}\right\}\right\}
$$

Next, iterate $\tau=1,2,4, \ldots, 2^{\left\lfloor\log _{2}(n / 6)\right\rfloor}$ in increasing order, and compute $\widehat{M}_{\mathrm{WINGIT}}(\tau)$ on the sequence $Z^{(1)}$; denote this random variable by $\widehat{M}_{\text {WINGIT }}\left(Z^{(1)} ; \tau\right)$ for convenience. We then set $\widehat{\tau}$ to be the smallest $\tau$ among this set such that

$$
\left|\widehat{M}_{\mathrm{WINGIT}}\left(Z^{(1)} ; \tau\right)-\widetilde{M}\left(Z^{(1)}\right)\right|^{2} \leq \frac{C_{\mathrm{tune}} \tau}{(n / 3)}
$$

for a suitable choice of the constant $C_{\text {tune }}>0$. If such an inequality is not satisfied for any $\tau$ in the prescribed list, then we set $\widehat{\tau}=n / 6$. Appendix B provides some intuition for why this procedure is reasonable as an automatic tuning method. We next show that empirically, this tuning method is competitive with the optimally chosen window size.

### 6.2 Experiments on simulated Markov chains and natural language text

For the simulated Markov and natural language text sequences considered in this section, we vary the sequence length $n$ and plot the MSE of the estimator $\widehat{M}_{\text {WINGIT }}(\tau)$ as a function of $n$ for different values of the window size $\tau$. We also plot the MSE of the tuned estimator $\widehat{M}_{\text {WINGIT }}(\widehat{\tau})$. Note that the special case $\tau=1$ corresponds to the Good-Turing estimator (7). We also plot (in dashed lines) the result of the tuning procedure that we described in Section 6.1, with the constant $C_{\text {tune }}=1$. Every point in these plots is generated by averaging the results of multiple sequences generated from the source.

First, and as a sanity check, we consider the case of the trivial Markov chain formed by i.i.d. samples. For generating $n$ samples, we consider the uniform distribution over the state space $\mathcal{X}=\{1,2, \ldots,\lfloor 1.2 n\rfloor\}$, which is close to the worst-case distribution for the Good-Turing estimator. Moreover, this ensures that the missing mass $M_{\pi}\left(X^{n}\right)$ is significant. Figure 1 shows two plots. The


Figure 1: IID Uniform([1.2n]) for $n$ samples, averaged over 100 trajectories.

plot on the left is that of the MSE of the estimator $\widehat{M}_{\text {WINGIT }}(\tau)$ as a function of sequence length $n$ for various values of the window size $\tau$ and for tuned $\widehat{\tau}$. The plot on the right shows the mean values (over the 100 runs) of the triple of random variables $\left(M_{\pi}, \widehat{M}(1), \widehat{M}(\widehat{\tau})\right.$ ) along with the 90 percentile confidence bar (5th to 95th percentile). Observe that on the one hand - and as expected in the i.i.d. setting with mixing time $\mathrm{T}_{\text {mix }}=1$ - the minimum MSE is attained when $\tau=1$, i.e., by the vanilla Good-Turing estimator (7). On the other hand, the MSE is only marginally higher for higher values of the window size $\tau$, and all estimators appear to enjoy the same rate of decay of MSE in the sequence length $n$. In other words, the effect of misspecifying $\tau$ appears as a multiplicative constant in the error, as predicted by Theorem 1. The MSE of $\widehat{M}(\widehat{\tau})$ with tuned $\widehat{\tau}$ (dashed line) is close to the minimum attained MSE. In the plot to the right, the mean values of missing mass $M_{\pi}$ and the estimators $\widehat{M}(1), \widehat{M}(\widehat{\tau})$ are almost overlapping for all $n$. The confidence bars for the three quantities are shown as a wide blue bar for $M_{\pi}$, an orange bar for $\widehat{M}(1)$ and as a capped black line for $\widehat{M}(\widehat{\tau})$. The confidence bars, narrow to begin with, shrink to negligible lengths as $n$ increases.

In our second experiment, we once again consider the state space $\mathcal{X}=\{1, \ldots,\lfloor 1.2 n\rfloor\}$. We simulate the sticky Markov chain (10) with $p=0.5$ and stationary distribution given by the uniform distribution on $\mathcal{X}$, i.e., $\pi_{x}=\frac{1}{[1.2 n]}$ for all $x \in \mathcal{X}$. As before, we simulate the performance of the WINGIT estimator as a function of $n$ for different values of window size $\tau$, and present our results in Figure 2. In the MSE plot to the left, we observe the following. In contrast to the previous i.i.d. example, we now find that the choice $\tau=1$ is a poor one, and that the error of the estimator does not decay with the sample size $n$. As expected from the analysis presented in Section 2, the vanilla Good-Turing estimator (7) indeed suffers a constant bias in this setting. Note that by Lemma 1, the mixing time of this chain is bounded as $\mathrm{T}_{\text {mix }} \in[1,4]$, and Theorem 1 predicts that the estimator should succeed when the window size is larger than $T_{\text {mix }}$. This prediction is borne out in simulation: While the estimator exhibits constant bias even when $\tau=4$, when $\tau=8$ the MSE suddenly becomes consistent in $n$. Further increases in the window size $\tau$ preserve the consistency of the estimator while increasing the MSE by multiplicative constant factors. In the plot to the right in Figure 2, we see that the mean value of missing mass coincides with the mean value of


Figure 2: $\operatorname{Sticky}(0.5)$ with $\pi=\operatorname{Uniform}([1.2 n])$ for $n$ samples, averaged over 100 trajectories.

both the estimators (one with $\tau=8$ and the other with tuned window size) for larger values of $n$. For $n<2000$, the mean of the estimator $\widehat{M}_{\mathrm{WINGIT}}(8)$ almost coincides with missing mass, while the mean of $\widehat{M}_{\text {WINGIT }}(\widehat{\tau})$ is smaller. The confidence bars for both estimators are wider than that of the missing mass for $n<2000$ though they narrow quickly as $n$ grows. These observations suggest that the tuning procedure could be possibly improved, particularly for small $n$.


Figure 3. $\operatorname{Sticky}(\bar{p})$ with $\pi=\operatorname{Uniform}([1.2 n])$ for $n$ samples, 100 trajectories. Compared to Eq. (10), we have reparameterized as $\bar{p}=1-p$. To reduce clutter, confidence bar is shown only for $\widehat{M}_{\text {WInGIT }}(\widehat{\tau})$.

In our next experiment, we simulate the sticky Markov chain (10) with $\bar{p} \triangleq 1-p=0.1,0.5,0.9$ setting the state space and stationary distribution as before. The aim of this experiment is to examine more closely the influence of the stickiness parameter $\bar{p}$ on the optimal choice of window size $\tau$. The same simulations are performed and results are compared in Figure 3. The best
(power of 2) window sizes for $\bar{p}=0.1,0.5,0.9$ are observed through simulations to be, respectively, $\tau=4,8,64$. The plot to the left shows the MSE of $\widehat{M}_{\mathrm{WINGIT}}(\tau)$ for the best observed window size (called "best") and for the data-tuned window size $\widehat{\tau}$ (called "tuned"). For the least sticky chain $(\bar{p}=0.1)$, the tuned and the best estimators have overlapping MSEs for all $n$. As stickiness increases, the MSE of the tuned estimator marginally deviates from the best for small $n$. For highly sticky chains $(\bar{p}=0.9)$, the deviation persists for significantly longer. The plot to the right shows mean values and confidence bars (for the tuned estimator alone) for all three values of $\bar{p}$. The best estimator is close in mean to missing mass for all $n$ for all $\bar{p}$. As stickiness increases, the tuning procedure appears to require increasingly larger values of $n$ for good accuracy.

In our final experiment, presented in Figure 4, we consider the text of the novel $A$ Tale of Two Cities by Charles Dickens accessed through Project Gutenberg (Dickens, 1994). All auxiliary content (preface, table of contents, chapter titles, Project Gutenberg related text) were removed and only the novel text was retained. This text was tokenized and all punctuation was removed. Titles (Miss, Mr. etc.) and names of characters that occurred as collocations with high frequency (10 of them) were merged into single tokens. The result was a sequence of $N=136092$ tokens, numbered from 0 to $N-1$, with a vocabulary $\mathcal{X}$ (unique tokens) of size $|\mathcal{X}|=10542$. For defining missing mass $M_{\pi}$, the overall frequency distribution of the $N$ tokens was taken to be the stationary distribution $\pi$. A consecutive sequence of $n$ tokens (Token $s+1$ to Token $s+n$ with starting point $s)$ is considered as a trajectory of length $n$, i.e. $X^{n}$. For a given length $n$, approximately $15 N / n$ trajectories were considered in the simulations with their starting points separated by $n / 15$. An important feature of this data is that the Markov assumption (also known as the bigram assumption in this literature) is clearly violated, since we expect the text to have longer-range dependencies. In any case, we can run our estimator for the missing mass and compare it to the true missing mass, which can still be computed from the sequence once the stationary probability is fixed.


Figure 4. Text of 'A Tale of Two Cities' by Charles Dickens, Vocabulary: 10542 words, Trajectories: sequences of $n$ words from text.

In Figure 4, we show the MSE in the plot to the left and the means with confidence bars to the right. Interestingly, all of the choices of $\tau$ that we consider yield similar MSE performance for the WINGIT estimator, and all of these choices appear to have a super-linear rate of decay with the



Figure 5. Schematic showing our block notation for assistance with the proof. For the various values $j \in\left[n_{0}\right]$, the index $i=j \tau$ is shown in black and the window of size $\tau-1$ on either size of it is excluded when computing the estimator $\widehat{M}_{\tau}^{(j)}$. For each value of $j$ and $i=j \tau$, the indices in color form the sets $\mathcal{D}_{i}=\mathcal{B}_{j}$, while the indices in white form the sets $\mathcal{I}_{i}=\mathcal{H}_{j}$. In Eq. (32) below, we define the sets $S_{j}:=\left\{\ell \in\left[n_{0}\right]:|\ell-j| \bmod 3 \equiv 0\right\}$ for each $j \in\left[n_{0}\right]$; let us use this figure to explain the intuition behind this definition. Take for instance $j=1$; in this case, we have $S_{j}=\{1,4\}$. In particular, it is clear that the largest colored block in the sequence with $j=1$ is separated from the smallest colored block of $S_{j} \backslash\{j\}$ by 3 indices, which is greater than $\tau$. This fact is used crucially in Lemma 8, and allows to construct a surrogate process of restarted Markov chains for large $\tau$.

sample size $n$. The reason for the difference in rate of decay could be because we hold $|\mathcal{X}|$ constant as we increase $n$ in the text simulations resulting in a decrease in $M_{\pi}$ with $n$. This decrease is confirmed in the plot on the right, where we see that the mean of missing mass falls from about 0.45 for $n=600$ to about 0.1 for $n=19200$. Further, from the right plot, we observe that the tuned estimator and $\tau=32$ estimator are close to each other in mean, while deviating a bit from the mean of missing mass for small $n$. The aforementioned long-range dependencies in the text are likely to be causing this minor deviation. In any case, the estimator $\widehat{M}_{\text {WINGIT }}(\widehat{\tau})$ appears to be accurate for all $n$. Overall, our experiments on this corpus demonstrate that the missing mass estimator is robust to model misspecification, and can work well even for non-Markovian sources.

## 7 Proofs

In this section, we present proofs of the main theorems. Technical lemmas are frequently referenced in these proofs, and their statements and proofs can be found in Appendix A.

Recall that $n_{0}=\lfloor n / \tau\rfloor$; we will drop the floor notation henceforth for readability. Also recall our index sets from Eq. (14). For $j \in\left[n_{0}\right]$, define the sets $\mathcal{B}_{j}:=\mathcal{D}_{j \tau}$ and $\mathcal{H}_{j}:=\mathcal{I}_{j \tau}$ as the "dependent" and "independent" indices, respectively, for the $j$-th window, or block, of size (at most) $2 \tau-1$. Mnemonically, one should view $\mathcal{B}_{j}$ as the $j$-th block of indices and $\mathcal{H}_{j}=[n] \backslash \mathcal{B}_{j}$ as the set of indices having a hole at block $j$. As convention, we will use $i \in[n]$ to index individual samples and $j \in\left[n_{0}\right]$ to index the various windows or blocks. See Figure 5 for an illustration.

### 7.1 Proof of Theorem 1

In the case $n / \tau \leq 9$, the theorem is immediate since the RHS of the claim is minimized by 1 . We therefore focus on the complementary case $n / \tau=n_{0} \geq 9$ for the entire proof. Note that in this case, we also have $n \geq 9 \mathrm{~T}_{\text {mix }}$.

Viewing $X^{n}$ as fixed for the moment and writing out our estimator $\widehat{M}_{\text {WINGIT }}(\tau)=\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \widehat{M}_{\tau}^{(j \tau)}$, we have that $\frac{1}{2}\left|\widehat{M}_{\text {WINGIT }}(\tau)-M_{\pi}\left(X^{n}\right)\right|^{2}$ is equal to

$$
\begin{aligned}
& \frac{1}{2} \cdot\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{[n]}\right\}\right|^{2} \\
& \leq \underbrace{\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}}\left(\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{[n]}\right\}\right)\right|^{2}}_{T_{1}} \\
& +\underbrace{\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}}\left(\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{\substack{Y \sim X^{n} \\
Y \Perp}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right)\right|^{2}}_{T_{2}}
\end{aligned}
$$


$M_{\pi}\left(X^{n}\right) \mid$ and used the inequality $\frac{1}{2}(a+b)^{2} \leq\left(a^{2}+b^{2}\right)$. Recall that $\boldsymbol{X}_{[n]}=\left\{X_{1}, \ldots, X_{n}\right\}$ is the set (not sequence) of all random variables. We start by bounding $\mathbb{E}\left[T_{1}\right]$, noting that $T_{1}$ resembles a conditional squared bias term.

Bounding $\mathbb{E}\left[T_{1}\right]$ : Using the inequality $\frac{1}{n_{0}}\left(\sum_{j=1}^{n_{0}} a_{j}\right)^{2} \leq \sum_{j=1}^{n_{0}} a_{j}^{2}$, we have

$$
\begin{aligned}
& \mathbb{E}\left[T_{1}\right] \leq \frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \underset{X^{n}}{\mathbb{E}}\left(\underset{\substack{Y \sim \pi^{n} \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{[n]}\right\}\right)^{2} \\
& \leq \max _{j \in\left[n_{0}\right]} \underset{X^{n}}{\mathbb{E}}\left(\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{[n]}\right\}\right)^{2}
\end{aligned}
$$

For any $j \in\left[n_{0}\right]$, we further have





where step (i) follows from Lemma 2 and step (ii) uses the fact that

$$
0 \leq \underset{\substack{Y \sim \pi^{n} \\ Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\} \leq 1
$$

We now proceed to uniformly bound $\mathbb{E}_{X^{n}} \mathbb{E}_{Y^{Y} \sim X^{n}} \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}$ for any $j \in\left[n_{0}\right]$, and drop the subscripts in the expectation from here on for convenience. The key observation is that since $\bigcup_{\ell \in\left[n_{0}\right] \backslash j} \mathcal{B}_{\ell} \subseteq \mathcal{H}_{j}$, we can write

$$
\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\} \leq \prod_{\ell \in\left[n_{0}\right] \backslash j} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{B}_{\ell}}\right\} \leq \prod_{\substack{\ell \in\left[n_{0}\right] \backslash j \\|\ell-j| \bmod 3 \equiv 0}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{B}_{\ell}}\right\}
$$

We define

$$
S_{j}:=\left\{\ell \in\left[n_{0}\right]:|\ell-j| \quad \bmod 3 \equiv 0\right\}
$$

as shorthand (see Figure 5 for an illustration), and define the set

$$
W_{j}:=\bigcup_{\ell \in S_{j} \backslash\{j\}} \boldsymbol{X}_{\mathcal{B}_{\ell}}
$$

Recalling our notation $\oplus$ for concatenation of sequences, we also define the corresponding sequence

$$
W_{j}:=\bigoplus_{\ell \in S_{j} \backslash\{j\}} X_{\mathcal{B}_{\ell}}
$$

Using Eq. (31) and this new notation, we can write

$$
\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\} \leq \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{W}_{j}\right\}
$$

Now define the auxiliary sequence of random variables

$$
W_{j}^{\prime}:=\bigoplus_{\ell \in S_{j} \backslash\{j\}} X_{\mathcal{B}_{\ell}}^{\prime}
$$

where each $X_{\mathcal{B}_{\ell}}^{\prime}$ is a Markov chain initialized at stationary distribution $\pi$ and drawn independently of everything else. The sequence $W_{j}^{\prime}$ can thus be viewed as a concatenation of several independent Markov chains. Following parallel notation to above, let $\boldsymbol{W}_{j}^{\prime}$ denote the set containing elements in $W_{j}^{\prime}$. By assumption, we have $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$ for $\epsilon=\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2} \leq 1 / 81$. Applying Lemma 8 yields

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{W}_{j}\right\}\right] \leq \mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{W}_{j}^{\prime}\right\}\right]+n_{0} \epsilon
$$

But since $W_{j}^{\prime}$ is a concatenation of independent Markov chains and is also independent of the Markov chain $X_{\mathcal{B}_{j}}$, applying Lemma 4 with $k=\left|S_{j} \backslash\{j\}\right|$ yields

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{W}_{j}^{\prime}\right\}\right] \leq \frac{1}{k} \leq \frac{3}{n_{0}-3}
$$

where we have used the fact that, by definition, $\left|S_{j} \backslash\{j\}\right| \geq \frac{n_{0}}{3}-1$. Putting all of the pieces together and substituting $\epsilon=\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2}$, we have

$$
\mathbb{E}\left[T_{1}\right] \leq \frac{3}{n_{0}-3}+n_{0} \cdot\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2} \stackrel{(\mathrm{i})}{\lesssim} \frac{\tau}{n}
$$

where step (i) follows because $\tau \geq \mathrm{T}_{\text {mix }}$ and $n_{0} \geq 9$.

Bounding $\mathbb{E}\left[T_{2}\right]$ : We note that $T_{2}$ resembles a conditional variance term. Define the random variables $Z_{j}:=\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\mathbb{E}_{Y \Perp X^{n}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}$ for all $j \in\left[n_{0}\right]$ as shorthand. Then we have

$$
\mathbb{E}\left[T_{2}\right]=\frac{1}{n_{0}^{2}} \sum_{j, k=1}^{n_{0}} \mathbb{E}\left[Z_{j} Z_{k}\right] \leq \frac{1}{n_{0}}+\frac{1}{n_{0}^{2}} \sum_{j \neq k} \mathbb{E}\left[Z_{j} Z_{k}\right]
$$

where the inequality follows since $Z_{j} \in[-1,1]$ for all $j \in\left[n_{0}\right]$. Therefore, it suffices to bound the cross terms $\mathbb{E}\left[Z_{j} Z_{k}\right]$ for $j \neq k$. We have

$$
\begin{aligned}
\mathbb{E}\left[Z_{j} Z_{k}\right]= & \underbrace{\mathbb{E}\left[\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\} \cdot \mathbb{I}\left\{X_{k \tau} \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]}_{U_{1}}-\underbrace{\mathbb{E}\left[\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \cdot \mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]}_{U_{3}} \\
& -\underbrace{\mathbb{E}\left[\mathbb{I}\left\{X_{k \tau} \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right] \cdot \mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right]}_{U_{2}}+\underbrace{\mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \cdot \mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]}_{U_{4}}
\end{aligned}
$$

Let $\left(X_{1}^{\prime}, X_{2}^{\prime}, \ldots, X_{n}^{\prime}\right.$ ) denote a sequence of $n$ random variables drawn i.i.d. from $\pi$, and independently of everything else. Note that $Y$ can also be viewed as an additional such draw. Once again noting that $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$ for $\epsilon=\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2}$, we may apply Lemma 6 to obtain

$$
\mathbb{E}\left[\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \geq \mathbb{E}\left[\mathbb{I}\left\{X_{j \tau}^{\prime} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right]-4 \epsilon=\mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right]-4 \epsilon
$$

and similarly,

$$
\mathbb{E}\left[\mathbb{I}\left\{X_{k \tau} \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right] \geq \mathbb{E}\left[\mathbb{I}\left\{X_{k \tau}^{\prime} \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]-4 \epsilon=\mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]-4 \epsilon
$$

Noting that $\mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \leq 1$ (and similarly for $\mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]$, the above two displays imply that $U_{2} \geq U_{4}-4 \epsilon$ and $U_{3} \geq U_{4}-4 \epsilon$. Applying this to Eq.(37) yields

$$
\mathbb{E}\left[Z_{j} Z_{k}\right] \leq \underbrace{\mathbb{E}\left[\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\} \cdot \mathbb{I}\left\{X_{k \tau} \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]}_{U_{1}}-\underbrace{\mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \cdot \mathbb{E}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]}_{U_{4}}+8 \epsilon
$$

Looking at the first term of Eq. (38) and using Lemma 7, we have

$$
\begin{aligned}
U_{1} & \leq \mathbb{E}\left[\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\} \cdot \mathbb{I}\left\{X_{k \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right] \\
& \leq \mathbb{E}\left[\mathbb{I}\left\{X_{j \tau}^{\prime} \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\} \cdot \mathbb{I}\left\{X_{k \tau}^{\prime} \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right]+8 \epsilon \\
& \left.\stackrel{(\mathrm{i})}{=} \underset{\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}}{\mathbb{E}}\left\{\underset{X_{j \tau}^{\prime}}{\mathbb{E}}\left[\mathbb{I}\left\{X_{j \tau}^{\prime} \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right] \cdot \underset{X_{k \tau}^{\prime}}{\mathbb{E}} \mathbb{I}\left\{X_{k \tau}^{\prime} \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right]\right\}+8 \epsilon \\
& =\underset{\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}}{\mathbb{E}}\left\{\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right] \cdot \underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right]\right\}+8 \epsilon
\end{aligned}
$$

where step (i) follows because $X_{j \tau}^{\prime}$ and $X_{k \tau}^{\prime}$ are independent of everything else.

Taking stock, it remains to bound the expectation of the term

$$
\begin{aligned}
& T\left(\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}\right):=\left.\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right] \cdot \underset{Y}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}-\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \cdot \underset{Y}{\mathbb{I}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right] \\
&=\left(\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right]\right) \cdot \underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right] \\
&\left.+\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right] \cdot\left(\frac{\mathbb{E}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right]\right)
\end{aligned}
$$

We now characterize $\mathbb{E}_{Y}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right]$. By Lemma 2, we have

$$
\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right]=\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{H}_{j} \backslash \mathcal{H}_{k}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}\right]
$$

Next, note that $\mathcal{H}_{j} \backslash \mathcal{H}_{k}=\mathcal{B}_{k}$ and $\mathcal{H}_{j} \cap \mathcal{H}_{k}=[n] \backslash\left\{\mathcal{B}_{j} \cup \mathcal{B}_{k}\right\}$. Therefore, we have

$$
\begin{aligned}
\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{H}_{j} \backslash \mathcal{H}_{k}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\} & =\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{k}}\right\} \cdot \prod_{\ell \neq j, k} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{B}_{\ell}}\right\} \\
& \leq \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{k}}\right\} \cdot \prod_{\ell \in S_{j} \backslash\{j, k\}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{B}_{\ell}}\right\}
\end{aligned}
$$

In the above, recall that we defined $S_{j}:=\left\{\ell \in\left[n_{0}\right]:|\ell-j| \bmod 3 \equiv 0\right\}$. Note that $\left|S_{j} \backslash\{j, k\}\right| \geq$ $n_{0} / 3-2$. Using the same argument as in the proof of bounding $\mathbb{E}\left[T_{1}\right]$ (see Eqs. (31)-(36)), we have

$$
\begin{aligned}
\mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{k}}\right\} \cdot \prod_{\ell \in S_{j} \backslash\{j, k\}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{B}_{\ell}}\right\}\right] & \leq \frac{1}{\left|S_{j} \backslash\{j, k\}\right|}+n_{0} \epsilon \\
& \leq \frac{3}{n_{0}-6}+n_{0} \epsilon
\end{aligned}
$$

For the second term in Eq. (43), an identical argument yields

$$
\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{k}}\right\}\right] \leq \frac{3}{n_{0}-6}+n_{0} \epsilon
$$

so that for each $(j, k)$ pair, we have

$$
\mathbb{E} T\left(\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}\right) \lesssim \frac{3}{n_{0}-6}+n_{0} \epsilon
$$

Putting together the pieces, we then have $\mathbb{E}\left[Z_{j} Z_{k}\right] \lesssim \frac{3}{n_{0}-6}+n_{0} \epsilon+16 \epsilon$.

Substituting $\epsilon=\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2}$ and noting that $\tau \geq \mathrm{T}_{\text {mix }}$ and $n_{0} \geq 9$, we obtain $\mathbb{E}\left[Z_{j} Z_{k}\right] \lesssim \frac{\tau}{n}$. Averaging over all $j \neq k$ completes the proof of the fact $\mathbb{E}\left[T_{2}\right] \leq C \cdot \frac{\tau}{n} \wedge 1$.

We conclude by putting together our bounds on $\mathbb{E}\left[T_{1}\right]$ and $\mathbb{E}\left[T_{2}\right]$.

### 7.2 Proof of Theorem 2

Via a decomposition similar to Eq. (19), we obtain

$\operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right) \leq 3 \cdot \operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}}(\tau), M_{\pi}\left(X^{n}\right)\right)+3\left|\underset{X^{n}}{\mathbb{E}}\left[\widehat{M}_{\mathrm{WINGIT}}(\tau)-M_{\pi}\left(X^{n}\right)\right]\right|^{2}+3 \operatorname{var}\left(\widehat{M}_{\mathrm{WINGIT}}(\tau)\right)$.

Above, the first term corresponds to the MSE of the estimator $\widehat{M}_{\text {WINGIT }}$, the second term corresponds to a squared bias term, and the third term corresponds to the variance of the estimator $\widehat{M}_{\text {WINGIT }}$. Throughout this proof, we will choose $\tau=\mathrm{t}_{\text {mix }}\left(\left(\mathrm{T}_{\text {mix }} / n\right)^{2} \wedge 1 / 4\right) \lesssim \mathrm{T}_{\text {mix }} \cdot \log \left(1+n / \mathrm{T}_{\text {mix }}\right)$, where the last inequality holds due to Eq. (6).

Bounding MSE: Applying Theorem 1 yields the direct bound

$$
\operatorname{MSE}\left(\widehat{M}_{\mathrm{WINGIT}}(\tau), M_{\pi}\left(X^{n}\right)\right) \lesssim \tau / n \lesssim \frac{\mathrm{T}_{\mathrm{mix}}}{n} \cdot \log \left(1+n / \mathrm{T}_{\mathrm{mix}}\right)
$$

It remains to bound the squared bias and variance terms on the RHS of Ineq. (45).

Bounding squared bias: Note that it suffices to bound the positive term $\mathbb{E}\left[\widehat{M}_{\tau}^{(j \tau)}\right]-\mathbb{E}\left[M_{\pi}\left(X^{n}\right)\right]$ for each $j \in\left[n_{0}\right]$. Write

$$
\begin{aligned}
\mathbb{E}\left[\widehat{M}_{\tau}^{(j \tau)}\right]-\mathbb{E}\left[M_{\pi}\left(X^{n}\right)\right]= & \underset{X^{n}}{\mathbb{E}} \underset{Y \sim \pi}{Y}\left[\mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{[n]}\right\}\right] \\
& \stackrel{(\mathrm{i})}{=} \underset{X^{n}}{\mathbb{E}} \underset{Y \sim \pi}{\mathbb{E}}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right],
\end{aligned}
$$

where step (i) follows from Lemma 2.

By executing the same steps that we used to bound the term in Eq. (30), we have

$$
\mathbb{E}\left[\widehat{M}_{\tau}^{(j \tau)}\right]-\mathbb{E}\left[M_{\pi}\left(X^{n}\right)\right] \leq C \cdot \frac{\tau}{n} \lesssim \frac{\mathrm{T}_{\text {mix }}}{n} \cdot \log \left(1+n / \mathrm{T}_{\text {mix }}\right)
$$

where the final bound holds owing to the choice $\tau \asymp T_{\text {mix }} \cdot \log \left(1+n / T_{\text {mix }}\right)$. We are eventually interested in the squared bias, so we have

$$
\left|\underset{X^{n}}{\mathbb{E}}\left[\widehat{M}_{\mathrm{WINGIT}}(\tau)-M_{\pi}\left(X^{n}\right)\right]\right|^{2} \lesssim\left(\frac{\mathrm{T}_{\text {mix }}}{n} \cdot \log \left(1+n / \mathrm{T}_{\text {mix }}\right)\right)^{2}
$$

Bounding variance: We have

$$
\begin{aligned}
& \operatorname{var}\left(\widehat{M}_{\mathrm{WINGIT}}(\tau)\right)=\underset{X^{n}}{\mathbb{E}}\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}}\left(\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{X^{n}}{\mathbb{E}} \underset{Y \sim X^{n}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right)\right|^{2} \\
& \stackrel{\text { (i) }}{\leq} \underset{X^{n}}{\mathbb{E}}\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}}\left(\mathbb{I}\left\{X_{j \tau} \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \notin \boldsymbol{X}_{\mathcal{H}_{j}}\right\}\right)\right|^{2} \stackrel{(\mathrm{ii})}{=} \mathbb{E}\left[T_{2}\right] .
\end{aligned}
$$

Here step (i) follows from Jensen's inequality and step (ii) uses the definition of the term $T_{2}$ from Section 7.1. But we know from that proof that $\mathbb{E}\left[T_{2}\right] \lesssim \tau / n$, which is in turn bounded by $C \frac{\mathrm{T}_{\text {mix }}}{n} \cdot \log \left(1+n / \mathrm{T}_{\text {mix }}\right)$ for the choice $\tau \asymp \mathrm{T}_{\text {mix }} \cdot \log \left(1+n / \mathrm{T}_{\text {mix }}\right)$.

Putting together the bounds on MSE, squared bias, and variance thus yields

$$
\operatorname{var}\left(M_{\pi}\left(X^{n}\right)\right) \leq C \cdot \frac{\mathrm{T}_{\text {mix }}}{n} \cdot \log \left(1+n / \mathrm{T}_{\text {mix }}\right) \wedge 1
$$

as desired.

### 7.3 Proof of Theorem 3

The structure of this proof parallels the proof of Theorem 1; the reader is advised to read that proof first. As in that proof, if $n / \tau \leq 9$ then the theorem is immediate since the RHS of the claim is minimized by 1 . We therefore focus on the complementary case $n / \tau=n_{0} \geq 9$ for the entire proof. Note that in this case, we also have $n \geq 9 T_{\text {mix }}$.

We next proceed via a series of steps that resembles the proof of Theorem 1. Recall the notation $N_{x}\left(\boldsymbol{X}_{P}\right), N_{x}\left(X_{P}\right)$ that we defined in Section 5. Viewing $X^{n}$ as fixed for the moment and writing out our estimator $\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau):=\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \widehat{M}_{\tau, \leq \zeta}^{(j \tau)}$, a series of steps identical to Eq. (29) yield that $\frac{1}{2}\left|\widehat{M}_{\mathrm{WINGIT}, \leq \zeta}(\tau)-M_{\pi, \leq \zeta}\left(X^{n}\right)\right|^{2}$ is equal to

$$
\begin{aligned}
& \frac{1}{2} \cdot\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}} \mathbb{I}\left\{N_{X_{j \tau}}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(X^{n}\right) \leq \zeta\right\}\right|^{2} \\
& \leq \underbrace{\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}}\left(\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(X^{n}\right) \leq \zeta\right\}\right)\right|^{2}}_{T_{1}^{\prime}} \\
& +\underbrace{\left|\frac{1}{n_{0}} \sum_{j=1}^{n_{0}}\left(\mathbb{I}\left\{N_{X_{j \tau}}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}-\underset{\substack{Y \sim \pi \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right)\right|^{2}}_{T_{2}^{\prime}}
\end{aligned}
$$

As in the proof of Theorem 1, we upper bound $\mathbb{E}\left[T_{1}^{\prime}\right]$ and $\mathbb{E}\left[T_{2}^{\prime}\right]$.

Bounding $\mathbb{E}\left[T_{1}^{\prime}\right]$ : An identical argument to the proof of Theorem 1 gives

$$
\mathbb{E}\left[T_{1}^{\prime}\right] \leq \max _{j \in\left[n_{0}\right] X^{n}}^{\mathbb{E}}\left(\underset{\substack{Y \\ Y^{Y} \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}-\underset{\substack{Y \\ Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(X^{n}\right) \leq \zeta\right\}\right)^{2}
$$

For any $j \in\left[n_{0}\right]$, we further have

$$
\begin{aligned}
& \underset{X^{n}}{\mathbb{E}}\left(\underset{\underset{Y}{Y \sim X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}-\underset{\substack{Y \sim \pi^{n} \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{N_{Y}\left(X^{n}\right) \leq \zeta\right\}\right)^{2} \stackrel{(\mathrm{i})}{\leq} \underset{X^{n}}{\mathbb{E}}\left(\underset{\substack{Y \sim X^{n} \\
Y \Perp X^{n}}}{\mathbb{E}} \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right)^{2} \\
& \stackrel{(i i)}{\leq} \underset{X^{n}}{\mathbb{E}} \underset{Y \sim \pi}{Y} \mathbb{Y} \underset{Y X^{n}}{\mathbb{E}} \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}
\end{aligned}
$$

where step (i) follows from Lemma 3 and step (ii) follows because, as in the proof of Theorem 1, the expectation of a product of indicator random variables is between 0 and 1 .

We now proceed to uniformly bound $\mathbb{E}_{X^{n}} \mathbb{E}_{Y_{Y \sim \pi^{n}}} \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}$ for any $j \in$ $\left[n_{0}\right]$, and drop the subscripts in the expectation from here on for convenience. Recall the definitions of the set $\boldsymbol{W}_{j}$ and the corresponding sequence $W_{j}$ from Eqs. (33) and (34). Note that, since $\boldsymbol{W}_{j} \subset \boldsymbol{X}_{\mathcal{H}_{j}}$, we can write

$$
\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\} \leq \mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{W}_{j}\right) \leq \zeta\right\}
$$

We also recall the definition of the auxiliary sequence $W_{j}^{\prime}$ (and the corresponding set notation $\boldsymbol{W}_{j}^{\prime}$ ) in Eq. (35). Since $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$ for $\epsilon=\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2}$, we can again apply Lemma 8 to yield

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{W}_{j}\right) \leq \zeta\right\}\right] \leq \mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{W}_{j}^{\prime}\right) \leq \zeta\right\}\right]+n_{0} \epsilon
$$

Now, since $W_{j}^{\prime}$ is a concatenation of independent Markov chains and is also independent of the Markov chain $X_{\mathcal{B}_{j}}$, applying Lemma 5 (which is a generalization of Lemma 4) with $k=\left|S_{j} \backslash\{j\}\right|$ yields

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{j}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{W}_{j}^{\prime}\right) \leq \zeta\right\}\right] \leq \frac{\zeta+1}{k} \leq \frac{3(\zeta+1)}{n_{0}-3}
$$

Putting all of the pieces together in a similar manner to the proof of Theorem 1, we obtain

$$
\mathbb{E}\left[T_{1}^{\prime}\right] \leq \frac{3(\zeta+1)}{n_{0}-3}+n_{0} \cdot\left(\frac{\mathrm{T}_{\mathrm{mix}}}{n}\right)^{2} \lesssim \frac{\tau(\zeta+1)}{n}
$$

Bounding $\mathbb{E}\left[T_{2}^{\prime}\right]$ : We now define, for all $j \in\left[n_{0}\right]$, the random variables



Then we have, as before,

$$
\mathbb{E}\left[T_{2}^{\prime}\right] \leq \frac{1}{n_{0}}+\frac{1}{n_{0}^{2}} \sum_{j \neq k} \mathbb{E}\left[Z_{j}^{\prime} Z_{k}^{\prime}\right]
$$

We then follow a series of steps identical to Eqs. (37)-(38) to obtain

$\mathbb{E}\left[Z_{j}^{\prime} Z_{k}^{\prime}\right] \leq \underbrace{\mathbb{E}\left[\mathbb{I}\left\{N_{X_{j \tau}}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\} \cdot \mathbb{I}\left\{N_{X_{k \tau}}\left(\boldsymbol{X}_{\mathcal{H}_{k}}\right) \leq \zeta\right\}\right]}_{U_{1}^{\prime}}-\underbrace{\mathbb{E}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{k}}\right) \leq \zeta\right\}\right]}_{U_{2}^{\prime}}$.

We start with analyzing $U_{1}^{\prime}$. We have

$$
\begin{aligned}
& U_{1}^{\prime} \leq \mathbb{E}\left[\mathbb{I}\left\{N_{X_{j \tau}}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\} \cdot \mathbb{I}\left\{N_{X_{k \tau}}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \\
& \stackrel{(\mathrm{i})}{\leq} \mathbb{E}\left[\mathbb{I}\left\{N_{X_{j \tau}^{\prime}}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\} \cdot \mathbb{I}\left\{N_{X_{k \tau}^{\prime}}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right]+8 \epsilon \\
& \stackrel{(\mathrm{ii})}{=} \underset{\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}}{\mathbb{E}}\left\{\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \cdot \underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right]\right\}+8 \epsilon
\end{aligned}
$$

where step (i) follows from Lemma 7 and step (ii) uses the independence of $X_{j \tau}^{\prime}, X_{k \tau}^{\prime}$ from everything else. Thus, it suffices to upper bound the expectation of the term

$$
\begin{aligned}
& T^{\prime}\left(\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}\right):=\underset{Y}{\mathbb{E}}[\mathbb{I}\{\left.\left.N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \cdot \underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \\
&-\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right] \cdot \underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \\
&=\left(\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right]\right) \cdot \underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \\
&+\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right]\left(\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{k}}\right) \leq \zeta\right\}\right]\right)
\end{aligned}
$$

We next upper bound the term $\mathbb{E}_{Y}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right]$, noting that the term $\mathbb{E}_{Y}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{k}}\right) \leq \zeta\right\}\right]$ can be identically controlled. Applying Lemma 3 with $P:=\mathcal{H}_{j} \cap \mathcal{H}_{k}$ and $Q:=\mathcal{H}_{j}$ yields

$$
\begin{aligned}
\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right] & \leq \mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{H}_{j} \backslash \mathcal{H}_{k}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \\
& =\mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{k}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}\right] \\
& \stackrel{\text { (i) }}{\leq} \mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{k}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{W}_{j, k}\right) \leq \zeta\right\}\right]
\end{aligned}
$$

Above, we defined $\boldsymbol{W}_{j, k}:=\bigcup_{\ell \in S_{j} \backslash\{j, k\}} \boldsymbol{X}_{\mathcal{B}_{\ell}}$ and the corresponding sequence notation as $W_{j, k}:=$ $\bigoplus_{\ell \in S_{j} \backslash\{j, k\}} X_{\mathcal{B}_{\ell}}$, and step (i) followed because $\boldsymbol{W}_{j, k} \subseteq \boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}$. We define the corresponding sequences of iid Markov chains

$$
\begin{aligned}
\boldsymbol{W}_{j, k}^{\prime} & :=\bigcup_{\ell \in S_{j} \backslash\{j, k\}} \boldsymbol{X}_{\mathcal{B}_{\ell}}^{\prime} \\
W_{j, k}^{\prime} & :=\bigoplus_{\ell \in S_{j} \backslash\{j, k\}} X_{\mathcal{B}_{\ell}}^{\prime}
\end{aligned}
$$

Then, proceeding from Eq. (46), Lemma 8 gives us

$$
\begin{aligned}
\underset{Y}{\mathbb{E}}\left[\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j} \cap \mathcal{H}_{k}}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{\mathcal{H}_{j}}\right) \leq \zeta\right\}\right] & \leq \mathbb{E}\left[\mathbb{I}\left\{Y \in \boldsymbol{X}_{\mathcal{B}_{k}}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{W}_{j, k}^{\prime}\right) \leq \zeta\right\}\right]+n_{0} \epsilon \\
& \stackrel{\text { (i) }}{\leq} \frac{\zeta+1}{\left|S_{j} \backslash\{j, k\}\right|}+n_{0} \epsilon \\
& \leq \frac{3(\zeta+1)}{n_{0}-6}+n_{0} \epsilon
\end{aligned}
$$

where step (i) uses Lemma 5. Ultimately, we have

$$
\mathbb{E} T^{\prime}\left(\boldsymbol{X}_{\mathcal{H}_{j}}, \boldsymbol{X}_{\mathcal{H}_{k}}\right) \lesssim \frac{\zeta+1}{n_{0}}+n_{0} \epsilon
$$

and obtain $\mathbb{E}\left[Z_{j}^{\prime} Z_{k}^{\prime}\right] \lesssim \frac{(\zeta+1)}{n_{0}}+n_{0} \epsilon+16 \epsilon$. Substituting $\epsilon=\left(\frac{\mathrm{T}_{\text {mix }}}{n}\right)^{2}$ and noting that $\tau \geq \mathrm{T}_{\text {mix }}$, we obtain $\mathbb{E}\left[Z_{j} Z_{k}\right] \lesssim \frac{(\zeta+1) \tau}{n}$. Averaging over all $j \neq k$ completes the proof of the fact $\mathbb{E}\left[T_{2}\right] \leq$ $C \cdot \frac{(\zeta+1) \tau}{n} \wedge 1$.

Finally, combining our bounds on $\mathbb{E}\left[T_{1}^{\prime}\right]$ and $\mathbb{E}\left[T_{2}^{\prime}\right]$ completes the proof.

## 8 Discussion

We presented the WINGIT estimator for estimating the stationary mass missing from a Markovian sequence. While the vanilla Good-Turing estimator can suffer constant bias in the Markovian setting, our estimator achieves (near) minimax optimal mean-squared error over mixing Markov chains. It can also be computed with a linear-time algorithm, and performs favorably in our experiments, even in language text applications in which the Markovian assumption is clearly
violated. We also presented a variant of WINGIT for estimating the small-count probability in a Markov sequence and established mean squared error bounds for this task.

Our work leaves open several important and intriguing questions. First, while Theorem 1 and 2 provide a complete picture - up to a logarithmic factor - for stationary missing mass estimation from the point of view of MSE, exponential concentration inequalities, both for our estimator and for the missing mass estimand itself, remain out of reach of our current techniques. Such concentration inequalities could, for instance, be used to provide a provable guarantee on the validation procedure that we outlined in Section 6 . Second, we reiterate that our estimator is only optimal up to a logarithmic factor in $n / T_{\text {mix }}$, and removing this factor to match the minimax lower bound - possibly by designing an alternative estimator - is an interesting open problem.

Third, we believe that the Markov property may not be central to our main results, and that Theorem 1 could be extended to more general $\alpha$-mixing sequences (Rosenblatt, 1956). While nontrivial, this extension would capture, for instance, other classes of interesting temporal processes such as some hidden Markov models. Fourth, a related point is that the assumption (5) of geometric ergodicity itself is central to the design and analysis of our estimator; designing estimators that do not require ergodicity — perhaps just irreducibility (Fried, 2023) — would be of great interest and likely require new ideas.

Finally, it would be interesting to estimate other functionals of the Markov chain other than the stationary missing mass and solve related estimation problems such as competitive distribution estimation of the stationary measure. Our extensions to estimating the mass of elements occurring at most $\zeta$ times in Section 5 might be a useful starting point as in the i.i.d. case (Drukh and Mansour, 2005; Acharya et al., 2013), but several questions remain, such as obtaining a uniform bound on the error of estimating all such quantities uniformly over $\zeta \in\{0,1, \ldots, n\}$.

## Acknowledgments

This work was supported in part by National Science Foundation grants CCF-2107455, DMS2210734, CCF-2239151 and IIS-2212182, and by research awards/gifts from Adobe, Amazon, Google and Mathworks. AP thanks Wenlong Mou for helpful discussions.

## References

J. Acharya, A. Jafarpour, A. Orlitsky, and A. T. Suresh. Optimal probability estimation with applications to prediction and classification. In Conference on Learning Theory, pages 764-796, 2013 .

J. Acharya, Y. Bao, Y. Kang, and Z. Sun. Improved bounds for minimax risk of estimating missing mass. In 2018 IEEE International Symposium on Information Theory (ISIT), pages 326-330. IEEE, 2018.

F. Ayed, M. Battiston, F. Camerlenghi, and S. Favaro. On consistent and rate optimal estimation of the missing mass. In Annales de l'Institut Henri Poincare (B) Probabilites et statistiques, volume 57, pages 1476-1494. Institut Henri Poincaré, 2021.

A. Ben-Hamou, S. Boucheron, and M. I. Ohannessian. Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications. Bernoulli, 23(1):249 - 287, 2017. doi: 10.3150/15-BEJ743. URL https://doi.org/10.3150/15-BEJ743.

D. Berend and A. Kontorovich. The missing mass problem. Statistics \& 3 Probability Letters, 82(6): 1102-1110, 2012.

D. Berend and A. Kontorovich. On the concentration of the missing mass. Electronic Communications in Probability, 18(none):1 - 7, 2013. doi: 10.1214/ECP.v18-2359. URL https: //doi.org/10.1214/ECP.v18-2359.

P. Chandra, A. Pradeep, and A. Thangaraj. Improved tail bounds for missing mass and confidence intervals for Good-Turing estimator. In 2019 National Conference on Communications (NCC), pages 1-6. IEEE, 2019.

P. Chandra, A. Thangaraj, and N. Rajaraman. How good is Good-Turing for Markov samples? arXiv preprint arXiv:2102.01938, 2021.

P. Chandra, A. Thangaraj, and N. Rajaraman. Missing mass estimation from sticky channels. In 2022 IEEE International Symposium on Information Theory (ISIT), pages 910-915. IEEE, 2022.

S. F. Chen and J. Goodman. An empirical study of smoothing techniques for language modeling. Computer Speech $\mathcal{E}$ Language, 13(4):359-394, 1999.

K. W. Church and W. A. Gale. Probability scoring for spelling correction. Statistics and Computing, 1:93-103, 1991.

R. K. Colwell, A. Chao, N. J. Gotelli, S.-Y. Lin, C. X. Mao, R. L. Chazdon, and J. T. Longino. Models and estimators linking individual-based and sample-based rarefaction, extrapolation and comparison of assemblages. Journal of Plant Ecology, 5(1):3-21, 2012.

C. Dickens. A Tale of Two Cities. Project Gutenberg, Urbana, IL, USA, 1994. URL gutenberg. org/ebooks/98.

E. Drukh and Y. Mansour. Concentration bounds for unigram language models. Journal of Machine Learning Research, 6(8), 2005.

S. Favaro, A. Lijoi, and I. Prünster. A new estimator of the discovery probability. Biometrics, 68 (4):1188-1196, 2012.

S. Favaro, B. Nipoti, and Y. W. Teh. Rediscovery of Good-Turing estimators via Bayesian nonparametrics. Biometrics, 72(1):136-145, 2016.

R. A. Fisher, A. S. Corbet, and C. B. Williams. The relation between the number of species and the number of individuals in a random sample of an animal population. The Journal of Animal Ecology, pages 42-58, 1943.

S. Fried. On the $\alpha$-lazy version of Markov chains in estimation and testing problems. Statistical Inference for Stochastic Processes, 26(2):413-435, 2023.

W. Gale and K. Church. What is wrong with adding one? In Corpus-based research into language, pages 189-198. Brill, 1994.

W. A. Gale and G. Sampson. Good-Turing frequency estimation without tears. Journal of Quantitative Linguistics, 2(3):217-237, 1995.

W. A. Gale, K. W. Church, and D. Yarowsky. A method for disambiguating word senses in a large corpus. Computers and the Humanities, 26:415-439, 1992.

A. Gandolfi and C. C. Sastri. Nonparametric estimations about species not observed in a random sample. Milan Journal of Mathematics, 72:81-105, 2004.

I. J. Good. The population frequencies of species and the estimation of population parameters. Biometrika, 40(3-4):237-264, 1953.

M. Grabchak and Z. Zhang. Asymptotic properties of Turing's formula in relative error. Machine Learning, 106:1771-1785, 2017.

Y. Han, S. Jana, and Y. Wu. Optimal prediction of Markov chains with and without spectral gap. IEEE Transactions on Information Theory, 69(6):3920-3959, 2023.

Y. Hao, A. Orlitsky, and V. Pichapati. On learning Markov chains. Advances in Neural Information Processing Systems, 31, 2018.

D. Hsu, A. Kontorovich, D. A. Levin, Y. Peres, C. Szepesvári, and G. Wolfer. Mixing time estimation in reversible Markov chains from a single sample path. The Annals of Applied Probability, 29(4):2439 - 2480, 2019. doi: 10.1214/18-AAP1457. URL https://doi.org/10.1214/ 18-AAP1457.

F. Jelinek. Probability distribution estimation from sparse data. IBM technical disclosure bulletin, 28:2591-2594, 1985.

R. Krichevsky and V. Trofimov. The performance of universal encoding. IEEE Transactions on Information Theory, 27(2):199-207, 1981.

P.-S. Laplace. Essai philosophique sur les probabilités. 1814.

D. A. Levin and Y. Peres. Markov chains and mixing times, volume 107. American Mathematical Soc., 2017.

A. Lijoi, R. H. Mena, and I. Prünster. A Bayesian nonparametric method for prediction in EST analysis. BMC bioinformatics, 8:1-10, 2007.

D. McAllester and L. Ortiz. Concentration inequalities for the missing mass and for histogram rule error. Journal of Machine Learning Research, 4(Oct):895-911, 2003.

D. McAllester and R. E. Schapire. Learning theory and language modeling. In Seventeenth International Joint Conference on Artificial Intelligence, 2001.

D. A. McAllester and R. E. Schapire. On the convergence rate of Good-Turing estimators. In Conference on Learning Theory, pages 1-6, 2000.

E. Mossel and M. I. Ohannessian. On the impossibility of learning the missing mass. Entropy, 21 (1):28, 2019 .

H. Ney, U. Essen, and R. Kneser. On structuring probabilistic dependences in stochastic language modelling. Computer Speech E3 Language, 8(1):1-38, 1994.

J. Norris, Y. Peres, and A. Zhai. Surprise probabilities in Markov chains. Combinatorics, Probability and Computing, 26(4):603-627, 2017.

M. I. Ohannessian and M. A. Dahleh. Rare probability estimation under regularly varying heavy tails. In Conference on Learning Theory, pages 21-1, 2012.

R. Oliveira. Mixing and hitting times for finite Markov chains. Electronic Journal of Probability, 17(none):1 - 12, 2012. doi: 10.1214/EJP.v17-2274. URL https://doi.org/10.1214/EJP. v17-2274.

A. Orlitsky and A. T. Suresh. Competitive distribution estimation: Why is Good-Turing good. Advances in Neural Information Processing Systems, 28, 2015.

A. Orlitsky, N. P. Santhanam, and J. Zhang. Always Good-Turing: Asymptotically optimal probability estimation. Science, 302(5644):427-431, 2003.

A. Painsky. Convergence guarantees for the Good-Turing estimator. Journal of Machine Learning Research, 23(279):1-37, 2022.

A. Painsky. Generalized Good-Turing improves missing mass estimation. Journal of the American Statistical Association, 118(543):1890-1899, 2023.

D. Paulin. Concentration inequalities for Markov chains by Marton couplings and spectral methods. Electronic Journal of Probability, 20(none):1 - 32, 2015. doi: 10.1214/EJP.v20-4039. URL https://doi.org/10.1214/EJP.v20-4039.

Y. Peres and P. Sousi. Mixing times are hitting times of large sets. Journal of Theoretical Probability, 28(2):488-519, 2015.

N. Rajaraman, A. Thangaraj, and A. T. Suresh. Minimax risk for missing mass estimation. In 2017 IEEE International Symposium on Information Theory (ISIT), pages 3025-3029. IEEE, 2017.

M. Rosenblatt. A central limit theorem and a strong mixing condition. Proceedings of the National Academy of Sciences, 42(1):43-47, 1956.

T.-J. Shen, A. Chao, and C.-F. Lin. Predicting the number of new species in further taxonomic sampling. Ecology, 84(3):798-804, 2003.

M. Skorski. Missing mass concentration for Markov chains. arXiv preprint arXiv:2001.03603, 2020.

F. Song and W. B. Croft. A general language model for information retrieval. In Proceedings of the Eighth International Conference on Information and Knowledge Management, pages 316-321, 1999.

A. Thangaraj, A. Pananjady, and V. Muthukumar. Missing Mass of Markov Chains, 2024. URL https://github.com/andrewthan/Missing-Mass.

V. Q. Vu, B. Yu, and R. E. Kass. Coverage-adjusted entropy estimation. Statistics in Medicine, 26(21):4039-4060, 2007.

G. Wolfer and A. Kontorovich. Minimax learning of ergodic Markov chains. In Algorithmic Learning Theory, pages 904-930. PMLR, 2019.

## A Technical lemmas

In this section, we collect technical lemmas that were stated and used in the main paper. We first collect lemmas that were used to formalize basic calculations for the Good-Turing estimator, and next lemmas that were used in the proofs of the main results (Theorems 1 and 2).

## A. 1 Elementary lemmas

Our first lemma shows a tight characterization of the mixing time $T_{\text {mix }}=t_{\text {mix }}(1 / 4)$ for the class of sticky Markov chains, defined in Eq. (10).

Lemma 1. Suppose $|\mathcal{X}| \geq 2$ and $p \in(0,1 / 2]$. For any sticky Markov chain as defined in Eq. (10), we have

$$
\frac{1}{2 p} \leq \mathrm{T}_{\text {mix }} \leq \frac{2}{p}
$$

Proof. We proceed by exactly calculating the total variation distance $\max _{x \in \mathcal{X}}\left\|_{x}^{\top} \boldsymbol{P}^{t}-\pi^{\top}\right\|_{\mathrm{TV}}$. First, we note that we can explicitly calculate the $t$-step transition kernel as

$$
\boldsymbol{P}^{t}=(1-p)^{t} \boldsymbol{I}+\left(1-(1-p)^{t}\right) \cdot \mathbf{1} \pi^{\top}
$$

Therefore, we have

$$
\begin{aligned}
\max _{x \in \mathcal{X}}\left\|e_{x}^{\top} \boldsymbol{P}^{t}-\pi^{\top}\right\|_{\mathrm{TV}} & =\max _{x \in \mathcal{X}} \frac{1}{2}\left\|(1-p)^{t} \cdot\left(e_{x}-\pi\right)\right\|_{1} \\
& =\frac{(1-p)^{t}}{2} \cdot \max _{x \in \mathcal{X}}\left\|e_{x}-\pi\right\|_{1}
\end{aligned}
$$

Since $(1-p)^{t} \cdot \max _{x \in \mathcal{X}}\left\|e_{x}-\pi\right\|_{\mathrm{TV}}$ is monotonically decreasing in $t$, we have

$$
\mathrm{T}_{\text {mix }}=\mathrm{t}_{\text {mix }}(1 / 4)=\frac{\log \left(2 \cdot \max _{x \in \mathcal{X}}\left\|e_{x}-\pi\right\|_{1}\right)}{\log (1 /(1-p))}
$$

But

$$
\left\|e_{x}-\pi\right\|_{1}=\left(1-\pi_{x}\right)+\sum_{y \in \mathcal{X} \backslash\{x\}} \pi_{y}=2-2 \pi_{x}
$$

and if $|\mathcal{X}| \geq 2$, then we have $1 \leq \max _{x \in \mathcal{X}}\left\|e_{x}-\pi\right\|_{1} \leq 2$. Furthermore, if $p \in(0,1 / 2]$, then $p \leq \log (1 /(1-p)) \leq p \log 4$. Putting together the pieces, we obtain the sandwich bound

$$
\frac{1}{2 p} \leq \mathrm{T}_{\text {mix }} \leq \frac{2}{p}
$$

as desired.

For any set $P \subseteq[n]$, recall that $\boldsymbol{X}_{P}=\left\{X_{k}\right\}_{k \in P}$ denotes the set of random variables in $X^{n}$ restricted to the index set $P$. The following lemma is a deterministic statement regarding indicator random variables.

Lemma 2. Consider the sequence $X^{n}$ and any random variable $Y$ defined on the space $\mathcal{X}$. Let $P \subseteq Q \subseteq[n]$ denote two index sets, and let $R:=Q \backslash P$. We have

$$
\mathbb{I}\left\{Y \notin \boldsymbol{X}_{P}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{Q}\right\}=\mathbb{I}\left\{Y \in \boldsymbol{X}_{R}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{P}\right\}
$$

Proof. Since $P \subseteq Q$, the exclusion $Y \notin \boldsymbol{X}_{Q}$ implies that $Y \notin \boldsymbol{X}_{P}$. Therefore $\mathbb{I}\left\{Y \notin \boldsymbol{X}_{P}\right\}$ $\mathbb{I}\left\{Y \notin \boldsymbol{X}_{Q}\right\}=1$ if $Y \notin \boldsymbol{X}_{P}$ and $Y \in \boldsymbol{X}_{Q}$, and 0 otherwise. Since $R=Q \backslash P$, we have

$$
\mathbb{I}\left\{Y \notin \boldsymbol{X}_{P}\right\}-\mathbb{I}\left\{Y \notin \boldsymbol{X}_{Q}\right\}=\mathbb{I}\left\{Y \in \boldsymbol{X}_{R}\right\} \cdot \mathbb{I}\left\{Y \notin \boldsymbol{X}_{P}\right\}
$$

as claimed.

We also define an extension of Lemma 2 to slightly more complicated indicator random variables involving the count of an element in index sets.

Lemma 3. Consider the sequence $X^{n}$ and any random variable $Y$ defined on the space $\mathcal{X}$. Let $P \subseteq Q \subseteq[n]$ denote two index sets, and let $R:=Q \backslash P$. Then, for any $\zeta \geq 0$, we have

$$
\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{Q}\right) \leq \zeta\right\} \leq \mathbb{I}\left\{Y \in \boldsymbol{X}_{R}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta\right\}
$$

Proof. Since $P \subseteq Q$, the event $N_{Y}\left(\boldsymbol{X}_{Q}\right) \leq \zeta$ implies that $N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta$. Consequently, $\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta\right\}-$ $\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{Q}\right) \leq \zeta\right\}=1$ if and only if $N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta$ and $N_{Y}\left(\boldsymbol{X}_{Q}\right)>\zeta$. Further, we have $N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta$ and $N_{Y}\left(\boldsymbol{X}_{Q}\right)>\zeta$ only if $N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta$ and $N_{Y}\left(\boldsymbol{X}_{R}\right) \geq 1$, i.e. $N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta$ and $Y \in \boldsymbol{X}_{R}$. This gives us

$$
\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta\right\}-\mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{Q}\right) \leq \zeta\right\} \leq \mathbb{I}\left\{Y \in \boldsymbol{X}_{R}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\boldsymbol{X}_{P}\right) \leq \zeta\right\}
$$

## A. 2 Functionals of hitting times in independent Markov chains

Our next lemma is an analog, for Markov chains, of the bias bound known for i.i.d. data.

Lemma 4. Consider $k$ independent and identically distributed Markov chains $\left\{\mathrm{X}_{j}\right\}_{j=1}^{k}$ supported on $\mathcal{X}^{t}$, where $\mathrm{X}_{j}=\left(X_{1}^{j}, \ldots, X_{t}^{j}\right)$ is a Markov chain with initial distribution sampled from stationary distribution $\pi$ and having transition kernel $\boldsymbol{P}$. With a slight abuse of notation, let $\mathbf{X}_{j}$ also denote the set of random variables in $\mathrm{X}_{j}$.

Now suppose that $Y$ is a random variable taking values in $\mathcal{X}$ sampled independently of everything else. Then

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \mathrm{X}_{1}\right\} \cdot \prod_{j=2}^{k} \mathbb{I}\left\{Y \notin \mathrm{X}_{j}\right\}\right] \leq \frac{1}{k}
$$

Proof. Let $p_{Y}$ denote the probability mass function of the random variable $Y$. Owing to independence between the sequences $\left\{\mathrm{X}_{j}\right\}_{j=1}^{k}$, we use the tower property of expectation to write

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \mathbf{X}_{1}\right\} \cdot \prod_{j=2}^{k} \mathbb{I}\left\{Y \notin \mathbf{X}_{j}\right\}\right]=\sum_{y \in \mathcal{X}} p(y)\left[\mathbb{E}\left[\mathbb{I}\left\{y \in \mathbf{X}_{1}\right\}\right] \cdot\left(\prod_{j=2}^{k} \mathbb{E}\left[\mathbb{I}\left\{y \notin \mathbf{X}_{j}\right\}\right]\right)\right]
$$

For a Markov chain $\left(X_{i}\right)_{i \geq 1}$ initialized at $X_{1} \sim \pi$ and each fixed $x \in \mathcal{X}$, let the random variable $H(x):=\min \left\{\tau:\left\{X_{1}, \ldots, X_{\tau}\right\} \ni x\right\}$ denote the hitting time of $x$. Also, for each natural number $t$, let $q_{t}(x)=\operatorname{Pr}\{H(x) \leq t\}$. With this notation, and noting that each Markov chain has length $t$, we can write the above expression as

$$
\begin{aligned}
\mathbb{E}\left[\mathbb{I}\left\{Y \in \mathbf{X}_{1}\right\} \cdot \prod_{j=2}^{k} \mathbb{I}\left\{Y \notin \mathbf{X}_{j}\right\}\right] & =\sum_{y \in \mathcal{X}} p_{Y}(y) q_{t, y}\left(1-q_{t, y}\right)^{k-1} \\
& =\frac{1}{k} \sum_{y \in \mathcal{X}} p_{Y}(y) \cdot k \cdot q_{t, y}\left(1-q_{t, y}\right)^{k-1} \\
& \leq\left(\frac{1}{k} \sum_{y \in \mathcal{X}} p_{Y}(y)\right) \cdot \max _{y} k q_{t, y}\left(1-q_{t, y}\right)^{k-1} \leq \frac{1}{k}
\end{aligned}
$$

where the final step follows because $k q_{t, y}\left(1-q_{t, y}\right)^{k-1} \in[0,1]$ since $q_{t, y}$ is a probability, and $\sum_{y \in \mathcal{X}} p_{Y}(y)=1$.

We also extend the above lemma to indicator random variables involving the counts of elements in i.i.d. Markov chains. It is convenient to define notation for binomial and multinomial random variables in a self-contained manner, which we do below.

Definition 1. We denote by $\operatorname{Bin}(k, q)$ a binomial distribution with $k$ trials and success probability $q$. In other words, if $L \sim \operatorname{Bin}(k, q)$ then we have

$$
\operatorname{Pr}\{L=\ell\}=\left(\begin{array}{c}
k \\
\ell
\end{array}\right) q^{\ell}(1-q)^{k-\ell} \quad \text { for each } \quad \ell \in\{0, \ldots, k\}
$$

Similarly, we denote by $\operatorname{Mult}\left(k,\left(q_{s}\right)_{s \in S}\right)$ a multinomial distribution with $k$ trials, a set of outcomes $S$, and probabilities for each outcome $s \in S$ given by $q_{s}$. We say that $\left(K_{s}\right)_{s \in S} \sim \operatorname{Multi}\left(k,\left(q_{s}\right)_{s \in S}\right)$ if $\sum_{s \in S} K_{s}=k$, and

$$
\operatorname{Pr}\left\{\bigcap_{s \in S}\left\{K_{s}=k_{s}\right\}\right\}=\frac{k !}{\prod_{s \in S} k_{s} !} \cdot \prod_{s \in S}\left(q_{s}\right)^{k_{s}}
$$

Lemma 5. Carrying over the notation defined in Lemma 4, we have, for any $\zeta \geq 0$,

$$
\mathbb{E}\left[\mathbb{I}\left\{Y \in \mathrm{X}_{1}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\mathrm{X}_{2} \oplus \ldots \oplus \mathrm{X}_{k}\right) \leq \zeta\right\}\right] \leq \frac{\zeta+1}{k}
$$

(Note that in the special case where $\zeta=0$, we have $\mathbb{I}\left\{N_{Y}\left(\mathrm{X}_{2} \oplus \ldots \oplus \mathrm{X}_{k}\right) \leq \zeta\right\}=\prod_{j=2}^{k} \mathbb{I}\left\{Y \notin \mathrm{X}_{j}\right\}$, and Lemma 5 recovers Lemma 4 as a special case.)

Proof. The proof of this lemma uses similar ideas to the proof of Lemma 4, but is significantly more intricate due to the need to directly handle the complicated random variable $N_{Y}\left(\mathrm{X}_{2} \oplus \ldots \oplus \mathrm{X}_{k}\right)$.

Carrying over notation from the proof of Lemma 4, we can again use independence between $X_{1}$ and $\oplus_{j=2}^{k} \mathrm{X}_{j}$ to obtain

$$
\begin{aligned}
\mathbb{E}\left[\mathbb{I}\left\{Y \in \mathrm{X}_{1}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\mathrm{X}_{2} \oplus \ldots \oplus \mathrm{X}_{k}\right) \leq \zeta\right\}\right] & =\sum_{y \in \mathcal{X}} p(y)\left[\operatorname{Pr}\left\{y \in \mathrm{X}_{1}\right\} \cdot \operatorname{Pr}\left\{N_{y}\left(\oplus_{j=2}^{k} \mathrm{X}_{j}\right) \leq \zeta\right\}\right] \\
& =\sum_{y \in \mathcal{X}} p(y) \cdot q_{t, y} \cdot \operatorname{Pr}\left\{N_{y}\left(\oplus_{j=2}^{k} \mathrm{X}_{j}\right) \leq \zeta\right\}
\end{aligned}
$$

The bulk of the proof concerns handling the term $\operatorname{Pr}\left\{N_{y}\left(\oplus_{j=2}^{k} \mathrm{X}_{j}\right) \leq \zeta\right\}$, and to do so, we make a key connection to multinomial random variables. For every $s \in\{0,1, \ldots, t\}$, let $K_{s}:=\sum_{j=2}^{k} \mathbb{I}\left\{N_{y}\left(\mathrm{X}_{j}\right)=s\right\}$. Because the random variables $N_{y}\left(\mathrm{X}_{j}\right)$ are independent, the random variables $\left(K_{0}, \ldots, K_{t}\right)$ are drawn from a multinomial distribution. By definition, we have $\sum_{s=0}^{t} K_{s}=k-1$. Let $r_{t, y}(s):=\operatorname{Pr}\left\{N_{y}\left(\mathrm{X}_{j}\right)=s\right\}$ and further note that

$$
r_{t, y}(0):=1-q_{t, y} \quad \text { and } \quad r_{t, y}(s):=q_{t, y} \cdot \alpha_{s} \text { for all } s \geq 1
$$

where $\sum_{s=1}^{t} \alpha_{s}=1$ and $\alpha_{s} \geq 0$ for all $s \in[t]$. In other words, in the notation of Definition 1, we have

$$
\left(K_{0}, \ldots, K_{t}\right) \sim \operatorname{Multi}\left(k-1,\left(r_{t, y}(s)\right)_{s \in\{0, \ldots, t\}}\right)
$$

With this notation, we have

$$
\begin{aligned}
\operatorname{Pr}\left\{K_{0}=k_{0}, \ldots, K_{t}=k_{t}\right\} & =\frac{(k-1) !}{k_{0} ! \ldots, k_{t} !} \cdot \prod_{s=0}^{t}\left(r_{t, y}(s)\right)^{k_{s}} \\
& =\frac{(k-1) !}{k_{0} ! \ldots, k_{t} !} \cdot\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-1-k_{0}} \cdot \prod_{s=1}^{t}\left(\alpha_{s}\right)^{k_{s}} \\
& =\underbrace{\left(\begin{array}{c}
k-1 \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}}\left(q_{t, y}\right)^{k-1-k_{0}}}_{\beta\left(k, k_{0}\right)} \cdot \frac{\left(k-1-k_{0}\right) !}{k_{1} ! \ldots k_{t} !} \cdot \prod_{s=1}^{t}\left(\alpha_{s}\right)^{k_{s}}
\end{aligned}
$$

Our next observation is that $N_{y}\left(\oplus_{j=2}^{k} \mathrm{X}_{j}\right)=\sum_{s=1}^{t} s \cdot K_{s}$. Moreover, any realization of $\left(k_{0}, \ldots, k_{t}\right)$ under which $N_{y}\left(\oplus_{j=2}^{k} \mathrm{X}_{j}\right) \leq \zeta$ requires $k_{0} \geq k-1-\zeta$. Therefore, we can write

$$
\begin{aligned}
& \operatorname{Pr}\left\{N_{y}\left(\oplus_{j=2}^{k} \mathrm{X}_{j}\right) \leq \zeta\right\}=\sum_{\substack{\left(k_{0}, \ldots, k_{t}\right) \\
k_{0} \geq k-1-\zeta \\
\sum_{s=1}^{t} s k_{s} \leq \zeta}} \operatorname{Pr}\left\{K_{0}=k_{0}, \ldots, K_{t}=k_{t}\right\} \\
& =\sum_{k_{0} \geq k-1-\zeta} \beta\left(k, k_{0}\right) \cdot \sum_{\substack{\left(k_{1}, \ldots, k_{t}\right) \\
\sum_{s=1}^{t} k_{s}=k-1-k_{0} \\
\sum_{s=1}^{t} s k_{s} \leq \zeta}} \frac{\left(k-1-k_{0}\right) !}{k_{1} ! \ldots k_{t} !} \cdot \prod_{s=1}^{t}\left(\alpha_{s}\right)^{k_{s}} \\
& \leq \sum_{k_{0} \geq k-1-\zeta} \beta\left(k, k_{0}\right) \cdot \sum_{\substack{\left(k_{1}, \ldots, k_{t}\right) \\
\sum_{s=1}^{t} k_{s}=k-1-k_{0}}} \frac{\left(k-1-k_{0}\right) !}{k_{1} ! \ldots k_{t} !} \cdot \prod_{s=1}^{t}\left(\alpha_{s}\right)^{k_{s}} \\
& \stackrel{(\mathrm{i})}{=} \sum_{k_{0} \geq k-1-\zeta} \beta\left(k, k_{0}\right)
\end{aligned}
$$

where step (i) follows because the term $\frac{\left(k-1-k_{0}\right) !}{k_{1} ! \ldots k_{t} !} \cdot \prod_{s=1}^{t}\left(\alpha_{s}\right)^{k_{s}}$ denotes the PMF of a different multinomial random variable with $k-1-k_{0}$ independent trials, outcomes in $[t]$ and outcome probabilities $\left(\alpha_{1}, \ldots, \alpha_{t}\right)$, i.e. Multi $\left(k-1-k_{0},\left\{\alpha_{s}\right\}_{s \in[t]}\right)$ in the notation of Definition 1.

Substituting Eq. (51) into Eq. (49), we have

$$
\begin{aligned}
\mathbb{E}\left[\mathbb{I}\left\{Y \in \mathrm{X}_{1}\right\} \cdot \mathbb{I}\left\{N_{Y}\left(\mathrm{X}_{2} \oplus \ldots \oplus \mathrm{X}_{k}\right) \leq \zeta\right\}\right] & =\sum_{y \in \mathcal{X}} \sum_{k_{0} \geq k-1-\zeta} p(y) \cdot q_{t, y} \cdot \beta\left(k, k_{0}\right) \\
& =\sum_{y \in \mathcal{X}} \sum_{k_{0} \geq k-1-\zeta} p(y) \cdot\left(\begin{array}{c}
k-1 \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-k_{0}} \\
& =\sum_{y \in \mathcal{X}} \sum_{k_{0} \geq k-1-\zeta} p(y) \cdot \frac{k-k_{0}}{k} \cdot\left(\begin{array}{c}
k \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-k_{0}} \\
& \leq \frac{\text { (i) }}{\leq} \frac{\zeta+1}{k} \cdot \sum_{y \in \mathcal{X}} p(y) \cdot \sum_{k_{0} \geq k-1-\zeta}\left(\begin{array}{c}
k \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-k_{0}}
\end{aligned}
$$

where step (i) follows because $k_{0} \geq k-1-\zeta$ implies that $k-k_{0} \leq \zeta+1$. Finally, we apply Holder's inequality to obtain

$$
\begin{aligned}
& \frac{\zeta+1}{k} \cdot \sum_{y \in \mathcal{X}} p(y) \cdot \sum_{k_{0} \geq k-1-\zeta}\left(\begin{array}{c}
k \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-k_{0}} \\
& \leq\left(\frac{\zeta+1}{k} \cdot \sum_{y \in \mathcal{X}} p(y)\right) \cdot \max _{y \in \mathcal{X}} \sum_{k_{0} \geq k-1-\zeta}\left(\begin{array}{c}
k \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-k_{0}} \\
& \stackrel{\text { (i) }}{\leq}\left(\frac{\zeta+1}{k} \cdot \sum_{y \in \mathcal{X}} p(y)\right)=\frac{\zeta+1}{k}
\end{aligned}
$$

Above, step (i) follows because for any $y \in \mathcal{X}$, the sum

$$
\sum_{k_{0} \geq k-1-\zeta}\left(\begin{array}{c}
k \\
k_{0}
\end{array}\right)\left(1-q_{t, y}\right)^{k_{0}} \cdot\left(q_{t, y}\right)^{k-k_{0}}
$$

is equal to the probability of a subset of outcomes of a $\operatorname{Bin}\left(k, q_{t, y}\right)$ random variable, which is less than or equal to 1 . This completes the proof of the lemma.

## A. 3 Lemmas on surrogate processes

We next present several consequences of mixing, and each lemma is proved in a purely algebraic fashion. In all the lemmas below, let $\left(X_{1}, \ldots, X_{n}\right)$ denote a Markov chain with unique stationary distribution $\pi$ and $X_{1} \sim \pi$. Let $\mathrm{t}_{\text {mix }}(\epsilon)$ denote its mixing time in the sense of Eq. (5), with $\epsilon \in(0,1 / 2]$.

Lemma 6. Fix a positive scalar $\epsilon \leq 1 / 2$, and let $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$ be an integer. For each $i \in[n]$, define the stochastic processes

$$
\begin{aligned}
& Z_{i}=\left(X_{1}, X_{2}, \ldots, X_{i-\tau}, X_{i}, X_{i+\tau}, X_{i+\tau+1}, \ldots, X_{n}\right) \\
& Z_{i}^{\prime}=\left(X_{1}, X_{2}, \ldots, X_{i-\tau}, X_{i}^{\prime}, X_{i+\tau}, X_{i+\tau+1}, \ldots, X_{n}\right)
\end{aligned}
$$

where $X_{i}^{\prime} \sim \pi$ is drawn independently of everything else. Then $\mathrm{d}_{\mathrm{TV}}\left(Z_{i}, Z_{i}^{\prime}\right) \leq 4 \epsilon$.

Consequently, for any function $f: \mathcal{X}^{n-2 \tau} \rightarrow[0,1]$, we have

$$
\left|\mathbb{E}\left[f\left(Z_{i}\right)-f\left(Z_{i}^{\prime}\right)\right]\right| \leq 4 \epsilon
$$

Proof. Let $A_{i}=\left(X_{i-\tau}, X_{i}, X_{i+\tau}\right)$ and $A_{i}^{\prime}=\left(X_{i-\tau}, X_{i}^{\prime}, X_{i+\tau}\right)$. By the Markov property, we have $\mathrm{d}_{\mathrm{TV}}\left(Z_{i}, Z_{i}^{\prime}\right)=\mathrm{d}_{\mathrm{TV}}\left(A_{i}, A_{i}^{\prime}\right)$. But the distributions of these triples can be written explicitly, as

$$
\begin{aligned}
& \operatorname{Pr}\left\{A_{i}=(j, k, \ell)\right\}=\operatorname{Pr}\left\{\left(X_{i-\tau}, X_{i}, X_{i+\tau}\right)=(j, k, \ell)\right\}=\pi_{j} \cdot \boldsymbol{e}_{j}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{k} \boldsymbol{e}_{k}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{\ell} \text { and } \\
& \operatorname{Pr}\left\{A_{i}^{\prime}=(j, k, \ell)\right\}=\operatorname{Pr}\left\{\left(X_{i-\tau}, X_{i}^{\prime}, X_{i+\tau}\right)=(j, k, \ell)\right\}=\pi_{j} \cdot \pi_{k} \cdot \boldsymbol{e}_{j}^{\top} \boldsymbol{P}^{2 \tau} \boldsymbol{e}_{\ell}
\end{aligned}
$$

Here $\boldsymbol{e}_{j} \in \mathbb{R}^{\mathcal{X}}$ denotes the indicator vector that is 1 in index $j \in \mathcal{X}$ and 0 elsewhere. For each pair of indices $(j, k) \in \mathcal{X} \times \mathcal{X}$, define

$$
\delta_{j, k}:=\boldsymbol{e}_{j}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{k}-\pi_{k} \text { and } \bar{\delta}_{j, k}:=\boldsymbol{e}_{j}^{\top} \boldsymbol{P}^{2 \tau} \boldsymbol{e}_{k}-\pi_{k}
$$

Owing to our total variation mixing assumption (5) and the choice $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$, we have that the $\ell_{1}$ size of errors is bounded as

$$
\max _{j \in \mathcal{X}} \sum_{k \in \mathcal{X}}\left|\delta_{j, k}\right| \leq 2 \epsilon \quad \text { and } \quad \max _{j \in \mathcal{X}} \sum_{k \in \mathcal{X}}\left|\bar{\delta}_{j, k}\right| \leq 2 \epsilon^{2}
$$

With this shorthand notation, we may define

$$
\begin{aligned}
& \operatorname{Pr}\left\{A_{i}=(j, k, \ell)\right\}=\pi_{j} \cdot\left(\pi_{k}+\delta_{j, k}\right) \cdot\left(\pi_{\ell}+\delta_{k, \ell}\right) \text { and } \\
& \operatorname{Pr}\left\{A_{i}^{\prime}=(j, k, \ell)\right\}=\pi_{j} \cdot \pi_{k} \cdot\left(\pi_{\ell}+\bar{\delta}_{j, \ell}\right)
\end{aligned}
$$

and we can write the total variation explicitly as

$$
\begin{aligned}
& \mathrm{d}_{\mathrm{TV}}\left(A_{i}, A_{i}^{\prime}\right) \\
& =\frac{1}{2} \sum_{j, k, \ell \in \mathcal{X}}\left|\pi_{j} \cdot\left(\pi_{k}+\delta_{j, k}\right) \cdot\left(\pi_{\ell}+\delta_{k, \ell}\right)-\pi_{j} \cdot \pi_{k} \cdot\left(\pi_{\ell}+\bar{\delta}_{j, \ell}\right)\right| \\
& =\frac{1}{2} \sum_{j, k, \ell \in \mathcal{X}}\left|\pi_{j} \cdot \pi_{k} \cdot \delta_{k, \ell}+\pi_{j} \cdot \pi_{\ell} \cdot \delta_{j, k}+\pi_{j} \cdot \delta_{j, k} \cdot \delta_{k, \ell}-\pi_{j} \cdot \pi_{k} \cdot \bar{\delta}_{j, \ell}\right| \\
& \leq \frac{1}{2} \sum_{j, k, \ell \in \mathcal{X}}\left|\pi_{j} \cdot \pi_{k} \cdot \delta_{k, \ell}\right|+\sum_{j, k, \ell \in \mathcal{X}} \frac{1}{2}\left|\pi_{j} \cdot \pi_{\ell} \cdot \delta_{j, k}\right|+\sum_{j, k, \ell \in \mathcal{X}} \frac{1}{2}\left|\pi_{j} \cdot \delta_{j, k} \cdot \delta_{k, \ell}\right|+\sum_{j, k, \ell \in \mathcal{X}} \frac{1}{2}\left|\pi_{j} \cdot \pi_{k} \cdot \bar{\delta}_{j, \ell}\right| \\
& \stackrel{(\mathrm{i})}{\leq} \epsilon+\epsilon+2 \epsilon^{2}+\epsilon^{2} \leq 4 \epsilon
\end{aligned}
$$

where we claim that the bound in step (i) holds term by term and the last inequality uses the fact that $\epsilon \leq 1 / 2$. It remains to prove step (i). The first term can be bounded as

$$
\sum_{j, k, \ell \in \mathcal{X}}\left|\pi_{j} \cdot \pi_{k} \cdot \delta_{k, \ell}\right| \leq \sum_{j, k \in \mathcal{X}} \pi_{j} \cdot \pi_{k} \sum_{\ell \in \mathcal{X}}\left|\delta_{k, \ell}\right| \leq \sum_{j, k \in \mathcal{X}} \pi_{j} \cdot \pi_{k} \cdot(2 \epsilon)=2 \epsilon
$$

where the last equality follows because $\pi$ is a probability distribution. The remaining terms can be bounded using similar logic, so we omit the steps for brevity.

The consequence of the TV bound for expectations of bounded functions follows as a definition of total variation.

Lemma 7. Fix a positive scalar $\epsilon \leq 1 / 2$, and let $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$ be an integer. For each $i_{1}<i_{2} \in[n]$ with $i_{2}-i_{1}>\tau$, define the stochastic processes

$$
\begin{aligned}
Z_{i_{1}, i_{2}} & =\left(X_{1}, X_{2}, \ldots, X_{i_{1}-\tau}, X_{i_{1}}, X_{i_{1}+\tau}, \ldots, X_{i_{2}-\tau}, X_{i_{2}}, X_{i_{2}+\tau}, \ldots, X_{n}\right) \\
Z_{i_{1}, i_{2}}^{\prime} & =\left(X_{1}, X_{2}, \ldots, X_{i_{1}-\tau}, X_{i_{1}}^{\prime}, X_{i_{1}+\tau}, \ldots, X_{i_{2}-\tau}, X_{i_{2}}^{\prime}, X_{i_{2}+\tau}, \ldots, X_{n}\right)
\end{aligned}
$$

where $X_{i_{1}}^{\prime}, X_{i_{2}}^{\prime} \sim \pi$ are drawn independently of each other and of everything else. Then we have $\mathrm{d}_{\mathrm{TV}}\left(Z_{i_{1}, i_{2}}, Z_{i_{1}, i_{2}}^{\prime}\right) \leq 8 \epsilon$.

Consequently, for any function $f$ with range $[0,1]$, we have

$$
\left|\mathbb{E}\left[f\left(Z_{i, j}\right)-f\left(Z_{i, j}^{\prime}\right)\right]\right| \leq 8 \epsilon
$$

Proof. We prove the bound on total variation, noting that the consequence for bounded functions follows as a corollary. As in the proof of Lemma 6, we define the sub-processes

$$
\begin{aligned}
& A_{i_{1}, i_{2}}=\left(X_{i_{1}-\tau}, X_{i_{1}}, X_{i_{1}+\tau}, X_{i_{2}-\tau}, X_{i_{2}}, X_{i_{2}+\tau}\right) \\
& A_{i_{1}, i_{2}}^{\prime}=\left(X_{i_{1}-\tau}, X_{i_{1}}^{\prime}, X_{i_{1}+\tau}, X_{i_{2}-\tau}, X_{i_{2}}^{\prime}, X_{i_{2}+\tau}\right)
\end{aligned}
$$

We also define an intermediate sub-process $\widetilde{A}_{i_{1}, i_{2}}=\left(X_{i_{1}-\tau}, X_{i_{1}}^{\prime}, X_{i_{1}+\tau}, X_{i_{2}-\tau}, X_{i_{2}}, X_{i_{2}+\tau}\right)$ for convenience. Then, simplifying the expression for total variation over the entire Markov chain and noting that the stochastic processes $Z_{i_{1}, i_{2}}, Z_{i_{1}, i_{2}}^{\prime}$ follow identical transition laws over the indices $\left\{1, \ldots, i_{1}-\tau\right\} \cup\left\{i_{1}+\tau+1, \ldots, i_{2}-\tau\right\} \cup\left\{i_{2}+\tau+1, \ldots, n\right\}$

$$
\mathrm{d}_{\mathrm{TV}}\left(Z_{i_{1}, i_{2}}, Z_{i_{1}, i_{2}}^{\prime}\right)=\mathrm{d}_{\mathrm{TV}}\left(A_{i_{1}, i_{2}}, A_{i_{1}, i_{2}}^{\prime}\right) \stackrel{(\mathrm{i})}{\leq} \mathrm{d}_{\mathrm{TV}}\left(A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}\right)+\mathrm{d}_{\mathrm{TV}}\left(\widetilde{A}_{i_{1}, i_{2}}, A_{i_{1}, i_{2}}^{\prime}\right)
$$

where step (i) follows by the triangle inequality. We proceed to upper bound each of the terms $\mathrm{d}_{\mathrm{TV}}\left(A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}\right)$ and $\mathrm{d}_{\mathrm{TV}}\left(\widetilde{A}_{i_{1}, i_{2}}, A_{i_{1}, i_{2}}^{\prime}\right)$ by $4 \epsilon$ each, using a similar argument to the proof of Lemma 6. We denote $\rho_{j_{2}, \ell_{1}}=\operatorname{Pr}\left[X_{i_{2}-\tau-1}=j_{2} \mid X_{i_{1}+\tau+1}=\ell_{1}\right]$ as shorthand, noting that for each $\ell_{1} \in \mathcal{X}$, we have $\sum_{j_{2} \in \mathcal{X}} \rho_{j_{2}, \ell_{1}}=1$. We begin with the first term $\operatorname{dVV}\left(A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}\right)$ and characterize the distributions of $A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}$ as below:

$$
\begin{aligned}
& \operatorname{Pr}\left\{A_{i_{1}, i_{2}}=\left(j_{1}, k_{1}, \ell_{1}, j_{2}, k_{2}, \ell_{2}\right)\right\}=\pi_{j_{1}} \cdot \boldsymbol{e}_{j_{1}}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{k_{1}} \boldsymbol{e}_{k_{1}}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{\ell_{1}} \cdot \rho_{j_{2}, \ell_{1}} \cdot \boldsymbol{e}_{j_{2}}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{k_{2}} \boldsymbol{e}_{k_{2}}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{\ell_{2}} \text { and } \\
& \operatorname{Pr}\left\{A_{i_{1}, i_{2}}^{\prime}=\left(j_{1}, k_{1}, \ell_{1}, j_{2}, k_{2}, \ell_{2}\right)\right\}=\pi_{j_{1}} \cdot \pi_{k_{1}} \cdot \boldsymbol{e}_{j_{1}}^{\top} \boldsymbol{P}^{2 \tau} \boldsymbol{e}_{\ell_{1}} \cdot \rho_{j_{2}, \ell_{1}} \cdot \boldsymbol{e}_{j_{2}}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{k_{2}} \boldsymbol{e}_{k_{2}}^{\top} \boldsymbol{P}^{\tau} \boldsymbol{e}_{\ell_{2}}
\end{aligned}
$$

Recalling the shorthand notation $\delta_{j, k}, \bar{\delta}_{j, k}$ that was defined in the proof of Lemma 6, we can write the above as

$\operatorname{Pr}\left\{A_{i_{1}, i_{2}}=\left(j_{1}, k_{1}, \ell_{1}, j_{2}, k_{2}, \ell_{2}\right)\right\}=\pi_{j_{1}} \cdot\left(\pi_{k_{1}}+\delta_{j_{1}, k_{1}}\right) \cdot\left(\pi_{\ell_{1}}+\delta_{k_{1}, \ell_{1}}\right) \cdot \rho_{j_{2}, \ell_{1}} \cdot\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right) \cdot\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)$

$\operatorname{Pr}\left\{\widetilde{A}_{i_{1}, i_{2}}=\left(j_{1}, k_{1}, \ell_{1}, j_{2}, k_{2}, \ell_{2}\right)\right\}=\pi_{j_{1}} \cdot \pi_{k_{1}} \cdot\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right) \cdot \rho_{j_{2}, \ell_{1}} \cdot\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right) \cdot\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)$.

Next, we note that $\rho_{j_{2}, \ell_{1}} \cdot\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right) \cdot\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)=\operatorname{Pr}\left[X_{i_{2}-\tau-1}=j_{2}, X_{i_{2}}=k_{2}, X_{i_{2}+\tau+1}=\right.$ $\left.\ell_{2} \mid X_{i_{1}+\tau+1}=\ell_{1}\right]$ which is a conditional probability distribution that is identical for the stochastic processes $\widetilde{A}_{i_{1}, i_{2}}$ and $A_{i_{1}, i_{2}}$. Therefore, we have $\sum_{j_{2}, k_{2}, \ell_{2} \in \mathcal{X}} \rho_{j_{2}, \ell_{1}} \cdot\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right) \cdot\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)=1$ for
any value of $\ell_{1} \in \mathcal{X}$. This yields

$$
\begin{aligned}
& \mathrm{d}_{\mathrm{TV}}\left(A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}\right) \\
& \left.=\frac{1}{2} \sum_{\substack{j_{1}, k_{1}, \ell_{1} \in \mathcal{X} \\
j_{2}, k_{2}, \ell_{2} \in \mathcal{X}}} \right\rvert\, \pi_{j_{1}}\left(\pi_{k_{1}}+\delta_{j_{1}, k_{1}}\right)\left(\pi_{\ell_{1}}+\delta_{k_{1}, \ell_{1}}\right) \rho_{j_{2}, \ell_{1}}\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right)\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right) \\
& \quad-\pi_{j_{1}} \pi_{k_{1}}\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right) \rho_{j_{2}, \ell_{1}}\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right)\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right) \mid \\
& =\frac{1}{2} \sum_{\substack{j_{1}, k_{1}, \ell_{1} \in \mathcal{X} \\
j_{2}, k_{2}, \ell_{2} \in \mathcal{X}}} \rho_{j_{2}, \ell_{1}}\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right)\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)\left|\pi_{j_{1}}\left(\pi_{k_{1}}+\delta_{j_{1}, k_{1}}\right)\left(\pi_{\ell_{1}}+\delta_{k_{1}, \ell_{1}}\right)-\pi_{j_{1}} \pi_{k_{1}}\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right)\right| \\
& =\frac{1}{2} \sum_{j_{1}, k_{1}, \ell_{1} \in \mathcal{X}}\left|\pi_{j_{1}}\left(\pi_{k_{1}}+\delta_{j_{1}, k_{1}}\right)\left(\pi_{\ell_{1}}+\delta_{k_{1}, \ell_{1}}\right)-\pi_{j_{1}} \pi_{k_{1}}\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right)\right|
\end{aligned}
$$

where the last equality uses the fact that $\sum_{j_{2}, k_{2}, \ell_{2} \in \mathcal{X}} \rho_{j_{2}, \ell_{1}} \cdot\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right) \cdot\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)=1$ for any value of $\ell_{1} \in \mathcal{X}$. We have thus arrived an expression for $\mathrm{d}_{\mathrm{TV}}\left(A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}\right)$ that is identical to Equation (55), which is upper bounded by $4 \epsilon$. Therefore, we have $\operatorname{d}_{\operatorname{TV}}\left(A_{i_{1}, i_{2}}, \widetilde{A}_{i_{1}, i_{2}}\right) \leq 4 \epsilon$.

We now use a similar technique to bound the other term $\mathrm{d}_{\operatorname{TV}}\left(\widetilde{A}_{i_{1}, i_{2}}, A_{i_{1}, i_{2}}^{\prime}\right)$. In particular, we have

$$
\begin{aligned}
& \operatorname{Pr}\left\{\widetilde{A}_{i_{1}, i_{2}}=\left(j_{1}, k_{1}, \ell_{1}, j_{2}, k_{2}, \ell_{2}\right)\right\}=\pi_{j_{1}} \cdot \pi_{k_{1}} \cdot\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right) \cdot \rho_{j_{2}, \ell_{1}} \cdot\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right) \cdot\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right) \\
& \operatorname{Pr}\left\{A_{i_{1}, i_{2}}^{\prime}=\left(j_{1}, k_{1}, \ell_{1}, j_{2}, k_{2}, \ell_{2}\right)\right\}=\pi_{j_{1}} \cdot \pi_{k_{1}} \cdot\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right) \cdot \rho_{j_{2}, \ell_{1}} \cdot \pi_{k_{2}} \cdot\left(\pi_{\ell_{2}}+\bar{\delta}_{j_{2}, \ell_{2}}\right)
\end{aligned}
$$

This time, we note that $\pi_{j_{1}} \cdot \pi_{k_{1}} \cdot\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right) \cdot \rho_{j_{2}, \ell_{1}}=\operatorname{Pr}\left[X_{i_{1}-\tau-1}=j_{1}, X_{i_{1}}^{\prime}=k_{1}, X_{i_{1}+\tau+1}=\right.$ $\left.\ell_{1}, X_{i_{2}-\tau-1}=j_{2}\right]$ and therefore $\sum_{j_{1}, k_{1}, \ell_{1} \in \mathcal{X}} \pi_{j_{1}} \cdot \pi_{k_{1}} \cdot\left(\pi_{\ell_{1}}+\bar{\delta}_{j_{1}, \ell_{1}}\right) \cdot \rho_{j_{2}, \ell_{1}}=\operatorname{Pr}\left[X_{i_{2}-T-1}=j_{2}\right]=\pi_{j_{2}}$. Using a similar series of steps to the preceding calculation, we obtain

$$
\mathrm{d}_{\mathrm{TV}}\left(\widetilde{A}_{i_{1}, i_{2}}, A_{i_{1}, i_{2}}\right)=\frac{1}{2} \sum_{j_{2}, k_{2}, \ell_{2} \in \mathcal{X}}\left|\pi_{j_{2}}\left(\pi_{k_{2}}+\delta_{j_{2}, k_{2}}\right)\left(\pi_{\ell_{2}}+\delta_{k_{2}, \ell_{2}}\right)-\pi_{j_{2}} \pi_{k_{2}}\left(\pi_{\ell_{2}}+\bar{\delta}_{j_{2}, \ell_{2}}\right)\right| \leq 4 \epsilon
$$

by an identical argument to Equation (55). Putting these together yields $\operatorname{d}_{\operatorname{TV}}\left(Z_{i_{1}, i_{2}}, Z_{i_{1}, i_{2}}^{\prime}\right) \leq 8 \epsilon$, which completes the proof of the lemma.

Lemma 8. Fix a positive scalar $\epsilon \leq 1 / 2$ and let $\tau \geq \mathrm{t}_{\text {mix }}(\epsilon)$ denote a positive integer. Let $n_{0}=n / \tau$. For each $j \in\left[n_{0}\right]$, define the stochastic process $\left(X_{k}^{\prime}\right)_{k \in \mathcal{D}_{j \tau}}$ as a $\left|\mathcal{D}_{j \tau}\right|$-length Markov chain with transition kernel $\boldsymbol{P}$ and initial state sampled from the distribution $\pi$ and independently of everything else. Let $S_{j}=\left\{\ell \in\left[n_{0}\right]:|\ell-j| \bmod 3 \equiv 0\right\}$. Now define the stochastic processes

$$
\begin{aligned}
W_{j} & =\bigoplus_{\ell \in S_{j}} X_{\mathcal{B}_{\ell}} \quad \text { and } \\
W_{j}^{\prime} & =\bigoplus_{\ell \in S_{j}} X_{\mathcal{B}_{\ell}}^{\prime}
\end{aligned}
$$

Then we have $\mathrm{d}_{\mathrm{TV}}\left(W_{j}, W_{j}^{\prime}\right) \leq n_{0} \cdot \epsilon$.

Consequently, for any function $f$ having range $[0,1]$, we have

$$
\left|\mathbb{E}\left[f\left(W_{j}\right)-f\left(W_{j}^{\prime}\right)\right]\right| \leq n_{0} \epsilon
$$

Proof. We prove the bound on total variation, noting that the consequence for bounded functions follows as a corollary. Denote $m=\left|S_{j}\right|$ as shorthand and index the elements of $S_{j}$ as $\ell_{1}, \ldots, \ell_{m}$. Fix $j$ and, for each $k=0,1, \ldots m$, define the auxiliary stochastic process

$$
\widetilde{W}_{j}^{(k)}=\left(\bigoplus_{k^{\prime}=1}^{k} X_{\mathcal{B}_{\ell^{\prime}}}\right) \bigoplus\left(\bigoplus_{k^{\prime}=k+1}^{m} X_{\mathcal{B}_{k^{\prime}}}^{\prime}\right)
$$

noting that $\widetilde{W}_{j}^{(m)}=W_{j}$ and $\widetilde{W}_{j}^{(0)}=W_{j}^{\prime}$. Then by the triangle inequality,

$$
\mathrm{d}_{\mathrm{TV}}\left(W_{j}, W_{j}^{\prime}\right) \leq \sum_{k=0}^{m-1} \mathrm{~d}_{\mathrm{TV}}\left(\widetilde{W}_{j}^{(k)}, \widetilde{W}_{j}^{(k+1)}\right)
$$

We now claim that

$$
\mathrm{d}_{\mathrm{TV}}\left(\widetilde{W}_{j}^{(k)}, \widetilde{W}_{j}^{(k+1)}\right) \leq \epsilon \text { for all } k=0,1, \ldots, m-1
$$

Since $m=\left|S_{j}\right| \leq n_{0}$, this claim immediately yields the desired result.

Proof of claim (64): For strings $s_{1}, \ldots, s_{k} \in \mathcal{X}^{2 \tau}$ each of length $2 \tau$, we let $\rho\left(s_{1}, \ldots, s_{k}\right)=$ $\operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{1}}}=s_{1}, \ldots, X_{\mathcal{B}_{\ell_{k}}}=s_{k}\right\}$. For additional strings ${ }^{5} s_{k+2}, \ldots, s_{m} \in \mathcal{X}^{2 \tau}$, we also define

$$
\mu\left(s_{k+2}, \ldots, s_{m}\right)=\operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+2}}}^{\prime}=s_{k+2}, \ldots, X_{\mathcal{B}_{\ell_{m}}}^{\prime}=s_{m}\right\} \text { for } s_{1}, \ldots, s_{m} \in \mathcal{X}^{2 \tau}
$$

Using the Markov property and the mutual independence of $\left\{X_{\mathcal{B}_{\ell}}^{\prime}\right\}_{\ell \in S_{j}}$, we have

$$
\begin{aligned}
& \mathrm{d}_{\operatorname{TV}}\left(\widetilde{W}_{j}^{(k)}, \widetilde{W}_{j}^{(k+1)}\right) \\
& \left.=\frac{1}{2} \sum_{s_{1}, \ldots, s_{k}, s, s_{k+2}, \ldots, s_{m} \in \mathcal{X}^{2 \tau}} \right\rvert\, \rho\left(s_{1}, \ldots, s_{k}\right) \cdot \operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}=s \mid X_{\mathcal{B}_{\ell_{1}}}=s_{1}, \ldots, X_{\mathcal{B}_{\ell_{k}}}=s_{k}\right\} \cdot \mu\left(s_{k+2}, \ldots, s_{m}\right) \\
& -\rho\left(s_{1}, \ldots, s_{k}\right) \cdot \operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}^{\prime}=s\right\} \cdot \mu\left(s_{k+2}, \ldots, s_{m}\right) \mid \\
& =\frac{1}{2} \sum_{s_{1}, \ldots, s_{k} \in \mathcal{X}^{2 \tau}} \rho\left(s_{1}, \ldots, s_{k}\right) \cdot \sum_{s \in \mathcal{X}^{2 \tau}}\left|\operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}=s \mid X_{\mathcal{B}_{\ell_{1}}}=s_{1}, \ldots, X_{\mathcal{B}_{\ell_{k}}}=s_{k}\right\}-\operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}^{\prime}=s\right\}\right|
\end{aligned}
$$

Next, we characterize the term $\sum_{s \in \mathcal{X}^{2 \tau}} \mid \operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}=s \mid X_{\mathcal{B}_{\ell_{1}}}=s_{1}, \ldots, X_{\mathcal{B}_{\ell_{k}}}=s_{k}\right\}-\operatorname{Pr}\left\{X_{\mathcal{B}_{k+1}}^{\prime}=\right.$ $s\} \mid$ for each fixed tuple $\left(s_{1}, \ldots, s_{k}\right)$. Let $s(i)$ denote the $i$-th element in the string $s$. Note that $(\tau-1) \ell_{k+1}+1$ is the first index of $\mathcal{B}_{\ell_{k+1}}$, and $\tau \ell_{k}$ is the index in $\mathcal{B}_{\ell_{k}}$. By the Markov property, we[^4]have

$$
\begin{aligned}
& \sum_{s \in \mathcal{X}^{2 \tau}}\left|\operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}=s \mid X_{\mathcal{B}_{\ell_{1}}}=s_{1}, \ldots, X_{\mathcal{B}_{\ell_{k}}}=s_{k}\right\}-\operatorname{Pr}\left\{X_{\mathcal{B}_{\ell_{k+1}}}^{\prime}=s\right\}\right| \\
& =\sum_{s(1) \in \mathcal{X}}\left|\operatorname{Pr}\left\{X_{(\tau-1) \ell_{k+1}+1}=s(1) \mid X_{\mathcal{B}_{\ell_{1}}}=s_{1}, \ldots, X_{\mathcal{B}_{\ell_{k}}}=s_{k}\right\}-\operatorname{Pr}\left\{X_{(\tau-1) \ell_{k+1}+1}^{\prime}=s(1)\right\}\right| \\
& \stackrel{(\mathrm{i})}{=} \sum_{s(1) \in \mathcal{X}}\left|\operatorname{Pr}\left\{X_{(\tau-1) \ell_{k+1}+1}=s(1) \mid X_{\tau \ell_{k}}=s_{k}(\tau)\right\}-\operatorname{Pr}\left\{X_{(\tau-1) \ell_{k+1}+1}^{\prime}=s(1)\right\}\right| \\
& \stackrel{(\mathrm{iii})}{=} \sum_{s(1) \in \mathcal{X}}\left|e_{s_{k}(\tau)}^{\top} P^{3 \tau+1} e_{s(1)}-\pi_{s(1)}\right|=: \sum_{s(1) \in \mathcal{X}}\left|\delta_{s_{k}(\tau), s(1)}\right| \stackrel{(\text { iii) }}{\leq} 2 \epsilon
\end{aligned}
$$

Above, equality (i) again uses the Markov property, equality (ii) uses the fact that $\ell_{k+1}=\ell_{k}+3$ by definition, and inequality (iii) uses Eq. (54). Plugging this into the previous display yields

$$
\mathrm{d} \operatorname{TV}\left(\widetilde{W}_{j}^{(k)}, \widetilde{W}_{j}^{(k+1)}\right)=\frac{1}{2} \sum_{s_{1}, \ldots, s_{k} \in \mathcal{X}^{2 \tau}} \rho\left(s_{1}, \ldots, s_{k}\right) \cdot 2 \epsilon=\epsilon
$$

This completes the proof of the lemma.

## B Intuition for data-dependent tuning of window size $\tau$

In this section, we provide some simple intuition to justify the data-dependent tuning procedure for the window size $\tau$ that we described in Section 6.1. Assuming that ${ }^{6} n \gg T_{\text {mix }}$, we have that $Z^{(1)}$ and $Z^{(2)}$ are near-independent since they are significantly separated within the sequence. Thus, conditioned on $Z^{(1)}$, the sequence $Z^{(2)}$ should be thought of as an independent Markov chain started at the stationary distribution $\pi$. Consequently, the random variable $\widetilde{M}\left(Z^{(1)}\right)$ ought to be close to the estimand $M_{\pi}\left(Z^{(1)}\right)$, and this can be formalized via a bounded differences inequality for mixing Markov chains (Paulin, 2015). Indeed, if independence between $Z^{(1)}$ and $Z^{(2)}$ held exactly, then it is straightforward to show that with high probability over the randomness in $Z^{(2)}$, we have

$$
\left|\widetilde{M}\left(Z^{(1)}\right)-M_{\pi}\left(Z^{(1)}\right)\right|^{2} \lesssim \frac{\mathrm{T}_{\mathrm{mix}} \log \left(n / \mathrm{T}_{\mathrm{mix}}\right)}{n}
$$

Now Theorem 1 guarantees that for some $\tau_{0} \asymp \mathrm{T}_{\text {mix }} \log \left(n / \mathrm{T}_{\text {mix }}\right)$, we must have the inequality ${ }^{7}$ $\left|\widehat{M}_{\mathrm{WINGIT}}\left(Z^{(1)} ; \tau_{0}\right)-M_{\pi}\left(Z^{(1)}\right)\right|^{2} \lesssim \frac{\tau}{n}$. Combining this observation with Ineq. (65) and noting that $\tau_{0} \asymp \mathrm{T}_{\text {mix }} \log \left(n / \mathrm{T}_{\text {mix }}\right)$, we have

$\left|\widehat{M}_{\mathrm{WINGIT}}\left(Z^{(1)} ; \tau_{0}\right)-\widetilde{M}\left(Z^{(1)}\right)\right|^{2} \leq 2\left|\widehat{M}_{\mathrm{WINGIT}}\left(Z^{(1)} ; \tau_{0}\right)-M_{\pi}\left(Z^{(1)}\right)\right|^{2}+2\left|M_{\pi}\left(Z^{(1)}\right)-\widetilde{M}\left(Z^{(1)}\right)\right|^{2} \lesssim \frac{\tau_{0}}{n}$.

Thus, we see that Ineq. (28) is a reasonable validation criterion since it is satisfied for some choice of window size at most $\tau_{0}$, for a suitable choice of constant $C_{\text {tune }}$ on the RHS. Conversely, if Ineq. (28)[^5]holds for some smaller window size $\tau=\widehat{\tau} \leq \tau_{0}$, then combining this with Ineq. (65) yields

$$
\begin{aligned}
\frac{1}{2}\left|\widehat{M}_{\mathrm{WINGIT}}\left(Z^{(1)} ; \widehat{\tau}\right)-M_{\pi}\left(Z^{(1)}\right)\right|^{2} & \leq\left|\widehat{M}_{\mathrm{WINGIT}}\left(Z^{(1)} ; \widehat{\tau}\right)-\widetilde{M}\left(Z^{(1)}\right)\right|^{2}+\left|M_{\pi}\left(Z^{(1)}\right)-\widetilde{M}\left(Z^{(1)}\right)\right|^{2} \\
& \lesssim \frac{\widehat{\tau}}{n}+\frac{\mathrm{T}_{\text {mix }} \log \left(n / \mathrm{T}_{\text {mix }}\right)}{n} \\
& \leq \frac{\tau_{0}}{n}+\frac{\mathrm{T}_{\text {mix }} \log \left(n / \mathrm{T}_{\text {mix }}\right)}{n} \lesssim \frac{\mathrm{T}_{\text {mix }} \log \left(n / \mathrm{T}_{\text {mix }}\right)}{n}
\end{aligned}
$$

Putting together the pieces, we see that our validation procedure is reasonable since (a) It is satisfied by the window size $\tau_{0}$ prescribed by Theorem 1, and (b) It always produces a good value of tuning window size $\widehat{\tau}$, in that this choice of window size leads to the optimal rate of estimation of the functional $M_{\pi}\left(Z^{(1)}\right)$.

It is important to note that the above sketch does not constitute a rigorous argument. In order to make it rigorous, one would have to formally establish Eq. (65) and also a version of Theorem 1 that holds with high probability, both of which are interesting directions for future work.


[^0]:    ${ }^{1}$ Indeed, one can verify that our procedure retains its estimation error guarantees even if $X_{1}$ is arbitrary.

[^1]:    ${ }^{2}$ Such a statement follows from noting that in Chandra et al. (2022, Eq. (6)): (a) We can set $T=2 /(1-\alpha$ ), and (b) When $n \geq \frac{2 \log n}{1-\alpha}=2 T \log n$, the second term on the RHS can be made less than half the first term.

[^2]:    ${ }^{3}$ In the regime $n \leq \mathrm{T}_{\text {mix }}$, the worst case risk of any estimator can be shown to be lower bounded by a constant, so our estimator is also trivially minimax-optimal in this regime.

[^3]:    ${ }^{4}$ Note that the small $\zeta$ regime, i.e. $\zeta=o(n)$, is the interesting one; we should expect accurate estimation to be possible for large $\zeta$ since the corresponding elements appear many times.

[^4]:    ${ }^{5}$ The last string $s_{m}$ may be of shorter length, but our argument can be modified straightforwardly to accommodate this case.

[^5]:    ${ }^{6}$ If $n \lesssim T_{\text {mix }}$, it is impossible to obtain consistent estimation anyway, at least in a minimax sense.

    ${ }^{7}$ Note that this step of the argument is heuristic, since Theorem 1 only gives such a guarantee in expectation.

