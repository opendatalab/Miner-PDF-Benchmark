# Covariance Regression with High-Dimensional Predictors 

Yuheng He ${ }^{1}$, Changliang Zou $^{1}$, and Yi Zhao ${ }^{2}$<br>${ }^{1}$ School of Statistics and Data Science, Nankai University, Tianjin, China<br>${ }^{2}$ Department of Biostatistics and Health Data Science,<br>Indiana University School of Medicine, USA


#### Abstract

In the high-dimensional landscape, addressing the challenges of covariance regression with highdimensional covariates has posed difficulties for conventional methodologies. This paper addresses these hurdles by presenting a novel approach for high-dimensional inference with covariance matrix outcomes. The proposed methodology is illustrated through its application in elucidating brain coactivation patterns observed in functional magnetic resonance imaging (fMRI) experiments and unraveling complex associations within anatomical connections between brain regions identified through diffusion tensor imaging (DTI). In the pursuit of dependable statistical inference, we introduce an integrative approach based on penalized estimation. This approach combines data splitting, variable selection, aggregation of lowdimensional estimators, and robust variance estimation. It enables the construction of reliable confidence intervals for covariate coefficients, supported by theoretical confidence levels under specified conditions, where asymptotic distributions are provided. Through various types of simulation studies, the proposed approach performs well for covariance regression in the presence of high-dimensional covariates. This innovative approach is applied to the Lifespan Human Connectome Project (HCP) Aging Study, which aims to uncover a typical aging trajectory and variations in the brain connectome among mature and older adults. The proposed approach effectively identifies brain networks and associated predictors of white matter integrity, aligning with established knowledge of the human brain.


Keywords: Covariance regression; Confidence interval; High-dimensional covariates; Penalized estimation, Variance estimation.

## 1 Introduction

This manuscript investigates a high-dimensional regression problem with covariance matrices as the outcome. Assume the observed outcome data consist of $n$ subjects, each with $T_{i}$ observations of a $p$-dimensional random vector, denote as $\mathbf{y}_{i t} \in \mathbb{R}^{p}$, for $t=1, \ldots, T_{i}$ and $i=1, \ldots, n$. Let $\mathbf{Y}_{i}=\left(\mathbf{y}_{i 1}, \ldots, \mathbf{y}_{i T_{i}}\right)^{\top} \in \mathbb{R}^{T_{i} \times p}$ and $\mathbf{Y}=\left\{\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{n}\right\}$. The distribution of $\mathbf{y}_{i t}$ is assumed to be multivariate normal with mean zero and covariance matrix $\boldsymbol{\Sigma}_{i}$. Without loss of generality, the distribution mean is set to zero as the focus of the study is on the covariance matrices. Let $\tilde{\mathbf{x}}_{i} \in \mathbb{R}^{q-1}$ denote the $(q-1)$ dimensional covariates of interest acquired from subject $i$. Denote $\mathbf{x}_{i}=\left(1, \tilde{\mathbf{x}}_{i}^{\top}\right)^{\top} \in \mathbb{R}^{q}$ the vector that includes the intercept term and $\mathbf{X}=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)^{\top} \in \mathbb{R}^{n \times q}$

The term "high-dimensional covariance" pertains to scenarios where $q>n$ and $q$ increases toward infinity. For covariance matrix outcomes, the following regression model introduced in Zhao et al. (2021) is considered. Assuming there is a linear projection, the study proposed a parsimonious model in the projection space that accounts for data heteroscedasticity via a generalized linear regression model with a logarithmic link function,

$$
\log \left(\boldsymbol{\gamma}^{\top} \boldsymbol{\Sigma}_{i} \boldsymbol{\gamma}\right)=\beta_{0}+\tilde{\mathbf{x}}_{i}^{\top} \boldsymbol{\beta}_{1} \equiv \mathbf{x}_{i}^{\top} \boldsymbol{\beta}
$$

where $\boldsymbol{\gamma} \in \mathbb{R}^{p}$ is a linear projection and $\boldsymbol{\beta}=\left(\beta_{0}, \boldsymbol{\beta}_{1}^{\top}\right)^{\top} \in \mathbb{R}^{q}$ corresponds to the model coefficients. The use of the logarithmic link ensures the positive definiteness of the covariance matrices. The primary goal is to estimate both $\boldsymbol{\gamma}$ and $\boldsymbol{\beta}$ using the observed data, $\left\{\left(\mathbf{y}_{i 1}, \ldots, \mathbf{y}_{i T_{i}}\right), \mathbf{x}_{i}\right\}_{i=1}^{n}$.

This regression framework finds practical application in various domains. One notable context is its utilization for investigating the impact of covariates on brain synchronization measured by resting-state

functional magnetic resonance imaging (fMRI) experiments. In the realm of fMRI studies, the utilization of covariance or correlation matrices derived from resting-state signals serves as a common approach to unveil intrinsic brain coactivation patterns. Exploring the interplay between these patterns and population or individual-level covariates emerges as a significant avenue of exploration within the field of neuroimaging research (Mueller et al., 2013; Seiler and Holmes, 2017; Zhao et al., 2021). A parallel application of this framework emerges within the realm of financial equities analysis. Consider a dataset comprising stock values, where covariance matrices calculated over specific time intervals provide insights into the level of co-movement or synchronicity among these stocks. This synchronicity is notably influenced by pertinent attributes at both the firm and market levels, including factors such as industry categorization, the firm's cash flow, stock size, and book-to-market ratio. The assessment and quantification of these intricate associations represent pivotal pursuits within the domain of financial theory (Zou et al., 2017).

For a covariance regression model as in (1), when $q$ is less than $n$ and fixed, Zhao et al. (2021) conducted an initial investigation, wherein a novel approach of estimating $\gamma$ and $\boldsymbol{\beta}$ was introduced. This approach was grounded in likelihood principles, where iterations took place between minimizing the negative log-likelihood function within the projection space (fix $\gamma$ ) and optimizing for the projection (fix $\boldsymbol{\beta}$ ) with a quadratic constraint. It is worth noting that the optimization is applicable when the covariance matrix of the design
matrix, $\mathbb{E}\left(\mathbf{x}_{i} \mathbf{x}_{i}^{\top}\right)$, is invertible. Consequently, when $q>n$, the above-mentioned approach becomes ill-defined, primarily attributed to the rank deficiency in the covariance matrix of the covariates. Recently, Kim and Zhang (2024) investigated a covariance regression model that accommodates high-dimensional covariates. They modeled $\boldsymbol{\Sigma}$ as a quadratic function of covariates $\mathbf{x}$, expressed as $\boldsymbol{B} \mathbf{x x}^{\top} \boldsymbol{B}^{\top}$, where $\boldsymbol{B} \in \mathbb{R}^{p \times q}$. However, as the covariance matrix is modeled as a linear function of covariates with matrix-valued coefficients, it primarily addresses a multivariate linear regression problem, which may be less pertinent to the context under discussion here.

When encountering problems with high-dimensional covariates, one typical solution is to consider regularized estimation, including the LASSO (Tibshirani, 1996), the elastic net (Zou and Hastie, 2005), the adaptive LASSO (Zou, 2006), SCAD (Fan and Li, 2001), MCP (Zhang, 2010), ISIS (Fan and Lv, 2008), and among others. Asymptotic properties, including model selection consistency and estimation consistency, under various conditions and regularization functions, have been established (see a review by Bühlmann and Van De Geer, 2011). Besides point estimation, achieving reliable inferences in high-dimensional models is also fundamental to the field. Researchers have approached this challenge from various angles. One primary direction involves making inferences based on the selected model chosen by a particular variable selection procedure. Wasserman and Roeder (2009) introduced a multi-stage procedure that employs data splitting to separate the steps of selection and inference. Lee et al. (2016) developed conditional asymptotics for coefficient estimates conditional on the selected model. Another direction centers on estimating and making inferences about low-dimensional parameters within high-dimensional models. Belloni et al. (2014) proposed a double selection procedure that involves multiple steps, rather than a single selection, to estimate and construct confidence regions for a primary regression parameter of interest. Some alternative approaches are based on penalized estimation. Notably, the bias correction method was introduced based on the LASSO proposed by Javanmard and Montanari (2014); Van de Geer et al. (2014); Zhang and Zhang (2014), which provides both point estimates and confidence intervals for model parameters. Ning and Liu (2017) introduced hypothesis tests and confidence regions based on the decorrelated score function and test statistic.

Each of the above-mentioned approaches has its strengths and limitations. Some methods, such as Van de Geer et al. (2014), require precisely estimating the precision matrix of $\mathbf{x}$, which is the inverse of a $q \times q$ dimensional covariance matrix, imposing a large computational burden and the assumption of sparsity in GLMs that is sometimes violated (Xia et al., 2020). Other methods, such as Wasserman and Roeder (2009) and Lee et al. (2016), aim for exact inference in post-selection estimates while being constrained to the correctness of model selection in the initial step. In this study, we incorporate a newly developed approach proposed by (Fei and Li, 2021) to our scenario, which utilizes sample splitting for inference with highdimensional covariates. This approach tackles the high-dimensional estimation challenge by aggregating low-dimensional estimates, thus overcoming computational complexity issues. Importantly, the method avoids making parameter assumptions in variance estimation and does not require consistency in model selection.

The proposed covariance regression with high-dimensional covariates has two steps.

1. Penalized estimation. It starts with estimating model parameters, $\gamma$, and $\boldsymbol{\beta}$, using the full dataset with regularization on the high-dimensional coefficient, $\boldsymbol{\beta}$.
2. High-dimensional inference. This step employs a data splitting procedure, which divides the samples into two distinct subsets, one for dimension reduction and one for low-dimensional model fitting.

The proposal is a comprehensive framework that enables estimating coefficients efficiently, conducting variable selection, and obtaining coefficient estimates for both selected and non-selected predictors. This approach addresses the intricacies of high-dimensional covariance regression and enhances the ability to draw meaningful inferences from the data. A pivotal assumption underlying the proposed approach is that the number of non-zero elements in the true $\boldsymbol{\beta}$ is small, that is the sparsity assumption. This assumption is in line with practical implementations. For instance, the small-world topology in brain science, where human brain anatomy is economically organized (Bullmore and Sporns, 2012) and information processing is often highly clustered and concentrated (Bassett and Bullmore, 2017). Another example is in the field of cancer genomics, it is plausible that a specific type of cancer is primarily associated with only a handful of oncogenes and tumor suppressor genes. For inference, the proposed approach is inspired by the work of Fei and Li (2021), where a Splitting and Smoothing method for Generalized Linear Models (GLMs) was introduced and effectiveness under mild conditions was demonstrated. This compelling property motivates us to adapt and generalize to models with covariance outcomes, opening new avenues for statistical inference in covariance regression with high-dimensional covariates.

The contributions of this study can be summarized into three key aspects.

- Penalized estimation and inference for covariance regression. To our best knowledge, this is the first attempt to delve into penalized estimation and statistical inference for covariance regression under the setting of high-dimensional covariates. This pioneering work lays the foundation for addressing complex problems involving high-dimensional data and covariance matrices.
- Aggregation of low-dimensional modeling. The proposed approach tackles the challenges of high-dimensional inference by aggregating low-dimensional modeling. It significantly improves computational effectiveness compared to existing approaches, enables efficient handling of high-dimensional data, and obtains more robust estimates.
- Robust variance estimation. To ensure reliable inference, a variance estimator is developed, which utilizes the infinitesimal jackknife method following the splitting and smoothing procedure. This variance estimation approach is free from parametric assumptions, a notable advantage, and results in confidence intervals with correct coverage probabilities.

The rest of the paper is organized as follows. Section 2 introduces the proposed penalized estimator of model coefficients and imposed assumptions for estimation and inference and studies the asymptotic
properties. In Section 3, a Splitting and Smooth method for statistical inference is introduced and asymptotic properties are derived. Section 4 demonstrates the good performance of the proposed approach via simulation studies. Section 5 articulates an application to the Lifespan Human Connectome Project (HCP) Aging Study. Section 6 summarizes the manuscript with discussions. The supporting information also collects the technical proof of the theorems in the main text, additional theoretical results, and additional data analysis results.

## 2 Estimation

### 2.1 Method

Given the regression model (1), it is proposed that an estimation of the parameters can be obtained by solving the following optimization problem. Specifically, the optimization problem is formulated to minimize the regularized negative likelihood function:

$$
\begin{array}{ll}
\underset{\boldsymbol{\beta}, \boldsymbol{\gamma}}{\operatorname{minimize}} & \ell(\boldsymbol{\beta}, \boldsymbol{\gamma}):=\frac{1}{2} \sum_{i=1}^{n} T_{i}\left\{\left(\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)+\boldsymbol{\gamma}^{\top} \hat{\boldsymbol{\Sigma}}_{i} \boldsymbol{\gamma} \cdot \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\right\}+\lambda\|\boldsymbol{\beta}\|_{1} \\
\text { such that } & \boldsymbol{\gamma}^{\top} \mathbf{H} \boldsymbol{\gamma}=1
\end{array}
$$

One may express the objective function as $\ell(\boldsymbol{\beta}, \boldsymbol{\gamma})=\mathcal{L}_{n}(\boldsymbol{\beta}, \boldsymbol{\gamma})+\mathcal{P}(\boldsymbol{\beta})$, wherein the first component denotes the negative log-likelihood and the second denotes the regularization.

