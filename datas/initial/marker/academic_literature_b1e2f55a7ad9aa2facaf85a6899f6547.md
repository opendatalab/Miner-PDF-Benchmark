# A New Statistic For Testing Covariance Equality In High-Dimensional Gaussian Low-Rank Models

R. BEISSON, *Student Member, IEEE*, P. VALLET, *Member, IEEE*, A. GIREMUS, *Member, IEEE*, G. GINOLHAC,
Member, IEEE
Abstract**—In this paper, we consider the problem of testing**
equality of the covariance matrices of L **complex Gaussian** multivariate time series of dimension M**. We study the special** case where each of the L **covariance matrices is modeled as a rank** K **perturbation of the identity matrix, corresponding to a signal**
plus noise model. A new test statistic based on the estimates of the eigenvalues of the different covariance matrices is proposed. In particular, we show that this statistic is consistent and with controlled type I error in the high-dimensional asymptotic regime where the sample sizes N1*, . . . , N*L **of each time series and the**
dimension M **both converge to infinity at the same rate, while**
K and L **are kept fixed. We also provide some simulations**
on synthetic and real data (SAR images) which demonstrate significant improvements over some classical methods such as the GLRT, or other alternative methods relevant for the highdimensional regime and the low-rank model.

## I. Introduction

D
ETECTING changes in the behaviour of multivariate time series is a fundamental problem in many applications going from remote sensing [2], [3], [4], [5] and wireless communications [6] to finance [7], climatology [8] or genomics [9]. In several of those applications, a usual approach consists in modeling the changes using the distribution of the time series, and in particular through an evolution in the structure of the covariance matrix.

Consider the context of M-dimensional time series
(yn,1)n∈Z
, . . . ,(yn,L)n∈Z
, assumed mutually independent and such that for all ℓ ∈ {1*, . . . , L*},

$$\left(\mathbf{y}_{n,\ell}\right)_{n\in\mathbb{Z}}{\mathrm{\overset{i.i.d.}{\sim}}}\,{\mathcal{N}}_{\mathbb{C}^{M}}\left(\mathbf{0},\mathbf{R}_{\ell}\right),$$

where NCM (0, Rℓ) denotes the zero-mean complex normal distribution with covariance matrix Rℓ. Detecting the changes in the distribution of (yn,ℓ)n∈Z
, for all ℓ ∈ {1*, . . . , L*}, can be formalized as the following binary hypothesis test dealing with the equality of the L covariance matrices R1*, . . . ,* RL,

$$\begin{array}{l}\mathcal{H}_{0}:\ \ \mathbf{R}_{1}=\ldots=\mathbf{R}_{L}\\ \mathcal{H}_{1}:\ \ \exists(i,j)\in\{1,\ldots,L\}^{2}:\mathbf{R}_{i}\neq\mathbf{R}_{j}\end{array}.\tag{2}$$  Assume that for all $\ell\in\{1,\ldots,L\}$, $N_{\ell}$ observations $\mathbf{Y}_{1}\,\ell,\ldots,\mathbf{Y}_{N_{\ell}\,\ell}$ are available and let $N=N_{1}+\cdots+N_{L}$. A 
R. Beisson, P. Vallet and A. Giremus are with Laboratoire de l'Integration ´
du Materiau au Syst ´ eme (CNRS, Univ. Bordeaux, Bordeaux INP), 351 Cours ` de la Liberation, 33400 Talence (France) ´
G. Ginolhac is with Laboratoire d'Informatique, Systemes, Traitement `
de l'Information et de la Connaissance (Univ. Savoie/Mont-Blanc, Polytech Annecy), 5 chemin de Bellevue, 74940 Annecy (France)
This work was partially supported by Agence de l'Innovation de Defense ´
and Region Nouvelle-Aquitaine. The material of this paper was partly pre- ´ sented in the conference paper [1].

large class of test statistics widely encountered in the literature
[3] involves, provided that M < N1*, . . . , N*L, linear spectral statistics of the matrices Rˆ −1 ℓ Rˆ of the form:

$$S=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\frac{1}{M}\sum_{k=1}^{M}\varphi\left(\lambda_{k}(\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}})\right),$$
$$(3)$$
, (3)
where λk(Rˆ −1 ℓ Rˆ ), for all k ∈ {1*, . . . , M*}, are the eigenvalues of the matrix Rˆ −1 ℓ Rˆ with

$${\hat{\mathbf{R}}}_{\ell}:={\frac{1}{N_{\ell}}}\sum_{n=1}^{N_{\ell}}\mathbf{y}_{n,\ell}\mathbf{y}_{n,\ell}^{*},$$
$${\mathrm{(4)}}$$

denoting the sample covariance matrix (SCM) associated with Rℓ and

$${\hat{\mathbf{R}}}=\sum_{\ell=1}^{L}{\frac{N_{\ell}}{N}}{\hat{\mathbf{R}}}_{\ell}.$$
$$(S)$$
$$(1)$$

In (3), φ denotes some continuous function defined on
(0, +∞). In particular, the Generalized Likelihood Ratio
(GLR) [3] with φ(x) = log(x) or the *Nagao* statistic with φ(x) = (x − 1)2are included in the class of statistics
(3). The presence of a change in the covariance is decided by comparing (3) to a threshold ϵ chosen to guarantee a certain type I error and the null hypothesis H0 is rejected if S > ϵ. Moreover, the test statistics based on (3) have the key property that the distribution of S under H0 is independent of R1 = *. . .* = RL, which allows to control its type I error.

However, in practice, the distribution of statistics of type
(3) under H0 is untractable and only known in a few special cases for finite M, N1*, . . . , N*L (e.g. for the GLR, see [10]). To circumvent this issue, approximations in the *low-dimensional*
(or *large sample size*) regime in which N1, . . . , NL → ∞
while *M, L* are fixed can be derived, see e.g. [11, Th. 10.8.4].

While the latter are meant to be used in practical scenarios where N1*, . . . , N*L ≫ M, they may not be reliable in contexts involving high-dimensional (large M) observations or moderate sample sizes N1*, . . . , N*L. Indeed, in that highdimensional case, it is often more reasonable to assume that M, N1*, . . . , N*L are of the same order of magnitude in which case the predictions of the distribution of (3) under H0 in the low-dimensional regime become irrelevant.

The context where M, N1*, . . . , N*L are of the same order of magnitude can be modeled more realistically by the *highdimensional regime* in which it is assumed that M converges to infinity together with N1*, . . . , N*L such that M
Nℓ → cℓ > 0, while L is kept fixed. In this non-standard regime, the asymptotic distribution of the statistic S can be derived using random matrix theory techniques (see e.g. [12] for the case L = 2).

Moreover, in several applications involving highdimensional observations, the potential changes in the covariance Rℓ may only be carried by a low-rank component
(see e.g. [13], [14], [15]). This is the case, e.g., in array processing when dealing with a large array of M sensors and a small number K of source signals compared to M [15].

In that case, we have the model

$$+\,\sigma^{2}\mathbf{I},$$

## Rℓ = Γℓ + Σ 2I, (6)

2
with Γℓ the covariance matrix of rank *K < M* of a useful signal and σ 2I the covariance matrix of a spatially white additive noise. When the rank K remains constant in the high-dimensional regime, the matrices R−1 ℓ Rℓ
′ are fixed rank perturbations of the identity. Using well-known results [16],
[17] on the asymptotic spectral distribution of the Fisher type random matrices Rˆ −1 ℓ Rˆ , one can show under both H0 and H1 that

$$S\rightarrow\sum_{\ell=1}^{L}\frac{c}{c_{\ell}}\int_{x_{\ell}^{-}}^{x_{\ell}^{+}}\varphi\left(\frac{c}{c_{\ell}}(1+x)\right)f_{\ell}(x)\mathrm{d}x,\tag{7}$$  almost surely (a.s.) where $c=(c_{1}^{-1}+\ldots+c_{L}^{-1})^{-1}$ and where $f_{\ell}$ is the so-called _Wacher_ distribution given by 
$$f_{\ell}(x)=\left(\frac{1}{c_{\ell}}-1\right)\frac{\sqrt{(x-x_{\ell}^{-})(x_{\ell}^{+}-x)}}{2\pi x(1+x)}\mathds{1}_{[x_{\ell}^{-},x_{\ell}^{+}]}(x),\tag{8}$$  with $x_{\ell}^{\pm}=\frac{c_{\ell}-c}{c(1-c_{\ell})^{2}}\left(1\pm\sqrt{c_{\ell}+\frac{cc_{\ell}}{c_{\ell}-c}-\frac{cc_{\ell}^{2}}{c_{\ell}-c}}\right)^{2}.$ Thus $S$ converges to the same limit under both hypotheses $\mathcal{H}_{0}$ and 
H1, which indicates that test statistics relying on (3) might not be relevant in the *high-dimensional regime* and for the low-rank model in (6).

So far from our knowledge, the problem of covariance equality testing under low-rank models has not received much attention in the literature. The work of [18] considers the GLRT, under a low-rank Gaussian model, for a covariance equality test with a different alternative hypothesis H′1
: R1 ̸=
R2 = *. . .* = RL. An extension to the specific case of subspace equality test has also been proposed by the same authors in
[19].

Under the model (6), the information about a potential change is contained in the K largest eigenvalues and associated eigenvectors of Rℓ. Therefore, classical results on the spiked models for random matrices of the Fisher type [17] can be exploited to characterize the asymptotic behaviour of the extreme eigenvalues of (Rˆ −1 ℓ Rˆ )ℓ=1*,...,L*, from which information about a potential change can be extracted. In the same way, the asymptotic behaviour of the largest eigenvalues of the spiked Wishart-type matrices [20] Rˆ ,(Rˆℓ)ℓ=1*,...,L* convey information about changes in the true covariances R1*, . . . ,* RL
[1], which can also be exploited to build test statistics relevant for the low-rank model in the high-dimensional regime. This latter option is the path followed in this paper.

Contributions. In this paper, we derive a new test statistic, no longer based on the family of statistics S studied in [3],
but which relies on the K largest eigenvalues of the matrices Rˆ1*, . . . ,* Rˆ L, Rˆ . More precisely, the test statistic compares in a certain sense estimates of the eigenvalues of the matrices Γ1*, . . . ,*ΓL with estimates of the eigenvalues of the mixture Γ =PL
ℓ=1 Nℓ N Γℓ. We show that the proposed test statistic is consistent under the high-dimensional regime and the low-rank model (6), and with a controlled asymptotic type I error. To that purpose, the results of [21], which provides the asymptotic distribution of the K largest eigenvalues of Rˆℓ for a fixed ℓ, are extended to provide the joint asymptotic distribution of the K largest eigenvalues of the matrices Rˆ , Rˆ1*, . . . ,* Rˆ L. The proposed test statistic is then compared to various alternatives, including the GLRT for the low-rank model (6) as well as a statistic built from the results of [17] on the extreme eigenvalues of the spiked Fisher matrices (Rˆ −1 ℓ Rˆ )ℓ=1*,...,L*. We also provide an empirical study of the proposed test statistic on Synthetic Aperture Radar (SAR) images for detecting changes between two scenes.

Organization. The paper is organized as follows. In Section II, we study an extension of the results of [21] on the asymptotic distribution of the largest eigenvalues of Rˆ1*, . . . ,* Rˆ L, Rˆ .

In Section III, we exploit the results derived in the previous section to build a new test statistic, for which we study its performance in the *high-dimensional regime*. Sections IV and V are dedicated to compare, both theoretically and numerically, our proposed test statistic with alternative approaches.

Simulations on synthetic data and on real data (SAR images) are provided.

Notations. For a ∈ R, a
+ denotes the positive part. Vectors and matrices are denoted with boldface lower case and upper case letters respectively. For a complex matrix A, we denote by ATand A
∗its transpose and conjugate transpose. If A
is a n × n complex matrix, tr(A) denotes its trace and λ1(A)*, . . . , λ*n(A) denote its eigenvalues. If A is Hermitian, the eigenvalues are considered in decreasing order λ1(A) ≥ . . . ≥ λn(A). For matrices A1*, . . . ,* An, bdiag(A1*, . . . ,* An)
denotes the the block diagonal matrix formed by A1*, . . . ,* An.

The complex circular Gaussian distribution on C
n with covariance matrix R is denoted as NCn (0, R), while the real Gaussian distribution on R
n with mean µ and covariance matrix R is denoted as NRn (µ, R).

## Ii. Spectrum Of Rˆ

In this section, we study the asymptotic behavior at 1 st and 2 nd orders of the largest eigenvalues of Rˆ when the matrices Rˆ1*, . . . ,* Rˆ L follow the low-rank model (6).

Consider the following two assumptions, which describe the high-dimensional regime and specify the asymptotic behavior of the eigenvalues of Γ1*, . . . ,*ΓL. Assumption 1. The sample sizes N1 = N1(M)*, . . . , N*L = NL(M) are functions of M *such that*

$$\frac{M}{N_{\ell}}=c_{\ell}+o\left(\frac{1}{\sqrt{M}}\right),\tag{9}$$  _as $M\rightarrow\infty$, where $c_{1},\ldots,c_{L}>0$ and $K,L$ are independent._
of M.
In comparison with the classical *low-dimensional regime* where M is assumed fixed while N1, . . . , NL → ∞ (see e.g. [22], [11]), the high-dimensional regime described in Assumption 1 models practical scenarios where the sample sizes N1*, . . . , N*L are of the same order of magnitude as the dimension M and where K is small compared to M. This regime has been widely used in the high-dimensional statistics literature (see e.g. [23]), as well as in the signal processing applications (see e.g. [15], [24], [25]).

In what follows the *high-dimensional regime* described in Assumption 1 is represented by the notation M → ∞. We also define

as well as $\frac{1}{2}$
$$c:=\left(\sum_{\ell=1}^{L}\frac{1}{c_{\ell}}\right)^{-1},$$  $$\Gamma:=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\Gamma_{\ell}.$$
One can notice that Γ is the the pooling of the low-rank covariance matrices Γ1*, . . . ,*ΓL and has rank at most KL. In the following, we also need to ensure the convergence of the eigenvalues of matrices Γℓ,Γ in the high-dimensional regime.

  **Assumption 2**.: _For all $k\in\{1,\ldots,K\}$, $\ell\in\{1,\ldots,L\}$,_  $$\lambda_{k}(\mathbf{\Gamma}_{\ell})=\gamma_{k,\ell}+o\left(\frac{1}{\sqrt{M}}\right),$$  _and $\lambda_{k}$ is a $\ell$-invariant._
