# From Naive Trees To Random Forests: A General Approach For Proofing Consistency Of Tree-Based Methods

Nico Föge Department of Mathematics Otto-von-Guericke Universität Magdeburg nico.foege@ovgu.de

| Department of Statistics TU Dortmund University   |
|---------------------------------------------------|
| markus.pauly@tu-dortmund.de                       |

Lena Schmid Department of Statistics TU Dortmund University lena.@tu-dortmund.de Marc Ditzhaus Department of Mathematics Otto-von-Guericke Universität Magdeburg marc.ditzhaus@ovgu.de April 11, 2024

## A**Bstract**

Tree-based methods such as Random Forests are learning algorithms that have become an integral part of the statistical toolbox. The last decade has shed some light on theoretical properties such as their consistency for regression tasks. However, the usual proofs assume normal error terms as well as an additive regression function and are rather technical. We overcome these issues by introducing a simple and catchy technique for proofing consistency under quite general assumptions. To this end, we introduce a new class of naive trees, which do the subspacing completely at random and independent of the data. We then give a direct proof of their consistency. Using them to bound the error of more complex tree-based approaches such as univariate and multivariate CARTs, Extra Randomized Trees, or Random Forests, we deduce the consistency of all of them. Since naive trees appear to be too simple for actual application, we further analyze their finite sample properties in a simulation and small benchmark study. We find a slow convergence speed and a rather poor predictive performance. Based on these results, we finally discuss to what extent consistency proofs help to justify the application of complex learning algorithms.

## 1 Introduction

Due to their capacity to handle complex relationships while also offering possibilities for interpretability [19, 27], treebased learning algorithms, especially Random Forests [7], are among the most popular machine learning approaches.

Their possible applications include predictive tasks [44], variable selection [20, 36], uncertainty quantification [9, 26, 34],
imputation [35, 41] as well as inference [24, 44]. Moreover, they are still one of the state-of-the-art approaches for tabular data despite the ubiquity of deep learning approaches [17]. Thus, there is a lot of empirical evidence for the good performance of Random Forests and other tree-based learners. We nevertheless don't know enough about the underlying mathematical reasons, despite several theoretical investigations from the last ten to fifteen years. Here, several papers focused on the mathematical study of the consistency of Random Forests. This started with the seminal paper by [3] who were the first to prove consistency for the Random Forest, though for a simplified version. The work was continued by [14] and [2] until [40] finally provided a consistency proof for the original regression estimator introduced by [7]. The paper quickly gained scientific recognition and is one of the most cited Annals of Statistics papers of the last decade. The stated result is valid for the class of additive models with normally distributed errors

$$(1)$$
$$Y=\sum_{j=1}^{p}m_{j}\left(X^{(j)}\right)+\varepsilon,$$
´

¯

` ε, (1)
$\vdash\star$ 3. 
2
where Y P R is the univariate output variable, X " pXp1q*, . . . , X*ppqq J is uniformly distributed on r0, 1s p, ε is an independent centered Gaussian error with finite variance and each additive regression function mj is assumed to be continuous. The consistency results were later extended from the i.i.d. setting to dependent [16] and spatial-dependent data [37] as well as settings with missing observations [18], still assuming Gaussianity and an additive regression function. The result from [40] was also used to construct valid prediction intervals [33] or to prove consistency of residual variance estimators [25, 35] and of certain variable importance measures [36, 39]. More recently, the preprint [5] studied consistency of tree-based methods by means of a new probabilistic impurity decrease condition. This way, they were able to prove consistency of tree-based ensembles such as Extremely Randomized Trees [15, ExtraTrees] under technical but quite general assumptions. However, the classical Random Forest was not covered. Another line of research focused on generalized Random Forests [1] fulfilling the honesty condition [42]. The corresponding regressions estimators were also shown to be consistent and even asymptotically normal [1, 42]. Moreover, [10] even established rates of consistency for the Random Forest [7] based on the CART (Classification And Rregression Tree)
algorithm of [8]. While there are various theoretical results for the univariate Random Forest and other tree-based learners, the imposed conditions for consistency are often technical and quite strong. Moreover, there is a lack of mathematical theory for multivariate extensions [38]. In the present paper we therefore propose 1. a simple proof technique for the consistency of general univariate and multivariate tree-based regression learner that 2. neither requires Gaussianity of error terms nor an additive regression function.

To this end, we construct a naive tree, which does the splitting of the feature space independent of the data and completely at random and prove its L
2-consistency. We then compare the quadratic error of the naive tree and other existing trees, such as CART within the Random Forest, from which we deduce the consistency of the respective tree and the corresponding ensemble-learner. The technique is straightforward and also applicable for multivariate trees and ensembles thereof. Unlike [12], who created completely random decision trees to maximize the diversity of the trees in a forest, our naive tree does not show good finite sample performance and is only a theoretical tool to show the consistency of more accurate methods.

The rest of the present paper is organized as follows. In Section 2 we introduce our general statistical model and the assumptions. Moreover, we define the naive tree, which splits the feature space independent of the data. Our main asymptotic results are given in Section 3. We derive consistency of the naive tree from which we deduce consistency of the uni- and multivariate ExtraTrees or Random Forest algorithm in Section 4. To analyze the finite sample performance of the naive trees with respect to well-known approaches, we conduct a simulation (Section 5) and a small benchmark study (Section 6). The paper closes with a conclusion and outlook (Section 7). All proofs are given in the Appendix.

## 2 Mathematical Framework

We consider a regression model with a multivariate d-dimensional output variable Y "
`

