# 

Lijun Wang* 1,2, Xiaodan Fan† 1, Hongyu Zhao‡ 2, and Jun S. Liu§ 3 1*Department of Statistics, The Chinese University of Hong Kong, Hong Kong SAR, China* 2*Department of Biostatistics, Yale University, New Haven, Connecticut, USA*
3*Department of Statistics, Harvard University, Cambridge, Massachusetts, USA*

## Abstract

A univariate continuous function can always be decomposed as the sum of a non-increasing function and a non-decreasing one. Based on this property, we propose a non-parametric regression method that combines two spline-fitted monotone curves. We demonstrate by extensive simulations that, compared to standard spline-fitting methods, the proposed approach is particularly advantageous in high-noise scenarios. Several theoretical guarantees are established for the proposed approach. Additionally, we present statistics to test the monotonicity of a function based on monotone decomposition, which can better control Type I
error and achieve comparable (if not always higher) power compared to existing methods.

Finally, we apply the proposed fitting and testing approaches to analyze the single-cell pseudotime trajectory datasets, identifying significant biological insights for non-monotonically expressed genes through Gene Ontology enrichment analysis. The source code implementing the methodology and producing all results is accessible at https://github.com/szcf-weiya/ MonotoneDecomposition.jl.

Keywords: Function Decomposition; Monotone B-splines; Curve Fitting; Test of Monotonicity.

arXiv:2401.06383v2 [stat.ME] 9 Apr 2024

## 1 Introduction

Suppose we have n pairs of observations (xi, yi), i = 1*, . . . , n*, with xi ∈ IRd, yi ∈ IR, independent and identically distributed (i.i.d.) according to an unknown probability distribution P(*X, Y* ).

Various methods exist for estimating the conditional expectation function f(x) = E(Y |X = x),
ranging from simple linear regressions (including ridge and lasso) to more sophisticated nonlinear techniques. Spline is one of the most popular methods, particularly when d = 1. Unlike existing methods, we aim to estimate the monotonic components of f(x) and then use their sum as an estimator for f(x). This is because any general function can be decomposed into the sum of an increasing function fup(x) and a decreasing function fdown(x) (a more formal proof is given in the Supplementary Material for self-contained).

The monotone decomposition idea has been exploited by Chipman et al. (2022) in their recent algorithm, where the monotone decomposition is incorporated into fitting monotone Bayesian additive regression trees (mBART). They found that fitting by monotone decomposition with mBART outperforms the corresponding BART algorithm proposed earlier in Chipman et al.

(2010). We here focus on the case of d = 1, and adopt B-spline basis functions to represent the monotone components,

$$f_{\mathrm{up}}(x)=\sum_{j=1}^{J_{u}}\gamma_{j}^{u}B_{j}^{u}(x)+\varepsilon_{u}\,,\qquad f_{\mathrm{down}}(x)=\sum_{j=1}^{J_{d}}\gamma_{j}^{d}B_{j}^{d}(x)+\varepsilon_{d}\,,$$

where the superscripts and subscripts "u" and "d" indicate for up (increasing) and *down* (decreasing), respectively. The monotonicity of each monotone component is ensured by the monotonicity of the coefficients (L. Wang et al., 2023), i.e.,

$$\gamma_{1}^{u}\leq\gamma_{2}^{u}\leq\cdots\leq\gamma_{J_{u}}^{u};\quad\gamma_{1}^{d}\geq\gamma_{2}^{d}\geq\cdots\geq\gamma_{J_{d}}^{d}\,.$$

This paper is organized as follows. In Section 2, we formulate monotone decomposition with cubic splines and establish properties of the solution, particularly for monotone functions. In Section 3, we propose the monotone decomposition with smoothing splines and establish similar properties and theoretical guarantees. In Section 4, we present simulation results to demonstrate how fitting via monotone decomposition can outperform the corresponding unconstrained fitting, particularly in high-noise scenarios. In Section 5, we propose statistics for testing monotonicity and, in Section 6, we demonstrate the power of the proposed method via simulations. In Section 7, we present the results of our analysis on single-cell pseudo-time trajectory datasets using the fitting and testing techniques based on monotone decomposition. Finally, we discuss the limitations and potential future work in Section 8.

## 2 Monotone Decomposition With Cubic Splines

Cubic splines are the most popular polynomial splines for practitioners. Presumably, cubic splines are the lowest-order splines for which the knot-discontinuity is not visible to the human eye, and there is scarcely any good reason to go beyond cubic splines (Hastie et al., 2009). On the other hand, although there are many equivalent bases for representing a spline function, the B-spline basis system developed by De Boor (1978) is attractive numerically (Ramsay & Silverman, 2005). Thus, we take the order-4 B-spline basis to represent cubic splines, under which the problem reduces to solving the following optimization problem:
min γ u,γd
∥y − Buγ u − Bdγ d∥2 ,
s.t. γ u 1 ≤ γ u 2 *≤ · · · ≤* γ u J; γ

$$\gamma_{1}^{d}\geq\gamma_{2}^{d}\geq\cdots\geq\gamma_{J}^{d}\,,$$
$\eqref{eq:walpha}$. 
where y = (y1*, . . . , y*n) is an n-vector of the responses (note that we use *round brackets* to denote column vectors), (Bu)ik = Bu k
(xi), k = 1*, . . . , J*u,(Bd)iℓ = Bd ℓ
(xi), ℓ = 1*, . . . , J*d are the matrices constructed by evaluating the B-spline basis at {xi}
n i=1, and γ u = (γ u 1
, . . . , γu J
), γd = (γ d 1
, . . . , γd J
)
are the coefficient vectors.

For simplicity, we consider Ju = Jd = J. Note that the knots for determining the B-spline basis are conventionally on the quantiles of x's, then the B-spline basis functions are also the same, Bu k = Bd ℓ
, so the above problem (1) becomes

$$\operatorname*{min}_{\gamma^{u},\gamma^{d}}\|\mathbf{y}-\mathbf{B}(\gamma^{u}+\gamma^{d})\|_{2}$$
 ## **Int1**  $\gamma^{\rm{tr}},\gamma^{\rm{G}}$

$${\mathrm{s.t.}}\ \gamma_{1}^{u}\leq\gamma_{2}^{u}\leq\cdots\leq\gamma_{J}^{u};\ \gamma_{1}^{d}\geq\gamma_{2}^{d}\geq\cdots\geq\gamma_{J}^{d}\,,$$
(2)
where Bij = Bj (xi), j = 1*, . . . , J*.

First of all, Proposition 1 establishes the equivalence between problem (2) with the corresponding unconstrained B-spline fitting.

Proposition 1. *Regardless of the component solutions* γˆ
u, γˆ
d*to problem* (2)*, the overall solution* γˆ
u + ˆγ d is equivalent to the unconstrained B-spline fitting, i.e., the least squares solution, γˆ
ls = arg min γ
∥y − Bγ∥2 = (B
T B)
−1B
T y . (3)
Specifically, γˆ
u + ˆγ d = ˆγ ls.

Note that the monotone components in (2) are not identifiable, since γ u + γ d = γ u + δ + γ d − δ ,
where δ is an arbitrary increasing sequence, δ1 *≤ · · · ≤* δJ . In other words, the decomposition for a general function is not unique since fup(x) + fdown(x) = fup(x) + h(x) + fdown(x) − h(x),
where h(x) is an arbitrary increasing function.

In order to have a unique decomposition, we consider the *closest* decomposition in some sense, such as the difference between two monotone components being the smallest in the L2norm. Thus, we consider imposing some discrepancy constraint on problem (2), as detailed in the following subsections, to help obtain a unique solution.

## 2.1 Discrepancy Constraint: A Motivating Example

Consider the simple function y = x 3, x ∈ [−1, 1], which may be decomposed as x 3 = {x 3 + h(x)} + {0 − h(x)} ≜ fup(x) + fdown(x),
where h(x) is an increasing function. If we set h(0) = 0, then it is easy to show that the magnitude of the difference between the two monotone components is lower-bounded by |x 3|, i.e.,
|x 3*| ≤ |*x 3 + 2h(x)|. (4)
Since it is unreasonable to have a decreasing component for a strictly increasing function, the ideal decomposition should correspond to h(x) = 0. Equation (4) suggests to us that such an ideal decomposition may be obtained by requiring the two monotone components to differ the least.

In light of this observation, we introduce the following *discrepancy constraint* for the two monotone components in the decomposition:

$$\|f_{\mathrm{up}}-f_{\mathrm{down}}\|_{2}\leq s,$$
∥fup − fdown∥2 ≤ s, (5)
where s ≥ 0 is a tuning parameter. The role of parameter s can be summarized as follows,

- if s → 0, then the solution is γ u = γ d = c1J , and hence ˆfup = ˆfdown = cB1J = c1n are constant functions;
- if s → ∞, then the problem reduces to be equivalent to the unconstrained B-spline fitting;
- a moderate s imposes some regularization, which is preferable for a better fitting.

## 2.2 General Functions

With the discrepancy constraint in (5), we can restate problem (2) as

$$\operatorname*{min}_{\mathbf{y}\in\mathcal{A}}\|\mathbf{y}-\mathbf{B}(\gamma^{-1}+\gamma^{-1})\|_{2}$$

min
$\gamma^{u},\gamma^{d}$  s.t. $\gamma^{u}_{1}\leq\gamma^{u}_{2}\leq\cdots\leq\gamma^{u}_{J}$; $\gamma^{d}_{1}\geq\gamma^{d}_{2}\geq\cdots\geq\gamma^{d}_{J}$  $\|{\bf B}(\gamma^{u}-\gamma^{d})\|_{2}\leq s$.  
∥y − B(γ
u + γ
d)∥2
$$(6)$$
$$\left(7\right)$$

$$({\mathfrak{s}})$$
Defining $\Upsilon\triangleq\{\gamma=(\gamma^{u},\gamma^{d})\in\mathbb{R}^{2J}:\gamma_{1}^{u}\leq\gamma_{2}^{u}\leq\cdots\leq\gamma_{J}^{u};\ \gamma_{1}^{d}\geq\gamma_{2}^{d}\geq\cdots\geq\gamma_{J}^{d}\}$ and  $$\mathbf{Z}\triangleq\begin{bmatrix}\mathbf{B}&\mathbf{B}\end{bmatrix},\quad\mathbf{W}\triangleq\begin{bmatrix}\mathbf{B}^{T}\\ -\mathbf{B}^{T}\end{bmatrix}\begin{bmatrix}\mathbf{B}&-\mathbf{B}\end{bmatrix},$$
we further rewrite problem (6) as

$$\operatorname*{min}_{\gamma\in\Upsilon}\;\|{\bf y}-{\bf Z}\gamma\|_{2}^{2}\qquad\mathrm{s.t.}\;\;\gamma^{T}{\bf W}\gamma\leq s^{2}\;.$$
γ∈Υ
2. (7)
It is more convenient to consider its Lagrangian form

$$\operatorname*{min}_{\gamma\in\Upsilon}\left[\|{\bf y}-{\bf Z}\gamma\|_{2}^{2}+\mu(\gamma^{T}{\bf W}\gamma-s^{2})\right]=\operatorname*{min}_{\gamma\in\Upsilon}\|{\bf y}-{\bf Z}\gamma\|_{2}^{2}+\mu\gamma^{T}{\bf W}\gamma\,,$$
2 + µγTWγ , (8)
where µ ≥ 0 is the Lagrange multiplier. By Lagrangian duality, there is a one-to-one correspondence between the constrained problem (7) and the Lagrangian form (8): for each value of s in the range where the constraint γ TWγ ≤ s 2is active, there is a corresponding value of µ that yields the same solution from the Lagrangian form (8). Conversely, the solution γˆµ to problem (8) solves the bound problem (7) with s 2 = ˆγ T
µWγˆµ. Some basic properties of the solution to problem (8)
are summarized in Proposition 2.

Proposition 2. Let γˆ = (ˆγ u, γˆ
d) *be the monotone decomposition to problem* (8) *(or problem* (13) discussed later).

(i) *There must be ties in the solution* γˆ
uor γˆ
d, i.e., there exists i or j *such that* γˆ
u i = ˆγ u i+1 or γˆ
d j = ˆγ d j+1.

(ii) *The mean values of two monotone components are equal,* 1 T Bγˆ
u = 1 T Bγˆ
d.

## 2.3 Monotone Functions

To delve deeper into the properties of the solution to problem (8), this section discusses the monotone decomposition of monotone functions. Without loss of generality, we consider increasing functions.

Proposition 3. Let γˆ = (ˆγ u, γˆ
d) *be the monotone decomposition to problem* (8)*. Suppose* γˆ
u + ˆγ dis increasing, then
(i) γˆ
d*is a vector with identical elements, i.e.,* γˆ
d = c1*, where the constant* c =

$$e\;t h e\;c o n s t a n t\;c={\frac{{\bf1}^{T}{\bf B}{\hat{\gamma}}^{u}}{n}};$$
_(ii) if there is no ties in $\hat{\gamma}^{u}$, i.e., $\hat{\gamma}^{u}_{1}<\hat{\gamma}^{u}_{2}<\ldots<\hat{\gamma}^{u}_{J}$, then_
$${\hat{\gamma}}^{u}={\frac{1}{\mu+1}}{\hat{\gamma}}^{\mathrm{ls}}+{\frac{\mu-1}{\mu+1}}c{\bf1}\,,$$
$$(9)$$
$\pm$). 
$${\mathfrak{I}}_{2}\leq$$
$$(10)$$
c1 , (9)
where the unconstrained B-spline solution γˆ
ls *is given in Equation* (3);

_._ 3. _if_ $\hat{\gamma}_{1}^{u}<\cdots<\hat{\gamma}_{k_{1}}^{u}=\cdots=\hat{\gamma}_{k_{2m}}^{u}<\cdots<\hat{\gamma}_{k_{2m-1}}^{u}=\cdots=\hat{\gamma}_{k_{2m}}^{u}<\cdots<\hat{\gamma}_{J}^{u}$_, where_ $1\leq k_{1}\leq k_{2}\leq\cdots\leq k_{2m-1}\leq k_{2m}\leq J$_, then_ $$\hat{\gamma}^{u}=\frac{1}{\mu+1}\mathbf{G}^{T}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}\mathbf{y}+\frac{\mu-1}{\mu+1}\mathbf{c}\mathbf{1}\,,$$ (10)
where G *is a block diagonal matrix with elements*

$$\left\{\mathbf{I}_{k_{1}-1},\mathbf{1}_{k_{2}-k_{1}+1}^{T},\ldots,\mathbf{I}_{k_{2m-1}-k_{2m-2}-1},\mathbf{1}_{k_{2m}-k_{2m-1}+1}^{T},\mathbf{I}_{J-k_{2m}}\right\}.$$

The above result (ii) *can be viewed as a special case when* k1 = k2 = J.

Intuitively, solution (9) can be viewed as a *shrinkage with offset* applied to the unconstrained B-spline fitting γˆ
ls, where 1 µ+1 is the shrinkage factor, and µ−1 µ+1 c1 is the offset. Even with the general matrix G, solution (10) also exhibits a similar *shrinkage with offset* pattern.

## 2.4 Mse Comparisons

To quantify the performance of fitting by monotone decomposition, consider the model

$$y=f(x)+\varepsilon\,,\quad\varepsilon\sim N(0,\sigma^{2})\,.$$
$\left(11\right)^{2}$
y = f(x) + ε , ε ∼ N(0, σ2). (11)
Define the mean squared error of the fitness, MSE(yˆ) = E∥f − B(ˆγ u + ˆγ d)∥
2 2, MSE(yˆ

$$\mathbb{E}({\hat{\mathbf{y}}}^{\mathrm{ls}})=\mathbb{E}\|\mathbf{f}-\mathbf{B}{\hat{\gamma}}^{\mathrm{ls}}\|_{2}^{2}\,,$$

where f = [f(x1)*, . . . , f*(xn)]T, and the expectations are taken over y ∼ N(f, σ2I). Proposition 4 shows that the fitting with monotone decomposition can achieve better performance, particularly in high-noise scenarios, when the underlying function is monotone.

Proposition 4. *Suppose the monotone decomposition* γˆ = (ˆγ u, γˆ
d) *satisfies that* γˆ
u + ˆγ d*is increasing. Let* G be a g × J matrix defined in Proposition 3 *such that* GT γˆ
u*is the sub-vector with unique elements. If*

$$\sigma^{2}>\frac{-C_{1}(J-\mathbb{E}g)+C_{2}(\mathbb{E}g+1)+\sqrt{\Delta}}{2[(J-\mathbb{E}g)(\mathbb{E}g+1)+(\mathbb{E}g-1)^{2}]}\,,$$
−C1(J − Eg) + C2(Eg + 1) + √∆
where

$$\begin{array}{l}{{C_{1}=\mathbf{f}^{T}\mathbf{A}\mathbf{f}-\frac{(\mathbf{I}_{n}^{T}\mathbf{f})^{2}}{n}\geq0\,,\quad C_{2}=\mathbf{f}^{T}(\mathbf{I}-\mathbf{A})\mathbf{f}\geq0}}\\ {{\mathbf{A}=\mathbb{E}[\mathbf{B}\mathbf{G}^{T}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}]}}\\ {{\Delta=\left[C_{1}(J-\mathbb{E}g)+C_{2}(\mathbb{E}g+1)\right]^{2}+4C_{1}C_{2}(\mathbb{E}g-1)^{2}\,,}}\end{array}$$

and the expectations are taken over y since G (and hence g) depends on y*, then there exists monotone* decomposition such that MSE(yˆ) < MSE(yˆ
ls).

Particularly, if we assume there is no ties in γˆ
u, i.e.,G ≡ I for different y*, then there always exists a* monotone decomposition such that MSE(yˆ) < MSE(yˆ
ls) *regardless of the noise level.*
The lower bound of σ 2in Proposition 4 might not be easy to evaluate. Nonetheless, the pivotal implication is that the monotone decomposition fitting can achieve better performance when the noise level is large enough. Extensive simulations in Section 4 agree with this argument. Moreover, although Proposition 4 is specifically established for monotone functions, the simulations show that the monotone decomposition fitting with cubic splines can also outperform the corresponding unconstrained cubic splines applied to random functions, particularly in high-noise scenarios.

## 3 Monotone Decomposition With Smoothing Splines

When dealing with cubic splines, it is typically necessary to ascertain both the number of basis functions, denoted as J, and the optimal placement of knots. In contrast, smoothing splines take a different approach by employing all unique data points as knots, thus bypassing the need for an optimization process to determine the knot placement and the number of knots required for B-spline basis functions.

With B-spline basis functions, the smoothing spline f(x) = PJ
j=1 γjBj (x) can be estimated as follows, γˆ
ss = arg min ∥y − Bγ∥
2 2 + λγT Ωγ , (12)
where {Ω}jk =RB′′
j
(s)B′′
k
(s)ds is called the roughness penalty matrix and λ > 0 is the penalty parameter. For this reason, smoothing splines are also referred to as penalized splines.

Imposing the roughness penalty γ T Ωγ = (γ u+γ d)
T Ω(γ u+γ d) = γ T Σγ on problem (8), where Σ ≜
Ω Ω
Ω Ω, we have the Lagrangian form of monotone decomposition with smoothing splines,

$$\operatorname*{min}_{\gamma\in\Upsilon}\|\mathbf{y}-\mathbf{Z}\gamma\|_{2}^{2}+\mu\gamma^{T}\mathbf{W}\gamma+\lambda\gamma^{T}\mathbf{\Sigma}\gamma\,.$$
2 + µγTWγ + λγT Σγ . (13)
For general functions, the properties in Proposition 2 also hold for the monotone decomposition with smoothing splines.

## 3.1 Monotone Functions

Likewise, we delve deeper into the characteristics of monotone decomposition with smoothing splines on monotone functions. The solutions demonstrate analogous *shrinkage with offset* patterns, akin to those observed in Proposition 3 for monotone decomposition with cubic splines, and the results are articulated in the following Proposition 5.

Proposition 5. Let γˆ = (ˆγ u, γˆ
d) *be the monotone decomposition to problem* (13)*. Suppose* γˆ
u + ˆγ dis increasing, then

$$(13)$$

(i) γˆ
d*is a vector with identical elements, i.e.,* γˆ
d = c1*, where the constant* c =
1 T Bγˆ
u n;
(ii) *if there is no ties in* γˆ
u*, i.e., the inequalities hold strictly,* γˆ
u 1 < γˆ
u 2 *< . . . <* γˆ
u J
, then

$$\hat{\gamma}^{\mu}=\frac{1}{1+\mu}\hat{\gamma}^{\mu\nu}\left(\frac{\lambda}{1+\mu}\right)-c((1+\mu)\mathbf{B}^{T}\mathbf{B}+\lambda\mathbf{\Omega})^{-1}((1-\mu)\mathbf{B}^{T}\mathbf{B}+\lambda\mathbf{\Omega})\mathbf{1}_{J}\tag{14}$$  _where $\hat{\gamma}^{\mu\nu}\left(\frac{\lambda}{1+\mu}\right)$ is the solution to smoothing spline with penalty parameter $\frac{\lambda}{1+\mu}$,_
$$\phi^{\rm u}\left(\frac{\lambda}{1+\mu}\right)=\left({\bf B}^{T}{\bf B}+\frac{\lambda}{1+\mu}{\bf\Omega}\right)^{-1}{\bf B}^{T}{\bf y}\,.$$ 3. _if_ $\zeta_{1}^{*}<\cdots<\zeta_{k_{1}}^{*}=\cdots=\zeta_{k_{2}}^{*}<\cdots<\zeta_{k_{2m-1}}^{*}=\cdots=\zeta_{k_{2m}}^{*}<\zeta_{J}^{*}$_, where_ $1\leq k_{1}\leq k_{2}\leq\cdots\leq k_{2m-1}\leq k_{2m}\leq J$_, then_
$$\begin{array}{c}{{\hat{\gamma}^{u}={\bf G}^{T}((1+\mu){\bf G B}^{T}{\bf B G}^{T}+\lambda{\bf G}\Omega{\bf G}^{T})^{-1}{\bf G B}^{T}{\bf y}-}}\\ {{c{\bf G}^{T}((1+\mu){\bf G B}^{T}{\bf B G}^{T}+\lambda{\bf G}\Omega{\bf G}^{T})^{-1}((1-\mu){\bf G B}^{T}{\bf B G}^{T}+\lambda{\bf G}\Omega{\bf G}^{T}){\bf1}_{g}\,,}}\end{array}$$

where G is defined in Proposition 3. The above result (ii) *can be viewed as a special case when* k1 = k2 = J.

For the no-tie solution (14), the *shrinkage* is on the ridge solution γˆ
ss(λ 1+µ
), but different from the constant *offset* in Equation (9), the offset c((1 +µ)BT B +λΩ)−1((1−µ)BT B +λΩ)1J depends on B and Ω.

## 3.2 Mse Comparisons

Based on model (11), for a comparative analysis of the fitting performance between monotone decomposition with smoothing splines and their smoothing splines counterparts, we further define the mean squared error for smoothing splines, MSE(yˆ
ss(λ)) = E∥f − Bγˆ
ss(λ)∥
2 2, where γˆ
ss(λ) is the solution to smoothing splines with penalty parameter λ.

Proposition 6 shows that employing monotone decomposition with smoothing splines can result in a superior mean squared error (MSE) compared to smoothing splines in the context of monotone functions, particularly when the noise level is sufficiently high. While the condition
(15) outlined in Proposition 6 may appear intricate, the simulations presented in the next section empirically substantiate this assertion. Furthermore, although the proposition is specifically formulated for monotone functions, the simulations show that the monotone decomposition applied to general functions can still achieve better performance in high-noise scenarios.

Proposition 6. Consider the smoothing spline with penalty parameter λ0*. Let* γˆ
ss(λ0) be the coefficient vector and denote its hat matrix by Q = B(BT B + λ0Ω)−1BT*. If*

$$\sigma^{2}>\frac{\mathbf{f}^{T}\mathbf{Q}(\mathbf{I}-\frac{\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}}{n})(\mathbf{I}-\mathbf{Q})\mathbf{f}}{\mathrm{tr}[(\mathbf{I}-\frac{\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}}{n})\mathbf{Q}^{2}]}\,,$$
, (15)
and suppose the monotone decomposition γˆ
u + ˆγ d*is increasing with no ties, then there exists a monotone* decomposition with parameters λ = λ0*/k, µ* = 1/k − 1, where k ∈ (0, 1), that achieves smaller mean squared error than MSE(yˆ
ss(λ0)).

$$(15)$$

## 4 Simulations For Fitting

In this section, we compare the performance of monotone decomposition using simulated examples. We generate data from function f with standard Gaussian noises, y = f(x) + N(0, σ2), x ∈ [−1, 1] .

To cover a diverse range of functional forms, we consider the following different types of functions.

- monotone functions: (i) polynomial function: y = x 3; (ii) exponential function: y = exp(x);
(iii) sigmoid function: y =1 1+exp(−5x)
.

