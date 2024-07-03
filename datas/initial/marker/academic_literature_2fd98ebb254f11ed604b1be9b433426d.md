# Stability And Performance Analysis Of Discrete-Time Relu Recurrent Neural Networks

Sahel Vahedi Noori, Bin Hu, Geir Dullerud, and Peter Seiler Abstract**— This paper presents sufficient conditions for the**
stability and ℓ2**-gain performance of recurrent neural networks**
(RNNs) with ReLU activation functions. These conditions are derived by combining Lyapunov/dissipativity theory with Quadratic Constraints (QCs) satisfied by repeated ReLUs. We write a general class of QCs for repeated RELUs using known properties for the scalar ReLU. Our stability and performance condition uses these QCs along with a "lifted" representation for the ReLU RNN. We show that the positive homogeneity property satisfied by a scalar ReLU does not expand the class of QCs for the repeated ReLU. We present examples to demonstrate the stability / performance condition and study the effect of the lifting horizon.

## I. Introduction

This paper considers the analysis of recurrent neural networks (RNNs) with ReLU activation functions. These are modeled by the interconnection of a discrete-time, linear time-invariant (LTI) system in feedback with a repeated ReLU. The goal is to derive sufficient conditions to prove stability and performance (as measured by the induced ℓ2 gain) for this RNN. This work is motivated by the increasing interest in RNNs for inner-loop feedback control. Such RNNs can potentially improve performance over more standard LTI controllers. However, the analysis of closed-loop stability and performance is challenging due to the nonlinear activation functions in the RNN. The sufficient conditions in this paper are one step to address this issue.

Our technical approach combines multiple ingredients in the existing literature. First, we note that the scalar ReLU has slope restricted to [0,1]. Hence the repeated ReLU satisfies a known QC involving doubly hyperdominant matrices [1]–[3]. Second, we present QCs that are specific to repeated ReLUs building on work in [4], [5]. Next, we write the ReLU RNN
using a "lifted" representation over an N-step horizon [6].

This lifting allows us to construct more general QCs that hold for the ReLU across multiple time steps. Finally, we combine Lyapunov and dissipativity theory [7]–[10] with these QCs to obtain sufficient conditions for stability and performance of the lifted ReLU RNN. Stability and performance of the original (unlifted) ReLU RNN follows from this analysis.

This paper adds to the broader literature on integral quadratic constraint (IQC) conditions [11]–[14]. Our stability/performance condition is similar to the discrete-time, IQC formulations in [15]–[22]. The most closely related conditions are in [16], [23], both of which use lifting and static QCs (rather than dynamic IQCs). There is also growing literature on using these techniques to analyze NNs and RNNs [4], [5], [24]–[26]. We specifically build on the results for ReLU RNNs in [4], [5]. In particular, [4] derives QCs for ReLU and uses Lyapunov theory to prove stability for continuous-time ReLU RNNs. We build on this work in discrete-time and also prove ℓ2 bounds. The work in [5] also addresses discrete-time ReLU RNNs, similar to our paper, but uses small-gain arguments. In contrast, we use QCs and Lyapunov/dissipativity theory leading to related, but different conditions.

Our contributions to this existing literature are as follows.

First, we write a general class of QCs for repeated ReLU
using known existing properties. We show that the positive homogeneity property satisfied by scalar ReLUs, i.e.

φ(βv) = βv for all β ≥ 0, does not expand the class of QCs for repeated ReLUs. Second, we use the discrete-time lifting, originally proposed in [6], that maintains the state dimension. This is different from the liftings used previously in [16], [23] for which the lifted state grows with the lifting horizon. Finally, we present examples to illustrate the effects of the ReLU QCs and lifting time horizon. We show that the ReLU QCs can significantly reduce the conservatism as compared to QCs developed for the more general class of slope-restricted nonlinearities (although the performance is problem dependent).

## Ii. Notation

This section briefly reviews basic notation regarding vectors, matrices, and signals. Let R
nand R
n×m denote the sets of real n × 1 vectors and n × m matrices, respectively.

Moreover, R
n ≥0 and R
n×m
≥0denote vectors and matrices of the given dimensions with non-negative entries. Let D
n denote the set of n × n diagonal matrices and D
n ≥0 the subset of diagonal matrices with non-negative entries. Finally, M ∈
R

n×nis a *Metzler matrix* if the off-diagonal entries are nonnegative, i.e. Mi j ≥ 0 for i 6= j. A matrix M ∈ R
n×nis doubly hyperdominant if the off-diagonal elements are non-positive, and both the row sums and column sums are non-negative.

Next, let N denote the set of non-negative integers. Let v : N → R
nand w : N → R
n be real, vector-valued sequences.

Define the inner product hv,wi := ∑
∞
k=0 v(k)
⊤w(k). The set ℓ2 is an inner product space with sequences v that satisfy hv,vi < ∞. The corresponding norm is kvk2 :=phv,vi.

## Iii. Problem Statement

Consider the interconnection shown on the left of Figure 1 with a static nonlinearity Φ wrapped in feedback around the top channels of a nominal system G. This interconnection is denoted as FU(G,Φ). The nominal part G is a discrete-time, linear time-invariant (LTI) system described by the following state-space model:

$$\begin{array}{l}{{x(k+1)=A x(k)+B_{1}\,w(k)+B_{2}\,d(k)}}\\ {{v(k)=C_{1}\,x(k)+D_{11}\,w(k)+D_{12}\,d(k)}}\\ {{e(k)=C_{2}\,x(k)+D_{21}\,w(k)+D_{22}\,d(k),}}\end{array}$$
$$\quad(1)$$