, (12)
_and for all $k\in\{1,\ldots,KL\}$,_  $$\lambda_{k}(\mathbf{\Gamma})=\gamma_{k}+o\left(\frac{1}{\sqrt{M}}\right).$$  We note that $\Lambda$ is a $\gamma$-independent, $\Lambda$ is a $\gamma$-independent.  
We note that Assumption 2 is a purely technical assumption which is not restrictive in practice as the corresponding results derived from it are meant to be used for fixed values of M, N, K.

Under Assumptions 1 and 2, the global behaviour of the eigenvalues of Rˆ can be described through its empirical spectral distribution defined as the random probability measure

$$\hat{\mu}=\frac{1}{M}\sum_{k=1}^{M}\delta_{\lambda_{k}}(\mathbf{\hat{n}}),\tag{14}$$

where δx is the Dirac measure centered at x. Under the model (6), each covariance matrix R1*, . . . ,* RL is a fixed rank K perturbation of the matrix σ 2I and it can be shown using standard perturbations arguments that µˆ asymptotically behaves as the Marcenko-Pastur distribution, i.e. µˆ converges weakly almost surely *(a.s.)* to the probability measure:

by almost surely ($a.s.$) to the probability measure.  $$\mu(\mathrm{d}x)=\frac{\sqrt{(x-x^{-})(x^{+}-x)}}{2\pi\sigma^{2}cx}\mathbbm{1}_{[x^{-},x^{+}]}(x)\mathrm{d}x$$ $$\qquad+\left(1-\frac{1}{c}\right)^{+}\delta_{0}(\mathrm{d}x),\tag{15}$$  we $x^{\pm}=\sigma^{2}(1\pm\sqrt{c})^{2}.$ Consequently, any functional of the 
where x
type
$${\hat{\mu}}(\varphi):={\frac{1}{M}}\sum_{k=1}^{M}\varphi(\lambda_{k}({\hat{\mathbf{R}}})),$$
where φ is a bounded continuous function, satisfies

3
$$\hat{\mu}(\varphi)=\int_{\mathbb{R}}\varphi(\lambda)\mathrm{d}\hat{\mu}(\lambda)\ \frac{a.s.}{M\rightarrow\infty}\int_{\mathbb{R}}\varphi(\lambda)\mathrm{d}\mu(\lambda).\tag{17}$$
As the limit in (17) only depends on σ 2and c, it is not possible to recover information on the low-rank matrices Γ1*, . . . ,*ΓL
in the *high-dimensional regime* from statistics of type (16).

However, under the previous assumptions, it can be shown that the information related to the spectrum of Γ can be found in the largest KL eigenvalues of Rˆ , thanks to the following result.

1. _Under Assumptions 1 and 2, $\forall k\in\{1,\ldots,KL\}$,_  $$\lambda_{k}\left(\hat{\mathbf{R}}\right)\xrightarrow[M\to\infty]{a.s.}\phi_{c}\left(\gamma_{k},\sigma^{2}\right),\tag{18}$$
$$(10)$$
$$(11)$$
with

$$\phi_{c}(\gamma,\sigma^{2}):=\begin{cases}\frac{(\gamma+\sigma^{2})(\gamma+\sigma^{2}c)}{\gamma}&\text{if}\gamma>\sigma^{2}\sqrt{c}\\ \sigma^{2}(1+\sqrt{c})^{2}&\text{if}\gamma\leq\sigma^{2}\sqrt{c}\end{cases},\tag{19}$$

Moreover, λKL+1(Rˆ ) → σ 2(1 + √c)
2a.s. when M → ∞.

Proof. The proof of Theorem 1 is deferred to Appendix B.

$$(12)$$
$$(13)$$

The matrix Rˆ being a mixture of L independent but not identically distributed Wishart matrices, we note that Theorem 1 provides an extension of the results of [21, Th. 2.7] (see also [26]) to the case L > 1. It shows in particular that the largest eigenvalues of Rˆ converge to some limits depending directly of the eigenvalues of Γ, provided that for all k ∈
{1*, . . . , KL*} the ratios γk σ2 are above √c. The threshold √c can be interpreted as a minimal SNR above which the k th largest *signal related* eigenvalues of Rˆ splits from the largest noise related eigenvalue λKL+1(Rˆ ).

The next result shows, under hypothesis H0, a joint *Central Limit Theorem* (CLT) on the largest eigenvalues of Rˆ1*, . . . ,* Rˆ L, Rˆ .

Theorem 2. *Let Assumptions 1-2 hold. Assume moreover that* Γ1 = . . . = ΓL (thus γk,ℓ = γk*) and that* γ1 > . . . > γK > σ2 max{
√c, √c1
, . . . , √cL}. (20)
Then we have

in we have  $$\sqrt{M}\left(\begin{array}{c}\lambda_{k}\left(\hat{\mathbf{R}}\right)-\phi_{c}(\gamma_{k},\sigma^{2})\\ \left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\phi_{c\ell}(\gamma_{k},\sigma^{2})\right)_{\ell=1,...,L}\right)_{k=1,...,K}\\ \frac{\mathcal{D}}{M\rightarrow\infty}\,\mathcal{N}_{\mathbb{R}^{K(L+1)}}\left(\mathbf{0},\mathbf{\Theta}\right),\end{array}\tag{21}$$
(15)  $\mathfrak{\text{of the}}$
where Θ *is a positive definite block diagonal matrix given by* Θ = bdiag (Θ1, . . . , ΘK) *with*

$$\mathbf{\Theta}_{k}:=\begin{pmatrix}\theta_{k,0}^{2}&\vartheta_{k,1}&\dots&\vartheta_{k,L}\\ \vartheta_{k,1}&\ddots&(0)\\ \vdots&&(0)&\ddots\\ \vartheta_{k,L}&&\theta_{k,L}^{2}\end{pmatrix},\tag{22}$$
$$(16)$$

and by denoting c0 = c,

$$\theta_{k,\ell}^{2}=c_{\ell}\frac{(\gamma_{k}^{2}-\sigma^{4}c_{\ell})(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}},\quad\ell\geq0,\tag{23}$$

4
$$\vartheta_{k,\ell}=c_{0}\frac{(\gamma_{k}^{2}-\sigma^{4}c_{\ell})(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}},\quad\ell\geq1.\tag{24}$$  Proof.: The proof is postponed to Appendix C.  
The result of Theorem 2 provides an extension of [20, Th.

1.4] which studies a CLT for the K largest eigenvalues of Rˆℓ. We note that the result of Theorem 2 cannot be inferred directly from [20, Th. 1.4] and requires a careful study due to the strong dependency between the eigenvalues of Rˆ and the ones of Rˆ1*, . . . ,* Rˆ L.

Theorems 1 and 2 are exploited in the following section to build a new statistic for the test (2), relevant for the low-rank model (6).

III. PROPOSED TEST STATISTIC

Before introducing our new test statistic, we first notice that
the test (2) can be reformulated as:
$${\mathcal{H}}_{0}:\quad\mathbf{\Gamma}_{1}=\ldots=\mathbf{\Gamma}_{L}$$
, (25)
$${\mathcal{H}}_{1}:\ \ \exists(i,j)\in\{1,\ldots,L\}^{2}\ \mathrm{s.t.}\ \Gamma_{i}\neq\Gamma_{j}^{\ ;}$$
and we assume in the following that the rank K is *known* (see also Remark 1 below in case the rank is unknown). Next, we consider the following lemma, which shows that hypothesis H0 can be verified by comparing the eigenvalues of matrix Γ
with the ones of matrices Γ1*, . . . ,*ΓL.

Lemma 1. *The following assertions are equivalent:*

1. $\Gamma_{1}=\ldots=\Gamma_{L}$, 2. _For all_ $k=1,\ldots,K$_,_ $\ell=1,\ldots,L$_,_ $\lambda_{k}\left(\Gamma_{\ell}\right)=\lambda_{k}\left(\Gamma\right)$_._  Proof.: The proof of Lemma 1 can be found in [1].  
From Lemma 1, one can equivalently formulate the test (25)
as follows
$$\begin{array}{l}{\cal H}_{0}:\ \ \forall k,\ell,\ \lambda_{k}\left(\Gamma_{\ell}\right)=\lambda_{k}\left(\Gamma\right)\\ {\cal H}_{1}:\ \ \exists k,\ell:\lambda_{k}\left(\Gamma_{\ell}\right)\neq\lambda_{k}\left(\Gamma\right)^{\cdot}\end{array}\tag{26}$$
Consequently, it is possible to discriminate between hypotheses H0 and H1 by exploiting only the eigenvalues of the matrices Γ1*, . . . ,*ΓL,Γ for which we can also build consistent estimators in the high-dimensional regime as follows. Let us consider first the maximum likelihood estimator of the noise variance σ 2 given by

$$\hat{\sigma}^{2}:=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\frac{1}{M-K}\sum_{k=K+1}^{M}\lambda_{k}\left(\hat{\bf R}_{\ell}\right).$$
. (27)
From (6) and Theorem 1, one can easily show that σˆ
2 −→ σ 2 a.s. as M → +∞ under both H0 and H1. Next, for all k ∈ {1*, . . . , KL*}, let γˆk be the largest solution to the equation ϕc(γk, σˆ
2) = λk(Rˆ ) if λk(Rˆ ) > σˆ
2(1 + √c)
2, or γˆk = ˆσ 2√c otherwise. Similarly, for all k ∈ {1*, . . . , K*}, let γˆk,ℓ be the largest solution to the equation ϕcℓ
(γk,ℓ, σˆ
2) = λk(Rˆℓ) if λk(Rˆℓ) > σˆ
2(1 + √cℓ
)
2, or γˆk,ℓ = ˆσ 2√cℓ otherwise. Then we have the following immediate result, as a consequence of Theorem 1.

Corollary 1. *Under Assumptions 1 and 2,*

$$\hat{\gamma}_{k}\ \frac{a.s.}{M\!\rightarrow\!\infty}\,\begin{cases}\gamma_{k}&\text{if}\gamma_{k}>\sigma^{2}\sqrt{c}\\ \sigma^{2}\sqrt{c}&\text{otherwise}\end{cases},\tag{28}$$
$$\hat{\gamma}_{k,\ell}\xrightarrow[M\to\infty]{a.s.}\xrightarrow[M\to\infty]{}\begin{cases}\gamma_{k,\ell}&\text{if}\gamma_{k,\ell}>\sigma^{2}\sqrt{c_{\ell}}\\ \sigma^{2}\sqrt{c_{\ell}}&\text{otherwise}\end{cases}.\tag{29}$$

Considering this result we propose the following test statistic
$$T(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(\|{\hat{\gamma}}\|_{2}^{2}\right),$$
, (30)
where
$$\hat{\gamma}=(\hat{\gamma}_{k}-\hat{\gamma}_{k,\ell})_{k=1,...,K}\cdot\ell=1,...,L\tag{31}$$
To study the performance in terms of consistency and asymptotic type I error of the test statistic (30), we consider the following assumption which ensures that the signal and noise eigenvalues of matrices Rˆ , Rˆ1*, . . . ,* Rˆ L are separated in the high-dimensional regime.

  **Assumption 3**.: _For all $k\in\{1,\ldots,K\}$ and $\ell\in\{1,\ldots,L\}$,_  $$\gamma_{1,\ell}>\ldots>\gamma_{K,\ell}>\sigma^{2}\max\{\sqrt{c_{1}},\ldots,\sqrt{c_{L}}\},\tag{32}$$ $$\gamma_{1}>\ldots>\gamma_{K}>\sigma^{2}\sqrt{c}.\tag{33}$$
$$(25)$$
Moreover, under H1, there exist k, ℓ such that γk ̸= γk,ℓ.

As a consequence of Corollary 1, we have under Assumptions 1-3,

$$L\},$$ $$\quad(32)$$ $$\quad(33)$$
$$\|{\hat{\gamma}}\|_{2}^{2}\ {\xrightarrow[M\to\infty]{\mathrm{a.s.}}}\ \|\gamma\|_{2}^{2}\,,$$
$$(35)$$
, (34)
with

$$\gamma=(\gamma_{k}-\gamma_{k,l})_{\stackrel{k=1,...,K}{\ell=1,...,L}},$$

such that γ = 0 under H0 and γ ̸= 0 under H1. This implies the following consistency result.

Theorem 3. *Let Assumptions 1-3 hold and denote* ϵ1 =
∥γ∥
2 2 > 0 under H1. Then for all ϵ ∈ (0, ϵ1),

$$\mathbb{P}_{i}\left(\operatorname*{lim}_{M\to\infty}T(\epsilon)=i\right)=1,$$

for i ∈ {0, 1}, where Pi*is the probability measure under* hypothesis Hi.

To control the asymptotic type I error of the proposed test statistic (30), we also need the following result which, as a consequence of Theorem 2, provides a CLT for (31).

$$(27)$$
Corollary 2. Under hypothesis H0 *and Assumptions 1-3, we*
have√
$$\sqrt{M}\hat{\gamma}\ \frac{\mathcal{D}}{M\!\rightarrow\!\infty}\ \mathcal{N}_{\mathbb{R}KL}\left(\mathbf{0},\mathbf{H}\mathbf{\gamma}\mathbf{H}^{T}\right),\tag{37}$$

where H *is the* KL × K(L + 1) *matrix defined by* H =
bdiag H˜ *, . . . ,* H˜, Υ = bdiag (Υ1, . . . , ΥK) with H˜ the L × (L + 1) *matrix given by*

$$\tilde{\bf H}=\begin{pmatrix}1&-1&0&\dots&\dots&0\\ 1&0&-1&\ddots&&\vdots\\ \vdots&\vdots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\vdots&&\ddots&\ddots&0\\ 1&0&\dots&\dots&0&-1\end{pmatrix},\tag{38}$$

and with

5
_and with_  $$\Upsilon_{k}=\begin{pmatrix}\omega_{k,0}^{2}&\xi_{k}&\ldots&\xi_{k}\\ \xi_{k}&\ddots&(0)\\ \vdots&(0)&\ddots&\\ \xi_{k}&&\omega_{k,L}^{2}\end{pmatrix},$$  _where_  $$\omega_{k,\ell}^{2}=\frac{c_{\ell}\gamma_{k}^{2}(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}-\sigma^{4}c_{\ell}},\quad\ell=0,\ldots,L,$$  $$\xi_{k}=\frac{c_{0}\gamma_{k}^{2}(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}-\sigma^{4}c_{0}}.$$  Proof.: The proof is deferred to Appendix D.  
, (39)
From Corollary 2, we can adjust the threshold ϵ in (30) to control the asymptotic type I error in the high-dimensional regime, as described in the next result. Let us define Υˆ =
bdiag Υˆ1*, . . . ,* Υˆ K
with

