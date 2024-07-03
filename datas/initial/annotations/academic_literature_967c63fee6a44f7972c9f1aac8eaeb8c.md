# Exploring Neural Network Landscapes: Star-Shaped and Geodesic Connectivity 

Zhanran $\operatorname{Lin}^{* 1}$, Puheng $\mathrm{Li}^{* 2}$, and Lei $\mathrm{Wu}^{\dagger 3,4}$<br>${ }^{1}$ Department of Statistics and Data Science, Wharton School, University of Pennsylvania<br>${ }^{2}$ Department of Statistics, Stanford University<br>${ }^{3}$ School of Mathematical Sciences, Peking University<br>${ }^{4}$ Center for Machine Learning Research, Peking University

April 10, 2024


#### Abstract

One of the most intriguing findings in the structure of neural network landscape is the phenomenon of mode connectivity [FB17, DVSH18]: For two typical global minima, there exists a path connecting them without barrier. This concept of mode connectivity has played a crucial role in understanding important phenomena in deep learning.

In this paper, we conduct a fine-grained analysis of this connectivity phenomenon. First, we demonstrate that in the overparameterized case, the connecting path can be as simple as a two-piece linear path, and the path length can be nearly equal to the Euclidean distance. This finding suggests that the landscape should be nearly convex in a certain sense. Second, we uncover a surprising star-shaped connectivity: For a finite number of typical minima, there exists a center on minima manifold that connects all of them simultaneously via linear paths. These results are provably valid for linear networks and two-layer ReLU networks under a teacher-student setup, and are empirically supported by models trained on MNIST and CIFAR-10.


## 1 Introduction

It is well-known that neural networks are highly non-convex, but they can still be efficiently trained by simple algorithms like stochastic gradient descent (SGD). Understanding the underlying mechanism is crucial and in particular, a key aspect of this is to uncover the topology and geometry of neural network landscapes.

Some recent studies exploited the local properties of neural network landscapes, including the absence of spurious minima [GLM16, SC16], the sharpness of different minima [HS97, $\mathrm{KMN}^{+} 17$, WZE17], and the structures of saddle points [ZZLX21] and plateaus [AS21]. Other studies have examined the nonlocal structures, including the impact of symmetries and invariances [SGJ+21], the presence of non-attracting regions of minima [PS21], the monotonic linear interpolation[^0]phenomenon [GVS14, WWZG22, VF22, $\left.\mathrm{LBZ}^{+} 21\right]$. Among these nonlocal structures, one of the most intriguing findings is the mode connectivity, which is the focus of this paper.

Mode connectivity refers to the property that global minima of (over-parameterized) neural networks are (nearly) path-connected and form a connected manifold [Coo18], rather than being isolated. This characteristic of neural network landscape was first observed by Freeman and Bruna in [FB17], and its practical universality was later demonstrated in [DVSH18, GIP ${ }^{+}$18] through extensive large-scale experiments. Mode connectivity has attracted wide attention and has been utilized to understand many important aspects of deep learning, including the role of permutation invariance [ESSN21, AHS22], properties of SGD solutions [MFG+20, FDRC20], explaining the success of certain learning methods such as ensemble methods [GIP ${ }^{+} 18$, HHY19], and even to design methods with better generalization [BMLW21].

In this paper, we conduct a fine-grained analysis of this mode connectivity. Our specific investigation is inspired by the empirical observation that the connecting paths can be piecewise linear with as few as two pieces $\left[\mathrm{GIP}^{+} 18\right]$. This motivates us to examine the piecewise linear connectivity of the global minima manifold. Two minima are said to be $k$-piece linearly connected if they can be connected using paths with at most $k$ linear segments. Specifically, our main contributions are summarized as follows.

- We provide a theoretical analysis of the piecewise linear connectivity for two-layer ReLU networks and linear networks under a teacher-student setup. We prove that as long as the network is sufficiently over-parameterized, any two minima are 2-piece linearly connected. By exploiting this property, we further discover the following surprising structures of the global minima manifold:
- Star-shaped connectivity: For a finite set of typical minima, there exists a minimum (center) such that it is linearly connected to all these minima simultaneously.
- Geodesic connectivity: For two typical minima, the geodesic distance on the minima manifold is close to the Euclidean distance. Moreover, the ratio between them monotonically decreases towards 1 as increasing the network width. This suggests that the landscape of over-parameterized networks might be not far away from a convex one in some sense.
- We then provide extensive experiments on MNIST and CIFAR-10 datasets that confirm our theoretical findings on practical models.


### 1.1 Related works

Understanding the mode connectivity. There have been several studies that aim to theoretically explain the phenomenon of mode connectivity. The initial work by Freeman and Bruna [FB17] proved the mode connectivity for both linear networks and two-layer ReLU networks when the model is regularized by squared $\ell_{2}$ norm. [GIP $\left.{ }^{+} 18\right]$ empirically discovered that connecting paths can be piecewise linear. Based on this observation, $\left[\mathrm{KWL}^{+} 19\right]$ proved that if two minima satisfy certain conditions such as the dropout stability and noise stability, then they can be connected using paths with at most 10 linear segments. Moreover, the result in $\left[\mathrm{KWL}^{+} 19\right]$ is applicable to deep neural networks. [SM20] provided a theoretical explanation of why SGD tends to find solutions that satisfy the dropout stability for two-layer neural networks. In addition to these studies, [NMH18, NBM21a, NBM21b] investigated how the connectivity depends on the network width and depth, but the analysis does not provide any information about the structure
![](https://cdn.mathpix.com/cropped/2024_04_26_1e005a33dbad0096ad20g-03.jpg?height=500&width=1356&top_left_y=216&top_left_x=362)

Figure 1: Left: The speculation of a potential shape of the star-shaped connectivity in the loss landscape. Due to the limitation in 2-dimensional visualization, here we only provide a potential section as a heuristic plot. Right: For 2 minima $\theta_{1}, \theta_{2}$ as described in the setting of Proposition 16, we consider the linear mode connectivity through a center $\theta^{*}$. For the linear interpolations between two minima, and the $\theta_{1} \rightarrow \theta^{*} \rightarrow \theta_{2}$ fold-lines constructed by two linear interpolations, we plot the training loss along these paths. Specifically, the $x$-axis $t$ here denotes the point $t \theta^{*}+(1-t) \theta_{i}$ in the linear interpolation (the orange line). On the other hand, for the loss along the fold-line (blue line), $t<0.5$ corresponds to the point $2 t \theta^{*}+(1-2 t) \theta_{1}$, while $t \geq 0.5$ corresponds to $(2 t-1) \theta_{2}+(2-2 t) \theta^{*}$. The result shows our expectation of linear mode connectivity through the center we obtained.

of the connecting paths. In contrast, we investigate the particular structure of connecting paths and provide both empirical and theoretical evidence showing that when networks are sufficiently over-parameterized, typical minima can be connected using paths of merely 2 linear segment. Moreover, we also explore the geometry of the global minima manifold by using the simplicity of connecting paths.

Critical points. [FYMT19, ZZLX21] studied the hierarchical structures of critical points and in particular, how local minima degenerate to saddle points when increasing the number of neurons. [RABC19, MAB20] provided an analytical characterization of the distribution of critical points for learning a single neuron in an asymptotic regime by using the Kac-Rice replicated method from statistical physics. [AS21, FA00, YO19] studied the appearance of plateaus in the neural network landscape and its impact on the training process. In addition, it has been always a major problem to understand under what conditions bad local minima/valley disappear [Kaw16, SC16, LSLS18, LSZ22] or not [AHW95, SS18, YSJ18, DLS22, LK17]. Another line of works inspects curvatures at minima [SEG $\left.{ }^{+} 17\right]$ and how the curvatures of the local landscape are related to the generalization of networks represented by those minima [HS97, WZE17, JKA ${ }^{+} 17$, MY21, WWS]. In this paper, we study the topology and geometry of global minima by utilizing the mode connectivity.

Nonlocal structures. Note that the mode connectivity is nonlocal in nature. Therefore, our work is also helpful for understanding the nonlocal structures of the neural network landscape. [FJ19] proposed a phenomenological model (a set of high dimensional wedges) to study large-scale structures of neural network landscape. [GVS14] discovered the surprising monotonic linear interpolation (MLI) phenomenon: the loss often decreases monotonically in the linear interpolation between random initialization and minima found by SGD. [WWZG22, VF22, LBZ ${ }^{+} 21$ ] provided theoretical analyses of MLI phenomenon. [Coo18] proved that in the over-parameterized case,
global minima form a high-dimensional manifold and this minima manifold is path connected as implied by the mode connectivity phenomenon [GIP ${ }^{+}$18, FB17, DVSH18]. Recently, [ALL $\left.{ }^{+} 23\right]$ showed a star-shaped structure in the regime of the spherical negative perceptron. We instead provide both theoretical and empirical evidence, showing that star-shaped structure also exists for neural networks.

## 2 Preliminaries

Notation. For an integer $n$, let $[n]=\{1,2, \ldots, n\}$. For a compact $\Omega$, denote by $\operatorname{Unif}(\Omega)$ the uniform distribution over $\Omega$. Let $\mathbb{S}^{d-1}=\left\{\mathbf{x} \in \mathbb{R}^{d}:\|\mathbf{x}\|_{2}=1\right\}$ and $\tau_{d-1}=\operatorname{Unif}\left(\mathbb{S}^{d-1}\right)$. Denote by $\left\{\mathbf{e}_{j}\right\}_{j=1}^{d}$ the canonical basis of $\mathbb{R}^{d}$.

Let $f: \mathcal{X} \times \Theta \mapsto \mathcal{Y}$ be a neural network with $\mathcal{X}$ and $\Theta$ denoting the input space and parameter space, respectively. Let $\ell: \mathcal{Y} \times \mathcal{Y} \mapsto \mathbb{R}$ be a loss function. Then the loss landscape is determined by $\mathcal{R}(\theta)=\mathbb{E}_{(\mathbf{x}, y) \sim \mathcal{D}}[\ell(f(\mathbf{x} ; \theta), y)]$, where $\mathcal{D}$ denotes the input distribution. In this paper, we make the over-parameterization assumption: $\inf _{\theta \in \Theta} \mathcal{R}(\theta)=0$. Then, the global minima manifold is given by

$$
\mathcal{M}=\{\theta \in \Theta: \mathcal{R}(\theta)=0\}
$$

For any $\theta_{1}, \theta_{2} \in \mathcal{M}$, denote by $\mathcal{P}_{\theta_{1}, \theta_{2}}$ the space of paths on $\mathcal{M}$ connecting $\theta_{1}$ and $\theta_{2}$ :

$$
\mathcal{P}_{\theta_{1}, \theta_{2}}=\left\{\gamma:[0,1] \mapsto \mathcal{M} \mid \gamma(0)=\theta_{1}, \gamma(1)=\theta_{2}\right\}
$$

Existing works on mode connectivity imply that under some conditions, $\mathcal{M}$ is path connected, i.e., $\mathcal{P}_{\theta_{1}, \theta_{2}} \neq \emptyset$ for typical $\theta_{1}, \theta_{2} \in \mathcal{M}$. In this paper, we make a refined analysis of the connectivity. To be rigorous, we formalize some concepts that we shall use throughout this paper below.

Definition 1 (Linear interpolation). For any $\theta_{1}, \theta_{2} \in \Theta$, denote by $\gamma_{\theta_{1}, \theta_{2}}^{\operatorname{lin}}:[0,1] \rightarrow \Theta$ the linear interpolation path defined as $\gamma(t)=t \theta_{1}+(1-t) \theta_{2}, t \in[0,1]$.

Definition 2 ( $k$-piece linear connectivity). For any $\theta_{1}, \theta_{2} \in \mathcal{M}$, we write $\theta_{1} \leftrightarrow \theta_{2}$ if $\gamma_{\theta_{1}, \theta_{2}}^{\operatorname{lin}} \subset \mathcal{M}$. We say $\theta_{1}$ and $\theta_{2}$ are $k$-piece linearly ( $k$-PL) connected if there exist $\beta_{1}, \ldots, \beta_{k-1} \in \mathcal{M}$ such that $\theta_{1} \leftrightarrow \beta_{1} \leftrightarrow \cdots \leftrightarrow \beta_{k-1} \leftrightarrow \theta_{2}$. Particularly, the case of $k=1$ is referred to as linear connectivity.

Definition 3 (Star-shaped linear connectivity). For multiple minima $S=\left\{\theta_{i}\right\}_{i=1}^{r} \subset \mathcal{M}$, we refer to the star-shaped linear connectivity as there exists a $\theta^{*} \in \mathcal{M}$ such that $\theta_{i} \leftrightarrow \theta^{*}$ for all $i=1,2, \ldots, r$. Specifically, $\theta^{*}$ and $S$ are said to be the center and feet, respectively.

In this paper, we also consider another quantity to measure the strength of connectivity.

Definition 4 (Normalized geodesic distance (NGD)). For any $\theta_{1}, \theta_{2} \in \mathcal{M}$, define the normalized geodesic distance between $\theta_{1}$ and $\theta_{2}$ by

$$
G\left(\theta_{1}, \theta_{2}\right)=\frac{\inf _{\gamma \in \mathcal{P}_{\theta_{1}, \theta_{2}}} \int_{0}^{1}\left\|\gamma^{\prime}(t)\right\|_{2} \mathrm{~d} t}{\left\|\theta_{1}-\theta_{2}\right\|_{2}}
$$

If $\mathcal{P}_{\theta_{1}, \theta_{2}}$ is an empty set, set $G\left(\theta_{1}, \theta_{2}\right)=+\infty$.

If the landscape is convex, it is trivial that the NGD is exactly 1 for any pair of global minima since the geodesic is simply the linear interpolation. However, for nonconvex landscapes, the NGD is always strictly greater than 1 . The value of NGD can serve as a factor to quantify the degree of non-convexity. If the NGD keeps close to 1 for any pair of minima, then the landscape should be somehow as benign as a convex one. Otherwise, the landscape must be highly nonconvex. We are particularly interested in how the value of NGD changes as increasing the level of over-parameterization.

## 3 Two-layer ReLU networks

We first consider the two-layer ReLU network under a teacher-student setup, where the label is generated by a teacher network: $f^{*}(\mathbf{x})=\sum_{j=1}^{M} \sigma\left(\mathbf{w}_{j}^{*} \cdot \mathbf{x}\right)$. Here the activation function $\sigma: \mathbb{R} \mapsto \mathbb{R}$ is given by $\sigma(z):=\max (0, z)$. We make the following assumption.

Assumption 5. Suppose $M \leq d, \mathbf{w}_{j}^{*}=\mathbf{e}_{j}$ for $j=1, \ldots, M$, and $\mathbf{x} \sim \tau_{d-1}$.

By the rotational symmetry, the specific assumption that $\mathbf{w}_{j}^{*}=\mathbf{e}_{j}$ for $j=1, \ldots, M$ is equivalent to only assume $\left\{\mathbf{w}_{j}^{*}\right\}_{j=1}^{M}$ to be orthonormal. However, we will focus on Assumption 5 to make our statement more succinct. In such a case, the loss objective can be rewritten as

$$
\mathcal{R}(\theta)=\mathbb{E}_{\mathbf{x} \sim \tau_{d-1}}\left[\left(\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i} \cdot \mathbf{x}\right)-\sum_{i=1}^{M} \sigma\left(x_{i}\right)\right)^{2}\right]
$$