- general functions: (i) unimodal: y = x 2; (ii) random functions, where the kernel can be Squared Exponential (SE), Rational Quadratic (RQ), Matérn (Mat) and Periodic (Rasmussen
& Williams, 2006). The numerical values appended to the kernel names in Tables 6 and 8 are the kernel parameters. For example, "Mat12" refers to the Matérn kernel with parameter ν = 1/2. The detailed procedure for generating a random function and a visualization of those curves can be found in the Supplementary Material.
To compare the performance of different methods, we adopt the mean squared fitting error
(MSFE), i.e., the residual sum of squares (RSS) divided by sample size, and the mean squared prediction error (MSPE),

$$\mathrm{MSFE}=\frac{1}{n}\sum_{i=1}^{n}\left(y_{i}-\hat{f}(x_{i})\right)^{2}\,,\qquad\mathrm{MSPE}=\frac{1}{N}\sum_{i=1}^{N}\left(\hat{f}(t_{i})-f(t_{i})\right)^{2}\,,$$

where ti = x(1) + (i − 1) ·
x(N)−x(1)
N, i = 1*, . . . , N* are equally spaced within the same range of x. Based on R = 100 replications, we estimate the mean MSFE and MSPE, together with their respective standard errors. To judge how significant the differences of MSPE between the fitting by monotone decomposition and the corresponding spline fitting, we consider
∆ = MSPE(Monotone decomposition) − MSPE(Spline fitting),
and denote the differences for each experiment as δi, i = 1*, . . . , R*. We report the p-value for the one-sided t-test H0 : ∆ = 0 versus H<
1: ∆ < 0 when Pn i=1 δi < 0 (or H>
1 P
: ∆ > 0 when n i=1 δi > 0). Besides, we also count the proportion for the fitting by monotone decomposition that achieves better performance, prop ≜
PR
i=1 \#{δi<0}
R.

## 4.1 Cubic Splines

Firstly, we consider the monotone decomposition with cubic splines. There are two tuning parameters: the number of basis functions J, and the Lagrange multiplier µ for the discrepancy between the two components. We adopt two strategies to optimize these parameters:
Tune µ **with fixed** J: We pick J, the tuning parameter for cubic splines, to be a minimizer of the cross-validation (CV) error, and then perform the monotone decomposition with cubic splines using the same J while tuning the parameter µ. Figure 1 shows an example, with J = 26 selected by CV. The left panel shows the leave-one-out CV error plotted against µ. The cubic spline fitting and the monotone decomposition fitting are displayed in the right panel, where the former achieves 0.102 MSPE, while the latter improves the MSPE to 0.066.

![8_image_0.png](8_image_0.png) 

Tune µ and J **simultaneously:** Instead of fixing J in the monotone decomposition procedure, we also use cross-validation to choose it, together with µ. Figure 2 displays an example of this process, where the left panel shows the CV error for each parameter pair (*µ, J*), and the right panel compares the fitting given the parameters that minimize the CV error to cubic spline fitting, whose parameter J is separately tuned by CV.

![8_image_1.png](8_image_1.png) 

Figure 2: Demo for monotone decomposition with cubic splines. The left panel shows the leaveone-out cross-validation error curve for each candidate pair (*µ, J*). The right panel shows the corresponding fitting curves, together with the truth and noised observations. The values in the parentheses are the mean squared prediction error.

Note that the right panels of Figures 1 and 2 depict the same training data. Although the MSPE of 0.079 by tuning (*µ, J*) simultaneously is slightly larger than the MSPE of 0.066 by tuning µ with fixed J, the monotone decomposition method achieves better performance than the cubic spline fitting, which has an MSPE of 0.102.

To provide comprehensive comparisons, we conducted 100 repetitions for 12 types of curves under different noise levels. The results by tuning µ and J simultaneously are summarized in Table 6, and the results by tuning µ with fixed J can be found in the Supplementary Material.

For some curves with small noises (e.g., σ = 0.2), such as y = x 3, the decomposition method performs slightly worse than cubic spline fitting. Nevertheless, the monotone decomposition always outperforms cubic spline fitting in higher noise (e.g., σ = 1.0) scenarios, regardless of the optimization strategies.

Table 1: Results for comparing the cubic splines and the fitting by monotone decomposition with CV-tuned (*µ, J*). The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error. The complete table with finer noise levels can be found in the Supplementary Material.

| curve          | σ          | MSFE               | MSPE               | p-value            | prop.              |                |      |
|----------------|------------|--------------------|--------------------|--------------------|--------------------|----------------|------|
| CubicSpline    | MonoDecomp | CubicSpline        | MonoDecomp         |                    |                    |                |      |
| x 2            | 1.0        | 9.71e+00 (7.3e-02) | 9.73e+00 (7.3e-02) | 7.50e+00 (3.1e-01) | 6.93e+00 (2.6e-01) | 5.91e-03 (**)  | 0.59 |
| x 3            | 1.0        | 9.65e+00 (7.4e-02) | 9.60e+00 (7.2e-02) | 7.63e+00 (3.5e-01) | 7.17e+00 (2.7e-01) | 2.21e-02 (*)   | 0.6  |
| exp(x)         | 1.0        | 9.57e+00 (5.9e-02) | 9.49e+00 (7.3e-02) | 7.56e+00 (2.8e-01) | 7.08e+00 (3.1e-01) | 3.59e-02 (*)   | 0.57 |
| sigmoid        | 1.0        | 9.51e+00 (8.5e-02) | 9.50e+00 (8.7e-02) | 7.33e+00 (3.2e-01) | 6.61e+00 (2.6e-01) | 1.45e-03 (**)  | 0.56 |
| SE-1           | 1.0        | 9.55e+00 (7.0e-02) | 9.51e+00 (7.6e-02) | 7.29e+00 (3.2e-01) | 6.62e+00 (2.7e-01) | 5.51e-03 (**)  | 0.63 |
| SE-0.1         | 1.0        | 9.29e+00 (8.5e-02) | 9.20e+00 (9.3e-02) | 1.44e+01 (2.6e-01) | 1.38e+01 (2.4e-01) | 5.93e-04 (***) | 0.7  |
| Mat12-1        | 1.0        | 9.79e+00 (8.9e-02) | 9.73e+00 (9.1e-02) | 1.26e+01 (2.9e-01) | 1.17e+01 (2.4e-01) | 9.31e-07 (***) | 0.68 |
| Mat12-0.1      | 1.0        | 1.04e+01 (1.3e-01) | 1.04e+01 (1.3e-01) | 2.07e+01 (2.4e-01) | 2.01e+01 (2.4e-01) | 1.85e-04 (***) | 0.73 |
| Mat32-1        | 1.0        | 9.62e+00 (8.2e-02) | 9.61e+00 (8.3e-02) | 9.01e+00 (3.5e-01) | 8.00e+00 (2.6e-01) | 1.46e-04 (***) | 0.56 |
| Mat32-0.1      | 1.0        | 9.62e+00 (1.1e-01) | 9.53e+00 (9.7e-02) | 1.68e+01 (2.5e-01) | 1.58e+01 (2.1e-01) | 4.67e-10 (***) | 0.72 |
| RQ-0.1-0.5     | 1.0        | 9.55e+00 (1.1e-01) | 9.50e+00 (1.2e-01) | 1.50e+01 (2.4e-01) | 1.44e+01 (2.6e-01) | 5.01e-03 (**)  | 0.68 |
| Periodic-0.1-4 | 1.0        | 9.41e+00 (1.2e-01) | 9.31e+00 (1.1e-01) | 1.72e+01 (3.0e-01) | 1.60e+01 (2.5e-01) | 2.03e-10 (***) | 0.63 |

## 4.2 Smoothing Splines

This section compares the fitting performance of monotone decomposition with smoothing splines to the fitting of the smoothing splines. There are two tuning parameters: the penalty parameter λ and the Lagrange multiplier µ for the discrepancy. We consider three strategies to optimize these parameters:

- Tune λ for smoothing splines first, then tune µ for the monotone decomposition with smoothing splines using the tuned λ;
- According to Proposition 6, tune λ for smoothing splines first, then tune the shrinkage factor k =1 1+µ for monotone decomposition with smoothing splines using penalty parameter λ/k;
- Simultaneously tune λ and µ for monotone decomposition with smoothing splines.
All strategies use cross-validation (CV) to determine the parameters. Specifically, we pick the tuning parameters that minimize the CV error.

For brevity, we only present the results using the third strategy in this section. Results based on the other two strategies can be found in the Supplementary Material. Figure 3 illustrates the simultaneous tuning of (*µ, λ*) using the same toy example presented in Figures 1 and 2. The smoothness penalty in smoothing splines results in fitted curves that are notably less wiggly compared to the curves fitted by cubic splines without such a penalty.

The results of 100 repetitive experiments are summarized in Table 8. We observe that the monotone decomposition consistently outperforms the corresponding smoothing splines. Moreover, the monotone decomposition with CV-tuned (*λ, µ*) is more likely to obtain better performance

![10_image_0.png](10_image_0.png) 

Figure 3: Demo for monotone decomposition with smoothing splines. The left panel shows the leave-one-out cross-validation error heatmap for each candidate pair(*µ, λ*). The right panel shows the corresponding fitting curves, together with the truth and the noised observations. The values in the parentheses are the mean squared prediction errors.

compared to the other two strategies. Regardless of the optimization strategies employed, all results consistently show that the monotone decomposition fitting can achieve a good performance, especially in high-noise scenarios.

Table 2: Results for comparing the smoothing splines with CV-tuned λ and the fitting by monotone decomposition with CV-tuned (*λ, µ*). The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error. The complete table with finer noise levels can be found in the Supplementary Material.

| curve          | σ          | MSFE               | MSPE               | p-value            | prop.              |                |      |
|----------------|------------|--------------------|--------------------|--------------------|--------------------|----------------|------|
| SmoothSpline   | MonoDecomp | SmoothSpline       | MonoDecomp         |                    |                    |                |      |
| x 2            | 1.0        | 9.65e+00 (8.9e-02) | 9.69e+00 (8.5e-02) | 6.44e+00 (2.9e-01) | 6.35e+00 (2.5e-01) | 1.68e-01       | 0.49 |
| x 3            | 1.0        | 9.75e+00 (8.2e-02) | 9.77e+00 (8.2e-02) | 6.47e+00 (1.8e-01) | 6.21e+00 (1.7e-01) | 1.18e-04 (***) | 0.65 |
| exp(x)         | 1.0        | 9.74e+00 (8.4e-02) | 9.75e+00 (8.4e-02) | 5.94e+00 (2.3e-01) | 5.82e+00 (2.1e-01) | 3.12e-02 (*)   | 0.58 |
| sigmoid        | 1.0        | 9.60e+00 (7.8e-02) | 9.64e+00 (7.5e-02) | 5.99e+00 (2.9e-01) | 5.68e+00 (2.4e-01) | 4.47e-04 (***) | 0.67 |
| SE-1           | 1.0        | 9.67e+00 (8.3e-02) | 9.70e+00 (8.1e-02) | 6.32e+00 (2.8e-01) | 6.11e+00 (2.5e-01) | 3.86e-03 (**)  | 0.6  |
| SE-0.1         | 1.0        | 8.92e+00 (9.2e-02) | 8.99e+00 (9.0e-02) | 1.23e+01 (2.1e-01) | 1.23e+01 (2.1e-01) | 4.32e-01       | 0.57 |
| Mat12-1        | 1.0        | 9.65e+00 (9.5e-02) | 9.69e+00 (9.2e-02) | 1.15e+01 (2.3e-01) | 1.13e+01 (2.1e-01) | 3.40e-04 (***) | 0.56 |
| Mat12-0.1      | 1.0        | 9.76e+00 (1.2e-01) | 9.92e+00 (1.1e-01) | 1.90e+01 (2.2e-01) | 1.90e+01 (2.2e-01) | 2.06e-01       | 0.58 |
| Mat32-1        | 1.0        | 9.59e+00 (8.5e-02) | 9.64e+00 (7.5e-02) | 7.20e+00 (2.4e-01) | 7.04e+00 (2.0e-01) | 3.65e-02 (*)   | 0.49 |
| Mat32-0.1      | 1.0        | 8.96e+00 (1.1e-01) | 9.14e+00 (1.0e-01) | 1.48e+01 (2.2e-01) | 1.47e+01 (2.1e-01) | 1.44e-01       | 0.54 |
| RQ-0.1-0.5     | 1.0        | 9.10e+00 (1.1e-01) | 9.22e+00 (1.1e-01) | 1.27e+01 (2.4e-01) | 1.25e+01 (2.2e-01) | 1.21e-03 (**)  | 0.6  |
| Periodic-0.1-4 | 1.0        | 8.69e+00 (1.0e-01) | 8.89e+00 (9.1e-02) | 1.44e+01 (2.1e-01) | 1.43e+01 (1.9e-01) | 3.03e-01       | 0.49 |

## 5 Test Of Monotonicity

Once obtaining two monotone components through monotone decomposition, in addition to utilizing the sum of these two components as a fitting method, we can also derive statistics for the monotonicity testing. Consider the model Y = f(X) + ϵ, where X is a scalar covariate, Y is a scalar dependent random variable, ϵ is the noise satisfying E[ϵ | X] = 0, and f is an unknown function. Testing of monotonicity aims to test H0 : f is monotone H1 : f is not monotone ,
where "monotone" can be specifically (strictly) "increasing" or "decreasing".

## 5.1 Related Work

There are many existing approaches for testing monotonicity. Bowman et al. (1998) constructed a test based on critical bandwidth. They fitted a local linear regression and determined the smallest bandwidth value such that the estimate becomes monotone. This critical bandwidth is then used as a test statistic, and the p-value is calculated by the bootstrap method. Hall and Heckman (2000)
pointed out the shortcoming of the test when the true function has flat and nearly flat spots, and they proposed a test that estimates local slopes and approximates the distribution of the weighted minimum. Ghosal et al. (2000) proposed test statistics that are functionals of a U-process, which is based on the signs of (Yi+k − Yi)(Xi+k − Xi). They approximated the limiting distribution by Gaussian processes and then derived the critical values for an asymptotic significance level α.

Chetverikov (2019) used the similar U-statistics, but he introduced a weighting function Q(Xi, Xj )
and proposed a statistic based on (Yi − Yj ) sign(Xj − Xi)Q(Xi, Xj ), where Q is chosen from a large set of potentially useful weighting functions to maximize the statistic. J. C. Wang and Meyer (2011) used quadratic regression splines to fit the data, took the minimum of the slopes at the knots as the test statistic, and then estimated the null distribution of such a statistic by performing constrained quadratic regression splines.

## 5.2 Test By Monotone Decomposition

Suppose we have obtained the monotone components. Propositions 3 and 5 imply that the coefficients for one component would be constant if the function is monotone. Thus, we can test the monotonicity of a function by testing whether the coefficients of monotone components are constant. The equivalences are summarized in Table 3.

