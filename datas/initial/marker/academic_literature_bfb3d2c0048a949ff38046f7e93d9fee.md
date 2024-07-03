# Improving Prediction Accuracy By Choosing Resampling Distribution Via Cross-Validation Wataru Yoshida And Kei Hirose Kyushu University

## Abstract

In a regression model, prediction is typically performed after model selection. The large variability in the model selection makes the prediction unstable. Thus, it is essential to reduce the variability in model selection and improve prediction accuracy. To achieve this goal, a parametric bootstrap smoothing can be applied. In this method, model selection is performed for each resampling from a parametric distribution, and these models are then averaged such that the distribution of the selected models is considered. Here, the prediction accuracy is highly dependent on the choice of a distribution for resampling. In particular, an experimental study shows that the choice of error variance significantly changes the distribution of the selected model and thus plays a key role in improving the prediction accuracy. We also observed that the true error variance does not always provide optimal prediction accuracy. Therefore, it would not always be appropriate to use unbiased estimators of the true parameters or standard estimators of the parameters for the resampling distribution. In this study, we propose employing cross validation to choose a suitable resampling distribution rather than unbiased estimators of parameters. Our proposed method was applied to electricity demand data. The results indicate that the proposed method provides a better prediction accuracy than the existing method.

## 1 Introduction

In regression modeling, estimation and prediction are typically performed after model selection. Reducing the variability in model selection is essential for achieving high accuracy. In addition, this variability should be considered when creating confidence or prediction intervals. The problem of appropriately handling the uncertainty caused by the model selection process is called selective inference [Taylor and Tibshirani 2015]. For example, the selective inference in lasso estimation is researched by Lee et al. [2016].

To reduce variability in model selection and improve prediction accuracy, we may use parametric bootstrap smoothing. Parametric bootstrap smoothing performs model selection for each resampling from a parametric distribution, and these models are averaged such that the distribution of the selected models is considered. Thus, this method is expected to reduce the variability in model selection and improve prediction accuracy. A similar smoothing method using nonparametric bootstrapping is well-known in the field of machine learning under the name of bagging [Breiman 1996]. For these smoothing methods, Efron [2014] proposed a formula for computing the standard errors of the estimators. Using this formula, we can construct the prediction interval in parametric bootstrap smoothing.

2 Suppose a sample follows the regression model N(Xβ, σ2In). To apply parametric bootstrap smoothing to estimate β, the distribution for resampling must be set. A general approach is to choose N(XβˆOLS, σˆ
2 UB) as the resampling distribution [MacKinnon 2006]. Here, βˆOLS and σˆ
2 UB denote the ordinary least squares (OLS) estimator of the coefficient vector and the unbiased estimator of the variance based on βˆOLS, respectively. However, in this study, we found that some distributions significantly outperform those based on OLS in terms of predictive accuracy. In fact, our simulation shows that the choice of error variance changes the distribution of the selected model and thus significantly affects prediction accuracy. We also discovered that choosing the true σ 2for the resampling distribution did not always provide the optimal prediction accuracy. This suggests that it is inappropriate to use ˆσ 2 UB for the resampling distribution, even though ˆσ 2 UB is an unbiased estimator of the true variance. In addition, our simulation shows that it may not be optimal to set the mean vector to XβˆOLS, especially when the true model is not full model. Therefore, we propose a method for choosing the resampling distribution by cross-validation, rather than model estimation. The proposed method searches for a distribution that specializes in improving the prediction of parametric bootstrap smoothing, whereas the existing methods select a distribution that fits the data. The proposed method is applied to predict the electricity demand. The results indicate that the proposed method provides better prediction accuracy than the existing methods.

The remainder of this paper is organized as follows. In Section 2, we introduce the prediction and the prediction interval construction using parametric bootstrap smoothing. In Section 3, we show the effect of the choice of the resampling distribution on the prediction accuracy from the experimental results of applying it to electricity demand data. Then, we propose a method for choosing a resampling distribution by cross-validation and show the results of an actual application to electricity demand data. In Section 4, we discuss through simulation why some choices of distribution provide better prediction accuracy than OLS-based distribution. In the simulation, the variance and mean vector of a resampling distribution were varied, and the prediction error and distribution of the selected models were examined. Finally, the conclusions are presented in Section 5.

## 2 Prediction Using Parametric Bootstrap Smoothing 2.1 Parametric Bootstrap Smoothing

Let y = (y1*, . . . , y*n)
T be the vector of n observations. We assume that y follows the linear regression model:

$$\mathbf{y}=X{\boldsymbol{\beta}}+{\boldsymbol{\varepsilon}},\quad{\boldsymbol{\varepsilon}}\sim N\left(0,\sigma^{2}I_{n}\right),$$
$$(2.1)$$
, (2.1)
where X is an n × p design matrix with X := (x1*, . . . ,* xn)
T and β is a p × 1 regression coefficient vector. Now, assume that we obtain xnew, and ynew follows the linear regression model:

$$y_{n e w}={\bf x}_{n e w}^{T}\beta+\varepsilon_{n e w},\quad\varepsilon_{n e w}\sim N\left(0,\sigma^{2}\right).$$

Our aim is to obtain the prediction value and prediction interval of ynew. We derive βˆ, the estimator of β and predict ynew as ˆµ(y) := x Tnewβˆ. Model selection is conducted to derive βˆ. For example, cross-validation [Stone 1974], AIC [Akaike 1974], and sparse estimation can be considered. If n is not sufficiently large for p, the model selection is unstable, and the prediction value of ynew is also unstable. To address this problem, we use parametric bootstrap smoothing (see, for example,
[Efron 2014]):
1. Compute βˆOLS = (XT X)
−1XT y and ˆσ 2that is an estimate of σ 2.

2. Generate bootstrap sample y
∗
1
, . . . , y
∗
B
, where y
∗
i ∼ N(XβˆOLS, σˆ
2In) for i = 1*, . . . , B*.

3. Derive βˆ(y
∗
1
),. . . , βˆ(y
∗
B
) that are estimates of β from each bootstrap sample y
∗
i
.

4. Compute the mean of estimates as βˆ*P BS*(y) := 1B
PB
b=1 βˆ(y
∗
b
), and we get the prediction of ynew as follows:
$$\hat{\mu}_{P B S}(\mathbf{y}):=x_{n e w}^{T}\hat{\boldsymbol{\theta}}_{P B S}(\mathbf{y}).$$
$\left(2.2\right)^{2}$
newβˆ*P BS*(y). (2.2)
In Step 3, note that the result of the model selection varies with each bootstrap sampling, that is, even if βˆk(y
∗
i
) = 0, it may be βˆk(y
∗
j
) ̸= 0 (i ̸= j). Here, βˆl(y
∗m) denotes lth component of βˆ(y
∗m).

In Step 4, the randomness of model selection is smoothed.

## 2.2 Prediction Interval

We consider a 100(1−α) % prediction interval for ynew similar to the confidence interval derivation process proposed by Efron [2014]. First, the estimator of V (ˆµ*P BS*(y)) is derived by using the delta method as follows:

$$\hat{V}(\widehat{\mu}_{P B S}({\bf y})):=\frac{1}{\widehat{\sigma}^{2}}\widehat{C o v}^{T}(X^{T}X)^{-1}\widehat{C o v},$$
−1*Cov,* d (2.3)
$$(2.3)$$

where

$${\widetilde{C o v}}:={\frac{1}{B}}\sum_{b=1}^{B}({\hat{\mu}}({\bf y}_{b}^{*})-{\hat{\mu}}_{P B S}({\bf y}))(X^{T}{\bf y}_{b}^{*}-X^{T}{\bf\hat{y}}^{*}),\quad{\bar{\bf y}}^{*}:={\frac{1}{B}}\sum_{b=1}^{B}{\bf y}_{b}^{*},\ {\hat{\mu}}({\bf y}_{b}^{*}):=x_{n e v}^{T}{\hat{\beta}}({\bf y}_{b}^{*}).$$

Next, V(Enew) is estimated as m = p ||y - X P BS (y) || 2 . Using the above estimators, the 100(1 - a)
% prediction interval of ynew is derived as follows:

$${\hat{\mu}}_{P B S}(\mathbf{y})\pm z_{\alpha/2}{\sqrt{{\hat{V}}({\hat{\mu}}_{P B S}(\mathbf{y}))+{\frac{1}{n-p}}\|\mathbf{y}-X{\hat{\beta}}_{P B S}(\mathbf{y})\|_{2}^{2}}},$$
$$\quad(2.4)$$

where za/2 is the 100(1 - §)th percentile of the standard normal distribution.

## 3 Effect Of Resampling Distribution Parameters On Prediction Accuracy Application Of Parametric Bootstrap Smoothing To Electricity 3.1 Demand Data

We applied parametric bootstrap smoothing to the Tokyo electricity demand data and verified the validity of the prediction accuracy. The source of this data is https://www.tepco.co.jp/ forecast/html/download-j.html .

![3_image_0.png](3_image_0.png)

