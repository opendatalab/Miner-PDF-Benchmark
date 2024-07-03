# Longitudinal Targeted Minimum Loss-based Estimation with Temporal-Difference Heterogeneous Transformer 

Toru Shirakawa ${ }^{12} \mathbf{Y i ~ L i}^{2}$ Yulun Wu ${ }^{2}$ Sky Qiu ${ }^{2}$ Yuxuan $\mathbf{L i}^{2}$<br>Mingduo Zhao $^{2}$ Hiroyasu Iso $^{13}$ Mark van der Laan ${ }^{2}$


#### Abstract

We propose Deep Longitudinal Targeted Minimum Loss-based Estimation (Deep LTMLE), a novel approach to estimate the counterfactual mean of outcome under dynamic treatment policies in longitudinal problem settings. Our approach utilizes a transformer architecture with heterogeneous type embedding trained using temporal-difference learning. After obtaining an initial estimate using the transformer, following the targeted minimum loss-based likelihood estimation (TMLE) framework, we statistically corrected for the bias commonly associated with machine learning algorithms. Furthermore, our method also facilitates statistical inference by enabling the provision of $95 \%$ confidence intervals grounded in asymptotic statistical theory. Simulation results demonstrate our method's superior performance over existing approaches, particularly in complex, long time-horizon scenarios. It remains effective in small-sample, short-duration contexts, matching the performance of asymptotically efficient estimators. To demonstrate our method in practice, we applied our method to estimate counterfactual mean outcomes for standard versus intensive blood pressure management strategies in a real-world cardiovascular epidemiology cohort study.


## 1. Introduction

In the fields of medicine and public health, researchers frequently encounter data that are both high-dimensional and longitudinal. The outcomes of interest in these settings often involve time to the incidence of some failure event, such as total mortality (van der Laan \& Robins, 2003; Salerno \&[^0]

Li. 2023). Estimating the counterfactual probability of the event is challenging in high-dimensional longitudinal settings. Existing methods suffer computationally due to lack of scalability and have worse performance due to curse-ofdimensionality (Wyss et al. 2022). In response, we propose an estimator that is computationally scalable and simultaneously allows for robust statistical inference. Our estimator incorporates a transformer architecture for estimating the target estimand, defined as the cumulative incidence probability under dynamic interventions, where the treatment sequence depends on patients' evolving histories. The target estimand can be identified through the $\mathrm{g}$-formula contingent upon suitable assumptions (Robins, 1986). However, the target functional involves integration over potentially highdimensional time-dependent covariates across time-horizon, posing computational challenges. Our method advances the longitudinal targeted minimum loss-based estimation (LTMLE) framework (van der Laan \& Gruber, 2012; Lendle et al. 2017) by leveraging the computational capabilities of the transformer, facilitating the estimation of the target estimand and relevant nuisance parameters.

A number of estimators for the target estimand were proposed since the pioneering work by Robins (Robins, 1986). These estimators first factor the target parameter as a functional of nuisance parameters given a structural assumption on the underlying variables. Then, a common strategy to construct an estimator is plug-in, where one estimate the nuisance components with some models and then plug them into the target functional. However, since the naive plugin of the estimated nuisance components causes bias, several methods have been proposed to remove this bias using the first variation of the target functional called influence function. Examples of such de-biasing techniques include one-step estimators (Klaassen, 1987, Bickel et al., 1993), estimating equations (Robins et al., 1994, Chernozhukov et al. 2022), and targeted minimum loss-based estimation (TMLE) (van der Laan \& Rose, 2011). Notably, due to its plug-in property, TMLE stands out because it will respect any conditional bounds on the outcome or global bounds on the statistical model, resulting in improved finite-sample performance (Gruber \& van der Laan, 2012).

The first-order bias of the plug-in estimator is represented as a population mean of the influence function evaluated at the estimated nuisance distribution. Bias correction is performed by solving the empirical analogue of this term. TMLE solves this term by optimizing a loss function along a submodel starting from the initial nuisance estimate (Bang \& Robins, 2005, van der Laan \& Rubin, 2006, van der Laan \& Rose, 2011). The loss function and the submodel are chosen so that the linear span of the derivative of the loss function along the submodel contains the efficient influence function, the influence function with minimal variance. Targeting is the term that refers to this correction by fluctuating of the initial estimate along the path.

The current LTMLE, a TMLE developed in the context of longitudinal data, relies on a sequential regression representation of the target estimand (Bang \& Robins, 2005). An ensemble machine learning technique called super learner is then used to estimate the nuisance components of the data-generating distribution (van der Laan et al., 2007). In real-world complex longitudinal data, these nuisance components, such as the survival probability at a given time, may depend on all past histories. Therefore, the Markovian property, which states that future variable values only depends on the present variables, independent of the past, is not guaranteed to hold. In other words, every observed variable could depend on the past variables in the time ordering. Hence, we want our model for the nuisance components to be able to take variable length of history as input. Under the targeted learning framework, we introduce a transformer architecture tailored towards our longitudinal setting and propose a novel method for the bias correction using a single fluctuation parameter across all time-points.

Our contribution includes: 1) Developed a general method that uses a transformer architecture to facilitate valid statistical inference in longitudinal settings concerning survival outcomes under dynamic interventions; 2) Proposed a method for bias correction using one-dimensional fluctuation for any length of time-horizon; 3) Demonstrated competetive statistical performance with asymptotically efficient estimators in simple and low-dimensional settings and superior statistical and computational performances in more complex settings; and 4) Applied our method to a real-world medical data with results presented in a format that aligns with clinical research guidelines.

## 2. Related Work

In the data science literature, several methods were proposed that predict the counterfactual outcomes from patient history. The methods include G-Net (Li et al. 2021), counterfactual recurrent network (CRN) (Bica et al. 2020), and causal transformer (CT) (Melnychuk et al. 2022). However, their target parameters do not involve survival outcomes, and their methods are optimized for the mean squared error (MSE) of the individual predictions, rather than for making statistical inferences. DeepACE (Frauen et al., 2023) is closely related to the present study which uses deep neural networks to estimate the whole propensity scores and outcome regressions simultaneously. Furthermore, it has an additional layer for targeting implementing the one-dimensional submodel proposed by van der Laan (van der Laan \& Rose, 2018). Our method differs from theirs in the following three aspects. First, DeepACE incorporates the targeting step within their loss function, which requires an additional hyperparameter. However, there is a lack of justification for the chosen value of this hyperparameter and guidance on its tuning in practical applications. Our approach, in contrast, separates the targeting step, aligning more closely with the TMLE literature. Second, DeepACE does not address survival outcomes, specifically failing to consider the process degeneracy following a patient's event occurrence. Third, while DeepACE utilizes the long short-term memory (LSTM) architecture, our method employs transformers. Transformers are superior in capturing long-term dependencies and offer greater computational efficiency during training than LSTM. Moreover, DeepACE does not provide uncertainty measures, such as confidence intervals, limiting its utility for statistical inference.

Our problem of estimating mean of counterfactual outcomes from longitudinal observational data under dynamic interventions has been extensively investigated as an off-policy evaluation problem in the bandit algorithm and reinforcement learning literature (Levine et al., 2020). Methods of bias correction after plugging in the initial estimate with influence function were also introduced in this context (Jiang \& Li, 2016; Farajtabar et al., 2018, Narita et al., 2021). However, they did not provide tools for inference. Double reinforcement learning (Kallus \& Uehara, 2020) utilized the efficient influence functions in the spirit of double machine learning (Chernozhukov et al. 2018), which is a closed form of a more general debiased estimating equation framework (Chernozhukov et al., 2022), to correct plug-in bias and proved efficiency. TMLE deform the distribution itself to correct bias before plugged-in to the the target functional, thereby the values are contained the domain of the functional.

## 3. Problem Formulation

In this section, follwing the roadmap of causal inference (Petersen \& van der Laan, 2014, van der Laan \& Rose, 2018, Dang et al., 2023), we first describe the experiment that generated the observed data and the statistical model that contains the data-generating distribution. Next, we define our causal target parameter. Then, we discuss assumptions needed to identify our target parameter from the observed
data. Finally, we describe the idea of statistical method for constructing estimator and correcting bias.

### 3.1. Data

We consider the general longitudinal setting involving repeated measurements of a set of variables for a group of $n$ patients over a period of time. In particular, our observed data contains $n$ independent and identically distributed copies of random vector

$$
O=\left(W_{0}=W, L_{1}, A_{1}, Y_{1}, \ldots, L_{T}, A_{T}, Y_{T}=Y\right)
$$

with baseline covariates $W$, time-dependent covariates $L_{t}$, treatments $A_{t}$, and outcome $Y_{t}$. We use $P_{0}$ to denote the true probability distribution of $O$ that generated the data, and $P_{0}$ is in some statistical model $\mathcal{M}$. Stopping time $T$ is a random variable (e.g. time of death in the case of survival analysis) and we use $\tau$ to denote the maximum time. We make the remark that in real-world data, patients are often subject to censoring. For a formulation of the data structure involving censoring nodes, see Appendix $\mathrm{H}$

### 3.2. Target Parameter

To define the target parameter, we introduce a structural causal model (SCM). In brief, SCM assumes each observed random variable $X$ is generated from the parent nodes $p a(X)$ and the external noise $U_{X}$ by a production function $f_{X}$ as $X=f_{X}\left(p a(X), U_{X}\right)$. By abusing notation, we also denote the induced probability measure of $X$ by the same symbol $f_{X}$. See Appendix C. 1 for details.