Υˆk =   ωˆ 2 k,0ˆξk . . .ˆξk ˆξk... (0) ... (0) ... ˆξk ωˆ 2 k,L   , (41) where ωˆ 2 k,ℓ = cℓγˆ 2 k (ˆγk + ˆσ 2) 2 γˆ 2 k − σˆ 4cℓ, ℓ ≥ 0 ˆξk = c0γˆ 2 k (ˆγk + ˆσ 2) 2 γˆ 2 k − σˆ 4c0. From Corollary 1, it is clear that Υˆ → Υ a.s. as M → ∞.
where $$\mathbf{\mu}$$
Theorem 4. Let x ∈ NRKL (0, I) and F(t, Ξ) =
Px T Ξx ≤ t, α ∈ (0, 1) *and set*

$$\hat{\epsilon}=\frac{1}{M}\operatorname*{inf}\left\{t\in\mathbb{R}:F\left(t,\mathbf{H}\hat{\mathbf{Y}}\mathbf{H}^{T}\right)\geq1-\alpha\right\}.$$  _Then under Assumptions 1 and 3, we have_
o. (43)
$$\mathbb{P}_{0}(T({\hat{\epsilon}})=1)\;{\xrightarrow[M\to\infty]{}}\;\alpha.$$
α. (44)
In practice, Theorem 4 is used as follows. For a fixed realization of Υˆ , we sample the distribution of the Gaussian quadratic form x T HΥHˆ T x and the threshold ϵˆ is then set as the (1 − α)-quantile of x T HΥHˆ T x.

Remark 1. *For a more general approach where each* Γℓ has unknown rank Kℓ*, one can obtain consistent estimates of* K1, . . . , KL thanks to Theorem 1. Assuming K1, . . . , KL fixed with respect to M, and if for ℓ ∈ {1, . . . , L}, γKℓ,ℓ > σ2√cℓ
,
under Assumption 2 the quantity

$$\hat{K}_{\ell}=\max\left\{k:\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)>\sigma^{2}(1+\sqrt{c}_{\ell})^{2}+\epsilon_{\ell}\right\},\tag{45}$$

converges almost surely to Kℓ *in the high-dimensional regime,*
for all ϵℓ ∈0, ϕcℓ γKℓ,ℓ, σ2− σ 2(1 + √cℓ)
2. This shows that we can build consistent test statistics to capture changes in the rank (see further [27]).

$$(39)$$

Remark 2. *It is easy to show that under Assumption 3,*
the matrix HΥHT*is non singular. Therefore, an alternative* approach to obtain a test statistic with controlled asymptotic type I error would be to consider the statistic

$$\tilde{T}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(M\left\|\left(\mathbf{H}\hat{\mathbf{T}}\mathbf{H}^{T}\right)^{-\frac{1}{2}}\hat{\gamma}\right\|_{2}^{2}\right),$$
$$(46)$$
, (46)
since from Corollary 2, we have

$$(40)$$
(41)  $$\begin{array}{l}\mathbf{a}\end{array}$$ = (42)  . 
$$M\left\|\left(\mathbf{H\hat{T}H}^{T}\right)^{-\frac{1}{2}}\hat{\gamma}\right\|_{2}^{2}\xrightarrow[M\to\infty]{}\chi^{2}(KL).\tag{47}$$
$$\square$$

Nevertheless, although this approach looks simpler, it appears that the covariance matrix HΥHT*is ill-conditioned. This can* be readily seen, e.g. in the special case where c1 = *. . .* = cL and for a large SNR. If κ(Υk) *denotes the condition number* of Υk *defined in* (39), then we can verify (details are omitted) that κ(Υk) *scales with* γ 2 as γ 2 → ∞*. Therefore, in practice,*
setting the threshold ϵ *based on the* χ 2(KL) *distribution gives* poor performance.

## Iv. Some Comparisons With Alternative Methods

In this section, we compare the test statistic given in (30)
with two relevant alternatives for the low-rank model (6) and the *high-dimensional regime* described in Assumption 1. To that purpose, we consider scenarios involving a change of subspace/eigenvalues for the rank K = 1 model Γℓ = γ1,ℓuℓu
∗
ℓ
,
where ∥uℓ∥2 = 1, and where γ1,ℓ is independent of M.

We precise that our objective is not to provide an exhaustive analysis of all the possible scenarios under H1, but to draw some performance comparisons, in terms of consistency, out of a few simple cases. In the remainder of this section, we also assume that L = 2 and N1 = N2 so that c1 = c2 = 2c.

$$(43)$$

## A. A Test Based On Spiked Fisher Matrices

Although test statistics of the form (3) are not consistent in the *high-dimensional regime*, we can build consistent test statistics by exploiting the behaviour of the largest and smallest eigenvalues of the Fisher matrices Rˆ −1 2 Rˆ1 (see [17]). We propose 1to use TFisher(ϵ) = 1(ϵ,+∞)(F) with

$$F=\sum_{\begin{array}{c}\ell,\ell^{\prime}=1\\ \ell^{\prime}\neq\ell\end{array}}^{L}\sum_{k=1}^{K}\Biggl{[}\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}}_{\ell^{\prime}}\right)-\nu_{\ell,\ell^{\prime}}^{+}\right)^{+}\tag{48}$$ $$+\left(\nu_{\ell,\ell^{\prime}}^{-}-\lambda_{M-k}\left(\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}}_{\ell^{\prime}}\right)\right)^{+}\Biggr{]},$$

where ν
$$\nu_{\ell,\ell^{\prime}}^{\pm}=\left(\frac{1\pm\sqrt{c_{\ell}+c_{\ell^{\prime}}-c_{\ell}c_{\ell^{\prime}}}}{1-c_{\ell}}\right)^{2}.$$
Change of subspace. Let us consider that under H1, γ1,1 =
γ1,2 and u
∗
1u2 → 0 as M → ∞, so that the changes between 1Although outside the scope of this paper, we note that the results of [17, Th. 6.1] could be exploited to build a test statistic with controlled asymptotic type I error, which is not the case for (48).

Γ1 and Γ2 are only carried by the unit norm eigenvector u2.

It is easily seen that

$$\lambda_{k}\left(\mathbf{R}_{2}^{-1}\mathbf{R}_{1}\right)\xrightarrow[M\to\infty]{}\begin{cases}\frac{\gamma_{1,1}+\sigma^{2}}{\sigma^{2}}&\text{if}k=1,\\ 1&\text{if}k=2,\ldots,M-1,\\ \frac{\sigma^{2}}{\gamma_{1,1}+\sigma^{2}}&\text{if}k=M,\end{cases}\tag{49}$$
so that applying [17, Th. 3.1] shows that for all small ϵ > 0,
Pi(lim TFisher(ϵ) = i) = 1 for i ∈ {0, 1} as M → ∞ iff
$$\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2\left(c+\sqrt{c-c^{2}}\right)}{1-2c}.\tag{50}$$

One can see that β > √2c and therefore, from Assumption 3 and Theorem 3, we deduce that the Fisher based statistic requires a larger SNR γ1,1 σ2 compared to the Wishart based statistic proposed in (30) to be consistent in the change of subspace scenario.

Change of eigenvalues. In that case, we assume that γ1,2 =
γ1,1(1 + δ) with δ > 0 and u1 = u2, so that the changes are only carried by the largest eigenvalue of Γ2. Note that under these settings, Assumption 2 is verified and it holds that

$$\lambda_{k}\left(\mathbf{R}_{2}^{-1}\mathbf{R}_{1}\right)\xrightarrow[M\to\infty]{}\begin{cases}\frac{\gamma_{1,1}+\sigma^{2}}{\gamma_{1,1}(1+\delta)+\sigma^{2}}&\text{if$k=1$,}\\ 1&\text{if$k=2,\ldots,M$.}\end{cases}\tag{51}$$
Using again [17, Th. 3.1], we have that for all small ϵ > 0,
P(lim TFisher(ϵ) = i) = 1 for i ∈ 0, 1 as M → ∞ iff
$$\delta>\frac{2(c+\sqrt{c-c^{2}})}{1-2c},$$  and  $$\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2(c+\sqrt{c-c^{2}})}{(1+\delta)(1-2c)-(1+2\sqrt{c-c^{2}})}.$$  **In the case of $\alpha$, the $\alpha$-function is a function of $\alpha$.**
. (53)
In this scenario, one can see that the minimal SNR β decreases when δ increases, which can be exploited to produce conditions where the Fisher test statistic is consistent while the Wishart one is not. Indeed, choose √c < γ1,1 σ2 <
√2c and δ large enough so that (52) and (53) are verified. Then it can be seen from Corollary 1 that ∥γˆ∥
2 2 → 2(γ1,1 − σ 2
√2c)
2 a.s. as M → ∞ and therefore for all small ϵ > 0, P0 (lim T(ϵ) = 1) = 1.

## B. The Glr For (25)

As an alternative to the GLR for the general covariance equality test (2), the GLR for the low-rank test (25) can be derived. Classical computations (details are omitted) provide the following test statistic TGLR−LR(ϵ) = 1(ϵ,+∞)(G) where

$$G=-\sum_{\ell=1}^{L}N_{\ell}\sum_{k=1}^{K}\log\left(\frac{\lambda_{k}(\hat{\mathbf{R}}_{\ell})}{\lambda_{k}(\hat{\mathbf{R}})}\right)$$ $$-N(M-K)\log\left(\frac{\frac{1}{M-K}\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\sum_{k=K+1}^{M}\lambda_{k}(\hat{\mathbf{R}}_{\ell})}{\frac{1}{M-K}\sum_{k=K+1}^{M}\lambda_{k}(\hat{\mathbf{R}})}\right).$$

Using Theorem 1, it can be shown that G → G∞ a.s. as M → ∞ where

6
$$G_{\infty}=\sum_{\ell=1}^{L}\frac{c}{c_{\ell}}\sum_{k=1}^{K}\left(\psi\left(\frac{\phi_{c}(\gamma_{k})}{\sigma^{2}}\right)-\psi\left(\frac{\phi_{c_{\ell}}(\gamma_{k,\ell})}{\sigma^{2}}\right)\right),\tag{55}$$  with $\ell(\gamma)$ as a value $(\gamma)$
with ψ(x) = x − log(x).

Let us consider a change of eigenvalues with γ1,2 = γ1,1+δ and u1 = u2 under H1. Then it is easy to see that under both H0 and H1, G∞ = −c + O
1 γ1,1 as γ1,1 → +∞.

Regarding the proposed test (30), we have ∥γ∥
2 2 =
δ 2 2under H1 which shows the limit (34) under H0 and H1 cannot be made arbitrarily close as γ1,1 → ∞. This suggests that for a large γ1,1 and a fixed change δ, the GLR for the low-rank model might experience a performance loss compared to the test (30).

## V. Simulations

In this section, we provide simulations to illustrate the performance of the test statistic T proposed in (30), and to perform some comparisons with the alternative test statistics introduced in Section IV. We consider σ 2 = 0.5, K = 2, L =
2 as well as a Toeplitz model of rank K = 2 for the covariance matrix Γℓ which can therefore be written as Γℓ = γ1,ℓa (θ1,ℓ) a
∗(θ1,ℓ) + γ2,ℓa (θ2,ℓ) a
∗(θ2,ℓ), (56)
with a(θ) = √
1 M
(1, e iθ*. . . ,* e i(M−1)θ)
T. Note that the model
(56) is common in spectral analysis and array processing [28].

$$(52)^{\frac{1}{2}}$$
$$({\mathfrak{H}}^{3})$$

A. Empirical and asymptotic Type I error of T(ϵ)
We first illustrate the result of Theorem 4 and consider θk,ℓ = 0 for (k, ℓ) ∈ {1, 2}
2, γ1,ℓ = 3 and γ2,ℓ = 1.5 for ℓ ∈ {1, 2} and N1 = N2 = 2M. The threshold ϵ of (30)
is set as the (1 − α)-quantile of the Gaussian quadratic form x T HΥHˆ T x with x ∼ NRKL (0, I), and we provide in TABLE
I the empirical Type I error of T(ϵ) (evaluated over 100000 iterations) for M ∈ {10, 20, 50, 100}. Table I thus shows that TABLE I
TYPE I ERROR OF T(ϵ)

| α           | 0.005   | 0.01   | 0.02   | 0.05   | 0.10   |
|-------------|---------|--------|--------|--------|--------|
| T(ϵ) M = 10 | 0.002   | 0.004  | 0.009  | 0.028  | 0.065  |
| M = 20      | 0.0025  | 0.005  | 0.01   | 0.03   | 0.073  |
| M = 50      | 0.003   | 0.006  | 0.013  | 0.038  | 0.083  |
| M = 100     | 0.004   | 0.008  | 0.016  | 0.043  | 0.09   |

the empirical type I error is close to the asymptotic type I
error predicted in Theorem 4, when M is increasing.

## B. Comparisons Of Powers

In this section, we evaluate the proposed test statistic on synthetic data by considering the following two scenarios.

(1) *Change of subspace:* under H0, θ1,1 = θ1,2 = 0, θ2,1 =
θ2,2 =
π 8 and under H1, θ1,1 = 0, θ1,2 =
π 2
, θ2,1 =
π 8
, θ2,2 =
π 2 +
π 8
. We will also consider under both 7
hypothesis γ1,1 = γ1,2 = 2, γ2,1 = γ2,2 = 1 and N1 =
N2 = 2M thus c1 = c2.

(2) *Change of Eigenvalues:* under H0, γ1,1 = γ1,2 = 2, γ2,1 = γ2,2 = 1.5 and under H1, γ1,1 = 2, γ1,2 = 5, γ2,1 = 1.5, γ2,2 = 4. We will also consider under both hypothesis θ1,1 = θ1,2 = 0, θ2,1 = θ2,2 = 0 and N1 =
N2 = 4M thus c1 = c2.

In the simulations that follow, for both scenarios, we compute the power of different test statistics for a given type I error α and different values of M. The statistic T(ϵ), which will be termed as "Wishart" below, will be compared to the statistics TFisher(ϵ) (termed as "Fisher"), TGLR−LR(ϵ) (termed as
"GLR-LR") and TGLR(ϵ) = 1(ϵ,+∞)(S|φ=log ) where S is given in (3) (termed as "GLR"). For each of the statistics, the threshold ϵ is adjusted separately to achieve a type I error of α. Note that for both scenarios, Assumptions 2, 3 are verified and that the condition for the Fisher statistic to be consistent is verified as well. We observe that in both scenarios, TABLE II
POWER FOR DIFFERENT VALUES OF M (CHANGE OF EIGENVALUES
SCENARIO)
TABLE III
POWER FOR DIFFERENT VALUES OF M (CHANGE OF SUBSPACE SCENARIO)

