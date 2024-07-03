# Generalized Measure Black-Scholes Equation: Towards Option Self-Similar Pricing

Nizar Riane:;, Claire David; April 9, 2024
: **Université Mohammed V de Rabat, FSJESR-Agdal, Maroc**1
; **Sorbonne Université**
CNRS, UMR 7598, Laboratoire Jacques-Louis Lions, 4, place Jussieu 75005, Paris, France2 Abstract In this work, we give a generalized formulation of the Black-Scholes model. The novelty resides in considering the Black-Scholes model to be valid on 'average', but such that the pointwise option price dynamics depends on a measure representing the investors' 'uncertainty'.

We make use of the theory of non-symmetric Dirichlet forms and the abstract theory of partial differential equations to establish well posedness of the problem. A detailed numerical analysis is given in the case of self-similar measures.

Keywords**: Generalized measure Black-Scholes equation; self-similar measure; non-symmetric Dirichlet form; fractal differential equations; finite difference method.**
AMS Classification**: 28A80 - 91G20 - 65L12 - 65L20.**

## 1 Introduction

The Black-Scholes model arises as one of the most important application of mathematics to economics and finance of the 20th **century, allowing the emergence of the theory of financial partial**
differential equations and the associated numerical analysis.

Yet, despite its phenomenal success in the financial market, **the model suffers from deficiencies, for**
instance, when it comes to the modeling of real market options with erratic behaviors [For96]. One can argue that the model does not capture all the factors influencing investor decisions.

From a practical point of view, investors employ technical analysis to detect patterns in price evolution graphs to beat the market; since those patterns seem to appear in small and large scales, this could justify a self-similar modelling of the market. Investigation of fractals in finance is not new, we can refer, for instance, to Benoît Mandelbrot's work in [Man97], the aspects of which are not taken 1nizar.riane@gmail.com 2Corresponding author: Claire.David@Sorbonne-Universite.fr In this paper, we give a definition of a general version of the Black-Scholes model, based on the theory of non-symmetric Dirichlet forms, and on the abstract theory of partial differential equations.

The key point is to consider the Black-Scholes equation describing an average evolution, while the exact dynamics depends on uncertainty captured by a mathematical measure. The analysis goes so far as proving the existence of a **Generalized Black-Scholes operator**.

Special treatment is given to the self-similar case by writing an explicit formula, which enables computation of the solution. The CFL3**convergence condition for the associated finite difference scheme is**
determined and written explicitly. For the proper calibration, our model can avoid overpricing options at the money, and underpricing options at the ends, either deep in the money4, or deep **out of** the money5. This work opens the way to an empirical investigation and an **inverse problem of the**
probability measure µ.

## 2 Generalized Measure Black-Scholes Model Definition 2.1 (**Generalized Measure Black-Scholes Equation**).

Let's introduce the generalized measure Black-Scholes equation, for European options, in the sense of distributions:

%
$$\frac{\partial u}{\partial t}(t,x)\,d\mu=\left(-r(t)\,x\,\frac{\partial u}{\partial x}(t,x)-\frac{\sigma^{2}(t)}{2}\,x^{2}\,\Delta u(t,x)+r(t)\,u(t,x)\right)\,dx\forall\,(t,x)\in[0,T]\times]L,M[\,\forall\,x\in[L,M]$$ $$u(T,x)=h(x)\forall\,x\in[L,M]$$
$&
where the variable 0 ă L ă x ă M is the price of the underlying financial instrument, σ **denotes the**
volatility, r the risk-free interest rate, T the maturity of the option, µ **a non atomic finite measure with**
total mass M " M ´ L and u represents the option price. The real valued function h **takes the values**
hpx**q " p**x ´ Kq
` for a call6, and hpx**q " p**K ´ xq
` for a put 7, given a constant K**: "the strike".**
In order to prove that the problem has a solution, technical results associated to the classical Black-Scholes model are required. We refer to [AP05] for the proof of the following assertions.

## Notation (**Space Of Test Functions**).

Given a continuous subset E of R, we will denote by DpEq the space of test functions on E**, i.e.**
the space of smooth functions with compact support in E.

## Notation (**Black-Scholes Bilinear Form**).

For any pair pu, vq P DpR`q ˆ DpR`q**, set:**

$$B(u,v)=\int_{\mathbb{R}_{+}}\frac{\sigma^{2}x^{2}}{2}\frac{\partial u}{\partial x}\frac{\partial v}{\partial x}dx+\int_{\mathbb{R}_{+}}\left(\sigma^{2}-r\right)x\frac{\partial u}{\partial x}\,v\,dx+\int_{\mathbb{R}_{+}}r\,u\,v\,dx\,.$$

and note Bpu, uq " Bpuq.

## Property 2.1.

The bilinear form Bp¨, ¨q **is non-symmetric.**
Define its symmetric part, for any pair pu, vq P DpR`q ˆ DpR`q**, through:**

$$\hat{B}(u,v)=\frac{1}{2}\ (B(u,v)+B(v,u))$$ $$=\int_{\mathbb{R}_{+}}\frac{\sigma^{2}x^{2}}{2}\frac{\partial u}{\partial x}\frac{\partial v}{\partial x}dx+\frac{1}{2}\int_{\mathbb{R}_{+}}\left(\sigma^{2}-r\right)\,x\,\left(\frac{\partial u}{\partial x}v+u\,\frac{\partial v}{\partial x}\right)\,dx+\int_{\mathbb{R}_{+}}\,r\,u\,v\,dx$$ $$=\frac{\sigma^{2}}{2}\int_{\mathbb{R}_{+}}x^{2}\,\frac{\partial u}{\partial x}\frac{\partial v}{\partial x}\,dx+\frac{3r-\sigma^{2}}{2}\int_{\mathbb{R}_{+}}\,u\,v\,dx$$

Notations. Set

$$V=\left\{v\in L^{2}(\mathbb{R}_{+})\quad,\quad x\,\frac{\partial v}{\partial x}\in L^{2}(\mathbb{R}_{+})\right\}\quad,\quad W=\left\{v\in L^{2}(\mathbb{R}_{+})\quad,\quad x^{2}\,\frac{\partial^{2}v}{\partial x^{2}}\in L^{2}(\mathbb{R}_{+})\right\}\,.$$

## Property 2.2.

The space

$$V=\left\{v\,\in\,L^{2}(\mathbb{R}_{+})\quad,\quad x\,\frac{\partial v}{\partial x}\,\in\,L^{2}(\mathbb{R}_{+})\right\}$$  Let $\mathcal{L}$ be a $\mathcal{L}$-valued function of $\mathcal{L}$. 

endowed with the inner product

$$\left.\left(u,v\right)\mapsto\langle u,v\rangle_{V}=\langle u,v\rangle_{L^{2}(\mathbb{R}_{+})}+\left\langle x\frac{d u}{d x},x\,\frac{d v}{d x}\right\rangle_{L^{2}(\mathbb{R}_{+})}\right..$$

is a Hilbert space.

## Definition 2.2 (**Black-Scholes Weak Formula**).

```
The Black-Scholes variational formula reads: find u P Cpr0, Ts;L
                                                                2
                                                                 
                                                                 pR`qq X L
                                                                            2
                                                                            
                                                                             pp0, Tq; V q such that
Btu P L
      2
       
       pp0, Tq; V
                ‹q, satisfying:

```

$$\begin{array}{r l r l}{{\left\{\begin{array}{l l}{B(u,v)}&{={\frac{d}{d t}}\int_{\mathbb{R}_{+}}u(t,x)\,v(x)\,d x}&{{},}&{\forall v\in{\mathcal{D}}(\mathbb{R}_{+})}\\ {u(T,x)}&{=h(x)}\end{array}\right.}}\end{array}\right.}$$

where V
‹**is the dual space of** V .

## Lemma 2.3 (**Black-Scholes Operator**).

There exists a unique bounded linear operator BS : V Ñ V
1**, which will be called Black-Scholes**
operator, such that:

$$\forall\,(u,v)\,\in\,V^{2}:\quad B(u,v)=\langle{\mathcal{B S}}(u),v\rangle_{L^{2}(\mathbb{R}_{+})}\,\,.$$
$$\mathbf{\partial}(\mathbf{x}),v\rangle_{L^{2}(\mathbb{R}_{+})}\mathbf{\partial}(\mathbf{x})$$

## Definition 2.3.

Recall that the first derivative is always bounded in the Hilbert-Sobolev space H1pR`q**, and that**
the second derivative is always bounded in the Hilbert-Sobolev space H2pR`q.

The Black-Scholes operator is given, for any v in W**, by**

$${\mathcal{B S}}(v)=-{\frac{x^{2}\sigma^{2}}{2}}{\frac{\hat{c}^{2}v}{\hat{c}x^{2}}}-r\,x\,{\frac{\hat{c}v}{\hat{c}x}}+r\,v\,.$$

Lemma 2.4.

The set

$$W=\left\{v\in V\quad,\quad x^{2}\,\frac{\partial^{2}v}{\partial x^{2}}\,\in\,L^{2}(\mathbb{R}_{+})\right\}$$

$$i s\ d e n s e\ i n\ V.$$

4

## Lemma 2.5 (**Black-Scholes Weak Solution**).

```
For h in L
         2
          
          pR`q, the Black-Scholes problem has a unique weak solution.

```

## 2.2 An Interpretation Of The Generalized Measure Black-Scholes Model

The generalized measure Black-Scholes equation, for a probability measure µ**, can be written, by**
choosing v " u**, as**

$${\frac{\partial}{\partial t}}\mathbb{E}\left(|u|^{2}\right)={\frac{2}{\mathbb{M}}}\,B\left(u\right)$$

where M " M ´ L, while E p.q is the expected value and Bp¨, ¨q **denotes the involved Black-Scholes**
bilinear form. This equation can be understood in the following way: the expected value depreciation of u 2
(and, hence, of u, since it is positive) is proportional to the Black-Scholes energy Bpuq**. This**
implies a law given by the classical Black-Scholes theory which holds on average **and another induced**
by investors' perception of reality and reflected by µ.

A direct implication of this vision is a local dependence of the option price dynamics on the probability measure µ, which can be interpreted as azn confidencezuncertainty **measure.**

## 3 Non-Symmetric Dirichlet Forms And Generalized Measure Blackscholes Operators

Given two strictly positive numbers L ă M, if one replaces R` with M " rL, Ms **(where** M "
sL, Mr) in the generalized measure Black-Scholes model, it does not **result in a dramatic effect on the**
mathematical or economical foundations of the model from the following two points of view:

1. Financial stability: One can suppose, in short run**, boundedness of the underlying financial**
instrument price.

2. Numerical analysis: **It is well known that infinite boundaries are replaced with finite ones for**
numerical simulations (See [KN01] for error estimates).
In section 5.3, a tolerance level associated with the choice of the bounds L and M **is calculated.**

## Notations.

Let's introduce the following two spaces:

$$\begin{array}{r c l}{{}}&{{}}&{{V_{\mathcal M}=\left\{v\,\in\,L^{2}(\mathcal M)\quad,\quad x\,\frac{\partial v}{\partial x}\,\in\,L^{2}(\mathcal M)\right\}\quad,}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{L_{\mu}^{2}(\mathcal M)=\left\{v\quad,\quad\int_{L}^{M}v^{2}\,d\mu<\infty\right\}\quad.}}\end{array}$$

The dual space of VM **will be denoted by** V
‹M **and the closure of** DpMq in VM by V0,M.

## Proposition 3.1.

```
The space DpMq is dense in L
                            2
                             
                            µpMq.

```

As in [HLN06], the fundamental conditions under which the solution exist are obtained thanks to the following assumptions:

## Assumptions 3.2.

For any u in DpMq**, there exists a positive constant** C0:

$$\left|u\right|_{L^{2}_{\sigma}(\mathcal{M})}\leq C_{0}\left|x\,\frac{\widehat{\partial}u}{\widehat{\partial}x}\right|_{L^{2}(\mathcal{M})}\,,$$ (Continuous injection condition) (1) $$\sigma^{2}<4r\,.$$ (Coercivity condition) (2)

## Proposition 3.3.

```
   Under the first condition in assumption 3.2, there exists a unique L
                                                                        2
                                                                        
                                                                        µpMq-representative u˜ of each
equivalence class of functions u in VM such that the above condition holds. There also exists a DpMq
sequence punqnPN which converges towards u˜ both in VM and in L
                                                                  2
                                                                   
                                                                  µpMq, since DpMq is dense in VM
and L
      2
      
      µpMq [Kil94].

```

Consider the bilinear form Bp¨, ¨q with domain dom pBq on the Hilbert space VM**. We introduce**
the bilinear form:

$$B^{\star}(\cdot,\cdot)=B(\cdot,\cdot)+\langle\cdot,\cdot\rangle_{L_{\mu}^{2}({\mathcal{M}})}$$
and the symmetric one:
$$\tilde{B}^{\star}(\cdot,\cdot)=\tilde{B}(\cdot,\cdot)+\langle\cdot,\cdot\rangle_{L_{\mu}^{2}(\mathcal{M})}\ .$$

We refer to [MR92] for further details on the theory of non-symmetric Dirichlet forms.

## Definition 3.1 (**Symmetric Closed Form**).

A pair pB, dom pBqq is a symmetric closed form (on H) if dom pBq **is a dense linear subspace**
of H and B : dom pBq ˆ dom pBq Ñ R **is a positive definite bilinear which is symmetric and closed**
on H (i.e., dom pBq **is complete with respect to the norm** B‹p¨, ¨q 1 2 ).

## Definition 3.2 (**Sector Condition**).

Let us denote by B a bilinear form on the Hilbert space H, and by dom pBq **its domain. The**
pair pB, dom pBqq **is said to satisfy:**

 $\circ$ Dirichlet f$\circ$
@ pu, vq P dom pBq ˆ dom pBq : |B
‹pu, v**q| ĺ** K
aB‹pu, uq B‹pv, vq¨ (3)
ii. The strong sector condition if there exists K ą 0 **such that**

$$\left({\mathcal{3}}\right)$$

@ pu, vq P dom pBq ˆ dom pBq : |Bpu, v**q| ĺ** K
aBpu, uq Bpv, vq ¨
Remark 3.1.

A coercive continuous bilinear form satisfies both conditions.

## Definition 3.3 (**Coercive Closed Form**).

A pair pB, dom pBqq will be called a coercive closed form (on H) if dom pBq is a dense linear subspace of H and B : dom pBq ˆ dom pBq Ñ R **is a bilinear form such that the following two conditions**
hold:
i. Its symmetric part pB, ˜ dom pBqq **is a symmetric closed form on** H.

ii. pB, dom pBqq satisfies the weak sector condition inequality i**. given in (3).**

## Definition 3.4 (**Symmetric Vs Non-Symmetric Dirichlet Form**).

```
   A coercive closed form pB, dom pBqq on L
                                            2
                                             
                                            µpMq, for a given measure µ, will be called a Dirichlet
form if, for any u in dom pBq, one has:

```

u˜ P dom pBq and "Bpu ` u, u ˜ ´ u˜q ě 0
$$\left\{\begin{array}{l l l}{{B(u+\tilde{u},u-\tilde{u})}}&{{\geqslant}}&{{0}}\\ {{B(u-\tilde{u},u+\tilde{u})}}&{{\geqslant}}&{{0}}\end{array}\right.$$
where u˜ " maxp0, minpu, 1qq. If pB, dom pBqq **is in addition symmetric, this is equivalent to:**
$$\begin{array}{l l}{{\geqslant}}&{{0}}\\ {{\geqslant}}&{{0}}\end{array}$$

Bpu, ˜ u˜q ĺ Bpu, uq ¨
B will be called a **symmetric Dirichlet form**.

## Theorem 3.4. **[Mr92]**

Let us denote by pB, dom pBqq a coercive closed form on H, and J **a continuous linear functional**
on dom pBq. Then, there exists a unique u P dom pBq **such that**
@ v P dom pBq : B
‹pu, vq " Jpvq ¨

## Definition 3.5 (**Non-Symmetric Dirichlet Forms**).

A coercive closed form on H, pB, dom pBqq, is said to be a non-symmetric Dirichlet form (on H), if there exists a one-to-one correspondence with a pair of bounded linear operators pL,L˜q:
@ pu, vq P dom pLq ˆ dom pLq : Bpu, vq " p´Lu, v**q " p**u, ´Lv˜ q where dom pLq is the domain of L. Also, dom pLq **is a dense subset of dom** pBq.

The operator L (respectively L˜**) is the generator of a strongly continuous contraction semi-group** pTtqtą0
(respectively pT˜qtą0).

The following result follows from [AP05].

## Proposition 3.5 (**Poincaré Inequality** ).

The space DpMq is dense in VM, and, for any v P DpMq**, the following inequality is satisfied:**

$$\|v\|_{L^{2}({\mathcal{M}})}\leq2\,\left\|x\,{\frac{d v}{d x}}\right\|_{L^{2}({\mathcal{M}})}$$
This inequality induces a second norm on VM, given, for any v in VM**, by:**
$$|v|_{V_{\mathcal{M}}}=\left\|x\frac{d v}{d x}\right\|_{L^{2}(\mathcal{M})}.$$

Proposition 3.6. **(Continuity and Gårding Inequality)**
The bilinear form Bp¨, ¨q is continuous on VM**, and satisfies the Gårding inequality:**

$$\forall\,u\in V_{\mathcal{M}}:\quad B(u)\geqslant\frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}^{2}-\lambda\parallel u\parallel_{L^{2}(\mathcal{M})}^{2}$$  _where $\lambda=\frac{\left(\sigma^{2}-3r\right)}{2}$. Moreover, $B(\cdot,\cdot)$ is coercive under the second assumption 3.2._

Proof.

For any pair pu, vq P DpMq ˆ DpMq**, by using the Poincaré inequality, we obtain that**

$$|B(u,v)|=\left|\int_{L}^{M}\frac{\sigma^{2}x^{2}}{2}\frac{\partial u}{\partial x}\frac{\partial v}{\partial x}dx+\int_{L}^{M}\left(\sigma^{2}-r\right)x\frac{\partial u}{\partial x}v\,dx+\int_{L}^{M}r\,u\,v\,dx\right|$$ $$\leq\frac{\sigma^{2}}{2}|u|_{V_{M}}|v|_{V_{M}}+\left(\sigma^{2}-r\right)|u|_{V_{M}}\parallel v\parallel_{L^{2}(\mathcal{M})}+r\parallel u\parallel_{L^{2}(\mathcal{M})}\parallel v\parallel_{L^{2}(\mathcal{M})}$$ $$\leq C_{1}\parallel u|_{V_{M}}|v|_{V_{M}}$$

where $C_{1}=2r+\frac{5\sigma^{2}}{2}$. For the coercivity, we use again Poincare inequality:

$$B(u)=\frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}^{2}+\int_{L}^{\mathcal{M}}\left(\sigma^{2}-r\right)x\frac{\partial u}{\partial x}\,u\,dx+r\parallel u\parallel_{L^{2}(\mathcal{M})}^{2}$$ $$=\frac{\sigma^{2}}{2}|u|_{V_{\mathcal{M}}}^{2}-\frac{\left(\sigma^{2}-3r\right)}{2}\parallel u\parallel_{L^{2}(\mathcal{M})}^{2}$$ $$\geq C_{2}\,|u|_{V_{\mathcal{M}}}^{2}$$