Our target parameter is the counterfactual mean of the final outcome $Y$ under a user-specified dynamic treatment policy $g=\left[g_{t}\right]_{t=1}^{\tau}$ where $g_{t}$ is a probability measure on the treatment space conditioned on the whole history, $p a\left(A_{t}\right)=\left(L_{1: t}, A_{1: t-1}, Y_{1: t-1}\right)$ up until $A_{t}$ (not including $A_{t}$ ). Specifically, our target parameter is given by

$$
\psi(P)=\mathbb{E} Y^{g}
$$

which is the mean of the counterfactual outcome produced by replacing $\pi$, defined as the observed treatment policy from the data, with $g$ in the structural causal model.

Identification Under the positivity assumption:

$$
g \ll \pi
$$

and the sequential randomization assumption:

$$
Y^{g} \perp A_{t} \mid p a\left(A_{t}\right) \text { for } t=1, \ldots, \tau
$$

we can identify our target causal parameter through gformula as the mean of $Y$ under the counterfactual distribution which is given by replacing distributions $\pi$ with $g$ (Robins, 1986):

$$
\mathbb{E} Y^{g}=\mathbb{E}_{g} Y
$$

Note that the consistency assumption $Y=Y^{\pi}$, usually stated in causal inference literature, is a consequence of the definition of counterfactual outcome in our SCM. Now the problem is reduced to the estimation of the statistical parameter:

$$
\psi(P)=\mathbb{E}_{g} Y
$$

### 3.3. Targeted Minimum Loss-based Estimation

Given we have an estimator $\hat{P}_{n}$ of the data-generating distribution $P_{0}$, a natural estimator of the target functional is the plug-in estimator $\hat{\psi}_{n}=\psi\left(\hat{P}_{n}\right)$. Under a regularity condition, $\psi$ admits the following first-order expansion

$$
\psi\left(\hat{P}_{n}\right)-\psi\left(P_{0}\right)=-\int_{\mathcal{O}} D^{\star}\left(\hat{P}_{n}\right) d P_{0}+R_{2}\left(\hat{P}_{n}, P_{0}\right)
$$

where $D^{\star}$ is the efficient influence function of $\psi$, and $R_{2}\left(\hat{P}_{n}, P_{0}\right)$ is the exact remainder. Influence functions quantifies the amount of changes of an estimator under small perturbations of the sample. The efficient influence function is the influence function with minimal variance. The idea of TMLE is to eliminate the empirical analogue of the first term of the right hand side by fluctuating $\hat{P}_{n}$ to find a distribution $\hat{P}_{n}^{\star}$ with $P_{n} D^{\star}\left(\hat{P}_{n}^{\star}\right)=0$, where $P f=\int f d P$ is a shorthand for the expectation of a measurable function $f$ with respect to a probability measure $P$. Our problem is to obtain an initial estimate $\hat{P}_{n}$ with a potentially large scale and high dimensional longitudinal data, and correct bias of the plug-in estimator $\psi\left(\hat{P}_{n}\right)$ by fluctuating $\hat{P}_{n}$.

## 4. Proposed Method

In this section, we describe our proposed method, Deep Longitudinal Targeted Minimum Loss-based Estimation (Deep LTMLE). Let

$$
Q_{t}^{g}\left(p a\left(Y_{t}\right)\right)=\mathbb{E}_{g}\left[Y_{T} \mid L_{1: t}, A_{1: t}, Y_{1: t-1}\right]
$$

be the mean outcome at stopping time $T$ given the history before node $Y_{t}$ for $t=1, \ldots, \tau$, where future treatments $A_{t+1}, \ldots, A_{T}$ follow a counterfactual treatment assignment policy $g$. Similarly,

$$
V_{t}^{g}\left(p a\left(A_{t}\right)\right)=\mathbb{E}_{g}\left[Y_{T} \mid L_{1: t}, A_{1: t-1}, Y_{1: t-1}\right]
$$

is the mean outcome at stopping time $T$ given the history before node $A_{t}$, for $t=1, \ldots, \tau$. We abbreviate $Q_{t}^{g}$ for $Q_{t}^{g}\left(p a\left(Y_{t}\right)\right)$ if it is clear from the context, similarly for $V_{t}^{g}$. Our goal is to estimate $\psi(P)$ by

$$
\begin{aligned}
\hat{\psi}_{n}^{\star} & =P_{n} \hat{V}_{1, \varepsilon^{\star}}^{g}\left(p a\left(A_{1}\right)\right) \\
& =P_{n} \mathbb{E}_{A_{1} \sim g_{1}\left(p a\left(A_{1}\right)\right)}\left[\hat{Q}_{1, \varepsilon^{\star}}^{g}\left(p a\left(A_{1}\right), A_{1}\right)\right]
\end{aligned}
$$

where $\hat{Q}_{1, \varepsilon^{\star}}^{g}$ is an estimation of $Q_{1}^{g}$ such that $\hat{\psi}_{n}^{\star}$ is asymptotically efficient. We achieve this by proposing a temporal-



difference heterogeneous transformer to yield an initial estimation $\hat{Q}_{1}^{g}$, then update this estimation to get $\hat{Q}_{1, \varepsilon^{\star}}^{g}$ via Targeted Minimum Loss-based Estimation (TMLE).

### 4.1. Temporal-Difference Heterogeneous Transformer

To learn the initial model $\hat{V}_{1}^{g}$, we use temporal-difference loss as the objective to learn underlying models $\hat{Q}_{t}^{g}$ for $t=1, \ldots, \tau$ via stochastic gradient descent (SGD). The principle of temporal difference learning (Sutton, 1988 Mnih et al. 2013) is to supervise $\hat{Q}_{t}^{g}$ to obey the temporal equality of $Q_{t}^{g}$ :

$$
\begin{aligned}
Q_{t}^{g} & =\mathbb{E}_{p\left(Y_{t}, L_{t+1} \mid p a\left(Y_{t}\right)\right)} V_{t+1}^{g} \\
& =\mathbb{E}_{p\left(Y_{t}, L_{t+1} \mid p a\left(Y_{t}\right)\right), g_{t+1}\left(p a\left(A_{t+1}\right)\right)} Q_{t+1}^{g}
\end{aligned}
$$

for $t=1, \ldots, \tau-1$ and $Q_{\tau}^{g}=\mathbb{E}_{p\left(Y_{\tau} \mid p a\left(Y_{\tau}\right)\right)} Y_{\tau}$. The temporal difference loss on a sample trajectory is thus given by $\mathcal{L}_{t}^{Q}=\mathcal{L}\left(\hat{Q}_{t}^{g}, \hat{V}_{t+1}^{g}\right)$ for $t=1, \ldots, T-1$, where $\hat{V}_{t+1}^{g}\left(p a\left(A_{t+1}\right)\right)=$ $\mathbb{E}_{A_{t+1} \sim g_{t+1}\left(p a\left(A_{t+1}\right)\right)}\left[\hat{Q}_{t+1}^{g}\left(p a\left(A_{t+1}\right), A_{t+1}\right)\right] \quad$ can be computed by Monte-Carlo estimation if $A$ is continuous, and $\mathcal{L}_{T}^{Q}=\mathcal{L}\left(\hat{Q}_{T}^{g}, Y_{T}\right)$. In the case of survival analysis, the components for $t=1, \ldots, \tau-1$ are defined as $\mathcal{L}_{t}^{Q}=\mathcal{L}_{\text {bce }}\left(\hat{Q}_{t}^{g}, \hat{V}_{t+1}^{g}\right)$, where $\mathcal{L}_{\text {bce }}(\hat{y}, y)=-[y \log \hat{y}+(1-y) \log (1-\hat{y})]$ is the binary cross entropy loss. To yield the updated model $\hat{Q}_{t, \varepsilon}^{g}$, we need to adjust $\hat{Q}_{t}^{g}$ after model training factoring in the estimating model $\hat{G}_{t}$ for the propensity score

$$
G_{t}\left(p a\left(A_{t}\right)\right)=\mathbb{P}\left[A_{T}=1 \mid L_{1: t}, A_{1: t-1}, Y_{1: t-1}\right]
$$

which we will describe in detail in the next section. Hence, the loss function also needs to include $\mathcal{L}_{t}^{G}=\mathcal{L}\left(\hat{G}_{t}, A_{t}\right)$ and is thus given by

$$
\mathcal{L}=\sum_{t=1}^{\tau} \mathbb{1}\{t \leq T\} \mathcal{L}_{t}=\sum_{t=1}^{T} \mathcal{L}_{t}=\sum_{t=1}^{T} \mathcal{L}_{t}^{Q}+\alpha \mathcal{L}_{t}^{G}
$$

where $\alpha$ is a hyperparameter that controls the weights of losses. See Algorithm 1 for the optimization workflow. Convergence of the algorithm can be found in Appendix D

For the estimation of $Q_{t}^{g}$ and $G_{t}$, we propose a unified model architecture to simultaneously optimize deep neural networks $\hat{Q}_{t}^{g}$ and $\hat{G}_{t}$ in an efficient, non-sequential manner by adapting a decoder-only Transformer (Vaswani et al., 2017, Brown et al., 2020) to longitudinal data with heterogeneous tokens. An overview of the model architecture is given in Figure 1. For each sampled sequence in the training set, we feed each token in the sequence to a linear embedding layer according to its variable type. In the case of Figure 1 there are four different embedding layers $e_{W}, e_{L}$, $e_{A}$, and $e_{Y}$. Each embedding layer has the same number of output dimensions. Then, each embedding is integrated with its positional encoding $E_{0}, \ldots, E_{\tau}$ and type encoding $E_{W}$, $E_{L}, E_{A}$, and $E_{Y}$ that represent its timestamp and variable type information through an aggregation function (e.g. sum, concat):