| α          | 0.005   | 0.01   | 0.02   | 0.05   | 0.1   |
|------------|---------|--------|--------|--------|-------|
| Statistics | M = 10  |        |        |        |       |
| GLR        | 0.493   | 0.592  | 0.701  | 0.826  | 0.906 |
| GLR-LR     | 0.992   | 0.996  | 0.998  | 0.999  | 1     |
| Fisher     | 0.149   | 0.215  | 0.312  | 0.473  | 0.624 |
| Wishart    | 0.026   | 0.056  | 0.119  | 0.3    | 0.519 |
| M = 20     |         |        |        |        |       |
| GLR        | 0.757   | 0.829  | 0.89   | 0.949  | 0.978 |
| GLR-LR     | 1       | 1      | 1      | 1      | 1     |
| Fisher     | 0.398   | 0.493  | 0.597  | 0.739  | 0.84  |
| Wishart    | 0.646   | 0.812  | 0.924  | 0.988  | 1     |
| M = 50     |         |        |        |        |       |
| GLR        | 0.832   | 0.883  | 0.927  | 0.968  | 0.987 |
| GLR-LR     | 1       | 1      | 1      | 1      | 1     |
| Fisher     | 0.783   | 0.846  | 0.894  | 0.944  | 0.972 |
| Wishart    | 1       | 1      | 1      | 1      | 1     |
| M = 100    |         |        |        |        |       |
| GLR        | 0.838   | 0.891  | 0.934  | 0.972  | 0.988 |
| GLR-LR     | 1       | 1      | 1      | 1      | 1     |
| Fisher     | 0.955   | 0.971  | 0.984  | 0.993  | 0.997 |
| Wishart    | 1       | 1      | 1      | 1      | 1     |

TABLE IV
POWER FOR DIFFERENT VALUES OF σ 2(CHANGE OF EIGENVALUES
SCENARIO)

| POWER FOR DIFFERENT VALUES OF σ 2 (CHANGE OF EIGENVALUES SCENARIO)   |            |       |       |       |       |    |       |      |      |      |     |
|----------------------------------------------------------------------|------------|-------|-------|-------|-------|----|-------|------|------|------|-----|
| α                                                                    | 0.005      | 0.01  | 0.02  | 0.05  | 0.1   |    |       |      |      |      |     |
| Statistics                                                           | M = 10     |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.120      | 0.181 | 0.266 | 0.412 | 0.550 |    |       |      |      |      |     |
| GLR-LR                                                               | 0.381      | 0.483 | 0.588 | 0.734 | 0.832 |    |       |      |      |      |     |
| Fisher                                                               | 0.309      | 0.397 | 0.5   | 0.653 | 0.775 |    |       |      |      |      |     |
| Wishart                                                              | 0.998      | 0.999 | 0.999 | 1     | 1     |    |       |      |      |      |     |
| M = 20                                                               |            |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.137      | 0.197 | 0.277 | 0.424 | 0.569 |    |       |      |      |      |     |
| GLR-LR                                                               | 0.736      | 0.808 | 0.87  | 0.934 | 0.967 |    |       |      |      |      |     |
| Fisher                                                               | 0.578      | 0.672 | 0.762 | 0.861 | 0.923 |    |       |      |      |      |     |
| Wishart                                                              | 1          | 1     | 1     | 1     | 1     |    |       |      |      |      |     |
| M = 50                                                               |            |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.145      | 0.209 | 0.297 | 0.445 | 0.591 |    |       |      |      |      |     |
| GLR-LR                                                               | 0.992      | 0.996 | 1     | 1     | 1     |    |       |      |      |      |     |
| Fisher                                                               | 0.946      | 0.965 | 0.98  | 0.992 | 0.997 |    |       |      |      |      |     |
| Wishart                                                              | 1          | 1     | 1     | 1     | 1     |    |       |      |      |      |     |
| M = 100                                                              |            |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.154      | 0.207 | 0.290 | 0.445 | 0.591 |    |       |      |      |      |     |
| GLR-LR                                                               | 1          | 1     | 1     | 1     | 1     |    |       |      |      |      |     |
| Fisher                                                               | 0.998      | 0.999 | 1     | 1     | 1     |    |       |      |      |      |     |
| Wishart                                                              | 1          | 1     | 1     | 1     | 1     | α  | 0.005 | 0.01 | 0.02 | 0.05 | 0.1 |
| Statistics                                                           | σ 2 = 0.75 |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.1        | 0.153 | 0.226 | 0.368 | 0.512 |    |       |      |      |      |     |
| GLR-LR                                                               | 0.999      | 1     | 1     | 1     | 1     |    |       |      |      |      |     |
| Fisher                                                               | 0.925      | 0.95  | 0.97  | 0.987 | 0.944 |    |       |      |      |      |     |
| Wishart                                                              | 1          | 1     | 1     | 1     | 1     |    |       |      |      |      |     |
| σ 2 = 1                                                              |            |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.079      | 0.121 | 0.185 | 0.310 | 0.448 |    |       |      |      |      |     |
| GLR-LR                                                               | 0.995      | 0.998 | 0.999 | 1     | 1     |    |       |      |      |      |     |
| Fisher                                                               | 0.662      | 0.736 | 0.809 | 0.89  | 0.938 |    |       |      |      |      |     |
| Wishart                                                              | 1          | 1     | 1     | 1     | 1     |    |       |      |      |      |     |
| σ 2 = 5.5                                                            |            |       |       |       |       |    |       |      |      |      |     |
| GLR                                                                  | 0.008      | 0.019 | 0.037 | 0.083 | 0.152 |    |       |      |      |      |     |
| GLR-LR                                                               | 0.029      | 0.045 | 0.07  | 0.13  | 0.207 |    |       |      |      |      |     |
| Fisher                                                               | 0.008      | 0.015 | 0.029 | 0.07  | 0.133 |    |       |      |      |      |     |
| Wishart                                                              | 0.315      | 0.409 | 0.498 | 0.649 | 0.762 |    |       |      |      |      |     |
| Table V).                                                            |            |       |       |       |       |    |       |      |      |      |     |

the proposed Wishart statistic shows a significantly better performance as M is increasing. Second, while the GLR-LR statistic outperforms the Wishart one for low dimensions M
in the change of subspace scenario, the Wishart statistic still demonstrates a higher power compared to the Fisher and GLR statistics for both scenarios.

The next simulation in Table IV shows the evolution of the power for different values of the noise variance in the change of eigenvalues scenario (M = 100). The same can be done for the change of subspace scenario in Table V. We observe that the test statistics designed for a low-rank scenario
(Wishart, Fisher, GLR-LR) outperform the GLR in general.

Additionally, when the noise variance σ 2 becomes too large, the conditions on the SNR ensuring the consistency of these statistics (Assumption 3 and the conditions of [17]) are not met anymore, and one observes in that case a significant drop of the performance (σ 2 = 5.5 in Table IV and σ 2 = 2.5 in Remark 3. *In view of the simulations results described in* Tables II-V, we observe that the proposed test statistic (30)
performs poorly when the conditions described in Assumptions 1 and 3 are not met, i.e. when the dimension M *or the SNR are* not large enough. Scenarios where the rank K *is also of the* same order of magnitude than M*, thus violating Assumption* 1, will also invalidate Theorem 4 and the asymptotic type I
error will be poorly controlled in that case.

## C. An Application To Change Detection In Sar Images

In this section, we evaluate the performance of the proposed test statistic on images drawn from the UAV-SAR dataset of NASA/JPL-Caltech (SanAnd 26524 03, Segment 4). We consider two scenes with respective sizes 2360 × 600 and 2300 × 600 pixels, which have been previously used in [4],
[18], and which are formed of L = 2 images acquired within a 5 years interval (see Figures 1 and 2). The azimuthal TABLE V
POWER FOR DIFFERENT VALUES OF σ 2(CHANGE OF SUBSPACE SCENARIO)

| α          | 0.005      | 0.01   | 0.02   | 0.05   | 0.1   |
|------------|------------|--------|--------|--------|-------|
| Statistics | σ 2 = 0.75 |        |        |        |       |
| GLR        | 0.4        | 0.496  | 0.602  | 0.749  | 0.849 |
| GLR-LR     | 1          | 1      | 1      | 1      | 1     |
| Fisher     | 0.329      | 0.414  | 0.510  | 0.625  | 0.763 |
| Wishart    | 1          | 1      | 1      | 1      | 1     |
| σ 2 = 1    |            |        |        |        |       |
| GLR        | 0.172      | 0.246  | 0.34   | 0.505  | 0.646 |
| GLR-LR     | 1          | 1      | 1      | 1      | 1     |
| Fisher     | 0.077      | 0.119  | 0.18   | 0.297  | 0.424 |
| Wishart    | 1          | 1      | 1      | 1      | 1     |
| σ 2 = 2.5  |            |        |        |        |       |
| GLR        | 0.017      | 0.031  | 0.057  | 0.120  | 0.209 |
| GLR-LR     | 0.341      | 0.423  | 0.537  | 0.695  | 0.809 |
| Fisher     | 0.007      | 0.015  | 0.03   | 0.068  | 0.129 |
| Wishart    | 0.256      | 0.327  | 0.414  | 0.566  | 0.655 |

![7_image_2.png](7_image_2.png)

![7_image_0.png](7_image_0.png)

![7_image_1.png](7_image_1.png)

that is N1 = N2 = 25. In Figure 3, the ratio resolution is approximately 0.6 m while the distance resolution

![7_image_3.png](7_image_3.png)

is 1.67 m. The dimension of each pixel, which was initially of M = 3, has been increased to M = 12 using the wavelet decomposition technique of [29]. Local patches of sizes 5 × 5 centered around each pixel under test are used for estimation,

$$r(k)=\frac{\mathbb{E}\left[\sum_{i=1}^{k}\lambda_{i}\left(\hat{\mathbf{R}}_{1}\right)\right]}{\mathbb{E}\left[\text{tr}\left(\hat{\mathbf{R}}_{1}\right)\right]},\tag{57}$$

is plotted for both scenes, where the expectations are estimated by a sample mean over all the local patches. The rank K is set to 5 in the following to reach a ratio of r(K) ⪆ 95%.

In Figure 4 are plotted the ROC curves for scenes 1 and 2, where we have compared the performance of the proposed test statistic (30), the GLR, the GLR-LR and the method of [18].

We observe some improvement of the proposed test statistic for type I errors greater than 15% for the scene 1 or greater than 5% for the scene 2.

## Vi. Conclusion

In this paper, the problem of covariance equality testing in low-rank Gaussian models has been studied. A new test statistic has been proposed, which is based on the asymptotic behaviour of the largest eigenvalues of certain Wishart matrices in the high-dimensional regime where the dimension of the observations and the number of samples both converge to infinity at the same rate. In particular, it is shown that the proposed statistic has a controlled type I error in the highdimensional regime. Simulations on both synthetic and real datasets have demonstrated that the proposed test statistic is relevant compared to other alternative approaches.

## Appendix

Notations. Throughout this Appendix, we use the following notations. For a sequence of random matrices (Xn)n≥1, Xn = oP(1) denotes the convergence of (∥Xn∥2) to 0 in probability, while Xn = OP(1) denotes the tightness of
(∥Xn∥2), as n → ∞, where ∥.∥2 stands for the spectral norm.

If X is a random matrix, we denote by X◦ = X − E[X].

Finally, C
1(U) (resp. C∞
c
(U)) denotes the set of continuously differentiable functions (resp. infinitely differentiable functions with compact support) defined on an open set U.

A. Useful results around the Marcenko-Pastur distribution In this section, we provide well-known results on the Stieltjes transform

$$m(z)=\int_{\mathbb{R}}\frac{\mathrm{d}\mu(\lambda)}{\lambda-z},\quad z\in\mathbb{C}\backslash\mathbb{R},\tag{58}$$

of the Marcenko-Pastur distribution µ with parameters (σ 2, c)
defined in (15), having the interval [x
−, x+] as support with x
± = σ 2(1 ±
√c)
2, and which will be of constant use for the proofs of Theorems 1, 2 and Corollary 2 below.

We first recall that the limit m(x) = limz∈C+,z→x m(z) exists for all x ∈ R\{x
−, x+}, and that for all z ∈ C\{x
−, x+},
m(z) satisfies the equation:

$m(z)=\dfrac{1+\sigma^2cm(z)}{\sigma^2-z\left(1+\sigma^2cm(z)\right)}=\dfrac{w(z)}{z(\sigma^2-w(z))},$  b. 
2 − w(z)), (59)
with
$$w(z)=z\left(1+\sigma^{2}c m(z)\right).$$
Moreover, m is continuously differentiable on R\{0, x−, x+}.

We now provide some results on the function w, which plays a central role in describing the behaviour of the largest eigenvalues of Rˆ . From (59), we observe that for all z ∈ C\{x
−, x+},

$$\phi(w(z))=z,$$
where $\phi$ is defined as:
$$\phi(w)=w\left(1-\frac{\sigma^{2}c}{\sigma^{2}-w}\right).\tag{62}$$

Function ϕ is increasing on (−∞, w−) ∪ (w
+, ∞) and decreasing on (w
−, σ2) ∪ (σ 2, w+), with w
± = σ 2(1 ±
√c)
and ϕ(w
±) = x
±.

Next, we consider the following lemma (see [30]) regarding w.

Lemma 2. For all x ∈ R\{x
−, x+}, w(x) ∈ ϕ
−1({x}).

Moreover, among the preimages of x *under* ϕ,
- if x ∈ (x
−, x+), w(x) *is the unique one such that* Im(w(x)) > 0;
- if x ∈ R\ [x
−, x+], w(x) *is real and is the unique* preimage such that ϕ
′(w(x)) > 0.

Finally, z ∈ C\R *implies that* w(z) ∈ C\R.

Let γ ≥ 0. From Lemma 2, it is easily deduced that the equation w(x) = γ + σ 2admits a solution iff *γ > σ*2√c, and that the solution is unique and given by

$$(63)$$
 (64)  (65)  (66)  (67)  (68)  (69)  (69)
9
$$x=\phi(\gamma+\sigma^{2})=\frac{(\gamma+\sigma^{2})(\gamma+\sigma^{2}c)}{\gamma}.$$

