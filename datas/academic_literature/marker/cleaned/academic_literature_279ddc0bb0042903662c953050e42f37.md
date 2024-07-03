# Longitudinal Targeted Minimum Loss-Based Estimation With Temporal-Difference Heterogeneous Transformer Toru Shirakawa 1 2 Yi Li 2 Yulun Wu 2 Sky Qiu 2 **Yuxuan Li** 2 Mingduo Zhao 2 **Hiroyasu Iso** 1 3 **Mark Van Der Laan** 2

## Abstract

We propose Deep Longitudinal Targeted Minimum Loss-based Estimation (Deep LTMLE), a novel approach to estimate the counterfactual mean of outcome under dynamic treatment policies in longitudinal problem settings. Our approach utilizes a transformer architecture with heterogeneous type embedding trained using temporal-difference learning. After obtaining an initial estimate using the transformer, following the targeted minimum loss-based likelihood estimation (TMLE) framework, we statistically corrected for the bias commonly associated with machine learning algorithms. Furthermore, our method also facilitates statistical inference by enabling the provision of 95% confidence intervals grounded in asymptotic statistical theory. Simulation results demonstrate our method's superior performance over existing approaches, particularly in complex, long time-horizon scenarios. It remains effective in small-sample, short-duration contexts, matching the performance of asymptotically efficient estimators. To demonstrate our method in practice, we applied our method to estimate counterfactual mean outcomes for standard versus intensive blood pressure management strategies in a real-world cardiovascular epidemiology cohort study.

## 1. Introduction

In the fields of medicine and public health, researchers frequently encounter data that are both high-dimensional and longitudinal. The outcomes of interest in these settings often involve time to the incidence of some failure event, such as total mortality (van der Laan & Robins, 2003; Salerno &
1Osaka University Graduate School of Medicine, Suita, Japan 2Univerity of California, Berkeley, United States 3National Center for Global Health and Medicine, Tokyo, Japan. Correspondence to: Toru Shirakawa <shirakawa@pbhel.med.osaka-u.ac.jp>.

Li, 2023). Estimating the counterfactual probability of the event is challenging in high-dimensional longitudinal settings. Existing methods suffer computationally due to lack of scalability and have worse performance due to curse-ofdimensionality (Wyss et al., 2022). In response, we propose an estimator that is computationally scalable and simultaneously allows for robust statistical inference. Our estimator incorporates a transformer architecture for estimating the target estimand, defined as the cumulative incidence probability under dynamic interventions, where the treatment sequence depends on patients' evolving histories. The target estimand can be identified through the g-formula contingent upon suitable assumptions (Robins, 1986). However, the target functional involves integration over potentially highdimensional time-dependent covariates across time-horizon, posing computational challenges. Our method advances the longitudinal targeted minimum loss-based estimation
(LTMLE) framework (van der Laan & Gruber, 2012; Lendle et al., 2017) by leveraging the computational capabilities of the transformer, facilitating the estimation of the target estimand and relevant nuisance parameters.

A number of estimators for the target estimand were proposed since the pioneering work by Robins (Robins, 1986). These estimators first factor the target parameter as a functional of nuisance parameters given a structural assumption on the underlying variables. Then, a common strategy to construct an estimator is plug-in, where one estimate the nuisance components with some models and then plug them into the target functional. However, since the naive plugin of the estimated nuisance components causes bias, several methods have been proposed to remove this bias using the first variation of the target functional called influence function. Examples of such de-biasing techniques include one-step estimators (Klaassen, 1987; Bickel et al., 1993),
estimating equations (Robins et al., 1994; Chernozhukov et al., 2022), and targeted minimum loss-based estimation
(TMLE) (van der Laan & Rose, 2011). Notably, due to its plug-in property, TMLE stands out because it will respect any conditional bounds on the outcome or global bounds on the statistical model, resulting in improved finite-sample performance (Gruber & van der Laan, 2012).

The first-order bias of the plug-in estimator is represented as a population mean of the influence function evaluated at the estimated nuisance distribution. Bias correction is performed by solving the empirical analogue of this term.

TMLE solves this term by optimizing a loss function along a submodel starting from the initial nuisance estimate (Bang & Robins, 2005; van der Laan & Rubin, 2006; van der Laan &
Rose, 2011). The loss function and the submodel are chosen so that the linear span of the derivative of the loss function along the submodel contains the efficient influence function, the influence function with minimal variance. Targeting is the term that refers to this correction by fluctuating of the initial estimate along the path.

The current LTMLE, a TMLE developed in the context of longitudinal data, relies on a sequential regression representation of the target estimand (Bang & Robins, 2005). An ensemble machine learning technique called *super learner* is then used to estimate the nuisance components of the data-generating distribution (van der Laan et al., 2007). In real-world complex longitudinal data, these nuisance components, such as the survival probability at a given time, may depend on all past histories. Therefore, the Markovian property, which states that future variable values only depends on the present variables, independent of the past, is not guaranteed to hold. In other words, every observed variable could depend on the past variables in the time ordering.

Hence, we want our model for the nuisance components to be able to take variable length of history as input. Under the targeted learning framework, we introduce a transformer architecture tailored towards our longitudinal setting and propose a novel method for the bias correction using a single fluctuation parameter across all time-points.

Our contribution includes: 1) Developed a general method that uses a transformer architecture to facilitate valid statistical inference in longitudinal settings concerning survival outcomes under dynamic interventions; 2) Proposed a method for bias correction using one-dimensional fluctuation for any length of time-horizon; 3) Demonstrated competetive statistical performance with asymptotically efficient estimators in simple and low-dimensional settings and superior statistical and computational performances in more complex settings; and 4) Applied our method to a real-world medical data with results presented in a format that aligns with clinical research guidelines.

## 2. Related Work

In the data science literature, several methods were proposed that predict the counterfactual outcomes from patient history.

The methods include G-Net (Li et al., 2021), counterfactual recurrent network (CRN) (Bica et al., 2020), and causal transformer (CT) (Melnychuk et al., 2022). However, their target parameters do not involve survival outcomes, and their methods are optimized for the mean squared error (MSE) of the individual predictions, rather than for making statistical inferences. DeepACE (Frauen et al., 2023) is closely related to the present study which uses deep neural networks to estimate the whole propensity scores and outcome regressions simultaneously. Furthermore, it has an additional layer for targeting implementing the one-dimensional submodel proposed by van der Laan (van der Laan & Rose, 2018). Our method differs from theirs in the following three aspects.

First, DeepACE incorporates the targeting step within their loss function, which requires an additional hyperparameter. However, there is a lack of justification for the chosen value of this hyperparameter and guidance on its tuning in practical applications. Our approach, in contrast, separates the targeting step, aligning more closely with the TMLE literature. Second, DeepACE does not address survival outcomes, specifically failing to consider the process degeneracy following a patient's event occurrence. Third, while DeepACE utilizes the long short-term memory (LSTM) architecture, our method employs transformers. Transformers are superior in capturing long-term dependencies and offer greater computational efficiency during training than LSTM.

Moreover, DeepACE does not provide uncertainty measures, such as confidence intervals, limiting its utility for statistical inference. Our problem of estimating mean of counterfactual outcomes from longitudinal observational data under dynamic interventions has been extensively investigated as an off-policy evaluation problem in the bandit algorithm and reinforcement learning literature (Levine et al., 2020). Methods of bias correction after plugging in the initial estimate with influence function were also introduced in this context (Jiang
& Li, 2016; Farajtabar et al., 2018; Narita et al., 2021).

However, they did not provide tools for inference. Double reinforcement learning (Kallus & Uehara, 2020) utilized the efficient influence functions in the spirit of double machine learning (Chernozhukov et al., 2018), which is a closed form of a more general debiased estimating equation framework
(Chernozhukov et al., 2022), to correct plug-in bias and proved efficiency. TMLE deform the distribution itself to correct bias before plugged-in to the the target functional, thereby the values are contained the domain of the functional.

## 3. Problem Formulation

In this section, follwing the roadmap of causal inference
(Petersen & van der Laan, 2014; van der Laan & Rose, 2018; Dang et al., 2023), we first describe the experiment that generated the observed data and the statistical model that contains the data-generating distribution. Next, we define our causal target parameter. Then, we discuss assumptions needed to identify our target parameter from the observed data. Finally, we describe the idea of statistical method for constructing estimator and correcting bias.

## 3.1. Data

We consider the general longitudinal setting involving repeated measurements of a set of variables for a group of n patients over a period of time. In particular, our observed data contains n independent and identically distributed copies of random vector O = (W0 = W, L1, A1, Y1, . . . , LT , AT , YT = Y ) (1)
with baseline covariates W, time-dependent covariates Lt, treatments At, and outcome Yt. We use P0 to denote the true probability distribution of O that generated the data, and P0 is in some statistical model M. Stopping time T is a random variable (e.g. time of death in the case of survival analysis) and we use τ to denote the maximum time. We make the remark that in real-world data, patients are often subject to censoring. For a formulation of the data structure involving censoring nodes, see Appendix H.

