# Kun Zhang 1 2 Shaoan Xie 1Ignavier Ng 1 **Yujia Zheng** 1

## Abstract

In many problems, the measured variables (e.g.,
image pixels) are just mathematical functions of the hidden causal variables (e.g., the underlying concepts or objects). For the purpose of making predictions in changing environments or making proper changes to the system, it is helpful to recover the hidden causal variables Zi and their causal relations represented by graph GZ.

This problem has recently been known as causal representation learning. This paper is concerned with a general, completely nonparametric setting of causal representation learning from multiple distributions (arising from heterogeneous data or nonstationary time series), without assuming hard interventions behind distribution changes.

We aim to develop general solutions in this fundamental case; as a by product, this helps see the unique benefit offered by other assumptions such as parametric causal models or hard interventions. We show that under the sparsity constraint on the recovered graph over the latent variables and suitable sufficient change conditions on the causal influences, interestingly, one can recover the moralized graph of the underlying directed acyclic graph, and the recovered latent variables and their relations are related to the underlying causal model in a specific, nontrivial way. In some cases, each latent variable can even be recovered up to component-wise transformations.

Experimental results verify our theoretical claims.

## 1. Introduction

Causal representation learning holds paramount significance across numerous fields, offering insights into intricate relationships within datasets. Most traditional methodologies
(e.g., causal discovery) assume the observation of causal variables. This assumption, however reasonable, falls short in complex scenarios involving indirect measurements, such as electronic signals, image pixels, and linguistic tokens.

1Carnegie Mellon University 2Mohamed bin Zayed University of Artificial Intelligence.

Moreover, there are usually changes on the causal mechanisms in real-world, such as the heterogeneous or nonstationary data. Identifying the hidden causal variables and their structures together with the change of the causal mechanism is in pressing need to understand the complicated real-world causal process. This has been recently known as causal representation learning (Scholkopf et al. ¨ , 2021).

It is worth noting that identifying only the hidden causal variables but not the structure among them, is already a considerable challenge. In the i.i.d. case, different latent representations can explain the same observations equally well, while not all of them are consistent with the true causal process. For instance, nonlinear independent component analysis (ICA), where a set of observed variables X is represented as a mixture of independent latent variables Z, i.e, X = g(Z), is known to be unidentifiable without additional assumptions (Comon, 1994). While being a strictly easier task since there are no relations among hidden variables, the identifiability of nonlinear ICA often relies on conditions on distributional assumptions (non-i.i.d. data) (Hyvarinen & ¨ Morioka, 2016; 2017; Hyvarinen et al. ¨ , 2019; Khemakhem et al., 2020a; Sorrenson et al., 2020; Lachapelle et al., 2022; Halv ¨ a & Hyv ¨ arinen ¨ , 2020; Halv ¨ a et al. ¨ , 2021; Yao et al.,
2022) or specific functional constraints (Comon, 1994; Hyvarinen & Pajunen ¨ , 1999; Taleb & Jutten, 1999; Buchholz et al., 2022; Zheng et al., 2022; Zheng & Zhang, 2023).

To generalize beyond the independent hidden variables and achieve causal representation learning (recovering the latent variables and their causal structure), recent advances either introduce additional experiments in the forms of interventional or counterfactual data, or place more restrictive parametric or graphical assumptions on the latent causal model. For observational data, various graphical conditions have been proposed together with parametric assumptions such as linearity (Silva et al., 2006; Cai et al., 2019; Xie et al., 2020; 2022; Adams et al., 2021; Huang et al., 2022) and discreteness (Kivva et al., 2021).

For interventional data, single-node interventions have been considered together with parametric assumptions (e.g., linearity) on the mixing function (Varici et al., 2023; Ahuja et al., 2023; Buchholz et al., 2022) or also on the latent causal model (Squires et al., 2023). The nonparametric settings for both the mixing function and causal model have been explored by (Brehmer et al., 2022; von Kugelgen et al. ¨ ,
2023; Jiang & Aragam, 2023) together with additional assumptions on counterfactual views (Brehmer et al., 2022),
distinct paired interventions (von Kugelgen et al. ¨ , 2023),
and graphical conditions (Jiang & Aragam, 2023).

Despite the exciting developments in the field, one fundamental question pertinent to causal representation learning from multiple distributions remains unanswered–in the most general situation, without assuming parametric models on the data-generating process or the existence of hard interventions in the data, what information of the latent variables and the latent structure can be recovered? This paper attempts to provide an answer to it, which, surprisingly, shows that each latent variable can be recovered up to clearly defined indeterminacies. It suggests what we can achieve in the general case and furthermore, what unique contribution the typical assumptions that are currently made in causal representation learning from multiple distributions make towards complete identifiability of the latent variables (up to component-wise transformations). This may make it possible to figure out what minimal assumptions are needed to achieve complete identifiability, given partial knowledge of the system.

Contributions. Concretely, as our contributions, we show that under the sparsity constraint on the recovered graph over the latent variables and suitable sufficient change conditions on the causal influences, interestingly, one can recover the moralized graph of the underlying directed acyclic graph (Thm. 3.1), and the recovered latent variables and their relations are related to the underlying causal model in a specific, nontrivial way (Thm. 3.4)–each latent variables is recovered as a function of itself and its so-called intimate neighbors in the Markov network implied by the true causal structure over the latent variables. Depending on the properties of the true causal structure over latent variables, the set of intimate neighbors might even be empty, in which case each latent variable can be recovered up to an invertible transformation (Remark 1). Lastly, we show how the recovered moralized graph relates to the underlying causal graph under new relaxations of faithfulness assumption (Thm.

3.5). Simulation studies verified our theoretical findings.

## 2. Problem Setting

Let X = (X1*, . . . , X*d) be an d-dimensional random vector that represents the observations. We assume that they are generated by n hidden causal variables Z = (Z1*, . . . , Z*n)
via a nonlinear injective mixing function g : R
n → R
d
(d ≥ n), which is also a C
2 diffeomorphism. Furthermore, the variables Zi's are assumed to follow a structural equation model (SEM) (Pearl, 2000). Putting them together, the data generating process can be written as

$$\underbrace{X=g(Z)}_{\text{Nonlinear mixing}},\quad\underbrace{Z_{i}=f_{i}(\text{PA}(Z_{i}),\epsilon_{i};\theta_{i}),i=1,\ldots,n}_{\text{Latent SEM}}.\tag{1}$$



where PA(Zi) denotes the parents of variable Zi, ϵi's are exogenous noise variables that are mutually independent, and θi denotes the latent (changing) factor (or effective parameters) associated with each model. Here, the data generating process of each hidden variable Zi may change, e.g., across domains or over time, governed by the corresponding latent factor θi; it is commonplace to encounter such changes in causal mechanisms in practice (arising from heterogeneous data or nonstationary time series). In addition, interventional data can be seen as a special type of change, which qualitatively restructure the causal relations.

As their names suggest, we assume that the observations X
are observed, while the hidden causal variables Z and latent factors θ = (θ1*, . . . , θ*n) are unobserved.

Let PX and PZ be the distributions of X and Z, respectively, and their corresponding probability density functions be pX(X; θ) and pZ(Z; θ), respectively. To lighten the notation, we drop the subscript in the density when the context is clear. The latent SEM in Eq. (1) induces a causal graph GZ with vertices {Zi}
n i=1 and edges Zj → Ziif and only if Zj ∈ PA(Zi). We assume that GZ is acyclic, i.e., a directed acyclic graph (DAG). This implies that the distribution of variables Z satisfy the Markov property w.r.t. DAG GZ
(Pearl, 2000), i.e., p(Z; θ) = Qn i=1 p(Zi| PA(Zi); θi). We provide an example of the data generating process in Eq.

(1) and its corresponding latent DAG GZ in Figure 1. In particular, given the observations X arising from multiple distributions (governed by the latent factors θ), our goal is to recover the hidden causal variables Z = g
−1(X) and their causal relations up to surprisingly minor indeterminacies.

## 3. Learning Causal Representations With Sparsity Constraints

In this section, we provide theoretical results to show how one is able to recover the underlying hidden causal variables and their causal relations up to certain indeterminacies. Specifically, we show that under the sparsity constraint on the recovered graph over the latent variables and suitable sufficient change conditions on the causal influences, the recovered latent variables are related to the underlying hidden causal variables in a specific, nontrivial way. Such theoretical results serve as the foundation of our algorithm described in Section 4.

To start with, we estimate a model (ˆg, ˆ*f, p*Zˆ) which assumes the same data generating process as in Eq. (1) and matches the true distribution of X in different domains:

$$p_{X}(X^{\prime};\theta^{\prime})=p_{\bar{X}}(X^{\prime};\theta^{\prime}),\quad\forall X^{\prime},\theta^{\prime}.\tag{2}$$
3
where X and Xˆ are generated from the true model (*g, f, p*Z)
and the estimated model (ˆg, ˆ*f, p*Zˆ), respectively.

A key ingredient in our theoretical analysis is the Markov network that represents conditional dependencies among random variables in a graphical manner via an undirected graph. Let MZ be the Markov network over variables Z, specifically, with vertices {Zi}
n i=1 and edges (*i, j*) ∈
E(MZ) if and only if Zi ⊥̸⊥ Zj | Z[n]\{i,j}.

1 Also, we denote by |MZ| the number of undirected edges in the Markov network. In Section 3.1, apart from showing how to estimate the underlying hidden causal variables up to certain indeterminacies, we also show that such latent Markov network MZ can be recovered up to trivial indeterminacies
(i.e., relabeling of the hidden variables). To achieve so, we make use of the following property (assuming that pZ is twice differentiable):

$$Z_{i}\perp\!\!\!\perp Z_{j}\mid Z_{[n]\setminus\{i,j\}}\iff\frac{\partial^{2}\log p(Z)}{\partial Z_{i}\partial Z_{j}}=0.$$

Such a connection between pairwise conditional independence and cross derivatives of the density function has been noted by Lin (1997) and utilized in Markov network learning for observed variables (Zheng et al., 2023). With the recovered latent Markov network structure, we provide results in Section 3.2 to show how it relates to the true latent causal DAG GZ, by exploiting a specific type of faithfulness assumption that is considerably weaker than the standard faithfulness assumption used in the literature of causal discovery (Spirtes et al., 2001).

## 3.1. Recovering Hidden Causal Variables And Latent Markov Network

We show how one benefits from multiple distributions to recover the hidden causal variables and the true Markov network structure among them up to minor indeterminacies, by making use of sparsity constraint and sufficient change conditions on the causal mechanisms.

We start with the following result that provides information about the relationship between the Markov network MZ
1We use [n] to denote {1*, . . . , n*} and Z[n]\{i,j} to denote
{Zi}
n i=1 \ {Zi, Zj}.

over true hidden causal variables Z and the Markov network MZˆ over the estimated hidden variables Zˆ. This result serves as the backbone of our further analysis in this section.

Denote by ⊕ the vector concatenation symbol.

Theorem 3.1. Let the observations be sampled from the data generating process in Eq. (1), and MZ *be the Markov* network over Z*. Suppose that the following assumptions* hold:

- *A1 (Smooth and positive density): The probability density function of latent causal variables is smooth and* positive, i.e. pZ is smooth and pZ > 0 *over* R
n.

- *A2 (Sufficient changes): For any* Z ∈ R
n, there exist 2n + |MZ| + 1 values of θ*, i.e.,* θ
(u) *with* u = 0, . . . , 2n+|MZ|, such that the vectors w(*Z, u*)−
w(z, 0) *with* u = 1, . . . , 2n + |MZ| are linearly independent, where vector w(Z, u) *is defined as*

$$w(Z,u)=\left(\frac{\partial\log p(Z;\theta^{(u)})}{\partial Z_{1}},\ldots,\frac{\partial\log p(Z;\theta^{(u)})}{\partial Z_{n}},\right.$$ $$\left.\frac{\partial^{2}\log p(Z;\theta^{(u)})}{\partial Z_{1}^{2}},\ldots,\frac{\partial^{2}\log p(Z;\theta^{(u)})}{\partial Z_{n}^{2}}\right)$$ $$\left.\frac{\partial^{2}\log p(Z;\theta^{(u)})}{\partial Z_{i}\partial Z_{j}}\right)_{(i,j)\in\mathcal{E}(\mathcal{M}_{Z})}.$$

Suppose that we learn (ˆg, ˆf, pZˆ) to achieve Eq. (2). Then, for every pair of estimated hidden variables Zˆk and Zˆlthat are **not adjacent in the Markov network** MZˆ over Zˆ, we have the following statements:

(a) Each true hidden causal variable Zi*is a function of at* most one of Zˆk and Zˆl.

(b) For each pair of true hidden causal variables Zi and Zj that are adjacent in the Markov network MZ over Z*, at most one of them is a function of* Zˆk or Zˆl.
The proof is provided in Appx. A. Here is the basic idea.

Let h
′
i,l := ∂Zi
∂Zˆl
, and h
′′
i,kl =∂
2Zi
∂Zˆk∂Zˆl
. Under the assumptions A1 and A2, one can finally show that the following constraints hold:

$$h^{\prime}_{i,l}h^{\prime}_{i,k}=0,\tag{3}$$ $$h^{\prime}_{j,l}h^{\prime}_{i,k}=0,$$ (4) $$h^{\prime\prime}_{i,kl}=0.\tag{5}$$

Eq. (3) indicates that Ziis a function of at most one of Zˆk and Zˆl, while Eq. (4) implies that given that Zi and Zj are adjacent in Markov network MZ, at most one of them is a function of Zˆk or Zˆl.

It is worth noting that the requirement of a sufficient number of environments has been commonly adopted in the literature (e.g., see (Hyvarinen et al. ¨ , 2023) for a recent survey), such as visual disentanglement (Khemakhem et al.,
2020b), domain adaptation (Kong et al., 2022), video analysis (Yao et al., 2021), and image-to-image translation (Xie et al., 2022). Also, we do not specify exactly how to learn
(ˆg, ˆ*f, p*Zˆ) to achieve Eq. (2), and leave the door open for different approaches to be used, such as normalizing flow or variational approaches. For example, we adopt a variational approach in Section 4.

The above result sheds light on how each pair of the estimated latent variables Zˆk and Zˆlthat are not adjacent in Markov network MZˆ relate to the true hidden causal variables Z. Without any constraint on the estimating process, a trivial solution would be a complete graph over Zˆ. To avoid it, we enforce the sparsity of the Markov network over Zˆ.

In fact, the Markov network of the underlying DAG GZ can be recovered, as shown in the following theorem, with a proof provided in Appx. B.

Theorem 3.2 (Identifiability of Latent Markov Network).

Let the observations be sampled from the data generating process in Eq. (1), and MZ *be the Markov network over* Z. Suppose that Assumptions A1 and A2 from Theorem 1 hold. Suppose also that we learn (ˆg, ˆf, pZˆ) to achieve Eq.

(2) with the minimal number of edges of Markov network MZˆ over Zˆ. Then, the Markov network MZˆ *over estimated* hidden variables Zˆ *is isomorphic to the true latent Markov* network MZ.

Since traditional nonlinear ICA always has a valid solution
(to produce nonlinear independent components) (Hyvarinen ¨
et al., 1999), one may wonder whether it is possible to find nonlinear components as functions of X that are independent in each domain, as produced by recent methods for nonlinear ICA with surrogates (Hyvarinen et al. ¨ , 2019). As a corollary of the above theorem, we show that the answer is no–there do not exist nonlinear components that are independent across domains.

Corollary 3.3 (Impossibility of Finding Independent Components). *Let the observations be sampled from the data* generating process in Eq. (1), and MZ be the Markov network over Z. Suppose that Assumptions A1 and A2 from Theorem 1 hold, and that MZ is not an empty graph. Suppose also that we learn (ˆg, ˆf, pZˆ) *with the components of* Zˆ
being independent in each domain. Then, (ˆg, ˆf, pZˆ) *cannot* achieve Eq. (2).

Apart from recovering the true Markov network MZ, we show that the sparsity constraint on the Markov network structure over Zˆ also allows us to recover the underlying hidden causal variables Z up to specific, relatively minor indeterminacies. In the result, the following variable set, termed *intimate neighbor set*, plays an important role:

ΨZi
:= {Zj | j ̸= i, but Zj is adjacent to Zi and all other neighbors of Ziin MZ}.

4
For example, according to the Markov network implied by GZ in Figure 1, ΨZ1 = {Z2}, ΨZ2 = Φ, where Φ denotes the empty set, ΨZ3 = {Z2, Z4}, ΨZ4 = Φ, and ΨZ5 = {Z4}. As another example, according to the Markov network in Figure 2(b), which is implied by the DAG in Figure 2(a), we have ΨZi = Φ for i = 1, 2, 3, 5, 6 and ΨZ4 = {Z3, Z6}.

Theorem 3.4 (Identifiability of Hidden Causal Variables).

Let the observations be sampled from the data generating process in Eq. (1), and MZ *be the Markov network over* Z*. Let* NZi be the set of neighbors of variable Ziin MZ.

Suppose that Assumptions A1 and A2 from Theorem 1 hold.

Suppose also that we learn (ˆg, ˆf, pZˆ) to achieve Eq. (2)
with the minimal number of edges of Markov network MZˆ
over Zˆ. Then, there exists a permutation π *of the estimated* hidden variables, denoted as Zˆπ, such that each Zˆπ(i)*is a* function of (a subset of) the variables in {Zi} ∪ ΨZi
.

The proof is given in Appx. D. It is worth noting that in many cases, the above result already enables us to recover some of the hidden variables up to a component-wise transformation.

Remark 1. No matter how many neighbors each hidden causal variable Zi *has, as long as each of its neighbors is* not adjacent to at least one other neighbor in the Markov network MZ, then Zi *can be recovered up to a componentwise transformation.*
Even if the above case does not hold, Theorem 3.4 still shows how the estimated hidden variables relate to the underlying causal variables in a specific, nontrivial way. Two examples are provided below.

Example 1. First consider the Markov network MZ corresponding to the DAG GZ over Ziin Figure 1. By Theorem 3.4 *and suitable permutation of estimated hidden variables* Zˆ*, we have: (a)* Zˆπ(1) is a function of Z1 and possibly Z2,
(b) Zˆπ(2) is a function of Z2*, (c)* Zˆπ(3) *is a function of* Z3 and possibly Z2, Z4*, (d)* Zˆπ(4) is a function of Z4*, and (d)* Zˆπ(5) is a function of Z5 and possibly Z4. In this example, the hidden causal variables Z2 and Z4 can be recovered up to component-wise transformation, while variables Z1, Z3, and Z5 can be identified up to mixtures with certain neighbors in the Markov network.

Example 2. One may think that generally speaking, the more complex GZ*, the more indeterminacies we have in the* estimated latent variables (in the sense that each estimated latent variable receives contributions from more latent variables). In fact, this may not be the case. In example 2, the



Figure 2: Illustrative example 2.

underlying latent causal graph GZ is given in Figure 2(a),
which involves more variables and more edges and whose Markov network is shown in Figure 2(b). For every variables Zi*that is not the sink node, it has* ΨZi = Φ *and thus* can be recovered up to a component-wise transformation.

Permutation of estimated latent variables. Theorems 3.2 and 3.4 involve certain permutation of the estimated hidden variables Zˆ. Such an indeterminacy is common in the literature of causal discovery and representation learning tasks involving latent variables. In our case, since the function h := ˆg
−1 ◦ g where Zˆ = h(Z) is invertible, there exists a permutation of the latent variables such that the corresponding Jacobian matrix Jh has nonzero diagonal entries
(see Lemma 2 in Appx. B); such a permutation is what Theorems 3.2 and 3.4 refer to.

## 3.2. From Latent Markov Network To Latent Causal Dag

Now we have identified the Markov network up to an isomorphism, which characterizes conditional independence relations in the distribution. To build the connection between Markov network or conditional independence relations and causal structures, prior theory relies on the Markov and faithfulness assumptions. However, in real-world scenarios, the faithfulness assumption could be violated due to various reasons including path cancellations
(Zhang & Spirtes, 2008; Uhler et al., 2013).

Since our goal is to generalize the identifiability theory as much as possible to fit practical applications, we introduce two relaxations of the faithfulness assumptions:
Assumption 1 (Single adjacency-faithfulness (SAF)).

Given a DAG GZ and distribution PZ over the variable set Z, if two variables Zi and Zj are adjacent in GZ*, then* Zi ⊥̸⊥Zj |Z[n]\{i,k}.

Assumption 2 (Single unshielded-collider-faithfulness (SUCF) (Ng et al., 2021)). *Given a latent causal graph* GZ and distribution PZ over the variable set Z*, let* Zi → Zj ← Zk be any unshielded collider in GZ, then Zi ⊥̸⊥
Zk|Z[n]\{i,k}.

We propose SAF as a relaxtion of the Adjacencyfaithfulness (Ramsey et al., 2012). The SUCF assumption is first introduced by Ng et al. (2021), which is strictly weaker than Orientation-faithfulness (Ramsey et al., 2012). Thus, both of them are strictly weaker than the faithfulness assumption, since the combination of Adjacency-faithfulness and Orientation-faithfulness is weaker than the faithfulness assumption (Zhang & Spirtes, 2008).

Interestingly, not only they are weaker variants of faithfulness, but we also prove that they are actually necessary and sufficient conditions, thus the weakest possible ones, to bridge conditional independence relations and causal structures. Specifically, we show that the recovered Markov network is exactly the moralized graph of the true causal DAG if and only if the proposed variants of faithfulness hold. The proofs of Lemma 1 and Theorem 3.5 are shown in Appx. E.

Lemma 1. Given a latent causal graph GZ *and distribution* PZ with its Markov Network MZ, under Markov assumption, the undirected graph defined by MZ is a subgraph of the moralized graph of the true causal DAG G.

Theorem 3.5. Given a causal DAG GZ *and distribution* PZ
with its Markov Network MZ, under Markov assumption, the undirected graph defined by MZ is the moralized graph of the true causal DAG GZ *if and only if the SAF and SUCF*
assumptions are satisfied.

It is worth noting that the connection between conditional independence relations and causal structures has been developed by (Loh & Buhlmann ¨ , 2014; Ng et al., 2021) in the linear case by leveraging the properties of the inverse covariance matrix; our results here focus on the nonparametric case and thus being able to serve the considered general settings for identifiability. Also note that the necessary and sufficient assumptions may also be of independent interest for other causal discovery tasks exploring conditional independence relations in the nonparametric case.

Discussion on additional assumptions. We investigated how the sparsity constraint on the recovered graph over latent variables and sufficient change conditions on causal influences can be used to recover the latent variables and causal graph up to certain indeterminacies. Our framework is connected with previous ones in a spectrum of related studies (Varici et al., 2023; Ahuja et al., 2023; Buchholz et al., 2022; Squires et al., 2023; Brehmer et al., 2022; von Kugelgen et al. ¨ , 2023; Brehmer et al., 2022; von Kugelgen ¨ et al., 2023; Zheng & Zhang, 2023; Zhang et al., 2023). For instance, the connection between conditional independence and cross-derivatives of the log density in both linear and nonlinear cases means our theorems directly apply to linear SEMs. Furthermore, our results do not require the mixing function to be sufficiently nonlinear, allowing them to encompass linear mixing processes as well.

At the same time, we may be able to leverage possible parametric constraints on the data generating process (or functions) or specific types of interventions. For instance, if we know that the changes happen to the linear causal mechanisms with Gaussian noises, this constraint can readily help reduce the search space and improve the identifiability.

Moreover, since we only require the changing distribution, any type of interventions will be covered since any change to the conditional distribution is allowed. Given the additional information illustrated by experimental interventions
(e.g., single-node interventions), alternative identifiability that might be particularly useful in certain tasks can be established. We hope this work can provide a helpful, bigger picture of causal representation learning in the general setting and further illustrates the necessity and connections of the different assumptions formulated in this line of works.

## 4. Change Encoding Network For Representation Learning

Thanks to the identifiability result, we now present two different practical implementations to recover the latent variables and their causal relations from observations from multiple domains. We build our method on the variational autoencoder (VAE) framework and can be easily extended to other models, such as normalizing flows.

We learn a deep latent generative model (decoder)
p(X|Z; θ u) and a variational approximation (encoder)
q(Z|*X, u*) of its true posterior p(Z|X; θ u) since the true posterior is usually intractable. To learn the model, we minimize the lower bound of the log-likelihood as

$$\log p(X;\theta^{u})=\log\int p(X|Z;\theta^{u})p(Z;\theta^{u})dZ\tag{6}$$ $$=\log\int\frac{q(Z|X,u)}{q(Z|X,u)}p(X|Z;\theta^{u})p(Z;\theta^{u})dZ$$ $$\geq-\mbox{KL}(q(Z|X,u)||p(Z;\theta^{u}))+\mathbb{E}_{q}[\log p(X|Z;\theta^{u})]$$ $$=-\mathcal{L}_{ELBO}$$

For the posterior q(Z|*X, u*), we assume that it is a multivariate Gaussian or a Laplacian distribution, where the mean and variance are generated by the neural network encoder.

As for q(X|Z), we assume that it is a multivariate Gaussian and the mean is the output of the decoder and the variance is a pre-defined value.

In practice, we can parameterize p(X|Z; θ u) as the decoder which takes as input the latent representation Z and q(Z|*X, u*) as an encoder which outputs the mean and scale of the posterior distribution. An essential difference from VAE (Kingma & Welling, 2013) and iVAE (Khemakhem et al., 2020a) is that our method allow the components of Z
to be causally dependent and we are able to learn the components and causal relationships. And the key is the prior distribution P(Z; θ u). Now we present two different implementations to capture the changes with a properly defined prior distribution.

## 4.1. Nonparametric Implementation Of The Prior Distribution

To recover the relationships and latent variables Z, we build the normalizing flow to mimic the inverse of the latent SEM
Zi = fi(PA(Zi), ϵi) in Eq. (1). We first assume a causal ordering as Zˆ1*, . . . ,Z*ˆn. Then, for each component Zˆi, we consider the previous components {Zˆ1*, . . . ,Z*ˆi−1} as potential parents of Zˆi and we can select the true parents with the adjacency matrix Aˆ, where Aˆi,j denotes that component Zˆj contributes in the generation of Zˆi. If Aˆi,j = 0, it means that Zˆj will not contribute to the generation of Zˆi.

Since θ u governs the changes across domain, we use the observed domain index u to discover the changes. Then, we use the selected parents {Aˆi,1Zˆ1, . . . , Aˆi,i−1Zˆi−1} and the domain label u to generate parameters of normalizing flow and apply the flow transformation on Zˆito turn it into ϵˆi.

Specifically, we have

$${\hat{\epsilon}}_{i},\log\operatorname*{det}_{i}=\operatorname{Flow}({\hat{Z}}_{i};\operatorname{NN}(\{{\hat{A}}_{i,j}{\hat{Z}}_{j}\}_{j=1}^{i-1},u)),$$
$$\left(7\right)$$
j=1, u)), (7)
where log detiis the log determinant of the conditional flow transformation on Zˆi.

To compute the prior distribution, we make an assumption on the noise term ϵ that it follows an independent prior distribution p(ϵ), such as a standard isotropic Gaussian or a Laplacian. Then according to the change of variable formula, the prior distribution of the dependent latents can be written as

$$\log p(\hat{Z};\theta^{u})=\sum_{i=1}^{n}(\log p(\hat{\epsilon}_{i})+\log\operatorname*{det}_{i}).\qquad\mathrm{(8)}$$

Intuitively, to minimize the KL divergence loss between p(Z; θ u) and q(Z|*X, u*), the network has to learn the correct structure and the underlying latent variables; otherwise, it can be difficult to transform the dependent latent variables Zˆ to a factorized prior distribution, e.g., N (0, I).

## 4.2. Parametric Implementation Of The Prior Distribution

We can make parametric assumption on the latent causal process and facilitate the learning of true causal structure and components. Here, we consider the linear SEM and more complex SEMs can be generalized. Specifically, we assume that the true generation process of the latent Z is linear and only consists of scaling and shifting mechanisms:

$$Z=A(C^{(u)}Z)+S^{(u)}\epsilon+B^{(u)},$$
$$\mathbf{j}_{i}$$

where A ∈ [0, 1]n×nis a causal adjacency matrix which can be permuted to be strictly lower-triangular, C
(u) ∈ R
n×n and S
(u) ∈ R
n×1are underlying domain-specific scaling matrix and vector for domain u, respectively, B(u) ∈ R
n×1 is the underlying domain-specific shift vector, and ϵ is the independent noise.

To estimate the latent variables Z, the causal structure A, and capture the changes across domains, we introduce the learnable scaling Cˆ ∈ R
n×n, Sˆ ∈ R
n×1and bias parameters Bˆ ∈ R
n×1and pre-define a causal ordering as Zˆ1,Zˆ2*, . . . ,Z*ˆn. Then we have the matrix form as

$$\hat{\epsilon}=(\hat{Z}-\hat{B}^{(u)}-\hat{A}\hat{C}^{(u)}\hat{Z})/\hat{S}^{(u)}.$$
7
Given a prior distribution of the noise term p(ˆϵ), and according to the change of variable rule, we have the prior distribution for Zˆ in parametric case as

$$\log p(\hat{Z};\theta^{u})=\sum_{i=1}^{n}(\log p(\hat{\epsilon}_{i})-\log|\hat{S}_{i}^{(u)}|),$$

since the determinant of the strict lower triangular matrix Cˆ
is 0.

## 4.3. Full Objective

After we have properly defined the needed distributions p(X|Z; θ u), q(Z|*X, u*), p(Z; θ u), we can train our model to minimize the loss function L*ELBO*. However, without any further constraint, the powerful network may choose to use the fully connected causal graph during training. In other words, all lower-triangular elements of the estimated graph Aˆ is non-zero, which implies that each component Zˆiis caused by all previous i − 1 components. To exclude such unwanted solutions and encourage the model to learn the true causal structure among components of Z, we apply the ℓ1 regularization on Aˆ, i.e.,

$${\mathcal{L}}_{s p a r s i t y}=\|{\hat{A}}\|_{1}.$$
L*sparsity* = ∥Aˆ∥1. (12)
It is worth noting that the sparsity regularization term above is an approximation of the sparsity constraint on the edges of the estimated Markov network specified in Thms. 3.2 and 3.4, since it is not straightforward to impose the latter constraint in a differentiable end-to-end training process.

Finally, the full training objective is

$${\mathcal{L}}_{f u l l}={\mathcal{L}}_{E L B O}+{\mathcal{L}}_{s p a r s i t y}.$$

After the model converges, the output of the encoder Zˆ is our recovered latents from the observations in multiple domains and the revealed causal structure is in Aˆ which encapsulates the causal relationships across the components.

## 4.4. Simulations

To verify our theory and the proposed implementations, we run experiments on the simulated data because the ground truth causal adjacency matrix and the latent variables across domains are available for simulated data. Consequently, we consider following common causal structures (i) Y-structure with 4 variables, Z1 → Z3 ← Z2, Z3 → Z4 and (ii) chain structure Z1 → Z2 → Z3 → Z4. The noises are modulated with scaling random sampled from Unif[0.5, 2] and shifts are sampled from Unif[−2, 2]. The scaling on the Z are also randomly sampled from Unif[0.5, 2]. In other words, the changes are modular. After generating Z, we feed the latent variables into MLP with orthogonal weights and LeakyReLU activations for invertibility. Specifically, we sample orthogonal matrix as the weights of the MLP layers. Since orthogonal matrix and LeakyReLU are invertible, the MLP function is also invertible.

$$(10)^{\frac{1}{2}}$$
$$(11)$$

We present the results in Fig. 3 and 4. Each sub-figure consist of 4 × 4 panels and penal on i-th row and j − thcolumn denotes the relationship between the estimated component Zˆi with the true latent Zj . We can see that under most cases, our model learns a strong one-to-one correspondence from the estimated components and the true components. For instance, the first column in Fig. 3 show that Zˆ1 is strongly correlated with the true components Z1 while it is nearly independent from the true Z2.

From the estimated Aˆ, we find that our method is able to recover the true causal structure. For instance, on the Y
structure with Z1 → Z3 ← Z2 and Z3 → Z4, our estimated model only keep the components Aˆ1,3, Aˆ2,3, Aˆ3,4 nonzero with the proposed sparsity regularization. The estimated causal graph is consistent with the true Y -structure causal graph. We can also see that the latent causal structure is also recovered from Fig. 4 and 3. We observe that the learned Zˆ1 is strongly correlated with the true Z2 and is independent from the true Z1, but correlated with the Zˆ3 and Zˆ4. These results aligns well with the true causal graph since Z2 is independent from Z1 while is the cause of Z3 and Z4.

The experiments support our theoretical result that the components and structure are identifiable up to certain indeterminacies. As for the results in Fig. 3, we observe that our non-parametric method is still able to recover the true latent variables with Laplace noise.

$$(13)$$

## 5. Related Work

Causal representation learning aims to unearth causal latent variables and their relations from observed data. Despite its significance, the identifiability of the hidden generating process is known to be impossible without additional constraints, especially with only observational data. In the linear, non-Gaussian case, Silva et al. (2006) recover the Markov equivalence class, provided that each observed variable has a unique latent causal parent; Xie et al. (2020);
Cai et al. (2019) estimate the latent variables and their relations assuming at least twice measured variables as latent



Figure 3: Recovered latent variables v.s. the true latent variables with Non-Parametric Approach. (a) Y-structure with



Laplace noise. (b) Y-structure with Gaussian noise. (c) Chain structure with Laplace noise. (d) Chain structure with Gaussian noise. In each sub-figure, i-th row and j-th column depcits the relationship between the estimated Zˆi and the true components Zj .

ones, which has been further extended to learn the latent hierarchical structure (Xie et al., 2022). Moreover, Adams et al. (2021) provide theoretical results on the graphical conditions for identification. In the linear, Gaussian case, Huang et al. (2022) leverage rank deficiency of the observed sub-covariance matrix to estimate the latent hierarchical structure, while Dong et al. (2023) further extend the rank constraint to accommodate flexibly related latent and observed variables. In the discrete case, Kivva et al. (2021)
identify the hidden causal graph up to Markov equivalence by assuming a mixture model where the observed children sets of any pair of latent variables are different.

Given the challenge of identifiability on purely observational data, a different line of research leverage experiments by assuming the accessibility of various types of interventional data. Based on the single-node perfect intervention, Squires et al. (2023) leverage single-node interventions for the identifiability of linear causal model and linear mixing function;
(Varici et al., 2023) incorporate for nonlinear causal model and linear mixing function; (Varici et al., 2023; Buchholz et al., 2023; Jiang & Aragam, 2023) provide the identifiability of the nonparametric causal model and linear mixing function; (Ahuja et al., 2023) further generalize the result to nonparametric causal model and polynomial mixing functions with additional constraints on the latent support; and
(Brehmer et al., 2022; von Kugelgen et al. ¨ , 2023; Jiang &
Aragam, 2023) explore the nonparametric settings for both the causal model and mixing function. In addition to the single-node perfect interventions, Brehmer et al. (2022) introduced counterfactual pre- and post-intervention views; von Kugelgen et al. ¨ (2023) assume two distinct, paired interventions per node for multivariate causal models; Zhang et al. (2023) explore soft interventions on polynomial mixing functions; and Jiang & Aragam (2023) places specific structural restrictions on the latent causal graph.

Our study lies in the line of leveraging only observational data, and provides identifiability results in the general nonparametric settings on *both* the latent causal model and mixing function. Unlike prior works with observational data, we do not have any parametric assumptions or graphical restrictions; Compared to those relying on interventional data, our results naturally benefit from the heterogeneity of observational data (e.g., multi-domain data, nonstationary time series) and avoid additional experiments for interventions.

## 6. Conclusion And Discussions

We establish a set of new identifiability results to reveal hidden causal variables and latent structures in the general nonparametric settings. Specifically, with sparsity regularization during estimation and sufficient changes in the causal influences, we demonstrate that the revealed hidden variables and structures are related to the underlying causal model in a specific, nontrivial way. In contrast to recent works on the recovery of hidden causal variables and structures, our results rely on purely observational data without graphical or parametric constraints. Our results offer insight into unveiling the latent causal process in one of the most universal settings. Experiments in various settings have been conducted to validate the theory. As future work, we will explore the scenario where only a subset of the causal relations change, which could be a challenge as well as a chance, and show up to what extent the underlying causal variables can be recovered with potentially weaker assumptions.

## Acknowledgements

This project is partially supported by NSF Grant 2229881, the National Institutes of Health (NIH) under Contract R01HL159805, and grants from Apple Inc., KDDI Research Inc., Quris AI, and Infinite Brain Technology.

## References

Adams, J., Hansen, N., and Zhang, K. Identification of partially observed linear causal models: Graphical conditions for the non-gaussian and heterogeneous cases.

Advances in Neural Information Processing Systems, 34:
22822–22833, 2021.

Ahuja, K., Mahajan, D., Wang, Y., and Bengio, Y. Interventional causal representation learning. In *International* Conference on Machine Learning, pp. 372–407. PMLR,
2023.

Brehmer, J., De Haan, P., Lippe, P., and Cohen, T. S. Weakly supervised causal representation learning. Advances in Neural Information Processing Systems, 35:38319–
38331, 2022.

Buchholz, S., Besserve, M., and Scholkopf, B. Function ¨
classes for identifiable nonlinear independent component analysis. *arXiv preprint arXiv:2208.06406*, 2022.

Buchholz, S., Rajendran, G., Rosenfeld, E., Aragam, B.,
Scholkopf, B., and Ravikumar, P. Learning linear causal ¨
representations from interventions under general nonlinear mixing. *arXiv preprint arXiv:2306.02235*, 2023.

Cai, R., Xie, F., Glymour, C., Hao, Z., and Zhang, K. Triad constraints for learning causal structure of latent variables.

Advances in neural information processing systems, 32, 2019.
Comon, P. Independent component analysis - a new concept? *Signal Processing*, 36:287–314, 1994.

Dong, X., Huang, B., Ng, I., Song, X., Zheng, Y., Jin, S.,
Legaspi, R., Spirtes, P., and Zhang, K. A versatile causal discovery framework to allow causally-related hidden variables. In *The Twelfth International Conference on* Learning Representations, 2023.

Halv ¨ a, H. and Hyv ¨ arinen, A. Hidden markov nonlinear ICA: ¨
Unsupervised learning from nonstationary time series. In Conference on Uncertainty in Artificial Intelligence, pp.

939–948. PMLR, 2020.

Halv ¨ a, H., Le Corff, S., Leh ¨ ericy, L., So, J., Zhu, Y., Gassiat, ´
E., and Hyvarinen, A. Disentangling identifiable features ¨
from noisy data with structured nonlinear ICA. Advances in Neural Information Processing Systems, 34, 2021.

Huang, B., Low, C. J. H., Xie, F., Glymour, C., and Zhang, K. Latent hierarchical causal structure discovery with rank constraints. *Advances in Neural Information Processing Systems*, 35:5549–5561, 2022.

Hyvarinen, A. and Morioka, H. Unsupervised feature ex- ¨
traction by time-contrastive learning and nonlinear ICA.

Advances in Neural Information Processing Systems, 29:
3765–3773, 2016.
Hyvarinen, A. and Morioka, H. Nonlinear ICA of tem- ¨
porally dependent stationary sources. In *International* Conference on Artificial Intelligence and Statistics, pp.

460–469. PMLR, 2017.

Hyvarinen, A. and Pajunen, P. Nonlinear independent com- ¨
ponent analysis: Existence and uniqueness results. *Neural* networks, 12(3):429–439, 1999.

Hyvarinen, A., Cristescu, R., and Oja, E. A fast algorithm ¨
for estimating overcomplete ICA bases for image windows. In *Proc. Int. Joint Conf. on Neural Networks*, pp.

894–899, Washington, D.C., 1999.

Hyvarinen, A., Sasaki, H., and Turner, R. Nonlinear ICA us- ¨
ing auxiliary variables and generalized contrastive learning. In International Conference on Artificial Intelligence and Statistics, pp. 859–868. PMLR, 2019.

Hyvarinen, A., Khemakhem, I., and Morioka, H. Non- ¨
linear independent component analysis for principled disentanglement in unsupervised deep learning.

Patterns, 4(10):100844, 2023. ISSN 2666-3899.

doi: https://doi.org/10.1016/j.patter.2023.100844.

URL https://www.sciencedirect.com/ science/article/pii/S2666389923002234.

Jiang, Y. and Aragam, B. Learning nonparametric latent causal graphs with unknown interventions. arXiv preprint arXiv:2306.02899, 2023.

Khemakhem, I., Kingma, D., Monti, R., and Hyvarinen, A. ¨
Variational autoencoders and nonlinear ICA: A unifying framework. In International Conference on Artificial Intelligence and Statistics, pp. 2207–2217. PMLR, 2020a.

Khemakhem, I., Monti, R., Kingma, D., and Hyvarinen, A. Ice-beem: Identifiable conditional energy-based deep models based on nonlinear ica. *Advances in Neural Information Processing Systems*, 33:12768–12778, 2020b.

Kingma, D. P. and Welling, M. Auto-encoding variational bayes. *arXiv preprint arXiv:1312.6114*, 2013.

Kivva, B., Rajendran, G., Ravikumar, P., and Aragam, B.

Learning latent causal graphs via mixture oracles. *Advances in Neural Information Processing Systems*, 34:
18087–18101, 2021.

Kong, L., Xie, S., Yao, W., Zheng, Y., Chen, G., Stojanov, P., Akinwande, V., and Zhang, K. Partial disentanglement for domain adaptation. In *International Conference on* Machine Learning, pp. 11455–11472. PMLR, 2022.

Lachapelle, S., Lopez, P. R., Sharma, Y., Everett, K., Priol, ´
R. L., Lacoste, A., and Lacoste-Julien, S. Disentanglement via mechanism sparsity regularization: A new principle for nonlinear ICA. Conference on Causal Learning and Reasoning, 2022.

Lin, J. Factorizing multivariate function classes. Advances in neural information processing systems, 10, 1997.

Loh, P.-L. and Buhlmann, P. High-dimensional learning of ¨
linear causal networks via inverse covariance estimation.

The Journal of Machine Learning Research, 15(1):3065–
3105, 2014.

Ng, I., Zheng, Y., Zhang, J., and Zhang, K. Reliable causal discovery with improved exact search and weaker assumptions. In Advances in Neural Information Processing Systems, 2021.

Pearl, J. *Causality: Models, Reasoning, and Inference*.

Cambridge University Press, Cambridge, 2000.

Ramsey, J., Zhang, J., and Spirtes, P. L. Adjacencyfaithfulness and conservative causal inference. *arXiv* preprint arXiv:1206.6843, 2012.

Scholkopf, B., Locatello, F., Bauer, S., Ke, N. R., Kalch- ¨
brenner, N., Goyal, A., and Bengio, Y. Towards causal representation learning. *Proceedings of the IEEE*, 109(5):
612–634, 2021.
Silva, R., Scheines, R., Glymour, C., and Spirtes, P. Learning the structure of linear latent variable models. Journal of Machine Learning Research, 7:191–246, 2006.

Sorrenson, P., Rother, C., and Kothe, U. Disentanglement ¨
by nonlinear ICA with general incompressible-flow networks (GIN). *arXiv preprint arXiv:2001.04872*, 2020.

Spirtes, P., Glymour, C., and Scheines, R. *Causation, Prediction, and Search*. MIT Press, Cambridge, MA, 2nd edition, 2001.

Squires, C., Seigal, A., Bhate, S. S., and Uhler, C. Linear causal disentanglement via interventions. In *International* Conference on Machine Learning, 2023.

Taleb, A. and Jutten, C. Source separation in post-nonlinear mixtures. *IEEE Transactions on signal Processing*, 47
(10):2807–2820, 1999.

Uhler, C., Raskutti, G., Buhlmann, P., and Yu, B. Geometry ¨
of the faithfulness assumption in causal inference. The Annals of Statistics, pp. 436–463, 2013.

Varici, B., Acarturk, E., Shanmugam, K., Kumar, A., and Tajer, A. Score-based causal representation learning with interventions. *arXiv preprint arXiv:2301.08230*, 2023.

von Kugelgen, J., Besserve, M., Liang, W., Gresele, L., ¨
Kekic, A., Bareinboim, E., Blei, D. M., and Sch ´ olkopf, ¨
B. Nonparametric identifiability of causal representations from unknown interventions. arXiv preprint arXiv:2306.00542, 2023.

Xie, F., Cai, R., Huang, B., Glymour, C., Hao, Z., and Zhang, K. Generalized independent noise condition for estimating latent variable causal graphs. In *Advances in* Neural Information Processing Systems, 2020.

Xie, F., Huang, B., Chen, Z., He, Y., Geng, Z., and Zhang, K. Identification of linear non-gaussian latent hierarchical structure. In International Conference on Machine Learning, pp. 24370–24387. PMLR, 2022.

Yao, W., Sun, Y., Ho, A., Sun, C., and Zhang, K. Learning temporally causal latent processes from general temporal data. *arXiv preprint arXiv:2110.05428*, 2021.

Yao, W., Chen, G., and Zhang, K. Temporally disentangled representation learning. In *Advances in Neural Information Processing Systems*, 2022.

Zhang, J. and Spirtes, P. Detection of unfaithfulness and robust causal inference. *Minds and Machines*, 18:239–
271, 2008.

Zhang, J., Greenewald, K., Squires, C., Srivastava, A., Shanmugam, K., and Uhler, C. Identifiability guarantees for causal disentanglement from soft interventions. *Advances* in Neural Information Processing Systems, 36, 2023.

Zheng, Y. and Zhang, K. Generalizing nonlinear ica beyond structural sparsity. Advances in Neural Information Processing Systems, 36:13326–13355, 2023.

Zheng, Y., Ng, I., and Zhang, K. On the identifiability of nonlinear ICA: Sparsity and beyond. In *Advances in* Neural Information Processing Systems, 2022.

Zheng, Y., Ng, I., Fan, Y., and Zhang, K. Generalized precision matrix for scalable estimation of nonparametric markov networks. *arXiv preprint arXiv:2305.11379*,
2023.

## A. Proof Of Theorem 3.1

Theorem 3.1. Let the observations be sampled from the data generating process in Eq. (1), and MZ be the Markov network over Z*. Suppose that the following assumptions hold:*

- *A1 (Smooth and positive density): The probability density function of latent causal variables is smooth and positive, i.e.*
pZ is smooth and pZ > 0 *over* R
n.

- *A2 (Sufficient changes): For any* Z ∈ R
n*, there exist* 2n + |MZ| + 1 values of θ*, i.e.,* θ
(u) *with* u = 0*, . . . ,* 2n + |MZ|, such that the vectors w(Z, u) − w(z, 0) *with* u = 1, . . . , 2n + |MZ| are linearly independent, where vector w(*Z, u*)
is defined as

$$w(Z,u)=\left(\frac{\partial\log p(Z;\theta^{(u)})}{\partial Z_{1}},\ldots,\frac{\partial\log p(Z;\theta^{(u)})}{\partial Z_{n}},\right.$$ $$\left.\frac{\partial^{2}\log p(Z;\theta^{(u)})}{\partial Z_{1}^{2}},\ldots,\frac{\partial^{2}\log p(Z;\theta^{(u)})}{\partial Z_{n}^{2}}\right)$$ $$\left.\frac{\partial^{2}\log p(Z;\theta^{(u)})}{\partial Z_{i}\partial Z_{j}}\right)_{(i,j)\in\mathcal{E}(\mathcal{M}_{Z})}.$$

Suppose that we learn (ˆg, ˆf, pZˆ) to achieve Eq. (2). Then, for every pair of estimated hidden variables Zˆk and Zˆl*that are* not adjacent in the Markov network MZˆ over Zˆ*, we have the following statements:*
(a) Each true hidden causal variable Ziis a function of at most one of Zˆk and Zˆl.

(b) For each pair of true hidden causal variables Zi and Zj that are adjacent in the Markov network MZ over Z, at most one of them is a function of Zˆk or Zˆl.

Proof. Since h in Zˆ = h(Z) is invertible, we have

$$p(Z;\theta)-\log|J_{h}|.$$

p(Zˆ; θ) = p(Z; θ)/|Jh|, log p(Zˆ; θ) = log p(Z; θ) − log |Jh|. (14)
Suppose Zˆk and Zˆl are conditionally independent given Zˆ[n]\{k,l} i.e., they are not adjacent in the Markov network over Zˆ.

For each θ, by Lin (1997), we have

$$\frac{\partial^{2}\log p(\hat{Z};\theta)}{\partial\hat{Z}_{k}\partial\hat{Z}_{l}}=0.$$

To see what it implies, we find the first-order derivative:

$$\frac{\partial\log p(\hat{Z};\theta)}{\partial\hat{Z}_{k}}=\sum_{i}\frac{\partial\log p(Z;\theta)}{\partial Z_{i}}\frac{\partial Z_{i}}{\partial\hat{Z}_{k}}-\frac{\partial\log|J_{q}|}{\partial\hat{Z}_{k}}.$$

Let η(θ) = log p(Z; θ), η ′ i (θ) = ∂ log p(Z;θ) ∂Zi, η ′′ ij (θ) = ∂ 2log p(Z;θ) ∂Zi∂Zj, h ′ i,l = ∂Zi ∂Zˆl , and h ′′ i,kl =∂ 2Zi ∂Zˆk∂Zˆl . We then derive the
second-order derivative:

∂ 2log p(Z; θ) ∂Zi∂Zj ∂Zj ∂Zˆl ∂Zi ∂Zˆk + X i ∂ log p(Z; θ) ∂Zi ∂ 2Zi ∂Zˆk∂Zˆl − ∂ 2log |Jq| ∂Zˆk∂Zˆl . 0 =X j X i ∂ 2log p(Z; θ) ∂Z2 i ∂Zi ∂Zˆl ∂Zi ∂Zˆk + X j X (j,i)∈E(MZ ) ∂ 2log p(Z; θ) ∂Zi∂Zj ∂Zj ∂Zˆl ∂Zi ∂Zˆk = X i ∂ log p(Z; θ) ∂Zi ∂ 2Zi ∂Zˆk∂Zˆl − ∂ 2log |Jq| ∂Zˆk∂Zˆl + X i i η ′′ ii(θ)h ′ i,lh ′ i,k + X j X (j,i)∈E(MZ ) η ′′ ij (θ)h ′ j,lh ′ i,k + X i η ′ i (θ)h ′′ i,kl − ∂ 2log |Jq| ∂Zˆk∂Zˆl . (15) = X
Here we denote by E(MZ) the set of edges in the Markov network over Z and we already make use of the fact that if Zi and Zj are not adjacent in the Markov network, then ∂
2log p(Z;θ)
∂Zi∂Zj= 0.

By Assumption A2, consider the 2n + |MZ| + 1 values of θ, i.e., θ
(u) with u = 0*, . . . ,* 2n + |MZ|, such that Eq. (15) hold.

Then, we have 2n + |MZ| + 1 such equations. Subtracting each equation corresponding to θ
(u), u = 1*, . . . ,* 2n + |MZ| with the equation corresponding to θ
(0) resuls in 2n + |MZ| equations:

$$\begin{array}{l l}{{0=\sum_{i}(\eta_{i i i}^{\prime\prime}(\theta^{(u)})-\eta_{i i i}^{\prime\prime}(\theta^{(0)}))h_{i,i}^{\prime}h_{i,k}^{\prime}+\sum_{j}\sum_{(j,i)\in{\mathcal{E}}({\mathcal{M}}_{Z})}(\eta_{i j}^{\prime\prime}(\theta^{(u)})-\eta_{i j}^{\prime\prime}(\theta^{(0)}))h_{j,i}^{\prime}h_{i,k}^{\prime}}}\\ {{}}&{{+\sum_{i}(\eta_{i}^{\prime}(\theta^{(u)})-\eta_{i}^{\prime}(\theta^{(0)}))h_{i,k l}^{\prime\prime},}}\end{array}$$

where u = 1*, . . . ,* 2n + |MZ|. By Assumption A2, the vectors formed by collecting the corresponding coefficients are linearly independent. Therefore, for any i and any j such that (j, i) ∈ E(MZ), we have

$h^{\prime}_{i,h}h^{\prime}_{i,k}=0$,  $h^{\prime}_{j,h}h^{\prime}_{i,k}=0$,  $h^{\prime\prime}_{i,kl}=0$.  
 $\left(16\right)$  $\left(17\right)$  $\left(18\right)$
Eq. (16) indicates that Ziis a function of at most one of Zˆk and Zˆl, while Eq. (17) implies that given that Zi and Zj are adjacent in Markov network MZ, at most one of them is a function of Zˆk or Zˆl.

## B. Proof Of Theorem 3.2

First, we introduce the following lemma, which will be used in the proof.

Lemma 2. For any invertible matrix A, there exists a permutation of its row such that the diagonal entries of the resulting matrix are nonzero.

Proof. Suppose by contradiction that there exists at least a zero diagonal entry for every row permutation. By Leibniz formula, we have

$$\operatorname*{det}(A)=\sum_{\sigma\in S_{n}}\left(\operatorname{sgn}(\sigma)\prod_{i=1}^{n}a_{\sigma(i),i}\right),$$

where Sn denotes the set of n-permutations. Since there exists a zero diagonal entry for every permutation, we have

$$\prod_{i=1}^{n}a_{\sigma(i),i}=0,\quad\forall\sigma\in{\mathcal{S}}_{n},$$

which implies det(A) = 0 and that matrix A is not invertible. This is a contradiciton with the assumption that A is invertible.

Theorem 3.2 (Identifiability of Latent Markov Network). Let the observations be sampled from the data generating process in Eq. (1), and MZ be the Markov network over Z*. Suppose that Assumptions A1 and A2 from Theorem 1 hold. Suppose* also that we learn (ˆg, ˆf, pZˆ) to achieve Eq. (2) with the minimal number of edges of Markov network MZˆ over Zˆ. Then, the Markov network MZˆ over estimated hidden variables Zˆ is isomorphic to the true latent Markov network MZ.

Proof. Based on Lemma 2, there exists a permutation π of the estimated hidden variables, denoted as Zˆπ, such that

$$\frac{\partial Z_{i}}{\partial\hat{Z}_{\pi(i)}}\neq0,\quad i=1,\ldots,n.$$
̸= 0, i = 1*, . . . , n.* (19)
Suppose that Zi and Zj are adjacent in the Markov network MZ over Z, but Z˜π(i) and Z˜π(i) are not adjacent in the Markov network MZˆ over Zˆ. By Theorem 3.1, at most one of Zi and Zj is a function of Z˜π(i) and Z˜π(i). This is clearly a contradiction with Eq. (19).

$$(19)$$

Therefore, we have shown by contradiction that, if Zi and Zj are adjacent in the Markov network MZ over Z, then Z˜π(i)
and Z˜π(i) are adjacent in the Markov network MZˆπ over variables Zˆπ. That is, all edges in MZ must be present in Markov network MZˆπ over variables Zˆπ. Also, note that the true model (*g, f, p*Z) is clearly one of the solutions that achieves Eq.

(2). Thus, under sparsity constraint on the edges of MZˆ, we conclude that the Markov network MZˆπ over Zˆπ must be identical to the Markov network MZ over Z,

## C. Proof Of Corollary 3.3

Suppose by contradiction that (ˆg, ˆ*f, p*Zˆ) achieves Eq. (2). By assumption, the components of Zˆ are independent in each domain, indicating that the Markov network MZˆ is an empty graph. By similar reasoning in the proof of Theorem 3.2, all edges in the true Markov network MZ must be present in MZˆ (up to isomorphism). Since MZˆ is an empty graph, this implies that MZ is also an empty graph, which is contradictory with the assumption that MZ is not an empty graph.

## D. Proof Of Theorem 3.4

We first state the following lemma that is used to prove Statement (b) of Theorem 3.4. The proof is a straightforward consequence of Cayley–Hamilton theorem and is omitted here.

Lemma 3. Let A be an n × n invertible matrix. Then, it can be expressed as a linear combination of the powers of A*, i.e.,*

$$A^{-1}=\sum_{k=0}^{n-1}c_{k}A^{k}$$

for some appropriate choice of coefficients c0, c1*, . . . , c*n−1.

Now consider the Markov network MZ over hidden causal variables Z. Let NZi be the set of neighbors of Ziin MZ. We provide the following result that relates a matrix to its inverse, given that such matrix satisfies certain property defined by MZ.

Proposition 1. Consider a Markov network MZ over Z*. Let* NZi be the set of neighbors of Ziin MZ, and A *be an* n × n invertible matrix. For each i ̸= j where Zj is not adjacent to some nodes in {Zi} ∪ NZi
, suppose Aij = 0*. Then, we have* A
−1 ij = 0.

Proof. By Lemma 3, A−1can be expressed as linear combination of the powers of A. Therefore, it suffices to prove that, each matrix power Aksatisfies the following property: Ak ij = 0 for each i ̸= j where Zj is not adjacent to some nodes in
{Zi} ∪ NZi
. We proceed with mathematical induction on k. By definition, the property holds in the base case where k = 1.

Now suppose that the property holds for Ak. We prove by contradiction that the property holds for Ak+1. Suppose by contradiction that A
k+1 ij ̸= 0 for some i ̸= j where Zj is not adjacent to some nodes in {Zi} ∪ NZi
. This implies that one of the following cases holds:
- Case (a): Zj is not adjacent to Ziin MGZ
.

- Case (b): There exists Zl ∈ NZi
\ {Zj} such that Zj and Zl are not adjacent in MGZ
.
Since A
k+1 ij =Pn r=0 Ak irArj , the assumption A
k+1 ij ̸= 0 implies that there must exist m such that Ak imAmj ̸= 0, i.e.,
Ak im ̸= 0 and Amj ̸= 0. Since both Akand A satisfy the property, this indicates (i) Zm is adjacent to Zi and all nodes in NZi \ {Zm}, and (ii) Zj is adjacent to Zm and all nodes in NZm \ {Zj}. We consider the following cases:

- Case of m = l: By (ii), Zj is adjacent to Zl, which contradicts Case (b) above. Also, we know that Zlis adjacent to Zi by (i), which indicates that Ziis adjacent to Zj , contradicting Case (a) above.

- Case of m ̸= l: By (i) and (ii), Zm is adjacent to Zi and Zj is adjacent to Zm, implying that Zi and Zj are adjacent, which is contradictory with Case (a) above. Furthermore, since Zlis a neighbor of Zi, we know that Zm and Zl are adjacent by (i). Also, by (ii), Zj is adjacent to Zl, which contradicts Case (b) above.
In either of the cases above, there is a contradiction.

We are now ready to give the following result.

Theorem 3.4 (Identifiability of Hidden Causal Variables). Let the observations be sampled from the data generating process in Eq. (1), and MZ be the Markov network over Z. Let NZi be the set of neighbors of variable Ziin MZ*. Suppose that* Assumptions A1 and A2 from Theorem 1 hold. Suppose also that we learn (ˆg, ˆf, pZˆ) to achieve Eq. (2) with the minimal number of edges of Markov network MZˆ over Zˆ. Then, there exists a permutation π *of the estimated hidden variables,*
denoted as Zˆπ, such that each Zˆπ(i)is a function of (a subset of) the variables in {Zi} ∪ ΨZi
.

Proof. We first prove a simpler case: there exists a permutation π of the estimated hidden variables, denoted as Zˆπ, such that Ziis a function of Zˆπ(i) and a subset of the variables in {Zˆπ(j)|Zj is adjacent to Zi and all other neighbors of Ziin MZ}.

By Theorem 3.2 and its proof, there exists a permutation π of the estimated variables, denoted as Zˆπ, such that the Markov network MZˆπ over Zˆπ is identical to MZ, and that

$$\frac{\partial Z_{i}}{\partial\hat{Z}_{\pi(i)}}\neq0,\quad i=1,\ldots,n.$$

Clearly, each variable Ziis a function of Zˆπ(i).

We first show that if Zj is not adjacent to Ziin MZ, then Zi cannot be a function of Zˆπ(j). Since Zi and Zj are not adjacent in MZ, we know that Zˆπ(i) and Zˆπ(j) are not adjacent in MZˆπ
. By Theorem 3.1, Ziis a function of at most one of Zˆπ(i)
and Zˆπ(j), which implies that Zi cannot be a function of Zˆπ(j), because we have shown that Ziis a function of Zˆπ(i).

To refine further, now suppose that Zj is adjacent to Zi, but not adjacent to some Zk ∈ NZi
\ {Zj}. Since MZ and MZˆπ are identical, Zˆπ(j)is also not adjacent to Zˆπ(k)in MZˆπ
. Since Zi and Zk are adjacent in MZ, by Theorem 3.1, at most one of them is a function of Zˆπ(j) or Zˆπ(k). This implies that Zi cannot be a function of Zˆπ(j), because we have shown that Zk is a function of Zˆπ(k).

Therefore, we have just shown that Ziis a function of at most the variables in Zˆπ(i) ∪ {Zˆπ(j)|Zj is adjacent to Zi and all other neighbors of Ziin MZ}.

Now for each k ̸= i where Ziis not adjacent to some nodes in {Zk} ∪ NZk
, we have

∂Zk
∂Zˆπ(i)
$${\underline{{{\underline{{k}}}}}}=0.$$
which, by inverse function theorem, implies.  
By Proposition $1$, we have . 



$$\left({\frac{\partial Z}{\partial{\hat{Z}}_{\pi}}}\right)_{k}$$
ki

$$\frac{\partial\hat{Z}_{\pi(i)}}{\partial Z_{k}}=\left(\frac{\partial Z}{\partial\hat{Z}_{\pi}}\right)_{k i}^{-1}=0.$$
$$\square$$

This implies that Zˆπ(i) cannot be a function of Zk.

## E. Proof Of Lemma 1 And Theorem 3.5

Lemma 1. Given a latent causal graph GZ and distribution PZ with its Markov Network MZ*, under Markov assumption,*
the undirected graph defined by MZ *is a subgraph of the moralized graph of the true causal DAG* G.

Proof. Let Zj and Zk, j ̸= k be two variables that i and j are not adjacent in the moralized graph of GZ. Then it suffices to show that (j, k) ∈ E / (MZ) and (k, j) ∈ E / (MZ). Because they are not adjacent in the moralized graph of GZ, they must not be adjacent in GZ and must not share a common child in GZ. Thus, j and k are d-separated conditioning on V \ {*j, k*},
which implies the conditional independence Zj ⊥⊥ Zk|Z \ {Zj , Zk} based on the Markov assumption on {GZ, PZ}. Then we have (j, k) ∈ E / (MZ) and (k, j) ∈ E / (MZ).

Theorem 3.5. Given a causal DAG GZ and distribution PZ with its Markov Network MZ*, under Markov assumption,*
the undirected graph defined by MZ is the moralized graph of the true causal DAG GZ *if and only if the SAF and SUCF*
assumptions are satisfied.

Proof. We prove both directions as follows.

Sufficient condition. We prove it by contradiction. Suppose that the structure defined by supp(MZ) is not equivalent to the moralized graph of GZ. Then, according to Lem. 1, there exists a pair of variables Zj and Zk, j ̸= k that i and j are adjacent in the moralized graph but (j, k) ∈ E / (MZ) and (k, j) ∈ E / (MZ). Thus, we have Zj ⊥⊥ Zk|Z \ {Zj , Zk}. Then we consider the following two cases:

- If variables Zj and Zk correspond to a pair of neighbors in GZ, then they are adjacent. Together with the conditional independence relation Zj ⊥⊥ Zk|Z \ {Zj , Zk}, this implies that the SAF assumption is violated.

- If variables Zj and Zk correspond to a pair of non-adjacent spouses in GZ. Then they have an unshielded collider, indicating that the SUCF assumption is violated.
Necessary condition. We prove it by contradiction. Suppose SUCF or SAF is violated, we have the following two cases:

- Suppose SUCF is violated, i.e., there exists an unshielded collider j → i ← k in the DAG GZ such that Zj ⊥⊥
Zk|Z \ {Zj , Zk}. This conditional independence relation indicates that (j, k) ∈ E / (MZ) and (k, j) ∈ E / (MZ). Since j and k are spouses, there exists an edge between them in the moralized graph of GZ, but is not contained in the structure defined by MZ, showing that they are not the same.

- Or, suppose SAF is violated, i.e., there exists a pair of neighbors j and k in the DAG GZ such that Zj ⊥⊥ Zk|Z\{Zj , Zk}.

This conditional independence relation indicates that (j, k) ∈ E / (MZ) and (k, j) ∈ E / (MZ). Because j and k are adjacent in GZ, clearly they are also adjacent in the moralized graph of GZ. However, the edge between them is not contained in the structure defined by MZ, showing that they are not the same.
Thus, when SUCF or SAF is violated, the structure defined by MZ is the moralized graph of the true DAG GZ.