Finally, we also have the following result giving various useful formulas. Define m˜ (z) = −1 z(1+σ2cm(z)) and τ (z) =
zm(z) ˜m(z).

  **Lemma 3**.: _If $\gamma>\sigma^{2}\sqrt{c}$, then we have_
  **3.**: _If $\gamma>\sigma$, then we have_  $$m(\phi(\gamma+\sigma^{2}))=-\frac{1}{\gamma+\sigma^{2}c},\tag{1}$$ $$\tilde{m}(\phi(\gamma+\sigma^{2}))=-\frac{1}{\gamma+\sigma^{2}},$$ (2) $$m^{\prime}(\phi(\gamma+\sigma^{2}))=\frac{\gamma^{2}}{(\gamma+\sigma^{2}c)^{2}(\gamma^{2}-\sigma^{4}c)},$$ $$\tilde{m}^{\prime}(\phi(\gamma+\sigma^{2}))=\frac{\gamma^{2}}{(\gamma+\sigma^{2})^{2}(\gamma^{2}-\sigma^{4}c)},$$ (3) $$\tau(\phi(\gamma+\sigma^{2}))=\frac{1}{\gamma},$$ (4) $$\tau^{\prime}(\phi(\gamma+\sigma^{2}))=-\frac{1}{\gamma^{2}-\sigma^{4}c}.$$
, (66)
, (67)
B. Proof of Theorem 1

$$(59)$$

This proof is based on techniques developed in [21].

1) Some notations: Denote by e1*, . . . ,* eN the column vectors of the standard basis of C

tors of the standard basis of $\mathbb{C}^{N}$, and let  $$\mathbf{J}_{1}=\sum_{n=1}^{N_{1}}\mathbf{e}_{n}\mathbf{e}_{n}^{*},\tag{1}$$  and for $\ell=2,\ldots,L$,  $$\mathbf{J}_{\ell}=\sum_{n=N_{1}+\ldots+N_{\ell-1}+1}^{N_{1}+\ldots+N_{\ell}}\mathbf{e}_{n}\mathbf{e}_{n}^{*}.\tag{2}$$  We also consider the following eigendecomposition of $\Gamma_{\ell}$:  $$\Gamma_{\ell}=\mathbf{U}_{\ell}\mathbf{D}_{\ell}\mathbf{U}_{\ell}^{*},\tag{3}$$
$$(70)$$
(71)  $\gamma_{\ell}$ .... 
$$(60)$$
$=\;\frac{1}{2}$
ℓ
with ${\bf U}_{\ell}$ a $M\times K$ isometric matrix and ${\bf D}_{\ell}={\rm diag}\,(\lambda_{1}({\bf\Gamma}_{\ell}),\ldots,\lambda_{K}({\bf\Gamma}_{\ell}))$.  2) _Linearization:_ Let ${\bf Y}$ be the $M\times N$ matrix given by ${\bf Y}=[{\bf y}_{1,1},\ldots,{\bf y}_{N,1},\ldots,{\bf y}_{1,L},\ldots,{\bf y}_{N_{L},L}]$. Due to the 
$$(61)$$
Gaussian model, one can assume, without loss of generality,
with U${}_{\ell}$ a $M\times K$ 1  diag ($\lambda_{1}(\Gamma_{\ell}),\ldots,\lambda_{K}(\Gamma_{\ell})$).  2) Linearization: Let Y by Y = [Y1,1, $\ldots,$, $\Psi_{N_{1}},1,\ldots,$]  Gaussian model $\alpha$ and $\alpha$
that
$$\mathbf{Y}=\mathbf{\Omega}\mathbf{S}^{*}+\mathbf{W},$$
$$(73)$$

Y = ΩS∗ + W, (73)
where $\mathbf{W}$ is $M\times N$ matrix with i.i.d. $\mathcal{N}_{\mathbb{C}}(0,\sigma^{2})$ entries and where $\mathbf{\Omega}=\left[\mathbf{U}\cdot\mathbf{D}^{\frac{1}{2}}\ldots\mathbf{U}\cdot\mathbf{D}^{\frac{1}{2}}\right]$ and $\mathbf{S}=\left[\mathbf{S}\cdot\ldots\mathbf{S}\cdot\mathbf{I}\right]$ with 
where Ω =
hU1D
1
, . . . , ULD
L
iand S = [S1*, . . . ,* SL]. with Sℓ = JℓX and X a N × K matrix with i.i.d. NC(0, 1) entries and independent of W. In particular, we have Rˆ =
1 N YY∗,
and Y is a fixed rank (at most KL) perturbation of W so that from *Weyl's* inequality and the classical results on the extreme eigenvalues of *Wishart* matrices (see e.g. [31]), it holds that

$$\lambda_{M}(\hat{\bf R})\stackrel{{a.s.}}{{\longrightarrow}}x^{-},\tag{74}$$

while *a.s.*

$$\lim_{M\to\infty}\lambda_{KL+1}\left(\hat{\mathbf{R}}\right)\leq\limsup_{M\to\infty}\lambda_{1}\left(\frac{1}{N}\mathbf{W}\mathbf{W}^{*}\right)=x^{+}.\tag{75}$$

To study the remaining eigenvalues of Rˆ , we use the linearization trick which consists in studying the following Hermitian

block matrix  $$\tilde{\mathbf{Y}}=\begin{bmatrix}\mathbf{0}&\frac{1}{\sqrt{N}}\mathbf{Y}\\ \frac{1}{\sqrt{N}}\mathbf{Y}^{*}&\mathbf{0}\end{bmatrix},$$  for which it is well-known that [32, Th. 7.3.7]
, (76)
$$\operatorname{sp}\left({\dot{\mathbf{Y}}}\right)=\left\{{\pm{\sqrt{\lambda_{k}\left({\hat{\mathbf{R}}}\right)}}}\right\}\cup\{0\}.$$
3) Asymptotics for the characteristic polynomial of Yˇ :
Obviously, we have:

$${\dot{\mathbf{Y}}}=\mathbf{B}{\dot{\mathbf{I}}}\mathbf{B}^{*}+{\dot{\mathbf{W}}},$$
Yˇ = BˇIB∗ + Wˇ , (78)
where B,
ˇI and Wˇ are given by:

$$\mathbf{B}=\begin{bmatrix}\mathbf{\Omega}&\mathbf{0}\\ \mathbf{0}&\frac{1}{\sqrt{N}}\mathbf{S}\end{bmatrix},\mathbf{i}=\begin{bmatrix}\mathbf{0}&\mathbf{I}\\ \mathbf{I}&\mathbf{0}\end{bmatrix},\mathbf{\tilde{W}}=\begin{bmatrix}\mathbf{0}&\frac{1}{\sqrt{N}}\mathbf{W}\\ \frac{1}{\sqrt{N}}\mathbf{W}^{*}&\mathbf{0}\end{bmatrix}.\tag{79}$$  Let $\epsilon>0$ and let $\mathcal{D}_{\epsilon}$ the $\epsilon$-neighborhood in $\mathbb{C}$ of the set $\mathcal{D}=\mathbb{C}$
[x
−, x+]. Let K be a compact subset of C\ (Dϵ ∪ (−∞, 0)).

Then (see again [31]), with probability one for all large M,

$$\operatorname{sp}\left({\tilde{\mathbf{W}}}\right)\cap\left\{{\sqrt{z}}:z\in{\mathcal{K}}\right\}=\varnothing,$$

and the following factorization

$$\operatorname*{det}\left({\dot{\mathbf{Y}}}-{\sqrt{z}}\mathbf{I}\right)=\operatorname*{det}\left({\dot{\mathbf{W}}}-{\sqrt{z}}\mathbf{I}\right)\operatorname*{det}\left({\dot{\mathbf{I}}}\right){\dot{P}}(z),$$

where
$$\hat{P}(z)=\operatorname*{det}\left(\hat{\mathbf{I}}+\hat{\Xi}(z)\right),$$
, (82)
and Ξˆ (z) = B∗Wˇ −
√zI−1B, holds for all z ∈ K. Then from the block matrix inversion formula, we have

$$\hat{\Xi}(z)=\left[\begin{array}{cc}\sqrt{z}\Omega^{*}{\bf Q}(z)\Omega&\frac{1}{N}\Omega^{*}{\bf Q}(z){\bf WS}\\ \frac{1}{N}{\bf S}^{*}{\bf W}^{*}{\bf Q}(z)\Omega&\sqrt{z}\frac{1}{N}{\bf S}^{*}\hat{\bf Q}(z){\bf S}\end{array}\right],\tag{83}$$

where Q(z) and Q˜ (z) are the resolvent matrices of 1NWW∗
and 1NW∗W given by

$${\bf Q}(z)=\left(\frac{1}{N}{\bf W}{\bf W}^{*}-z{\bf I}\right)^{-1},\ \tilde{\bf Q}(z)=\left(\frac{1}{N}{\bf W}^{*}{\bf W}-z{\bf I}\right)^{-1}.\tag{84}$$  We then use the following result.  
Proposition 1. *We have*

sup
z∈K
∥Ω
∗Q(z)Ω − m(z)Ω
$$\cdot\left.m(z)\Omega^{*}\Omega\right|_{2}\,\frac{a.s.}{M\!\rightarrow\!\infty}$$
0, (85)
as well as

as well as_  $$\sup_{z\in\mathcal{K}}\left\|\frac{1}{N}\mathbf{S}_{k}^{*}\bar{\mathbf{Q}}(z)\mathbf{S}_{\ell}+\frac{\delta_{k-\ell}\frac{N_{k}}{N}}{z\left(1+\sigma^{2}cm(z)\right)}\mathbf{I}\right\|_{2}\xrightarrow[M\to\infty]{a.s.}0,\tag{86}$$  _and_  $$\sup_{z\in\mathcal{K}}\left\|\frac{1}{N}\mathbf{S}_{k}^{*}\mathbf{W}^{*}\mathbf{Q}(z)\mathbf{\Omega}\right\|_{2}\xrightarrow[M\to\infty]{a.s.}0.\tag{87}$$
Proof. Proposition 1 is obtained as a trivial modification of standard results in random matrix theory regarding quadratic forms of resolvents of standard Wishart matrices (see e.g. [33, Sec. 5.5]) and the proof is therefore omitted.

Using Proposition 1, we deduce that:

$$\operatorname*{sup}_{z\in K}\left\|{\hat{\Xi}}(z)-{\Xi}(z)\right\|_{2}\,{\xrightarrow[M\to\infty]{a.s.}}0,$$
0, (88)
$$(76)$$
$${\mathrm{where}}$$
$$\Xi(z)=\left[\begin{array}{c c}{{\sqrt{z}m(z)\Omega^{*}\Omega}}&{{\mathbf{0}}}\\ {{\mathbf{0}}}&{{\mathbf{A}(z)}}\end{array}\right],$$
, (89)
$$(77)$$
$$\mathrm{with}$$

with A(z) the KL × KL block diagonal matrix given by

$${\bf A}(z)=-\frac{1}{\sqrt{z}\left(1+\sigma^{2}c m(z)\right)}\left[\begin{array}{cccc}\frac{N_{1}}{N}{\bf I}&&&\\ &\ddots&&\\ &&&\frac{N_{L}}{N}{\bf I}\end{array}\right].\tag{90}$$
$$(88)$$

It is straightforward to check that

$$\det\left(\tilde{\mathbf{I}}+\mathbf{\Xi}(z)\right)=\det\left(\sqrt{z}m(z)\mathbf{\Omega}^{*}\mathbf{\Omega}\mathbf{\Lambda}(z)-\mathbf{I}\right)$$ $$=\det\left(-\frac{m(z)}{1+\sigma^{2}cm(z)}\mathbf{\Gamma}-\mathbf{I}\right),\tag{91}$$

where Γ is defined in (11). Consequently, from Assumption
2, one has
$$\sup_{z\in\mathcal{K}}\left|\hat{P}(z)-P(z)\right|\xrightarrow[N\to\infty]{a.s.}0,$$  $$P(z)=\prod_{k=1}^{KL}\Big{(}-\frac{m(z)}{1+\sigma^{2}cm(z)}\gamma_{k}-1\Big{)}.\qed$$
0, (92)
$$(80)$$
$$(81)$$
. Using the equation (59), one can rewrite P(z) as P(z) =
QKL
k=1 γk w(z)−σ2 − 1
, with w defined in (60).

4) Spectrum of Rˆ : Using Lemma 2 and the discussion below, we immediately obtain that the set of zeros of P is given by

$$(82)$$
$${\cal Z}=\left\{\phi(\gamma_{k}+\sigma^{2}):k=1,\ldots,KL,\ \gamma_{k}>\sigma^{2}\sqrt{c}\right\}.\tag{93}$$

Moreover, Lemma 2 also implies that P has no pole and thus P is holomorphic on C\[x
−, x+].

Let Q = |Z| and denote by x1 *> . . . > x*Q the elements of Z. We also set ϵ > 0 small enough such that

$$\begin{array}{c}\includegraphics[width=140.0pt]{28.45}\end{array}\tag{94}$$

For all q = 1*, . . . , Q*, let Cq be a continuously differentiable simple closed curve intersecting the real axis only at the two points xq ± ϵ and enclosing xq so that Cq is a compact subset of C\ (Dϵ ∪ (−∞, 0)). Applying (92) with K = Cq provides that with probability one for all large M,

$$\left|\hat{P}(z)-P(z)\right|<\left|P(z)\right|,\tag{95}$$

for all z ∈ Cq, with both Pˆ and P being holomorphic on any open set enclosed by Cq. Thus, for all q = 1*, . . . , Q*, we deduce from Rouche's Theorem that ´ Pˆ admits a unique zero in the interval [xq − *ϵ, x*q + ϵ]. With a similar reasoning, Pˆ does not have any zero in (0, x− − ϵ) ∪ (x1 + ϵ, ∞) with probability one for all large M. Therefore, getting back to (81) and since ϵ can be made arbitrarily small, it follows that

11
$$\lambda_{k}\left(\hat{\mathbf{R}}\right)\xrightarrow[M\to\infty]{a.s.}\phi(\gamma_{k}+\sigma^{2})=\frac{(\gamma_{k}+\sigma^{2})(\gamma_{k}+\sigma^{2}c)}{\gamma_{k}},\tag{96}$$  for all $k=1,\ldots,KL$ such that $\gamma_{k}>\sigma^{2}\sqrt{c}$. Moreover,
with probability one for all large M, λk(Rˆ ) ∈ Dϵ for all k = 1*, . . . , KL* such that γk ≤ σ 2√c. Since the empirical spectral distribution µˆ of Rˆ converges a.s. to the MarcenkoPastur distribution as M → ∞, this further implies that for all k = 1*, . . . , KL* such that γk ≤ σ 2√c, λk Rˆa.s. *−−−−→*
M→∞
x
+

