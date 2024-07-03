# Generalized measure Black-Scholes equation: Towards option self-similar pricing 

Nizar Riane ${ }^{\dagger \ddagger}$, Claire David ${ }^{\ddagger}$

April 9, 2024

† Université Mohammed V de Rabat, FSJESR-Agdal, Marod1

‡ Sorbonne Université<br>CNRS, UMR 7598, Laboratoire Jacques-Louis Lions, 4, place Jussieu 75005, Paris, France2 2


#### Abstract

In this work, we give a generalized formulation of the Black-Scholes model. The novelty resides in considering the Black-Scholes model to be valid on 'average', but such that the pointwise option price dynamics depends on a measure representing the investors' 'uncertainty'.

We make use of the theory of non-symmetric Dirichlet forms and the abstract theory of partial differential equations to establish well posedness of the problem. A detailed numerical analysis is given in the case of self-similar measures.


Keywords: Generalized measure Black-Scholes equation; self-similar measure; non-symmetric Dirichlet form; fractal differential equations; finite difference method.

AMS Classification: 28A80 - 91G20 - 65L12 - 65L20.

## 1 Introduction

The Black-Scholes model arises as one of the most important application of mathematics to economics and finance of the $20^{\text {th }}$ century, allowing the emergence of the theory of financial partial differential equations and the associated numerical analysis.

