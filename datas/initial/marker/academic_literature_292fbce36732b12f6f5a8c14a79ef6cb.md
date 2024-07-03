# Just Wing It: Optimal Estimation Of Missing Mass In A Markovian Sequence

Ashwin Pananjady⋆,†, Vidya Muthukumar†,⋆, Andrew Thangaraj‡
Schools of Industrial and Systems Engineering⋆ and Electrical and Computer Engineering†,
Georgia Institute of Technology Department of Electrical Engineering‡, IIT Madras April 8, 2024

## Abstract

We study the problem of estimating the stationary mass—also called the unigram massthat is missing from a single trajectory of a discrete-time, ergodic Markov chain. This problem has several applications—for example, estimating the stationary missing mass is critical for accurately smoothing probability estimates in sequence models. While the classical Good–
Turing estimator from the 1950s has appealing properties for i.i.d. data, it is known to be biased in the Markov setting, and other heuristic estimators do not come equipped with guarantees. Operating in the general setting in which the size of the state space may be much larger than the length n of the trajectory, we develop a linear-runtime estimator called *Windowed Good–*
Turing (WingIt) and show that its risk decays as Oe(Tmix/n), where Tmix denotes the mixing time of the chain in total variation distance. Notably, this rate is independent of the size of the state space and minimax-optimal up to a logarithmic factor in n/Tmix. We also present a bound on the variance of the missing mass random variable, which may be of independent interest.

We extend our estimator to approximate the stationary mass placed on elements occurring with small frequency in Xn. Finally, we demonstrate the efficacy of our estimators both in simulations on canonical chains and on sequences constructed from a popular natural language corpus.

## 1 Introduction

Two classical problems in statistical analysis—relevant to both design of experiments and inference—are those of assessing *sample coverage* and *discovery probability*. Given a "training" sequence Xn = (X1, X2*, . . . , X*n) of random examples in some unknown sample space, the latter question concerns the probability with which an independent "test" observation Y will be a *discovery*, in that it is an element of the sample space that was unseen at training time. Equivalently, we are interested in estimating the *missing mass* in the training sample Xn, i.e. Pr{Y /∈ {X1*, . . . , X*n}}.

This problem has roots in statistical analysis for ecology (Fisher et al., 1943), and also has important applications across genomics (Favaro et al., 2012) as well as speech and language modeling (Church and Gale, 1991; Chen and Goodman, 1999). Let us give a few operational examples. For a first example from genomics (Lijoi et al., 2007), suppose we have performed genome sequencing on several genes of an organism as part of training data, and we are now interested in whether there is value in performing additional sequencing. Then the missing mass exactly measures the probability that we discover a new gene with additional sequencing, and an accurate estimate of this quantity can guide decisions about whether or not to sequence further. For a second example, consider the problem of building a probability model for a language corpus (Ney et al., 1994).

Many heuristic "smoothing" estimators have been developed for estimating these probability models (e.g., Ney et al., 1994; Jelinek, 1985; Gale and Sampson, 1995). A crucial component of these smoothing techniques is an estimate of the missing mass, since one would like to account for the (non-trivial) possibility that a word exists in the population corpus but has not yet been observed in the training data. Besides these two examples, estimates of the missing mass are also used in so-called competitive distribution estimation (Orlitsky and Suresh, 2015) and in estimating other functionals of distributions such as their entropy (Vu et al., 2007).

Many estimators with provable—and in fact minimax-optimal—guarantees exist for the case where the training data are exchangeable (Good, 1953; Lijoi et al., 2007; McAllester and Schapire, 2000). While the exchangeability assumption is reasonable in some applications, for example ecology (Shen et al., 2003; Colwell et al., 2012), it is clearly limiting in both genomics and speech or language applications, where temporal dependencies exist between the examples. The simplest form of such temporal dependence is Markovian structure, and, as articulated repeatedly in the literature (Hao et al., 2018; Chandra et al., 2021; Skorski, 2020), handling such structure in a principled fashion is an important first step for estimation of missing mass in temporally dependent training sequences. In spite of a significant body of work motivated by this topic, there still do not exist consistent estimators for missing mass functionals in general classes of Markovian sequences.

In this paper, we propose and theoretically analyze an estimator for the missing mass in a Markovian data sample, and variants for related problems. To make things concrete, suppose our stochastic process Xn:= (X1*, . . . , X*n) is modeled by a stationary Markov chain (P , π) on a finite but *unknown* state space X . We will make no assumptions on the alphabet size *|X |*,
and will be interested in also capturing the practically relevant large-alphabet setting, i.e. where |X | ≫ n. Here π = (πx)x∈X denotes the unique stationary distribution of the chain, and the matrix P ∈ [0, 1]*|X|×|X|* denotes the transition probability matrix of the Markov chain. We assume for convenience that X1 ∼ π, but this assumption can be straightforwardly relaxed1.

As previously mentioned, our primary goal is to estimate the mass of the Markov chain that is missing from the random sample Xn. Motivated by the questions above, we focus on the *stationary* missing mass of the chain, given by

$$M_{\pi}(X^{n}):=\sum_{x\in{\mathcal{X}}}\pi_{x}\cdot\mathbb{I}\left\{x\notin\{X_{1},\ldots,X_{n}\}\right\},$$
$$\quad(1)$$

where πx is the probability assigned by the stationary distribution π to element x ∈ X . Note that Mπ(Xn) is a *random functional*, as it depends not only on the parameters of the chain but also the random sample Xn. An equivalent definition—which resembles the description above—is given by

$$M_{\pi}(X^{n})=\operatorname*{\mathbb{E}}_{\begin{array}{l}{Y\circ\pi}\\ {Y\bot X^{n}}\end{array}}\left[\mathbb{I}\left\{Y\notin\{X_{1},\ldots,X_{n}\}\right\}\right],$$
[I {Y /∈ {X1*, . . . , X*n}}] , (2)
where U ⊥⊥ V denotes that random variables U and V are independent.

The missing mass is not the only functional that is relevant to discovery probabilities. A closely related functional is the *small-count* stationary probability, which measures the probability of seeing an element that had a frequency at most ζ in the training sequence (Lijoi et al., 2007; Favaro et al.,
2012). In particular, consider the estimand

 Remark, consider the solution  $M_{\pi,\leq\zeta}(X^n)=\underset{Y\to\widetilde{X}^n}{\to}\left[\mathbb{I}\left\{Y\text{appears at most}\zeta\text{times in}\left\{X_1,\ldots,X_n\right\}\right\}\right].$  can verify that our procedure retains its estimation error guarantees even if $X_1$ is arbitrary. 
$$\left(2\right)$$
$$\quad(3)$$
We will present detailed results for estimating the functional Mπ,≤ζ in Section 5, focusing up until that point on the missing mass.

Our goal is to produce an estimator Mc : X
n → [0, 1] with minimum risk, where risk is measured using the mean squared error. In particular, for an estimand M : X
n → [0, 1] and estimator Mc, we write

$$\operatorname{MSE}({\widehat{M}},M)={\frac{\mathbb{E}}{X^{n}}}\left[|{\widehat{M}}(X^{n})-M(X^{n})|^{2}\right].$$
$$\left(4\right)$$

Above, the expectation is taken over any other sources of randomness in Mc in addition to the randomness in the sequence Xn.

To set up some additional notions, we let ∥µ−ν∥TV denote the total variation distance between two probability measures µ and ν defined on the same space. Throughout, we assume that the Markov chain is ergodic and mixes in finite time. In particular, let tmix(ϵ) denote the mixing time of the chain to within total variation ϵ ∈ (0, 1/2] of the stationary measure, i.e.

$$\mathbf{t}_{\text{mix}}(\epsilon):=\min\ \left\{t\in\mathbb{N}:\max_{x\in\mathcal{X}}\|e_{x}^{\top}\mathbf{P}^{t}-\pi^{\top}\|_{\text{TV}}\leq\epsilon\right\},\tag{5}$$

where ex denotes the indicator vector on element x ∈ X and π is viewed as a *|X |*-dimensional column vector. The quantity tmix(1/4) is typically called the mixing time of the chain, and so we will write Tmix := tmix(1/4). It is straightforward to show (see, e.g. Levin and Peres (2017)) that

$$\mathbf{t}_{\operatorname*{mix}}(\epsilon)\leq\operatorname{T}_{\operatorname*{mix}}\cdot\log(1/\epsilon){\mathrm{~for~all~}}\epsilon<1/4.$$
$$\left({\mathrm{6}}\right)$$
tmix(ϵ) ≤ Tmix · log(1/ϵ) for all ϵ < 1/4. (6)

## 1.1 Related Work

The problem of estimating missing mass of a random sequence, where each element is drawn from an arbitrarily large sample space, was studied as far back as the 1800s by Laplace (1814), who proposed the first among the class of "add-constant" estimators. These estimators have seen a line of theoretical and empirical follow-up work (Krichevsky and Trofimov, 1981; Gale and Church, 1994), with special attention being paid to the add-1/2-estimator (Krichevsky and Trofimov, 1981). Instead of outputting the normalized empirical frequencies of elements as a maximum-likelihood estimator would, these estimators add a constant to the (un-normalized) empirical frequency prior to normalization. In the process, they output a non-zero missing mass probability.

A notable and groundbreaking result of Good (1953)—attributed also to Turing—moved away from the class of add-constant estimators and proposed to estimate the missing mass via the normalized frequency of elements appearing *once* in the sequence. In particular, letting ϕs(Xn)
denote the number of distinct elements of X that have appeared s times in the sample Xn, the celebrated Good–Turing estimator for the missing mass is given by

$$\widehat{M}_{\mathsf{G T}}=\frac{\phi_{1}(X^{n})}{n}.$$
n. (7)
The estimator has been applied to diverse areas (see, e.g., Song and Croft, 1999; Gale et al., 1992; Church and Gale, 1991) and has also seen intense theoretical study in the last three decades (see, e.g., McAllester and Schapire, 2000; Drukh and Mansour, 2005; Orlitsky et al., 2003). In particular, several analyses of fine-grained properties of the estimator now exist for the i.i.d. setting (see, e.g., Chandra et al., 2019; Rajaraman et al., 2017; Acharya et al., 2018), and variants of the estimator

$$\left(7\right)$$

have also been proposed and studied (Gandolfi and Sastri, 2004; Favaro et al., 2016; Painsky, 2022, 2023). While most analyses focus on additive error—e.g., the mean squared error of estimating the missing mass Mπ(Xn)—the multiplicative error metric has also been studied (Ohannessian and Dahleh, 2012; Mossel and Ohannessian, 2019; Ayed et al., 2021; Ben-Hamou et al., 2017; Grabchak and Zhang, 2017). Besides estimation, the missing mass random variable Mπ(Xn) has itself generated a lot of interest in the i.i.d. setting—its concentration properties have been thoroughly studied, and several analysis techniques have been developed along the way (McAllester and Ortiz, 2003; Berend and Kontorovich, 2012, 2013).

In contrast to the i.i.d. setting, the Markovian setting has received relatively sparse treatment, in spite of being the main setting—smoothing in language models—that motivated some of the initial papers on the theory of the subject (McAllester and Schapire, 2000, 2001). Some such papers include results for sticky Markov chains (Chandra et al., 2022) and rank-2 Markov chains (Chandra et al., 2021). These papers mainly study the performance of the Good–Turing estimator and/or certain scaled variants of it, and also give sufficient conditions under which Good–Turing can succeed for Markovian data. However, these conditions are restrictive, and it is not yet known if one can perform consistent, let alone minimax-optimal estimation of the missing mass in the general Markovian setting. Concentration of missing mass in the Markovian setting has also received some recent interest (Skorski, 2020)—we will discuss this paper in greater detail in the sequel.

The problem of estimating the small-count probability (3) has also been studied in the literature (Lijoi et al., 2007), along with the related problem of estimating the *exact count probability*,
i.e., the probability of elements occurring *exactly* ζ times (Good, 1953). Estimators of the count probability have been developed for i.i.d. samples, and several theoretical results are also available for this setting (McAllester and Schapire, 2001; Drukh and Mansour, 2005; Acharya et al., 2013).

The Markovian case, however, does not seem to have been theoretically studied.

Finally, we mention that besides the missing mass and count probabilities, other estimation and prediction problems (Hao et al., 2018; Han et al., 2023; Wolfer and Kontorovich, 2019) and bounds on 'surprise' probabilities (Norris et al., 2017) have been studied for Markov chains. The size of the state space appears explicitly as a parameter in these results.

## 1.2 Contributions And Organization Our Contributions Are Summarized Below:

- In Section 3, we propose an estimator for stationary missing mass in the Markov setting called the *Windowed Good–Turing*, or WingIt, estimator. Our estimator is based on the viewpoint of the Good–Turing estimator as a leave-one-out estimator, a perspective that we review (for the i.i.d. setting) and develop in Section 2.

- In Theorem 1 of Section 4, we provide a risk bound on the WingIt estimator, showing that it attains mean squared error on the order Tmix/n up to a logarithmic factor in n/Tmix. This matches, up to this logarithmic factor, the minimax lower bound for missing mass estimation in mixing Markov chains (Chandra et al., 2022).

- Aside from providing an estimator for the missing mass, we also analyze the missing mass functional Mπ(Xn) as a random variable, and show in Theorem 2 that its variance is bounded on the order Tmix/n up to a logarithmic factor. This constitutes, to our knowledge, the first such result in the Markovian setting, complementing a one-sided bound due to Skorski (2020).

- In Section 5, we present an extension of our methodology for estimating the small-count probability (3). Note that this generalizes the problem of estimating the stationary missing mass, which corresponds to the case ζ = 0. This result, stated as Theorem 3, appears to improve analogous guarantees from the literature even for i.i.d. samples.

- In Section 6, we provide simulations on some synthetic Markov chains and on natural language text. These experiments corroborate our theory while showing how the WingIt estimator can significantly outperform the vanilla Good–Turing estimator. We also explore an automatic and data-dependent tuning method for the window size in our WingIt estimator.
Notation: For two real numbers a and b, let a∧b = min{*a, b*} and a∨b = max{*a, b*}. Let [n] denote the set of natural numbers less than or equal to n. For an index set P ⊆ [n], let XP = {Xi}i∈P
denote the set of random variables corresponding to that index set. The set X[n]thus contains all random variables in the sequence Xn. With a slight abuse of notation, we let XP = (Xi)i∈P
denote the sequence of random variables with indices in P, ordered canonically. We use ⊕ to denote the concatenation of sequences, e.g., (X1, X2) ⊕ (X4, X5) = (X1, X2, X4, X5). For two sequences indexed by u, we use the notation f(u) ≲ g(u) to mean that there exists some absolute positive constant C that is independent of all problem parameters, such that f(u) ≤ C · g(u) for all u.

We use the notation f(u) ≳ g(u) when g(u) ≲ f(u). We write f(u) ≍ g(u) if both relations f(u) ≳ g(u) and g(u) ≲ f(u) hold. Logarithms are taken to the base e. We use (*c, C*) to denote universal positive constants that could be different in each instantiation.

## 2 From I.I.D. To Markov: Revisiting Good–Turing

First, let us revisit the special case where the samples Xn are i.i.d. and the stationary distribution π corresponds to the probability mass function from which each sample is drawn. Here, the celebrated Good–Turing estimator (7) of Mπ(Xn) is given by the number of symbols that appear *once* in Xn divided by the sample size n. As articulated by, e.g., McAllester and Schapire (2001), this quantity can be thought of as a *leave-one-out* estimate of the functional that repeatedly simulates a placeholder for Y from the given sample and approximately evaluates the indicator in Eq. (2). In particular, consider the collection of estimators given by the random variables

$$\widehat{M}^{(i)}=\mathbb{I}\left\{X_{i}\notin\{X_{1},\ldots,X_{i-1},X_{i+1},\ldots,X_{n}\}\right\}\quad\mathrm{for}\quad i=1,\ldots,n.$$
We can then equivalently write the Good–Turing estimator (7) as
$${\widehat{M}}_{\sf G T}={\frac{1}{n}}\sum_{i=1}^{n}{\widehat{M}}^{(i)}.$$
$$({\boldsymbol{\delta}})$$

$$(9)$$
Mc(i). (9)
Clearly, the random variable Xi "simulates" drawing a fresh sample Y from π independently of the subsequence (X1, . . . , Xi−1, Xi+1*, . . . , X*n), and inspecting Eq. (2) yields that Mc(i)is an unbiased estimator of Mπ(X1, . . . , Xi−1, Xi+1*, . . . , X*n). Using the i.i.d. nature of the observations, one can then show that (McAllester and Schapire, 2000)

$$\mathbb{E}[M_{\pi}((X_{1},\ldots,X_{i-1},X_{i+1},\ldots,X_{n}))]-M_{\pi}(X^{n})]|\lesssim n^{-1}.$$

so that we have a near-unbiased estimator of the quantity E[Mπ(Xn)]. Coupling this observation with additional arguments that bound the variance of the estimator McGT and estimand Mπ (McAllester and Schapire, 2000; McAllester and Ortiz, 2003), we obtain a bound on the meansquared error of the Good–Turing estimator.

It is instructive to re-examine the central pitfall of the Good–Turing estimator for a Markov chain, which is that strong local dependencies between adjacent samples in the Markov chain induce non-vanishing bias. This argument has been sketched before (see, e.g. Chandra et al. (2022)), but we nevertheless give a brief, self-contained illustrative example and a heuristic calculation of the bias below. Let X = [k] for some k ≫ n and consider transition kernels P ∈ [0, 1]k×k of the form