an $k=1,\ldots,KL$ such that $\frac{1}{lk}\leq0$, $\forall\,\epsilon,\,\lambda_{k}\left(\mathbf{R}\right)$ and similarly $\lambda_{KL+1}\left(\hat{\mathbf{R}}\right)\xrightarrow[M\to\infty]{a.s.}x^{+}$.  
C. Proof of Theorem 2 1) Some notations.: Let us first recall that under hypothesis H0, we have Γ1 = *. . .* = ΓL = Γ, and we denote by Γ = UDU∗its eigendecomposition with U a M × K
isometric matrix and D = diag (λ1(Γ)*, . . . , λ*K(Γ)). To unify some notations, define as in the previous section Yℓ =
[y1,ℓ*, . . . ,* yNℓ,ℓ] for all ℓ = 1*, . . . , L* so that we have Yℓ = ΩS∗
ℓ + Wℓ, (97)
where Ω = UD1/2, S1*, . . . ,* SL are independent matrices such that Sℓ = [s1,ℓ, . . . , sK,ℓ] is Nℓ × K with i.i.d. NC(0, 1)
entries, and where W1*, . . . ,*WL are independent matrices with Wℓ having i.i.d. NC(0, σ2) entries. We also define Y0 = [Y1*, . . . ,* YL] so that

$${\bf Y}_{0}=\Omega{\bf S}_{0}^{*}+{\bf W}_{0},\tag{98}$$  with ${\bf S}_{0}=[{\bf S}_{1}^{*},\ldots,{\bf S}_{L}^{*}]^{*}$ and ${\bf W}_{0}=[{\bf W}_{1},\ldots,{\bf W}_{L}]$, and write $N_{0}=N_{1}+\ldots+N_{L}$, so that $\hat{\bf R}_{0}=\frac{{\bf Y}_{0}{\bf Y}_{0}^{*}}{N_{0}}=\hat{\bf R}$. Moreover, let $c_{0}=c=(\frac{1}{c_{1}}+\ldots+\frac{1}{c_{L}})^{-1}$ and 
$$a=\sigma^{2}\min_{\ell=0,...,L}\left(1-\sqrt{c_{\ell}}\right)^{2},\quad b=\sigma^{2}\max_{\ell=0,...,L}\left(1+\sqrt{c_{\ell}}\right)^{2},\tag{99}$$  and consider $\varphi\in\mathcal{C}_{\alpha}^{\infty}(\mathbb{R})$ such that $\mathrm{supp}(\varphi)=[a-\epsilon,b+\epsilon]$
c
and φ(t) = 1 for all t ∈-a −
ϵ
2
, b +
ϵ
2
, where *ϵ < a* . The
following quantity defined as
$$\chi=\prod_{\ell=0}^{L}\mathrm{det}\varphi\left(\frac{\mathbf{W}_{\ell}\mathbf{W}_{\ell}^{*}}{N_{\ell}}\right),\tag{100}$$

verifies χ = 1 with probability 1 for all large M from the classical results on the localization of the eigenvalues of Wishart matrices [31]. Recall also the definition of m and w in
(58) and (60) respectively and denote for all ℓ = 0*, . . . , L* by mℓ the *Stieltjes* transform of the *Marcenko-Pastur* distribution with parameter (cℓ, σ2), as well as for all z ∈ C\[x
−
ℓ
, x+
ℓ
]

$$\begin{aligned} w_{\ell}(z)&=z\left(1+\sigma^{2}c_{\ell}m_{\ell}(z)\right),\\ \tilde{m}_{\ell}(z)&=-\frac{1}{z(1+\sigma^{2}c_{\ell}m_{\ell}(z))},\\ \tau_{\ell}(z)&=z m_{\ell}(z)\tilde{m}(z), \end{aligned}$$ with $x_{\ell}^{\pm}=\sigma^{2}\left(1\pm\sqrt{c_{\ell}}\right)^{2}$. 
2) Characteristic Polynomials Approximation: The first step of the proof consists in using the trick from [34] whose main idea is to relate the cumulative distribution function of the spiked eigenvalues with the determinant of certain random matrices.

Using Theorem 1 and the same arguments used to obtain the factorization (81) and (83) in Appendix B, we have that λ1(Rˆℓ)*, . . . , λ*K(Rˆℓ) are the zeros of

$$\hat{P}_{\ell}(z)=\operatorname*{det}\left(\hat{\mathbf{I}}+\hat{\Xi}_{\ell}(z)\right),$$

, (104)
for all ℓ ∈ {0*, . . . , L*}, with probability one for all large M,
with

Ξˆℓ(z) = " √zΩ ∗Qℓ(z)Ωχ1 Nℓ Ω ∗Qℓ(z)WℓSℓχ 1 Nℓ S ∗ ℓW∗ ℓQℓ(z)Ωχ √z 1 Nℓ S ∗ ℓQ˜ℓ(z)Sℓχ # , (105) where Qℓ(z) = WℓW∗ ℓ Nℓ− zI −1and Q˜ℓ(z) = W∗ ℓWℓ Nℓ− zI −1. For all ℓ, k, let −∞ < xk,ℓ < yk,ℓ < +∞ and denote ρk,ℓ = (γk + σ 2)(γk + σ 2cℓ) γk. (106) Then with probability one for all large M, we have
$$(104)$$
$$\sqrt{M}\left(\lambda_{k}(\hat{\mathbf{R}}_{\ell})-\rho_{k,\ell}\right)\in[x_{k,\ell},y_{k,\ell}]$$ $$\Leftrightarrow\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x_{k,\ell}}{\sqrt{M}}\right)\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{y_{k,\ell}}{\sqrt{M}}\right)<0.\tag{107}$$  Therefore, as $M\rightarrow\infty$,
$$\mathbb{P}\left(\bigcap_{k=1}^{K}\bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}(\widehat{\mathbf{R}}_{\ell})-\rho_{k,\ell}\right)\in[x_{k,\ell},y_{k,\ell}]\right\}\right)=$$ $$\mathbb{P}\left(\bigcap_{k=1}^{K}\bigcap_{\ell=0}^{L}\left\{\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x_{k,\ell}}{\sqrt{M}}\right)\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{y_{k,\ell}}{\sqrt{M}}\right)<0\right\}\right)$$ $$\quad+o(1).\tag{108}$$  The following proposition provides the expression of 
The following proposition provides the expansion of Pˆℓ ρk,ℓ + √xM
around ρk,ℓ.

Proposition 2. *For all* x ∈ R,
$$\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)=\frac{1}{\sqrt{M}}\prod_{i\neq k}\left(\gamma_{i}\tau_{\ell}(\rho_{k,\ell})-1\right)$$ $$\times\left(x\gamma_{k}\tau_{\ell}^{\prime}(\rho_{k,\ell})-2\sqrt{\gamma_{k}}\text{Re}\left(\eta_{3,k,\ell}\right)+\gamma_{k}\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})\eta_{1,k,\ell}\right.$$ $$\left.+\left.\gamma_{k}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\eta_{2,k,\ell}\right)\right)+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),\tag{109}$$  _where $\tau_{\ell}(z)=zm_{\ell}(z)\tilde{m}_{\ell}(z)$ and_
$$(101)$$
$$\binom{102}{103}$$
$$\eta_{1,k,\ell}=\sqrt{M}\mathbf{u}_{k}^{*}\left(\mathbf{Q}_{\ell}(\rho_{k,\ell})\chi\right)^{\circ}\mathbf{u}_{k},\tag{110}$$ $$\eta_{2,k,\ell}=\frac{\sqrt{M}}{N_{\ell}}\left(\mathbf{s}_{k,\ell}^{*}\mathbf{\hat{Q}}_{\ell}(\rho_{k,\ell})\mathbf{s}_{k,\ell}\chi\right)^{\circ},$$ (111) $$\eta_{3,k,\ell}=\frac{\sqrt{M}}{N_{\ell}}\mathbf{u}_{k}^{*}\mathbf{Q}_{\ell}(\rho_{k,\ell})\mathbf{W}_{\ell}\mathbf{s}_{k,\ell}\chi.\tag{112}$$  Proof.: The proof is deferred to Appendix E1.  
From (108) and Proposition 2, it is clear that we have to study a CLT for the following generic quantity

$$\eta=\sum_{\ell=0}^{L}\sum_{k=1}^{K}\left(\beta_{1,k,\ell}\eta_{1,k,\ell}+\beta_{2,k,\ell}\eta_{2,k,\ell}+\text{Re}\left(\overline{\beta_{3,k,\ell}}\eta_{3,k,\ell}\right)\right),\tag{113}$$  where $\left(\beta_{i,k,\ell}\right)_{\begin{array}{c}i=1,2\\ k=1,...,K\\ \ell=0,...,L\end{array}}\in\mathbb{R}^{2K(L+1)}$ and $\left(\beta_{3,k,\ell}\right)_{\begin{array}{c}k=1,...,K\\ \ell=0,...,L\end{array}}\in\mathbb{C}^{K(L+1)}$.  
3) Central Limit Theorem: Let us consider the characteristic function Ψ(u) = E [ξ(u)], with ξ(u) = exp (iuη). Our approach consists in deriving a perturbed differential equation for Ψ as shown in the following proposition. Let bdiag() denotes the block diagonal operator. Define K = bdiag (K1*, . . . ,* KK) with Kk = bdiag(K1,k*, . . . ,* K4,k) and where (Ki,k)i=1*,...,*4 are (L + 1) × (L + 1) symmetric matrices with entries given by

$\begin{array}{l}\left[\mathbf{K}_{1,k}\right]\ell+1,\ell'+1=\\ \left\{\frac{\sigma^4c_\ell}{(\gamma_k+\sigma^2c_\ell)^2(\gamma_k^2-\sigma^4c_\ell)}\right.\\ \\ \left.\frac{\sigma^4c_0}{(\gamma_k+\sigma^2c_0)(\gamma_k+\sigma^2c_\ell,)(\gamma_k^2-\sigma^4c_0)}\right.\\ \\ \left.0\right.\end{array}$
k−σ4cℓ)if ℓ = ℓ
if $ \ell=\ell'$  if $ \ell=0<\ell'$ ,      (114)  if $ 0<\ell<\ell'$  ... 
k−σ4c0)if ℓ = 0 < ℓ′
0 if 0 *< ℓ < ℓ*′
$$[{\bf K}_{2,k}]\ell+1,\ell^{\prime}+1=\begin{cases}\frac{c_{\ell}}{(\gamma_{k}+\sigma^{2})^{2}(\gamma_{k}^{2}-\sigma^{4}c_{\ell})}&\text{if}\ell=\ell^{\prime}\\ \frac{c_{0}}{(\gamma_{k}+\sigma^{2})^{2}(\gamma_{k}^{2}-\sigma^{4}c_{0})}&\text{if}\ell=0<\ell^{\prime}\,\\ 0&\text{if}0<\ell<\ell^{\prime}\end{cases}\tag{115}$$
and for $i\in\{3,4\}$,  $$[{\bf K}_{i,k}]_{\ell+1,\ell^{\prime}+1}=\begin{cases}\frac{1}{2}\frac{\sigma^{2}c_{\ell}}{\gamma_{k}^{2}-\sigma^{4}c_{\ell}}&\text{if}\ell=\ell^{\prime}\\ \\ \frac{1}{2}\frac{\sigma^{2}c_{0}}{\gamma_{k}^{2}-\sigma^{4}c_{0}}&\text{if}\ell=0<\ell^{\prime}\\ \\ 0&\text{if}0<\ell<\ell^{\prime}\end{cases}\tag{116}$$  Denote also $\boldsymbol{\beta}=\left(\boldsymbol{\beta}_{1}^{T},\ldots,\boldsymbol{\beta}_{K}^{T}\right)^{T}$ with 
$$\beta_{k}=\left(\beta_{1,k,0},\ldots,\beta_{1,k,L},\beta_{2,k,0},\ldots,\beta_{2,k,L},\right.$$ $$\left.\mathrm{Re}(\beta_{3,k,0}),\ldots,\mathrm{Re}(\beta_{3,k,L}),\mathrm{Im}(\beta_{3,k,0}),\ldots,\mathrm{Im}(\beta_{3,k,L})\right)^{T}.\tag{117}$$
Proposition 3. The matrix K *is positive definite and*

$$\Psi^{\prime}(u)=-u\beta^{T}\mathbf{K}\beta\Psi(u)+{\frac{\Delta(u)}{\sqrt{M}}},$$
, (118)
where ∆ *is a continuous function such that* |∆(u)| < P(u)
for some polynomial P with positive coefficients independent of M.

Proof. The proof is deferred to Appendix E2.

From Proposition 3, by solving the perturbed differential equation in (118), we deduce that

$$\Psi(u)\xrightarrow[M\to\infty]{}\exp\left(-\beta^{T}{\bf K}\beta\frac{u^{2}}{2}\right),$$  which of course implies that  $$\eta\xrightarrow[M\to\infty]{}\mathcal{N}_{\mathbb{R}}\left(0,\beta^{T}{\bf K}\beta\right).$$
, (119)
. (120)
The final step of the proof consists in transferring the CLT to the K largest eigenvalues of (Rˆℓ)ℓ=1*,...,L*. From Proposition