| Original Hypothesis              | Hypothesis in terms of Monotone Decomposition    |                                                          |
|----------------------------------|--------------------------------------------------|----------------------------------------------------------|
| Hu : f is increasing             | Hu : γ d = c1 .                                  |                                                          |
| 0                                | 0                                                |                                                          |
| Hd : f is decreasing             | Hd                                               | u = c1 .                                                 |
| : γ                              |                                                  |                                                          |
| 0                                | 0                                                |                                                          |
| Hsu 0 : f is strictly increasing | Hsu 0 : γ d = c1, γu ̸= c1 .                      |                                                          |
| Hsd 0 : f is strictly decreasing | Hsd 0 : γ u = c1, γd ̸= c1 .                      |                                                          |
| 0                                | : f is monotone                                  | Hm 0 : one monotone component is constant,               |
| Hm                               | u , γd ) = c1 .                                  |                                                          |
| i.e., min(γ                      |                                                  |                                                          |
| 0                                | : f is strictly monotone                         | Hsm 0 : one and only one monotone component is constant, |
| Hsm                              | i.e., min(γ u , γd ) = c1, max(γ u , γd ) ̸= c1 . |                                                          |

Table 3: Equivalent hypotheses.

In Table 3, the minimum (maximum) of two vectors *a, b* ∈ IRJare defined as:
min(*a, b*) ≜ arg min x∈{a,b}
V (x), max(*a, b*) ≜ arg max x∈{a,b}
V (x),
where V is the sample variance on the elements of a vector. To test Hu 0
, Hd 0and Hm 0, consider the test statistics Tu = V (ˆγ d), Td = V (ˆγ u), Tm = V (min(ˆγ u, γˆ
d)).

Note that the null hypothesis will be rejected if the test statistic T is large enough. Specifically, given a significance level α, the respective null hypothesis would be rejected if Tu ≥ tu,1−α, Td ≥ td,1−α or Tm ≥ tm,1−α, where tu,1−α, td,1−α and tm,1−α denote the critical values of the distributions of Tu, Td, Tm under the respective null hypotheses, respectively. The distributions of Tu, Td, Tm under their null hypotheses can be characterized by the bootstrap samples. Note that the ϵ and ϵˆ
can be heterogeneous, so we take the wild bootstrap (Davidson & Flachaire, 2008). Without loss of generality, we focus on the test of increasing functions, and the procedure for testing Hu 0is outlined in Algorithm 1.

## Algorithm 1 Test Of Monotonicity (Increasing): Hu

0 Input: Significance level α, number of bootstrap samples R.

1: Fit {xi, yi}
n i=1 by monotone decomposition, either with cubic splines or smoothing splines.

Denote the increasing component as yˆ
u, let cˆ =
1 T yˆ
u n, and denote the fitting method as mˆ .

2: Calculate the test statistic T.

3: Calculate the errors, ϵi = yi − yˆi.

4: for r from 1 to R do 5: Sample ηi ∼ N(0, 1) and construct ϵ
⋆
i = ηiϵi. [Wild Bootstrap]
6: Construct bootstrap samples y
⋆
i = ˆy u i + ˆc + ϵ
⋆
i
, i = 1*, . . . , n*.

7: Apply mˆ on {xi, y⋆
i
}
n i=1, and calculate the bootstrap statistic δr 8: **end for**
9: The critical value t1−α is the 1 − α quantile of {δr}
R
r=1, then reject the null hypothesis if T > t1−α Alternatively, construct p-value 1R
PR
r=1 \#{δr > T}, and reject if *p < α*.

## 6 Simulations For Testing

Firstly, we want to check whether the methods can control the Type I error. Specifically, consider five monotone functions, x, x3, x1/3, ex and 1 1+e−x . We conducted 100 simulations and calculated the proportion of rejecting the null hypothesis. Ideally, the rejection proportion should be less than 0.05 if we pick the commonly used significance level α = 0.05. The results are reported in Table 4.

Ghosal et al. (2000) always accepts the null hypothesis. J. C. Wang and Meyer (2011) fails to control the Type I error when the noise level is small on curve x 3, and Bowman et al. (1998)
cannot control the Type I error when the noise level is large on curve x 3. In contrast, our proposed methods, monotone decomposition with cubic splines (MDCS) and monotone decomposition with smoothing splines (MDSS), demonstrate strong Type I error control in the majority of cases, even though the rejection rates are slightly elevated in a few instances.

Furthermore, the p-value should follow Uniform[0, 1] under the null hypothesis. To check the distribution of p-value for each approach, Figure 4 displays the uniform QQ plots of 1000 p-values for x 3 and e x with sample size n = 200 and noise level σ = 0.01, respectively. The uniform QQ
Table 4: Simulated size (the proportion of rejecting the null hypothesis) of monotone curves under different noise levels and different sample sizes given the significance level α = 0.05.

![13_image_0.png](13_image_0.png)

Methods Curves σ = 0.001 σ = 0.01 σ = 0.1

n = 50 100 200 n = 50 100 200 n = 50 100 200

| n = 50       | 100   | 200   | n = 50   | 100   | 200   | n = 50   | 100   | 200   |      |
|--------------|-------|-------|----------|-------|-------|----------|-------|-------|------|
| x            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.01  | 0.0  |
| 3            | 0.53  | 0.84  | 1.0      | 0.05  | 0.08  | 0.08     | 0.02  | 0.06  | 0.04 |
| 1/3          | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.03  | 0.02  | 0.01 |
| x            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 1/(1 + e−x ) | 0.0   | 0.0   | 0.0      | 0.01  | 0.0   | 0.0      | 0.04  | 0.06  | 0.05 |
| x            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 3            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 1/3          | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| x            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 1/(1 + e−x ) | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| x            | 0.0   | 0.0   | 0.0      | 0.02  | 0.0   | 0.01     | 0.01  | 0.0   | 0.01 |
| 3            | 0.0   | 0.0   | 0.0      | 0.2   | 0.19  | 0.18     | 0.26  | 0.2   | 0.15 |
| 1/3          | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.05  | 0.02  | 0.01 |
| x            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.04  | 0.02  | 0.0  |
| 1/(1 + e−x ) | 0.0   | 0.0   | 0.0      | 0.02  | 0.0   | 0.02     | 0.02  | 0.01  | 0.0  |
| x            | 0.01  | 0.0   | 0.12     | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 3            | 0.0   | 0.0   | 0.0      | 0.01  | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 1/3          | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| x            | 0.02  | 0.11  | 0.03     | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 1/(1 + e−x ) | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| x            | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0      | 0.0   | 0.0   | 0.0  |
| 3            | 0.1   | 0.08  | 0.08     | 0.08  | 0.1   | 0.07     | 0.09  | 0.05  | 0.03 |
| 1/3          | 0.0   | 0.02  | 0.02     | 0.01  | 0.03  | 0.07     | 0.05  | 0.06  | 0.05 |
| x            | 0.04  | 0.05  | 0.02     | 0.08  | 0.07  | 0.05     | 0.04  | 0.08  | 0.08 |
| 1/(1 + e−x ) | 0.03  | 0.03  | 0.03     | 0.0   | 0.01  | 0.0      | 0.0   | 0.0   | 0.0  |

![13_image_1.png](13_image_1.png)

Next, we compare the simulated size and power under the settings of two competitors. The Table 5: Simulated size and power on curves from Bowman et al. (1998) and Ghosal et al. (2000) based on 100 repetitive experiments.

MethodsBowman et al. (1998) Ghosal et al. (2000)

Curves σ = 0.001 σ = 0.01 σ = 0.1 Curves σ = 0.001 σ = 0.01 σ = 0.1

n = 50 100 200 n = 50 100 200 n = 50 100 200 n = 50 100 200 n = 50 100 200 n = 50 100 200

J. C. Wang and Meyer (2011)

a = 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.01 0.01 0.01 m1 0.1 0.04 0.04 0.06 0.02 0.06 0.07 0.07 0.1

a = 0.15 0.0 0.0 0.0 0.07 0.04 0.06 0.03 0.03 0.01 m2 1.0 1.0 1.0 1.0 1.0 1.0 0.09 0.27 0.45

a = 0.25 1.0 1.0 1.0 1.0 1.0 1.0 0.13 0.24 0.64 m3 1.0 1.0 1.0 1.0 1.0 1.0 0.34 0.56 0.88

a = 0.45 1.0 1.0 1.0 1.0 1.0 1.0 0.56 0.95 1.0 m4 0.36 0.57 0.98 0.39 0.57 0.98 0.23 0.38 0.78

Ghosal et al. (2000)

a = 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 m1 0.01 0.0 0.01 0.01 0.04 0.02 0.02 0.0 0.01

a = 0.15 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 m2 1.0 1.0 1.0 1.0 1.0 1.0 0.37 0.7 0.94

a = 0.25 0.0 0.0 1.0 0.0 0.0 0.31 0.0 0.0 0.0 m3 0.97 1.0 1.0 0.94 1.0 1.0 0.1 0.33 0.87

a = 0.45 1.0 1.0 1.0 1.0 1.0 1.0 0.06 0.71 0.99 m4 0.01 0.19 0.53 0.02 0.13 0.53 0.0 0.05 0.34

Bowman et al. (1998)

a = 0.0 0.0 0.0 0.0 0.02 0.01 0.0 0.01 0.01 0.03 m1 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

a = 0.15 0.0 0.0 0.0 0.0 0.03 0.0 0.01 0.02 0.04 m2 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 a = 0.25 1.0 1.0 1.0 1.0 1.0 1.0 0.09 0.16 0.44 m3 1.0 1.0 1.0 1.0 1.0 1.0 0.9 1.0 1.0

a = 0.45 1.0 1.0 1.0 1.0 1.0 1.0 0.3 0.72 0.98 m4 0.0 0.0 0.0 0.01 0.02 0.0 0.34 0.33 0.28

MDCS

a = 0.0 0.01 0.0 0.07 0.0 0.0 0.0 0.0 0.0 0.0 m1 0.03 0.02 0.02 0.0 0.01 0.0 0.0 0.0 0.0

a = 0.15 0.05 0.02 0.04 0.01 0.0 0.0 0.0 0.0 0.0 m2 0.98 0.99 0.95 1.0 1.0 0.94 0.18 0.35 0.65

a = 0.25 0.97 1.0 1.0 0.74 0.92 0.95 0.0 0.0 0.0 m3 0.89 0.93 1.0 0.9 0.97 0.99 0.16 0.22 0.29

a = 0.45 1.0 1.0 1.0 0.99 1.0 1.0 0.01 0.08 0.17 m4 0.89 0.91 0.94 0.88 0.92 0.99 0.51 0.68 0.81

MDSS

a = 0.0 0.02 0.07 0.06 0.02 0.08 0.03 0.02 0.04 0.04 m1 0.05 0.07 0.04 0.06 0.04 0.03 0.05 0.07 0.05

a = 0.15 0.05 0.03 0.05 0.03 0.06 0.05 0.02 0.05 0.06 m2 1.0 1.0 1.0 1.0 1.0 1.0 0.79 0.96 1.0

a = 0.25 0.99 1.0 1.0 0.98 1.0 1.0 0.03 0.04 0.03 m3 1.0 1.0 1.0 1.0 1.0 1.0 0.67 0.83 0.97

a = 0.45 1.0 1.0 1.0 1.0 1.0 1.0 0.46 0.82 0.98 m4 0.98 1.0 1.0 0.99 1.0 1.0 0.84 0.99 1.0

first one is the simulation setting in Bowman et al. (1998),

$$f(x,a)=1+x-a\exp\left(-\frac{(x-0.5)^{2}}{2\cdot0.1^{2}}\right)\,,$$
$$y=f(x,a)+N(0,\sigma^{2})\,,$$
, y = f(*x, a*) + N(0, σ2),
where a = 0, and 0.15 generate strongly and just monotonic curves, respectively; a = 0.25, and 0.45 produce mildly and strongly non-monotonic shapes, respectively. Also, we consider the simulation setting in Ghosal et al. (2000), y = mi(x) + N(0, σ2), where

$$m_{1}(x)=0\,,\quad m_{2}(x)=x(1-x)\,,\quad m_{3}(x)=x+0.415\exp(-50x^{2})\,,$$ $$m_{4}(x)=\begin{cases}10(x-0.5)^{3}-\exp(-100(x-0.25)^{2})&\text{if}x<0.5\\ 0.1(x-0.5)-\exp(-100(x-0.25)^{2})&\text{otherwise}\end{cases}\,,$$

and mi(x), i ≥ 2 are non-monotone curves. A visualization of those curves can be found in the Supplementary Material.

For each combination of parameters on each curve, 100 simulations are carried out, using a bootstrap simulation size of 100. The proportions of rejecting the null hypothesis, i.e., the simulated size and power, are reported. The complete results are displayed in Table 5, from which we have the following observations:

- Ghosal et al. (2000) fails to achieve high power on Bowman et al. (1998)'s curve a = 0.25, but our proposed method can achieve as high power as Bowman et al. (1998).

- Bowman et al. (1998) loses power on Ghosal et al. (2000)'s curve m4, but our proposed method can obtain as high power as Ghosal et al. (2000).

- For most curves, the behaviors of MDCS are similar to MDSS. But MDCS has better control over Type I errors while losing some power.
In summary, our proposed method can achieve comparable (and even better) power as other methods while controlling the Type I error.

## 7 Application: Monotonicity Test For Scrna-Seq Trajectory Inference

Single-cell transcriptome sequencing (scRNA-seq) is a powerful technique that allows researchers to profile transcript abundance at the resolution of individual cells. Trajectory inference aims first to allocate cells to lineages and then order them based on pseudotimes within these lineages.

Based on trajectory inference, researchers can discover differentially expressed genes within lineages, such as Van den Berge et al. (2020)'s tradeSeq, Song and Li (2021)'s PseudotimeDE, and Hou et al. (2023)'s Lamian. These methods mostly focus on the differential genes by checking whether the trajectory is constant along the pseudotime. Once a gene is identified as differentially expressed, researchers may further check whether its expression exhibits a monotone pattern.

A non-decreasing expression pattern indicates that the corresponding gene is turning on and needed thereafter along the cell lineage. A decreasing expression pattern indicates that the corresponding gene is needed less and less along the pseudotime. On the other hand, a non-monotone expression pattern indicates that the corresponding gene is part of a more complex dynamics.

Such detailed dynamics may illuminate the critical regulatory mechanism of cell differentiation along the corresponding lineage.

As an analogy to the term *differentially expressed (DE)* gene when the null hypothesis that the expression of the gene along the trajectory is constant is rejected, we call a non-monotonically expressed (nME) gene when the null hypothesis that the expression is monotonic is rejected. We adopt tradeSeq to identify DE genes, and the monotonicity test via monotone decomposition with cubic spline (MDCS) to find nME genes. Both DE genes and nME genes are selected using the Benjamini–Hochberg (BH) procedure to control the false discovery rate (FDR) with cutoff α = 0.05.

To explore the biological functions of DE genes and nME genes, we examined the Gene Ontology (GO), which is a relational database of terms (concepts) used to describe gene functions, and conducted enrichment analysis (Boyle et al., 2004).

Suppose there are N genes in the reference gene list, among which n genes are in our analyzed gene set. For a GO term of interest, suppose there are M and k genes within the reference gene list and our analyzed gene set, respectively, that are annotated to have the GO term. The p-value for the one-sided Fisher's exact test of the null hypothesis that the GO term is not enriched in the analyzed gene set can be calculated based on the hypergeometric distribution:

$$p=1-\sum_{i=0}^{k-1}{\frac{{\binom{M}{i}}{\binom{N-M}{k-i}}}{{\binom{N}{n}}}}\,.$$

We repeat this test for multiple GO terms of interest and correct for multiple comparisons via the BH procedure to control the FDR at the cutoff α = 0.05.

## 7.1 Nme Genes Can Identify Significant Go Terms When De Genes Fail

We studied the leukocyte lineage of the mouse bone marrow data set (Paul et al., 2015), which consists of the expression measurements of 3004 genes at 1474 pseudotime points. Figure 5a shows the reduced two-dimensional representation of the data using uniform manifold approximation and projection (UMAP) (McInnes et al., 2018). Eight cell types are denoted with different colors and shapes. The solid curve is the pseudotime axis, which starts from the cell type *Multipotent* progenitors at the bottomright and ends at the cell type *Neutrophils* at the topleft. Note that although a monotone pattern is a special DE pattern, we do not perform the monotonicity test in a two-step manner, i.e., firstly find DE genes and then perform the monotonicity test among those found DE
genes. Instead, for each gene, we test whether it is a DE gene or an nME gene independently.

Figure 5b displays the paired p-values (pnME, pDE) in the logarithmic scale, where the dash lines denote the cutoff determined by the BH procedure. As a result, we identified 109 nME genes (it is 102 after GO analysis since 7 genes are not mapped in the GO database) and 767 DE genes, of which 53 genes are in common. These numbers are also noted in the titles of GO bar plots in Figure 6. Figure 5c illustrates the fitted trajectory for gene 2610029G23Rik, which is identified as an nME gene but not a DE gene, i.e., it lies in the bottom right green block of Figure 5b.

![16_image_0.png](16_image_0.png) 

Figure 5: *(a):* Two-dimensional representation of the data using UMAP. Different cell types are denoted with different colors (and shapes). The pseudotime axis is displayed, which starts from the *Multipotent progenitors* cell type at the bottom-right to the *Neutrophils* cell type at the top-left.

(b): the scatter plot of the paired p-values (pnME, pDE), where the star symbols denote NA values when tradeSeq failed. (c): one example gene located in the bottom right green block of (b), which is identified as an nME gene but not a DE gene. (d): Trajectory curves of 109 nME genes. The curves of 22 genes annotated in the GO term "translation" are highlighted.

Figure 6 displays GO enrichment analysis on the DE genes and nME genes by R package clusterProfiler (Yu et al., 2023). Figures 6a, 6b and 6c take the whole 3004 genes as the reference gene list, but note that, because some genes are not mapped in the GO database, there are only 2665 genes after filtering. We cannot find significant GO terms for the DE gene list, as shown in Figure 6b, which is left blank deliberately due to no significant results. In contrast, we can identify several significant GO terms for the nME gene list. Figures 6c and 6d display the intersection of the DE gene list and the nME gene list with respect to the whole gene list or the DE gene list, respectively. Both can identify significant GO terms. One possible reason for DE genes failing to identify significant GO terms is that the range of DE genes might be too broad, thus different sub-categories of DE genes (the non-monotonic pattern is a special sub-category) might contribute to different GO terms, but the increased sample size due to incorporating unrelated genes might reduce the significance for determining the significant GO terms. Another potential reason is that the tradeSeq test is not robust enough. As shown by the star symbol in Figure 5b, there are many NA values returned by tradeSeq, which is a known issue discussed in their GitHub repository1.

We can further check whether the pattern of trajectory curves in the enriched GO terms agrees with the biological mechanism. Take the first GO term "translation" as an example. Figure 5d displays the trajectory curves of 109 nME genes along the pseudotime. Among these 109 nME genes, the curves of 22 genes annotated in the GO term "translation" are highlighted. These genes exhibit a coherent pattern, characterized by an initial increase in expression followed by a subsequent decrease. If we cast the pseudotime axis in Figure 5d back to Figure 5a, the curve pattern implies that the gene expression increases when the cell develops from *Multipotent*

![17_image_0.png](17_image_0.png) 

progenitors to *Monocytes*, and roughly after the gene expression reaching the peak, the cell evolves to *Neutrophils*. This behavior is consistent with the biological fact that specialized cell types (here Neutrophils) might reduce rates of translation (and hence protein synthesis), since their structure and function are relatively stable.

## 7.2 Nme Genes Can Fine-Locate Go Terms When De Genes Identify Too Many Terms

In some scenarios, although GO enrichment analysis can identify significant GO terms given the DE genes, nME genes can further fine-locate GO terms and focus on a small but significant set of GO terms. We analyzed the cholangiocyte lineage from the mouse liver data studied in Ghazanfar et al. (2020) to demonstrate such an advantage of nME genes. In the dataset, there are 6038 genes and 308 pseudotime points.

tradeSeq identifies 767 DE genes (it is 801 before filtering due to unmapping in GO), and the monotonicity test identifies 67 nME genes (it is 69 before filtering due to unmapping in GO),
of which 45 genes are in common. For the 767 DE genes, we identify 439 significant GO terms, whereas for the 67 nME genes, we find 39 significant GO terms. Between the two sets, 28 GO terms are in common. Figure 7a displays all GO terms returned by the 39 nME genes, where the star symbol indicates GO terms not shared by the DE genes. Figure 7b shows the enrichment map constructed by the GO terms from DE genes, in which the common GO terms shared by the nME genes are highlighted. In the enrichment map, an edge connects two GO terms if there are overlapped genes, and hence, mutually overlapping GO terms tend to cluster together, making it easy to identify functional modules. It is clear that the shared GO terms mainly focus on two clusters: one is isolated from others on the right side and forms a pentagon shape with the keyword "coagulation"; another cluster is located at the left corner of the biggest cluster, related to "catabolic process". In other words, nME genes can help fine-locate GO terms, which might help save time for researchers without checking too many GO terms from DE genes.

We further check the new GO terms enriched by the nME genes, which are annotated with the star symbol in Figure 7a. These new GO terms might be contributed by new genes that are not identified as DE genes. For example, we take the GO term "regulation of blood coagulation" as an example, which contains 5 genes {F11, Kng2, Serpinc1, Serpinf2, Vtn} in the nME gene set, where the first three are also in the DE gene set, but the last two are only in the nME gene set. Figures 8c and 8d display the fitted trajectory of the expression along pseudotime by our

![18_image_0.png](18_image_0.png) 

monotone decomposition fitting technique, and the p-values are also noted in the title of each figure. We observe that the p-value for the DE gene is not quite as significant as the one for the nME gene. In other words, these two p-values lie in the bottom right green block of Figure 8a.

Using the same data at the hepatoblast stage (an earlier stage than the cholangiocyte stage we considered), Ghazanfar et al. (2020) identified 68 *differentially variable* (DV) genes, which indicates that the *variances* (instead of the *mean* expression considered in DE genes and nME genes) of gene expressions change along the pseudotime. Accidentally, Serpinf2 and Vtn are the two and the only two which are both in the 68 DV gene set and the 69 nME gene set. The coexistence of DV and nME characteristics in these genes suggests intricate and dynamic expression patterns, which might indicate significant biological interest. The dual nature of being both DV and nME genes underscores the complexity of the regulatory mechanisms governing these specific genetic expressions.

Furthermore, we check all genes that are identified as nME but not DE. Figure 8b displays the trajectory curves of all nME genes, and the curves of nME but not DE genes are highlighted, while others are transparent. To facilitate comparative analysis, all curves are centered and different colors denote different clusters (see Section 7.3). Note that the variations of highlighted curves are relatively small compared to curves in transparent, so different methods might make different conclusions. As a result, some non-DE genes are treated as nME genes despite the initial expectation that nME genes should naturally encompass a subset of DE genes.

## 7.3 Nme Genes Can Highlight Non-Monotonic Patterns While De Genes Blur Them

The clustering of genes based on their fitted expression patterns can reveal intriguing insights for biologists. However, a potential limitation of clustering based on DE genes is the tendency of clustering methods to amalgamate pure monotonic patterns with somewhat intricate nonmonotonic patterns (e.g., Figure 5 of Van den Berge et al. (2020)). To mitigate the amalgamation of non-monotonic patterns and maintain their clarity, one possible direction is to tailor clustering approaches, such as constructing more suitable similarity measurements. Another direct approach is to focus only on non-monotonic patterns from nME genes.

![19_image_0.png](19_image_0.png)

Here, we consider the liver dataset in Section 7.2. Figure 9a shows the dendrogram from hierarchical clustering with *complete* linkage on 69 nME genes. We take the cutoff 2.0 to obtain 10 clusters with clear patterns. Figure 9b presents the trajectory curves of those 69 nME genes, and different colors denote different clusters. Notably, we have highlighted three representative clusters, each depicted in its respective figure, ranging from Figure 9c to Figure 9d. Figure 9c displays a peak on the right side, while Figure 9d showcases a peak on the left side.

On the other hand, we perform hierarchical clustering with a similar cutoff 1.5 and identify 12 clusters, as shown in Figure 9e. The trajectory curves of 801 DE genes with different colors representing different clusters are displayed in Figure 9f. It is worth noting that the presence of monotonic patterns has somewhat concealed the underlying wiggly patterns, as evidenced in Figure 9g, which combines non-monotonic patterns similar to those found in Figure 9c with numerous ascending curves. Similarly, Figure 9h combines the non-monotonic pattern observed in Figure 9d, illustrating the challenges in distinguishing these patterns.

Pure non-monotonic patterns hold the potential to identify significant patterns. For example, all three genes in Figure 9c are significantly annotated to GO terms "defense response to other organism", "response to external biotic stimulus", and "response to other organism", each accompanied by FDR adjusted p-value of 0.00278.

## 8 Discussions

We formulate the monotone decomposition with monotone splines. It can serve as a fitting method when we sum up two monotone components, and it can be used to conduct a test of monotonicity by checking whether one component is constant.

As a fitting method, the experiments have shown that the monotone decomposition with cubic splines improves the performance, especially in high noise cases. We can explain the better performance in monotone functions theoretically. Similar phenomena have been observed for the monotone decomposition with smoothing splines. However, there are also some limitations:
- The cross-validation procedure for simultaneously tuning two parameters is computationally extensive. The generative bootstrap sampler (GBS) proposed by Shin et al. (2023) might be an alternative to speed up the cross-validation step.

- Currently, the theoretical guarantees are only for monotone functions. It would be great if the theoretical results could be extended to general functions.

![20_image_0.png](20_image_0.png)

Figure 9: Clustering of trajectory curves of nME genes (first row) and DE genes (second row).

(a): Hierarchical dendrogram of 69 nME genes. The cutoff (2.0) at the dashed line results in 10 clusters. *(b):* Trajectory curves of 69 nME genes. *(c)-(d)* display the curves of 2 out of 10 clusters from (b), respectively. The gene symbols are noted for clusters with few genes. *(e):* Hierarchical dendrogram of 801 DE genes. The cutoff (1.5) at the dashed line results in 12 clusters. *(f):* Trajectory curves of 801 DE genes. (g) and (h) are two distinct clusters from 12 clusters in (f). Different colors denote different clusters. The same color in (b) to (d) denotes the same cluster, and the same color in (g) to (h) denotes the same cluster, but there is no direct correspondence between the colors in (b) and (f).

For the test of monotonicity by monotone decomposition, the proposed statistics based on monotone decomposition show competitive performance and are even much better than the existing approaches.

We also apply the fitting and testing based on monotone decomposition to investigate the monotonic and non-monotonic trajectory patterns in several scRNA-seq datasets. In parallel with the conventional analysis of differentially expressed (DE) genes, we propose the concept of non-monotonically expressed (nME) genes, which might lead to new biological insights.

## Acknowledgement

Lijun Wang was supported by the Hong Kong Ph.D. Fellowship Scheme from the University Grant Committee. Hongyu Zhao was supported in part by NIH grant P50 CA196530. JSL was supported in part by the NSF DMS/NIGMS 2 Collaborative Research grant (R01 GM152814).

## Supplementary Material

The Supplementary Material contains additional simulation results and technical proofs of propositions.

## References

Bowman, A. W., Jones, M. C., & Gijbels, I. (1998). Testing Monotonicity of Regression. *Journal of* Computational and Graphical Statistics, 7(4), 489–500. https://doi.org/10.1080/10618600.

1998.10474790 Boyle, E. I., Weng, S., Gollub, J., Jin, H., Botstein, D., Cherry, J. M., & Sherlock, G. (2004).

GO::TermFinder—open source software for accessing Gene Ontology information and finding significantly enriched Gene Ontology terms associated with a list of genes. *Bioinformatics*, 20(18), 3710–3715. https://doi.org/10.1093/bioinformatics/bth456 Chetverikov, D. (2019). Testing regression monotonicity in econometric models. *Econometric Theory*, 35(4), 729–776. https://doi.org/10.1017/S0266466618000282 Chipman, H. A., George, E. I., & McCulloch, R. E. (2010). BART: Bayesian additive regression trees.

The Annals of Applied Statistics, 4(1), 266–298. https://doi.org/10.1214/09-AOAS285 Chipman, H. A., George, E. I., McCulloch, R. E., & Shively, T. S. (2022). mBART: Multidimensional Monotone BART. *Bayesian Analysis*, 17(2), 515–544. https://doi.org/10.1214/21-BA1259 Davidson, R., & Flachaire, E. (2008). The wild bootstrap, tamed at last. *Journal of Econometrics*,
146(1), 162–169. https://doi.org/10.1016/j.jeconom.2008.08.003 De Boor, C. (1978). *A practical guide to splines* (Vol. 27). Springer.

Ghazanfar, S., Lin, Y., Su, X., Lin, D. M., Patrick, E., Han, Z.-G., Marioni, J. C., & Yang, J. Y. H. (2020).

Investigating higher-order interactions in single-cell data with scHOT. Nature Methods, 17(8), 799–806. https://doi.org/10.1038/s41592-020-0885-x Ghosal, S., Sen, A., & van der Vaart, A. W. (2000). Testing Monotonicity of Regression. The Annals of Statistics, 28(4), 1054–1082.

Gramacy, R. B. (2020). Surrogates: Gaussian Process Modeling, Design and Optimization for the Applied Sciences. Chapman Hall/CRC.

Hall, P., & Heckman, N. E. (2000). Testing for Monotonicity of a Regression Mean by Calibrating for Linear Functions. *The Annals of Statistics*, 28(1), 20–39.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of statistical learning: Data mining, inference, and prediction (2nd ed.). Springer Science & Business Media.

Hou, W., Ji, Z., Chen, Z., Wherry, E. J., Hicks, S. C., & Ji, H. (2023). A statistical framework for differential pseudotime analysis with multiple single-cell RNA-seq samples. Nature Communications, 14(1), 7286. https://doi.org/10.1038/s41467-023-42841-y Magnus, J. R., & Neudecker, H. (2019). *Matrix Differential Calculus with Applications in Statistics and* Econometrics (1st ed.). John Wiley & Sons, Ltd. https://doi.org/10.1002/9781119541219 McInnes, L., Healy, J., Saul, N., & Großberger, L. (2018). UMAP: Uniform Manifold Approximation and Projection. *Journal of Open Source Software*, 3(29), 861. https://doi.org/10.21105/joss.

00861 Paul, F., Arkin, Y., Giladi, A., Jaitin, D. A., Kenigsberg, E., Keren-Shaul, H., Winter, D., Lara-Astiaso, D., Gury, M., Weiner, A., David, E., Cohen, N., Lauridsen, F. K. B., Haas, S., Schlitzer, A., Mildner, A., Ginhoux, F., Jung, S., Trumpp, A., . . . Amit, I. (2015). Transcriptional Heterogeneity and Lineage Commitment in Myeloid Progenitors. Cell, 163(7), 1663–1677.

https://doi.org/10.1016/j.cell.2015.11.013 Ramsay, J. O., & Silverman, B. W. (2005). *Functional data analysis* (Second edition). Springer.

Rasmussen, C. E., & Williams, C. K. I. (2006). *Gaussian processes for machine learning*. MIT Press.

Shin, M., Wang, S., & Liu, J. S. (2023). Generative Multi-purpose Sampler for Weighted Mestimation. *Journal of Computational and Graphical Statistics*, 0(ja), 1–53. https://doi.org/10.

1080/10618600.2023.2292668 Song, D., & Li, J. J. (2021). PseudotimeDE: Inference of differential gene expression along cell pseudotime with well-calibrated p-values from single-cell RNA sequencing data. *Genome* Biology, 22(1), 124. https://doi.org/10.1186/s13059-021-02341-y Van den Berge, K., Roux de Bézieux, H., Street, K., Saelens, W., Cannoodt, R., Saeys, Y., Dudoit, S., & Clement, L. (2020). Trajectory-based differential expression analysis for single-cell sequencing data. *Nature Communications*, 11(1), 1201. https://doi.org/10.1038/s41467020-14766-3 Wang, J. C., & Meyer, M. C. (2011). Testing the monotonicity or convexity of a function using regression splines. *The Canadian Journal of Statistics / La Revue Canadienne de Statistique*, 39(1), 89–107.

Wang, L., Fan, X., Li, H., & Liu, J. S. (2023). Monotone Cubic B-Splines. https://doi.org/10.48550/
arXiv.2307.01748 Yu, G., Wang, L.-G., Hu, E., Luo, X., Chen, M., Dall'Olio, G., Wei, W., & Gao, C.-H. (2023).

clusterProfiler: A universal enrichment tool for interpreting omics data. https://doi.org/ 10.18129/B9.bioc.clusterProfiler

## A More Simulation Results A.1 Candidate Kernels

Random functions with kernel K, including Squared Exponential (SE) kernel KSE, Rational Quadratic (RQ) kernel KRQ, Matérn (Mat) kernel KMat and Periodic kernel K*P eriodic*(Rasmussen
& Williams, 2006).

$$K_{S E}(x,x^{\prime})=\exp\left(-\frac{(x-x^{\prime})^{2}}{2\ell^{2}}\right),\ K_{M a t}(x,x^{\prime})=\frac{2^{1-\nu}}{\Gamma(\nu)}\left(\frac{\sqrt{2\nu}|x-x^{\prime}|}{\ell}\right)^{\nu}S_{\nu}\left(\frac{\sqrt{2\nu}}{\ell}\right)$$ $$K_{R Q}(x,x^{\prime})=\left(1+\frac{(x-x^{\prime})^{2}}{2\alpha\ell^{2}}\right)^{-\alpha},\ K_{P e r i o d i c}(x,x^{\prime})=\exp\left(-\frac{2\sin^{2}(|x-x^{\prime}|/T)}{\ell^{2}}\right)$$

![23_image_0.png](23_image_0.png)

,
where *ℓ, ν, α, T* are the parameters, and Sν is a modified Bessel function. In particular, "Mat12" refers to the Matérn kernel with ν = 1/2, and similarly, "Mat32" and "Mat52" indicate ν = 3/2 and 5/2, respectively. Any additional parameters are appended to the kernel name; for example,
"SE-1" represents the Squared Exponential kernel with ℓ = 1, "Mat12-1" denotes the Matérn kernel with ν = 1/2, ℓ = 1, and "RQ-0.1-0.5" is the Rational Quadratic kernel with parameter ℓ = 0.1, α = 0.5.

## A.2 Random Function Generation

A random function f with kernel K is generated as follows, 1. Generate n random points, xi ∼ U[−1, 1], i = 1*, . . . , n*.

2. Calculate the covariance matrix Σ based on kernel K, Σij = K(xi, xj ). Practically, add a small constant, say 10−7, on the diagonal of Σ to prevent numerically ill-conditioned matrix
(Gramacy, 2020).

3. Generate a random Gaussian vector with the above covariance matrix, f ∼ N(0, Σ).

![23_image_1.png](23_image_1.png) 

## A.3 Monotone Decomposition With Cubic Splines

Table 6: A complete version with finer noise levels fro Table 1. Results for comparing the cubic splines and the fitting by monotone decomposition with CV-tuned (*µ, J*). The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error.

| curve              | σ                  | MSFE                                  | MSPE                                  | p-value                               | prop.          |      |
|--------------------|--------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------|------|
| CubicSpline        | MonoDecomp         | CubicSpline                           | MonoDecomp                            |                                       |                |      |
| 0.2                | 1.95e+00 (1.4e-02) | 1.94e+00 (1.5e-02)                    | 1.46e+00 (6.1e-02) 1.46e+00 (6.4e-02) | 4.44e-01                              | 0.57           |      |
| 0.4                | 3.84e+00 (3.4e-02) | 3.83e+00 (3.0e-02)                    | 2.97e+00 (1.5e-01) 2.90e+00 (1.3e-01) | 2.79e-01                              | 0.57           |      |
| 2 x                | 0.6                | 5.80e+00 (4.3e-02)                    | 5.77e+00 (4.7e-02)                    | 4.45e+00 (2.0e-01) 4.22e+00 (1.9e-01) | 7.97e-02 (.)   | 0.63 |
| 1.0                | 9.71e+00 (7.3e-02) | 9.73e+00 (7.3e-02)                    | 7.50e+00 (3.1e-01) 6.93e+00 (2.6e-01) | 5.91e-03 (**)                         | 0.59           |      |
| 0.2                | 1.89e+00 (1.6e-02) | 1.88e+00 (1.7e-02) 1.53e+00 (6.9e-02) | 1.54e+00 (5.9e-02)                    | 3.81e-01                              | 0.47           |      |
| 0.4                | 3.83e+00 (3.0e-02) | 3.80e+00 (3.0e-02) 2.82e+00 (1.4e-01) | 2.89e+00 (1.2e-01)                    | 1.71e-01                              | 0.45           |      |
| x 3                | 0.6                | 5.74e+00 (4.6e-02)                    | 5.68e+00 (4.9e-02)                    | 4.78e+00 (2.1e-01) 4.71e+00 (1.6e-01) | 2.93e-01       | 0.49 |
| 1.0                | 9.65e+00 (7.4e-02) | 9.60e+00 (7.2e-02)                    | 7.63e+00 (3.5e-01) 7.17e+00 (2.7e-01) | 2.21e-02 (*)                          | 0.6            |      |
| 0.2                | 1.91e+00 (1.3e-02) | 1.88e+00 (1.5e-02) 1.51e+00 (5.8e-02) | 1.61e+00 (6.6e-02)                    | 3.47e-02 (*)                          | 0.53           |      |
| 0.4                | 3.83e+00 (2.9e-02) | 3.82e+00 (3.1e-02)                    | 2.79e+00 (1.3e-01) 2.71e+00 (1.1e-01) | 1.97e-01                              | 0.57           |      |
| exp(x)             | 0.6                | 5.72e+00 (4.4e-02)                    | 5.68e+00 (4.4e-02)                    | 4.45e+00 (1.8e-01) 4.27e+00 (1.7e-01) | 1.15e-01       | 0.61 |
| 1.0                | 9.57e+00 (5.9e-02) | 9.49e+00 (7.3e-02)                    | 7.56e+00 (2.8e-01) 7.08e+00 (3.1e-01) | 3.59e-02 (*)                          | 0.57           |      |
| 0.2                | 1.91e+00 (1.5e-02) | 1.91e+00 (1.6e-02)                    | 1.69e+00 (5.4e-02) 1.59e+00 (5.0e-02) | 6.14e-03 (**)                         | 0.65           |      |
| 0.4                | 3.89e+00 (3.2e-02) | 3.88e+00 (3.2e-02)                    | 2.99e+00 (1.2e-01) 2.96e+00 (1.1e-01) | 3.53e-01                              | 0.47           |      |
| sigmoid            | 0.6                | 5.77e+00 (4.8e-02)                    | 5.76e+00 (4.8e-02)                    | 4.35e+00 (1.7e-01) 4.14e+00 (1.4e-01) | 4.19e-02 (*)   | 0.56 |
| 1.0                | 9.51e+00 (8.5e-02) | 9.50e+00 (8.7e-02)                    | 7.33e+00 (3.2e-01) 6.61e+00 (2.6e-01) | 1.45e-03 (**)                         | 0.56           |      |
| 0.2                | 1.93e+00 (1.4e-02) | 1.93e+00 (1.6e-02)                    | 1.62e+00 (7.3e-02) 1.59e+00 (5.2e-02) | 3.21e-01                              | 0.52           |      |
| 0.4                | 3.81e+00 (3.4e-02) | 3.78e+00 (3.6e-02)                    | 3.18e+00 (1.4e-01) 3.16e+00 (1.2e-01) | 3.93e-01                              | 0.54           |      |
| SE-1               | 0.6                | 5.77e+00 (4.4e-02)                    | 5.77e+00 (4.6e-02)                    | 4.67e+00 (2.0e-01) 4.34e+00 (1.6e-01) | 2.88e-02 (*)   | 0.57 |
| 1.0                | 9.55e+00 (7.0e-02) | 9.51e+00 (7.6e-02)                    | 7.29e+00 (3.2e-01) 6.62e+00 (2.7e-01) | 5.51e-03 (**)                         | 0.63           |      |
| 0.2                | 1.76e+00 (2.0e-02) | 1.78e+00 (2.5e-02) 3.54e+00 (5.3e-02) | 3.54e+00 (6.7e-02)                    | 4.92e-01                              | 0.6            |      |
| 0.4                | 3.54e+00 (3.6e-02) | 3.55e+00 (3.8e-02)                    | 6.59e+00 (1.1e-01) 6.25e+00 (1.0e-01) | 1.36e-04 (***)                        | 0.66           |      |
| SE-0.1             | 0.6                | 5.57e+00 (5.4e-02)                    | 5.59e+00 (6.0e-02)                    | 9.20e+00 (1.6e-01) 9.13e+00 (1.6e-01) | 3.14e-01       | 0.59 |
| 1.0                | 9.29e+00 (8.5e-02) | 9.20e+00 (9.3e-02)                    | 1.44e+01 (2.6e-01) 1.38e+01 (2.4e-01) | 5.93e-04 (***)                        | 0.7            |      |
| 0.2                | 2.12e+00 (3.2e-02) | 2.15e+00 (2.9e-02)                    | 5.43e+00 (5.2e-02) 5.29e+00 (6.5e-02) | 7.85e-03 (**)                         | 0.72           |      |
| 0.4                | 4.08e+00 (4.7e-02) | 4.02e+00 (4.8e-02)                    | 7.55e+00 (9.5e-02) 7.20e+00 (8.9e-02) | 7.51e-09 (***)                        | 0.72           |      |
| Mat12-1            | 0.6                | 5.82e+00 (6.5e-02)                    | 5.79e+00 (5.8e-02)                    | 9.34e+00 (1.4e-01) 8.94e+00 (1.1e-01) | 1.35e-04 (***) | 0.7  |
| 1.0                | 9.79e+00 (8.9e-02) | 9.73e+00 (9.1e-02)                    | 1.26e+01 (2.9e-01) 1.17e+01 (2.4e-01) | 9.31e-07 (***)                        | 0.68           |      |
| 0.2                | 3.87e+00 (6.8e-02) | 3.88e+00 (7.3e-02)                    | 1.26e+01 (1.6e-01) 1.25e+01 (1.8e-01) | 2.28e-01                              | 0.57           |      |
| 0.4                | 5.15e+00 (8.3e-02) | 5.08e+00 (6.9e-02)                    | 1.47e+01 (1.5e-01) 1.42e+01 (1.3e-01) | 1.25e-03 (**)                         | 0.66           |      |
| Mat12-0.1          | 0.6                | 6.77e+00 (1.0e-01)                    | 6.64e+00 (8.8e-02)                    | 1.67e+01 (1.8e-01) 1.61e+01 (1.7e-01) | 2.66e-04 (***) | 0.67 |
| 1.0                | 1.04e+01 (1.3e-01) | 1.04e+01 (1.3e-01)                    | 2.07e+01 (2.4e-01) 2.01e+01 (2.4e-01) | 1.85e-04 (***)                        | 0.73           |      |
| 0.2                | 1.87e+00 (1.6e-02) | 1.87e+00 (1.6e-02)                    | 2.40e+00 (4.5e-02) 2.29e+00 (4.3e-02) | 1.30e-03 (**)                         | 0.66           |      |
| 0.4                | 3.82e+00 (3.5e-02) | 3.79e+00 (3.6e-02)                    | 3.99e+00 (1.0e-01) 3.92e+00 (9.6e-02) | 2.08e-01                              | 0.63           |      |
| Mat32-1            | 0.6                | 5.77e+00 (4.4e-02)                    | 5.76e+00 (4.3e-02)                    | 5.60e+00 (1.6e-01) 5.28e+00 (1.3e-01) | 4.84e-03 (**)  | 0.68 |
| 1.0                | 9.62e+00 (8.2e-02) | 9.61e+00 (8.3e-02)                    | 9.01e+00 (3.5e-01) 8.00e+00 (2.6e-01) | 1.46e-04 (***)                        | 0.56           |      |
| 0.2                | 2.05e+00 (3.5e-02) | 2.11e+00 (4.4e-02) 5.46e+00 (7.6e-02) | 5.54e+00 (1.1e-01)                    | 1.82e-01                              | 0.57           |      |
| 0.4                | 3.84e+00 (5.4e-02) | 3.77e+00 (6.0e-02)                    | 8.83e+00 (1.1e-01) 8.41e+00 (1.3e-01) | 8.21e-05 (***)                        | 0.74           |      |
| Mat32-0.1          | 0.6                | 5.64e+00 (7.0e-02)                    | 5.58e+00 (7.6e-02)                    | 1.17e+01 (1.5e-01) 1.13e+01 (1.4e-01) | 1.68e-05 (***) | 0.69 |
| 1.0                | 9.62e+00 (1.1e-01) | 9.53e+00 (9.7e-02)                    | 1.68e+01 (2.5e-01) 1.58e+01 (2.1e-01) | 4.67e-10 (***)                        | 0.72           |      |
| 0.2                | 1.72e+00 (2.9e-02) | 1.74e+00 (3.1e-02)                    | 4.14e+00 (6.5e-02) 4.12e+00 (7.4e-02) | 3.53e-01                              | 0.61           |      |
| 0.4                | 3.77e+00 (4.6e-02) | 3.68e+00 (4.6e-02)                    | 7.33e+00 (1.1e-01) 6.92e+00 (9.9e-02) | 1.44e-06 (***)                        | 0.77           |      |
| RQ-0.1-0.5         | 0.6                | 5.63e+00 (7.2e-02)                    | 5.54e+00 (6.4e-02)                    | 1.03e+01 (1.7e-01) 9.61e+00 (1.6e-01) | 2.72e-07 (***) | 0.72 |
| 1.0                | 9.55e+00 (1.1e-01) | 9.50e+00 (1.2e-01)                    | 1.50e+01 (2.4e-01) 1.44e+01 (2.6e-01) | 5.01e-03 (**)                         | 0.68           |      |
| 0.2                | 1.68e+00 (2.8e-02) | 1.70e+00 (2.7e-02)                    | 4.27e+00 (7.0e-02) 4.21e+00 (6.6e-02) | 2.00e-01                              | 0.6            |      |
| 0.4                | 3.40e+00 (4.2e-02) | 3.48e+00 (5.2e-02)                    | 7.90e+00 (1.1e-01) 7.84e+00 (1.3e-01) | 2.81e-01                              | 0.65           |      |
| Periodic-0.1-4 0.6 | 5.42e+00 (7.3e-02) | 5.45e+00 (7.0e-02)                    | 1.12e+01 (1.6e-01) 1.08e+01 (1.8e-01) | 2.52e-02 (*)                          | 0.65           |      |
| 1.0                | 9.41e+00 (1.2e-01) | 9.31e+00 (1.1e-01)                    | 1.72e+01 (3.0e-01) 1.60e+01 (2.5e-01) | 2.03e-10 (***)                        | 0.63           |      |

Table 7: Results for comparing the cubic splines and the fitting by monotone decomposition with CV-tuned µ and fixed J. The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error.

| curve              | σ                  | MSFE                                  | MSPE                                  | p-value                               | prop.          |      |
|--------------------|--------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------|------|
| CubicSpline        | MonoDecomp         | CubicSpline                           | MonoDecomp                            |                                       |                |      |
| 0.1                | 9.68e-01 (8.2e-03) | 9.71e-01 (8.2e-03)                    | 7.38e-01 (3.6e-02)                    | 7.07e-01 (3.3e-02)                    | 1.47e-03 (**)  | 0.65 |
| 0.2                | 1.92e+00 (1.6e-02) | 1.93e+00 (1.6e-02)                    | 1.53e+00 (7.7e-02) 1.45e+00 (7.2e-02) | 1.03e-03 (**)                         | 0.74           |      |
| x 2                | 0.5                | 4.88e+00 (3.6e-02)                    | 4.90e+00 (3.6e-02)                    | 3.67e+00 (1.5e-01) 3.37e+00 (1.3e-01) | 2.20e-06 (***) | 0.77 |
| 1.0                | 9.63e+00 (8.2e-02) | 9.73e+00 (8.0e-02)                    | 7.12e+00 (3.2e-01) 5.92e+00 (2.5e-01) | 1.73e-10 (***)                        | 0.77           |      |
| 0.1                | 9.56e-01 (7.6e-03) | 9.58e-01 (7.1e-03)                    | 7.32e-01 (3.5e-02)                    | 6.98e-01 (2.9e-02)                    | 1.01e-03 (**)  | 0.61 |
| 0.2                | 1.93e+00 (1.6e-02) | 1.94e+00 (1.5e-02)                    | 1.47e+00 (7.1e-02) 1.38e+00 (5.8e-02) | 2.88e-05 (***)                        | 0.69           |      |
| x 3                | 0.5                | 4.83e+00 (4.3e-02)                    | 4.86e+00 (4.2e-02)                    | 3.66e+00 (1.5e-01) 3.41e+00 (1.4e-01) | 7.49e-03 (**)  | 0.64 |
| 1.0                | 9.55e+00 (8.1e-02) | 9.68e+00 (7.8e-02)                    | 8.03e+00 (3.7e-01) 7.02e+00 (2.7e-01) | 2.01e-06 (***)                        | 0.69           |      |
| 0.1                | 9.56e-01 (7.4e-03) | 9.57e-01 (7.3e-03)                    | 7.51e-01 (3.3e-02)                    | 7.26e-01 (3.0e-02)                    | 3.12e-04 (***) | 0.61 |
| 0.2                | 1.93e+00 (1.5e-02) | 1.94e+00 (1.5e-02)                    | 1.40e+00 (6.6e-02) 1.32e+00 (5.9e-02) | 4.32e-07 (***)                        | 0.67           |      |
| exp(x)             | 0.5                | 4.82e+00 (3.9e-02)                    | 4.84e+00 (3.7e-02)                    | 3.52e+00 (1.7e-01) 3.02e+00 (1.4e-01) | 9.36e-11 (***) | 0.8  |
| 1.0                | 9.74e+00 (7.6e-02) | 9.82e+00 (7.5e-02)                    | 7.47e+00 (3.3e-01) 6.09e+00 (2.5e-01) | 6.35e-11 (***)                        | 0.8            |      |
| 0.1                | 9.53e-01 (7.3e-03) | 9.60e-01 (7.5e-03)                    | 8.84e-01 (2.4e-02)                    | 8.55e-01 (2.5e-02)                    | 3.16e-03 (**)  | 0.68 |
| 0.2                | 1.87e+00 (1.4e-02) | 1.89e+00 (1.4e-02)                    | 1.81e+00 (6.2e-02) 1.67e+00 (5.2e-02) | 5.12e-05 (***)                        | 0.71           |      |
| sigmoid            | 0.5                | 4.78e+00 (3.8e-02)                    | 4.82e+00 (3.6e-02)                    | 3.83e+00 (1.7e-01) 3.51e+00 (1.3e-01) | 2.42e-04 (***) | 0.66 |
| 1.0                | 9.50e+00 (7.7e-02) | 9.62e+00 (7.7e-02)                    | 7.62e+00 (3.4e-01) 6.36e+00 (2.4e-01) | 5.51e-08 (***)                        | 0.61           |      |
| 0.1                | 9.69e-01 (6.9e-03) | 9.74e-01 (6.7e-03)                    | 8.68e-01 (3.5e-02)                    | 8.18e-01 (3.0e-02)                    | 1.44e-04 (***) | 0.73 |
| 0.2                | 1.92e+00 (1.6e-02) | 1.92e+00 (1.6e-02)                    | 1.62e+00 (6.1e-02) 1.55e+00 (5.6e-02) | 3.30e-04 (***)                        | 0.66           |      |
| SE-1               | 0.5                | 4.84e+00 (3.6e-02)                    | 4.88e+00 (3.5e-02)                    | 3.77e+00 (1.7e-01) 3.52e+00 (1.3e-01) | 2.43e-03 (**)  | 0.61 |
| 1.0                | 9.69e+00 (6.9e-02) | 9.77e+00 (6.7e-02)                    | 7.31e+00 (3.1e-01) 6.15e+00 (2.5e-01) | 2.24e-09 (***)                        | 0.63           |      |
| 0.1                | 8.51e-01 (1.1e-02) | 9.02e-01 (1.9e-02)                    | 1.88e+00 (3.1e-02)                    | 1.98e+00 (6.3e-02)                    | 3.83e-02 (*)   | 0.57 |
| 0.2                | 1.73e+00 (1.6e-02) | 1.79e+00 (3.1e-02) 3.43e+00 (4.8e-02) | 3.48e+00 (1.1e-01)                    | 2.94e-01                              | 0.73           |      |
| SE-0.1             | 0.5                | 4.47e+00 (5.0e-02)                    | 4.58e+00 (6.0e-02)                    | 7.77e+00 (1.4e-01) 7.73e+00 (1.7e-01) | 3.74e-01       | 0.67 |
| 1.0                | 9.31e+00 (8.4e-02) | 9.52e+00 (8.4e-02)                    | 1.45e+01 (2.6e-01) 1.41e+01 (2.5e-01) | 3.91e-04 (***)                        | 0.76           |      |
| 0.1                | 1.45e+00 (2.5e-02) | 1.56e+00 (2.4e-02) 4.42e+00 (5.5e-02) | 4.61e+00 (5.8e-02)                    | 2.37e-07 (***)                        | 0.37           |      |
| 0.2                | 2.19e+00 (3.5e-02) | 2.30e+00 (3.3e-02) 5.46e+00 (5.7e-02) | 5.50e+00 (6.5e-02)                    | 1.78e-01                              | 0.64           |      |
| Mat12-1            | 0.5                | 4.95e+00 (5.5e-02)                    | 5.05e+00 (5.2e-02)                    | 8.18e+00 (9.8e-02) 8.04e+00 (1.1e-01) | 1.52e-02 (*)   | 0.73 |
| 1.0                | 9.80e+00 (9.1e-02) | 9.94e+00 (9.0e-02)                    | 1.21e+01 (2.6e-01) 1.16e+01 (2.2e-01) | 6.76e-04 (***)                        | 0.74           |      |
| 0.1                | 3.41e+00 (6.6e-02) | 3.83e+00 (8.4e-02) 1.16e+01 (1.4e-01) | 1.25e+01 (2.3e-01)                    | 1.85e-06 (***)                        | 0.23           |      |
| 0.2                | 3.75e+00 (7.9e-02) | 4.17e+00 (9.4e-02) 1.24e+01 (1.7e-01) | 1.32e+01 (2.3e-01)                    | 2.05e-07 (***)                        | 0.27           |      |
| Mat12-0.1          | 0.5                | 5.91e+00 (9.0e-02)                    | 6.36e+00 (1.0e-01) 1.56e+01 (1.6e-01) | 1.62e+01 (2.4e-01)                    | 1.01e-03 (**)  | 0.35 |
| 1.0                | 1.04e+01 (1.4e-01) | 1.08e+01 (1.2e-01)                    | 2.11e+01 (2.2e-01) 2.11e+01 (2.3e-01) | 4.48e-01                              | 0.48           |      |
| 0.1                | 9.39e-01 (9.2e-03) | 9.51e-01 (8.3e-03)                    | 1.33e+00 (2.3e-02) 1.29e+00 (2.0e-02) | 5.22e-04 (***)                        | 0.7            |      |
| 0.2                | 1.91e+00 (1.7e-02) | 1.92e+00 (1.6e-02)                    | 2.27e+00 (4.7e-02) 2.18e+00 (4.2e-02) | 1.76e-04 (***)                        | 0.71           |      |
| Mat32-1            | 0.5                | 4.79e+00 (4.0e-02)                    | 4.84e+00 (3.8e-02)                    | 5.01e+00 (1.4e-01) 4.53e+00 (1.1e-01) | 3.31e-07 (***) | 0.66 |
| 1.0                | 9.59e+00 (8.2e-02) | 9.67e+00 (8.1e-02)                    | 8.49e+00 (2.9e-01) 7.58e+00 (2.6e-01) | 3.94e-08 (***)                        | 0.67           |      |
| 0.1                | 1.25e+00 (3.3e-02) | 1.42e+00 (4.2e-02) 3.86e+00 (8.2e-02) | 4.27e+00 (1.3e-01)                    | 1.67e-05 (***)                        | 0.42           |      |
| 0.2                | 1.97e+00 (3.8e-02) | 2.23e+00 (6.7e-02) 5.41e+00 (7.8e-02) | 5.95e+00 (1.9e-01)                    | 1.59e-03 (**)                         | 0.53           |      |
| Mat32-0.1          | 0.5                | 4.66e+00 (5.9e-02)                    | 4.97e+00 (6.9e-02) 1.03e+01 (1.2e-01) | 1.06e+01 (1.8e-01)                    | 2.05e-02 (*)   | 0.55 |
| 1.0                | 9.55e+00 (1.2e-01) | 9.82e+00 (1.2e-01)                    | 1.69e+01 (2.3e-01) 1.67e+01 (2.7e-01) | 4.00e-02 (*)                          | 0.68           |      |
| 0.1                | 8.92e-01 (1.9e-02) | 9.95e-01 (3.3e-02)                    | 2.37e+00 (4.1e-02)                    | 2.58e+00 (1.0e-01)                    | 1.91e-02 (*)   | 0.51 |
| 0.2                | 1.82e+00 (2.7e-02) | 1.95e+00 (3.7e-02) 4.15e+00 (7.0e-02) | 4.36e+00 (1.1e-01)                    | 6.07e-03 (**)                         | 0.57           |      |
| RQ-0.1-0.5         | 0.5                | 4.60e+00 (6.2e-02)                    | 4.84e+00 (7.4e-02)                    | 9.08e+00 (1.5e-01) 8.99e+00 (2.0e-01) | 2.66e-01       | 0.61 |
| 1.0                | 9.30e+00 (9.9e-02) | 9.57e+00 (9.8e-02)                    | 1.48e+01 (2.3e-01) 1.43e+01 (2.2e-01) | 6.64e-03 (**)                         | 0.74           |      |
| 0.1                | 8.82e-01 (3.6e-02) | 9.46e-01 (3.8e-02)                    | 2.44e+00 (1.1e-01)                    | 2.58e+00 (1.2e-01)                    | 2.75e-03 (**)  | 0.54 |
| 0.2                | 1.65e+00 (2.6e-02) | 1.80e+00 (4.4e-02) 4.26e+00 (6.2e-02) | 4.47e+00 (1.3e-01)                    | 3.92e-02 (*)                          | 0.67           |      |
| Periodic-0.1-4 0.5 | 4.34e+00 (5.1e-02) | 4.54e+00 (6.0e-02)                    | 9.44e+00 (1.3e-01) 9.41e+00 (1.9e-01) | 4.14e-01                              | 0.59           |      |
| 1.0                | 9.25e+00 (1.3e-01) | 9.64e+00 (1.3e-01)                    | 1.76e+01 (2.6e-01) 1.72e+01 (2.9e-01) | 3.24e-02 (*)                          | 0.66           |      |

## A.4 Monotone Decomposition Fitting With Smoothing Splines A.4.1 A Complete Version For Table 2

Table 8: Results for comparing the smoothing splines with CV-tuned λ and the fitting by monotone decomposition with CV-tuned (*λ, µ*). The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error.

| curve              | σ                  | MSFE                                  | MSPE                                  | p-value                               | prop.          |      |
|--------------------|--------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------|------|
| SmoothSpline       | MonoDecomp         | SmoothSpline                          | MonoDecomp                            |                                       |                |      |
| 0.1                | 9.57e-01 (8.3e-03) | 9.73e-01 (8.2e-03)                    | 7.38e-01 (2.4e-02)                    | 8.67e-01 (2.4e-02)                    | 1.74e-14 (***) | 0.25 |
| 0.5                | 4.79e+00 (4.1e-02) | 4.80e+00 (4.1e-02)                    | 3.41e+00 (1.2e-01) 3.39e+00 (1.1e-01) | 3.61e-01                              | 0.46           |      |
| 1.0                | 9.65e+00 (8.9e-02) | 9.69e+00 (8.5e-02)                    | 6.44e+00 (2.9e-01) 6.35e+00 (2.5e-01) | 1.68e-01                              | 0.49           |      |
| x 2                | 1.5                | 1.44e+01 (1.1e-01)                    | 1.45e+01 (1.1e-01)                    | 9.31e+00 (3.9e-01) 9.14e+00 (3.4e-01) | 4.68e-02 (*)   | 0.6  |
| 2.0                | 1.92e+01 (1.6e-01) | 1.92e+01 (1.5e-01)                    | 1.23e+01 (4.9e-01) 1.15e+01 (4.3e-01) | 4.45e-06 (***)                        | 0.81           |      |
| 0.1                | 9.46e-01 (8.0e-03) | 9.89e-01 (8.0e-03)                    | 8.65e-01 (2.4e-02)                    | 1.11e+00 (2.5e-02)                    | 0.00e+00 (***) | 0.2  |
| 0.5                | 4.86e+00 (4.4e-02) | 4.88e+00 (4.3e-02)                    | 3.65e+00 (1.2e-01) 3.55e+00 (1.2e-01) | 9.06e-03 (**)                         | 0.58           |      |
| x 3                | 1.0                | 9.75e+00 (8.2e-02)                    | 9.77e+00 (8.2e-02)                    | 6.47e+00 (1.8e-01) 6.21e+00 (1.7e-01) | 1.18e-04 (***) | 0.65 |
| 1.5                | 1.45e+01 (1.1e-01) | 1.46e+01 (1.1e-01)                    | 9.16e+00 (3.1e-01) 8.67e+00 (2.8e-01) | 1.67e-06 (***)                        | 0.81           |      |
| 2.0                | 1.92e+01 (1.8e-01) | 1.92e+01 (1.6e-01)                    | 1.16e+01 (5.9e-01) 1.09e+01 (4.9e-01) | 1.15e-04 (***)                        | 0.78           |      |
| 0.1                | 9.53e-01 (7.6e-03) | 9.64e-01 (7.7e-03)                    | 7.96e-01 (2.6e-02)                    | 9.13e-01 (2.6e-02)                    | 5.02e-12 (***) | 0.26 |
| 0.5                | 4.80e+00 (4.3e-02) | 4.82e+00 (3.9e-02)                    | 3.33e+00 (1.5e-01) 3.30e+00 (1.3e-01) | 2.60e-01                              | 0.51           |      |
| 1.0                | 9.74e+00 (8.4e-02) | 9.75e+00 (8.4e-02)                    | 5.94e+00 (2.3e-01) 5.82e+00 (2.1e-01) | 3.12e-02 (*)                          | 0.58           |      |
| exp(x)             | 1.5                | 1.45e+01 (1.3e-01)                    | 1.46e+01 (1.3e-01)                    | 9.10e+00 (4.4e-01) 8.83e+00 (4.1e-01) | 7.93e-03 (**)  | 0.69 |
| 2.0                | 1.95e+01 (1.5e-01) | 1.95e+01 (1.5e-01)                    | 1.08e+01 (4.9e-01) 1.06e+01 (4.4e-01) | 3.80e-02 (*)                          | 0.57           |      |
| 0.1                | 9.58e-01 (8.0e-03) | 9.58e-01 (7.9e-03)                    | 7.75e-01 (2.7e-02)                    | 7.69e-01 (2.5e-02)                    | 1.81e-01       | 0.56 |
| 0.5                | 4.82e+00 (4.2e-02) | 4.82e+00 (4.2e-02)                    | 3.55e+00 (1.3e-01) 3.49e+00 (1.2e-01) | 2.45e-02 (*)                          | 0.61           |      |
| 1.0                | 9.60e+00 (7.8e-02) | 9.64e+00 (7.5e-02)                    | 5.99e+00 (2.9e-01) 5.68e+00 (2.4e-01) | 4.47e-04 (***)                        | 0.67           |      |
| sigmoid            | 1.5                | 1.43e+01 (1.6e-01)                    | 1.44e+01 (1.5e-01)                    | 8.94e+00 (5.4e-01) 8.36e+00 (4.9e-01) | 5.86e-07 (***) | 0.65 |
| 2.0                | 1.93e+01 (1.6e-01) | 1.94e+01 (1.5e-01)                    | 1.15e+01 (6.4e-01) 1.08e+01 (5.4e-01) | 2.06e-05 (***)                        | 0.7            |      |
| 0.1                | 9.66e-01 (7.5e-03) | 9.71e-01 (7.4e-03)                    | 7.54e-01 (2.4e-02)                    | 8.19e-01 (2.6e-02)                    | 7.24e-08 (***) | 0.26 |
| 0.5                | 4.88e+00 (3.9e-02) | 4.89e+00 (3.8e-02)                    | 3.15e+00 (1.2e-01) 3.10e+00 (1.1e-01) | 5.92e-02 (.)                          | 0.55           |      |
| SE-1               | 1.0                | 9.67e+00 (8.3e-02)                    | 9.70e+00 (8.1e-02)                    | 6.32e+00 (2.8e-01) 6.11e+00 (2.5e-01) | 3.86e-03 (**)  | 0.6  |
| 1.5                | 1.47e+01 (1.1e-01) | 1.47e+01 (1.1e-01)                    | 8.65e+00 (3.8e-01) 8.39e+00 (3.4e-01) | 2.48e-02 (*)                          | 0.55           |      |
| 2.0                | 1.93e+01 (1.5e-01) | 1.94e+01 (1.5e-01)                    | 1.15e+01 (4.3e-01) 1.10e+01 (3.8e-01) | 6.24e-04 (***)                        | 0.7            |      |
| 0.1                | 7.68e-01 (9.1e-03) | 7.94e-01 (9.4e-03) 1.71e+00 (2.7e-02) | 1.79e+00 (3.0e-02)                    | 3.41e-09 (***)                        | 0.24           |      |
| 0.5                | 4.36e+00 (4.4e-02) | 4.40e+00 (4.5e-02) 6.65e+00 (1.0e-01) | 6.72e+00 (1.0e-01)                    | 2.24e-03 (**)                         | 0.42           |      |
| 1.0                | 8.92e+00 (9.2e-02) | 8.99e+00 (9.0e-02)                    | 1.23e+01 (2.1e-01) 1.23e+01 (2.1e-01) | 4.32e-01                              | 0.57           |      |
| SE-0.1             | 1.5                | 1.41e+01 (1.3e-01)                    | 1.42e+01 (1.3e-01)                    | 1.76e+01 (3.1e-01) 1.72e+01 (3.1e-01) | 5.96e-05 (***) | 0.64 |
| 2.0                | 1.89e+01 (1.7e-01) | 1.91e+01 (1.7e-01)                    | 2.16e+01 (4.3e-01) 2.11e+01 (4.3e-01) | 2.13e-04 (***)                        | 0.68           |      |
| 0.1                | 1.16e+00 (2.0e-02) | 1.23e+00 (1.9e-02) 3.71e+00 (2.7e-02) | 3.80e+00 (3.1e-02)                    | 5.72e-14 (***)                        | 0.15           |      |
| 0.5                | 4.80e+00 (4.9e-02) | 4.87e+00 (4.5e-02) 7.50e+00 (8.3e-02) | 7.51e+00 (8.3e-02)                    | 3.83e-01                              | 0.4            |      |
| 1.0                | 9.65e+00 (9.5e-02) | 9.69e+00 (9.2e-02)                    | 1.15e+01 (2.3e-01) 1.13e+01 (2.1e-01) | 3.40e-04 (***)                        | 0.56           |      |
| Mat12-1            | 1.5                | 1.43e+01 (1.1e-01)                    | 1.43e+01 (1.1e-01)                    | 1.40e+01 (3.0e-01) 1.38e+01 (2.8e-01) | 3.13e-03 (**)  | 0.64 |
| 2.0                | 1.96e+01 (1.6e-01) | 1.97e+01 (1.6e-01)                    | 1.69e+01 (4.4e-01) 1.64e+01 (3.7e-01) | 1.97e-04 (***)                        | 0.69           |      |
| 0.1                | 2.60e+00 (3.9e-02) | 2.88e+00 (3.8e-02) 9.86e+00 (7.0e-02) | 1.03e+01 (8.1e-02)                    | 0.00e+00 (***)                        | 0.06           |      |
| 0.5                | 4.81e+00 (6.4e-02) | 5.11e+00 (6.1e-02) 1.35e+01 (8.5e-02) | 1.37e+01 (9.4e-02)                    | 6.90e-06 (***)                        | 0.3            |      |
| Mat12-0.1          | 1.0                | 9.76e+00 (1.2e-01)                    | 9.92e+00 (1.1e-01)                    | 1.90e+01 (2.2e-01) 1.90e+01 (2.2e-01) | 2.06e-01       | 0.58 |
| 1.5                | 1.46e+01 (1.7e-01) | 1.48e+01 (1.6e-01)                    | 2.29e+01 (2.8e-01) 2.25e+01 (2.7e-01) | 1.21e-05 (***)                        | 0.69           |      |
| 2.0                | 1.93e+01 (1.8e-01) | 1.95e+01 (1.7e-01)                    | 2.70e+01 (4.1e-01) 2.65e+01 (3.6e-01) | 3.05e-04 (***)                        | 0.66           |      |
| 0.1                | 9.15e-01 (8.0e-03) | 9.20e-01 (7.7e-03) 1.18e+00 (2.1e-02) | 1.19e+00 (2.2e-02)                    | 5.89e-02 (.)                          | 0.45           |      |
| 0.5                | 4.86e+00 (4.2e-02) | 4.88e+00 (4.0e-02)                    | 4.35e+00 (1.3e-01) 4.32e+00 (1.2e-01) | 2.45e-01                              | 0.52           |      |
| 1.0                | 9.59e+00 (8.5e-02) | 9.64e+00 (7.5e-02)                    | 7.20e+00 (2.4e-01) 7.04e+00 (2.0e-01) | 3.65e-02 (*)                          | 0.49           |      |
| Mat32-1            | 1.5                | 1.45e+01 (1.3e-01)                    | 1.46e+01 (1.3e-01)                    | 1.03e+01 (3.7e-01) 1.00e+01 (3.3e-01) | 7.41e-03 (**)  | 0.65 |
| 2.0                | 1.95e+01 (1.7e-01) | 1.96e+01 (1.7e-01)                    | 1.26e+01 (5.1e-01) 1.19e+01 (4.4e-01) | 6.29e-05 (***)                        | 0.68           |      |
| 0.1                | 8.83e-01 (1.4e-02) | 9.47e-01 (1.4e-02) 2.92e+00 (2.4e-02) | 3.02e+00 (2.6e-02)                    | 3.54e-10 (***)                        | 0.21           |      |
| 0.5                | 4.22e+00 (5.3e-02) | 4.37e+00 (5.0e-02) 8.99e+00 (9.9e-02) | 9.03e+00 (9.9e-02)                    | 1.82e-01                              | 0.45           |      |
| 1.0                | 8.96e+00 (1.1e-01) | 9.14e+00 (1.0e-01)                    | 1.48e+01 (2.2e-01) 1.47e+01 (2.1e-01) | 1.44e-01                              | 0.54           |      |
| Mat32-0.1          | 1.5                | 1.41e+01 (1.6e-01)                    | 1.43e+01 (1.6e-01)                    | 1.99e+01 (3.5e-01) 1.97e+01 (3.4e-01) | 8.29e-02 (.)   | 0.59 |
| 2.0                | 1.92e+01 (1.9e-01) | 1.94e+01 (1.8e-01)                    | 2.36e+01 (4.4e-01) 2.29e+01 (3.9e-01) | 6.38e-08 (***)                        | 0.74           |      |
| 0.1                | 7.21e-01 (9.5e-03) | 7.52e-01 (1.0e-02) 2.04e+00 (2.1e-02) | 2.07e+00 (2.2e-02)                    | 1.35e-04 (***)                        | 0.38           |      |
| 0.5                | 4.31e+00 (4.8e-02) | 4.41e+00 (4.7e-02) 7.50e+00 (9.8e-02) | 7.55e+00 (9.5e-02)                    | 1.36e-01                              | 0.46           |      |
| RQ-0.1-0.5         | 1.0                | 9.10e+00 (1.1e-01)                    | 9.22e+00 (1.1e-01)                    | 1.27e+01 (2.4e-01) 1.25e+01 (2.2e-01) | 1.21e-03 (**)  | 0.6  |
| 1.5                | 1.43e+01 (1.5e-01) | 1.44e+01 (1.5e-01)                    | 1.75e+01 (3.3e-01) 1.74e+01 (3.1e-01) | 1.29e-01                              | 0.5            |      |
| 2.0                | 1.91e+01 (1.9e-01) | 1.92e+01 (1.8e-01)                    | 2.10e+01 (5.4e-01) 2.07e+01 (5.0e-01) | 1.08e-02 (*)                          | 0.63           |      |
| 0.1                | 7.11e-01 (8.8e-03) | 7.44e-01 (1.0e-02) 2.07e+00 (2.7e-02) | 2.11e+00 (2.6e-02)                    | 3.37e-06 (***)                        | 0.27           |      |
| 0.5                | 4.07e+00 (4.6e-02) | 4.20e+00 (4.6e-02) 8.20e+00 (1.2e-01) | 8.35e+00 (1.1e-01)                    | 1.66e-03 (**)                         | 0.27           |      |
| 1.0                | 8.69e+00 (1.0e-01) | 8.89e+00 (9.1e-02)                    | 1.44e+01 (2.1e-01) 1.43e+01 (1.9e-01) | 3.03e-01                              | 0.49           |      |
| Periodic-0.1-4 1.5 | 1.39e+01 (1.7e-01) | 1.42e+01 (1.6e-01)                    | 2.06e+01 (2.7e-01) 2.02e+01 (2.7e-01) | 1.96e-05 (***)                        | 0.67           |      |
| 2.0                | 1.90e+01 (1.8e-01) | 1.92e+01 (1.8e-01)                    | 2.47e+01 (3.9e-01) 2.45e+01 (3.8e-01) | 4.46e-02 (*)                          | 0.63           |      |

## A.4.2 Tune Μ **With Fixed** Λ

First, we fix the parameter λ for the roughness penalty as the CV-tuned one for the smoothing splines. Then, we choose the parameter µ to minimize the CV error. Figure 11 demonstrates the procedure. The left panel shows the CV-error curve for each candidate parameter µ, and the right panel compares the monotone decomposition fitting given the parameter which minimized the curve in the left panel to the smoothing spline fitting. The monotone decomposition achieves a better MSPE, and it is obvious that the better performance is mainly due to the shrinkage on the local modes based on the shapes of fitting curves.

![27_image_0.png](27_image_0.png) 

The average results based on 100 repetitions are summarized in Table 9. The table shows that we can obtain better performance in the high noise cases, and comparable results in the smaller noise scenarios.

Table 9: Results for comparing the smoothing splines with CV-tuned λ and the fitting by monotone decomposition with CV-tuned µ and the same λ. The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean square prediction error.

curve σ SNR MSFE MSPE p-value prop.

SmoothSpline MonoDecomp SmoothSpline MonoDecomp

0.1 1.03e+01 (1.9e-01) 9.30e-03 (1.4e-04) 9.55e-03 (1.4e-04) **6.78e-04** (4.8e-05) 9.03e-04 (5.4e-05) 7.17e-12 (***) 0.24

0.2 2.68e+00 (7.4e-02) 3.72e-02 (6.4e-04) 3.76e-02 (6.3e-04) **2.15e-03** (1.8e-04) 2.29e-03 (1.7e-04) 1.03e-02 (*) 0.33

0.5 5.04e-01 (2.1e-02) 2.35e-01 (3.8e-03) 2.37e-01 (3.6e-03) 1.36e-02 (1.4e-03) **1.23e-02** (9.5e-04) 3.49e-02 (*) 0.44 1.0 1.75e-01 (1.0e-02) 9.48e-01 (1.5e-02) 9.59e-01 (1.5e-02) 5.17e-02 (3.0e-03) **4.81e-02** (2.7e-03) 7.22e-03 (**) 0.48 1.5 1.23e-01 (1.2e-02) 2.07e+00 (3.5e-02) 2.09e+00 (3.6e-02) 1.03e-01 (1.0e-02) **9.57e-02** (8.8e-03) 1.14e-02 (*) 0.57 2.0 1.13e-01 (2.3e-02) 3.82e+00 (5.9e-02) 3.87e+00 (5.6e-02) 1.94e-01 (2.4e-02) **1.55e-01** (1.6e-02) 1.98e-04 (***) 0.63

| 2 x x 3 exp(x) sigmoid SE-1 SE-0.1 Mat12-1 Mat12-0.1 Mat32-1 Mat32-0.1 RQ-0.1-0.5 Periodic-0.1-4   |
|----------------------------------------------------------------------------------------------------|

0.1 1.76e+01 (3.3e-01) 8.80e-03 (1.3e-04) 9.92e-03 (1.4e-04) **8.51e-04** (4.8e-05) 1.70e-03 (7.3e-05) 0.00e+00 (***) 0.15 0.2 4.51e+00 (1.1e-01) 3.62e-02 (6.0e-04) 3.74e-02 (6.1e-04) **2.89e-03** (1.5e-04) 3.11e-03 (1.6e-04) 4.74e-02 (*) 0.51 0.5 7.70e-01 (2.3e-02) 2.33e-01 (3.5e-03) 2.36e-01 (3.5e-03) 1.51e-02 (9.3e-04) **1.36e-02** (8.0e-04) 3.25e-04 (***) 0.52 1.0 2.43e-01 (1.6e-02) 9.44e-01 (1.6e-02) 9.54e-01 (1.6e-02) 5.32e-02 (3.9e-03) **4.63e-02** (2.9e-03) 1.77e-04 (***) 0.69

1.5 1.58e-01 (1.6e-02) 2.09e+00 (3.7e-02) 2.12e+00 (3.5e-02) 1.11e-01 (1.1e-02) **9.53e-02** (1.1e-02) 1.90e-05 (***) 0.69

2.0 1.36e-01 (2.1e-02) 3.75e+00 (7.0e-02) 3.80e+00 (6.6e-02) 1.74e-01 (2.1e-02) **1.37e-01** (1.6e-02) 1.55e-04 (***) 0.74

0.1 5.10e+01 (1.1e+00) 9.06e-03 (1.7e-04) 9.42e-03 (1.6e-04) **6.66e-04** (5.0e-05) 9.11e-04 (5.6e-05) 3.13e-06 (***) 0.36

0.2 1.26e+01 (3.1e-01) 3.65e-02 (6.4e-04) 3.69e-02 (6.0e-04) 2.35e-03 (2.6e-04) **2.34e-03** (1.8e-04) 4.72e-01 0.37

0.5 1.98e+00 (4.5e-02) 2.40e-01 (3.9e-03) 2.41e-01 (3.8e-03) 1.16e-02 (9.4e-04) **1.10e-02** (7.9e-04) 4.03e-02 (*) 0.52 1.0 5.89e-01 (2.2e-02) 9.07e-01 (1.4e-02) 9.14e-01 (1.3e-02) 5.39e-02 (5.7e-03) **4.79e-02** (4.5e-03) 3.84e-04 (***) 0.55 1.5 3.02e-01 (1.9e-02) 2.11e+00 (3.6e-02) 2.13e+00 (3.5e-02) 1.02e-01 (1.0e-02) **9.10e-02** (8.7e-03) 5.87e-04 (***) 0.62

2.0 2.00e-01 (2.9e-02) 3.79e+00 (6.3e-02) 3.81e+00 (6.2e-02) 1.71e-01 (2.7e-02) **1.53e-01** (2.4e-02) 1.71e-04 (***) 0.72

0.1 1.70e+01 (3.2e-01) 9.31e-03 (1.4e-04) 9.36e-03 (1.4e-04) 6.33e-04 (4.3e-05) **6.03e-04** (3.3e-05) 5.12e-02 (.) 0.55

0.2 4.38e+00 (6.9e-02) 3.66e-02 (4.6e-04) 3.68e-02 (4.6e-04) 2.44e-03 (1.7e-04) **2.39e-03** (1.6e-04) 7.53e-02 (.) 0.61

0.5 7.87e-01 (2.7e-02) 2.32e-01 (4.0e-03) 2.33e-01 (3.9e-03) 1.50e-02 (1.0e-03) **1.34e-02** (7.9e-04) 1.59e-05 (***) 0.63 1.0 2.31e-01 (1.3e-02) 9.44e-01 (1.6e-02) 9.51e-01 (1.6e-02) 3.96e-02 (3.9e-03) **3.43e-02** (3.1e-03) 8.84e-06 (***) 0.67 1.5 1.70e-01 (1.5e-02) 2.09e+00 (3.3e-02) 2.12e+00 (3.1e-02) 1.12e-01 (1.0e-02) **8.82e-02** (7.8e-03) 4.95e-05 (***) 0.64

2.0 1.26e-01 (1.9e-02) 3.69e+00 (6.5e-02) 3.73e+00 (6.3e-02) 1.67e-01 (2.4e-02) **1.32e-01** (1.7e-02) 1.58e-04 (***) 0.75

0.1 3.43e+01 (4.3e+00) 9.02e-03 (1.6e-04) 9.16e-03 (1.5e-04) 7.53e-04 (7.0e-05) **7.32e-04** (5.5e-05) 2.40e-01 0.43

0.2 5.41e+00 (6.9e-01) 3.77e-02 (6.6e-04) 3.78e-02 (6.5e-04) **2.31e-03** (2.0e-04) 2.36e-03 (1.9e-04) 2.04e-01 0.4

0.5 1.20e+00 (1.4e-01) 2.38e-01 (3.9e-03) 2.39e-01 (3.8e-03) 1.24e-02 (1.2e-03) **1.12e-02** (9.5e-04) 7.34e-03 (**) 0.51 1.0 3.59e-01 (3.9e-02) 9.38e-01 (1.6e-02) 9.50e-01 (1.6e-02) 4.74e-02 (3.6e-03) **4.12e-02** (2.8e-03) 4.67e-04 (***) 0.63 1.5 1.68e-01 (1.9e-02) 2.13e+00 (3.2e-02) 2.15e+00 (3.2e-02) 9.58e-02 (8.1e-03) **8.60e-02** (6.7e-03) 3.72e-04 (***) 0.6

2.0 1.18e-01 (1.2e-02) 3.68e+00 (5.9e-02) 3.71e+00 (5.7e-02) 1.69e-01 (1.6e-02) **1.48e-01** (1.2e-02) 2.36e-04 (***) 0.75

0.1 1.50e+02 (6.4e+00) 6.36e-03 (1.3e-04) 7.06e-03 (1.8e-04) **3.00e-03** (7.7e-05) 3.51e-03 (1.6e-04) 3.81e-05 (***) 0.25

0.2 3.55e+01 (1.9e+00) 2.79e-02 (5.5e-04) 2.90e-02 (5.7e-04) **1.00e-02** (3.1e-04) 1.05e-02 (3.3e-04) 6.47e-05 (***) 0.39 0.5 4.98e+00 (2.3e-01) 1.97e-01 (3.9e-03) 2.02e-01 (3.7e-03) **4.70e-02** (1.7e-03) 4.74e-02 (1.5e-03) 2.98e-01 0.38

1.0 1.30e+00 (6.9e-02) 8.23e-01 (1.6e-02) 8.54e-01 (1.5e-02) **1.54e-01** (5.3e-03) 1.55e-01 (4.6e-03) 3.62e-01 0.35 1.5 6.35e-01 (3.9e-02) 1.96e+00 (4.0e-02) 2.02e+00 (4.0e-02) **3.20e-01** (1.2e-02) 3.23e-01 (1.3e-02) 2.79e-01 0.51

2.0 3.69e-01 (2.3e-02) 3.71e+00 (6.7e-02) 3.79e+00 (6.8e-02) 4.69e-01 (1.8e-02) **4.62e-01** (1.7e-02) 1.57e-01 0.54

0.1 3.51e+01 (2.7e+00) 1.41e-02 (4.1e-04) 1.58e-02 (4.3e-04) **1.40e-02** (2.3e-04) 1.48e-02 (2.6e-04) 3.30e-10 (***) 0.2

0.2 1.29e+01 (9.7e-01) 3.80e-02 (1.0e-03) 4.17e-02 (9.8e-04) **2.39e-02** (4.6e-04) 2.44e-02 (5.0e-04) 1.39e-02 (*) 0.43 0.5 1.97e+00 (1.5e-01) 2.27e-01 (4.6e-03) 2.38e-01 (4.4e-03) 5.88e-02 (1.7e-03) **5.78e-02** (1.5e-03) 1.09e-01 0.54

1.0 6.51e-01 (5.1e-02) 9.19e-01 (1.6e-02) 9.40e-01 (1.5e-02) 1.26e-01 (4.8e-03) **1.20e-01** (4.1e-03) 1.12e-03 (**) 0.57 1.5 3.52e-01 (4.4e-02) 2.10e+00 (3.4e-02) 2.14e+00 (3.1e-02) 2.13e-01 (1.2e-02) **1.97e-01** (9.0e-03) 2.02e-02 (*) 0.62 2.0 1.71e-01 (1.9e-02) 3.76e+00 (6.0e-02) 3.81e+00 (5.9e-02) 2.94e-01 (2.1e-02) **2.75e-01** (1.8e-02) 1.00e-03 (**) 0.61 0.1 1.51e+01 (8.5e-01) 6.84e-02 (2.5e-03) 8.71e-02 (3.1e-03) **9.73e-02** (1.8e-03) 1.10e-01 (2.3e-03) 7.39e-13 (***) 0.1

0.2 9.80e+00 (5.0e-01) 9.35e-02 (2.9e-03) 1.12e-01 (3.5e-03) **1.14e-01** (1.7e-03) 1.26e-01 (2.5e-03) 3.16e-11 (***) 0.1

0.5 3.90e+00 (2.3e-01) 2.55e-01 (7.8e-03) 2.90e-01 (7.9e-03) **1.92e-01** (3.0e-03) 2.02e-01 (3.5e-03) 8.52e-08 (***) 0.2 1.0 1.24e+00 (7.2e-02) 9.43e-01 (2.5e-02) 1.01e+00 (2.3e-02) **3.62e-01** (7.5e-03) 3.65e-01 (7.5e-03) 2.24e-01 0.25

1.5 5.39e-01 (4.7e-02) 2.15e+00 (5.0e-02) 2.23e+00 (4.6e-02) 5.26e-01 (1.7e-02) **5.14e-01** (1.3e-02) 8.29e-02 (.) 0.51

2.0 3.22e-01 (3.3e-02) 3.85e+00 (8.0e-02) 3.94e+00 (7.4e-02) 7.69e-01 (2.3e-02) **7.36e-01** (2.2e-02) 7.18e-04 (***) 0.5

0.1 3.78e+01 (3.8e+00) 8.48e-03 (1.6e-04) 8.70e-03 (1.6e-04) **1.50e-03** (5.1e-05) 1.57e-03 (5.1e-05) 1.71e-02 (*) 0.4

0.2 1.11e+01 (1.0e+00) 3.50e-02 (6.3e-04) 3.57e-02 (6.0e-04) **4.32e-03** (2.0e-04) 4.37e-03 (1.9e-04) 2.68e-01 0.47

0.5 1.70e+00 (1.6e-01) 2.32e-01 (3.6e-03) 2.35e-01 (3.6e-03) 1.95e-02 (1.1e-03) **1.87e-02** (9.8e-04) 1.28e-02 (*) 0.48 1.0 4.05e-01 (3.9e-02) 9.54e-01 (1.4e-02) 9.65e-01 (1.4e-02) 6.44e-02 (4.2e-03) **6.09e-02** (3.9e-03) 5.44e-03 (**) 0.57 1.5 2.24e-01 (2.4e-02) 2.17e+00 (3.9e-02) 2.18e+00 (3.8e-02) 1.13e-01 (1.1e-02) **1.01e-01** (8.2e-03) 1.09e-03 (**) 0.6 2.0 1.55e-01 (1.4e-02) 3.79e+00 (6.3e-02) 3.84e+00 (6.2e-02) 1.94e-01 (1.6e-02) **1.62e-01** (1.2e-02) 4.61e-05 (***) 0.74 0.1 1.30e+02 (6.8e+00) 7.72e-03 (2.2e-04) 9.77e-03 (3.8e-04) **8.67e-03** (2.0e-04) 9.84e-03 (3.0e-04) 2.79e-05 (***) 0.27

0.2 4.25e+01 (2.6e+00) 2.47e-02 (7.1e-04) 2.88e-02 (8.5e-04) **2.04e-02** (3.6e-04) 2.15e-02 (5.4e-04) 3.83e-03 (**) 0.32

0.5 5.49e+00 (2.8e-01) 1.81e-01 (4.9e-03) 2.01e-01 (5.2e-03) **8.16e-02** (2.2e-03) 8.51e-02 (2.4e-03) 1.74e-03 (**) 0.4

1.0 1.34e+00 (6.7e-02) 8.44e-01 (2.0e-02) 9.01e-01 (1.9e-02) 2.44e-01 (7.8e-03) **2.40e-01** (7.6e-03) 6.21e-02 (.) 0.41

1.5 6.73e-01 (4.4e-02) 1.99e+00 (4.1e-02) 2.07e+00 (3.9e-02) 3.98e-01 (1.6e-02) **3.82e-01** (1.3e-02) 4.94e-03 (**) 0.5 2.0 3.67e-01 (3.0e-02) 3.76e+00 (6.6e-02) 3.87e+00 (6.2e-02) 5.92e-01 (2.6e-02) **5.64e-01** (2.0e-02) 8.86e-03 (**) 0.6 0.1 1.23e+02 (6.6e+00) 5.70e-03 (1.5e-04) 6.56e-03 (1.9e-04) **4.33e-03** (8.3e-05) 4.71e-03 (1.0e-04) 2.57e-07 (***) 0.28

0.2 3.44e+01 (2.0e+00) 2.47e-02 (6.1e-04) 2.66e-02 (6.3e-04) **1.30e-02** (3.2e-04) 1.34e-02 (3.3e-04) 2.92e-03 (**) 0.34

0.5 4.27e+00 (2.4e-01) 1.94e-01 (4.5e-03) 2.10e-01 (5.0e-03) **5.97e-02** (1.6e-03) 6.17e-02 (1.7e-03) 6.21e-02 (.) 0.41 1.0 1.07e+00 (6.2e-02) 8.53e-01 (1.8e-02) 8.92e-01 (1.7e-02) 1.72e-01 (6.8e-03) **1.70e-01** (6.1e-03) 3.52e-01 0.43 1.5 4.43e-01 (3.3e-02) 2.11e+00 (3.9e-02) 2.15e+00 (3.8e-02) 3.05e-01 (1.0e-02) **3.02e-01** (1.0e-02) 3.03e-01 0.49 2.0 3.07e-01 (2.4e-02) 3.83e+00 (6.6e-02) 3.92e+00 (6.6e-02) 4.56e-01 (1.8e-02) **4.43e-01** (1.6e-02) 3.16e-02 (*) 0.54

Periodic-0.1-4

0.1 1.90e+02 (7.8e+00) 5.22e-03 (1.3e-04) 6.09e-03 (2.5e-04) **4.37e-03** (9.4e-05) 4.99e-03 (2.3e-04) 1.19e-03 (**) 0.34

0.2 4.32e+01 (2.3e+00) 2.35e-02 (4.9e-04) 2.60e-02 (6.4e-04) **1.45e-02** (3.6e-04) 1.54e-02 (4.9e-04) 2.14e-03 (**) 0.3

0.5 6.84e+00 (3.2e-01) 1.66e-01 (4.2e-03) 1.76e-01 (4.6e-03) **6.68e-02** (1.8e-03) 6.84e-02 (1.9e-03) 3.44e-02 (*) 0.51

1.0 1.59e+00 (8.1e-02) 7.92e-01 (1.9e-02) 8.49e-01 (1.9e-02) **2.27e-01** (7.4e-03) 2.34e-01 (7.8e-03) 5.08e-02 (.) 0.48 1.5 6.94e-01 (5.0e-02) 1.96e+00 (4.3e-02) 2.06e+00 (4.4e-02) 4.40e-01 (1.4e-02) **4.35e-01** (1.4e-02) 2.60e-01 0.55 2.0 4.22e-01 (3.9e-02) 3.62e+00 (8.5e-02) 3.72e+00 (8.4e-02) 6.51e-01 (2.3e-02) **6.30e-01** (2.0e-02) 1.19e-02 (*) 0.62

29

## A.4.3 Tune The Shrinkage Factor K

In light of Proposition 6, we tune the shrinkage factor k instead of ( λ, µ ).  It shows that the monotone decomposition with the shrinkage factor can achieve better performance in high noise cases for monotone functions such as x 3 , exp( x ) and sigmoid function. Promisingly, it also works for x 2 and SE_1, although Proposition 6 is intended for pure monotone functions.

![29_image_0.png](29_image_0.png)

## A.5 Qq Plots Of P-Values

![30_image_0.png](30_image_0.png) ![30_image_1.png](30_image_1.png)

![31_image_0.png](31_image_0.png)

![31_image_1.png](31_image_1.png)

![32_image_0.png](32_image_0.png)

![32_image_1.png](32_image_1.png)

![33_image_0.png](33_image_0.png)

![33_image_1.png](33_image_1.png)

## A.6 Different Curves For Testing The Monotonicity

![34_image_0.png](34_image_0.png) 

## B More Go Analysis

Figure 22 is the same as Figure 8except that panel (d) displays the GO terms identified by the interaction of DE genes and ME genes (the complementary of nME genes). Similar to DE genes, the interaction of DE genes and ME genes failed to identify significant GO terms.

![35_image_0.png](35_image_0.png) 
For the liver dataset, the GO terms identified by different gene sets are shown in Figure 23.

Most GO terms selected by the DE genes (Figure 23b) and by the ME&DE genes (Figure 23d) are the same. The numbers of different GO terms are illustrated in the Venn diagram of Figure 24.

![36_image_0.png](36_image_0.png) 

![37_image_0.png](37_image_0.png)

Figures 25 and 26 display the distinct GO terms selected by DE genes and ME genes, respectively. Note that the counts of GO terms and associated p-values are relatively small compared to their common GO terms.

![38_image_0.png](38_image_0.png)

![39_image_0.png](39_image_0.png)

## C Theoretical Proofs Of Some Basic Propositions C.1 A Proposition

Proposition 7. Suppose f(x) is a univariate continuous function in an interval I*, there exists a decomposition* f(x) = fup(x) + fdown(x). (16)
where fup(x) and fdown(x) *are continuous increasing and decreasing functions, respectively.*
Proof. Decompose the interval I as I = ∪
n k=1[a2k−1, a2k] .

Without loss of generality, suppose f(x) is increasing in [a2k−1, a2k] and decreasing in [a2k, a2k+1].

Then one feasible decomposition is

$$f_{\mathrm{up}}(x)=\begin{cases}f(a_{2})&x\in[a_{1},a_{2}]\\ f(a_{2})&x\in[a_{2},a_{3}]\\ f(x)-f(a_{3})+f(a_{2})&x\in[a_{3},a_{4}]\\ f(a_{4})-f(a_{3})+f(a_{2})&x\in[a_{4},a_{5}]\\ \ldots&\ldots\\ f(x)+\sum_{i=2}^{k}(f(a_{2i-2})-f(a_{2i-1}))&x\in[a_{2k-1},a_{2k}],k\geq2\\ f(a_{2k})+\sum_{i=2}^{k}(f(a_{2i-2})-f(a_{2i-1}))&x\in[a_{2k},a_{2k+1}],k\geq2\end{cases}$$
f(x) x ∈ [a1, a2]
,
and fdown(x) = f(x) − fup(x).

## C.2 Proposition 1

Proof. Consider the problem

$$\operatorname*{min}_{\gamma^{u},\gamma^{d}}\|y-\mathbf{B}(\gamma^{u}+\gamma^{d})\|_{2}$$
$\gamma^{u},\gamma^{d}$  s.t. $\gamma^{u}_{1}\leq\gamma^{u}_{2}\leq\cdots\leq\gamma^{u}_{J}$; $\gamma^{d}_{1}\geq\gamma^{d}_{2}\geq\cdots\geq\gamma^{d}_{J}$  $\gamma^{u}+\gamma^{d}=\hat{\gamma}$,
$$(17)$$
$$(18)$$

where γˆ is the unconstrained solution. Since we can always decompose a vector into the sum of an increasing vector and a decreasing vector. For 2 ≤ i ≤ J, let

$$\begin{array}{l}{{\hat{\gamma}_{i}^{u}=\hat{\gamma}_{i-1}^{u}+(\hat{\gamma}_{i}-\hat{\gamma}_{i-1})_{+}}}\\ {{\hat{\gamma}_{i}^{d}=\hat{\gamma}_{i-1}^{d}+(\hat{\gamma}_{i}-\hat{\gamma}_{i-1})_{-}\;,}}\end{array}$$
i−1 + (ˆγi − γˆi−1)+ (18)
i−1 + (ˆγi − γˆi−1)− , (19)
where t+ = max(0, t) and t− = min(0, t). And γˆ
u 1 + ˆγ d 1 = ˆγ1 ,
for example, take γˆ
u 1 = ˆγ1 and γˆ
d 1 = 0. Thus the constraints are feasible, i.e., non-empty, and then any solution would satisfy γˆ
u + ˆγ d = ˆγ .

## C.3 Proposition 2

Proof. Here we only prove the second property since the first property has been incorporated into the proof for the main propositions in Sections D.2 and G.3.

We can also put the constraint γ ∈ Υ into the Lagrangian form. Define

$$\mathbf{A}\triangleq\begin{bmatrix}\mathbf{I}_{J-1}&0\end{bmatrix}-\begin{bmatrix}0&\mathbf{I}_{J-1}\end{bmatrix}=\begin{bmatrix}1&-1&0&\cdots&0&0\\ 0&1&-1&\cdots&0&0\\ 0&0&1&\cdots&0&0\\ \vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\ 0&0&0&\cdots&1&-1\end{bmatrix}\qquad,\quad\mathbf{H}\triangleq\begin{bmatrix}\mathbf{A}&\mathbf{0}\\ \mathbf{0}&-\mathbf{A}\end{bmatrix},$$

and the Lagrange form is

$$L_{\mathrm{ls}}(\gamma,\nu,\mu)=\|{\bf y}-{\bf Z}\gamma\|_{2}^{2}+2\nu^{T}{\bf H}\gamma+\mu\gamma^{T}{\bf W}\gamma\,,$$
T Hγ + µγTWγ , (20)
where 2(J −1)-vector ν and scalar µ are the Lagrange multipliers, and factor 2 is just for convenient formulas after taking the first derivatives. Take the derivatives on the Lagrange form,

$$-2{\bf Z}^{T}(y-{\bf Z}\gamma)+2{\bf H}^{T}\nu+2\mu{\bf W}\gamma+2\lambda\begin{bmatrix}{\bf\Omega}&{\bf\Omega}\\ {\bf\Omega}&{\bf\Omega}\end{bmatrix}\gamma=0\,,$$

where if λ = 0, it reduces to the cubic spline. Then

$$\begin{array}{c}{{-{\bf B}_{i}^{T}({\bf y}-{\bf Z}\gamma)+{\bf H}_{i}^{T}\nu+\mu{\bf B}_{i}^{T}{\bf B}(\gamma^{u}-\gamma^{d})+\lambda{\bf\Omega}_{i}(\gamma^{u}+\gamma^{d})=0}}\\ {{-{\bf B}_{i}^{T}({\bf y}-{\bf Z}\gamma)+{\bf H}_{i+J}^{T}\nu+\mu{\bf B}_{i}^{T}{\bf B}(-\gamma^{u}+\gamma^{d})+\lambda{\bf\Omega}_{i}(\gamma^{u}+\gamma^{d})=0}}\end{array}$$

Note that

$$\begin{array}{l}{(21)}\\ {(22)}\end{array}$$
$$\sum_{i=1}^{J}\mathbf{H}_{i}^{T}\nu=0\,,$$

and

$$\sum_{i=1}^{J}\mathbf{H}_{i+J}^{T}\nu=0\,,$$

then we have
$$\mu{\bf1}^{T}{\bf B}^{T}{\bf B}(\gamma^{u}-\gamma^{d})=\mu{\bf1}^{T}{\bf B}^{T}{\bf B}(-\gamma^{u}+\gamma^{d})\,,$$
which implies
$$\mu{\bf1}^{T}{\bf B}(\gamma^{u}-\gamma^{d})=\mu{\bf1}^{T}{\bf B}(-\gamma^{u}+\gamma^{d})\,,$$
so
$$2\mu{\bf1}^{T}{\bf B}\gamma^{u}=2\mu{\bf1}^{T}{\bf B}\gamma^{d}\,.$$

If µ = 0, by KKT condition, then Bγ u − Bγ d = 0. If µ ̸= 0, then 1 T Bγ u = 1 T Bγ d.

Thus, 1 T Bγ u = 1 T Bγ d always holds.

## D Proof Of Proposition 3

Lemma 1 (Chebyshev Sum Inequality). If a1 ≥ a2 ≥ · · · ≥ an, and b1 ≥ b2 ≥ · · · ≥ bn*, then*

$$n\sum_{k=1}^{n}a_{k}b_{k}\geq\left(\sum_{k=1}^{n}a_{k}\right)\left(\sum_{k=1}^{n}b_{k}\right)$$

Proof. Since these two sequences are decreasing, then the sum

$$S=\sum_{j=1}^{n}\sum_{k=1}^{n}(a_{j}-a_{k})(b_{j}-b_{k})\geq0\,.$$

Note that

$$S=\sum_{j=1}^{n}\left(na_{j}b_{j}-b_{j}\sum_{k=1}^{n}a_{k}-a_{j}\sum_{k=1}^{n}b_{k}+\sum_{k=1}^{n}a_{k}b_{k}\right)$$ $$=n\sum_{j=1}^{n}a_{j}b_{j}+n\sum_{k=1}^{n}a_{k}b_{k}-\sum_{j=1}^{n}b_{j}\sum_{k=1}^{n}a_{k}-\sum_{j=1}^{n}a_{j}\sum_{k=1}^{n}b_{k}$$ $$=2n\sum_{k=1}^{n}a_{k}b_{k}-2\sum_{k=1}^{n}b_{k}\sum_{k=1}^{n}a_{k}\;,$$  $$n\sum_{k=1}^{n}a_{k}b_{k}\geq\left(\sum_{k=1}^{n}a_{k}\right)\left(\sum_{k=1}^{n}b_{k}\right)\;.$$

$$\square$$

hence

## D.1 (I)

Proof. Suppose γ = γ u + γ dis increasing, then we have a decomposition in which γ dis a vector with identical elements. Write the decomposition as γ = γ u + c1, where c is a constant. If there exists a non-zero non-decreasing vector δ such that the non-increasing part is not a constant, i.e.,

$$\gamma=(\gamma^{u}+\delta)+(c{\bf1}-\delta)\triangleq\tilde{\gamma}^{u}+\tilde{\gamma}^{d}\,.$$
Then
$$\|y-{\bf B}(\gamma^{u}+c{\bf1})\|=\|y-{\bf B}(\hat{\gamma}^{u}+\hat{\gamma}^{d})\|\,,$$

and if we impose the roughness penalty, we have

$$(\gamma^{u}+\gamma^{d})^{T}\Omega(\gamma^{u}+\gamma^{d})=(\tilde{\gamma}^{u}+\tilde{\gamma}^{d})^{T}\Omega(\tilde{\gamma}^{u}+\tilde{\gamma}^{d})\,.$$

So the first two terms in the Lagrange objective function (13) are the same, and we only need to compare the difference between these two components,

$$\begin{array}{r l}{{}}&{{}\|{\bf B}(\tilde{\gamma}^{u}-\tilde{\gamma}^{d})\|_{2}^{2}-\|{\bf B}(\gamma^{u}-\gamma^{d})\|_{2}^{2}}}\\ {{}}&{{}=(\tilde{\gamma}^{u}-\tilde{\gamma}^{d}-(\gamma^{u}-\gamma^{d}))^{T}{\bf B}^{T}{\bf B}(\tilde{\gamma}^{u}-\tilde{\gamma}^{d}+(\gamma^{u}-\gamma^{d}))}}\\ {{}}&{{}=2\delta^{T}{\bf B}^{T}{\bf B}(2\gamma^{u}+2\delta-2c{\bf1})}}\\ {{}}&{{}=4\left\{\delta^{T}{\bf B}^{T}{\bf B}\delta+\delta^{T}{\bf B}^{T}{\bf B}(\gamma^{u}-c{\bf1})\right\}\,.}\end{array}$$

