# Modular Curves X1(N) **As Moduli Spaces Of Point** Arrangements And Applications

LEV BORISOV, XAVIER ROULLEAU
Abstract. For a complex elliptic curve E and a point p **of order** n on it, the images of the points pk = kp **under the Weierstrass embedding**
of E into CP2**are collinear if and only if the sum of indices is divisible**
by n**. Thus, it provides a realization of a certain matroid. We study**
this matroid in detail and prove that its realization space is isomorphic
(over C) to the modular curve X1(n), provided n ≥ 10**, which also**
provides an integral model of X1(n)**. In the process, we find a connection**
to the classical Ceva and Böröczky examples of special point **and line**
configurations. We also discuss the situation for smaller values of n.

## 1. Introduction

For n > 4 **coprime to the characteristic of the base field, modular curves**
X1(n) **were defined as the compactifications of the moduli spaces of pairs**
(E, t), where t is a point of order n on an elliptic curve E. The first constructions of these curves were obtained over C **by taking the compactification of**
the quotient H/Γ1(n) **of the upper half-plane by the modular group** Γ1(n).

Deligne and Rapoport in [12] constructed these curves as representation of functors, using Deligne-Mumford stacks. Another approach was done by Katz-Mazur in [16] using Drinfeld modules. These two works have been unified by Conrad in [9] using Artin stacks. The main difficulties of the constructions of X1(n) are to find a model over the integers, to have a geometric interpretation of the points at the compactification **(the cusps), and a**
geometric moduli interpretation of their reduction modulo p when p **divides** n.

We propose in this paper to give a geometric construction of the modular curves as (compactifications of) moduli spaces of realizations of certain matroids, i.e. as moduli spaces of line or points arrangements. Here a line (respectively a point) arrangement in the projective plane **is a finite set of** lines (respectively points). Such arrangement is said labeled if there is a set parametrizing its elements.

Let us recall that a matroid T (of rank 3**) is a combinatorial structure**
which formally describes the intersection relations between the elements of a labeled line arrangement, or in the dual setting, T **encodes the alignments**
arXiv:2404.04364v1 [math.AG] 5 Apr 2024 between the points of a labeled point arrangement. The word "formally" here means that that given a matroid such a line (or point) arrangement does not always exist, and a matroid T (of rank 3**) is said realizable over a field** K if there is indeed a labeled line (or point) arrangement over K **which has** the same combinatorial data as T **. There is a well-defined notion of moduli** space of realizations of a matroid, which moduli space is a scheme naturally defined over Z, the realizations over the field K **being obtained by taking**
the fiber over **Spec(**K).

To a pair (E, t) of an elliptic curve and an element t of order n**, let us**
associate the labeled point arrangement

## Pe,T = (Kt)K∈Z/Nz,

where we fix an embedding ι : E ֒→ P
2**sending the group identity to a flex**
point on the image and where we identify a point with its image. Up to projective transformations, PE,t does not depend on the choice of ι**. Three**
distinct points s1 = it, s2 = jt, s3 = kt (i, j, k ∈ Z/nZ) on PE,t **lie on a**
line if and only if s1 + s2 + s3 = 0 on the elliptic curve E**, thus if and**
only if i + j + k = 0. Accordingly, the set of triples {i, j, k} ⊂ Z/nZ **such**
that i + j + k = 0 defines the so-called non-bases of a matroid Tn**, and the** point arrangement PE,t is a realization of Tn. Let R(Tn) **be the moduli**
space of realizations of Tn**: this is the quotient of the space of all realization**
P = (pk)k∈Z/nZ of Tn by the action of the projective transformations γ **such**
that γ.P = (γpk)k∈Z/nZ. We denote the class of P in R(Tn) by [P]**, so that**
[P] = {γ.P | γ ∈ P GL2}**. We obtain:**
Theorem 1. **Suppose that the base field is an algebraically closed field of**
characteristic not dividing n. For n ≥ 7, the map φ : X1(n)◦ → R(Tn),
(E, t) → [PE,t] is birational, where X1(n)◦**is the complement of the cusps in**
X1(n).

