# Limit Behavior Of The Invariant Measure For Langevin Dynamics

## Gerardo Barrera

Abstract. **In this manuscript, we consider the Langevin dynamics on** R
d **with an overdamped vector field**
and driven by multiplicative Brownian noise of small amplitude √ǫ, ǫ > **0. Under suitable assumptions on**
the vector field and the diffusion coefficient, it is well-known **that it possesses a unique invariant probability**
measure µ ǫ. As ǫ **tends to zero, we prove that the probability measure** ǫ d/2µ ǫ(
√ǫdx**) converges in the**
p-Wasserstein distance for p ∈ [1, **2] to a Gaussian measure with zero-mean vector and non-degenerate**
covariance matrix which solves a Lyapunov matrix equation. **Moreover, the error term is estimated. We**
emphasize that generically no explicit formula for µ ǫ**can be found.**

## 1. **Introduction**

arXiv:2006.06808v3 [math.PR] 26 Jan 2022 1.1. The overdamped Langevin dynamics. **Random dynamical systems arise in the modeling of a (realistic) physical system subject to noise perturbations from its surrounding environments or from intrinsic**
uncertainties associated with the system. The Langevin dynamics was introduced by P. Langevin in 1908 in his celebrated article Sur la th´eorie du mouvement brownien, **C. R. Acad. Sci. Paris 146, pp. 530–533. It is** perhaps one of the most popular models in molecular systems. For details about the history of the Langevin equation, see [31]. For a phenomenological treatment, we recommend the monography [7].

In the last decades, there have been many applications of Markov chain Monte Carlo methods to complex systems in Computer Science and Statistical Physics. Since sampling high-dimensional distributions is typically a difficult task, the use of stochastic equations for sampling has **become important in many applications**
such as artificial intelligence and Bayesian algorithms. Stochastic algorithms based on Langevin equations have been proposed to simulate and improve the rate of convergence to limiting distributions. For further details we refer to [8], [11], [13], [14], [19], [24], [35] and the references therein.

Differential equations subject to small noise perturbations are one of the classic directions of modern mathematical physics. Let ǫ ∈ (0, 1] be a parameter that measures the perturbation strength and **let (**Bt)t≥0 be a standard Brownian motion on R
d**. For any (deterministic)** x ∈ R
d **we consider the unique strong solution**
(Xǫ t
(x))t≥0 **of the following stochastic differential equation (SDE for short) on** R
d
(1.1) dXǫ t(x) = −F(Xǫ t(x))dt +
√ǫσ(Xǫ t(x))dBt **for any** t ≥ 0, Xǫ 0
(x) = x, where the vector field F ∈ C2(R
d, R
d) and the diffusion coefficient σ ∈ C2(R
d, R
d×d**) satisfy the following**
assumptions. We assume that 0d is a fixed point for F, i.e., F(0d) = 0d **and the following hypotheses for** F.

Bakry–Emery condition: ´ there exists a positive constant δ **such that**
(A) hF(x1) − F(x2), x1 − x2i ≥ δkx1 − x2k 2for any x1, x2 ∈ R
d, where h·, ·i **denotes the standard inner product on** R
d and k · k **denotes the standard Euclidean norm on** R
d.

Exponential growth condition: there exist positive constants c0 and c1 **satisfying**
(B) kD2F(x)k ≤ c0e c1kxk 2**for any** x ∈ R
d, where D2F **denotes the second order derivative of** F.

For the diffusion coefficient σ **we assume the following standard hypotheses.**
Lipschitz continuity: there exists a positive constant ℓ **such that**

$\frac{1}{4}$  . 

(C) kσ(x) − σ(x0)kF ≤ ℓkx − x0k for all **x, x**0 ∈ R

$$x,x_{0}\in\mathbb{R}^{d},$$

where k · kF **denotes the Frobenius norm.**
Ellipticity: there is a positive constant κ **such that**

(D) hσ(x0)σ
$\langle\sigma(x_{0})\sigma^{*}(x_{0})x,x\rangle\geq\kappa\|x\|^{2}$ for all $x,x_{0}\in\mathbb{R}^{d}$,
where ∗ **denotes the transpose operator.**
Hypotheses (A) and (C**) imply the monotone condition (3.14) given in Theorem 3.5, p. 58 in [26], and**
hence the existence and uniqueness of the unique strong solution of (1.1). Along this manuscript, let (Ω, F, P)
be a complete probability space where (1.1) is defined and denote by E **the expectation with respect to** P.

1.2. Invariant distribution. Existence of invariant measures for stochastic processes are an **important**
feature in probability theory and mathematical physics; and typically they are not so easy to describe explicitly. By Theorem 3.3.4, p. 91 in [22], it is not hard to verify that Hypotheses (A), (C) and (D**) yield**
the existence and uniqueness of an invariant (absolutely continuous with respect to the Lebesgue measure on R
d**) probability measure** µ ǫfor the stochastic dynamics (1.1). If in addition, F(x) = ∇V (x) + b(x**) and**
σ(x) = Id **for any** x ∈ R
d, where Id **is the identity matrix of dimension** d × d, V : R
d → R **is a scalar function**
and b : R
d → R
d**is a vector field which satisfies the divergence-free condition**

$\left(1.2\right)^{\frac{1}{2}}$
(1.2) X
$$\sum_{j=1}^{d}{\frac{\partial}{\partial x_{j}}}\left(b(x)\exp(-(^{2}/\epsilon)V(x))\right)=0\quad{\mathrm{~for~any~}}\quad x=(x_{1},\ldots,x_{d})\in\mathbb{R}^{d},$$
one can verify that exp(−(
2/ǫ)V (x))dx **is a stationary measure for the random dynamics (1.1). However, it**
might not be a probability measure. Under some appropriate assumptions on V for kxk ≫ **1, the unique**
invariant probability measure µ ǫ **of (1.1) is of the Gibbs type**