where x ∈ R
nxis the state. The inputs are w ∈ R
nw and d ∈ R
nd while v ∈ R
nv and e ∈ R
ne are outputs. The static nonlinearity Φ : R
nv → R
nv
≥0 maps v to w elementwise by wi = φ(vi) for i = 1,...,nv where φ : R → R≥0 is the ReLU
function. The ReLU, shown on the right of Figure 1, is:

$$\phi(v)=\left\{\begin{array}{l l}{{0}}&{{\mathrm{if~}v<0}}\\ {{v}}&{{\mathrm{if~}v\geq0}}\end{array}\right..$$

We refer to Φ as a repeated ReLU and φ as the scalar ReLU.

The interconnection FU(G,Φ) is known as a linear fractional transformation (LFT) in the robust control literature [27]. The interconnection has its roots in the Lurye decomposition used in the absolute stability problem [10].

![1_image_0.png](1_image_0.png)

Fig. 1: Left: Interconnection FU(G,Φ) of a nominal discretetime LTI system G and repeated ReLU Φ. Right: Graph of scalar ReLU φ.

This feedback interconnection involves an implicit equation if D11 6= 0. Specifically, the second equation in (1)
combined with w(k) = Φ(v(k)) yields:

$$v(k)=C_{1}\,x(k)+D_{11}\,\Phi(v(k))+D_{12}\,d(k).$$

This equation is *well-posed* if there exists a unique solution v(k) for all values of x(k) and d(k). Well-posedness of this equation implies that the dynamic system FU(G,Φ) is wellposed in the following sense: for all initial conditions x(0) ∈
R

nx and inputs d ∈ ℓ2 there exists unique solutions x, v, w and e ∈ ℓ2 to the system FU (G,Φ). There are simple sufficient conditions for well-posedness of (3), e.g. Lemma 1 in [4]
(which relies on results in [28], [29]). Thus, we'll assume well-posed for simplicity in the remainder of the paper.

A well-posed interconnection FU(G,Φ) is *internally stable* if x(k) → 0 from any initial condition x(0) with d(k) = 0 for k ∈ N. In other words, FU(G,Φ) is internally stable if x = 0 is a globally asymptotically stable equilibrium point with no external input. A well-posed interconnection FU (G,Φ)
has finite induced-ℓ2 *gain* if there exists γ < ∞ such that the output e generated by any d ∈ ℓ2 with x(0) = 0 satisfies kek2 ≤ γ kdk2. This bound is denoted as kFU(G,Φ)k2→2 ≤ γ.

The goal of this paper is to derive sufficient conditions, using the properties of the ReLU, that verify FU(G,Φ) is internally stable and has finite induced ℓ2 gain.

## Iv. Main Results

The section presents the main results: sufficient conditions for stability and performance of the ReLU RNNs. These sufficient conditions are based on dissipativity theory and quadratic constraints (QCs) for the repeated ReLU.

A. Quadratic Constraints for Slope-Restricted Functions First, consider a scalar function φ : R → R≥0 that satisfies φ(0) = 0 and has slope restricted to [0,1], i.e.:

$$0\leq{\frac{\phi(v_{2})-\phi(v_{1})}{v_{2}-v_{1}}}\leq1,\,\forall v_{1},v_{2}\in R,v_{1}\neq v_{2}.$$
$$(2)$$

This subsection presents QCs that hold for any activation function φ that satisfies these conditions. This includes, but is not limited to, the ReLU.

The graph of φ is restricted to the [0,1] sector, i.e. its graph lies between lines that pass through the origin with slope 0 and 1. Thus the following QC holds ∀v ∈ R and w = φ(v):

$$w(v-w)\geq0.$$
$$({\mathfrak{H}})$$
* [16] A. A. K.  
w(v−w) ≥ 0. (4)
Moreover, any two points on the graph of φ are connected by a line with slope in [0,1]. Hence the following QC holds for all v1,v2 ∈ R, w1 = φ(v1), and w2 = φ(v2):

$$\left(w_{2}-w_{1}\right)\left(v_{2}-v_{1}-\left(w_{2}-w_{1}\right)\right)\geq0.$$

Next, consider a repeated nonlinearity Φ : R
m → R
m ≥0 that maps v to w elementwise wk = φ(vk) for k = 1,...,m. We can derive a QC for Φ based on scaled combinations of the sector and slope constraints for the data {(vk,wk)}
m k=1
. Specifically, for any non-negative constants λk and γk j:

$\lambda_{k}\,w_{k}(v_{k}-w_{k})\geq0$ for $k=1,\ldots m$  $\gamma_{k_{j}}\left(w_{k}-w_{j}\right)\left(v_{k}-v_{j}-(w_{k}-w_{j})\right)\geq0$. for $k,j=1,\ldots m$.  
$\eqref{eq:walpha}$
Summing over all these constraints gives an inequality of the form w
⊤Q0(v−w) ≥ 0 where

$$(Q_{0})_{kj}=\left\{\begin{array}{cc}\lambda_{k}+\sum_{k\neq j}(\gamma_{kj}+\gamma_{jk})&\mbox{if$k=j$}\\ -(\gamma_{kj}+\gamma_{jk})&\mbox{else}\end{array}\right..\tag{6}$$

Q0 is a symmetric, doubly hyperdominant matrix. Lemma 1, stated next, provides a more general QC for this case in that it allows for Q0 to be non-symmetric.

Lemma 1: Let Φ : R
m → R
m
≥0 be a repeated nonlinearity with Φ(0) = 0 and slope restricted (elementwise) to [0,1]. If Q0 ∈ R
m×m is doubly hyperdominant then the following QC
holds ∀v ∈ R
m and w = Φ(v):

$$\left[\begin{array}{c}v\\ w\end{array}\right]^{\top}\left[\begin{array}{cc}0&Q_{0}^{\top}\\ Q_{0}&-(Q_{0}+Q_{0}^{\top})\end{array}\right]\left[\begin{array}{c}v\\ w\end{array}\right]\geq0.\tag{7}$$

Proof: This follows from the results in Section 3.5 of [2]. Specifically, for any pair v and w = Φ(v), define v˜ := v − w ∈ R
m. Equation 5 implies that {(v˜k,wk)}
m k=1 is similarly ordered data, i.e. ˜vk > v˜jimplies wk ≥ wj.

Moreover, it follows from (4) that the data is unbiased, i.e. wkv˜k ≥ 0 for k = 1,...,m. Theorem 3.8 in [2] implies that if Q0 is doubly hyperdominant then w
⊤Q0v˜ ≥ 0. Thus w
⊤Q0(v−w) + (v−w)
⊤Q
⊤
0 w ≥ 0.

The proof of Theorem 3.8 in [2] relies on a cyclic rearrangement inequality satisfied by similarly ordered, unbiased data. In fact, the doubly hyperdominance condition is the largest class of QCs that holds for slope-restricted functions whose graph passes through the origin. A precise statement of this fact is given in Theorem 1 of [3].1

## B. Quadratic Constraints For Relu

The previous subsection presented QCs for functions with slope restricted to [0,1]. This section derives several additional QCs that are specific to the repeated ReLU. This builds on prior work in [4], [5]. The starting point for these QCs are the following properties for the scalar ReLU that have been used previously in the literature [4], [5], [30], [31]:.

1) *Positivity:* The scalar ReLU is non-negative for all inputs: φ(v) ≥ 0 ∀v ∈ R.

2) *Positive Complement:* The scalar ReLU satisfies φ(v) ≥ v ∀v ∈ R.

