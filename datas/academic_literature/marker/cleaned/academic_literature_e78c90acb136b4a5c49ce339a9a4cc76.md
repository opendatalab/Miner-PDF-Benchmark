# A Sharp Uniform-In-Time Error Estimate For Stochastic Gradient Langevin Dynamics

Lei Lia,b,c and Yuliang Wanga,b aSchool of Mathematical Sciences, Shanghai Jiao Tong University, Shanghai, 200240, P.R.China.

bInstitute of Natural Sciences, MOE-LSC, Shanghai Jiao Tong University, Shanghai, 200240, P.R.China.

cQing Yuan Research Institute, Shanghai Jiao Tong University, Shanghai, 200240, P.R.China.

## Abstract 1

We establish a sharp uniform-in-time error estimate for the **Stochastic Gradient**
Langevin Dynamics (SGLD), which is a popular sampling algorithm. Under mild assumptions, we obtain a uniform-in-time O(η 2
**) bound for the KL-divergence between**
the SGLD iteration and the Langevin diffusion, where η **is the step size (or learning**
rate). Our analysis is also valid for varying step sizes. Based on this, we are able to obtain an O(η**) bound for the distance between the SGLD iteration and the distribution**
of the Langevin diffusion, in terms of Wasserstein or total variation distances.

## 1 Introduction

The Stochastic Gradient Langevin Dynamics (SGLD) [49], first proposed by Welling and Teh, has drawn great attention of researchers when dealing with optimization or sampling tasks [2, 33, **40]. As a sampling algorithm, SGLD can be viewed as a "random batch" version** of the Unadjusted Langevin Algorithm (ULA), which is the Euler-Maruyama discretization of the Langevin diffusion, a stochastic process converging to a target Gibbs' distribution under suitable settings. As an optimization algorithm, SGLD can be viewed as a variant of the classical Stochastic Gradient Descent (SGD) [44], by adding independent Gaussian noise in each iteration of SGD. At recent decades, SGD and its variants [44, 25, 11, 37] have received a great deal of attention when solving high-dimensional tasks, ranging from computer vision, natural language processing, to high dimensional sampling, statistical optimization, etc. Also much theoretical analysis for SGD has been done **by former researchers,**
including loss landscape of SGD iteration [46, **47], its dynamical stability [50] and diffusion**
approximation [32, 21, 17]. The combination of the SGD algorithm and the Langevin diffusion, can improve the behavior of both methods: for SGD, by taking **another independent**
diffusion term into consideration, though not converging to a fixed point, the algorithm may be able to admit better ergodic properties and obtain better performance near saddle points [26, **52]. Besides, the application of the methodology of random mini-batch to**
Langevin diffusion could result in some efficient methods that could reduce computational cost while preserving the dynamical and statistical properties. Examples include the SGLD algorithm we study in the paper and the random batch methods for interacting particle systems [22, **23].**
In this paper, we consider the error estimate of SGLD for sampling from the target distribution π ∝ e
−βU , where the function U(x**) of the form**
U(x) := Eξ [U(x; ξ)] , x ∈ R
d. **(1.1)**
arXiv:2207.09304v2 [math.PR] 22 Oct 2022 Here, ξ ∼ ν is a random variable/vector for some distribution ν**. A typical form of (1.1)**
arising from applications like Bayesian inference or machine learning [49] is given by

$$U(x):=U_{0}(x)+{\frac{1}{N}}\sum_{i=1}^{N}U_{i}(x).$$
$$(1.2)$$
$$(1.3)$$

We remark that in [49], there was no 1/N **factor. Such a factor can be obtained by suitable** scaling, like choosing suitable β **or rescaling the time in the Langevin diffusion, and it is** helpful so that it can be written as an expectation over a probability **distribution. Then the**
random vector ξ can be taken as a random batch with size S and then U(x; ξ) = U0(x) +
1 S
Pi∈ξ Ui(x**). The associated (overdamped) Langevin diffusion (a stochastic differential**
equation (SDE)) for the target distribution π **is given by:**

$$d X=b(X)d t+{\sqrt{2\beta^{-1}}}d W,$$
dX = b(X)dt +p2β−1dW, **(1.3)**
where

$$b(x):=-\nabla U(x),$$
$$(1.4)$$
b(x) := −∇U(x), **(1.4)**
and W **is the standard Brownian Motion in** R
d**, and** β
−1 > **0 is the fixed temperature**
constant. The target distribution π(x) ∝ e
−βU(x)**is exactly the invariant distribution of the**
Langevin diffusion [41]. We also denote

$\left(1.5\right)$ . 
$\downarrow$ . 
$$(1.6)$$
$$(1.7)$$
b ξ(x) = −∇U(x; ξ**) (1.5)**
in this paper. Then the SGLD algorithm with time step ηk at k**-th iteration is:**

$$\bar{X}_{T_{k+1}}=\bar{X}_{T_{k}}+\eta_{k}b^{\xi k}(\bar{X}_{T_{k}})+\sqrt{2\beta^{-1}\eta_{k}}Z_{k},\quad Z_{k}\sim N(0,I_{d})\quad i.i.d.,$$

with Tk := Pk−1 i=0 ηi. Here, ξk **are i.i.d. sampled. Also we have the following continuous**
version which coincides with the discrete SGLD at grid point Tk:

$$\bar{X}_{t}:=\bar{X}_{T_{k}}+(t-T_{k})b^{\xi_{k}}(\bar{X}_{T_{k}})+\sqrt{2\beta^{-1}}\left(W_{t}-W_{T_{k}}\right),\quad t\in[T_{k},T_{k+1})\,.$$

At time t, denote densities of Xt, X¯t by ρt, ¯ρt**, respectively. In this paper, our main results**
focus on the "distance" between ρt and ¯ρt**. In our main results, we consider the KullbackLeibler (KL) divergence [28], defined by**

$$D_{K L}(\mu||\nu):=\int_{\mathbb{R}^{d}}\log{\frac{d\mu}{d\nu}}\,\mu(d x),$$
$$(1.8)$$

where µ, ν **are probability measures on** R
d**. Note that the KL-divergence is not a distance**
(a metric) in mathematics. Furthermore, based on this estimate, convergence rate to the invariant distribution of the Langevin diffusion (1.3) and results for particular time step sequences will be discussed.

A great deal of theoretical research for the SGLD algorithm has been done. In [51], the authors studied the hitting time of SGLD for non-convex optimization problem. Different from the goal of our work, instead of analyzing the convergence to a target distribution, the authors focused on finding a local minimum and the corresponding convergence results. For sampling-aimed tasks, much SGLD-related research has been done when the target distribution is log-concave [10, 9, **8]. Convergence analysis for SGLD under non-convex settings**
is a bit more technical. In [43], the authors obtained an error bound for the Wasserstein-2 distance between the SGLD iteration and the target distribution of **order** O(kη + e
−kη),
where k is the number of iterations and η **is the constant time step. In [36], assuming the** boundedness of the drift function, the authors proved the error is of order O(
√kη**) in terms**
of Wasserstein-2 distance. In [53], assuming the second-order smoothness of the drift function, the authors obtained an improved bound of order O(
√η/S + η **+ (1** − η)
k**) in terms**
of total variance, where S **is the batch size. Different from most former work, where the**
error bounds had an at least polynomial dependency on the time T **, in [16], the authors**
obtained a uniform-in-time bound, enabling more long time analysis for **SGLD. One point**
worth emphasizing is that, observing the time step η**, none of the former work can get estimation better than** O(
√η**) in terms of Wasserstein distances or total variation distance. In**
this paper, we resolve this issue and obtain a sharp bound in terms of η.

As has been mentioned, SGLD can be viewed as the "random batch" version of the EulerMaruyama scheme for the Langevin diffusion (1.3), which is also known as the Unadjusted Langevin Algorithm (ULA), or the Langevin Monte Carlo (LMC). In this paper, the main part of our result for SGLD is built upon our analysis for ULA, since it can be viewed as the simpler full-batch version of SGLD. Based on this observation, the convergence rate with respect to the time step η **for SGLD would not exceed that for ULA. Much work on ULA** has been done before, some of which are found useful for our sharp analysis for SGLD. In
[8], using the first order smoothness assumption, the authors showed that DKL(ˆρT ||ρT ) =
O(ηT d), where ˆρt denotes the density of the continuous version ULA (similar with ¯ρt**) at**
time t, T is the length of the (finite) time interval, and d **is the dimension of the Euclidean**
space. However, this is not the optimal rate, since this result implies that W2(ˆρT , ρT ) =
O(
√η) rather than the well-known O(η) [3, **9]. In [35], Mou improved the KL divergence**
DKL(ˆρT ||ρT ) from O(ηT d**) to** O(η 2d 2T ), so the Wasserstein distance is of O(η**). Compared**
with the former "O(ηT d**)" result, the improved result in [35] needs second order smoothness** of the drift function b(x).

Our work is naturally motivated by the following two questions:
- For ULA, the error in terms of KL-divergence can be improved from O(η**) to** O(η 2**) if**
we add the second order smoothness assumption for the drift. Can we do the same for SGLD to obtain a sharp bound?

- **Most error analysis for ULA and SGLD has at least polynomial dependency for the**
time interval T **, which prevents us from digging deeper into the asymptotic behaviors**
as T → ∞ **of these stochastic algorithms. Are we able to establish a uniform-in-time**
error bound?

In this paper, we give positive answers to both questions above.

The main contribution of this paper is to establish a uniform-in-time O(η 2**) bound for**
the KL-divergence between SGLD iterates and the Langevin diffusion, namely, in Theorem 3.2 **we show that**

$$D_{KL}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})\leq c_{1}\eta_{0}^{2}e^{-A_{0}T_{k}}+c_{2}\int_{0}^{T_{k}}e^{-A_{0}(T_{k}-s)}f(s)ds,\tag{1.9}$$

where

$$T_{k}=\sum_{i=0}^{k-1}\eta_{i},\quad f(s)=\sum_{i=0}^{\infty}\eta_{i}^{2}\mathbf{1}_{[T_{i},T_{i+1})}(s).\tag{1.10}$$  The constant term $\sum_{i=0}^{\infty}\eta_{i}^{2}\mathbf{1}_{[T_{i},T_{i+1})}(s)$ is the same if we obtain 
If we simply consider the constant step size (or learning rate), then a uniform-in-time O(η 2) error bound is obtained in Corollary **3.1:**

$$(1.11)^{\frac{1}{2}}$$
$$\mathbf{\partial})\leq c\eta^{2}.$$
$$\operatorname*{sup}_{t\geq0}D_{K}$$

DKL(¯ρt||ρt) ≤ cη2. **(1.11)**
The proof of our main results are based on the Markov property of **SGLD. Indeed, the** discrete SGLD process in our setting is a Markov Chain [13], and it is a time homogeneous one if the step size (or learning rate) is constant. Let ρ ξ t **be the probability density of the**
fixed-batch version of SGLD (1.7) for a given sequence of batches ξ := (ξ0, ξ1, · · · , ξk, **· · ·**)
(which is actually the ULA with the drift b ξ(x**)). Consequently, we have the following**
expression of the density:
ρ¯t(·) = Eξ[ρ ξ t
(·)]. **(1.12)**
Here,Eξ[ρ ξ t(·)] means taking expectation for all possible choice of batch ξ**. Note that** ρ ξ t satisfies a Fokker-Planck equation, whose explicit expression will be derived in Lemma **2.1.**
By the Markov property, we are able to find that

$$\mathbb{E}\left[\rho_{t}^{\xi}\Big|\xi_{i},\;i\geq k\right]=\mathcal{S}_{T_{k},t}^{\xi_{k}}\bar{\rho}_{T_{k}},\quad t\in[T_{k},T_{k+1}),$$

where the operator S
ξk Tk,t is the evolution operator from Tk to t **for the Fokker-Planck**
equation. Based on this observation, we are able to estimate the time derivative of the KL-divergence DKL(¯ρt||ρt**), and then obtain the desired second-order error bound after a**
Gr¨onwall's inequality. Also, while handling the details, techniques including integration by parts (to eliminate the Gaussian noise that would possibly lower the convergence rate) and Girsanov transform are adopted.

We also have some corollaries of our results:
First, we consider the special case ηi = (ℓ + i)
−θ, i = 0, 1, 2, ..., with θ ∈ (0, **1) being the**
decaying coefficient, which is common in many practical tasks [31]. In Section **3, we analyze**
the asymptotic convergence rate of DKL(¯ρTk||ρTk
) as k → +∞ **for different** θ.

Second, we estimate the Wasserstein-2 distance [45] between the SGLD iteration and the target distribution π**, and after comparison with former work, our result is confirmed to** be a great improvement.

The rest of the paper is organized as follows. Before our main results, we introduce some preliminaries in Section 2 **including the basic background and properties of the (overdamped)**
Langevin diffusion and its Euler-Maruyama discretization, ULA. In Section **3, we present** and prove our main result: a sharp uniform-in-time estimate for SGLD, and some useful corollaries are also included. In Section **4, we provide the proof for a crucial local estimate,** which is omitted in Section 3 **for the convenience of readers. Some technical details that** are not so important are moved to the Appendix. In Section **5, we perform discussion** on our analysis on the Wasserstein-2 distance between the SGLD iteration and the target distribution π based on our main results. The ergodicity of SGLD algorithm as well as the reason why our analysis is "sharp" are also discussed in Section 5.

## 2 Preliminaries

For the convenience of readers, let us begin with some basic definitions and properties that would be useful in this paper.

## 2.1 (Overdamped) Langevin Diffusion

Derived from the Langevin equation, the (overdamped) Langevin diffusion has strong, wellknown physical background [41]. Let us first consider the following second-order SDE called Langevin equation:
X¨ = −∇U(X) − γX˙ +
»2γ/β W , ˙ **(2.1)**

$$(X\,)-\gamma X\,+\,{\sqrt{\,}}^{2}\gamma/\beta$$

where γ **is the friction coefficient,** β
−1:= kBT with kB **being the Boltzmann constant and**
T being the (physical) temperature. The term γX˙ **here describes the linear dissipation** damping, and the term p2γ/βW˙ **describes the fluctuation stochastic forcing. Note that** the Brownian Motion W is not pointwise differentiable, and so W˙ **should be understood**
in the distributional sense and is in fact the white noise [38]. Moreover, thanks to the Fluctuation-Dissipation Theorem [27], we are able to relate the dissipation and the fluctuation by considering the covariance of the fluctuation term.

Langevin equation (2.1) describes a particle moving according the Newton's second law and being in contact with a heat reservoir that is at equilibrium at temperature T **. This** physical is called an open classical system. To see this more clearly, we rewrite the Langevin equation (2.1) into an SDE system. Letting Y = X˙**, we have**

$$\left\{\begin{array}{l l}{d X=Y d t}\\ {d Y=-\nabla U(X)d t-\gamma Y d t+\sqrt{2\gamma\beta^{-1}}d W}\end{array}\right.$$
dY = −∇U(X)dt − γY dt +p2γβ−1dW **(2.2)**
$$(2.2)$$

It is also well-known that if we consider the time rescaling Xγ(t) = X(γt**), and let**
γ → +∞**, the Langevin equation (2.1) turns into the overdamped Langevin diffusion [41]:**
dX = −∇U(X)dt +p2β−1dW. **(2.3)**
The derived (overdamped) Langevin diffusion above has some pretty properties. First, it has invariant distribution π ∝ e
−βU **, which is trivial to check. Second, the invariant**
distribution π satisfies the detailed balance since the probability flux J(π**) :=** b·π− 12∇·(Σπ)
equals zero with b = −∇U and Σ = p2β−1I **here, and thus the stationary diffusion is**
reversible [41]. Third, the density of the Langevin diffusion satisfies the following FokkerPlanck equation:
∂tρt = −∇ · (ρtb) + β
−1∆ρt, ρt|t=0 = ρ0. **(2.4)**
with b = −∇U. Moreover, if we add some mild assumptions to the function U **like strongly**
log-concaveness, the Langevin diffusion above is guaranteed to converge to equilibrium [34]. Note that in this paper, instead of log-concaveness of the invariant distribution π**, we add** the much weaker assumption that π **satisfies a Log-Sobolev inequality (LSI).**

## 2.2 Unadjusted Langevin Algorithm(Ula)

Among the classical numerical schemes for the Langevin diffusion (1.3), the simplest one is the well-known Euler-Maruyama scheme, which is also known as the Unadjusted Langevin Algorithm (ULA) or the Langevin Monte Carlo (LMC). Consider this Euler-Maruyama scheme with constant time step for (1.3)

5
$$Z_{k}\sim N(0,I_{d})\quad i.i.d.,$$
XˆTk+1 = XˆTk + ηkb(XˆTk
) + p2β−1ηkZk, Zk ∼ N(0, Id) i.i.d., **(2.5)**
where ηk is the time step at k**-th iteration and** Tk := Pk−1
i=0 ηi**. (2.5) naturally admits the**
following continuous version:
Xˆt := XˆTk + (t − Tk)b(XˆTk
) + p2β−1 (Wt − WTk
), t ∈ [Tk, Tk+1), **(2.6)**
where Wt **is the Brownian Motion in** R
d. We also denote ˆρt(x**) the probability density**
function of Xˆt. It is not difficult to show that ˆρt **satisfies a Fokker-Planck equation, and we**
conclude it in the following lemma:
Lemma 2.1. Denote ρˆt(x) the probability density function of Xˆt defined in (2.6)**. Then the**
following Fokker-Planck equation holds:
$$\partial_{t}\hat{\rho}_{t}=-\nabla\cdot(\hat{\rho}_{t}\hat{b}_{t})+\beta^{-1}\Delta\hat{\rho}_{t},\quad\hat{\rho}_{t}|_{t=0}=\rho_{0},$$
−1∆ˆρt, ρˆt|t=0 = ρ0, **(2.7)**
where
The derivation is not difficult and has appeared in many classical work [35]. Indeed, for
t ∈ [Tk, Tk+1**), consider the random variable ˆ**ρt|FˆTk
, where FˆTk = σ(Xˆs, s ≤ Tk**). Then, by**
definition of Xˆt, ˆρt|FˆTk
satisfies:
$$\hat{b}_{t}(x):=\mathbb{E}\left[b\left(\hat{X}_{T_{k}}\right)|\hat{X}_{t}=x\right],\quad t\in[T_{k},T_{k+1})\,.$$
$$\partial_{t}(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})=-\nabla\cdot\left(b(\hat{X}_{T_{k}})(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})\right)+\beta^{-1}\Delta(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}}),\quad t\in[T_{k},T_{k+1})\,.$$  expectation, we have 
Taking expectation, we have