By Proposition 2, we have

$${\bf1}^{T}{\bf B}\gamma^{u}={\bf1}^{T}{\bf B}\gamma^{d}\qquad{\bf1}^{T}{\bf B}\tilde{\gamma}^{u}={\bf1}^{T}{\bf B}\tilde{\gamma}^{d}\,,$$
then
$${\bf1}^{T}{\bf B}(\gamma^{u}-c{\bf1})={\bf1}^{T}{\bf B}\delta=0\,.$$
Let $\mathbf{a}=\mathbf{B}\delta,\mathbf{b}=\mathbf{B}(\gamma^u-c\mathbf{1})$, then by Fact 1, . 
$$\mathbf{a}^{T}\mathbf{b}\geq{\frac{1}{n}}(\mathbf{1}^{T}\mathbf{a})(\mathbf{1}^{T}\mathbf{b})=0\,.$$

And δ T BT Bδ > 0 for non-zero δ, thus,

$$\|{\bf B}(\hat{\gamma}^{u}-\hat{\gamma}^{d})\|_{2}^{2}>\|{\bf B}(\gamma^{u}-\gamma^{d})\|_{2}^{2}\,.$$
 So if $\gamma^u+\gamma^d$ is increase  Note that  . 
dis increasing, the best decomposition is γ d = c1.