The first component employs an estimator, denoted by $\hat{\boldsymbol{\Sigma}}_{i}$, to approximate the true covariance matrix, $\boldsymbol{\Sigma}_{i}$. Under the normally assumption and likelihood criterion, $\hat{\boldsymbol{\Sigma}}_{i}=\mathbf{S}_{i}=\sum_{t=1}^{T_{i}} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} / T_{i}$ is the sample covariance matrix as introduced in Zhao et al. (2021). To identify $\gamma$, a quadratic constraint concerning a positive definite matrix $(\mathbf{H})$ is necessary, analogous to the principal component analysis (PCA) principle. With a likelihood-based objective function, $\mathbf{H}$ is set to be the average of the $\hat{\boldsymbol{\Sigma}}_{i}$ 's with $\mathbf{H}=\sum_{i=1}^{n} T_{i} \hat{\boldsymbol{\Sigma}}_{i} / \sum_{i=1}^{n} T_{i}$ to incorporate distributional information (see also the discussion in Zhao et al., 2021).

When the value of $q$ significantly exceeds that of $n$ (a high-dimensional scenario), the problem becomes challenging due to the rank deficiency of the design matrix. To address this issue, a regularization component, $\mathcal{P}(\boldsymbol{\beta})$, is introduced. Examples include the $\ell_{1}$-regularization (Tibshirani, 1996) and its extensions. Existing findings also guarantee both estimation consistency and selection consistency under mild conditions. A generalization to the current model setting with covariance matrices as the outcome will be comprehensively discussed in Section 2.2.

The present study considers an optimization problem of (2), which exhibits biconvexity. Following the approach utilized in Zhao et al. (2021), we consider a high-dimensional block coordinate descent algorithm that is well-suited for fitting model parameters, $\boldsymbol{\gamma}$ and $\boldsymbol{\beta}$. The procedure is described in Algorithm 1. To enhance the likelihood of escaping from local minima, we recommend adopting a randomized approach to selecting initial values, followed by selecting the estimate that yields the lowest value of the objective function.

Similar to Algorithm 2 in Zhao et al. (2021), when there are higher-order components, it is possible to first remove the identified components and utilize the updated data for estimating the succeeding component. This estimation involves incorporating an orthogonality constraint, ensuring the newfound component is orthogonal to the previously identified ones. To determine the number of projections, the same metric introduced by Zhao et al. (2021) is utilized, which quantifies the "deviation from diagonality" of the projected matrices. Let $\Gamma^{(k)} \in \mathbb{R}^{p \times k}$ denote the first $k$ estimated components, the average deviation from diagonality is defined as

$$
\operatorname{DfD}\left(\Gamma^{(k)}\right)=\prod_{i=1}^{n}\left(\frac{\operatorname{det}\left\{\operatorname{diag}\left(\Gamma^{(k) \top} \mathbf{S}_{i} \Gamma^{(k)}\right)\right\}}{\operatorname{det}\left(\Gamma^{(k) \top} \mathbf{S}_{i} \Gamma^{(k)}\right)}\right)^{T_{i} / \sum_{i} T_{i}}
$$

where $\operatorname{diag}(\mathbf{A})$ represents a diagonal matrix comprising the diagonal elements of a square matrix $\mathbf{A}$, and $\operatorname{det}(\mathbf{A})$ is the determinant of $\mathbf{A}$. If $\Gamma^{(k)}$ is a shared diagonalization of $\mathbf{S}_{i}$ 's, meaning $\Gamma^{(k) \top} \mathbf{S}_{i} \Gamma^{(k)}$ is a diagonal matrix, for $\forall i=1, \ldots, n$, then $\operatorname{DfD}\left(\Gamma^{(k)}\right)=1$. In practice, the selection of $k$ can occur before DfD significantly deviates from one or before a sudden increase takes place.

Algorithm 1 The optimization algorithm for problem (2).

Input: Y: a list of data where the $i$ th element a $T_{i} \times p$ data matrix;

X: an $n \times q$ matrix of covariates with the first column of ones.

1: Initialization: $\boldsymbol{\beta}^{(0)}, \boldsymbol{\gamma}^{(0)}$

2: repeat for iteration $s=0,1,2, \ldots$, given $\left(\boldsymbol{\beta}^{(s)}, \gamma^{(s)}\right)$, for the $(s+1)$ th step:

(1) update $\boldsymbol{\beta}$ by solving

$$
\frac{1}{2} \sum_{i=1}^{n} T_{i}\left\{\left(\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)+\gamma^{(s)^{\top}} \mathbf{S}_{i} \gamma^{(s)} \cdot \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\right\}+\lambda\|\boldsymbol{\beta}\|_{1}
$$

4: $\quad(2)$ update $\gamma$ by solving

$$
\begin{array}{ll}
\underset{\gamma}{\operatorname{minimize}} & \boldsymbol{\gamma}^{\top}\left\{\frac{1}{2} \sum_{i=1}^{n} T_{i} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}^{(s+1)}\right) \mathbf{S}_{i}\right\} \boldsymbol{\gamma} \\
\text { such that } & \boldsymbol{\gamma}^{\top} \mathbf{H} \boldsymbol{\gamma}=1
\end{array}
$$

until the objective function in (2) converges.

Consider a random series of initializations, repeat Steps 1-5, and choose the results with the minimum objective value.

Output: $\hat{\boldsymbol{\beta}}, \hat{\gamma}$

### 2.2 Asymptotic properties

In this section, we establish the estimation consistency and model selection consistency of the proposed approach. We denote the true model parameter as $\boldsymbol{\beta}^{*}$ and the model space under regularization $\mathcal{P}$ (for example, the $\ell_{1}$-norm) as $\mathcal{M}=\left\{\boldsymbol{\beta} \in \mathbb{R}^{p} \mid(\boldsymbol{\beta})_{S^{c}}=\mathbf{0}\right\}$, where $S$ is the support of $\boldsymbol{\beta}^{*}$ and $S^{c}$ is the complement
of $S$. To ensure the desired theoretical properties, we impose the following regularity conditions.

(A1) (Bounded observations) For a random feature vector $\tilde{\mathbf{x}} \in \mathbb{R}^{q-1},\|\tilde{\mathbf{x}}\|_{\infty} \leq C_{0}$ and $\mathbb{E}(|\mathbf{Y}|)<\infty$.

(A2) (Bounded eigenvalues) The eigenvalues of $\Omega=\mathbb{E}\left(\mathbf{x}_{i} \mathbf{x}_{i}^{\top}\right)$, denoted as $\mu(\Omega)$, are bounded below and above by constants $c_{\min }, c_{\max }$, such that

$$
0<c_{\min } \leq \mu_{\min }(\Omega)<\mu_{\max }(\Omega) \leq c_{\max }<\infty
$$

(A3) (Irrepresentability) For $\tau \in(0,1)$,

$$
\left\|\mathbf{X}_{S^{c}}^{\top}\left(\mathbf{X}_{S}^{\top}\right)^{\dagger} \operatorname{sign}\left(\boldsymbol{\beta}_{S}^{*}\right)\right\|_{\infty} \leq 1-\tau
$$

where $\mathbf{X}=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)^{\top} \in \mathbb{R}^{n \times q}, \mathbf{X}_{S^{c}}$ is the columns of $\mathbf{X}$ in $S^{c}, \mathbf{X}_{S}$ is the columns of $\mathbf{X}$ in $S$, and $\boldsymbol{\beta}_{S}^{*}$ is the corresponding elements of $\boldsymbol{\beta}^{*}$ in $S$. For a matrix $\mathbf{A} \in \mathbb{R}^{p \times p}, \mathbf{A}^{\dagger}$ is Moore-Penrose pseudoinverse and $\operatorname{sign}(\cdot)$ is the sign function.

(A4) (Common eigenstructure) All the covariance matrices share the same set of eigenvectors, denoted as $\Gamma_{i}$ and $\Gamma_{i}=\Gamma$, for $i=1, \ldots, n$. For each $\boldsymbol{\Sigma}_{i}$, there exists (at least) a column, indexed by $j_{i}$, such that $\gamma=\gamma_{i j_{i}}$ and Model (1) is satisfied.

The random design assumption postulated in Assumption (A1) is a fundamental and prevalent condition in the literature (Song et al., 2020). Additionally, it is reasonable to restrict the range of predictors via appropriate data preprocessing techniques. Assumption (A2) regulates the covariance matrix of $\mathbf{x}$, denoted as $\Omega$. It also serves as the expected Hessian matrix of the considered objective function, which is likelihoodbased. Assumption (A2) is a standard regularity condition, requiring that the eigenvalues of the expected Hessian matrix remain bounded away from zero and infinity. This condition is necessary to guarantee the existence of the maximum likelihood estimate and to ensure the stability of the optimization algorithm. Assumption (A3) pertains to the irrepresentability condition which necessitates that active predictors are not excessively aligned with inactive predictors. Ideally, the inactive predictors are orthogonal to the active predictors. However, the high dimensionality of the data makes this an impractical assumption. Therefore, Assumption (A3) relaxes the orthogonality requirement to near-orthogonality, enabling greater flexibility in model specification. Assumption (A4) posits that all covariance matrices share an identical eigenspace, irrespective of the order. For $i=1, \ldots, n$, it is assumed that $\boldsymbol{\Sigma}_{i}$ has the eigendecomposition of $\boldsymbol{\Sigma}_{i}=\Gamma_{i} \Lambda_{i} \Gamma_{i}^{\top}$, where $\Lambda_{i}=\operatorname{diag}\left\{\lambda_{i 1}, \ldots, \lambda_{i p}\right\}$ is a diagonal matrix and $\Gamma_{i}=\left(\gamma_{i 1}, \ldots, \gamma_{i p}\right)$ is an orthonormal rotation matrix; $\left\{\lambda_{i 1}, \ldots, \lambda_{i p}\right\}$ are the eigenvalues and the columns of $\Gamma_{i}$ are the corresponding eigenvectors. Under Assumption (A4), we investigate the theoretical outcomes of the proposed method under the assumption of common principal components.

To begin with, we aim to establish a connection between Assumptions (A1), (A2), and the well-known condition of Restricted Strong Convexity (RSC) introduced by Negahban et al. (2012). The basic concept
underlying the definition of RSC is the relaxation of strong convexity, which is unable to hold under the highdimensional setting due to rank deficiency, resulting in vanishing curvature of $\mathcal{L}_{n}$ along certain directions. The RSC condition ensures the availability of gradient information for the algorithm to navigate towards the optimal solution $\boldsymbol{\beta}^{*}$ despite the absence of strong convexity.

Proposition 1. Assume Assumptions (A1) and (A2) are satisfied and $q \gg n$ and $\log q / M_{n}=o(1)$, where $M_{n}=\sum_{i=1}^{n} T_{i}$. Then for any given $\epsilon>0$, there exist positive constants $\alpha_{1}, \alpha_{2}$, and $C$ such that for $n \geq C \log (1 / \epsilon)$, it holds with probability at least $1-\epsilon$ that

$$
\left(\nabla \mathcal{L}_{n}(\boldsymbol{\beta})-\nabla \mathcal{L}_{n}\left(\boldsymbol{\beta}^{*}\right)\right)^{\top}\left(\boldsymbol{\beta}-\boldsymbol{\beta}^{*}\right) \geq \alpha_{1}\left\|\boldsymbol{\beta}-\boldsymbol{\beta}^{*}\right\|_{2}^{2}-\alpha_{2} \sqrt{\frac{\log q}{M_{n}}}\left\|\boldsymbol{\beta}-\boldsymbol{\beta}^{*}\right\|_{1}^{2}, \quad \forall \boldsymbol{\beta} \in \mathbb{B}_{2}\left(r ; \boldsymbol{\beta}^{*}\right)
$$

where $\mathbb{B}_{2}\left(r ; \boldsymbol{\beta}^{*}\right)$ is a compact region containing $\boldsymbol{\beta}^{*}$ with radius $r$. Inequality (3) is the restricted strong convexity.

Then We first discuss the asymptotic property of our $\boldsymbol{\beta}$ estimator given the true $\boldsymbol{\gamma}$. Incorporating the RSC and Assumption (A3), the present study advances a novel theorem that closely resembles Theorem 3.4 in Lee et al. (2015).

Theorem 2. Under RSC and Assumption (A3), for some $\tau$ defined in Assumption (A3), constants $\kappa, c_{1}, c_{2}$ and $\lambda=\left(3 \kappa c_{1} / \tau\right) \sqrt{\log q / c_{2} M_{n}}$ with $M_{n}=\sum_{i=1}^{n} T_{i}$, the estimator of $\boldsymbol{\beta}$ under $\mathcal{P}$ is unique, and with probability at least $1-2 q^{-5 / 4}$,

(1) estimation consistent:

$$
\left\|\hat{\boldsymbol{\beta}}-\boldsymbol{\beta}^{*}\right\|_{2} \leq \frac{6}{\alpha_{1}} \frac{\kappa}{\tau} c_{1}\left(\sqrt{|S|}+\frac{\tau}{2 \kappa} \sqrt{|S|}\right) \sqrt{\frac{\log q}{c_{2} M_{n}}}
$$

(2) model selection consistent:

$$
\hat{\boldsymbol{\beta}} \in \mathcal{M}
$$

where $|S|$ is the cardinality of set $S$.

The proof of Theorem 2 and values of $\kappa$ are provided in Supporting Information Section A.3.

### 2.3 Extension

In practice, based on domain knowledge, structural constraints on the predictors are sometimes enforced, instead of imposing pure sparsity. Assuming the predictor structure can be captured by a matrix $\mathbf{D} \in \mathbb{R}^{r \times q}$, where $r$ is the number of structural constraints, the imposed regularization is then $\mathcal{P}(\boldsymbol{\beta})=\|\mathbf{D} \boldsymbol{\beta}\|_{1}$. We refer to these problems as the generalized lasso (Tibshirani and Taylor, 2011). Example choices of $\mathbf{D}$ include the fused lasso, trend filtering, wavelet smoothing, and a method for outlier detection. In our neuroimaging application, the goal is to evaluate whether brain white matter integrity regulates brain functional connectivity. Local constancy and smoothness within each functional module are imposed on the structural imaging data (Grosenick et al., 2013), and the fused lasso regularization is particularly well-suited.

