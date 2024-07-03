# Stability and Performance Analysis of Discrete-Time ReLU Recurrent Neural Networks 

Sahel Vahedi Noori, Bin Hu, Geir Dullerud, and Peter Seiler


#### Abstract

This paper presents sufficient conditions for the stability and $\ell_{2}$-gain performance of recurrent neural networks (RNNs) with ReLU activation functions. These conditions are derived by combining Lyapunov/dissipativity theory with Quadratic Constraints (QCs) satisfied by repeated ReLUs. We write a general class of QCs for repeated RELUs using known properties for the scalar ReLU. Our stability and performance condition uses these QCs along with a "lifted" representation for the ReLU RNN. We show that the positive homogeneity property satisfied by a scalar ReLU does not expand the class of QCs for the repeated ReLU. We present examples to demonstrate the stability / performance condition and study the effect of the lifting horizon.


## I. InTRODUCTION

This paper considers the analysis of recurrent neural networks (RNNs) with ReLU activation functions. These are modeled by the interconnection of a discrete-time, linear time-invariant (LTI) system in feedback with a repeated ReLU. The goal is to derive sufficient conditions to prove stability and performance (as measured by the induced $\ell_{2}$ gain) for this RNN. This work is motivated by the increasing interest in RNNs for inner-loop feedback control. Such RNNs can potentially improve performance over more standard LTI controllers. However, the analysis of closed-loop stability and performance is challenging due to the nonlinear activation functions in the RNN. The sufficient conditions in this paper are one step to address this issue.

Our technical approach combines multiple ingredients in the existing literature. First, we note that the scalar ReLU has slope restricted to $[0,1]$. Hence the repeated ReLU satisfies a known QC involving doubly hyperdominant matrices [1]-[3]. Second, we present QCs that are specific to repeated ReLUs building on work in [4], [5]. Next, we write the ReLU RNN using a "lifted" representation over an $N$-step horizon [6]. This lifting allows us to construct more general QCs that hold for the ReLU across multiple time steps. Finally, we combine Lyapunov and dissipativity theory [7]-[10] with these QCs to obtain sufficient conditions for stability and performance of the lifted ReLU RNN. Stability and performance of the original (unlifted) ReLU RNN follows from this analysis.

This paper adds to the broader literature on integral quadratic constraint (IQC) conditions [11]-[14]. Our sta-

S. Vahedi Noori and P. Seiler are with the Department of Electrical Engineering \& Computer Science, at the University of Michigan (sahelvn@umich.edu; and pseiler@umich.edu). B. Hu is with the Department of Electrical and Computer Engineering at the University of Illinois at Urbana-Champaign (binhu7@illinois.edu). G. Dullerud is with the the Department of Mechanical Science and Engineering at the University of Illinois at Urbana-Champaign (dullerud@illinois.edu) bility/performance condition is similar to the discrete-time, IQC formulations in [15]-[22]. The most closely related conditions are in [16], [23], both of which use lifting and static QCs (rather than dynamic IQCs). There is also growing literature on using these techniques to analyze $\mathrm{NNs}$ and RNNs [4], [5], [24]-[26]. We specifically build on the results for ReLU RNNs in [4], [5]. In particular, [4] derives QCs for ReLU and uses Lyapunov theory to prove stability for continuous-time ReLU RNNs. We build on this work in discrete-time and also prove $\ell_{2}$ bounds. The work in [5] also addresses discrete-time ReLU RNNs, similar to our paper, but uses small-gain arguments. In contrast, we use QCs and Lyapunov/dissipativity theory leading to related, but different conditions.

Our contributions to this existing literature are as follows. First, we write a general class of QCs for repeated ReLU using known existing properties. We show that the positive homogeneity property satisfied by scalar ReLUs, i.e. $\phi(\beta v)=\beta v$ for all $\beta \geq 0$, does not expand the class of QCs for repeated ReLUs. Second, we use the discrete-time lifting, originally proposed in [6], that maintains the state dimension. This is different from the liftings used previously in [16], [23] for which the lifted state grows with the lifting horizon. Finally, we present examples to illustrate the effects of the ReLU QCs and lifting time horizon. We show that the ReLU QCs can significantly reduce the conservatism as compared to QCs developed for the more general class of slope-restricted nonlinearities (although the performance is problem dependent).

## II. NOTATION

This section briefly reviews basic notation regarding vectors, matrices, and signals. Let $\mathbb{R}^{n}$ and $\mathbb{R}^{n \times m}$ denote the sets of real $n \times 1$ vectors and $n \times m$ matrices, respectively. Moreover, $\mathbb{R}_{\geq 0}^{n}$ and $\mathbb{R}_{\geq 0}^{n \times m}$ denote vectors and matrices of the given dimensions with non-negative entries. Let $D^{n}$ denote the set of $n \times n$ diagonal matrices and $D_{\geq 0}^{n}$ the subset of diagonal matrices with non-negative entries. Finally, $M \in$ $\mathbb{R}^{n \times n}$ is a Metzler matrix if the off-diagonal entries are nonnegative, i.e. $M_{i j} \geq 0$ for $i \neq j$. A matrix $M \in \mathbb{R}^{n \times n}$ is doubly hyperdominant if the off-diagonal elements are non-positive, and both the row sums and column sums are non-negative.

Next, let $\mathbb{N}$ denote the set of non-negative integers. Let $v: \mathbb{N} \rightarrow \mathbb{R}^{n}$ and $w: \mathbb{N} \rightarrow \mathbb{R}^{n}$ be real, vector-valued sequences. Define the inner product $\langle v, w\rangle:=\sum_{k=0}^{\infty} v(k)^{\top} w(k)$. The set $\ell_{2}$ is an inner product space with sequences $v$ that satisfy $\langle v, v\rangle<\infty$. The corresponding norm is $\|v\|_{2}:=\sqrt{\langle v, v\rangle}$.

## III. Problem Statement

Consider the interconnection shown on the left of Figure 1 with a static nonlinearity $\Phi$ wrapped in feedback around the top channels of a nominal system $G$. This interconnection is denoted as $F_{U}(G, \Phi)$. The nominal part $G$ is a discrete-time, linear time-invariant (LTI) system described by the following state-space model:

$$
\begin{aligned}
& x(k+1)=A x(k)+B_{1} w(k)+B_{2} d(k) \\
& v(k)=C_{1} x(k)+D_{11} w(k)+D_{12} d(k) \\
& e(k)=C_{2} x(k)+D_{21} w(k)+D_{22} d(k)
\end{aligned}
$$

where $x \in \mathbb{R}^{n_{x}}$ is the state. The inputs are $w \in \mathbb{R}^{n_{w}}$ and $d \in \mathbb{R}^{n_{d}}$ while $v \in \mathbb{R}^{n_{v}}$ and $e \in \mathbb{R}^{n_{e}}$ are outputs. The static nonlinearity $\Phi: \mathbb{R}^{n_{v}} \rightarrow \mathbb{R}_{>0}^{n_{v}}$ maps $v$ to $w$ elementwise by $w_{i}=\phi\left(v_{i}\right)$ for $i=1, \ldots, n_{v}$ where $\phi: \mathbb{R} \rightarrow \mathbb{R}_{\geq 0}$ is the ReLU function. The ReLU, shown on the right of Figure 11 is:

$$
\phi(v)= \begin{cases}0 & \text { if } v<0 \\ v & \text { if } v \geq 0\end{cases}
$$

We refer to $\Phi$ as a repeated ReLU and $\phi$ as the scalar ReLU. The interconnection $F_{U}(G, \Phi)$ is known as a linear fractional transformation (LFT) in the robust control literature [27]. The interconnection has its roots in the Lurye decomposition used in the absolute stability problem [10].



Fig. 1: Left: Interconnection $F_{U}(G, \Phi)$ of a nominal discretetime LTI system $G$ and repeated ReLU $\Phi$. Right: Graph of scalar ReLU $\phi$.

This feedback interconnection involves an implicit equation if $D_{11} \neq 0$. Specifically, the second equation in (1) combined with $w(k)=\Phi(v(k))$ yields:

$$
v(k)=C_{1} x(k)+D_{11} \Phi(v(k))+D_{12} d(k)
$$

This equation is well-posed if there exists a unique solution $v(k)$ for all values of $x(k)$ and $d(k)$. Well-posedness of this equation implies that the dynamic system $F_{U}(G, \Phi)$ is wellposed in the following sense: for all initial conditions $x(0) \in$ $\mathbb{R}^{n_{x}}$ and inputs $d \in \ell_{2}$ there exists unique solutions $x, v, w$ and $e \in \ell_{2}$ to the system $F_{U}(G, \Phi)$. There are simple sufficient conditions for well-posedness of (3), e.g. Lemma 1 in [4] (which relies on results in [28], [29]). Thus, we'll assume well-posed for simplicity in the remainder of the paper.

A well-posed interconnection $F_{U}(G, \Phi)$ is internally stable if $x(k) \rightarrow 0$ from any initial condition $x(0)$ with $d(k)=0$ for $k \in \mathbb{N}$. In other words, $F_{U}(G, \Phi)$ is internally stable if $x=0$ is a globally asymptotically stable equilibrium point with no external input. A well-posed interconnection $F_{U}(G, \Phi)$ has finite induced- $\ell_{2}$ gain if there exists $\gamma<\infty$ such that the output $e$ generated by any $d \in \ell_{2}$ with $x(0)=0$ satisfies $\|e\|_{2} \leq \gamma\|d\|_{2}$. This bound is denoted as $\left\|F_{U}(G, \Phi)\right\|_{2 \rightarrow 2} \leq \gamma$. The goal of this paper is to derive sufficient conditions, using the properties of the $\operatorname{ReLU}$, that verify $F_{U}(G, \Phi)$ is internally stable and has finite induced $\ell_{2}$ gain.

## IV. Main Results

The section presents the main results: sufficient conditions for stability and performance of the ReLU RNNs. These sufficient conditions are based on dissipativity theory and quadratic constraints $(\mathrm{QCs})$ for the repeated ReLU.

## A. Quadratic Constraints for Slope-Restricted Functions

First, consider a scalar function $\phi: \mathbb{R} \rightarrow \mathbb{R}_{\geq 0}$ that satisfies $\phi(0)=0$ and has slope restricted to $[0,1]$, i.e.:

$$
0 \leq \frac{\phi\left(v_{2}\right)-\phi\left(v_{1}\right)}{v_{2}-v_{1}} \leq 1, \forall v_{1}, v_{2} \in R, v_{1} \neq v_{2}
$$

This subsection presents QCs that hold for any activation function $\phi$ that satisfies these conditions. This includes, but is not limited to, the ReLU.

The graph of $\phi$ is restricted to the $[0,1]$ sector, i.e. its graph lies between lines that pass through the origin with slope 0 and 1. Thus the following QC holds $\forall v \in \mathbb{R}$ and $w=\phi(v)$ :

$$
w(v-w) \geq 0
$$

Moreover, any two points on the graph of $\phi$ are connected by a line with slope in $[0,1]$. Hence the following QC holds for all $v_{1}, v_{2} \in \mathbb{R}, w_{1}=\phi\left(v_{1}\right)$, and $w_{2}=\phi\left(v_{2}\right)$ :

$$
\left(w_{2}-w_{1}\right)\left(v_{2}-v_{1}-\left(w_{2}-w_{1}\right)\right) \geq 0
$$

Next, consider a repeated nonlinearity $\Phi: \mathbb{R}^{m} \rightarrow \mathbb{R}_{>0}^{m}$ that maps $v$ to $w$ elementwise $w_{k}=\phi\left(v_{k}\right)$ for $k=1, \ldots, m$. We can derive a QC for $\Phi$ based on scaled combinations of the sector and slope constraints for the data $\left\{\left(v_{k}, w_{k}\right)\right\}_{k=1}^{m}$. Specifically, for any non-negative constants $\lambda_{k}$ and $\gamma_{k j}$ :

$$
\begin{aligned}
& \lambda_{k} w_{k}\left(v_{k}-w_{k}\right) \geq 0 \text { for } k=1, \ldots m \\
& \gamma_{k j}\left(w_{k}-w_{j}\right)\left(v_{k}-v_{j}-\left(w_{k}-w_{j}\right)\right) \geq 0 . \text { for } k, j=1, \ldots m
\end{aligned}
$$

Summing over all these constraints gives an inequality of the form $w^{\top} Q_{0}(v-w) \geq 0$ where

