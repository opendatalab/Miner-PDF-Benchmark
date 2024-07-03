# Improving prediction accuracy by choosing resampling distribution via cross-validation 

Wataru Yoshida and Kei Hirose<br>Kyushu University


#### Abstract

In a regression model, prediction is typically performed after model selection. The large variability in the model selection makes the prediction unstable. Thus, it is essential to reduce the variability in model selection and improve prediction accuracy. To achieve this goal, a parametric bootstrap smoothing can be applied. In this method, model selection is performed for each resampling from a parametric distribution, and these models are then averaged such that the distribution of the selected models is considered. Here, the prediction accuracy is highly dependent on the choice of a distribution for resampling. In particular, an experimental study shows that the choice of error variance significantly changes the distribution of the selected model and thus plays a key role in improving the prediction accuracy. We also observed that the true error variance does not always provide optimal prediction accuracy. Therefore, it would not always be appropriate to use unbiased estimators of the true parameters or standard estimators of the parameters for the resampling distribution. In this study, we propose employing cross validation to choose a suitable resampling distribution rather than unbiased estimators of parameters. Our proposed method was applied to electricity demand data. The results indicate that the proposed method provides a better prediction accuracy than the existing method.


## 1 Introduction

In regression modeling, estimation and prediction are typically performed after model selection. Reducing the variability in model selection is essential for achieving high accuracy. In addition, this variability should be considered when creating confidence or prediction intervals. The problem of appropriately handling the uncertainty caused by the model selection process is called selective inference Taylor and Tibshirani 2015. For example, the selective inference in lasso estimation is researched by Lee et al. 2016 .

To reduce variability in model selection and improve prediction accuracy, we may use parametric bootstrap smoothing. Parametric bootstrap smoothing performs model selection for each resam-
pling from a parametric distribution, and these models are averaged such that the distribution of the selected models is considered. Thus, this method is expected to reduce the variability in model selection and improve prediction accuracy. A similar smoothing method using nonparametric bootstrapping is well-known in the field of machine learning under the name of bagging Breiman 1996]. For these smoothing methods, Efron [2014 proposed a formula for computing the standard errors of the estimators. Using this formula, we can construct the prediction interval in parametric bootstrap smoothing.

Suppose a sample follows the regression model $N\left(X \boldsymbol{\beta}, \sigma^{2} I_{n}\right)$. To apply parametric bootstrap smoothing to estimate $\boldsymbol{\beta}$, the distribution for resampling must be set. A general approach is to choose $N\left(X \hat{\boldsymbol{\beta}}_{O L S}, \hat{\sigma}_{U B}^{2}\right)$ as the resampling distribution MacKinnon 2006. Here, $\hat{\boldsymbol{\beta}}_{O L S}$ and $\hat{\sigma}_{U B}^{2}$ denote the ordinary least squares (OLS) estimator of the coefficient vector and the unbiased estimator of the variance based on $\hat{\boldsymbol{\beta}}_{O L S}$, respectively. However, in this study, we found that some distributions significantly outperform those based on OLS in terms of predictive accuracy. In fact, our simulation shows that the choice of error variance changes the distribution of the selected model and thus significantly affects prediction accuracy. We also discovered that choosing the true $\sigma^{2}$ for the resampling distribution did not always provide the optimal prediction accuracy. This suggests that it is inappropriate to use $\hat{\sigma}_{U B}^{2}$ for the resampling distribution, even though $\hat{\sigma}_{U B}^{2}$ is an unbiased estimator of the true variance. In addition, our simulation shows that it may not be optimal to set the mean vector to $X \hat{\boldsymbol{\beta}}_{O L S}$, especially when the true model is not full model. Therefore, we propose a method for choosing the resampling distribution by cross-validation, rather than model estimation. The proposed method searches for a distribution that specializes in improving the prediction of parametric bootstrap smoothing, whereas the existing methods select a distribution that fits the data. The proposed method is applied to predict the electricity demand. The results indicate that the proposed method provides better prediction accuracy than the existing methods.

The remainder of this paper is organized as follows. In Section 2, we introduce the prediction and the prediction interval construction using parametric bootstrap smoothing. In Section 3, we show the effect of the choice of the resampling distribution on the prediction accuracy from the experimental results of applying it to electricity demand data. Then, we propose a method for choosing a resampling distribution by cross-validation and show the results of an actual application to electricity demand data. In Section 4, we discuss through simulation why some choices of distribution provide better prediction accuracy than OLS-based distribution. In the simulation, the variance and mean vector of a resampling distribution were varied, and the prediction error and distribution of the selected models were examined. Finally, the conclusions are presented in Section 5 .

## 2 Prediction using parametric bootstrap smoothing

### 2.1 Parametric bootstrap smoothing

Let $\mathbf{y}=\left(y_{1}, \ldots, y_{n}\right)^{T}$ be the vector of $n$ observations. We assume that $\mathbf{y}$ follows the linear regression model:

$$
\mathbf{y}=X \boldsymbol{\beta}+\varepsilon, \quad \boldsymbol{\varepsilon} \sim N\left(0, \sigma^{2} I_{n}\right)
$$

where $X$ is an $n \times p$ design matrix with $X:=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)^{T}$ and $\boldsymbol{\beta}$ is a $p \times 1$ regression coefficient vector. Now, assume that we obtain $\mathbf{x}_{\text {new }}$, and $y_{\text {new }}$ follows the linear regression model:

$$
y_{n e w}=\mathbf{x}_{n e w}^{T} \boldsymbol{\beta}+\varepsilon_{n e w}, \quad \varepsilon_{n e w} \sim N\left(0, \sigma^{2}\right)
$$

Our aim is to obtain the prediction value and prediction interval of $y_{\text {new }}$. We derive $\hat{\boldsymbol{\beta}}$, the estimator of $\boldsymbol{\beta}$ and predict $y_{\text {new }}$ as $\hat{\mu}(\mathbf{y}):=\mathbf{x}_{\text {new }}^{T} \hat{\boldsymbol{\beta}}$. Model selection is conducted to derive $\hat{\boldsymbol{\beta}}$. For example, cross-validation [Stone 1974], AIC [Akaike 1974], and sparse estimation can be considered. If $n$ is not sufficiently large for $p$, the model selection is unstable, and the prediction value of $y_{n e w}$ is also unstable. To address this problem, we use parametric bootstrap smoothing (see, for example, Efron 2014):

1. Compute $\hat{\boldsymbol{\beta}}_{O L S}=\left(X^{T} X\right)^{-1} X^{T} \mathbf{y}$ and $\hat{\sigma}^{2}$ that is an estimate of $\sigma^{2}$.
2. Generate bootstrap sample $\mathbf{y}_{1}^{*}, \ldots, \mathbf{y}_{B}^{*}$, where $\mathbf{y}_{i}^{*} \sim N\left(X \hat{\boldsymbol{\beta}}_{O L S}, \hat{\sigma}^{2} I_{n}\right)$ for $i=1, \ldots, B$.
3. Derive $\hat{\boldsymbol{\beta}}\left(\mathbf{y}_{1}^{*}\right), \ldots, \hat{\boldsymbol{\beta}}\left(\mathbf{y}_{B}^{*}\right)$ that are estimates of $\boldsymbol{\beta}$ from each bootstrap sample $\mathbf{y}_{i}^{*}$.
4. Compute the mean of estimates as $\hat{\boldsymbol{\beta}}_{P B S}(\mathbf{y}):=\frac{1}{B} \sum_{b=1}^{B} \hat{\boldsymbol{\beta}}\left(\mathbf{y}_{b}^{*}\right)$, and we get the prediction of $y_{\text {new }}$ as follows:

$$
\hat{\mu}_{P B S}(\mathbf{y}):=x_{n e w}^{T} \hat{\boldsymbol{\beta}}_{P B S}(\mathbf{y})
$$

In Step 3, note that the result of the model selection varies with each bootstrap sampling, that is, even if $\hat{\beta}_{k}\left(\mathbf{y}_{i}^{*}\right)=0$, it may be $\hat{\beta}_{k}\left(\mathbf{y}_{j}^{*}\right) \neq 0(i \neq j)$. Here, $\hat{\beta}_{l}\left(\mathbf{y}_{m}^{*}\right)$ denotes lth component of $\hat{\boldsymbol{\beta}}\left(\mathbf{y}_{m}^{*}\right)$. In Step 4, the randomness of model selection is smoothed.

### 2.2 Prediction interval

