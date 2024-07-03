# Stabilizing Estimates of Shapley Values with Control Variates 

Jeremy Goldwasser ${ }^{1}$ and Giles Hooker ${ }^{2}$<br>${ }^{1}$ UC Berkeley, Department of Statistics<br>367 Evans Hall, Berkeley, CA 94720<br>jeremy_goldwasser@berkeley . edu<br>2 University of Pennsylvania, Department of Statistics \& Data Science<br>265 South 37th Street, Philadelphia PA 19104<br>ghooker@wharton. upenn. edu


#### Abstract

Shapley values are among the most popular tools for explaining predictions of black-box machine learning models. However, their high computational cost motivates the use of sampling approximations, inducing a considerable degree of uncertainty. To stabilize these model explanations, we propose ControlSHAP, an approach based on the Monte Carlo technique of control variates. Our methodology is applicable to any machine learning model and requires virtually no extra computation or modeling effort. On several high-dimensional datasets, we find it can produce dramatic reductions in the Monte Carlo variability of Shapley estimates.


## 1 Introduction

Machine learning models have become widely deployed in high-stakes domains such as healthcare, finance, and criminal justice [1412/2514. Use of algorithmic decision-making in these areas has profound human consequences, but the predictive models themselves may be opaque. This motivates the development of methods to understand the reasoning behind the predictions of a black-box model [2].

To that end, feature importance methods attribute a value to each feature passed into the model, indicating its predictive importance 39|24|11|30|5. In this paper, we focus on Shapley values, a seminal concept in game theory which have emerged as one of the most popular tools for model interpretability [32|24]. In layman's terms, Shapley values quantify how much information is gained from being told the value of each feature, averaged over orderings in which the features are revealed.

Shapley values are rarely computed exactly, as the computational cost is exponential in the number of input features. Rather, they are typically estimated using the Shapley Sampling or KernelSHAP algorithm 2413435. These algorithms, however, are subject to sampling variability; as a result, running the same procedure twice may yield different estimated Shapley values, including
different estimated orderings of features. This instability raises questions about the trustworthiness of insights gleaned from Shapley values.

We seek to mitigate this issue by employing Monte Carlo variance reduction techniques. In particular, we use control variates, a method that adjusts one random estimator based on the known error of another. Here, the related estimator approximates the Shapley values of a first or second order Taylor expansion to the original model, depending on whether the value function assumes features are correlated or independent. In the independent case, these estimates entail essentially no additional computation; otherwise we must put some effort into pre-computing terms which can then be used for any query point for which we need to calculate Shapley values. While variations on our methods are possible, from tuning parameters to more complex Monte Carlo schemes [29, our goal is to provide a default scheme that requires minimal computational or intellectual effort.

Estimates of Shapley values are significantly more stable with control variates. In some cases, variance reductions reach as high as $90 \%$ for dozens of features, along with noticeably more consistent rankings of Shapley values among features 1

## 2 Shapley Values in Machine Learning

### 2.1 Shapley Values

In the context of machine learning, the Shapley values for an input sample $x \in \mathbb{R}^{d}$ present the change in prediction - i.e. the information gained - from learning the value of each feature. They do so by averaging the marginal contribution of a feature to every subset, or "coalition," of other features.

Formally, let $f: \mathcal{X} \rightarrow \mathbb{R}$ be a machine learning model trained on $X \in \mathbb{R}^{n \times d}$. Further, let $S \subseteq[d]:=\{1, \ldots, d\}$ denote a subset of the $d$ features. Following SHAP [24, the value function for input $x$ maps a subset $S$ to an estimate of the mean prediction, conditioned on the known features $x_{S}$ :

$$
v_{x}(S):=\hat{\mathbb{E}}\left[f\left(x_{S}, X_{[d] \backslash S}\right)\right]=\hat{\mathbb{E}}\left[f(X) \mid X_{S}=x_{S}\right]
$$

In some settings - e.g. if the features are multivariate Gaussian or mutually independent - the conditional mean can be computed exactly. Otherwise, when the conditional distribution is intractable, the true mean is impossible to compute. Hence, in this case the value function $v_{x}(S)$ estimates $\mathbb{E}\left[f\left(x_{S}, X_{[d] \backslash S}\right)\right]$ using an approximation of the conditional distribution $X \mid X_{S}$.

The $\mathrm{j}^{\text {th }}$ Shapley value for input $x$, which we denote $\phi_{j}(x)$, averages the change in value function across all subsets of $[d]$, with and without the $j^{\text {th }}$ feature.

$$
\phi_{j}(x)=\frac{1}{d} \sum_{S \subseteq[d] \backslash\{j\}}\left(\begin{array}{c}
d-1 \\
|S|
\end{array}\right)^{-1}\left(v_{x}(S \cup\{j\})-v_{x}(S)\right)
$$[^0]

Each Shapley value is a function of $\mathcal{O}\left(2^{d}\right)$ subsets. Since this is computationally prohibitive in high dimensions, we consider sampling approximations.

### 2.2 Shapley Estimation

Shapley sampling [34] is the most straightforward algorithm to approximate Shapley Values. For each iteration $m \in\{1, \ldots, M\}$, randomly permute the $d$ features, and select the subset $S^{m} \subseteq[d] \backslash\{j\}$ that appears before $j$. Shapley sampling averages the change in value function from adding feature $j$ to each subset.

$$
\hat{\phi}_{j}(x)=\frac{1}{M} \sum_{m=1}^{M} v_{x}\left(S^{m} \cup\{j\}\right)-v_{x}\left(S^{m}\right)
$$

In contrast, the KernelSHAP method [24] estimates all $d$ features at once. Again, in each iteration $m$ we select a coalition $S^{m}$ and compute its value function $v_{x}\left(S^{m}\right)$. Rather than sampling coalitions via permutations, however, $S^{m}$ is sampled from the distribution

$$
p(S) \propto \frac{d-1}{\left(\begin{array}{c}
d \\
|S|
\end{array}\right)(|S|)(d-|S|)}
$$

Each coalition $S$ can be equivalently expressed as a binary vector $z \in\{0,1\}^{d}$ by defining $z_{i}=\mathbb{1}\{i \in S\}$ for all $i \in[d]$. Accordingly, $z$ vectors $\mathbf{0}$ and $\mathbf{1}$ correspond to $S=\emptyset$ and $[d]$, respectively.

Abusing notation, let $v_{x}(z):=v_{x}(S)$, where $z$ is the binary representation of $S$. Consequently, we can express $v_{x}(\mathbf{0})=\mathbb{E}[f(X)]$ and $v_{x}(\mathbf{1})=f(x)$. The KernelSHAP estimator is defined as

$$
\begin{array}{r}
\hat{\phi}(x)=\underset{\phi \in \mathbb{R}^{d}}{\operatorname{argmin}} \frac{1}{M} \sum_{m=1}^{M}\left(\phi^{T} z^{m}-\left(v_{x}\left(z^{m}\right)-v_{x}(\mathbf{0})\right)\right)^{2} \\
\text { s.t. } \quad \mathbf{1}^{T} \phi=v_{x}(\mathbf{1})-v_{x}(\mathbf{0}) \\
=\left(Z^{T} Z\right)^{-1}\left(I-\frac{\mathbf{1 1}^{T}\left(Z^{T} Z\right)^{-1}}{\mathbf{1}^{T}\left(Z^{T} Z\right)^{-1} \mathbf{1}}\right) Z^{T}\left(V-v_{x}(\mathbf{0})\right) \\
\\
+\left(\frac{v_{x}(\mathbf{1})-v_{x}(\mathbf{0})}{\mathbf{1}^{T}\left(Z^{T} Z\right)^{-1} \mathbf{1}}\right)\left(Z^{T} Z\right)^{-1} \mathbf{1}
\end{array}
$$

where $Z \in \mathbb{R}^{M \times d}$ and $V \in \mathbb{R}^{M}$ contain the coalitions $z^{m}$ and values $v_{x}\left(z^{m}\right)$.

Drawing from [7, 24] proved that the weighting kernel in 4 produces linear regression coefficients that are equal to the Shapley values.

### 2.3 Related Work

A number of works seek to reduce the sample variability of Shapley values. Mitchell et al. propose several Monte Carlo techniques for choosing subsets [26];
independently, Covert and Lee advocate antithetic sampling for KernelSHAP [10. Song et al. accelerate computation by storing pre-computed subsets [33. Our method can be applied on top of these methods, leveraging their contributions for added benefit.

Alternatives to sampling-based methods have also been proposed. Chen et al. derive expressions for Shapley values in settings for which the features contribute to predictions with a well-understood graphical structure 9]. FastSHAP directly predicts Shapley values using a neural network [19] it generalizes well when the neural network is trained on a large, diverse dataset. Other works more efficiently compute Shapley values given specific predictive models, e.g. Tree SHAP and Deep SHAP 2324. These methods can quickly estimate Shapley values or obtain them exactly. However, they are limited to settings that satisfy their preconditions on model types, data structures, and number of inputs to explain.

## 3 Control Variates for Shapley Values

### 3.1 Control Variates

The method of control variates is a variance reduction technique for Monte Carlo sampling problems. To reduce the error of an estimator, it leverages information about the known error of another.

Suppose $\hat{A}$ and $\hat{B}$ are unbiased estimators of $A^{*}$ and $B^{*}$, where only $B^{*}$ is known. Define the control variates estimator as

$$
\tilde{A}:=\hat{A}-c\left(\hat{B}-B^{*}\right)
$$

For any constant $c, \tilde{A}$ is an unbiased estimator of $A^{*}$. Consequently, its mean squared error (MSE) is equivalent to its variance. The optimal $c$ is selected with the following lemma, using plug-in estimates of the variance and covariance.

Lemma 1. Suppose $\hat{A}, \hat{B}$ are unbiased estimators and $\rho_{\hat{A}, \hat{B}}>0$, where $\rho$ is Pearson's correlation coefficient. Then the control variates estimator (6) has minimal variance $\operatorname{Var}(\tilde{A})=\left(1-\rho_{\hat{A}, \hat{B}}^{2}\right) \operatorname{Var}(\hat{A})$ when $c^{*}=\frac{\operatorname{Cov}(\hat{A}, \hat{B})}{\operatorname{Var}(\hat{B})}$.

### 3.2 ControlSHAP

Our method, ControlSHAP, applies the method of control variates to the Shapley values for input $x$. The estimands $A^{*}$ and $B^{*}$ in 3.1 are represented by $\phi_{j}^{\text {model }}(x)$ and $\phi_{j}^{\text {approx }}(x)$; these are the $\mathrm{j}^{\text {th }}$ Shapley values of $f$ and its Taylor approximation. In the following subsections, we will elaborate on the approximate model and its true Shapley values $\phi^{\text {approx }}(x)$.

Either Shapley sampling or KernelSHAP can be used to compute $\hat{\phi}_{j}^{\text {model }}(x)$ and $\hat{\phi}_{j}^{\text {approx }}(x)$. These are both appropriate for control variates because they are essentially unbiased for the true Shapley value (Eq. 2), whose value function
is the approximate conditional mean (Eq. 1). Trivially, Shapley sampling (Eq. 3) is unbiased, and 10 showed that KernelSHAP has negligible bias (Eq. 5). Prior works have established that these methods may be biased for the Shapley value whose value function is the true conditional mean, $v_{x}(S)=\mathbb{E}\left[f(X) \mid X_{s}\right]$; however, by definition this Shapley value is not the estimand for this problem, as these means are intractable 36|811. By virtue of (6), control variate corrections to these estimands do not change their bias.

Whichever method we choose, we must use the same subsets $S$ in computing $\hat{\phi}_{j}^{\text {model }}(x)$ and $\hat{\phi}_{j}^{\text {approx }}(x)$ to ensure they are correlated. Following Eq. 6 and Lemma 11, the ControlSHAP estimator is

$$
\begin{aligned}
\hat{\phi}_{j}^{\mathrm{CV}}(x) & =\hat{\phi}_{j}^{\mathrm{model}}(x)-\hat{\alpha}\left(\hat{\phi}_{j}^{\mathrm{approx}}(x)-\phi_{j}^{\mathrm{approx}}(x)\right) \\
\text { where } \hat{\alpha} & =\frac{\widehat{\operatorname{Cov}}\left(\hat{\phi}_{j}^{\mathrm{model}}(x), \hat{\phi}_{j}^{\mathrm{approx}}(x)\right)}{\widehat{\operatorname{Var}}\left(\hat{\phi}_{j}^{\mathrm{approx}}(x)\right)}
\end{aligned}
$$

If $\alpha$ is obtained using the oracle covariance and variance, then this estimator reduces variance and MSE by a factor of $\rho^{2}\left(\hat{\phi}_{j}(x)^{\text {model }}, \hat{\phi}_{j}(x)^{\text {approx }}\right)$.

### 3.3 Independent Features

To compute Shapley values at $x$, we must estimate the conditional mean for each sampled subset, $\mathbb{E}\left[f(X) \mid X_{S}=x_{S}\right]$. To do so, we generate a number of samples from $X \mid X_{S}$, compute $f(X)$ on each, and take a sample mean. The conditional distribution $X \mid X_{S}$ may be difficult or impossible to characterize. Because of this, the standard approach popularized by SHAP samples the features in $S^{C}$ from their marginal distributions 3424. Doing so makes the implicit assumption that the features are independent for the sake of computing $\mathbb{E}\left[f(X) \mid X_{S}=x_{S}\right]$.

Consider the second-order Taylor approximation of $f$ around $x$. If the value function is computed sampling features from their marginal distributions, then the Shapley values $\phi^{\text {approx }}(x)$ of this approximate model can be computed exactly. While we refer to this as the "independent features case," the following theorem holds regardless of whether the features are actually independent.

Theorem 1. Define $\mu:=\mathbb{E}[X]$ and $\Sigma_{j k}:=\operatorname{Cov}\left(X_{j}, X_{k}\right)$. Let the value function $v_{x}(S)$ compute conditional means by sampling each feature from its marginal distribution. The $j^{\text {th }}$ Shapley value of the second-order Taylor approximation of $f$ around $x$ is

$$
\begin{aligned}
\phi_{j}^{\text {approx }}(x)=\frac{\partial f}{\partial x_{j}} & \left(x_{j}-\mu_{j}\right) \\
& -\frac{1}{2}\left[\sum_{k=1}^{d}\left(x_{k}-\mu_{k}\right) \frac{\partial^{2} f}{\partial x_{j} x_{k}}\right]\left(x_{j}-\mu_{j}\right) \\
& -\frac{1}{2} \sum_{k=1}^{d} \Sigma_{j k} \frac{\partial^{2} f}{\partial x_{j} x_{k}}
\end{aligned}
$$

Proof of Theorem 1 is in the section 1.1 of the appendix.

### 3.4 Correlated Features

Input features are often correlated with one another. When this is the case, it may be imprudent to falsely assume independence for the sake of computational convenience. This may produce Shapley values that misrepresent the relationship between inputs and predictions, and rely on the values that a machine learning function makes in areas where it has very little data 18 .

Unfortunately, respecting feature correlations requires that we sample from $X \mid X_{S}$ for all sampled subsets $S$. Nonparametric density estimation in high dimensions is challenging due to the curse of dimensionality, and most approaches typically require considerable modeling effort.

To circumvent this, a common alternative estimates the conditional mean by characterizing $X \mid X_{S}$ as a multivariate normal distribution [8]1]. This makes the value function easy to compute, without having to ignore dependencies between the features. One can even faithfully represent binary data under this categorization by simulating Gaussian random variables and thresholding accordingly 22 .

Moreover, using this value function enables us to compute the true Shapley value of a first-order Taylor expansion of $f$. As in Theorem 1, the formula in Theorem 2 holds whether or not the features are indeed normally distributed.

Theorem 2. Define the value function to take the conditional expectation of $f(X) \mid X_{S}$ over a multivariate normal distribution. Let $S^{m} \subseteq[d] \backslash\{j\}$ be the subset of features appearing before $j$ in the $m^{\text {th }}$ permutation of $[d]$, and let $Q_{S}$ and $R_{S}$ be matrices defined in Section 1.2 of the supplementary material that do not depend on $x$. Define

$$
D_{j}:=\frac{1}{d !} \sum_{m=1}^{d !}\left(\left[Q_{S_{j}^{m} \cup j}+R_{S_{j}^{m} \cup j}\right]-\left[Q_{S_{j}^{m}}+R_{S_{j}^{m}}\right]\right)
$$

The $j^{\text {th }}$ Shapley value of the first-order Taylor approximation of $f$ around $x$ is

$$
\phi_{j}^{a p p r o x}(x)=\nabla f(x)^{T} D_{j}(x-\mu)
$$

Evaluating $\phi_{j}^{\text {approx }}(x)$ still requires computing an exponential number of terms for $D_{j}$. However, because $D_{j}$ does not depend on $x$, we can reuse it for other inputs $x$. That is, we can front-load computational work into accurately estimating $D_{j}$; then, we can instantly obtain close approximations to $\phi_{j}^{\text {approx }}(x)$ for as many inputs $x$ as we want. This is valuable if we want to estimate Shapley values at many inputs, either for future data or to provide a global notion of feature importance.

The normality condition in Therorem 2 can be relaxed somewhat. It is needed insofar as it produces conditional means of the form

$$
E\left[X_{1} \mid X_{2}=x_{2}\right]=\mu_{1}+\Sigma_{12} \Sigma_{22}^{-1}\left(x_{2}-\mu_{2}\right)
$$

which occur whenever the variance of the conditional distribution is independent of the values of the conditioning set. This property holds for all ellipticallysymmetric distributions, including the multivariate $t$-, Laplace, and logistic distributions [13].

### 3.5 Non-Differentiable Models

The discussion so far assumes that we have access to first and sometimes second derivatives of $f$. This excludes models based on trees that result in piecewise constant functions, as well as neural networks with ReLU activation functions, which have first but not second derivatives. While there are specific Shapley methods for trees [6, these only apply to models with axis-oriented splits (counter to e.g. [38].

For our purposes, we use a Taylor series only to provide linear and quadratic approximations to $f$. Thus, we can replace $\partial f / \partial x_{i}$ and $\partial^{2} f / \partial x_{i} \partial x_{j}$ with finitedifference approximations based on large step sizes, so as to approximate model behavior across substantial changes in the features.

In our experiments below, we used finite differencing on random forest predictors. We chose the step size of each numeric feature to be its marginal standard deviation; for categorical features, we swapped the observed values. Alternative choices would include basing step sizes on conditional distributions, or tuning them for agreement with $f$. Our goal has been to examine a straightforward control variate method with minimal costs both computationally and in human effort, so we have not pursued these variations here. We speculate that additional tuning would provide further improvements, which may be worthwhile in particular applications.

## 4 Variance Estimation

To use the method of control variates, we need to estimate the variance and covariance of our two estimators, as in Eq.7. This section outlines strategies for doing so.

### 4.1 Shapley Sampling

Let $G_{S}:=v_{x}(S \cup j)-v_{x}(S)$ for subset $S$. Shapley sampling selects $M$ subsets $S$ via independent permutations, then takes a sample mean of their $G_{S}$ values. Therefore the variance of Shapley sampling values is

$$
\operatorname{Var}\left(\hat{\phi}_{j}\right)=\frac{1}{M} \operatorname{Var}\left(G_{S}\right)
$$

We estimate $\operatorname{Var}\left(G_{S}\right)$ empirically across the $M$ observations of $G_{S}$. Estimating the covariance between the Shapley estimates is similarly straightfoward:

$$
\operatorname{Cov}\left(\hat{\phi}_{j}^{\text {model }}, \hat{\phi}_{j}^{\text {approx }}\right)=\frac{1}{M} \operatorname{Cov}\left(G_{S}^{\text {model }}, G_{S}^{\text {approx }}\right)
$$

which again we estimate empirically.

### 4.2 KernelSHAP

We present three approaches to estimate the KernelSHAP variance and covariance. These are unrelated to the choice of independent or correlated features.

1. Bootstrapping. For many iterations, take $M$ samples with replacement from the observed subsets $S$. Compute the KernelSHAP estimates $\hat{\phi}_{\text {boot }}^{\text {model }}$ and $\hat{\phi}_{\text {boot }}^{\text {approx }}$ on the pairs $\left\{\left(S_{\text {boot }}, v_{\text {boot }}^{\text {model }}(S)\right)\right\}_{i=1}^{M}$ and $\left\{\left(S_{\text {boot }}, v_{\text {boot }}^{\text {approx }}(S)\right)\right\}_{i=1}^{M}$. Repeat this process to produce many bootstrapped estimates of $\hat{\phi}_{\mathrm{boot}}^{\text {model }}$ and $\hat{\phi}_{\text {boot }}^{\text {approx }}$, with which we compute empirical variance and covariance.
2. Least Squares. KernelSHAP learns $\hat{\phi}$ by fitting a constrained least squares (Eq. 5). Writing $A(Z)=\left(Z^{T} Z\right)^{-1}\left[I-\left(\mathbf{1 1}^{T}\left(Z^{T} Z\right)^{-1}\right) /\left(\mathbf{1}^{T}\left(Z^{T} Z\right)^{-1} \mathbf{1}\right)\right] Z^{T}$ we make the approximation

$$
\widehat{\operatorname{Var}}(\hat{\phi})=A(Z) \operatorname{Var}\left(v_{x}(S)\right) A(Z)^{T}
$$

The diagonals of $\operatorname{Var}\left(v_{x}(S)\right)$ are computed via sample variance, provided more than one sample is used to estimate each $v_{x}(S)$. Analogously,

$$
\widehat{\operatorname{Cov}}\left(\hat{\phi}^{\text {model }}, \hat{\phi}^{\text {approx }}\right)=A(Z) \widetilde{\Sigma} A(Z)^{T}
$$

where $\widetilde{\Sigma}=\operatorname{Cov}\left(v_{x}(S)^{\text {model }}, v_{x}(S)^{\text {approx }}\right)$.

Here we note that this formula ostensibly accounts only for the sampling variability in $v_{x}(S)$ rather than the Monte Carlo choice of coalitions $Z$. However, by the total covariance formula writing $\hat{\phi}=B(Z, V)$ we have that

$$
\begin{aligned}
& \operatorname{Cov}\left(\hat{\phi}^{\text {model }}, \hat{\phi}^{\text {approx }}\right) \\
& \quad=\mathbb{E}_{Z} \operatorname{Cov}\left(B\left(Z, V^{\text {model }}\right), B\left(Z, V^{\text {approx }}\right) \mid Z\right) \\
& \quad+\operatorname{Cov}_{Z}\left(\mathbb{E}_{V} B\left(Z, V^{\text {model }}\right), \mathbb{E}_{V} B\left(Z, V^{\text {approx }}\right)\right)
\end{aligned}
$$

10] demonstrated that kernelSHAP has small bias, making the second term small, and this calculation provides a consistent estimate of the first term. $\operatorname{Var}\left(\hat{\phi}^{\text {model }}\right)$ is estimated with an equivalent calculation.

3. Grouped. 10 introduced a method based on their finding that the variance evolves at a $O\left(\frac{1}{M}\right)$ rate. First, split the $\left\{\left(S, v_{x}(S)\right)\right\}_{i=1}^{M}$ pairs into disjoint groups, and fit $\hat{\phi}^{(k)}$ in each. Then, take the empirical variance and covariance of these $\hat{\phi}^{(k)}$ values, and scale linearly.

Empirically, we observed that the bootstrapped and least squares methods yield roughly the same variances and covariances. Section 4 of the appendix shows that ControlSHAP with these two methods has nearly identical performance, across multiple datasets and machine learning models. Our experimental results all use the least squares method, since bootstrapping has a moderately higher computational cost.

In our experiments, we were not able to get the grouped method to reliably work. We observed that it occasionally produced highly erroneous estimates of variance and covariance. While this may be remedied by fitting a larger number of groups, the group size must be large enough to avoid singularity issues in fitting $\hat{\phi}^{(k)}$. More details are in Section 4 of the appendix.

## 5 Experiments

We demonstrated the efficacy of our ControlSHAP methodology on five datasets. A simulated dataset contained ten normally distributed features with block covariance structure; each feature had a correlation of 0.5 with one feature and 0.25 with another, and the response given by a logistic regression. We also used four public datasets from the UCI ML repository: Portuguese bank 27, German credit 17, census income 20, and breast cancer subtyping 3.

These real-world datasets are higher-dimensional, containing roughly 20 features on average. Many features are categorical with more than two levels, e.g. Month. We represent each of these features as a set of one-hot encodings. These transformations are necessary to use models like logistic regression and neural networks; they are also required for ControlSHAP, which takes gradients with respect to the features. The Shapley value of a categorical feature is the sum across the individual levels 24.

In the following analyses, we refer to the two approaches for the value function as assuming features are independent versus correlated (dependent). This terminology only serves to distinguish the method of sampling and Taylor expansion. It does not entail making actual assumptions about the data, as detailed in Section 3. The ControlSHAP estimator's properties such as unbiasedness do not require feature independence or Gaussianity to hold.

For each data set, and each model, we sampled 40 data points from the test set at random and estimated Shapley values 50 times for each, with and without control variates and using both correlated and independent sampling. For each estimate, we sampled 1000 coalitions. For KernelSHAP, we generated 10 points per coalition to estimate pointwise variances. We ran 200 bootstrap samples and 20 groups to estimate variances and covariances for control variates for bootstrap and grouped estimators. For Shapley sampling, which re-runs the Monte Carlo calculation for each feature, we used 1 sample per coalition. Computations were run on an internal cluster.



Fig. 1: Variance (or MSE) of Shapley estimates. Computed independent-features Shapley sampling estimates on "Prev Days" feature, using logistic regression model on Bank dataset. Bands show inner quartiles across 50 iterations.

As Figure 1 demonstrates, ControlSHAP significantly improves the variability of Shapley estimates, regardless of the number of samples drawn. For this feature - chosen because it has the highest Shapley value - adjusting the Shapley estimate consistently reduces its variance by at least $90 \%$.

Next, we consider the improvements in variance - equivalently, in MSE across all 5 datasets, using a variety of machine learning predictors. We calculated the variance reduction of our ControlSHAP methods by taking the sample variance of each feature's Shapley value across 50 iterations.

$$
\operatorname{VarReduc}_{j}(x)=\frac{\left[\widehat{\operatorname{Var}}\left(\hat{\phi}_{j}^{\text {model }}(x)\right)-\widehat{\operatorname{Var}}\left(\hat{\phi}_{j}^{\mathrm{CV}}(x)\right)\right]}{\widehat{\operatorname{Var}}\left(\hat{\phi}_{j}^{\mathrm{model}}(x)\right)}
$$



Fig. 2: Variance reductions of ControlSHAP methods. Sorted features by absolute Shapley values (unscaled in plot) with logistic regression predictor. Confidence bands denote lower and upper quartiles of Eq. 8 across 40 held-out values of $x$.

Figure 2 displays results for all features of the German Credit dataset, using logistic regression as a predictor. Our four ControlSHAP methods produce large variance reductions on all features, whose Shapley values span several orders of magnitude. On average, our final Shapley estimates have roughly $80-95 \%$ lower variability than the original estimates.

A second stability metric we used was the number of ranking changes. This metric is motivated by the fact that often practitioners care more about identifying features with high Shapley values than the values themselves [15|28|16. Formally, let $\hat{r}_{j}(x)$ be the ranking of feature $j$ within a set of $d$ Shapley estimates. For each method, we compute the average number of pairwise ranking changes across 50 resamplings.

$$
\operatorname{RankChgs}(x)=\left(\begin{array}{c}
50 \\
2
\end{array}\right)^{-1} \sum_{a \neq b}\left[\sum_{j=1}^{d}\left|\hat{r}_{j}^{a}(x)-\hat{r}_{j}^{b}(x)\right|\right]
$$

Figure 3 shows the average number of ranking changes for 40 sample inputs. We observe that the rankings are significantly more stable with the control variate. ControlSHAP averages around 20 rank changes, compared to 60 for the original estimates. Note that this statistic highly depends on the stability of Shapley sampling prior to using control variates: if the original estimates exhibit no ranking changes between simulations, this statistic will not show an improvement even if they variance of the estimates is reduced. We believe our simulations to be representative of current practice where a noticeable reduction is evident.



Fig. 3: Average number of Ranking Changes (Eq. 9) across 50 iterations, with and without ControlSHAP correction. Shapley values estimated on 40 inputs via KernelSHAP with correlated features. Neural network trained on Credit dataset.

Table 1 contains results across all 5 datasets with logistic regression, neural network, and random forest predictors. In addition to reductions in variance, we also present reductions in the number of rank changes, averaged over 40 sample inputs. Full sets of visualizations for variance reductions and rank changes can be found in Section 2 of the appendix.

In every setting, ControlSHAP reduces the variability of Shapley estimates, often by a wide margin. For both logistic regression and neural networks, at least one ControlSHAP method produces over a $50 \%$ reduction in variance and $30 \%$ reduction in number of rank changes on all five datasets. On the BRCA and German credit datasets, these figures rise to $85 \%$ and $55 \%$ for most ControlSHAP methods. Every ControlSHAP method reduces variance by over $67 \%$ on three of the four real-world datasets with logistic regression.

While ControlSHAP is generally strong for neural networks, it tends to work better when in the dependent features case. On the simulated, bank, and census

Table 1: ControlSHAP Percent Reductions in Variance (left) and Ranking Changes (right). Shapley Sampling (SS) and KernelSHAP (KS), with and without independence assumption. Averaging variance and rank-change reductions over 40 sample inputs. Taking median variance reduction of features with 5 highest Shapley values.

| Logistic Reg. | SIM | BANK |  | BRCA |  | CENSUS |  | CREDIT |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Indep., $S S$ | $10 \% \mid 6 \%$ | $76 \% \mid 57 \%$ | $75 \% \mid 57 \%$ | $33 \% \mid 13 \%$ | $83 \% \mid 60 \%$ |  |  |  |  |
| Indep., $K S$ | $24 \% \mid 17 \%$ | $84 \% \mid 43 \%$ | $87 \% \mid 54 \%$ | $3 \% \mid 2 \%$ | $94 \% \mid 67 \%$ |  |  |  |  |
| Correlated, $S S$ | $59 \% \mid 32 \%$ | $67 \% \mid$ | $42 \%$ | $92 \% \mid 68 \%$ | $71 \% \mid 58 \%$ | $85 \% \mid 64 \%$ |  |  |  |
| Correlated, $K S$ | $51 \% \mid 27 \%$ | $69 \% \mid 29 \%$ | $94 \% \mid 71 \%$ | $59 \% \mid 30 \%$ | $87 \% \mid 59 \%$ |  |  |  |  |


| Neural Net | SIM | BANK | BRCA | CENSUS | CREDIT |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Indep., $S S$ | $9 \% \mid 6 \%$ | $8 \% \mid 2 \%$ | $76 \% \mid 52 \%$ | $4 \% \mid 3 \%$ | $55 \% \mid 36 \%$ |  |
| Indep., $K S$ | $22 \% \mid 15 \%$ | $25 \% \mid 8 \%$ | $86 \% \mid 55 \%$ | $-1 \% \mid 1 \%$ | $80 \% \mid 45 \%$ |  |
| Correlated, $S S$ | $58 \% \mid 31 \%$ | $58 \% \mid 37 \%$ | $92 \% \mid 65 \%$ | $61 \% \mid 42 \%$ | $84 \% \mid 61 \%$ |  |
| Correlated, $K S$ | $51 \% \mid 28 \%$ | $40 \% \mid 13 \%$ | $92 \% \mid 68 \%$ | $51 \% \mid 24 \%$ | $87 \% \mid 60 \%$ |  |


| RF |  | BANK |  | BRCA |  |  |  | CREDIT |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Indep., $S S$ | $31 \%$ |  | $3 \%$ | $3 \%$ | $19 \%$ | $7 \%$ | 4 | $2 \%$ | $15 \%$ | $6 \%$ |
| Indep |  | 19 |  | 3 | $14 \%$ | 69 |  |  | $14 \%$ | $6 \%$ |
| orrel | 6\% | 319 | 0 | $5 \%$ | $\%$ | 1 | $\%$ | $5^{0}$ | $4 \%$ | $17 \%$ |
| orrelated, 1 | $54 \%$ | 31 | $1 \%$ | $-2 \%$ | $17 \%$ | $9 \%$ | $3 \%$ | $-1 \%$ | $22 \%$ | $10 \%$ |

datasets, variance reductions are typically below $25 \%$ assuming independence and above $50 \%$ otherwise. Presumably, this owes to the fact that neural networks are less smooth. The quadratic model from the independent features case (Thm. 1) is more prone to neural networks' steep gradients and hessians, and may poorly approximate model behavior as a result.

When the machine learning model is not differentiable, gradients and hessians can be taken via finite differencing. These coarse estimates use a smooth approximation to step-wise constant model behavior, which also results in a lower correlation between our target and control variate.

Nevertheless, ControlSHAP increases stability on random forests, again particularly in the correlated features case. Figure 4 showcases its solid performance on the simulated dataset, reducing variability by over $50 \%$ with dependent features. Table 1 shows its reductions in variance and rank changes on all datasets and ControlSHAP methods.

Finally, we analyzed the ControlSHAP estimates to confirm they are unbiased. While the true SHAP values are computationally prohibitive to compute, their sum is known to be $f(x)-E[f(X)]$ by the efficiency property 24|32]. To search for bias, we compared the sum of Shapley estimates from this target, across multiple ML predictors. Figure 5 demonstrates that ControlSHAP ex-



Fig. 4: Variance Reductions of Random Forest on simulated dataset with 10 features. Upper and lower quantiles of reductions provided across 40 inputs. Computed gradients via finite differencing.



Fig. 5: Normalized absolute difference from sum of Shapely estimates to $f(x)-$ $E f(X)$. Ran for 10 iterations on credit dataset with independent features.

hibits no evidence of bias; on the contrary, the sum of its Shapley estimates is typically closer to the target.

## 6 Discussion

While Shapley values are capable of providing useful model explanations, they fall short in one critical way: stability. Stability is necessary to instill trust in our interpretations of black-box machine learning algorithms. Practitioners cannot use such a system with confidence if rerunning the same procedure yields different explanations.

This work proposes a method, ControlSHAP, to address this. ControlSHAP can be applied in conjunction with other attempts to mitigate sampling variability. Further, while designed for differentiable models, it can help explain other predictive models via finite differencing. Specifically, it adjusts Shapley estimates using the method of control variates, which track the extent to which the random samples over- or underestimate on a correlated estimator.

ControlSHAP stabilizes Shapley estimates across a wide range of datasets and algorithms, in some cases reducing variability by as high as $90 \%$. Moreover,
we can easily obtain accurate estimates of the added benefit from performing ControlSHAP adjustments. Recall that ControlSHAP reduces variance by approximately $\rho^{2}\left(\hat{\phi}_{j}(x)^{\text {model }}, \hat{\phi}_{j}(x)^{\text {approx }}\right)($ Eq. 7). We can estimate this correlation using the variance and covariance used to compute $\widehat{\alpha}$; this enables us to estimate the variance reduction. As section 3 in the appendix demonstrates, these anticipated reductions closely mirror the empirical quantities.

Alternatively, ControlSHAP can be used to accelerate convergence. 10, for example, suggest terminating when the variability falls below a certain threshold. Using the control variate here could lead to a dramatic speed-up. Note in Figure 1 that the ControlSHAP estimates have comparable variability after 100 iterations as the original values after 1000 .

ControlSHAP can be employed as a relatively "off-the-shelf" tool, in the sense that it stabilizes Shapley estimates with close to no extra computational or modeling work. The only model insight required is the gradient, as well as the hessian in the independent features case. Computationally, the single substantial cost is in the correlated features case, which requires accurate estimation of pre-compute matrices. Otherwise, ControlSHAP only necessitates passing each $X \mid X_{S}$ through the Taylor approximation, and computing the Shapley values' covariance - both of which are extremely quick tasks.

It is worth noting that other explanation algorithms also suffer from various forms of instability. 41 and 40 found that the explanations from LIME and distillation trees are sensitive to the synthetic data used to generate them. In addition, counterfactual explanations for adjacent points may be subject to vary widely 21.

These drawbacks motivate future work stabilizing model explanations. Shapley computations may benefit from tuning finite differences, more sophisticated Monte Carlo schemes, or alternative control variates. In some contexts it may be preferable to use inherently interpretable models like decision trees or the LASSO 31 137. We intend ControlSHAP to complement these models, enabling more trustworthy use of black-box methods.

## References

1. Aas, K., Jullum, M., Løland, A.: Explaining individual predictions when features are dependent: More accurate approximations to shapley values. Artif. Intell. 298, $103502(2021)$
2. Belle, V., Papantonis, I.: Principles and practice of explainable machine learning. Frontiers Big Data 4, 688969 (2021)
3. Berger, A., Korkut, A., Kanchi, R.S., Group, T.P.G., Mills, G.B., Levine, D.A., Akbani, R.: A comprehensive tcga pan-cancer molecular study of gynecologic and breast cancers. Cancer Cell 33 (2018)
4. Berk, R.: Machine Learning Risk Assessments in Criminal Justice Settings. Springer (2019)
5. Breiman, L.: Random forests. Mach. Learn. 45(1), 5-32 (2001)
6. Campbell, T.W., Roder, H., Georgantas III, R.W., Roder, J.: Exact shapley values for local and model-true explanations of decision tree ensembles. Machine Learning with Applications 9, 100345 (2022)
7. Charnes, A., Golany, B., Keane, M., Rousseau, J.: Extremal principle solutions of games in characteristic function form: core, Chebychev and Shapley value generalizations, pp. 123-133. Springer (1988)
8. Chen, H., Janizek, J.D., Lundberg, S.M., Lee, S.: True to the model or true to the data? CoRR abs/2006.16234 (2020)
9. Chen, J., Song, L., Wainwright, M.J., Jordan, M.I.: L-shapley and c-shapley: Efficient model interpretation for structured data. CoRR abs/1808.02610 (2018)
10. Covert, I., Lee, S.: Improving kernelshap: Practical shapley value estimation via linear regression. CoRR abs/2012.01536 (2020)
11. Covert, I., Lundberg, S.M., Lee, S.: Understanding global feature contributions through additive importance measures. CoRR abs/2004.00668 (2020)
12. Dubey, R., Chandani, A.: Application of machine learning in banking and finance: a bibliometric analysis. Int. J. Data Anal. Tech. Strateg. 14(3) (2022)
13. Fang, K.T., Kotz, S., Ng, K.W.: Symmetric Multivariate and Related Distributions. Chapman and Hall (1990)
14. Ferdous, M., Debnath, J., Chakraborty, N.R.: Machine learning algorithms in healthcare: A literature survey. In: 11th International Conference on Computing, Communication and Networking Technologies, ICCCNT 2020, Kharagpur, India, July 1-3, 2020. pp. 1-6. IEEE (2020)
15. Ghorbani, A., Zou, J.Y.: Neuron shapley: Discovering the responsible neurons. In: Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., Lin, H. (eds.) Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual (2020)
16. Goli, A., Mohammadi, H.: Developing a sustainable operational management system using hybrid Shapley value and Multimoora method: case study petrochemical supply chain. Environment, Development and Sustainability: A Multidisciplinary Approach to the Theory and Practice of Sustainable Development 24(9), 1054010569 (September 2022). https://doi.org/10.1007/s10668-021-01844-
17. Hofmann, H.: Statlog (german credit data) (Nov 1994)
18. Hooker, G., Mentch, L., Zhou, S.: Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance. Statistics and Computing 31, 1-16 (2021)
19. Jethani, N., Sudarshan, M., Covert, I.C., Lee, S., Ranganath, R.: Fastshap: Realtime shapley value estimation. In: The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022. OpenReview.net (2022)
20. Kohavi, R.: Census income (Apr 1996)
21. Laugel, T., Lesot, M., Marsala, C., Detyniecki, M.: Issues with post-hoc counterfactual explanations: a discussion. CoRR abs/1906.04774 (2019), http://arxiv. org/abs/1906.04774
22. Leisch, F., Weingessel, A., Hornik, K.: On the generation of correlated artificial binary data. SFB Adaptive Information Systems and Modelling in Economics and Management Science 20 (02 1970)
23. Lundberg, S.M., Erion, G.G., Chen, H., DeGrave, A.J., Prutkin, J.M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., Lee, S.: From local explanations to global understanding with explainable AI for trees. Nat. Mach. Intell. 2(1), 56-67 (2020). https://doi.org/10.1038/s42256-019-0138-9, https://doi.org/10. 1038/s42256-019-0138-9
24. Lundberg, S.M., Lee, S.: A unified approach to interpreting model predictions. In: Guyon, I., von Luxburg, U., Bengio, S., Wallach, H.M., Fergus, R., Vishwanathan,

S.V.N., Garnett, R. (eds.) Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA. pp. 4765-4774 (2017)

25. Mandalapu, V., Elluri, L., Vyas, P., Roy, N.: Crime prediction using machine learning and deep learning: A systematic review and future directions. IEEE Access 11, 60153-60170 (2023)
26. Mitchell, R., Cooper, J., Frank, E., Holmes, G.: Sampling permutations for shapley value estimation. J. Mach. Learn. Res. 23, 43:1-43:46 (2022)
27. Moro, S., Cortez, P., Rita, P.: A data-driven approach to predict the success of bank telemarketing. Decis. Support Syst. 62, 22-31 (2014)
28. Narayanam, R., Narahari, Y.: Determining the top-k nodes in social networks using the shapley value. In: Padgham, L., Parkes, D.C., Müller, J.P., Parsons, S. (eds.) 7th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS 2008), Estoril, Portugal, May 12-16, 2008, Volume 3. pp. 15091512. IFAAMAS (2008)
29. Oates, C.J., Girolami, M., Chopin, N.: Control functionals for monte carlo integration. Journal of the Royal Statistical Society Series B: Statistical Methodology $\mathbf{7 9}(3), 695-718$ (2017)
30. Ribeiro, M.T., Singh, S., Guestrin, C.: "why should I trust you?": Explaining the predictions of any classifier. In: Krishnapuram, B., Shah, M., Smola, A.J., Aggarwal, C.C., Shen, D., Rastogi, R. (eds.) Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, August 13-17, 2016. pp. 1135-1144. ACM (2016)
31. Rudin, C.: Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. Nat. Mach. Intell. 1(5), 206-215 (2019). https://doi.org/10.1038/s42256-019-0048-x https://doi.org/10.1038/ s42256-019-0048-x
32. Shapley, L.: A value for n-person games (March 1952)
33. Song, E., Nelson, B.L., Staum, J.: Shapley effects for global sensitivity analysis: Theory and computation. SIAM/ASA J. Uncertain. Quantification 4(1), 1060-1083 (2016)
34. Strumbelj, E., Kononenko, I.: An efficient explanation of individual classifications using game theory. J. Mach. Learn. Res. 11, 1-18 (2010)
35. Strumbelj, E., Kononenko, I.: Explaining prediction models and individual predictions with feature contributions. Knowl. Inf. Syst. 41(3), 647-665 (2014)
36. Sundararajan, M., Najmi, A.: The many shapley values for model explanation. In: Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event. Proceedings of Machine Learning Research, vol. 119, pp. 9269-9278. PMLR (2020), http://proceedings.mlr.press/v119/ sundararajan20b.html
37. Tibshirani, R.: Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society. Series B (Methodological) 58(1), 267-288 (1996)
38. Tomita, T.M., Browne, J., Shen, C., Chung, J., Patsolic, J.L., Falk, B., Priebe, C.E., Yim, J., Burns, R., Maggioni, M., et al.: Sparse projection oblique randomer forests. The Journal of Machine Learning Research 21(1), 4193-4231 (2020)
39. Verma, S., Dickerson, J.P., Hines, K.: Counterfactual explanations for machine learning: A review. CoRR abs/2010.10596 (2020)
40. Zhou, Y., Zhou, Z., Hooker, G.: Approximation trees: Statistical stability in model distillation. CoRR abs/1808.07573 (2018), http://arxiv.org/abs/1808.07573
41. Zhou, Z., Hooker, G., Wang, F.: S-LIME: stabilized-lime for model explanation. In: Zhu, F., Ooi, B.C., Miao, C. (eds.) KDD '21: The 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Virtual Event, Singapore, August 1418, 2021. pp. 2429-2438. ACM (2021). https://doi.org/10.1145/3447548.3467274, https://doi.org/10.1145/3447548.3467274

## Appendix

## 1 Exact Shapley Values

### 1.1 Shapley Value, Assuming Feature Independence

Proof. Assume features are sampled independently in the value function. Consider a second-order Taylor approximation to $f$ at $x$ :

$$
g\left(x^{\prime}\right):=f(x)+\left(x^{\prime}-x\right)^{T} \nabla f(x)+\frac{1}{2}\left(x^{\prime}-x\right)^{T} \nabla^{2} f(x)\left(x^{\prime}-x\right)
$$

Let $J=\nabla f(x), H=\nabla^{2} f(x), \Sigma=\operatorname{Cov}(X)$, and $\sigma_{k \ell}^{2}=\operatorname{Cov}\left(X_{k}, X_{\ell}\right)$. The Shapley value function is

$$
\begin{aligned}
v_{x}(S)= & E\left[g\left(X^{\prime}\right) \mid X_{S}^{\prime}=x_{S}\right] \\
=f(x)+ & E\left[\left(x^{\prime}-x\right) \mid X_{S}^{\prime}=x_{S}\right]^{T} \nabla f(x) \\
& +\frac{1}{2} E\left[\left(x^{\prime}-x\right)^{T} \nabla^{2} f(x)\left(x^{\prime}-x\right) \mid X_{S}^{\prime}=x_{S}\right] \\
=f(x)+ & \left(\mu_{S^{C}}-x_{S^{C}}\right)^{T} J_{S^{C}} \\
& +\frac{1}{2} E\left[\left(x_{S^{C}}^{\prime}-x_{S^{C}}\right)^{T} \nabla^{2} f(x)_{S^{C} S^{C}}\left(x_{S^{C}}^{\prime}-x_{S^{C}}\right)\right]
\end{aligned}
$$

where the quadratic term is equal to

$$
\begin{aligned}
& \operatorname{tr}\left(H_{S^{C} S^{C}} \Sigma_{S^{C} S^{C}}\right)+\left(\mu_{S^{C}}-x_{S^{C}}\right)^{T} H_{S^{C} S^{C}}\left(\mu_{S^{C}}-x_{S^{C}}\right) \\
= & \sum_{k \in S^{C}} \sum_{\ell \in S^{C}} H_{k \ell}\left(\sigma_{k \ell}^{2}+\left(\mu_{k}-x_{k}\right)\left(\mu_{\ell}-x_{\ell}\right)\right) \\
= & H_{j j}\left(\sigma_{j j}^{2}+\left(\mu_{j}-x_{j}\right)^{2}\right)
\end{aligned}
$$

Recall $\phi_{j}(x):=\frac{1}{d} \sum_{S \subseteq[d] \backslash\{j\}}\left(\begin{array}{c}d-1 \\ |S|\end{array}\right)^{-1}\left(v_{x}(S \cup\{j\})-v_{x}(S)\right)$. The difference in value functions is

$$
\begin{aligned}
& v_{x}(S \cup j)-v_{x}(S)=\underbrace{\left(x_{j}-\mu_{j}\right) J_{j}-\frac{1}{2} H_{j} j\left(\sigma_{j}^{2}+\left(\mu_{j}-x_{j}\right)^{2}\right)}_{\text {(a) }} \\
&-\underbrace{\sum_{k \in(S \cup j)^{C}} \underbrace{\left.H_{j k}\left[\sigma_{j k}^{2}+\left(\mu_{j}-x_{j}\right)\left(\mu_{k}-x_{k}\right)\right)\right]}_{\text {C }}}_{\text {b) }}
\end{aligned}
$$

Define the Shapley weight $w_{S}=\frac{1}{d}\left(\begin{array}{c}d-1 \\ |S|\end{array}\right)^{-1}$.

$$
\begin{aligned}
\phi_{j}(x) & \left.=\sum_{S \subseteq[d] \backslash\{j\}} w_{S}(\mathrm{a})-\text { (b) }\right) \\
& =\left(\sum_{S \subseteq[d] \backslash\{j\}} w_{S}-\sum_{S \subseteq[d] \backslash\{j\}} w_{S}\right. \text { (b) } \\
\sum_{S \subseteq[d] \backslash\{j\}} w_{S}(\mathrm{~b}) & =\sum_{S \subseteq[d] \backslash\{j\}} w_{S} \sum_{k \in\{S \cup j\}^{C}} \text { (C) } \\
& =\sum_{S \subseteq[d] \backslash\{j\}} \sum_{k \in\{S \cup j\}^{C}} w_{S}(\mathrm{C} \\
& =\sum_{k \neq j} \sum_{S \subseteq[d] \backslash\{j, k\}} w_{S} \text { C } \\
& =\sum_{k \neq j}\left(\sum_{S \subseteq[d] \backslash\{j, k\}} w_{S}\right.
\end{aligned}
$$

Noting subsets of equal size have the same Shapley weight, we can easily show $\sum_{S \subseteq[d] \backslash j\}} w_{S}=1$.

$$
\begin{aligned}
\sum_{S \subseteq[d] \backslash\{j\}} w_{S} & =\sum_{S \subseteq[d] \backslash\{j\}} \frac{1}{d}\left(\begin{array}{c}
d-1 \\
|S|
\end{array}\right)^{-1} \\
& =\sum_{a=0}^{d-1}\left(\begin{array}{c}
d-1 \\
a
\end{array}\right) \frac{1}{d}\left(\begin{array}{c}
d-1 \\
a
\end{array}\right)^{-1}=\sum_{a=0}^{d-1} \frac{1}{d}=1
\end{aligned}
$$

With a bit more arithmetic, we can show $\sum_{S \subseteq[d] \backslash\{j, k\}} w_{S}=\frac{1}{2}$.

$$
\begin{aligned}
\sum_{S \subseteq[d] \backslash\{j, k\}} w_{S} & =\sum_{a=0}^{d-2}\left(\begin{array}{c}
d-2 \\
a
\end{array}\right) \frac{1}{d}\left(\begin{array}{c}
d-1 \\
a
\end{array}\right)^{-1} \\
& =\sum_{a=0}^{d-2} \frac{(d-2) !}{a !(d-a-2) !} \frac{a !(d-a-1) !}{d !} \\
& =\sum_{a=0}^{d-2} \frac{d-a-1}{d(d-1)} \\
& =\frac{1}{d(d-1)}\left[d(d-1)-\sum_{a=0}^{d-2}(a+1)\right] \\
& =\frac{1}{d(d-1)}\left[d(d-1)-\frac{d(d-1)}{2}\right]=\frac{1}{2}
\end{aligned}
$$

Plugging the results of 11 and 12 into 10 yields the final expression for the Shapley value:

$$
\begin{aligned}
& \phi_{j}(x)= \sum_{S \subseteq[d] \backslash\{j\}} w_{S}-\sum_{S \subseteq[d] \backslash\{j\}} w_{S} \text { b } \\
&=-\frac{1}{2} \sum_{k \neq j} \text { (c) } \\
&=\left(x_{j}-\mu_{j}\right) J_{j}-\frac{1}{2} H_{j} j\left(\sigma_{j}^{2}+\left(\mu_{j}-x_{j}\right)\right) \\
&\left.-\frac{1}{2} \sum_{k \neq j} H_{j k}\left[\sigma_{j k}^{2}+\left(\mu_{j}-x_{j}\right)\left(\mu_{k}-x_{k}\right)\right)\right] \\
&=\left(x_{j}-\right.\left.\left.\mu_{j}\right) J_{j}-\frac{1}{2}\left[\sum_{k=1}^{d}\left(x_{k}-\mu_{k}\right) H_{j k}\right)\right]\left(x_{j}-\mu_{j}\right) \\
& \quad-\frac{1}{2} \sum_{k=1}^{d} \sigma_{j k}^{2} H_{j k}
\end{aligned}
$$