$$
E\left(\bullet_{t}\right)=\operatorname{aggr}\left\{e_{\bullet}\left(\bullet_{t}\right), E_{\bullet}, E_{t}\right\}
$$

for $\bullet_{t} \in\left(W_{0}, L_{1}, A_{1}, Y_{1}, \ldots, L_{\tau}, A_{\tau}, Y_{\tau}\right)$ where we used concat as aggr in the experiments in this work. Note that we include type embedding $E_{\bullet}$ because $e_{\bullet}$ need not necessarily be type-specific linear layers. For more efficient and parallelizable embedding operation, we can pad each variable to the same number of dimensions before feeding into the same embedding layer $e_{\bullet}=e$. Then, the embedded sequence is fed into the transformer and produce $\hat{G}$ and $\hat{Q}^{g}$ through output heads $f_{G}$ and $f_{Q}$ at each position that corresponds to token type $L$ and $A$ respectively:

$$
\begin{aligned}
& \hat{G}_{t}=f_{G}\left(\text { transformer }\left\{E\left(W_{0}\right), \ldots, E\left(L_{t}\right)\right\}\right) \\
& \hat{Q}_{t}^{g}=f_{Q}\left(\text { transformer }\left\{E\left(W_{0}\right), \ldots, E\left(A_{t}\right)\right\}\right)
\end{aligned}
$$

In practice, we can use a joint output layer $f$ for $f_{G}$ and $f_{Q}$ for more efficient and parallelizable output generation, where the output number of dimensions is the sum of the number of dimensions $\operatorname{dim}(A)$ for treatment $A$ and $\operatorname{dim}(Y)$ for outcome $Y$. Then, we compute softmax probabilities



Figure 1. Architecture of temporal-difference heterogeneous-token transformer (TDHT). Observed variables are fed into transformer after embedding layers depending on the variable types. Embedding layers aggregate linear transform with learnable type encoding and learnable positional encoding. Outputs of the transformer are $G$ after $L$ and $Q$ after $A$. Each output head consists of a linear layer and the final activation function depending on variable distribution (sigmoid for binary, softmax for categorical and none for continuous). The outputs of $G$ heads are used to learn propensity scores and those $Q$ are used for temporal-difference learning after integration with respect to the counterfactual treatment policy.

masking out the last $\operatorname{dim}(Y)$ dimensions for $\hat{G}_{t}$ and first $\operatorname{dim}(A)$ dimensions for $\hat{Q}_{t}^{g}$.

Our proposed architecture does not entail concatenation of variables at the same timestamp or sequential decoding of outputs following the transformer embedding block like prior work Melnychuk et al. (2022), which 1) allows us to handle different types of and different number of variables at different timestamps (e.g. starting from $W_{0}$, ending at $L_{8}$, while $A_{3}$ and $Y_{3}$ are missing), and 2) is fully parallelizable when we use padding instead of learnable linear mapping for the embedding layer $e_{\bullet}$ and use the joint output layer $f$.

### 4.2. Targeted Minimum Loss-based Estimation

Efficient Influence Function Since our target parameter is the counterfactual mean outcome at the final $\tau$, the relevant part of $P_{0}$ of interest are $Q_{t, 0}^{g}$ for $t=1,2, \ldots, \tau$.

Theorem 4.1. In our counterfactual mean case, the efficient influence function $D^{\star}(P)(O)=D^{\star}\left(\left\{Q_{t}^{g}, G_{t}\right\}_{t=1}^{\tau}\right)(O)$ is given by

$$
D^{\star}(P)(O)=\left(V_{1}^{g}-\psi_{0}\right)+\sum_{t=1}^{T} I_{t}\left(V_{t+1}^{g}-Q_{t}^{g}\right)
$$

where $I_{t}=\prod_{s=1}^{t} d g_{s} / d \pi_{s}$ and $V_{T+1}^{g}=Y_{T}$.

This is given in (van der Laan \& Gruber 2012).

### 4.2.1. Temporal Difference Targeting

Submodel We update the initial estimate $\hat{Q}_{t}^{g}$ for $Q_{t, 0}^{g}$ to $\hat{Q}_{t}^{g \star}$ such that $P_{n} D^{\star}\left(\left\{\hat{Q}_{t}^{g \star}, \hat{G}_{t}\right\}_{t=1}^{\tau}\right)=0$. We realize this by fluctuating $\hat{Q}_{t}^{g}$ along a one-dimensional submodel through the initial fit $\hat{Q}^{g}=\left[\hat{Q}_{t}^{g}\right]_{t=1}^{\tau}$ given by, $\hat{Q}_{\varepsilon}^{g}=\left[\hat{Q}_{t, \varepsilon}^{g}\right]_{t=1}^{\tau}$, where

$$
\operatorname{logit} \hat{Q}_{t, \varepsilon}^{g}=\operatorname{logit} \hat{Q}_{t}^{g}+\varepsilon
$$

with a common fluctuation parameter $\varepsilon$ across $t$. If the outcome is survival, then we automatically have $Y_{t} \in[0,1]$. In a general longitudinal setting for bounded $Y_{t}^{\prime}$ 's, we can re-scale both $Y_{t}$ and $\hat{Q}_{t}^{g}$ to $[0,1]$ and use the same onedimensional submodel.

Partial Loss function We search for the optimal fluctuation $\varepsilon^{\star}$ with respect to the partial loss function

$$
\mathcal{L}^{\star}\left(\hat{Q}_{\varepsilon}^{g}, \hat{V}_{\varepsilon^{\prime}}^{g} ; \hat{G}\right)=\sum_{t=1}^{T} I_{t}(\hat{G}) \mathcal{L}_{\mathrm{bce}}\left(\hat{Q}_{t, \varepsilon}^{g}, \hat{V}_{t+1, \varepsilon^{\prime}}^{g}\right)
$$

where $\hat{V}_{T+1, \varepsilon}^{g}=Y_{T}$ and $\hat{V}_{t, \varepsilon}^{g}=\mathbb{E}_{A_{t} \sim g_{t}}\left[\hat{Q}_{t, \varepsilon}^{g}\right]$, such that $\mathcal{L}^{\star}\left(\hat{Q}_{\varepsilon}^{g}, \hat{V}_{\varepsilon^{\prime}}^{g}\right)$ satisfies the following theorem:

Theorem 4.2. For any $\varepsilon^{\star}$, we have

$$
\left.\partial_{\varepsilon}\right|_{\varepsilon^{\star}} \mathcal{L}^{\star}\left(\hat{Q}_{\varepsilon}^{g}, \hat{V}_{\varepsilon^{\star}}^{g}\right)=D^{\star}\left(\hat{Q}_{\varepsilon^{\star}}^{g}, \hat{G}\right)
$$

See Section B for the proof.

Corollary 4.3. Suppose that we found an $\varepsilon^{\star}$ satisfying

$$
\left.\partial_{\varepsilon}\right|_{\varepsilon^{\star}} P_{n} \mathcal{L}^{\star}\left(\hat{Q}_{\varepsilon}^{g}, \hat{V}_{\varepsilon^{\star}}^{g}\right)=0
$$

then $\hat{Q}_{\varepsilon^{\star}}^{g}$ solves the efficient influence function.

In practice, for the finite sample performance, we only need to solve it to the order of standard error with a $\sigma_{n} / \log n$ factor (van der Laan \& Rose, 2011) (Algorithm2).



Convergence of Algorithm 2 The investigation of $\mathcal{L}_{\text {bce }}\left(\hat{Q}_{t, \varepsilon}^{g}, \hat{V}_{t, \varepsilon}^{g}\right)(O)$ for different $t$ and $O$ 's as a function of $\varepsilon$ suggests that they admit different bell curve shapes concentrating at different $\varepsilon$ 's and have different spread out levels. Thus, by summing up $\mathcal{L}_{\text {bce }}\left(\hat{Q}_{t, \varepsilon}^{g}, \hat{V}_{t, \varepsilon}^{g}\right)(O)$ across $t$ and across $O$ 's as $P_{n} \mathcal{L}^{\star}\left(\hat{Q}_{\varepsilon}^{g}, \hat{V}_{\varepsilon}^{g}\right)$ as a function of $\varepsilon$ will fluctuate a lot and we expect a local minima and local maxima around the neighborhood of $\varepsilon=0$. And thus the convergence of the algorithm is highly probable and we don't discover any issue in our simulations.

Comparison to LTMLE In the LTMLE, we only need a good estimate of $Q_{\tau}^{g}$ and then do backward sequential regression and targeting as mentioned in (van der Laan \& Gruber 2012). However, the problem is the error in the estimation of $Q_{\tau}^{g}$ can propagate as we progress back to get $Q_{\tau-1}^{g, *}, \ldots, Q_{1}^{g, *}$. Nonetheless, after our initial transformer step, we have good initial estimates for all $Q_{1}^{g}, \ldots, Q_{\tau}^{g}$. So, instead of only relying on a good estimate of $Q_{\tau}^{g}$, our algorithm makes uses of all of them. and doing targeting across $t$ with $o(\varepsilon)$ fluctuation at each $t$ level. Thus, we are able to pool information across time when doing the targeting step.

### 4.2.2. SEQUENTIAL TARGETING

Alternatively, one could apply a sequential targeting procedure that is very similar to LTMLE but with given initials generated from the transformer step.

