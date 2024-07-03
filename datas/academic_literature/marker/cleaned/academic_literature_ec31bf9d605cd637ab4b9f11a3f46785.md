# Stabilizing Estimates Of Shapley Values With Control Variates

Jeremy Goldwasser 1 and Giles Hooker 2 1 UC Berkeley, Department of Statistics 367 Evans Hall, Berkeley, CA 94720 jeremy goldwasser@berkeley.edu 2 University of Pennsylvania, Department of Statistics & Data Science 265 South 37th Street, Philadelphia PA 19104 ghooker@wharton.upenn.edu Abstract. Shapley values are among the most popular tools for explaining predictions of black-box machine learning models. However, their high computational cost motivates the use of sampling approximations, inducing a considerable degree of uncertainty. To stabilize these model explanations, we propose ControlSHAP, an approach based on the Monte Carlo technique of control variates. Our methodology is applicable to any machine learning model and requires virtually no extra computation or modeling effort. On several high-dimensional datasets, we find it can produce dramatic reductions in the Monte Carlo variability of Shapley estimates.

## 1 Introduction

Machine learning models have become widely deployed in high-stakes domains such as healthcare, finance, and criminal justice [14,12,25,4]. Use of algorithmic decision-making in these areas has profound human consequences, but the predictive models themselves may be opaque. This motivates the development of methods to understand the reasoning behind the predictions of a black-box model [2].

To that end, feature importance methods attribute a value to each feature passed into the model, indicating its predictive importance [39,24,11,30,5]. In this paper, we focus on Shapley values, a seminal concept in game theory which have emerged as one of the most popular tools for model interpretability [32,24].

In layman's terms, Shapley values quantify how much information is gained from being told the value of each feature, averaged over orderings in which the features are revealed.

Shapley values are rarely computed exactly, as the computational cost is exponential in the number of input features. Rather, they are typically estimated using the Shapley Sampling or KernelSHAP algorithm [24,34,35]. These algorithms, however, are subject to sampling variability; as a result, running the same procedure twice may yield different estimated Shapley values, including arXiv:2310.07672v3 [stat.ML] 10 Apr 2024 different estimated orderings of features. This instability raises questions about the trustworthiness of insights gleaned from Shapley values.

We seek to mitigate this issue by employing Monte Carlo variance reduction techniques. In particular, we use control variates, a method that adjusts one random estimator based on the known error of another. Here, the related estimator approximates the Shapley values of a first or second order Taylor expansion to the original model, depending on whether the value function assumes features are correlated or independent. In the independent case, these estimates entail essentially no additional computation; otherwise we must put some effort into pre-computing terms which can then be used for any query point for which we need to calculate Shapley values. While variations on our methods are possible, from tuning parameters to more complex Monte Carlo schemes [29], our goal is to provide a default scheme that requires minimal computational or intellectual effort.

Estimates of Shapley values are significantly more stable with control variates. In some cases, variance reductions reach as high as 90% for dozens of features, along with noticeably more consistent rankings of Shapley values among features.1

## 2 Shapley Values In Machine Learning 2.1 Shapley Values

In the context of machine learning, the Shapley values for an input sample x ∈ R
d present the change in prediction - i.e. the information gained - from learning the value of each feature. They do so by averaging the marginal contribution of a feature to every subset, or "coalition," of other features.

Formally, let f : X → R be a machine learning model trained on X ∈ R
n×d.

Further, let S ⊆ [d] := {1*, . . . , d*} denote a subset of the d features. Following SHAP [24], the value function for input x maps a subset S to an estimate of the mean prediction, conditioned on the known features xS:

$$v_{x}(S):={\hat{\mathbb{E}}}[f(x_{S},X_{[d]\setminus S})]={\hat{\mathbb{E}}}[f(X)|X_{S}=x_{S}].$$
vx(S) := Eˆ[f(xS, X[d]\S)] = Eˆ[f(X)|XS = xS]. (1)
In some settings - e.g. if the features are multivariate Gaussian or mutually independent - the conditional mean can be computed exactly. Otherwise, when the conditional distribution is intractable, the true mean is impossible to compute. Hence, in this case the value function vx(S) estimates E[f(xS, X[d]\S)]
using an approximation of the conditional distribution X|XS.