We consider the following optimization problem under structured constraints.

$$
\begin{aligned}
\underset{\boldsymbol{\beta}, \boldsymbol{\gamma}}{\operatorname{minimize}} & \ell(\boldsymbol{\beta}, \boldsymbol{\gamma})=\frac{1}{2} \sum_{i=1}^{n} T_{i}\left\{\left(\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)+\boldsymbol{\gamma}^{\top} \mathbf{S}_{i} \boldsymbol{\gamma} \cdot \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\right\}+\lambda\|\mathbf{D} \boldsymbol{\beta}\|_{1} \\
\text { such that } & \boldsymbol{\gamma}^{\top} \mathbf{H} \boldsymbol{\gamma}=1
\end{aligned}
$$

When the matrix $\mathbf{D}$ is invertible, let $\boldsymbol{\theta} \equiv \mathbf{D} \boldsymbol{\beta}\left(\boldsymbol{\beta}=\mathbf{D}^{-1} \boldsymbol{\theta}\right)$, it reparameterizes the problem with $\boldsymbol{\theta}$ and the same approaches can be utilized followed by the asymptotic consistency. When $\mathbf{D}$ is not invertible, to guarantee the theoretical properties of the generalized lasso, an adapted version of the third condition (A3) is introduced.

Let $\boldsymbol{\beta}^{*}$ denote the true model parameter and $\mathcal{M}^{\prime}=\left\{\boldsymbol{\beta} \in \mathbb{R}^{q} \mid(\mathbf{D} \boldsymbol{\beta})_{S^{\prime c}}=0\right\}$ denote the model space under regularization $\mathcal{P}(\boldsymbol{\beta})=\|\mathbf{D} \boldsymbol{\beta}\|_{1}$, where $S^{\prime}$ is the support of $\mathbf{D} \boldsymbol{\beta}^{*}$ and $S^{\prime c}$ is the complement of $S^{\prime}$. The following irrepresentability condition is assumed.

$\left(\mathrm{A} 3^{\prime}\right)$ (Irrepresentability) For $\tau \in(0,1)$

$$
\left\|\mathbf{D}_{S^{\prime}} \mathbf{X}^{\top}\left(\mathbf{D}_{S^{\prime}} \mathbf{X}^{\top}\right)^{\dagger} \operatorname{sign}\left\{\left(\mathbf{D} \boldsymbol{\beta}^{*}\right)_{S^{\prime}}\right\}\right\|_{\infty} \leq 1-\tau
$$

This adapted version of the irrepresentability condition requires that the active predictors, concerning $\mathbf{D}$, should not be overly well-aligned with the inactive predictors. The following theorem is an analogy to Theorem 2 for the generalized lasso.

Theorem 3. Under RSC and Assumption ( $A 3^{\prime}$ ), for some $\tau$ defined in Assumption ( $A 3^{\prime}$ ), constants $\kappa^{\prime}, c_{1}^{\prime}, c_{2}^{\prime}$ and $\lambda=\left(3 \kappa^{\prime} c_{1}^{\prime} / \tau\right) \sqrt{\log q / c_{2}^{\prime} M_{n}}$ with $M_{n}=\sum_{i=1}^{n} T_{i}$, the estimator of $\boldsymbol{\beta}$ under $\mathcal{P}$ is unique, and with probability at least $1-2 q^{-5 / 4}$,

(1) estimation consistent:

$$
\left\|\hat{\boldsymbol{\beta}}-\boldsymbol{\beta}^{*}\right\|_{2} \leq \frac{6}{\alpha_{1}} \frac{\kappa^{\prime}}{\tau} c_{1}^{\prime}\left(\sqrt{\left|S^{\prime}\right|}+\frac{\tau}{2 \kappa^{\prime}} \sqrt{\left|S^{\prime}\right|}\right) \sqrt{\frac{\log q}{c_{2}^{\prime} M_{n}}}
$$

(2) model selection consistent:

$$
\hat{\boldsymbol{\beta}} \in \mathcal{M}^{\prime}
$$

## 3 Inference

### 3.1 Method

In general, it is often necessary to make statistical inferences on the estimated model coefficients, such as to evaluate the significance of the effect of a covariate or to obtain confidence intervals of the coefficient estimates. However, when faced with high-dimensional covariates, the resulting estimates are typically biased, rendering additional challenges. This is evident in the use of a lasso-type of estimation in the
preceding section. To overcome this obstacle, we utilize a "split-and-smooth" approach (Fei and Li, 2021), which combines low-dimensional estimations with prior variable selection to correct for bias in the highdimensional problem. In the following discussion of inference on $\boldsymbol{\beta}$, it is assumed that the projection vector, $\gamma$, is given, either prespecified or using the estimate from the full dataset. Based on the formulation in Model (1), define $z_{i} \equiv \sum_{t=1}^{T_{i}}\left(\gamma^{\top} \mathbf{y}_{i t}\right)^{2}$, and consider it as the response variable. Notably, after standardization, $z_{i}$ has been shown to follow a chi-squared distribution, a member of the exponential distribution family. Consequently, fitting Model (1) between the predictor $\mathbf{x}_{i}$ and $z_{i}$ corresponds to solving a generalized linear model (GLM) problem.

We consider $n$ subjects of observed data $\mathbf{C}^{(n)}=(\mathbf{Y}, \mathbf{X})=\left\{\left(\mathbf{Y}_{i}, \mathbf{x}_{i}\right) \mid 1, \ldots, n\right\}$, where $\mathbf{Y}=\left\{\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{n}\right\}$, $\mathbf{Y}_{i}=\left(\mathbf{y}_{i 1}, \ldots, \mathbf{y}_{i T_{i}}\right)^{\top} \in \mathbb{R}^{T_{i} \times p}$ and $\mathbf{X}=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)^{\top} \in \mathbb{R}^{n \times q}$. For Model (1), a sparsity condition is imposed where the number of nonzero coefficients is small relative to the sample size. More details will be explained in the upcoming subsection. Considering a high-dimensional problem, a data-splitting approach is employed as an initial step. For instance, the observed dataset is divided into two mutually exclusive subsets, denoted as $\mathbf{C}_{1}=\left(\mathbf{Y}^{1}, \mathbf{X}^{1}\right)$ and $\mathbf{C}_{2}=\left(\mathbf{Y}^{2}, \mathbf{X}^{2}\right)$, of sizes $n_{1}$ and $n_{2}$ respectively, with $n_{1}+n_{2}=n$. The former subset, $\mathbf{C}_{1}$, is used for dimension reduction, where a variable selection technique (denoted as $\mathcal{S}_{\lambda}$, where $\lambda$ is the tuning parameter used in the technique) is implemented and a subset of predictors, denoted as $\hat{S} \subseteq\{1, \ldots, q\}$, is selected. The second dataset, $\mathbf{C}_{2}$, is utilized to fit low-dimensional models of (1) using $\mathbf{Y}^{2}$ and $\mathbf{X}_{\hat{S}_{+j}}^{2}$, where $\hat{S}_{+j}=\{j\} \cup \hat{S}$, for $j=1,2, \ldots, q$. Let $\tilde{\boldsymbol{\beta}}_{\hat{S}_{+j}}$ denote the corresponding maximum likelihood estimate and $\tilde{\beta}_{j}=\left(\tilde{\boldsymbol{\beta}}_{\hat{S}_{+j}}\right)_{j}$ denote the element corresponding to the $j$ th predictor. Note that, the first column of $\mathbf{X}$ are ones, thus, $\tilde{\beta}_{1}$ is the estimate of the intercept. The estimate of the model coefficients from one data split, namely single-splitting estimator, is then obtained and denoted as $\tilde{\boldsymbol{\beta}}=\left(\tilde{\beta}_{1}, \ldots, \tilde{\beta}_{q}\right)^{\top} \in \mathbb{R}^{q}$.

Utilizing a single-split estimator is recognized with high variability, primarily due to the nature of random data splitting. This heightened variability poses a challenge in distinguishing genuine signals from noise, a recurrent issue encountered in bagging algorithms (Bühlmann and Yu, 2002). To address this issue, we are considering implementing a multi-splitting strategy. We repeat the above single-splitting procedure for $B$ times, where $B$ is a large number. Denote $\mathbf{C}_{1}^{b}$ and $\mathbf{C}_{2}^{b}$ as the two subsets of the bth splitting with $\left|\mathbf{C}_{1}^{b}\right|=n_{1}$ and $\left|\mathbf{C}_{2}^{b}\right|=n_{2}$, for $b=1, \ldots, B$. We apply $\mathcal{S}_{\lambda}$ on $\mathbf{C}_{1}^{b}$ to obtain the estimate of the active set, $\hat{S}^{b}$, and yield the estimate of model coefficients by fitting a low-dimensional model using $\mathbf{C}_{2}^{b}$, denoted as $\tilde{\boldsymbol{\beta}}^{b}=\left(\tilde{\beta}_{1}^{b}, \ldots, \tilde{\beta}_{q}^{b}\right)^{\top}$. Then, these $B$ estimates of model coefficients are averaged over all splits to attain a smoothed coefficient estimate, defined as

$$
\hat{\boldsymbol{\beta}}=\left(\hat{\beta}_{1}, \ldots, \hat{\beta}_{q}\right)^{\top}, \text { where } \hat{\beta}_{j}=\frac{1}{B} \sum_{b=1}^{B} \tilde{\beta}_{j}^{b}, \text { for } j=1, \ldots, q
$$

The process for the multi-splitting estimator $\hat{\beta}_{j}$ is detailed in Algorithm 2. The subsequent subsection will delve into the theoretical properties of this procedure, enabling the construction of a confidence interval for $\hat{\beta}_{j}$ to facilitate inference.

## Algorithm 2 The Multi-splitting Estimator Algorithm $1 ;$ <br> $\mathcal{S}_{\lambda}:$ a variable selection procedure; <br> $n_{1}, n_{2}$ : sample sizes for splitting; <br> $B$ : the number of random splits.

Input: $\mathbf{Y}$ : a list of data, where the $i$ th element is a $T_{i} \times p$ matrix;

$\mathbf{X}$ : an $n \times q$ matrix of covariates with the first column of ones;

$\hat{\gamma}$ : a $p$-dimensional vector denoting the prespecified or estimated projection vector obtained from

for $b=1,2, \ldots, B$ do

Split the samples into $\mathbf{C}_{1}^{b}$ and $\mathbf{C}_{2}^{b}$, with $\left|\mathbf{C}_{1}^{b}\right|=n_{1}$ and $\left|\mathbf{C}_{2}^{b}\right|=n_{2}$.

With given $\hat{\gamma}$, apply $\mathcal{S}_{\lambda}$ to $\mathbf{C}_{1}^{b}$ to select predictors indexed by $\hat{S}^{b} \subset\{1, \ldots, q\}$.

for $j=1, \ldots, q$ do

With $\hat{S}_{+j}^{b}=\{j\} \cup \hat{S}^{b}$, fit model (1) using $\mathbf{Y}^{b 2}$ and $\mathbf{X}_{\hat{S}_{+j}}^{b 2}$ with $\gamma=\hat{\gamma}$ and obtain the estimate of model coefficients, denoted as $\tilde{\boldsymbol{\beta}}_{\hat{S}_{+j}}^{b}$.

6: $\quad$ Let $\tilde{\beta}_{j}^{b}=\left(\tilde{\boldsymbol{\beta}}_{\hat{S}_{+j}^{b}}^{b}\right)_{j}$, which is the coefficient for predictor $\mathbf{X}_{j}$.

end for

Set $\tilde{\boldsymbol{\beta}}^{b}=\left(\tilde{\beta}_{1}^{b}, \ldots, \tilde{\beta}_{q}^{b}\right)^{\top}$

end for

Compute $\hat{\boldsymbol{\beta}}=\left(\hat{\beta}_{1}, \ldots, \hat{\beta}_{q}\right)^{\top}$, where $\hat{\beta}_{j}=\frac{1}{B} \sum_{b=1}^{B} \tilde{\beta}_{j}^{b}$

Output: $\hat{\boldsymbol{\beta}}$.

### 3.2 Asymptotic properties

According to the model selection consistency outlined in Theorem 2, the sure screening property is readily satisfied under regularity conditions. Assuming $\gamma$ is known, similar properties as those in Fei and Li (2021) can be derived. Define the observed information as $\hat{I}(\boldsymbol{\beta})=1 / 2 M_{n} \sum_{i=1}^{n} T_{i} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t} \cdot \mathbf{y}_{i t}^{\top} \boldsymbol{\gamma}\right) \mathbf{x}_{i} \mathbf{x}_{i}^{\top}$, the expected information as $I^{*}=\mathbb{E}\left\{\hat{I}\left(\boldsymbol{\beta}^{*}\right)\right\}$, where $\boldsymbol{\beta}^{*}$ is the true model parameter. For $S \subseteq\{1,2, \ldots, q\}$, the support of $\boldsymbol{\beta}^{*}$, we have an estimation $\hat{S} \supseteq S$ and $\mathbf{x}_{i S}, \boldsymbol{\beta}_{S}$ are subvectors of $\mathbf{x}_{i}$ and $\boldsymbol{\beta}$ only containing elements indexed by $S$, respectively. Moreover, $S_{+j}=S \cup\{j\}$ and $S_{-j}=S \backslash\{j\}$. Similarly, define the observed sub-information by $\hat{I}_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}\right)=1 / 2 M_{n} \sum_{i=1}^{n} T_{i} \exp \left(-\mathbf{x}_{i \hat{S}}^{\top} \boldsymbol{\beta}_{\hat{S}}\right)\left(\boldsymbol{\gamma}^{\top} \mathbf{y}_{i t} \cdot \mathbf{y}_{i t}^{\top} \gamma\right) \mathbf{x}_{i \hat{S}}^{\mathbf{x}_{i \hat{S}}^{\top}}$ and the expected sub-information by $I_{\hat{S}}=\mathbb{E}\left\{\hat{I}_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right\}=I_{\hat{S}}^{*}$, which is the submatrix of $I^{*}$ with rows and columns indexed by $\hat{S}$.

