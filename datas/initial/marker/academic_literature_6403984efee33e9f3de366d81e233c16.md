# Adaptive Strategy Of Testing Alphas In High Dimensional Linear Factor Pricing Models

Chenxi Zhao, Ping Zhao, Long Feng and Zhaojun Wang School of Statistics and Data Science, KLMDASR, LEBPS, and LPMC,
Nankai University April 11, 2024

## Abstract

In recent years, there has been considerable research on testing alphas in highdimensional linear factor pricing models. In our study, we introduce a novel maxtype test procedure that performs well under sparse alternatives. Furthermore, we demonstrate that this new max-type test procedure is asymptotically independent from the sum-type test procedure proposed by Pesaran and Yamagata (2017). Building on this, we propose a Fisher combination test procedure that exhibits good performance for both dense and sparse alternatives.

## 1 Introduction

Linear Factor Pricing Model (LFPM) plays a central role in modern theories of security pricing (Zhou, 1993). Let N be the number of securities, and T be the time dimension of the return series of each security. Let the tth return of the ith security be Yit. LFPM has the form

$$Y_{i t}=\alpha_{i}+\beta_{i}^{\top}\mathbf{f}_{t}+\varepsilon_{i t},$$
ft + εit, (1)
1
for i = 1*, . . . , N*, t = 1*, . . . , T*, where ft ≡ (ft1, · · · , ftp)
⊤ ∈ Rpcontains p economic factors at time t, αiis a scalar representing the security specific intercept, βi ≡ (βi1, · · · , βip)
⊤ ∈ Rpis a vector of multiple regression betas with respect to the p factors and εit is the corresponding idiosyncratic error term with Cov(εt) ≡ Σ = (σij )N×N , where εt ≡ (ε1t, · · · , εN t)
⊤ ∈ R
N
for each t ∈ {1, · · · , T}. Many well known factor models belong to LPFM, such as the Sharpe-Lintner Capital Asset Pricing Model (CAPM) (Sharpe, 1964; Lintner, 1965), the Fama–French three-factor model (Fama and French, 1993), and the Fama–French five-factor model (Fama and French, 2015). The LFPM aims to clarify the variations in anticipated security returns by considering the interaction between security betas and systematic economic factors. It specifically predicts a linear relationship between the expected security return and the economic factors that are unique to each security. This linear framework is highly intuitive and offers the practical advantage of simplifying the modeling of security returns.

The intercept term αiin (1) captures the excessive return of the ith security. That is, other than the return associated with the overall market factors, some securities may have systematic positive or negative returns due to characteristics of the individual securities, termed excess returns. Thus, the following pair of hypotheses

$$H_{0}:\alpha=0\;\;\mathrm{versus}\;\;H_{1}:\alpha\neq0$$
$$H_{1}:\mathbf{\alpha}\neq\mathbf{0}$$
H0 : α = 0 versus H1 : α ̸= 0 (2)
with α ≡ (α1, · · · , αN )
⊤ = 0 allows to assess whether the excess return of the market portfolio presents. When the number of securities N is fixed, many test procedures are devised under the normal or non-normal distribution assumptions, such as Gibbons et al.

(1989), Mackinlay and Richardson (1991), Zhou (1993) and Beaulieu et al. (2007), etc.

Nowadays, thousands of securities are traded in modern financial markets. So the assumption of fixed N is not appropriate.

Many efforts have been devoted for testing alphas in high dimensional linear factor pricing model. Generally speaking, there are three-types test procedures in literature. The first type is the sum-type test procedure, which are constructed by summing the square of the classic t-test statistic of each security, such as Pesaran and Yamagata (2017), Gagliardini et al. (2016),Ma et al. (2020) and Giglio et al. (2021), etc. These sum-type tests have good performance against dense alternatives, i.e. the alphas of over a large number of securities are not zero. The second type is the max-type test procedure, which are constructed by taking the maximum of the squared standard t-ratio of each securities, such as Feng et al.