we have  $$\mathbb{E}\left[\partial_{t}(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})\right]=\partial_{t}\hat{\rho}_{t},\quad\mathbb{E}\left[\Delta(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})\right]=\Delta\hat{\rho}_{t},\tag{2.10}$$  m.  
and for the drift term,  $$\mathbb{E}\left[-\nabla\cdot\left((\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})(x)b(\hat{X}_{T_{k}}^{\xi})\right)\right]=-\nabla\cdot\int(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})(x|y)b(y)\hat{\rho}_{T_{k}}(y)dy\tag{2.11}$$ $$=-\nabla\cdot\int b(y)\hat{\rho}_{t}.\tau_{k}(x,y)dy$$ $$=-\nabla\cdot\left(\hat{\rho}_{t}(x)\mathbb{E}\left[b(\hat{X}_{T_{k}}^{\xi})|\hat{X}_{t}=x\right]\right),$$  where $\hat{\rho}_{t}.\tau_{k}$ indicates the joint distribution density of $\hat{\rho}_{t}$ and $\hat{\rho}_{T_{k}}$. Note that we use Bayes's law is the same as we will use Gaussian all the above and to calculate the joint density ($\hat{\rho}_{t}$)
$$(2.7)$$
$$(2.8)$$
$$(2.9)$$
law in the second equality. Combining all the above, we obtain the desired result (2.7).

## 3 Main Results

In this section, we present our main result of this paper: a sharp uniform-in-time error estimate for SGLD. In Section **3.1, we present the assumptions required by later analysis.** In Section **3.2, we give some auxiliary results, including propagation of LSI of Langevin**
diffusion, moment control for ULA, and estimation of the Fisher information for ULA. After these preparations, in Section 3.3, we present the main theorem, Theorem **3.2, by first** showing a crucial local result, Proposition **3.2. Moreover, we give some corollaries including**
constant time step case, special decaying step size (or learning rate) case, and the special step size case, ηi = (ℓ + i)
−θ.

## 3.1 Our Assumptions

Before the main results and proofs, we firstly give the following assumptions we use throughout this paper. Recall the definition of the drift function b **in SGLD and its target distribution**
π in Section **1. For technical reasons, we will need the following assumptions.**
Assumption 3.1.
(a) (1st order smoothness) For a.e. ξ ∼ ν, b
ξis Lipshitz with a uniform constant L**, i.e.**
∀ξ, ∀**x, y** ∈ R
d,
$$|b^{\xi}(x)-b^{\xi}(y)|\leq L|x-y|.$$
ξ(y)| ≤ L|x − y|. **(3.1)**
_._ 2. _(2nd order smoothness) For a.e._ $\xi\sim\nu$_,_ $\nabla b^{\xi}$ _is Lipschitz with a uniform constant_ $L_{2}$_, i.e._ $\forall\xi$_,_ $\forall x,y\in\mathbb{R}^{d}$_,_ $$|\nabla b^{\xi}(x)-\nabla b^{\xi}(y)|\leq L_{2}d^{-\frac{1}{2}}|x-y|.$$ (3.2)
(c) (distance dissipation) For a.e. ξ ∼ ν, b ξis confining in the sense that
$\left(3,1\right)$. 

$$(3.2)$$
$$(3.3)$$
$$x\cdot b^{\xi}(x)\leq-\mu|x|^{2}+\sigma$$
$$(3.4)$$
2 + σ **(3.3)**
$$i t h\ \mu,$$
with µ, σ **being positive constants.**

(d) (boundedness) b
ξ − b **is uniformly bounded, namely,**
$$\operatorname{esssup}_{\xi}\|b^{\xi}-b\|_{L^{\infty}(\mathbb{R}^{d})}<+\infty.$$
ξ − b||L∞(Rd) < +∞. **(3.4)**
Moreover, the coefficient L, L2, µ, σ are independent of ξ and d.

In condition (a), the Lipschitz constant L **is the upper bound of the spectrum norm**
(largest singular value) of the Jacobian matrix and it is insensitive to the dimension d**. In** (3.2) in condition (b), we have put d
−1/2in the constant and assumed L2 **to be independent**
of d**. The intuition is that the left hand side is the spectral norm of the Jacobian matrix,**
which can be assumed to be insensitive to d while |x − y| scales like √d**. As we shall later,**
putting such a scaling can make the bounds of the relative entropy and Fisher information linear in d (see our discussion at the end of Section **5.2), which is the correct scaling. This** is a difference from the result in [35].

Note that condition (d) is equivalent to saying that b ξ − b ξ˜**is also uniformly bounded**
for two different ξ,
˜ξ. In (d) of Assumption **3.1, we do not need the uniform boundedness**
for every b ξ**, though (d) naturally holds when esssup**ξkb ξ(x)k∞ < ∞**, which is a much**
stronger condition. Actually the condition (d) is natural in applications. In many problems in machine learning, the loss has the same asymptotics for different data point.

In our paper, conditions (c) is used only to control the moments. Actually condition
(c) is the confinement condition which is crucial in literature for ergodicity. In our case, the log Sobolev inequality later in Assumption 3.2 **actually plays the role of confinement** for ergodicity. Moreover, it is not difficult to see that if one has the stronger boundedness condition esssupξ supx|b ξ(x)| < ∞**, then conditions (c) and (d) can be removed since the**
only place we use the distance dissipation condition (c) is the moment control (Propostition 3.1), but the only place we use the moment control is bounding terms like b ξ(Xt**). Now if**
we assume each b ξ**is bounded, we do not need the result for moment control any more.**

## Assumption 3.2.

(a) (λ-warm start) There exists λ ≥ 1 such that the initial distribution ρ0 **satisfies**

$${\frac{1}{\lambda}}\leq{\frac{\rho_{0}}{\pi}}\leq\lambda,$$
$$(3.5)$$

≤ λ, **(3.5)**
$\left(3.7\right)$. 
$$(3.8)$$
$\left(3.9\right)$. 
$=\left.x\right]$ . 
7
where π ∝ e
−βU is the invariant distribution of (1.3). Note that ρ0 **is the initial**
distribution for all the processes X, Xˆ , and X¯, and λ **is independent of the dimension**
d.

(b) (LSI for π**) The invariant distribution** π ∝ e
−βU **satisfies a Log-Sobolev inequality with**
a constant C
LS
π**, namely,** ∀f ∈ C∞
>0
,

$$Ent_{\pi}(f):=\int f\log fd\pi-\Big{(}\int fd\pi\Big{)}\log\Big{(}\int fd\pi\Big{)}\leq C_{\pi}^{LS}\int\frac{|\nabla f|^{2}}{f}d\pi.\tag{3.6}$$
$ative\ smooth\ functions$. 
*Here, $C_{>0}^{\infty}$ consists of all no*. 
>0 consists of all nonnegative smooth functions.

The Log-Sobolev inequality (LSI) was first discussed by Gross in 1975 [20]. Besides the simplest Gaussian distribution, other distributions satisfying an LSI **can be found following** the Bakry-Emery criterion [4], including strongly log-concave ones. It is also shown that distributions that are strongly log-concave outside a compact set **also satisfy the LSI [29].** We remark that the log-concaveness outside a compact set can imply both the distance dissipation and the log Sobolev inequality so the LSI assumption is much **weaker than the** log-concaveness assumption in many other literature. However, the distance dissipation condition x · b ≤ −µ|x| 2 + σ **outside a compact set can not derive the corresponding LSI so**
neither the distance dissipation nor the LSI assumption can be simply **removed though they** seem to have repetition somehow.

## 3.2 Some Auxiliary Results

Before presenting the main theorem, we give some useful auxiliary results first, including the propagation of LSI for the Langevin diffusion (1.3), moment control for ULA (2.6), and estimation of Fisher information for ULA (2.6).

## 3.2.1 Propagation Of Log-Sobolev Inequality

In this section, we aim to establish a Log-Sobolev inequality (LSI) for ρt**, which is the density**
of Xt **in the Langevin diffusion (1.3).**
Theorem 3.1. Consider the Fokker-Planck equation (2.4) associated with the SDE **(1.3)**.

Suppose Assumption 3.2 holds. Then, ρt **satisfies a LSI with a uniform LSI constant** λ 2C
LS
π.

The following Holley-Stroock perturbation lemma [5] is essential to our proof :
Lemma 3.1 (Holley-Stroock perturbation). Suppose the probability measure ν ∈ P(R
d)
satisfies an LSI with constant C
LS
ν, and µ ∈ P(R
d) satisfies dµ = hdν **with the uniform**
bound 1λ ≤ h ≤ λ. Then µ **satisfies an LSI with constant** λ 2C
LS
ν.

Proof of Theorem 3.1:
$$\rho_{t}={\frac{\rho_{t}}{\pi}}\pi=:q_{t}\pi.$$
π
π =: qtπ. **(3.7)**
Since b = β
−1∇ log π**, the detailed balanced is satisfied [34]. So it is well-known that** qt satisfies the following backwards Kolmogorov equation [30]:

$$\partial_{t}q_{t}=b\cdot\nabla q_{t}+\beta^{-1}\Delta q_{t},\quad q_{t}|_{t=0}=\frac{\rho_{0}}{\pi},$$
, **(3.8)**
and qt **can be expressed by the following conditional expectation form:**
qt(x) = E[q0(Xt)|X0 = x] . **(3.9)**

Then, as a direct consequence of (3.9), we know that at any time t > 0, infx qt ≥ infx q0,
and supx
qt ≤ supx
q0. Combining this fact and condition (a) in Assumption **3.2, it holds**
that1
$${\frac{1}{\lambda}}\leq q_{t}\leq\lambda,\quad\forall t\geq0.$$
≤ qt ≤ λ, ∀t ≥ 0. **(3.10)**
$$\lambda\ =\ n\ =\ 0,\ \ \lambda\ =\ 0.\tag{3.10}$$  Then, combining (3.10), Lemma 3.1, and (b) in Assumption 3.2, the conclusion holds.  
Note that the fact infx qt ≥ infx q0, supxqt ≤ supxq0 **can also be derived from classical**
results of PDE. Indeed, since the backward Kolmogorov equation (3.8) for qt **is of parabolic**
type, the maximal principle holds, whose details can be found in Chapter 7 of [15]. By maximal principle and condition (a) in Assumption **3.2, we also obtain**
$${\frac{1}{\lambda}}\leq q_{t}\leq\lambda,\quad\forall t\geq0.$$

## ≤ Qt ≤ Λ, ∀T ≥ 0. **(3.11)** 3.2.2 Moment Control

In this section, we aim to find a uniform-in-time bound for the moments E|X¯ ξ t| p **with** X¯ ξ defined in (1.12) of Section 1 and p = 2, **4. The details could be found in the proposition** below:
Proposition 3.1. Consider the process X¯t defined in (1.7) of Section 1**. Suppose (a), (c)**
of Assumption 3.1 holds. For all integer p ≥ 1, there exists positive constants cp and ∆p independent of t and ξ such that if ηk ≤ ∆p for all k**, then**

$$(3.11)$$

$$\mathbb{E}\left[|{\bar{X}}_{t}|^{p}\Big|{\mathcal{F}}_{\xi}\right]\leq c_{p}d^{\frac{p}{2}},\quad\forall t\geq0.$$
2 , ∀t ≥ 0. **(3.12)**
Moreover, for all integer p ≥ 1, there exists a positive constant αp such that when **α < α**p,

$$(3.12)^{\frac{1}{2}}$$
$$\operatorname*{sup}_{t\geq0}\mathbb{E}\left[e^{\alpha|\bar{X}_{t}|^{p}}\Big|{\mathcal{F}}_{\xi}\right]<+\infty.$$
i< +∞. **(3.13)**
Here, Fξ denotes the σ-algebra generated by ξ = (ξk)k≥0.

See Section A.1 **for the detailed proof.**

## 3.2.3 Estimate Of The Fisher Information

The Fisher information for a probability measure ρ **is defined by**

$${\mathcal{I}}(\rho):=\int|\nabla\log\rho|^{2}\rho d x.$$
$\left(3.14\right)$ . 
2ρdx. **(3.14)**
In our analysis, we come up with the exponential-weighted sum of Fisher information at the
grid point Tk **of ULA (SGLD with fixed batch), and a uniform-in-time order-one bound for**
this summation is required. To handle this, our strategy is to firstly estimate the continuous sum (i.e. integration) of the exponential-weighted Fisher information in Lemma **3.2. Then,** using the existing stability result (Lemma 3.3 **below) for Fisher information of ULA [35], we**
are able to control the desired discrete summation with the integration of the exponentialweighted Fisher information along the time axis.
Recall that ρ
ξ
t**is the law of the SGLD (1.7) conditioning on the given sequence of batches**
ξ = (ξ0, ξ1, · · · , ξk, · · ·). In Section **A.2, we first establish**
$$\frac{d}{d t}D_{K L}(\rho_{t}^{\xi}||\pi)\leq-c_{0}{\mathcal{I}}(\rho_{t}^{\xi})+c_{1}d,$$
) + c1d, **(3.15)**
where we recall π ∝ e
−βU **and consequently**

$$D_{K L}(\rho_{t}^{\xi}||\pi)\leq c d,$$

t||π) ≤ cd, **(3.16)**
where c0, c1, c are positive constants independent of t and ξ**. Then, after simple calculation**
including integration by parts, we are able to prove the following Lemma:

$$(3.15)$$
quentlly $\,$
$\left(3.16\right)^{2}$
Lemma 3.2. Let f **be a non-increasing, nonnegative, piecewise-constant function. Then**
under Assumption 3.1, 3.2, there exists ∆0 > 0, for any A0 > 0**, there exist positive constants**
M1, M2, independent of T and ξ such that when the step size sequence {ηk} defined in **(1.6)**
is bounded by ∆0**, the followings hold:**
$$\operatorname*{sup}_{t>0}D_{K L}(\rho_{t}^{\xi}||\pi)\leq c d,$$
t||π) ≤ cd, **(3.17)**
sup $t\geq0$. 
where c is independent of T , d and ξ**. Moreover,**

$$\int_{0}^{T}e^{-A_{0}(T-s)}f(s){\mathcal{I}}(\rho_{s}^{\xi})d s$$

$$\leq M_{1}D_{KL}(\rho_{0}||\pi)f(0)e^{-A_{0}T}+M_{2}\left(1+\sup_{s\geq0}D_{KL}(\rho_{s}^{\rho}||\pi)\right)\int_{0}^{T}e^{-A_{0}(T-s)}f(s)ds\tag{3.18}$$

The next lemma bounds the Fisher information I(ρ ξ t) at time t **with the Fisher information** I(ρ ξ Tk
) at the grid point. The estimation is valid for small ηk**, and we can view it**
as one kind of stability for the Fisher information of an only piecewise continuous process. The proof of the following lemma can be found in Lemma 6 of [35]
Lemma 3.3. Under the same setting of Lemma 3.2**, if** ηk ≤1 2L
, k ≥ 0**, then there is a**
positive constant c independent of k, d, and ξ **such that**

$$(3.17)$$
$$(3.19)$$
$\uparrow$ . 
* [16] M. C.  

I(ρ
ξ t
) ≤ 8I(ρ
ξ
$$\left(P t_{0}\right)^{\frac{1}{2}}$$
$\mathbf{r}\mathbf{A}$
) + cη2
kd, ∀Tk ≤ t0 ≤ t ≤ Tk+1. **(3.19)**
Clearly, with a factor d
−1/2in the Lipschitz constant in Assumption **3.1, the bounds of**
the relative entropy and Fisher information are linear in d.

## 3.3 Main Theorems