Yet, despite its phenomenal success in the financial market, the model suffers from deficiencies, for instance, when it comes to the modeling of real market options with erratic behaviors [For96. One can argue that the model does not capture all the factors influencing investor decisions.

From a practical point of view, investors employ technical analysis to detect patterns in price evolution graphs to beat the market; since those patterns seem to appear in small and large scales, this could justify a self-similar modelling of the market. Investigation of fractals in finance is not new, we can refer, for instance, to Benoit Mandelbrot's work in Man97, the aspects of which are not taken[^0]into account by the classical model.

In this paper, we give a definition of a general version of the Black-Scholes model, based on the theory of non-symmetric Dirichlet forms, and on the abstract theory of partial differential equations. The key point is to consider the Black-Scholes equation describing an average evolution, while the exact dynamics depends on uncertainty captured by a mathematical measure. The analysis goes so far as proving the existence of a Generalized Black-Scholes operator.

Special treatment is given to the self-similar case by writing an explicit formula, which enables computation of the solution. The CFL 3 convergence condition for the associated finite difference scheme is determined and written explicitly. For the proper calibration, our model can avoid overpricing options at the money, and underpricing options at the ends, either deep in the money, or deep out of the money 5 . This work opens the way to an empirical investigation and an inverse problem of the probability measure $\mu$.

## 2 Generalized Measure Black-Scholes Model

## Definition 2.1 (Generalized Measure Black-Scholes Equation).

Let's introduce the generalized measure Black-Scholes equation, for European options, in the sense of distributions:

$\left\{\begin{array}{cccc}\frac{\partial u}{\partial t}(t, x) d \mu & = & \left(-r(t) x \frac{\partial u}{\partial x}(t, x)-\frac{\sigma^{2}(t)}{2} x^{2} \Delta u(t, x)+r(t) u(t, x)\right) d x & \forall(t, x) \in[0, T] \times] L, M[ \\ u(T, x) & = & h(x) & \forall x \in[L, M]\end{array}\right.$

where the variable $0<L<x<M$ is the price of the underlying financial instrument, $\sigma$ denotes the volatility, $r$ the risk-free interest rate, $T$ the maturity of the option, $\mu$ a non atomic finite measure with total mass $\mathbb{M}=M-L$ and $u$ represents the option price. The real valued function $h$ takes the values $h(x)=(x-K)^{+}$for a call], and $h(x)=(K-x)^{+}$for a $p u t \sqrt{7}$, given a constant $K$ : "the strike".

In order to prove that the problem has a solution, technical results associated to the classical Black-Scholes model are required. We refer to AP05 for the proof of the following assertions.[^1]

### 2.1 The Black-Scholes Model

## Notation (Space of Test Functions).

Given a continuous subset $E$ of $\mathbb{R}$, we will denote by $\mathcal{D}(E)$ the space of test functions on $E$, i.e. the space of smooth functions with compact support in $E$.

## Notation (Black-Scholes Bilinear Form).

For any pair $(u, v) \in \mathcal{D}\left(\mathbb{R}_{+}\right) \times \mathcal{D}\left(\mathbb{R}_{+}\right)$, set:

$$
B(u, v)=\int_{\mathbb{R}_{+}} \frac{\sigma^{2} x^{2}}{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\int_{\mathbb{R}_{+}}\left(\sigma^{2}-r\right) x \frac{\partial u}{\partial x} v d x+\int_{\mathbb{R}_{+}} r u v d x
$$

and note $B(u, u)=B(u)$.

## Property 2.1.

The bilinear form $B(\cdot, \cdot)$ is non-symmetric.

Define its symmetric part, for any pair $(u, v) \in \mathcal{D}\left(\mathbb{R}_{+}\right) \times \mathcal{D}\left(\mathbb{R}_{+}\right)$, through:

$$
\begin{aligned}
\tilde{B}(u, v) & =\frac{1}{2}(B(u, v)+B(v, u)) \\
& =\int_{\mathbb{R}_{+}} \frac{\sigma^{2} x^{2}}{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\frac{1}{2} \int_{\mathbb{R}_{+}}\left(\sigma^{2}-r\right) x\left(\frac{\partial u}{\partial x} v+u \frac{\partial v}{\partial x}\right) d x+\int_{\mathbb{R}_{+}} r u v d x \\
& =\frac{\sigma^{2}}{2} \int_{\mathbb{R}_{+}} x^{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\frac{3 r-\sigma^{2}}{2} \int_{\mathbb{R}_{+}} u v d x
\end{aligned}
$$

## Notations.

Set

$$
V=\left\{v \in L^{2}\left(\mathbb{R}_{+}\right) \quad, \quad x \frac{\partial v}{\partial x} \in L^{2}\left(\mathbb{R}_{+}\right)\right\} \quad, \quad W=\left\{v \in L^{2}\left(\mathbb{R}_{+}\right) \quad, \quad x^{2} \frac{\partial^{2} v}{\partial x^{2}} \in L^{2}\left(\mathbb{R}_{+}\right)\right\}
$$

## Property 2.2.

The space

$$
V=\left\{v \in L^{2}\left(\mathbb{R}_{+}\right) \quad, \quad x \frac{\partial v}{\partial x} \in L^{2}\left(\mathbb{R}_{+}\right)\right\}
$$

endowed with the inner product

$$
(u, v) \mapsto\langle u, v\rangle_{V}=\langle u, v\rangle_{L^{2}\left(\mathbb{R}_{+}\right)}+\left\langle x \frac{d u}{d x}, x \frac{d v}{d x}\right\rangle_{L^{2}\left(\mathbb{R}_{+}\right)}
$$

is a Hilbert space.

## Definition 2.2 (Black-Scholes Weak Formula).

The Black-Scholes variational formula reads: find $u \in C\left([0, T] ; L^{2}\left(R_{+}\right)\right) \cap L^{2}((0, T) ; V)$ such that $\partial_{t} u \in L^{2}\left((0, T) ; V^{\star}\right)$, satisfying:

$$
\left\{\begin{array}{l}
B(u, v)=\frac{d}{d t} \int_{\mathbb{R}_{+}} u(t, x) v(x) d x \quad, \quad \forall v \in \mathcal{D}\left(\mathbb{R}_{+}\right) \\
u(T, x)=h(x)
\end{array}\right.
$$

where $V^{\star}$ is the dual space of $V$.

## Lemma 2.3 (Black-Scholes Operator).

There exists a unique bounded linear operator $\mathcal{B S}: V \rightarrow V^{\prime}$, which will be called Black-Scholes operator, such that:

$$
\forall(u, v) \in V^{2}: \quad B(u, v)=\langle\mathcal{B S}(u), v\rangle_{L^{2}\left(\mathbb{R}_{+}\right)}
$$

## Definition 2.3.

Recall that the first derivative is always bounded in the Hilbert-Sobolev space $H^{1}\left(\mathbb{R}_{+}\right)$, and that the second derivative is always bounded in the Hilbert-Sobolev space $H^{2}\left(\mathbb{R}_{+}\right)$.

The Black-Scholes operator is given, for any $v$ in $W$, by

$$
\mathcal{B S}(v)=-\frac{x^{2} \sigma^{2}}{2} \frac{\partial^{2} v}{\partial x^{2}}-r x \frac{\partial v}{\partial x}+r v
$$

## Lemma 2.4.

The set

$$
W=\left\{v \in V \quad, \quad x^{2} \frac{\partial^{2} v}{\partial x^{2}} \in L^{2}\left(\mathbb{R}_{+}\right)\right\}
$$

is dense in $V$.

## Lemma 2.5 (Black-Scholes Weak Solution).

For $h$ in $L^{2}\left(\mathbb{R}_{+}\right)$, the Black-Scholes problem has a unique weak solution.

### 2.2 An Interpretation of the Generalized Measure Black-Scholes Model

The generalized measure Black-Scholes equation, for a probability measure $\mu$, can be written, by choosing $v=u$, as

$$
\frac{\partial}{\partial t} \mathbb{E}\left(|u|^{2}\right)=\frac{2}{\mathbb{M}} B(u)
$$

where $\mathbb{M}=M-L$, while $\mathbb{E}($.$) is the expected value and B(\cdot, \cdot)$ denotes the involved Black-Scholes bilinear form. This equation can be understood in the following way: the expected value depreciation of $u^{2}$ (and, hence, of $u$, since it is positive) is proportional to the Black-Scholes energy $B(u)$. This implies a law given by the classical Black-Scholes theory which holds on average and another induced by investors' perception of reality and reflected by $\mu$.

A direct implication of this vision is a local dependence of the option price dynamics on the probability measure $\mu$, which can be interpreted as a $\backslash n$ confidence $\backslash$ uncertainty measure.

## 3 Non-Symmetric Dirichlet Forms and Generalized Measure BlackScholes Operators

Given two strictly positive numbers $L<M$, if one replaces $\mathbb{R}_{+}$with $\overline{\mathcal{M}}=[L, M]$ (where $\mathcal{M}=$ ]$L, M[$ ) in the generalized measure Black-Scholes model, it does not result in a dramatic effect on the mathematical or economical foundations of the model from the following two points of view:

1. Financial stability: One can suppose, in short run, boundedness of the underlying financial instrument price.
2. Numerical analysis: It is well known that infinite boundaries are replaced with finite ones for numerical simulations (See KN01 for error estimates).

In section 5.3 a tolerance level associated with the choice of the bounds $L$ and $M$ is calculated.

## Notations.

Let's introduce the following two spaces:

$$
\begin{aligned}
V_{\mathcal{M}} & =\left\{v \in L^{2}(\mathcal{M}) \quad, \quad x \frac{\partial v}{\partial x} \in L^{2}(\mathcal{M})\right\} \\
L_{\mu}^{2}(\mathcal{M}) & =\left\{v \quad, \quad \int_{L}^{M} v^{2} d \mu<\infty\right\}
\end{aligned}
$$

The dual space of $V_{\mathcal{M}}$ will be denoted by $V_{\mathcal{M}}^{\star}$ and the closure of $D(\mathcal{M})$ in $V_{\mathcal{M}}$ by $V_{0, \mathcal{M}}$.

## Proposition 3.1.

The space $\mathcal{D}(\mathcal{M})$ is dense in $L_{\mu}^{2}(\mathcal{M})$.

As in HLN06, the fundamental conditions under which the solution exist are obtained thanks to the following assumptions:

## Assumptions 3.2.

For any $u$ in $\mathcal{D}(\mathcal{M})$, there exists a positive constant $C_{0}$ :

$$
\begin{aligned}
\|u\|_{L_{\mu}^{2}(\mathcal{M})} & \leq C_{0}\left\|x \frac{\partial u}{\partial x}\right\|_{L^{2}(\mathcal{M})}, & \text { (Continuous injection condition) } \\
\sigma^{2} & <4 r & \text { (Coercivity condition) }
\end{aligned}
$$

## Proposition 3.3.

Under the first condition in assumption 3.2, there exists a unique $L_{\mu}^{2}(\mathcal{M})$-representative $\tilde{u}$ of each equivalence class of functions $u$ in $V_{\mathcal{M}}$ such that the above condition holds. There also exists a $\mathcal{D}(\mathcal{M})$ sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ which converges towards $\tilde{u}$ both in $V_{\mathcal{M}}$ and in $L_{\mu}^{2}(\mathcal{M})$, since $\mathcal{D}(\mathcal{M})$ is dense in $V_{\mathcal{M}}$ and $L_{\mu}^{2}(\mathcal{M})$ Kil94.

Consider the bilinear form $B(\cdot, \cdot)$ with domain $\operatorname{dom}(B)$ on the Hilbert space $V_{\mathcal{M}}$. We introduce the bilinear form:

$$
B^{\star}(\cdot, \cdot)=B(\cdot, \cdot)+\langle\cdot, \cdot\rangle_{L_{\mu}^{2}(\mathcal{M})}
$$

and the symmetric one:

$$
\tilde{B}^{\star}(\cdot, \cdot)=\tilde{B}(\cdot, \cdot)+\langle\cdot, \cdot\rangle_{L_{\mu}^{2}(\mathcal{M})}
$$

We refer to MR92 for further details on the theory of non-symmetric Dirichlet forms.

## Definition 3.1 (Symmetric Closed Form).

A pair $(B, \operatorname{dom}(B))$ is a symmetric closed form $($ on $H)$ if $\operatorname{dom}(B)$ is a dense linear subspace of $H$ and $B: \operatorname{dom}(B) \times \operatorname{dom}(B) \rightarrow \mathbb{R}$ is a positive definite bilinear which is symmetric and closed on $H$ (i.e., $\operatorname{dom}(B)$ is complete with respect to the norm $\left.B^{\star}(\cdot, \cdot)^{\frac{1}{2}}\right)$.

## Definition 3.2 (Sector Condition).

Let us denote by $B$ a bilinear form on the Hilbert space $H$, and by $\operatorname{dom}(B)$ its domain. The pair $(B, \operatorname{dom}(B))$ is said to satisfy:
i. The weak sector condition if there exists $K>0$ such that:

$$
\forall(u, v) \in \operatorname{dom}(B) \times \operatorname{dom}(B): \quad\left|B^{\star}(u, v)\right| \leq K \sqrt{B^{\star}(u, u) B^{\star}(v, v)}
$$

ii. The strong sector condition if there exists $K>0$ such that

$$
\forall(u, v) \in \operatorname{dom}(B) \times \operatorname{dom}(B):|B(u, v)| \leq K \sqrt{B(u, u) B(v, v)}
$$

Remark 3.1.

A coercive continuous bilinear form satisfies both conditions.

## Definition 3.3 (Coercive Closed Form).

A pair $(B, \operatorname{dom}(B))$ will be called a coercive closed form $($ on $H)$ if $\operatorname{dom}(B)$ is a dense linear subspace of $H$ and $B: \operatorname{dom}(B) \times \operatorname{dom}(B) \rightarrow \mathbb{R}$ is a bilinear form such that the following two conditions hold:

i. Its symmetric part $(\tilde{B}, \operatorname{dom}(B))$ is a symmetric closed form on $H$.

ii. ( $B, \operatorname{dom}(B))$ satisfies the weak sector condition inequality $i$. given in (3).

## Definition 3.4 (Symmetric Vs Non-Symmetric Dirichlet Form).

A coercive closed form $(B, \operatorname{dom}(B))$ on $L_{\mu}^{2}(\mathcal{M})$, for a given measure $\mu$, will be called a Dirichlet form if, for any $u$ in $\operatorname{dom}(B)$, one has:

$$
\tilde{u} \in \operatorname{dom}(B) \quad \text { and } \quad\left\{\begin{array}{l}
B(u+\tilde{u}, u-\tilde{u}) \geqslant 0 \\
B(u-\tilde{u}, u+\tilde{u}) \geqslant 0
\end{array}\right.
$$

where $\tilde{u}=\max (0, \min (u, 1))$. If $(B, \operatorname{dom}(B))$ is in addition symmetric, this is equivalent to:

$$
B(\tilde{u}, \tilde{u}) \leq B(u, u)
$$

$B$ will be called a symmetric Dirichlet form.

## Theorem 3.4. MR92]

Let us denote by $(B, \operatorname{dom}(B))$ a coercive closed form on $H$, and $J$ a continuous linear functional on $\operatorname{dom}(B)$. Then, there exists a unique $u \in \operatorname{dom}(B)$ such that

$$
\forall v \in \operatorname{dom}(B): \quad B^{\star}(u, v)=J(v)
$$

## Definition 3.5 (Non-Symmetric Dirichlet Forms).

A coercive closed form on $H,(B, \operatorname{dom}(B))$, is said to be a non-symmetric Dirichlet form (on $H$ ), if there exists a one-to-one correspondence with a pair of bounded linear operators $(L, \tilde{L})$ :

$$
\forall(u, v) \in \operatorname{dom}(L) \times \operatorname{dom}(L): \quad B(u, v)=(-L u, v)=(u,-\tilde{L} v)
$$

where $\operatorname{dom}(L)$ is the domain of $L$. Also, $\operatorname{dom}(L)$ is a dense subset of $\operatorname{dom}(B)$.

The operator $L$ (respectively $\tilde{L}$ ) is the generator of a strongly continuous contraction semi-group $\left(T_{t}\right)_{t>0}$ (respectively $(\tilde{T})_{t>0}$ ).

The following result follows from AP05.

## Proposition 3.5 (Poincaré Inequality).

The space $\mathcal{D}(\mathcal{M})$ is dense in $V_{\mathcal{M}}$, and, for any $v \in \mathcal{D}(\mathcal{M})$, the following inequality is satisfied:

$$
\|v\|_{L^{2}(\mathcal{M})} \leq 2\left\|x \frac{d v}{d x}\right\|_{L^{2}(\mathcal{M})}
$$

This inequality induces a second norm on $V_{\mathcal{M}}$, given, for any $v$ in $V_{\mathcal{M}}$, by:

$$
|v|_{V_{\mathcal{M}}}=\left\|x \frac{d v}{d x}\right\|_{L^{2}(\mathcal{M})}
$$

## Proposition 3.6. (Continuity and Gårding Inequality)

The bilinear form $B(\cdot, \cdot)$ is continuous on $V_{\mathcal{M}}$, and satisfies the Gårding inequality:

$$
\forall u \in V_{\mathcal{M}}: \quad B(u) \geqslant \frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}^{2}-\lambda\|u\|_{L^{2}(\mathcal{M})}^{2}
$$

where $\lambda=\frac{\left(\sigma^{2}-3 r\right)}{2}$. Moreover, $B(\cdot, \cdot)$ is coercive under the second assumption 3.2.

Proof.

For any pair $(u, v) \in \mathcal{D}(\mathcal{M}) \times \mathcal{D}(\mathcal{M})$, by using the Poincaré inequality, we obtain that

$$
\begin{aligned}
|B(u, v)| & =\left|\int_{L}^{M} \frac{\sigma^{2} x^{2}}{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\int_{L}^{M}\left(\sigma^{2}-r\right) x \frac{\partial u}{\partial x} v d x+\int_{L}^{M} r u v d x\right| \\
& \leq \frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}|v|_{V_{\mathcal{M}}}+\left(\sigma^{2}-r\right)|u|_{V_{\mathcal{M}}}\|v\|_{L^{2}(\mathcal{M})}+r\|u\|_{L^{2}(\mathcal{M})}\|v\|_{L^{2}(\mathcal{M})} \\
& \leq C_{1}|u|_{V_{\mathcal{M}}}|v|_{V_{\mathcal{M}}}
\end{aligned}
$$

where $C_{1}=2 r+\frac{5 \sigma^{2}}{2}$. For the coercivity, we use again Poincaré inequality:

$$
\begin{aligned}
B(u) & =\frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}^{2}+\int_{L}^{M}\left(\sigma^{2}-r\right) x \frac{\partial u}{\partial x} u d x+r\|u\|_{L^{2}(\mathcal{M})}^{2} \\
& =\frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}^{2}-\frac{\left(\sigma^{2}-3 r\right)}{2}\|u\|_{L^{2}(\mathcal{M})}^{2} \\
& \geqslant C_{2}|u|_{V_{\mathcal{M}}}^{2}
\end{aligned}
$$

where $C_{2}=6 r-\frac{3 \sigma^{2}}{2}$.

## Definition 3.6.

We introduce the mapping $\iota: V_{\mathcal{M}} \rightarrow L_{\mu}^{2}(\mathcal{M})$ by

$$
\iota(u)=\bar{u}
$$

where $\bar{u}$ is the unique $L_{\mu}^{2}(\mathcal{M})$-representative of $u$, along with the closed set:

$$
\mathcal{N}=\left\{v \in V_{\mathcal{M}}:\|v\|_{L_{\mu}^{2}(\mathcal{M})}=0\right\}
$$

## Theorem 3.7. The Black-Scholes Non-Symmetric Dirichlet Form

Under the assumption 3.2:
i. $\operatorname{dom}(B)=V_{\mathcal{M}}$ is dense in $L_{\mu}^{2}(\mathcal{M})$.

ii. $\left(\tilde{B}^{\star}, V_{\mathcal{M}}\right)$ is a Hilbert space.

iiii. $(B, \operatorname{dom}(B))$ is a (non-symmetric) Dirichlet form.

Proof.

- Let us consider a sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ of $\mathcal{D}(\mathcal{M})$, which converges towards $u$ in $L_{\mu}^{2}(\mathcal{M})$.

We then consider two sequences, $\left(a_{n}\right)_{n \in \mathbb{N}} \in \mathcal{N}^{\mathbb{N}}$, and $\left(b_{n}\right)_{n \in \mathbb{N}} \in V_{\mathcal{M}} \mathbb{N}$ such that, for any natural integer $n$,

$$
u_{n}=a_{n}+b_{n}
$$

Then, the sequence $\left(b_{n}\right)_{n \in \mathbb{N}}$ converges to $u$ in $L_{\mu}^{2}(\mathcal{M})$.

- Under the continuous injection condition (1) in assumption 3.2, the induced norm $\tilde{B}^{\star}(\cdot, \cdot)^{\frac{1}{2}}$ is equivalent to the norm $|\cdot|_{V_{\mathcal{M}}}$. Hence, $\left(B^{\star}, \operatorname{dom}(B)\right)$ is complete.
- It follows from the coercivity of $B$ that:

$$
0 \leq C_{2}\left|u^{2}-\tilde{u}^{2}\right|_{V_{\mathcal{M}}}^{2} \leq B(u \pm \tilde{u}, u \mp \tilde{u})
$$

## Theorem 3.8 (Generalized Measure Black-Scholes Operator).

Under the assumption 3.2, there exists a bounded linear operators $\mathcal{B} \mathcal{S}_{\mu}$, that we will call generalized measure Black-Scholes operator, such that, for any pair $(u, v) \in \operatorname{dom}\left(\mathcal{B S}_{\mu}\right) \times \operatorname{dom}(B)$ :

$$
B(u, v)=\left\langle\mathcal{B \mathcal { S } _ { \mu }}(u), v\right\rangle_{L_{\mu}^{2}(\mathcal{M})}
$$

Moreover, we will say that $u \in \operatorname{dom}\left(\mathcal{B S}_{\mu}\right)$ and $\mathcal{B S}_{\mu}(u)=f$ if and only if

$$
B(u, v)=\int_{\mathcal{M}} f v d \mu \quad, \quad \forall v \in V_{0, \mathcal{M}}
$$

Remark 3.2.

The generalized measure Black-Scholes operator is bounded from $V_{\mathcal{M}}$ to $V_{\mathcal{M}}^{\star}$ since, $\forall v \in V_{0, \mathcal{M}}$

$$
\begin{aligned}
\left|\left\langle\mathcal{B S}_{\mu}(u), v\right\rangle_{L_{\mu}^{2}(\mathcal{M})}\right| & =|B(u, v)| \\
& \leq C_{1}|u|_{V_{\mathcal{M}}}|v|_{V_{\mathcal{M}}}
\end{aligned}
$$

by continuity of $B(\cdot, \cdot)$.

## Notations (Sobolev Spaces).

Given a continuous subset $E$ of $\mathbb{R}, k \in \mathbb{N}$, and $p \geqslant 1$, we recall that the classical Sobolev spaces on $E$ are

$$
W_{p}^{k}(E)=\left\{f \in L^{p}(E), \forall j \leq k: f^{(j)} \in L^{p}(E)\right\}
$$

and

$$
H^{k}(E)=W_{2}^{k}(E)=\left\{f \in L^{2}(E), \forall j \leq k: f^{(j)} \in L^{2}(E)\right\}
$$

The subspace $H_{0}^{k}$ of functions which vanish on the boundary $\partial E$ is

$$
H_{0}^{k}(E)=\left\{f \in L^{2}(E), f_{\mid \partial E}=0 \text { and } \forall j \leq k: f^{(j)} \in L^{2}(E)\right\}
$$

that:

It directly comes form the abstract theory of partial differential equations [Zei90, Wlo87, [LM68

Theorem 3.9 (Generalized Measure Black-Scholes Weak Solution).

Let us define the Gelfand triple (or equipped Hilbert space) $V_{\mathcal{M}} \subset L_{\mu}^{2}(\mathcal{M}) \subset V_{\mathcal{M}}^{\star}$. For $h$ in $L_{\mu}^{2}(\mathcal{M})$, the generalized measure Black-Scholes problem admits, under the assumptions 3.2. a unique weak solution. Moreover, for $k \geqslant 1$, the solution map:

$$
\begin{aligned}
L_{\mu}^{2}(\mathcal{M}) & \longrightarrow W_{2}^{k}\left([0, T] ; V_{\mathcal{M}}\right) \\
\quad h(x) & \longrightarrow u(t, x) \quad, \quad x \in \mathcal{M} \quad \text { and } \quad t \in[0, T]
\end{aligned}
$$

is continuous.

## 4 The Self-Similar Black-Scholes Operator - a Pointwise Formula

Definition 4.1 (Self-Similar Measure on a Real Interval, Associated to a Set of Contractions [Str06].

We hereafter consider the particular case where the real interval $\mathcal{M}=] L, M\left[\subset \mathbb{R}_{+}\right.$is self-similar with respect to the family of contractions $\left\{f_{1}, f_{2}\right\}$, and where $f_{1}$ and $f_{2}$ are defined, for any real number $x$, by:

$$
f_{1}(x)=\frac{1}{2}(x+L) \quad, \quad f_{2}(x)=\frac{1}{2}(x+M)
$$

A measure $\mu$ with full support on $\overline{\mathcal{M}}$ will be called self-similar measure on $\overline{\mathcal{M}}$, relative to the set of contractions $\left(f_{1}, f_{2}\right)$ if, given a family of strictly positive weights $\left(\mu_{1}, \mu_{2}\right)$ such that

$$
\mu_{1}+\mu_{2}=1
$$

one has, then,

$$
\mu=\mu_{1} \mu \circ f_{1}^{-1}+\mu_{2} \mu \circ f_{2}^{-1}
$$

Let us consider $u \in \operatorname{dom}\left(\mathcal{B S}_{\mu}\right)$ where $\mu$ is a self-similar measure according to definition 4.1 . $\mathcal{B S}_{\mu}$ is now called the self-similar Black-Scholes operator and we set: $\mathcal{B S}_{\mu}(u)=f$.

In order to compute the explicit formula of $\mathcal{B} \mathcal{S}_{\mu}$, we set $\mathbb{M}=M-L$ and we recall the self similar construction of $\mathcal{M}$ :

$$
\overline{\mathcal{M}}=f_{1}(\overline{\mathcal{M}})+f_{2}(\overline{\mathcal{M}})
$$

## Definition 4.2 (Prefractal Graph Approximation).

We denote by $V_{0}$ the ordered set of the (boundary) points:

$$
\{L, M\}
$$

We build the graph $\mathcal{M}_{0}$ by connecting the two extremities of $V_{0}$.

For any strictly positive integer $m$, we set:

$$
V_{m}=f_{1}\left(V_{m-1}\right)+f_{2}\left(V_{m-1}\right)
$$

The set of points $V_{m}$, where consecutive points are connected, will be denoted by $\mathcal{M}_{m}$.

The set $V_{m}$ is called the set of vertices of the graph $\mathcal{M}_{m}$. By extension, we will write that

$$
\mathcal{M}_{m}=f_{1}\left(\mathcal{M}_{m-1}\right)+f_{2}\left(\mathcal{M}_{m-1}\right)
$$

One can prove that the sequence $\left\{V_{m}\right\}_{m \in \mathbb{N}}$ is increasing and its limit is dense in $\mathcal{M}$ (Kig01).

## Proposition 4.1.

Given a natural integer $m$, we will denote by $\mathcal{N}_{m}$ the number of vertices of the graph $\mathcal{M}_{m}$. One has:

$$
\mathcal{N}_{0}=2
$$

and, for any strictly positive integer $m$ :

$$
\mathcal{N}_{m}=2^{m}+1
$$

We recall the following definitions:

## Definition 4.3 (Word).

Given a strictly positive integer $m$, we will call number-letter any integer $\mathcal{W}_{i}$ of $\{1,2\}$, and word of length $|\mathcal{W}|=m$, on the graph $\mathcal{M}_{m}$, any set of number-letters of the form:

$$
\mathcal{W}=\left(\mathcal{W}_{1}, \ldots, \mathcal{W}_{m}\right)
$$

We will write:

$$
f_{\mathcal{W}}=f_{\mathcal{W}_{1}} \circ \ldots \circ f_{\mathcal{W}_{m}}
$$

## Definition 4.4 (Addresses).

Given a natural integer $m$, and a vertex $X$ of $\mathcal{M}_{m}$, we will call address of the vertex $X$ an expression of the form

$$
X=f_{\mathcal{W}}(L) \quad \text { or } \quad X=f_{\mathcal{W}^{\prime}}(M)
$$

where $\mathcal{W}$ and $\mathcal{W}^{\prime}$ denote words of length $m$. The vertex $X$ has thus a double address.

## Property 4.2 (Space of Harmonic Splines).

Given a strictly positive integer $m$, we introduce the space of harmonic splines of order $m$, denoted by $\mathcal{H}^{m}([L, M])$, as the space of functions $\psi_{X}^{m}, X \in[L, M]$, such that:

$$
\forall Y \in \mathcal{M}_{m} \quad \psi_{X}^{m}(Y)=\delta_{X Y}
$$

For $k \in\left\{1, \ldots, 2^{m}-1\right\}$, and $Y \in[L, M]$ :

$$
\psi_{L+\frac{k \mathbb{M}}{2^{m}}}^{m}(Y)=\left\{\begin{array}{lc}
\frac{2^{m}}{\mathbb{M}}(Y-L)-(k-1) & L+\frac{(k-1) \mathbb{M}}{2^{m}} \leq Y \leq L+\frac{k \mathbb{M}}{2^{m}} \\
-\frac{2^{m}}{\mathbb{M}}(Y-L)+(k+1) & L+\frac{k \mathbb{M}}{2^{m}} \leq Y \leq L+\frac{(k+1) \mathbb{M}}{2^{m}} \\
0 \quad \text { otherwise }
\end{array}\right.
$$

and

$$
\begin{aligned}
& \psi_{L}^{m}(Y)= \begin{cases}-\frac{2^{m}}{\mathbb{M}}(Y-L)+1 & L \leq Y \leq L+\frac{\mathbb{M}}{2^{m}} \\
0 & \text { otherwise }\end{cases} \\
& \psi_{M}^{m}(Y)= \begin{cases}\frac{2^{m}}{\mathbb{M}}(Y-M)+1 \\
0 & \text { otherwise }\end{cases}
\end{aligned}
$$

Proposition 4.3 (Integration of Harmonic Splines).

Let us consider a strictly positive integer $m$. For $k \in\left\{1, \ldots, 2^{m}-1\right\}$, we denote by $\mathcal{V}_{\mathcal{M} k}$ and $\mathcal{W}_{k}$ the unique indices such that

$$
f_{\mathcal{V}_{\mathcal{M} k}}([L, M])=\left[L+\frac{(k-1) \mathbb{M}}{2^{m}}, L+\frac{k \mathbb{M}}{2^{m}}\right] \quad \text { and } \quad f_{\mathcal{W}_{k}}([L, M])=\left[L+\frac{k \mathbb{M}}{2^{m}}, L+\frac{(k+1) \mathbb{M}}{2^{m}}\right]
$$

Then,

$$
\int_{L}^{M} \psi_{L+\frac{k \mathbb{M}}{2^{m}}}^{m} d \mu=\mu_{1}^{s \mathcal{V}_{\mathcal{M} k}} \mu_{2}^{m+1-s \mathcal{V}_{\mathcal{M} k}}+\mu_{1}^{s \mathcal{W}_{k}+1} \mu_{2}^{m-s_{\mathcal{W}_{k}}}
$$

and

$$
\int_{L}^{M} \psi_{L}^{m} d \mu=\mu_{1}^{m+1} \quad \int_{L}^{M} \psi_{M}^{m} d \mu=\mu_{2}^{m+1}
$$

In addition, if $\mu_{1}<\frac{1}{2}$ :

$$
\int_{L}^{M} \psi_{L}^{m} d \mu<\int_{L}^{M} \psi_{L+\frac{k M}{2^{m}}}^{m} d \mu<\int_{L}^{M} \psi_{M}^{m} d \mu
$$

Property 4.4. Given a strictly positive integer $m$, we set, for any integer $k \in\left\{0, \ldots, 2^{m}\right\}$ :

$$
x_{k}=L+\left(k \frac{\mathbb{M}}{2^{m}}\right)
$$

and, for any $u \in \operatorname{dom}\left(\mathcal{B S}_{\mu}\right)$ :

$$
\begin{aligned}
B\left(u, \psi_{x_{k}}^{m}\right) & =\int_{L}^{M}\left(-\frac{\sigma^{2} x^{2}}{2} \frac{\partial^{2} u}{\partial x^{2}}-r x \frac{\partial u}{\partial x}+r u\right) \psi_{x_{k}}^{m} d x \\
& =\lim _{m \rightarrow+\infty} \sum_{j=0}^{2^{m}} \mathcal{B} \mathcal{S}_{m}\left(u\left(t, x_{j}\right)\right) \psi_{x_{k}}^{m}\left(\frac{\mathbb{M}}{2^{m}}\right) \\
& =\lim _{m \rightarrow+\infty} \mathcal{B} \mathcal{S}_{m}\left(u\left(t, x_{k}\right)\right)\left(\frac{\mathbb{M}}{2^{m}}\right)
\end{aligned}
$$

where $\mathcal{B S}_{m}$ is the discrete Black-Scholes operator defined, for any $t$ in $[0, T]$, by:

$$
\begin{aligned}
\mathcal{B} \mathcal{S}_{m} u\left(t, x_{k}\right) & =-\frac{\sigma^{2}}{2} x_{k}^{2}\left(\frac{u\left(t, x_{k+1}\right)-2 u\left(t, x_{k}\right)+u\left(t, x_{k-1}\right)}{\left(\frac{\mathbb{M}}{2^{m}}\right)^{2}}\right) \\
& -r x_{k}\left(\frac{u\left(t, x_{k+1}\right)-u\left(t, x_{k-1}\right)}{2\left(\frac{\mathbb{M}}{2^{m}}\right)}\right)+r C\left(t, x_{k}\right) \\
& =-\frac{\sigma^{2}}{2} k^{2}\left(u\left(t, x_{k+1}\right)-2 u\left(t, x_{k}\right)+u\left(t, x_{k-1}\right)\right) \\
& -r k\left(\frac{u\left(t, x_{k+1}\right)-u\left(t, x_{k-1}\right)}{2}\right)+r C\left(t, x_{k}\right)
\end{aligned}
$$

The mean value formula yields asymptotically

$$
\int_{L}^{M} \mathcal{B} \mathcal{S}_{\mu} u(x) \psi_{x_{k}}^{m} d \mu \approx \mathcal{B} \mathcal{S}_{\mu} u\left(x_{k}\right) \int_{L}^{M} \psi_{x_{k}}^{m} d \mu
$$

Theorem 4.5 (Self-Similar Black-Scholes Operator Pointwise Formula).

Let us consider $u \in \operatorname{dom}\left(\mathcal{B S}_{\mu}\right)$. Then, for any $x \in \overline{\mathcal{M}}$, and any sequence $\left(x_{m}\right)_{m \in \mathbb{N}}$ of $V_{m} \backslash V_{0}$ which uniformly converges towards $x$ :

$$
\mathcal{B S}_{\mu}(u)(x)=\lim _{m \rightarrow+\infty} 2^{-m}\left(\int_{L}^{M} \psi_{x_{m}}^{m} d \mu\right)^{-1} \mathcal{B} \mathcal{S}_{m}(u)\left(x_{m}\right)
$$

Proof.

The uniform convergence directly comes from the fact that

$$
\left(\frac{\mathbb{M}}{2^{m}}\right)\left(\int_{L}^{M} \psi_{x_{m}}^{m} d \mu\right)^{-1} \mathcal{B} \mathcal{S}_{m}(u)\left(x_{m}\right)=C \frac{\int_{L}^{M} \mathcal{B} \mathcal{S}_{\mu} \psi_{x_{m}}^{m} d \mu}{\int_{L}^{M} \psi_{x_{m}}^{m} d \mu}=C \mathcal{B} \mathcal{S}_{\mu}(u)(x)
$$

For $\mu_{1}=\mu_{2}=\frac{1}{2}$, one recovers the classical Black-Scholes operator, which implies that: $C=\mathbb{M}$.

## 5 Proof of the Assumptions

We hereafter consider the general case of non atomic finite measure $\mu$ with total mass $\mathbb{M}=M-L$ (In the case of self-similar measures, it suffice to multiply the measure by $\mathbb{M}$ ).

### 5.1 First assumption 3.2

## Notation (Space of Weighted Continuous Functions).

We will denote by $C(\overline{\mathcal{M}})$ the space of weighted continuous functions on $\overline{\mathcal{M}}$ endowed with the norm

$$
\|u\|_{\eta, \infty}=\max _{x \in \overline{\mathcal{M}}}|x u(x)|
$$

## Proof. of the first assumption

Let us consider $u \in V_{0, \mathcal{M}}$. On the one hand, we have that

$$
\begin{aligned}
|x u(x)| & =\left|\int_{L}^{x}(s u(s))^{\prime} d s\right| \\
& =\left|\int_{L}^{x} u(s) d s+\int_{L}^{x} s u^{\prime}(s) d s\right| \\
& \leq \sqrt{\mathbb{M}}\left(\|u\|_{L^{2}}+|u|_{V_{\mathcal{M}}}\right) \\
& \leq \sqrt{\mathbb{M}}\|u\|_{V_{\mathcal{M}}}
\end{aligned}
$$

We deduce the continuity of the injection $\iota:\left(V_{\mathcal{M}},\|\cdot\|_{V_{\mathcal{M}}}\right) \rightarrow\left(C_{\eta}(\overline{\mathcal{M}}),\|\cdot\|_{\eta, \infty}\right)$. On the other hand, for $u \in C_{\eta}(\overline{\mathcal{M}})$, one also has that

$$
\|u\|_{L_{\mu}^{2}(\mathcal{M})}=\left(\int_{L}^{M} \frac{1}{x^{2}}(x u)^{2} d \mu\right)^{\frac{1}{2}} \leq\|u\|_{\eta, \infty}\left(\int_{L}^{M} \frac{1}{x^{2}} d \mu\right)^{\frac{1}{2}} \leq\|u\|_{\eta, \infty} \frac{\mu(\overline{\mathcal{M}})^{\frac{1}{2}}}{L}
$$

the injection $\iota:\left(C_{\eta}(\overline{\mathcal{M}}),\|\cdot\|_{\eta, \infty}\right) \rightarrow\left(L_{\mu}^{2}(\mathcal{M}),\|\cdot\|_{L_{\mu}^{2}(\mathcal{M})}\right)$ is continuous, so we obtain that

$$
\|u\|_{L_{\mu}^{2}(\mathcal{M})} \leq C_{0}\|u\|_{V_{\mathcal{M}}}
$$

for $C_{0}=\frac{\sqrt{\mathbb{M} \mu(\overline{\mathcal{M}})}}{L}=\frac{\mathbb{M}}{L}$.

### 5.2 Commentary on the second assumption 3.2

The assumption $4 r>\sigma^{2}$ is not that restrictive as it may seem in the first sight, for example, if we give a look to sample from Vance L. Martin data LMM05. The sample consist of $\mathbf{N}=269$ observations on the European call options written on the S\&P500 stock index on the $4^{\text {th }}$ of April, 1995. One can calculate (see RD21)

- The interest rate $r=0.0591$.
- The volatility $\sigma=0.076675$.

which means that

$$
4 r=0.2364 \gg 0.00587906=\sigma^{2}
$$

The second assumption could also be replaced by the following condition: for any $u$ in $\mathcal{D}(\mathcal{M})$,

$$
\|u\|_{L^{2}(\mathcal{M})} \leq C_{3}\|u\|_{L_{\mu}^{2}(\mathcal{M})}
$$

Given $u$ in $\operatorname{dom}(B)$, set, in the spirit of Wlo87:

$$
\tilde{\lambda}=\lambda C_{3} \quad, \quad w(t, x)=e^{-\tilde{\lambda} t} u(T-t, x)
$$

where $\lambda$ is Gårding's inequality constant in proposition 3.6 Then $\forall v \in \operatorname{dom}(B)$, with $w(0, x)=h(x)$, one has:

$$
\int_{L}^{M} \frac{d}{d t} w(t, x) v(x) d \mu=-B(w, v)-\tilde{\lambda} \int_{L}^{M} w(t, x) v(x) d \mu=-\hat{B}(w, v)
$$

Without affecting the solution space, one obtains the continuity and the coercivity of the form $\widehat{B}$ :

$$
\begin{aligned}
|\widehat{B}(u, v)| & \leq C|u|_{V_{\mathcal{M}}}|v|_{V_{\mathcal{M}}}+\tilde{\lambda}\|u\|_{L_{\mu}^{2}(\mathcal{M})}\|v\|_{L_{\mu}^{2}(\mathcal{M})} \\
& \leq\left(C+\tilde{\lambda} C_{0}\right)|u|_{V_{\mathcal{M}}}|v|_{V_{\mathcal{M}}}
\end{aligned}
$$

and:

$$
\begin{aligned}
\widehat{B}(u, u) & \geqslant \frac{\sigma^{2}}{4}|u|_{V_{\mathcal{M}}}^{2}-\lambda\|u\|_{L^{2}(\mathcal{M})}^{2}+\tilde{\lambda}\|u\|_{L_{\mu}^{2}(\mathcal{M})}^{2} \\
& \geqslant \frac{\sigma^{2}}{4}|u|_{V_{\mathcal{M}}}^{2}
\end{aligned}
$$

### 5.3 Underlying asset price bounds

An important question arises: how to choose $M$ and $L$ ? one answer is to use the law of $S_{t}$, the underlying asset price, then choose $M(\alpha)$ (respectively $L(\alpha)$ ) using the rule:

$$
1-\mathbb{P}\left(L(\alpha) \leq S_{t} \leq M(\alpha)\right) \leq \alpha \quad, \quad 0 \leq t \leq T
$$

for some tolerance level $\alpha$.

One can deduce a similar rule in the case of boundary conditions. For example, in the case of a call option:

$$
\mathbb{P}\left(S_{T}>K \mid S_{0}=L(\alpha)\right) \leq \alpha
$$

and

$$
\mathbb{P}\left(S_{T} \leq K \mid S_{0}=M(\alpha)\right) \leq \alpha
$$

## 6 Numerical Simulation of Self-Similar European Options

Let us consider as in section 4, the self-similar case, for an European options call, defined by the system:

$$
\begin{array}{rlrl}
\frac{\partial C}{\partial t}(t, S) & =\mathcal{B S}_{\mu}(C)(t, S) & \forall t \in[0, T], & \forall S \in \mathcal{M} \\
C(T, S) & =h(S) & \forall S \in \mathcal{M} \\
C(t, L) & =0 & \forall t \in[0, T] \\
C(t, M) & =g(t) & \forall t \in[0, T]
\end{array}
$$

for a self-similar measure $\mu$ on $\overline{\mathcal{M}}$, under the condition

$$
4 r>\sigma^{2}
$$

where $h(S)=(S-K)^{+}$and $g(t)=M-K \exp (-r(T-t))$, and where the constant $\sigma$ is the volatility, $r$ the risk-free interest rate, $T$ the maturity of the option and $C$ represents the call price.

We will use the following change of variables: $\tau=T-t$, which leads to the following equation (with the same notations):

$$
\begin{array}{rlrl}
-\frac{\partial C}{\partial t}(t, S) & =\mathcal{B} \mathcal{S}_{\mu}(C)(t, S) & \forall t \in[0, T], & \forall S \in \mathcal{M} \\
C(0, S) & =h(S) & \forall S \in \mathcal{M} \\
C(t, L) & =0 & \forall t \in[0, T] \\
C(t, M) & =g(t) & \forall t \in[0, T]
\end{array}
$$

for $g(t)=M-K \exp (-r t)$.

Remark 6.1.

The results of section 3 still hold, if we write $\tilde{C}=C-\tilde{g}$, where $\tilde{g}(t, x)=(x-L)\left(\frac{M-K \exp (-r t)}{M-L}\right)$, and replace the space $V_{\mathcal{M}}$ by $V_{0, \mathcal{M}}$, then we solve the non homogeneous problem

$$
\int_{L}^{M} \frac{\partial \tilde{C}}{\partial t} v d \mu+B(\tilde{C}, v)=\int_{L}^{M} \frac{d \tilde{g}}{d t} v d \mu
$$

applying abstract theory of partial differential equations Wlo87.

### 6.1 The Finite Difference Method

In the spirit of our previous work [RD19, we fix a strictly positive integer $N$, and set:

$$
h=\frac{T}{N}
$$

We will write, for a function $f, n \in\{0, \ldots, N\}$ and $k \in\left\{0, \ldots, 2^{m}\right\}$ :

$$
f(h, k)=f\left(n h, L+k \frac{\mathbb{M}}{2^{m}}\right)
$$

We use the Euler implicit scheme, for any integer $n$ belonging to $\{0, \ldots, N-1\}$ :

$$
\forall k \in\left\{0, \ldots, 2^{m}\right\}: \quad \frac{\partial C}{\partial t}(n, k) \approx \frac{1}{h}(C(n+1, k)-C(n, k))
$$

The self-similar Black-Scholes operator for $k=\left\{0, \ldots, 2^{m}\right\}$ is approximated through

$$
\begin{aligned}
\mathcal{B S}_{\mu} C(n, k) & \approx\left(\frac{2^{-m}}{\mu_{1}{ }^{s \mathcal{V}_{\mathcal{M}} \mu_{2}}{ }^{m-s_{\mathcal{V}} \mathcal{M}^{+1}}+\mu_{1}{ }^{s \mathcal{W}+1} \mu_{2}{ }^{m-s \mathcal{W}}}\right) \mathcal{B} \mathcal{S}_{m} C(n, k) \\
& \approx \delta_{m} \mathcal{B S}_{m} C(n, k)
\end{aligned}
$$

where $\mathcal{B} \mathcal{S}_{m}$ is the discretized Black-Scholes operator given by

$$
\begin{aligned}
\mathcal{B} \mathcal{S}_{m} C(n, k) & =-\frac{\sigma^{2}}{2}\left(\frac{k \mathbb{M}}{2^{m}}\right)^{2}\left(\frac{C(n, k+1)-2 C(n, k)+C(n, k-1)}{\left(\frac{\mathbb{M}}{2^{m}}\right)^{2}}\right) \\
& -r\left(\frac{k \mathbb{M}}{2^{m}}\right)\left(\frac{C(n, k+1)-C(n, k-1)}{2\left(\frac{\mathbb{M}}{2^{m}}\right)}\right)+r C(n, k)
\end{aligned}
$$

For $0 \leq n \leq N-1$, and $1 \leq k \leq 2^{m}-1$, we define the following scheme:

$$
\left(\mathcal{S}_{\mathcal{B S}}\right)\left\{\begin{array}{ccc}
-\frac{\mathcal{C}_{h, m}(n+1, k)-\mathcal{C}_{h, m}(n, k)}{h} & = & \delta_{m} \mathcal{B} \mathcal{S}_{m} \mathcal{C}_{h, m}(n, k) \\
\mathcal{C}_{h, m}(n, 0) & = & 0 \\
\mathcal{C}_{h, m}\left(n, 2^{m}\right) & = & g(n) \\
\mathcal{C}_{h, m}(0, k) & = & h(k)
\end{array}\right.
$$

For $n \in\{0, \ldots, N-1\}$, we set:

$$
\mathcal{C}(n)=\left(\begin{array}{c}
\mathcal{C}_{h, m}(n, 1) \\
\vdots \\
\mathcal{C}_{h, m}\left(n, 2^{m}-1\right)
\end{array}\right)=\left(\begin{array}{c}
\mathcal{C}_{h, m}\left(n, f_{\mathcal{W}^{1}}(M)\right) \\
\vdots \\
\mathcal{C}_{h, m}\left(n, f_{\mathcal{W}^{2}}{ }^{m}-1\right. \\
\left.\operatorname{col}^{2}(M)\right)
\end{array}\right) \quad, \quad\left\{\mathcal{W}^{1}, \ldots, \mathcal{W}^{2^{m}-1}\right\} \in\{1,2\}^{m}
$$

We have the following recurrence relation:

$$
\mathcal{C}(n+1)=A \mathcal{C}(n)+B(n)
$$

where the $\left(2^{m}-1\right) \times\left(2^{m}-1\right)$ matrix $A$ is given by:

$$
A=I_{2^{m}-1}-h 2^{-m} \Psi_{m}^{-1} B S_{m}
$$

and where $I_{2^{m}-1}$ denotes the $\left(2^{m}-1\right) \times\left(2^{m}-1\right)$ identity matrix, $\Psi_{m}$ and $B S_{m}$ the $\left(2^{m}-1\right) \times\left(2^{m}-1\right)$ matrices:

$$
\Psi_{m}=\left(\begin{array}{lll}
\ddots & & 0 \\
& \mu_{1}{ }^{s \mathcal{V}_{\mathcal{M}}} \mu_{2}{ }^{m+1-s_{\mathcal{V}}}+\mu_{1}{ }^{s W_{W}+1} \mu_{2}{ }^{m-s w} & \\
0 & & \ddots
\end{array}\right)
$$

$$
B S_{m}=\left(\begin{array}{cccccc}
-\sigma^{2}-r & \frac{\sigma^{2}}{2}+\frac{r}{2} & 0 & \ldots & 0 & 0 \\
2 \sigma^{2}-r & -4 \sigma^{2}-r & 2 \sigma^{2}+r & \ldots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \cdots & -\left(2^{m}-2\right)^{2} \sigma^{2}-r & \left(2^{m}-2\right)^{2} \frac{\sigma^{2}}{2}+\left(2^{m}-2\right) \frac{r}{2} \\
0 & 0 & 0 & \cdots & \left(2^{m}-1\right)^{2} \frac{\sigma^{2}}{2}-\left(2^{m}-1\right) \frac{r}{2} & -\left(2^{m}-1\right)^{2} \sigma^{2}-r
\end{array}\right)
$$

and

$$
B(n)=h 2^{-m} \mu_{2}^{-(m+1)}\left(\left(2^{m}-1\right)^{2} \frac{\sigma^{2}}{2}+\left(2^{m}-1\right) \frac{r}{2}\right)\left(\begin{array}{c}
0 \\
\vdots \\
0 \\
g(n)
\end{array}\right)
$$

### 6.2 Numerical Analysis

### 6.2.0.1 The Scheme Error and Consistency

Let us consider a function $V_{\mathcal{M}}$ defined on $\mathcal{M}$. For any integer $n$ in $\{0, \ldots, N-1\}$, and any $X$ in $\mathcal{M}$ :

$$
\frac{\partial v}{\partial t}(n h, X)=\frac{1}{h}(v((n+1) h, X)-v(n h, X))+\mathcal{O}(h)
$$

As in RD19, for any strictly positive integer $m$, and any $X$ in $V_{m} \backslash V_{0}$, we can prove that:

$$
2^{-m}\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right)^{-1} \mathcal{B} \mathcal{S}_{m} v(X)=\frac{\int_{L}^{M} \mathcal{B} \mathcal{S}_{\mu} \psi_{X}^{m} d \mu}{\int_{L}^{M} \psi_{X}^{m} d \mu}
$$

and that there exists a vertex $Z$ in the $m$-cell $f_{\mathcal{W}}([L, M])$ containing $X$ such that

$$
\begin{aligned}
\left|\mathcal{B} \mathcal{S}_{\mu} v(X)-2^{-m}\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right)^{-1} \mathcal{B S}_{m} v(X)\right| & =\left|\mathcal{B S} \mathcal{S}_{\mu} v(X)-\mathcal{B S}_{\mu} v(Z)\right| \\
& \lesssim|v(X)-v(Z)| \\
& \lesssim|X-Z| \\
& \lesssim\left(\frac{1}{2}\right)^{m}
\end{aligned}
$$

using remark 3.2 and the uniform continuity of $v \in V_{\mathcal{M}}$. Thus,

$$
\mathcal{B} \mathcal{S}_{\mu} v(X)=2^{-m}\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right)^{-1} \mathcal{B} \mathcal{S}_{m} v(X)+\mathcal{O}\left(2^{-m}\right)
$$

The consistency error of our scheme is given by :

$$
\varepsilon_{n, k}^{h, m}=\mathcal{O}(h)+\mathcal{O}\left(2^{-m}\right) \quad 0 \leq n \leq N, 0 \leq k \leq 2^{m}
$$

We can check that the scheme is consistent:

$$
\lim _{h \rightarrow 0, m \rightarrow \infty} \varepsilon_{n, k}^{h, m}=0
$$

### 6.2.0.2 Stability

We hereafter prove that the scheme is conditionally stable for the $\|\cdot\|_{\infty}$ norm.

Let us recall that, for $0 \leq n \leq N$, and $0 \leq k \leq 2^{m}$ :

$$
\begin{aligned}
\mathcal{C}_{h, m}(n+1, k) & =\mathcal{C}_{h, m}(n, k)\left(1-h \delta_{m} \sigma^{2} k^{2}\right) \\
& +\mathcal{C}_{h, m}(n, k+1)\left(h \delta_{m} \frac{\sigma^{2}}{2} k^{2}+h \delta_{m} \frac{r}{2} k\right) \\
& +\mathcal{C}_{h, m}(n, k-1)\left(h \delta_{m} \frac{\sigma^{2}}{2} k^{2}-h \delta_{m} \frac{r}{2} k\right) \\
& -\mathcal{C}_{h, m}(n, k) h \delta_{m} r \\
& =\mathcal{C}_{h, m}(n, k)\left(1-\alpha_{k}\right)+\mathcal{C}_{h, m}(n, k+1)\left(\frac{\alpha_{k}}{2}+\beta_{k}\right)+\mathcal{C}_{h, m}(n, k-1)\left(\frac{\alpha_{k}}{2}-\beta_{k}\right) \\
& -\mathcal{C}_{h, m}(n, k) \gamma
\end{aligned}
$$

If we consider $\gamma=0$, this is just an affine combination. Moreover, we have:

$$
1-\alpha_{k} \geqslant 1-\sigma^{2} \frac{h 2^{2 m}}{2^{m}\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right)} \geqslant 0 \quad, \quad \frac{\alpha_{k}}{2}-\beta_{k} \geqslant 0 \quad, \quad 1-\gamma \geqslant 0
$$

May we suppose that $\sigma^{2} \geqslant r$ and that the following CFL condition

$$
\frac{h 2^{m}}{\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right)} \leq \frac{1}{\sigma^{2}}
$$

is satisfied, the combination is then convex, and the scheme is stable for the norm $\|\cdot\|_{\infty}$.

For $\gamma \neq 0$, one has:

$$
\begin{aligned}
(1-\gamma) \min _{0 \leq j \leq 2^{m}} \mathcal{C}_{h, m}(n, j) \leq \mathcal{C}_{h, m}(n+1, k) & \leq \max _{0 \leq j \leq 2^{m}} \mathcal{C}_{h, m}(n, j)-\gamma \min _{0 \leq j \leq 2^{m}} \mathcal{C}_{h, m}(n, j) \\
& \leq \max _{0 \leq j \leq 2^{m}} \mathcal{C}_{h, m}(n, j)-\gamma(1-\gamma)^{n} \min _{0 \leq j \leq 2^{m}} \mathcal{C}_{h, m}(0, j) \\
& \leq \max _{0 \leq j \leq 2^{m}} \mathcal{C}_{h, m}(n, j)
\end{aligned}
$$

and the scheme is $\|\cdot\|_{\infty}$-stable under the same conditions.

### 6.2.0.3 Convergence

## Theorem 6.1.

If the above CFL condition holds, the scheme is convergent for the norm $\|\cdot\|_{2, \infty}$ given by:

$$
\left.\left\|\left(\mathcal{C}_{h, m}(n, k)\right)_{0 \leq n \leq N, 0 \leq k \leq 2^{m}}\right\|_{2, \infty}=\max _{0 \leq n \leq N}\left(\sum_{0 \leq k \leq 2^{m}} \mu\left(f_{\mathcal{W}^{k}}(\mathcal{M})\right)\left(\mathcal{C}_{h, m}(n, k)\right)^{2}\right)\right)^{\frac{1}{2}}
$$

where $\mu\left(f_{\mathcal{W}^{k}}(\mathcal{M})\right)$ is the measure of the $f_{\mathcal{W}^{k}}(\mathcal{M})$.

Proof.

For $0 \leq n \leq N$ and $0 \leq k \leq 2^{m}$, we set:

$$
w_{k}^{n}=C(n, k)-\mathcal{C}_{h, m}(n, k)
$$

and

$$
\begin{aligned}
\mathcal{B} \mathcal{S}_{m} C(n, k) & =-\frac{\sigma^{2}}{2}\left(\frac{k \mathbb{M}}{2^{m}}\right)^{2}\left(\frac{C(n, k+1)-2 C(n, k)+C(n, k-1)}{\left(\frac{\mathbb{M}}{2^{m}}\right)^{2}}\right) \\
& -r\left(\frac{k \mathbb{M}}{2^{m}}\right)\left(\frac{C(n, k+1)-C(n, k)}{\left(\frac{\mathbb{M}}{2^{m}}\right)}\right)+r C(n, k)
\end{aligned}
$$

We can check that

$$
\begin{array}{rlrl}
\frac{w_{k}^{n+1}-w_{k}^{n}}{h}-\frac{\sigma^{2}}{2} k^{2} \delta_{m}\left(w_{k+1}^{n}-2 w_{k}^{n}+w_{k-1}^{n}\right)-r k \delta_{m}\left(w_{k+1}^{n}-w_{k}^{n}\right)+r \delta_{m} w_{k}^{n}=\varepsilon_{n, k}^{h, m} & 0 \leq n \leq N-1,1 \leq k \leq 2^{m}-1 \\
w_{0}^{n}=w_{2^{m}}^{n} & =0 & 0 \leq n \leq N \\
w_{k}^{0} & =0 & 1 \leq k \leq 2^{m}-1
\end{array}
$$

Let us set, for any integer $n$ in $\{0, \ldots, N\}$ :

$$
W^{n}=\left(\begin{array}{c}
w_{1}^{n} \\
\vdots \\
w_{2^{m}-1}^{n}
\end{array}\right) \quad, \quad E^{n}=\left(\begin{array}{c}
\varepsilon_{n, 1}^{h, m} \\
\vdots \\
\varepsilon_{n, 2^{m}-1}^{h, m}
\end{array}\right)
$$

One has:

$$
W^{0}=0 \quad \text { and } \quad \forall n \in\{0, \ldots, N-1\}: \quad W^{n+1}=A W^{n}+h E^{n}
$$

By induction, this yields, for any integer $n$ in $\{0, \ldots, N-1\}$ :

$$
W^{n+1}=A^{n} W^{0}+h \sum_{j=0}^{n} A^{j} E^{n-j}=h \sum_{j=0}^{n} A^{j} E^{n-j}
$$

Since $A$ is a symmetric matrix, the CFL stability condition yields, for any integer $n$ in $\{0, \ldots, N\}$ :

$$
\begin{aligned}
\left|W^{n}\right| & \leq h\left(\sum_{j=0}^{n-1}\|A\|^{j}\right)\left(\max _{0 \leq j \leq n-1}\left|E^{j}\right|\right) \\
& \leq h n\left(\max _{0 \leq j \leq n-1}\left|E^{j}\right|\right) \\
& \leq h N\left(\max _{0 \leq j \leq n-1}\left|E^{j}\right|\right) \\
& \leq T\left(\max _{0 \leq j \leq n-1}\left(\sum_{k=1}^{2^{m}-1}\left|\varepsilon_{j, k}^{h, m}\right|^{2}\right)^{\frac{1}{2}}\right)
\end{aligned}
$$

that:

By assuming $\mu_{1} \geqslant \frac{1}{2}$ (the same result holds for $\mu_{1} \leq \frac{1}{2}$ by changing $\mu_{1}$ into $\mu_{2}$ ), we deduce then

$$
\begin{aligned}
\max _{0 \leq n \leq N}\left(\sum_{k=1}^{2^{m}-1} \mu\left(f_{\mathcal{W}^{k}}(\mathcal{M})\right)\left|w_{k}^{n}\right|^{2}\right)^{\frac{1}{2}} & \leq \max _{1 \leq k \leq 2^{m}-1}\left(\mu\left(f_{\mathcal{W}^{k}}(\mathcal{M})\right)\right)^{\frac{1}{2}} \max _{1 \leq n \leq N}\left|W^{n}\right| \\
& \leq \max _{1 \leq k \leq 2^{m}-1}\left(\mu\left(f_{\mathcal{W}^{k}}(\mathcal{M})\right)\right)^{\frac{1}{2}} T\left(\max _{0 \leq n \leq N-1}\left(\sum_{k=1}^{2^{m}-1}\left|\varepsilon_{n, k}^{h, m}\right|^{2}\right)^{1 / 2}\right) \\
& \leq \max _{1 \leq k \leq 2^{m}-1}\left(\mu\left(f_{\mathcal{W}^{k}}(\mathcal{M})\right)\right)^{\frac{1}{2}} T\left(\left(2^{m}-1\right)^{\frac{1}{2}} \max _{0 \leq n \leq N-1,1 \leq k \leq 2^{m}-1}\left|\varepsilon_{n, k}^{h, m}\right|\right) \\
& \leq \sqrt{\left(\mu_{1} \times 2\right)^{m}} T\left(\max _{0 \leq n \leq N-1,1 \leq k \leq 2^{m}-1}\left|\varepsilon_{n, k}^{h, m}\right|\right) \\
& =\sqrt{\left(\mu_{1} \times 2\right)^{m}}\left(\mathcal{O}(h)+\mathcal{O}\left(2^{-m}\right)\right) \\
& =\mathcal{O}\left(\left(\sqrt{\frac{\mu_{1}}{2}}\right)^{m}\right)
\end{aligned}
$$

The scheme is then convergent.

### 6.3 Self-Similar Pricing

In the sequel, we give a numerical simulation of the self-similar pricing, in the case of a call:

$$
\begin{array}{rlrl}
\frac{\partial C}{\partial t}(t, S) & =\mathcal{B S}_{\mu}(C)(t, S) & \forall t \in[0, T], & \forall S \in[L, M[ \\
C(T, S) & =(S-K)^{+} & \forall x \in[L, M[ \\
C(t, L) & =0 & \forall t \in v[0, T] \\
C(t, M) & =M-K \exp (-r(T-t)) & \forall t \in[0, T]
\end{array}
$$

for a self-similar measure $\mu$ on $[L, M]$. The solutions are generated using the finite difference method, for

$$
T=1 \quad, \quad K=150 \quad, \quad \sigma=0.3 \quad, \quad r=0.1
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-23.jpg?height=736&width=1634&top_left_y=423&top_left_x=194)

Figure 1: Black-Scholes solution $u(0, x)$ for different values of the weights.

The self-similar Black-Scholes model generates an exotic pricing for different values of $\mu_{1}$, including the classical one for $\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-23.jpg?height=309&width=529&top_left_y=1650&top_left_x=181)

$\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-23.jpg?height=294&width=529&top_left_y=1663&top_left_x=775)

$\mu_{1}=0.2$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-23.jpg?height=285&width=514&top_left_y=1668&top_left_x=1365)

$\mu_{1}=0.8$.

Figure 2: The call value for different values of the weights.

### 6.4 The Greeks

As in Dav17, we recall that, in finance, the sensitivity of a portfolio to changes in parameters values can be measured through what commonly call "the Greeks", i.e.,

i. The Delta, $\Delta=\frac{\partial C}{\partial S} \in[0,1]$, which enables one to quantify the risk, and is thus the most important Greek. It can also be interpreted as a probability that the option will expire in the money.
ii. The Gamma, $\Gamma=\frac{\partial^{2} C}{\partial S^{2}} \geqslant 0$, which measures the rate of the acceleration of the option price, with respect to changes in the underlying price.

iii. The Vega (the name of which comes from the form of the Greek letter $\nu$ ), $\nu=\frac{\partial C}{\partial \sigma}$, which measures the sensitivity to volatility.

$i v$. The Theta $\Theta=\frac{\partial C}{\partial t}$, which is the time cost of holding an option.

$v$. The rho, $\rho=\frac{\partial C}{\partial r}$, which measures the sensitivity to the risk-free interest rate.

The good strategy, for traders, is to have delta-neutral positions at least once a day, and, whenever the opportunity arises, to improve the Gamma and the Vega.

### 6.4.1 The Delta

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-24.jpg?height=331&width=514&top_left_y=988&top_left_x=197)

$\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-24.jpg?height=323&width=529&top_left_y=995&top_left_x=772)

$\mu_{1}=\frac{1}{3}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-24.jpg?height=306&width=511&top_left_y=998&top_left_x=1366)

