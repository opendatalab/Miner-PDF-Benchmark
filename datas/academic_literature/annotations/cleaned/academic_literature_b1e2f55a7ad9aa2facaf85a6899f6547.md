# A New Statistic for Testing Covariance Equality in High-Dimensional Gaussian Low-Rank Models 

R. Beisson, Student Member, IEEE, P. Vallet, Member, IEEE, A. Giremus, Member, IEEE, G. Ginolhac,<br>Member, IEEE


#### Abstract

In this paper, we consider the problem of testing equality of the covariance matrices of $L$ complex Gaussian multivariate time series of dimension $M$. We study the special case where each of the $L$ covariance matrices is modeled as a rank $K$ perturbation of the identity matrix, corresponding to a signal plus noise model. A new test statistic based on the estimates of the eigenvalues of the different covariance matrices is proposed. In particular, we show that this statistic is consistent and with controlled type I error in the high-dimensional asymptotic regime where the sample sizes $N_{1}, \ldots, N_{L}$ of each time series and the dimension $M$ both converge to infinity at the same rate, while $K$ and $L$ are kept fixed. We also provide some simulations on synthetic and real data (SAR images) which demonstrate significant improvements over some classical methods such as the GLRT, or other alternative methods relevant for the highdimensional regime and the low-rank model.


## I. INTRODUCTION

D ETECTING changes in the behaviour of multivariate time series is a fundamental problem in many applications going from remote sensing [2], [3], [4], [5] and wireless communications [6] to finance [7], climatology [8] or genomics [9]. In several of those applications, a usual approach consists in modeling the changes using the distribution of the time series, and in particular through an evolution in the structure of the covariance matrix.

Consider the context of $M$-dimensional time series $\left(\mathbf{y}_{n, 1}\right)_{n \in \mathbb{Z}}, \ldots,\left(\mathbf{y}_{n, L}\right)_{n \in \mathbb{Z}}$, assumed mutually independent and such that for all $\ell \in\{1, \ldots, L\}$,

$$
\left(\mathbf{y}_{n, \ell}\right)_{n \in \mathbb{Z}} \stackrel{\text { i.i.d. }}{\sim} \mathcal{N}_{\mathbb{C}^{M}}\left(\mathbf{0}, \mathbf{R}_{\ell}\right)
$$

where $\mathcal{N}_{\mathbb{C}^{M}}\left(\mathbf{0}, \mathbf{R}_{\ell}\right)$ denotes the zero-mean complex normal distribution with covariance matrix $\mathbf{R}_{\ell}$. Detecting the changes in the distribution of $\left(\mathbf{y}_{n, \ell}\right)_{n \in \mathbb{Z}}$, for all $\ell \in\{1, \ldots, L\}$, can be formalized as the following binary hypothesis test dealing with the equality of the $L$ covariance matrices $\mathbf{R}_{1}, \ldots, \mathbf{R}_{L}$,

$$
\begin{aligned}
\mathcal{H}_{0}: & \mathbf{R}_{1}=\ldots=\mathbf{R}_{L} \\
\mathcal{H}_{1}: & \exists(i, j) \in\{1, \ldots, L\}^{2}: \mathbf{R}_{i} \neq \mathbf{R}_{j}
\end{aligned}
$$

Assume that for all $\ell \in\{1, \ldots, L\}, N_{\ell}$ observations $\mathbf{y}_{1, \ell}, \ldots, \mathbf{y}_{N_{\ell}, \ell}$ are available and let $N=N_{1}+\cdots+N_{L}$. A

R. Beisson, P. Vallet and A. Giremus are with Laboratoire de l'Intégration du Matériau au Système (CNRS, Univ. Bordeaux, Bordeaux INP), 351 Cours de la Libération, 33400 Talence (France)

G. Ginolhac is with Laboratoire d'Informatique, Systèmes, Traitement de l'Information et de la Connaissance (Univ. Savoie/Mont-Blanc, Polytech Annecy), 5 chemin de Bellevue, 74940 Annecy (France)

This work was partially supported by Agence de l'Innovation de Défense and Région Nouvelle-Aquitaine. The material of this paper was partly presented in the conference paper [1]. large class of test statistics widely encountered in the literature [3] involves, provided that $M<N_{1}, \ldots, N_{L}$, linear spectral statistics of the matrices $\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}$ of the form:

$$
S=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \frac{1}{M} \sum_{k=1}^{M} \varphi\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)\right)
$$

where $\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)$, for all $k \in\{1, \ldots, M\}$, are the eigenvalues of the matrix $\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}$ with

$$
\hat{\mathbf{R}}_{\ell}:=\frac{1}{N_{\ell}} \sum_{n=1}^{N_{\ell}} \mathbf{y}_{n, \ell} \mathbf{y}_{n, \ell}^{*}
$$

denoting the sample covariance matrix (SCM) associated with $\mathbf{R}_{\ell}$ and

$$
\hat{\mathbf{R}}=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \hat{\mathbf{R}}_{\ell}
$$

In (3), $\varphi$ denotes some continuous function defined on $(0,+\infty)$. In particular, the Generalized Likelihood Ratio (GLR) [3] with $\varphi(x)=\log (x)$ or the Nagao statistic with $\varphi(x)=(x-1)^{2}$ are included in the class of statistics (3). The presence of a change in the covariance is decided by comparing (3) to a threshold $\epsilon$ chosen to guarantee a certain type I error and the null hypothesis $\mathcal{H}_{0}$ is rejected if $S>\epsilon$. Moreover, the test statistics based on (3) have the key property that the distribution of $S$ under $\mathcal{H}_{0}$ is independent of $\mathbf{R}_{1}=\ldots=\mathbf{R}_{L}$, which allows to control its type I error.

However, in practice, the distribution of statistics of type (3) under $\mathcal{H}_{0}$ is untractable and only known in a few special cases for finite $M, N_{1}, \ldots, N_{L}$ (e.g. for the GLR, see [10]). To circumvent this issue, approximations in the low-dimensional (or large sample size) regime in which $N_{1}, \ldots, N_{L} \rightarrow \infty$ while $M, L$ are fixed can be derived, see e.g. [11, Th. 10.8.4]. While the latter are meant to be used in practical scenarios where $N_{1}, \ldots, N_{L} \gg M$, they may not be reliable in contexts involving high-dimensional (large $M$ ) observations or moderate sample sizes $N_{1}, \ldots, N_{L}$. Indeed, in that highdimensional case, it is often more reasonable to assume that $M, N_{1}, \ldots, N_{L}$ are of the same order of magnitude in which case the predictions of the distribution of (3) under $\mathcal{H}_{0}$ in the low-dimensional regime become irrelevant.

The context where $M, N_{1}, \ldots, N_{L}$ are of the same order of magnitude can be modeled more realistically by the highdimensional regime in which it is assumed that $M$ converges to infinity together with $N_{1}, \ldots, N_{L}$ such that $\frac{M}{N_{\ell}} \rightarrow c_{\ell}>0$,
while $L$ is kept fixed. In this non-standard regime, the asymptotic distribution of the statistic $S$ can be derived using random matrix theory techniques (see e.g. [12] for the case $L=2$ ).

Moreover, in several applications involving highdimensional observations, the potential changes in the covariance $\mathbf{R}_{\ell}$ may only be carried by a low-rank component (see e.g. [13], [14], [15]). This is the case, e.g., in array processing when dealing with a large array of $M$ sensors and a small number $K$ of source signals compared to $M$ [15].

In that case, we have the model

$$
\mathbf{R}_{\ell}=\boldsymbol{\Gamma}_{\ell}+\sigma^{2} \mathbf{I}
$$

with $\boldsymbol{\Gamma}_{\ell}$ the covariance matrix of rank $K<M$ of a useful signal and $\sigma^{2} \mathbf{I}$ the covariance matrix of a spatially white additive noise. When the rank $K$ remains constant in the high-dimensional regime, the matrices $\mathbf{R}_{\ell}^{-1} \mathbf{R}_{\ell^{\prime}}$ are fixed rank perturbations of the identity. Using well-known results [16], [17] on the asymptotic spectral distribution of the Fisher type random matrices $\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}$, one can show under both $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$ that

$$
S \rightarrow \sum_{\ell=1}^{L} \frac{c}{c_{\ell}} \int_{x_{\ell}^{-}}^{x_{\ell}^{+}} \varphi\left(\frac{c}{c_{\ell}}(1+x)\right) f_{\ell}(x) \mathrm{d} x
$$

almost surely (a.s.) where $c=\left(c_{1}^{-1}+\ldots+c_{L}^{-1}\right)^{-1}$ and where $f_{\ell}$ is the so-called Wachter distribution given by

$$
f_{\ell}(x)=\left(\frac{1}{c_{\ell}}-1\right) \frac{\sqrt{\left(x-x_{\ell}^{-}\right)\left(x_{\ell}^{+}-x\right)}}{2 \pi x(1+x)} \mathbb{1}_{\left[x_{\ell}^{-}, x_{\ell}^{+}\right]}(x)
$$

with $x_{\ell}^{ \pm}=\frac{c_{\ell}-c}{c\left(1-c_{\ell}\right)^{2}}\left(1 \pm \sqrt{c_{\ell}+\frac{c c_{\ell}}{c_{\ell}-c}-\frac{c c_{\ell}^{2}}{c_{\ell}-c}}\right)^{2}$. Thus $S$ converges to the same limit under both hypotheses $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$, which indicates that test statistics relying on (3) might not be relevant in the high-dimensional regime and for the low-rank model in (6).

So far from our knowledge, the problem of covariance equality testing under low-rank models has not received much attention in the literature. The work of [18] considers the GLRT, under a low-rank Gaussian model, for a covariance equality test with a different alternative hypothesis $\mathcal{H}_{1}^{\prime}: \mathbf{R}_{1} \neq$ $\mathbf{R}_{2}=\ldots=\mathbf{R}_{L}$. An extension to the specific case of subspace equality test has also been proposed by the same authors in [19].

Under the model (6), the information about a potential change is contained in the $K$ largest eigenvalues and associated eigenvectors of $\mathbf{R}_{\ell}$. Therefore, classical results on the spiked models for random matrices of the Fisher type [17] can be exploited to characterize the asymptotic behaviour of the extreme eigenvalues of $\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)_{\ell=1, \ldots, L}$, from which information about a potential change can be extracted. In the same way, the asymptotic behaviour of the largest eigenvalues of the spiked Wishart-type matrices [20] $\hat{\mathbf{R}},\left(\hat{\mathbf{R}}_{\ell}\right)_{\ell=1, \ldots, L}$ convey information about changes in the true covariances $\mathbf{R}_{1}, \ldots, \mathbf{R}_{L}$ [1], which can also be exploited to build test statistics relevant for the low-rank model in the high-dimensional regime. This latter option is the path followed in this paper.

Contributions. In this paper, we derive a new test statistic, no longer based on the family of statistics $S$ studied in [3], but which relies on the $K$ largest eigenvalues of the matrices $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}, \hat{\mathbf{R}}$. More precisely, the test statistic compares in a certain sense estimates of the eigenvalues of the matrices $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}$ with estimates of the eigenvalues of the mixture $\boldsymbol{\Gamma}=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \boldsymbol{\Gamma}_{\ell}$. We show that the proposed test statistic is consistent under the high-dimensional regime and the low-rank model (6), and with a controlled asymptotic type I error. To that purpose, the results of [21], which provides the asymptotic distribution of the $K$ largest eigenvalues of $\hat{\mathbf{R}}_{\ell}$ for a fixed $\ell$, are extended to provide the joint asymptotic distribution of the $K$ largest eigenvalues of the matrices $\hat{\mathbf{R}}, \hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$. The proposed test statistic is then compared to various alternatives, including the GLRT for the low-rank model (6) as well as a statistic built from the results of [17] on the extreme eigenvalues of the spiked Fisher matrices $\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)_{\ell=1, \ldots, L}$. We also provide an empirical study of the proposed test statistic on Synthetic Aperture Radar (SAR) images for detecting changes between two scenes.

Organization. The paper is organized as follows. In Section [I]. we study an extension of the results of [21] on the asymptotic distribution of the largest eigenvalues of $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}, \hat{\mathbf{R}}$. In Section III, we exploit the results derived in the previous section to build a new test statistic, for which we study its performance in the high-dimensional regime. Sections IV] and $\mathrm{V}$ are dedicated to compare, both theoretically and numerically, our proposed test statistic with alternative approaches. Simulations on synthetic data and on real data (SAR images) are provided.

Notations. For $a \in \mathbb{R}, a^{+}$denotes the positive part. Vectors and matrices are denoted with boldface lower case and upper case letters respectively. For a complex matrix $\mathbf{A}$, we denote by $\mathbf{A}^{T}$ and $\mathbf{A}^{*}$ its transpose and conjugate transpose. If $\mathbf{A}$ is a $n \times n$ complex matrix, $\operatorname{tr}(\mathbf{A})$ denotes its trace and $\lambda_{1}(\mathbf{A}), \ldots, \lambda_{n}(\mathbf{A})$ denote its eigenvalues. If $\mathbf{A}$ is Hermitian, the eigenvalues are considered in decreasing order $\lambda_{1}(\mathbf{A}) \geq$ $\ldots \geq \lambda_{n}(\mathbf{A})$. For matrices $\mathbf{A}_{1}, \ldots, \mathbf{A}_{n}, \operatorname{bdiag}\left(\mathbf{A}_{1}, \ldots, \mathbf{A}_{n}\right)$ denotes the the block diagonal matrix formed by $\mathbf{A}_{1}, \ldots, \mathbf{A}_{n}$. The complex circular Gaussian distribution on $\mathbb{C}^{n}$ with covariance matrix $\mathbf{R}$ is denoted as $\mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0}, \mathbf{R})$, while the real Gaussian distribution on $\mathbb{R}^{n}$ with mean $\boldsymbol{\mu}$ and covariance matrix $\mathbf{R}$ is denoted as $\mathcal{N}_{\mathbb{R}^{n}}(\boldsymbol{\mu}, \mathbf{R})$.

## II. Spectrum of $\hat{\mathbf{R}}$

In this section, we study the asymptotic behavior at $1^{\text {st }}$ and $2^{\text {nd }}$ orders of the largest eigenvalues of $\hat{\mathbf{R}}$ when the matrices $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$ follow the low-rank model (6).

Consider the following two assumptions, which describe the high-dimensional regime and specify the asymptotic behavior of the eigenvalues of $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}$.

Assumption 1. The sample sizes $N_{1}=N_{1}(M), \ldots, N_{L}=$ $N_{L}(M)$ are functions of $M$ such that

$$
\frac{M}{N_{\ell}}=c_{\ell}+o\left(\frac{1}{\sqrt{M}}\right)
$$

as $M \rightarrow \infty$, where $c_{1}, \ldots, c_{L}>0$ and $K, L$ are independent of $M$.

In comparison with the classical low-dimensional regime where $M$ is assumed fixed while $N_{1}, \ldots, N_{L} \rightarrow \infty$ (see e.g. [22], [11]), the high-dimensional regime described in Assumption 1 models practical scenarios where the sample sizes $N_{1}, \ldots, N_{L}$ are of the same order of magnitude as the dimension $M$ and where $K$ is small compared to $M$. This regime has been widely used in the high-dimensional statistics literature (see e.g. [23]), as well as in the signal processing applications (see e.g. [15], [24], [25]).

In what follows the high-dimensional regime described in Assumption 1 is represented by the notation $M \rightarrow \infty$. We also define

$$
c:=\left(\sum_{\ell=1}^{L} \frac{1}{c_{\ell}}\right)^{-1}
$$

as well as

$$
\boldsymbol{\Gamma}:=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \boldsymbol{\Gamma}_{\ell}
$$

One can notice that $\Gamma$ is the the pooling of the low-rank covariance matrices $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}$ and has rank at most $K L$. In the following, we also need to ensure the convergence of the eigenvalues of matrices $\boldsymbol{\Gamma}_{\ell}, \boldsymbol{\Gamma}$ in the high-dimensional regime.

Assumption 2. For all $k \in\{1, \ldots, K\}, \ell \in\{1, \ldots, L\}$,

$$
\lambda_{k}\left(\boldsymbol{\Gamma}_{\ell}\right)=\gamma_{k, \ell}+o\left(\frac{1}{\sqrt{M}}\right)
$$

and for all $k \in\{1, \ldots, K L\}$,