Equipped with the preparation work before, we are then able to establish a sharp uniformin-time second order error estimate for SGLD in terms of KL-divergence. Our analysis for SGLD is from local to global. The following local estimation is crucial **to our main** result, and the η 2**term here is the core of our** O(η 2**) bound in the main theorem. To avoid**
overloading the notation, the dependence on the size of function family N**, the dimension** d, the temperature β, and other parameters in Assumption 3.1, 3.2 **are implicit.**
Proposition 3.2. Consider the probability density functions ρt, ρ¯t for Xt, X¯t **defined in**
(1.3), (1.7). Then under Assumption 3.1, 3.2**, there exist positive constants** A0, A1, ∆0 independent of k and d such that when ηk < ∆0**, the following local estimation holds:**
d dtDKL(¯ρt||ρt) ≤ −A0DKL(¯ρt||ρt) + A1η 2 k
(d + I(¯ρTk
)), ∀t ∈ [Tk, Tk+1). **(3.20)**
For the convenience of readers, we move the proof of Proposition 3.2 **to the next section.**
Combining this local estimation for SGLD and the previous result for estimating the Fisher information of ULA (fixed batch SGLD), it is not difficult to obtain the following main theorem.

Define the following piecewise-constant function f:

$\pm1$). 
$$f(t):=\sum_{i=0}^{\infty}\eta_{i}^{2}\mathbf{1}_{[T_{i},T_{i+1})}(t),$$  on for set $E$. 
$$(3.21)$$

i 1[Ti,Ti+1)(t), **(3.21)**
where 1E **is the indicator function for set** E.

Theorem 3.2. **[Sharp error analysis for SGLD] Consider the probability density functions**
ρt, ρ¯t for Xt, X¯t defined in (1.3), (1.7). Suppose the time step sequence {ηk} is nonincreasing. Then under Assumption 3.1, 3.2**, there exists positive constants** ∆0, A0, c1, c2 independent of k and d **such that when** η0 ≤ ∆0,

$$D_{K L}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})\leq c_{1}\eta_{0}^{2}e^{-A_{0}T_{k}}+c_{2}d\int_{0}^{T_{k}}e^{-A_{0}(T_{k}-s)}f(s)d s,$$
−A0(Tk−s)f(s)ds, **(3.22)**
$$(3.22)$$

for f defined in (3.21). Consequently, if the non-increasing time step sequence {ηk} **converges to zero, and** P+∞
i=0 ηi = +∞**, the KL-divergence** DKL(¯ρTk||ρTk
) **also tends to zero.**
Proof of Theorem 3.2: By Proposition 3.2, since ηk ≤ η0 ≤ ∆0, and since the Fisher information I(ρ) is a convex functional with respect to ρ **(see [18, Lemma 4.2]), we have**

$$\frac{d}{dt}D_{KL}(\bar{\rho}_{t}||\rho_{t})\leq-A_{0}D_{KL}(\bar{\rho}_{t}||\rho_{t})+A_{1}\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right)$$ $$\leq-A_{0}D_{KL}(\bar{\rho}_{t}||\rho_{t})+A_{1}\eta_{k}^{2}\left(d+\mathbb{E}_{\xi}\mathcal{I}(\rho_{T_{k}}^{\xi})\right),\quad t\in[T_{k},T_{k+1}).$$
$$(3.23)$$

Then by Gr¨onwall's inequality, for all k**, we have**

DKL(¯ρTk||ρTk ) ≤ Eξ k X−1 i=0 Z Ti+1 Ti e −A0(Tk−s)A1η 2 i Äd + I(ρ ξ Ti )äds = A1d Z Tk 0 e −A0(T −s)f(s)ds + A1Eξ Z Tk 0 e −A0(T −s)I(ρ ξ Ti )fk(s)ds (3.24) ≤ A˜1d Z Tk 0 e −A0(T −s)f(s)ds + 8A1Eξ Z Tk 0 e −A0(T −s)I(ρ ξ s)f(s)ds and the last inequality of (3.24) is due to Lemma 3.3.
Clearly, f **is a piecewise constant, non-increasing, nonnegative function. Then by Lemma**
3.2, we are able to estimate the exponential-weighted sum of Fisher information along the path:

$$\int_{0}^{T_{k}}e^{-A_{0}(T-s)}{\cal I}(\rho_{s}^{\mathbf{\xi}})f(s)ds\leq M_{1}^{\prime}\eta_{0}^{2}e^{-A_{0}T_{k}}+M_{2}^{\prime}d\int_{0}^{T_{k}}e^{-A_{0}(T-s)}f(s)ds.\tag{3.25}$$

Here, the positive constanes M′1, M′2 are independent of the batch ξ **and the time** Tk.

Finally, combining (3.25) and (3.24), we have

$$D_{KL}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})\leq c_{1}\eta_{0}^{2}e^{-A_{0}T_{k}}+c_{2}d\int_{0}^{T_{k}}e^{-A_{0}(T_{k}-s)}f(s)ds,\tag{3.26}$$

where c1, c2, A0 are positive constant independent of the iteration number k **and the dimension** d.

Clearly, by (3.26), when the sequence {ηk} **decays to zero, and** P∞
k=0 ηk = +∞**, the**
KL-divergence DKL(¯ρTk||ρTk
) tends to zero. This then ends the proof.

As a direct corollary, if we consider the constant step size (or learning rate) case (ηk ≡ η),
the following sharp time-independent estimation can be established:
Corollary 3.1 (Sharp uniform-in-time error analysis for SGLD, constant step size η). Consider the probability density functions ρt, ρ¯t for Xt, X¯t defined in (1.3), (1.7)**. Suppose**
ηk = η, ∀k. Then, under Assumption 3.1, 3.2, there exist positive constants c , ∆0 independent of t **such that for all** η ∈ (0, ∆0),

$$\operatorname*{sup}_{t>0}D_{K L}(\bar{\rho}_{t}||\rho_{t})\leq c d\eta^{2}.$$
DKL(¯ρt||ρt) ≤ cdη2. **(3.27)**
Since ULA can be viewed as a special case of SGLD when b ξ ≡ b **(or the batch size** S
equals N **for the special case (1.2)), we have the following direct corollary:**
Corollary 3.2 (Sharp uniform-in-time error analysis for ULA, constant time step η). Consider the probability density functions ρt and ρˆt defined in (1.3), (2.6)**. Suppose** ηk = η, ∀k.

Then, under Assumption 3.1, 3.2, there is a positive constant c independent of t and ∆0 > 0 such that for all η ∈ (0, ∆0),
sup t>0 DKL(ˆρt||ρt) ≤ cdη2. **(3.28)**
Based on our main result, Theorem 3.2 or Corollary **3.1, we are able to obtain the**
following corollaries, which are useful in many practical tasks.

First, we choose special case for the decaying time step sequence {ηk}
+∞
k=0**, and applying**
Theorem **3.2, we obtain the following asymptotic convergence rate:**
Corollary 3.3 (asymptotic rate for special case). Suppose Assumption 3.1, 3.2 **hold. Set**
ηi = (ℓ + i)
−θ, i ∈ N, with θ ∈ (0, 1) being the decaying coefficient. Here, ℓ **is a positive**
integer such that η0 ≤ ∆0, where ∆0 > 0 is a positive constant obtained in Theorem 3.2. Then there exist k0 > 0, c > 0 such that ∀**k > k**0,

$$D_{K L}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})\leq c d\left(\frac{1}{k}\right)^{2\theta}\,,$$
ã2θ, **(3.29)**
Proof of Corollary 3.3: For θ ∈ (0, 1), by Theorem **3.2, we have**

DKL(¯ρTk||ρTk ) ≤ c1e −A0Tk + c2d Ñ⌊ X k/2⌋ i=1+⌊k/2⌋ é Ä(ℓ + i) −2θÄe −A0(Tk−Ti) − e −A0(Tk−Ti−1)ää i=1 +X k ≤ c1e −A0Tk + c ′ 2dÄe −A0(Tk−T⌊k/2⌋) − e −A0Tkä+ c ′ 2d Å2 k ã2θÄ1 − e −A0(Tk−T1+⌊k/2⌋)ä ≤ c1e −A0Tk + c ′ 2de−A0(Tk−T⌊k/2⌋) + c ′ 2d Å2 k ã2θ. (3.30)
$$(3.29)$$
$$(3.31)$$
As k → +∞, Tk ∼Pk i=1 i
−θ ∼ k 1−θ**. Hence,** e
−A0Tk and e
−A0(Tk−T⌊k/2⌋) **decay much faster**
than k
−2θ as k → +∞. Therefore, there exists k0 > 0 such that when **k > k**0,

$$D_{K L}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})\leq c d\left(\frac{1}{k}\right)^{2\theta},$$

where c is a positive constant independent of k**. This is what we want.**

## 4 Delayed Proof For The Local Estimation

In this section, we prove the crucial local analysis result of this paper, Proposition **3.2. For**
convenience, the proof is still a high-level overview and more technical details can be found in the Appendix.

Proof of Proposition 3.2: **We prove this local result following three main steps.**
STEP 1: **estimate time derivative of KL-divergence** d
dtDKL(¯ρt||ρt**) via Fokker-Planck**
equations.
Firstly, note that SGLD at discrete time points is a Markov chain (which is timehomogeneous when ηk **is a constant), and ¯**ρTk
is the law at Tk**. Recall that** ρ
ξ
t**is the**
probability density of the fixed-batch version of SGLD (1.7) for a given sequence of batches
ξ := (ξ0, ξ1, · · · , ξk, · · ·**) so that ¯**ρTk = Eξ
îρ
ξ
Tk
ó**. Moreover, by Markov property, we are able**
to define
$$\bar{\rho}_{t}^{\xi_{k}}:=\mathbb{E}\left[\rho_{t}^{\xi}\Big|\xi_{i},\,i\geq k\right]=\mathcal{S}_{T_{k},t}^{\xi_{k}}\bar{\rho}_{T_{k}},\quad t\in[T_{k},T_{k+1}),$$
, t ∈ [Tk, Tk+1), **(4.1)**
where the operator S
ξk Tk,t is the evolution operator from Tk to t **for the Fokker-Planck equation**
of the continuous SGLD (1.7) derived in Lemma **2.1, for some given** ξk:

$$\partial_{t}\bar{\rho}_{t}^{\xi_{k}}=-\nabla\cdot(\bar{\rho}_{t}^{\xi_{k}}\bar{b}_{t}^{\xi_{k}})+\beta^{-1}\Delta\bar{\rho}_{t}^{\xi_{k}},\quad\bar{\rho}_{T_{k}}^{\xi_{k}}=\bar{\rho}_{T_{k}},$$
, **(4.2)**
where $t\in[T_{k},T_{k+1})$ and 
$$\bar{b}_{t}^{\xi_{k}}(x):=\mathbb{E}\left[b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)|\bar{X}_{t}=x,\xi_{k}\right],\quad t\in\left[T_{k},T_{k+1}\right).$$
$$T_{k+1}),$$
$$(4.2)$$
$$(4.3)$$

Next, we calculate d dtDKL(¯ρt||ρt**) based on (4.2). Since ¯**ρt = Eξk
[¯ρ ξk t] for t ∈ [Tk, Tk+1),
by (4.2) we have
∂tρ¯t = Eξk î**−∇ ·** (
¯b ξk t ρ¯
ξk t) + β
−1∆¯ρ ξk t ó. **(4.4)**
Then, using the Fokker-Planck equations (4.4), (2.4) for ¯ρt and ρt**, respectively, we are able**
to calculate the following time derivative of the KL-divergence in the time interval [Tk, Tk+1):

d dtDKL(¯ρt||ρt) = Z(∂tρ¯t) Ålog ρ¯t ρt + 1ãdx + Z(∂tρt) Å − ρ¯t ρt ãdx = (Eξk ( ¯b ξk t ρ¯ ξk t) − β −1∇ρ¯t) · (∇ log ρ¯t ρt ) + (bρt − β −1∇ρt) · (−∇ρ¯t ρt )dx. (4.5) = Z Å(bρ¯t − β −1∇ρ¯t) · (∇ log ρ¯t ρt ) + (bρt − β −1∇ρt) · (−∇ρ¯t ρt ) ãdx + ZEξk î( ¯b ξk t − b ξk)¯ρ ξk t ó· (∇ log ρ¯t ρt )dx + ZEξk îb ξk ρ¯ ξk t − bρ¯t ó· (∇ log ρ¯t ρt )dx
Note that |b ξk ρ¯
ξk t − bρ¯t| is of order O**(1). The mechanism is that ¯**ρ ξk tis close to ¯ρt **and using**
the consistency of random batch Eξk
-b ξk (x)= b(x**). This can cancel the leading error.**
Hence, we rearrange the terms to get

$$\frac{d}{dt}D_{KL}(\bar{\rho}_{t}||\rho_{t})=\left(-\beta^{-1}\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}dx\right)+\left(\int\mathbb{E}_{\xi_{t}}\left[(\bar{b}_{t}^{\xi_{t}}-b^{\xi_{t}})\bar{\rho}_{t}^{\xi_{t}}\right]\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})dx\right)\tag{4.6}$$ $$+\left(\int\mathbb{E}_{\xi_{t}}\left[(b^{\xi_{t}}-b)(\bar{\rho}_{t}^{\xi_{t}}-\bar{\rho}_{t})\right]\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})dx\right)$$ $$:=J_{1}+J_{2}+J_{3}.$$
(4.6)
For J2**, by Young's inequality,**

$$\begin{split}J_{2}&=\mathbb{E}_{\xi_{k}}\left[\int(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}})\bar{\rho}_{t}^{\xi_{k}}\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})dx\right]\\ &\leq\beta\mathbb{E}_{\xi_{k}}\int|\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}|^{2}\bar{\rho}_{t}^{\xi_{k}}dx+\frac{1}{4\beta}\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}dx,\end{split}\tag{4.7}$$  iv important.  
where γ **is a positive constant.**
For J3, our approach is to introduce another copy of SGLD Y¯ **such that**
- Y¯Tk = X¯Tk
;
- the Browmian Motion are the same in [Tk, Tk+1);
- the batch ˜ξk on [Tk, Tk+1**) is independent of** ξk.

Consequently, the corresponding density of the law ¯ρt ξ˜k for Y¯ **satisfy both (4.1) and (4.2),**
with ¯ρ ξ˜k Tk
= ¯ρTk
. Using the consistency of the random batch, we are able to obtain

$$J_{3}=\mathbb{E}_{\xi_{k},\bar{\xi}_{k}}\int\left[(b^{\xi_{k}}-b)(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\bar{\xi}_{k}})\right]\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})d x$$
)dx **(4.8)**
Then by Young's inequality we have:

$$J_{3}\leq\beta\mathbb{E}_{\xi_{k}},\xi_{k}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\tilde{\rho}_{t}^{\tilde{\xi}_{k}}-\tilde{\rho}_{t}^{\tilde{\xi}_{k}}|^{2}}{\tilde{\rho}_{t}^{\tilde{\xi}_{k}}}dx\right]+\frac{1}{4\beta}\int|\nabla\log\frac{\tilde{\rho}_{t}}{\rho_{t}}|^{2}\tilde{\rho}_{t}dx\tag{4.9}$$

where we applied the fact Eξk,ξ˜k|∇ log ρ¯t ρt| 2ρ¯
ξ˜k t = |∇ log ρ¯t ρt| 2ρ¯t**. The introduction of the**
independent copy of ˜ξk **is useful since we may apply the Girsanov transform later to estimate**
this quantitatively.

Now by Theorem 3.1, ρt **satisfies a LSI with a constant** λ 2C
LS
π**, namely,** ∀f ∈ C∞
>0,

$$Ent_{\rho_{t}}(f):=\int f\log fd\rho_{t}-\Big{(}\int fd\rho_{t}\Big{)}\log\Big{(}\int fd\rho_{t}\Big{)}\leq\lambda^{2}C_{\pi}^{LS}\int\frac{|\nabla f|^{2}}{f}d\rho_{t}.\tag{4.10}$$
Taking $f=\frac{\bar{\rho}_t}{\rho_t}$, one has:
$$\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}d x\geq\frac{1}{\lambda^{2}C_{\pi}^{L S}}D_{K L}(\bar{\rho}_{t}||\rho_{t}).$$
DKL(¯ρt||ρt). **(4.11)**
Then, combining (4.6), (4.7), (4.9), and (4.11), one has d dtDKL(¯ρt||ρt) ≤ −A0DKL(¯ρt||ρt)

$$\leq-A_{0}D_{KL}(\bar{\rho}_{t}||\rho_{t})$$ $$+\beta\,\mathbb{E}_{\xi_{k}}\left[\int|\tilde{b}_{t}^{\xi_{k}}-b^{\xi_{k}}|^{2}\bar{\rho}_{t}^{\xi_{k}}\,dx\right]+\beta\,\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\tilde{\rho}_{t}^{\xi_{k}}-\tilde{\rho}_{t}^{\xi_{k}}|^{2}}{\tilde{\rho}_{t}^{\xi_{k}}}dx\right],\tag{4.12}$$
$$(4.11)$$

where