Submodel We fluctuate each component of the initial fit $\hat{Q}^{g}=\left[\hat{Q}_{t}^{g}\right]_{t=1}^{\tau}$ along a model as

$$
\operatorname{logit} \hat{Q}_{t, \varepsilon_{t}}^{g}=\operatorname{logit} \hat{Q}_{t}^{g}+\varepsilon_{t}
$$

Loss function Starting from $t=\tau$, given we have found $\varepsilon_{t+1}^{\star}$, among individuals whose $T>t-1$, we search for empirical loss minimizer $\varepsilon_{t}^{\star}$ with respect to the loss function $\mathcal{L}_{t}^{\star}$ as,

$$
\mathcal{L}_{t}^{\star}\left(\hat{Q}_{t, \varepsilon_{t}}^{g}, \hat{V}_{t+1, \varepsilon_{t+1}^{\star}}^{g}\right)=I_{t}(\hat{G}) \mathcal{L}_{\mathrm{bce}}\left(\hat{Q}_{t, \varepsilon_{t}}^{g}, \hat{V}_{t+1, \varepsilon_{t+1}^{\star}}^{g}\right)
$$

where $\hat{V}_{t+1, \varepsilon_{t+1}^{*}}^{g}=\mathbb{E}_{A_{t+1} \sim g_{t+1}}\left[\hat{Q}_{t+1, \varepsilon_{t+1}^{\star}}^{g}\right]$ when $T>t$ and $\hat{V}_{t+1, \varepsilon_{t+1}^{\star}}^{g}=Y_{T}$ when $T=t$. To initialize, we set $\varepsilon_{\tau+1}^{\star}=0$.

Lemma 4.4. Suppose that we found $\varepsilon_{\tau}^{\star}, \ldots \varepsilon_{1}^{\star}$ sequentially as mentioned above, then $\left\{\hat{Q}_{\varepsilon_{t}^{\star}}^{g}\right\}_{t=1}^{\tau}$ solves the efficient influence function.



Comparaison to LTMLE While the error can still propagate as we move back in time, the error propagates only through the targeting steps whereas in LTMLE the error can also propagate through regressions. At each time step $t$, LTMLE needs to first regress $\hat{V}_{t+1, \varepsilon_{t+1}^{\star}}^{g}$ on $p a\left(Y_{t}\right)$ to get an estimate $\hat{Q}_{t}^{g}$ and then perform the targeting through the submodel in(22). However, we only use initial estimate $\hat{Q}_{t}^{g}$ from our transformer fit and it does not depend on $\varepsilon_{t+1}^{\star}, \ldots, \varepsilon_{\tau}^{\star}$.

Why not targeting through additional loss function As in DeepACE, the targeting can be performed through introducing additional loss components to further train the transformer we have build in the first step. This additional loss function will have its derivative equal to the efficient influence function. However, we find that the penalty factor before this loss function is hard to tune and in near all cases, it is hard to guarantee the EIF is solved and most of the time we will hurt our initial fits as shown in Appendix 5.1

## 5. Experiments

We conducted two experiments. In the first experiment, we compare the bias, root-mean-squared-error (RMSE), and coverage probability, of our estimator with existing estimators based on 100 times of estimations for both continuous and survival outcomes. The second experiment is an application of our proposed method to a real-world data.


Figure 2. Results from simple synthetic data with continuous outcome. Left: Sampling distributions of estimates. Right: Sampling distributions of empirical means of estimated efficient influence functions.

Table 1. Results from complex synthetic data. LTMLE (GLM): LTMLE with GLM; LTMLE (SL): LTMLE with super learner of GLM, MARS, and XGBoost; Deep LTMLE: initial estimate with TDHT; Deep LTMLE $\dagger$ : TDHT with sequential targeting; Deep LTMLE $\star$ : TDHT with temporal-difference targeting.

| Model | Bias |  |  | RMSE |  |  | Coverage |  |  | Mean $\hat{\sigma}_{n}$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | $\tau=10$ | $\tau=20$ | $\tau=30$ | $\tau=10$ | $\tau=20$ | $\tau=30$ | $\tau=10$ | $\tau=20$ | $\tau=30$ | $\tau=10$ | $=20$ | $\tau=30$ |
| LTMLE (GLM) | 0.0230 | 0.0766 | 0.1344 | 0.0265 | 0.0796 | 0.1381 | 1.00 | 1.00 | 1.00 | 0.43 | 0.69 | 0.76 |
| LTMLE (SL) | 0.0144 | 0.0297 | 0.0477 | 0.0185 | 0.0344 | 0.0545 | 1.00 | 1.00 | 1.00 | 0.31 | 0.40 | 0.45 |
| DeepACE | -0.0704 | -0.1491 | -0.2396 | 0.0948 | 0.1601 | 0.2453 | 1.00 | 1.00 | 1.00 | 0.74 | 0.69 | 0.57 |
| Deep LTMLE | 0.0182 | 0.0304 | 0.0499 | 0.0264 | 0.0342 | 0.0532 | 1.00 | 0.94 | 0.71 | 0.17 | 0.09 | 0.06 |
| Deep LTMLE $\dagger$ | 0.0158 | 0.0286 | 0.0548 | 0.0188 | 0.0314 | 0.0589 | 1.00 | 0.93 | 0.73 | 0.16 | 0.09 | 0.06 |
| Deep LTMLE $\star$ | 0.0143 | 0.0305 | 0.0471 | 0.0204 | 0.0333 | 0.0509 | 1.00 | 0.93 | 0.76 | 0.16 | 0.08 | 0.06 |

### 5.1. Synthetic Data with Continuous Outcome

First, we start our experiment with a very simple data generating process with continuous outcome, $n=500$, and $\tau=10$. The data generating proccess is described in the Section F.1. After fitting DeepACE, we additionally performed our targeting precedures on the fit.

The results were shown in Figure 2. Initial fits of Deep LTMLE and DeepACE had comparable bias. Even with the targeting loss, DeepACE failed to solve the efficient influence function. On the other hand, due to the separation of the targeting step in our method, we managed to solve it completely and succeeded in correcting bias.

### 5.2. Synthetic Data with Survival Outcome

Next, we evaluated Deep LTMLE under a highly complex data-generating process with survival outcomes, fivedimensional time-dependent covariates, non-Markovian dependencies, $n=1000$, and $\tau=10,20,30$, imitating the setups from previous studies (Bica et al. 2020, Frauen et al. 2023). See Section F. 3 for details.

Results are presented in Table 1. We observe that Deep LTMLE on average achieves a lower RMSE compared to other methods, particularly in scenarios with larger $\tau$, indicating its robustness in complex and realistic scenarios without Markovian dependencies. Benefits by our targeting procedures are obvious for $\tau=10,20$. For $\tau=30$, we still see reductions in bias and in RMSE when the temporaldifference targeting is applied. While Deep LTMLE's coverage probability diminished at $\tau=30$, the confidence intervals generated by LTMLE and DeepACE were notably over-conservative with large estimated standard errors.

The pronounced bias of DeepACE can likely be attributed to three factors. First, DeepACE's use of the squared-errorloss for the outcome is known to induce greater bias in sparse outcomes, a common scenario in survival analysis, as opposed to the logistic loss used in our approach (Gruber $\&$ van der Laan, 2010). Second, DeepACE failed to solve the efficient influence function. Third, DeepACE does not account for the degeneration of the survival outcome.

Simple Synthetic Data with Survival Outcome We also conducted an eperiment with a very simple survival synthetic data with one-dimensional time-dependent covariates, $n=1000$, and $\tau=10,20,30$. Although LTMLE with GLM is expected to have strong performance in this experiment, Deep LTMLE remains highly competitive in this

Table 2. Results from semi-synthetic data with unmeasured confounding

|  | Bias |  |  |  | RMSE |  |  |  | Coverage |  |  |  | Mean $\hat{\sigma}_{n}$ |  |  |  |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :---: | :---: | :---: |
| Model | $\tau=10$ | $\tau=20$ | $\tau=30$ | $\tau=10$ | $\tau=20$ | $\tau=30$ | $\tau=10$ | $\tau=20$ | $\tau=30$ | $\tau=10$ | $\tau=20$ | $\tau=30$ |  |  |  |  |
| LTMLE (SL) | 0.0075 | 0.0341 | 0.0574 | 0.0138 | 0.0491 | 0.0786 | 0.70 | 0.45 | 0.25 | 0.09 | 0.12 | 0.14 |  |  |  |  |
| DeepACE | -0.0174 | -0.0434 | -0.0770 | 0.0788 | 0.1154 | 0.1341 | 1.00 | 1.00 | 1.00 | 0.67 | 0.78 | 0.86 |  |  |  |  |
| Deep LTMLE | -0.0002 | 0.0108 | 0.0041 | 0.0162 | 0.0720 | 0.0772 | 1.00 | 0.95 | 1.00 | 0.18 | 0.27 | 0.32 |  |  |  |  |
| Deep LTMLE $\star$ | 0.0058 | 0.0429 | 0.0709 | 0.0205 | 0.0724 | 0.0968 | 0.95 | 0.90 | 0.95 | 0.18 | 0.26 | 0.31 |  |  |  |  |

context, equalling LTMLE's performance (Section G).

### 5.3. Semi-Synthetic Data

To evaluate the performance of the proposed methods, we generated realistic data from Circulatory Risk in Communities Study (CIRCS) (Yamagishi et al., 2019), a long-term on-going cardiovascular epidemiological cohort study, lasting over a half century. See Section G. 1 for the detail.