$$
\lambda_{k}(\boldsymbol{\Gamma})=\gamma_{k}+o\left(\frac{1}{\sqrt{M}}\right)
$$

We note that Assumption 2 is a purely technical assumption which is not restrictive in practice as the corresponding results derived from it are meant to be used for fixed values of $M, N, K$.

Under Assumptions 1 and 2, the global behaviour of the eigenvalues of $\hat{\mathbf{R}}$ can be described through its empirical spectral distribution defined as the random probability measure

$$
\hat{\mu}=\frac{1}{M} \sum_{k=1}^{M} \delta_{\lambda_{k}(\hat{\mathbf{R}})}
$$

where $\delta_{x}$ is the Dirac measure centered at $x$. Under the model (6), each covariance matrix $\mathbf{R}_{1}, \ldots, \mathbf{R}_{L}$ is a fixed rank $K$ perturbation of the matrix $\sigma^{2} \mathbf{I}$ and it can be shown using standard perturbations arguments that $\hat{\mu}$ asymptotically behaves as the Marcenko-Pastur distribution, i.e. $\hat{\mu}$ converges weakly almost surely (a.s.) to the probability measure:

$$
\begin{aligned}
\mu(\mathrm{d} x)= & \frac{\sqrt{\left(x-x^{-}\right)\left(x^{+}-x\right)}}{2 \pi \sigma^{2} c x} \mathbb{1}_{\left[x^{-}, x^{+}\right]}(x) \mathrm{d} x \\
& +\left(1-\frac{1}{c}\right)^{+} \delta_{0}(\mathrm{~d} x)
\end{aligned}
$$

where $x^{ \pm}=\sigma^{2}(1 \pm \sqrt{c})^{2}$. Consequently, any functional of the type

$$
\hat{\mu}(\varphi):=\frac{1}{M} \sum_{k=1}^{M} \varphi\left(\lambda_{k}(\hat{\mathbf{R}})\right)
$$

where $\varphi$ is a bounded continuous function, satisfies

$$
\hat{\mu}(\varphi)=\int_{\mathbb{R}} \varphi(\lambda) \mathrm{d} \hat{\mu}(\lambda) \xrightarrow[M \rightarrow \infty]{a . s .} \int_{\mathbb{R}} \varphi(\lambda) \mathrm{d} \mu(\lambda)
$$

As the limit in (17) only depends on $\sigma^{2}$ and $c$, it is not possible to recover information on the low-rank matrices $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}$ in the high-dimensional regime from statistics of type (16). However, under the previous assumptions, it can be shown that the information related to the spectrum of $\boldsymbol{\Gamma}$ can be found in the largest $K L$ eigenvalues of $\hat{\mathbf{R}}$, thanks to the following result.

Theorem 1. Under Assumptions 1 and $2 \forall k \in\{1, \ldots, K L\}$,

$$
\lambda_{k}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} \phi_{c}\left(\gamma_{k}, \sigma^{2}\right)
$$

with

$$
\phi_{c}\left(\gamma, \sigma^{2}\right):= \begin{cases}\frac{\left(\gamma+\sigma^{2}\right)\left(\gamma+\sigma^{2} c\right)}{\gamma} & \text { if } \gamma>\sigma^{2} \sqrt{c} \\ \sigma^{2}(1+\sqrt{c})^{2} & \text { if } \gamma \leq \sigma^{2} \sqrt{c}\end{cases}
$$

Moreover, $\lambda_{K L+1}(\hat{\mathbf{R}}) \rightarrow \sigma^{2}(1+\sqrt{c})^{2}$ a.s. when $M \rightarrow \infty$.

Proof. The proof of Theorem 1 is deferred to Appendix B

The matrix $\hat{\mathbf{R}}$ being a mixture of $L$ independent but not identically distributed Wishart matrices, we note that Theorem 1 provides an extension of the results of [21, Th. 2.7] (see also [26]) to the case $L>1$. It shows in particular that the largest eigenvalues of $\hat{\mathbf{R}}$ converge to some limits depending directly of the eigenvalues of $\boldsymbol{\Gamma}$, provided that for all $k \in$ $\{1, \ldots, K L\}$ the ratios $\frac{\gamma_{k}}{\sigma^{2}}$ are above $\sqrt{c}$. The threshold $\sqrt{c}$ can be interpreted as a minimal SNR above which the $k^{t h}$ largest signal related eigenvalues of $\hat{\mathbf{R}}$ splits from the largest noise related eigenvalue $\lambda_{K L+1}(\hat{\mathbf{R}})$.

The next result shows, under hypothesis $\mathcal{H}_{0}$, a joint Central Limit Theorem (CLT) on the largest eigenvalues of $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}, \hat{\mathbf{R}}$

Theorem 2. Let Assumptions 112 hold. Assume moreover that $\boldsymbol{\Gamma}_{1}=\ldots=\boldsymbol{\Gamma}_{L}$ (thus $\gamma_{k, \ell}=\gamma_{k}$ ) and that

$$
\gamma_{1}>\ldots>\gamma_{K}>\sigma^{2} \max \left\{\sqrt{c}, \sqrt{c}_{1}, \ldots, \sqrt{c}_{L}\right\}
$$

Then we have

$$
\begin{gathered}
\sqrt{M}\left(\begin{array}{c}
\lambda_{k}(\hat{\mathbf{R}})-\phi_{c}\left(\gamma_{k}, \sigma^{2}\right) \\
\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\phi_{c_{\ell}}\left(\gamma_{k}, \sigma^{2}\right)\right)_{\ell=1, \ldots, L}
\end{array}\right)_{k=1, \ldots, K} \underset{M \rightarrow \infty}{\mathcal{D}} \mathcal{N}_{\mathbb{R}^{K(L+1)}}(\mathbf{0}, \boldsymbol{\Theta})
\end{gathered}
$$

where $\Theta$ is a positive definite block diagonal matrix given by $\boldsymbol{\Theta}=\operatorname{bdiag}\left(\boldsymbol{\Theta}_{1}, \ldots, \boldsymbol{\Theta}_{K}\right)$ with

$$
\boldsymbol{\Theta}_{k}:=\left(\begin{array}{cccc}
\theta_{k, 0}^{2} & \vartheta_{k, 1} & \ldots & \vartheta_{k, L} \\
\vartheta_{k, 1} & \ddots & (0) & \\
\vdots & (0) & \ddots & \\
\vartheta_{k, L} & & & \theta_{k, L}^{2}
\end{array}\right)
$$

and by denoting $c_{0}=c$,

$$
\theta_{k, \ell}^{2}=c_{\ell} \frac{\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)\left(\gamma_{k}+\sigma^{2}\right)^{2}}{\gamma_{k}^{2}}, \quad \ell \geq 0
$$

$$
\vartheta_{k, \ell}=c_{0} \frac{\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)\left(\gamma_{k}+\sigma^{2}\right)^{2}}{\gamma_{k}^{2}}, \quad \ell \geq 1
$$

Proof. The proof is postponed to Appendix C

The result of Theorem 2 provides an extension of [20, Th. 1.4] which studies a CLT for the $K$ largest eigenvalues of $\hat{\mathbf{R}}_{\ell}$. We note that the result of Theorem 2 cannot be inferred directly from [20, Th. 1.4] and requires a careful study due to the strong dependency between the eigenvalues of $\hat{\mathbf{R}}$ and the ones of $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$.

Theorems 1 and 2 are exploited in the following section to build a new statistic for the test (2), relevant for the low-rank model (6).

## III. Proposed test statistic

Before introducing our new test statistic, we first notice that the test (2) can be reformulated as:

$$
\begin{aligned}
& \mathcal{H}_{0}: \quad \boldsymbol{\Gamma}_{1}=\ldots=\boldsymbol{\Gamma}_{L} \\
& \mathcal{H}_{1}: \quad \exists(i, j) \in\{1, \ldots, L\}^{2} \text { s.t. } \boldsymbol{\Gamma}_{i} \neq \boldsymbol{\Gamma}_{j}
\end{aligned}
$$

and we assume in the following that the rank $K$ is known (see also Remark 1 below in case the rank is unknown). Next, we consider the following lemma, which shows that hypothesis $\mathcal{H}_{0}$ can be verified by comparing the eigenvalues of matrix $\Gamma$ with the ones of matrices $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}$.

Lemma 1. The following assertions are equivalent:

(a) $\boldsymbol{\Gamma}_{1}=\ldots=\boldsymbol{\Gamma}_{L}$,

(b) For all $k=1, \ldots, K, \ell=1, \ldots, L, \lambda_{k}\left(\boldsymbol{\Gamma}_{\ell}\right)=\lambda_{k}(\boldsymbol{\Gamma})$.

Proof. The proof of Lemma 1 can be found in [1].

From Lemma 1, one can equivalently formulate the test 25 as follows

$$
\begin{array}{ll}
\mathcal{H}_{0}: & \forall k, \ell, \lambda_{k}\left(\boldsymbol{\Gamma}_{\ell}\right)=\lambda_{k}(\boldsymbol{\Gamma}) \\
\mathcal{H}_{1}: \quad \exists k, \ell: \lambda_{k}\left(\boldsymbol{\Gamma}_{\ell}\right) \neq \lambda_{k}(\boldsymbol{\Gamma})
\end{array}
$$

Consequently, it is possible to discriminate between hypotheses $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$ by exploiting only the eigenvalues of the matrices $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}, \boldsymbol{\Gamma}$ for which we can also build consistent estimators in the high-dimensional regime as follows. Let us consider first the maximum likelihood estimator of the noise variance $\sigma^{2}$ given by

$$
\hat{\sigma}^{2}:=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \frac{1}{M-K} \sum_{k=K+1}^{M} \lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)
$$

From (6) and Theorem 1, one can easily show that $\hat{\sigma}^{2} \rightarrow \sigma^{2}$ a.s. as $M \rightarrow+\infty$ under both $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$. Next, for all $k \in\{1, \ldots, K L\}$, let $\hat{\gamma}_{k}$ be the largest solution to the equation $\phi_{c}\left(\gamma_{k}, \hat{\sigma}^{2}\right)=\lambda_{k}(\hat{\mathbf{R}})$ if $\lambda_{k}(\hat{\mathbf{R}})>\hat{\sigma}^{2}(1+\sqrt{c})^{2}$, or $\hat{\gamma}_{k}=\hat{\sigma}^{2} \sqrt{c}$ otherwise. Similarly, for all $k \in\{1, \ldots, K\}$, let $\hat{\gamma}_{k, \ell}$ be the largest solution to the equation $\phi_{c_{\ell}}\left(\gamma_{k, \ell}, \hat{\sigma}^{2}\right)=\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)$ if $\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)>\hat{\sigma}^{2}\left(1+\sqrt{c_{\ell}}\right)^{2}$, or $\hat{\gamma}_{k, \ell}=\hat{\sigma}^{2} \sqrt{c_{\ell}}$ otherwise. Then we have the following immediate result, as a consequence of Theorem 1 .

Corollary 1. Under Assumptions 1 and 2 ,

$$
\hat{\gamma}_{k} \xrightarrow[M \rightarrow \infty]{a . s .} \begin{cases}\gamma_{k} & \text { if } \gamma_{k}>\sigma^{2} \sqrt{c} \\ \sigma^{2} \sqrt{c} & \text { otherwise }\end{cases}
$$

$$
\hat{\gamma}_{k, \ell} \underset{M \rightarrow \infty}{\text { a.s. }} \begin{cases}\gamma_{k, \ell} & \text { if } \gamma_{k, \ell}>\sigma^{2} \sqrt{c_{\ell}} \\ \sigma^{2} \sqrt{c_{\ell}} & \text { otherwise }\end{cases}
$$

Considering this result we propose the following test statistic

$$
T(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(\|\hat{\gamma}\|_{2}^{2}\right)
$$

where

$$
\hat{\gamma}=\left(\hat{\gamma}_{k}-\hat{\gamma}_{k, \ell}\right)_{\substack{k=1, \ldots, K \\ \ell=1, \ldots, L}}
$$

To study the performance in terms of consistency and asymptotic type I error of the test statistic (30), we consider the following assumption which ensures that the signal and noise eigenvalues of matrices $\hat{\mathbf{R}}, \hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$ are separated in the high-dimensional regime.

Assumption 3. For all $k \in\{1, \ldots, K\}$ and $\ell \in\{1, \ldots, L\}$,

$$
\begin{aligned}
\gamma_{1, \ell} & >\ldots>\gamma_{K, \ell}>\sigma^{2} \max \left\{\sqrt{c_{1}}, \ldots, \sqrt{c_{L}}\right\} \\
\gamma_{1} & >\ldots>\gamma_{K}>\sigma^{2} \sqrt{c}
\end{aligned}
$$

Moreover, under $\mathcal{H}_{1}$, there exist $k, \ell$ such that $\gamma_{k} \neq \gamma_{k, \ell}$.

As a consequence of Corollary 1, we have under Assumptions 1.3

$$
\|\hat{\gamma}\|_{2}^{2} \xrightarrow[M \rightarrow \infty]{\text { a.s. }}\|\gamma\|_{2}^{2}
$$

with

$$
\gamma=\left(\gamma_{k}-\gamma_{k, l}\right)_{\substack{k=1, \ldots, K \\ \ell=1, \ldots, L}}
$$

such that $\gamma=\mathbf{0}$ under $\mathcal{H}_{0}$ and $\boldsymbol{\gamma} \neq \mathbf{0}$ under $\mathcal{H}_{1}$. This implies the following consistency result.

Theorem 3. Let Assumptions 13 hold and denote $\epsilon_{1}=$ $\|\gamma\|_{2}^{2}>0$ under $\mathcal{H}_{1}$. Then for all $\epsilon \in\left(0, \epsilon_{1}\right)$,

$$
\mathbb{P}_{i}\left(\lim _{M \rightarrow \infty} T(\epsilon)=i\right)=1
$$

for $i \in\{0,1\}$, where $\mathbb{P}_{i}$ is the probability measure under hypothesis $\mathcal{H}_{i}$.

To control the asymptotic type I error of the proposed test statistic (30), we also need the following result which, as a consequence of Theorem 2, provides a CLT for (31).

Corollary 2. Under hypothesis $\mathcal{H}_{0}$ and Assumptions $7 \mid 3$ we have

$$
\sqrt{M} \hat{\boldsymbol{\gamma}} \underset{M \rightarrow \infty}{\mathcal{D}} \mathcal{N}_{\mathbb{R}^{K L}}\left(\mathbf{0}, \mathbf{H} \Upsilon \mathbf{H}^{T}\right)
$$

where $\mathbf{H}$ is the $K L \times K(L+1)$ matrix defined by $\mathbf{H}=$ $\operatorname{bdiag}(\tilde{\mathbf{H}}, \ldots, \tilde{\mathbf{H}}), \boldsymbol{\Upsilon}=\operatorname{bdiag}\left(\boldsymbol{\Upsilon}_{1}, \ldots, \boldsymbol{\Upsilon}_{K}\right)$ with $\tilde{\mathbf{H}}$ the $L \times(L+1)$ matrix given by

$$
\tilde{\mathbf{H}}=\left(\begin{array}{cccccc}
1 & -1 & 0 & \ldots & \ldots & 0 \\
1 & 0 & -1 & \ddots & & \vdots \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots \\
\vdots & \vdots & & \ddots & \ddots & 0 \\
1 & 0 & \ldots & \ldots & 0 & -1
\end{array}\right)
$$

and with

$$
\mathbf{\Upsilon}_{k}=\left(\begin{array}{cccc}
\omega_{k, 0}^{2} & \xi_{k} & \ldots & \xi_{k} \\
\xi_{k} & \ddots & (0) & \\
\vdots & (0) & \ddots & \\
\xi_{k} & & & \omega_{k, L}^{2}
\end{array}\right)
$$

where

$$
\begin{aligned}
\omega_{k, \ell}^{2} & =\frac{c_{\ell} \gamma_{k}^{2}\left(\gamma_{k}+\sigma^{2}\right)^{2}}{\gamma_{k}^{2}-\sigma^{4} c_{\ell}}, \quad \ell=0, \ldots, L \\
\xi_{k} & =\frac{c_{0} \gamma_{k}^{2}\left(\gamma_{k}+\sigma^{2}\right)^{2}}{\gamma_{k}^{2}-\sigma^{4} c_{0}}
\end{aligned}
$$

Proof. The proof is deferred to Appendix D

From Corollary 2, we can adjust the threshold $\epsilon$ in (30) to control the asymptotic type I error in the high-dimensional regime, as described in the next result. Let us define $\hat{\boldsymbol{\Upsilon}}=$ $\operatorname{bdiag}\left(\hat{\boldsymbol{\Upsilon}}_{1}, \ldots, \hat{\boldsymbol{\Upsilon}}_{K}\right)$ with

$$
\hat{\boldsymbol{\Upsilon}}_{k}=\left(\begin{array}{cccc}
\hat{\omega}_{k, 0}^{2} & \hat{\xi}_{k} & \ldots & \hat{\xi}_{k} \\
\hat{\xi}_{k} & \ddots & (0) & \\
\vdots & (0) & \ddots & \\
\hat{\xi}_{k} & & & \hat{\omega}_{k, L}^{2}
\end{array}\right)
$$

where

$$
\begin{aligned}
\hat{\omega}_{k, \ell}^{2} & =\frac{c_{\ell} \hat{\gamma}_{k}^{2}\left(\hat{\gamma}_{k}+\hat{\sigma}^{2}\right)^{2}}{\hat{\gamma}_{k}^{2}-\hat{\sigma}^{4} c_{\ell}}, \quad \ell \geq 0 \\
\hat{\xi}_{k} & =\frac{c_{0} \hat{\gamma}_{k}^{2}\left(\hat{\gamma}_{k}+\hat{\sigma}^{2}\right)^{2}}{\hat{\gamma}_{k}^{2}-\hat{\sigma}^{4} c_{0}}
\end{aligned}
$$

From Corollary 1, it is clear that $\hat{\Upsilon} \rightarrow \mathbf{\Upsilon}$ a.s. as $M \rightarrow \infty$.

Theorem 4. Let $\mathbf{x} \in \mathcal{N}_{\mathbb{R}^{K L}}(\mathbf{0}, \mathbf{I})$ and $F(t, \boldsymbol{\Xi})=$ $\mathbb{P}\left(\mathbf{x}^{T} \boldsymbol{\Xi} \mathbf{x} \leq t\right), \alpha \in(0,1)$ and set

$$
\hat{\epsilon}=\frac{1}{M} \inf \left\{t \in \mathbb{R}: F\left(t, \mathbf{H} \hat{\boldsymbol{\Upsilon}} \mathbf{H}^{T}\right) \geq 1-\alpha\right\}
$$

Then under Assumptions 1 and 3, we have

$$
\mathbb{P}_{0}(T(\hat{\epsilon})=1) \underset{M \rightarrow \infty}{ } \alpha
$$

In practice, Theorem 4 is used as follows. For a fixed realization of $\hat{\Upsilon}$, we sample the distribution of the Gaussian quadratic form $\mathbf{x}^{T} \mathbf{H} \hat{\mathbf{Y}} \mathbf{H}^{T} \mathbf{x}$ and the threshold $\hat{\epsilon}$ is then set as the $(1-\alpha)$-quantile of $\mathbf{x}^{T} \mathbf{H} \hat{\mathbf{Y}} \mathbf{H}^{T} \mathbf{x}$.

Remark 1. For a more general approach where each $\boldsymbol{\Gamma}_{\ell}$ has unknown rank $K_{\ell}$, one can obtain consistent estimates of $K_{1}, \ldots, K_{L}$ thanks to Theorem 1 Assuming $K_{1}, \ldots, K_{L}$ fixed with respect to $M$, and if for $\ell \in\{1, \ldots, L\}, \gamma_{K_{\ell}, \ell}>\sigma^{2} \sqrt{c}_{\ell}$, under Assumption 2 the quantity

$$
\hat{K}_{\ell}=\max \left\{k: \lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)>\sigma^{2}\left(1+\sqrt{c}_{\ell}\right)^{2}+\epsilon_{\ell}\right\}
$$

