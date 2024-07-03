# Exploring Neural Network Landscapes: Star-Shaped And Geodesic Connectivity

Zhanran Lin∗1, Puheng Li∗2, and Lei Wu†3,4 1Department of Statistics and Data Science, Wharton School, University of Pennsylvania 2Department of Statistics, Stanford University 3School of Mathematical Sciences, Peking University 4Center for Machine Learning Research, Peking University April 10, 2024

## Abstract

One of the most intriguing findings in the structure of neural network landscape is the phenomenon of *mode connectivity* [FB17, DVSH18]: For two typical global minima, there exists a path connecting them without barrier. This concept of mode connectivity has played a crucial role in understanding important phenomena in deep learning.

In this paper, we conduct a fine-grained analysis of this connectivity phenomenon. First, we demonstrate that in the overparameterized case, the connecting path can be as simple as a *two-piece linear path*, and the path length can be nearly equal to the Euclidean distance. This finding suggests that the landscape should be nearly convex in a certain sense. Second, we uncover a surprising *star-shaped* connectivity: For a finite number of typical minima, there exists a center on minima manifold that connects all of them simultaneously via linear paths. These results are provably valid for linear networks and two-layer ReLU networks under a teacher-student setup, and are empirically supported by models trained on MNIST
and CIFAR-10.

## 1 Introduction

It is well-known that neural networks are highly non-convex, but they can still be efficiently trained by simple algorithms like stochastic gradient descent (SGD). Understanding the underlying mechanism is crucial and in particular, a key aspect of this is to uncover the topology and geometry of neural network landscapes.

Some recent studies exploited the local properties of neural network landscapes, including the absence of spurious minima [GLM16, SC16], the sharpness of different minima [HS97, KMN+17, WZE17], and the structures of saddle points [ZZLX21] and plateaus [AS21]. Other studies have examined the nonlocal structures, including the impact of symmetries and invariances [SGJ+21],
the presence of non-attracting regions of minima [PS21], the monotonic linear interpolation arXiv:2404.06391v1 [cs.LG] 9 Apr 2024 phenomenon [GVS14, WWZG22, VF22, LBZ+21]. Among these nonlocal structures, one of the most intriguing findings is the *mode connectivity*, which is the focus of this paper.

Mode connectivity refers to the property that global minima of (over-parameterized) neural networks are (nearly) path-connected and form a connected manifold [Coo18], rather than being isolated. This characteristic of neural network landscape was first observed by Freeman and Bruna in [FB17], and its practical universality was later demonstrated in [DVSH18, GIP+18]
through extensive large-scale experiments. Mode connectivity has attracted wide attention and has been utilized to understand many important aspects of deep learning, including the role of permutation invariance [ESSN21, AHS22], properties of SGD solutions [MFG+20, FDRC20], explaining the success of certain learning methods such as ensemble methods [GIP+18, HHY19],
and even to design methods with better generalization [BMLW21].

In this paper, we conduct a fine-grained analysis of this mode connectivity. Our specific investigation is inspired by the empirical observation that the connecting paths can be piecewise linear with as few as two pieces [GIP+18]. This motivates us to examine the piecewise linear connectivity of the global minima manifold. Two minima are said to be k-piece linearly connected if they can be connected using paths with at most k linear segments. Specifically, our main contributions are summarized as follows.

- We provide a theoretical analysis of the piecewise linear connectivity for two-layer ReLU
networks and linear networks under a teacher-student setup. We prove that as long as the network is sufficiently over-parameterized, any two minima are 2-piece linearly connected.

By exploiting this property, we further discover the following surprising structures of the global minima manifold:
- Star-shaped connectivity: For a finite set of typical minima, there exists a minimum (center) such that it is linearly connected to all these minima simultaneously. - Geodesic connectivity: For two typical minima, the geodesic distance on the minima manifold is close to the Euclidean distance. Moreover, the ratio between them monotonically decreases towards 1 as increasing the network width. This suggests that the landscape of over-parameterized networks might be not far away from a convex one in some sense.

- We then provide extensive experiments on MNIST and CIFAR-10 datasets that confirm our theoretical findings on practical models.

## 1.1 Related Works

Understanding the mode connectivity. There have been several studies that aim to theoretically explain the phenomenon of mode connectivity. The initial work by Freeman and Bruna
[FB17] proved the mode connectivity for both linear networks and two-layer ReLU networks when the model is regularized by squared ℓ2 norm. [GIP+18] empirically discovered that connecting paths can be piecewise linear. Based on this observation, [KWL+19] proved that if two minima satisfy certain conditions such as the dropout stability and noise stability, then they can be connected using paths with at most 10 linear segments. Moreover, the result in [KWL+19] is applicable to deep neural networks. [SM20] provided a theoretical explanation of why SGD tends to find solutions that satisfy the dropout stability for two-layer neural networks. In addition to these studies, [NMH18, NBM21a, NBM21b] investigated how the connectivity depends on the network width and depth, but the analysis does not provide any information about the structure

![2_image_0.png](2_image_0.png)

of the connecting paths. In contrast, we investigate the particular structure of connecting paths and provide both empirical and theoretical evidence showing that when networks are sufficiently over-parameterized, typical minima can be connected using paths of merely 2 linear segment.

Moreover, we also explore the geometry of the global minima manifold by using the simplicity of connecting paths. Critical points. [FYMT19, ZZLX21] studied the hierarchical structures of critical points and in particular, how local minima degenerate to saddle points when increasing the number of neurons. [RABC19, MAB20] provided an analytical characterization of the distribution of critical points for learning a single neuron in an asymptotic regime by using the Kac-Rice replicated method from statistical physics. [AS21, FA00, YO19] studied the appearance of plateaus in the neural network landscape and its impact on the training process. In addition, it has been always a major problem to understand under what conditions bad local minima/valley disappear
[Kaw16, SC16, LSLS18, LSZ22] or not [AHW95, SS18, YSJ18, DLS22, LK17]. Another line of works inspects curvatures at minima [SEG+17] and how the curvatures of the local landscape are related to the generalization of networks represented by those minima [HS97, WZE17, JKA+17, MY21, WWS]. In this paper, we study the topology and geometry of global minima by utilizing the mode connectivity.

Nonlocal structures. Note that the mode connectivity is nonlocal in nature. Therefore, our work is also helpful for understanding the nonlocal structures of the neural network landscape. [FJ19] proposed a phenomenological model (a set of high dimensional wedges) to study large-scale structures of neural network landscape. [GVS14] discovered the surprising monotonic linear interpolation (MLI) phenomenon: the loss often decreases monotonically in the linear interpolation between random initialization and minima found by SGD. [WWZG22, VF22, LBZ+21] provided theoretical analyses of MLI phenomenon. [Coo18] proved that in the over-parameterized case, global minima form a high-dimensional manifold and this minima manifold is path connected as implied by the mode connectivity phenomenon [GIP+18, FB17, DVSH18]. Recently, [ALL+23]
showed a star-shaped structure in the regime of the spherical negative perceptron. We instead provide both theoretical and empirical evidence, showing that star-shaped structure also exists for neural networks.

## 2 Preliminaries

Notation. For an integer n, let [n] = {1, 2*, . . . , n*}. For a compact Ω, denote by Unif(Ω) the uniform distribution over Ω. Let S
d−1 = {x ∈ R
d: ∥x∥2 = 1} and τd−1 = Unif(S
d−1). Denote by {ej}
d j=1 the canonical basis of R
d.

Let f : X ×Θ *7→ Y* be a neural network with X and Θ denoting the input space and parameter space, respectively. Let ℓ : *Y × Y 7→* R be a loss function. Then the loss landscape is determined by R(θ) = E(x,y)∼D[ℓ(f(x; θ), y)], where D denotes the input distribution. In this paper, we make the over-parameterization assumption: infθ∈Θ R(θ) = 0. Then, the global minima manifold is given by M = {θ ∈ Θ : R(θ) = 0}. (1)
For any θ1, θ2 ∈ M, denote by Pθ1,θ2 the space of paths on M connecting θ1 and θ2:

$\operatorname{tg}\,\theta_1$ and $\theta_2$:. 
$${\mathcal{P}}_{\theta_{1},\theta_{2}}=\left\{\gamma:[0,1]\mapsto{\mathcal{M}}\,|\,\gamma(0)=\theta_{1},\gamma(1)=\theta_{2}\right\}.$$
Existing works on mode connectivity imply that under some conditions, M is path connected, i.e., Pθ1,θ2
̸= ∅ for typical θ1, θ2 ∈ M. In this paper, we make a refined analysis of the connectivity.

To be rigorous, we formalize some concepts that we shall use throughout this paper below.

Definition 1 (Linear interpolation). For any θ1, θ2 ∈ Θ, denote by γ lin θ1,θ2
: [0, 1] → Θ the linear interpolation path defined as γ(t) = tθ1 + (1 − t)θ2, t ∈ [0, 1].

Definition 2 (k-piece linear connectivity). For any θ1, θ2 ∈ M, we write θ1 ↔ θ2 if γ lin θ1,θ2
⊂ M.

We say θ1 and θ2 are k-piece linearly (k-PL) connected if there exist β1, . . . , βk−1 ∈ M such that θ1 ↔ β1 *↔ · · · ↔* βk−1 ↔ θ2. Particularly, the case of k = 1 is referred to as linear connectivity.

Definition 3 (Star-shaped linear connectivity). For multiple minima S = {θi}
r i=1 ⊂ M, we refer to the star-shaped linear connectivity as there exists a θ
∗ ∈ M such that θi ↔ θ
∗for all i = 1, 2*, . . . , r*. Specifically, θ
∗ and S are said to be the *center* and feet, respectively.

In this paper, we also consider another quantity to measure the strength of connectivity.

Definition 4 (Normalized geodesic distance (NGD)). For any θ1, θ2 ∈ M, define the normalized geodesic distance between θ1 and θ2 by

$$G(\theta_{1},\theta_{2})={\frac{\operatorname*{inf}_{\gamma\in{\mathcal{P}}_{\theta_{1},\theta_{2}}}\int_{0}^{1}\|\gamma^{\prime}(t)\|_{2}\,\mathrm{d}t}{\|\theta_{1}-\theta_{2}\|_{2}}}.$$

$$G(\theta_{1},\theta_{2})=+\infty.$$
. (2)
If Pθ1,θ2 is an empty set, set G(θ1, θ2) = +∞.

If the landscape is convex, it is trivial that the NGD is exactly 1 for any pair of global minima since the geodesic is simply the linear interpolation. However, for nonconvex landscapes, the NGD is always strictly greater than 1. The value of NGD can serve as a factor to quantify the degree of non-convexity. If the NGD keeps close to 1 for any pair of minima, then the landscape should be somehow as benign as a convex one. Otherwise, the landscape must be highly nonconvex. We are particularly interested in how the value of NGD changes as increasing the level of over-parameterization.

$$\left(2\right)$$

## 3 Two-Layer Relu Networks

We first consider the two-layer ReLU network under a teacher-student setup, where the label is generated by a teacher network: f
∗(x) = PM
j=1 σ(w∗
j
·x). Here the activation function σ : R 7→ R
is given by σ(z) := max(0, z). We make the following assumption.

Assumption 5. Suppose M ≤ d, w∗
j = ej for j = 1*, . . . , M*, and x ∼ τd−1.