where $m$ denotes the number of neurons of the student network and $\theta=\left(\mathbf{w}_{1}, \mathbf{w}_{2}, \ldots, \mathbf{w}_{m}\right)^{T}=$ $\left(w_{i, j}\right) \in \mathbb{R}^{m \times d}$. Using this notation, each row of $W$ represents a student neuron.

Assumption 5 allows us to obtain the following analytic characterization of the global minima manifold. This characterization will play a critical role in our theoretical analysis and might be of independent interest to other related problems as well.

Theorem 6. Suppose that $m \geq M$ and Assumption 5 hold. Let $S_{0}=\left\{(0, \ldots, 0) \in \mathbb{R}^{d}\right\}$, $S_{j}=\left\{\alpha \mathbf{e}_{j}: \alpha \neq 0\right\}$ for $j \in[M]$, and $S=\cup_{j=0}^{M} S_{j}$. Then the global minima manifold $\mathcal{M}$ is a compact set in $\mathbb{R}^{m \times d}$ :

$$
\mathcal{M}=\left\{\theta=\left(\mathbf{w}_{1}, \ldots, \mathbf{w}_{m}\right)^{T} \in \mathbb{R}^{m \times d}: \forall i \in[m], \mathbf{w}_{i} \in S \text { and } \forall j \in[M], \sum_{i=1}^{m} w_{i, j}=1\right\}
$$

The proof is deferred to Appendix A.1. Note that $S_{j} \cap S_{k}=\emptyset$ for any $j \neq k \in\{0,1, \ldots, M\}$. Hence Theorem 6 implies the following facts about the global minima:

- There are at most $m+1$ types of student neurons, represented by $S_{0}, S_{1}, \ldots, S_{M}$, regardless of how overparameterized the student network is. Moreover, for any $j \in[M]$, there exists at least one student neuron taking the type of $S_{j}$.
- For each neuron, there exists at most one coordinate to be nonzero and the coordinates from $M+1$ to $d$ must be zero.

The following lemma provides a precise condition of when two global minima are linearly connected, which will be used in our subsequent analysis.

Lemma 7 (Linear connectivity). For any two global minima $\theta^{(1)}=\left(\mathbf{w}_{1}^{(1)}, \ldots, \mathbf{w}_{m}^{(1)}\right)^{T}$, $\theta^{(2)}=\left(\mathbf{w}_{1}^{(2)}, \ldots, \mathbf{w}_{m}^{(2)}\right)^{T} \in \mathbb{R}^{m \times d}$, we have $W^{(1)} \leftrightarrow W^{(2)}$ if and only for any $i \in\{1, \ldots, m\}$, one of the following happens:

- $\mathbf{w}_{i}^{(1)} \in S_{0}$ or $\mathbf{w}_{i}^{(2)} \in S_{0}$;
- there exists $j \in\{1, \ldots, M\}$ such that $\mathbf{w}_{i}^{(1)} \in S_{j}$ and $\mathbf{w}_{i}^{(2)} \in S_{j}$.

The above lemma (proof deferred to Appendix A.1) means that if $\theta_{1} \leftrightarrow \theta_{2}$, then for any $i \in[m]$, the nonzero coordinates of $\mathbf{w}_{i}^{(1)}$ and $\mathbf{w}_{i}^{(2)}$ must be the same if they are not zero simultaneously.

### 3.1 The $k$-piece linear connectivity

Theorem 8. Suppose $m>M$ and two minima $\theta^{(1)}, \theta^{(2)}$ are i.i.d. drawn from $\operatorname{Unif}(\mathcal{M})$. Then, w.p. at least $p_{m, M}=1-M\left(\frac{M^{2}-1}{M^{2}}\right)^{m-2 M}, \theta^{(1)}$ and $\theta^{(2)}$ are $2-P L$ connected.

The proof of this theorem can be found in Appendix A.2. Notice that the probability $p_{m, M} \rightarrow 1$ as $m \rightarrow \infty$, implying that when the student is sufficiently over-parameterized, the 2-PL connectivity holds with probability nearly 1 . Quantitatively speaking, for any $\delta \in(0,1)$, $m \geq C M^{2} \log (M / \delta)$ is sufficient to guarantee that the probability of 2-PL connectivity is no less than $1-\delta$.

The following theorem further shows that if allowing the number of pieces to be slightly larger, then the $k$-PL connectivity holds for two global minima.

Theorem 9. Suppose $m \geq 2 M-1$, then any two global minima are 4-PL connected.

The proof is deferred to Appendix A.3.

### 3.2 Star-shaped connectivity

Theorem 10. Suppose $m>M$ and let $\theta_{1}, \theta_{2}$ be two minima i.i.d. drawn from $\operatorname{Unif}(\mathcal{M})$. Then, w.p. at least $1-M\left(\frac{M^{k}-1}{M^{k}}\right)^{m-k M}$, there exists a center $\theta^{*} \in \mathcal{M}$ such that $\theta^{i} \leftrightarrow \theta^{*}$ for all $i \in[k]$.

A simple calculation implies that to ensure the probability larger than $1-\delta$, we need $m \geq$ $C M^{k} \log (M / \delta)$. The following theorem shows by allowing the connectivity between feet and the center to be two-piece linear path, then the probability becomes exactly 1 as long as $m \geq k M$.

Theorem 11. Given $k \in \mathbb{N}$, suppose $m \geq k M$. For any $k$ global minima $\theta_{1}, \ldots, \theta_{k}$, we can find a center $\theta^{*}$ such that $\theta^{*}$ and $\theta_{i}$ are 2 - $P L$ connected for any $i=1, \ldots, k$.