$$\mathbf{P}=(1-p)\mathbf{I}+p\mathbf{1}\pi^{\top},$$
$\left(10\right)^3$
⊤, (10)
where I and 1 denote the identity matrix and all-1s column vector of suitable dimensions. Such a transition kernel gives rise to a so-called "sticky", or lazy, Markov chain having stationary distribution π and mixing time 1 2p ≤ Tmix ≤
2 p for all k ≥ 2 and p ∈ (0, 1/2] (see Lemma 1). Thus, as the probability p becomes small, the mixing time becomes proportionally large.

Now suppose that π =
1 k 1, so that the stationary distribution is the uniform distribution on k elements. Due to the stickiness of the chain—i.e., its propensity to remain in its current state—we will see K ≍ np ≍ n/Tmix unique elements in a typical sample (X1*, . . . , X*n) of the chain. The stationary missing mass of the chain will hence be given, in expectation, by

$$\mathbb{E}[M_{\pi}(X^{n})]={\frac{k-\mathbb{E}[K]}{k}}\geq{\frac{k\mathsf{T}_{\mathrm{mix}}-C n}{k\mathsf{T}_{\mathrm{mix}}}}$$

for some universal constant C.

On the other hand, the Good–Turing estimator will obey E[McGT(Xn)] ≤ p. This is because for all i ∈ [n], we have

$\mathbb{E}[\widehat{M}_{\mathbb{G}\intercal}(X^{n})]=\mathbb{E}[\widehat{M}^{(i)}]=\Pr\{X_{i}\notin\{X_{1},\ldots,X_{i-1},X_{i+1},\ldots,X_{n}\}\leq\Pr\{X_{i}\neq X_{i-1}\}=p.$  **Corollary**: we have 
Consequently, we have
$$\left(\begin{array}{cccc}1&1&1&1\\ \end{array}\right)\leq\Pr\{X_{i}\neq X_{i-1}\}=p.\tag{11}$$
$$|\,\mathbb{E}[M_{\pi}(X^{n})-\widehat{M}_{\sf GT}(X^{n})]|\stackrel{{\rm(i)}}{{=}}\left|\frac{k\mathsf{T}_{\rm mix}-\mathbb{E}[K]}{k\mathsf{T}_{\rm mix}}-\frac{2}{\mathsf{T}_{\rm mix}}\right|\stackrel{{\rm(ii)}}{{=}}\frac{1}{4}$$  the fact that $p\in\left[\frac{1}{2\mathsf{T}_{\rm mix}},\frac{2}{\mathsf{T}_{\rm mix}}\right]$ and step (ii) holds as long as 
where step (i) uses the fact that p ∈
Tmix iand step (ii) holds as long as k ≥ Cn/Tmix for a sufficiently large constant C > 0 and Tmix ≥ 8. Applying Jensen's inequality yields the lower bound

$${\mathsf{M S E}}({\widehat{M_{\mathsf{G T}}}},M_{\pi})\geq|\operatorname{\mathbb{E}}[M_{\pi}(X^{n})-{\widehat{M_{\mathsf{G T}}}}(X^{n})]|^{2}\geq1/16,$$
2 ≥ 1/16, (12)
thus illustrating that the Good–Turing estimator has constant, non-vanishing bias for sticky Markov chains in which the stationary distribution is uniform on a large state space. This phenomenon is also empirically illustrated in Figure 2 in Section 6.

While the biased nature of the Good–Turing estimator is unfortunate, we next build on some important design principles sketched here in order to develop an unbiased estimator.

## 3 Methodology: The Windowed Good–Turing Estimator

In this section, we describe a natural modification of the Good–Turing estimator, interpreted through the leave-one-out lens (8), that mitigates the above issues and estimates the stationary missing mass at a minimax-optimal rate.

$$\left(12\right)$$

## 3.1 A First Step: Modifying The "Leave-One-Out" Estimator To Reduce Its Bias

The central issue with the original leave-one-out estimator Mc(i)(8) when applied to Markov chains lay in the strong dependencies induced between adjacent samples of the chain: As demonstrated by Eq. (11), successive samples Xi and Xi−1 are tightly coupled through the structure of the transition kernel and very far from being independent. To mitigate this issue, we modify the leaveone-out estimator to a "leave-a-window-out" estimator that removes the samples adjacent to Xi before computing the corresponding estimator. We first illustrate the idea for i = n for simplicity.

Recall that Mc(n) = I {Xn ∈ { / X1*, . . . , X*n−1}}. Instead of using the leave-one-out subsequence
(X1*, . . . , X*n−1) as a proxy for Xn, we use the slightly smaller subsequence (X1*, . . . , X*n−τ ). As long as we choose τ ≫ Tmix, we should expect that (X1*, . . . , X*n−τ ) is nearly independent of Xn.

Accordingly, we define the estimator

$$\widehat{M}_{\tau}^{(n)}:=\mathbb{I}\left\{X_{n}\not\in\left\{X_{1},\ldots,X_{n-\tau}\right\}\right\}.$$
$\left(13\right)$. 
τ:= I {Xn ∈ { / X1*, . . . , X*n−τ }}. (13)
7
To develop some quantitative intuition, suppose for the moment that Xn were exactly independent of (X1*, . . . , X*n−τ ), and recall that the marginal distribution of Xnis the stationary measure π.

Then by construction, the random variable Mc(n)
τ would be an unbiased estimator of Mπ(Xn−τ),
which one should expect, in turn, to be close to the desired missing mass Mπ(Xn). More formally, Lemmas 2 and 4 (referenced in the proof of Theorem 1) use an approximate-independence argument and show that for sufficiently large τ , we have

$$\mathbb{E}[M_{\pi}(X^{n-\tau})-M_{\pi}(X^{n})]\stackrel{<}{\sim}\frac{\tau}{n}.$$

Thus, the bias of Mc(n)
τ now decays with the "effective" sample size n0 := n/τ .

## 3.2 Wingit: Averaging An Ensemble Of Windowed Leave-One-Out Estimators

Above, we have produced a single random variable Mc(n)
τ with decaying bias. However, we still have the issue of variance. How do we construct multiple estimators like Mc(n)
τ and average over them as in Eq. (9)? The natural idea to construct the i-th such estimator is to inspect the definition (13),
replace Xn with Xi, and the set {X1*, . . . , X*n−τ } with the portion of the sequence Xnthat should behave as nearly independent of Xi. Concretely, for each i ∈ [n], define the index sets

$${\mathcal{D}}_{i}=\{k\in[n]:|k-i|<\tau\}\quad{\mathrm{~and~}}\quad{\mathcal{I}}_{i}=[n]\setminus{\mathcal{D}}_{i}.$$
Di = {k ∈ [n] : |k − i| < τ} and Ii = [n] \ Di. (14)
In words the set Di contains indices that are close to i, so that if τ ≫ tmix then we should expect XDi to be the set of random variables in the sequence that depend on Xi. On the other hand, the complementary set Iiis the index set of random variables that are nearly independent of Xi. The above intuition then leads naturally to the estimator

$$\widehat{M}_{\tau}^{(i)}:=\mathbb{I}\left\{X_{i}\notin X_{\mathcal{I}_{i}}\right\},$$
}, (15)
which generalizes Mc(n)
τ to any index i. Finally, we combine these estimates to reduce variance.

Letting n0 := ⌊n/τ ⌋, we create the final estimator

$$\widehat{M}_{\mathrm{WingIT}}(\tau)=\frac{1}{n_{0}}\sum_{j=1}^{n_{0}}\widehat{M}_{\tau}^{(j\tau)}.$$
$\left(14\right)^3$
$$(15)$$
$$(16)$$

Note that we have not used the random variables Mc(i)
τ for all i ∈ [n]; instead, we have skipped samples at intervals of the window size τ to attempt to decorrelate the summands in Eq. (16) while still benefiting from averaging. Note that if τ = 1, then we recover the Good–Turing estimator (9).

See Figure 5 later in the paper for an illustration of the windowing procedure.

## 3.3 Linear Time Implementation Of Wingit

As presented in Eqs. (15) and (16), the WingIt estimator can be naively implemented in O(n 2)
time, since each estimator Mc(i)
τ can be computed by searching through the entire sequence. In this section, we show that, in fact, the entire estimator McWingIt(τ ) can be computed in time O(n) time for any value of the window size τ . The computational complexity of the WingIt estimator is thus comparable to that of the vanilla Good–Turing estimator (7). Given a sequence Xn and a natural number τ , the algorithm proceeds via two passes through the data:

1. Iterate through indices i = 1*, . . . , n* while forming a dictionary locations with keys as elements in X and values as lists containing indices. If 'Xi' exists already as a key, append i to its list value; otherwise create a key 'Xi' and associate to it a list containing i. Eventually, for each x ∈ X[n], locations['x'] will contain a list of all indices at which x appears in the sequence, sorted in increasing order.

2. Next, iterate through window indices j = 1*, . . . , n*0. For each j, call the list locations['Xjτ ']
and inspect its first element ℓj and last element rj . Let Pj = I {|jτ − ℓj | < τ}·I {|rj − jτ | < τ}.

3. Return the estimate 1 n0 Pn0 j=1 Pj .
Correctness: It suffices to show that in step 2 we have Pj = IXjτ ∈/ XHjτ 	= M
(jτ)
τ for all j ∈ [n0]. To evaluate the indicator IXjτ ∈/ XHjτ 	—or equivalently, the indicator IXjτ ∈/ XHjτ 	—
we must check if there exists some index k ∈ [n] such that |k − jτ | ≥ τ and Xk = Xjτ . But note that by construction, the list locations['Xjτ '] contains indices k ∈ [n] sorted in increasing order such that Xk = Xjτ . Thus, we have

max
$$\operatorname*{max}_{X_{k}=X_{j\tau}}|j\tau-k|=\operatorname*{max}\{|j\tau-k|\}$$
|jτ − k| = max{|jτ − ℓj |, |rj − jτ |}
and it suffices to compare jτ with the first (i.e. smallest) and last (i.e., largest) element of the list locations['Xjτ '].

Running time: Step 1 requires a single pass through the data and O(n) time in total. In step 2, for each value of j, we access only the first and last element of the list locations['Xjτ '], which takes two operations in a Python implementation. The total running time of step 2 is therefore O(n) and step 3 also takes O(n0) = O(n) time, resulting in an overall algorithm that runs in linear time. Memory: The memory requirement is dominated by the dictionary creation in step 1. We create a list for each dictionary key, and the sum of sizes of all lists is equal to the number of elements observed, i.e., n. So the memory, assuming each element of X and [n] can be stored in constant space, is O(n).

Having proved that the WingIt estimator can be computed using linear time and space, we now turn to studying its estimation error properties.

## 4 Theoretical Results On Missing Mass Estimation

This section presents a risk guarantee for McWingIt and a variance bound on the estimand Mπ(Xn).

## 4.1 Risk Guarantee For The Wingit Estimator

We first provide a guarantee for the risk of the estimator McWingIt (16). Recall the definition (5)
of the mixing time up to arbitrary total variation tmix(ϵ) and that we write Tmix = tmix(1/4).

Theorem 1. *Suppose we choose* τ ≥ tmix (Tmix/n)
2 ∧ 1/4*, and let* McWingIt(τ ) *denote the estimator defined in Eq.* (16). Then there is an absolute positive constant C *such that*

$$\mathsf{M S E}({\widehat{M}}_{\mathrm{WingIT}}(\tau),M_{\pi})\leq C\cdot{\frac{\tau}{n}}\wedge1.$$
$$(17)$$

Before proceeding to our detailed discussion of the Markov case, we note in passing that the MSE
guarantee (17) recovers existing guarantees (McAllester and Schapire, 2000; Rajaraman et al., 2017)
for the Good–Turing estimator, since in the i.i.d. case the chain mixes in one step, our estimator specializes to Good–Turing, and we may set τ = 1 in Theorem 1.

A few remarks on the general Markov case are now in order. We assume that n ≥ 2Tmix in all the remarks below; if n < 2Tmix, then the RHS in Eq. (17) reduces to a universal constant and conversely, it is straightforward to show that consistent estimation is impossible (see footnote 3 below). Let us now proceed to our discussion.

First, observe that if n ≥ 2Tmix, it follows from the mixing condition in Eqs. (5) and (6) that tmix (
Tmix n
)
2 ∧ 1/4
≤ 2Tmix · log(n/Tmix). Therefore, if we know Tmix up to a universal constant factor—estimators for the mixing time are available in the literature for, e.g. for reversible Markov chains (Hsu et al., 2019)—then we can set the window size τ ≍ Tmix · log(n/Tmix) and obtain

$${\mathsf{M S E}}({\widehat{M}}_{\mathrm{WingIT}}(\tau),M_{\pi})\lesssim{\frac{\mathsf{T_{m i x}}}{n}}\cdot\log(n/\mathsf{T_{m i x}}).$$

In practice, one would need to tune τ , and we sketch a possible tuning method in Section 6.

Second, we remark on the issue of optimality. Chandra et al. (2022) proved a minimax lower bound of order Ω((np)
−1) on the mean squared error of estimating missing mass in sticky chains of the form (10). As remarked on before (see Lemma 1), such chains have a mixing time Tmix ≍ p
−1, so this yields a lower bound of Ω(Tmix/n) for such chains. Theorem 1 matches this lower bound up to the logarithmic factor log(n/Tmix) and further holds for all chains of mixing time at most Tmix.

More formally, define the class of Markov chains that mix in time at most T, as Pmix(T) := {Markov chain (P , π) : mixing time of chain Tmix is at most T}.

Theorem 1 implies that for a universal constant C > 0, we have the worst-case upper bound

$$\sup_{(\mathbf{P},\pi)\in\mathcal{P}_{\text{mix}}(T)}\text{MSE}(\widehat{M}_{\text{WinGTr}}(2T\log n),M_{\pi})\leq C\cdot\frac{T\log(n/T)}{n}.\tag{18a}$$

On the other hand, we may state2the minimax lower bound (Chandra et al., 2022, Theorem 2) as the following: There is a universal constant c > 0 such that if n ≥ 2T log n then for any estimator 2Such a statement follows from noting that in Chandra et al. (2022, Eq. (6)): (a) We can set T = 2/(1 − α), and
(b) When n ≥
2 log n 1−α = 2T log n, the second term on the RHS can be made less than half the first term.

Mc that is a measurable function of the observations Xn, we must have

$$\sup_{(\mathbf{P},\pi)\in\mathcal{P}_{\rm min}(T)}\mathsf{MSE}(\widehat{M},M_{\pi})\geq c\cdot\frac{T}{n}.\tag{18b}$$

Taken together, Eqs. (18a) and (18b) thus imply that in the regime3 n ≳ T log n, the WingIt estimator is information-theoretically minimax optimal up to a logarithmic factor in n. Removing this logarithmic factor is an interesting open problem, and will likely require new ideas both in terms of algorithm design and analysis.

Finally, we comment on our analysis path, which is significantly different from the related literature on missing mass estimation from an i.i.d. sequence. As alluded to before, a natural and popular method to analyze estimators of the missing mass in the i.i.d. setting (McAllester and Schapire, 2000, 2001) is to exploit concentration of the estimand and write

$$\mathsf{MSE}(\widehat{M},M_{\pi})\leq3|\,\mathbb{E}\,[\widehat{M}(X^{n})]-\,\mathbb{E}\,[M_{\pi}(X^{n})]|^{2}+3\,\mathrm{var}(\widehat{M}(X^{n}))+3\,\mathrm{var}(M_{\pi}(X^{n})),\tag{19}$$

which can be obtained by adding and subtracting terms and using the elementary inequality (a +
b+c)
2 ≤ 3(a 2+b 2+c 2). Operationally, therefore, analyzing the MSE of the estimator relies in itself on understanding the variance of the missing mass random variable Mπ(Xn), which has nothing to do with the estimator. In the Markovian case, it appears challenging to control var(Mπ(Xn))
by straightforward means. Other analysis techniques for missing mass estimation in the i.i.d.

setting (e.g. Rajaraman et al., 2017; Chandra et al., 2019) work with an exact decomposition of the MSE expressed as a sum of weighted indicators over pairs of elements x, x′ ∈ X , and use the i.i.d. assumption to bound these terms in a precise fashion. One such property that is used to show concentration is the negative associativity of certain random variables (McAllester and Ortiz, 2003), and we do not expect this property to hold for general Markov chains.

In contrast to these approaches, we begin with a nonstandard decomposition of the MSE by conditioning on the sequence Xn, and our argument deviates significantly from Eq. (19). Besides the nonstandard decomposition, we also call out a few other features of the proof. Throughout, owing to the structure of our estimator (16), we must compare our random sequence Xnto suitably modified random sequences with windows of random variables left out; we do so by proving certain total variation bounds for Markov bridges, in Lemmas 6 and 7. Another important but delicate feature of our proof is that we are able to obtain the sharp near-linear dependence of the rate on Tmix—in order to do this, we bound a certain functional of hitting times in independent draws of a shorter Markov chain (Lemma 4) and show that our Markovian sequence Xncan be approximated in some appropriate sense by such independent shorter Markovian draws via repeatedly restarting the chain at stationarity (Lemma 8).

## 4.2 Variance Of Missing Mass Functional Mπ(Xn)

