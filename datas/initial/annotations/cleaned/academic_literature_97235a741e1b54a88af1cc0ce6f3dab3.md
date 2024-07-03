# Filtering and smoothing estimation algorithms from uncertain nonlinear observations with time-correlated additive noise and random deception attacks 

R. Caballero-Águila ${ }^{a}$ J. Hu $^{\mathrm{b}}$ and J. Linares-Pérez ${ }^{\mathrm{c}}$<br>${ }^{a}$ Departamento de Estadística. Universidad de Jaén. Paraje Las Lagunillas. 23071. Jaén. Spain;<br>${ }^{\mathrm{b}}$ Key Laboratory of Advanced Manufacturing and Intelligent Technology, Ministry of Education,<br>Harbin University of Science and Technology, Harbin 150080, China;<br>${ }^{\text {c} D e p a r t a m e n t o ~ d e ~ E s t a d i ́ s t i c a . ~ U n i v e r s i d a d ~ d e ~ G r a n a d a . ~ A v e n i d a ~ F u e n t e n u e v a . ~ 18071 . ~ G r a n a d a . ~ S p a i n ~}$

## ARTICLE HISTORY

Compiled May 9, 2024


#### Abstract

This paper discusses the problem of estimating a stochastic signal from nonlinear uncertain observations with time-correlated additive noise described by a first-order Markov process. Random deception attacks are assumed to be launched by an adversary, and both this phenomenon and the uncertainty in the observations are modelled by two sets of Bernoulli random variables. Under the assumption that the evolution model generating the signal to be estimated is unknown and only the mean and covariance functions of the processes involved in the observation equation are available, recursive algorithms based on linear approximations of the real observations are proposed for the least-squares filtering and fixed-point smoothing problems. Finally, the feasibility and effectiveness of the developed estimation algorithms are verified by a numerical simulation example, where the impact of uncertain observation and deception attack probabilities on estimation accuracy is evaluated.


## KEYWORDS

Nonlinear observation models; least-squares estimation; missing measurements;

time-correlated noise; random deception attacks

## 1. Introduction

Although state-space models can theoretically be divided into linear and nonlinear models, in practice there are no strictly linear models. So-called linear systems are nothing more than approximations, usually valid over a limited range of values of the variables involved in the model. Even though many systems have a sufficiently high degree of approximation to linearity, we eventually encounter systems that deviate significantly from linear behaviour, even within a limited operating range. In such cases, the accuracy of linear estimation techniques diminishes and it becomes necessary to explore nonlinear estimation approaches Simon, 2006). Despite these considerations, there has been a huge amount of work on linear estimation for linear systems and the mathematical tools available for this kind of systems are much more accessible and well understood. For this reason, linear approximations are often used to adapt linear estimation techniques to the nonlinear problems that are encountered in[^0] SCIENCE on March 19 2024, available at: https://doi.org/10.1080/00207721.2024.2328781.
many branches of practical domains, such as computer vision, communications, navigation and tracking systems or econometrics and finance (Hu et al., 2015).

The performance of estimation algorithms is often affected by the occurrence of random uncertainties, a common one being the presence of missing measurements (also called uncertain observations). Indeed, this phenomenon is unavoidable in many real-world scenarios where the information received by the estimator side is usually incomplete, due to several causes (e.g., random failures in the measurement mechanism, accidental loss of some data packets or inaccessibility of data at certain times). In these situations, it is necessary to consider the influence of this incomplete information when designing estimation algorithms. In the context of linear systems, the estimation problem for multisensor stochastic uncertain systems with missing measurements and unknown measurement disturbances is addressed in Pang \& S Sun (2015). Using a new augmented state approach, three robust Kalman-like filtering algorithms are proposed in Ran \& Deng (2020) for a class of multisensor systems with mixed uncertainties including random delays, missing measurements, multiplicative noises and uncertain noise variances. The distributed filtering problem for systems with missing measurements is studied in Wen et al. (2020), under the assumption that the state noises and the measurement noises are correlated. In the context of nonlinear systems, the impact of incomplete information on the estimation problem has also been analyzed, e.g., in Hu et al. (2023b), where a class of singular systems subject to random delays, packet dropouts and nonlinearities, and in Han et al. (2017), where a distributed $H_{\infty}$-consensus filtering approach is proposed for nonlinear systems with missing measurements. More recently, a particle filter is proposed in Ma \& Wang (2022) for nonlinear systems with time-varying delays and unknown noise distribution and, in Hu et al. (2023a), a distributed resilient fusion filtering algorithm is designed for nonlinear systems with dynamic event-triggered mechanism under the missingmeasurement phenomenon. A complete survey on estimation algorithms for nonlinear systems with communication constraints causing random delays, missing/fading measurements or randomly occurring incomplete information can be found in Hu et al. (2020).

Many conventional estimation algorithms are typically based on the assumption that the additive noise in measurements is either white or finite-step correlated. However, in practical engineering applications, infinite-step correlated measurement noises can be prevalent, especially when the sampling frequency is sufficiently high, leading to significant correlation over two or more consecutive sampling periods. Over the past decade, the estimation problem has been widely studied under the assumption that the infinite-step time-correlated noise is a first-order Markov process. The state estimation problem for linear systems with multiplicative noise and time-correlated additive noise in the measurements has been investigated in Liu (2015) and an improved steady-state filter has been designed in Liu \& Shi (2019). Least-squares estimation algorithms are proposed in García-Ligero et al. (2020), considering random delays in the transmission connections that are modelled by Markov chains, and in Caballero-Águila et al. (2022), considering random parameter matrices in the measurement model and random packet dropouts for which two different compensation scenarios are compared. Distributed fusion filtering algorithms for uncertain systems with random delays and packet loss prediction compensation are designed in Caballero-Águila \& Linares-Pérez (2023a). Recursive estimation algorithms for linear stochastic uncertain systems with timecorrelated additive noises and packet dropout compensations are proposed in Ma \& Sun (2020) and a similar study for nonlinear systems is carried out in Cheng et al. (2021).

In addressing the estimation problem, security emerges as a crucial consideration that should not be disregarded. The vulnerability to cyber attacks is well-documented in the literature (see, for instance, Mahmoud et al., 2019; Sanchez et al., 2019). Particularly, the es-
timation problem in networked systems exposed to deception attacks has been the focus of numerous significant research endeavors. In general, deception attackers aim to compromise data integrity by maliciously introducing random falsifications into their information. Several research studies have delved into security-guaranteed filtering problems, such as the investigation of centralized solutions for linear time-invariant stochastic systems with multirate-sensor fusion under deception attacks in Wang et al. (2018). The exploration of the $H_{\infty}$-consensus filtering problem for discrete-time systems with multiplicative noises and deception attacks is documented in Han et al. (2019). Additionally, the study of the chance-constrained $H_{\infty}$ state estimation problem for a class of time-varying neural networks, subject to measurement degradation and randomly occurring deception attacks, is presented in Qu et al. (2022). Also, the distributed estimation problem in sensor networks has been addressed under various security threats. Examples include investigations under false data injection attacks in Yang et al. (2019) and under deception attacks in Caballero-Águila \& Linares-Pérez (2023b), Xiao et al. (2020), Ma \& Sun (2023) and Ma et al. (2021).