We consider a 100(1- $\alpha) \%$ prediction interval for $y_{\text {new }}$ similar to the confidence interval derivation process proposed by Efron 2014. First, the estimator of $V\left(\hat{\mu}_{P B S}(\mathbf{y})\right)$ is derived by using the delta method as follows:

$$
\hat{V}\left(\hat{\mu}_{P B S}(\mathbf{y})\right):=\frac{1}{\hat{\sigma}^{2}} \widehat{\operatorname{Cov}}^{T}\left(X^{T} X\right)^{-1} \widehat{\operatorname{Cov}}
$$

where

$$
\widehat{\operatorname{Cov}}:=\frac{1}{B} \sum_{b=1}^{B}\left(\hat{\mu}\left(\mathbf{y}_{b}^{*}\right)-\hat{\mu}_{P B S}(\mathbf{y})\right)\left(X^{T} \mathbf{y}_{b}^{*}-X^{T} \overline{\mathbf{y}}^{*}\right), \quad \overline{\mathbf{y}}^{*}:=\frac{1}{B} \sum_{b=1}^{B} \mathbf{y}_{b}^{*}, \hat{\mu}\left(\mathbf{y}_{b}^{*}\right):=x_{n e w}^{T} \hat{\boldsymbol{\beta}}\left(\mathbf{y}_{b}^{*}\right)
$$

Next, $V\left(\varepsilon_{\text {new }}\right)$ is estimated as $\frac{1}{n-p}\left\|\mathbf{y}-X \hat{\boldsymbol{\beta}}_{P B S}(\mathbf{y})\right\|_{2}^{2}$. Using the above estimators, the $100(1-\alpha)$ $\%$ prediction interval of $y_{\text {new }}$ is derived as follows:

$$
\hat{\mu}_{P B S}(\mathbf{y}) \pm z_{\alpha / 2} \sqrt{\hat{V}\left(\hat{\mu}_{P B S}(\mathbf{y})\right)+\frac{1}{n-p}\left\|\mathbf{y}-X \hat{\boldsymbol{\beta}}_{P B S}(\mathbf{y})\right\|_{2}^{2}}
$$

where $z_{\alpha / 2}$ is the $100\left(1-\frac{\alpha}{2}\right)$ th percentile of the standard normal distribution.

## 3 Effect of resampling distribution parameters on prediction accuracy

### 3.1 Application of parametric bootstrap smoothing to electricity demand data

We applied parametric bootstrap smoothing to the Tokyo electricity demand data and verified the validity of the prediction accuracy. The source of this data is https://www.tepco.co.jp/ forecast/html/download-j.html.



Figure 3.1 : Electricity demand data (hourly)

Let $y_{i j}$ be electricity demand at $j: 00$ on day $i(j=1, \ldots, 24)$. We use a regression model with the temperature information proposed by Hirose 2021]. The source of the temperature information is https://www.data.jma.go.jp/gmd/risk/obsdl/index.php. Specifically, the following model was considered:

$$
y_{i j}=\sum_{t=1}^{T} \alpha_{j t} y_{(i-t) j}+\sum_{m=1}^{M} \sum_{q=1}^{Q} \gamma_{q m} h_{q}(j) g_{m}\left(s_{i}\right)+\varepsilon_{i j} \quad \varepsilon_{i j} \sim N\left(0, \sigma^{2}\right)
$$

where $s_{i}$ is the average temperature on day $i ; h_{q}(j)$ is the cyclic B-spline basis function; and $g_{m}\left(s_{i}\right)$ is the B-spline basis function. The estimated regression coefficients are $\alpha_{j t}$ and $\gamma_{q m}$ (hereafter, the regression coefficients are collectively written as $\boldsymbol{\beta}$ ). The following experiments are conducted using this model.

[Experiment overview]