The analysis path that we sketched above circumvents needing to control the variance of the estimand, i.e. var(Mπ(Xn)). Nevertheless, and somewhat surprisingly, analyzing various properties of the estimator McWingIt allows us to indirectly bound var(Mπ(Xn)). We state this result as the following theorem, which could be of independent interest.

3In the regime n ≤ Tmix, the worst case risk of any estimator can be shown to be lower bounded by a constant, so our estimator is also trivially minimax-optimal in this regime.

Theorem 2. There is an absolute positive constant C *such that*

$$\operatorname{var}(M_{\pi}(X^{n}))\leq C\cdot{\frac{\mathsf{T_{m i x}}\cdot\log(1+n/\mathsf{T_{m i x}})}{n}}\wedge1.$$
$$(20)$$

Theorem 2 is proved in Section 7.2. En route, we control the bias and variance of the estimator McWingIt, which—owing to our nonstandard error decomposition—are related but distinct quantities from the MSE that was characterized in Theorem 1.

The most related result to Theorem 2 was proved by Skorski (2020), who showed a *one-sided* tail bound on Mπ(Xn) in terms of the hitting time of large sets of the Markov chain. Even though the hitting time of large sets is comparable to the mixing time (Oliveira, 2012; Peres and Sousi, 2015), the main result of Skorski (2020) cannot, strictly speaking, be compared with Theorem 2. On the one hand, Theorem 2 implies the two-sided polynomial tail bound

$$\operatorname*{Pr}\left\{|M_{\pi}(X^{n})-\mathbb{E}[M_{\pi}(X^{n})]|\geq\epsilon\right\}\leq C\cdot{\frac{\mathsf{T}_{\mathrm{mix}}\log(1+n/\mathsf{T}_{\mathrm{mix}})}{n\epsilon^{2}}}{\mathrm{~for~all~}}\epsilon>0,$$

which can be obtained via direct application of Markov's inequality. On the other hand, Skorski (2020, Corollary 1) provides a stronger exponentially decaying bound, but only on the upper tail.

In the result of Skorski (2020), the random variable Mπ(Xn) is also not centered at its expectation.

Having discussed estimation guarantees for the missing mass, we now turn to the problem of estimating small-count probabilities.

## 5 Estimating Stationary Mass Of Elements With Frequency At Most Ζ

In this section, we show that the idea behind the WingIt estimator can be applied robustly to estimate not only the missing mass functional Mπ(Xn), but also the mass of all elements that occur at most ζ times (3). To define this functional formally, let Nx(XP ) = Nx(XP ) := Pi∈P
I {Xi = x}
denote the number of occurrences of the element x ∈ X in the (sub)-sequence XP and subset XP .

Then, the mass of all elements that occur *exactly* ζ times is defined as

$$M_{\pi,\zeta}(X^{n}):=\sum_{x\in{\mathcal{X}}}\pi_{x}\cdot\mathbb{I}\left\{N_{x}(X^{n})=\zeta\right\}.$$
πx · I {Nx(Xn) = ζ}. (21)
We focus on the mass of all elements that occur *at most* ζ times (cf. the definition in Eq. (3))

$$M_{\pi,\leq\zeta}(X^{n}):=\sum_{x\in{\mathcal{X}}}\pi_{x}\cdot\mathbb{I}\left\{N_{x}(X^{n})\leq\zeta\right\}.$$

Clearly, both Eq. (21) and Eq. (22) recover the missing mass functional Mπ(Xn) when ζ = 0. For small ζ, both of these functionals provide more fine-grained information about the mass placed by the stationary distribution on low-frequency elements of Xn. We now define a natural extension of the WingIt estimator for the functional Mπ,≤ζ (Xn) that retains the leave-a-window-out principle. In particular, recalling our notation from Eq. (14), we generalize the missing mass estimator Mc(i)
τ (15) via

$$\widetilde{M}_{r,\leq\zeta}^{(t)}:=\mathds{1}\left\{N_{X_{t}}(\mathbf{X}_{\mathbf{Z}_{t}})\leq\zeta\right\},\quad\text{and construct the estimator}\quad\widetilde{M}_{\text{Wwd}\mathds{1},\leq\zeta}(\tau):=\frac{1}{n_{0}}\sum_{j=1}^{n_{0}}\widetilde{M}_{r,\leq\zeta}^{(r)}.\tag{23}$$
$$(21)$$
$$(22)$$

The following theorem shows that the estimator McWingIt,≤ζ (τ ) has small MSE.

Theorem 3. *Suppose we choose* τ ≥ tmix (Tmix/n)
2 ∧ 1/4*, and let* McWingIt,≤ζ (τ ) *denote the* estimator defined in Eq. (23). Then there is an absolute positive constant C *such that*

$$\mathsf{M S E}(\widehat{M}_{\mathrm{WingIT},\leq\zeta}(\tau),M_{\pi,\leq\zeta})\leq C\cdot\frac{(\zeta+1)\tau}{n}\wedge1.$$
∧ 1. (24)
Theorem 3 is proved in Section 7.3; a few remarks on the result follow. First, note that by setting ζ = 0, Theorem 3 recovers Theorem 1, our result for missing mass, since the estimator McWingIt,≤0(τ ) coincides with the missing mass estimator McWingIt(τ ). The main technical results that enable this generalization are given by Lemmas 3 and 5; the proof is otherwise structured similarly to the proof of Theorem 1. Second, note that McWingIt,≤ζ (τ ) is an estimate of the stationary mass of all elements occurring at most ζ times in the sample Xn, and corresponds to a notion of discovery probability (Favaro et al., 2012). In particular, setting τ ≍ Tmix log(1 + n/Tmix) yields

$$\mathsf{MSE}(\widehat{M}_{\mathrm{Wscr},\leq\zeta}(\tau),M_{\pi,\leq\zeta})\leq\frac{(\zeta+1)\mathsf{T}_{\mathsf{mix}}}{n}\cdot\log(1+n/\mathsf{T}_{\mathsf{mix}}).\tag{25}$$  To our knowledge, a result equivalent to Eq. (25) with linear dependence on $\zeta+1$ is not directly 
available in the literature, even in the i.i.d. setting. In fact, it is instructive to revisit the i.i.d.

setting for small-count probabilities and compare with the Good–Turing estimator (Good, 1953).

Remark 1. Recalling the notation ϕs(Xn) for the number of elements of the sample space X that occur s times in Xn, the Good–Turing estimator for the functional Mπ,ζ (Xn) (21) *is given by* McGT,ζ =
ζ+1 n
·ϕζ+1(Xn). The natural estimator for Mπ,≤ζ (Xn) is then given by McGT,≤ζ =Pζs=0 McGT,s. Conversely, we obtain an estimator of the exact-count functional Mπ,ζ *from our estimator* McWingIt,≤ζ .

In particular, we can construct the estimator McWingIt,ζ (τ ) := McWingIt,≤ζ (τ ) − McWingIt,≤(ζ−1)(τ ),
which can be interpreted as writing

$$\widehat{M}_{r,\zeta}^{(t)}:=\mathbb{I}\left\{N_{X_{i}}(\mathbf{X}_{\mathbb{Z}_{i}})=\zeta\right\},\quad\text{and constructing the estimator}\quad\widehat{M}_{\mathrm{WEGrt},\zeta}(\tau)=\frac{1}{n_{0}}\sum_{j=1}^{n_{0}}\widehat{M}_{r,\zeta}^{(j r)}.$$  In the case of a set $\tau=\{\mathbb{I}_{\zeta},\,M_{r,\zeta}\}$, we have $\mathbb{I}_{\zeta}\subset\mathbb{I}_{\zeta}$, $\mathbb{I}_{\zeta}\subset\mathbb{I}_{\zeta}$, $\mathbb{I}_{\zeta}\subset\mathbb{I}_{\zeta}$, \(\mathbb{I}_{\zeta}\subset\mathbb{I
$$(24)$$

The leave-one-out perspective (McAllester and Schapire, 2001) then yields the following consequence for τ = 1 *in our estimator: We have* McWingIt,ζ (1) = MGT,ζ *, and therefore* McWingIt,≤ζ (1) = MGT,≤ζ .

Following up on the observation in Remark 1, one can ask if existing analyses of the Good–
Turing estimator recover the guarantee of Theorem 3 in the special case of i.i.d. observations.

Applying the result of Drukh and Mansour (2005) (which is for the MSE of McGT,ζ ) yields

$$\mathsf{MSE}(\widehat{M}_{\mathsf{GT},\leq\zeta},M_{\pi,\leq\zeta})\stackrel{{\eqref{eq:mse}}}{{=}}\zeta\sum_{s=0}^{\zeta}\mathsf{MSE}(\widehat{M}_{\mathsf{GT},s},M_{\pi,s})=\zeta\sum_{s=0}^{\zeta}\frac{\sqrt{s}}{n}+\left(\frac{s}{n}\right)^{2}\leq\frac{\zeta^{5/2}}{n}\wedge1,$$  for $(i)$ follows from the inequality $(\sum_{s=0}^{\zeta}\frac{1}{n})^{2}<\zeta\sum_{s=0}^{\zeta}\frac{1}{n}$. However, setting $\zeta=\zeta$

$$(26)$$
$$\mathbf{T}_{\uparrow}$$
∧ 1, (26)
where step (i) follows from the inequality (Pζs=0 as)
2 ≤ ζPζs=0 a s
. However, setting τ = 1 in Theorem 3, we see that Eq. (24) improves the guarantee (26) even in the i.i.d. case, showing that MSE(McGT,≤ζ , Mπ,≤ζ )
(i)
= MSE(McWingIt,≤ζ (1), Mπ,≤ζ ) ≲ (ζ + 1)/n, (27)
where step (i) follows from Remark 1. The problems of whether the rate (27) and its Markovian analog (25) are information-theoretically optimal for estimating the small-count4 probability Mπ,≤ζ are interesting and, to our knowledge, open, both in the i.i.d. and Markovian settings.

4Note that the small ζ regime, i.e. ζ = o(n), is the interesting one; we should expect accurate estimation to be possible for large ζ since the corresponding elements appear many times.

## 6 Numerical Experiments

In this section, we provide a set of simulations on synthetically constructed Markov chains and on natural language text in order to corroborate our theoretical results, in particular Theorem 1. Before proceeding to the experiments themselves, we describe in Section 6.1 a data-dependent tuning procedure of the window size τ in the estimator McWingIt(τ ).

Code and the text used for the simulations are available at Thangaraj et al. (2024).

## 6.1 Data-Dependent Tuning Of Window Size Τ

Theorem 1 prescribes that we choose the window size τ to be at least on the order Tmix log(1 + n/Tmix). An important question to address is how to choose the window size τ when we do not have access to a valid upper bound on Tmix. We now propose a validation procedure to select τ ,
and test this procedure in the experiments in the sequel. For this section, assume n is divisible by 3 for notational convenience.

Given the sequence Xn, we choose a candidate window size τb via the following procedure.

We first split the sequence into the first one-third Z
(1) = (X1*, . . . , X*n/3) and the final one-third Z
(2) = (X2n/3+1*, . . . , X*n) and compute the random variable

$$\widetilde{M}(Z^{(1)})=\frac{1}{(n/3)}\sum_{i=2n/3+1}^{n}\mathbb{I}\left\{X_{i}\notin\{X_{1},\ldots,X_{n/3}\}\right\}.$$

Next, iterate τ = 1, 2, 4*, . . . ,* 2
⌊log2
(n/6)⌋in increasing order, and compute McWingIt(τ ) on the sequence Z
(1); denote this random variable by McWingIt(Z
(1); τ ) for convenience. We then set τb to be the smallest τ among this set such that

$$\widehat{M}_{\rm WNgIT}(Z^{(1)};\tau)-\widetilde{M}(Z^{(1)})\Big{|}^{2}\leq\frac{C_{\rm tune}\,\tau}{(n/3)}\tag{28}$$

for a suitable choice of the constant Ctune > 0. If such an inequality is not satisfied for any τ in the prescribed list, then we set τb = n/6. Appendix B provides some intuition for why this procedure is reasonable as an automatic tuning method. We next show that empirically, this tuning method is competitive with the optimally chosen window size.

## 6.2 Experiments On Simulated Markov Chains And Natural Language Text

For the simulated Markov and natural language text sequences considered in this section, we vary the sequence length n and plot the MSE of the estimator McWingIt(τ ) as a function of n for different values of the window size τ . We also plot the MSE of the tuned estimator McWingIt(τb). Note that the special case τ = 1 corresponds to the Good–Turing estimator (7). We also plot (in dashed lines)
the result of the tuning procedure that we described in Section 6.1, with the constant Ctune = 1.

Every point in these plots is generated by averaging the results of multiple sequences generated from the source.

First, and as a sanity check, we consider the case of the trivial Markov chain formed by i.i.d.

samples. For generating n samples, we consider the uniform distribution over the state space X = {1, 2*, . . . ,* ⌊1.2n⌋}, which is close to the worst-case distribution for the Good–Turing estimator.

Moreover, this ensures that the missing mass Mπ(Xn) is significant. Figure 1 shows two plots. The

![13_image_0.png](13_image_0.png)

plot on the left is that of the MSE of the estimator McWingIt(τ ) as a function of sequence length n for various values of the window size τ and for tuned τb. The plot on the right shows the mean values (over the 100 runs) of the triple of random variables (Mπ, Mc(1), Mc(τb)) along with the 90 percentile confidence bar (5th to 95th percentile). Observe that on the one hand—and as expected in the i.i.d. setting with mixing time Tmix = 1—the minimum MSE is attained when τ = 1, i.e., by the vanilla Good–Turing estimator (7). On the other hand, the MSE is only marginally higher for higher values of the window size τ , and all estimators appear to enjoy the same rate of decay of MSE
in the sequence length n. In other words, the effect of misspecifying τ appears as a multiplicative constant in the error, as predicted by Theorem 1. The MSE of Mc(τb) with tuned τb (dashed line) is close to the minimum attained MSE. In the plot to the right, the mean values of missing mass Mπ and the estimators Mc(1), Mc(τb) are almost overlapping for all n. The confidence bars for the three quantities are shown as a wide blue bar for Mπ, an orange bar for Mc(1) and as a capped black line for Mc(τb). The confidence bars, narrow to begin with, shrink to negligible lengths as n increases.

In our second experiment, we once again consider the state space X = {1*, . . . ,* ⌊1.2n⌋}. We simulate the sticky Markov chain (10) with p = 0.5 and stationary distribution given by the uniform distribution on X , i.e., πx =1
⌊1.2n⌋
for all x ∈ X . As before, we simulate the performance of the WingIt estimator as a function of n for different values of window size τ , and present our results in Figure 2. In the MSE plot to the left, we observe the following. In contrast to the previous i.i.d. example, we now find that the choice τ = 1 is a poor one, and that the error of the estimator does not decay with the sample size n. As expected from the analysis presented in Section 2, the vanilla Good–Turing estimator (7) indeed suffers a constant bias in this setting. Note that by Lemma 1, the mixing time of this chain is bounded as Tmix ∈ [1, 4], and Theorem 1 predicts that the estimator should succeed when the window size is larger than Tmix. This prediction is borne out in simulation: While the estimator exhibits constant bias even when τ = 4, when τ = 8 the MSE suddenly becomes consistent in n. Further increases in the window size τ preserve the consistency of the estimator while increasing the MSE by multiplicative constant factors. In the plot to the right in Figure 2, we see that the mean value of missing mass coincides with the mean value of

![14_image_0.png](14_image_0.png)

both the estimators (one with τ = 8 and the other with tuned window size) for larger values of n. For n < 2000, the mean of the estimator McWingIt(8) almost coincides with missing mass, while the mean of McWingIt(τb) is smaller. The confidence bars for both estimators are wider than that of the missing mass for n < 2000 though they narrow quickly as n grows. These observations suggest that the tuning procedure could be possibly improved, particularly for small n.

![14_image_1.png](14_image_1.png)

In our next experiment, we simulate the sticky Markov chain (10) with p ≜ 1 − p = 0.1, 0.5, 0.9 setting the state space and stationary distribution as before. The aim of this experiment is to examine more closely the influence of the stickiness parameter p on the optimal choice of window size τ . The same simulations are performed and results are compared in Figure 3. The best
(power of 2) window sizes for p = 0.1, 0.5, 0.9 are observed through simulations to be, respectively, τ = 4, 8, 64. The plot to the left shows the MSE of McWingIt(τ ) for the best observed window size (called "best") and for the data-tuned window size τb (called "tuned"). For the least sticky chain (p = 0.1), the tuned and the best estimators have overlapping MSEs for all n. As stickiness increases, the MSE of the tuned estimator marginally deviates from the best for small n. For highly sticky chains (p = 0.9), the deviation persists for significantly longer. The plot to the right shows mean values and confidence bars (for the tuned estimator alone) for all three values of p. The best estimator is close in mean to missing mass for all n for all p. As stickiness increases, the tuning procedure appears to require increasingly larger values of n for good accuracy.

In our final experiment, presented in Figure 4, we consider the text of the novel A Tale of Two Cities by Charles Dickens accessed through Project Gutenberg (Dickens, 1994). All auxiliary content (preface, table of contents, chapter titles, Project Gutenberg related text) were removed and only the novel text was retained. This text was tokenized and all punctuation was removed. Titles (Miss, Mr. etc.) and names of characters that occurred as collocations with high frequency
(10 of them) were merged into single tokens. The result was a sequence of N = 136092 tokens, numbered from 0 to N − 1, with a vocabulary X (unique tokens) of size *|X |* = 10542. For defining missing mass Mπ, the overall frequency distribution of the N tokens was taken to be the stationary distribution π. A consecutive sequence of n tokens (Token s + 1 to Token s + n with starting point s) is considered as a trajectory of length n, i.e. Xn. For a given length n, approximately 15N/n trajectories were considered in the simulations with their starting points separated by n/15. An important feature of this data is that the Markov assumption (also known as the bigram assumption in this literature) is clearly violated, since we expect the text to have longer-range dependencies. In any case, we can run our estimator for the missing mass and compare it to the true missing mass, which can still be computed from the sequence once the stationary probability is fixed.

![15_image_0.png](15_image_0.png)

In Figure 4, we show the MSE in the plot to the left and the means with confidence bars to the right. Interestingly, all of the choices of τ that we consider yield similar MSE performance for the WingIt estimator, and all of these choices appear to have a super-linear rate of decay with the

![16_image_0.png](16_image_0.png)

sample size n. The reason for the difference in rate of decay could be because we hold *|X |* constant as we increase n in the text simulations resulting in a decrease in Mπ with n. This decrease is confirmed in the plot on the right, where we see that the mean of missing mass falls from about 0.45 for n = 600 to about 0.1 for n = 19200. Further, from the right plot, we observe that the tuned estimator and τ = 32 estimator are close to each other in mean, while deviating a bit from the mean of missing mass for small n. The aforementioned long-range dependencies in the text are likely to be causing this minor deviation. In any case, the estimator McWingIt(τb) appears to be accurate for all n. Overall, our experiments on this corpus demonstrate that the missing mass estimator is robust to model misspecification, and can work well even for non-Markovian sources.

## 7 Proofs

In this section, we present proofs of the main theorems. Technical lemmas are frequently referenced in these proofs, and their statements and proofs can be found in Appendix A.

Recall that n0 = ⌊n/τ ⌋; we will drop the floor notation henceforth for readability. Also recall our index sets from Eq. (14). For j ∈ [n0], define the sets Bj := Djτ and Hj := Ijτ as the "dependent" and "independent" indices, respectively, for the j-th window, or block, of size (at most) 2τ − 1.

Mnemonically, one should view Bj as the j-th *block* of indices and Hj = [n]\Bj as the set of indices having a *hole* at block j. As convention, we will use i ∈ [n] to index individual samples and j ∈ [n0]
to index the various windows or blocks. See Figure 5 for an illustration.

## 7.1 Proof Of Theorem 1

In the case n/τ ≤ 9, the theorem is immediate since the RHS of the claim is minimized by 1. We therefore focus on the complementary case n/τ = n0 ≥ 9 for the entire proof. Note that in this case, we also have n ≥ 9Tmix.

Viewing Xn as fixed for the moment and writing out our estimator McWingIt(τ ) = 1 n0 Pn0 j=1 Mc(jτ)
τ ,
we have that 12 |McWingIt(τ ) − Mπ(Xn)| 2is equal to

j=1 I Xjτ ∈/ XHj 	− E Y ∼π Y ⊥⊥Xn I Y /∈ X[n] 	  2 1 2 ·  1 n0 Xn0 j=1 E Y ∼π Y ⊥⊥Xn I Y /∈ XHj 	− E Y ∼π Y ⊥⊥Xn I Y /∈ X[n] 	! 2 ≤  1 n0 Xn0 | {z } T1 j=1 IXjτ ∈/ XHj 	− E Y ∼π Y ⊥⊥Xn I Y /∈ XHj 	! 2 +  1 n0 Xn0 , (29) | {z } T2
where we have added and subtracted the term 1 n0 Pn0 j=1 E

Y ∼π Y ⊥⊥Xn I
Y /∈ XHj inside |McWingIt(τ ) −
Mπ(Xn)| and used the inequality 12
(a + b)
2 ≤ (a 2 + b 2). Recall that X[n] = {X1*, . . . , X*n} is the set (not sequence) of all random variables. We start by bounding E[T1], noting that T1 resembles a *conditional* squared bias term.

Bounding E[T1]: Using the inequality 1 n0 Pn0 j=1 aj 2≤Pn0 j=1 a 2 j , we have j=1 E Xn  E Y ∼π Y ⊥⊥Xn I Y /∈ XHj 	− E Y ∼π Y ⊥⊥Xn I Y /∈ X[n] 	!2 E[T1] ≤1 n0 Xn0 ≤ max j∈[n0] E Xn  E Y ∼π Y ⊥⊥Xn I Y /∈ XHj 	− E Y ∼π Y ⊥⊥Xn I Y /∈ X[n] 	!2.

For any j ∈ [n0], we further have

E Xn  E Y ∼π Y ⊥⊥Xn I Y /∈ XHj 	− E Y ∼π Y ⊥⊥Xn I Y /∈ X[n] 	!2(i) = E Xn  E Y ∼π Y ⊥⊥Xn I Y ∈ XBj 	· IY /∈ XHj 	!2 (ii) ≤ E Xn E Y ∼π Y ⊥⊥Xn I Y ∈ XBj 	· IY /∈ XHj 	(30)

where step (i) follows from Lemma 2 and step (ii) uses the fact that

$$0\leq\operatorname*{\mathbb{E}}_{\begin{array}{c}{Y\sim\pi}\\ {Y\coprod X^{n}}\end{array}}\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}\leq1.$$

18 We now proceed to uniformly bound EXn E Y ∼π Y ⊥⊥Xn I
Y ∈ XBj
	· IY /∈ XHj for any j ∈ [n0],
and drop the subscripts in the expectation from here on for convenience. The key observation is that since Sℓ∈[n0]\j Bℓ ⊆ Hj , we can write

$$\mathbb{I}\left\{Y\not\in X_{\mathcal{H}_{j}}\right\}\leq\prod_{\ell\in[n_{0}]\setminus j}\mathbb{I}\left\{Y\not\in X_{\mathcal{B}_{\ell}}\right\}\leq\prod_{\begin{array}{c}{{\ell\in[n_{0}]\setminus j}}\\ {{|\ell-j|\mod3=0}}\end{array}}\mathbb{I}\left\{Y\not\in X_{\mathcal{B}_{\ell}}\right\}.$$
}. (31)
We define

