# Covariance Regression With High-Dimensional Predictors

Yuheng He1, Changliang Zou1, and Yi Zhao2 1School of Statistics and Data Science, Nankai University, Tianjin, China 2Department of Biostatistics and Health Data Science, Indiana University School of Medicine, USA

## Abstract

In the high-dimensional landscape, addressing the challenges of covariance regression with highdimensional covariates has posed difficulties for conventional methodologies. This paper addresses these hurdles by presenting a novel approach for high-dimensional inference with covariance matrix outcomes.

The proposed methodology is illustrated through its application in elucidating brain coactivation patterns observed in functional magnetic resonance imaging (fMRI) experiments and unraveling complex associations within anatomical connections between brain regions identified through diffusion tensor imaging
(DTI). In the pursuit of dependable statistical inference, we introduce an integrative approach based on penalized estimation. This approach combines data splitting, variable selection, aggregation of lowdimensional estimators, and robust variance estimation. It enables the construction of reliable confidence intervals for covariate coefficients, supported by theoretical confidence levels under specified conditions, where asymptotic distributions are provided. Through various types of simulation studies, the proposed approach performs well for covariance regression in the presence of high-dimensional covariates. This innovative approach is applied to the Lifespan Human Connectome Project (HCP) Aging Study, which aims to uncover a typical aging trajectory and variations in the brain connectome among mature and older adults. The proposed approach effectively identifies brain networks and associated predictors of white matter integrity, aligning with established knowledge of the human brain.

Keywords: Covariance regression; Confidence interval; High-dimensional covariates; Penalized estimation, Variance

## 1 Introduction

This manuscript investigates a high-dimensional regression problem with covariance matrices as the outcome.

Assume the observed outcome data consist of n subjects, each with Ti observations of a p-dimensional random vector, denote as yit ∈ R
p, for t = 1*, . . . , T*i and i = 1*, . . . , n*. Let Yi = (yi1*, . . . ,* yiTi
)
⊤ ∈ R
Ti×p and Y = {Y1*, . . . ,* Yn}. The distribution of yit is assumed to be multivariate normal with mean zero and covariance matrix Σi. Without loss of generality, the distribution mean is set to zero as the focus of the study is on the covariance matrices. Let x˜i ∈ R
q−1 denote the (q − 1) dimensional covariates of interest acquired from subject i. Denote xi = (1, x˜
⊤ i
)
⊤ ∈ R
qthe vector that includes the intercept term and X = (x1*, . . . ,* xn)
⊤ ∈ R
n×q.

The term "high-dimensional covariance" pertains to scenarios where *q > n* and q increases toward infinity.

For covariance matrix outcomes, the following regression model introduced in Zhao et al. (2021) is considered.

Assuming there is a linear projection, the study proposed a parsimonious model in the projection space that accounts for data heteroscedasticity via a generalized linear regression model with a logarithmic link function,

$$\log\left(\gamma^{\top}\Sigma_{i}\gamma\right)=\beta_{0}+\tilde{\mathbf{x}}_{i}^{\top}\beta_{1}\equiv\mathbf{x}_{i}^{\top}\beta,$$
i β, (1)
1
where γ ∈ R
pis a linear projection and β = (β0, β
⊤
1
)
⊤ ∈ R
qcorresponds to the model coefficients. The use of the logarithmic link ensures the positive definiteness of the covariance matrices. The primary goal is to estimate both γ and β using the observed data, {(yi1*, . . . ,* yiTi
), xi}
n i=1.

This regression framework finds practical application in various domains. One notable context is its utilization for investigating the impact of covariates on brain synchronization measured by resting-state functional magnetic resonance imaging (fMRI) experiments. In the realm of fMRI studies, the utilization of covariance or correlation matrices derived from resting-state signals serves as a common approach to unveil intrinsic brain coactivation patterns. Exploring the interplay between these patterns and population or individual-level covariates emerges as a significant avenue of exploration within the field of neuroimaging research (Mueller et al., 2013; Seiler and Holmes, 2017; Zhao et al., 2021). A parallel application of this framework emerges within the realm of financial equities analysis. Consider a dataset comprising stock values, where covariance matrices calculated over specific time intervals provide insights into the level of co-movement or synchronicity among these stocks. This synchronicity is notably influenced by pertinent attributes at both the firm and market levels, including factors such as industry categorization, the firm's cash flow, stock size, and book-to-market ratio. The assessment and quantification of these intricate associations represent pivotal pursuits within the domain of financial theory (Zou et al., 2017).

For a covariance regression model as in (1), when q is less than n and fixed, Zhao et al. (2021) conducted an initial investigation, wherein a novel approach of estimating γ and β was introduced. This approach was grounded in likelihood principles, where iterations took place between minimizing the negative log-likelihood function within the projection space (fix γ) and optimizing for the projection (fix β) with a quadratic constraint. It is worth noting that the optimization is applicable when the covariance matrix of the design matrix, E(xix
⊤ i
), is invertible. Consequently, when *q > n*, the above-mentioned approach becomes ill-defined, primarily attributed to the rank deficiency in the covariance matrix of the covariates. Recently, Kim and Zhang (2024) investigated a covariance regression model that accommodates high-dimensional covariates.

They modeled Σ as a quadratic function of covariates x, expressed as Bxx⊤B
⊤, where B ∈ R
p×q. However, as the covariance matrix is modeled as a linear function of covariates with matrix-valued coefficients, it primarily addresses a multivariate linear regression problem, which may be less pertinent to the context under discussion here.

When encountering problems with high-dimensional covariates, one typical solution is to consider regularized estimation, including the LASSO (Tibshirani, 1996), the elastic net (Zou and Hastie, 2005), the adaptive LASSO (Zou, 2006), SCAD (Fan and Li, 2001), MCP (Zhang, 2010), ISIS (Fan and Lv, 2008),
and among others. Asymptotic properties, including model selection consistency and estimation consistency, under various conditions and regularization functions, have been established (see a review by B¨uhlmann and Van De Geer, 2011). Besides point estimation, achieving reliable inferences in high-dimensional models is also fundamental to the field. Researchers have approached this challenge from various angles. One primary direction involves making inferences based on the selected model chosen by a particular variable selection procedure. Wasserman and Roeder (2009) introduced a multi-stage procedure that employs data splitting to separate the steps of selection and inference. Lee et al. (2016) developed conditional asymptotics for coefficient estimates conditional on the selected model. Another direction centers on estimating and making inferences about low-dimensional parameters within high-dimensional models. Belloni et al. (2014) proposed a double selection procedure that involves multiple steps, rather than a single selection, to estimate and construct confidence regions for a primary regression parameter of interest. Some alternative approaches are based on penalized estimation. Notably, the bias correction method was introduced based on the LASSO
proposed by Javanmard and Montanari (2014); Van de Geer et al. (2014); Zhang and Zhang (2014), which provides both point estimates and confidence intervals for model parameters. Ning and Liu (2017) introduced hypothesis tests and confidence regions based on the decorrelated score function and test statistic.

Each of the above-mentioned approaches has its strengths and limitations. Some methods, such as Van de Geer et al. (2014), require precisely estimating the precision matrix of x, which is the inverse of a q × qdimensional covariance matrix, imposing a large computational burden and the assumption of sparsity in GLMs that is sometimes violated (Xia et al., 2020). Other methods, such as Wasserman and Roeder (2009) and Lee et al. (2016), aim for exact inference in post-selection estimates while being constrained to the correctness of model selection in the initial step. In this study, we incorporate a newly developed approach proposed by (Fei and Li, 2021) to our scenario, which utilizes sample splitting for inference with highdimensional covariates. This approach tackles the high-dimensional estimation challenge by aggregating low-dimensional estimates, thus overcoming computational complexity issues. Importantly, the method avoids making parameter assumptions in variance estimation and does not require consistency in model selection.

The proposed covariance regression with high-dimensional covariates has two steps.

1. Penalized estimation. It starts with estimating model parameters, γ, and β, using the full dataset with regularization on the high-dimensional coefficient, β.

2. High-dimensional inference. This step employs a data splitting procedure, which divides the samples into two distinct subsets, one for dimension reduction and one for low-dimensional model fitting.

The proposal is a comprehensive framework that enables estimating coefficients efficiently, conducting variable selection, and obtaining coefficient estimates for both selected and non-selected predictors. This approach addresses the intricacies of high-dimensional covariance regression and enhances the ability to draw meaningful inferences from the data. A pivotal assumption underlying the proposed approach is that the number of non-zero elements in the true β is small, that is the sparsity assumption. This assumption is in line with practical implementations. For instance, the small-world topology in brain science, where human brain anatomy is economically organized (Bullmore and Sporns, 2012) and information processing is often highly clustered and concentrated (Bassett and Bullmore, 2017). Another example is in the field of cancer genomics, it is plausible that a specific type of cancer is primarily associated with only a handful of oncogenes and tumor suppressor genes. For inference, the proposed approach is inspired by the work of Fei and Li (2021), where a Splitting and Smoothing method for Generalized Linear Models (GLMs) was introduced and effectiveness under mild conditions was demonstrated. This compelling property motivates us to adapt and generalize to models with covariance outcomes, opening new avenues for statistical inference in covariance regression with high-dimensional covariates.

The contributions of this study can be summarized into three key aspects.

- Penalized estimation and inference for covariance regression. To our best knowledge, this is the first attempt to delve into penalized estimation and statistical inference for covariance regression under the setting of high-dimensional covariates. This pioneering work lays the foundation for addressing complex problems involving high-dimensional data and covariance matrices.

- Aggregation of low-dimensional modeling. The proposed approach tackles the challenges of high-dimensional inference by aggregating low-dimensional modeling. It significantly improves computational effectiveness compared to existing approaches, enables efficient handling of high-dimensional data, and obtains more robust estimates.

- Robust variance estimation. To ensure reliable inference, a variance estimator is developed, which utilizes the infinitesimal jackknife method following the splitting and smoothing procedure. This variance estimation approach is free from parametric assumptions, a notable advantage, and results in confidence intervals with correct coverage probabilities.

The rest of the paper is organized as follows. Section 2 introduces the proposed penalized estimator of model coefficients and imposed assumptions for estimation and inference and studies the asymptotic properties. In Section 3, a Splitting and Smooth method for statistical inference is introduced and asymptotic properties are derived. Section 4 demonstrates the good performance of the proposed approach via simulation studies. Section 5 articulates an application to the Lifespan Human Connectome Project (HCP) Aging Study.

Section 6 summarizes the manuscript with discussions. The supporting information also collects the technical proof of the theorems in the main text, additional theoretical results, and additional data analysis results.

## 2 Estimation 2.1 Method

Given the regression model (1), it is proposed that an estimation of the parameters can be obtained by solving the following optimization problem. Specifically, the optimization problem is formulated to minimize the regularized negative likelihood function:

$$\begin{array}{ll}\underset{\boldsymbol{\beta},\boldsymbol{\gamma}}{\text{minimize}}&\ell(\boldsymbol{\beta},\boldsymbol{\gamma}):=\frac{1}{2}\sum_{i=1}^{n}T_{i}\left\{(\mathbf{x}_{i}^{\top}\boldsymbol{\beta})+\boldsymbol{\gamma}^{\top}\boldsymbol{\Sigma}_{i}\boldsymbol{\gamma}\cdot\exp\left(-\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)\right\}+\lambda\|\boldsymbol{\beta}\|_{1},\\ \text{such that}&\boldsymbol{\gamma}^{\top}\mathbf{H}\boldsymbol{\gamma}=1.\end{array}\tag{2}$$

One may express the objective function as ℓ(β, γ) = Ln(β, γ) + P(β), wherein the first component denotes the negative log-likelihood and the second denotes the regularization.

The first component employs an estimator, denoted by Σˆi, to approximate the true covariance matrix, Σi.

Under the normally assumption and likelihood criterion, Σˆi = Si =PTi t=1 yity
⊤
it/Tiis the sample covariance matrix as introduced in Zhao et al. (2021). To identify γ, a quadratic constraint concerning a positive definite matrix (H) is necessary, analogous to the principal component analysis (PCA) principle. With a likelihood-based objective function, H is set to be the average of the Σˆi's with H =Pn i=1 TiΣˆi/Pn i=1 Ti to incorporate distributional information (see also the discussion in Zhao et al., 2021).

When the value of q significantly exceeds that of n (a high-dimensional scenario), the problem becomes challenging due to the rank deficiency of the design matrix. To address this issue, a regularization component, P(β), is introduced. Examples include the ℓ1-regularization (Tibshirani, 1996) and its extensions. Existing findings also guarantee both estimation consistency and selection consistency under mild conditions. A generalization to the current model setting with covariance matrices as the outcome will be comprehensively discussed in Section 2.2.

The present study considers an optimization problem of (2), which exhibits biconvexity. Following the approach utilized in Zhao et al. (2021), we consider a high-dimensional block coordinate descent algorithm that is well-suited for fitting model parameters, γ and β. The procedure is described in Algorithm 1. To enhance the likelihood of escaping from local minima, we recommend adopting a randomized approach to selecting initial values, followed by selecting the estimate that yields the lowest value of the objective function.

Similar to Algorithm 2 in Zhao et al. (2021), when there are higher-order components, it is possible to first remove the identified components and utilize the updated data for estimating the succeeding component. This estimation involves incorporating an orthogonality constraint, ensuring the newfound component is orthogonal to the previously identified ones. To determine the number of projections, the same metric introduced by Zhao et al. (2021) is utilized, which quantifies the "deviation from diagonality" of the projected matrices. Let Γ(k) ∈ R
p×k denote the first k estimated components, the average deviation from diagonality is defined as

$$\mathrm{DfD}\left(\Gamma^{(k)}\right)=\prod_{i=1}^{n}\left(\frac{\operatorname*{det}\left\{\operatorname{diag}\left(\Gamma^{(k)\top}\mathbf{S}_{i}\Gamma^{(k)}\right)\right\}}{\operatorname*{det}\left(\Gamma^{(k)\top}\mathbf{S}_{i}\Gamma^{(k)}\right)}\right)^{T_{i}/\sum_{i}T_{i}},$$
5
where diag(A) represents a diagonal matrix comprising the diagonal elements of a square matrix A, and det(A) is the determinant of A. If Γ(k)is a shared diagonalization of Si's, meaning Γ(k)⊤SiΓ
(k)is a diagonal matrix, for ∀ i = 1*, . . . , n*, then DfD Γ
(k)= 1. In practice, the selection of k can occur before DfD
significantly deviates from one or before a sudden increase takes place.

Algorithm 1 The optimization algorithm for problem (2).

Input: Y: a list of data where the ith element a Ti × p data matrix; X: an n × q matrix of covariates with the first column of ones.

1: Initialization: β
(0), γ
(0)
2: repeat for iteration s = 0, 1, 2*, . . .*, given β
(s), γ
(s), for the (s + 1)th step:
3: (1) update β by solving

$${\frac{1}{2}}\sum_{i=1}^{n}T_{i}\left\{\left(\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)+\gamma^{(s)}{}^{\top}\mathbf{S}_{i}\gamma^{(s)}\cdot\exp\left(-\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)\right\}+\lambda\|\boldsymbol{\beta}\|_{1};$$

4: (2) update γ by solving

$$\begin{array}{r l}{{\mathrm{minimize}}}&{{}\quad\gamma^{\top}\left\{{\frac{1}{2}}\sum_{i=1}^{n}T_{i}\exp\left(-\mathbf{x}_{i}^{\top}{\boldsymbol{\beta}}^{(s+1)}\right)\mathbf{S}_{i}\right\}\gamma,}\\ {{\mathrm{such~that}}}&{{}\quad\gamma^{\top}\mathbf{H}\gamma=1;}\end{array}$$

5: until the objective function in (2) converges. 6: Consider a random series of initializations, repeat Steps 1–5, and choose the results with the minimum objective value.

Output: βˆ, γˆ

## 2.2 Asymptotic Properties

In this section, we establish the estimation consistency and model selection consistency of the proposed approach. We denote the true model parameter as β
∗and the model space under regularization P (for example, the ℓ1-norm) as M = {β ∈ R
p| (β)Sc = 0}, where S is the support of β
∗and S
cis the complement of S. To ensure the desired theoretical properties, we impose the following regularity conditions.

(A1) (Bounded observations) For a random feature vector x˜ ∈ R
q−1, ∥x˜∥∞ ≤ C0 and E(|Y|) < ∞.

(A2) (Bounded eigenvalues) The eigenvalues of Ω = Exix
⊤
i
, denoted as µ(Ω) , are bounded below and above by constants cmin, cmax, such that
0 < cmin ≤ µmin(Ω) < µmax(Ω) ≤ cmax < ∞.

(A3) (Irrepresentability) For τ ∈ (0, 1),

## X⊤ Scx⊤ S †Sign (Β ∗ S ) ∞ ≤ 1 − Τ,

where X = (x1*, . . . ,* xn)
⊤ ∈ R
n×q, XSc is the columns of X in S
c, XS is the columns of X in S, and β
∗
S
is the corresponding elements of β
∗in S. For a matrix A ∈ R
p×p, A†is *Moore-Penrose pseudoinverse* and sign(·) is the sign function.

(A4) (Common eigenstructure) All the covariance matrices share the same set of eigenvectors, denoted as Γi and Γi = Γ, for i = 1*, . . . , n*. For each Σi, there exists (at least) a column, indexed by ji, such that γ = γiji and Model (1) is satisfied.
The random design assumption postulated in Assumption (A1) is a fundamental and prevalent condition in the literature (Song et al., 2020). Additionally, it is reasonable to restrict the range of predictors via appropriate data preprocessing techniques. Assumption (A2) regulates the covariance matrix of x, denoted as Ω. It also serves as the expected Hessian matrix of the considered objective function, which is likelihoodbased. Assumption (A2) is a standard regularity condition, requiring that the eigenvalues of the expected Hessian matrix remain bounded away from zero and infinity. This condition is necessary to guarantee the existence of the maximum likelihood estimate and to ensure the stability of the optimization algorithm.

Assumption (A3) pertains to the irrepresentability condition which necessitates that active predictors are not excessively aligned with inactive predictors. Ideally, the inactive predictors are orthogonal to the active predictors. However, the high dimensionality of the data makes this an impractical assumption. Therefore, Assumption (A3) relaxes the orthogonality requirement to near-orthogonality, enabling greater flexibility in model specification. Assumption (A4) posits that all covariance matrices share an identical eigenspace, irrespective of the order. For i = 1*, . . . , n*, it is assumed that Σi has the eigendecomposition of Σi = ΓiΛiΓ
⊤ i
,
where Λi = diag {λi1*, . . . , λ*ip} is a diagonal matrix and Γi =γi1
, . . . , γipis an orthonormal rotation matrix; {λi1*, . . . , λ*ip} are the eigenvalues and the columns of Γi are the corresponding eigenvectors. Under Assumption (A4), we investigate the theoretical outcomes of the proposed method under the assumption of common principal components.

To begin with, we aim to establish a connection between Assumptions (A1), (A2), and the well-known condition of Restricted Strong Convexity (RSC) introduced by Negahban et al. (2012). The basic concept underlying the definition of RSC is the relaxation of strong convexity, which is unable to hold under the highdimensional setting due to rank deficiency, resulting in vanishing curvature of Ln along certain directions.

The RSC condition ensures the availability of gradient information for the algorithm to navigate towards the optimal solution β
∗despite the absence of strong convexity.

Proposition 1. Assume Assumptions (A1) and (A2) are satisfied and q ≫ n and log q/Mn = o(1)*, where* Mn =Pn i=1 Ti. Then for any given ϵ > 0, there exist positive constants α1, α2, and C *such that for* n ≥ C log(1/ϵ), it holds with probability at least 1 − ϵ *that*

$$\left(\nabla\mathcal{L}_{n}(\beta)-\nabla\mathcal{L}_{n}\left(\beta^{\star}\right)\right)^{\top}\left(\beta-\beta^{\star}\right)\geq\alpha_{1}\left\|\beta-\beta^{\star}\right\|_{2}^{2}-\alpha_{2}\sqrt{\frac{\log q}{M_{n}}}\left\|\beta-\beta^{\star}\right\|_{1}^{2},\quad\forall\ \beta\in\mathbb{B}_{2}\left(r;\beta^{\star}\right),\tag{3}$$  $\left(\beta-\beta^{\star}\right)$
7
where B2(r; β
∗) *is a compact region containing* β
∗ with radius r*. Inequality* (3) is the restricted strong convexity.

Then We first discuss the asymptotic property of our β estimator given the true γ. Incorporating the RSC and Assumption (A3), the present study advances a novel theorem that closely resembles Theorem 3.4 in Lee et al. (2015).

Theorem 2. Under RSC and Assumption (A3), for some τ defined in Assumption (A3), constants κ, c1, c2 and λ = (3κc1/τ )plog q/c2Mn *with* Mn =Pn i=1 Ti, the estimator of β under P *is unique, and with probability at least* 1 − 2q
−5/4,
(1) *estimation consistent:*

$$\left\|\hat{\boldsymbol{\beta}}-\boldsymbol{\beta}^{*}\right\|_{2}\leq\frac{6}{\alpha_{1}}\frac{\kappa}{\tau}c_{1}\left(\sqrt{|S|}+\frac{\tau}{2\kappa}\sqrt{|S|}\right)\sqrt{\frac{\log q}{c_{2}M_{n}}},$$  _at:_
$$\iota t_{*}$$
 $\text{(2)}\text{}$ $model\text{}selection\text{}consistent$
$${\hat{\boldsymbol{\beta}}}\in M,$$

where |S| *is the cardinality of set* S.

The proof of Theorem 2 and values of κ are provided in Supporting Information Section A.3.

## 2.3 Extension

In practice, based on domain knowledge, structural constraints on the predictors are sometimes enforced, instead of imposing pure sparsity. Assuming the predictor structure can be captured by a matrix D ∈ R
r×q, where r is the number of structural constraints, the imposed regularization is then P(β) = ∥Dβ∥1. We refer to these problems as the generalized lasso (Tibshirani and Taylor, 2011). Example choices of D include the fused lasso, trend filtering, wavelet smoothing, and a method for outlier detection. In our neuroimaging application, the goal is to evaluate whether brain white matter integrity regulates brain functional connectivity. Local constancy and smoothness within each functional module are imposed on the structural imaging data (Grosenick et al., 2013), and the fused lasso regularization is particularly well-suited.

We consider the following optimization problem under structured constraints.

$$\begin{array}{ll}\underset{\boldsymbol{\beta},\boldsymbol{\gamma}}{\text{minimize}}&\ell(\boldsymbol{\beta},\boldsymbol{\gamma})=\frac{1}{2}\sum_{i=1}^{n}T_{i}\left\{\left(\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)+\boldsymbol{\gamma}^{\top}\mathbf{S}_{i}\boldsymbol{\gamma}\cdot\exp\left(-\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)\right\}+\lambda\|\mathbf{D}\boldsymbol{\beta}\|_{1},\\ \text{such that}&\boldsymbol{\gamma}^{\top}\mathbf{H}\boldsymbol{\gamma}=1.\end{array}$$

When the matrix D is invertible, let θ ≡ Dβ (β = D−1θ), it reparameterizes the problem with θ and the same approaches can be utilized followed by the asymptotic consistency. When D is not invertible, to guarantee the theoretical properties of the generalized lasso, an adapted version of the third condition (A3)
is introduced.

Let β
∗denote the true model parameter and M′ = {β ∈ R
q| (Dβ)S′c = 0} denote the model space under regularization P(β) = ∥Dβ∥1, where S
′is the support of Dβ
∗and S
′cis the complement of S
′. The following irrepresentability condition is assumed.

(A3′) (Irrepresentability) For τ ∈ (0, 1),

$$\left\|\mathbf{D}_{S^{\prime\epsilon}}\mathbf{X}^{\mathsf{T}}\left(\mathbf{D}_{S^{\prime}}\mathbf{X}^{\mathsf{T}}\right)^{\dagger}\operatorname{sign}\left\{(\mathbf{D}\boldsymbol{\beta}^{*})_{S^{\prime}}\right\}\right\|_{\infty}\leq1-\tau.$$

This adapted version of the irrepresentability condition requires that the active predictors, concerning D, should not be overly well-aligned with the inactive predictors. The following theorem is an analogy to Theorem 2 for the generalized lasso. Theorem 3. *Under RSC and Assumption (A*3
′), for some τ *defined in Assumption (A*3
′*), constants* κ
′, c′1
, c′2 and λ = (3κ
′c
′
1/τ )plog q/c′2Mn *with* Mn =Pn i=1 Ti, the estimator of β under P is unique, and with probability at least 1 − 2q
−5/4,
(1) *estimation consistent:*

$$\left\|\hat{\beta}-\beta^{*}\right\|_{2}\leq\frac{6}{\alpha_{1}}\frac{\kappa^{\prime}}{\tau}c_{1}^{\prime}\left(\sqrt{|S^{\prime}|}+\frac{\tau}{2\kappa^{\prime}}\sqrt{|S^{\prime}|}\right)\sqrt{\frac{\log q}{c_{2}^{\prime}M_{n}}},$$

(2) *model selection consistent:*

$$\hat{\beta}\in{\cal M}^{\prime}.$$

## 3 Inference 3.1 Method

In general, it is often necessary to make statistical inferences on the estimated model coefficients, such as to evaluate the significance of the effect of a covariate or to obtain confidence intervals of the coefficient estimates. However, when faced with high-dimensional covariates, the resulting estimates are typically biased, rendering additional challenges. This is evident in the use of a lasso-type of estimation in the preceding section. To overcome this obstacle, we utilize a "split-and-smooth" approach (Fei and Li, 2021),
which combines low-dimensional estimations with prior variable selection to correct for bias in the highdimensional problem. In the following discussion of inference on β, it is assumed that the projection vector, γ, is given, either prespecified or using the estimate from the full dataset. Based on the formulation in Model (1), define zi ≡PTi t=1(γ
⊤yit)
2, and consider it as the response variable. Notably, after standardization, zi has been shown to follow a chi-squared distribution, a member of the exponential distribution family. Consequently, fitting Model (1) between the predictor xi and zi corresponds to solving a generalized linear model (GLM) problem.

We consider n subjects of observed data C(n) = (Y, X) = {(Yi, xi) | 1*, . . . , n*}, where Y = {Y1*, . . . ,* Yn},
Yi = (yi1*, . . . ,* yiTi
)
⊤ ∈ R
Ti×p and X = (x1*, . . . ,* xn)
⊤ ∈ R
n×q. For Model (1), a sparsity condition is imposed where the number of nonzero coefficients is small relative to the sample size. More details will be explained in the upcoming subsection. Considering a high-dimensional problem, a data-splitting approach is employed as an initial step. For instance, the observed dataset is divided into two mutually exclusive subsets, denoted as C1 = (Y1, X1) and C2 = (Y2, X2), of sizes n1 and n2 respectively, with n1+n2 = n. The former subset, C1, is used for dimension reduction, where a variable selection technique (denoted as Sλ, where λ is the tuning parameter used in the technique) is implemented and a subset of predictors, denoted as Sˆ ⊆ {1*, . . . , q*}, is selected. The second dataset, C2, is utilized to fit low-dimensional models of (1) using Y2 and X2Sˆ+j
, where Sˆ+j = {j} ∪ Sˆ, for j = 1, 2*, . . . , q*. Let β˜Sˆ+j denote the corresponding maximum likelihood estimate and β˜j =
β˜Sˆ+j j denote the element corresponding to the jth predictor. Note that, the first column of X are ones, thus, β˜1 is the estimate of the intercept. The estimate of the model coefficients from one data split, namely single-splitting estimator, is then obtained and denoted as β˜ = (β˜1*, . . . ,* β˜q)
⊤ ∈ R
q.

Utilizing a single-split estimator is recognized with high variability, primarily due to the nature of random data splitting. This heightened variability poses a challenge in distinguishing genuine signals from noise, a recurrent issue encountered in bagging algorithms (B¨uhlmann and Yu, 2002). To address this issue, we are considering implementing a multi-splitting strategy. We repeat the above single-splitting procedure for B
times, where B is a large number. Denote Cb1 and Cb2 as the two subsets of the bth splitting with |Cb1 | = n1 and |Cb2 | = n2, for b = 1*, . . . , B*. We apply Sλ on Cb1 to obtain the estimate of the active set, Sˆb, and yield the estimate of model coefficients by fitting a low-dimensional model using Cb2
, denoted as β˜
b= (β˜b 1
, . . . , β˜b q
)
⊤.

Then, these B estimates of model coefficients are averaged over all splits to attain a smoothed coefficient estimate, defined as

$$\hat{\mathbf{\beta}}=\left(\hat{\beta}_{1},\ldots,\hat{\beta}_{q}\right)^{\top},\text{where}\hat{\beta}_{j}=\frac{1}{B}\sum_{b=1}^{B}\hat{\beta}_{j}^{b},\text{for}j=1,\ldots,q.\tag{4}$$
9
The process for the multi-splitting estimator βˆj is detailed in Algorithm 2. The subsequent subsection will delve into the theoretical properties of this procedure, enabling the construction of a confidence interval for βˆj to facilitate inference.

## Algorithm 2 The Multi-Splitting Estimator

Input: Y: a list of data, where the ith element is a Ti × p matrix; X: an n × q matrix of covariates with the first column of ones; γˆ: a p-dimensional vector denoting the prespecified or estimated projection vector obtained from Algorithm 1; Sλ: a variable selection procedure; n1, n2: sample sizes for splitting; B: the number of random splits.

1: for b = 1, 2*, . . . , B* do 2: Split the samples into Cb1 and Cb2
, withCb1
 = n1 andCb2
 = n2.

3: With given γˆ, apply Sλ to Cb1 to select predictors indexed by Sˆb ⊂ {1*, . . . , q*}.

4: for j = 1*, . . . , q* do 5: With Sˆb+j = {j} ∪ Sˆb, fit model (1) using Yb2 and Xb2 Sˆ+j with γ = γˆ and obtain the estimate of model coefficients, denoted as β˜
b Sˆ+j
.

6: Let β˜b j =
β˜
b Sˆb+j j
, which is the coefficient for predictor Xj .

7: end for 8: Set β˜
b=
β˜b 1
, . . . , β˜b q
⊤.

9: end for 10: Compute βˆ =
βˆ1*, . . . ,* βˆq
⊤, where βˆj =
1 B
PB
b=1 β˜b j Output: βˆ.

## 3.2 Asymptotic Properties

According to the model selection consistency outlined in Theorem 2, the sure screening property is readily satisfied under regularity conditions. Assuming γ is known, similar properties as those in Fei and Li (2021)
can be derived. Define the *observed information* as ˆI(β) = 1/2MnPn i=1 Ti exp −x
⊤
i β γ
⊤yit· y
⊤
itγxix
⊤ i
,
the *expected information* as I
∗ = E{
ˆI(β
∗)}, where β
∗is the true model parameter. For S ⊆ {1, 2*, . . . , q*},
the support of β
∗, we have an estimation Sˆ ⊇ S and xiS, βS are subvectors of xi and β only containing elements indexed by S, respectively. Moreover, S+j = S ∪ {j} and S−j = S\{j}. Similarly, define the observed sub-information by ˆISˆ(βSˆ) = 1/2MnPn i=1 Ti exp −x
⊤
iSˆβSˆ
 γ
⊤yit· y
⊤
itγxiSˆx
⊤
iSˆ
and the expected sub-information by ISˆ = E{
ˆISˆ(β
∗
Sˆ)} = I
∗
Sˆ
, which is the submatrix of I
∗ with rows and columns indexed by Sˆ.

The asymptotic properties of the single-splitting estimator are outlined in Theorem 4, demonstrating its consistency and normality. However, due to its utilization of only n1 subjects, it exhibits reduced efficiency. In contrast, a multi-splitting strategy is employed to address the high variability associated with data splitting, yielding a smoothed estimator denoted as βˆ. The subsequent Theorem 5 details the asymptotic properties of this smoothed estimator.

Theorem 4. When the dimension of the predictors is divergent with sample size n, consider the singlesplitting estimator β˜ = (β˜1*, . . . ,* β˜q)
⊤. With known γ, denote m = |Sˆ| and σ˜
2 j =
nI
∗
Sˆ+j o−1 jj
, for j ∈ {1, . . . , q}*. Let* T = mini Ti and M1 n =Pn i=1 Ti. As n, T → ∞,