For n ≥ 7, there exists a natural compactification R(Tn) of R(Tn) **and the**
map φ **extends to a morphism**
φ : X1(n) → R(Tn).

Let us suppose that the base field is C**, and let**
π : H∗ → X1(n) = H∗/Γ1(n), τ 7→ Γ1(n)τ be the quotient map.

Theorem 2. Let be n ≥ 10. The map φ **is an isomorphism and the curve**
R(Tn) is contained in a projective space P **of dimension** n−3 2. The composite map H∗ → X1(n) → P **is obtained by weight one modular forms for**
the group Γ1(n).

Borisov, Gunnels and Popescu proved in [4], [6] that certain weight 1 Eisenstein series, obtained as log-derivatives of the Jacobi theta function at rational points, generate the ring of modular forms for Γ1(n) in sufficiently high degree and thus provide an embedding X1(n) → P**. When** n ≥ 5 is prime, one can even find explicit relations that cut out X1(p) schemetheoretically in P
p−3 2 **, see [5].**
In [23], Voight and Zureick-Brown study a generalization of Petri's Theorem about the quadratic relations defining the compactification of a curve H/Γ, where H is the upper-half plane and Γ **is a modular group. In our**
situation, for a rank 3 matroid M, the ideal of the moduli space R(M) of realizations of M **is always generated by quadrics or linear forms with integral**
coefficients.

Let us describe the structure of the paper. In Section 2, we recall the basics of line arrangements and the notations of some operators acting on them defined in [19], which will be used later. We also recall the theory of matroids T and their moduli space of realizations R(T )**. We then introduce**
the matroid Tn and the map X1(n)◦ → R(Tn), where X1(n)◦**is the open**
sub-scheme parametrizing pairs (E, t), where E **is an elliptic curve and** t is a n**-torsion point, the complement of the cusps points in** X1(n).

In Section 3, we prove that R(Tn) **is one-dimensional and its generic point**
is the image of the map φ**. In Section 4, we prove several results on modular** forms which are needed in the next section. In particular, we **find explicit**
Eisenstein series for Γ1(n) **which have zeros only at the cusps of** X1(n).

Their ratios could be used to study the cuspidal subgroup of the Jacobian of X1(n) **(the finite subgroup generated by the differences of the cusps).**
Section 5 contains the proof of Theorem 2. Section 6 studies two natural compactifications of R(Tn).

In the ancillary files of the first arXiv version of this paper, **one can find**
a) the Magma algorithms used for computing the moduli space of realizations of a matroid, and the equations of the curves X1(n) for low n**, b) the**
Mathematica computations used in Sections 3, 5 and 6.

Finally let us observe that a similar construction may be obtained for the modular curve X(n)**. Also, using embedding of elliptic curves in** P
k−1 as degree k curves, one may study the modular curves X1(n) **as realization**
spaces of rank k ≥ 4 **matroids. That will be the subject of another paper.**
Acknowledgements. **The authors thank Lukas Kühne for useful discussions on matroids. We used the computer algebra systems OSCAR [11],**
Magma [7] and Mathematica [18]. X.R. acknowledges support from Centre Henri Lebesgue ANR-11-LABX-0020-01.

2. Preliminaries on matroids, operators and cubic curves 2.1. Point and line arrangements. A line arrangement C = ℓ1+**· · ·**+ℓn is the union of a finite number of distinct lines in P
2**. A labeled line arrangement**
C = (ℓ1, . . . , ℓn) **is a line arrangement with a choice of ordering of the lines.**
We denote by D the duality operator which to a line arrangement C associates the set of the annihilators of the lines of C in the dual projective plane Pˇ2. Concretely, we fix coordinates x, y, z and then D(ℓ) = (a : b : c) **for the**
line ℓ : {ax + by + cz = 0}, moreover D(a : b : c) = ℓ**. By duality, one also**
has a natural notion of (labeled) point arrangements.

Recall that for a given line arrangement C in P
2 and m ≥ 2, an m**-point**
of C is a point at which exactly m lines of C meet. For m **a set of integers** m ≥ 2, let us denote by Pm(C) the union of the m-points of C**, over** m ∈ m.