The proofs of Theorem 10 and Theorem 11 can be found in Appendix A. 4 and A.5, respectively. In Figure 2, we provide an illustration of the difference in how the feet are connected to the star center between Theorem 10 and Theorem 11.
![](https://cdn.mathpix.com/cropped/2024_04_26_1e005a33dbad0096ad20g-06.jpg?height=452&width=944&top_left_y=1652&top_left_x=598)

Figure 2: Left. The original star-shaped connectivity. The five white circles are the feet and the red circle is the center. The blue line represents the linear connecting path. Right. The extended star-shaped connectivity is proved in Theorem 11, where the feet are connected to the center via a two-piece linear path.

### 3.3 The geodesic connectivity

The left of Figure 3 shows the normalized geodesic distances (NGDs) between minima found by SGD for the two-layer ReLU networks mentioned above. We can see clearly that the value of NGD decreases monotonically towards 1 as the network width $m$ increases. This implies that the landscape of wide networks should be somehow not far from a convex one. This is consistent with our intuition that wider networks should have a simpler landscape than narrow networks. Below, we provide some theoretical evidence to explain this mysterious phenomenon.
![](https://cdn.mathpix.com/cropped/2024_04_26_1e005a33dbad0096ad20g-07.jpg?height=494&width=1292&top_left_y=628&top_left_x=384)

Figure 3: Left. How the normalized geodesic distance (NGD) changes with the network width for two-layer ReLU networks. The teacher network has $M=4$ neurons and we refer to Section 5 for the algorithm of estimating NGD. Right. The $L^{2}$ norm of each neuron for SGD solutions. Here, $m=512, M=4, d=4$. One can see that SGD tends to find sparse solutions.

Theorem 12. Suppose $m>M$, and let $\theta_{1}, \theta_{2}$ be two minima independently drawn from $\operatorname{Unif}(\mathcal{M})$. Then there exists absolute constants $c_{1}, c_{2}>0$ such that w.p. at least $1-c_{1} e^{-m}$ that $G\left(\theta_{1}, \theta_{2}\right) \leq$ $c_{2} \sqrt{M}$. Moreover, the upper bound can be achieved by a two-piece linear path.

The proof is deferred to Appendix A.6. This theorem shows that the NGD between uniformly sampled minima is independent of the level of over-parameterization. However, Figure 3 shows that NGD shrinks to 1 when increasing the network width for minima found by SGD. We hypothesize that SGD induces a biased distribution over the minima manifold. In the right of Figure 3, we visualize the magnitude of different neurons for an SGD solution. We observe that SGD tends to find solutions with sparse structures, i.e., only a few dominant neurons contribute.

To study the influence of neuron sparsity on the geodesic connectivity, we define the following distribution to formulate the sparsity bias.

Definition 13 (Neuron-sparse distribution). For any absolute constant $0<r<1$, we define $\operatorname{SP}(\mathcal{M}, r)$, the neuron-sparse distribution with a sparsity $r$ over $\mathcal{M}$, as following: for $\theta=\left(\mathbf{w}_{1}, \ldots, \mathbf{w}_{m}\right)^{T}$, for any $i \in\{1, \ldots, m\}, P\left(\mathbf{w}_{i} \in S_{0}\right)=r$ and $P\left(\mathbf{w}_{i} \in S_{j}\right)=\frac{1-r}{M}$ for $j \in\{1, \ldots, M\}$.

Theorem 14. Suppose $m>M$ and let $\theta_{1}, \theta_{2}$ be two minima independently drawn from $\operatorname{SP}(\mathcal{M}, r)$. Then there exists two absolute constants $c_{1}, c_{2}>0$ such that w.p.at least $1-c_{1} M e^{-m r^{2}}$ that $G\left(\theta_{1}, \theta_{2}\right) \leq 1+\frac{c_{2}}{r \sqrt{m}}$. Moreover, the upper bound can be achieved by a two-piece linear path.

The proof is deferred to Appendix A.7. This theorem demonstrates that the bias towards sparse solutions can explain the shrinkage of NGD to 1. In particular, when $m \rightarrow \infty$, NGD approaches to 1 .

## 4 Linear networks

A linear network $f(\cdot ; \theta): \mathbb{R}^{d} \mapsto \mathbb{R}$ is parameterized by $f(\mathbf{x} ; \theta)=A_{L} A_{L-1} \ldots A_{1} \mathbf{x}$, where $A_{l} \in$ $\mathbb{R}^{m_{l} \times m_{l-1}}$ for $l=1,2, \ldots, L$. Here $L$ denotes the network depth and $\left\{m_{l}\right\}_{l=0}^{L}$ denotes the widths. Note that $m_{0}=d$ and $m_{L}=1$ and we assume $m_{2}=\cdots=m_{L-1}=m$ for simplicity. We make the following assumption on the data distribution.

Assumption 15. Suppose that $y=Q \mathbf{x}$ for some $Q \in \mathbb{R}^{1 \times d}, \mathbb{E}[\mathbf{x}]=0$, and $\lambda_{\min }\left(\mathbb{E}\left[\mathbf{x x}^{T}\right]\right)>0$.

The above assumption is quite mild but ensures that the global minima manifold has the following analytic characterization:

$$
\mathcal{M}=\left\{\left(A_{L}, A_{L-1}, \ldots, A_{1}\right): A_{L} A_{L-1} \cdots A_{1}=Q\right\}
$$

The following theorem provides the characterization of $k$-PL connectivity of the loss landscape of linear networks. The proof can be found in Appendix B.

Theorem 16. Let $f(\cdot ; \theta)$ be the linear network described in Section 4. Let $\theta_{1}, \theta_{2} \in \mathcal{M}$ be two global minima. If $m>2 L-1$, then we have:

- Two global minima are almost surely 2-PL connected;
- Any two global minima are 3-PL connected,

We remark that the "almost surely" condition in characterizing the 2-PL connectivity cannot be removed. The following lemma provides a counterexample, showing that there indeed exist pathological minima that are not 2-PL connected.

Lemma 17. Consider the case of $m=4, d=1, L=2$ and the target $y=x$. Then, we have $\mathcal{M}=\left\{(a, b) \in \mathbb{R}^{m} \otimes \mathbb{R}^{m}: a^{T} b=1\right\}$. Consider two global minima $\theta_{1}=\left(A_{1}^{(1)}, A_{1}^{(2)}\right)$, $\theta_{2}=\left(A_{2}^{(1)}, A_{2}^{(2)}\right)$ with

$$
A_{1}^{(1)}=(1,0,0,0), A_{2}^{(1)}=(1,0,0,0)^{T}, \quad A_{1}^{(2)}=(-1,0,0,0), A_{2}^{(2)}=(-1,0,0,0)^{T}
$$

Then, $\theta_{1}$ and $\theta_{2}$ are not 2-PL connected. Quantitatively,

$$
\inf _{\theta \in \mathcal{M}}\left(\int_{0}^{1} \mathcal{R}\left(t \theta_{1}+(1-t) \theta\right) \mathrm{d} t+\int_{0}^{1} \mathcal{R}\left(t \theta_{2}+(1-t) \theta\right)\right) \mathrm{d} t \geq \frac{4}{15} \mathbb{E} x^{2}
$$

Theorem 18 (star-shaped linear connectivity). Consider linear networks of depth $L$ and width m. Let $\left\{\theta_{i}\right\}_{i=1}^{r}$ be $r$ global minima. If $m>1+r(L-1)$, then we almost surely (with respect to the Lebesgue measure over $\mathcal{M}^{\otimes r}$ ) have that there exist a $\theta^{*} \in \mathcal{M}$ such that $\theta^{*} \leftrightarrow \theta_{i}$ for all $i=1, \ldots, r$.

Here $\mathcal{M}^{\otimes r}=\left\{\left(\theta_{1}, \ldots, \theta_{r}\right) \in \mathbb{R}^{r}: \theta_{i} \in \mathcal{M}\right.$ for $\left.i \in[r]\right\}$. This theorem establishes that when linear networks are sufficiently wide, the star-shaped connectivity holds almost surely. The proof can be found in Appendix B.1.

The geodesic connectivity. In Figure 4, we empirically demonstrate that the Normalized Geodesic Distances (NGDs) for linear networks are also close to 1. Additionally, we observe that the NGD monotonically decreases with increasing network width, although this phenomenon has not yet been theoretically proven.

![](https://cdn.mathpix.com/cropped/2024_04_26_1e005a33dbad0096ad20g-09.jpg?height=520&width=784&top_left_y=255&top_left_x=627)

Figure 4: Normalized geodesic distance vs. network width for linear networks. Following the setting as described earlier in this section, we consider a fully connected linear network with $L=2$. We set $d=m$, and vary $m$ to consider the normalized geodesic distance of a center with 2-PL-connectivity. Algorithm 5 is applied here to train a center and the result is an average of 5 separate experiments. It is shown that as the width increases, we can obtain a center that satisfies 2-PL-connectivity with a shorter geodesic distance.

## 5 Experiments

In this section, we provide experiments to validate the star-shaped and geodesic connectivity across a range of architectures and datasets.

The center-finding algorithm. Given a set of minima $S=\left\{\theta_{i}^{*}\right\}_{i=1}^{r}$, to find a center $\theta$ that connects to all of them via linear paths, we propose to minimize the following objective

$$
\mathcal{J}_{S}(\theta):=\frac{1}{r} \sum_{i=1}^{r}\left(\mathbb{E}_{t \sim U[0,1]}\left[\mathcal{R}\left(t \theta+(1-t) \theta_{i}^{*}\right)\right]+\lambda p\left(\theta, \theta_{i}^{*}\right)\right)
$$

where $p(\cdot, \cdot)$ is a penalization function to be determined later. To efficiently solve this optimization problem, we use the Adam [KB14] optimizer with the minibatch gradient:

$$
\nabla \widehat{\mathcal{J}}_{S}(\theta)=\nabla\left(\frac{1}{B_{r} B_{t}} \sum_{k=1}^{B_{r}} \sum_{j=1}^{B_{t}} \mathcal{R}\left(t_{j} \theta_{t}+\left(1-t_{j}\right) \theta_{i_{k}}^{*}\right)+\frac{\lambda}{B_{r}} \sum_{k=1}^{B_{r}} p\left(\theta_{t}, \theta_{i_{k}}^{*}\right)\right)
$$

where $i_{k} \stackrel{\text { i.i.d. }}{\sim} \operatorname{Unif}([r])$ and $t_{j} \stackrel{\text { i.i.d. }}{\sim} \operatorname{Unif}([0,1])$ for $k \in\left[B_{r}\right]$ and $j \in\left[B_{t}\right]$. Here, $B_{r}, B_{t} \in \mathbb{N}$ denote the batch sizes. Across all our experiments, we always set $B_{r}=1, B_{t}=3$.

Estimating the normalized geodesic distance. Given two minima $\theta_{1}^{*}$ and $\theta_{2}^{*}$, we first find a center $\tilde{\theta} \in \mathcal{M}$ by minimizing the objective (6) for $S=\left\{\theta_{1}^{*}, \theta_{2}^{*}\right\}$ and $p\left(\theta, \theta^{\prime}\right)=\left\|\theta-\theta^{\prime}\right\|_{2}^{2}$. This allows us to find a minimum on the minima manifold such that it connects to both $\theta_{1}^{*}$ and $\theta_{2}^{*}$ via the shortest linear paths. Moreover, by Definition 4, it holds for any $\theta \in \mathcal{M}$, satisfying $\theta \leftrightarrow \theta_{i}^{*}$ for $i=1,2$, that

$$
G\left(\theta_{1}^{*}, \theta_{2}^{*}\right) \leq \frac{\left\|\theta_{1}^{*}-\theta\right\|_{2}+\left\|\theta-\theta_{2}^{*}\right\|_{2}}{\left\|\theta_{1}^{*}-\theta_{2}^{*}\right\|_{2}}
$$

Then, plugging $\tilde{\theta}$ into the right hand side of (8) gives an upper bound of $G\left(\theta_{1}^{*}, \theta_{2}^{*}\right)$.

The experiment setup. To validate our theoretical findings for practical models, we train fully-connected neural networks (FNNs) and VGG16 [SZ14] for classifying MNIST [LBBH98] dataset, and VGG16 [SZ14] and ResNet34 [HZRS16] for classifying CIFAR-10 [KH+09] dataset, respectively:

- The FNN is three-layer, whose architecture is $728 \rightarrow 500 \rightarrow 300 \rightarrow 10$. We trained FNNs under the hyperparameters: $\operatorname{lr}=1 \mathrm{e}-3$ and batchsize $=200$,
- The architecture of VGG16 and ResNet34 can be found in [SZ14] and [HZRS16], respectively. We trained VGG16 and ResNet34 under the hyperparameters: $\mathrm{lr}=5 \mathrm{e}-3$ and batchsize $=200$.

As for the center-finding algorithm, we set $B_{r}=1, B_{t}=3$ as mentioned above, and learning rate $\eta=0.01$. For all cases, the Adam optimizer [KB14] is adopted.

### 5.1 Star-shaped connectivity

In Figure 5, we visualize the star-shaped connectivity for VGG-16 in classifying the CIFAR10 dataset. We independently train the model to find 3 minima $\left\{\theta_{i}^{*}\right\}_{i=1}^{3}$ and then run the centerfinding algorithm to locate a center $\theta_{\mathrm{c}^{*}}$ on the minima manifold. We can see that the linear interpolation between any pair minima among the three ones indeed encounters a very high barrier. However, through the center $\theta_{\mathrm{c}}$, the three minima form a star-shaped connectivity.

In Table 1, we provide more experiments for a variety of model architectures and training datasets. We can see that the star-shaped connectivity holds for all scenarios examined.
![](https://cdn.mathpix.com/cropped/2024_04_26_1e005a33dbad0096ad20g-10.jpg?height=552&width=1508&top_left_y=1382&top_left_x=300)

Figure 5: An validation of star-shaped connectivity. The model is VGG16 and the dataset is CIFAR-10. We examine 3 minima obtained by running Adam independently. Then we applied the center-finding algorithm to obtain the corresponding center. For all the 3 linear interpolations between minima, and all the 3 "minimum-center-minimum" fold-lines constructed by two linear interpolations, we plot the training loss (left) and accuracy (right) along these paths. Specifically, the $x$-axis $t$ here denotes the point $t \theta^{*}+(1-t) \theta_{i}$ in the linear interpolation (the orange line). On the other hand, for a pair $\left(\theta_{i}, \theta_{j}\right)$ (blue line), $t<0.5$ corresponds to the point $2 t \theta^{*}+(1-2 t) \theta_{i}$, while $t \geq 0.5$ corresponds to $(2 t-1) \theta_{j}+(2-2 t) \theta^{*}$. It is shown in the experiment that our algorithm successfully found a center that is linearly connected to all three minima simultaneously, i.e., forms a star-shaped connectivity.

![](https://cdn.mathpix.com/cropped/2024_04_26_1e005a33dbad0096ad20g-11.jpg?height=455&width=1220&top_left_y=214&top_left_x=450)

Table 1: For different models and datasets, we independently trained 5 minima using Adam optimizer. Then, we run the path-finding algorithm with $B_{r}=1, B_{t}=3$ for 200 epochs. For all the 10 linear interpolations between minima, and all the 10 "minimum-center-minimum" fold-lines constructed by two linear interpolations, we computed the maximum (for loss) or minimum (for accuracy) and averaged them, which is denoted as "barrier". It is shown that there is nearly no barrier on the fold-lines we constructed, which validates that our observation of star-shaped connectivity holds for a wide range of settings.

### 5.2 The geodesic connectivity

In Table 2, we report the NGDs estimated by the aforementioned algorithm. It is demonstrated that minima (found by the commonly-used Adam optimizers) can be connected via paths whose NGDs are nearly 1 . This is consistent with our theoretical findings in toy models.

|  | FNN+MNIST | VGG16+MNIST | VGG16+CIFAR10 | ResNet18+CIFAR10 |
| :---: | :---: | :---: | :---: | :---: |
| NGD | 1.003 | 1.001 | 1.051 | 1.003 |
| Barrier | $99.89 \%$ | $99.25 \%$ | $99.91 \%$ | $99.63 \%$ |

Table 2: The upper bound of NGD estimated via Eq. 8 for different networks and datasets. We independently trained 2 minima in each setting, then trained the center via the centerfinding algorithm with a penalized term. It turns out that we can obtain great linear mode connectivity via a fold-line, as well as keeping the relative distance proportion controlled.

## 6 Conclusion

In this paper, we systematically investigate the star-shaped and geodesic connectivity phenomenon for the landscape of neural networks. We provide theoretical analysis on toy models such as two-layer ReLU networks and linear networks, as well as experimental validations on popular networks trained on MNIST and CIFAR-10 datasets. Our findings reveal that the neural network landscape has many simple structures. Specifically, the star-shaped phenomenon suggests a connectivity property stronger than mode connectivity. The geodesic connectivity indicates that the loss landscape might be not far from being convex in a certain sense. For future work, it would be interesting to explore the potential relationships between our findings and optimization and generalization in neural networks.

## Acknowledgements

The work is supported by the National Key R\&D Program of China (No. 2022YFA1008200) and National Natural Science Foundation of China (No. 12288101).

## References

[AHS22] Samuel K Ainsworth, Jonathan Hayase, and Siddhartha Srinivasa, Git re-basin: Merging models modulo permutation symmetries, arXiv preprint arXiv:2209.04836 (2022).

[AHW95] Peter Auer, Mark Herbster, and Manfred KK Warmuth, Exponentially many local minima for single neurons, Advances in Neural Information Processing Systems, vol. 8, 1995.

$\left[\mathrm{ALL}^{+}{ }^{23]}\right.$ Brandon Livio Annesi, Clarissa Lauditi, Carlo Lucibello, Enrico M Malatesta, Gabriele Perugini, Fabrizio Pittorino, and Luca Saglietti, Star-shaped space of solutions of the spherical negative perceptron, Physical Review Letters 131 (2023), no. 22, 227301.

[AS21] Mark Ainsworth and Yeonjong Shin, Plateau phenomenon in gradient descent training of relu networks: Explanation, quantification, and avoidance, SIAM Journal on Scientific Computing 43 (2021), no. 5, A3438-A3468.

[BMLW21] Gregory Benton, Wesley Maddox, Sanae Lotfi, and Andrew Gordon Gordon Wilson, Loss surface simplexes for mode connecting volumes and fast ensembling, International Conference on Machine Learning, PMLR, 2021, pp. 769-779.

[Coo18] Yaim Cooper, The loss landscape of overparameterized neural networks, arXiv preprint arXiv:1804.10200 (2018).

[DLS22] Tian Ding, Dawei Li, and Ruoyu Sun, Suboptimal local minima exist for wide neural networks with smooth activations, Mathematics of Operations Research (2022).

[DVSH18] Felix Draxler, Kambis Veschgini, Manfred Salmhofer, and Fred Hamprecht, Essentially no barriers in neural network energy landscape, International Conference on Machine Learning, PMLR, 2018, pp. 1309-1318.

[ESSN21] Rahim Entezari, Hanie Sedghi, Olga Saukh, and Behnam Neyshabur, The role of permutation invariance in linear mode connectivity of neural networks, International Conference on Learning Representations, 2021.

[FA00] Kenji Fukumizu and Shun-ichi Amari, Local minima and plateaus in hierarchical structures of multilayer perceptrons, Neural Networks 13 (2000), no. 3, 317-327.

[FB17] C Daniel Freeman and Joan Bruna, Topology and geometry of half-rectified network optimization, 5th International Conference on Learning Representations, 2017.

[FDRC20] Jonathan Frankle, Gintare Karolina Dziugaite, Daniel Roy, and Michael Carbin, Linear mode connectivity and the lottery ticket hypothesis, International Conference on Machine Learning, PMLR, 2020, pp. 3259-3269.

[FJ19] Stanislav Fort and Stanislaw Jastrzebski, Large scale structure of neural network loss landscapes, Advances in Neural Information Processing Systems 32 (2019).

[FYMT19] Kenji Fukumizu, Shoichiro Yamaguchi, Yoh-ichi Mototake, and Mirai Tanaka, Semi-flat minima and saddle points by embedding neural networks to overparameterization, Advances in Neural Information Processing Systems 32 (2019).

[GIP+18] Timur Garipov, Pavel Izmailov, Dmitrii Podoprikhin, Dmitry P Vetrov, and Andrew G Wilson, Loss surfaces, mode connectivity, and fast ensembling of DNNs, Advances in Neural Information Processing Systems 31 (2018).

[GLM16] Rong Ge, Jason D Lee, and Tengyu Ma, Matrix completion has no spurious local minimum, Advances in Neural Information Processing Systems 29 (2016).

[GVS14] Ian J Goodfellow, Oriol Vinyals, and Andrew M Saxe, Qualitatively characterizing neural network optimization problems, arXiv preprint arXiv:1412.6544 (2014).

[HHY19] Haowei He, Gao Huang, and Yang Yuan, Asymmetric valleys: Beyond sharp and flat local minima, Advances in Neural Information Processing Systems 32 (2019).

[HS97] Sepp Hochreiter and Jürgen Schmidhuber, Flat minima, Neural Computation 9 (1997), no. 1, $1-42$.

[HZRS16] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun, Deep residual learning for image recognition, Proceedings of the IEEE conference on computer vision and pattern recognition, 2016 , pp. 770-778.

$\left[\mathrm{JKA}^{+}{ }^{17]}\right.$ Stanisław Jastrzębski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua Bengio, and Amos Storkey, Three factors influencing minima in SGD, arXiv preprint arXiv:1711.04623 (2017).

[Kaw16] Kenji Kawaguchi, Deep learning without poor local minima, Advances in Neural Information Processing Systems 29 (2016).

[KB14] Diederik P Kingma and Jimmy Ba, Adam: A method for stochastic optimization, arXiv preprint arXiv:1412.6980 (2014).

$\left[\mathrm{KH}^{+} 09\right]$ Alex Krizhevsky, Geoffrey Hinton, et al., Learning multiple layers of features from tiny images, 2009.

$\left[\mathrm{KMN}^{+}\right.$17] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang, On large-batch training for deep learning: Generalization gap and sharp minima, International Conference on Learning Representations, 2017.

[KWL ${ }^{+}$19] Rohith Kuditipudi, Xiang Wang, Holden Lee, Yi Zhang, Zhiyuan Li, Wei Hu, Rong Ge, and Sanjeev Arora, Explaining landscape connectivity of low-cost solutions for multilayer nets, Advances in Neural Information Processing Systems 32 (2019).

[LBBH98] Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner, Gradient-based learning applied to document recognition, Proceedings of the IEEE 86 (1998), no. 11, 2278-2324.

[LBZ $\left.{ }^{+} 21\right]$ James R Lucas, Juhan Bae, Michael R Zhang, Stanislav Fort, Richard Zemel, and Roger B Grosse, On monotonic linear interpolation of neural network parameters, Proceedings of the 38th International Conference on Machine Learning, vol. 139, PMLR, 18-24 Jul 2021, pp. 7168-7179.

[LK17] Haihao Lu and Kenji Kawaguchi, Depth creates no bad local minima, arXiv preprint arXiv:1702.08580 (2017).

[LSLS18] Shiyu Liang, Ruoyu Sun, Jason D Lee, and Rayadurgam Srikant, Adding one neuron can eliminate all bad local minima, Advances in Neural Information Processing Systems 31 (2018).

[LSZ22] Dachao Lin, Ruoyu Sun, and Zhihua Zhang, On the landscape of one-hidden-layer sparse networks and beyond, Artificial Intelligence (2022), 103739.

[MAB20] Antoine Maillard, Gérard Ben Arous, and Giulio Biroli, Landscape complexity for the empirical risk of generalized linear models, Mathematical and Scientific Machine Learning, PMLR, 2020, pp. 287-327.

[MFG ${ }^{+}$20] Seyed Iman Mirzadeh, Mehrdad Farajtabar, Dilan Gorur, Razvan Pascanu, and Hassan Ghasemzadeh, Linear mode connectivity in multitask and continual learning, International Conference on Learning Representations, 2020.

[MY21] Chao Ma and Lexing Ying, On linear stability of SGD and input-smoothness of neural networks, Advances in Neural Information Processing Systems 34 (2021), 16805-16817.

[NBM21a] Quynh Nguyen, Pierre Bréchet, and Marco Mondelli, On connectivity of solutions in deep learning: The role of over-parameterization and feature quality, Advances in Neural Information Processing Systems 34 (2021).

[NBM21b] Quynh N Nguyen, Pierre Bréchet, and Marco Mondelli, When are solutions connected in deep networks?, Advances in Neural Information Processing Systems 34 (2021), 20956-20969.

[NMH18] Quynh Nguyen, Mahesh Chandra Mukkamala, and Matthias Hein, On the loss landscape of a class of deep neural networks with no bad local valleys, International Conference on Learning Representations, 2018.

[PS21] Henning Petzka and Cristian Sminchisescu, Non-attracting regions of local minima in deep and wide neural networks., Journal of Machine Learning Research 22 (2021), 143-1.

[RABC19] Valentina Ros, Gerard Ben Arous, Giulio Biroli, and Chiara Cammarota, Complex energy landscapes in spiked-tensor and simple glassy models: Ruggedness, arrangements of local minima, and phase transitions, Physical Review X 9 (2019), no. 1, 011003.

[SC16] Daniel Soudry and Yair Carmon, No bad local minima: Data independent training error guarantees for multilayer neural networks, arXiv preprint arXiv:1605.08361 (2016).

[SEG $\left.{ }^{+} 17\right]$ Levent Sagun, Utku Evci, V Ugur Guney, Yann Dauphin, and Leon Bottou, Empirical analysis of the hessian of over-parametrized neural networks, arXiv preprint arXiv:1706.04454 (2017).

[SGJ ${ }^{+}$21] Berfin Simsek, François Ged, Arthur Jacot, Francesco Spadaro, Clément Hongler, Wulfram Gerstner, and Johanni Brea, Geometry of the loss landscape in overparameterized neural networks: Symmetries and invariances, International Conference on Machine Learning, PMLR, 2021, pp. 9722-9732.

[SM20] Alexander Shevchenko and Marco Mondelli, Landscape connectivity and dropout stability of SGD solutions for over-parameterized neural networks, International Conference on Machine Learning, PMLR, 2020, pp. 8773-8784.

[SS18] Itay Safran and Ohad Shamir, Spurious local minima are common in two-layer relu neural networks, International Conference on Machine Learning, PMLR, 2018, pp. 4433-4441.

[SZ14] Karen Simonyan and Andrew Zisserman, Very deep convolutional networks for large-scale image recognition, arXiv preprint arXiv:1409.1556 (2014).

[VF22] Tiffany J Vlaar and Jonathan Frankle, What can linear interpolation of neural network loss landscapes tell us?, International Conference on Machine Learning, PMLR, 2022, pp. 2232522341 .

[WWS] Lei Wu, Mingze Wang, and Weijie J Su, The alignment property of SGD noise and how it helps select flat minima: A stability analysis, Advances in Neural Information Processing Systems.

[WWZG22] Xiang Wang, Annie N Wang, Mo Zhou, and Rong Ge, Plateau in monotonic linear interpolation-a" biased" view of loss landscape for deep networks, arXiv preprint arXiv:2210.01019 (2022).

[WZE17] Lei Wu, Zhanxing Zhu, and Weinan E, Towards understanding generalization of deep learning: Perspective of loss landscapes, arXiv preprint arXiv:1706.10239 (2017).

[YO19] Yuki Yoshida and Masato Okada, Data-dependence of plateau phenomenon in learning with neural network-statistical mechanical analysis, Advances in Neural Information Processing Systems 32 (2019).

[YSJ18] Chulhee Yun, Suvrit Sra, and Ali Jadbabaie, Small nonlinearities in activation functions create bad local minima in neural networks, International Conference on Learning Representations, 2018.

[ZZLX21] Yaoyu Zhang, Zhongwang Zhang, Tao Luo, and Zhiqin J Xu, Embedding principle of loss landscape of deep neural networks, Advances in Neural Information Processing Systems 34 (2021), 14848-14859.

## A Proofs in Section 3

## A. 1 Proof of Theorem 6.

Let

$$
\widetilde{\mathcal{M}}=\left\{W \in \mathbb{R}^{m \times d}: \mathbf{w}_{i} \in S \text { for } i=1, \ldots, m \text { and } \sum_{i=1}^{m} w_{i, j}=1 \text { for } j=1, \ldots, M\right\}
$$

Our task is to prove that $\mathcal{M}=\widetilde{\mathcal{M}}$. For any $W \in \mathcal{M}$, we have $L(W)=\mathbb{E}_{\mathbf{x} \sim \tau_{d-1}}\left[\left(\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i}^{T} \mathbf{x}\right)-\right.\right.$ $\left.\left.\sum_{j=1}^{M} \sigma\left(x_{j}\right)\right)^{2}\right]=0$. By the non-degeneracy of $\tau_{d-1}$, this is equivalent to

$$
\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i}^{T} \mathbf{x}\right)=\sum_{j=1}^{M} \sigma\left(x_{j}\right) \quad \forall \mathbf{x} \in \mathbb{S}^{d-1}
$$

- We first consider the first $M$ columns. Taking $\mathbf{x}=\mathbf{e}_{j}$ in (9) gives for any $j \in[M]$ that

$$
\sum_{i=1}^{m} \sigma\left(w_{i, j}\right)=\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i}^{T} \mathbf{e}_{j}\right)=1
$$