$$
\left(Q_{0}\right)_{k j}=\left\{\begin{array}{cc}
\lambda_{k}+\sum_{k \neq j}\left(\gamma_{k j}+\gamma_{j k}\right) & \text { if } k=j \\
-\left(\gamma_{k j}+\gamma_{j k}\right) & \text { else }
\end{array}\right.
$$

$Q_{0}$ is a symmetric, doubly hyperdominant matrix. Lemma 1 , stated next, provides a more general $\mathrm{QC}$ for this case in that it allows for $Q_{0}$ to be non-symmetric.

Lemma 1: Let $\Phi: \mathbb{R}^{m} \rightarrow \mathbb{R}_{>0}^{m}$ be a repeated nonlinearity with $\Phi(0)=0$ and slope restricted (elementwise) to $[0,1]$. If $Q_{0} \in \mathbb{R}^{m \times m}$ is doubly hyperdominant then the following QC holds $\forall v \in \mathbb{R}^{m}$ and $w=\Phi(v)$ :

$$
\left[\begin{array}{c}
v \\
w
\end{array}\right]^{\top}\left[\begin{array}{cc}
0 & Q_{0}^{\top} \\
Q_{0} & -\left(Q_{0}+Q_{0}^{\top}\right)
\end{array}\right]\left[\begin{array}{c}
v \\
w
\end{array}\right] \geq 0
$$

Proof: This follows from the results in Section 3.5 of [2]. Specifically, for any pair $v$ and $w=\Phi(v)$, define $\tilde{v}:=v-w \in \mathbb{R}^{m}$. Equation 5 implies that $\left\{\left(\tilde{v}_{k}, w_{k}\right)\right\}_{k=1}^{m}$ is similarly ordered data, i.e. $\tilde{v}_{k}>\tilde{v}_{j}$ implies $w_{k} \geq w_{j}$. Moreover, it follows from (4) that the data is unbiased, i.e. $w_{k} \tilde{v}_{k} \geq 0$ for $k=1, \ldots, m$. Theorem 3.8 in [2] implies that if $Q_{0}$ is doubly hyperdominant then $w^{\top} Q_{0} \tilde{v} \geq 0$. Thus $w^{\top} Q_{0}(v-w)+(v-w)^{\top} Q_{0}^{\top} w \geq 0$.

The proof of Theorem 3.8 in [2] relies on a cyclic rearrangement inequality satisfied by similarly ordered, unbiased data. In fact, the doubly hyperdominance condition is the largest class of QCs that holds for slope-restricted functions whose graph passes through the origin. A precise statement of this fact is given in Theorem 1 of [3] [1]

## B. Quadratic Constraints for ReLU

The previous subsection presented QCs for functions with slope restricted to $[0,1]$. This section derives several additional QCs that are specific to the repeated ReLU. This builds on prior work in [4], [5]. The starting point for these QCs are the following properties for the scalar ReLU that have been used previously in the literature [4], [5], [30], [31]:.

1) Positivity: The scalar ReLU is non-negative for all inputs: $\phi(v) \geq 0 \forall v \in \mathbb{R}$.
2) Positive Complement: The scalar ReLU satisfies $\phi(v) \geq v \forall v \in \mathbb{R}$
3) Complementarity: In addition to the $[0,1]$ sector, the ReLU satisfies the stronger complementarity property: its graph is identically on the line of slope 0 (when $v \leq$ 0 ) or the line of slope 1 (when $v \geq 0)$. Thus, $\phi(v)(v-$ $\phi(v))=0 \forall v \in \mathbb{R}$
4) Positive Homogeneity: The scalar ReLU is homogeneous for all non-negative constants: $\phi(\beta v)=\beta \phi(v)$ $\forall v \in \mathbb{R}$ and $\forall \beta \in \mathbb{R}_{\geq 0}$.

Properties 1-3 can be combined to construct QCs for the repeated ReLU. Lemmas 2 and 3 below are variations of results in $[4]$.

Lemma 2: Let $\Phi: \mathbb{R}^{m} \rightarrow \mathbb{R}_{\geq 0}^{m}$ be a repeated ReLU. If $Q_{1} \in$ $D^{m}$ then the following QC holds $\forall v \in \mathbb{R}^{m}$ and $w=\Phi(v)$ :

$$
\left[\begin{array}{c}
v \\
w
\end{array}\right]^{\top}\left[\begin{array}{cc}
0 & Q_{1} \\
Q_{1} & -\left(Q_{1}+Q_{1}^{\top}\right)
\end{array}\right]\left[\begin{array}{c}
v \\
w
\end{array}\right]=0
$$

Proof: $Q_{1}$ is diagonal by assumption so that:

$$
\left[\begin{array}{c}
v \\
w
\end{array}\right]^{\top}\left[\begin{array}{cc}
0 & Q_{1} \\
Q_{1} & -\left(Q_{1}+Q_{1}^{\top}\right)
\end{array}\right]\left[\begin{array}{c}
v \\
w
\end{array}\right]=\sum_{k=1}^{m}\left(Q_{1}\right)_{k k} w_{k}\left(v_{k}-w_{k}\right)
$$

This is equal to zero based on the complementarity property for each $\left\{\left(v_{k}, w_{k}\right)\right\}_{k=1}^{m}$. Note that the diagonal entries of $Q_{1}$ are not necessarily non-negative.[^0]

Lemma 3: Let $\Phi: \mathbb{R}^{m} \rightarrow \mathbb{R}_{\geq 0}^{m}$ be a repeated ReLU. If $Q_{2}=$ $Q_{2}^{\top}, Q_{3}=Q_{3}^{\top}, Q_{4} \in \mathbb{R}_{\geq 0}^{m \times m}$ then the following $\mathrm{QC}$ holds $\forall v \in$ $\mathbb{R}^{m}$ and $w=\Phi(v)$ :

$$
\left[\begin{array}{c}
v \\
w
\end{array}\right]^{\top}\left[\begin{array}{cc}
Q_{2} & -\left(Q_{2}+Q_{4}^{\top}\right) \\
-\left(Q_{2}+Q_{4}\right) & Q_{2}+Q_{3}+Q_{4}+Q_{4}^{\top}
\end{array}\right]\left[\begin{array}{c}
v \\
w
\end{array}\right] \geq 0
$$

Proof: The positivity and positive complement properties are linear constraints on $\left\{\left(v_{k}, w_{k}\right)\right\}_{k=1}^{m}$. These can be combined to form QCs on pairs of points. The QCs below hold for any non-negative $\left(Q_{2}\right)_{k j},\left(Q_{3}\right)_{k j}$, and $\left(Q_{4}\right)_{k j}$ :

$$
\begin{aligned}
& \left(Q_{2}\right)_{k j}\left(w_{k}-v_{k}\right)\left(w_{j}-v_{j}\right) \geq 0 \\
& \left(Q_{3}\right)_{k j} w_{k} w_{j} \geq 0 \\
& \left(Q_{4}\right)_{k j} w_{k}\left(w_{j}-v_{j}\right) \geq 0
\end{aligned}
$$

Equations 10 and 11 are equivalent to $(w-v)^{\top} Q_{2}(w-v) \geq 0$ and $w^{\top} Q_{3} w \geq 0$, respectively. These $\mathrm{QCs}$ are quadratic forms and hence we can assume $Q_{2}=Q_{2}^{\top}$ and $Q_{3}=Q_{3}^{\top}$ without loss of generality. Equation 12 is equivalent to $w^{\top} Q_{4}(w-$ $v)+(w-v)^{\top} Q_{4}^{\top} w \geq 0$.

The next result combines all the QCs in the Lemmas 1 3. This is the most general $\mathrm{QC}$ based on the $[0,1]$ sector / slope restrictions combined with the known properties for scalar ReLU.

Lemma 4: Let $\Phi: \mathbb{R}^{m} \rightarrow \mathbb{R}_{\geq 0}^{m}$ be a repeated ReLU. Let $Q_{2}=Q_{2}^{\top}, Q_{3}=Q_{3}^{\top} \in \mathbb{R}_{\geq 0}^{m \times m}$ and $\tilde{Q} \in \mathbb{R}^{m \times m}$ be given with $\tilde{Q}$ a Metzler matrix. Then the following QC holds $\forall v \in \mathbb{R}^{m}$ and $w=\Phi(v)$ :

