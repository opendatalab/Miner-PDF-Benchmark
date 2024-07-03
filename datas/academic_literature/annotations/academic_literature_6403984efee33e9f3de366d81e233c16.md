# Adaptive Strategy of Testing Alphas in High Dimensional Linear Factor Pricing Models 

Chenxi Zhao, Ping Zhao, Long Feng and Zhaojun Wang<br>School of Statistics and Data Science, KLMDASR, LEBPS, and LPMC,<br>Nankai University

April 11, 2024


#### Abstract

In recent years, there has been considerable research on testing alphas in highdimensional linear factor pricing models. In our study, we introduce a novel maxtype test procedure that performs well under sparse alternatives. Furthermore, we demonstrate that this new max-type test procedure is asymptotically independent from the sum-type test procedure proposed by Pesaran and Yamagata (2017). Building on this, we propose a Fisher combination test procedure that exhibits good performance for both dense and sparse alternatives.


## 1 Introduction

Linear Factor Pricing Model (LFPM) plays a central role in modern theories of security pricing (Zhou, 1993). Let $N$ be the number of securities, and $T$ be the time dimension of the return series of each security. Let the $t$ th return of the $i$ th security be $Y_{i t}$. LFPM has the form

$$
Y_{i t}=\alpha_{i}+\boldsymbol{\beta}_{i}^{\top} \mathbf{f}_{t}+\varepsilon_{i t}
$$

for $i=1, \ldots, N, t=1, \ldots, T$, where $\mathbf{f}_{t} \equiv\left(f_{t 1}, \cdots, f_{t p}\right)^{\top} \in \mathcal{R}^{p}$ contains $p$ economic factors at time $t, \alpha_{i}$ is a scalar representing the security specific intercept, $\boldsymbol{\beta}_{i} \equiv\left(\beta_{i 1}, \cdots, \beta_{i p}\right)^{\top} \in \mathcal{R}^{p}$ is a vector of multiple regression betas with respect to the $p$ factors and $\varepsilon_{i t}$ is the corresponding idiosyncratic error term with $\operatorname{Cov}\left(\boldsymbol{\varepsilon}_{t}\right) \equiv \boldsymbol{\Sigma}=\left(\sigma_{i j}\right)_{N \times N}$, where $\boldsymbol{\varepsilon}_{t} \equiv\left(\varepsilon_{1 t}, \cdots, \varepsilon_{N t}\right)^{\top} \in \mathbb{R}^{N}$ for each $t \in\{1, \cdots, T\}$. Many well known factor models belong to LPFM, such as the Sharpe-Lintner Capital Asset Pricing Model (CAPM) (Sharpe, 1964; Lintner, 1965), the Fama-French three-factor model (Fama and French, 1993), and the Fama-French five-factor model (Fama and French, 2015). The LFPM aims to clarify the variations in anticipated security returns by considering the interaction between security betas and systematic economic factors. It specifically predicts a linear relationship between the expected security
return and the economic factors that are unique to each security. This linear framework is highly intuitive and offers the practical advantage of simplifying the modeling of security returns.

The intercept term $\alpha_{i}$ in (1) captures the excessive return of the $i$ th security. That is, other than the return associated with the overall market factors, some securities may have systematic positive or negative returns due to characteristics of the individual securities, termed excess returns. Thus, the following pair of hypotheses

$$
H_{0}: \boldsymbol{\alpha}=\mathbf{0} \text { versus } H_{1}: \boldsymbol{\alpha} \neq \mathbf{0}
$$

with $\boldsymbol{\alpha} \equiv\left(\alpha_{1}, \cdots, \alpha_{N}\right)^{\top}=\mathbf{0}$ allows to assess whether the excess return of the market portfolio presents. When the number of securities $N$ is fixed, many test procedures are devised under the normal or non-normal distribution assumptions, such as Gibbons et al. (1989), Mackinlay and Richardson (1991), Zhou (1993) and Beaulieu et al. (2007), etc. Nowadays, thousands of securities are traded in modern financial markets. So the assumption of fixed $N$ is not appropriate.

Many efforts have been devoted for testing alphas in high dimensional linear factor pricing model. Generally speaking, there are three-types test procedures in literature. The first type is the sum-type test procedure, which are constructed by summing the square of the classic t-test statistic of each security, such as Pesaran and Yamagata (2017), Gagliardini et al. (2016) Ma et al. (2020) and Giglio et al. (2021), etc. These sum-type tests have good performance against dense alternatives, i.e. the alphas of over a large number of securities are not zero. The second type is the max-type test procedure, which are constructed by taking the maximum of the squared standard t-ratio of each securities, such as Feng et al. (2022b). The max-type test procedure is powerful under the sparse alternative, i.e. only a few alphas of securities are not zero. However, we can not know whether the alternative is dense or sparse in real applications. So the third type of test procedure are constructed by combining the above sum-type and max-type test procedures together. Fan et al. (2015) proposed a power enhancement procedure by adding sum-type test statistics and max-type test statistics. Feng et al. (2022b), Yu et al. (2023) proposed a Fisher combination test based on the asymptotically independence between the sum-type test statistic and the max-type test statistic. In this paper, we will propose a novel adaptive strategy test procedure, which belongs to the third type test procedure.

Yu et al. (2023) employed the thresholding covariance matrix estimator of Fan et al. (2015) and proposed a novel sum-type test statistic in their Fisher combination test procedure. However, there would be a non-negligible bias term in their sum-type test statistic if the covariance matrix estimator is not very accurate. In addition, the max-type test statistic in Feng et al. (2022b) and Yu et al. (2023) do not consider the information of the correlation of each security, which may perform not very well under some special sparse alternatives. To overcome this issue, we first proposed a novel max-type test statistic by standardizing the vector of t-test statistics of each security. Then, we prove that the new max-type test statistic is asymptotically independent with the sum-type test statistic of Pesaran and Yamagata (2017). Finnally, we propose a new Fisher combination test by the above two asymptotically
independent test statistics. Simulation studies show the superior of our proposed procedure.

The rest of paper is organized as follows. In Section 2, we introduce the new max-type test statistic and establish the theoretical results. And we also propose an adaptive strategy testing procedure. Simulation studies are presented in Section 3. All the technical proofs are given in the Appendix.

## 2 Our test procedure

### 2.1 Max-type test

To test the hypothesis (2), Feng et al. (2022b) propose a max-of-squares type test, named the MAX test, with the test statistic constructed as

$$
M_{\mathbf{I}}=\max _{1 \leq i \leq N} t_{i}^{2}
$$

where

$$
t_{i}=\frac{\hat{\alpha}_{i} \sqrt{\left(\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}\right)}}{\sqrt{v^{-1} \hat{\varepsilon}_{i \cdot}^{\top} \hat{\varepsilon}_{i}}}
$$

is the squared standard t-ratio of $\alpha_{i}$ in the OLS regression of $y_{i t}$ on an intercept and $\mathbf{f}_{t}$, and $v=T-p-1$. Here, $\mathbf{1}_{T}=(1, \cdots, 1)^{\top}, \mathbf{I}_{T}$ is the $T \times T$ identity matrix, $\mathbf{F}=\left(\mathbf{f}_{1}, \cdots, \mathbf{f}_{T}\right)^{\top} \in$ $\mathbb{R}^{T \times p}$ and $\mathbf{M}_{\mathbf{F}}=\mathbf{I}_{T}-\mathbf{F}\left(\mathbf{F}^{\top} \mathbf{F}\right)^{-1} \mathbf{F}^{\top} ; \hat{\boldsymbol{\alpha}}=\left(\hat{\alpha}_{1}, \cdots, \hat{\alpha}_{N}\right)^{\top}$ is the OLS estimator of $\boldsymbol{\alpha}$, where $\hat{\alpha}_{i}=\mathbf{Y}_{i}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} /\left(\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}\right)$ and $\mathbf{Y}_{i}=\left(Y_{i 1}, \cdots, Y_{i T}\right)^{\top} \in \mathbb{R}^{T} ; \hat{\varepsilon}_{i t}$ is the OLS residual from the regression of $y_{i t}$ on an intercept and $\mathbf{f}_{t}, \boldsymbol{\varepsilon}_{i} . \equiv\left(\varepsilon_{i 1}, \cdots, \varepsilon_{i T}\right)^{\top} \in \mathbb{R}^{T}$ and $\hat{\varepsilon}_{i .} \equiv\left(\hat{\varepsilon}_{i 1}, \cdots, \hat{\varepsilon}_{i T}\right)^{\top}=$ $\mathbf{M}_{\mathbf{F}}\left(\mathbf{Y}_{i}-\hat{\alpha}_{i}\right)$.

However, the test statistic (3) do not consider the correlation between those securities. Under the null hypothesis, $\boldsymbol{\alpha}=\mathbf{0}$ is equivalent to $\mathbf{B} \boldsymbol{\alpha}=\mathbf{0}$ for any positive definite matrix B. Under the null hypothesis, we have $\boldsymbol{t}=\left(t_{1}, \cdots, t_{N}\right) \xrightarrow{d} N(\mathbf{0}, \mathbf{R})$ if $\boldsymbol{\varepsilon}_{t} \sim N(0, \boldsymbol{\Sigma})$ where $\boldsymbol{\Sigma}$ is the covariance matrix and $\mathbf{R}$ is the corresponding correlation matrix. So a nature choice of $\mathbf{B}$ is $\mathbf{R}^{-1 / 2}$ which standardized the $t$-test statistics $\boldsymbol{t}$. So, if we have a good consistent estimator of $\boldsymbol{\Omega}^{1 / 2} \doteq \mathbf{R}^{-1 / 2}, \hat{\boldsymbol{\Omega}}^{1 / 2}$, we could propose a new max-type test

$$
M_{\hat{\Omega}^{1 / 2}}=\max _{1 \leq i \leq N} \nu_{i}^{2}
$$

where $\nu=\left(\nu_{1}, \cdots, \nu_{N}\right)^{\top}=\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}$.

Next, we consider the theoretical properties of $M_{\hat{\Omega}^{1 / 2}}$ based on the following assumptions.