Motivated by the preceding discussion, our aim is to address the least-squares (LS) estimation problem of signals using nonlinear uncertain observations (missing measurements) with time-correlated additive noise modeled by a first-order Markov process, in the presence of random deception attacks. The proposed recursive algorithms, based on linear approximations, offer a novel approach to mitigating the impact of missing measurements and deception attacks in signal estimation. The main contributions of this paper are summarized as follows: (a) A covariance-based estimation approach is used, so the evolution model of the signal to be estimated does not need to be known. (b) The class of stochastic signals investigated in this paper is quite comprehensive, as the assumptions under which our study is valid are verified by a great variety of stationary and non-stationary signals. (c) The direct estimation of the time-correlated additive noise avoids the use of the differencing method or vector augmentation. ( $d$ ) Despite the fact that the simultaneous consideration of uncertain observations, time-correlated noise and random attacks adds complexity to the model, the proposed filtering and fixed-point smoothing algorithms keep the advantages of recursivity and computational simplicity. (e) The proposed estimators have a satisfactory performance even in the presence of high probability of missing measurements and/or high probability of successful random deception attacks.

The paper is structured as follows. Section 2 details the characteristics of the observation model under consideration. The main results are presented in Section 3, which includes the problem statement (subsection 3.1) and the derivation of the proposed filtering and fixed-point smoothing algorithms (subsections 3.2 and 3.3 , respectively). Section 4 conducts a simulation study to showcase the effectiveness of the proposed filtering and fixed-point smoothing estimators, additionally exploring the impact of uncertain observation and random deception attacks probabilities on estimation performance. Finally, Section5provides some concluding remarks.

The notations and acronyms that are used throughout the paper are summarized in Table 1.

## 2. Mathematical model and preliminaries

### 2.1. Signal process

Consider a signal process $\left\{x_{k}\right\}_{k \geq 1}$ that must be estimated from a set of noisy measurements. Assume that the mathematical model describing the evolution of this signal process is not known, but its mean and covariance functions satisfy the following hypothesis:

Table 1. Notations and acronyms used throughout the paper. All vector and matrix dimensions are assumed to be compatible with algebraic operations unless explicitly stated.

| $\mathbb{R}^{n}$ | Set of $n$-dimensional real vectors |
| :--- | :--- |
| $\mathbb{R}^{n \times m}$ | Set of $n \times m$ real matrices |
| $\left.\frac{\partial f(x)}{\partial x}\right\|_{x=a}$ | $m \times n$ Jacobian matrix of $f: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ at a point $a \in \mathbb{R}^{n}$ |
| $M^{T}$ and $M^{-1}$ | Transpose and inverse of matrix $M$ |
| $\delta_{j, i}$ | Kronecker delta function |
| $\mathbb{E}[a]=\bar{a}$ | Mathematical expectation of a random variable or vector $a$ |
| $\Sigma_{k, s}^{a}$ | Covariance function of a stochastic process $\left\{a_{k}\right\}_{k \geq 1}:$ |
|  | $\Sigma_{k, s}^{a}=\operatorname{Cov}\left[a_{k}, a_{s}\right]=E\left[\left(a_{k}-\bar{a}_{k}\right)\left(a_{s}-\bar{a}_{s}\right)^{T}\right], \Sigma_{k}^{a}=\operatorname{Cov}\left[a_{k}\right]$ |
| $\widehat{a}_{k / s}$ | Optimal linear estimator of the vector $a_{k}$ based on $\left\{y_{1}, \ldots, y_{s}\right\}$ |
| LS | Least-squares |
| OPL | Orthogonal projection lemma |
| EKF | Extended Kalman filter |

(H1) The $n_{x}$-dimensional signal $\left\{x_{k}\right\}_{k \geq 1}$ is a second-order zero-mean random process and its covariance function, $\Sigma_{k, s}^{x}=\operatorname{Cov}\left[x_{k}, x_{s}\right]$, can be factorized as

$$
\Sigma_{k, s}^{x}=A_{k} B_{s}^{T}, s \leq k
$$

where $A_{k}, B_{s} \in \mathbb{R}^{n_{x} \times p}$ are known matrices.

Remark 1. Hypothesis (H1) on the signal covariance function is verified by a great variety of stationary and non-stationary signals (Caballero-Águila et al., 2022). Estimation approaches based on this hypothesis, rather than the state-space model, thus provide a comprehensive framework to obtain general algorithms that cover a wide range of practical situations.

### 2.2. Nonlinear uncertain measurements with time-correlated additive noise

The signal estimation will be performed from $n_{z}$-dimensional nonlinear outputs that are perturbed by additive noise and subject to random failures, causing that some measured outputs are only noise. This phenomenon is described by a sequence of Bernoulli random variables, $\left\{\gamma_{k}\right\}_{k \geq 1}$. When $\gamma_{k}=1$, the actual measurement value is equal to the original measurement value, while $\gamma_{k}=0$ means that the actual measurement is only noise. More specifically, the actual measurements are described by the following mathematical model:

$$
z_{k}=\gamma_{k} h_{k}\left(x_{k}\right)+v_{k}, \quad k \geq 1
$$

with the following hypotheses:

(H2) $\left\{\gamma_{k}\right\}_{k \geq 1}$ is a sequence of independent Bernoulli random variables with known mean function $\bar{\gamma}_{k}=\mathbb{E}\left[\gamma_{k}\right], k \geq 1$.

(H3) For all $k \geq 1$, the function $h_{k}: \mathbb{R}^{n_{x}} \rightarrow \mathbb{R}^{n_{z}}$ is an analytic function.

Remark 2. Hypothesis (H3) guarantees that $h_{k}$ is infinitely differentiable and, for every $x_{0} \in$ $\mathbb{R}^{n_{x}}$, its Taylor series about $x_{0}$ converges to the function in some neighborhood of $x_{0}$. Typical examples of analytic functions are: polynomials, exponential functions, logarithmic functions, trigonometric functions and power functions (Krantz, 2022).

In many engineering applications, the additive noise perturbing the observations has an infinite-step correlation; to better model such situations, the following first-order Markov model is used:

$$
v_{k}=D_{k-1} v_{k-1}+u_{k-1}, \quad k \geq 1
$$

where $D_{k}$ is non-singular for all $k \geq 0$ and the following hypotheses hold:

(H4) $v_{0}$ is a zero-mean random vector with known covariance $\Sigma_{0}^{v}=\operatorname{Cov}\left[v_{0}\right]$.

(H5) The noise process $\left\{u_{k}\right\}_{k \geq 0}$ is a zero-mean white sequence with known covariance function $\Sigma_{k}^{u}=\operatorname{Cov}\left[u_{k}\right], k \geq 0$, and it is independent of the initial vector $v_{0}$.

Remark 3. Hypotheses $(\mathrm{H} 4)$ and $(\mathrm{H} 5)$, together with the non-singularity of $D_{k}$, guarantee that the covariance function of the time-correlated additive noise, $\Sigma_{k, s}^{v}=\operatorname{Cov}\left[v_{k}, v_{s}\right]$, admits the following factorization:

$$
\Sigma_{k, s}^{v}=E_{k} F_{s}^{T}, \quad s \leq k
$$

where $E_{k}=D_{k-1} \cdots D_{0}, F_{s}=\Sigma_{s}^{v}\left(E_{s}^{-1}\right)^{T}$ and $\Sigma_{s}^{v}=\operatorname{Cov}\left[v_{s}\right]$ is recursively obtained as

$$
\Sigma_{s}^{v}=D_{s-1} \Sigma_{s-1}^{v} D_{s-1}^{T}+\Sigma_{s-1}^{u}, s \geq 1
$$

### 2.3. Random deception attacks

