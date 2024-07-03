# Filtering And Smoothing Estimation Algorithms From Uncertain Nonlinear

observations with time-correlated additive noise and random deception attacks R. Caballero-Aguila ´ a, J. Huband J. Linares-P´erezc aDepartamento de Estad´ıstica. Universidad de Ja´en. Paraje Las Lagunillas. 23071. Ja´en. Spain; bKey Laboratory of Advanced Manufacturing and Intelligent Technology, Ministry of Education, Harbin University of Science and Technology, Harbin 150080, China; cDepartamento de Estad´ıstica. Universidad de Granada. Avenida Fuentenueva. 18071. Granada. Spain

## Article History

Compiled May 9, 2024

## Abstract

This paper discusses the problem of estimating a stochastic signal from nonlinear uncertain observations with time-correlated additive noise described by a first-order Markov process.

Random deception attacks are assumed to be launched by an adversary, and both this phenomenon and the uncertainty in the observations are modelled by two sets of Bernoulli random variables. Under the assumption that the evolution model generating the signal to be estimated is unknown and only the mean and covariance functions of the processes involved in the observation equation are available, recursive algorithms based on linear approximations of the real observations are proposed for the least-squares filtering and fixed-point smoothing problems. Finally, the feasibility and effectiveness of the developed estimation algorithms are verified by a numerical simulation example, where the impact of uncertain observation and deception attack probabilities on estimation accuracy is evaluated. KEYWORDS
Nonlinear observation models; least-squares estimation; missing measurements; time-correlated noise; random deception attacks

## 1. Introduction

Although state-space models can theoretically be divided into linear and nonlinear models, in practice there are no strictly linear models. So-called linear systems are nothing more than approximations, usually valid over a limited range of values of the variables involved in the model. Even though many systems have a sufficiently high degree of approximation to linearity, we eventually encounter systems that deviate significantly from linear behaviour, even within a limited operating range. In such cases, the accuracy of linear estimation techniques diminishes and it becomes necessary to explore nonlinear estimation approaches (Simon, 2006). Despite these considerations, there has been a huge amount of work on linear estimation for linear systems and the mathematical tools available for this kind of systems are much more accessible and well understood. For this reason, linear approximations are often used to adapt linear estimation techniques to the nonlinear problems that are encountered in This is an original manuscript of an article published by Taylor & Francis in INTERNATIONAL JOURNAL OF SYSTEMS
SCIENCE on March 19 2024, available at: https://doi.org/10.1080/00207721.2024.2328781.

many branches of practical domains, such as computer vision, communications, navigation and tracking systems or econometrics and finance (Hu et al., 2015).

The performance of estimation algorithms is often affected by the occurrence of random uncertainties, a common one being the presence of missing measurements (also called uncertain observations). Indeed, this phenomenon is unavoidable in many real-world scenarios where the information received by the estimator side is usually incomplete, due to several causes (e.g., random failures in the measurement mechanism, accidental loss of some data packets or inaccessibility of data at certain times). In these situations, it is necessary to consider the influence of this incomplete information when designing estimation algorithms. In the context of linear systems, the estimation problem for multisensor stochastic uncertain systems with missing measurements and unknown measurement disturbances is addressed in Pang & Sun (2015). Using a new augmented state approach, three robust Kalman-like filtering algorithms are proposed in Ran & Deng (2020) for a class of multisensor systems with mixed uncertainties including random delays, missing measurements, multiplicative noises and uncertain noise variances. The distributed filtering problem for systems with missing measurements is studied in Wen et al. (2020), under the assumption that the state noises and the measurement noises are correlated. In the context of nonlinear systems, the impact of incomplete information on the estimation problem has also been analyzed, e.g., in Hu et al.

(2023b), where a class of singular systems subject to random delays, packet dropouts and nonlinearities, and in Han et al. (2017), where a distributed H∞-consensus filtering approach is proposed for nonlinear systems with missing measurements. More recently, a particle filter is proposed in Ma & Wang (2022) for nonlinear systems with time-varying delays and unknown noise distribution and, in Hu et al. (2023a), a distributed resilient fusion filtering algorithm is designed for nonlinear systems with dynamic event-triggered mechanism under the missingmeasurement phenomenon. A complete survey on estimation algorithms for nonlinear systems with communication constraints causing random delays, missing/fading measurements or randomly occurring incomplete information can be found in Hu et al. (2020).