- Four candidate models are prepared by changing the number of B-spline bases. The dimensions $p$ of $\boldsymbol{\beta}$ in each model are 121, 146, 146, 196, respectively.
- The estimate $\hat{\boldsymbol{\beta}}$ is computed by ridge regression Hoerl and Kennard 1970 to make a prediction. The model and regularization parameter $\lambda$ are selected by generalized cross-validation, respectively. The prediction interval is derived by regarding $V(\hat{\boldsymbol{\beta}})=\sigma^{2}\left(X^{T} X+\lambda I_{p}\right)^{-1} X^{T} X\left(X^{T} X+\right.$ $\left.\lambda I_{p}\right)^{-1}$, without considering the randomness of the model selection.
- The parametric bootstrap smoothing is applied to the above ridge regression. Here, bootstrap sample size $B$ is 500 , and $\hat{\sigma}^{2}$, which is in step 1 of the parametric bootstrap smoothing procedure introduced in Section 2.1, is determined as $\hat{\sigma}_{U B}^{2}:=\frac{1}{n-p}\left\|\mathbf{y}-X \hat{\boldsymbol{\beta}}_{O L S}\right\|_{2}^{2}$.
- The prediction values and the prediction intervals of $y_{i 1}, \ldots, y_{i 24}$ are computed for each day $i=1, \ldots, 365(1 / 4 / 2019 \sim 31 / 3 / 2020)$. The training data used in this prediction is the last 15 days of the data which are on the same day of the week as the prediction date $i$. Then, we compared the prediction accuracy between ridge regression and parametric bootstrap smoothing.

Table 3.1 compares the prediction and prediction intervals for accuracy between ridge regression and parametric bootstrap smoothing. The results show that although the prediction accuracy was improved, the prediction interval did not improve, but rather worsened. However, we conducted further experiments and found that the accuracy varied significantly depending on the choice of $\hat{\sigma}^{2}$ used for resampling in the parametric bootstrap smoothing.

### 3.2 Experiments comparing the prediction accuracy for each different $\hat{\sigma}^{2}$

In Section 3.1 , we chose $\hat{\sigma}^{2}$ as $\hat{\sigma}_{U B}^{2}=\frac{1}{n-p}\left\|\mathbf{y}-X \hat{\boldsymbol{\beta}}_{O L S}\right\|_{2}^{2}$; but in this Section, we give $\hat{\sigma}^{2}$ in advance and conduct the same experiment as in Section 3.1 to test the affect of the choice of $\hat{\sigma}^{2}$. The choice

Table 3.1 : Comparison of two methods

|  | Ridge regression | Parametric bootstrap smoothing |
| :--- | :---: | :---: |
| Mean-squared prediction error | 147051.5 | 126762.8 |
| Percentage of observed values included <br> in prediction interval | $72.8 \%$ | $70.7 \%$ |

of $\hat{\sigma}^{2}$ varies as $\hat{\sigma}^{2}=50^{2}, 100^{2}, \ldots, 800^{2}$. Figure 3.2 and 3.3 show the mean squared prediction error and percentage of observed values included in the prediction interval, respectively. The results show that the choice of $\hat{\sigma}^{2}$ has a significant effect on prediction accuracy. In particular, for some variance values, the prediction accuracy was significantly improved over choosing the variance $\hat{\sigma}_{U B}^{2}$.



Figure 3.2 : Mean-squared prediction error



Figure 3.3 : Percentage of observed values included in prediction interval

### 3.3 Choosing of resampling distribution by cross-validation

We have evaluated the effect of the choice of $\hat{\sigma}^{2}$. Now, we also focus on the mean vector. Specifically, we consider resampling from the following distribution:

$$
N\left(\hat{\gamma} X \hat{\boldsymbol{\beta}}_{O L S}+(1-\hat{\gamma}) \mathbf{y}, \hat{\sigma}^{2} I_{n}\right), \text { where } 0 \leq \hat{\gamma} \leq 1
$$

The properties of this mean vector are discussed in Section 4

We aim to find $\hat{\sigma}^{2}$ and $\hat{\gamma}$, and choose a resampling distribution with better accuracy than the distribution based on OLS estimation. Here, we propose a method for choosing $\hat{\sigma}^{2}$ and $\hat{\gamma}$ using cross validation, as follows:

1. Split $\mathbf{y}$ into $K$ pairs, and let $\mathbf{y}=\left(\mathbf{y}_{(1)}^{T}, \ldots, \mathbf{y}_{(K)}^{T}\right)^{T}$.
2. Give $\hat{\sigma}^{2}$ and $\hat{\gamma}$ candidates as $\bar{\sigma}_{1}^{2}, \ldots, \bar{\sigma}_{T}^{2}$ and $\bar{\gamma}_{1}, \ldots, \bar{\gamma}_{S}$.
3. The parametric bootstrap smoothing with $\mathbf{y}^{(k)}$ is conducted to compute $\hat{\mu}_{P B S}\left(\mathbf{y}^{(k)}, \bar{\sigma}_{i}^{2}, \bar{\gamma}_{j}\right)$, which is the prediction of $\mathbf{y}_{(k)}$, for each $\bar{\sigma}_{i}^{2}, \bar{\gamma}_{j}$, and $k$. Here, $\mathbf{y}^{(k)}$ is $\mathbf{y}$ with $\mathbf{y}_{(k)}$ removed. Bootstrap samples are generated from $N\left(\bar{\gamma}_{j} X^{(k)} \hat{\boldsymbol{\beta}}_{O L S}+\left(1-\bar{\gamma}_{j}\right) \mathbf{y}^{(k)}, \bar{\sigma}_{i}^{2} I_{n^{(k)}}\right)$, where $X^{(k)}$ denotes the submatrix of $X$ corresponding to $\mathbf{y}^{(k)}$, and $n^{(k)}$ denotes the dimension of $\mathbf{y}^{(k)}$.
4. Choose $\hat{\sigma}^{2}$ and $\hat{\gamma}$ as follows:

$$
\left(\hat{\sigma}^{2}, \hat{\gamma}\right)=\underset{\bar{\sigma}_{i}^{2}, \bar{\gamma}_{j}}{\arg \min } \sum_{k=1}^{K}\left\|\mathbf{y}_{(k)}-\hat{\mu}_{P B S}\left(\mathbf{y}^{(k)}, \bar{\sigma}_{i}^{2}, \bar{\gamma}_{j}\right)\right\|_{2}^{2}
$$

and the parametric bootstrap smoothing using chosen $\hat{\sigma}^{2}$ and $\hat{\gamma}$ is conducted.

When computing the prediction interval, $V\left(\hat{\mu}_{P B S}(\mathbf{y})\right)$ is estimated as

$$
\hat{V}\left(\hat{\mu}_{P B S}(\mathbf{y})\right):=\frac{1}{\hat{\sigma}^{2}} \widehat{\operatorname{Cov}}^{T}\left\{\hat{\gamma} X\left(X^{T} X\right)^{-1} X^{T}+(1-\hat{\gamma}) I_{n}\right\}^{2} \widehat{\operatorname{Cov}}
$$

where $\widehat{C o v}:=\frac{1}{B} \sum_{b=1}^{B}\left(\hat{\mu}\left(\mathbf{y}_{b}^{*}\right)-\hat{\mu}_{P B S}(\mathbf{y})\right)\left(\mathbf{y}_{b}^{*}-\overline{\mathbf{y}}^{*}\right)$. As in 2.3 , we derive this estimator using the delta method. We conducted the same experiment as that in Section 3.1 using this method. The number of candidates for $\hat{\sigma}^{2}$ and $\hat{\gamma}$ is 50 and 6 , respectively, and the bootstrap sample size is 500. The data used for the prediction were changed over 15,20,25, and 30 days (sample sizes $n=360,480,600,720)$. Figures 3.4 and 3.5 show the mean squared prediction error and percentage of observed values included in the predicted interval for each sample size, respectively. In addition to the ridge regression and the proposed method, a method that selects only $\hat{\sigma}^{2}$ by crossvalidation was also compared (i.e., fixed $\hat{\gamma}=1$ ). The results showed that the proposed method gave the best results, independent of the sample size. It was found to be particularly effective compared with ridge regression when the sample size was small.



Figure 3.4 : Mean-squared prediction error



Figure 3.5: Percentage of observed values included in prediction interval

## 4 Simulation study

In this Section, we discuss, through simulation, why some choices of $\hat{\sigma}^{2}$ provide better prediction accuracy than $\hat{\sigma}_{U B}^{2}$. We also consider changing the mean vector and its effect on prediction accuracy. First, random numbers were independently generated from a uniform distribution $U(-5,5)$ to create an $n \times 20$ design matrix $X$. Subsequently, we considered four models. The $j$ th model is as follows:

$$
\mathbf{y}=\mathbf{1}_{n}+X \boldsymbol{\beta}_{j}+\boldsymbol{\varepsilon}, \quad \boldsymbol{\varepsilon} \sim N\left(0,5^{2} I_{n}\right)
$$

