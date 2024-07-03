# StREAmLining Ocean Dynamics Modeling With Fourier Neural Operators: A Multiobjective Hyperparameter AND ARCHITECTURE OPTIMIZATION APPROACH 

(1) Yixuan Sun<br>Argonne National Laboratory<br>yixuan.sun@anl.gov

Sri Hari Krishna Narayanan

Argonne National Laboratory

snarayan@mcs . anl.gov

Ololade Sowunmi<br>Florida State University<br>osowunmi@fsu . edu

Romain Egele<br>Université Paris-Saclay<br>romain.egele@universite-paris-saclay.fr

Luke Van Roekel<br>Los Alamos National Laboratory<br>lvanroekel@lanl.gov

Prasanna Balaprakash*<br>Oak Ridge National Laboratory<br>pbalapra@ornl.gov


#### Abstract

Training an effective deep learning model to learn ocean processes involves careful choices of various hyperparameters. We leverage the advanced search algorithms for multiobjective optimization in DeepHyper, a scalable hyperparameter optimization software, to streamline the development of neural networks tailored for ocean modeling. The focus is on optimizing Fourier neural operators (FNOs), a data-driven model capable of simulating complex ocean behaviors. Selecting the correct model and tuning the hyperparameters are challenging tasks, requiring much effort to ensure model accuracy. DeepHyper allows efficient exploration of hyperparameters associated with data preprocessing, FNO architecture-related hyperparameters, and various model training strategies. We aim to obtain an optimal set of hyperparameters leading to the most performant model. Moreover, on top of the commonly used mean squared error for model training, we propose adopting the negative anomaly correlation coefficient as the additional loss term to improve model performance and investigate the potential trade-off between the two terms. The experimental results show that the optimal set of hyperparameters enhanced model performance in single timestepping forecasting and greatly exceeded the baseline configuration in the autoregressive rollout for long-horizon forecasting up to 30 days. Utilizing DeepHyper, we demonstrate an approach to enhance the use of FNOs in ocean dynamics forecasting, offering a scalable solution with improved precision.


Keywords Ocean Modeling $\cdot$ Operator Learning $\cdot$ Hyperparameter Optimization

## 1 Introduction

Deep learning techniques significantly enhance scientific computing, serving as efficient surrogate models for complex, time-intensive first-principles-driven simulations. Their application in climate modeling leverages large amounts of high-resolution, multidimensional data. It addresses the computational challenges posed by increasingly complex climate systems, resulting in remarkable advances in environmental research $[1,2,3,4,5]$.

The oceans play a leading role in the climate system via the storage and transport of anthropogenically generated heat and carbon dioxide, a role that is crucial for mitigating climate change. Simultaneously, oceanic processes that redistribute mass, heat, and salt are instrumental in driving phenomena such as hurricanes, extreme precipitation, and droughts [6]. Deep learning models have empowered ocean modeling from a spatial-temporal forecast of select ocean features $[7,8,9]$ to parameterization $[10,11,12]$. Despite the success of those models, however, selecting and fine-[^0]tuning appropriate model hyperparameters remain challenging, often requiring a significant amount of manual search via trial and error.

Hyperparameters are the non-trainable parameters determining the data preprocessing, network structure, and training procedures; and they highly impact the performance of deep learning models [13]. Searching for a proper combination that works optimally for the specific problem can be challenging. With the increasing complexity of performant deep learning models, manual tuning conducted in a trial-and-error way becomes infeasible, given that hyperparameter configurations exist within a vast search space.

Deep learning models for ocean processes must accurately capture the mean behavior of the ocean state profile and account for the detailed variation throughout the domain. In modeling climate processes using deep learning models, one typically formulates the problem as an image-to-image regression problem, where the pixels of an image represent the state values within the domain of interest and the image channels are associated with different state variables. One often uses per-pixel mean squared error (MSE) as the loss function because of differentiability and correspondence to maximized likelihood with assumed Gaussian errors to train these models [5, 14, 3]. However, MSE penalizes large errors more significantly and usually produces images in favor of averaged pixel values that may be blurry and unnatural $[15,16]$. This situation might become problematic in producing ocean dynamics forecasts because the values are relatively stable and have a long time scale compared with the weather, where the values evolve closely to the mean field. Many modifications and different loss functions have been proposed to mitigate the issue of MSE [17, 15], but they are highly problem-dependent and can be complex. Here, specifically for ocean modeling with deep neural networks, we propose using the negative value of a simple metric, the anomaly correlation withefficient (ACC) [18], commonly used in climate model evaluation, as the additional loss term on top of the MSE to address this potential issue.

We construct the model with Fourier neural operators (FNOs) [19] and utilize DeepHyper [20, 21] to perform hyperparameter and architecture searches to automate the model selection of FNOs for an idealized baroclinic wind-driven ocean system. The aim is to predict four prognostic variables at a single time step in the future, given the variable values and a physical parameter at the current time. We also anticipate an improvement in autoregressive rollout performance, which typically requires special treatment during training [22, 5, 14]. This expected enhancement is due to the selected model's ability to provide more accurate forecasts for single-time steps. We investigate the potential disadvantages of pure MSE loss and the effect of combining MSE and negative ACC with an associated hyperparameter, weighing the importance of the two. Furthermore, we have expanded the hyperparameter optimization (HPO) across a high-performance computing (HPC) environment involving more than 20 nodes, each equipped with four GPUs per node, while integrating effective early stopping criteria to refine the search process, yielding more timely and potent outcomes. The experimental results show that using the optimal hyperparameter configuration from the search results in a model that outperforms the baseline in the single time-stepping forecast of all four prognostic variables and significantly improves the model's autoregressive performance for long-range rollout. We expect this work to pave the way for a more systematic model construction process for ocean/climate modeling using FNOs and their variants.

The rest of the paper is organized as follows. Section 2 introduces the work involving deep learning studies for ocean modeling, FNOs, and the general hyperparameter search processes with multiple objectives. Section 3 formulates the problem into an operator learning setting and describes Bayesian optimization with multipoint acquisitions for parallelization. Sections 4 and 5 define the hyperparameter search space and discuss the search results and the impact of hyperparameters associated with data preprocessing, neural architecture, and training process. Section 6 summarizes our conclusions and briefly mentions future directions.