Many conventional estimation algorithms are typically based on the assumption that the additive noise in measurements is either white or finite-step correlated. However, in practical engineering applications, infinite-step correlated measurement noises can be prevalent, especially when the sampling frequency is sufficiently high, leading to significant correlation over two or more consecutive sampling periods. Over the past decade, the estimation problem has been widely studied under the assumption that the infinite-step time-correlated noise is a first-order Markov process. The state estimation problem for linear systems with multiplicative noise and time-correlated additive noise in the measurements has been investigated in Liu (2015) and an improved steady-state filter has been designed in Liu & Shi (2019).

Least-squares estimation algorithms are proposed in Garc´ıa-Ligero et al. (2020), considering random delays in the transmission connections that are modelled by Markov chains, and in Caballero-Aguila et al. (2022), considering random parameter matrice ´ s in the measurement model and random packet dropouts for which two different compensation scenarios are compared. Distributed fusion filtering algorithms for uncertain systems with random delays and packet loss prediction compensation are designed in Caballero-Aguila & Linares-P´erez ´
(2023a). Recursive estimation algorithms for linear stochastic uncertain systems with timecorrelated additive noises and packet dropout compensations are proposed in Ma & Sun
(2020) and a similar study for nonlinear systems is carried out in Cheng et al. (2021).

In addressing the estimation problem, security emerges as a crucial consideration that should not be disregarded. The vulnerability to cyber attacks is well-documented in the literature (see, for instance, Mahmoud et al., 2019; Sanchez et al., 2019). Particularly, the estimation problem in networked systems exposed to deception attacks has been the focus of numerous significant research endeavors. In general, deception attackers aim to compromise data integrity by maliciously introducing random falsifications into their information. Several research studies have delved into security-guaranteed filtering problems, such as the investigation of centralized solutions for linear time-invariant stochastic systems with multirate-sensor fusion under deception attacks in Wang et al. (2018). The exploration of the H∞-consensus filtering problem for discrete-time systems with multiplicative noises and deception attacks is documented in Han et al. (2019). Additionally, the study of the chance-constrained H∞
state estimation problem for a class of time-varying neural networks, subject to measurement degradation and randomly occurring deception attacks, is presented in Qu et al. (2022). Also, the distributed estimation problem in sensor networks has been addressed under various security threats. Examples include investigations under false data injection attacks in Yang et al.

(2019) and under deception attacks in Caballero-Aguila & Linares-P´erez (2023b), Xiao et al. ´
(2020), Ma & Sun (2023) and Ma et al. (2021).

Motivated by the preceding discussion, our aim is to address the least-squares (LS) estimation problem of signals using nonlinear uncertain observations (missing measurements)
with time-correlated additive noise modeled by a first-order Markov process, in the presence of random deception attacks. The proposed recursive algorithms, based on linear approximations, offer a novel approach to mitigating the impact of missing measurements and deception attacks in signal estimation. The main contributions of this paper are summarized as follows: (a) A covariance-based estimation approach is used, so the evolution model of the signal to be estimated does not need to be known. (b) The class of stochastic signals investigated in this paper is quite comprehensive, as the assumptions under which our study is valid are verified by a great variety of stationary and non-stationary signals. (c) The direct estimation of the time-correlated additive noise avoids the use of the differencing method or vector augmentation. (d) Despite the fact that the simultaneous consideration of uncertain observations, time-correlated noise and random attacks adds complexity to the model, the proposed filtering and fixed-point smoothing algorithms keep the advantages of recursivity and computational simplicity. (e) The proposed estimators have a satisfactory performance even in the presence of high probability of missing measurements and/or high probability of successful random deception attacks.

The paper is structured as follows. Section 2 details the characteristics of the observation model under consideration. The main results are presented in Section 3, which includes the problem statement (subsection 3.1) and the derivation of the proposed filtering and fixed-point smoothing algorithms (subsections 3.2 and 3.3, respectively). Section 4 conducts a simulation study to showcase the effectiveness of the proposed filtering and fixed-point smoothing estimators, additionally exploring the impact of uncertain observation and random deception attacks probabilities on estimation performance. Finally, Section 5 provides some concluding remarks.

