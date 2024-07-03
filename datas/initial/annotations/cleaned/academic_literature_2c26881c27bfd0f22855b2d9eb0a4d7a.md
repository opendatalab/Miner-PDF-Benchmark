# TRADE-OFF BETWEEN PREDICTIVE PERFORMANCE AND FDR CONTROL FOR HIGH-DIMENSIONAL GAUSSIAN MODEL SELECTION 

Perrine Lacroix<br>Laboratoire de Mathématiques d'Orsay, CNRS, Université Paris-Saclay, Orsay, France<br>Université Paris-Saclay, CNRS, INRAE, Université Evry, Institute of Plant Sciences Paris-Saclay (IPS2),<br>91190, Gif sur Yvette, France<br>Université Paris Cité, Institute of Plant Sciences Paris-Saclay (IPS2), 91190, Gif sur Yvette, France<br>perrine.lacroix@universite-paris-saclay.fr<br>Marie-Laure Martin<br>Université Paris-Saclay, AgroParisTech, INRAE, UMR MIA Paris-Saclay, 91120, Palaiseau, France<br>Université Paris-Saclay, CNRS, INRAE, Université Evry, Institute of Plant Sciences Paris-Saclay (IPS2),<br>91190, Gif sur Yvette, France<br>Université Paris Cité, Institute of Plant Sciences Paris-Saclay (IPS2), 91190, Gif sur Yvette, France<br>marie-laure.martin@inrae.fr


#### Abstract

In the context of the high-dimensional Gaussian linear regression for ordered variables, we study the variable selection procedure via the minimization of the penalized least-squares criterion. We focus on model selection where the penalty function depends on an unknown multiplicative constant commonly calibrated for prediction. We propose a new proper calibration of this hyperparameter to simultaneously control predictive risk and false discovery rate. We obtain non-asymptotic bounds on the False Discovery Rate with respect to the hyperparameter and we provide an algorithm to calibrate it. This algorithm is based on quantities that can typically be observed in real data applications. The algorithm is validated in an extensive simulation study and is compared with some existing variable selection procedures. Finally, we study an extension of our approach to the case in which an ordering of the variables is not available.


Keywords Ordered variable selection $\cdot$ Prediction $\cdot$ FDR $\cdot$ High-dimension $\cdot$ Gaussian regression $\cdot$ Hyperparameter calibration

## 1 Introduction.

### 1.1 Problem statement.

We consider the following high-dimensional univariate Gaussian linear regression model :

$$
Y=X \beta^{*}+\varepsilon
$$

The random response vector $Y=\left(\left(Y_{i}\right)_{\{1 \leq i \leq n\}}\right)^{T} \in \mathbb{R}^{n}$ is regressed on $p$ deterministic vectors : $X_{1}=$ $\left(\left(x_{i 1}\right)_{\{1 \leq i \leq n\}}\right)^{T}, \cdots, X_{p}=\left(\left(x_{i p}\right)_{\{1 \leq i \leq n\}}\right)^{T}$. The design matrix of size $n \times p$ is denoted by $X=\left(X_{1}, \cdots, X_{p}\right)$. The noise $\varepsilon=\left(\left(\varepsilon_{i}\right)_{\{1 \leq i \leq n\}}\right)^{T}$ is assumed to be Gaussian : $\varepsilon \sim \mathcal{N}\left(0, \sigma^{2} I_{n}\right)$ with $\sigma^{2}>0$. In the high-dimensional context, additional assumptions of regularity are required and we assume that $\beta^{*}$ is sparse, meaning that only a few coefficients are non-zero. In the following, a variable $X_{j}$ corresponding to a non-zero coefficient $\beta_{j}^{*}$ is called an active

Trade-off between prediction and FDR for variable selection

variable. Otherwise the variable is said to be non-active.

In this paper, we are interested in variable selection. We refer the reader to [1] and references therein. To the best of our knowledge, some variable selection procedures focus on the prediction of the response variable $Y$ through a control of the predictive risk. Others focus on limiting the number of selected non-active variables through a control of the False Discovery Rate. There also exists procedures where several cost functions are considered simultaneously. In the line of the latter, our goal is to identify a set of variables from a model selection procedure by limiting the selection of non-active variables while maintaining accurately prediction performances.

### 1.2 Related works.

In a variable selection procedure, a cost function has to be defined. The predictive risk (PR) and the False Discovery Rate (FDR) are the common used cost functions.

The penalized methods to control the predictive risk. The penalization procedure balances goodness of fit and sparsity : the smaller the penalty function, the better the fitting to the data but the higher the number of selected variables. In high-dimension, the most popular method is the Lasso criterion [2] where the estimator $\hat{\beta}_{\lambda}$ of $\beta^{*}$ is the solution of :

$$
\hat{\beta}_{\lambda}=\underset{\beta \in \mathbb{R}^{p}}{\arg \min }\left\{\|Y-X \beta\|_{2}^{2}+\lambda|\beta|_{1}\right\}
$$

where $|\cdot|_{1}$ and $\|\cdot\|_{2}$ design the $\ell_{1}$-norm and the euclidean norm of a vector respectively. The main challenge is to calibrate the hyperparameter $\lambda>0$. If $\lambda$ is chosen to be proportional to $\sigma \sqrt{\frac{\log (p)}{n}}$, then the predictive risk is bounded $[3,4]$. However, the noise being usually unknown, the choice of $\lambda$ remains tricky. Therefore, an alternative is to solve the Lasso criterion for a $\lambda$ within a reasonable interval by using subsamples [5] or resamples [6]. The selected variables are then defined as the variables with the highest selection frequencies. Such alternative is no longer sensitive to the choice of $\lambda$ but the main challenge lies in the threshold on the frequency defining the selected variables.

In this paper, we consider a model selection procedure composed of three steps. The first step consists in solving the Lasso criterion on a relevant grid $\Lambda$. Each $\lambda \in \Lambda$ defines a variable subset to get a collection $\mathcal{M}$ of relevant subsets of variables with a wide range of sizes. In the second step, the least-squares estimator onto each variable subset of $\mathcal{M}$ is calculated leading to a collection of estimators $\left(\hat{\beta}_{m}\right)_{m \in \mathcal{M}}$. Lastly, the following penalized least-squares minimization is solved to select the best $m$ of $\mathcal{M}$ :

$$
\hat{m}=\underset{m \in \mathcal{M}}{\arg \min }\left\{\left\|Y-X \hat{\beta}_{m}\right\|_{2}^{2}+\operatorname{pen}\left(D_{m}\right)\right\}
$$

where $D_{m}$ is the dimension of the model $m$ and the function pen is a penalty function increasing with $D_{m}$.

Selecting $\hat{m}$ from $\mathcal{M}$ by minimizing (1.3) corresponds to selecting $\hat{\lambda}$ from $\Lambda$ by minimizing (1.2). Hence, the main challenge is the definition of pen that achieves an optimal trade-off between goodness of fit and sparsity within $\mathcal{M}$. Popular methods of model selection include $V$-fold cross-validation [7, 8], AIC [9], Cp-Mallows [10], BIC [11] and eBIC [12]. For these penalty functions, the predictive risk is bounded when $\sigma^{2}$ is known and when the sample size $n$ tends to infinity. When $n$ is fixed, relatively small, and possibly smaller than the dimension $p$, a non-asymptotic point of view is preferable to get properties for all couples of $(n, p)$. In this direction, [13] propose some penalty functions depending on the collection complexity such that $\hat{m}$ guarantees non-asymptotic optimal control of the predictive risk. If the model collection is nested with a known variance, $\operatorname{pen}\left(D_{m}\right)=2 \sigma^{2} D_{m}$ allows to achieve an optimal non-asymptotic control of the predictive risk [9]. If the model collection is fixed and large (for instance with an exponential growth with $\left.D_{m}\right)$ and if the variance is unknown, this optimal control is obtained with data-driven penalties [13, 14]. Lastly, if the model collection is data-dependent and if the variance $\sigma^{2}$ is unknown, the LinSelect penalty $[15,16]$ guarantees an optimal control of the predictive risk.

The multiple testing methods to control the False Discovery Rate. In the multiple testing procedure, the $p$ tests $H_{0}=\left\{\beta_{j}^{*}=0\right\}$ versus $H_{1}=\left\{\beta_{j}^{*} \neq 0\right\}$ are performed independently to get a list of $p$-values. Variables associated with a $p$-value smaller than a threshold are selected and the challenge is to find this threshold to obtain an upper bound on a function of the number of selected non-active variables. Several methods control the Family-Wise Error (FWER) which is the probability of selecting at least one non-active variable [17, 18]. However, these methods tend to be conservative leading to a tiny set of selected variables. An alternative consists in controlling the FDR which is the expectation of the proportion of non-active variables among the selected ones. The authors of [19] first provide a threshold assuming independence of the $p$-values. This hypothesis is then relaxed in [20, 21, 22, 23].

Instead of considering the $p$-values, the knockoff filter method [24] consists in introducing copies of $X_{j}$ built to be non-active variables to calibrate a threshold on test statistics.

The simultaneous control of several cost functions. Controlling PR or FDR is commonly performed independently in the literature and yield different sets of selected variables. For a PR control, selected variables aim at correctly predicting a new observation of $Y$, without guaranteeing that the set of selected variables does not contain non-active variables. Conversely, when the cost function is the FDR, the number of non-active variables is controlled at the price that some active variables are not selected.

Therefore, recent works have been proposed to combine prediction and FDR approaches to select all active variables without selecting non-active ones. For instance, [25] propose a multi-step algorithm where a threshold procedure is applied to some Lasso estimators computed for specific values of $\lambda$. In addition to prediction performances, a consistency property on the selected variable set is satisfied under some conditions on $X$. Another idea is the postselection inference [26,27] where the principle is to test the relevance of each selected variable by a model selection procedure. Valid confidence intervals are provided from conditional hypothesis tests for each model of the collection in addition to a PR control. Their work has been generalized by [28, 29, 30] and a review can be found in [31].

In a completely different direction, [32, 33] propose to control the False Negative Rate (FNR) in addition to the FDR. A good FNR control ensures that most of the active variables are selected. So, minimizing a weighted sum of FDR and FNR provide a set of variables close to the set of active variables. However, improving FDR control deteriorates FNR control and vice versa. Hence, optimal controls of both criteria are impossible to achieve.

Some other papers propose to combine the FDR with the PR. Additional motivation to consider the PR is its behavior between the learning phase and the over-fitting phase. In the learning phase, the addition of a variable in the selected set drastically reduces the PR, whereas in the over-fitting phase, it increases proportionally to the noise level. Firstly, in the standard multivariate normal mean problem with a known variance, [34] propose a penalty function in the model selection procedure built from a multiple testing procedure. They obtain simultaneously sharp asymptotic bounds of the FDR and the PR. Then, [35] propose the Sorted $\ell_{1}$ penalized estimator (SLOPE) which is the minimizer of the Lasso criterion (1.2) where $\lambda$ is replaced by a $p$-vector built from a multiple testing procedure. For the orthogonal design, their approach achieves a non-asymptotic control of the FDR and satisfies a minimum value of the total mean squared error with minimax convergence rate [36]. This asymptotic convergence of the FDR has been generalized under a wide range of hypotheses, for instance, for a random design in [37].

Ordered variable selection. The ordered variable framework has attracted much attention recently, especially to overcome the high-dimensional problem. In literature, a large class of methods exists dealing with variables having a natural ranking : [38] for the regression framework, [39] with the nested lasso penalty and [40] for covariance matrix estimation. This assumption allows for drastically reducing the estimation complexity. We develop our paper's theory under this assumption. It can be applied to datasets where assuming an order of variables, obtained for example via a priori knowledge, makes sense.

However, in most applications, no canonical ranking of the variables is available and having a natural order on variables becomes a strong assumption. In this case, alternatives consist in proposing a candidate order from random procedures and applying theoretical statistical methods on the random variable ranking. Several approaches have been implemented in the literature to provide the random orders. The most used ones are based either on a regularization path which is built with the Lasso type equation solving [2] or on a decision tree [41]. However, these approaches suffer from instability in that a small modification of the initial sample could radically change the variable order [42]. To circumvent this instability problem, one solution is to add a sampling procedure like the bootstrap [43]. We adopt this point of view in this article to generalize our theoretical results in non-ordering variable selection.

### 1.3 Main contributions.

The originality of this paper is to obtain a control of the FDR in addition to the PR control in model selection through a convenient calibration of the penalty.

We assume variables are ranked according to their importance for the response variable $Y ; X_{1}$ being the most important one, $X_{2}$ being the second one, $\cdots$, and $X_{p}$ being the least important one. In Gaussian linear regression, the order is given by the partial correlation between $Y$ and each $X_{j}$. A natural model collection is the one containing the nested models respecting the variable order. This framework sounds restrictive but allows to derive theoretical expressions of the FDR in the considered model selection procedure. According to [13], all the penalty functions defined by :

$$
\operatorname{pen}\left(D_{m}\right)=K \sigma^{2} D_{m}, \quad \forall m \in \mathcal{M}
$$

provide a non-asymptotic control of the PR for $K>1$ when variables are ranked.

Theoretical bounds on the FDR in model selection : Although the model selection procedure is built for a PR control, we obtain non-asymptotic lower and upper bounds on the FDR with respect to $K>0$ when $\sigma^{2}$ is known. We show that these bounds only involve some evaluations of cumulative distribution functions of the standard Gaussian and of some chi-squared variables. Whatever the noise level, FDR is always strictly positive. When $K$ tends to infinity, the FDR

Trade-off between prediction and FDR for variable selection

converges to 0 with an exponential rate. So, a low value of the FDR is satisfying as soon as the value of $K$ is not too large.

Calibration of the hyperparameter $K$ : The obtained theoretical bounds depend on the parameters $\beta^{*}$ and $\sigma^{2}$. We replace them with estimators to obtain completely data-dependent bounds on the FDR. Then, we propose a calibration of the hyperparameter $K$ to control a trade-off between FDR and PR. Our algorithm is validated on an extensive simulation study and is compared with several existing variable selection procedures.

Towards a non-ordering variable selection : From a practical point of view, a crucial assumption of this work is the knowledge of the variable ranking. We investigate empirically an extension in which the variable ordering is not beforehand but estimated using a data-driven procedure to build random model collections.

### 1.4 Outline of the paper.

The rest of the paper is organized as follows. Section 2 introduces the Gaussian linear regression model and some notations. Section 3 contains theoretical results. Since an increase of the hyperparameter $K$ leads to a decrease of the FDR, it motivates the study of the FDR function in model selection with respect to $K$. As the FDR has an intractable expression, bounds are obtained when the variable order and the variance are known. We establish an exponential convergence rate of the FDR function when $K$ tends to infinity. The special case of orthogonal design matrix is studied to illustrate the main results. In Section 4, an algorithm is proposed to calibrate the hyperparameter $K$ in the penalty function to achieve a suitable trade-off between FDR and PR controls. It is based on simultaneous evaluations of the prediction performance and the FDR of the models, which are calculated from properly chosen estimators of $\sigma^{2}$ and $\beta^{*}$. We then present a study to generalize our procedure in non-ordering variable selection and we compare our algorithm with some existing variable selection procedures. Section 5 contains a conclusion and a discussion of prospective work. In Section 6, proofs of all the theoretical results are provided. Lastly, validations of the chosen estimators of $\sigma^{2}$ and $\beta^{*}$, of our algorithm to calibrate $K$ and of the considered alternatives to go towards the non-ordering variable selection are proposed in Section 7 through an extensive simulation study with different parameters.

## 2 Model and notations.

Let us consider the Gaussian linear regression model given in (1.1). We define $q=\min (n, p)$ and assume that $\left(X_{1}, \cdots, X_{q}\right)$ is a family of linearly independent vectors. We consider the deterministic and nested model collection of linear spaces :

$$
\mathcal{M}=\left\{m_{0}=\{0\}, m_{1}=\operatorname{Span}\left(X_{1}\right), \cdots, m_{q}=\operatorname{Span}\left(X_{1}, X_{2}, \cdots, X_{q}\right)\right\}
$$

By construction, the true model $m^{*}=\operatorname{Span}\left(X_{j}, j\right.$ s.t. $\left.\beta_{j}^{*} \neq 0\right)$ belongs to $\mathcal{M}$.

For each $m \in \mathcal{M}, D_{m}$ is the dimension of $m$ and $\hat{\beta}_{m}$ is the least-squares estimator onto $m$ :

$$
\hat{\beta}_{m}=\underset{\{\beta, X \beta \in m\}}{\arg \min }\left\{\|Y-X \beta\|_{2}^{2}\right\}
$$

With the definition of $q$ and properties on the family $\left(X_{1}, \cdots, X_{q}\right), \hat{\beta}_{m}$ is unique for each $m \in \mathcal{M}$.

For all $K>0$, we define the function $\operatorname{crit}_{K}$ on $\mathcal{M}$ as :

$$
\operatorname{crit}_{K}(m)=\left\|Y-X \hat{\beta}_{m}\right\|_{2}^{2}+K \sigma^{2} D_{m}
$$

and the selected model $\hat{m}(K)$ by :

$$
\hat{m}(K)=\underset{m \in \mathcal{M}}{\arg \min }\left\{\operatorname{crit}_{K}(m)\right\}
$$

We define $\operatorname{PR}(m)$ the predictive risk associated to the model $m \in \mathcal{M}$ by :

$$
\operatorname{PR}(m)=\mathbb{E}\left[\left\|Y-X \hat{\beta}_{m}\right\|_{2}^{2}\right]
$$

