# Trade-Off Between Predictive Performance And Fdr Control For High-Dimensional Gaussian Model Selection

Perrine Lacroix Laboratoire de Mathématiques d'Orsay, CNRS, Université Paris-Saclay, Orsay, France Université Paris-Saclay, CNRS, INRAE, Université Evry, Institute of Plant Sciences Paris-Saclay (IPS2),
91190, Gif sur Yvette, France Université Paris Cité, Institute of Plant Sciences Paris-Saclay (IPS2), 91190, Gif sur Yvette, France perrine.lacroix@universite-paris-saclay.fr

## Marie-Laure Martin

Université Paris-Saclay, AgroParisTech, INRAE, UMR MIA Paris-Saclay, 91120, Palaiseau, France Université Paris-Saclay, CNRS, INRAE, Université Evry, Institute of Plant Sciences Paris-Saclay (IPS2),
91190, Gif sur Yvette, France Université Paris Cité, Institute of Plant Sciences Paris-Saclay (IPS2), 91190, Gif sur Yvette, France marie-laure.martin@inrae.fr

## A**Bstract**

In the context of the high-dimensional Gaussian linear regression for ordered variables, we study the variable selection procedure via the minimization of the penalized least-squares criterion. We focus on model selection where the penalty function depends on an unknown multiplicative constant commonly calibrated for prediction. We propose a new proper calibration of this hyperparameter to simultaneously control predictive risk and false discovery rate. We obtain non-asymptotic bounds on the False Discovery Rate with respect to the hyperparameter and we provide an algorithm to calibrate it. This algorithm is based on quantities that can typically be observed in real data applications. The algorithm is validated in an extensive simulation study and is compared with some existing variable selection procedures. Finally, we study an extension of our approach to the case in which an ordering of the variables is not available.

K**eywords** Ordered variable selection · Prediction · FDR · High-dimension · Gaussian regression ·
Hyperparameter calibration

## 1 Introduction. 1.1 Problem Statement.

We consider the following high-dimensional univariate Gaussian linear regression model :

$\mathcal{L}$
Y = Xβ∗ + ε. (1.1)
The random response vector Y =(Yi){1≤i≤n}
T∈ R
n is regressed on p deterministic vectors : X1 =
(xi1){1≤i≤n}
T, · · · , Xp =
(xip){1≤i≤n}
T. The design matrix of size n × p is denoted by X = (X1, · · · , Xp).

The noise ε =
(εi){1≤i≤n}
Tis assumed to be Gaussian : ε ∼ N (0, σ2In) with σ 2 > 0. In the high-dimensional context, additional assumptions of regularity are required and we assume that β
∗is sparse, meaning that only a few coefficients are non-zero. In the following, a variable Xj corresponding to a non-zero coefficient β
∗
j is called an active variable. Otherwise the variable is said to be non-active.

In this paper, we are interested in variable selection. We refer the reader to [1] and references therein. To the best of our knowledge, some variable selection procedures focus on the prediction of the response variable Y through a control of the predictive risk. Others focus on limiting the number of selected non-active variables through a control of the False Discovery Rate. There also exists procedures where several cost functions are considered simultaneously. In the line of the latter, our goal is to identify a set of variables from a model selection procedure by limiting the selection of non-active variables while maintaining accurately prediction performances.

## 1.2 Related Works.

In a variable selection procedure, a cost function has to be defined. The predictive risk (PR) and the False Discovery Rate (FDR) are the common used cost functions.

The penalized methods to control the predictive risk. The penalization procedure balances goodness of fit and sparsity : the smaller the penalty function, the better the fitting to the data but the higher the number of selected variables.

In high-dimension, the most popular method is the Lasso criterion [2] where the estimator βˆλ of β
∗is the solution of :

$${\hat{\beta}}_{\lambda}=\operatorname*{arg\,min}_{\beta\in\mathbb{R}^{p}}\Bigl\{||Y-X\beta||_{2}^{2}+\lambda|\beta|_{1}\Bigr\},$$
$$(1.2)$$
o, (1.2)
2
where *| · |*1 and *|| · ||*2 design the ℓ1-norm and the euclidean norm of a vector respectively. The main challenge is to calibrate the hyperparameter λ > 0. If λ is chosen to be proportional to σ qlog(p)
n, then the predictive risk is bounded
[3, 4]. However, the noise being usually unknown, the choice of λ remains tricky. Therefore, an alternative is to solve the Lasso criterion for a λ within a reasonable interval by using subsamples [5] or resamples [6]. The selected variables are then defined as the variables with the highest selection frequencies. Such alternative is no longer sensitive to the choice of λ but the main challenge lies in the threshold on the frequency defining the selected variables.

In this paper, we consider a model selection procedure composed of three steps. The first step consists in solving the Lasso criterion on a relevant grid Λ. Each λ ∈ Λ defines a variable subset to get a collection M of relevant subsets of variables with a wide range of sizes. In the second step, the least-squares estimator onto each variable subset of M is calculated leading to a collection of estimators βˆm m∈M
. Lastly, the following penalized least-squares minimization is solved to select the best m of M :