The notations and acronyms that are used throughout the paper are summarized in Table 1.

## 2. Mathematical Model And Preliminaries 2.1. Signal Process

Consider a signal process {xk}k≥1 that must be estimated from a set of noisy measurements.

Assume that the mathematical model describing the evolution of this signal process is not known, but its mean and covariance functions satisfy the following hypothesis:

| Table 1.   | Notations and acronyms used throughout the paper. All vector and matrix dimensions are assumed to be compatible   |
|------------|-------------------------------------------------------------------------------------------------------------------|
| with algebraic operations unless explicitly stated. R n Set of n-dimensional real vectors R n×m Set of n × m real matrices     x=a m × n Jacobian matrix of f : R ∂ f(x) n → R m at a point a ∈ R n ∂x MT and M−1 Transpose and inverse of matrix M δj,i Kronecker delta function E[a] = a Mathematical expectation of a random variable or vector a Σ a k,s Covariance function of a stochastic process {ak}k≥1: Σ a = Cov[ak, as] = E ak − ak as − as T  , Σ a = Cov[ak] k,s k bak/s Optimal linear estimator of the vector ak based on  y1, . . . , ys 	 LS Least-squares OPL Orthogonal projection lemma EKF Extended Kalman filter            |                                                                                                                   |

(H1) The nx-dimensional signal {xk}k≥1 is a second-order zero-mean random process and its covariance function, Σ
x k,s
= Cov[xk, xs], can be factorized as
Σ
x k,s = AkB
T
s
, s ≤ k, where Ak, Bs ∈ R
nx×pare known matrices.

Remark 1. Hypothesis*(H1)* on the signal covariance function is verified by a great variety of stationary and non-stationary signals (Caballero-Aguila et al., 2022). Estimation approaches ´
based on this hypothesis, rather than the state-space model, thus provide a comprehensive framework to obtain general algorithms that cover a wide range of practical situations.

## 2.2. Nonlinear Uncertain Measurements With Time-Correlated Additive Noise

The signal estimation will be performed from nz-dimensional nonlinear outputs that are perturbed by additive noise and subject to random failures, causing that some measured outputs are only noise. This phenomenon is described by a sequence of Bernoulli random variables,
{γk}k≥1. When γk = 1, the actual measurement value is equal to the original measurement value, while γk = 0 means that the actual measurement is only noise. More specifically, the actual measurements are described by the following mathematical model:

$$z_{k}=\gamma_{k}h_{k}(x_{k})+v_{k},\;\;k\geq1,$$
$\eqref{eq:walpha}$. 
zk = γkhk(xk) + vk, k ≥ 1, (1)
with the following hypotheses:

(H2) γk k≥1 is a sequence of independent Bernoulli random variables with known mean function γk = E[γk], k ≥ 1.

(H3) For all k ≥ 1, the function hk : R
nx → R
nzis an analytic function.
Remark 2. Hypothesis *(H3)* guarantees that hk is infinitely differentiable and, for every x0 ∈
R

nx, its Taylor series about x0 converges to the function in some neighborhood of x0. Typical examples of analytic functions are: polynomials, exponential functions, logarithmic functions, trigonometric functions and power functions (Krantz, 2022).

In many engineering applications, the additive noise perturbing the observations has an infinite-step correlation; to better model such situations, the following first-order Markov model is used:

$$\nu_{k}=D_{k-1}\nu_{k-1}+u_{k-1},\;\;k\geq1,$$
vk = Dk−1vk−1 + uk−1, k ≥ 1, (2)
where Dk is non-singular for all k ≥ 0 and the following hypotheses hold:
(H4) v0 is a zero-mean random vector with known covariance Σ
v 0
= Cov[v0].

(H5) The noise process{uk}k≥0 is a zero-mean white sequence with known covariance function Σ
u k
= Cov[uk], k ≥ 0, and it is independent of the initial vector v0.

Remark 3. Hypotheses *(H4)* and *(H5)*, together with the non-singularity of Dk, guarantee that the covariance function of the time-correlated additive noise, Σ
v k,s
= Cov[vk, vs], admits the following factorization:

$$\Sigma_{k,s}^{v}=E_{k}F_{s}^{T},\quad s\leq k,$$
where $E_{k}=D_{k-1}\cdots D_{0}$, $F_{s}=\Sigma_{s}^{v}(E_{s}^{-1})^{T}$ and $\Sigma_{s}^{v}=Cov[v_{s}]$ is recursively obtained as:
$$\Sigma_{s}^{v}=D_{s-1}\Sigma_{s-1}^{v}D_{s-1}^{T}+\Sigma_{s-1}^{u},\ s\geq1.$$

## 2.3. Random Deception Attacks

In many practical situations, a crucial issue that cannot be ignored in the study of the estimation problem is the possible occurrence of cyber-attacks. In particular, deception attacks constitute a significant threat that attempts to compromise data integrity by maliciously and randomly falsifying information. In this type of attacks, the signal injected by the attacker, z˘k, aims to neutralise the actual measurement, zk, and replace it with a deceptive noise, wk.

Specifically, z˘k = −zk + wk, k ≥ 1, where
(H6) The noise process {wk}k≥1 is a zero-mean white sequence with known covariance function Σ
w k
= Cov[wk], k ≥ 1.

To describe the fact that, in practice, cyber-attacks are often unpredictable and random, a sequence of Bernoulli random variables is adopted. More specifically, the following model with stochastic deception attacks is considered to describe the measurements processed for the estimation:

$$y_{k}=z_{k}+\lambda_{k}\breve{z}_{k},\;\;k\geq1,$$

which can be equivalently rewritten as

$$y_{k}=(1-\lambda_{k})z_{k}+\lambda_{k}w_{k},\;\;k\geq1,$$
yk = (1 − λk)zk + λkwk, k ≥ 1, (3)
where

$\eqref{eq:walpha}$. 
(H7) λk k≥1 is a sequence of independent Bernoulli random variables with known mean function λk = E[λk], k ≥ 1.
Remark 4. The binary values of λk indicate if the adversary actually launch the attack (λk =
1) or not (λk = 0). When the actual measurement is attacked, yk = wk and only noise will be processed. Otherwise, if no attack is injected, yk = zk and the actual measurement is processed for the estimation.

Finally, the following independence hypotheses on the processes involved in the considered model is required to address the estimation problem.

(H8) The signal process {xk}k≥1 and the processes {γk}k≥1, {vk}k≥1, {wk}k≥1 and {λk}k≥1 are mutually independent.

## 2.4. Linearized Observations

Under hypotheses *(H1)–(H8)*, our goal is to obtain recursive algorithms for the filtering and fixed-point smoothing problems; that is, to address the estimation problem of the signal xk given the nonlinear observations {y1, . . . , yL}, L ≥ k. To this end, we will use a similar reasoning to that used to derive the extended Kalman filter. The problem is thus reduced to linearizing the observation equation (1) and then inserting such linearized observations into
(3) to calculate the LS linear estimator of the signal from the resulting measurements.

More precisely, from hypothesis *(H3)*, assuming knowledge of a nominal trajectory of the signal, {x 0 k
}k≥1, the function hk can be expanded in Taylor series about x 0 k
:

$$h_{k}(x)=h_{k}(x_{k}^{0})+\frac{\partial h_{k}(x)}{\partial x}\Big|_{x=x_{k}^{0}}(x-x_{k}^{0})+\cdots,\;\;k\geq1,$$

Neglecting the terms of order greater than one in this Taylor expansion, equation (1) can be approximated by the following **linearized observation equation**

$$z_{k}=\gamma_{k}(H_{k}x_{k}+C_{k})+v_{k},\;\;k\geq1,$$
$\eqref{eq:walpha}$. 
zk = γk(Hk xk + Ck) + vk, k ≥ 1, (4)
where

$$H_{k}=\frac{\partial h_{k}(x)}{\partial x}\Big|_{x=x_{k}^{0}},\quad C_{k}=h_{k}(x_{k}^{0})-H_{k}x_{k}^{0}.$$

The above equation is a linear equation affected by the binary multiplicative noise, {γk}k≥1, and the time-correlated additive noise, {vk}k≥1. Our aim is to derive recursive estimation algorithms by using the linear approximation (4) in the equation for the available observations
(3).