The asymptotic properties of the single-splitting estimator are outlined in Theorem 4, demonstrating its consistency and normality. However, due to its utilization of only $n_{1}$ subjects, it exhibits reduced efficiency. In contrast, a multi-splitting strategy is employed to address the high variability associated with data splitting, yielding a smoothed estimator denoted as $\hat{\boldsymbol{\beta}}$. The subsequent Theorem 5 details the asymptotic properties of this smoothed estimator.

Theorem 4. When the dimension of the predictors is divergent with sample size $n$, consider the singlesplitting estimator $\tilde{\boldsymbol{\beta}}=\left(\tilde{\beta}_{1}, \ldots, \tilde{\beta}_{q}\right)^{\top}$. With known $\gamma$, denote $m=|\hat{S}|$ and $\tilde{\sigma}_{j}^{2}=\left(\left\{I_{\hat{S}_{+j}}^{*}\right\}^{-1}\right)_{j j}$, for $j \in\{1, \ldots, q\}$. Let $T=\min _{i} T_{i}$ and $M_{n}^{1}=\sum_{i=1}^{n} T_{i}$. As $n, T \rightarrow \infty$,

$$
\left\|\tilde{\boldsymbol{\beta}}_{S_{+j}}-\boldsymbol{\beta}_{S_{+j}}^{*}\right\|_{2}^{2}=o_{p}\left(m / M_{n}^{1}\right), \text { if } m \log m / M_{n}^{1} \rightarrow 0
$$

$$
\frac{\sqrt{M_{n}^{1}}\left(\tilde{\beta}_{j}-\beta_{j}^{*}\right)}{\tilde{\sigma}_{j}} \xrightarrow{\mathcal{D}} \mathcal{N}(0,1), \text { if } m^{2} \log m / M_{n}^{1} \rightarrow 0
$$

Theorem 5. Under an additional partial orthogonality condition that $\left\{x_{j}, j \in S\right\}$ are independent of $\left\{x_{i}, i \notin\right.$ S\}. Repeat random data splitting for $B$ times and obtain the multi-splitting estimator $\hat{\boldsymbol{\beta}}=\left(\hat{\beta_{1}}, \ldots, \hat{\beta_{q}}\right)^{\top}$ defined in (4). With known $\gamma$, denote $m=|S|$ and $\hat{\sigma}_{j}^{2}=\left(\left\{I_{S_{+j}}^{*}\right\}^{-1}\right)_{j j}$, for $j \in\{1, \ldots, q\}$. Let $T=\min _{i} T_{i}$ and $M_{n}=\sum_{i=1}^{n} T_{i}$. As $n, T, B \rightarrow \infty$,

$$
\frac{\sqrt{M_{n}}\left(\hat{\beta}_{j}-\beta_{j}^{*}\right)}{\hat{\sigma}_{j}} \stackrel{\mathcal{D}}{\longrightarrow} \mathcal{N}(0,1)
$$

The theoretical analysis above suggests that the variance of estimating $\hat{\beta}_{j}$, referred to as $\hat{\sigma}_{j}^{2}$, relies on the unknown active set, $S$, while accounting for the data variation across $B$ random splits. Thus, it is impossible to compute $\hat{\sigma}_{j}^{2}$ directly in an analytical form. Instead, one can estimate the variance component by employing the infinitesimal jackknife method (Efron, 2014), denoted as $\hat{V}_{j}$. In scenarios where we have
obtained a reliable approximation of the estimating variance $\hat{\sigma}_{j}^{2}$, for $0<\alpha<1$, the asymptotic $1-\alpha$ confidence interval for $\hat{\beta}_{j}(j=1, \ldots, q)$ is given by

$$
\left(\hat{\beta}_{j}-\Phi^{-1}(1-\alpha / 2) \sqrt{\hat{V}_{j}}, \hat{\beta}_{j}+\Phi^{-1}(1-\alpha / 2) \sqrt{\hat{V}_{j}}\right)
$$

where $\Phi(\cdot)$ is the cumulative distribution function of the standard normal distribution. The $p$-value for testing $\mathrm{H}_{0}: \beta_{j}^{*}=0$ is

$$
2 \times\left\{1-\Phi\left(\left|\hat{\beta}_{j}\right| / \sqrt{\hat{V}_{j}}\right)\right\}
$$

The procedure for estimating the variance component of the multi-splitting estimator $\hat{\beta}_{j}$ is outlined in Algorithm A.1, presented in the Appendix A.1. Additionally, a comprehensive derivation procedure for the approximate variance will be provided. It's noteworthy that when $\gamma$ is estimated, such as the maximum likelihood estimator (MLE) of $\gamma$, the asymptotic properties of $\hat{\boldsymbol{\beta}}_{j}$ also hold due to the consistency of the profile likelihood estimator.

## 4 Simulation

In this section, we evaluate the performance of the proposed approaches for coefficient estimation and inference with high-dimensional covariates and covariance matrix outcomes via simulation studies.

For $\mathbf{y}_{i t}$, data dimension is set to $p=5$ and data are generated from a multivariate normal distribution with mean zero and covariance matrix $\boldsymbol{\Sigma}_{i}$. The covariance matrix has the eigendecomposition of $\boldsymbol{\Sigma}_{i}=\Gamma \Lambda_{i} \Gamma^{\top}$, where $\Gamma=\left(\gamma_{1}, \ldots, \gamma_{p}\right)^{\top}$ is the orthonormal eigenvector matrix assumed to be identical across units and $\Lambda_{i}=\operatorname{diag}\left\{\lambda_{i 1}, \ldots, \lambda_{i p}\right\}$ is a diagonal matrix containing $p$ distinct eigenvalues. For the covariates, a dimension of $q=200$ is considered, including the intercept column. $\tilde{\mathbf{x}}_{i}$ 's are generated from a ( $q-1$ )-dimensional standard normal distribution. Two scenarios are tested in the simulation. (i) The null case, where the eigenvalues, $\lambda_{i j}$, are generated from a log-normal distribution with mean zero and variance of $0.5^{2}$. (ii) The alternative case, where the second (denoted as C2) and third (denoted as C3) eigenvalues are assumed to satisfy the log-linear model (1). That is for these two components, $\lambda_{i j}=\exp \left(\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)$, where $\mathbf{x}_{i}=\left(1, \tilde{\mathbf{x}}_{i}^{\top}\right)^{\top}$. Under the alternative, $\boldsymbol{\beta}$ is defined as follows. The intercept term is a random number between -10 and 10. The indices of the active set of $\mathrm{C} 2$ is $\{10,20,30\}$ with $\beta$ values $(2,2,-2), \mathrm{C} 3$ is $\{15,25,35\}$ with $\beta$ values $(1,-1,1)$ and those of other components equal to zero except intercept term. Under the above model settings, Assumptions (A1)-(A3) are satisfied. When implementing the proposed approach, the number of components is determined using the average DfD (degrees of freedom difference Zhao et al., 2019) with a threshold of two. The proposed methods employ the asymptotic variance in Theorem 5. The multi-splitting procedure introduced in Algorithm 2 is performed with $B=200$ to construct the confidence intervals. All the simulations are repeated 200 times.

We first examine the validity of the proposed method across varying covariate dimensions. We consider two cases: $q=200$ and $q=500$, with a fixed sample size $n=100$ and $T_{i}=T=100$ for all $i$. Table 1
displays the performance in estimating and conducting inference on $\boldsymbol{\beta}$. In the instance of high-dimensional covariates, the estimated $\hat{\boldsymbol{\beta}}$ from the proposed methods closely aligns with the true values in both components. The coverage probability, derived from the asymptotic variance, successfully achieves the designated level of $\alpha=0.05$ for both components, while keeping the mean squared error (MSE) at a minimal level. It is noteworthy that for particularly large covariate dimensions (e.g., $q=500$ ), unsatisfactory results are obtained for C3, while still achieving positive results for C2. To assess the accuracy of estimating $\gamma$, we use $|\langle\hat{\gamma}, \gamma\rangle| \rightarrow 1$ as a metric for the estimation error, where $|\langle\cdot, \cdot\rangle|$ represents the inner product of two vectors. Table 2 displays the performance in estimating $\gamma$. The proposed method yields accurate estimates in both components with a high correlation to the truth in the case where $q=200$. These results collectively indicate that the proposed methods effectively capture the underlying relationships and offer reliable inference in this simulation scenario.

Table 1: Estimate and inference on $\boldsymbol{\beta}$ in the simulation study. The results are averages over 200 simulations. Component: corresponding to different eigenvectors; True: real coeffecients; Est.: estimate; SE: standard error; CP: coverage probability; MSE: mean squared error.

|  | Component | $\beta_{10}$ |  |  |  | $\beta_{25}$ |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | Truth | Est. (SE) | $\mathrm{CP}$ | MSE | Truth | Est. (SE) | $\mathrm{CP}$ | MSE |
| $\mathrm{q}=200$ | C2 | 2 | $2(0.03)$ | 0.97 | 0.01 | 0 | $-0.01(0.03)$ | 0.98 | 0.02 |
|  | $\mathrm{C} 3$ | 0 | $0.01(0.01)$ | 0.93 | 0.01 | -1 | $-0.99(0.01)$ | 0.94 | 0.01 |
| $\mathrm{q}=500$ | $\mathrm{C} 2$ | 2 | $2(0.02)$ | 0.98 | 0.06 | 0 | $0.02(0.02)$ | 0.97 | 0.12 |
|  | C3 | 0 | $1.24(0.01)$ | 0.11 | 1.79 | -1 | $-0.04(0.01)$ | 0.05 | 0.97 |

Table 2: Estimate of $\gamma$ in the simulation study. All values are averaged over 200 simulations. Est.: estimate, SE: standard error

|  |  | $\gamma_{1}$ | $\gamma_{2}$ | $\gamma_{3}$ | $\gamma_{4}$ | $\gamma_{5}$ | $\|\langle\hat{\gamma}, \gamma\rangle\|(\mathrm{SE})$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathrm{C} 2$ | Truth | 0.447 | -0.862 | 0.138 | 0.138 | 0.138 |  |
|  | Est. | 0.460 | -0.858 | 0.135 | 0.140 | 0.123 | $0.816(0.142)$ |
| C3 | Truth | 0.447 | 0.138 | -0.862 | 0.138 | 0.138 | $0.829(0.126)$ |
|  | Est. | 0.425 | 0.138 | -0.868 | 0.174 | 0.132 |  |
|  |  |  |  |  |  |  |  |

To further assess the finite sample performance of the proposed methods, we conduct experiments, varying the number of units $(n=100,200,500)$, the number of observations $\left(T_{i}=T=100,200,500\right)$, and fixing the dimension of the covariates $(q=200)$. The emphasis is on evaluating the ability to identify nonzero coefficients in each component. The results, displayed in Figure 1, include the estimates, coverage probability derived from the asymptotic variance, and the mean squared error (MSE) of the target model coefficients for


Figure 1: Performance of proposed method. Coverage probability (CP) is derived from the asymptotic variance in the proposed method. The gray dot-dash lines are the true parameters in (a) and (d), the designated level 0.95 in (b) and (e), and zero in (c) and (f). (a) Estimate of $\beta_{20}$ in C2, (b) CP of $\hat{\beta}_{20}$ in C2, (c) MSE of $\hat{\beta}_{20}$ in C2, (d) Estimate of $\beta_{40}$ in C3, (e) CP of $\hat{\beta}_{40}$ in C3, (f) MSE of $\hat{\beta}_{40}$ in C3.
both components. The figure illustrates that as both $n$ and $T_{i}$ increase, the estimates of $\beta_{20}$ in $\mathrm{C} 2$ and $\beta_{40}$ in C3 converge to their true values, 2 and 0, respectively. The coverage probability of $\beta_{20}$ in $\mathrm{C} 2$ converges to the designated level of 0.95 as both $n$ and $T_{i}$ increase, while the coverage probability of $\beta_{40}$ in C3 fluctuates around 0.95 . The MSEs of estimating $\beta$ in both components converge to zero as $n$ and $T_{i}$ increase. These findings suggest that the proposed methods demonstrate promising performance in terms of accuracy and reliability as both the sample size and the number of observations increase.

Additionally, we conduct an investigation to assess the impact of changes in the dimensionality of the response variable $\mathbf{y}$ on the performance and present the results in Table 3. The results illustrate that the proposed method remains remarkably robust to increases in the dimension of $\mathbf{y}$, as long as $p<\min _{i} T_{i}$. This observation emphasizes the reliability and effectiveness of our method across various scenarios.

Table 3: Estimate and inference on $\boldsymbol{\beta}$ as $p$ varies from 5 to 50 , while maintaining a fixed sample size of $n=100$ and $T_{i}=T=100$ for $i=1, \ldots, n$. The results are averages over 200 simulations. Component: corresponding to different eigenvectors; True: real coeffecients; Est.: estimate; SE: standard error; CP: coverage probability; MSE: mean squared error.