For a given point arrangement P and n ≥ 2, we define Ln(P) **as the union** of the lines that are n-rich, where an n**-rich line is a line containing exactly** n points of P. Of course, Pm(C) and Ln(P) **could be empty. We denote by**
Dn(L) the line arrangement D(Pn(L)) **in the dual plane.**
For n ≥ 2, by abuse of notations, we denote by Ln(P) **the line arrangement**
L{≥n}(P), and use a similar notation Pn(C) or Dn(C) **for a line arrangement**
C.

2.2. Matroids. **Let us recall the following first definitions and results on**
matroids:
A matroid M is a pair M = (E,B), where E **is a finite set of elements**
called atoms and the elements of B are subsets of E, called basis **(plural:**
bases**), subject to the following properties:** - B **is non-empty;**
- if A and B are distinct members of B and a ∈ A \ B**, then there exists** b ∈ B \ A such that (A \ {a}) ∪ {b**} ∈ B**.

The bases have the same order k, called the rank of (E,B)**. An order** k subset of E that is not a basis is called a **non-basis**.

As we will be only concerned with line or point arrangements in P
2**, we**
now suppose that the rank of M is 3. If m is the order of E**, we may identify** E with the set {1**, . . . , m**}.

Matroids originated from the following kind of examples: If C = (ℓ1**, . . . , ℓ**m)
is a labeled line arrangement, the subsets {i, j, k} ⊂ {1, . . . , m} **such that the**
lines ℓi, ℓj , ℓk **meet in three distinct points are the bases of a matroid** M(C)
over the set {1, . . . , m}. We say that M(C) **is the matroid associated to** C.

In the dual setting, if P = (p1, . . . , pm) **is a point arrangement, the order**
3 subsets {i, j, k} ⊂ {1, . . . , m} such that pi, pj , pk **are not collinear are the**
bases of a matroid M(P). One has M(D(P**)) =** M(P).

A realization (over some field, and when that exists) of a matroid M =
(E,B) is a converse operation to the application L → M(L) or P → M(P):
it is the data of a size 3× m matrix with non-zero columns c1, . . . , cm**, which**
are considered up to a multiplication by a scalar (thus as points in the projective plane, which points must be distinct), and such that any order 3 subset {i1, i2, i3} of E is a non-basis if and only if the size 3 **minor** |ci1
, ci2
, ci3 | is zero. Then we denote by ℓi the line with normal vector the point ci**. The**
labeled line arrangement C = (ℓ1, . . . , ℓm) **is such that three lines** ℓi1
, ℓi2
, ℓi3 meet at a common point if and only if {i1, i2, i3} **is a non-basis; it is a**
realization of M(L). Dually, P = (ci)1≤i≤m is a point realization of M(P).

The space of realizations U(M) of a matroid M **is therefore defined as**
follows: For 1 ≤ j ≤ m, let x1,j , x2,j , x3,j **be the coordinates of the** j th **term**
in the product (P
2)
m. Consider the matrix A = (xi,j )1≤i≤3,1≤j≤m**. For a**
set µ = {i, j, k} of three elements in E, let Aµ be the 3 × 3 **sub-matrix of**
A obtained by taking columns i, j, k and let Vµ **be the sub-scheme of** (P
2)
m defined by det(Aµ) = 0**. Consider**
V (M) = ∩µ∈NBVµ, where the product runs over the non-bases of M and W(M) = ∪µ∈BVµ, where the union runs over the bases of M**. The space of realizations** U(M)
of M **is the scheme**
U(M) = V (M) \ W(M).

We observe that this scheme U(M) is naturally defined over Z **as a subscheme of** (P
2Z
)
m.

Suppose that the realization space U/k **is non-empty over some field** k.

For a realization P = (p1, . . . , pm) ∈ U(k) of M and γ ∈ P GL3(k)**, the**
point arrangement (γp1, . . . , γpm) **is another realization. Let us denote by**
[P] the orbit of P under that action of P GL3**. The moduli space** R(M) of realizations of M is the quotient of U by P GL3(k)**; we denote by**
q : U(M) → R(M), P → [P]
the quotient map. Suppose that there exist distinct elements j1**, . . . , j**4 ∈
{1, . . . , m} such that every order 3 subset in j1, . . . , j4 **is a basis of the matroid**
M **(that will always be the case in this paper). Then any class** [C] in R(M)
has a unique representative C such that the points number j1**, . . . , j**4 of P
are the canonical basis
(2.1) (1 : 0 : 0), (0 : 1 : 0), (0 : 0 : 1), **(1 : 1 : 1)**.

