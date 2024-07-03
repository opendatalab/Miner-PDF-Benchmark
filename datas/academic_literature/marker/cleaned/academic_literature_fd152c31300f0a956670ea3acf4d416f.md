# The Projective Linear Supergroup And The Susy-Preserving Automorphisms Of P 1∣1

R. Fioresi†**, S. D. Kwok**⋆
† **Dipartimento di Matematica, Universit`a di Bologna**
Piazza di Porta S. Donato, 5. 40126 Bologna. Italy.

e-mail: rita.fioresi@UniBo.it
⋆ **Mathematics Research Unit, University of Luxembourg**
6, Rue Richard Coudenhove-Kalergi, L-1359, Luxembourg e-mail: stephen.kwok@uni.lu

## Abstract

The purpose of this paper is to describe the projective linear supergroup, its relation with the automorphisms of the projective superspace and to determine the supergroup of SUSY preserving **automorphisms of** P
1∣1.

## 1 Introduction

The works of Manin [13, 14] and more recently of Witten et al. [16, 4] have drawn attention to projective supergeometry and more specifically to SUSY curves and their moduli superspaces.

In this paper we study the automorphisms of the projective superspace Pm∣n and its SUSY-preserving subsupergroup. We start by defining the projective linear supergroup PGLm∣n**, using the functor of points formalism, and**
then we show that this supergroup functor is indeed representable, that is, it is the functor of points of a superscheme. We achieve this by realizing PGLm∣n as a closed subsupergroup scheme of GLm2+n2∣2mn**, mimicking the**
ordinary procedure.

In relating this supergroup scheme to the automorphism supergroup of Pm∣n **we encounter a difficulty, not present in the ordinary setting, namely**
the fact that the Picard group of the projective superspace is not known in general and involves some difficulties. This is a consequence of the fact that the supergroup of automorphism of the projective superspace is **larger than**
PGLm∣n for n > 1. Neverthless, going to the special case of n = **1, we are**
able to give quite explicitly the projective linear supergroup and to prove it coincides with the automorphisms of the projective superspace.

The question of singling out the SUSY-preserving automorphisms inside this supergroup was already settled over the complex field by Manin [13] and Witten [16], we extend their considerations to an arbitrary algebraically closed field k**, char**(k) ≠ **2, and provide some extra details of their proofs.**
The organization of this paper is as follows. In Sec. 2 we start by reviewing some generally known facts on the projective superspace and its functor of points to establish our notation. We then discuss line bundles and projective morphisms, proving, in Prop. 2.3, that the Picard group of Pm∣1is Z.

To our knowledge this result is new and gives insight into projective supergeometry. In Sec. 3 we define the projective linear supergroup in terms of functor of points and we prove its representability by realizing it as a **closed**
subsuperscheme of the general linear supergroup. Then, in Sec. **4 we prove** that the projective linear supergroup is the supergroup of automorphisms of the projective superspace in the case of one odd dimension. Though the approach in both Sec. 3 and 4 resembles closely the ordinary one, the results are novel in the supergeometric context. In Sec. 5, we use the machinery developed previously to prove that the subsupergroup of Aut(P
1∣1) **of SUSY**
preserving automorphisms of P1∣1 consists precisely of the irreducible component (SpO2∣1)
0 of the 2∣1-symplecticorthogonal supergroup SpO2∣1**containing**
the identity. This section is a generalization of the claims made by Manin in [13] regarding complex supergeometry and provides proofs for such claims for a generic algebraically closed field.

Acknowledgements. **We are indebted to Prof. D. Gaitsgory for clarifying to us the structure of line bundles over** P
n A
in the ordinary setting. We also thank Prof. L. Migliorini for helpful discussions. We are also grateful to the anonymous Referee for his/her suggestions and remarks on the paper.

## 2 The Projective Superspace P M∣N

In this section we want to recall different, but equivalent definitions **of projective superspace and we describe the line bundles on it. For all of our notation**
and main definitions of supergeometry, we refer the reader to [14, **3, 1].**
Let k **be our ground ring.**
We recall that, by definition, the functor of points of a superscheme X =
(∣X∣,OX) **is the functor:**

$${\mathrm{ssschemes}})^{o}\longrightarrow{\mathrm{(sets)}}$$

X ∶ (**sschemes**)
o Ð→ (sets), X(S) = Hom(sschemes)(S, X), X(φ)(f) = f - φ where (sschemes) **denotes the category of superschemes (it is customary to**
use the same letter for X **and its functor of points). Equivalently (see [1] Ch.**
10), we can view the functor of points of X as: X ∶ (salg) Ð→ (**sets**):

$$\mathbf{s})(S,X)$$
$$X(\phi)(f)=f\circ$$
$$X(R)=\operatorname{Hom}_{(\mathrm{sechemes})}(\underline{{{\mathrm{Spec}}}}\ R,X),\quad X(\phi)(f)=f\circ\underline{{{\mathrm{Spec}}}}\,(\phi)$$

where (salg) denotes the category of superalgebras (over k**), (we shall use**
the same letter also for this functor). In fact the functor of points of a superscheme is determined by its behaviour on the affine superscheme subcategory, which in turn is equivalent to the category of superalgebras (see [1] **Ch. 10,**
Theorem 10.2.5). If X = SpecO(X), that is X **is affine, we have that**

## X(R) = Hom(Sschemes)(Spec **R, X**) = Hom(**Salg**)(O(X), R)

where O(X) denotes the superalgebra of global sections of the sheaf of superalgebras OX . We say that X(R) are the R-points **of the superscheme**
X.

The algebraic superscheme Pm∣n **is defined as the patching of the** m + 1 affine superspaces Ui = SpecO(Ui)**, with** O(Ui) = **Spec** k[x i 0
, . . . ,̂x i i
, **. . .** ,
x im, ξi1
, . . . , ξin] **through the change of charts:**

$$\begin{array}{r c l}{{\phi_{i j}:}}&{{{\mathcal{O}}(U_{j})[(x_{i}^{j})^{-1}]}}&{{\mapsto}}&{{{\mathcal{O}}(U_{i})[(x_{j}^{i})^{-1}]}}\\ {{}}&{{}}&{{x_{k}^{j}}}&{{\mapsto}}&{{x_{k}^{i}/x_{j}^{i}}}\\ {{}}&{{}}&{{x_{i}^{j}}}&{{\mapsto}}&{{1/x_{j}^{i}}}\\ {{}}&{{}}&{{\xi_{k}^{j}}}&{{\mapsto}}&{{\xi_{k}^{i}/x_{j}^{i}}}\end{array}\qquad(1)$$

(as usual ̂x i i **means that we are omitting the indeterminate** x i i
). Notice that O(Uj)[(x j i)
−1] **is the superalgebra representing the open subscheme** Uj ∩ Ui of Uj (and similarly for O(Ui)[(x i j)
−1]).

Proposition 2.1. The R-points of Pm∣n, R ∈ (salg) **are given equivalently**
by:
1.Pm∣n(R) = {α ∶ Rm+1∣n Ð→ L,**R-linear, surjective**}/ ∼,
Pm∣n(ψ) ∶ Rm+1∣n ⊗R T Ð→ L ⊗R T
where L is locally free of rank 1∣0, ψ ∶ R Ð→ T and α ∶ Rm+1∣n Ð→
L ∼ α′∶ Rm+1∣n Ð→ L′if and only if ker(α) = ker(α′) **(or equivalently,**
α ∼ α
′if they differ by an automorphism of L **by multiplication of an**
element in R×).

2.Pm∣n(R) = {α ∶ L ↪ Rm+1∣n **R-linear, injective**},

$$\mathbb{P}^{m|n}(\psi):L\otimes_{R}T\longrightarrow R^{m+1|n}\otimes_{R}T$$
$\star\;\mathbb{R}$). 
where L **is locally free of rank** 1∣0.

Let O
m+1∣n S= OS ⊗km+1∣n. The S-points of Pm∣n, S ∈ (sschemes) **are given**
equivalently by:
(a) Pm∣n(S) = {α ∶ Om+1∣n S Ð→ L, **surjective**}/ ∼, Pm∣n(ψ) ∶ (ψ∗OS)m+1∣n Ð→
ψ∗(L) where ψ ∶ T Ð→ S, L is a line bundle on S (of rank 1∣0**) and**
α ∶ Om+1∣n S Ð→ L ∼ α′∶ Om+1∣n S Ð→ L′∶ if and only if ker(α) = ker(α′)
(or equivalently, α ∼ α′**if they differ by an automorphism of** L by multiplication of an element in O×
S
).

(b) Pm∣n(S) = {α ∶ L ↪ O
m+1∣n S}, Pm∣n(ψ) ∶ ψ∗L Ð→ (ψ∗OS)m+1∣n Proof. **The proof relative to (1) and (a) works as in the ordinary setting and**
it is detailed in [1] Ch. 10. The equivalence with (2) and (b) is immediate.

The equivalence (1) and (2) is essentially the same as in the ordinary setting (see [5] Ch. III, Sec. 2 Prop. III-40, Cor. III-42).

For every A ∈ (salg), let (**salg**)A
denote the category of superalgebras over A**. We will need to consider also** P
m∣n A**that is the projective superspace**
over a base A ∈ (salg)**. This means that we are considering the superscheme**
obtained by patching the affine superspaces Ui = A[x i j
, ξik], i, j = 0**, . . . ,m**,
j ≠ i, k = 1, . . . , n **as above. For example, in the Case (2) of Prop. 2.1 each**
of the T-points, T ∈ (**salg**)A
, is identified with a morphisms α ∶ L Ð→ T m+1∣n of A-modules, where L and T m+1∣n are T-modules which become A**-modules**
via the map φ ∶ A Ð→ T:

P

m∣n
A(T) = Hom(**sschemes**)A
(**Spec** T,P
$$\{T,\mathbb{P}_{A}^{m+1|n}\}=\{\alpha:L\hookrightarrow T^{m+1|n}\}$$
m+1∣n} (2)
Notice that the functor of points of P
m∣n Ais defined on the category of Asuperalgebras or equivalently on the category of A**-superschemes (that is**
superschemes equipped with a morphism to the superscheme Spec A and morphisms compatible with it).

We leave to the reader the generalization of the other cases of Prop. 2.1 since it is straightforward.

We end this section with some observations on line bundles and morphisms on P
m∣n A**. We start with a result completely similar to the ordinary**
counterpart, that we leave to the reader as a simple exercise (see **also [1] Ch.** 9).

Proposition 2.2. **We have a bijective correspondence between the following:**
1. The set of equivalence classes of m+n+2-tuples (L, s0, . . . , sm, σ1**, . . . , σ**n),
where L **is a line bundle on** P
m∣n A**globally generated by the global sections**
s0, . . . , sm, σ1, . . . , σn of L, under the relation (L, s0, . . . sm, σ1, . . . σn) ∼
(**L, s**′0
, . . . s′m, σ′1
, . . . σ′n) **if and only if there exists some** c ∈ O(P
m∣n A)
∗ 0 such that s
′ i
= csi, σ′
i
= cσi**for all** i.

2. The set of A**-morphisms** P
m∣n A → P
m∣n A.

In the ordinary setting we have that a line bundle on P
m A
is of the form O(n)⊗L, where L is a line bundle on Spec A**. This non trivial fact is still true**
in supergeometry for P
m∣1 A**, and it will turn out to be crucial in our treatment.**
Proposition 2.3. **Every line bundle on** P
m∣1 A**is isomorphic to** O(n) ⊗ L,
where L is a line bundle on **Spec** A.

Proof. **A line bundle on** P
m∣1 A**is determined once we know its transition functions, say** gij ∈ OP

m∣1 A
(Ui ∪ Uj)
∗
0
, which are even. We then need to prove that any such set of transition functions is equivalent, up to a coboundary, to a set of transition functions for a line bundle of the form O(n)⊗L, for L **a line**
bundle on Spec A**. In other words we need to show**

```
hi∣Ui∩Uj
     gij h
        −1
        j∣Ui∩Uj = (x
                  i
                  j)
                   n, hi ∈ OP
                              
                              m∣1
                              A
                                (Ui)
                                   ∗
                                   0

