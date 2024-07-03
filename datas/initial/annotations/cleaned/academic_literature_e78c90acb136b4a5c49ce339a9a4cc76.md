# A sharp uniform-in-time error estimate for Stochastic Gradient Langevin Dynamics 

Lei Li ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}}$ and Yuliang Wanga ${ }^{\mathrm{a}, \mathrm{b}}$<br>${ }^{a}$ School of Mathematical Sciences, Shanghai Jiao Tong University, Shanghai,<br>200240, P.R.China.<br>${ }^{b}$ Institute of Natural Sciences, MOE-LSC, Shanghai Jiao Tong University,<br>Shanghai, 200240, P.R.China.<br>${ }^{\mathrm{c}}$ Qing Yuan Research Institute, Shanghai Jiao Tong University, Shanghai,<br>200240, P.R.China.


#### Abstract

We establish a sharp uniform-in-time error estimate for the Stochastic Gradient Langevin Dynamics (SGLD), which is a popular sampling algorithm. Under mild assumptions, we obtain a uniform-in-time $O\left(\eta^{2}\right)$ bound for the KL-divergence between the SGLD iteration and the Langevin diffusion, where $\eta$ is the step size (or learning rate). Our analysis is also valid for varying step sizes. Based on this, we are able to obtain an $O(\eta)$ bound for the distance between the SGLD iteration and the distribution of the Langevin diffusion, in terms of Wasserstein or total variation distances.


## 1 Introduction

The Stochastic Gradient Langevin Dynamics (SGLD) [49], first proposed by Welling and Teh, has drawn great attention of researchers when dealing with optimization or sampling tasks $[2,33,40]$. As a sampling algorithm, SGLD can be viewed as a "random batch" version of the Unadjusted Langevin Algorithm (ULA), which is the Euler-Maruyama discretization of the Langevin diffusion, a stochastic process converging to a target Gibbs' distribution under suitable settings. As an optimization algorithm, SGLD can be viewed as a variant of the classical Stochastic Gradient Descent (SGD) [44], by adding independent Gaussian noise in each iteration of SGD. At recent decades, SGD and its variants [44, 25, 11, 37] have received a great deal of attention when solving high-dimensional tasks, ranging from computer vision, natural language processing, to high dimensional sampling, statistical optimization, etc. Also much theoretical analysis for SGD has been done by former researchers, including loss landscape of SGD iteration [46, 47], its dynamical stability [50] and diffusion approximation $[32,21,17]$. The combination of the SGD algorithm and the Langevin diffusion, can improve the behavior of both methods: for SGD, by taking another independent diffusion term into consideration, though not converging to a fixed point, the algorithm may be able to admit better ergodic properties and obtain better performance near saddle points $[26,52]$. Besides, the application of the methodology of random mini-batch to Langevin diffusion could result in some efficient methods that could reduce computational cost while preserving the dynamical and statistical properties. Examples include the SGLD algorithm we study in the paper and the random batch methods for interacting particle systems $[22,23]$.

In this paper, we consider the error estimate of SGLD for sampling from the target distribution $\pi \propto e^{-\beta U}$, where the function $U(x)$ of the form

$$
U(x):=\mathbb{E}_{\xi}[U(x ; \xi)], \quad x \in \mathbb{R}^{d}
$$

Here, $\xi \sim \nu$ is a random variable/vector for some distribution $\nu$. A typical form of (1.1) arising from applications like Bayesian inference or machine learning [49] is given by

$$
U(x):=U_{0}(x)+\frac{1}{N} \sum_{i=1}^{N} U_{i}(x)
$$

We remark that in [49], there was no $1 / N$ factor. Such a factor can be obtained by suitable scaling, like choosing suitable $\beta$ or rescaling the time in the Langevin diffusion, and it is helpful so that it can be written as an expectation over a probability distribution. Then the random vector $\xi$ can be taken as a random batch with size $S$ and then $U(x ; \xi)=U_{0}(x)+$ $\frac{1}{S} \sum_{i \in \xi} U_{i}(x)$. The associated (overdamped) Langevin diffusion (a stochastic differential equation (SDE)) for the target distribution $\pi$ is given by:

$$
d X=b(X) d t+\sqrt{2 \beta^{-1}} d W
$$

where

$$
b(x):=-\nabla U(x)
$$

and $W$ is the standard Brownian Motion in $\mathbb{R}^{d}$, and $\beta^{-1}>0$ is the fixed temperature constant. The target distribution $\pi(x) \propto e^{-\beta U(x)}$ is exactly the invariant distribution of the Langevin diffusion [41]. We also denote

$$
b^{\xi}(x)=-\nabla U(x ; \xi)
$$

in this paper. Then the SGLD algorithm with time step $\eta_{k}$ at $k$-th iteration is:

$$
\bar{X}_{T_{k+1}}=\bar{X}_{T_{k}}+\eta_{k} b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)+\sqrt{2 \beta^{-1} \eta_{k}} Z_{k}, \quad Z_{k} \sim N\left(0, I_{d}\right) \quad \text { i.i.d.. }
$$

with $T_{k}:=\sum_{i=0}^{k-1} \eta_{i}$. Here, $\xi_{k}$ are i.i.d. sampled. Also we have the following continuous version which coincides with the discrete SGLD at grid point $T_{k}$ :

$$
\bar{X}_{t}:=\bar{X}_{T_{k}}+\left(t-T_{k}\right) b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)+\sqrt{2 \beta^{-1}}\left(W_{t}-W_{T_{k}}\right), \quad t \in\left[T_{k}, T_{k+1}\right)
$$

At time $t$, denote densities of $X_{t}, \bar{X}_{t}$ by $\rho_{t}, \bar{\rho}_{t}$, respectively. In this paper, our main results focus on the "distance" between $\rho_{t}$ and $\bar{\rho}_{t}$. In our main results, we consider the KullbackLeibler (KL) divergence $[28]$, defined by

$$
D_{K L}(\mu \| \nu):=\int_{\mathbb{R}^{d}} \log \frac{d \mu}{d \nu} \mu(d x)
$$

where $\mu, \nu$ are probability measures on $\mathbb{R}^{d}$. Note that the KL-divergence is not a distance (a metric) in mathematics. Furthermore, based on this estimate, convergence rate to the invariant distribution of the Langevin diffusion (1.3) and results for particular time step sequences will be discussed.

A great deal of theoretical research for the SGLD algorithm has been done. In [51], the authors studied the hitting time of SGLD for non-convex optimization problem. Different from the goal of our work, instead of analyzing the convergence to a target distribution, the authors focused on finding a local minimum and the corresponding convergence results. For sampling-aimed tasks, much SGLD-related research has been done when the target distribution is $\log$-concave $[10,9,8]$. Convergence analysis for SGLD under non-convex settings is a bit more technical. In [43], the authors obtained an error bound for the Wasserstein-2 distance between the SGLD iteration and the target distribution of order $O\left(k \eta+e^{-k \eta}\right)$, where $k$ is the number of iterations and $\eta$ is the constant time step. In [36], assuming the boundedness of the drift function, the authors proved the error is of order $O(\sqrt{k \eta})$ in terms of Wasserstein-2 distance. In [53], assuming the second-order smoothness of the drift function, the authors obtained an improved bound of order $O\left(\sqrt{\eta} / S+\eta+(1-\eta)^{k}\right)$ in terms of total variance, where $S$ is the batch size. Different from most former work, where the
error bounds had an at least polynomial dependency on the time $T$, in [16], the authors obtained a uniform-in-time bound, enabling more long time analysis for SGLD. One point worth emphasizing is that, observing the time step $\eta$, none of the former work can get estimation better than $O(\sqrt{\eta})$ in terms of Wasserstein distances or total variation distance. In this paper, we resolve this issue and obtain a sharp bound in terms of $\eta$.

As has been mentioned, SGLD can be viewed as the "random batch" version of the EulerMaruyama scheme for the Langevin diffusion (1.3), which is also known as the Unadjusted Langevin Algorithm (ULA), or the Langevin Monte Carlo (LMC). In this paper, the main part of our result for SGLD is built upon our analysis for ULA, since it can be viewed as the simpler full-batch version of SGLD. Based on this observation, the convergence rate with respect to the time step $\eta$ for SGLD would not exceed that for ULA. Much work on ULA has been done before, some of which are found useful for our sharp analysis for SGLD. In [8], using the first order smoothness assumption, the authors showed that $D_{K L}\left(\hat{\rho}_{T} \| \rho_{T}\right)=$ $O(\eta T d)$, where $\hat{\rho}_{t}$ denotes the density of the continuous version ULA (similar with $\bar{\rho}_{t}$ ) at time $t, T$ is the length of the (finite) time interval, and $d$ is the dimension of the Euclidean space. However, this is not the optimal rate, since this result implies that $W_{2}\left(\hat{\rho}_{T}, \rho_{T}\right)=$ $O(\sqrt{\eta})$ rather than the well-known $O(\eta)[3,9]$. In [35], Mou improved the KL divergence $D_{K L}\left(\hat{\rho}_{T} \| \rho_{T}\right)$ from $O(\eta T d)$ to $O\left(\eta^{2} d^{2} T\right)$, so the Wasserstein distance is of $O(\eta)$. Compared with the former " $O(\eta T d)$ " result, the improved result in [35] needs second order smoothness of the drift function $b(x)$.

Our work is naturally motivated by the following two questions:

- For ULA, the error in terms of KL-divergence can be improved from $O(\eta)$ to $O\left(\eta^{2}\right)$ if we add the second order smoothness assumption for the drift. Can we do the same for SGLD to obtain a sharp bound?
- Most error analysis for ULA and SGLD has at least polynomial dependency for the time interval $T$, which prevents us from digging deeper into the asymptotic behaviors as $T \rightarrow \infty$ of these stochastic algorithms. Are we able to establish a uniform-in-time error bound?

In this paper, we give positive answers to both questions above.

The main contribution of this paper is to establish a uniform-in-time $O\left(\eta^{2}\right)$ bound for the KL-divergence between SGLD iterates and the Langevin diffusion, namely, in Theorem 3.2 we show that

$$
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) \leq c_{1} \eta_{0}^{2} e^{-A_{0} T_{k}}+c_{2} \int_{0}^{T_{k}} e^{-A_{0}\left(T_{k}-s\right)} f(s) d s
$$

where

$$
T_{k}=\sum_{i=0}^{k-1} \eta_{i}, \quad f(s)=\sum_{i=0}^{\infty} \eta_{i}^{2} \mathbf{1}_{\left[T_{i}, T_{i+1}\right)}(s)
$$

If we simply consider the constant step size (or learning rate), then a uniform-in-time $O\left(\eta^{2}\right)$ error bound is obtained in Corollary 3.1:

$$
\sup _{t \geq 0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) \leq c \eta^{2}
$$

The proof of our main results are based on the Markov property of SGLD. Indeed, the discrete SGLD process in our setting is a Markov Chain [13], and it is a time homogeneous one if the step size (or learning rate) is constant. Let $\rho_{t}^{\boldsymbol{\xi}}$ be the probability density of the fixed-batch version of SGLD (1.7) for a given sequence of batches $\boldsymbol{\xi}:=\left(\xi_{0}, \xi_{1}, \cdots, \xi_{k}, \cdots\right)$ (which is actually the ULA with the drift $b^{\xi}(x)$ ). Consequently, we have the following expression of the density:

$$
\bar{\rho}_{t}(\cdot)=\mathbb{E}_{\xi}\left[\rho_{t}^{\boldsymbol{\xi}}(\cdot)\right]
$$

Here, $\mathbb{E}_{\xi}\left[\rho_{t}^{\boldsymbol{\xi}}(\cdot)\right]$ means taking expectation for all possible choice of batch $\boldsymbol{\xi}$. Note that $\rho_{t}^{\boldsymbol{\xi}}$ satisfies a Fokker-Planck equation, whose explicit expression will be derived in Lemma 2.1.

By the Markov property, we are able to find that

$$
\mathbb{E}\left[\rho_{t}^{\xi} \mid \xi_{i}, i \geq k\right]=\mathcal{S}_{T_{k}, t}^{\xi_{k}} \bar{\rho}_{T_{k}}, \quad t \in\left[T_{k}, T_{k+1}\right)
$$

where the operator $\mathcal{S}_{T_{k}, t}^{\xi_{k}}$ is the evolution operator from $T_{k}$ to $t$ for the Fokker-Planck equation. Based on this observation, we are able to estimate the time derivative of the KL-divergence $D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)$, and then obtain the desired second-order error bound after a Grönwall's inequality. Also, while handling the details, techniques including integration by parts (to eliminate the Gaussian noise that would possibly lower the convergence rate) and Girsanov transform are adopted.

We also have some corollaries of our results:

First, we consider the special case $\eta_{i}=(\ell+i)^{-\theta}, i=0,1,2, \ldots$, with $\theta \in(0,1)$ being the decaying coefficient, which is common in many practical tasks [31]. In Section 3, we analyze the asymptotic convergence rate of $D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right)$ as $k \rightarrow+\infty$ for different $\theta$.

Second, we estimate the Wasserstein-2 distance [45] between the SGLD iteration and the target distribution $\pi$, and after comparison with former work, our result is confirmed to be a great improvement.

The rest of the paper is organized as follows. Before our main results, we introduce some preliminaries in Section 2 including the basic background and properties of the (overdamped) Langevin diffusion and its Euler-Maruyama discretization, ULA. In Section 3, we present and prove our main result: a sharp uniform-in-time estimate for SGLD, and some useful corollaries are also included. In Section 4, we provide the proof for a crucial local estimate, which is omitted in Section 3 for the convenience of readers. Some technical details that are not so important are moved to the Appendix. In Section 5, we perform discussion on our analysis on the Wasserstein-2 distance between the SGLD iteration and the target distribution $\pi$ based on our main results. The ergodicity of SGLD algorithm as well as the reason why our analysis is "sharp" are also discussed in Section 5.

## 2 Preliminaries

For the convenience of readers, let us begin with some basic definitions and properties that would be useful in this paper.

## 2.1 (Overdamped) Langevin Diffusion

Derived from the Langevin equation, the (overdamped) Langevin diffusion has strong, wellknown physical background [41]. Let us first consider the following second-order SDE called Langevin equation:

$$
\ddot{X}=-\nabla U(X)-\gamma \dot{X}+\sqrt{2 \gamma / \beta} \dot{W}
$$

where $\gamma$ is the friction coefficient, $\beta^{-1}:=k_{B} T$ with $k_{B}$ being the Boltzmann constant and $T$ being the (physical) temperature. The term $\gamma \dot{X}$ here describes the linear dissipation damping, and the term $\sqrt{2 \gamma / \beta} \dot{W}$ describes the fluctuation stochastic forcing. Note that the Brownian Motion $W$ is not pointwise differentiable, and so $\dot{W}$ should be understood in the distributional sense and is in fact the white noise [38]. Moreover, thanks to the Fluctuation-Dissipation Theorem [27], we are able to relate the dissipation and the fluctuation by considering the covariance of the fluctuation term.

Langevin equation (2.1) describes a particle moving according the Newton's second law and being in contact with a heat reservoir that is at equilibrium at temperature $T$. This physical is called an open classical system. To see this more clearly, we rewrite the Langevin equation (2.1) into an SDE system. Letting $Y=\dot{X}$, we have

$$
\left\{\begin{aligned}
d X & =Y d t \\
d Y & =-\nabla U(X) d t-\gamma Y d t+\sqrt{2 \gamma \beta^{-1}} d W
\end{aligned}\right.
$$

It is also well-known that if we consider the time rescaling $X^{\gamma}(t)=X(\gamma t)$, and let $\gamma \rightarrow+\infty$, the Langevin equation (2.1) turns into the overdamped Langevin diffusion [41]:

$$
d X=-\nabla U(X) d t+\sqrt{2 \beta^{-1}} d W
$$

The derived (overdamped) Langevin diffusion above has some pretty properties. First, it has invariant distribution $\pi \propto e^{-\beta U}$, which is trivial to check. Second, the invariant distribution $\pi$ satisfies the detailed balance since the probability flux $J(\pi):=b \cdot \pi-\frac{1}{2} \nabla \cdot(\Sigma \pi)$ equals zero with $b=-\nabla U$ and $\Sigma=\sqrt{2 \beta^{-1}} I$ here, and thus the stationary diffusion is reversible [41]. Third, the density of the Langevin diffusion satisfies the following FokkerPlanck equation:

$$
\partial_{t} \rho_{t}=-\nabla \cdot\left(\rho_{t} b\right)+\beta^{-1} \Delta \rho_{t},\left.\quad \rho_{t}\right|_{t=0}=\rho_{0}
$$

with $b=-\nabla U$. Moreover, if we add some mild assumptions to the function $U$ like strongly log-concaveness, the Langevin diffusion above is guaranteed to converge to equilibrium [34]. Note that in this paper, instead of $\log$-concaveness of the invariant distribution $\pi$, we add the much weaker assumption that $\pi$ satisfies a Log-Sobolev inequality (LSI).

### 2.2 Unadjusted Langevin Algorithm(ULA)

Among the classical numerical schemes for the Langevin diffusion (1.3), the simplest one is the well-known Euler-Maruyama scheme, which is also known as the Unadjusted Langevin Algorithm (ULA) or the Langevin Monte Carlo (LMC). Consider this Euler-Maruyama scheme with constant time step for $(1.3)$

$$
\hat{X}_{T_{k+1}}=\hat{X}_{T_{k}}+\eta_{k} b\left(\hat{X}_{T_{k}}\right)+\sqrt{2 \beta^{-1} \eta_{k}} Z_{k}, \quad Z_{k} \sim N\left(0, I_{d}\right) \quad \text { i.i.d. }
$$

where $\eta_{k}$ is the time step at $k$-th iteration and $T_{k}:=\sum_{i=0}^{k-1} \eta_{i}$. (2.5) naturally admits the following continuous version:

$$
\hat{X}_{t}:=\hat{X}_{T_{k}}+\left(t-T_{k}\right) b\left(\hat{X}_{T_{k}}\right)+\sqrt{2 \beta^{-1}}\left(W_{t}-W_{T_{k}}\right), \quad t \in\left[T_{k}, T_{k+1}\right)
$$

where $W_{t}$ is the Brownian Motion in $\mathbb{R}^{d}$. We also denote $\hat{\rho}_{t}(x)$ the probability density function of $\hat{X}_{t}$. It is not difficult to show that $\hat{\rho}_{t}$ satisfies a Fokker-Planck equation, and we conclude it in the following lemma:

Lemma 2.1. Denote $\hat{\rho}_{t}(x)$ the probability density function of $\hat{X}_{t}$ defined in (2.6). Then the following Fokker-Planck equation holds:

$$
\partial_{t} \hat{\rho}_{t}=-\nabla \cdot\left(\hat{\rho}_{t} \hat{b}_{t}\right)+\beta^{-1} \Delta \hat{\rho}_{t},\left.\quad \hat{\rho}_{t}\right|_{t=0}=\rho_{0}
$$

where

$$
\hat{b}_{t}(x):=\mathbb{E}\left[b\left(\hat{X}_{T_{k}}\right) \mid \hat{X}_{t}=x\right], \quad t \in\left[T_{k}, T_{k+1}\right)
$$

The derivation is not difficult and has appeared in many classical work [35]. Indeed, for $t \in\left[T_{k}, T_{k+1}\right)$, consider the random variable $\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}$, where $\hat{\mathcal{F}}_{T_{k}}=\sigma\left(\hat{X}_{s}, s \leq T_{k}\right)$. Then, by definition of $\hat{X}_{t}, \hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}$ satisfies:

$$
\partial_{t}\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right)=-\nabla \cdot\left(b\left(\hat{X}_{T_{k}}\right)\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right)\right)+\beta^{-1} \Delta\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right), \quad t \in\left[T_{k}, T_{k+1}\right)
$$

Taking expectation, we have

$$
\mathbb{E}\left[\partial_{t}\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right)\right]=\partial_{t} \hat{\rho}_{t}, \quad \mathbb{E}\left[\Delta\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right)\right]=\Delta \hat{\rho}_{t}
$$

and for the drift term,

$$
\begin{aligned}
\mathbb{E}\left[-\nabla \cdot\left(\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right)(x) b\left(\hat{X}_{T_{k}}^{\xi}\right)\right)\right] & =-\nabla \cdot \int\left(\hat{\rho}_{t} \mid \hat{\mathcal{F}}_{T_{k}}\right)(x \mid y) b(y) \hat{\rho}_{T_{k}}(y) d y \\
& =-\nabla \cdot \int b(y) \hat{\rho}_{t, T_{k}}(x, y) d y \\
& =-\nabla \cdot\left(\hat{\rho}_{t}(x) \mathbb{E}\left[b\left(\hat{X}_{T_{k}}^{\xi}\right) \mid \hat{X}_{t}=x\right]\right)
\end{aligned}
$$

where $\hat{\rho}_{t, T_{k}}$ indicates the joint distribution density of $\hat{\rho}_{t}$ and $\hat{\rho}_{T_{k}}$. Note that we use Bayes' law in the second equality. Combining all the above, we obtain the desired result (2.7).

## 3 Main results

In this section, we present our main result of this paper: a sharp uniform-in-time error estimate for SGLD. In Section 3.1, we present the assumptions required by later analysis. In Section 3.2, we give some auxiliary results, including propagation of LSI of Langevin diffusion, moment control for ULA, and estimation of the Fisher information for ULA. After these preparations, in Section 3.3, we present the main theorem, Theorem 3.2, by first showing a crucial local result, Proposition 3.2. Moreover, we give some corollaries including constant time step case, special decaying step size (or learning rate) case, and the special step size case, $\eta_{i}=(\ell+i)^{-\theta}$.

### 3.1 Our assumptions

Before the main results and proofs, we firstly give the following assumptions we use throughout this paper. Recall the definition of the drift function $b$ in SGLD and its target distribution $\pi$ in Section 1. For technical reasons, we will need the following assumptions.

## Assumption 3.1.

(a) (1st order smoothness) For a.e. $\xi \sim \nu, b^{\xi}$ is Lipshitz with a uniform constant L, i.e. $\forall \xi, \forall x, y \in \mathbb{R}^{d}$

$$
\left|b^{\xi}(x)-b^{\xi}(y)\right| \leq L|x-y|
$$

(b) (2nd order smoothness) For a.e. $\xi \sim \nu, \nabla b^{\xi}$ is Lipshitz with a uniform constant $L_{2}$, i.e. $\forall \xi, \forall x, y \in \mathbb{R}^{d}$,

$$
\left|\nabla b^{\xi}(x)-\nabla b^{\xi}(y)\right| \leq L_{2} d^{-\frac{1}{2}}|x-y|
$$

(c) (distance dissipation) For a.e. $\xi \sim \nu, b^{\xi}$ is confining in the sense that

$$
x \cdot b^{\xi}(x) \leq-\mu|x|^{2}+\sigma
$$

with $\mu, \sigma$ being positive constants.

(d) (boundedness) $b^{\xi}-b$ is uniformly bounded, namely,

$$
\operatorname{esssup}_{\xi}\left\|b^{\xi}-b\right\|_{L^{\infty}\left(\mathbb{R}^{d}\right)}<+\infty
$$

Moreover, the coefficient $L, L_{2}, \mu, \sigma$ are independent of $\xi$ and $d$.

In condition (a), the Lipschitz constant $L$ is the upper bound of the spectrum norm (largest singular value) of the Jacobian matrix and it is insensitive to the dimension $d$. In (3.2) in condition (b), we have put $d^{-1 / 2}$ in the constant and assumed $L_{2}$ to be independent of $d$. The intuition is that the left hand side is the spectral norm of the Jacobian matrix, which can be assumed to be insensitive to $d$ while $|x-y|$ scales like $\sqrt{d}$. As we shall later, putting such a scaling can make the bounds of the relative entropy and Fisher information linear in $d$ (see our discussion at the end of Section 5.2), which is the correct scaling. This is a difference from the result in [35].

Note that condition (d) is equivalent to saying that $b^{\xi}-b^{\tilde{\xi}}$ is also uniformly bounded for two different $\xi, \tilde{\xi}$. In (d) of Assumption 3.1, we do not need the uniform boundedness for every $b^{\xi}$, though (d) naturally holds when $\operatorname{esssup}_{\xi}\left\|b^{\xi}(x)\right\|_{\infty}<\infty$, which is a much stronger condition. Actually the condition (d) is natural in applications. In many problems in machine learning, the loss has the same asymptotics for different data point.

In our paper, conditions (c) is used only to control the moments. Actually condition (c) is the confinement condition which is crucial in literature for ergodicity. In our case, the $\log$ Sobolev inequality later in Assumption 3.2 actually plays the role of confinement for ergodicity. Moreover, it is not difficult to see that if one has the stronger boundedness condition $\operatorname{esssup}_{\xi} \sup _{x}\left|b^{\xi}(x)\right|<\infty$, then conditions (c) and (d) can be removed since the only place we use the distance dissipation condition (c) is the moment control (Propostition 3.1), but the only place we use the moment control is bounding terms like $b^{\xi}\left(X_{t}\right)$. Now if we assume each $b^{\xi}$ is bounded, we do not need the result for moment control any more.

## Assumption 3.2.

(a) ( $\lambda$-warm start) There exists $\lambda \geq 1$ such that the initial distribution $\rho_{0}$ satisfies

$$
\frac{1}{\lambda} \leq \frac{\rho_{0}}{\pi} \leq \lambda
$$

where $\pi \propto e^{-\beta U}$ is the invariant distribution of (1.3). Note that $\rho_{0}$ is the initial distribution for all the processes $X, \hat{X}$, and $\bar{X}$, and $\lambda$ is independent of the dimension $d$.

(b) (LSI for $\pi$ ) The invariant distribution $\pi \propto e^{-\beta U}$ satisfies a Log-Sobolev inequality with a constant $C_{\pi}^{L S}$, namely, $\forall f \in C_{>0}^{\infty}$,

$$
\operatorname{Ent}_{\pi}(f):=\int f \log f d \pi-\left(\int f d \pi\right) \log \left(\int f d \pi\right) \leq C_{\pi}^{L S} \int \frac{|\nabla f|^{2}}{f} d \pi
$$

Here, $C_{>0}^{\infty}$ consists of all nonnegative smooth functions.

The Log-Sobolev inequality (LSI) was first discussed by Gross in 1975 [20]. Besides the simplest Gaussian distribution, other distributions satisfying an LSI can be found following the Bakry-Emery criterion [4], including strongly log-concave ones. It is also shown that distributions that are strongly log-concave outside a compact set also satisfy the LSI [29]. We remark that the log-concaveness outside a compact set can imply both the distance dissipation and the log Sobolev inequality so the LSI assumption is much weaker than the log-concaveness assumption in many other literature. However, the distance dissipation condition $x \cdot b \leq-\mu|x|^{2}+\sigma$ outside a compact set can not derive the corresponding LSI so neither the distance dissipation nor the LSI assumption can be simply removed though they seem to have repetition somehow.

### 3.2 Some auxiliary results

Before presenting the main theorem, we give some useful auxiliary results first, including the propagation of LSI for the Langevin diffusion (1.3), moment control for ULA (2.6), and estimation of Fisher information for ULA (2.6).

### 3.2.1 Propagation of Log-Sobolev inequality

In this section, we aim to establish a Log-Sobolev inequality (LSI) for $\rho_{t}$, which is the density of $X_{t}$ in the Langevin diffusion (1.3).

Theorem 3.1. Consider the Fokker-Planck equation (2.4) associated with the SDE (1.3). Suppose Assumption 3.2 holds. Then, $\rho_{t}$ satisfies a LSI with a uniform LSI constant $\lambda^{2} C_{\pi}^{L S}$.

The following Holley-Stroock perturbation lemma [5] is essential to our proof :

Lemma 3.1 (Holley-Stroock perturbation). Suppose the probability measure $\nu \in \mathcal{P}\left(\mathbb{R}^{d}\right)$ satisfies an LSI with constant $C_{\nu}^{L S}$, and $\mu \in \mathcal{P}\left(\mathbb{R}^{d}\right)$ satisfies $d \mu=h d \nu$ with the uniform bound $\frac{1}{\lambda} \leq h \leq \lambda$. Then $\mu$ satisfies an LSI with constant $\lambda^{2} C_{\nu}^{L S}$.

Proof of Theorem 3.1:

$$
\rho_{t}=\frac{\rho_{t}}{\pi} \pi=: q_{t} \pi
$$

Since $b=\beta^{-1} \nabla \log \pi$, the detailed balanced is satisfied [34]. So it is well-known that $q_{t}$ satisfies the following backwards Kolmogorov equation [30]:

$$
\partial_{t} q_{t}=b \cdot \nabla q_{t}+\beta^{-1} \Delta q_{t},\left.\quad q_{t}\right|_{t=0}=\frac{\rho_{0}}{\pi}
$$

and $q_{t}$ can be expressed by the following conditional expectation form:

$$
q_{t}(x)=\mathbb{E}\left[q_{0}\left(X_{t}\right) \mid X_{0}=x\right]
$$

Then, as a direct consequence of (3.9), we know that at any time $t>0, \inf _{x} q_{t} \geq \inf _{x} q_{0}$, and $\sup _{x} q_{t} \leq \sup _{x} q_{0}$. Combining this fact and condition (a) in Assumption 3.2, it holds that

$$
\frac{1}{\lambda} \leq q_{t} \leq \lambda, \quad \forall t \geq 0
$$

Then, combining (3.10), Lemma 3.1, and (b) in Assumption 3.2, the conclusion holds.

Note that the fact $\inf _{x} q_{t} \geq \inf _{x} q_{0}, \sup _{x} q_{t} \leq \sup _{x} q_{0}$ can also be derived from classical results of PDE. Indeed, since the backward Kolmogorov equation (3.8) for $q_{t}$ is of parabolic type, the maximal principle holds, whose details can be found in Chapter 7 of [15]. By maximal principle and condition (a) in Assumption 3.2, we also obtain

$$
\frac{1}{\lambda} \leq q_{t} \leq \lambda, \quad \forall t \geq 0
$$

### 3.2.2 Moment control

In this section, we aim to find a uniform-in-time bound for the moments $\mathbb{E}\left|\bar{X}_{t}^{\xi}\right|^{p}$ with $\bar{X} \xi$ defined in (1.12) of Section 1 and $p=2,4$. The details could be found in the proposition below:

Proposition 3.1. Consider the process $\bar{X}_{t}$ defined in (1.7) of Section 1. Suppose (a), (c) of Assumption 3.1 holds. For all integer $p \geq 1$, there exists positive constants $c_{p}$ and $\Delta_{p}$ independent of $t$ and $\boldsymbol{\xi}$ such that if $\eta_{k} \leq \Delta_{p}$ for all $k$, then

$$
\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right] \leq c_{p} d^{\frac{p}{2}}, \quad \forall t \geq 0
$$

Moreover, for all integer $p \geq 1$, there exists a positive constant $\alpha_{p}$ such that when $\alpha<\alpha_{p}$,

$$
\sup _{t \geq 0} \mathbb{E}\left[e^{\alpha\left|\bar{X}_{t}\right|^{p}} \mid \mathcal{F}_{\xi}\right]<+\infty
$$

Here, $\mathcal{F}_{\xi}$ denotes the $\sigma$-algebra generated by $\boldsymbol{\xi}=\left(\xi_{k}\right)_{k \geq 0}$.

See Section A. 1 for the detailed proof.

### 3.2.3 Estimate of the Fisher information

The Fisher information for a probability measure $\rho$ is defined by

$$
\mathcal{I}(\rho):=\int|\nabla \log \rho|^{2} \rho d x
$$

In our analysis, we come up with the exponential-weighted sum of Fisher information at the grid point $T_{k}$ of ULA (SGLD with fixed batch), and a uniform-in-time order-one bound for this summation is required. To handle this, our strategy is to firstly estimate the continuous sum (i.e. integration) of the exponential-weighted Fisher information in Lemma 3.2. Then, using the existing stability result (Lemma 3.3 below) for Fisher information of ULA [35], we are able to control the desired discrete summation with the integration of the exponentialweighted Fisher information along the time axis.

Recall that $\rho_{t}^{\xi}$ is the law of the SGLD (1.7) conditioning on the given sequence of batches $\boldsymbol{\xi}=\left(\xi_{0}, \xi_{1}, \cdots, \xi_{k}, \cdots\right)$. In Section A.2, we first establish

$$
\frac{d}{d t} D_{K L}\left(\rho_{t}^{\boldsymbol{\xi}} \| \pi\right) \leq-c_{0} \mathcal{I}\left(\rho_{t}^{\boldsymbol{\xi}}\right)+c_{1} d
$$

where we recall $\pi \propto e^{-\beta U}$ and consequently

$$
D_{K L}\left(\rho_{t}^{\boldsymbol{\xi}} \| \pi\right) \leq c d
$$

where $c_{0}, c_{1}, c$ are positive constants independent of $t$ and $\xi$. Then, after simple calculation including integration by parts, we are able to prove the following Lemma:

Lemma 3.2. Let $f$ be a non-increasing, nonnegative, piecewise-constant function. Then under Assumption 3.1, 3.2, there exists $\Delta_{0}>0$, for any $A_{0}>0$, there exist positive constants $M_{1}, M_{2}$, independent of $T$ and $\boldsymbol{\xi}$ such that when the step size sequence $\left\{\eta_{k}\right\}$ defined in (1.6) is bounded by $\Delta_{0}$, the followings hold:

$$
\sup _{t \geq 0} D_{K L}\left(\rho_{t}^{\boldsymbol{\xi}} \| \pi\right) \leq c d
$$

where $c$ is independent of $T, d$ and $\boldsymbol{\xi}$. Moreover,

$$
\begin{aligned}
& \int_{0}^{T} e^{-A_{0}(T-s)} f(s) \mathcal{I}\left(\rho_{s}^{\boldsymbol{\xi}}\right) d s \\
& \quad \leq M_{1} D_{K L}\left(\rho_{0} \| \pi\right) f(0) e^{-A_{0} T}+M_{2}\left(1+\sup _{s \geq 0} D_{K L}\left(\rho_{s}^{\boldsymbol{\xi}} \| \pi\right)\right) \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s
\end{aligned}
$$

The next lemma bounds the Fisher information $\mathcal{I}\left(\rho_{t}^{\xi}\right)$ at time $t$ with the Fisher information $\mathcal{I}\left(\rho_{T_{k}}^{\xi}\right)$ at the grid point. The estimation is valid for small $\eta_{k}$, and we can view it as one kind of stability for the Fisher information of an only piecewise continuous process. The proof of the following lemma can be found in Lemma 6 of [35]

Lemma 3.3. Under the same setting of Lemma 3.2, if $\eta_{k} \leq \frac{1}{2 L}, k \geq 0$, then there is a positive constant $c$ independent of $k, d$, and $\boldsymbol{\xi}$ such that

$$
\mathcal{I}\left(\rho_{t}^{\boldsymbol{\xi}}\right) \leq 8 \mathcal{I}\left(\rho_{t_{0}}^{\boldsymbol{\xi}}\right)+c \eta_{k}^{2} d, \quad \forall T_{k} \leq t_{0} \leq t \leq T_{k+1}
$$

Clearly, with a factor $d^{-1 / 2}$ in the Lipschitz constant in Assumption 3.1, the bounds of the relative entropy and Fisher information are linear in $d$.

### 3.3 Main theorems

Equipped with the preparation work before, we are then able to establish a sharp uniformin-time second order error estimate for SGLD in terms of KL-divergence. Our analysis for SGLD is from local to global. The following local estimation is crucial to our main result, and the $\eta^{2}$ term here is the core of our $O\left(\eta^{2}\right)$ bound in the main theorem. To avoid overloading the notation, the dependence on the size of function family $N$, the dimension $d$, the temperature $\beta$, and other parameters in Assumption 3.1, 3.2 are implicit.

Proposition 3.2. Consider the probability density functions $\rho_{t}, \bar{\rho}_{t}$ for $X_{t}, \bar{X}_{t}$ defined in (1.3), (1.7). Then under Assumption 3.1, 3.2, there exist positive constants $A_{0}, A_{1}, \Delta_{0}$ independent of $k$ and $d$ such that when $\eta_{k}<\Delta_{0}$, the following local estimation holds:

$$
\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) \leq-A_{0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)+A_{1} \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right), \quad \forall t \in\left[T_{k}, T_{k+1}\right)
$$

For the convenience of readers, we move the proof of Proposition 3.2 to the next section. Combining this local estimation for SGLD and the previous result for estimating the Fisher information of ULA (fixed batch SGLD), it is not difficult to obtain the following main theorem.

Define the following piecewise-constant function $f$ :

$$
f(t):=\sum_{i=0}^{\infty} \eta_{i}^{2} \mathbf{1}_{\left[T_{i}, T_{i+1}\right)}(t)
$$

where $\mathbf{1}_{E}$ is the indicator function for set $E$.

Theorem 3.2. [Sharp error analysis for SGLD] Consider the probability density functions $\rho_{t}, \bar{\rho}_{t}$ for $X_{t}, \bar{X}_{t}$ defined in (1.3), (1.7). Suppose the time step sequence $\left\{\eta_{k}\right\}$ is nonincreasing. Then under Assumption 3.1, 3.2, there exists positive constants $\Delta_{0}, A_{0}, c_{1}, c_{2}$ independent of $k$ and $d$ such that when $\eta_{0} \leq \Delta_{0}$,

