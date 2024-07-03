# Model-Free Change-Point Detection Using Modern Classifiers

Rohit Kanrar1, Feiyu Jiang2, and Zhanrui Cai3 1*Department of Statistics, Iowa State University* 2School of Management, Fudan University 3*Faculty of Business and Economics, University of Hong Kong*

## Abstract

In contemporary data analysis, it is increasingly common to work with non-stationary complex datasets. These datasets typically extend beyond the classical low-dimensional Euclidean space, making it challenging to detect shifts in their distribution without relying on strong structural assumptions. This paper introduces a novel offline change-point detection method that leverages modern classifiers developed in the machine-learning community. With suitable data splitting, the test statistic is constructed through sequential computation of the Area Under the Curve (AUC) of a classifier, which is trained on data segments on both ends of the sequence. It is shown that the resulting AUC process attains its maxima at the true change-point location, which facilitates the change-point estimation.

The proposed method is characterized by its complete nonparametric nature, significant versatility, considerable flexibility, and absence of stringent assumptions pertaining to the underlying data or any distributional shifts. Theoretically, we derive the limiting pivotal distribution of the proposed test statistic under null, as well as the asymptotic behaviors under both local and fixed alternatives. The weak consistency of the change-point estimator is provided. Extensive simulation studies and the analysis of two real-world datasets illustrate the superior performance of our approach compared to existing modelfree change-point detection methods.

Key words: distribution-free, classification, change-point, sample splitting, AUC

## 1 Introduction

In this paper, we are interested in detecting distributional changes in a sequence of independent elements {Zt}
T
t=1 taking value in a measurable space (E, E). The problem can be formulated as, H0 :Zt ∼ PX for all 1 ≤ t ≤ T

$$H_{1}:\mathbf{Z}_{t}\sim\begin{cases}\mathcal{P}_{X}\text{for}1\leq t\leq t_{0}\\ \mathcal{P}_{Y}\text{for}t_{0}+1\leq t\leq T,\quad1\leq t_{0}<T\text{is unknown,}\end{cases}\tag{1.1}$$

where PX ̸= PY are two unknown distributions. The hypothesis testing problem (1.1) is typically known as the change-point detection problem, with vast literature devoted to this area and broad applications in bioinformatics, climate science, finance, geographic studies, signal processing, and robotics, among many other areas.

Existing methods for change-point detection often rely on strong structural assumptions regarding the distributions, PX and PY , and are typically designed for specific scenarios. Many of these approaches concentrate on either the first- or second-order moments within the classical Euclidean space or rely on parametric assumptions about the data generation process, see, e.g.,
Aue and Horv´ath (2013), Chen and Gupta (2012), and Truong et al. (2020) for recent reviews.

However, in contemporary data analysis, collecting data in complex forms has become increasingly prevalent, often characterized by high dimensionality and even deviations from the conventional Euclidean space. For instance, financial analysts may seek to employ high-dimensional stock data to elucidate the causes of distributional shifts during significant economic events like the "Great Recession" (Chakraborty and Zhang, 2021). In fields such as economic geography, researchers frequently leverage satellite image data to investigate the impact of human activities on various environments (Atto et al., 2021). In urban studies, researchers analyze transportation data for disruptions or changes in traffic patterns (Chu and Chen, 2019). These examples highlight the formidable challenge of devising a universally applicable change-point detection framework that accommodates diverse data dimensions and types. In light of these observations, we propose a novel change-point detection framework named changeAUC, for detecting general distributional changes, irrespective of data dimensions and types.

## 1.1 Our Contributions

Our proposed method changeAUC is motivated by the recent success of modern classification algorithms in high-dimensional two-sample testing problems (Kim et al., 2021; Hu and Lei, 2023)
and independence testing problems (Cai et al., 2022, 2023). changeAUC involves a three-step process: data-splitting by trimming at both ends, training the classifier on terminal observations, and testing the accuracy of observations in the middle based on AUC, the Area Under the ROC Curve. The key idea behind the classification accuracy test is the following: if the two groups of samples are indeed heterogeneous, a complex classifier should be able to distinguish the underlying distributions, yielding higher accuracy on the test set. We leverage this intuition by training a classifier once, followed by recursively conducting two-sample testing across time points by measuring classification accuracy, thus enabling our objective of change-point detection. The proposed method enjoys several appealing advantages.