That shows that the quotient map has a section

## S = Sj1**,...,J**4 : R(M) → U(M),

sending a class to the unique representative such that the vectors number j1, . . . , j4 are the canonical basis. Then one can identify, although noncanonically, R(M) with its image by s, so that any element of R(M) **is not**
only a class but an actual realization. Let us fix such such a section: then R(M) is the intersection of U(M) **with the scheme defined by the ideal of**
the canonical basis at the points number j1, . . . , j4**. We note that** s(R(M))
then gets a scheme structure, defined over Z**. Let** j′1
, . . . , j′4 ∈ {1**, . . . , m**} be four other elements such that such that every order 3 **subset in** j′1
, . . . , j′4 is a basis of the matroid M. Define s1 = sj1**,...,j**4
, s2 = sj
′

1
,...,j′4
. There exists a unique 3 × 3 matrix P **with coprime coefficients in**
Z[(xi,j )| 1 ≤ i ≤ 3, j ∈ {j
′1, . . . , j′4}]
6 LEV BORISOV, XAVIER ROULLEAU

```
sending the columns cj
                     ′
                     
                     1
                      , . . . , cj
                            ′
                             
                            4
                              to the canonical basis, P defines an isomor-

```

phism between s1(R(M)) and s2(R(M)), thus R(M) **is well-defined over**
Z.

Definition 3. Once a section s : R(M) → U(M) **is fixed, we call the map**
s ◦ q **the period map of** M.

Very often the first four elements of the matroid are such that **every order**
3 subset is a basis of the matroid M**, so that, when speaking of a period**
map, we implicitly refer to the section s **associated to these four elements.** We then moreover identify R(M) **with its image by** s.

2.3. The matroid Tn. For n ≥ 3, let Tn **be the matroid such that the atoms**
of Tn are the elements of Z/nZ **and the non-bases are the order three subsets**
{i, j, k} of Z/nZ **such that**
i + j + k = 0.

The automorphism group of Tn contains (Z/nZ)∗**since the multiplication by**
an element of (Z/nZ)∗ **preserves the set of non-bases.**
2.4. **Cyclic torsion groups on elliptic curves and realizations of** Tn.

Let E be an elliptic curve with neutral element O, and let T **be a cyclic** torsion subgroup of order n. Fix a plane model of E so that O **is a flex** point. For t, t′, t′′, three distinct elements of T, the points t, t′, t′′ **are aligned** if and only if t + t
′ + t
′′ = O.

By taking a generator t ∈ T, one gets a labeling Z/nZ → **T, k** → kt of T.

Proposition 4. The labeled point arrangement P = (kt)k∈Z/nZ **associated**
to (E, t) is a realization of the matroid Tn**. Up to projective automorphism,**
the point arrangement P **is independent of the choice of the plane model of**
E so that O **is a flex point.**
Proof. The first assertion is clear. The second assertion is a direct **consequence of [21, III, Proposition 3.1].** 
As we will see in the next sections, conversely, for n ≥ 7, any realization of Tn **comes from such torsion points on a (possibly singular) cubic**
curve. Moreover we will obtain that, knowing P**, one may recover -up to** isomorphism- the cubic curve and the generator of the torsion group.

Let X1(n)◦ ⊂ X1(n) **be the open subscheme of the modular curve which**
parametrizes pairs (E, t) **of elliptic curves with a torsion point of order** n. Proposition 4 may be rephrased as:
Corollary 5. **There exists a morphism**
φn : X1(n)
◦ → R(Tn)
which to a point (E, t) associates the realization (kt)k∈Z/nZ **up to projective**
automorphism.

The aim of this section is to further study realization spaces of Tn for n ≥ 5**. We will also be interested in their compactifications in** (P
2)
n−4**. For**
simplicity, we will work over the field of complex numbers.