## 3.2. Target Parameter

To define the target parameter, we introduce a structural causal model (SCM). In brief, SCM assumes each observed random variable X is generated from the parent nodes pa(X) and the external noise UX by a production function fX as X = fX(pa(X), UX). By abusing notation, we also denote the induced probability measure of X by the same symbol fX. See Appendix C.1 for details.

Our target parameter is the counterfactual mean of the final outcome Y under a user-specified dynamic treatment policy g = [gt]
τ t=1 where gt is a probability measure on the treatment space conditioned on the whole history, pa(At) = (L1:t, A1:t−1, Y1:t−1) up until At (not including At). Specifically, our target parameter is given by

$$\psi(P)=\mathbb{E}Y^{g},$$
g, (2)
which is the mean of the counterfactual outcome produced by replacing π, defined as the observed treatment policy from the data, with g in the structural causal model.

Identification Under the positivity assumption:

$$g\ll\pi,$$
g ≪ π, (3)
and the sequential randomization assumption:

$$Y^{g}\perp A_{t}\mid p a(A_{t})\;\mathrm{for}\;t=1,\ldots,\tau,$$

we can identify our target causal parameter through gformula as the mean of Y under the counterfactual distribution which is given by replacing distributions π with g
(Robins, 1986):
$$\mathbb{E}Y^{g}=\mathbb{E}_{g}Y.$$
g = EgY. (5)
Note that the consistency assumption Y = Y
π, usually stated in causal inference literature, is a consequence of the definition of counterfactual outcome in our SCM. Now the problem is reduced to the estimation of the statistical parameter:
ψ(P) = EgY. (6)

## 3.3. Targeted Minimum Loss-Based Estimation

, $Y_T=Y$). 
Given we have an estimator Pˆn of the data-generating distribution P0, a natural estimator of the target functional is the plug-in estimator ψˆn = ψ(Pˆn). Under a regularity condition, ψ admits the following first-order expansion

$$\psi(\hat{P}_{n})-\psi(P_{0})=-\int_{\cal O}D^{\star}(\hat{P}_{n})d P_{0}+R_{2}(\hat{P}_{n},P_{0}),\tag{7}$$

where D⋆is the efficient influence function of ψ, and R2(Pˆn, P0) is the exact remainder. Influence functions quantifies the amount of changes of an estimator under small perturbations of the sample. The efficient influence function is the influence function with minimal variance. The idea of TMLE is to eliminate the empirical analogue of the first term of the right hand side by fluctuating Pˆn to find a distribution Pˆ⋆
n with PnD⋆(Pˆ⋆
n
) = 0, where P f =R*f dP* is a shorthand for the expectation of a measurable function f with respect to a probability measure P. Our problem is to obtain an initial estimate Pˆn with a potentially large scale and high dimensional longitudinal data, and correct bias of the plug-in estimator ψ(Pˆn) by fluctuating Pˆn.

## 4. Proposed Method

In this section, we describe our proposed method, Deep Longitudinal Targeted Minimum Loss-based Estimation
(Deep LTMLE). Let

$$Q_{t}^{g}(p a(Y_{t}))=\mathbb{E}_{g}[Y_{T}\mid L_{1:t},A_{1:t},Y_{1:t-1}]$$

be the mean outcome at stopping time T given the history before node Yt for t = 1*, . . . , τ* , where future treatments At+1*, . . . , A*T follow a counterfactual treatment assignment policy g. Similarly,

$$V_{t}^{g}(p a(A_{t}))=\mathbb{E}_{g}[Y_{T}\mid L_{1:t},A_{1:t-1},Y_{1:t-1}]$$
$$({\mathfrak{I}})$$

is the mean outcome at stopping time T given the history before node At, for t = 1*, . . . , τ* . We abbreviate Q
g tfor Q
g t
(pa(Yt)) if it is clear from the context, similarly for V
g t
.

Our goal is to estimate ψ(P) by

$\eqref{eq:walpha}$. 
$$\hat{\psi}_{n}^{\star}=P_{n}\hat{V}_{1,\epsilon^{\star}}^{g}(pa(A_{1}))\tag{10}$$ $$=P_{n}\mathbb{E}_{A_{1}\sim g_{1}(pa(A_{1}))}[\hat{Q}_{1,\epsilon^{\star}}^{g}(pa(A_{1}),A_{1})]$$  where $\hat{Q}_{1,\epsilon^{\star}}^{g}$ is an estimation of $Q_{1}^{g}$ such that $\hat{\psi}_{n}^{\star}$ is asympt 
1
is asymptotically efficient. We achieve this by proposing a temporal-
Algorithm 1 Temporal Difference Learning of Conditional Counterfactual Mean Outcomes 1: for b = 1 to B do 2: QˆgT
(pa(YT )) ← QˆgT
(pa(YT )) − α · ∂ QˆgT
(pa(YT ))L(QˆgT
(pa(YT )), YT )
3: GˆT ← GˆT − α · ∂ GˆT (pa(AT ))L(GˆT (pa(AT )), AT )
4: for t = T − 1 to 1 do 5: Vˆ g t+1(pa(At+1)) ← EAt+1∼gt+1(pa(At+1))-Qˆg t+1(pa(At+1), At+1)
6: Qˆg t
(pa(Yt)) ← Qˆg t
(pa(Yt)) − α · ∂Qˆg t
(pa(Yt))L(Qˆg t
(pa(Yt)), Vˆ g t+1(pa(At+1)))
7: Gˆt ← Gˆt − α · ∂ Gˆt(pa(At))L(Gˆt(pa(At)), At)
8: **end for** 9: **end for**
10: Output (Qˆg t
, Vˆ g t
, Gˆt)
T
t=1
difference heterogeneous transformer to yield an initial estimation Qˆg1
, then update this estimation to get Qˆg1,ε⋆ via Targeted Minimum Loss-based Estimation (TMLE).

losses. See Algorithm 1 for the optimization workflow.

Convergence of the algorithm can be found in Appendix D.

## 4.1. Temporal-Difference Heterogeneous Transformer

To learn the initial model Vˆ g 1
, we use temporal-difference loss as the objective to learn underlying models Qˆg tfor t = 1*, . . . , τ* via stochastic gradient descent (SGD). The principle of temporal difference learning (Sutton, 1988; Mnih et al., 2013) is to supervise Qˆg tto obey the temporal equality of Q
g t
:

$$Q_{t}^{g}=\mathbb{E}_{p(Y_{t},L_{t+1}|pa(Y_{t}))}V_{t+1}^{g}$$ $$=\mathbb{E}_{p(Y_{t},L_{t+1}|pa(Y_{t}))},g_{t+1}(pa(A_{t+1}))Q_{t+1}^{g}\tag{11}$$  for $t=1,\ldots,\tau-1$ and $Q_{\tau}^{g}=\mathbb{E}_{p(Y_{\tau}|pa(Y_{\tau}))}Y_{\tau}$.  
4
The temporal difference loss on a sample trajectory is thus given by L
Q
t = L(Qˆg t
, Vˆ g t+1) for t = 1*, . . . , T* − 1, where Vˆ g t+1(pa(At+1)) =
EAt+1∼gt+1(pa(At+1))-Qˆg t+1(pa(At+1), At+1)can be computed by Monte-Carlo estimation if A is continuous, and L
Q
T = L(QˆgT
, YT ). In the case of survival analysis, the components for t = 1*, . . . , τ* − 1 are defined as L
Q
t = Lbce(Qˆg t
, Vˆ g t+1), where Lbce(ˆ*y, y*) = −-y log ˆy + (1 − y) log(1 − yˆ)is the binary cross entropy loss. To yield the updated model Qˆg t,ε, we need to adjust Qˆg tafter model training factoring in the estimating model Gˆt for the propensity score

$$G_{t}(p a(A_{t}))=\mathbb{P}[A_{T}=1\mid L_{1:t},A_{1:t-1},Y_{1:t-1}],$$

which we will describe in detail in the next section. Hence, the loss function also needs to include L
G
t = L(Gˆt, At) and is thus given by

$${\mathcal{L}}=\sum_{t=1}^{\tau}\mathbb{1}\left\{t\leq T\right\}{\mathcal{L}}_{t}=\sum_{t=1}^{T}{\mathcal{L}}_{t}=\sum_{t=1}^{T}{\mathcal{L}}_{t}^{Q}+\alpha{\mathcal{L}}_{t}^{G}\tag{13}$$

where α is a hyperparameter that controls the weights of For the estimation of Q
g tand Gt, we propose a unified model architecture to simultaneously optimize deep neural networks Qˆg t and Gˆt in an efficient, non-sequential manner by adapting a decoder-only Transformer (Vaswani et al.,
2017; Brown et al., 2020) to longitudinal data with heterogeneous tokens. An overview of the model architecture is given in Figure 1. For each sampled sequence in the training set, we feed each token in the sequence to a linear embedding layer according to its variable type. In the case of Figure 1, there are four different embedding layers eW , eL, eA, and eY . Each embedding layer has the same number of output dimensions. Then, each embedding is integrated with its positional encoding E0*, . . . , E*τ and type encoding EW , EL, EA, and EY that represent its timestamp and variable type information through an aggregation function (e.g. sum, concat):

