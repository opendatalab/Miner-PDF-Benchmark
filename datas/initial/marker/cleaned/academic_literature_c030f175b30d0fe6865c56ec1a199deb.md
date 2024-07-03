# A Physics And Data Co-Driven Surrogate Modeling Method For High-Dimensional Rare Event Simulation

Jianhua Xiana, Ziqi Wanga,∗
a*Department of Civil and Environmental Engineering, University of California, Berkeley, United States*

## Abstract

This paper presents a physics and data co-driven surrogate modeling method for efficient rare event simulation of civil and mechanical systems with high-dimensional input uncertainties. The method fuses interpretable low-fidelity physical models with data-driven error corrections. The hypothesis is that a welldesigned and well-trained simplified physical model can preserve salient features of the original model, while data-fitting techniques can fill the remaining gaps between the surrogate and original model predictions. The coupled physics-data-driven surrogate model is adaptively trained using active learning, aiming to achieve a high correlation and small bias between the surrogate and original model responses in the critical parametric region of a rare event. A final importance sampling step is introduced to correct the surrogate model-based probability estimations. Static and dynamic problems with input uncertainties modeled by random field and stochastic process are studied to demonstrate the proposed method.

Keywords: surrogate modeling, active learning, importance sampling, high-dimensional, rare event simulation, uncertainty quantification

## 1. Introduction

Uncertainty quantification (UQ) aims at quantifying and understanding the influence of ubiquitous uncertainties arising in science and engineering. Rare event simulation is a challenging branch of UQ with numerous engineering applications, such as the reliability of aerospace systems [1], resilience of critical infrastructures [2], and safety of nuclear power plants [3]. Sampling and surrogate modeling-based methods are two general approaches for rare event simulation, although other more specialized techniques exist [4–9].

Monte Carlo simulation [10, 11] is typically insensitive to the dimensionality and nonlinearity of computational models. However, for rare event simulation, even the advanced variance-reduction techniques [12–19]
would require thousands of samples, restricting their applications to expensive computational models.

Surrogate modeling seeks to replace the original expensive computational model with an efficient substitute. A non-intrusive data-fitting surrogate model is derived directly from training samples of the inputoutput pairs of the computational model. Examples of data-fitting surrogate models include the quadratic response surface [20, 21], polynomial chaos expansion [22–24], support vector machine [25, 26], and Gaussian process (also called Kriging) [27–32], among others. Unlike many regression models, a noise-free Gaussian process is an exact interpolation model, i.e., the predictions at the training points are exact. For non-training points, the Gaussian process offers estimations of prediction variability [33–35]. This feature facilitates the application of active learning, such that the training set can be adaptively enriched to reduce prediction variability for specified quantities of interest, resulting in improved accuracy and efficiency for Gaussian process-based rare event simulation [28, 29]. The active learning-based metamodeling approach can be further combined with advanced sampling techniques [30, 31], or adapted to estimate probability distribution functions [32].

Despite the remarkable success of Gaussian process-based methods in various UQ applications, the model training becomes increasingly challenging, ultimately infeasible, with a growing number of input variables–a phenomenon known as the curse of dimensionality [36]. To alleviate this problem, specialized unsupervised [37–40] and supervised [41–44] dimensionality reduction techniques have been proposed to couple with Gaussian process modeling. However, the effectiveness of these techniques is problem-dependent. More critically, many real-world high-dimensional problems do not admit simple low-dimensional representations
[45]. Qualitatively speaking, for a "high-dimensional input–low-dimensional output" problem, an "optimal" dimensionality reduction is the computational model itself. It follows that constructing an effective dimensionality reduction can be as challenging as finding an accurate high-dimensional surrogate model. An alternative approach is to inject domain/problem-specific prior knowledge into the surrogate modeling process. This idea is reflected in the emerging paradigms of scientific machine learning [46–49] and multi-fidelity UQ [50–52], enabling them to handle high-dimensional problems.

In this paper, we leverage physics-based surrogate modeling to solve high-dimensional rare event estimation problems. This idea is under the broad umbrella of multi-fidelity UQ. A physics-based surrogate model can be adapted from the original high-fidelity model in various ad hoc ways, such as domain-specific simplifications [53–55], reduced-order modelings [56–58], and relaxations of numerical solvers [50]. In this study, we address static and dynamic problems with a random field/process as input, typically discretized by 1,000 random variables. We construct physics-based surrogate models equipped with the properties of (i) parsimonious: the surrogate model is parameterized by a few tunable control parameters, and (ii) compatible with high-dimensional input uncertainties: the surrogate model can accept high-dimensional input uncertainties either directly as input of the model or indirectly through filtering and coarse-graining operations. For example, the classic equivalent linearization method [59, 60] for nonlinear random vibration analysis involves constructing linear physical models with random processes as input and output. Therefore, the equivalent linearization method can be reformulated into a physics-based surrogate modeling approach for nonlinear random vibration problems [61]. In other engineering applications such as computational fluid dynamics
[53], aerodynamic design [54], and climate modeling [55], there exist various domain-specific approaches in constructing simplified physics-based models.

Physics-based surrogate models may have inherent errors due to simplifications; therefore, it is promising to introduce a data-driven error correction to fill the gap between the surrogate and original model predictions. This idea has been investigated recently in [62, 63], where an active learning-based Gaussian process is trained to correct the low-fidelity model predictions. Inspired by the success of existing works, this study is devoted to low probability estimations with high-dimensional input uncertainties. Different from existing works [62, 63], we construct the data-driven error correction as a function of the output of the physics-based surrogate model, thereby mitigating the curse of dimensionality associated with high-dimensional input uncertainties. Three critical ingredients–parametric optimization for physics-based surrogate models, heteroscedastic Gaussian process for error corrections, and active learning for effective training–are leveraged to construct and train coupled physics-data-driven surrogate models. Finally, one can apply an importance sampling to couple the surrogate model simulations with limited evaluations of the original model, known as multi-fidelity importance sampling [51, 52]. The common practice of multi-fidelity importance sampling uses parametric distribution models such as the Gaussian mixture as the importance density, which scales poorly with dimensionality [14]. In this work, we adopt an importance sampling formulation [61] tailored to high-dimensional rare event simulations.

This paper is organized as follows. Section 2 introduces the general formulation of the coupled physicsdata-driven surrogate model. Section 3 develops a training process for the surrogate model, including optimization of parametric physical models, error corrections using an heteroscedastic Gaussian process, and adaptive training by active learning. Section 4 introduces an importance sampling scheme to correct the surrogate model-based probability estimations. Section 5 demonstrates the performance of the proposed method for high-dimensional rare event simulation problems. Section 6 discusses limitations. Section 7 provides concluding remarks. The implementation details are provided in Appendix A.

## 2. Coupled Physics-Data-Driven Surrogate Model

Consider an end-to-end computational model M : x ∈ R
n 7→ y ∈ R that maps a n-dimensional input x into a 1-dimensional output y. The input x is an outcome of a random vector X defined in the probability space (R
n, Bn, PX), where Bn is the Borel σ-algebra on R
n, and PX is the probability measure of X with the distribution function fX. The output y is a performance variable such that it defines the rare event of interest through {y ≤ 0}, without loss of generality. Since the source of randomness is from X, the rare event probability is typically formulated in the space of X, expressed by PX(M(X) ≤ 0). This problem is challenging in real-world applications, because (i) the dimension of x is high, (ii) the computational model M involves expensive physics-based simulations, and (iii) the probability to be estimated is small. To reduce the computational cost of M, we construct a simplified (end-to-end) computational model expressed by:

$$\begin{array}{l}{{y_{p}=({\mathcal{M}}_{p}\circ\psi)({\mathbf{x}};{\mathbf{\theta}}_{p})\,,}}\\ {{{\mathcal{M}}_{p}:{\mathbf{x}}^{\prime}\in\mathbb{R}^{n^{\prime}}\mapsto y_{p}\in\mathbb{R}\,,}}\\ {{\psi:{\mathbf{x}}\in\mathbb{R}^{n}\mapsto{\mathbf{x}}^{\prime}\in\mathbb{R}^{n^{\prime}}\,,n^{\prime}\leq n\,,}}\end{array}$$
$$\left(1\right)$$

where Mp represents a cheaper physics-based model derived from the original model M, ψ is a filtering or coarse-graining function of the input x, "◦" denotes function composition, and θp are tunable parameters of Mp and/or ψ. Depending on the selection of Mp, the filtering function ψ can be a trivial identity mapping if Mp and M share the same input space, or it can be a dimensionality reduction mapping if Mp is defined on a coarser/different input space. However, it is important to notice that Mp ◦ ψ and M share the same source of randomness from X, enabling a tuning of Mp ◦ ψ (via adjusting θp) to maximize the statistical correlation between Y and Yp.

To improve the accuracy of Eq. (1), a data-driven error correction can be introduced, leading to a coupled physics-data-driven surrogate model expressed by:

$$\hat{y}=y_{p}+\epsilon(y_{p};\theta_{\epsilon})=({\mathcal{M}}_{p}\circ v)$$

yˆ = yp + ϵ(yp; θϵ) = (Mp ◦ ψ)(x; θp) + (ϵ ◦ Mp ◦ ψ)(x; θp, θϵ), (2)

$${}_{p})+(\epsilon\circ\mathcal{M}_{p}\circ\psi)(\mathbf{x};\theta_{p},\theta_{\epsilon})\,,$$
$$\left({\boldsymbol{2}}\right)$$

3 where c : y, E R → ε E R is the error correction function constructed using data-fitting methods, and θ c are parameters of the data-fitting model.  It is worth highlighting that the input of the error correction function is the output of the physics-based surrogate model. This construction is different from existing works [62, 63],
where the error correction term was constructed on the product space of x and x ′ . The methodology of [62, 63] may face difficulties for problems with high-dimensional input uncertainties, due to the weak scalability of conventional data-fitting methods such as Gaussian process and polynomial regression [36]. In comparison, our construction of the surrogate model can mitigate the curse of dimensionality. However, it comes with a price of having inherent noises in the error correction term, even at the training points of y p .

This is because the mapping from y p to y can be one-to-many. An intuitive restatement is that the physicsbased surrogate model cannot capture all details of the original model. To quantify and mitigate the impact of the inherent noises, we use the heteroscedastic Gaussian process [64–66] to model ε ( y p ). This differs from the noise-free and homoscedastic Gaussian process models, as the heteroscedastic Gaussian process model no longer performs exact interpolations and the noise is input-dependent.



Figure 1 presents a schematic of the proposed surrogate modeling method for rare event simulation.

The technical details for optimizing the physics-based surrogate and error correction models are introduced in Sections 3.1 and 3.2, respectively. The active learning approach for efficient surrogate model training is described in Section 3.3. Section 4 details the importance sampling method for rare event probability estimations.

## 3. Training Of The Coupled Physics-Data-Driven Surrogate Model 3.1. Optimization Of Parametric Physical Models

In physics-based surrogate modeling, the response predictions of the surrogate model can be inaccurate but still be mildly/highly correlated with that of the original model. The statistical correlation between the surrogate and original model responses has a decisive impact on the noise of the error correction term (see Figure 2 for a simple illustration)–higher correlation indicates smaller noise. Pearson, Spearman's Rank, and Kendall's Tau correlation coefficients are popular indices for quantifying the correlation between two random variables [67]. The Pearson correlation coefficient can only reflect the linear correlation, while the Spearman's Rank and Kendall's Tau correlation coefficients can handle the nonlinear dependency. In our context, the physics-based surrogate model, by construction, is a simplification of the original model. Thus, a mildly nonlinear correlation is expected. Consequently, the Pearson correlation coefficient is sufficient. The Spearman's Rank and Kendall's Tau correlation coefficients can be readily implemented into the proposed surrogate modeling method, but we did not observe an improvement in performance for the numerical examples we have studied. It is worth mentioning that mutual information [68, 69] is a more general metric for measuring dependency between two random variables, but the sample estimate of mutual information involves additional assumptions on the joint distributions.



Because rare event probabilities are dominated by conditional distributions, the correlation between Y
and Yp generated by X ∼ fX(x) may not be an ideal objective for optimizing the surrogate model. The issue is that limited samples from fX(x) are unlikely to fall near to the boundary of the rare event, where most of the misclassifications happen. In this work, we adopt active learning to adaptively enrich the training set D = {(x i,M(x
(i)))} toward the critical region around {M(x) = 0}. Using the training set D, the sample correlation coefficient emphasizes the contribution from the rare event. This is essentially equivalent to redefining the correlation between M(X) and (Mp ◦ ψ)(X) using an active learning-controlled importance sampling distribution rather than the original fX(x). To summarize, the optimization for the physics-based surrogate model (Mp ◦ ψ)(x; θp) is formulated as:

$$\theta_{p}^{*}=\arg\operatorname*{max}_{\theta_{p}}\rho_{Y Y_{p}}(\theta_{p}|{\mathcal{D}})$$
$$\begin{split}&\boldsymbol{\theta}_{r}\\ &=\operatorname*{arg\,max}_{\boldsymbol{\theta}_{p}}\frac{\langle(\mathcal{M}(\boldsymbol{X})-\langle\mathcal{M}(\boldsymbol{X})\rangle_{\mathcal{D}})\left((\mathcal{M}_{p}\circ\psi)(\boldsymbol{X};\boldsymbol{\theta}_{p})-\langle(\mathcal{M}_{p}\circ\psi)(\boldsymbol{X};\boldsymbol{\theta}_{p})\rangle_{\mathcal{D}}\right)_{\mathcal{D}}}{\sqrt{\langle(\mathcal{M}(\boldsymbol{X})-\langle\mathcal{M}(\boldsymbol{X})\rangle_{\mathcal{D}})^{2}\rangle_{\mathcal{D}}\left\langle((\mathcal{M}_{p}\circ\psi)(\boldsymbol{X};\boldsymbol{\theta}_{p})-\langle(\mathcal{M}_{p}\circ\psi)(\boldsymbol{X};\boldsymbol{\theta}_{p})\rangle_{\mathcal{D}})^{2}\right\rangle_{\mathcal{D}}}}\,,\end{split}\tag{3}$$

where ⟨·⟩ denotes sample mean.

Before solving Eq. (3), we need to design θp for the physics-based surrogate model, i.e., determine which parameters are tunable. For specific applications, engineering judgement can be used to design θp. A more objective approach is to adopt a parsimonious principle to select a minimum number of parameters that can achieve a relatively high maxθp ρY Yp
(θp|D). This principle can be materialized as an incremental approach to start with a single tunable parameter and iteratively augment if maxθp ρY Yp
(θp|D) can be significantly improved. In the simulation test cases of civil and mechanical systems, we have investigated the use of elastic modulus, damping ratio, stiffness, and yield displacement as tunable parameters, where maxθp ρY Yp
(θp|D)
can typically achieve 0.95.

Finally, the optimization in Eq. (3) can be solved by gradient-free metaheuristic algorithms [70]. Provided with a training set D, solving Eq. (3) does not involve additional simulations of the original model, but it requires simulations of the physics-based surrogate model. If D is enriched by active learning, Eq. (3) needs to be re-solved; the solution from the previous training set can be used as a warm initial guess. 3.2. Error corrections using heteroscedastic Gaussian process Given a training set D = {(x i,M(x
(i)))} and the solution of Eq. (3), we obtain the training set for the error correction, Dϵ = {(y
(i)
p , ε(i))}, where y
(i)
p = (Mp ◦ψ)(x
(i); θ
∗
p
) and ε
(i) = M(x
(i))−(Mp ◦ψ)(x
(i); θ
∗
p
).