(1.3) µ
$$\mu^{\epsilon}(\mathrm{d}x)={\frac{\exp(-(^{2}/\epsilon)V(x))}{Z^{\epsilon}}}\mathrm{d}x$$
Zǫ
dx, where Zǫ**is the so-called partition function (normalizing constant). See for instance Chapter 2, Convergence**
of the Langevin process, p. 21-23 in [34]. Using the Laplace Method (Saddle-point Method), asymptotics as ǫ → 0
+ **for the density of** µ ǫ**can be carried out, see for instance [2] and [18].**
If we drop the free-divergence condition (1.2) and replace it by the transversal condition h∇V (x), b(x)i = 0 for all x ∈ R
d, in [33] for additive noise it is shown a beautiful expansion on ǫ **for the density of** µ ǫ**. However,**
this expansion requires smoothness of the so-called Freidlin–Wentzell quasipotential. The latter is a nontrivial mathematical problem since it is expressed by a variational principle. **Using calculus of variations, in [10] it** is shown various results about the smoothness of the quasipotential under the assumptions of smoothness, boundedness and ellipticity of the coefficients of (1.1). In Section 5 of [9] it is proved that the asymptotic expansion given in [33] remains valid in any open set in which the quasipotential is C
2**. For additive noise,**
and bounded and dissipative vector field F**, in [27], by way of Watanabe's theory and Malliavin calculus, an** asymptotic expansion of µ ǫ **has been proved. Later, in [28] it is shown that** µ ǫ**can be expanded in Wentzel–**
Kramers–Brillouin (W.K.B.) type, as ǫ → 0
+, in the set in which the quasipotential is of C∞**-class and**
each coefficient which appears in the expansion is of C∞**-class. More recently, in [6], using control theoretic**
methods, it is proved that µ ǫ(dx) ≈ exp(−V∗(x)/ǫ), ǫ ≪ 1, where V∗ **is characterized as the optimal cost of a**
deterministic control problem. Nevertheless, the control problem is not easy to solve explicitly.

In (1.1) we consider multiplicative noise, and no transverse condition on the vector field F **is assumed.**
Moreover, we do not need that the Gibbs measure (1.3) remains stationary, and no smoothness on µ ǫ and the Freidlin–Wentzell quasipotential are needed. We remark that generically **it is not possible to compute** an explicit formula for µ ǫ.

1.3. Informal result. **Our goal is to prove that the probability** ǫ d/2µ ǫ(
√ǫdx**) has a Gaussian shape in the**
small noise limit. To be more precise, under Hypotheses (A), (B), (C) and (D**), it follows that the probability**
measure (1.4) ǫ d/2µ ǫ(
√ǫdx)
converges in the p-Wasserstein (p ∈ [1, 2]) to a Gaussian N **distribution with zero-mean vector and covariance**
matrix given by the unique solution X **of the Lyapunov matrix equation**
(1.5) DF(0d)X + X(DF(0d))∗ = σ(0d)(σ(0d))∗.

Generically, it is hard to find an explicit formula for the solution of the (1.5). Nevertheless, it can be estimated via numerical algorithms, see for instance [4], [32] and the references therein. More precisely, it is shown an asymptotic expansion (in the Wasserstein distance) of µ ǫ **as follows**

(1.6) J
ǫ
$$\frac{\mathcal{J}^{\epsilon}}{\sqrt{\epsilon}}=\mathcal{N}+\mathcal{O}(\sqrt{\epsilon})\quad\mathrm{~for~}\quad\epsilon\to0^{+},$$
where J
ǫ **denotes a random variable with law** µ ǫ.

We anticipate that the proof of (1.6) does not rely on explicit computations of the distribution µ ǫ**. It is**
based on the linearization of the nonlinear dynamics around the stationary point 0d**. It is not hard to see**
that the resulting linear process has the target Gaussian as invariant distribution. It is then necessary to control the difference between this linear process and the nonlinear dynamics. This is done using the so-called synchronous coupling techniques with the help of Hypotheses (A), (B) and (C). The proof of (1.6) is **purely**
dynamic and it does not require techniques as Malliavin calculus, large deviation **theory for SDEs as in [15],** smoothness of the quasipotential, smoothness of the density µ ǫ**, analysis of the infinitesimal generator or the**
W.K.B. expansion.

Quantitative bounds on the rate of convergence of Markov processes to their limiting distribution are an important and widely studied topic, particularly in the context of Markov chains, see for instance [12], [16], [25] and the references therein. We quantify **in the Wasserstein distance the implicit error term given** in (1.6). We point out that the critical regime analyzed in Section 5.1 of **[1] implies for additive noise the** total variation convergence of (1.4) to a Gaussian distribution. However, it seems hard to obtain bounds for the total variation error term, even under our assumptions on F and σ.

1.4. Wasserstein distance. Let P **be the set of probability measures in the measurable space (**R
d, B(R
d)),
where B(R
d) denotes the Borel σ**-algebra of** R
d. For p ≥ **1 we define**

$${\mathcal{P}}_{p}:=\left\{\mu\in{\mathcal{P}}:\int_{\mathbb{R}^{d}}\|x\|^{p}\mu(\mathrm{d}x)<\infty\right\},$$

the space of probability measures with finite p-moment. For any µ, ν ∈ P **we say that a probability measure**
π∗ **in the measurable space (**R
d × R
d, B(R
d × R
d)) is a coupling between µ and ν if the marginals of π∗ are µ and ν, that is, for any B ∈ B(R
d**) it follows that** π∗(B × R
d) = µ(B**) and** π∗(R
d × B) = ν(B). Let Π(**µ, ν**)
be the set of all coupling between µ and ν. For any µ, ν ∈ Pp, the Wasserstein distance of order p **between** µ and ν, Wp(µ, ν**), is defined by**

$${\mathcal{W}}_{p}(\mu,\nu):=\operatorname*{inf}\left\{\left(\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\|x-y\|^{p}\pi_{*}(\mathrm{d}x,\mathrm{d}y)\right)^{1/p}:\pi_{*}\in\Pi(\mu,\nu)\right\}.$$