$$
\left[\begin{array}{c}
v \\
w
\end{array}\right]^{\top}\left[\begin{array}{cc}
Q_{2} & -\tilde{Q}^{\top}-Q_{2} \\
-\tilde{Q}-Q_{2} & Q_{2}+Q_{3}+\tilde{Q}+\tilde{Q}^{\top}
\end{array}\right]\left[\begin{array}{c}
v \\
w
\end{array}\right] \geq 0
$$

Proof: Gather all the QCs given in Lemmas 113 Define $\tilde{Q}=Q_{4}-Q_{0}-Q_{1}$ where $Q_{0} \in \mathbb{R}^{m \times m}$ is doubly hyperdominant, $Q_{1} \in D^{m}$ and $Q_{4} \in \mathbb{R}_{\geq 0}^{m \times m}$. The diagonal entries of $\tilde{Q}$ can be anything while the off-diagonal entries must be non-negative. Hence $\tilde{Q}$ is a Metzler matrix.

Finally, the next lemma exploits the positive homogeneity property of the ReLU. Related results are given in Section 4.3 of $[5]$.

Lemma 5: Let $\Phi: \mathbb{R}^{m} \rightarrow \mathbb{R}_{\geq 0}^{m}$ be a repeated ReLU. Assume $\Phi$ satisfies the QC defined by $M=M^{\top} \in \mathbb{R}^{2 m \times 2 m}$, i.e $\forall v \in \mathbb{R}^{m}$ and $w=\Phi(v):$

$$
\left[\begin{array}{c}
v \\
w
\end{array}\right]^{\top}\left[\begin{array}{ll}
M_{11} & M_{12} \\
M_{12}^{\top} & M_{22}
\end{array}\right]\left[\begin{array}{c}
v \\
w
\end{array}\right] \geq 0
$$

If $\Lambda \in D_{\geq 0}^{m}$ then $\Phi$ also satisfies the $\mathrm{QC}$ defined by $\left[\begin{array}{ll}\Lambda & 0 \\ 0 & \Lambda\end{array}\right] M\left[\begin{array}{ll}\lambda & 0 \\ 0 & \Lambda\end{array}\right] \in \mathbb{R}^{2 m \times 2 m}$, i.e. $\forall \bar{v} \in \mathbb{R}^{m}$ and $\bar{w}=\Phi(\bar{v})$ :

$$
\left[\begin{array}{c}
\bar{v} \\
\bar{w}
\end{array}\right]^{\top}\left[\begin{array}{cc}
\Lambda^{\top} M_{11} \Lambda & \Lambda^{\top} M_{12} \Lambda \\
\left(\Lambda^{\top} M_{12} \Lambda\right)^{\top} & \Lambda^{\top} M_{22} \Lambda
\end{array}\right]\left[\begin{array}{c}
\bar{v} \\
\bar{w}
\end{array}\right] \geq 0
$$

Proof: Take any $\bar{v} \in \mathbb{R}^{m}$ and $\bar{w}=\Phi(\bar{v})$. Let $\Lambda$ is a diagonal matrix with non-negative entries. Apply positive homogeneity of the scalar ReLU, element-wise, to conclude that $\Lambda \bar{w}=\Phi(\Lambda \bar{v})$. Next, define $v=\Lambda \bar{v}$ and $w=\Lambda \bar{w}$ so that
$w=\Phi(v)$. The $\mathrm{QC}$ in (14) holds, by assumption, for $(v, w)$. Substitute $v=\Lambda \bar{v}$ and $w=\Lambda \bar{w}$ to show the $\mathrm{QC}$ in (15) also holds for $(\bar{v}, \bar{w})$.

The positive homogeneity property seems to generalize the class of QCs for repeated ReLU by allowing for an additional scaling $\Lambda \in D_{>0}^{m}$. However, this additional freedom does not increase the class of QCs if we use the results of Lemma4. Specifically, if $Q_{2}, Q_{3} \in \mathbb{R}_{>0}^{m \times m}$ then $\Lambda Q_{2} \Lambda, \Lambda Q_{3} \Lambda \in \mathbb{R}_{>0}^{m \times m}$ for all $\Lambda \in D_{>0}^{m}$. Similarly, if $\tilde{Q} \in \mathbb{R}^{m \times m}$ is a Metzler matrix then $\Lambda \tilde{Q} \Lambda$ is also a Metzler matrix for all $\Lambda \in D_{>0}^{m}$. Thus positive homogeneity does not provide additional freedom when combined with the most general QC given in Lemma4, i.e. we get the same class of QCs. However, the positive homogeneity scaling $\Lambda$ can provide an additional degrees of freedom when combined with more restricted subsets of QCs. For example, suppose we use the restricted class of QCs based on slope restrictions (Lemma 1). In this case, the positive homogeneity property can provide a benefit because if $Q_{0} \in \mathbb{R}^{m \times m}$ is doubly hyperdominant and $\Lambda \in D_{\geq 0}^{m}$ then $\Lambda Q_{0} \Lambda$ is not necessarily doubly hyperdominant. In this case, the scaling introduced by positivity homogeneity (Lemma 5) will generalize beyond the initial (restricted) class of sloperestricted QCs.

## C. Conditions for Stability and Performance

This section presents a sufficient condition for the feedback connection $F_{U}(G, \Phi)$ to be stable and have bounded induced $\ell_{2}$-gain. The condition uses a lifted plant, defined below, combined with Lyapunov/dissipativity theory and the QCs derived in the previous subsection.

The first step is to create a lifted representation for $F_{U}(G, \Phi)$ where $G$ is the LTI system (1) and $\Phi$ is the repeated ReLU. Define the stacked vectors for both the input/output signals of $G$ as:

$$
\begin{aligned}
V_{N}(k) & =\left[\begin{array}{llll}
v^{\top}(k) & v^{\top}(k-1) & \cdots & v^{\top}(k-N+1)
\end{array}\right]^{\top} \\
W_{N}(k) & =\left[\begin{array}{llll}
w^{\top}(k) & w^{\top}(k-1) & \cdots & w^{\top}(k-N+1)
\end{array}\right]^{\top} \\
D_{N}(k) & =\left[\begin{array}{llll}
d^{\top}(k) & d^{\top}(k-1) & \cdots & d^{\top}(k-N+1)
\end{array}\right]^{\top} \\
E_{N}(k) & =\left[\begin{array}{llll}
e^{\top}(k) & d^{\top}(k-1) & \cdots & d^{\top}(k-N+1)
\end{array}\right]^{\top}
\end{aligned}
$$

These vectors stack the signals over an $N$ step horizon from $k-N+1$ to $k$.

The nominal plant dynamics can be lifted [6] to evolve the state $N$ steps from $x(k-N+1)$ to $x(k+1)$. The lifted nominal plant, denoted $G_{N}$, has the form:

$$
\begin{aligned}
& x(k+1)=A^{N} x(k-N+1)+B_{1, N} W_{N}(k)+B_{2, N} D_{N}(k) \\
& V_{N}(k)=C_{1, N} x(k-N+1)+D_{11, N} W_{N}(k)+D_{12, N} D_{N}(k) \\
& E_{N}(k)=C_{2, N} x(k-N+1)+D_{21, N} W_{N}(k)+D_{22, N} D_{N}(k)
\end{aligned}
$$

The state matrices ( $B_{1, N}, B_{2, N}$, etc.) can be constructed for the specified horizon $N$ from the state-matrices of the original nominal plant. The lifted plant given here has the same state dimension as the original plant but the input/output dimensions are stacked, e.g. $W_{N} \in \mathbb{R}^{n_{w} N}$ and $B_{1, N} \in \mathbb{R}^{n_{x} \times n_{w} N}$.
A related, but different, lifting is used in [16], [17] where the state-dimension grows with the horizon $N$.

The repeated ReLU can also be lifted. Define $\Phi_{N}: \mathbb{R}^{n_{v} N} \rightarrow$ $\mathbb{R}^{n_{v} N}$ by applying the scalar ReLU elementwise to the input. In summary, the lifted system $F_{U}\left(G_{N}, \Phi_{N}\right)$ maps $D_{N}(k)$ to $E_{N}(k)$ based on the interconnection of $G_{N}$ in (16) and $W_{N}(k)=\Phi_{N}\left(V_{N}(k)\right)$.

We next state the stability and performance condition for the lifted system. Define a linear matrix inequality (LMI) with the lifted system of $G_{N}$ :

$$
\begin{aligned}
& \operatorname{LMI}\left(P, M, \gamma^{2}\right):= \\
& {\left[\begin{array}{ccc}
\left(A^{N}\right)^{\top} P\left(A^{N}\right)-P & \left(A^{N}\right)^{\top} P B_{1, N} & \left(A^{N}\right)^{\top} P B_{2, N} \\
B_{1, N}^{\top} P\left(A^{N}\right) & B_{1, N}^{\top} P B_{1, N} & B_{1, N}^{\top} P B_{2, N} \\
B_{2, N}^{\top} P\left(A^{N}\right) & B_{2, N}^{\top} P B_{1, N} & B_{2, N}^{\top} P B_{2, N}-\gamma^{2} I
\end{array}\right]} \\
& +\left[\begin{array}{c}
C_{2, N}^{\top} \\
D_{21, N}^{\top} \\
D_{22, N}^{\top}
\end{array}\right]\left[\begin{array}{c}
C_{2, N}^{\top} \\
D_{21}^{\top} \\
D_{22, N}^{\top}
\end{array}\right]^{\top}+\left[\begin{array}{cc}
C_{1, N}^{\top} & 0 \\
D_{11, N}^{\top} & I \\
D_{12, N}^{\top} & 0
\end{array}\right] M\left[\begin{array}{cc}
C_{1, N}^{\top} & 0 \\
D_{11, N}^{\top} & I \\
D_{12, N}^{\top} & 0
\end{array}\right]^{\top}
\end{aligned}
$$

The next theorem provides an stability and performance condition for the ReLU RNN formulated with this LMI. The proof uses a QC for the lifted ReLU and a standard Lyapunov / dissipation argument.

Theorem 1: Consider the $\operatorname{ReLU} \operatorname{RNN} F_{U}(G, \Phi)$ with the LTI system $G$ defined in (1). Assume this interconnection is well-posed. Let $G_{N}$ and $\Phi_{N}: \mathbb{R}^{m} \rightarrow \mathbb{R}^{m}$ be the lifted system and lifted ReLU for some $N \in \mathbb{N}$ with dimension $m:=n_{v} N$.

Let $Q_{2}=Q_{2}^{\top}, Q_{3}=Q_{3}^{\top} \in \mathbb{R}_{\geq 0}^{m \times m}$ and $\tilde{Q} \in \mathbb{R}^{m \times m}$ be given with $\tilde{Q}$ a Metzler matrix. Define $M=M^{\top} \in \mathbb{R}^{2 m \times 2 m}$ as follows:

$$
M:=\left[\begin{array}{cc}
Q_{2} & -\tilde{Q}^{\top}-Q_{2} \\
-\tilde{Q}-Q_{2} & Q_{2}+Q_{3}+\tilde{Q}+\tilde{Q}^{\top}
\end{array}\right]
$$

Then the lifted ReLU $\Phi_{N}$ satisfies the QC defined by $M$, i.e. $\left[\begin{array}{l}v \\ w\end{array}\right]^{\top} M\left[\begin{array}{l}v \\ w\end{array}\right] \forall v \in \mathbb{R}^{m}$ and $w=\Phi_{N}(v)$.

Moreover, if there exists a positive semidefinite matrix $P=$ $P^{\top} \in \mathbb{R}^{n_{x} \times n_{x}}$ and scalar $\gamma \geq 0$ such that $\operatorname{LMI}\left(P, M, \gamma^{2}\right)<0$, then the ReLU RNN $F_{U}(G, \Phi)$ is internally stable and has $\left\|F_{U}(G, \Phi)\right\|_{2 \rightarrow 2}<\gamma$

Proof: This theorem is a standard dissipation result [7][10], [20]. A proof is given for completeness.

It follows directly from Lemman that $\Phi_{N}$ satisfies the QC defined by $M$. We'll first use this $\mathrm{QC}$ and the LMI condition to show the lifted system $F_{U}\left(G_{N}, \Phi_{N}\right)$ is stable and with $\ell_{2}$ gain bounded by $\gamma$.

The LMI is strictly feasible by assumption and hence it remains feasible under small perturbations: $L M I(P+$ $\left.\varepsilon I, M, \gamma^{2}\right)+\varepsilon I<0$ for some sufficiently small $\varepsilon>0$. Moreover, well-posedness of $F_{U}\left(G_{N}, \Phi_{N}\right)$ follows from the assumption that $F_{U}(G, \Phi)$ is well-posed. Hence the lifted system $F_{U}\left(G_{N}, \Phi_{N}\right)$ has a unique causal solution $\left(x, W_{N}, V_{N}, E_{N}\right)$ for any given initial condition $x_{N}(0)$ and input $D_{N} \in \ell_{2}^{n_{d} N}$.

Define a storage function by $V(x):=x^{\top}(P+\varepsilon I) x$. Left and right multiply the perturbed LMI by $\left[x(k)^{\top}, W_{N}(k)^{\top}, D_{N}(k)^{\top}\right]$
and its transpose. The result, applying the lifted dynamics (16), gives the following condition:

$$
\begin{aligned}
& V(x(k+1))-V(x(k))-\gamma^{2} D_{N}(k)^{\top} D_{N}(k)+E_{N}(k)^{\top} E_{N}(k) \\
& +\left[\begin{array}{c}
V_{N}(k) \\
W_{N}(k)
\end{array}\right]^{\top} M\left[\begin{array}{l}
V_{N}(k) \\
W_{N}(k)
\end{array}\right]+\varepsilon\left[\begin{array}{c}
x(k) \\
W_{N}(k) \\
D_{N}(k)
\end{array}\right]^{\top}\left[\begin{array}{c}
x(k) \\
W_{N}(k) \\
D_{N}(k)
\end{array}\right] \leq 0
\end{aligned}
$$