(2), we have that:  $$\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)=$$ $$\frac{1}{\sqrt{M}}\gamma_{k}\tau^{\prime}_{\ell}(\rho_{k,\ell})\left(x-\zeta_{k,\ell}+o_{\mathbb{P}}\left(1\right)\right)\prod_{i\neq k}\left(\gamma_{i}\tau_{\ell}(\rho_{k,\ell})-1\right),\tag{121}$$  with
with  $$\zeta_{k,\ell}=\frac{1}{\gamma_{k}\,\tau_{\ell}^{\prime}(\rho_{k,\ell})}\Big{(}2\sqrt{\gamma_{k}}\text{Re}\,(\eta_{3,k,\ell})-\gamma_{k}\rho_{k,\ell}\bar{m}_{\ell}(\rho_{k,\ell})\eta_{1,k,\ell}\tag{122}$$ $$-\gamma_{k}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\eta_{2,k,\ell}\Big{)}.$$  Thus, going back to (108), we get 
$$\mathbb{P}\left(\bigcap_{k=1}^{K}\bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}(\hat{\mathbf{R}}_{\ell})-\rho_{k,\ell}\right)\in[x_{k,\ell},y_{k,\ell}]\right\}\right)=$$ $$\mathbb{P}\left(\bigcap_{k=1}^{K}\bigcap_{\ell=0}^{L}\left\{x_{k,\ell}<\zeta_{k,\ell}+o_{\mathbb{P}}(1)<y_{k,\ell}\right\}\right)+o(1).\tag{123}$$  Using (120) with suitable values for $\beta$ as well as the equal 
Using (120) with suitable values for β as well as the equalities of Lemma 3, we have ζ = (ζk,ℓ) ℓ=0,...,L
k=1*,...,K*
D
−−−−→
M→∞
NRK(L+1) (0, Θ), where Θ is given in the statement of Theorem 2. Finally, noticing that

  **Lemma 2.** Finally, noticing that  $$\det(\mathbf{\Theta})=\prod_{k=1}^{K}\prod_{\ell=1}^{L}\theta_{k,\ell}^{2}\left(\theta_{0}^{2}-\sum_{\ell^{\prime}=1}^{L}\frac{\vartheta_{k,\ell^{\prime}}^{2}}{\theta_{k,\ell}^{2}}\right)$$ $$=\left(\sigma^{4}c_{0}^{2}(L-1)\right)^{K}\prod_{k=1}^{K}\left(\frac{\gamma_{k}+\sigma^{2}}{\gamma_{k}}\right)^{2(L+1)}$$ $$\quad\times\prod_{\ell=1}^{L}c_{\ell}(\gamma_{k}^{2}-\sigma^{4}c_{\ell}),\tag{124}$$  $\bullet$\(\
we obtain that det(Θ) > 0 thanks to Assumption 3 which concludes the proof of Theorem 2.

D. Proof of Corollary 2

$$(118)$$

Denote c0 = c and for all ℓ = 0*, . . . , L*, let ϕˆℓ(w) =
w 1 −
σˆ
2cℓ σˆ
2−w
. Denote as well Rˆ0 = Rˆ and γˆk,0 = ˆγk for ease of reading. Under Assumption 3, we first observe from Theorem 1 that

$$\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\xrightarrow[M\to\infty]{a.s.}\phi_{\ell}(\gamma_{k}+\sigma^{2})=\frac{(\gamma_{k}+\sigma^{2})(\gamma_{k}+\sigma^{2}c_{\ell})}{\gamma_{k}},\tag{125}$$
$$(119)$$  $$(120)$$

so that λˆk(Rˆℓ) > σˆ
2√cℓ with probability one for all large M,
and therefore γˆk,ℓ + ˆσ 2coincides with the largest solution to the equation ϕˆℓ(w) = λk(Rˆℓ). From Lemma 2, we deduce that γˆk,ℓ = ˆwℓ λˆk(Rˆℓ)
− σˆ
2. with probability one for all large M, where wˆℓ(z) = z1 + ˆσ 2cℓmˆ ℓ(z)with mˆ ℓ the Stieltjes transform of the Marcenko-Pastur distribution with parameter
(ˆσ 2, cℓ). It is easy to see that σˆ
2 = σ 2 + OP
1M
and:

$$\hat{m}_{\ell}\left(\hat{\lambda}_{k}(\hat{\mathbf{R}}_{\ell})\right)=m_{\ell}\left(\hat{\lambda}_{k}(\hat{\mathbf{R}}_{\ell})\right)+{\mathcal O}_{\mathbb{P}}\left({\frac{1}{M}}\right).$$
. (126)
Therefore, we deduce that

$$\hat{\gamma}_{k,\ell}=w_{\ell}\left(\hat{\lambda}_{k}(\hat{\mathbf{R}}_{\ell})\right)-\sigma^{2}+{\mathcal{O}}_{\mathbb{P}}\left({\frac{1}{M}}\right).$$
. (127)
As wℓ(ϕℓ(γk+σ
2)) = γk+σ
2and wℓ is differentiable at point
γk + σ
2, a straightforward use of the delta-method provides
$$\sqrt{M}\left(\hat{\gamma}_{k,\ell}-\gamma_{k}\right)_{\begin{subarray}{c}\ell=0,...,L\\ k=1,...,K\end{subarray}}\xrightarrow[M\to\infty]{\mathcal{D}}\mathcal{N}_{\mathbb{R}^{K(L+1)}}\left(\mathbf{0},\mathbf{G}\mathbf{G}\right),\tag{1}$$
$${\vec{\mathbf{r}}})\,,$$
where ${\bf G}={\rm diag}\left(\left(w^{\prime}_{\ell}(\phi_{\ell}(\gamma_{k}+\sigma^{2}))\right)_{\ell=0,...,L}\right)$. Noticting that $w^{\prime}_{\ell}(\phi_{\ell}(\gamma_{k}+\sigma^{2}))=\frac{\gamma_{k}^{2}}{\gamma_{k}^{2}-\sigma^{2}c_{\ell}}$ from Lemma 3, we end 
up with GΘG = Ω, where Ω is given in the statement of Corollary 2. Another immediate use of the delta-method allows to transfer the CLT from (ˆγk,ℓ) ℓ=0,...,L
k=1*,...,K*
to γˆ.

E. Additional proofs 1) Proof of Proposition 2: It is easy to see using Proposition 1 that for all x ∈ R,

tion 1 that for all $\varepsilon>0$,  $$\hat{\Xi}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)=$$ $$\left[\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell})\mathbf{D}\right.\left.\mathbf{0}\right]+\mathbf{\Delta},$$ $$\left.\mathbf{0}\right.\left.\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}\right]+\mathbf{\Delta},\tag{129}$$  where
∆ = "√ρk,ℓΩ ∗(Qℓ(ρk,ℓ)χ) ◦ Ω 1 Nℓ Ω ∗Qℓ(ρk,ℓ)χWℓSℓ 1 Nℓ S ∗ ℓW∗ ℓQℓ(ρk,ℓ)χΩ√ρk,ℓ 1 Nℓ S ∗ ℓQ˜ℓ(ρk,ℓ)Sℓχ ◦ # +x √M h (ρk,ℓ) D 0 0 h˜ (ρk,ℓ) I + oP 1 √M , (130) with hℓ(z) = mℓ(z) 2 √z + √zm′ℓ (z) and h˜ℓ(z) = m˜ ℓ(z) 2 √z + √zm˜ ′ ℓ (z). Note that ∥∆∥2 = OP √ 1 M and we also consider the partition ∆ = (∆i,j )i,j=1,2 where each block ∆i,j is
K×K. Consider the event A =∥∆2,2∥2 <
√ρk,ℓm˜ ℓ(ρk,ℓ)	.
From the block matrix determinant formula, we have:
$$\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)\mathbb{1}_{\mathcal{A}}=\Phi\,\det\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}+\mathbf{\Delta}_{2,2}\right)\mathbb{1}_{\mathcal{A}},\tag{131}$$
$${}_{2})\ 1_{A},$$ $$(131)$$
with

$$\Phi=\det\biggl{(}\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell}){\bf D}+\mathbf{\Delta}_{1,1}$$ $$-({\bf I}+\mathbf{\Delta}_{2,1})\left(\sqrt{\rho}_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell}){\bf I}+\mathbf{\Delta}_{2,2}\right)^{-1}({\bf I}+\mathbf{\Delta}_{1,2})\biggr{)}\mathds{1}_{\mathcal{A}}.\tag{132}$$
Moreover,  $$\left(\sqrt{\rho}_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}+\boldsymbol{\Delta}_{2,2}\right)^{-1}\mathds{1}_{\mathcal{A}}=$$ $$\left(\frac{\mathbf{I}}{\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})}}-\frac{\boldsymbol{\Delta}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\right)\mathds{1}_{\mathcal{A}}+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),\tag{133}$$  which yields
$$(126)$$
$$(127)$$
$$\Phi=\det\Biggl{(}\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell})\mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell}))}+\mathbf{\Delta}_{1,1}$$ $$\quad-\frac{\mathbf{\Delta}_{1,2}+\mathbf{\Delta}_{2,1}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}+\frac{\mathbf{\Delta}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\Biggr{)}\mathds{1}_{\mathcal{A}}+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right).\tag{134}$$

Since D = diag(γ1*, . . . , γ*K) + o
* [10] M. C.  
from Assumption 2,
and from Lemma 3, we have
and from Lemma 3, we have  $$\det\left(\sqrt{\rho_{k,\ell}m_{\ell}}(\rho_{k,\ell})\mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}}(\rho_{k,\ell})}\right)=o\left(\frac{1}{\sqrt{M}}\right).\tag{135}$$
Using the differential of the determinant, we further have

Using the differential of the determinant, we further have  $$\Phi=\mathrm{tr}\Bigg{[}\mathrm{com}\left(\sqrt{\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})}\mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})}}\right)^{T}$$ $$\quad\times\left(\boldsymbol{\Delta}_{1,1}-\frac{\boldsymbol{\Delta}_{1,2}+\boldsymbol{\Delta}_{2,1}}{\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})}}+\frac{\boldsymbol{\Delta}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\right)\Bigg{]}\mathds{1}_{\mathcal{A}}$$ $$\quad+o_{\mathrm{P}}\left(\frac{1}{\sqrt{M}}\right),\tag{136}$$  where $\mathrm{com}()$ denotes the comatrix operation. A direct com
where com() denotes the comatrix operation. A direct computation together with Assumption 2 provides
$$\ln\left(\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell})\mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}\right)=$$ $$\frac{\prod_{i\neq k}\left(\gamma_{i}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\tilde{m}_{\ell}(\rho_{k,\ell})-1\right)}{\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\right)^{K-1}}\mathbf{e}_{k}\mathbf{e}_{k}^{*}+o\left(\frac{1}{\sqrt{M}}\right).\tag{137}$$  $\mathbf{e}_{k}$
$$\mathrm{com}$$
Consequently,  $$\Phi=o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)+\frac{\prod_{i\neq k}\left(\gamma_{i}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\tilde{m}_{\ell}(\rho_{k,\ell})-1\right)}{(\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})})^{K-1}}$$ $$\times\left[\mathbf{\Delta}_{1,1}-\frac{\mathbf{\Delta}_{1,2}+\mathbf{\Delta}_{2,1}}{\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})}}+\frac{\mathbf{\Delta}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\right]_{k,k}\mathbbm{1}_{\mathcal{A}}.\tag{138}$$  In the same way,
det √ρk,ℓm˜ ℓ(ρk,ℓ)I + ∆2,2
=

$$\left(\sqrt{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})}\right)^{K}+{\cal O}_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),\tag{139}$$
so that  $$\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)\mathbb{1}_{\mathcal{A}}=$$ $$\left[\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{\Delta}_{1,1}+\frac{\mathbf{\Delta}_{2,2}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}-(\mathbf{\Delta}_{1,2}+\mathbf{\Delta}_{2,1})\right]_{k,\ell}$$ $$\times\prod_{i\neq k}\left(\gamma_{i}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\tilde{m}_{\ell}(\rho_{k,\ell})-1\right)+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right).\tag{140}$$
Since $\mathds{1}_{\mathcal{A}}=1+o_{\mathbb{P}}(1)$, we also deduce that  $$\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)\mathds{1}_{\mathcal{A}^{c}}=o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),\tag{141}$$  and using Assumption 2 leads to the result of Proposition 2.  
2) Proof of Proposition 3: The proof makes use of wellknown techniques specific to the Gaussian distribution, namely the *Stein's lemma* and the *Poincare's inequality* ´ which we recall below and which have already been exploited in e.g. [35], [15], [24]. Therefore, we only give the main steps of the proof and skip some details of the computations.

a) Useful tools.: A function f : C
n → C is said to be C
1(C
n) if f(z) = ˜f(Re(z),Im(z)) with ˜f ∈ C1(R
2n).

Moreover, we also recall the definition of the standard complex differential operators

$$\frac{\partial f}{\partial z_{k}}({\bf z})=\frac{1}{2}\left(\frac{\partial\bar{f}}{\partial x_{k}}({\bf x},{\bf y})-{\rm i}\frac{\partial\bar{f}}{\partial y_{k}}({\bf x},{\bf y})\right)\tag{142}$$ $$\frac{\partial f}{\partial\overline{z}_{k}}({\bf z})=\frac{1}{2}\left(\frac{\partial\bar{f}}{\partial x_{k}}({\bf x},{\bf y})+{\rm i}\frac{\partial\bar{f}}{\partial y_{k}}({\bf x},{\bf y})\right)\tag{143}$$  with ${\bf x}={\rm Re}({\bf z})$ and ${\bf y}={\rm Im}({\bf z})$.  
Lemma 4 (Stein's lemma). Let w ∼ NCn (0, I) and f ∈
C
1(C
n), assumed polynomially bounded together with its partial derivatives. Then for all k = 1*, . . . , n*,

$$\mathbb{E}[f(\mathbf{w})w_{k}]=\mathbb{E}\left[\frac{\partial f}{\partial\overline{w_{k}}}(\mathbf{w})\right],\ \mathbb{E}[f(\mathbf{w})\overline{w_{k}}]=\mathbb{E}\left[\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right].$$  **Lemma 5** (Poincare inequality).: _Let $\mathbf{w}\sim\mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0},\mathbf{I})$ and $\mathbf{w}$ be a $\mathbf{w}$-independent of $\mathbf{w}$. Then $\mathbf{w}$ is a $\mathbf{w}$-independent of $\mathbf{w}$._
f ∈ C1(C
n)*, assumed polynomially bounded together with* its partial derivatives. Then,

$$\mathbb{V}[f(\mathbf{w})]\leq\sum_{k=1}^{n}\left(\mathbb{E}\left|\frac{\partial f}{\partial\overline{w}_{k}}(\mathbf{w})\right|^{2}+\mathbb{E}\left|\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right|^{2}\right).\tag{144}$$

For ease of reading, we introduce the following differentiation operators with respect to the entries of the M ×Nℓ matrix Wℓ, which will be constantly used in the derivations below,

$$\partial_{i,j}^{(\ell)}=\frac{\partial}{\partial[{\bf W}_{\ell}]_{i,j}},\quad\overline{\partial}_{i,j}^{(\ell)}=\frac{\partial}{\partial[{\bf W}_{\ell}]_{i,j}}.\tag{145}$$  We will also need the following auxiliary result (see [33])
related to the quantity χ defined in (100).
Lemma 6. For all p ∈ N and r ∈ N, E [χ r] = 1 + O1 Np

and for ℓ ∈ {0, . . . , L} and for any i ∈ {1*, . . . , M*}, j ∈
$\ldots,N_{\ell}\}$,  $$\mathbb{E}\left[\partial_{i,j}^{(\ell)}\chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right)\text{and}\mathbb{E}\left[\overline{\partial}_{i,j}^{(\ell)}\chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right).\tag{146}$$
Lemma 6 shows in particular that the presence of the regularization term χ can be removed from expectations, up to an error term of arbitrary polynomial decay.