## 2 Related Work

### 2.1 Fourier Neural Opearator

The Fourier neural operator and its variants $[19,23,24,25]$ have shown outstanding ability to solve partial differential equations and predictive tasks in various scientific domains [26, 27]. In particular, FNOs powered climate modeling and enabled accurate mid- and long-range prediction at a fraction of the cost compared with first-principles-based simulations [5,28]. The general idea behind FNOs is to composite convolutional kernel integrals in the Fourier domain to approximate the solution operator. FNOs generally have three major components: lifting layers, Fourier operator blocks, and projection layers. During lifting, the network transforms the input functions (e.g., initial condition or other parameters) to higher-dimensional spaces. The transformed input goes through a series of FNO blocks where fast Fourier transform (FFT) transforms the data, followed by convolutional operations in the frequency domain. A preset number of high-frequency modes in the results are filtered out, preserving general features and smoother behaviors associated with lower-frequency modes. An inverse FFT then transforms the data back to the physical domain. Finally, the projection components map the data back to its original dimensions, forming the solution. As an operator learning
framework, FNOs learn the mapping between function spaces and can predict beyond the resolution of the training data. Therefore, they are suitable for solving problems involving partial differential equations and various mesh representations of the domain, including weather and ocean modeling.

### 2.2 Hyperparameter Optimization with DeepHyper