Let X and Y **be two random vectors on** R
d defined on the probability space (Ω, F, P) with finite p**-moment.**
The Wasserstein distance of order p between X and Y , Wp(X, Y ), is defined by Wp(X, Y **) :=** Wp(PX, PY ), where PX and PY are the push-forward probability measures PX(B) := P(X ∈ B) and PY (B**) :=** P(Y ∈ B) for any B ∈ B(R
d). For short, we write Wp(X, Y ) in place of Wp(X, Y **). A remarkable property that we use**
along this manuscript is the following scaling property
(1.7) Wp(cX,cY ) = |c|Wp(X, Y **) for any** c ∈ R.

The Wasserstein distance metrizes the weak convergence in the space of probabilities with finite p**-moment.** It is a fundamental concept in optimal transport theory, probability theory and partial differential equations. The Wasserstein distance is a natural way to compare the law of two random variables X and Y **(even for** degenerate cases), where one variable is derived from the other by a small perturbation. For further details and properties of the Wassertein distance, we refer to the monographies [29] and [34].

1.5. Results. We denote by N (v, **Ξ) the Gaussian distribution in** R
d with vector mean v **and positive**
definite covariance matrix Ξ. Let Id be the identity d × d**-matrix. Given a matrix** A ∈ R
d×d**, denote by** A∗
the transpose matrix of A and denote by Tr(A**) the trace of** A.

The main result of this manuscript is the following.

Theorem 1.1 (Gaussian W2**-approximation of the invariant measure** µ ǫ). **Assume Hypotheses** (A), (B),
(C) and (D) **are valid. Let** J
ǫ**be a random vector on** R
d **with distribution** µ ǫ**. Then there exists a positive**
constant K := K(δ, ℓ, d, c0, σ(0d)) such that for any ǫ ∈ (0, ǫ∗) **with**

$$\epsilon_{*}=\operatorname*{min}\left\{{\frac{\delta}{8c_{1}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}\cdot d^{2}}},{\frac{\delta}{2\ell^{2}}}\right\}$$

it follows that

(1.8) W2
$${\mathcal{W}}_{2}\left({\frac{{\mathcal{I}}^{\epsilon}}{\sqrt{\epsilon}}},{\mathcal{N}}\right)\leq K{\sqrt{\epsilon}},$$
where N **denotes the Gaussian distribution on** R
d with zero-mean vector and covariance matrix Σ **which is**
the unique solution of the Lyapunov matrix equation
(1.9) DF(0d**)Σ + Σ(**DF(0d))∗ = σ(0d)(σ(0d))∗.

Using the coupling approach, rates of convergence of the time evolution to equilibrium in the Wasserstein distance for Langevin processes are given in [13] for the underdamped dynamics and in [14] for the overdamped dynamics. In [5], linking functional inequalities with the dissipation to ensure a spectral gap, it is shown that the solution of the Fokker–Planck equation converges in Wasserstein distance of order 2 to its equilibrium as the time evolution goes by. However, the authors in [5], [13] and [14] do not study small random perturbations of dynamical systems, and hence, an asymptotic analysis for the invariant measure is not needed there.

The proof of Theorem 1.1 does not rely on explicit computations of µ ǫ **neither on explicit formula of**
the Wasserstein distance of order 2 between Gaussian distributions. The Itˆo formula with the help of (A)
and (C) implies that the p-moments are bounded recursively as a function of moments of order p and p − 2.

Consequently, by an analogous reasoning (but more involved) one can see that the proof of Theorem 1.1 can be adapted for any L
p**-Wasserstein distance for any** p ≥ 1.

Remark 1.1 (A comment about total variation convergence for additive noise). We stress that (1.8) **does not**
imply directly any convergence of the corresponding densities. In other words, the following approximation of densities (1.10) µ ǫ(dx) ≈ ǫ
−d/2N (dx/
√ǫ) for ǫ ≪ 1.

cannot be straightforward deduced from (1.8). For additive noise, that is, σ(x) = Id **for all** x ∈ R
d, using Theorem 5.1, p. 30 in [21] **(implicitly the celebrated Cameron–Martin–Girsanov Theorem) it is shown**
that (1.10) is valid, see Proposition 3.7, p. 1190 in [3] **for further details. However, no rate of convergence** is given there. Multiplicative noise is implicitly discussed in p. 123 of [9].

Remark 1.2 (A word about the constant K). The constant K given in the right-hand side of (1.8) **can be**
taken as

$$K=\frac{96c_{0}d^{2}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}}{\delta^{2}}+\frac{2\ell C_{0}^{1/2}}{\delta}\quad\quad\mathrm{with}\quad\quad C_{0}=2\mathrm{Tr}((\sigma(0_{d}))^{*}\sigma(0_{d})).$$

We emphasize that the error term K
√ǫ **may not be optimal**
Remark 1.3 **(Existence, uniqueness and integral representation for the covariance matrix Σ)**. By (A) and (D), Theorem 1, p. 443 of [23] implies that (1.9) **possesses a unique solution. Moreover, Theorem 3,**
p. 414 of [23] **yields the integral representation for its solution**

$\blacksquare$
$$\Sigma=\int_{0}^{\infty}e^{-D F(0_{d})s}\sigma(0_{d})(\sigma(0_{d}))^{*}e^{-(D F(0_{d}))^{*}s}\mathrm{d}s.$$
As a consequence of Theorem 1.1 we have the following corollaries.

Corollary 1.1 (Wp convergence for p ∈ [1, 2]). Assume Hypotheses (A), (B), (C) and (D) **are valid. Let**
J
ǫ, N , K and ǫ∗ be as in Theorem 1.1. For any p ∈ [1, 2] **it follows that**

$\mathcal{O}\left(\mathcal{N}\right)$, $\mathcal{N}$ and $\epsilon$ be as in Theorem 1.1.1. For any $p\in[1,2]$ we suppose that  $$\mathcal{W}_{p}\left(\frac{\mathcal{J}^{\epsilon}}{\sqrt{\epsilon}},\mathcal{N}\right)\leq K\sqrt{\epsilon}\quad\text{for all}\quad\epsilon\in(0,\epsilon_{*}).$$  Proof.: The proof follows immediately by the Holder inequality and (1.8).  
Corollary 1.2 (Concentration). Assume Hypotheses (A), (B), (C) and (D) **are valid. Let** J
ǫ**be as in**
Theorem 1.1. For any p ∈ [1, 2] and β < 1/2 **it follows that**