In many practical situations, a crucial issue that cannot be ignored in the study of the estimation problem is the possible occurrence of cyber-attacks. In particular, deception attacks constitute a significant threat that attempts to compromise data integrity by maliciously and randomly falsifying information. In this type of attacks, the signal injected by the attacker, $\breve{z}_{k}$, aims to neutralise the actual measurement, $z_{k}$, and replace it with a deceptive noise, $w_{k}$. Specifically,

$$
\breve{z}_{k}=-z_{k}+w_{k}, \quad k \geq 1
$$

where

(H6) The noise process $\left\{w_{k}\right\}_{k \geq 1}$ is a zero-mean white sequence with known covariance function $\Sigma_{k}^{w}=\operatorname{Cov}\left[w_{k}\right], k \geq 1$.

To describe the fact that, in practice, cyber-attacks are often unpredictable and random, a sequence of Bernoulli random variables is adopted. More specifically, the following model with stochastic deception attacks is considered to describe the measurements processed for the estimation:

$$
y_{k}=z_{k}+\lambda_{k} \breve{z}_{k}, \quad k \geq 1
$$

which can be equivalently rewritten as

$$
y_{k}=\left(1-\lambda_{k}\right) z_{k}+\lambda_{k} w_{k}, \quad k \geq 1
$$

where

(H7) $\left\{\lambda_{k}\right\}_{k \geq 1}$ is a sequence of independent Bernoulli random variables with known mean function $\bar{\lambda}_{k}=\mathbb{E}\left[\lambda_{k}\right], k \geq 1$.

Remark 4. The binary values of $\lambda_{k}$ indicate if the adversary actually launch the attack ( $\lambda_{k}=$ 1) or not $\left(\lambda_{k}=0\right)$. When the actual measurement is attacked, $y_{k}=w_{k}$ and only noise will be processed. Otherwise, if no attack is injected, $y_{k}=z_{k}$ and the actual measurement is processed for the estimation.

Finally, the following independence hypotheses on the processes involved in the considered model is required to address the estimation problem.

(H8) The signal process $\left\{x_{k}\right\}_{k \geq 1}$ and the processes $\left\{\gamma_{k}\right\}_{k \geq 1},\left\{v_{k}\right\}_{k \geq 1},\left\{w_{k}\right\}_{k \geq 1}$ and $\left\{\lambda_{k}\right\}_{k \geq 1}$ are mutually independent.

### 2.4. Linearized observations

Under hypotheses $(H 1)-(H 8)$, our goal is to obtain recursive algorithms for the filtering and fixed-point smoothing problems; that is, to address the estimation problem of the signal $x_{k}$ given the nonlinear observations $\left\{y_{1}, \ldots, y_{L}\right\}, L \geq k$. To this end, we will use a similar reasoning to that used to derive the extended Kalman filter. The problem is thus reduced to linearizing the observation equation (1) and then inserting such linearized observations into (3) to calculate the LS linear estimator of the signal from the resulting measurements.

More precisely, from hypothesis (H3), assuming knowledge of a nominal trajectory of the signal, $\left\{x_{k}^{0}\right\}_{k \geq 1}$, the function $h_{k}$ can be expanded in Taylor series about $x_{k}^{0}$ :

$$
h_{k}(x)=h_{k}\left(x_{k}^{0}\right)+\left.\frac{\partial h_{k}(x)}{\partial x}\right|_{x=x_{k}^{0}}\left(x-x_{k}^{0}\right)+\cdots, k \geq 1,
$$

Neglecting the terms of order greater than one in this Taylor expansion, equation (1) can be approximated by the following linearized observation equation

$$
z_{k}=\gamma_{k}\left(H_{k} x_{k}+C_{k}\right)+v_{k}, k \geq 1
$$

where

$$
H_{k}=\left.\frac{\partial h_{k}(x)}{\partial x}\right|_{x=x_{k}^{0}}, \quad C_{k}=h_{k}\left(x_{k}^{0}\right)-H_{k} x_{k}^{0} .
$$

The above equation is a linear equation affected by the binary multiplicative noise, $\left\{\gamma_{k}\right\}_{k \geq 1}$, and the time-correlated additive noise, $\left\{v_{k}\right\}_{k z 1}$. Our aim is to derive recursive estimation algorithms by using the linear approximation (4) in the equation for the available observations (3).

## 3. Main results

### 3.1. Problem statement and innovation approach

Our goal is to obtain recursive algorithms for the LS linear filter and fixed-point smoother of the signal $x_{k}$ from the available observations (3), based on the linearized measurements

(4). For this purpose, we will use an innovation approach. According to this approach, the observation process is transformed into an equivalent innovation process and the LS linear estimator, $\widehat{\zeta}_{k / L}$, of a random vector $\zeta_{k}$ based on a set of observations $\left\{y_{j}, 1 \leq j \leq L\right\}$, can be expressed as a linear combination of the innovations as follows:

$$
\widehat{\zeta}_{k / L}=\sum_{j=1}^{L} \mathcal{S}_{k, j}^{\zeta}\left(\Sigma_{j}^{\eta}\right)^{-1} \eta_{j}, \quad k, L \geq 1
$$

where $\mathcal{S}_{k, j}^{\zeta}=\mathbb{E}\left[\zeta_{k} \eta_{j}^{T}\right], \eta_{j}=y_{j}-\widehat{y}_{j / j-1}$ is the innovation at time $j$ and $\Sigma_{j}^{\eta}=\operatorname{Cov}\left[\eta_{j}\right]$.

Using (3) and the model hypotheses, the innovation can be written as

$$
\eta_{k}=y_{k}-\left(1-\bar{\lambda}_{k}\right) \widehat{z}_{k / k-1}, \quad k \geq 1
$$

and, from the linear approximation (4), it is clear that the prediction estimator of $z_{k}$ can be approximated by

$$
\widehat{z}_{k / k-1}=\bar{\gamma}_{k}\left(H_{k} \widehat{x}_{k / k-1}+C_{k}\right)+\widehat{v}_{k / k-1}
$$

Expressions (5)-(7) are the key points for the derivation of the recursive filtering and fixedpoint smoothing algorithms that will be presented in the following subsections.

### 3.2. Recursive filtering algorithm

For the sake of convenience, we introduce the following notations:

$$
\begin{aligned}
& \Gamma_{k}^{a}= \begin{cases}\bar{\gamma}_{k} H_{k} B_{k}, & a=x, \\
F_{k}, & a=v,\end{cases} \\
& \Delta_{k}^{a}= \begin{cases}\bar{\gamma}_{k} H_{k} A_{k}, & a=x, \\
E_{k}, & a=v\end{cases}
\end{aligned}
$$

Theorem 3.1. Consider the observation model (Z)-(3), where the processes involved satisfy hypotheses (H1)-(H8). Then, the innovation $\eta_{k}$ is calculated as

$$
\eta_{k}=y_{k}-\left(1-\bar{\lambda}_{k}\right)\left(\Delta_{k}^{x} e_{k-1}^{x}+\Delta_{k}^{v} e_{k-1}^{v}+\bar{\gamma}_{k} C_{k}\right), k \geq 1
$$

and its covariance matrix $\Sigma_{k}^{\eta}$ satisfies

$$
\begin{aligned}
\Sigma_{k}^{\eta}= & \Sigma_{k}^{y}-\left(1-\bar{\lambda}_{k}\right)^{2}\left[\left(\Delta_{k}^{x} T_{k-1}^{x x}+\Delta_{k}^{v} T_{k-1}^{v x}\right)\left(\Delta_{k}^{x}\right)^{T}\right. \\
& \left.+\left(\Delta_{k}^{x} T_{k-1}^{x v}+\Delta_{k}^{v} T_{k-1}^{v v}\right)\left(\Delta_{k}^{v}\right)^{T}+\bar{\gamma}_{k}^{2} C_{k} C_{k}^{T}\right], \quad k \geq 1
\end{aligned}
$$

