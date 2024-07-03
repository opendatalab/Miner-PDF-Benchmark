# Model-free Change-point Detection Using Modern Classifiers 

Rohit Kanrar ${ }^{1}$, Feiyu Jiang ${ }^{2}$, and Zhanrui Cai ${ }^{3}$<br>${ }^{1}$ Department of Statistics, Iowa State University<br>${ }^{2}$ School of Management, Fudan University<br>${ }^{3}$ Faculty of Business and Economics, University of Hong Kong


#### Abstract

In contemporary data analysis, it is increasingly common to work with non-stationary complex datasets. These datasets typically extend beyond the classical low-dimensional Euclidean space, making it challenging to detect shifts in their distribution without relying on strong structural assumptions. This paper introduces a novel offline change-point detection method that leverages modern classifiers developed in the machine-learning community. With suitable data splitting, the test statistic is constructed through sequential computation of the Area Under the Curve (AUC) of a classifier, which is trained on data segments on both ends of the sequence. It is shown that the resulting AUC process attains its maxima at the true change-point location, which facilitates the change-point estimation. The proposed method is characterized by its complete nonparametric nature, significant versatility, considerable flexibility, and absence of stringent assumptions pertaining to the underlying data or any distributional shifts. Theoretically, we derive the limiting pivotal distribution of the proposed test statistic under null, as well as the asymptotic behaviors under both local and fixed alternatives. The weak consistency of the change-point estimator is provided. Extensive simulation studies and the analysis of two real-world datasets illustrate the superior performance of our approach compared to existing modelfree change-point detection methods.


Key words: distribution-free, classification, change-point, sample splitting, AUC

## 1 Introduction

In this paper, we are interested in detecting distributional changes in a sequence of independent elements $\left\{\boldsymbol{Z}_{t}\right\}_{t=1}^{T}$ taking value in a measurable space $(E, \mathcal{E})$. The problem can be formulated as,

$$
\begin{aligned}
& H_{0}: \boldsymbol{Z}_{t} \sim \mathcal{P}_{X} \text { for all } 1 \leq t \leq T \\
& H_{1}: \boldsymbol{Z}_{t} \sim\left\{\begin{array}{l}
\mathcal{P}_{X} \text { for } 1 \leq t \leq t_{0} \\
\mathcal{P}_{Y} \text { for } t_{0}+1 \leq t \leq T, \quad 1 \leq t_{0}<T \text { is unknown }
\end{array}\right.
\end{aligned}
$$

where $\mathcal{P}_{X} \neq \mathcal{P}_{Y}$ are two unknown distributions. The hypothesis testing problem (1.1) is typically known as the change-point detection problem, with vast literature devoted to this area and broad applications in bioinformatics, climate science, finance, geographic studies, signal processing, and robotics, among many other areas.

Existing methods for change-point detection often rely on strong structural assumptions regarding the distributions, $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$, and are typically designed for specific scenarios. Many of these approaches concentrate on either the first- or second-order moments within the classical Euclidean space or rely on parametric assumptions about the data generation process, see, e.g., Aue and Horváth (2013), Chen and Gupta (2012), and Truong et al. (2020) for recent reviews. However, in contemporary data analysis, collecting data in complex forms has become increasingly prevalent, often characterized by high dimensionality and even deviations from the conventional Euclidean space. For instance, financial analysts may seek to employ high-dimensional stock data to elucidate the causes of distributional shifts during significant economic events like the "Great Recession" (Chakraborty and Zhang, 2021). In fields such as economic geography, researchers frequently leverage satellite image data to investigate the impact of human activities on various environments (Atto et al., 2021). In urban studies, researchers analyze transportation data for disruptions or changes in traffic patterns (Chu and Chen, 2019). These examples highlight the formidable challenge of devising a universally applicable change-point detection framework that accommodates diverse data dimensions and types. In light of these observations, we propose a novel change-point detection framework named changeAUC, for detecting general distributional changes, irrespective of data dimensions and types.

### 1.1 Our Contributions

Our proposed method changeAUC is motivated by the recent success of modern classification algorithms in high-dimensional two-sample testing problems (Kim et al., 2021; Hu and Lei, 2023) and independence testing problems (Cai et al., 2022, 2023). changeAUC involves a three-step process: data-splitting by trimming at both ends, training the classifier on terminal observations, and testing the accuracy of observations in the middle based on AUC, the Area Under the ROC Curve. The key idea behind the classification accuracy test is the following: if the two groups of samples are indeed heterogeneous, a complex classifier should be able to distinguish the underlying distributions, yielding higher accuracy on the test set. We leverage this intuition by training a classifier once, followed by recursively conducting two-sample testing across time points by measuring classification accuracy, thus enabling our objective of change-point detection. The proposed method enjoys several appealing advantages.

- COMPlETELY NONPaRametRic. It does not impose any parametric assumption on the data distributions. Moreover, it does not impose any structure on the distributional shift, e.g., change occurs in mean or covariance, change is sparse or dense.
- HIGHLY VERSATILE. Our approach applies to virtually any data type, encompassing classical low-dimensional Euclidean, high-dimensional, and non-Euclidean data like images and texts. The sole prerequisite is the availability of a suitable classifier.
- CONSIDERABLY FLEXIBLE. It can be fine-tuned for any particular application by selecting an appropriate classifier. Such flexibility also enables effective incorporation of prior knowledge into the analysis. For instance, a Convolutional Neural Network (CNN) can be employed to identify change-points in images or videos. Importantly, our method does not necessitate a consistently accurate classifier. As long as it captures some signals between two distributions, our proposed approach can effectively detect change-points.
- DISTRIBUTION-FREE. Our test statistic has a pivotal limiting distribution under the null. In fact, it is shown to be a functional of Brownian motion, which implies that the critical values can be numerically tabulated.

We provide a rigorous theoretical analysis of the proposed method. We use empirical process theory (Vaart and Wellner, 2023) to obtain the pivotal limiting distribution of the test statistic under null. The asymptotic behaviors of the test statistic are also derived under local and fixed alternatives. Furthermore, we establish the weak consistency of the maximizer of the AUC process for estimation purposes. Extensive numerical studies on both simulated data and two real applications further corroborate the theoretical findings. The empirical results underscore the effectiveness of our testing framework, demonstrating its ability to control size performance and showcasing competitive power performance compared to existing methods.

### 1.2 Related Work

The origin of offline change-point problems can be dated back to the seminal work of Page (1954). The classical approaches to tackling change-point problems are typically limited to low dimensional quantities, such as mean and variance, or specific parametric models. We refer to Aue and Horváth (2013), Chen and Gupta (2012), and Truong et al. (2020) for comprehensive reviews. With the development of modern data collection techniques, high-dimensional data and non-Euclidean data have become frequently encountered in many scientific areas. In particular, for high dimensional data, extensive works have devoted to mean changes (Jirak, 2015; Cho and Fryzlewicz, 2015; Wang and Samworth, 2018; Enikeeva and Harchaoui, 2019; Yu and Chen, 2020; Wang et al., 2022); covariance changes (Avanesov and Buzun, 2018; Steland, 2019; Dette et al., 2022; Li et al., 2023); and other model parameters (Kaul et al., 2019; Liu et al., 2020). For non-Euclidean data, much effort has been put into Hilbert space, and we mention Berkes et al. (2009); Aue et al. (2018) for functional mean changes and Jiao et al. (2023) for functional covariance changes. We also note Dubey and Müller (2020) and Jiang et al. (2024) for recent
developments in change-point detection of first- and second-order moments in metric space.

The above works are primarily developed for detecting only one or two specific types of changes, which may lack power when changes occur in other aspects of data. In light of this finding, in recent years, nonparametric methods that are powerful against general types of changes have attracted much attention, and most of them focus on the low dimensional Euclidean space, see, e.g., Harchaoui and Cappé (2007), Matteson and James (2014), Zou et al. (2014), Arlot et al. (2019). We are only aware of a few recent developments in high-dimensional data. In particular, Chakraborty and Zhang (2021) uses the idea of generalized energy distance. However, their method can only capture the pairwise homogeneity (heterogeneity under $H_{1}$ ) of the marginal distributions in high dimensional $\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right.$ ), which may lack power when $\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right)$ correspond to the same marginal distributions but differ in other aspects. Some graph-based tests have been proposed recently by Chen and Zhang (2015) and Chu and Chen (2019). Yet, as pointed out by Chakraborty and Zhang (2021), they may lack power to detect changes in higher-order moments. In contrast, our proposed approach takes advantage of of contemporary classifiers within the machine-learning community. This adaptability allows us to detect changes that extend beyond the realms of marginal distributions and moments, setting our method apart in terms of its capability to uncover variations in high-dimensional data and even non-Euclidean data. These findings are further corroborated by simulation studies in Section 4.

We also mention a few recent contributions that borrow the strength of machine learning tools in the context of the two-sample testing and change-point problems. Since Kim et al. (2021), there has been a flurry of efforts that employ classifiers to conduct two-sample tests, see, e.g., Lopez-Paz and Oquab (2016), Kim et al. (2019), Kirchler et al. (2020). However, the extension to the change-point context seems largely unexplored, with the exception of Lee et al. (2023), Londschien et al. (2023) and Li et al. (2024). In particular, Lee et al. (2023) applies neural networks for online change-point detection, while the latter two focuses on the offline setting as ours. Londschien et al. (2023) uses Random Forest for detecting change-points by
introducing a classifier-based nonparametric likelihood ratio, while Li et al. (2024) proposes to use neural networks for detecting change-points in time series under supervised setting. Our proposed framework differs in several key aspects. 1) Both of the aforementioned methods implicitly assume low-dimensional data, whereas our approach accommodates additionally both high-dimensional data and non-Euclidean data. 2) Neither of the aforementioned methods offers asymptotic results, leading to either increased computational demands through permutation or conservative type-I error controls. In contrast, our method offers an asymptotic approach by providing a pivotal limiting null distribution, which facilitates practical statistical inference. Therefore, our results complement their works, particularly in the theoretical aspect. 3) Unlike the nonparametric likelihood used by Londschien et al. (2023) and the empirical risk minimizerbased classification accuracy utilized by Li et al. (2024), we measure classification accuracy using the AUC. Owing to its rank-sum-based nature, AUC could be more favorable as it is robust in handling imbalanced data splits and weakly trained classifiers. For a more comprehensive discussion, we refer the reader to Section 2. Lastly, we mention a similar data-splitting approach implemented by Gao et al. (2023), where the authors propose a dimension agnostic change-point test statistic by projecting middle observations to the direction determined by observations at both ends of the sequence. However, their method is designed only for detecting a change in the mean, while our method is more general and uses rank-sum comparison by obtaining AUC.