where $\mathbb{E}$ designs the expectation under the distribution of $Y$ satisfying (1.1). We define successively $F P(m)$ the number of variables contained in $m$ but not in $m^{*}$, the false discovery proportion by :

$$
\operatorname{FDP}(m)=\frac{\mathrm{FP}(m)}{\max \left(D_{m}, 1\right)}
$$

and the False Discovery Rate by :

$$
\operatorname{FDR}(m)=\mathbb{E}[\operatorname{FDP}(m)]
$$

where $\mathbb{E}$ still designs the expectation under the distribution of $Y$ satisfying (1.1), so that $\operatorname{FDR}(m)$ is deterministic even in the case where $m$ is random.

Finally, the notation $\langle.,$.$\rangle designs the canonical scalar product in \mathbb{R}^{n}, \Pi_{\mathcal{X}}$ denotes the orthogonal projection function onto the space $\mathcal{X}, \Phi$ denotes the standard Gaussian cumulative distribution function and $F_{\chi^{2}(k)}$ is the cumulative distribution function of a chi-squared variable with $k$ degrees of freedom. By convention, an intersection or an union from indices $k$ to $\ell$ with $k>\ell$ are the intersection or the union over an empty set. In the same way, the set $\{k, \cdots, \ell\}$ is empty if $k>\ell$.

## 3 Main results.

In this section, the variance $\sigma^{2}$ is supposed to be known. We first present intuitions that lead to study $\operatorname{FDR}(\hat{m}(K))$ in model selection. Non-asymptotic bounds on $\operatorname{FDR}(\hat{m}(K))$ are obtained in Theorem 3.2, as well as asymptotic behaviors when $K$ tends to infinity in Corollary 3.4. Finally, the particular case where $X$ is the orthogonal design matrix is studied to illustrate the main results.

### 3.1 Intuitions.

According to [13], the penalty function (1.4) satisfies a non-asymptotic control of the PR if and only if $K>1$. The constant $K=2$ allows to achieve the optimal asymptotic control of the PR. Hence, 2 is commonly chosen in practice but other values of $K$ close to 2 can give identical if not better non-asymptotic prediction performances. In this direction, we propose to calibrate the hyperparameter $K$ among those leading to prediction performances close to or better than for $K=2$ while satisfying a control of the $\operatorname{FDR}$. The calibration is based on both $\operatorname{PR}(\hat{m}(K))$ and $\operatorname{FDR}(\hat{m}(K))$ functions with respect to $K$.


Figure 1: Curves of the empirical $\operatorname{FDR}(\hat{m}(K))$ and $\operatorname{PR}(\hat{m}(K))$ for the toy data set described in Subsection 7.1. The vertical lines correspond to $K=3$.

We propose an example to illustrate our point and intuition. In Figure 1, we plot the empirical estimators of $\operatorname{PR}(\hat{m}(K))$ and $\operatorname{FDR}(\hat{m}(K))$ on a regular grid of positive $K$. Graphs are obtained from the toy data set described in Section 7 and values are transferred to Table 1 . We observe that the empirical $\operatorname{PR}(\hat{m}(K))$ values are kept low for $K \in[2,4]$ while the $\operatorname{FDR}(\hat{m}(K))$ function decreases with $K$ until 0 . Here, the choice $K=3$ is more judicious than $K=2$ : it ensures a stronger and positive (a FDR zero value is not relevant as it means that no variable is selected) control of the FDR while

| $\mathrm{K}$ | 0.1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| empirical <br> FDR $(\hat{m}(K))$ | 0.80 | 0.38 | 0.05 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| empirical <br> PR $(\hat{m}(K))$ | 2.01 | 1.55 | 1.25 | 1.24 | 1.25 | 1.26 | 1.28 | 1.30 | 1.32 | 1.33 | 1.36 |

Table 1: Values of the empirical estimators of $\operatorname{PR}(\hat{m}(K))$ and $\operatorname{FDR}(\hat{m}(K))$ according to $K$ for the toy data set described in Subsection 7.1.

satisfying similar prediction performances. We also observe that while FDR decreases with $K$, PR increases from a certain value of $K \geq 2$. To control PR and FDR simultaneously, the constant $K$ must be close to 2 .

Increasing the constant $K$ to limit the non-active variable selection is known for the asymptotic point of view. Indeed, AIC and Cp-Mallows penalties [9, 10], where $K$ equals 2 , give asymptotically the best set of variables for prediction performances; while BIC penalty [11], where $K$ is fixed to $\log (n)$, exactly recovers asymptotically the set of active variables. Obtaining the asymptotic properties of AIC, Cp-Mallows and BIC penalties simultaneously is impossible [44], but it suggests that a value of $K \in[2, \log (n)]$ would get reasonable (but not necessarily optimal) values for both PR and FDR in a non-asymptotic framework. In this way, we propose to study the function $\operatorname{FDR}(\hat{m}(K))$ in the model selection procedure (2.2) where the penalty function is (1.4) in the ordered variable setting.

### 3.2 Bounds on the FDR in model selection.

### 3.2.1 FDR expression in model selection for ordered variables.

Let us assume that $K>0$ and $\operatorname{crit}_{K}$ is injective on $\mathcal{M}$. If $D_{m}^{*}=q, \operatorname{FDR}(\hat{m}(K))=0$. Otherwise, the $\operatorname{FDR}(\hat{m}(K))$ is expressed within the model selection procedure as :

$$
\operatorname{FDR}(\hat{m}(K))=\sum_{r=D_{m^{*}}+1}^{q} \frac{r-D_{m^{*}}}{r} \mathbb{P}\left(\left\{\bigcap_{\substack{\ell=0 \\ \ell \neq r}}^{q}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\}\right)
$$

A detailed proof of (3.1) can be found in Subsection 6.1.

By using the decomposition

$$
\left\{\bigcap_{\ell=0}^{r-1}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\} \bigcap\left\{\underset{\ell=r+1}{q}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\}
$$

of the term $\underset{\substack{\ell=0 \\ \ell \neq r}}{q}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}$, we obtain the following proposition :

Proposition 3.1. Let us consider the ordered variable framework and the model collection (2.1) where $q=\min (n, p)$, $m^{*} \in \mathcal{M}$ and $D_{m}^{*}<q$. Let us assume that crit ${ }_{K}$ is injective on $\mathcal{M}$. Let $\left(u_{1}, \cdots, u_{n}\right)$ an orthonormal basis of $\mathbb{R}^{n}$ such that $\operatorname{Span}\left(X_{1}, \cdots, X_{j}\right)=\operatorname{Span}\left(u_{1}, \cdots, u_{j}\right), \forall j \in\{1, \cdots, q\}$.

Then, $\forall K>0$,

$$
\operatorname{FDR}(\hat{m}(K))=\sum_{r=D_{m^{*}+1}}^{q} \frac{r-D_{m^{*}}}{r} P_{r}(K) Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)
$$

where for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$,

$$
P_{r}(K)=\mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell} Z_{k}^{2}<K(\ell-r)\right\}\right)
$$

where $Z_{k} \stackrel{i . i . d .}{\sim} \mathcal{N}(0,1), \forall k \in\{r+1, \cdots, q\}$,

$$
\text { and } Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)=\mathbb{P}\left(\bigcap_{\ell=0}^{r-1}\left\{\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}>K \sigma^{2}(r-\ell)\right\}\right)
$$

Trade-off between prediction and FDR for variable selection

A proof of Proposition 3.1 can be found in Subsection 6.1.

### 3.2.2 General bounds.

In (3.2), the $P_{r}(K)$ terms do not depend on data. Conversely, the $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ terms depend on the data. Thus, to understand the behavior of the FDR function with respect to $\hat{m}(K)$, we propose to bound the $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ terms in the following theorem :

Theorem 3.2. Let us consider the ordered variable framework and the model collection (2.1) where $q=\min (n, p)$. Let us suppose that $m^{*} \in \mathcal{M}$ and $D_{m}^{*}<q$. The notation $\Phi$ stands for the standard gaussian cumulative distribution function and $F_{\chi^{2}(k)}$ is the cumulative distribution function of a chi-squared variable with $k$ degrees of freedom. Let us assume that $\forall K>0$, crit $_{K}$ is injective on $\mathcal{M}$. Let $\left(u_{1}, \cdots, u_{n}\right)$ an orthonormal basis of $\mathbb{R}^{n}$ such that $\operatorname{Span}\left(X_{1}, \cdots, X_{j}\right)=\operatorname{Span}\left(u_{1}, \cdots, u_{j}\right), \forall j \in\{1, \cdots, q\}$.

Then, $\forall K>0, \hat{m}(K)$ satisfies :

$$
b\left(K, \beta^{*}, \sigma^{2}\right) \leq F D R(\hat{m}(K)) \leq B\left(K, \beta^{*}, \sigma^{2}\right)
$$

where $\left[K \mapsto b\left(K, \beta^{*}, \sigma^{2}\right)\right]$ and $\left[K \mapsto B\left(K, \beta^{*}, \sigma^{2}\right)\right]$ are two real-valued functions on $\mathbb{R}^{+}$defined by :

$$
\begin{aligned}
b\left(K, \beta^{*}, \sigma^{2}\right) & =\sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right) \\
B\left(K, \beta^{*}, \sigma^{2}\right) & =\sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
\end{aligned}
$$

where for all $K>0, P_{r}(K)$ is defined in (3.3) and

1. for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $\ell \in\{1, \cdots, r\}, \underline{f}_{\ell}\left(\cdot, \beta^{*}, \sigma^{2}\right)$ is defined by :

$$
\begin{aligned}
& \underline{f}_{1}\left(K, \beta^{*}, \sigma^{2}\right)=G_{1} \\
& \underline{f}_{\ell}\left(K, \beta^{*}, \sigma^{2}\right)=G_{\ell}+H_{\ell} \underline{f}_{\ell-1}\left(K, \beta^{*}, \sigma^{2}\right), \quad \forall \ell \in\{2, \cdots, r\}
\end{aligned}
$$

with for $\ell \in\left\{1, \cdots, D_{m^{*}}\right\}$ :

$$
G_{\ell}=2-\left(\Phi\left(\sqrt{\ell K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)\right)
$$

for $\ell \in\left\{2, \cdots, D_{m^{*}}\right\}$ :

$$
\begin{aligned}
H_{\ell}= & \Phi\left(\sqrt{\ell K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right) \\
& -\left(\Phi\left(\sqrt{K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)\right)
\end{aligned}
$$

for $\ell \in\left\{D_{m^{*}}+1, \cdots, r\right\}$ :

$$
\begin{aligned}
& G_{\ell}=2(1-\Phi(\sqrt{\ell K})) \\
& H_{\ell}=2(\Phi(\sqrt{\ell K})-\Phi(\sqrt{K}))
\end{aligned}
$$

2. $\forall r \in\left\{D_{m^{*}}+1, \cdots, q\right\}, \bar{f}_{r}\left(\cdot, \beta^{*}, \sigma^{2}\right)$ is defined by :

$$
\begin{aligned}
\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)= & 1-\max \left(\max _{\ell \in\left\{1, \cdots, r-D_{m^{*}}\right\}}\left(F_{\chi^{2}(\ell)}(\ell K)\right)\right. \\
& \left.\max _{\ell \in\left\{r-D_{m^{*}}+1, \cdots, r\right\}}\left(F_{\chi^{2}(\ell)}\left(\frac{\ell K}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)\right)\right)
\end{aligned}
$$

A proof of Theorem 3.2 can be found in Subsection 6.2.

Hence, although the model selection procedure is built for prediction performances, bounds on the FDR are derived with respect to $\hat{m}(K)$. Terms $\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ and $\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ only involve evaluations of cumulative distribution functions of the standard Gaussian and chi-squared variables. So, they have a fully explicit form which simplifies the understanding of the behavior of the FDR in model selection. However, they depend on the unknown parameters $\beta^{*}$ and $\sigma^{2}$ for which estimators are proposed in Section 4.1.2.

### 3.2.3 Strictly positive FDR.

The following corollary gives a lower bound on the FDR independent from $\sigma^{2}$.

Corollary 3.3. Under the assumptions and definitions of Theorem 3.2, $\forall K>0$ :

$$
F D R(\hat{m}(K)) \geq \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \frac{2 \sqrt{2}}{\sqrt{\pi}(\sqrt{r K}+\sqrt{r K+4})} e^{-\frac{r K}{2}}\right)>0
$$

A proof of Corollary 3.3 can be found in Subsection 6.3.

From Corollary 3.3, $\operatorname{FDR}(\hat{m}(K))>0$ for all $K>0$ and whatever $\sigma^{2}$. This may be counter-intuitive, especially in the noiseless setting. When $\sigma^{2}=0, Y=X \beta^{*}$ and the minimization in (2.2) is reduced to the least-squares criterion minimization. So, in this particular noiseless case, $\hat{\beta}_{m^{*}}=\beta^{*}$ and the associated least-squares criterion is zero. Any $m$ including $m^{*}$ also attains a least squares objective of zero as the magnitude of the regression coefficients corresponding to the non-active variables is null. Such supersets can be selected leading to $\operatorname{FDP}(\hat{m})>0$ and so $\operatorname{FDR}(\hat{m})>0$.

### 3.2.4 Asymptotic analysis.

The following corollary gives the asymptotic behavior of the FDR function in model selection when $K$ tends to infinity.

Corollary 3.4. Under the assumptions and the definitions of Theorem 3.2, the $\operatorname{FDR}(\hat{m}(K))$ function tends to 0 when $K$ tends to infinity and satisfies $\forall \eta>0$,

$$
\operatorname{FDR}(\hat{m}(K))=\underset{K \longrightarrow+\infty}{o}\left(e^{-K\left(\frac{1}{2}-\eta\right)}\right)
$$

Furthermore, $\forall \eta>0, \exists C_{\eta}>0, \exists L_{\eta}>0, \forall K>L_{\eta}$, we have :

$$
F D R(\hat{m}(K)) \geq C_{\eta} e^{-K\left(\frac{D_{m^{*}+1+2 \eta}}{2}\right)}
$$

So, $\forall \varepsilon>0$,

$$
\begin{aligned}
-\frac{D_{m^{*}}}{2}-\frac{1}{2}-\varepsilon \leq & \liminf _{K \longrightarrow+\infty} \frac{1}{K} \log (\operatorname{FDR}(\hat{m}(K))) \\
& \limsup _{K \longrightarrow+\infty} \frac{1}{K} \log (\operatorname{FDR}(\hat{m}(K))) \leq-\frac{1}{2}+\varepsilon
\end{aligned}
$$

A proof of Corollary 3.4 can be found in Subsection 6.4 .

From Equation (3.6), $\operatorname{FDR}(\hat{m}(K))$ tends to 0 when $K$ tends to $+\infty$ with at least an exponential convergence rate and Equation (3.7) suggests that the exponential convergence rate is optimal.

Remark 3.5. With no signal $\left(\beta^{*}=0\right.$ and $D_{m^{*}}=0$ ), the asymptotic bounds in (3.8) are $-\frac{1}{2}-\varepsilon$ and $-\frac{1}{2}+\varepsilon$ and consequently :

$$
\log (\operatorname{FDR}(\hat{m}(K))) \underset{K \rightarrow+\infty}{\sim}-\frac{1}{2} K
$$

Remark 3.6. The asymptotic upper and lower bounds (3.6) and (3.7) are satisfied whatever the value of $\sigma^{2}>0$. It is possible to obtain the following sharpest asymptotic upper bound : $\forall \tilde{\eta}>0$,




Subsection 6.4.

### 3.3 Illustrations of the main result in the orthogonal case.

We propose to analyze the particular case where the design matrix $X$ is orthogonal since it leads to simplified forms for the FDR bounds that are easy to calculate.

Corollary 3.7 (Application on the orthogonal case). Under assumptions of Theorem 3.2 and by assuming that $\left(X_{1}, \cdots, X_{q}\right)$ are orthonormal with respect to $\langle.,$.$\rangle , then, \forall K>0, \operatorname{FDR}(\hat{m}(K))$ satisfies the same inequalities as (3.4) where :

for $\ell \in\left\{1, \cdots, D_{m^{*}}\right\}$ :

for $\ell \in\left\{2, \cdots, D_{m^{*}}\right\}$ :

$$
G_{\ell}=2-\left(\Phi\left(\sqrt{\ell K}-\frac{\beta_{\ell}^{*}}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\beta_{\ell}^{*}}{\sigma}\right)\right)
$$

$$
H_{\ell}=\Phi\left(\sqrt{\ell K}-\frac{\beta_{\ell}^{*}}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\beta_{\ell}^{*}}{\sigma}\right)-\left(\Phi\left(\sqrt{K}-\frac{\beta_{\ell}^{*}}{\sigma}\right)+\Phi\left(\sqrt{K}+\frac{\beta_{\ell}^{*}}{\sigma}\right)\right)
$$

for all $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ :

$$
\begin{aligned}
\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)=1-\max & \max _{\ell \in\left\{1, \cdots, r-D_{m^{*}}\right\}}\left(F_{\chi^{2}(\ell)}(\ell K)\right) \\
& \left.\max _{\ell \in\left\{r-D_{m^{*}}+1, \cdots, r\right\}}\left(F_{\chi^{2}(\ell)}\left(\frac{\ell K}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\beta_{k}^{* 2}}{\sigma^{2}}\right)\right)\right)
\end{aligned}
$$

and all other terms are the same as those defined in Theorem 3.2.

A proof of Corollary 3.7 can be found in Subsection 6.5.