### 1.2 Shapley Value, Correlated Features

Consider the linear model $g\left(x^{\prime}\right)=\beta^{T} x^{\prime}+b$, where $x^{\prime} \sim \mathcal{N}(\mu, \Sigma)$. (For our problem, $\beta=\nabla f(x)$ and $b=f(x)$.)

Let $P_{S}$ be the projection matrix selecting set $S$; define $R_{S}=P_{\bar{S}}^{T} P_{\bar{S}} \Sigma P_{S}^{T}\left(P_{S} \Sigma P_{S}^{T}\right)^{-1} P_{S}$ and $Q_{S}=P_{S}^{T} P_{S}$. We consider the set of permutations of $[d]$, each of which indexes a subset $S$ as the features that appear before $j$. Averaging over all such permutations, the Shapley values of $g(x)$ [24|8|1] are

$$
\begin{aligned}
\phi_{j}\left(x^{\prime}\right)=\beta \underbrace{\left[\frac{1}{d !} \sum_{m}\left(\left[Q_{\left\{S^{m} \cup j\right\}^{C}}-R_{S^{m} \cup j}\right]-\left[Q_{\left\{S^{m}\right\}^{C}}-R_{S^{m}}\right]\right)\right]}_{C_{j}} \mu \\
+\beta \underbrace{\left[\frac{1}{d !} \sum_{m}\left(\left[Q_{S^{m} \cup j}+R_{S^{m} \cup j}\right]-\left[Q_{S^{m}}+R_{S^{m}}\right]\right)\right]}_{D_{j}} x^{\prime}
\end{aligned}
$$