By the rotational symmetry, the specific assumption that w∗
j = ej for j = 1*, . . . , M* is equivalent to only assume {w∗
j
}M
j=1 to be orthonormal. However, we will focus on Assumption 5 to make our statement more succinct. In such a case, the loss objective can be rewritten as

$${\cal R}(\theta)=\mathbb{E}_{{\bf x}\sim r_{d-1}}\left[\left(\sum_{i=1}^{m}\sigma\left({\bf w}_{i}\cdot{\bf x}\right)-\sum_{i=1}^{M}\sigma\left(x_{i}\right)\right)^{2}\right],\tag{3}$$

where m denotes the number of neurons of the student network and θ = (w1, w2*, . . . ,* wm)
T =
(wi,j ) ∈ R
m×d. Using this notation, each row of W represents a student neuron.

Assumption 5 allows us to obtain the following analytic characterization of the global minima manifold. This characterization will play a critical role in our theoretical analysis and might be of independent interest to other related problems as well.

Theorem 6. Suppose that m ≥ M and Assumption 5 hold. Let S0 = {(0*, . . . ,* 0) ∈ R
d},
Sj = {αej : α ̸= 0} for j ∈ [M], and S = ∪M
j=0Sj . Then the global minima manifold M is a compact set in R
m×d:

$$\mathcal{M}=\left\{\theta=\left(\mathbf{w}_{1},\ldots,\mathbf{w}_{m}\right)^{T}\in\mathbb{R}^{m\times d}\ :\ \forall\,i\in[m],\mathbf{w}_{i}\in S\ \text{and}\ \forall\,j\in[M],\sum_{i=1}^{m}w_{i,j}=1\right\}\tag{4}$$

The proof is deferred to Appendix A.1. Note that Sj ∩ Sk = ∅ for any j ̸= k ∈ {0, 1*, . . . , M*}.

Hence Theorem 6 implies the following facts about the global minima:

- There are at most m+1 types of student neurons, represented by S0, S1*, . . . , S*M, regardless of how overparameterized the student network is. Moreover, for any j ∈ [M], there exists at least one student neuron taking the type of Sj .

- For each neuron, there exists at most one coordinate to be nonzero and the coordinates from M + 1 to d must be zero.
The following lemma provides a precise condition of when two global minima are linearly connected, which will be used in our subsequent analysis.

Lemma 7 (Linear connectivity). *For any two global minima* θ
(1) = (w
(1)
1*, . . . ,* w
(1)
m )
T,
θ
(2) = (w
(2)
1*, . . . ,* w
(2)
m )
T ∈ R
m×d*, we have* W(1) ↔ W(2) if and only for any i ∈ {1, . . . , m}, one of the following happens:
- w
(1)
i ∈ S0 or w
(2)
i ∈ S0;
- there exists j ∈ {1, . . . , M} *such that* w

$${\bf w}_{i}^{(1)}\in S_{j}\,\,a n d\,\,{\bf w}_{i}^{(2)}\in S_{j}.$$

The above lemma (proof deferred to Appendix A.1) means that if θ1 ↔ θ2, then for any i ∈ [m], the nonzero coordinates of w
(1)
iand w
(2)
i must be the same if they are not zero simultaneously.

## 3.1 The K-Piece Linear Connectivity

Theorem 8. Suppose m > M *and two minima* θ
(1), θ
(2) *are i.i.d. drawn from* Unif(M). Then, w.p. at least pm,M = 1 − M(
M2−1 M2 )
m−2M, θ
(1) and θ
(2) are 2*-PL connected.*
The proof of this theorem can be found in Appendix A.2. Notice that the probability pm,M → 1 as m → ∞, implying that when the student is sufficiently over-parameterized, the 2-PL connectivity holds with probability nearly 1. Quantitatively speaking, for any δ ∈ (0, 1),
m ≥ CM2log(M/δ) is sufficient to guarantee that the probability of 2-PL connectivity is no less than 1 − δ.

The following theorem further shows that if allowing the number of pieces to be slightly larger, then the k-PL connectivity holds for two global minima.

Theorem 9. Suppose m ≥ 2M − 1, then any two global minima are 4*-PL connected.*
The proof is deferred to Appendix A.3.

## 3.2 Star-Shaped Connectivity

Theorem 10. Suppose m > M and let θ1, θ2 *be two minima i.i.d. drawn from* Unif(M). Then, w.p. at least 1 − M(
Mk−1 Mk )
m−kM*, there exists a center* θ
∗ ∈ M *such that* θ i ↔ θ
∗*for all* i ∈ [k].

A simple calculation implies that to ensure the probability larger than 1 − δ, we need m ≥
CMklog(M/δ). The following theorem shows by allowing the connectivity between feet and the center to be two-piece linear path, then the probability becomes exactly 1 as long as m ≥ kM.

Theorem 11. Given k ∈ N, suppose m ≥ kM. For any k global minima θ1, . . . , θk, we can find a center θ
∗*such that* θ
∗ and θi are 2*-PL connected for any* i = 1*, . . . , k*.

The proofs of Theorem 10 and Theorem 11 can be found in Appendix A.4 and A.5, respectively. In Figure 2, we provide an illustration of the difference in how the feet are connected to the star center between Theorem 10 and Theorem 11.

![5_image_0.png](5_image_0.png)

## 3.3 The Geodesic Connectivity

The left of Figure 3 shows the normalized geodesic distances (NGDs) between minima found by SGD for the two-layer ReLU networks mentioned above. We can see clearly that the value of NGD decreases monotonically towards 1 as the network width m increases. This implies that the landscape of wide networks should be somehow not far from a convex one. This is consistent with our intuition that wider networks should have a simpler landscape than narrow networks. Below, we provide some theoretical evidence to explain this mysterious phenomenon.

![6_image_0.png](6_image_0.png) 

Theorem 12. Suppose m > M, and let θ1, θ2 *be two minima independently drawn from* Unif(M).

Then there exists absolute constants c1, c2 > 0 *such that w.p. at least* 1 − c1e
−m that G(θ1, θ2) ≤
c2
√M*. Moreover, the upper bound can be achieved by a two-piece linear path.*
The proof is deferred to Appendix A.6. This theorem shows that the NGD between uniformly sampled minima is independent of the level of over-parameterization. However, Figure 3 shows that NGD shrinks to 1 when increasing the network width for minima found by SGD. We hypothesize that SGD induces a biased distribution over the minima manifold. In the right of Figure 3, we visualize the magnitude of different neurons for an SGD solution. We observe that SGD tends to find solutions with sparse structures, i.e., only a few dominant neurons contribute.

To study the influence of neuron sparsity on the geodesic connectivity, we define the following distribution to formulate the sparsity bias.

Definition 13 (Neuron-sparse distribution). For any absolute constant 0 *< r <* 1, we define SP(M, r), the neuron-sparse distribution with a sparsity r over M, as following: for θ = (w1*, . . . ,* wm)
T, for any i ∈ {1*, . . . , m*}, P(wi ∈ S0) = r and P(wi ∈ Sj ) = 1−r M for j ∈ {1*, . . . , M*}.

Theorem 14. Suppose m > M and let θ1, θ2 *be two minima independently drawn from* SP(M, r).

Then there exists two absolute constants c1, c2 > 0 such that w.p.at least 1 − c1Me−mr2*that* G(θ1, θ2) ≤ 1 + c2 r
√m
. Moreover, the upper bound can be achieved by a two-piece linear path.

The proof is deferred to Appendix A.7. This theorem demonstrates that the bias towards sparse solutions can explain the shrinkage of NGD to 1. In particular, when m → ∞, NGD
approaches to 1.

## 4 Linear Networks

A linear network f(·; θ) : R
d7→ R is parameterized by f(x; θ) = ALAL−1 *. . . A*1x, where Al ∈
R

ml×ml−1 for l = 1, 2*, . . . , L*. Here L denotes the network depth and {ml}
L
l=0 denotes the widths.

Note that m0 = d and mL = 1 and we assume m2 = *· · ·* = mL−1 = m for simplicity. We make the following assumption on the data distribution.

Assumption 15. Suppose that y = Qx for some Q ∈ R
1×d, E[x] = 0, and λmin(E[xxT]) > 0.

The above assumption is quite mild but ensures that the global minima manifold has the following analytic characterization:
M = {(AL, AL−1*, . . . , A*1) : ALAL−1 *· · ·* A1 = Q} (5)
The following theorem provides the characterization of k-PL connectivity of the loss landscape of linear networks. The proof can be found in Appendix B.

Theorem 16. Let f(·; θ) be the linear network described in Section 4. Let θ1, θ2 ∈ M be two global minima. If m > 2L − 1*, then we have:*
- *Two global minima are almost surely 2-PL connected;*

- Any two global minima are 3*-PL connected,*
We remark that the "almost surely" condition in characterizing the 2-PL connectivity cannot be removed. The following lemma provides a counterexample, showing that there indeed exist pathological minima that are not 2-PL connected.

Lemma 17. *Consider the case of* m = 4, d = 1, L = 2 and the target y = x. Then, we have M = {(*a, b*) ∈ R
m ⊗ R
m : a Tb = 1}*. Consider two global minima* θ1 = (A
(1)
1, A(2)
1),
θ2 = (A
(1)
2, A(2)
2) *with* A
(1)
1 = (1, 0, 0, 0), A(1)
2 = (1, 0, 0, 0)T, A(2)
1 = (−1, 0, 0, 0), A(2)
2 = (−1, 0, 0, 0)T.

Then, θ1 and θ2 are not 2*-PL connected. Quantitatively,*

$$\operatorname*{inf}_{\theta\in\mathcal{M}}\left(\int_{0}^{1}\mathcal{R}(t\theta_{1}+(1-t)\theta)\,\mathrm{d}t+\int_{0}^{1}\mathcal{R}(t\theta_{2}+(1-t)\theta)\right)\mathrm{d}t\geq\frac{4}{15}\mathbb{E}x^{2}.$$

Theorem 18 (star-shaped linear connectivity). Consider linear networks of depth L *and width* m*. Let* {θi}
r i=1 be r global minima. If m > 1 + r(L − 1), then we almost surely (with respect to the Lebesgue measure over M⊗r*) have that there exist a* θ
∗ ∈ M *such that* θ
∗ ↔ θi *for all* i = 1*, . . . , r*.

Here M⊗r = {(θ1*, . . . , θ*r) ∈ R
r: θi ∈ M for i ∈ [r]}. This theorem establishes that when linear networks are sufficiently wide, the star-shaped connectivity holds almost surely. The proof can be found in Appendix B.1.

The geodesic connectivity. In Figure 4, we empirically demonstrate that the Normalized Geodesic Distances (NGDs) for linear networks are also close to 1. Additionally, we observe that the NGD monotonically decreases with increasing network width, although this phenomenon has not yet been theoretically proven.

![8_image_0.png](8_image_0.png)

## 5 Experiments

In this section, we provide experiments to validate the star-shaped and geodesic connectivity across a range of architectures and datasets.

The center-finding algorithm. Given a set of minima S = {θ
∗
i
}
r i=1, to find a center θ that connects to all of them via linear paths, we propose to minimize the following objective

$${\mathcal J}_{S}(\theta):={\frac{1}{r}}\sum_{i=1}^{r}\left(\mathbb{E}_{t\sim U[0,1]}[{\mathcal R}(t\theta+(1-t)\theta_{i}^{*})]+\lambda p(\theta,\theta_{i}^{*})\right),$$