- completely nonparametric. It does not impose any parametric assumption on the data distributions. Moreover, it does not impose any structure on the distributional shift, e.g., change occurs in mean or covariance, change is sparse or dense.

- highly versatile. Our approach applies to virtually any data type, encompassing classical low-dimensional Euclidean, high-dimensional, and non-Euclidean data like images and texts. The sole prerequisite is the availability of a suitable classifier.

- considerably flexible. It can be fine-tuned for any particular application by selecting an appropriate classifier. Such flexibility also enables effective incorporation of prior knowledge into the analysis. For instance, a Convolutional Neural Network (CNN) can be employed to identify change-points in images or videos. Importantly, our method does not necessitate a consistently accurate classifier. As long as it captures some signals between two distributions, our proposed approach can effectively detect change-points.

- distribution-free. Our test statistic has a pivotal limiting distribution under the null.

In fact, it is shown to be a functional of Brownian motion, which implies that the critical values can be numerically tabulated.
We provide a rigorous theoretical analysis of the proposed method. We use empirical process theory (Vaart and Wellner, 2023) to obtain the pivotal limiting distribution of the test statistic under null. The asymptotic behaviors of the test statistic are also derived under local and fixed alternatives. Furthermore, we establish the weak consistency of the maximizer of the AUC
process for estimation purposes. Extensive numerical studies on both simulated data and two real applications further corroborate the theoretical findings. The empirical results underscore the effectiveness of our testing framework, demonstrating its ability to control size performance and showcasing competitive power performance compared to existing methods.

## 1.2 Related Work

The origin of offline change-point problems can be dated back to the seminal work of Page (1954). The classical approaches to tackling change-point problems are typically limited to low dimensional quantities, such as mean and variance, or specific parametric models. We refer to Aue and Horv´ath (2013), Chen and Gupta (2012), and Truong et al. (2020) for comprehensive reviews. With the development of modern data collection techniques, high-dimensional data and non-Euclidean data have become frequently encountered in many scientific areas. In particular, for high dimensional data, extensive works have devoted to mean changes (Jirak, 2015; Cho and Fryzlewicz, 2015; Wang and Samworth, 2018; Enikeeva and Harchaoui, 2019; Yu and Chen, 2020; Wang et al., 2022); covariance changes (Avanesov and Buzun, 2018; Steland, 2019; Dette et al., 2022; Li et al., 2023); and other model parameters (Kaul et al., 2019; Liu et al., 2020).

For non-Euclidean data, much effort has been put into Hilbert space, and we mention Berkes et al. (2009); Aue et al. (2018) for functional mean changes and Jiao et al. (2023) for functional covariance changes. We also note Dubey and M¨uller (2020) and Jiang et al. (2024) for recent developments in change-point detection of first- and second-order moments in metric space.

The above works are primarily developed for detecting only one or two specific types of changes, which may lack power when changes occur in other aspects of data. In light of this finding, in recent years, nonparametric methods that are powerful against general types of changes have attracted much attention, and most of them focus on the low dimensional Euclidean space, see, e.g., Harchaoui and Capp´e (2007), Matteson and James (2014), Zou et al. (2014), Arlot et al. (2019). We are only aware of a few recent developments in high-dimensional data. In particular, Chakraborty and Zhang (2021) uses the idea of generalized energy distance.

However, their method can only capture the pairwise homogeneity (heterogeneity under H1) of the marginal distributions in high dimensional (PX,PY ), which may lack power when (PX,PY )
correspond to the same marginal distributions but differ in other aspects. Some graph-based tests have been proposed recently by Chen and Zhang (2015) and Chu and Chen (2019). Yet, as pointed out by Chakraborty and Zhang (2021), they may lack power to detect changes in higher-order moments. In contrast, our proposed approach takes advantage of of contemporary classifiers within the machine-learning community. This adaptability allows us to detect changes that extend beyond the realms of marginal distributions and moments, setting our method apart in terms of its capability to uncover variations in high-dimensional data and even non-Euclidean data. These findings are further corroborated by simulation studies in Section 4.

We also mention a few recent contributions that borrow the strength of machine learning tools in the context of the two-sample testing and change-point problems. Since Kim et al.