Figure 2: Left : curves of the empirical $\operatorname{FDR}(\hat{m}(K))$ (red) and of the terms $b\left(K, \beta^{*}, \sigma^{2}\right)$ (green) and $B\left(K, \beta^{*}, \sigma^{2}\right)$ (blue) for the orthogonal design matrix $X$ for the toy data set described in Subsection 7.1. Right : curves are plotted only for $K \geq 2$.

In Figure 2, we plot the empirical estimation of the $\operatorname{FDR}(\hat{m}(K))$ with the functions $b\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \beta^{*}, \sigma^{2}\right)$ on a grid of positive $K$ (left) and for $K \geq 2$ (right). Graphs are obtained from the toy data set described in Section 7 where $X$ is orthogonal. The left figure is devoted to illustrate Corollary 3.7. The FDR values are well smaller than the upper bound values and larger than the lower bound ones. From the right figure and in accordance with Corollary 3.4, the empirical $\operatorname{FDR}(\hat{m}(K))$ values tend to 0 when $K$ increases and the convergence rate seems to be exponential. Moreover, the curves of $b\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \beta^{*}, \sigma^{2}\right)$ frame the empirical FDR and the difference between the three functions becomes quickly negligible for $K$ larger than 2 .

## 4 Trade-off between the PR and the FDR controls.

While bounds $b\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \beta^{*}, \sigma^{2}\right)$ are easily understandable and fully implementable, they depend on $\beta^{*}$, $\sigma^{2}$ and $D_{m}^{*}$. These quantities are unknown in practice. For a practical use, we propose to replace the theoretical bounds on the FDR as well as the theoretical expression of the PR with observable quantities (Subsection 4.1). Then, we propose an algorithm to calibrate the hyperparameter $K$ from the data set such that both PR and FDR are controlled (Subsection 4.2).

As variables are not usually naturally ranked, we explore the robustness of our algorithm under perturbations of the correct variable ordering and present approaches for obtaining a variable ordering in a data-driven manner. Results are provided in Subsection 4.3. Lastly, our algorithm is compared with some existing variable selection procedures in Subsection 4.4, in terms of both PR and FDR.

### 4.1 Estimation of the unknown quantities appearing in our bounds.

We propose to replace the theoretical terms by observable quantities.

### 4.1.1 Estimation of the PR.

Commonly, the predictive risk is evaluated with the mean squared error on a validation set independent from the training set used to estimate the parameters (see Formula (7.1) for the definition). However, it requires separating the dataset in two parts which increases the estimation errors. Here, we propose to use the entire dataset to both apply the model selection procedure and evaluate the predictive risk. Intuitively, the response vector $Y$ is replaced with $X \hat{\beta}_{\hat{m}(2)}$ which provides good prediction performances [13]. Moreover, by re-expressing the PR, it is straightforward to show that for all $K>0$ and $K^{\prime}>0$ :

$$
\begin{aligned}
& \mathbb{E}\left[\left\|Y-X \hat{\beta}_{\hat{m}(K)} \mid\right\|_{2}^{2}\right]- \mathbb{E}\left[\left\|Y-X \hat{\beta}_{\hat{m}\left(K^{\prime}\right)}\right\|_{2}^{2}\right] \\
&=\mathbb{E}\left[\left\|X \hat{\beta}_{\hat{m}(2)}-X \hat{\beta}_{\hat{m}(K)}\right\|_{2}^{2}\right]-\mathbb{E}\left[\left\|X \hat{\beta}_{\hat{m}(2)}-X \hat{\beta}_{\hat{m}\left(K^{\prime}\right)} \mid\right\|_{2}^{2}\right] \\
&-2 \mathbb{E}\left[\left\langle X \hat{\beta}_{\hat{m}(2)}-Y, X \hat{\beta}_{\hat{m}\left(K^{\prime}\right)}-X \hat{\beta}_{\hat{m}(K)}\right\rangle\right]
\end{aligned}
$$

According to [45], the constant 2 provides the optimal asymptotic control of (2.3), so $\left\|Y-X \hat{\beta}_{\hat{m}(2)}\right\|_{2}$ is close to 0 . Moreover, $X \hat{\beta}_{\hat{m}(2)}$ is close to $\Pi_{\operatorname{Im}(X)}(Y)$, so $X \hat{\beta}_{\hat{m}(2)}-Y$ almost belongs to the subspace $\operatorname{Im}(X)^{\perp}$. $\operatorname{In}$ addition, $X \hat{\beta}_{\hat{m}(K)}$ and $X \hat{\beta}_{\hat{m}\left(K^{\prime}\right)}$ belongs to $\operatorname{Im}(X)$, so the last term in (4.1) is close to 0 and is negligible compared to the two others. So, for all $K>0$ and $K^{\prime}>0, \mathbb{E}\left[\left\|Y-X \hat{\beta}_{\hat{m}(K)}\right\|_{2}^{2}\right]-\mathbb{E}\left[\left\|Y-X \hat{\beta}_{\hat{m}\left(K^{\prime}\right)}\right\|_{2}^{2}\right]$ equals $\mathbb{E}\left[\| X \hat{\beta}_{\hat{m}(2)}-\right.$ $\left.X \hat{\beta}_{\hat{m}(K)} \|_{2}^{2}\right]-\mathbb{E}\left[\left\|X \hat{\beta}_{\hat{m}(2)}-X \hat{\beta}_{\hat{m}\left(K^{\prime}\right)}\right\|_{2}^{2}\right]$ up to an additive negligible term. Hence, the constant $K$ minimizing $\mathbb{E}\left[\left\|X \hat{\beta}_{\hat{m}(2)}-X \hat{\beta}_{\hat{m}(K)}\right\|_{2}^{2}\right]$ and the one minimizing $\mathbb{E}\left[\left\|Y-X \hat{\beta}_{\hat{m}(K)}\right\|_{2}^{2}\right]$ are almost equal. Therefore, to evaluate the prediction performances of $\hat{m}(K)$, we propose to compare prediction performances of the estimates $X \hat{\beta}_{\hat{m}(K)}$ and $X \hat{\beta}_{\hat{m}(2)}$. We introduce the following term that we call estimated difference in predictions :

$$
\widehat{\operatorname{diff-PR}}(\hat{m}(K))=\frac{1}{n} \sum_{i=1}^{n}\left(\left(X \hat{\beta}_{\hat{m}(2)}\right)_{i}-\left(X \hat{\beta}_{\hat{m}(K)}\right)_{i}\right)^{2}
$$

For the rest of the paper, the empirical version of (4.2) is calculated averaging over 100 independent data sets and is denoted diff-PR. If this difference is significantly smaller than the noise level $\sigma^{2}$, the model $\hat{m}(K)$ has performances similar to those satisfied by $\hat{m}(2)$.

### 4.1.2 Estimation of the FDR.

The functions $b\left(\cdot, \beta^{*}, \sigma^{2}\right)$ and $B\left(\cdot, \beta^{*}, \sigma^{2}\right)$ are explicit and easily implementable but depend on $\beta^{*}, \sigma^{2}$ and $D_{m}^{*}$, which are unknown.

We propose :

1. to apply the slope heuristic method [13] to get an estimator $\hat{\sigma}^{2}$ of $\sigma^{2}$,
2. to replace $\beta^{*}$ by the estimator $\hat{\beta}_{\hat{m}(4)}$,

Trade-off between prediction and FDR for variable selection

3. to replace $D_{m^{*}}$ by the number of non zero in $\hat{\beta}_{\hat{m}(4)}$.

Justifications are provided in Subsection 7.2.

### 4.2 A data-dependent calibration of $K$ in the model selection procedure.

We propose a completely data-driven calibration of the hyperparameter $K$ up to chosen parameters $\alpha$ and $\gamma$ that we define just below. The algorithm depends on the functions $K \longrightarrow B\left(\cdot, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ and $K \longrightarrow \widehat{\operatorname{diff}-\mathrm{PR}}(\hat{m}(K))$ to obtain a lower bound on both PR and FDR.

We propose the following algorithm :



Curves of Figure 3 are generated from the toy data set and from the simulation protocol described in Subsection 7.1. Parameters $\alpha$ and $\gamma$ are free and are defined by the user for maximum acceptable values for FDR and PR. In this example, we choose $\alpha=0.05$ and $\gamma=0.1$. The graph at bottom right shows that there exists some constants $K$ for which a trade-off between both theoretical FDR and PR and both empirical FDR and PR can be achieved: here for a value of $K$ between 2 and 6 . These values correspond to a selected model dimension close to $D_{m^{*}}$ (Figure 3 at the bottom left). By applying our algorithm on this example, we get $I_{1}=[3.3,10]$ and $I_{2}=[2,5.8]$ and so, our proposed algorithm returns $K=3.3$. The evaluation of the prediction performances provided by the selected model $\hat{m}(3.3)$ is equal to 1.14 and we get $B\left(3.3, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)=0.03$. The constant $K=3.3$ corresponds to a low value of both empirical predictive risk and FDR functions. Indeed, the empirical predictive risk of $\hat{m}(3.3)$ is equal to 1.24 and the empirical FDR of $\hat{m}(3.3)$ is equal to 0.01 . To compare with the usual choice $K=2$, the empirical predictive risk of $\hat{m}(2)$ is equal to 1.25 and the empirical FDR of $\hat{m}(2)$ is equal to 0.05 . Hence, our proposed algorithm allows to maintain the prediction performances from $\hat{m}(2)$, reinforce the control of the FDR criterion and so gain a convenient trade-off between PR and FDR.

In Subsection 7.4, the algorithm 1 is applied to several data sets generated from various sets of parameters and described in Table 4. Each time, the hyperparameter $K$ is strictly larger than the commonly used constant 2 and provides a low value of FDR while maintaining the prediction performances given by $\hat{m}(2)$.

### 4.3 Towards the non-ordering variable selection

For most applications, no canonical order of variables is available and our algorithm cannot be applied directly. We propose to generate candidate orders from random procedures to use our method in non-ordering variable selection. More precisely, we first study the robustness to variable ordering of our method (Subsection 4.3.1) and provide some procedures to construct variable orders in practice (Subsection 4.3.2). Our algorithm 1 is then applied from the generated rankings in Subsection 4.4.

### 4.3.1 Robustness to variable ordering

We propose numerical experiments where the assumption of ordered variables is not fulfilled. The goal is to test the robustness to variable ordering of our algorithm by measuring how this impacts its performances. We consider the toy data set where the size of the true model is $D_{m^{*}}=10$ and we consider three collections which are the results of a random permutation of the nested model collection (2.1) on respectively the first ten, the first twelve and the first fifteen variables. Hence, active variables remain first in the first collection; perturbations may introduce non-active variables among the first ten variables in the second collection, while in the third collection, some active variables can be pushed far into the collection.





FDR



diff-PR



selected model per dim



FDR and $\widehat{\text { FDR }}$ as function of diff-PR and $\widehat{\text { diff-PR }}$

Figure 3: Top : Curves of the empirical functions $\operatorname{FDR}(\hat{m}(K))$ (red) and diff-PR $(\hat{m}(K))$ (blue), of the $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ functions (pink) and of $\widehat{\text { diff-PR }}(\hat{m}(K))$ (violet) for $K \geq 2$ for the toy data set. Bottom: Curves of the $D_{\hat{m}(K)}$ as function of $K$ averaged over the 1000 data sets (left) and values of the empirical $\operatorname{FDR}(\hat{m}(K))$ and $\widehat{\operatorname{FDR}}(\hat{m}(K))$ as functions of diff-PR $(\hat{m}(K))$ and $\widehat{\operatorname{diff}-\mathrm{PR}}(\hat{m}(K))$ (right) for all $K>0$ and for the toy data set.

To test the robustness to variable ordering of our algorithm, Figure 4 shows how the empirical FDR behaves in relation to its estimated upper bound as well as the empirical and estimated differences in predictions for the three perturbed collections. We observe that when the permutation concerns only the active variables (on the nested model collection (2.1)), values of the empirical FDR are smaller than the values of $B\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ which are close. For prediction, the diff-PR function has the same behavior than for the nested model collection (2.1).

When the permutation concerns the first twelve and the first fifteen variables, the empirical FDR is higher than $B\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ as soon as $K \geq 2$ and with an increasing deviation when the error on estimated variable order increases. Moreover, we observe that the rate of the empirical FDR decay is much slower and values are high whatever the value of $K$ : above 0.13 and 0.28 for respectively the second and third perturbed model collection. For prediction, the diff-PR function is stable for $K \geq 2$.





FDR



diff-PR

Figure 4: Curves of the empirical functions $\operatorname{FDR}(\hat{m}(K))$ (red) and diff-PR $(\hat{m}(K))$ (blue), of the $B\left(K, \beta^{*}, \sigma^{2}\right)$ functions (blue), the $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ functions (pink) and $\widehat{\operatorname{diff}-\mathrm{PR}}(\hat{m}(K))$ (violet) for the toy data set and for the three perturbed collections.

Hence, permutations among only the active variables have no effect on FDR and PR. However, as soon as a non-active variable is ranked before an active variable, the theoretical guarantees of Theorem 3.2 no longer hold and empirical FDR can be high whatever the value of $K$. To tackle this problem, one solution consists of combining our algorithm with a method discriminating active and non-active variables. We consider this direction for the rest of this section.

### 4.3.2 Random variable order

We consider four strategies to estimate variable orders. The Bolasso procedure [6] consists in solving the Lasso equation (1.2), through the LARS algorithm [46], on several resamples and for different values of $\lambda$. Variables are ranked according to their occurrence frequency in the models averaged over the $\lambda$ 's and the resamples. The random forests [43] are aggregation of several binary decision trees. The tree predictors are generated on bootstrap resamples and on a subset of variables randomly chosen. Here, we combine the random forest with the recursive feature elimination (RFE) algorithm [47] whose efficiency has been proved especially for correlated variables [48]. Variables are ordered according to their importance defined by the random forest. The Sorted $\ell_{1}$ penalized estimator (SLOPE) [35] is obtained by solving the Lasso equation (1.2) with $\lambda$ a $p$-vector calculated from a multiple testing procedure. Lastly, the knockoff method [24] consists in building a non-active copy $\tilde{X}_{j}$ of each $X_{j}$ and solving the Lasso equation (1.2) for several values of $\lambda$ on the augmented matrix composed on the $X_{j}$ and $\tilde{X}_{j}$ variables. Variables are then sorted according to the values of

$$
W_{j}=\max \left(Z_{j}, \tilde{Z}_{j}\right) \times \operatorname{sign}\left(Z_{j}-\tilde{Z}_{j}\right)
$$

where $Z_{j}$ and $\tilde{Z}_{j}$ correspond to the largest $\lambda$ for which $X_{j}$ and $\tilde{X}_{j}$ are respectively selected. For each strategy, a random model collection, on which model selection can be applied is defined from the estimated variable order. Bolasso and random forest both provide a variable order from a prediction point of view, whereas SLOPE and the knockoff method provide a variable order by considering both PR and FDR controls.

To quantify the ability to discriminate between active and non-active variables, we calculate the proportion of active variables in models of size 5, 10, 15 and 20 of each random collection. Results are presented in Table 2 where each value is the average over 100 independent iterations. With Bolasso, random forests and SLOPE, 50 resamples for the construction of random collections are considered.

|  | Bolasso | SLOPE | random <br> forests | the knockoff <br> method |
| :--- | :--- | :--- | :--- | :--- |
| $D_{m}=5$ | 0.99 | 0.99 | 0.98 | 1.00 |
| $D_{m}=10$ | 0.83 | 0.83 | 0.82 | 0.85 |
| $D_{m}=15$ | 0.92 | 0.92 | 0.90 | 0.90 |
| $D_{m}=20$ | 0.95 | 0.95 | 0.93 | 0.92 |

Table 2: Proportion of active variables in models of size 5, 10, 15 and 20 for random collections built with Bolasso, SLOPE, random forest and the knockoff method. Each value is the average over 100 independent iterations.

The collection built by the knockoff method is the collection containing the fewest non-active variables in the models of size 5 and 10. For models of size 15 and 20, Bolasso and SLOPE are slightly better and the proportion of active variables is always larger than 0.9 . We observe with the model of size 20 that there are active variables far away in the collections, which is undesirable. In the following, we consider now the random collections built with the knockoff method and Bolasso (since Bolasso is slightly better than SLOPE on scenarios described in Table 4 (see Subsection 7.3)).

### 4.4 Comparison with other variable selection methods

Performances of Algorithm 1 are compared with three variable selection procedures. The LinSelect penalty [16] is a model selection criterion introduced in a non-asymptotic setting to take into account of the randomness of the model collection. The penalty function provides a sharp oracle inequality. The $V$-fold cross-validation $[49,50,51]$ is the most popular, adaptive and simple variable selection method. The final selected model is the one with the best prediction performance accuracy over the data sets obtained by splitting the initial data set into a training set and a validation set. The last method is the knockoff method where the final variable subset is composed by $X_{j}$ such that $W_{j} \geq T$ where $T$ is defined to satisfy a given control of FDR. LinSelect and $V$-fold cross-validation aim at providing a control of PR while the knockoff method aims at providing a control of FDR.

We consider the 50-fold cross-validation and evaluate PR and FDR of our algorithm and of the three variable selection procedures on the nested model collection (2.1) where the active variables are properly ranked before the non-active variables and on random collections built with Bolasso and with the knockoff method.

|  | $D_{\hat{m}}$ | $\operatorname{PR}(\hat{m})$ | FDR $(\hat{m})$ |
| :--- | :--- | :--- | :--- |
| nested model collection |  |  |  |
| LinSelect | 8.86 | 1.35 | 0.01 |
| 50-fold CV | 26.42 | 2.29 | 0.45 |
| Knockoff |  |  |  |
| Our algorithm | 9.37 | 1.25 | 0.00 |
| Bolasso collection |  |  |  |
| LinSelect | 10.17 | 1.93 | 0.07 |
| 50-fold CV | 22.10 | 2.77 | 0.37 |
| Knockoff |  |  |  |
| Our algorithm | 13.96 | 1.59 | 0.25 |
| the knockoffs collection |  |  |  |
| LinSelect | 8.86 | 1.81 | 0.03 |
| 50-fold CV | 20.85 | 2.45 | 0.35 |
| Knockoff | 0.00 | 14.10 | 0.00 |
| Our algorithm | 13.33 | 1.65 | 0.18 |

Table 3: Results of the dimension, PR and FDR of the selected models obtained by LinSelect, the 50 -fold CV, the knockoff method and our algorithm, applied on the nested model collection (2.1) and on random collections built with Bolasso and the knockoff method. Each value is the average over 100 independent iterations. PR and FDR of each selected model are the empirical quantities. Input parameters of our algorithm are fixed to $\gamma=0.1$ and $\alpha=0.05$. Note that the knockoff variable selection method is adapted for only the knockoff random model collection.

Table 3 shows the performances of the four variable selection procedures. As the knockoff method is a procedure for both collection generation and variable selection, the knockoff collection is only used with the knockoff variable

Trade-off between prediction and FDR for variable selection

selection method. On the nested model collection (2.1), our algorithm provides the smallest values in both FDR and PR and the average of the selected model sizes is the closest to the true model size. LinSelect behaves in a similar way while the 50-fold cross validation selects a model located in the over-fitting area providing a high value of both PR and FDR. On random model collections, performances are deteriorated for all methods, as expected, and are slightly better on model collections built with the knockoff method than with Bolasso. Our algorithm provides the smallest PR but LinSelect provides the smallest FDR. While LinSelect is designed to control the PR theoretically, we remark that it is apparently also a relevant candidate to control FDR and to achieve a trade-off between both PR and FDR. The 50 -fold cross validation method provides poor results while the knockoff method selects the empty set of variable. The size of the model selected by our algorithm is larger when the collections are random and provides high values of FDR. These results show that a meticulous choice of $\gamma$ and $\alpha$ is important to improve our algorithm performances.

The robustness of our algorithm to variable order, the construction of random model collections and performances of the four variable selection procedures are studied on several data sets generated from various sets of parameters and described in Table 4. Results are presented in Subsection 7.3 and Subsection 7.4 and the conclusions remain the same.

## 5 Conclusions.

The variable selection procedure in a high-dimensional Gaussian linear regression with sparsity assumption is commonly used to identify a set of variables with prediction performances or with as few non-active variables as possible. For prediction performances, the PR is usually controlled via a penalized least-squares minimization; to avoid the selection of non-active variables, the FDR is usually controlled via a multiple testing approach. Controlling the PR tends to select too many variables, including non-active ones, whereas controlling the FDR tends to select too few variables, leaving out some active ones.

This work shows that a convenient trade-off between PR and FDR can be achieved in ordered variable selection. The originality of this paper is to obtain this trade-off through a proper calibration of the hyperparameter $K$ in the penalty of the model selection (1.4). Firstly, theoretical results lead to non-asymptotic lower and upper bounds on the $\operatorname{FDR}(\hat{m}(K))$ function when $\sigma^{2}$ is known. Asymptotic behaviors suggest that bounds are optimal. Secondly, the proposed methodology provides an algorithm to calibrate the hyperparameter $K$ in the penalty function when $\sigma^{2}$ is unknown. This algorithm is based on completely data-driven terms : the estimated difference in predictions and the estimated upper bound on the FDR where the choices of estimators $\hat{\sigma}^{2}$ and $\hat{\beta}_{\hat{m}(4)}$ are derived from an extensive simulation study. The hyperparameter $K$ is calibrated from the dataset to ensure $\widehat{\text { diff-PR }}(\hat{m}(K))<\gamma \times \hat{\sigma}^{2}$ under the constraint $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)<\alpha$. Our algorithm is validated on an extensive simulation study and allows to obtain a selected model ensuring a small value of both theoretical PR and FDR. The calibrated hyperparameter $K$ is strictly larger than the commonly used constant $K=2$. Moreover, PR and FDR values of the selected model with our algorithm are the smallest values compared with the existing variable selection procedures considered in the paper. Lastly, we propose a preliminary response to construct a random model collection to extend our work in non-ordering variable selection. The performances of our algorithm deteriorate as soon as a non-active variable is ranked before an active one, but combined with procedures with high ability to discriminate between active and non-active variables, our algorithm is competitive with some existing variable selection procedures.