where $\boldsymbol{\beta}_{j}=\left(\mathbf{1}_{5 j}^{T}, \mathbf{0}_{20-5 j}^{T}\right)^{T}$ for $j=1,2,3,4$, and $\mathbf{1}_{m}, \mathbf{0}_{m}$ denote $m \times 1$ vectors with $\mathbf{1}_{m}=(1, \ldots, 1)^{T}$, $\mathbf{0}_{m}=(0, \ldots, 0)^{T}$. In the simulation, $\mathbf{y}$ was generated from one of the four different models and a similar experiment to that in Section 3.2. Here, we consider resampling from 3.2 and varying the mean vector in addition to $\hat{\sigma}^{2}$.

Remark 4.1. Let $\mathbf{y}^{*}=\hat{\gamma} X \hat{\boldsymbol{\beta}}_{O L S}+(1-\hat{\gamma}) \mathbf{y}+\varepsilon^{*}$ be the bootstrap sample generated from 3.2 . The ridge estimator based on model $j$ can then be computed as follows:

$$
\left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1} X_{j}^{T} \mathbf{y}^{*}=\left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1} X_{j}^{T}\left(\hat{\gamma} X \hat{\boldsymbol{\beta}}_{O L S}+(1-\hat{\gamma}) \mathbf{y}+\varepsilon^{*}\right)
$$

where $X_{j}$ denotes $n \times 5 j$ design matrix in model $j$ with $X_{j}:=X\left(I_{5 j}, 0\right)^{T}$. Here, since

$$
\begin{aligned}
& \left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1} X_{j}^{T} X \hat{\boldsymbol{\beta}}_{O L S} \\
& =\left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1}\left(I_{5 j}, 0\right) X^{T} X\left(X^{T} X\right)^{-1} X^{T} \mathbf{y}=\left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1} X_{j}^{T} \mathbf{y}
\end{aligned}
$$

it holds that $\left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1} X_{j}^{T} \mathbf{y}^{*}=\left(X_{j}^{T} X_{j}+\lambda I_{5 j}\right)^{-1} X_{j}^{T}\left(\mathbf{y}+\varepsilon^{*}\right)$. That is, $\hat{\gamma}$ does not affect the ridge estimation itself for any bootstrap sample. Therefore, the twice-shrinking noted in Section 7A of Efron 2014 can be avoided. For each bootstrap sample, $\hat{\gamma}$ is only related to the results of model and $\lambda$ selection by cross-validation. In particular, when $\hat{\gamma}$ is large, the mean vector is close to $X \hat{\boldsymbol{\beta}}_{\text {OLS }}$. Therefore, the full model is more likely to be selected for cross-validation. Thus, $\hat{\gamma}$ would be interpreted as a measure of the trust of the prepared full model.

The choices of $\hat{\sigma}^{2}$ and $\hat{\gamma}$ varied as $\hat{\sigma}^{2}=1^{2}, 1.2^{2}, 1.4^{2}, \ldots, 10^{2}$ and $\hat{\gamma}=0,0.2,0.5,1$, respectively. This simulation was repeated 1000 times to evaluate the accuracy of the estimation of $\boldsymbol{\beta}_{j}$ and the constant term. Figures 4.1 and 4.2 show the results for $n=30$ and 40 , respectively (the results for $n>40$ are similar to those of $n=40$ ). Column $j$ of the figure shows the results when the true model is $j$. The top figure compares the mean squared estimation errors, and the four figures below show the percentage of each model selected in parametric bootstrap smoothing for each $\hat{\gamma}$. The results of MSE show that the optimal $\hat{\sigma}^{2}$ depends on $n$, $\hat{\gamma}$, and the true model. In addition, compared to ridge estimation, parametric bootstrap smoothing is more effective when $n$ is small. We find that the mixing ratio of the model selection varies significantly, depending on $\hat{\sigma}^{2}$ and $\hat{\gamma}$. In particular, $\hat{\gamma}$ has a significant influence on the probability of selecting the full model. However, when $\hat{\sigma}^{2}$ is large, the mixing ratio is similar, regardless of $\hat{\gamma}$. Note that a high probability of selecting the true model does not necessarily lead to optimal prediction accuracy. For example, looking at the results for the case in which the true model is Model 4, it seems that a smaller $\hat{\sigma}^{2}$ is optimal in terms of the probability that Model 4 is selected, but not in terms of MSE. This fact would be because $\hat{\sigma}^{2}$ and $\hat{\gamma}$ affect not only the ratio of model selection but also the ratio of the selection of the regularization parameter $\lambda$. For example, considering the case $\hat{\sigma}^{2}=0$ and $\hat{\gamma}=1$, the bootstrap sample is always $X \hat{\boldsymbol{\beta}}_{O L S}$, thus the full model is always selected, but the $\lambda$ is also always 0. Consequently, $\hat{\boldsymbol{\beta}}_{P B S}=\hat{\boldsymbol{\beta}}_{O L S}$ and the variance in $\hat{\boldsymbol{\beta}}_{P B S}$ increases.