(1)
$$\left\|\vec{\beta}_{S_{+j}}-\beta_{S_{+j}}^{*}\right\|_{2}^{2}=o_{p}\left(m/M_{n}^{1}\right),\,\,\,i f\,m\log m/M_{n}^{1}\rightarrow0.$$
$$({\mathcal{Q}})$$
$$\frac{\sqrt{M_{n}^{1}}\left(\tilde{\beta}_{j}-\beta_{j}^{s}\right)}{\tilde{\sigma}_{j}}\stackrel{\mathcal{D}}{\longrightarrow}\mathcal{N}(0,1),\,\,\,i f\,m^{2}\log m/M_{n}^{1}\rightarrow0.$$
Theorem 5. Under an additional partial orthogonality condition that {xj , j ∈ S} are independent of {xi*, i /*∈
S}. Repeat random data splitting for B *times and obtain the multi-splitting estimator* βˆ = (βˆ1*, . . . ,* βˆq)
⊤
defined in (4). With known γ, denote m = |S| and σˆ
2 j =
nI
∗
S+j o−1 jj
, for j ∈ {1, . . . , q}*. Let* T = mini Ti and Mn =Pn i=1 Ti. As n, T, B → ∞,

$$\frac{\sqrt{M_{n}}\left(\hat{\beta}_{j}-\beta_{j}^{*}\right)}{\hat{\sigma}_{j}}\stackrel{\mathcal{D}}{\longrightarrow}\mathcal{N}(0,1).$$

The theoretical analysis above suggests that the variance of estimating βˆj , referred to as ˆσ 2 j
, relies on the unknown active set, S, while accounting for the data variation across B random splits. Thus, it is impossible to compute ˆσ 2 j directly in an analytical form. Instead, one can estimate the variance component by employing the infinitesimal jackknife method (Efron, 2014), denoted as Vˆj . In scenarios where we have obtained a reliable approximation of the estimating variance ˆσ 2 j
, for 0 *< α <* 1, the asymptotic 1 − α confidence interval for βˆj (j = 1*, . . . , q*) is given by

$$\left(\hat{\beta}_{j}-\Phi^{-1}(1-\alpha/2)\sqrt{\hat{V}_{j}},\hat{\beta}_{j}+\Phi^{-1}(1-\alpha/2)\sqrt{\hat{V}_{j}}\right),$$

where Φ(·) is the cumulative distribution function of the standard normal distribution. The p-value for testing H0 : β
∗
j = 0 is

$$2\times\left\{1-\Phi\left(|\hat{\beta}_{j}|/\sqrt{\hat{V}_{j}}\right)\right\}.$$

The procedure for estimating the variance component of the multi-splitting estimator βˆj is outlined in Algorithm A.1, presented in the Appendix A.1. Additionally, a comprehensive derivation procedure for the approximate variance will be provided. It's noteworthy that when γ is estimated, such as the maximum likelihood estimator (MLE) of γ, the asymptotic properties of βˆj also hold due to the consistency of the profile likelihood estimator.

## 4 Simulation

In this section, we evaluate the performance of the proposed approaches for coefficient estimation and inference with high-dimensional covariates and covariance matrix outcomes via simulation studies.

For yit, data dimension is set to p = 5 and data are generated from a multivariate normal distribution with mean zero and covariance matrix Σi. The covariance matrix has the eigendecomposition of Σi = ΓΛiΓ
⊤,
where Γ = (γ1
, . . . , γp
)
⊤ is the orthonormal eigenvector matrix assumed to be identical across units and Λi = diag{λi1*, . . . , λ*ip} is a diagonal matrix containing p distinct eigenvalues. For the covariates, a dimension of q = 200 is considered, including the intercept column. x˜i's are generated from a (q − 1)-dimensional standard normal distribution. Two scenarios are tested in the simulation. (i) The null case, where the eigenvalues, λij , are generated from a log-normal distribution with mean zero and variance of 0.5 2. (ii) The alternative case, where the second (denoted as C2) and third (denoted as C3) eigenvalues are assumed to satisfy the log-linear model (1). That is for these two components, λij = exp x
⊤
i β, where xi = (1, x˜
⊤ i
)
⊤.

Under the alternative, β is defined as follows. The intercept term is a random number between −10 and 10. The indices of the active set of C2 is {10, 20, 30} with β values (2, 2, −2), C3 is {15, 25, 35} with β values (1, −1, 1) and those of other components equal to zero except intercept term. Under the above model settings, Assumptions (A1)–(A3) are satisfied. When implementing the proposed approach, the number of components is determined using the average DfD (degrees of freedom difference Zhao et al., 2019) with a threshold of two. The proposed methods employ the asymptotic variance in Theorem 5. The multi-splitting procedure introduced in Algorithm 2 is performed with B = 200 to construct the confidence intervals. All the simulations are repeated 200 times.

We first examine the validity of the proposed method across varying covariate dimensions. We consider two cases: q = 200 and q = 500, with a fixed sample size n = 100 and Ti = T = 100 for all i. Table 1 displays the performance in estimating and conducting inference on β. In the instance of high-dimensional covariates, the estimated βˆ from the proposed methods closely aligns with the true values in both components.

The coverage probability, derived from the asymptotic variance, successfully achieves the designated level of α = 0.05 for both components, while keeping the mean squared error (MSE) at a minimal level. It is noteworthy that for particularly large covariate dimensions (e.g., q = 500), unsatisfactory results are obtained for C3, while still achieving positive results for C2. To assess the accuracy of estimating γ, we use |⟨γˆ, γ*⟩| →* 1 as a metric for the estimation error, where |⟨·, ·⟩| represents the inner product of two vectors.

Table 2 displays the performance in estimating γ. The proposed method yields accurate estimates in both components with a high correlation to the truth in the case where q = 200. These results collectively indicate that the proposed methods effectively capture the underlying relationships and offer reliable inference in this simulation scenario. Table 1: Estimate and inference on β in the simulation study. The results are averages over 200 simulations.

| β10       | β25   |           |            |      |       |             |             |      |      |
|-----------|-------|-----------|------------|------|-------|-------------|-------------|------|------|
| Component | Truth | Est. (SE) | CP         | MSE  | Truth | Est. (SE)   | CP          | MSE  |      |
| C2        | 2     | 2(0.03)   | 0.97       | 0.01 | 0     | -0.01(0.03) | 0.98        | 0.02 |      |
| q=200     | C3    | 0         | 0.01(0.01) | 0.93 | 0.01  | -1          | -0.99(0.01) | 0.94 | 0.01 |
| C2        | 2     | 2(0.02)   | 0.98       | 0.06 | 0     | 0.02(0.02)  | 0.97        | 0.12 |      |
| q=500     | C3    | 0         | 1.24(0.01) | 0.11 | 1.79  | -1          | -0.04(0.01) | 0.05 | 0.97 |

| γ1    | γ2    | γ3     | γ4     | γ5     | |⟨γˆ, γ⟩| (SE)   |               |
|-------|-------|--------|--------|--------|------------------|---------------|
| Truth | 0.447 | -0.862 | 0.138  | 0.138  | 0.138            | 0.816 (0.142) |
| C2    | Est.  | 0.460  | -0.858 | 0.135  | 0.140            | 0.123         |
| Truth | 0.447 | 0.138  | -0.862 | 0.138  | 0.138            | 0.829 (0.126) |
| C3    | Est.  | 0.425  | 0.138  | -0.868 | 0.174            | 0.132         |

To further assess the finite sample performance of the proposed methods, we conduct experiments, varying the number of units (n = 100, 200, 500), the number of observations (Ti = T = 100, 200, 500), and fixing the dimension of the covariates (q = 200). The emphasis is on evaluating the ability to identify nonzero coefficients in each component. The results, displayed in Figure 1, include the estimates, coverage probability derived from the asymptotic variance, and the mean squared error (MSE) of the target model coefficients for

![14_image_0.png](14_image_0.png)

both components. The figure illustrates that as both n and Tiincrease, the estimates of β20 in C2 and β40 in C3 converge to their true values, 2 and 0, respectively. The coverage probability of β20 in C2 converges to the designated level of 0.95 as both n and Tiincrease, while the coverage probability of β40 in C3 fluctuates around 0.95. The MSEs of estimating β in both components converge to zero as n and Tiincrease. These findings suggest that the proposed methods demonstrate promising performance in terms of accuracy and reliability as both the sample size and the number of observations increase.

Additionally, we conduct an investigation to assess the impact of changes in the dimensionality of the response variable y on the performance and present the results in Table 3. The results illustrate that the proposed method remains remarkably robust to increases in the dimension of y, as long as p < mini Ti. This observation emphasizes the reliability and effectiveness of our method across various scenarios.

| β10       | β25   |            |            |      |       |             |             |      |      |
|-----------|-------|------------|------------|------|-------|-------------|-------------|------|------|
| Component | Truth | Est. (SE)  | CP         | MSE  | Truth | Est. (SE)   | CP          | MSE  |      |
| C2        | 2     | 2(0.03)    | 0.97       | 0.01 | 0     | -0.01(0.03) | 0.98        | 0.02 |      |
| p=5       | C3    | 0          | 0.01(0.01) | 0.93 | 0.01  | -1          | -0.99(0.01) | 0.94 | 0.01 |
| C2        | 2     | 2(0.03)    | 0.98       | 0.01 | 0     | 0.02(0.03)  | 0.96        | 0.01 |      |
| p=20      | C3    | 0          | 0.02(0.02) | 0.99 | 0.01  | -1          | -0.95(0.05) | 0.99 | 0.01 |
| C2        | 2     | 2.01(0.05) | 0.89       | 0.02 | 0     | -0.02(0.04) | 0.98        | 0.01 |      |
| p=50      | C3    | 0          | 0.01(0.02) | 0.99 | 0.01  | -1          | -1(0.01)    | 0.99 | 0.01 |

## 5 Application

We apply the proposed approach to the Lifespan Human Connectome Project (HCP) Aging Study. As an extension of the HCP study of healthy young adults, the Lifespan study utilizes the developed technological advances to offer a high-quality dataset across the human lifespan. The Aging study, in particular, aims to explore a typical aging trajectory and how brain connectome varies among mature and older adults. In this study, the association between two imaging modalities, diffusion tensor imaging (DTI) and restingstate functional magnetic resonance imaging (fMRI), is investigated. DTI is an MRI technique that offers an assessment of brain structural connectivity by tracing the diffusion process of water molecules along white matter fiber bundles. Resting-state fMRI, on the other hand, offers an assessment of the so-called brain functional connectivity, where the fMRI technique measures the blood oxygen level-dependent as a surrogate of neural activity. Hebb's law postulates that frequently communicated brain regions are more likely the consequences of direct structural connections (Hebb, 2005). Existing literature also suggested that brain structural connectivity shapes and regulates the dynamics of cortical circuits and systems captured by functional connectivity (Sporns, 2007). Thus, in this study, the output from DTI is considered as the predictor (X), and the output from resting-state fMRI is considered as the outcome (Y ). A total of n = 564 subjects aged between 36 and 90 (307 Female and 257 Male) with both the resting-state fMRI and DTI available without quality control concerns are analyzed. The fMRI data were minimally preprocessed (Glasser et al., 2013). Signals (yit) are extracted from p = 75 brain regions (60 cortical and 15 subcortical regions)
using the Harvard-Oxford atlas in FSL (Smith et al., 2004) and motion-corrected. The DTI data were preprocessed using developed pipelines for noise reduction, motion, and distortion correction (more details are described in Hall et al., 2022). The Desikan atlas (Desikan et al., 2006) is considered for brain parcellation, which divides the brain into q = 84 regions of interest (ROIs). Two regions are considered structurally connected if there exists at least one fiber streamline with two endpoints located in these two regions. After building such a network, the degree of each region is summarized and treated as the predictor (xi). Regions in both the Harvard-Oxford and Desikan atlas are grouped into 10 functional modules. To better interpret fMRI components, γ is sparsified following an ad hoc procedure using a fused lasso regression (Tibshirani et al., 2005) to impose local smoothness and constancy within each functional module (Grosenick et al.,
2013).

Using the DfD criterion, the proposed approach identifies three orthogonal fMRI components, denoted as C1, C2, and C3. Figure 2 presents the brain maps of regions with a nonzero loading in γ in the restingstate fMRI data, along with the corresponding brain maps of regions with a significant β coefficient in the DTI data. The loading profile of all regions is shown in Figure B.1 of the supporting information and the β estimate (together with the 95% confidence interval) of all regions is presented in Figure B.2. Using a river plot, configurations by brain functional modules are demonstrated in Figure B.3. A high proportion of overlapping and sign consistency between nonzero γ's and significant β's is observed in both C1 and C2, consistent with the regulating role of brain white matter integrity on functional connectivity (Jbabdi and Johansen-Berg, 2011). In C3, the overlapping region, the supramarginal gyrus, yields the lowest negative value in both γ and β. A significant portion of the nonzero γ's of all three components are regions in the default mode network (DMN), which is more active during the resting state. However, these three components represent three different subnetworks in the DMN. C1 is considered part of the caudal-temporal DMN related to auditory processing and language comprehension (Gollo et al., 2018). C2 is primarily the cingulate-precuneus DMN suggested to play a role in memory and perception (Laird et al., 2009). For C3, the middle temporal gyrus, inferior parietal gyrus, and supramarginal gyrus have been identified as part of a distinct subnetwork within the DMN referred to as the "temporoparietal junction" subnetwork playing a role in social cognition, attention, and self-referential processing (Leech et al., 2011). In summary, the proposed approach identifies brain networks, as well as associated brain structural predictors, that are consistent with existing knowledge of the human brain.

![17_image_0.png](17_image_0.png)

![17_image_1.png](17_image_1.png)

## 6 Discussion

In this manuscript, we extend a prior work of covariance regression to the scenario with high-dimensional covariates, where a linear projection on the covariance matrices is assumed and a log-linear model on heteroscedasticity is imposed in the projection space. A regularized estimator of the model coefficient, β, is proposed. Integrated with a likelihood-based optimization criterion, the projection, γ, and the model coefficient, β, are identified simultaneously. A novel split-and-smooth procedure is introduced for statistical inference on the estimated model coefficients. Under the assumption of common eigenstructure across covariance matrices, the proposed approach offers asymptotically consistent estimators. Remarkably, our approach stands out for its computational efficiency and estimation reliability requiring fewer assumptions, which is noteworthy as we refrain from making any assumptions regarding the sparsity of the precision matrix of covariates x.

Several challenges lie ahead for future research. Firstly, theoretical properties when relaxing the common eigenstructure assumption to partial common diagonalization assumption are worth investigating. This is particularly pertinent in real-world scenarios, especially when p is relatively large. Secondly, though asymptotic normality of βˆj is achieved following the proposed inference procedure, the exploration of the covariance structure of the entire β vector is a promising avenue for future investigation. Thirdly, the present manuscript focuses on the statistical inference of β, future inquiries into the statistical inference of γ will be valuable, particularly in applications, such as fMRI studies, where identifying significant subnetwork structures is crucial. Lastly, considering scenarios where both the response and covariates are high-dimensional, that is both p and q are large, opens up avenues for developing methods and theoretical results tailored to such situations.

## Appendix

This Appendix collects additional theoretical results, the technical proof of the theorems in the main text, and additional data analysis results.

## A Additional Theoretical Results A.1 The Variance Estimation

To define the variance of estimating βˆj in Theorem 5, let β˜b j = ψ(Cb2
) be the estimate given by the bth splitting, where ψ(·) is a general function that maps the data to the estimator. Let Nib ∈ {0, 1} indicate whether or not the ith unit was sampled in Cb2
. Using the infinitesimal jackknife method, a biased-corrected estimation of the variance of βˆj is introduced as the following. For the jth model coefficient,

$$\hat{V}_{j}=\frac{n-1}{n}\left(\frac{n}{n-n_{1}}\right)^{2}\sum_{i=1}^{n}\widehat{\text{Cov}}_{ij}^{2}-\frac{n}{B^{2}}\frac{n_{1}}{n-n_{1}}\sum_{b=1}^{B}(\hat{\beta}_{j}^{b}-\hat{\beta}_{j})^{2},$$ (A.1)
where

$$\widehat{\mathrm{Cov}}_{ij}^{2}=\frac{1}{B}\sum_{b=1}^{B}\left(N_{ib}-\frac{1}{B}\sum_{b=1}^{B}N_{ib}\right)\left(\hat{\beta}_{j}^{b}-\hat{\beta}_{j}\right)$$ (A.2)  the estimates, $\hat{\beta}_{i}^{b}$, and the sampling indicators, $N_{ib}$, with respect to the $B$ splits.  
is the covariance between the estimates, β˜b j
, and the sampling indicators, Nib, with respect to the B splits.

The initial term of Vˆj is consistent with *V ar*(βˆj ) as demonstrated in Theorem 1 of Wager and Athey (2018),
while the second term of Vˆj is designed to correct bias tailored to the sub-sampling scheme. The process for estimating the variance component of the multi-splitting estimator βˆj is summarized in Algorithm A.1.

Algorithm A.1 Estimate the variance of the multi-splitting estimator of β.

Input: n1, n2: sample sizes for splitting; B: the number of random splits;

$D$. the number of random spins,  $$\widehat{\boldsymbol{\beta}}^{b}=\left(\widehat{\beta}_{1}^{b},\ldots,\widehat{\beta}_{q}^{b}\right)^{\top},b=1,2,\ldots,B;$$ $$\widehat{\boldsymbol{\beta}}=\left(\widehat{\beta}_{1},\ldots,\widehat{\beta}_{q}\right)^{\top};$$  1: **for**$j=1,\ldots,q$**do**  2: Compute  $$\widehat{\operatorname{Cov}}_{ij}^{2}=\frac{1}{B}\sum_{b=1}^{B}\left(N_{ib}-N_{i\cdot}\right)\left(\widehat{\beta}_{j}^{b}-\widehat{\beta}_{j}\right),$$
where Nib ∈ {0, 1} indicate whether or not the ith subject was sampled in Cb2
, which is defined above,

and Ni· =
1
and $N_{i}=\overline{B}\bigtriangleup_{b=1}N_{ib}$. 3: Compute $$\hat{V}_{j}=\frac{n-1}{n}\left(\frac{n}{n-n_{1}}\right)^{2}\sum_{i=1}^{n}\widehat{\operatorname{Cov}}_{ij}^{2}-\frac{n}{B^{2}}\frac{n_{1}}{n-n_{1}}\sum_{b=1}^{B}(\hat{\beta}_{j}^{b}-\hat{\beta}_{j})^{2}.$$ 4: **end for**  5: Let $\hat{V}=\left(\hat{V}_{1},\ldots,\hat{V}_{q}\right)^{\top}$.  **Output:**$\hat{V}$.  

## Pb
B=1 Nib. A.2 Proof Of Proposition 1

Proof. The log-likelihood function is:

Ln(β) = 1 2Mn X i∈n x ⊤ i β· Ti +1 2Mn X i∈n γ ⊤Siγ · exp −x ⊤ i β =1 Mn X i∈n X Ti t=1 ℓit. ℓ ′ it(β) = − 1 2 xi + 1 2 exp −x ⊤ i β γ ⊤yity ⊤ itγxi ℓ ′′ it(β) = − 1 2 exp −x ⊤ i β γ ⊤yity ⊤ itγxix ⊤ i
Thus, ⟨∇Ln(β) − ∇Ln (β ∗), β − β ∗⟩ =1 Mn X i∈n X Ti t=1 µx ⊤ i β− µx ⊤ i β ∗ x ⊤ i (β − β ∗) =1 Mn X i∈n X Ti t=1 µ ′x ⊤ i β ∗ + vx ⊤ i (β − β ∗) x ⊤ i (β − β ∗)2 where µx ⊤ i β= 1 2 exp −x ⊤ i β γ ⊤yity ⊤ itγ.
Then from the proof in Negahban et al. (2012), there exist positive constants κ1 and κ2 such that

$$\langle\nabla{\mathcal{L}}_{n}(\beta)-\nabla{\mathcal{L}}_{n}\left(\beta^{*}\right),\beta-\beta^{*}\rangle\geq\kappa_{1}\|\Delta\|_{2}\left(\|\Delta\|_{2}-\kappa_{2}{\sqrt{\frac{\log P}{M_{n}}}}\|\Delta\|_{1}\right),\quad\forall\beta\in\mathbb{B}_{2}\left(1;\beta^{*}\right)$$

with probability at least 1 − c1 exp (−c2n), for some c1, c2 > 0. The result follows from the basic arithmetic inequality 2ab ≤ (a + b)
2.

Proof. We assume that the sample fisher matrix Σ satisfies the RSC condition, and it is not difficult to find ˆ
that

that  $$\hat{\Sigma}=\frac{1}{2M_{n}}\sum_{i=1}^{n}T_{i}\exp\left(-\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)\left(\boldsymbol{\gamma}^{\top}\mathbf{y}_{it}\mathbf{y}_{it}^{\top}\boldsymbol{\gamma}\right)\mathbf{x}_{i}\mathbf{x}_{i}^{\top},$$  $$\nabla\mathcal{L}_{n}(\boldsymbol{\beta})=-\frac{1}{2M_{n}}\sum_{i=1}^{n}T_{i}\mathbf{x}_{i}+\frac{1}{2M_{n}}\sum_{i=1}^{n}T_{i}\exp\left(-\mathbf{x}_{i}^{\top}\boldsymbol{\beta}\right)\left(\boldsymbol{\gamma}^{\top}\mathbf{y}_{it}\mathbf{y}_{it}^{\top}\boldsymbol{\gamma}\right)\mathbf{x}_{i}$$  Since data $\{x_{i},y_{it}\}$ satisfies the following regression model with a logarithmic link function:
$$\log(\gamma^{\top}\Sigma_{i}\gamma)=x_{i}^{\top}\beta$$
we can reasonably assume there exist a finite bound that | exp −x
⊤
i β γ
⊤yity
⊤
itγ| < ξ.

We can adaptly apply Theorem 3.4 in Lee et al. (2015), before that, we compute the constants κρ, κϱ and κIC. Since the regularizer is finite (it's a norm), its dual semi-norm is finite. To keep things simple, we let ϱ = *∥ · ∥*1. Denote M = span (B∞,S ), the constant κρ = κϱ is

$$\kappa_{\rho}=\operatorname*{sup}_{\beta}\left\{\|\beta\|_{1}\mid\beta\in{\mathcal{M}}\right\}={\sqrt{|{\mathcal{S}}|}}.$$
Meanwhile, denote $X^{T}=(\sqrt{T_{1}}\mathbf{x}_{1},\ldots,\sqrt{T_{n}}\mathbf{x}_{n})$, the constant $\kappa_{IC}$ is  $$\kappa_{IC}=\left\|P_{B_{\infty,\mathscr{B}}}\left(\hat{\Sigma}P_{B_{\infty,\mathscr{B}}}\left(P_{B_{\infty,\mathscr{B}}}\hat{\Sigma}P_{B_{\infty,\mathscr{B}}}\right)^{\dagger}P_{B_{\infty,\mathscr{B}}}z-z\right)\right\|_{\infty}$$ $$\leq\left\|X_{S^{c}}^{T}\left(X_{S}^{T}\right)^{\dagger}z_{S}\right\|_{\infty}+\|z_{S^{c}}\|_{\infty}\leq(2-\tau)\|z\|_{\infty}$$

Since the loss function is continuous differentiable, thus any λ < ∞ satisfies the upper bound in Theorem 3.4 of Lee et al. (2015). We check our choice also satisfies the lower bound in Theorem 3.4. By Vershynin
(2010), Proposition 5.10 and a union bound,

$$\mathrm{Pr}\left(\|\nabla\ell\left(\theta^{*}\right)\|_{\infty}>t\right)\leq\mathrm{Pr}\left(\left\|\sum_{i=1}^{n}T_{i}\big{(}\frac{1}{2}\xi-\frac{1}{2}\big{)}\mathbf{x}_{i}\right\|_{\infty}>M_{n}t\right)\leq2\exp\left(-\frac{M_{n}t^{2}}{2\sigma^{2}}+\log p\right).$$
$$20$$
When $\lambda=\frac{8\xi\kappa_{LG}}{\tau}\sigma\sqrt{\frac{\log p}{M_n}}$, . 
 $ \begin{array}{l}\ \Pr\left(\frac{4\kappa I C}{\tau}\left\|\nabla\ell\left({{\theta}^{\star}}\right)\right\|_{\infty}>\frac{8(2-\alpha)}{\alpha}\sigma\sqrt{\frac{\log p}{{{M}_{n}}}}\right)\\\\\ \ \ \leq2\exp(-2\log p+\log p)=2{{p}^{-1}}.\end{array}$  deduce. 
$$\mathbb{D}$$

Finally, conclusion is easy to deduce.

Proof. When α ̸= 0, D is invertible, thus D has a nontrivial null space. Let ϱ = *∥ · ∥*1, the compatibility constants are computed as the following:

κ1 = κIC =  DScX⊤D˜SX⊤−sign (β ∗ S ) ∞ , κ2 = κR = sup β ∥D˜ β∥1 : β ∈ B2 ∩ span D˜ ⊤B∞,Sc ⊥, κ3 = κϱ = sup β ∥β∥1 : β ∈ B2 ∩ span D˜ ⊤B∞,Sc ⊥. R and ϱ are finite, κ1, κ2, κ3 < ∞. The rest of the proof can be found in Lee et al. (2015).

$$\square$$

Proof. As a result of the data split, C1 and C2 are mutually exclusive, leading to the independence of Sˆ,
derived from C1, from C2 = Y2, X2. To analyze the asymptotic properties of single-splitting estimator βeSˆ+j when the number of parameters m diverges, we employ the techniques and findings from He and Shao
(2001). Without loss of generality and for the sake of notation simplicity, let us consider the case where j = 1 ∈ Sˆ. The argument holds true if 1 ∈/ Sˆ or for any other j.

To proceed, we first restrict on the event of Ω = nSˆ ⊇ S
o. With sure screening property deduced by theorem 1, assume constants 0 ≤ c ≤ 1/2*, K >* 0, P(Ω) ≥ 1 − K (p ∨ n)
−1−c. Recall that

$$\begin{array}{c}{{\widetilde{\beta}_{\mathcal{S}_{+j}}=\operatorname*{argmin}\ell_{\mathcal{S}}\left(\beta_{\mathcal{S}}\right)=\operatorname*{argmin}_{\beta\in\mathbf{R}^{1\mathcal{S}_{+1}+1}}\ell\left(\beta_{\mathcal{S}};\mathbf{Y}^{1},\mathbf{X}_{\mathcal{S}}^{1}\right);}}\\ {{\widetilde{\beta}_{1}=\left(\widetilde{\beta}_{\mathcal{S}_{+j}}\right)_{1}.}}\end{array}$$

Given Mn random samples (x1, y11),(x1, y12)*, . . . ,*(x1, y1T1
), . . . ,(xn, ynTn
), the likelihood is

 $\mathcal{L}_n(\boldsymbol{\beta})=\sum_{i=1}^n\sum_{t=1}^{T_i}\left(\frac{1}{2}\mathbf{x}_i^\top\boldsymbol{\beta}-\frac{1}{2}\left(\boldsymbol{\gamma}^\top y_{it}y_{it}^\top\boldsymbol{\gamma}\right)\cdot\exp\left(-\mathbf{x}_i^\top\boldsymbol{\beta}\right)\right)$  and 2.2 of He and Shao (2000) in our case, we can verify that ... 
To apply Theorems 2.1 and 2.2 of He and Shao (2000) in our case, we can verify that our Assumptions (A1)
and (A2) will lead to their conditions (C1), (C2), (C4) and (C5) with C = 1, r = 2 and A (Mn, m) = m.

To verify their (C3), we first note that their Dn is our I
∗
Sˆ
. Then for any βSˆ, α ∈ Rm such that ∥α∥2 = 1, a second order Taylor expansion of score function USˆ
βSˆ
around β
∗
Sˆ leads to

$$\left|\alpha^{\mathrm{T}}\mathbf{E}_{{\boldsymbol{\beta}}^{*}}\left(U_{\mathcal{S}}\left(\beta_{\mathcal{S}}\right)-U_{\mathcal{S}}\left(\beta_{\mathcal{S}}^{*}\right)\right)-\alpha^{\mathrm{T}}I_{\mathcal{S}}^{*}\left(\beta_{\mathcal{S}}-\beta_{\mathcal{S}}^{*}\right)\right|\leq O\left(\|\beta_{\mathcal{S}}-\beta_{\mathcal{S}}^{*}\|_{2}^{2}\right)$$

Hence, sup
∥βSˆ−β∗Sˆ∥≤(m/Mn)
1/2
α TEβ∗USˆ
βSˆ
− USˆ
β
∗
Sˆ
 − α TI
∗
Sˆ
βSˆ − β
∗
Sˆ
 ≤ O (m/Mn) = o Mn 1/2, which means their (C3) follows. Thus, by Theorem 2.1 of He and Shao (2000),
βeSˆ − β
∗
Sˆ

2 2
= op m/M1 n given m log m/M1 n → 0. Furthermore, by Theorem 2.2 of He and Shao (2000), if m2log m/M1 n → 0, then

$$\left\|M_{n}^{11/2}\left(\widetilde{\mathbf{\beta}}_{\widetilde{S}}-\mathbf{\beta}_{\widetilde{S}}^{*}\right)+M_{n}^{1-1/2}\left\{I_{\widetilde{S}}^{*}\right\}^{-1}U_{\widetilde{S}}\left(\mathbf{\beta}_{\widetilde{S}}^{*}\right)\right\|_{2}=o_{p}(1)$$

Releasing the restriction on Ω and with P (Ωc) = PSˆ ⊉ S
≤ K (p ∨ n)
−1−c, we would still have βeSˆ − β
∗
Sˆ

2 2
=
op m/M1 n
, given M log M/m1n → 0.

Similarly, we can show M1 n 1/2βeSˆ − β
∗
Sˆ
+ M1 n
−1/2nI
∗
Sˆ
o−1USˆ
β
∗
Sˆ
2
= op(1), if m2log m/M1 n → 0, which can also be written as

$$\widetilde{\boldsymbol{\beta}}_{\hat{S}}-\boldsymbol{\beta}_{\hat{S}}^{*}=-M_{n}^{1-1}\left\{I_{\hat{S}}^{*}\right\}^{-1}U_{\hat{S}}\left(\boldsymbol{\beta}_{\hat{S}}^{*}\right)+r_{M_{n}^{1}},$$

withrM1n 2 2
= op 1/M1 n
. Consequently, by taking α = (0, 1, 0*, . . . ,* 0)T and left-multiplying both sides by M1 n 1/2α T, we have

$$\sqrt{M_{n}^{1}}\left(\widetilde{\beta}_{1}-\beta_{1}^{*}\right)/\widetilde{\sigma}_{1}\stackrel{d}{\rightarrow}N(0,1),$$
$$\square$$

$$\mathrm{where}\ {\widetilde{\sigma}}_{1}^{2}=\left(\left\{I_{\widetilde{S}}^{*}\right\}^{-1}\right)_{11}.$$

Similar to Lemma 4 in Fei and Li (2021), we apply the lemma here to our case without proof.

Lemma A.1. With model and Assumptions (A1) and (A2), consider the estimator βeSˆ *with respect to subset* Sˆ as defined above. Denote by m = |Sˆ|*. If* m log m/Mn → 0*, then with probability going to* 1,
βeSˆ
∞
≤ Cβ, where Cβ > 0 *is a constant depending on* cmin, cmax, cβ.

Now we use the Lemma to prove the result of Theorem 5.

Proof. We define the oracle estimators of β
∗
j on the full data (Y, X) and the b-th subsample Cb2 respectively, where the candidate set is the true set S and |S| = s0:

βˇS+j = argmin β∈Rs0+1 ℓS+j βS+j = argmin β∈Rs0+1 ℓS+j βS+j ; Y, XS+j , βˇj = βˇS+j  j ; βˇ b S+j = argmin β∈Rs0+1 ℓ b S+j βS+j = argmin β∈Rs0+1 ℓS+j βS+j ; Y1(b), X 1(b) S+j , βˇ b j = βˇ b S+j  j .
By Theorem 4 and given s 2 0 log s0/n → 0, for each j ∈ {1*, . . . , p*},

pM1 n βˇj − β ∗ j /σˇj d→ N(0, 1) as M1 n → ∞, (A.3) where ˇσ 2 j = nI ∗ S+j o−1 jj . With the oracle estimators β˘j 's and β˘b j ,s, we have the following decomposition: pMn βbj − β ∗ j  =pMn βˇj − β ∗ j +pMn βbj − βˇj  =pMn βˇj − β ∗ j +pMn  1 B X B b=1 βeb j − βˇj ! +pMn  1 B X B b=1 βˇb j − βˇj ! +pMn  1 B X B b=1 nβeb j − βˇb j o! =pMn βˇj − β ∗ j  | {z } I . | {z } II | {z } III
The initial two terms in the aforementioned decomposition, which do not encompass various selections S
b's, pertaining to the oracle estimators and the true active set S. We need to show the following, as it will subsequently yield the outcomes articulated in the theorem through the application of Slutsky's theorem.

(a) I/σˇj =
√Mn
$$\left(\beta_{j}-\beta_{j}^{*}\right)/\tilde{\sigma}_{j}\stackrel{a}{\rightarrow}N(0,$$
d→ N(0, 1);
(b) $\Pi=\frac{\sqrt{M_{n}}}{B}\sum_{b=1}^{B}\left\{\tilde{\beta}_{j}^{b}-\tilde{\beta}_{j}\right\}=o_{p}(1)$;  (c) $\Pi\Pi=\frac{\sqrt{M_{n}}}{B}\sum_{b=1}^{B}\left\{\tilde{\beta}_{j}^{b}-\tilde{\beta}_{j}^{b}\right\}=o_{p}(1)$.  
First, (a) holds because of (A.3). To show (b), i.e. II = op(1), we first denote ξb,Mn =
√Mn βˇb j − βˇj
,
then II = PB
b=1 ξb,Mn
/B. Since the sampling indicator vectors, Nib 's (defined in above Appendix A.1)
are i.i.d, ξb,Mn
's are i.i.d conditional on data C(n) = (Y, X). The conditional distribution of √Mn βˇb j − βˇj given C(n)is asymptotically the same as the unconditional distribution of √Mn βˇj − β
∗
j
, which converges to zero Gaussian by (A.3). With the uniform boundedness of βˇb j and βˇj as shown in Lemma A.1, we can show that Eξb,Mn | C(n)→ 0 and Var ξb,Mn | C(n)→ σˇ
2 j uniformly over C(n) as Mn → ∞. Furthermore, EII | C(n)= Eξb,Mn | C(n), and Var II | C(n)= Var ξb,Mn | C(n)/B. By Chebyshev Inequality, for any *δ, ζ >* 0, there exist N0, B0 > 0 such that when n > N0*, B > B*0, P(|II| ≥ δ) ≤ ζ. Thus, II = op(1).

To prove (c), i.e. III = op(1), we first note that each subsample Cb1 can be regarded as a random sample of n1 = kn(0 *< k <* 1) i.i.d. observations from the population distribution for which Theorem 2 holds, that is to say
Sˆb ≤ K1n c1 and PS ⊆ Sˆb≥ 1 − K2(q ∨ n)
−1−c2. We show that for any b, conditional on Sˆb ⊇ S, √Mn βeb j − βˇb j
= op(1).

To see this, we first arrange the order of the components of x = (x1*, . . . , x*q) such that the first s0 components are signal variables. In other words, S = {1*, . . . , s*0}. From the proof of Theorem 4 and omitting superscript b, we have that

$$\begin{split}\widetilde{\beta}_{j}-\beta_{j}^{*}&=-M_{n}^{1-1}\widetilde{\epsilon}_{j}^{T}\left\{I_{S_{+j}}^{*}\right\}^{-1}U_{S_{+j}}\left(\beta_{S_{+j}}^{*}\right)+\widetilde{r}_{M_{n}^{1}},\\ \widetilde{\beta}_{j}-\beta_{j}^{*}&=-M_{n}^{1-1}\widetilde{\epsilon}_{j}^{T}\left\{I_{S_{+j}^{*}}^{*}\right\}^{-1}U_{S_{+j}}\left(\beta_{S_{+j}^{*}}^{*}\right)+\widetilde{r}_{M_{n}^{1}},\end{split}$$ (A.4)
23 where eej = (0, . . . , 0, 1, 0*, . . . ,* 0)T is a unit vector of length
Sˆ+j
 to index the position of variable j in Sˆ+j ,
eˇj is a unit vector of length |S+j | to index the position of variable j in S+j , and the residualsreM1n 2 2
=
op 1/M1 n
,rˇM1n 2 2
= op (1/n1). Here, I
∗
Sˆ+j and I
∗
S+j are two submatrices of the expected information at β
∗,
which is derived in the proof of Proposition 1 as I
∗ = E
n1 2Mn Pi∈n PTi t=1 exp −x
⊤
i β γ
⊤yity
⊤
itγxix
⊤ i o=
E
 1nXTVX	, where V = diag {ν1*, . . . , ν*n} is an n×n diagonal matrix with νi =1 2Ti PTi t=1 exp −x
⊤
i β γ
⊤yit y
⊤
itγ.

For any j ∈ *S, k* ∈ S
c, the complement of S, the partial orthogonality condition (Fan and Lv, 2008) that
{xj , j ∈ S} are independent of {xk, k ∈ S
c} implies that I
∗is block-diagonal with two blocks indexed by S
and S
c. That is,

$$I^{*}=\left(\begin{array}{c c}{{{\bf E}\left(\frac{1}{n}{\bf X}_{S}^{\mathrm{T}}{\bf V}{\bf X}_{S}\right)}}&{{0}}\\ {{0}}&{{{\bf E}\left(\frac{1}{n}{\bf X}_{S^{c}}^{\mathrm{T}}{\bf V}{\bf X}_{S^{c}}\right)}}\end{array}\right).$$
$\bullet$  . 
where the submatrices XS and XSc are submatrices of X. Hence, I
∗
Sˆ+j is blockdiagonal with two blocks indexed by S and Sˆ+j\S, and I
∗
S+j is block-diagonal with two blocks indexed by S and S+j\S = ∅ if j ∈ S

or = {j} otherwise. Therefore, {I ∗} −1, nI ∗ Sˆ+j o−1and nI ∗ S+j o−1are all block-diagonal. Write U (β ∗) = (u0, u1, . . . , up) T, ee T j nI ∗ Sˆ+j o−1= eijkk∈Sˆ+j and ˇe T j nI ∗ S+j o−1=ˇijkk∈S+j . Then, it follows that eijk = ˇijk for k ∈ S, which leads to pM1 n βej − βˇj = −1 pM1 n X k∈Sˆ+j eijkuk + 1 pM1 n X k∈S+j ˇijkuk + r ′ n1 = −1 pM1 n X k∈Sˆ\S eijkuk + 1 (j /∈ S) pM1 n ˇijj −eijjuj + r ′ n1 where r ′ n1 = c1 = o√n1 with
√n1 (ren1 − rˇn1
) = op(1), and ren1 and ˇrn1 are as in (A.4). As
Sˆ\S
 ≤ K1n
0 ≤ c1 < 1/2, Var Pk∈Sˆ\Seijkuk
= o (n1). By the Chebyshev inequality, the first term on the right-hand side converges to 0 in probability. Thus, each of these three terms is op(1) and we have pM1 n βej − βˇj
=
op(1). As n1/n = k where 0 *< k <* 1, the original statement holds.

Now define ηb = 1 nS ⊈ Sˆbo √Mn βeb j − βˇb j
, while omitting subscripts j in η for simplicity, then III
=
PB
b=1 ηb
/B. When S ⊈ Sˆb, by Lemma A.1, there exists a Cβ ≥ cβ such that supb
βeb j − βˇb j
 ≤
supb
βeb j − β
∗
j
 + supb
βˇb j − β
∗
j
 ≤ 2Cβ + 1. Therefore,

$$\mathbb{E}\left(\eta_{k}\right)\leq\mathrm{P}\left(S\not\subseteq\hat{S}^{b}\right)\sqrt{M_{n}}\sup_{1\leq k\leq B}\left|\widehat{\beta}_{j}^{b}-\widehat{\beta}_{j}^{b}\right|\leq2C_{\beta}\sqrt{M_{n}}K_{2}(q\lor n)^{-1-c_{2}},$$ (A.5) $$\mathrm{Var}\left(\eta_{k}\right)\leq\mathrm{P}\left(S\not\subseteq\hat{S}^{b}\right)M_{n}\sup_{1\leq k\leq B}\left(\widehat{\beta}_{j}^{b}-\widehat{\beta}_{j}^{b}\right)^{2}\leq4C_{\beta}^{2}M_{n}K_{2}(q\lor n)^{-1-c_{2}}.$$

With dependent ηb 's, we further have

, we further have $$\begin{aligned} \mathbf{E}(\mathrm{III}) = \mathbf{E}\left\{\left(\sum_{b=1}^{B}\eta_{b}\right)/B\right\} \leq 2C_{\beta}\sqrt{M_{n}}K_{2}(q \vee n)^{-1-c_{2}}, \\ \mathrm{Var}(\mathrm{III}) \leq \frac{1}{B^{2}}\sum_{b=1}^{B}\sum_{b^{\prime}=1}^{B} |\mathrm{Cov}\left(\eta_{b},\eta_{b^{\prime}}\right)| \leq 4C_{\beta}^{2}M_{n}K_{2}(q \vee n)^{-1-c_{2}},  \end{aligned}$$. 
where the last inequality holds because of |Cov ( η , η ν )| ≤ {Var ( η ь ) Var ( η ν )} 1/2 and (     ). Then we can show III = op (1).

□

![25_image_0.png](25_image_0.png)

## Additional Application Results B

![26_image_0.png](26_image_0.png)

![26_image_1.png](26_image_1.png)

![27_image_0.png](27_image_0.png)

## References

Bassett, D. S. and Bullmore, E. T. (2017). Small-world brain networks revisited. *The Neuroscientist*,
23(5):499–516.

Belloni, A., Chernozhukov, V., and Hansen, C. (2014). Inference on treatment effects after selection among high-dimensional controls. *The Review of Economic Studies*, 81(2):608–650.

B¨uhlmann, P. and Van De Geer, S. (2011). *Statistics for high-dimensional data: methods, theory and* applications. Springer Science & Business Media.
B¨uhlmann, P. and Yu, B. (2002). Analyzing bagging. *The annals of Statistics*, 30(4):927–961.

Bullmore, E. and Sporns, O. (2012). The economy of brain network organization. Nature Reviews Neuroscience, 13(5):336.

Desikan, R. S., S´egonne, F., Fischl, B., Quinn, B. T., Dickerson, B. C., Blacker, D., Buckner, R. L., Dale, A. M., Maguire, R. P., and Hyman, B. T. (2006). An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest. *NeuroImage*, 31(3):968–980.

Efron, B. (2014). Estimation and accuracy after model selection. *Journal of the American Statistical* Association, 109(507):991–1007.

Fan, J. and Li, R. (2001). Variable selection via nonconcave penalized likelihood and its oracle properties.

Journal of the American statistical Association, 96(456):1348–1360.
Fan, J. and Lv, J. (2008). Sure independence screening for ultrahigh dimensional feature space. *Journal of* the Royal Statistical Society: Series B (Statistical Methodology), 70(5):849–911.

Fei, Z. and Li, Y. (2021). Estimation and inference for high dimensional generalized linear models: A splitting and smoothing approach. *The Journal of Machine Learning Research*, 22(1):2681–2712.

Glasser, M. F., Sotiropoulos, S. N., Wilson, J. A., Coalson, T. S., Fischl, B., Andersson, J. L., Xu, J.,
Jbabdi, S., Webster, M., and Polimeni, J. R. (2013). The minimal preprocessing pipelines for the Human Connectome Project. *NeuroImage*, 80:105–124.

Gollo, L. L., Roberts, J. A., Cropley, V. L., Di Biase, M. A., Pantelis, C., Zalesky, A., and Breakspear, M. (2018). Fragility and volatility of structural hubs in the human connectome. *Nature Neuroscience*,
21(8):1107–1116.

Grosenick, L., Klingenberg, B., Katovich, K., Knutson, B., and Taylor, J. E. (2013). Interpretable wholebrain prediction analysis with GraphNet. *NeuroImage*, 72:304–321.

Hall, Z., Chien, B., Zhao, Y., Risacher, S. L., Saykin, A. J., Wu, Y.-C., and Wen, Q. (2022). Tau deposition and structural connectivity demonstrate differential association patterns with neurocognitive tests. *Brain* Imaging and Behavior, 16(2):702–714.
Hebb, D. O. (2005). *The organization of behavior: A neuropsychological theory*. Psychology Press. Javanmard, A. and Montanari, A. (2014). Confidence intervals and hypothesis testing for high-dimensional regression. *The Journal of Machine Learning Research*, 15(1):2869–2909.

Jbabdi, S. and Johansen-Berg, H. (2011). Tractography: where do we go from here? *Brain Connectivity*,
1(3):169–183.
Kim, R. and Zhang, J. (2024). High-dimensional covariance regression with application to co-expression qtl

detection. *arXiv preprint arXiv:2404.02093*.

Laird, A. R., Eickhoff, S. B., Li, K., Robin, D. A., Glahn, D. C., and Fox, P. T. (2009). Investigating the functional heterogeneity of the default mode network using coordinate-based meta-analytic modeling.

Journal of Neuroscience, 29(46):14496–14505.

Lee, J. D., Sun, D. L., Sun, Y., and Taylor, J. E. (2016). Exact post-selection inference, with application to the lasso. *The Annals of Statistics*, 44(3):907–927.

Lee, J. D., Sun, Y., and Taylor, J. E. (2015). On model selection consistency of regularized M-estimators.

Electronic Journal of Statistics, 9(1):608–642.

Leech, R., Kamourieh, S., Beckmann, C. F., and Sharp, D. J. (2011). Fractionating the default mode network: distinct contributions of the ventral and dorsal posterior cingulate cortex to cognitive control. Journal of Neuroscience, 31(9):3217–3224.

Mueller, S., Wang, D., Fox, M. D., Yeo, B. T., Sepulcre, J., Sabuncu, M. R., Shafee, R., Lu, J., and Liu, H. (2013). Individual variability in functional connectivity architecture of the human brain. *Neuron*,
77(3):586–595.

Negahban, S. N., Ravikumar, P., Wainwright, M. J., and Yu, B. (2012). A unified framework for highdimensional analysis of m-estimators with decomposable regularizers. *Statistical Science*, 27(4):538–557.

Ning, Y. and Liu, H. (2017). eneral theory of hypothesis tests and confidence regions for sparse high dimensional models. *The Annals of Statistics*, 45(1):158–195.

Seiler, C. and Holmes, S. (2017). Multivariate heteroscedasticity models for functional brain connectivity.

Frontiers in Neuroscience, 11:696.

Smith, S. M., Jenkinson, M., Woolrich, M. W., Beckmann, C. F., Behrens, T. E., Johansen-Berg, H.,
Bannister, P. R., De Luca, M., Drobnjak, I., Flitney, D. E., et al. (2004). Advances in functional and structural MR image analysis and implementation as FSL. *NeuroImage*, 23:S208–S219.
Song, H., Dai, R., Raskutti, G., and Barber, R. F. (2020). Convex and non-convex approaches for statistical inference with class-conditional noisy labels. *The Journal of Machine Learning Research*, 21(1):6805–6862.

Sporns, O. (2007). Brain connectivity. *Scholarpedia*, 2(10):4695. Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. *Journal of the Royal Statistical* Society: Series B (Methodological), 58(1):267–288.

Tibshirani, R., Saunders, M., Rosset, S., Zhu, J., and Knight, K. (2005). Sparsity and smoothness via the fused lasso. *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 67(1):91–108.

Tibshirani, R. J. and Taylor, J. (2011). The solution path of the generalized lasso. *The Annals of Statistics*,
39(3):1335–1371.
Van de Geer, S., B¨uhlmann, P., Ritov, Y., and Dezeure, R. (2014). On asymptotically optimal confidence regions and tests for high-dimensional models. *The Annals of Statistics*, 42(3):1166–1202.

Vershynin, R. (2010). Introduction to the non-asymptotic analysis of random matrices. *arXiv preprint*
arXiv:1011.3027.

Wager, S. and Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. *Journal of the American Statistical Association*, 113(523):1228–1242.
Wasserman, L. and Roeder, K. (2009). High dimensional variable selection. *Annals of statistics*, 37(5A):2178. Xia, L., Nan, B., and Li, Y. (2020). A revisit to de-biased lasso for generalized linear models. arXiv preprint arXiv:2006.12778.

Zhang, C.-H. (2010). Nearly unbiased variable selection under minimax concave penalty. *The Annals of* Statistics, pages 894–942.

Zhang, C.-H. and Zhang, S. S. (2014). Confidence intervals for low dimensional parameters in high dimensional linear models. *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*,
76(1):217–242.
Zhao, Y., Wang, B., Mostofsky, S., Caffo, B., and Luo, X. (2019). Covariate assisted principal regression for covariance matrix outcomes. *Biostatistics*.

Zhao, Y., Wang, B., Mostofsky, S. H., Caffo, B. S., and Luo, X. (2021). Covariate assisted principal regression for covariance matrix outcomes. *Biostatistics*, 22(3):629–645.

Zou, H. (2006). The adaptive lasso and its oracle properties. *Journal of the American Statistical Association*,
101(476):1418–1429.

Zou, H. and Hastie, T. (2005). Regularization and variable selection via the elastic net. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 67(2):301–320.

Zou, T., Lan, W., Wang, H., and Tsai, C.-L. (2017). Covariance regression analysis. *Journal of the American* Statistical Association, 112(517):266–281.