(2021), there has been a flurry of efforts that employ classifiers to conduct two-sample tests, see, e.g., Lopez-Paz and Oquab (2016), Kim et al. (2019), Kirchler et al. (2020). However, the extension to the change-point context seems largely unexplored, with the exception of Lee et al. (2023), Londschien et al. (2023) and Li et al. (2024). In particular, Lee et al. (2023) applies neural networks for online change-point detection, while the latter two focuses on the offline setting as ours. Londschien et al. (2023) uses Random Forest for detecting change-points by introducing a classifier-based nonparametric likelihood ratio, while Li et al. (2024) proposes to use neural networks for detecting change-points in time series under supervised setting. Our proposed framework differs in several key aspects. 1) Both of the aforementioned methods implicitly assume low-dimensional data, whereas our approach accommodates additionally both high-dimensional data and non-Euclidean data. 2) Neither of the aforementioned methods offers asymptotic results, leading to either increased computational demands through permutation or conservative type-I error controls. In contrast, our method offers an asymptotic approach by providing a pivotal limiting null distribution, which facilitates practical statistical inference.

Therefore, our results complement their works, particularly in the theoretical aspect. 3) Unlike the nonparametric likelihood used by Londschien et al. (2023) and the empirical risk minimizerbased classification accuracy utilized by Li et al. (2024), we measure classification accuracy using the AUC. Owing to its rank-sum-based nature, AUC could be more favorable as it is robust in handling imbalanced data splits and weakly trained classifiers. For a more comprehensive discussion, we refer the reader to Section 2. Lastly, we mention a similar data-splitting approach implemented by Gao et al. (2023), where the authors propose a dimension agnostic change-point test statistic by projecting middle observations to the direction determined by observations at both ends of the sequence. However, their method is designed only for detecting a change in the mean, while our method is more general and uses rank-sum comparison by obtaining AUC.

The rest of this paper is organized as follows. Section 2 introduces our proposed method with comprehensive justifications for each step. Theoretical analysis is conducted in Section 3.

Section 4 showcases the finite sample performance of our framework. Section 5 demonstrates the application of our method to two real datasets. Section 6 concludes with discussion and future direction. All technical proofs are deferred to the supplementary materials.

## 2 Methods

Section 2.1 outlines the proposed method, changeAUC, for detecting at most one change-point in a sequence of independent observations. Section 2.2 provides a detailed justification of steps of changeAUC. Section 2.3 extends changeAUC for estimation of multiple change-points.

## 2.1 Proposed Method

Consider a sequence of independent random elements {Zt}
T
t=1 defined on a common probability space (Ω, F, P) and taking value in a measurable space (E, E). Let PX and PY be two different probability distributions on the same probability space such that PX,PY are absolutely continuous with respect to each other, i.e., PX ≪ PY and PY ≪ PX. Let us recall (1.1) for the hypothesis testing of at most one change-point in a set of observations {zt}
T
t=1:

$$H_{0}:\mathbf{Z}_{t}\sim\mathcal{P}_{X}\text{for all}1\leq t\leq T$$ $$H_{1}:\mathbf{Z}_{t}\sim\begin{cases}\mathcal{P}_{X}\text{for}1\leq t\leq t_{0}\\ \mathcal{P}_{Y}\text{for}t_{0}+1\leq t\leq T,\quad1\leq t_{0}<T\text{is unknown.}\end{cases}$$  Our proposed methodology comprises the following four steps.  
7
1. Sample Splitting: For a small trimming parameter ϵ ∈ (0, 1/2) with m = ⌊T ϵ⌋, we split the observations into three parts:

$D_{0}\stackrel{{\rm def}}{{=}}\{{\bf z}_{1},\ldots,{\bf z}_{m}\},\quad D^{v}\stackrel{{\rm def}}{{=}}\{{\bf z}_{m+1},\ldots,{\bf z}_{T-m}\},\quad D_{1}\stackrel{{\rm def}}{{=}}\{{\bf z}_{T-m+1},\ldots,{\bf z}_{T}\}.$
2. Training Classifier: We assign labels vt = 0 for zt ∈ D0 and vt = 1 for zt ∈ D1 and train a classifier based on observations from both ends:

$$\left\{\left(v_{t},\mathbf{z}_{t}\right):\mathbf{z}_{t}\in D_{0}\cup D_{1}\right\}.$$