Lastly, we observe that $C_{j}=-D_{j}$. For each subset $S$, the $R$ terms cancel out; $Q_{S^{C}}+Q_{S}=I_{d}$, so $Q_{\{S \cup j\}^{C}}-Q_{S^{C}}=-\left(Q_{S \cup j}-Q_{S}\right)$. This yields our expression for the dependent Shapley value:

$$
\phi_{j}^{g}(x)=\beta^{T} D_{j}(x-\mu)
$$

## 2 Comprehensive Results

We display results across all 5 datasets and 3 machine learning predictors. All datasets were binary classification problems, so we used the same models to fit them. For logistic regression and random forest, we used the sklearn implementation with default hyperparameters. For the neural network, we fit a two-layer MLP in Pytorch with 50 neurons in the hidden layer and hyperbolic tangent activation functions.

Figure 6 displays the variance reductions of our ControlSHAP methods in the four settings: Independent vs Dependent Features, and Shapley Sampling vs KernelSHAP. The error bars span the $2^{\text {th }}$ to $7^{\text {th }}$ percentiles of the variance reductions for 40 held-out samples.

Figure 7 compares the average number of changes in rankings between the original and ControlSHAP Shapley estimates. Specifically, we look the Shapley estimates obtained via KernelSHAP, assuming correlated features.

