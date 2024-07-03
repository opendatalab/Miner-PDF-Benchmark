# Some variation of COBRA in sequential learning setup 

Aryan Bhambu ${ }^{\mathrm{a}}$, Arabin Kumar $^{\text {Dey }}{ }^{b}, *$<br>${ }^{a}$ Department of Mathematics, Indian Institute of<br>Technology, Guwahati, 781039, Assam, India<br>${ }^{b}$ Department of Mathematics, Indian Institute of<br>Technology, Guwahati, 781039, Assam, India


#### Abstract

This research paper introduces innovative approaches for multivariate time series forecasting based on different variations of the combined regression strategy. We use specific data preprocessing techniques which makes a radical change in the behaviour of prediction. We compare the performance of the model based on two types of hyper-parameter tuning Bayesian optimisation (BO) and Usual Grid search. Our proposed methodologies outperform all state-of-the-art comparative models. We illustrate the methodologies through eight time series datasets from three categories: cryptocurrency, stock index, and short-term load forecasting.


Keywords: Time Series Forecasting, Forecast combination, Machine learning, Deep Neural network, Ensemble Learning, Bayesian Optimisation.

## 1. Introduction

Multivariate time series forecasting is essential as it considers the interdependencies among multiple variables, providing a more accurate understanding of complex systems [5]. This approach proves valuable in the fields such as finance, economics, and environmental monitoring, allowing organisations to make more informed decisions by capturing underlying relationships between variables.[^0]