$$
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) \leq c_{1} \eta_{0}^{2} e^{-A_{0} T_{k}}+c_{2} d \int_{0}^{T_{k}} e^{-A_{0}\left(T_{k}-s\right)} f(s) d s
$$

for $f$ defined in (3.21). Consequently, if the non-increasing time step sequence $\left\{\eta_{k}\right\}$ converges to zero, and $\sum_{i=0}^{+\infty} \eta_{i}=+\infty$, the $K L$-divergence $D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right)$ also tends to zero.

Proof of Theorem 3.2: By Proposition 3.2, since $\eta_{k} \leq \eta_{0} \leq \Delta_{0}$, and since the Fisher information $\mathcal{I}(\rho)$ is a convex functional with respect to $\rho$ (see [18, Lemma 4.2]), we have

$$
\begin{aligned}
\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) & \leq-A_{0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)+A_{1} \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right) \\
& \leq-A_{0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)+A_{1} \eta_{k}^{2}\left(d+\mathbb{E}_{\xi} \mathcal{I}\left(\rho_{T_{k}}^{\xi}\right)\right), \quad t \in\left[T_{k}, T_{k+1}\right)
\end{aligned}
$$

Then by Grönwall's inequality, for all $k$, we have

$$
\begin{aligned}
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) & \leq \mathbb{E}_{\xi} \sum_{i=0}^{k-1} \int_{T_{i}}^{T_{i+1}} e^{-A_{0}\left(T_{k}-s\right)} A_{1} \eta_{i}^{2}\left(d+\mathcal{I}\left(\rho_{T_{i}}^{\xi}\right)\right) d s \\
& =A_{1} d \int_{0}^{T_{k}} e^{-A_{0}(T-s)} f(s) d s+A_{1} \mathbb{E}_{\xi} \int_{0}^{T_{k}} e^{-A_{0}(T-s)} \mathcal{I}\left(\rho_{T_{i}}^{\xi}\right) f_{k}(s) d s \\
& \leq \tilde{A}_{1} d \int_{0}^{T_{k}} e^{-A_{0}(T-s)} f(s) d s+8 A_{1} \mathbb{E}_{\xi} \int_{0}^{T_{k}} e^{-A_{0}(T-s)} \mathcal{I}\left(\rho_{s}^{\xi}\right) f(s) d s
\end{aligned}
$$

and the last inequality of (3.24) is due to Lemma 3.3.

Clearly, $f$ is a piecewise constant, non-increasing, nonnegative function. Then by Lemma 3.2, we are able to estimate the exponential-weighted sum of Fisher information along the path:

$$
\int_{0}^{T_{k}} e^{-A_{0}(T-s)} \mathcal{I}\left(\rho_{s}^{\xi}\right) f(s) d s \leq M_{1}^{\prime} \eta_{0}^{2} e^{-A_{0} T_{k}}+M_{2}^{\prime} d \int_{0}^{T_{k}} e^{-A_{0}(T-s)} f(s) d s
$$

Here, the positive constanes $M_{1}^{\prime}, M_{2}^{\prime}$ are independent of the batch $\boldsymbol{\xi}$ and the time $T_{k}$.

Finally, combining (3.25) and (3.24), we have

$$
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) \leq c_{1} \eta_{0}^{2} e^{-A_{0} T_{k}}+c_{2} d \int_{0}^{T_{k}} e^{-A_{0}\left(T_{k}-s\right)} f(s) d s
$$

where $c_{1}, c_{2}, A_{0}$ are positive constant independent of the iteration number $k$ and the dimension $d$.

Clearly, by (3.26), when the sequence $\left\{\eta_{k}\right\}$ decays to zero, and $\sum_{k=0}^{\infty} \eta_{k}=+\infty$, the KL-divergence $D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right)$ tends to zero. This then ends the proof.

As a direct corollary, if we consider the constant step size (or learning rate) case $\left(\eta_{k} \equiv \eta\right)$, the following sharp time-independent estimation can be established:

Corollary 3.1 (Sharp uniform-in-time error analysis for SGLD, constant step size $\eta$ ). Consider the probability density functions $\rho_{t}, \bar{\rho}_{t}$ for $X_{t}, \bar{X}_{t}$ defined in (1.3), (1.7). Suppose $\eta_{k}=\eta, \forall k$. Then, under Assumption 3.1, 3.2, there exist positive constants $c, \Delta_{0}$ independent of $t$ such that for all $\eta \in\left(0, \Delta_{0}\right)$,

$$
\sup _{t>0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) \leq c d \eta^{2}
$$

Since ULA can be viewed as a special case of SGLD when $b^{\xi} \equiv b$ (or the batch size $S$ equals $N$ for the special case (1.2)), we have the following direct corollary:

Corollary 3.2 (Sharp uniform-in-time error analysis for ULA, constant time step $\eta$ ). Consider the probability density functions $\rho_{t}$ and $\hat{\rho}_{t}$ defined in (1.3), (2.6). Suppose $\eta_{k}=\eta, \forall k$. Then, under Assumption 3.1, 3.2, there is a positive constant c independent of $t$ and $\Delta_{0}>0$ such that for all $\eta \in\left(0, \Delta_{0}\right)$,

$$
\sup _{t>0} D_{K L}\left(\hat{\rho}_{t} \| \rho_{t}\right) \leq c d \eta^{2}
$$

Based on our main result, Theorem 3.2 or Corollary 3.1, we are able to obtain the following corollaries, which are useful in many practical tasks.

First, we choose special case for the decaying time step sequence $\left\{\eta_{k}\right\}_{k=0}^{+\infty}$, and applying Theorem 3.2, we obtain the following asymptotic convergence rate:

Corollary 3.3 (asymptotic rate for special case). Suppose Assumption 3.1, 3.2 hold. Set $\eta_{i}=(\ell+i)^{-\theta}, i \in \mathbf{N}$, with $\theta \in(0,1)$ being the decaying coefficient. Here, $\ell$ is a positive integer such that $\eta_{0} \leq \Delta_{0}$, where $\Delta_{0}>0$ is a positive constant obtained in Theorem 3.2. Then there exist $k_{0}>0, c>0$ such that $\forall k>k_{0}$,

$$
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) \leq c d\left(\frac{1}{k}\right)^{2 \theta}
$$

Proof of Corollary 3.3: For $\theta \in(0,1)$, by Theorem 3.2, we have

$$
\begin{aligned}
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) & \leq c_{1} e^{-A_{0} T_{k}}+c_{2} d\left(\sum_{i=1}^{\lfloor k / 2\rfloor}+\sum_{i=1+\lfloor k / 2\rfloor}^{k}\right)\left((\ell+i)^{-2 \theta}\left(e^{-A_{0}\left(T_{k}-T_{i}\right)}-e^{-A_{0}\left(T_{k}-T_{i-1}\right)}\right)\right) \\
& \leq c_{1} e^{-A_{0} T_{k}}+c_{2}^{\prime} d\left(e^{-A_{0}\left(T_{k}-T_{\lfloor k / 2\rfloor}\right)}-e^{-A_{0} T_{k}}\right)+c_{2}^{\prime} d\left(\frac{2}{k}\right)^{2 \theta}\left(1-e^{-A_{0}\left(T_{k}-T_{1+\lfloor k / 2\rfloor}\right)}\right) \\
& \leq c_{1} e^{-A_{0} T_{k}}+c_{2}^{\prime} d e^{-A_{0}\left(T_{k}-T_{\lfloor k / 2\rfloor)}\right)}+c_{2}^{\prime} d\left(\frac{2}{k}\right)^{2 \theta}
\end{aligned}
$$

As $k \rightarrow+\infty, T_{k} \sim \sum_{i=1}^{k} i^{-\theta} \sim k^{1-\theta}$. Hence, $e^{-A_{0} T_{k}}$ and $e^{-A_{0}\left(T_{k}-T_{\lfloor k / 2\rfloor}\right)}$ decay much faster than $k^{-2 \theta}$ as $k \rightarrow+\infty$. Therefore, there exists $k_{0}>0$ such that when $k>k_{0}$,

$$
D_{K L}\left(\bar{\rho}_{T_{k}} \| \rho_{T_{k}}\right) \leq c d\left(\frac{1}{k}\right)^{2 \theta}
$$

where $c$ is a positive constant independent of $k$. This is what we want.

## 4 Delayed proof for the local estimation

In this section, we prove the crucial local analysis result of this paper, Proposition 3.2. For convenience, the proof is still a high-level overview and more technical details can be found in the Appendix.

Proof of Proposition 3.2: We prove this local result following three main steps.

STEP 1: estimate time derivative of KL-divergence $\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)$ via Fokker-Planck equations.

Firstly, note that SGLD at discrete time points is a Markov chain (which is timehomogeneous when $\eta_{k}$ is a constant), and $\bar{\rho}_{T_{k}}$ is the law at $T_{k}$. Recall that $\rho_{t}^{\xi}$ is the probability density of the fixed-batch version of SGLD (1.7) for a given sequence of batches $\boldsymbol{\xi}:=\left(\xi_{0}, \xi_{1}, \cdots, \xi_{k}, \cdots\right)$ so that $\bar{\rho}_{T_{k}}=\mathbb{E}_{\xi}\left[\rho_{T_{k}}^{\xi}\right]$. Moreover, by Markov property, we are able to define

$$
\bar{\rho}_{t}^{\xi_{k}}:=\mathbb{E}\left[\rho_{t}^{\xi} \mid \xi_{i}, i \geq k\right]=\mathcal{S}_{T_{k}, t}^{\xi_{k}} \bar{\rho}_{T_{k}}, \quad t \in\left[T_{k}, T_{k+1}\right)
$$

where the operator $\mathcal{S}_{T_{k}, t}^{\xi_{k}}$ is the evolution operator from $T_{k}$ to $t$ for the Fokker-Planck equation of the continuous SGLD (1.7) derived in Lemma 2.1, for some given $\xi_{k}$ :

$$
\partial_{t} \bar{\rho}_{t}^{\xi_{k}}=-\nabla \cdot\left(\bar{\rho}_{t}^{\xi_{k}} \bar{b}_{t}^{\xi_{k}}\right)+\beta^{-1} \Delta \bar{\rho}_{t}^{\xi_{k}}, \quad \bar{\rho}_{T_{k}}^{\xi_{k}}=\bar{\rho}_{T_{k}}
$$

where $t \in\left[T_{k}, T_{k+1}\right)$ and

$$
\bar{b}_{t}^{\xi_{k}}(x):=\mathbb{E}\left[b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right) \mid \bar{X}_{t}=x, \xi_{k}\right], \quad t \in\left[T_{k}, T_{k+1}\right)
$$

Next, we calculate $\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)$ based on (4.2). Since $\bar{\rho}_{t}=\mathbb{E}_{\xi_{k}}\left[\bar{\rho}_{t}^{\xi_{k}}\right]$ for $t \in\left[T_{k}, T_{k+1}\right)$, by (4.2) we have

$$
\partial_{t} \bar{\rho}_{t}=\mathbb{E}_{\xi_{k}}\left[-\nabla \cdot\left(\bar{b}_{t}^{\xi_{k}} \bar{\rho}_{t}^{\xi_{k}}\right)+\beta^{-1} \Delta \bar{\rho}_{t}^{\xi_{k}}\right]
$$

Then, using the Fokker-Planck equations (4.4), (2.4) for $\bar{\rho}_{t}$ and $\rho_{t}$, respectively, we are able to calculate the following time derivative of the KL-divergence in the time interval $\left[T_{k}, T_{k+1}\right)$ :

$$
\begin{aligned}
& \frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)=\int\left(\partial_{t} \bar{\rho}_{t}\right)\left(\log \frac{\bar{\rho}_{t}}{\rho_{t}}+1\right) d x+\int\left(\partial_{t} \rho_{t}\right)\left(-\frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x \\
& =\left(\mathbb{E}_{\xi_{k}}\left(\bar{b}_{t}^{\xi_{k}} \bar{\rho}_{t}^{\xi_{k}}\right)-\beta^{-1} \nabla \bar{\rho}_{t}\right) \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right)+\left(b \rho_{t}-\beta^{-1} \nabla \rho_{t}\right) \cdot\left(-\nabla \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x \\
& =\int\left(\left(b \bar{\rho}_{t}-\beta^{-1} \nabla \bar{\rho}_{t}\right) \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right)+\left(b \rho_{t}-\beta^{-1} \nabla \rho_{t}\right) \cdot\left(-\nabla \frac{\bar{\rho}_{t}}{\rho_{t}}\right)\right) d x \\
& +\int \mathbb{E}_{\xi_{k}}\left[\left(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}\right) \rho_{t}^{\xi_{k}}\right] \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x+\int \mathbb{E}_{\xi_{k}}\left[b^{\xi_{k}} \bar{\rho}_{t}^{\xi_{k}}-b \bar{\rho}_{t}\right] \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x
\end{aligned}
$$

Note that $\left|b^{\xi_{k}} \bar{\rho}_{t}^{\xi_{k}}-b \bar{\rho}_{t}\right|$ is of order $O(1)$. The mechanism is that $\bar{\rho}_{t}^{\xi_{k}}$ is close to $\bar{\rho}_{t}$ and using the consistency of random batch $\mathbb{E}_{\xi_{k}}\left[b^{\xi_{k}}(x)\right]=b(x)$. This can cancel the leading error. Hence, we rearrange the terms to get

$$
\begin{aligned}
\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t}|| \rho_{t}\right)= & \left(-\beta^{-1} \int\left|\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right|^{2} \bar{\rho}_{t} d x\right)+\left(\int \mathbb{E}_{\xi_{k}}\left[\left(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}\right) \bar{\rho}_{t}^{\xi_{k}}\right] \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x\right) \\
& +\left(\int \mathbb{E}_{\xi_{k}}\left[\left(b^{\xi_{k}}-b\right)\left(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}\right)\right] \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x\right) \\
:= & J_{1}+J_{2}+J_{3}
\end{aligned}
$$

For $J_{2}$, by Young's inequality,

$$
\begin{aligned}
J_{2} & =\mathbb{E}_{\xi_{k}}\left[\int\left(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}\right) \bar{\rho}_{t}^{\xi_{k}} \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x\right] \\
& \leq \beta \mathbb{E}_{\xi_{k}} \int\left|\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}\right|^{2} \bar{\rho}_{t}^{\xi_{k}} d x+\frac{1}{4 \beta} \int\left|\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right|^{2} \bar{\rho}_{t} d x
\end{aligned}
$$

where $\gamma$ is a positive constant.

For $J_{3}$, our approach is to introduce another copy of SGLD $\bar{Y}$ such that

- $\bar{Y}_{T_{k}}=\bar{X}_{T_{k}}$
- the Browmian Motion are the same in $\left[T_{k}, T_{k+1}\right)$;
- the batch $\tilde{\xi}_{k}$ on $\left[T_{k}, T_{k+1}\right)$ is independent of $\xi_{k}$.

Consequently, the corresponding density of the law $\bar{\rho}_{t} \tilde{\xi}_{k}$ for $\bar{Y}$ satisfy both (4.1) and (4.2), with $\bar{\rho}_{T_{k}}^{\tilde{\xi}_{k}}=\bar{\rho}_{T_{k}}$. Using the consistency of the random batch, we are able to obtain

$$
J_{3}=\mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}} \int\left[\left(b^{\xi_{k}}-b\right)\left(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\tilde{\xi}_{k}}\right)\right] \cdot\left(\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right) d x
$$

Then by Young's inequality we have:

$$
J_{3} \leq \beta \mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}}\left[\int\left|b^{\xi_{k}}-b\right|^{2} \frac{\left|\rho_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}\right|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}} d x\right]+\frac{1}{4 \beta} \int\left|\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right|^{2} \overline{\rho_{t}} d x
$$

where we applied the fact $\mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}}\left|\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right|^{2} \rho_{\rho_{t}}^{\tilde{\xi_{k}}}=\left|\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right|^{2} \bar{\rho}_{t}$. The introduction of the independent copy of $\tilde{\xi}_{k}$ is useful since we may apply the Girsanov transform later to estimate this quantitatively.

Now by Theorem 3.1, $\rho_{t}$ satisfies a LSI with a constant $\lambda^{2} C_{\pi}^{L S}$, namely, $\forall f \in C_{>0}^{\infty}$,

$$
\operatorname{Ent}_{\rho_{t}}(f):=\int f \log f d \rho_{t}-\left(\int f d \rho_{t}\right) \log \left(\int f d \rho_{t}\right) \leq \lambda^{2} C_{\pi}^{L S} \int \frac{|\nabla f|^{2}}{f} d \rho_{t}
$$

Taking $f=\frac{\overline{\bar{p}_{t}}}{\rho_{t}}$, one has

$$
\int\left|\nabla \log \frac{\bar{\rho}_{t}}{\rho_{t}}\right|^{2} \bar{\rho}_{t} d x \geq \frac{1}{\lambda^{2} C_{\pi}^{L S}} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)
$$

Then, combining (4.6), (4.7), (4.9), and (4.11), one has

$$
\begin{aligned}
\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) & \leq-A_{0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) \\
& +\beta \mathbb{E}_{\xi_{k}}\left[\int\left|\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}\right|^{2} \bar{\rho}_{t}^{\xi_{k}} d x\right]+\beta \mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}}\left[\int\left|b^{\xi_{k}}-b\right|^{2} \frac{\left|\rho_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}\right|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}} d x\right]
\end{aligned}
$$

where

$$
A_{0}=\frac{\beta^{-1}}{2 \lambda^{2} C_{\pi}^{L S}}>0
$$

With (4.12), to obtain the final estimate, one then needs to obtain an $O\left(\eta^{2}\right)$ estimate



STEP 2: estimate $\mathbb{E}_{\xi_{k}} \mathbb{E}\left[\left|\bar{b}_{t}^{\xi_{k}}\left(\bar{X}_{t}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right]$

In this step, we aim to obtain an $O\left(\eta_{k}^{2}\right)$ bound for $\mathbb{E}_{\xi_{k}} \mathbb{E}\left[\left|\bar{b}_{t}^{\xi_{k}}\left(\bar{X}_{t}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right]$ based on Taylor expansion for $b^{\xi_{k}}$. Note that $\xi_{k}$ is fixed so we may follow the estimate for the Unadjusted Langevin Algorithm (ULA) in [35] in this step.

By Taylor expansion, $\forall t \in\left[T_{k}, T_{k+1}\right)$,

$$
\begin{aligned}
& \bar{b}_{t}^{\xi_{k}}(x)-b^{\xi_{k}}(x)=\mathbb{E}\left[b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right) \mid \bar{X}_{t}=x, \xi_{k}\right] \\
& =\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=x, \xi_{k}\right] \cdot \nabla b^{\xi_{k}}(x) \\
& +\frac{1}{2} \mathbb{E}\left[\left(\bar{X}_{T_{k}}-\bar{X}_{t}\right)^{\otimes 2}: \int_{0}^{1} \nabla^{2} b^{\xi_{k}}\left((1-s) \bar{X}_{t}+s \bar{X}_{T_{k}}\right) d s \mid \bar{X}_{t}=x, \xi_{k}\right] .
\end{aligned}
$$