The jth Shapley value for input x, which we denote ϕj (x), averages the change in value function across all subsets of [d], with and without the j th feature.

$$\phi_{j}(x)=\frac{1}{d}\sum_{S\subseteq[d]\setminus\{j\}}{\binom{d-1}{|S|}}^{-1}{\big(}v_{x}(S\cup\{j\})-v_{x}(S){\big)}.$$
$$\left(2\right)$$

1https://github.com/jeremy-goldwasser/ControlSHAP contains our code and experimental results.

Each Shapley value is a function of O(2d) subsets. Since this is computationally prohibitive in high dimensions, we consider sampling approximations.

## 2.2 Shapley Estimation

Shapley sampling [34] is the most straightforward algorithm to approximate Shapley Values. For each iteration m ∈ {1*, . . . , M*}, randomly permute the d features, and select the subset S
m ⊆ [d]\{j} that appears before j. Shapley sampling averages the change in value function from adding feature j to each subset.

$$\hat{\phi}_{j}(x)=\frac{1}{M}\sum_{m=1}^{M}v_{x}(S^{m}\cup\{j\})-v_{x}(S^{m}).$$
$$\left({\mathrm{3}}\right)$$
$$\quad(4)$$

In contrast, the KernelSHAP method [24] estimates all d features at once.

Again, in each iteration m we select a coalition S
m and compute its value function vx(S
m). Rather than sampling coalitions via permutations, however, S
m is sampled from the distribution

$$p(S)\propto{\frac{d-1}{\binom{d}{|S|}(|S|)(d-|S|)}}.$$

Each coalition S can be equivalently expressed as a binary vector z ∈ {0, 1}
d by defining zi = 1{i ∈ S} for all i ∈ [d]. Accordingly, z vectors 0 and 1 correspond to S = ∅ and [d], respectively.

Abusing notation, let vx(z) := vx(S), where z is the binary representation of S. Consequently, we can express vx(0) = E[f(X)] and vx(1) = f(x). The KernelSHAP estimator is defined as

ϕˆ(x) = argmin ϕ∈Rd 1 M X M m=1 ϕ Tz m − (vx(z m) − vx(0))2 s.t. 1 T ϕ = vx(1) − vx(0) (5) = (Z TZ) −1 I − 11T(Z TZ) −1 1 T (ZTZ)−11 Z T(V − vx(0)) + vx(1) − vx(0) 1 T (ZTZ)−11 (Z TZ) −11,
where Z ∈ RM×d and V ∈ RM contain the coalitions z m and values vx(z m).

Drawing from [7], [24] proved that the weighting kernel in 4 produces linear regression coefficients that are equal to the Shapley values.

## 2.3 Related Work

A number of works seek to reduce the sample variability of Shapley values.

Mitchell et al. propose several Monte Carlo techniques for choosing subsets [26]; independently, Covert and Lee advocate antithetic sampling for KernelSHAP
[10]. Song et al. accelerate computation by storing pre-computed subsets [33].

Our method can be applied on top of these methods, leveraging their contributions for added benefit.

Alternatives to sampling-based methods have also been proposed. Chen et al.

derive expressions for Shapley values in settings for which the features contribute to predictions with a well-understood graphical structure [9]. FastSHAP directly predicts Shapley values using a neural network [19]; it generalizes well when the neural network is trained on a large, diverse dataset. Other works more efficiently compute Shapley values given specific predictive models, e.g. Tree SHAP and Deep SHAP [23,24]. These methods can quickly estimate Shapley values or obtain them exactly. However, they are limited to settings that satisfy their preconditions on model types, data structures, and number of inputs to explain.