$\square$
$$\operatorname*{lim}_{\epsilon\rightarrow0^{+}}\frac{1}{\epsilon^{\beta}}\mathcal{W}_{p}(\mathcal{I}^{\epsilon},0_{d})=0.$$
$\mathcal{V}_p$, Property (1.7) and Theorem 1.1. 
$\boxed{\text{}}$
Proof. The proof follows by the triangle inequality for Wp**, Property (1.7) and Theorem 1.1.** 
The study of the concentration of the equilibrium measure has been **of considerable interest to physicists.**
Theorem 1 in [6] implies that J
ǫ → 0d as ǫ → 0
+ in distribution sense. However, it does not say anything about its rate of convergence as Corollary 1.2. Results about **quantitative concentration of stationary**
measures on attractors and repellers for multiplicative noise are given in [17] and [20].

The rest of the manuscript is organized as follows. Section 2 describes the outline of the proof for the main Theorem 1.1. Section 3 is devoted to the proofs of the results skipped in Section 2. Finally, in the Appendix A we provide polynomials and exponential moments estimates for the Ornstein–Uhlenbeck process that we use in Section 3.

$$t\geq0,$$
for any $t\geq0$.  
$\text{10D}$  . 

## 2. **Outline Of The Proof**

2.1. Linear diffusion approximation. Due to the dissipativity condition (A**), the nonlinear random dynamics (**Xǫ t
(x))t≥0 is pushed-back to the origin with high probability. In a neighbourhood **of the origin, it**
is reasonable that an Ornstein–Uhlenbeck process helps us to understand (Xǫ t
(x))t≥0 **for large times. Let**
(Yt(x))t≥0 **be the unique strong solution of the following linear SDE**

(2.1) dY
$$\left\{\begin{array}{c}{{\mathrm{d}Y_{t}^{\varepsilon}(x)=-,}}\\ {{Y_{0}^{\varepsilon}(x)=x,}}\end{array}\right.$$
t(x) = −DF(0d)Y
ǫ
t(x)dt +
√ǫσ(0d)dBt **for any** t ≥ 0,
where (Bt)t≥0 **is a standard Brownian motion on** R
d and DF(0d**) denotes the Jacobian matrix at the point**
0d**. The method of variation of parameters yields**
Y
ǫ
t(x) = e
−DF (0d)tx +
√ǫ e
−DF (0d)tZ t
0
$$-DF(0_d)t\int_{0}^{}\ e^{DF(0_d)s}\sigma(0_d)$$

```
(2.2) σ(0d)dBs **for any** t ≥ 0.
Formula (2.2) implies that for any t > 0, Y
                                           ǫ
                                          t
                                           (x) possesses Gaussian distribution with vector mean mt(x) :=

```

e−DF (0d)tx **and covariance matrix Σ**ǫ t
:= ǫΣt for any t ≥ 0, where (Σt)t≥0 **solves the following matrix**
differential equation

(2.3)  d
dtΣt = −DF(0d)Σt − Σt(DF(0d))∗ + σ(0d)(σ(0d))∗**for any** t ≥ 0,
$\left\{\begin{array}{l l}{\frac{\mathrm{d}}{\mathrm{d}t}\Sigma_{t}=-D F_{t}}\\ {\Sigma_{0}=0_{d\times d\times t}}\end{array}\right.$
where 0d×d is the d-squared zero matrix. We refer to Section 3.7 in [30] for further details. By (A**) one can**
easily see that the eigenvalues of DF(0d) are contained in the set {z ∈ C : ℜ(z) ≥ δ}**. As a consequence, we**
have
kmt(x)k ≤ e
−δtkxk → 0 as t → ∞.
If in addition, we assume that σ(0d**) is invertible, Lemma A.2 in Appendix A implies**

$$\mathrm{for~any}\quad t\geq0,$$
$\frac{1}{2}$  3. 

kΣt − ΣkF ≤ kΣk 2 F e
−2δt → 0 as t → ∞,
where Σ is the unique solution of the matrix Lyapunov equation (1.9). **Therefore, the limiting distribution** of Y
ǫ t(x) is a Gaussian law with zero-mean vector and positive definite covariance matrix ǫ**Σ. Moreover,**
Proposition 3.5 in [30] implies that N (0d, ǫ**Σ) is the unique invariant probability measure for the dynamics**
given by (2.1).

2.2. Disintegration. For short we write N in a place of N (0d, **Σ). Recall that** J
ǫ **denotes a random vector**
on R
d **with distribution** µ ǫ. Let t ≥ **0 and** x0 ∈ R
d. The triangle inequality for the distance W2 **yields**
W2J
ǫ,
√ǫN≤ W2 (J
ǫ, Xǫ t(x0**)) +** W2 (X
ǫ t(x0), Y ǫ t(x0**)) +** W2Y
ǫ t(x0),
√ǫN
(2.4) .

Since µ ǫ**is invariant for the dynamics (1.1), for any** t ≥ 0, Xǫ t(J
ǫ**) has distribution** µ ǫ**. By disintegration,**
the first-term of the right-hand side of (2.4) can be estimated as follows

$$\mathcal{W}_{2}\left(\mathcal{J}^{\epsilon},X_{t}^{\epsilon}(x_{0})\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(x_{0})\right)\mu^{\epsilon}(\mathrm{d}x).$$
(2.5) (dx).
Analogously,

Analogously,  $$\mathcal{W}_{2}\left(\sqrt{\epsilon}\mathcal{N},Y_{t}^{\epsilon}(x_{0})\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x),Y_{t}^{\epsilon}(x_{0})\right)\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x),\tag{2.6}$$  where $\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x)$ denotes the density of $\sqrt{\epsilon}\mathcal{N}$. Combining (2.4), (2.5) and (2.6) we obtain 
where $\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x)$ denotes the density of $\sqrt{\epsilon}\mathcal{N}$. Combining (2.4), (2.5) and (2.6) we ob  $$\mathcal{W}_{2}\left(\mathcal{J}^{\epsilon},\sqrt{\epsilon}\mathcal{N}\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(x_{0})\right)\mu^{\epsilon}(\mathrm{d}x)+\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x_{0}),Y_{t}^{\epsilon}(x_{0})\right)$$ $$+\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x),Y_{t}^{\epsilon}(x_{0})\right)\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x)$$  for any $t\geq0$ and $x_{0}\in\mathbb{R}^{d}$. In particular, for any $t\geq0$ we have 
for any $t\geq0$ and $x_{0}\in\mathbb{R}^{d}$. In particular, for any $t\geq0$ we have  $$\mathcal{W}_{2}\left(\mathcal{J}^{*},\sqrt{c}\mathcal{N}\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(X_{t}^{*}(x),X_{t}^{*}(0_{d})\right)t^{*}(dx)+\mathcal{W}_{2}\left(X_{t}^{*}(0_{d}),Y_{t}^{*}(0_{d})\right)$$ $$\quad+\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(Y_{t}^{*}(x),Y_{t}^{*}(0_{d})\right)\mathcal{N}(0_{d},c\Sigma)(dx).\tag{2.7}$$  In what follows, we provide the tools for estimating the right-hand side of (2.7). The following lemma allows us to couple two solutions of (1.1) starting in different initial conditions.  
Lemma 2.1 (Synchronous coupling I). Assume Hypotheses (A) and (C) are valid. Let **x, x**0 ∈ R
d**. Then**
W2 (X
ǫ t(x), Xǫ t(x0)) ≤ e
−(δ/2)tkx − x0k for all t ≥ 0, ǫ ∈ (0, δ/ℓ 2],
where δ > 0 is the dissipativity constant that appears in (A) and ℓ **is the Lipschitz constant that appears**
in (C)**. In particular,**
W2 (X
ǫ t(x), Xǫ t(0d)) ≤ e
−(δ/2)tkxk for all t ≥ 0, ǫ ∈ (0, δ/ℓ 2].

The following lemma provides second moment estimates for the marginals of the process (1.1) and also for its invariant probability measure µ ǫ.

Lemma 2.2 (Second moment estimates). Assume Hypotheses (A) and (C) **are valid. For any** x ∈ R
d we have E[kX
ǫ t(x)k 2] ≤ kxk 2e
−δt +
ǫC0 δfor all t ≥ 0, ǫ ∈ (0, δ/(2ℓ 2)],
where δ > 0 is the dissipativity constant that appears in (A), ℓ **is the Lipschitz constant that appears in** (C)
and C0 = 2Tr((σ(0d))∗σ(0d))**. In addition,**

(2.8) Z
$$\int_{\mathbb{R}^{d}}\|x\|^{2}\mu^{\epsilon}(\mathrm{d}x)\leq{\frac{\epsilon C_{0}}{\delta}}\quad{\mathrm{~for~all~}}\quad.$$
δ**for all** ǫ ∈ (0,
δ/(2ℓ
2)].

The next lemma is crucial in our argument. Due to the contracting nature of the dynamics, the random dynamics around zero, (Xǫ t
(0d))t≥0**, can be approximated from its linearization (**Y
ǫ t
(0d))t≥0.

Lemma 2.3 (Synchronous coupling II). Assume Hypotheses (A), (B), (C) and (D) **are valid. Then there**
exists a positive constant C := C(δ, ℓ, d, c0, σ(0d)) such that for any ǫ ∈ (0, ǫ∗) **with**

$\downarrow\downarrow$ . 
$\equiv$ $\mathcal{L}$
$$\epsilon_{*}:=\operatorname*{min}\left\{{\frac{\delta}{8c_{1}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}\cdot d^{2}}},{\frac{\delta}{2\ell^{2}}}\right\},$$
Gaussian approximation 7 and for all t ≥ 0 **we have**
W2 (X
ǫ t(0d), Y ǫ t(0d)) ≤ Cǫ, where δ > 0 is the dissipativity constant that appears in (A), c0, c1 **are the positive constants that appear**
in (B) and ℓ **is the Lipschitz constant that appears in** (C).