If $D_{\hat{m}(K)}=q$ for one $K>1$, the lower and upper bounds equal 0 . This means that a distinction between $D_{m^{*}}=q$ and $D_{m^{*}}<q$ is not possible without additional arguments. This is a limitation of our work.

The main perspective of our work is to generalize our theoretical results to non-ordering variable selection. The ordered variable assumption is the key ingredient of our proofs and appears in the second line of the proof where the ratio is fixed, allowing randomness only on $\hat{m}$ that we control thanks to the ordered model selection theory. Hence, relaxing this assumption requires new technical arguments and this is a real challenge for future work. Moreover, in non-ordering variable selection, the penalty function (1.4) has to include a logarithmic term to take into account that all possible models should be explored but this is computationally infeasible given the combinatorial nature of the problem. In this case, two hyperparameters have to be calibrated. Another way to generalize our work in non-ordering variable selection is to detect the value of $K$ from which the theoretical FDR is larger than the theoretical upper bound on the FDR and quantify the gap between the theoretical upper bound and the FDR.

One way to improve the performances of our algorithm can be a meticulous choice of the algorithm input parameters $\alpha$ and $\gamma$, which are arbitrarily fixed in our work.

Achieving a trade-off between FDR and PR is not trivial and investigating alternatives in this direction can be considered in future work. In particular, satisfying some trade-offs between PR and FDR for each model of the generated collection can be judicious in processing our variable selection then.

A possible opening is to study the potential characteristics of the hyperparameter $K$ provided by our algorithm in a theoretical point of view (dependence in $\beta^{*}$ and $\sigma^{2}$ ). Another possible extension is to study the false negative rate (FNR) function in the model selection procedure, similarly and in addition to the FDR one. This can provide a more powerful method, similarly to [32, 33].

Finally, another generalization is to extend our theoretical results to unknown variance, random model collections or to non-fixed designs, which are more general frameworks adapted to some application points of view. These extensions are much more intricate.

## 6 Proofs of theoretical results.

This section contains proofs of all the theoretical results of this paper.

### 6.1 FDR expression in model selection.

## Proof of Formula 3.1.

If $D_{m}^{*}=q$, then $\operatorname{FP}(m)=0$ for all $m \in \mathcal{M}$ and $\operatorname{FDR}(m)=0$ for all $m \in \mathcal{M}$.

Let us now suppose that $D_{m}^{*}<q$. The FDP expression within the model selection procedure is :

$$
\begin{aligned}
& \forall K>0, \quad \operatorname{FDP}(\hat{m}(K))=\frac{\operatorname{FP}(\hat{m}(K))}{\max \left(D_{\hat{m}(K)}, 1\right)} \\
& \underset{(*)}{=} \frac{D_{\hat{m}(K)}-D_{m^{*}}}{D_{\hat{m}(K)}} \mathbb{1}_{\left\{D_{\hat{m}(K)}>D_{m^{*}}\right\}} \\
& =\sum_{r=1}^{q} \frac{r-D_{m^{*}}}{r} \mathbb{1}_{\left\{r>D_{m^{*}}\right\}} \mathbb{1}_{\left\{D_{\hat{m}(K)}=r\right\}} \\
& =\sum_{(\text {**) }}^{=} \frac{r-D_{m^{*}}}{r} \mathbb{1}_{\left\{\hat{m}(K)=m_{m^{*}}\right\}}
\end{aligned}
$$



(*) and (**) are due to the fact that models $(m)_{m \in \mathcal{M}}$ are nested and $m^{*} \in \mathcal{M}$. (***) is obtained since the crit $_{K}$ function is injective on $\mathcal{M}$. Finally, by taking the expectation, we obtain the FDR expression (3.1).

## Proof of Proposition 3.1.

Before proving Proposition 3.1, let us cite and prove two lemmas.

Lemma 6.1. For $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $\ell \in\{0, \cdots, r-1\}$ :

$$
\left\|Y-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|Y-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}=-\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}
$$

Lemma 6.2. For $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $\ell \in\{r+1, \cdots, q\}$ :

$$
\left\|Y-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|Y-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}=\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}
$$

Trade-off between prediction and FDR for variable selection

## Proof of Lemma 6.1.

For $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and $\ell \in\{0, \cdots, r-1\}$ :

$$
\begin{aligned}
& \left\|Y-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|Y-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}=\left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}+2\left\langle Y, X \hat{\beta}_{m_{\ell}}-X \hat{\beta}_{m_{r}}\right\rangle \\
& =\left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}+2\left\langle Y-X \hat{\beta}_{m_{r}}, X \hat{\beta}_{m_{\ell}}\right\rangle \\
& \quad-2\left\langle Y-X \hat{\beta}_{m_{r}}, X \hat{\beta}_{m_{r}}\right\rangle+2\left\langle X \hat{\beta}_{m_{r}}, X \hat{\beta}_{m_{\ell}}\right\rangle-2\left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2} \\
& =-\left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}+2\left\langle X \hat{\beta}_{m_{r}}, X \hat{\beta}_{m_{\ell}}\right\rangle=-\left\|X \hat{\beta}_{m_{r}}-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}
\end{aligned}
$$

The last line is due to the fact that $Y-X \hat{\beta}_{m_{r}} \in\left(m_{r}\right)^{\perp} \subset\left(m_{\ell}\right)^{\perp}$ since $m_{\ell} \subset m_{r}$ and $X \hat{\beta}_{m_{r}}$ is the projection of $Y$ onto $m_{r}$.

Then,

$$
\begin{aligned}
\left\|X \hat{\beta}_{m_{r}}-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2} & =\left\|\Pi_{m_{r}}(Y)-\Pi_{m_{\ell}}(Y)\right\|_{2}^{2} \\
& =\left\|\Pi_{\operatorname{Span}\left(X_{1}, \cdots, X_{r}\right)}(Y)-\Pi_{\operatorname{Span}\left(X_{1}, \cdots, X_{\ell}\right)}(Y)\right\|_{2}^{2} \\
& =\left\|\Pi_{\operatorname{Span}\left(u_{1}, \cdots, u_{r}\right)}(Y)-\Pi_{\mathrm{Span}\left(u_{1}, \cdots, u_{\ell}\right)}(Y)\right\|_{2}^{2} \\
& =\left\|\Pi_{\operatorname{Span}\left(u_{\ell+1}, \cdots, u_{r}\right)}(Y)\right\|_{2}^{2} \\
& =\left\|\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle u_{k}\right\|_{2}^{2} \\
& =\sum_{\left({ }^{* *}\right)}^{r}\left\langle Y, u_{k}\right\rangle^{2}
\end{aligned}
$$

(*) come from the definition of $\left(u_{1}, \cdots, u_{n}\right)$ and $(* *)$ is obtained by Parseval's identity.

Proof of Lemma 6.2.

For $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and $l \in\{r+1, \cdots, q\}$ :

$$
\begin{aligned}
\left\|Y-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|Y-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}= & \left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}+2\left\langle Y, X \hat{\beta}_{m_{\ell}}-X \hat{\beta}_{m_{r}}\right\rangle \\
= & \left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}+2\left\langle Y-X \hat{\beta}_{m_{\ell}}, X \hat{\beta}_{m_{\ell}}\right\rangle \\
& -2\left\langle Y-X \hat{\beta}_{m_{\ell}}, X \hat{\beta}_{m_{r}}\right\rangle+2\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2} \\
& -2\left\langle X \hat{\beta}_{m_{\ell}}, X \hat{\beta}_{m_{r}}\right\rangle \\
= & \left\|X \hat{\beta}_{m_{r}}\right\|_{2}^{2}+\left\|X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}-2\left\langle X \hat{\beta}_{m_{\ell}}, X \hat{\beta}_{m_{r}}\right\rangle \\
= & \left\|X \hat{\beta}_{m_{\ell}}-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}
\end{aligned}
$$

(*) is due to the fact that $Y-X \hat{\beta}_{m_{\ell}} \in\left(m_{\ell}\right)^{\perp} \subset\left(m_{r}\right)^{\perp}$ since $m_{r} \subset m_{\ell}$, and $X \hat{\beta}_{m_{\ell}}$ is the projection of $Y$ onto $m_{\ell}$. Then,

$$
\begin{aligned}
\left\|X \hat{\beta}_{m_{\ell}}-X \hat{\beta}_{m_{r}}\right\|_{2}^{2} & =\left\|\Pi_{m_{\ell}}(Y)-\Pi_{m_{r}}(Y)\right\|_{2}^{2} \\
& =\left\|\Pi_{\operatorname{Span}\left(X_{1}, \cdots, X_{\ell}\right)}(Y)-\Pi_{\operatorname{Span}\left(X_{1}, \cdots, X_{r}\right)}(Y)\right\|_{2}^{2} \\
& =\left\|\Pi_{\operatorname{span}\left(u_{1}, \cdots, u_{\ell}\right)}(Y)-\Pi_{\operatorname{Span}\left(u_{1}, \cdots, u_{r}\right)}(Y)\right\|_{2}^{2} \\
& =\left\|\Pi_{\operatorname{Span}\left(u_{r+1}, \cdots, u_{\ell}\right)}(Y)\right\|_{2}^{2} \\
& =\left\|\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle u_{k}\right\|_{2}^{2} \\
& =\sum_{(*=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}
\end{aligned}
$$

(*) come from the definition of $\left(u_{1}, \cdots, u_{n}\right)$ and (**) is obtained by Parseval's identity.

## Proof of Proposition 3.1.

Starting from (3.1), we decompose the event $\left\{\underset{\substack{\ell=0 \\ \ell \neq r}}{q}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\}$ by the intersection of these two events $\left\{\bigcap_{\ell=0}^{r-1}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\}$ and $\left\{\underset{\ell=r+1}{q}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\}$.

By using the definition of the $\operatorname{crit}_{K}$ function, we have for $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and $\ell \in\{0, \cdots, r-1, r+1, \cdots, q\}$ :

$$
\begin{aligned}
\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\} & =\left\{\left\|Y-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}+K \sigma^{2} r<\left\|Y-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}+K \sigma^{2} \ell\right\} \\
& =\left\{\left\|Y-X \hat{\beta}_{m_{r}}\right\|_{2}^{2}-\left\|Y-X \hat{\beta}_{m_{\ell}}\right\|_{2}^{2}<K \sigma^{2}(\ell-r)\right\}
\end{aligned}
$$

So, by applying Lemma $6.1, \ell \in\{0, \cdots, r-1\}$ :

$$
\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}=\left\{\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}>K \sigma^{2}(r-\ell)\right\}
$$

and by applying Lemma $6.2, \ell \in\{r+1, \cdots, q\}$ :

$$
\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}=\left\{\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}<K \sigma^{2}(\ell-r)\right\}
$$

In this way, $\left\{\underset{\substack{\ell=0 \\ \ell \neq r}}{q}\left\{\operatorname{crit}_{K}\left(m_{r}\right)<\operatorname{crit}_{K}\left(m_{\ell}\right)\right\}\right\}$ is decomposed by two events :

$$
\left\{\underset{\ell=0}{r-1}\left\{\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}>K \sigma^{2}(r-\ell)\right\}\right\} \cap\left\{\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}<K \sigma^{2}(\ell-r)\right\}\right\}
$$

Let us define $U$ the $n \times n$ matrix such that $u_{k}$ is the $k-$ th column of $U$. Since $\varepsilon \sim \mathcal{N}\left(0, \sigma^{2} I_{n}\right)$ and $\left(u_{1}, \cdots, u_{n}\right)$ is an orthonormal basis of $\mathbb{R}^{n}$, we get $U^{T} \varepsilon=\left(\left\langle\varepsilon, u_{1}\right\rangle, \cdots,\left\langle\varepsilon, u_{n}\right\rangle\right)^{T} \sim \mathcal{N}\left(0, \sigma^{2} U I_{n} U^{T}\right)=\mathcal{N}\left(0, \sigma^{2} I_{n}\right)$. Hence, random variables $\left(\left\langle Y, u_{i}\right\rangle\right)_{i \in\{1, \cdots, n\}}$ are independent with $\left\langle Y, u_{i}\right\rangle \sim \mathcal{N}\left(\left\langle X \beta^{*}, u_{i}\right\rangle, \sigma^{2}\right)$ for all $i$ in $\{1, \cdots, n\}$. Since the first event of the previous decomposition depends only on random variables $\left\langle Y, u_{i}\right\rangle$ for $i \in\{1, \cdots, r-1\}$ whereas the second one depends only on random variables $\left\langle Y, u_{i}\right\rangle$ for $i \in\{r+1, \cdots, q\}$, the two events are independent. Hence, from (3.1), we obtain for all $K>0$ :

$$
\begin{aligned}
\operatorname{FDR}(\hat{m}(K))=\sum_{r=D_{m^{*}}+1}^{q} \frac{r-D_{m^{*}}}{r} & \mathbb{P}\left(\bigcap_{\ell=0}^{r-1}\left\{\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}>K \sigma^{2}(r-\ell)\right\}\right) \\
\times & \mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}<K \sigma^{2}(\ell-r)\right\}\right)
\end{aligned}
$$