$$S_{j}:=\{\ell\in[n_{0}]:|\ell-j|\mod3\equiv0\}$$
Sj := {ℓ ∈ [n0] : |ℓ − j| mod 3 ≡ 0} (32)
as shorthand (see Figure 5 for an illustration), and define the set

$$(31)$$
$$(32)$$
$$(33)$$
$$W_{j}:=\bigcup_{\ell\in S_{j}\setminus\{j\}}X_{\mathcal{B}_{\ell}}$$

XBℓ(33)
Recalling our notation ⊕ for concatenation of sequences, we also define the corresponding sequence

$$W_{j}:=\bigoplus_{\ell\in S_{j}\setminus\{j\}}X_{\mathcal{B}_{\ell}}.$$
. (34)
Using Eq. (31) and this new notation, we can write

$$\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}\leq\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{W}_{j}\right\}.$$

Now define the auxiliary sequence of random variables

$$W_{j}^{\prime}:=\bigoplus_{\ell\in S_{j}\setminus\{j\}}X_{B_{\ell}}^{\prime},$$
$$(35)$$

where each X′Bℓ is a Markov chain initialized at stationary distribution π and drawn independently of everything else. The sequence W′
j can thus be viewed as a concatenation of several independent Markov chains. Following parallel notation to above, let W′
j denote the set containing elements in

W′
j
. By assumption, we have τ ≥ tmix(ϵ) for ϵ =
· $\epsilon=\left(\frac{\mathbb{T}_{\mathrm{mix}}}{n}\right)^{-1}$
2≤ 1/81. Applying Lemma 8 yields
$\mathbb{E}[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{W}_{j}\right\}]\leq\mathbb{E}[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{W}_{j}^{\prime}\right\}]+n_{0}\epsilon$.  
But since W′
j is a concatenation of independent Markov chains and is also independent of the Markov chain XBj
, applying Lemma 4 with k = |Sj \ {j}| yields

$$\mathbb{E}[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{W}_{j}^{\prime}\right\}]\leq\frac{1}{k}\leq\frac{3}{n_{0}-3},\tag{36}$$

where we have used the fact that, by definition, |Sj \ {j*}| ≥* n0
3 − 1. Putting all of the pieces
together and substituting ϵ =
$\epsilon=\left(\frac{\text{T}_{\text{m}}}{m}\right)\\$. 
2, we have
, $|S_j\setminus\{j\}|\geq\frac{n_0}{2}-1$. Putting all of 
$$\mathbb{E}[T_{1}]\leq{\frac{3}{n_{0}-3}}+n_{0}\cdot\left({\frac{\mathsf{T}_{\mathrm{mix}}}{n}}\right)^{2}{\stackrel{\mathrm{(i)}}{\leq}}{\frac{\tau}{n}},$$  use $\tau\geq\mathsf{T}_{\mathrm{mix}}$ and $n_{0}\geq9$.  

where step (i) follows because τ ≥ Tmix and n0 ≥ 9.

19

Bounding E[T2]: We note that T2 resembles a *conditional* variance term. Define the random
variables Zj := IXjτ ∈/ XHj
	− E Y ∼π
$$\begin{array}{c c c c}{{}}&{{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}&{{Y\bot X^{n}}}&{{(\bot,\bot,\bot)}}\\ {{}}&{{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}&{{\mathbb{E}[T_{2}]=\frac{1}{n_{0}^{2}}\sum_{j,k=1}^{n_{0}}\mathbb{E}[Z_{j}Z_{k}]\leq\frac{1}{n_{0}}+\frac{1}{n_{0}^{2}}\sum_{j\neq k}\mathbb{E}[Z_{j}Z_{k}],}}\\ {{}}&{{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}&{{Z_{j}\in[-1,1],\mathrm{~for~all~i~}\pi_{i}[-1,1],\mathrm{~}T_{i}=f_{i}=j_{i}.}}\end{array}$$
I
Y /∈ XHj
	for all j ∈ [n0] as shorthand. Then we have
where the inequality follows since Zj ∈ [−1, 1] for all j ∈ [n0]. Therefore, it suffices to bound the
cross terms E[ZjZk] for j ̸= k. We have
$$\mathbb{E}[Z_{j}Z_{k}]=\underbrace{\mathbb{E}[\mathbb{I}\left\{X_{j\tau}\notin\mathbf{X}_{H_{j}}\right\}\cdot\mathbb{I}\left\{X_{k\tau}\notin\mathbf{X}_{H_{k}}\right\}]}_{U_{1}}-\underbrace{\mathbb{E}[\mathbb{I}\left\{X_{j\tau}\notin\mathbf{X}_{H_{j}}\right\}]\cdot\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{H_{k}}\right\}]}_{U_{2}}$$
$$-\underbrace{\mathbb{E}[\mathbb{I}\left\{X_{k\tau}\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]\cdot\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]}_{U_{3}}+\underbrace{\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]\cdot\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]}_{U_{4}}$$

$$(37)$$
Let (X′1
, X′2
, . . . , X′n
) denote a sequence of n random variables drawn i.i.d. from π, and independently of everything else. Note that Y can also be viewed as an additional such draw. Once again noting that τ ≥ tmix(ϵ) for ϵ =
Tmix n 2, we may apply Lemma 6 to obtain

$\mathbb{E}[\mathbb{I}\left\{X_{j\tau}\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]\geq\mathbb{E}[\mathbb{I}\left\{X_{j\tau}^{\prime}\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]-4\epsilon=\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]-4\epsilon,$
and similarly,

$$\mathbb{E}[\mathbb{I}\left\{X_{k\tau}\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]\geq\mathbb{E}[\mathbb{I}\left\{X_{k\tau}^{\prime}\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]-4\epsilon=\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]-4\epsilon.$$

Noting that E[IY /∈ XHj
	] ≤ 1 (and similarly for E[I {Y /∈ XHk
}], the above two displays imply that U2 ≥ U4 − 4ϵ and U3 ≥ U4 − 4ϵ. Applying this to Eq.(37) yields

$$\mathbb{E}[Z_{j}Z_{k}]\leq\underbrace{\mathbb{E}[\mathbb{I}\left\{X_{j\tau}\notin\mathbf{X}_{H_{j}}\right\}\cdot\mathbb{I}\left\{X_{k\tau}\notin\mathbf{X}_{H_{k}}\right\}]}_{U_{1}}-\underbrace{\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{H_{j}}\right\}]\cdot\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{H_{k}}\right\}]}_{U_{4}}+8e.$$
$$(38)$$
$$\begin{array}{l}{(39)}\\ {(40)}\end{array}$$
$$(41)$$
+8ϵ. (38)
Looking at the first term of Eq. (38) and using Lemma 7, we have

U1 ≤ E[IXjτ ∈/ XHj∩Hk 	· IXkτ ∈/ XHj∩Hk 	] (39) ≤ E[IX′jτ ∈/ XHj∩Hk 	· IX′kτ ∈/ XHj∩Hk 	] + 8ϵ (40) (i) = E XHj ,XHk (E X′jτ [IX′jτ ∈/ XHj∩Hk 	] · E X′kτ I X′kτ ∈/ XHj∩Hk 	] ) + 8ϵ (41) = E XHj ,XHk E Y [IY /∈ XHj∩Hk 	] · E Y [IY /∈ XHj∩Hk 	] + 8ϵ, (42)

where step (i) follows because X′jτ and X′kτ are independent of everything else.
Taking stock, it remains to bound the expectation of the term  $$T(\mathbf{X}_{\mathcal{H}_{j}},\mathbf{X}_{\mathcal{H}_{k}}):=\mathbb{E}[\{Y\notin\mathbf{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\}]\cdot\mathbb{E}\frac{\mathbb{E}}{Y}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\right\}-\mathbb{E}[\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\}]\cdot\mathbb{E}\frac{\mathbb{E}}{Y}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]\tag{4}$$
,}]   $\left(43\right)$  . 
$$(44)$$
$$=\left(\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]\right)\cdot\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\right\}]$$ $$\qquad+\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}]\cdot\left(\mathbb{E}[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{k}}\right\}]\right).$$

. (44)
20 We now characterize EY [IY /∈ XHj∩Hk
	− IY /∈ XHj
	]. By Lemma 2, we have

$$\mathbb{E}[\mathbb{I}\left\{Y\notin\boldsymbol{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\right\}-\mathbb{I}\left\{Y\notin\boldsymbol{X}_{\mathcal{H}_{j}}\right\}]=\mathbb{E}\left[\mathbb{I}\left\{Y\in\boldsymbol{X}_{\mathcal{H}_{j}\setminus\mathcal{H}_{k}}\right\}\cdot\mathbb{I}\left\{Y\notin\boldsymbol{X}_{\mathcal{H}_{j}\cap\mathcal{H}_{k}}\right\}\right].$$  Note that $\mathcal{H}_{j}\setminus\mathcal{H}_{k}=\mathcal{B}_{k}$ and $\mathcal{H}_{j}\cap\mathcal{H}_{k}=[n]\setminus\{\mathcal{B}_{j}\cup\mathcal{B}_{k}\}$. Therefore, we have 

Next, note that Hj \ Hk = Bk and Hj ∩ Hk = [n] \ {Bj ∪ Bk}. Therefore, we have I nY ∈ XHj\Hk o· IY /∈ XHj∩Hk 	= I {Y ∈ XBk } · Y ℓ̸=j,k I {Y /∈ XBℓ } ≤ I {Y ∈ XBk } · Y ℓ∈Sj\{j,k} I {Y /∈ XBℓ }

In the above, recall that we defined Sj := {ℓ ∈ [n0] : |ℓ − j| mod 3 ≡ 0}. Note that |Sj \ {j, k*}| ≥*
n0/3−2. Using the same argument as in the proof of bounding E[T1] (see Eqs. (31)–(36)), we have

$$\mathbb{E}\left[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{k}}\right\}\cdot\prod_{\ell\in S_{j}\setminus\{j,k\}}\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{B}_{\ell}}\right\}\right]\leq\frac{1}{|S_{j}\setminus\{j,k\}|}+n_{0}\epsilon$$ $$\leq\frac{3}{n_{0}-6}+n_{0}\epsilon.$$

For the second term in Eq. (43), an identical argument yields

$$\mathbb{E}[\mathbb{I}\left\{Y\notin{\mathbf{X}}_{{\mathcal{H}}_{j}\cap{\mathcal{H}}_{k}}\right\}-\mathbb{I}\left\{Y\notin{\mathbf{X}}_{{\mathcal{H}}_{k}}\right\}]\leq{\frac{3}{n_{0}-6}}+n_{0}\epsilon,$$

so that for each (*j, k*) pair, we have

$$\mathbb{E}\,T({\mathbf{X}}_{{\mathcal{H}}_{j}},{\mathbf{X}}_{{\mathcal{H}}_{k}})\lesssim{\frac{3}{n_{0}-6}}+n_{0}\epsilon.$$
$$\mathbb{E}[T_{1}]{\mathrm{~and~}}\mathbb{E}[T_{2}].$$

Putting together the pieces, we then have E[ZjZk] ≲3 n0−6 + n0ϵ + 16ϵ.