The term involving $M$ is non-negative as the lifted ReLU satisfies the QC defined by $M$. Thus the dissipation inequality simplifies to:

$$
\begin{aligned}
& V(x(k+1))-V(x(k))+E_{N}(k)^{\top} E_{N}(k) \\
& \leq\left(\gamma^{2}-\varepsilon\right) D_{N}(k)^{\top} D_{N}(k)-\varepsilon x(k)^{\top} x(k)
\end{aligned}
$$

Internal stability and the $\ell_{2}$ gain bound for the lifted system $F_{U}\left(G_{N}, \Phi_{N}\right)$ follow from this inequality. Specifically, if $D_{N}(k)=0$ for all $k$ then (19) simplifies to the following Lyapunov inequality:

$$
V(x(k+1))-V(x(k)) \leq-\varepsilon x(k)^{\top} x(k)
$$

Hence $V$ is a Lyapunov function and the lifted system is globally asymptotically stable (Theorem 27 in Section 5.9 of $[32])$.

Next, assume $x(0)=0$ and $D_{N} \in \ell_{2}$. Summing (19) from $k=0$ to $k=T-1$ and using $V(x(0))=0$ yields:

$$
V(x(T))+\sum_{k=0}^{T-1} E_{N}(k)^{\top} E_{N}(k) \leq \sum_{k=0}^{T-1}\left(\gamma^{2}-\varepsilon\right) D_{N}(k)^{\top} D_{N}(k)
$$

Note that $V(x(T)) \geq 0$ because $P$ is positive semidefinite. Moreover, the right side is upper bounded by $\left(\gamma^{2}-\varepsilon\right)\left\|D_{N}\right\|_{2}^{2}$ for all $T \in \mathbb{N}$. This implies that $E_{N} \in \ell_{2}$ and $\left\|E_{N}\right\|_{2}<\gamma\left\|D_{N}\right\|_{2}$.