![3_image_1.png](3_image_1.png)

Let yij be electricity demand at j : 00 on day i (j = 1*, . . . ,* 24). We use a regression model with the temperature information proposed by Hirose [2021]. The source of the temperature information is https://www.data.jma.go.jp/gmd/risk/obsdl/index.php. Specifically, the following model was considered:

$$y_{ij}=\sum_{t=1}^{T}\alpha_{ijt}y_{(i-t)j}+\sum_{m=1}^{M}\sum_{q=1}^{Q}\gamma_{qm}h_{q}(j)g_{m}(s_{i})+\varepsilon_{ij}\ \ \ \ \ \varepsilon_{ij}\sim N(0,\sigma^{2}),\tag{3.1}$$  where $s_{i}$ is the average temperature on day $i$; $h_{q}(j)$ is the cyclic B-spline basis function; and $g_{m}(s_{i})$
is the B-spline basis function. The estimated regression coefficients are αjt and γqm (hereafter, the regression coefficients are collectively written as β). The following experiments are conducted using this model.

[Experiment overview]

- Four candidate models are prepared by changing the number of B-spline bases. The dimensions p of β in each model are 121, 146, 146, 196, respectively.

- The estimate βˆ is computed by ridge regression [Hoerl and Kennard 1970] to make a prediction. The model and regularization parameter λ are selected by generalized cross-validation, respectively. The prediction interval is derived by regarding V (βˆ) = σ 2(XT X+λIp)
−1XT X(XT X+
λIp)
−1, without considering the randomness of the model selection.

- The parametric bootstrap smoothing is applied to the above ridge regression. Here, bootstrap sample size B is 500, and ˆσ 2, which is in step 1 of the parametric bootstrap smoothing procedure introduced in Section 2.1, is determined as ˆσ 2 UB := 1 n−p
∥y − XβˆOLS∥
22
.

- The prediction values and the prediction intervals of yi1*, . . . , y*i24 are computed for each day i = 1*, . . . ,* 365 (1/4/2019∼31/3/2020). The training data used in this prediction is the last 15 days of the data which are on the same day of the week as the prediction date i. Then, we compared the prediction accuracy between ridge regression and parametric bootstrap smoothing.
Table 3.1 compares the prediction and prediction intervals for accuracy between ridge regression and parametric bootstrap smoothing. The results show that although the prediction accuracy was improved, the prediction interval did not improve, but rather worsened. However, we conducted further experiments and found that the accuracy varied significantly depending on the choice of ˆσ 2 used for resampling in the parametric bootstrap smoothing.

## 3.2 Experiments Comparing The Prediction Accuracy For Each Different Σˆ 2

In Section 3.1, we chose ˆσ 2 as ˆσ 2 UB =1 n−p
∥y − XβˆOLS∥
22
; but in this Section, we give ˆσ 2in advance and conduct the same experiment as in Section 3.1 to test the affect of the choice of ˆσ 2. The choice

| Table 3.1 : Comparison of two methods   |                                |          |
|-----------------------------------------|--------------------------------|----------|
| Ridge regression |                      | Parametric bootstrap smoothing |          |
| Mean-squared prediction error           | 147051.5                       | 126762.8 |
| Percentage of observed values included  | 72.8%                          | 70.7%    |
| in prediction interval                  |                                |          |

of 6 2 varies as 6 2 = 50 2 , 100 2 , . . , 800 2 . Figure 3.2 and 3.3 show the mean squared prediction

![5_image_0.png](5_image_0.png)

![6_image_0.png](6_image_0.png)

## 3.3 Choosing Of Resampling Distribution By Cross-Validation

We have evaluated the effect of the choice of ∂ 2 .  Now, we also focus on the mean vector.  Specifically, we consider resampling from the following distribution:

$$N\Bigl(\hat{\gamma}X\hat{\beta}_{O L S}+(1-\hat{\gamma}){\bf y},\hat{\sigma}^{2}I_{n}\Bigr),\mathrm{~where~}0\leq\hat{\gamma}\leq1.$$
$$(3.2)$$

The properties of this mean vector are discussed in Section 4.

We aim to find o 2 and o 2 and choose a resampling distribution with better accuracy than the distribution based on OLS estimation. Here, we propose a method for choosing ∂ 2 and ˆ γ using cross validation, as follows:
1. Split y into K pairs, and let y = ( y f 1 ), ..., y f K )) T .

2. Give 6 2 and 7 candidates as 6 2 , ..., 6 2 and 7 1 , ..., 7 s-