3) *Complementarity:* In addition to the [0,1] sector, the ReLU satisfies the stronger complementarity property:
its graph is identically on the line of slope 0 (when v ≤
0) or the line of slope 1 (when v ≥ 0). Thus, φ(v) (v−
φ(v)) = 0 ∀v ∈ R.

4) *Positive Homogeneity:* The scalar ReLU is homogeneous for all non-negative constants: φ(βv) = β φ(v)
∀v ∈ R and ∀β ∈ R≥0.

Properties 1-3 can be combined to construct QCs for the repeated ReLU. Lemmas 2 and 3 below are variations of results in [4].
Lemma 2: Let Φ : R
m → R
m
≥0 be a repeated ReLU. If Q1 ∈
D
m then the following QC holds ∀v ∈ R
m and w = Φ(v):

$$\begin{bmatrix}v\\ w\end{bmatrix}^{\top}\begin{bmatrix}0&Q_{1}\\ Q_{1}&-(Q_{1}+Q_{1}^{\top})\end{bmatrix}\begin{bmatrix}v\\ w\end{bmatrix}=0.\tag{8}$$  _Proof: $Q_{1}$_ is diagonal by assumption so that:
$$\begin{bmatrix}v\\ w\end{bmatrix}^{\top}\begin{bmatrix}0&Q_{1}\\ Q_{1}&-(Q_{1}+Q_{1}^{\top})\end{bmatrix}\begin{bmatrix}v\\ w\end{bmatrix}=\sum_{k=1}^{m}(Q_{1})_{kk}w_{k}(v_{k}-w_{k}).$$  This is equal to zero based on the complementarity property.  
for each {(vk,wk)}
m k=1
. Note that the diagonal entries of Q1 are not necessarily non-negative.

1Theorem 1 in [3] is stated for repeated monotone nonlinearities. A
similar fact holds for nonlinearities with slope restricted to [0,1] by a transformation of the input-output data.

Lemma 3: Let Φ : R
m → R
m
≥0 be a repeated ReLU. If Q2 =
Q
⊤ 2
, Q3 = Q
⊤ 3
, Q4 ∈ R
m×m
≥0then the following QC holds ∀v ∈
R

m and w = Φ(v):

$$\begin{bmatrix}v\\ w\end{bmatrix}^{\top}\begin{bmatrix}Q_{2}&-(Q_{2}+Q_{4}^{\top})\\ -(Q_{2}+Q_{4})&Q_{2}+Q_{3}+Q_{4}+Q_{4}^{\top}\end{bmatrix}\begin{bmatrix}v\\ w\end{bmatrix}\geq0.\tag{9}$$

Proof: The positivity and positive complement properties are linear constraints on {(vk,wk)}
m k=1
. These can be combined to form QCs on pairs of points. The QCs below hold for any non-negative (Q2)k j, (Q3)k j, and (Q4)k j:

$$\begin{array}{l}{{(Q_{2})_{k j}(w_{k}-v_{k})(w_{j}-v_{j})\geq0,}}\\ {{(Q_{3})_{k j}w_{k}w_{j}\geq0,}}\\ {{(Q_{4})_{k j}w_{k}(w_{j}-v_{j})\geq0.}}\end{array}$$
$$\begin{array}{c}{{(10)}}\\ {{(11)}}\\ {{(12)}}\end{array}$$

Equations 10 and 11 are equivalent to (w−v)
⊤Q2(w−v) ≥ 0 and w
⊤Q3w ≥ 0, respectively. These QCs are quadratic forms and hence we can assume Q2 = Q
⊤
2 and Q3 = Q
⊤
3 without loss of generality. Equation 12 is equivalent to w
⊤Q4(w −
v) + (w−v)
⊤Q
⊤
4 w ≥ 0.

The next result combines all the QCs in the Lemmas 13. This is the most general QC based on the [0,1] sector
/ slope restrictions combined with the known properties for scalar ReLU.