(2022b). The max-type test procedure is powerful under the sparse alternative, i.e. only a few alphas of securities are not zero. However, we can not know whether the alternative is dense or sparse in real applications. So the third type of test procedure are constructed by combining the above sum-type and max-type test procedures together. Fan et al. (2015) proposed a power enhancement procedure by adding sum-type test statistics and max-type test statistics. Feng et al. (2022b), Yu et al. (2023) proposed a Fisher combination test based on the asymptotically independence between the sum-type test statistic and the max-type test statistic. In this paper, we will propose a novel adaptive strategy test procedure, which belongs to the third type test procedure.

Yu et al. (2023) employed the thresholding covariance matrix estimator of Fan et al.

(2015) and proposed a novel sum-type test statistic in their Fisher combination test procedure. However, there would be a non-negligible bias term in their sum-type test statistic if the covariance matrix estimator is not very accurate. In addition, the max-type test statistic in Feng et al. (2022b) and Yu et al. (2023) do not consider the information of the correlation of each security, which may perform not very well under some special sparse alternatives. To overcome this issue, we first proposed a novel max-type test statistic by standardizing the vector of t-test statistics of each security. Then, we prove that the new max-type test statistic is asymptotically independent with the sum-type test statistic of Pesaran and Yamagata
(2017). Finnally, we propose a new Fisher combination test by the above two asymptotically independent test statistics. Simulation studies show the superior of our proposed procedure.

The rest of paper is organized as follows. In Section 2, we introduce the new max-type test statistic and establish the theoretical results. And we also propose an adaptive strategy testing procedure. Simulation studies are presented in Section 3. All the technical proofs are given in the Appendix.

## 2 Our Test Procedure 2.1 Max-Type Test

To test the hypothesis (2), Feng et al. (2022b) propose a max-of-squares type test, named the MAX test, with the test statistic constructed as

$$M_{\mathbf{I}}=\operatorname*{max}_{1\leq i\leq N}t_{i}^{2},$$
$$\left({\boldsymbol{3}}\right)$$
, (3)
where

$$t_{i}={\frac{{\hat{\alpha}}_{i}{\sqrt{\left(\mathbf{1}_{T}^{\top}\mathbf{M_{F}1_{T}}\right)}}}{\sqrt{v^{-1}{\hat{\epsilon}}_{i}^{\top}{\hat{\epsilon}}_{i}.}}}$$

is the squared standard t-ratio of αiin the OLS regression of yit on an intercept and ft, and v = T − p − 1. Here, 1T = (1, *· · ·* , 1)⊤, IT is the T × T identity matrix, F = (f1, *· · ·* ,fT )
⊤ ∈
R

T ×p and MF = IT − F(F
⊤F)
−1F
⊤; αˆ = (ˆα1, *· · ·* , αˆN )
⊤ is the OLS estimator of α, where αˆi = Y⊤
i· MF1T /(1
⊤
T MF1T ) and Yi· = (Yi1, · · · , YiT )
⊤ ∈ R
T; εˆit is the OLS residual from the regression of yit on an intercept and ft, εi· ≡ (εi1, · · · , εiT )
⊤ ∈ R
T and εˆi· ≡ (ˆεi1, *· · ·* , εˆiT )
⊤ =
MF(Yi − αˆi).

However, the test statistic (3) do not consider the correlation between those securities.

Under the null hypothesis, α = 0 is equivalent to Bα = 0 for any positive definite matrix B. Under the null hypothesis, we have t = (t1, · · · , tN )
d→N(0, R) if εt ∼ *N(0,* Σ) where Σ
is the covariance matrix and R is the corresponding correlation matrix. So a nature choice of B is R−1/2 which standardized the t-test statistics t. So, if we have a good consistent estimator of Ω1/2.= R−1/2, Ωˆ 1/2, we could propose a new max-type test

$$M_{\hat{\mathbf{\Omega}}^{1/2}}=\operatorname*{max}_{1\leq i\leq N}\nu_{i}^{2},$$
$$\left({4}\right)$$
$\mathbf{\omega})^\top=\hat{\mathbf{Q}}^{1/2}\pmb{t}$. 
, (4)
where ν = (ν1, · · · , νN )
⊤ = Ωˆ 1/2t.