The rest of this paper is organized as follows. Section 2 introduces our proposed method with comprehensive justifications for each step. Theoretical analysis is conducted in Section 3. Section 4 showcases the finite sample performance of our framework. Section 5 demonstrates the application of our method to two real datasets. Section 6 concludes with discussion and future direction. All technical proofs are deferred to the supplementary materials.

## 2 Methods

Section 2.1 outlines the proposed method, changeAUC, for detecting at most one change-point in a sequence of independent observations. Section 2.2 provides a detailed justification of steps of changeAUC. Section 2.3 extends changeAUC for estimation of multiple change-points.

### 2.1 Proposed Method

Consider a sequence of independent random elements $\left\{\mathbf{Z}_{t}\right\}_{t=1}^{T}$ defined on a common probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and taking value in a measurable space $(E, \mathcal{E})$. Let $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$ be two different probability distributions on the same probability space such that $\mathcal{P}_{X}, \mathcal{P}_{Y}$ are absolutely continuous with respect to each other, i.e., $\mathcal{P}_{X} \ll \mathcal{P}_{Y}$ and $\mathcal{P}_{Y} \ll \mathcal{P}_{X}$. Let us recall (1.1) for the hypothesis testing of at most one change-point in a set of observations $\left\{\mathbf{z}_{t}\right\}_{t=1}^{T}$ :

$$
\begin{aligned}
& H_{0}: \boldsymbol{Z}_{t} \sim \mathcal{P}_{X} \text { for all } 1 \leq t \leq T \\
& H_{1}: \boldsymbol{Z}_{t} \sim\left\{\begin{array}{l}
\mathcal{P}_{X} \text { for } 1 \leq t \leq t_{0} \\
\mathcal{P}_{Y} \text { for } t_{0}+1 \leq t \leq T, \quad 1 \leq t_{0}<T \text { is unknown }
\end{array}\right.
\end{aligned}
$$

Our proposed methodology comprises the following four steps.

1. Sample Splitting: For a small trimming parameter $\epsilon \in(0,1 / 2)$ with $m=\lfloor T \epsilon\rfloor$, we split the observations into three parts:

$$
D_{0} \stackrel{\text { def }}{=}\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}, \quad D^{v} \stackrel{\text { def }}{=}\left\{\mathbf{z}_{m+1}, \ldots, \mathbf{z}_{T-m}\right\}, \quad D_{1} \stackrel{\text { def }}{=}\left\{\mathbf{z}_{T-m+1}, \ldots, \mathbf{z}_{T}\right\}
$$

2. Training Classifier: We assign labels $v_{t}=0$ for $\mathbf{z}_{t} \in D_{0}$ and $v_{t}=1$ for $\mathbf{z}_{t} \in D_{1}$ and train a classifier based on observations from both ends:

$$
\left\{\left(v_{t}, \mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{0} \cup D_{1}\right\}
$$

Let $\widehat{\theta}(\cdot)$ be the estimated conditional probability distribution associated with the classifier. In other words, given a new observation $\boldsymbol{z}, \widehat{\theta}(\boldsymbol{z})=\widehat{\mathbb{P}}[v=1 \mid \boldsymbol{z}]$ is the estimated probability of $\boldsymbol{z}$ being generated by the same distribution governing $D_{1}$.

3. Recursive Splitting: For another small trimming parameter $\eta \in(0,1 / 2-\epsilon)$, we define the set of candidate change-points as, $\mathcal{I}_{c p} \stackrel{\text { def }}{=}\{\lfloor T r\rfloor: r \in[\epsilon+\eta, 1-\epsilon-\eta]\}$. For each $k \in \mathcal{I}_{c p}$, we split the validation set, $D^{v}$ into two parts:

$$
D_{0}^{v}(k) \stackrel{\text { def }}{=}\left\{\mathbf{z}_{m+1}, \ldots, \mathbf{z}_{k}\right\}, \quad D_{1}^{v}(k) \stackrel{\text { def }}{=}\left\{\mathbf{z}_{k+1}, \ldots, \mathbf{z}_{T-m}\right\}
$$

4. Measuring Accuracy: For each $k \in \mathcal{I}_{c p}$, we assign labels, $v_{t}=0$ for all $\mathbf{z}_{t} \in D_{0}^{v}(k)$ and $v_{t}=1$ for all $\mathbf{z}_{t} \in D_{1}^{v}(k)$, and calculate the Area Under the Receiver Operating Characteristic (ROC) curve (AUC) using $\left\{\left(v_{t}, \mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{0}^{v}(k) \cup D_{1}^{v}(k)\right\}$, which is defined as follows:

$$
\widehat{\Psi}(k) \stackrel{\text { def }}{=} \frac{1}{(k-m)(T-m-k)} \sum_{i=m+1}^{k} \sum_{j=k+1}^{T-m} \mathbb{I}\left\{\widehat{\theta}\left(\mathbf{z}_{i}\right)<\widehat{\theta}\left(\mathbf{z}_{j}\right)\right\}
$$

We iterate through the aforementioned four steps for all candidate change-points and obtain the collection of AUCs, denoted by $\{\widehat{\Psi}(k)\}_{k \in \mathcal{I}_{c p}}$.

Remark 1. The choices of $\epsilon$ and $\eta$ are subjective. A moderate value of $m=\lfloor T \epsilon\rfloor$ is essential for appropriate training of the classifier. A smaller choice of $\epsilon$ may result in power loss, whereas a larger $\epsilon$ requires the change-point to exist near the middle of the sequence. In practice, we propose to fix $\epsilon=0.15$. However, choosing a smaller $\epsilon$ in our framework is feasible, particularly when the sample size is substantial or if the classification algorithm performs well with a smaller training sample. The role of $\eta$ works as the trimming parameter commonly adopted in changepoint literature, see Andrews (1993). We propose to fix $\eta=0.05$ for practical implementations.

Intuitively, under $H_{0}$ when there is no change-point, the estimate $\widehat{\Psi}(k)$ is expected to be close to 0.5 for all values of $k$, resembling a random guess. In contrast, under $H_{1}, \widehat{\Psi}(k)$ is anticipated to exceed 0.5 for $k$ near the true change-point $t_{0}$, allowing for differentiation between the two distributions. Therefore, the test statistic is formulated by choosing the maximal AUC,

$$
\widehat{Q}_{T} \stackrel{\text { def }}{=} \max _{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)
$$

The resulting maximizer, $\widehat{R}_{T} \stackrel{\text { def }}{=} \operatorname{argmax}_{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)$, is then used for change-point estimation.

We reject the null hypothesis $H_{0}$ in (1.1) for a large value of $\widehat{Q}_{T}$. In Section 3, we rigorously investigate the asymptotic behavior of $\widehat{Q}_{T}$ under the null hypothesis $H_{0}$ and establish that, after appropriate scaling, it converges weakly a pivotal process. Specifically,

$$
\sup _{k \in \mathcal{I}_{c p}}\{\sqrt{T}(\widehat{\Psi}(k)-1 / 2)\} \xrightarrow{d} \sup _{r \in[\gamma, 1-\gamma]} G_{0}(r) \quad \text { as } \quad T \rightarrow \infty
$$

where $\gamma=\epsilon+\eta$, and $G_{0}(\cdot)$ is a pivotal functional of standard Brownian motions. Therefore, we can simulate the theoretical quantiles and devise a test for $H_{0}$. Let $Q(1-\alpha)$ be the $100(1-\alpha) \%$ quantile of $\sup _{r \in[\gamma, 1-\gamma]} G_{0}(r)$. Based on 100,000 Monte Carlo simulations, Table 1 outline the value of $Q(1-\alpha)$ for $\alpha=20 \%, 10 \%, 5 \%, 1 \%$ and $0.5 \%$ respectively. Consequently, a level- $\alpha$ test for detecting a single change-point rejects $H_{0}$ if $\sqrt{T}\left(\widehat{Q}_{T}-1 / 2\right) \geq Q(1-\alpha)$.

Table 1: Simulated quantiles of $\sup _{r \in[\gamma, 1-\gamma]} G_{0}(r)$ for $\epsilon=0.15, \eta=0.05$.

| $\alpha$ | $20 \%$ | $10 \%$ | $5 \%$ | $1 \%$ | $0.5 \%$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $Q(1-\alpha)$ | 2.231 | 2.664 | 3.040 | 3.784 | 4.051 |

We summarize a concise view for all the steps of changeAUC in Algorithm 1.

### 2.2 Classification Accuracy for Detecting a Single Change-point

In practice, both $\mathcal{P}_{X}, \mathcal{P}_{Y}$ and $t_{0}$ are unknown. In order to test (1.1), it is important to distinguish $\mathcal{P}_{Y}$ from $\mathcal{P}_{X}$. The fundamental feature of changeAUC lies in training an appropriate classifier to discern the heterogeneity between the two unknown distributions. Let $\theta(\cdot)$ be the true conditional probability corresponding to $\widehat{\theta}(\cdot)$. When infinite samples are drawn from two distributions, $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$, and each sample is associated with a label $V=0$ or $V=1$ depending on its origin, it becomes feasible to obtain the true conditional probability,

$$
\theta(\mathbf{z}) \stackrel{\text { def }}{=} \mathbb{P}[v=1 \mid \mathbf{z}]
$$

where, $\mathbf{z} \in E$ is a new observation. Moreover, $\theta(\cdot)$ is related to the true likelihood ratio,

$$
L(\mathbf{z}) \stackrel{\text { def }}{=} \frac{\theta(\mathbf{z})}{1-\theta(\mathbf{z})}=\frac{d \mathcal{P}_{Y}}{d \mathcal{P}_{X}}(\mathbf{z})
$$

Algorithm 1 changeAUC: Using Classifier To Detect and Localize a Single change-point

Require: Data $\left\{\boldsymbol{z}_{t}\right\}_{t=1}^{T}$; choice of classifier; choices of tuning parameters, $\epsilon \in(0,1 / 2)$ and $\eta \in(0,1 / 2-\epsilon)$; significance level $\alpha$.

1: Split the data into $D_{0}, D^{v}, D_{1}$ using $m=\lfloor T \epsilon\rfloor$ and obtain $\mathcal{I}_{c p}$ from $D^{v}$ using $\eta$.

2: Train the classifier based on $D_{0}, D_{1}$ to obtain $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right): \mathbf{z}_{t} \in D^{v}\right\}$.