(A1) $\varepsilon_{1}, \ldots, \boldsymbol{\varepsilon}_{T}$ are independently and identically distributed with $\varepsilon_{t}=\boldsymbol{\Sigma}^{1 / 2} \boldsymbol{\xi}_{t}$. And we assume $\boldsymbol{\xi}_{t}=\left(\xi_{1 t}, \cdots, \xi_{N t}\right)$ contains independent components $\xi_{i t}$ 's with $E\left(\xi_{i t}\right)=0$ and $\operatorname{var}\left(\xi_{i t}\right)=1, E\left(\xi_{i t}^{4}\right)<c$ for some positive constant $c$. Define $\mathbf{R}=\mathbf{D}^{-1 / 2} \boldsymbol{\Sigma} \mathbf{D}^{-1 / 2}=$ $\left(r_{i j}\right)_{1 \leq i, j \leq N}$ where $\mathbf{D}$ is the diagonal matrix of $\boldsymbol{\Sigma}$. (i) There exists $c_{3}>0$, such that $c_{3}^{-1} \leq \lambda_{\min }(\mathbf{R}) \leq \lambda_{\max }(\mathbf{R}) \leq c_{3}$. (ii) There exists $r_{1}>0$, such that $\max _{1 \leq i<j \leq N}\left|r_{i j}\right| \leq$ $r_{1}<1$.

(A2) $\xi_{i t}$ 's have one of the following three types of tails: (i) sub-Gaussian-type tails, i.e. there exist $\eta>0$ and $K>0$ such that $E\left\{\exp \left(\eta \xi_{i t}^{2} / \sigma_{i i}\right)\right\} \leq K$ for $1 \leq i \leq N$, where $N$ satisfies $\log (N)=o\left(T^{1 / 4}\right)$; (ii) sub-exponential-type tails, i.e. there exist $\eta>0$ and $K>0$ such that $E\left\{\exp \left(\eta\left|\xi_{i t}\right| / \sigma_{i i}^{1 / 2}\right)\right\} \leq K$ for $1 \leq i \leq N$, where $N$ satisfies $\log (N)=o\left(T^{1 / 4}\right)$; (iii) sub-polynomial-type tails, i.e. for some constants $\gamma_{0}, \epsilon>0$ and $K>0, E\left|\xi_{i t} / \sigma_{i i}^{1 / 2}\right|^{2 \gamma_{0}+2+\epsilon} \leq K$ for $1 \leq i \leq N$, where $N$ satisfies $N \leq c_{1} T^{\gamma_{0}}$ for some constants $c_{1}>0$.

(A3) (i) $\left\{\mathbf{f}_{1}, \ldots, \mathbf{f}_{T}\right\}$ is strictly stationary and independent of $\left\{\varepsilon_{1}, \ldots, \boldsymbol{\varepsilon}_{T}\right\}$. (ii) $\mathbf{f}_{t}^{\prime} \mathbf{f}_{t} \leq K<$ $\infty$, for all $t$. The $(m+1) \times(m+1)$ matrix $T^{-1} \mathbf{G}^{\prime} \mathbf{G}$, with $\mathbf{G}=\left(\mathbf{1}_{T}, \mathbf{F}\right)$, is a positive definite matrix for all $T$, and as $T \rightarrow \infty$, and $\mathbf{1}_{T}^{\prime} \mathbf{M}_{F} \mathbf{1}_{T}>0$ where $\mathbf{M}_{F}=\mathbf{I}_{T}-$ $\mathbf{F}\left(\mathbf{F}^{\prime} \mathbf{F}\right)^{-1} \mathbf{F}^{\prime}$. (iii) $\operatorname{cov}\left(\mathbf{f}_{t}\right)$ is strictly positive definite.

(A4) We assume that the estimator $\hat{\Omega}^{1 / 2}=\left(\hat{\omega}_{i j}\right)$ has at least a logarithmic rate of convergence

$$
\left\|\hat{\Omega}^{1 / 2}-\Omega^{1 / 2}\right\|_{L_{1}}=o_{p}\left\{\frac{1}{\log (N)}\right\}, \max _{1 \leqslant i \leqslant p}\left|\hat{\omega}_{i, i}-\omega_{i, i}\right|=o_{p}\left\{\frac{1}{\log (N)}\right\}
$$

Assumption (A1) assume that the error term follows the independent component model, which is widely used in high dimensional data analysis, such as Li et al. (2019); Chen et al. (2022). The assumption of the correlation matrix is the same as condition 1 and 2 in Cai et al. (2014). Assumption (A2) consider three types of tails of $\xi_{i t}$, which allows the dimension $N$ smaller as the tails gets heavier. Assumption (A3) is also widely assumed in high dimensional linear factor pricing model, such as Fan et al. (2015); Feng et al. (2022b). Assumption (A4) is the same as condition (8) in Cai et al. (2014), which is a rather weak requirement on $\hat{\Omega}$ and can be easily satisfied by many high dimensional precision matrix estimators, such as Bickel and Levina (2008); Cai et al. (2011).

Theorem 1 Under the condition (A1)-(A4), we have

$$
P_{H_{0}}\left(M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log (N)+\log \log (N) \leq x\right) \rightarrow F(x) \doteq \exp \{-(1 / \sqrt{\pi}) \exp (-x / 2)\}
$$

for any $x \in \mathbb{R}$.

Based on Theorem 1, a level $\gamma$ test will then be performed through rejecting $H_{0}$ when $M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log (N)+\log \{\log (N)\}$ is larger than the $1-\gamma$ quantile, $q_{\gamma}=-\log (\pi)-2 \log \{\log (1-$ $\left.\gamma)^{-1}\right\}$, of the type I extreme value distribution.

Next, we will show the consistency of the new proposed max-type test procedure. Define

$$
\mathcal{S}\left(k_{N}\right) \equiv\left\{\boldsymbol{\alpha} \in \mathcal{R}^{N}: \sum_{I=1}^{N} I\left(\alpha_{i} \neq 0\right)=k_{N}\right\}
$$

Here, $\mathcal{S}\left(k_{N}\right)$ denote the set of $k_{N}$-sparse vectors with $k_{N}=O\left(N^{r}\right)$ and $r<\frac{1}{4}$.

Theorem 2 Under the condition (A1)-(A4), as $\min (T, N) \rightarrow \infty$

$$
\inf _{\alpha \in \mathcal{A}(\beta) \cap \mathcal{S}\left(k_{N}\right)} P\left(\phi_{\gamma}=1\right) \rightarrow 1
$$

where $\phi_{\gamma} \equiv I\left[M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log (N)+\log \log (N) \geq q_{\gamma}\right], \beta \geq 1 / \min _{i}\left\{\omega_{i, i}^{2}\right\}+\epsilon$ for some constant $\epsilon>0$, and

$$
\mathcal{A}(\beta) \equiv\left\{\boldsymbol{\alpha} \equiv\left(\alpha_{1}, \ldots, \alpha_{N}\right) \in \mathcal{R}^{N}: \max _{1 \leq i<j \leq N}\left|\alpha_{i} / \sigma_{i i}^{1 / 2}\right| \geq \sqrt{8 \beta \log (N) / T}\right\}
$$

### 2.2 Adaptive Test

As shown in Theorem 2, the max-type test statistic $M_{\hat{\Omega}^{1 / 2}}$ has good performance under sparse alternatives. While for the dense alternatives, Pesaran and Yamagata (2017) proposed a sum-type test statistic:

$$
T_{\mathrm{PY}}=\frac{N^{-1 / 2} \sum_{i=1}^{N}\left\{t_{i}^{2}-v /(v-2)\right\}}{v /(v-2) \sqrt{2(v-1) /(v-4)\left\{1+(N-1) \tilde{\rho}_{M T}^{2}\right\}}}
$$

where $v=T-p-1$ and $\tilde{\rho}_{M T}=2 /\{N(N-1)\} \sum_{i=2}^{N} \sum_{j=1}^{i-1} \tilde{\rho}_{i j}^{2}$ is the corresponding correlation estimator of $\rho^{2}=2 /\{N(N-1)\} \sum_{i=2}^{N} \sum_{j=1}^{i-1} \rho_{i j}^{2}$ with $\tilde{\rho}_{i j}$ denoting the multiple testing estimator of the correlation $\rho_{i j}=\sigma_{i j} /\left(\sigma_{i i}^{1 / 2} \sigma_{j j}^{1 / 2}\right)$ (Bailey et al. 2019). Under the null hypothesis, we have $T_{P Y} \xrightarrow{d} N(0,1)$. Thus, we will reject the null hypothesis when $T_{P Y}>z_{\gamma}$ where $z_{\gamma}$ is the upper $\gamma$ quantile of the standard normal distribution.

In practice, we can not know whether the alternative is dense or sparse. So we proposed the following Fisher combination test statistic

$$
T_{F C 2}=-2 \log p_{\text {sum }}-2 \log p_{\max 2}
$$

where

$$
p_{\text {sum }}=1-\Phi\left(T_{P Y}\right), \quad p_{\max 2}=1-F\left(M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log N+\log \log (N)\right)
$$

To establish the asymptotic distribution of $T_{F C 2}$, we need the following additional conditions:

(A5) $\sup _{i, t} E\left(\left|\xi_{i t}\right|^{8+c}\right) \leq K<\infty$ for some $c>0$.

(A6) Let $\left\|\mathbf{R}^{1 / 2}\right\|_{1}<K$ and $\left\|\mathbf{R}^{1 / 2}\right\|_{\infty}<K$.

Assumption (A5) and (A6) are the same as Assumption 3 in Pesaran and Yamagata (2017). As shown in Remark 3 in Pesaran and Yamagata (2017), the sparse conditions of $\mathbf{R}$ is particularly important in finance where security returns could be affected by weak unobserved factors. Based on these assumptions, we can establish the asymptotic independence between the sum-type test statistic $T_{P Y}$ and the max-type test statistic $M_{\hat{\mathbf{\Omega}}^{1 / 2}}$.

Theorem 3 Under the conditions (A1), (A3)-(A6), we have, if $N / T^{2} \rightarrow 0$,

$$
P\left(T_{P Y}<x, M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log N+\log \log N<y\right) \rightarrow \Phi(x) F(y)
$$

Based on Theorem 3, we have the limit distribution of $T_{F C 2}$ as follow.

Corollary 1 Under the same condition as Theorem 3, we have $T_{F C 2} \xrightarrow{d} \chi_{4}^{2}$ under the null hypothesis.

Because the convergence rate of $T_{F C 2}$ is not very fast, we suggest to use the critical value $\left(1+\log ^{-1}\left(T N^{1 / 2}\right)\right) \chi_{4}^{2}(\gamma)$ in practice, where $\chi_{4}^{2}(\gamma)$ is the upper $\gamma$-quantile of $\chi_{4}^{2}$ distribution.

We consider the following alternative hypothesis:

$$
H_{1}: \tilde{\alpha}_{i} \neq 0, i \in \mathcal{M}, \quad|\mathcal{M}|=m, \quad m=o\left(N^{1 / 2}\right), \quad N^{-1} T \tilde{\boldsymbol{\alpha}}^{\top} \tilde{\boldsymbol{\alpha}}=o(1)
$$