$${\bf1}^{T}{\bf B}\gamma^{u}={\bf1}^{T}{\bf B}c{\bf1}=c{\bf1}^{T}{\bf1}\,,$$

the constant c is

$$c=\frac{{\bf1}^{T}{\bf B}\gamma^{u}}{n}\,.$$
$$(23)$$

D.2 (ii)
Proof. Take the derivatives on the Lagrange form,

$$\mathbf{Z}_{\gamma})+$$

−2Z
T(y − Zγ) + 2HTν + 2µWγ = 0 (23)
then

γˆ = (Z T Z + µW) −1(Z Ty − HTν) ≜ (Z T Z + µW) −1Z Ty − (Z T Z + µW) −1ξ ,
where ξ ≜ HT ν. Note that

$$(\mathbf{Z}^{T}\mathbf{Z}+\mu\mathbf{W})^{-1}=\begin{bmatrix}1+\mu&1-\mu\\ 1-\mu&1+\mu\end{bmatrix}^{-1}\otimes(\mathbf{B}^{T}\mathbf{B})^{-1}={\frac{1}{4\mu}}\begin{bmatrix}\mu+1&\mu-1\\ \mu-1&\mu+1\end{bmatrix}\otimes(\mathbf{B}^{T}\mathbf{B})^{-1}\,,$$