$${\hat{m}}=\operatorname*{arg\,min}_{m\in{\mathcal{M}}}\Bigl\{||Y-X{\hat{\beta}}_{m}||_{2}^{2}+\operatorname{pen}(D_{m})\Bigr\},$$
$$(1.3)$$
o, (1.3)
where Dm is the dimension of the model m and the function pen is a penalty function increasing with Dm.

Selecting mˆ from M by minimizing (1.3) corresponds to selecting λˆ from Λ by minimizing (1.2). Hence, the main challenge is the definition of pen that achieves an optimal trade-off between goodness of fit and sparsity within M.

Popular methods of model selection include V −fold cross-validation [7, 8], AIC [9], Cp-Mallows [10], BIC [11] and eBIC [12]. For these penalty functions, the predictive risk is bounded when σ 2is known and when the sample size n tends to infinity. When n is fixed, relatively small, and possibly smaller than the dimension p, a non-asymptotic point of view is preferable to get properties for all couples of (*n, p*). In this direction, [13] propose some penalty functions depending on the collection complexity such that mˆ guarantees non-asymptotic optimal control of the predictive risk. If the model collection is nested with a known variance, pen(Dm) = 2σ 2Dm allows to achieve an optimal non-asymptotic control of the predictive risk [9]. If the model collection is fixed and large (for instance with an exponential growth with Dm) and if the variance is unknown, this optimal control is obtained with data-driven penalties [13, 14]. Lastly, if the model collection is data-dependent and if the variance σ 2is unknown, the LinSelect penalty [15, 16] guarantees an optimal control of the predictive risk.

The multiple testing methods to control the False Discovery Rate. In the multiple testing procedure, the p tests H0 = {β
∗
j = 0} versus H1 = {β
∗
j
̸= 0} are performed independently to get a list of p-values. Variables associated with a p-value smaller than a threshold are selected and the challenge is to find this threshold to obtain an upper bound on a function of the number of selected non-active variables. Several methods control the Family-Wise Error (FWER) which is the probability of selecting at least one non-active variable [17, 18]. However, these methods tend to be conservative leading to a tiny set of selected variables. An alternative consists in controlling the FDR which is the expectation of the proportion of non-active variables among the selected ones. The authors of [19] first provide a threshold assuming independence of the p-values. This hypothesis is then relaxed in [20, 21, 22, 23].

Instead of considering the p-values, the knockoff filter method [24] consists in introducing copies of Xj built to be non-active variables to calibrate a threshold on test statistics.

The simultaneous control of several cost functions. Controlling PR or FDR is commonly performed independently in the literature and yield different sets of selected variables. For a PR control, selected variables aim at correctly predicting a new observation of Y , without guaranteeing that the set of selected variables does not contain non-active variables. Conversely, when the cost function is the FDR, the number of non-active variables is controlled at the price that some active variables are not selected.

Therefore, recent works have been proposed to combine prediction and FDR approaches to select all active variables without selecting non-active ones. For instance, [25] propose a multi-step algorithm where a threshold procedure is applied to some Lasso estimators computed for specific values of λ. In addition to prediction performances, a consistency property on the selected variable set is satisfied under some conditions on X. Another idea is the postselection inference [26, 27] where the principle is to test the relevance of each selected variable by a model selection procedure. Valid confidence intervals are provided from conditional hypothesis tests for each model of the collection in addition to a PR control. Their work has been generalized by [28, 29, 30] and a review can be found in [31]. In a completely different direction, [32, 33] propose to control the False Negative Rate (FNR) in addition to the FDR. A good FNR control ensures that most of the active variables are selected. So, minimizing a weighted sum of FDR and FNR provide a set of variables close to the set of active variables. However, improving FDR control deteriorates FNR control and vice versa. Hence, optimal controls of both criteria are impossible to achieve.

Some other papers propose to combine the FDR with the PR. Additional motivation to consider the PR is its behavior between the learning phase and the over-fitting phase. In the learning phase, the addition of a variable in the selected set drastically reduces the PR, whereas in the over-fitting phase, it increases proportionally to the noise level. Firstly, in the standard multivariate normal mean problem with a known variance, [34] propose a penalty function in the model selection procedure built from a multiple testing procedure. They obtain simultaneously sharp asymptotic bounds of the FDR and the PR. Then, [35] propose the Sorted ℓ1 penalized estimator (SLOPE) which is the minimizer of the Lasso criterion (1.2) where λ is replaced by a p-vector built from a multiple testing procedure. For the orthogonal design, their approach achieves a non-asymptotic control of the FDR and satisfies a minimum value of the total mean squared error with minimax convergence rate [36]. This asymptotic convergence of the FDR has been generalized under a wide range of hypotheses, for instance, for a random design in [37].