Lemma 4: Let Φ : R
m → R
m
≥0 be a repeated ReLU. Let Q2 = Q
⊤
2
, Q3 = Q
⊤
3 ∈ R
m×m
≥0and Q˜ ∈ R
m×m be given with Q˜ a Metzler matrix. Then the following QC holds ∀v ∈ R
m and w = Φ(v):

$$\begin{bmatrix}v\\ w\end{bmatrix}^{\top}\begin{bmatrix}Q_{2}&-Q^{\top}-Q_{2}\\ -Q-Q_{2}&Q_{2}+Q_{3}+Q+Q^{\top}\end{bmatrix}\begin{bmatrix}v\\ w\end{bmatrix}\geq0.\tag{13}$$  _Proof:_ Gather all the QCs given in Lemmas 1-3.  
Define Q˜ = Q4 − Q0 − Q1 where Q0 ∈ R
m×m is doubly hyperdominant, Q1 ∈ D
m and Q4 ∈ R
m×m
≥0. The diagonal entries of Q˜ can be anything while the off-diagonal entries must be non-negative. Hence Q˜ is a Metzler matrix.

Finally, the next lemma exploits the positive homogeneity property of the ReLU. Related results are given in Section 4.3 of [5].

Lemma 5: Let Φ : R
m → R
m
≥0 be a repeated ReLU. Assume Φ satisfies the QC defined by M = M⊤ ∈ R
2m×2m, i.e
∀v ∈ R
m and w = Φ(v):

v w ⊤ M11 M12 M⊤ 12 M22 vw ≥ 0. (14) If Λ ∈ D m ≥0then Φ also satisfies the QC defined by -Λ 0 0 Λ M-Λ 0 0 Λ ∈ R 2m×2m, i.e. ∀v¯ ∈ R m and ¯w = Φ(v¯): v¯ w¯ ⊤ Λ ⊤M11Λ Λ⊤M12Λ (Λ ⊤M12Λ) ⊤ Λ ⊤M22Λ  v¯ w¯ ≥ 0 (15) Proof: Take any ¯v ∈ R m and ¯w = Φ(v¯). Let Λ is a
diagonal matrix with non-negative entries. Apply positive homogeneity of the scalar ReLU, element-wise, to conclude that Λw¯ = Φ(Λv¯). Next, define v = Λv¯ and w = Λw¯ so that w = Φ(v). The QC in (14) holds, by assumption, for (v,w).

Substitute v = Λv¯ and w = Λw¯ to show the QC in (15) also holds for (v¯,w¯).

The positive homogeneity property seems to generalize the class of QCs for repeated ReLU by allowing for an additional scaling Λ ∈ D
m
≥0
. However, this additional freedom does not increase the class of QCs if we use the results of Lemma 4.

Specifically, if Q2,Q3 ∈ R
m×m
≥0then ΛQ2Λ,ΛQ3Λ ∈ R
m×m ≥0 for all Λ ∈ D
m
≥0
. Similarly, if Q˜ ∈ R
m×m is a Metzler matrix then ΛQ˜Λ is also a Metzler matrix for all Λ ∈ D
m
≥0
. Thus positive homogeneity does not provide additional freedom when combined with the most general QC given in Lemma 4, i.e. we get the same class of QCs. However, the positive homogeneity scaling Λ can provide an additional degrees of freedom when combined with more restricted subsets of QCs. For example, suppose we use the restricted class of QCs based on slope restrictions (Lemma 1). In this case, the positive homogeneity property can provide a benefit because if Q0 ∈ R
m×m is doubly hyperdominant and Λ ∈ D
m
≥0 then ΛQ0Λ is not necessarily doubly hyperdominant. In this case, the scaling introduced by positivity homogeneity (Lemma 5)
will generalize beyond the initial (restricted) class of sloperestricted QCs.

## C. Conditions For Stability And Performance

This section presents a sufficient condition for the feedback connection FU (G,Φ) to be stable and have bounded induced ℓ2-gain. The condition uses a lifted plant, defined below, combined with Lyapunov/dissipativity theory and the QCs derived in the previous subsection.

The first step is to create a lifted representation for FU (G,Φ) where G is the LTI system (1) and Φ is the repeated ReLU. Define the stacked vectors for both the input/output signals of G as:

$$V_{N}(k)=\left[v^{\top}(k)\quad v^{\top}(k-1)\quad\cdots\quad v^{\top}(k-N+1)\right]^{\top},$$ $$W_{N}(k)=\left[w^{\top}(k)\quad w^{\top}(k-1)\quad\cdots\quad w^{\top}(k-N+1)\right]^{\top},$$ $$D_{N}(k)=\left[d^{\top}(k)\quad d^{\top}(k-1)\quad\cdots\quad d^{\top}(k-N+1)\right]^{\top},$$ $$E_{N}(k)=\left[e^{\top}(k)\quad d^{\top}(k-1)\quad\cdots\quad d^{\top}(k-N+1)\right]^{\top}.$$  The next turn is to be the $\alpha$-independent, and the $\alpha$-independent, respectively.  
These vectors stack the signals over an N step horizon from k −N +1 to k.

The nominal plant dynamics can be lifted [6] to evolve the state N steps from x(k − N + 1) to x(k + 1). The lifted nominal plant, denoted GN, has the form:

$$x(k+1)=A^{N}x(k-N+1)+B_{1,N}W_{N}(k)+B_{2,N}D_{N}(k)$$ $$V_{N}(k)=C_{1,N}x(k-N+1)+D_{11,N}W_{N}(k)+D_{12,N}D_{N}(k)$$ $$E_{N}(k)=C_{2,N}x(k-N+1)+D_{21,N}W_{N}(k)+D_{22,N}D_{N}(k).\tag{16}$$