$$E(\bullet_{t})=\operatorname{aggr}\left\{e_{\bullet}(\bullet_{t}),\,E_{\bullet},\,E_{t}\right\}$$
$\mathbf{v}$ 4. 
for •t ∈ (W0, L1, A1, Y1, . . . , Lτ , Aτ , Yτ ) where we used concat as aggr in the experiments in this work. Note that we include type embedding E• because e• need not necessarily be type-specific linear layers. For more efficient and parallelizable embedding operation, we can pad each variable to the same number of dimensions before feeding into the same embedding layer e• = e. Then, the embedded sequence is fed into the transformer and produce Gˆ and Qˆgthrough output heads fG and fQ at each position that corresponds to token type L and A respectively:

$\hat{G}_{t}=f_{G}(\text{transformer}\left\{E(W_{0}),\ldots,E(L_{t})\right\})$  $\hat{G}_{t}^{g}=f_{Q}(\text{transformer}\left\{E(W_{0}),\ldots,E(A_{t})\right\})$.  
$$\begin{array}{l}{(15)}\\ {(16)}\end{array}$$
In practice, we can use a joint output layer f for fG and fQ for more efficient and parallelizable output generation, where the output number of dimensions is the sum of the number of dimensions dim(A) for treatment A and dim(Y ) for outcome Y . Then, we compute softmax probabilities



masking out the last dim(Y ) dimensions for Gˆt and first dim(A) dimensions for Qˆg t
.

Our proposed architecture does not entail concatenation of variables at the same timestamp or sequential decoding of outputs following the transformer embedding block like prior work Melnychuk et al. (2022), which 1) allows us to handle different types of and different number of variables at different timestamps (e.g. starting from W0, ending at L8, while A3 and Y3 are missing), and 2) is fully parallelizable when we use padding instead of learnable linear mapping for the embedding layer e• and use the joint output layer f.

## 4.2. Targeted Minimum Loss-Based Estimation

Efficient Influence Function Since our target parameter is the counterfactual mean outcome at the final τ , the relevant part of P0 of interest are Q
g t,0 for t = 1, 2*, ..., τ* .

Theorem 4.1. In our counterfactual mean case, the efficient influence function D⋆(P)(O) = D⋆({Q
g t
, Gt}
τ t=1)(O) is given by

$$D^{\star}(P)(O)=(V_{1}^{g}-\psi_{0})+\sum_{t=1}^{T}I_{t}(V_{t+1}^{g}-Q_{t}^{g})\quad\quad(17)$$
$$\&\;\mathrm{Grubber},\,2012).$$
where It =Qts=1 dgs/dπs and V g T +1 = YT .
  **Acknowledgments**  I would like to thank my supervisor, for his kind of support. I would like to thank my supervisor, for his kind of support.  
This is given in (van der Laan & Gruber, 2012).

4.2.1. TEMPORAL DIFFERENCE TARGETING
Submodel We update the initial estimate Qˆg tfor Q
g t,0 to Qˆg⋆
tsuch that PnD⋆({Qˆg⋆
t
, Gˆt}
τ t=1) = 0. We realize this by fluctuating Qˆg talong a one-dimensional submodel through the initial fit Qˆg = [Qˆg t
]
τ t=1 given by, Qˆg ε = [Qˆg t,ε]
τ t=1, where

$$\mbox{logit}\,\hat{Q}^{g}_{t,\varepsilon}=\mbox{logit}\,\hat{Q}^{g}_{t}+\varepsilon\tag{18}$$

with a common fluctuation parameter ε across t. If the outcome is survival, then we automatically have Yt ∈ [0, 1].

In a general longitudinal setting for bounded Yt's, we can re-scale both Yt and Qˆg tto [0, 1] and use the same onedimensional submodel. Partial Loss function We search for the optimal fluctuation ε
⋆ with respect to the partial loss function

$\mathcal{L}^{\star}(\hat{Q}^{g}_{\varepsilon},\hat{V}^{g}_{\varepsilon^{\prime}};\hat{G})=\sum_{t=1}^{T}I_{t}(\hat{G})\mathcal{L}_{\text{bce}}(\hat{Q}^{g}_{t,\varepsilon},\hat{V}^{g}_{t+1,\varepsilon^{\prime}}),$
$$(19)$$
$$\mathrm{h}\ \mathrm{that}$$

$$(20)$$
t+1,ε′ ), (19)
where $\hat{V}^{g}_{T+1,\varepsilon}=Y_{T}$ and $\hat{V}^{g}_{t,\varepsilon}=\mathbb{E}_{A_{t}\sim g_{t}}\left[\hat{Q}^{g}_{t,\varepsilon}\right]$, such that $\mathcal{L}^{\star}(\hat{Q}^{g}_{\varepsilon},\hat{V}^{g}_{\varepsilon})$ satisfies the following theorem:
  **Theorem 4.2**.: _For any $\varepsilon^{\star}$, we have_
$$\partial_{\varepsilon}|_{\varepsilon^{\star}}{\mathcal{L}}^{\star}(\hat{Q}_{\varepsilon}^{g},\hat{V}_{\varepsilon^{\star}}^{g})=D^{\star}(\hat{Q}_{\varepsilon^{\star}}^{g},\hat{G}).$$
⋆ , Gˆ). (20)
See Section B for the proof.  
Corollary 4.3. *Suppose that we found an* ε
⋆*satisfying*

$$\partial_{\varepsilon}|_{\varepsilon^{\star}}P_{n}{\mathcal{L}}^{\star}(\hat{Q}_{\varepsilon}^{g},\hat{V}_{\varepsilon^{\star}}^{g})=0,$$
$$f l u e n c e\,f u n c t i o n.$$
⋆ ) = 0, (21)
then Qˆg
$$n\;\hat{Q}_{\varepsilon}^{g}.\;s o l v e s\;t h e$$
⋆ *solves the efficient influence function.*
In practice, for the finite sample performance, we only need to solve it to the order of standard error with a σn/ log n factor (van der Laan & Rose, 2011) (Algorithm 2).

Algorithm 2 Temporal-Difference Targeting
1: ε ← 0
2: **repeat**
3: ε ← argminε
′PnL
⋆(Qˆg
$\begin{array}{l}\tau_{\mathrm{eff}}\\ \tau_{\mathrm{eff}}\end{array}$
′ , Vˆ g
ε
).

$$\tau_{2}(Q_{\varepsilon}^{2},G)$$
$\mathbf{a}\cdot\mathbf{b}$
4: σˆn ←
qn−1PnD⋆2(Qˆg ε, Gˆ)
5: **until** PnD⋆(Qˆg ε
, Gˆ) < σˆn/ log n 6: ψˆ⋆n ← PnVˆ g 1,ε(pa(A1))
7: 95% CI as ψˆ⋆n ± 1.96 · σˆn Convergence of Algorithm 2 The investigation of Lbce(Qˆg t,ε, Vˆ g t,ε)(O) for different t and O's as a function of ε suggests that they admit different bell curve shapes concentrating at different ε's and have different spread out levels. Thus, by summing up Lbce(Qˆg t,ε, Vˆ g t,ε)(O) across t and across O's as PnL
⋆(Qˆg ε
, Vˆ g ε
) as a function of ε will fluctuate a lot and we expect a local minima and local maxima around the neighborhood of ε = 0. And thus the convergence of the algorithm is highly probable and we don't discover any issue in our simulations.

Comparison to LTMLE In the LTMLE, we only need a good estimate of Qg τ and then do backward sequential regression and targeting as mentioned in (van der Laan &
Gruber, 2012). However, the problem is the error in the estimation of Qg τ can propagate as we progress back to get Q
g,∗ τ−1
, ..., Qg,∗
1. Nonetheless, after our initial transformer step, we have good initial estimates for all Q
g 1
, ..., Qg τ
. So, instead of only relying on a good estimate of Qg τ
, our algorithm makes uses of all of them. and doing targeting across t with o(ε) fluctuation at each t level. Thus, we are able to pool information across time when doing the targeting step.

## 4.2.2. Sequential Targeting

Alternatively, one could apply a sequential targeting procedure that is very similar to LTMLE but with given initials generated from the transformer step.

Submodel We fluctuate each component of the initial fit Qˆg = [Qˆg t
]
τ t=1 along a model as

$$\operatorname*{logit}\hat{Q}_{t,\varepsilon_{t}}^{g}=\operatorname*{logit}\hat{Q}_{t}^{g}+\varepsilon_{t}.$$
t + εt. (22)
$$(22)^{\frac{1}{2}}$$

Loss function Starting from t = τ , given we have found ε
⋆
t+1, among individuals whose *T > t* − 1, we search for empirical loss minimizer ε
⋆
t with respect to the loss function L
⋆ t as,