```

$=\;\frac{p\sin[A]}{A}$ . 

Notice that

$${\mathcal{O}}_{\mathbb{P}_{A}^{m11}}(U_{p})^{*}\,=\,(A[x_{k}^{p},\xi^{p}])_{0}^{*}\,=\,(A[\xi^{p}][x_{k}^{p}])_{0}^{*},\qquad p=i,j.$$

Since φij(ξ j) =
ξ i x i j
, φij(x j i) = 1/x i j and φij(x j k) =
x i k x i j
(φij **being the change of**
chart as in (1)), we can view the restrictions of the hp's (p = i, j**) to** Ui ∩ Uj, through this identification, as both belonging to (A[ξ i][x i j
, (x i j)
−1])∗
0
. We now apply the classical result and obtain h
′p∈ (A[ξ i][x i j
, (x i j)
−1])∗
0 such that

$$h_{i}^{\prime}g_{i j}(h_{j}^{\prime})^{-1}=(x_{j}^{i})^{n}.$$
$\square$
The h
′p**'s thus obtained are not yet the sections we want; since the odd dimension is one by hypothesis, the most general possible form for** h
′
j is

$$h_{j}^{\prime}=a_{0}+\alpha_{0}\xi^{i}+\sum_{K}a_{K}x_{K}^{i}(x_{j}^{i})^{-|K|}+\sum_{L}\alpha_{L}x_{L}^{i}(x_{j}^{i})^{-|L|}\xi^{i}+\sum_{k}\beta_{k}(x_{j}^{i})^{-k}\xi^{i}$$

where K and L are multiindices, K = (k1, . . . , kr), kl ≠ j (r ∈ N) and x i K ∶=
x i k1

. . . xikr
(similarly for L).

In order to eliminate the term α0ξ i which is not well defined on Uj**, we**
define:
hi∶= (a0 + α0ξ i)h
′

$$,\qquad h_{j}:=(a_{0}^{-1}-a_{0}^{-2}\alpha_{0}\xi^{i})h_{j}^{\prime}.$$

and this gives the required sections.

Notice that it was absolutely fundamental for our argument that there is only one odd dimension. This calculation will give us key information when we want to determine the automorphism supergroup of the projective linear supergroup.

## 3 The Projective Linear Supergroup

In this section we want to define the supergroup functor of the projective linear supergroup and to show it is representable by producing an embedding of it as a closed subgroup into the general linear supergroup.

Let Mm∣n(R) denote the associative superalgebra of supermatrices of order m∣n by m∣n with entries in a commutative superalgebra R. More intrinsically, Mm∣n(R) = EndR(Rm∣n).

Definition 3.1. The automorphism supergroup of supermatrices is the supergroup functor Aut(Mm∣n) ∶ (salg) Ð→ (**grps**)

$[\operatorname{Aut}(\underline{\operatorname{M}}_{m|n})](R):=\{f:\underline{\operatorname{M}}_{m|n}(R)\to\underline{\operatorname{M}}_{m|n}(R)\,|$  $f$ is an $R$-superalgebra automorphism$\}$.  
In analogy with the ordinary setting we also will call this supergroup functor the projective linear supergroup **and denote it with PGL**(m∣n).

Since Mm∣n(R) is itself a free R-module of rank M∣N**, where** M = m2 +n 2 and N = 2mn, Aut(Mm∣n) is a subfunctor of GLM∣N **in a natural way. We**
want to prove this is the functor of points of a closed subsuperscheme of GLM∣N **. Before proceeding we need a lemma characterizing the morphisms**
of the superalgebra of supermatrices.

Lemma 3.2. 1. An R**-linear parity preserving map** ψ ∶ Mm∣n(R) Ð→
Mm∣n(R) **is a morphism of the superalgebra of supermatrices** Mm∣n(R)
if and only if
(a) ψ(id) = id;
(b) ψ(eij)ψ(ekl) = δkjψ(eil),
where eij **are the elementary matrices in** Mm∣n(R).

2. If R **is a local superalgebra, all of the automorphisms of the superalgebra**
Mm∣n(R) **are of the form:**

$$\mathrm{M}_{m|n}(R)\;\;\longrightarrow\;\;\mathrm{M}_{m|n}(R)$$
$$\begin{array}{r c l}{(T,X)}&{{}\mapsto}&{T X T^{-1}}\end{array}$$

for a suitable T ∈ GLm∣n(R).

3. Aut(Mm∣n) is a closed subsuperscheme of GLM∣N = Spec k[x**ij,kl**][d
−1 1
, d−1 2],
M = m2 + n 2 and N = 2mn**, defined by the equations:**

$$\sum_{k}x_{i j,k k}=\delta_{i j},\qquad\quad\sum_{s}x_{r s,i j}x_{s t,k l}=\delta_{j k}x_{r t,i l},\qquad\quad(3)$$

where GLM∣N (R) **is identified with the parity preserving automorphisms**
of the free R**-module** Mm∣n(R).

$\cdot1,\;d–1$1. 
Proof. (1). If ψ is an R-superalgebra endomorphism of Mm∣n(R) **then the**
two relations are obviously satisfied and vice-versa.

(2). Now assume ψ is an automorphism of Mm∣n(R), R **local, which satisfies** the relations (a) and (b). We need to find T ∈ GLm∣n(R) **such that** ψ(eij) =
T eijT
−1**. This is an application of super Morita theory (see [12]), however**
we shall recall the main idea to make this proof self-contained. By (a) and
(b) **we have that**
∑ψ(eii) = id, ψ(eii)
2 = ψ(eii), ψ(eii)ψ(ejj) = 0, i ≠ j hence we can write R
m∣n = ⊕ψ(eii)R
m∣n Since by (b) ψ(eji)ψ(eii) = ψ(eji) = ψ(ejj)ψ(eji) **we have that** ψ(eji) ∶
ψ(eii)Rm∣n Ð→ ψ(ejj)Rm∣n (recall that R **is local so projective implies free).**
Hence there exists a basis {ti} of the free module Rm∣n **such that**
ψ(eii)R
m∣n = **span**R{ti}
and ψ(eji)ti = tj. Let T be the matrix whose columns are the ti's, T = ∑ti⊗e
∗
i
,
T
−1 = ∑ei ⊗ t
∗
i
. It is then immediate to verify ψ(eij) = T eijT
−1.

(3). This is immediate from (1).

Let us view the multiplicative algebraic supergroup G
1∣0 m ∶ (**salg**) Ð→
(grps) **as the following subsupergroup of GL**m∣n:

```
G
 
 1∣0
 m (R) = {aI ∣ a ∈ R
          ∗
          0} ⊂ GLm∣n(R).