where $\tilde{\boldsymbol{\alpha}}=\boldsymbol{\Omega}^{1 / 2} \boldsymbol{\alpha}$. Next, we also demonstrate that $T_{P Y}$ is still asymptotically independent with $M_{\hat{\Omega}^{1 / 2}}$ under this special alternatives.

Theorem 4 Under the conditions (A1), (A3)-(A6), we have, if $N / T^{2} \rightarrow 0$,

$P\left(T_{P Y}<x, M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log N+\log \log N<y\right) \rightarrow P\left(T_{P Y}<x\right) P\left(M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log N+\log \log N<y\right)$

under the alternative hypothesis (10).

Similar to the arguments in Wang and Feng (2023), we have

$$
\beta_{T_{F C 2}} \geq \beta_{\text {sum }, \gamma / 2}+\beta_{\max 2, \gamma / 2}-\beta_{\text {sum }, \gamma / 2} \beta_{\max 2, \gamma / 2}
$$

where $\beta_{\text {sum }}, \beta_{\max 2, \gamma}$ is the power function of the sum-type test $T_{P Y}$ and $M_{\hat{\Omega}^{1 / 2}}$ at significant value $\gamma$, respectively. For a small $\gamma$, the difference between $\beta_{\max 2, \gamma}$ and $\beta_{\max 2, \gamma / 2}$ should be small, and the same fact applies to $\beta_{\text {sum }, \gamma}$. Consequently, the power of the adaptive test $T_{F C 2}$ would be no smaller than or even significantly larger than that of either max-type or sum-type test.

## 3 Simulation

This experiment is designed to mimic the commonly used Fama-French three-factor model, where the factors $\mathbf{f}_{t}$ have strong serial correlation and heterogeneous variance. Specifically, we consider a modified version of the example studied in Section 5.1 of Pesaran and Yamagata (2017). The response $Y_{i t}$ are generated according to the LFPM in (1) with $p=3$ :

$$
Y_{i t}=\alpha_{i}+\sum_{k=1}^{p} \beta_{i k} f_{k t}+\varepsilon_{i t}
$$

where the three factors, $f_{t 1}, f_{t 2}$ and $f_{t 3}$, are the Fama-French three factors. We generate each factor from an autoregressive conditional heteroskedasticity process and the $\operatorname{GARCH}(1,1)$ model respectively. Specifically The data generating process is as follows:

$$
Y_{i t}=\alpha_{i}+\sum_{k=1}^{p} \beta_{i k} f_{k t}+\varepsilon_{i t}, i \in\{1, \cdots, N\}, t \in\{1, \cdots, T\}
$$

Let $p=3$. The three factors $f_{1 t}, f_{2 t}$ and $f_{3 t}$ are presented as the Fama-French three factors, Market factor, SMB and HML. We generate the factors as follows, where for each factor, the error term follows a $\operatorname{GARCH}(1,1)$ process, and all the coefficients are the same as that in Pesaran and Yamagata (2017). Specifically,

$$
\begin{aligned}
f_{1 t} & =0.53+0.06 f_{1, t-1}+h_{1 t}^{1 / 2} \zeta_{1 t}, \text { Market factor } \\
f_{2 t} & =0.19+0.19 f_{2, t-1}+h_{2 t}^{1 / 2} \zeta_{2 t}, \text { SMB factor } \\
f_{3 t} & =0.19+0.05 f_{3, t-1}+h_{3 t}^{1 / 2} \zeta_{3 t}, \text { HML factor }
\end{aligned}
$$

where $\zeta_{k t}$ 's are simulated from a standard normal distribution, the variance terms $h_{k t}$ 's are generated from

$$
\begin{aligned}
& h_{1 t}=0.89+0.85 h_{1, t-1}+0.11 \zeta_{1, t-1}^{2}, \text { Market factor } \\
& h_{2 t}=0.62+0.74 h_{2, t-1}+0.19 \zeta_{2, t-1}^{2}, \mathrm{SMB} \\
& h_{3 t}=0.80+0.76 h_{3, t-1}+0.15 \zeta_{3, t-1}^{2}, \text { HML }
\end{aligned}
$$

Similar to Pesaran and Yamagata (2017), the above process is simulated over the periods $t=-49, \cdots, 0,1, \cdots, T$ with the initial values $f_{k,-50}=0$ and $h_{k,-50}=1$ for any $k=1,2$ and 3. We use the simulated data for observations $t=1, \cdots, T$ for our final experiments.

The errors are generated from $\boldsymbol{\varepsilon}_{t} \sim \boldsymbol{\Sigma}^{1 / 2} \boldsymbol{z}_{t}$, where $\boldsymbol{z}_{t}=\left(z_{1 t}, \cdots, z_{N t}\right)^{\top}$. We consider four settings of $z_{i t}$ 's:

(i) Normal distribution: $z_{i t} \stackrel{i . i . d}{\sim} N(0,1)$;

(ii) $t_{3}$ distribution: $z_{i t} \stackrel{i . i . d}{\sim} t(5) / \sqrt{5 / 3}$

(iii) mixture normal distribution: $z_{i t} \stackrel{i . i . d}{\sim}\{0.9 N(0,1)+0.1 N(0,9)\} / \sqrt{1.8}$

We consider four models for the covariance matrix

(1) Model 1: $\boldsymbol{\Sigma}=\left(0.7^{|i-j|}\right)_{1 \leq i, j \leq N}$;

(2) Model 2: $\boldsymbol{\Sigma}=\mathbf{D}^{1 / 2} \mathbf{R D}^{1 / 2}, \mathbf{D}=\operatorname{diag}\left\{\sigma_{1}^{2}, \cdots, \sigma_{N}^{2}\right\}$ and $\mathbf{R}=\mathbf{I}_{N}+\boldsymbol{b} \boldsymbol{b}^{\top}-\tilde{\mathbf{B}}$, where $\boldsymbol{b}=\left(b_{1}, \cdots, b_{N}\right)^{\top}$ and $\tilde{\mathbf{B}}=\operatorname{diag}\left\{b_{1}^{2}, \cdots, b_{N}^{2}\right\}$. We generate $\sigma_{i i} \sim U(1,2)$. We randomly generate $\left[N^{0.3}\right]$ elements of $\boldsymbol{b}$ from $U(0.7,0.9)$ and set the remaining elements to be zero. Here [.] denotes the integer part of a real number.

(3) Model 3: $\boldsymbol{\Sigma}=\boldsymbol{\Omega}^{-1}$ where $\boldsymbol{\Omega}=\left(0.6^{|i-j|}\right)_{1 \leq i, j \leq N}$;

(4) Model 4: $\boldsymbol{\Sigma}=\boldsymbol{\gamma} \boldsymbol{\gamma}^{T}+\left(\mathbf{I}_{p}-\rho_{\epsilon} \boldsymbol{W}\right)^{-1}\left(\mathbf{I}_{p}-\rho_{\epsilon} \boldsymbol{W}^{T}\right)^{-1}$, where $\boldsymbol{\gamma}=\left(\gamma_{1}, \cdots, \gamma_{\left[p^{\left.\delta_{\gamma}\right]}\right]}, 0,0, \cdots, 0\right)^{T}$. Here $\gamma_{i}$ with $i=1, \cdots,\left[p^{\delta_{\gamma}}\right]$ are generated independently from $\operatorname{Uniform}(0.7,0.9)$. Let $\rho_{\epsilon}=0.5$ and $\delta_{\gamma}=0.3$. Let $\boldsymbol{W}=\left(w_{i_{1} i_{2}}\right)_{1 \leq i_{1}, i_{2} \leq p}$ have a so-called rook form, i.e., all elements of $\boldsymbol{W}$ are zero except that $w_{i_{1}+1, i_{1}}=w_{i_{2}-1, i_{2}}=0.5$ for $i_{1}=1, \cdots, p-2$ and $i_{2}=3, \cdots, p$, and $w_{1,2}=w_{p, p-1}=1$.

Here $P Y$ means $T_{P Y}$, MAX1 means $M_{\mathbf{I}}$, MAX2 means $M_{\hat{\mathbf{\Omega}}^{1 / 2}}, H C 1$ means $T_{F C 1}$ which is the Fisher combination test based on $T_{P Y}$ and $M_{\mathrm{I}}, \mathrm{HC} 2$ means $T_{F C 2}$, COM means the combination method proposed by Feng et al. (2022b). PE means the power enhancement

Table 1: Sizes of tests with $T=100$.