Table 2 shows the results with semi-synthetic data with unmeasured confounding, which reflects a real world setting. Deep LTMLE performed best in terms of bias for all time horizons. Furthermore, as the time horizon increases from 10 to 30, LTMLE's coverage probability drops as low as 0.3. On the other hand, Deep LTMLE has nominal coverage even in the longest time-horizon setting.

### 5.4. Real World Data

We applied Deep LTMLE to real world data from CIRCS. We estimated the counterfactual mean outcomes under the standard blood pressure (SBP) management strategy that controls SBP less than $140 \mathrm{mmHg}$ and the intensive blood pressure management strategy with SBP less than 120 $\mathrm{mmHg}$ after the 30 years of sustained management.

In real world applications, we often encounter with practical problems of censoring, that is loss of follow-up for some reasons. Our model can be easily generalized to cover this setting with a slight modification by adding censoring nodes. Details are described in Section $\mathrm{H}$ of Appendix.

The results were shown in Figure 3 . The average treatment effect (ATE) of the intensive management strategy over the standard management strategy first increased with a peak at 20 years after baseline and then decreased with a fluctuation. The direction and trend of ATE is consistent with the difference of empirical means of cumulative outcomes between two groups followed the two strategies.

### 5.5. Computation Details

DeepACE and Deep LTMLE were run on a GPU (Tesla T4) with 16 GB memory and LTMLE on CPU (Intel Xeon Skylake $6230 @ 2.1 \mathrm{GHz}$ ) with 40 cores and 96 GB memory. We used the R package ltmle with GLM and a super


Figure 3. Counterfactual mean outcomes and $\mathbf{9 5 \%}$ simultaneous confidence intervals according to standard and intensive treatment policies among 13,485 participants of the CIRCS.

learner (SL) library consisting of GLM, maltivariate adaptive regression spline with earth package, and xgboost for the simple synthetic data and the real world data (Lendle et al. 2017; Polley et al. 2021, Milborrow, 2023, Chen et al. 2022). Confidence intervals for LTMLE was constructed based on its estimate of the efficient influence function.

Table 3. Running time with complex synthetic data

|  | Time, sec |  |  |
| :--- | ---: | ---: | ---: |
| Model | $\tau=10$ | $\tau=20$ | $\tau=30$ |
| LTMLE (SL) | 271 | 958 | 2122 |
| DeepACE | 53 | 54 | 133 |
| Deep LTMLE $\star$ | 38 | 39 | 116 |

As shown in Table 3, Deep LTMLE leverages GPU acceleration to achieve significantly faster processing times than LTMLE, presenting a substantial computational benefit for analyses involving extensive time horizons and highdimensional time-dependent covariates.

## 6. Limitations

Our method assumes the sequential randomization and the positivity assumption on the intervention mechanism to identify the counterfactual outcome from observational data. However, to our surprise, in semi-synthetic data simulations, we found that when there is unmeasured confounding violating the sequential randomization assumption rely on, our method is very robust and could even provide robust inference. Furthermore, our proposed model does not currently address several complexities often found in real-world data, such as visiting processes, competing risks, and continuous time horizons. These challenges will be the focus of our future research efforts.

## 7. Conclusion

In this paper, we propose a variant of LTMLE that leverages the sequential learning capabilities of transformers. This approach enables simultaneous fitting of the entire LTMLE, allowing us to target the mean survival under dynamic interventions directly through weighting the loss function with cumulative inverse probabilities of intervention. The proposed method performs competitively with asymptotically efficient estimators in low-dimensional settings and exceeds the performance of existing models in high-dimensional scenarios. Scalability of our model to larger and longer datasets was implied. We applied our method to real world data and demonstrated a causal inference on the effect of sustained blood pressure management strategies on total mortality.

## Acknowledgement

This research is funded by NIH and Berkeley School of Public Health, Interdisciplinary Collaborative Research Grant. TS is supported by Fulbright scholarship program. The authors thank Dr. Ahmed Alaa at University of California, San Francisco and Berkeley for valuable discussions. The authors acknowledge the CIRCS investigators team for providing the real world data for experiments; Dr. Akihiko Kitamura at Yao City, Dr. Masahiko Kiyama at Osaka Center for Prevention of Cardiovascular Diseases, Dr. Takeo Okada at Osaka Center for Prevention of Cardiovascular Diseases, Dr. Yuji Shimizu at Osaka Center for Prevention of Cardiovascular Diseases, Dr. Hironori Imano at Kinki University, Dr. Tetsuya Ohira at Fukushima Prefeture Medical University, Dr. Kazumasa Yamagishi at Tsukuba University, and Dr. Isao Muraki at Osaka University.

## References

Bang, H. and Robins, J. M. Doubly robust estimation in missing data and causal inference models. Biometrics, 61 (4):962-973, 2005.
Bica, I., Alaa, A. M., Jordon, J., and van der Schaar, M. Estimating counterfactual treatment outcomes over time through adversarially balanced representations. In International Conference on Learning Representations, 2020.

Bickel, P., Klaassen, C., Ritov, Y., and Wellner, J. Efficient and Adaptive Estimation for Semiparametric Models. Johns Hopkins Series in the Mathematical Sciences. Springer New York, 1993. ISBN 978-0-387-98473-5.

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. Language models are few-shot learners. Advances in neural information processing systems, 33: 1877-1901, 2020.

Chen, T., He, T., Benesty, M., Khotilovich, V., Tang, Y., Cho, H., Chen, K., Mitchell, R., Cano, I., Zhou, T., Li, M., Xie, J., Lin, M., Geng, Y., Li, Y., and Yuan, J. xgboost: Extreme Gradient Boosting, 2022. URL https: //CRAN. $\mathrm{R}$-project.org/package=xgboost. $\mathrm{R}$ package version 1.7.6.1.

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., and Robins, J. Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal, 21(1):C1-C68, 2018.

Chernozhukov, V., Escanciano, J. C., Ichimura, H., Newey, W. K., and Robins, J. M. Locally robust semiparametric estimation. Econometrica, 90(4):1501-1535, 2022.

Dang, L. E., Gruber, S., Lee, H., Dahabreh, I. J., Stuart, E. A., Williamson, B. D., Wyss, R., Díaz, I., Ghosh, D., Kıcman, E., Alemayehu, D., Hoffman, K. L., Vossen, C. Y., Huml, R. A., Ravn, H., Kvist, K., Pratley, R., Shih, M.-C., Pennello, G., Martin, D., Waddy, S. P., Barr, C. E., Akacha, M., Buse, J. B., van der Laan, M., and Petersen, M. A causal roadmap for generating high-quality realworld evidence. Journal of Clinical and Translational Science, 7(1):e212, 2023.

Farajtabar, M., Chow, Y., and Ghavamzadeh, M. More robust doubly robust off-policy evaluation. In Proceedings of the 35th International Conference on Machine Learning, volume 80 of Proceedings of Machine Learning Research, pp. 1447-1456. PMLR, 10-15 Jul 2018.

Frauen, D., Hatt, T., Melnychuk, V., and Feuerriegel, S. Estimating average causal effects from patient trajectories. Proceedings of the AAAI Conference on Artificial Intelligence, 37(6):7586-7594, 2023.

Gruber, S. and van der Laan, M. J. A targeted maximum likelihood estimator of a causal effect on a bounded continuous outcome. The International Journal of Biostatistics, 6(1):Article 26, 2010. ISSN 1557-4679. doi: $10.2202 / 1557-4679.1260$.

Gruber, S. and van der Laan, M. J. Targeted minimum loss based estimation of a causal effect on an outcome with known conditional bounds. The international journal of biostatistics, 8(1):21-21, 2012. ISSN 1557-4679.

Jiang, N. and Li, L. Doubly robust off-policy value evaluation for reinforcement learning. In Proceedings of The 33rd International Conference on Machine Learning, volume 48 of Proceedings of Machine Learning Research, pp. 652-661, New York, New York, USA, 20-22 Jun 2016. PMLR.

Kallus, N. and Uehara, M. Double reinforcement learning for efficient and robust off-policy evaluation. In Proceedings of the 37th International Conference on Machine Learning, volume 119 of Proceedings of Machine Learning Research, pp. 5078-5088. PMLR, 13-18 Jul 2020.

Kennedy, E. H. Semiparametric doubly robust targeted double machine learning: A review. arXiv preprint arXiv:2203.06469, 2022.

Klaassen, C. A. J. Consistent estimation of the influence function of locally asymptotically linear estimators. The Annals of Statistics, 15(4):1548-1562, 1987.

Lendle, S. D., Schwab, J., Petersen, M. L., and van der Laan, M. J. ltmle: An R package implementing targeted minimum loss-based estimation for longitudinal data. Journal of Statistical Software, 81(1):1-21, 2017. doi: 10.18637/jss.v081.i01.

Levine, S., Kumar, A., Tucker, G., and Fu, J. Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems. arXiv preprint arXiv:2005.01643, 2020.

Li, R., Hu, S., Lu, M., Utsumi, Y., Chakraborty, P., Sow, D. M., Madan, P., Li, J., Ghalwash, M., Shahn, Z., and Lehman, L.-w. G-net: A recurrent network approach to G-computation for counterfactual prediction under a dynamic treatment regime. In Proceedings of Machine Learning for Health, volume 158 of Proceedings of Machine Learning Research, pp. 282-299. PMLR, 2021.

Melnychuk, V., Frauen, D., and Feuerriegel, S. Causal transformer for estimating counterfactual outcomes. In Chaudhuri, K., Jegelka, S., Song, L., Szepesvari, C., Niu, G., and Sabato, S. (eds.), Proceedings of the 39th International Conference on Machine Learning, volume 162 of Proceedings of Machine Learning Research, pp. 15293-15329. PMLR, 2022.