Using Dϵ, we train a heteroscedastic Gaussian process: [64–66] to model ϵ(yp), expressed by:

$$\epsilon(y_{p};\theta_{\epsilon})=f(y_{p};\theta_{f})+\tau(y_{p};\theta_{\tau})\,,$$
ϵ(yp; θϵ) = f(yp; θf ) + τ (yp; θτ ), (4)
where θϵ = θf ∪ θτ , f(yp) ∼ GP(µf (yp), kf (yp, y′p
); θf ) is a Gaussian process with hyperparameters θf to model the mean µf (yp) and kernel kf (yp, y′p
), τ (yp) ∼ N (0, exp(g(yp))) is an input-dependent Gaussian noise with zero mean and variance exp(g(yp)), and g(yp) ∼ GP(µg, kg(yp, y′p
); θg) is another Gaussian process with hyperparameters θg to model the mean µg and kernel kg(yp, y′p
).

The introduction of the heteroscedastic Gaussian noise is essential in this study because the mapping from yp to y can be one-to-many. The use of heteroscedastic Gaussian process comes with a price of increasing the number of hyperparameters, and the analytical marginal likelihood and prediction equations for the homoscedastic Gaussian process are no longer useful [64–66]. The hyperparameters θf and θg can be approximated by maximizing the following lower bound of the exact marginal likelihood [64]:

$$F(\mu,\Sigma)=\log\!f_{N}(e;{\bf0},K_{f}+R)-\frac{1}{4}\mathrm{tr}(\Sigma)-\mathrm{KL}(f_{N}(g;\mu,\Sigma)||f_{N}(g;\mu_{g}{\bf1},K_{g}))\,,$$

where µ and Σ are the variational mean vector and covariance matrix to be determined alongside with the hyperparameters θf and θg; ε = [ε
(1), ε(2)*, ...*]
⊺ are from the training set Dϵ; 0 and 1 are vectors of zeros and

$$\left(5\right)$$

6

ones; Kf and Kg are respectively the covariance matrices of the Gaussian processes f(yp) and g(yp); R is a
diagonal matrix with diagonal entries Rii = exp(µi − Σii/2); fN denotes the probability density function of
a multivariate Gaussian distribution; tr(·) denotes matrix trace; and KL(*·||·*) denotes the Kullback–Leibler divergence between two probability density functions.
Once the hyperparameters θf and θg are estimated, the predictions for the mean and variance of ϵ(y
∗
p
)
at y
∗
p are obtained from [64]:
$$\mu_{\epsilon}(y_{p}^{*})={\mathbf{k}}_{f*}^{\mathsf{T}}({\mathbf{K}}_{f}+{\mathbf{R}})^{-1}{\boldsymbol{\varepsilon}}\,,$$
−1ε , (6)
and

$\nabla f=-\nabla f$. 
$\mathbf{M}$
σ 2 ϵ (y ∗ p ) = exp k ⊺ g∗ (Λ − 1 2 I)1 + µg + kg∗∗ − k ⊺ g∗ (Kg + Λ −1) −1kg∗ 2 ! + kf∗∗ − k ⊺ f∗ (Kf + R) −1kf∗ , (7) ∗ ∗ (1) (2)

respectively, where kf∗∗ = kf (y p
, y∗
p
), kg∗∗ = kg(y p
, y∗
p
), kf∗ = [kf (y p , y∗
p
), kf (y p , y∗
p
)*, ...*]
⊺ and kg∗ = [kg(y
(1)
p , y∗
p
), kg(y
(2)
p , y∗
p
)*, ...*]
⊺
, I is the identity matrix, and Λ is a positive semi-definite diagonal matrix introduced to re-parameterize µ and Σ in a reduced order.



The mean µϵ(y
∗
p
) can be used as the prediction of the surrogate modeling error at y
∗
p
, and σ 2 ϵ
(y
∗
p
) quantifies the uncertainty of this prediction. The latter quantity is desirable in active learning. It is worth noting that the roles of the heteroscedastic Gaussian process involve quantifying the noise and correcting the (mean)
predictions of the physics-based surrogate model (see Figure 3); it cannot reduce the noise.

3.3. Adaptive training by active learning Given an initial training set D = {(x
(i),M(x
(i)))}
N0 i=1 ≡ Dx × Dy, we sequentially train the physics-based surrogate model yp = (Mp◦ψ)(x; θp) and the error correction function ϵ(yp; θϵ) to obtain the initial surrogate model ˆy = (Mp ◦ ψ)(x; θp) + ϵ(yp; θϵ). Subsequently, we initiate an active learning process to iteratively enrich the training set D and update the surrogate model. Hereafter, we develop an active learning process tailored to the physics-data-driven surrogate modeling.

Provided with the current surrogate model, we first define a critical learning region Ωc as:

$$\Omega_{e}=\left\{\mathbf{x}\in\mathbb{R}^{n}:\frac{|y_{p}+\mu_{e}(y_{p})|}{\sigma_{e}(y_{p})}\leqslant\delta,\ \ y_{p}=(\mathcal{M}_{p}\circ\psi)(\mathbf{x};\mathbf{\theta}_{p})\right\}\,,$$
$$({\boldsymbol{\delta}})$$

where δ > 0 is a cutoff value for the learning region, and µϵ(yp) and σϵ(yp) are respectively the mean and standard deviation of the Gaussian process error correction at yp.

Next, we generate a candidate training set Xc = {x
(i)}
N
i=1 through:

$$({\mathfrak{g}})$$
$$\mathbf{X}^{(i)}\sim\mathbb{I}_{\Omega_{c}}\left(\mathbf{x}\right)f_{\mathbf{X}}(\mathbf{x})\,,$$
$$(10)$$
(x) fX(x), (9)
where IΩc
: R
n *7→ {*0, 1} is an indicator function for {x ∈ Ωc} and the normalizing constant for the density IΩc
(x) fX(x) is omitted for simplicity. To reduce surrogate model simulations and improve the scalability toward low probability estimations, the sequential Monte Carlo [17–19] is used to generate Xc.

Given Xc, the next training point x
∗is identified by:

$$\mathbf{x}^{*}=\operatorname*{arg\,max}_{\mathbf{x}\in\mathcal{X}_{c}}\left(\operatorname*{min}_{y_{p}^{\prime}\in\mathcal{Y}_{p}}\|y_{p}-y_{p}^{\prime}\|\right),\;\;y_{p}=(\mathcal{M}_{p}\circ\psi)(\mathbf{x};\mathbf{\theta}_{p})\,,$$
$1\cdot i$=? 
where Yp = {yp = (Mp ◦ ψ)(x; θp) : x ∈ Dx} is a set of yp predictions from existing training samples. This
equation picks the point in Xc that differs (in terms of yp) the most from the existing training points, aiming
to achieve sparsely distributed training points in the space of yp. This learning criterion is a relaxation of the
classic U-function-based learning [29] through introducing additional, seemingly redundant, distance-based
selection to enforce sparsity. This relaxation is necessary because the prediction uncertainty term σϵ(yp)
of the U-function, which influences the "sparsity" of the U-function-based training point selection, is not
only affected by the distance to existing training points, but also contributed, sometimes dominantly, by
the inherent noise of the surrogate model. In the conventional application [29–31] of active learning-based
Gaussian process modeling, the training data does not have inherent stochastic noise, and the distancebased selection in Eq. (10) can be unnecessary. Incidentally, the constructions of Eq. (8) and Eq. (9) are
still meaningful even for noise-free scenarios, because they facilitate the use of efficient sampling methods
to identify the low-probability critical region to propose training points.
Provided with the next training point x
∗, the original model is simulated to obtain y
∗ = M(x
∗), the
training set D is augmented to include (x
∗, y∗), and the surrogate model is updated. The learning process is
stopped if the mean prediction is stable and/or the prediction uncertainty is small [71, 72]. In our context, the inherent noise originated from the imperfection of the physics-based surrogate model cannot be reduced through training. Additionally, the magnitude of this inherent noise varies with the problem. Thus, the conventional prediction uncertainty-based stopping criterion is not suitable. To address this, we adopt a
stopping criterion that monitors the stability of prediction uncertainty, expressed as follows:
$$\frac{\left|\hat{P}_{\Delta}^{(m+1)}-\hat{P}_{\Delta}^{(m)}\right|}{\hat{P}_{\Delta}^{(m+1)}}\leqslant\eta,\,\,\,m=0,1,\ldots,$$
⩽ *η, m* = 0, 1*, ... ,* (11)
$$(11)$$
where Pˆ
(m)
∆ = Pˆ+ − Pˆ− measures the prediction uncertainty, and Pˆ+ and Pˆ− are respectively the upperand lower- confidence limits of the rare event probability at the m-th learning step, estimated from the surrogate models yp +µϵ(yp)−σϵ(yp) and yp +µϵ(yp) +σϵ(yp), respectively. The mechanism of the stopping criterion is that the epistemic uncertainty from insufficient training is minimized when Pˆ
(m)
∆ is stabilized; the remaining component of Pˆ
(m)
∆ is the aleatory uncertainty that cannot be reduced by training, unless another physics-based surrogate model is used.