$\mu_{1}=\frac{2}{3}$.

Figure 3: The $\Delta$, for different values of the weights.

### 6.4.2 The Gamma

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-24.jpg?height=379&width=529&top_left_y=1715&top_left_x=181)

$\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-24.jpg?height=369&width=531&top_left_y=1726&top_left_x=771)

$\mu_{1}=\frac{1}{3}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-24.jpg?height=354&width=517&top_left_y=1730&top_left_x=1363)

$\mu_{1}=\frac{2}{3}$.

Figure 4: The $\Gamma$, for different values of the weights.

### 6.4.3 The Theta

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=325&width=525&top_left_y=297&top_left_x=183)

$\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=354&width=529&top_left_y=280&top_left_x=775)

$\mu_{1}=\frac{1}{3}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=354&width=517&top_left_y=280&top_left_x=1363)

$\mu_{1}=\frac{2}{3}$.

Figure 5: The $\Theta$, for different values of the weights.

### 6.4.4 The Vega

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=348&width=494&top_left_y=1071&top_left_x=198)

$\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=348&width=531&top_left_y=1071&top_left_x=771)

$\mu_{1}=\frac{1}{3}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=365&width=517&top_left_y=1068&top_left_x=1363)

$\mu_{1}=\frac{2}{3}$.