We point out that the constant C **can be taken as**

$$C=\frac{48c_{0}d^{2}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}}{\delta^{2}}+\frac{\ell C_{0}^{1/2}}{\delta}.$$

The latter is deduced from (3.17). Recall that Σ is the solution of (2.3). Since for any t ≥ 0, Y
ǫ t(N (0d, ǫΣt))
has distribution N (0d, ǫ**Σ), an analogous reasoning used in the proofs of Lemma 2.1 and Lemma 2.2 implies**
the following lemma.

Lemma 2.4 (Synchronous coupling III). Assume Hypotheses (A) and (C) **are valid. For any** x ∈ R
dit follows that W2 (Y
ǫ t(x), Y ǫ t(0d)) ≤ e
−(δ/2)tkxk for all t ≥ 0, ǫ ∈ (0, δ/ℓ 2],
where δ > 0 is the dissipativity constant that appears in (A) and ℓ **is the Lipschitz constant that appears**
in (C). In addition, assume that σ(0d) **is invertible. Then it follows that**

(2.9) Z
$$\int_{\mathbb{R}^{d}}\|x\|^{2}{\mathcal{N}}(0_{d},\epsilon\Sigma)(\mathrm{d}x)\leq\epsilon d\|\Sigma^{1/2}\|_{\mathrm{F}}^{2}.$$
For simplicity we assume that σ(0d**) is invertible in Lemma 2.4. Actually, it is not needed to obtain an**
estimate such as (2.9). Nevertheless, it is enforced to define the so-called generalized Gaussian distribution with degenerate covariance matrix and hence the notion of Moore–Penrose pseudoinverse is required. The assumption that σ(0d**) is invertible can be removed and (2.8) in Lemma 2.4 remains valid replacing** µ ǫ by the law of N (0d, ǫΣ).

In the sequel, we stress the fact that Theorem 1.1 is just a consequence of what we have already stated up to here.