Ordered variable selection. The ordered variable framework has attracted much attention recently, especially to overcome the high-dimensional problem. In literature, a large class of methods exists dealing with variables having a natural ranking : [38] for the regression framework, [39] with the nested lasso penalty and [40] for covariance matrix estimation. This assumption allows for drastically reducing the estimation complexity. We develop our paper's theory under this assumption. It can be applied to datasets where assuming an order of variables, obtained for example via a priori knowledge, makes sense.

However, in most applications, no canonical ranking of the variables is available and having a natural order on variables becomes a strong assumption. In this case, alternatives consist in proposing a candidate order from random procedures and applying theoretical statistical methods on the random variable ranking. Several approaches have been implemented in the literature to provide the random orders. The most used ones are based either on a regularization path which is built with the Lasso type equation solving [2] or on a decision tree [41]. However, these approaches suffer from instability in that a small modification of the initial sample could radically change the variable order [42]. To circumvent this instability problem, one solution is to add a sampling procedure like the bootstrap [43]. We adopt this point of view in this article to generalize our theoretical results in non-ordering variable selection.

## 1.3 Main Contributions.

The originality of this paper is to obtain a control of the FDR in addition to the PR control in model selection through a convenient calibration of the penalty.

We assume variables are ranked according to their importance for the response variable Y ; X1 being the most important one, X2 being the second one, *· · ·* , and Xp being the least important one. In Gaussian linear regression, the order is given by the partial correlation between Y and each Xj . A natural model collection is the one containing the nested models respecting the variable order. This framework sounds restrictive but allows to derive theoretical expressions of the FDR in the considered model selection procedure. According to [13], all the penalty functions defined by :

$$\mathrm{pen}(D_{m})=K\sigma^{2}D_{m},\quad\forall m\in\mathcal{M},$$
pen(Dm) = Kσ2Dm, ∀m ∈ M, (1.4)

## Provide A Non-Asymptotic Control Of The Pr For K > 1 When Variables Are Ranked.

Theoretical bounds on the FDR in model selection : Although the model selection procedure is built for a PR control, we obtain non-asymptotic lower and upper bounds on the FDR with respect to K > 0 when σ 2is known. We show that these bounds only involve some evaluations of cumulative distribution functions of the standard Gaussian and of some chi-squared variables. Whatever the noise level, FDR is always strictly positive. When K tends to infinity, the FDR
converges to 0 with an exponential rate. So, a low value of the FDR is satisfying as soon as the value of K is not too large.

Calibration of the hyperparameter K : The obtained theoretical bounds depend on the parameters β
∗and σ 2. We replace them with estimators to obtain completely data-dependent bounds on the FDR. Then, we propose a calibration of the hyperparameter K to control a trade-off between FDR and PR. Our algorithm is validated on an extensive simulation study and is compared with several existing variable selection procedures.

Towards a non-ordering variable selection : From a practical point of view, a crucial assumption of this work is the knowledge of the variable ranking. We investigate empirically an extension in which the variable ordering is not beforehand but estimated using a data-driven procedure to build random model collections.

## 1.4 Outline Of The Paper.

The rest of the paper is organized as follows. Section 2 introduces the Gaussian linear regression model and some notations. Section 3 contains theoretical results. Since an increase of the hyperparameter K leads to a decrease of the FDR, it motivates the study of the FDR function in model selection with respect to K. As the FDR has an intractable expression, bounds are obtained when the variable order and the variance are known. We establish an exponential convergence rate of the FDR function when K tends to infinity. The special case of orthogonal design matrix is studied to illustrate the main results. In Section 4, an algorithm is proposed to calibrate the hyperparameter K in the penalty function to achieve a suitable trade-off between FDR and PR controls. It is based on simultaneous evaluations of the prediction performance and the FDR of the models, which are calculated from properly chosen estimators of σ 2and β
∗.

We then present a study to generalize our procedure in non-ordering variable selection and we compare our algorithm with some existing variable selection procedures. Section 5 contains a conclusion and a discussion of prospective work.

In Section 6, proofs of all the theoretical results are provided. Lastly, validations of the chosen estimators of σ 2and β
∗,
of our algorithm to calibrate K and of the considered alternatives to go towards the non-ordering variable selection are proposed in Section 7 through an extensive simulation study with different parameters.

## 2 Model And Notations.

Let us consider the Gaussian linear regression model given in (1.1). We define q = min(*n, p*) and assume that
(X1, · · · , Xq) is a family of linearly independent vectors. We consider the deterministic and nested model collection of
linear spaces :
$$\mathcal{M}=\Big{\{}m_{0}=\{0\},m_{1}=\text{Span}(X_{1}),\cdots,m_{q}=\text{Span}(X_{1},X_{2},\cdots,X_{q})\Big{\}}.$$  By construction, the true model $m^{*}=\text{Span}(X_{j},\,j\,\text{st}\,\,\beta_{j}^{*}\neq0)$ belongs to $\mathcal{M}$.  For each $m\in\mathcal{M}$, $D_{m}$ is the dimension of $m$ and $\beta_{m}$ is the least square estimator onto $m$
o. (2.1)
For each m ∈ M, Dm is the dimension of m and βˆm is the least-squares estimator onto m :