converges almost surely to $K_{\ell}$ in the high-dimensional regime, for all $\epsilon_{\ell} \in\left(0, \phi_{c_{\ell}}\left(\gamma_{K_{\ell}, \ell}, \sigma^{2}\right)-\sigma^{2}\left(1+\sqrt{c_{\ell}}\right)^{2}\right)$. This shows that we can build consistent test statistics to capture changes in the rank (see further [27]).
Remark 2. It is easy to show that under Assumption 33 the matrix $\mathbf{H} \Upsilon \mathbf{H}^{T}$ is non singular. Therefore, an alternative approach to obtain a test statistic with controlled asymptotic type I error would be to consider the statistic

$$
\tilde{T}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(M\left\|\left(\mathbf{H} \hat{\Upsilon} \mathbf{H}^{T}\right)^{-\frac{1}{2}} \hat{\gamma}\right\|_{2}^{2}\right)
$$

since from Corollary 2 we have

$$
M\left\|\left(\mathbf{H} \hat{\Upsilon} \mathbf{H}^{T}\right)^{-\frac{1}{2}} \hat{\boldsymbol{\gamma}}\right\|_{2}^{2} \xrightarrow[M \rightarrow \infty]{\mathcal{D}} \chi^{2}(K L)
$$

Nevertheless, although this approach looks simpler, it appears that the covariance matrix $\mathbf{H} \Upsilon \mathbf{H}^{T}$ is ill-conditioned. This can be readily seen, e.g. in the special case where $c_{1}=\ldots=c_{L}$ and for a large SNR. If $\kappa\left(\Upsilon_{k}\right)$ denotes the condition number of $\Upsilon_{k}$ defined in (39), then we can verify (details are omitted) that $\kappa\left(\Upsilon_{k}\right)$ scales with $\gamma^{2}$ as $\gamma^{2} \rightarrow \infty$. Therefore, in practice, setting the threshold $\epsilon$ based on the $\chi^{2}(K L)$ distribution gives poor performance.

## IV. SOME COMPARISONS WITH ALTERNATIVE METHODS

In this section, we compare the test statistic given in 30 , with two relevant alternatives for the low-rank model 6) and the high-dimensional regime described in Assumption 1. To that purpose, we consider scenarios involving a change of subspace/eigenvalues for the rank $K=1$ model $\boldsymbol{\Gamma}_{\ell}=\gamma_{1, \ell} \mathbf{u}_{\ell} \mathbf{u}_{\ell}^{*}$, where $\left\|\mathbf{u}_{\ell}\right\|_{2}=1$, and where $\gamma_{1, \ell}$ is independent of $M$. We precise that our objective is not to provide an exhaustive analysis of all the possible scenarios under $\mathcal{H}_{1}$, but to draw some performance comparisons, in terms of consistency, out of a few simple cases. In the remainder of this section, we also assume that $L=2$ and $N_{1}=N_{2}$ so that $c_{1}=c_{2}=2 c$.

## A. A test based on spiked Fisher matrices

Although test statistics of the form (3) are not consistent in the high-dimensional regime, we can build consistent test statistics by exploiting the behaviour of the largest and smallest eigenvalues of the Fisher matrices $\hat{\mathbf{R}}_{2}^{-1} \hat{\mathbf{R}}_{1}$ (see [17]). We propose 1 to use $T_{\text {Fisher }}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}(F)$ with

$$
\begin{aligned}
F=\sum_{\substack{\ell, \ell^{\prime}=1 \\
\ell^{\prime} \neq \ell}}^{L} \sum_{k=1}^{K}[ & \left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}_{\ell^{\prime}}\right)-\nu_{\ell, \ell^{\prime}}^{+}\right)^{+} \\
& \left.+\left(\nu_{\ell, \ell^{\prime}}^{-}-\lambda_{M-k}\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}_{\ell^{\prime}}\right)\right)^{+}\right]
\end{aligned}
$$

where $\nu_{\ell, \ell^{\prime}}^{ \pm}=\left(\frac{1 \pm \sqrt{c_{\ell}+c_{\ell^{\prime}}-c_{\ell} c_{\ell^{\prime}}}}{1-c_{\ell}}\right)^{2}$.

Change of subspace. Let us consider that under $\mathcal{H}_{1}, \gamma_{1,1}=$ $\gamma_{1,2}$ and $\mathbf{u}_{1}^{*} \mathbf{u}_{2} \rightarrow 0$ as $M \rightarrow \infty$, so that the changes between[^0]$\boldsymbol{\Gamma}_{1}$ and $\boldsymbol{\Gamma}_{2}$ are only carried by the unit norm eigenvector $\mathbf{u}_{2}$. It is easily seen that

$$
\lambda_{k}\left(\mathbf{R}_{2}^{-1} \mathbf{R}_{1}\right) \xrightarrow[M \rightarrow \infty]{\longrightarrow} \begin{cases}\frac{\gamma_{1,1}+\sigma^{2}}{\sigma^{2}} & \text { if } k=1 \\ 1 & \text { if } k=2, \ldots, M-1 \\ \frac{\sigma^{2}}{\gamma_{1,1}+\sigma^{2}} & \text { if } k=M\end{cases}
$$

so that applying [17, Th. 3.1] shows that for all small $\epsilon>0$, $\mathbb{P}_{i}\left(\lim T_{\text {Fisher }}(\epsilon)=i\right)=1$ for $i \in\{0,1\}$ as $M \rightarrow \infty$ iff

$$
\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2\left(c+\sqrt{c-c^{2}}\right)}{1-2 c}
$$

One can see that $\beta>\sqrt{2 c}$ and therefore, from Assumption 3 and Theorem 3 , we deduce that the Fisher based statistic requires a larger SNR $\frac{\gamma_{1,1}}{\sigma^{2}}$ compared to the Wishart based statistic proposed in (30) to be consistent in the change of subspace scenario.

Change of eigenvalues. In that case, we assume that $\gamma_{1,2}=$ $\gamma_{1,1}(1+\delta)$ with $\delta>0$ and $\mathbf{u}_{1}=\mathbf{u}_{2}$, so that the changes are only carried by the largest eigenvalue of $\boldsymbol{\Gamma}_{2}$. Note that under these settings, Assumption 2 is verified and it holds that

$$
\lambda_{k}\left(\mathbf{R}_{2}^{-1} \mathbf{R}_{1}\right) \underset{M \rightarrow \infty}{\longrightarrow} \begin{cases}\frac{\gamma_{1,1}+\sigma^{2}}{\gamma_{1,1}(1+\delta)+\sigma^{2}} & \text { if } k=1 \\ 1 & \text { if } k=2, \ldots, M\end{cases}
$$

Using again [17, Th. 3.1], we have that for all small $\epsilon>0$, $\mathbb{P}\left(\lim T_{\text {Fisher }}(\epsilon)=i\right)=1$ for $i \in 0,1$ as $M \rightarrow \infty$ iff

$$
\delta>\frac{2\left(c+\sqrt{c-c^{2}}\right)}{1-2 c}
$$

and

$$
\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2\left(c+\sqrt{c-c^{2}}\right)}{(1+\delta)(1-2 c)-\left(1+2 \sqrt{c-c^{2}}\right)}
$$

In this scenario, one can see that the minimal SNR $\beta$ decreases when $\delta$ increases, which can be exploited to produce conditions where the Fisher test statistic is consistent while the Wishart one is not. Indeed, choose $\sqrt{c}<\frac{\gamma_{1,1}}{\sigma^{2}}<\sqrt{2 c}$ and $\delta$ large enough so that (52) and (53) are verified. Then it can be seen from Corollary 1 that $\|\hat{\gamma}\|_{2}^{2} \rightarrow 2\left(\gamma_{1,1}-\sigma^{2} \sqrt{2 c}\right)^{2}$ a.s. as $M \rightarrow \infty$ and therefore for all small $\epsilon>0$, $\mathbb{P}_{0}(\lim T(\epsilon)=1)=1$.

## B. The GLR for (25)

As an alternative to the GLR for the general covariance equality test (2), the GLR for the low-rank test (25) can be derived. Classical computations (details are omitted) provide the following test statistic $T_{\mathrm{GLR}-\mathrm{LR}}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}(G)$ where

$$
\begin{aligned}
& G=-\sum_{\ell=1}^{L} N_{\ell} \sum_{k=1}^{K} \log \left(\frac{\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)}{\lambda_{k}(\hat{\mathbf{R}})}\right) \\
& -N(M-K) \log \left(\frac{\frac{1}{M-K} \sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \sum_{k=K+1}^{M} \lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)}{\frac{1}{M-K} \sum_{k=K+1}^{M} \lambda_{k}(\hat{\mathbf{R}})}\right)
\end{aligned}
$$

Using Theorem 1, it can be shown that $G \rightarrow G_{\infty}$ a.s. as $M \rightarrow \infty$ where

$$
G_{\infty}=\sum_{\ell=1}^{L} \frac{c}{c_{\ell}} \sum_{k=1}^{K}\left(\psi\left(\frac{\phi_{c}\left(\gamma_{k}\right)}{\sigma^{2}}\right)-\psi\left(\frac{\phi_{c_{\ell}}\left(\gamma_{k, \ell}\right)}{\sigma^{2}}\right)\right)
$$

with $\psi(x)=x-\log (x)$.

Let us consider a change of eigenvalues with $\gamma_{1,2}=\gamma_{1,1}+\delta$ and $\mathbf{u}_{1}=\mathbf{u}_{2}$ under $\mathcal{H}_{1}$. Then it is easy to see that under both $\mathcal{H}_{0}$ and $\mathcal{H}_{1}, G_{\infty}=-c+\mathcal{O}\left(\frac{1}{\gamma_{1,1}}\right)$ as $\gamma_{1,1} \rightarrow+\infty$. Regarding the proposed test (30), we have $\|\gamma\|_{2}^{2}=\frac{\delta^{2}}{2}$ under $\mathcal{H}_{1}$ which shows the limit (34) under $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$ cannot be made arbitrarily close as $\gamma_{1,1} \rightarrow \infty$. This suggests that for a large $\gamma_{1,1}$ and a fixed change $\delta$, the GLR for the low-rank model might experience a performance loss compared to the test 30 .

## V. Simulations

In this section, we provide simulations to illustrate the performance of the test statistic $T$ proposed in (30), and to perform some comparisons with the alternative test statistics introduced in Section IV We consider $\sigma^{2}=0.5, K=2, L=$ 2 as well as a Toeplitz model of rank $K=2$ for the covariance matrix $\Gamma_{\ell}$ which can therefore be written as

$$
\boldsymbol{\Gamma}_{\ell}=\gamma_{1, \ell} \mathbf{a}\left(\theta_{1, \ell}\right) \mathbf{a}^{*}\left(\theta_{1, \ell}\right)+\gamma_{2, \ell} \mathbf{a}\left(\theta_{2, \ell}\right) \mathbf{a}^{*}\left(\theta_{2, \ell}\right)
$$

with $\mathbf{a}(\theta)=\frac{1}{\sqrt{M}}\left(1, \mathrm{e}^{\mathrm{i} \theta} \ldots, \mathrm{e}^{\mathrm{i}(M-1) \theta}\right)^{T}$. Note that the model (56) is common in spectral analysis and array processing [28].

## A. Empirical and asymptotic Type I error of $T(\epsilon)$

We first illustrate the result of Theorem 4 and consider $\theta_{k, \ell}=0$ for $(k, \ell) \in\{1,2\}^{2}, \gamma_{1, \ell}=3$ and $\gamma_{2, \ell}=1.5$ for $\ell \in\{1,2\}$ and $N_{1}=N_{2}=2 M$. The threshold $\epsilon$ of 30 is set as the $(1-\alpha)$-quantile of the Gaussian quadratic form $\mathbf{x}^{T} \mathbf{H} \hat{\mathbf{Y}} \mathbf{H}^{T} \mathbf{x}$ with $\mathbf{x} \sim \mathcal{N}_{\mathbb{R} K L}(\mathbf{0}, \mathbf{I})$, and we provide in TABLE I the empirical Type I error of $T(\epsilon)$ (evaluated over 100000 iterations) for $M \in\{10,20,50,100\}$. Table $\square$ thus shows that

TABLE I

TYPE I ERROR OF $T(\epsilon)$

| $T(\epsilon)$ | 0.005 | 0.01 | 0.02 | 0.05 | 0.10 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $M=10$ | 0.002 | 0.004 | 0.009 | 0.028 | 0.065 |
| $M=20$ | 0.0025 | 0.005 | 0.01 | 0.03 | 0.073 |
| $M=50$ | 0.003 | 0.006 | 0.013 | 0.038 | 0.083 |
| $M=100$ | $\mathbf{0 . 0 0 4}$ | $\mathbf{0 . 0 0 8}$ | $\mathbf{0 . 0 1 6}$ | $\mathbf{0 . 0 4 3}$ | $\mathbf{0 . 0 9}$ |