DeepHyper [21] is a Python package that provides asynchronous parallel hyperparameter and neural architecture search algorithms. It provides parallel implementations of the SMAC (sequential model-based algorithm configuration algorithm [29], which is a type of Bayesian optimization algorithm [30]. For parallelization, it can leverage different backends with minimal code changes, such as threads, processes, and MPI. We will now provide an overview of the hyperparameter optimization algorithms we used in this work.

### 2.2.1 Centralized Bayesian Optimziation

Bayesian optimization (BO), also known as efficient global optimization [30], is a popular approach for hyperparameter optimization frameworks because of its fast convergence properties. BO is a type of black-box optimization algorithm where the core idea is to iteratively update an internal surrogate model in order to minimize the number of direct queries to the real "expensive" black-box function. The standard BO algorithm is sequential, thus making it difficult to leverage parallel computing resources available on HPC systems. Within DeepHyper, BO can be parallelized through a centralized or decentralized architecture. In the centralized scheme, a single manager decides the function evaluation locations when workers conduct the evaluations in parallel. In contrast, the decentralized scheme equips workers with their own optimizer and allows all operations in parallel. The latter provides maximum scalability [31] when performing large-scale hyperparameter optimization (i.e., ; 1,000 parallel function evaluations). In our case, we use the centralized approach with a $q \mathrm{UCB}$ ( $q$-Upper Confidence Bound) acquisition function [32] for the multipoint acquisition strategy. This method provides better scalability than does the usual constant-liar multipoint acquisition strategy [33], also known as Kriging Believer [34].

In a centralized architecture, the central coordinator determines the next hyperparameters at which the function should be tested and then distributes these tasks to available remote workers. The surrogate model used is Extremely Randomized Trees [35], a type of random forest approach [36] that provides better epistemic uncertainty estimates thanks to a random-split strategy when building tree nodes.

### 2.2.2 Multiobjective Optimization

The most common objective in hyperparameter optimization for neural networks is to minimize the validation loss. In our problem setup, the loss function contains two terms, MSE and negative ACC, and we plan to investigate any potential trade-off between the two. MSE accounts for the average behavior of the state variable fields, penalizing large errors, whereas ACC focuses on anomalies between forecast and true fields, emphasizing pattern nuances. In ocean modeling, we not only care about accurate forecasts of the mean field over time, for example, the gyre circulation, but also are interested in the precise characterization of the local variations, for example, intergyre exchange from eddies. We investigate the relationship between the two objectives through the lens of multiobjective optimization.

A trade-off between MSE and ACC would mean that on the optimal frontier, the Pareto front, one objective cannot be improved without degrading the other. On the contrary, without a trade-off, both objectives can be improved jointly, thus providing a dominant point on the Pareto front [37], that is, in the objective space. A simple way to find the Pareto optimal solutions is to combine the objectives and perform optimization only over the combined single objective, known as scalarization [38]. With a trade-off between objectives, however, this process corresponds to optimizing for a fixed trade-off. DeepHyper can perform multiobjective hyperparameter optimization through randomized scalarization within Bayesian optimization [39]. Randomized scalarization resamples random objective weights for each new suggestion, thus reducing the multiobjective optimization problem to a single-objective optimization problem where each weight vector represents a fixed trade-off between objectives. By resampling different weights, the Pareto-Front can be explored. We leverage this capability to optimize for both validation MSE and ACC.

### 2.3 Data-Driven Ocean Modeling

Conventional first-principles-based simulations of ocean evolution, while being reliable and accurate, are computationally intensive and can become intractable for tasks such as uncertainty quantification, sensitivity analysis, and optimization. With the advance of deep learning models and the computational efficiency once trained, data-driven methods for modeling ocean dynamics have emerged. Some recent developments address spatial-temporal ocean property forecasts [40] and rainfall pattern segmentation over oceans [41]. However, according to the specific application
scenario and datasets, building effective models usually involves careful design of the model architecture and significant trial and error to fine-tune model training to achieve better overall performance. This process introduces a new round of computational overhead. To address this issue, we show a workflow that leverages FNO and hyperparameter optimization to streamline the modeling process of ocean dynamics, which other data-driven models can easily adapt.

## 3 Method

### 3.1 Problem Formulation

The dynamics of the idealized baroclinic wind-driven ocean model can be formulated as an initial value problem (IVP), which starts with the initial state, $\mathbf{x}_{0}$, and the model parameter(s), $\kappa$. We aim to solve for the state $\mathbf{x}(t)$ (i.e., the state prognostic variables) at time $t$. The IVP, $d \mathbf{x}(t, \kappa) / d t=f(\mathbf{x}(t))$, with $\mathbf{x}(0)=\mathbf{x}_{0}$, leads to the solution at time $t$, $\mathbf{x}_{t}=\mathbf{x}_{0}+\int_{0}^{t} f(\mathbf{x}(\tau, \kappa)) d \tau$. The solution at the discrete time step $t+1$ can be expressed as

$$
\mathbf{x}(t+1)=\mathbf{x}(t)+\int_{t}^{t+1} f(\mathbf{x}(\tau, \kappa)) d \tau
$$

We use a FNO, $\mathcal{N}_{\theta}$, parameterized by learnable weights and biases $\theta$ to approximate the solution operator to (1). In particular, we trained the neural network to approximate the following mapping,

$$
\mathbf{x}_{t+1}=\mathcal{N}_{\theta}\left(\mathbf{x}_{t}, \kappa\right)
$$

where $\mathbf{x}$ is the state variable vector, $t$ represents the current time, and $\kappa$ is the parameter that impacts the trajectories of state variables. With the training dataset $\mathcal{D}$ containing input-output pairs, the learning objective is to minimize the empirical loss function,

$$
\begin{aligned}
\mathcal{L}(\theta, \mathcal{D}) & =\alpha \cdot \mathcal{L}_{\mathrm{MSE}}+(1-\alpha) \cdot \mathcal{L}_{\mathrm{NegACC}} \\
\mathcal{L}_{\mathrm{MSE}} & =\frac{1}{N} \sum_{i=1}^{N}\left\|\mathbf{x}_{t+1}^{(i)}-\mathcal{N}_{\theta}\left(\mathbf{x}_{t}^{(i)}, \kappa^{(i)}\right)\right\|_{2}^{2} \\
\mathcal{L}_{\mathrm{NegACC}} & =-\frac{\sum_{i=1}^{N}\left(\mathcal{N}_{\theta}\left(\mathbf{x}_{t}^{(i)}, \kappa^{(i)}\right)-\overline{\mathbf{x}}_{t+1}\right)\left(\mathbf{x}_{t+1}^{(i)}-\overline{\mathbf{x}}_{t+1}\right)}{\sum_{i=1}^{N} \sqrt{\left(\mathcal{N}_{\theta}\left(\mathbf{x}_{t}^{(i)}, \kappa^{(i)}\right)-\overline{\mathbf{x}}_{t+1}\right)^{2}\left(\mathbf{x}_{t+1}^{(i)}-\overline{\mathbf{x}}_{t+1}\right)^{2}}}
\end{aligned}
$$

where $N$ is the number of data points in the training set. The loss function contains two terms: the standard MSE loss and the negative ACC. We assign a weighting factor $\alpha$, treated as a hyperparameter, to adjust the relative importance between the two terms. We expect the trained neural network to predict the state variables one step forward accurately.

### 3.2 Bayesian Optimization and Multipoint Acquisition

Bayesian optimization is an efficient global optimization method for black-box functions with the presence of noise. Our HPO problem focuses on finding a set of hyperparameters that maximize the preset objectives. The black-box function, $f(x)$, in this context, is the function that maps hyperparameters to the objectives. Formally, we aim to solve the following,

$$
\max _{p}\left\{f(p): p=\left(p_{D}, p_{N}, p_{T}\right) \in \mathcal{P}\right\}
$$

where $p$ is a set of hyperparameters and subscripts $D, N$, and $T$ represent hyperparameters in the data preprocessing, neural architecture, and training process, respectively. The hyperparameter search space $\mathcal{P}$ is predefined. The evaluation of $f(p)$ is computationally expensive because it requires complete training of neural networks. Therefore, a surrogate model is needed to approximate these expensive functions, allowing for a more efficient exploration of the hyperparameter space. We used the default surrogate model in DeepHyper, random forest [36], to perform BO. Random forest regressors have scaling advantages over more commonly used Gaussian processes [31].

In BO, the acquisition function describes the quality of the input and determines the next evaluation points. We used the upper confidence bound (UCB), defined as the follows,

$$
U C B(p)=\mu(p)+c \cdot \sigma(p)
$$

where $\mu(p)$ and $\sigma(p)$ are the mean and standard deviation of the surrogate predictions, respectively. The constant, $c$, controls the trade-off between exploration and exploitation. BO iteratively evaluates $f(p)$ and determines the next evaluation point(s) $p^{\prime}$ based on the value of $U C B(p)$.

To perform efficient searches and leverage the HPC environment, we enabled multipoint acquisition with UCB to parallelize BO. This poses a multipoint optimization problem. In the centralized scheme, a manager performs BO and selects hyperparameter configurations, and workers evaluate the configurations and return the results back to the manager. Since BO typically updates the surrogate model and selects points sequentially, we used the $q \mathrm{UCB}$ strategy [32] to ensure effective evaluation point selection in parallel, where various values of $c$ are drawn from the exponential distribution for the UCB acquisition function and different next points are chosen according to these values to achieve an optimal balance between exploration and exploitation.

## 4 Experiment

This section describes the experiment setup, including the data generation, hyperparameter search space, and optimization execution.

### 4.1 Dataset

We adopted and simplified the data generated from [42]. The dataset used in the experiment consisted of 100 simulations of salinity, temperature, zonal velocity, and meridional velocity at the ocean surface of an idealized baroclinic wind-driven ocean model. They were obtained by running the Simulating Ocean Mesoscale Activity (SOMA) test case [43] within a circular basin of a $150 \mathrm{~km}$ wide and $100 \mathrm{~m}$ deep shelf. An ensemble of simulations was developed by varying the bolus diffusivity ( $\kappa_{G M}$ ) in the Gent-McWilliams parameterization. The diffusivity was uniformly sampled from $[200,2000]$. Each variable of interest has two dimensions in space, spanning 100 grid points per direction. Therefore, along with $\kappa_{G M}$, the data obtained from each simulation (associated with a different $\kappa_{G M}$ ) has the shape of $(30,100,100,5)$, where 30 indicates 30 time steps (days) and 5 includes the four state variables and $\kappa_{G M}$. To train models that take the state variables and parameters at the current time and predict the same set of state variables at the next step, we split 30 time steps into 29 input-output pairs per simulation, resulting in 2,900 input-output instances in total. We further split the data based on independent simulations into training, validation, and testing sets with a ratio of $0.6,0.2$, and 0.2 , respectively. The search for the optimal set of hyperparameters was determined by the model performance on the validation set. The final evaluations were done using the testing set.

### 4.2 Hyperparameter Search Space

The hyperparameters involved in this work mainly belong to three categories: data preprocessing, neural architecture related, and training process related. The neural-architecture-related hyperparameters determine the hypothesis (model) space, bounding the expressivity, and generalizability. The training-process-related hyperparameters affect the learning, of which the goal is to find the optimal model by varying its trainable weights to minimize the loss function over the training and validation data. We focus on searching for the optimal set of hyperparameters, listed in Table 1, that contribute to the best-performing FNO for ocean modeling.

Since the convolution operations in the Fourier domain are the critical components of FNOs, the usage of padding and coordinate features is essential to the learning results. The first set of hyperparameters is whether we use padding for the input data and the padding type. Paddings affect the output of the convolutions at the domain boundaries [44] and potentially mitigate the edge effect introduced by the subsequent FFT. Also, we consider incorporating the coordinate features on the input data level, allowing the model to learn the explicit solution dependency on the spatial position.

In the lifting block of FNOs, which maps the input data to higher dimensions elementwise (preserving the spatial dimension), we aim to optimize the number of layers and the activation functions. The next component in FNOs is the operator learning block, consisting of the forward FFT, convolution operation in the frequency domain, filtering out of high-frequency modes, followed by nonlinear activations, and then an inverse FFT. Here, we search for the optimal number of operator learning blocks, the number of Fourier (low-frequency) modes to keep, and the choice of the activation function. The last component in the typical FNOs is the projection block, transforming the lifted and convolved data back to the original data dimension. Similar to the lifting block, we are interested in finding the optimal number of projection layers, the number of neurons per layer, and the choice of the activation function. During training, the choice of the optimizer, batch size, magnitude of the learning rate, weights associated with the loss terms, and regularization could highly impact the quality of the trained model. Therefore, we aim to find an optimal combination of these values that leads to the most accurate model.

Table 1: List of hyperparameters and their ranges. (a) shows the hyperparameters related to data preprocessing. (b) shows the hyperparameters determining the neural architecture. (c) describes the ones in the training process.

(a)

| Variable Names. | Type | Range/Choice | Explanation |
| :---: | :---: | :---: | :---: |
| padding | bool | [True, False] | If zero-pad the data. |
| padding_type | str | ['constant',' 'reflect', <br> 'replicate', 'circular'] | Types of padding. |
| coord_feat | bool | [True, False] | If use domain coordinates as addi- <br> tional features. |

(b)

| Variable Names | Type | Range/Choice | Explanation |
| :---: | :---: | :---: | :---: |
| lift_act | str | ['relu', 'leaky_relu', <br> 'prelu', 'relu6', 'elu', <br> 'selu', 'silu', 'gelu', <br> 'sigmoid', 'logsigmoid', <br> 'softplus', 'softshrink', <br> 'softsign', 'tanh', <br> 'tanhshrink', 'threshold', <br> 'hardtanh', 'identity', <br> 'squareplus'] | Activation function for lifting lay- <br> ers. The choices include common <br> activation functions implemented in <br> PyTorch. |
| num_FNO | int | $[2,16]$ | The number of FNO blocks. |
| num_latent_feat | int | $[2,64]$ | The number of latent features in <br> FNO blocks. This is equivalent to <br> the number of channels in an image <br> representation. |
| num_modes | int | $[2,32]$ | The number of Fourier modes to <br> keep. |
| num_proj_layers | int | $[2,16]$ | The number of projection layers. |
| proj_size | int | $[2,16]$ | Projection layer size. |
| proj_act | str | ['relu', 'leaky_relu', <br> 'prelu', 'relu6', 'elu', <br> 'selu', 'silu', 'gelu', <br> 'sigmoid', 'logsigmoid', <br> 'softplus', 'softshrink', <br> 'softsign', 'tanh', <br> 'tanhshrink', 'threshold', <br> 'hardtanh', 'identity', <br> 'squareplus'] | Activation function for projection <br> layers. The choices include com- <br> mon activation functions imple- <br> mented in PyTorch. |

(c)

| Variable Names | Type | Range/Choice | Explanation |
| :---: | :---: | :---: | :---: |
| alpha | float | $(0,1)$ | Weight associated with MSE and <br> negative ACC in the loss function. |
| optimizer | str | ['Adadelta', 'Adagrad', <br> 'Adam', 'AdamW', 'RMSprop', <br> 'SGD'] | Types of optimizers. |
| $\operatorname{lr}$ | float | $(1 e-6,1 e-2)$ | Learning rate |
| weight_decay | float | $(0,0.1)$ | The weighting factor of the $L_{2}$ reg- <br> ularization. |
| batch_size | int | $(2,64)$ | The batch size of training data dur- <br> ing training. |

Table 2: Model performance on the testing set using the baseline models trained with MSE loss and composite loss.

|  | $\log (R S E) \downarrow$ |  | $\log (1-A C C) \downarrow$ |  |
| :--- | :---: | :---: | :---: | :---: |
|  | MSE Loss | MSE + NegACC Loss | MSE Loss | MSE + NegACC Loss |
| Salinity | -2.202 | $\mathbf{- 2 . 4 9 8}$ | -2.503 | $\mathbf{- 2 . 8 0 0}$ |
| Temperature | $-\mathbf{3 . 6 9 6}$ | -3.061 | $-\mathbf{4 . 0 1 5}$ | -3.363 |
| Meridional V. | -1.958 | $-\mathbf{2 . 0 6 7}$ | -2.258 | $\mathbf{- 2 . 8 4 2}$ |
| Zonal V. | -2.248 | $\mathbf{- 2 . 3 0 3}$ | -2.549 | $\mathbf{- 2 . 8 0 8}$ |

### 4.3 Objectives

We set up the hyperparameter optimization problem to optimize two objectives. The first objective is to minimize the validation MSE, defined as the first term in (3). MSE is calculated pixelwise, aiming to reach the average minimum value. The second objective is to maximize the validation anomaly correlation coefficient (ACC), defined as the second term in (3), which is a commonly used metric in climate studies. Given that adding negative ACC could potentially avoid the drawbacks of MSE, we treat them as two separate objectives with equal importance and investigate the relationship between ACC and MSE. In DeepHyper, all the searches are focused on maximizing objectives. Therefore, we implemented the objectives as negative MSE and positive ACC.

### 4.4 Implementation

We constructed the FNO model using the Nvidia Modulus package and set up the hyperparameter search space, the black-box function for BO, and the evaluator in DeepHyper. The searches used 20 computing nodes, with four Nvidia A100 GPUS per node, on Polaris cluster at the Argonne Leadership Computing Facility.

Training FNO with high-dimensional data can be computationally expensive. Therefore, we adopted two stoppers to accelerate the searches and the parallelization. A stopper terminates the training of a neural network based on certain criteria, improving search efficiency. The first stopper used a constant predictor, a constant number that minimizes the MSE term in the loss function (3). In this case, the constant predictor becomes the mean value of the target. The second stopper keeps track of the running time for each training epoch. In our optimized training regimen for each hyperparameter configuration, we implemented an early stopping mechanism for efficiency. Specifically, we terminated the training of any models whose configurations yielded results inferior to that of the constant predictor within the initial 10 epochs or taking over 100 seconds to complete a single epoch during training. If neither stopper was triggered, the training was terminated at epoch 30 , returning the objective values. This approach strategically reduces unnecessary computational expenditure on unpromising model configurations.

With the search results, we conducted a full training (100 epochs) using the set of hyperparameters that resulted in the best objectives. We used the default hyperparameter configuration preset in Modulus as a baseline to compare the testing performance with the fully trained model.

## 5 Results and Discussion

To demonstrate the positive impact of using negative ACC as the additional loss term, we trained models using the default hyperparameters provided by Modulus for 100 epochs using loss functions that are pure MSE and the equally weighted ones of MSE and negative ACC. While the search objectives were validation MSE and ACC, we use Relative Squared Error (RSE), $R S E=\sum\left(\mathbf{x}_{t+1}-\mathcal{N}_{\theta}\left(\mathbf{x}_{t}, \kappa\right)\right)^{2} / \sum\left(\mathbf{x}_{t+1}-\overline{\mathbf{x}}_{t+1}\right)^{2}$, and 1 - ACC in their log scale to highlight performance differences. We also use these metrics to evaluate search results in the later sections.

Table 2 shows the $\log (R S E)$ and $\log (1-A C C)$ values from the two models. Overall, the model trained with the composite loss function achieved lower values for both metrics. Notably, training the network with the composite loss improved MSE values over the pure MSE loss in salinity, meridional velocity, and zonal velocity. These results validate adding negative $\mathrm{ACC}$ as part of the loss function. The model training for the subsequent hyperparameter optimization adopts this composite loss.
(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-08.jpg?height=352&width=1049&top_left_y=320&top_left_x=251)

(b)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-08.jpg?height=342&width=1352&top_left_y=748&top_left_x=251)

(c)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-08.jpg?height=353&width=1662&top_left_y=1165&top_left_x=253)