$$\mathcal{L}_{t}^{*}(\hat{Q}_{t,\varepsilon_{t}}^{g},\hat{V}_{t+1,\varepsilon_{t+1}^{*}}^{g})=I_{t}(\hat{G})\mathcal{L}_{\text{bce}}(\hat{Q}_{t,\varepsilon_{t}}^{g},\hat{V}_{t+1,\varepsilon_{t+1}^{*}}^{g}),\tag{23}$$

where Vˆ g t+1,ε⋆
t+1
= EAt+1∼gt+1 -Qˆg t+1,ε⋆
t+1 when *T > t* and Vˆ g t+1,ε⋆
t+1
= YT when T = t. To initialize, we set ε
⋆
τ+1 = 0.

Lemma 4.4. *Suppose that we found* ε
⋆ τ
, ...ε⋆
1 sequentially as mentioned above, then {Qˆg ε
⋆ t
}
τ t=1 *solves the efficient influence function.*

$$\mathbb{19}\,r_{0}$$

Algorithm 3 Sequential Targeting 1: ε
⋆
τ+1 ← 0 2: for t = τ to 1 do 3: ε
⋆
t ← argminεt Pn1(T ≥ t)L
⋆(Qˆg t,εt
, Vˆ g t+1,ε⋆
t+1
).

4: **end for**
5: ψˆ†n ← PnVˆ g 1,ε⋆
1
(pa(A1))
6: σˆn ←
qn−1PnD⋆2({Qˆg ε
⋆
t
}
τ t=1, Gˆ)
7: 95% CI as ψˆ†n ± 1.96 · σˆn Comparaison to LTMLE While the error can still propagate as we move back in time, the error propagates only through the targeting steps whereas in LTMLE the error can also propagate through regressions. At each time step t, LTMLE needs to first regress Vˆ g t+1,ε⋆
t+1 on pa(Yt) to get an estimate Qˆg tand then perform the targeting through the submodel in(22). However, we only use initial estimate Qˆg t from our transformer fit and it does not depend on ε
⋆
t+1*, . . . , ε*⋆
τ
.

Why not targeting through additional loss function As in DeepACE, the targeting can be performed through introducing additional loss components to further train the transformer we have build in the first step. This additional loss function will have its derivative equal to the efficient influence function. However, we find that the penalty factor before this loss function is hard to tune and in near all cases, it is hard to guarantee the EIF is solved and most of the time we will hurt our initial fits as shown in Appendix 5.1.

## 5. Experiments

We conducted two experiments. In the first experiment, we compare the bias, root-mean-squared-error (RMSE), and coverage probability, of our estimator with existing estimators based on 100 times of estimations for both continuous and survival outcomes. The second experiment is an application of our proposed method to a real-world data.



Table 1. Results from complex synthetic data. LTMLE (GLM): LTMLE with GLM; LTMLE (SL): LTMLE with super learner of GLM,

MARS, and XGBoost; Deep LTMLE: initial estimate with TDHT; Deep LTMLE †: TDHT with sequential targeting; Deep LTMLE ⋆:

TDHT with temporal-difference targeting.

Bias RMSE Coverage Mean σˆn

Model τ = 10 τ = 20 τ = 30 τ = 10 τ = 20 τ = 30 τ = 10 τ = 20 τ = 30 τ = 10 τ = 20 τ = 30

LTMLE (GLM) 0.0230 0.0766 0.1344 0.0265 0.0796 0.1381 1.00 1.00 1.00 0.43 0.69 0.76

LTMLE (SL) 0.0144 0.0297 0.0477 0.0185 0.0344 0.0545 1.00 1.00 1.00 0.31 0.40 0.45

DeepACE -0.0704 -0.1491 -0.2396 0.0948 0.1601 0.2453 1.00 1.00 1.00 0.74 0.69 0.57

Deep LTMLE 0.0182 0.0304 0.0499 0.0264 0.0342 0.0532 1.00 0.94 0.71 0.17 0.09 0.06 Deep LTMLE † 0.0158 0.0286 0.0548 0.0188 0.0314 0.0589 1.00 0.93 0.73 0.16 0.09 0.06 Deep LTMLE ⋆ 0.0143 0.0305 0.0471 0.0204 0.0333 0.0509 1.00 0.93 0.76 0.16 0.08 0.06

## 5.1. Synthetic Data With Continuous Outcome

First, we start our experiment with a very simple data generating process with continuous outcome, n = 500, and τ = 10. The data generating proccess is described in the Section F.1. After fitting DeepACE, we additionally performed our targeting precedures on the fit.

The results were shown in Figure 2. Initial fits of Deep LTMLE and DeepACE had comparable bias. Even with the targeting loss, DeepACE failed to solve the efficient influence function. On the other hand, due to the separation of the targeting step in our method, we managed to solve it completely and succeeded in correcting bias.

## 5.2. Synthetic Data With Survival Outcome

Next, we evaluated Deep LTMLE under a highly complex data-generating process with survival outcomes, fivedimensional time-dependent covariates, non-Markovian dependencies, n = 1000, and τ = 10, 20, 30, imitating the setups from previous studies (Bica et al., 2020; Frauen et al.,
2023). See Section F.3 for details.

Results are presented in Table 1. We observe that Deep LTMLE on average achieves a lower RMSE compared to other methods, particularly in scenarios with larger τ , indicating its robustness in complex and realistic scenarios without Markovian dependencies. Benefits by our targeting procedures are obvious for τ = 10, 20. For τ = 30, we still see reductions in bias and in RMSE when the temporaldifference targeting is applied. While Deep LTMLE's coverage probability diminished at τ = 30, the confidence intervals generated by LTMLE and DeepACE were notably over-conservative with large estimated standard errors.

The pronounced bias of DeepACE can likely be attributed to three factors. First, DeepACE's use of the squared-errorloss for the outcome is known to induce greater bias in sparse outcomes, a common scenario in survival analysis, as opposed to the logistic loss used in our approach (Gruber
& van der Laan, 2010). Second, DeepACE failed to solve the efficient influence function. Third, DeepACE does not account for the degeneration of the survival outcome.

## Simple Synthetic Data With Survival Outcome We Also

conducted an eperiment with a very simple survival synthetic data with one-dimensional time-dependent covariates, n = 1000, and τ = 10, 20, 30. Although LTMLE with GLM is expected to have strong performance in this experiment, Deep LTMLE remains highly competitive in this



| Table 2. Results from semi-synthetic data with unmeasured confounding Bias RMSE Coverage   | Mean σˆn   |         |         |        |        |        |        |        |        |        |        |        |
|--------------------------------------------------------------------------------------------|------------|---------|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Model                                                                                      | τ = 10     | τ = 20  | τ = 30  | τ = 10 | τ = 20 | τ = 30 | τ = 10 | τ = 20 | τ = 30 | τ = 10 | τ = 20 | τ = 30 |
| LTMLE (SL)                                                                                 | 0.0075     | 0.0341  | 0.0574  | 0.0138 | 0.0491 | 0.0786 | 0.70   | 0.45   | 0.25   | 0.09   | 0.12   | 0.14   |
| DeepACE                                                                                    | -0.0174    | -0.0434 | -0.0770 | 0.0788 | 0.1154 | 0.1341 | 1.00   | 1.00   | 1.00   | 0.67   | 0.78   | 0.86   |
| Deep LTMLE                                                                                 | -0.0002    | 0.0108  | 0.0041  | 0.0162 | 0.0720 | 0.0772 | 1.00   | 0.95   | 1.00   | 0.18   | 0.27   | 0.32   |
| Deep LTMLE ⋆                                                                               | 0.0058     | 0.0429  | 0.0709  | 0.0205 | 0.0724 | 0.0968 | 0.95   | 0.90   | 0.95   | 0.18   | 0.26   | 0.31   |

context, equalling LTMLE's performance (Section G).

## 5.3. Semi-Synthetic Data

To evaluate the performance of the proposed methods, we generated realistic data from Circulatory Risk in Communities Study (CIRCS) (Yamagishi et al., 2019), a long-term on-going cardiovascular epidemiological cohort study, lasting over a half century. See Section G.1 for the detail.

Table 2 shows the results with semi-synthetic data with unmeasured confounding, which reflects a real world setting.

Deep LTMLE performed best in terms of bias for all time horizons. Furthermore, as the time horizon increases from 10 to 30, LTMLE's coverage probability drops as low as 0.3. On the other hand, Deep LTMLE has nominal coverage even in the longest time-horizon setting.

## 5.4. Real World Data

We applied Deep LTMLE to real world data from CIRCS.

We estimated the counterfactual mean outcomes under the standard blood pressure (SBP) management strategy that controls SBP less than 140 mmHg and the intensive blood pressure management strategy with SBP less than 120 mmHg after the 30 years of sustained management.

In real world applications, we often encounter with practical problems of censoring, that is loss of follow-up for some reasons. Our model can be easily generalized to cover this setting with a slight modification by adding censoring nodes.

Details are described in Section H of Appendix.

The results were shown in Figure 3. The average treatment effect (ATE) of the intensive management strategy over the standard management strategy first increased with a peak at 20 years after baseline and then decreased with a fluctuation.