For simplicity, we denote

$$
\bar{r}_{t}(x):=\frac{1}{2} \mathbb{E}\left[\left(\bar{X}_{T_{k}}-\bar{X}_{t}\right)^{\otimes 2}: \int_{0}^{1} \nabla^{2} b^{\xi_{k}}\left((1-s) \bar{X}_{t}+s \bar{X}_{T_{k}}\right) d s \mid \bar{X}_{t}=x, \xi_{k}\right]
$$

In Lemma A.2, we show that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\mathbb{E}\left[\left|\bar{r}_{t}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq c d\left(t-T_{k}\right)^{2}
$$

where $c$ is a positive constant independent of $k, d$ and $\xi_{k}$. For the first term $\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=\right.$ $\left.x, \xi_{k}\right] \cdot \nabla b^{\xi_{k}}(x)$, by Bayes' law we have

$$
\begin{aligned}
\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}^{\xi}=x, \xi_{k}\right] & =\int(y-x) P\left(\bar{X}_{T_{k}}=y \mid \bar{X}_{t}=x, \xi_{k}\right) d y \\
& =\int(y-x) \frac{\bar{\rho}_{T_{k}}^{\xi_{k}}(y) P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)}{\rho_{t}^{\xi_{k}}(x)} d y
\end{aligned}
$$

Clearly, the distribution $P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)$ is Gaussian, namely,

$$
P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)=\left(4 \pi \beta^{-1}\left(t-T_{k}\right)\right)^{-\frac{d}{2}} \exp \left(-\frac{\left|x-y-b^{\xi_{k}}(y)\left(t-T_{k}\right)\right|^{2}}{4 \beta^{-1}\left(t-T_{k}\right)}\right)
$$

which motivates us to calculate (4.16) via integration by parts. Indeed, we show in Lemma A. 3 that

$$
\int\left|\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=x, \xi_{k}\right]\right|^{2} \bar{\rho}_{t}^{\xi_{k}}(x) d x \leq c \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right), \quad \forall t \in\left[T_{k}, T_{k+1}\right)
$$

where $\mathcal{I}(\rho):=\int \rho|\nabla \log \rho|^{2} d x$ is the Fisher information, and $c$ is a positive constant independent of $k, d$ and $\xi_{k}$. Then, it is left to give an $O(1)$ estimate for each Fisher information $\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)$ in ULA, which has been done in Section 3.2.

STEP 3: estimate $\mathbb{E}_{\xi_{k}, \tilde{\xi_{k}}}\left[\int\left|b^{\xi_{k}}-b\right|^{2} \frac{\left|\hat{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}\right|^{2}}{\bar{\rho}_{t}^{\xi_{k}}} d x\right]$.


Recall that $\bar{\rho}_{t}^{\xi_{k}}$ and $\bar{\rho}_{t}^{\tilde{\xi}_{k}}$ are the densities of the laws of $\bar{X}$ and $\bar{Y}$ with two independent batches $\xi_{k}$ and $\tilde{\xi}_{k}$ for interval $\left[T_{k}, T_{k+1}\right)$. Hence the problem is again reduced to the ULA case.

We first note that

$$
\int \frac{\left|\bar{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{-\xi_{k}}\right|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}} d x=\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\hat{\rho}_{t}^{\tilde{\xi}_{k}}}-1\right|^{2} \bar{\rho}_{t}^{\tilde{\xi}_{k}} d x
$$

and the property of path measures gives

$$
\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}(x)=\mathbb{E}\left[\left.\frac{d P_{\bar{X}}}{d P_{\bar{Y}}} \right\rvert\, \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right]
$$

where $P_{\bar{X}}$ and $P_{\bar{Y}}$ are path measures in $C\left(\left[T_{k}, T_{k+1}\right] ; \mathbb{R}^{d}\right)$. Let

$$
\bar{X}_{T_{k}}=\bar{Y}_{T_{k}}=y \sim \bar{\rho}_{T_{k}}
$$

Then for $t \in\left[T_{k}, T_{k+1}\right)$, Girsanov transform gives:

$$
\frac{d P_{\bar{X}}}{d P_{\bar{Y}}}(\bar{Y})=\exp \left(\sqrt{\frac{\beta}{2}} \int_{T_{k}}^{T_{k+1}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y) d W_{s}-\frac{\beta}{4} \int_{T_{k}}^{T_{k+1}}\left|\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y)\right|^{2} d s\right)
$$

Details for (4.20) and (4.21) can be found in Corollary A. 1 of Appendix A. Denote

$$
\tilde{b}(y):=\frac{1}{\sqrt{2 \beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y)
$$

Then, for $t \in\left[T_{k}, T_{k+1}\right)$, the martingale property gives

$$
\frac{\bar{\rho}_{t}^{-\xi_{k}}}{\bar{\rho}_{t} \tilde{\xi}_{k}}(x)=\mathbb{E}\left[\left.\exp \left(\int_{T_{k}}^{t} \tilde{b}(y) d W_{s}-\frac{1}{2} \int_{T_{k}}^{t}|\tilde{b}(y)|^{2} d s\right) \right\rvert\, \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right]
$$

Hence,

$$
\begin{aligned}
& \int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\tilde{\rho}_{t}^{\tilde{\xi}_{k}}}-1\right|^{2} \bar{\rho}_{t}^{\tilde{\xi}_{k}} d x \\
= & \int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left|\mathbb{E}\left[\left.e^{\int_{T_{k}}^{t} \tilde{b}\left(\bar{Y}_{T_{k}}\right) d W_{s}-\frac{1}{2} \int_{T_{k}}^{t}\left|\tilde{b}\left(\bar{Y}_{T_{k}}\right)\right|^{2} d s} \right\rvert\, \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right]-1\right|^{2} d x \\
= & \int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left|\int\left(e^{\sqrt{\frac{\beta}{2}} \tilde{b}(y)\left(x-y-\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right)-\frac{1}{2}|\tilde{b}(y)|^{2}\left(t-T_{k}\right)}-1\right) P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right|^{2} d x
\end{aligned}
$$

Above we have used the fact that $\bar{Y}_{t}=y+b^{\tilde{\xi}_{k}}(y)\left(t-T_{k}\right)+\sqrt{2 \beta^{-1}}\left(W_{t}-W_{T_{k}}\right)$, resulting in that

$$
\sqrt{2 \beta^{-1}}\left(W_{t}-W_{T_{k}}\right)=x-y-b^{\tilde{\xi}_{k}}(y)\left(t-T_{k}\right)
$$

Now in order to handle the integration of the term $e^{\sqrt{\frac{\bar{B}}{2} \tilde{b}}(y)\left(x-y-\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right)-\frac{1}{2}|\tilde{b}(y)|^{2}\left(t-T_{k}\right)}$, we split it by

$$
\begin{aligned}
& e^{\sqrt{\frac{\beta}{2}} \tilde{b}(y)\left(x-y-\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right)-\left.\frac{1}{2} \tilde{b}(y)\right|^{2}\left(t-T_{k}\right)}-1 \\
= & \sqrt{\frac{\beta}{2}} \tilde{b}(y)(x-y)+\left(-\sqrt{\frac{\beta}{2}} \tilde{b}(y) b^{\tilde{\xi}_{k}}(y)-\frac{1}{2}|\tilde{b}(y)|^{2}\right)\left(t-T_{k}\right)+\left(e^{z}-z-1\right) \\
:= & K_{1}+K_{2}+K_{3},
\end{aligned}
$$

where

$$
z:=\sqrt{\frac{\beta}{2}} \tilde{b}(y)\left(x-y-\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right)-\frac{1}{2}|\tilde{b}(y)|^{2}\left(t-T_{k}\right)
$$

Then

$$
\int\left|\frac{\bar{\rho}_{t}^{-\xi_{k}}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}-1\right|^{2} \bar{\rho}_{t}^{\tilde{\xi}_{k}} d x=\int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left|\int\left(K_{1}+K_{2}+K_{3}\right) P\left(\bar{X}_{T_{k}}=y \mid \overline{\bar{y}}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right|^{2} d x
$$

For $K_{1}=\sqrt{\frac{\beta}{2}} \tilde{b}(y)(x-y)$, using integration by parts again, we prove in Lemma A. 4 in Section A that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int \tilde{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{1} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right)
$$

where $c$ is a positive constant independent of $k, d, \tilde{\xi}_{k}$ and $\xi_{k}$.

For $\left.K_{2}=\left(-\sqrt{\frac{\beta}{2}} \tilde{b}(y) \cdot b^{\tilde{\xi}_{k}}(y)\right)-\left.\frac{1}{2} \tilde{b}(y)\right|^{2}\right)\left(t-T_{k}\right)$, using the boundedness and Lipshitz condition in Assumption 3.1, we prove in Lemma A. 5 that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c d \eta_{k}^{2}
$$

where $c$ is a positive constant independent of $k, d, \tilde{\xi}_{k}$ and $\xi_{k}$.

For the remaining term $K_{3}$, after applying Jensen's inequality and the tower property of conditional expectation, we prove in Lemma A. 6 that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int \rho_{\rho_{t}}^{\tilde{\xi}_{k}}(x)\left(\int K_{3} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c d \eta_{k}^{2}
$$

where $c$ is a positive constant independent of $k, d, \tilde{\xi}_{k}$ and $\xi_{k}$.

Equipped with the estimation for the integration of $K_{1}, K_{2}$, and $K_{3}$, one finally obtains

$$
\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\hat{\rho}_{t}^{\tilde{\xi}_{k}}}-1\right|^{2} \bar{\rho}_{t}^{\tilde{\rho}_{k}} d x \leq c \eta_{k}^{2}\left(1+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right), \quad \forall t \in\left[T_{k}, T_{k+1}\right)
$$

where $c$ is a positive constant independent of $k, d, \tilde{\xi}_{k}$ and $\xi_{k}$. Combining with the estimate for Fisher information obtained in Section 3.2, one is able to get an $\eta_{k}^{2}$ estimation for the term $\mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}}\left[\int\left|b^{\xi_{k}}-b\right|^{2} \frac{|| \hat{\rho}_{t}^{\tilde{\xi}_{k}}-\left.\bar{\rho}_{k}^{\xi_{k}}\right|^{2}}{\bar{\rho}_{t}^{\xi_{k}}} d x\right]$. Note that after taking the expectation $\mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}}[\cdot]$, the bound is still of order $\eta_{k}^{2}$, since the bounds above are all independent of the batches $\xi_{k}, \tilde{\xi}_{k}$.

Combining the results in STEP 2 and STEP 3 finally leads to the desired result:

$$
\frac{d}{d t} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) \leq-A_{0} D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right)+A_{1} d \eta_{k}^{2}\left(1+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right), \quad \forall t \in\left[T_{k}, T_{k+1}\right)
$$

where $A_{0}, A_{1}$ are positive constants independent of $k, d$, and $\xi_{k}$.

## 5 Discussion

### 5.1 Convergence to equilibrium and target distribution

## - Convergence to the target distribution

Viewing SGLD as a popular sampling algorithm, many researchers would care about the convergence rate to the target distribution. An important extension of Theorem 3.2 or Corollary 3.1 is about the distance between the SGLD iteration and the target distribution, namely, the invariant distribution of the Langevin diffusion (1.3). When we are doing sampling tasks, this result is an important measure for the efficiency of a sampling algorithm. Note that the rate in our result can be viewed as a great improvement compared with former work like $[36,53,16]$, where the optimal bound so far is of order $O(\sqrt{\eta})$ in terms of Wasserstein distance or total variation. Meanwhile, as will be derived in the followings, we obtain a bound of order $O(\eta)$.

To compare our result with former ones more directly, we consider the constant step size (or learning rate) $\eta$. We consider the Wasserstein-2 $\left(W_{2}\right)$ distance, the Wasserstein$1\left(W_{1}\right)$ distance, and the total variation (TV) distance in the following discussion. Firstly let us recall the definition of $W_{p}$ distance ( $p=1,2$ here) and TV distance between two distributions $\mu$ and $\nu[45]$ :

$$
W_{p}(\mu, \nu):=\left(\inf _{\gamma \in \Pi(\mu, v)} \int_{\mathbb{R}^{d} \times \mathbb{R}^{d}}|x-y|^{p} d \gamma\right)^{1 / p}
$$

and

$$
D_{T V}(\mu, \nu):=\sup _{A \in \mathcal{B}\left(\mathbb{R}^{d}\right)}|\mu(A)-\nu(A)|
$$

Here, $\Pi(\mu, \nu)$ means all joint distributions whose marginal distributions are $\mu$ and $\nu$, respectively,

Now, by Corollary 3.1, we have

$$
D_{K L}\left(\bar{\rho}_{t} \| \rho_{t}\right) \leq c d \eta^{2}, \quad t>0
$$

where $c$ is independent of $t$, and $\eta$ is the constant step size (or learning rate).

Also, since the invariant distribution $\pi$ satisfies a Log-Sobolev inequality by Assumption 3.2, we have the following exponential convergence for the Langevin diffusion (1.3), which is a classical result [34]:

$$
D_{K L}\left(\rho_{t} \| \pi\right) \leq e^{-\gamma t} D_{K L}\left(\rho_{0} \| \pi\right)
$$

It is well-known that we can bound the $W_{2}, W_{1}$, and TV distance with square root of the KL-divergence by Talagrand transportation inequality [39, 48], the weighted Csiszar-Kullback-Pinsker inequality [6], and the Pinsker's inequality [42], respectively. Note that for $W_{2}$ distance and TV distance, the constant $c_{1}^{\prime}$ above is dimension-free; for $W_{1}$ distance, the constant $c_{1}^{\prime}$ above is of $O\left(d^{\frac{1}{2}}\right)$. Together with the triangle inequality for $W_{2}, W_{1}$, and TV distances, one has the following:

Corollary 5.1. Consider the probability density functions $\rho_{t}$, $\bar{\rho}_{t}$ for $X_{t}, \bar{X}_{t}$ defined in (1.3), (1.7). Suppose Assumption 3.1, 3.2 hold. Then the following holds:

(a) If $\eta_{k}=\eta, \forall k$, then there exist positive constants $c_{1}^{W_{1}}, c_{2}^{W_{1}}, c_{1}^{W_{2}}, c_{2}^{W_{2}}, c_{1}^{T V}, c_{2}^{T V}$, $\gamma, \Delta_{0}$ independent of $t$ and $d$ such that for all $\eta \in\left(0, \Delta_{0}\right)$,

$* W_{1}\left(\bar{\rho}_{t}, \pi\right) \leq c_{1}^{W_{1}} d \eta+c_{2}^{W_{1}} d^{\frac{1}{2}} e^{-\frac{1}{2} \gamma t}$

* $W_{2}\left(\bar{\rho}_{t}, \pi\right) \leq c_{1}^{W_{2}} d^{\frac{1}{2}} \eta+c_{2}^{W_{2}} e^{-\frac{1}{2} \gamma t}$,
* $D_{T V}\left(\bar{\rho}_{t}, \pi\right) \leq c_{1}^{T V} d^{\frac{1}{2}} \eta+c_{2}^{T V} e^{-\frac{1}{2} \gamma t}$.

(b) If $\eta_{i}=(\ell+i)^{-\theta}$, with $\theta \in(0,1)$ being the decay rate, then there exist positive constants $c^{W_{1}}, c^{W_{2}}, c^{T V}$ independent of $k$ and $d$ such that

* $W_{1}\left(\bar{\rho}_{T_{k}}, \pi\right) \leq c^{W_{1}} d\left(\frac{1}{k}\right)^{\theta}$,
* $W_{2}\left(\bar{\rho}_{T_{k}}, \pi\right) \leq c^{W_{2}} d^{\frac{1}{2}}\left(\frac{1}{k}\right)^{\theta}$,

$* D_{T V}\left(\bar{\rho}_{T_{k}}, \pi\right) \leq c^{T V} d^{\frac{1}{2}}\left(\frac{1}{k}\right)^{\theta}$.

By Corollary 5.1, we can conclude the steps of simulations for SGLD needed to achieve a tolerance $\epsilon$ under different distances.

Corollary 5.2. Under Assumption 3.1, 3.2, to achieve an error smaller than $\epsilon$, one needs the following numbers of simulations of SGLD respectively under the corresponding distances:

- $N=O\left(d \epsilon^{-1}\left(\log \epsilon^{-1}+\log d^{\frac{1}{2}}\right)\right)$ for $W_{1}$ distance (by setting $\eta=O\left(d^{-1} \epsilon\right)$ );

$-N=O\left(d^{\frac{1}{2}} \epsilon^{-1} \log \epsilon^{-1}\right)$ for $W_{2}$ distance (by setting $\eta=O\left(d^{-\frac{1}{2}} \epsilon\right)$ );

$-N=O\left(d^{\frac{1}{2}} \epsilon^{-1} \log \epsilon^{-1}\right)$ for $T V$ distance (by setting $\eta=O\left(d^{-1} \epsilon\right)$ ).

These results are improved compared to existing results in literature.

## - Ergodicity of SGLD

An important property of SGLD that remains to be studied is its ergodicity, which then ensures the existence of the invariant distribution of the SGLD dynamic and enables us to explore the convergence of the algorithm itself. In [7], the authors considered the ergodicity of SGLD under $W_{2}$ distance with the assumptions of global strong convexity of $U$ and 4 -th order Lipshitz condition.

In our setup, we do not have the global strong convexity of $U$ and only have second order Lipschitz condition. Luckily, the ergodicity could be studied using reflection coupling $[14,24]$, under mild assumptions. In particular, we have the following claim. In fact, we need to assume the followings, which can be understood as the positive upper and lower bound of $\nabla^{2} U$ outside the circle $B(0, R)$ in $\mathbb{R}^{d}$.

Assumption 5.1. There exist $R_{0}>0, \kappa_{0}>0, K>0$ such that the followings hold:

(a) (locally nonconvex) The Hessian matrix of $U$ is uniformly positive definite outside $B\left(0, R_{0}\right)$, namely

$$
\nabla^{2} U(x) \succeq \kappa_{0} I_{d}, \quad \forall x \in \mathbb{R}^{d} \backslash B\left(0, R_{0}\right)
$$