the empirical type I error is close to the asymptotic type I error predicted in Theorem 4, when $M$ is increasing.

## B. Comparisons of powers

In this section, we evaluate the proposed test statistic on synthetic data by considering the following two scenarios.

(1) Change of subspace: under $\mathcal{H}_{0}, \theta_{1,1}=\theta_{1,2}=0, \theta_{2,1}=$ $\theta_{2,2}=\frac{\pi}{8}$ and under $\mathcal{H}_{1}, \theta_{1,1}=0, \theta_{1,2}=\frac{\pi}{2}, \theta_{2,1}=$ $\frac{\pi}{8}, \theta_{2,2}=\frac{\pi}{2}+\frac{\pi}{8}$. We will also consider under both
hypothesis $\gamma_{1,1}=\gamma_{1,2}=2, \gamma_{2,1}=\gamma_{2,2}=1$ and $N_{1}=$ $N_{2}=2 M$ thus $c_{1}=c_{2}$.

(2) Change of Eigenvalues: under $\mathcal{H}_{0}, \gamma_{1,1}=\gamma_{1,2}=2$, $\gamma_{2,1}=\gamma_{2,2}=1.5$ and under $\mathcal{H}_{1}, \gamma_{1,1}=2, \gamma_{1,2}=5$, $\gamma_{2,1}=1.5, \gamma_{2,2}=4$. We will also consider under both hypothesis $\theta_{1,1}=\theta_{1,2}=0, \theta_{2,1}=\theta_{2,2}=0$ and $N_{1}=$ $N_{2}=4 M$ thus $c_{1}=c_{2}$.

In the simulations that follow, for both scenarios, we compute the power of different test statistics for a given type I error $\alpha$ and different values of $M$. The statistic $T(\epsilon)$, which will be termed as "Wishart" below, will be compared to the statistics $T_{\text {Fisher }}(\epsilon)$ (termed as "Fisher"), $T_{G L R-L R}(\epsilon)$ (termed as "GLR-LR") and $T_{G L R}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(S_{\mid \varphi=\log }\right)$ where $S$ is given in (3) (termed as "GLR"). For each of the statistics, the threshold $\epsilon$ is adjusted separately to achieve a type I error of $\alpha$. Note that for both scenarios, Assumptions 2, 3 are verified and that the condition for the Fisher statistic to be consistent is verified as well. We observe that in both scenarios,

TABLE II

POWER FOR DIFFERENT VALUES OF $M$ (CHANGE OF EIGENVALUES SCENARIO)

| $\widehat{S t a t i s t i c s ~}^{\alpha} \alpha$ | 0.005 | 0.01 | 0.02 | 0.05 | 0.1 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\frac{1}{M}=10$ |  |  |  |  |  |
| GLR | 0.120 | 0.181 | 0.266 | 0.412 | 0.550 |
| GLR-LR | 0.381 | 0.483 | 0.588 | 0.734 | 0.832 |
| Fisher | 0.309 | 0.397 | 0.5 | 0.653 | 0.775 |
| Wishart | 0.998 | 0.999 | 0.999 | 1 | 1 |
| $M=20$ |  |  |  |  |  |
| GLR | 0.137 | 0.197 | 0.277 | 0.424 | 0.569 |
| GLR-LR | 0.736 | 0.808 | 0.87 | 0.934 | 0.967 |
| Fisher | 0.578 | 0.672 | 0.762 | 0.861 | 0.923 |
| Wishart | 1 | 1 | 1 | 1 | 1 |
| $M=50$ |  |  |  |  |  |
| $\overline{\text { GLR }}$ | 0.145 | 0.209 | 0.297 | 0.445 | 0.591 |
| GLR-LR | 0.992 | 0.996 | 1 | 1 | 1 |
| Fisher | 0.946 | 0.965 | 0.98 | 0.992 | 0.997 |
| Wishart | 1 | 1 | 1 | 1 | 1 |
| $M=100$ |  |  |  |  |  |
| GLR | 0.154 | 0.207 | 0.290 | 0.445 | 0.591 |
| GLR-LR | 1 | 1 | 1 | 1 | 1 |
| Fisher | 0.998 | 0.999 | 1 | 1 | 1 |
| Wishart | 1 | 1 | 1 | 1 | 1 |

the proposed Wishart statistic shows a significantly better performance as $M$ is increasing. Second, while the GLR-LR statistic outperforms the Wishart one for low dimensions $M$ in the change of subspace scenario, the Wishart statistic still demonstrates a higher power compared to the Fisher and GLR statistics for both scenarios.

The next simulation in Table IV shows the evolution of the power for different values of the noise variance in the change of eigenvalues scenario $(M=100)$. The same can be done for the change of subspace scenario in Table $\mathrm{V}$. We observe that the test statistics designed for a low-rank scenario (Wishart, Fisher, GLR-LR) outperform the GLR in general. Additionally, when the noise variance $\sigma^{2}$ becomes too large, the conditions on the SNR ensuring the consistency of these statistics (Assumption 3 and the conditions of [17]) are not met anymore, and one observes in that case a significant drop of the performance $\left(\sigma^{2}=5.5\right.$ in Table IV and $\sigma^{2}=2.5$ in
TABLE III

POWER FOR DIFFERENT VALUES OF $M$ (CHANGE OF SUBSPACE SCENARIO)

| ${ }_{\text {Statistics }} \alpha$ | 0.005 | 0.01 | 0.02 | 0.05 | 0.1 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $M=10$ |  |  |  |  |  |
| GLR | 0.493 | 0.592 | 0.701 | 0.826 | 0.906 |
| GLR-LR | 0.992 | 0.996 | 0.998 | 0.999 | 1 |
| Fisher | 0.149 | 0.215 | 0.312 | 0.473 | 0.624 |
| Wishart | 0.026 | 0.056 | 0.119 | 0.3 | 0.519 |
| $M=20$ |  |  |  |  |  |
| GLR | 0.757 | 0.829 | 0.89 | 0.949 | 0.978 |
| GLR-LR | 1 | 1 | $\mathbf{1}$ | $\mathbf{1}$ | 1 |
| Fisher | 0.398 | 0.493 | 0.597 | 0.739 | 0.84 |
| Wishart | 0.646 | 0.812 | 0.924 | 0.988 | 1 |
| $M=50$ |  |  |  |  |  |
| GLR | 0.832 | 0.883 | 0.927 | 0.968 | 0.987 |
| GLR-LR | 1 | 1 | 1 | 1 | 1 |
| Fisher | 0.783 | 0.846 | 0.894 | 0.944 | 0.972 |
| Wishart | $\mathbf{1}$ | 1 | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ |
| $M=100$ |  |  |  |  |  |
| GLR | 0.838 | 0.891 | 0.934 | 0.972 | 0.988 |
| GLR-LR | 1 | 1 | 1 | 1 | 1 |
| Fisher | 0.955 | 0.971 | 0.984 | 0.993 | 0.997 |
| Wishart | 1 | 1 | 1 | 1 | 1 |

TABLE IV

POWER FOR DIFFERENT VALUES OF $\sigma^{2}$ (CHANGE OF EIGENVALUES SCENARIO)

| ${ }_{\text {Statistics }} \alpha^{\alpha}$ | 0.005 | 0.01 | 0.02 | 0.05 | 0.1 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\sigma^{2}=0.75$ |  |  |  |  |  |
| GLR | 0.1 | 0.153 | 0.226 | 0.368 | 0.512 |
| GLR-LR | 0.999 | 1 | 1 | 1 | 1 |
| Fisher | 0.925 | 0.95 | 0.97 | 0.987 | 0.944 |
| Wishart | 1 | 1 | 1 | 1 | 1 |
| $\sigma^{2}=1$ |  |  |  |  |  |
| GLR | 0.079 | 0.121 | 0.185 | 0.310 | 0.448 |
| GLR-LR | 0.995 | 0.998 | 0.999 | 1 | 1 |
| Fisher | 0.662 | 0.736 | 0.809 | 0.89 | 0.938 |
| Wishart | 1 | 1 | 1 | $\overline{1}$ | $\overline{1}$ |
| $\sigma^{2}=5.5$ |  |  |  |  |  |
| GLR | 0.008 | 0.019 | 0.037 | 0.083 | 0.152 |
| GLR-LR | 0.029 | 0.045 | 0.07 | 0.13 | 0.207 |
| Fisher | 0.008 | 0.015 | 0.029 | 0.07 | 0.133 |
| Wishart | 0.315 | 0.409 | 0.498 | 0.649 | 0.762 |

Table V).

Remark 3. In view of the simulations results described in Tables [II] we observe that the proposed test statistic (30) performs poorly when the conditions described in Assumptions $1]$ and 3 are not met, i.e. when the dimension $M$ or the SNR are not large enough. Scenarios where the rank $K$ is also of the same order of magnitude than $M$, thus violating Assumption 1] will also invalidate Theorem 4 and the asymptotic type I error will be poorly controlled in that case.

## C. An application to change detection in SAR images

In this section, we evaluate the performance of the proposed test statistic on images drawn from the UAV-SAR dataset of NASA/JPL-Caltech (SanAnd_26524_03, Segment 4). We consider two scenes with respective sizes $2360 \times 600$ and $2300 \times 600$ pixels, which have been previously used in [4], [18], and which are formed of $L=2$ images acquired within a 5 years interval (see Figures 1 and 2). The azimuthal

TABLE V

POWER FOR DIFFERENT VALUES OF $\sigma^{2}$ (CHANGE OF SUBSPACE SCENARIO)

| Statistics | 0.005 | 0.01 | 0.02 | 0.05 | 0.1 |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\sigma^{2}=0.75$ |  |  |  |  |  |  |  |  |  |  |  |
| GLR |  |  |  |  |  |  | 0.4 | 0.496 | 0.602 | 0.749 | 0.849 |
| GLR-LR | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ |  |  |  |  |  |  |
| Fisher | 0.329 | 0.414 | 0.510 | 0.625 | 0.763 |  |  |  |  |  |  |
| Wishart | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ |  |  |  |  |  |  |
| $\sigma^{2}=1$ |  |  |  |  |  |  |  |  |  |  |  |
| GLR | 0.172 | 0.246 | 0.34 | 0.505 | 0.646 |  |  |  |  |  |  |
| GLR-LR | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ |  |  |  |  |  |  |
| Fisher | 0.077 | 0.119 | 0.18 | 0.297 | 0.424 |  |  |  |  |  |  |
| Wishart | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ | $\mathbf{1}$ |  |  |  |  |  |  |
| $\sigma^{2}=2.5$ |  |  |  |  |  |  |  |  |  |  |  |
| GLR | 0.017 | 0.031 | 0.057 | 0.120 | 0.209 |  |  |  |  |  |  |
| GLR-LR | $\mathbf{0 . 3 4 1}$ | $\mathbf{0 . 4 2 3}$ | $\mathbf{0 . 5 3 7}$ | $\mathbf{0 . 6 9 5}$ | $\mathbf{0 . 8 0 9}$ |  |  |  |  |  |  |
| Fisher | 0.007 | 0.015 | 0.03 | 0.068 | 0.129 |  |  |  |  |  |  |
| Wishart | 0.256 | 0.327 | 0.414 | 0.566 | 0.655 |  |  |  |  |  |  |



Fig. 1. Scene 1 (Pauli representation) at two different times and its ground truth

resolution is approximately $0.6 \mathrm{~m}$ while the distance resolution is $1.67 \mathrm{~m}$. The dimension of each pixel, which was initially of $M=3$, has been increased to $M=12$ using the wavelet decomposition technique of [29]. Local patches of sizes $5 \times 5$ centered around each pixel under test are used for estimation,


Fig. 2. Scene 2 (Pauli representation) at two different times and its ground truth



(a) Scene 1



(b) Scene 2
Fig. 3. Ratio $k \mapsto r(k)$ for both scenes



(a) Scene 1



(b) Scene 2
Fig. 4. ROC plots for the two scenes

that is $N_{1}=N_{2}=25$. In Figure 3, the ratio

$$
r(k)=\frac{\mathbb{E}\left[\sum_{i=1}^{k} \lambda_{i}\left(\hat{\mathbf{R}}_{1}\right)\right]}{\mathbb{E}\left[\operatorname{tr}\left(\hat{\mathbf{R}}_{1}\right)\right]}
$$

is plotted for both scenes, where the expectations are estimated by a sample mean over all the local patches. The rank $K$ is set to 5 in the following to reach a ratio of $r(K) \gtrsim 95 \%$. In Figure 4 are plotted the ROC curves for scenes 1 and 2, where we have compared the performance of the proposed test statistic (30), the GLR, the GLR-LR and the method of [18]. We observe some improvement of the proposed test statistic for type I errors greater than $15 \%$ for the scene 1 or greater than $5 \%$ for the scene 2 .

## VI. CONCLUSION

In this paper, the problem of covariance equality testing in low-rank Gaussian models has been studied. A new test statistic has been proposed, which is based on the asymptotic behaviour of the largest eigenvalues of certain Wishart matrices in the high-dimensional regime where the dimension of the observations and the number of samples both converge to infinity at the same rate. In particular, it is shown that the
proposed statistic has a controlled type I error in the highdimensional regime. Simulations on both synthetic and real datasets have demonstrated that the proposed test statistic is relevant compared to other alternative approaches.

## APPENDIX

Notations. Throughout this Appendix, we use the following notations. For a sequence of random matrices $\left(\mathbf{X}_{n}\right)_{n \geq 1}$, $\mathbf{X}_{n}=o_{\mathbb{P}}(1)$ denotes the convergence of $\left(\left\|\mathbf{X}_{n}\right\|_{2}\right)$ to 0 in probability, while $\mathbf{X}_{n}=\mathcal{O}_{\mathbb{P}}(1)$ denotes the tightness of $\left(\left\|\mathbf{X}_{n}\right\|_{2}\right)$, as $n \rightarrow \infty$, where $\|\cdot\|_{2}$ stands for the spectral norm. If $\mathbf{X}$ is a random matrix, we denote by $\mathbf{X}^{\circ}=\mathbf{X}-\mathbb{E}[\mathbf{X}]$. Finally, $\mathcal{C}^{1}(U)$ (resp. $\mathcal{C}_{c}^{\infty}(U)$ ) denotes the set of continuously differentiable functions (resp. infinitely differentiable functions with compact support) defined on an open set $U$.

## A. Useful results around the Marcenko-Pastur distribution

In this section, we provide well-known results on the Stieltjes transform

$$
m(z)=\int_{\mathbb{R}} \frac{\mathrm{d} \mu(\lambda)}{\lambda-z}, \quad z \in \mathbb{C} \backslash \mathbb{R}
$$

of the Marcenko-Pastur distribution $\mu$ with parameters $\left(\sigma^{2}, c\right)$ defined in (15), having the interval $\left[x^{-}, x^{+}\right]$as support with $x^{ \pm}=\sigma^{2}(1 \pm \sqrt{c})^{2}$, and which will be of constant use for the proofs of Theorems 1, 2 and Corollary 2 below.

We first recall that the limit $m(x)=\lim _{z \in \mathbb{C}^{+}, z \rightarrow x} m(z)$ exists for all $x \in \mathbb{R} \backslash\left\{x^{-}, x^{+}\right\}$, and that for all $z \in \mathbb{C} \backslash\left\{x^{-}, x^{+}\right\}$, $m(z)$ satisfies the equation:

$$
m(z)=\frac{1+\sigma^{2} c m(z)}{\sigma^{2}-z\left(1+\sigma^{2} c m(z)\right)}=\frac{w(z)}{z\left(\sigma^{2}-w(z)\right)}
$$

with

$$
w(z)=z\left(1+\sigma^{2} c m(z)\right)
$$

Moreover, $m$ is continuously differentiable on $\mathbb{R} \backslash\left\{0, x^{-}, x^{+}\right\}$. We now provide some results on the function $w$, which plays a central role in describing the behaviour of the largest eigenvalues of $\hat{\mathbf{R}}$. From (59), we observe that for all $z \in \mathbb{C} \backslash\left\{x^{-}, x^{+}\right\}$,

$$
\phi(w(z))=z
$$

where $\phi$ is defined as:

$$
\phi(w)=w\left(1-\frac{\sigma^{2} c}{\sigma^{2}-w}\right)
$$