| Method | Model 1 |  |  |  | Model 2 |  |  |  | Model 3 |  |  |  | Model 4 |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | $N$ |  |  |  | $N$ |  |  |  | $N$ |  |  |  | $N$ |  |  |  |
|  | 50 | 100 | 200 | 300 | 50 | 100 | 200 | 300 | 50 | 100 | 200 | 300 | 50 | 100 | 200 | 300 |
| Normal Errors |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PY | 6.2 | 6.1 | 7.9 | 7.8 | 5.7 | 6.1 | 7.3 | 5.5 | 5.8 | 5.8 | 5.4 | 4.4 | 5.3 | 6.4 | 4.9 | 4.5 |
| MAX1 | 3.1 | 4.6 | 4.6 | 4.6 | 4.1 | 3.5 | 4.2 | 5 | 3.2 | 5.3 | 5.5 | 5.2 | 3.6 | 5.3 | 4.5 | 4.9 |
| MAX2 | 8.2 | 6.9 | 4.8 | 5.3 | 3.9 | 3.6 | 5 | 7.4 | 4.1 | 5.2 | 5.4 | 5.2 | 4 | 5.6 | 4.4 | 5 |
| FC1 | 4.9 | 5.6 | 6.1 | 6.7 | 5.2 | 5.3 | 5.1 | 4 | 4.8 | 5.7 | 5 | 4.5 | 4.7 | 6.1 | 4.8 | 4.5 |
| $\mathrm{FC} 2$ | 6.4 | 6.4 | 6.6 | 6.2 | 5.2 | 5.4 | 5.4 | 5.9 | 5.4 | 5.6 | 4.9 | 4.5 | 4.9 | 6.4 | 4.9 | 4.5 |
| COM | 5.1 | 4.9 | 5.6 | 6.8 | 5.1 | 5.2 | 6.5 | 5.1 | 4.9 | 5.7 | 5.3 | 4.2 | 3.9 | 6.1 | 5 | 4.1 |
| $\mathrm{PE}$ | 22.8 | 20.1 | 14.3 | 12.2 | 6.5 | 8.4 | 10.4 | 12 | 9.9 | 11.9 | 12.1 | 12.4 | 9 | 12.5 | 11 | 13.1 |
| $t(5)$ Errors |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PY | 7.8 | 6.9 | 6.8 | 5.7 | 5.2 | 4.1 | 4.6 | 4 | 5.7 | 4.4 | 6 | 5.7 | 6.2 | 5.3 | 5.5 | 4.5 |
| MAX1 | 3.9 | 2.6 | 3.8 | 4.4 | $J$ | 4.7 | 3.8 | 4.1 | 3.4 | 3.3 | 3.5 | 4.7 | 3.7 | 4.2 | 3.9 | 4.3 |
| MAX2 | 8.1 | 5.4 | 5.2 | 4.4 | 2.9 | 4.6 | 4.7 | 6.5 | 3.5 | 3.3 | 3.6 | 4.9 | 3.7 | 4.3 | 4 | 4.4 |
| FC1 | 6.8 | 5.2 | 6.6 | 5.4 | 3.7 | 3.4 | 3.5 | 3.4 | 4.7 | 3.7 | 4.6 | 5.5 | 5.6 | 4.4 | 3.9 | 3.4 |
| FC2 | 8.6 | 5.8 | 6.5 | 4.8 | 3.7 | 3.4 | 3.9 | 4.9 | 4.9 | 3.5 | 4.6 | 5.5 | 5.3 | 4.2 | 4 | 3.6 |
| COM | 5.8 | 5.8 | 6.2 | 5.5 | 3.7 | 3.5 | 4.3 | 3.6 | 4.7 | 3.7 | 4.2 | 6.4 | 5.7 | 3.9 | 5.4 | 3.2 |
| $\mathrm{PE}$ | 23.1 | 19.3 | 16.9 | 9.6 | 5.7 | 5.9 | 9.6 | 11.6 | 9.3 | 9.5 | 11.9 | 12.2 | 10.1 | 10.4 | 10.9 | 10.9 |
| Mixture Normal Errors |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PY | 7.1 | 5.5 | 6.4 | 7.5 | 5.6 | 6.7 | 5.4 | 4.2 | 5.3 | 7 | 3.8 | 5.9 | 5.4 | 4.8 | 5.3 | 6.1 |
| MAX1 | 2.7 | 3.4 | 4.5 | 4.1 | 2.3 | 4.3 | 2.2 | 4.3 | 3.3 | 4 | 4.7 | 3.3 | 3.6 | 3.8 | 4 | 3.3 |
| MAX2 | 8.4 | 5.5 | 3.5 | 4.8 | 2.3 | 4.3 | 2.8 | 6.8 | 3.2 | 3.5 | 4.9 | 3.6 | 4.2 | 4.1 | 4.1 | 3.6 |
| FC1 | 5.5 | 4.4 | 5.3 | 6 | 3.7 | 6.1 | 3.4 | 3.8 | 4.3 | 5.5 | 5 | 4.4 | 4.3 | 3.7 | 4.7 | 4 |
| $\mathrm{FC} 2$ | 8.1 | 4.4 | 5.4 | 6.2 | 3.6 | 6.2 | 3.6 | 5.2 | 4.2 | 5.6 | 5.2 | 4.3 | 4.1 | 4 | 4.5 | 4.3 |
| COM | 5.5 | 4.6 | 5.2 | 6 | 3.7 | 5.8 | 4.3 | 3.7 | 4 | 5.6 | 4.8 | 5.3 | 4.2 | 3.7 | 4.7 | 4.2 |
| PE | 24.2 | 17.1 | 12.5 | 10.2 | 7.2 | 9.2 | 9.2 | 12.8 | 9.7 | 12.6 | 10 | 13.5 | 9.3 | 9.2 | 10.4 | 11.2 |

method proposed by Fan et al. (2015). We estimate the covariance matrix by the thresholding method proposed by Bickel and Levina (2008). For fair comparison, we use the same covariance estimator in PE. Finally, the three groups of coefficients corresponding to the three factors, $\beta_{i 1}, \beta_{i 2}$ and $\beta_{i 3}$, are generated independently from $U(0.2,2), U(-1,1.5)$ and $U(-1.5,1.5)$, respectively. We set $\boldsymbol{\alpha}=\mathbf{0}$ under the null hypothesis. Table 1 reports the empirical sizes of each test with sample size $T=100$. We found that PE can not control the empirical sizes in most cases. However, the other methods can control the empirical sizes very well. So we do not consider the PE method in power comparison.

To compare the power performance of the various tests under different sparsity of $\boldsymbol{\alpha}$, we present the empirical power of each test under different number of nonzero elements of $\boldsymbol{\alpha}$. For illustration, here we only consider $T=100, N=200$. Specifically, given the number of nonzero elements of $\boldsymbol{\alpha}$, i.e. $m \in\{1, \cdots, 20\}$, we randomly choose a subset $S$ from $\{1, \cdots, N\}$ with $|S|=m$ and let $\alpha_{i}=\sqrt{\frac{10 \log (N)}{m T}}$ for $i \in S$, such that the signal strength $\|\boldsymbol{\alpha}\|^{2}$ is fixed for each $m$. Figure 143 show the power curves of each tests under different error distributions.

In Model 2-4, the newly introduced max-type test, denoted as $M_{\hat{\mathbf{\Omega}}^{1 / 2}}$, exhibits a performance that is comparable to $M_{\mathbf{I}}$, as referenced in Feng et al. (2022b). When we consider varying degrees of sparsity, it is observed that the sum-type test $T_{P Y}$ surpasses the max-type tests $M_{\hat{\mathbf{\Omega}}^{1 / 2}}$ and $M_{\mathbf{I}}$ as the value of $m$ increases. However, when $m$ is relatively small, the max-type tests outperform the sum-type test $T_{P Y}$.

The combination tests demonstrate more consistent results across different levels of sparsity. Notably, when $m$ is neither too large nor too small, these combination tests prove to be more potent than both the max-type and sum-type tests. These observations align with our theoretical findings and corroborate many existing studies, such as Feng et al. (2022a b); Chen et al. (2022).

Moreover, in Model 1, $M_{\hat{\mathbf{\Omega}}^{1 / 2}}$ demonstrates significantly higher power than $M_{\mathbf{I}}$, underscoring the benefits of accounting for error correlation. As a result, the newly proposed adaptive test $T_{F C 2}$ outperforms both $T_{F C 1}$ and COM tests.

## 4 Conclusion

In this study, we initially introduce a novel max-type test statistic that takes into account the correlation among errors and exhibits superior performance under sparse alternatives. For broader alternatives, we suggest a Fisher combination test, which is predicated on the asymptotic independence between the newly proposed max-type test statistic and the sumtype test statistic from Pesaran and Yamagata (2017). The efficacy of the proposed methods is further demonstrated through simulation studies.

Looking ahead, we propose several directions for future research. Firstly, the assumption of a constant regression coefficient may not hold in real-world scenarios. Therefore, numerous studies, such as Ma et al. (2020) and Ma et al. (2024a), have explored the testing of alpha in the high-dimensional time-varying factor model. It would be intriguing to propose a new max-type test and an adaptive test that standardizes the corresponding $t$-test statistic in

Figure 1: Power of tests with different numbers of nonzero alpha at $T=100, N=200$ with normal errors.

![](https://cdn.mathpix.com/cropped/2024_04_26_35e35e7eecefb02bf89ag-10.jpg?height=1872&width=1504&top_left_y=365&top_left_x=300)

- PY - MAX2 - - FC2
- MAX1 + FC1 *. COM
![](https://cdn.mathpix.com/cropped/2024_04_26_35e35e7eecefb02bf89ag-10.jpg?height=1786&width=1506&top_left_y=450&top_left_x=294)

the high-dimensional time-varying factor model. Secondly, the assumption of independence

Figure 2: Power of tests with different numbers of nonzero alpha at $T=100, N=200$ with $t(5)$ errors.

![](https://cdn.mathpix.com/cropped/2024_04_26_35e35e7eecefb02bf89ag-11.jpg?height=1873&width=1510&top_left_y=375&top_left_x=297)

$$
\begin{aligned}
& \rightarrow P Y \quad M \cdot M A X 2 \cdot \mathbb{F C} 2 \\
& \triangle \operatorname{MAX} 1+\mathrm{FC} 1 \text { * } \operatorname{CON}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_04_26_35e35e7eecefb02bf89ag-11.jpg?height=1792&width=1496&top_left_y=452&top_left_x=304)

Figure 3: Power of tests with different numbers of nonzero alpha at $T=100, N=200$ with mixture normal errors.

![](https://cdn.mathpix.com/cropped/2024_04_26_35e35e7eecefb02bf89ag-12.jpg?height=1870&width=1504&top_left_y=366&top_left_x=300)

for the error term can be restrictive in practice. Thus, considering an adaptive test pro-
cedure with dependent observations, as suggested by Ma et al. (2024b), poses a significant and interesting challenge. Finally, the independent component model, unfortunately, does not accommodate certain heavy-tailed distributions, such as the multivariate $t$-distribution. This is a limitation, given that financial data often exhibit heavy tails. Robust sum-type test procedures based on spatial signs for high-dimensional factor pricing models have been proposed by Liu et al. (2023), Zhao et al. (2022). The extension of these methods to our paper, particularly in conjunction with traditional spatial sign methods for sparse alternatives, is an area that warrants further exploration.

## 5 Appendix

### 5.1 Proof of Theorem 1

By the definition of $\hat{\alpha}_{i}$, we have $\hat{\alpha}_{i}=\sum_{t=1}^{T} \varepsilon_{i t} c_{t}$ where $\boldsymbol{c}=\left(c_{1}, \cdots, c_{T}\right)^{\top}=\left(\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}\right)^{-1} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}$. Let $\epsilon_{i t}=\varepsilon_{i t} / \sigma_{i i}^{1 / 2}$. We rewrite

$$
\tilde{t}=\sum_{t=1}^{T} \epsilon_{i t} h_{t}
$$

where $\boldsymbol{h}=\left(h_{1}, \cdots, h_{T}\right)^{\top}=\left(\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}\right)^{-1 / 2} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}$. And we have $\sum_{t=1}^{T} h_{t}^{2}=1$.

Under condition (A1), we have $\boldsymbol{\Omega}^{1 / 2} \tilde{\boldsymbol{t}}=\boldsymbol{v}=\left(v_{1}, \ldots, v_{N}\right)$ where $v_{i}=\sum_{t=1}^{T} \xi_{i t} h_{t}$. Thus, taking the same procedure as Theorem 1 in Feng et al. (2022b), we have

$$
P\left(\max _{1 \leq i \leq N}\left|v_{i}\right| \leq \sqrt{2 \log (N)-\log \log (N)+x}\right) \rightarrow \exp \left\{-\frac{1}{\sqrt{\pi}} \exp \left(-\frac{x}{2}\right)\right\}
$$

By the definition, we have $\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}=\boldsymbol{\nu}=\left(\nu_{1}, \ldots, \nu_{N}\right)$ and