then

$$(\mathbf{Z}^{T}\mathbf{Z}+\mu\mathbf{W})^{-1}\mathbf{Z}^{T}y=\left\{\frac{1}{4\mu}\begin{bmatrix}\mu+1&\mu-1\\ \mu-1&\mu+1\end{bmatrix}\begin{bmatrix}1\\ 1\end{bmatrix}\right\}\otimes(\mathbf{B}^{T}\mathbf{B})^{-1}\mathbf{B}^{T}y=\frac{1}{2}\begin{bmatrix}1\\ 1\end{bmatrix}\otimes(\mathbf{B}^{T}\mathbf{B})^{-1}\mathbf{B}^{T}y\,.$$  Consider the $i$-th element of (23),
$$-{\bf Z}_{i}^{T}(y-{\bf Z}\gamma)+{\bf H}_{i}^{T}\nu+\mu{\bf W}_{i}^{T}\gamma=0\,,$$
i γ = 0 , (24)
where Zi, Hi,Wi are the i-th column of Z, H,W, respectively. Note that for 1 ≤ i ≤ J,

$$\mathbf{W}_{i}={\begin{bmatrix}\mathbf{B}^{T}\mathbf{B}_{i}\\ -\mathbf{B}^{T}\mathbf{B}_{i}\end{bmatrix}}\,,\qquad\mathbf{W}_{i+J}={\begin{bmatrix}-\mathbf{B}^{T}\mathbf{B}_{i}\\ \mathbf{B}^{T}\mathbf{B}_{i}\end{bmatrix}}\,,$$

44 and Zi = Bi, Zi+J = Bi, where Biis the i-th column of B. Then (24) turns out to be

$$\begin{array}{c}{{-{\bf B}_{i}^{T}(y-{\bf Z}\gamma)+{\bf H}_{i}^{T}\nu+\mu{\bf B}_{i}^{T}{\bf B}(\gamma^{u}-\gamma^{d})=0\,,}}\\ {{-{\bf B}_{i}^{T}(y-{\bf Z}\gamma)+{\bf H}_{i+J}^{T}\nu+\mu{\bf B}_{i}^{T}{\bf B}(-\gamma^{u}+\gamma^{d})=0\,.}}\end{array}$$

(25) + (26) yields
$$(\mathbf{H}_{i}^{T}-\mathbf{H}_{i+J}^{T})\nu=-2\mu\mathbf{B}_{i}^{T}\mathbf{B}(\gamma^{u}-\gamma^{d})\,,$$
d), (27)
and (25) - (26) yields
$$({\bf H}_{i}^{T}+{\bf H}_{i+J}^{T})\nu=2{\bf B}_{i}^{T}(y-{\bf Z}\gamma)\,.$$
If there is no ties in the solution, i.e.,

$$\gamma_{1}^{u}<\gamma_{2}^{u}<\cdots<\gamma_{J}^{u}\,,\qquad\gamma_{1}^{d}>\gamma_{2}^{d}>\cdots>\gamma_{J}^{d}\,,$$

by the KKT condition, ν = 0, and then (27) implies µ = 0. Then it reduces to unconstrained B-spline fitting. This argument proves the first point of Proposition 2.

If

$$\gamma_{1}^{u}<\gamma_{2}^{u}<\ldots<\gamma_{J}^{u}\,,$$
then from (27), we have
$$\xi_{i+J}=2\mu{\bf B}_{i}^{T}{\bf B}(\gamma^{u}-\gamma^{d})\,,$$

then it follows that