Moreover, since $\left\langle X \beta^{*}, u_{k}\right\rangle=0, \forall k>D_{m^{*}}$ and since $r \geq D_{m^{*}}+1$, we have :

$$
\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}=\sum_{k=\ell+1}^{r}\left\langle\varepsilon, u_{k}\right\rangle^{2}
$$

So, for all $K>0$ and for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ :

$$
\begin{gathered}
\mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}<K \sigma^{2}(\ell-r)\right\}\right)=\mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell} \tilde{Z}_{k}^{2}<K \sigma^{2}(\ell-r)\right\}\right) \\
\text { where } \tilde{Z}_{k} \stackrel{i . i . d .}{\sim} \mathcal{N}\left(0, \sigma^{2}\right) \\
\mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}<K \sigma^{2}(\ell-r)\right\}\right)=\mathbb{P}\left(\underset{\ell=r+1}{q}\left\{\sum_{k=r+1}^{\ell} Z_{k}^{2}<K(\ell-r)\right\}\right) \\
\text { where } Z_{k} \stackrel{i . i . d .}{\sim} \mathcal{N}(0,1)
\end{gathered}
$$

Trade-off between prediction and FDR for variable selection

Hence, for all $K>0$ and for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$,

$\mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell}\left\langle Y, u_{k}\right\rangle^{2}<K \sigma^{2}(\ell-r)\right\}\right)$ does not depend on the data and we deduce the Formula (3.2) with :

$$
\begin{aligned}
P_{r}(K) & =\mathbb{P}\left(\bigcap_{\ell=r+1}^{q}\left\{\sum_{k=r+1}^{\ell} Z_{k}^{2}<K(\ell-r)\right\}\right) \\
Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) & =\mathbb{P}\left(\bigcap_{\ell=0}^{r-1}\left\{\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}>K \sigma^{2}(r-\ell)\right\}\right)
\end{aligned}
$$

where $Z_{k} \stackrel{i . i . d .}{\sim} \mathcal{N}(0,1), \forall k \in\{r+1, \cdots, q\}$.

### 6.2 General bounds.

## Proof of Theorem 3.2.

We start from (3.2).

## - bounds on the $Q_{r}$ terms.

For all $K>0$ and for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$, we recall that :

$$
Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)=\mathbb{P}\left(\bigcap_{\ell=0}^{r-1}\left\{\sum_{k=\ell+1}^{r}\left\langle Y, u_{k}\right\rangle^{2}>K \sigma^{2}(r-\ell)\right\}\right)
$$

and since $\left\langle X \beta^{*}, u_{k}\right\rangle=0, \forall k>D_{m^{*}}$, we have :

$$
\begin{aligned}
& Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \\
& =\mathbb{P}\left(\bigcap_{\ell=0}^{r-1}\left\{\sum_{k=\ell+1}^{r}\left(\left\langle\varepsilon, u_{k}\right\rangle^{2} \mathbb{1}_{k>D_{m^{*}}}+\left\langle Y, u_{k}\right\rangle^{2} \mathbb{1}_{k \leq D_{m^{*}}}\right)>K \sigma^{2}(r-\ell)\right\}\right) \\
& =\mathbb{P}\left(\left\{\left\langle\varepsilon, u_{r}\right\rangle^{2}>K \sigma^{2}\right\} \cap \cdots \cap\left\{\left\langle\varepsilon, u_{r}\right\rangle^{2}+\cdots+\left\langle\varepsilon, u_{D_{m^{*}}+1}\right\rangle^{2}>K \sigma^{2}\left(r-D_{m^{*}}\right)\right\}\right. \\
& \cap\left\{\left\langle\varepsilon, u_{r}\right\rangle^{2}+\cdots+\left\langle\varepsilon, u_{D_{m^{*}+1}}\right\rangle^{2}+\left\langle Y, u_{D_{m^{*}}}\right\rangle^{2}>K \sigma^{2}\left(r-D_{m^{*}}+1\right)\right\} \cap \cdots \\
& \left.\cap\left\{\left\langle\varepsilon, u_{r}\right\rangle^{2}+\cdots+\left\langle\varepsilon, u_{D_{m^{*}+1}}\right\rangle^{2}+\left\langle Y, u_{D_{m^{*}}}\right\rangle^{2}+\cdots+\left\langle Y, u_{1}\right\rangle^{2}>K \sigma^{2} r\right\}\right) \\
& =\mathbb{P}\left(\left\{c_{r}>K \sigma^{2}\right\} \cap\left\{c_{r}+c_{r-1}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{r}+c_{r-1}+\cdots+c_{1}>r K \sigma^{2}\right\}\right)
\end{aligned}
$$

where $c_{\ell}=\left\langle Y, u_{\ell}\right\rangle^{2}$ for $\ell \in\left\{1, \cdots D_{m^{*}}\right\}$ and $c_{\ell}=\left\langle\varepsilon, u_{\ell}\right\rangle^{2}$ for $\ell \in\left\{D_{m^{*}}+1, \cdots, r\right\}$.

Lower bound on $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ for $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ :

Lemma 6.3. Let us consider an integer $s>1, K>0$ and $c_{1}, \cdots, c_{s} s$ non-negative random independent quantities. We define by $E_{\ell}$ the event $\left\{c_{\ell}>\ell K \sigma^{2}\right\}$ for $\ell \in\{1, \cdots, s\}$ and by $F_{\ell}$ the event $\left\{K \sigma^{2}<c_{\ell} \leq \ell K \sigma^{2}\right\}$ for $\ell \in\{2, \cdots, s\}$. Then :

$$
\begin{aligned}
& \left\{c_{s}>K \sigma^{2}\right\} \cap\left\{c_{s}+c_{s-1}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s}+c_{s-1}+\cdots+c_{1}>s K \sigma^{2}\right\} \\
& \supseteq E_{s} \sqcup\left(F_{s} \sqcap\left(E_{s-1} \sqcup\left(F_{s-1} \sqcap\left(E_{s-2} \sqcup \cdots \sqcup\left(F_{3} \sqcap\left(E_{2} \sqcup\left(F_{2} \sqcap E_{1}\right)\right)\right)\right)\right)\right),\right.
\end{aligned}
$$

where $\cap$ and $\sqcap$ design respectively any intersection and a disjoint intersection of events, as well as $\cup$ and $\sqcup$ designing respectively any union and a disjoint union of events.

Proof. We prove Lemma 6.3 by a recurrence on $s \geq 1$.

For $s=1$, both sets correspond to $E_{1}$, so the inclusion is obvious. Let $s \geq 1$ and suppose that the inclusion is true for $s$.

Trade-off between prediction and FDR for variable selection

With the definitions of $E_{s+1}$ and $F_{s+1}$, we obtain :

$$
\begin{aligned}
& \left\{c_{s+1}>K \sigma^{2}\right\} \cap\left\{c_{s+1}+c_{s}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s+1}+c_{s}+\cdots+c_{1}>(s+1) K \sigma^{2}\right\} \\
& =\left(E_{s+1} \sqcup F_{s+1}\right) \\
& \cap\left(\left\{c_{s+1}+c_{s}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s+1}+c_{s}+\cdots+c_{1}>(s+1) K \sigma^{2}\right\}\right) \\
& =\left(E_{s+1} \cap\left(\left\{c_{s+1}+c_{s}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s+1}+c_{s}+\cdots+c_{1}>(s+1) K \sigma^{2}\right\}\right)\right) \\
& \sqcup\left(F_{s+1} \cap\left(\left\{c_{s+1}+c_{s}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s+1}+c_{s}+\cdots+c_{1}>(s+1) K \sigma^{2}\right\}\right)\right) \\
& \underset{\left({ }^{*}\right)}{=} E_{s+1} \\
& \sqcup\left(F_{s+1} \cap\left(\left\{c_{s+1}+c_{s}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s+1}+c_{s}+\cdots+c_{1}>(s+1) K \sigma^{2}\right\}\right)\right) \\
& \underset{(* *)}{\supsetneq} E_{s+1} \sqcup\left(F_{s+1}\right. \\
& \left.\cap\left(\left\{c_{s}>K \sigma^{2}\right\} \cap\left\{c_{s}+c_{s-1}>2 K \sigma^{2}\right\} \cap \cdots \cap\left\{c_{s}+c_{s-1}+\cdots+c_{1}>s K \sigma^{2}\right\}\right)\right) \\
& \underset{(\text { ***) }}{\supseteq} E_{s+1} \sqcup\left(F_{s+1} \cap\left(E_{s} \sqcup\left(F_{s} \sqcap\left(E_{s-1} \sqcup \cdots \sqcup\left(F_{3} \sqcap\left(E_{3} \sqcup\left(F_{2} \sqcap E_{1}\right)\right)\right)\right)\right)\right)\right) \\
& \underset{(* * * *)}{\supset} E_{s+1} \sqcup\left(F_{s+1} \sqcap\left(E_{s} \sqcup\left(F_{s} \sqcap\left(E_{s-1} \sqcup \cdots \sqcup\left(F_{3} \sqcap\left(E_{3} \sqcup\left(F_{2} \sqcap E_{1}\right)\right)\right)\right)\right)\right)\right) .
\end{aligned}
$$

(*) is true since $c_{i}$ are non-negative for all $i \in\{1, \cdots, s+1\}$ providing that $E_{s+1} \subset\left(\left\{c_{s+1}+c_{s}>2 K \sigma^{2}\right\} \cap \cdots \cap\right.$ $\left.\left\{c_{s+1}+c_{s}+\cdots+c_{1}>(s+1) K \sigma^{2}\right\}\right),(* *)$ comes from the inclusion $\left\{c_{s+1}>K \sigma^{2}\right\} \subset F_{s+1}$. We obtain (***) by applying the recurrence assumption at the step $s$. Independence of $c_{1}, \cdots, c_{s+1}$ provides the independence between $F_{s+1}$ and $\left(E_{s} \sqcup\left(F_{s} \sqcap\left(E_{s-1} \sqcup \cdots \sqcup\left(F_{3} \sqcap\left(E_{3} \sqcup\left(F_{2} \sqcap E_{1}\right)\right)\right)\right)\right)\right)$ which gets (****).

Thus, the property is true for $s+1$, which proves lemma.

By applying Lemma 6.3 on Formula (6.1) with $s=r$, we obtain :

$$
\begin{aligned}
& Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \geq \mathbb{P}\left(E_{r}\right) \\
& \quad+\mathbb{P}\left(F_{r}\right)\left(\mathbb{P}\left(E_{r-1}\right)+\mathbb{P}\left(F_{r-1}\right)\left(\mathbb{P}\left(E_{r-2}\right)+\cdots+\mathbb{P}\left(F_{3}\right)\left(\mathbb{P}\left(E_{2}\right)+\mathbb{P}\left(F_{2}\right) \mathbb{P}\left(E_{1}\right)\right)\right)\right)
\end{aligned}
$$

By using that $\left\langle Y, u_{\ell}\right\rangle \sim \mathcal{N}\left(\left\langle X \beta^{*}, u_{\ell}\right\rangle, \sigma^{2}\right)$ for $\ell \in\left\{1, \cdots, D_{m^{*}}\right\}$ and $\left\langle\varepsilon, u_{\ell}\right\rangle \in \mathcal{N}\left(0, \sigma^{2}\right)$ for $\ell \in\{1, \cdots, r\}$, we get : For $\ell \in\left\{1, \cdots, D_{m^{*}}\right\}$ :

$$
\begin{aligned}
\mathbb{P}\left(E_{\ell}\right) & =\mathbb{P}\left(\left\{\left\langle Y, u_{\ell}\right\rangle^{2}>\ell K \sigma^{2}\right\}\right) \\
& =2-\left(\Phi\left(\sqrt{\ell K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)\right) \\
& =G_{\ell}
\end{aligned}
$$

Trade-off between prediction and FDR for variable selection

For $\ell \in\left\{2, \cdots, D_{m^{*}}\right\}$ :

$$
\begin{aligned}
\mathbb{P}\left(F_{\ell}\right)= & \mathbb{P}\left(\left\{K \sigma^{2}<\left\langle Y, u_{\ell}\right\rangle^{2} \leq \ell K \sigma^{2}\right\}\right) \\
= & \Phi\left(\sqrt{\ell K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right) \\
& \quad-\left(\Phi\left(\sqrt{K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)\right) \\
= & H_{\ell}
\end{aligned}
$$

For $\ell \in\left\{D_{m^{*}}+1, \cdots, r\right\}:$

$$
\begin{aligned}
\mathbb{P}\left(E_{\ell}\right) & =\mathbb{P}\left(\left\{\left\langle\varepsilon, u_{\ell}\right\rangle^{2}>\ell K \sigma^{2}\right\}\right) \\
& =2(1-\Phi(\sqrt{\ell K})) \\
& =G_{\ell} \\
\mathbb{P}\left(F_{\ell}\right) & =\mathbb{P}\left(\left\{K \sigma^{2}<\left\langle\varepsilon, u_{\ell}\right\rangle^{2} \leq \ell K \sigma^{2}\right\}\right) \\
& =2(\Phi(\sqrt{\ell K})-\Phi(\sqrt{K})) \\
& =H_{\ell}
\end{aligned}
$$

Hence, a lower bound on $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ is obtained for all $K>0$ :

$$
\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right) \leq Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)
$$

with :

$$
\begin{gathered}
\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)=G_{r}+H_{r} \underline{f}_{r-1}\left(K, \beta^{*}, \sigma^{2}\right) \\
\text { and } \underline{f}_{1}\left(K, \beta^{*}, \sigma^{2}\right)=G_{1}
\end{gathered}
$$

Upper bound on $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ for $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ :

By using definitions of Lemma 6.3 and formula (6.1), we get :

$$
\begin{gathered}
Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \leq \min \left(\mathbb{P}\left(\left\{c_{r}>K \sigma^{2}\right\}\right), \mathbb{P}\left(\left\{c_{r}+c_{r-1}>2 K \sigma^{2}\right\}\right), \cdots\right. \\
\left.\mathbb{P}\left(\left\{c_{r}+c_{r-1}+\cdots+c_{1}>r K \sigma^{2}\right\}\right)\right)
\end{gathered}
$$

Since $\left\langle\varepsilon, u_{i}\right\rangle_{i \in\left\{D_{m^{*}}+1, \cdots, r\right\}} \stackrel{\text { i.i.d. }}{\sim} \mathcal{N}\left(0, \sigma^{2}\right)$, we have for all $j \in\left\{D_{m^{*}}+1, \cdots, r\right\}$ :

$$
\mathbb{P}\left(\left\{c_{r}+\cdots+c_{j}>(r-j+1) K \sigma^{2}\right\}\right)=1-F_{\chi^{2}(r-j+1)}((r-j+1) K)
$$

Trade-off between prediction and FDR for variable selection

For all $j \in\left\{1, \cdots, D_{m^{*}}\right\}$,

$$
\begin{aligned}
& \mathbb{P}\left(\left\{c_{r}+\cdots+c_{j}>(r-j+1) K \sigma^{2}\right\}\right) \\
& =\mathbb{P}\left(\left\{c_{r}+\cdots+c_{D_{m^{*}}+1}+c_{D_{m^{*}}}+\cdots+c_{j}>(r-j+1) K \sigma^{2}\right\}\right) \\
& =\mathbb{P}\left(\left\{c_{r}+\cdots+c_{D_{m^{*}}+1}+\left(\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle+\left\langle\varepsilon, u_{D_{m^{*}}}\right\rangle\right)^{2}+\cdots\right.\right. \\
& \left.\left.+\left(\left\langle X \beta^{*}, u_{j}\right\rangle+\left\langle\varepsilon, u_{j}\right\rangle\right)^{2}>(r-j+1) K \sigma^{2}\right\}\right) \\
& \underset{\left({ }^{(* *)}\right.}{\leq} \mathbb{P}\left(\left\{c_{r}+\cdots+c_{D_{m^{*}+1}}+2\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}+2\left\langle\varepsilon, u_{D_{m^{*}}}\right\rangle^{2}+\cdots\right.\right. \\
& \left.\left.+2\left\langle X \beta^{*}, u_{j}\right\rangle^{2}+2\left\langle\varepsilon, u_{j}\right\rangle^{2}>(r-j+1) K \sigma^{2}\right\}\right) \\
& \leq \mathbb{P}\left(\left\{2 c_{r}+\cdots+2 c_{D_{m^{*}}+1}+2\left\langle\varepsilon, u_{D_{m^{*}}}\right\rangle^{2}+\cdots+2\left\langle\varepsilon, u_{j}\right\rangle^{2}>(r-j+1) K \sigma^{2}\right.\right. \\
& \left.\left.-2\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}-\cdots-2\left\langle X \beta^{*}, u_{j}\right\rangle^{2}\right\}\right) \\
& \underset{\left({ }^{* * *}\right)}{=} \mathbb{P}\left(\left\{2 \sigma^{2} Z_{r}^{2}+\cdots+2 \sigma^{2} Z_{D_{m^{*}+1}}^{2}+2 \sigma^{2} Z_{D_{m^{*}}}^{2}+\cdots+2 \sigma^{2} Z_{j}^{2}\right.\right. \\
& \left.\left.>(r-j+1) K \sigma^{2}-2\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}-\cdots-2\left\langle X \beta^{*}, u_{j}\right\rangle^{2}\right\}\right) \\
& \text { where }\left(Z_{\ell}\right)_{\ell \in\{j, \cdots, r\}} \stackrel{i . i . d}{\sim} \mathcal{N}(0,1) \\
& =\mathbb{P}\left(\left\{Z_{r}^{2}+\cdots+Z_{D_{m^{*}+1}}^{2}+Z_{D_{m^{*}}}^{2}+\cdots+Z_{j}^{2}\right.\right. \\
& \left.\left.>\frac{(r-j+1) K}{2}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}}{\sigma^{2}}-\cdots-\frac{\left\langle X \beta^{*}, u_{j}\right\rangle^{2}}{\sigma^{2}}\right\}\right) \\
& =\mathbb{P}\left(\left\{X>\frac{(r-j+1) K}{2}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}}{\sigma^{2}}-\cdots-\frac{\left\langle X \beta^{*}, u_{j}\right\rangle^{2}}{\sigma^{2}}\right\}\right) \\
& \text { for } X \sim \chi^{2}(r-j+1) \\
& =1-F_{\chi^{2}(r-j+1)}\left(\frac{(r-j+1) K}{2}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}}{\sigma^{2}}-\cdots-\frac{\left\langle X \beta^{*}, u_{j}\right\rangle^{2}}{\sigma^{2}}\right)
\end{aligned}
$$