3. The parametric bootstrap smoothing with y(k) is conducted to compute fipbs(y(k), a?, fij),
which is the prediction of y(k), for each a 2 , fj, and k. Here, y(k) is y with y(k) removed.

Bootstrap samples are generated from N(7jX(k)BOLS + (1 - 7j)y(k), a 2 I n(k) ), where X(k)
denotes the submatrix of X corresponding to y ( k ), and n ( k ) denotes the dimension of y ( k ),
4. Choose ∂ 2 and ˆ γ as follows:

$$(\hat{\sigma}^{2},\ \hat{\gamma})=\arg\operatorname*{min}_{\bar{\sigma}_{i}^{2},\ \bar{\gamma}_{j}}\sum_{k=1}^{K}\|\mathbf{y}_{(k)}-\hat{\mu}_{P B S}(\mathbf{y}^{(k)},\bar{\sigma}_{i}^{2},\bar{\gamma}_{j})\|_{2}^{2},$$

and the parametric bootstrap smoothing using chosen 6 2 and 7 is conducted.

When computing the prediction interval, V(fipbs(y)) is estimated as

$$\hat{V}(\hat{\mu}_{PBS}({\bf y})):=\frac{1}{\hat{\sigma}^{2}}\widehat{Cov}^{T}\{\hat{\gamma}X(X^{T}X)^{-1}X^{T}+(1-\hat{\gamma})I_{n}\}^{2}\widehat{Cov},\tag{3.3}$$

where Cov := b L B 1 ( R ( y i ) - ppbs(y))(y i - y *). As in ( 2.3 ), we derive this estimator using the delta method. We conducted the same experiment as that in Section 3.1 using this method. The number of candidates for 6 2 and 7 is 50 and 6, respectively, and the bootstrap sample size is 500. The data used for the prediction were changed over 15, 20, 25, and 30 days (sample sizes n = 360,480,600,720). Figures  3.4  and  3.5  show the mean squared prediction error and percentage of observed values included in the predicted interval for each sample size, respectively. In addition to the ridge regression and the proposed method, a method that selects only ∂ 2 by crossvalidation was also compared (i.e., fixed f = 1). The results showed that the proposed method gave the best results, independent of the sample size. It was found to be particularly effective compared with ridge regression when the sample size was small.

![7_image_0.png](7_image_0.png)

![8_image_0.png](8_image_0.png)

## Simulation Study 4

In this Section, we discuss, through simulation, why some choices of ∂ 2 provide better prediction accuracy than ∂ T H .  We also consider changing the mean vector and its effect on prediction accuracy.