## 3. Main Results 3.1. Problem Statement And Innovation Approach

Our goal is to obtain recursive algorithms for the LS linear filter and fixed-point smoother of the signal xk from the available observations (3), based on the linearized measurements
(4). For this purpose, we will use an *innovation approach*. According to this approach, the observation process is transformed into an equivalent innovation process and the LS linear estimator, bζk/L, of a random vector ζk based on a set of observations ny j, 1 ≤ j ≤ L
o, can be expressed as a linear combination of the innovations as follows:

$$\widehat{\zeta_{k/L}}=\sum_{j=1}^{L}S_{k,j}^{\zeta}(\Sigma_{j}^{\eta})^{-1}\eta_{j},\;\;k,L\geq1,$$
$$({\mathfrak{H}})$$
$$(11)$$
$$(12)$$
7
where S
ζ k, j
= E[ζkη T
j
], ηj = y j −by j/ j−1 is the innovation at time j and Σ
η j
= Cov[ηj].

Using (3) and the model hypotheses, the innovation can be written as

$$\eta_{k}=y_{k}-(1-\overline{{{\lambda}}}_{k})\widehat{z}_{k/k-1},\;\;k\geq1,$$
$$(7)$$
ηk = yk − (1 − λk)bzk/k−1, k ≥ 1, (6)
and, from the linear approximation (4), it is clear that the prediction estimator of zk can be approximated by

$$\widehat{\mathcal{Z}}_{k/k-1}=\overline{{{\gamma}}}_{k}(H_{k}\widehat{x}_{k/k-1}+C_{k})+\widehat{v}_{k/k-1}.$$

+bvk/k−1. (7)
Expressions (5)–(7) are the key points for the derivation of the recursive filtering and fixedpoint smoothing algorithms that will be presented in the following subsections.

## 3.2. Recursive Filtering Algorithm

For the sake of convenience, we introduce the following notations:

$$\Gamma_{k}^{a}=\left\{\begin{array}{l l}{{\overline{{{\gamma}}}_{k}H_{k}B_{k},}}&{{a=x,}}\\ {{F_{k},}}&{{a=v,}}\end{array}\right.$$
$$({\mathfrak{s}})$$
Fk, a = v,(8)
$$\Lambda_{k}^{a}=\left\{\begin{array}{ll}\overline{\gamma}_{k}H_{k}A_{k},&a=x,\\ E_{k},&a=v.\end{array}\right.\tag{1}$$
$$(\Phi)$$
$$(10)$$

Theorem 3.1. **Consider the observation model (1)–(3), where the processes involved satisfy**
hypotheses (H1)–(H8). Then, the innovation ηk *is calculated as*

$$\eta_{k}=y_{k}-(1-\overline{{{\lambda}}}_{k})(\Delta_{k}^{x}e_{k-1}^{x}+\Delta_{k}^{y}e_{k-1}^{y}+\overline{{{\gamma}}}_{k}C_{k}),\;\;k\geq1,$$
, k ≥ 1, (10)
and its covariance matrix Σ
η k satisfies

$$\begin{array}{r l}{{\Sigma_{k}^{\eta}=}}&{{\Sigma_{k}^{y}-(1-\overline{{{\lambda}}}_{k})^{2}\big[\left(\Delta_{k}^{x}T_{k-1}^{x x}+\Delta_{k}^{y}T_{k-1}^{y x}\right)(\Delta_{k}^{x})^{T}}}\\ {{}}&{{+\left(\Delta_{k}^{x}T_{k-1}^{x y}+\Delta_{k}^{y}T_{k-1}^{y y}\right)(\Delta_{k}^{y})^{T}+\overline{{{\gamma}}}_{k}^{2}C_{k}C_{k}^{T}\big],\,\,\,k\geq1,}}\end{array}$$

with

$$\begin{array}{l l}{{\Sigma_{k}^{y}=(1-\overline{{{A}}}_{k})\Sigma_{k}^{z}+\overline{{{A}}}_{k}\Sigma_{k}^{w},}}&{{k\geq1,}}\\ {{\Sigma_{k}^{z}=\overline{{{\gamma}}}_{k}\left(H_{k}A_{k}B_{k}^{T}H_{k}^{T}+C_{k}C_{k}^{T}\right)+E_{k}F_{k}^{T},}}&{{k\geq1.}}\end{array}$$

The vectors ea k
(a = x, **v) are recursively obtained by**

$$e_{k}^{a}=e_{k-1}^{a}+\Psi_{k}^{a}(\Sigma_{k}^{\eta})^{-1}\eta_{k},\;\;k\geq1;\;\;e_{0}^{a}=0,$$
$$(13)$$

where

$$\Psi_{k}^{a}=(1-\overline{{{A}}}_{k})(\Gamma_{k}^{a}-\Delta_{k}^{x}T_{k-1}^{x a}-\Delta_{k}^{v}T_{k-1}^{v a})^{T},\;\;k\geq1.$$

The matrices Tab k= E[e a k
(e b k
)
T] (a, b = x, **v) are also recursively calculated by**

$$T_{k}^{a b}=T_{k-1}^{a b}+\Psi_{k}^{a}(\Sigma_{k}^{\eta})^{-1}(\Psi_{k}^{b})^{T},\;\;k\geq1;\;\;T_{0}^{a b}=0.$$

The filtering estimator of the signal, bxk/k**, is then computed by**

$$(14)$$
$$(15)$$
$$(16)$$

bxk/k = Ake x k
, k ≥ 1. (16)
Proof. According to (5), the estimator of the signal xk based on a set of observations
{y1, . . . , yL}, with L ≤ k, is given by

$$\widehat{x}_{k/L}=\sum_{j=1}^{L}S_{k,j}^{x}(\Sigma_{j}^{\eta})^{-1}\eta_{j},\;\;L\leq k,$$

where S
x k, j
= E[xkη T
j
]. From (6), it is clear that

$${\mathcal{S}}_{k,j}^{x}=\mathbb{E}[x_{k}y_{j}^{T}]-(1-\overline{{{\lambda}}}_{j})\mathbb{E}[x_{k}\overline{{{z}}}_{j/j-1}^{T}].$$

Using (3) and (4), and taking into account hypotheses *(H1)* and *(H8)*, we have

$$\mathbb{E}[x_{k}y_{j}^{T}]=(1-\overline{{{A}}}_{j})\overline{{{\gamma}}}_{j}A_{k}B_{j}^{T}H_{j}^{T},\ \ 1\leq j\leq k,$$

and, from (7), the following expression is deduced

$$\mathbb{E}[x_{k}\widetilde{z_{j/j-1}^{T}}]=\overline{{{\gamma}}}_{j}\mathbb{E}[x_{k}\widetilde{x_{j/j-1}^{T}}]H_{j}^{T}+\mathbb{E}[x_{k}\widetilde{v}_{j/j-1}^{T}],\ \ 1\leq j\leq k.$$

Using again the general expression (5) for the estimators bx T
j/ j−1 andbv T
j/ j−1
, we can write

$$\mathbb{E}[x_{k}\widehat{a}_{j/j-1}^{T}]=\sum_{i=1}^{j-1}\mathcal{S}_{k,i}^{x}(\Sigma_{i}^{\eta})^{-1}(\mathcal{S}_{j,i}^{a})^{T},\;\;j\geq2,\;\;a=x,v.$$

Consequently, S
x k, j admits the following expression

$$S_{k,j}^{x}=(1-\overline{{{\lambda}}}_{j})\Big[\,\overline{{{\gamma}}}_{j}A_{k}B_{j}^{T}H_{j}^{T}-(1-\delta_{j,1})\sum_{i=1}^{j-1}S_{k,i}^{x}(\Sigma_{i}^{n})^{-1}\big(\overline{{{\gamma}}}_{j}H_{j}S_{j,i}^{x}+S_{j,i}^{w}\big)^{T}\Big],\;\;j\geq1,$$

from which the following factorization is easily deduced:

$${\bf S}_{k,j}^{x}=A_{k}\Psi_{j}^{x},\;\;j\leq k,$$
, j ≤ k, (17)
$$(17)$$
$${\mathfrak{s}}$$

just defining

$$\Psi_{j}^{x}=(1-\overline{{{\lambda}}}_{j})\Big[\,\overline{{{\gamma}}}_{j}B_{j}^{T}H_{j}^{T}-(1-\delta_{j,1})\sum_{i=1}^{j-1}\Psi_{i}^{x}(\Sigma_{i}^{n})^{-1}(\overline{{{\gamma}}}_{j}H_{j}A_{j}\Psi_{i}^{x}+\mathcal{S}_{j,i}^{n})^{T}\,\Big],\;\;j\geq1.$$
$$(18)$$
Ti, j ≥ 1. (18)
Similarly, the following identity is derived

$${\mathcal{S}}_{k,j}^{v}=E_{k}\Psi_{j}^{v},\;\;j\leq k,$$
, j ≤ k, (19)
with

$$\Psi_{j}^{v}=(1-\overline{{{\lambda}}}_{j})\Big[\ F_{j}^{T}-(1-\delta_{j,1})\sum_{i=1}^{j-1}\Psi_{i}^{v}(\Sigma_{i}^{\eta})^{-1}(\overline{{{\nu}}}_{j}H_{j}A_{j}\Psi_{i}^{x}+E_{j}\Psi_{i}^{v})^{T}\Big],\ \ j\geq1.$$
$$(20)$$
$$(21)$$
Ti, j ≥ 1. (20)
Thus, defining the following vectors:

$$e_{k}^{a}=\sum_{j=1}^{k}\Psi_{j}^{a}(\Sigma_{j}^{\eta})^{-1}\eta_{j},\;\;k\geq1,\;\;a=x,v,$$
$$(22)$$
−1ηj, k ≥ 1, a = x, v, (21)
and using (17) and (19), we have that

$$\widehat{x_{k/k}}=A_{k}e_{k}^{x},\quad\widehat{x_{k/k-1}}=A_{k}e_{k-1}^{x},\quad\widehat{v}_{k/k-1}=E_{k}e_{k-1}^{v},\quad\ k\geq1.$$
, k ≥ 1. (22)
Substituting these expressions for bxk/k−1 andbvk/k−1 in (7) and taking into account the definition of ∆
a k
(a = x, v) given in (9) we have that

$$\widehat{z_{k/k-1}}=\Delta_{k}^{x}e_{k-1}^{x}+\Delta_{k}^{v}e_{k-1}^{v}+\overline{{{\gamma}}}_{k}C_{k},\;\;k\geq1.$$
k−1 + γkCk, k ≥ 1. (23)
So, using (6), expression (10) for the innovation is straightforward.

In order to obtain the innovation covariance matrix, Σ
η k
= E-ηkη T
k
, we use (6) and the OPL
to deduce that

$$\Sigma_{k}^{\eta}=\Sigma_{k}^{y}-(1-\overline{{{\lambda}}}_{k})^{2}\mathbb{E}[\widehat{z}_{k/k-1}\widehat{z}_{k/k-1}^{T}],\;k\geq1.$$
Defining $T_{k}^{ab}=\mathbb{E}[e_{k}^{a}(e_{k}^{b})^{T}],\ \ k\geq1\ (a,b=x,v)$, and using (23), we can write 
$$\begin{array}{r l}{{\mathbb{E}[\widehat{c_{k/k-1}}\widehat{c_{k/k-1}^{T}}]=}}&{{\Delta_{k}^{x}T_{k-1}^{x x}(\Delta_{k}^{x})^{T}+\Delta_{k}^{x}T_{k-1}^{x y}(\Delta_{k}^{y})^{T}}}\\ {{}}&{{+\Delta_{k}^{v}T_{k-1}^{v x}(\Delta_{k}^{x})^{T}+\Delta_{k}^{v}T_{k-1}^{v v}(\Delta_{k}^{v})^{T}+\overline{{{\gamma}}}_{k}^{2}C_{k}C_{k}^{T}}}\end{array}$$

and expression (11) for the innovation covariance matrix is immediately obtained. The formulas for Σ
y k and Σ
z k given in (12) are easily derived from the model hypotheses.

Using (21), the recursion (13) is directly obtained and, also, the following expression for T
ab kis straightforward:

$$T_{k}^{a b}=\sum_{j=1}^{k}\Psi_{j}^{a}(\Sigma_{j}^{\eta})^{-1}(\Psi_{j}^{b})^{T},\;\;k\geq1,$$
$$(24)$$

which, together with the definitions (8) and (9), leads to expression (14) just by substitution in (18) and (20). Also, from the above expression, the recursion (15) is immediately obtained.

Finally, the filter expression (16) has been already obtained in (22), so the proof is complete.

Remark 5. The derivation of the estimation algorithm presented in Theorem 3.1 is based on the linear approximation (4) of the nonlinear observations around a nominal trajectory of the signal. Hence, the first question that arises is what to do if we do not have a reliable nominal signal trajectory. In such cases, we can follow an EKF approach; in other words, we can use the prediction estimates {bxk/k−1}k≥1 as a nominal trajectory of the signal, because bxk/k−1 is our best approximation of xk before the observation at time k is considered. When doing so, the matrices Hk and Ck in equation (4) are given by

$$H_{k}=\frac{\partial h_{k}(x)}{\partial x}\bigg|_{x=A_{k}e_{k-1}^{x}},\quad C_{k}=h_{k}(A_{k}e_{k-1}^{x})-H_{k}A_{k}e_{k-1}^{x},$$

since the prediction estimate at time k is calculated as bxk/k−1 = Ake x k−1
(see (22)).

Substituting these matrices in (7) and taking into account that bvk/k−1 = Eke v k−1
(see (22)),
we obtain that

$$\widehat{\Xi_{k/k-1}}=\overline{{{\gamma}}}_{k}h_{k}(A_{k}e_{k-1}^{x})+E_{k}e_{k-1}^{v},\;\;k\geq1,$$
, k ≥ 1, (25)
from which expression (10) for the innovation admits the following simplified form:

$$\eta_{k}=y_{k}-(1-\overline{{{\lambda}}}_{k})\left(\overline{{{\gamma}}}_{k}h_{k}(A_{k}e_{k-1}^{x})+E_{k}e_{k-1}^{v}\right),\;\;k\geq1,$$
, k ≥ 1, (26)
and the innovation covariance matrix, Σ
η k
, can be written as

$$\Sigma_{k}^{\eta}=(1-\overline{{{\lambda}}}_{k})\Sigma_{k/k-1}^{\widetilde{z}}+\overline{{{\lambda}}}_{k}(1-\overline{{{\lambda}}}_{k})\widehat{z}_{k/k-1}\widehat{z}_{k/k-1}^{\widetilde{T}}+\overline{{{\lambda}}}_{k}\Sigma_{k}^{w},\;\;k\geq1,$$
, k ≥ 1, (27)
whith

Σezk/k−1 = γkHkΣex k/k−1H T k + γk (1 − γk )hk(Ake x k−1 )h T k (Ake x k−1 ) +Σevk/k−1 , k ≥ 1, Σex k/k−1 = AkB T k − AkT xx k−1 A T k , k ≥ 1, Σevk/k−1 = EkF T k − EkT vv k−1 E T k , k ≥ 1.
$$(27)$$
$$(28)$$
The following steps summarize the filtering algorithm and its computational procedure when the prediction estimates, bxk/k−1 = Ake x k−1
, are used as a nominal trajectory of the signal.

Filtering algorithm using x0 k
= Ake x k−1 as a nominal trajectory of the signal

_Step 1._ Set $k=1$ and initialize the algorithm with $e_{0}^{a}=0$ and $T_{0}^{ab}=0$ ($a,b=x,v$).  _Step 2._ Compute $H_{k}=\dfrac{\partial h_{k}(x)}{\partial x}\big{|}_{x=A_{k}e_{k-1}^{a}}$ and, from it, compute $\Gamma_{k}^{a}$ and $\Delta_{k}^{a}$ ($a=x,v$) by (8) and (9), respectively.  _Step 3._ Compute $\Psi_{k}^{a}$ ($a=x,v$) by (14).  
Step 4. Computebzk/k−1 by (25) and, from it, compute the innovation ηk by (26).
Step 5. Compute the matrices Σezk/k−1
by (28) and, from them, compute the innovation covariance matrix Σ
η
k
by (27).