with

$$
\begin{aligned}
& \Sigma_{k}^{y}=\left(1-\bar{\lambda}_{k}\right) \Sigma_{k}^{z}+\bar{\lambda}_{k} \Sigma_{k}^{w}, \quad k \geq 1 \\
& \Sigma_{k}^{z}=\bar{\gamma}_{k}\left(H_{k} A_{k} B_{k}^{T} H_{k}^{T}+C_{k} C_{k}^{T}\right)+E_{k} F_{k}^{T}, \quad k \geq 1
\end{aligned}
$$

The vectors $e_{k}^{a}(a=x, v)$ are recursively obtained by

$$
e_{k}^{a}=e_{k-1}^{a}+\Psi_{k}^{a}\left(\Sigma_{k}^{\eta}\right)^{-1} \eta_{k}, \quad k \geq 1 ; \quad e_{0}^{a}=0
$$

where

$$
\Psi_{k}^{a}=\left(1-\bar{\lambda}_{k}\right)\left(\Gamma_{k}^{a}-\Delta_{k}^{x} T_{k-1}^{x a}-\Delta_{k}^{v} T_{k-1}^{v a}\right)^{T}, \quad k \geq 1
$$

The matrices $T_{k}^{a b}=\mathbb{E}\left[e_{k}^{a}\left(e_{k}^{b}\right)^{T}\right](a, b=x, v)$ are also recursively calculated by

$$
T_{k}^{a b}=T_{k-1}^{a b}+\Psi_{k}^{a}\left(\Sigma_{k}^{\eta}\right)^{-1}\left(\Psi_{k}^{b}\right)^{T}, \quad k \geq 1 ; \quad T_{0}^{a b}=0
$$

The filtering estimator of the signal, $\widehat{x}_{k / k}$, is then computed by

$$
\widehat{x}_{k / k}=A_{k} e_{k}^{x}, k \geq 1
$$

Proof. According to (5), the estimator of the signal $x_{k}$ based on a set of observations $\left\{y_{1}, \ldots, y_{L}\right\}$, with $L \leq k$, is given by

$$
\widehat{x}_{k / L}=\sum_{j=1}^{L} \mathcal{S}_{k, j}^{x}\left(\Sigma_{j}^{\eta}\right)^{-1} \eta_{j}, \quad L \leq k
$$

where $\mathcal{S}_{k, j}^{x}=\mathbb{E}\left[x_{k} \eta_{j}^{T}\right]$. From (6), it is clear that

$$
\mathcal{S}_{k, j}^{x}=\mathbb{E}\left[x_{k} y_{j}^{T}\right]-\left(1-\bar{\lambda}_{j}\right) \mathbb{E}\left[x_{k} \widehat{z}_{j / j-1}^{T}\right]
$$

Using (3) and (4), and taking into account hypotheses (H1) and (H8), we have

$$
\mathbb{E}\left[x_{k} y_{j}^{T}\right]=\left(1-\bar{\lambda}_{j}\right) \bar{\gamma}_{j} A_{k} B_{j}^{T} H_{j}^{T}, \quad 1 \leq j \leq k
$$

and, from (7), the following expression is deduced

$$
\mathbb{E}\left[x_{k} \widehat{z}_{j / j-1}^{T}\right]=\bar{\gamma}_{j} \mathbb{E}\left[x_{k} \widehat{x}_{j / j-1}^{T}\right] H_{j}^{T}+\mathbb{E}\left[x_{k} \widehat{v}_{j / j-1}^{T}\right], \quad 1 \leq j \leq k
$$

Using again the general expression (5) for the estimators $\widehat{x}_{j / j-1}^{T}$ and $\widehat{v}_{j / j-1}^{T}$, we can write

$$
\mathbb{E}\left[x_{k} \widehat{a}_{j / j-1}^{T}\right]=\sum_{i=1}^{j-1} \mathcal{S}_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\mathcal{S}_{j, i}^{a}\right)^{T}, j \geq 2, a=x, v
$$

Consequently, $\mathcal{S}_{k, j}^{x}$ admits the following expression

$$
\mathcal{S}_{k, j}^{x}=\left(1-\bar{\lambda}_{j}\right)\left[\bar{\gamma}_{j} A_{k} B_{j}^{T} H_{j}^{T}-\left(1-\delta_{j, 1}\right) \sum_{i=1}^{j-1} \mathcal{S}_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\bar{\gamma}_{j} H_{j} \mathcal{S}_{j, i}^{x}+\mathcal{S}_{j, i}^{v}\right)^{T}\right], \quad j \geq 1
$$

from which the following factorization is easily deduced:

$$
\mathcal{S}_{k, j}^{x}=A_{k} \Psi_{j}^{x}, \quad j \leq k
$$

just defining

$$
\Psi_{j}^{x}=\left(1-\bar{\lambda}_{j}\right)\left[\bar{\gamma}_{j} B_{j}^{T} H_{j}^{T}-\left(1-\delta_{j, 1}\right) \sum_{i=1}^{j-1} \Psi_{i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\bar{\gamma}_{j} H_{j} A_{j} \Psi_{i}^{x}+\mathcal{S}_{j, i}^{v}\right)^{T}\right], \quad j \geq 1
$$

Similarly, the following identity is derived

$$
\mathcal{S}_{k, j}^{v}=E_{k} \Psi_{j}^{v}, \quad j \leq k
$$

with

$$
\Psi_{j}^{v}=\left(1-\bar{\lambda}_{j}\right)\left[F_{j}^{T}-\left(1-\delta_{j, 1}\right) \sum_{i=1}^{j-1} \Psi_{i}^{v}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\bar{\gamma}_{j} H_{j} A_{j} \Psi_{i}^{x}+E_{j} \Psi_{i}^{v}\right)^{T}\right], \quad j \geq 1
$$

Thus, defining the following vectors:

$$
e_{k}^{a}=\sum_{j=1}^{k} \Psi_{j}^{a}\left(\Sigma_{j}^{\eta}\right)^{-1} \eta_{j}, \quad k \geq 1, a=x, v
$$

and using (17) and (19), we have that

$$
\widehat{x}_{k / k}=A_{k} e_{k}^{x}, \quad \widehat{x}_{k / k-1}=A_{k} e_{k-1}^{x}, \quad \widehat{v}_{k / k-1}=E_{k} e_{k-1}^{v}, \quad k \geq 1
$$

Substituting these expressions for $\widehat{x}_{k / k-1}$ and $\widehat{v}_{k / k-1}$ in (7) and taking into account the definition of $\Delta_{k}^{a}(a=x, v)$ given in (9) we have that

$$
\widehat{z}_{k / k-1}=\Delta_{k}^{x} e_{k-1}^{x}+\Delta_{k}^{v} e_{k-1}^{v}+\bar{\gamma}_{k} C_{k}, \quad k \geq 1
$$

So, using (6), expression (10) for the innovation is straightforward.

In order to obtain the innovation covariance matrix, $\Sigma_{k}^{\eta}=\mathbb{E}\left[\eta_{k} \eta_{k}^{T}\right]$, we use (6) and the OPL to deduce that

$$
\Sigma_{k}^{\eta}=\Sigma_{k}^{y}-\left(1-\bar{\lambda}_{k}\right)^{2} \mathbb{E}\left[\widehat{z}_{k / k-1} \widehat{z}_{k / k-1}^{T}\right], k \geq 1
$$