Next, we consider the theoretical properties of MΩˆ 1/2 based on the following assumptions.

(A1) ε1*, . . . ,* εT are independently and identically distributed with εt = Σ
1/2ξt
. And we assume ξt = (ξ1t, · · · , ξN t) contains independent components ξit's with E(ξit) = 0 and var(ξit) = 1, E(ξ 4 it) < c for some positive constant c. Define R = D−1/2ΣD−1/2 =
(rij )1≤i,j≤N where D is the diagonal matrix of Σ. (i) There exists c3 > 0, such that c
−1 3 ≤ λmin(R) ≤ λmax(R) ≤ c3. (ii) There exists r1 > 0, such that max1≤i<j≤N |rij | ≤
r1 < 1.

(A2) ξit's have one of the following three types of tails: (i) sub-Gaussian-type tails, i.e.

there exist η > 0 and K > 0 such that E{exp(ηξ2 it/σii)} ≤ K for 1 ≤ i ≤ N, where N satisfies log(N) = o(T
1/4); (ii) sub-exponential-type tails, i.e. there exist η > 0 and K > 0 such that E{exp(η|ξit|/σ1/2 ii )} ≤ K for 1 ≤ i ≤ N, where N satisfies log(N) = o(T
1/4); (iii) sub-polynomial-type tails, i.e. for some constants γ0, ϵ > 0 and K > 0, E|ξit/σ1/2 ii | 2γ0+2+ϵ ≤ K for 1 ≤ i ≤ N, where N satisfies N ≤ c1T
γ0for some constants c1 > 0.

(A3) (i) {f1*, . . . ,*fT } is strictly stationary and independent of {ε1*, . . . ,* εT }. (ii) f
′
t ft ≤ K <
∞, for all t. The (m + 1) × (m + 1) matrix T
−1G′G, with G = (1T , F), is a positive definite matrix for all T, and as T → ∞, and 1
′
TMF 1T > 0 where MF = IT −
F (F
′F)
−1 F
′. (iii) cov (ft) is strictly positive definite.

(A4) We assume that the estimator Ωˆ 1/2 = (ˆωij ) has at least a logarithmic rate of convergence

$$\|\hat{\Omega}^{1/2}-\Omega^{1/2}\|_{L_{1}}=o_{p}\left\{\frac{1}{\log(N)}\right\},\operatorname*{max}_{1\leqslant i\leqslant p}|\hat{\omega}_{i,i}-\omega_{i,i}|=o_{p}\left\{\frac{1}{\log(N)}\right\}.$$

Assumption (A1) assume that the error term follows the independent component model, which is widely used in high dimensional data analysis, such as Li et al. (2019); Chen et al.

(2022). The assumption of the correlation matrix is the same as condition 1 and 2 in Cai et al.

(2014). Assumption (A2) consider three types of tails of ξit, which allows the dimension N
smaller as the tails gets heavier. Assumption (A3) is also widely assumed in high dimensional linear factor pricing model, such as Fan et al. (2015); Feng et al. (2022b). Assumption (A4)
is the same as condition (8) in Cai et al. (2014), which is a rather weak requirement on Ωˆ
and can be easily satisfied by many high dimensional precision matrix estimators, such as Bickel and Levina (2008); Cai et al. (2011).

Theorem 1 *Under the condition (A1)-(A4), we have*

$$P_{H_{0}}\left(M_{\Omega^{1/2}}-2\log(N)+\log\log(N)\leq x\right)\to F(x)\doteq\exp\{-(1/\sqrt{\pi})\exp(-x/2)\}\tag{5}$$

for any x ∈ R.

Based on Theorem 1, a level γ test will then be performed through rejecting H0 when MΩˆ 1/2 −2 log(N)+log{log(N)} is larger than the 1−γ quantile, qγ = − log(π)−2 log{log(1−
γ)
−1}, of the type I extreme value distribution.

Next, we will show the consistency of the new proposed max-type test procedure. Define