$$A_{0}=\frac{\beta^{-1}}{2\lambda^{2}C_{\pi}^{L S}}>0.$$
> 0. **(4.13)**
With (4.12), to obtain the final estimate, one then needs to obtain an O(η 2**) estimate**
for the two terms: Eξk E
h|
¯b ξk t(X¯t) − b ξk (X¯t)| 2ξk iand Eξk,ξ˜k ïR|b ξk − b| 2 |ρ¯
ξ˜k t −ρ¯
ξk t | 2 ρ¯
ξ˜k t dxò.

STEP 2: **estimate** Eξk E
h|
¯b ξk t(X¯t) − b ξk (X¯t)| 2ξk i In this step, we aim to obtain an O(η 2 k
) bound for Eξk E
h|
¯b ξk t
(X¯t) − b ξk (X¯t)| 2ξk i**based**
on Taylor expansion for b ξk . Note that ξk **is fixed so we may follow the estimate for the**
Unadjusted Langevin Algorithm (ULA) in [35] in this step.

By Taylor expansion, ∀t ∈ [Tk, Tk+1),

$$\bar{b}_{t}^{\xi_{k}}(x)-b^{\xi_{k}}(x)=\mathbb{E}\left[b^{\xi_{k}}(\bar{X}_{T_{k}})-b^{\xi_{k}}(\bar{X}_{t})|\bar{X}_{t}=x,\xi_{k}\right]$$ $$=\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]\cdot\nabla b^{\xi_{k}}(x)$$ $$\quad+\frac{1}{2}\mathbb{E}\left[\left(\bar{X}_{T_{k}}-\bar{X}_{t}\right)^{\otimes2}:\int_{0}^{1}\nabla^{2}b^{\xi_{k}}\left((1-s)\bar{X}_{t}+s\bar{X}_{T_{k}}\right)ds\Big{|}\bar{X}_{t}=x,\xi_{k}\right].$$  It is proved.  
For simplicity, we denote

$$\bar{r}_{t}(x):=\frac{1}{2}\mathbb{E}\left[\left(\bar{X}_{T_{k}}-\bar{X}_{t}\right)^{\otimes2}:\int_{0}^{1}\nabla^{2}b^{\xi_{k}}\left((1-s)\bar{X}_{t}+s\bar{X}_{T_{k}}\right)d s\Big{|}\bar{X}_{t}=x,\xi_{k}\right].$$
ô. **(4.14)**
In Lemma A.2 , we show that for t ∈ [Tk, Tk+1),

$$(4.14)$$
$$\mathbb{E}\left[|{\bar{r}}_{t}({\bar{X}}_{t})|^{2}\Big|\xi_{k}\right]\leq c d(t-T_{k})^{2},$$

2, **(4.15)**
where c is a positive constant independent of k, d and ξk**. For the first term** E[X¯Tk −X¯t|X¯t =
x, ξk] · ∇b ξk (x**), by Bayes' law we have**

$$\begin{split}\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}^{\xi}=x,\xi_{k}]&=\int(y-x)P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})dy\\ &=\int(y-x)\frac{\bar{\rho}_{T_{k}}^{\xi_{k}}(y)P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})}{\bar{\rho}_{t}^{\xi_{k}}(x)}dy.\end{split}\tag{4.16}$$

Clearly, the distribution P(X¯t = x|X¯Tk = y, ξk**) is Gaussian, namely,**

$$P\left(\tilde{X}_{t}=x|\tilde{X}_{T_{k}}=y,\xi_{k}\right)=\left(4\pi\beta^{-1}(t-T_{k})\right)^{-\frac{\phi}{2}}\exp\left(-\frac{|x-y-b^{\zeta_{k}}(y)(t-T_{k})|^{2}}{4\beta^{-1}(t-T_{k})}\right),\tag{4.17}$$

13

which motivates us to calculate (4.16) via integration by parts. Indeed, we show in Lemma
A.3 **that**
$$\int\left|\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}\right]\right|^{2}\bar{\rho}_{t}^{\xi_{k}}(x)dx\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right),\quad\forall t\in[T_{k},T_{k+1}),\tag{4.18}$$
where I(ρ) := Rρ|∇ log ρ| 2dx is the Fisher information, and c is a positive constant independent of k, d and ξk. Then, it is left to give an O**(1) estimate for each Fisher information**
I(¯ρTk
) in ULA, which has been done in Section **3.2.**
STEP 3: **estimate** Eξk,ξ˜k ïR|b ξk − b| 2 |ρ¯
ξ˜k t −ρ¯
ξk t | 2 ρ¯
ξ˜k t dxò.

```
By the boundedness assumption in Assumption 3.1, we only need to estimate R |ρ¯
                                                                         ξ˜k
                                                                         t −ρ¯
                                                                             ξk
                                                                             t
                                                                               |
                                                                               2
                                                                          ρ¯
                                                                           ξ˜k
                                                                           t
                                                                                dx.

```

Recall that ¯ρ ξk t **and ¯**ρ ξ˜k t are the densities of the laws of X¯ and Y¯ **with two independent batches**
ξk and ˜ξk for interval [Tk, Tk+1**). Hence the problem is again reduced to the ULA case.**
We first note that

$$\int\frac{|\bar{\rho}_{t}^{\bar{\xi}_{k}}-\bar{\rho}_{t}^{\bar{\xi}_{k}}|^{2}}{\bar{\rho}_{t}^{\bar{\xi}_{k}}}d x=\int\left|\frac{\bar{\rho}_{t}^{\bar{\xi}_{k}}}{\bar{\rho}_{t}^{\bar{\xi}_{k}}}-1\right|^{2}\bar{\rho}_{t}^{\bar{\xi}_{k}}d x,$$
$$(4.19)$$

and the property of path measures gives

$$\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\xi_{k}}}(x)=\mathbb{E}\left[\frac{d P_{\bar{X}}}{d P_{\bar{Y}}}\left|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k}\right.\right],$$
, **(4.20)**
where PX¯ and PY¯ are path measures in C[Tk, Tk+1]; R
d**. Let**

$$(4.21)$$

X¯Tk = Y¯Tk = y ∼ ρ¯Tk
.

Then for t ∈ [Tk, Tk+1**), Girsanov transform gives:**

$${\frac{d P_{\bar{X}}}{d P_{\bar{Y}}}}(\bar{Y})=\exp\left(\sqrt{\frac{\beta}{2}}\int_{T_{k}}^{T_{k+1}}(b^{\bar{k}_{k}}-b^{\bar{k}_{k}})(y)d W_{s}-{\frac{\beta}{4}}\int_{T_{k}}^{T_{k+1}}\left|(b^{\bar{k}_{s}}-b^{\bar{k}_{s}})(y)\right|^{2}d s\right).$$
dså. **(4.21)**
Details for (4.20) and (4.21) can be found in Corollary A.1 of Appendix **A. Denote**

$$\tilde{b}(y):=\frac{1}{\sqrt{2\beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y).$$
p2β−1
ξkä(y). **(4.22)**
Then, for t ∈ [Tk, Tk+1**), the martingale property gives**

$$\frac{\frac{\tilde{\rho}_{t}^{\xi_{k}}}{\tilde{\rho}_{t}^{\xi_{k}}}(x)=\mathbb{E}\left[\exp\left(\int_{T_{k}}^{t}\tilde{b}(y)d W s-\frac{1}{2}\int_{T_{k}}^{t}|\tilde{b}(y)|^{2}d s\right)\right]\tilde{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k}\right].$$

Hence,

Z ρ¯ ξk t ρ¯ ξ˜k t − 1  2 ρ¯ ξ˜k t dx = Zρ¯ ξ˜k t (x) E he R t Tk ˜b(Y¯Tk )dWs− 12 R t Tk |˜b(Y¯Tk )| 2dsY¯t = x, ξk, ˜ξk i− 1  2 dx = Zρ¯ ξ˜k t(x)  Z e √β 2 ˜b(y)(x−y−(t−Tk)b ξ˜k (y))− 12 |˜b(y)| 2(t−Tk) − 1 P(X¯Tk = y|Y¯t = x, ξk, ˜ξk)dy  2 dx Above we have used the fact that Y¯t = y + b ξ˜k (y)(t − Tk) + p2β−1(Wt − WTk ), resulting in that p2β−1(Wt − WTk ) = x − y − b ξ˜k(y)(t − Tk).
Now in order to handle the integration of the term e
√β 2
˜b(y)(x−y−(t−Tk)b ξ˜k (y))− 12 |˜b(y)| 2(t−Tk),
we split it by

$$\begin{array}{l}{{e^{\sqrt{\frac{\beta}{2}}\tilde{b}(y)(x-y-(t-T_{k})\tilde{b}^{\tilde{k}_{k}}(y))-\frac{1}{2}|\tilde{b}(y)|^{2}(t-T_{k})}-1}}\\ {{=\sqrt{\frac{\beta}{2}}\tilde{b}(y)(x-y)+\left(-\sqrt{\frac{\beta}{2}}\tilde{b}(y)\delta^{\tilde{k}_{k}}(y)-\frac{1}{2}|\tilde{b}(y)|^{2}\right)(t-T_{k})+\left(e^{z}-z-1\right)}}\\ {{=K_{1}+K_{2}+K_{3},}}\end{array}$$
$$(4.23)$$
$$(4.24)$$
$$(4.26)$$
$$(4.27)$$

where

$$z:=\sqrt{\frac{\beta}{2}}\,\bar{b}(y)(x-y-(t-T_{k})b^{\hat{\ell}_{k}}(y))-\frac{1}{2}|\bar{b}(y)|^{2}(t-T_{k}).$$

Then

Z ρ¯ ξk t ρ¯ ξ˜k t − 1  2 ρ¯ ξ˜k t dx = Zρ¯ ξ˜k t (x)  Z(K1 + K2 + K3) P(X¯Tk = y|Y¯t = x, ξk, ˜ξk)dy  2 dx.
$$d x.\,$$ $$(4.25)$$
For K1 =
»β 2
˜b(y)(x − y), using integration by parts again, we prove in Lemma A.4 in Section A that for t ∈ [Tk, Tk+1),

$$\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{1}\,P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right).$$
)). **(4.26)**
where c **is a positive constant independent of** k, d,
˜ξk and ξk.

For K2 = (−
»β 2
˜b(y) · b ξ˜k (y)) − 12|
˜b(y)| 2)(t − Tk**), using the boundedness and Lipshitz**
condition in Assumption 3.1, we prove in Lemma A.5 that for t ∈ [Tk, Tk+1),

$$\int\rho_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2}\,P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2},$$
k, **(4.27)**
where c **is a positive constant independent of** k, d,
˜ξk and ξk.

For the remaining term K3**, after applying Jensen's inequality and the tower property of**
conditional expectation, we prove in Lemma A.6 that for t ∈ [Tk, Tk+1),

$$\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{3}\,P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.$$
$$(4.28)$$
k. **(4.28)**
where c **is a positive constant independent of** k, d,
˜ξk and ξk.

Equipped with the estimation for the integration of K1, K2, and K3**, one finally obtains**

$$\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\xi_{k}}}-1\right|^{2}\bar{\rho}_{t}^{\xi_{k}}d x\leq c\eta_{k}^{2}\left(1+\mathcal{I}(\bar{\rho}_{T_{k}})\right),\quad\forall t\in[T_{k},T_{k+1}),$$

where c **is a positive constant independent of** k, d,
˜ξk and ξk**. Combining with the estimate**
for Fisher information obtained in Section **3.2, one is able to get an** η 2 k estimation for the term Eξk,ξ˜k ïR|b ξk − b| 2 |ρ¯
ξ˜k t −ρ¯
ξk t | 2 ρ¯
ξ˜k t dxò**. Note that after taking the expectation** Eξk,ξ˜k
[·**], the**
bound is still of order η 2 k
, since the bounds above are all independent of the batches ξk,
˜ξk.

Combining the results in STEP 2 and STEP 3 finally leads to the desired result:
d dtDKL(¯ρt||ρt) ≤ −A0DKL(¯ρt||ρt) + A1dη2 k
(1 + I(¯ρTk
)), ∀t ∈ [Tk, Tk+1), **(4.30)**
where A0, A1 are positive constants independent of k, d**, and** ξk.

$$(4.29)$$

## 5 Discussion 5.1 Convergence To Equilibrium And Target Distribution - **Convergence To The Target Distribution**

Viewing SGLD as a popular sampling algorithm, many researchers would **care about** the convergence rate to the target distribution. An important extension of Theorem 3.2 or Corollary 3.1 **is about the distance between the SGLD iteration and the target** distribution, namely, the invariant distribution of the Langevin diffusion (1.3). When we are doing sampling tasks, this result is an important measure for the efficiency of a sampling algorithm. Note that the rate in our result can be viewed **as a great**
improvement compared with former work like [36, 53, **16], where the optimal bound so** far is of order O(
√η**) in terms of Wasserstein distance or total variation. Meanwhile,**
as will be derived in the followings, we obtain a bound of order O(η).

To compare our result with former ones more directly, we consider the constant step size (or learning rate) η. We consider the Wasserstein-2 (W2) distance, the Wasserstein1 (W1**) distance, and the total variation (TV) distance in the following discussion.**
Firstly let us recall the definition of Wp distance (p = 1, **2 here) and TV distance**
between two distributions µ and ν **[45]:**

$$W_{p}(\mu,\nu):=\left(\operatorname*{inf}_{\gamma\in\Pi(\mu,v)}\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}|x-y|^{p}d\gamma\right)^{1/p},$$
and
$$D_{T V}(\mu,\nu):=\operatorname*{sup}_{A\in{\mathcal{B}}(\mathbb{R}^{d})}|\mu(A)-\nu(A)|.$$

Here, Π(µ, ν) means all joint distributions whose marginal distributions are µ and ν, respectively. Now, by Corollary **3.1, we have**

$$(5.1)$$
$\left(\begin{matrix}5.2\\ 5\end{matrix}\right)$ . 
$$\eta^{2},\quad t>0,$$
$\left(5.3\right)^{2}$
$\geq\:\alpha\nu$  . 
DKL(¯ρt||ρt) ≤ cdη2, t > 0, **(5.3)**
where c is independent of t, and η **is the constant step size (or learning rate).**
Also, since the invariant distribution π satisfies a Log-Sobolev inequality by Assumption **3.2, we have the following exponential convergence for the Langevin diffusion**
(1.3), which is a classical result [34]:

$\mathcal{D}_{KL}(\rho_0||\mathbb{Z}^n)$
$\mathbf{a}$
DKL(ρt||π) ≤ e
−γtDKL(ρ0||π**) (5.4)**
It is well-known that we can bound the W2, W1**, and TV distance with square root**
of the KL-divergence by Talagrand transportation inequality [39, **48], the weighted** Csiszar-Kullback-Pinsker inequality [6], and the Pinsker's inequality [42], respectively.

Note that for W2 **distance and TV distance, the constant** c
′ 1 above is dimension-free; for W1 **distance, the constant** c
′
1 **above is of** O(d 1 2 **). Together with the triangle inequality**
for W2, W1**, and TV distances, one has the following:**
Corollary 5.1. Consider the probability density functions ρt, ρ¯t for Xt, X¯t **defined**
in (1.3), (1.7). Suppose Assumption 3.1, 3.2 **hold. Then the following holds:**

(a) If ηk = η, ∀k**, then there exist positive constants** c W1 1, c W1 2, c W2 1, c W2 2, c T V
1, c T V
2, γ , ∆0 independent of t and d **such that for all** η ∈ (0, ∆0),
∗ W1(¯ρt, π) ≤ c W1 1dη + c W1 2d 1 2 e
− 12 γt,
∗ W2(¯ρt, π) ≤ c W2 1d 1 2 η + c W2 2e
− 12 γt,
∗ DT V (¯ρt, π) ≤ c T V
1 d 1 2 η + c T V
2e
− 12 γt.

(b) If ηi = (ℓ + i)
−θ, with θ ∈ (0, 1) **being the decay rate, then there exist positive**
constants cW1, cW2, c T V independent of k and d **such that**
∗ W1(¯ρTk
, π) ≤ cW1 d1k θ,
∗ W2(¯ρTk
, π) ≤ cW2 d 1 21k θ,
∗ DT V (¯ρTk
, π) ≤ c T V d 1 21k θ.
By Corollary **5.1, we can conclude the steps of simulations for SGLD needed to achieve** a tolerance ǫ **under different distances.**
Corollary 5.2. Under Assumption 3.1, 3.2, to achieve an error smaller than ǫ**, one**
needs the following numbers of simulations of SGLD respectively under the corresponding distances:
- N = O(dǫ−1**(log** ǫ
−1 **+ log** d 1 2 )) for W1 **distance (by setting** η = O(d
−1ǫ));

- N = O(d 1 2 ǫ
−1log ǫ
−1) for W2 **distance (by setting** η = O(d
− 12 ǫ)) ;

$$N=O(d^{\frac{1}{2}}\epsilon^{-1}\log\epsilon^{-1})\,\,f o r\,\,\,1$$