## 3 Control Variates For Shapley Values 3.1 Control Variates

The method of control variates is a variance reduction technique for Monte Carlo sampling problems. To reduce the error of an estimator, it leverages information about the known error of another.

Suppose Aˆ and Bˆ are unbiased estimators of A∗ and B∗, where only B∗is known. Define the control variates estimator as

$$\bar{A}:=\hat{A}-c(\hat{B}-B^{*}).$$
∗). (6)
For any constant c, A˜ is an unbiased estimator of A∗. Consequently, its mean squared error (MSE) is equivalent to its variance. The optimal c is selected with the following lemma, using plug-in estimates of the variance and covariance.

Lemma 1. Suppose A, ˆ Bˆ are unbiased estimators and ρA, ˆ Bˆ > 0*, where* ρ is Pearson's correlation coefficient. Then the control variates estimator (6) has minimal variance Var(A˜) = (1 − ρ 2 A, ˆ Bˆ
)Var(Aˆ) *when* c
∗ =
Cov(A, ˆ Bˆ)
Var(Bˆ)
.

## 3.2 Controlshap

Our method, ControlSHAP, applies the method of control variates to the Shapley values for input x. The estimands A∗ and B∗in 3.1 are represented by ϕ model j(x)
and ϕ approx j(x); these are the jth Shapley values of f and its Taylor approximation. In the following subsections, we will elaborate on the approximate model and its true Shapley values ϕ approx(x).

Either Shapley sampling or KernelSHAP can be used to compute ϕˆmodel j(x)
and ϕˆapprox j(x). These are both appropriate for control variates because they are essentially unbiased for the true Shapley value (Eq. 2), whose value function is the approximate conditional mean (Eq. 1). Trivially, Shapley sampling (Eq.

3) is unbiased, and [10] showed that KernelSHAP has negligible bias (Eq. 5).

Prior works have established that these methods may be biased for the Shapley value whose value function is the true conditional mean, vx(S) = E[f(X)|Xs];
however, by definition this Shapley value is not the estimand for this problem, as these means are intractable [36,8,1]. By virtue of (6), control variate corrections to these estimands do not change their bias.

Whichever method we choose, we must use the same subsets S in computing ϕˆmodel j(x) and ϕˆapprox j(x) to ensure they are correlated. Following Eq. 6 and Lemma 1, the ControlSHAP estimator is

$$\hat{\phi}_{j}^{\rm CV}(x)=\hat{\phi}_{j}^{\rm model}(x)-\hat{\alpha}\big{(}\hat{\phi}_{j}^{\rm approx}(x)-\phi_{j}^{\rm approx}(x)\big{)}\tag{7}$$  where $\hat{\alpha}=\dfrac{\widehat{\rm Cov}(\hat{\phi}_{j}^{\rm model}(x),\hat{\phi}_{j}^{\rm approx}(x))}{\widehat{\rm Var}(\hat{\phi}_{j}^{\rm approx}(x))}$.  
If α is obtained using the oracle covariance and variance, then this estimator reduces variance and MSE by a factor of ρ 2(ϕˆj (x)
model, ϕˆj (x)
approx).

## 3.3 Independent Features

To compute Shapley values at x, we must estimate the conditional mean for each sampled subset, E[f(X)|XS = xS]. To do so, we generate a number of samples from X|XS, compute f(X) on each, and take a sample mean. The conditional distribution X|XS may be difficult or impossible to characterize. Because of this, the standard approach popularized by SHAP samples the features in S
C from their marginal distributions [34,24]. Doing so makes the implicit assumption that the features are independent for the sake of computing E[f(X)|XS = xS].

Consider the second-order Taylor approximation of f around x. If the value function is computed sampling features from their marginal distributions, then the Shapley values ϕ approx(x) of this approximate model can be computed exactly. While we refer to this as the "independent features case," the following theorem holds *regardless* of whether the features are actually independent.