$${\mathcal{S}}(k_{N})\equiv\{\mathbf{\alpha}\in{\mathcal{R}}^{N}:\sum_{I=1}^{N}I(\alpha_{i}\neq0)=k_{N}\}$$

Here, S(kN ) denote the set of kN -sparse vectors with kN = O(Nr) and r < 14
.

Theorem 2 Under the condition (A1)-(A4), as min(T, N) → ∞

$$({\hat{0}})$$
$$\operatorname*{inf}_{\alpha\in{\mathcal{A}}(\beta)\cap{\mathcal{S}}(k_{N})}P(\phi_{\gamma}=1)\to1$$
$1\quad\rho\,>\,1\,/\,\rho$
where ϕγ ≡ I[MΩˆ 1/2 − 2 log(N) + log log(N) ≥ qγ], β ≥ 1/ mini{ω 2 i,i} + ϵ *for some constant* ϵ > 0*, and*

$${\mathcal{A}}(\beta)\equiv\{\alpha\equiv(\alpha_{1},\ldots,\alpha_{N})\in{\mathcal{R}}^{N}:\operatorname*{max}_{1\leq i<j\leq N}|\alpha_{i}/\sigma_{i i}^{1/2}|\geq\sqrt{8\beta\log(N)/T}\}$$

## 2.2 Adaptive Test

As shown in Theorem 2, the max-type test statistic MΩˆ 1/2 has good performance under sparse alternatives. While for the dense alternatives, Pesaran and Yamagata (2017) proposed a sum-type test statistic:

$$T_{\mathrm{PY}}=\frac{N^{-1/2}\sum_{i=1}^{N}\{t_{i}^{2}-v/(v-2)\}}{v/(v-2)\sqrt{2(v-1)/(v-4)\{1+(N-1)\bar{\rho}_{M T}^{2}\}}},$$

where v = T −p−1 and ˜ρMT = 2/{N(N −1)}PN
i=2 Pi−1 j=1 ρ˜
2 ij is the corresponding correlation estimator of ρ 2 = 2/{N(N − 1)}PN
i=2 Pi−1 j=1 ρ 2 ij with ˜ρij denoting the multiple testing estimator of the correlation ρij = σij/(σ 1/2 ii σ 1/2 jj ) (Bailey et al., 2019). Under the null hypothesis, we have TP Yd→*N(0,* 1). Thus, we will reject the null hypothesis when TP Y > zγ where zγ is the upper γ quantile of the standard normal distribution.

In practice, we can not know whether the alternative is dense or sparse. So we proposed the following Fisher combination test statistic

$$T_{F C2}=-2\log p_{s u m}-2\log p_{m a x2}$$
$$\left(7\right)$$
TF C2 = −2 log psum − 2 log pmax2 (7)
where

$$p_{s u m}=1-\Phi(T_{P Y}),\ \ p_{m a x2}=1-F(M_{\dot{\mathbf{Q}}^{1/2}}-2\log N+\log\log(N))$$

To establish the asymptotic distribution of TF C2, we need the following additional conditions:
(A5) supi,t E(|ξit| 8+c) ≤ K < ∞ for some c > 0.

 (A6) Let $||\mathbf{R}^{1/2}||_1<K$ and $||\mathbf{R}^{1/2}||_\infty<K$. 
Assumption (A5) and (A6) are the same as Assumption 3 in Pesaran and Yamagata (2017).

As shown in Remark 3 in Pesaran and Yamagata (2017), the sparse conditions of R is particularly important in finance where security returns could be affected by weak unobserved factors. Based on these assumptions, we can establish the asymptotic independence between the sum-type test statistic TP Y and the max-type test statistic MΩˆ 1/2 .

$$({\boldsymbol{\delta}})$$
  **Theorem 3**: _Under the conditions (A1), (A3)-(A6), we have, if $N/T^{2}\to0$,
$$(9)$$
$$P\left(T_{P Y}<x,M_{\hat{\Omega}^{1/2}}-2\log N+\log\log N<y\right)\to\Phi(x)F(y)$$

Based on Theorem 3, we have the limit distribution of TF C2 as follow.