As mentioned above, the optimal $\hat{\sigma}^{2}$ varies complexly by various factors, and it is not always the true variance, which may be the reason why some choices of $\hat{\sigma}^{2}$ provide better prediction accuracy than $\hat{\sigma}_{U B}^{2}$, which is an unbiased estimator of $\sigma^{2}$. Additionally, it is not always optimal to set the mean vector to $X \hat{\boldsymbol{\beta}}_{O L S}(\hat{\gamma}=1)$. Overall, it may be better not to determine a resampling distribution based on model estimation.


Figure 4.1: Mean-squared error of estimation and percentage of each model selected in $n=30$


Figure 4.2 : Mean-squared error of estimation and percentage of each model selected in $n=40$

## 5 Concluding remarks

We performed a Monte Carlo simulation and electricity demand prediction to investigate the effectiveness of parametric bootstrap smoothing. The results show that the choice of variance $\hat{\sigma}^{2}$ when generating bootstrap samples has a significant effect on prediction accuracy. In particular, we found that true variance does not always provide optimal prediction accuracy. We focused on this and the mean vector, and then proposed a method to conduct parametric bootstrap smoothing with a resampling distribution chosen by cross-validation. In our simulation, the proposed method showed better prediction accuracy than the method using a resampling distribution based on OLS estimation.

In future studies, we will consider developing a faster method. The proposed method requires $K \times T \times S$ times parametric bootstrap smoothing, which is computationally expensive. Here, $K$ is the number of data splits in the cross-validation and $T$ and $S$ are the numbers of $\hat{\sigma}^{2}$ and $\hat{\gamma}$ candidates, respectively. We will also consider researching how the $\hat{\sigma}$ and mean vector selected by cross-validation are related to the true $\sigma$ and mean vector.

## Acknowledgments

This work was supported by JSPS KAKENHI Grant Numbers JP22J20435 (W.Y.), JP23K11007, JP23K01333, JP23H04474, JP23H00466, and JP22H01139 (K.H.), WISE program (MEXT) at Kyushu University, and JST-Mirai Program Grant Number JPMJMI18A2.

## References

Hirotugu Akaike. A new look at the statistical model identification. IEEE transactions on automatic control, 19(6):716-723, 1974.

Leo Breiman. Bagging predictors. Machine learning, 24(2):123-140, 1996.

Bradley Efron. Estimation and accuracy after model selection. Journal of the American Statistical Association, 109(507):991-1007, 2014.

Kei Hirose. Interpretable modeling for short-and medium-term electricity demand forecasting. Frontiers in Energy Research, 9:724780, 2021.

Arthur E Hoerl and Robert W Kennard. Ridge regression: Biased estimation for nonorthogonal problems. Technometrics, 12(1):55-67, 1970.

Jason D Lee, Dennis L Sun, Yuekai Sun, and Jonathan E Taylor. Exact post-selection inference, with application to the lasso. The Annals of Statistics, 44(3):907-927, 2016.

James G MacKinnon. Bootstrap methods in econometrics. Economic Record, 82:S2-S18, 2006.

Mervyn Stone. Cross-validatory choice and assessment of statistical predictions. Journal of the royal statistical society: Series B (Methodological), 36(2):111-133, 1974.

Jonathan Taylor and Robert J Tibshirani. Statistical learning and selective inference. Proceedings of the National Academy of Sciences, 112(25):7629-7634, 2015.