$(* *)$ provides from $(a+b)^{2} \leq 2\left(a^{2}+b^{2}\right), \forall(a, b) \in \mathbb{R}$ and $(* * *)$ is true since $\left\langle\varepsilon, u_{i}\right\rangle_{i \in\{1, \cdots, r\}} \stackrel{\text { i.i.d. }}{\sim} \mathcal{N}\left(0, \sigma^{2}\right)$.

So, from (6.4), (6.5) and (6.6), we deduce that for all $K>0$ and for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ :

$$
\begin{aligned}
& Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \leq \\
& \quad \min \left(1-F_{\chi^{2}(1)}(K), \cdots, 1-F_{\chi^{2}\left(r-D_{m^{*}}\right)}\left(\left(r-D_{m^{*}}\right) K\right)\right. \\
& \quad 1-F_{\chi^{2}\left(r-D_{m^{*}}+1\right)}\left(\frac{\left(r-D_{m^{*}}+1\right) K}{2}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}}{\sigma^{2}}\right) \\
& \quad 1-F_{\chi^{2}\left(r-D_{m^{*}+2}\right.}\left(\frac{\left(r-D_{m^{*}}+2\right) K}{2}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}}{\sigma^{2}}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}-1}}\right\rangle^{2}}{\sigma^{2}}\right) \\
& \quad \cdots, \\
& \\
& \left.\quad 1-F_{\chi^{2}(r)}\left(\frac{r K}{2}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}}}\right\rangle^{2}}{\sigma^{2}}-\frac{\left\langle X \beta^{*}, u_{D_{m^{*}-1}}\right\rangle^{2}}{\sigma^{2}}-\cdots-\frac{\left\langle X \beta^{*}, u_{1}\right\rangle^{2}}{\sigma^{2}}\right)\right)
\end{aligned}
$$

Trade-off between prediction and FDR for variable selection

Hence, an upper bound on $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ is obtained for all $K>0$ :

$$
\left.Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \leq \bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
$$

with :

$$
\begin{aligned}
\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)=1-\max & \left(\max _{\ell \in\left\{1, \cdots, r-D_{\left.m^{*}\right\}}\right.}\left(F_{\chi^{2}(\ell)}(\ell K)\right)\right. \\
& \left.\max _{\ell \in\left\{r-D_{\left.m^{*}+1, \cdots, r\right\}}\right.}\left(F_{\chi^{2}(\ell)}\left(\frac{\ell K}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)\right)\right)
\end{aligned}
$$

- bounds on the FDR.

By combining (3.2), (6.2), (6.3), (6.7), (6.8) and (3.3), we obtain :

$$
\sum_{r=D_{m^{*}}+1}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right) \leq \operatorname{FDR}(\hat{m}(K))
$$

and

$$
\operatorname{FDR}(\hat{m}(K)) \leq \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
$$

which allows us to obtain Theorem 3.2 with $\forall K>0$,

$$
b\left(K, \beta^{*}, \sigma^{2}\right)=\sum_{r=D_{m^{*}}+1}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
$$

and

$$
B\left(K, \beta^{*}, \sigma^{2}\right)=\sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
$$

### 6.3 Strictly positive FDR.

Proof of Corollary 3.3.

From Theorem 3.2, we have $\forall K>0$,

$$
\operatorname{FDR}(\hat{m}(K)) \geq \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
$$

For the rest of the proof, we use the following Lemma :

Lemma 6.4 (Frank R. Kschischang [52]). The complementary error function, $\operatorname{erfc}(x)$, is defined, for $x \geq 0$, as :

$$
\operatorname{erfc}(x)=2\left(1-F_{\mathcal{N}\left(0, \frac{1}{2}\right)}(x)\right)
$$

where $F_{\mathcal{N}\left(0, \frac{1}{2}\right)}$ designs the cumulative function of the centered Gaussian with the variance equals $\frac{1}{2}$. Then,

$$
\forall x \geq 0, \quad \frac{2 e^{-x^{2}}}{\sqrt{\pi}\left(x+\sqrt{x^{2}+2}\right)} \leq \operatorname{erfc}(x) \leq \frac{e^{-x^{2}}}{\sqrt{\pi} x}
$$

Trade-off between prediction and FDR for variable selection

We remark that for all $x \geq 0,1-\Phi(x)=\frac{1}{2} \operatorname{erfc}\left(\frac{x}{\sqrt{2}}\right)$. Then, for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$,

$$
\begin{aligned}
\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right) & =G_{r}+H_{r}\left(G_{r-1}+H_{r-1}\left(G_{r-2}+\cdots+H_{2} G_{1}\right)\right) \\
& \geq G_{r} \\
& =2(1-\Phi(\sqrt{r K})) \\
& =\operatorname{ercf}\left(\sqrt{\frac{r K}{2}}\right) \\
& \geq \frac{2}{\left({ }^{(* *)}\right.} \sqrt{\sqrt{\pi}\left(\sqrt{\frac{r K}{2}}+\sqrt{\frac{r K}{2}+2}\right)} e^{-\frac{r K}{2}} \\
& =\frac{2 \sqrt{2}}{\sqrt{\pi}(\sqrt{r K}+\sqrt{r K+4})} e^{-\frac{r K}{2}}
\end{aligned}
$$

(**) is provided by Lemma 6.4. So, from (6.9) and (6.10), we obtain :

$$
\forall K>0, \quad \operatorname{FDR}(\hat{m}(K)) \geq \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} P_{r}(K) \frac{2 \sqrt{2}}{\sqrt{\pi}(\sqrt{r K}+\sqrt{r K+4})} e^{-\frac{r K}{2}}\right)
$$

This lower bound is strictly positive and since the $P_{r}(K)$ terms are all strictly positive too, we deduce that the FDR function is a strictly positive function.

### 6.4 Asymptotic analysis.

## Proof of Corollary 3.4.

For all $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and by using the definitions from Theorem 3.2, for $\ell \in\left\{1, \cdots, D_{m^{*}}\right\}$ :

$$
\begin{gathered}
\left.G_{\ell}=2-\left(\Phi\left(\sqrt{\ell K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right\rangle\right)+\Phi\left(\sqrt{\ell K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)\right) \\
K \longrightarrow+\infty
\end{gathered}
$$

for $\ell \in\left\{2, \cdots, D_{m^{*}}\right\}$ :

$$
\begin{gathered}
H_{\ell}=\Phi\left(\sqrt{\ell K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{\ell K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)- \\
\left(\Phi\left(\sqrt{K}-\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)+\Phi\left(\sqrt{K}+\frac{\left\langle X \beta^{*}, u_{\ell}\right\rangle}{\sigma}\right)\right) \\
K \longrightarrow 0
\end{gathered}
$$

and for $\ell \in\left\{D_{m^{*}}+1, \cdots, r\right\}$ :

$$
\begin{aligned}
& G_{\ell}=2(1-\Phi(\sqrt{\ell K}))_{K \longrightarrow+\infty} 0 \\
& H_{\ell}=2(\Phi(\sqrt{\ell K})-\Phi(\sqrt{K}))_{K \longrightarrow+\infty} 0
\end{aligned}
$$

which provides that $\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right) \underset{K \longrightarrow+\infty}{\longrightarrow} 0$.

Moreover, $\left.\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right) \underset{K \longrightarrow+\infty}{\longrightarrow} 0$. So, $Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \underset{K \longrightarrow+\infty}{\longrightarrow} 0$. In the same way, $P_{r}(K) \underset{K \longrightarrow+\infty}{\longrightarrow}$. So, $P_{r}(K) Q_{r}\left(K, \beta^{*}, \sigma^{2}\right) \underset{K \longrightarrow+\infty}{\longrightarrow} 0$.

Finally, for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$, we deduce from (3.2) that

$$
\operatorname{FDR}(\hat{m}(K)) \underset{K \longrightarrow+\infty}{\longrightarrow} 0
$$

Trade-off between prediction and FDR for variable selection

For each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\} P_{r}(K) \underset{K \longrightarrow+\infty}{\longrightarrow} 1$, we deduce that for all $\left.C_{1} \in\right] 0,1\left[\right.$, there exists $\tilde{L}_{C_{1}}>0$ such that $\forall K>\tilde{L}_{C_{1}}$ and $\forall r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$, we have $C_{1} \leq P_{r}(K)$. For the following, we fix $\left.C_{1} \in\right] 0,1[$. By using (6.2), (6.7) and $P_{r}(K) \leq 1$ for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$, we deduce that :

$$
\forall K>\tilde{L}_{C_{1}}, \quad \operatorname{FDR}(\hat{m}(K)) \geq C_{1} \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} \underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)
$$

and

$$
\left.\forall K>0, \quad \operatorname{FDR}(\hat{m}(K)) \leq \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} \bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)\right)
$$

## - Upper bound on $\bar{f}_{r}$ :

For each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $K>0$ :

$$
\begin{aligned}
&\left.\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right)= 1-\max \left(\max _{\ell \in\left\{1, \cdots, r-D_{\left.m^{*}\right\}}\right.}\left(F_{\chi^{2}(\ell)}(\ell K)\right)\right. \\
&\left.\max _{\ell \in\left\{r-D_{\left.m^{*}+1, \cdots, r\right\}}\right.}\left(F_{\chi^{2}(\ell)}\left(\frac{\ell K}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)\right)\right) \\
&= \min \left(\min _{\ell \in\left\{1, \cdots, r-D_{\left.m^{*}\right\}}\right.}\left(\mathbb{P}\left(X_{\ell}>\ell K\right)\right)\right. \\
&\left.\min _{\ell \in\left\{r-D_{\left.m^{*}+1, \cdots, r\right\}}\right.}\left(\mathbb{P}\left(Y_{\ell}>\frac{\ell K}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)\right)\right) \\
&= \min \left(\min _{\ell \in\left\{1, \cdots, r-D_{m^{*}}\right\}}\left(\mathbb{P}\left(X_{\ell}-\ell>\ell K-\ell\right)\right)\right. \\
& \min _{\ell}(\ell) \text { and } Y_{\ell} \sim \chi^{2}(\ell) \\
&\left.\left(\mathbb{P}\left(Y_{\ell}-\ell>\frac{\ell(K-2)}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)\right)\right) \\
& \text { with } X_{\ell} \sim \chi^{2}(\ell) \text { and } Y_{\ell} \sim \chi^{2}(\ell) .
\end{aligned}
$$

So, for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $K>0$ :

$$
\left.\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)\right) \leq \min _{\ell \in\left\{1, \cdots, r-D_{m^{*}}\right\}}\left(\mathbb{P}\left(X_{\ell}-\ell>\ell K-\ell\right)\right), \quad \text { with } X_{\ell} \sim \chi^{2}(\ell)
$$

By the exponential inequality of [53] for $X \sim \chi^{2}(\ell)$ and $\ell \in \mathbb{N}^{*}$ :

$$
\forall x \geq 0, \quad \mathbb{P}(X-\ell>2 \sqrt{\ell x}+2 x) \leq e^{-x}
$$

We apply (6.14) for each $\ell=1, \cdots,\left(r-D_{m^{*}}\right)$ with $x=\frac{\ell}{4}(1-\sqrt{2 K-1})^{2}$ which is one solution of $2 \sqrt{\ell x}+2 x=$ $\ell K-\ell$ when $K>1$. We obtain for all $K>1$ :

$$
\begin{aligned}
\min _{\ell \in\left\{1, \cdots, r-D_{m^{*}}\right\}}\left(\mathbb{P}\left(X_{\ell}-\ell>\ell K-\ell\right)\right) & \leq \min _{\ell=1, \cdots,\left(r-D_{m^{*}}\right)}\left(e^{\left.-\frac{\ell}{4}(1-\sqrt{2 K-1})^{2}\right)}\right. \\
& \leq e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}} e^{-\frac{\left(r-D_{\left.m^{*}\right) K}\right.}{2}}
\end{aligned}
$$

Trade-off between prediction and FDR for variable selection

So, from (6.12) and (6.15), we obtain for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $K>1$ :

$$
\begin{aligned}
\operatorname{FDR}(\hat{m}(K)) & \leq \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}} e^{-\frac{\left(r-D_{\left.m^{*}\right) K}\right.}{2}}\right) \\
& \leq e^{-\frac{K}{2}} \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}}\right)
\end{aligned}
$$

For all $\eta>0$ and $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}, e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}}=\underset{K \xrightarrow{o}}{o}\left(e^{\eta K}\right)$.

Hence, $\forall \eta>0$

$$
\operatorname{FDR}(\hat{m}(K))=\underset{K \longrightarrow+\infty}{o}\left(e^{-K\left(\frac{1}{2}-\eta\right)}\right)
$$

which allows to obtain (3.6).

Proof of Remark 3.6 :


finest asymptotic upper bound (3.9), we start from the equation (6.13) and we consider the second term. Similar to previously, we apply (6.14) for each $\ell=r-D_{m^{*}}+1, \cdots, r$ with

$$
x=\frac{\ell}{4}\left(1-\sqrt{\left.K-1-\frac{2}{\ell} \sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)^{2}}\right.
$$

which is one solution of

$$
2 \sqrt{\ell x}+2 x=\frac{\ell(K-2)}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}
$$


leading to $\frac{1}{\sigma^{2}}=\underset{\sigma \xrightarrow{O}(K)}{ }(K)$ and so $\sigma^{2}(K-1) \longrightarrow+\infty$ when $K \longrightarrow+\infty$. We obtain for all $K>0$ such that $\sigma^{2}(K-1)>\frac{2}{r-D_{m^{*}}+1} \sum_{k=1}^{D_{m^{*}}}\left\langle X \beta^{*}, u_{k}\right\rangle^{2}+2:$

$$
\begin{aligned}
\min _{\ell \in\left\{r-D_{\left.m^{*}+1, \cdots, r\right\}}\right.} & \left.\left(\mathbb{P}\left(Y_{\ell}-\ell>\frac{\ell(K-2)}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right)\right)\right) \\
& \left.\leq \min _{\ell \in\left\{r-D_{\left.m^{*}+1, \cdots, r\right\}}\right.}\left(e^{-\frac{\ell}{4}\left(1-\sqrt{K-1-\frac{2}{\ell}} \sum_{k=r-\ell+1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}\right.}\right)^{2}\right) \\
& \leq e^{\frac{1}{2} \sum_{k=1}^{D_{m}^{*}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}} e^{\frac{r}{2} \sqrt{K-1-\frac{2}{r} \sum_{k=1}^{D_{m}^{*}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}}} e^{-\frac{r K}{4}}
\end{aligned}
$$

(*) come from the fact that a minimum into a set is smaller than any value in the set. We choose the value corresponding for $\ell=0$.

So, from (6.12), (6.15) and (6.16), we obtain for each $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}$ and for all $K>1$ respecting $\sigma^{2}(K-1)>$

Trade-off between prediction and FDR for variable selection

$$
\begin{aligned}
& \frac{2}{r-D_{m^{*}}+1} \sum_{k=1}^{D_{m^{*}}}\left\langle X \beta^{*}, u_{k}\right\rangle^{2}+2: \\
& \operatorname{FDR}(\hat{m}(K)) \leq \sum_{r=D_{m^{*}}+1}^{q}\left(\frac { r - D _ { m ^ { * } } } { r } \operatorname { m i n } \left(e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}} e^{-\frac{\left(r-D_{\left.m^{*}\right) K}\right.}{2}}\right.\right. \\
& \left.\left.e^{\frac{1}{2} \sum_{k=1}^{D_{m}^{*}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}} e^{\frac{r}{2}} \sqrt{K-1-\frac{2}{r} \sum_{k=1}^{D_{m}^{*}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}} e^{-\frac{r K}{4}}\right)\right) \\
& =\min \left(\sum_{r=D_{m^{*}}+1}^{q}\left(\frac{r-D_{m^{*}}}{r} e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}} e^{-\frac{\left(r-D_{m^{*}}\right) K}{2}}\right)\right.
\end{aligned}
$$



$$
\begin{aligned}
& \leq \min \left(e^{-\frac{K}{2}} \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}}\right)\right. \\
& \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} e^{\left.\frac{r}{2} \sqrt{K-1-\frac{2}{r} \sum_{k=1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}}\right)} e^{-\left(\frac{\left(D_{m^{*}}+1\right) K}{4}-\frac{1}{2 \sigma^{2}} \sum_{k=1}^{D_{m}^{*}}\left\langle X \beta^{*}, u_{k}\right\rangle^{2}\right)}\right)
\end{aligned}
$$