Milborrow, S. earth: Multivariate Adaptive Regression Splines, 2023. URL https://CRAN.R-project. org/package=earth. R package version 5.3.2.
Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013.

Narita, Y., Yasui, S., and Yata, K. Debiased off-policy evaluation for recommendation systems. In Proceedings of the 15th ACM Conference on Recommender Systems, RecSys '21, pp. 372-379, New York, NY, USA, 2021. Association for Computing Machinery. ISBN 9781450384582.

Petersen, M. L. and van der Laan, M. J. Causal models and learning from data: Integrating causal modeling and statistical estimation. Epidemiology (Cambridge, Mass.), 25(3):418-426, 2014.

Polley, E., LeDell, E., Kennedy, C., and van der Laan, M. SuperLearner: Super Learner Prediction, 2021. URL https://CRAN.R-project.org/ package=SuperLearner. $\mathrm{R}$ package version 2.0 28.1 .

Robins, J. A new approach to causal inference in mortality studies with a sustained exposure period-application to control of the healthy worker survivor effect. Mathematical modelling, 7(9-12):1393-1512, 1986.

Robins, J. M., Rotnitzky, A., and Zhao, L. P. Estimation of Regression Coefficients When Some Regressors Are Not Always Observed. Journal of the American Statistical Association, 89(427):846-866, 1994.

Salerno, S. and Li, Y. High-dimensional survival analysis: Methods and applications. Annual review of statistics and its application, 10:25-49, 2023.

Sutton, R. S. Learning to predict by the methods of temporal differences. Machine learning, 3:9-44, 1988.

van der Laan, M. and Rubin, D. Targeted Maximum Likelihood Learning. The International Journal of Biostatistics, 2(1), 2006.

van der Laan, M. J. and Gruber, S. Targeted Minimum Loss Based Estimation of Causal Effects of Multiple Time Point Interventions. The International Journal of Biostatistics, 8(1), 2012.

van der Laan, M. J. and Robins, J. Unified Methods for Censored Longitudinal Data and Causality. Springer Series in Statistics. Springer New York, 2003. ISBN 978-0-387-21700-0.

van der Laan, M. J. and Rose, S. Targeted Learning: Causal Inference for Observational and Experimental Data. Springer Series in Statistics. Springer, 2011. ISBN 978-1-4419-9781-4 978-1-4419-9782-1.
van der Laan, M. J. and Rose, S. Targeted Learning in Data Science: Causal Inference for Complex Longitudinal Studies. Springer Series in Statistics. Springer International Publishing, 2018.

van der Laan, M. J., Polley, E. C., and Hubbard, A. E. Super learner. Statistical Applications in Genetics and Molecular Biology, 6(1):1309-1309, 2007. ISSN 15446115 .

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention is all you need. In Advances in Neural Information Processing Systems, volume 30. Curran Associates, Inc., 2017.

Wyss, R., Yanover, C., El-Hay, T., Bennett, D., Platt, R. W., Zullo, A. R., Sari, G., Wen, X., Ye, Y., Yuan, H., Gokhale, M., Patorno, E., and Lin, K. J. Machine learning for improving high-dimensional proxy confounder adjustment in healthcare database studies: An overview of the current literature. Pharmacoepidemiology and drug safety, 31(9): 932-943, 2022. ISSN 1053-8569.

Yamagishi, K., Muraki, I., Kubota, Y., Hayama-Terada, M., Imano, H., Cui, R., Umesawa, M., Shimizu, Y., Sankai, T., Okada, T., Sato, S., Kitamura, A., Kiyama, M., and Iso, H. The Circulatory Risk in Communities Study (CIRCS): A Long-Term Epidemiological Study for Lifestyle-Related Disease Among Japanese Men and Women Living in Communities. Journal of Epidemiology, 29(3):83-91, 2019.

## A. Notation

Here we list notations used in the article.



## B. Proof

Proof of Theorem 4.2 A direct calculation shows

$$
\partial_{\varepsilon} \mathcal{L}_{t}^{\star}\left(Q_{t, \varepsilon}^{g}, V_{t+1, \varepsilon^{\star}}^{g}\right)=I_{t}(G)\left[\partial_{\varepsilon} Q_{t, \varepsilon}^{g}\right]\left[\partial_{Q_{t, \varepsilon}^{g}} \mathcal{L}_{\mathrm{bce}}\left(Q_{t, \varepsilon}^{g}, V_{t+1, \varepsilon^{\star}}^{g}\right)\right]=I_{t}(G)\left(V_{t+1, \varepsilon^{\star}}^{g}-Q_{t, \varepsilon}^{g}\right)
$$

Substitution of $\varepsilon^{\star}$ to $\varepsilon$ yields the $t$-th component of the efficient influence function (34) at $\left(Q_{\varepsilon^{\star}}^{g}, V_{\varepsilon^{\star}}^{g}, G\right)$.

## C. Review of TMLE

## C.1. Structural Causal Model

We assume each node depends on the all previous nodes in the trajectory, that is, we do not assume the Markovian property. And each node $X$ is produced from the parent nodes $p a(X)$ and independent noise random variables $U_{X}$ by a measurable
function $f_{X}: X=f_{X}\left(p a(X), U_{X}\right)$. This production function $f_{X}$ induces a conditional distribution $P_{X \mid H}$ of $X$ given $H=p a(X)$ by pushing forward the distribution of noise variable: $P_{X \mid H}(A \mid h)=\left(P_{U_{X}} \circ f_{X}^{-1}(h, \cdot)\right)(A)$ for all measurable $A \subset \mathcal{X}$, where $\mathcal{X}$ is a domain of random vector $X$. Starting from nodes without parents including noise nodes and their distributions, production functions and their causal structure, which can be described by a directed acyclic graph over the ovservables, generate the joint distribution of the observed random variables. With our particular data in longitudinal setting, we define the propensity score $\pi_{t}=P_{A_{t} \mid p a\left(A_{t}\right)}$, where $p a\left(A_{t}\right)=p a\left(A_{t}\right)$ is the patient history before the node $A_{t}$. We use the same symbol for the production function if the treatment assignment is deterministics, that is, there is no noise variable in generating the treatment node: $d \pi_{t}\left(A_{t} \mid p a\left(A_{t}\right)\right)=1$ if $A_{t}=a_{t}$ for some specific $a_{t}$.

## C.2. Causal Target Parameter and Identification

Our target parameter is the counterfactual mean of the final outcome $Y$ under the user-specified dynamic treatment policy $g=\left(g_{t}\right)$. This is the mean of counterfactual outcome which is produced by replacing $\pi_{t}$ with $g_{t}$ in the structural causal model:

$$
\psi^{g}(P)=E Y^{g}
$$

To identify this causal target paratmer from observatoinal data, we assume the following conditions of the positiviy:

$$
g \ll \pi
$$

and the sequential randomization:

$$
Y^{g} \perp A_{t} \mid p a\left(A_{t}\right) \text { for } t=1, \ldots, \tau
$$

Note that the consistency $Y=Y^{\pi}$ usually stated in the causal inference literature is a consequence of the definition of counterfactual outcome in our structural causal model. Under these identifiability conditions, this parameter is identified through $\mathrm{g}$-formula that is the mean of $Y$ under the counterfactual distribution which is given by replacing distributions $\pi_{t}$ with $g_{t}$ :

$$
E Y^{g}=E_{g} Y
$$

Then the problem reduced to the estimation of the statistical parameter:

$$
\psi(P)=E_{g} Y
$$

## C.3. TMLE

Bias correction by TMLE is based on the following first order approximation of the target functional around the true distribution $P_{0}$ (van der Laan \& Rubin, 2006; van der Laan \& Rose, 2011; Kennedy, 2022):

$$
\psi\left(\hat{P}_{n}\right)-\psi\left(P_{0}\right)=-P_{0} D^{\star}\left(\hat{P}_{n}\right)+R_{2}\left(\hat{P}_{n}, P_{0}\right)
$$

where $D^{\star}$ is called influence function and $R_{2}$ is the second order remainder. This equation is the infinite dimensional extension of Taylor expansion.

The right hand side of this equation can be further written as:

$$
-P_{n} D^{\star}\left(\hat{P}_{n}\right)+\left(P_{n}-P_{0}\right)\left[D^{\star}\left(\hat{P}_{n}\right)-D^{\star}\left(P_{0}\right)\right]+\left(P_{n}-P_{0}\right) D^{\star}\left(P_{0}\right)+R_{2}\left(\hat{P}_{n}, P_{0}\right)
$$

whose second term called empirical process term converges to zero in the rate of square root of $n$ if $D^{\star}\left(\hat{P}_{n}\right), D^{\star}\left(P_{0}\right)$ belong to the Donsker class and $D^{\star}\left(\hat{P}_{n}\right)$ converges to $D^{\star}\left(P_{0}\right)$ in $L^{2}\left(P_{0}\right)$. Given a good initial fit $\hat{P}_{n}$ of $P_{0}$, above conditions are usually satisfied and, in addition, $R_{2}\left(\hat{P}_{n}, P_{0}\right)=o_{P_{0}}\left(n^{-1 / 2}\right)$. Thus, by further using the fact about the influence function that $P_{0} D^{\star}\left(P_{0}\right)=0$, the right hand side reduced to

$$
-P_{n} D^{\star}\left(\hat{P}_{n}\right)+P_{n} D^{\star}\left(P_{0}\right)+o_{P_{0}}\left(n^{-1 / 2}\right)
$$