Taking $\mathbf{x}=-\mathbf{e}_{j}$ in (9) gives for any $j \in[M]$ that

$$
\sum_{i=1}^{m} \sigma\left(-w_{i j}\right)=\sum_{i=1}^{m} \sigma\left(-\mathbf{w}_{i}^{T} \mathbf{e}_{j}\right)=0
$$

Combining (10) and (11) leads to

$$
\begin{cases}w_{i j} \geq 0 & \forall i \in[m], j \in[M] \\ \sum_{i=1}^{m} w_{i j}=1 & \forall j \in[M]\end{cases}
$$

- Next we turn to consider the columns from $M+1$ to $d$. Analogously, for any $j \in M+1, \ldots, d$, we take $\mathbf{x}=\mathbf{e}_{j}$ and $\mathbf{x}=-\mathbf{e}_{j}$ in (9), yielding

$$
\left\{\begin{array}{l}
\sum_{i=1}^{m} \sigma\left(w_{i j}\right)=0 \\
\sum_{i=1}^{m} \sigma\left(-w_{i j}\right)=0
\end{array}\right.
$$

This implies

$$
w_{i j}=0, \quad \forall i \in\{1, \ldots, m\}, j \in\{M+1, \ldots, d\}
$$

- Now we prove by contradiction that for each $j \in[m]$, there exists at most one coordinate to be nonzero. Suppose that there exists $i \in[m]$ such that $\left\|w_{i}\right\|_{0} \geq 2$. W.L.O.G, let $i=1$ and $w_{11}>0, w_{12}>0$. Then, there must exist $\epsilon>0$ such that $\sqrt{1-\epsilon^{2}} w_{11}-\epsilon w_{12}>0$.

Let $\mathbf{x}=\sqrt{1-\epsilon^{2}} \mathbf{e}_{1}-\epsilon \mathbf{e}_{2}$ in (9). First, we have $\sum_{i=1}^{M} \sigma\left(x_{i}\right)=\sqrt{1-\epsilon^{2}}$. Second,

$$
\begin{aligned}
\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i} \cdot \mathbf{x}\right) & =\sum_{i=1}^{m} \sigma\left(\sqrt{1-\epsilon^{2}} w_{i 1}-\epsilon w_{i 2}\right)=\sigma\left(\sqrt{1-\epsilon^{2}} w_{11}-\epsilon w_{12}\right)+\sum_{i=2}^{m} \sigma\left(\sqrt{1-\epsilon^{2}} w_{i 1}-\epsilon w_{i 2}\right) \\
& \leq \sigma\left(\sqrt{1-\epsilon^{2}} w_{11}-\epsilon w_{12}\right)+\sum_{i=2}^{m} \sigma\left(\sqrt{1-\epsilon^{2}} w_{i 1}\right)=\sqrt{1-\epsilon^{2}} w_{11}-\epsilon w_{12}+\sum_{i=2}^{m} \sqrt{1-\epsilon^{2}} w_{i 1} \\
& =\sqrt{1-\epsilon^{2}} \sum_{i=1}^{m} w_{i 1}-\epsilon w_{i 2}<\sqrt{1-\epsilon^{2}} \sum_{i=1}^{m} w_{i 1}=\sqrt{1-\epsilon^{2}}
\end{aligned}
$$

Thus, $\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i} \cdot \mathbf{x}\right)<\sum_{i=1}^{M} \sigma\left(x_{i}\right)$, which is contradictory with (9).

Combining the three conclusions above, we proved $\mathcal{M} \subset \widetilde{\mathcal{M}}$. What remains is to prove $\widetilde{\mathcal{M}} \subset \mathcal{M}$. It is obvious that for any $W \in \widetilde{\mathcal{M}}$, we have $\sum_{i=1}^{m} \sigma\left(\mathbf{w}_{i} \cdot \mathbf{x}\right)=\sum_{i=1}^{m} \sigma\left(\sum_{j=1}^{d} w_{i j} x_{j}\right)=\sum_{i=1}^{m} \sum_{j=1}^{d} w_{i j} \sigma\left(x_{j}\right)=\sum_{i=1}^{M} \sigma\left(x_{i}\right)$. Thus $W$ is a global minimum, implying $\tilde{\mathcal{M}} \subset \mathcal{M}$.

Proof of Lemma 7. Recall that Theorem 6 shows

$$
\mathcal{M}=\left\{W \in \mathbb{R}^{m \times d}: \mathbf{w}_{i} \in S \text { for } i=1, \ldots, m \text { and } \sum_{i=1}^{m} w_{i, j}=1 \text { for } j=1, \ldots, M\right\}
$$

where $S=\cup_{j=0}^{M} S_{j}$ with $S_{0}=\left\{(0, \ldots, 0) \in \mathbb{R}^{d}\right\}$ and $S_{j}=\left\{\alpha \mathbf{e}_{j} \in \mathbb{R}^{d}: \alpha \neq 0\right\}$ for $j=1, \ldots, M$.