Y
p1q*, . . . , Y* pdq
˘JP R
dand and error vector ε "
`

ε p1q*, . . . , ε*pdq
˘JP R
d. The output variable is linked to a uniformly distributed feature vector X " Ur0, 1s pthrough a continuous function m : r0, 1s p ÝÑ R
d, i.e.

Y " mpXq ` ε, (2)
where Erεs " 0 and Covpεq " diagpσ 2 1
, . . . , σ2 dq P R
dˆd with σj ą 0 for all j " 1*, . . . , d*. As in classical CLTs for nonparametric regression models. We only assume that ε is independent of X and possesses finite second marginal moments, i.e. E
"`

ε pjq
˘2 ı ď Kε for all j " 1*, . . . , d* and a fixed Kε ą 0. Thus, this model is a generalization of the regression model (1) utilized in [40] in three directions (error distribution, regression function, output dimensionality).

The function m can be estimated by a regression tree. To formulate this mathematically, we follow [36, 40] who describe the tree generation by a random vector Θ. At each node of the regression tree, mtry P t1*, . . . , p*u features are randomly selected. The selected features determine the direction during the feature subspacing at each node. In our situation, the training set Dn "
␣

rXJ
i
, YJ
is J P r0, 1s p ˆ R
d; i " 1*, . . . , n*(
contains independent random vectors rXJ
i
, YJ
is J that have the same distribution as rXJ, YJs J. The iid errors are denoted by ε1*, . . . , ε*n and have the same distribution as ε.