3: for $k \in \mathcal{I}_{c p}$ do

4: $\quad$ Split $D^{v}$ into $D_{0}^{v}(k), D_{1}^{v}(k)$.

5: $\quad$ Calculate $\widehat{\Psi}(k)$, based on $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{0}^{v}(k)\right\}$ and $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{1}^{v}(k)\right\}$.

6: end for

7: Compute $\widehat{Q}_{T} \stackrel{\text { def }}{=} \max _{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)$ and $\widehat{R}_{T} \stackrel{\text { def }}{=} \operatorname{argmax}_{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)$.

8: if $\sqrt{T}\left(\widehat{Q}_{T}-1 / 2\right)>Q(1-\alpha)$ then

9: $\quad$ return $\widehat{R}_{T}$ as a significant change-point

10: end if

and $L(\mathbf{z})=1$ almost surely if $\mathcal{P}_{X}=\mathcal{P}_{Y}$. Otherwise, $L(\mathbf{z})$ is expected to be larger (smaller) than one if $\mathbf{Z} \sim \mathcal{P}_{Y}\left(\mathbf{Z} \sim \mathcal{P}_{X}\right)$, respectively. Therefore, $L(\mathbf{z})$ or equivalently, $\theta(\mathbf{z})$ serves as a one-dimensional projection of the original observation z. Proposition 1 below asserts the close relationship between such projection and the total variation between two distributions. This provides an initial motivation for employing a rank-sum comparison of the likelihood ratios to assess the heterogeneity.

Proposition 1. Consider two probability measures $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$ on a common probability space $(\Omega, \mathcal{F}, \mathbb{P})$ such that $\mathcal{P}_{Y} \ll \mathcal{P}_{X}$, with the Radon-Nikodyn derivative $d \mathcal{P}_{Y} / d \mathcal{P}_{X}(\cdot)$ having a continuous distribution under $\mathcal{P}_{X}$. Let $\mathbf{Z}_{1} \sim \mathcal{P}_{X}$ and $\mathbf{Z}_{2} \sim \mathcal{P}_{Y}$ be independent random elements. Then, it follows that,

$$
\frac{1}{2} d_{t v}\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right) \leq \mathbb{P}\left\{\frac{d \mathcal{P}_{Y}}{d \mathcal{P}_{X}}\left(\mathbf{Z}_{1}\right)<\frac{d \mathcal{P}_{Y}}{d \mathcal{P}_{X}}\left(\mathbf{Z}_{2}\right)\right\}-\frac{1}{2} \leq d_{t v}\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right)
$$

where, $d_{t v}\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right)$ is defined as the total variation distance between $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$.

Given a significant total variation distance between the two probability distributions, it is anticipated that an empirical estimate of the probability in (2.3) will effectively encapsulate the
heterogeneity between $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$. In this context, it is noteworthy that the probability in (2.3) involves the likelihood ratio, $L(\cdot) \stackrel{\text { def }}{=}\left(d \mathcal{P}_{Y} / d \mathcal{P}_{X}\right)(\cdot)$. For low-dimensional Euclidean data, it is common to estimate $L(\cdot)$ directly. However, for high-dimensional Euclidean data, direct estimation of the likelihood ratio is challenging due to the curse of dimensionality. Instead, it is possible to estimate $L(\cdot)$ by plugging in a consistent estimate, $\widehat{\theta}(\cdot)$ in $(2.2)$ :

$$
\widehat{L}(\mathbf{z}) \stackrel{\text { def }}{=} \frac{\widehat{d \mathcal{P}_{Y}}}{d \mathcal{P}_{X}}(\mathbf{z})=\frac{\widehat{\theta}(\mathbf{z})}{1-\widehat{\theta}(\mathbf{z})}
$$

We note that it is possible to utilize external datasets to obtain the estimated conditions probabilities $\widehat{\theta}(\cdot)$ under supervised setting, as in Li et al. (2024). But this paper works under the unsupervised setting by presuming the absence of such external datasets. Therefore, to mitigate the risk of over-fitting, we propose data-splitting as a more practical solution and utilize the observations in the training set: $\left\{\left(v_{t}, \mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{0} \cup D_{1}\right\}$ to obtain $\widehat{\theta}(\cdot)$. Furthermore, we utilize the observations in the validation set, $D^{v}$, and employ $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right): \mathbf{z}_{t} \in D^{v}\right\}$ to assess the heterogeneity between $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$.

In the change-point problem, the change location $t_{0}$ is typically unknown and unlike a conventional supervised classification problem, the validation data $D^{v}$ is not labeled. To circumvent this challenge, we recursively split $D^{v}$ into $D_{0}^{v}(k)$ and $D_{1}^{v}(k)$ for each $k \in \mathcal{I}_{c p}$, and propose the two-sample rank sum comparison of $\left\{\widehat{L}(\mathbf{z}): \mathbf{z} \in D^{v}\right\}$, as a robust alternative to the average misclassification error. Later in Section 3, it is elucidated that the use of rank-sum comparison alleviates the necessity for a consistently estimated $\widehat{\theta}(\cdot)$. See Remark 2 for more details.

The two-sample rank-sum comparison of the estimated likelihood ratio is equivalent to the AUC of the trained classifier (Fawcett, 2006; Chakravarti et al., 2023). Specifically, for each change-point candidate $k$, based on the validation data, $D_{0}^{v}(k)$ and $D_{1}^{v}(k)$, provided, $\widehat{\theta}\left(\mathbf{z}_{t}\right) \in$
$(0,1), \forall t=m+1, \ldots, T-m$, we have

$$
\begin{aligned}
\widehat{\Psi}(k) & \stackrel{\text { def }}{=} \frac{1}{(k-m)(T-m-k)} \sum_{i=m+1}^{k} \sum_{j=k+1}^{T-m} \mathbb{I}\left\{\widehat{\theta}\left(\mathbf{z}_{i}\right)<\widehat{\theta}\left(\mathbf{z}_{j}\right)\right\} \\
& =\frac{1}{(k-m)(T-m-k)} \sum_{i=m+1}^{k} \sum_{j=k+1}^{T-m} \mathbb{I}\left\{\frac{\widehat{\theta}\left(\mathbf{z}_{i}\right)}{1-\widehat{\theta}\left(\mathbf{z}_{i}\right)}<\frac{\widehat{\theta}\left(\mathbf{z}_{j}\right)}{1-\widehat{\theta}\left(\mathbf{z}_{j}\right)}\right\} \\
& =\frac{1}{(k-m)(T-m-k)} \sum_{i=m+1}^{k} \sum_{j=k+1}^{T-m} \mathbb{I}\left\{\widehat{L}\left(\mathbf{z}_{i}\right)<\widehat{L}\left(\mathbf{z}_{j}\right)\right\}
\end{aligned}
$$

where, the second equality holds since, $x \rightarrow x /(1-x)$ is a monotone transformation for $x \in(0,1)$. Note that, $\left\{\widehat{L}\left(\mathbf{z}_{i}\right)\right\}_{i=m+1}^{T-m}$ is expected to be close to 1 , if $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$ are the same, yielding a value of $\widehat{\Psi}(k)$ close to $1 / 2$. Otherwise, the likelihood ratios, $\left\{\widehat{L}\left(\mathbf{z}_{i}\right)\right\}_{i=t_{0}+1}^{T-m}$, are likely to be larger than 1 , which essentially yields $\widehat{\Psi}(k)$, larger than $1 / 2$ for $k$ near $t_{0}$.

A couple of remarks are in order to provide further justification for our decision to use a ranksum comparison of the estimated probabilities, or equivalently AUC, as opposed to employing raw class probabilities or more commonly used metrics such as average misclassification error.

Remark 2. The AUC provides an additional advantage by its connection to a rank sum comparison. Our framework excels in accurately estimating the change-point's location. In the case of a single change-point at $t_{0}$, precise estimation is achieved when the sets of conditional probabilities, $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{0}^{v}\right\}$ and $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right): \mathbf{z}_{t} \in D_{1}^{v}\right\}$, demonstrate a noticeable distinction. Unlike approaches requiring these sets to be close to 0 and 1, respectively, as typically obtained through training a consistent classifier, our framework exhibits robust performance even when such conditions are not strictly met.

Remark 3. Another advantage of AUC in this context is its robust performance in two-sample classification with severe class imbalance. To elaborate, consider Step 4 of changeAUC, where the estimated class probabilities $\left\{\widehat{\theta}\left(\mathbf{z}_{t}\right)\right\}_{t=m+1}^{T-m}$ are utilized to derive the collection of AUC, denoted as $\{\widehat{\Psi}(k)\}_{k \in \mathcal{I}_{c p}}$. When $\eta$ is chosen to be small, $D_{0}^{v}(k)$ and $D_{1}^{v}(k)$ form two sets of observations with severe imbalance when $k$ is in proximity to the start or end of $\mathcal{I}_{c p}$. In such cases, if $t_{0}$ is not close to the middle of $\mathcal{I}_{c p}$, the use of AUC proves to be a more robust alternative for achieving
higher accuracy near $t_{0}$ compared to the average misclassification error with a fixed threshold, such as 1/2, as proposed in Kim et al. (2021) for two-sample testing with similar sample sizes.