$$(2.1)$$
$${\hat{\beta}}_{m}=\operatorname*{arg\,min}_{\{\beta,X\beta\in m\}}\Big\{||Y-X\beta||_{2}^{2}\Big\}.$$
$$(X_{1},\cdots,X_{q}),\hat{\beta}_{m}{\mathrm{~is~unique~for~each~}}m\in{\mathcal{M}}.$$

With the definition of q and properties on the family (X1, · · · , Xq), βˆm is unique for each m ∈ M.
For all K > 0, we define the function critK on M as :
$$\operatorname{crit}_{K}(m)=||Y-X{\hat{\beta}}_{m}||_{2}^{2}+K\sigma^{2}D_{m},$$
o. (2.2)
$${\hat{m}}(K)=\operatorname*{arg\,min}_{m\in{\mathcal{M}}}\Bigl\{\operatorname{crit}_{K}(m)\Bigr\}.$$
$$\mathrm{and~the~selected~model~}\hat{m}(K)\mathrm{~by~}:$$
We define PR(m) the predictive risk associated to the model m ∈ M by :

e model $m\in\mathcal{M}$ by :. 
$$\mathbf{PR}(m)=\mathbb{E}{\Big[}||Y-X{\hat{\beta}}_{m}||_{2}^{2}{\Big]},$$
i, (2.3)
where E designs the expectation under the distribution of Y satisfying (1.1). We define successively F P(m) the number of variables contained in m but not in m∗, the false discovery proportion by :

$$\mathrm{FDP}(m)={\frac{\mathrm{FP}(m)}{\operatorname*{max}(D_{m},1)}};$$
$$\mathrm{FDR}(m)=\mathbb{E}\Big[\mathrm{FDR}(m)\Big],$$
and the False Discovery Rate by :  $$\begin{array}{l}\mbox{\rm\bf?}\end{array}$$
$$(2.2)$$
(2.3)  $$\begin{array}{l}\mbox{\rm(2.3)}\end{array}$$

where E still designs the expectation under the distribution of Y satisfying (1.1), so that FDR(m) is deterministic even in the case where m is random.

Finally, the notation ( ., . ) designs the canonical scalar product in R n , II x denotes the orthogonal projection function onto the space X , Φ denotes the standard Gaussian cumulative distribution function and F x a ( k ) is the cumulative distribution function of a chi-squared variable with k degrees of freedom. By convention, an intersection or an union from indices k to ℓ with k > ℓ are the intersection or the union over an empty set. In the same way, the set { k , . . . ℓ } is empty if k > ℓ .

## 3 Main Results.

In this section, the variance σ 2 is supposed to be known. We first present intuitions that lead to study FDR( m ( K )) in model selection. Non-asymptotic bounds on FDR( m ( K )) are obtained in Theorem 3.2, as well as asymptotic behaviors when K tends to infinity in Corollary 3.4. Finally, the particular case where X is the orthogonal design matrix is studied to illustrate the main results.

## Intuitions. 3.1

According to [13] , the penalty function (1.4) satisfies a non-asymptotic control of the PR if and only if K > 1. The constant K = 2 allows to achieve the optimal asymptotic control of the PR. Hence, 2 is commonly chosen in practice but other values of K close to 2 can give identical if not better non-asymptotic prediction performances. In this direction, we propose to calibrate the hyperparameter K among those leading to prediction performances close to or better than for K = 2 while satisfying a control of the FDR. The calibration is based on both PR( m ( K )) and FDR( m ( K )) functions with respect to K .

![4_image_0.png](4_image_0.png)

We propose an example to illustrate our point and intuition. In Figure 1, we plot the empirical estimators of PR( m ( K )) and FDR( m ( K )) on a regular grid of positive K . Graphs are obtained from the toy data set described in Section 7 and values are transferred to Table I. We observe that the empirical PR( m ( K )) values are kept low for K ′ ∈ [2, 4] while the FDR( m ( K )) function decreases with K until 0. Here, the choice K = 3 is more judicious than K = 2: it ensures a stronger and positive (a FDR zero value is not relevant as it means that no variable is selected) control of the FDR while

| K                                                                                                             | 0.1   | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
|---------------------------------------------------------------------------------------------------------------|-------|------|------|------|------|------|------|------|------|------|------|
| empirical                                                                                                     |       |      |      |      |      |      |      |      |      |      |      |
| FDR( ˆm(K))                                                                                                   | 0.80  | 0.38 | 0.05 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| empirical                                                                                                     |       |      |      |      |      |      |      |      |      |      |      |
| PR( ˆm(K))                                                                                                    | 2.01  | 1.55 | 1.25 | 1.24 | 1.25 | 1.26 | 1.28 | 1.30 | 1.32 | 1.33 | 1.36 |
| Table 1: Values of the empirical estimators of PR( ˆm(K)) and FDR( ˆm(K)) according to K for the toy data set |       |      |      |      |      |      |      |      |      |      |      |