Substituting ϵ =
Tmix n 2and noting that τ ≥ Tmix and n0 ≥ 9, we obtain E[ZjZk] ≲τn
.

Averaging over all j ̸= k completes the proof of the fact E[T2] ≤ C ·
τ n
∧ 1.

We conclude by putting together our bounds on E[T1] and E[T2].

## 7.2 Proof Of Theorem 2

Via a decomposition similar to Eq. (19), we obtain

$$\mathrm{var}(M_{\pi}(X^{n}))\leq3\cdot\mathsf{MSE}(\widehat{M}_{\mathrm{WnCrBr}}(\tau),M_{\pi}(X^{n}))+3\left|\frac{\pi}{X^{n}}[\widehat{M}_{\mathrm{WnCrBr}}(\tau)-M_{\pi}(X^{n})]\right|^{2}+3\,\mathrm{var}(\widehat{M}_{\mathrm{WnCrBr}}(\tau)).\tag{45}$$

Above, the first term corresponds to the MSE of the estimator McWingIt, the second term corresponds to a squared bias term, and the third term corresponds to the variance of the estimator McWingIt. Throughout this proof, we will choose τ = tmix (Tmix/n)
2 ∧ 1/4≲ Tmix ·log(1+n/Tmix),
where the last inequality holds due to Eq. (6).

Bounding MSE: Applying Theorem 1 yields the direct bound

$$\mathrm{MSE}(\widehat{M}_{\mathrm{WingIT}}(\tau),M_{\pi}(X^{n}))\lesssim\tau/n\lesssim\frac{\mathsf{T}_{\mathrm{mix}}}{n}\cdot\log(1+n/\mathsf{T}_{\mathrm{mix}}).$$

It remains to bound the squared bias and variance terms on the RHS of Ineq. (45).

Bounding squared bias: Note that it suffices to bound the positive term E[Mc(jτ)
τ ]−E[Mπ(Xn)]
for each j ∈ [n0]. Write

$$\mathbb{E}[\widehat{M}_{\tau}^{(j\tau)}]-\mathbb{E}[M_{\pi}(X^{n})]=\mathbb{E}\underset{X^{n}}{\mathbb{E}}\mathbb{E}\left[\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}-\mathbb{I}\left\{Y\notin\mathbf{X}_{[n]}\right\}\right]$$ $$\overset{\text{(i)}}{=}\mathbb{E}\underset{X^{n}}{\mathbb{E}}\mathbb{E}\left[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{X}_{\mathcal{H}_{j}}\right\}\right],$$

where step (i) follows from Lemma 2.

By executing the same steps that we used to bound the term in Eq. (30), we have

$$\mathbb{E}[\widehat{M}_{\tau}^{(j\tau)}]-\mathbb{E}[M_{\pi}(X^{n})]\leq C\cdot\frac{\tau}{n}\lesssim\frac{\mathsf{T}_{\mathrm{mix}}}{n}\cdot\log(1+n/\mathsf{T}_{\mathrm{mix}}),$$

where the final bound holds owing to the choice τ ≍ Tmix · log(1 + n/Tmix). We are eventually interested in the squared bias, so we have

$$\left|\operatorname*{\mathbb{E}}_{X^{n}}[\widehat{M}_{\mathrm{WingIT}}(\tau)-M_{\pi}(X^{n})]\right|^{2}\lesssim\left(\frac{\mathsf{T}_{\mathrm{mix}}}{n}\cdot\log(1+n/\mathsf{T}_{\mathrm{mix}})\right)^{2}.$$

Bounding variance: We have

$$\mathrm{var}(\widehat{M}_{\mathrm{WNGIT}}(\tau))=\mathbb{E}\left|\frac{1}{n_{0}}\sum_{j=1}^{n_{0}}\left(\mathbb{I}\left\{X_{j\tau}\notin\mathbf{X}_{H_{j}}\right\}-\mathbb{E}\underset{Y\subset X^{n}}{\mathbb{E}}\mathbb{I}\left\{Y\notin\mathbf{X}_{H_{j}}\right\}\right)\right|^{2}$$ $$\overset{(i)}{\leq}\mathbb{E}\left|\frac{1}{n_{0}}\sum_{j=1}^{n_{0}}\left(\mathbb{I}\left\{X_{j\tau}\notin\mathbf{X}_{H_{j}}\right\}-\underset{Y\subset X^{n}}{\mathbb{E}}\mathbb{I}\left\{Y\notin\mathbf{X}_{H_{j}}\right\}\right)\right|^{2}\overset{(ii)}{=}\mathbb{E}[T_{2}].$$

Here step (i) follows from Jensen's inequality and step (ii) uses the definition of the term T2 from Section 7.1. But we know from that proof that E[T2] ≲ *τ /n*, which is in turn bounded by C
Tmix n· log(1 + n/Tmix) for the choice τ ≍ Tmix · log(1 + n/Tmix).

Putting together the bounds on MSE, squared bias, and variance thus yields

$$\operatorname{var}(M_{\pi}(X^{n}))\leq C\cdot{\frac{\mathsf{T_{m i x}}}{n}}\cdot\log(1+n/\mathsf{T_{m i x}})\wedge1,$$

as desired.

## 7.3 Proof Of Theorem 3

The structure of this proof parallels the proof of Theorem 1; the reader is advised to read that proof first. As in that proof, if n/τ ≤ 9 then the theorem is immediate since the RHS of the claim is minimized by 1. We therefore focus on the complementary case n/τ = n0 ≥ 9 for the entire proof. Note that in this case, we also have n ≥ 9Tmix.

We next proceed via a series of steps that resembles the proof of Theorem 1. Recall the notation Nx(XP ), Nx(XP ) that we defined in Section 5. Viewing Xn as fixed for the moment and writing out our estimator McWingIt,≤ζ (τ ) := 1 n0 Pn0 j=1 Mc(jτ)
τ,≤ζ
, a series of steps identical to Eq. (29) yield that 1 2 |McWingIt,≤ζ (τ ) − Mπ,≤ζ (Xn)| 2is equal to

j=1 I NXjτ (XHj ) ≤ ζ	− E Y ∼π Y ⊥⊥Xn I {NY (Xn) ≤ ζ}  2 1 2 ·  1 n0 Xn0 j=1 E Y ∼π Y ⊥⊥Xn I NY (XHj ) ≤ ζ	− E Y ∼π Y ⊥⊥Xn I {NY (Xn) ≤ ζ} ! 2 ≤  1 n0 Xn0 | {z } T ′ 1 j=1 INXjτ (XHj ) ≤ ζ	− E Y ∼π Y ⊥⊥Xn I NY (XHj ) ≤ ζ	! 2 +  1 n0 Xn0 . | {z } T ′ 2
As in the proof of Theorem 1, we upper bound E[T
′1
] and E[T
′2
].

Bounding E[T
′1
]: An identical argument to the proof of Theorem 1 gives

$$\mathbb{E}[T_{1}^{\prime}]\leq\operatorname*{max}_{j\in[n_{0}]}\mathbb{E}\left(\operatorname*{\mathbb{E}}_{Y_{1}^{\prime}\to\mathbb{T}}\mathbb{I}\left\{N_{Y}(\mathbf{X}_{\mathcal{H}_{j}})\leq\zeta\right\}-\operatorname*{\mathbb{E}}_{Y_{1}^{\prime}\to\mathbb{T}}\mathbb{I}\left\{N_{Y}(X^{n})\leq\zeta\right\}\right)^{2}.$$  $[n_{0}]$ we further have 

For any $j\in[n_0]$, we further have . 
For any j ∈ [n0], we further have E Xn  E Y ∼π Y ⊥⊥Xn I NY (XHj ) ≤ ζ	− E Y ∼π Y ⊥⊥Xn I {NY (Xn) ≤ ζ} !2(i) ≤ E Xn  E Y ∼π Y ⊥⊥Xn I Y ∈ XBj 	· INY (XHj ) ≤ ζ	!2 (ii) ≤ E Xn E Y ∼π Y ⊥⊥Xn I Y ∈ XBj 	· INY (XHj ) ≤ ζ	,

where step (i) follows from Lemma 3 and step (ii) follows because, as in the proof of Theorem 1, the expectation of a product of indicator random variables is between 0 and 1.

We now proceed to uniformly bound EXn E Y ∼π Y ⊥⊥Xn I
Y ∈ XBj
	· INY (XHj
) ≤ ζ	for any j ∈
[n0], and drop the subscripts in the expectation from here on for convenience. Recall the definitions of the set Wj and the corresponding sequence Wj from Eqs. (33) and (34). Note that, since Wj ⊂ XHj
, we can write I
Y ∈ XBj
	· INY (XHj
) ≤ ζ	≤ IY ∈ XBj
	· I {NY (Wj ) ≤ ζ}.

We also recall the definition of the auxiliary sequence W′
j
(and the corresponding set notation W′
j
)
in Eq. (35). Since τ ≥ tmix(ϵ) for ϵ =
Tmix n 2, we can again apply Lemma 8 to yield E
-IY ∈ XBj
	· I {NY (Wj ) ≤ ζ}≤ E-IY ∈ XBj
	· INY (W′
j
) ≤ ζ	 + n0ϵ.

Now, since W′
j is a concatenation of independent Markov chains and is also independent of the Markov chain XBj
, applying Lemma 5 (which is a generalization of Lemma 4) with k = |Sj \ {j}| yields

$$\mathbb{E}\left[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{j}}\right\}\cdot\mathbb{I}\left\{N_{Y}(\mathbf{W}_{j}^{\prime})\leq\zeta\right\}\right]\leq{\frac{\zeta+1}{k}}\leq{\frac{3(\zeta+1)}{n_{0}-3}}.$$
.
Putting all of the pieces together in a similar manner to the proof of Theorem 1, we obtain

$$\mathbb{E}[T_{1}^{\prime}]\leq{\frac{3(\zeta+1)}{n_{0}-3}}+n_{0}\cdot\left({\frac{\mathsf{T_{m i x}}}{n}}\right)^{2}\lesssim{\frac{\tau(\zeta+1)}{n}}.$$

Bounding E[T
′2
]: We now define, for all j ∈ [n0], the random variables

$$Z_{j}^{\prime}:=\mathbb{I}\left\{N_{X_{j\tau}}(X_{\mathcal{H}_{j}})\leq\zeta\right\}-\underset{Y\perp\bar{X}^{n}}{\mathbb{E}}\mathbb{I}\left\{N_{Y}(X_{\mathcal{H}_{j}})\leq\zeta\right\}.$$

Then we have, as before,

$$\mathbb{E}[T_{2}^{\prime}]\leq\frac{1}{n_{0}}+\frac{1}{n_{0}^{2}}\sum_{j\neq k}\mathbb{E}[Z_{j}^{\prime}Z_{k}^{\prime}].$$

We then follow a series of steps identical to Eqs. (37)-(38) to obtain

$$\mathbb{E}[Z_{j}^{\prime}Z_{k}^{\prime}]\leq\underbrace{\mathbb{E}\left[\mathbb{I}\left\{N_{X_{jr}}(\mathbf{X}_{H_{j}})\leq\zeta\right\}\cdot\mathbb{I}\left\{N_{X_{k}r}(\mathbf{X}_{H_{k}})\leq\zeta\right\}\right]}-\underbrace{\mathbb{E}\left[\mathbb{I}\left\{N_{Y}(\mathbf{X}_{H_{j}})\leq\zeta\right\}\cdot\mathbb{I}\left\{N_{Y}(\mathbf{X}_{H_{k}})\leq\zeta\right\}\right]}.$$
| {z }
U′1
| {z }
U′2
We start with analyzing U
′1
. We have

U ′ 1 ≤ E[INXjτ (XHj∩Hk ) ≤ ζ	· INXkτ (XHj∩Hk ) ≤ ζ	] (i) ≤ E[I nNX′jτ (XHj∩Hk ) ≤ ζ o· I nNX′kτ (XHj∩Hk ) ≤ ζ o] + 8ϵ (ii) = E XHj ,XHk E Y -INY (XHj∩Hk ) ≤ ζ	 · E Y -INY (XHj∩Hk ) ≤ ζ	+ 8ϵ,

where step (i) follows from Lemma 7 and step (ii) uses the independence of X′jτ , X′kτ from everything else. Thus, it suffices to upper bound the expectation of the term

T ′(XHj , XHk ) := E Y -INY (XHj∩Hk ) ≤ ζ	 · E Y -INY (XHj∩Hk ) ≤ ζ	 − E Y -INY (XHj ) ≤ ζ	 · E Y [I {NY (XHk ) ≤ ζ}] = E Y -INY (XHj∩Hk ) ≤ ζ	− INY (XHj ) ≤ ζ	· E Y -INY (XHj∩Hk ) ≤ ζ	 + E Y -INY (XHj∩Hk ) ≤ ζ	 · E Y -INY (XHj∩Hk ) ≤ ζ	− I {NY (XHk ) ≤ ζ}.

24 We next upper bound the term EY
-INY (XHj∩Hk
) ≤ ζ	− INY (XHj
) ≤ ζ	, noting that the term EY
-INY (XHj∩Hk
) ≤ ζ	− I {NY (XHk
) ≤ ζ}can be identically controlled. Applying Lemma 3 with P := Hj ∩ Hk and Q := Hj yields

E Y -INY (XHj∩Hk ) ≤ ζ	− INY (XHj ) ≤ ζ	 ≤ E hI nY ∈ XHj\Hk o· INY (XHj∩Hk ) ≤ ζ	i = E-I {Y ∈ XBk } · INY (XHj∩Hk ) ≤ ζ	 (i) ≤ E [I {Y ∈ XBk } · I {NY (Wj,k) ≤ ζ}] , (46)

Above, we defined Wj,k := Sℓ∈Sj\{j,k} XBℓ and the corresponding sequence notation as Wj,k :=
Lℓ∈Sj\{j,k} XBℓ
, and step (i) followed because Wj,k ⊆ XHj∩Hk
. We define the corresponding sequences of iid Markov chains

$$W_{j,k}^{\prime}:=\bigcup_{\ell\in S_{j}\backslash\{j,k\}}X_{B_{\ell}}^{\prime}$$ $$W_{j,k}^{\prime}:=\bigoplus_{\ell\in S_{j}\backslash\{j,k\}}X_{B_{\ell}}^{\prime}.$$

Then, proceeding from Eq. (46), Lemma 8 gives us

$$\mathbb{E}\left[\mathbb{I}\left\{N_{Y}(\mathbf{X}_{H_{j}\cap\mathcal{H}_{k}})\leq\zeta\right\}-\mathbb{I}\left\{N_{Y}(\mathbf{X}_{H_{j}})\leq\zeta\right\}\right]\leq\mathbb{E}\left[\mathbb{I}\left\{Y\in\mathbf{X}_{\mathcal{B}_{k}}\right\}\cdot\mathbb{I}\left\{N_{Y}(\mathbf{W}_{j,k}^{\prime})\leq\zeta\right\}\right]+n_{0}\epsilon,$$ $$\overset{(\mathbb{I})}{\leq}\frac{\zeta+1}{|S_{j}\setminus\{j,k\}|}+n_{0}\epsilon$$ $$\leq\frac{3(\zeta+1)}{n_{0}-6}+n_{0}\epsilon,$$

where step (i) uses Lemma 5. Ultimately, we have

$$\mathbb{E}\,T^{\prime}(X_{{\mathcal{H}}_{j}},X_{{\mathcal{H}}_{k}})\stackrel{<}{\sim}\frac{\zeta+1}{n_{0}}+n_{0}\epsilon,$$

and obtain E[Z
′
jZ
′
k
] ≲
(ζ+1)
n0+ n0ϵ + 16ϵ. Substituting ϵ =
Tmix n 2and noting that τ ≥ Tmix, we obtain E[ZjZk] ≲
(ζ+1)τ n. Averaging over all j ̸= k completes the proof of the fact E[T2] ≤
C ·
(ζ+1)τ n∧ 1.

Finally, combining our bounds on E[T
′1
] and E[T
′2
] completes the proof.

## 8 Discussion

We presented the WingIt estimator for estimating the stationary mass missing from a Markovian sequence. While the vanilla Good–Turing estimator can suffer constant bias in the Markovian setting, our estimator achieves (near) minimax optimal mean-squared error over mixing Markov chains. It can also be computed with a linear-time algorithm, and performs favorably in our experiments, even in language text applications in which the Markovian assumption is clearly violated. We also presented a variant of WingIt for estimating the small-count probability in a Markov sequence and established mean squared error bounds for this task.

Our work leaves open several important and intriguing questions. First, while Theorem 1 and 2 provide a complete picture—up to a logarithmic factor—for stationary missing mass estimation from the point of view of MSE, exponential concentration inequalities, both for our estimator and for the missing mass estimand itself, remain out of reach of our current techniques. Such concentration inequalities could, for instance, be used to provide a provable guarantee on the validation procedure that we outlined in Section 6. Second, we reiterate that our estimator is only optimal up to a logarithmic factor in n/Tmix, and removing this factor to match the minimax lower bound—possibly by designing an alternative estimator—is an interesting open problem.

Third, we believe that the Markov property may not be central to our main results, and that Theorem 1 could be extended to more general α-mixing sequences (Rosenblatt, 1956). While nontrivial, this extension would capture, for instance, other classes of interesting temporal processes such as some hidden Markov models. Fourth, a related point is that the assumption (5) of geometric ergodicity itself is central to the design and analysis of our estimator; designing estimators that do not require ergodicity—perhaps just irreducibility (Fried, 2023)—would be of great interest and likely require new ideas.