The state matrices (B1,N, B2,N, etc.) can be constructed for the specified horizon N from the state-matrices of the original nominal plant. The lifted plant given here has the same state dimension as the original plant but the input/output dimensions are stacked, e.g. WN ∈ R
nwN and B1,N ∈ R
nx×nwN.

A related, but different, lifting is used in [16], [17] where the state-dimension grows with the horizon N.

The repeated ReLU can also be lifted. Define ΦN : R
nvN →
R

nvN by applying the scalar ReLU elementwise to the input.

In summary, the lifted system FU(GN,ΦN) maps DN(k)
to EN(k) based on the interconnection of GN in (16) and WN(k) = ΦN(VN(k)).

We next state the stability and performance condition for the lifted system. Define a linear matrix inequality (LMI)
with the lifted system of GN:

LMI(P,M, γ 2) :=  (A N) ⊤P(A N)−P (A N) ⊤PB1,N (A N) ⊤PB2,N B ⊤ 1,NP(A N) B ⊤ 1,NPB1,N B ⊤ 1,NPB2,N B ⊤ 2,NP(A N) B ⊤ 2,NPB1,N B ⊤ 2,NPB2,N −γ 2I     ⊤  ⊤  C ⊤ 2,N D ⊤ 21,N D ⊤ 22,N   C ⊤ 2,N D ⊤ 21,N D ⊤ 22,N   C ⊤ 1,N0 D ⊤ 11,NI D ⊤ 12,N0   C ⊤ 1,N0 D ⊤ 11,NI D ⊤ 12,N0  +    +  M  (17)
The next theorem provides an stability and performance condition for the ReLU RNN formulated with this LMI. The proof uses a QC for the lifted ReLU and a standard Lyapunov / dissipation argument.

Theorem 1: Consider the ReLU RNN FU (G,Φ) with the LTI system G defined in (1). Assume this interconnection is well-posed. Let GN and ΦN : R
m → R
m be the lifted system and lifted ReLU for some N ∈ N with dimension m := nvN.

Let Q2 = Q
⊤ 2
, Q3 = Q
⊤
3 ∈ R
m×m
≥0and Q˜ ∈ R
m×m be given with Q˜ a Metzler matrix. Define M = M⊤ ∈ R
2m×2m as follows:

$$M:=\left[\begin{array}{cc}Q_{2}&-\tilde{Q}^{\top}-Q_{2}\\ -\tilde{Q}-Q_{2}&Q_{2}+Q_{3}+\tilde{Q}+\tilde{Q}^{\top}\end{array}\right],\tag{18}$$

Then the lifted ReLU ΦN satisfies the QC defined by M, i.e.

[
vw]
⊤ M [
vw] ∀v ∈ R
m and w = ΦN(v).

Moreover, if there exists a positive semidefinite matrix P =
P
⊤ ∈ R
nx×nx and scalar γ ≥ 0 such that LMI(P,M, γ 2) < 0, then the ReLU RNN FU(G,Φ) is internally stable and has kFU(G,Φ)k2→2 < γ.

Proof: This theorem is a standard dissipation result [7]–
[10], [20]. A proof is given for completeness.

It follows directly from Lemma 4 that ΦN satisfies the QC
defined by M. We'll first use this QC and the LMI condition to show the lifted system FU (GN,ΦN) is stable and with ℓ2 gain bounded by γ.

The LMI is strictly feasible by assumption and hence it remains feasible under small perturbations: LMI(P +
εI,M, γ 2) +εI < 0 for some sufficiently small ε > 0. Moreover, well-posedness of FU (GN,ΦN) follows from the assumption that FU (G,Φ) is well-posed. Hence the lifted system FU (GN,ΦN) has a unique causal solution (x,WN,VN,EN)
for any given initial condition xN(0) and input DN ∈ ℓ ndN
2.

Define a storage function by V (x):= x
⊤(P+εI)x. Left and right multiply the perturbed LMI by [x(k)
⊤,WN(k)
⊤,DN(k)
⊤]
and its transpose. The result, applying the lifted dynamics (16), gives the following condition:

$$V\left(x(k+1)\right)-V\left(x(k)\right)-\gamma^{2}D_{N}(k)^{\top}D_{N}(k)+E_{N}(k)^{\top}E_{N}(k)$$ $$+\begin{bmatrix}V_{N}(k)\\ W_{N}(k)\end{bmatrix}^{\top}M\begin{bmatrix}V_{N}(k)\\ W_{N}(k)\end{bmatrix}+\varepsilon\begin{bmatrix}x(k)\\ W_{N}(k)\\ D_{N}(k)\end{bmatrix}^{\top}\begin{bmatrix}x(k)\\ W_{N}(k)\\ D_{N}(k)\end{bmatrix}\leq0$$

The term involving M is non-negative as the lifted ReLU
satisfies the QC defined by M. Thus the dissipation inequality simplifies to:

$$\begin{array}{l}V\left(x(k+1)\right)-V\left(x(k)\right)+E_{N}(k)^{\top}E_{N}(k)\\ \leq(\gamma^{2}-\varepsilon)D_{N}(k)^{\top}D_{N}(k)-\varepsilon x(k)^{\top}x(k)\end{array}\tag{19}$$

Internal stability and the ℓ2 gain bound for the lifted system FU (GN,ΦN) follow from this inequality. Specifically, if DN(k) = 0 for all k then (19) simplifies to the following Lyapunov inequality:

$$V(x(k+1))-V(x(k))\leq-\varepsilon x(k)^{\top}x(k)$$

Hence V is a Lyapunov function and the lifted system is globally asymptotically stable (Theorem 27 in Section 5.9 of [32]).