Figure 1: Parallel coordinate plots of the hyperparameters in the search space with respect to the validation MSE (in $\log$ scale). The space is divided into three categories. (a) shows the data-related hyperparameters, (b) shows trainingrelated hyperparameters, and (c) contains neural architecture-related hyperparameters.

### 5.1 First Objective: Validation Mean Square Error

Varying separate hyperparameters results in differing responses in the validation MSE. Figure 1 shows the parallel coordinates plots of the hyperparameters in the search space, divided into three categories. The curves are ranked based on the objective values in the log scale, where the lighter blue represents favorable configurations. Figure 1a suggests that, among the data-related hyperparameters, in this case, the padding (its type and coordinate features, if used) has an unclear effect on the final model performance in validation MSE. The reason could be that the region of interest is a circular basin represented in the regular grids, with the area outside the basin being zeros, and using padding or different types of padding only expands the area, not affecting learning. Figure $1 \mathrm{~b}$ shows the effect of various training strategies. Among the hyperparameters for training, the loss term weighing factor $\alpha$ near the two ends of its range results in suboptimal performance. A smaller batch size corresponds to a lower validation MSE, while the magnitude of the learning rate seems to have negatively affected the validation MSE. We suspect this was due to the limited number of epochs in the search, where models update more slowly with lower learning rates and wind up with worse performance at the end of training. The weight decay does not show an evident correlation with the model performance. A smaller batch size is considered useful for improving generalization error and accelerating convergence [45], coinciding with the search results. The configurations with lower validation MSE are present mostly with the AdamW optimizers, while Adadelta is associated with mostly lower-ranked configurations. The Adam optimizer [46], the default optimizer in our cases, has led to mixed model performances. Regarding the neural architecture-related hyperparameters, we can observe evident impact from the choice of the number of latent channels, number of FNO blocks, number of Fourier modes, number of projection layers, and projection activation functions.
(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-09.jpg?height=350&width=1049&top_left_y=324&top_left_x=251)