Defining $T_{k}^{a b}=\mathbb{E}\left[e_{k}^{a}\left(e_{k}^{b}\right)^{T}\right], k \geq 1(a, b=x, v)$, and using (23), we can write

$$
\begin{aligned}
\mathbb{E}\left[\widehat{z}_{k / k-1} \widehat{z}_{k / k-1}^{T}\right]= & \Delta_{k}^{x} T_{k-1}^{x x}\left(\Delta_{k}^{x}\right)^{T}+\Delta_{k}^{x} T_{k-1}^{x v}\left(\Delta_{k}^{v}\right)^{T} \\
& +\Delta_{k}^{v} T_{k-1}^{v x}\left(\Delta_{k}^{x}\right)^{T}+\Delta_{k}^{v} T_{k-1}^{v v}\left(\Delta_{k}^{v}\right)^{T}+\bar{\gamma}_{k}^{2} C_{k} C_{k}^{T}
\end{aligned}
$$

and expression (11) for the innovation covariance matrix is immediately obtained. The formulas for $\Sigma_{k}^{y}$ and $\Sigma_{k}^{z}$ given in (12) are easily derived from the model hypotheses.

Using (21), the recursion (13) is directly obtained and, also, the following expression for $T_{k}^{a b}$ is straightforward:

$$
T_{k}^{a b}=\sum_{j=1}^{k} \Psi_{j}^{a}\left(\Sigma_{j}^{\eta}\right)^{-1}\left(\Psi_{j}^{b}\right)^{T}, \quad k \geq 1
$$

which, together with the definitions (8) and (9), leads to expression (14) just by substitution in (18) and (20). Also, from the above expression, the recursion (15) is immediately obtained. Finally, the filter expression (16) has been already obtained in (22), so the proof is complete.

Remark 5. The derivation of the estimation algorithm presented in Theorem 3.1 is based on the linear approximation (4) of the nonlinear observations around a nominal trajectory of the signal. Hence, the first question that arises is what to do if we do not have a reliable nominal signal trajectory. In such cases, we can follow an EKF approach; in other words, we can use the prediction estimates $\left\{\widehat{x}_{k / k-1}\right\}_{k \geq 1}$ as a nominal trajectory of the signal, because $\widehat{x}_{k / k-1}$ is our best approximation of $x_{k}$ before the observation at time $k$ is considered. When doing so, the matrices $H_{k}$ and $C_{k}$ in equation (4) are given by

$$
H_{k}=\left.\frac{\partial h_{k}(x)}{\partial x}\right|_{x=A_{k} e_{k-1}^{x}}, \quad C_{k}=h_{k}\left(A_{k} e_{k-1}^{x}\right)-H_{k} A_{k} e_{k-1}^{x}
$$

since the prediction estimate at time $k$ is calculated as $\widehat{x}_{k / k-1}=A_{k} e_{k-1}^{x}$ (see (22)).

Substituting these matrices in (7) and taking into account that $\widehat{v}_{k / k-1}=E_{k} e_{k-1}^{v}$ (see (22)), we obtain that

$$
\widehat{z}_{k / k-1}=\bar{\gamma}_{k} h_{k}\left(A_{k} e_{k-1}^{x}\right)+E_{k} e_{k-1}^{v}, \quad k \geq 1
$$

from which expression (10) for the innovation admits the following simplified form:

$$
\eta_{k}=y_{k}-\left(1-\bar{\lambda}_{k}\right)\left(\bar{\gamma}_{k} h_{k}\left(A_{k} e_{k-1}^{x}\right)+E_{k} e_{k-1}^{v}\right), \quad k \geq 1
$$

and the innovation covariance matrix, $\Sigma_{k}^{\eta}$, can be written as

$$
\Sigma_{k}^{\eta}=\left(1-\bar{\lambda}_{k}\right) \Sigma_{k / k-1}^{\widetilde{z}}+\bar{\lambda}_{k}\left(1-\bar{\lambda}_{k}\right) \widehat{z}_{k / k-1} \widehat{z}_{k / k-1}^{T}+\bar{\lambda}_{k} \Sigma_{k}^{w}, \quad k \geq 1
$$

whith

$$
\begin{aligned}
\Sigma_{k / k-1}^{\widetilde{z}}= & \bar{\gamma}_{k} H_{k} \Sigma_{k / k-1}^{\widetilde{x}} H_{k}^{T}+\bar{\gamma}_{k}\left(1-\bar{\gamma}_{k}\right) h_{k}\left(A_{k} e_{k-1}^{x}\right) h_{k}^{T}\left(A_{k} e_{k-1}^{x}\right) \\
& +\Sigma_{k / k-1}^{\widetilde{v}}, k \geq 1, \\
\Sigma_{k / k-1}^{\widetilde{x}}= & A_{k} B_{k}^{T}-A_{k} T_{k-1}^{x x} A_{k}^{T}, \quad k \geq 1 \\
\Sigma_{k / k-1}^{v}= & E_{k} F_{k}^{T}-E_{k} T_{k-1}^{v v} E_{k}^{T}, \quad k \geq 1
\end{aligned}
$$

The following steps summarize the filtering algorithm and its computational procedure when the prediction estimates, $\widehat{x}_{k / k-1}=A_{k} e_{k-1}^{x}$, are used as a nominal trajectory of the signal.

Filtering algorithm using $x_{k}^{0}=A_{k} e_{k-1}^{x}$ as a nominal trajectory of the signal

Step 1. Set $k=1$ and initialize the algorithm with $e_{0}^{a}=0$ and $T_{0}^{a b}=0(a, b=x, v)$.

Step 2. Compute $H_{k}=\left.\frac{\partial h_{k}(x)}{\partial x}\right|_{x=A_{k} e_{k-1}^{x}}$ and, from it, compute $\Gamma_{k}^{a}$ and $\Delta_{k}^{a}(a=x, v)$ by (8) and (9), respectively.

Step 3. Compute $\Psi_{k}^{a}(a=x, v)$ by (14).

Step 4. Compute $\widehat{z_{k} / k-1}$ by (25) and, from it, compute the innovation $\eta_{k}$ by (26).

Step 5. Compute the matrices $\Sigma_{k / k-1}^{\widetilde{z}}$ by (28) and, from them, compute the innovation covariance matrix $\Sigma_{k}^{\eta}$ by (27).

Step 6. Compute $e_{k}^{a}(a=x, v)$ by (13) and $T_{k}^{a b}(a, b=x, v)$ by (15).

Step 7. Compute the filter, $\widehat{x}_{k / k}$, by (16).

Step 8. Set $k=k+1$ and return to Step 2.

### 3.3. Recursive fixed-point smoothing algorithm

The following algorithm allows us to update the filter at any time $k$ as the measurements keep rolling in. More precisely, it allows us to obtain the fixed-point smoothing estimators $\widehat{x}_{k / k+1}, \widehat{x}_{k / k+2}, \ldots$.

Theorem 3.2. Starting from the filter, $\widehat{x}_{k / k}$, at a fixed sampling time $k \geq 1$, the fixed-point smoothers, $\widehat{x}_{k / L}, L>k$, satisfy the following recursion:

$$
\widehat{x}_{k / L}=\widehat{x}_{k / L-1}+\mathcal{S}_{k, L}^{x}\left(\Sigma_{L}^{\eta}\right)^{-1} \eta_{L}, L>k
$$

with