The direction and trend of ATE is consistent with the difference of empirical means of cumulative outcomes between two groups followed the two strategies.

## 5.5. Computation Details

DeepACE and Deep LTMLE were run on a GPU (Tesla T4) with 16 GB memory and LTMLE on CPU (Intel Xeon Skylake 6230 @ 2.1 GHz) with 40 cores and 96 GB memory. We used the R package ltmle with GLM and a super learner (SL) library consisting of GLM, maltivariate adaptive regression spline with earth package, and xgboost for the simple synthetic data and the real world data (Lendle et al., 2017; Polley et al., 2021; Milborrow, 2023; Chen et al.,
2022). Confidence intervals for LTMLE was constructed based on its estimate of the efficient influence function.

| Table 3. Running time with complex synthetic data Time, sec Model τ = 10 τ = 20 τ = 30 LTMLE (SL) 271 958 2122 DeepACE 53 54 133 Deep LTMLE ⋆ 38 39 116   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

As shown in Table 3, Deep LTMLE leverages GPU acceleration to achieve significantly faster processing times than LTMLE, presenting a substantial computational benefit for analyses involving extensive time horizons and highdimensional time-dependent covariates.

## 6. Limitations

Our method assumes the sequential randomization and the positivity assumption on the intervention mechanism to identify the counterfactual outcome from observational data.

However, to our surprise, in semi-synthetic data simulations, we found that when there is unmeasured confounding violating the sequential randomization assumption rely on, our method is very robust and could even provide robust inference. Furthermore, our proposed model does not currently address several complexities often found in real-world data, such as visiting processes, competing risks, and continuous time horizons. These challenges will be the focus of our future research efforts.

## 7. Conclusion

In this paper, we propose a variant of LTMLE that leverages the sequential learning capabilities of transformers. This approach enables simultaneous fitting of the entire LTMLE,
allowing us to target the mean survival under dynamic interventions directly through weighting the loss function with cumulative inverse probabilities of intervention. The proposed method performs competitively with asymptotically efficient estimators in low-dimensional settings and exceeds the performance of existing models in high-dimensional scenarios. Scalability of our model to larger and longer datasets was implied. We applied our method to real world data and demonstrated a causal inference on the effect of sustained blood pressure management strategies on total mortality.

## Acknowledgement

This research is funded by NIH and Berkeley School of Public Health, Interdisciplinary Collaborative Research Grant.

TS is supported by Fulbright scholarship program. The authors thank Dr. Ahmed Alaa at University of California, San Francisco and Berkeley for valuable discussions. The authors acknowledge the CIRCS investigators team for providing the real world data for experiments; Dr. Akihiko Kitamura at Yao City, Dr. Masahiko Kiyama at Osaka Center for Prevention of Cardiovascular Diseases, Dr. Takeo Okada at Osaka Center for Prevention of Cardiovascular Diseases, Dr. Yuji Shimizu at Osaka Center for Prevention of Cardiovascular Diseases, Dr. Hironori Imano at Kinki University, Dr. Tetsuya Ohira at Fukushima Prefeture Medical University, Dr. Kazumasa Yamagishi at Tsukuba University, and Dr. Isao Muraki at Osaka University.

## References

Bang, H. and Robins, J. M. Doubly robust estimation in missing data and causal inference models. *Biometrics*, 61
(4):962–973, 2005.

Bica, I., Alaa, A. M., Jordon, J., and van der Schaar, M.

Estimating counterfactual treatment outcomes over time through adversarially balanced representations. In *International Conference on Learning Representations*, 2020.

9 Bickel, P., Klaassen, C., Ritov, Y., and Wellner, J. *Efficient and Adaptive Estimation for Semiparametric Models*. Johns Hopkins Series in the Mathematical Sciences.

Springer New York, 1993. ISBN 978-0-387-98473-5.

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D.,
Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
Askell, A., et al. Language models are few-shot learners.

Advances in neural information processing systems, 33:
1877–1901, 2020.

Chen, T., He, T., Benesty, M., Khotilovich, V., Tang, Y., Cho, H., Chen, K., Mitchell, R., Cano, I., Zhou, T., Li, M., Xie, J., Lin, M., Geng, Y., Li, Y., and Yuan, J. *xgboost: Extreme Gradient Boosting*, 2022. URL https://CRAN.

R-project.org/package=xgboost. R package version 1.7.6.1.

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E.,
Hansen, C., Newey, W., and Robins, J. Double/debiased machine learning for treatment and structural parameters.

The Econometrics Journal, 21(1):C1–C68, 2018.

Chernozhukov, V., Escanciano, J. C., Ichimura, H., Newey, W. K., and Robins, J. M. Locally robust semiparametric estimation. *Econometrica*, 90(4):1501–1535, 2022.

Dang, L. E., Gruber, S., Lee, H., Dahabreh, I. J., Stuart, E. A., Williamson, B. D., Wyss, R., D´ıaz, I., Ghosh, D.,
Kıcıman, E., Alemayehu, D., Hoffman, K. L., Vossen, C. Y., Huml, R. A., Ravn, H., Kvist, K., Pratley, R., Shih, M.-C., Pennello, G., Martin, D., Waddy, S. P., Barr, C. E.,
Akacha, M., Buse, J. B., van der Laan, M., and Petersen, M. A causal roadmap for generating high-quality realworld evidence. Journal of Clinical and Translational Science, 7(1):e212, 2023.
Farajtabar, M., Chow, Y., and Ghavamzadeh, M. More robust doubly robust off-policy evaluation. In Proceedings of the 35th International Conference on Machine Learning, volume 80 of *Proceedings of Machine Learning Research*, pp. 1447–1456. PMLR, 10–15 Jul 2018.

Frauen, D., Hatt, T., Melnychuk, V., and Feuerriegel, S.

Estimating average causal effects from patient trajectories. *Proceedings of the AAAI Conference on Artificial* Intelligence, 37(6):7586–7594, 2023.

Gruber, S. and van der Laan, M. J. A targeted maximum likelihood estimator of a causal effect on a bounded continuous outcome. *The International Journal of Biostatistics*, 6(1):Article 26, 2010. ISSN 1557-4679. doi:
10.2202/1557-4679.1260.
Gruber, S. and van der Laan, M. J. Targeted minimum loss based estimation of a causal effect on an outcome with known conditional bounds. *The international journal of* biostatistics, 8(1):21–21, 2012. ISSN 1557-4679.

Jiang, N. and Li, L. Doubly robust off-policy value evaluation for reinforcement learning. In Proceedings of The 33rd International Conference on Machine Learning, volume 48 of *Proceedings of Machine Learning Research*,
pp. 652–661, New York, New York, USA, 20–22 Jun 2016. PMLR.

Kallus, N. and Uehara, M. Double reinforcement learning for efficient and robust off-policy evaluation. In Proceedings of the 37th International Conference on Machine Learning, volume 119 of *Proceedings of Machine Learning Research*, pp. 5078–5088. PMLR, 13–18 Jul 2020.

Kennedy, E. H. Semiparametric doubly robust targeted double machine learning: A review. *arXiv preprint* arXiv:2203.06469, 2022.

Klaassen, C. A. J. Consistent estimation of the influence function of locally asymptotically linear estimators. The Annals of Statistics, 15(4):1548–1562, 1987.

Lendle, S. D., Schwab, J., Petersen, M. L., and van der Laan, M. J. ltmle: An R package implementing targeted minimum loss-based estimation for longitudinal data. *Journal of Statistical Software*, 81(1):1–21, 2017.

doi: 10.18637/jss.v081.i01.
Levine, S., Kumar, A., Tucker, G., and Fu, J. Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems. *arXiv preprint arXiv:2005.01643*,
2020.

Li, R., Hu, S., Lu, M., Utsumi, Y., Chakraborty, P., Sow, D. M., Madan, P., Li, J., Ghalwash, M., Shahn, Z., and Lehman, L.-w. G-net: A recurrent network approach to G-computation for counterfactual prediction under a dynamic treatment regime. In *Proceedings of Machine* Learning for Health, volume 158 of *Proceedings of Machine Learning Research*, pp. 282–299. PMLR, 2021.

Melnychuk, V., Frauen, D., and Feuerriegel, S. Causal transformer for estimating counterfactual outcomes. In Chaudhuri, K., Jegelka, S., Song, L., Szepesvari, C., Niu, G., and Sabato, S. (eds.), *Proceedings of the 39th International Conference on Machine Learning*, volume 162 of *Proceedings of Machine Learning Research*, pp.

15293–15329. PMLR, 2022.

Milborrow, S. *earth: Multivariate Adaptive Regression* Splines, 2023. URL https://CRAN.R-project.

org/package=earth. R package version 5.3.2.

Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A.,
Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. *arXiv preprint* arXiv:1312.5602, 2013.

Narita, Y., Yasui, S., and Yata, K. Debiased off-policy evaluation for recommendation systems. In Proceedings of the 15th ACM Conference on Recommender Systems, RecSys
'21, pp. 372–379, New York, NY, USA, 2021. Association for Computing Machinery. ISBN 9781450384582.