satisfying similar prediction performances. We also observe that while FDR decreases with K, PR increases from a certain value of K ≥ 2. To control PR and FDR simultaneously, the constant K must be close to 2.

Increasing the constant K to limit the non-active variable selection is known for the asymptotic point of view. Indeed, AIC and Cp-Mallows penalties [9, 10], where K equals 2, give asymptotically the best set of variables for prediction performances; while BIC penalty [11], where K is fixed to log(n), exactly recovers asymptotically the set of active variables. Obtaining the asymptotic properties of AIC, Cp-Mallows and BIC penalties simultaneously is impossible
[44], but it suggests that a value of K ∈ [2, log(n)] would get reasonable (but not necessarily optimal) values for both PR and FDR in a non-asymptotic framework. In this way, we propose to study the function FDRmˆ (K)in the model selection procedure (2.2) where the penalty function is (1.4) in the ordered variable setting.

## 3.2 Bounds On The Fdr In Model Selection. 3.2.1 Fdr Expression In Model Selection For Ordered Variables.

Let us assume that K > 0 and critK is injective on M. If D∗m = q, FDR( ˆm(K)) = 0. Otherwise, the FDR( ˆm(K)) is expressed within the model selection procedure as :

$$\text{FDR}(\hat{m}(K))=\sum_{r=D_{m}+1}^{q}\frac{r-D_{m}}{r}\mathfrak{p}\left(\left\{\begin{array}{l}\beta\\ \ell=0\\ \ell\neq r\end{array}\right.\left(\text{crit}_{K}(m_{r})<\text{crit}_{K}(m_{\ell})\right)\right\}\right).\tag{3.1}$$

A detailed proof of (3.1) can be found in Subsection 6.1.

By using the decomposition
$$\left\{\bigcap_{\ell=0}^{r-1}\{\mathrm{crit}_{K}(m_{r})<\mathrm{crit}_{K}(m_{\ell})\}\right\}\bigcap\left\{\bigcap_{\ell=r+1}^{q}\{\mathrm{crit}_{K}(m_{r})<\mathrm{crit}_{K}(m_{\ell})\}\right\}$$
of the termq∩
ℓ=0 ℓ̸=r
{critK(mr) < critK(mℓ)}, we obtain the following proposition :
Proposition 3.1. *Let us consider the ordered variable framework and the model collection (2.1) where* q = min(*n, p*),
m∗ ∈ M and D∗m < q. Let us assume that critK is injective on M. Let (u1, · · · , un) *an orthonormal basis of* R
n such that Span(X1, · · · , Xj ) = Span(u1, · · · , uj ), ∀j ∈ {1, · · · , q}.

Then, ∀K > 0,

$$F D R(\dot{m}(K))=\sum_{r=D_{m}{}^{*}+1}^{q}\frac{r-D_{m}{}^{*}}{r}\;P_{r}(K)\;Q_{r}(K,\beta^{*},\sigma^{2}),$$
$$w h e r e\;f o r\;e a c h\;r\in\{D_{m^{*}}+1,\cdots,q\},$$
$$P_{r}(K)=\mathbb{P}\bigg{(}\bigcap_{\ell=r+1}^{q}\bigg{\{}\sum_{k=r+1}^{\ell}Z_{k}^{2}<K(\ell-r)\bigg{\}}\bigg{)},$$  _where $Z_{k}\stackrel{{i,i,d}}{{\leadsto}}\mathcal{N}(0,1),\ \ \forall k\in\{r+1,\cdots,q\},$_  _and $Q_{r}(K,\beta^{*},\sigma^{2})=\mathbb{P}\bigg{(}\bigcap_{\ell=0}^{r-1}\bigg{\{}\sum_{k=\ell+1}^{r}\langle Y,u_{k}\rangle^{2}>K\sigma^{2}(r-\ell)\bigg{\}}\bigg{)}.$_
$$(3.2)$$
$$(3.3)$$

A proof of Proposition 3.1 can be found in Subsection 6.1.

## 3.2.2 General Bounds.

In (3.2), the Pr(K) terms do not depend on data. Conversely, the Qr(K, β∗, σ2) terms depend on the data. Thus, to understand the behavior of the FDR function with respect to mˆ (K), we propose to bound the Qr(K, β∗, σ2) terms in the following theorem :
Theorem 3.2. *Let us consider the ordered variable framework and the model collection (2.1) where* q = min(*n, p*).

Let us suppose that m∗ ∈ M and D∗m < q. The notation Φ stands for the standard gaussian cumulative distribution function and Fχ2(k)is the cumulative distribution function of a chi-squared variable with k degrees of freedom.