### 2.3 Extension to Multiple change-points:

It is feasible to integrate changeAUC into existing algorithms designed for estimating multiple change-points, such as wild binary segmentation (Fryzlewicz, 2014), seeded binary segmentation (SBS) (Kovács et al., 2023), isolating single change-points (Anastasiou and Fryzlewicz, 2022), among others. In this paper, we employ SBS for the estimation of multiple change-points in two real datasets in Section 5.

The SBS procedure works as follows. For a sequence of length $T$, SBS recursively applies a single change-point test statistic to a set of predetermined intervals $\mathcal{I}_{\lambda}$ defined as:

$$
\mathcal{I}_{\lambda}=\bigcup_{k=1}^{\left\lceil\log _{1 / \gamma}(T)\right\rceil} \mathcal{I}_{k}, \quad \mathcal{I}_{k}=\cup_{i=1}^{T_{k}}\left\{\left(\left\lfloor(i-1) s_{k}\right\rfloor,\left\lfloor(i-1) s_{k}+l_{k}\right\rfloor\right)\right\}
$$

where $\lambda \in[1 / 2,1)$ is known as a decay parameter, and each $\mathcal{I}_{k}$ is a collection of sub-intervals of length $l_{k}=T \gamma^{k-1}$ evenly shifted by $s_{k}=\left(T-l_{k}\right) /\left(T_{k}-1\right)$. SBS finds the largest value of test statistics evaluated at all sub-intervals, and compare it with a predetermined threshold level $\Delta$. Once the maximum test statistic exceeds $\Delta$, a change-point is claimed. The data is further divided into two subsamples accordingly and the same procedure is applied to each of them.

It is worth noting that Kovács et al. (2023) specifically addresses multiple change-point detection in the mean only. Their threshold $\Delta$ may not be directly applicable when integrating changeAUC into their algorithm, necessitating new theoretical developments for overall control of type-I error in the presence of multiple change-points beyond the mean of distributions. We defer this aspect to future work. Instead, following the approach proposed by Dubey and Zheng (2023), we perform a permutation test to obtain the threshold $\Delta$. Algorithm 2 outlines the procedure for this approach. For practical implementation, we set $\Delta$ as the $90 \%$ quantile of the permutation null distribution of the maximal test statistics, and $\gamma=1 / \sqrt{2}$.

Algorithm 2 Multiple change-point Detection with changeAUC \& SBS

Require: $l$ and $u$ : lower and upper boundaries of time index; all parameters of changeAUC in Algorithm 1, minLen: minimum length of intervals, $\gamma$ : decay parameter, $\widehat{\tau}$ : initial set of change-points, $B$ : number of permutations.

procedure CHANGEAUC-SBS $(1, \mathrm{u}, \gamma, \widehat{\tau}$, minLen $)$

if $u-l<$ minLen then

STOP

else

calculate seeded intervals $\mathcal{I}_{\lambda}=\left\{\left[l_{i}, u_{i}\right]: i \in\left|\mathcal{I}_{\lambda}\right|\right\}$.

for $i=1, \ldots,\left|\mathcal{I}_{\lambda}\right|$ do

Apply changeAUC on $\left\{\mathbf{z}_{t}: t \in\left[l_{i}, u_{i}\right] \cap \mathbb{N}\right\}$.

Denote the maximum AUC as $\widehat{Q}_{i}$ and maximizer as $\widehat{R}_{i}$.

end for

for $b=1, \ldots, B$ do

Permute $\left\{\mathbf{z}_{t}: t \in[l, u] \cap \mathbb{N}\right\}$. Apply changeAUC on the permuted sample.

Denote $\widehat{Q}^{(b)}$ as the maximum AUC.

end for

Calculate $\Delta: 90 \%$ quantile of $\left\{\widehat{Q}^{(b)}\right\}_{b=1}^{B}$.

if $\max _{i \in\left\{1, \ldots,\left|\mathcal{I}_{\lambda}\right|\right\}} \widehat{Q}_{i} \geq \Delta$ then

Fix $m_{Q}=\operatorname{argmax}_{i \in\left\{1, \ldots,\left|\mathcal{I}_{\lambda}\right|\right\}} \widehat{Q}_{i}$ and $\widehat{\tau}=\widehat{\tau} \cup \widehat{R}_{m_{Q}}$

Implement changeAUC-SBS $\left(1, \widehat{R}_{m_{Q}}, \gamma, \widehat{\tau}\right.$, minLen $)$.

Implement changeAUC-SBS $\left(\widehat{R}_{m_{Q}}+1, \mathrm{u}, \gamma, \widehat{\tau}\right.$, minLen $)$.

else

break

end if

end if

return $\widehat{\tau}$ : final set of change-points.

end procedure

## 3 Theoretical Justification

In this section, we investigate the theoretical properties of changeAUC. Section 3.1 derives the limiting null distribution of the test statistic, which justifies our claims in (2.1). The power behavior under both fixed and local alternatives is presented in Section 3.2. Furthermore, Section 3.3 presents the weak consistency property of the change-point estimator $\widehat{R}_{T}$. Before presenting the theoretical results, we define some necessary notations.

Let $\mathbb{P}_{*}, \mathbb{E}_{*}, \operatorname{Var}_{*}$ and, $\operatorname{Cov}_{*}$ be the conditional probability, expectation, variance, and covariance given the trained classifier and the training data $D_{0} \cup D_{1}$. For an arbitrary random element $\mathbf{Z} \in E$, let $F_{X, *}(\cdot)$ and $F_{Y, *}(\cdot)$ be the conditional cumulative distribution functions (CDF) of $\widehat{\theta}(\mathbf{Z})$ when $\mathbf{Z} \sim \mathcal{P}_{X}$ and $\mathbf{Z} \sim \mathcal{P}_{Y}$, respectively. For independent random elements $\left\{\mathbf{Z}_{t}\right\}_{t=1}^{T}$, we define $\widehat{W}_{t}^{X} \stackrel{\text { def }}{=} F_{X, *}\left(\mathbf{Z}_{t}\right)$ and $\widehat{W}_{t}^{Y} \stackrel{\text { def }}{=} F_{Y, *}\left(\mathbf{Z}_{t}\right)$ for all $t=1, \ldots, T$. Also define, $\gamma \stackrel{\text { def }}{=} \epsilon+\eta$.

### 3.1 Limiting Null Distribution

Recall, $\widehat{Q}_{T} \stackrel{\text { def }}{=} \max _{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)$ is the proposed test statistic for $H_{0}$ vs $H_{1}$. With suitable scaling, it is customary to study the limiting behavior of the whole AUC process: $\{\widehat{\Psi}(\lfloor T r\rfloor)\}_{r \in[\gamma, 1-\gamma]}$. In Theorem 1, we prove that $\{\sqrt{T}(\widehat{\Psi}(\lfloor T r\rfloor)-1 / 2)\}_{r \in[\gamma, 1-\gamma]}$ converges uniformly to a pivotal process with respect to the conditional probability measure $\mathbb{P}_{*}$.

Theorem 1. Suppose, $\widehat{\theta}(z)$ is continuous with respect to $\mathcal{P}_{X}$. Then, under $H_{0}$, it follows that, in probability $\mathbb{P}_{*}$,

$$
\{\sqrt{T}(\widehat{\Psi}(\lfloor T r\rfloor)-1 / 2)\}_{r \in[\gamma, 1-\gamma]} \stackrel{d}{\rightsquigarrow}\left\{G_{0}(r)\right\}_{r \in[\gamma, 1-\gamma]}, \quad \text { in } L^{\infty}([0,1])
$$

where for a standard Brownian Motion $B(\cdot), G_{0}(\cdot)$ is defined as

$$
G_{0}(r) \stackrel{\text { def }}{=} \frac{1}{\sqrt{12}}\left[\frac{B(1-\epsilon)-B(r)}{1-\epsilon-r}-\frac{B(r)-B(\epsilon)}{r-\epsilon}\right], \quad \text { for } r \in[\gamma, 1-\gamma]
$$

Note that $G_{0}(\cdot)$ is functional of standard Brownian Motion, and does not depend on the classifier, data dimension, or the data distribution, which leads us to propose a computation-
ally feasible yet statistically sound testing framework using simulated theoretical quantiles of $\sup _{r \in[\gamma, 1-\gamma]} G_{0}(r)$ in Table 1.

In Theorem 1, we do not require that $\widehat{\theta}(z)$ is consistently estimated. In fact, under $H_{0}$, a random guess is also applicable. The key assumption lies in the continuity of $\widehat{\theta}(z)$ with respect to $\mathcal{P}_{X}$, which is typically satisfied for commonly used classifiers such as logistic regression, random forest, and deep neural networks. When there exists a point mass, we can inject a random tie-breaking ranking scheme and all the theory still goes through.

### 3.2 Uniform Weak Convergence Under Local and Fixed Alternative

Next, we investigate the limiting behaviors of the test under the alternative hypothesis of at most one change-point. Let the true change-point be $t_{0}=\lfloor\tau T\rfloor$ for some $\tau \in[\gamma, 1-\gamma]$. The observed random elements, $\left\{\mathbf{z}_{t}\right\}_{t=1}^{T}$, are generated from the following setup:

$$
\mathbf{Z}_{t} \stackrel{\mathrm{iid}}{\sim}\left\{\begin{array}{l}
\mathcal{P}_{X} \text { for } 1 \leq t \leq t_{0} \\
\mathcal{P}_{Y} \text { for } t_{0}+1 \leq t \leq T
\end{array}\right.
$$

Recall the likelihood ratio, $L(\cdot)=\left(d \mathcal{P}_{Y} / d \mathcal{P}_{X}\right)(\cdot)$ in $(2.2)$, the following proposition quantifies how it is connected to the total variation distance between $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$ and thus the departure of $H_{1}$ from $H_{0}$.

Proposition 2. Consider two probability measures $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$ on a common probability space $(\Omega, \mathcal{F}, \mathbb{P})$ such that $\mathcal{P}_{Y} \ll \mathcal{P}_{X}$, with the Radon-Nikodyn derivative $d \mathcal{P}_{Y} / d \mathcal{P}_{X}(\cdot)$ having a continuous distribution under $\mathcal{P}_{X}$. Let $\mathbf{Z}_{X}, \mathbf{Z}_{X}^{\prime} \sim$ iid $\mathcal{P}_{X}$ be independent random elements, and define

$$
\delta \stackrel{\text { def }}{=} \mathbb{E}\left|L\left(\mathbf{Z}_{X}\right)-L\left(\mathbf{Z}_{X}^{\prime}\right)\right|, \quad \text { for } \mathbf{Z}_{X}, \mathbf{Z}_{X}^{\prime} \stackrel{\text { iid }}{\sim} \mathcal{P}_{X}
$$

Then, it follows that,

$$
2 d_{t v}\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right) \leq \delta \leq 4 d_{t v}\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right)
$$

where $d_{t v}\left(\mathcal{P}_{X}, \mathcal{P}_{Y}\right)$ is defined as the total variation distance between $\mathcal{P}_{X}$ and $\mathcal{P}_{Y}$.

Note that $\delta=0$ if and only if $L(\cdot)$ is a constant measurable function, which is equivalent to $\mathcal{P}_{X} \equiv \mathcal{P}_{Y}$ almost surely. Therefore, $\delta$ can measure how much the alternative hypothesis $H_{1}$
deviates from the null hypothesis $H_{0}$. In Section 3.2.1. we present the limiting behavior of $\widehat{Q}_{T}$ under the fixed alternative framework $\sqrt{T} \delta \rightarrow \infty$. Section 3.2.2 investigates the limiting behavior of $\widehat{Q}_{T}$, under a local alternative framework $\sqrt{T} \delta \rightarrow C$ for a fixed constant $C>0$.

### 3.2.1 Fixed Alternative

Assumption 1. For independent random elements $\mathbf{Z}_{X} \sim \mathcal{P}_{X}, \mathbf{Z}_{Y} \sim \mathcal{P}_{Y}$, let us define $\mu_{*} \stackrel{\text { def }}{=}$ $\mathbb{P}_{*}\left(\widehat{\theta}\left(\mathbf{Z}_{X}\right)<\widehat{\theta}\left(\mathbf{Z}_{Y}\right)\right)$ and $\mu \stackrel{\text { def }}{=} \mathbb{P}\left(\theta\left(\mathbf{Z}_{X}\right)<\theta\left(\mathbf{Z}_{Y}\right)\right)$. Then, there exists a fixed small constant $c>0$, such that

$$
\mathbb{P}_{*}\left[\left|\mu_{*}-\mu\right| \leq \frac{\delta}{8}-c\right] \rightarrow 1 \quad \text { as, } T \rightarrow \infty
$$

where $\delta$ is defined in (3.2).

Assumption 1 stipulates that, with high probability, the true signal $\delta$ should dominate the average approximation error incurred by estimating conditional probability using classifier, which is denoted as $\mu_{*}-\mu$. Note that a constant error bound is sufficient to ensure high power within our testing framework as we don't require that the classifier is consistently trained. Instead, we only require the estimated $\widehat{\theta}(\cdot)$ can preserve the monotonicity of $\theta(\cdot)$ up to a small constant error. This observation substantiates the assertions in Section 2.2 and is further underscored in Remark 2.

The following theorem ensures the consistency of our test.

Theorem 2. Under $H_{1}$, suppose Assumption 1 holds and $\sqrt{T} \delta \rightarrow \infty$. Then,

$$
\sup _{r \in[\gamma, 1-\gamma]}\left\{\sqrt{T}\left(\widehat{\Psi}(\lfloor T r\rfloor)-\frac{1}{2}\right)\right\} \rightarrow \infty, \quad \text { in probability, } \mathbb{P}_{*}
$$

### 3.2.2 Local Alternative

Assumption 2. For random elements $\mathbf{Z}_{1}, \mathbf{Z}_{2} \in E$ there exists $\zeta>0$ such that

(1) $\mathbb{E}_{*}\left|\mathbb{I}\left\{\widehat{\theta}\left(\mathbf{Z}_{1}\right)<\widehat{\theta}\left(\mathbf{Z}_{2}\right)\right\}-\mathbb{I}\left\{\theta\left(\mathbf{Z}_{1}\right)<\theta\left(\mathbf{Z}_{2}\right)\right\}\right|=O_{\mathbb{P}_{*}}\left(T^{-\zeta}\right)$.

For $\mathbf{Z}_{1} \sim \mathcal{P}_{X}, \mathbf{Z}_{2} \sim \mathcal{P}_{Y}$ and $\mu_{*}=\mathbb{P}_{*}\left(\widehat{\theta}\left(\mathbf{Z}_{1}\right)<\widehat{\theta}\left(\mathbf{Z}_{2}\right)\right), \mu=\mathbb{P}\left(\theta\left(\mathbf{Z}_{1}\right)<\theta\left(\mathbf{Z}_{2}\right)\right)$, we assume

(2) $\mu_{*}-\mu=o_{\mathbb{P}_{*}}\left(T^{-1 / 2}\right)$.

Assumption 2(1) is slightly stronger than Assumption 1, and requires that $\widehat{\theta}(\cdot)$ can consistently preserve the monotonicity of $\theta(\cdot)$. In the context of the local alternative hypothesis, where $\delta$ approaches zero as rapidly as $1 / \sqrt{T}$, a more stringent condition in Assumption 2(2) is imposed on the average approximation error $\left(\mu_{*}-\mu\right)$. Notably, the super consistency in Assumption 2(2) is applied to the expected monotonicity of rank of conditional probabilities rather than directly to the classifier $\widehat{\theta}(\cdot)$. Similar assumptions have been recently utilized and verified in tests of independence (Theorem 7 in Cai et al. (2023)) and two-sample conditional distribution testing (Proposition 1 in Hu and Lei (2023)).

Theorem 3. Suppose Assumption 2 is true. Under the local alternative such that $\sqrt{T} \delta \rightarrow C$, for some constant $C>0$, then the following holds true:

$$
\left\{\sqrt{T}\left(\widehat{\Psi}(\lfloor T r\rfloor)-\frac{1}{2}\right)\right\}_{r \in[\gamma, 1-\gamma]} \stackrel{d}{\rightsquigarrow}\left\{\Delta_{G}(r ; \tau, \epsilon)+G_{0}(r)\right\}_{r \in[\gamma, 1-\gamma]}, \quad \text { in probability, } \mathbb{P}_{*},
$$

where $G_{0}(\cdot)$ is defined in Theorem 1, and

$$
\Delta_{G}(r ; \tau, \epsilon) \stackrel{\text { def }}{=} \frac{C}{4} \begin{cases}(1-\epsilon-\tau) /(1-\epsilon-r) & \text { for } \gamma<r<\tau<1-\gamma \\ (\tau-\epsilon) /(r-\epsilon) & \text { for } \gamma<\tau<r<1-\gamma\end{cases}
$$

### 3.3 Weak Consistency

The primary objective of this paper is to introduce a testing framework for a single changepoint. Motivated by favorable localization performance observed in simulation studies, we establish a weak consistency result for estimating the change-point using $\widehat{R}_{T}=\operatorname{argmax}_{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)$. To accomplish this, we introduce Assumption 3, which, while stronger than Assumption 1, is considerably weaker than Assumption 2.

Assumption 3. For independent random elements $\mathbf{Z}_{1} \sim \mathcal{P}_{X}, \mathbf{Z}_{2} \sim \mathcal{P}_{Y}$, let us recall, $\mu_{*}=$ $\mathbb{P}_{*}\left(\hat{\theta}\left(\mathbf{Z}_{1}\right)<\widehat{\theta}\left(\mathbf{Z}_{2}\right)\right)$ and $\mu=\mathbb{P}\left(\theta\left(\mathbf{Z}_{1}\right)<\theta\left(\mathbf{Z}_{2}\right)\right)$. Then, the following holds true:

$$
\mu_{*}-\mu=o_{\mathbb{P}_{*}}(1)
$$

Note we only require the classification error to have a constant error bound in Assumption 1 to ensure power. However, the error bound must vanish asymptotically for accurate estimation.

Theorem 4. Recall that $\widehat{R}_{T}=\operatorname{argmax}_{k \in \mathcal{I}_{c p}} \widehat{\Psi}(k)$ and $t_{0}$ is the true change-point. Under the fixed alternative with $\delta>C$ for some fixed constant $C>0$. If Assumption 3 holds then, $\left|\widehat{R}_{T}-t_{0}\right| / T \xrightarrow{p} 0$, under $\mathbb{P}_{*}$.

Theorem 4 obtains the consistency of the relative location of change-point. Since our framework is purely nonparametric, it would be challenging to derive the explicit localization rate, and we leave this problem for future investigation.

## 4 Numerical Simulations

In this section, we examine the finite sample performance of our proposed method. Specifically, the performance on high-dimensional Euclidean data is investigated in Section 4.1 whereas that on the non-Euclidean data using artificially constructed images CIFAR10 database (Krizhevsky et al., 2009) is presented in Section 4.2.

### 4.1 High Dimensional Euclidean Data

In this section, we examine the size and power performance of the proposed test in highdimensional Euclidean data. To implement our test, we apply three classifiers, briefly summarized as follows.

- Regularized Logistic: (denoted by Logis) We apply the regularized logistic classifier with LASSO penalty. R package glmnet is used for Logis (Friedman et al., 2010).
- Fully-connected Neural Network: (denoted by Fnn) We use a fully connected neural network with three hidden layers, ReLU activation and the binary cross-entropy loss. Additionally, a LASSO penalty is enforced in each layer. Python framework Tensorflow is used for Fnn (Abadi et al., 2016).
- Random Forest: (denoted by Rf) We employ a random forest classifier with 200 trees, with each having a maximum depth of 8. R package randomForest (Liaw and Wiener, 2002) is used for Rf.