Figure 6: The $\nu$, for different values of the weights.

### 6.4.5 The rho

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=371&width=525&top_left_y=1845&top_left_x=183)

$\mu_{1}=\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=383&width=531&top_left_y=1833&top_left_x=771)

$\mu_{1}=\frac{1}{3}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_8d021841cae214721ffdg-25.jpg?height=360&width=506&top_left_y=1850&top_left_x=1369)

$\mu_{1}=\frac{2}{3}$.

Figure 7: The $\rho$, for different values of the weights.

### 6.5 Discussion

Let us make a few remarks about the behavior of the solution with respect to the weight $\mu$ at $t=0$ :

i. For $\mu_{1}=\frac{1}{3}$ : the premium is greater than that of the classical model under the strike and smaller above. The Greeks value shows a drastic increase in the strike neighbor, and self-similarity clearly affects in the money region. The Theta shows a slower premium expected decrease.

ii. For $\mu_{1}=\frac{2}{3}$ : the premium is everywhere greater than that of the classical model. The Greeks value increases progressively in the strike neighbor, and self-similarity affects in the money region. The Theta indicates a slower premium expected decrease in the money and a greater decrease deep in the money.

The dynamic generated by the self-similar Black-Scholes model is exotic and enables the emergence of non-standard behaviors, the parameter $\mu_{1}$ can capture the behavior of non confident investors under uncertainty and other factors influencing their perception of future.