Let us assume that ∀K > 0, critK is injective on M. Let (u1, · · · , un) *an orthonormal basis of* R
n such that Span(X1, · · · , Xj ) = Span(u1, · · · , uj ), ∀j ∈ {1, · · · , q}.

Then, ∀K > 0, mˆ (K) *satisfies :*

$b(K,\beta^{*},\sigma^{2})\leq FDR(\hat{m}(K))\leq B(K,\beta^{*},\sigma^{2})$, (3.4)
where hK 7→ b(K, β∗, σ2) iand hK 7→ B(K, β∗, σ2) iare two real-valued functions on R + defined by : b(K, β∗, σ2) = Xq r=Dm∗+1 r − Dm∗ rPr(K) fr (K, β∗, σ2) ! , B(K, β∗, σ2) = Xq r=Dm∗+1 r − Dm∗ rPr(K) f r (K, β∗, σ2) ! , (3.5) where for all K > 0, Pr(K) is defined in (3.3) and
where for all K > 0, Pr(K) is defined in (3.3) and 1. for each r ∈ {Dm∗ + 1, · · · , q} and for all ℓ ∈ {1, · · · , r}, fℓ (·, β∗, σ2) is defined by : f1 (K, β∗, σ2) = G1 fℓ (K, β∗, σ2) = Gℓ + Hℓ fℓ−1 (K, β∗, σ2), ∀ℓ ∈ {2, · · · , r}, with for ℓ ∈ {1, · · · , Dm∗ } : Gℓ = 2 − Φ√ℓK − ⟨Xβ∗, uℓ⟩ σ + Φ√ℓK + ⟨Xβ∗, uℓ⟩ σ , for ℓ ∈ {2, · · · , Dm∗ } : Hℓ = Φ√ℓK − ⟨Xβ∗, uℓ⟩ σ + Φ√ℓK + ⟨Xβ∗, uℓ⟩ σ  − Φ √K − ⟨Xβ∗, uℓ⟩ σ + Φ√K + ⟨Xβ∗, uℓ⟩ σ , for ℓ ∈ {Dm∗ + 1, · · · , r} : Gℓ = 21 − Φ√ℓK Hℓ = 2Φ√ℓK− Φ√K,
2. $\forall r\in\{D_{m^{*}}+1,\cdots,q\}$, $\overline{f}_{r}(\cdot,\beta^{*},\sigma^{2})$ is defined by : $$\overline{f}_{r}(K,\beta^{*},\sigma^{2})=1-\max\bigg{(}\max_{\ell\in\{1,\cdots,r-D_{m^{*}}\}}\Big{(}F_{\chi^{2}(\ell)}(\ell K)\Big{)},$$ $$\ell\in\{r-D_{m^{*}}+1,\cdots,r\}\bigg{(}F_{\chi^{2}(\ell)}\Big{(}\frac{\ell K}{2}-\sum_{k=r-\ell+1}^{D_{m^{*}}}\frac{\langle X\beta^{*},u_{k}\rangle^{2}}{\sigma^{2}}\Big{)}\bigg{)}\bigg{)}.$$
A proof of Theorem 3.2 can be found in Subsection 6.2.

Hence, although the model selection procedure is built for prediction performances, bounds on the FDR are derived with respect to mˆ (K). Terms fr
(K, β∗, σ2) and f r
(K, β∗, σ2) only involve evaluations of cumulative distribution functions of the standard Gaussian and chi-squared variables. So, they have a fully explicit form which simplifies the understanding of the behavior of the FDR in model selection. However, they depend on the unknown parameters β
∗
and σ 2for which estimators are proposed in Section 4.1.2.

## 3.2.3 Strictly Positive Fdr.

The following corollary gives a lower bound on the FDR independent from σ 2.

Corollary 3.3. Under the assumptions and definitions of Theorem 3.2, ∀K > 0 :

$$F D R({\hat{m}}(K))\geq\sum_{r=D_{m}+1}^{q}\left(\frac{r-D_{m}{}^{*}}{r}P_{r}(K)\,\frac{2\sqrt{2}}{\sqrt{\pi}\Big{(}\sqrt{rK}+\sqrt{rK+4}\Big{)}}e^{-\frac{rK}{2}}\right)\ >0.$$

A proof of Corollary 3.3 can be found in Subsection 6.3.

From Corollary 3.3, FDR( ˆm(K)) > 0 for all K > 0 and whatever σ 2. This may be counter-intuitive, especially in the noiseless setting. When σ 2 = 0, Y = Xβ∗and the minimization in (2.2) is reduced to the least-squares criterion minimization. So, in this particular noiseless case, βˆm∗ = β
∗and the associated least-squares criterion is zero. Any m including m∗also attains a least squares objective of zero as the magnitude of the regression coefficients corresponding to the non-active variables is null. Such supersets can be selected leading to FDP( ˆm) > 0 and so FDR( ˆm) > 0.

## 3.2.4 Asymptotic Analysis.