Finally, it would be interesting to estimate other functionals of the Markov chain other than the stationary missing mass and solve related estimation problems such as competitive distribution estimation of the stationary measure. Our extensions to estimating the mass of elements occurring at most ζ times in Section 5 might be a useful starting point as in the i.i.d. case (Drukh and Mansour, 2005; Acharya et al., 2013), but several questions remain, such as obtaining a uniform bound on the error of estimating all such quantities uniformly over ζ ∈ {0, 1*, . . . , n*}.

## Acknowledgments

This work was supported in part by National Science Foundation grants CCF-2107455, DMS2210734, CCF-2239151 and IIS-2212182, and by research awards/gifts from Adobe, Amazon, Google and Mathworks. AP thanks Wenlong Mou for helpful discussions.

## References

J. Acharya, A. Jafarpour, A. Orlitsky, and A. T. Suresh. Optimal probability estimation with applications to prediction and classification. In *Conference on Learning Theory*, pages 764–796, 2013.

J. Acharya, Y. Bao, Y. Kang, and Z. Sun. Improved bounds for minimax risk of estimating missing mass. In *2018 IEEE International Symposium on Information Theory (ISIT)*, pages 326–330. IEEE, 2018.

F. Ayed, M. Battiston, F. Camerlenghi, and S. Favaro. On consistent and rate optimal estimation of the missing mass. In *Annales de l'Institut Henri Poincare (B) Probabilites et statistiques*, volume 57, pages 1476–1494. Institut Henri Poincar´e, 2021.

A. Ben-Hamou, S. Boucheron, and M. I. Ohannessian. Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications. *Bernoulli*, 23(1):249
- 287, 2017. doi: 10.3150/15-BEJ743. URL https://doi.org/10.3150/15-BEJ743.

D. Berend and A. Kontorovich. The missing mass problem. *Statistics & Probability Letters*, 82(6):
1102–1110, 2012.

D. Berend and A. Kontorovich. On the concentration of the missing mass. *Electronic Communications in Probability*, 18(none):1 - 7, 2013. doi: 10.1214/ECP.v18-2359. URL https:
//doi.org/10.1214/ECP.v18-2359.

P. Chandra, A. Pradeep, and A. Thangaraj. Improved tail bounds for missing mass and confidence intervals for Good–Turing estimator. In *2019 National Conference on Communications (NCC)*, pages 1–6. IEEE, 2019.

P. Chandra, A. Thangaraj, and N. Rajaraman. How good is Good–Turing for Markov samples?

arXiv preprint arXiv:2102.01938, 2021.

P. Chandra, A. Thangaraj, and N. Rajaraman. Missing mass estimation from sticky channels. In 2022 IEEE International Symposium on Information Theory (ISIT), pages 910–915. IEEE, 2022.

S. F. Chen and J. Goodman. An empirical study of smoothing techniques for language modeling.

Computer Speech & Language, 13(4):359–394, 1999.

K. W. Church and W. A. Gale. Probability scoring for spelling correction. *Statistics and Computing*,
1:93–103, 1991.

R. K. Colwell, A. Chao, N. J. Gotelli, S.-Y. Lin, C. X. Mao, R. L. Chazdon, and J. T. Longino.

Models and estimators linking individual-based and sample-based rarefaction, extrapolation and comparison of assemblages. *Journal of Plant Ecology*, 5(1):3–21, 2012.

C. Dickens. *A Tale of Two Cities*. Project Gutenberg, Urbana, IL, USA, 1994. URL gutenberg.

org/ebooks/98.

E. Drukh and Y. Mansour. Concentration bounds for unigram language models. Journal of Machine Learning Research, 6(8), 2005.

S. Favaro, A. Lijoi, and I. Pr¨unster. A new estimator of the discovery probability. *Biometrics*, 68
(4):1188–1196, 2012.

S. Favaro, B. Nipoti, and Y. W. Teh. Rediscovery of Good–Turing estimators via Bayesian nonparametrics. *Biometrics*, 72(1):136–145, 2016.

R. A. Fisher, A. S. Corbet, and C. B. Williams. The relation between the number of species and the number of individuals in a random sample of an animal population. *The Journal of Animal* Ecology, pages 42–58, 1943.

S. Fried. On the α-lazy version of Markov chains in estimation and testing problems. *Statistical* Inference for Stochastic Processes, 26(2):413–435, 2023.

W. Gale and K. Church. What is wrong with adding one? In *Corpus-based research into language*,
pages 189–198. Brill, 1994.

W. A. Gale and G. Sampson. Good–Turing frequency estimation without tears. *Journal of Quantitative Linguistics*, 2(3):217–237, 1995.

W. A. Gale, K. W. Church, and D. Yarowsky. A method for disambiguating word senses in a large corpus. *Computers and the Humanities*, 26:415–439, 1992.

A. Gandolfi and C. C. Sastri. Nonparametric estimations about species not observed in a random sample. *Milan Journal of Mathematics*, 72:81–105, 2004.

I. J. Good. The population frequencies of species and the estimation of population parameters.

Biometrika, 40(3-4):237–264, 1953.

M. Grabchak and Z. Zhang. Asymptotic properties of Turing's formula in relative error. Machine Learning, 106:1771–1785, 2017.

Y. Han, S. Jana, and Y. Wu. Optimal prediction of Markov chains with and without spectral gap.

IEEE Transactions on Information Theory, 69(6):3920–3959, 2023.

Y. Hao, A. Orlitsky, and V. Pichapati. On learning Markov chains. Advances in Neural Information Processing Systems, 31, 2018.

D. Hsu, A. Kontorovich, D. A. Levin, Y. Peres, C. Szepesv´ari, and G. Wolfer. Mixing time estimation in reversible Markov chains from a single sample path. *The Annals of Applied Probability*, 29(4):2439 - 2480, 2019. doi: 10.1214/18-AAP1457. URL https://doi.org/10.1214/
18-AAP1457.

F. Jelinek. Probability distribution estimation from sparse data. *IBM technical disclosure bulletin*,
28:2591–2594, 1985.

R. Krichevsky and V. Trofimov. The performance of universal encoding. IEEE Transactions on Information Theory, 27(2):199–207, 1981.

P.-S. Laplace. *Essai philosophique sur les probabilit´es.* 1814. D. A. Levin and Y. Peres. *Markov chains and mixing times*, volume 107. American Mathematical Soc., 2017.

A. Lijoi, R. H. Mena, and I. Pr¨unster. A Bayesian nonparametric method for prediction in EST
analysis. *BMC bioinformatics*, 8:1–10, 2007.

D. McAllester and L. Ortiz. Concentration inequalities for the missing mass and for histogram rule error. *Journal of Machine Learning Research*, 4(Oct):895–911, 2003.

D. McAllester and R. E. Schapire. Learning theory and language modeling. In *Seventeenth International Joint Conference on Artificial Intelligence*, 2001.

D. A. McAllester and R. E. Schapire. On the convergence rate of Good–Turing estimators. In Conference on Learning Theory, pages 1–6, 2000.

E. Mossel and M. I. Ohannessian. On the impossibility of learning the missing mass. *Entropy*, 21
(1):28, 2019.

H. Ney, U. Essen, and R. Kneser. On structuring probabilistic dependences in stochastic language modelling. *Computer Speech & Language*, 8(1):1–38, 1994.

J. Norris, Y. Peres, and A. Zhai. Surprise probabilities in Markov chains. Combinatorics, Probability and Computing, 26(4):603–627, 2017.

M. I. Ohannessian and M. A. Dahleh. Rare probability estimation under regularly varying heavy tails. In *Conference on Learning Theory*, pages 21–1, 2012.

R. Oliveira. Mixing and hitting times for finite Markov chains. *Electronic Journal of Probability*, 17(none):1 - 12, 2012. doi: 10.1214/EJP.v17-2274. URL https://doi.org/10.1214/EJP.

v17-2274.

A. Orlitsky and A. T. Suresh. Competitive distribution estimation: Why is Good–Turing good.

Advances in Neural Information Processing Systems, 28, 2015.

A. Orlitsky, N. P. Santhanam, and J. Zhang. Always Good–Turing: Asymptotically optimal probability estimation. *Science*, 302(5644):427–431, 2003.

A. Painsky. Convergence guarantees for the Good–Turing estimator. Journal of Machine Learning Research, 23(279):1–37, 2022.

A. Painsky. Generalized Good–Turing improves missing mass estimation. *Journal of the American* Statistical Association, 118(543):1890–1899, 2023.

D. Paulin. Concentration inequalities for Markov chains by Marton couplings and spectral methods.

Electronic Journal of Probability, 20(none):1 - 32, 2015. doi: 10.1214/EJP.v20-4039. URL
https://doi.org/10.1214/EJP.v20-4039.

Y. Peres and P. Sousi. Mixing times are hitting times of large sets. *Journal of Theoretical Probability*,
28(2):488–519, 2015.

N. Rajaraman, A. Thangaraj, and A. T. Suresh. Minimax risk for missing mass estimation. In *2017* IEEE International Symposium on Information Theory (ISIT), pages 3025–3029. IEEE, 2017.

M. Rosenblatt. A central limit theorem and a strong mixing condition. *Proceedings of the National* Academy of Sciences, 42(1):43–47, 1956.

T.-J. Shen, A. Chao, and C.-F. Lin. Predicting the number of new species in further taxonomic sampling. *Ecology*, 84(3):798–804, 2003.

M. Skorski. Missing mass concentration for Markov chains. *arXiv preprint arXiv:2001.03603*, 2020. F. Song and W. B. Croft. A general language model for information retrieval. In *Proceedings of the* Eighth International Conference on Information and Knowledge Management, pages 316–321, 1999.

A. Thangaraj, A. Pananjady, and V. Muthukumar. Missing Mass of Markov Chains, 2024. URL
https://github.com/andrewthan/Missing-Mass.

V. Q. Vu, B. Yu, and R. E. Kass. Coverage-adjusted entropy estimation. *Statistics in Medicine*,
26(21):4039–4060, 2007.

G. Wolfer and A. Kontorovich. Minimax learning of ergodic Markov chains. In *Algorithmic Learning* Theory, pages 904–930. PMLR, 2019.

## A Technical Lemmas

In this section, we collect technical lemmas that were stated and used in the main paper. We first collect lemmas that were used to formalize basic calculations for the Good–Turing estimator, and next lemmas that were used in the proofs of the main results (Theorems 1 and 2).

## A.1 Elementary Lemmas

Our first lemma shows a tight characterization of the mixing time Tmix = tmix(1/4) for the class of sticky Markov chains, defined in Eq. (10).

Lemma 1. Suppose |X | ≥ 2 and p ∈ (0, 1/2]*. For any sticky Markov chain as defined in Eq.* (10),
we have

$${\frac{1}{2p}}\leq\mathsf{T_{m i x}}\leq{\frac{2}{p}}.$$
$$(47)$$

. (47)
Proof. We proceed by exactly calculating the total variation distance maxx∈X ∥e
⊤
x P
t − π
⊤∥TV.

First, we note that we can explicitly calculate the t-step transition kernel as

$$\mathbf{P}^{t}=(1-p)^{t}\mathbf{I}+(1-(1-p)^{t})\cdot\mathbf{1}\pi^{\top}.$$

Therefore, we have

$$\operatorname*{max}_{x\in\mathcal{X}}\|e_{x}^{\top}\mathbf{P}^{t}-\pi^{\top}\|_{\mathsf{TV}}=\operatorname*{max}_{x\in\mathcal{X}}{\frac{1}{2}}\|(1-p)^{t}\cdot(e_{x}-\pi)\|_{1}$$ $$={\frac{(1-p)^{t}}{2}}\cdot\operatorname*{max}_{x\in\mathcal{X}}\|e_{x}-\pi\|_{1}.$$

Since (1 − p)
t· maxx∈X ∥ex − π∥TV is monotonically decreasing in t, we have

$$\mathsf{T_{m i x}=t_{m i x}(1/4)=\frac{\log(2\cdot\operatorname*{max}_{x\in{\mathcal{X}}}\|e_{x}-\pi\|_{1})}{\log(1/(1-p))}.}$$
But
$$\|e_{x}-\pi\|_{1}=(1-\pi_{x})+\sum_{y\in{\mathcal{X}}\backslash\{x\}}\pi_{y}=2-2\pi_{x},$$

and if *|X | ≥* 2, then we have 1 ≤ maxx∈X ∥ex − π∥1 ≤ 2. Furthermore, if p ∈ (0, 1/2], then p ≤ log(1/(1 − p)) ≤ p log 4. Putting together the pieces, we obtain the sandwich bound

$${\frac{1}{2p}}\leq\mathsf{T}_{\mathrm{mix}}\leq{\frac{2}{p}},$$

as desired.

For any set P ⊆ [n], recall that XP = {Xk}k∈P denotes the set of random variables in Xn restricted to the index set P. The following lemma is a deterministic statement regarding indicator random variables.

$\boxed{\text{L}}$
Lemma 2. Consider the sequence Xn and any random variable Y defined on the space X *. Let* P ⊆ Q ⊆ [n] denote two index sets, and let R := Q \ P*. We have*

$$\mathbb{I}\left\{Y\notin\mathbf{X}_{P}\right\}-\mathbb{I}\left\{Y\notin\mathbf{X}_{Q}\right\}=\mathbb{I}\left\{Y\in\mathbf{X}_{R}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{X}_{P}\right\}.$$
$\mathbb{I}\left\{Y\:\not\in\:X_R\right\}\:=\:$. 
Proof. Since P ⊆ Q, the exclusion Y /∈ XQ implies that Y /∈ XP . Therefore I {Y /∈ XP } −
I {Y /∈ XQ} = 1 if Y /∈ XP and Y ∈ XQ, and 0 otherwise. Since R = Q \ P, we have

$$\mathbb{I}\left\{Y\notin\mathbf{X}_{P}\right\}-\mathbb{I}\left\{Y\notin\mathbf{X}_{Q}\right\}=\mathbb{I}\left\{Y\in\mathbf{X}_{R}\right\}\cdot\mathbb{I}\left\{Y\notin\mathbf{X}_{P}\right\},$$

as claimed.

We also define an extension of Lemma 2 to slightly more complicated indicator random variables involving the count of an element in index sets.

Lemma 3. Consider the sequence Xn and any random variable Y defined on the space X *. Let* P ⊆ Q ⊆ [n] denote two index sets, and let R := Q \ P. Then, for any ζ ≥ 0*, we have*

$\mathbb{I}\left\{N_{Y}(\mathbf{X}_{P})\leq\zeta\right\}-\mathbb{I}\left\{N_{Y}(\mathbf{X}_{Q})\leq\zeta\right\}\leq\mathbb{I}\left\{Y\in\mathbf{X}_{R}\right\}\cdot\mathbb{I}\left\{N_{Y}(\mathbf{X}_{P})\leq\zeta\right\}$.  
Proof. Since P ⊆ Q, the event NY (XQ) ≤ ζ implies that NY (XP ) ≤ ζ. Consequently, I {NY (XP ) ≤ ζ}− I {NY (XQ) ≤ ζ} = 1 if and only if NY (XP ) ≤ ζ and NY (XQ) > ζ. Further, we have NY (XP ) ≤ ζ and NY (XQ) > ζ *only if* NY (XP ) ≤ ζ and NY (XR) ≥ 1, i.e. NY (XP ) ≤ ζ and Y ∈ XR. This gives us

$\mathbb{I}\left\{N_{Y}(\mathbf{X}_{P})\leq\zeta\right\}-\mathbb{I}\left\{N_{Y}(\mathbf{X}_{Q})\leq\zeta\right\}\leq\mathbb{I}\left\{Y\in\mathbf{X}_{R}\right\}\cdot\mathbb{I}\left\{N_{Y}(\mathbf{X}_{P})\leq\zeta\right\}$.  

## A.2 Functionals Of Hitting Times In Independent Markov Chains

Our next lemma is an analog, for Markov chains, of the bias bound known for i.i.d. data.

Lemma 4. Consider k independent and identically distributed Markov chains {Xj}
k j=1 *supported* on X
t*, where* Xj = (X
j 1
, . . . , Xj t
) *is a Markov chain with initial distribution sampled from stationary* distribution π and having transition kernel P . With a slight abuse of notation, let Xj also denote the set of random variables in Xj .

Now suppose that Y is a random variable taking values in X sampled independently of everything else. Then

$$\mathbb{E}[\mathbb{I}\left\{Y\in\mathsf{X}_{1}\right\}\cdot\prod_{j=2}^{k}\mathbb{I}\left\{Y\notin\mathsf{X}_{j}\right\}]\leq{\frac{1}{k}}.$$

Proof. Let pY denote the probability mass function of the random variable Y . Owing to independence between the sequences {Xj}
k j=1, we use the tower property of expectation to write

$$\mathbb{E}[\mathbb{I}\left\{Y\in\mathsf{X}_{1}\right\}\cdot\prod_{j=2}^{k}\mathbb{I}\left\{Y\notin\mathsf{X}_{j}\right\}]=\sum_{y\in\mathsf{X}}p(y)\left[\mathbb{E}[\mathbb{I}\left\{y\in\mathsf{X}_{1}\right\}]\cdot\left(\prod_{j=2}^{k}\mathbb{E}[\mathbb{I}\left\{y\notin\mathsf{X}_{j}\right\}]\right)\right].\tag{48}$$
$$\square$$
$$31$$