Petersen, M. L. and van der Laan, M. J. Causal models and learning from data: Integrating causal modeling and statistical estimation. *Epidemiology (Cambridge, Mass.)*,
25(3):418–426, 2014.

Polley, E., LeDell, E., Kennedy, C., and van der Laan, M. *SuperLearner: Super Learner Prediction*,
2021. URL https://CRAN.R-project.org/ package=SuperLearner. R package version 2.028.1.

Robins, J. A new approach to causal inference in mortality studies with a sustained exposure period—application to control of the healthy worker survivor effect. *Mathematical modelling*, 7(9-12):1393–1512, 1986.

Robins, J. M., Rotnitzky, A., and Zhao, L. P. Estimation of Regression Coefficients When Some Regressors Are Not Always Observed. *Journal of the American Statistical* Association, 89(427):846–866, 1994.

Salerno, S. and Li, Y. High-dimensional survival analysis:
Methods and applications. *Annual review of statistics and* its application, 10:25–49, 2023.

Sutton, R. S. Learning to predict by the methods of temporal differences. *Machine learning*, 3:9–44, 1988.

van der Laan, M. and Rubin, D. Targeted Maximum Likelihood Learning. *The International Journal of Biostatistics*,
2(1), 2006.

van der Laan, M. J. and Gruber, S. Targeted Minimum Loss Based Estimation of Causal Effects of Multiple Time Point Interventions. *The International Journal of* Biostatistics, 8(1), 2012.

van der Laan, M. J. and Robins, J. *Unified Methods for* Censored Longitudinal Data and Causality. Springer Series in Statistics. Springer New York, 2003. ISBN
978-0-387-21700-0.

van der Laan, M. J. and Rose, S. Targeted Learning:
Causal Inference for Observational and Experimental Data. Springer Series in Statistics. Springer, 2011. ISBN
978-1-4419-9781-4 978-1-4419-9782-1.

van der Laan, M. J. and Rose, S. Targeted Learning in Data Science: Causal Inference for Complex Longitudinal Studies. Springer Series in Statistics. Springer International Publishing, 2018.

van der Laan, M. J., Polley, E. C., and Hubbard, A. E.

Super learner. Statistical Applications in Genetics and Molecular Biology, 6(1):1309–1309, 2007. ISSN 15446115.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention is all you need. In *Advances in Neural Information* Processing Systems, volume 30. Curran Associates, Inc.,
2017.

Wyss, R., Yanover, C., El-Hay, T., Bennett, D., Platt, R. W.,
Zullo, A. R., Sari, G., Wen, X., Ye, Y., Yuan, H., Gokhale, M., Patorno, E., and Lin, K. J. Machine learning for improving high-dimensional proxy confounder adjustment in healthcare database studies: An overview of the current literature. *Pharmacoepidemiology and drug safety*, 31(9):
932–943, 2022. ISSN 1053-8569.

Yamagishi, K., Muraki, I., Kubota, Y., Hayama-Terada, M.,
Imano, H., Cui, R., Umesawa, M., Shimizu, Y., Sankai, T.,
Okada, T., Sato, S., Kitamura, A., Kiyama, M., and Iso, H.

The Circulatory Risk in Communities Study (CIRCS): A
Long-Term Epidemiological Study for Lifestyle-Related Disease Among Japanese Men and Women Living in Communities. *Journal of Epidemiology*, 29(3):83–91, 2019.

## A. Notation

Here we list notations used in the article.

| O                                    | Observed variables O = (W = W0, L1, A1, Y1, L2, A2, Y2, . . . , Lτ , Aτ , Yτ )   |                   |    |    |
|--------------------------------------|----------------------------------------------------------------------------------|-------------------|----|----|
| τ                                    | Maximum length of time-horizon                                                   |                   |    |    |
| T                                    | Stopping time                                                                    |                   |    |    |
| W                                    | Baseline covariates                                                              |                   |    |    |
| Lt                                   | Time-dependent covariates (states)                                               |                   |    |    |
| At                                   | Time-dependent treatments (controls)                                             |                   |    |    |
| Yt                                   | Outcomes. In survival case, binary failure indicator defined as Yt = 1{T ≤ t}    |                   |    |    |
| Y                                    | Outcome at the end of the trajectory: Y = YT                                     |                   |    |    |
| pa(X)                                | Parent nodes of X. For example, pa(Lt) = (W, L1:t−1, A1:t−1, Y1:t−1)             |                   |    |    |
| P0                                   | The true distribution of the observed variable                                   |                   |    |    |
| Pˆ n                                 | Estimator of P0                                                                  |                   |    |    |
| π                                    | Propensity scores π = [πt] τ 1 with π(dat|pa(at)) = P(dat|pa(at))                |                   |    |    |
| g                                    | User-specified treatment policies g = [gt] τ t=1                                 |                   |    |    |
| ψ                                    | Target functional ψ(P) = EgY                                                     |                   |    |    |
| ψ0                                   | True parameter ψ0 = ψ(P0)                                                        |                   |    |    |
| ψˆ n                                 | Estimator of ψ0                                                                  |                   |    |    |
| σˆn                                  | Estimator of the standard error of the estimator ψˆ n                            |                   |    |    |
| Qg                                   | State-action value functions Qg = [Q g ] τ t t=1                                 |                   |    |    |
| g                                    | g (pa(Yt)) = Eg[Y |pa(Yt)]                                                       |                   |    |    |
| Q t                                  | = Q t                                                                            |                   |    |    |
| V g                                  | Value functions V g = [V g ] τ+1 t t=1                                           |                   |    |    |
| g                                    | g (pa(At)) = Eg[Y |pa(At)] for t = 1, . . . , τ and V g                          |                   |    |    |
| V t                                  | = V t                                                                            | τ+1 = Yτ          |    |    |
| 1 with G(dat|pa(at)) = P(dat|pa(at)) |                                                                                  |                   |    |    |
| G                                    | Propensity scores G = [Gt] τ                                                     |                   |    |    |
| It                                   | Clever covariates (importance weights) It = Qt s=1 dgs/dπs(O) 1 − ψ0 + Pτ g      | g                 | g  |    |
| D⋆                                   | Efficient influence function of ψ: D⋆ (Qg , V g ; G) = V                         | t=1(V t+1 − Q ) t |    |    |
| Qg ε                                 | Local least favorable submodel Qg ε = [Q g t,ε] τ t=1                            |                   |    |    |
| g                                    | g                                                                                | g                 |    |    |
| Q t                                  | logit Q t,ε = logit Q t + ε                                                      |                   |    |    |
| V ε                                  | Local least favorable submodel V                                                 |                   |    |    |
| g                                    | ε = [V g t,ε] g τ+1 t=1                                                          |                   |    |    |
| g                                    | g                                                                                | g                 | g  | g  |
| V t                                  | logit V t,ε = logit V t + ε for t = 1, . . . , τ and V τ+1,ε = V τ+1             |                   |    |    |
| L(Qg , V g )                         | Loss function for temporal difference learning                                   |                   |    |    |
| L ⋆                                  | Loss function for targeting                                                      |                   |    |    |
| α                                    | Weight for the propensity loss (hyperparameter)                                  |                   |    |    |
| P f                                  | Mean of a function f under the distribution P: P f = R f dP                      |                   |    |    |
| E(•t)                                | Embedding of a node •t                                                           |                   |    |    |
| e•(•t)                               | Type embedding of a node •t                                                      |                   |    |    |
| Et                                   | Positional encoding at time t                                                    |                   |    |    |
| fX                                   | production function of a node X                                                  |                   |    |    |

## B. Proof

Proof of Theorem 4.2. A direct calculation shows
∂εL
⋆ t
(Q
g t,ε, V g t+1,ε⋆ ) = It(G)[∂εQ
g t,ε][∂Q
g t,ε Lbce(Q
g t,ε, V g t+1,ε⋆ )] = It(G)(V
g t+1,ε⋆ − Q
g t,ε).

Substitution of ε
⋆to ε yields the t-th component of the efficient influence function (34) at (Q
g ε
⋆ , V g ε
⋆ , G).

## C. Review Of Tmle C.1. Structural Causal Model

We assume each node depends on the all previous nodes in the trajectory, that is, we do not assume the Markovian property.

And each node X is produced from the parent nodes pa(X) and independent noise random variables UX by a measurable

$$g\ll\pi,$$

function fX: X = fX(pa(X), UX). This production function fX induces a conditional distribution PX|H of X given H = pa(X) by pushing forward the distribution of noise variable: PX|H(A|h) = (PUX ◦ f
−1 X (h, ·))(A) for all measurable A ⊂ X , where X is a domain of random vector X. Starting from nodes without parents including noise nodes and their distributions, production functions and their causal structure, which can be described by a directed acyclic graph over the ovservables, generate the joint distribution of the observed random variables. With our particular data in longitudinal setting, we define the propensity score πt = PAt|pa(At), where pa(At) = pa(At) is the patient history before the node At. We use the same symbol for the production function if the treatment assignment is deterministics, that is, there is no noise variable in generating the treatment node: dπt(At|pa(At)) = 1 if At = at for some specific at.