- Case n = 5. We have points p0, . . . , p4 **with the non-bases** {0, 1, 4}, {0, 2, 3}
only. This means that we can make p1, . . . , p4 **to be canonical basis (2.1),**
which then forces p0 = (0, 1, 1)**, so the realization scheme is a point and** φ5 is constant.

Remark 3.1. **It is possible to modify the matroid slightly to get an open**
subset of the modular curve X1(5). Namely, consider the pair (E, α)**, where**
E is an elliptic curve and α is a 5-torsion element of E**. Up to projective**
transformation, one may suppose that E = Eθ **is the elliptic curve**
Eθ : y 2 **+ (1** − θ)xy − θy = y 3 − θx2, (θ ∈ P
1**generic**)
and α = αθ = (0 : 0 : 1); Eθ **is the universal elliptic curve with a point**
of 5-torsion, see e.g. [1]. Let us associate to (Eθ, α) the labeled line arrangement C = Cθ which is the union of the 5 **tangent lines to the points**
in T = (kα)k∈Z/5Z and the two lines in L2(T) **which are not the tangent**
lines, where L2(T) **is the union of the lines that contain at least two points**
of T **(see Section 2.1). Let** T′
5 be the matroid with 7 **atoms defined by the**
non-bases
{1, 6, 7}, {2, 3, 7}, {2, 4, 6}, {3, 5, 6}, {4, 5, 7}.

The realization space R(T′
5
) **is smooth, 1-dimensional; the seven lines associated to a point in** R(T′
5
) **have duals the canonical basis of** P
2 and
(θ **+ 1 : 1 : 1** − θ 2),(θ + 1 : 1 : θ + 1),(0 : 1 : θ **+ 1)**,
for θ ∈ P
1, t /∈ {0, ±1}.

The line arrangement Cθ **is a realization of** T′
5 and a direct computation shows that the rational map (Eθ, αθ) → Cθ from X1(5) ≃ P
1to R(T′
5
) has degree one.

- Case n = 6. The matroid T6 **has non-bases** {0, 1, 5}, {0, 2, 4}, {1, 2, 3}
and {3, 4, 5}. We can put the points p0, p1, p3, p4 **in the standard form (2.1),**
which forces p2 = (0, 1, 1), p5 **= (1**, 1, 0).

So the realization scheme is again a point.

Remark 3.2. As in the n = 5 **case, we can find a matroid description for**
X1(6). The universal elliptic curve over X1(6) ≃ P
1**is given by**
Eθ : y 2 **+ (1** − θ)xy − (θ 2 + θ)y = x 3 − (θ 2 + θ)x 2, θ ∈ P
1**generic**,
(see e.g. [1], [22]). The point α = (0 : 0 : 1) has order 6. For k ∈ Z/6Z**, let us**
denote by p′kα the dual of the line tangent to Eθ at the point kα**; this is a point**
in the dual plane. The line arrangement Cθ = L{2}((p′kα)k∈Z/6Z) (see notations in Section 2.1) is the union of 15 lines. We label these lines from 1 to 15 so that they correspond bijectively with the 15 pairs (0, 1),(0, 2)**, . . . ,**(4, 5):
by that bijection the line corresponding to the pair (i, j) **is the line through**
the points p′iα and p′jα.

Inspired by this, let T′
6 be the matroid with atoms {1, . . . , 15} **and non-bases**
all the order three subsets of the following sets
{1, 12, 13}, {3, 6, 15}, {3, 8, 12}, {5, 8, 10}, {1, 2, 3, 4, 5}, {1, 6, 7, 8, 9},
{2, 6, 10, 11, 12}, {3, 7, 10, 13, 14}, {4, 8, 11, 13, 15}, {5, 9, 12, 14, 15}.

One computes that the moduli space R(T′
6
) of realizations is 1**-dimensional.**
Corresponding to the above description of the non-bases, a realization C **is a** union of 15 lines which has four triple points and six 5**-points; moreover** C
has 33 double points. The six 5**-points of a realization** Cθ in R(T′
6
) are Pθ : (0 : 0 : 1),(0 : 1 : 0),(−1 : 1 : 1),(θ : 0 : 1),(−θ : 1 : 0),(−θ − **1 : 1 : 1)**,
for θ ∈ P
1 **not in the zero loci of the polynomials**
x + 1, x, 2x + 1, x − 1, x2 + x + 1, x2 − x − 1.