where p(·, ·) is a penalization function to be determined later. To efficiently solve this optimization problem, we use the Adam [KB14] optimizer with the minibatch gradient:

$$\nabla\widehat{\mathcal{J}}_{S}(\theta)=\nabla\left(\frac{1}{B_{r}B_{t}}\sum_{k=1}^{B_{r}}\sum_{j=1}^{B_{t}}\mathcal{R}(t_{j}\theta_{t}+(1-t_{j})\theta_{t_{k}}^{*})+\frac{\lambda}{B_{r}}\sum_{k=1}^{B_{r}}p(\theta_{t},\theta_{t_{k}}^{*})\right),\tag{7}$$
$$({\mathfrak{h}})$$
$$({\mathfrak{S}})$$

where ik i.i.d. ∼ Unif([r]) and tj i.i.d. ∼ Unif([0, 1]) for k ∈ [Br] and j ∈ [Bt]. Here, Br, Bt ∈ N denote the batch sizes. Across all our experiments, we always set Br = 1, Bt = 3.

Estimating the normalized geodesic distance. Given two minima θ
∗
1 and θ
∗
2
, we first find a center ˜θ ∈ M by minimizing the objective (6) for S = {θ
∗
1
, θ∗
2
} and p(*θ, θ*′) = ∥θ − θ
′∥
22
. This allows us to find a minimum on the minima manifold such that it connects to both θ
∗
1 and θ
∗
2 via the shortest linear paths. Moreover, by Definition 4, it holds for any θ ∈ M, satisfying θ ↔ θ
∗
i for i = 1, 2, that

$$G(\theta_{1}^{*},\theta_{2}^{*})\leq\frac{\|\theta_{1}^{*}-\theta\|_{2}+\|\theta-\theta_{2}^{*}\|_{2}}{\|\theta_{1}^{*}-\theta_{2}^{*}\|_{2}}.$$
. (8)
Then, plugging ˜θ into the right hand side of (8) gives an upper bound of G(θ
∗
1
, θ∗
2
).

The experiment setup. To validate our theoretical findings for practical models, we train fully-connected neural networks (FNNs) and VGG16 [SZ14] for classifying MNIST [LBBH98]
dataset, and VGG16 [SZ14] and ResNet34 [HZRS16] for classifying CIFAR-10 [KH+09] dataset, respectively:

G The FNN is three-layer, whose architecture is 728 -> 500 -> 300 -> 10. We trained FNNs under the hyperparameters: Ir = 1e-3 and batchsize = 200, G The architecture of VGG16 and ResNet34 can be found in [SZ14] and [HZRS16], respectively. We trained VGG16 and ResNet34 under the hyperparameters: 1r = 5e-3 and batchsize = 200.
As for the center-finding algorithm, we set B t = 1, B t = 3 as mentioned above, and learning rate η = 0.01. For all cases, the Adam optimizer [KB14] is adopted.

## 5.1 Star-Shaped Connectivity

In Figure 5, we visualize the star-shaped connectivity for VGG-16 in classifying the CIFAR10 dataset. We independently train the model to find 3 minima { θ ∗ } 2 =1 and then run the centerfinding algorithm to locate a center θ c + on the minima manifold.  We can see that the linear interpolation between any pair minima among the three ones indeed encounters a very high barrier. However, through the center θ c , the three minima form a star-shaped connectivity.

In Table 1, we provide more experiments for a variety of model aritectures and training datasets. We can see that the star-shaped connectivity holds for all scenarios examined.

![9_image_0.png](9_image_0.png)

Loss

| MNIST                        | CIFAR10   |         |          |         |
|------------------------------|-----------|---------|----------|---------|
| VGG16                        | FNN       | VGG16   | ResNet34 |         |
| Loss Barrier (linear)        | 16.91     | 1.25    | 6.21     | 3.28    |
| Loss Barrier (fold-line)     | 3.1e-05   | 1.1e-03 | 5.0e-03  | 1.0e-02 |
| MNIST                        | CIFAR10   |         |          |         |
| VGG16                        | FNN       | VGG16   | ResNet34 |         |
| Accuracy Barrier (linear)    | 28.55%    | 68.09%  | 10.79%   | 41.21%  |
| Accuracy Barrier (fold-line) | 100.00%   | 99.96%  | 99.99%   | 99.65%  |

Table 1: For different models and datasets, we independently trained 5 minima using Adam optimizer. Then, we run the path-finding algorithm with Br = 1, Bt = 3 for 200 epochs. For all the 10 linear interpolations between minima, and all the 10 "minimum-center-minimum" fold-lines constructed by two linear interpolations, we computed the maximum (for loss)
or minimum (for accuracy) and averaged them, which is denoted as "barrier". It is shown that there is nearly no barrier on the fold-lines we constructed, which validates that our observation of star-shaped connectivity holds for a wide range of settings.

## 5.2 The Geodesic Connectivity

In Table 2, we report the NGDs estimated by the aforementioned algorithm. It is demonstrated that minima (found by the commonly-used Adam optimizers) can be connected via paths whose NGDs are nearly 1. This is consistent with our theoretical findings in toy models.

| FNN+MNIST   | VGG16+MNIST   | VGG16+CIFAR10   | ResNet18+CIFAR10   |        |
|-------------|---------------|-----------------|--------------------|--------|
| NGD         | 1.003         | 1.001           | 1.051              | 1.003  |
| Barrier     | 99.89%        | 99.25%          | 99.91%             | 99.63% |

Table 2: The upper bound of NGD estimated via Eq. 8 for different networks and datasets.

We independently trained 2 minima in each setting, then trained the center via the centerfinding algorithm with a penalized term. It turns out that we can obtain great linear mode connectivity via a fold-line, as well as keeping the relative distance proportion controlled.

## 6 Conclusion

In this paper, we systematically investigate the star-shaped and geodesic connectivity phenomenon for the landscape of neural networks. We provide theoretical analysis on toy models such as two-layer ReLU networks and linear networks, as well as experimental validations on popular networks trained on MNIST and CIFAR-10 datasets. Our findings reveal that the neural network landscape has many simple structures. Specifically, the star-shaped phenomenon suggests a connectivity property stronger than mode connectivity. The geodesic connectivity indicates that the loss landscape might be not far from being convex in a certain sense. For future work, it would be interesting to explore the potential relationships between our findings and optimization and generalization in neural networks.

## Acknowledgements

The work is supported by the National Key R&D Program of China (No. 2022YFA1008200) and National Natural Science Foundation of China (No. 12288101).

## References

[AHS22] Samuel K Ainsworth, Jonathan Hayase, and Siddhartha Srinivasa, *Git re-basin: Merging* models modulo permutation symmetries, arXiv preprint arXiv:2209.04836 (2022).

[AHW95] Peter Auer, Mark Herbster, and Manfred KK Warmuth, *Exponentially many local minima* for single neurons, Advances in Neural Information Processing Systems, vol. 8, 1995.

[ALL+23] Brandon Livio Annesi, Clarissa Lauditi, Carlo Lucibello, Enrico M Malatesta, Gabriele Perugini, Fabrizio Pittorino, and Luca Saglietti, *Star-shaped space of solutions of the spherical* negative perceptron, Physical Review Letters 131 (2023), no. 22, 227301.

[AS21] Mark Ainsworth and Yeonjong Shin, *Plateau phenomenon in gradient descent training of* relu networks: Explanation, quantification, and avoidance, SIAM Journal on Scientific Computing 43 (2021), no. 5, A3438–A3468.

[BMLW21] Gregory Benton, Wesley Maddox, Sanae Lotfi, and Andrew Gordon Gordon Wilson, *Loss* surface simplexes for mode connecting volumes and fast ensembling, International Conference on Machine Learning, PMLR, 2021, pp. 769–779.

[Coo18] Yaim Cooper, *The loss landscape of overparameterized neural networks*, arXiv preprint arXiv:1804.10200 (2018).

[DLS22] Tian Ding, Dawei Li, and Ruoyu Sun, *Suboptimal local minima exist for wide neural networks* with smooth activations, Mathematics of Operations Research (2022).

[DVSH18] Felix Draxler, Kambis Veschgini, Manfred Salmhofer, and Fred Hamprecht, Essentially no barriers in neural network energy landscape, International Conference on Machine Learning, PMLR, 2018, pp. 1309–1318.

[ESSN21] Rahim Entezari, Hanie Sedghi, Olga Saukh, and Behnam Neyshabur, *The role of permutation invariance in linear mode connectivity of neural networks*, International Conference on Learning Representations, 2021.

[FA00] Kenji Fukumizu and Shun-ichi Amari, Local minima and plateaus in hierarchical structures of multilayer perceptrons, Neural Networks 13 (2000), no. 3, 317–327.

[FB17] C Daniel Freeman and Joan Bruna, *Topology and geometry of half-rectified network optimization*, 5th International Conference on Learning Representations, 2017.

[FDRC20] Jonathan Frankle, Gintare Karolina Dziugaite, Daniel Roy, and Michael Carbin, Linear mode connectivity and the lottery ticket hypothesis, International Conference on Machine Learning, PMLR, 2020, pp. 3259–3269.

[FJ19] Stanislav Fort and Stanislaw Jastrzebski, *Large scale structure of neural network loss landscapes*, Advances in Neural Information Processing Systems 32 (2019).

[FYMT19] Kenji Fukumizu, Shoichiro Yamaguchi, Yoh-ichi Mototake, and Mirai Tanaka, *Semi-flat* minima and saddle points by embedding neural networks to overparameterization, Advances in Neural Information Processing Systems 32 (2019).

[GIP+18] Timur Garipov, Pavel Izmailov, Dmitrii Podoprikhin, Dmitry P Vetrov, and Andrew G
Wilson, *Loss surfaces, mode connectivity, and fast ensembling of DNNs*, Advances in Neural Information Processing Systems 31 (2018).

[GLM16] Rong Ge, Jason D Lee, and Tengyu Ma, *Matrix completion has no spurious local minimum*,
Advances in Neural Information Processing Systems 29 (2016).

[GVS14] Ian J Goodfellow, Oriol Vinyals, and Andrew M Saxe, Qualitatively characterizing neural network optimization problems, arXiv preprint arXiv:1412.6544 (2014).

[HHY19] Haowei He, Gao Huang, and Yang Yuan, Asymmetric valleys: Beyond sharp and flat local minima, Advances in Neural Information Processing Systems 32 (2019).

[HS97] Sepp Hochreiter and Jürgen Schmidhuber, *Flat minima*, Neural Computation 9 (1997), no. 1, 1–42.

[HZRS16] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun, *Deep residual learning for image* recognition, Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, pp. 770–778.

[JKA+17] Stanisław Jastrzębski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua Bengio, and Amos Storkey, *Three factors influencing minima in SGD*, arXiv preprint arXiv:1711.04623 (2017).

[Kaw16] Kenji Kawaguchi, *Deep learning without poor local minima*, Advances in Neural Information Processing Systems 29 (2016).

[KB14] Diederik P Kingma and Jimmy Ba, *Adam: A method for stochastic optimization*, arXiv preprint arXiv:1412.6980 (2014).

[KH+09] Alex Krizhevsky, Geoffrey Hinton, et al., Learning multiple layers of features from tiny images, 2009.

[KMN+17] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang, *On large-batch training for deep learning: Generalization gap and sharp* minima, International Conference on Learning Representations, 2017.