For the CART algorithm used within Random Forests, Θ can be decomposed into two subvectors Θ "
`

Θp1q, Θp2q
˘

,
where Θp1q P R
n models the bootstrap sampling mechanism prior to tree construction and Θp2q models the feature
subspacing in the tree construction [36]. To describe this step more formally, for each node the algorithm selects
mtry P t1*, . . . , p*u features from#
$$\left\{\left(\Theta_{1}^{(2)},\ldots,\Theta_{p}^{(2)}\right)\in\{0,1\}^{p}:\sum_{j=1}^{p}\Theta_{j}^{(2)}=m_{\mathrm{try}}\right\},$$
$$({\mathfrak{I}})$$
3
where Θ
p2q jdenotes whether the j-th component was selected (Θ
p2q j " 1) or not (Θ
p2q j " 0) based upon optimizing the CART-split criterion (minimizing the squared prediction error) within Random Forest. It is described in detail in Algorithm 3 in the Supplement. For the tree construction in the ExtraTrees algorithm [15], we have to re-define Θ, since there is no bootstrap of the training data and a random selection of the splits as described in Section 4 and Algorithm 2 below.

Regression trees use the training set to approximate m by a piece-wise constant function. For this purpose, the feature space is partitioned into subspaces through a tree-based procedure. We denote the number of subspaces with tn P t1*, . . . , n*u and the resulting subspaces as An,1pΘ, Dnq, . . . , An,tnpΘ, Dnq. Moreover, let Anpx, Θ, Dnq be the subspace containing x P r0, 1s p. As an estimator for m, we use a step function mn,1px, Θ, Dnq over these subsets, which heights are determined by averaging the output variable over all individuals, that fall into the same cell as x, i.e.

$$m_{n,1}(\mathbf{x},\Theta,{\mathcal{D}}_{n})=\sum_{i=1}^{n}W_{i}(\mathbf{x},\Theta,{\mathcal{D}}_{n})\mathbf{Y}_{i}.$$

Wipx, Θ, DnqYi. (3)
This covers various tree-based algorithms, that differ in the construction of the cells An,1pΘ, Dnq, . . . , An,tnpΘ, Dnq via Θ. In particular, we study CART, CART within Random Forest and the ExtraTree (i.e. a single tree used in the ExtraTrees ensemble) regression tree. For CART [8] and a single ExtraTree [15], the corresponding weights Wiin
(3) are given by Wipx, Θ, Dnq " 1tXi P Anpx, Θ, Dnqu{Nnpx, Θ, Dnq, where Nnpx, Θ, Dnq denotes the number of observations in Dn that fall into the same cell as x. For a single CART within the Random Forest, the definition slightly changes as the tree is only build based upon a subsample of Dn, see Algorithm 3 in the supplement and [4]. More general as before, we thus have to define the denominator Nnpx, Θ, Dnq as the number of observations from the subsample of Dn that fall into the same cell as x and work with the weights

$W_{i}(\mathbf{x},\boldsymbol{\Theta},\mathcal{D}_{n})=\begin{cases}\frac{1\{\mathbf{X}_{i}\in A_{n}(\mathbf{x},\boldsymbol{\Theta},\mathcal{D}_{n})\}}{N_{n}(\mathbf{x},\boldsymbol{\Theta},\mathcal{D}_{n})}&\text{if}\mathbf{X}_{i}\text{is drawn during feature selection}\\ 0&\text{else}\end{cases}$
.
Here, and throughout we use the convention 0{0 " 0 for the weights. In all three cases, we can rewrite mn,1 as the mean mn,1px, Θ, Dnq " YAnpx,Θ,Dnq, where the right-hand side denotes the mean of all output vectors Yi of the sample (subsample in case of CART within Random Forest), whose corresponding feature vector Xilies in Anpx, Θ, Dnq.

As stated above, the algorithms differ in the construction of the cells An,1pΘ, Dnq, . . . , An,tnpΘ, Dnq. To establish their consistency, and subsequently of the corresponding ensembles of Random Forest and ExtraTrees, our approach is to construct a naive tree, which partitions the feature space completely at random and independent of the data i.e. we set An,tpΘ, Dnq " An,tpΘq, t " 1*, . . . , t*n, where Θ is described in the algorithm below.

The algorithm constructs a partition An,1pΘq, . . . , An,tnpΘq, that is independent of the data and thus simplifies the theoretical handling of the tree. In the next section, we prove that even this simple approach can deliver a consistent estimator for m. Through the comparison with this naive approach, we get the consistency of more complex tree-based regression learners like CART, (single) ExtraTree and corresponding ensembles.

## 3 Consistency Of The Naive Tree

In this section, we present our main consistency result for naive trees described in Algorithm 1. We will later use this as a new tool for proving consistency for different tree-based learners. To be more flexible, we prove the results for naive trees built upon a subsample of size an P t1*, . . . , n*u as described in Algorithm 1 drawn prior to tree construction. This contains no subsampling (an " n) as special case. For consistent estimation of m, cells must become become small as n Ñ 8 to take advantage of the continuity of m.

The shrinking of the cells is guaranteed, with a growing number of splits, as we show in Lemma 1 of the Appendix.

Algorithm 1: Naive Tree Algorithm Data: The number of leaves tn P N, the size of the subsample an P t1*, . . . , n*u and the number of features during feature subsampling mtry P t1*, . . . , p*u Output: A partition of r0, 1s pand a subset of Dn Let Θ be the tree constructing random vector, and ApΘ**q " r**a1pΘq, b1pΘ**qs ˆ** *. . .* ˆ rappΘq, bppΘqs; Set nnodes " 1, level " 0 and the starting partition P0 **" tr**0, 1s pu and Plevel " H for all 1 ď level ď n; Draw and save a subsample of Dn of the size an without replacement; while n*nodes* ă tn do if P*level* " H **then**
levelÐlevel`1; else Let ApΘq be the first element of Plevel Draw a random subset Mtry Ă t1*, . . . , p*u with |Mtry| " mtry; Draw a dimension J uniformly on Mtry; Draw a cut-point zJ pΘq uniformly on raJ pΘq, bJ pΘqs; Set`

A
JpΘq
˘

L
" ra1pΘq, b1pΘ**qs ˆ** *. . .* ˆ raJ´1pΘq, bJ´1pΘ**qs ˆ r**aJ pΘq, zJ pΘqs ˆ raJ`1pΘq, bJ`1pΘ**qs ˆ** *. . .* ˆ rappΘq, bppΘqs and`

A
JpΘq
˘

R
" ra1pΘq, b1pΘ**qs ˆ** *. . .* ˆ raJ´1pΘq, bJ´1pΘqs ˆ pzJ pΘq, bJ pΘ**qs ˆ r**aJ`1pΘq, bJ`1pΘ**qs ˆ** *. . .* ˆ rappΘq, bppΘqs, where Θ contains the randomly drawn dimension J and the corresponding zJ for each split in the constructed tree; Plevel Ð PlevelztApΘqu Plevel`1 Ð Plevel`1 Y
␣`AJpΘq
˘

L
(

Y
␣`AJpΘq
˘