Let θb(·) be the estimated conditional probability distribution associated with the classifier.

In other words, given a new observation z, θb(z) = Pb [v = 1|z] is the estimated probability of z being generated by the same distribution governing D1.

3. Recursive Splitting: For another small trimming parameter η ∈ (0, 1/2 − ϵ), we define the set of candidate change-points as, Icp def = {⌊T r⌋ : r ∈ [ϵ + η, 1 − ϵ − η]}. For each k ∈ Icp, we split the validation set, Dvinto two parts:
$D_{0}^{v}(k)\stackrel{{\rm def}}{{=}}\{{\bf z}_{m+1},\ldots,{\bf z}_{k}\},\quad D_{1}^{v}(k)\stackrel{{\rm def}}{{=}}\{{\bf z}_{k+1},\ldots,{\bf z}_{T-m}\}$
4. Measuring Accuracy: For each k ∈ Icp, we assign labels, vt = 0 for all zt ∈ Dv 0
(k)
and vt = 1 for all zt ∈ Dv 1
(k), and calculate the Area Under the Receiver Operating Characteristic (ROC) curve (AUC) using {(vt, zt) : zt ∈ Dv 0
(k) ∪ Dv 1
(k)}, which is defined as follows:

$$\widehat{\Psi}(k)\stackrel{\mathrm{def}}{=}\frac{1}{(k-m)(T-m-k)}\sum_{i=m+1}^{k}\sum_{j=k+1}^{T-m}\mathbb{I}\left\{\widehat{\theta}(\mathbf{z}_{i})<\widehat{\theta}(\mathbf{z}_{j})\right\}.$$

We iterate through the aforementioned four steps for all candidate change-points and obtain the collection of AUCs, denoted by {Ψ( b k)}k∈Icp
.

Remark 1. The choices of ϵ and η are subjective. A moderate value of m = ⌊T ϵ⌋ is essential for appropriate training of the classifier. A smaller choice of ϵ *may result in power loss, whereas* a larger ϵ *requires the change-point to exist near the middle of the sequence. In practice, we* propose to fix ϵ = 0.15. However, choosing a smaller ϵ in our framework is feasible, particularly when the sample size is substantial or if the classification algorithm performs well with a smaller training sample. The role of η works as the trimming parameter commonly adopted in changepoint literature, see Andrews *(1993). We propose to fix* η = 0.05 *for practical implementations.*
Intuitively, under H0 when there is no change-point, the estimate Ψ( b k) is expected to be close to 0.5 for all values of k, resembling a random guess. In contrast, under H1, Ψ( b k) is anticipated to exceed 0.5 for k near the true change-point t0, allowing for differentiation between the two distributions. Therefore, the test statistic is formulated by choosing the maximal AUC,

$$\widehat{Q}_{T}\ {\stackrel{\mathrm{def}}{=}}\ \operatorname*{max}_{k\in{\mathcal{I}}_{c p}}\widehat{\Psi}(k).$$

The resulting maximizer, RbT
def
= argmaxk∈Icp Ψ( b k), is then used for change-point estimation.

We reject the null hypothesis H0 in (1.1) for a large value of QbT . In Section 3, we rigorously investigate the asymptotic behavior of QbT under the null hypothesis H0 and establish that, after appropriate scaling, it converges weakly a pivotal process. Specifically,

$$\sup_{k\in\mathbb{Z}_{\mathbb{P}}}\left\{\sqrt{T}(\widehat{\Psi}(k)-1/2)\right\}\stackrel{{d}}{{\to}}\sup_{r\in[\gamma,1-\gamma]}G_{0}(r)\quad\text{as}\quad T\to\infty,\tag{2.1}$$

where γ = ϵ + η, and G0(·) is a pivotal functional of standard Brownian motions. Therefore, we can simulate the theoretical quantiles and devise a test for H0. Let Q(1−α) be the 100(1−α)%
quantile of supr∈[γ,1−γ] G0(r). Based on 100,000 Monte Carlo simulations, Table 1 outline the value of Q(1 − α) for α = 20%, 10%, 5%, 1% and 0.5% respectively. Consequently, a level-α test for detecting a single change-point rejects H0 if √T
QbT − 1/2
≥ Q(1 − α).