[KWL+19] Rohith Kuditipudi, Xiang Wang, Holden Lee, Yi Zhang, Zhiyuan Li, Wei Hu, Rong Ge, and Sanjeev Arora, *Explaining landscape connectivity of low-cost solutions for multilayer nets*,
Advances in Neural Information Processing Systems 32 (2019).

[LBBH98] Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner, *Gradient-based learning* applied to document recognition, Proceedings of the IEEE 86 (1998), no. 11, 2278–2324.

[LBZ+21] James R Lucas, Juhan Bae, Michael R Zhang, Stanislav Fort, Richard Zemel, and Roger B
Grosse, *On monotonic linear interpolation of neural network parameters*, Proceedings of the 38th International Conference on Machine Learning, vol. 139, PMLR, 18–24 Jul 2021, pp. 7168–7179.

[LK17] Haihao Lu and Kenji Kawaguchi, *Depth creates no bad local minima*, arXiv preprint arXiv:1702.08580 (2017).

[LSLS18] Shiyu Liang, Ruoyu Sun, Jason D Lee, and Rayadurgam Srikant, *Adding one neuron can* eliminate all bad local minima, Advances in Neural Information Processing Systems 31
(2018).

[LSZ22] Dachao Lin, Ruoyu Sun, and Zhihua Zhang, *On the landscape of one-hidden-layer sparse* networks and beyond, Artificial Intelligence (2022), 103739.

[MAB20] Antoine Maillard, Gérard Ben Arous, and Giulio Biroli, *Landscape complexity for the empirical risk of generalized linear models*, Mathematical and Scientific Machine Learning, PMLR,
2020, pp. 287–327.

[MFG+20] Seyed Iman Mirzadeh, Mehrdad Farajtabar, Dilan Gorur, Razvan Pascanu, and Hassan Ghasemzadeh, *Linear mode connectivity in multitask and continual learning*, International Conference on Learning Representations, 2020.

[MY21] Chao Ma and Lexing Ying, *On linear stability of SGD and input-smoothness of neural networks*, Advances in Neural Information Processing Systems 34 (2021), 16805–16817.

[NBM21a] Quynh Nguyen, Pierre Bréchet, and Marco Mondelli, On connectivity of solutions in deep learning: The role of over-parameterization and feature quality, Advances in Neural Information Processing Systems 34 (2021).

[NBM21b] Quynh N Nguyen, Pierre Bréchet, and Marco Mondelli, When are solutions connected in deep networks?, Advances in Neural Information Processing Systems 34 (2021), 20956–20969.

[NMH18] Quynh Nguyen, Mahesh Chandra Mukkamala, and Matthias Hein, *On the loss landscape* of a class of deep neural networks with no bad local valleys, International Conference on Learning Representations, 2018.

[PS21] Henning Petzka and Cristian Sminchisescu, Non-attracting regions of local minima in deep and wide neural networks., Journal of Machine Learning Research 22 (2021), 143–1.

[RABC19] Valentina Ros, Gerard Ben Arous, Giulio Biroli, and Chiara Cammarota, *Complex energy* landscapes in spiked-tensor and simple glassy models: Ruggedness, arrangements of local minima, and phase transitions, Physical Review X 9 (2019), no. 1, 011003.

[SC16] Daniel Soudry and Yair Carmon, *No bad local minima: Data independent training error* guarantees for multilayer neural networks, arXiv preprint arXiv:1605.08361 (2016).

[SEG+17] Levent Sagun, Utku Evci, V Ugur Guney, Yann Dauphin, and Leon Bottou, *Empirical analysis of the hessian of over-parametrized neural networks*, arXiv preprint arXiv:1706.04454
(2017).

[SGJ+21] Berfin Simsek, François Ged, Arthur Jacot, Francesco Spadaro, Clément Hongler, Wulfram Gerstner, and Johanni Brea, *Geometry of the loss landscape in overparameterized neural networks: Symmetries and invariances*, International Conference on Machine Learning, PMLR,
2021, pp. 9722–9732.

[SM20] Alexander Shevchenko and Marco Mondelli, *Landscape connectivity and dropout stability of* SGD solutions for over-parameterized neural networks, International Conference on Machine Learning, PMLR, 2020, pp. 8773–8784.

[SS18] Itay Safran and Ohad Shamir, *Spurious local minima are common in two-layer relu neural* networks, International Conference on Machine Learning, PMLR, 2018, pp. 4433–4441.

[SZ14] Karen Simonyan and Andrew Zisserman, Very deep convolutional networks for large-scale image recognition, arXiv preprint arXiv:1409.1556 (2014).

[VF22] Tiffany J Vlaar and Jonathan Frankle, *What can linear interpolation of neural network loss* landscapes tell us?, International Conference on Machine Learning, PMLR, 2022, pp. 22325–
22341.

[WWS] Lei Wu, Mingze Wang, and Weijie J Su, *The alignment property of SGD noise and how it* helps select flat minima: A stability analysis, Advances in Neural Information Processing Systems.

[WWZG22] Xiang Wang, Annie N Wang, Mo Zhou, and Rong Ge, *Plateau in monotonic linear interpolation–a" biased" view of loss landscape for deep networks*, arXiv preprint arXiv:2210.01019 (2022).

[WZE17] Lei Wu, Zhanxing Zhu, and Weinan E, *Towards understanding generalization of deep learning: Perspective of loss landscapes*, arXiv preprint arXiv:1706.10239 (2017).

[YO19] Yuki Yoshida and Masato Okada, Data-dependence of plateau phenomenon in learning with neural network—statistical mechanical analysis, Advances in Neural Information Processing Systems 32 (2019).

[YSJ18] Chulhee Yun, Suvrit Sra, and Ali Jadbabaie, *Small nonlinearities in activation functions* create bad local minima in neural networks, International Conference on Learning Representations, 2018.

[ZZLX21] Yaoyu Zhang, Zhongwang Zhang, Tao Luo, and Zhiqin J Xu, *Embedding principle of loss* landscape of deep neural networks, Advances in Neural Information Processing Systems 34
(2021), 14848–14859.

## A Proofs In Section 3 A.1 Proof Of Theorem 6.

Let  $$\widetilde{\mathcal{M}}=\left\{W\in\mathbb{R}^{m\times d}\,:\,\mathbf{w}_{i}\in S\text{for}i=1,\ldots,m\text{and}\sum_{i=1}^{m}w_{i,j}=1\text{for}j=1,\ldots,M\right\}.$$  Our task is to prove that $\mathcal{M}=\widetilde{\mathcal{M}}$. For any $W\in\mathcal{M}$, we have $L(W)=\mathbb{E}_{\mathbf{w}\sim\mathbf{r}_{d-1}}[(\sum_{i=1}^{m}\sigma(\mathbf{w}_{i}^{T}\mathbf{x})-\sigma(\mathbf{w}_{i}^{T}\mathbf{x}))]$.  
PM
j=1 σ(xj ))2] = 0. By the non-degeneracy of τd−1, this is equivalent to

$$\sum_{i=1}^{m}\sigma(\mathbf{w}_{i}^{T}\mathbf{x})=\sum_{j=1}^{M}\sigma(x_{j})\quad\forall\,\mathbf{x}\,\in\mathbb{S}^{d-1}.$$
$$({\mathfrak{g}})$$
d−1. (9)
- We first consider the first M columns. Taking x = ej in (9) gives for any j ∈ [M] that

$$\sum_{i=1}^{m}\sigma(w_{i,j})=\sum_{i=1}^{m}\sigma(\mathbf{w}_{i}^{T}\mathbf{e}_{j})=1.$$
i ej ) = 1. (10)
Taking x = −ej in (9) gives for any j ∈ [M] that

$$\sum_{i=1}^{m}\sigma(-w_{i j})=\sum_{i=1}^{m}\sigma(-\mathbf{w}_{i}^{T}\mathbf{e}_{j})=0.$$
i ej ) = 0. (11)
Combining (10) and (11) leads to

$$\begin{cases}w_{ij}\geq0&\forall\,i\in[m],j\in[M]\\ \sum\limits_{i=1}^{m}w_{ij}=1&\forall\,j\in[M]\end{cases}.\tag{1}$$

- Next we turn to consider the columns from M + 1 to d. Analogously, for any j ∈ M + 1*, . . . , d*, we take x = ej and x = −ej in (9), yielding

$$\left\{\begin{array}{l l}{{\sum_{i=1}^{m}\sigma(w_{i j})=0}}\\ {{\sum_{i=1}^{m}\sigma(-w_{i j})=0.}}\end{array}\right.$$

$$(13)$$

This implies wij = 0, ∀ i ∈ {1, . . . , m}, j ∈ {M + 1*, . . . , d*}. (14)

- Now we prove by contradiction that for each j ∈ [m], there exists at most one coordinate to be nonzero. Suppose that there exists i ∈ [m] such that ||wi||0 ≥ 2. W.L.O.G, let i = 1 and w11 > 0, w12 > 0. Then, there must exist ϵ > 0 such that √1 − ϵ 2w11 − ϵw12 > 0.
Let x =
√1 − ϵ 2e1 − ϵe2 in (9). First, we have P
M
i=1 σ (xi) = √1 − ϵ 2. Second,

Xm i=1 σ(wi· x) = Xm i=1 σ( p1 − ϵ 2wi1 − ϵwi2) = σ( p1 − ϵ 2w11 − ϵw12) +Xm i=2 σ( p1 − ϵ 2wi1 − ϵwi2) ≤ σ( p1 − ϵ 2w11 − ϵw12) +Xm i=2 σ( p1 − ϵ 2wi1) = p1 − ϵ 2w11 − ϵw12 + Xm i=2 p1 − ϵ 2wi1 = p1 − ϵ 2Xm i=1 wi1 − ϵwi2 < p1 − ϵ 2Xm i=1 wi1 = p1 − ϵ 2. Thus, Pm i=1 σ(wi· x) <P M i=1 σ (xi), which is contradictory with (9).
Combining the three conclusions above, we proved M ⊂ Mf. What remains is to prove *M ⊂ M* f . It is obvious that for any W ∈ Mf, we have Pm i=1 σ (wi· x) = Pm i=1

$\widetilde{\mathcal{M}}$. What remains is to prove $\widetilde{\mathcal{M}}\subset\mathcal{M}$. It is $\sigma\left(\sum\limits_{j=1}^{d}w_{ij}x_{j}\right)=\sum\limits_{i=1}^{m}\sum\limits_{j=1}^{d}w_{ij}\sigma\left(x_{j}\right)=\sum\limits_{i=1}^{M}\sigma\left(x_{i}\right)$.  
Thus W is a global minimum, implying *M ⊂ M* ˜ .

Proof of Lemma 7. Recall that Theorem 6 shows

$$\mathcal{M}=\left\{W\in\mathbb{R}^{m\times d}\,:\,\mathbf{w}_{i}\in S\text{for}i=1,\ldots,m\text{and}\sum_{i=1}^{m}w_{i,j}=1\text{for}j=1,\ldots,M\right\},\tag{15}$$

where S = ∪M
j=0Sj with S0 = {(0*, . . . ,* 0) ∈ R
d} and Sj = {αej ∈ R
d: α ̸= 0} for j = 1*, . . . , M*.

Given any θ1, θ2 ∈ M, our task is to prove that θ1 ↔ θ2 is equivalent to that one of the following two conditions is satisfied:
a) w
(1)
i ∈ S0 or w
(2)
i ∈ S0; b) there exists j ∈ {1*, . . . , M*} such that w
(1)
i ∈ Sj and w
(2)
i ∈ Sj .