Given any $\theta_{1}, \theta_{2} \in \mathcal{M}$, our task is to prove that $\theta_{1} \leftrightarrow \theta_{2}$ is equivalent to that one of the following two conditions is satisfied:
a) $\mathbf{w}_{i}^{(1)} \in S_{0}$ or $\mathbf{w}_{i}^{(2)} \in S_{0}$;

b) there exists $j \in\{1, \ldots, M\}$ such that $\mathbf{w}_{i}^{(1)} \in S_{j}$ and $\mathbf{w}_{i}^{(2)} \in S_{j}$.

We first prove that $\theta_{1} \leftrightarrow \theta_{2}$ can lead to the condition a) or b). Note that $\theta_{1} \leftrightarrow \theta_{2}$ means

$$
\gamma(t)=\left((1-t) \mathbf{w}_{1}^{(1)}+t \mathbf{w}_{1}^{(2)}, \cdots,(1-t) \mathbf{w}_{m}^{(1)}+t \mathbf{w}_{m}^{(2)}\right)^{T} \in \mathcal{M}
$$

By (15), $(1-t) \mathbf{w}_{i}^{(1)}+t \mathbf{w}_{i}^{(2)} \in S$ holds for any $i \in[m]$ and $t \in[0,1]$. Since any element in $S$ has at most one nonzero coordinate, $\mathbf{w}_{i}^{(1)}$ and $\mathbf{w}_{i}^{(2)}$ have at most one nonzero coordinate and their nonzero coordinates must be the same. Otherwise, the number of nonzero coordinates of $(1-t) \mathbf{w}_{i}^{(1)}+t \mathbf{w}_{i}^{(2)}$ will be no less than 2 for any $t \in(0,1)$. This implies that either condition a) or condition b) is satisfied.

Second, if condition a) or condition b) is satisfied, then for any $t \in[0,1]$ and any $i \in[m],(1-t) \mathbf{w}_{i}^{(1)}+$ $t \mathbf{w}_{i}^{(2)} \in S$. Moreover, for any $j \in[M]$,

$$
\sum_{i=1}^{m}\left((1-t) w_{i, j}^{(1)}+t w_{i, j}^{(2)}\right)=(1-t) \sum_{i=1}^{m} w_{i, j}^{(1)}+t \sum_{i=1}^{m} w_{i, j}^{(2)}=(1-t)+t=1
$$

Hence, by (15), $(1-t) \theta_{1}+t \theta_{2} \in \mathcal{M}$ for any $t \in[0,1]$.

## A. 2 Proof of Theorem 8.

Let $\theta_{i} \stackrel{i i d}{\sim} \operatorname{Unif}(\mathcal{M})$ for $i=1,2$. We aim to give a lower bound for the probability that there exists a global minimum $\theta^{*}$ such that $\theta^{1} \leftrightarrow \theta^{*}$ and $\theta^{*} \leftrightarrow \theta^{2}$. From Theorem 6 , given a $\theta=\left(\mathbf{w}_{1}, \ldots, \mathbf{w}_{m}\right)^{T} \in \mathbb{R}^{m \times d}$, the sufficient and necessary condition for $\theta$ to be a global minimum is:

(1) $\mathbf{w}_{i} \in S$, for any $i \in[m]$.

(2) $\sum_{j: \mathbf{w}_{j} \in S_{i}} \mathbf{w}_{j}=e_{i}$, for $i \in\{1, \ldots, M\}$.

We notice that $\theta^{1}\left(\theta^{2}\right)$ has the requirement that for every $i \in\{1, \ldots, M\}$, there exists $j \in\{1, \ldots, m\}$ such that $\theta_{j}^{1}\left(\theta_{j}^{2}\right) \in S_{i}$, after we already have $M$ different elements of $\theta^{1}\left(\theta^{2}\right)$, the rest elements have no restriction and can be arbitrarily chosen in at least $m-2 M$ overlapped positions.

Hence, we suppose $\mathbf{w}_{j}^{1}$ and $\mathbf{w}_{j}^{2}$ have uniform distribution over $S$ for any $j \in T$, where $T$ is a subset of $\{1, \ldots, m\}$ containing $m-2 M$ elements. i.e. $\mathbf{w}_{j}^{1}\left(\mathbf{w}_{j}^{2}\right)(j \in T)$ chooses randomly a set from $\left\{S_{0}, \ldots, S_{M}\right\}$ to belong to.

For $j \in T$, we consider the pair $\left(\mathbf{w}_{j}^{1}, \mathbf{w}_{j}^{2}\right)$. We denote $\left[\mathbf{w}_{j}^{1}, \mathbf{w}_{j}^{2}\right] \triangleq[p, q]$ if $\mathbf{w}_{j}^{1} \in S_{p}$ and $\mathbf{w}_{j}^{2} \in S_{q}$.

Then we define the incident $A_{i}$ : for any $j \in T,\left[\mathbf{w}_{j}^{1}, \mathbf{w}_{j}^{2}\right] \neq[i, i]$. Since $\theta_{i} \stackrel{i i d}{\sim} \operatorname{Unif}(\mathcal{M})$ for $i=1,2$, we have $P\left(A_{i}\right)=\left(\frac{M^{2}-1}{M^{2}}\right)^{m-2 M}$.

Thus, from the inclusion-exclusion principle, we have:

$$
\begin{aligned}
& P\left(\theta_{1} \text { and } \theta_{2} \text { are } 2-\mathrm{PL} \text { connected }\right) \\
\geq & 1-\sum_{i=1}^{M} P\left(A_{i}\right) \\
= & 1-M P\left(A_{1}\right) \\
= & 1-M\left(\frac{M^{2}-1}{M^{2}}\right)^{m-2 M}
\end{aligned}
$$

## A. 3 Proof of Theorem 9.

First, we consider the choice of $\theta^{3}\left(\theta^{5}\right)$. Since $\theta^{1}\left(\theta^{2}\right)$ has property that for every $i \in\{1, \ldots, M\}$, there exists $j_{i} \in\{1, \ldots, m\}$ such that $\mathbf{w}_{j_{i}}^{1} \in S_{i}$. Then, we let $\mathbf{w}_{j_{i}}^{3}=\boldsymbol{e}_{i}$ for $i \in\{1, \ldots, M\}$, and set the other line vector of $\theta^{3}$ as zero. From Theorem $6, \theta^{3}$ is a global minimum of Equation (3). Further, from Lemma 7, we have $\theta^{1} \leftrightarrow \theta^{3}$. We call this method generating $\theta^{3}$ from $\theta^{1}$ "merging", since it straightforwardly merges some line vectors of $\theta^{1}$ belonging to the same set in $S$ to a single non-zero vector. Similarly, we can merge $\theta^{2}$ to $\theta^{5}$.

$\theta^{3}$ and $\theta^{5}$ share the common characteristic that they contain exactly $M$ different non-zero line vectors $\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$, and $m-M$ zero line vectors. Since $m \geq 2 M-1$, we have $m-M \geq M-1$, thus $\theta^{3}$ has at least $M-1$ zero line vectors.

Case 1.

If there are at least $M$ zero line vectors, suppose the set of the zero line vectors is $\left\{\mathbf{w}_{a_{1}}^{3}, \ldots, \mathbf{w}_{a_{M}}^{3}\right\}$, then since $\mathbf{w}_{a_{1}}^{5}, \ldots, \mathbf{w}_{a_{M}}^{5}$ belong to different subsets of $S$ or belong to $S_{0}$, We can find a feasible set of $\left\{\mathbf{w}_{a_{1}}^{4}, \ldots, \mathbf{w}_{a_{M}}^{4}\right\}=\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$, we set other line vectors of $\theta^{4}$ as zero and then we are done since we have a feasible global minimum $\theta^{4}$.

Case 2.

If there are only $M-1$ zero line vectors for $\theta^{3}$. Now, we fix a feasible $\theta^{3}$ merged from $\theta^{1}$, suppose the set of its zero line vectors is $\left\{\mathbf{w}_{a_{1}}^{3}, \ldots, \mathbf{w}_{a_{M-1}}^{3}\right\}$. First, we look at the corresponding line vectors of these $\theta^{3}$ 's zero vectors in $\theta^{5}$, i.e. $\left\{\mathbf{w}_{a_{1}}^{5}, \ldots, \mathbf{w}_{a_{M-1}}^{5}\right\}$. We notice that $\theta^{5}$ is not fixed when generated from $\theta^{2}$, and trivially we have at least $M$ different positions to choose from for the $M-1$ zero line vectors. Hence, there exists a choice of $\theta^{5}$ where at least one element of $\left\{\mathbf{w}_{a_{1}}^{5}, \ldots, \mathbf{w}_{a_{M-1}}^{5}\right\}$ is non-zero. Thus, there is at least one zero vector of $\theta^{5}$ with a non-zero corresponding line vector in $\theta^{3}$, the set of which we denote as $\left\{\mathbf{w}_{b_{1}}^{3}, \ldots, \mathbf{w}_{b_{f}}^{3}\right\}$.

Case 2-1.

If there exists $\mathbf{w}_{b_{i}}^{3}$ belongs to different subset of $S$ from any element of $\left\{\mathbf{w}_{a_{1}}^{5}, \ldots, \mathbf{w}_{a_{M-1}}^{5}\right\}$, then we can find a feasible set of $\left\{\mathbf{w}_{b_{i}}^{4}, \mathbf{w}_{a_{1}}^{4}, \ldots, \mathbf{w}_{a_{M-1}}^{4}\right\}=\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$. We set other line vectors of $\theta^{4}$ as zero and then we are done since we have a feasible global minimum $\theta^{4}$.

Case 2-2.

If every element of $\mathbf{w}_{b_{1}}^{3}, \ldots, \mathbf{w}_{b_{f}}^{3}$ belongs to the same subset of $S$ as an element of $\left\{\mathbf{w}_{a_{1}}^{5}, \ldots, \mathbf{w}_{a_{M-1}}^{5}\right\}$, we arbitrarily choose a line vector from $\mathbf{w}_{b_{1}}^{3}, \ldots, \mathbf{w}_{b_{f}}^{3}$. Suppose $\mathbf{w}_{b_{j}}^{3} \in S_{t}$ and $\mathbf{w}_{a_{q}}^{5} \in S_{t}$. Then we suppose $\mathbf{w}_{b_{j}}^{2} \in S_{p}$, and $\mathbf{w}_{b_{g}}^{5} \in S_{p}$.

Case 2-2-1.

If $p=0$, then we let $\mathbf{w}_{b_{j}}^{5}=e_{t}$, and let $\mathbf{w}_{a_{q}}^{5}=0$. Then we can find a feasible set of $\left\{\mathbf{w}_{b_{j}}^{4}, \mathbf{w}_{a_{1}}^{4}, \ldots, \mathbf{w}_{a_{M-1}}^{4}\right\}=$ $\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$. We set other line vectors of $\theta^{4}$ as zero and then we are done since we have a feasible global minimum $\theta^{4}$.

Case 2-2-2.

If $p \neq 0$, then we can switch $\mathbf{w}_{b_{j}}^{5}$ and $\mathbf{w}_{b_{g}}^{5}$ without damaging the connectivity of the global minima. Now, the number of the non-zero corresponding line vectors in $\theta^{3}$ reduces to $f-1$. After at most $f-1$ same operations, if we still didn't find the feasible global minimum $W_{4}$, then we get exactly one non-zero corresponding line vector in $\theta^{3}$ and exactly one non-zero element in $\left\{\mathbf{w}_{a_{1}}^{5}, \ldots, \mathbf{w}_{a_{M-1}}^{5}\right\}$, and these two
vectors belong to the same subset of $S$. Suppose $\mathbf{w}_{b_{j^{\prime}}}^{3} \in S_{t^{\prime}}$ and $\mathbf{w}_{q_{q^{\prime}}}^{5} \in S_{t^{\prime}}\left(t^{\prime} \neq 0\right)$. Then we suppose $\mathbf{w}_{b_{j^{\prime}}}^{2} \in S_{p^{\prime}}$, and $\mathbf{w}_{b_{g^{\prime}}}^{5} \in S_{p^{\prime}}$.

Case 2-2-2-1.

If $p^{\prime}=0$, then we let $\mathbf{w}_{b_{j^{\prime}}}^{5}=e_{t^{\prime}}$, and let $\mathbf{w}_{a_{q^{\prime}}}^{5}=0$. Then we can find a feasible set of $\left\{\mathbf{w}_{b_{j^{\prime}}}^{4}, \mathbf{w}_{a_{1}}^{4}, \ldots, \mathbf{w}_{a_{M-1}}^{4}\right\}=$ $\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$. We set other line vectors of $\theta^{4}$ as zero and then we are done since we have a feasible global minimum $\theta^{4}$.

Case 2-2-2-2.

If $p^{\prime} \neq 0$, then we can switch $\mathbf{w}_{b_{j^{\prime}}}^{5}$, and $\mathbf{w}_{b_{g^{\prime}}}^{5}$ without damaging the connectivity of the global minima. Since $p^{\prime} \neq t^{\prime}$, then we can find a feasible set of $\left\{\mathbf{w}_{b_{g^{\prime}}}^{4}, \mathbf{w}_{a_{1}}^{4}, \ldots, \mathbf{w}_{a_{M-1}}^{4}\right\}=\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$. We set other line vectors of $\theta^{4}$ as zero and then we are done since we have a feasible global minimum $\theta^{4}$.

Finally, we complete the proof.

## A. 4 Proof of Theorem 10

We follow the proof of Theorem 8 and apply some modifications.