$$\xi={\begin{bmatrix}0\\ 1\end{bmatrix}}\otimes2\mu\mathbf{B}^{T}\mathbf{B}(\gamma^{u}-\gamma^{d})\,,$$
$$(\mathbf{Z}^{T}\mathbf{Z}+\mu\mathbf{W})^{-1}\xi={\frac{1}{2}}\begin{bmatrix}\mu-1\\ \mu+1\end{bmatrix}\otimes(\gamma^{u}-\gamma^{d})\,.$$
Soγ
$$\left[\gamma^{u}\right]=\frac{1}{2}\left[(\mathbf{B}^{T}\mathbf{B})^{-1}\mathbf{B}^{T}y-(\mu-1)(\gamma^{u}-\gamma^{d})\right]\,,$$
both yield
$$(\mu+1)\gamma^{u}-(\mu-1)\gamma^{d}=(\mathbf{B}^{T}\mathbf{B})^{-1}\mathbf{B}^{T}y\,.$$

On the other hand, from (25), we have

$$-{\bf B}^{T}(y-{\bf Z}\gamma)+\mu{\bf B}^{T}{\bf B}(\gamma^{u}-\gamma^{d})=0\,,$$
that is,
$$(\gamma^{u}+\gamma^{d})+\mu(\gamma^{u}-\gamma^{d})=(\mathbf{B}^{T}\mathbf{B})^{-1}\mathbf{B}^{T}y\,,$$
that is,
$$(\mu+1)\gamma^{u}-(\mu-1)\gamma^{d}=(\mathbf{B}^{T}\mathbf{B})^{-1}\mathbf{B}^{T}y\triangleq\hat{\gamma}^{\mathrm{ls}}\,.$$

Incorporate with the result in Section D.1, we have

$$\gamma^{d}=c{\bf1}\,,\gamma^{u}=\frac{1}{\mu+1}\hat{\gamma}^{\mathrm{ls}}+\frac{\mu-1}{\mu+1}c{\bf1}\,.$$
$\square$
D.3 (iii) Proof. Note that   ξ1 = ν1 ξ2 = ν2 − ν1 ... ξJ−1 = νJ−1 − νJ−2 ξJ = −νJ−1 (28) If γˆ u 1 < · · · < γˆ u k1 = · · · = ˆγ u k2 < · · · < γˆ u k2m−1 = · · · = ˆγ u k2m < γˆJ , then   ξ1 = · · · = ξk1−1 = 0 ... k X2−1   ν1 = · · · = νk1−1 = 0 ... νk2m−2 = · · · = νk2m−1 = 0 νk2m = · · · = νJ−1 = 0 i=k1 ξi = 0 =⇒ ... k2Xm−1 i=k2m−1 ξi = 0 ξk2m = · · · = ξJ = 0 Thus,
B T 1y = (µ + 1)B T 1 Bγ u − (µ − 1)B T 1 Bγ d ... B T k1−1 y = (µ + 1)B T k1−1Bγ u − (µ − 1)B T k1−1Bγ d k X2−1 i=k1 B T iy = (µ + 1) k X2−1 i=k1 B T i Bγ u − (µ − 1) k X2−1 i=k1 B T i Bγ d ... k2Xm−1 i=k2m−2 B T iy = (µ + 1) k2Xm−1 i=k2m−2 B T i Bγ u − (µ − 1) k2Xm−1 i=k2m−2 B T i Bγ d B T k2m y = (µ + 1)B T k2mBγ u − (µ − 1)B T k2mBγ d ... B T Jy = (µ + 1)B T J Bγ u − (µ − 1)B T J Bγ d.
Then
$$\mathbf{G}\mathbf{B}^{T}y=(\mu+1)\mathbf{G}\mathbf{B}^{T}\mathbf{B}\gamma^{u}-(\mu-1)\mathbf{G}\mathbf{B}^{T}\mathbf{B}\gamma^{d}\,,$$

where

G = 
  Ik1−11 T k2−k1+1... Ik2m−1−k2m−2−11 T k2m−k2m−1+1IJ−k2m   .
Let γ u = GT β, where β is the sub-vector of γ uconstructed by the unique elements. Since γ d = c1, and GT 1 = 1, then GBTy = (µ + 1)GBT BGT β − (µ − 1)GBT BGTγ dc1 ,

then
$$\beta=\frac{1}{\mu+1}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}y+\frac{\mu-1}{\mu+1}c\mathbf{1}\,.$$  $$\gamma^{u}=\mathbf{G}^{T}\beta=\frac{1}{\mu+1}\mathbf{G}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}y+\frac{\mu-1}{\mu+1}c\mathbf{1}\,,\qquad\gamma^{d}=c\mathbf{1}\,.$$
thus

## D.4 Corollary 1

The monotone decomposition for decreasing functions can be straightforward to derive, as summarized in Corollary 1.

Corollary 1. Let γˆ = (ˆγ u, γˆ
d) *be the monotone decomposition to problem (6).Suppose* γˆ
u+ˆγ dis decreasing, then
(i) γˆ
uis a vector with identical elements;
(ii) if γˆ
d 1 > *· · ·* > γˆ
d k1
= *· · ·* = ˆγ d k2
> *· · ·* > γˆ
d k2m−1
= *· · ·* = ˆγ d k2m
> · · · > γˆJ *, where* 1 ≤ k1 ≤ k2 ≤
· · · ≤ k2m−1 ≤ k2m ≤ J*, then*

$$\begin{array}{c c c}{{\hat{\gamma}^{d}=\frac{1}{\mu+1}\mathbf{G}^{T}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}y+\frac{\mu-1}{\mu+1}\mathbf{c}\mathbf{1}\,,\qquad\hat{\gamma}^{u}=\frac{\mathbf{1}^{T}\mathbf{B}\hat{\gamma}^{d}}{n}\mathbf{1}\,.}}\end{array}$$

Proof. With (*X, y*), the solution is γˆ
u + ˆγ d, then the solution for (X, −y) is −γˆ
u − γˆ
d.

If γ u + γ dis decreasing, then −γ u − γ dis increasing. Note that −γ uis non-increasing, and −γ d is non-decreasing, then by Proposition 1, firstly, −γ uis a constant, and hence γ uis a constant.

If γˆ
d 1 > *· · ·* > γˆ
d k1
= *· · ·* = ˆγ d k2
> *· · ·* > γˆ
d k2m−1
= *· · ·* = ˆγ d k2m
> γˆJ , then
−γˆ
d 1 < *· · ·* < −γˆ
d k1 = *· · ·* = −γˆ
d k2 < *· · ·* < −γˆ
d k2m−1 = *· · ·* = −γˆ

$$\cdots=-\hat{\gamma}_{k_{2m}}^{d}<-\hat{\gamma}_{J}\,.$$

Thus,

$$-\hat{\gamma}^d=\frac{1}{\omega+1}\mathbf{G}(\mathbf{G}\mathbf{B}^T)$$
µ + 1
G(GBT BGT)
$${\bf\hat{T}}(-y)+\frac{\mu-1}{\mu+1}\tilde{c}{\bf1}\,,\qquad\tilde{c}=\frac{{\bf1}^{T}{\bf B}(-\gamma^{d})}{n}\,,$$

it follows that

$$\hat{\gamma}^{d}=\frac{1}{\mu+1}$$
$$\frac{1}{\mu+1}{\bf G}({\bf G B}^{T}{\bf B G}^{T})^{-1}{\bf G B}^{T}y+\frac{\mu-1}{\mu+1}c{\bf1}\,,\qquad c=\frac{{\bf1}^{T}{\bf B}y^{d}}{n}\,,\qquad\hat{\gamma}^{u}=c{\bf1}\,.$$

## E A Side Product: Unimodal Functions

We explore the solution for more general unimodal functions, as summarized in Proposition 8.

Specifically, the second point of Proposition 3 can be viewed as a special instance with k = ℓ = 1 of Proposition 8.

Proposition 8. Let γˆ = (ˆγ u, γˆ
d) *be the monotone decomposition to problem (8). If*

$$\hat{\gamma}_{1}^{u}=\hat{\gamma}_{2}^{u}=\cdots=\hat{\gamma}_{k}^{u}<\hat{\gamma}_{k+1}^{u}<\cdots<\hat{\gamma}_{J}^{u}$$ $$\hat{\gamma}_{1}^{d}>\hat{\gamma}_{2}^{d}>\cdots>\hat{\gamma}_{\ell}^{d}=\hat{\gamma}_{\ell+1}^{d}=\cdots=\hat{\gamma}_{J}^{d}\,,$$
$$s u p p o s e\;\ell\leq k,\;t h e n$$
_suppose $\ell\leq k$, then_  $$\begin{bmatrix}\mathbf{I}_{\ell-1}&\\ &\mathbf{1}_{k-\ell+1}&\\ &&\mathbf{I}_{J-k}\end{bmatrix}\mathbf{B}^{T}\mathbf{y}=\mathbf{A}\mathbf{B}^{T}\mathbf{B}\hat{\gamma}^{u}+(2\mathbf{I}-\mathbf{A})\mathbf{B}^{T}\mathbf{B}\hat{\gamma}^{d}\,,$$  _where_  $$\begin{bmatrix}(1-\mu)\mathbf{I}_{\ell-1}&\\ \end{bmatrix}$$
$$\mathbf{A}=\begin{bmatrix}(1-\mu)\mathbf{I}_{\ell-1}\\ 2\mu\mathbf{1}_{\ell-1}^{T}&1+\mu\\ &(1+\mu)\mathbf{I}_{J-k}\end{bmatrix}.$$
$$P r o o f.{\mathrm{~If~}}$$

and
$$\gamma_{1}^{u}=\gamma_{2}^{u}=\cdots=\gamma_{k}^{u}<\gamma_{k+1}^{u}<\cdots<\gamma_{J}^{u}$$  $$\gamma_{1}^{d}>\gamma_{2}^{d}>\cdots>\gamma_{\ell}^{d}=\gamma_{\ell+1}^{d}=\cdots=\gamma_{J}^{d}\,.$$
and
Then from (28), we have ξi = 0, k + 1 ≤ i ≤ J, and then
$$\nu_{k}=\nu_{k+1}=\dots=\nu_{J-1}=0\,,$$  $$\nu_{J-1+i}=0,i=1,\dots,\ell-1\,.$$
Suppose $\ell\leq k$, then ... 
Then from (28), we have $\xi_{i}=0,k+1\leq i\leq3$, and then $$\sum_{i=1}^{k}\mathbf{B}_{i}^{T}y=(\mu+1)\sum_{i=1}^{k}\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{\mu}-(\mu-1)\sum_{i=1}^{k}\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{d}\,,$$ $$\mathbf{B}_{i}^{T}y=(\mu+1)\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{\mu}-(\mu-1)\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{d}\quad k+1\leq i\leq J\,.$$  Similarly, $\xi_{i+J}=0,1\leq i\leq\ell-1$, and hence 
(29)  $\binom{30}{2}$  . 
Similarly, $\xi_{i+J}=0,1\leq i\leq\ell-1$, and hence 
$0,1\leq i\leq\ell-1$, and hence  $$\mathbf{B}_{i}^{T}y=(\mu+1)\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{d}-(\mu-1)\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{u}\quad1\leq i\leq\ell-1$$ $$\sum_{i=\ell}^{J}\mathbf{B}_{i}^{T}y=(\mu+1)\sum_{i=\ell}^{J}\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{d}-(\mu-1)\sum_{i=\ell}^{J}\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{u}\;.$$
(31)  $\binom{32}{32}$  . 

Note that

$$\sum_{i=1}^{J}{\bf B}_{i}^{T}y=(\mu+1)\sum_{i=1}^{J}{\bf B}_{i}^{T}{\bf B}\gamma^{u}-(\mu-1)\sum_{i=1}^{J}{\bf B}_{i}^{T}{\bf B}\gamma^{d}$$ $$=(\mu+1)\sum_{i=1}^{J}{\bf B}_{i}^{T}{\bf B}\gamma^{d}-(\mu+1)\sum_{i=1}^{J}{\bf B}_{i}^{T}{\bf B}\gamma^{u}\,,\tag{3}$$
$$(33)$$

48 then (29) + (32) - (33) yields

X
k
ℓ
B
T
iy =
X
k
i=1
B
T
iy +
X
J
i=ℓ
B
T
iy −
X
J
i=1
B
T
iy
= (µ + 1)X
k
i=1
B
T
i Bγ
u − (µ − 1)X
k
i=1
B
T
i Bγ
d+
(µ + 1)X
J
i=ℓ
B
T
i Bγ
d − (µ − 1)X
J
i=ℓ
B
T
i Bγ
u−
[(1 − µ)1
T Bγ
u + (µ + 1)1
T Bγ
d]
= (µ + 1)X
k
i=1
B
T
i Bγ
u − (µ − 1)X
k
i=1
B
T
i Bγ
d+
(µ − 1)X
ℓ−1
i=1
B
T
i Bγ
u − (µ + 1)X
ℓ−1
i=1
B
T
i Bγ
d
= 2µ
X
ℓ−1
i=1
B
T
i Bγ
u + (µ + 1)X
k
i=ℓ
B
T
i Bγ
u − 2µ
X
ℓ−1
i=1
B
T
i Bγ
d − (µ − 1)X
k
i=ℓ
B
T
i Bγ
d,
then
BT
1
y
...
BT
ℓ−1
y
Pk
i=ℓ BT
i
y
BT
k+1y
...
BT
J
y

=

1 − µ *· · ·* 0 0 0 *· · ·* 0
...... 0 0 0 *· · ·* 0
0 *· · ·* 1 − µ 0 0 *· · ·* 0
2µ *· · ·* 2µ 1 + µ 0 *· · ·* 0
0 *· · ·* 0 0 1 + µ *· · ·* 0
.....................
0 *· · ·* 0 0 0 *· · ·* 1 + µ

B
T Bγ
u+

1 + µ *· · ·* 0 0 0 *· · ·* 0
...... 0 0 0 *· · ·* 0
0 *· · ·* 1 + µ 0 0 *· · ·* 0
−2µ · · · −2µ 1 − µ 0 *· · ·* 0
0 *· · ·* 0 0 1 − µ *· · ·* 0
.....................
0 *· · ·* 0 0 0 *· · ·* 1 − µ

B
T Bγ
d
≜ ABT Bγ
u + (2I − A)B
T Bγ
d.
If ℓ = k, then
$$\mathbf{B}^{T}y=\mathbf{A}\mathbf{B}^{T}\mathbf{B}\gamma^{u}+(2\mathbf{I}-\mathbf{A})\mathbf{B}^{T}\mathbf{B}\gamma^{d}\,.$$

## F Proof Of Proposition 4

Proof. The fitting vector is ˆf = Bγˆ
u + Bγˆ
d

$$\begin{array}{l l}{{{\bf1}={\bf B}^{T}\mathbf{\nabla}+{\bf B}^{T}\mathbf{\nabla}}}\\ {{}}&{{=\frac{1}{\mu+1}{\bf B G}^{T}({\bf G B}^{T}{\bf B G}^{T})^{-1}{\bf G B}^{T}{\bf y}+\frac{2\mu}{\mu+1}\frac{{\bf1}_{n}^{T}{\bf\hat{f}}}{2n}{\bf1}_{n}}}\\ {{}}&{{\triangleq k{\bf A}{\bf y}+\frac{1}{n}(1-k){\bf1}_{n}^{T}{\bf\hat{f}}{\bf1}_{n}\,,}}\end{array}$$
$$(34)$$

then
$$\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}=k\mathbf{1}_{n}^{T}\mathbf{A}\mathbf{y}+(1-k)\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}\,.$$
ˆf . (35)
It follows that
$$\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}=\mathbf{1}_{n}^{T}\mathbf{A}\mathbf{y}\,,$$
then
$${\hat{\mathbf{f}}}=k\mathbf{A}\mathbf{y}+{\frac{1-k}{n}}\mathbf{1}_{n}^{T}\mathbf{A}\mathbf{y}\mathbf{1}_{n}=\left[k\mathbf{I}+{\frac{1-k}{n}}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\right]\mathbf{A}\mathbf{y}\ .$$
Note that G depends on y, and hence A also depends on y. Take expectation on (36) and by the law of total expectation, we have

$$\mathbb{E}{\hat{\mathbf{f}}}=\mathbb{E}[\mathbb{E}[{\hat{\mathbf{f}}}\mid\mathbf{G}]]=\mathbb{E}[k\mathbf{A}\mathbf{f}+{\frac{1-k}{n}}\mathbf{1}_{n}^{T}\mathbf{A}\mathbf{f}\mathbf{1}_{n}]\,.$$
Note that $\mathbf{A}\mathbf{A}^T=\mathbf{A}=\mathbf{A}^T$ and $\mathbf{1}_n=\mathbf{B}\mathbf{1}_J=\mathbf{G}^T\mathbf{1}_g=\mathbf{B}\mathbf{G}^T\mathbf{1}_g$, then . 
$$\begin{array}{r l}{{\mathbf{1}_{n}^{T}\mathbf{A}=\mathbf{1}_{n}^{T}\mathbf{B}\mathbf{G}^{T}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}}}\\ {{}}&{{}=\mathbf{1}_{g}^{T}\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}}}\\ {{}}&{{}=\mathbf{1}_{g}^{T}\mathbf{G}\mathbf{B}^{T}}\\ {{}}&{{}=\mathbf{1}_{n}^{T}\,,}\end{array}$$
$$(36)$$

and hence 1 TnAAT 1n = n. It follows that

$$\mathbb{E}\mathbf{\hat{f}}=k\mathbb{E}\mathbf{A}\mathbf{f}+{\frac{1-k}{n}}\mathbf{1}_{n}^{T}\mathbf{f}\mathbf{1}_{n}\,.$$

The square of bias is

$$\|\mathbf{f}-\mathbb{E}\mathbf{\hat{f}}\|^{2}=\|\mathbf{f}-k\mathbb{E}\mathbf{A}\mathbf{f}-{\frac{1-k}{n}}\mathbf{1}_{n}^{T}\mathbf{f}\mathbf{1}_{n}\|^{2}$$
n = f T(I − kEA) 2f − 2(1 − k) n f T(I − kEA)1 T n f1n + (1 − k) 2 n2(1 T n f) 21 T n 1n = f T(I − kEA) 2f − 2(1 − k) n(1 T n f)f T(I − kEA)1n + (1 − k) 2 n(1 T n f) 2 = f T(I − kEA) 2f − (1 − k) 2 n(1 T n f) 2 = f Tf − 2kf TEAf + k 2f T[EA] 2f − (1 − k) 2 n(1 T n f) 2.
Note that
$$[\mathbb{E}\mathbf{A}]^{2}=\mathbb{E}\mathbf{A}^{2}-\mathrm{Var}(\mathbf{A})\,,$$

and A2 = A, we can write k 2f T[EA]
2f = k 2f T[EA − Var(A)]f .

It follows that

∥f − Eˆf∥ 2 = f TEAf − 2kf TEAf + k 2f TEAf + f Tf − f TEAf − k 2f T Var(A)f − (1 − k) 2 n(1 T n f) 2 = (1 − k) 2f TEAf + f T(I − EA)f − k 2f T Var(A)f − (1 − k) 2 n(1 T n f) 2 = (1 − k) 2 f TEAf − (1 Tn f) 2 n + f T(I − EA)f − k 2f T Var(A)f ≜ (1 − k) 2C1 + C2 − k 2C3 .
Since for each A, we have (I − A)
2 = (I − A) and (A − 11T /n)
2 = A − 11T /n, then both I − A
and A − 11T are idempotent, and hence are positive semi-definite. It follows that both I − EA
and EA − 11T /n are also positive semi-definite. Hence C1 ≥ 0 and C2 ≥ 0.

On the other hand, by the law of total variance, we have

$$\operatorname{Var}({\hat{\mathbf{f}}})=\mathbb{E}[\operatorname{Var}({\hat{\mathbf{f}}}\mid\mathbf{G})]+\operatorname{Var}[\mathbb{E}[{\hat{\mathbf{f}}}\mid\mathbf{G}]]\,.$$
ˆf | G]] . (37)
For the first term of (37), we have

$$\begin{split}\text{Var}(\mathbf{\hat{f}}\mid\mathbf{G})&=\sigma^{2}\left[k\mathbf{I}+\frac{1-k}{n}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\right]\mathbf{A}\mathbf{A}^{T}\left[k\mathbf{I}+\frac{1-k}{n}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\right]\\ &=\sigma^{2}\left[k^{2}\mathbf{A}\mathbf{A}^{T}+\frac{1-k}{n}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{A}\mathbf{A}^{T}+\frac{1-k}{n}\mathbf{A}\mathbf{A}^{T}\mathbf{1}_{n}\mathbf{1}_{n}^{T}+\frac{(1-k)^{2}}{n^{2}}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{1}_{n}^{T}\right]\,.\end{split}$$

Since

$$\operatorname{tr}(\mathbf{A}\mathbf{A}^{T})=\operatorname{tr}(\mathbf{A})$$
$$\begin{array}{r l}{{\mathrm{r}(\mathbf{A}\mathbf{B}^{T})=\mathrm{tr}(\mathbf{A})}}\\ {{}}&{{}=\mathrm{tr}(\mathbf{B}\mathbf{G}^{T}(\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T})}\\ {{}}&{{}=\mathrm{tr}((\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})^{-1}\mathbf{G}\mathbf{B}^{T}\mathbf{B}\mathbf{G}^{T})}\\ {{}}&{{}=g\,,}\end{array}$$
then
$$\operatorname{tr}[\operatorname{Var}({\hat{\mathbf{f}}}\mid\mathbf{G})]=\sigma^{2}\left[k^{2}g+2(1-k)+(1-k)^{2}\right]\,.$$

For the second term of (37), we have

$$\operatorname{Var}[\mathbb{E}[{\hat{\mathbf{f}}}\mid\mathbf{G}]]=\operatorname{Var}[k\mathbf{A}\mathbf{f}+{\frac{1-k}{n}}\mathbf{1}_{n}^{T}\mathbf{f}\mathbf{1}_{n}]=k^{2}\operatorname{Var}[\mathbf{A}]\mathbf{f}\mathbf{f}^{T}\,.$$

Thus,

$$\begin{array}{l}{{\mathrm{tr}[\mathrm{Var}(\hat{\mathbf{f}})]=\mathrm{tr}[\mathbb{E}[\mathrm{Var}(\hat{\mathbf{f}}\mid\mathbf{G})]]+\mathrm{tr}[\mathrm{Var}[\mathbb{E}[\hat{\mathbf{f}}\mid\mathbf{G}]]]}}\\ {{=\mathbb{E}[\mathrm{tr}[\mathrm{Var}(\hat{\mathbf{f}}\mid\mathbf{G})]]+\mathrm{tr}[k^{2}\,\mathrm{Var}[\mathbf{A}]\mathbf{f}^{T}]}}\\ {{=\sigma^{2}[k^{2}\mathbb{E}g+2(1-k)+(1-k)^{2}]+k^{2}\mathbf{f}^{T}\,\mathrm{Var}(\mathbf{A})\mathbf{f}}}\\ {{\triangleq\sigma^{2}[k^{2}\mathbb{E}g+2(1-k)+(1-k)^{2}]+k^{2}C_{3}\,.}}\end{array}$$

It follows that the mean square error is MSE = ∥ Bias ∥
2 + tr[Var(ˆf)]
= (1 − k)
2C1 + C2 + σ 2-k 2Eg + 2(1 − k) + (1 − k)
2.

The unconstrained B-spline fitting has MSEls = Jσ2.

To have MSE < MSEls,

$$(1-k)^{2}C_{1}+C_{2}+\sigma^{2}\left[k^{2}\mathbb{E}g+2(1-k)+(1-k)^{2}\right]<J\sigma^{2}\,,$$
that is
$h(k)\triangleq\left[C_{1}+(\mathbb{E}g+1)\sigma^{2}\right]k^{2}-\left[2C_{1}+4\sigma^{2}\right]k+C_{1}+C_{2}+3\sigma^{2}-J\sigma^{2}<0\,.$
Note that the minimum is obtained at

$$k_{\mathrm{min}}={\frac{\left[2C_{1}+4\sigma^{2}\right]}{2\left[C_{1}+(\mathbb{E}g+1)\sigma^{2}\right]}}={\frac{C_{1}+2\sigma^{2}}{C_{1}+(\mathbb{E}g+1)\sigma^{2}}}\in(0,1)\,,$$

since g ≥ 1, and the minimum value is

hmin = C1 + C2 + 3σ 2 − Jσ2 − -2C1 + 4σ 22 4 [C1 + (Eg + 1)σ 2] = σ 4[(3 − J)(Eg + 1) − 4] + σ 2[−C1(J − Eg) + C2(Eg + 1)] + C1C2 C1 + (Eg + 1)σ 2 = −σ 4-(J − Eg)(Eg + 1) + (Eg − 1)2+ σ 2[−C1(J − Eg) + C2(Eg + 1)] + C1C2 C1 + (Eg + 1)σ 2 =u(σ 2) C1 + (Eg + 1)σ 2 ,
$\left[\frac{1}{2}\right]+\left[-\frac{1}{2}\right]+\left[-\frac{1}{2}\right]+\left[-\frac{1}{2}\right]+\left[-\frac{1}{2}\right]+\left[-\frac{1}{2}\right]+\left[-\frac{1}{2}\right]$
where u(t) = −t 2-(J − Eg)(Eg + 1) + (Eg − 1)2+ t[−C1(J − Eg) + C2(Eg + 1)] + C1C2 .