The implementation details for the training of the coupled physics-data-driven surrogate model are presented in Appendix A.19. Due to the presence of inherent noises, there is no guarantee that the probability 8 prediction from the surrogate model will converge to the true value. To address this issue, a final importance sampling step will be introduced in the following section.

## 4. Importance Sampling Using The Coupled Physics-Data-Driven Surrogate Model

The target rare event probability can be formulated as

$$P=\int_{\mathbf{x}\in\mathbb{R}^{n}}\mathds{1}_{\leq0}\left(\mathcal{M}(\mathbf{x})\right)f_{\mathbf{X}}(\mathbf{x})\mathrm{d}\mathbf{x}\,.\tag{12}$$  The importance sampling rewrites the integral in Eq. (12) by introducing an importance density $h(\mathbf{x})$, i.e.,
$$P=\int_{\mathbf{x}\in\mathbb{R}^{n}}\mathbb{I}_{\leq0}\left({\mathcal{M}}(\mathbf{x})\right){\frac{f_{\mathbf{X}}(\mathbf{x})}{h(\mathbf{x})}}h(\mathbf{x})\mathrm{d}\mathbf{x}\,.$$
h(x)dx . (13)
The support of the importance density h(x) should cover the rare event, and the optimal importance density
is [10]
$$h^{*}(\mathbf{x})={\frac{\mathbb{I}_{\leq0}\left({\mathcal{M}}(\mathbf{x})\right)f_{\mathbf{X}}(\mathbf{x})}{P}}\,.$$
P. (14)
Due to the high correlation between the original and surrogate model responses, it is tempting to use the
following importance density from the surrogate model as an approximation for the optimal density.
$${\hat{h}}(\mathbf{x})={\frac{\mathbb{I}_{\leq0}\left({\hat{\mathcal{M}}}(\mathbf{x};\mathbf{\theta}_{p},\mathbf{\theta}_{\epsilon})\right)f_{\mathbf{X}}(\mathbf{x})}{{\hat{P}}}}\,,$$
$$(12)$$
$$(13)$$
$\left(14\right)^2$
$$(15)$$

$$(16)$$
Pˆ, (15)
where Mˆ (x; θp, θϵ) ≡ (Mp ◦ ψ)(x; θp) + µϵ((Mp ◦ ψ)(x; θp); θϵ) is the integrated surrogate model, and Pˆ is its rare event probability. However, there is no guarantee that the target rare event is an improper subset of the support of hˆ(x). Therefore, hˆ(x) cannot be directly employed as an importance density. One remedy is to replace the binary indicator function in Eq. (15) by a smooth approximation [17, 61], so that hˆ(x)
becomes nonzero everywhere. This approach requires the tuning of a relaxation parameter associated with the smooth approximation of the indicator function.

An alternative remedy, which is adopted in this paper, is to use the following identity derived from properties of conditional probability [61]:

$$P=c_{P}\cdot{\hat{P}}\equiv{\frac{\int_{\mathbf{x}\in\mathbb{R}^{n}}\mathbb{I}_{\leq0}\left({\mathcal{M}}(\mathbf{x})\right){\hat{h}}(\mathbf{x})\mathrm{d}\mathbf{x}}{\int_{\mathbf{x}\in\mathbb{R}^{n}}\mathbb{I}_{\leq0}\left({\hat{\mathcal{M}}}(\mathbf{x};\theta_{p},\theta_{\epsilon})\right)h^{*}(\mathbf{x})\mathrm{d}\mathbf{x}}}\,{\hat{P}}\,,$$

where cP is the correction factor for the surrogate model-based rare event probability estimation. The numerator represents the conditional probability of the original rare event given the surrogate rare event, while the denominator represents the conditional probability of the surrogate rare event given the original rare event. Ideally, the correction factor cP should be close to 1; therefore, cP can be used as a performance measure of the surrogate model. The conditional probabilities in Eq. (16) can be estimated by Monte Carlo simulation with Markov Chain Monte Carlo algorithms [73, 74] to generate samples from h
∗(x) and hˆ(x). For a well-trained surrogate model, the overlap between h
∗(x) and hˆ(x) is expected to be significant; consequently, the computational cost to estimate cP would be small. However, theoretically speaking, Eq. (16) implies that the surrogate model solution Pˆ can be highly accurate even when the surrogate rare 9 event does not largely overlap with the actual rare event; this is illustrated by Figure 4. Finally, the

 implementation details of the importance sampling using Eq. (16) are presented in Appendix A.20.

## 5. Numerical Examples

In this section, we will investigate (1) a static problem of a linear elastic cantilever beam with material properties modeled by a Gaussian random field, (2) a dynamic problem of a nonlinear viscous damper under white noise excitation, and (3) a dynamic problem of a multi-degree-of-freedom hysteretic system under white noise excitation. Three schemes are investigated to construct physics-based surrogate models.

Specifically, homogenization of material properties is considered in the first example, statistical linearization is used in the second example, and relaxation of the numerical solver is adopted in the third example.

## 5.1. Example 1: A Linear Elastic Cantilever Beam

Consider a linear elastic cantilever beam of length 5m and width 2m subjected to 20 evenly spaced concentrated loads on the upper edge with magnitudes Q = 500kN, shown in Figure 5. The Poisson ratio of the beam is ν = 0.3. The reference/original computational model is represented by a discretization of the beam into 50 × 20 = 1000 four-node quadrilateral elements, and the elastic modulus of the beam is characterized by a homogeneous random field E(*x, y*) with a discretization of 1000 Gaussian random variables compatible with the spatial discretization. The autocorrelation function of the Gaussian random field is modeled by the isotropic exponential model RE(∆x, ∆y) = exp −
q∆2x + ∆2y/lwith the correlation length l = 10m.

The mean value and standard deviation of the marginal Gaussian distribution are µE = 200GPa and σE = 30GPa, respectively. The physics-based surrogate model is constructed via a simple homogenization of the random field of the elastic modulus:

$$E_{p}=a_{E}\bar{E}+b_{E}\,,$$
$$\left(17\right)$$
$$-\;d_{A}\leq0\}\;,$$
Ep = aEE¯ + bE , (17)
where {aE, bE} = θp are tunable parameters of the physics-based surrogate model, and E¯ represents the average of the 1000 Gaussian random variables. The initial values of aE and bE are set to be 1 and 0, respectively. The rare event of interest is defined as the vertical displacement of point A exceeds a prescribed threshold of 0.0032m, expressed by
{y = 0.0032 − dA ≤ 0} , (18)
where dA is the vertical displacement of point A.