−1) **for TV distance (by setting** η = O(d

$$(d^{-1}\epsilon)).$$

These results are improved compared to existing results in literature.

## - **Ergodicity Of Sgld**

An important property of SGLD that remains to be studied is its ergodicity, which then ensures the existence of the invariant distribution of the SGLD dynamic and enables us to explore the convergence of the algorithm itself. In [7], the authors considered the ergodicity of SGLD under W2 **distance with the assumptions of global strong convexity**
of U **and 4-th order Lipshitz condition.** In our setup, we do not have the global strong convexity of U **and only have second** order Lipschitz condition. Luckily, the ergodicity could be studied using reflection coupling [14, **24], under mild assumptions. In particular, we have the following claim.** In fact, we need to assume the followings, which can be understood **as the positive**
upper and lower bound of ∇2U outside the circle B(0, R**) in** R
d.

Assumption 5.1. There exist R0 > 0, κ0 > 0, K > 0 **such that the followings hold:**
(a) (locally nonconvex) The Hessian matrix of U **is uniformly positive definite outside**
B(0, R0)**, namely,**

$$\nabla^{2}U(x)\succeq\kappa_{0}I_{d},\quad\forall x\in\mathbb{R}^{d}\setminus B(0,R_{0});$$
d\ B(0, R0**); (5.5)**
(b) (global uniform-in-batch Lipshitz) ∀**x, y** ∈ R

$$\in\mathbb{R}^{d},\ \forall\xi,$$
$\left(5.5\right)^{2}$
$$\left|\nabla U^{\xi}(x)-\nabla U^{\xi}(y)\right|\leq K|x-y|^{2}.$$
$$(5.6)$$

2. **(5.6)**
Then the following claim holds.

Proposition 5.1. Suppose Assumption 5.1 holds. Denote ∆0 := supk ηk**. There exist**
positive constants ∆¯ , c0, c1 such that if ∆0 < ∆¯ **, then for any two initial distributions**
µ0 and ν0, denoting µ¯t and ν¯t **to be the corresponding time marginal distributions for**
the time continuous interpolation of SGLD algorithm (1.7)**, it holds that**
W1(¯µTk
, ν¯Tk
) ≤ c0e
−c1TkW1(µ0, ν0). **(5.7)**
Consequently, if the step size (or learning rate) is constant ηk ≡ η **such that the**
discrete chain is time-homogeneous, then the SGLD as a discrete time Markov chain has an invariant measure ˜π **by the Banach contraction mapping theorem. Then, we** have the following conclusion Corollary 5.3. Let ηk ≡ η. Under Assumption 5.1**, there exist positive constants** ∆¯ ,
c0, c1 such that if η ≤ ∆¯ , then for any initial distribution ρ0 **with finite first moment,**
the SGLD iteration has an invariant measure π˜ time marginal distribution ρ¯t of **(1.7)**
convergences exponentially to π˜ **in terms of W-1 distance:**
W1(¯ρnη, π˜) ≤ c0e
−cnηW1(ρ0, π˜). **(5.8)**
Equipped with the ergodicity results for SGLD and combining the results in Corollary 5.1, we are able to estimate the distance between the target distribution and the invariant distribution of SGLD itself:
W1(˜π, π) ≤ cη. **(5.9)**
This is improved compared to existing results in literature. Detailed derivation can be found in [1].

## 5.2 Other Discussions - **Justification Of Sharpness**

A natural question for our results is: is this bound we obtained really **a "sharp" one?** To answer this question, we simply consider the following Ornstein-Uhlenbeck (O-U)
process in R
1**, which satisfies all our assumptions.**

$$(5.11)$$

dX = −Xdt + dW. **(5.10)**
Its solution has an explicit expression:

$$X_{t}=e^{-t}X_{0}+\int_{0}^{t}e^{s-t}d W_{s}.$$
s−tdWs. **(5.11)**
Consider the full-batch SGLD, namely, the Euler-Maruyama scheme **for (5.10) with** constant step size η:
XˆTk+1 = XˆTk − ηXˆTk + (WTk+1 − WTk
). **(5.12)**
Suppose Xt, Xˆt are Gaussion, and E[X0] 6= 0, then we are able to calculate the KLdivergence without much difficulty. Indeed, by definition, at T := kη**, their mean and**
variance are given by µ1 := E[XT ] = e
−T E[X0] ,

$$\Xi\left[X_{T}\right]=\mathrm{e}^{-\Xi\left[X_{0}\right]}$$
$$\sigma_{1}^{2}:=\mathrm{Var}(X_{T})=e^{-2T}\mathrm{Var}(X_{0})+\frac{1}{2}\left(1-e^{-2T}\right),$$
and
$$\mu_{2}:=\mathbb{E}\left[{\hat{X}}_{T}\right]=(1-\eta)^{(T/\eta)}\mathbb{E}\left[X_{0}\right],$$
$\sigma^2_2\ \raisebox{-0.6ex}{\scriptsize\raisebox{-0.6ex}{$\stackrel{\circ}{=}$}}\ \raisebox{-0.6ex}{\scriptsize\raisebox{-0.6ex}{$\stackrel{\circ}{=}$}}\ \raisebox{-0.6ex}{\scriptsize\raisebox{-0.6ex}{$\stackrel{\circ}{=}$}}$
2:= Var(XˆT **) = (1** − η)
2(T /η)Var(X0) + 1
$$X_{0})+\frac{1}{2-\eta}\left(1-(1-\eta)^{2(T/\eta)}\right).$$

Clearly, for small η,

$$\mu_{1}-\mu_{2}|=|\mathbb{E}\left[X_{0}\right]|\left(e^{-T}-(1-\eta)^{(T/\eta)}\right)\geq|\mathbb{E}\left[X_{0}\right]|\left(e^{-t}-e^{-t-t\eta/2}\right)$$ $$>|\mathbb{E}\left[X_{0}\right]|\,e^{-T}\left(\frac{1}{2}\eta T-\frac{1}{8}\eta^{2}T^{2}\right)>\frac{1}{4}\left|\mathbb{E}\left[X_{0}\right]\right|e^{-T}T\eta$$

and σ 2 2 < 2σ 2 1
.

Also by direct calculation, the KL-divergence between two Gaussian **distributions**
N(µ1, σ2 1
), N(µ2, σ2 2
) is given by

$$D_{KL}\left(N(\mu_{1},\sigma_{1}^{2})||N(\mu_{2},\sigma_{2}^{2})\right)=\left(\frac{1}{2}\log\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}+\frac{1}{2}\left(\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}-1\right)\right)+\frac{(\mu_{1}-\mu_{2})^{2}}{2\sigma_{2}^{2}}\tag{5.13}$$ $$\geq0+\frac{(\mu_{1}-\mu_{2})^{2}}{2\sigma_{2}^{2}}.$$

Therefore,

$$D_{K L}(\bar{\rho}_{T}||\rho_{T})\geq{\frac{(1/16)\left|\mathbb{E}\left[X_{0}\right]\right|^{2}e^{-2T}T^{2}}{4\sigma_{1}(T)^{2}}}$$
$\left[\begin{array}{c}0\\ 0\end{array}\right]^{2}e^{-2T}T^{2}$  $T)^{2}$
This then indicates that our η 2 **bound is a sharp one.**

## - **The Role Of Consistency Of Random Batch Technique**

As a variant of ULA, the key difference of SGLD is the introduction of **the minibatch technique, which reduces the computational cost. To understand the error and**
mechanism for the sharp error estimate, let us take ηk ≡ η.

For each single step, the error of the drift is O**(1). The methods involving random** batches (such as the SGD and the random batch methods) have a strong error like (see for example [22])
»EkX − X¯ k 2 ∼
»(e kη − 1)η.

Clearly, the strong error decays like √η**, which is actually sharp. As mentioned in [22],**
the averaging effect in time ensures a convergence like "law of large numbers" in time so the convergence rate is √η**. The strong error estimate can imply that**

$$(\mathbb{E}_{\xi}W_{2}^{2}(\rho_{t}^{\xi},\rho_{t}))^{1/2}\sim\sqrt{(e^{k\eta}-1)\eta}.$$

This indicates that the fluctuation of the trajectory and ρ ξ tis really like √η**. Hence,**
the existing error estimates of SGLD based on the trajectory estimates can achieve
√η **at most. Moreover, such an estimate based on trajectory estimate can only give**
an O(η**) one step error of the SGLD under Wasserstein distance (the** O(
√η**) global**
error is due to the time averaging over multiple intervals). The most important property of the random batch is its consistency:

$\left(5.15\right)^{2}$
$$\mathbb{E}_{\xi}\left[b^{\xi}(x)\right]=b(x),$$
ξ(x)= b(x), **(5.15)**
which can be interpreted as an unbiased approximation of the original drift function, as has been mentioned in (1.1). Consider one step. Starting from a common ρ0**, after**
one step, formally each ρ ξ η **has the following expression**
ρη = ρ0 + ηL
∗
ξ ρ0 + O(η 2),
where Lξ is the generator corresponding to batch ξ**, while**
ρη = ρ0 + ηL
∗ρ0 + O(η 2).

Hence, the error is like O(η**). Since the error of the drift can cancel if one takes average** across batches and thus one is motivated to take the average of all possible ρ ξ t
:

$$\bar{\rho}_{t}=\mathbb{E}_{\xi}\left[\rho_{t}^{\xi}\right],$$
ó, **(5.16)**
which is the true law of the SGLD. The obtained ¯ρt **is then expected to have** O(η 2)
local error compared to ρtn+1 **. Of course, direct proof using Wasserstein distances**
has some difficulty and we make use of the KL divergence to accomplish **the proof** motivated by the recent work [35]. Anyway, this intuition lays the foundation of our proof and is reflected in treating the terms in (4.5). In fact, the last term in (4.5), or b ξk ρ¯
ξk t − bρ¯t, can be as O**(1). The intuition is that the averaged drift should be** b and one may cancel the error: E(b ξk )ρ ξk t − bρ¯t **is small and one may have convergence.**
With this intuition, we rearrange b ξk ρ¯
ξk t − bρ¯t = E(b ξk − b)(¯ρ ξk t − ρ¯t)
At last, we remark that though ¯ρt is close to ρt**, in practice we do not repeat the**
experiment for many times and take the average. Instead, we only **generate a sequence** of the batches (ξ 0, · · · , ξk, · · ·**) and generate the samples. Even though we use a single**
b ξk **each step, the empirical distribution by the generated samples converges weakly**
to the invariant measure with error O(η**) under Wasserstein distance to the interested** distribution, due to the ergodicity of SGLD. Hence, one does not have to run SGLD
for many experiments to approximate ¯ρt **and further to approximate the invariant**
distribution with error O(η).

## - **Dependence On The Dimensionality**

The linear scaling with respect to d **arising in (3.17) and (3.19) is quite natural for the** entropy and Fisher information. In fact, if one considers cases where the dynamics in difference dimensions are decouple so that ρt(x) = Qd i=1 ρ
(i)
t(xi**), the dependence on**
dimension in the entropy and Fisher information would be linear.

As we have mentioned, the linear dependence in the our error bounds largely comes from with the factor d
−1/2in the Lipschitz constant in Assumption **3.1, and we have**
justified this below Assumption **3.1. A slight discrepancy of this intuition comes from**
DKL(ρ0||π), which by by condition (a) in Assumption 3.2 **satisfies**
DKL(ρ0||π) ≤ log λ.

This independence of the dimension is a consequence of the strong assumption Assumption **3.2. However, if we use a weaker assumption like** ρ0/π ≤ λ d**, there would be**
dimension dependence in the constant for log-Sobolev inequality of the Hooley-Stroock perturbation lemma. This may indicate that the Hooley-Stroock perturbation lemma is not sharp regarding the scalability in d.

## 6 Acknowledgement

This work is financially supported by the National Key R&D Program of **China, Project** Number 2021YFA1002800 and Project Number 2020YFA0712000. **The work of L. Li was** partially supported by NSFC 11901389 and 12031013, Shanghai Municipal Science and Technology Major Project 2021SHZDZX0102, Shanghai Science and Technology Commission Grant No. 21JC1402900, and Shanghai Sailing Program 19YF1421300.

## A Omitted Details In Section 3 And 4

In this section, we prove the details omitted in Section 3 and 4. Lemma A.2, A.3 **have been** proved in [35].

## A.1 Proof Of Proposition 3.1

The method for bounding the p**-th moment of fixed-batch SGLD is based on direct Itˆo**
calculation and basic inequalities. In the followings, we denote Fξ the σ**-algebra generated**
by ξk **for all** k ∈ N.

Proof of Proposition 3.1: **By definition, for fixed batch sequence** ξ, dX¯t = b ξk(X¯Tk
)dt +p2β−1dW, t ∈ [Tk, Tk+1),
where we recall Tk =Pk−1 i=0 ηi. For p ≥ **2, by Itˆo's formula, we have**

$$d|\bar{X}_{t}|^{p}=p|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot\left(b^{\xi}(\bar{X}_{T_{k}})d t+\sqrt{2\beta^{-1}}d W\right),$$
$\sqrt{2\beta^{-1}}dW$)  $$+\beta^{-1}p|\bar{X}_{t}|^{p-2}\left(I_{d}+(p-2)\frac{\bar{X}_{t}\otimes\bar{X}_{t}}{|\bar{X}_{t}|^{2}}\right):I_{d}dt.$$  20
So

$$\frac{d}{dt}\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p}\right|\mathcal{F}_{\xi}\right]\leq p\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2}\bar{X}_{t}\cdot b^{\xi_{k}}(\bar{X}_{t})\right|\mathcal{F}_{\xi}\right]$$ $$+p\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2}\bar{X}_{t}\cdot\left(b^{\xi_{k}}(\bar{X}_{T_{k}})-b^{\xi_{k}}(\bar{X}_{t})\right)\right].$$

) − b ξk(X¯t)Fξ i+ β
−1p(p − 1)dE
h|X¯t| p−2Fξ i. **(A.1)**
Using the dissipation condition in Assumption **3.1, we can control the first term above,** namely, pE
h|X¯t| p−2X¯t · b ξk(X¯t)
Fξ i. −pE
h|X¯t| pFξ i+ pE
h|X¯t| p−2Fξ i.

By Young's inequality, for any δ > 0,

 $ \mathbb{E}\left[|\bar{X}_t|^{p-2}\Big|\mathcal{F}_\xi\right]\leq\delta d^{-1}\frac{p-2}{p}\mathbb{E}\left[|\bar{X}_t|^p\Big|\mathcal{F}_\xi\right]+\delta^{-\frac{p-2}{2}}d^{\frac{p-2}{2}}\frac{2}{p}$  erm_direct estimate gives... 
For the second term, direct estimate gives E
h|X¯t| p−2X¯t ·b ξk(X¯Tk
) − b ξk(X¯t)Fξ i≤ cE
h|X¯t| p−1|X¯t − X¯Tk|
Fξ i
. (t − Tk)E
h|b ξk(X¯Tk
)||X¯t| p−1Fξ i+p2β−1E
h|X¯t| p−1|N (0, t − Tk)|
Fξ i Note that b(·**) grows linearly only. Then, by Young's inequality, together with the fact that** t − Tk ≤ ηk**, one has**
E
h|X¯t| p−2X¯t ·b ξk(X¯Tk

$$\begin{array}{c}{{()-b^{\xi_{k}}(\bar{X}_{t}))\left|{\mathcal{F}_{\xi}}\right|}}\\ {{\qquad\qquad\lesssim(\eta_{k}^{p/(2(p-1))}+\eta_{k})\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p}\left|{\mathcal{F}_{\xi}}\right|+\eta_{k}\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p}\left|{\mathcal{F}_{\xi}}\right|+d^{\frac{p}{2}}.}\right]}\end{array}$$

Hence, d dtE
h|X¯t| pFξ i≤ −c1E
h|X¯t| pFξ i+ c3ηkE
h|X¯Tk| pFξ i+ c2d p 2 , t ∈ [Tk, Tk+1). **(A.2)**
Here, c1, c2, c3 are positive constants independent of t, d and ξ **but possibly dependent of**
p.

We claim that since there exists c
′
1 > **0 such that**
−c1 + c3ηk ≤ −c
′ 1
, ∀k, the moment is uniformly bounded.

In fact, applying the Gr¨onwall inequality,

In fact, applying the Gronwall inequality, $$\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p}\right|\mathcal{F}_{\xi}\right]\leq e^{-c_{1}(t-T_{k})}\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p}\right|\mathcal{F}_{\xi}\right]+\int_{T_{k}}^{t}e^{-c_{1}(t-s)}\left(c_{3}\eta_{k}\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p}\right|\mathcal{F}_{\xi}\right]+c_{2}d^{\frac{p}{2}}\right)ds.$$  defining
$$u^{\xi}(t):=\operatorname*{sup}_{0\leq s\leq t}\mathbb{E}\left[|{\bar{X}}_{s}|^{p}\Big|{\mathcal{F}}_{\xi}\right],$$
one thus finds

u
ξ(t) ≤ e
−c1(t−Tk)u
) $ u^{\xi}(T_k)+\int_{-\infty}^t e^{-c_1(t-s)}[c_3\eta_k u]$
Tk
ξ(s) + c2d
p
2 ]ds.

Then, it is not hard to find that u ξ(t) ≤ v ξ(t**) where**

$$\frac{d}{dt}v^{\xi}(t)=-c^{\prime}_{1}v^{\xi}(t)+c_{2}d^{\overline{\xi}},\quad t\in[T_{k},T_{k+1}),\ v^{\xi}(T_{k})\geq u^{\xi}(T_{k}).$$ (A.3)
$\square$
Remark A.1. **One may use an intermediate function satisfying the following to justify the**
above comparison principle:
d dtv˜
ξ(t) = −c1v˜
ξ(t) + c3ηkv˜
ξ(t) + c2d p 2 .