For a Markov chain (Xi)i≥1 initialized at X1 ∼ π and each fixed x ∈ X , let the random variable H(x) := min{τ : {X1, . . . , Xτ } ∋ x} denote the hitting time of x. Also, for each natural number t, let qt(x) = Pr{H(x) ≤ t}. With this notation, and noting that each Markov chain has length t, we can write the above expression as

E[I {Y ∈ X1} · Y k j=2 I {Y /∈ Xj}] = X y∈X pY (y)qt,y(1 − qt,y) k−1 = 1 k X y∈X pY (y) · k · qt,y(1 − qt,y) k−1 ≤   1 k X y∈X pY (y)   · max ykqt,y(1 − qt,y) k−1 ≤ 1 k , where the final step follows because kqt,y(1 − qt,y) k−1 P ∈ [0, 1] since qt,y is a probability, and y∈X pY (y) = 1.
We also extend the above lemma to indicator random variables involving the *counts* of elements in i.i.d. Markov chains. It is convenient to define notation for binomial and multinomial random variables in a self-contained manner, which we do below.

Definition 1. *We denote by* Bin(k, q) a binomial distribution with k *trials and success probability* q*. In other words, if* L ∼ Bin(k, q) *then we have*

$$\operatorname*{Pr}\{L=\ell\}={\binom{k}{\ell}}q^{\ell}(1-q)^{k-\ell}\quad{\mathrm{~for~}}e a c h\quad\ell\in\{0,\ldots,k\}.$$

Similarly, we denote by Multi(k,(qs)s∈S) a multinomial distribution with k trials, a set of outcomes S, and probabilities for each outcome s ∈ S given by qs*. We say that* (Ks)s∈S ∼ Multi(k,(qs)s∈S)
if Ps∈S Ks = k*, and*

$$\Pr\{\bigcap_{s\in S}\{K_{s}=k_{s}\}\}={\frac{k!}{\prod_{s\in S}k_{s}!}}\cdot\prod_{s\in S}(q_{s})^{k_{s}}.$$

Lemma 5. Carrying over the notation defined in Lemma 4, we have, for any ζ ≥ 0, E[I {Y ∈ X1} · I {NY (X2 ⊕ . . . ⊕ Xk) ≤ ζ}] ≤ ζ + 1 k. (Note that in the special case where ζ = 0, we have I {NY (X2 ⊕ . . . ⊕ Xk) ≤ ζ} =Qk
(Note that in the special case where $\zeta=0$, we have $\mathbb{I}\left\{N_Y(\mathsf{X}_2\oplus\ldots\oplus\mathsf{X}_k)\leq\zeta\right\}=\prod_{j=2}^k\mathbb{I}\left\{Y\notin\mathsf{X}_j\right\}$, a Lemma 5 recovers Lemma 4 as a special case.)
Proof. The proof of this lemma uses similar ideas to the proof of Lemma 4, but is significantly more intricate due to the need to directly handle the complicated random variable NY (X2 ⊕ *. . .* ⊕ Xk).

Carrying over notation from the proof of Lemma 4, we can again use independence between X1 and ⊕k j=2Xj to obtain

$$\mathbb{E}[\mathbb{I}\left\{Y\in\mathsf{X}_{1}\right\}\cdot\mathbb{I}\left\{N_{Y}(\mathsf{X}_{2}\oplus\ldots\oplus\mathsf{X}_{k})\leq\zeta\right\}]=\sum_{y\in\mathcal{X}}p(y)\left[\Pr\{y\in\mathsf{X}_{1}\}\cdot\Pr\{N_{y}(\oplus_{j=2}^{k}\mathsf{X}_{j})\leq\zeta\}\right]$$ $$=\sum_{y\in\mathcal{X}}p(y)\cdot q_{\imath,y}\cdot\Pr\{N_{y}(\oplus_{j=2}^{k}\mathsf{X}_{j})\leq\zeta\}.\tag{49}$$

32 The bulk of the proof concerns handling the term Pr{Ny(⊕k j=2Xj ) ≤ ζ}, and to do so, we make a key connection to multinomial random variables. For every s ∈ {0, 1*, . . . , t*}, let Ks := Pk j=2 I {Ny(Xj ) = s}.

Because the random variables Ny(Xj ) are independent, the random variables (K0*, . . . , K*t) are drawn from a multinomial distribution. By definition, we have Pts=0 Ks = k−1. Let rt,y(s) := Pr{Ny(Xj ) = s}
and further note that

$$r_{t,y}(0):=1-q_{t,y}\quad\mathrm{~and~}\quad r_{t,y}(s):$$
rt,y(0) := 1 − qt,y and rt,y(s) := qt,y · αs for all s ≥ 1,
where Pts=1 αs = 1 and αs ≥ 0 for all s ∈ [t]. In other words, in the notation of Definition 1, we have

$$(K_{0},\ldots,K_{t})\sim\operatorname{Multi}(k-1,(r_{t,y}(s))_{s\in\{0,\ldots,t\}}).$$

With this notation, we have

$$\Pr\{K_{0}=k_{0},\ldots,K_{t}=k_{t}\}=\frac{(k-1)!}{k_{0}!\ldots k_{t}!}\cdot\prod_{s=0}^{t}\left(r_{t,y}(s)\right)^{k_{s}}$$ $$=\frac{(k-1)!}{k_{0}!\ldots k_{t}!}\cdot(1-q_{t,y})^{k_{0}}\cdot(q_{t,y})^{k-1-k_{0}}\cdot\prod_{s=1}^{t}(\alpha_{s})^{k_{s}}$$ $$=\underbrace{\left(\begin{matrix}k-1\\ k_{0}\end{matrix}\right)(1-q_{t,y})^{k_{0}}(q_{t,y})^{k-1-k_{0}}}_{\beta(k_{0}^{s}k_{0})}\cdot\frac{(k-1-k_{0})!}{k_{1}!\ldots k_{t}!}\cdot\prod_{s=1}^{t}(\alpha_{s})^{k_{s}}.\tag{50}$$

Our next observation is that Ny(⊕k j=2Xj ) = Pts=1 s · Ks. Moreover, any realization of (k0*, . . . , k*t)
under which Ny(⊕k j=2Xj ) ≤ ζ requires k0 ≥ k − 1 − ζ. Therefore, we can write

Pr{Ny(⊕ k j=2Xj ) ≤ ζ} =X (k0,...,kt) P k0≥k−1−ζ t s=1 sks≤ζ Pr{K0 = k0, . . . , Kt = kt} (k − 1 − k0)! k1! . . . kt! · Y t =X k0≥k−1−ζ β(k, k0) ·X s=1 (αs) ks P (k1,...,kt) t s=1 P ks=k−1−k0 t s=1 sks≤ζ P (k1,...,kt) t s=1 ks=k−1−k0 (k − 1 − k0)! k1! . . . kt! · Y t ≤X k0≥k−1−ζ β(k, k0) ·X s=1 (αs) ks (i) =X k0≥k−1−ζ β(k, k0), (51)
where step (i) follows because the term (k−1−k0)!

k1!*...k*t!·Qts=1(αs)
ks denotes the PMF of a different multinomial random variable with k − 1 − k0 independent trials, outcomes in [t] and outcome probabilities (α1*, . . . , α*t), i.e. Multi(k − 1 − k0, {αs}s∈[t]) in the notation of Definition 1.

Substituting Eq. (51) into Eq. (49), we have E[I {Y ∈ X1} · I {NY (X2 ⊕ . . . ⊕ Xk) ≤ ζ}] = X y∈X X k0≥k−1−ζ p(y) · qt,y · β(k, k0) y∈X X k0≥k−1−ζ p(y) · k − 1 k0 (1 − qt,y) k0· (qt,y) k−k0 = X y∈X X k0≥k−1−ζ p(y) · k − k0 k · k k0 (1 − qt,y) k0· (qt,y) k−k0 = X (i) ≤ ζ + 1 k · X y∈X p(y) ·X k0≥k−1−ζ k k0 (1 − qt,y) k0· (qt,y) k−k0, where step (i) follows because k0 ≥ k −1−ζ implies that k −k0 ≤ ζ + 1. Finally, we apply Holder's
inequality to obtain
$$\frac{\zeta+1}{k}\cdot\sum_{y\in\mathcal{X}}p(y)\cdot\sum_{k_{0}\geq k-1-\zeta}{k\choose k_{0}}(1-q_{t,y})^{k_{0}}\cdot(q_{t,y})^{k-k_{0}}$$ $$\leq\left(\frac{\zeta+1}{k}\cdot\sum_{y\in\mathcal{X}}p(y)\right)\cdot\max_{y\in\mathcal{X}}\sum_{k_{0}\geq k-1-\zeta}{k\choose k_{0}}(1-q_{t,y})^{k_{0}}\cdot(q_{t,y})^{k-k_{0}}$$ $$\stackrel{{\text{(i)}}}{{\leq}}\left(\frac{\zeta+1}{k}\cdot\sum_{y\in\mathcal{X}}p(y)\right)=\frac{\zeta+1}{k}.$$  If $\zeta$ is a $\zeta$-function, $\zeta$ is a $\zeta$-function.  
Above, step (i) follows because for any y ∈ X , the sum

$$\sum_{k_{0}\geq k-1-\zeta}{\binom{k}{k_{0}}}(1-q_{t,y})^{k_{0}}\cdot(q_{t,y})^{k-k_{0}}$$

is equal to the probability of a subset of outcomes of a Bin(k, qt,y) random variable, which is less than or equal to 1. This completes the proof of the lemma.

## A.3 Lemmas On Surrogate Processes

We next present several consequences of mixing, and each lemma is proved in a purely algebraic fashion. In all the lemmas below, let (X1*, . . . , X*n) denote a Markov chain with unique stationary distribution π and X1 ∼ π. Let tmix(ϵ) denote its mixing time in the sense of Eq. (5), with ϵ ∈ (0, 1/2].

Lemma 6. Fix a positive scalar ϵ ≤ 1/2*, and let* τ ≥ tmix(ϵ) be an integer. For each i ∈ [n], define the stochastic processes

$$Z_{i}=(X_{1},X_{2},\ldots,X_{i-\tau},X_{i},X_{i+\tau},X_{i+\tau+1},\ldots,X_{n})\tag{52}$$ $$Z^{\prime}_{i}=(X_{1},X_{2},\ldots,X_{i-\tau},X^{\prime}_{i},X_{i+\tau},X_{i+\tau+1},\ldots,X_{n}),\tag{53}$$

where X′
i ∼ π is drawn independently of everything else. Then dTV(Zi, Z′
i
) ≤ 4ϵ.

Consequently, for any function f : X
n−2τ → [0, 1]*, we have*

$$|\,\mathbb{E}[f(Z_{i})-f(Z_{i}^{\prime})]|\leq4\epsilon.$$

34 Proof. Let Ai = (Xi−τ , Xi, Xi+τ ) and A′i = (Xi−τ , X′
i
, Xi+τ ). By the Markov property, we have dTV(Zi, Z′
i
) = dTV(Ai, A′i
). But the distributions of these triples can be written explicitly, as

$$\begin{array}{l}{{\Pr\{A_{i}=(j,k,\ell)\}=\Pr\{(X_{i-\tau},X_{i},X_{i+\tau})=(j,k,\ell)\}=\pi_{j}\cdot e_{j}^{\top}P^{\tau}e_{k}e_{k}^{\top}P^{\tau}e_{\ell}\mathrm{~and~}}}\\ {{\Pr\{A_{i}^{\prime}=(j,k,\ell)\}=\Pr\{(X_{i-\tau},X_{i}^{\prime},X_{i+\tau})=(j,k,\ell)\}=\pi_{j}\cdot\pi_{k}\cdot e_{j}^{\top}P^{2\tau}e_{\ell}.}}\end{array}$$

Here ej ∈ R
X denotes the indicator vector that is 1 in index j ∈ X and 0 elsewhere. For each pair of indices (j, k) *∈ X × X* , define

$$\delta_{j,k}:=e_{j}^{\top}P^{\tau}e_{k}-\pi_{k}\mathrm{~and~}\bar{\delta}_{j,k}:=e_{j}^{\top}P^{2\tau}e_{k}-\pi_{k}.$$

Owing to our total variation mixing assumption (5) and the choice τ ≥ tmix(ϵ), we have that the ℓ1 size of errors is bounded as

$$\operatorname*{max}_{j\in\mathcal{X}}\sum_{k\in\mathcal{X}}|\delta_{j,k}|\leq2\epsilon\quad\mathrm{~and~}\quad\operatorname*{max}_{j\in\mathcal{X}}\sum_{k\in\mathcal{X}}|\overline{{{\delta}}}_{j,k}|\leq2\epsilon^{2}.$$

With this shorthand notation, we may define

$$\begin{array}{l}{{\Pr\{A_{i}=(j,k,\ell)\}=\pi_{j}\cdot(\pi_{k}+\delta_{j,k})\cdot(\pi_{\ell}+\delta_{k,\ell})\mathrm{~and~}}}\\ {{\Pr\{A_{i}^{\prime}=(j,k,\ell)\}=\pi_{j}\cdot\pi_{k}\cdot(\pi_{\ell}+\overline{{{\delta}}}_{j,\ell})}}\end{array}$$

and we can write the total variation explicitly as dTV(Ai, A′i
)

= 1 2 X j,k,ℓ∈X |πj · (πk + δj,k) · (πℓ + δk,ℓ) − πj · πk · (πℓ + δj,ℓ)| (55) = 1 2 X j,k,ℓ∈X |πj · πk · δk,ℓ + πj · πℓ· δj,k + πj · δj,k · δk,ℓ − πj · πk · δj,ℓ| (56) ≤ 1 2 X j,k,ℓ∈X |πj · πk · δk,ℓ| +X j,k,ℓ∈X 1 2 |πj · πℓ· δj,k| +X j,k,ℓ∈X 1 2 |πj · δj,k · δk,ℓ| +X j,k,ℓ∈X 1 2 |πj · πk · δj,ℓ|
$$(54)$$
$$\left(55\right)$$
(56)  $\stackrel{\text{̂}}{b}_{j,\ell}\text{|}$  (57)  . 
$$(58)$$
$$(59)$$
$$\stackrel{(\mathrm{i})}{\leq}\epsilon+\epsilon+2\epsilon^{2}+\epsilon^{2}\leq4\epsilon,$$
2 ≤ 4ϵ, (58)
where we claim that the bound in step (i) holds term by term and the last inequality uses the fact that ϵ ≤ 1/2. It remains to prove step (i). The first term can be bounded as

$$\sum_{j,k,\ell\in{\mathcal{X}}}|\pi_{j}\cdot\pi_{k}\cdot\delta_{k,\ell}|\leq\sum_{j,k\in{\mathcal{X}}}\pi_{j}\cdot\pi_{k}\sum_{\ell\in{\mathcal{X}}}|\delta_{k,\ell}|\leq\sum_{j,k\in{\mathcal{X}}}\pi_{j}\cdot\pi_{k}\cdot(2\epsilon)=2\epsilon,$$

where the last equality follows because π is a probability distribution. The remaining terms can be bounded using similar logic, so we omit the steps for brevity.

The consequence of the TV bound for expectations of bounded functions follows as a definition of total variation.

Lemma 7. Fix a positive scalar ϵ ≤ 1/2*, and let* τ ≥ tmix(ϵ) be an integer. For each i1 < i2 ∈ [n] with i2 − i1 > τ *, define the stochastic processes*

$$Z_{i_{1},i_{2}}=(X_{1},X_{2},\ldots,X_{i_{1}-\tau},X_{i_{1}},X_{i_{1}+\tau},\ldots,X_{i_{2}-\tau},X_{i_{2}},X_{i_{2}+\tau},\ldots,X_{n})\tag{60}$$ $$Z^{\prime}_{i_{1},i_{2}}=(X_{1},X_{2},\ldots,X_{i_{1}-\tau},X^{\prime}_{i_{1}},X_{i_{1}+\tau},\ldots,X_{i_{2}-\tau},X^{\prime}_{i_{2}},X_{i_{2}+\tau},\ldots,X_{n}),\tag{61}$$

where X′
i1
, X′
i2 ∼ π *are drawn independently of each other and of everything else. Then we have* dTV(Zi1,i2
, Z′
i1,i2
) ≤ 8ϵ.

Consequently, for any function f with range [0, 1]*, we have*

$$|\operatorname{\mathbb{E}}[f(Z_{i,j})-f(Z_{i,j}^{\prime})]|\leq8\epsilon.$$

Proof. We prove the bound on total variation, noting that the consequence for bounded functions follows as a corollary. As in the proof of Lemma 6, we define the sub-processes

$$\begin{array}{l}{{A_{i_{1},i_{2}}=(X_{i_{1}-\tau},X_{i_{1}},X_{i_{1}+\tau},X_{i_{2}-\tau},X_{i_{2}},X_{i_{2}+\tau})}}\\ {{A_{i_{1},i_{2}}^{\prime}=(X_{i_{1}-\tau},X_{i_{1}}^{\prime},X_{i_{1}+\tau},X_{i_{2}-\tau},X_{i_{2}}^{\prime},X_{i_{2}+\tau}).}}\end{array}$$

We also define an intermediate sub-process Aei1,i2 = (Xi1−τ , X′
i1
, Xi1+τ , Xi2−τ , Xi2
, Xi2+τ ) for convenience. Then, simplifying the expression for total variation over the entire Markov chain and noting that the stochastic processes Zi1,i2
, Z′
i1,i2 follow identical transition laws over the indices
{1, . . . , i1 − τ*} ∪ {*i1 + τ + 1, . . . , i2 − τ*} ∪ {*i2 + τ + 1*, . . . , n*}

dTV(Zi1,i2
$$Z_{i_{1},i_{2}}^{\prime})=\mathsf{d_{T V}}(A_{i_{1}}$$
, A′i1,i2
)
(i)
≤ dTV(Ai1,i2
$${}_{\!:},A_{i_{1},i_{2}}^{\prime})$$
$${}_{i_{2}},\widetilde{A}_{i_{1},i_{2}})+\mathrm{d}_{\mathrm{TV}}(\widetilde{A}_{i_{1}},$$
where step (i) follows by the triangle inequality. We proceed to upper bound each of the terms dTV(Ai1,i2
, Aei1,i2
) and dTV(Aei1,i2
, A′i1,i2
) by 4ϵ each, using a similar argument to the proof of Lemma 6. We denote ρj2,ℓ1 = Pr[Xi2−τ−1 = j2|Xi1+τ+1 = ℓ1] as shorthand, noting that for each ℓ1 ∈ X , we have Pj2∈X ρj2,ℓ1 = 1. We begin with the first term dTV(Ai1,i2
, Aei1,i2
) and characterize the distributions of Ai1,i2
, Aei1,i2 as below:
Pr{Ai1,i2 = (j1, k1, ℓ1, j2, k2, ℓ2)} = πj1
· e
⊤
j1P
τek1 e
⊤
k1P
τeℓ1
· ρj2,ℓ1
· e
⊤
j2P
τek2 e
⊤
k2P
τeℓ2 and Pr{A
′
i1,i2 = (j1, k1, ℓ1, j2, k2, ℓ2)} = πj1
· πk1
· e
⊤
j1P
2τeℓ1
· ρj2,ℓ1
· e
⊤
j2P
τek2 e
⊤
k2P
τeℓ2
.

Recalling the shorthand notation δj,k, δj,k that was defined in the proof of Lemma 6, we can write the above as Pr{Ai1,i2 = (j1, k1, ℓ1, j2, k2, ℓ2)} = πj1
· (πk1 + δj1,k1
) · (πℓ1 + δk1,ℓ1
) · ρj2,ℓ1
· (πk2 + δj2,k2
) · (πℓ2 + δk2,ℓ2
)
Pr{Aei1,i2 = (j1, k1, ℓ1, j2, k2, ℓ2)} = πj1
· πk1
· (πℓ1 + δj1,ℓ1
) · ρj2,ℓ1
· (πk2 + δj2,k2
) · (πℓ2 + δk2,ℓ2
).

Next, we note that ρj2,ℓ1
· (πk2 + δj2,k2
) · (πℓ2 + δk2,ℓ2
) = Pr[Xi2−τ−1 = j2, Xi2 = k2, Xi2+τ+1 =
ℓ2|Xi1+τ+1 = ℓ1] which is a conditional probability distribution that is identical for the stochastic processes Aei1,i2 and Ai1,i2
. Therefore, we have Pj2,k2,ℓ2∈X ρj2,ℓ1
·(πk2 + δj2,k2
)·(πℓ2 + δk2,ℓ2
) = 1 for any value of ℓ1 ∈ X . This yields

dTV(Ai1,i2
, Aei1,i2
)
=
1
2
X
j1,k1,ℓ1∈X
j2,k2,ℓ2∈X
πj1
(πk1 + δj1,k1
)(πℓ1 + δk1,ℓ1
)ρj2,ℓ1
(πk2 + δj2,k2
)(πℓ2 + δk2,ℓ2
)
− πj1 πk1
(πℓ1 + δj1,ℓ1
)ρj2,ℓ1
(πk2 + δj2,k2
)(πℓ2 + δk2,ℓ2
)

=
1
2
X
j1,k1,ℓ1∈X
j2,k2,ℓ2∈X
ρj2,ℓ1
(πk2 + δj2,k2
)(πℓ2 + δk2,ℓ2
)
πj1
(πk1 + δj1,k1
)(πℓ1 + δk1,ℓ1
) − πj1 πk1
(πℓ1 + δj1,ℓ1
)

=
1
2
X
j1,k1,ℓ1∈X
πj1
(πk1 + δj1,k1
)(πℓ1 + δk1,ℓ1
) − πj1 πk1
(πℓ1 + δj1,ℓ1
)
,
where the last equality uses the fact that Pj2,k2,ℓ2∈X ρj2,ℓ1
· (πk2 + δj2,k2
) · (πℓ2 + δk2,ℓ2
) = 1 for
any value of ℓ1 ∈ X . We have thus arrived an expression for dTV(Ai1,i2
, Aei1,i2
) that is identical to Equation (55), which is upper bounded by 4ϵ. Therefore, we have dTV(Ai1,i2
, Aei1,i2
) ≤ 4ϵ.

We now use a similar technique to bound the other term dTV(Aei1,i2
, A′i1,i2
). In particular, we have

Pr{Aei1,i2 = (j1, k1, ℓ1, j2, k2, ℓ2)} = πj1 · πk1 · (πℓ1 + δj1,ℓ1 ) · ρj2,ℓ1 · (πk2 + δj2,k2 ) · (πℓ2 + δk2,ℓ2 ) Pr{A ′ i1,i2 = (j1, k1, ℓ1, j2, k2, ℓ2)} = πj1 · πk1 · (πℓ1 + δj1,ℓ1 ) · ρj2,ℓ1 · πk2 · (πℓ2 + δj2,ℓ2 ).
This time, we note that πj1
· πk1
· (πℓ1 + δj1,ℓ1
) · ρj2,ℓ1 = Pr[Xi1−τ−1 = j1, X′
i1 = k1, Xi1+τ+1 =
ℓ1, Xi2−τ−1 = j2] and therefore Pj1,k1,ℓ1∈X πj1
· πk1
· (πℓ1 + δj1,ℓ1
) · ρj2,ℓ1 = Pr[Xi2−T −1 = j2] = πj2
.

Using a similar series of steps to the preceding calculation, we obtain

$$\mathrm{d}\tau_{\mathrm{TV}}(\widehat{A}_{i_{1},i_{2}},A_{i_{1},i_{2}})=\frac{1}{2}\sum_{j_{2},k_{2},\ell_{2}\in\mathcal{X}}\left|\pi_{j_{2}}(\pi_{k_{2}}+\delta_{j_{2},k_{2}})(\pi_{\ell_{2}}+\delta_{k_{2},\ell_{2}})-\pi_{j_{2}}\pi_{k_{2}}(\pi_{\ell_{2}}+\overline{{{\delta}}}_{j_{2},\ell_{2}})\right|\leq4\epsilon_{\mathrm{TV}}(\overline{{{\delta}}}_{j_{2},\ell_{2}}).$$

by an identical argument to Equation (55). Putting these together yields dTV(Zi1,i2
, Z′
i1,i2
) ≤ 8ϵ, which completes the proof of the lemma.

Lemma 8. Fix a positive scalar ϵ ≤ 1/2 *and let* τ ≥ tmix(ϵ) denote a positive integer. Let n0 = n/τ .

For each j ∈ [n0]*, define the stochastic process* (X′k
)k∈Djτ as a |Djτ |*-length Markov chain with* transition kernel P and initial state sampled from the distribution π *and independently of everything* else. Let Sj = {ℓ ∈ [n0] : |ℓ − j| mod 3 ≡ 0}*. Now define the stochastic processes*

$$W_{j}=\bigoplus_{\ell\in S_{j}}X_{\mathcal{B}_{\ell}}\quad\quad\text{and}\tag{62}$$ $$W_{j}^{\prime}=\bigoplus_{\ell\in S_{j}}X_{\mathcal{B}_{\ell}}^{\prime}\tag{63}$$

Then we have dTV(Wj , W′
j
) ≤ n0 · ϵ.

Consequently, for any function f having range [0, 1]*, we have*

$$|\mathbb{E}[f(W_{j})-f(W_{j}^{\prime})]|\leq n_{0}\epsilon.$$

37 Proof. We prove the bound on total variation, noting that the consequence for bounded functions follows as a corollary. Denote m = |Sj | as shorthand and index the elements of Sj as ℓ1*, . . . , ℓ*m.

Fix j and, for each k = 0, 1*, . . . m*, define the auxiliary stochastic process

$$\widetilde{W}_{j}^{(k)}=\left(\bigoplus_{k^{\prime}=1}^{k}X_{B_{\ell_{k^{\prime}}}}\right)\bigoplus\left(\bigoplus_{k^{\prime}=k+1}^{m}X_{B_{\ell_{k^{\prime}}}}^{\prime}\right).$$

noting that Wf(m)
j = Wj and Wf(0)
j = W′
j
. Then by the triangle inequality,

$$\mathrm{d}_{\mathrm{TV}}(W_{j},W_{j}^{\prime})\leq\sum_{k=0}^{m-1}\mathrm{d}_{\mathrm{TV}}(\widetilde{W}_{j}^{(k)},\widetilde{W}_{j}^{(k+1)}).$$
(64) $$\begin{array}{l}\small\text{(64)}\end{array}$$. 
We now claim that

$$\mathrm{d}_{\mathrm{TV}}(\widetilde{W}_{j}^{(k)},\widetilde{W}_{j}^{(k+1)})\leq\epsilon{\mathrm{~for~all~}}k=0,1,\ldots,m-1.$$
j) ≤ ϵ for all k = 0, 1*, . . . , m* − 1. (64)
Since m = |Sj | ≤ n0, this claim immediately yields the desired result.