$$
\mathcal{S}_{k, L}^{x}=\left(1-\bar{\lambda}_{L}\right)\left[\left(B_{k}-M_{k, L}^{x}\right)\left(\Delta_{L}^{x}\right)^{T}-M_{k, L}^{v}\left(\Delta_{L}^{v}\right)^{T}\right], L>k
$$

The matrices $M_{k, L}^{a}=\mathbb{E}\left[x_{k}\left(e_{L}^{a}\right)^{T}\right], a=x, v$ are recursively calculated by

$$
M_{k, L}^{a}=M_{k, L-1}^{a}+\mathcal{S}_{k, L}^{x}\left(\Sigma_{L}^{\eta}\right)^{-1}\left(\Psi_{L}^{a}\right)^{T}, L>k ; \quad M_{k, k}^{a}=A_{k} T_{k}^{x a}
$$

Proof. The recursion (29) is immediately deduced from (5), so we must find an expression for $\mathcal{S}_{k, L}^{x}=\mathbb{E}\left[x_{k} \eta_{L}^{T}\right], L>k$. A similar reasoning to that used to obtain $\mathcal{S}_{k, j}^{x}(j \leq k)$ in Theorem 3.1 yields

$$
\mathcal{S}_{k, L}^{x}=\left(1-\bar{\lambda}_{L}\right)\left[\bar{\gamma}_{L} B_{k} A_{L}^{T} H_{L}^{T}-\sum_{i=1}^{L-1} \mathcal{S}_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\bar{\gamma}_{L} H_{L} \mathcal{S}_{L, i}^{x}+\mathcal{S}_{L, i}^{v}\right)^{T}\right], L>k
$$

Taking into account that, from (17) and (19) , $\mathcal{S}_{L, i}^{x}=A_{L} \Psi_{i}^{x}$ and $\mathcal{S}_{L, i}^{v}=E_{L} \Psi_{i}^{v}$, respectively, and using (9), the above expression can be rewritten as

$$
\mathcal{S}_{k, L}^{x}=\left(1-\bar{\lambda}_{L}\right)\left[B_{k}\left(\Delta_{L}^{x}\right)^{T}-\sum_{i=1}^{L-1} \mathcal{S}_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\Delta_{L}^{x} \Psi_{i}^{x}+\Delta_{L}^{v} \Psi_{i}^{v}\right)^{T}\right], L>k
$$

Then, defining $M_{k, L}^{a}=\mathbb{E}\left[x_{k}\left(e_{L}^{a}\right)^{T}\right]$ and using (21), we have that

$$
M_{k, L}^{a}=\sum_{i=1}^{L} \mathcal{S}_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\Psi_{i}^{a}\right)^{T}, a=x, v
$$

from which the formula (30) for $\mathcal{S}_{k, L}^{x}$ is straightforward and also the recursion (31) is immediately deduced. Its initial condition is derived just using that, for $i \leq k, \mathcal{S}_{k, i}^{x}=A_{k} \Psi_{i}^{x}$ and taking into account expression (24). The proof is then complete.

## 4. Numerical simulation example

In this section, a simple numerical simulation example concerning the phase modulation of analogue communication systems is presented with a dual purpose: on the one hand, to illustrate the implementation and performance of the proposed filtering and fixed-point smoothing algorithms and, on the other hand, to analyze the effect of missing measurements and deception attacks on the estimation accuracy.

Scalar signal process: $A R(2)$ model. Consider that the modulating signal $\left\{x_{k}\right\}_{k \geq 1}$ is a stationary stochastic process with autocovariance function

$$
\Sigma_{k, s}^{x}=Q_{1} \beta_{1}^{k-s}+Q_{2} \beta_{2}^{k-s}, \quad k, s \geq 1
$$

where, for $b_{1}=0.1, b_{2}=-0.5$ and $\sigma^{2}=0.25$, the values of $\beta_{i}$ and $Q_{i}, i=1,2$, are given by:

$$
\beta_{1}, \beta_{2}=\frac{-b_{1} \pm \sqrt{b_{1}^{2}-4 b_{2}}}{2}, \quad Q_{1}=\frac{\sigma^{2} \beta_{1}\left(\beta_{2}^{2}-1\right)}{\left(\beta_{2}-\beta_{1}\right)\left(\beta_{1} \beta_{2}+1\right)}, \quad Q_{2}=-\frac{\sigma^{2} \beta_{2}\left(\beta_{1}^{2}-1\right)}{\left(\beta_{2}-\beta_{1}\right)\left(\beta_{1} \beta_{2}+1\right)}
$$

According to hypothesis $(H 1)$, this autocovariance function can be expressed in a separable form defining, for example, $A_{k}=\left[\begin{array}{ll}Q_{1} \beta_{1}^{k} & Q_{2} \beta_{2}^{k}\end{array}\right]$ and $B_{k}=\left[\begin{array}{lll}\beta_{1}^{-k} & \beta_{2}^{-k}\end{array}\right]$.

For simulation purposes, the signal is assumed to be generated from the following secondorder autoregressive model:

$$
x_{k}=-b_{1} x_{k-1}-b_{2} x_{k-2}+\varepsilon_{k}, k \geq 3 ; \quad x_{2}=-b_{1} x_{1}+\varepsilon_{2} ; \quad x_{1}=\varepsilon_{1},
$$

where $\left\{\varepsilon_{k}\right\}_{k \geq 1}$ is a zero-mean white Gaussian noise with variance $\Sigma_{k}^{\varepsilon}=\sigma^{2}, \forall k$.

Uncertain measurements of the carrier signal. Consider the following scalar carrier signal:

$$
h_{k}\left(x_{k}\right)=\cos \left(2 \pi f_{p} k \Delta+m_{A} x_{k}\right), k \geq 1,
$$

where $f_{p}=10[\mathrm{~Hz}]$ is the carrier frequency, $\Delta=0.01$ is the sampling period of the modulating signal $x_{k}$ and $m_{A}=2$ represents the phase sensitivity. Clearly, if we use the prediction estimates as a nominal trajectory of the signal, the functions $H_{k}$ in equation (4) are

$$
H_{k}=-m_{A} \sin \left(2 \pi f_{p} k \Delta+m_{A} A_{k} e_{k-1}^{x}\right), k \geq 1
$$

According to the theoretical model, let us suppose that the measurements of the carrier signal $h_{k}\left(x_{k}\right)$ are given by $\left.\mathbb{1}\right\}$, where:

- $\left\{\gamma_{k}\right\}_{k>1}$ is a sequence of independent Bernoulli random variables with probabilities $P\left(\gamma_{k}=1\right)=\mathbb{E}\left[\gamma_{k}\right]=\bar{\gamma}, k \geq 1$.
- The noise process $\left\{v_{k}\right\}_{k \geq 0}$ is generated by (2) where $D_{k}=0.75,\left\{u_{k}\right\}_{k \geq 0}$ is a zeromean white Gaussian noise with $\Sigma_{k}^{u}=0.01, \forall k \geq 0$, and $v_{0}$ is a zero-mean Gaussian variable with $\Sigma_{0}^{v}=0.1$.

Random deception attacks. Finally, also according to the theoretical model, let us suppose that the measurements are subject to deception attacks and the observations available for the estimation, $y_{k}$, are given by $(\sqrt{3})$, where:

- The noise of the false data injection attacks $\left\{w_{k}\right\}_{k \geq 1}$ is a standard Gaussian white process.
- The status of the attacks is described by a white sequence of Bernoulli random variables $\left\{\lambda_{k}\right\}_{k \geq 1}$, with probabilities $P\left(\lambda_{k}=1\right)=\mathbb{E}\left[\lambda_{k}\right]=\bar{\lambda}, k \geq 1$.