(b) (global uniform-in-batch Lipshitz) $\forall x, y \in \mathbb{R}^{d}, \forall \xi$,

$$
\left|\nabla U^{\xi}(x)-\nabla U^{\xi}(y)\right| \leq K|x-y|^{2}
$$

Then the following claim holds.

Proposition 5.1. Suppose Assumption 5.1 holds. Denote $\Delta_{0}:=\sup _{k} \eta_{k}$. There exist positive constants $\bar{\Delta}, c_{0}, c_{1}$ such that if $\Delta_{0}<\bar{\Delta}$, then for any two initial distributions $\mu_{0}$ and $\nu_{0}$, denoting $\bar{\mu}_{t}$ and $\bar{\nu}_{t}$ to be the corresponding time marginal distributions for the time continuous interpolation of SGLD algorithm (1.7), it holds that

$$
W_{1}\left(\bar{\mu}_{T_{k}}, \bar{\nu}_{T_{k}}\right) \leq c_{0} e^{-c_{1} T_{k}} W_{1}\left(\mu_{0}, \nu_{0}\right)
$$

Consequently, if the step size (or learning rate) is constant $\eta_{k} \equiv \eta$ such that the discrete chain is time-homogeneous, then the SGLD as a discrete time Markov chain has an invariant measure $\tilde{\pi}$ by the Banach contraction mapping theorem. Then, we have the following conclusion

Corollary 5.3. Let $\eta_{k} \equiv \eta$. Under Assumption 5.1, there exist positive constants $\bar{\Delta}$, $c_{0}, c_{1}$ such that if $\eta \leq \bar{\Delta}$, then for any initial distribution $\rho_{0}$ with finite first moment, the SGLD iteration has an invariant measure $\tilde{\pi}$ time marginal distribution $\bar{\rho}_{t}$ of (1.7) convergences exponentially to $\tilde{\pi}$ in terms of $W$ - 1 distance:

$$
W_{1}\left(\bar{\rho}_{n \eta}, \tilde{\pi}\right) \leq c_{0} e^{-c n \eta} W_{1}\left(\rho_{0}, \tilde{\pi}\right)
$$

Equipped with the ergodicity results for SGLD and combining the results in Corollary 5.1, we are able to estimate the distance between the target distribution and the invariant distribution of SGLD itself:

$$
W_{1}(\tilde{\pi}, \pi) \leq c \eta
$$

This is improved compared to existing results in literature. Detailed derivation can be found in $[1]$.

### 5.2 Other discussions

## - Justification of sharpness

A natural question for our results is: is this bound we obtained really a "sharp" one? To answer this question, we simply consider the following Ornstein-Uhlenbeck (O-U) process in $\mathbb{R}^{1}$, which satisfies all our assumptions.

$$
d X=-X d t+d W
$$

Its solution has an explicit expression:

$$
X_{t}=e^{-t} X_{0}+\int_{0}^{t} e^{s-t} d W_{s}
$$

Consider the full-batch SGLD, namely, the Euler-Maruyama scheme for (5.10) with constant step size $\eta$ :

$$
\hat{X}_{T_{k+1}}=\hat{X}_{T_{k}}-\eta \hat{X}_{T_{k}}+\left(W_{T_{k+1}}-W_{T_{k}}\right)
$$

Suppose $X_{t}, \hat{X}_{t}$ are Gaussion, and $\mathbb{E}\left[X_{0}\right] \neq 0$, then we are able to calculate the KLdivergence without much difficulty. Indeed, by definition, at $T:=k \eta$, their mean and variance are given by

$$
\begin{gathered}
\mu_{1}:=\mathbb{E}\left[X_{T}\right]=e^{-T} \mathbb{E}\left[X_{0}\right] \\
\sigma_{1}^{2}:=\operatorname{Var}\left(X_{T}\right)=e^{-2 T} \operatorname{Var}\left(X_{0}\right)+\frac{1}{2}\left(1-e^{-2 T}\right)
\end{gathered}
$$

and

$$
\begin{gathered}
\mu_{2}:=\mathbb{E}\left[\hat{X}_{T}\right]=(1-\eta)^{(T / \eta)} \mathbb{E}\left[X_{0}\right] \\
\sigma_{2}^{2}:=\operatorname{Var}\left(\hat{X}_{T}\right)=(1-\eta)^{2(T / \eta)} \operatorname{Var}\left(X_{0}\right)+\frac{1}{2-\eta}\left(1-(1-\eta)^{2(T / \eta)}\right)
\end{gathered}
$$

Clearly, for small $\eta$,

$$
\begin{aligned}
\left|\mu_{1}-\mu_{2}\right| & =\left|\mathbb{E}\left[X_{0}\right]\right|\left(e^{-T}-(1-\eta)^{(T / \eta)}\right) \geq\left|\mathbb{E}\left[X_{0}\right]\right|\left(e^{-t}-e^{-t-t \eta / 2}\right) \\
& >\left|\mathbb{E}\left[X_{0}\right]\right| e^{-T}\left(\frac{1}{2} \eta T-\frac{1}{8} \eta^{2} T^{2}\right)>\frac{1}{4}\left|\mathbb{E}\left[X_{0}\right]\right| e^{-T} T \eta
\end{aligned}
$$

and $\sigma_{2}^{2}<2 \sigma_{1}^{2}$.

Also by direct calculation, the KL-divergence between two Gaussian distributions $N\left(\mu_{1}, \sigma_{1}^{2}\right), N\left(\mu_{2}, \sigma_{2}^{2}\right)$ is given by

$$
\begin{aligned}
D_{K L}\left(N\left(\mu_{1}, \sigma_{1}^{2}\right) \| N\left(\mu_{2}, \sigma_{2}^{2}\right)\right) & =\left(\frac{1}{2} \log \frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}+\frac{1}{2}\left(\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}-1\right)\right)+\frac{\left(\mu_{1}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}} \\
& \geq 0+\frac{\left(\mu_{1}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}
\end{aligned}
$$

Therefore,

$$
D_{K L}\left(\bar{\rho}_{T} \| \rho_{T}\right) \geq \frac{(1 / 16)\left|\mathbb{E}\left[X_{0}\right]\right|^{2} e^{-2 T} T^{2}}{4 \sigma_{1}(T)^{2}} \eta^{2}
$$

This then indicates that our $\eta^{2}$ bound is a sharp one.

## - The role of consistency of random batch technique

As a variant of ULA, the key difference of SGLD is the introduction of the minibatch technique, which reduces the computational cost. To understand the error and mechanism for the sharp error estimate, let us take $\eta_{k} \equiv \eta$.

For each single step, the error of the drift is $O(1)$. The methods involving random batches (such as the SGD and the random batch methods) have a strong error like (see for example $[22]$ )

$$
\sqrt{\mathbb{E}\|X-\bar{X}\|^{2}} \sim \sqrt{\left(e^{k \eta}-1\right) \eta} .
$$

Clearly, the strong error decays like $\sqrt{\eta}$, which is actually sharp. As mentioned in [22], the averaging effect in time ensures a convergence like "law of large numbers" in time so the convergence rate is $\sqrt{\eta}$. The strong error estimate can imply that

$$
\left(\mathbb{E}_{\xi} W_{2}^{2}\left(\rho_{t}^{\xi}, \rho_{t}\right)\right)^{1 / 2} \sim \sqrt{\left(e^{k \eta}-1\right) \eta}
$$

This indicates that the fluctuation of the trajectory and $\rho_{t}^{\boldsymbol{\xi}}$ is really like $\sqrt{\eta}$. Hence, the existing error estimates of SGLD based on the trajectory estimates can achieve $\sqrt{\eta}$ at most. Moreover, such an estimate based on trajectory estimate can only give an $O(\eta)$ one step error of the SGLD under Wasserstein distance (the $O(\sqrt{\eta})$ global error is due to the time averaging over multiple intervals).

The most important property of the random batch is its consistency:

$$
\mathbb{E}_{\xi}\left[b^{\xi}(x)\right]=b(x)
$$

which can be interpreted as an unbiased approximation of the original drift function, as has been mentioned in (1.1). Consider one step. Starting from a common $\rho_{0}$, after one step, formally each $\rho_{\eta}^{\xi}$ has the following expression

$$
\rho_{\eta}=\rho_{0}+\eta \mathcal{L}_{\xi}^{*} \rho_{0}+O\left(\eta^{2}\right)
$$

where $\mathcal{L}_{\xi}$ is the generator corresponding to batch $\xi$, while

$$
\rho_{\eta}=\rho_{0}+\eta \mathcal{L}^{*} \rho_{0}+O\left(\eta^{2}\right)
$$

Hence, the error is like $O(\eta)$. Since the error of the drift can cancel if one takes average across batches and thus one is motivated to take the average of all possible $\rho_{t}^{\xi}$ :

$$
\bar{\rho}_{t}=\mathbb{E}_{\xi}\left[\rho_{t}^{\xi}\right]
$$

which is the true law of the SGLD. The obtained $\bar{\rho}_{t}$ is then expected to have $O\left(\eta^{2}\right)$ local error compared to $\rho_{t_{n+1}}$. Of course, direct proof using Wasserstein distances has some difficulty and we make use of the KL divergence to accomplish the proof motivated by the recent work [35]. Anyway, this intuition lays the foundation of our proof and is reflected in treating the terms in (4.5). In fact, the last term in (4.5), or $b^{\xi_{k}} \bar{\rho}_{t}^{\xi_{k}}-b \bar{\rho}_{t}$, can be as $O(1)$. The intuition is that the averaged drift should be $b$ and one may cancel the error: $\mathbb{E}\left(b^{\xi_{k}}\right) \rho_{t}^{\xi_{k}}-b \bar{\rho}_{t}$ is small and one may have convergence. With this intuition, we rearrange

$$
b^{\xi_{k}} \bar{\rho}_{t}^{\xi_{k}}-b \bar{\rho}_{t}=\mathbb{E}\left(b^{\xi_{k}}-b\right)\left(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}\right)
$$

in $(4.6)$.

At last, we remark that though $\bar{\rho}_{t}$ is close to $\rho_{t}$, in practice we do not repeat the experiment for many times and take the average. Instead, we only generate a sequence of the batches $\left(\xi^{0}, \cdots, \xi^{k}, \cdots\right)$ and generate the samples. Even though we use a single $b^{\xi_{k}}$ each step, the empirical distribution by the generated samples converges weakly to the invariant measure with error $O(\eta)$ under Wasserstein distance to the interested distribution, due to the ergodicity of SGLD. Hence, one does not have to run SGLD for many experiments to approximate $\bar{\rho}_{t}$ and further to approximate the invariant distribution with error $O(\eta)$.

## - Dependence on the dimensionality

The linear scaling with respect to $d$ arising in (3.17) and (3.19) is quite natural for the entropy and Fisher information. In fact, if one considers cases where the dynamics in difference dimensions are decouple so that $\rho_{t}(x)=\prod_{i=1}^{d} \rho_{t}^{(i)}\left(x_{i}\right)$, the dependence on dimension in the entropy and Fisher information would be linear.

As we have mentioned, the linear dependence in the our error bounds largely comes from with the factor $d^{-1 / 2}$ in the Lipschitz constant in Assumption 3.1, and we have justified this below Assumption 3.1. A slight discrepancy of this intuition comes from $D_{K L}\left(\rho_{0} \| \pi\right)$, which by by condition (a) in Assumption 3.2 satisfies

$$
D_{K L}\left(\rho_{0} \| \pi\right) \leq \log \lambda
$$

This independence of the dimension is a consequence of the strong assumption Assumption 3.2. However, if we use a weaker assumption like $\rho_{0} / \pi \leq \lambda^{d}$, there would be dimension dependence in the constant for log-Sobolev inequality of the Hooley-Stroock perturbation lemma. This may indicate that the Hooley-Stroock perturbation lemma is not sharp regarding the scalability in $d$.

## 6 Acknowledgement

This work is financially supported by the National Key R\&D Program of China, Project Number 2021YFA1002800 and Project Number 2020YFA0712000. The work of L. Li was partially supported by NSFC 11901389 and 12031013, Shanghai Municipal Science and Technology Major Project 2021SHZDZX0102, Shanghai Science and Technology Commission Grant No. 21JC1402900, and Shanghai Sailing Program 19YF1421300.

## A Omitted details in Section 3 and 4

In this section, we prove the details omitted in Section 3 and 4. Lemma A.2, A. 3 have been proved in $[35]$.

## A. 1 Proof of Proposition 3.1

The method for bounding the $p$-th moment of fixed-batch SGLD is based on direct Itô calculation and basic inequalities. In the followings, we denote $\mathcal{F}_{\xi}$ the $\sigma$-algebra generated by $\xi_{k}$ for all $k \in \mathbb{N}$.

Proof of Proposition 3.1: By definition, for fixed batch sequence $\boldsymbol{\xi}$,

$$
d \bar{X}_{t}=b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right) d t+\sqrt{2 \beta^{-1}} d W, \quad t \in\left[T_{k}, T_{k+1}\right)
$$

where we recall $T_{k}=\sum_{i=0}^{k-1} \eta_{i}$. For $p \geq 2$, by Itô's formula, we have

$$
\begin{aligned}
& d\left|\bar{X}_{t}\right|^{p}=p\left|\bar{X}_{t}\right|^{p-2} \bar{X}_{t} \cdot\left(b^{\xi}\left(\bar{X}_{T_{k}}\right) d t+\sqrt{2 \beta^{-1}} d W\right) \\
& \quad+\beta^{-1} p\left|\bar{X}_{t}\right|^{p-2}\left(I_{d}+(p-2) \frac{\bar{X}_{t} \otimes \bar{X}_{t}}{\left|\bar{X}_{t}\right|^{2}}\right): I_{d} d t
\end{aligned}
$$

So

$$
\begin{aligned}
& \frac{d}{d t} \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right] \leq p \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \bar{X}_{t} \cdot b^{\xi_{k}}\left(\bar{X}_{t}\right) \mid \mathcal{F}_{\xi}\right] \\
& \quad+p \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \bar{X}_{t} \cdot\left(b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right)\right) \mid \mathcal{F}_{\xi}\right]+\beta^{-1} p(p-1) d \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \mid \mathcal{F}_{\xi}\right]
\end{aligned}
$$

Using the dissipation condition in Assumption 3.1, we can control the first term above, namely,

$$
p \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \bar{X}_{t} \cdot b^{\xi_{k}}\left(\bar{X}_{t}\right) \mid \mathcal{F}_{\xi}\right] \lesssim-p \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right]+p \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \mid \mathcal{F}_{\xi}\right]
$$

By Young's inequality, for any $\delta>0$,

$$
\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \mid \mathcal{F}_{\xi}\right] \leq \delta d^{-1} \frac{p-2}{p} \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right]+\delta^{-\frac{p-2}{2}} d^{\frac{p-2}{2}} \frac{2}{p}
$$

For the second term, direct estimate gives

$$
\begin{aligned}
& \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \bar{X}_{t} \cdot\left(b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right)\right) \mid \mathcal{F}_{\xi}\right] \leq c \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-1}\left|\bar{X}_{t}-\bar{X}_{T_{k}}\right| \mid \mathcal{F}_{\xi}\right] \\
& \lesssim\left(t-T_{k}\right) \mathbb{E}\left[\left|b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)\right|\left|\bar{X}_{t}\right|^{p-1} \mid \mathcal{F}_{\xi}\right]+\sqrt{2 \beta^{-1}} \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-1}\left|\mathcal{N}\left(0, t-T_{k}\right)\right| \mid \mathcal{F}_{\xi}\right]
\end{aligned}
$$

Note that $b(\cdot)$ grows linearly only. Then, by Young's inequality, together with the fact that $t-T_{k} \leq \eta_{k}$, one has

$$
\begin{aligned}
& \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2} \bar{X}_{t} \cdot\left(b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right)\right) \mid \mathcal{F}_{\xi}\right] \\
& \lesssim\left(\eta_{k}^{p /(2(p-1))}+\eta_{k}\right) \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right]+\eta_{k} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p} \mid \mathcal{F}_{\xi}\right]+d^{\frac{p}{2}}
\end{aligned}
$$

Hence,

$$
\frac{d}{d t} \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right] \leq-c_{1} \mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right]+c_{3} \eta_{k} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p} \mid \mathcal{F}_{\xi}\right]+c_{2} d^{\frac{p}{2}}, \quad t \in\left[T_{k}, T_{k+1}\right)
$$

Here, $c_{1}, c_{2}, c_{3}$ are positive constants independent of $t, d$ and $\boldsymbol{\xi}$ but possibly dependent of $p$.

We claim that since there exists $c_{1}^{\prime}>0$ such that

$$
-c_{1}+c_{3} \eta_{k} \leq-c_{1}^{\prime}, \quad \forall k
$$

the moment is uniformly bounded.

In fact, applying the Grönwall inequality,

$$
\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right] \leq e^{-c_{1}\left(t-T_{k}\right)} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p} \mid \mathcal{F}_{\xi}\right]+\int_{T_{k}}^{t} e^{-c_{1}(t-s)}\left(c_{3} \eta_{k} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p} \mid \mathcal{F}_{\xi}\right]+c_{2} d^{\frac{p}{2}}\right) d s
$$

Defining

$$
u^{\boldsymbol{\xi}}(t):=\sup _{0 \leq s \leq t} \mathbb{E}\left[\left|\bar{X}_{s}\right|^{p} \mid \mathcal{F}_{\xi}\right]
$$

one thus finds

$$
u^{\boldsymbol{\xi}}(t) \leq e^{-c_{1}\left(t-T_{k}\right)} u^{\boldsymbol{\xi}}\left(T_{k}\right)+\int_{T_{k}}^{t} e^{-c_{1}(t-s)}\left[c_{3} \eta_{k} u^{\boldsymbol{\xi}}(s)+c_{2} d^{\frac{p}{2}}\right] d s
$$

Then, it is not hard to find that $u^{\boldsymbol{\xi}}(t) \leq v^{\boldsymbol{\xi}}(t)$ where

$$
\frac{d}{d t} v^{\boldsymbol{\xi}}(t)=-c_{1}^{\prime} v^{\xi}(t)+c_{2} d^{\frac{p}{2}}, \quad t \in\left[T_{k}, T_{k+1}\right), v^{\xi}\left(T_{k}\right) \geq u^{\boldsymbol{\xi}}\left(T_{k}\right)
$$

Remark A.1. One may use an intermediate function satisfying the following to justify the above comparison principle:

$$
\frac{d}{d t} \tilde{v}^{\xi}(t)=-c_{1} \tilde{v}^{\xi}(t)+c_{3} \eta_{k} \tilde{v}^{\xi}(t)+c_{2} d^{\frac{p}{2}}
$$