$$
\begin{gathered}
||\left|\boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\left\|_{\infty}-\right\| \boldsymbol{\Omega}^{1 / 2} \tilde{\boldsymbol{t}}\left\|_{\infty} \mid \leq\right\| \boldsymbol{\Omega}^{1 / 2}(\boldsymbol{t}-\tilde{\boldsymbol{t}})\left\|_{\infty} \leq\right\| \boldsymbol{t}-\tilde{\boldsymbol{t}}\left\|_{\infty}\right\| \boldsymbol{\Omega}^{1 / 2} \|_{L_{1}}\right. \\
|| \hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}\left\|_{\infty}-\right\| \boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\left\|_{\infty} \mid \leq\right\|\left(\hat{\boldsymbol{\Omega}}^{1 / 2}-\boldsymbol{\Omega}^{1 / 2}\right) \boldsymbol{t}\left\|_{\infty} \leq\right\| \boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\left\|_{\infty}\right\|\left(\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{\Omega}^{-1 / 2}-\mathbf{I}_{N}\right) \|_{L_{1}}
\end{gathered}
$$

By the triangle inequality, we have

$$
\begin{aligned}
\|\boldsymbol{t}-\tilde{\boldsymbol{t}}\|_{\infty} & =\max _{1 \leq i \leq N}\left|(\boldsymbol{t}-\tilde{\boldsymbol{t}})_{i}\right|=\max _{1 \leq i \leq N}\left|\frac{\hat{\alpha}_{i} \sqrt{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}}{\hat{\sigma}_{i i}^{1 / 2}}-\frac{\hat{\alpha}_{i} \sqrt{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}}{\sigma_{i i}^{1 / 2}}\right| \\
& \leq \max _{1 \leq i \leq N}\left|\frac{\hat{\alpha}_{i} \sqrt{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}}{\sigma_{i i}^{1 / 2}}\right| \max _{1 \leq i \leq N}\left|\frac{\sigma_{i i}^{1 / 2}}{\hat{\sigma} i i^{1 / 2}}-1\right|
\end{aligned}
$$

By Lemma E. 2 and Proposition 4.1 in Fan et al. (2015), for some $c>0$, we have

$$
P\left\{\max _{1 \leq i \leq N}\left|\hat{\sigma}_{i, i}-\sigma_{i, i}\right|>c \sqrt{\log (N) / T}\right\} \rightarrow 0
$$

$$
P\left\{\frac{4}{9} \leq \frac{\hat{\sigma}_{i, i}}{\sigma_{i, i}} \leq \frac{9}{4}, i=1, \ldots, N\right\} \rightarrow 1
$$

Thus, with probability to one,we have

$$
\begin{aligned}
\max _{1 \leq i \leq N}\left|\frac{\sigma_{i i}^{1 / 2}}{\hat{\sigma}_{i i}^{1 / 2}}-1\right| & \leq \max _{1 \leq i \leq N} \frac{1}{\hat{\sigma}_{i i}^{1 / 2}} \max _{1 \leq i \leq N}\left|\sigma_{i i}^{1 / 2}-\hat{\sigma}_{i i}^{1 / 2}\right| \\
& \leq \frac{3}{2} \max _{1 \leq i \leq N} \frac{1}{\sigma_{i i}^{1 / 2}} \max _{1 \leq i \leq N}\left|\sigma_{i i}-\hat{\sigma}_{i i}\right|^{1 / 2}=O_{p}\left(\left\{\frac{\log (N)}{T}\right\}^{1 / 4}\right)
\end{aligned}
$$

And by Theorem 1 in Feng et al. (2022b), we have

$$
\max _{1 \leq i \leq N}\left|\frac{\hat{\alpha}_{i} \sqrt{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}}{\sigma_{i}^{1 / 2}}\right|=O_{p}(\sqrt{\log (N)})
$$

which leads to

$$
\max _{1 \leq i \leq N}\left|\frac{\hat{\alpha}_{i} \sqrt{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}}{\hat{\sigma}_{i i}^{1 / 2}}-\frac{\hat{\alpha}_{i} \sqrt{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}}{\sigma_{i i}^{1 / 2}}\right|=O_{p}\left(\frac{\{\log (N)\}^{3 / 4}}{T^{1 / 4}}\right) \rightarrow 0
$$

due to $\log (N)=o\left(T^{1 / 4}\right)$. So $\left\|\boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\right\|_{\infty}-\left\|\boldsymbol{\Omega}^{1 / 2} \tilde{\boldsymbol{t}}\right\|_{\infty}=o_{p}(1)$. By 12), we have $\left\|\boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\right\|_{\infty}=$ $O_{p}\left(\{\log (N)\}^{1 / 2}\right)$. By condition (A4), we have $\left\|\left(\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{\Omega}^{-1 / 2}-\mathbf{I}_{N}\right)\right\|_{L_{1}}=o_{p}\left(\log ^{-1}(N)\right)$. So $\left\|\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}\right\|_{\infty}-\left\|\boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\right\|_{\infty}=o_{p}(1)$. Hence, we have

$$
P\left(\max _{1 \leq i \leq N}\left|\nu_{i}\right| \leq \sqrt{2 \log (N)-\log \log (N)+x}\right) \rightarrow \exp \left\{-\frac{1}{\sqrt{\pi}} \exp \left(-\frac{x}{2}\right)\right\}
$$

Thus,

$$
P\left(M_{\hat{\mathbf{\Omega}}^{1 / 2}}-2 \log (N)+\log \log (N) \leq x\right) \rightarrow F(x)
$$

where

$$
M_{\hat{\mathbf{\Omega}}^{1 / 2}}=\max _{1 \leq i \leq N} \nu_{i}^{2}
$$

Here we obtain the result.

### 5.2 Proof of Theorem 2

It suffices to prove

$$
P\left(\max _{1 \leq i \leq N}\left|\left(\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}\right)_{i}\right| \geq \sqrt{2 \log (N)-\log \{\log (N)\}+q_{\gamma}}\right) \rightarrow 1
$$

According to the proof of Theorem 1, we have

$$
P_{H_{0}}\left(\max _{1 \leq i \leq N}\left(\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}\right)_{i}^{2}-2 \log (N)+\log \{\log (N)\} \leq x\right) \rightarrow \exp \left\{-\frac{1}{\sqrt{\pi}} \exp \left(-\frac{x}{2}\right)\right\}
$$

By lemma 3 in Cai et al. (2014), for $k_{N}$-sparse $\boldsymbol{t}, r<\frac{1}{4}$, we have, for any $2 r<a<1-2 r$, as $p \rightarrow \infty$

$$
P\left(\max _{i \in H}\left|\left(\boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\right)_{i}-\omega_{i, i} t_{i}\right|=O_{p}\left(N^{r-a / 2}\right) \max _{i \in H}\left|t_{i}\right|\right) \rightarrow 1
$$

where $H$ is the support of $\boldsymbol{t}$. And as $\left\|\hat{\boldsymbol{\Omega}}^{1 / 2} \boldsymbol{t}\right\|_{\infty}-\left\|\boldsymbol{\Omega}^{1 / 2} \boldsymbol{t}\right\|_{\infty}=o_{p}(1)$, we have

$$
P_{H_{0}}\left(\max _{1 \leq i \leq N}\left(\omega_{i, i} t_{i}\right)^{2}-2 \log (N)+\log \{\log (N)\} \leq x\right) \rightarrow \exp \left\{-\frac{1}{\sqrt{\pi}} \exp \left(-\frac{x}{2}\right)\right\}
$$

Thus,

$$
P\left(\max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\left(\hat{\alpha}_{i}-\alpha_{i}\right)^{2} \mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}}{\hat{\sigma}_{i, i}} \leq 2 \log (N)-\frac{1}{2} \log \{\log (N)\}\right) \rightarrow 1
$$

when we set $x=\frac{1}{2} \log \log (N)$. By the triangle inequality, we have

$$
\begin{aligned}
& \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \hat{\alpha}_{i}^{2}}{\hat{\sigma}_{i, i}} \\
\geq & \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}^{2}}{2 \hat{\sigma}_{i, i}}-\max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}\left(\hat{\alpha}_{i}-\alpha_{i}\right)^{2}}{\hat{\sigma}_{i, i}} \\
\geq & \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}^{2}}{2 \sigma_{i, i}}-\max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T}\left(\hat{\alpha}_{i}-\alpha_{i}\right)^{2}}{\hat{\sigma}_{i, i}}-\sqrt{\frac{\log (N)}{T}} \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}^{2}}{2 \sigma_{i, i}} \\
\geq & 4 \log (N)-2 \log (N)+\frac{1}{2} \log \log (N)-\sqrt{\frac{\log (N)}{T}} \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}^{2}}{2 \sigma_{i, i}}
\end{aligned}
$$

with probability tending to 1 . If $\max _{1 \leq i<j \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}{ }^{2}}{2 \sigma_{i, i}}=O\{\log (N)\}$

$$
\begin{aligned}
\max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}^{2}}{2 \sigma_{i, i}} & \geq 4 \log (N)-2 \log (N)+\frac{1}{2} \log \{\log (N)\}-O\left(\sqrt{\frac{\{\log (N)\}^{3}}{T}}\right) \\
& \geq 2 \log (N)-\log \{\log (N)\}+q_{\gamma}
\end{aligned}
$$

which implies $P\left(\phi_{\gamma}=1\right) \rightarrow 1$. If $\log ^{-1}(N) \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \alpha_{i}{ }^{2}}{2 \sigma_{i, i}} \rightarrow \infty$

$$
\max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \hat{\alpha}_{i}^{2}}{\hat{\sigma}_{i, i}} \geq \frac{4}{9} \max _{1 \leq i \leq N} \omega_{i, i}^{2} \frac{\mathbf{1}_{T}^{\top} \mathbf{M}_{\mathbf{F}} \mathbf{1}_{T} \hat{\alpha}_{i}^{2}}{\sigma_{i, i}} \geq 2 \log (N)-\log \{\log (N)\}+q_{\gamma}
$$

Thus, $P\left(\phi_{\gamma}=1\right)$ converges to one.

### 5.3 Some useful Theorems and Lemmas

We also restate Lemma S. 10 in Feng et al. (2022a) here.

Lemma 1 Let $\left\{\left(U, U_{N}, \tilde{U}_{N}\right) \in \mathbb{R}^{3} ; N \geq 1\right\}$ and $\left\{\left(V, V_{N}, \tilde{V}_{N}\right) \in \mathbb{R}^{3} ; N \geq 1\right\}$ be two sequences of random variables with $U_{N} \rightarrow U$ and $V_{N} \rightarrow V$ in distribution as $N \rightarrow \infty$. Assume $U$ and $V$ are continuous random variables. We assume that