The line arrangement L{2}(Pθ) **is the realization** Cθ of T′
6
. Then a direct computation shows that the map
(Eθ, α) → Cθ is a map from X1(6)◦to R(T′
6
) and that this map has degree 1 (here X1(6)◦
is the complement of the cusps). The curve R(T′
6
) **is smooth.**
- Case n = 7. When n ≥ 7, we can take the points p0, . . . , p3 **to be**
the canonical basis. The moduli space R(T7) of realizations of T7 **is one** dimensional and irreducible. The seven points of a realization C of T7 are the four points of the canonical base and the points
(0 : 1 : 1), (1 : 0 : t), (t − 1**, t,** 0),
for t /∈ {0, 1}. The universal elliptic curve with Z/7Z**-torsion is**
Et: y 2 **+ (1 +** t − t 2)yx + (t 2 − t 3)y = x 3 + (t 2 − t 3)x, and α = (0 : 0 : 1) has order 7 **(see e.g. [22]). Using the period map, one**
can check that the map φ : X1(7)◦ → R(T7) **defined by**
(Et, α) → (kα)k∈Z/7Z
has degree 1, where X1(7)◦**is the complement of the cusps.**
- Case n = 8. The non-bases of the matroid T8 are
{0, 1, 7}, {0, 2, 6}, {0, 3, 5}, {1, 2, 5}, {1, 3, 4}, {3, 6, 7}, {4, 5, 7}.

One computes that the moduli space R(T8) is one-dimensional and irreducible; the eight points of a realization P = (pi)i∈Z/8Z of T8 are
(1 : 0 : 0),(0 : 1 : 0),(1 : 1 : 1),**(0 : 0 : 1)**,
(0 : t : −1),(1 : 0 : 1),(1 : t : t),(1 : t : 0)
for t /∈ {0, ±1,∞}. Using the universal elliptic curve with 8**-torsion elements**
(see [1]), one can check that the map (E, α) ∈ X1(8)◦ → (kα)k∈Z/8Z ∈
R(T8) is well-defined and has degree one onto its image, where X1(8)◦**is the**
complement of the cusps.

- Case n = 9. Up to a projective transformation, the 9 **points of a**
realization of T9 are
(1 : 0 : 0),(0 : 1 : 0),(1 : 1 : 1),**(0 : 0 : 1)**,(t : t : t − 1),
(0 : t : t − 1),(1 : 0 : 1),(1 : t : t),(1 : t **: 0)**,
for t /∈ {0, 1, 1±
√−3 2,∞}. As for n = 7, 8**, one may use the universal elliptic**
curve to check that the map φ : X1(9)◦ → R(T9) **has degree** 1.

- Case n ≥ 10. We will now study R(Tn) for n ≥ 10**. Here is an outline**
of our approach.

We begin by defining a sequence (pk)k∈Z **of points in** P
2such that p0, p1, p2 are not on the same line, and for all sets {i, j, k} ⊂ Z **of three distinct integers**
such that i+ j + k = 0, the points pi, pj , pk **are on a line. We focus on which**
conditions that sequence becomes exactly n**-periodic, so that this gives a**
realization of Tn. We prove that the coordinates of the points (pk)k∈Z are parametrized by fractions of some variables s, t**, which are subject to some** relations and inequalities. Using that n ≥ 10**, one shows that there is a**
unique cubic curve E that contains the points (pk)k∈Z**. In case that cubic**
curve is smooth, it proves that the realization (pk)k∈Z/nZ **is the image by** φ of a point of the modular curve, namely the point corresponding to the pair
(E, p1). We then focus to the case when E is singular; then E **is a nodal**
cubic curve and the realization (pk)k∈Z/nZ of Tn **is a cyclic sub-group on the**
smooth part of E**, for the natural group law with neutral element** p0.