We first prove that θ1 ↔ θ2 can lead to the condition a) or b). Note that θ1 ↔ θ2 means

$$\gamma(t)=((1-t)\mathbf{w}_{1}^{(1)}+t\mathbf{w}_{1}^{(2)},\cdots,(1-t)\mathbf{w}_{m}^{(1)}+t\mathbf{w}_{m}^{(2)})^{T}\in{\mathcal{M}}.$$

By (15), (1 − t)w
(1)
i + tw
(2)
i ∈ S holds for any i ∈ [m] and t ∈ [0, 1]. Since any element in S has at most one nonzero coordinate, w
(1)
iand w
(2)
ihave at most one nonzero coordinate and their nonzero coordinates must be the same. Otherwise, the number of nonzero coordinates of (1 − t)w
(1)
i + tw
(2)
i will be no less than 2 for any t ∈ (0, 1). This implies that either condition a) or condition b) is satisfied.

Second, if condition a) or condition b) is satisfied, then for any t ∈ [0, 1] and any i ∈ [m], (1−t)w
(1)
i +
tw
(2)
i ∈ S. Moreover, for any j ∈ [M],

$$\sum_{i=1}^{m}\left((1-t)w_{i,j}^{(1)}+t w_{i,j}^{(2)}\right)=(1-t)\sum_{i=1}^{m}w_{i,j}^{(1)}+t\sum_{i=1}^{m}w_{i,j}^{(2)}=(1-t)+t=1.$$

Hence, by (15), (1 − t)θ1 + tθ2 ∈ M for any t ∈ [0, 1].

## A.2 Proof Of Theorem 8.

Let θi iid∼ Unif(M) for i = 1, 2. We aim to give a lower bound for the probability that there exists a global minimum θ
∗such that θ 1 ↔ θ
∗ and θ
∗ ↔ θ 2. From Theorem 6, given a θ = (w1*, . . . ,* wm)
T ∈ R
m×d, the sufficient and necessary condition for θ to be a global minimum is:
(1) wi ∈ S, for any i ∈ [m].

(2) $\sum_{j:\mathbf{w}_{j}\in S_{i}}\mathbf{w}_{j}=e_{i}$, for $i\in\{1,\ldots,M\}$.  
We notice that θ 1(θ 2) has the requirement that for every i ∈ {1*, . . . , M*}, there exists j ∈ {1*, . . . , m*}
such that θ 1 j
(θ 2 j
) ∈ Si, after we already have M different elements of θ 1(θ 2), the rest elements have no restriction and can be arbitrarily chosen in at least m − 2M overlapped positions.

Hence, we suppose w1 j and w2 j have uniform distribution over S for any j ∈ T, where T is a subset of
{1*, . . . , m*} containing m − 2M elements. i.e. w1 j
(w2 j
) (j ∈ T)chooses randomly a set from {S0*, . . . , S*M}
to belong to.

For j ∈ T, we consider the pair (w1 j
, w2 j
). We denote [w1 j
, w2 j
]
∆=[*p, q*] if w1 j ∈ Sp and w2 j ∈ Sq.

Then we define the incident Ai: for any j ∈ T, [w1 j
, w2 j
] ̸= [*i, i*]. Since θi iid∼ Unif(M) for i = 1, 2, we have P(Ai) = (M2−1 M2 )
m−2M.

$\square$
Thus, from the inclusion-exclusion principle, we have:

$P(\theta_1\text{and}\theta_2\text{are}Z\text{-}\mathbb{P}\mathbb{L})$  . 
P(θ1 and θ2 are 2-PL connected)

≥1 − X M i=1 P(Ai) =1 − MP(A1) =1 − M M2 − 1 M2 m−2M.
$$\square$$

## A.3 Proof Of Theorem 9.

First, we consider the choice of θ 3(θ 5). Since θ 1(θ 2) has property that for every i ∈ {1*, . . . , M*}, there exists ji ∈ {1*, . . . , m*} such that w1 ji
∈ Si. Then, we let w3 ji = ei for i ∈ {1*, . . . , M*}, and set the other line vector of θ 3 as zero. From Theorem 6, θ 3is a global minimum of Equation (3). Further, from Lemma 7, we have θ 1 ↔ θ 3. We call this method generating θ 3from θ 1"merging", since it straightforwardly merges some line vectors of θ 1 belonging to the same set in S to a single non-zero vector. Similarly, we can merge θ 2to θ 5.

θ 3 and θ 5share the common characteristic that they contain exactly M different non-zero line vectors
{e1*, . . . ,* eM}, and m − M zero line vectors. Since m ≥ 2M − 1, we have m − M ≥ M − 1, thus θ 3 has at least M − 1 zero line vectors.

Case 1.

If there are at least M zero line vectors, suppose the set of the zero line vectors is {w3a1
, . . . , w3aM
},
then since w5a1
, . . . , w5aM
belong to different subsets of S or belong to S0, We can find a feasible set of
{w4a1
, . . . , w4aM
} = {e1*, . . . ,* eM}, we set other line vectors of θ 4 as zero and then we are done since we have a feasible global minimum θ 4.

Case 2.

If there are only M −1 zero line vectors for θ 3. Now, we fix a feasible θ 3 merged from θ 1, suppose the set of its zero line vectors is {w3a1
, . . . , w3aM−1
}. First, we look at the corresponding line vectors of these θ 3's zero vectors in θ 5, i.e. {w5a1
, . . . , w5aM−1
}. We notice that θ 5is not fixed when generated from θ 2, and trivially we have at least M different positions to choose from for the M −1 zero line vectors. Hence, there exists a choice of θ 5 where at least one element of {w5a1
, . . . , w5aM−1
} is non-zero. Thus, there is at least one zero vector of θ 5 with a non-zero corresponding line vector in θ 3, the set of which we denote as
{w3 b1
, . . . , w3 bf
}.

Case 2-1.

If there exists w3 bi belongs to different subset of S from any element of {w5a1
, . . . , w5aM−1
}, then we can find a feasible set of {w4 bi
, w4a1,
. . . , w4aM−1
} = {e1*, . . . ,* eM}. We set other line vectors of θ 4 as zero and then we are done since we have a feasible global minimum θ 4.

Case 2-2.

If every element of w3 b1
, . . . , w3 bf belongs to the same subset of S as an element of {w5a1
, . . . , w5aM−1
},
we arbitrarily choose a line vector from w3 b1
, . . . , w3 bf
. Suppose w3 bj
∈ St and w5aq
∈ St. Then we suppose w2 bj
∈ Sp, and w5 bg
∈ Sp.

Case 2-2-1.

If p = 0, then we let w5 bj = et, and let w5aq = 0. Then we can find a feasible set of {w4 bj
, w4a1,
. . . , w4aM−1
} =
{e1*, . . . ,* eM}. We set other line vectors of θ 4 as zero and then we are done since we have a feasible global minimum θ 4.

Case 2-2-2.

If p ̸= 0, then we can switch w5 bj and w5 bg without damaging the connectivity of the global minima.

Now, the number of the non-zero corresponding line vectors in θ 3reduces to f − 1. After at most f − 1 same operations, if we still didn't find the feasible global minimum W4, then we get exactly one non-zero corresponding line vector in θ 3 and exactly one non-zero element in {w5a1
, . . . , w5aM−1
}, and these two vectors belong to the same subset of S. Suppose w3 bj
′ ∈ St
′ and w5aq′ ∈ St
′ (t
′ ̸= 0). Then we suppose w2 bj
′ ∈ Sp′ , and w5 bg′ ∈ Sp′ .

Case 2-2-2-1. If p
′ = 0, then we let w5 bj
′ = et
′ , and let w5aq′ = 0. Then we can find a feasible set of {w4 bj
′
, w4a1,
. . . , w4aM−1
} =
{e1*, . . . ,* eM}. We set other line vectors of θ 4 as zero and then we are done since we have a feasible global minimum θ 4.

Case 2-2-2-2. If p
′ ̸= 0, then we can switch w5 bj
′
and w5 bg′ without damaging the connectivity of the global minima.

Since p
′ ̸= t
′, then we can find a feasible set of {w4 bg′
, w4a1,
. . . , w4aM−1
} = {e1*, . . . ,* eM}. We set other line vectors of θ 4 as zero and then we are done since we have a feasible global minimum θ 4.

Finally, we complete the proof.

We follow the proof of Theorem 8 and apply some modifications.

Here, for j ∈ T, we consider the combination (w1 j
, . . . , wk j
). We denote [w1 j
, . . . wk j
]
∆=[p1*, . . . , p*k] if wij ∈ Spi for i ∈ {1*, . . . , k*}.

Similarly, we define the incident Ai: for any j ∈ T, [w1 j
, w2 j
, . . . , wk j
] ̸= [*i, i, . . . , i*].

Thus. following the proof of Theorem 8, based on our assumption for uniform distribution, we can calculate that P(Ai) = (Mk−1 Mk )
m−kM.

Hence, $1-\sum\limits_{i=1}^M P(A_i)=1-M(\frac{M^k-1}{M^k})^{m-kM}$, which is the lower bound in the theorem. 
$$\square$$

## A.5 Proof Of Theorem 11.

We follow the proof of Theorem 9. Firstly, we merge θ ito be θ i0just as what we did in the proof of Theorem 9. Considering θ i0for any i ∈ {1*, . . . , k*}, since m ≥ kM, it has at least (k − 1)M zero line vectors.

Hence, it trivially holds that θ 10 and θ 20 share at least (k − 2)M zero line vectors of relatively same position, θ 10, θ 20 and θ 30 share at least (k − 3)M zero line vectors of relatively same position*. . .* We can easily use mathematical induction to deduce that θ 10*, . . . , θ*k−10 share at least M zero line vectors of relatively same position. Suppose the positions of the M common line vectors are {a1*, . . . , a*M}.

Since wk a1
, . . . , wk aM
belong to different subsets of S or belong to S0, we can find a feasible set of
{wk+1 a1*, . . . ,* wk+1 aM
} = {e1*, . . . ,* eM}. We set other line vectors of θ k+1 as zero and then we are done since we have a feasible global minimum θ k+1.

Here we finish proving Theorem 11.

Lemma 19. *For any two global minima* θ1 = (u 1 1
, . . . ,u 1 d
), θ2 = (u 2 1
, . . . ,u 2 d
), for i ∈ {1, . . . , M}*, suppose* θ1 and θ2 respectively have m1 and m2 neurons that belong to Si*, with* mt(mt ≤ min{m1, m2}) neurons sharing common coordinates, then for any global minimum θ = (v1, . . . , vd)*, we have*

$$\min_{\theta}{\frac{\|\mathbf{v}_{i}-\mathbf{u}_{i}^{1}\|_{2}^{2}+\|\mathbf{v}_{i}-\mathbf{u}_{i}^{2}\|_{2}^{2}}{\|\mathbf{u}_{i}^{1}-\mathbf{u}_{i}^{2}\|_{2}^{2}}}\leq{\frac{1}{1-{\sqrt{\frac{(m_{1}-m_{t})(m_{2}-m_{t})}{m_{1}m_{2}}}}}}.$$