Function $\phi$ is increasing on $\left(-\infty, w^{-}\right) \cup\left(w^{+}, \infty\right)$ and decreasing on $\left(w^{-}, \sigma^{2}\right) \cup\left(\sigma^{2}, w^{+}\right)$, with $w^{ \pm}=\sigma^{2}(1 \pm \sqrt{c})$ and $\phi\left(w^{ \pm}\right)=x^{ \pm}$.

Next, we consider the following lemma (see [30]) regarding $w$.

Lemma 2. For all $x \in \mathbb{R} \backslash\left\{x^{-}, x^{+}\right\}, w(x) \in \phi^{-1}(\{x\})$. Moreover, among the preimages of $x$ under $\phi$,

- if $x \in\left(x^{-}, x^{+}\right), w(x)$ is the unique one such that $\operatorname{Im}(w(x))>0$;
- if $x \in \mathbb{R} \backslash\left[x^{-}, x^{+}\right], w(x)$ is real and is the unique preimage such that $\phi^{\prime}(w(x))>0$.
Finally, $z \in \mathbb{C} \backslash \mathbb{R}$ implies that $w(z) \in \mathbb{C} \backslash \mathbb{R}$.

Let $\gamma \geq 0$. From Lemma 2, it is easily deduced that the equation $w(x)=\gamma+\sigma^{2}$ admits a solution iff $\gamma>\sigma^{2} \sqrt{c}$, and that the solution is unique and given by

$$
x=\phi\left(\gamma+\sigma^{2}\right)=\frac{\left(\gamma+\sigma^{2}\right)\left(\gamma+\sigma^{2} c\right)}{\gamma}
$$

Finally, we also have the following result giving various useful formulas. Define $\tilde{m}(z)=-\frac{1}{z\left(1+\sigma^{2} c m(z)\right)}$ and $\tau(z)=$ $z m(z) \tilde{m}(z)$.

Lemma 3. If $\gamma>\sigma^{2} \sqrt{c}$, then we have

$$
\begin{aligned}
m\left(\phi\left(\gamma+\sigma^{2}\right)\right) & =-\frac{1}{\gamma+\sigma^{2} c} \\
\tilde{m}\left(\phi\left(\gamma+\sigma^{2}\right)\right) & =-\frac{1}{\gamma+\sigma^{2}} \\
m^{\prime}\left(\phi\left(\gamma+\sigma^{2}\right)\right) & =\frac{\gamma^{2}}{\left(\gamma+\sigma^{2} c\right)^{2}\left(\gamma^{2}-\sigma^{4} c\right)} \\
\tilde{m}^{\prime}\left(\phi\left(\gamma+\sigma^{2}\right)\right) & =\frac{\gamma^{2}}{\left(\gamma+\sigma^{2}\right)^{2}\left(\gamma^{2}-\sigma^{4} c\right)} \\
\tau\left(\phi\left(\gamma+\sigma^{2}\right)\right) & =\frac{1}{\gamma} \\
\tau^{\prime}\left(\phi\left(\gamma+\sigma^{2}\right)\right) & =-\frac{1}{\gamma^{2}-\sigma^{4} c}
\end{aligned}
$$

## B. Proof of Theorem 1

This proof is based on techniques developed in [21].

1) Some notations: Denote by $\mathbf{e}_{1}, \ldots, \mathbf{e}_{N}$ the column vectors of the standard basis of $\mathbb{C}^{N}$, and let

$$
\mathbf{J}_{1}=\sum_{n=1}^{N_{1}} \mathbf{e}_{n} \mathbf{e}_{n}^{*}
$$

and for $\ell=2, \ldots, L$,

$$
\mathbf{J}_{\ell}=\sum_{n=N_{1}+\ldots+N_{\ell-1}+1}^{N_{1}+\ldots+N_{\ell}} \mathbf{e}_{n} \mathbf{e}_{n}^{*}
$$

We also consider the following eigendecomposition of $\Gamma_{\ell}$

$$
\boldsymbol{\Gamma}_{\ell}=\mathbf{U}_{\ell} \mathbf{D}_{\ell} \mathbf{U}_{\ell}^{*}
$$

with $\mathbf{U}_{\ell}$ a $M \times K$ isometric matrix and $\mathbf{D}_{\ell}=$ $\operatorname{diag}\left(\lambda_{1}\left(\boldsymbol{\Gamma}_{\ell}\right), \ldots, \lambda_{K}\left(\boldsymbol{\Gamma}_{\ell}\right)\right)$.

2) Linearization: Let $\mathbf{Y}$ be the $M \times N$ matrix given by $\mathbf{Y}=\left[\mathbf{y}_{1,1}, \ldots, \mathbf{y}_{N_{1}, 1}, \ldots, \mathbf{y}_{1, L}, \ldots, \mathbf{y}_{N_{L}, L}\right]$. Due to the Gaussian model, one can assume, without loss of generality, that

$$
\mathbf{Y}=\mathbf{\Omega} \mathbf{S}^{*}+\mathbf{W}
$$

where $\mathbf{W}$ is $M \times N$ matrix with i.i.d. $\mathcal{N}_{\mathbb{C}}\left(0, \sigma^{2}\right)$ entries and where $\boldsymbol{\Omega}=\left[\mathbf{U}_{1} \mathbf{D}_{1}^{\frac{1}{2}}, \ldots, \mathbf{U}_{L} \mathbf{D}_{L}^{\frac{1}{2}}\right]$ and $\mathbf{S}=\left[\mathbf{S}_{1}, \ldots, \mathbf{S}_{L}\right]$. with $\mathbf{S}_{\ell}=\mathbf{J}_{\ell} \mathbf{X}$ and $\mathbf{X}$ a $N \times K$ matrix with i.i.d. $\mathcal{N}_{\mathbb{C}}(0,1)$ entries and independent of $\mathbf{W}$. In particular, we have $\hat{\mathbf{R}}=\frac{1}{N} \mathbf{Y} \mathbf{Y}^{*}$, and $\mathbf{Y}$ is a fixed rank (at most $K L$ ) perturbation of $\mathbf{W}$ so that from Weyl's inequality and the classical results on the extreme eigenvalues of Wishart matrices (see e.g. [31]), it holds that

$$
\lambda_{M}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} x^{-}
$$

while a.s.

$$
\limsup _{M \rightarrow \infty} \lambda_{K L+1}(\hat{\mathbf{R}}) \leq \limsup _{M \rightarrow \infty} \lambda_{1}\left(\frac{1}{N} \mathbf{W} \mathbf{W}^{*}\right)=x^{+}
$$

To study the remaining eigenvalues of $\hat{\mathbf{R}}$, we use the linearization trick which consists in studying the following Hermitian block matrix

$$
\check{\mathbf{Y}}=\left[\begin{array}{cc}
\mathbf{0} & \frac{1}{\sqrt{N}} \mathbf{Y} \\
\frac{1}{\sqrt{N}} \mathbf{Y}^{*} & \mathbf{0}
\end{array}\right]
$$

for which it is well-known that [32, Th. 7.3.7]

$$
\operatorname{sp}(\check{\mathbf{Y}})=\left\{ \pm \sqrt{\lambda_{k}(\hat{\mathbf{R}})}\right\} \cup\{0\}
$$

3) Asymptotics for the characteristic polynomial of $\check{\mathbf{Y}}$ : Obviously, we have:

$$
\check{\mathbf{Y}}=\mathrm{BI}^{\mathbf{I}} \mathbf{B}^{*}+\check{\mathbf{W}}
$$

where $\mathbf{B}, \check{\mathbf{I}}$ and $\check{\mathbf{W}}$ are given by:

$$
\mathbf{B}=\left[\begin{array}{cc}
\boldsymbol{\Omega} & \mathbf{0} \\
\mathbf{0} & \frac{1}{\sqrt{N}} \mathbf{S}
\end{array}\right], \check{\mathbf{I}}=\left[\begin{array}{ll}
\mathbf{0} & \mathbf{I} \\
\mathbf{I} & \mathbf{0}
\end{array}\right], \check{\mathbf{W}}=\left[\begin{array}{cc}
\mathbf{0} & \frac{1}{\sqrt{N}} \mathbf{W} \\
\frac{1}{\sqrt{N}} \mathbf{W}^{*} & \mathbf{0}
\end{array}\right]
$$

Let $\epsilon>0$ and let $\mathcal{D}_{\epsilon}$ the $\epsilon$-neighborhood in $\mathbb{C}$ of the set $\mathcal{D}=$ $\left[x^{-}, x^{+}\right]$. Let $\mathcal{K}$ be a compact subset of $\mathbb{C} \backslash\left(\mathcal{D}_{\epsilon} \cup(-\infty, 0)\right)$. Then (see again [31]), with probability one for all large $M$,

$$
\operatorname{sp}(\check{\mathbf{W}}) \cap\{\sqrt{z}: z \in \mathcal{K}\}=\emptyset
$$

and the following factorization

$$
\operatorname{det}(\check{\mathbf{Y}}-\sqrt{z} \mathbf{I})=\operatorname{det}(\check{\mathbf{W}}-\sqrt{z} \mathbf{I}) \operatorname{det}(\check{\mathbf{I}}) \hat{P}(z)
$$

where

$$
\hat{P}(z)=\operatorname{det}(\check{\mathbf{I}}+\hat{\boldsymbol{\Xi}}(z))
$$

and $\hat{\boldsymbol{\Xi}}(z)=\mathbf{B}^{*}(\breve{\mathbf{W}}-\sqrt{z} \mathbf{I})^{-1} \mathbf{B}$, holds for all $z \in \mathcal{K}$. Then from the block matrix inversion formula, we have

$$
\hat{\boldsymbol{\Xi}}(z)=\left[\begin{array}{cc}
\sqrt{z} \boldsymbol{\Omega}^{*} \mathbf{Q}(z) \boldsymbol{\Omega} & \frac{1}{N} \boldsymbol{\Omega}^{*} \mathbf{Q}(z) \mathbf{W} \mathbf{S} \\
\frac{1}{N} \mathbf{S}^{*} \mathbf{W}^{*} \mathbf{Q}(z) \boldsymbol{\Omega} & \sqrt{z} \frac{1}{N} \mathbf{S}^{*} \tilde{\mathbf{Q}}(z) \mathbf{S}
\end{array}\right]
$$

where $\mathbf{Q}(z)$ and $\tilde{\mathbf{Q}}(z)$ are the resolvent matrices of $\frac{1}{N} \mathbf{W} \mathbf{W}^{*}$ and $\frac{1}{N} \mathbf{W}^{*} \mathbf{W}$ given by

$\mathbf{Q}(z)=\left(\frac{1}{N} \mathbf{W} \mathbf{W}^{*}-z \mathbf{I}\right)^{-1}, \tilde{\mathbf{Q}}(z)=\left(\frac{1}{N} \mathbf{W}^{*} \mathbf{W}-z \mathbf{I}\right)^{-1}$.

We then use the following result.

Proposition 1. We have

$$
\sup _{z \in \mathcal{K}}\left\|\boldsymbol{\Omega}^{*} \mathbf{Q}(z) \boldsymbol{\Omega}-m(z) \boldsymbol{\Omega}^{*} \boldsymbol{\Omega}\right\|_{2} \xrightarrow[M \rightarrow \infty]{\text { a.s. }} 0
$$

as well as

$$
\sup _{z \in \mathcal{K}}\left\|\frac{1}{N} \mathbf{S}_{k}^{*} \tilde{\mathbf{Q}}(z) \mathbf{S}_{\ell}+\frac{\delta_{k-\ell} \frac{N_{k}}{N}}{z\left(1+\sigma^{2} c m(z)\right)} \mathbf{I}\right\|_{2} \xrightarrow[M \rightarrow \infty]{\text { a.s. }} 0
$$

and

$$
\sup _{z \in \mathcal{K}}\left\|\frac{1}{N} \mathbf{S}_{k}^{*} \mathbf{W}^{*} \mathbf{Q}(z) \boldsymbol{\Omega}\right\|_{2} \xrightarrow[M \rightarrow \infty]{\stackrel{a . s .}{\longrightarrow}} 0
$$

Proof. Proposition 1 is obtained as a trivial modification of standard results in random matrix theory regarding quadratic forms of resolvents of standard Wishart matrices (see e.g. [33, Sec. 5.5]) and the proof is therefore omitted.

Using Proposition 1, we deduce that:

$$
\sup _{z \in \mathcal{K}}\|\hat{\boldsymbol{\Xi}}(z)-\boldsymbol{\Xi}(z)\|_{2} \xrightarrow[M \rightarrow \infty]{a . s .} 0
$$

where

$$
\boldsymbol{\Xi}(z)=\left[\begin{array}{cc}
\sqrt{z} m(z) \boldsymbol{\Omega}^{*} \boldsymbol{\Omega} & \mathbf{0} \\
\mathbf{0} & \mathbf{A}(z)
\end{array}\right]
$$

with $\mathbf{A}(z)$ the $K L \times K L$ block diagonal matrix given by

$$
\mathbf{A}(z)=-\frac{1}{\sqrt{z}\left(1+\sigma^{2} c m(z)\right)}\left[\begin{array}{lll}
\frac{N_{1}}{N} \mathbf{I} & & \\
& \ddots & \\
& & \frac{N_{L}}{N} \mathbf{I}
\end{array}\right]
$$

It is straightforward to check that

$$
\begin{aligned}
\operatorname{det}(\check{\mathbf{I}}+\boldsymbol{\Xi}(z)) & =\operatorname{det}\left(\sqrt{z} m(z) \boldsymbol{\Omega}^{*} \boldsymbol{\Omega} \mathbf{A}(z)-\mathbf{I}\right) \\
& =\operatorname{det}\left(-\frac{m(z)}{1+\sigma^{2} c m(z)} \boldsymbol{\Gamma}-\mathbf{I}\right)
\end{aligned}
$$

where $\Gamma$ is defined in (11). Consequently, from Assumption 2. one has

$$
\sup _{z \in \mathcal{K}}|\hat{P}(z)-P(z)| \underset{N \rightarrow \infty}{\text { a.s. }} 0
$$

where $P(z)=\prod_{k=1}^{K L}\left(-\frac{m(z)}{1+\sigma^{2} c m(z)} \gamma_{k}-1\right)$. Using the equation (59), one can rewrite $P(z)$ as $P(z)=$ $\prod_{k=1}^{K L}\left(\frac{\gamma_{k}}{w(z)-\sigma^{2}}-1\right)$, with $w$ defined in 60).

4) Spectrum of $\hat{\mathbf{R}}$ : Using Lemma 2 and the discussion below, we immediately obtain that the set of zeros of $P$ is given by

$$
\mathcal{Z}=\left\{\phi\left(\gamma_{k}+\sigma^{2}\right): k=1, \ldots, K L, \gamma_{k}>\sigma^{2} \sqrt{c}\right\}
$$

Moreover, Lemma 2 also implies that $P$ has no pole and thus $P$ is holomorphic on $\mathbb{C} \backslash\left[x^{-}, x^{+}\right]$.

Let $Q=|\mathcal{Z}|$ and denote by $x_{1}>\ldots>x_{Q}$ the elements of $\mathcal{Z}$. We also set $\epsilon>0$ small enough such that

$$
\mathcal{D}_{\epsilon} \cap \bigcap_{q=1}^{Q}\left[x_{q}-\epsilon, x_{q}+\epsilon\right]=\emptyset
$$

For all $q=1, \ldots, Q$, let $\mathcal{C}_{q}$ be a continuously differentiable simple closed curve intersecting the real axis only at the two points $x_{q} \pm \epsilon$ and enclosing $x_{q}$ so that $\mathcal{C}_{q}$ is a compact subset of $\mathbb{C} \backslash\left(\mathcal{D}_{\epsilon} \cup(-\infty, 0)\right)$. Applying (92) with $\mathcal{K}=\mathcal{C}_{q}$ provides that with probability one for all large $M$,

$$
|\hat{P}(z)-P(z)|<|P(z)|
$$

for all $z \in \mathcal{C}_{q}$, with both $\hat{P}$ and $P$ being holomorphic on any open set enclosed by $\mathcal{C}_{q}$. Thus, for all $q=1, \ldots, Q$, we deduce from Rouché's Theorem that $\hat{P}$ admits a unique zero in the interval $\left[x_{q}-\epsilon, x_{q}+\epsilon\right]$. With a similar reasoning, $\hat{P}$ does not have any zero in $\left(0, x^{-}-\epsilon\right) \cup\left(x_{1}+\epsilon, \infty\right)$ with probability
one for all large $M$. Therefore, getting back to (81) and since $\epsilon$ can be made arbitrarily small, it follows that