R
(

nnodes Ð nnodes ` 1; end end This is necessary because in the construction of the partition of the feature space, no information about the regression function m is used. With an arbitrary fine partition, a step function can approximate m on this partition. To obtain a good approximation of m with the naive tree, it is not only necessary to obtain an arbitrarily fine partition of r0, 1s p, but also that sufficiently many observations lie in the individual cells as an Ñ 8, so that the estimates for the values of m can become consistent. Therefore, the number of leaves tn and the size of the subsample drawn prior to tree construction an must be chosen in a suitable ratio. This is assumed in the following theorem to prove L
2-consistency.

Theorem 3.1. Let the feature subspacing be performed according to Algorithm *1. If* limnÑ8 tn{an " 0, then the corresponding naive tree estimator mn,1pX1, Θ, Dnq is L
2-consistent for the regression m *of Model* (2)*, i.e.*

$$\mathbb{E}\biggl[\left\|m_{n,1}(\mathbf{X}_{1},\boldsymbol{\Theta},\mathcal{D}_{n})-m(\mathbf{X}_{1})\right\|^{2}\biggr]$$
$$\frac{1}{2}$$  4. 

"
›
›

ȷ

Ñ 0
if tn Ñ 8 and an Ñ 8 as n Ñ 8.

The consistency on the training set Dn of the naive tree is sufficient to establish the consistency of other tree-based learners, because the training set becomes dense on r0, 1s pfor growing sample size n as we'll see in the next section.

## 4 Consistency Of The Extratree And Cart Algorithms And Deduced Ensembles

The naive tree from Algorithm 1 has major weaknesses, particularly if there are a lot of non-informative predictors. To be concrete, assume that there are p˜ P t1*, . . . , p*u predictors `Xp1q*, . . . ,* Xpp˜q
˘

, which are independent of Y. Therefore, on average, a portion of p˜{p of all splits would be completely without any gain of information. Thus, although Algorithm 1 leads to consistent estimation, it is strongly advised not to actually use them. We will elaborate on this in Section 5.

Nevertheless, it is a very useful tool to prove consistency of more powerful algorithms. In particular, we use it to prove consistency of the multivariate ExtraTree and CART algorithms, as well as their corresponding ensemble learners.

## 4.1 Extratrees

We start with the (single) ExtraTree algorithm, as the naive tree can be seen as its simplification in the case an "
n (starting with the complete training set instead of true subsampling). The concrete procedure is provided in Algorithm 2 below. We will denote the resulting regression estimator constructed by the ExtraTree algorithm as mexT
n,1 " mexT
n,1pX, Θ, Dnq. Heuristically, the regression estimator from the ExtraTree algorithm should be consistent under the consistency conditions of the naive tree given in Theorem 3.1. That this is indeed the case can be proven by bounding the quadratic error of the ExtraTree algorithm through the quadratic error of the naive tree.

Theorem 4.1. If limnÑ8 tn{n " 0, then mexT
n,1 is L
2-consistent for the regression function m *of Model* (2)*, i.e.*

$$\mathbb{E}\bigg[\left\|m_{n,1}^{e x T}(\mathbf{X},\boldsymbol{\Theta},\mathcal{D}_{n})-m(\mathbf{X})\right\|^{2}\bigg]\to0.$$

"

ȷ

5
$$f o r\,t_{n}\to\infty\,a s\,n\to\infty.$$

The above result holds for a single regression tree constructed by the ExtraTree Algorithm 2. From this we'll derive the consistency of the corresponding ensemble of Extremely Randomized Trees (ExtraTrees) as proposed by [15] in Section 4.3.

## 4.2 Cart

Breiman's [8] CART algorithm is probably the best-known single tree-based learner. In this subsection, we prove its consistency covering the original CART from [8] as well as the trees within Random Forest. The CART algorithm in Random Forest is built upon two true resampling steps. First, a sample of the size an P t1*, . . . , n*u is drawn from Dn. In the original Random Forest of [7], the subsample is a bootstrap sample drawn with replacement. However, we follow [40] and draw without replacement from Dn. As discussed in [40], this change from sampling with to without replacement is harmless. For the feature subspacing, a random subset from all features is drawn and the feature optimizing an L
2-type splitting criterion is chosen for the split. The concrete definition of the CART within Random Forest approach is stated in Algorithm 3 in the Supplement. Setting an " n and p " mtry in Algorithm 3, becomes equivalent to the original CART in [8] which is thus contained as a special case. We denote the resulting regression estimator as m*CART*
n,1pX, Θ, Dq and its consistency follows again by a comparison to the quadratic error of the naive tree. The resulting theorem is stated below.

Theorem 4.2. If limnÑ8 tn{an " 0 , then mCART
n,1is L
2-consistent for the regression function m *of Model* (2)*, i.e.*

$0$, _then $m_{n,1}^{C}$ is $L^{2}$-consistent for the regression function_  $$\mathbb{E}\!\left[\left\|m_{n,1}^{CART}(\mathbf{X},\boldsymbol{\Theta},\mathcal{D}_{n})-m(\mathbf{X})\right\|^{2}\right]\to0.$$

for tn Ñ 8 as n Ñ 8.

## 4.3 Ensembles (Including Random Forest)

In this subsection we prove the consistency of bagged-type ensembles based on consistent base learners, particularly covering the ExtraTrees [15] and Random Forest [7] approaches. It turns out that the consistency of the ensemble learner can be deduced rather easily from the consistency of its base learner. The ensemble learner (or forest) is defined as the average of a larger number, say M, of independent base learners. Mathematically, this means we have M i.i.d.

copies Θ1*, . . . ,* ΘM of Θ (each corresponding to one tree) and define the ensemble of base learners m p¨q n,1 as

$$m_{n,M}^{(\cdot)}({\bf X},\mathbf{\Theta}_{1},\ldots,\mathbf{\Theta}_{M},{\mathcal D}_{n})=\frac{1}{M}\sum_{t=1}^{M}m_{n,1}^{(\cdot)}({\bf X},\mathbf{\Theta}_{t},{\mathcal D}_{n}).$$

By an application of the finite Jensen's inequality, the consistency of the base learner is sufficient for the consistency of the corresponding ensemble.

Corollary 4.3. Let m p¨q n,1 be an L
2-consistent estimator for m in Model (2). Then, under the conditions of Theorem 4.1, we have

$$\mathbb{E}\!\left[\left\|m_{n,M}^{(\cdot)}(\mathbf{X},\mathbf{\Theta}_{1},\ldots,\mathbf{\Theta}_{M},\mathcal{D}_{n})-m(\mathbf{X})\right\|^{2}\right]\to0$$

"

ȷ

$$f o r\,t_{n}\to\infty\,a s\,n\to\infty.$$

## Algorithm 2: Extratree Algorithm

Data: The training data Dn, the maximum number of leaves tn P t1*, . . . , n*u and the number of features during the feature subsampling step mtry P t1*, . . . , p*u.

Output: A partition of r0, 1s p Set nnodes " 1, level " 0, the starting partition P0 **" tr**0, 1s pu and Plevel " H for all 1 ď level ď n; while nnodes ă tn *and at least one node contains at least two different feature- and output vectors in each case* do if P*level* " H **then**
levelÐlevel`1 else Let A " ApΘ, Dn**q " r**a1pΘq, b1pΘ**qs ˆ** *. . .* ˆ rappΘq, bppΘqs be the first element of Plevel.

if A *contains exactly one element* **then**
Plevel Ð PlevelztAu Plevel`1 Ð Plevel`1 Y tAu else Select mtry dimensions uniformly from the feature space t1*, . . . , p*u. Denote the resulting set with Mtry.;
for j P Mtry do Draw a cut-point zj " zj pΘ, Dnq uniformly on raj pΘ, Dnq, bj pΘ, Dnqs ;
Set A
jpΘ,DnqL " ra1pΘ, Dnq, b1pΘ, Dn**qs ˆ** *. . .*
ˆ raj´1pΘ, Dnq, bj´1pΘ, Dn**qs ˆ r**aj pΘ, Dnq, zj pΘ, Dnqs ˆ raj`1pΘ, Dnq, bj`1pΘ, Dn**qs ˆ** *. . .* ˆ rappΘ, Dnq, bppΘ, Dnqs and A
jpΘ,DnqR " ra1pΘ, Dnq, b1pΘ, Dn**qs ˆ** *. . .*
ˆ raj´1pΘ, Dnq, bj´1pΘ, Dn**qs ˆ p**zj pΘ, Dnq, bj pΘ, Dnqs ˆ raj`1pΘ, Dnq, bj`1pΘ, Dn**qs ˆ** *. . .* ˆ rappΘ, Dnq, bppΘ, Dnqs.

Determine

```
Ln
 `
  
  A
   jpΘ, DnqL
          ˘
          
           " Ln
              `
               
               A
                jpΘ, DnqL, AjpΘ, DnqR
                               ˘
                               

```

i"1 1XiPApΘ,Dnq
˜
›
›Yi ´ YApΘ,Dnq
› ›

2
"
1 |Gn| ÿn
´
›
›Yi ´ YAj pΘ,DnqL 1X
pjq i ăzj
´ YAj pΘ,DnqR 1X
pjq i ězj
›
›

2
¸

where |Gn| denotes the cardinality of ti : Xi P Au .

end Choose A
exT pΘ, DnqL " argmax Aj pΘ,DnqLPApMtryq LnpA
jpΘ, DnqLq, where ApMtry**q " t**AjpΘ, DnqL : j P Mtryu. AexT pΘ, DnqR is chosen analogously ([15]). Denote the resulting cells by AexT
Land AexT
R .

Plevel Ð PlevelztAu Plevel`1 Ð Plevel`1 Y tAexT
L**u Y t**AexT
R u nnodes Ð nnodes ` 1 end end end With the choice of m p¨q n,1pX, Θt, Dnq " mn,1pX, Θt, Dnq Corollary 4.3 guarantees the consistency of the ensemble of naive trees, which we call Naive Forest. For m p¨q n,1pX, Θt, Dnq " mexT
n,1pX, Θt, Dnq, Corollary 4.3 also contains the consistency of the ExtraTrees algorithm from [15]. Moreover, the consistency of the original Random Forest from [7] is included as special case by setting m p¨q n,1pX, Θt, Dnq " mCART
n,1pX, Θt, Dnq. Unlike the consistency result in [40], our result doesn't rely on an additive regression function nor on Gaussian errors and holds for multivariate output. Moreover, the Random Forest consistency Theorem 1 given in [40] requires the condition limnÑ8 tnplogpanqq9{an " 0, which enforces our condition limnÑ8 tn{an " 0. Thus, Corollary 4.3 is a generalization of Theorem 1 in [40] in four directions (regression function, error terms, output dimension and the choice of hyperparameters).

Moreover, we extend the consistency result for ExtraTrees from [5] by also covering multivariate outcomes and non-symmetric errors with finite second marginal moments. Since [5] also covers non-fixed dimensions and bounded non-continuous m, our Corollary 4.3 is not a generalization of their result.

## 5 Simulation Study

The consistency results from Sections 3 and 4 hold asymptotically. But how much are these really worth in practice?

This question is particularly interesting for the naive approaches. To answer this, we conduct a simulation study for the discussed ensemble methods. In particular, we compare the Naive Forest with the common ensemble approaches Random Forest and ExtraTrees.

## 5.1 Simulation Setting

To this end, we perform MC " 1, 000 simulation runs. In each run we generate a dataset Dmc n "
␣

rX
mc iJ, Y
mc iJs J P
r0, 1s p ˆ R
d; i ", 1*, . . . , n*(for mc " 1*, . . . , MC* according to Model (2). That is, we generate uniformly distributed feature vectors X
mc i " U pr0, 1s pq and Y
mc i " mpX
mc iq ` εi. We set p " 4 and vary the sample size n P
t50, 100, 150, 200u. All computations were made with R Version 4.2.3 [32] and the concrete model specifications are discussed below.

Regression functions. To carry out the analysis for different scenarios, we use a variety of continuous functions m as regression function:
1. Linear function: mpxiq " x J
i β, i " 1*, . . . , n*.

7

2. Polynomial function: $m(\mathbf{x}_{i})=\sum\limits_{j=1}^{4}\beta_{j}\left(x_{i}^{(j)}\right)^{j}$, $i=1,\ldots,n$. 3. Trigonometric function: $m(\mathbf{x}_{i})=2\cdot\sin(\mathbf{x}^{\top}\boldsymbol{\beta}+2)$, $i=1,\ldots$

$$\mathbf{a}(\mathbf{x}_{i}^{\top}{\boldsymbol{\beta}}+2),i=1,\ldots$$
These three settings with a univariate output are motivated from [36]. In all three settings we set the parameter vector as β " p2, 4, ´3, 0q J, which should be disadvantageous for the Naive Forest because the last feature is non-informative.

To also study a multivariate model, we consider the bivariate case (d " 2) with one non-informative feature:
4. Multivariate output function m : R
4 ÝÑ R
2 with

$$m(\mathbf{x}_{i})=\left(3\left(x_{i}^{(1)}\right)^{2}+2\left(x_{i}^{(2)}\right)^{2},\left(x_{i}^{(3)}\right)^{4}+4x_{i}^{(2)}\right)^{\top}$$

Error terms. We consider different distributional settings for the error terms ε in the univariate cases 1. - 3. We first consider Gaussian noise with εi " N p0, σ2q and then rerun the models with t5 distributed noise, to underline that gaussianity is not necessary for the consistency. For the function in 4. we generate bivariate error vectors pε1i, ε2iq J,
with ε1i and ε2iindependent and identically distributed. For the marginal distributions of ε1i and ε2ithe same combinations as for the functions 1.-3. are used. We choose the variance of the Gaussian noise such that the signal-tonoise ratio SN takes on the values t0.5, 1, 3, 5u as in [36]. Therefore, the choice of σ 2 " VarpmpXi**qq {**SN depends on VarpmpXiqq. Due to the independence of the covariates, the calculations for VarpmpXiqq are straightforward in the first two settings. In the first setting we get VarpmpXi**qq "** Var `XJ
i β
˘

" 29{12 while the variance in 2. is given by VarpmpXi**qq «** 0.7692. For 3. we estimate VarpmpXiqq by Monte Carlo simulation with 10,000 runs itself. The simulations provides the estimation Var{pmpXi**qq «** 1, 9872. For the multivariate function, we use Varp}mpXiq}q, which results in Varp}{mpXi**q}q «** 1, 7925. For the t distribution, the variance is 5/3 and not freely selectable. Hence, since we fixed the regression function m, there is no differentiation in the Signal-to-Noise ratio for the t-distributed errors.

Hyperparameters. Our choice for the number of terminal nodes is tn " ta 1{2 n u. This choice also enforces the condition limnÑ8 tn{an " 0 and we choose an " t2{3nu for Random Forest, which is close to the default value of 0.632 in the widespread R Package ranger ([45]). For simplicity, we set mtry " 2 as suggested by [31]. For the Naive Forest and the ExtraTrees we use the complete dataset, i.e. choose an " n. We consider these three ensemble learners mn,M
(Naive Forest), mexT
n,M (ExtraTrees) and m*CART*
n,M (Random Forest) with varying numbers of trees M " 50, 100, 200.

Training and Evaluation. For all combinations of n and SN we generate training datasets D1n
, . . . , DMC
nand for each dataset we train the three different ensemble learners. For a new observation x P r0, 1s we denote the prediction by the ensemble obtained from training on Dmc n by m p¨q n,Mpx, Θ1, . . . , ΘM, Dmc nq, where m p¨q n,M either stands for mn,M, mexT
n,M or m*CART*
n,M , respectively. To evaluate the performance on test data, we generate an i.i.d set of new feature vectors X11
, . . . , X11000 " U
`

r0, 1s 4
˘

for each run. Based on this set we compute

$$L_{m_{e}}^{2}=\frac{1}{1000}\sum_{i=1}^{1000}\left|m(\mathbf{X}_{i}^{\prime})-m_{n,M}^{(\cdot)}\left(\mathbf{X}_{i}^{\prime},\mathbf{\Theta}_{1},\ldots,\mathbf{\Theta}_{M},\mathcal{D}_{n}^{m_{e}}\right)\right|^{2}.$$  to estimate $\mathbb{E}\left[\left|m(\mathbf{X})-m_{n,M}^{(\cdot)}\left(\mathbf{X},\mathbf{\Theta}_{1},\ldots,\mathbf{\Theta}_{M},\mathcal{D}_{n}^{m_{e}}\right)\right|^{2}\right]$. We finally use the mean  $$\widehat{L}^{2}=\frac{1}{MC}\sum_{m_{e}=1}^{MC}L_{m_{e}}^{2}$$

as summarizing performance measure and to compare the three forests for each combination of signal-to-noise ratio, sample size and regression function.

## 5.2 Simulation Results

For M " 50 trees, we can see in Figure 2, that for most combinations of sample size, signal-to-noise ratios and considered functions m, the Random Forest performs best, closely followed by the ExtraTrees. In each setting, the Naive Forest is by far the worst performing method, reflecting our intuition to not use it for practical data analyses.

The largest margin between errors occurs for the multivariate function, while the smallest margin occurs for the non-monotonic trigonometric function. Increasing the number of trees from M " 50 to M " 100 or M " 200 (see Figure 5 and Figure 6 in the Appendix) doesn't change this conclusion, since the main problem of doing non-informative splits with probability 1{4 in the Naive Forest stays the same. Furthermore, we observe that the proven convergence of the quadratic error is relatively slow in case of the Naive Forest. In contrast, the behavior of the quadratic errors of the Random Forest matches with the results of the simulation study conducted in [2]. Changing from Gaussian to more heavy-tailed t5-distributed errors (Figure 1) also doesn't change much. In all simulated settings the error of the Naive Forest is far above the error of the Random Forest and ExtraTrees which lie close to each other. This indicates that the consistency statement alone, though certainly reassuring, doesn't indicate a good predictive performance. In fact, numerical analyses are essential to judge a method's performance.





## 6 A Small Benchmark Study

As recent discussion on neutral methods comparisons [e.g. 6, 13] encourage 'to perform benchmarking analyses additionally to the traditional simulation study' [13], we compare the performance of the three ensemble learners
(Naive Forest, ExtraTrees and Random Forest) on 6 different datasets (Airquality, Ames Housing, House Price, Possum, Quakes and Trees), that are suitable for regression tasks. Airquality, Quakes and Trees are build-in datasets in the base version of R. Possum is from the DAAG package [23], Ames Housing was provided by [11] and House Price was retrieved from Kaggle [29]. We are excluding non-binary categorical features from all datasets, as our theoretical framework in the preceding sections was specifically designed for numerical data. Additionally, we remove any features with missing values from the data and we omit six rows of the House Price dataset due to implausible entries.

Furthermore, we transform the features into the interval r0, 1s by min-max normalization [30] and standardize the target variable for better comparability of the results. The datasets are from different fields and have a variety of properties, that are listed in Table 1. Each dataset is randomly divided into five datasets by the R function createFolds from the Package caret [22], to estimate Lx2, via five-fold cross-validation.

The performance of all three ensemble learners with M " 50 (Naive Forest, ExtraTrees and Random Forest) is evaluated. The hyperparameters tn and an are chosen similar to Section 5. We choose tn " tn 1{2u as well as an " t2{3nu, see Table 1: Properties of the six different datasets and chosen hyperparameters tn and mtry. The skewness of the output variable was estimated by the empirical skewness.

| Dataset      | sample size   | p   | tn   | mtry   | skewness of Y   |
|--------------|---------------|-----|------|--------|-----------------|
| Airquality   | 153           | 4   | 12   | 2      | -0.37           |
| Ames Housing | 2930          | 27  | 54   | 5      | 1.74            |
| House Price  | 3740          | 6   | 61   | 2      | 4.78            |
| Possum       | 101           | 13  | 10   | 3      | -0.24           |
| Quakes       | 1000          | 5   | 31   | 2      | 0.77            |
| Trees        | 31            | 3   | 5    | 2      | 1.01            |

| Naive Forest   | ExtraTrees   | Random Forest   |         |           |         |           |
|----------------|--------------|-----------------|---------|-----------|---------|-----------|
| Dataset        | runtime      | Lx2             | runtime | Lx2       | runtime | Lx2       |
| Airquality     | 0.1          | 0.5971215       | 0.3     | 0.5797349 | 5.7     | 1.096039  |
| Ames Housing   | 3.8          | 0.6646426       | 6.1     | 0.3695726 | 546.4   | 0.3170644 |
| House Price    | 5.2          | 0.8857712       | 7.0     | 0.7857531 | 117.4   | 0.5095062 |
| Possum         | 0.0          | 0.8104764       | 0.3     | 0.7168872 | 6.3     | 0.5486962 |
| Quakes         | 0.8          | 0.5182705       | 1.6     | 0.3357833 | 94.2    | 0.2575057 |
| Trees          | 0.0          | 0.5675174       | 0.0     | 0.4964377 | 0.0     | 0.5220893 |

Table 2: Cross-validated L-loss estimates and runtimes (in seconds) for the three tree-based ensembles (Naive Forest, ExtraTrees, Random Forest).

Table 1 for the resulting values. We follow the recommendation of [45] and set mtry " t
?pu. The cross validated empirical Lx2 errors as well as the runtimes are presented in Table 2. The predictive performance results are quite similar to our findings from the simulation study (Section 5): The Naive Forest shows the worst performance of all three approaches and every dataset except for the Airquality dataset, where the Random Forest was even worse. For four ot of six datasets, the Random Forest exhibit a better predictive accuracy than the ExtraTree which itself was better than the Naive Forest on all datasets. Regarding runtime, the results are also not surprising: the Random Forest is remarkably slower than the other two approaches due to the greediness of the involved CART splitting optimization. Moreover, the Naive Forest is even faster than the ExrtaTrees and had a runtime advanatge up to a factor of 144 compared to the Random Forest (dataset Quakes). Due to its poor predictive performance, which cannot be improved much by tuning as it only has the hyperparameter M, we nevertheless cannot recommend the Naive Forest as predictive algorithm.

## 7 Discussion

Today, tree-based methods are an integral part of the statistical toolbox and serve as essential analysis and modeling techniques. This is especially true for Random Forests, which are often used as a reliable benchmark method [17].

Existing consistency proofs are rather technical and rely on rather restrictive model assumptions such as Gaussian errors and additive regression functions [16, 34, 40]. This is where the present paper comes in. We introduce naive trees as a straightforward and flexible proof technique for all kinds of tree-based learners. These naive trees are a simple regression approach that splits the feature space completely independent of the data. We prove that the resulting estimator is L
2-consistent in general univariate and multivariate regression settings, which do not rely on Gaussian errors nor an additive regression function. From this, we deduce consistency of a variety of tree-based learners including the CART [8], the ExtraTrees [15] and the Random Forest [7] learner.

To investigate what this consistency statement actually means in real applications, we analyze ensembles of naive trees in simulations and a small benchmark study on real datasets. The results show a relative weakness compared to its more evolved counterparts (ExtraTrees and Random Forests). In particular, (ensembles of) naive trees can in general not be recommended for practical data analyses as very large sample sizes are needed to obtain quite accurate results. This is contrary to the Random Forest and the ExtraTrees algorithms which are both (more) powerful regression approaches.

We thus conclude that while consistency results are reassuring in the sense that the approaches are roughly doing the right thing, they do not tell us anything about the practicality and predictive power in real-world scenarios. This finding also highlights the importance of numeric evaluations of theoretical results to make general practical recommendations as well as for method comparisons [6, 13, 28].

Moreover, our consistency result does not tell us anything about the underlying estimation uncertainty. In principle, naive trees could be used here due to their fast and simple computability (e.g. via Monte Carlo). However, the bounds to other learners that we use in the consistency proof are not sharp and we will work on improving them in future work and also try to derive asymptotic relative efficiencies. Moreover, other approaches based upon bootstrapping or central limit theorems [43] need to be established for our general multivariate regression setting in future research.

## Appendix

This appendix contains the proof of all theorems (APPENDIX A-C) as well as additional simulation results (APPENDIX
E). In particular, APPENDIX A derives the proof for the consistency of the naive tree, while APPENDIX B-C are concerned with the consistency of the more common tree-based learners and ensembles.