Now, the idea is to find $\hat{P}_{n}^{\star}$ in the close neighborhood of $\hat{P}_{n}$ that solves the empirical analog of the first term:

$$
P_{n} D^{\star}\left(\hat{P}_{n}^{\star}\right)=0
$$

By doing so, using similar arguments as above for $\hat{P}_{n}^{\star}$ instead of $\hat{P}_{n}$, we have the following.

$$
\psi\left(\hat{P}_{n}^{\star}\right)-\psi\left(P_{0}\right)=P_{n} D^{\star}\left(P_{0}\right)+o_{P_{0}}\left(n^{-1 / 2}\right)
$$

Thus, our estimator $\psi\left(\hat{P}_{n}^{\star}\right)$ is a plug in estimator and attains the efficiency bound among the asymptotically linear and regular estimators.

## C.4. Efficient influence curve

Then the efficient influence function of our target parameter is computed as follows (van der Laan \& Gruber, 2012)

$$
\begin{aligned}
D^{\star}(P) & =\sum_{t=1}^{\tau} D_{t}^{\star}(P) \\
& =\left(V_{1}^{g}-\psi_{0}\right)+\sum_{t=1}^{\tau-1} I_{t}\left(V_{t+1}^{g}-Q_{t}^{g}\right)+I_{\tau}\left(Y_{\tau}-Q_{\tau}^{g}\right) \\
& =\left(V_{1}^{g}-\psi_{0}\right)+\sum_{t=1}^{\tau-1} \mathbb{1}\left\{Y_{t-1}=0\right\} I_{t}\left(V_{t+1}^{g}-Q_{t}^{g}\right)+\mathbb{1}\left\{Y_{\tau-1}=0\right\} I_{\tau}\left(Y_{\tau}-Q_{\tau}^{g}\right) \\
& =\left(V_{1}^{g}-\psi_{0}\right)+\sum_{t=1}^{T-1} I_{t}\left(V_{t+1}^{g}-Q_{t}^{g}\right)+I_{T}\left(Y_{T}-Q_{T}^{g}\right)
\end{aligned}
$$

where $Y_{0}=0$ by definition.

## D. Convergence of Temporal Difference Learning

First, consider a flexible model $Q_{\theta}$ and corresponding $V_{t, \theta}=\mathbb{E}_{A_{t} \sim g_{t}} Q_{t, \theta}$. Initiate $\theta^{0}$ and then iteratively update by $\theta^{k+1}=\arg \min _{\theta} P \mathcal{L}\left(Q_{\theta}, V_{\theta^{k}}\right)$ for $k=2, \ldots$, till convergence. Our proof below shows that if we use a variation independent parameter space for each $Q_{t, \theta}$ and the parameter spaces contain the true $Q_{t, P}$, then in $K+2$-steps this algorithm will have converged to the true solution $Q_{P}$.

Ignoring the parameterization, but just thinking in terms of optimizing over parameter spaces, this algorithm corresponds with: initiate $V^{0}$, and then for $k=0, \ldots$, compute $Q^{k+1}=\arg \min _{Q} P \mathcal{L}\left(Q, V^{k}\right)$ and set $V^{k+1}$ as the one implied by the intervention $g$ and $Q^{k+1}$; and set $k=k+1$.

Firstly, we claim that in a nonparametric model the $t$-specific parameters $Q_{t}$ are variation independent across $t$. Consider a given $V$ (misspecified). This implies a parameter space $\left\{\mathbb{E}_{L_{t} \mid p a\left(L_{t}\right) \sim \mu_{t}\left(\cdot \mid p a\left(L_{t}\right)\right)} V_{t}: \mu_{t}\right\}$ for the regressions $Q$. The parameter space of the free parameter $\mu_{t}$ is even larger than the parameter space of functions of $p a\left(L_{t}\right)$. Therefore this appears indeed a reasonable condition. Then we can state that the parameter space over which we optimize at step $k$ of the algorithm is the cartesian product of the parameter spaces $\mathcal{Q}_{t}$ for $Q_{t}$ across $t=\tau, \ldots, 1$. Consider the $k=1$-step of the algorithm in which the outcomes are $V^{0}$ and we optimize over all the $Q \in \prod_{t=\tau}^{1} \mathcal{Q}_{t}$. Then, $Q^{1}$ is the minimizer of $Q \rightarrow P \mathcal{L}\left(Q, V^{0}\right)$. That means that the derivative w.r.t. $\varepsilon_{t}$ along a path $Q_{t}^{1}+\varepsilon_{t} h_{t}$ through $Q_{t}^{1}$ in any direction $h_{t}$ at $\epsilon_{t}=0$ should be equal to zero, across all $t=\tau, \ldots, 1$. Thus, at $\varepsilon=0$, we have

$$
\frac{d}{d \varepsilon} \sum_{t=1}^{\tau} \mathcal{L}_{t}\left(Q_{t}^{1}+\varepsilon_{t} h_{t} \mid V_{t+1}^{0}\right)=0
$$

Consider the derivative w.r.t. $\varepsilon_{Y}$. This yields the score equation $P h_{Q_{\tau}}\left(V_{\tau+1}-Q_{\tau}^{1}\right)=0$ for all $h_{Q_{\tau}}$. This implies that $Q_{\tau}^{1}=Q_{\tau, P}$. The others are some optimizer. Now, we go to step $k=2$. We now know that $V_{\tau}^{1}=V_{\tau, P}$ due to $Q_{\tau}^{1}=Q_{\tau, P}$. Therefore, at the next step, due to the derivative w.r.t. $\varepsilon_{\tau-1}$, it follows that $Q_{\tau-1}^{2}=Q_{\tau-1, P}$, while it again $Q_{\tau}^{2}=Q_{\tau}^{1}=Q_{\tau, P}$. Then, at step $k=3$, we also obtain $Q_{\tau-2}^{3}=Q_{\tau-2, P}$. In this manner, it follows that after $K+2$ steps we have $Q^{K+2}=Q_{P}$.

## E. Hyperparameter Tuning

We selected hyperparameters shown in Table 4 which optimized the empiricall loss $\mathcal{L}^{Q}+\mathcal{L}^{G}$ in the validation set which is the $30 \%$ of the entire dataset. The parameter $\alpha$ and $\beta$ for censoring mechanism balances the learning rate of $G$-parts and $Q$-parts because the complexity of $G$-parts would be simpler than $Q$-parts which involves prediction in the long-range.

Table 4. Selected hyperparameters.

| Data | Simple Synthetic Data |  |  |  | Complex Synthetic Data |  |  |  | Real World |  |  |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Model | Deep LTMLE |  |  | DeepACE |  | Deep LTMLE |  | DeepACE |  | Deep LTMLE |  |  |  |
| $\tau$ | 10 | 20 | 30 | 10 | 20 | 30 | 10 | 20 | 30 | 10 | 20 | 30 | 30 |
| Embedding dimension | 32 | 32 | 32 | 32 | 32 | 32 | 16 | 32 | 32 | 32 | 32 | 32 | 32 |
| Dropout rate | 0 | 0 | 0.1 | 0.3 | 0.2 | 0.1 | 0 | 0 | 0 | 0.3 | 0.2 | 0.2 | 0 |
| Hidden size | 64 | 64 | 16 | 8 | 4 | 4 | 64 | 32 | 16 | 4 | 4 | 4 | 16 |
| Number of Layers | 8 | 4 | 4 | 1 | 1 | 2 | 4 | 4 | 4 | 2 | 8 | 2 | 8 |
| Number of heads | 8 | 4 | 4 | - | - | - | 8 | 8 | 8 | - | - | - | 4 |
| Learning rate | $1 \mathrm{e}-04$ | $5 \mathrm{e}-04$ | $5 \mathrm{e}-04$ | $5 \mathrm{e}-03$ | $1 \mathrm{e}-02$ | $5 \mathrm{e}-03$ | $1 \mathrm{e}-03$ | $5 \mathrm{e}-04$ | $1 \mathrm{e}-04$ | $5 \mathrm{e}-04$ | $5 \mathrm{e}-04$ | $5 \mathrm{e}-04$ | $5 \mathrm{e}-04$ |
| $\alpha$ | 0.1 | 0.01 | 0.01 | 0.01 | 0.1 | 0.05 | 0.01 | 0.05 | 0.05 | 0.01 | 0.1 | 0.1 | 0.1 |
| $\beta$ | - | - | - | 0.05 | 0.05 | 0.05 | - | - | - | 0.05 | 0.05 | 0.05 | 0.01 |
| Number of epochs | 100 | 200 | 400 | 100 | 200 | 100 | 100 | 100 | 400 | 100 | 100 | 100 | 100 |

## F. Synthetic Data

## F.1. Simple Synthetic Data with Continuous Outcome

The process iteratively generates variables $W, L_{t}, A_{t}$, and $Y_{t}$ over time steps $t$, for $t=0, \ldots, \tau-1$. $W \sim \operatorname{Normal}(0,1)$. At $t=0, L_{0} \sim \operatorname{Normal}(0.1 W, 1), A_{0} \sim \operatorname{Ber}\left(\sigma\left(-0.5 W+L_{0}\right)\right), Y_{0} \sim \operatorname{Ber}\left(\sigma\left(-3+0.2 W+0.2 L_{0}-2 A_{0}\right)\right)$. For $t>0$, $L_{t} \sim \operatorname{Normal}\left(0.1 W-0.1 A_{t-1}, 1\right), A_{t} \sim \operatorname{Ber}\left(\sigma\left(-0.5+0.3 W+0.3 L_{t}+2 A_{t-1}\right)\right), Y_{t}=\sigma\left(-3+0.2 W+0.2 L_{t}-2 A_{t}\right)$, $\sigma(x)=\left(1+e^{-x}\right)^{-1}$ is the sigmoid function. We set the counterfactual treatment at all time-points to 1 and and evaluated the counterfactual mean of survival under this treatment policy.