$$
\lambda_{k}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} \phi\left(\gamma_{k}+\sigma^{2}\right)=\frac{\left(\gamma_{k}+\sigma^{2}\right)\left(\gamma_{k}+\sigma^{2} c\right)}{\gamma_{k}}
$$

for all $k=1, \ldots, K L$ such that $\gamma_{k}>\sigma^{2} \sqrt{c}$. Moreover, with probability one for all large $M, \lambda_{k}(\hat{\mathbf{R}}) \in \mathcal{D}_{\epsilon}$ for all $k=1, \ldots, K L$ such that $\gamma_{k} \leq \sigma^{2} \sqrt{c}$. Since the empirical spectral distribution $\hat{\mu}$ of $\hat{\mathbf{R}}$ converges a.s. to the MarcenkoPastur distribution as $M \rightarrow \infty$, this further implies that for all $k=1, \ldots, K L$ such that $\gamma_{k} \leq \sigma^{2} \sqrt{c}, \lambda_{k}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} x^{+}$ and similarly $\lambda_{K L+1}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} x^{+}$.

## C. Proof of Theorem 2

1) Some notations.: Let us first recall that under hypothesis $\mathcal{H}_{0}$, we have $\Gamma_{1}=\ldots=\Gamma_{L}=\Gamma$, and we denote by $\boldsymbol{\Gamma}=$ UDU $^{*}$ its eigendecomposition with $\mathbf{U}$ a $M \times K$ isometric matrix and $\mathbf{D}=\operatorname{diag}\left(\lambda_{1}(\boldsymbol{\Gamma}), \ldots, \lambda_{K}(\boldsymbol{\Gamma})\right)$. To unify some notations, define as in the previous section $\mathbf{Y}_{\ell}=$ $\left[\mathbf{y}_{1, \ell}, \ldots, \mathbf{y}_{N_{\ell}, \ell}\right]$ for all $\ell=1, \ldots, L$ so that we have

$$
\mathbf{Y}_{\ell}=\mathbf{\Omega} \mathbf{S}_{\ell}^{*}+\mathbf{W}_{\ell}
$$

where $\boldsymbol{\Omega}=\mathbf{U D}^{1 / 2}, \mathbf{S}_{1}, \ldots, \mathbf{S}_{L}$ are independent matrices such that $\mathbf{S}_{\ell}=\left[\mathbf{s}_{1, \ell}, \ldots, \mathbf{s}_{K, \ell}\right]$ is $N_{\ell} \times K$ with i.i.d. $\mathcal{N}_{\mathbb{C}}(0,1)$ entries, and where $\mathbf{W}_{1}, \ldots, \mathbf{W}_{L}$ are independent matrices with $\mathbf{W}_{\ell}$ having i.i.d. $\mathcal{N}_{\mathbb{C}}\left(0, \sigma^{2}\right)$ entries. We also define $\mathbf{Y}_{0}=\left[\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{L}\right]$ so that

$$
\mathbf{Y}_{0}=\mathbf{\Omega} \mathbf{S}_{0}^{*}+\mathbf{W}_{0}
$$

with $\mathbf{S}_{0}=\left[\mathbf{S}_{1}^{*}, \ldots, \mathbf{S}_{L}^{*}\right]^{*}$ and $\mathbf{W}_{0}=\left[\mathbf{W}_{1}, \ldots, \mathbf{W}_{L}\right]$, and write $N_{0}=N_{1}+\ldots+N_{L}$, so that $\hat{\mathbf{R}}_{0}=\frac{\mathbf{Y}_{0} \mathbf{Y}_{0}^{*}}{N_{0}}=\hat{\mathbf{R}}$. Moreover, let $c_{0}=c=\left(\frac{1}{c_{1}}+\ldots+\frac{1}{c_{L}}\right)^{-1}$ and

$$
a=\sigma^{2} \min _{\ell=0, \ldots, L}\left(1-\sqrt{c_{\ell}}\right)^{2}, \quad b=\sigma^{2} \max _{\ell=0, \ldots, L}\left(1+\sqrt{c_{\ell}}\right)^{2}
$$

and consider $\varphi \in \mathcal{C}_{c}^{\infty}(\mathbb{R})$ such that $\operatorname{supp}(\varphi)=[a-\epsilon, b+\epsilon]$ and $\varphi(t)=1$ for all $t \in\left[a-\frac{\epsilon}{2}, b+\frac{\epsilon}{2}\right]$, where $\epsilon<a$. The following quantity defined as

$$
\chi=\prod_{\ell=0}^{L} \operatorname{det} \varphi\left(\frac{\mathbf{W}_{\ell} \mathbf{W}_{\ell}^{*}}{N_{\ell}}\right)
$$

verifies $\chi=1$ with probability 1 for all large $M$ from the classical results on the localization of the eigenvalues of Wishart matrices [31]. Recall also the definition of $m$ and $w$ in (58) and (60) respectively and denote for all $\ell=0, \ldots, L$ by $m_{\ell}$ the Stieltjes transform of the Marcenko-Pastur distribution with parameter $\left(c_{\ell}, \sigma^{2}\right)$, as well as for all $z \in \mathbb{C} \backslash\left[x_{\ell}^{-}, x_{\ell}^{+}\right]$

$$
\begin{aligned}
w_{\ell}(z) & =z\left(1+\sigma^{2} c_{\ell} m_{\ell}(z)\right) \\
\tilde{m}_{\ell}(z) & =-\frac{1}{z\left(1+\sigma^{2} c_{\ell} m_{\ell}(z)\right)} \\
\tau_{\ell}(z) & =z m_{\ell}(z) \tilde{m}(z)
\end{aligned}
$$

with $x_{\ell}^{ \pm}=\sigma^{2}\left(1 \pm \sqrt{c_{\ell}}\right)^{2}$.
2) Characteristic Polynomials Approximation: The first step of the proof consists in using the trick from [34] whose main idea is to relate the cumulative distribution function of the spiked eigenvalues with the determinant of certain random matrices.

Using Theorem 1 and the same arguments used to obtain the factorization (81) and (83) in Appendix B, we have that $\lambda_{1}\left(\hat{\mathbf{R}}_{\ell}\right), \ldots, \lambda_{K}\left(\hat{\mathbf{R}}_{\ell}\right)$ are the zeros of

$$
\hat{P}_{\ell}(z)=\operatorname{det}\left(\check{\mathbf{I}}+\hat{\Xi}_{\ell}(z)\right)
$$

for all $\ell \in\{0, \ldots, L\}$, with probability one for all large $M$, with

$$
\hat{\mathbf{\Xi}}_{\ell}(z)=\left[\begin{array}{cc}
\sqrt{z} \boldsymbol{\Omega}^{*} \mathbf{Q}_{\ell}(z) \boldsymbol{\Omega} \chi & \frac{1}{N_{\ell}} \boldsymbol{\Omega}^{*} \mathbf{Q}_{\ell}(z) \mathbf{W}_{\ell} \mathbf{S}_{\ell} \chi \\
\frac{1}{N_{\ell}} \mathbf{S}_{\ell}^{*} \mathbf{W}_{\ell}^{*} \mathbf{Q}_{\ell}(z) \boldsymbol{\Omega} \chi & \sqrt{z} \frac{1}{N_{\ell}} \mathbf{S}_{\ell}^{*} \tilde{\mathbf{Q}}_{\ell}(z) \mathbf{S}_{\ell} \chi
\end{array}\right]_{(1(}
$$

where $\mathbf{Q}_{\ell}(z)=\left(\frac{\mathbf{W}_{\ell} \mathbf{W}_{\ell}^{*}}{N_{\ell}}-z \mathbf{I}\right)^{-1}$ and $\tilde{\mathbf{Q}}_{\ell}(z)=$ $\left(\frac{\mathbf{W}_{\ell}^{*} \mathbf{W}_{\ell}}{N_{\ell}}-z \mathbf{I}\right)^{-1}$. For all $\ell, k$, let $-\infty<x_{k, \ell}<y_{k, \ell}<+\infty$ and denote

$$
\rho_{k, \ell}=\frac{\left(\gamma_{k}+\sigma^{2}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)}{\gamma_{k}}
$$

Then with probability one for all large $M$, we have

$$
\begin{aligned}
& \sqrt{M}\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\rho_{k, \ell}\right) \in\left[x_{k, \ell}, y_{k, \ell}\right] \\
& \Leftrightarrow \hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x_{k, \ell}}{\sqrt{M}}\right) \hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{y_{k, \ell}}{\sqrt{M}}\right)<0
\end{aligned}
$$

Therefore, as $M \rightarrow \infty$,

$$
\begin{aligned}
& \mathbb{P}\left(\bigcap_{k=1}^{K} \bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\rho_{k, \ell}\right) \in\left[x_{k, \ell}, y_{k, \ell}\right]\right\}\right)= \\
& \mathbb{P}\left(\bigcap_{k=1}^{K} \bigcap_{\ell=0}^{L}\left\{\hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x_{k, \ell}}{\sqrt{M}}\right) \hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{y_{k, \ell}}{\sqrt{M}}\right)<0\right\}\right) \\
& \quad+o(1) .
\end{aligned}
$$

The following proposition provides the expansion of $\hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right)$ around $\rho_{k, \ell}$.

Proposition 2. For all $x \in \mathbb{R}$,

$$
\begin{aligned}
& \hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right)=\frac{1}{\sqrt{M}} \prod_{i \neq k}\left(\gamma_{i} \tau_{\ell}\left(\rho_{k, \ell}\right)-1\right) \\
& \times\left(x \gamma_{k} \tau_{\ell}^{\prime}\left(\rho_{k, \ell}\right)-2 \sqrt{\gamma_{k}} \operatorname{Re}\left(\eta_{3, k, \ell}\right)+\gamma_{k} \rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \eta_{1, k, \ell}\right. \\
& \left.\left.\quad+\gamma_{k} \rho_{k, \ell} m_{\ell}\left(\rho_{k, \ell}\right) \eta_{2, k, \ell}\right)\right)+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

where $\tau_{\ell}(z)=z m_{\ell}(z) \tilde{m}_{\ell}(z)$ and

$$
\begin{aligned}
\eta_{1, k, \ell} & =\sqrt{M} \mathbf{u}_{k}^{*}\left(\mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \chi\right)^{\circ} \mathbf{u}_{k} \\
\eta_{2, k, \ell} & =\frac{\sqrt{M}}{N_{\ell}}\left(\mathbf{s}_{k, \ell}^{*} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{s}_{k, \ell} \chi\right)^{\circ} \\
\eta_{3, k, \ell} & =\frac{\sqrt{M}}{N_{\ell}} \mathbf{u}_{k}^{*} \mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{W}_{\ell} \mathbf{s}_{k, \ell} \chi
\end{aligned}
$$

Proof. The proof is deferred to Appendix E1.

From (108) and Proposition 2, it is clear that we have to study a CLT for the following generic quantity

$$
\eta=\sum_{\ell=0}^{L} \sum_{k=1}^{K}\left(\beta_{1, k, \ell} \eta_{1, k, \ell}+\beta_{2, k, \ell} \eta_{2, k, \ell}+\operatorname{Re}\left(\overline{\beta_{3, k, \ell}} \eta_{3, k, \ell}\right)\right)
$$

where $\left(\beta_{i, k, \ell}\right)_{\substack{i=1,2 \\ l=1, \ldots, K \\ \ell=0, \ldots, L}} \in \mathbb{R}^{2 K(L+1)}$ and $\left(\beta_{3, k, \ell}\right)_{\substack{k=1, \ldots, K \\ \ell=0, \ldots, L}} \in$ $\mathbb{C}^{K(L+1)}$.

3) Central Limit Theorem: Let us consider the characteristic function $\Psi(u)=\mathbb{E}[\xi(u)]$, with $\xi(u)=\exp (\mathrm{i} u \eta)$. Our approach consists in deriving a perturbed differential equation for $\Psi$ as shown in the following proposition. Let $\operatorname{bdiag}()$ denotes the block diagonal operator. Define $\mathbf{K}=\operatorname{bdiag}\left(\mathbf{K}_{1}, \ldots, \mathbf{K}_{K}\right)$ with $\mathbf{K}_{k}=\operatorname{bdiag}\left(\mathbf{K}_{1, k}, \ldots, \mathbf{K}_{4, k}\right)$ and where $\left(\mathbf{K}_{i, k}\right)_{i=1, \ldots, 4}$ are $(L+1) \times(L+1)$ symmetric matrices with entries given by

$$
\begin{aligned}
& {\left[\mathbf{K}_{1, k}\right]_{\ell+1, \ell^{\prime}+1}=} \\
& \begin{cases}\frac{\sigma^{4} c_{\ell}}{\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)} & \text { if } \ell=\ell^{\prime} \\
\frac{\sigma^{4} c_{0}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell^{\prime}}\right)\left(\gamma_{k}^{2}-\sigma^{4} c_{0}\right)} & \text { if } \ell=0<\ell^{\prime} \\
0 & \text { if } 0<\ell<\ell^{\prime}\end{cases} \\
& {\left[\mathbf{K}_{2, k}\right]_{\ell+1, \ell^{\prime}+1}= \begin{cases}\frac{c_{\ell}}{\left(\gamma_{k}+\sigma^{2}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)} & \text { if } \ell=\ell^{\prime} \\
\frac{c_{0}}{\left(\gamma_{k}+\sigma^{2}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{4} c_{0}\right)} & \text { if } \ell=0<\ell^{\prime} \\
0 & \text { if } 0<\ell<\ell^{\prime}\end{cases} }
\end{aligned}
$$

and for $i \in\{3,4\}$,

$$
\left[\mathbf{K}_{i, k}\right]_{\ell+1, \ell^{\prime}+1}= \begin{cases}\frac{1}{2} \frac{\sigma^{2} c_{\ell}}{\gamma_{k}^{2}-\sigma^{4} c_{\ell}} & \text { if } \ell=\ell^{\prime} \\ \frac{1}{2} \frac{\sigma^{2} c_{0}}{\gamma_{k}^{2}-\sigma^{4} c_{0}} & \text { if } \ell=0<\ell^{\prime} \\ 0 & \text { if } 0<\ell<\ell^{\prime}\end{cases}
$$

Denote also $\boldsymbol{\beta}=\left(\boldsymbol{\beta}_{1}^{T}, \ldots, \boldsymbol{\beta}_{K}^{T}\right)^{T}$ with

$\boldsymbol{\beta}_{k}=\left(\beta_{1, k, 0}, \ldots, \beta_{1, k, L}, \beta_{2, k, 0}, \ldots, \beta_{2, k, L}\right.$,

$$
\left.\operatorname{Re}\left(\beta_{3, k, 0}\right), \ldots, \operatorname{Re}\left(\beta_{3, k, L}\right), \operatorname{Im}\left(\beta_{3, k, 0}\right), \ldots, \operatorname{Im}\left(\beta_{3, k, L}\right)\right)^{T}
$$

Proposition 3. The matrix $\mathbf{K}$ is positive definite and

$$
\Psi^{\prime}(u)=-u \boldsymbol{\beta}^{T} \mathbf{K} \boldsymbol{\beta} \Psi(u)+\frac{\Delta(u)}{\sqrt{M}}
$$

where $\Delta$ is a continuous function such that $|\Delta(u)|<\mathrm{P}(u)$ for some polynomial $\mathrm{P}$ with positive coefficients independent of $M$.

Proof. The proof is deferred to Appendix E2
From Proposition 3, by solving the perturbed differential equation in 118 , we deduce that

$$
\Psi(u) \underset{M \rightarrow \infty}{\longrightarrow} \exp \left(-\boldsymbol{\beta}^{T} \mathbf{K} \boldsymbol{\beta} \frac{u^{2}}{2}\right)
$$

which of course implies that

$$
\eta \xrightarrow[M \rightarrow \infty]{\mathcal{D}} \mathcal{N}_{\mathbb{R}}\left(0, \boldsymbol{\beta}^{T} \mathbf{K} \boldsymbol{\beta}\right)
$$

The final step of the proof consists in transferring the CLT to the $K$ largest eigenvalues of $\left(\hat{\mathbf{R}}_{\ell}\right)_{\ell=1, \ldots, L}$. From Proposition (2), we have that:

$$
\begin{aligned}
& \hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right)= \\
& \quad \frac{1}{\sqrt{M}} \gamma_{k} \tau_{\ell}^{\prime}\left(\rho_{k, \ell}\right)\left(x-\zeta_{k, \ell}+o_{\mathbb{P}}(1)\right) \prod_{i \neq k}\left(\gamma_{i} \tau_{\ell}\left(\rho_{k, \ell}\right)-1\right)
\end{aligned}
$$

with

$$
\begin{gathered}
\zeta_{k, \ell}=\frac{1}{\gamma_{k} \tau_{\ell}^{\prime}\left(\rho_{k, \ell}\right)}\left(2 \sqrt{\gamma_{k}} \operatorname{Re}\left(\eta_{3, k, \ell}\right)-\gamma_{k} \rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \eta_{1, k, \ell}\right. \\
\left.-\gamma_{k} \rho_{k, \ell} m_{\ell}\left(\rho_{k, \ell}\right) \eta_{2, k, \ell}\right)
\end{gathered}
$$

Thus, going back to (108), we get

$$
\begin{aligned}
& \mathbb{P}\left(\bigcap_{k=1}^{K} \bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\rho_{k, \ell}\right) \in\left[x_{k, \ell}, y_{k, \ell}\right]\right\}\right)= \\
& \mathbb{P}\left(\bigcap_{k=1}^{K} \bigcap_{\ell=0}^{L}\left\{x_{k, \ell}<\zeta_{k, \ell}+o_{\mathbb{P}}(1)<y_{k, \ell}\right\}\right)+o(1)
\end{aligned}
$$

Using (120) with suitable values for $\boldsymbol{\beta}$ as well as the equal-


$\mathcal{N}_{\mathbb{R}^{K(L+1)}}(\mathbf{0}, \boldsymbol{\Theta})$, where $\boldsymbol{\Theta}$ is given in the statement of Theorem 2 Finally, noticing that

$$
\begin{aligned}
& \operatorname{det}(\boldsymbol{\Theta})= \prod_{k=1}^{K} \prod_{\ell=1}^{L} \theta_{k, \ell}^{2}\left(\theta_{0}^{2}-\sum_{\ell^{\prime}=1}^{L} \frac{\vartheta_{k, \ell^{\prime}}^{2}}{\theta_{k, \ell}^{2}}\right) \\
&=\left(\sigma^{4} c_{0}^{2}(L-1)\right)^{K} \prod_{k=1}^{K}\left(\frac{\gamma_{k}+\sigma^{2}}{\gamma_{k}}\right)^{2(L+1)} \\
& \times \prod_{\ell=1}^{L} c_{\ell}\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)
\end{aligned}
$$

we obtain that $\operatorname{det}(\boldsymbol{\Theta})>0$ thanks to Assumption 3 which concludes the proof of Theorem 2

## D. Proof of Corollary 2

Denote $c_{0}=c$ and for all $\ell=0, \ldots, L$, let $\hat{\phi}_{\ell}(w)=$ $w\left(1-\frac{\hat{\sigma}^{2} c_{\ell}}{\hat{\sigma}^{2}-w}\right)$. Denote as well $\hat{\mathbf{R}}_{0}=\hat{\mathbf{R}}$ and $\hat{\gamma}_{k, 0}=\hat{\gamma}_{k}$ for ease of reading. Under Assumption 3, we first observe from Theorem 1 that

$$
\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right) \xrightarrow[M \rightarrow \infty]{a . s .} \phi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)=\frac{\left(\gamma_{k}+\sigma^{2}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)}{\gamma_{k}}
$$

so that $\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)>\hat{\sigma}^{2} \sqrt{c_{\ell}}$ with probability one for all large $M$, and therefore $\hat{\gamma}_{k, \ell}+\hat{\sigma}^{2}$ coincides with the largest solution to the equation $\hat{\phi}_{\ell}(w)=\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)$. From Lemma 2 , we deduce that $\hat{\gamma}_{k, \ell}=\hat{w}_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)-\hat{\sigma}^{2}$. with probability one for all large $M$, where $\hat{w}_{\ell}(z)=z\left(1+\hat{\sigma}^{2} c_{\ell} \hat{m}_{\ell}(z)\right)$ with $\hat{m}_{\ell}$ the Stieltjes transform of the Marcenko-Pastur distribution with parameter $\left(\hat{\sigma}^{2}, c_{\ell}\right)$. It is easy to see that $\hat{\sigma}^{2}=\sigma^{2}+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{M}\right)$ and:

$$
\hat{m}_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)=m_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{M}\right)
$$

Therefore, we deduce that

$$
\hat{\gamma}_{k, \ell}=w_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)-\sigma^{2}+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{M}\right)
$$

As $w_{\ell}\left(\phi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)\right)=\gamma_{k}+\sigma^{2}$ and $w_{\ell}$ is differentiable at point $\gamma_{k}+\sigma^{2}$, a straightforward use of the delta-method provides

$$
\sqrt{M}\left(\hat{\gamma}_{k, \ell}-\gamma_{k}\right)_{\substack{\ell=0, \ldots, L \\ k=1, \ldots, K}} \xrightarrow[M \rightarrow \infty]{\mathcal{D}} \mathcal{N}_{\mathbb{R}^{K(L+1)}}(\mathbf{0}, \mathbf{G} \boldsymbol{\Theta} \mathbf{G})
$$

where $\mathbf{G}=\operatorname{diag}\left(\left(w_{\ell}^{\prime}\left(\phi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)\right)\right)_{\substack{\ell=0, \ldots, L \\ k=1, \ldots, K}}\right)$. Noticing that $w_{\ell}^{\prime}\left(\phi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)\right)=\frac{\gamma_{k}^{2}}{\gamma_{k}^{2}-\sigma^{2} c_{\ell}}$ from Lemma 3, we end up with $\mathbf{G} \Theta \mathbf{G}=\boldsymbol{\Omega}$, where $\boldsymbol{\Omega}$ is given in the statement of Corollary 2 Another immediate use of the delta-method allows to transfer the CLT from $\left(\hat{\gamma}_{k, \ell}\right)_{\substack{\ell=0, \ldots, L \\ k=1, \ldots, K}}$ to $\hat{\gamma}$.

## E. Additional proofs

1) Proof of Proposition 2, It is easy to see using Proposition 1 that for all $x \in \mathbb{R}$,

$$
\begin{aligned}
& \hat{\boldsymbol{\Xi}}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right)= \\
& {\left[\begin{array}{cc}
\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D} & \mathbf{0} \\
\mathbf{0} & \sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}
\end{array}\right]+\boldsymbol{\Delta}}
\end{aligned}
$$

where

$$
\begin{aligned}
& \boldsymbol{\Delta}= \\
& {\left[\begin{array}{cc}
\sqrt{\rho_{k, \ell}} \boldsymbol{\Omega}^{*}\left(\mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \chi\right)^{\circ} \boldsymbol{\Omega} & \frac{1}{N_{\ell}} \boldsymbol{\Omega}^{*} \mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \chi \mathbf{W}_{\ell} \mathbf{S}_{\ell} \\
\frac{1}{N_{\ell}} \mathbf{S}_{\ell}^{*} \mathbf{W}_{\ell}^{*} \mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \chi \boldsymbol{\Omega} & \sqrt{\rho_{k, \ell}} \frac{1}{N_{\ell}}\left(\mathbf{S}_{\ell}^{*} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{S}_{\ell} \chi\right)^{\circ}
\end{array}\right]} \\
& +\frac{x}{\sqrt{M}}\left[\begin{array}{cc}
h\left(\rho_{k, \ell}\right) \mathbf{D} & \mathbf{0} \\
\mathbf{0} & \tilde{h}\left(\rho_{k, \ell}\right) \mathbf{I}
\end{array}\right]+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

with $h_{\ell}(z)=\frac{m_{\ell}(z)}{2 \sqrt{z}}+\sqrt{z} m_{\ell}^{\prime}(z)$ and $\tilde{h}_{\ell}(z)=\frac{\tilde{m}_{\ell}(z)}{2 \sqrt{z}}+$ $\sqrt{z} \tilde{m}_{\ell}^{\prime}(z)$. Note that $\|\boldsymbol{\Delta}\|_{2}=\mathcal{O}_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)$ and we also consider the partition $\boldsymbol{\Delta}=\left(\boldsymbol{\Delta}_{i, j}\right)_{i, j=1,2}$ where each block $\boldsymbol{\Delta}_{i, j}$ is $K \times K$. Consider the event $\mathcal{A}=\left\{\left\|\boldsymbol{\Delta}_{2,2}\right\|_{2}<\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)\right\}$. From the block matrix determinant formula, we have:

$\hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right) \mathbb{1}_{\mathcal{A}}=\Phi \operatorname{det}\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\Delta_{2,2}\right) \mathbb{1}_{\mathcal{A}}$, with

$$
\begin{aligned}
& \Phi=\operatorname{det}\left(\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D}+\boldsymbol{\Delta}_{1,1}\right. \\
& \left.-\left(\mathbf{I}+\boldsymbol{\Delta}_{2,1}\right)\left(\sqrt{\rho}_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\boldsymbol{\Delta}_{2,2}\right)^{-1}\left(\mathbf{I}+\boldsymbol{\Delta}_{1,2}\right)\right) \mathbb{1}_{\mathcal{A}}
\end{aligned}
$$

Moreover,

$$
\begin{aligned}
& \left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\boldsymbol{\Delta}_{2,2}\right)^{-1} \mathbb{1}_{\mathcal{A}}= \\
& \left(\frac{\mathbf{I}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}-\frac{\boldsymbol{\Delta}_{2,2}}{\rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)^{2}}\right) \mathbb{1}_{\mathcal{A}}+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

which yields

$$
\begin{aligned}
\Phi= & \operatorname{det}\left(\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D}-\frac{\mathbf{I}}{\left.\sqrt{\rho}_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)\right)}+\boldsymbol{\Delta}_{1,1}\right. \\
& \left.-\frac{\boldsymbol{\Delta}_{1,2}+\boldsymbol{\Delta}_{2,1}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}+\frac{\boldsymbol{\Delta}_{2,2}}{\rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)^{2}}\right) \mathbb{1}_{\mathcal{A}}+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right) .
\end{aligned}
$$

Since $\mathbf{D}=\operatorname{diag}\left(\gamma_{1}, \ldots, \gamma_{K}\right)+o\left(\frac{1}{\sqrt{M}}\right)$ from Assumption 2 and from Lemma 3, we have

$$
\operatorname{det}\left(\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}\right)=o\left(\frac{1}{\sqrt{M}}\right) .
$$

Using the differential of the determinant, we further have

$$
\begin{aligned}
\Phi & =\operatorname{tr}\left[\operatorname{com}\left(\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho}_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}\right)^{T}\right. \\
& \left.\times\left(\boldsymbol{\Delta}_{1,1}-\frac{\boldsymbol{\Delta}_{1,2}+\boldsymbol{\Delta}_{2,1}}{\sqrt{\rho}_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}+\frac{\boldsymbol{\Delta}_{2,2}}{\rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)^{2}}\right)\right] \mathbb{1}_{\mathcal{A}} \\
& +o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

where $\operatorname{com}()$ denotes the comatrix operation. A direct computation together with Assumption 2 provides

$$
\begin{aligned}
& \operatorname{com}\left(\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}\right)= \\
& \quad \frac{\prod_{i \neq k}\left(\gamma_{i} \rho_{k, \ell} m_{\ell}\left(\rho_{k, \ell}\right) \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)-1\right)}{\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)\right)^{K-1}} \mathbf{e}_{k} \mathbf{e}_{k}^{*}+o\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

Consequently,

$$
\begin{aligned}
\Phi & =o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)+\frac{\prod_{i \neq k}\left(\gamma_{i} \rho_{k, \ell} m_{\ell}\left(\rho_{k, \ell}\right) \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)-1\right)}{\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)\right)^{K-1}} \\
& \times\left[\boldsymbol{\Delta}_{1,1}-\frac{\boldsymbol{\Delta}_{1,2}+\boldsymbol{\Delta}_{2,1}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}+\frac{\boldsymbol{\Delta}_{2,2}}{\rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)^{2}}\right]_{k, k} \mathbb{1}_{\mathcal{A}}
\end{aligned}
$$

In the same way,

$$
\begin{aligned}
& \operatorname{det}\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\boldsymbol{\Delta}_{2,2}\right)= \\
& \quad\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)\right)^{K}+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

so that

$$
\begin{aligned}
& \hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right) \mathbb{1}_{\mathcal{A}}= \\
& {\left[\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \boldsymbol{\Delta}_{1,1}+\frac{\boldsymbol{\Delta}_{2,2}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}-\left(\boldsymbol{\Delta}_{1,2}+\boldsymbol{\Delta}_{2,1}\right)\right]} \\
& \times \prod_{i \neq k}\left(\gamma_{i} \rho_{k, \ell} m_{\ell}\left(\rho_{k, \ell}\right) \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)-1\right)+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
\end{aligned}
$$

Since $\mathbb{1}_{\mathcal{A}}=1+o_{\mathbb{P}}(1)$, we also deduce that

$$
\hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right) \mathbb{1}_{\mathcal{A}^{c}}=o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
$$

and using Assumption 2 leads to the result of Proposition 2 .

2) Proof of Proposition 3. The proof makes use of wellknown techniques specific to the Gaussian distribution, namely the Stein's lemma and the Poincaré's inequality which we recall below and which have already been exploited in e.g. [35], [15], [24]. Therefore, we only give the main steps of the proof and skip some details of the computations.

a) Useful tools.: A function $f: \mathbb{C}^{n} \rightarrow \mathbb{C}$ is said to be $\mathcal{C}^{1}\left(\mathbb{C}^{n}\right)$ if $f(\mathbf{z})=\tilde{f}(\operatorname{Re}(\mathbf{z}), \operatorname{Im}(\mathbf{z}))$ with $\tilde{f} \in \mathcal{C}^{1}\left(\mathbb{R}^{2 n}\right)$. Moreover, we also recall the definition of the standard complex differential operators

$$
\begin{aligned}
\frac{\partial f}{\partial z_{k}}(\mathbf{z}) & =\frac{1}{2}\left(\frac{\partial \tilde{f}}{\partial x_{k}}(\mathbf{x}, \mathbf{y})-\mathrm{i} \frac{\partial \tilde{f}}{\partial y_{k}}(\mathbf{x}, \mathbf{y})\right) \\
\frac{\partial f}{\partial \bar{z}_{k}}(\mathbf{z}) & =\frac{1}{2}\left(\frac{\partial \tilde{f}}{\partial x_{k}}(\mathbf{x}, \mathbf{y})+\mathrm{i} \frac{\partial \tilde{f}}{\partial y_{k}}(\mathbf{x}, \mathbf{y})\right)
\end{aligned}
$$

with $\mathbf{x}=\operatorname{Re}(\mathbf{z})$ and $\mathbf{y}=\operatorname{Im}(\mathbf{z})$.

Lemma 4 (Stein's lemma). Let $\mathbf{w} \sim \mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0}, \mathbf{I})$ and $f \in$ $\mathcal{C}^{1}\left(\mathbb{C}^{n}\right)$, assumed polynomially bounded together with its partial derivatives. Then for all $k=1, \ldots, n$,

$$
\mathbb{E}\left[f(\mathbf{w}) w_{k}\right]=\mathbb{E}\left[\frac{\partial f}{\partial \overline{w_{k}}}(\mathbf{w})\right], \mathbb{E}\left[f(\mathbf{w}) \overline{w_{k}}\right]=\mathbb{E}\left[\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right]
$$

Lemma 5 (Poincaré inequality). Let $\mathbf{w} \sim \mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0}, \mathbf{I})$ and $f \in \mathcal{C}^{1}\left(\mathbb{C}^{n}\right)$, assumed polynomially bounded together with its partial derivatives. Then,

$$
\mathbb{V}[f(\mathbf{w})] \leq \sum_{k=1}^{n}\left(\mathbb{E}\left|\frac{\partial f}{\partial \overline{w_{k}}}(\mathbf{w})\right|^{2}+\mathbb{E}\left|\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right|^{2}\right)
$$

For ease of reading, we introduce the following differentiation operators with respect to the entries of the $M \times N_{\ell}$ matrix $\mathbf{W}_{\ell}$, which will be constantly used in the derivations below,