Here, for $j \in T$, we consider the combination $\left(\mathbf{w}_{j}^{1}, \ldots, \mathbf{w}_{j}^{k}\right)$. We denote $\left[\mathbf{w}_{j}^{1}, \ldots \mathbf{w}_{j}^{k}\right] \stackrel{\Delta}{\Delta}\left[p_{1}, \ldots, p_{k}\right]$ if $\mathbf{w}_{j}^{i} \in S_{p_{i}}$ for $i \in\{1, \ldots, k\}$.

Similarly, we define the incident $A_{i}$ : for any $j \in T,\left[\mathbf{w}_{j}^{1}, \mathbf{w}_{j}^{2}, \ldots, \mathbf{w}_{j}^{k}\right] \neq[i, i, \ldots, i]$.

Thus. following the proof of Theorem 8, based on our assumption for uniform distribution, we can calculate that $P\left(A_{i}\right)=\left(\frac{M^{k}-1}{M^{k}}\right)^{m-k M}$.

Hence, $1-\sum_{i=1}^{M} P\left(A_{i}\right)=1-M\left(\frac{M^{k}-1}{M^{k}}\right)^{m-k M}$, which is the lower bound in the theorem.

## A. 5 Proof of Theorem 11.

We follow the proof of Theorem 9. Firstly, we merge $\theta^{i}$ to be $\theta^{i_{0}}$ just as what we did in the proof of Theorem 9. Considering $\theta^{i_{0}}$ for any $i \in\{1, \ldots, k\}$, since $m \geq k M$, it has at least $(k-1) M$ zero line vectors.

Hence, it trivially holds that $\theta^{1_{0}}$ and $\theta^{2_{0}}$ share at least $(k-2) M$ zero line vectors of relatively same position, $\theta^{1_{0}}, \theta^{2_{0}}$ and $\theta^{3_{0}}$ share at least $(k-3) M$ zero line vectors of relatively same position... We can easily use mathematical induction to deduce that $\theta^{1_{0}}, \ldots, \theta^{k-1_{0}}$ share at least $M$ zero line vectors of relatively same position. Suppose the positions of the $M$ common line vectors are $\left\{a_{1}, \ldots, a_{M}\right\}$. Since $\mathbf{w}_{a_{1}}^{k}, \ldots, \mathbf{w}_{a_{M}}^{k}$ belong to different subsets of $S$ or belong to $S_{0}$, we can find a feasible set of $\left\{\mathbf{w}_{a_{1}}^{k+1}, \ldots, \mathbf{w}_{a_{M}}^{k+1}\right\}=\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{M}\right\}$. We set other line vectors of $\theta^{k+1}$ as zero and then we are done since we have a feasible global minimum $\theta^{k+1}$.

Here we finish proving Theorem 11.

## A. 6 Proof of Theorem 12

Lemma 19. For any two global minima $\theta_{1}=\left(\boldsymbol{u}_{1}^{1}, \ldots, \boldsymbol{u}_{d}^{1}\right), \theta_{2}=\left(\boldsymbol{u}_{1}^{2}, \ldots, \boldsymbol{u}_{d}^{2}\right)$, for $i \in\{1, \ldots, M\}$, suppose $\theta_{1}$ and $\theta_{2}$ respectively have $m_{1}$ and $m_{2}$ neurons that belong to $S_{i}$, with $m_{t}\left(m_{t} \leq \min \left\{m_{1}, m_{2}\right\}\right)$ neurons sharing common coordinates, then for any global minimum $\theta=\left(\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{d}\right)$, we have

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \leq \frac{1}{1-\sqrt{\frac{\left(m_{1}-m_{t}\right)\left(m_{2}-m_{t}\right)}{m_{1} m_{2}}}}
$$

Proof of Lemma 19. Suppose $\theta_{1}=\left(\mathbf{w}_{1}^{1}, \ldots, \mathbf{w}_{m}^{1}\right)^{T}=\left(\boldsymbol{u}_{1}^{1}, \ldots, \boldsymbol{u}_{d}^{1}\right), \theta_{2}=\left(\mathbf{w}_{1}^{2}, \ldots, \mathbf{w}_{m}^{2}\right)^{T}=\left(\boldsymbol{u}_{1}^{2}, \ldots, \boldsymbol{u}_{d}^{2}\right) \in$ $\mathbb{R}^{m \times d}$. Suppose $\theta=\left(\mathbf{w}_{1}, \ldots, \mathbf{w}_{m}\right)^{T}=\left(\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{d}\right)$.

Suppose $a_{1}, \ldots, a_{m_{t}}, b_{1}, \ldots, b_{m_{t}}$ are the $i^{t h}$ components of $\mathbf{w}^{1}$ where $\mathbf{w}^{1}$ shares common coordinates with $\mathbf{w}^{2} . a_{m_{t}+1}, \ldots, a_{m_{1}}, b_{m_{t}+1}, \ldots, b_{m_{2}}$ are the rest components. We have $\sum_{j=1}^{m_{t}} a_{j} \leq 1$ and $\sum_{j=1}^{m_{t}} b_{j} \leq 1$.

Suppose $x_{1}, \ldots, x_{m_{t}}$ are the $i^{\text {th }}$ components of $\mathbf{w}$ that share common coordinates with $\mathbf{w}^{1}$ and $\mathbf{w}^{2}$. From Theorem 6 , we have $\sum_{j=1}^{m_{t}} x_{j}=1$. Thus,

$$
\begin{aligned}
& \left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2} \\
= & \sum_{i=1}^{m_{t}}\left[\left(x_{i}-a_{i}\right)^{2}+\left(x_{i}-b_{i}\right)^{2}\right]+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2} \\
= & 2 \sum_{i=1}^{m_{t}}\left[x_{i}^{2}-\left(a_{i}+b_{i}\right) x_{i}+\frac{a_{i}^{2}+b_{i}^{2}}{2}\right]+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2} \\
= & 2 \sum_{i=1}^{m_{t}}\left[\left(x_{i}-\frac{a_{i}+b_{i}}{2}\right)^{2}+\frac{\left(a_{i}-b_{i}\right)^{2}}{4}\right]+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2} \\
\geq & 2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}
\end{aligned}
$$

Thus, we have

$$
\begin{aligned}
& \min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \\
= & \frac{2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}} \triangleq M
\end{aligned}
$$

Further, we have

$$
M \leq \frac{2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\frac{\left(1-\sum_{i=1}^{m_{t}} a_{i}\right)^{2}}{m_{1}-m_{t}}+\frac{\left(1-\sum_{i=1}^{m_{t}} b_{i}\right)^{2}}{m_{2}-m_{t}}}{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}+\frac{\left(1-\sum_{i=1}^{m_{t}} a_{i}\right)^{2}}{m_{1}-m_{t}}+\frac{\left(1-\sum_{i=1}^{m_{t}} b_{i}\right)^{2}}{m_{2}-m_{t}}}
$$

Denote $S_{a} \triangleq \sum_{i=1}^{m_{t}} a_{i}, S_{b} \triangleq \sum_{i=1}^{m_{t}} b_{i}$, then we have

$$
\begin{aligned}
M & \leq \frac{2 \frac{\left(1-\frac{S_{a}+S_{b}}{2}\right)^{2}}{m}+\frac{\left(S_{a}-S_{b}\right)^{2}}{2 m_{t}}+\frac{\left(1-S_{a}\right)^{2}}{m_{1}-m_{t}}+\frac{\left(1-S_{b}\right)^{2}}{m_{2}-m_{t}}}{\frac{\left(S_{a}-S_{b}\right)^{2}}{m_{t}}+\frac{\left(1-S_{a}\right)^{2}}{m_{1}-m_{t}}+\frac{\left(1-S_{b}\right)^{2}}{m_{2}-m_{t}}} \\
& =\frac{\frac{m_{1}}{m_{t}\left(m_{1}-m_{t}\right)}\left(1-S_{a}\right)^{2}+\frac{m_{2}}{m_{t}\left(m_{2}-m_{t}\right)}\left(1-S_{b}\right)^{2}}{\frac{\left(S_{a}-S_{b}\right)^{2}}{m_{t}}+\frac{\left(1-S_{a}\right)^{2}}{m_{1}-m_{t}}+\frac{\left(1-S_{b}\right)^{2}}{m_{2}-m_{t}}} \\
& \leq \frac{\sqrt{m_{1}\left(m_{2}-m_{t}\right) m_{2}\left(m_{1}-m_{t}\right)}}{\sqrt{m_{1}\left(m_{2}-m_{t}\right) m_{2}\left(m_{1}-m_{t}\right)}-\left(m_{1}-m_{t}\right)\left(m_{2}-m_{t}\right)} \\
& =\frac{1}{1-\sqrt{\frac{\left(m_{1}-m_{t}\right)\left(m_{2}-m_{t}\right)}{m_{1} m_{2}}}}
\end{aligned}
$$

Now we completed the proof.

Lemma 20 (Hoeffding's inequality). Let $X_{1}, \ldots, X_{n}$ be independent random variables. Assume that $X_{i} \in\left[m_{i}, M_{i}\right]$ for every $i$. Then, for any $t>0$, we have

$$
\mathbb{P}\left\{\sum_{i=1}^{n}\left(X_{i}-\mathbb{E} X_{i}\right) \geq t\right\} \leq e^{-\frac{2 t^{2}}{\sum_{i=1}^{n}\left(M_{i}-m_{i}\right)^{2}}}
$$

We suppose $m_{1} \geq m_{2}$, then we have $\frac{m_{t}}{m_{1}}=\frac{\sum_{j=1}^{m_{1}} 1\left\{\mathbf{w}_{j}^{2} \in S_{i}\right\}}{m_{1}}$. Then, from Hoeffding's inequality (Lemma 20), we have for any $\epsilon>0$, with probability $1-e^{-2 m_{1} \epsilon^{2}}$,

$$
\frac{\sum_{j=1}^{m_{1}} \mathbb{1}\left\{\mathbf{w}_{j}^{2} \in S_{i}\right\}}{m_{1}}-\frac{1}{m+1} \geq-\epsilon
$$

Then we have

$$
\frac{1}{1-\sqrt{\frac{\left(m_{1}-m_{t}\right)\left(m_{2}-m_{t}\right)}{m_{1} m_{2}}}} \leq \frac{1}{1-\frac{m_{1}-m_{t}}{m_{1}}}=\frac{1}{\frac{m_{t}}{m_{1}}} \leq \frac{1}{\frac{1}{M+1}-\epsilon}
$$

Now, we suppose $\theta_{1}$ and $\theta_{2}$ respectively have $m_{1 i}$ and $m_{2 i}$ neurons that belong to $S_{i}$, and from Lemma 19 we have with probability $1-\sum_{i=1}^{M} e^{-2 \max \left\{m_{1 i}, m_{2 i}\right\} \epsilon^{2}}$,

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \leq \frac{1}{\frac{1}{M+1}-\epsilon}
$$

for all $i \in\{1, \ldots, M\}$. Hence,

$$
\min _{\theta} \frac{\left\|\theta-\theta_{1}\right\|_{2}^{2}+\left\|\theta-\theta_{2}\right\|_{2}^{2}}{\left\|\theta_{1}-\theta_{2}\right\|_{2}^{2}} \leq \frac{1}{\frac{1}{M+1}-\epsilon}
$$

Furthermore, for any $\delta>0$, from Hoeffding's inequality, we have with probability $1-e^{-2 m \delta^{2}}$,

$$
\frac{m_{1 i}}{m}-\frac{1}{M+1} \geq-\delta
$$

Hence, with probability $1-M e^{-2 m \delta^{2}}$,

$$
\frac{\max \left\{m_{1 i}, m_{2 i}\right\}}{m}-\frac{1}{M+1} \geq-\delta
$$

for all $i \in\{1, \ldots, M\}$. Therefore, with probability $1-M e^{-2 m \delta^{2}}-M e^{-2\left(\frac{m}{M+1}-m \delta\right) \epsilon^{2}}$,

$$
\min _{\theta} \frac{\left\|\theta-\theta_{1}\right\|_{2}^{2}+\left\|\theta-\theta_{2}\right\|_{2}^{2}}{\left\|\theta_{1}-\theta_{2}\right\|_{2}^{2}} \leq \frac{1}{\frac{1}{M+1}-\epsilon}
$$

We let $\delta=\epsilon$, and we obtain with probability $1-M e^{-2 m \epsilon^{2}}-M e^{-2\left(\frac{m}{M+1}-m \epsilon\right) \epsilon^{2}}$,

$$
\min _{\theta} \frac{\left\|\theta-\theta_{1}\right\|_{2}^{2}+\left\|\theta-\theta_{2}\right\|_{2}^{2}}{\left\|\theta_{1}-\theta_{2}\right\|_{2}^{2}} \leq \frac{1}{\frac{1}{M+1}-\epsilon}
$$

From Cauchy's inequality, we completed the proof.

## A. 7 Proof of Theorem 14

Lemma 21. Suppose $a_{1}, \ldots, a_{m_{t}}, b_{1}, \ldots, b_{m_{t}}$ are the $i^{\text {th }}$ components of $\mathbf{w}^{1}$ and $\mathbf{w}^{2}$ where $\mathbf{w}^{1}$ shares common coordinates with $\mathbf{w}^{2}$ or where the neuron of $\mathbf{w}^{1}$ or $\mathbf{w}^{2}$ belongs to $S_{0} . a_{m_{t}+1}, \ldots, a_{m_{1}}, b_{m_{t}+1}, \ldots, b_{m_{2}}$ are the rest components. Then we have

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}=\frac{2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m_{t}}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}
$$

Proof of Lemma 21. We have $\sum_{j=1}^{m_{t}} a_{j} \leq 1$ and $\sum_{j=1}^{m_{t}} b_{j} \leq 1$. Suppose $x_{1}, \ldots, x_{m_{t}}$ are the $i^{\text {th }}$ components of $\mathbf{w}$ that share common coordinates with $\mathbf{w}^{1}$ and $\mathbf{w}^{2}$. From Theorem 6 , we have $\sum_{j=1}^{m_{t}} x_{j}=1$. Thus,