Theorem 1.1. By (2.7), Lemma 2.1, Lemma 2.2, Lemma 2.3 and Lemma 2.4 we have (2.10) W2J ǫ, √ǫN≤ rǫC0 δe −(δ/2)t + Cǫ + qǫdkΣ 1/2k 2 F e −(δ/2)t for any t ≥ 0 and ǫ ∈ (0, ǫ∗]. Due to (1.7), (2.10) implies W2 J ǫ √ǫ , N  ≤ rC0 δ e −(δ/2)t + C √ǫ + qdkΣ 1/2k 2 F e −(δ/2)t for any t ≥ 0 and ǫ ∈ (0, ǫ∗]. The cunning choice 2
$$t_{\epsilon}=\operatorname*{max}\left\{{\frac{1}{\delta}}\ln\left({\frac{4C_{0}}{\delta C^{2}\epsilon}}\right),{\frac{1}{\delta}}\ln\left({\frac{4d\|\Sigma^{1/2}\|_{\mathrm{F}}^{2}}{C^{2}\epsilon}}\right)\right\}$$
$$\mathrm{yields}$$
 Theorem 1.1.$\square$
which concludes Theorem 1.1. 

$${\mathcal{W}}_{2}\left({\frac{{\mathcal{I}}^{\epsilon}}{\sqrt{\epsilon}}},{\mathcal{N}}\right)\leq2C{\sqrt{\epsilon}},$$
$\square$
 $\;3.\;$ Proofs  . 
In this section, we give the proofs of Lemma 2.1, Lemma 2.2 and Lemma **2.3. Along their proofs, we use**
several times the celebrated Gr¨onwall inequality. We state it here as a lemma for the sake of completeness.

8 **Invariant probability measure**
Lemma 3.1 (Gr¨onwall's inequality). Let T > 0 be fixed, g : [0, T ] → R **be a** C
1-function and h : [0, T ] → R
be a C
0**-function. Assume that**
d dt g(t) ≤ −ag(t) + h(t) for any t ∈ [0, T ],
where a ∈ R, and the derivative at 0 and T **are understood as the right and left derivatives, respectively. Then**
g(t) ≤ e
−atg**(0) +** e
−at Z t 0 e ash(s)ds for any t ∈ [0, T ].

3.1. The synchronous coupling I. For any **x, x**0 ∈ R
d**, let (**Xǫ t
(x))t≥0 **and (**Xǫ t
(x0))t≥0 **be the solutions**
of (1.1) with initial conditions x and x0**, respectively. In the sequel, we consider the so-called synchronous**
coupling, i.e., both processes (Xǫ t(x))t≥0 **and (**Xǫ t(x0))t≥0 **have the same driving noise (**Bt)t≥0.

Lemma 2.1. **By the Itˆo formula we have**
dkXǫ t
(x)−Xǫ t
(x0)k 2 = −2hXǫ t
(x) − Xǫ t
(x0), F(Xǫ t
(x)) − F(Xǫ t
(x0))idt
+ ǫ **Tr[(**σ(Xǫ t(x)) − σ(Xǫ t(x0)))∗(σ(Xǫ t(x)) − σ(Xǫ t(x0**)))]d**t
+ 2√ǫhX
ǫ t(x) − X
ǫ t(x0),(σ(X
ǫ t(x)) − σ(X
ǫ t(x0**)))d**Bti.

By (C**) we have**
Tr[(σ(Xǫ t(x)) − σ(Xǫ t(x0)))∗(σ(Xǫ t(x)) − σ(Xǫ t(x0**)))]** ≤ ℓ 2kXǫ t(x) − Xǫ t(x0)k 2
(3.1) . A localization argument with the help of (A**) and (3.1) implies**
d dt E[kXǫ t
(x) − Xǫ t
(x0)k 2] ≤ −2δE-kXǫ t
(x) − Xǫ t
(x0)k 2+ ǫℓ2 E-kXǫ t
(x) − Xǫ t
(x0)k 2
≤ −(2δ − ǫℓ2)E-kXǫ t
(x) − Xǫ t
(x0)k 2 for all t ≥ **0. Since** E[kXǫ 0
(x) − Xǫ 0
(x0)k 2] = kx − x0k 2**, Lemma 3.1 yields**
E[kXǫ t(x) − Xǫ t(x0)k 2] ≤ e
−(2δ−ǫℓ2)tkx − x0k 2**for any** t ≥ 0.

Therefore, for any ǫ ∈ (0, δ/ℓ 2**] we have**
W2(Xǫ t
(x), Xǫ t
(x0)) ≤ e
−(δ/2)tkx − x0k for any **x, x**0 ∈ R
d, t ≥ 0.

3.2. Second moment estimates. **For any** x ∈ R
d**, let (**Xǫ t(x))t≥0 **be the solution of (1.1) with initial**
condition x.

Lemma 2.2. **In the sequel, we estimate** E[kXǫ t
(x)k 2]. The Itˆo formula and (A**) yield**
dkXǫ t
(x)k 2 = −2hXǫ t
(x), F(Xǫ t
(x))idt + ǫ **Tr[(**σ(Xǫ t
(x)))∗σ(Xǫ t
(x**))] +** Mǫ t
(x)
≤ −2δkXǫ t
(x)k 2dt + ǫ **Tr[(**σ(Xǫ t
(x)))∗σ(Xǫ t
(x**))]d**t + Mǫ t
(x),
where Mǫ t(x**) :=** h2
√ǫXǫ t(x), dBti for every t ≥ **0. Since**
Tr[(σ(Xǫ t
(x)))∗σ(Xǫ t
(x))] ≤ **2Tr[(**σ(Xǫ t
(x)) − σ(0d))∗(σ(Xǫ t
(x)) − σ(0d**))] + 2Tr((**σ(0d))∗σ(0d)),
Hypothesis (C**) implies**
Tr[(σ(X
ǫ t(x)))∗σ(X
ǫ t(x))] ≤ 2ℓ 2kX
ǫ t(x)k 2
(3.2) + C0, where C0 := 2Tr((σ(0d))∗σ(0d)). A localization argument with the help of (A**) and (3.2) implies**
d dt E[kX
ǫ t(x)k 2] ≤ −(2δ − 2ǫℓ2)E[kX
ǫ t(x)k 2] + ǫC0 **for any** t ≥ 0.

Since E[kXǫ 0
(x)k 2] = kxk 2**, for any** ǫ ∈ (0, δ/(2ℓ 2**)] Lemma 3.1 yields**
(3.3) E[kXǫ t
(x)k 2] ≤ e
−δtkxk 2 +
ǫC0 δ(1 − e
−δt) ≤ e
−δtkxk 2 +
ǫC0 δ Gaussian approximation 9 for any t ≥ **0 and** x ∈ R
d**. Following the same reasoning used on p. 39 in [3], it is not hard to see that (3.3)**

implies
 I am trying the same reasoning used on p: 00 in [0], for  $ \int_{\mathbb{R}^d}\|x\|^2\mu^\epsilon(\mathrm{d}x)\leq\frac{\epsilon C_0}{\delta}\quad$ for all $ \quad\epsilon\in(0,\delta/(2\ell^2)]$. 
3.3. The synchronous coupling II. We consider the solution of (1.1) with initial condition x = 0d,
(Xǫ
t
(0d))t≥0**. Let (**Y
ǫ
t
(0d))t≥0 **be as (2.1). In this section, we use the synchronous coupling between** Xǫ
t
(0d)
and Y
ǫ
t
(0d**), i.e., both processes (**Xǫ
t
(0d))t≥0 **and (**Y
ǫ
t
(0d))t≥0 **have the same driving noise (**Bt)t≥0.
Lemma 2.3. **In the sequel, we estimate** E-kXǫ
t
(0d) − Y
ǫ
t
(0d)k
2**. Note that** Xǫ
0
(0d) = Y
ǫ
0
(0d) = 0d**. Let**
∆ǫ
t(0d**) :=** Xǫ
t(0d) − Y
ǫ
t(0d), t ≥ **0. Then**
d∆ǫ
t
(0d) = − [F(Xǫ
t
(0d)) − F(Y
ǫ
t
(0d))] dt + [DF(0d)Y
ǫ
t
(0d) − F(Y
ǫ
t
(0d**))] d**t
+
√ǫ(σ(Xǫ
t
(0d)) − σ(0d))dBt.
Hence, the Itˆo formula reads
dk∆ǫ
t
(0d)k
2 = −2h∆ǫ
(0d), F(Xǫ
ǫ
By (C**) we have**
(3.4) Tr[(σ(X
ǫ
t(0d)) − σ(0d))∗(σ(X
ǫ
t(0d)) − σ(0d)] ≤ ℓ
2kX
ǫ
$$\Gamma=-2\langle\Delta_{t}^{\epsilon}(0_{d}),F(X_{t}^{\epsilon}(0_{d}))-F(Y_{t}^{\epsilon}(0_{d}))\rangle{\rm d}t$$ $$+2\langle\Delta_{t}^{\epsilon}(0_{d}),DF(0_{d})Y_{t}^{\epsilon}(0_{d})-F(Y_{t}^{\epsilon}(0_{d}))\rangle{\rm d}t$$ $$+\epsilon\,{\rm Tr}[(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))^{*}(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))]{\rm d}t$$ $$+2\sqrt{\epsilon}(\Delta_{t}^{\epsilon}(0_{d}),(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d})){\rm d}B_{t}).$$
t(0d)k
2.
A localization argument with the help of (A**), the Cauchy–Schwarz inequality and (3.4) implies**
d
dt
E[k∆ǫ t (0d)k 2] ≤ −2δE[k∆ǫ t (0d)k 2] + 2E[k∆ǫ t
(0d)**k · k**F(Y
ǫ t
(0d)) − DF(0d)Y
ǫ t
(0d)k] + ǫℓ2E[kXǫ t
(0d)k 2].