Since (A.3) holds for each time interval and the moment is continuous in time so one can concatenate them and conclude by induction that $u^{\boldsymbol{\xi}}(t) \leq v^{\boldsymbol{\xi}}(t)$ with

$$
\frac{d}{d t} v^{\boldsymbol{\xi}}(t)=-c_{1}^{\prime} v^{\boldsymbol{\xi}}(t)+c_{2} d^{\frac{p}{2}}, \quad v(0)=u(0)=\mathbb{E}\left|\bar{X}_{0}\right|^{p}
$$

Hence,

$$
\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p} \mid \mathcal{F}_{\xi}\right] \leq c_{p} d^{\frac{p}{2}}, \quad \forall t>0
$$

where $c_{p}$ is a positive constant independent of $t, d$ and $\boldsymbol{\xi}$ but possibly dependent of $p$.

For the exponential moment $\mathbb{E}\left[e^{\alpha|X|^{p}}\right]$ with small $\alpha$, after similar Itô's calculation, we are able to obtain

$$
\sup _{t>0} \mathbb{E}\left[e^{\alpha\left|\bar{X}_{t}\right|^{p}} \mid \mathcal{F}_{\xi}\right]<+\infty
$$

This then ends the proof.

## A. 2 Proof of Lemma 3.2

Proof of Lemma 3.2: We first claim the followings:

- There exist positive constants $c_{0}, c_{1}$ independent of the time $t$ such that

$$
\frac{d}{d t} D_{K L}\left(\rho_{t}^{\xi} \| \pi\right) \leq-c_{0} \mathcal{I}\left(\rho_{t}^{\xi}\right)+c_{1} d
$$

- There is a positive constant $c_{2}$ independent of the time $t\left(c_{2}\right.$ is dependent on $D_{K L}\left(\rho_{0} \| \pi\right)$, which is a dimension-free positive constant due to Assumption 3.2) such that

$$
D_{K L}\left(\rho_{t}^{\xi} \| \pi\right) \leq c_{2} d
$$

Indeed, for the first claim (A.6), using Fokker-Planck equation (2.7) for $\rho_{t}^{\xi}$, we can directly calculate the following:

$$
\begin{aligned}
\frac{d}{d t} D_{K L}\left(\rho_{t}^{\boldsymbol{\xi}} \| \pi\right) & =\int\left(1+\log \frac{\rho_{t}^{\boldsymbol{\xi}}}{\pi}\right) \partial_{t} \rho_{t}^{\xi} d x \\
& =\int\left(\nabla \log \rho_{t}^{\boldsymbol{\xi}}-\beta b\right) \cdot\left(\rho_{t}^{\xi} \hat{b}_{t}-\beta^{-1} \nabla \rho_{t}^{\boldsymbol{\xi}}\right) d x
\end{aligned}
$$

where we recall $b=-\nabla U=\beta \nabla \log \pi$. By Young's inequality, we have

$$
\begin{aligned}
\frac{d}{d t} D_{K L}\left(\rho_{t}^{\boldsymbol{\xi}}|| \pi\right) \leq & \left(\frac{\beta^{-1}}{4} \int\left|\nabla \log \rho_{t}^{\boldsymbol{\xi}}\right|^{2} \rho_{t}^{\boldsymbol{\xi}} d x+\beta \int\left|\hat{b}_{t}\right|^{2} \rho_{t}^{\boldsymbol{\xi}} d x\right)-\beta^{-1} \int\left|\nabla \log \rho_{t}^{\boldsymbol{\xi}}\right|^{2} \rho_{t}^{\boldsymbol{\xi}} d x \\
& +\frac{\beta}{2} \int\left(|b|^{2}+\left|\hat{b}_{t}\right|^{2}\right) \rho_{t}^{\boldsymbol{\xi}} d x+\left(\beta \int|b|^{2} \rho_{t}^{\boldsymbol{\xi}} d x+\frac{\beta^{-1}}{4} \int\left|\nabla \log \rho_{t}^{\xi}\right|^{2} \rho_{t}^{\xi} d x\right) \\
= & -\frac{1}{2} \beta^{-1} \mathcal{I}\left(\rho_{t}^{\xi}\right)+\frac{3 \beta}{2}\left(\mathbb{E}\left[\left|\hat{b}_{t}\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right]+\mathbb{E}\left[\left|b\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right]\right)
\end{aligned}
$$

Using the Lipshitz assumption, the result for moment control Proposition 3.1, and Jensen's inequality, since $\eta_{k} \leq \Delta_{0}$, we know that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\begin{aligned}
\mathbb{E}\left[\left|\bar{b}_{t}\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right] & =\int \rho_{t}^{\xi}(x)\left(\mathbb{E}\left[b\left(\bar{X}_{T_{k}}\right) \mid \bar{X}_{t}=x, \mathcal{F}_{\xi}\right]\right)^{2} d x \\
& \leq \mathbb{E}\left[\left|b\left(\bar{X}_{T_{k}}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right] \leq \mathbb{E}\left[\left(|b(0)|+\left|\bar{X}_{T_{k}}\right|\right)^{2} \mid \mathcal{F}_{\xi}\right] \leq \tilde{c}_{1} d
\end{aligned}
$$

where $c_{1}$ is a time-independent positive constant according to Proposition 3.1. Hence by (A.8) and (A.9), the first claim (A.6) holds with $c_{0}=\frac{1}{2} \beta^{-1}$ and $c_{1}=3 \beta \tilde{c}_{1}$

For the second claim (A.7), we first observe that, we can control the negative Fisher information $-\mathcal{I}\left(\bar{\rho}_{t}^{\boldsymbol{\xi}}\right)$ by the negative relative information $-\mathcal{I}\left(\rho_{t}^{\xi} \mid \pi\right):=-\int\left|\nabla \log \frac{\rho_{t}^{\xi}}{\pi}\right|^{2} \rho_{t}^{\xi} d x$ via Young's inequality, namely,

$$
\mathcal{I}\left(\rho_{t}^{\boldsymbol{\xi}} \mid \pi\right)=\int\left|\nabla \log \frac{\rho_{t}^{\xi}}{\pi}\right|^{2} \rho_{t}^{\xi} d x \leq 2 \mathcal{I}\left(\rho_{t}^{\xi}\right)+2 \beta^{2} \mathbb{E}\left[\left|b\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right]
$$

So we have

$$
-\mathcal{I}\left(\rho_{t}^{\xi}\right) \leq-\frac{1}{2} \mathcal{I}\left(\rho_{t}^{\xi} \mid \pi\right)+\beta^{2} \mathbb{E}\left[\left|b\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right]
$$

Then, combining (A.8), (A.9) and (A.11), we have

$$
\begin{aligned}
\frac{d}{d t} D_{K L}\left(\rho_{t}^{\boldsymbol{\xi}} \| \pi\right) & \leq-\frac{1}{4} \beta^{-1} \mathcal{I}\left(\rho_{t}^{\xi} \mid \pi\right)+2 \beta \mathbb{E}\left[\left|b\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right]+\frac{3 \beta}{2} \mathbb{E}\left[\left|\hat{b}_{t}\left(\bar{X}_{t}\right)\right|^{2} \mid \mathcal{F}_{\xi}\right] \\
& \leq-\frac{1}{4} \beta^{-1} \mathcal{I}\left(\rho_{t}^{\boldsymbol{\xi}} \mid \pi\right)+c_{1}^{\prime} d
\end{aligned}
$$

where $c_{1}^{\prime}$ is a positive constant. Since $\pi$ satisfies a Log-Sobolev inequality with constant $C_{\pi}^{L S}$, we have

$$
\frac{d}{d t} D_{K L}\left(\rho_{t}^{\xi} \| \pi\right) \leq-\frac{1}{4 \beta C_{\pi}^{L S}} D_{K L}\left(\rho_{t}^{\xi} \| \pi\right)+c_{1}^{\prime} d
$$

By Grönwall's inequality, we have

$$
\begin{aligned}
D_{K L}\left(\rho_{t}^{\xi} \| \pi\right) & \leq e^{-\rho t} D_{K L}\left(\rho_{0} \| \pi\right)+c_{1}^{\prime} \rho^{-1}\left(1-e^{-\rho t}\right) \\
& \leq D_{K L}\left(\rho_{0} \| \pi\right)+c_{1}^{\prime} \rho^{-1} d:=c_{2} d
\end{aligned}
$$

where $\rho:=\frac{1}{4 \beta C_{\pi}^{L S}}$. Hence the second claim (A.7) holds.

Now, equipped with the two claims (A.6) and (A.7), using integration by parts, we know that for all differential, nonnegative, non-increasing $f$,

$$
\begin{aligned}
& \int_{0}^{T} e^{-A_{0}(T-s)} f(s) \mathcal{I}\left(\rho_{s}^{\boldsymbol{\xi}}\right) d s \\
\leq & -\tilde{c_{0}} \int_{0}^{T} e^{-A_{0}(T-s)} f(s)\left(\frac{d}{d s} D_{K L}\left(\rho_{s}^{\boldsymbol{\xi}} \| \pi\right)\right) d s+\tilde{c_{1}} d \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s \\
= & \tilde{c_{1}} d \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s-\tilde{c_{0}} f(T) D_{K L}\left(\rho_{T}^{\boldsymbol{\xi}} \| \pi\right)+\tilde{c_{0}} e^{-A_{0} T} f(0) D_{K L}\left(\rho_{0} \| \pi\right) \\
& +\tilde{c_{0}} \int_{0}^{T} e^{-A_{0}(T-s)} f^{\prime}(s) D_{K L}\left(\rho_{s}^{\boldsymbol{\xi}} \| \pi\right) d s+\tilde{c_{0}} A_{0} \int_{0}^{T} e^{-A_{0}(T-s)} f(s) D_{K L}\left(\rho_{s}^{\boldsymbol{\xi}} \| \pi\right) d s \\
\leq & \tilde{c_{1}} d \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s+0+\tilde{c_{0}} e^{-A_{0} T} f(0) D_{K L}\left(\rho_{0} \| \pi\right)+0+\tilde{c_{0}} c_{2} d \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s \\
:= & M_{1} D_{K L}\left(\rho_{0} \| \pi\right) f(0) e^{-A_{0} T}+M_{2} d\left(1+\sup _{s \geq 0} D_{K L}\left(\rho_{s}^{\boldsymbol{\xi}} \| \pi\right)\right) \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s
\end{aligned}
$$

Here, $\tilde{c_{0}}, \tilde{c_{1}}, M_{1}, M_{2}$ are positive constants independent of $\xi$. The last inequality is because the KL-divergence is non-negative, and $f$ is nonnegative and non-increasing.

Now, we have already obtained the desired estimation

$$
\begin{aligned}
& \int_{0}^{T} e^{-A_{0}(T-s)} f(s) \mathcal{I}\left(\rho_{s}^{\xi}\right) d s \\
& \leq M_{1} D_{K L}\left(\rho_{0} \| \pi\right) f(0) e^{-A_{0} T}+M_{2} d\left(1+\sup _{s \geq 0} D_{K L}\left(\rho_{s}^{\xi} \| \pi\right)\right) \int_{0}^{T} e^{-A_{0}(T-s)} f(s) d s
\end{aligned}
$$

for all differential, non-increasing, nonnegative function $f$. Since piecewise-constant functions can be approximated by differential functions, we know that (A.15) holds for all nonincreasing, nonnegative, piecewise-constant function $f$. This then ends the proof.

## A. 3 Basics on path measure

In this section, we review some basics of path measure. Consider the following two SDEs in $\mathbb{R}^{d}$ with different drifts but the same diffusion $\sigma$ :

$$
\begin{aligned}
& d X^{(1)}=b^{(1)}\left(X^{(1)}, x_{0}\right) d t+\sigma \cdot d W, \\
& d X^{(2)}=b^{(2)}\left(X^{(2)}, x_{0}\right) d t+\sigma \cdot d W,
\end{aligned} \quad X_{0}^{(1)}=X_{0}^{(2)}=x_{0}
$$

Here, $W$ is a standard Brownian motion under the probability $\mathbb{P}$ (the same for the two SDEs), and $x_{0} \sim \mu_{0}$ is a common, but random, initial position. We allow the drifts to be possibly dependent on the initial position $x_{0}$ for our application. For fixed time interval $[0, T]$, the two processes $X^{(1)}$ and $X^{(2)}$ naturally induce two probability measures in the path space $\mathcal{X}:=C\left([0, T] ; \mathbb{R}^{d}\right)$, denoted by $P^{(1)}$ and $P^{(2)}$, respectively. To be more specific, for $[s, t] \subset[0, T], A \in \mathcal{B}\left(\mathbb{R}^{d}\right), P^{(i)}([s, t] \times A)=\mathbb{P}\left(X_{\tau}^{(i)} \in A, \tau \in[s, t]\right), i=1,2$. It is also obvious that the two probability measures $P^{(1)}, P^{(2)}$ are mutually absolutely continuous, so we are able to define the Radon-Nikodym derivative $\frac{d P^{(1)}}{d P^{(2)}} \in L^{1}\left(P^{(2)}, \mathcal{X}\right)$.

To obtain the formula for $\frac{d P^{(1)}}{d P^{(2)}} \in L^{1}\left(P^{(2)}, \mathcal{X}\right)$, we recall that the Girsanov transform $[19,12,10]$ asserts that under the probability measure $\mathbb{Q}$ satisfying

$$
\begin{aligned}
\frac{d \mathbb{Q}}{d \mathbb{P}}\left(X^{(2)}(\omega)\right)=\exp \left(\int _ { 0 } ^ { T } ( b ^ { ( 1 ) } - b ^ { ( 2 ) } ) \left(X_{s}^{(2)}\right.\right. & \left., x_{0}\right) \cdot G^{-1} \sigma \cdot d W_{s} \\
& \left.-\frac{1}{2} \int_{0}^{T}\left|\left(b^{(1)}-b^{(2)}\right)\left(X_{s}^{(2)}, x_{0}\right) \cdot G^{-1} \sigma\right|^{2} d s\right)
\end{aligned}
$$

with the matrix $G$ is defined by

$$
G:=\left(\sigma \sigma^{T}\right)^{-1}
$$

the law of $X^{(2)}$ is the same as the law of $X^{(1)}$ under $\mathbb{P}$. In other words, for any Borel measurable set $B \subset \mathcal{X}$,

$$
\mathbb{E}_{\mathbb{P}}\left[1_{B}\left(X^{(1)}\right)\right]=\mathbb{E}_{\mathbb{Q}}\left[1_{B}\left(X^{(2)}\right)\right]=\mathbb{E}_{\mathbb{P}}\left[1_{B}\left(X^{(2)}\right) \frac{d \mathbb{Q}}{d \mathbb{P}}\right]
$$

Note that the expression of $\frac{d \mathbb{Q}}{d \mathbb{P}}(\omega)=g\left(X^{(2)}(\omega)\right)$ where $\left(X_{0}:=X(0)\right)$

$$
\begin{aligned}
& g(X)=\exp \left(\int_{0}^{T}\left(b^{(1)}-b^{(2)}\right)\left(X, X_{0}\right)\right) \cdot G^{-1} \cdot d X \\
&\left.+\frac{1}{2} \int_{0}^{T}\left(b^{(2)} \cdot G^{-1} \cdot b^{(2)}-b^{(1)} \cdot G^{-1} \cdot b^{(1)}\right)\left(X, X_{0}\right) d s\right)
\end{aligned}
$$

Since $P^{(1)}=\left(X^{(1)}\right) \# \mathbb{P}$ and $P^{(2)}=\left(X^{(2)}\right) \# \mathbb{P}$ are the laws of $X^{(1)}$ and $X^{(2)}$ respectively, then one has

$$
P^{(1)}(B)=\mathbb{E}_{X \sim P^{(2)}}\left[\mathbf{1}_{B}(X) g(X)\right]
$$

It follows that the Radon-Nikodym derivative is

$$
\frac{d P^{(1)}}{d P^{(2)}}(X)=g(X)
$$

Hence, since $d X^{(2)}=b^{(2)}\left(X^{(2)}, x_{0}\right) d t+\sigma \cdot d W$, we have derived that

$$
\begin{aligned}
\frac{d P^{(1)}}{d P^{(2)}}\left(X^{(2)}(\omega)\right)=\frac{d \mathbb{Q}}{d \mathbb{P}}(\omega)=\exp ( & \int_{0}^{T}\left(b^{(1)}-b^{(2)}\right)\left(X_{s}^{(2)}, x_{0}\right) \cdot G^{-1} \sigma \cdot d W_{s} \\
& \left.\quad-\frac{1}{2} \int_{0}^{T}\left|\left(b^{(1)}-b^{(2)}\right)\left(X_{s}^{(2)}, x_{0}\right) \cdot G^{-1} \sigma\right|^{2} d s\right)
\end{aligned}
$$

which is a martingale under $\mathbb{P}$ and its natural filtration defined by $\mathcal{F}_{t}^{(2)}:=\sigma\left(X_{s}^{(2)}, s \leq t\right)$, $t \in[0, T]$. Note that (A.17) will be used in our proof.

Moreover, we can view the process $X^{(i)}$ as an identical mapping: $X^{(i)}=\left(X_{t}^{(i)}\right)_{0 \leq t \leq T}$ : $\Omega \rightarrow \mathcal{X}$. For fixed $t \in[0, T], X_{t}^{(i)}$ can be viewed as a measurable mapping from $\Omega$ to $\mathbb{R}^{d}$ and one in fact has $X_{t}^{(i)}=\omega_{t} \circ X^{(i)} \in \mathbb{R}^{d}$, where $\omega_{t}: \mathcal{X} \rightarrow \mathbb{R}^{d}$ is the time marginal defined by $\omega_{t}(\gamma)=\gamma_{t}$. Then the law of the solution $X_{t}^{(i)}$ at time $t$, namely, the time marginal of $P^{(i)}$, is the push forward measures $P_{t}^{(i)}:=\left(X_{t}^{(i)}\right) \# \mathbb{P}=\left(\omega_{t}\right)_{\#} P^{(i)}, \forall t \in[0, T]$. This means $P_{t}^{(i)}$ is a probability measure in $\mathbb{R}^{d}$, satisfying

$$
P_{t}^{(i)}(A)=\mathbb{P}\left(X_{t}^{(i)} \in A\right), \quad \forall A \in \mathcal{B}\left(\mathbb{R}^{d}\right), \quad i=1,2
$$

Clearly, at any time $t, P_{t}^{(1)}$ and $P_{t}^{(2)}$ are mutually absolutely continuous, the Radon-Nikodym derivative $\frac{d P_{t}^{(1)}}{d P_{t}^{(2)}} \in L^{1}\left(P_{t}^{(2)}, \mathbb{R}^{d}\right)$ is well defined.