Theorem 1. Define µ := E[X] and Σjk := Cov(Xj , Xk)*. Let the value function* vx(S) *compute conditional means by sampling each feature from its marginal* distribution. The jth *Shapley value of the second-order Taylor approximation of* f *around* x is

$$\phi_{j}^{a p p r o x}(x)=\frac{\partial f}{\partial x_{j}}(x_{j}-\mu_{j})$$ $$\qquad-\frac{1}{2}\Biggl[\sum_{k=1}^{d}(x_{k}-\mu_{k})\frac{\partial^{2}f}{\partial x_{j}x_{k}}\Biggr](x_{j}-\mu_{j})$$ $$\qquad-\frac{1}{2}\sum_{k=1}^{d}\Sigma_{j k}\frac{\partial^{2}f}{\partial x_{j}x_{k}}.$$

Proof of Theorem 1 is in the section 1.1 of the appendix.

## 3.4 Correlated Features

Input features are often correlated with one another. When this is the case, it may be imprudent to falsely assume independence for the sake of computational convenience. This may produce Shapley values that misrepresent the relationship between inputs and predictions, and rely on the values that a machine learning function makes in areas where it has very little data [18].

Unfortunately, respecting feature correlations requires that we sample from X|XS for all sampled subsets S. Nonparametric density estimation in high dimensions is challenging due to the curse of dimensionality, and most approaches typically require considerable modeling effort.

To circumvent this, a common alternative estimates the conditional mean by characterizing X|XS as a multivariate normal distribution[8,1]. This makes the value function easy to compute, without having to ignore dependencies between the features. One can even faithfully represent binary data under this categorization by simulating Gaussian random variables and thresholding accordingly
[22].

Moreover, using this value function enables us to compute the true Shapley value of a first-order Taylor expansion of f. As in Theorem 1, the formula in Theorem 2 holds whether or not the features are indeed normally distributed. Theorem 2. *Define the value function to take the conditional expectation of* f(X)|XS *over a multivariate normal distribution. Let* S
m ⊆ [d]\{j} *be the subset* of features appearing before j in the mth permutation of [d], and let QS and RS
be matrices defined in Section 1.2 of the supplementary material that do not depend on x*. Define*

$$D_{j}:=\frac{1}{d!}\sum_{m=1}^{d!}([Q S_{j}^{m}\cup_{j}+R S_{j}^{m}\cup_{j}]-[Q S_{j}^{m}+R S_{j}^{m}]).$$

The jth Shapley value of the first-order Taylor approximation of f *around* x is

$$\phi_{j}^{a p p r o x}(x)=\nabla f(x)^{T}D_{j}(x-\mu).$$

Evaluating ϕ approx j(x) still requires computing an exponential number of terms for Dj . However, because Dj does not depend on x, we can reuse it for other inputs x. That is, we can front-load computational work into accurately estimating Dj ; then, we can instantly obtain close approximations to ϕ approx j(x)
for as many inputs x as we want. This is valuable if we want to estimate Shapley values at many inputs, either for future data or to provide a global notion of feature importance.

The normality condition in Therorem 2 can be relaxed somewhat. It is needed insofar as it produces conditional means of the form E[X1|X2 = x2] = µ1 + Σ12Σ
−1 22 (x2 − µ2),
which occur whenever the variance of the conditional distribution is independent of the values of the conditioning set. This property holds for all ellipticallysymmetric distributions, including the multivariate t-, Laplace, and logistic distributions [13].

## 3.5 Non-Differentiable Models

The discussion so far assumes that we have access to first and sometimes second derivatives of f. This excludes models based on trees that result in piecewise constant functions, as well as neural networks with ReLU activation functions, which have first but not second derivatives. While there are specific Shapley methods for trees [6], these only apply to models with axis-oriented splits (counter to e.g.

[38]).

For our purposes, we use a Taylor series only to provide linear and quadratic approximations to f. Thus, we can replace *∂f /∂x*i and ∂
2*f /∂x*i∂xj with finitedifference approximations based on large step sizes, so as to approximate model behavior across substantial changes in the features.