Proof of Lemma 19. Suppose θ1 = (w1
1
, . . . , w1m)
T = (u
1 1
, . . . ,u
1 d
), θ2 = (w2
1
, . . . , w2m)
$\mathbf)^T=(\mathbfit{u}_1^2,\ldots,\mathbfit{u}_1^2)\in$. 
1
d
) ∈
R

m×d. Suppose θ = (w1*, . . . ,* wm)
T = (v1*, . . . ,* vd).
Suppose a1*, . . . , a*mt
, b1*, . . . , b*mt
are the i
th components of w1 where w1shares common coordinates with w2. amt+1*, . . . , a*m1
, bmt+1*, . . . , b*m2 are the rest components. We have Pmt j=1 aj ≤ 1 and Pmt j=1 bj ≤ 1.

Suppose x1*, . . . , x*mt are the i th components of w that share common coordinates with w1 and w2. From Theorem 6, we have Pmt j=1 xj = 1. Thus,

∥vi − u
1
i ∥
2
2 + ∥vi − u
2
i ∥
2
2
=
Xmt
i=1
-(xi − ai)
2 + (xi − bi)
2+Xm1
i=mt+1
a
2
i +Xm2
i=mt+1
b
2
i
=2Xmt
i=1
x
2
i − (ai + bi)xi +
a
2
i + b
2
i
2
+Xm1
i=mt+1
a
2
i +Xm2
i=mt+1
b
2
i
=2Xmt
i=1
(xi −
ai + bi
2)
2 +
(ai − bi)
2
4
+Xm1
i=mt+1
a
2
i +Xm2
i=mt+1
b
2
i
≥2
1 −Pmt
i=1
(ai + bi) /2
2
m+
Pmt
i=1
(ai − bi)
2
2+Xm1
i=mt+1
a
2
i +Xm2
i=mt+1
b
2
i
.
Thus, we have
min
θ
∥vi − u
1
i
∥
2
2 + ∥vi − u
2
i
∥
2
2
∥u
1
i − u
2
i
∥
2
2
=
2
1−
mPt
i=1
(ai+bi)/2
2
m +
mPt
i=1
(ai−bi)
2
2 +
mP1
i=mt+1
a
2
i +
mP2
i=mt+1
b
2
i
∆= M.
Pmt
i=1
(ai − bi)
2 +
mP1
i=mt+1
a
2
i +
mP2
i=mt+1
b
2
i
Further, we have
M ≤
2
1−
mPt
i=1
(ai+bi)/2
2
m +
mPt
i=1
(ai−bi)
2
2 +
(1−
mPt
i=1
ai)
2
m1−mt+
(1−
mPt
i=1
bi)
2
m2−mt
.
Pmt
i=1
(ai − bi)
2 +
(1−
mPt
i=1
ai)
2
m1−mt+
(1−
mPt
i=1
bi)
2
m2−mt
Denote Sa
∆=Pmt
i=1
ai, Sb
∆=Pmt
i=1
bi, then we have
M ≤
2
(1−
Sa+Sb
2)
2
m +
(Sa−Sb)
2
2mt+
(1−Sa)
2
m1−mt
+
(1−Sb)
2
m2−mt
(Sa−Sb)
2
mt+
(1−Sa)
2
m1−mt
+
(1−Sb)
2
m2−mt
=
m1
mt(m1−mt)
(1 − Sa)
2 +m2
mt(m2−mt)
(1 − Sb)
2
(Sa−Sb)
2
mt+
(1−Sa)
2
m1−mt
+
(1−Sb)
2
m2−mt
≤
pm1(m2 − mt)m2(m1 − mt)
pm1(m2 − mt)m2(m1 − mt) − (m1 − mt)(m2 − mt)
=1
1 −
q(m1−mt)(m2−mt)
m1m2
.
Now we completed the proof.
Lemma 20 (Hoeffding's inequality). Let X1, . . . , Xn *be independent random variables. Assume that* Xi ∈ [mi, Mi] for every i. Then, for any t > 0*, we have*

$$\mathbb{P}\left\{\sum_{i=1}^{n}\left(X_{i}-\mathbb{E}X_{i}\right)\geq t\right\}\leq e^{-{\frac{2t^{2}}{\sum_{i=1}^{n}\left(M_{i}-m_{i}\right)^{2}}}}.$$

We suppose m1 ≥ m2, then we have mt m1
=
mP1 j=1 1{w2 j ∈Si}
m1. Then, from Hoeffding's inequality (Lemma 20), we have for any ϵ > 0, with probability 1 − e
−2m1ϵ 2,

$$\frac{\sum_{j=1}^{m_{1}}\mathbb{I}\left\{\mathbf{w}_{j}^{2}\in S_{i}\right\}}{m_{1}}-\frac{1}{m+1}\geq-\epsilon.$$
Then we have  $$\frac{1}{1-\sqrt{\frac{(m_{1}-m_{1})(m_{2}-m_{1})}{m_{1}m_{2}}}}\leq\frac{1}{1-\frac{m_{1}-m_{2}}{m_{1}}}=\frac{1}{\frac{m_{1}}{m_{1}}}\leq\frac{1}{\frac{1}{M+1}-\epsilon}.$$  Now, we suppose $\theta_{1}$ and $\theta_{2}$ respectively have $m_{1i}$ and $m_{2j}$ neurons that belong to $S_{i}$, and from Lemma 1.  
Now, we suppose $\theta_{1}$ and $\theta_{2}$ respectively have $m_{1i}$ and $m_{2i}$ neurons that  $$19$$  we have with probability $1-\sum\limits_{i=1}^{M}e^{-2\max\{m_{1i},m_{2i}\}\epsilon^{2}}$,  $$\min_{\theta}\frac{\|\mathbf{v}_{i}-\mathbf{u}_{i}^{1}\|_{2}^{2}+\|\mathbf{v}_{i}-\mathbf{u}_{i}^{2}\|_{2}^{2}}{\|\mathbf{u}_{i}^{1}-\mathbf{u}_{i}^{2}\|_{2}^{2}}\leq\frac{1}{\frac{1}{M+1}-\epsilon}$$  for all $i\in\{1,\ldots,M\}$. Hence,  $$\|\theta-\theta_{1}\|^{2}+\|\theta-\theta_{2}\|^{2},\ldots,1.$$
$$\operatorname*{min}_{\theta}{\frac{\|\theta-\theta_{1}\|_{2}^{2}+\|\theta-\theta_{2}\|_{2}^{2}}{\|\theta_{1}-\theta_{2}\|_{2}^{2}}}\leq{\frac{1}{{\frac{1}{M+1}}-\epsilon}}.$$

Furthermore, for any δ > 0, from Hoeffding's inequality, we have with probability 1 − e
−2mδ2, m1i m−
1 M + 1
≥ −δ.

Hence, with probability 1 − Me−2mδ2,

$${\frac{\operatorname*{max}\{m_{1i},m_{2i}\}}{m}}-{\frac{1}{M+1}}\geq-\delta$$
$$\mathrm{ll}\ i\in\{1,\ldots,M\}.\ \mathrm{Th}$$
for all $i\in\{1,\ldots,M\}$. Therefore, with probability $1-Me^{-2m\delta^{2}}-Me^{-2(\frac{\pi}{M+1}-m\delta)\epsilon^{2}}$,
$$\min_{\theta}\frac{\|\theta-\theta_{1}\|_{2}^{2}+\|\theta-\theta_{2}\|_{2}^{2}}{\|\theta_{1}-\theta_{2}\|_{2}^{2}}\leq\frac{1}{\frac{1}{M+1}-\epsilon}.$$  We let $\delta=\epsilon$, and we obtain with probability $1-Me^{-2me^{2}}-Me^{-2(\frac{\pi^{2}}{M+1}-me)\epsilon^{2}}$,
$$\operatorname*{min}_{\theta}{\frac{\|\theta-\theta_{1}\|_{2}^{2}+\|\theta-\theta_{2}\|_{2}^{2}}{\|\theta_{1}-\theta_{2}\|_{2}^{2}}}\leq{\frac{1}{{\frac{1}{M+1}}-\epsilon}}.$$

From Cauchy's inequality, we completed the proof.

Lemma 21. Suppose a1*, . . . , a*mt
, b1, . . . , bmt *are the* i th components of w1 and w2 where w1shares common coordinates with w2 or where the neuron of w1 or w2belongs to S0. amt+1*, . . . , a*m1
, bmt+1*, . . . , b*m2 are the rest components. Then we have

$$\min_{\theta}\frac{\|\mathbf{v}_{i}-\mathbf{u}_{i}^{1}\|_{2}^{2}+\|\mathbf{v}_{i}-\mathbf{u}_{i}^{2}\|_{2}^{2}}{\|\mathbf{u}_{i}^{1}-\mathbf{u}_{i}^{2}\|_{2}^{2}}=\frac{2\frac{\left(1-\sum\limits_{i=1}^{m}(a_{i}+b_{i})/2\right)^{2}}{m_{t}}+\frac{\sum\limits_{i=1}^{m}(a_{i}-b_{i})^{2}}{2}+\sum\limits_{i=m+t+1}^{m}a_{i}^{2}+\sum\limits_{i=m+t+1}^{m}b_{i}^{2}}{\sum\limits_{i=1}^{m}(a_{i}-b_{i})^{2}+\sum\limits_{i=m+t+1}^{m}a_{i}^{2}+\sum\limits_{i=m+t+1}^{m}b_{i}^{2}}.$$
$$\square$$

20 Proof of Lemma 21. We have Pmt j=1 aj ≤ 1 and Pmt j=1 bj ≤ 1. Suppose x1*, . . . , x*mt are the i th components

of w that share common coordinates with w1 and w2. From Theorem 6, we have Pmt
j=1 ∥vi − u 1 i ∥ 2 2 + ∥vi − u 2 i ∥ 2 2 = Xmt i=1 [(xi − ai) 2 + (xi − bi) 2] + Xm1 i=mt+1 a 2 i +Xm2 i=mt+1 b 2 i =2Xmt i=1 [x 2 i − (ai + bi)xi + a 2 i + b 2 i 2] + Xm1 i=mt+1 a 2 i +Xm2 i=mt+1 b 2 i =2Xmt i=1 [(xi − ai + bi 2) 2 + (ai − bi) 2 4] + Xm1 i=mt+1 a 2 i +Xm2 i=mt+1 b 2 i ≥2 1 −Pmt i=1 (ai + bi)/2 2 mt+ Pmt i=1 (ai − bi) 2 2+Xm1 i=mt+1 a 2 i +Xm2 i=mt+1 b 2 i
xj = 1. Thus, Thus, we have

$$\operatorname*{min}_{\theta}{\frac{\|v_{i}\|}{\theta}}$$
∥vi − u 1 i ∥ 2 2 + ∥vi − u 2 i ∥ 2 2 ∥u 1 i − u 2 i ∥ 2 2 = 2 1− mPt i=1 (ai+bi)/2 2 mt+ mPt i=1 (ai−bi) 2 2 + mP1 i=mt+1 a 2 i + mP2 i=mt+1 b 2 i Pmt i=1 (ai − bi) 2 + mP1 i=mt+1 a 2 i + mP2 i=mt+1 b 2 i .
$$\square$$

Lemma 22. *With probability* 1 − 5e
−2mtϵ 2,

$$\operatorname*{min}_{\theta}{\frac{\|\mathbf{v}_{i}-\mathbf{u}_{i}^{1}\|_{2}^{2}+\|\mathbf{v}_{i}-\mathbf{u}_{i}^{2}\|_{2}^{2}}{\|\mathbf{u}_{i}^{1}-\mathbf{u}_{i}^{2}\|_{2}^{2}}}\leq A.$$

Here,

$$A=\frac{\frac{2\left(\frac{1}{m_{t}}-\frac{1}{2m_{1}}+\frac{1}{2m_{2}}+\epsilon\right)^{2}}{m_{t}}+\frac{\epsilon-\epsilon}{2}+(\frac{1}{m_{t}}-\frac{1}{m_{1}}+\epsilon)^{2}+(\frac{1}{m_{t}}-\frac{1}{m_{2}}+\epsilon)^{2}}{c-\epsilon+(\frac{1}{m_{t}}-\frac{1}{m_{1}}+\epsilon)^{2}+(\frac{1}{m_{t}}-\frac{1}{m_{2}}+\epsilon)^{2}}.$$

Proof of Lemma 22. From Lemma 21, we have

min θ ∥vi − u 1 i ∥ 2 2 + ∥vi − u 2 i ∥ 2 2 ∥u 1 i − u 2 i ∥ 2 2 ≤ 2 1− mPt i=1 (ai+bi)/2 2 mt+ mPt i=1 (ai−bi) 2 2 + (1 −Pmt i=1 ai) 2 + (1 −Pmt i=1 bi) 2 Pmt i=1 (ai − bi) 2 + (1 −Pmt i=1 ai) 2 + (1 −Pmt i=1 bi) 2 .
Since θ1 and θ2 are independently drawn from SP(M, r), (ai − bi)
2 has a positive expectation c > 0.

Then, from Hoeffding's inequality (Lemma 20), for any ϵ > 0, we have with probability 1 − e
−2mtϵ 2,

$$\sum_{i=1}^{m_{t}}(a_{i}-b_{i})^{2}-c m_{t}\geq-m_{t}\epsilon.$$

Similarly, we have with probability 1 − 2e
−2mtϵ 2,

$$\left|\sum_{i=1}^{m_{t}}a_{i}-{\frac{m_{t}}{m_{1}}}\right|\leq m_{t}\epsilon,$$
 and with probability 1 − 2e −2mtϵ 2, 
$$\left|\sum_{i=1}^{m_{t}}b_{i}-{\frac{m_{t}}{m_{2}}}\right|\leq m_{t}\epsilon.$$
min θ ∥vi − u 1 i ∥ 2 2 + ∥vi − u 2 i ∥ 2 2 ∥u 1 i − u 2 i ∥ 2 2 = 2 1− mPt i=1 (ai+bi)/2 2 mt+ mPt i=1 (ai−bi) 2 2 + mP1 i=mt+1 a 2 i + mP2 i=mt+1 b 2 i Pmt i=1 (ai − bi) 2 + mP1 i=mt+1 a 2 i + mP2 i=mt+1 b 2 i ≤A.

$${\frac{m_{t}}{m_{1}}}\geq{\frac{\sum\limits_{j=1}^{m_{1}}\mathbb{1}\left\{\mathbf{w}_{j}^{2}\in S_{i}\right\}+\sum\limits_{j=1}^{m_{1}}\mathbb{1}\left\{\mathbf{w}_{j}^{2}\in S_{0}\right\}}{m_{1}}}.$$
$$\left|\sum_{j=1}^{m_{1}}\mathbb{1}\left\{\mathbf{w}_{j}^{2}\in S_{i}\right\}+\sum_{j=1}^{m_{1}}\mathbb{1}\left\{\mathbf{w}_{j}^{2}\in S_{0}\right\}\right.$$
$$\left|\sum_{j=1}^{m_{2}}\mathbb{1}\left\{\mathbf{w}_{j}^{1}\in S_{i}\right\}+\sum_{j=1}^{m_{2}}\mathbb{1}\left\{\mathbf{w}_{j}^{1}\in S_{0}\right\}\right.$$
$$\frac{m_{1}}{m}-\frac{1+(M-1)r}{M}\geq-\epsilon,$$  and with probability $1-e^{-2me^{2}}$,  $$\frac{m_{2}}{m}-\frac{1+(M-1)r}{M}\geq-\epsilon.$$  We denote $\left(\frac{\frac{(M-1)(1-r)}{M}+\epsilon}{(\frac{1+(M-1)r}{M}-\epsilon)^{2}m}+\epsilon\right)^{2}=q$, then in this case, we have  $$A\leq\frac{1}{2}+\frac{\frac{2q}{(\frac{1+(M-1)r}{M}-\epsilon)^{2}m}+q}{c-\epsilon+2q}.$$

Hence, we have with probability 1 − 5e
−2mtϵ 2, Now, go back to the original problem, we have Then, from Hoeffding's inequality (Lemma 20), we have for any ϵ > 0, with probability 1 − 2e
−2m1ϵ 2, Similarly we have with probability 1 − 2e
−2m2ϵ 2, Also, with probability 1 − e
−2mϵ2, Now, we suppose θ 1 and θ 2respectively have m1i and m2i neurons that belong to Si, and we have with probability 1 −P
M

i=1
11e
−2( 1+(M−1)r
M −ϵ)
2mϵ2,
$$\begin{array}{c}{{\sum_{i=1}^{M}\frac{\|\mathbf{v}_{i}-\mathbf{u}_{i}^{1}\|_{2}^{2}+\|\mathbf{v}_{i}-\mathbf{u}_{i}^{2}\|_{2}^{2}}{\|\mathbf{u}_{i}^{1}-\mathbf{u}_{i}^{2}\|_{2}^{2}}\leq\frac{1}{2}+\frac{\frac{2q}{(\frac{1+(M-1)r}{M}-\epsilon)^{2}m}+q}}}\end{array}$$
for all $i\in\{1,\ldots,M\}$.  
Hence, with probability 1 − 11Me−2( 1+(M−1)r M −ϵ)
2mϵ2,

$$\operatorname*{min}_{\theta}{\frac{\|\theta-\theta^{1}\|_{2}^{2}+\|\theta-\theta^{2}\|_{2}^{2}}{\|\theta^{1}-\theta^{2}\|_{2}^{2}}}\leq{\frac{1}{2}}+{\frac{{\frac{2q}{(1+(M-1)^{n}-\epsilon)^{2}m}}+q}{c-\epsilon+2q}}.$$
$$\mathbb{D}$$
$\left(16\right)$. 
At last, we used Cauchy's inequality and we completed the proof.

## B Proofs In Section 4

Before delving into Theorem 16, we first consider the simplest case where L = 2, d = 1 for gaining some intuition of the proof technique. Proposition 23. Theorem 16 *holds true for* L = 2, d = 1.

Proof. Let θi = (A
(i)
1
, A(i)
2
) for i = 1, 2 be the two global minima. We are aiming to find a θ
∗ = (A
(3)
1, A(3)
2)
satisfying
- θ
∗is a global minima: A
(3)
1 A
(3)
2 = Q;
- θ1 and θ2 are 2-PL connected through θ
∗: for any t ∈ [0, 1] and i = 1, 2, we have

$$+\left(1-t\right)$$

(tA(i)
1 + (1 − t)A
(3)
1)(tA(i)
2 + (1 − t)A
$$\cdot\,t)A_{2}^{(3)})=Q.$$
$\mathbf{T}_1$
$\star\star$ . 
2) = Q. (16)
Noticing that θ1 and θ2 are global minima, we have A
(i)
1 A
(i)
2 = Q for i = 1, 2. Combining this with (16)
leads to A
(3)
1 A
(i)
2 + A
(i)
1 A
(3)
2 = 2Q
The problem now is converted to finding A
(3)
1 ∈ R
1×m, A(3)
2 ∈ R
m×1satisfied the following properties:

$$\begin{cases}A_{1}^{(1)}A_{2}^{(3)}=2Q-A_{1}^{(3)}A_{2}^{(1)}\\ A_{1}^{(2)}A_{2}^{(3)}=2Q-A_{1}^{(3)}A_{2}^{(2)}\\ A_{1}^{(3)}A_{2}^{(3)}=Q\end{cases}$$

1. When A
(1)
1, A(2)
1are linearly independent, we choose A
(3)
1linearly independent of both A
(1)
1and A
(2)
1. Then the problem above turns into solving a set of linear equations for A
(3)
2. Since m ≥ 3, we can find a proper solution and finish the proof.

2. Suppose kA(1)
1 = A
(2)
1, we consider the first two equations, θ
∗ = (A
(3)
1, A(3)
2) exists only if A
(3)
1(kA(1)
2 −
A
(2)
2) = (2k − 2)C, otherwise the first two equations will draw a contradiction by multiplying k times in both sides of the first equation. Noticing that if kA(1)
2 − A
(2)
2 = 0, we have Q = A
(2)
1 A
(2)
2 = k 2A
(1)
1 A
(1)
2 = k 2Q, then k = 1 or −1. We note that we have assumed that k ̸= −1, while for k = 1, (A
(1)
1, A(2)
1) = (A
(2)
1, A(2)
2) is a trivial case. Thus, with the condition kA(1)
2 − A
(2)
2̸= 0, we can find a solution A
(3)
1for A
(3)
1(kA(1)
2 − A
(2)
2) = (2k − 2)C that is linearly independent of A
(1)
1, A(1)
2(we can find m − 1 ≥ 2 linearly independent solutions in fact) first, then get a proper A
(3)
2and finish the whole proof.
Remark 24. This will not hold for the case that (A
(1)
1, A(1)
2) = (−A
(2)
1, −A
(2)
2), since k = −1,(kA(2)
1 −
A
(2)
2) = 0 will directly draw 0 = −4A
(2)
1 A
(2)
2, which will be a contradiction when A
(2)
1 A
(2)
2̸= 0. We outline a simple counter-example here: A
(1)
1 = (1, 0, 0, 0), A(1)
2 = (1, 0, 0, 0)T, A(2)
1 = (−1, 0, 0, 0), A(2)
2 =
(−1, 0, 0, 0)T, Q = 1. In particular, denote the center A′1 = (α1*, . . . , α*4), A′2 = (β1*, . . . , β*4), the necessary conditions can be converted into α1 + β1 = 2, α1 + β1 = −2,P4 i=1 αiβi = 2, which draw a contradiction.

## Proof Of Theorem 16

The case of 2-PL connectivity. With the toy structure in Proposition 23, we can similarly consider the representation structure in Theorem 16 with the case d > 1.

Proof. If we consider each column of A2 separately, then the problem turns out to be the case in Proposition 23 by considering each column separately. Once A
(1)
1, A(2)
1are independent, we consider A
(3)
1linearly independent of A
(1)
1, A(2)
1and find a solution for each column in A
(3)
2independently, then the problem is solved directly by applying the case with d = 1 separately.

Now we consider the case that kA(1)
1 = A
(2)
1for some k ∈ R, in this case by considering conditions

$$\begin{array}{l}{{\left\{A_{1}^{(1)}A_{2}^{(3)}=2Q-A_{1}^{(3)}A_{2}^{(1)}\right.}}}\\ {{\left.A_{1}^{(2)}A_{2}^{(3)}=2Q-A_{1}^{(3)}A_{2}^{(2)}\right.}}\end{array}$$