$$
\partial_{i, j}^{(\ell)}=\frac{\partial}{\partial\left[\mathbf{W}_{\ell}\right]_{i, j}}, \quad \bar{\partial}_{i, j}^{(\ell)}=\frac{\partial}{\partial\left[\overline{\left.\mathbf{W}_{\ell}\right]_{i, j}}\right.}
$$

We will also need the following auxiliary result (see [33]) related to the quantity $\chi$ defined in $(100)$.

Lemma 6. For all $p \in \mathbb{N}$ and $r \in \mathbb{N}, \mathbb{E}\left[\chi^{r}\right]=1+\mathcal{O}\left(\frac{1}{N^{p}}\right)$ and for $\ell \in\{0, \ldots, L\}$ and for any $i \in\{1, \ldots, M\}, j \in$ $\left\{1, \ldots, N_{\ell}\right\}$,

$$
\mathbb{E}\left[\partial_{i, j}^{(\ell)} \chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right) \text { and } \mathbb{E}\left[\bar{\partial}_{i, j}^{(\ell)} \chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right)
$$

Lemma 6 shows in particular that the presence of the regularization term $\chi$ can be removed from expectations, up to an error term of arbitrary polynomial decay.

In the following, $\Delta$ is a generic notation for a continuous function such that $|\Delta(u)|<\mathrm{P}(u)$ for some polynomial $\mathrm{P}$ with positive coefficients independent of $M$, and whose value may change from one line to another.

b) Development of $\Psi^{\prime}$ : Write

$$
\begin{aligned}
& \Psi^{\prime}(u)=\mathrm{i} \sum_{k=1}^{K} \sum_{\ell=0}^{L} \mathbb{E}\left[\left(\beta_{1, k, \ell} \eta_{1, k, \ell}+\beta_{2, k, \ell} \eta_{2, k, \ell}\right.\right. \\
&\left.\left.+\operatorname{Re}\left(\overline{\beta_{3, k, \ell}} \eta_{3, k, \ell}\right)\right) \xi(u)\right]
\end{aligned}
$$

In the following, we only provide some details for the development of $\mathbb{E}\left[\eta_{1, k, 0} \xi(u)\right]$, as the other terms can be obtained similarly. Using the resolvent identity, we start by writing

$\mathbb{E}\left[\eta_{1, k, 0} \xi(u)\right]=\frac{\sqrt{M}}{\rho_{k, 0}} \mathbb{E}\left[\left(\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \frac{\mathbf{W}_{0} \mathbf{W}_{0}^{*}}{N_{0}} \mathbf{u}_{k} \chi\right)^{\circ} \xi(u)\right]$.

Next, we apply Stein's lemma, Poincaré's inequality and Lemma 6 to obtain

$$
\begin{aligned}
& \mathbb{E}\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \frac{\mathbf{W}_{0} \mathbf{W}_{0}^{*}}{N_{0}} \mathbf{u}_{k} \chi \xi(u)\right]= \\
& \frac{\mathrm{i} u \sigma^{2} \sum_{i, j} \mathbb{E}\left[\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell}^{*} \mathbf{u}_{k}\right]_{j} \chi \bar{\partial}_{i, j}^{(0)}\{\eta\} \xi(u)\right]}{N_{0}\left(1+\alpha_{0}\left(\rho_{k, 0}\right)\right)} \\
& \quad+\frac{\sigma^{2} \mathbb{E}\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{u}_{k} \chi \xi(u)\right]}{1+\alpha_{0}\left(\rho_{k, 0}\right)}+\frac{\Delta(u)}{M}
\end{aligned}
$$

where $\alpha_{\ell}(z)=\mathbb{E}\left[\frac{\sigma^{2}}{N_{\ell}} \operatorname{tr} \mathbf{Q}_{\ell}(z) \chi\right]$ for all $\ell=0, \ldots, L$. Using the fact that $\alpha_{0}\left(\rho_{k, 0}\right)=\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)+\mathcal{O}\left(\frac{1}{M^{2}}\right)$, this gives

$$
\begin{aligned}
& \mathbb{E}\left[\eta_{1, k, 0} \xi(u)\right]= \\
& \frac{\mathrm{i} u \sigma^{2} \sqrt{M} \sum_{i, j} \mathbb{E}\left[\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell}^{*} \mathbf{u}_{k}\right]_{j} \chi \bar{\partial}_{i, j}^{(0)}\{\eta\} \xi(u)\right]}{N_{0}\left(\rho_{k, 0}\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)-\sigma^{2}\right)} \\
& +\frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

Developing further the derivatives and using Lemma 6, we have

$$
\begin{gathered}
\sum_{i, j} \mathbb{E}\left[\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell}^{*} \mathbf{u}_{k}\right]_{j} \chi \bar{\partial}_{i, j}^{(0)}\left\{\eta_{1, k^{\prime}, \ell}\right\} \xi(u)\right]= \\
-\sqrt{M} \mathbb{E}\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{Q}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{u}_{k^{\prime}} \mathbf{u}_{k^{\prime}}^{*} \mathbf{Q}_{\ell}\left(\rho_{k^{\prime}, \ell}\right)\right. \\
\left.\quad \times \frac{\mathbf{W}_{\ell} \mathbf{W}_{\ell}^{*}}{N_{\ell}} \mathbf{u}_{k} \chi \xi(u)\right]+\frac{\Delta(u)}{\sqrt{M}} \\
=\sqrt{M} \theta_{k, \ell} \delta_{k-k^{\prime}} \Psi(u)+\frac{\Delta(u)}{\sqrt{M}}
\end{gathered}
$$

with

$$
\begin{aligned}
\kappa_{k, \ell} & = \begin{cases}\frac{\sigma^{2} m_{0}\left(\rho_{k, 0}\right) m_{0}^{\prime}\left(\rho_{k, 0}\right)}{1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)} & \text { if } \ell=0 \\
\frac{\sigma^{2} m_{\ell}\left(\rho_{k, \ell}\right) m_{0}\left(\rho_{k, 0}\right)\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)}{\sigma^{2}-\rho_{k, \ell}\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)\left(1+\sigma^{2} c_{\ell} m_{\ell}\left(\rho_{k, \ell}\right)\right)} & \text { if } \ell \geq 1\end{cases} \\
& = \begin{cases}-\frac{\sigma^{2} \gamma_{k}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)} & \text { if } \ell=0 \\
-\frac{\sigma^{2} \gamma_{k}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)} & \text { if } \ell \geq 1\end{cases}
\end{aligned}
$$

where the second equality in the expression of $\theta_{k, \ell}$ can be obtained with Lemma 3 Moreover,

$$
\begin{aligned}
& \sum_{i, j} \mathbb{E}[ {\left.\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell}^{*} \mathbf{u}_{k}\right]_{j} \chi \bar{\partial}_{i, j}^{(0)}\left\{\eta_{2, k^{\prime}, \ell}\right\} \xi(u)\right] } \\
&=-\frac{\sqrt{M}}{N_{\ell}^{2}} \mathbb{E}[ \mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{W}_{\ell} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{s}_{k^{\prime}, \ell} \\
&\left.\quad \times \mathbf{s}_{k^{\prime}, \ell}^{*} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{W}_{\ell}^{*} \mathbf{u}_{k} \chi \xi(u)\right]+\frac{\Delta(u)}{\sqrt{M}} \\
&=\frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

and

$$
\begin{aligned}
& \sum_{i, j} \mathbb{E}[ {\left.\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell}^{*} \mathbf{u}_{k}\right]_{j} \chi \bar{\partial}_{i, j}^{(0)}\left\{\eta_{3, k^{\prime}, \ell}\right\} \xi(u)\right] } \\
&=-\frac{\sqrt{M}}{N_{\ell}} \mathbb{E}\left[\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{Q}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{W}_{\ell} \mathbf{s}_{k^{\prime}, \ell}\right. \\
&\left.\quad \times \mathbf{u}_{k^{\prime}}^{*} \mathbf{Q}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \frac{\mathbf{W}_{\ell} \mathbf{W}_{\ell}^{*}}{N_{\ell}} \mathbf{u}_{k} \chi \xi(u)\right]+\frac{\Delta(u)}{\sqrt{M}} \\
&=\frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

Finally, using again Lemma 3, we obtain

$$
\begin{aligned}
& \mathbb{E}\left[\eta_{1, k, 0} \xi(u)\right] \\
& =\frac{\mathrm{i} u \sigma^{2} c_{0} \sum_{\ell=0}^{L} \beta_{1, k, \ell} \kappa_{k, \ell}}{\rho_{k, 0}\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)-\sigma^{2}} \Psi(u)+\frac{\Delta(u)}{\sqrt{M}} \\
& =-\mathrm{i} u\left(\frac{\beta_{1, k, 0} \sigma^{4} c_{0}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)}\right. \\
& \left.+\sum_{\ell=1}^{L} \frac{\beta_{1, k, \ell} \sigma^{4} c_{0}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)}\right) \Psi(u)+\frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

Using similar computations for the remaining terms $\left(\mathbb{E}\left[\eta_{i, k, \ell} \xi(u)\right]\right)_{i=1}^{\ell \geq 1}$ in $\Psi^{\prime}(u)$, we finally obtain the result of Proposition 3

## REFERENCES

[1] R. Beisson, P. Vallet, A. Giremus, and G. Ginolhac, "Change Detection in The Covariance Structure of High-Dimensional Gaussian Low-Rank Models," in Statistical Signal Processing Workshop (SSP). IEEE, 2021, pp. 421-425.
[2] K. Conradsen, A. Nielsen, J. Schou, and H. Skriver, "A test statistic in the complex Wishart distribution and its application to change detection in polarimetric SAR data," IEEE Trans. Geosci. Remote Sens., vol. 41, no. 1, pp. 4-19, 2003.

[3] D. Ciuonzo, V. Carotenuto, and A. De Maio, "On multiple covariance equality testing with application to SAR change detection," IEEE Trans. on Signal Process., vol. 65, no. 19, pp. 5078-5091, 2017.

[4] A. Mian, G. Ginolhac, J.-P. Ovarlez, and A. Atto, "New robust statistics for change detection in time series of multivariate SAR images," IEEE Trans. Signal Process., vol. 67, no. 2, pp. 520-534, 2018.

[5] A. Mian, A. Collas, A. Breloy, G. Ginolhac, and J.-P. Ovarlez, "Robust low-rank change detection for multivariate sar image time series," IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens., vol. 13, pp. 3545-3556, 2020.

[6] R. Liu, L. Liu, D. He, W. Zhang, and E. G. Larsson, "Detection of abrupt change in channel covariance matrix for multi-antenna communication," in Global Communications Conference (GLOBECOM). IEEE, 2021.

[7] P. Galeano and D. Peña, "Covariance changes detection in multivariate time series,” J. Stat. Plan. Inference, vol. 137, no. 1, pp. 194-211, 2007.

[8] A. Ribes, J.-M. Azais, and S. Planton, "Adaptation of the optimal fingerprint method for climate change detection using a well-conditioned covariance matrix estimate," Clim. Dyn., vol. 33, no. 5, pp. 707-722, 2009.

[9] Y.-H. Zhou, "Set-based differential covariance testing for genomics," Stat, vol. 8, no. 1, p. e235, 2019

[10] A. Gupta and J. Tang, "Distribution of likelihood ratio statistic for testing equality of covariance matrices of multivariate gaussian models," Biometrika, vol. 71, no. 3, pp. 555-559, 1984.

[11] R. Muirhead, Aspects of multivariate statistical theory. Wiley Online Library, 1982.

[12] S. Zheng, "Central limit theorems for linear spectral statistics of large dimensional F-matrices," Ann. Inst. H. Poincaré Probab. Statist., vol. 48, no. 2, pp. 444-476, 2012.

[13] I. Johnstone, "On the distribution of the largest eigenvalue in principal components analysis," Ann. Statist., vol. 29, no. 2, pp. 295-327, 042001.

[14] A. Combernoux, F. Pascal, and G. Ginolhac, "Performance of the lowrank adaptive normalized matched filter test under a large dimension regime," IEEE Trans. Aerosp. Electron. Syst., vol. 55, no. 1, pp. 459$468,2018$.

[15] P. Vallet, X. Mestre, and P. Loubaton, "Performance analysis of an improved music doa estimator," IEEE Trans. Signal Process, vol. 63, no. 23, p. 6407-6422, 2015.

[16] K. Wachter, "The limiting empirical measure of multiple discriminant ratios," Ann. Statist., pp. 937-957, 1980.

[17] Q. Wang and J. Yao, "Extreme eigenvalues of large-dimensional spiked fisher matrices with application," Ann. Statist., vol. 45, no. 1, pp. 415460, 2017 .

[18] R. Abdallah, A. Mian, A. Breloy, A. Taylor, M. El Korso, and D. Lautru, "Detection methods based on structured covariance matrices for multivariate SAR images processing," IEEE Geosci. Remote. Sens. Lett., vol. 16, no. 7, pp. 1160-1164, 2019.

[19] R. Abdallah, A. Breloy, A. Taylor, M. El Korso, and D. Lautru, "Signal subspace change detection in structured covariance matrices," in 27th European Signal Processing Conference (EUSIPCO). IEEE, 2019.

[20] F. Benaych-Georges, A. Guionnet, and M. Maida, "Fluctuations of the Extreme Eigenvalues of Finite Rank Deformations of Random Matrices," Electron. J. Probab., vol. 16, pp. no. 60,1621-1662, 2011.

[21] F. Benaych-Georges and R. Nadakuditi, "The eigenvalues and eigenvectors of finite, low rank perturbations of large random matrices," Adv. Math., vol. 227, no. 1, pp. 494-521, 2011.

[22] T. Anderson, An introduction to multivariate statistical analysis. John Wiley \& Sons, 1958.

[23] I. Johnstone, "High dimensional statistical inference and random matrices," in International Congress of Mathematicians, Madrid, 2006.

[24] X. Mestre and P. Vallet, "Correlation Tests and Linear Spectral Statistics of the Sample Correlation Matrix," IEEE Trans. Inf. Theory, vol. 63, no. 7, pp. 4585-4618, 2017.

[25] R. Couillet, "Robust spiked random matrices and a robust G-MUSIC estimator," J. Multivariate Anal., vol. 140, pp. 139-161, 2015, publisher: Elsevier.

[26] J. B. G. A. S. Péché, "Phase transition of the largest eigenvalue for nonnull complex sample covariance matrices," Ann. Probab. 33 (5) 1643 - 1697, 2005.

[27] P. Vallet, P. Loubaton, and X. Mestre, "On the consistency of likelihood penalization methods in large sensor networks," in 7th Sensor Array and Multichannel Signal Processing Workshop (SAM). IEEE, 2012, pp. 109-112.

[28] P. Stoica and R. Moses, Spectral analysis of signals. Pearson Prentice Hall, 2005, vol. 452.

[29] A. Mian, J.-P. Ovarlez, A. Atto, and G. Ginolhac, "Design of new wavelet packets adapted to high-resolution sar images with an application to target detection," IEEE Trans. Geosci. Remote Sens., vol. 57, no. 6, pp. 3919-3932, 2019.

[30] X. Mestre, "On the asymptotic behavior of the sample estimates of eigenvalues and eigenvectors of covariance matrices," IEEE Trans. Signal Process., vol. 56, no. 11, pp. 5353-5368, 2008.

[31] S. Geman, "A limit theorem for the norm of random matrices," Ann. Prob., pp. 252-261, 1980.

[32] R. Horn and C. Johnson, Matrix analysis. Cambridge university press, 2012.

[33] W. Hachem, P. Loubaton, X. Mestre, J. Najim, and P. Vallet, "Large information plus noise random matrix models and consistent subspace estimation in large sensor networks," Random Matrices: Theory Appl., vol. 1, no. 2, 2012.

[34] F. Benaych-Georges and R. Nadakuditi, "The singular values and vectors of low rank perturbations of large rectangular random matrices," $J$. Multivariate Anal., vol. 111, no. 0, pp. 120-135, 2012.

[35] W. Hachem, O. Khorunzhiy, P. Loubaton, J. Najim, and L. Pastur, "A new approach for capacity analysis of large dimensional multi-antenna channels," IEEE Trans. Inf. Theory, vol. 54, no. 9, pp. 3987-4004, 2008.


[^0]:    ${ }^{1}$ Although outside the scope of this paper, we note that the results of 17 Th. 6.1] could be exploited to build a test statistic with controlled asymptotic type I error, which is not the case for (48).