For size performance, we consider the following data generating processes with $T \in\{1000,2000\}$ and $p \in\{10,50,200,500,1000\}$,

Standard Null: $\left\{\mathbf{Z}_{t}\right\}_{t=1}^{T} \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, I_{p}\right) ;$

Banded Null: $\left\{\mathbf{Z}_{t}\right\}_{t=1}^{T} \stackrel{\text { iid }}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, \Sigma\right)$ with $\Sigma=\left(\sigma_{i j}\right)_{i, j=1}^{p}, \sigma_{i j}=0.8^{|i-j|} ;$

Exponential Null: $\left\{\mathbf{Z}_{t j}\right\}_{t=1}^{T} \stackrel{\mathrm{iid}}{\sim} \operatorname{Exp}(1)$ for $j=1, \cdots, p$.

Table 2 presents the empirical rejection rates across 1000 replications at $5 \%$ significance level. The results demonstrate that all the considered classifiers successfully control the type-I error in all settings.

Table 2: Size performance over 1000 Monte Carlo replications, at 5\% significance level.(\%)

|  | Standard Null |  |  | Banded Null |  |  | Exponential Null |  |  |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $(T, p) \backslash$ Classifier | Logis | Rf | Fnn | Logis | Rf | Fnn | Logis | Rf | Fnn |
| $(1000,10)$ | 3.6 | 2.5 | 4.4 | 3.6 | 2.5 | 3.9 | 3.6 | 4.7 | 4.5 |
| $(1000,50)$ | 4.4 | 3.5 | 3.9 | 4.4 | 3.5 | 3.8 | 5.7 | 4.1 | 5.0 |
| $(1000,200)$ | 4.4 | 4.1 | 5.4 | 4.4 | 4.1 | 4.5 | 5.2 | 5.1 | 5.0 |
| $(1000,500)$ | 5.7 | 4.5 | 3.5 | 5.7 | 4.5 | 3.7 | 4.5 | 4.4 | 4.4 |
| $(1000,1000)$ | 3.8 | 5.1 | 3.6 | 3.8 | 5.1 | 4.4 | 4.1 | 4.7 | 3.7 |
| $(2000,10)$ | 3.8 | 3.1 | 2.8 | 3.8 | 3.1 | 4.8 | 4.4 | 3.7 | 4.6 |
| $(2000,50)$ | 4.4 | 4.6 | 4.0 | 4.4 | 4.6 | 4.5 | 4.6 | 5.1 | 5.0 |
| $(2000,200)$ | 5.2 | 4.7 | 3.5 | 5.2 | 4.7 | 5.0 | 5.2 | 4.7 | 4.5 |
| $(2000,500)$ | 4.2 | 3.9 | 4.3 | 4.2 | 3.9 | 3.3 | 4.0 | 5.6 | 3.6 |
| $(2000,1000)$ | 4.0 | 4.1 | 4.6 | 4.0 | 4.1 | 5.0 | 4.3 | 4.6 | 3.8 |

Next, we study the power performance in the high-dimensional setting. We fix the changepoint location at $t_{0}=\lfloor T / 2\rfloor$ with data length $T=1000$, and data dimension $p \in\{500,1000\}$, such that $\left\{\mathbf{Z}_{t}\right\}_{t=1}^{t_{0}} \stackrel{\text { iid }}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, I_{p}\right)$. For the data after the change-point, the following datagenerating processes are considered.

Dense Mean: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{p}\left(\boldsymbol{\mu}, I_{p}\right)$ with $\boldsymbol{\mu}=\left(\mu_{i}\right)_{i=1}^{p}, \mu_{i}=2 / \sqrt{\lfloor p / 5\rfloor}$ for $1 \leq i \leq\lfloor p / 5\rfloor$, and $\mu_{i}=0$ for $1+\lfloor p / 5\rfloor \leq i \leq p$;

Sparse Mean: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{p}\left(\boldsymbol{\mu}, I_{p}\right)$ with $\boldsymbol{\mu}=\left(\mu_{i}\right)_{i=1}^{p}, \mu_{i}=2 / \sqrt{\lfloor p / 100\rfloor}$ for $1 \leq i \leq$ $\lfloor p / 100\rfloor$, and $\mu_{i}=0$ for $1+\lfloor p / 100\rfloor \leq i \leq p$;

Dense Cov: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, \Sigma\right)$ with $\Sigma=\left(\sigma_{i j}\right)_{i, j=1}^{p}, \sigma_{i i}=1, \sigma_{i j}=0.1$ for $i \neq j$;

Banded Cov: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, \Sigma\right)$ with $\Sigma=\left(\sigma_{i j}\right)_{i, j=1}^{p}, \sigma_{i j}=0.8^{|i-j|} ;$

Dense Diag Cov: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\text { iid }}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, \Sigma\right)$, with $\Sigma=\left(\sigma_{i j}\right)_{i, j=1}^{p}, \sigma_{i i}=1+5 / \sqrt{\lfloor p / 5\rfloor}$ for $1 \leq i \leq\lfloor p / 5\rfloor, \sigma_{i i}=1$ for $\lfloor p / 5\rfloor+1 \leq i \leq p$, and $\sigma_{i j}=0$ for $i \neq j$;

Sparse Diag Cov: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{p}\left(\mathbf{0}_{p}, \Sigma\right)$, with $\Sigma=\left(\sigma_{i j}\right)$, where $\sigma_{i i}=1+5 / \sqrt{\lfloor p / 100\rfloor}$ for $1 \leq i \leq\lfloor p / 100\rfloor, \sigma_{i i}=1$ for $\lfloor p / 100\rfloor+1 \leq i \leq p$, and $\sigma_{i j}=0$ for $i \neq j$;

Dense Distribution: $\left\{\mathbf{Z}_{t j}\right\}_{t=t_{0}+1}^{T} \stackrel{\text { iid }}{\sim} \operatorname{Exp}(1)-1$ for $j=1, \ldots,\lfloor p / 5\rfloor$ and $\left\{\mathbf{Z}_{t j}\right\}_{t=t_{0}+1}^{T} \stackrel{\text { iid }}{\sim} \mathcal{N}_{1}(0,1)$ for $j=\lfloor p / 5\rfloor+1, \ldots, p$;

Sparse Distribution: $\left\{\mathbf{Z}_{t}\right\}_{t=t_{0}+1}^{T} \stackrel{\text { iid }}{\sim} \operatorname{Exp}(1)-1$ for $j=1, \ldots,\lfloor p / 100\rfloor$ and $\left\{\mathbf{Z}_{t j}\right\}_{t=t_{0}+1}^{T} \stackrel{\text { iid }}{\sim}$ $\mathcal{N}_{1}(0,1)$ for $j=\lfloor p / 100\rfloor+1, \ldots, p$.

Note that for the distributional changes, the first- and second-order moments of the underlying distributions remain the same before and after the change-point.

In addition to the proposed methods, we consider the following two competitors among many existing tests for detecting change-points in high-dimensional data.

- The graph-based method gseg proposed by Chen and Zhang (2015) and Chu and Chen (2019), and is implemented by the gSeg package in R. Here, the graph is constructed using the minimal spanning tree, and four edge-count scan statistics are considered: the original one (gseg_orig), weighted (gseg_wei), generalized (gseg_gen), and max-type (gseg_max).
- The generalized energy distance-based method proposed by Chakraborty and Zhang (2021) (denoted as Hddc): The default distance metric $\gamma\left(z, z^{\prime}\right)=\left\|z-z^{\prime}\right\|_{1}^{1 / 2}$ is utilized to calculate the interpoint distance.

We first assess the computational efficiency of the proposed methods in comparison to existing ones. To illustrate the idea, we use a 16-core AMD EPYC 7542 CPU with 32 GB RAM for all methods except for Fnn, which is performed using a single core Intel Xeon 6226R CPU with a single NVIDIA Tesla V100 GPU. Data generation follows the "Dense Mean" setup, with performance under other settings being similar and thus omitted. Table 3 presents the average computation time for all five methods over 1000 replications, with standard deviations shown in parentheses. From the table, it's evident that the proposed three methods, along with gseg, exhibit considerable speed, making them feasible for implementation within reasonable time. However, owing to the recursive calculation of $U$-statistics, Hddc is notably sluggish, making it nearly impractical for implementation on personal laptops.

Table 3: Average computation time (in seconds) across 1000 replications from "Dense Mean" setup with $T=1000$.

| $p$ | gseg | Hddc | Logis | Fnn | Rf |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 500 | $1.473(0.013)$ | $13116.962(36696.262)$ | $0.101(0.031)$ | $2.539(0.351)$ | $0.697(0.013)$ |
| 1000 | $1.476(0.012)$ | $68892.896(87704.009)$ | $0.122(0.036)$ | $2.592(0.338)$ | $1.325(0.020)$ |

To further examine the effectiveness of these approaches, following Chakraborty and Zhang (2021), we use Adjusted Rand Index (ARI) (Morey and Agresti, 1984) to measure the accuracy of the estimated change-points, which is commonly used to evaluate clustering algorithms. In
the context of change-point problems, an ARI close to 0 indicates a larger disparity between the estimated and true change-points or the detection of a change-point without any actual change. Conversely, an ARI of 1 indicates perfect estimation of true change-points. We fix ARI as 0 if no significant change-point is detected.

The empirical performance from 500 Monte Carlo repetitions is depicted in Figure 1 through boxplots. We list our finding as follows. 1) Our proposed methods together with Hddc are powerful in detecting both dense and sparse mean changes, outperforming gseg type methods. 2) The gseg methods lose power in distributional changes, while Hddc worsens when changes occur in dense or banded covariance matrices. This corroborates the findings in Chakraborty and Zhang (2021). 3) The performance of our method is varied; it depends on the chosen classifiers, especially when changes occur in higher-order moments or distributions. In particular, we note that Logis performs well in detecting mean changes only and loses power in other setups. As for Fnn, we find that it is most powerful in detecting changes in dense or banded covariances, while its performance is deteriorated in other settings. We conjecture that this is due to the necessity of certain dependence among the data dimensions for a neural network to train effectively. On the other hand, the performance of Rf is quite robust in all settings; albeit certain power loss in dense covariance changes, it is among the best in all other setups. In summary, if certain prior knowledge of the data is available, our proposed framework can work best when paired with a suitable classification algorithm. On the other hand, in the absence of such knowledge, considering the significant computational burden of Hddc, we recommend using Rf.