|  | Component | $\beta_{10}$ |  |  |  | $\beta_{25}$ |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | Truth | Est. (SE) | $\mathrm{CP}$ | MSE | Truth | Est. (SE) | $\mathrm{CP}$ | MSE |
| $\mathrm{p}=5$ | $\mathrm{C} 2$ | 2 | $2(0.03)$ | 0.97 | 0.01 | 0 | $-0.01(0.03)$ | 0.98 | 0.02 |
|  | $\mathrm{C} 3$ | 0 | $0.01(0.01)$ | 0.93 | 0.01 | -1 | $-0.99(0.01)$ | 0.94 | 0.01 |
| $\mathrm{p}=20$ | $\mathrm{C} 2$ | 2 | $2(0.03)$ | 0.98 | 0.01 | 0 | $0.02(0.03)$ | 0.96 | 0.01 |
|  | $\mathrm{C} 3$ | 0 | $0.02(0.02)$ | 0.99 | 0.01 | -1 | $-0.95(0.05)$ | 0.99 | 0.01 |
| $\mathrm{p}=50$ | $\mathrm{C} 2$ | 2 | $2.01(0.05)$ | 0.89 | 0.02 | 0 | $-0.02(0.04)$ | 0.98 | 0.01 |
|  | $\mathrm{C} 3$ | 0 | $0.01(0.02)$ | 0.99 | 0.01 | -1 | $-1(0.01)$ | 0.99 | 0.01 |

## 5 Application

We apply the proposed approach to the Lifespan Human Connectome Project (HCP) Aging Study. As an extension of the HCP study of healthy young adults, the Lifespan study utilizes the developed technological advances to offer a high-quality dataset across the human lifespan. The Aging study, in particular, aims to explore a typical aging trajectory and how brain connectome varies among mature and older adults. In this study, the association between two imaging modalities, diffusion tensor imaging (DTI) and restingstate functional magnetic resonance imaging (fMRI), is investigated. DTI is an MRI technique that offers an assessment of brain structural connectivity by tracing the diffusion process of water molecules along white matter fiber bundles. Resting-state fMRI, on the other hand, offers an assessment of the so-called brain functional connectivity, where the fMRI technique measures the blood oxygen level-dependent as a surrogate of neural activity. Hebb's law postulates that frequently communicated brain regions are more
likely the consequences of direct structural connections (Hebb, 2005). Existing literature also suggested that brain structural connectivity shapes and regulates the dynamics of cortical circuits and systems captured by functional connectivity (Sporns, 2007). Thus, in this study, the output from DTI is considered as the predictor $(X)$, and the output from resting-state fMRI is considered as the outcome $(Y)$. A total of $n=564$ subjects aged between 36 and 90 ( 307 Female and 257 Male) with both the resting-state fMRI and DTI available without quality control concerns are analyzed. The fMRI data were minimally preprocessed (Glasser et al., 2013). Signals $\left(\mathbf{y}_{i t}\right)$ are extracted from $p=75$ brain regions ( 60 cortical and 15 subcortical regions) using the Harvard-Oxford atlas in FSL (Smith et al., 2004) and motion-corrected. The DTI data were preprocessed using developed pipelines for noise reduction, motion, and distortion correction (more details are described in Hall et al., 2022). The Desikan atlas (Desikan et al., 2006) is considered for brain parcellation, which divides the brain into $q=84$ regions of interest (ROIs). Two regions are considered structurally connected if there exists at least one fiber streamline with two endpoints located in these two regions. After building such a network, the degree of each region is summarized and treated as the predictor $\left(\mathbf{x}_{i}\right)$. Regions in both the Harvard-Oxford and Desikan atlas are grouped into 10 functional modules. To better interpret fMRI components, $\gamma$ is sparsified following an ad hoc procedure using a fused lasso regression (Tibshirani et al., 2005) to impose local smoothness and constancy within each functional module (Grosenick et al., $2013)$.

Using the DfD criterion, the proposed approach identifies three orthogonal fMRI components, denoted as $\mathrm{C} 1, \mathrm{C} 2$, and $\mathrm{C} 3$. Figure 2 presents the brain maps of regions with a nonzero loading in $\gamma$ in the restingstate fMRI data, along with the corresponding brain maps of regions with a significant $\beta$ coefficient in the DTI data. The loading profile of all regions is shown in Figure B. 1 of the supporting information and the $\beta$ estimate (together with the $95 \%$ confidence interval) of all regions is presented in Figure B.2. Using a river plot, configurations by brain functional modules are demonstrated in Figure B.3. A high proportion of overlapping and sign consistency between nonzero $\gamma$ 's and significant $\beta$ 's is observed in both C1 and C2, consistent with the regulating role of brain white matter integrity on functional connectivity (Jbabdi and Johansen-Berg, 2011). In C3, the overlapping region, the supramarginal gyrus, yields the lowest negative value in both $\gamma$ and $\boldsymbol{\beta}$. A significant portion of the nonzero $\gamma$ 's of all three components are regions in the default mode network (DMN), which is more active during the resting state. However, these three components represent three different subnetworks in the DMN. C1 is considered part of the caudal-temporal DMN related to auditory processing and language comprehension (Gollo et al., 2018). C2 is primarily the cingulate-precuneus DMN suggested to play a role in memory and perception (Laird et al., 2009). For C3, the middle temporal gyrus, inferior parietal gyrus, and supramarginal gyrus have been identified as part of a distinct subnetwork within the DMN referred to as the "temporoparietal junction" subnetwork playing a role in social cognition, attention, and self-referential processing (Leech et al., 2011). In summary, the proposed approach identifies brain networks, as well as associated brain structural predictors, that are consistent with existing knowledge of the human brain.



(a) C1 rs-fMRI map $(\gamma)$



(b) $\mathrm{C} 2$ rs-fMRI map $(\gamma)$



(c) C3 rs-fMRI map $(\gamma)$



(d) C1 DTI map $(\beta)$

$\mathbf{R}$



(e) C2 DTI map $(\beta)$
R $\mathbf{L}$



(f) C3 DTI map $(\beta)$

Figure 2: Regions with a nonzero loading in $\gamma$ from resting-state fMRI and regions with a significant $\beta$ coefficient from DTI in brain maps of the three identified components (C1, C2, and C3) using the proposed approach in the HCP Aging study.

## 6 Discussion

In this manuscript, we extend a prior work of covariance regression to the scenario with high-dimensional covariates, where a linear projection on the covariance matrices is assumed and a log-linear model on heteroscedasticity is imposed in the projection space. A regularized estimator of the model coefficient, $\boldsymbol{\beta}$, is proposed. Integrated with a likelihood-based optimization criterion, the projection, $\gamma$, and the model coefficient, $\boldsymbol{\beta}$, are identified simultaneously. A novel split-and-smooth procedure is introduced for statistical inference on the estimated model coefficients. Under the assumption of common eigenstructure across covariance matrices, the proposed approach offers asymptotically consistent estimators. Remarkably, our approach stands out for its computational efficiency and estimation reliability requiring fewer assumptions, which is noteworthy as we refrain from making any assumptions regarding the sparsity of the precision matrix of covariates $\mathbf{x}$.

Several challenges lie ahead for future research. Firstly, theoretical properties when relaxing the common eigenstructure assumption to partial common diagonalization assumption are worth investigating. This is particularly pertinent in real-world scenarios, especially when $p$ is relatively large. Secondly, though asymp-

totic normality of $\hat{\beta}_{j}$ is achieved following the proposed inference procedure, the exploration of the covariance structure of the entire $\boldsymbol{\beta}$ vector is a promising avenue for future investigation. Thirdly, the present manuscript focuses on the statistical inference of $\boldsymbol{\beta}$, future inquiries into the statistical inference of $\gamma$ will be valuable, particularly in applications, such as fMRI studies, where identifying significant subnetwork structures is crucial. Lastly, considering scenarios where both the response and covariates are high-dimensional, that is both $p$ and $q$ are large, opens up avenues for developing methods and theoretical results tailored to such situations.

## Appendix

This Appendix collects additional theoretical results, the technical proof of the theorems in the main text, and additional data analysis results.

## A Additional Theoretical Results

## A. 1 The variance estimation

To define the variance of estimating $\hat{\beta}_{j}$ in Theorem 5 , let $\tilde{\beta}_{j}^{b}=\psi\left(\mathbf{C}_{2}^{b}\right)$ be the estimate given by the $b$ th splitting, where $\psi(\cdot)$ is a general function that maps the data to the estimator. Let $N_{i b} \in\{0,1\}$ indicate whether or not the $i$ th unit was sampled in $\mathbf{C}_{2}^{b}$. Using the infinitesimal jackknife method, a biased-corrected
estimation of the variance of $\hat{\beta}_{j}$ is introduced as the following. For the $j$ th model coefficient,

$$
\hat{V}_{j}=\frac{n-1}{n}\left(\frac{n}{n-n_{1}}\right)^{2} \sum_{i=1}^{n} \widehat{\operatorname{Cov}}_{i j}^{2}-\frac{n}{B^{2}} \frac{n_{1}}{n-n_{1}} \sum_{b=1}^{B}\left(\tilde{\beta}_{j}^{b}-\hat{\beta}_{j}\right)^{2}
$$

where

$$
\widehat{\operatorname{Cov}}_{i j}^{2}=\frac{1}{B} \sum_{b=1}^{B}\left(N_{i b}-\frac{1}{B} \sum_{b=1}^{B} N_{i b}\right)\left(\tilde{\beta}_{j}^{b}-\hat{\beta}_{j}\right)
$$

is the covariance between the estimates, $\tilde{\beta}_{j}^{b}$, and the sampling indicators, $N_{i b}$, with respect to the $B$ splits. The initial term of $\hat{V}_{j}$ is consistent with $\operatorname{Var}\left(\hat{\beta}_{j}\right)$ as demonstrated in Theorem 1 of Wager and Athey (2018), while the second term of $\hat{V}_{j}$ is designed to correct bias tailored to the sub-sampling scheme. The process for estimating the variance component of the multi-splitting estimator $\hat{\beta}_{j}$ is summarized in Algorithm A.1.

Algorithm A. 1 Estimate the variance of the multi-splitting estimator of $\boldsymbol{\beta}$.

Input: $n_{1}, n_{2}$ : sample sizes for splitting;

$B$ : the number of random splits;

$$
\begin{aligned}
& \tilde{\boldsymbol{\beta}}^{b}=\left(\tilde{\beta}_{1}^{b}, \ldots, \tilde{\beta}_{q}^{b}\right)^{\top}, b=1,2, \ldots, B \\
& \hat{\boldsymbol{\beta}}=\left(\hat{\beta}_{1}, \ldots, \hat{\beta}_{q}\right)^{\top}
\end{aligned}
$$

1: for $j=1, \ldots, q$ do

Compute

$$
\widehat{\operatorname{Cov}}_{i j}^{2}=\frac{1}{B} \sum_{b=1}^{B}\left(N_{i b}-N_{i \cdot}\right)\left(\tilde{\beta}_{j}^{b}-\hat{\beta}_{j}\right)
$$

where $N_{i b} \in\{0,1\}$ indicate whether or not the $i$ th subject was sampled in $\mathbf{C}_{2}^{b}$, which is defined above, and $N_{i}=\frac{1}{B} \sum_{b=1}^{B} N_{i b}$.

3: $\quad$ Compute

$$
\hat{V}_{j}=\frac{n-1}{n}\left(\frac{n}{n-n_{1}}\right)^{2} \sum_{i=1}^{n}{\widehat{\operatorname{Cov}_{i j}}}^{2}-\frac{n}{B^{2}} \frac{n_{1}}{n-n_{1}} \sum_{b=1}^{B}\left(\tilde{\beta}_{j}^{b}-\hat{\beta}_{j}\right)^{2}
$$

end for

Let $\hat{V}=\left(\hat{V}_{1}, \ldots, \hat{V}_{q}\right)^{\top}$

Output: $\hat{V}$.

## A. 2 Proof of Proposition 1

Proof. The log-likelihood function is:

$$
\begin{aligned}
\mathcal{L}_{n}(\beta) & =\frac{1}{2 M_{n}} \sum_{i \in n}\left(\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right) \cdot T_{i}+\frac{1}{2 M_{n}} \sum_{i \in n} \gamma^{\top} \mathbf{S}_{i} \boldsymbol{\gamma} \cdot \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right) \\
& =\frac{1}{M_{n}} \sum_{i \in n} \sum_{t=1}^{T_{i}} \ell_{i t} \\
\ell_{i t}^{\prime}(\boldsymbol{\beta}) & =-\frac{1}{2} \mathbf{x}_{i}+\frac{1}{2} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \boldsymbol{\gamma}\right) \mathbf{x}_{i} \\
\ell_{i t}^{\prime \prime}(\boldsymbol{\beta}) & =-\frac{1}{2} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\boldsymbol{\gamma}^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \boldsymbol{\gamma}\right) \mathbf{x}_{i} \mathbf{x}_{i}^{\top}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
\left\langle\nabla \mathcal{L}_{n}(\beta)-\nabla \mathcal{L}_{n}\left(\beta^{*}\right), \beta-\beta^{*}\right\rangle & =\frac{1}{M_{n}} \sum_{i \in n} \sum_{t=1}^{T_{i}}\left(\mu\left(\mathbf{x}_{i}^{\top} \beta\right)-\mu\left(\mathbf{x}_{i}^{\top} \beta^{*}\right)\right) \mathbf{x}_{i}^{\top}\left(\beta-\beta^{*}\right) \\
& =\frac{1}{M_{n}} \sum_{i \in n} \sum_{t=1}^{T_{i}} \mu^{\prime}\left(\mathbf{x}_{i}^{\top} \beta^{*}+v \mathbf{x}_{i}^{\top}\left(\beta-\beta^{*}\right)\right)\left(\mathbf{x}_{i}^{\top}\left(\beta-\beta^{*}\right)\right)^{2}
\end{aligned}
$$

where $\mu\left(\mathbf{x}_{i}^{\top} \beta\right)=\frac{1}{2} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\boldsymbol{\gamma}^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \gamma\right)$.

Then from the proof in Negahban et al. (2012), there exist positive constants $\kappa_{1}$ and $\kappa_{2}$ such that

$$
\left\langle\nabla \mathcal{L}_{n}(\beta)-\nabla \mathcal{L}_{n}\left(\beta^{*}\right), \beta-\beta^{*}\right\rangle \geq \kappa_{1}\|\Delta\|_{2}\left(\|\Delta\|_{2}-\kappa_{2} \sqrt{\frac{\log p}{M_{n}}}\|\Delta\|_{1}\right), \quad \forall \beta \in \mathbb{B}_{2}\left(1 ; \beta^{*}\right)
$$

with probability at least $1-c_{1} \exp \left(-c_{2} n\right)$, for some $c_{1}, c_{2}>0$. The result follows from the basic arithmetic inequality $2 a b \leq(a+b)^{2}$.

## A. 3 Proof of Theorem 2

Proof. We assume that the sample fisher matrix $\hat{\Sigma}$ satisfies the RSC condition, and it is not difficult to find that

$$
\begin{aligned}
\hat{\Sigma} & =\frac{1}{2 M_{n}} \sum_{i=1}^{n} T_{i} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \gamma\right) \mathbf{x}_{i} \mathbf{x}_{i}^{\top} \\
\nabla \mathcal{L}_{n}(\beta) & =-\frac{1}{2 M_{n}} \sum_{i=1}^{n} T_{i} \mathbf{x}_{i}+\frac{1}{2 M_{n}} \sum_{i=1}^{n} T_{i} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \gamma\right) \mathbf{x}_{i}
\end{aligned}
$$

Since data $\left\{x_{i}, y_{i t}\right\}$ satisfies the following regression model with a logarithmic link function:

$$
\log \left(\gamma^{\top} \Sigma_{i} \gamma\right)=x_{i}^{\top} \beta
$$

we can reasonably assume there exist a finite bound that $\left|\exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \boldsymbol{\gamma}\right)\right|<\xi$.

We can adaptly apply Theorem 3.4 in Lee et al. (2015), before that, we compute the constants $\kappa_{\rho}, \kappa_{\varrho}$ and $\kappa_{\mathrm{IC}}$. Since the regularizer is finite (it's a norm), its dual semi-norm is finite. To keep things simple, we let $\varrho=\|\cdot\|_{1}$. Denote $\mathcal{M}=\operatorname{span}\left(B_{\infty, \mathcal{S}}\right)$, the constant $\kappa_{\rho}=\kappa_{\varrho}$ is

$$
\kappa_{\rho}=\sup _{\beta}\left\{\|\beta\|_{1} \mid \beta \in \mathcal{M}\right\}=\sqrt{|\mathcal{S}|}
$$

Meanwhile, denote $X^{T}=\left(\sqrt{T_{1}} \mathbf{x}_{1}, \ldots, \sqrt{T_{n}} \mathbf{x}_{n}\right)$, the constant $\kappa_{I C}$ is

$$
\begin{aligned}
\kappa_{I C}= & \left\|P_{B_{\infty}, \mathcal{S}}\left(\hat{\Sigma} P_{B_{\infty}, \mathcal{S}}\left(P_{B_{\infty}, \mathcal{S}} \hat{\Sigma} P_{B_{\infty}, \mathcal{S}}\right)^{\dagger} P_{B_{\infty}, \mathcal{S}} z-z\right)\right\|_{\infty} \\
& \leq\left\|X_{\mathcal{S}^{c}}^{T}\left(X_{\mathcal{S}}^{T}\right)^{\dagger} z_{\mathcal{S}}\right\|_{\infty}+\left\|z_{\mathcal{S}^{c}}\right\|_{\infty} \leq(2-\tau)\|z\|_{\infty}
\end{aligned}
$$

Since the loss function is continuous differentiable, thus any $\lambda<\infty$ satisfies the upper bound in Theorem 3.4 of Lee et al. (2015). We check our choice also satisfies the lower bound in Theorem 3.4. By Vershynin (2010), Proposition 5.10 and a union bound,

$$
\operatorname{Pr}\left(\left\|\nabla \ell\left(\theta^{\star}\right)\right\|_{\infty}>t\right) \leq \operatorname{Pr}\left(\left\|\sum_{i=1}^{n} T_{i}\left(\frac{1}{2} \xi-\frac{1}{2}\right) \mathbf{x}_{i}\right\|_{\infty}>M_{n} t\right) \leq 2 \exp \left(-\frac{M_{n} t^{2}}{2 \sigma^{2}}+\log p\right)
$$

When $\lambda=\frac{8 \xi \kappa_{I C}}{\tau} \sigma \sqrt{\frac{\log p}{M_{n}}}$

$$
\begin{aligned}
& \operatorname{Pr}\left(\frac{4 \kappa_{I C}}{\tau}\left\|\nabla \ell\left(\theta^{\star}\right)\right\|_{\infty}>\frac{8(2-\alpha)}{\alpha} \sigma \sqrt{\frac{\log p}{M_{n}}}\right) \\
& \leq 2 \exp (-2 \log p+\log p)=2 p^{-1}
\end{aligned}
$$

Finally, conclusion is easy to deduce.

## A. 4 Proof of Theorem 3

Proof. When $\alpha \neq 0, \mathbf{D}$ is invertible, thus $\mathbf{D}$ has a nontrivial null space. Let $\varrho=\|\cdot\|_{1}$, the compatibility constants are computed as the following:

$$
\begin{gathered}
\kappa_{1}=\kappa_{\mathrm{IC}}=\left\|\mathbf{D}_{\mathcal{S}^{c}} \mathbf{X}^{\top}\left(\tilde{\mathbf{D}}_{\mathcal{S}} \mathbf{X}^{\top}\right)^{-} \operatorname{sign}\left(\boldsymbol{\beta}_{\mathcal{S}}^{*}\right)\right\|_{\infty} \\
\kappa_{2}=\kappa_{\mathcal{R}}=\sup _{\boldsymbol{\beta}}\left\{\|\tilde{\mathbf{D}} \boldsymbol{\beta}\|_{1}: \boldsymbol{\beta} \in \mathcal{B}_{2} \cap \operatorname{span}\left(\tilde{\mathbf{D}}^{\top} \mathcal{B}_{\infty, \mathcal{S}^{c}}\right)^{\perp}\right\} \\
\kappa_{3}=\kappa_{\varrho}=\sup _{\boldsymbol{\beta}}\left\{\|\boldsymbol{\beta}\|_{1}: \boldsymbol{\beta} \in \mathcal{B}_{2} \cap \operatorname{span}\left(\tilde{\mathbf{D}}^{\top} \mathcal{B}_{\infty, \mathcal{S}^{c}}\right)^{\perp}\right\}
\end{gathered}
$$

$\mathcal{R}$ and $\varrho$ are finite, $\kappa_{1}, \kappa_{2}, \kappa_{3}<\infty$. The rest of the proof can be found in Lee et al. (2015).

## A. 5 Proof of Theorem 4

Proof. As a result of the data split, $\mathbf{C}_{1}$ and $\mathbf{C}_{2}$ are mutually exclusive, leading to the independence of $\hat{S}$, derived from $\mathbf{C}$ 1, from $\mathbf{C} 2=\left(\mathbf{Y}^{2}, \mathbf{X}^{2}\right)$. To analyze the asymptotic properties of single-splitting estimator $\widetilde{\boldsymbol{\beta}}_{\hat{S}+j}$ when the number of parameters $m$ diverges, we employ the techniques and findings from He and Shao (2001). Without loss of generality and for the sake of notation simplicity, let us consider the case where $j=1 \in \hat{S}$. The argument holds true if $1 \notin \hat{S}$ or for any other $j$.

To proceed, we first restrict on the event of $\Omega=\{\hat{S} \supseteq S\}$. With sure screening property deduced by theorem 1, assume constants $0 \leq c \leq 1 / 2, K>0, \mathrm{P}(\Omega) \geq 1-K(p \vee n)^{-1-c}$. Recall that

$$
\begin{gathered}
\widetilde{\boldsymbol{\beta}}_{\hat{S}_{+j}}=\underset{\boldsymbol{\beta} \in \mathbf{R}|\hat{S}|+1}{\operatorname{argmin}} \ell_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}\right)=\underset{\boldsymbol{\beta} \in \mathbf{R}|\hat{S}|+1}{\operatorname{argmin}} \ell\left(\boldsymbol{\beta}_{\hat{S}} ; \mathbf{Y}^{1}, \mathbf{X}_{\hat{S}}^{1}\right) ; \\
\widetilde{\beta}_{1}=\left(\widetilde{\boldsymbol{\beta}}_{\hat{S}_{+j}}\right)_{1}
\end{gathered}
$$

Given $M_{n}$ random samples $\left(x_{1}, y_{11}\right),\left(x_{1}, y_{12}\right), \ldots,\left(x_{1}, y_{1 T_{1}}\right), \ldots,\left(x_{n}, y_{n T_{n}}\right)$, the likelihood is

$$
\mathcal{L}_{n}(\beta)=\sum_{i=1}^{n} \sum_{t=1}^{T_{i}}\left(\frac{1}{2} \mathbf{x}_{i}^{\top} \boldsymbol{\beta}-\frac{1}{2}\left(\gamma^{\top} y_{i t} y_{i t}^{\top} \gamma\right) \cdot \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\right)
$$

To apply Theorems 2.1 and 2.2 of He and Shao (2000) in our case, we can verify that our Assumptions (A1) and (A2) will lead to their conditions (C1), (C2), (C4) and (C5) with $C=1, r=2$ and $A\left(M_{n}, m\right)=m$. To verify their (C3), we first note that their $D_{n}$ is our $I_{\hat{S}}^{*}$. Then for any $\beta_{\hat{S}}, \alpha \in \mathbf{R}^{m}$ such that $\|\alpha\|_{2}=1$, a second order Taylor expansion of score function $U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}\right)$ around $\boldsymbol{\beta}_{\hat{S}}^{*}$ leads to

$$
\left|\alpha^{\mathrm{T}} \mathbf{E}_{\boldsymbol{\beta}^{*}}\left(U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}\right)-U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right)-\alpha^{\mathrm{T}} I_{\hat{S}}^{*}\left(\boldsymbol{\beta}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right| \leq O\left(\left\|\boldsymbol{\beta}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right\|_{2}^{2}\right)
$$

Hence,

$$
\sup _{\left\|\boldsymbol{\beta}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right\| \leq\left(m / M_{n}\right)^{1 / 2}}\left|\alpha^{\mathrm{T}} \mathbf{E}_{\boldsymbol{\beta}^{*}}\left(U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}\right)-U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right)-\alpha^{\mathrm{T}} I_{\hat{S}}^{*}\left(\boldsymbol{\beta}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right| \leq O\left(m / M_{n}\right)=o\left(M_{n}{ }^{1 / 2}\right)
$$

which means their (C3) follows. Thus, by Theorem 2.1 of He and Shao (2000),

$$
\left\|\widetilde{\boldsymbol{\beta}}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right\|_{2}^{2}=o_{p}\left(m / M_{n}^{1}\right)
$$

given $m \log m / M_{n}^{1} \rightarrow 0$. Furthermore, by Theorem 2.2 of He and Shao (2000), if $m^{2} \log m / M_{n}^{1} \rightarrow 0$, then

$$
\left\|M_{n}^{1^{1 / 2}}\left(\widetilde{\boldsymbol{\beta}}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right)+M_{n}^{1-1 / 2}\left\{I_{\hat{S}}^{*}\right\}^{-1} U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right\|_{2}=o_{p}(1)
$$

Releasing the restriction on $\Omega$ and with $\mathrm{P}\left(\Omega^{c}\right)=\mathrm{P}(\hat{S} \nsupseteq S) \leq K(p \vee n)^{-1-c}$, we would still have $\left\|\widetilde{\boldsymbol{\beta}}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right\|_{2}^{2}=$ $o_{p}\left(m / M_{n}^{1}\right)$, given $M \log M / m_{n}^{1} \rightarrow 0$.

Similarly, we can show $\left\|M_{n}^{1^{1 / 2}}\left(\widetilde{\boldsymbol{\beta}}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}\right)+M_{n}^{1-1 / 2}\left\{I_{\hat{S}}^{*}\right\}^{-1} U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)\right\|_{2}=o_{p}(1)$, if $m^{2} \log m / M_{n}^{1} \rightarrow 0$, which can also be written as

$$
\widetilde{\boldsymbol{\beta}}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}=-M_{n}^{1^{-1}}\left\{I_{\hat{S}}^{*}\right\}^{-1} U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)+r_{M_{n}^{1}}
$$

with $\left\|r_{M_{n}^{1}}\right\|_{2}^{2}=o_{p}\left(1 / M_{n}^{1}\right)$. Consequently, by taking $\alpha=(0,1,0, \ldots, 0)^{\mathrm{T}}$ and left-multiplying both sides by $M_{n}^{1^{1 / 2}} \alpha^{\mathrm{T}}$, we have

$$
\sqrt{M_{n}^{1}}\left(\widetilde{\beta}_{1}-\beta_{1}^{*}\right) / \widetilde{\sigma}_{1} \xrightarrow{d} N(0,1),
$$

where $\widetilde{\sigma}_{1}^{2}=\left(\left\{I_{\hat{S}}^{*}\right\}^{-1}\right)_{11}$

## A. 6 Proof of Theorem 5

Similar to Lemma 4 in Fei and Li (2021), we apply the lemma here to our case without proof.

Lemma A.1. With model and Assumptions (A1) and (A2), consider the estimator $\widetilde{\boldsymbol{\beta}}_{\hat{S}}$ with respect to subset $\hat{S}$ as defined above. Denote by $m=|\hat{S}|$. If $m \log m / M_{n} \rightarrow 0$, then with probability going to $1,\left|\widetilde{\boldsymbol{\beta}}_{\hat{S}}\right|_{\infty} \leq C_{\beta}$, where $C_{\beta}>0$ is a constant depending on $c_{\min }, c_{\max }, c_{\beta}$.

Now we use the Lemma to prove the result of Theorem 5.

Proof. We define the oracle estimators of $\beta_{j}^{*}$ on the full data $(\mathbf{Y}, \mathbf{X})$ and the $b$-th subsample $\mathbf{C}_{2}^{b}$ respectively, where the candidate set is the true set $S$ and $|S|=s_{0}$ :

$$
\begin{aligned}
& \check{\boldsymbol{\beta}}_{S_{+j}}=\underset{\boldsymbol{\beta} \in \mathbf{R}^{s_{0}+1}}{\operatorname{argmin}} \ell_{S_{+j}}\left(\boldsymbol{\beta}_{S_{+j}}\right)=\underset{\boldsymbol{\beta} \in \mathbf{R}^{s_{0}+1}}{\operatorname{argmin}} \ell_{S_{+j}}\left(\boldsymbol{\beta}_{S_{+j}} ; \mathbf{Y}, \mathbf{X}_{S_{+j}}\right), \check{\boldsymbol{\beta}}_{j}=\left(\check{\boldsymbol{\beta}}_{S_{+j}}\right)_{j} \\
& \check{\boldsymbol{\beta}}_{S_{+j}}^{b}=\underset{\boldsymbol{\beta} \in \mathbf{R}^{s_{0}+1}}{\operatorname{argmin} \ell_{S_{+j}}^{b}}\left(\boldsymbol{\beta}_{S_{+j}}\right)=\underset{\boldsymbol{\beta} \in \mathbf{R}^{s_{0}+1}}{\operatorname{argmin} \ell_{S_{+j}}}\left(\boldsymbol{\beta}_{S_{+j}} ; \mathbf{Y}^{1(b)}, \mathbf{X}_{S_{+j}}^{1(b)}\right), \check{\boldsymbol{\beta}}_{j}^{b}=\left(\check{\boldsymbol{\beta}}_{S_{+j}}^{b}\right)_{j} .
\end{aligned}
$$

By Theorem 4 and given $s_{0}^{2} \log s_{0} / n \rightarrow 0$, for each $j \in\{1, \ldots, p\}$,

$$
\sqrt{M_{n}^{1}}\left(\check{\beta}_{j}-\beta_{j}^{*}\right) / \check{\sigma}_{j} \xrightarrow{d} N(0,1) \quad \text { as } M_{n}^{1} \rightarrow \infty
$$

where $\breve{\sigma}_{j}^{2}=\left(\left\{I_{S_{+j}}^{*}\right\}^{-1}\right)_{j j}$. With the oracle estimators $\breve{\beta}_{j}$ 's and $\breve{\beta}_{j}^{b}, \mathrm{~s}$, we have the following decomposition:

$$
\begin{aligned}
& \sqrt{M_{n}}\left(\widehat{\beta}_{j}-\beta_{j}^{*}\right) \\
= & \sqrt{M_{n}}\left(\check{\beta}_{j}-\beta_{j}^{*}\right)+\sqrt{M_{n}}\left(\widehat{\beta}_{j}-\check{\beta}_{j}\right) \\
= & \sqrt{M_{n}}\left(\check{\beta}_{j}-\beta_{j}^{*}\right)+\sqrt{M_{n}}\left(\frac{1}{B} \sum_{b=1}^{B} \widetilde{\beta}_{j}^{b}-\check{\beta}_{j}\right) \\
= & \underbrace{\sqrt{M_{n}}\left(\check{\beta}_{j}-\beta_{j}^{*}\right)}_{\mathrm{I}}+\underbrace{\sqrt{M_{n}}\left(\frac{1}{B} \sum_{b=1}^{B} \check{\beta}_{j}^{b}-\check{\beta}_{j}\right)}_{\mathrm{II}}+\underbrace{\sqrt{M_{n}}\left(\frac{1}{B} \sum_{b=1}^{B}\left\{\widetilde{\beta}_{j}^{b}-\check{\beta}_{j}^{b}\right\}\right)}_{\mathrm{III}} .
\end{aligned}
$$

The initial two terms in the aforementioned decomposition, which do not encompass various selections $S^{b}$ 's, pertaining to the oracle estimators and the true active set $S$. We need to show the following, as it will subsequently yield the outcomes articulated in the theorem through the application of Slutsky's theorem.

(a) $\mathrm{I} / \check{\sigma}_{j}=\sqrt{M_{n}}\left(\check{\beta}_{j}-\beta_{j}^{*}\right) / \check{\sigma}_{j} \xrightarrow{d} N(0,1)$;

(b) $\mathrm{II}=\frac{\sqrt{M_{n}}}{B} \sum_{b=1}^{B}\left\{\check{\beta}_{j}^{b}-\check{\beta}_{j}\right\}=o_{p}(1)$;

(c) $\left.\mathrm{III}=\frac{\sqrt{M_{n}}}{B} \sum_{b=1}^{B}\left\{\widetilde{\beta}_{j}^{b}-\check{\beta}_{j}^{b}\right\}=o_{p}(1) \cdot\right]$

First, (a) holds because of (A.3). To show (b), i.e. $\mathrm{II}=o_{p}(1)$, we first denote $\xi_{b, M_{n}}=\sqrt{M_{n}}\left(\check{\beta}_{j}^{b}-\check{\beta}_{j}\right)$, then II $=\left(\sum_{b=1}^{B} \xi_{b, M_{n}}\right) / B$. Since the sampling indicator vectors, $N_{i b}$ 's (defined in above Appendix A.1) are i.i.d, $\xi_{b, M_{n}}$ 's are i.i.d conditional on data $\mathbf{C}^{(n)}=(\mathbf{Y}, \mathbf{X})$. The conditional distribution of $\sqrt{M_{n}}\left(\check{\beta}_{j}^{b}-\check{\beta}_{j}\right)$ given $\mathbf{C}^{(n)}$ is asymptotically the same as the unconditional distribution of $\sqrt{M_{n}}\left(\check{\beta}_{j}-\beta_{j}^{*}\right)$, which converges to zero Gaussian by (A.3). With the uniform boundedness of $\check{\beta}_{j}^{b}$ and $\check{\beta}_{j}$ as shown in Lemma A.1, we can show that $\mathbf{E}\left(\xi_{b, M_{n}} \mid \mathbf{C}^{(n)}\right) \rightarrow 0$ and $\operatorname{Var}\left(\xi_{b, M_{n}} \mid \mathbf{C}^{(n)}\right) \rightarrow \check{\sigma}_{j}^{2}$ uniformly over $\mathbf{C}^{(n)}$ as $M_{n} \rightarrow \infty$. Furthermore, $\mathbf{E}\left(\mathrm{II} \mid \mathbf{C}^{(n)}\right)=\mathbf{E}\left(\xi_{b, M_{n}} \mid \mathbf{C}^{(n)}\right)$, and $\operatorname{Var}\left(\mathrm{II} \mid \mathbf{C}^{(n)}\right)=\operatorname{Var}\left(\xi_{b, M_{n}} \mid \mathbf{C}^{(n)}\right) / B$. By Chebyshev Inequality, for any $\delta, \zeta>0$, there exist $N_{0}, B_{0}>0$ such that when $n>N_{0}, B>B_{0}, \mathrm{P}(|\mathrm{II}| \geq \delta) \leq \zeta$. Thus, $\mathrm{II}=o_{p}(1)$.

To prove (c), i.e. III $=o_{p}(1)$, we first note that each subsample $\mathbf{C}_{1}^{b}$ can be regarded as a random sample of $n_{1}=k n(0<k<1)$ i.i.d. observations from the population distribution for which Theorem 2 holds, that is to say $\left|\hat{S}^{b}\right| \leq K_{1} n^{c_{1}}$ and $\mathrm{P}\left(S \subseteq \hat{S}^{b}\right) \geq 1-K_{2}(q \vee n)^{-1-c_{2}}$. We show that for any $b$, conditional on $\hat{S}^{b} \supseteq S, \sqrt{M_{n}}\left(\widetilde{\beta}_{j}^{b}-\breve{\beta}_{j}^{b}\right)=o_{p}(1)$.

To see this, we first arrange the order of the components of $\mathbf{x}=\left(x_{1}, \ldots, x_{q}\right)$ such that the first $s_{0}$ components are signal variables. In other words, $S=\left\{1, \ldots, s_{0}\right\}$. From the proof of Theorem 4 and omitting superscript $b$, we have that

$$
\begin{aligned}
& \widetilde{\beta}_{j}-\beta_{j}^{*}=-M_{n}^{1-1} \widetilde{e}_{j}^{\mathrm{T}}\left\{I_{S_{+j}}^{*}\right\}^{-1} U_{\hat{S}_{+j}}\left(\boldsymbol{\beta}_{\hat{S}_{+j}}^{*}\right)+\widetilde{r}_{M_{n}^{1}} \\
& \check{\beta}_{j}-\beta_{j}^{*}=-M_{n}^{1-1} \check{e}_{j}^{\mathrm{T}}\left\{I_{S_{+j}^{*}}^{*}\right\}^{-1} U_{S_{+j}}\left(\boldsymbol{\beta}_{S_{+j}}^{*}\right)+\check{r}_{M_{n}^{1}}
\end{aligned}
$$

where $\widetilde{e}_{j}=(0, \ldots, 0,1,0, \ldots, 0)^{\mathrm{T}}$ is a unit vector of length $\left|\hat{S}_{+j}\right|$ to index the position of variable $j$ in $\hat{S}_{+j}$, $\check{e}_{j}$ is a unit vector of length $\left|S_{+j}\right|$ to index the position of variable $j$ in $S_{+j}$, and the residuals $\left\|\widetilde{r}_{M_{n}^{1}}\right\|_{2}^{2}=$ $o_{p}\left(1 / M_{n}^{1}\right),\left\|\check{M}_{M_{n}^{1}}\right\|_{2}^{2}=o_{p}\left(1 / n_{1}\right)$. Here, $I_{\hat{S}_{+j}}^{*}$ and $I_{S_{+j}}^{*}$ are two submatrices of the expected information at $\boldsymbol{\beta}^{*}$, which is derived in the proof of Proposition 1 as $I^{*}=\mathbb{E}\left\{\frac{1}{2 M_{n}} \sum_{i \in n} \sum_{t=1}^{T_{i}} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t} \mathbf{y}_{i t}^{\top} \gamma\right) \mathbf{x}_{i} \mathbf{x}_{i}^{\top}\right\}=$ $\mathbb{E}\left\{\frac{1}{n} \mathbf{X}^{\mathrm{T}} \mathbf{V} \mathbf{X}\right\}$, where $\mathbf{V}=\operatorname{diag}\left\{\nu_{1}, \ldots, \nu_{n}\right\}$ is an $n \times n$ diagonal matrix with $\nu_{i}=\frac{1}{2 T_{i}} \sum_{t=1}^{T_{i}} \exp \left(-\mathbf{x}_{i}^{\top} \boldsymbol{\beta}\right)\left(\gamma^{\top} \mathbf{y}_{i t}\right.$ $\left.\mathbf{y}^{\top} \gamma\right)$.

For any $j \in S, k \in S^{c}$, the complement of $S$, the partial orthogonality condition (Fan and Lv, 2008) that $\left\{x_{j}, j \in S\right\}$ are independent of $\left\{x_{k}, k \in S^{c}\right\}$ implies that $I^{*}$ is block-diagonal with two blocks indexed by $S$ and $S^{c}$. That is,

$$
I^{*}=\left(\begin{array}{cc}
\mathbf{E}\left(\frac{1}{n} \mathbf{X}_{S}^{\mathrm{T}} \mathbf{V} \mathbf{X}_{S}\right) & 0 \\
0 & \mathbf{E}\left(\frac{1}{n} \mathbf{X}_{S^{c}}^{\mathrm{T}} \mathbf{V} \mathbf{X}_{S^{c}}\right)
\end{array}\right)
$$

where the submatrices $\mathbf{X}_{S}$ and $\mathbf{X}_{S^{c}}$ are submatrices of $\mathbf{X}$. Hence, $I_{\hat{S}_{+j}}^{*}$ is blockdiagonal with two blocks indexed by $S$ and $\hat{S}_{+j} \backslash S$, and $I_{S_{+j}}^{*}$ is block-diagonal with two blocks indexed by $S$ and $S_{+j} \backslash S=\emptyset$ if $j \in S$ or $=\{j\}$ otherwise.

Therefore, $\left\{I^{*}\right\}^{-1},\left\{I_{\hat{S}_{+j}}^{*}\right\}^{-1}$ and $\left\{I_{S_{+_{j}}^{*}}\right\}^{-1}$ are all block-diagonal. Write $U\left(\boldsymbol{\beta}^{*}\right)=\left(u_{0}, u_{1}, \ldots, u_{p}\right)^{\mathrm{T}}$, $\widetilde{e}_{j}^{T}\left\{I_{\hat{S}_{+j}^{*}}^{*}\right\}^{-1}=\left(\tilde{i}_{j k}\right)_{k \in \hat{S}_{+j}}$ and $\check{e}_{j}^{T}\left\{I_{S_{+j}}^{*}\right\}^{-1}=\left(\check{i}_{j k}\right)_{k \in S_{+j}}$. Then, it follows that $\widetilde{i}_{j k}=\check{i}_{j k}$ for $k \in S$, which leads to