The following Lemma describes the relationship between the two Radon-Nikodym derivatives (of path measures and of push forward measures):

Lemma A.1. Let $Q_{1}, Q_{2}$ be two probability distributions on $\mathcal{X}$, and $Q_{2}$ is absolutely continuous with respect to $Q_{1}$. Let $\phi: \mathcal{X} \rightarrow \mathbb{R}^{d}$ be a measurable mapping, and consider the push forward measure $\phi_{\#} Q_{1}$ and $\phi_{\#} Q_{2}$, denoted by $Q_{1, \phi}$ and $Q_{2, \phi}$, respectively. Then the Randon-Nikodym derivatives $\frac{d Q_{1, \phi}}{d Q_{2, \phi}} \in L^{1}\left(d Q_{2, \phi}, \mathbb{R}^{d}\right), \frac{d Q_{1}}{d Q_{2}} \in L^{1}\left(d Q_{2}, \mathcal{X}\right)$ are well-defined, and

$$
\frac{d Q_{1, \phi}}{d Q_{2, \phi}}(x)=\mathbb{E}_{X \sim Q_{2}}\left[\left.\frac{d Q_{1}}{d Q_{2}} \right\rvert\, \phi(X)=x\right], \quad Q_{2}-\text { a.e. }
$$

Proof of Lemma A.1: Using the definition of Radon-Nikodym derivative, it suffices to check that for any $A \in \mathcal{B}\left(\mathbb{R}^{d}\right)$,

$$
\mathbb{E}_{x \sim Q_{1, \phi}}\left[\mathbf{1}_{A}(x)\right]=\mathbb{E}_{x \sim Q_{2, \phi}}\left[\mathbf{1}_{A}(x) \mathbb{E}_{X \sim Q_{2}}\left[\left.\frac{d Q_{1}}{d Q_{2}}(X) \right\rvert\, \phi(X)=x\right]\right]
$$

Indeed, using the definition of push forward measure and Randon-Nikodym derivative, as well as the conditional expectation, we have

$$
\begin{aligned}
L H S & =\mathbb{E}_{X \sim Q_{1}}\left[\mathbf{1}_{A}(\phi(X))\right] \\
& =\mathbb{E}_{X \sim Q_{2}}\left[\frac{d Q_{1}}{d Q_{2}}(X) \mathbf{1}_{A}(\phi(X))\right] \\
& =\mathbb{E}_{X \sim Q_{2}}\left[\mathbf{1}_{A}(\phi(X)) \mathbb{E}_{X \sim Q_{2}}\left[\left.\frac{d Q_{1}}{d Q_{2}}(X) \right\rvert\, \phi(X)\right]\right] \\
& =\text { RHS }
\end{aligned}
$$

This is what we want.

Clearly, if we take $\phi=\omega_{t}$ for $t \in[0, T]$, the time projection mapping, then we conclude the following result for Radon-Nikodym of time marginals.

Corollary A.1. For $t \in[0, T]$, recall the definition of $P_{t}^{(i)}$ and $P^{(i)}, i=1,2$ above. Then the following holds:

$$
\frac{d P_{t}^{(1)}}{d P_{t}^{(2)}}(x)=\mathbb{E}_{X \sim P^{(2)}}\left[\left.\frac{d P^{(1)}}{d P^{(2)}}(X) \right\rvert\, X_{t}=x\right], \quad \mathbb{P}-\text { a.e. }
$$

Also note that Corollary A. 1 here is very useful. For instance, if we combine the result (A.21) in Corollary A. 1 with the Girsanov transform in (A.17), we can express the quotient of densities of two processes $\rho^{(1)} / \rho^{(2)}$ by one process $X^{(2)}$ alone. Meanwhile, the information coming from the process $X^{(1)}$ is stored in the drift term $b^{(1)}(\cdot)$, which is usually a deterministic function. Then we only need to look into one of these two processes instead of both of them, and this can often simplify the analysis.

## A. 4 Estimate of the remaining terms

We estimate the remaining terms

$$
\mathbb{E}_{\xi_{k}} \mathbb{E}\left[\left|\bar{b}_{t}^{\xi_{k}}\left(\bar{X}_{t}\right)-b^{\xi_{k}}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right]
$$

, and

$$
\mathbb{E}_{\xi_{k}, \tilde{\xi}_{k}}\left[\int\left|b^{\xi_{k}}-b\right|^{2} \frac{\left|\hat{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{-\xi_{k}}\right|^{2}}{\hat{\rho}_{t}^{\tilde{\varepsilon}_{k}}} d x\right]
$$

in Section 4. Note that in the followings we consider the behaviour of SGLD in a time subinterval $\left[T_{k}, T_{k+1}\right)$, and recall that $\bar{\rho}^{\xi_{k}}, \bar{\rho}^{\tilde{\xi}_{k}}$ are defined in (4.1).

Lemma A.2. Recall the definition of $\bar{r}_{t}(x)$ in (4.14). Then under the setting of Proposition 3.2, there exists a positive constant $c$ independent of the choice of the batch $\xi_{k}$ such that for all $t \in\left[T_{k}, T_{k+1}\right)$, it holds that

$$
\mathbb{E}\left[\left|\bar{r}_{t}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq c d\left(t-T_{k}\right)^{2}
$$

Proof of Lemma A.2: Since $\nabla b^{\xi}$ is $L_{2}$-Lipshitz, we know that

$$
\left|\bar{r}_{t}(x)\right| \leq L_{2} \mathbb{E}\left[\left|\bar{X}_{T_{k}}-\bar{X}_{t}\right|^{2} \mid \bar{X}_{t}=x, \xi_{k}\right]
$$

Hence by Jensen's inequality, and using the Lipshitz assumption for $b^{\xi_{k}}$ in Assumption 3.1, we haveddd

$$
\begin{aligned}
\mathbb{E}\left[\left|\bar{r}_{t}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] & \leq L_{2}^{2} d^{-1} \mathbb{E}\left[\left|\mathbb{E}\left[\left|\bar{X}_{T_{k}}-\bar{X}_{t}\right|^{2} \mid \bar{X}_{t}=x\right]\right|^{2} \mid \xi_{k}\right] \\
& \leq L_{2}^{2} d^{-1} \mathbb{E}\left[\mathbb{E}\left[\left|\bar{X}_{T_{k}}-\bar{X}_{t}\right|^{4} \mid \bar{X}_{t}=x\right] \mid \xi_{k}\right] \\
& =L_{2}^{2} d^{-1} \mathbb{E}\left[\left|b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)\left(t-T_{k}\right)+\int_{T_{k}}^{t} d W\right|^{4} \mid \xi_{k}\right] \\
& \leq L_{2}^{2} d^{-1}\left(\left(t-T_{k}\right)^{4}\left(\left|b^{\xi_{k}}(0)\right|+L \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right| \mid \xi_{k}\right]\right)^{4}+3\left(t-T_{k}\right)^{2} d^{2}\right)
\end{aligned}
$$

where we use the inequality $(a+b)^{p} \leq 2^{p-1}\left(a^{p}+b^{p}\right)$ in the last inequality.

Finally, by Proposition 3.1, we have a uniform bound for the moment $\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{4} \mid \mathcal{F}_{\xi}\right]$, which leads to the conclusion (A.22).

Lemma A.3. Under the setting of Proposition 3.2, there exists a positive constant c independent of $k$ and $\xi_{k}$ such that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int\left|\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=x, \xi_{k}\right]\right|^{2} \bar{\rho}_{t}^{\xi_{k}}(x) d x \leq c \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right)
$$

where $\mathcal{I}(\rho):=\int \rho|\nabla \log \rho|^{2} d x$ is the Fisher information.

Proof of Lemma A.3: By Bayes' law, we have

$$
\begin{aligned}
\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=x, \xi_{k}\right] & =\int(y-x) P\left(\bar{X}_{T_{k}}=y \mid \bar{X}_{t}=x, \xi_{k}\right) d y \\
& =\int(y-x) \frac{\bar{\rho}_{T_{k}}(y) P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)}{\bar{\rho}_{t}^{\xi_{k}}(x)} d y
\end{aligned}
$$

Since $P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)$ is Gaussian, and since its derivative is also similar to the Gaussian form, we split the term $\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=x, \xi_{k}\right]$ into three parts and use integration by parts to handle them.

Let

$$
\begin{aligned}
y-x= & \left(I_{d}+\left(t-T_{k}\right) \nabla b^{\xi_{k}}(y)\right) \cdot\left(y-x+\left(t-T_{k}\right) b^{\xi_{k}}(y)\right) \\
& -\left(t-T_{k}\right) \nabla b^{\xi_{k}}(y) \cdot\left(y-x+\left(t-T_{k}\right) b^{\xi_{k}}(y)\right) \\
& -\left(t-T_{k}\right) \cdot b^{\xi_{k}}(y) \\
:= & a_{1}(x, y)-a_{2}(x, y)-a_{3}(x, y)
\end{aligned}
$$

and define

$$
I_{i}(x):=\mathbb{E}\left[a_{i}\left(\bar{X}_{t}, \bar{X}_{T_{k}}\right) \mid \bar{X}_{t}=x\right], \quad i=1,2,3
$$

Next, we will obtain an $\eta_{k}^{2}$ estimate for $\mathbb{E}\left[\left|I_{i}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right], i=1,2,3$. We first claim that, there exist positive constants $c, c^{\prime}, c^{\prime \prime}$ independent of $k$ and $\xi$ such that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\begin{aligned}
& \mathbb{E}\left[\left|I_{1}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq c\left(t-T_{k}\right)^{2} \mathcal{I}\left(\bar{\rho}_{T_{k}}\right) \\
& \mathbb{E}\left[\left|I_{2}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq c^{\prime} d\left(t-T_{k}\right)^{3} \\
& \mathbb{E}\left[\left|I_{3}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq c^{\prime \prime} d\left(t-T_{k}\right)^{2}
\end{aligned}
$$

where $\mathcal{I}(\rho):=\int \rho|\nabla \log \rho|^{2} d x$ is the Fisher information.

By the claims (A.26), (A.27), (A.28), we can easily obtain the following $O\left(\eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right)\right.$ bound:

$$
\int\left|\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t} \mid \bar{X}_{t}=x, \xi_{k}\right]\right|^{2} \bar{\rho}_{t}^{\xi_{k}}(x) d x \leq 3 \sum_{i=1}^{3} \mathbb{E}\left[\left|I_{i}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq \tilde{c} \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right)
$$

where the positive constant $\tilde{c}$ is independent of the batch $\xi_{k}$, and this is what we desire.

For the the claims (A.26), (A.27), (A.28), we prove them separately in the followings:

(a) For the term $I_{1}$, since the distribution $P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)$ is Gaussian, namely,

$$
P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right)=\left(4 \pi \beta^{-1}\left(t-T_{k}\right)\right)^{-\frac{d}{2}} \exp \left(-\frac{\left|x-y-b^{\xi_{k}}(y)\left(t-T_{k}\right)\right|^{2}}{4 \beta^{-1}\left(t-T_{k}\right)}\right)
$$

Then, after integration by parts we obtain:

$$
I_{1}(x)=2 \beta^{-1}\left(t-T_{k}\right) \int \frac{\nabla_{y} \bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{t}^{\xi_{k}}(x)} P\left(\bar{X}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}\right) d y
$$

Using Bayes' law again, we have

$$
I_{1}(x)=2 \beta^{-1}\left(t-T_{k}\right) \int \frac{\nabla_{y} \bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{T_{k}}(y)} P\left(\bar{X}_{T_{k}}=y \mid \bar{X}_{t}=x, \xi_{k}\right) d y
$$

Hence, by Jensen's inequality,

$$
\begin{aligned}
\mathbb{E}\left[\left|I_{1}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] & \leq 4 \beta^{-2}\left(t-T_{k}\right)^{2} \int \bar{\rho}_{t}^{\xi_{k}}(x) \int\left|\frac{\nabla_{y} \bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{T_{k}}(y)}\right|^{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{X}_{t}=x, \xi_{k}\right) d y d x \\
& =4 \beta^{-2}\left(t-T_{k}\right)^{2} \mathcal{I}\left(\bar{\rho}_{T_{k}}\right):=c\left(t-T_{k}\right)^{2} \mathcal{I}\left(\bar{\rho}_{T_{k}}\right)
\end{aligned}
$$

(b) For the term $I_{2}$, using the Lipshitz condition in Assumption 3.1 and Jensen's inequality, we have

$$
\begin{aligned}
\mathbb{E}\left[\left|I_{2}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] & \leq \tilde{c}^{\prime}\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|\mathbb{E}\left[\bar{X}_{t}-\bar{X}_{T_{k}}-\left(t-T_{k}\right) b^{\xi_{k}}\left(\bar{X}_{t}\right) \mid \bar{X}_{T_{k}}\right]\right|^{2} \mid \xi_{k}\right] \\
& \leq \tilde{c}^{\prime}\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|\bar{X}_{t}-\bar{X}_{T_{k}}-\left(t-T_{k}\right) b^{\xi_{k}}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \\
& \leq \tilde{c}^{\prime}\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|\int_{T_{k}}^{t} \sqrt{2 \beta^{-1}} d W_{s}\right|^{2} \mid \xi_{k}\right]=c^{\prime} d\left(t-T_{k}\right)^{3}
\end{aligned}
$$

The constant $c^{\prime}$ here is independent of $\xi_{k}$ since the Lipshitz constant is uniform.

(c) For the term $I_{3}$, still using Jensen's inequality and Lipshitz assumption for $b^{\xi_{k}}$, it is clear that

$$
\begin{aligned}
\mathbb{E}\left[\left|I_{3}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] & \leq\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)\right|^{2} \mid \xi_{k}\right] \\
& \leq 2\left(t-T_{k}\right)^{2}\left(\left|b^{\xi_{k}}(0)\right|^{2}+L_{2} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{2} \mid \xi_{k}\right]\right)
\end{aligned}
$$

By Proposition 3.1, for any fixed batch $\xi_{k}$, the moment $\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{2} \mid \xi_{k}\right]$ has a uniform-in-batch $O(1)$ upper bound. Therefore, we are able to obtain the following batch-independent bound for the term $\bar{I}_{3}$ :

$$
\mathbb{E}\left[\left|I_{3}\left(\bar{X}_{t}\right)\right|^{2} \mid \xi_{k}\right] \leq c^{\prime \prime} d\left(t-T_{k}\right)^{2}
$$

Concluding the results we obtained in parts (a), (b), (c) yields the claims (A.26), (A.27), $($ A. 28$)$.



Lemma A.4. Recall the notations

$$
K_{1}:=\sqrt{\frac{\beta}{2}} \tilde{b}(y)(x-y), \quad \tilde{b}(y):=\left(b^{\xi_{k}}-b^{\tilde{\xi}_{k}}\right)(y)
$$

Then under the conditions of Proposition 3.2, there exists a positive constant c independent of $k$ and $\xi_{k}, \tilde{\xi}_{k}$ such that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{1} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c \eta_{k}^{2}\left(d+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right)
$$

Proof of Lemma A.4: The technique here is similar to the one we use in the proof of Lemma A.3. To begin with, we split the term $K_{1}$ into the following three parts:

$$
\begin{aligned}
\tilde{b}(y) \cdot(y-x)= & \tilde{b}(y) \cdot\left(I_{d}+\left(t-T_{k}\right) \nabla b^{\tilde{\xi}_{k}}(y)\right) \cdot\left(y-x+\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right) \\
& -\left(t-T_{k}\right) \tilde{b}(y) \cdot \nabla b^{\tilde{\xi}_{k}}(y) \cdot\left(y-x+\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right) \\
& -\left(t-T_{k}\right) \tilde{b}(y) \cdot b^{\tilde{\xi}_{k}}(y) \\
:= & \bar{a}_{1}(x, y)-\bar{a}_{2}(x, y)-\bar{a}_{3}(x, y)
\end{aligned}
$$

and define

$$
\bar{I}_{i}(x):=\mathbb{E}\left[\bar{a}_{i}\left(\bar{X}_{T_{k}}, \bar{Y}_{t}\right) \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right], \quad i=1,2,3
$$

Then,

$$
\int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{1} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x\right) d y\right)^{2} d x=\frac{\beta}{2} \mathbb{E}\left[\left|\bar{I}_{1}\left(\bar{Y}_{t}\right)-\bar{I}_{2}\left(\bar{Y}_{t}\right)-\bar{I}_{3}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]
$$

(a) For the first term $\bar{I}_{1}$, using Bayes' formula and integration by parts, since $P\left(\bar{Y}_{t}=\right.$ $\left.x \mid \bar{X}_{T_{k}}=y, \xi_{k}, \tilde{\xi}_{k}\right)$ is Gaussian, we have

$$
\begin{aligned}
\bar{I}_{1}(x) & =2 \beta^{-1} \int \tilde{b}(y) \cdot\left(I_{d}+\left(t-T_{k}\right) \nabla b^{\tilde{\xi}_{k}}(y)\right) \cdot \frac{\beta}{2}\left(y-x+\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right) \frac{\bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)} P\left(\bar{Y}_{t}=x \mid \bar{X}_{T_{k}}=y\right) d y \\
& =2 \beta^{-1}\left(t-T_{k}\right) \int \frac{\nabla y\left(\tilde{b}(y) \bar{\rho}_{T_{k}}(y)\right)}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)} P\left(\bar{Y}_{t}=x \mid \bar{X}_{T_{k}}=y, \xi_{k}, \tilde{\xi}_{k}\right) d y \\
& =2 \beta^{-1}\left(t-T_{k}\right) \int\left(\nabla \tilde{b}(y)+\tilde{b}(y) \frac{\nabla \bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{T_{k}}(y)}\right) P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y
\end{aligned}
$$

Since $\nabla \tilde{b}$ and $\tilde{b}=\left[\left(b^{\xi_{k}}-b\right)-\left(b^{\tilde{\xi}_{k}}-b\right)\right] / \sqrt{2 \beta^{-1}}$ are uniformly bounded by Assumption 3.1, we obtain