### 4.2 Non-Euclidean CIFAR10 Data

In this section, we examine the size and power performance of the proposed method in highdimensional non-Euclidean data. In particular, we detect change-points in artificially constructed sequences of images of various animals (dog, cat, deer, horse, etc) from the CIFAR10 database (Krizhevsky et al., 2009), see Figure 2 for visual illustration. For this purpose, we apply

Methods 追 gseg_orig 官 gseg_maxt 官 Hddc 官 Fnn



Figure 1: Boxplots of ARI values across 500 repetitions. The first and third rows correspond to dimension $p=500$, and the second and fourth rows to dimension $p=1000$, respectively. The columns represent different data-generating processes under consideration. Each of the 16 grouped boxplots contains eight different boxplots arranged horizontally, which correspond to each of the eight methods considered in this paper.
two pre-trained deep convolutional neural network (CNN) classifiers, popular in the machinelearning community:

- vgg16, vgg19: Simonyan and Zisserman (2014) proposed a deep CNN classifier with 1619 hidden layers and a small 3-by-3 convolution filter. In the machine-learning community, it is a common practice to use pre-trained deep CNN classifiers such as vgg16 and vgg19 to classify images in new datasets. Here, we adopt the pre-trained weights from Tensorflow.


Figure 2: RGB 32-by-32 images of a Cat, Deer, Dog and Horse from CIFAR10 Database

To evaluate the size performance, we randomly sample 1000 images of a dog and horse in two separate sequences of images. While for the alternative, we artificially order random images sampled from two different categories. More specifically, for each replication, we randomly choose 500 images of two different animals and arrange them so that the first 500 images correspond to one animal and the next 500 to the other. Hence, the true change-point is located at $t_{0}=500$. We consider three choices for such pairs: (cat, dog), (deer, dog) and (dog, horse).

Out of all the methods considered, only gseg (Chen and Zhang, 2015; Chu and Chen, 2019) can accommodate such non-Euclidean data. To compare the performance, we also used the four graph-based methods: gseg_orig, gseg_wei, gseg_max and gseg_gen.

Table 4 summarizes the performance of our methods and gseg type methods. The first two rows consist of the empirical rejection rate at $5 \%$ significance level when no change-point exists, and the last three rows enlist average ARI across 500 replications when there is a change-point. From the table, we find that size is maintained across all methods. Moreover, the proposed
framework using vgg16 and vgg19 classifiers outperforms in all of the cases, especially in the last case: (Cat $\rightarrow$ Dog). We also find gseg_max and gseg_gen showcase competitive performance when it is comparatively easier to detect changes (Deer $\rightarrow$ Dog, Deer $\rightarrow$ Horse), but loses power in the most difficult scenario (Cat $\rightarrow$ Dog).

Table 4: Size and Power performance of all methods: the first two rows correspond to the size and the last three rows correspond to average ARI values.

|  | Cases | gseg_orig | gseg_wei | gseg_max | gseg_gen | vgg16 | vgg19 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Size | Deer vs Deer | $4.7 \%$ | $4.3 \%$ | $4.9 \%$ | $4.0 \%$ | $4.6 \%$ | $3.6 \%$ |
|  | Dog vs Dog | $4.2 \%$ | $4.2 \%$ | $4.6 \%$ | $4.8 \%$ | $4.6 \%$ | $3.3 \%$ |
| ARI | Cat vs Dog | 0.6295 | 0.3775 | 0.2887 | 0.2256 | 0.9603 | 0.9512 |
|  | Deer vs Dog | 0.9546 | 0.9755 | 0.9755 | 0.9782 | 0.9969 | 0.9957 |
|  | Deer vs Horse | 0.9020 | 0.9697 | 0.9676 | 0.9751 | 0.9939 | 0.9925 |

## 5 Real Data applications

In this section, we present two real data applications and compare the performance of our proposed method with other methods considered in Section 4.

### 5.1 US Stock Market during the Great Recession

Detecting shifts in financial markets is crucial for policymakers and investors. In this section, we apply the proposed methods to the NYSE and NASDAQ stock data from 2005 to 2010 . Our study builds upon Chakraborty and Zhang (2021) where stock price changes of 72 companies under the "Consumer Defensive" sector are analyzed. Here, we expand our focus to a larger dataset comprising daily log returns of 289 companies across the "Healthcare", "Consumer Defensive", and "Utilities" sectors from January 2005 to December 2010. These sectors are identified as "Recession-Proof Industries" during the "Great Recession" from December 2007

Table 5: Estimated change-points (in MM-DD format) of US Stock Data

| Years | 2006 | 2007 | 2008 | 2009 |
| :--- | :--- | :--- | :--- | :--- |
| Rf | $08-09$ | $07-25$ | $09-09$ | $08-07$ |
| Hddc | $08-09$ | $07-25$ | - | $07-13$ |
| gseg_orig | $06-05$ | - | $02-08$ | $03-25$ |
| gseg_wei | $11-29$ | $02-12$ | $05-30$ | $12-02$ |
| gseg_max | $12-18$ | $02-12$ | $05-30$ | $11-19$ |
| gseg_gen | $12-04$ | $02-12,07-16, \quad 10-$ <br> 16 | - | $07-16$ |

to June 2009, a period during which the US Federal Government implemented fiscal stimulus packages to stabilize the economy.

In Table 5, we outline the estimated change-points using Rf, Hddc, and gseg type methods. Each method is embedded into the Seeded Binary Segmentation (Kovács et al., 2023) algorithm to estimate multiple change-points. From the table, we find that our estimated change-points are aligned with important historical dates during the recession. For example, in early August 2007* (identified by 07-25-2007) the market experienced a liquidity crisis, and in September 2008 (identified by 09-09-2008) the international banking crisis happend caused by the bankruptcy of "Lehman Brothers" (Wiggins et al., 2014). The change-points detected by Hddc are rather close to ours albeit a miss in 2008. However, the change-points reported by the gseg methods differ significantly. Given that for stock price data, changes in daily log returns typically manifest in higher-order moments beyond the mean, we conjecture that this discrepancy is due to their impaired performance in estimating distributional changes, as indicated in Section 4.1.

*http://news.bbc.co.uk/1/hi/business/7521250.stm

### 5.2 New York Taxi Trips during the COVID-19 Pandemic

The COVID-19 Pandemic significantly impacted New York State, particularly in early 2020. The state, especially New York City (NYC), became an epicenter for the virus, with strict lockdown measures implemented to curb the spread. This study investigates the impact of several lockdowns enforced in NYC during the COVID-19 pandemic.

We collect For-Hire Vehicle (FHV) Trip records during 2018 and 2022 from the NYC Taxi and Limousine Commission (TLC) Trip Record Database. ${ }^{\dagger}$ These records contain crucial details such as pickup and drop-off times, drop-off location, trip distances, and other information. To harness the geographical insights within the dataset, we employed the name of the borough associated with each drop-off point to generate daily areal heat maps. These heat maps visually depict the estimated spatial density of drop-off counts; see Figure 3 for six such heat-maps. In Chu and Chen (2019), the same data source (during different time horizons and different types of taxi) is analyzed by summarizing the information on the number of taxi drop-offs into a 30 by 30 matrix.

Table 6 showcases the estimated change-points obtained through our method with the vgg16 classifier and gseg type methods as described in Chu and Chen (2019). Notably, the changepoints identified by both methods closely align with each other except for 2021. These significant shifts correspond to events such as the 2019 North American cold wave (2019-01-31), the potential impact of summer vacation (2019-08-31), and the implementation of NYC's first lockdown (2020-03-17). For instance, Figure 3a and 3b depict the areal heat maps on January 15, 2019 (before the heatwave) and February 15, 2019 (after the heatwave), respectively, revealing a noteworthy decrease in taxi usage. Subsequently, areal heat maps in Figure 3c and 3d illustrate an increasing effect on taxi usage following the end of summer vacation. Additionally, Figure $3 \mathrm{e}$ and $3 \mathrm{f}$ present the areal heat maps on March 5, 2020 (before the lockdown) and April 5, 2020 (after the lockdown), respectively, indicating a significant decline in taxi usage.[^0]

(a) $2019-01-15$

(b) 2019-02-15

(c) 2019-08-05

(d) 2019-09-05

(e) 2020-03-05

(f) 2020-04-05

Figure 3: Areal heatmaps of daily taxi trip counts in New York City on six different days before and during the COVID-19 pandemic.

Table 6: Estimated change-points (in MM-DD format) of New York taxi data

| Years | 2018 | 2019 | 2020 | 2021 | 2022 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| vgg16 | - | $01-31,08-31$ | $03-17,11-29$ | $10-31$ | $04-03$ |
| gseg_orig | $09-03$ | $02-28,10-01$ | $06-05,11-26$ | $08-01$ | $04-01$ |
| gseg_wei | - | $01-31,10-01$ | $03-16,08-01$ | $07-01$ | $04-01$ |
| gseg_max | - | $01-31,10-01$ | $03-16,08-01$ | $07-01$ | $04-01$ |
| gseg_gen | - | $01-31,10-01$ | $03-16,08-01$ | $07-01$ | $04-01$ |

## 6 Discussion

In this paper, we propose a novel framework for offline change-point detection based on classifiers. Despite the vast literature on change-point detection, our approach stands out in four key aspects. First, our method is entirely nonparametric, as it does not impose any parametric assumptions on the data distribution or the structure of distributional changes. Second, by leveraging the success of modern classifiers, the proposed framework is widely applicable to diverse data dimensions and types. Third, by selecting an appropriate classifier, prior information can be integrated to enhance the test power. Last but not least, with suitable sample splitting and trimming, the test statistic converges to the supremum of a pivotal Gaussian process, which is independent of the choice of classifier and thus can be easily implemented.