Since (A.3) holds for each time interval and the moment is continuous in time so one can concatenate them and conclude by induction that u ξ(t) ≤ v ξ(t**) with**

$$\frac{d}{d t}v^{\xi}(t)=-c_{1}^{\prime}v^{\xi}(t)+c_{2}d^{\frac{p}{2}},\quad v(0)=u(0)=\mathbb{E}|\bar{X}_{0}|^{p}.$$

Hence,
$$\mathbb{E}\left[|{\bar{X}}_{t}|^{p}\Big|{\mathcal{F}}_{\xi}\right]\leq c_{p}d^{\frac{p}{2}},\quad\forall t>0,$$
2 , ∀t > 0, **(A.4)**
where cp is a positive constant independent of t, d and ξ **but possibly dependent of** p.
For the exponential moment E-e
α|X|
p with small α**, after similar Itˆo's calculation, we**
are able to obtain
i< +∞. **(A.5)**
$$\operatorname*{sup}_{t>0}\mathbb{E}\left[e^{\alpha|\bar{X}_{t}|^{p}}\Big|\mathcal{F}\xi\right]<+\infty.$$
This then ends the proof.

## A.2 Proof Of Lemma 3.2

Proof of Lemma 3.2: **We first claim the followings:**
- There exist positive constants c0, c1 independent of the time t **such that**

$$\frac{d}{d t}D_{K L}(\rho_{t}^{\xi}||\pi)\leq-c_{0}{\mathcal{I}}(\rho_{t}^{\xi})+c_{1}d.$$
) + c1d. **(A.6)**
- There is a positive constant c2 independent of the time t (c2 **is dependent on** DKL(ρ0||π),
which is a dimension-free positive constant due to Assumption **3.2) such that**
DKL(ρ ξ t||π) ≤ c2d. **(A.7)**
Indeed, for the first claim (A.6), using Fokker-Planck equation (2.7) for ρ ξ t**, we can**
directly calculate the following:

$$\frac{d}{dt}D_{KL}(\rho_{t}^{\xi}||\pi)=\int\left(1+\log\frac{\rho_{t}^{\xi}}{\pi}\right)\partial_{t}\rho_{t}^{\xi}dx$$ $$=\int\left(\nabla\log\rho_{t}^{\xi}-\beta b\right)\cdot\left(\rho_{t}^{\xi}\hat{b}_{t}-\beta^{-1}\nabla\rho_{t}^{\xi}\right)dx,$$
 $\pi.\,$ By Young's inequality, w. 
where we recall b = −∇U = β∇ log π**. By Young's inequality, we have**

d dtDKL(ρ ξ t||π) ≤ Åβ −1 4 Z |∇ log ρ ξ t| 2ρ ξ t dx + β Z | ˆbt| 2ρ ξ t dxã− β −1Z|∇ log ρ ξ t| 2ρ ξ t dx + β 2 Z(|b| 2 + | ˆbt| 2)ρ ξ t dx + Åβ Z |b| 2ρ ξ t dx + β −1 4 Z |∇ log ρ ξ t| 2ρ ξ t dxã = − 1 2 β −1I(ρ ξ t) + 3β 2 E h| ˆbt(X¯t)| 2Fξ i+ E h|b(X¯t)| 2Fξ i . (A.8)
Using the Lipshitz assumption, the result for moment control Proposition **3.1, and Jensen's**
inequality, since ηk ≤ ∆0, we know that for t ∈ [Tk, Tk+1),

$$\mathbb{E}\left[|\tilde{b}_{t}(\bar{X}_{t})|^{2}\Big{|}\mathcal{F}_{\xi}\right]=\int\rho_{t}^{\xi}(x)\left(\mathbb{E}\left[b(\bar{X}_{T_{k}})|\bar{X}_{t}=x,\mathcal{F}_{\xi}\right]\right)^{2}dx$$ (A.9) $$\leq\mathbb{E}\left[|b(\bar{X}_{T_{k}})|^{2}\Big{|}\mathcal{F}_{\xi}\right]\leq\mathbb{E}\left[\left(|b(0)|+|\bar{X}_{T_{k}}|\right)^{2}\Big{|}\mathcal{F}_{\xi}\right]\leq\bar{c}_{1}d,$$

22 where c1 is a time-independent positive constant according to Proposition **3.1. Hence by**
(A.8) and (A.9), the first claim (A.6) holds with c0 = 12 β
−1 and c1 = 3βc˜1 For the second claim (A.7), we first observe that, we can control the negative Fisher information −I(¯ρ ξ t
) by the negative relative information −I(ρ ξ t|π) := −R|∇ log ρ ξ t π| 2ρ ξ t dx via Young's inequality, namely,

$$\mathcal{I}(\rho_{t}^{\xi}|\pi)=\int|\nabla\log\frac{\rho_{t}^{\xi}}{\pi}|^{2}\rho_{t}^{\xi}dx\leq2\mathcal{I}(\rho_{t}^{\xi})+2\beta^{2}\mathbb{E}\left[|b(\bar{X}_{t})|^{2}\left|\mathcal{F}_{\xi}\right.\right].$$  So we have  $$-\mathcal{I}(\rho_{t}^{\xi})\leq-\frac{1}{2}\mathcal{I}(\rho_{t}^{\xi}|\pi)+\beta^{2}\mathbb{E}\left[|b(\bar{X}_{t})|^{2}\left|\mathcal{F}_{\xi}\right.\right].$$  Then, combining (A.8), (A.9) and (A.11), we have 
i. **(A.10)**
$$(\mathrm{A.10})$$  $$(\mathrm{A.11})$$
i. **(A.11)**
$$\frac{d}{dt}D_{KL}(\rho_{t}^{\xi}||\pi)\leq-\frac{1}{4}\beta^{-1}\mathcal{I}(\rho_{t}^{\xi}|\pi)+2\beta\mathbb{E}\left[|b(\bar{X}_{t})|^{2}\Big{|}\mathcal{F}_{\xi}\right]+\frac{3\beta}{2}\mathbb{E}\left[|\hat{b}_{t}(\bar{X}_{t})|^{2}\Big{|}\mathcal{F}_{\xi}\right]$$ $$\leq-\frac{1}{4}\beta^{-1}\mathcal{I}(\rho_{t}^{\xi}|\pi)+c_{1}^{\prime}d,$$
$$(\mathrm{A.12})$$

where c
′ 1
is a positive constant. Since π **satisfies a Log-Sobolev inequality with constant**
C
LS
π**, we have**d
constant. Since $\pi$ satisfies a Log-Sobolev inequality  $$\frac{d}{dt}D_{KL}(\rho_{t}^{\xi}||\pi)\leq-\frac{1}{4\beta C_{\pi}^{LS}}D_{KL}(\rho_{t}^{\xi}||\pi)+c_{1}^{\prime}d.$$  ity, we have 
1d. **(A.13)**
By Gr¨onwall's inequality, we have

any, we have  $$\begin{split}D_{KL}(\rho_{t}^{\xi}||\pi)&\leq e^{-\rho t}D_{KL}(\rho_{0}||\pi)+c_{1}^{\prime}\rho^{-1}(1-e^{-\rho t})\\ &\leq D_{KL}(\rho_{0}||\pi)+c_{1}^{\prime}\rho^{-1}d:=c_{2}d,\end{split}$$ (A.14)  I am the same label in (A.7) label.  
where ρ := 1 4βCLS
π**. Hence the second claim (A.7) holds.**
Now, equipped with the two claims (A.6) and (A.7), using integration by parts, we know that for all differential, nonnegative, non-increasing f,

Z T
0
e
−A0(T −s)f(s)I(ρ
ξ
s)ds
≤ −c˜0
Z T
0
e
−A0(T −s)f(s)
Åd
dsDKL(ρ
ξ
s||π)
ãds + ˜c1d
Z T
0
e
−A0(T −s)f(s)ds
= ˜c1d
Z T
0
e
−A0(T −s)f(s)ds − c˜0f(T )DKL(ρ
ξ
T||π**) + ˜**c0e
−A0Tf(0)DKL(ρ0||π)
+ ˜c0
Z T
0
e
−A0(T −s)f
′(s)DKL(ρ
ξ
s||π)ds + ˜c0A0
Z T
0
e
−A0(T −s)f(s)DKL(ρ
ξ
s||π)ds
≤ c˜1d
Z T
0
e
−A0(T −s)f(s)ds **+ 0 + ˜**c0e
−A0Tf(0)DKL(ρ0||π**) + 0 + ˜**c0c2d
Z T
0
e
−A0(T −s)f(s)ds
:= M1DKL(ρ0||π)f(0)e
−A0T + M2d
Ç**1 + sup**
s≥0
DKL(ρ
ξ
s||π)
å Z T
0
e
−A0(T −s)f(s)ds.
Here, ˜c0, ˜c1, M1, M2 are positive constants independent of ξ**. The last inequality is because**
the KL-divergence is non-negative, and f **is nonnegative and non-increasing.**
Now, we have already obtained the desired estimation

$$\int_{0}^{T}e^{-A_{0}(T-s)}f(s)\mathcal{I}(\rho_{s}^{\mathbf{\xi}})ds$$ $$\leq M_{1}D_{KL}(\rho_{0}||\pi)f(0)e^{-A_{0}T}+M_{2}d\left(1+\sup_{s\geq0}D_{KL}(\rho_{s}^{\mathbf{\xi}}||\pi)\right)\int_{0}^{T}e^{-A_{0}(T-s)}f(s)ds$$ (A.15)
23 for all differential, non-increasing, nonnegative function f. Since piecewise-constant functions can be approximated by differential functions, we know that (A.15) holds for all nonincreasing, nonnegative, piecewise-constant function f**. This then ends the proof.**

## A.3 Basics On Path Measure

In this section, we review some basics of path measure. Consider the following two SDEs in
R
d **with different drifts but the same diffusion** σ:
$$dX^{(1)}=b^{(1)}(X^{(1)},x_{0})dt+\sigma\cdot dW,\quad X^{(1)}_{0}=X^{(2)}_{0}=x_{0}.$$ (A.16)
Here, W is a standard Brownian motion under the probability P **(the same for the two**
SDEs), and x0 ∼ µ0 **is a common, but random, initial position. We allow the drifts to be**
possibly dependent on the initial position x0 **for our application. For fixed time interval**
[0, T ], the two processes X(1) and X(2) **naturally induce two probability measures in the**
path space X := C([0, T ]; R
d**), denoted by** P
(1) and P
(2)**, respectively. To be more specific,**
for [s, t] ⊂ [0, T ], A ∈ B(R
d), P
(i)([s, t] × A) = P(X
(i)
τ ∈ A, τ ∈ [s, t]), i = 1, **2. It is also**
obvious that the two probability measures P
(1), P
(2) **are mutually absolutely continuous, so**
we are able to define the Radon-Nikodym derivative dP (1)
dP (2) ∈ L
1(P
(2), X).

To obtain the formula for dP (1)
dP (2) ∈ L
1(P
(2), X**), we recall that the Girsanov transform**
[19, 12, 10] asserts that under the probability measure Q **satisfying**

$$\frac{dQ}{d\overline{\theta}}(X^{(2)}(\omega))=\exp\Big{(}\int_{0}^{T}(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\cdot dW_{s}\\ -\frac{1}{2}\int_{0}^{T}\Big{|}(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\Big{|}^{2}\,ds\Big{)},$$  with the matrix $G$ is defined by  $$\cdot$$

G := σσT−1, the law of X(2) is the same as the law of X(1) under P**. In other words, for any Borel**
measurable set B ⊂ X,

EP[1B(X(1))] = EQ[1B(X(2)**)] =** EP
$$\L_{B}(X^{(2)})]=\mathbb{E}_{\mathbb{P}}\left[1_{B}(X^{(2)}){\frac{d\mathbb{Q}}{d\mathbb{P}}}\right].$$
Note that the expression of dQ
dP g(X) = exp  Z T 0 Äb (1) − b (2))(X, X0)ä· G −1· dX + 1 2 Z T 0 Äb (2)· G −1· b (2) − b (1)· G −1· b (1)ä(X, X0)ds, Since P (1) = (X(1))#P and P (2) = (X(2))#P are the laws of X(1) and X(2) respectively, then one has P (1)(B) = EX∼P (2) [1B(X)g(X)] It follows that the Radon-Nikodym derivative is
(ω) = g(X(2)(ω)) where (X0 := X**(0))**
Hence, since dX(2) = b
(2)(X(2), x0)dt + σ · dW**, we have derived that**
$${\frac{d P^{(1)}}{d P^{(2)}}}(X)=g(X).$$
Hence, since $\partial X^{\prime}=\partial^{\prime}\left(X^{\prime},x_{0}\right)\partial\nu+\partial^{\prime}\partial\nu$, we have derived that  $$\frac{dP^{(1)}}{dP^{(2)}}(X^{(2)}(\omega))=\frac{dQ}{dP}(\omega)=\exp\bigg{(}\int_{0}^{T}(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\cdot dW_{s}$$ $$-\frac{1}{2}\int_{0}^{T}\left|(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\right|^{2}ds\bigg{)},$$ (A.17)
$$24$$
which is a martingale under P **and its natural filtration defined by** F
(2)
t:= σ(X
(2)
s , s ≤ t),
t ∈ [0, T **]. Note that (A.17) will be used in our proof.**
Moreover, we can view the process X(i) as an identical mapping: X(i) = (X
(i)
t)0≤t≤T :
Ω → X. For fixed t ∈ [0, T ], X
(i)
t**can be viewed as a measurable mapping from Ω to** R
d and one in fact has X
(i)
t = ωt ◦ X(i) ∈ R
d, where ωt : X → R
d**is the time marginal defined by**
ωt(γ) = γt**. Then the law of the solution** X
(i)
tat time t**, namely, the time marginal of** P
(i),
is the push forward measures P
(i)
t**:= (**X
(i)
t)\#P = (ωt)\#P
(i), ∀t ∈ [0, T **]. This means** P
(i)
tis a probability measure in R
d**, satisfying**

P (i) t(A) = P(X (i) t ∈ A), ∀A ∈ B(R (1) (2)
$$(\mathrm{A.18})$$
d), i = 1, 2. **(A.18)**
Clearly, at any time t, P
tand P
t**are mutually absolutely continuous, the Radon-Nikodym**
derivative dP (1)
t dP (2)
t∈ L
1(P
(2)
t, R
d**) is well defined.**
The following Lemma describes the relationship between the two Radon-Nikodym derivatives (of path measures and of push forward measures):
Lemma A.1. Let Q1, Q2 be two probability distributions on X, and Q2 is absolutely continuous with respect to Q1. Let φ : X → R
d**be a measurable mapping, and consider the**
push forward measure φ\#Q1 and φ\#Q2, denoted by Q1,φ and Q2,φ**, respectively. Then the**
Randon-Nikodym derivatives dQ1,φ dQ2,φ∈ L
1(dQ2,φ, R
d),
dQ1 dQ2∈ L
1(dQ2, X) **are well-defined,**
anddQ1,φ

$$\frac{dQ_{1,\phi}}{dQ_{2,\phi}}(x)=\mathbb{E}_{X\sim Q_{2}}\left[\frac{dQ_{1}}{dQ_{2}}|\phi(X)=x\right],\quad Q_{2}-a.e.$$ (A.19)
Proof of Lemma A.1: **Using the definition of Radon-Nikodym derivative, it suffices to check**
that for any A ∈ B(R
d),

$$\mathbb{E}_{x\sim Q_{1,\phi}}\left[\mathbf{1}_{A}(x)\right]=\mathbb{E}_{x\sim Q_{2,\phi}}\left[\mathbf{1}_{A}(x)\mathbb{E}_{X\sim Q_{2}}\left[\frac{dQ_{1}}{dQ_{2}}(X)|\phi(X)=x\right]\right].$$ (A.20)
Indeed, using the definition of push forward measure and Randon-Nikodym derivative, as well as the conditional expectation, we have

$$LHS=\mathbb{E}_{X\sim Q_{1}}\left[\mathbf{1}_{A}(\phi(X))\right]$$ $$=\mathbb{E}_{X\sim Q_{2}}\left[\frac{dQ_{1}}{dQ_{2}}(X)\mathbf{1}_{A}(\phi(X))\right]$$ $$=\mathbb{E}_{X\sim Q_{2}}\left[\mathbf{1}_{A}(\phi(X))\mathbb{E}_{X\sim Q_{2}}\left[\frac{dQ_{1}}{dQ_{2}}(X)|\phi(X)\right]\right]$$ $$=RHS.$$

This is what we want.

Clearly, if we take φ = ωt for t ∈ [0, T **], the time projection mapping, then we conclude**
the following result for Radon-Nikodym of time marginals.

Corollary A.1. For t ∈ [0, T ]**, recall the definition of** P
(i)
t and P
(i), i = 1, 2 **above. Then**
the following holds:

$$\frac{dP_{t}^{(1)}}{dP_{t}^{(2)}}(x)=\mathbb{E}_{X\sim P^{(2)}}\left[\frac{dP^{(1)}}{dP^{(2)}}(X)|X_{t}=x\right],\quad\mathbb{P}-a.e.$$ (A.21)
Also note that Corollary A.1 **here is very useful. For instance, if we combine the result**
(A.21) in Corollary A.1 **with the Girsanov transform in (A.17), we can express the quotient** of densities of two processes ρ
(1)/ρ(2) by one process X(2) **alone. Meanwhile, the information**
coming from the process X(1) **is stored in the drift term** b
(1)(·**), which is usually a deterministic function. Then we only need to look into one of these two processes instead of both of**
them, and this can often simplify the analysis.

## A.4 Estimate Of The Remaining Terms

We estimate the remaining terms

$$\mathbb{E}_{\xi_{k}}\mathbb{E}\left[|{\bar{b}}_{t}^{\xi_{k}}({\bar{X}}_{t})-b^{\xi_{k}}({\bar{X}}_{t})|^{2}\Big|\xi_{k}\right]$$

, and

$$\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\bar{\hat{\rho}}_{t}^{\xi_{k}}-\bar{\hat{\rho}}_{t}^{\xi_{k}}|^{2}}{\bar{\hat{\rho}}_{t}^{\tilde{\xi}_{k}}}d x\right]$$