## F.2. Simple Synthetic Data with Survival Outcome

The process iteratively generates variables $W, L_{t}, A_{t}$, and $Y_{t}$ over time steps $t$, for $t=0, \ldots, \tau-1$. $W \sim \operatorname{Normal}(0,1)$. At $t=0, L_{0} \sim \operatorname{Normal}(0.1 W, 1), A_{0} \sim \operatorname{Ber}\left(\sigma\left(-0.5 W+L_{0}\right)\right), Y_{0} \sim \operatorname{Ber}\left(\sigma\left(-3+0.2 W+0.2 L_{0}-2 A_{0}\right)\right)$. For $t>0$, $L_{t} \sim \operatorname{Normal}\left(0.1 W-0.1 A_{t-1}, 1\right), A_{t} \sim \operatorname{Ber}\left(\sigma\left(-0.5+0.3 W+0.3 L_{t}+2 A_{t-1}\right)\right), Y_{t} \sim \operatorname{Ber}\left(\sigma\left(-3+0.2 W+0.2 L_{t}-2 A_{t}\right)\right)$, with $Y_{t-1}=1$ implying $Y_{t}=1$. Here $\sigma(x)=\left(1+e^{-x}\right)^{-1}$ is the sigmoid function. We set the counterfactual treatment at all time-points to 1 and and evaluated the counterfactual mean of survival under this treatment policy.

## F.3. Complex Synthetic Data with Survival Outcome

First draw parameters $\alpha_{i}, \beta_{i} \sim \operatorname{Normal}\left((i+1)^{-1}, 0.02\right)$ and $\gamma_{i} \sim 2 * \operatorname{Binom}(0.5)-1$ for $i \in[h t]$, where $h$ is the length of time-dependency with $h=1$ corresponding to Markovian process. Then, draw error in time-dependet variables $\varepsilon_{t j}^{\ell} \sim \operatorname{Normal}(0,0.1)$ for $t \in[\tau]$ and $j \in[p]$, errors in treatment $\varepsilon_{t 1}^{A} \sim \operatorname{Normal}(0,0.2), \varepsilon_{t 2}^{A} \sim \operatorname{Normal}(0,0.05)$ for $t \in[\tau]$. For each $t \in[\tau], L_{t}=\tanh \left(\sum_{k \in[h t]} \alpha_{k} L_{t-k}+\beta_{k} \gamma_{k}\left(2 A_{t-k}-1\right)\right)+\varepsilon_{t j}^{\ell}$, then draw $A_{t}$ from an indicator function $\mathbb{1}\left\{\left(\sigma\left(s_{t}+\right)+\varepsilon_{t 2}^{A}\right)>0.5\right\}$, with $s_{t}=\tan \left(\prod_{j \in[p]} \bar{L}_{j}+\bar{A}\right)+\varepsilon_{t 1}^{A}$. The outcome $Y_{t}$ is drawn from a Bernoulli distribution of a probability $\sigma\left(p_{t}\right)$ with $p_{t}=\tan \left(\prod_{j \in[p]} \bar{L}_{j}-0.7 *(\bar{A}-0.5)\right)-4.5 . Y_{t}=1$ if $Y_{t-1}=1$ for $t>0$. We set the counterfactual treatment policy as $\mathbb{1}\left\{\sigma\left(s_{t}\right)>0.5\right\}$ for $t \in[\tau]$ and evaluated the counterfactual mean of survival under this policy.

## G. Results with Simple Synthetic Data with Survival Outcome

Results of an experiment with the simple synthetic data described in Section F. 2 was shown in Table 5 Although LTMLE's strong performance on simple synthetic data is anticipated due to reduced burden in estimating nuisance parameters from Markovian dependencies, Deep LTMLE remains highly competitive in this context, equalling LTMLE's performance. Our two targeting approaches demonstrated better bias variance trade off for the estimation of the target parameter compared to the untargeted approach. Both bias and standard deviation get improved a lot for all $\tau$ 's considered. The targeting step made a marked difference in terms of coverage probability, getting much closer to a nominal $95 \%$ coverage probability compared to the one without targeting.

Table 5. Results from simple synthetic data

| Model | $\tau=10$ | Bias <br> $\tau=20$ | $\tau=30$ | $\tau=10$ | RMSE <br> $\tau=20$ | $\tau=30$ | $\tau=10$ | Coverage <br> $\tau=20$ | $\tau=30$ | $\tau=10$ | Mean $\hat{\sigma}_{n}$ <br> $\tau=20$ | $\tau=30$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| LTMLE (GLM) | 0.0052 | 0.0045 | 0.0021 | 0.0202 | 0.0268 | 0.0308 | 0.95 | 0.94 | 0.93 | 0.02 | 0.03 | 0.03 |
| LTMLE (SL) | 0.0056 | 0.0058 | 0.0061 | 0.0203 | 0.0263 | 0.0311 | 0.91 | 0.93 | 0.91 | 0.02 | 0.02 | 0.03 |
| DeepACE | 0.0213 | 0.0462 | -0.1342 | 0.0266 | 0.0515 | 0.1397 | 1.00 | 1.00 | 1.00 | 0.19 | 0.70 | 0.70 |
| Deep LTMLE | 0.0080 | 0.0133 | 0.0090 | 0.0292 | 0.0569 | 0.0449 | 0.79 | 0.78 | 0.87 | 0.02 | 0.04 | 0.03 |
| Deep LTMLE $\dagger$ | 0.0054 | 0.0070 | 0.0080 | 0.0207 | 0.0350 | 0.0329 | 0.91 | 0.95 | 0.91 | 0.02 | 0.04 | 0.03 |
| Deep LTMLE $\star$ | 0.0053 | 0.0053 | 0.0080 | 0.0207 | 0.0361 | 0.0310 | 0.90 | 0.96 | 0.92 | 0.02 | 0.04 | 0.03 |

## G.1. Semi-Synthetic Data

As a compromise, we conducted several additional experiments with semi-synthetic data from the real world data as used in previous studies (Bica et al. 2020; Frauen et al. 2023). For this experiment, we used covariates from the Circulatory Risk in Communities Study (CIRCS) and fit outcome regression given the history through each time point using XGBoost with early stopping. Outcomes were then generated using this fitted regression model. For the experiment, we sample 1000 observations from the empirical dstribution of covariates $W, L_{t}, A_{t}$ and generate $Y_{t}$ for $t=1, \ldots, \tau$ with $\tau \in\{10,20.30\}$.

## H. Extension to Survival Analysis with Censoring

In this section, we describe the extended LTMLE model with censoring for the real world application in Section 5.4 We assume the following order of observed nodes $O=\left(W=W_{0}, L_{1}, A_{1}, C_{1}, Y_{1}, L_{2}, A_{2}, C_{2}, Y_{2}, \ldots, L_{\tau}, A_{\tau}, C_{\tau}, Y_{\tau}=Y\right)$, where $C_{t}$ are binary censoring nodes with $C_{t}=1$ indicating one being censord. Our interest is to estimate the risk of our outcome $Y_{\tau}$, the mortality of the individual. However, our observation period spans long-term, individuals are at risk of being censored. Censoring $C_{t}$ is loss of follow-up from administrative reasons, for example, move to other areas or denial of participation in the survey. We assume degenerations of nodes. When we observe a jump in $Y$ or $C$ nodes, the process halts and all nodes after the jump remain constant with the last observed values. For example, if $Y_{t}=1$, then $Y_{s}=1, C_{s}=0$, $A_{s-1}=A_{t-1}$, and $L_{s}=L_{t}$ for all $s>t$.

We constructed a Deep LTMLE similar to the one describe in Section 4 with this structure. The only difference is an additional component of censoring mechanism $G^{c}$ which is involved in the clever covariate $I_{t}$ and the loss function:

$$
\begin{aligned}
I_{t}(G) & =\prod_{s=1}^{t} \frac{d\left(g \otimes \mathbb{1}\left(C_{s}=0\right)\right)}{d\left(G_{t}^{a} \otimes G_{t}^{c}\right)}(O), \text { and } \\
\mathcal{L}(Q, V, G) & =\mathcal{L}^{Q}(Q, V)+\alpha \mathcal{L}^{G^{a}}\left(G^{a}, A\right)+\beta \mathcal{L}^{G^{c}}\left(G^{c}, C\right)
\end{aligned}
$$

where $\beta$ is an additional hyperparameter for the loss function of binary logistic loss. The counterfactual treatment on the censoring process is $\mathbb{1}\left(C_{t}=0\right)$ meaning supression of censoring. Estimates of the target parameter and the efficient influence curve for different treatment strategies are computed using Deep LTMLE, and average treatment effects (ATEs) and its EIC were computed using the delta method. Based on the estimated EICs of the target parameters at each time point $\mathrm{t}$, we constructed a simultaneous confidence intervals.


[^0]:    ${ }^{1}$ Osaka University Graduate School of Medicine, Suita, Japan ${ }^{2}$ Univerity of California, Berkeley, United States ${ }^{3}$ National Center for Global Health and Medicine, Tokyo, Japan. Correspondence to: Toru Shirakawa <shirakawa@ pbhel.med.osaka-u.ac.jp>.