Under these conditions, using the proposed filtering and smoothing algorithms, the phase demodulation problem is considered. This problem consists of estimating the signal $x_{k}$ from the observed values $y_{k}$ and, for this purpose, we have implemented a MATLAB program that simulates the values of the signal, $x_{k}$, the uncertain measurements, $z_{k}$, and the available ones, $y_{k}$, considering different probabilities $\bar{\gamma}$ and $\bar{\lambda}$, and provides the filtering and fixed-point smoothing estimates of $x_{k}$ obtained from theorems 1 and 2, respectively.

Considering one thousand independent simulations, each with fifty iterations of the algorithms, in order to quantify the performance of the proposed estimators, we use the root mean square error (RMSE) criterion, which is widely used because it allows straightforward quantitative comparisons. Denoting $\left\{x_{k}^{(s)}\right\}_{k=1, \ldots, 50}$ the $s$-th set of the simulated data (which is taken as the $s$-th set of true values of the signal), and $\widehat{x}_{k / k+h}^{(s)}$ as the filtering $(h=0)$ and fixed-point smoothing $(h=2)$ estimates at time $k$ in the $s$-th simulation run, the RMSE at time $k$ is calculated by

$$
\operatorname{RMSE}_{k}=\sqrt{\frac{1}{1000} \sum_{s=1}^{1000}\left(x_{k}^{(s)}-\widehat{x}_{k / k+h}^{(s)}\right)^{2}}, \quad 1 \leq k \leq 50, \quad h=0,2
$$

First, considering fixed probabilities $\bar{\gamma}=0.7$ and $\bar{\lambda}=0.3$, Figure 1 displays the values $\mathrm{RMSE}_{k}$, for $k=1, \ldots, 50$, corresponding to the filtering $\left(\widehat{x}_{k / k}\right)$ and fixed-point smoothing $\left(\widehat{x}_{k / k+2}\right)$ estimates. From this figure, it can be seen that, at any time $k$, the $\operatorname{RMSE}_{k}$ of the smoothing estimates is smaller than that of the filtering estimates; hence, according to the $\mathrm{RMSE}_{k}$ criterion, the smoother outperforms the filter. Analogous results are obtained for other values of the probabilities $\bar{\gamma}$ and $\bar{\lambda}$.

In order to analyze the overall performance of the estimations provided by the filtering and smoothing algorithms as a function of the deception attack probability $\bar{\lambda}$, Figure 2 shows the mean values of $\mathrm{RMSE}_{k}$ corresponding to the 50 iterations, versus $\bar{\lambda}=0.1$ to 0.9 , when $\bar{\gamma}=0.7$ and 0.9 . As expected, it is shown that the mean values of $\mathrm{RMSE}_{k}$, for both filtering and smoothing estimates, become larger as the deception attack probability $\bar{\lambda}$ increases, and this increase is less noticeable for high values of $\bar{\lambda}$. Furthermore, this figure shows the superiority of the smoother over the filter and also that, for $\bar{\gamma}=0.9$, the results of both estimators are better than those obtained for $\bar{\gamma}=0.7$, and this improvement is more evident for values of $\bar{\lambda}$ less than or equal to 0.5 .

Finally, to illustrate the influence of $\bar{\gamma}$ (the probability that the observations contain the signal) on the performance of the estimators, Figure 3 shows the mean values of $\mathrm{RMSE}_{k}$ corresponding to the 50 iterations, for a range of $\bar{\gamma}$ values from 0.1 to 0.9 , when $\bar{\lambda}=0.1$ and 0.3. For these values of $\bar{\lambda}$, as expected, the mean values of $\mathrm{RMSE}_{k}$, for both filtering and smoothing estimates, decrease as the probability $\bar{\gamma}$ increases, meaning that better estimations are obtained as the probability that the signal is missing in the measurements, $1-\bar{\gamma}$, decreases. Moreover, this improvement is more noticeable for high values of $\bar{\gamma}$. This figure also shows the superiority of the smoother over the filter and that, for $\bar{\lambda}=0.1$, the results of both estimators are better than those obtained for $\bar{\lambda}=0.3$, being this improvement more significant for values of $\bar{\gamma}$ greater than or equal to 0.5 .

## 5. Conclusions

Recursive algorithms for the LS filtering and fixed-point smoothing problems from nonlinear observations perturbed by time-correlated additive noise and subject to random failures, causing that some measured outputs are only noise, have been proposed. The possibility of random deception attacks adds some complexity to the mathematical model considered. Using linear approximations of the actual observations, together with the projection theory and the innovation approach, the derivation of the estimation algorithms is based on the EKF approach. Some numerical results are used to examine the performance of the proposed estimators and to analyze the effect of missing measurement and deception attack success probabilities on the estimation accuracy.

Future research topics would include extending the proposed framework to deal with other nonlinear estimation approaches, such as unscented Kalman filtering, cubature Kalman filtering, particle filtering, Gaussian-Hermite filtering, divided differences filtering or Bayesian filtering. Another interesting further research direction would be considering nonlinear multisensor systems with different communication constraints (random delays, fading measurements and packet dropouts, among others) and different communication protocols (e.g., event triggering mechanisms, random communication protocol or round-robin protocol).

## Disclosure statement

The authors report there are no competing interests to declare.

## Data availability statement

Data sharing is not applicable to this article as no new data were created or analyzed in this study.

## Funding

Grant PID2021-124486NB-I00 funded by MCIN/AEI/ 10.13039/501100011033 and by "ERDF A way of making Europe".

## Notes on contributors

R. Caballero-Águila received the M.Sc. degree in Mathematics and Ph.D. degree in Polynomial Filtering in Systems with Uncertain Observations, both from the University of Granada (Spain), in 1997 and 1999, respectively. In 1997, she joined the University of Jaén (Spain), where she is currently a Professor with the Department of Statistics and Operations Research. Her current research interests include stochastic systems, filtering, prediction and smoothing.

Jun $H u$ received the B.Sc. degree in information and computing science and M.Sc. degree in Applied Mathematics from the Harbin University of Science and Technology, Harbin, China, in 2006 and 2009, respectively, and the Ph.D. degree in control science and engineering from the Harbin Institute of Technology, Harbin, in 2013. From 2010 to 2012, he was a Visiting Ph.D. Student with the Department of Information Systems and Computing, Brunel University, Uxbridge, U.K. From 2014 to 2016, he was an Alexander von Humboldt Research

Fellow with the University of Kaiserslautern, Kaiserslautern, Germany. From 2018 to 2021, he was a Research Fellow with the University of South Wales, U.K. He is currently with the Department of Applied Mathematics, Harbin University of Science and Technology, and also with the School of Automation, Harbin University of Science and Technology, Harbin. His research interests include nonlinear control, filtering and fault estimation, time-varying systems and complex networks.

J. Linares-Pérez received the M.Sc. degree in Mathematics and Ph.D. in Stochastic Differential Equations, both from the University of Granada (Spain) in 1980 and 1982, respectively. She is currently a Professor with the Department of Statistics and Operations Research, University of Granada (Spain). Her research interests are related with stochastic calculus and estimation in stochastic systems.

## References

Caballero-Águila R, Hu J, Linares-Pérez J. Two Compensation Strategies for Optimal Estimation in Sensor Networks with Random Matrices, Time-Correlated Noises, Deception Attacks and Packet Losses. Sensors 2022;22:8505. https://doi.org/10.3390/s22218505.

Caballero-Águila R, Linares-Pérez J. Distributed fusion filtering for uncertain systems with coupled noises, random delays and packet loss prediction compensation. Int J Syst Sci 2023a; 54(2):371390. https://doi.org/10.1080/00207721.2022.2122905