(3.5)

Differential inequality (3.5) and the Young inequality (for p **= 2) yield**
d
dt
E[k∆
ǫ
t(0d)k
2] ≤ −δE[k∆
ǫ
t(0d)k
2] + 1
δ
E[kF(Y
ǫ
t(0d)) − DF(0d)Y
ǫ
t(0d)k
2] + ǫℓ2E[kX
ǫ
t(0d)k
2].
By Lemma 2.2 we have
E[kXǫ
t
(0d)k
2] ≤
ǫC0
δfor all t ≥ 0, ǫ ∈ (0,
δ/(2ℓ
2)],
where C0 = 2Tr((σ(0d))∗σ(0d**)). Since ∆**ǫ
t(0d**) = 0, Lemma 3.1 implies**
E[k∆ǫ
t
(0d)k
2] ≤
1
δ
e
−δt Z t
0
e
δsE[kF(Y
ǫ
s
(0d)) − DF(0d)Y
ǫ
s
(0d)k
2]ds +
ǫ
2ℓ
2C0
δ
2
≤
1
δ
2sup
0≤s≤t
E[kF(Y
ǫ
s(0d)) − DF(0d)Y
ǫ
s(0d)k
2] + ǫ
2ℓ
2C0
δ
2
(3.6)
for all t ≥ **0 and** ǫ ∈ (0,
δ/(2ℓ
2)**]. Next, we estimate**
sup
0≤s≤t
E[kF(Y
ǫ
s
(0d)) − DF(0d)Y
ǫ
s
(0d)k
2].
Let $s\in[0,t]$. Recall that $F\in\mathcal{C}^{2}(\mathbb{R}^{d},\mathbb{R}^{d})$. Since $F(0_{d})=0_{d}$, The mean value then  $$F(Y_{s}^{\epsilon}(0_{d}))-F(0_{d})=\int_{0}^{1}DF(\theta_{1}Y_{s}^{\epsilon}(0_{d}))\mathrm{d}\theta_{1}\cdot Y_{s}^{\epsilon}(0_{d}),$$  where $DF$ denotes the derivative of $F$. Since $F(0_{d})=0_{d}$, we have 
$$F(Y_{s}^{\varepsilon}(0_{d}))-D F(0_{d})Y_{s}^{\varepsilon}(0_{d})=\int_{0}^{1}\left[D F(\theta_{1}Y_{s}^{\varepsilon}(0_{d}))-D F(0_{d})\right]\mathrm{d}\theta_{1}\cdot Y_{s}^{\varepsilon}(0_{d}).$$
10 **Invariant probability measure**
Applying The mean value theorem to (3.7) we deduce kF(Y
ǫ s(0d)) − DF(0d)Y
ǫ s(0d))k ≤ C
ǫ skY
ǫ s(0d)k 2
(3.8) ,