For all $\eta>0$ and $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}, e^{\frac{\left(r-D_{m^{*}}\right) \sqrt{2 K-1}}{2}}=\underset{K \xrightarrow{o}}{o}\left(e^{\eta K}\right)$, independently of the value of $\sigma^{2}$. Hence,



For all $r \in\left\{D_{m^{*}}+1, \cdots, q\right\}, e^{\frac{r}{2} \sqrt{K-1-\frac{2}{r} \sum_{k=1}^{D_{m^{*}}} \frac{\left\langle X \beta^{*}, u_{k}\right\rangle^{2}}{\sigma^{2}}}} \leq e^{\frac{r}{2} \sqrt{K}}$. Moreover, for all $\tilde{\eta}>0$ and $r \in$ $\left\{D_{m^{*}}+1, \cdots, q\right\}, e^{\frac{r}{2} \sqrt{K}}=\underset{K \xrightarrow{o}+\infty}{o}\left(e^{\tilde{\eta} K}\right)$, independently of the value of $\sigma^{2}$. Hence, the second term in (6.17) is


Hence,







- Lower bound on $\underline{f}_{r}$ :

From (6.10) and (6.11), we obtain :

$$
\begin{aligned}
\forall K>\tilde{L}_{C_{1}}, \operatorname{FDR}(\hat{m}(K)) & \geq C_{1} \sum_{r=D_{m^{*}+1}}^{q}\left(\frac{r-D_{m^{*}}}{r} \frac{2 \sqrt{2}}{\sqrt{\pi}(\sqrt{r K}+\sqrt{r K+4})} e^{-\frac{r K}{2}}\right) \\
& \geq C_{1} \frac{2 \sqrt{2}}{\sqrt{\pi}(\sqrt{q K}+\sqrt{q K+4})} \frac{1}{D_{m^{*}}+1} \sum_{r=D_{m^{*}+1}}^{q}\left(e^{-\frac{r K}{2}}\right) \\
& \geq C_{1} \frac{2 \sqrt{2}}{\sqrt{\pi}(\sqrt{q K}+\sqrt{q K+4})} \frac{1}{D_{m^{*}}+1} e^{-\frac{\left(D_{\left.m^{*}+1\right) K}\right.}{2}} \\
& =\frac{2 \sqrt{2} C_{1}}{\sqrt{\pi}\left(D_{m^{*}}+1\right)} \frac{1}{\sqrt{q K+\sqrt{q K+4}}} e^{-K \frac{\left(D_{\left.m^{*}+1\right)}^{2}\right.}{2}}
\end{aligned}
$$

(*) is true since each term in the sum is positive, so, the sum is larger than one of them.

For all $\eta>0, \exists \tilde{C}_{\eta}>0, \exists \tilde{L}_{\eta}>0$ such that $\forall K>\tilde{L}_{\eta}$, we have $\tilde{C}_{\eta} e^{-\eta K} \leq \frac{1}{\sqrt{q K}+\sqrt{q K+4}}$.

So,

$$
\begin{aligned}
& \forall \eta>0, \exists \tilde{C}_{\eta}>0, \exists \tilde{L}_{\eta}>0, \forall K>\max \left(\tilde{L}_{C_{1}}, \tilde{L}_{\eta}\right) \\
& \quad \operatorname{FDR}(\hat{m}(K)) \geq \frac{2 \sqrt{2} C_{1}}{\sqrt{\pi}\left(D_{m^{*}}+1\right)} \tilde{C}_{\eta} e^{-K\left(\frac{D_{m^{*}+1+2 \eta}}{2}\right)}
\end{aligned}
$$

which gives (3.7) with $C_{\eta}=\frac{2 \sqrt{2} C_{1}}{\sqrt{\pi}\left(D_{m^{*}}+1\right)} \tilde{C}_{\eta}$ and $L_{\eta}=\max \left(\tilde{L}_{C_{1}}, \tilde{L}_{\eta}\right)$.

Formula (3.8) automatically follows from (3.6) and (3.7).

### 6.5 General bounds.

Proof of Corollary 3.7.

By taking $u_{j}=X_{j}, \forall j \in\{1, \cdots, q\}$, then $\left(X_{1}, \cdots, X_{q}, u_{q+1}, \cdots, u_{n}\right)$ is an orthonormal basis of $\mathbb{R}^{n}$. Consequently, $\forall j \in\{1, \cdots, q\},\left\langle X \beta^{*}, u_{j}\right\rangle=\left\langle X \beta^{*}, X_{j}\right\rangle=\beta_{j}^{*}$, which concludes the proof.

## 7 Extensive simulation study to justify the observable estimations.

This section is a complement to Section 4 and presents an extensive simulation study.

### 7.1 Description of the simulation protocol

Description of the data simulation. Given values of $n$ and $p$, we simulate $Y \sim \mathcal{N}\left(\beta^{*}, I_{n}\right)$ where $\beta^{*}$ is a vector satisfying $\beta_{j}^{*} \geq \beta_{j+1}^{*}$ for all $j \in\left\{1, \cdots, D_{m^{*}-1}\right\}$ to get ordered active variables. We consider four scenarios, described in Table 4, where values of $D_{m^{*}}, \beta^{*}, n$ and $\sigma^{2}$ vary and where the number of variables $p$ is always equal to 50 .

The scenario (i) allows us to evaluate the impact of the sparsity of the parameter $\beta^{*}$. The scenario (ii) allows us to evaluate how the values of the non-zero coefficients in $\beta^{*}$ complicate the identification of the active variables. In particular, the non-zero coefficients are close and, in the second configuration, some of them are smaller than the noise level $\sigma$. The scenario (iii) allows us to evaluate the behavior of our method in a high-dimensional context through the variation of the number of observations $n$, either smaller, equal or larger than the number of variables $p$. The last scenario (iv) allows us to evaluate the impact of the noise amplitude through different values of $\sigma^{2}$.

Note that for a fair comparison, the datasets where $n=30$ in scenario (iii) are inlcuded in those where $n=50$ which are included in those where $n=300$. Moreover, for the sake of reproducibility, the seed of the random number generator is identically fixed for each scenario.

The toy data set. We call the toy data set the data set where $n=p=50, D_{m^{*}}=10, \beta_{10}^{*}=2$ and $\forall j \in\{1, \cdots, 9\}$, $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.5, \beta_{j+1}^{*}+1.5\right)$. It corresponds to the reference data set in all scenarios.

Empirical estimations. For the empirical estimations, we simulate $\mathcal{D}$ a set of 1000 data sets for each scenario. For each $d \in \mathcal{D}$ and for all $K>0$, the selected model $\hat{m}^{d}(K)$ is obtained from $\left(Y^{d}, X^{d}\right)$. Since $m^{*}$ is known, the quantity $\operatorname{FDP}\left(\hat{m}^{d}(K)\right)$ is calculable for each $d \in \mathcal{D}$ and the empirical estimator of $\operatorname{FDR}(\hat{m}(K))$ is the average of the $\operatorname{FDP}\left(\hat{m}^{d}(K)\right)$. Concerning PR, we simulate $\tilde{\mathcal{D}}$ a new set of 1000 data sets for each scenario. New $\tilde{Y}^{d}$ are generated on $\tilde{\mathcal{D}}$, from the model (1.1), and by using the $X^{d}$ on $\mathcal{D}$ to respect the fixed design assumption. The selected models $\hat{m}^{d}(K)$ and the $\hat{\beta}_{\hat{m}(K)}^{d}$ estimators are extracted by solving (2.2) from the training sets $\left(Y^{d}, X^{d}\right)$ on $\mathcal{D}$. The PR is evaluated from the validation sets $\left(\tilde{Y}^{d}, X^{d}\right)$ on $\tilde{\mathcal{D}}$ by the mean squared error :

$$
\operatorname{MSE}\left(\hat{m}^{d}(K)\right)=\frac{1}{n} \sum_{i=1}^{n}\left(\tilde{Y}_{i}^{d}-\sum_{j=1}^{p} x_{i j}^{d} \hat{\beta}_{\hat{m}^{d}(K)_{j}}\right)^{2}
$$

The empirical estimator of $\operatorname{PR}(\hat{m}(K))$ is the average of the $\operatorname{MSE}\left(\hat{m}^{d}(K)\right)$.

To validate the quality of the empirical estimations, the central limit theorem is applied to get the $95 \%$ asymptotic

Trade-off between prediction and FDR for variable selection

confidence intervals :

$$
\left[\operatorname{FDR}(\hat{m}(K))-1.96 \frac{\hat{\sigma}}{\sqrt{1000}}, \operatorname{FDR}(\hat{m}(K))+1.96 \frac{\hat{\sigma}}{\sqrt{1000}}\right]
$$

and

$$
\left[\operatorname{PR}(\hat{m}(K))-1.96 \frac{\hat{\sigma}}{\sqrt{1000}}, \operatorname{PR}(\hat{m}(K))+1.96 \frac{\hat{\sigma}}{\sqrt{1000}}\right]
$$

where $\hat{\sigma}$ is the unbiased empirical estimator of the standard deviation $\sigma$. Since their width do not exceed 0.011 and 0.07 for respectively the FDR and the PR, they are tight, meaning that the empirical estimations are close to the theoretical quantities $\operatorname{FDR}(\hat{m}(K))$ and $\operatorname{PR}(\hat{m}(K))$.

### 7.2 Estimation of the theoretical FDR

This subsection completes Subsection 4.1. We present the slope heuristic principle and an analyse of the $\hat{\sigma}^{2}$, obtained by the slope heuristics, is processed. Then, a large simulation study is performed to justify the choice of $\hat{\beta}_{\hat{m}(4)}$ to estimate $\beta^{*}$ in the upper bound of the FDR.

The FDR bounds of Theorem 3.2 depend on the $P_{r}$, the $\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ and the $\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ quantities. Concerning the $P_{r}$ quantities, they do not depend on the data as soon as $r$ is given. They can be estimated once and for all without any dataset. For each $1 \leq r \leq q, P_{r}$ is estimated by generating 5000 independent standard Gaussian vectors $\left(Z_{k}\right)_{k \in\{r+1, \cdots, q\}}$ and by counting for each vector the number of times that $Z_{k}^{2}<K(\ell-r)$ for each $\ell \in\{r+1, \cdots, q\}$.

| Scenario <br> with <br> $p=50$ | Active <br> variable <br> number | Non-zero coefficient amplitude <br> in $\beta^{*}$ | Number of <br> observa- <br> tions | Noise <br> amplitude |
| :---: | :---: | :---: | :---: | :---: |
| (i) <br> Sparsity | $D_{m^{*}} \in$ <br> $\{1,10,20\}$ | $\beta_{D_{m^{*}}}^{*}=2$, <br> $\forall j \in\left\{1, \cdots, D_{m^{*}}-1\right\}$ <br> $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.5, \beta_{j+1}^{*}+\right.$ <br> $1.5)$ | $n=50$ | $\sigma^{2}=1$ |
| (ii) <br> Com- <br> plexity | $D_{m^{*}}=$ <br> 10 | $\beta_{10}^{*}=2$ with <br> $\forall j \in\{1, \cdots, 9\}$ <br> $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.5, \beta_{j+1}^{*}+\right.$ <br> $1.5)$ <br> $\beta_{10}^{*}=\frac{2}{10}$ with <br> $\forall j \in\{1, \cdots, 9\}$ <br> $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.05, \beta_{j+1}^{*}+\right.$ <br> $0.15)$ <br> $\beta_{10}^{*}=2$ with <br> $\forall j \in\{1, \cdots, 9\}$ <br> $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.05, \beta_{j+1}^{*}+\right.$ <br> $0.15)$ | $n=50$ | $\sigma^{2}=1$ |
| (iii) <br> High- <br> dimension | $D_{m^{*}}=$ <br> 10 | $\beta_{D_{m^{*}}}^{*}=2$ <br> $\forall j \in\{1, \cdots, 9\}$ <br> $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.5, \beta_{j+1}^{*}+\right.$ <br> $1.5)$ | $n \in$ <br> $\{30,50,300\}$ | $\sigma^{2}=1$ |
| (iv) <br> Noise | $D_{m^{*}}=$ <br> 10 | $\beta_{D_{m^{*}}}^{*}=2$ <br> $\forall j \in\{1, \cdots, 9\}$ <br> $\beta_{j}^{*} \sim \operatorname{Unif}\left(\beta_{j+1}^{*}+0.5, \beta_{j+1}^{*}+\right.$ <br> $1.5)$ | $n=50$ | $\sigma^{2} \in$ <br> $\{0.1,1,4\}$ |

Concerning the $\underline{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ and $\bar{f}_{r}\left(K, \beta^{*}, \sigma^{2}\right)$ quantities, they depend on $\beta^{*}$ and $\sigma^{2}$, both unknown.

Table 4: Description of the four scenarios.

The slope heuristic to estimate $\sigma^{2}$. The slope heuristic principle, introduced in [13], is that when $D_{m}$ is large enough, the empirical least squares values $\frac{1}{n}\left\|Y-X \hat{\beta}_{m}\right\|_{2}^{2}$ are almost equal to $-\frac{1}{2 n} K \sigma^{2} D_{m}$ plus an additive constant independent of $n$ and $m$. Hence, it is possible to estimate $\sigma^{2}$ from the dataset by the multiplicative coefficient of the affine behavior between the empirical least squares and $-\frac{K}{2 n} D_{m}$ for $D_{m}$ large enough. We use the function capushe of the $\mathrm{R}$ package capushe (version 1.1.1) [14] with parameters set to the default values.

Some substitutes of $\beta^{*}$. According to [13], $\hat{\beta}_{\hat{m}(K)}$ is a good estimator of $\beta^{*}$ in a predictive point of view when $K$ is equal or close to 2 . We propose to test the estimators $\hat{\beta}_{\hat{m}(\tilde{K})}$ for $\tilde{K} \in\{1,1.5,2,2.5,3,3.5,4,4.5,5, \log (n)\}$ to replace $\beta^{*}$ in the lower and upper bounds $b\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \beta^{*}, \sigma^{2}\right)$.

To determine the best constant $\tilde{K}$ among $\{1,1.5,2,2.5,3,3.5,4,4.5,5, \log (n)\}$, we evaluate all $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ on the sets $\mathcal{D}$ from the four scenarios described in Subsection 7.1. To take into account the randomness of $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$, the model collection generation and model selection given by (2.2) are processed on a new data set independent of $\mathcal{D}$ for the four scenarios.

To evaluate the error by replacing $b\left(K, \beta^{*}, \sigma^{2}\right)$ and $B\left(K, \beta^{*}, \sigma^{2}\right)$ with their estimation $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$, we propose to evaluate the relative changes defined by $: \forall K>0$,

$$
\frac{b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)-b\left(K, \beta^{*}, \sigma^{2}\right)}{b\left(K, \beta^{*}, \sigma^{2}\right)}
$$

for the lower bound and by :

$$
\frac{B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)-B\left(K, \beta^{*}, \sigma^{2}\right)}{B\left(K, \beta^{*}, \sigma^{2}\right)}
$$

for the upper bound. To ensure that $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ values are larger than the $B\left(K, \beta^{*}, \sigma^{2}\right)$ values and so larger than the FDR ones, positive relative change values and as close to 0 as possible are expected. Concerning the lower bounds, negative relative change values are expected to ensure that $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ values are smaller than $B\left(K, \beta^{*}, \sigma^{2}\right)$ values and so smaller than the FDR ones. To take into account randomness of the $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ terms, we evaluate for all $K$ the relative standard deviation, defined by the standard deviation divided by the mean, by calculated the variance of bounds $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ evaluated on 100 new data sets generated independently of $\mathcal{D}$. The relative standard deviation values are expected to be as close to 0 as possible.

Figures 5-7 are plotted from the toy data set. In Figure 5, the empirical estimation of the $\operatorname{FDR}(\hat{m}(K))$ and the quantities $b\left(K, \beta^{*}, \sigma^{2}\right), B\left(K, \beta^{*}, \sigma^{2}\right), b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ are plotted on a grid of positive $K$. Relative changes and relative standard deviations for the lower bounds $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and upper bounds $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ are plotted in Figure 6 and 7. The graphs of all others $\mathcal{D}$ of the 4 scenarios described in Subsection 7.1 are provided in the supplementary material available in ${ }^{1}$.

The lower bounds : For $\tilde{K}>1$, the relative change values are positive until achieving more than 2 for large $K$ (Figure 6 (top)) and the estimated lower bounds curves can be larger than the theoretical one. The relative standard deviation functions increase quickly whatever the value of $\tilde{K}$ suggesting that fluctuations around the mean are not negligible (Figure 7 (top)).

The upper bounds : For $\tilde{K}>1$, the relative change functions are always positive and do not exceed 0.11 meaning that the $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ curves are close to $B\left(K, \beta^{*}, \sigma^{2}\right)$ for all $K>0$ (Figure 6 (bottom)). For data sets $\mathcal{D}$ other than the toy data set (Figures are available in Supplementary material ${ }^{1}$ ), the relative change values are always small but can be negative. However, it happens very rarely for $\tilde{K} \geq 4$ and in this case, values are low enough (smaller than $-0.02 \%)$ to ensure that the empirical FDR estimation curves do not exceed the $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ terms. Concerning the relative standard deviation functions (Figures 7 (bottom) and in Supplementary material ${ }^{1}$ ), the larger $\tilde{K}$, the smaller the values, except for the scenario (ii) with the third configuration where values increase after $\tilde{K} \geq 4.5$. For $\tilde{K} \geq 3.5$, the relative standard deviation values are around 0.2 for all the scenarios except for scenario (ii) with the second configuration (can achieve 0.8 ) and with the third configuration (can achieve 1). Thus, for a value of $\tilde{K} \in\{3.5, \log (n), 4,4.5,5\}$ and eventually except for the two extreme scenarios, fluctuations around the mean are[^0]small, meaning that the upper bound estimations are stable.