## 3 Anticipated Correlation

Figure 8 compares the observed and anticipated variance reductions, across two combinations of dataset and predictor. Recall that the variance reduction of the control variate estimate for $\phi_{j}(x)$ is $\rho^{2}\left(\hat{\phi}_{j}(x)^{\text {model }}, \hat{\phi}_{j}(x)^{\text {approx }}\right)$, where $\rho$ is the Pearson's correlation coefficient. We compute the sample correlation coefficient of the Shapley values on sample $x$ as follows:

$$
\hat{\rho}:=\frac{\widehat{\operatorname{Cov}}\left(\hat{\phi}_{j}(x)^{\text {model }}, \hat{\phi}_{j}(x)^{\text {approx }}\right)}{\sqrt{\widehat{\operatorname{Var}}\left(\hat{\phi}_{j}(x)^{\text {model })} \widehat{\operatorname{Var}}\left(\hat{\phi}_{j}(x)^{\text {approx }}\right)\right.}}
$$

We average this across the 50 iterations to obtain a single estimate for the correlation $\hat{\rho}$. The plots display the median and error bars for $\hat{\rho}^{2}\left(\hat{\phi}_{j}(x)^{\text {model }}, \hat{\phi}_{j}(x)^{\text {approx }}\right)$ across 40 samples. Once again, the error bars span the $2^{\text {th }}$ to $7^{\text {th }}$ percentiles.