Researchers used not just deep learning techniques to predict future values in both univariate and multivariate time series, but also created elegant framework where they accommodated large number of machine learning models which are specifically meant for independent datasets. Multiple researchers used different regression based models like Multiple Linear regression, Ridge, LASSO, Support Vector Regression (SVR) ([16), Decision tree based approaches to forecast time-series of various nature.

Deep Neural Networks (DNN), particularly recurrent neural networks like Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and Highway Long Short-Term Memory (Highway-LSTM), gained prominence due to their powerful generalisation and scalability [9, 4, 23]. Literature contains even comparative studies between traditional methods like ARIMA and advanced neural network models such as LSTM and GRU for time series forecasting [19, 8]. These studies demonstrate the superiority of certain deep learning models, such as GRU, in specific forecasting tasks like traffic time series forecasting [8]. Hybrid time series forecasting models integrate diverse techniques, combining statistical methods and machine learning to enhance accuracy and adaptability, capturing both linear and non-linear patterns in the data [7, 10]. Fathi proposed a hybrid model that merges ARIMA and LSTM for sales forecasting [7. Islam et al. [10] introduced a hybrid LSTM model composed of GRU and LSTM for time series forecasting, demonstrating its superiority over alternative models. [22] proposed a transformerbased model for long sequence time-series forecasting and fully utilise the self-attention mechanism to deal with super long sequences, outperforming the existing models on four large-scale datasets.

Researchers over the years constantly focused on improving the accuracy by the introducing many ensemble algorithms. K-NN ensemble [13] leverages the collective insights of its nearest neighbours to make predictions, effectively capturing non-linear relationships in time series data. Similarly, AdaBoost [18] sequentially combines weak learners to enhance overall predictive accuracy, while XGBoost [ [16, [6], [17]], a powerful ensemble method, excels in capturing complex temporal dependencies through boosting. However, these ensembles use regression based weak learners. A framework for ensemble learning methods with sequential learning based Deep Neural Networks as weak learners are not available in the literature.

Distance-based ensembles are important as they enhance model robustness by leveraging diverse algorithms, reducing overfitting, and improving generalisation across varying data patterns. By considering the dissimilarity
between instances, these ensembles excel at capturing complex relationships in data, leading to more reliable and accurate predictions [11, 20, 21]. We propose a non-linear way of combining estimators, adding to a streamline of works pioneered by Mojirsheibani [14]. Our methods Dynamic Proximity Ensemble (DPE) model extends the COBRA (Combined Regression Strategy) algorithm introduced by Biau et al. [3]. There is no work available based on COBRA in sequential learning framework so far.

In the domain of time series forecasting, which involves preprocessing, sequence modelling, independent forecasting, and aggregation, tuning numerous hyper-parameters is essential for accurate predictions. While grid search is commonly employed due to its simplicity, it can be time-consuming and biased without correlation. The motivation behind applying the Bayesian Optimisation Algorithm (BOA) [15] in hyper-parameter tuning lies in controlling time complexity and preserving balance in exploitation and exploration. The effectiveness of BOA in improving hyper-parameter tuning for various prediction models, including attention-based LSTM, PM2.5 prediction, and COVID-19 prediction are available in different research articles [[2], [1], and [12]]. These works validate the superiority of BOA over baseline models in achieving optimised model performance [2, 1, 12]. The paper explores the implementation of BOA in all proposed variations and highlight the best model in this context.

The organisation of the paper goes as follows. Section 2 demonstrates the all proposed methodologies adapted in this sequential learning setup. Section 3 describes implementation structure of Bayesian Optimisation for Hyper-parameter Tuning on the proposed setup. Details of the framework for empirical studies on different datasets are available in Section 4. We discuss the empirical results in Section 5. Section 6 describes dynamic prediction in this context. We conclude the paper in Section 7.

### 1.1. Contributions of our proposed model

The main contribution of the paper are:

1. The paper would be first contribution of COBRA in sequential learning setup in multi-dimensional signal.
2. We explore two different variation of COBRA, Dynamic Proximity Ensemble and Partitioned Dynamic Proximity Ensemble respectively for multivariate time series forecasting.
3. We observe Dynamic Proximity Ensemble outperforms all other variations of COBRA and existing state or the models with respect to the two metrics considered in this paper.
4. We apply the computationally efficient Bayesian optimisation algorithm to automatically search the optimal ensemble configurations.
5. We experiment with the eight different time series datasets having three groups of datasets: Cryptocurrency, Stock Index, and Australian Energy Market Operator. The computational and statistical experiments evidence superiority of our proposed model over others.

## 2. Proposed Methodologies

### 2.1. Dynamic Proximity based Ensemble (DPE)

Let us assume the dataset $D_{\text {ori }}=\left\{\left(Y_{11}, \cdots Y_{N 1}\right), \ldots,\left(Y_{1 T}, \cdots, Y_{N T}\right)\right\}$ and $D_{\text {ori }}=\left(\underline{Y}_{1}, \cdots, \underline{Y}_{T}\right) \in \mathbb{R}^{N}$. The initial objective is to make one step ahead prediction in a time-series data or to find out the expectation of $\underline{Y}_{T}$ given $\mathcal{F}_{T-1}=\left\{\underline{Y}_{1}, \underline{Y}_{2}, \cdots, \underline{Y}_{T-1}\right\}$

The current form of COBRA available in the literature so far is valid for independent datasets which is meant for usual regression purpose or with an extension in functional regression (Goswami et al. ).

We propose the following initial steps to transfer the time series problems into a similar framework/design that can mimic the existing COBRA. We use sliding window to create the frames. It will help to transfer the whole data into series of exchangeable datasets with a specific window length of covariates and a target variable to perform COBRA on these exchangeable sets.

In multidimensional data, we are creating a tensor $\left(D_{1}\right)$ where each matrix will consist of exchangeable set of elements. Thus, we can use COBRA in multi-dimensional time series framework.

Let us denote the i-th frame/matrix with $l$ time step of the tensor is

$$
F_{i}^{l}=\left[\begin{array}{ccccc}
Y_{1, i} & Y_{1, i+1} & Y_{1, i+2} & \ldots & Y_{1, i+l} \\
Y_{2, i} & Y_{2, i+1} & Y_{2, i+2} & \ldots & Y_{2, i+l} \\
\ldots \ldots & \ldots & \ldots \ldots & \ldots & \ldots \\
Y_{N, i} & Y_{2, i+1} & Y_{2, i+2} & \ldots & Y_{N, i+l}
\end{array}\right]
$$

Thus, $D_{1}=\left\{F_{1}^{l}, \cdots, F_{T-l+1}^{l}\right\}$.

We further create a new set of exchangeable sets taking both frames of covariates and the target observations. We call the set as $D^{c o b}$. Therefore, $D^{c o b}=\left\{\left(F_{1}^{l}, \underline{Y}_{1}\right), \cdots,\left(F_{T-l+1}^{l}, \underline{Y}_{T-l+1}\right)\right\}$.

According to our proposition, we divide $D^{c o b}$ into train, validation and test set. For better understanding of the methodology, let us consider training set $D_{n}=\left\{\left(F_{1}^{l}, \underline{Y}_{1}\right), \cdots,\left(F_{n}^{l}, \underline{Y}_{n}\right)\right\}$ and validation set $D_{v}=\left\{\left(F_{n+1}^{l}, \underline{Y}_{n+1}\right) \cdots,\left(F_{n+v}^{l}, \underline{Y}_{n+v}\right)\right\}$.

In the DPE framework, $M$ competing estimators, referred to as machines, are employed. Each machine $m$ is trained on $D_{n}$ and denoted as $r_{t r}^{1}, r_{t r}^{2}, \ldots, r_{t r}^{M}$, with $r_{t r}^{i}$ representing a machine trained exclusively on $D_{n}$ (train) capable of estimating $E\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ for any $x \in \mathbb{R}^{t-1}$. The DPE estimate of $E\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ is then formulated as :

$$
\hat{E}_{D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)=\sum_{i=1}^{n} W_{n, i}(x) \underline{Y}_{i}
$$

The weight $W_{n, i}(x)$ for the $i$-th sample in $D_{n}$ is defined by:

$$
W_{n, i}(x)=\frac{I\left(\bigcap_{m=1}^{M}\left\|r_{t r}^{m}\left(F_{i}^{l}\right)-r_{t r}^{m}(x)\right\| \leq \epsilon\right)}{\sum_{j=1}^{n} I\left(\bigcap_{m=1}^{M}\left\|r_{t r}^{m}\left(F_{j}^{l}\right)-r_{t r}^{m}(x)\right\| \leq \epsilon\right)}
$$

Here, $\epsilon$ is distance threshold, a user-specified parameter. The weight reflects the consensus across machines regarding the proximity of the $i$ th frame to the query frame $x$. Specifically, if the $i$ th frame is close to $x$ in all machines, the weight is 1 ; otherwise, if it is distant in any machine, the weight is 0 . A new parameter, $\alpha$, determines the minimum number of concurring machines for the weight to be 1 , thus introducing an element of consensus. The weight can be expressed as:

$$
W_{n, i}(x)=\frac{I\left(\sum_{m=1}^{M} \mid I\left(\mid r_{t r}^{m}\left(F_{i}^{l}\right)-r_{t r}^{m}(x) \| \leq \epsilon\right) \geq M \alpha\right)}{\sum_{j=1}^{n} I\left(\sum_{m=1}^{M} I\left(\left\|r_{t r}^{m}\left(F_{j}^{l}\right)-r_{t r}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}
$$

### 2.2. Partition-Dynamic Proximity based Ensemble (PaDPE)

PaDPE also initially starts with three division of the data : training, validation and test. However, we divide further the training dataset $D_{n}$ into two distinct parts in PaDPE : $D_{n_{1}}=\left(F_{1}^{l}, \underline{Y}_{1}\right), \ldots\left(F_{n_{1}}^{l}, \underline{Y}_{n_{1}}\right)$ and $D_{n_{2}}=$ $\left(F_{n_{1}+1}^{l}, \underline{Y}_{n_{1}+1}\right), \ldots,\left(F_{n}^{l}, \underline{Y}_{n}\right)$, where $n_{2}=n-n_{1} \geq 1$. We denote validation set as $D_{v}=\left\{\left(F_{n+1}^{l}, \underline{Y}_{n+1}\right) \cdots,\left(F_{n+v}^{l}, \underline{Y}_{n+v}\right)\right\}$.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-06.jpg?height=688&width=1341&top_left_y=453&top_left_x=381)

Figure 1: The schematic representation of the Dynamic Proximity Ensemble (DPE) approach. It condenses the model into four key phases: fine-tuning of model candidates' hyper-parameters, configuring combinations via the Bayesian optimisation algorithm (BOA), retraining the model candidates, generating the ensemble output with the optimal combination configuration.

In the PaDPE framework, $M$ competing estimators, referred to as machines, are employed. Each machine $m$ is trained on $D_{n_{1}}$ and denoted as $r_{n_{1}}^{1}, r_{n_{1}}^{2}, \ldots, r_{n_{1}}^{M}$, with $r_{n_{1}}^{i}$ representing a machine trained exclusively on $D_{n_{1}}$ capable of estimating $\hat{E}_{\text {PaDPE }}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ for any $x \in \mathbb{R}^{l \times N}$. The PaDPE estimate of $\hat{E}_{P a D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ is then formulated as:

$$
\hat{E}_{P a D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)=\sum_{i=1}^{n} W_{n, i}(x) \underline{Y}_{i}
$$

The weight $W_{n, i}(x)$ for the $i$ th sample in $D_{n}$ is defined by:

$$
W_{n, i}(x)=\frac{I\left(\bigcap_{m=1}^{M}\left\|r_{n_{1}}^{m}\left(F_{i}^{l}\right)-r_{n_{1}}^{m}(x)\right\| \leq \epsilon\right)}{\sum_{j=1}^{n} I\left(\bigcap_{m=1}^{M}\left\|r_{n_{1}}^{m}\left(F_{j}^{l}\right)-r_{n_{1}}^{m}(x)\right\| \leq \epsilon\right)}
$$

Here, $\epsilon$ is distance threshold, a user-specified parameter. The weight reflects the consensus across machines regarding the proximity of the $i$ th
sample to the query point $x$. Specifically, if the $i$ th sample is close to $x$ in all machines, the weight is 1 ; otherwise, if it is distant in any machine, the weight is 0 . A new parameter, $\alpha$, determines the minimum number of concurring machines for the weight to be 1 , thus introducing an element of consensus. The weight can be expressed as:

$$
W_{n, i}(x)=\frac{I\left(\sum_{m=1}^{M} I\left(\left\|r_{n_{1}}^{m}\left(F_{i}^{l}\right)-r_{n_{1}}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}{\sum_{j=1}^{n} I\left(\sum_{m=1}^{M} I\left(\left\|r_{n_{1}}^{m}\left(F_{j}^{l}\right)-r_{n_{1}}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}
$$

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-07.jpg?height=691&width=1336&top_left_y=985&top_left_x=381)

Figure 2: The schematic representation of the Partition-Dynamic Proximity Ensemble (PaDPE) approach. It condenses the model into four key phases: fine-tuning of model candidates' hyper-parameters, configuring combinations via the Bayesian optimisation algorithm (BOA), retraining the model candidates, generating the ensemble output with the optimal combination configuration.

### 2.3. Training

Moreover, detailed explanations regarding the training methods for the proposed algorithms are available in algorithms 1 and 2. This subsection provides a comprehensive understanding of the steps and processes involved in training the models providing insights into the training procedures for both the DPE and PaDPE algorithms.

To delve into specifics, algorithms 1 and 2 offers a detailed walkthrough of the training process for the DPE and PaDPE algorithm, explaining the steps taken to fine-tune the model parameters and improve its predictive capabilities. This includes initiating the base models, calculating distances between predictions, and determining weights, all contributing to the generation of accurate predictions.

Furthermore, the subsequent section provides a comprehensive overview of Bayesian Optimisation. This serves as a precursor to understanding how both the DPE and PaDPE models undergo optimisation using Bayesian techniques.

```
Algorithm 1 Training Algorithm for DPE network
    Input: Training dataset \(D_{n}\), distance threshold \(\epsilon, M\) number of base
    models, and fraction of base models \(\alpha\).
    Output: Prediction \(\hat{y}\) for any test observation \(x\).
    Train \(M\) base models using the training dataset \(D_{n}\).
    for \(i \leftarrow 1\) to \(n\) do
        Obtain predictions \(r_{t r}^{m}\left(F_{i}^{l}\right)\) for each model \(m\).
        Calculate the distance between \(r_{t r}^{m}\left(F_{i}^{l}\right)\) and \(r_{t r}^{m}(x)\).
    end for
    Calculate the indicator function and weights for each training sample
    with respect to the test observation using \(\epsilon\), and \(\alpha\) from equation 3 .
    : After calculation of weights, calculate their product with the training
        labels \(Y_{i}\), resulting in the prediction \(\hat{y}\) according to Equation (1)
```


### 2.4. Testing

In this study, we delve into testing procedures for the DPE and PaDPE methodologies. These approaches aim to estimate the conditional expectations $\hat{E}_{D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ and $\hat{E}_{P a D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ respectively. Note that $\underline{Y}_{t}$ is a point from test dataset, $F_{t-l-1}^{l}$ is the respective query frame. In a different note, our aim is to make one step ahead forecasting of a multidimensional time series given a new frame.

### 2.4.1. DPE Methodology on Test dataset

For the DPE method, proximity frames are from the combined dataset comprising of predictions from both $D_{n}$ (training data) and $D_{v}$ (validation data). The DPE estimate of $\hat{E}_{D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ is formulated as:

Algorithm 2 Training Algorithm for PaDPE network

Input: Training dataset $D_{n}$, fraction $\frac{n_{1}}{n}$, distance threshold $\epsilon, M$ number of base models, and fraction of base models $\alpha$.

Output: Prediction $\hat{y}$ for any test observation $x$.

1: Partition the training dataset $D_{n}$ into $D_{n_{1}}$, and $D_{n_{2}}$ using the fraction $\frac{n_{1}}{n}$.

Train $M$ base models on the dataset $D_{n_{1}}$.

for $i \leftarrow 1$ to $n$ do

Obtain predictions $r_{n_{1}}^{m}\left(F_{i}^{l}\right)$ for each model $m$.

Calculate the distance between $r_{n_{1}}^{m}\left(F_{i}^{l}\right)$ and $r_{n_{1}}^{m}(x)$.

end for

: Calculate the indicator function and weights for each training sample with respect to the test observation using $\epsilon$, and $\alpha$ from equation 6 .

8: After calculation of weights, calculate their product with the training labels $Y_{i}$, resulting in the prediction $\hat{y}$ according to Equation 4 .

$$
\hat{E}_{D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)=\sum_{i=1}^{n} W_{n, i}(x) \underline{Y}_{i}
$$

Here, the weights $\left(W_{n v, i}(x)\right)$ are computed using the following equation:

$$
W_{n v, i}(x)=\frac{I\left(\sum_{m=1}^{M} I\left(\left\|r_{t r}^{m}\left(F_{i}^{l}\right)-r_{t r}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}{\sum_{j=1}^{n+v} I\left(\sum_{m=1}^{M} I\left(\left\|r_{t r}^{m}\left(F_{j}^{l}\right)-r_{t r}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}
$$

In this formulation, $r_{t r}^{m}\left(F_{i}\right)$ represents the $\mathrm{m}$-th machine for the frame $F_{i}^{l}$ where $F_{i}^{l}$ is some arbitrary frame from combined set $D_{n}$ and $D_{v}$, and $\epsilon$ and $\alpha$ are threshold parameters.

### 2.4.2. PaDPE Methodology

In PaDPE Methodology, the testing space is similar to the tuning space. Proximity set consists of predictions from a smaller training set as well as predictions on new points in both during tuning parameters and prediction on new query points from test dataset.

The PaDPE methodology involves a more extensive proximity point set consists of predictions on a combined space of $D_{n_{1}}$ and $D_{n_{2}}$ and validation
data $D_{v}$. The PaDPE estimate of $\hat{E}_{P a D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)$ follows a similar formulation as the DPE method:

$$
\hat{E}_{P a D P E}\left(\underline{Y}_{t} \mid F_{t-l-1}^{l}=x\right)=\sum_{i=1}^{n} W_{n, i}(x) \underline{Y}_{i}
$$

where, $F_{t-l-1}^{l}=x$ is the query frame from test dataset.

The corresponding weight calculation is given by:

$$
W_{n v, i}(x)=\frac{I\left(\sum_{m=1}^{M} I\left(\left\|r_{n_{1}}^{m}\left(F_{i}^{l}\right)-r_{n_{1}}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}{\sum_{j=1}^{n+v} I\left(\sum_{m=1}^{M} I\left(\left\|r_{n_{1}}^{m}\left(F_{j}^{l}\right)-r_{n_{1}}^{m}(x)\right\| \leq \epsilon\right) \geq M \alpha\right)}
$$

In this context, $r_{n_{1}}^{m}\left(F_{i}^{l}\right)$ denotes the $\mathrm{m}$-th machine for the frame $F_{i}^{l}$ from a combined space of $D_{n_{1}}$ and $D_{n_{2}}$ and $D_{v}$. Note that, $\epsilon$ and $\alpha$ remain the threshold parameters.

## 3. Bayesian Optimisation for Hyperparameter Tuning

Multiple hyper parameter together creates large number of possible models. In automated learning one popular technique to select the best model is Bayesian Optimisation which selects the hyper-parameter based on on a surrogate function to model the conditional probability of performance on a validation set. Unlike traditional grid search methods, Bayesian Optimisation Algorithm (BOA) preserves and leverages all prior computations, avoiding redundant evaluations of suboptimal hyper-parameter configurations. The algorithm employs an acquisition function to systematically identify the most promising hyper-parameter configuration for evaluation in subsequent iterations.

The Bayesian Optimisation Algorithm (BOA) comprises five key components: the surrogate function, the hyper-parameter search space, the acquisition function, the objective function, and the historical record of evaluations. In this context, the objective function is defined as the predictive performance on the validation set. The surrogate function is established using the Tree-based Parzen Window Estimation (TPE) algorithm, and the selected acquisition function is the expected improvement. The formulation of the acquisition function, denoted as $S_{f^{\star}}(v)$, is expressed as follows:

$$
S_{f^{\star}}(v)=\int_{-\infty}^{f^{\star}}\left(f^{\star}-f\right) P(f \mid v) d f
$$

Here, $f^{\star}$ represents the objective function, and $f$ represents the predefined threshold for the objective function concerning the hyper-parameters $v$. The Tree-based Parzen Estimation (TPE) algorithm encompasses several steps, as elucidated in Algorithm 3 .

```
Algorithm 3 TPE for Hyperparameter Tuning
    \(\mathbb{H}_{v}\), acquisition function validation \(\mathcal{S}\), initialised memory \(\mathcal{D}\).
    Output: Best hyperparameters \(v^{\star}\) in memory \(\mathcal{D}\).
    for \(i \leftarrow 1\) to \(N\) do
        \(P(f \mid v) \leftarrow\) Fit memory \(\mathcal{D}\) using \(\mathcal{M}\)
        \(v_{i+1} \leftarrow\) Maximize acquisition function \(\mathcal{S}\) in Equation
        (11) to determine the next hyper-parameter choice
        \(f\left(v_{i+1}\right) \leftarrow\) Evaluate the objective function
        \(\mathcal{D} \leftarrow \mathcal{D} \cup\left(v_{i+1}, f\left(v_{i+1}\right)\right)\)
    end for
```

Input: Objective function $f$, TPE method $\mathcal{M}$, hyper-parameter space

This algorithm iteratively refines hyper-parameter choices, leveraging the acquisition function to guide the search toward promising regions within the hyper-parameter space. The historical record $\mathcal{D}$ accumulates optimal configurations, ultimately leading to improved model performance.

For our proposed methodology, The objective function aims to minimise the mean squared error. The search space defines hyper-parameter values. The Tree of Parzen Estimators (TPE) algorithm, used implicitly in hyperopt, guides the exploration-exploitation trade-off through its acquisition function, suggesting where to sample for optimal hyper-parameters.

## 4. Empirical Study

This section presents the empirical study conducted on eight time series datasets, comprising cryptocurrency, stock index, and load forecasting time series datasets. The cryptocurrency and stock index finance datasets have been gathered from Yahoo Finance, while the load time series forecasting datasets have been obtained from the Australian Energy Market Operator (AEMO). Initially, we present a brief introduction to the datasets and

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-12.jpg?height=769&width=1203&top_left_y=426&top_left_x=450)

Figure 3: The schematic flowchart of the proposed dynamic proximity ensemble forecasting framework

pre-processing steps. We also describe the assessment metrics, benchmark models, and hyper-parameter optimisation in this context.

### 4.1. Data and its nature

The first three, covering the period from January 1, 2015, to June 30, 2023, are financial datasets from Yahoo Finance. The Bitcoin dataset represents the cryptocurrency's daily market performance. The DJI dataset tracks the Dow-Jones Industrial Average, reflecting the performance of 30 major U.S. companies. The S\&P500 dataset covers 500 large-cap American companies, providing a comprehensive view of the U.S. stock market. All datasets are publicly accessible on Yahoo Finance's official website. Summary of the dataset is available in Table-1.

The subsequent five datasets encompass load data collected from the states of South Australia (SA), New South Wales (NSW), Victoria (VIC), and Tasmania (TAS) for the month of December 2022. The records of data are available for every half an hour, resulting in 48 data points per day. These datasets are also publicly available and can be accessed on the official website of the Australian Energy Market Operator. Table-2 provides a brief summary of load datasets. We also show the data visualisation for the Bit-
coin data: Closing and Volume Price and for NSW data: Total Demand and RRP in the figures: 4 and 5 respectively.

Table 1: Dataset Summary for the Closing price and Volume for the finance datasets

| Dataset Name | Max | Min | Median | Mean | Std | Skewness | Kurtosis |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Bitcoin | 67566.82 | 178.10 | 8041.77 | 14024.54 | 16089.06 | 1.36 | 0.88 |
| DJI | 36799.64 | 15660.17 | 25669.32 | 25783.14 | 6059.98 | 0.06 | -1.23 |
| S\&P 500 | 4796.56 | 1829.07 | 2842.73 | 3046.08 | 830.93 | 0.42 | -1.13 |
| Bitcoin | $350.9 \mathrm{e}+9$ | $\mathrm{e}+9$ | $0.07 \mathrm{e}+9$ | $17.1 \mathrm{e}+9$ | $19.6 \mathrm{e}+9$ | 2.73 | 28.28 |
| DJI | $0.9 \mathrm{e}+9$ | $0.04 \mathrm{e}+9$ | $0.2 \mathrm{e}+9$ | $0.2 \mathrm{e}+9$ | $0.1 \mathrm{e}+9$ | 0.57 | 1.34 |
| S\&P 500 | $9.9 \mathrm{e}+9$ | $1.2 \mathrm{e}+9$ | $3.8 \mathrm{e}+9$ | $4 \mathrm{e}+9$ | $0.9 \mathrm{e}+9$ | 1.69 | 4.87 |

Table 2: Dataset Summary for the Closing price and Total demand of the finance and load time series datasets respectively

| Month | Max | Min | Median | Mean | Std | Skewness | Kurtosis |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| SA | 2834.54 | 119.6 | 1240.97 | 1135.00 | 419.97 | -0.16 | 0.47 |
| NSW | 9575.59 | 4530.54 | 6636.68 | 6721.05 | 902.91 | 0.25 | -0.42 |
| VIC | 8148.52 | 1976.53 | 4194.06 | 4239.37 | 788.26 | 0.54 | 2.18 |
| TAS | 1398.93 | 770.52 | 1079.82 | 1082.54 | 92.08 | 0.18 | -0.26 |
| QLD | 8873.19 | 3859.83 | 5497.31 | 5736.49 | 924.75 | 0.73 | 0.23 |
| SA | 12523.61 | -1000.0 | 23.08 | 35.43 | 180.14 | 42.41 | 2701.58 |
| NSW | 15500.0 | -120.0 | 93.35 | 82.64 | 179.12 | 72.52 | 6168.07 |
| VIC | 316.21 | -937.19 | 19.15 | 31.28 | 71.74 | -0.49 | 7.96 |
| TAS | 15493.4 | -51.65 | 83.85 | 76.35 | 169.75 | 84.00 | 7617.79 |
| QLD | 1250.0 | -122.19 | 92.77 | 85.46 | 80.11 | 1.83 | 15.90 |

We adapt a set of specific data pre-processing techniques to ensure that machine learning models yield precise outputs. In our methodology, first we employ the max-min normalisation technique to refine the raw data. We assume that the highest and lowest values within the training set represented by $x_{\max }$ and $x_{\min }$, respectively. The process transforms the data values in $[0,1]$ using the following equation:

$$
x_{\text {normalized }}=\frac{x-x_{\min }}{x_{\max }-x_{\min }}
$$

Here, $x_{\text {normalized }}$ represents the normalised time series, and $x$ denotes the original time series.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-14.jpg?height=331&width=550&top_left_y=604&top_left_x=386)

(a) Total Demand - Train, Validation, and Test partitions of the raw data short-term load forecast time series data for NSW.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-14.jpg?height=326&width=529&top_left_y=604&top_left_x=1145)

(b) RRP - Train, Validation, and Test partitions of the raw data short-term load forecast time series data for NSW.

Figure 4: Short-term load forecast time series data for New South Wales (NSW) showing the train, validation, and test partitions of the raw data for total demand and RRP respectively.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-14.jpg?height=355&width=545&top_left_y=1584&top_left_x=386)

(a) Closing Price - Train, Validation, and Test partitions of the raw data time series for Bitcoin cryptocurrency.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-14.jpg?height=358&width=510&top_left_y=1583&top_left_x=1165)

(b) Volume - Train, Validation, and Test partitions of the raw data time series for Bitcoin cryptocurrency.

Figure 5: Time series data for Bitcoin crypto-currency, illustrating the train, validation, and test partitions of the raw data for closing price and volume.

To implement cross-validation, we first divide the dataset into three parts: the training set, validation set, and test set. We choose the validation and test sets each with $10 \%$ of the entire dataset. Furthermore, the dataset underwent cumulative sum (cumsum) pre-processing before being subjected to scaling.

### 4.2. Assessment Metrics

4.2.1. Root Mean Square Error ( $R M S E$ )

RMSE measures the average magnitude of the errors between predicted $\left(\hat{y}_{i}\right)$ and actual $\left(y_{i}\right)$ values. Squaring the differences emphasizes larger errors, and taking the square root provides an interpretable metric in the same unit as the target variable. RMSE is sensitive to outliers due to the squaring effect.

$$
\mathrm{RMSE}=\sqrt{\frac{\sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}}{n}}
$$

### 4.2.2. Mean Absolute Percentage Error (MAPE)

MAPE represents the average percentage difference between predicted $\left(\hat{y}_{i}\right)$ and actual $\left(y_{i}\right)$ values. It is particularly useful when dealing with variables of different scales, as it normalizes the error by the magnitude of the actual values. However, MAPE can be problematic when the actual values are close to zero.

$$
\text { MAPE }=\frac{1}{n} \sum_{i=1}^{n}\left(\frac{\left|y_{i}-\hat{y}_{i}\right|}{\left|y_{i}\right|}\right) \times 100
$$

### 4.3. Base Models

In our study, we have employed various deep learning models as the foundation or base models, also referred to as learners. These models are selected for their proficiency in capturing intricate patterns and dependencies within data. The following are the base models utilised in our research:

1. Long Short-Term Memory (LSTM): LSTM is a type of recurrent neural network (RNN) designed to retain long-term dependencies in sequential data, making it effective for tasks involving time-series or sequential information.
2. Gated Recurrent Unit (GRU): Similar to LSTM, GRU is another variant of $R N N$ designed to address the vanishing gradient problem. It simplifies the architecture while maintaining the capability to capture dependencies in sequential data.
3. Hybrid LSTM-GRU Model: This model combines elements of both LSTM and GRU architectures, leveraging their respective strengths to enhance overall performance.
4. Highway LSTM Model: The Highway LSTM model incorporates highway networks with LSTM units, allowing for a more controlled flow of information through the network. This can be beneficial in learning hierarchical representations.
5. Transformer Model: The Transformer model is a non-recurrent architecture that utilises self-attention mechanisms to capture dependencies across different positions in the input sequence simultaneously. It has demonstrated remarkable success in various natural language processing tasks.

### 4.4. Comparison Models

We conduct a comprehensive comparison of our proposed models, DPE and PaDPE, against several state-of-the-art models, encompassing both classical and contemporary approaches. The aim is to evaluate the effectiveness of our models in capturing complex relationships within the data. The comparison includes the following models:

1. Adaptive Boosting
2. Gradient Boosting
3. K-Nearest Neighbours
4. Combined Regression Strategy (COBRA)

This comprehensive selection of base and comparison models provides a thorough foundation for evaluating the proposed models' capabilities and understanding their potential advantages in the context of the specific tasks under consideration.

### 4.5. Hyperparameter Tuning

In the pursuit of a rigorous and equitable comparison among various models, hyper-parameter optimization through cross-validation is employed. The hyper-parameter search space, as delineated in Table 3, serves as a crucial
framework for this optimization process. Certain parameters remain constant throughout the optimisation, maintaining uniformity across all pertinent models. These fixed parameters include a batch size set to 32 , a learning rate fixed at 0.001 , and a fixed number of epochs at 80 .

For models DPE and PaDPE, specific hyper-parameters undergo meticulous tuning through this process. Notably, the parameters subject to tuning encompass the distance parameter denoted as $\epsilon$, the number of machines represented by $\alpha$, and the fraction denoted as $\frac{l}{n}$. The specific range for these hyper-parameters is elucidated in Table 3, guiding the optimisation process to attain optimal model performance.

## 5. Empirical Results and Discussion

### 5.1. Performance evaluation over multivariate time series forecasting

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-17.jpg?height=521&width=1350&top_left_y=1168&top_left_x=385)

Figure 6: The visualization illustrates the Closing Price of the Bitcoin dataset employing the proposed DPE methodology.

Tables 5 and 6 provide a detailed comparison of different forecasting models applied to distinct time series, using metrics like Root Mean Square Error (RMSE) and Mean Absolute Percentage Error (MAPE). Bold highlights in the tables indicate instances where a specific model excels for a given time series. Importantly, the DPE model consistently shows exceptional accuracy across most datasets. While the proposed PaDPE model outperforms others in certain datasets, there is noticeable variability in its results. Additionally, XGBoost ensemble models consistently demonstrate outstanding accuracy compared to their counterparts, highlighting their strong predictive capabilities.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-18.jpg?height=526&width=1309&top_left_y=431&top_left_x=403)

Figure 7: The visualization illustrates the Volume of the Bitcoin dataset employing the proposed DPE methodology.

In this research, we apply the proposed models on a bitcoin finance dataset. A visual representations of the raw price and volume of the dataset are available in Figures 6 and 7 respectively. The figures also present a side-by-side view of DPE predictions on respective test datasets, providing a detailed understanding of the model's predictive strengths. Specifically, the closing and volume prices for the Bitcoin dataset were meticulously studied, shedding light on the model's effectiveness in capturing intricate patterns within financial time series data.

### 5.1.1. Statistical comparison using Wilcoxon's test

Despite these notable performances, selecting the most suitable forecasting method based only on error metrics is challenging due to the competitive outcomes among models. Further analysis is conducted using statistical tests to probe differences among all models. This indicates substantial differences in forecasting models' performances across the eight datasets. The use of statistical tests adds depth to the analysis beyond error metrics, providing insights into the comparative strengths and weaknesses of the forecasting models under consideration.

Table 7 and 8 showcase the results of statistical comparisons involving the proposed models: DPE, PaDPE, and other models used for comparison. These tables display the average ranks, with the model achieving the lowest rank considered the most favourable in terms of performance. The proposed models DPE and PaDPE consistently attains a lower average rank across all tables, as illustrated in Tables 7 and 8 .

### 5.2. Abliation Study

### 5.2.1. Comparative analysis of Two Tuning Methods : BOA and Grid based tuning

The suggested model comprises two crucial elements: BOA hyper-parameter tuning and the proposed methodologies, DPE and PaDPE. To delve into the significance of each component, we conduct an ablation study. This entails the formulation and assessment of five variants, each representing a distinct combination of the model's components. These variants are systematically evaluated across diverse datasets, enabling us to gauge the necessity and impact of each element. The overall performance is then averaged across all datasets, and errors are normalised to accentuate variations among them. The five variants under examination are:

- GridCOBRA: The DPE utilises grid search for parameter optimisation.
- BOACOBRA: The combined regression strategy utilises BOA to optimise parameters in original COBRA.
- GridDPE: The DPE utilises grid search for parameter optimisation.
- BOADPE: The DPE utilises both the BOA for parameter optimisation.
- BOAPaDPE: The PaDPE utilises both the BOA for parameter optimisation.
- GridPaDPE: The PaDPE utilises gridserach for parameter optimisation.

The bar-plots shows the performance of different variations of COBRA in sequential prediction setup with respect to RMSE in Figure-8 8 and Figure-9 respectively. The above comparison between the proposed BOA methodologies and their grid-based counterparts reveals that BOA based models consistently outperform the Grid-search based models. This underlines the robustness and effectiveness of the BOA methodologies in enhancing the study's overall outcomes. Moreover, BOADPE outperforms all models in both the metrics considered in this paper.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-20.jpg?height=734&width=1312&top_left_y=533&top_left_x=428)

Figure 8: The bar-plot of the performance of different variations of COBRA with respect to RMSE

### 5.3. Some Analysis on RMSE and Model Parameters

We adapt a sensitivity analysis for both the proposed methodologies, namely DPE and PaDPE and conduct a simulation study by systematically varying the number of machines represented by the parameter $\alpha$, while maintaining a constant optimal value for $\epsilon$. Subsequently, we varied the parameter $\epsilon$ while keeping $\alpha$ fixed.

These approaches allow us to assess the robustness and performance of both DPE and PaDPE under different conditions. By systematically altering key parameters, namely $\alpha$ and $\epsilon$, we gained insights into how these variations impact the outcomes of the simulation studies.

### 5.3.1. Varying the number of machines

In Figure-10, we systematically explore the interplay between machine numbers, denoted as alpha, and the Mean Squared Error (MSE). We vary alpha values within the range of 1 to 5 and observe a consistent reduction in the Mean Squared Error providing optimal $\alpha$ at 5 for DJI dataset. The

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-21.jpg?height=734&width=1297&top_left_y=530&top_left_x=444)

Figure 9: The bar-plot of the performance of different variations of COBRA with respect to MAPE

above study also indicates that more number of models together improve DPE accuracy, ultimately resulting in a noteworthy reduction in errors.

### 5.3.2. Varying the distance parameter $\epsilon$

We also explore the relation between the distance parameter epsilon and Mean Squared Error (MSE). The study involves a systematic variation of epsilon values, ranging from 0.001 to 0.01 . We keep the alpha parameter at a constant value. Figure-11 shows the curve for MSE with respect to $\epsilon$ convex in nature, finally providing the minimum value of $\epsilon$ at 0.004 .

Our findings provide valuable information on the sensitivity of the proposed methodologies to changes in the number of machines $(\alpha)$ and the threshold parameter, $\epsilon$. This comprehensive analysis enhances our understanding of the behaviour and effectiveness of DPE and PaDPE, contributing to the refinement of these methodologies in all other datasets.

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-22.jpg?height=914&width=1266&top_left_y=546&top_left_x=386)

Figure 10: This barplot illustrates the relation between RMSE and the number of models

## 6. Dynamic Prediction

We assess our model's effectiveness through dynamic predictions, wherein the model operates through dynamically changing scalers. The scaler takes step-by-step update and we fed the scaled data to the model. After obtaining the predictions we inverse-scaled the result and concatenate the same with past data. Time-lagged entries help to preserve temporal context, and we define a new scaler for the next iteration. This iterative process ensures adaptability to evolving data patterns.

The dynamic predictions depicted in Figure-12 showcase the future predictive capabilities of the proposed models. These plots illustrate the predictions conducted on the dynamic scaler, with subsequent inverse scaling concerning dynamic scaler. The visualisations does not strongly emphasise the models' proficiency in dynamic predictions, since the picture is zoomed

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-23.jpg?height=900&width=1268&top_left_y=550&top_left_x=388)

Figure 11: This relation between the MSE and the distance parameter $\epsilon$

closely in ten successive prediction. However, It captures better signal capture for volume than prices. It depends on the practitioner how much accuracy required for certain purpose. We need more improvement and better design in this respect.

## 7. Conclusion

Dynamic-Based Proximity Ensemble Method and Partitioned DynamicBased Proximity Ensemble Method are two proposed variations which exhibit superior performance over a state-of-the-art comparative models. The efficacy of our proposed methodology is further validated through its ability to capture complex temporal patterns across diverse datasets, including cryptocurrency, stock index, and short-term load forecasting. This research contributes to the advancement of forecasting techniques in an arbitrary mul-

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-24.jpg?height=639&width=1114&top_left_y=453&top_left_x=489)

Figure 12: This figure demonstrates dynamic predictions on the Bitcoin dataset using the DPE method, with subsequent inverse scaling performed by the dynamic scaler

tidimensional signals. More improvement of the work is necessary specifically in capturing accurate evolving future data patterns. Additionally, exploring adaptive combinations for the final prediction could enhance the flexibility and robustness of the ensemble method. An interval estimation in this context could be a challenging problem. The work is in progress.

## Declarations

- Funding: The work is not related to any funding.
- Conflict of interest/Competing interests: This work has no conflict of interest or competing interests.
- Ethics approval: The paper does not have any ethics-related issues.
- Consent to participate: All co-authors provide consent to participate in this research article.
- Consent for publication: All co-authors have consented to keep their names in related publications.
- Availability of data and materials: All datasets are publicly available and downloaded directly from Yahoo Finance and AEMO.
- Code availability: The codes are available to each author. We can make it accessible through publicly available through Github link on request.
- Authors' contributions: Aryan Bhambu is the first author of the paper. He was associated with all computation, empirical study, proposed model creation, and manuscript completion. Arabin Kumar Dey is the corresponding author and mentor for the project.


## References

[1] Abbasimehr, H., Paki, R., 2021. Prediction of covid-19 confirmed cases combining deep learning methods and bayesian optimization. Chaos, Solitons \& Fractals 142, 110511.

[2] Alizadeh, B., Bafti, A.G., Kamangir, H., Zhang, Y., Wright, D.B., Franz, K.J., 2021. A novel attention-based lstm cell post-processor coupled with bayesian optimization for streamflow prediction. Journal of Hydrology $601,126526$.

[3] Biau, G., Fischer, A., Guedj, B., Malley, J.D., 2016. Cobra: A combined regression strategy. Journal of Multivariate Analysis 146, 18-28.

[4] Chung, J., Gulcehre, C., Cho, K., Bengio, Y., 2014. Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv: 1412.3555

[5] De Livera, A.M., Hyndman, R.J., Snyder, R.D., 2011. Forecasting time series with complex seasonal patterns using exponential smoothing. Journal of the American statistical association 106, 1513-1527.

[6] Fan, J., Wang, X., Wu, L., Zhou, H., Zhang, F., Yu, X., Lu, X., Xiang, Y., 2018. Comparison of support vector machine and extreme gradient boosting for predicting daily global solar radiation using temperature and precipitation in humid subtropical climates: A case study in china. Energy conversion and management 164, 102-111.

[7] Fathi, O., 2019. Time series forecasting using a hybrid arima and lstm model. Velvet Consulting , 1-7.

[8] Fu, R., Zhang, Z., Li, L., 2016. Using lstm and gru neural network methods for traffic flow prediction, in: 2016 31st Youth academic annual conference of Chinese association of automation (YAC), IEEE. pp. 324328.

[9] Hochreiter, S., Schmidhuber, J., 1997. Long short-term memory. Neural computation 9, 1735-1780.

[10] Islam, M.S., Hossain, E., 2021. Foreign exchange currency rate prediction using a gru-lstm hybrid network. Soft Computing Letters 3, 100009.

[11] Juditsky, A., Nemirovski, A., 2000. Functional aggregation for nonparametric regression. The Annals of Statistics 28, 681-712.

[12] Ma, J., Ding, Y., Cheng, J.C., Jiang, F., Gan, V.J., Xu, Z., 2020. A lagflstm deep learning network based on bayesian optimization for multisequential-variant pm2. 5 prediction. Sustainable Cities and Society 60, 102237.

[13] Martínez, F., Frías, M.P., Pérez, M.D., Rivera, A.J., 2019. A methodology for applying k-nearest neighbor to time series forecasting. Artificial Intelligence Review 52, 2019-2037.

[14] Mojirsheibani, M., 1999. Combining classifiers via discretization. Journal of the American Statistical Association , 600-609.

[15] Snoek, J., Larochelle, H., Adams, R.P., 2012. Practical bayesian optimization of machine learning algorithms. Advances in neural information processing systems 25 .

[16] Tay, F.E., Cao, L., 2001. Application of support vector machines in financial time series forecasting. omega $29,309-317$.

[17] Vuong, P.H., Dat, T.T., Mai, T.K., Uyen, P.H., et al., 2022. Stock-price forecasting based on xgboost and lstm. Computer Systems Science \& Engineering 40.

[18] Wang, J., Chen, Y., 2021. Adaboost-based integration framework coupled two-stage feature extraction with deep learning for multivariate exchange rate prediction. Neural Processing Letters 53, 4613-4637.

[19] Yamak, P.T., Yujian, L., Gadosey, P.K., 2019. A comparison between arima, lstm, and gru for time series forecasting, in: Proceedings of the 2019 2nd international conference on algorithms, computing and artificial intelligence, pp. 49-55.

[20] Yang, Y., 2000. Combining different procedures for adaptive regression. Journal of multivariate analysis 74, 135-161.

[21] Yang, Y., 2004. Aggregating regression procedures to improve performance. Bernoulli $10,25-47$.

[22] Zhou, H., Zhang, S., Peng, J., Zhang, S., Li, J., Xiong, H., Zhang, W., 2021. Informer: Beyond efficient transformer for long sequence timeseries forecasting, in: Proceedings of the AAAI conference on artificial intelligence, pp. $11106-11115$.

[23] Zilly, J.G., Srivastava, R.K., Koutnık, J., Schmidhuber, J., 2017. Recurrent highway networks, in: International conference on machine learning, PMLR. pp. 4189-4198.

Table 3: Hyper-parameter search space for the base and proposed models.

| Model | Parameter | Values |
| :--- | :--- | :--- |
| LSTM | nodes | $[16,32,50,64,96,100,128]$ |
|  | Layers | $[0,1,2,3]$ |
|  | Optimizer | Adam |
|  | Activation | $[$ ReLU, tanh $]$ |
|  | Dropout Rate | $(0,0.5)$ |
| GRU | nodes | $[16,32,50,64,96,100,128]$ |
|  | Layers | $[0,1,2,3]$ |
|  | Optimizer | Adam |
|  | Activation | $[$ ReLU, tanh $]$ |
|  | Dropout Rate | $(0,0.5)$ |
| Hybrid LSTM | LSTM nodes | $[16,32,50,64,96,100,128]$ |
|  | GRU nodes | $[16,32,50,64,96,100,128]$ |
|  | LSTM Layers | $[0,1,2,3]$ |
|  | Optimizer | Adam |
|  | Activation | $[$ ReLU, tanh, sigmoid $]$ |
|  | Dropout Rate | $(0,0.5)$ |
| Highway LSTM | LSTM nodes | $[16,32,50,64,96,100,128]$ |
|  | Layers | $[1,2,3,4,5]$ |
|  | t_bias | $(-5,5)$ |
|  | Optimizer | Adam |
|  | acti.h | ReLU |
|  | acti_t | sigmoid |
|  | learning rate | $(1 e-6,1 e-2)$ |
| Transformer | nodes | $(32,200,2)$ |
|  | Layers | $[1,2,3,4,5]$ |
|  | Optimizer | Adam |
|  | Activation | $[$ ReLU, tanh, sigmoid $]$ |
|  | d k $/$ d_v | $[32,64,96]$ |
|  | learning rate | $(1 e-5,1 e-2)$ |
|  | Dropout Rate | $(0,0.5)$ |
|  | feedforward dimension | $(32,200,2)$ |
|  | Number of heads | $[1,2,4,8,12]$ |
| DPE-based models | $\epsilon$ | $(0,1)$ |
|  | $\alpha$ | $\left[\frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}, 1\right]$ |
|  | $\alpha$ | $(0,1)$ |
|  | $\frac{n_{1}}{n}$ |  |

Table 4: Hyper-parameter search space for the benchmark models.

| Model | Parameter | Values |
| :--- | :--- | :--- |
| AdaBoost | estimators | $[10,50,100,200,300,400,500]$ |
|  | learning Rate | $\left[10^{-3}, 10^{-2}, 10^{-1}\right]$ |
| XGBoost | estimators | $[10,50,100,200,300,400,500]$ |
|  | depth | $[1,2,3,4,5]$ |
|  | subsample | $[0.5,0.6,0.7,0.8,0.9]$ |
|  | child weight | $[2,4,6,8,10]$ |
| K-NN | neighbours | $[1,2,3,4,5]$ |
|  | weights | $[$ uniform, distance $]$ |
|  | $\mathrm{P}$ | $[1,2,3,4,5]$ |
| COBRA | $\epsilon$ | $(0,1)$ |
|  | $\alpha$ | $\left[\frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}, 1\right]$ |
|  | $\frac{l}{n}$ | $(0,1)$ |


| 垉 | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=112&width=99&top_left_y=444&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=112&width=182&top_left_y=444&top_left_x=1070) |
| :---: | :---: | :---: |
| 䞍 | $\stackrel{1}{c}$  0 <br>  0  <br> 0 8 8 <br> 0 0 0 <br> 0 0  | $\left[\begin{array}{llll}\infty & 0 & -1 \\ 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{array}\right.$ |
| ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=133&width=43&top_left_y=681&top_left_x=920) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=133&width=99&top_left_y=681&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=133&width=182&top_left_y=681&top_left_x=1070) |
|  | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=112&width=99&top_left_y=813&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=112&width=185&top_left_y=813&top_left_x=1067) |
| ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=140&width=43&top_left_y=935&top_left_x=920) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=140&width=99&top_left_y=935&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=140&width=182&top_left_y=935&top_left_x=1067) |
| ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=137&width=43&top_left_y=1084&top_left_x=920) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=140&width=99&top_left_y=1081&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=137&width=182&top_left_y=1081&top_left_x=1067) |
| ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=165&width=43&top_left_y=1244&top_left_x=920) |  | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=164&width=182&top_left_y=1241&top_left_x=1067) |
| 交 | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=224&width=99&top_left_y=1418&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=224&width=182&top_left_y=1418&top_left_x=1067) |
|  | 6 | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=206&width=182&top_left_y=1641&top_left_x=1067) |
|  | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=99&width=99&top_left_y=1853&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=99&width=186&top_left_y=1853&top_left_x=1063) |
|  | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=105&width=99&top_left_y=1958&top_left_x=969) | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=105&width=182&top_left_y=1958&top_left_x=1063) |
| 点 | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=112&width=99&top_left_y=2080&top_left_x=969) |  |
|  | ![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-30.jpg?height=126&width=99&top_left_y=2205&top_left_x=969) |  |