in Section **4. Note that in the followings we consider the behaviour of SGLD in a time**
subinterval [Tk, Tk+1**), and recall that ¯**ρ ξk , ¯ρ ξ˜k **are defined in (4.1).**
Lemma A.2. Recall the definition of r¯t(x) in (4.14)**. Then under the setting of Proposition**
3.2, there exists a positive constant c independent of the choice of the batch ξk **such that for**
all t ∈ [Tk, Tk+1)**, it holds that**

$$\mathbb{E}\left[|{\bar{r}}_{t}({\bar{X}}_{t})|^{2}\Big|\xi_{k}\right]\leq c d(t-T_{k})^{2}.$$
2. **(A.22)**
Proof of Lemma A.2: **Since** ∇b ξis L2**-Lipshitz, we know that**

$$|\bar{r}_{t}(x)|\leq L_{2}\mathbb{E}\left[|\bar{X}_{T_{k}}-\bar{X}_{t}|^{2}|\bar{X}_{t}=x,\xi_{k}\right].$$
2|X¯t = x, ξk. **(A.23)**
Hence by Jensen's inequality, and using the Lipshitz assumption for b ξk in Assumption **3.1,**
we haveddd

E h|r¯t(X¯t)| 2ξk i≤ L 2 2d −1E hE-|X¯Tk − X¯t| 2|X¯t = x 2ξk i ≤ L 2 2d −1E hE-|X¯Tk − X¯t| 4|X¯t = xξk i = L 2 2d −1E ñ |b ξk(X¯Tk )(t − Tk) + Z t Tk dW| 4ξk ô ≤ L 2 2d −1Å(t − Tk) 4|b ξk(0)| + LE h|X¯Tk| ξk i4+ 3(t − Tk) 2d 2ã,
where we use the inequality (a + b)
p ≤ 2 p−1(a p + b p**) in the last inequality.**
Finally, by Proposition **3.1, we have a uniform bound for the moment** E
h|X¯Tk| 4Fξ i, which leads to the conclusion (A.22).

Lemma A.3. Under the setting of Proposition 3.2, there exists a positive constant c independent of k and ξk such that for t ∈ [Tk, Tk+1),

$$\int\left|\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]\right|^{2}\bar{\rho}_{t}^{\xi_{k}}(x)d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right),$$

where I(ρ) := Rρ|∇ log ρ| 2dx **is the Fisher information.**
Proof of Lemma A.3: **By Bayes' law, we have**

$$\begin{split}\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}&=x,\xi_{k}]=\int(y-x)P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})dy\\ &=\int(y-x)\frac{\bar{\rho}_{T_{k}}(y)P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})}{\bar{\rho}_{t}^{\xi_{k}}(x)}dy.\end{split}$$ (A.24)
Since P(X¯t = x|X¯Tk = y, ξk**) is Gaussian, and since its derivative is also similar to the** Gaussian form, we split the term E[X¯Tk −X¯t|X¯t = x, ξk**] into three parts and use integration**
by parts to handle them.

Let
$$y-x=\left(I_{d}+(t-T_{k})\nabla b^{\xi_{k}}(y)\right)\cdot\left(y-x+(t-T_{k})b^{\xi_{k}}(y)\right)$$ $$\qquad-(t-T_{k})\nabla b^{\xi_{k}}(y)\cdot\left(y-x+(t-T_{k})b^{\xi_{k}}(y)\right)$$ $$\qquad-(t-T_{k})\cdot b^{\xi_{k}}(y)$$ $$\qquad:=a_{1}(x,y)-a_{2}(x,y)-a_{3}(x,y),$$
and define
$$I_{i}(x):=\mathbb{E}\left[a_{i}(\bar{X}_{t},\bar{X}_{T_{k}})|\bar{X}_{t}=x\right],\quad i=1,2,3.$$
Next, we will obtain an η 2 k estimate for E
h|Ii(X¯t)| 2ξk i, i = 1, 2, **3. We first claim that,**
there exist positive constants c, c
′, c
′′ independent of k and ξ such that for t ∈ [Tk, Tk+1),

$$\mathbb{E}\left[|I_{1}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c(t-T_{k})^{2}\mathcal{I}(\bar{\rho}_{T_{k}}),$$  $$\mathbb{E}\left[|I_{2}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c^{\prime}d(t-T_{k})^{3},$$  $$\mathbb{E}\left[|I_{3}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c^{\prime\prime}d(t-T_{k})^{2},$$
), **(A.26)**
3, **(A.27)**
2, **(A.28)**
where I(ρ) := Rρ|∇ log ρ| 2dx **is the Fisher information.**
By the claims (A.26), (A.27), (A.28) , we can easily obtain the following Oη 2 k
(d + I(¯ρTk
)
bound:

Z
$$\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]|^{2}\bar{\rho}_{t}^{\xi_{k}}(x)dx\leq3\sum_{k=1}^{3}\mathbb{E}\left[|I_{i}(\bar{X}_{t})|^{2}\Big{|}\xi_{k}\right]\leq\bar{c}\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right),$$
$$(\mathrm{A.25})$$
i=1
where the positive constant ˜c is independent of the batch ξk**, and this is what we desire.**
For the the claims (A.26), (A.27), (A.28), we prove them separately in the followings:
(a) For the term I1, since the distribution P(X¯t = x|X¯Tk = y, ξk**) is Gaussian, namely,**
$$P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})=\left(4\pi\beta^{-1}(t-T_{k})\right)^{-\frac{d}{d}}\exp\left(-\frac{|x-y-b^{\xi_{k}}(y)(t-T_{k})|^{2}}{4\beta^{-1}(t-T_{k})}\right).$$ (A.29)
Then, after integration by parts we obtain:

$$I_{1}(x)=2\beta^{-1}(t-T_{k})\int\frac{\nabla_{y}\bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{t}^{\xi_{k}}(x)}P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})d y.$$
P(X¯t = x|X¯Tk = y, ξk)dy. **(A.30)**
Using Bayes' law again, we have

 In figure, we have  $ I_1(x)=2\beta^{-1}(t-T_k)\int\frac{\nabla_y\bar{\rho}_{T_k}(y)}{\bar{\rho}_{T_k}(y)}P(\bar{X}_{T_k}=y|\bar{X}_t=x,\xi_k)dy$. 
(y)P(X¯Tk = y|X¯t = x, ξk)dy. **(A.31)**
Hence, by Jensen's inequality,

$$\mathbb{E}\left[\left|I_{1}(\bar{X}_{t})\right|^{2}\left|\xi_{t}\right|\right]\leq4\beta^{-2}(t-T_{k})^{2}\int\bar{\rho}_{t}^{\xi_{t}}(x)\int\left|\frac{\nabla_{y}\bar{\rho}\tau_{1}(y)}{\bar{\rho}\tau_{1_{k}}(y)}\right|^{2}P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})dydx$$ $$=4\beta^{-2}(t-T_{k})^{2}\mathcal{I}(\bar{\rho}\tau_{k}):=c(t-T_{k})^{2}\mathcal{I}(\bar{\rho}\tau_{k}).$$ (A.2)
(A.32)
(b) For the term I2, using the Lipshitz condition in Assumption 3.1 **and Jensen's inequality, we have**

E h|I2(X¯t)| 2ξk i≤ c˜ ′(t − Tk) 2E ïE hX¯t − X¯Tk − (t − Tk)b ξk(X¯t) X¯Tk i 2ξk ò ≤ c˜ ′(t − Tk) 2E ïX¯t − X¯Tk − (t − Tk)b ξk(X¯t)  2ξk ò (A.33) ≤ c˜ ′(t − Tk) 2E " Z t Tk p2β−1dWs  2 ξk # = c ′d(t − Tk) 3.
27 The constant c
′ here is independent of ξk **since the Lipshitz constant is uniform.**
(c) For the term I3**, still using Jensen's inequality and Lipshitz assumption for** b ξk **, it is**

clear that
$$\mathbb{E}\left[\left|I_{3}(\bar{X}_{t})\right|^{2}\right|\xi_{k}\right]\leq(t-T_{k})^{2}\mathbb{E}\left[\left|b^{\xi_{k}}(\bar{X}_{T_{k}})\right|^{2}\right|\xi_{k}\right]$$ $$\leq2(t-T_{k})^{2}\left(|b^{\xi_{k}}(0)|^{2}+L_{2}\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{2}\right|\xi_{k}\right]\right)\,.$$
$$(\mathrm{A.34})$$
By Proposition 3.1, for any fixed batch ξk**, the moment** E
h|X¯Tk| 2ξk i**has a uniform-in-batch**

O**(1) upper bound. Therefore, we are able to obtain the following batch-independent bound**
for the term ¯I3:
$$\mathbb{E}\left[|I_{3}({\bar{X}}_{t})|^{2}\Big|\xi_{k}\right]\leq c^{\prime\prime}d(t-T_{k})^{2}.$$
2. **(A.35)**
Concluding the results we obtained in parts (a), (b), (c) yields the claims (A.26), (A.27),
(A.28).

In the following lemmas, we prove some details for estimate of Eξk,ξ˜k

of $\mathbb{E}_{\xi_k,\tilde{\xi}_k}\left[\int|b^{\xi_k}-b|^2\frac{|\vec{\hat{P}_t}^{\xi_k}-\vec{\hat{P}_t}^{\xi_k}|^2}{\vec{\hat{P}_t}^{\xi_k}}dx\right]$. 
Lemma A.4. **Recall the notations**

$$K_{1}:=\sqrt{\frac{\beta}{2}}\,\bar{b}(y)(x-y),\quad\bar{b}(y):=(b^{\xi_{k}}-b^{\bar{\xi}_{k}})(y).$$
ξ˜k)(y). **(A.36)**
Then under the conditions of Proposition 3.2, there exists a positive constant c **independent**
of k and ξk,
˜ξk such that for t ∈ [Tk, Tk+1),

$$\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{1}P(\bar{X}_{\bar{T}_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{\bar{T}_{k}})\right).$$
)). **(A.37)**
Proof of Lemma A.4: **The technique here is similar to the one we use in the proof of Lemma**
A.3. To begin with, we split the term K1 **into the following three parts:**

$$\bar{b}(y)\cdot(y-x)=\bar{b}(y)\cdot\left(I_{d}+(t-T_{k})\nabla b^{\bar{\xi}_{k}}(y)\right)\cdot\left(y-x+(t-T_{k})b^{\bar{\xi}_{k}}(y)\right)$$ $$\qquad-(t-T_{k})\bar{b}(y)\cdot\nabla b^{\bar{\xi}_{k}}(y)\cdot\left(y-x+(t-T_{k})b^{\bar{\xi}_{k}}(y)\right)$$ $$\qquad-(t-T_{k})\bar{b}(y)\cdot b^{\bar{\xi}_{k}}(y)$$ $$\qquad:=\bar{a}_{1}(x,y)-\bar{a}_{2}(x,y)-\bar{a}_{3}(x,y),$$

Then,

and define
$$\bar{I}_{i}(x):=\mathbb{E}\left[\bar{a}_{i}(\bar{X}_{T_{k}},\bar{Y}_{t})\Big|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k}\right],\quad i=1,2,3.$$
can,  $$\int\widehat{p}_{t}^{\widehat{\xi}_{k}}(x)\left(\int K_{1}P(\widehat{X}_{T_{k}}=y|\widehat{Y}_{t}=x)dy\right)^{2}dx=\frac{\beta}{2}\mathbb{E}\left[|\widehat{I}_{1}(\widehat{Y}_{t})-\widehat{I}_{2}(\widehat{Y}_{t})-\widehat{I}_{3}(\widehat{Y}_{t})|^{2}\right]\xi_{k},\,\widehat{\xi}_{k}\right]$$ (A.38)  (a) For the first term $\bar{I}_{1}$, using Bayes' formula and integration by parts, since $P(\bar{Y}_{t}=\widehat{I}_{1})$, we have 
$$(\mathrm{A.37})$$
x|X¯Tk = **y, ξ**k,
˜ξk**) is Gaussian, we have**
¯I1(x) = 2β −1Z˜b(y) ·ÄId + (t − Tk)∇b ξ˜k(y)ä· β 2 Äy − x + (t − Tk)b ξ˜k(y)ä ρ¯Tk (y) ρ¯ ξ˜k t(x) P(Y¯t = x|X¯Tk = y)dy = 2β −1(t − Tk) Z∇y( ˜b(y)¯ρTk (y)) ρ¯ ξ˜k t (x) P(Y¯t = x|X¯Tk = y, ξk, ˜ξk)dy = 2β −1(t − Tk) Z Å ∇˜b(y) + ˜b(y) ∇ρ¯Tk (y) ρ¯Tk (y) ãP(X¯Tk = y|Y¯t = x, ξk, ˜ξk)dy.
Since ∇˜b and ˜b **= [(**b ξk − b) − (b ξ˜k − b)]/p2β−1 are uniformly bounded by Assumption **3.1,**
we obtain E
h|
¯I1(Y¯t)| 2ξk,
˜ξk i≤ cη2 k
(1 + I(¯ρTk
)), **(A.39)**
and the constant c is independent of ξk and ˜ξk.

(b) For the second term ¯I2**, by Jensen's inequality, it holds that**

$$\mathbb{E}\left[|\bar{I}_{2}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\bar{\xi}_{k}\right]\leq(t-T_{k})^{2}\mathbb{E}\left[\left|\bar{b}(\bar{X}_{T_{k}})\cdot\nabla b^{\bar{\xi}_{k}}(\bar{X}_{T_{k}})\cdot\int_{T_{k}}^{t}d W\right|^{2}\Big|\xi_{k},\bar{\xi}_{k}\right].$$
. **(A.40)**
By Assumption 3.1, both ˜b **= [(**b ξk −b)−(b ξ˜k −b)]/p2β−1 and ∇b ξ˜k **are uniformly bounded,**

so we can directly get
$$\mathbb{E}\left[|{\bar{I}}_{2}({\bar{Y}}_{t})|^{2}\Big|\xi_{k},{\tilde{\xi}}_{k}\right]\leq c d(t-T_{k})^{3},$$
3, **(A.41)**
and the constant c is independent of ξk and ˜ξk.

(c) For the third term ¯I3**, by Jensen's inequality,**

$$\mathbb{E}\left[\left|\bar{I}_{3}(\bar{Y}_{t})\right|^{2}\left|\xi_{k},\bar{\xi}_{k}\right|\right.\leq(t-T_{k})^{2}\mathbb{E}\left[\left|\bar{b}(\bar{X}_{T_{k}})\cdot b^{\bar{\xi}_{k}}(\bar{X}_{T_{k}})\right|^{2}\left|\xi_{k},\bar{\xi}_{k}\right|\right].$$
ò. **(A.42)**
Since ˜b **is bounded, and since** b ξ˜k is Lipshitz by Assumption **3.1, we have**

$$\mathbb{E}\left[|\bar{I}_{3}(\bar{Y}_{t})|^{2}\Big{|}\xi_{k},\bar{\xi}_{k}\right]\leq c(t-T_{k})^{2}\mathbb{E}\left[|b^{\bar{\xi}_{k}}(\bar{X}_{T_{k}})|^{2}\Big{|}\xi_{k},\bar{\xi}_{k}\right]$$ $$\leq2c(t-T_{k})^{2}\left(|b^{\bar{\xi}_{k}}(0)|^{2}+L^{2}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{2}\Big{|}\xi_{k},\bar{\xi}_{k}\right]\right).$$
$$(\mathrm{A.40})$$
(A.43)
Due to (3.4), |b ξ˜k (0)| ≤ |b(0)| + |b ξ˜k (0) − b(0)| **is uniformly bounded almost surely. By**
Proposition 3.1, there is a uniform-in-batch O**(1) bound for the moment** E|X¯Tk| 2**. Hence we**