(b)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-09.jpg?height=347&width=1369&top_left_y=743&top_left_x=237)

(c)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-09.jpg?height=353&width=1665&top_left_y=1165&top_left_x=249)

Figure 2: Parallel coordinate plots of the hyperparameters in the search space with respect to the validation ACC. The space is divided into three categories. (a) shows the data-related hyperparameters, (b) shows training-related hyperparameters, and (c) contains neural architecture-related hyperparameters.

More specifically, latent channels being greater than two and less than ten, fewer FNO blocks, a higher number of Fourier modes, and a mid- to low-level number of projection layers correspond to a lower validation MSE. Among the projection activations, the commonly used rectified linear unit (ReLU) led to relatively suboptimal performance. However, some ReLU variants-leaky ReLU and PReLU—positively influenced the minimization of the validation MSE.

### 5.2 Second objective: Validation Anomaly Coefficient Correlation

The second search objective was the validation ACC, which measures how much the forecasted deviation from the mean field is correlated with the true deviation. A higher ACC is preferred; thus, the search aimed to maximize the ACC. Figure 2 shows the parallel coordinates plots of the impact of hyperparameters on the validation ACC, where the lines are ranked with decreasing ACC values. Different hyperparameters have different impact. Figure 2a implies that the data preprocessing approaches do not have an obvious impact on the validation ACC, which coincides with the case for validation MSE. In Figure $2 \mathrm{~b}$ the loss weighing factor $\alpha$ does not present an obvious impact on the validation ACC. Similar to the impact on the validation MSE, a greater learning rate positively affects the ACC. The influence of the weight decay magnitude is clearer compared with it on the validation MSE, where a lower weight decay leads to higher ACC. Conversely, the impact of the batch size is not as evident as it is for the validation MSE, but a smaller value continues to have a positive impact on the performance. Regarding the choice of optimizers, the AdamW optimizer leads to the most high-ranking configurations. Regarding the neural architecture-related hyperparameters,

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-10.jpg?height=890&width=1616&top_left_y=257&top_left_x=252)