$$
\begin{aligned}
& \left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2} \\
= & \sum_{i=1}^{m_{t}}\left[\left(x_{i}-a_{i}\right)^{2}+\left(x_{i}-b_{i}\right)^{2}\right]+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2} \\
= & 2 \sum_{i=1}^{m_{t}}\left[x_{i}^{2}-\left(a_{i}+b_{i}\right) x_{i}+\frac{a_{i}^{2}+b_{i}^{2}}{2}\right]+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2} \\
= & 2 \sum_{i=1}^{m_{t}}\left[\left(x_{i}-\frac{a_{i}+b_{i}}{2}\right)^{2}+\frac{\left(a_{i}-b_{i}\right)^{2}}{4}\right]+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2} \\
\geq & \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m_{t}}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}
\end{aligned}
$$

Thus, we have

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}=\frac{2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m_{t}}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}
$$

Lemma 22. With probability $1-5 e^{-2 m_{t} \epsilon^{2}}$,

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \leq A
$$

Here,

$$
A=\frac{\frac{2\left(\frac{1}{m_{t}}-\frac{1}{2 m_{1}}+\frac{1}{2 m_{2}}+\epsilon\right)^{2}}{m_{t}}+\frac{c-\epsilon}{2}+\left(\frac{1}{m_{t}}-\frac{1}{m_{1}}+\epsilon\right)^{2}+\left(\frac{1}{m_{t}}-\frac{1}{m_{2}}+\epsilon\right)^{2}}{c-\epsilon+\left(\frac{1}{m_{t}}-\frac{1}{m_{1}}+\epsilon\right)^{2}+\left(\frac{1}{m_{t}}-\frac{1}{m_{2}}+\epsilon\right)^{2}}
$$

Proof of Lemma 22. From Lemma 21, we have

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \leq \frac{2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m_{t}}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\left(1-\sum_{i=1}^{m_{t}} a_{i}\right)^{2}+\left(1-\sum_{i=1}^{m_{t}} b_{i}\right)^{2}}{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}+\left(1-\sum_{i=1}^{m_{t}} a_{i}\right)^{2}+\left(1-\sum_{i=1}^{m_{t}} b_{i}\right)^{2}}
$$

Since $\theta_{1}$ and $\theta_{2}$ are independently drawn from $S P(\mathcal{M}, r),\left(a_{i}-b_{i}\right)^{2}$ has a positive expectation $c>0$. Then, from Hoeffding's inequality (Lemma 20), for any $\epsilon>0$, we have with probability $1-e^{-2 m_{t} \epsilon^{2}}$,

$$
\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}-c m_{t} \geq-m_{t} \epsilon
$$

Similarly, we have with probability $1-2 e^{-2 m \epsilon^{2}}{ }^{2}$,

$$
\left|\sum_{i=1}^{m_{t}} a_{i}-\frac{m_{t}}{m_{1}}\right| \leq m_{t} \epsilon
$$

and with probability $1-2 e^{-2 m_{t} \epsilon^{2}}$,

$$
\left|\sum_{i=1}^{m_{t}} b_{i}-\frac{m_{t}}{m_{2}}\right| \leq m_{t} \epsilon
$$

Hence, we have with probability $1-5 e^{-2 m_{t} \epsilon^{2}}$,

$$
\begin{aligned}
& \min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \\
= & \frac{2 \frac{\left(1-\sum_{i=1}^{m_{t}}\left(a_{i}+b_{i}\right) / 2\right)^{2}}{m_{t}}+\frac{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}}{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}{\sum_{i=1}^{m_{t}}\left(a_{i}-b_{i}\right)^{2}+\sum_{i=m_{t}+1}^{m_{1}} a_{i}^{2}+\sum_{i=m_{t}+1}^{m_{2}} b_{i}^{2}}
\end{aligned}
$$

$$
\leq A
$$

Now, go back to the original problem, we have

$$
\frac{m_{t}}{m_{1}} \geq \frac{\sum_{j=1}^{m_{1}} \mathbb{1}\left\{\mathbf{w}_{j}^{2} \in S_{i}\right\}+\sum_{j=1}^{m_{1}} \mathbb{1}\left\{\mathbf{w}_{j}^{2} \in S_{0}\right\}}{m_{1}}
$$

Then, from Hoeffding's inequality (Lemma 20), we have for any $\epsilon>0$, with probability $1-2 e^{-2 m_{1} \epsilon^{2}}$,

$$
\left|\frac{\sum_{j=1}^{m_{1}} \mathbb{1}\left\{\mathbf{w}_{j}^{2} \in S_{i}\right\}+\sum_{j=1}^{m_{1}} \mathbb{1}\left\{\mathbf{w}_{j}^{2} \in S_{0}\right\}}{m_{1}}-\frac{1+(M-1) r}{M}\right| \leq \epsilon
$$

Similarly we have with probability $1-2 e^{-2 m_{2} \epsilon^{2}}$,

$$
\left|\frac{\sum_{j=1}^{m_{2}} \mathbb{1}\left\{\mathbf{w}_{j}^{1} \in S_{i}\right\}+\sum_{j=1}^{m_{2}} \mathbb{1}\left\{\mathbf{w}_{j}^{1} \in S_{0}\right\}}{m_{2}}-\frac{1+(M-1) r}{M}\right| \leq \epsilon
$$

Also, with probability $1-e^{-2 m \epsilon^{2}}$,

$$
\frac{m_{1}}{m}-\frac{1+(M-1) r}{M} \geq-\epsilon
$$

and with probability $1-e^{-2 m \epsilon^{2}}$,

$$
\frac{m_{2}}{m}-\frac{1+(M-1) r}{M} \geq-\epsilon
$$

We denote $\left(\frac{\frac{(M-1)(1-r)}{M}+\epsilon}{\left(\frac{1+(M-1) r}{M}-\epsilon\right)^{2} m}+\epsilon\right)^{2}=q$, then in this case, we have

$$
A \leq \frac{1}{2}+\frac{\frac{2 q}{\left(\frac{1+(M-1) r}{M}-\epsilon\right)^{2} m}+q}{c-\epsilon+2 q}
$$

Now, we suppose $\theta^{1}$ and $\theta^{2}$ respectively have $m_{1 i}$ and $m_{2 i}$ neurons that belong to $S_{i}$, and we have with probability $1-\sum_{i=1}^{M} 11 e^{-2\left(\frac{1+(M-1) r}{M}-\epsilon\right)^{2} m \epsilon^{2}}$,

$$
\min _{\theta} \frac{\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{1}\right\|_{2}^{2}+\left\|\boldsymbol{v}_{i}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}}{\left\|\boldsymbol{u}_{i}^{1}-\boldsymbol{u}_{i}^{2}\right\|_{2}^{2}} \leq \frac{1}{2}+\frac{\frac{2 q}{\left(\frac{1+(M-1) r}{M}-\epsilon\right)^{2} m}+q}{c-\epsilon+2 q}
$$

for all $i \in\{1, \ldots, M\}$.

Hence, with probability $1-11 M e^{-2\left(\frac{1+(M-1) r}{M}-\epsilon\right)^{2} m \epsilon^{2}}$,

$$
\min _{\theta} \frac{\left\|\theta-\theta^{1}\right\|_{2}^{2}+\left\|\theta-\theta^{2}\right\|_{2}^{2}}{\left\|\theta^{1}-\theta^{2}\right\|_{2}^{2}} \leq \frac{1}{2}+\frac{\frac{2 q}{\left(\frac{1+(M-1) r}{M}-\epsilon\right)^{2} m}+q}{c-\epsilon+2 q}
$$

At last, we used Cauchy's inequality and we completed the proof.

## B Proofs in Section 4

Before delving into Theorem 16, we first consider the simplest case where $L=2, d=1$ for gaining some intuition of the proof technique.

Proposition 23. Theorem 16 holds true for $L=2, d=1$.

Proof. Let $\theta_{i}=\left(A_{1}^{(i)}, A_{2}^{(i)}\right)$ for $i=1,2$ be the two global minima. We are aiming to find a $\theta^{*}=\left(A_{1}^{(3)}, A_{2}^{(3)}\right)$ satisfying

- $\theta^{*}$ is a global minima: $A_{1}^{(3)} A_{2}^{(3)}=Q$;
- $\theta_{1}$ and $\theta_{2}$ are 2-PL connected through $\theta^{*}$ : for any $t \in[0,1]$ and $i=1,2$, we have

$$
\left(t A_{1}^{(i)}+(1-t) A_{1}^{(3)}\right)\left(t A_{2}^{(i)}+(1-t) A_{2}^{(3)}\right)=Q
$$

Noticing that $\theta_{1}$ and $\theta_{2}$ are global minima, we have $A_{1}^{(i)} A_{2}^{(i)}=Q$ for $i=1,2$. Combining this with (16) leads to

$$
A_{1}^{(3)} A_{2}^{(i)}+A_{1}^{(i)} A_{2}^{(3)}=2 Q
$$

The problem now is converted to finding $A_{1}^{(3)} \in \mathbb{R}^{1 \times m}, A_{2}^{(3)} \in \mathbb{R}^{m \times 1}$ satisfied the following properties:

$$
\left\{\begin{array}{l}
A_{1}^{(1)} A_{2}^{(3)}=2 Q-A_{1}^{(3)} A_{2}^{(1)} \\
A_{1}^{(2)} A_{2}^{(3)}=2 Q-A_{1}^{(3)} A_{2}^{(2)} \\
A_{1}^{(3)} A_{2}^{(3)}=Q
\end{array}\right.
$$

1. When $A_{1}^{(1)}, A_{1}^{(2)}$ are linearly independent, we choose $A_{1}^{(3)}$ linearly independent of both $A_{1}^{(1)}$ and $A_{1}^{(2)}$. Then the problem above turns into solving a set of linear equations for $A_{2}^{(3)}$. Since $m \geq 3$, we can find a proper solution and finish the proof.
2. Suppose $k A_{1}^{(1)}=A_{1}^{(2)}$, we consider the first two equations, $\theta^{*}=\left(A_{1}^{(3)}, A_{2}^{(3)}\right)$ exists only if $A_{1}^{(3)}\left(k A_{2}^{(1)}-\right.$ $\left.A_{2}^{(2)}\right)=(2 k-2) C$, otherwise the first two equations will draw a contradiction by multiplying $k$ times in both sides of the first equation. Noticing that if $k A_{2}^{(1)}-A_{2}^{(2)}=0$, we have $Q=A_{1}^{(2)} A_{2}^{(2)}=k^{2} A_{1}^{(1)} A_{2}^{(1)}=k^{2} Q$, then $k=1$ or -1 . We note that we have assumed that $k \neq-1$, while for $k=1,\left(A_{1}^{(1)}, A_{1}^{(2)}\right)=\left(A_{1}^{(2)}, A_{2}^{(2)}\right)$ is a trivial case. Thus, with the condition $k A_{2}^{(1)}-A_{2}^{(2)} \neq 0$, we can find a solution $A_{1}^{(3)}$ for $A_{1}^{(3)}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)=(2 k-2) C$ that is linearly independent of $A_{1}^{(1)}, A_{2}^{(1)}$ (we can find $m-1 \geq 2$ linearly independent solutions in fact) first, then get a proper $A_{2}^{(3)}$ and finish the whole proof.

Remark 24. This will not hold for the case that $\left(A_{1}^{(1)}, A_{2}^{(1)}\right)=\left(-A_{1}^{(2)},-A_{2}^{(2)}\right)$, since $k=-1,\left(k A_{1}^{(2)}-\right.$ $\left.A_{2}^{(2)}\right)=0$ will directly draw $0=-4 A_{1}^{(2)} A_{2}^{(2)}$, which will be a contradiction when $A_{1}^{(2)} A_{2}^{(2)} \neq 0$. We outline a simple counter-example here: $A_{1}^{(1)}=(1,0,0,0), A_{2}^{(1)}=(1,0,0,0)^{T}, A_{1}^{(2)}=(-1,0,0,0), A_{2}^{(2)}=$ $(-1,0,0,0)^{T}, Q=1$. In particular, denote the center $A_{1}^{\prime}=\left(\alpha_{1}, \ldots, \alpha_{4}\right), A_{2}^{\prime}=\left(\beta_{1}, \ldots, \beta_{4}\right)$, the necessary conditions can be converted into $\alpha_{1}+\beta_{1}=2, \alpha_{1}+\beta_{1}=-2, \sum_{i=1}^{4} \alpha_{i} \beta_{i}=2$, which draw a contradiction.

## Proof of Theorem 16

The case of 2-PL connectivity. With the toy structure in Proposition 23, we can similarly consider the representation structure in Theorem 16 with the case $d>1$.

Proof. If we consider each column of $A_{2}$ separately, then the problem turns out to be the case in Proposition 23 by considering each column separately. Once $A_{1}^{(1)}, A_{1}^{(2)}$ are independent, we consider $A_{1}^{(3)}$ linearly independent of $A_{1}^{(1)}, A_{1}^{(2)}$ and find a solution for each column in $A_{2}^{(3)}$ independently, then the problem is solved directly by applying the case with $d=1$ separately.

Now we consider the case that $k A_{1}^{(1)}=A_{1}^{(2)}$ for some $k \in \mathbb{R}$, in this case by considering conditions

$$
\left\{\begin{array}{l}
A_{1}^{(1)} A_{2}^{(3)}=2 Q-A_{1}^{(3)} A_{2}^{(1)} \\
A_{1}^{(2)} A_{2}^{(3)}=2 Q-A_{1}^{(3)} A_{2}^{(2)}
\end{array}\right.
$$

we need $A_{1}^{(3)}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)=(2 k-2) Q$. We view it as solving linear equations $A_{1}^{(3)}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)=$ $(2 k-2) Q$ for $A_{1}^{(3)}$. Denote $Q=\left(Q_{1}, \ldots, Q_{n}\right)$. If $\operatorname{rank}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)=d<m$, it would be easy to find a solution $A_{1}^{(3)}$ that is additionally independent to $A_{1}^{(1)}$. Otherwise, if $\operatorname{rank}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)<d$, without loss of generality, we consider a case of column-wise linear dependency. Assume that the first two columns of $A_{2}^{(1)}, A_{2}^{(2)}$ are $\left(\alpha_{1}, \alpha_{2}\right),\left(\beta_{1}, \beta_{2}\right)$, respectively. If $k \alpha_{1}-\beta_{1}=t\left(k \alpha_{2}-\beta_{2}\right)$, we naturally have

$$
k^{2} Q_{1}-Q_{1}=A_{1}^{(2)}\left(k \alpha_{1}-\beta_{1}\right)=t A_{1}^{(2)}\left(k \alpha_{2}-\beta_{2}\right)=t k^{2} Q_{2}-t Q_{2}
$$

We have assumed that $k \neq-1$. If $k=1$, the linear connectivity always holds naturally. On the other hand, if $k^{2} \neq 1$, we will obtain $Q_{1}=t Q_{2}$, which will never affect the linear equations in $A_{1}^{(3)}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)=$ $(2 k-2) Q$.

Thus, we can find a solution $A_{1}^{(3)}$ that satisfies $A_{1}^{(3)}\left(k A_{2}^{(1)}-A_{2}^{(2)}\right)=(2 k-2) Q$ for $A_{1}^{(3)}$ and independent to $A_{1}^{(1)}$. With this, we can then derive a proper $A_{2}^{(3)}$ by considering each column separately as in Proposition 23. Then, we finish our proof of Theorem 16.

The case of 3-PL connectivity. For two minima

$$
\theta_{1}=\left(A_{L}^{(1)}, A_{L-1}^{(1)}, \ldots, A_{1}^{(1)}\right), \theta_{2}=\left(A_{L}^{(2)}, A_{L-1}^{(2)}, \ldots, A_{1}^{(2)}\right)
$$

that belong to the zero-measure set in the proof of 2-PL connectivity, we consider $\theta_{3}=\left(A_{L}^{\prime}, A_{L-1}^{(1)}, \ldots, A_{1}^{(1)}\right)$, where $A_{L}^{\prime}$ satisfies that $A_{L}^{\prime} A_{L-1}^{(1)} \ldots A_{1}^{(1)}=Q$. Then it is natural that $\theta_{1} \leftrightarrow \theta_{3}$.

We consider the following linear relationship: $A_{L}^{\prime} A_{L-1}^{(1)} \ldots A_{t}^{(1)}$ and $A_{L}^{(2)} A_{L-1}^{(2)} \ldots A_{t}^{(2)}$ are linearly independent for $t=L, \ldots, 2$, which would yield 2-PL connectivity of $\theta_{2}$ and $\theta_{3}$ following by the discussion above. To satisfy the $L-1$ conditions along with $A_{L}^{\prime} A_{L-1}^{(1)} \ldots A_{1}^{(1)}=Q$, we consider seeking for $F_{L}, \ldots, F_{2}$ such that $F_{j}$ is independent of $A_{L}^{(2)} \ldots A_{j}^{(2)}$ for $j=2, \ldots, L$. Then we consider $A_{L}^{\prime} A_{L-1}^{(1)} \ldots A_{j}^{(1)}=F_{j}$ for $j=2, \ldots, L$ and $A_{L}^{\prime} A_{L-1}^{(1)} \ldots A_{1}^{(1)}=Q$ as $L$ linear equations on the $m_{1}$ parameters in $A_{L}^{\prime}$. We have assumed that $m>2 L-1$, thus if $E_{t}=A_{L-1}^{(1)} \ldots A_{t}^{(1)}, t=L, \ldots, 1\left(E_{L}=\mathbf{1}_{m}\right)$ are linearly independent, the linear system would have a proper solution.

On the other hand, as we need to select $F_{L}, \ldots, F_{2}$ to make sure the linear equations have a solution, we consider solving the dependency by the following adjustments. If some of the $E_{j}$ 's are linearly dependent, for instance, $E_{k}$ can be represented by the linear combination of another group of $E_{j}$ 's, then our $F_{k}$ need to be automatically determined by the corresponding $F_{j}$ 's to ensure the existence of solutions. Since $F_{k}$ need to be independent of $A_{L-1}^{(2)} \ldots A_{k}^{(2)}$, here we (might) lose a degree of freedom when selecting $F_{j}$ 's, while the fact that we do not need to consider $F_{k}$ anymore reduces an equation from the $L$ conditions required. Thus, in the process of reducing our restrictions to be linearly independent, our degree of freedom would always be greater than the number of restrictions since $m>2 L-1$ at the beginning. Thus, with the (eventually) linear-independent coefficients (with the number of restrictions less than parameters), we will have a proper solution of $A_{L}^{\prime}$ that meets the above conditions, which would yield $\theta_{2} \leftrightarrow \theta^{*}, \theta^{*} \leftrightarrow \theta_{3}$ for some $\theta^{*}$ from the first statement. Thus we will have $\theta_{1} \leftrightarrow \theta_{3}, \theta_{3} \leftrightarrow \theta_{*}, \theta_{*} \leftrightarrow \theta_{2}$.

## B. 1 Proof of Theorem 18

We first propose a lemma about linear independence which we will use in our later proof.

Lemma 25. For linearly independent vectors $C_{1}, \ldots, C_{p} \in \mathbb{R}^{1 \times r_{1}}$, linearly independent vectors $D_{1}, \ldots, D_{q} \in$ $\mathbb{R}^{1 \times r_{2}}$, and vectors $E_{1}, \ldots, E_{p} \in \mathbb{R}^{1 \times r_{2}}$, if $r_{2}>p+q$ and $r_{1}>q$, there exist a matrix $K \in \mathbb{R}^{r_{1} \times r_{2}}$ such that the $p+q$ vectors $C_{i} K+E_{i}(i=1,2, \ldots, p), D_{i}(i=1,2, \ldots, q)$ are linearly independent.

Proof. Since $r_{2}>p+q$, we can find another $p$ vectors $F_{1}, \ldots, F_{p}$ such that $D_{1}, \ldots, D_{q}, F_{1}, \ldots, F_{p}$ are linearly independent.

Then, we consider the $p$ equations $C_{i} K+E_{i}=F_{i}(i=1,2, \ldots, p)$. Since $C_{1}, \ldots, C_{p} \in \mathbb{R}^{1 \times r_{1}}$ are independent and $r_{1}>p$, we can find a solution for $K$ by considering each column of $K$ separately.

Thus, with $C_{i} K+E_{i}=F_{i}(i=1,2, \ldots, p)$ and the linear independence of $D_{1}, \ldots, D_{q}, F_{1}, \ldots, F_{p}$, we finish our proof of the lemma.

Now we begin with our proof of 18 .

Proof. Following the explicit description in (5), it is natural to consider whether the explicit representation of linear layers achieves $A_{L}^{*} \ldots A_{2}^{*} A_{1} *$. As a set out of only zero-measure points in the minima manifold, we consider an assumption below:

Assumption 26. For all $k=1,2, \ldots, n-1$, the $r$ vectors $A_{L}^{(i)} \ldots A_{2}^{(i)} A_{1}^{(i)} \in \mathbb{R}^{1 \times m}(i=1,2, \ldots, r)$ are linearly independent.

To begin, for each $i \in[1, r], q=1,2, \ldots, L$, we define $\sigma_{i, k, q}$ to be the sum of all $C_{q}^{k}$ elements in $\left\{B_{L} B_{L-1} \ldots B_{L-q+1} \mid\right.$ for $j \in\{1, \ldots, q\}$, only $k$ of $B_{j}$ to be $A_{j}^{i}$, while the remaining $q-k B_{j}$ to be $\left.A_{j}^{*}\right\}$,

With this notation, our desirable connectivity property can be written in terms that

$$
\left(t A_{L}^{(i)}+(1-t) A_{L}^{*}\right)\left(t A_{L-1}^{(i)}+(1-t) A_{L-1}^{*}\right) \ldots\left(t A_{1}^{(i)}+(1-t) A_{1}^{*}\right)=\sum_{j=0}^{L} t^{j}(1-t)^{L-j} \sigma_{i, j, L}
$$

for all $i=1,2, \ldots, r$ and $j=1,2, \ldots, L$. Since this should be right for any $t \in[0,1]$ in the context of star-shaped connectivity, it is natural to find $A_{1}^{*}, \ldots, A_{L}^{*}$ such that $\sigma_{i, k, L}=C_{L}^{k} Q$ for all $i$ and $k$, which are the necessary condition followed by considering different order terms of $t$. On the other hand, if this holds, we will directly derive that each point in the star-shaped manifold is an exact minimum, i.e., for any $t \in[0,1]$,

$$
\left(t A_{L}^{(i)}+(1-t) A_{L}^{*}\right)\left(t A_{L-1}^{(i)}+(1-t) A_{L-1}^{*}\right) \ldots\left(t A_{1}^{(i)}+(1-t) A_{1}^{*}\right)=\sum_{j=0}^{L} C_{L}^{j} t^{j}(1-t)^{L-j} Q=Q
$$

Now we start to construct $A_{1}^{*}, \ldots, A_{L}^{*}$ inductively. Firstly, consider the case in Assumption 26 when $k=1$. Since $m>r+1$, we can find $A_{L}^{*}$ by Lemma 25 such that $\mathcal{C}_{1}=\left\{A_{L}^{*}, A_{L}^{(1)}, \ldots, A_{L}^{(r)}\right\}$ are linearly independent.

Then, we consider Assumption 26 with $k=2$. We notice that $A_{L}^{*}, A_{L}^{(1)}, \ldots, A_{L}^{(r)}$ are linearly independent and $m>2 r+1, m>r$, then following Lemma 25, we can find $A_{L-1}^{*}$ such that the $2 r+1$ vectors in

$$
\mathcal{C}_{L-1}=\left\{A_{L}^{(i)} A_{L-1}^{*}+A_{L}^{*} A_{L-1}^{(i)}(i=1,2, \ldots, r), A_{L}^{(i)} A_{L-1}^{(i)}(i=1,2, \ldots, r), A_{L}^{*} A_{L-1}^{*}\right\}
$$

are linearly independent.

We repeat the process using Assumption 2,3 and Lemma 25 to accumulate more layers while keeping with their independent property. In particular, with $w r+1(1<w<L-1)$ linearly independent vectors in

$$
\begin{array}{r}
\mathcal{C}_{w}=\left\{\sigma_{i, k, w-1} A_{L-w+1}^{*}+\sigma_{i, k-1, w-1} A_{L-w+1}^{i}(k=1, \ldots, w-1 ; i=1, \ldots, r)\right. \\
\left.A_{L}^{*} A_{L-1}^{*} \ldots A_{L-w+1}^{*}, A_{L}^{(i)} A_{L-1}^{(i)} \ldots A_{L-w+1}^{(i)}(i=1,2, \ldots, r)\right\}
\end{array}
$$

we consider Lemma 25 to obtain $K$ as $A_{L-w}^{*}$, with $D_{i}$ being independent vectors $A_{L}^{(i)} \ldots A_{1}^{(i)}, i=1,2, \ldots, r$ being ensured by Assumption 26. By doing so, we derive a new group of independent vectors

$\mathcal{C}_{w+1}=\left\{\sigma_{i, k, w} A_{L-w}^{*}+\sigma_{i, k-1, w} A_{L-w}^{i}(k=1, \ldots, w ; i=1, \ldots, r), A_{L}^{*} A_{L-1}^{*} \ldots A_{L-w}^{*}, A_{L}^{(i)} A_{L-1}^{(i)} \ldots A_{L-w}^{i}(i=1,2, \ldots, r)\right\}$.

Thus, by induction, we can sequentially get $A_{L}^{*}, \ldots, A_{2}^{*}$ such that all $(L-1) r+1$ vectors

$$
\begin{array}{r}
\mathcal{C}_{L-1}=\left\{\sigma_{i, k, L-2} A_{2}^{*}+\sigma_{i, k-1, L-2} A_{2}^{i}(k=1, \ldots, L-2 ; i=1, \ldots, r)\right. \\
\left.A_{L}^{*} A_{L-1}^{*} \ldots A_{2}^{*}, A_{L}^{(i)} A_{L-1}^{(i)} \ldots A_{2}^{i}(i=1,2, \ldots, r)\right\}
\end{array}
$$

are linearly independent.

We illustrate that keeping such linearly independent properties in induction is of essential importance in this proof, which shares the very essence in Theorem 16, providing a sufficient condition for us to obtain the proper solution of the linear equations.

Finally, recall that we aim to make sure $\sigma_{i, k, L}=C_{L}^{k} Q$ for all $i=1,2, \ldots, r$ and $k=0,1, \ldots, L$. Consider that the case for $k=L$ is naturally true, and all $r$ equations when $k=0$ are the same, we can therefore view that as $(L-1) r+1$ linear equations of variable $A_{1}^{*}$ since $A_{L}^{*}, \ldots, A_{2}^{*}$ have been fixed. Since all the coefficients of $A_{1}^{*}$ in the $(L-1) r+1$ equations are actually the $(L-1) r+1$ vectors in $\mathcal{C}_{L-1}$, which are linearly independent, we can therefore find a proper solution for $A_{1}^{*}$ by considering each column in $A_{1}^{*}$ separately. The condition $m>(L-1) r+1$ in Assumption 2 makes sure of the existence of the solution.

Thus, we finish the construction of $A_{L}^{*}, \ldots, A_{1}^{*}$, which satisfies the required property, and finish the proof.


[^0]:    "The first two authors contributed equally and the order was determined by a coin flip. This work was done when the first two authors were undergraduate students at Peking University.

    ${ }^{\dagger}$ Corresponding author