$$\mathrm{where}\ C_{2}=6r-\frac{3\sigma^{2}}{2}.$$

$${\mathrm{ntative~of~}}u,{\mathrm{along~with~the~closed~set:}}$$
$${\mathcal N}=\left\{v\in V_{{\mathcal M}}\,:\,\|v\|_{L_{\mu}^{2}({\mathcal M})}=0\right\}\,.$$
$$i i.\;\;\left(\tilde{B}^{\star},V_{\mathcal{M}}\right)\;i s\;a\;H i l b e r t\;s p a c e.$$

- Under the continuous injection condition (1) in assumption 3.2, the induced norm B˜‹p¨, ¨q 1 2 is equivalent to the norm | ¨ |VM. Hence, pB‹, dompBqq **is complete.**

## Definition 3.6. Theorem 3.7. **The Black-Scholes Non-Symmetric Dirichlet Form**

```
We introduce the mapping ι : VM Ñ L
                                   2
                                    
                                   µpMq by

```

$$\begin{array}{l}{\square}\end{array}$$

ιpuq " u¯

```
where u¯ is the unique L
                    2
                     
                    µpMq-representative of u, along with the closed set:

```

Under the assumption 3.2:

```
i. dompBq " VM is dense in L
                           2
                            
                           µpMq.

```