The self-similar Black-Scholes equation can be understood as a diffusion equation with a time change through self-similar probability $\mu$, where the cumulative distribution function satisfies for $x \in] 0,1[$, $[0, x]=f_{\mathcal{W}}([0,1])$ for some word $\mathcal{W}$

$$
\mu[0, x]=\Pi_{i \in \mathcal{W}} \mu_{i}
$$

depending on the address (path) of $x$. According to this remark, we can create more exotic behavior by using a self-similar measure $\mu$ with many weights or enable the weights to change over time.

## References

[AP05] Y. Achdou and O. Pironneau. Computational Methods for Option Pricing. Society for Industrial and Applied Mathematics, 2005.

[Dav17] C. David. Control of the Black-Scholes equation. Comput. Math. Appl., 73(7):1566-1575, 2017 .

[For96] P. Fortune. Anomalies in option pricing: The black-scholes model revisited. New England Economic Review, March/April:17-40, 1996.

[HLN06] J. Hu, K.-S. Lau, and S.-M. Ngai. Laplace operators related to self-similar measures on $\mathbb{R}^{d}$. Journal of Functional Analysis, 239:542-565, 2006.

[Kig01] J. Kigami. Analysis on Fractals. Cambridge University Press, 2001.

[Kil94] T. Kilpeläinen. Weighted sobolev spaces and capacity. Annales Academiae Scientiarum Fennicae. Series A I. Mathematica, 19(1):95-113, 1994.

[KN01] R. Kangro and R. Nicolaides. Far field boundary conditions for black-scholes equations. SIAM Journal on Numerical Analysis, 38(4):1357-1368, 2001.

[LM68] J.-L. Lions and E. Magenes. Problèmes aux limites non homogènes et applications. Dunod, 1968 .

[LMM05] G. C. Lim, G. M. Martin, and V. L. Martin. Parametric pricing of higher order moments in s\&p500 options. Journal of Applied Econometrics, 20(3):377-404, 2005.

[Man97] B. B. Mandelbrot. Fractals and Scaling in Finance. Springer New York, 1997.

[MR92] Z.-M. Ma and M. Röckner. Introduction to the Theory of (Non-Symmetric) Dirichlet Forms. Springer-Verlag, 1992.

[RD19] N. Riane and C. David. The finite difference method for the heat equation on sierpiński simplices. International Journal of Computer Mathematics, 96(7):1477-1501, 2019.

[RD21] N. Riane and C. David. An inverse black-scholes problem. Optimization and Engineering, 22:2183-2204, 2021.

[Str06] R. S. Strichartz. Differential Equations on Fractals. A Tutorial. Princeton University Press, 2006 .

[Wlo87] J. Wloka. Partial differential equations. Cambridge University Press, 1987.

[Zei90] E. Zeidler. Nonlinear Functional Analysis and its Applications. II/A.: Linear Monotone Operators. Springer, 1990.


[^0]:    ${ }^{1}$ nizar.riane@gmail.com

    ${ }^{2}$ Corresponding author: Claire.David@Sorbonne-Universite.fr

[^1]:    ${ }^{3}$ Courant-Friedrichs-Lewy.

    ${ }^{4}$ When the option has what is also called an intrinsic value, i.e. the real value of the option, that is to say the profit that could be made in the event of immediate exercise. It means that the value is at a favorable strike price relative to the prevailing market price of the underlying asset. Yet, this does not mean that the trader will be making profit, since the expense of buying, and the commission prices have also to be considered.

    ${ }^{5}$ When the option has what is also called an extrinsic value, i.e. a value at a strike price higher than the market price of the underlying asset. In such a case, the Delta, i.e. the Greek which quantifies the risk, is less than 50.

    ${ }^{6}$ The call is an option on a financial instrument, which consists in a right to buy. Concretely, it consists in a contract which allows the subscriber to get the targeted financial product, at a price fixed in advance - the strike price - at a given date - the expiry one, or maturity of the call.

    ${ }^{7}$ As for the put, it is this time a right to sell - or not - at the maturity date.