$$
\mathbb{E}\left[\left|\bar{I}_{1}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq c \eta_{k}^{2}\left(1+\mathcal{I}\left(\bar{\rho}_{T_{k}}\right)\right)
$$

and the constant $c$ is independent of $\xi_{k}$ and $\tilde{\xi}_{k}$.

(b) For the second term $\bar{I}_{2}$, by Jensen's inequality, it holds that

$$
\mathbb{E}\left[\left|\bar{I}_{2}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|\tilde{b}\left(\bar{X}_{T_{k}}\right) \cdot \nabla b^{\tilde{\xi}_{k}}\left(\bar{X}_{T_{k}}\right) \cdot \int_{T_{k}}^{t} d W\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]
$$

By Assumption 3.1, both $\tilde{b}=\left[\left(b^{\xi_{k}}-b\right)-\left(b^{\tilde{\xi}_{k}}-b\right)\right] / \sqrt{2 \beta^{-1}}$ and $\nabla b^{\tilde{\xi}_{k}}$ are uniformly bounded, so we can directly get

$$
\mathbb{E}\left[\left|\overline{\bar{I}}_{2}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq c d\left(t-T_{k}\right)^{3}
$$

and the constant $c$ is independent of $\xi_{k}$ and $\tilde{\xi}_{k}$.

(c) For the third term $\bar{I}_{3}$, by Jensen's inequality,

$$
\mathbb{E}\left[\left|\bar{I}_{3}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|\tilde{b}\left(\bar{X}_{T_{k}}\right) \cdot b^{\tilde{\xi}_{k}}\left(\bar{X}_{T_{k}}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]
$$

Since $\tilde{b}$ is bounded, and since $b^{\tilde{\xi}_{k}}$ is Lipshitz by Assumption 3.1, we have

$$
\begin{aligned}
\mathbb{E}\left[\left|\bar{I}_{3}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] & \leq c\left(t-T_{k}\right)^{2} \mathbb{E}\left[\left|b^{\tilde{\xi}_{k}}\left(\bar{X}_{T_{k}}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \\
& \leq 2 c\left(t-T_{k}\right)^{2}\left(\left|b^{\tilde{\xi}_{k}}(0)\right|^{2}+L^{2} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]\right)
\end{aligned}
$$

Due to (3.4), $\left|b^{\tilde{\xi}_{k}}(0)\right| \leq|b(0)|+\left|b^{\tilde{\xi}_{k}}(0)-b(0)\right|$ is uniformly bounded almost surely. By Proposition 3.1, there is a uniform-in-batch $O(1)$ bound for the moment $\mathbb{E}\left|\bar{X}_{T_{k}}\right|^{2}$. Hence we obtain

$$
\mathbb{E}\left[\left|\overline{\bar{I}}_{3}\left(\bar{Y}_{t}\right)\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq c d\left(t-T_{k}\right)^{2}
$$

and the constant $c$ is independent of $\xi_{k}$ and $\tilde{\xi}_{k}$.

Finally, combining (a), (b) and (c), we get the desired result.

## Lemma A.5. Recall the notations

$$
K_{2}:=\left(-\sqrt{\frac{\beta}{2}} \tilde{b}(y) \cdot b^{\tilde{\xi}_{k}}(y)-\frac{1}{2}|\tilde{b}(y)|^{2}\right)\left(t-T_{k}\right), \quad \tilde{b}(y):=\frac{1}{\sqrt{2 \beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y)
$$

Then under the conditions of Proposition 3.2, there exists a positive constant c independent of $k$ and $\xi_{k}$ such that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int \tilde{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c d \eta_{k}^{2}
$$

The bound is independent of the choice of the batches $\tilde{\xi}_{k}, \xi_{k}$.

Proof of A.5: By Jensen's inequality, we have

$$
\begin{aligned}
& \int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x\right) d y\right)^{2} d x \\
\leq & \int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int\left|K_{2}\right|^{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x\right) d y\right) d x \\
= & \left(t-T_{k}\right)^{2} \mathbb{E}\left[\left.\left.\left.\left|\sqrt{\frac{\beta}{2}} \tilde{b}\left(\bar{X}_{T_{k}}\right) \cdot b^{\tilde{\xi}_{k}}\left(\bar{X}_{T_{k}}\right)+\frac{1}{2}\right| \tilde{b}\left(\bar{X}_{T_{k}}\right)\right|^{2}\right|^{2} \right\rvert\, \xi_{k}, \tilde{\xi}_{k}\right]
\end{aligned}
$$

Since $b^{\tilde{\xi}_{k}}$ is Lipshitz by Assumption 3.1, we have

$$
\mathbb{E}\left[\left.\left.\left.\left|\sqrt{\frac{\beta}{2}} \tilde{b}\left(\bar{X}_{T_{k}}\right) \cdot b^{\tilde{\xi}_{k}}\left(\bar{X}_{T_{k}}\right)+\frac{1}{2}\right| \tilde{b}\left(\bar{X}_{T_{k}}\right)\right|^{2}\right|^{2} \right\rvert\, \xi_{k}, \tilde{\xi}_{k}\right] \leq \tilde{c}_{1}+\tilde{c}_{2} \mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]
$$

Here, the positive constants $\tilde{c_{1}}, \tilde{c_{2}}$ are independent of the batch since the coefficients in conditions (a), (d) of Assumption 3.1 are uniform-in-batch. By Proposition 3.1, $\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{2}\right]$ has a uniform-in-batch $O(1)$ upper bound. Combining this fact with (A.47), one then has

$$
\int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c d \eta_{k}^{2}
$$

Here, $c$ is a positive constant independent of $k, d, \xi_{k}$ and $\tilde{\xi}_{k}$.

Lemma A.6. Recall the notations

$$
K_{3}:=e^{z}-1-z
$$

with

$$
z:=\sqrt{\frac{\beta}{2}} \tilde{b}(y)\left(x-y-\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}(y)\right)-\frac{1}{2}|\tilde{b}(y)|^{2}\left(t-T_{k}\right)
$$

and

$$
\tilde{b}(y):=\frac{1}{\sqrt{2 \beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y)
$$

Then under the conditions of Proposition 3.2, there exists a positive constant c independent of $k$ and $\xi_{k}$ such that for $t \in\left[T_{k}, T_{k+1}\right)$,

$$
\int \tilde{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{3} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \leq c d \eta_{k}^{2}
$$

Proof of Lemma A.6: By Jensen's inequality, it holds that

$$
\begin{aligned}
& \int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{3} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x, \xi_{k}, \tilde{\xi}_{k}\right) d y\right)^{2} d x \\
\leq & \int \bar{\rho}_{t}^{\tilde{\xi}_{k}}(x) \int\left|K_{3}\right|^{2} P\left(\bar{X}_{T_{k}}=y \mid \bar{Y}_{t}=x\right) d y d x=\mathbb{E}\left[\left|e^{\hat{Y}_{t}}-1-\hat{Y}_{t}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]
\end{aligned}
$$

where we denote the process

$$
\begin{aligned}
\hat{Y}_{t} & :=\sqrt{\frac{\beta}{2}} \tilde{b}\left(\bar{X}_{T_{k}}\right) \cdot\left(\bar{Y}_{t}-\bar{X}_{T_{k}}-\left(t-T_{k}\right) b^{\tilde{\xi}_{k}}\left(\bar{X}_{T_{k}}\right)\right)-\frac{1}{2}\left|\tilde{b}\left(\bar{X}_{T_{k}}\right)\right|^{2} \Delta t \\
& =-\frac{1}{2}\left|\tilde{b}\left(\bar{X}_{T_{k}}\right)\right|^{2} \Delta t+\tilde{b}\left(\bar{X}_{T_{k}}\right) \cdot \int_{T_{k}}^{t} d W
\end{aligned}
$$

with

$$
\Delta t:=t-T_{k}, \quad \forall t \in\left[T_{k}, T_{k+1}\right)
$$

Denote $\bar{Z}_{t}:=e^{\hat{Y}_{t}}-1-\hat{Y}_{t}$. In the following, we aim to obtain an $O\left(\eta_{k}^{2}\right)$ bound for the term $\mathbb{E}\left[\left|\bar{Z}_{t}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]$ mainly via Itô's formula. In fact, for $t \in\left[T_{k}, T_{k+1}\right)$

$$
\bar{Z}_{t}=\frac{1}{2}|\tilde{b}|^{2} \Delta t+\tilde{b} \cdot \int_{T_{k}}^{t}\left(e^{\hat{Y}_{s}}-1\right) d W_{s}=\frac{1}{2}|\tilde{b}|^{2} \Delta t+\tilde{b} \cdot \int_{T_{k}}^{t}\left(\bar{Z}_{s}+\hat{Y}_{s}\right) d W_{s}
$$

So

$$
\mathbb{E}\left[\left|\bar{Z}_{t}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right]=\frac{1}{4} \mathbb{E}\left[|\tilde{b}|^{4} \mid \xi_{k}, \tilde{\xi}_{k}\right](\Delta t)^{2}+\int_{T_{k}}^{t} \mathbb{E}\left[\left|\tilde{b}^{2}\left(\bar{Z}_{s}+\hat{Y}_{s}\right)^{2}\right| \xi_{k}, \tilde{\xi}_{k}\right] d s
$$

By Assumption 3.1, $\tilde{b}$ is uniformly bounded. Then, $\mathbb{E}\left[\left|\hat{Y}_{t}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq c d \Delta t$. Then, one has

$$
\mathbb{E}\left[\left|\bar{Z}_{t}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq c \int_{T_{k}}^{t} \mathbb{E}\left[\left|\bar{Z}_{s}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] d s+c d(\Delta t)^{2}
$$

By Grönwall's inequality, when $\eta_{k}$ is small, one thus has

$$
\mathbb{E}\left[\left|\bar{Z}_{t}\right|^{2} \mid \xi_{k}, \tilde{\xi}_{k}\right] \leq c d(\Delta t)^{2} \leq c d \eta_{k}^{2}
$$

Above, $c$ is a generative positive constant independent of $k$ and $\xi_{k}$, with the concrete meaning varying from line to line. This then ends the proof.

## References

[1] Geometric ergodicity of SGLD via reflection coupling. 2022.

[2] Gabriele Abbati, Alessandra Tosi, Michael Osborne, and Seth Flaxman. Adageo: Adaptive geometric learning for optimization and sampling. In International conference on artificial intelligence and statistics, pages 226-234. PMLR, 2018.

[3] Aurélien Alfonsi, Benjamin Jourdain, and Arturo Kohatsu-Higa. Optimal transport bounds between the time-marginals of a multidimensional diffusion and its Euler scheme. Electronic Journal of Probability, 20:1-31, 2015.

[4] Dominique Bakry and Michel Émery. Diffusions hypercontractives. In Seminaire de probabilités XIX 1983/84, pages 177-206. Springer, 1985.

[5] Dominique Bakry, Ivan Gentil, Michel Ledoux, et al. Analysis and geometry of Markov diffusion operators, volume 103. Springer, 2014.

[6] François Bolley and Cédric Villani. Weighted Csiszár-Kullback-Pinsker inequalities and applications to transportation inequalities. In Annales de la Faculté des sciences de Toulouse: Mathématiques, volume 14, pages 331-352, 2005.

[7] Nicolas Brosse, Alain Durmus, and Eric Moulines. The promises and pitfalls of stochastic gradient Langevin dynamics. Advances in Neural Information Processing Systems, $31,2018$.

[8] Arnak S Dalalyan. Theoretical guarantees for approximate sampling from smooth and log-concave densities. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 79(3):651-676, 2017.

[9] Arnak S Dalalyan and Avetik Karagulyan. User-friendly guarantees for the Langevin Monte Carlo with inaccurate gradient. Stochastic Processes and their Applications, $129(12): 5278-5311,2019$.

[10] Arnak S Dalalyan and Alexandre B Tsybakov. Sparse regression learning by aggregation and Langevin Monte-Carlo. Journal of Computer and System Sciences, 78(5):1423$1443,2012$.

[11] Christian Daniel, Jonathan Taylor, and Sebastian Nowozin. Learning step size controllers for robust neural network training. In Thirtieth AAAI Conference on Artificial Intelligence, 2016.

[12] Richard Durrett. Stochastic calculus: a practical introduction. CRC press, 2018.

[13] Rick Durrett. Probability: theory and examples, volume 49. Cambridge university press, 2019.

[14] Andreas Eberle. Reflection coupling and Wasserstein contractivity without convexity. Comptes Rendus Mathematique, 349(19-20):1101-1104, 2011.

[15] Lawrence C Evans. Partial differential equations, volume 19. American mathematical society, 2022.

[16] Tyler Farghly and Patrick Rebeschini. Time-independent generalization bounds for SGLD in non-convex settings. Advances in Neural Information Processing Systems, $34: 19836-19846,2021$.

[17] Yuanyuan Feng, Tingran Gao, Lei Li, Jian-Guo Liu, and Yulong Lu. Uniform-in-time weak error analysis for stochastic gradient descent algorithms via diffusion approximation. arXiv preprint arXiv:1902.00635, 2019.

[18] Nicolas Fournier, Maxime Hauray, and Stéphane Mischler. Propagation of chaos for the 2d viscous vortex model. Journal of the European Mathematical Society, 16(7):1423$1466,2014$.

[19] Igor Vladimirovich Girsanov. On transforming a certain class of stochastic processes by absolutely continuous substitution of measures. Theory of Probability \& Its Applications, $5(3): 285-301,1960$.

[20] Leonard Gross. Logarithmic Sobolev inequalities. American Journal of Mathematics, 97(4):1061-1083, 1975

[21] Wenqing Hu, Chris Junchi Li, Lei Li, and Jian-Guo Liu. On the diffusion approximation of nonconvex stochastic gradient descent. Annals of Mathematical Sciences and Applications, 4(1), 2019.

[22] Shi Jin, Lei Li, and Jian-Guo Liu. Random batch methods (RBM) for interacting particle systems. Journal of Computational Physics, 400:108877, 2020.

[23] Shi Jin, Lei Li, Zhenli Xu, and Yue Zhao. A random batch Ewald method for particle systems with Coulomb interactions. SIAM Journal on Scientific Computing, 43(4):B937-B960, 2021.

[24] Shi Jin, Lei Li, Xuda Ye, and Zhennan Zhou. Ergodicity and long-time behavior of the random batch method for interacting particle systems. arXiv preprint arXiv:2202.04952, 2022.

[25] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980, 2014.

[26] Bobby Kleinberg, Yuanzhi Li, and Yang Yuan. An alternative view: When does SGD escape local minima? In International Conference on Machine Learning, pages 26982707. PMLR, 2018.

[27] Rep Kubo. The fluctuation-dissipation theorem. Reports on progress in physics, $29(1): 255,1966$.

[28] Solomon Kullback and Richard A Leibler. On information and sufficiency. The annals of mathematical statistics, 22(1):79-86, 1951.

[29] Michel Ledoux. Concentration of measure and logarithmic Sobolev inequalities. In Seminaire de probabilites XXXIII, pages 120-216. Springer, 1999.

[30] Lei Li and Jian-Guo Liu. Large time behaviors of upwind schemes and B-schemes for Fokker-Planck equations on $\mathrm{R}$ by jump processes. Mathematics of Computation, $89(325): 2283-2320,2020$.

[31] Lei Li, Lin Liu, and Yuzhou Peng. A splitting Hamiltonian Monte Carlo method for efficient sampling. arXiv preprint arXiv:2105.14406, 2021.

[32] Lei Li and Yuliang Wang. On uniform-in-time diffusion approximation for stochastic gradient descent. arXiv preprint arXiv:2207.04922, 2022.

[33] Wenzhe Li, Sungjin Ahn, and Max Welling. Scalable MCMC for mixed membership stochastic blockmodels. In Artificial Intelligence and Statistics, pages 723-731. PMLR, 2016.

[34] Peter A Markowich and Cédric Villani. On the trend to equilibrium for the FokkerPlanck equation: an interplay between physics and functional analysis. Mat. Contemp, $19: 1-29,2000$.

[35] Wenlong Mou, Nicolas Flammarion, Martin J Wainwright, and Peter L Bartlett. Improved bounds for discretization of Langevin diffusions: Near-optimal rates without convexity. arXiv preprint arXiv:190\%.11331, 2019.

[36] Wenlong Mou, Liwei Wang, Xiyu Zhai, and Kai Zheng. Generalization bounds of SGLD for non-convex learning: Two theoretical viewpoints. In Conference on Learning Theory, pages 605-638. PMLR, 2018.

[37] Arvind Neelakantan, Luke Vilnis, Quoc V Le, Ilya Sutskever, Lukasz Kaiser, Karol Kurach, and James Martens. Adding gradient noise improves learning for very deep networks. arXiv preprint arXiv:1511.06807, 2015.

[38] David Nualart. The Malliavin calculus and related topics, volume 1995. Springer, 2006.

[39] Felix Otto and Cédric Villani. Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality. Journal of Functional Analysis, 173(2):361$400,2000$.

[40] Sam Patterson and Yee Whye Teh. Stochastic gradient Riemannian Langevin dynamics on the probability simplex. Advances in neural information processing systems, 26, 2013.

[41] Grigorios A Pavliotis. Stochastic processes and applications: diffusion processes, the Fokker-Planck and Langevin equations, volume 60. Springer, 2014.

[42] MS Pinsker. Information and information stability of random quantities and processes. Holden-Day, 1964.

[43] Maxim Raginsky, Alexander Rakhlin, and Matus Telgarsky. Non-convex learning via stochastic gradient Langevin dynamics: a nonasymptotic analysis. In Conference on Learning Theory, pages 1674-1703. PMLR, 2017.

[44] Herbert Robbins and Sutton Monro. A stochastic approximation method. The annals of mathematical statistics, pages 400-407, 1951.

[45] Filippo Santambrogio. Optimal transport for applied mathematicians. Birkäuser, NY, $55(58-63): 94,2015$.

[46] Samuel Smith, Erich Elsen, and Soham De. On the generalization benefit of noise in stochastic gradient descent. In International Conference on Machine Learning, pages 9058-9067. PMLR, 2020.

[47] Samuel L Smith, Benoit Dherin, David GT Barrett, and Soham De. On the origin of implicit regularization in stochastic gradient descent. arXiv preprint arXiv:2101.121\%6, 2021.

[48] Michel Talagrand. A new isoperimetric inequality and the concentration of measure phenomenon. In Geometric aspects of functional analysis, pages 94-124. Springer, 1991.

[49] Max Welling and Yee W Teh. Bayesian learning via stochastic gradient Langevin dynamics. In Proceedings of the 28th international conference on machine learning (ICML-11), pages 681-688. Citeseer, 2011.

[50] Lei Wu, Chao Ma, et al. How SGD selects the global minima in over-parameterized learning: A dynamical stability perspective. Advances in Neural Information Processing Systems, 31, 2018.

[51] Yuchen Zhang, Percy Liang, and Moses Charikar. A hitting time analysis of stochastic gradient Langevin dynamics. In Conference on Learning Theory, pages 1980-2022. PMLR, 2017.

[52] Liu Ziyin, Botao Li, James B Simon, and Masahito Ueda. SGD with a constant large learning rate can converge to local maxima. arXiv preprint arXiv:2107.11774, 2021.

[53] Difan Zou, Pan Xu, and Quanquan Gu. Faster convergence of stochastic gradient Langevin dynamics for non-log-concave sampling. In Uncertainty in Artificial Intelligence, pages 1152-1162. PMLR, 2021.