iiii. pB, dompBqq **is a (non-symmetric) Dirichlet form.**
Proof.

```
- Let us consider a sequence punqnPN of DpMq, which converges towards u in L
                                                                             2
                                                                              
                                                                             µpMq.

```

We then consider two sequences, panqnPN P N N**, and** pbnqnPN P VM
N
**such that, for any natural**
integer n, un " an ` bn ¨

```
Then, the sequence pbnqnPN converges to u in L
                                            2
                                             
                                            µpMq.

```

$$0\leq C_{2}\,|u^{2}-\tilde{u}^{2}|_{V_{M}}^{2}\leq B(u\pm\tilde{u},u\mp\tilde{u})\,.$$
$$\boxed{\mathrm{~L~}}$$

## Theorem 3.8 (**Generalized Measure Black-Scholes Operator**).

Under the assumption 3.2, there exists a bounded linear operators BSµ, that we will call **generalized**
measure Black-Scholes operator, such that, for any pair pu, vq P dompBSµq ˆ dompBq:
Bpu, vq " xBSµpuq, vyL2µpMq

 *Moreover, we will say that $u\in\textit{dom}(\mathcal{BS}_\mu)$ and $\mathcal{BS}_\mu(u)=f$ if and only if*  . 
$$B(u,v)=\int_{\mathcal M}f\,v\,d\mu\quad,\quad\forall v\in V_{0,\mathcal M}$$