In our experiments below, we used finite differencing on random forest predictors. We chose the step size of each numeric feature to be its marginal standard deviation; for categorical features, we swapped the observed values. Alternative choices would include basing step sizes on conditional distributions, or tuning them for agreement with f. Our goal has been to examine a straightforward control variate method with minimal costs both computationally and in human effort, so we have not pursued these variations here. We speculate that additional tuning would provide further improvements, which may be worthwhile in particular applications.

## 4 Variance Estimation

To use the method of control variates, we need to estimate the variance and covariance of our two estimators, as in Eq. 7. This section outlines strategies for doing so.

## 4.1 Shapley Sampling

Let GS := vx(S ∪ j) − vx(S) for subset S. Shapley sampling selects M subsets S via independent permutations, then takes a sample mean of their GS values.

Therefore the variance of Shapley sampling values is

$$\mathrm{Var}(\hat{\phi}_{j})=\frac{1}{M}\mathrm{Var}(G_{S}).$$

We estimate Var(GS) empirically across the M observations of GS. Estimating the covariance between the Shapley estimates is similarly straightfoward:

$$\mathrm{Cov}(\hat{\phi}_{j}^{\mathrm{model}},\hat{\phi}_{j}^{\mathrm{approx}})=\frac{1}{M}\mathrm{Cov}(G_{S}^{\mathrm{model}},G_{S}^{\mathrm{approx}}),$$ which again we estimate empirically. 

## 4.2 Kernelshap

We present three approaches to estimate the KernelSHAP variance and covariance. These are unrelated to the choice of independent or correlated features.

1. Bootstrapping. For many iterations, take M samples with replacement from the observed subsets S. Compute the KernelSHAP estimates ϕˆmodel boot and ϕˆapprox boot on the pairs {(Sboot, vmodel boot (S))}M
i=1 and {(Sboot, v approx boot (S))}M
i=1.

Repeat this process to produce many bootstrapped estimates of ϕˆmodel boot and ϕˆapprox boot , with which we compute empirical variance and covariance.

2. Least Squares. KernelSHAP learns ϕˆ by fitting a constrained least squares
(Eq. 5). Writing A(Z) = (Z
TZ)
−1-I − (11T(Z
TZ)
−1)/(1 T(Z
TZ)
−11)Z
T
we make the approximation Var( d ϕˆ) = A(Z)Var(vx(S))A(Z)
T.
The diagonals of *V ar*(vx(S)) are computed via sample variance, provided more than one sample is used to estimate each vx(S). Analogously,

$$,\,\psi\,:\,1$$
$\downarrow$ . 
Cov( d ϕˆmodel, ϕˆapprox) = A(Z)ΣAe (Z)
T
where Σe = Cov(vx(S)
model, vx(S)
approx).

Here we note that this formula ostensibly accounts only for the sampling variability in vx(S) rather than the Monte Carlo choice of coalitions Z.

However, by the total covariance formula writing ϕˆ = B(*Z, V* ) we have that

$$\mathrm{Cov}(\hat{\phi}^{\mathrm{model}},\hat{\phi}^{\mathrm{approx}})$$ $$=\mathbb{E}_{Z}\mathrm{Cov}(B(Z,V^{\mathrm{model}}),B(Z,V^{\mathrm{approx}})|Z)$$ $$+\,\mathrm{Cov}_{Z}(\mathbb{E}_{V}B(Z,V^{\mathrm{model}}),\mathbb{E}_{V}B(Z,V^{\mathrm{approx}})).$$

[10] demonstrated that kernelSHAP has small bias, making the second term small, and this calculation provides a consistent estimate of the first term.

Var(ϕˆmodel) is estimated with an equivalent calculation.