$$
\tilde{U}_{N}=U_{N}+o_{p}(1), \tilde{V}_{N}=V_{N}+o_{p}(1)
$$

If $U_{N}$ and $V_{N}$ are asymptotically independent, then $\tilde{U}_{N}$ and $\tilde{V}_{N}$ are also asymptotically independent.

Define $B_{i}=\left\{v_{i}^{2}>l_{N}\right\}$ and $A_{N}(x)=\left\{\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}<x\right\}$. Define $l_{N}=2 \log (N)-$ $2 \log \log (N)+y$. We first proof the following important lemma. Define $h(y)=\frac{1}{\sqrt{\pi}} e^{-y / 2}$.

Lemma 2 Under the assumption of Theorem 3, for each $d \geq 1$, we have

$$
\lim _{N \rightarrow \infty} H(d, N) \leq \frac{1}{d !} h^{d}(y)<\infty
$$

where $H(d, N) \doteq \sum_{1 \leq i_{1}<\cdots<i_{d} \leq N} P\left(B_{i_{1}} \cdots B_{i_{d}}\right)$. And then, we have

$$
\sum_{1 \leq i_{1}<\cdots<i_{d} \leq N}\left|P\left(A_{N}(x) B_{i_{1}} \cdots B_{i_{d}}\right)-P\left(A_{N}(x)\right) \cdot P\left(B_{i_{1}} \cdots B_{i_{d}}\right)\right| \rightarrow 0
$$

as $N \rightarrow \infty$.

Proof. According to the proof of Theorem 1 in Feng et al. (2022b), we have

$$
N P\left(v_{i}^{2} \geq l_{N}\right)=2 N\left(1-\Phi\left(\sqrt{l_{N}}\right)\right)+o(1)=\frac{1}{\sqrt{\pi}} e^{-y / 2}+o(1)
$$

as $T, N \rightarrow \infty$ and $N / T^{2} \rightarrow 0$. Because $N P\left(B_{i}\right) \rightarrow h(y)$, we have $N B\left(B_{i}\right)<h(y)+\epsilon$ for any $\epsilon>0$ as $N \rightarrow \infty$. By the independence of $z_{i}$, we have

$$
\begin{aligned}
H(d, N) & =\sum_{1 \leq i_{1}<\cdots<i_{d} \leq N} P\left(B_{i_{1}} \cdots B_{i_{d}}\right)=\sum_{1 \leq i_{1}<\cdots<i_{d} \leq N} \prod_{k=1}^{d} P\left(B_{i_{k}}\right) \\
& \leq C_{N}^{d}\left\{N^{-1}(h(y)+\epsilon)\right\}^{d} \leq \frac{1}{d !}(h(y)+\epsilon)^{d}
\end{aligned}
$$

So, by letting $\epsilon \rightarrow 0$, we have

$$
\lim _{N \rightarrow \infty} H(d, N) \leq \frac{1}{d !} h^{d}(y)<\infty
$$

Here we prove (16).

Additionally, because of $e^{x} \leq 1+(1+\epsilon)|x|$ for $x<\epsilon$, we have

$$
\begin{aligned}
E\left(\exp \left(\lambda v_{i}\right)\right) & \left.=\prod_{t=1}^{T} E\left(e^{\lambda \xi_{i t} h_{t}}\right) \leq \prod_{t=1}^{T}\left(1+(1+\epsilon) \lambda E\left(\left|\xi_{i t} h_{t}\right|\right)\right)\right) \\
& \left.\leq\left(1+(1+\epsilon) C_{h} K^{1 /(8+c)} T^{-1 / 2} \lambda\right)\right)^{T} \\
& \leq \exp \left((1+\epsilon)^{2} C_{h}^{2} K^{2 /(8+c)} \lambda^{2}\right)
\end{aligned}
$$

Thus, we have $v_{i}$ is a sub-gaussian random variable. So there exist $\eta>0$ and $K>0$ such that $E\left(\exp \left(\eta v_{i}^{2}\right)\right) \leq K$.

Define $\boldsymbol{v}=\left(\boldsymbol{v}_{1}, \boldsymbol{v}_{2}\right)$ where $\boldsymbol{v}_{1}=\left(v_{1}, \cdots, v_{d}\right)$ and $\boldsymbol{v}_{2}=\left(v_{d+1}, \cdots, v_{N}\right)$. And

$$
\mathbf{R}=\left(\begin{array}{ll}
\mathbf{R}_{11} & \mathbf{R}_{12} \\
\mathbf{R}_{21} & \mathbf{R}_{22}
\end{array}\right)
$$

So,

$$
\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}=\boldsymbol{v}_{1}^{\top} \mathbf{R}_{11} \boldsymbol{v}_{1}+2 \boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2}+\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}
$$

Because $\lambda_{\max }\left(\mathbf{R}_{11}\right) \leq \lambda_{\max }(\mathbf{R})<c$,

$$
\begin{aligned}
P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{11} \boldsymbol{v}_{1}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) & \leq P\left(c \boldsymbol{v}_{1}^{\top} \boldsymbol{v}_{1}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \\
& =P\left(\eta \sum_{i=1}^{d} z_{i}^{2}>c^{-1} \eta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \\
& \leq \exp \left(-c^{-1} \eta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(e^{\eta \sum_{i=1}^{d} z_{i}^{2}}\right) \\
& =\exp \left(-c^{-1} \eta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right)\left\{E\left(e^{\eta z_{i}^{2}}\right)\right\}^{d} \\
& \leq K^{d} \exp \left(-c^{-1} \eta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right)
\end{aligned}
$$

By the assumption (iii), we have ${\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}^{2} \geq 2 \operatorname{tr}\left(\mathbf{R}^{2}\right) \geq 2 c^{-2} N$. So

$$
P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{11} \boldsymbol{v}_{1}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \leq K^{d} \exp \left(-\sqrt{2} c^{-2} \eta \epsilon N^{1 / 2}\right)
$$

Define $\mathbf{A}=\mathbf{Q}^{\top} \boldsymbol{\Lambda} \mathbf{Q}$ where $\mathbf{Q}=\left(q_{i j}\right)_{1 \leq i, j \leq p}$ is an orthogonal matrix and $\boldsymbol{\Lambda}=\operatorname{diag}\left\{\lambda_{1}, \ldots, \lambda_{N}\right\}, \lambda_{i}, i=$ $1, \ldots, N$ are the eigenvalues of $\mathbf{A}$. Note that $\sum_{1 \leq j \leq N} a_{i j}^{2}$ is the $i$ th diagonal element of $\mathbf{A}^{2}=\mathbf{Q}^{\top} \boldsymbol{\Lambda}^{2} \mathbf{Q}$, we have $\sum_{1 \leq j \leq N} a_{i j}^{2}=\sum_{l=1}^{N} q_{l i}^{2} \lambda_{l}^{2} \leq c^{2}$ according to Assumption (ii).

Next, define $\theta=\sqrt{\frac{2 \eta}{d c^{2} \sigma^{2}}}$, we have

$$
P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2} \geq \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \leq \exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\exp \left(\theta \boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2}\right)\right)
$$

$$
\begin{aligned}
& =\exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(e^{\theta \sum_{i=1}^{d} \sum_{j=d+1}^{N} a_{i j} z_{i} z_{j}}\right) \\
& \leq \exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(E\left(e^{\theta \sum_{j=d+1}^{N}\left(\sum_{i=1}^{d} a_{i j} z_{i}\right) z_{j}} \mid \boldsymbol{v}_{1}\right)\right) \\
& =\exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\prod_{j=d+1}^{N} E\left(e^{\left(\theta \sum_{i=1}^{d} a_{i j} z_{i}\right) z_{j}} \mid \boldsymbol{v}_{1}\right)\right) \\
& \leq \exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\prod_{j=d+1}^{N} \exp \left(\frac{\sigma^{2} \theta^{2}}{2}\left(\sum_{i=1}^{d} a_{i j} z_{i}\right)^{2}\right)\right) \\
& =\exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\exp \left(\frac{\sigma^{2} \theta^{2}}{2} \sum_{j=d+1}^{N}\left(\sum_{i=1}^{d} a_{i j} z_{i}\right)^{2}\right)\right) \\
& \leq \exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\exp \left(\frac{d \sigma^{2} \theta^{2}}{2} \sum_{j=d+1}^{N} \sum_{i=1}^{d} a_{i j}^{2} z_{i}^{2}\right)\right) \\
& \leq \exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\exp \left(\frac{d c^{2} \sigma^{2} \theta^{2}}{2} \sum_{i=1}^{d} z_{i}^{2}\right)\right) \\
& =\exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) E\left(\exp \left(\eta \sum_{i=1}^{d} z_{i}^{2}\right)\right) \\
& \leq K^{d} \exp \left(-\theta \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \leq K^{d} \exp \left(-\sqrt{2} c^{-1} \theta \epsilon N^{1 / 2}\right)
\end{aligned}
$$

So

$$
P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2} \geq \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \leq K^{d} \exp \left(-\sqrt{\frac{4 \eta}{d c^{4} \sigma^{2}}} \epsilon N^{1 / 2}\right)
$$

Similarly, we also can prove that

$$
P\left(\left(-\boldsymbol{v}_{1}\right)^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2} \geq \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \leq K^{d} \exp \left(-\sqrt{\frac{4 \eta}{d c^{4} \sigma^{2}}} \epsilon N^{1 / 2}\right)
$$

Let $\Theta_{p}=\boldsymbol{v}_{1}^{\top} \mathbf{R}_{11} \boldsymbol{v}_{1}+2 \boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2}$.

$$
\begin{aligned}
& P\left(\left|\Theta_{N}\right|>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \\
\leq & P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{11} \boldsymbol{v}_{1}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)} / 2\right)+P\left(\left|\boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2}\right|>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)} / 4\right) \\
\leq & P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{11} \boldsymbol{v}_{1}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)} / 2\right)+P\left(\boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)} / 8\right)+P\left(-\boldsymbol{v}_{1}^{\top} \mathbf{R}_{12} \boldsymbol{v}_{2}>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)} / 8\right)
\end{aligned}
$$

So, by (18), (19) and (20), there exist a constant $c_{\epsilon}>0$,

$$
P\left(\left|\Theta_{N}\right|>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \leq K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right)
$$