Proof of claim (64): For strings s1, . . . , sk ∈ X 2τeach of length 2τ , we let ρ(s1*, . . . , s*k) =
Pr{XBℓ1
= s1*, . . . , X*Bℓk
= sk}. For additional strings5sk+2, . . . , sm ∈ X 2τ, we also define

$\mu(s_{k+2},\ldots,s_{m})=\Pr\{X^{\prime}_{B^{\prime}_{t_{k+2}}}=s_{k+2},\ldots,X^{\prime}_{B^{\prime}_{t_{m}}}=s_{m}\}$ for $s_{1},\ldots,s_{m}\in\mathcal{X}^{2\tau}$.  
Using the Markov property and the mutual independence of {X′Bℓ
}ℓ∈Sj
, we have

$$\mathrm{d}_{\mathrm{TV}}(\overline{W}_{j}^{(k)},\overline{W}_{j}^{(k+1)})$$ $$=\frac{1}{2}\sum_{s_{1},\ldots,s_{k},s_{k+2},\ldots,s_{m}\in\mathbb{X}^{2^{r}}}\left|\rho(s_{1},\ldots,s_{k})\cdot\Pr\{X_{\overline{\nu}_{k_{k+1}}}=s|X_{\overline{\nu}_{k_{1}}}=s_{1},\ldots,X_{\overline{\nu}_{k_{k}}}=s_{k}\}\cdot\mu(s_{k+2},\ldots,s_{m})\right|$$
$$-\rho(s_{1},\ldots,s_{k})\cdot\Pr\{X^{\prime}_{B_{k_{k+1}}}=s\}\cdot\mu(s_{k+2},\ldots,s_{m})\Big{|}$$  $$=\frac{1}{2}\sum_{s_{1},\ldots,s_{k}\in X^{\prime}}\rho(s_{1},\ldots,s_{k})\cdot\sum_{s\in X^{\prime}}\Big{|}\Pr\{X_{B_{k_{k+1}}}=s|X_{B_{k_{1}}}=s_{1},\ldots,X_{B_{k_{k}}}=s_{k}\}-\Pr\{X^{\prime}_{B_{k_{k+1}}}=s\}\Big{|}.$$

Next, we characterize the term Ps∈X2τ |Pr{XBℓk+1
= s|XBℓ1
= s1*, . . . , X*Bℓk
= sk} − Pr{X′Bℓk+1
=
s}| for each fixed tuple (s1*, . . . , s*k). Let s(i) denote the i-th element in the string s. Note that
(τ − 1)ℓk+1 + 1 is the first index of Bℓk+1 , and τ ℓk is the index in Bℓk
. By the Markov property, we 5The last string sm may be of shorter length, but our argument can be modified straightforwardly to accommodate this case.

have

s∈X2τ Pr{XBℓk+1 = s|XBℓ1 = s1, . . . , XBℓk = sk} − Pr{X′Bℓk+1 = s}  X s(1)∈X Pr{X(τ−1)ℓk+1+1 = s(1)|XBℓ1 = s1, . . . , XBℓk = sk} − Pr{X′(τ−1)ℓk+1+1 = s(1)}  =X (i) =X s(1)∈X Pr{X(τ−1)ℓk+1+1 = s(1)|Xτ ℓk = sk(τ )} − Pr{X′(τ−1)ℓk+1+1 = s(1)}  s(1)∈X |e ⊤ sk(τ)P 3τ+1es(1) − πs(1)| =: X s(1)∈X |δsk(τ),s(1)| (iii) ≤ 2ϵ. (ii) =X Above, equality (i) again uses the Markov property, equality (ii) uses the fact that ℓk+1 = ℓk + 3
by definition, and inequality (iii) uses Eq. (54). Plugging this into the previous display yields

$$\mathbf{d}_{\mathrm{{TV}}}({\widetilde{W}}_{j}^{(k)},{\widetilde{W}}_{j}^{(k+1)})={\frac{1}{2}}\sum_{s_{1},\ldots,s_{k}\in{\mathcal{X}}^{2r}}\rho(s_{1},\ldots,s_{k})\cdot2\epsilon=\epsilon.$$

This completes the proof of the lemma.

## B Intuition For Data-Dependent Tuning Of Window Size Τ

In this section, we provide some simple intuition to justify the data-dependent tuning procedure for the window size τ that we described in Section 6.1. Assuming that6 n ≫ Tmix, we have that Z
(1)
and Z
(2) are near-independent since they are significantly separated within the sequence. Thus, conditioned on Z
(1), the sequence Z
(2) should be thought of as an independent Markov chain started at the stationary distribution π. Consequently, the random variable Mf(Z
(1)) ought to be close to the estimand Mπ(Z
(1)), and this can be formalized via a bounded differences inequality for mixing Markov chains (Paulin, 2015). Indeed, if independence between Z
(1) and Z
(2) held exactly, then it is straightforward to show that with high probability over the randomness in Z
(2), we have

$$|\widetilde{M}(Z^{(1)})-M_{\pi}(Z^{(1)})|^{2}\stackrel{<}{\sim}\frac{\mathsf{T}_{\mathrm{mix}}\log(n/\mathsf{T}_{\mathrm{mix}})}{n}.$$

 ) $$\tag*{(65)}$$  must have the inequality. 
Now Theorem 1 guarantees that for some τ0 ≍ Tmix log(n/Tmix), we must have the inequality7
McWingIt(Z
(1); τ0) − Mπ(Z
(1))

2≲

τ n
. Combining this observation with Ineq. (65) and noting that τ0 ≍ Tmix log(n/Tmix), we have

$$\widehat{M}_{\rm WNcIT}(Z^{(1)};\tau_{0})-\widehat{M}(Z^{(1)})\bigg{|}^{2}\leq2\left|\widehat{M}_{\rm WNcIT}(Z^{(1)};\tau_{0})-M_{\pi}(Z^{(1)})\right|^{2}+2\left|M_{\pi}(Z^{(1)})-\widehat{M}(Z^{(1)})\right|^{2}\lesssim\frac{\tau_{0}}{n}.$$

Thus, we see that Ineq. (28) is a reasonable validation criterion since it is satisfied for some choice of window size at most τ0, for a suitable choice of constant Ctune on the RHS. Conversely, if Ineq. (28)

holds for some smaller window size τ = τb ≤ τ0, then combining this with Ineq. (65) yields
$$\frac{1}{2}\left|\widehat{M}_{\text{WroGl}\tau}(Z^{(1)};\widehat{\tau})-M_{\pi}(Z^{(1)})\right|^{2}\leq\left|\widehat{M}_{\text{WroGl}\tau}(Z^{(1)};\widehat{\tau})-\widehat{M}(Z^{(1)})\right|^{2}+\left|M_{\pi}(Z^{(1)})-\widehat{M}(Z^{(1)})\right|^{2}$$ $$\leq\frac{\widehat{\tau}}{n}+\frac{\tau_{\text{mb}}\log(n/\mathsf{T}_{\text{mb}i})}{n}$$ $$\leq\frac{\tau_{0}}{n}+\frac{\tau_{\text{mb}i}\log(n/\mathsf{T}_{\text{mb}i})}{n}\leq\frac{\mathsf{T}_{\text{mb}i}\log(n/\mathsf{T}_{\text{mb}i})}{n}.$$

Putting together the pieces, we see that our validation procedure is reasonable since (a) It is satisfied by the window size τ0 prescribed by Theorem 1, and (b) It always produces a good value of tuning window size τb, in that this choice of window size leads to the optimal rate of estimation of the functional Mπ(Z
(1)).

It is important to note that the above sketch does not constitute a rigorous argument. In order to make it rigorous, one would have to formally establish Eq. (65) and also a version of Theorem 1 that holds with high probability, both of which are interesting directions for future work.