The performance of the proposed method is investigated across different sizes of the initial training set, N0 = 30, 50, 100. We found that 30 initial points are typically required for stable training. During the active learning process, around 33 new training points are identified, insensitive to N0. This is expected because the initial training set may not offer sufficient information on the rare event–starting from 30 or 100 training points may not make much difference. The heteroscedastic Gaussian process model for the error correction at the final learning stage is shown in Figure 6. It is seen that the heteroscedastic Gaussian process can model the noisy errors. The optimization histories of the correlation coefficient ρ, the parameter bE, and the prediction uncertainty Pˆ∆ = Pˆ+ − Pˆ− are shown in Figure 7. The scatter plots of yp and yp + ϵ(yp) against y are shown in Figure 8. It is seen that the response predictions of the physics-based surrogate model are highly correlated with the responses of the original model, and the data-driven error correction can improve the bias of the surrogate predictions. To estimate the statistical variability of the proposed surrogate modeling method, the box plot of probability estimations using 10 independent runs is shown in Figure 9. It is observed that the method has a small but noticeable bias for rare event probability estimations. Furthermore, increasing the number of initial training points may not improve the prediction bias and variability. Therefore, using 30 initial training points seems to be ideal for the current problem. The first quartile, median, and third quartile of the rare event probability estimations are presented in

 Table 1. Finally, importance sampling is implemented to improve the probability estimation. To achieve a coefficient of variation of 5%, 400 runs of the original model is typically required. The final probability estimate ranges from 3.5 × 10−5to 4.0 × 10−5, with a correction factor cP between 1.1 and 1.6.







Consider an oscillator with nonlinear viscous damper under a Gaussian white noise excitation with the equation of motion expressed as mu¨(t) + cu˙(t) + ku(t) + cdsign( ˙u(t))|u˙(t)| αd = −mu¨g(t), (19)
where m = 3000kg, c = 3000N/(m/s), and k = 3 × 105N/m are the mass, damping, and stiffness of the oscillator, respectively, u(t), ˙u(t), and ¨u(t) are the displacement, velocity, and acceleration of the oscillator, respectively, cd = 800N/(m/s)αdand αd = 0.3 are the damping coefficient and velocity exponent of the nonlinear viscous damper, respectively, sign(·) is the sign function, and ¨ug(t) is the acceleration excitation.

The excitation has a duration of 15 seconds. Using the spectral representation method [75], the white noise can be discretized into a finite set of Gaussian variables:

$$\ddot{u}_{g}(\mathbf{X},t)=\sum_{i=1}^{D/2}\sqrt{2S_{0}\Delta\omega}\left(X_{i}\cos(\omega_{i}t)+\bar{X}_{i}\sin(\omega_{i}t)\right)\,,\tag{20}$$
$${}^{d}=-m{\ddot{u}}_{g}(t)\;,$$
$\bigcup_{i=1}^{\mathbb{L}}J_{i}$
where Xi and X¯i, i = 1, 2*, ..., D/*2, are mutually independent standard normal variables, D = 1000, ∆ω =
2ωmax/D is the frequency increment with ωmax = 25π being the upper cutoff angular frequency, ωi =
(i − 0.5)∆ω is the discretized frequency points, and S0 = 5 × 10−3m2/s 3is the intensity of the white noise.

13 To obtain the physics-based surrogate model, the nonlinear equation of motion shown in Eq. (19) is linearized into mu¨(t) + (c + ce) ˙u(t) + ku(t) = −mu¨g(t), (21)
where {ce} = θp is the equivalent damping coefficient used as the tuning parameter of the physics-based surrogate model. The rare event of interest is defined as the peak absolute displacement of the oscillator exceeding a threshold of 0.06m, expressed by

$$\left\{y=0.06-\operatorname*{sup}_{t\in[0,15]}|u(t)|\leq0\right\}\,.$$
$$(22)$$

. (22)
The initial value of ce for optimization is determined by the traditional statistical linearization method [76].

The coupled physics-data-driven surrogate model is trained using 30, 50, and 100 initial samples and around 34 active learning samples. The heteroscedastic Gaussian process model for error correction at the final learning stage is shown in Figure 10. The optimization histories of the correlation coefficient ρ, the equivalent damping coefficient ce, and the prediction uncertainty Pˆ∆ = Pˆ+ − Pˆ− are shown in Figure 11. The scatter plots of yp and yp + ϵ(yp) against y are shown in Figure 12. The box plot of probability estimations using 10 independent runs of the proposed surrogate modeling method is shown in Figure 13, and the first quartile, median, and third quartile of the probability estimations are presented in Table 1.

Applying importance sampling, the final probability estimate ranges from 2.6 × 10−7to 2.8 × 10−7, with a correction factor between 1.2 and 1.4, based on 400 runs of the original model.









5.3. Example 3: A multi-degree-of-freedom hysteretic system Consider a 6-degree-of-freedom shear-type hysteretic system under ground motion excitation, shown in Figure 14. The mass and initial stiffness of each storey are mi = 8000kg and ki = 1×107N/m, i = 1, 2*, ...,* 6, respectively. Rayleigh damping is assumed for the hysteretic system with a damping ratio of 5% for the 1st and 6th mode of the system. The restoring force of each storey is described by the Bouc-Wen model [77] as follows:
fi(t) = αikiui(t) + (1 − αi)kizi(t), (23)

$$f_{i}(t)=\alpha_{i}k_{i}u_{i}(t)+(1-\alpha_{i})k_{i}z_{i}(t)\,,$$



$$(23)$$
$$\begin{array}{c}{{{}_{J i\,(t)}=\alpha_{i i}\kappa_{i}u_{i}(t)+(1-\alpha_{i})\kappa_{i}z_{i}(t)\,,}}\\ {{{}}}\\ {{{}}}\\ {{{}\dot{z}_{i}(t)=g_{i}(\dot{u}_{i}(t),z_{i}(t))=\phi_{i}\dot{u}_{i}(t)-\varphi_{i}\left|\dot{u}_{i}(t)\right|z_{i}(t)\left|z_{i}(t)\right|^{\gamma_{i}-1}-\psi_{i}\dot{u}_{i}(t)\left|z_{i}(t)\right|^{\gamma_{i}}\,,}}\end{array}$$
$$(24)$$
γi, (24)
where αi = 0.1 is the stiffness reduction ratio of the i-th storey; ui(t), ˙ui(t), and zi(t) are the relative displacement, relative velocity, and the hysteretic displacement of the i-th storey, respectively; ϕi = 1, φi = ψi = 1/(2x γi yi ), and γi = 1 are the shape parameters of the hysteresis loop; and xyi = 1.25mm is the yield displacement of the i-th storey. The excitation is assumed to be the same as that in Example 2, but the intensity of the white noise is set to S0 = 8.5 × 10−4m2/s 3.

The rare event of interest is defined as the peak absolute deformation among the six storeys exceeding a threshold of 0.015m, expressed by

$$\left\{y=0.015-\operatorname*{max}_{i\in\{1,2,\ldots,6\}}\left(\operatorname*{sup}_{t\in[0,15]}|u_{i}(t)|\right)\leq0\right\}\,.$$
$$(25)$$

. (25)
We define the original and physics-based surrogate models based on solvers of the equation of motion shown in Eq. (24). For the original model, Eq. (24) is solved by the implicit Euler algorithm:

$$z_{i}(t+\Delta)$$

zi(t + ∆t) = zi(t) + gi( ˙ui(t + ∆t), zi(t + ∆t))∆t , (26)
and for the surrogate model, Eq. (24) is solved by the explicit Euler algorithm:

$$(26)^{\frac{1}{2}}$$
$$(27)$$
$$z_{i}(t+\Delta t)=z_{i}(t)+g_{i}(u_{i}(t),z_{i}(t))\Delta t\,,$$
zi(t + ∆t) = zi(t) + gi( ˙ui(t), zi(t))∆t , (27)
where ∆t is the time step. The explicit Euler algorithm is highly efficient but less accurate, and thus is ideal in constructing the physics-based surrogate model. The stiffness reduction ratio αi, initial stiffness 16 ki, and yield displacement xyi are set as tunable parameters for the physics-based surrogate model, i.e.,



θp = {αi, ki, xyi}
6 i=1. The initial values of the those parameters are set to be the same as the original model.

The coupled physics-data-driven surrogate model is trained using 30, 50, and 100 initial samples and around 45 active learning samples. The heteroscedastic Gaussian process model for error correction at the final learning stage is shown in Figure 15. The optimization histories of the correlation coefficient ρ, the first-storey stiffness reduction ratio α1, and the prediction uncertainty Pˆ∆ = Pˆ+ − Pˆ− are shown in Figure 16. Figure 17 confirms the accuracy of the coupled surrogate model. Figure 18 shows the box plot of probability estimations using 10 independent runs of the proposed surrogate modeling method. Table 1 reports the first quartile, median, and third quartile of the probability estimations.







| Surrogate model solution   |            |                |            |                |            |
|----------------------------|------------|----------------|------------|----------------|------------|
| Case                       | N0         | First quartile | Median     | Third quartile | Reference  |
| 30                         | 2.4 × 10−5 | 2.9 × 10−5     | 3.1 × 10−5 |                |            |
| Example 1                  | 50         | 2.4 × 10−5     | 2.9 × 10−5 | 3.1 × 10−5     | 3.6 × 10−5 |
| 100                        | 2.4 × 10−5 | 2.6 × 10−5     | 3.4 × 10−5 |                |            |
| 30                         | 2.1 × 10−7 | 2.2 × 10−7     | 2.4 × 10−7 |                |            |
| Example 2                  | 50         | 2.2 × 10−7     | 2.3 × 10−7 | 2.4 × 10−7     | 3.0 × 10−7 |
| 100                        | 2.1 × 10−7 | 2.2 × 10−7     | 2.4 × 10−7 |                |            |
| 30                         | 1.3 × 10−3 | 1.3 × 10−3     | 1.4 × 10−3 |                |            |
| Example 3                  | 50         | 1.2 × 10−3     | 1.3 × 10−3 | 1.4 × 10−3     | 1.4 × 10−3 |
| 100                        | 1.3 × 10−3 | 1.3 × 10−3     | 1.4 × 10−3 |                |            |

## 6. Additional Remarks And Future Directions 6.1. Multiple Critical Domains Of The Rare Event

The data-driven error correction may not perform well in the presence of multiple critical domains with different response behaviors. Here, the crux is not the "multiple critical domains" per se, but the "different response behaviors" within these domains. For instance, the first-passage probability problems examined in Example 2 and 3 are series systems with numerous modes corresponding to the times at which crossing events occur. However, when the response process reaches stationarity, the rare crossing events become homogeneous across different time points. As a result, the error correction function does not need to discern the specific time point of the crossing, since these events have similar statistical properties. In this context, a one-dimensional error correction function is effective. In contrast, if the computational model exhibits different behaviors across multiple critical domains for the rare event of interest, a one-dimensional error correction approach may introduce noise due to its inability to distinguish the details of the critical modes.

A potential solution is to incorporate additional output variables to differentiate between critical domains and train distinct error functions for each domain.

## 6.2. Selection Of Physics-Based Surrogate Models

Large noisy errors can be induced by the aforementioned mechanism, but another source is the inherent limitations of the selected physics-based surrogate model. We can reduce the inherent noise by using a more detailed surrogate model, but a trade-off between accuracy and efficiency is inevitable. Further studies are needed to standardize the selection of physics-based surrogate models for various classes of problems.

6.3. Alternative importance sampling strategies The importance sampling Eq. (16) can be reformulated into the following expression:

$$P=c_{P}\cdot\hat{P}\equiv\frac{\int_{\mathbf{x}\in\mathbb{R}^{n}}\mathds{1}_{\leq0}\left(\mathcal{M}(\mathbf{x})\right)h_{\mathcal{M}\cup\hat{\mathcal{M}}}(\mathbf{x})\mathrm{d}\mathbf{x}}{\int_{\mathbf{x}\in\mathbb{R}^{n}}\mathds{1}_{\leq0}\left(\hat{\mathcal{M}}(\mathbf{x};\mathbf{\theta}_{p},\mathbf{\theta}_{e})\right)h_{\mathcal{M}\cup\hat{\mathcal{M}}}(\mathbf{x})\mathrm{d}\mathbf{x}}\,\hat{P}\,,\tag{28}$$

where the importance density hM∪Mˆ is associated with the union of the original and surrogate rare events, expressed by:

$$h_{\mathcal{M}_{\mathsf{U}},\mathcal{M}}(\mathbf{x})\coloneqq\frac{\mathbb{I}_{\leq0}\left(\min(\mathcal{M}(\mathbf{x}),\hat{\mathcal{M}}(\mathbf{x};\mathbf{\theta}_{p},\mathbf{\theta}_{e}))\right)}{\mathbb{P}\left(\min(\mathcal{M}(\mathbf{X}),\hat{\mathcal{M}}(\mathbf{X};\mathbf{\theta}_{p},\mathbf{\theta}_{e}))\leq0\right)}f_{\mathbf{X}}(\mathbf{x})\,.\tag{29}$$

Compared to Eq. (16), this alternative formulation allows for the use of a single set of samples from hM∪Mˆ to estimate both the numerator and the denominator. On the other hand, since the union event is larger than individual ones, running Markov Chain Monte Carlo on the union increases the likelihood of biased estimation for the correction factor cP . From our preliminary tests, we have not observed a decisive performance gain from using this alternative formulation. Further investigations and tests are needed.

## 7. Conclusions

This paper develops an effective surrogate modeling method for rare event simulation with high-dimensional input uncertainties. The method circumvents the curse of dimensionality by using physics-based surrogate models parameterized by a few tunable parameters. A data-fitting error correction constructed in the output space of the physics-based surrogate model is leveraged to correct the bias of surrogate modeling. Due to inherent stochastic noise in the errors, the heteroscedastic Gaussian process is adopted to model the error correction function. An active learning process is developed to effectively train the coupled physics-datadriven surrogate model to explore the critical region for the rare event. A final importance sampling step is designed to approximate the correction factor for the surrogate model-based probability estimation. Three numerical examples are studied to demonstrate the performance of the proposed method. The first example considers a static problem of a linear elastic cantilever beam with material properties modeled by a Gaussian random field. The second example studies a dynamic problem of a nonlinear viscous damper under stochastic excitation. The third example investigates a multi-degree-of-freedom hysteretic system under stochastic excitation. Three schemes are investigated to construct physics-based surrogate models: a homogenization of material properties is considered in the first example, statistical linearization is used in the second example, and relaxation of the numerical solver is adopted in the third example. The numerical results are highly promising, suggesting that the proposed method can leverage limited calls of the original computational model to effectively estimate rare event probabilities with high-dimensional input uncertainties.

## References

[1] J´erˆome Morio and Mathieu Balesdent. *Estimation of rare event probabilities in complex aerospace and other systems: A*
practical approach. Woodhead Publishing, 2015.

[2] Enrico Zio and Romney B Duffey. The risk of the electrical power grid due to natural hazards and recovery challenge following disasters and record floods: What next? In *Climate Change and Extreme Events*, pages 215–238. Elsevier, 2021.

[3] Wen Jiang, Jason D Hales, Benjamin W Spencer, Blaise P Collin, Andrew E Slaughter, Stephen R Novascone, Aysenur Toptan, Kyle A Gamble, and Russell Gardner. TRISO particle fuel performance and failure analysis with BISON. *Journal* of Nuclear Materials, 548:152795, 2021.

[4] Chao Dang and Jun Xu. A mixture distribution with fractional moments for efficient seismic reliability analysis of nonlinear structures. *Engineering Structures*, 208:109912, 2020.

[5] Jun Xu, Long Li, and Zhao-Hui Lu. An adaptive mixture of normal-inverse Gaussian distributions for structural reliability analysis. *Journal of Engineering Mechanics*, 148(3):04022011, 2022.

[6] Jie Li and Jianbing Chen. *Stochastic dynamics of structures*. John Wiley & Sons, 2009.

[7] Guohai Chen and Dixiong Yang. Direct probability integral method for stochastic response analysis of static and dynamic structural systems. *Computer Methods in Applied Mechanics and Engineering*, 357:112612, 2019.

[8] Jianhua Xian, Cheng Su, and Houzuo Guo. Seismic reliability analysis of energy-dissipation structures by combining probability density evolution method and explicit time-domain method. *Structural Safety*, 88:102010, 2021.

[9] Meng-Ze Lyu and Jian-Bing Chen. A unified formalism of the GE-GDEE for generic continuous responses and firstpassage reliability analysis of multi-dimensional nonlinear systems subjected to non-white-noise excitations. Structural Safety, 98:102233, 2022.

[10] Reuven Y Rubinstein and Benjamin Melamed. *Modern simulation and modeling*, volume 7. Wiley New York, 1998.

[11] David Landau and Kurt Binder. *A guide to Monte Carlo simulations in statistical physics*. Cambridge University Press, 2015.

[12] Siu-Kui Au and James L Beck. Estimation of small failure probabilities in high dimensions by subset simulation. *Probabilistic Engineering Mechanics*, 16(4):263–277, 2001.

[13] Nolan Kurtz and Junho Song. Cross-entropy-based adaptive importance sampling using Gaussian mixture. *Structural* Safety, 42:35–44, 2013.

20
[14] Ziqi Wang and Junho Song. Cross-entropy-based adaptive importance sampling using von Mises-Fisher mixture for high dimensional reliability analysis. *Structural Safety*, 59:42–52, 2016.

[15] Michael Engel, Oindrila Kanjilal, Iason Papaioannou, and Daniel Straub. Bayesian updating and marginal likelihood estimation by cross entropy based importance sampling. *Journal of Computational Physics*, 473:111746, 2023.

[16] Mircea Grigoriu. Data-based importance sampling estimates for extreme events. *Journal of Computational Physics*,
412:109429, 2020.

[17] Iason Papaioannou, Costas Papadimitriou, and Daniel Straub. Sequential importance sampling for structural reliability analysis. *Structural Safety*, 62:66–75, 2016.

[18] Ziqi Wang, Marco Broccardo, and Junho Song. Hamiltonian Monte Carlo methods for subset simulation in reliability analysis. *Structural Safety*, 76:51–67, 2019.

[19] Jianhua Xian and Ziqi Wang. Relaxation-based importance sampling for structural reliability analysis. *Structural Safety*,
106:102393, 2024.

[20] Malur R Rajashekhar and Bruce R Ellingwood. A new look at the response surface approach for reliability analysis.

Structural Safety, 12(3):205–220, 1993.

[21] DIEGO LORENZO Allaix and VINCENZO ILARIO Carbone. An improvement of the response surface method. Structural Safety, 33(2):165–172, 2011.

[22] Bruno Sudret and Armen Der Kiureghian. Comparison of finite element reliability methods. Probabilistic Engineering Mechanics, 17(4):337–348, 2002.

[23] Stefano Marelli and Bruno Sudret. An active-learning algorithm that combines sparse polynomial chaos expansions and bootstrap for structural reliability analysis. *Structural Safety*, 75:67–74, 2018.

[24] Emiliano Torre, Stefano Marelli, Paul Embrechts, and Bruno Sudret. Data-driven polynomial chaos expansion for machine learning regression. *Journal of Computational Physics*, 388:601–623, 2019.

[25] Jorge E Hurtado. An examination of methods for approximating implicit limit state functions from the viewpoint of statistical learning theory. *Structural Safety*, 26(3):271–293, 2004.

[26] Atin Roy and Subrata Chakraborty. Support vector machine in structural reliability analysis: A review. Reliability Engineering & System Safety, page 109126, 2023.

[27] Irfan Kaymaz. Application of kriging method to structural reliability problems. *Structural Safety*, 27(2):133–151, 2005.

[28] Barron J Bichon, Michael S Eldred, Laura Painton Swiler, Sandaran Mahadevan, and John M McFarland. Efficient global reliability analysis for nonlinear implicit performance functions. *AIAA journal*, 46(10):2459–2468, 2008.

[29] Benjamin Echard, Nicolas Gayton, and Maurice Lemaire. AK-MCS: An active learning reliability method combining Kriging and Monte Carlo simulation. *Structural Safety*, 33(2):145–154, 2011.

[30] Benjamin Echard, Nicolas Gayton, Maurice Lemaire, and Nicolas Relun. A combined importance sampling and kriging reliability method for small failure probabilities with time-demanding numerical models. Reliability Engineering & System Safety, 111:232–240, 2013.

[31] Xiaoxu Huang, Jianqiao Chen, and Hongping Zhu. Assessing small failure probabilities by AK–SS: An active learning method combining Kriging and Subset Simulation. *Structural Safety*, 59:86–95, 2016.

[32] Ziqi Wang and Marco Broccardo. A novel active learning-based Gaussian process metamodelling strategy for estimating the full probability distribution in forward UQ analysis. *Structural Safety*, 84:101937, 2020.

[33] Donald R Jones. A taxonomy of global optimization methods based on response surfaces. *Journal of Global Optimization*,
21:345–383, 2001.

[34] Thomas J Santner, Brian J Williams, William I Notz, and Brain J Williams. The design and analysis of computer experiments, volume 1. Springer, 2003.

[35] Bruno Sudret. Meta-models for structural reliability and uncertainty quantification. *arXiv preprint arXiv:1203.2062*,
2012.

[36] Christos Lataniotis, Stefano Marelli, and Bruno Sudret. Extending classical surrogate modeling to high dimensions through supervised dimensionality reduction: A data-driven approach. *International Journal for Uncertainty Quantification*, 10(1),
2020.

[37] Dimitris G Giovanis and Michael D Shields. Uncertainty quantification for complex systems with very high dimensional response using Grassmann manifold variations. *Journal of Computational Physics*, 364:393–415, 2018.

[38] Dimitris G Giovanis and Michael D Shields. Data-driven surrogates for high dimensional models using Gaussian process regression on the Grassmann manifold. *Computer Methods in Applied Mechanics and Engineering*, 370:113269, 2020.

[39] Ketson R Dos Santos, Dimitrios G Giovanis, and Michael D Shields. Grassmannian diffusion maps–based dimension reduction and classification for high-dimensional data. *SIAM Journal on Scientific Computing*, 44(2):B250–B274, 2022.

[40] Katiana Kontolati, Dimitrios Loukrezis, Dimitrios G Giovanis, Lohit Vandanapu, and Michael D Shields. A survey of unsupervised learning methods for high-dimensional uncertainty quantification in black-box-type problems. Journal of Computational Physics, 464:111313, 2022.

[41] Zhongming Jiang and Jie Li. High dimensional structural reliability with dimension reduction. *Structural Safety*, 69:35–46, 2017.

[42] Tong Zhou and Yongbo Peng. Active learning and active subspace enhancement for PDEM-based high-dimensional reliability analysis. *Structural Safety*, 88:102026, 2021.

[43] N Navaneeth and Souvik Chakraborty. Surrogate assisted active subspace and active subspace assisted surrogate—A new paradigm for high dimensional structural reliability analysis. *Computer Methods in Applied Mechanics and Engineering*,
389:114374, 2022.

[44] Jungho Kim, Ziqi Wang, and Junho Song. Adaptive active subspace-based metamodeling for high-dimensional reliability analysis. *Structural Safety*, 106:102404, 2024.

[45] Zhong-Ming Jiang, De-Cheng Feng, Hao Zhou, and Wei-Feng Tao. A recursive dimension-reduction method for highdimensional reliability analysis with rare failure event. *Reliability Engineering & System Safety*, 213:107710, 2021.

[46] Maziar Raissi, Paris Perdikaris, and George E Karniadakis. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics, 378:686–707, 2019.

[47] Yinhao Zhu, Nicholas Zabaras, Phaedon-Stelios Koutsourelakis, and Paris Perdikaris. Physics-constrained deep learning for high-dimensional surrogate modeling and uncertainty quantification without labeled data. Journal of Computational Physics, 394:56–81, 2019.

[48] Kevin Linka, Amelie Sch¨afer, Xuhui Meng, Zongren Zou, George Em Karniadakis, and Ellen Kuhl. Bayesian physics informed neural networks for real-world nonlinear dynamical systems. Computer Methods in Applied Mechanics and Engineering, 402:115346, 2022.

[49] Zeng Meng, Qiaochu Qian, Mengqiang Xu, Bo Yu, Ali Rıza Yıldız, and Seyedali Mirjalili. PINN-FORM: A new physicsinformed neural network for reliability analysis with partial differential equation. *Computer Methods in Applied Mechanics* and Engineering, 414:116172, 2023.

[50] Benjamin Peherstorfer, Karen Willcox, and Max Gunzburger. Survey of multifidelity methods in uncertainty propagation, inference, and optimization. *Siam Review*, 60(3):550–591, 2018.

[51] Benjamin Peherstorfer, Tiangang Cui, Youssef Marzouk, and Karen Willcox. Multifidelity importance sampling. Computer Methods in Applied Mechanics and Engineering, 300:490–509, 2016.

[52] Boris Kramer, Alexandre Noll Marques, Benjamin Peherstorfer, Umberto Villa, and Karen Willcox. Multifidelity probability estimation via fusion of estimators. *Journal of Computational Physics*, 392:385–402, 2019.

[53] John W Peterson, Alexander D Lindsay, and Fande Kong. Overview of the incompressible navier–stokes simulation capabilities in the MOOSE framework. *Advances in Engineering Software*, 119:68–92, 2018.

[54] Zhong-Hua Han, Stefan G¨ortz, and Ralf Zimmermann. Improving variable-fidelity surrogate modeling via gradientenhanced kriging and a generalized hybrid bridge function. *Aerospace Science and Technology*, 25(1):177–189, 2013.

[55] Isaac M Held. The gap between simulation and understanding in climate modeling. *Bulletin of the American Meteorological* Society, 86(11):1609–1614, 2005.

[56] Peter Benner, Serkan Gugercin, and Karen Willcox. A survey of projection-based model reduction methods for parametric dynamical systems. *SIAM review*, 57(4):483–531, 2015.

[57] Boris Kramer and Karen E Willcox. Nonlinear model order reduction via lifting transformations and proper orthogonal decomposition. *AIAA Journal*, 57(6):2297–2307, 2019.

[58] D Patsialis and AA Taflanidis. Reduced order modeling of hysteretic structural response and applications to seismic risk assessment. *Engineering Structures*, 209:110135, 2020.

[59] Stephen H Crandall. A half-century of stochastic equivalent linearization. *Structural Control and Health Monitoring: The* Official Journal of the International Association for Structural Control and Monitoring and of the European Association for the Control of Structures, 13(1):27–40, 2006.

[60] Isaac Elishakoff and Stephen H Crandall. Sixty years of stochastic linearization technique. *Meccanica*, 52:299–305, 2017.

[61] Ziqi Wang. Optimized equivalent linearization for random vibration. *Structural Safety*, 106:102402, 2024.

[62] Somayajulu LN Dhulipala, Michael D Shields, Benjamin W Spencer, Chandrakanth Bolisetti, Andrew E Slaughter, Vincent M Labour´e, and Promit Chakroborty. Active learning with multifidelity modeling for efficient rare event simulation.

Journal of Computational Physics, 468:111506, 2022.

[63] Somayajulu LN Dhulipala, Michael D Shields, Promit Chakroborty, Wen Jiang, Benjamin W Spencer, Jason D Hales, Vincent M Laboure, Zachary M Prince, Chandrakanth Bolisetti, and Yifeng Che. Reliability estimation of an advanced nuclear fuel using coupled active learning, multifidelity modeling, and subset simulation. *Reliability Engineering & System* Safety, 226:108693, 2022.

[64] Miguel L´azaro-Gredilla, Michalis K Titsias, Jochem Verrelst, and Gustavo Camps-Valls. Retrieval of biophysical parameters with heteroscedastic Gaussian processes. *IEEE Geoscience and Remote Sensing Letters*, 11(4):838–842, 2013.

[65] TJ Rogers, P Gardner, N Dervilis, K Worden, AE Maguire, E Papatheou, and EJ Cross. Probabilistic modelling of wind turbine power curves with application of heteroscedastic Gaussian process regression. *Renewable Energy*, 148:1124–1136, 2020.

[66] Jungho Kim, Sang-ri Yi, and Junho Song. Estimation of first-passage probability under stochastic wind excitations by active-learning-based heteroscedastic Gaussian process. *Structural Safety*, 100:102268, 2023.

[67] Jan Hauke and Tomasz Kossowski. Comparison of values of Pearson's and Spearman's correlation coefficients on the same sets of data. *Quaestiones geographicae*, 30(2):87–93, 2011.

[68] Søren Taverniers, Eric J Hall, Markos A Katsoulakis, and Daniel M Tartakovsky. Mutual information for explainable deep learning of multiscale systems. *Journal of Computational Physics*, 444:110551, 2021.

[69] Samir Beneddine. Nonlinear input feature reduction for data-based physical modeling. *Journal of Computational Physics*,
474:111832, 2023.

[70] Andrew R Conn, Katya Scheinberg, and Luis N Vicente. *Introduction to derivative-free optimization*. SIAM, 2009. [71] Vincent Dubourg, Bruno Sudret, and Jean-Marc Bourinet. Reliability-based design optimization using kriging surrogates and subset simulation. *Structural and Multidisciplinary Optimization*, 44:673–690, 2011.

[72] Maliki Moustapha, Stefano Marelli, and Bruno Sudret. Active learning for structural reliability: Survey, general framework and benchmark. *Structural Safety*, 96:102174, 2022.

[73] Radford M Neal et al. MCMC using Hamiltonian dynamics. *Handbook of Markov Chain Monte Carlo*, 2(11):2, 2011.

[74] Iason Papaioannou, Wolfgang Betz, Kilian Zwirglmaier, and Daniel Straub. MCMC algorithms for subset simulation.

Probabilistic Engineering Mechanics, 41:89–103, 2015.

[75] Masanobu Shinozuka and George Deodatis. Simulation of stochastic processes by spectral representation. *Applied Mechanics Reviews*, 44(4):191–204, 1991. [76] Jianhua Xian, Cheng Su, and Billie F Spencer Jr. Stochastic sensitivity analysis of energy-dissipating structures with nonlinear viscous dampers by efficient equivalent linearization technique based on explicit time-domain method. Probabilistic Engineering Mechanics, 61:103080, 2020.

[77] YK Wen. Equivalent linearization for hysteretic systems under random excitation. *Journal of Applied Mechanics*,
47(1):150–154, 1980.





25.25