![](https://cdn.mathpix.com/cropped/2024_05_09_57b6873fab7db97d7a8dg-31.jpg?height=1913&width=434&top_left_y=426&top_left_x=824)

Table 7: Statistical comparison between proposed and other models over RMSE.

| Method | Avg. Rank | p-value |
| :---: | :---: | :---: |
| DPE $^{\dagger}$ | $\mathbf{2 . 9 4}$ |  |
| PaDPE $^{\dagger}$ | 3.000 | $2 e-1$ |
| COBRA | 8.50 | $1 e-2$ |
| K-NN | 9.94 | $7 e-3$ |
| XGBoost | 6.50 | $1 e-1$ |
| AdaBoost | 7.13 | $5 e-2$ |
| Transformer | 7.31 | $7 e-3$ |
| Highway-LSTM | 8.25 | $3 e-2$ |
| Hybrid-LSTM | 5.56 | $1 e-1$ |
| GRU | 6.63 | $7 e-2$ |
| LSTM | 5.94 | $1 e-1$ |

Table 8: Statistical comparison between proposed and other models over MAPE.

| Method | Avg. Rank | p-value |
| :---: | :---: | :---: |
| DPE $^{\dagger}$ | $\mathbf{2 . 8 8}$ |  |
| PaDPE $^{\dagger}$ | 2.94 | $5 e-1$ |
| COBRA | 7.75 | $1 e-1$ |
| K-NN | 9.25 | $7 e-3$ |
| XGBoost | 5.63 | $4 e-1$ |
| AdaBoost | 7.31 | $3 e-2$ |
| Transformer | 8.38 | $7 e-3$ |
| Highway-LSTM | 8.50 | $7 e-2$ |
| Hybrid-LSTM | 5.38 | $1 e-1$ |
| LSTM | 6.50 | $1 e-1$ |
| GRU | 6.63 | $5 e-1$ |


[^0]:    ${ }^{*}$ Corresponding author at: Department of Mathematics, Indian Institute of Technology, India

    Email addresses: a.bhambu@iitg.ac.in (Aryan Bhambu), arabin@iitg.ac.in (Arabin Kumar Dey)