Since C1, C2 ≥ 0,

$$\Delta=\left[-C_{1}(J-\mathbb{E}g)+C_{2}(\mathbb{E}g+1)\right]^{2}+4C_{1}C_{2}\left[(J-\mathbb{E}g)(\mathbb{E}g+1)+(\mathbb{E}g-1)^{2}\right]\geq0\,,$$ $$=\left[C_{1}(J-\mathbb{E}g)+C_{2}(\mathbb{E}g+1)\right]^{2}+4C_{1}C_{2}(\mathbb{E}g-1)^{2}\geq0\,,$$

then u(t) < 0 if

$$t>\frac{C_{1}(J-\mathbb{E}g)-C_{2}(\mathbb{E}g+1)-\sqrt{\Delta}}{-2[(J-\mathbb{E}g)(\mathbb{E}g+1)+(\mathbb{E}g-1)^{2}]}=\frac{-C_{1}(J-\mathbb{E}g)+C_{2}(\mathbb{E}g+1)+\sqrt{\Delta}}{2[(J-\mathbb{E}g)(\mathbb{E}g+1)+(\mathbb{E}g-1)^{2}]}\,.$$

F.1 G = I
If G = I, that is, no ties in the solution, Af = ABγ = B(B
T B)
−1B
T Bγ = Bγ = f .

$$\|\mathbf{f}-\mathbb{E}\mathbf{\hat{f}}\|^{2}=\|\mathbf{f}-k\mathbf{f}-{\frac{1-k}{n}}\mathbf{1}^{T}\mathbf{f}\mathbf{1}\|^{2}$$ $$=(1-k)^{2}\|\mathbf{f}-{\frac{1}{n}}\mathbf{1}^{T}\mathbf{f}\mathbf{1}\|^{2}$$ $$=(1-k)^{2}\left[\|\mathbf{f}\|^{2}-{\frac{1}{n}}(\mathbf{1}_{n}^{T}\mathbf{f})^{2}\right]$$
$$\mathbb{D}$$
$$\mathrm{If}\ \mathbf{G}=\mathbf{I},J=g,C_{2}=0,\mathrm{then}$$
$$h_{\mathrm{min}}=\frac{-\sigma^{4}(g-1)^{2}}{C_{1}+(g+1)\sigma^{2}}<0\,.$$
$$\begin{array}{l}{\square}\end{array}$$

## G Proof Of Proposition 5 G.1 (I)

Proof. Since if γ u + γ d = ˜γ u + ˜γ d, then the roughness penalty does not change,

$$\square$$

(γ u + γ d)
T Ω(γ u + γ d) = (˜γ u + ˜γ d)
T Ω(˜γ u + ˜γ d).

Then we can repeat the procedure in Section D.1.

G.2 (ii)
Proof. A special case when G = I in the following result.

## G.3 (Iii)

Proof. Take the derivatives on the Lagrange form,

$$-2\mathbf{Z}^{T}(\mathbf{y}-\mathbf{Z}\gamma)+2\mathbf{H}^{T}\nu+2\mu\mathbf{W}\gamma+2\lambda\begin{bmatrix}\mathbf{\Omega}&\mathbf{\Omega}\\ \mathbf{\Omega}&\mathbf{\Omega}\end{bmatrix}\gamma=0$$

Then

$$\begin{array}{c}{{-{\bf B}_{i}^{T}({\bf y}-{\bf Z}\gamma)+{\bf H}_{i}^{T}\nu+\mu{\bf B}_{i}^{T}{\bf B}(\gamma^{u}-\gamma^{d})+\lambda{\bf\Omega}_{i}(\gamma^{u}+\gamma^{d})=0}}\\ {{-{\bf B}_{i}^{T}({\bf y}-{\bf Z}\gamma)+{\bf H}_{i+J}^{T}\nu+\mu{\bf B}_{i}^{T}{\bf B}(-\gamma^{u}+\gamma^{d})+\lambda{\bf\Omega}_{i}(\gamma^{u}+\gamma^{d})=0}}\end{array}$$
d) = 0 (38)
d) = 0 (39)
Rewrite them as

$$\begin{array}{c}{{{\bf B}_{i}^{T}{\bf y}+\xi_{i}=((1+\mu){\bf B}_{i}^{T}{\bf B}+\lambda{\bf\Omega}_{i})\gamma^{u}+((1-\mu){\bf B}_{i}^{T}{\bf B}+\lambda{\bf\Omega}_{i})\gamma^{d}}}\\ {{{\bf B}_{i}^{T}{\bf y}+\xi_{i+J}=((1-\mu){\bf B}_{i}^{T}{\bf B}+\lambda{\bf\Omega}_{i})\gamma^{u}+((1+\mu){\bf B}_{i}^{T}{\bf B}+\lambda{\bf\Omega}_{i})\gamma^{d}\,.}}\end{array}$$
d(40)

$$(38)$$
$$\begin{array}{l}{(40)}\\ {(41)}\end{array}$$

If there are no ties in the solution, i.e.,
γ u 1 < γu 2 < · · · < γu J, γd 1 > γd 2 > · · · > γd J,
by the KKT condition, ν = 0, and hence ξi = ξi+J = 0, then (40) - (41) yields 0 = 2µB
T
i Bγ u − 2µB

$$\mu\mathbf{B}_{i}^{T}\mathbf{B}\gamma^{d}\,,$$

that is 0 = 2µB
T B(γ u − γ d),
which implies µ = 0 since γ u > γd. Then it reduces to unconstrained B-spline fitting. This argument proves the first point of Proposition 2.

If γˆ
u 1 < *· · ·* < γˆ
u k1
= *· · ·* = ˆγ u k2
< *· · ·* < γˆ
u k2m−1
= *· · ·* = ˆγ u k2m
< γˆJ , then similar to Section D, we have GBTy = ((1 + µ)GBT B + λGΩ)γ u + ((1 − µ)GBT B + λGΩ)γ d.

Let γ u = GT β, where β is the sub-vector of γ uconstructed by the unique elements. By G.1, γ d = c1J , and note that GT 1g = 1J , then GBTy = ((1 + µ)GBT BGT + λGΩGT)β + c((1 − µ)GBT BGT + λGΩGT)1g ,
it follows that

$$\begin{array}{l}{{(1+\mu){\bf G B}^{T}{\bf B G}^{T}+\lambda{\bf G}\Omega{\bf G}^{T})^{-1}{\bf G B}^{T}y-}}\\ {{c((1+\mu){\bf G B}^{T}{\bf B G}^{T}+\lambda{\bf G}\Omega{\bf G}^{T})^{-1}((1-\mu){\bf G B}^{T}{\bf B G}^{T}+\lambda{\bf G}\Omega{\bf G}^{T}){\bf1}_{g}\,,}}\end{array}$$

and

$$c={\frac{\mathbf{1}_{n}^{T}\mathbf{B}\gamma^{u}}{n}}={\frac{\mathbf{1}_{n}^{T}\mathbf{B}\mathbf{G}^{T}\beta}{n}}\,.$$

$\boxed{\text{I}}$

## G.4 Corollary 2

Analogously, we can obtain the monotone decomposition with smoothing splines on decreasing functions, as summarized in Corollary 2.

Corollary 2. Let γˆ = (ˆγ u, γˆ
d) *be the monotone decomposition to problem (11). Suppose* γˆ
u + ˆγ dis decreasing, then
(i) γˆ
u*is a vector with identical elements;*
(ii) if γˆ
d 1 > *· · ·* > γˆ
d k1
= *· · ·* = ˆγ d k2
> *· · ·* > γˆ
d k2m−1
= *· · ·* = ˆγ d k2m
> γˆJ , where 1 ≤ k1 ≤ k2 *≤ · · · ≤*
k2m−1 ≤ k2m ≤ J*, then* γˆ
d = GT((1 + µ)GBT BGT + λGΩGT)
−1GBTy−
cGT((1 + µ)GBT BGT + λGΩGT)
−1((1 − µ)GBT BGT + λGΩGT)1g ,

$$c{\bf G}^{\prime}((1+\mu){\bf G B}^{\prime}{\bf B G}^{\prime}+\lambda{\bf G H G}^{\prime})^{\prime}((1-\mu){\bf G B}^{\prime}{\bf B G}^{\prime}+\lambda{\bf G H G}^{\prime}){\bf I}_{g}\,,$$ $$\hat{\gamma}^{u}=c{\bf1}_{J}=\frac{{\bf1}^{T}{\bf B}\hat{\gamma}^{d}}{n}{\bf1}_{J}\,,$$

Proof. Similar to the proof D.4 for Corollary 1.

## H Proof Of Proposition 6 H.1 Lemmas

Lemma 2 (Magnus and Neudecker, 2019). Let A, B *be two real matrices of the same size, then*
[tr(AB)]2 ≤ [tr(A2)][tr(B
2)] .

Lemma 3. Let A *be a real positive semi-definite matrix, then*

$$\begin{array}{l}{\square}\end{array}$$

tr(A2) ≤ [tr(A)]2.

Proof. Let λi be the eigenvalues of A, then λ 2 iare the eigenvalues of A2. Note that

$$\operatorname{tr}[\mathbf{A}^{2}]=\sum\lambda_{i}^{2}\leq(\sum\lambda_{i})^{2}=[\operatorname{tr}(\mathbf{A})]^{2}\,.$$

Lemma 4. The eigenvalues of 1n1 Tnis

$$\begin{array}{l}{\square}\end{array}$$

λ1 = n, λ2 = *· · ·* = λn = 0 .

Proof. Since 1n1 Tnis a rank-1 matrix, which implies that it has n − 1 eigenvalues which are zero.

Denote the eigenvectors as ξi, i = 1*, . . . , n*. Suppose the nonzero eigenvalues is λ1 with associated eigenvectors ξ1, then 1n1 T
nξ1 = λ1ξ1 ,
left multiplying 1 Tn yields

$$n{\bf1}_{n}^{T}\xi_{1}=\lambda_{1}{\bf1}^{T}\xi_{1}\,,$$

which implies that λ1 = n.

H.2 G = I
Proof. If G = I, the solution is

poly. If $\mathbf{G}=\mathbf{I}$, the solution is  $$\hat{\gamma}^{u}=\frac{1}{1+\mu}\left[\mathbf{B}^{T}\mathbf{B}+\frac{\lambda}{1+\mu}\mathbf{I}\right]^{-1}\mathbf{B}^{T}\mathbf{y}-c((1+\mu)\mathbf{B}^{T}\mathbf{B}+\lambda\mathbf{\Omega})^{-1}((1-\mu)\mathbf{G}\mathbf{B}^{T}\mathbf{B}+\lambda\mathbf{\Omega})\mathbf{1}_{J}\,,$$ $$\triangleq\frac{1}{1+\mu}\left[\mathbf{B}^{T}\mathbf{B}+\lambda_{0}\mathbf{\Omega}\right]^{-1}\mathbf{B}^{T}\mathbf{y}-c\mathbf{K}\mathbf{1}_{J}\,,$$ $$\hat{\gamma}^{d}=c\mathbf{1}_{J}=\frac{\mathbf{1}_{J}^{T}\mathbf{\hat{I}}}{2\mu}\mathbf{1}_{J}\,,$$  in fact, we can write 

then the fitting vector is ˆf = Bγˆ
u + Bγˆ
d

=1 1 + µ ˆf ss + cB(−K + I)1J =1 1 + µ ˆf ss + 1 Tn ˆf 2n B-(1 + µ)B T B + λΩ−12µB T B1J =1 1 + µ ˆf ss +µ 1 + µ 1 Tn ˆf n B B T B +λ 1 + µ Ω −1B T 1n ≜ k ˆf ss + (1 − k) 1 Tn ˆf n Q1n ,
where Q = B-BT B + λ0Ω−1 BT. In practice, λ0 is given as a constant, so Q does not depend on k. Left multiplying 1 Tn yields

$$\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}=k\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}^{\mathrm{ss}}+(1-k)\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}{\frac{\mathbf{1}_{n}^{T}\mathbf{Q}\mathbf{1}_{n}}{n}}\,,$$

that is,

$$\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}={\frac{k\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}^{\mathrm{ss}}}{1-{\frac{\mathbf{1}_{n}^{T}\mathbf{Q}\mathbf{1}_{n}}{n}}(1-k)}}\triangleq{\frac{k\mathbf{1}_{n}^{T}{\hat{\mathbf{f}}}^{\mathrm{ss}}}{1-\eta(1-k)}}\,.$$

It follows that

$$\hat{\mathbf{f}}=\left[k\mathbf{I}+\frac{1-k}{n}\frac{k}{1-\eta(1-k)}\mathbf{Q1}_{n}\mathbf{1}_{n}^{T}\right]\hat{\mathbf{f}}^{\mathrm{ss}}\triangleq(k\mathbf{I}+\alpha\mathbf{Q1}_{n}\mathbf{1}_{n}^{T})\hat{\mathbf{f}}^{\mathrm{ss}}\,.$$  ed bias is  $$\|\mathbf{f}-\mathbb{E}\hat{\mathbf{f}}\|_{2}^{2}=\|\mathbf{f}-(k\mathbf{I}+\alpha\mathbf{Q1}_{n}\mathbf{1}_{n}^{T})\mathbb{E}\hat{\mathbf{f}}^{\mathrm{ss}}\|_{2}^{2}$$

Then the squared bias is

∥f − Eˆf∥ 2 2 = ∥f − (kI + αQ1n1 T n)Eˆf ss∥ 2 2 = ∥(kI + αQ1n1 T n)(f − Eˆf ss) + ((1 − k)I − αQ1n1 T n)f∥ 2 = (f − Eˆf ss) T(kI + α1n1 T nQ)(kI + αQ1n1 T n)(f − Eˆf ss)+ 2(f − Eˆf ss) T(kI + αQ1n1 T n) T((1 − k)I − αQ1n1 T n)f+ f T((1 − k)I − αQ1n1 T n) T((1 − k)I − αQ1n1 T n)f ≜ C1 + 2C2 + C3 .
First for term C1, we have

C1 = (f − Eˆf ss) T(kI + α1n1 T nQ)(kI + αQ1n1 T n)(f − Eˆf ss) = k 2∥f − Eˆf ss∥ 2 + 2kα(f − Eˆf ss) T 1n1 T nQ(f − Eˆf ss)+ α 2(f − Eˆf ss) T 1n1 T nQ21n1 T n(f − Eˆf ss).
Take the derivative with respect to k,

$$\frac{\partial C_{1}}{\partial k}=2k\|\mathbf{f}-\mathbb{E}\widehat{\mathbf{f}}^{\mathrm{ss}}\|^{2}+2\left(k\frac{\partial\alpha}{\partial k}+\alpha\right)(\mathbf{f}-\mathbb{E}\widehat{\mathbf{f}}^{\mathrm{ss}})^{T}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}(\mathbf{f}-\mathbb{E}\widehat{\mathbf{f}}^{\mathrm{ss}})$$ $$+2\alpha\frac{\partial\alpha}{\partial k}(\mathbf{f}-\mathbb{E}\widehat{\mathbf{f}}^{\mathrm{ss}})^{T}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}^{2}\mathbf{1}_{n}\mathbf{1}_{n}^{T}(\mathbf{f}-\mathbb{E}\widehat{\mathbf{f}}^{\mathrm{ss}})\,.$$  $\mathbf{1}_{n}$\(\mathbf
+ 2α ∂k (f − Eˆf Note that ∂α ∂k |k=1= − 1 n and α(1) = 0, then ∂C1 ∂k |k=1= 2∥f − Eˆf ss∥ 2 − 2 n (f − Eˆf ss) T 1n1 T nQ(f − Eˆf ss). Similarly, for term C2 and C3, we have C2 = (f − Eˆf ss) T(kI + αQ1n1 T n) T((1 − k)I − αQ1n1 T n)f
= f
T(I − Q)
T(kI + αQ1n1
$$\begin{split} \mathbf{Q1}_n\mathbf{1}_n^T)^T((1-k)\mathbf{I}-\alpha\mathbf{Q1}_n) \\ \mathbf{Q1}_n\mathbf{1}_n^T)^T((1-k)\mathbf{I}-\alpha\mathbf{Q1}_n) \\ +(1-k)\alpha\mathbf{f}^T(\mathbf{I}-\mathbf{Q})\mathbf{1}_n\mathbf{1}_n^T\\ \mathbf{1}_n\mathbf{1}^T\mathbf{Q}^2\mathbf{1}_n\mathbf{1}^T\mathbf{f} \end{split}$$
T
n)f
= k(1 − k)f
T(I − Q)f + (1 − k)αf
T
nQf − kαf
T(I − Q)Q1n1
T n
f+
α 2f T(I − Q)1n1 nQ21n1 n f ,
C3 = f T((1 − k)I − αQ1n1 T
n)
T((1 − k)I − αQ1n1 T
n)f
= (1 − k)
2f Tf − 2α(1 − k)f T 1n1 T
nQf + α 2f T 1n1 T
nQ21n1 T n f ,
and then take their derivatives with respect to k,

∂C2 ∂k = (1 − 2k)f T(I − Q)f + (1 − k) ∂α ∂k − α f T(I − Q)1n1 T nQf− ∂α ∂k + α f T(I − Q)Q1n1 T n f + 2α ∂α ∂k f T(I − Q)1n1 T nQ21n1 T n f , ∂C3 ∂k = −2(1 − k)f Tf − 2 (1 − k) ∂α ∂k − α f T 1n1 T nQf + 2α ∂α ∂k f T 1n1 T nQ21n1 T n f , it follows that
$$\begin{array}{l}{{{\frac{\partial C_{2}}{\partial k}}\mid_{k=1}=-\mathbf{f}^{T}(\mathbf{I}-\mathbf{Q})\mathbf{f}+{\frac{1}{n}}\mathbf{f}^{T}(\mathbf{I}-\mathbf{Q})\mathbf{Q}\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{f}\,,}}\\ {{{\frac{\partial C_{3}}{\partial k}}\mid_{k=1}=0\,.}}\end{array}$$
On the other hand, the variance is Var(ˆf) = (kI + αQ1n1 T
n) Var(ˆf ss)(kI + αQ1n1 T
n)
T
= k 2 Var(ˆf ss) + kαQ1n1 T
n Var(ˆf ss) + kα Var(ˆf ss)1n1 T
nQ + α 2Q1n1 T
n Var(ˆf ss)1n1 T
nQ ,
and tr[Var(ˆf)] = k 2tr[Var(ˆf ss)] + 2kα tr[Q1n1 T
n Var(ˆf ss)] + α 2tr[Q1n1 T
n Var(ˆf ss)1n1 T
nQ] ,
then its derivative with respect to k is

$${\frac{\partial\operatorname{tr}[\operatorname{Var}({\hat{\mathbf{f}}})]}{\partial k}}=2k\operatorname{tr}[\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})]+2\left(k{\frac{\partial\alpha}{\partial k}}+\alpha\right)\operatorname{tr}[\mathbf{Q1}_{n}\mathbf{1}_{n}^{T}\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})]+$$ $$2\alpha{\frac{\partial\alpha}{\partial k}}\mathbf{Q1}_{n}\mathbf{1}_{n}^{T}\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}\,.$$

Evaluate at k = 1,

$$\frac{\partial\operatorname{tr}[\operatorname{Var}({\hat{\mathbf{f}}})]}{\partial k}\mid_{k=1}=2\operatorname{tr}[\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})]-\frac{2}{n}\operatorname{tr}[\mathbf{Q1}_{n}\mathbf{1}_{n}^{T}\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})]\,.$$
Thus ∂ MSE(k) ∂k |k=1 = 2∥f − Eˆf ss∥ 2 − 2 n (f − Eˆf ss) T 1n1 T nQ(f − Eˆf ss)+ 2 −f T(I − Q)f + 1 n f T(I − Q)Q1n1 T n f + 2 tr[Var(ˆf ss)] − 2 n tr[Q1n1 T n Var(ˆf ss)] = 2f T Q 1n1 TnQ n(I − Q)f − 2f T Q(I − Q)f+ 2 tr[Var(ˆf ss)] − 2 n tr[Q1n1 T n Var(ˆf ss)] = 2 tr[Var(ˆf ss)] − 1 n tr[Q1n1 T n Var(ˆf ss)] − f T Q(I − 1n1 TnQ n)(I − Q)f (42) = 2 σ 2tr[(I − 1n1 TnQ n)Q2] − tr[(I − 1n1 TnQ n)(I − Q)ff T Q] . (43) 57
Next, we will prove the first term on the right-hand side of (43) is positive. By the Cauchy-Schwarz inequality for trace in Lemma 2,

$$\mathrm{tr}[\mathbf{Q1}_{n}\mathbf{1}_{n}^{T}\,\mathrm{Var}(\hat{\mathbf{f}}^{\mathrm{ss}})]\leq\sqrt{\mathrm{tr}[(\mathbf{Q1}_{n}\mathbf{1}_{n}^{T})^{2}]\,\mathrm{tr}[(\mathrm{Var}(\hat{\mathbf{f}}^{\mathrm{ss}}))^{2}]}$$ $$=\mathbf{1}_{n}^{T}\mathbf{Q1}_{n}\sqrt{\mathrm{tr}[(\mathrm{Var}(\hat{\mathbf{f}}^{\mathrm{ss}}))^{2}]}\,,$$

and since Var(ˆf ss) = σ 2Q2is a positive semi-definite matrix, then by Lemma 3,

$$\operatorname{tr}[(\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}}))^{2}]\leq[\operatorname{tr}(\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}}))]^{2}\,.$$

Note that

$$\eta=\frac{\mathbf{1}_{n}^{T}\mathbf{Q}\mathbf{1}_{n}}{n}=\frac{\mathbf{1}_{n}^{T}\mathbf{Q}\mathbf{1}_{n}}{\mathbf{1}_{n}^{T}\mathbf{1}_{n}}\leq\lambda_{\operatorname*{max}}(\mathbf{Q})=\lambda_{\operatorname*{max}}(\mathbf{B}(\mathbf{B}^{T}\mathbf{B}+\lambda_{0}\mathbf{\Omega})^{-1}\mathbf{B}^{T})\,.$$

Perform singular value decomposition (SVD) on B, B = UDVT, where U and V are n×J and J×J
orthogonal matrices, and D is a J ×J diagonal matrix, with diagonal entries d1 ≥ d2 *≥ · · ·* dp ≥ 0.

Then Q = UDVT(VD2VT + λ0Ω)
−1VDUT = U(I + λ0D−1VT ΩVD−1)
−1UT,
it follows that

$$\begin{array}{r l}{{\eta\leq\lambda_{\operatorname*{max}}(\mathbf{U}(\mathbf{I}+\lambda_{0}\mathbf{D}^{-1}\mathbf{V}^{T}\Omega\mathbf{V}\mathbf{D}^{-1})^{-1}\mathbf{U}^{T})}}\\ {{}}&{{=\lambda_{\operatorname*{max}}((\mathbf{I}+\lambda_{0}\mathbf{D}^{-1}\mathbf{V}^{T}\Omega\mathbf{V}\mathbf{D}^{-1})^{-1})}}\\ {{}}&{{={\frac{1}{\lambda_{\operatorname*{min}}(\mathbf{I}+\lambda_{0}\mathbf{D}^{-1}\mathbf{V}^{T}\Omega\mathbf{V}\mathbf{D}^{-1})}}}}\\ {{}}&{{={\frac{1}{1+\lambda_{\operatorname*{min}}(\lambda_{0}\mathbf{D}^{-1}\mathbf{V}^{T}\Omega\mathbf{V}\mathbf{D}^{-1})}}<1\,,}}\end{array}$$
thus1
$${\frac{1}{n}}\operatorname{tr}[\mathbf{Q1}_{n}\mathbf{1}_{n}^{T}\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})]<\operatorname{tr}[\operatorname{Var}({\hat{\mathbf{f}}}^{\mathrm{ss}})]\,.$$
Note that if $\frac{\partial\operatorname{MSE}(k)}{\partial k}>0$, that is,  . 
$$\sigma^{2}>\frac{\mathbf{f}^{T}\mathbf{Q}(\mathbf{I}-\frac{\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}}{n})(\mathbf{I}-\mathbf{Q})\mathbf{f}}{\mathrm{tr}[(\mathbf{I}-\frac{\mathbf{1}_{n}\mathbf{1}_{n}^{T}\mathbf{Q}}{n})\mathbf{Q}^{2}]}\,,$$

then there exists k ∈ (0, 1) such that MSE(k) < MSE(1).

If λ0 = 0, then (I − Q)f = 0, and

1n1 T nQ = 1n(B1J ) T B(B T B) −1B T = 1n1 T J B T = 1n1 T n, I − 1n1 TnQ n= I − 1n(B1J ) T B(BT B)−1BT n= I − 1n1 T J BT n= I − 1n1 Tn n, tr[(I − 1n1 TnQ n)Q2] = tr[(I − 1n1 Tn n)Q] = J − 1 n tr[1n1 T nQ] = J − 1 ,
then
and hence ∂ MSE(k)
∂k > 0 if σ 2 > 0, which always holds.