$$
\begin{aligned}
& \sqrt{M_{n}^{1}}\left(\widetilde{\beta}_{j}-\check{\beta}_{j}\right)=-\frac{1}{\sqrt{M_{n}^{1}}} \sum_{k \in \hat{S}_{+j}} \widetilde{i}_{j k} u_{k}+\frac{1}{\sqrt{M_{n}^{1}}} \sum_{k \in S_{+j}} \check{i}_{j k} u_{k}+r_{n_{1}}^{\prime} \\
& =-\frac{1}{\sqrt{M_{n}^{1}}} \sum_{k \in \hat{S} \backslash S} \tilde{i}_{j k} u_{k}+\frac{1(j \notin S)}{\sqrt{M_{n}^{1}}}\left(\check{i}_{j j}-\tilde{i}_{j j}\right) u_{j}+r_{n_{1}}^{\prime}
\end{aligned}
$$

where $r_{n_{1}}^{\prime}=\sqrt{n_{1}}\left(\widetilde{r}_{n_{1}}-\check{r}_{n_{1}}\right)=o_{p}(1)$, and $\widetilde{r}_{n_{1}}$ and $\check{r}_{n_{1}}$ are as in (A.4). As $|\hat{S} \backslash S| \leq K_{1} n^{c_{1}}=o\left(\sqrt{n_{1}}\right)$ with $0 \leq c_{1}<1 / 2, \operatorname{Var}\left(\sum_{k \in \hat{S} \backslash S} \widetilde{i}_{j k} u_{k}\right)=o\left(n_{1}\right)$. By the Chebyshev inequality, the first term on the right-hand side converges to 0 in probability. Thus, each of these three terms is $o_{p}(1)$ and we have $\sqrt{M_{n}^{1}}\left(\widetilde{\beta}_{j}-\breve{\beta}_{j}\right)=$ $o_{p}(1)$. As $n_{1} / n=k$ where $0<k<1$, the original statement holds.

Now define $\eta_{b}=\mathbb{1}\left\{S \nsubseteq \hat{S}^{b}\right\} \sqrt{M_{n}}\left(\widetilde{\beta}_{j}^{b}-\breve{\beta}_{j}^{b}\right)$, while omitting subscripts $j$ in $\eta$ for simplicity, then III $=\left(\sum_{b=1}^{B} \eta_{b}\right) / B$. When $S \nsubseteq \hat{S}^{b}$, by Lemma A.1, there exists a $C_{\beta} \geq c_{\beta}$ such that $\sup _{b}\left|\widetilde{\beta}_{j}^{b}-\breve{\beta}_{j}^{b}\right| \leq$ $\sup _{b}\left|\widetilde{\beta}_{j}^{b}-\beta_{j}^{*}\right|+\sup _{b}\left|\breve{\beta}_{j}^{b}-\beta_{j}^{*}\right| \leq 2 C_{\beta}+1$. Therefore,

$$
\begin{aligned}
\mathbb{E}\left(\eta_{b}\right) & \leq \mathrm{P}\left(S \not \hat{S}^{b}\right) \sqrt{M_{n}} \sup _{1 \leq b \leq B}\left|\widetilde{\beta}_{j}^{b}-\check{\beta}_{j}^{b}\right| \leq 2 C_{\beta} \sqrt{M_{n}} K_{2}(q \vee n)^{-1-c_{2}}, \\
\operatorname{Var}\left(\eta_{b}\right) & \leq \mathrm{P}\left(S \not \hat{S}^{b}\right) M_{n} \sup _{1 \leq b \leq B}\left(\widetilde{\beta}_{j}^{b}-\check{\beta}_{j}^{b}\right)^{2} \leq 4 C_{\beta}^{2} M_{n} K_{2}(q \vee n)^{-1-c_{2}}
\end{aligned}
$$

With dependent $\eta_{b}$ 's, we further have

$$
\begin{gathered}
\mathbf{E}(\mathrm{III})=\mathbf{E}\left\{\left(\sum_{b=1}^{B} \eta_{b}\right) / B\right\} \leq 2 C_{\beta} \sqrt{M_{n}} K_{2}(q \vee n)^{-1-c_{2}}, \\
\operatorname{Var}(\mathrm{III}) \leq \frac{1}{B^{2}} \sum_{b=1}^{B} \sum_{b^{\prime}=1}^{B}\left|\operatorname{Cov}\left(\eta_{b}, \eta_{b^{\prime}}\right)\right| \leq 4 C_{\beta}^{2} M_{n} K_{2}(q \vee n)^{-1-c_{2}},
\end{gathered}
$$

where the last inequality holds because of $\left|\operatorname{Cov}\left(\eta_{b}, \eta_{b^{\prime}}\right)\right| \leq\left\{\operatorname{Var}\left(\eta_{b}\right) \operatorname{Var}\left(\eta_{b^{\prime}}\right)\right\}^{1 / 2}$ and (A.5). Then we can show $\mathrm{III}=o_{p}(1)$.

## B Additional Application Results



(a) C1



(b) $\mathrm{C} 2$



(c) C3

Figure B.1: Sparsified loading profile $(\gamma)$ of the three identified components using the proposed approach in the HCP Aging study.


(a) $\mathrm{C} 1$



(b) $\mathrm{C} 2$



(c) $\mathrm{C} 3$

Figure B.2: Estimated model coefficient and $95 \%$ confidence interval of the three identified components using the proposed approach in the HCP Aging study.



(a) $\mathrm{C} 1$ rs-fMRI $(\gamma)$



(d) C1 DTI $(\beta)$



(b) $\mathrm{C} 2$ rs-fMRI $(\boldsymbol{\gamma})$



(e) $\mathrm{C} 2$ DTI $(\beta)$



(c) $\mathrm{C} 3 \mathrm{rs}-\mathrm{fMRI}(\gamma)$



(f) C3 DTI $(\beta)$

Figure B.3: River plot of module configuration of the three identified components using the proposed approach in the HCP Aging study.

## References

Bassett, D. S. and Bullmore, E. T. (2017). Small-world brain networks revisited. The Neuroscientist, $23(5): 499-516$.

Belloni, A., Chernozhukov, V., and Hansen, C. (2014). Inference on treatment effects after selection among high-dimensional controls. The Review of Economic Studies, 81(2):608-650.

Bühlmann, P. and Van De Geer, S. (2011). Statistics for high-dimensional data: methods, theory and applications. Springer Science \& Business Media.

Bühlmann, P. and Yu, B. (2002). Analyzing bagging. The annals of Statistics, 30(4):927-961.

Bullmore, E. and Sporns, O. (2012). The economy of brain network organization. Nature Reviews Neuroscience, 13(5):336.

Desikan, R. S., Ségonne, F., Fischl, B., Quinn, B. T., Dickerson, B. C., Blacker, D., Buckner, R. L., Dale, A. M., Maguire, R. P., and Hyman, B. T. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. NeuroImage, 31(3):968-980.

Efron, B. (2014). Estimation and accuracy after model selection. Journal of the American Statistical Association, 109(507):991-1007.

Fan, J. and Li, R. (2001). Variable selection via nonconcave penalized likelihood and its oracle properties. Journal of the American statistical Association, 96(456):1348-1360.

Fan, J. and Lv, J. (2008). Sure independence screening for ultrahigh dimensional feature space. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 70(5):849-911.

Fei, Z. and Li, Y. (2021). Estimation and inference for high dimensional generalized linear models: A splitting and smoothing approach. The Journal of Machine Learning Research, 22(1):2681-2712.

Glasser, M. F., Sotiropoulos, S. N., Wilson, J. A., Coalson, T. S., Fischl, B., Andersson, J. L., Xu, J., Jbabdi, S., Webster, M., and Polimeni, J. R. (2013). The minimal preprocessing pipelines for the Human Connectome Project. NeuroImage, 80:105-124.

Gollo, L. L., Roberts, J. A., Cropley, V. L., Di Biase, M. A., Pantelis, C., Zalesky, A., and Breakspear, M. (2018). Fragility and volatility of structural hubs in the human connectome. Nature Neuroscience, $21(8): 1107-1116$.

Grosenick, L., Klingenberg, B., Katovich, K., Knutson, B., and Taylor, J. E. (2013). Interpretable wholebrain prediction analysis with GraphNet. NeuroImage, 72:304-321.

Hall, Z., Chien, B., Zhao, Y., Risacher, S. L., Saykin, A. J., Wu, Y.-C., and Wen, Q. (2022). Tau deposition and structural connectivity demonstrate differential association patterns with neurocognitive tests. Brain Imaging and Behavior, 16(2):702-714.

Hebb, D. O. (2005). The organization of behavior: A neuropsychological theory. Psychology Press.

Javanmard, A. and Montanari, A. (2014). Confidence intervals and hypothesis testing for high-dimensional regression. The Journal of Machine Learning Research, 15(1):2869-2909.

Jbabdi, S. and Johansen-Berg, H. (2011). Tractography: where do we go from here? Brain Connectivity, $1(3): 169-183$.

Kim, R. and Zhang, J. (2024). High-dimensional covariance regression with application to co-expression qtl detection. arXiv preprint arXiv:2404.02093.

Laird, A. R., Eickhoff, S. B., Li, K., Robin, D. A., Glahn, D. C., and Fox, P. T. (2009). Investigating the functional heterogeneity of the default mode network using coordinate-based meta-analytic modeling. Journal of Neuroscience, 29(46):14496-14505.

Lee, J. D., Sun, D. L., Sun, Y., and Taylor, J. E. (2016). Exact post-selection inference, with application to the lasso. The Annals of Statistics, 44(3):907-927.

Lee, J. D., Sun, Y., and Taylor, J. E. (2015). On model selection consistency of regularized M-estimators. Electronic Journal of Statistics, 9(1):608-642.

Leech, R., Kamourieh, S., Beckmann, C. F., and Sharp, D. J. (2011). Fractionating the default mode network: distinct contributions of the ventral and dorsal posterior cingulate cortex to cognitive control. Journal of Neuroscience, 31(9):3217-3224.

Mueller, S., Wang, D., Fox, M. D., Yeo, B. T., Sepulcre, J., Sabuncu, M. R., Shafee, R., Lu, J., and Liu, H. (2013). Individual variability in functional connectivity architecture of the human brain. Neuron, $77(3): 586-595$.

Negahban, S. N., Ravikumar, P., Wainwright, M. J., and Yu, B. (2012). A unified framework for highdimensional analysis of $m$-estimators with decomposable regularizers. Statistical Science, 27(4):538-557.

Ning, Y. and Liu, H. (2017). eneral theory of hypothesis tests and confidence regions for sparse high dimensional models. The Annals of Statistics, 45(1):158-195.

Seiler, C. and Holmes, S. (2017). Multivariate heteroscedasticity models for functional brain connectivity. Frontiers in Neuroscience, 11:696.

Smith, S. M., Jenkinson, M., Woolrich, M. W., Beckmann, C. F., Behrens, T. E., Johansen-Berg, H., Bannister, P. R., De Luca, M., Drobnjak, I., Flitney, D. E., et al. (2004). Advances in functional and structural MR image analysis and implementation as FSL. NeuroImage, 23:S208-S219.

Song, H., Dai, R., Raskutti, G., and Barber, R. F. (2020). Convex and non-convex approaches for statistical inference with class-conditional noisy labels. The Journal of Machine Learning Research, 21(1):6805-6862.

Sporns, O. (2007). Brain connectivity. Scholarpedia, 2(10):4695.

Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (Methodological), 58(1):267-288.

Tibshirani, R., Saunders, M., Rosset, S., Zhu, J., and Knight, K. (2005). Sparsity and smoothness via the fused lasso. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 67(1):91-108.

Tibshirani, R. J. and Taylor, J. (2011). The solution path of the generalized lasso. The Annals of Statistics, $39(3): 1335-1371$.

Van de Geer, S., Bühlmann, P., Ritov, Y., and Dezeure, R. (2014). On asymptotically optimal confidence regions and tests for high-dimensional models. The Annals of Statistics, 42(3):1166-1202.

Vershynin, R. (2010). Introduction to the non-asymptotic analysis of random matrices. arXiv preprint $\operatorname{arXiv:1011.3027.}$

Wager, S. and Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. Journal of the American Statistical Association, 113(523):1228-1242.

Wasserman, L. and Roeder, K. (2009). High dimensional variable selection. Annals of statistics, 37(5A):2178.

Xia, L., Nan, B., and Li, Y. (2020). A revisit to de-biased lasso for generalized linear models. arXiv preprint arXiv:2006.12778.

Zhang, C.-H. (2010). Nearly unbiased variable selection under minimax concave penalty. The Annals of Statistics, pages $894-942$.

Zhang, C.-H. and Zhang, S. S. (2014). Confidence intervals for low dimensional parameters in high dimensional linear models. Journal of the Royal Statistical Society: Series B (Statistical Methodology), $76(1): 217-242$.

Zhao, Y., Wang, B., Mostofsky, S., Caffo, B., and Luo, X. (2019). Covariate assisted principal regression for covariance matrix outcomes. Biostatistics.

Zhao, Y., Wang, B., Mostofsky, S. H., Caffo, B. S., and Luo, X. (2021). Covariate assisted principal regression for covariance matrix outcomes. Biostatistics, 22(3):629-645.

Zou, H. (2006). The adaptive lasso and its oracle properties. Journal of the American Statistical Association, $101(476): 1418-1429$.

Zou, H. and Hastie, T. (2005). Regularization and variable selection via the elastic net. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 67(2):301-320.

Zou, T., Lan, W., Wang, H., and Tsai, C.-L. (2017). Covariance regression analysis. Journal of the American Statistical Association, 112(517):266-281.