The following corollary gives the asymptotic behavior of the FDR function in model selection when K tends to infinity.

Corollary 3.4. Under the assumptions and the definitions of Theorem 3.2, the FDR( ˆm(K)) function tends to 0 *when* K tends to infinity and satisfies ∀η > 0,

FDR( ˆm(K)) = o K−→+∞ e −K( 1 2 −η). (3.6) Furthermore, ∀η > 0, ∃Cη > 0, ∃Lη > 0, ∀K > Lη, we have : FDR( ˆm(K)) ≥ Cηe −K Dm∗ +1+2η 2  . (3.7)
$$S o,\,\forall\varepsilon>0,$$
$$-\frac{D_{m^{*}}}{2}-\frac{1}{2}-\varepsilon\leq\liminf_{K\to+\infty}\frac{1}{K}\log\left(FDR(\hat{m}(K))\right)$$ $$\limsup_{K\to+\infty}\frac{1}{K}\log\left(FDR(\hat{m}(K))\right)\ \leq\ -\frac{1}{2}+\varepsilon.$$
$$(3.7)$$
$$(3.8)$$
A proof of Corollary 3.4 can be found in Subsection 6.4.
From Equation (3.6), FDR( ˆm(K)) tends to 0 when K tends to +∞ with at least an exponential convergence rate and
Equation (3.7) suggests that the exponential convergence rate is optimal.
Remark 3.5. *With no signal (*β
∗ = 0 and Dm∗ = 0*), the asymptotic bounds in (3.8) are* −
$\frac{1}{2}-\varepsilon\;and\;-\frac{1}{2}+\varepsilon\;and\;$  . 
consequently :
$$\log\left(F D R(\hat{m}(K))\right)\stackrel{\sim}{K\rightarrow+\infty}-\frac{1}{2}K.$$
Remark 3.6. *The asymptotic upper and lower bounds (3.6) and (3.7) are satisfied whatever the value of* σ 2 > 0*. It is*

possible to obtain the following sharpest asymptotic upper bound : $\forall i_{j}>0$,_  $$FDR(\hat{in}(K))=o\bigg{(}e^{-\left(K\frac{\left(D_{i}+\alpha_{i}-1\right)}{1}-\frac{1}{2\sigma^{2}}\sum_{j=0}^{\sigma_{i}}\left(X^{\sigma_{i}}+\alpha_{i}\right)^{2}\right)}\bigg{)}\tag{3.9}$$  _in the asymptotic regime where $K\longrightarrow+\infty$ and $\sigma\longrightarrow0$ with $\frac{1}{\sigma}=\sigma\underset{\sigma\longrightarrow0}{\longrightarrow}(\sqrt{K})$. The reader can find a proof in Subsection 6.4._
$$(3.9)$$

## 3.3 Illustrations Of The Main Result In The Orthogonal Case.

We propose to analyze the particular case where the design matrix X is orthogonal since it leads to simplified forms for the FDR bounds that are easy to calculate.

Corollary 3.7 (Application on the orthogonal case). Under assumptions of Theorem 3.2 *and by assuming that*
(X1, · · · , Xq) are orthonormal with respect to ⟨., .⟩, then, ∀K > 0, FDR( ˆm(K)) *satisfies the same inequalities as (3.4)*
where :

for ℓ ∈ {1, · · · , Dm∗ } : Gℓ = 2 − Φ √ℓK − β ∗ ℓ σ + Φ√ℓK + β ∗ ℓ σ , for ℓ ∈ {2, · · · , Dm∗ } : Hℓ = Φ√ℓK − β ∗ ℓ σ + Φ√ℓK + β ∗ ℓ σ − Φ √K − β ∗ ℓ σ + Φ√K + β ∗ ℓ σ , for all r ∈ {Dm∗ + 1, · · · , q} : f r (K, β∗, σ2) = 1 − max max ℓ∈{1,··· ,r−Dm∗ } Fχ2(ℓ)(ℓK) , max ℓ∈{r−Dm∗+1,··· ,r} Fχ2(ℓ) ℓK 2− D Xm∗ k=r−ℓ+1 β ∗2 k σ 2 !, and all other terms are the same as those defined in Theorem 3.2.
A proof of Corollary 3.7 can be found in Subsection 6.5.

![8_image_0.png](8_image_0.png)

In Figure 2, we plot the empirical estimation of the FDR( ˆm(K)) with the functions b(K, β∗, σ2) and B(K, β∗, σ2) on a grid of positive K (left) and for K ≥ 2 (right). Graphs are obtained from the *toy data set* described in Section 7 where X is orthogonal. The left figure is devoted to illustrate Corollary 3.7. The FDR values are well smaller than the upper bound values and larger than the lower bound ones. From the right figure and in accordance with Corollary 3.4, the empirical FDR( ˆm(K)) values tend to 0 when K increases and the convergence rate seems to be exponential. Moreover, the curves of b(K, β∗, σ2) and B(K, β∗, σ2) frame the empirical FDR and the difference between the three functions becomes quickly negligible for K larger than 2.