Caballero-Águila R, Linares-Pérez J. Quadratic estimation for stochastic systems in the presence of random parameter matrices, time-correlated additive noise and deception attacks. J Frankl Inst 2023b;360:11141-11164. https://doi.org/10.1016/j.jfranklin.2023.08.033.

Cheng G, Ma M, Tan L, Song S. Gaussian estimation for non-linear stochastic uncertain systems with time-correlated additive noises and packet dropout compensations. IET Control Theory Appl 2022;16:600-614.http://dx.doi.org/10.1049/cth2.12252

García-Ligero, MJ, Hermoso-Carazo, A, Linares-Pérez, J. Least-squares estimators for systems with stochastic sensor gain degradation, correlated measurement noises and delays in transmission modelled by Markov chains. Int J Syst Sci 2020; 51(4):731-745. https://doi.org/10.1080/00207721.2020.1737757

Han F, Dong H, Wang Z, Li G. Local design of distributed $\mathrm{H}_{\infty}$-consensus filtering over sensor networks under multiplicative noises and deception attacks. Int J Robust Nonlinear Control 2019;29:22962314. https://doi.org/10.1002/rnc. 4493.

Han F, Song Y, Zhang S, Li W. Local condition-based finite-horizon distributed $\mathrm{H}_{\infty}$-consensus filtering for random parameter system with event-triggering protocols. Neurocomputing 2017;219:221-231. https://doi.org/10.1016/j.neucom.2016.09.022.

Hu J, Hu Z, Caballero-Águila R, Chen C, Fan S, Yi X. Distributed resilient fusion filtering for nonlinear systems with multiple missing measurements via dynamic event-triggered mechanism. Inf Sci 2023a;637:118950. https://doi.org/10.1016/j.ins.2023.118950.

Hu Z, Hu J, Yang G. A survey on distributed filtering, estimation and fusion for nonlinear systems with communication constraints: new advances and prospects. Syst Sci Control Eng 2020;8(1):189-205. https://doi.org/10.1080/21642583.2020.1737846.

Hu J, Wang C, Caballero-Águila R, Liu H. Distributed optimal fusion filtering for singular systems with random transmission delays and packet dropout compensations. Commun Nonlinear Sci Numer Simul 2023b;119:107093. https://doi.org/10.1016/j.cnsns.2023.107093.

Hu J, Wang Z, Gao H. Nonlinear Stochastic Systems with Network-Induced Phenomena: Recursive Filtering and Sliding-Mode Design. Springer, 2015. http://dx.doi.org/10.1007/978-3-319-08711-5.

Krantz S, Parks HR. A Primer of Real Analytic Functions, 2nd ed., Birkhäuser, Boston, 2002.

Liu W. Optimal estimation for discrete-time linear systems in the presence of multiplicative and time-correlated additive measurement noises. IEEE Trans Signal Process 2015;63(17):4583-4593. https://doi.org/10.1109/TSP.2015.2447491.

Liu W, Shi P. Convergence of optimal linear estimator with multiplicative and timecorrelated additive measurement noises. IEEE Trans Autom Control 2019;64(5):2190-2197. https://doi.org/10.1109/TAC.2018.2869467.

Ma J, Sun S. Optimal linear recursive estimators for stochastic uncertain systems with timecorrelated additive noises and packet dropout compensations. Signal Process 2020;176:107704. http://dx.doi.org/10.1016/j.sigpro.2020.107704

Ma Y, Sun S. Distributed Optimal and Self-Tuning Filters Based on Compressed Data for Networked Stochastic Uncertain Systems with Deception Attacks. Sensors 2023;23:335. https://doi.org/10.3390/s23010335.

Ma L, Wang M. State estimation of nonlinear time-varying complex networks with time-varying sensor delay for unknown noise distributions. Commun Nonlinear Sci Numer Simul 2022;114:106594. https://doi.org/10.1016/j.cnsns.2022.106594.

Ma L, Wang Z, Chen Y, Yi X. Probability-guaranteed distributed secure estimation for nonlinear systems over sensor networks under deception attacks on innovations. IEEE Trans Signal Inf Proc Netw 2021;7:465-477. https://doi.org/10.1109/TSIPN.2021.3097217.

Mahmoud MS, Hamdan MM, Baroudi UA. Modeling and control of Cyber-Physical Systems subject to cyber attacks: A survey of recent advances and challenges. Neurocomputing 2019;338:101-115. https://doi.org/10.1016/j.neucom. 2019.01 .099\).

Pang C, Sun S. Fusion Predictors for Multisensor Stochastic Uncertain Systems With Missing Measurements and Unknown Measurement Disturbances. IEEE Sens J 2015;15(8):4346-4354. https://doi.org/10.1109/JSEN.2015.2416511.

Qu F, Tian E, Zhao X. Chance-Constrained $H_{\infty}$ State Estimation for Recursive Neural Networks Under Deception Attacks and Energy Constraints: The Finite-Horizon Case. IEEE Trans Neural Netw Learn Syst 2023;34(9):6492-6503. https://doi.org/10.1109/TNNLS.2021.3137426.

Ran C, Deng Z. Robust fusion Kalman estimators for networked mixed uncertain systems with random one-step measurement delays, missing measurements, multiplicative noises and uncertain noise variances. Inf Sci 2020;534:27-52. https://doi.org/10.1016/j.ins.2020.04.044.

Sánchez HS, Rotondo D, Escobet T, Puig V, Quevedo J. Bibliographical review on cyber attacks from a control oriented perspective. Annu Rev Control 2019;48:103-128. https://doi.org/10.1016/j.arcontrol.2019.08.002.

Simon D. Optimal state estimation. John Wiley \& Sons, Inc., Hoboken, New Jersey, 2006.

Wang Z, Wang D, Shen B, Alsaadi FE. Centralized security-guaranteed filtering in multirate-sensor fusion under deception attacks. J Frankl Inst 2018;355:406-420. https://doi.org/10.1016/j.jfranklin.2017.11.010.

Wen T, Wen C, Roberts C, Cai B. Distributed filtering for a class of discretetime systems over wireless sensor networks. J Frankl Inst 2020;357:3038-3055. https://doi.org/10.1016/j.jfranklin.2020.02.005.

Xiao S, Han Q, Ge X, Zhang Y. Secure distributed finite-time filtering for positive systems over sensor networks under deception attacks. IEEE Trans Cybern 2020;50:1200-1228. https://doi.org/10.1109/tcyb.2019.2900478.

Yang W, Zhang Y, Chen G, Yang C, Shi L. Distributed filtering under false data injection attacks. Automatica 2019;102:34-44. https://doi.org/10.1016/j.automatica.2018.12.027.



Figure 1.



Figure 2.



Figure 3.

## Figure captions

Figure 1. $\operatorname{RMSE}_{k}$ for the filtering and smoothing estimates, when $\bar{\gamma}=0.7$ and $\bar{\lambda}=0.3$.

Figure 2. Means of $\operatorname{RMSE}_{k}$ for the filtering and smoothing estimates versus $\bar{\lambda}$, when $\bar{\gamma}=0.7$ and 0.9 .

Figure 3. Means of $\operatorname{RMSE}_{k}$ for the filtering and smoothing estimates versus $\bar{\gamma}$, when $\bar{\lambda}=0.1$ and 0.3 .


[^0]:    This is an original manuscript of an article published by Taylor \& Francis in INTERNATIONAL JOURNAL OF SYSTEMS