Next, assume x(0) = 0 and DN ∈ ℓ2. Summing (19) from k = 0 to k = T −1 and using V(x(0)) = 0 yields:

$$V\left(x(T)\right)+\sum_{k=0}^{T-1}E_{N}(k)^{\top}E_{N}(k)\leq\sum_{k=0}^{T-1}(\gamma^{2}-\varepsilon)D_{N}(k)^{\top}D_{N}(k)$$

Note that V(x(T)) ≥ 0 because P is positive semidefinite. Moreover, the right side is upper bounded by (γ 2 −ε)kDNk 2 2 for all T ∈ N. This implies that EN ∈ℓ2 and kENk2 < γkDNk2.

In summary, the lifted system FU(GN,ΦN) is internally stable and satisfies kFU((GN,ΦN)k2→2 < γ. The lifting is an isomorphism and preserves signal norms: kdk2 = kDNk2 and kek2 = kENk2. It follows that the original system also satisfies the gain bound kFU((G,Φ)k2→2 < γ. Moreover, the state of the lifted system corresponds to the evolving the state of the original system forward by N steps. Simple bounding arguments can be used to show that if the lifted state converges to the origin then so does the original state. Hence internal stability of the lifted system also implies internal stability of the original system.

## V. Numerical Examples A. Stability Analysis

A variety of examples are given in [18] to study the use of discrete-time Zames-Falb multipliers for analyzing stability of Lurye systems. We will use Example 6 in Table 1 of [18] as a benchmark to illustrate our ReLU RNN stability and performance condition.

Consider the Lurye system shown in Figure 2 where φ :
R → R is a nonlinear function, α is a non-negative scaling, and G11(z) = 2z+0.92 z 2−0.5z is a discrete-time system. The results in [18] focus on the class of nonlinearities that have slope restricted to [0,1]. The goal is to find the stability margin, i.e. the largest value of α ≥ 0 for which this Lurye system is stable for all nonlinearities in this class. Their reported results are shown in Table I. The Circle and Tsypkin criteria both can be used to prove stability for α up to 0.6510. The Zames-Falb condition in [18] proves stability for α up to 1.087.2In fact, the Zames-Falb condition achieves the largest possible stability margin for the class of [0,1] slope restricted nonlinearities. This follows because the Lurye system is unstable for φ(v) = v and α = 1.087. The destabilizing value α = 1.087 is called the Nyquist gain.

![4_image_0.png](4_image_0.png)

![4_image_1.png](4_image_1.png)

Next, we used the condition in Theorem 1 to analyze the stability margin for the case when φ is the scalar ReLU. The Lurye system in Figure 2 is equivalent to the LFT
representation FU (G,φ) in Figure 1 using:

$$G(z)=\begin{bmatrix}-G_{11}(z)\,\alpha&1\\ 1&0\end{bmatrix}\tag{20}$$  The Lurve system with ReLU is stable for a given value 
of α if the LMI(P,M, γ 2) < 0, defined in (17), is feasible for some γ < ∞. We solved for the largest feasible value of α using bisection using the ReLU QCs.3 The feasibility at each bisection step is a semidefinite program and was solved using CVX [33] as a front-end and SDPT3 [34], [35] as the solver. The bisection is initialized with α = 0 and α¯ = 200.

The bisection is terminated when α¯ −α ≤ 10−3(1+α¯).

The top row of Table II shows the results as a function of the lifting horizon. For comparison, we also computed the stability margin using QCs defined by M =
0 Q⊤
0 Q0 −(Q0+Q⊤
0
)

where Q0 is a doubly hyperdominant matrix. These results are shown in the second row of Table II. Computational times are also given for each bisection to the stopping tolerance.

The doubly hyperdominant QC is the strongest possible constraint for [0,1] slope restricted nonlinearities as discussed in Section IV-A. This test corresponds to the circle criterion when N = 1. The stability margin improves with the lifting horizon, getting to a maximum value of 0.8911, 2The results depend on the number of terms included in the Zames-Falb finite impulse response filter. This is the best (largest) reported value.

3Note that γ appears in the (3,3) block of the LMI in (17). A Schur complement argument can be used to conclude that feasibility for some γ < ∞ is equivalent to feasibility of the upper left two blocks. Hence our numerical implementation used bisection with only these upper left two blocks of the LMI.

lift size N 1 2 5 8 12 ReLU: max α 0.6516 0.6516 4.2999 33.472 181.543 DH: max α 0.6516 0.6516 0.8636 0.8820 0.8911 ReLU Comp. (s) 4.73 4.87 5.15 5.10 5.32 DH Comp. (s) 3.80 3.83 4.00 4.05 4.33 TABLE II: *Stability margins (top):* Results using the doubly hyperdominant (DH) and ReLU QCs as a function of lifting horizon N. The ReLU QC exploits specific ReLU properties to significantly improve the stability margin. *Computational* times (bottom): given for each stability margin calculation.

but stays below the Nyquist value as expected. The ZamesFalb condition, given in Table I, provides the larger stability margin of 1.0870 than our lifted Lyapunov condition with the doubly hyperdominance QC for N = 12.

More interestingly, the ReLU QC provides a stability margin that far exceeds the Nyquist value of 1.0870 as the lifting horizon N increases, giving a maximum value of 181.543. This is possible because the ReLU QC exploits specific properties of the repeated ReLU that appears in the lifted system. To empirically verify this result, we simulated the the Lurye system with φ as the scalar ReLU, α = 100, and 20 initial conditions for the state drawn from a 2 × 1 Gaussian distribution with standard deviation of 10. All simulations of the Lurye system with the ReLU converged back to the origin. This provides some independent validation of our stability margin results for the ReLU Lurye system.

## B. Gain Example

In this section, we used the condition in Theorem 1 to analyze the induced ℓ2-norm for a ReLU RNN FU(G,Φ).

The nominal part G is a discrete-time, linear time-invariant
(LTI) system given in (1) with the following state matrices:

A = "0.84 −0.17 0.10 −0.04 0.17 0.80 −0.11 −0.04 0.05 −0.11 0.90 −0.08 −0.04 0.18 0.01 0.74 # B1 = "−0.08 −0.18 −0.11 0.11 −0.01 −0.05 −0.04 0.03 #, B2 = "−0.04 0.11 0.14 −0.06 0.03 −0.02 0.02 −0.03 0.01 0.04 −0.08 0.20 # C1 =-−0.35 −0.40 −1.04 1.36 0.90 0.55 1.13 −0.46  C2 = 0.79 −0.62 −1.87 −0.09 −0.67 −1.05 1.80 −0.06 2.25 −1.08 −0.36 1.08  The nonlinearity Φ has nv = 2 inputs and nw = 2 outputs.
The dimensions of the disturbance and error channels are
nd = 3 and ne = 3, respectively. The "best" gain bound γ
for a specific lifting horizon N is obtained by minimizing γ
2
subject to the LMI constraint LMI(P,M, γ
2) < 0, as defined
in (17). There are additional (linear) constraints on the QC
matrices in M, e.g. Q˜ is a Metzler matrix. This minimization
is a semidefinite program and was solved using CVX [33] as a front-end and SDPT3 [34], [35] as the solver. The top row of Table III shows the results as a function of the lifting
horizon. For comparison, we also computed a bound on the
ℓ2 gain using QCs defined by M =
where Q0
$\mathbf{y}$$M=\left|\begin{array}{cc}0&\mathbf{Q}_{0}^{\top}\\ \mathbf{Q}_{0}&-(\mathbf{Q}_{0}+\mathbf{Q}_{0}^{\top})\end{array}\right.$  **matrix.** These results a 
is a doubly hyperdominant matrix. These results are shown in the second row of Table III. The doubly hyperdominant QC is the strongest possible constraint for [0,1] slope restricted nonlinearities as discussed in Section IV-A. The results gain bound obtained using the ReLU QC is better (smaller) as it exploits specific properties of the ReLU. Moreover, both results improve with the lifting horizon as the QCs can exploit couplings between the input/output data for the repeated nonlinearity. Computational times are also given to run each minimization. There is a mild growth in computation time with increasing horizon N for this problem.

lift size N 1 2 3 4 5 6 ReLU: gain bound 7.556 5.530 3.932 3.466 3.247 3.128 DH: gain bound 34.379 13.450 7.992 5.844 4.811 4.263 ReLU Comp. (s) 0.82 0.44 0.48 0.52 0.91 1.25 DH Comp. (s) 0.28 0.28 0.29 0.36 0.47 0.61 TABLE III: *Gain (top):* ℓ2-gain upper-bounds given using ReLU and the doubly hyperdominant (DH) QCs as a function of lifting horizon N. The ReLU QC exploits specific ReLU
properties to provide a significantly less conservative upperbound on the gain. *Computational times (bottom):* provided for each upper-bound solution.

## Vi. Conclusions

This paper presents sufficient conditions for the stability and ℓ2-gain performance of RNNs with ReLU activation functions. These conditions are derived by combining Lyapunov/dissipativity theory with Quadratic Constraints (QCs)
satisfied by repeated ReLUs. We use a "lifted" representation for the ReLU RNN to derive our stability and performance condition. Future work will consider the computational cost of this condition and scalability to larger RNNs. We will also study the theoretical properties as the lifting horizon N tends to infinity.

VII. ACKNOWLEDGMENTS
The authors acknowledge AFOSR Grant \#FA9550-23-10732 for funding of this work.

REFERENCES
[1] J. Willems and R. Brockett, "Some new rearrangement inequalities having application in stability analysis," *IEEE Transactions on Automatic Control*, vol. 13, no. 5, pp. 539–549, October 1968.

[2] J. C. Willems, *The analysis of feedback systems*, ser. Research monographs. Cambridge, Mass.: M.I.T. Press, 1971, no. 62.

[3] V. Kulkarni and M. Safonov, "All multipliers for repeated monotone nonlinearities," *IEEE Transactions on Automatic Control*, vol. 47, no. 7, pp. 1209–1212, 2002.

[4] C. R. Richardson, M. C. Turner, and S. R. Gunn, "Strengthened circle and Popov criteria for the stability analysis of feedback systems with ReLU neural networks," *IEEE Control Systems Letters*, 2023.

[5] Y. Ebihara, H. Waki, V. Magron, N. H. A. Mai, D. Peaucelle, and S. Tarbouriech, "ℓ2 induced norm analysis of discrete-time LTI systems for nonnegative input signals and its application to stability analysis of recurrent neural networks," *European Journal of Control*, vol. 62, pp. 99–104, 2021.

[6] P. Khargonekar, K. Poolla, and A. Tannenbaum, "Robust control of linear time-invariant plants using periodic compensation," *IEEE* Transactions on Automatic Control, vol. 30, no. 11, pp. 1088–1096, 1985.

[7] J. Willems, "Dissipative dynamical systems part I: General theory,"
Archive for Rational Mech. and Analysis, vol. 45, no. 5, pp. 321–351, 1972.
[8] ——, "Dissipative dynamical systems part II: Linear systems with quadratic supply rates," *Archive for Rational Mech. and Analysis*,
vol. 45, no. 5, pp. 352–393, 1972.

[9] A. Schaft, L2*-gain and passivity in nonlinear control*. Springer-Verlag New York, Inc., 1999.

[10] H. Khalil, *Nonlinear Systems*. Pearson, 2001. [11] A. Megretski and A. Rantzer, "System analysis via integral quadratic constraints," *IEEE Transactions on Automatic Control*, vol. 42, no. 6, pp. 819–830, 1997.

[12] J. Veenman, C. Scherer, and H. K ¨oro ˘glu, "Robust stability and performance analysis based on integral quadratic constraints," *European* Journal of Control, vol. 31, pp. 1–32, 2016.

[13] C. Scherer, "Dissipativity and integral quadratic constraints: Tailored computational robustness tests for complex interconnections," *IEEE*
Control Systems Magazine, vol. 42, no. 3, pp. 115–139, 2022.

[14] P. Seiler, "Stability analysis with dissipation inequalities and integral quadratic constraints," *IEEE Transactions on Automatic Control*,
vol. 60, no. 6, pp. 1704–1709, 2015.

[15] L. Lessard, B. Recht, and A. Packard, "Analysis and design of optimization algorithms via integral quadratic constraints," *SIAM Journal* on Optimization, vol. 26, no. 1, pp. 57–95, 2016.

[16] B. Lee and P. Seiler, "Finite step performance of first-order methods using interpolation conditions without function evaluations," 2020. [Online]. Available: https://arxiv.org/abs/2005.01825
[17] A. Taylor, B. Van Scoy, and L. Lessard, "Lyapunov functions for first-order methods: Tight automated convergence guarantees," in International Conference on Machine Learning. PMLR, 2018, pp.

4897–4906.

[18] J. Carrasco, M. C. Turner, and W. P. Heath, "Zames-Falb multipliers for absolute stability: From O'Shea's contribution to convex searches," European Journal of Control, vol. 28, pp. 1–19, 2016.

[19] J. M. Fry, M. Farhood, and P. Seiler, "IQC-based robustness analysis of discrete-time linear time-varying systems," *International Journal of* Robust and Nonlinear Control, vol. 27, no. 16, pp. 3135–3157, 2017.

[20] B. Hu, M. J. Lacerda, and P. Seiler, "Robustness analysis of uncertain discrete-time systems with dissipation inequalities and integral quadratic constraints," International Journal of Robust and Nonlinear Control, vol. 27, no. 11, pp. 1940–1962, 2017.

[21] M. Fetzer and C. W. Scherer, "Absolute stability analysis of discrete time feedback interconnections," *IFAC-PapersOnLine*, vol. 50, no. 1, pp. 8447–8453, 2017.

[22] J. Carrasco, W. P. Heath, J. Zhang, N. S. Ahmad, and S. Wang,
"Convex searches for discrete-time Zames–Falb multipliers," *IEEE* Transactions on Automatic Control, vol. 65, no. 11, pp. 4538–4553, 2019.

[23] B. Van Scoy and L. Lessard, "Absolute stability via lifting and interpolation," in *IEEE Conference on Decision and Control*. IEEE, 2022, pp. 6217–6223.

[24] J. Soykens, J. Vandewalle, and B. De Moor, "Lur'e systems with multilayer perceptron and recurrent neural networks: absolute stability and dissipativity," *IEEE Transactions on Automatic Control*, vol. 44, no. 4, pp. 770–774, 1999.

[25] W. G. Y. Tan and Z. Wu, "Robust machine learning modeling for predictive control using Lipschitz-constrained neural networks,"
Computers & Chemical Engineering, vol. 180, p. 108466, 2024.

[26] H. Yin, P. Seiler, and M. Arcak, "Stability analysis using quadratic constraints for systems with neural network controllers," *IEEE Transactions on Automatic Control*, vol. 67, no. 4, pp. 1980–1987, 2021.

[27] K. Zhou, J. C. Doyle, and K. Glover, *Robust and Optimal Control*.

Prentice-Hall, 1996.

[28] G. Valmorbida, R. Drummond, and S. R. Duncan, "Regional analysis of slope-restricted Lurie systems," *IEEE Transactions on Automatic* Control, vol. 64, no. 3, pp. 1201–1208, 2018.

[29] L. Zaccarian and A. R. Teel, "A common framework for anti-windup, bumpless transfer and reliable designs," *Automatica*, vol. 38, no. 10, pp. 1735–1744, 2002.

[30] R. Drummond, M. C. Turner, and S. R. Duncan, "Reduced-order neural network synthesis with robustness guarantees," *IEEE Transactions* on Neural Networks and Learning Systems, vol. 35, no. 1, pp. 1182– 1191, 2024.

[31] M. Fazlyab, M. Morari, and G. J. Pappas, "Safety verification and robustness analysis of neural networks via quadratic constraints and semidefinite programming," *IEEE Transactions on Automatic Control*, vol. 67, no. 1, pp. 1–15, 2020.

[32] M. Vidyasagar, *Nonlinear systems analysis*. SIAM, 2002.

[33] M. Grant and S. Boyd, "CVX: Matlab software for disciplined convex programming, version 2.1," https://cvxr.com/cvx, Mar. 2014.

[34] K.-C. Toh, M. J. Todd, and R. H. T ¨ut ¨unc¨u, "Sdpt3—a matlab software package for semidefinite programming, version 1.3," Optimization methods and software, vol. 11, no. 1-4, pp. 545–581, 1999.

[35] R. H. T ¨ut ¨unc¨u, K.-C. Toh, and M. J. Todd, "Solving semidefinitequadratic-linear programs using sdpt3," *Mathematical programming*,
vol. 95, pp. 189–217, 2003.

This figure "p1.jpg" is available in "jpg"
 format from:
http://arxiv.org/ps/2405.05236v1