From the hypothesis on the sequence (pk)k∈Z**, and up to projective transformation, one can suppose that**
p0 = (1 : 0 : 0), p1 = (0 : 1 : 0), p2 = (0 : 0 : 1), p3 **= (1 : 1 : 1)**.

Let us suppose moreover that the sequence is n**-periodic; it will be convenient**
for us to think of the data of pi as an n-periodic size Z × 3 **matrix with rows**
giving pi, and we will now look at the consequences of the collinearity for pa, pb, pc for a + b + c = 0**. We will denote the three coordinates on** P
2 as
(x1 : x2 : x3).

The line p1p2 = {x1 = 0} contains p−3 = pn−3**, but since no other**
points are on this line, we may assume that pi = (1 : yi,2 : yi,3) **for all**
i 6∈ {−3, 1, 2} mod n. Also note that since p−3 6∈ p0p2 = {x2 = 0}**, we have**
p−3 **= (0 : 1 :** y−3,3).

The realization space of Tn **is given by periodicity and vanishing of the**
minors for rows a, b, c with a + b + c = 0 mod n**, as well as nonvanishing of** the rest of the 3 × 3 **minors. Let us denote the minor of the rows labeled**
a, b, c ∈ Z/nZ by deta,b,c.

10 LEV BORISOV, XAVIER ROULLEAU
The point p−1 lies on the line p0p1 = {x3 = 0}**. On the other hand, it**
does not lie on p0p2 = {x2 = 0}**. Therefore,**
p−1 = (1 : s : 0), s 6= 0.

To be more precise, the vanishing and nonvanishing of the appropriate determinants eliminates the entry y−1,3 and forces y−1,2 6= 0**. Similarly,** p−3 lies on the intersection of the lines p1p2 = {x1 = 0} and p0p3 = {x2 = x3}
so p−3 **= (0 : 1 : 1)**.

The vanishing of det−2,0,2 = −y−2,2 and det−2,−1,3 = s−y−2,2+y−2,3−sy−2,3 yields

$$p_{-2}=(1:0:{\frac{s}{s-1}})$$ so dont $\sim$ 1 is 
where s − 1 is invertible since det−1,2,3 = s − 1 **is nonzero. We then compute**
det−4,1,3 = 1 − y−4,3 and denote t = y−4,2**, so that**
p−4 = (1 : t **: 1)**.

Then det−4,0,4 = y4,2 − ty4,3 = 0 and det−3,−1,4 = −s + y4,2 − y4,3 **allows :us**
to solve for p4 **= (1 :** st t − 1
:s t − 1
)
where we know that t − 1 is invertible because it is equal to det−4,2,3**. We**
can also compute p5 by using det−3,−2,5 = s s−1 + y5,2 − y5,3 and det−4,−1,5 =
−s + y5,2 + sy5,3 − ty5,3**. We get**

$$p_{5}=(1:{\frac{(s(-1+t))}{(s-1)(1+s-t)}}:{\frac{s^{2}}{(s-1)(1+s-t)}})$$
)
where (1 + s − t) is invertible because det−4,−3,4 = −1 − s + t.

We now observe that there is a unique up to scaling cubic curve **that**
passes through 9 points p−3, . . . , p5**. (There was a dimension two space of**
cubics through p−4, . . . , p4**.) We used Mathematica to compute the size** 9 minors of the matrix of the values of the 10 **cubic monomials to see that one** of them equals s 8(1 − t + st)
(−1 + s)
4**(1 +** s − t)
2(−1 + t)
.

We know that 1 − t + st is invertible because det−4,−3,5 =
1−t+st s−1**. This**
implies that the matrix of values of the 10 **cubic monomials at the above** 9 points has rank 9**. Its nullspace is one-dimensional and gives a unique cubic**
through the 9 **points. Explicitly, this cubic is**
E = {Fs,t = 0} = {−s 2x 21x2 + sx1x 22 + stx21x3 + (s 2 − s − t)x1x2x3
+(1 − s)x 22x3 + t(1 − s)x1x 23 + (s − 1)x2x 23 = 0}.

If the cubic E is non-singular (which is generically the case), the n **points**
pk = kp1, k ∈ Z/nZ on E **form a cyclic torsion sub-group (see also Remark**
3.3 below).