$$
\begin{aligned}
& P\left(A_{N}(x) B_{1} \cdots B_{d}\right) \\
& =P\left(\frac{\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}-\operatorname{tr}(\mathbf{R})+\Theta_{N}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x, B_{1} \cdots B_{d}\right) \\
& \leq P\left(\frac{\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}-\operatorname{tr}(\mathbf{R})+\Theta_{N}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x,\left|\Theta_{N}\right| \leq \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}, B_{1} \cdots B_{d}\right)+P\left(\left|\Theta_{N}\right|>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right) \\
& \leq P\left(\frac{\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x+\epsilon, B_{1} \cdots B_{d}\right)+K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right) \\
& =P\left(\frac{\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x+\epsilon\right) P\left(B_{1} \cdots B_{d}\right)+K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right) \\
& \leq\left[P\left(\frac{\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}-\operatorname{tr}(\mathbf{R})+\Theta_{N}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x+\epsilon,\left|\Theta_{N}\right| \leq \epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right)+P\left(\left|\Theta_{N}\right|>\epsilon \sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}\right)\right] P\left(B_{1} \cdots B_{d}\right) \\
& +K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right) \\
& \leq P\left(\frac{\boldsymbol{v}_{2}^{\top} \mathbf{R}_{22} \boldsymbol{v}_{2}-\operatorname{tr}(\mathbf{R})+\Theta_{n}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x+2 \epsilon\right) P\left(B_{1} \cdots B_{d}\right)+2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right) \\
& =P\left(A_{p}(x+2 \epsilon)\right) P\left(B_{1} \cdots B_{d}\right)+2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right)
\end{aligned}
$$

Similarly, we can prove that

$$
P\left(A_{N}(x) B_{1} \cdots B_{d}\right) \geq P\left(A_{N}(x-2 \epsilon)\right) P\left(B_{1} \cdots B_{d}\right)-2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right)
$$

So, we have

$$
\left|P\left(A_{N}(x) B_{1} \cdots B_{d}\right)-P\left(A_{p}(x)\right) \cdot P\left(B_{1} \cdots B_{d}\right)\right| \leq \Delta_{N, \epsilon} \cdot P\left(B_{1} \cdots B_{d}\right)+2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right)
$$

where

$$
\begin{aligned}
\Delta_{p, \epsilon} & =\left|P\left(A_{N}(x)\right)-P\left(A_{N}(x+2 \epsilon)\right)\right|+\left|P\left(A_{N}(x)\right)-P\left(A_{N}(x-2 \epsilon)\right)\right| \\
& =P\left(A_{N}(x+2 \epsilon)\right)-P\left(A_{N}(x-2 \epsilon)\right)
\end{aligned}
$$

Obviously, the inequality (22) holds for all $i_{1}, \cdots, i_{d}$. Thus,

$$
\begin{aligned}
& \sum_{1 \leq i_{1}<\cdots<i_{d} \leq p}\left|P\left(A_{N}(x) B_{i_{1}} \cdots B_{i_{d}}\right)-P\left(A_{N}(x)\right) \cdot P\left(B_{i_{1}} \cdots B_{i_{d}}\right)\right| \\
& \leq \sum_{1 \leq i_{1}<\cdots<i_{d} \leq p}\left[\Delta_{N, \epsilon} \cdot P\left(B_{i_{1}} \cdots B_{i_{d}}\right)+2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right)\right] \\
& \leq \Delta_{N, \epsilon} \cdot H(d, N)+\left(\begin{array}{c}
N \\
d
\end{array}\right) \cdot 2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right)
\end{aligned}
$$

By Theorem 3 in Pesaran and Yamagata (2021), we have $P\left(A_{N}(x)\right) \rightarrow \Phi(x)$ as $p \rightarrow \infty$. So $\Delta_{N, \epsilon} \rightarrow P(x+2 \epsilon)-P(x-2 \epsilon)$. By letting $\epsilon \rightarrow 0$, we have $\Delta_{p, \epsilon} \rightarrow 0$. By (16), we have $\lim _{p \rightarrow \infty} H(d, p)<\infty$. Additionally, $\left(\begin{array}{l}N \\ d\end{array}\right) \cdot 2 K^{d} \exp \left(-c_{\epsilon} N^{1 / 2}\right) \rightarrow 0$ as $N \rightarrow \infty$. So we can obtain (17).

### 5.4 Proof of Theorem 3

Proof of Theorem 3 According to the proof of Theorem 1, we have

$$
\max _{1 \leq i \leq N} \nu_{i}^{2}-\max _{1 \leq i \leq N} v_{i}^{2}=o_{p}(1)
$$

where

$$
v_{i}=\sum_{t=1}^{T} \xi_{i t} h_{t}
$$

And we have $\sum_{i=1}^{N} z_{i}^{2}=\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}$ where $\boldsymbol{v}=\left(v_{1}, \cdots, v_{N}\right)$. Thus, according to Lemma 1, we only need to show that

$$
P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}<x, \max _{1 \leq i \leq N} v_{i}^{2}-2 \log N+\log \log N<y\right) \rightarrow \Phi(x) F(y)
$$

Additionally, by Theorem 3 in Pesaran and Yamagata (2021) we know that

$$
P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x\right) \rightarrow \Phi(x)
$$

To show (9), we only need to show that

$$
P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x, \max _{1 \leq i \leq N} v_{i}^{2}>l_{N}(y)\right) \rightarrow \Phi(x)(1-F(y))
$$

Recall the notations in Lemma 2, we have

$$
P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x, \max _{1 \leq i \leq N} v_{i}^{2}>l_{N}\right)=P\left(\bigcup_{i=1}^{N} A_{N} B_{i}\right)
$$

Here the notation $A_{N} B_{i}$ stands for $A_{N} \cap B_{i}$ and we brief $A_{N}(x)$ as $A_{p}$. From the inclusionexclusion principle,

$$
P\left(\bigcup_{i=1}^{N} A_{N} B_{i}\right) \leq \sum_{1 \leq i_{1} \leq N} P\left(A_{N} B_{i_{1}}\right)-\sum_{1 \leq i_{1}<i_{2} \leq N} P\left(A_{N} B_{i_{1}} B_{i_{2}}\right)+\cdots+
$$

$$
\sum_{1 \leq i_{1}<\cdots<i_{2 k+1} \leq N} P\left(A_{N} B_{i_{1}} \cdots B_{i_{2 k+1}}\right)
$$

and

$$
P\left(\bigcup_{i=1}^{N} A_{N} B_{i}\right) \geq \sum_{1 \leq i_{1} \leq N} P\left(A_{N} B_{i_{1}}\right)-\sum_{1 \leq i_{1}<i_{2} \leq N} P\left(A_{N} B_{i_{1}} B_{i_{2}}\right)+\cdots-
$$

for any integer $k \geq 1$. Define

$$
H(N, d)=\sum_{1 \leq i_{1}<\cdots<i_{d} \leq p} P\left(B_{i_{1}} \cdots B_{i_{d}}\right)
$$

for $d \geq 1$. From (16) we know

$$
\lim _{d \rightarrow \infty} \limsup _{N \rightarrow \infty} H(p, d)=0
$$

Set

$$
\zeta(N, d)=\sum_{1 \leq i_{1}<\cdots<i_{d} \leq N}\left[P\left(A_{N} B_{i_{1}} \cdots B_{i_{d}}\right)-P\left(A_{N}\right) \cdot P\left(B_{i_{1}} \cdots B_{i_{d}}\right)\right]
$$

for $d \geq 1$. By Lemma 2 ,

$$
\lim _{N \rightarrow \infty} \zeta(N, d)=0
$$

for each $d \geq 1$. The assertion (28) implies that

$$
\begin{aligned}
P\left(\bigcup_{i=1}^{N} A_{N} B_{i}\right) \leq & P\left(A_{N}\right)\left[\sum_{1 \leq i_{1} \leq N} P\left(B_{i_{1}}\right)-\sum_{1 \leq i_{1}<i_{2} \leq N} P\left(B_{i_{1}} B_{i_{2}}\right)+\cdots-\right. \\
& \left.\sum_{1 \leq i_{1}<\cdots<i_{2 k} \leq N} P\left(B_{i_{1}} \cdots B_{i_{2 k}}\right)\right]+\left[\sum_{d=1}^{2 k} \zeta(N, d)\right]+H(N, 2 k+1) \\
\leq & P\left(A_{N}\right) \cdot P\left(\bigcup_{i=1}^{N} B_{i}\right)+\left[\sum_{d=1}^{2 k} \zeta(N, d)\right]+H(N, 2 k+1)
\end{aligned}
$$

where the inclusion-exclusion formula is used again in the last inequality, that is,

$$
P\left(\bigcup_{i=1}^{N} B_{i}\right) \geq \sum_{1 \leq i_{1} \leq N} P\left(B_{i_{1}}\right)-\sum_{1 \leq i_{1}<i_{2} \leq N} P\left(B_{i_{1}} B_{i_{2}}\right)+\cdots-
$$

$$
\sum_{1 \leq i_{1}<\cdots<i_{2 k} \leq N} P\left(B_{i_{1}} \cdots B_{i_{2 k}}\right)
$$

for all $k \geq 1$. By the definition of $l_{N}$ and Theorem 1 ,

$$
P\left(\bigcup_{i=1}^{N} B_{i}\right) \rightarrow 1-F(y)
$$

as $N \rightarrow \infty$. By (25), $P\left(A_{N}\right) \rightarrow \Phi(x)$ as $N \rightarrow \infty$. From (27), (31) and (32), by fixing $k$ first and sending $N \rightarrow \infty$ we obtain that

$\limsup _{N \rightarrow \infty} P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x, \max _{1 \leq i \leq N} v_{i}^{2}>l_{N}\right) \leq \Phi(x) \cdot[1-F(y)]+\lim _{N \rightarrow \infty} H(N, 2 k+1)$.

Now, by letting $k \rightarrow \infty$ and using (30) we have

$$
\limsup _{N \rightarrow \infty} P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x, \max _{1 \leq i \leq N} v_{i}^{2}>l_{N}\right) \leq \Phi(x) \cdot[1-F(y)]
$$

By applying the same argument to (29), we see that the counterpart of (32) becomes

$$
\begin{aligned}
P\left(\bigcup_{i=1}^{N} A_{N} B_{i}\right) \geq & P\left(A_{N}\right)\left[\sum_{1 \leq i_{1} \leq N} P\left(B_{i_{1}}\right)-\sum_{1 \leq i_{1}<i_{2} \leq N} P\left(B_{i_{1}} B_{i_{2}}\right)+\cdots+\right. \\
& \left.\sum_{1 \leq i_{1}<\cdots<i_{2 k-1} \leq N} P\left(B_{i_{1}} \cdots B_{i_{2 k-1}}\right)\right]+\left[\sum_{d=1}^{2 k-1} \zeta(N, d)\right]-H(N, 2 k) \\
\geq & P\left(A_{N}\right) \cdot P\left(\bigcup_{i=1}^{N} B_{i}\right)+\left[\sum_{d=1}^{2 k-1} \zeta(N, d)\right]-H(N, 2 k)
\end{aligned}
$$