Figure 3: Scatter plot of the quantile-transformed MSE and negative ACC among the search results. The points are color-coded based on the summation of the two objectives, where a lower value indicates better performance.

shown in Figure 2c, a higher number of latent channels is associated with higher ACC, a trend that is less evident in the validation MSE. Regarding the activation functions in the lifting layer, elu seems to be most helpful, but the advantage is not prominent. Similar to the impact on the validation MSE, fewer FNO blocks lead to better ACC. Within each FNO block, the number of Fourier modes to keep does not suggest a straightforward pattern, where having around 20 such nodes results in many highly ranked configurations. The rest of the hyperparameters determining the neural architecture do not present a strong correlation with the validation ACC.

### 5.3 Relationship between MSE and ACC

In the search configuration, we sought to optimize for both lower validation MSE and higher ACC. Given that the composite loss improves learning compared with MSE-only loss, we want to determine whether the two loss terms have any trade-offs. Figure 3 shows the scatter plot of the MSE and negative ACC values among the search results. The values are quantile transformed for easy comparison. The plot suggests no trade-off between the MSE and negative ACC. The optimal configuration in the search results led to the lowest MSE and negative ACC. This aligns with our observation, where negative ACC helped lower MSE in the baseline configuration.

While the MSE penalizes large errors and focuses on minimizing the average squared error between the forecast and ground truth, ACC pays more attention to the deviation from the mean field, encouraging the model to capture the patterns more accurately. From our experiment, ACC improved overall learning and helped reduce MSE, which might stem from smoothing the optimization landscape or introducing a beneficial gradient that led to easier and faster convergence. Therefore, the simple addition of negative ACC might benefit ocean modeling or climate modeling in general using FNOs. We plan to investigate the phenomenon and test this hypothesis in future work.

### 5.4 Train with Optimal Configuration

With the search results, we selected the hyperparameter configuration that produced the best performance in both validation MSE and ACC and a model for 100 epochs to report its testing performance and autoregressive rollout scores. Table 3 shows the performance among all the variables of interest using the model trained with the baseline configuration and optimal configuration from the search. The optimal configuration outperforms the baseline for all four variables regarding the ACC score, while the baseline has a slight advantage in terms of the MSE for meridional velocity profiles.
(a)
![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-11.jpg?height=474&width=1612&top_left_y=480&top_left_x=257)

(b)
![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-11.jpg?height=464&width=1610&top_left_y=1036&top_left_x=259)

Figure 4: Meridional velocity profiles of model predictions using the testing set. Both models, with different hyperparameters, were trained with 100 epochs using the composite loss function. (a) shows the model performance with the baseline hyperparameter configuration; (b) shows the model with the best configuration from the search results.

Table 3: MSE and ACC scores of the baseline model with the optimal configuration from the search results.

|  | Baseline |  | Optimal |  |
| :--- | :---: | :---: | :---: | :---: |
|  | $\log (R S E) \downarrow$ | $\log (1-A C C) \downarrow$ | $\log (R S E) \downarrow$ | $\log (1-A C C) \downarrow$ |
| Salinity | -2.498 | -2.800 | -3.143 | -3.552 |
| Temperature | -3.061 | -3.362 | -3.984 | -4.286 |
| Meridional V. | -2.067 | -2.842 | -2.921 | -3.254 |
| Zonal V. | -2.303 | -2.808 | -3.013 | -3.349 |

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-12.jpg?height=504&width=791&top_left_y=331&top_left_x=274)

(b)

![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-12.jpg?height=502&width=783&top_left_y=329&top_left_x=1061)