where  $$C_{s}^{\varepsilon}:=\int_{0}^{1}\int_{0}^{1}\|D^{2}F(\theta_{1}\theta_{2}Y_{s}^{\varepsilon}(0_{d}))\|{\rm d}\theta_{1}{\rm d}\theta_{2}$$  and $D^{2}F$ denotes the second order derivative of $F$. Note that  $$Y_{t}^{\varepsilon}(0_{d})=\sqrt{\varepsilon}\,Y_{t}\quad\mbox{for any}\quad t\geq0,\tag{3.9}$$  where $(Y_{t})_{t\geq0}$ is the unique strong solution of  $$\int\ {\rm d}Y_{t}=-DF(0_{d})Y_{t}{\rm d}t+\sigma(0_{d}){\rm d}B_{t}\quad\mbox{for any}\quad t\geq0,\tag{3.10}$$
$\downarrow$    . 
$\geq_{0}$ is the unique strong solution of  $$\left\{\begin{array}{l}\mathrm{d}Y_{t}=-DF(0_{d})Y_{t}\mathrm{d}t+\sigma(0_{d})\mathrm{d}B_{t}\quad\mbox{for any}\quad t\geq0,\\ Y_{0}=0_{d}.\end{array}\right.$$  $\mathrm{d}\left(\mathbf{R}\right)=1$
$\downarrow$ . 
By (3.9) and (B**) we have**
$\left(\alpha_{1}\right)\parallel_{\alpha}=\parallel\mathbf{D}^{2}\,\mathbf{F}(\theta,\theta-\mathbf{F}\mathbf{D})\parallel_{\alpha}<\alpha_{1}\theta_{1}^{2}$
$$(-1+2+\cdots+3)\,,\quad\Delta=-3\,,\quad\Delta=-3\,,$$

$\mathbf{a}=\mathbf{a}\cdot\mathbf{a}$. 

kD
2F(θ1θ2Y
ǫ s(0d))k = kD
2F(θ1θ2
√ǫYs)k ≤ c0e c1θ 2 1 θ 2 2 ǫkYsk 2.

Since θ1, θ2 ∈ [0, **1], we obtain**

(3.11) kD2F(θ1θ2Y
ǫ
s
(0d))k ≤ c0e
c1ǫkYsk
$\binom{2}{x}\left|1\right|^2$  4. 
Inequality (3.11) with the help of inequality (3.8) and equality (3.9) yields kF(Y
ǫ s
(0d)) − DF(0d)Y
ǫ s
(0d)k 2 ≤ c 2 0 e 2c1ǫkYsk 2ǫ 2kYsk 4
(3.12)
for any s ≥ 0, where (Yt)t≥0 **is the solution of (3.10). By item i) of Lemma A.1 in Appendix A it follows that**
(3.13) E[kYsk 8] ≤ 24C
4
∗**for any** s ≥ 0, where

(3.14) C∗ =
$$C_{*}={\frac{\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}\cdot d^{2}}{\delta}}$$
δ
and k · kF denotes the Frobenius norm. Due to (D), we note that C∗ > **0. Moreover, by item ii) Lemma A.1**
in Appendix A for ǫ ∈ (0,1
4c1C∗
) we have
(3.15) E[e 4c1ǫkYsk 2] ≤1 1 − 4ǫc1C∗
for any s ≥ 0.

Estimate (3.12) with the help of the Cauchy–Schwarz inequality, (3.13) and (3.15) implies

E[kF(Y
ǫ
s(0d)) − DF(0d)Y
ǫ
s(0d)k
2] ≤ ǫ
2c
2
0
E[e
4c1ǫkYsk
2]E[kYsk
$$\left[{}^{\circ}\right]\,\right)\quad C(\delta,d,c_{0}$$

1/2C˜(**δ, d, c**0)ǫ
1 − 4ǫc1C∗
$$\epsilon^2\left(\frac{1}{1-4\epsilon c_1C_\star}\right)^{1/2}$$
for any s ≥ 0, ǫ ∈ (0,1 4c1C∗
), where C˜(δ, d, c0) = √24c 20C
2
∗**is a positive constant. Consequently, for** ǫ ∈
(0,1 4c1C
) we obtain

$$\sup_{0\leq s\leq t}\mathbb{E}[\|F(Y_{s}^{\epsilon}(0_{d}))-DF(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}]\leq\bar{C}(\delta,d,c_{0})\epsilon^{2}\left(\frac{1}{1-4ec_{1}C_{s}}\right)^{1/2}.$$  That if $\epsilon\in(0,\frac{1}{8\epsilon_{1}C_{s}})$, then $(1-4ec_{1}C_{s})\geq1/2$. Let $\epsilon_{*}:=\min\left\{\frac{1}{8\epsilon_{1}C_{s}},\frac{\epsilon}{2t^{2}}\right\}$. By (3.6) and 
$\mathbf{a}=\mathbf{a}\cdot\mathbf{a}$. 
Note that if ǫ ∈ (0,1 2	**. By (3.6) and (3.16) we have**
for all ǫ ∈ (0, ǫ∗**] and all** t ≥ 0

E
-kXǫ
t
(0d) − Y
ǫ
t
(0d)k
2≤
√2
δ
2
C˜(**δ, d, c**0)ǫ
2 +
ǫ
2ℓ
2C0
δ
$${\frac{\mathrm{e}^{-t}\ \ C0}{\mathrm{e}^{-2}}}.$$

$\bigstar||\bigstar||\bigstar||\bigstar$  . 
$$\biguplus\leq$$
As a consequence, for any ǫ ∈ (0, ǫ∗] and t ≥ **0 we have**
W2 (Xǫ t
(0d), Y ǫ t
(0d)) ≤
ǫ δ
(
√2C˜(δ, d, c0) + ℓ 2C0)
1/2 ≤
ǫ δ
(48c0C∗ + ℓC1/2 0
(3.17) ), where in the last inequality we use the subadditivity property of the root-map. Inequality (3.17) with the help of (3.14) implies the statement. 