3. Grouped. [10] introduced a method based on their finding that the variance evolves at a O(
1 M ) rate. First, split the {(*S, v*x(S))}M
i=1 pairs into disjoint groups, and fit ϕˆ(k)in each. Then, take the empirical variance and covariance of these ϕˆ(k) values, and scale linearly.
Empirically, we observed that the bootstrapped and least squares methods yield roughly the same variances and covariances. Section 4 of the appendix shows that ControlSHAP with these two methods has nearly identical performance, across multiple datasets and machine learning models. Our experimental results all use the least squares method, since bootstrapping has a moderately higher computational cost.

In our experiments, we were not able to get the grouped method to reliably work. We observed that it occasionally produced highly erroneous estimates of variance and covariance. While this may be remedied by fitting a larger number of groups, the group size must be large enough to avoid singularity issues in fitting ϕˆ(k). More details are in Section 4 of the appendix.

## 5 Experiments

We demonstrated the efficacy of our ControlSHAP methodology on five datasets.

A simulated dataset contained ten normally distributed features with block covariance structure; each feature had a correlation of 0.5 with one feature and 0.25 with another, and the response given by a logistic regression. We also used four public datasets from the UCI ML repository: Portuguese bank [27], German credit [17], census income [20], and breast cancer subtyping [3].

These real-world datasets are higher-dimensional, containing roughly 20 features on average. Many features are categorical with more than two levels, e.g.

Month. We represent each of these features as a set of one-hot encodings. These transformations are necessary to use models like logistic regression and neural networks; they are also required for ControlSHAP, which takes gradients with respect to the features. The Shapley value of a categorical feature is the sum across the individual levels [24].

In the following analyses, we refer to the two approaches for the value function as assuming features are independent versus correlated (dependent). This terminology only serves to distinguish the method of sampling and Taylor expansion. It does not entail making actual assumptions about the data, as detailed in Section 3. The ControlSHAP estimator's properties such as unbiasedness do not require feature independence or Gaussianity to hold.

For each data set, and each model, we sampled 40 data points from the test set at random and estimated Shapley values 50 times for each, with and without control variates and using both correlated and independent sampling. For each estimate, we sampled 1000 coalitions. For KernelSHAP, we generated 10 points per coalition to estimate pointwise variances. We ran 200 bootstrap samples and 20 groups to estimate variances and covariances for control variates for bootstrap and grouped estimators. For Shapley sampling, which re-runs the Monte Carlo calculation for each feature, we used 1 sample per coalition. Computations were run on an internal cluster.



As Figure 1 demonstrates, ControlSHAP significantly improves the variability of Shapley estimates, regardless of the number of samples drawn. For this feature - chosen because it has the highest Shapley value - adjusting the Shapley estimate consistently reduces its variance by at least 90%.

Next, we consider the improvements in variance - equivalently, in MSE -
across all 5 datasets, using a variety of machine learning predictors. We calculated the variance reduction of our ControlSHAP methods by taking the sample variance of each feature's Shapley value across 50 iterations.

$$\mathrm{VarReduce}_{j}(x)={\frac{\left[{\widehat{\mathrm{Var}}}({\hat{\phi}}_{j}^{\mathrm{model}}(x))-{\widehat{\mathrm{Var}}}({\hat{\phi}}_{j}^{\mathrm{CV}}(x))\right]}{{\widehat{\mathrm{Var}}}({\hat{\phi}}_{j}^{\mathrm{model}}(x))}}$$





(8) $$\binom{8}{2}$$. 
Figure 2 displays results for all features of the German Credit dataset, using logistic regression as a predictor. Our four ControlSHAP methods produce large variance reductions on all features, whose Shapley values span several orders of magnitude. On average, our final Shapley estimates have roughly 80-95% lower variability than the original estimates.

A second stability metric we used was the number of ranking changes. This metric is motivated by the fact that often practitioners care more about identifying features with high Shapley values than the values themselves [15,28,16].

Formally, let ˆrj (x) be the ranking of feature j within a set of d Shapley estimates. For each method, we compute the average number of pairwise ranking changes across 50 resamplings.