where in the last step we use the inclusion-exclusion principle such that

$$
\begin{aligned}
& P\left(\bigcup_{i=1}^{N} B_{i}\right) \leq \sum_{1 \leq i_{1} \leq N} P\left(B_{i_{1}}\right)-\sum_{1 \leq i_{1}<i_{2} \leq N} P\left(B_{i_{1}} B_{i_{2}}\right)+\cdots+ \\
& \sum_{1 \leq i_{1}<\cdots<i_{2 k-1} \leq N} P\left(B_{i_{1}} \cdots B_{i_{2 k-1}}\right)
\end{aligned}
$$

for all $k \geq 1$. Review (27) and repeat the earlier procedure to see

$$
\liminf _{N \rightarrow \infty} P\left(\frac{\boldsymbol{v}^{\top} \mathbf{R} \boldsymbol{v}-\operatorname{tr}(\mathbf{R})}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \leq x, \max _{1 \leq i \leq N} v_{i}^{2}>l_{N}\right) \geq \Phi(x) \cdot[1-F(y)]
$$

by sending $N \rightarrow \infty$ and then sending $k \rightarrow \infty$. This and (33) yield (26). The proof is completed.

### 5.5 Proof of Theorem 4

According to the proof of Theorem 3, we only need to show that

$$
\begin{aligned}
& P\left(\frac{\tilde{\boldsymbol{v}}^{\top} \mathbf{R} \tilde{\boldsymbol{v}}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}<x, \max _{1 \leq i \leq N} \tilde{v}_{i}^{2}-2 \log N+\log \log N<y\right) \\
& \rightarrow P\left(\frac{\tilde{\boldsymbol{v}}^{\top} \mathbf{R} \tilde{\boldsymbol{v}}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}<x\right) P\left(\max _{1 \leq i \leq N} \tilde{v}_{i}^{2}-2 \log N+\log \log N<y\right)
\end{aligned}
$$

where $\tilde{v}_{i}=v_{i}+\tilde{\alpha}_{i} \sum_{t=1}^{T} h_{t}$. Define $\boldsymbol{\omega}=\left(\omega_{1}, \cdots, \omega_{N}\right)^{\top}$ and $\omega_{i}=\tilde{\alpha}_{i} \sum_{t=1}^{T} h_{t}=O\left(T^{1 / 2} \alpha_{i}\right)$. We have

$$
\max _{1 \leq i \leq N} \tilde{v}_{i}^{2}=\max \left\{\max _{i \in \mathcal{M}} \tilde{v}_{i}^{2}, \max _{i \in \mathcal{M}^{c}} \tilde{v}_{i}^{2}\right\} \doteq \max \left\{M_{1}, M_{2}\right\}
$$

and

$$
\begin{aligned}
& \frac{\tilde{\boldsymbol{v}}^{\top} \mathbf{R} \tilde{\boldsymbol{v}}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}=\frac{\boldsymbol{v}_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}^{c}} \boldsymbol{v}_{\mathcal{M}^{c}}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}+\frac{2 \boldsymbol{v}_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}^{c} \mathcal{M}} \tilde{\boldsymbol{v}}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}+\frac{\tilde{\boldsymbol{v}}_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}} \tilde{\boldsymbol{v}}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \\
& =\frac{\boldsymbol{v}_{\mathcal{M}^{c}}^{\top} \mathbf{R}_{\mathcal{M}^{c}} \boldsymbol{v}_{\mathcal{M}^{c}}-N}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}+\frac{2 \boldsymbol{v}_{\mathcal{M}^{c}}^{\top} \mathbf{R}_{\mathcal{M}^{c} \mathcal{M}} \boldsymbol{v}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}+\frac{2 \boldsymbol{v}_{\mathcal{M}^{c}}^{\top} \mathbf{R}_{\mathcal{M}^{c} \mathcal{M}} \boldsymbol{\omega}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \\
& +\frac{\boldsymbol{v}_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}} \boldsymbol{v}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}+\frac{2 \boldsymbol{v}_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}} \boldsymbol{\omega}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}}+\frac{\boldsymbol{\omega}_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}} \boldsymbol{\omega}_{\mathcal{M}}}{\sqrt{2 \operatorname{tr}\left(\mathbf{R}^{2}\right)}} \\
& \doteq T_{1}+T_{2}+T_{3}+T_{4}+T_{5}+T_{6}
\end{aligned}
$$

By the condition (A1), we have $\boldsymbol{v}_{\mathcal{M}}$ is independent of $\boldsymbol{v}_{\mathcal{M}^{c}}$. So $M_{1}$ is independent of $T_{1}$. By the results of Theorem 3, we have $M_{2}$ is asymptotically independent of $T_{1}$. So we only need to show that $T_{i}=o_{p}(1)$ for $i=2, \cdots, 5$. By the proof of Lemma 2, we have $T_{2}=o_{p}(1)$ and $T_{4}=o_{p}(1)$ if $m=o\left(N^{1 / 2}\right)$. And

$$
\begin{aligned}
& E\left(T_{3}^{2}\right)=O\left(\frac{\omega_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M} \mathcal{M}^{c}} \mathbf{R}_{\mathcal{M}^{c} \mathcal{M}} \omega_{\mathcal{M}}}{\operatorname{tr}\left(\mathbf{R}^{2}\right)}\right)=O\left(N^{-1} T \tilde{\boldsymbol{\alpha}}^{\top} \tilde{\boldsymbol{\alpha}}\right)=o(1) \\
& E\left(T_{5}^{2}\right)=O\left(\frac{\omega_{\mathcal{M}}^{\top} \mathbf{R}_{\mathcal{M}}^{2} \omega_{\mathcal{M}}}{\operatorname{tr}\left(\mathbf{R}^{2}\right)}\right)=O\left(N^{-1} T \tilde{\boldsymbol{\alpha}}^{\top} \tilde{\boldsymbol{\alpha}}\right)=o(1)
\end{aligned}
$$

by the alternative hypothesis 10) So $T_{3}=o_{p}(1)$ and $T_{5}=o_{p}(1)$. Thus, by the Lemma 1 . we complete the proof.

## References

Bailey, N., Pesaran, M., and Smith, L. (2019). A multiple testing approach to the regularisation of large sample correlation matrices. Journal of Econometrics, 208(2):507-534.

Beaulieu, M., Dufour, J., and Khalaf, L. (2007). Multivariate tests of mean-variance efficiency with possibly non-gaussian errors. Journal of Business $\mathcal{E}$ Economic Statistics, 25(4):398410 .

Bickel, P. and Levina, E. (2008). Covariance regularization by thresholding. Annals of Statistics, 36(6):2577-2604.

Cai, T., Liu, W., and Luo, X. (2011). A constrained 11 minimization approach to sparse precision matrix estimation. Journal of the American Statistical Association, 106(494):594-607.

Cai, T. T., Liu, W., and Xia, Y. (2014). Two-sample test of high dimensional means under dependence. Journal of the Royal Statistical Society. Series B (Statistical Methodology), 76(2):349-372.

Chen, D., Decai, L., and Feng, L. (2022). Asymptotic independence of the quadratic form and maximum of independent random variables with applications to high-dimensional tests. arXiv preprint arXiv:2204.08628.

Fama, E. and French, K. (1993). Common risk factors in the returns on stocks and bonds. Journal of Financial Economics, 33(1):3-56.

Fama, E. and French, K. (2015). A five-factor asset pricing model. Journal of Financial Economics, 116(1):1-22.

Fan, J., Liao, Y., and Yao, J. (2015). Power enhancement in high dimensional cross-sectional tests. Econometrica, 83(4):1497.

Feng, L., Jiang, T., Li, X., and Liu, B. (2022a). Asymptotic independence of the sum and maximum of dependent random variables with applications to high-dimensional tests. arXiv 2205.01638.

Feng, L., Lan, W., Liu, B., and Ma, Y. (2022b). High-dimensional test for alpha in linear factor pricing models with sparse alternatives. Journal of Econometrics, 229(1):152-175.

Gagliardini, P., Ossola, E., and Scaillet, O. (2016). Time-varying risk premium in large cross-sectional equity data sets. Econometrica, 84(3):985-1046.

Gibbons, M., Ross, S., and Shanken, J. (1989). A test of the efficiency of a given portfolio. Econometrica, 57(5):1121-1152.

Giglio, S., Liao, Y., and Xiu, D. (2021). Thousands of alpha tests. The Review of Financial Studies, 34(7):3456-3496.

Li, Z., Lam, C., Yao, J., and Yao, Q. (2019). On testing for high-dimensional white noise. The Annals of Statistics, 47(6):3382-3412.

Lintner, J. (1965). The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets. Review of Economics and Statistics, 47:13-37.

Liu, B., Feng, L., and Ma, Y. (2023). High-dimensional alpha test of linear factor pricing models with heavy-tailed distributions. Statistica Sinica, 33:1389-1410.

Ma, H., Feng, L., Wang, Z., and Bao, J. (2024a). Adaptive testing for alphas in conditional factor models with high dimensional assets. Journal of Business 83 Economic Statistics, (just-accepted):1-18.

Ma, H., Feng, L., Wang, Z., and Bao, J. (2024b). Testing alpha in high dimensional linear factor pricing models with dependent observations. arXiv preprint arXiv:2401.14052.

Ma, S., Lan, W., Su, L., and Tsai, C.-L. (2020). Testing alphas in conditional time-varying factor models with high-dimensional assets. Journal of Business 83 Economic Statistics, 38(1):214-227.

Mackinlay, A. and Richardson, M. (1991). Using generalized method of moments to test mean-variance efficiency. Journal of Finance, 46(2):511-527.

Pesaran, M. and Yamagata, T. (2017). Testing for apha in linear factor pricing models with a large number of securities. Social Science Electronic Publishing.

Sharpe, W. (1964). Capital asset prices: a theory of market equilibrium under conditions of risk. Journal of Finance, 19:425-442.

Wang, G. and Feng, L. (2023). Computationally efficient and data-adaptive changepoint inference in high dimension. Journal of the Royal Statistical Society Series B: Statistical Methodology, 85(3):936-958.

Yu, X., Yao, J., and Xue, L. (2023). Power enhancement for testing multi-factor asset pricing models via fisher's method. Journal of Econometrics, In press.

Zhao, P., Chen, D., and Zi, X. (2022). High-dimensional non-parametric tests for linear asset pricing models. Stat, 11(1):e490.

Zhou, G. (1993). Asset-pricing tests under alternative distributions. Journal of Finance, 48(5):1927-1942.