Corollary 1 Under the same condition as Theorem 3, we have TF C2 d→ χ 2 4 *under the null* hypothesis.

Because the convergence rate of TF C2 is not very fast, we suggest to use the critical value
(1 + log−1(T N1/2))χ 2 4
(γ) in practice, where χ 2 4
(γ) is the upper γ-quantile of χ 2 4 distribution.

We consider the following alternative hypothesis:

$$,i\in{\mathcal{M}},\ \ |{\mathcal{M}}|=m,\ \ m=e$$
$\left(10\right)^3$
H1 : ˜αi ̸= 0, i ∈ M, |M| = m, m = o(N

$$\vartheta(N^{1/2}),\quad N^{-1}T\tilde{\alpha}^{\top}\tilde{\alpha}=o(1)$$

where α˜ = Ω1/2α. Next, we also demonstrate that TP Y is still asymptotically independent with MΩˆ 1/2 under this special alternatives.

Theorem 4 Under the conditions (A1), (A3)-(A6), we have, if N/T2 → 0, P (TP Y *< x, M*Ωˆ 1/2 − 2 log N + log log N < y) → P (TP Y *< x)* P (MΩˆ 1/2 − 2 log N + log log *N < y*)

$$(T_{P Y}<x)\,P\left(M_{\Omega^{1/2}}-2\log N+\log\log N\right)\tag{11}$$

under the alternative hypothesis (10). Similar to the arguments in Wang and Feng (2023), we have βTF C2 ≥ βsum,γ/2 + βmax2,γ/2 − βsum,γ/2βmax2,γ/2 where βsum, βmax2,γ is the power function of the sum-type test TP Y and MΩˆ 1/2 at significant value γ, respectively. For a small γ, the difference between βmax2,γ and βmax2,γ/2 should be small, and the same fact applies to β*sum,γ*. Consequently, the power of the adaptive test TF C2 would be no smaller than or even significantly larger than that of either max-type or sum-type test.

## 3 Simulation

This experiment is designed to mimic the commonly used Fama-French three-factor model, where the factors ft have strong serial correlation and heterogeneous variance. Specifically, we consider a modified version of the example studied in Section 5.1 of Pesaran and Yamagata
(2017). The response Yit are generated according to the LFPM in (1) with p = 3:

$$Y_{i t}=\alpha_{i}+\sum_{k=1}^{p}\beta_{i k}f_{k t}+\varepsilon_{i t},$$
p
where the three factors, ft1, ft2 and ft3, are the Fama-French three factors. We generate each factor from an autoregressive conditional heteroskedasticity process and the GARCH(1,1)
model respectively. Specifically The data generating process is as follows:

$$Y_{i t}=\alpha_{i}+\sum_{k=1}^{p}\beta_{i k}f_{k t}+\varepsilon_{i t},\ i\in\{1,\cdots,N\},\ t\in\{1,\cdots,T\}.$$
7
Let p = 3. The three factors f1t, f2t and f3t are presented as the Fama–French three factors, Market factor, SMB and HML. We generate the factors as follows, where for each factor, the error term follows a GARCH(1, 1) process, and all the coefficients are the same as that in Pesaran and Yamagata (2017). Specifically,

$$\begin{array}{l}{{f_{1t}=\!\!0.53+0.06f_{1,t-1}+h_{1t}^{1/2}\zeta_{1t},\mathrm{~Market~factor},}}\\ {{f_{2t}=\!\!0.19+0.19f_{2,t-1}+h_{2t}^{1/2}\zeta_{2t},\mathrm{~SMB~factor},}}\\ {{f_{3t}=\!\!0.19+0.05f_{3,t-1}+h_{3t}^{1/2}\zeta_{3t},\mathrm{~HML~factor},}}\end{array}$$

where ζkt's are simulated from a standard normal distribution, the variance terms hkt's are generated from

$h_{1t}=0.89+0.85h_{1,t-1}+0.11\zeta_{1,t-1}^{2}$, Market factor, $h_{2t}=0.62+0.74h_{2,t-1}+0.19\zeta_{2,t-1}^{2}$, SMB, $h_{3t}=0.80+0.76h_{3,t-1}+0.15\zeta_{3,t-1}^{2}$, HML.  
Similar to Pesaran and Yamagata (2017), the above process is simulated over the periods t = −49, · · · , 0, 1, · · · , T with the initial values fk,−50 = 0 and hk,−50 = 1 for any k = 1, 2 and 3. We use the simulated data for observations t = 1, · · · , T for our final experiments.

The errors are generated from εt ∼ Σ
1/2zt, where zt = (z1t, · · · , zN t)
⊤. We consider four settings of zit's:
(i) Normal distribution: zit

$$\stackrel{i.i.d}{\sim}N(0,1);$$
$${\mathrm{(ii)}}\;\;t_{3}{\mathrm{~distribution:}}\;z_{i i}\stackrel{i.i.d}{\sim}t(5)/{\sqrt{5/3}}$$

(iii) mixture normal distribution: zit

$$\stackrel{i.i.d}{\sim}\{0.9N(0,1)+0.1N(0,9)\}/\sqrt{1.8}$$

We consider four models for the covariance matrix
(1) Model 1: Σ = (0.7 |i−j|)1≤i,j≤N ;
(2) Model 2: Σ = D1/2RD1/2, D = diag{σ 2 1
, · · · , σ2N } and R = IN + bb⊤ − B˜ , where b = (b1, · · · , bN )
⊤ and B˜ = diag{b 2 1
, · · · , b2N }. We generate σii ∼ *U(1,* 2). We randomly generate [N0.3] elements of b from *U(0.*7, 0.9) and set the remaining elements to be zero.

Here [·] denotes the integer part of a real number.

(3) Model 3: Σ = Ω−1 where Ω = (0.6 |i−j|)1≤i,j≤N ;
(4) Model 4: Σ = γγT+(Ip−ρϵW)
−1(Ip−ρϵWT)
−1, where γ = (γ1, · · · , γ[p δγ ]
, 0, 0, *· · ·* , 0)T.

Here γi with i = 1, *· · ·* , [p δγ] are generated independently from *Uniform(0.7,* 0.9). Let ρϵ = 0.5 and δγ = 0.3. Let W = (wi1i2
)1≤i1,i2≤p have a so-called rook form, i.e., all elements of W are zero except that wi1+1,i1 = wi2−1,i2 = 0.5 for i1 = 1, · · · , p − 2 and i2 = 3, · · · , p, and w1,2 = wp,p−1 = 1.
Here P Y means TP Y , MAX1 means MI, MAX2 means MΩˆ 1/2 , HC1 means TF C1 which is the Fisher combination test based on TP Y and MI, HC2 means TF C2, COM means the combination method proposed by Feng et al. (2022b). PE means the power enhancement

| Model 1               | Model 2                 | Model 3   | Model 4   |               |                    |          |      |                               |           |     |     |     |     |     |     |     |
|-----------------------|-------------------------|-----------|-----------|---------------|--------------------|----------|------|-------------------------------|-----------|-----|-----|-----|-----|-----|-----|-----|
| N                     | N                       | N         | N         |               |                    |          |      |                               |           |     |     |     |     |     |     |     |
| Method                | 50                      | 100       | 200       | 300           | 50                 | 100      | 200  | 300                           | 50        | 100 | 200 | 300 | 50  | 100 | 200 | 300 |
| Normal Errors         |                         |           |           |               |                    |          |      |                               |           |     |     |     |     |     |     |     |
| PY                    | 6.2                     | 6.1       | 7.9       | 7.8           | 5.7                | 6.1      | 7.3  | 5.5                           | 5.8       | 5.8 | 5.4 | 4.4 | 5.3 | 6.4 | 4.9 | 4.5 |
| MAX1                  | 3.1                     | 4.6       | 4.6       | 4.6           | 4.1                | 3.5      | 4.2  | 5                             | 3.2       | 5.3 | 5.5 | 5.2 | 3.6 | 5.3 | 4.5 | 4.9 |
| MAX2                  | 8.2                     | 6.9       | 4.8       | 5.3           | 3.9                | 3.6      | 5    | 7.4                           | 4.1       | 5.2 | 5.4 | 5.2 | 4   | 5.6 | 4.4 | 5   |
| FC1                   | 4.9                     | 5.6       | 6.1       | 6.7           | 5.2                | 5.3      | 5.1  | 4                             | 4.8       | 5.7 | 5   | 4.5 | 4.7 | 6.1 | 4.8 | 4.5 |
| FC2                   | 6.4                     | 6.4       | 6.6       | 6.2           | 5.2                | 5.4      | 5.4  | 5.9                           | 5.4       | 5.6 | 4.9 | 4.5 | 4.9 | 6.4 | 4.9 | 4.5 |
| COM                   | 5.1                     | 4.9       | 5.6       | 6.8           | 5.1                | 5.2      | 6.5  | 5.1                           | 4.9       | 5.7 | 5.3 | 4.2 | 3.9 | 6.1 | 5   | 4.1 |
| PE                    | 22.8 20.1 14.3 12.2 6.5 | 8.4       | 10.4      | 12            | 9.9 11.9 12.1 12.4 | 9        | 12.5 | 11                            | 13.1      |     |     |     |     |     |     |     |
| t(5) Errors           |                         |           |           |               |                    |          |      |                               |           |     |     |     |     |     |     |     |
| PY                    | 7.8                     | 6.9       | 6.8       | 5.7           | 5.2                | 4.1      | 4.6  | 4                             | 5.7       | 4.4 | 6   | 5.7 | 6.2 | 5.3 | 5.5 | 4.5 |
| MAX1                  | 3.9                     | 2.6       | 3.8       | 4.4           | 3                  | 4.7      | 3.8  | 4.1                           | 3.4       | 3.3 | 3.5 | 4.7 | 3.7 | 4.2 | 3.9 | 4.3 |
| MAX2                  | 8.1                     | 5.4       | 5.2       | 4.4           | 2.9                | 4.6      | 4.7  | 6.5                           | 3.5       | 3.3 | 3.6 | 4.9 | 3.7 | 4.3 | 4   | 4.4 |
| FC1                   | 6.8                     | 5.2       | 6.6       | 5.4           | 3.7                | 3.4      | 3.5  | 3.4                           | 4.7       | 3.7 | 4.6 | 5.5 | 5.6 | 4.4 | 3.9 | 3.4 |
| FC2                   | 8.6                     | 5.8       | 6.5       | 4.8           | 3.7                | 3.4      | 3.9  | 4.9                           | 4.9       | 3.5 | 4.6 | 5.5 | 5.3 | 4.2 | 4   | 3.6 |
| COM                   | 5.8                     | 5.8       | 6.2       | 5.5           | 3.7                | 3.5      | 4.3  | 3.6                           | 4.7       | 3.7 | 4.2 | 6.4 | 5.7 | 3.9 | 5.4 | 3.2 |
| PE                    | 23.1 19.3 16.9          | 9.6       | 5.7       | 5.9           | 9.6                | 11.6 9.3 | 9.5  | 11.9 12.2 10.1 10.4 10.9 10.9 |           |     |     |     |     |     |     |     |
| Mixture Normal Errors |                         |           |           |               |                    |          |      |                               |           |     |     |     |     |     |     |     |
| PY                    | 7.1                     | 5.5       | 6.4       | 7.5           | 5.6                | 6.7      | 5.4  | 4.2                           | 5.3       | 7   | 3.8 | 5.9 | 5.4 | 4.8 | 5.3 | 6.1 |
| MAX1                  | 2.7                     | 3.4       | 4.5       | 4.1           | 2.3                | 4.3      | 2.2  | 4.3                           | 3.3       | 4   | 4.7 | 3.3 | 3.6 | 3.8 | 4   | 3.3 |
| MAX2                  | 8.4                     | 5.5       | 3.5       | 4.8           | 2.3                | 4.3      | 2.8  | 6.8                           | 3.2       | 3.5 | 4.9 | 3.6 | 4.2 | 4.1 | 4.1 | 3.6 |
| FC1                   | 5.5                     | 4.4       | 5.3       | 6             | 3.7                | 6.1      | 3.4  | 3.8                           | 4.3       | 5.5 | 5   | 4.4 | 4.3 | 3.7 | 4.7 | 4   |
| FC2                   | 8.1                     | 4.4       | 5.4       | 6.2           | 3.6                | 6.2      | 3.6  | 5.2                           | 4.2       | 5.6 | 5.2 | 4.3 | 4.1 | 4   | 4.5 | 4.3 |
| COM                   | 5.5                     | 4.6       | 5.2       | 6             | 3.7                | 5.8      | 4.3  | 3.7                           | 4         | 5.6 | 4.8 | 5.3 | 4.2 | 3.7 | 4.7 | 4.2 |
| PE                    | 24.2 17.1 12.5 10.2 7.2 | 9.2       | 9.2       | 12.8 9.7 12.6 | 10                 | 13.5     | 9.3  | 9.2                           | 10.4 11.2 |     |     |     |     |     |     |     |

8 method proposed by Fan et al. (2015). We estimate the covariance matrix by the thresholding method proposed by Bickel and Levina (2008). For fair comparison, we use the same covariance estimator in PE. Finally, the three groups of coefficients corresponding to the three factors, βi1, βi2 and βi3, are generated independently from U(0.2, 2), U(−1, 1.5) and U(−1.5, 1.5), respectively. We set α = 0 under the null hypothesis. Table 1 reports the empirical sizes of each test with sample size T = 100. We found that PE can not control the empirical sizes in most cases. However, the other methods can control the empirical sizes very well. So we do not consider the PE method in power comparison.

To compare the power performance of the various tests under different sparsity of α, we present the empirical power of each test under different number of nonzero elements of α.

For illustration, here we only consider T = 100, N = 200. Specifically, given the number of nonzero elements of α, i.e. m ∈ {1, *· · ·* , 20}, we randomly choose a subset S from {1, · · · , N}
with |S| = m and let αi =
q10 log(N)
mT for i ∈ S, such that the signal strength ∥α∥
2is fixed for each m. Figure 1-3 show the power curves of each tests under different error distributions.

In Model 2-4, the newly introduced max-type test, denoted as MΩˆ 1/2 , exhibits a performance that is comparable to MI, as referenced in Feng et al. (2022b). When we consider varying degrees of sparsity, it is observed that the sum-type test TP Y surpasses the max-type tests MΩˆ 1/2 and MI as the value of m increases. However, when m is relatively small, the max-type tests outperform the sum-type test TP Y .

The combination tests demonstrate more consistent results across different levels of sparsity. Notably, when m is neither too large nor too small, these combination tests prove to be more potent than both the max-type and sum-type tests. These observations align with our theoretical findings and corroborate many existing studies, such as Feng et al. (2022a,b);
Chen et al. (2022).

Moreover, in Model 1, MΩˆ 1/2 demonstrates significantly higher power than MI, underscoring the benefits of accounting for error correlation. As a result, the newly proposed adaptive test TF C2 outperforms both TF C1 and COM tests.

## 4 Conclusion

In this study, we initially introduce a novel max-type test statistic that takes into account the correlation among errors and exhibits superior performance under sparse alternatives.

For broader alternatives, we suggest a Fisher combination test, which is predicated on the asymptotic independence between the newly proposed max-type test statistic and the sumtype test statistic from Pesaran and Yamagata (2017). The efficacy of the proposed methods is further demonstrated through simulation studies.

Looking ahead, we propose several directions for future research. Firstly, the assumption of a constant regression coefficient may not hold in real-world scenarios. Therefore, numerous studies, such as Ma et al. (2020) and Ma et al. (2024a), have explored the testing of alpha in the high-dimensional time-varying factor model. It would be intriguing to propose a new max-type test and an adaptive test that standardizes the corresponding t-test statistic in

![9_image_0.png](9_image_0.png)

Figure 1: Power of tests with different numbers of nonzero alpha at T = 100, N = 200 with