Remark 3.2.

The generalized measure Black-Scholes operator is bounded from VM to V
‹M **since,** @v P V0,M

$$\begin{array}{c}{{\left|\langle\mathcal{B S}_{\mu}(u),v\rangle_{L_{\mu}^{2}(\mathcal{M})}\right|=|B(u,v)|}}\\ {{\qquad\qquad\leq C_{1}\,|u|_{V_{\mathcal{M}}}|v|_{V_{\mathcal{M}}}}}\end{array}$$

by continuity of Bp¨, ¨q.

## Notations (**Sobolev Spaces**).

Given a continuous subset E of R, k P N, and p ě 1**, we recall that the classical Sobolev spaces**
on E are

$$W_{p}^{k}\left(E\right)=\left\{f\,\in\,L^{p}\left(E\right)\,,\,\forall\,j\leq k\,:\,f^{\left(j\right)}\,\in\,L^{p}\left(E\right)\right\}\,,$$
$$\operatorname{and}$$
$H^{k}\left(E\right)=W_{2}^{k}\left(E\right)=\left\{f\,\in\,L^{2}\left(E\right)\,,\,\forall\,j\leq k\,:\,f^{\left(j\right)}\,\in\,L^{2}\left(E\right)\right\}\,.$

The subspace $H^k_0$ of functions which vanish on the boundary $\partial E$ is 

$$H_{0}^{k}\left(E\right)=\left\{f\,\in\,L^{2}\left(E\right)\,,\,f_{|\partial E}=0\,\mathrm{and}\,\,\forall\,j\leq k\,:\,f^{\left(j\right)}\,\in\,L^{2}\left(E\right)\right\}\,.$$

It directly comes form the abstract theory of partial differential equations [Zei90], [Wlo87], [LM68]
that: