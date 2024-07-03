# A Recursion Formula For Mixed Trace Moments Of Isotropic Wishart Matrices And The Gaussian Unitary/Orthogonal Ensembles Ben Deitmar

Department of Mathematical Stochastics, ALU Freiburg Ernst-Zermelo-Str. 1, 79104 Freiburg, Germany E-mail: ben.deitmar@stochastik.uni-freiburg.de

## Abstract

Exact recursion formulas for mixed moments of four fundamental random matrix ensembles are derived. The reason such recursive formulas are possible is closely related to properties of polygon gluings studied **by Harer and Zagier** as well as Akhmedov and Shakirov. The proofs of the formulas are direct and written in such a way that they do not rely on understanding of polygon gluings.

## 1 Introduction

Let X be a (p×n) random matrix with iid standard normal entries and let Y **be a (**p×n) random matrix with iid standard complex normal entries. Further let Z **be an (**n × n)
random hermitian matrix, where the entries (Zi,j )i≤j are independent and Zi,i ∼ N (0, 1)
for all i ≤ n as well as Zi,j = Zj,i ∼ CN (0, 1) for all i < j ≤ n**. Similarly, let** Z˜ be an (n × n) random symmetric matrix, where the entries (Z˜i,j )i≤j **are independent and**
Z˜i,i ∼ N (0, 2) for all i ≤ n as well as Z˜i,j = Z˜j,i ∼ N (0, 1) for all **i < j** ≤ n.

The matrices √
1 n Z and √
1 n Z˜ **are of the Gaussian unitary and Gaussian orthogonal**
ensemble respectively. The matrices 1nXXT and 1n Y Y ∗ **are real and complex isotropic**
Wishart matrices. In this paper we give exact recursive formulas for mixed trace moments of the type

$$E_{X}(l):=\mathbb{E}\bigg[\prod_{k=1}^{K}\mathrm{tr}\left((\mathbf{X}\mathbf{X}^{T})^{l_{k}}\right)\bigg]\ \ ,\ \ E_{Y}(l):=\mathbb{E}\bigg[\prod_{k=1}^{K}\mathrm{tr}\left((\mathbf{Y}\mathbf{Y}^{*})^{l_{k}}\right)\bigg]$$

and

$$E_{Z}(l):=\mathbb{E}\bigg{[}\prod_{k=1}^{K}\operatorname{tr}\left(\boldsymbol{Z}^{l_{k}}\right)\bigg{]}\ \,\ \ E_{\tilde{Z}}(l):=\mathbb{E}\bigg{[}\prod_{k=1}^{K}\operatorname{tr}\left(\tilde{\boldsymbol{Z}}^{l_{k}}\right)\bigg{]}\ \,$$  for arbitrary $p,n,K\in\mathbb{N}$ and _layouts_$l=(l_{1},...,l_{K})\in\mathbb{N}_{0}^{K}$.  
Assuming l1 > **0, the formulas are as follows.**
1) Gaussian unitary ensemble:

$$\mathbb{E}\bigg[\prod_{r=1}^{K}\mathrm{tr}\left(\mathbf{Z}^{l_{r}}\right)\bigg]=\sum_{q=1}^{l_{1}-1}\mathbb{E}\bigg[\mathrm{tr}\left(\mathbf{Z}^{q-1}\right)\mathrm{tr}\left(\mathbf{Z}^{l_{1}-q-1}\right)\prod_{r=2}^{K}\mathrm{tr}\left(\mathbf{Z}^{l_{r}}\right)\bigg]$$ $$+\sum_{k=2}^{K}l_{k}\mathbb{E}\bigg[\mathrm{tr}\left(\mathbf{Z}^{l_{1}+l_{k}-2}\right)\prod_{\begin{subarray}{c}r=1\\ r\neq k\end{subarray}}^{K}\mathrm{tr}\left(\mathbf{Z}^{l_{r}}\right)\bigg]$$

For a complete formulation and proof see Theorem 2.1.

2) Gaussian orthogonal ensemble:

E Y K r=1 tr Z˜lr= (l1 − 1)E tr Z˜l1−2 Y K r=2 tr Z˜lr + l X1−1 q=1 E tr Z˜q−1tr Z˜l1−q−1Y K r=2 tr Z˜lr + 2X K k=2 lkE tr Z˜l1+lk−2 Y K r=1 r6=k tr Z˜lr

For a complete formulation and proof see Theorem 4.1.

3) Complex isotropic Wishart ensemble:

E Y K r=1 tr (Y Y ∗) lr= nE tr (Y Y ∗) l1−1 Y K r=2 tr (Y Y ∗) lr + lX1−1 q=1 E tr (Y Y ∗) qtr (Y Y ∗) l1−q−1 Y K r=2 tr (Y Y ∗) lr + X K k=2 lkE tr (Y Y ∗) l1+lk−1 Y K r=1 r6=k tr (Y Y ∗) lr

For a complete formulation and proof see Theorem 3.1.

4) Real isotropic Wishart ensemble:

E Y K r=1 tr (XXT) lr= (n + l1 − 1)E tr (XXT) l1−1 Y K r=2 tr (XXT) lr + lX1−1 q=1 E tr (XXT) qtr (XXT) l1−q−1 Y K r=2 tr (XXT) lr + 2X K k=2 lkE tr (XXT) l1+lk−1 Y K r=1 r6=k tr (XXT) lr

For a complete formulation and proof see Theorem 3.2.

The recursive formulas are proved in order of increasing difficulty, so Theorem 2.1 proves
(1), Theorem 3.1 proves (3), Theorem 3.2 proves (4) and Theorem 4.1 proves (2). The only random matrix ensembles for which explicit and non-recursive formulas for mixed moments are known are the Haar unitary and the Haar orthogonal ensembles.

Diaconis and Evans found the explicit formulas in [4] under an assumption roughly equivalent to n ≥ l1 + ... + lK**. Achieving non-recursive formulas for the ensembles studied**
here would prove extremely useful in the study of their spectral properties. For example the asymptotic behavior of

$$\mathbb{E}\left[\,\mathrm{tr}\left({\boldsymbol{Z}}^{\lfloor t_{1}n^{\frac{2}{3}}\rfloor}\right)\cdot\cdot\cdot\mathrm{tr}\left({\boldsymbol{Z}}^{\lfloor t_{K}n^{\frac{2}{3}}\rfloor}\right)\right]$$

is known to determine the behavior of the largest eigenvalue of Z **at the Tracy-Widom**
scale, which is why such mixed trace moments were already extensively studied in [10],
[12], [13], [14] and [15]. The strong universality results therein imply that a non-recursive result in any of the four cases studied here would already yield a greater understanding of Tracy-Widom laws in much more general settings. The fact that Akhmedov and Shakirov were able to find a non-recursive formula to a similar, but still different recursion in [1] suggests that non-recursive solutions may be achievable.

Explicit formulas for the (non-mixed) singular trace moments E
-tr Z2m **as well as**
E

-tr (XXT)
m and E
-tr (Y Y ∗)
m **are known thanks to Haarer-Zagier in [6] and**
E. Vassilieva in [16]. The formula in the GUE case is not written explicitly in [6], but following their work we give the formula in (1.2). The formulas for the real and complex Wishart case can be found in Corollaries 1.8 and 1.9 of [16]. For the singular trace moments in the GOE case E
-tr Z˜2m **a five-term recurrence relation is known thanks**
to M. Ledoux in [9]. The recursion from Theorem 2.1 for the GUE is not new, as it also follows from Section 5 in [6] by Harer and Zagier. We however still prove it as a precursor to Theorems 3.1, 3.2 and 4.1. The real Wishart case from Theorem 3.2 was already studied by Pielaszkiewicz, Von Rosen and Singull in [11], though they made a minor error in their formula. To the best of our knowledge the results of Theorems 3.1 and 4.1 for the complex Wishart ensemble and the GOE respectively are entirely new.

## 1.1 Trace Moments And Polygon Gluings

There is a well-known link between trace moments of the GUE and the number of ways to glue to edges of a polygon together to receive an orientable surface of a given genus.

This link was first described by Harer and Zagier in [6] to prove the recursive formula

$$(m+1)\mathbb{E}\big{[}\,\mathrm{tr}(\mathbf{Z}^{2m})\big{]}$$ $$=(4m-2)n\mathbb{E}\big{[}\,\mathrm{tr}(\mathbf{Z}^{2m-2})\big{]}+(m-1)(2m-1)(2m-3)\mathbb{E}\big{[}\,\mathrm{tr}(\mathbf{Z}^{2m-4})\big{]}\,\tag{1.1}$$

which allows for the explicit representation

$$\mathbb{E}\big{[}\,\mathrm{tr}(\mathbf{Z}^{2m})\big{]}=\frac{(2m)!}{m!}\sum_{r=1}^{n\wedge(m+1)}\frac{\binom{n}{r}\binom{m}{r-1}}{2^{m+1-r}}.\tag{1.2}$$

These equalities were first found by Harer and Zagier and later simplified by Haagerup and Thorbjørnsen in [5], but the more readable formulation for (1.1) is from Theorem 1 in [9] by M. Ledoux, where he goes on to find an analogous recursion formula for E

-tr(Z˜2m)
**in the GOE case.**
Akhmedov and Shakirov took this approach further in [1] by considering 'incomplete' gulings of a polygon such that the unglued edges form polygons of given lengths (l1**, ..., l**K ).

They were able to give a recursive formula for the number of such incomplete gluings with a given genus (for a certain definition of genus). Unfortunately, although they were able to derive the explicit expression from their recursive **formula, their results do not**
seem applicable to random matrix theory and their solution to a similar recursion does not seem applicable for solving the recursive formulas derived in this article.

In order to find formulas for mixed trace moments of the GUE for a layout l = (l1**, ..., l**K ),
one instead would need to count the number of ways to glue the edges of multiple polygons Pl1
, ..., PlKsuch that the resulting oriented surface is of a given genus. **Here a**
possible pairing π =
{e 11
, e15
}, {e 12
, e21
}, ...	of edges for the gluing of P8, P5**, ..., P**6:



Euler's characteristic formula guarantees

$$2-2g=V-L/2+K\ ,$$

where g is the genus of the resultant surface and V **is the number of vertices remaining**
in the ribbon graph determined by the pairing. Define VL,K(g**) = 2** − 2g +
L
2 − K and gL,K(V ) = L
4 + 1 −
V +K
2.

Let εg(l1, ..., lK **) denote the number of different gluings/pairings of polygons** Pl1
, ..., PlK
such that the resulting orientable surface is of genus g**, then it is provable by Wick's**
Theorem (aka. Isserlis' Theorem) that

$$E_{Z}(l)=\sum_{g=0}^{\lfloor g_{L,K}(0)\rfloor}n^{V_{L,K}(g)}\varepsilon_{g}(l_{1},...,l_{K})\eqno(1.3)$$
$$,...,l_{K}>0.$$

under the assumption l1**, ..., l**K > 0.

A recursion formula for EZ(l**) can then be found by mapping such polygon gluings onto**
gluings of polygons with two less total edges. If the edge e k q **paired with** e 11 is still part of the same polygon, i.e. k = 1, then we can contract along the connection of the edges before removing both such that we are left with a gluing of polygons Pq−2, Pl1−q, Pl2
, ..., Plk
.

Here a picture of what the above pairing would look like after **removing** e 11 and its paired edge e 15
:



The edges would of course have to be renamed and we have swapped the positions of the first two polygons such that the effects of contracting along the connection {e 11
, e15
}
are more obvious.

Similarly, when the edge e k q **paired with** e 11 is not in the first polygon, i.e. k > 1, contraction along the pairing and removal of the two edges creates one new polygon Pl1+lk−2 **from the two polygons** Pl1 and Plk
. The rest of the pairing remains a valid gluing for the polygons Pl1+lk−2, P2**, ...,** Pblk
, ..., PlK
. Here an example before the contraction and removal:



We have thus far heuristically argued the plausibility of Theorem 2.1.

## 1.2 Definition (Multigraphs By Route)

For a vertex set V = [n] = {1, ..., n} and a give *route* i 1 ∈ [n]
m **we define the directed**
multi-graph Gi 1 = (V, E, f), with edge set E = (e 11
, ..., e1m**) and**
f : E → V × V ; e 1 q 7→ (i 1 q
, i1
(q mod m)+1) .

By construction the route i 1**is an Euler path on** Gi 1 **. Let** A(Gi 1 ) ∈ N
n×n 0**denote the**
adjacency matrix of Gi 1**, that is**
Av,w(Gi 1 **) = \#**{e 1 q ∈ E | f(e 1 q
) = (**v, w**)} .

We can also define the undirected multi-graph G˜i 1 = (V, E, ˜f **) to a given route** i 1 ∈ [n]
m with the same edges, but ignorant of the edges direction. In this case we can define ˜f by
˜f : E → {M ⊂ V | \#M ≤ 2} ; e 1 q 7→ {i 1 q
, i1
(q mod m)+1} .

(If \#f(e 1 q**) = 1, the edge** e 1 q**is a self-loop.) Again** A(G˜i 1 ) ∈ N
n×n 0**denotes the adjacency**
matrix of G˜i 1 **, i.e.**

$$A_{v,w}(\tilde{G}_{i^{1}})=\#\{e_{q}^{1}\in E\mid f(e_{q}^{1})=\{v,w\}\}\ .$$

Note that for this definition of the adjacency matrix self-loops are only counted once.

For a sequence of routes i = (i 1**, ...,** i K ) ∈
K×
k=1
[n]
lk **define the joined adjacency matrices**

$$A(\mathbf{i}):=\sum_{k=1}^{K}A(G_{\mathbf{i}^{k}})\ \ ;\ \ \tilde{A}(\mathbf{i}):=\sum_{k=1}^{K}A(\tilde{G}_{\mathbf{i}^{k}}).\tag{1.4}$$

In Section 3 the vertex set V will be [p + n**], so we must exchange all above occurrences**
of n **with** p + n.

## 2 Gaussian Unitary Ensemble 2.1 Theorem (Recursion For Mixed Trace Moments Of The Gue)

For K ∈ N and any l = (l1**, ..., l**K ) ∈ N
K
0- with even L := l1 + ... + lK **- the following**
recursive properties hold.

a) If l1 = 0, then EZ(l) = nEZ(S0(l**)) for**

$$S_{0}(0,l_{2},...,l_{K}):=(l_{2},...,l_{K})\ .$$
S0(0, l2, ..., lK ) := (l2, ..., lK ) . **(2.1)**
 b) If $ l_1>0$, then? 
$$E_{Z}(l)=\sum_{q=1}^{l_{1}-1}E_{Z}(S_{2,q}(l))+\sum_{k=2}^{K}l_{k}E_{Z}(S_{3,k}(l))\ ,$$
$$(2.1)$$

$$(2.2)$$

where

$$\begin{array}{l}{{S_{2,q}(l):=\left(q-1,l_{1}-q-1,l_{2},...,l_{K}\right)}}\\ {{S_{3,k}(l):=\left(l_{1}+l_{k}-2,l_{2},...,\widehat{l_{k}},...,l_{K}\right)\;.}}\end{array}$$

Since (a) reduces K by one and (b) reduces L = l1 + ... + lK **by two, the starting point**
EZ
((,))= E**[tr(**Z)
0] = n for (K, L) = (1, 0) allows for the calculation of all mixed moments, when L **is even.**
When L **is odd, it is easy to see that the mixed trace moment must be zero.**
Proof. The property (a) holds trivially, since the empty matrix product is here the (n × n)
identity matrix. It remains to prove property (b).

For now assume l1, ..., lK > 0, then expanding the sums in tr(Zli **) yields**

$$E_{Z}(l)=\sum_{\begin{array}{c}{{i^{1}\in[n]^{l}}}\\ {{i^{K}\in[n]^{K}}}\end{array}}\mathbb{E}\left[\prod_{k=1}^{K}Z_{i_{1}^{k},i_{2}^{k}}\cdots Z_{i_{l_{k-1}^{k},i_{l_{k}^{k}}^{k}}}Z_{i_{l_{k}^{k},i_{1}^{k}}^{k}}\right]\,.$$

Extracting the first entries of each i k **and summing over them first gives**

$$E_{Z}(l)=\sum_{\begin{array}{c}{{b_{1},...,b_{K}\in[n]}}\\ {{i\in\atop{k=1}}}\end{array}}\sum_{\begin{array}{c}{{K}}\\ {{i\in\atop{k=1}}}\end{array}}\mathbb{E}\left[\prod_{k=1}^{K}Z_{i_{1}^{k},i_{2}^{k}}\cdots Z_{i_{l_{k-1}^{k}}^{k},i_{l_{k}^{k}}^{k}}\ Z_{i_{l_{k}^{k},i_{1}^{k}}^{k}}\right]\ .$$

For easier notation define

$$\mathbb{I}_{l,b}:=\left\{\dot{\mathbf{\mathit{i}}}=(\dot{\mathbf{\mathit{i}}}^{1},...,\dot{\mathbf{\mathit{i}}}^{K})\in\bigtimes_{k=1}^{K}[n]^{l_{k}}\ |\ \forall k\leq K:\,(l_{k}>0\Rightarrow i_{1}^{k}=b_{k})\right\}\,,$$

then the above formula can be written as

$$E_{Z}(l)=\sum_{b_{1},\ldots,b_{K}\in[n]}\sum_{i\in\mathbb{I}_{l,b}}\mathbb{E}\bigg{[}\prod_{k=1}^{K}Z_{i_{1}^{k},i_{2}^{k}}\cdots Z_{i_{l_{k}-1}^{k},i_{l_{k}}^{k}}\ Z_{i_{l_{k}}^{k},i_{1}^{k}}\bigg{]}.\tag{2.4}$$

The formula now also holds when some li **are zero, since then the summation over the**
corresponding bi brings the needed factors n **= tr(**Z0).

Since complex standard normal random variables satisfy E[XaXb] = 1a=b a**! and real**
standard normal random variables satisfy E[Xa] = 1a even (a − **1)!! (with the convention**
(−**1)!! = 1), the mean in (2.4) has the form**

E  Y K k=1 Zi k 1 ,ik 2 · · · Zi k lk−1 ,ik lk Zi k lk ,ik 1  = 1 A(i) is symmetric & diag. entries even  Y Av,w(i)! Y v∈[n] (Av,v(i) − 1)!!=: W(A(i)) , (2.5) v,w∈[n] v<w

$$(2.5)$$
where $A(\mathbf{i}):=\sum\limits_{k=1}^{K}A(G_{\mathbf{i}^{k}})$. L.  
k **). Let** c := i 1 l1
- here the assumption l1 > **0 is needed - and**
define the symmetric matrix Mb,c := 1i=b,j=c + 1i=c,j=b i,j∈[n]
. **(2.6)**

8 For c 6= b1, the above definition of W(A(i**)) then yields**

$$\begin{array}{l}{{{\mathcal W}(A(\dot{\mathbf{i}}))={\mathcal W}(A(\dot{\mathbf{i}}))-M_{b_{1},c})\,A_{c,b_{1}}(\dot{\mathbf{i}})}}\\ {{={\mathcal W}(A(\dot{\mathbf{i}})-M_{b_{1},c})\bigg(A_{c,b_{1}}(G_{\dot{\mathbf{i}}^{1}})+\sum_{s=2}^{K}A_{c,b_{1}}(G_{\dot{\mathbf{i}}^{s}})\bigg)\ ,}}\end{array}$$

where Ac,b1
(i**) is at least 1, since it counts the number of occurrences of the connection**
(i 1 l1
, i11
) = (c, b1). The fact that W(A) is zero as soon as A **is not symmetric, allows us**
to swap b1 and c **in arbitrary places of the formula, so we may also write**

$${\mathcal W}(A(\dot{\mathbf{i}}))={\mathcal W}(A(\dot{\mathbf{i}})-M_{b_{1},c})\bigg(A_{b_{1},c}(G_{\dot{\mathbf{i}}^{1}})+\sum_{s=2}^{K}A_{b_{1},c}(G_{\dot{\mathbf{i}}^{s}})\bigg)\ .$$

Similarly, when c = b1**, the weight satisfies**

$$\mathcal{W}(A(\mathbf{i}))=\mathcal{W}(A(\mathbf{i}))-M_{b_{1},b_{1}})\left(A_{b_{1},b_{1}}(\mathbf{i})-1\right)$$ $$=\mathcal{W}(A(\mathbf{i})-M_{b_{1},b_{1}})\bigg{(}A_{b_{1},b_{1}}(G_{\mathbf{i}^{1}})-1+\sum_{s=2}^{K}A_{b_{1},b_{1}}(G_{\mathbf{i}^{s}})\bigg{)}$$

and we can use these properties of the weight to decompose equality (2.4) into

=:E1Z
(l)
$$E_{Z}(l)=\overbrace{\sum_{\begin{subarray}{c}b\in[n]^{K}\hat{\mathbf{i}}\in\Pi_{b}\\ c\in[n]\end{subarray}}\sum_{\begin{subarray}{c}i_{1}^{l}=c\\ i_{1}^{l}=c\end{subarray}}\mathcal{W}(A(i)-M_{b_{1},c})(A_{b_{1},c}(G_{i^{1}})-1_{b_{1}=c})}^{\text{``}\Sigma(l)}$$ $$+\sum_{\begin{subarray}{c}b\in[n]^{K}\sum_{\begin{subarray}{c}i\in\Pi_{b}\\ c\in[n]\end{subarray}}\mathcal{W}(A(i)-M_{b_{1},c})\sum_{s=2}^{K}A_{b_{1},c}(G_{i^{s}})\enspace.\tag{2.7}$$
For E1Z
(l**) observe that** Ab1,c(Gi 1 ) counts the number of occurrences of (b1, c**) in** i 1 =
(i 11
, ..., i1 l1
) and, if this number is 1b1=c, such an i **will not contribute to** E1Z
(l**). Define**

$$Q_{b,c}^{1}(i^{1})=\{q<l_{1}\mid i_{q}^{1}=b,\,i_{q+1}^{1}=c\}\ ,$$
q+1 = c} , **(2.8)**
then Ab1,c(Gi 1 ) − 1b1=c = \#Q1 b1,c(i 1**). For each** q ∈ Q1 b1,c(i 1**) we give a unique way of**
splitting up i 1**into two new routes** hi 1iq,1 and hi 1iq,2**. Define**

$$\langle{\dot{\mathbf{i}}}^{1}\rangle_{q,1}:=\left(\underbrace{i_{1}^{1}}_{=b_{1}},...,i_{q-1}^{1}\right)\in[n]^{q-1}\;\;;\;\;\;\langle{\dot{\mathbf{i}}}^{1}\rangle_{q,2}:=(i_{q+2}^{1},...,\underbrace{i_{l_{1}}^{1}}_{=c})\in[n]^{l_{1}-q-1}$$

and observe that when going from the multi-graph Gi 1 to Ghi 1iq,1 ∪ Ghi 1iq,1 **we have**
only lost one edge in each direction (two edges without direction in the case of b1 = c)
between the vertices b1 and c **while all other edges remain. For**
J
1 q
(i**) :=** hi 1iq,1,hi 1iq,2, i 2**, ...,** i K**(2.9)**
it follows that A(J
1 q
(i**)) =** A(i) − Mb1,c .

Since we sum over all choices of c **and all the other elements in** i 1**, which were not**
specified can still be chosen freely, this for E1 l**implies**

E 1Z(l) = X b∈[n]K c∈[n] X X q∈Q1 b1,c (i 1) W(A(J 1 q(i))) i∈Il,b i 1 l1 =c = l X1−1 X X i∈Il,b i 1 l1 =c q∈Q1 b1,c (i 1) W(A(J 1 q (i))) q=1 b∈[n]K c∈[n]
$$=\sum_{q=1}^{l_{1}-1}\sum_{\tilde{b}\in[n]^{\tilde{k}+1}}\sum_{i\in\mathbb{I}_{\mathbb{S}_{2,q}(l),\tilde{b}}}\mathcal{W}(A(i))\,\tag{2.10}$$
where

$$S_{2,q}(l):=\left(q-1,l_{1}-q-1,l_{2},...,l_{K}\right)$$

is defined in analogy to J
1 q
(i**). We have thus shown**

$$E_{Z}^{1}(l)=\sum_{q=1}^{l_{1}-1}E_{Z}(S_{2,q}(l))\ .$$
$$\left({2.11}\right)$$... 
$$(2.12)$$
EZ(S2,q(l)) . **(2.11)**
Next, for E2Z
(l**) observe that** P
K
k=2 Ab1,c(Gi k ) counts the number of occurrences of (b1, c)
in

$$(i_{1}^{2},...,i_{l_{2}}^{2}),\cdot\cdot\cdot\;,(i_{1}^{K},...,i_{l_{K}}^{K})$$

and define the set

$Q_{b,c}^{2}(\mathbf{i}):=\left\{(k,q)\in\{2,...,K\}\times\mathbb{N}\ |\ q\leq l_{k}\ \text{and}\right.$  $$\left.q<l_{k}\Rightarrow(i_{q}^{k}=b\wedge i_{q+1}^{k}=c),\,q=l_{k}\Rightarrow(i_{l_{k}}^{k}=b\wedge i_{1}^{k}=c)\right\}\,.$$  $K$
	. **(2.12)**
Again P
K
k=2 Ab1,c(Gi k **) = \#**Q2 b1,c(i) and this time for each (**k, q**) ∈ Q2 b1,c(i**) we give a unique**
way of joining the routes i 1 and i k**into a new route**

$$\langle i^{1},i^{k}\rangle_{q}:=\left\{\begin{array}{l l}{{\left(\langle\,i_{1}^{1},\cdots,\,i_{l_{1}}^{1}\,,i_{k+2}^{k},...,i_{l_{k}}^{k},\,i_{l_{1}}^{k}\,,...,i_{q-1}^{k}\right)\in[n]^{l_{1}+l_{s}-1}}}&{{,\mathrm{~if~}q<l_{k}}}\\ {{=l_{1}}}&{{=c}}\\ {{\left(\underbrace{i_{1}^{1}}_{=l_{1}},...,\underbrace{i_{l_{1}}^{1}}_{=c},i_{2}^{k},...,i_{k_{s}-1}^{k}\right)\in[n]^{l_{1}+l_{s}-1}}}&{{,\mathrm{~if~}q=l_{k}}}\end{array}\right..$$