In the following, ∆ is a generic notation for a continuous function such that |∆(u)| < P(u) for some polynomial P with positive coefficients independent of M, and whose value may change from one line to another.

b) Development of Ψ′: Write k,k

$$\Psi^{\prime}(u)=\mathrm{i}\sum_{k=1}^{K}\sum_{\ell=0}^{L}\mathbb{E}\left[\left(\beta_{1,k,\ell}\eta_{1,k,\ell}+\beta_{2,k,\ell}\eta_{2,k,\ell}\right.\right.$$ $$\left.\left.+\,\mathrm{Re}\left(\overline{\beta_{3,k,\ell}\eta_{3,k,\ell}}\right)\right)\xi(u)\right].\tag{147}$$

In the following, we only provide some details for the development of E[η1,k,0ξ(u)], as the other terms can be obtained similarly. Using the resolvent identity, we start by writing

$$\mathbb{E}\left[\eta_{1,k,0}\xi(u)\right]=\frac{\sqrt{M}}{\rho_{k,0}}\mathbb{E}\left[\left(\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\frac{\mathbf{W}_{0}\mathbf{W}_{0}^{*}}{N_{0}}\mathbf{u}_{k}\chi\right)^{\circ}\xi(u)\right].\tag{148}$$

Next, we apply Stein's lemma, Poincare's inequality and ´
Lemma 6 to obtain

$$\mathbb{E}\left[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\frac{\mathbf{W}_{0}\mathbf{W}_{0}^{*}}{N_{0}}\mathbf{u}_{k}\chi\xi(u)\right]=$$ $$\mathrm{i}u\sigma^{2}\sum_{i,j}\mathbb{E}\left[[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})]_{i}[\mathbf{W}_{\ell}^{*}\mathbf{u}_{k}]_{j}\chi\overline{\partial}_{i,j}^{(0)}\{\eta\}\xi(u)\right]$$ $$\qquad\qquad N_{0}(1+\alpha_{0}(\rho_{k,0}))$$ $$\qquad\qquad+\frac{\sigma^{2}\mathbb{E}\left[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\mathbf{u}_{k}\chi\xi(u)\right]}{1+\alpha_{0}(\rho_{k,0})}+\frac{\Delta(u)}{M},\tag{149}$$

where αℓ(z) = E
hσ 2 Nℓ trQℓ(z)χ ifor all ℓ = 0*, . . . , L*. Using the fact that α0(ρk,0) = σ 2c0m0(ρk,0) + O(
1 M2 ), this gives

$$\mathbb{E}\left[\eta_{1,k,0}\xi(u)\right]=$$ $$\mathrm{i}u\sigma^{2}\sqrt{M}\sum_{i,j}\mathbb{E}\left[[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})]_{i}[\mathbf{W}_{\ell}^{*}\mathbf{u}_{k}]_{j}\chi\overline{\partial}_{i,j}^{(0)}\{\eta\}\xi(u)\right]$$ $$\qquad\qquad N_{0}\left(\rho_{k,0}(1+\sigma^{2}c_{0}m_{0}(\rho_{k,0}))-\sigma^{2}\right)$$ $$\qquad+\frac{\Delta(u)}{\sqrt{M}}.\tag{150}$$

Developing further the derivatives and using Lemma 6, we have

i,j E h[u ∗ kQ0(ρk,0)]i[W∗ ℓuk]jχ∂ (0) i,j {η1,k′,ℓ}ξ(u) i= X − √ ME " u ∗ kQ0(ρk,0)Qℓ(ρk′,ℓ)uk′u ∗ k′Qℓ(ρk′,ℓ) × WℓW∗ ℓ Nℓukχξ(u) # + ∆(u) √M = √ Mθk,ℓδk−k′Ψ(u) + ∆(u) √M , (151)
with

κk,ℓ =
$\ell=$  $$\left\{\begin{array}{ll}\frac{\sigma^{2}m_{0}(\rho_{k,0})m_{0}^{\prime}(\rho_{k,0})}{1+\sigma^{2}c_{0}m_{0}(\rho_{k,0})}&\mbox{if$\ell=0$,}\\ \frac{\sigma^{2}m_{\ell}(\rho_{k,\ell})m_{0}(\rho_{k,0})(1+\sigma^{2}c_{0}m_{0}(\rho_{k,0}))}{\sigma^{2}-\rho_{k,\ell}(1+\sigma^{2}c_{0}m_{0}(\rho_{k,0}))(1+\sigma^{2}c_{\ell}m_{\ell}(\rho_{k,\ell}))}&\mbox{if$\ell\geq1$}\\ \end{array}\right.\tag{152}$$
$$=\left\{\begin{array}{ll}-\frac{\sigma^{2}\gamma_{k}}{(\gamma_{k}+\sigma^{2}c_{0})^{2}(\gamma_{k}^{2}-\sigma^{2}c_{0})}&\mbox{if$\ell=0$}\\ -\frac{\sigma^{2}\gamma_{k}}{(\gamma_{k}+\sigma^{2}c_{0})(\gamma_{k}+\sigma^{2}c_{\ell})(\gamma_{k}^{2}-\sigma^{2}c_{0})}&\mbox{if$\ell\geq1$}\end{array}\right.,\tag{153}$$  where the second equality in the expression of $\theta_{k,\ell}$ can be 
obtained with Lemma 3. Moreover,
i,j E h[u ∗ kQ0(ρk,0)]i[W∗ ℓuk]jχ∂ (0) i,j {η2,k′,ℓ}ξ(u) i X = − √M N2 ℓ E " u ∗ kQ0(ρk,0)WℓQ˜ℓ(ρk′,ℓ)sk′,ℓ × s ∗ k′,ℓQ˜ℓ(ρk′,ℓ)W∗ ℓukχξ(u) # + ∆(u) √M = ∆(u) √M , (154) and i,j E h[u ∗ kQ0(ρk,0)]i[W∗ ℓuk]jχ∂ (0) i,j {η3,k′,ℓ}ξ(u) i X = − √M Nℓ E " u ∗ kQ0(ρk,0)Qℓ(ρk′,ℓ)Wℓsk′,ℓ × u ∗ k′Qℓ(ρk′,ℓ) WℓW∗ ℓ Nℓukχξ(u) # + ∆(u) √M = ∆(u) √M . (155) Finally, using again Lemma 3, we obtain
E [η1,k,0ξ(u)] =iuσ2c0PL ℓ=0 β1,k,ℓκk,ℓ ρk,0(1 + σ 2c0m0(ρk,0)) − σ 2 Ψ(u) + ∆(u) √M = −iu β1,k,0σ 4c0 (γk + σ 2c0) 2(γ 2 k − σ 2c0) + X L β1,k,ℓσ 4c0 (γk + σ 2c0)(γk + σ 2cℓ)(γ 2 k − σ 2c0) Ψ(u) + ∆(u) √M . ℓ=1 (156)
Using similar computations for the remaining terms
(E [η*i,k,ℓ*ξ(u)]) ℓ≥1 i=2,3 in Ψ′(u), we finally obtain the result of Proposition 3.

REFERENCES

```
[1] R. Beisson, P. Vallet, A. Giremus, and G. Ginolhac, "Change Detection
    in The Covariance Structure of High-Dimensional Gaussian Low-Rank
    Models," in Statistical Signal Processing Workshop (SSP). IEEE, 2021,
    pp. 421–425.

```

[2] K. Conradsen, A. Nielsen, J. Schou, and H. Skriver, "A test statistic in the complex Wishart distribution and its application to change detection in polarimetric SAR data," *IEEE Trans. Geosci. Remote Sens.*, vol. 41, no. 1, pp. 4–19, 2003.

[3] D. Ciuonzo, V. Carotenuto, and A. De Maio, "On multiple covariance equality testing with application to SAR change detection," IEEE Trans. on Signal Process., vol. 65, no. 19, pp. 5078–5091, 2017.

[4] A. Mian, G. Ginolhac, J.-P. Ovarlez, and A. Atto, "New robust statistics for change detection in time series of multivariate SAR images," IEEE Trans. Signal Process., vol. 67, no. 2, pp. 520–534, 2018.

[5] A. Mian, A. Collas, A. Breloy, G. Ginolhac, and J.-P. Ovarlez, "Robust low-rank change detection for multivariate sar image time series," *IEEE* J. Sel. Top. Appl. Earth Obs. Remote Sens., vol. 13, pp. 3545–3556, 2020.

[6] R. Liu, L. Liu, D. He, W. Zhang, and E. G. Larsson, "Detection of abrupt change in channel covariance matrix for multi-antenna communication,"
in *Global Communications Conference (GLOBECOM)*. IEEE, 2021.

[7] P. Galeano and D. Pena, "Covariance changes detection in multivariate ˜
time series," *J. Stat. Plan. Inference*, vol. 137, no. 1, pp. 194–211, 2007.

[8] A. Ribes, J.-M. Azais, and S. Planton, "Adaptation of the optimal fingerprint method for climate change detection using a well-conditioned covariance matrix estimate," *Clim. Dyn.*, vol. 33, no. 5, pp. 707–722, 2009.

[9] Y.-H. Zhou, "Set-based differential covariance testing for genomics,"
Stat, vol. 8, no. 1, p. e235, 2019.

[10] A. Gupta and J. Tang, "Distribution of likelihood ratio statistic for testing equality of covariance matrices of multivariate gaussian models,"
Biometrika, vol. 71, no. 3, pp. 555–559, 1984.

[11] R. Muirhead, *Aspects of multivariate statistical theory*. Wiley Online Library, 1982.

[12] S. Zheng, "Central limit theorems for linear spectral statistics of large dimensional F-matrices," *Ann. Inst. H. Poincare Probab. Statist.* ´ , vol. 48, no. 2, pp. 444–476, 2012.

[13] I. Johnstone, "On the distribution of the largest eigenvalue in principal components analysis," *Ann. Statist.*, vol. 29, no. 2, pp. 295–327, 04 2001.

[14] A. Combernoux, F. Pascal, and G. Ginolhac, "Performance of the lowrank adaptive normalized matched filter test under a large dimension regime," *IEEE Trans. Aerosp. Electron. Syst.*, vol. 55, no. 1, pp. 459–
468, 2018.

[15] P. Vallet, X. Mestre, and P. Loubaton, "Performance analysis of an improved music doa estimator," *IEEE Trans. Signal Process*, vol. 63, no. 23, p. 6407–6422, 2015.

[16] K. Wachter, "The limiting empirical measure of multiple discriminant ratios," *Ann. Statist.*, pp. 937–957, 1980.

[17] Q. Wang and J. Yao, "Extreme eigenvalues of large-dimensional spiked fisher matrices with application," *Ann. Statist.*, vol. 45, no. 1, pp. 415–
460, 2017.

[18] R. Abdallah, A. Mian, A. Breloy, A. Taylor, M. El Korso, and D. Lautru,
"Detection methods based on structured covariance matrices for multivariate SAR images processing," *IEEE Geosci. Remote. Sens. Lett.*,
vol. 16, no. 7, pp. 1160–1164, 2019.

[19] R. Abdallah, A. Breloy, A. Taylor, M. El Korso, and D. Lautru, "Signal subspace change detection in structured covariance matrices," in 27th European Signal Processing Conference (EUSIPCO). IEEE, 2019.

[20] F. Benaych-Georges, A. Guionnet, and M. Maida, "Fluctuations of the Extreme Eigenvalues of Finite Rank Deformations of Random Matrices,"
Electron. J. Probab., vol. 16, pp. no. 60,1621–1662, 2011.

[21] F. Benaych-Georges and R. Nadakuditi, "The eigenvalues and eigenvectors of finite, low rank perturbations of large random matrices," Adv.

Math., vol. 227, no. 1, pp. 494–521, 2011.

[22] T. Anderson, *An introduction to multivariate statistical analysis*. John Wiley & Sons, 1958.

[23] I. Johnstone, "High dimensional statistical inference and random matrices," in *International Congress of Mathematicians*, Madrid, 2006.

[24] X. Mestre and P. Vallet, "Correlation Tests and Linear Spectral Statistics of the Sample Correlation Matrix," *IEEE Trans. Inf. Theory*, vol. 63, no. 7, pp. 4585–4618, 2017.

[25] R. Couillet, "Robust spiked random matrices and a robust G-MUSIC
estimator," *J. Multivariate Anal.*, vol. 140, pp. 139–161, 2015, publisher:
Elsevier.

[26] J. B. G. A. S. Pech ´ e, "Phase transition of the largest eigenvalue for ´
nonnull complex sample covariance matrices," *Ann. Probab. 33 (5) 1643* - 1697, 2005.

[27] P. Vallet, P. Loubaton, and X. Mestre, "On the consistency of likelihood penalization methods in large sensor networks," in *7th Sensor Array* and Multichannel Signal Processing Workshop (SAM). IEEE, 2012, pp. 109–112.

[28] P. Stoica and R. Moses, *Spectral analysis of signals*. Pearson Prentice Hall, 2005, vol. 452.

[29] A. Mian, J.-P. Ovarlez, A. Atto, and G. Ginolhac, "Design of new wavelet packets adapted to high-resolution sar images with an application to target detection," *IEEE Trans. Geosci. Remote Sens.*, vol. 57, no. 6, pp. 3919–3932, 2019.

[30] X. Mestre, "On the asymptotic behavior of the sample estimates of eigenvalues and eigenvectors of covariance matrices," IEEE Trans. Signal Process., vol. 56, no. 11, pp. 5353–5368, 2008.

[31] S. Geman, "A limit theorem for the norm of random matrices," Ann.

Prob., pp. 252–261, 1980.

[32] R. Horn and C. Johnson, *Matrix analysis*. Cambridge university press, 2012.

[33] W. Hachem, P. Loubaton, X. Mestre, J. Najim, and P. Vallet, "Large information plus noise random matrix models and consistent subspace estimation in large sensor networks," *Random Matrices: Theory Appl.*,
vol. 1, no. 2, 2012.

[34] F. Benaych-Georges and R. Nadakuditi, "The singular values and vectors of low rank perturbations of large rectangular random matrices," J.

Multivariate Anal., vol. 111, no. 0, pp. 120–135, 2012.

[35] W. Hachem, O. Khorunzhiy, P. Loubaton, J. Najim, and L. Pastur, "A
new approach for capacity analysis of large dimensional multi-antenna channels," *IEEE Trans. Inf. Theory*, vol. 54, no. 9, pp. 3987–4004, 2008.