First, random numbers were independently generated from a uniform distribution U ( − 5 , 5 ) to create an n x 20 design matrix X . Subsequently, we considered four models. The j th model is as follows:
y = 1 n + X β j + ε,    ε ~ N (0 , 5 2 I n ) ,
where β j = (1 , , 0 ,
0 m = (0,...,0) T . In the simulation, y was generated from one of the four different models and a similar experiment to that in Section 3.2. Here, we consider resampling from ( 3.2 ) and varying the mean vector in addition to ∂ 2 .

Remark 4.1. Let y* = ~X ~ OLS + (1 - ~)y + e* be the bootstrap sample generated from ( 3.2 ).

The ridge estimator based on model j can then be computed as follows:
(X j x j + x I sj ) − 1 x j y* = (X j x j + x I sj ) − 1 x j ( j x β o l s + (1 − j ) y + e*),
where Xj denotes n × 5j design matrix in model j with Xj := X(Isj,0) T . Here, since
(Xf Xj + XI5j)-1 Xf X βols
= (X T X j + XI 5j ) − 1 (I 5j , 0) X T X(X T X) − 1 XT y = (X T X j + xI 5j ) − 1 XT y,

it holds that (XT
j Xj + λI5j )
−1XT
j y
∗ = (XT
j Xj + λI5j )
−1XT
j
(y + ε
∗). That is, ˆγ does not affect the ridge estimation itself for any bootstrap sample. Therefore, the twice-shrinking noted in Section 7A of [Efron 2014] can be avoided. For each bootstrap sample, ˆγ is only related to the results of model and λ selection by cross-validation. In particular, when ˆγ is large, the mean vector is close to XβˆOLS. Therefore, the full model is more likely to be selected for cross-validation. Thus, ˆγ would be interpreted as a measure of the trust of the prepared full model.

The choices of ˆσ 2 and ˆγ varied as ˆσ 2 = 12, 1.2 2, 1.4 2*, . . . ,* 102 and ˆγ = 0, 0.2, 0.5, 1, respectively.

This simulation was repeated 1000 times to evaluate the accuracy of the estimation of βj and the constant term. Figures 4.1 and 4.2 show the results for n = 30 and 40, respectively (the results for n > 40 are similar to those of n = 40). Column j of the figure shows the results when the true model is j. The top figure compares the mean squared estimation errors, and the four figures below show the percentage of each model selected in parametric bootstrap smoothing for each ˆγ. The results of MSE show that the optimal ˆσ 2 depends on n, ˆγ, and the true model. In addition, compared to ridge estimation, parametric bootstrap smoothing is more effective when n is small. We find that the mixing ratio of the model selection varies significantly, depending on ˆσ 2 and ˆγ. In particular, ˆγ has a significant influence on the probability of selecting the full model. However, when ˆσ 2is large, the mixing ratio is similar, regardless of ˆγ. Note that a high probability of selecting the true model does not necessarily lead to optimal prediction accuracy. For example, looking at the results for the case in which the true model is Model 4, it seems that a smaller ˆσ 2 is optimal in terms of the probability that Model 4 is selected, but not in terms of MSE. This fact would be because ˆσ 2 and ˆγ affect not only the ratio of model selection but also the ratio of the selection of the regularization parameter λ. For example, considering the case ˆσ 2 = 0 and ˆγ = 1, the bootstrap sample is always XβˆOLS, thus the full model is always selected, but the λ is also always 0. Consequently, βˆP BS = βˆOLS and the variance in βˆ*P BS* increases.

As mentioned above, the optimal ˆσ 2 varies complexly by various factors, and it is not always the true variance, which may be the reason why some choices of ˆσ 2 provide better prediction accuracy than ˆσ 2 UB, which is an unbiased estimator of σ 2. Additionally, it is not always optimal to set the mean vector to XβˆOLS (ˆγ = 1). Overall, it may be better not to determine a resampling distribution based on model estimation.

![10_image_0.png](10_image_0.png)

![11_image_0.png](11_image_0.png)

## 5 Concluding Remarks

We performed a Monte Carlo simulation and electricity demand prediction to investigate the effectiveness of parametric bootstrap smoothing. The results show that the choice of variance ˆσ 2 when generating bootstrap samples has a significant effect on prediction accuracy. In particular, we found that true variance does not always provide optimal prediction accuracy. We focused on this and the mean vector, and then proposed a method to conduct parametric bootstrap smoothing with a resampling distribution chosen by cross-validation. In our simulation, the proposed method showed better prediction accuracy than the method using a resampling distribution based on OLS estimation.

In future studies, we will consider developing a faster method. The proposed method requires K × T × S times parametric bootstrap smoothing, which is computationally expensive. Here, K is the number of data splits in the cross-validation and T and S are the numbers of ˆσ 2 and ˆγ candidates, respectively. We will also consider researching how the ˆσ and mean vector selected by cross-validation are related to the true σ and mean vector.

## Acknowledgments

This work was supported by JSPS KAKENHI Grant Numbers JP22J20435 (W.Y.), JP23K11007, JP23K01333, JP23H04474, JP23H00466, and JP22H01139 (K.H.), WISE program (MEXT) at Kyushu University, and JST-Mirai Program Grant Number JPMJMI18A2.

## References

Hirotugu Akaike. A new look at the statistical model identification. *IEEE transactions on automatic* control, 19(6):716–723, 1974.

Leo Breiman. Bagging predictors. *Machine learning*, 24(2):123–140, 1996.

Bradley Efron. Estimation and accuracy after model selection. *Journal of the American Statistical* Association, 109(507):991–1007, 2014.

Kei Hirose. Interpretable modeling for short-and medium-term electricity demand forecasting.

Frontiers in Energy Research, 9:724780, 2021.

Arthur E Hoerl and Robert W Kennard. Ridge regression: Biased estimation for nonorthogonal problems. *Technometrics*, 12(1):55–67, 1970.
Jason D Lee, Dennis L Sun, Yuekai Sun, and Jonathan E Taylor. Exact post-selection inference, with application to the lasso. *The Annals of Statistics*, 44(3):907–927, 2016.

James G MacKinnon. Bootstrap methods in econometrics. *Economic Record*, 82:S2–S18, 2006. Mervyn Stone. Cross-validatory choice and assessment of statistical predictions. *Journal of the* royal statistical society: Series B (Methodological), 36(2):111–133, 1974.

Jonathan Taylor and Robert J Tibshirani. Statistical learning and selective inference. *Proceedings* of the National Academy of Sciences, 112(25):7629–7634, 2015.