(c)
![](https://cdn.mathpix.com/cropped/2024_04_26_599a91e566e9bbfffc86g-12.jpg?height=422&width=1602&top_left_y=916&top_left_x=260)

Figure 5: Rollout performance comparison between the models with baseline hyperparameters and searched optimal configurations. (a) shows the rollout MSE values where the error accumulation is much slower for the model with the optimal configuration; (b) shows the rollout ACC scores where the model with default configuration degrades quickly as the rollout horizon increases; (c) shows the model rollout forecasts at Day 10 for meridional velocity profiles.

The slight improvement is amplified by reapplying the trained models for a longer horizon rollout. Figure 5 shows the model autoregressive rollout performance among the trajectories in the testing dataset. We generated the rollouts by providing the ground truth state variable values at the beginning and used the model to produce the forecast for the next time step. Then, we fed the forecast to the same model as input and obtained the prediction for the next. This process was repeated 29 times, generating forecasting trajectories for an entire month. Both baseline and optimal models start around the same performance. However, the baseline model quickly degrades. Regarding the model with the baseline configurations, the MSE growth rates are similar among the four variables, while meridional velocity shows the earlier ACC degradation and a higher decreasing rate. In comparison, the model using the optimal configurations displays very low error accumulation in MSE and a minimal decrease in the ACC score. Figure 5c shows the visualization of the rollout meridional velocity profiles on Day 10 from the models with baseline and optimal configurations. The optimal configuration greatly has improved the model's autoregressive performance, allowing more accurate longer horizon forecasts.

## 6 Conlusion

We explored streamlining data-driven ocean modeling using Fourier neural operators with hyperparameter search. In particular, we focused on forecasting four prognostic variables for an idealized baroclinic wind-driven ocean model. We proposed incorporating the anomaly correlation coefficient in the loss function as a simple improvement to address the potential drawbacks of the mean squared error loss function in model training. The hyperparameter search adopted multiobjective optimization to minimize validation MSE and maximize ACC simultaneously. The optimal configuration obtained from the search results improves the model performance for all four variables, which leads to immense improvement in the model's autoregressive rollout performance. We have demonstrated that hyperparameter
optimization can dramatically improve the performance of FNOs by targeting specific objectives, which consolidates high-performing ocean modeling using deep neural networks such as FNOs. Future work includes exploring more efficient function evaluation strategies during the search that allow more reduction in resource consumption, such as one-epoch and multifidelity approaches, and analyzing the effect of negative ACC on the loss landscape and optimization.

Acknowledgments This research used resources from the Argonne Leadership Computing Facility at Argonne National Laboratory. This material is based upon work supported by the U.S. Department of Energy, Office of Science, Office of Advanced Scientific Computing Research, and Office of Biological and Environmental Research, Scientific Discovery through Advanced Computing (SciDAC) program under Award Number(s) 9233218CNA000001.

## References

[1] T. Kurth, S. Treichler, J. Romero, M. Mudigonda, N. Luehr, E. Phillips, A. Mahesh, M. Matheson, J. Deslippe, M. Fatica, et al., "Exascale deep learning for climate analytics," in SC18: International conference for high performance computing, networking, storage and analysis, pp. 649-660, IEEE, 2018.

[2] S. Rasp, M. S. Pritchard, and P. Gentine, "Deep learning to represent subgrid processes in climate models," Proceedings of the National Academy of Sciences, vol. 115, no. 39, pp. 9684-9689, 2018.

[3] T. Nguyen, J. Brandstetter, A. Kapoor, J. K. Gupta, and A. Grover, "Climax: A foundation model for weather and climate," arXiv preprint arXiv:2301.10343, 2023.

[4] P. B. Gibson, W. E. Chapman, A. Altinok, L. Delle Monache, M. J. DeFlorio, and D. E. Waliser, "Training machine learning models on climate model output yields skillful interpretable seasonal precipitation forecasts," Communications Earth \& Environment, vol. 2, no. 1, p. 159, 2021.

[5] J. Pathak, S. Subramanian, P. Harrington, S. Raja, A. Chattopadhyay, M. Mardani, T. Kurth, D. Hall, Z. Li, K. Azizzadenesheli, et al., "FourCastNet: A global data-driven high-resolution weather model using adaptive fourier neural operators," arXiv preprint arXiv:2202.11214, 2022.

[6] L. Cheng, K. E. Trenberth, J. Fasullo, T. Boyer, J. Abraham, and J. Zhu, "Improved estimates of ocean heat content from 1960 to 2015," Science Advances, vol. 3, no. 3, p. e1601545, 2017.

[7] Y. Gou, T. Zhang, J. Liu, L. Wei, and J.-H. Cui, "DeepOcean: A general deep learning framework for spatiotemporal ocean sensing data prediction," IEEE Access, vol. 8, pp. 79192-79202, 2020.

[8] Y. Choi, Y. Park, J. Hwang, K. Jeong, and E. Kim, "Improving ocean forecasting using deep learning and numerical model integration," Journal of Marine Science and Engineering, vol. 10, no. 4, p. 450, 2022.

[9] S. Partee, M. Ellis, A. Rigazzi, A. E. Shao, S. Bachman, G. Marques, and B. Robbins, "Using machine learning at scale in numerical simulations with smartsim: An application to ocean climate modeling," Journal of Computational Science, vol. 62, p. 101707, 2022.

[10] Y. Zhu, R.-H. Zhang, J. N. Moum, F. Wang, X. Li, and D. Li, "Physics-informed deep-learning parameterization of ocean vertical mixing improves climate simulations,” National Science Review, vol. 9, no. 8, p. nwac044, 2022.

[11] A. P. Guillaumin and L. Zanna, "Stochastic-deep learning parameterization of ocean momentum forcing," Journal of Advances in Modeling Earth Systems, vol. 13, no. 9, p. e2021MS002534, 2021.

[12] L. Zanna and T. Bolton, "Data-driven equation discovery of ocean mesoscale closures," Geophysical Research Letters, vol. 47, no. 17, p. e2020GL088376, 2020.

[13] L. Liao, H. Li, W. Shang, and L. Ma, "An empirical study of the impact of hyperparameter tuning and model optimization on the performance properties of deep neural networks," ACM Transactions on Software Engineering and Methodology (TOSEM), vol. 31, no. 3, pp. 1-40, 2022.

[14] K. Bi, L. Xie, H. Zhang, X. Chen, X. Gu, and Q. Tian, "Pangu-Weather: A 3D high-resolution model for fast and accurate global weather forecast," 2022.

[15] A. Mustafa, A. Mikhailiuk, D. A. Iliescu, V. Babbar, and R. K. Mantiuk, "Training a task-specific image reconstruction loss," 2021.

[16] H. Zhao, O. Gallo, I. Frosio, and J. Kautz, "Loss functions for image restoration with neural networks," IEEE Transactions on Computational Imaging, vol. 3, no. 1, pp. 47-57, 2016.

[17] J. Johnson, A. Alahi, and L. Fei-Fei, "Perceptual losses for real-time style transfer and super-resolution," in Computer Vision-ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part II 14, pp. 694-711, Springer, 2016.

[18] A. H. Murphy and E. S. Epstein, "Skill scores and correlation coefficients in model verification," Monthly Weather Review, vol. 117, no. 3, pp. 572-582, 1989.

[19] Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, and A. Anandkumar, "Fourier neural operator for parametric partial differential equations," arXiv preprint arXiv:2010.08895, 2020.

[20] P. Balaprakash, M. Salim, T. D. Uram, V. Vishwanath, and S. M. Wild, "DeepHyper: Asynchronous hyperparameter search for deep neural networks," in 2018 IEEE 25th international conference on high performance computing (HiPC), pp. 42-51, IEEE, 2018.

[21] P. Balaprakash, R. Egele, M. Salim, R. Maulik, V. Vishwanath, S. Wild, et al., "'deephyper: A python package for scalable neural architecture and hyperparameter search"," 2018.

[22] R. Lam, A. Sanchez-Gonzalez, M. Willson, P. Wirnsberger, M. Fortunato, F. Alet, S. Ravuri, T. Ewalds, Z. EatonRosen, W. Hu, et al., "Learning skillful medium-range global weather forecasting," Science, vol. 382, no. 6677, pp. 1416-1421, 2023.

[23] J. Guibas, M. Mardani, Z. Li, A. Tao, A. Anandkumar, and B. Catanzaro, "Adaptive Fourier neural operators: Efficient token mixers for transformers," arXiv preprint arXiv:2111.13587, 2021.

[24] Z. Li, H. Zheng, N. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, and A. Anandkumar, "Physicsinformed neural operator for learning partial differential equations," 2023.

[25] V. Fanaskov and I. Oseledets, "Spectral neural operators," 2022.

[26] T. J. Grady, R. Khan, M. Louboutin, Z. Yin, P. A. Witte, R. Chandra, R. J. Hewett, and F. Herrmann, "Towards large-scale learned solvers for parametric PDEs with model-parallel Fourier neural operators," ArXiv, vol. abs/2204.01205, 2022.

[27] T. Zhang, D. O. Trad, and K. A. Innanen, "Learning to solve the elastic wave equation with Fourier neural operators," GEOPHYSICS, 2023.

[28] S. Bire, B. Lütjens, K. Azizzadenesheli, A. Anandkumar, and C. N. Hill, "Ocean emulation with Fourier neural operators: Double gyre," Authorea Preprints, 2023.

[29] F. Hutter, H. H. Hoos, and K. Leyton-Brown, "Sequential model-based optimization for general algorithm configuration," in Learning and Intelligent Optimization, 2011.

[30] D. R. Jones, M. Schonlau, and W. J. Welch, "Efficient global optimization of expensive black-box functions," Journal of Global Optimization, vol. 13, pp. 455-492, 1998.

[31] R. Egelé, I. Guyon, V. Vishwanath, and P. Balaprakash, "Asynchronous decentralized Bayesian optimization for large scale hyperparameter optimization," in 2023 IEEE 19th International Conference on e-Science (e-Science), pp. 1-10, IEEE, 2023.

[32] J. T. Wilson, R. Moriconi, F. Hutter, and M. P. Deisenroth, "The reparameterization trick for acquisition functions," arXiv preprint arXiv:1712.00424, 2017.

[33] J. Snoek, H. Larochelle, and R. P. Adams, "Practical Bayesian optimization of machine learning algorithms," Advances in Neural Information Processing Systems, vol. 25, 2012.

[34] D. Ginsbourger, R. L. Riche, and L. Carraro, "Kriging is well-suited to parallelize optimization," in Computational intelligence in expensive optimization problems, pp. 131-162, Springer, 2010.

[35] P. Geurts, D. Ernst, and L. Wehenkel, "Extremely randomized trees," Machine Learning, vol. 63, pp. 3-42, 2006.

[36] L. Breiman, "Random forests," Machine Learning, vol. 45, pp. 5-32, 2001.

[37] P. Kadlec and Z. Raida, "Multi-objective self-organizing migrating algorithm," Self-Organizing Migrating Algorithm: Methodology and Implementation, pp. 83-103, 2016.

[38] M. Ehrgott, Multicriteria optimization, vol. 491. Springer Science \& Business Media, 2005.

[39] R. Égelé, T. Chang, Y. Sun, V. Vishwanath, and P. Balaprakash, "Parallel multi-objective hyperparameter optimization with uniform normalization and bounded objectives," arXiv preprint arXiv:2309.14936, 2023.

[40] N. Zrira, A. Kamal-Idrissi, R. Farssi, and H. A. Khan, "Time series prediction of sea surface temperature based on BiLSTM model with attention mechanism," Journal of Sea Research, p. 102472, 2024.

[41] A. Colin, P. Tandeo, C. Peureux, R. Husson, N. Longépé, and R. Fablet, "Rain regime segmentation of sentinel1 observation learning from NEXRAD collocations with convolution neural networks," IEEE Transactions on Geoscience and Remote Sensing, 2024.

[42] Y. Sun, E. Cucuzzella, S. Brus, S. H. K. Narayanan, B. Nadiga, L. Van Roekel, J. Hückelheim, and S. Madireddy, "Surrogate neural networks to estimate parametric sensitivity of ocean models," arXiv preprint arXiv:2311.08421, 2023.

[43] P. J. Wolfram, T. D. Ringler, M. E. Maltrud, D. W. Jacobsen, and M. R. Petersen, "Diagnosing isopycnal diffusivity in an eddying, idealized midlatitude ocean basin via lagrangian, in situ, global, high-performance particle tracking (LIGHT)," Journal of Physical Oceanography, vol. 45, no. 8, pp. 2114-2133, 2015.

[44] F. Alrasheedi, X. Zhong, and P.-C. Huang, "Padding module: Learning the padding in deep neural networks," IEEE Access, vol. 11, pp. 7348-7357, 2023.

[45] Y. Bengio, "Practical recommendations for gradient-based training of deep architectures," 2012.

[46] D. P. Kingma and J. Ba, "Adam: A method for stochastic optimization," 2017.


[^0]:    ${ }^{*}$ Corresponding Author