## C.2. Causal Target Parameter And Identification

$$\Pi_{*}^{*}$$

Our target parameter is the counterfactual mean of the final outcome Y under the user-specified dynamic treatment policy g = (gt). This is the mean of counterfactual outcome which is produced by replacing πt with gt in the structural causal model:
ψ g(P) = EY g. (24)
To identify this causal target paratmer from observatoinal data, we assume the following conditions of the positiviy:
g ≪ π, (25)
and the sequential randomization:
Y
g ⊥ At | pa(At) for t = 1*, . . . , τ.* (26)
Note that the consistency Y = Y
π usually stated in the causal inference literature is a consequence of the definition of counterfactual outcome in our structural causal model. Under these identifiability conditions, this parameter is identified through g-formula that is the mean of Y under the counterfactual distribution which is given by replacing distributions πt with gt:
EY g = EgY. (27)
Then the problem reduced to the estimation of the statistical parameter:
ψ(P) = EgY. (28)

## C.3. Tmle

Bias correction by TMLE is based on the following first order approximation of the target functional around the true distribution P0 (van der Laan & Rubin, 2006; van der Laan & Rose, 2011; Kennedy, 2022):
ψ(Pˆn) − ψ(P0) = −P0D⋆(Pˆn) + R2(Pˆn, P0), (29)
where D⋆is called influence function and R2 is the second order remainder. This equation is the infinite dimensional extension of Taylor expansion.

The right hand side of this equation can be further written as:

$$Y^{g}=E_{g}Y.$$
$$\mathbf{\ddot{\cal{E}}}$$
$$\psi(P)=E_{g}Y.$$
$$-P_{n}D^{\star}(\hat{P}_{n})+(P_{n}-P_{0})\big[D^{\star}(\hat{P}_{n})-D^{\star}(P_{0})\big]+(P_{n}-P_{0})D^{\star}(P_{0})+R_{2}(\hat{P}_{n},P_{0}),$$

whose second term called empirical process term converges to zero in the rate of square root of n if D⋆(Pˆn), D⋆(P0) belong to the Donsker class and D⋆(Pˆn) converges to D⋆(P0) in L
2(P0). Given a good initial fit Pˆn of P0, above conditions are usually satisfied and, in addition, R2(Pˆn, P0) = oP0
(n
−1/2). Thus, by further using the fact about the influence function that P0D⋆(P0) = 0, the right hand side reduced to
−PnD⋆(Pˆn) + PnD⋆(P0) + oP0
(n
−1/2). (31)
Now, the idea is to find Pˆ⋆
n in the close neighborhood of Pˆn that solves the empirical analog of the first term:
PnD⋆(Pˆ⋆
n
) = 0. (32)
By doing so, using similar arguments as above for Pˆ⋆
n instead of Pˆn, we have the following.

ψ(Pˆ⋆
n
) − ψ(P0) = PnD⋆(P0) + oP0
(n
−1/2). (33)
Thus, our estimator ψ(Pˆ⋆
n
) is a plug in estimator and attains the efficiency bound among the asymptotically linear and regular estimators.

$\left(28\right)^2$
$$(30)^{\frac{1}{2}}$$
$\downarrow$ . 
$\square$
$$\mathrm{lowing}.$$
$\langle2\rangle$. 

## C.4. Efficient Influence Curve

Then the efficient influence function of our target parameter is computed as follows (van der Laan & Gruber, 2012)

$$D^{*}(P)=\sum_{t=1}^{\tau}D_{t}^{*}(P)\tag{34}$$ $$=(V_{1}^{2}-\psi_{0})+\sum_{t=1}^{\tau-1}I_{t}(V_{t+1}^{q}-Q_{t}^{q})+I_{\tau}(Y_{\tau}-Q_{\tau}^{q})$$ $$=(V_{1}^{2}-\psi_{0})+\sum_{t=1}^{\tau+1}\mathbb{1}\{Y_{t-1}=0\}I_{t}(V_{\tau+1}^{q}-Q_{t}^{q})+\mathbb{1}\{Y_{\tau-1}=0\}I_{\tau}(Y_{\tau}-Q_{\tau}^{q})$$ $$=(V_{1}^{2}-\psi_{0})+\sum_{t=1}^{\tau-1}I_{t}(V_{\tau+1}^{q}-Q_{t}^{q})+I_{T}(Y_{T}-Q_{T}^{q}),$$  w definition.  
where Y0 = 0 by definition.

## D. Convergence Of Temporal Difference Learning

First, consider a flexible model Qθ and corresponding Vt,θ = EAt∼gtQt,θ. Initiate θ 0and then iteratively update by θ k+1 = arg minθ PL(Qθ, Vθ k ) for k = 2*, . . . ,* till convergence. Our proof below shows that if we use a variation independent parameter space for each Qt,θ and the parameter spaces contain the true Qt,P , then in K + 2-steps this algorithm will have converged to the true solution QP .

Ignoring the parameterization, but just thinking in terms of optimizing over parameter spaces, this algorithm corresponds with: initiate V
0, and then for k = 0*, . . .*, compute Qk+1 = arg minQ PL*Q, V* kand set V
k+1 as the one implied by the intervention g and Qk+1; and set k = k + 1.

Firstly, we claim that in a nonparametric model the t-specific parameters Qt are variation independent across t. Consider a given V (misspecified). This implies a parameter space ELt|pa(Lt)∼µt(·|pa(Lt))Vt : µt for the regressions Q. The parameter space of the free parameter µt is even larger than the parameter space of functions of pa(Lt). Therefore this appears indeed a reasonable condition. Then we can state that the parameter space over which we optimize at step k of the algorithm is the cartesian product of the parameter spaces Qt for Qt across t = *τ, . . . ,* 1. Consider the k = 1-step of the algorithm in which the outcomes are V
0and we optimize over all the Q ∈Q1 t=τ Qt. Then, Q1is the minimizer of Q → PL(*Q, V* 0). That means that the derivative w.r.t. εt along a path Q1 t + εtht through Q1 t in any direction ht at ϵt = 0 should be equal to zero, across all t = *τ, . . . ,* 1. Thus, at ε = 0, we have

$$\frac{d}{d\varepsilon}\sum_{t=1}^{\tau}{\mathcal{L}}_{t}(Q_{t}^{1}+\varepsilon_{t}h_{t}\mid V_{t+1}^{0})=0$$

Consider the derivative w.r.t. εY . This yields the score equation P hQτ
(Vτ+1 − Q1 τ
) = 0 for all hQτ
. This implies that Q1 τ = Qτ,P . The others are some optimizer. Now, we go to step k = 2. We now know that V
1 τ = Vτ,P due to Q1 τ = Qτ,P . Therefore, at the next step, due to the derivative w.r.t. ετ−1, it follows that Q2 τ−1 = Qτ−1,P , while it again Q2 τ = Q1 τ = Qτ,P . Then, at step k = 3, we also obtain Q3 τ−2 = Qτ−2,P . In this manner, it follows that after K + 2 steps we have QK+2 = QP .

## E. Hyperparameter Tuning

We selected hyperparameters shown in Table 4 which optimized the empiricall loss L
Q + L
G in the validation set which is the 30% of the entire dataset. The parameter α and β for censoring mechanism balances the learning rate of G-parts and Q-parts because the complexity of G-parts would be simpler than Q-parts which involves prediction in the long-range.

| Table 4. Selected hyperparameters.   |                       |                        |            |         |            |       |       |       |       |       |       |       |       |
|--------------------------------------|-----------------------|------------------------|------------|---------|------------|-------|-------|-------|-------|-------|-------|-------|-------|
| Data                                 | Simple Synthetic Data | Complex Synthetic Data | Real World |         |            |       |       |       |       |       |       |       |       |
| Model                                | Deep LTMLE            | DeepACE                | Deep LTMLE | DeepACE | Deep LTMLE |       |       |       |       |       |       |       |       |
| τ                                    | 10                    | 20                     | 30         | 10      | 20         | 30    | 10    | 20    | 30    | 10    | 20    | 30    | 30    |
| Embedding dimension                  | 32                    | 32                     | 32         | 32      | 32         | 32    | 16    | 32    | 32    | 32    | 32    | 32    | 32    |
| Dropout rate                         | 0                     | 0                      | 0.1        | 0.3     | 0.2        | 0.1   | 0     | 0     | 0     | 0.3   | 0.2   | 0.2   | 0     |
| Hidden size                          | 64                    | 64                     | 16         | 8       | 4          | 4     | 64    | 32    | 16    | 4     | 4     | 4     | 16    |
| Number of Layers                     | 8                     | 4                      | 4          | 1       | 1          | 2     | 4     | 4     | 4     | 2     | 8     | 2     | 8     |
| Number of heads                      | 8                     | 4                      | 4          | -       | -          | -     | 8     | 8     | 8     | -     | -     | -     | 4     |
| Learning rate                        | 1e-04                 | 5e-04                  | 5e-04      | 5e-03   | 1e-02      | 5e-03 | 1e-03 | 5e-04 | 1e-04 | 5e-04 | 5e-04 | 5e-04 | 5e-04 |
| α                                    | 0.1                   | 0.01                   | 0.01       | 0.01    | 0.1        | 0.05  | 0.01  | 0.05  | 0.05  | 0.01  | 0.1   | 0.1   | 0.1   |
| β                                    | -                     | -                      | -          | 0.05    | 0.05       | 0.05  | -     | -     | -     | 0.05  | 0.05  | 0.05  | 0.01  |
| Number of epochs                     | 100                   | 200                    | 400        | 100     | 200        | 100   | 100   | 100   | 400   | 100   | 100   | 100   | 100   |