To conclude, we drop the lower bound to implement our data-driven algorithm for hyperparameter calibration since $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ functions can be larger than the theoretical FDR one. To control the FDR, only an upper bound control is sufficient. The best results for $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ are obtained with the hyperparameter $\tilde{K}=4$, where the relative change values are almost always positive, small enough to guarantee that the $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ are larger than the theoretical FDR, and the relative standard deviation values are the smallest ones whatever the scenarios. So, the estimator used in our algorithm to replace $\beta^{*}$ in the upper bound of the FDR is $\hat{\beta}_{\hat{m}(4)}$. A natural estimator of $D_{m^{*}}$ is $D_{\hat{m}(4)}$. The value of the hyperparameter $\tilde{K}=4$ is not surprising since the value of $D_{\hat{m}}$ has to be small enough in (3.5) to get an upper bound $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ larger than the theoretical upper one. So, the penalization function has to be large enough in (2.2).

### 7.3 The non-ordering variable selection

This subsection completes Subsection 4.3 about the assessment of our approach in non-ordering variable selection by considering scenarios described in Table 4. Figures and tables are provided in the supplementary material available in ${ }^{2}$.

Figures S-13 to S-15 (available in Supplementary material ${ }^{2}$ ), show similar results about the robustness to variable ordering. This confirms that being able to discriminate between active and non-active variables is crucial. For scenario (ii), $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ values begin to diverge from those of $B\left(K, \beta^{*}, \sigma^{2}\right)$ for the second and the third configurations where the coefficients of $\beta^{*}$ are close to each other. Concerning the second configuration, $B\left(K, \hat{\beta}_{\hat{m}(4)}, \hat{\sigma}^{2}\right)$ and $B\left(K, \beta^{*}, \sigma^{2}\right)$ values are both larger than the empirical FDR ones which is expected. When permutations of the first twelve and fifteen variables are processed, FDR values are, in most cases, even higher along the collections than for the toy data set, especially for scenario (ii) configuration (iii) and for scenario (iv) with $\sigma^{2}=4$ for which distinction between variables is more difficult; the PR values increase faster than for the toy data set. A meticulous study on the choice of the parameters $\gamma$ and $\alpha$ is required to get low values of both PR and FDR.

Table S-1 (available in Supplementary material ${ }^{2}$ ) show the proportion of active variables in models of size 5, 10, 15 and 20 for random collection built with Bolasso, SLOPE, random forest and the knockoff method. Among the random model collections, the knockoff method provides the highest values for all scenarios except scenario (iv) with $\sigma^{2}=0.1$ and some models of size 20 where Bolasso is the best method. Results deteriorate for specific scenarios : around 0.8 for scenario (iv) with $\sigma^{2}=4,0.6$ for scenario (ii) with the third configuration and 0.8 for scenario (ii) with the second configuration for which the discrimination between active and non-active variables is naturally less obvious.

### 7.4 Application of algorithm 1

This subsection completes Subsection 4.2 and Subsection 4.4 by comparing Algorithm 1 and the three variable selection methods (presented below) on scenarios described in Table 4 and from the different considered model collections. With the nested model collection (2.1) and with $\alpha=0.05$ and $\gamma=0.1$, algorithm 1 provides $K=2.8$ for scenario (i) with $D_{m}^{*}=20$ and $K=3.3$ for all others except for scenario (i) with $D_{m}^{*}=1$, for scenario (ii) with the second and the third configurations and for scenario (iv) with $\sigma^{2}=4$. Concerning these last four scenarios, the intersection of $I_{1}$ and $I_{2}$ is empty. The minimum of $I_{1}$ equals 4.8 for scenario (i) with $D_{m}^{*}=1$ and for scenario (ii) with the second configuration, and equals 3.3 for scenario (ii) with the third configuration and for scenario (iv) with $\sigma^{2}=4$. To get a non-empty intersection, $\gamma$ or $\alpha$ has to be higher. In all these examples, we observe that the value of $K$ provided by taking $\min \left(I_{1} \cap I_{2}\right)$ coincides with $\min \left(I_{1}\right)$, so increasing the value of $\gamma$ does not change $K$. However, increasing the value of $\alpha$ provides smaller values for $K$. When $\alpha=0.1$ and $\gamma=0.1$, the intersection of $I_{1}$ and $I_{2}$ is empty and the obtained values of $K$ from $\min \left(I_{1}\right)$ are 3.8 for scenario (i) with $D_{m}^{*}=1$ and for scenario (ii) with the second configuration and 2.8 for scenario (ii) with the third configuration and for scenario (iv) with $\sigma^{2}=4$. Hence, these four cases are typical examples where the choice of $K$ depends strongly on the chosen balance between PR and FDR. In all cases, we always notice that whatever the given balance, the $K$ provided from algorithm 1 coincides with the one given by the trade-off between the two empirical quantities of PR and FDR.

When we compare our algorithm application with the three considered existing variable selection methods (see Tables S2 to S-4 (available in Supplementary material ${ }^{2}$ )), all observations mentioned in Subsection 4.4 remain valid over the different scenarios[^1]

Lower bound

Upper bound

Figure 5: Top : Comparison of the empirical FDR, the functions $b\left(K, \beta^{*}, \sigma^{2}\right)$ (left) and $B\left(K, \beta^{*}, \sigma^{2}\right)$ (right) for the orthogonal design matrix $X$ and the functions $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ (left) and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ (right) with respectively $\hat{\beta}_{\hat{m}(1)}, \hat{\beta}_{\hat{m}(1.5)}, \hat{\beta}_{\hat{m}(2)}, \hat{\beta}_{\hat{m}(2.5)}, \hat{\beta}_{\hat{m}(3)}, \hat{\beta}_{\hat{m}(3.5)}, \hat{\beta}_{\hat{m}(4)}, \hat{\beta}_{\hat{m}(4.5)}, \hat{\beta}_{\hat{m}(5)}$ and $\hat{\beta}_{\hat{m}(\log (n))}$. The terms $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ are calculating from a single data set, independent of those used for the empirical estimations; for a better readability, we plot curves only for $K \geq 2$. Bottom : Same comparison and estimation only with $\tilde{K}=4$.

## 8 Acknowledgments

This research is supported in part by a public grant as part of the Investissement d'avenir project, reference ANR-11LABX-0056-LMH, LabEx LMH. IPS2 benefits from the support of the LabEx Saclay Plant Sciences-SPS (ANR-17EUR-0007).

The authors warmly thank and are grateful to Pascal Massart (Laboratoire de Mathématiques d'Orsay, Université Paris-Saclay) for helpful discussions and valuable comments. The authors would like to sincerely thank the Editor and the two anonymous referees for their valuable comments, suggestions and feedbacks which improved the paper.


Upper bound

Figure 6: Curves of the relative change values between the function $b\left(K, \beta^{*}, \sigma^{2}\right)$ (top) and $B\left(K, \beta^{*}, \sigma^{2}\right)$ (bottom) and the functions $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ (top) and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ (bottom) with respectively $\hat{\beta}_{\hat{m}(1)}, \hat{\beta}_{\hat{m}(1.5)}, \hat{\beta}_{\hat{m}(2)}$, $\hat{\beta}_{\hat{m}(2.5)}, \hat{\beta}_{\hat{m}(3)}, \hat{\beta}_{\hat{m}(3.5)}, \hat{\beta}_{\hat{m}(4)}, \hat{\beta}_{\hat{m}(4.5)}, \hat{\beta}_{\hat{m}(5)}$ and $\hat{\beta}_{\hat{m}(\log (n))}$, where estimators are calculated from a single data set.

## 9 Supplementary data

All the R scripts are available at https://github.com/PerrineLacroix/Trade_off_FDR_PR.

Trade-off between prediction and FDR for variable selection



Lower bound



Upper bound

Figure 7: Curves of the relative standard deviation (standard deviation normalized by the mean) of the functions $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ obtained from 100 data sets. With each one, $\hat{\beta}_{\hat{m}(1)}, \hat{\beta}_{\hat{m}(1.5)}, \hat{\beta}_{\hat{m}(2)}, \hat{\beta}_{\hat{m}(2.5)}, \hat{\beta}_{\hat{m}(3)}, \hat{\beta}_{\hat{m}(3.5)}, \hat{\beta}_{\hat{m}(4)}, \hat{\beta}_{\hat{m}(4.5)}, \hat{\beta}_{\hat{m}(5)}$ and $\hat{\beta}_{\hat{m}(\log (n))}$ are calculated given $b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$, variance of the $100 b\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ and $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ functions and then the relative standard deviation with respect to $K$.

The graphs for the bounds $B\left(K, \hat{\beta}_{\hat{m}(\tilde{K})}, \hat{\sigma}^{2}\right)$ applied on the 4 scenarios described in Subsection 7.1, as well as the study of the robustness of variable ordering, of the construction of random model collections and of the comparison

Trade-off between prediction and FDR for variable selection

of our algorithm with other variable selection procedures, are provided in the supplementary material available in https://github.com/PerrineLacroix/Trade_off_FDR_PR. It is complementary to Subsections 7.2, 7.3 and 7.4 .

Trade-off between prediction and FDR for variable selection

## References

[1] Trevor Hastie, Robert Tibshirani, Jerome H Friedman, and Jerome H Friedman. The elements of statistical learning: data mining, inference, and prediction, volume 2. Springer, 2009.

[2] R. Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (Methodological), 58(1):267-288, 1996.

[3] Florentina Bunea, Alexandre B Tsybakov, and Marten H Wegkamp. Aggregation for gaussian regression. The Annals of Statistics, 35(4):1674-1697, 2007.

[4] Florentina Bunea, Alexandre Tsybakov, and Marten Wegkamp. Sparsity oracle inequalities for the lasso. Electronic Journal of Statistics, 1:169-194, 2007.

[5] N. Meinshausen and P. Bühlmann. Stability selection. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 72(4):417-473, 2010.

[6] F. Bach. Bolasso: model consistent lasso estimation through the bootstrap. In Proceedings of the 25th international conference on Machine learning, pages 33-40, 2008.

[7] Seymour Geisser. The predictive sample reuse method with applications. Journal of the American statistical Association, 70(350):320-328, 1975.

[8] Sylvain Arlot and Alain Celisse. A survey of cross-validation procedures for model selection. Statistics surveys, 4:40-79, 2010.

[9] H Akaike. Information theory and an extension of maximum likelihood principle. In Proc. 2nd Int. Symp. on Information Theory, pages 267-281, 1973.

[10] Colin L Mallows. Some comments on cp. Technometrics, 42(1):87-94, 2000.

[11] G. Schwarz. Estimating the dimension of a model. The annals of statistics, 6(2):461-464, 1978.

[12] J. Chen and Z. Chen. Extended bayesian information criteria for model selection with large model spaces. Biometrika, 95(3):759-771, 2008.

[13] L. Birgé and P. Massart. Minimal penalties for gaussian model selection. Probability theory and related fields, 138(1-2):33-73, 2007.

[14] J.P. Baudry, C. Maugis, and B. Michel. Slope heuristics: overview and implementation. Statistics and Computing, 22(2):455-470, 2012.

[15] Y. Baraud, C. Giraud, S. Huet, et al. Gaussian model selection with an unknown variance. The Annals of Statistics, 37(2):630-672, 2009.

[16] C. Giraud, S. Huet, N. Verzelen, et al. High-dimensional regression with unknown variance. Statistical Science, 27(4):500-518, 2012.

[17] C Bonferroni. Teoria statistica delle classi e calcolo delle probabilita. Pubblicazioni del R Istituto Superiore di Scienze Economiche e Commericiali di Firenze, 8:3-62, 1936.

[18] R John Simes. An improved bonferroni procedure for multiple tests of significance. Biometrika, 73(3):751-754, 1986.

[19] Y. Benjamini and Y. Hochberg. Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal statistical society: series B (Methodological), 57(1):289-300, 1995.

[20] Yoav Benjamini and Daniel Yekutieli. The control of the false discovery rate in multiple testing under dependency. Annals of statistics, pages 1165-1188, 2001.

[21] J. Storey, J. Taylor, and D. Siegmund. Strong control, conservative point estimation and simultaneous conservative consistency of false discovery rates: a unified approach. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 66(1):187-205, 2004.

[22] J. Romano, A. Shaikh, and M. Wolf. Control of the false discovery rate under dependence using the bootstrap and subsampling. Test, 17(3):417-442, 2008.

[23] D. Leung and W. Sun. Zap: $z$-value adaptive procedures for false discovery rate control with side information. arXiv preprint arXiv:2108.12623, 2021.

[24] R. Barber, E. Candès, et al. Controlling the false discovery rate via knockoffs. The Annals of Statistics, 43(5):20552085, 2015.

[25] Shuheng Zhou. Thresholding procedures for high dimensional variable selection and statistical estimation. Advances in Neural Information Processing Systems, 22:2304-2312, 2009.

Trade-off between prediction and FDR for variable selection

[26] Richard Berk, Lawrence Brown, Andreas Buja, Kai Zhang, and Linda Zhao. Valid post-selection inference. The Annals of Statistics, pages 802-837, 2013.

[27] J. Lee, D. Sun, Y. Sun, and J. Taylor. Exact post-selection inference, with application to the lasso. The Annals of Statistics, 44(3):907-927, 2016.

[28] S. Hyun, M. G'sell, and R. Tibshirani. Exact post-selection inference for the generalized lasso path. Electronic Journal of Statistics, 12(1):1053-1097, 2018.

[29] Y. Chen, S. Jewell, and D. Witten. More powerful selective inference for the graph fused lasso, 2021.

[30] V. Duy and I. Takeuchi. More powerful conditional selective inference for generalized lasso by parametric programming. arXiv preprint arXiv:2105.04920, 2021.

[31] Dongliang Zhang, Abbas Khalili, and Masoud Asgharian. Post-model-selection inference in linear regression models: An integrated review. Statistics Surveys, 16:86-136, 2022.

[32] C. Genovese and L. Wasserman. Operating characteristics and extensions of the false discovery rate procedure. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 64(3):499-517, 2002.

[33] C. Genovese, L. Wasserman, et al. A stochastic process approach to false discovery control. The Annals of Statistics, 32(3):1035-1061, 2004.

[34] F. Abramovich, Y. Benjamini, D. Donoho, I. Johnstone, et al. Adapting to unknown sparsity by controlling the false discovery rate. The Annals of Statistics, 34(2):584-653, 2006.

[35] M. Bogdan, E. Berg, W. Su, and E. Candes. Statistical estimation and testing via the sorted 11 norm. arXiv preprint arXiv:1310.1969, 2013.

[36] Weijie Su and Emmanuel Candes. Slope is adaptive to unknown sparsity and asymptotically minimax. 2016.

[37] Michał Kos and Małgorzata Bogdan. On the asymptotic properties of slope. Sankhya A, 82(2):499-532, 2020.

[38] Peter J Bickel and Elizaveta Levina. Regularized estimation of large covariance matrices. 2008.

[39] Elizaveta Levina, Adam Rothman, and Ji Zhu. Sparse estimation of large covariance matrices via a nested lasso penalty. 2008.

[40] Jianhua Z Huang, Naiping Liu, Mohsen Pourahmadi, and Linxu Liu. Covariance matrix selection and estimation via penalised normal likelihood. Biometrika, 93(1):85-98, 2006.

[41] Bin Li, J Friedman, R Olshen, and C Stone. Classification and regression trees (cart). Biometrics, 40(3):358-361, 1984.

[42] Alexandros Kalousis, Julien Prados, and Melanie Hilario. Stability of feature selection algorithms: a study on high-dimensional spaces. Knowledge and information systems, 12:95-116, 2007.

[43] Leo Breiman. Random forests. Machine learning, 45:5-32, 2001.

[44] Y. Yang. Can the strengths of aic and bic be shared? a conflict between model indentification and regression estimation. Biometrika, 92(4):937-950, 2005.

[45] L. Birgé and P. Massart. Gaussian model selection. Journal of the European Mathematical Society, 3(3):203-268, 2001 .

[46] B. Efron, T. Hastie, I. Johnstone, and R. Tibshirani. Least angle regression. The Annals of statistics, 32(2):407-499, 2004.

[47] Isabelle Guyon, Jason Weston, Stephen Barnhill, and Vladimir Vapnik. Gene selection for cancer classification using support vector machines. Machine learning, 46:389-422, 2002.

[48] Baptiste Gregorutti, Bertrand Michel, and Philippe Saint-Pierre. Correlation and variable importance in random forests. Statistics and Computing, 27:659-678, 2017.

[49] David M Allen. The relationship between variable selection and data agumentation and a method for prediction. technometrics, 16(1):125-127, 1974.

[50] Mervyn Stone. Cross-validatory choice and assessment of statistical predictions. Journal of the royal statistical society: Series B (Methodological), 36(2):111-133, 1974.

[51] Jun Shao. Linear model selection by cross-validation. Journal of the American statistical Association, 88(422):486494, 1993.

[52] Frank R Kschischang. The complementary error function. Online, April, 2017.

[53] Beatrice Laurent and Pascal Massart. Adaptive estimation of a quadratic functional by model selection. Annals of Statistics, pages 1302-1338, 2000.


[^0]:    ${ }^{1}$ https://github.com/PerrineLacroix/Trade_off_FDR_PR

[^1]:    ${ }^{2}$ https://github.com/PerrineLacroix/Trade_off_FDR_PR