we need A
(3)
1(kA(1)
2 − A
(2)
2) = (2k − 2)Q. We view it as solving linear equations A
(3)
1(kA(1)
2 − A
(2)
2) =
(2k − 2)Q for A
(3)
1. Denote Q = (Q1*, . . . , Q*n). If rank(kA(1)
2 − A
(2)
2) = *d < m*, it would be easy to find a solution A
(3)
1that is additionally independent to A
(1)
1. Otherwise, if rank(kA(1)
2 −A
(2)
2) < d, without loss of generality, we consider a case of column-wise linear dependency. Assume that the first two columns of A
(1)
2, A(2)
2are (α1, α2),(β1, β2), respectively. If kα1 − β1 = t(kα2 − β2), we naturally have

k
$$\dot{\kappa}^{2}Q_{1}-Q_{1}=A_{1}^{(2)}(l)$$
(2)
1(kα1 − β1) = tA(2)
1(kα2 − β2) = tk2Q2 − tQ2.

We have assumed that k ̸= −1. If k = 1, the linear connectivity always holds naturally. On the other hand, if k 2 ̸= 1, we will obtain Q1 = tQ2, which will never affect the linear equations in A
(3)
1(kA(1)
2 − A
(2)
2) =
(2k − 2)Q.

Thus, we can find a solution A
(3)
1that satisfies A
(3)
1(kA(1)
2 −A
(2)
2) = (2k−2)Q for A
(3)
1and independent to A
(1)
1. With this, we can then derive a proper A
(3)
2 by considering each column separately as in Proposition 23. Then, we finish our proof of Theorem 16.

## The Case Of 3-Pl Connectivity. For Two Minima

$$\theta_{1}=(A_{L}^{(1)},A_{L-1}^{(1)},\ldots,A_{1}^{(1)}),\ \theta_{2}=(A_{L}^{(2)},A_{L-1}^{(2)},\ldots,A_{1}^{(2)}),$$

that belong to the zero-measure set in the proof of 2-PL connectivity, we consider θ3 = (A
′
L
, A(1)
L−1

* [10] M. C.  
where A′L
satisfies that A′LA
(1)
L−1
. . . A(1)
1 = Q. Then it is natural that θ1 ↔ θ3.

We consider the following linear relationship: A′LA
(1)
L−1
. . . A(1)
t and A
(2)
L A
(2)
L−1
. . . A(2)
t are linearly independent for t = *L, . . . ,* 2, which would yield 2-PL connectivity of θ2 and θ3 following by the discussion above. To satisfy the L−1 conditions along with A′LA
(1)
L−1
. . . A(1)
1 = Q, we consider seeking for FL*, . . . , F*2 such that Fj is independent of A
(2)
L*. . . A*(2)
jfor j = 2*, . . . , L*. Then we consider A′LA
(1)
L−1
. . . A(1)
j = Fj for j = 2*, . . . , L* and A′LA
(1)
L−1
. . . A(1)
1 = Q as L linear equations on the m1 parameters in A′L
. We have assumed that m > 2L − 1, thus if Et = A
(1)
L−1
. . . A(1)
t, t = *L, . . . ,* 1 (EL = 1m) are linearly independent, the linear system would have a proper solution.

On the other hand, as we need to select FL*, . . . , F*2 to make sure the linear equations have a solution, we consider solving the dependency by the following adjustments. If some of the Ej 's are linearly dependent, for instance, Ek can be represented by the linear combination of another group of Ej 's, then our Fk need to be automatically determined by the corresponding Fj 's to ensure the existence of solutions. Since Fk need to be independent of A
(2)
L−1
. . . A(2)
k
, here we (might) lose a degree of freedom when selecting Fj 's, while the fact that we do not need to consider Fk anymore reduces an equation from the L conditions required. Thus, in the process of reducing our restrictions to be linearly independent, our degree of freedom would always be greater than the number of restrictions since m > 2L − 1 at the beginning. Thus, with the (eventually) linear-independent coefficients (with the number of restrictions less than parameters), we will have a proper solution of A′L
that meets the above conditions, which would yield θ2 ↔ θ
∗, θ∗ ↔ θ3 for some θ
∗from the first statement. Thus we will have θ1 ↔ θ3, θ3 ↔ θ∗, θ∗ ↔ θ2.

We first propose a lemma about linear independence which we will use in our later proof.

Lemma 25. For linearly independent vectors C1*, . . . , C*p ∈ R
1×r1, linearly independent vectors D1*, . . . , D*q ∈
R

1×r2, and vectors E1*, . . . , E*p ∈ R
1×r2, if r2 > p + q and r1 > q*, there exist a matrix* K ∈ R
r1×r2 such that the p + q *vectors* CiK + Ei(i = 1, 2*, . . . , p*), Di(i = 1, 2, . . . , q) are linearly independent.

Proof. Since r2 > p + q, we can find another p vectors F1*, . . . , F*p such that D1, . . . , Dq, F1*, . . . , F*p are linearly independent.

Then, we consider the p equations CiK + Ei = Fi(i = 1, 2*, . . . , p*). Since C1*, . . . , C*p ∈ R
1×r1 are independent and r1 > p, we can find a solution for K by considering each column of K separately.

Thus, with CiK + Ei = Fi(i = 1, 2*, . . . , p*) and the linear independence of D1, . . . , Dq, F1*, . . . , F*p, we finish our proof of the lemma.

Now we begin with our proof of 18.

Proof. Following the explicit description in (5), it is natural to consider whether the explicit representation of linear layers achieves A∗L
. . . A∗
2A1∗. As a set out of only zero-measure points in the minima manifold, we consider an assumption below:
Assumption 26. For all k = 1, 2*, . . . , n* − 1, the r vectors A
(i)
L
. . . A(i)
2 A
(i)
1 ∈ R
1×m(i = 1, 2*, . . . , r*) are linearly independent.

To begin, for each i ∈ [1, r], q = 1, 2*, . . . , L*, we define σ*i,k,q* to be the sum of all C
k q elements in BLBL−1 *. . . B*L−q+1
for j ∈ {1*, . . . , q*}, only k of Bj to be A
i j
, while the remaining q − k Bj to be A
∗ j
	,
(17)
With this notation, our desirable connectivity property can be written in terms that

$$(t A_{L}^{(i)}+(1-t)A_{L}^{*})(t A_{L-1}^{(i)}+(1-t)A_{L-1}^{*})\ldots(t A_{1}^{(i)}+(1-t)A_{1}^{*})=\sum_{j=0}^{L}t^{j}(1-t)^{L-j}\sigma_{i,j,L}$$

for all i = 1, 2*, . . . , r* and j = 1, 2*, . . . , L*. Since this should be right for any t ∈ [0, 1] in the context of star-shaped connectivity, it is natural to find A∗
1
, . . . , A∗L
such that σ*i,k,L* = C
k LQ for all i and k, which are the necessary condition followed by considering different order terms of t. On the other hand, if this holds, we will directly derive that each point in the star-shaped manifold is an exact minimum, i.e., for any t ∈ [0, 1],

$$(t A_{L}^{(i)}+(1-t)A_{L}^{*})(t A_{L-1}^{(i)}+(1-t)A_{L-1}^{*})\dots(t A_{1}^{(i)}+(1-t)A_{1}^{*})=\sum_{j=0}^{L}C_{L}^{j}t^{j}(1-t)^{L-j}Q=Q.$$

Now we start to construct A∗
1
, . . . , A∗L
inductively. Firstly, consider the case in Assumption 26 when k = 1. Since *m > r* + 1, we can find A∗L by Lemma 25 such that C1 = {A∗L
, A(1)
L
, . . . , A(r)
L
} are linearly independent.

Then, we consider Assumption 26 with k = 2. We notice that A∗L
, A(1)
L
, . . . , A(r)
Lare linearly independent and m > 2r + 1*, m > r*, then following Lemma 25, we can find A∗L−1 such that the 2r + 1 vectors in

$$\mathcal{C}_{L-1}=\left\{A_{L}^{(i)}A_{L-1}^{*}+A_{L}^{*}A_{L-1}^{(i)}(i=1,2,\ldots,r),A_{L}^{(i)}A_{L-1}^{(i)}(i=1,2,\ldots,r),A_{L}^{*}A_{L-1}^{*}\right\},$$  in how do it.  
are linearly independent.

We repeat the process using Assumption 2,3 and Lemma 25 to accumulate more layers while keeping with their independent property. In particular, with wr + 1(1 *< w < L* − 1) linearly independent vectors in

$$\mathcal{C}_{w}=\{\sigma_{i,k,w-1}A_{L-w+1}^{*}+\sigma_{i,k-1,w-1}A_{L-w+1}^{i}(k=1,\ldots,w-1;i=1,\ldots,r),$$ $$A_{L}^{*}A_{L-1}^{*}\ldots A_{L-w+1}^{*},A_{L}^{(i)}A_{L-1}^{(i)}\ldots A_{L-w+1}^{(i)}(i=1,2,\ldots,r)\},$$

we consider Lemma 25 to obtain K as A∗L−w, with Di being independent vectors A
(i) L
. . . A(i)
1
, i = 1, 2*, . . . , r* being ensured by Assumption 26. By doing so, we derive a new group of independent vectors

Cw+1 = {σ*i,k,w*A
∗
L−w+σi,k−1,wA
i
L−w(k = 1*, . . . , w*;i = 1, . . . , r), A∗LA
∗
L−1
. . . A∗L−w, A(i)
$${}_{v},A_{L}^{(1)}A_{L-}^{(1)}$$
(i)
L−1
. . . AiL−w(i = 1, 2*, . . . , r*)}.

Thus, by induction, we can sequentially get A∗L
, . . . , A∗
2 such that all (L − 1)r + 1 vectors

$\mathcal{C}_{L-1}=\{\sigma_{i,k,L-2}A_{2}^{*}+\sigma_{i,k-1,L-2}A_{2}^{i}(k=1,\ldots,L-2;i=1,\ldots,r),$  $$A_{L}^{*}A_{L-1}^{*}\cdots A_{2}^{*},A_{L}^{(i)}A_{L-1}^{(i)}\cdots A_{2}^{i}(i=1,2,\ldots,r)\}\.$$
$$A_{L-w}^{i}(i=1,2,\ldots$$
$\cdot\cdot\cdot A\hat{L}-v$
$\phi=\mathbb{E}_{\phi}\mathbb{E}_{\phi}$
are linearly independent.

We illustrate that keeping such linearly independent properties in induction is of essential importance in this proof, which shares the very essence in Theorem 16, providing a sufficient condition for us to obtain the proper solution of the linear equations.

Finally, recall that we aim to make sure σ*i,k,L* = C
k LQ for all i = 1, 2*, . . . , r* and k = 0, 1*, . . . , L*.

Consider that the case for k = L is naturally true, and all r equations when k = 0 are the same, we can therefore view that as (L−1)r+ 1 linear equations of variable A∗
1 since A∗L
, . . . , A∗
2 have been fixed. Since all the coefficients of A∗
1 in the (L−1)r + 1 equations are actually the (L−1)r + 1 vectors in CL−1, which are linearly independent, we can therefore find a proper solution for A∗
1 by considering each column in A∗
1 separately. The condition m > (L − 1)r + 1 in Assumption 2 makes sure of the existence of the solution.

Thus, we finish the construction of A∗L
, . . . , A∗
1
, which satisfies the required property, and finish the proof.