Table 1: Simulated quantiles of supr∈[γ,1−γ] G0(r) for ϵ = 0.15, η = 0.05.

$$\frac{0.5\%}{4.051}$$

| α        | 20%   | 10%   | 5%    | 1%    | 0.5%   |
|----------|-------|-------|-------|-------|--------|
| Q(1 − α) | 2.231 | 2.664 | 3.040 | 3.784 | 4.051  |

We summarize a concise view for all the steps of changeAUC in Algorithm 1.

## 2.2 Classification Accuracy For Detecting A Single Change-Point

In practice, both PX,PY and t0 are unknown. In order to test (1.1), it is important to distinguish PY from PX. The fundamental feature of changeAUC lies in training an appropriate classifier to discern the heterogeneity between the two unknown distributions. Let θ(·) be the true conditional probability corresponding to θb(·). When infinite samples are drawn from two distributions, PX and PY , and each sample is associated with a label V = 0 or V = 1 depending on its origin, it becomes feasible to obtain the true conditional probability,

$$\theta(\mathbf{z})\ {\stackrel{\mathrm{def}}{=}}\ \mathbb{P}\left[v=1|\mathbf{z}\right],$$

where, z ∈ E is a new observation. Moreover, θ(·) is related to the true likelihood ratio,

$$L(\mathbf{z})\ {\stackrel{\mathrm{def}}{=}}\ {\frac{\theta(\mathbf{z})}{1-\theta(\mathbf{z})}}={\frac{d P_{Y}}{d P_{X}}}(\mathbf{z}),$$
(z), (2.2)
$$(2.2)$$
$$\mathrm{{9}}$$

Algorithm 1 changeAUC: Using Classifier To Detect and Localize a Single change-point Require: Data {zt}
T
t=1; choice of classifier; choices of tuning parameters, ϵ ∈ (0, 1/2) and η ∈ (0, 1/2 − ϵ); significance level α.

1: Split the data into D0, Dv, D1 using m = ⌊T ϵ⌋ and obtain Icp from Dv using η.

2: Train the classifier based on D0, D1 to obtain {θb(zt) : zt ∈ Dv}.

3: for k ∈ Icp do

4: Split Dvinto Dv 0
(k), Dv 1
(k).
5: Calculate Ψ( b k), based on {θb(zt) : zt ∈ Dv 0
(k)} and {θb(zt) : zt ∈ Dv 1
(k)}.

6: end for 7: Compute QbT
def
= maxk∈Icp Ψ( b k) and RbT
def
= argmaxk∈Icp Ψ( b k).

8: if √T(QbT − 1/2) > Q(1 − α) then 9: return RbT as a significant change-point 10: end if and L(z) = 1 almost surely if PX = PY . Otherwise, L(z) is expected to be larger (smaller) than one if Z ∼ PY (Z ∼ PX), respectively. Therefore, L(z) or equivalently, θ(z) serves as a one-dimensional projection of the original observation z. Proposition 1 below asserts the close relationship between such projection and the total variation between two distributions. This provides an initial motivation for employing a rank-sum comparison of the likelihood ratios to assess the heterogeneity.

Proposition 1. Consider two probability measures PX and PY *on a common probability space*
(Ω, F, P) such that PY ≪ PX, with the Radon-Nikodyn derivative dPY /dPX(·) having a continuous distribution under PX. Let Z1 ∼ PX and Z2 ∼ PY *be independent random elements.*
Then, it follows that,

$$\frac{1}{2}d_{tv}(\mathcal{P}_{X},\mathcal{P}_{Y})\leq\mathbb{P}\left\{\frac{d\mathcal{P}_{Y}}{d\mathcal{P}_{X}}(\mathbf{Z}_{1})<\frac{d\mathcal{P}_{Y}}{d\mathcal{P}_{X}}(\mathbf{Z}_{2})\right\}-\frac{1}{2}\leq d_{tv}(\mathcal{P}_{X},\mathcal{P}_{Y}),\tag{2.3}$$

where, dtv(PX,PY ) is defined as the total variation distance between PX and PY .

Given a significant total variation distance between the two probability distributions, it is anticipated that an empirical estimate of the probability in (2.3) will effectively encapsulate the

$$P_{Y\cdot}$$