## F. Synthetic Data F.1. Simple Synthetic Data With Continuous Outcome

The process iteratively generates variables W, Lt, At, and Yt over time steps t, for t = 0*, . . . , τ* − 1. W ∼ Normal(0, 1).

At t = 0, L0 ∼ Normal(0.1W, 1), A0 ∼ Ber(σ(−0.5W + L0)), Y0 ∼ Ber(σ(−3 + 0.2W + 0.2L0 − 2A0)). For t > 0, Lt ∼ Normal(0.1W − 0.1At−1, 1), At ∼ Ber(σ(−0.5 + 0.3W + 0.3Lt + 2At−1)), Yt = σ(−3 + 0.2W + 0.2Lt − 2At),
σ(x) = (1 + e
−x)
−1is the sigmoid function. We set the counterfactual treatment at all time-points to 1 and and evaluated the counterfactual mean of survival under this treatment policy.

## F.2. Simple Synthetic Data With Survival Outcome

The process iteratively generates variables W, Lt, At, and Yt over time steps t, for t = 0*, . . . , τ* − 1. W ∼ Normal(0, 1). At t = 0, L0 ∼ Normal(0.1W, 1), A0 ∼ Ber(σ(−0.5W + L0)), Y0 ∼ Ber(σ(−3 + 0.2W + 0.2L0 − 2A0)). For t > 0, Lt ∼ Normal(0.1W −0.1At−1, 1), At ∼ Ber(σ(−0.5+0.3W +0.3Lt+2At−1)), Yt ∼ Ber(σ(−3+0.2W +0.2Lt−2At)),
with Yt−1 = 1 implying Yt = 1. Here σ(x) = (1 + e
−x)
−1is the sigmoid function. We set the counterfactual treatment at all time-points to 1 and and evaluated the counterfactual mean of survival under this treatment policy.

## F.3. Complex Synthetic Data With Survival Outcome

First draw parameters αi, βi ∼ Normal((i + 1)−1, 0.02) and γi ∼ 2 ∗ Binom(0.5) − 1 for i ∈ [ht], where h is the length of time-dependency with h = 1 corresponding to Markovian process. Then, draw error in time-dependet variables ε ℓ tj ∼ Normal(0, 0.1) for t ∈ [τ ] and j ∈ [p], errors in treatment ε A
t1 ∼ Normal(0, 0.2), ε A
t2 ∼ Normal(0, 0.05) for t ∈ [τ ].

For each t ∈ [τ ], Lt = tanh Pk∈[ht] αkLt−k + βkγk(2At−k − 1)+ ε ℓ tj , then draw At from an indicator function 1{(σ(st+) + ε A t2
) > 0.5}, with st = tan  Qj∈[p] L¯j + A¯+ ε A t1
. The outcome Yt is drawn from a Bernoulli distribution of a probability σ(pt) with pt = tan  Qj∈[p] L¯j − 0.7 ∗ (A¯ − 0.5)) − 4.5. Yt = 1 if Yt−1 = 1 for t > 0. We set the counterfactual treatment policy as 1{σ(st) > 0.5} for t ∈ [τ ] and evaluated the counterfactual mean of survival under this policy.

## G. Results With Simple Synthetic Data With Survival Outcome

Results of an experiment with the simple synthetic data described in Section F.2 was shown in Table 5. Although LTMLE's strong performance on simple synthetic data is anticipated due to reduced burden in estimating nuisance parameters from Markovian dependencies, Deep LTMLE remains highly competitive in this context, equalling LTMLE's performance. Our two targeting approaches demonstrated better bias variance trade off for the estimation of the target parameter compared to the untargeted approach. Both bias and standard deviation get improved a lot for all τ 's considered. The targeting step made a marked difference in terms of coverage probability, getting much closer to a nominal 95% coverage probability compared to the one without targeting.

| Table 5. Results from simple synthetic data   |        |          |          |        |        |        |        |        |        |        |        |        |
|-----------------------------------------------|--------|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Bias                                          | RMSE   | Coverage | Mean σˆn |        |        |        |        |        |        |        |        |        |
| Model                                         | τ = 10 | τ = 20   | τ = 30   | τ = 10 | τ = 20 | τ = 30 | τ = 10 | τ = 20 | τ = 30 | τ = 10 | τ = 20 | τ = 30 |
| LTMLE (GLM)                                   | 0.0052 | 0.0045   | 0.0021   | 0.0202 | 0.0268 | 0.0308 | 0.95   | 0.94   | 0.93   | 0.02   | 0.03   | 0.03   |
| LTMLE (SL)                                    | 0.0056 | 0.0058   | 0.0061   | 0.0203 | 0.0263 | 0.0311 | 0.91   | 0.93   | 0.91   | 0.02   | 0.02   | 0.03   |
| DeepACE                                       | 0.0213 | 0.0462   | -0.1342  | 0.0266 | 0.0515 | 0.1397 | 1.00   | 1.00   | 1.00   | 0.19   | 0.70   | 0.70   |
| Deep LTMLE                                    | 0.0080 | 0.0133   | 0.0090   | 0.0292 | 0.0569 | 0.0449 | 0.79   | 0.78   | 0.87   | 0.02   | 0.04   | 0.03   |
| Deep LTMLE †                                  | 0.0054 | 0.0070   | 0.0080   | 0.0207 | 0.0350 | 0.0329 | 0.91   | 0.95   | 0.91   | 0.02   | 0.04   | 0.03   |
| Deep LTMLE ⋆                                  | 0.0053 | 0.0053   | 0.0080   | 0.0207 | 0.0361 | 0.0310 | 0.90   | 0.96   | 0.92   | 0.02   | 0.04   | 0.03   |

## G.1. Semi-Synthetic Data

As a compromise, we conducted several additional experiments with semi-synthetic data from the real world data as used in previous studies (Bica et al., 2020; Frauen et al., 2023). For this experiment, we used covariates from the Circulatory Risk in Communities Study (CIRCS) and fit outcome regression given the history through each time point using XGBoost with early stopping. Outcomes were then generated using this fitted regression model. For the experiment, we sample 1000 observations from the empirical dstribution of covariates W, Lt, At and generate Yt for t = 1*, . . . , τ* with τ ∈ {10, 20.30}.

## H. Extension To Survival Analysis With Censoring

In this section, we describe the extended LTMLE model with censoring for the real world application in Section 5.4. We assume the following order of observed nodes O = (W = W0, L1, A1, C1, Y1, L2, A2, C2, Y2, . . . , Lτ , Aτ , Cτ , Yτ = Y ),
where Ct are binary censoring nodes with Ct = 1 indicating one being censord. Our interest is to estimate the risk of our outcome Yτ , the mortality of the individual. However, our observation period spans long-term, individuals are at risk of being censored. Censoring Ct is loss of follow-up from administrative reasons, for example, move to other areas or denial of participation in the survey. We assume degenerations of nodes. When we observe a jump in Y or C nodes, the process halts and all nodes after the jump remain constant with the last observed values. For example, if Yt = 1, then Ys = 1, Cs = 0, As−1 = At−1, and Ls = Lt for all *s > t*.

We constructed a Deep LTMLE similar to the one describe in Section 4 with this structure. The only difference is an additional component of censoring mechanism Gc which is involved in the clever covariate It and the loss function:

$$I_{t}(G)=\prod_{s=1}^{t}\frac{d(g\otimes\mathbb{1}(C_{s}=0))}{d(G^{a}_{t}\otimes G^{c}_{t})}(O),\text{and}\tag{35}$$  $$\mathcal{L}(Q,V,G)=\mathcal{L}^{Q}(Q,V)+\alpha\mathcal{L}^{G^{a}}(G^{a},A)+\beta\mathcal{L}^{G^{c}}(G^{c},C),\tag{36}$$

where β is an additional hyperparameter for the loss function of binary logistic loss. The counterfactual treatment on the censoring process is 1(Ct = 0) meaning supression of censoring. Estimates of the target parameter and the efficient influence curve for different treatment strategies are computed using Deep LTMLE, and average treatment effects (ATEs)
and its EIC were computed using the delta method. Based on the estimated EICs of the target parameters at each time point t, we constructed a simultaneous confidence intervals.