(a) Logistic Regression



(b) Neural Network



(c) Random Forest

Fig. 6: Variance Reductions


(a) Logistic Regression


Neural Network


(c) Random Forest

Fig. 7: Average Number of Rank Changes, with and without ControlSHAP's adjustment via Control Variates (CV).


(a) Shapley Sampling


(b) KernelSHAP, Least Squares Variance Estimation


(c) KernelSHAP, Bootstrapped Variance Estimation

Fig. 8: Anticipated vs Observed Variance Reduction

## 4 Comparing KernelSHAP Variance Estimators

Section 4.2 of the paper details methods for computing the variance and covariance between KernelSHAP estimates. Bootstrapping and the least squares covariance produce extremely similar estimates. In turn, these produce ControlSHAP estimates that reduce variance by roughly the same amount, as shown in Figure 9 This indicates that both methods are appropriate choices.

In contrast, we were not able to get the grouped method to reliably work. Its variance estimates were somewhat erratic, as they are drawn from a heavytailed $\chi^{2}$ distribution (Figure 10). As a result, its ControlSHAP estimates were occasionally more variable than the original KernelSHAP values themselves.



Fig. 9: Variance reductions of ControlSHAP across 40 samples with bootstrapped and least-squares estimates of KernelSHAP variance and covariance. Shapley estimates computed assuming independent features.



Fig. 10: Correlation between model and Taylor approximation, grouped and least squares. Same input and feature across 50 iterations, with logistic regression on the bank dataset.


[^0]:    1 https://github.com/jeremy-goldwasser/ControlSHAP contains our code and experimental results.