## 4 Trade-Off Between The Pr And The Fdr Controls.

While bounds b(K, β∗, σ2) and B(K, β∗, σ2) are easily understandable and fully implementable, they depend on β
∗,
σ 2and D∗m. These quantities are unknown in practice. For a practical use, we propose to replace the theoretical bounds on the FDR as well as the theoretical expression of the PR with observable quantities (Subsection 4.1). Then, we propose an algorithm to calibrate the hyperparameter K from the data set such that both PR and FDR are controlled
(Subsection 4.2).

As variables are not usually naturally ranked, we explore the robustness of our algorithm under perturbations of the correct variable ordering and present approaches for obtaining a variable ordering in a data-driven manner. Results are provided in Subsection 4.3. Lastly, our algorithm is compared with some existing variable selection procedures in Subsection 4.4, in terms of both PR and FDR.

## 4.1 Estimation Of The Unknown Quantities Appearing In Our Bounds.

We propose to replace the theoretical terms by observable quantities.

## 4.1.1 Estimation Of The Pr.

Commonly, the predictive risk is evaluated with the mean squared error on a validation set independent from the training set used to estimate the parameters (see Formula (7.1) for the definition). However, it requires separating the dataset in two parts which increases the estimation errors. Here, we propose to use the entire dataset to both apply the model selection procedure and evaluate the predictive risk. Intuitively, the response vector Y is replaced with Xβˆmˆ (2) which provides good prediction performances [13]. Moreover, by re-expressing the PR, it is straightforward to show that for all K > 0 and K
′> 0 :

$$\mathbb{E}[||Y-X\hat{\beta}_{\hat{m}(K)}||_{2}^{2}]-\mathbb{E}[||Y-X\hat{\beta}_{\hat{m}(K^{\prime})}||_{2}^{2}]$$ $$=\mathbb{E}[||X\hat{\beta}_{\hat{m}(2)}-X\hat{\beta}_{\hat{m}(K)}||_{2}^{2}]-\mathbb{E}[||X\hat{\beta}_{\hat{m}(2)}-X\hat{\beta}_{\hat{m}(K^{\prime})}||_{2}^{2}]$$ $$\quad-2\mathbb{E}[(X\hat{\beta}_{\hat{m}(2)}-Y,X\hat{\beta}_{\hat{m}(K^{\prime})}-X\hat{\beta}_{\hat{m}(K)})].\tag{4.1}$$
f (2.3), so $||Y-X\hat{\beta}_{\hat{m}(2)}||_2$ i. 
According to [45], the constant 2 provides the optimal asymptotic control of (2.3), so ||Y − Xβˆmˆ (2)||2 is close to 0. Moreover, Xβˆmˆ (2) is close to ΠIm(X)(Y ), so Xβˆmˆ (2) − Y almost belongs to the subspace Im(X)
⊥. In addition, Xβˆmˆ (K) and Xβˆmˆ (K
′)
belongs to Im(X), so the last term in (4.1) is close to 0 and is negligible compared to the two others. So, for all K > 0 and K
′> 0, E[||Y − Xβˆmˆ (K)||22
] − E[||Y − Xβˆmˆ (K
′)
||22
] equals E[||Xβˆmˆ (2) −
Xβˆmˆ (K)||22
] − E[||Xβˆmˆ (2) − Xβˆmˆ (K
′)
||22
] up to an additive negligible term. Hence, the constant K minimizing E[||Xβˆmˆ (2) − Xβˆmˆ (K)||22
] and the one minimizing E[||Y − Xβˆmˆ (K)||22
] are almost equal. Therefore, to evaluate the prediction performances of mˆ (K), we propose to compare prediction performances of the estimates Xβˆmˆ (K) and Xβˆmˆ (2). We introduce the following term that we call *estimated difference in predictions* :

$$\widehat{\mathrm{diff-PR}}(\hat{m}(K))=\frac{1}{n}\widehat{\sum_{i=1}^{n}}\Bigl(\bigl(X\hat{\beta}_{\hat{m}(2)}\bigr)_{i}-\bigl(X\hat{\beta}_{\hat{m}(K)}\bigr)_{i}\Bigr)^{2}.$$
2. (4.2)
For the rest of the paper, the empirical version of (4.2) is calculated averaging over 100 independent data sets and is denoted diff-PR. If this difference is significantly smaller than the noise level σ 2, the model mˆ (K) has performances similar to those satisfied by mˆ (2).

## 4.1.2 Estimation Of The Fdr.

The functions b(·, β∗, σ2) and B(·, β∗, σ2) are explicit and easily implementable but depend on β
∗, σ 2and D∗m, which are unknown.

We propose :
1. to apply the slope heuristic method [13] to get an estimator σˆ
2 of σ 2, 2. to replace β
∗ by the estimator βˆmˆ (4),

$$(4.2)$$