In summary, the lifted system $F_{U}\left(G_{N}, \Phi_{N}\right)$ is internally stable and satisfies $\| F_{U}\left(\left(G_{N}, \Phi_{N}\right) \|_{2 \rightarrow 2}<\gamma\right.$. The lifting is an isomorphism and preserves signal norms: $\|d\|_{2}=\left\|D_{N}\right\|_{2}$ and $\|e\|_{2}=\left\|E_{N}\right\|_{2}$. It follows that the original system also satisfies the gain bound $\| F_{U}\left((G, \Phi) \|_{2 \rightarrow 2}<\gamma\right.$. Moreover, the state of the lifted system corresponds to the evolving the state of the original system forward by $N$ steps. Simple bounding arguments can be used to show that if the lifted state converges to the origin then so does the original state. Hence internal stability of the lifted system also implies internal stability of the original system.

## V. NUMERICAL EXAMPLES

## A. Stability Analysis

A variety of examples are given in [18] to study the use of discrete-time Zames-Falb multipliers for analyzing stability of Lurye systems. We will use Example 6 in Table 1 of [18] as a benchmark to illustrate our ReLU RNN stability and performance condition.

Consider the Lurye system shown in Figure 2 where $\phi$ : $\mathbb{R} \rightarrow \mathbb{R}$ is a nonlinear function, $\alpha$ is a non-negative scaling, and $G_{11}(z)=\frac{2 z+0.92}{z^{2}-0.5 z}$ is a discrete-time system. The results in [18] focus on the class of nonlinearities that have slope restricted to $[0,1]$. The goal is to find the stability margin, i.e. the largest value of $\alpha \geq 0$ for which this Lurye system is stable for all nonlinearities in this class. Their reported results are shown in Table The Circle and Tsypkin criteria both can be used to prove stability for $\alpha$ up to 0.6510 . The Zames-Falb condition in [18] proves stability for $\alpha$ up to 1.087知 In fact, the Zames-Falb condition achieves the largest possible stability margin for the class of $[0,1]$ slope restricted nonlinearities. This follows because the Lurye system is unstable for $\phi(v)=v$ and $\alpha=1.087$. The destabilizing value $\alpha=1.087$ is called the Nyquist gain.



Fig. 2: Lurye System

| Test type | Circle | Tsypkin | Zames-Falb | Nyquist |
| :---: | :---: | :---: | :---: | :---: |
| max $\alpha$ guarantee | 0.6510 | 0.6510 | 1.0870 | 1.0870 |

TABLE I: Stability margins: Results from [18] for the Lurye system and nonlinearities with slope restricted to $[0,1]$.

Next, we used the condition in Theorem 1 to analyze the stability margin for the case when $\phi$ is the scalar ReLU. The Lurye system in Figure 2 is equivalent to the LFT representation $F_{U}(G, \phi)$ in Figure 1 using:

$$
G(z)=\left[\begin{array}{cc}
-G_{11}(z) \alpha & 1 \\
1 & 0
\end{array}\right]
$$

The Lurye system with ReLU is stable for a given value of $\alpha$ if the $\operatorname{LMI}\left(P, M, \gamma^{2}\right)<0$, defined in (17), is feasible for some $\gamma<\infty$. We solved for the largest feasible value of $\alpha$ using bisection using the ReLU QCs 3 The feasibility at each bisection step is a semidefinite program and was solved using CVX [33] as a front-end and SDPT3 [34], [35] as the solver. The bisection is initialized with $\underline{\alpha}=0$ and $\bar{\alpha}=200$. The bisection is terminated when $\bar{\alpha}-\underline{\alpha} \leq 10^{-3}(1+\bar{\alpha})$.

The top row of Table $\Pi$ shows the results as a function of the lifting horizon. For comparison, we also computed the stability margin using QCs defined by $M=\left[\begin{array}{cc}0 & Q_{0}^{\top} \\ Q_{0} & -\left(Q_{0}+Q_{0}^{\top}\right)\end{array}\right]$ where $Q_{0}$ is a doubly hyperdominant matrix. These results are shown in the second row of Table $\square$ Computational times are also given for each bisection to the stopping tolerance.

The doubly hyperdominant $\mathrm{QC}$ is the strongest possible constraint for $[0,1]$ slope restricted nonlinearities as discussed in Section IV-A This test corresponds to the circle criterion when $N=1$. The stability margin improves with the lifting horizon, getting to a maximum value of 0.8911 ,[^1]

| lift size $N$ | 1 | 2 | 5 | 8 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| ReLU: $\max \alpha$ | 0.6516 | 0.6516 | 4.2999 | 33.472 | 181.543 |
| DH: $\max \alpha$ | 0.6516 | 0.6516 | 0.8636 | 0.8820 | 0.8911 |
| ReLU Comp. (s) | 4.73 | 4.87 | 5.15 | 5.10 | 5.32 |
| DH Comp. (s) | 3.80 | 3.83 | 4.00 | 4.05 | 4.33 |

TABLE II: Stability margins (top): Results using the doubly hyperdominant $(\mathrm{DH})$ and ReLU QCs as a function of lifting horizon $N$. The ReLU QC exploits specific ReLU properties to significantly improve the stability margin. Computational times (bottom): given for each stability margin calculation.

but stays below the Nyquist value as expected. The ZamesFalb condition, given in Table provides the larger stability margin of 1.0870 than our lifted Lyapunov condition with the doubly hyperdominance $\mathrm{QC}$ for $N=12$.

More interestingly, the ReLU QC provides a stability margin that far exceeds the Nyquist value of 1.0870 as the lifting horizon $N$ increases, giving a maximum value of 181.543. This is possible because the ReLU QC exploits specific properties of the repeated ReLU that appears in the lifted system. To empirically verify this result, we simulated the the Lurye system with $\phi$ as the scalar $\operatorname{ReLU}, \alpha=100$, and 20 initial conditions for the state drawn from a $2 \times 1$ Gaussian distribution with standard deviation of 10. All simulations of the Lurye system with the ReLU converged back to the origin. This provides some independent validation of our stability margin results for the ReLU Lurye system.

## B. Gain Example

In this section, we used the condition in Theorem 11 to analyze the induced $\ell_{2}$-norm for a $\operatorname{ReLU} \operatorname{RNN} F_{U}(G, \Phi)$. The nominal part $G$ is a discrete-time, linear time-invariant (LTI) system given in (1) with the following state matrices:

$$
\begin{aligned}
& A=\left[\begin{array}{cccc}
0.84 & -0.17 & 0.10 & -0.04 \\
0.17 & 0.80 & -0.11 & -0.04 \\
0.05 & -0.11 & 0.90 & -0.08 \\
-0.04 & 0.18 & 0.01 & 0.74
\end{array}\right] \\
& B_{1}=\left[\begin{array}{cc}
-0.08 & -0.18 \\
-0.11 & 0.11 \\
-0.01 & -0.05 \\
-0.04 & 0.03
\end{array}\right], B_{2}=\left[\begin{array}{ccc}
-0.04 & 0.11 & 0.14 \\
-0.06 & 0.03 & -0.02 \\
0.02 & -0.03 & 0.01 \\
0.04 & -0.08 & 0.20
\end{array}\right] \\
& C_{1}=\left[\begin{array}{cccc}
-0.35 & -0.40 & -1.04 & 1.36 \\
0.90 & 0.55 & 1.13 & -0.46
\end{array}\right] \\
& C_{2}=\left[\begin{array}{cccc}
0.79 & -0.62 & -1.87 & -0.09 \\
-0.67 & -1.05 & 1.80 & -0.06 \\
2.25 & -1.08 & -0.36 & 1.08
\end{array}\right]
\end{aligned}
$$

The nonlinearity $\Phi$ has $n_{v}=2$ inputs and $n_{w}=2$ outputs. The dimensions of the disturbance and error channels are $n_{d}=3$ and $n_{e}=3$, respectively. The "best" gain bound $\gamma$ for a specific lifting horizon $N$ is obtained by minimizing $\gamma^{2}$ subject to the LMI constraint $L M I\left(P, M, \gamma^{2}\right)<0$, as defined in (17). There are additional (linear) constraints on the QC matrices in $M$, e.g. $\tilde{Q}$ is a Metzler matrix. This minimization is a semidefinite program and was solved using CVX [33] as a front-end and SDPT3 [34], [35] as the solver. The top row of Table $\square$ shows the results as a function of the lifting horizon. For comparison, we also computed a bound on the $\ell_{2}$ gain using QCs defined by $M=\left[\begin{array}{cc}0 & Q_{0}^{\top} \\ Q_{0} & -\left(Q_{0}+Q_{0}^{\top}\right)\end{array}\right]$ where $Q_{0}$ is a doubly hyperdominant matrix. These results are shown in the second row of Table IIII The doubly hyperdominant QC is the strongest possible constraint for $[0,1]$ slope restricted nonlinearities as discussed in Section IV-A The results gain bound obtained using the ReLU QC is better (smaller) as it exploits specific properties of the ReLU. Moreover, both results improve with the lifting horizon as the QCs can exploit couplings between the input/output data for the repeated nonlinearity. Computational times are also given to run each minimization. There is a mild growth in computation time with increasing horizon $N$ for this problem.

| lift size $N$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ReLU: gain bound | 7.556 | 5.530 | 3.932 | 3.466 | 3.247 | 3.128 |
| DH: gain bound | 34.379 | 13.450 | 7.992 | 5.844 | 4.811 | 4.263 |
| ReLU Comp. (s) | 0.82 | 0.44 | 0.48 | 0.52 | 0.91 | 1.25 |
| DH Comp. (s) | 0.28 | 0.28 | 0.29 | 0.36 | 0.47 | 0.61 |

TABLE III: Gain (top): $\ell_{2}$-gain upper-bounds given using ReLU and the doubly hyperdominant (DH) QCs as a function of lifting horizon $N$. The ReLU QC exploits specific ReLU properties to provide a significantly less conservative upperbound on the gain. Computational times (bottom): provided for each upper-bound solution.

## VI. ConClusions

This paper presents sufficient conditions for the stability and $\ell_{2}$-gain performance of RNNs with ReLU activation functions. These conditions are derived by combining Lyapunov/dissipativity theory with Quadratic Constraints (QCs) satisfied by repeated ReLUs. We use a "lifted" representation for the ReLU RNN to derive our stability and performance condition. Future work will consider the computational cost of this condition and scalability to larger RNNs. We will also study the theoretical properties as the lifting horizon $N$ tends to infinity.

## VII. ACKNOWLEDGMENTS

The authors acknowledge AFOSR Grant \#FA9550-23-10732 for funding of this work.

## REFERENCES

[1] J. Willems and R. Brockett, "Some new rearrangement inequalities having application in stability analysis," IEEE Transactions on Automatic Control, vol. 13, no. 5, pp. 539-549, October 1968.

[2] J. C. Willems, The analysis of feedback systems, ser. Research monographs. Cambridge, Mass.: M.I.T. Press, 1971, no. 62.

[3] V. Kulkarni and M. Safonov, "All multipliers for repeated monotone nonlinearities," IEEE Transactions on Automatic Control, vol. 47, no. 7, pp. 1209-1212, 2002.

[4] C. R. Richardson, M. C. Turner, and S. R. Gunn, "Strengthened circle and Popov criteria for the stability analysis of feedback systems with ReLU neural networks," IEEE Control Systems Letters, 2023.

[5] Y. Ebihara, H. Waki, V. Magron, N. H. A. Mai, D. Peaucelle, and S. Tarbouriech, " $\ell_{2}$ induced norm analysis of discrete-time LTI systems for nonnegative input signals and its application to stability analysis of recurrent neural networks," European Journal of Control, vol. 62, pp. 99-104, 2021.

[6] P. Khargonekar, K. Poolla, and A. Tannenbaum, "Robust control of linear time-invariant plants using periodic compensation," IEEE Transactions on Automatic Control, vol. 30, no. 11, pp. 1088-1096, 1985.

[7] J. Willems, "Dissipative dynamical systems part I: General theory," Archive for Rational Mech. and Analysis, vol. 45, no. 5, pp. 321-351, 1972.

[8] - , "Dissipative dynamical systems part II: Linear systems with quadratic supply rates," Archive for Rational Mech. and Analysis, vol. 45 , no. 5 , pp. 352-393, 1972.

[9] A. Schaft, $L_{2}$-gain and passivity in nonlinear control. Springer-Verlag New York, Inc., 1999.

[10] H. Khalil, Nonlinear Systems. Pearson, 2001.

[11] A. Megretski and A. Rantzer, "System analysis via integral quadratic constraints," IEEE Transactions on Automatic Control, vol. 42, no. 6, pp. 819-830, 1997.

[12] J. Veenman, C. Scherer, and H. Köroğlu, "Robust stability and performance analysis based on integral quadratic constraints," European Journal of Control, vol. 31, pp. 1-32, 2016.

[13] C. Scherer, "Dissipativity and integral quadratic constraints: Tailored computational robustness tests for complex interconnections," IEEE Control Systems Magazine, vol. 42, no. 3, pp. 115-139, 2022.

[14] P. Seiler, "Stability analysis with dissipation inequalities and integral quadratic constraints," IEEE Transactions on Automatic Control, vol. 60, no. 6, pp. 1704-1709, 2015.

[15] L. Lessard, B. Recht, and A. Packard, "Analysis and design of optimization algorithms via integral quadratic constraints," SIAM Journal on Optimization, vol. 26, no. 1, pp. 57-95, 2016.

[16] B. Lee and P. Seiler, "Finite step performance of first-order methods using interpolation conditions without function evaluations," 2020. [Online]. Available: https://arxiv.org/abs/2005.01825

[17] A. Taylor, B. Van Scoy, and L. Lessard, "Lyapunov functions for first-order methods: Tight automated convergence guarantees," in International Conference on Machine Learning. PMLR, 2018, pp. $4897-4906$.

[18] J. Carrasco, M. C. Turner, and W. P. Heath, "Zames-Falb multipliers for absolute stability: From O'Shea's contribution to convex searches," European Journal of Control, vol. 28, pp. 1-19, 2016.

[19] J. M. Fry, M. Farhood, and P. Seiler, "IQC-based robustness analysis of discrete-time linear time-varying systems," International Journal of Robust and Nonlinear Control, vol. 27, no. 16, pp. 3135-3157, 2017.

[20] B. Hu, M. J. Lacerda, and P. Seiler, "Robustness analysis of uncertain discrete-time systems with dissipation inequalities and integral quadratic constraints," International Journal of Robust and Nonlinear Control, vol. 27, no. 11, pp. 1940-1962, 2017.

[21] M. Fetzer and C. W. Scherer, "Absolute stability analysis of discrete time feedback interconnections," IFAC-PapersOnLine, vol. 50, no. 1, pp. 8447-8453, 2017.

[22] J. Carrasco, W. P. Heath, J. Zhang, N. S. Ahmad, and S. Wang, "Convex searches for discrete-time Zames-Falb multipliers," IEEE Transactions on Automatic Control, vol. 65, no. 11, pp. 4538-4553, 2019.

[23] B. Van Scoy and L. Lessard, "Absolute stability via lifting and interpolation," in IEEE Conference on Decision and Control. IEEE, 2022, pp. 6217-6223.

[24] J. Soykens, J. Vandewalle, and B. De Moor, "Lur'e systems with multilayer perceptron and recurrent neural networks: absolute stability and dissipativity," IEEE Transactions on Automatic Control, vol. 44, no. 4, pp. 770-774, 1999

[25] W. G. Y. Tan and Z. Wu, "Robust machine learning modeling for predictive control using Lipschitz-constrained neural networks," Computers \& Chemical Engineering, vol. 180, p. 108466, 2024.

[26] H. Yin, P. Seiler, and M. Arcak, "Stability analysis using quadratic constraints for systems with neural network controllers," IEEE Transactions on Automatic Control, vol. 67, no. 4, pp. 1980-1987, 2021.

[27] K. Zhou, J. C. Doyle, and K. Glover, Robust and Optimal Control. Prentice-Hall, 1996.

[28] G. Valmorbida, R. Drummond, and S. R. Duncan, "Regional analysis of slope-restricted Lurie systems," IEEE Transactions on Automatic Control, vol. 64, no. 3, pp. 1201-1208, 2018.

[29] L. Zaccarian and A. R. Teel, "A common framework for anti-windup, bumpless transfer and reliable designs," Automatica, vol. 38, no. 10, pp. $1735-1744,2002$.

[30] R. Drummond, M. C. Turner, and S. R. Duncan, "Reduced-order neural network synthesis with robustness guarantees," IEEE Transactions on Neural Networks and Learning Systems, vol. 35, no. 1, pp. 1182$1191,2024$.

[31] M. Fazlyab, M. Morari, and G. J. Pappas, "Safety verification and robustness analysis of neural networks via quadratic constraints and semidefinite programming," IEEE Transactions on Automatic Control, vol. 67, no. 1 , pp. $1-15,2020$.

[32] M. Vidyasagar, Nonlinear systems analysis. SIAM, 2002.
[33] M. Grant and S. Boyd, "CVX: Matlab software for disciplined convex programming, version 2.1," https://cvxr.com/cvx Mar. 2014.

[34] K.--C. Toh, M. J. Todd, and R. H. Tütüncü, "Sdpt3-a matlab software package for semidefinite programming, version 1.3," Optimization methods and software, vol. 11, no. 1-4, pp. 545-581, 1999.

[35] R. H. Tütüncü, K.-C. Toh, and M. J. Todd, "Solving semidefinitequadratic-linear programs using sdpt3," Mathematical programming, vol. 95 , pp. $189-217,2003$.

This figure "p1.jpg" is available in "jpg" format from: http://arxiv.org/ps/2405.05236v1


[^0]:    ${ }^{1}$ Theorem 1 in [3] is stated for repeated monotone nonlinearities. A similar fact holds for nonlinearities with slope restricted to $[0,1]$ by a transformation of the input-output data.

[^1]:    ${ }^{2}$ The results depend on the number of terms included in the Zames-Falb finite impulse response filter. This is the best (largest) reported value.

    ${ }^{3}$ Note that $\gamma$ appears in the $(3,3)$ block of the LMI in 17). A Schur complement argument can be used to conclude that feasibility for some $\gamma<\infty$ is equivalent to feasibility of the upper left two blocks. Hence our numerical implementation used bisection with only these upper left two blocks of the LMI.