obtain
$$\mathbb{E}\left[|\bar{I}_{3}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c d(t-T_{k})^{2},$$
2, **(A.44)**
and the constant c is independent of ξk and ˜ξk.

Finally, combining (a), (b) and (c), we get the desired result.

Lemma A.5. **Recall the notations**

$$K_{2}:=\left(-\sqrt{\frac{\beta}{2}}\,\tilde{b}(y)\cdot b^{\tilde{b}_{k}}(y)-\frac{1}{2}|\tilde{b}(y)|^{2}\right)(t-T_{k}),\quad\tilde{b}(y):=\frac{1}{\sqrt{2\beta^{-1}}}\left(b^{\tilde{b}_{k}}-b^{\tilde{b}_{k}}\right)(y).$$ (A.45)
Then under the conditions of Proposition 3.2, there exists a positive constant c **independent**
of k and ξk such that for t ∈ [Tk, Tk+1),

$$\int\rho_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.$$
k. **(A.46)**
The bound is independent of the choice of the batches ˜ξk , ξk.

Proof of A.5: **By Jensen's inequality, we have**

$$\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)dy\right)^{2}dx$$ $$\leq\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int|K_{2}|^{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)dy\right)dx$$ (A.47) $$=(t-T_{k})^{2}\mathbb{E}\left[\left|\sqrt{\frac{\beta}{2}}\,\bar{b}(\bar{X}_{T_{k}})\cdot\bar{b}^{\bar{\xi}_{k}}(\bar{X}_{T_{k}})+\frac{1}{2}|\bar{b}(\bar{X}_{T_{k}})|^{2}\right|^{2}\left|\xi_{k},\bar{\xi}_{k}\right.\right]$$

29 Since b ξ˜k is Lipshitz by Assumption **3.1, we have**

$$\mathbb{E}\left[\left|\sqrt{\frac{\beta}{2}}\,\bar{b}(\bar{X}_{T_{k}})\cdot b^{\xi_{k}}(\bar{X}_{T_{k}})+\frac{1}{2}|\bar{b}(\bar{X}_{T_{k}})|^{2}\right|^{2}\left|\xi_{k},\bar{\xi}_{k}\right|\right]\leq\bar{c}_{1}+\bar{c}_{2}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{2}\big{|}\xi_{k},\bar{\xi}_{k}\right].$$

Here, the positive constants ˜c1, ˜c2 **are independent of the batch since the coefficients in**
conditions (a), (d) of Assumption 3.1 are uniform-in-batch. By Proposition **3.1,** E-|X¯Tk| 2 has a uniform-in-batch O**(1) upper bound. Combining this fact with (A.47), one then has**

$$\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.$$
k. **(A.48)**
Here, c is a positive constant independent of k, d, ξk and ˜ξk.

Lemma A.6. **Recall the notations**

$$(\mathrm{A.48})$$
$$(\mathrm{A.52})$$

K3 := e z − 1 − z, **(A.49)**
with

$$z:=\sqrt{\frac{\beta}{2}}\,\bar{b}(y)(x-y-(t-T_{k})b^{\hat{k}_{k}}(y))-\frac{1}{2}|\bar{b}(y)|^{2}(t-T_{k}),$$
2(t − Tk), **(A.50)**
and
$$\tilde{b}(y):=\frac{1}{\sqrt{2\beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y).$$
ξkä(y). **(A.51)**
Then under the conditions of Proposition 3.2, there exists a positive constant c **independent**
of k and ξk such that for t ∈ [Tk, Tk+1),

$$\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{3}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.$$
k. **(A.52)**
Proof of Lemma A.6: **By Jensen's inequality, it holds that**

$$\begin{array}{l}{{\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\left(\int K_{3}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\bar{\xi}_{k})d y\right)^{2}d x}}\\ {{\leq\int\bar{\rho}_{t}^{\bar{\xi}_{k}}(x)\int|K_{3}|^{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)d y d x=\mathbb{E}\left[\left|e^{\hat{Y}_{t}}-1-\hat{Y}_{t}\right|^{2}\left|\xi_{k},\bar{\xi}_{k}\right|\right],}}\end{array}$$
$$(\mathrm{A.53})$$

where we denote the process

$$\hat{Y}_{t}:=\sqrt{\frac{\beta}{2}}\tilde{b}(\bar{X}_{T_{k}})\cdot\left(\bar{Y}_{t}-\bar{X}_{T_{k}}-(t-T_{k})b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})\right)-\frac{1}{2}|\tilde{b}(\bar{X}_{T_{k}})|^{2}\Delta t$$ $$=-\frac{1}{2}|\tilde{b}(\bar{X}_{T_{k}})|^{2}\Delta t+\tilde{b}(\bar{X}_{T_{k}})\cdot\int_{T_{k}}^{t}dW.$$
$$(\mathrm{A.54})$$

with
∆t := t − Tk, ∀t ∈ [Tk, Tk+1). **(A.55)**
Denote Z¯t := e Yˆt − 1 − Yˆt**. In the following, we aim to obtain an** O(η 2 k
) bound for the term E
h|Z¯t| 2ξk,
˜ξk imainly via Itˆo's formula. In fact, for t ∈ [Tk, Tk+1)

$$\bar{Z}_{t}=\frac{1}{2}|\bar{b}|^{2}\Delta t+\bar{b}\cdot\int_{T_{k}}^{t}\left(e^{\bar{Y}_{s}}-1\right)d W_{s}=\frac{1}{2}|\bar{b}|^{2}\Delta t+\bar{b}\cdot\int_{T_{k}}^{t}\left(\bar{Z}_{s}+\hat{Y}_{s}\right)d W_{s}.$$
ädWs. **(A.56)**
So

$$\mathbb{E}\left[|Z_{t}|^{2}\Big|\xi_{k},\bar{\xi}_{k}\right]=\frac{1}{4}\mathbb{E}\left[|\bar{b}|^{4}\Big|\xi_{k},\bar{\xi}_{k}\right](\Delta t)^{2}+\int_{T_{k}}^{t}\mathbb{E}\left[|\bar{b}|^{2}\left(\tilde{Z}_{s}+\hat{Y}_{s}\right)^{2}\Big|\xi_{k},\bar{\xi}_{k}\right]d s.$$
ids. **(A.57)**
$$(\mathrm{A.56})$$
$$(\mathrm{A.57})$$

30 By Assumption **3.1,**
˜b **is uniformly bounded. Then,** E[|Yˆt| 2|ξk,
˜ξk] ≤ cd∆t**. Then, one has**

$$\mathbb{E}\left[|\tilde{Z}_{t}|^{2}\Big{|}\xi_{k},\tilde{\xi}_{k}\right]\leq c\int_{T_{k}}^{t}\mathbb{E}\left[|\tilde{Z}_{s}|^{2}\Big{|}\xi_{k},\tilde{\xi}_{k}\right]\,ds+cd(\Delta t)^{2}.$$

By Gr¨onwall's inequality, when ηk **is small, one thus has**

$$\mathbb{E}\left[|\bar{Z}_{t}|^{2}\Big|\xi_{k},\bar{\xi}_{k}\right]\leq c d(\Delta t)^{2}\leq c d\eta_{k}^{2}.$$
$\left(\text{A}.58\right)$. 
. **(A.58)**
Above, c is a generative positive constant independent of k and ξk**, with the concrete meaning**
varying from line to line. This then ends the proof.

## References

[1] Geometric ergodicity of SGLD via reflection coupling. 2022.

[2] Gabriele Abbati, Alessandra Tosi, Michael Osborne, and Seth Flaxman. Adageo: Adaptive geometric learning for optimization and sampling. In **International conference on**
artificial intelligence and statistics**, pages 226–234. PMLR, 2018.**
[3] Aur´elien Alfonsi, Benjamin Jourdain, and Arturo Kohatsu-Higa. **Optimal transport**
bounds between the time-marginals of a multidimensional diffusion and **its Euler** scheme. Electronic Journal of Probability**, 20:1–31, 2015.**
[4] Dominique Bakry and Michel Emery. Diffusions hypercontractives. In ´ **Seminaire de**
probabilit´es XIX 1983/84**, pages 177–206. Springer, 1985.**
[5] Dominique Bakry, Ivan Gentil, Michel Ledoux, et al. **Analysis and geometry of Markov**
diffusion operators**, volume 103. Springer, 2014.**
[6] Fran¸cois Bolley and C´edric Villani. Weighted Csisz´ar-Kullback-Pinsker inequalities and applications to transportation inequalities. In **Annales de la Facult´e des sciences** de Toulouse: Math´ematiques**, volume 14, pages 331–352, 2005.**
[7] Nicolas Brosse, Alain Durmus, and Eric Moulines. The promises and pitfalls of stochastic gradient Langevin dynamics. **Advances in Neural Information Processing Systems**,
31, 2018.

[8] Arnak S Dalalyan. Theoretical guarantees for approximate sampling from smooth and log-concave densities. **Journal of the Royal Statistical Society: Series B (Statistical**
Methodology)**, 79(3):651–676, 2017.**
[9] Arnak S Dalalyan and Avetik Karagulyan. User-friendly guarantees for the Langevin Monte Carlo with inaccurate gradient. **Stochastic Processes and their Applications**, 129(12):5278–5311, 2019.

[10] Arnak S Dalalyan and Alexandre B Tsybakov. Sparse regression **learning by aggregation**
and Langevin Monte-Carlo. Journal of Computer and System Sciences**, 78(5):1423–** 1443, 2012.

[11] Christian Daniel, Jonathan Taylor, and Sebastian Nowozin. Learning step size controllers for robust neural network training. In **Thirtieth AAAI Conference on Artificial**
Intelligence**, 2016.**
[12] Richard Durrett. Stochastic calculus: a practical introduction**. CRC press, 2018.**
[13] Rick Durrett. Probability: theory and examples**, volume 49. Cambridge university press,**
2019.

[14] Andreas Eberle. Reflection coupling and Wasserstein contractivity without convexity.

Comptes Rendus Mathematique**, 349(19-20):1101–1104, 2011.**
[15] Lawrence C Evans. Partial differential equations**, volume 19. American mathematical**
society, 2022.

[16] Tyler Farghly and Patrick Rebeschini. Time-independent generalization bounds for SGLD in non-convex settings. **Advances in Neural Information Processing Systems**,
34:19836–19846, 2021.

[17] Yuanyuan Feng, Tingran Gao, Lei Li, Jian-Guo Liu, and Yulong Lu. Uniform-in-time weak error analysis for stochastic gradient descent algorithms via diffusion approximation. arXiv preprint arXiv:1902.00635**, 2019.**
[18] Nicolas Fournier, Maxime Hauray, and St´ephane Mischler. Propagation of chaos for the 2d viscous vortex model. Journal of the European Mathematical Society**, 16(7):1423–** 1466, 2014.

[19] Igor Vladimirovich Girsanov. On transforming a certain class of stochastic processes by absolutely continuous substitution of measures. Theory of Probability & Its Applications**, 5(3):285–301, 1960.**
[22] Shi Jin, Lei Li, and Jian-Guo Liu. Random batch methods (RBM) for interacting particle systems. Journal of Computational Physics**, 400:108877, 2020.**
[24] Shi Jin, Lei Li, Xuda Ye, and Zhennan Zhou. Ergodicity and long-time behavior of the random batch method for interacting particle systems. **arXiv preprint**
arXiv:2202.04952**, 2022.**
[30] Lei Li and Jian-Guo Liu. Large time behaviors of upwind schemes **and B-schemes**
for Fokker-Planck equations on R by jump processes. **Mathematics of Computation**, 89(325):2283–2320, 2020.

[31] Lei Li, Lin Liu, and Yuzhou Peng. A splitting Hamiltonian Monte Carlo **method for**
efficient sampling. arXiv preprint arXiv:2105.14406**, 2021.**
[21] Wenqing Hu, Chris Junchi Li, Lei Li, and Jian-Guo Liu. On the diffusion approximation of nonconvex stochastic gradient descent. **Annals of Mathematical Sciences and**
Applications**, 4(1), 2019.**
[23] Shi Jin, Lei Li, Zhenli Xu, and Yue Zhao. A random batch Ewald method for particle systems with Coulomb interactions. **SIAM Journal on Scientific Computing**,
43(4):B937–B960, 2021.

[25] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization.

arXiv preprint arXiv:1412.6980**, 2014.**
[26] Bobby Kleinberg, Yuanzhi Li, and Yang Yuan. An alternative view: When does SGD
escape local minima? In International Conference on Machine Learning**, pages 2698–**
2707. PMLR, 2018.

[27] Rep Kubo. The fluctuation-dissipation theorem. **Reports on progress in physics**,
29(1):255, 1966.

[28] Solomon Kullback and Richard A Leibler. On information and sufficiency. **The annals**
of mathematical statistics**, 22(1):79–86, 1951.**
[29] Michel Ledoux. Concentration of measure and logarithmic Sobolev inequalities. In Seminaire de probabilites XXXIII**, pages 120–216. Springer, 1999.**
[20] Leonard Gross. Logarithmic Sobolev inequalities. **American Journal of Mathematics**,
97(4):1061–1083, 1975.

[32] Lei Li and Yuliang Wang. On uniform-in-time diffusion approximation for stochastic gradient descent. arXiv preprint arXiv:2207.04922**, 2022.**
[33] Wenzhe Li, Sungjin Ahn, and Max Welling. Scalable MCMC for mixed membership stochastic blockmodels. In Artificial Intelligence and Statistics**, pages 723–731. PMLR,** 2016.
[34] Peter A Markowich and C´edric Villani. On the trend to equilibrium for the FokkerPlanck equation: an interplay between physics and functional analysis. **Mat. Contemp**,
19:1–29, 2000.

[35] Wenlong Mou, Nicolas Flammarion, Martin J Wainwright, and Peter L **Bartlett. Improved bounds for discretization of Langevin diffusions: Near-optimal rates without**
convexity. arXiv preprint arXiv:1907.11331**, 2019.**
[36] Wenlong Mou, Liwei Wang, Xiyu Zhai, and Kai Zheng. Generalization bounds of SGLD for non-convex learning: Two theoretical viewpoints. In **Conference on Learning**
Theory**, pages 605–638. PMLR, 2018.**
[37] Arvind Neelakantan, Luke Vilnis, Quoc V Le, Ilya Sutskever, Lukasz Kaiser, Karol Kurach, and James Martens. Adding gradient noise improves learning for very deep networks. arXiv preprint arXiv:1511.06807**, 2015.**
[38] David Nualart. The Malliavin calculus and related topics**, volume 1995. Springer, 2006.** [39] Felix Otto and C´edric Villani. Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality. Journal of Functional Analysis**, 173(2):361–** 400, 2000.

[40] Sam Patterson and Yee Whye Teh. Stochastic gradient Riemannian Langevin dynamics on the probability simplex. Advances in neural information processing systems**, 26, 2013.**
[41] Grigorios A Pavliotis. **Stochastic processes and applications: diffusion processes, the**
Fokker-Planck and Langevin equations**, volume 60. Springer, 2014.**
[42] MS Pinsker. Information and information stability of random quantities and processes.

Holden-Day**, 1964.**

[43] Maxim Raginsky, Alexander Rakhlin, and Matus Telgarsky. Non-convex learning via stochastic gradient Langevin dynamics: a nonasymptotic analysis. In **Conference on**
Learning Theory**, pages 1674–1703. PMLR, 2017.**
[44] Herbert Robbins and Sutton Monro. A stochastic approximation method. **The annals**
of mathematical statistics**, pages 400–407, 1951.**
[45] Filippo Santambrogio. Optimal transport for applied mathematicians. **Birk¨auser, NY**,
55(58-63):94, 2015.

[46] Samuel Smith, Erich Elsen, and Soham De. On the generalization benefit of noise in stochastic gradient descent. In International Conference on Machine Learning**, pages** 9058–9067. PMLR, 2020.

[47] Samuel L Smith, Benoit Dherin, David GT Barrett, and Soham De. **On the origin of**
implicit regularization in stochastic gradient descent. **arXiv preprint arXiv:2101.12176**, 2021.

[48] Michel Talagrand. A new isoperimetric inequality and the concentration of measure phenomenon. In Geometric aspects of functional analysis**, pages 94–124. Springer, 1991.**
[49] Max Welling and Yee W Teh. Bayesian learning via stochastic gradient Langevin dynamics. In **Proceedings of the 28th international conference on machine learning** (ICML-11)**, pages 681–688. Citeseer, 2011.**
[50] Lei Wu, Chao Ma, et al. How SGD selects the global minima in over-parameterized learning: A dynamical stability perspective. **Advances in Neural Information Processing** Systems**, 31, 2018.**
[51] Yuchen Zhang, Percy Liang, and Moses Charikar. A hitting time analysis of stochastic gradient Langevin dynamics. In Conference on Learning Theory**, pages 1980–2022.**
PMLR, 2017.

[52] Liu Ziyin, Botao Li, James B Simon, and Masahito Ueda. SGD with a constant large learning rate can converge to local maxima. arXiv preprint arXiv:2107.11774**, 2021.**
[53] Difan Zou, Pan Xu, and Quanquan Gu. Faster convergence of stochastic gradient Langevin dynamics for non-log-concave sampling. In Uncertainty in Artificial Intelligence**, pages 1152–1162. PMLR, 2021.**