```

(Here I **denotes the identity matrix).**
We shall not specify the definition on the arrows whenever it is clear, as in this case.

Definition 3.3. We define the supergroup functor: PGL ̂m∣n ∶ (**salg**) Ð→
(**grps**)
PGL ̂m∣n(R) = GLm∣n(R)/G
1∣0 m (R),
and we call its sheafification (as customary) GLm∣n/G1∣0.

We wish to show that GLm∣n/G1∣0**is representable and coincides with the**
projective linear supergroup, that is with the automorphism supergroup of supermatrices.

Definition 3.4. We say that a functor F ∶ (salg) Ð→ (grps) is stalky **if for**
any superalgebra R**, the natural map**

$$\varinjlim_{f\notin{\mathfrak{p}}}F(R_{f})\;\longrightarrow\;F(R_{\mathfrak{p}})$$

is an isomorphism for any prime ideal p ∈ R0.

The next two lemmas are standard and their proof is the same as in the ordinary case, see [15].

Lemma 3.5. GLm∣n/G1∣0 and Aut(Mm∣n) **are stalky.**
Lemma 3.6. Let F,G be stalky Zariski sheaves (salg) → (**grps**), α ∶ F → G a morphism. If αR ∶ F(R) → G(R) **is an isomorphism for all local superrings**
R, then α **is an isomorphism of sheaves.**
Proposition 3.7. The supergroup functor GLm∣n/G1∣0**is representable and**
is realized as the closed subsupergroup Aut(Mm∣n) of GLM∣N for M = m2 +n 2 and N = 2mn.

Proof. **We need to establish an isomorphism of sheaves between GL**m∣n/G1∣0 and a closed subsupergroup of GLM∣N **. We will first give a morphism of**
sheaves and then show it is an isomorphism on local superalgebras; since GLm∣n/G1∣0**is a stalky sheaf, this will be enough. We start by giving a**
morphism of presheaves PGL ̂m∣n and GLM∣N ; since GLM∣N **is a sheaf then** such a morphism will factor through the sheafification of PGL ̂m∣n **thus giving**
us a sheaf morphism.

Consider the action of GLM∣N **on supermatrices M**m∣n
, where M = m2+n 2, N = 2mn:φ ∶ GLm∣n(R) × Mm∣n(R) Ð→ Mm∣n(R)

$$\mathbf{\partial}=\mathbf{\partial}$$
$$\left|n\left(R\right)\right.$$

$$(T,X)$$
$$\begin{array}{r l}{\mapsto{}}&{{}T X T^{-1}}\end{array}$$

(T, X) ↦ **T XT** −1
This clearly factors through G
1∣0
̂ m (R) **hence gives a well defined action** ρ of PGLm∣n and then in turn of GLm∣n/G1∣0**(see comments at the beginning of** the proof). Since X ↦ T XT −1, T ∈ (GLm∣n/G1∣0)(R) **is a parity preserving**
R**-superalgebra morphism, it is immediate to verify we have a morphism of**
sheaves GLm∣n/G
1∣0 → Aut(Mm∣n).

By the first part of Lemma 3.2, Aut(Mm∣n) is represented by the closed subsuperscheme H of GLM∣N = Spec k[x**ij,kl**][d
−1 1
, d−1 2] **defined by the equations:**

$$\sum_{k}x_{i j,k k}=\delta_{i j},\qquad\quad\sum_{s}x_{r s,i j}x_{s t,k l}=\delta_{j k}x_{r t,i l}$$
$$\left({4\atop4}\right)$$
xrs,ijxst,kl = δjkxrt,il (4)
(Here di **denotes as usual the determinants of the diagonal blocks of indeterminates). We want to show that the group homomorphism** (GLm∣n/G1∣0)(R) →
[Aut(Mm∣n)](R) is an isomorphism for R local. ψ ∈ GLM∣N (R) **belongs to**
H(R) if and only its entries ψ(eij)kl **satisfy the above relations (4) (where in**
our convention xij,kl corresponds to ψ(eij)kl**). Hence by Lemma 3.2 we have**
the result for R **local. By Lemmas 3.5 and 3.6, it is true for any superalgebra**
R **and this concludes the proof.**
Remark 3.8. **The projective linear supergroup may also be obtained through**
the Chevalley supergroup recipe as detailed in [6, 7, 8]). It corresponds to the choice of the adjoint action of the Lie superalgebra slm∣n**. In fact one**
may readily check that the Lie superalgebra of PGLm∣n is indeed slm∣n and
(PGLm∣n)0 = PGLm × PGLn × k
×.

## 4 The Automorphisms Of The Projective Superspace

We want to define the automorphism supergroup of the superscheme Pm∣n.

Definition 4.1. We define the supergroup functor of **automorphisms of the**
projective superspace:
Aut(P
m∣n)(A) ∶= AutA(P
m∣n × Spec A) = AutAP
m∣n A, A ∈ (**salg**).

Aut(Pm∣n) **is defined in an obvious way on the morphisms.**
The equality in the definition is straightforward noticing that we can identify the T-points of Pm∣n × Spec A **and of** P
m∣n A. In fact a T**-point of**
Pm∣n × Spec A is a morphism φ ∶ A Ð→ T and a morphism of A**-modules via**
φ, L Ð→ T m∣n**. This is exactly an element of** P
m∣n A(T) **and vice-versa.**
An automorphism ψ ∈ AutAP
m∣n Ais a family of automorphisms ψT for all T ∈ (**salg**)A
, which is functorial in T. ψT ∶ P
m∣n A(T) Ð→ P
m∣n A(T) **must**