To conclude, we mention a few directions that warrant future investigation. First, it should
be noted that the real data analysis in Section 5 may exhibit temporal dependence. Extending the proposed method to accommodate weakly dependent time series would be an intriguing endeavor. Second, it may be feasible to reduce the computational burden by drawing inspiration from Londschien et al. (2023). Instead of computing the AUC for all potential change-points, it could be computed for initial points, such as the quartiles of the sequence, followed by an extensive search in proximity to the initial candidate change-point that yields the highest AUC. However, exploring the theoretical properties of such a two-stage approach may be challenging. Third, the current setting is unsupervised and, therefore, requires certain sample splitting and trimming; it would be interesting to investigate the asymptotic properties of the test statistic under the supervised setting, as in Li et al. (2024).

## References

Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., Corrado, G. S., Davis, A., Dean, J., Devin, M., et al. (2016). TensorFlow: Large-scale machine learning on heterogeneous systems. arXiv preprint arXiv:1603.04467.

Anastasiou, A. and Fryzlewicz, P. (2022). Detecting multiple generalized change-points by isolating single ones. Metrika, 85(2):141-174.

Andrews, D. W. (1993). Tests for parameter instability and structural change with unknown change point. Econometrica, pages 821-856.

Arlot, S., Celisse, A., and Harchaoui, Z. (2019). A kernel multiple change-point algorithm via model selection. Journal of Machine Learning Research, 20(162):1-56.

Atto, A. M., Bovolo, F., and Bruzzone, L. (2021). Change Detection and Image Time Series Analysis 2: Supervised Methods. John Wiley \& Sons.

Aue, A. and Horváth, L. (2013). Structural breaks in time series. Journal of Time Series Analysis, 34(1):1-16.

Aue, A., Rice, G., and Sönmez, O. (2018). Detecting and dating structural breaks in functional data without dimension reduction. Journal of the Royal Statistical Society Series B: Statistical Methodology, 80(3):509-529.

Avanesov, V. and Buzun, N. (2018). Change-point detection in high-dimensional covariance structure. Electronic Journal of Statistics, 12(2):3254 - 3294.

Berkes, I., Gabrys, R., Horváth, L., and Kokoszka, P. (2009). Detecting changes in the mean of functional observations. Journal of the Royal Statistical Society Series B: Statistical Methodology, 71(5):927-946.

Cai, Z., Lei, J., and Roeder, K. (2022). Model-free prediction test with application to genomics data. Proceedings of the National Academy of Sciences, 119(34):e2205518119.

Cai, Z., Lei, J., and Roeder, K. (2023). Asymptotic distribution-free independence test for high dimension data. Journal of the American Statistical Association, in press.

Chakraborty, S. and Zhang, X. (2021). High-dimensional change-point detection using generalized homogeneity metrics. arXiv preprint arXiv:2105.08976.

Chakravarti, P., Kuusela, M., Lei, J., and Wasserman, L. (2023). Model-independent detection of new physics signals using interpretable semisupervised classifier tests. The Annals of Applied Statistics, 17(4):2759-2795.

Chen, H. and Zhang, N. (2015). Graph-based change-point detection. The Annals of Statistics, 43(1):139- 176.

Chen, J. and Gupta, A. K. (2012). Parametric statistical change point analysis: with applications to genetics, medicine, and finance. Springer.

Cho, H. and Fryzlewicz, P. (2015). Multiple-change-point detection for high dimensional time series via sparsified binary segmentation. Journal of the Royal Statistical Society Series B: Statistical Methodology, 77(2):475-507.

Chu, L. and Chen, H. (2019). Asymptotic distribution-free change-point detection for multivariate and non-Euclidean data. The Annals of Statistics, 47(1):382 - 414.

Dette, H., Pan, G., and Yang, Q. (2022). Estimating a change point in a sequence of very high-dimensional covariance matrices. Journal of the American Statistical Association, 117(537):444-454.

Dubey, P. and Müller, H.-G. (2020). Fréchet change-point detection. The Annals of Statistics, 48(6):3312-3335.

Dubey, P. and Zheng, M. (2023). Change point detection for random objects using distance profiles. arXiv preprint arXiv:2311.16025.

Enikeeva, F. and Harchaoui, Z. (2019). High-dimensional change-point detection under sparse alternatives. The Annals of Statistics, 47(4):2051 - 2079.

Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8):861874.

Friedman, J., Hastie, T., and Tibshirani, R. (2010). Regularization paths for generalized linear models via coordinate descent. Journal of Statistical Software, 33(1):1-22.

Fryzlewicz, P. (2014). Wild binary segmentation for multiple change-point detection. The Annals of Statistics, 42(6):2243 - 2281.

Gao, H., Wang, R., and Shao, X. (2023). Dimension-agnostic change point detection. arXiv preprint arXiv:2303.10808.

Harchaoui, Z. and Cappé, O. (2007). Retrospective mutiple change-point estimation with kernels. 2007 IEEE/SP 14th Workshop on Statistical Signal Processing, pages 768-772.

Hu, X. and Lei, J. (2023). A two-sample conditional distribution test using conformal prediction and weighted rank sum. Journal of the American Statistical Association, in press.

Jiang, F., Zhu, C., and Shao, X. (2024). Two-sample and change-point inference for noneuclidean valued time series. Electronic Journal of Statistics, in press.

Jiao, S., Frostig, R. D., and Ombao, H. (2023). Break point detection for functional covariance. Scandinavian Journal of Statistics, 50(2):477-512.

Jirak, M. (2015). Uniform change point tests in high dimension. The Annals of Statistics, $43(6): 2451-2483$.

Kaul, A., Jandhyala, V. K., and Fotopoulos, S. B. (2019). An efficient two step algorithm for high dimensional change point regression models without grid search. Journal of Machine Learning Research, 20:1-40.

Kim, I., Lee, A. B., and Lei, J. (2019). Global and local two-sample tests via regression. Electronic Journal of Statistics, 13:5253-5305.

Kim, I., Ramdas, A., Singh, A., and Wasserman, L. (2021). Classification accuracy as a proxy for two sample testing. The Annals of Statistics, 49(1):411-434.

Kirchler, M., Khorasani, S., Kloft, M., and Lippert, C. (2020). Two-sample testing using deep learning. In Chiappa, S. and Calandra, R., editors, Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, volume 108 of Proceedings of Machine Learning Research, pages 1387-1398. PMLR.

Kovács, S., Bühlmann, P., Li, H., and Munk, A. (2023). Seeded binary segmentation: a general methodology for fast and optimal changepoint detection. Biometrika, 110(1):249-256.

Krizhevsky, A., Nair, V., and Hinton, G. (2009). CIFAR-10 (canadian institute for advanced research).

Lee, J., Xie, Y., and Cheng, X. (2023). Training neural networks for sequential change-point detection. In IEEE ICASSP 2023, pages 1-5. IEEE.

Li, J., Fearnhead, P., Fryzlewicz, P., and Wang, T. (2024). Automatic change-point detection in time series via deep learning. Journal of the Royal Statistical Society Series B: Statistical Methodology, in press.

Li, Y.-N., Li, D., and Fryzlewicz, P. (2023). Detection of multiple structural breaks in large covariance matrices. Journal of Business 8 Economic Statistics, 41(3):846-861.

Liaw, A. and Wiener, M. (2002). Classification and regression by randomforest. $R$ News, $2(3): 18-22$.

Liu, B., Zhou, C., Zhang, X., and Liu, Y. (2020). A unified data-adaptive framework for high dimensional change point detection. Journal of the Royal Statistical Society Series B: Statistical Methodology, 82(4):933-963.

Londschien, M., Bühlmann, P., and Kovács, S. (2023). Random forests for change point detection. Journal of Machine Learning Research, 24(216):1-45.

Lopez-Paz, D. and Oquab, M. (2016). Revisiting classifier two-sample tests. International Conference on Learning Representations, arXiv preprint arXiv:1610.06545.

Matteson, D. S. and James, N. A. (2014). A nonparametric approach for multiple change point analysis of multivariate data. Journal of the American Statistical Association, 109(505):334345.

Morey, L. C. and Agresti, A. (1984). The measurement of classification agreement: An adjust-
ment to the Rand statistic for chance agreement. Educational and Psychological Measurement, $44: 33-37$.

Page, E. S. (1954). Continuous inspection schemes. Biometrika, 41(1/2):100-115.

Simonyan, K. and Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556.

Steland, A. (2019). Testing and estimating change-points in the covariance matrix of a highdimensional time series. Journal of Multivariate Analysis, 177:104582.

Truong, C., Oudre, L., and Vayatis, N. (2020). Selective review of offline change point detection methods. Signal Processing, 167:107299.

Vaart, A. v. d. and Wellner, J. A. (2023). Empirical processes. In Weak Convergence and Empirical Processes: With Applications to Statistics, pages 127-384. Springer.

Wang, R., Zhu, C., Volgushev, S., and Shao, X. (2022). Inference for change points in highdimensional data via selfnormalization. The Annals of Statistics, 50(2):781-806.

Wang, T. and Samworth, R. J. (2018). High dimensional change point estimation via sparse projection. Journal of the Royal Statistical Society Series B: Statistical Methodology, 80(1):5783.

Wiggins, R., Piontek, T., and Metrick, A. (2014). The lehman brothers bankruptcy a: overview. Yale program on financial stability case study.

Yu, M. and Chen, X. (2020). Finite sample change point inference and identification for highdimensional mean vectors. Journal of the Royal Statistical Society Series B: Statistical Methodology, 83(2):247-270.

Zou, C., Yin, G., Feng, L., and Wang, Z. (2014). Nonparametric maximum likelihood approach to multiple change-point problems. The Annals of Statistics, 42(3):970 - 1002.


[^0]:    †https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

