# Some Variation Of Cobra In Sequential Learning Setup

Aryan Bhambua, Arabin Kumar Deyb,∗
a*Department of Mathematics, Indian Institute of* Technology, Guwahati, 781039, Assam, India b*Department of Mathematics, Indian Institute of* Technology, Guwahati, 781039, Assam, India

## Abstract

This research paper introduces innovative approaches for multivariate time series forecasting based on different variations of the combined regression strategy. We use specific data preprocessing techniques which makes a radical change in the behaviour of prediction. We compare the performance of the model based on two types of hyper-parameter tuning Bayesian optimisation (BO) and Usual Grid search. Our proposed methodologies outperform all state-of-the-art comparative models. We illustrate the methodologies through eight time series datasets from three categories: cryptocurrency, stock index, and short-term load forecasting. Keywords: Time Series Forecasting, Forecast combination, Machine learning, Deep Neural network, Ensemble Learning, Bayesian Optimisation.

## 1. Introduction

Multivariate time series forecasting is essential as it considers the interdependencies among multiple variables, providing a more accurate understanding of complex systems [5]. This approach proves valuable in the fields such as finance, economics, and environmental monitoring, allowing organisations to make more informed decisions by capturing underlying relationships between variables.

arXiv:2405.04539v1 [stat.ML] 7 Apr 2024 Researchers used not just deep learning techniques to predict future values in both univariate and multivariate time series, but also created elegant framework where they accommodated large number of machine learning models which are specifically meant for independent datasets. Multiple researchers used different regression based models like Multiple Linear regression, Ridge, LASSO, Support Vector Regression (SVR) ([16]), Decision tree based approaches to forecast time-series of various nature.

Deep Neural Networks (DNN), particularly recurrent neural networks like Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and Highway Long Short-Term Memory (Highway-LSTM), gained prominence due to their powerful generalisation and scalability [9, 4, 23]. Literature contains even comparative studies between traditional methods like ARIMA and advanced neural network models such as LSTM and GRU for time series forecasting [19, 8]. These studies demonstrate the superiority of certain deep learning models, such as GRU, in specific forecasting tasks like traffic time series forecasting [8]. Hybrid time series forecasting models integrate diverse techniques, combining statistical methods and machine learning to enhance accuracy and adaptability, capturing both linear and non-linear patterns in the data [7, 10]. Fathi proposed a hybrid model that merges ARIMA and LSTM for sales forecasting [7]. Islam et al. [10] introduced a hybrid LSTM
model composed of GRU and LSTM for time series forecasting, demonstrating its superiority over alternative models. [22] proposed a transformerbased model for long sequence time-series forecasting and fully utilise the self-attention mechanism to deal with super long sequences, outperforming the existing models on four large-scale datasets.

Researchers over the years constantly focused on improving the accuracy by the introducing many ensemble algorithms. K-NN ensemble [13] leverages the collective insights of its nearest neighbours to make predictions, effectively capturing non-linear relationships in time series data. Similarly, AdaBoost [18] sequentially combines weak learners to enhance overall predictive accuracy, while XGBoost [ [16], [6], [17]], a powerful ensemble method, excels in capturing complex temporal dependencies through boosting. However, these ensembles use regression based weak learners. A framework for ensemble learning methods with sequential learning based Deep Neural Networks as weak learners are not available in the literature. Distance-based ensembles are important as they enhance model robustness by leveraging diverse algorithms, reducing overfitting, and improving generalisation across varying data patterns. By considering the dissimilarity between instances, these ensembles excel at capturing complex relationships in data, leading to more reliable and accurate predictions [11, 20, 21]. We propose a non-linear way of combining estimators, adding to a streamline of works pioneered by Mojirsheibani [14]. Our methods Dynamic Proximity Ensemble (DPE) model extends the COBRA (Combined Regression Strategy) algorithm introduced by Biau et al. [3]. There is no work available based on COBRA in sequential learning framework so far.

In the domain of time series forecasting, which involves preprocessing, sequence modelling, independent forecasting, and aggregation, tuning numerous hyper-parameters is essential for accurate predictions. While grid search is commonly employed due to its simplicity, it can be time-consuming and biased without correlation. The motivation behind applying the Bayesian Optimisation Algorithm (BOA) [15] in hyper-parameter tuning lies in controlling time complexity and preserving balance in exploitation and exploration. The effectiveness of BOA in improving hyper-parameter tuning for various prediction models, including attention-based LSTM, PM2.5 prediction, and COVID-19 prediction are available in different research articles
[[2], [1], and [12]]. These works validate the superiority of BOA over baseline models in achieving optimised model performance [2, 1, 12]. The paper explores the implementation of BOA in all proposed variations and highlight the best model in this context.

The organisation of the paper goes as follows. Section 2 demonstrates the all proposed methodologies adapted in this sequential learning setup.

Section 3 describes implementation structure of Bayesian Optimisation for Hyper-parameter Tuning on the proposed setup. Details of the framework for empirical studies on different datasets are available in Section 4. We discuss the empirical results in Section 5. Section 6 describes dynamic prediction in this context. We conclude the paper in Section 7.

## 1.1. Contributions Of Our Proposed Model

The main contribution of the paper are:
1. The paper would be first contribution of COBRA in sequential learning setup in multi-dimensional signal.

2. We explore two different variation of COBRA, Dynamic Proximity Ensemble and Partitioned Dynamic Proximity Ensemble respectively for multivariate time series forecasting.

3. We observe Dynamic Proximity Ensemble outperforms all other variations of COBRA and existing state or the models with respect to the two metrics considered in this paper.

4. We apply the computationally efficient Bayesian optimisation algorithm to automatically search the optimal ensemble configurations.

5. We experiment with the eight different time series datasets having three groups of datasets: Cryptocurrency, Stock Index, and Australian Energy Market Operator. The computational and statistical experiments evidence superiority of our proposed model over others.

## 2. Proposed Methodologies

2.1. Dynamic Proximity based Ensemble (DPE)
Let us assume the dataset Dori = {(Y11, · · · YN1), . . . ,(Y1T , · · · , YNT )} and Dori = (Y 1
, · · · , Y T
) ∈ R
N . The initial objective is to make one step ahead prediction in a time-series data or to find out the expectation of Y T given FT −1 = {Y 1
, Y 2
, · · · , Y T −1}.

The current form of COBRA available in the literature so far is valid for independent datasets which is meant for usual regression purpose or with an extension in functional regression (Goswami et al. ).

We propose the following initial steps to transfer the time series problems into a similar framework/design that can mimic the existing COBRA. We use sliding window to create the frames. It will help to transfer the whole data into series of exchangeable datasets with a specific window length of covariates and a target variable to perform COBRA on these exchangeable sets.

In multidimensional data, we are creating a tensor (D1) where each matrix will consist of exchangeable set of elements. Thus, we can use COBRA in multi-dimensional time series framework.

Let us denote the i-th frame/matrix with l time step of the tensor is F
l i =

Y1,i Y1,i+1 Y1,i+2 *. . . Y*1,i+l Y2,i Y2,i+1 Y2,i+2 *. . . Y*2,i+l
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

YN,i Y2,i+1 Y2,i+2 . . . YN,i+l Thus, D1 = {F
l 1
, · · · , FlT −l+1}.

We further create a new set of exchangeable sets taking both frames of covariates and the target observations. We call the set as Dcob. Therefore, Dcob = {(F
l 1
, Y 1
), · · · ,(F
l T −l+1, Y T −l+1)}.

According to our proposition, we divide Dcob into train, validation and test set. For better understanding of the methodology, let us consider training set Dn = {(F
l 1
, Y 1
), *· · ·* ,(F
l n
, Y n
)} and validation set Dv = {(F
l n+1, Y n+1)· · · ,(F
l n+v
, Y n+v
)}.

In the DPE framework, M competing estimators, referred to as machines, are employed. Each machine m is trained on Dn and denoted as r 1 tr, r2 tr*, . . . , r*M
tr , with r i tr representing a machine trained exclusively on Dn
(train) capable of estimating E(Y t |F
l t−l−1 = x) for any x ∈ R
t−1. The DPE
estimate of E(Y t |F
l t−l−1 = x) is then formulated as :

$$\hat{E}_{D P E}(\underline{{{Y}}}_{t}|F_{t-l-1}^{l}=x)=\sum_{i=1}^{n}W_{n,i}(x)\underline{{{Y}}}_{i}$$

The weight Wn,i(x) for the i-th sample in Dn is defined by:

$$W_{n,i}(x)=\frac{I\left(\bigcap_{m=1}^{M}||r_{t r}^{m}(F_{i}^{l})-r_{t r}^{m}(x)||\leq\epsilon\right)}{\sum_{j=1}^{n}I\left(\bigcap_{m=1}^{M}||r_{t r}^{m}(F_{j}^{l})-r_{t r}^{m}(x)||\leq\epsilon\right)}\eqno(2)$$
$$(1)$$

Here, ϵ is distance threshold, a user-specified parameter. The weight reflects the consensus across machines regarding the proximity of the ith frame to the query frame x. Specifically, if the ith frame is close to x in all machines, the weight is 1; otherwise, if it is distant in any machine, the weight is 0. A new parameter, α, determines the minimum number of concurring machines for the weight to be 1, thus introducing an element of consensus.

The weight can be expressed as:

$$W_{n,i}(x)=\frac{I\left(\sum_{m=1}^{M}|I\left(|r_{t r}^{m}(F_{i}^{l})-r_{t r}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}{\sum_{j=1}^{n}I\left(\sum_{m=1}^{M}I\left(||r_{t r}^{m}(F_{j}^{l})-r_{t r}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}\qquad(3)$$

2.2. Partition-Dynamic Proximity based Ensemble (PaDPE)
PaDPE also initially starts with three division of the data : training, validation and test. However, we divide further the training dataset Dn into two distinct parts in PaDPE : Dn1 = (F
l 1
, Y 1
)*, . . .(F*
l n1
, Y n1
) and Dn2 =
(F
l n1+1, Y n1+1)*, . . . ,*(F
l n
, Y n
), where n2 = n − n1 ≥ 1. We denote validation set as Dv = {(F
l n+1, Y n+1)*· · ·* ,(F
l n+v
, Y n+v
)}.



In the PaDPE framework, M competing estimators, referred to as machines, are employed. Each machine m is trained on Dn1 and denoted as r 1 n1
, r2n1
, . . . , rM
n1
, with r i n1 representing a machine trained exclusively on Dn1 capable of estimating Eˆ*P aDP E*(Y t |F
l t−l−1 = x) for any x ∈ R
l×N . The PaDPE
estimate of Eˆ*P aDP E*(Y t |F
l t−l−1 = x) is then formulated as:

$$\hat{E}_{P a D P E}(\underline{Y}_{t}|F^{l}_{t-l-1}=x)=\sum_{i=1}^{n}W_{n,i}(x)\underline{Y}_{i}\tag{4}$$

The weight Wn,i(x) for the ith sample in Dn is defined by:

$$W_{n,i}(x)=\frac{I\left(\bigcap_{m=1}^{M}||r_{n_{1}}^{m}(F_{i}^{l})-r_{n_{1}}^{m}(x)||\leq\epsilon\right)}{\sum_{j=1}^{n}I\left(\bigcap_{m=1}^{M}||r_{n_{1}}^{m}(F_{j}^{l})-r_{n_{1}}^{m}(x)||\leq\epsilon\right)}\tag{5}$$

Here, ϵ is distance threshold, a user-specified parameter. The weight reflects the consensus across machines regarding the proximity of the ith sample to the query point x. Specifically, if the ith sample is close to x in all machines, the weight is 1; otherwise, if it is distant in any machine, the weight is 0. A new parameter, α, determines the minimum number of concurring machines for the weight to be 1, thus introducing an element of consensus. The weight can be expressed as:

$$W_{n,i}(x)=\frac{I\left(\sum_{m=1}^{M}I\left(||r_{n_{1}}^{m}(F_{i}^{l})-r_{n_{1}}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}{\sum_{j=1}^{n}I\left(\sum_{m=1}^{M}I\left(||r_{n_{1}}^{m}(F_{j}^{l})-r_{n_{1}}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}\tag{6}$$



## 2.3. Training

Moreover, detailed explanations regarding the training methods for the proposed algorithms are available in algorithms 1 and 2. This subsection provides a comprehensive understanding of the steps and processes involved in training the models providing insights into the training procedures for both the DPE and PaDPE algorithms.

To delve into specifics, algorithms 1 and 2 offers a detailed walkthrough of the training process for the DPE and PaDPE algorithm, explaining the steps taken to fine-tune the model parameters and improve its predictive capabilities. This includes initiating the base models, calculating distances between predictions, and determining weights, all contributing to the generation of accurate predictions.

Furthermore, the subsequent section provides a comprehensive overview of Bayesian Optimisation. This serves as a precursor to understanding how both the DPE and PaDPE models undergo optimisation using Bayesian techniques.

## Algorithm 1 Training Algorithm For Dpe Network

Input: Training dataset Dn, distance threshold ϵ, M number of base models, and fraction of base models α. Output: Prediction ˆy for any test observation x.

1: Train M base models using the training dataset Dn.

2: for i ← 1 to n do 3: Obtain predictions r m tr (F
l i
) for each model m.

4: Calculate the distance between r m tr (F
l i
) and r m tr (x).

5: end for 6: Calculate the indicator function and weights for each training sample with respect to the test observation using ϵ, and α from equation 3.

7: After calculation of weights, calculate their product with the training labels Yi, resulting in the prediction ˆy according to Equation 1.

## 2.4. Testing

In this study, we delve into testing procedures for the DPE and PaDPE
methodologies. These approaches aim to estimate the conditional expectations Eˆ*DP E*(Y t |F
l t−l−1 = x) and Eˆ*P aDP E*(Y t |F
l t−l−1 = x) respectively. Note that Y t is a point from test dataset, F
l t−l−1 is the respective query frame. In a different note, our aim is to make one step ahead forecasting of a multidimensional time series given a new frame.

## 2.4.1. Dpe Methodology On Test Dataset

For the DPE method, proximity frames are from the combined dataset comprising of predictions from both Dn (training data) and Dv (validation data). The DPE estimate of Eˆ*DP E*(Y t |F
l t−l−1 = x) is formulated as:

## Algorithm 2 Training Algorithm For Padpe Network

Input: Training dataset Dn, fraction n1 n
, distance threshold ϵ, M number

of base models, and fraction of base models α.

Output: Prediction ˆy for any test observation x.

1: Partition the training dataset Dn into Dn1
, and Dn2 using the fraction n1 n
.

2: Train M base models on the dataset Dn1
.

3: for i ← 1 to n do 4: Obtain predictions r m n1
(F
l i
) for each model m.

5: Calculate the distance between r m n1
(F
l i
) and r m n1
(x).

6: end for 7: Calculate the indicator function and weights for each training sample with respect to the test observation using ϵ, and α from equation 6.

8: After calculation of weights, calculate their product with the training labels Yi, resulting in the prediction ˆy according to Equation 4.

$$\hat{E}_{DPE}(\underline{Y}_{t}|F^{l}_{t-l-1}=x)=\sum_{i=1}^{n}W_{n,i}(x)\underline{Y}_{i}\tag{7}$$

Here, the weights (W*nv,i*(x)) are computed using the following equation:

$$W_{n v,i}(x)=\frac{I\left(\sum_{m=1}^{M}I\left(||r_{t r}^{m}(F_{i}^{l})-r_{t r}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}{\sum_{j=1}^{n+v}I\left(\sum_{m=1}^{M}I\left(||r_{t r}^{m}(F_{j}^{l})-r_{t r}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}\tag{8}$$

In this formulation, r m tr (Fi) represents the m-th machine for the frame F
l i where F
l i is some arbitrary frame from combined set Dn and Dv , and ϵ and α are threshold parameters.

## 2.4.2. Padpe Methodology

In PaDPE Methodology, the testing space is similar to the tuning space.

Proximity set consists of predictions from a smaller training set as well as predictions on new points in both during tuning parameters and prediction on new query points from test dataset.

The PaDPE methodology involves a more extensive proximity point set consists of predictions on a combined space of Dn1 and Dn2 and validation data Dv. The PaDPE estimate of Eˆ*P aDP E*(Y t |F
l t−l−1 = x) follows a similar formulation as the DPE method:

$$\hat{E}_{P a D P E}(\underline{Y}_{t}|F^{l}_{t-l-1}=x)=\sum_{i=1}^{n}W_{n,i}(x)\underline{Y}_{i}\qquad\qquad\qquad(9)$$

where, F
l t−l−1 = x is the query frame from test dataset.

The corresponding weight calculation is given by:

$$W_{nv,i}(x)=\frac{I\left(\sum_{m=1}^{M}I\left(||r_{n_{1}}^{m}(F_{i}^{l})-r_{n_{1}}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}{\sum_{j=1}^{n+v}I\left(\sum_{m=1}^{M}I\left(||r_{n_{1}}^{m}(F_{j}^{l})-r_{n_{1}}^{m}(x)||\leq\epsilon\right)\geq M\alpha\right)}\tag{10}$$

In this context, r m n1
(F
l i
) denotes the m-th machine for the frame F
l i from a combined space of Dn1 and Dn2 and Dv. Note that, ϵ and α remain the threshold parameters.

## 3. Bayesian Optimisation For Hyperparameter Tuning

Multiple hyper parameter together creates large number of possible models. In automated learning one popular technique to select the best model is Bayesian Optimisation which selects the hyper-parameter based on on a surrogate function to model the conditional probability of performance on a validation set. Unlike traditional grid search methods, Bayesian Optimisation Algorithm (BOA) preserves and leverages all prior computations, avoiding redundant evaluations of suboptimal hyper-parameter configurations. The algorithm employs an acquisition function to systematically identify the most promising hyper-parameter configuration for evaluation in subsequent iterations.

The Bayesian Optimisation Algorithm (BOA) comprises five key components: the surrogate function, the hyper-parameter search space, the acquisition function, the objective function, and the historical record of evaluations.

In this context, the objective function is defined as the predictive performance on the validation set. The surrogate function is established using the Tree-based Parzen Window Estimation (TPE) algorithm, and the selected acquisition function is the expected improvement. The formulation of the acquisition function, denoted as Sf
⋆ (v), is expressed as follows:

$$S_{f^{\star}}(v)=\int_{-\infty}^{f^{\star}}(f^{\star}-f)P(f|v)\,df.\tag{11}$$  Here, $f^{\star}$ represents the objective function, and $f$ represents the predefined 
threshold for the objective function concerning the hyper-parameters v. The Tree-based Parzen Estimation (TPE) algorithm encompasses several steps, as elucidated in Algorithm 3.

## Algorithm 3 Tpe For Hyperparameter Tuning

Input: Objective function f, TPE method M, hyper-parameter space Hv, acquisition function validation S, initialised memory D.

Output: Best hyperparameters v
⋆in memory D.

1: for i ← 1 to N do 2: P(f|v) ← Fit memory D using M
3: vi+1 ← Maximize acquisition function S in Equation
(11) to determine the next hyper-parameter choice 4: f(vi+1) ← Evaluate the objective function 5: D ← D ∪ (vi+1*, f(v*i+1))
6: end for This algorithm iteratively refines hyper-parameter choices, leveraging the acquisition function to guide the search toward promising regions within the hyper-parameter space. The historical record D accumulates optimal configurations, ultimately leading to improved model performance.

For our proposed methodology, The objective function aims to minimise the mean squared error. The search space defines hyper-parameter values.

The Tree of Parzen Estimators (TPE) algorithm, used implicitly in hyperopt, guides the exploration-exploitation trade-off through its acquisition function, suggesting where to sample for optimal hyper-parameters.

## 4. Empirical Study

This section presents the empirical study conducted on eight time series datasets, comprising cryptocurrency, stock index, and load forecasting time series datasets. The cryptocurrency and stock index finance datasets have been gathered from Yahoo Finance, while the load time series forecasting datasets have been obtained from the Australian Energy Market Operator (AEMO). Initially, we present a brief introduction to the datasets and



pre-processing steps. We also describe the assessment metrics, benchmark models, and hyper-parameter optimisation in this context.

## 4.1. Data And Its Nature

The first three, covering the period from January 1, 2015, to June 30, 2023, are financial datasets from Yahoo Finance. The Bitcoin dataset represents the cryptocurrency's daily market performance. The DJI dataset tracks the Dow-Jones Industrial Average, reflecting the performance of 30 major U.S.

companies. The S&P500 dataset covers 500 large-cap American companies, providing a comprehensive view of the U.S. stock market. All datasets are publicly accessible on Yahoo Finance's official website.  Summary of the dataset is available in Table-1.

The subsequent five datasets encompass load data collected from the states of South Australia (SA), New South Wales (NSW), Victoria (VIC), and Tasmania (TAS) for the month of December 2022.  The records of data are available for every half an hour, resulting in 48 data points per day.

These datasets are also publicly available and can be accessed on the official website of the Australian Energy Market Operator. Table-2 provides a brief summary of load datasets. We also show the data visualisation for the Bitcoin data: Closing and Volume Price and for NSW data: Total Demand and RRP in the figures: 4 and 5 respectively.

Dataset Name Max Min Median Mean Std Skewness Kurtosis

Bitcoin 67566.82 178.10 8041.77 14024.54 16089.06 1.36 0.88

DJI 36799.64 15660.17 25669.32 25783.14 6059.98 0.06 -1.23

S&P 500 4796.56 1829.07 2842.73 3046.08 830.93 0.42 -1.13

Bitcoin 350.9e+9 e+9 0.07e+9 17.1e+9 19.6e+9 2.73 28.28

DJI 0.9e+9 0.04e+9 0.2e+9 0.2e+9 0.1e+9 0.57 1.34

S&P 500 9.9e+9 1.2e+9 3.8e+9 4e+9 0.9e+9 1.69 4.87

We adapt a set of specific data pre-processing techniques to ensure that machine learning models yield precise outputs. In our methodology, first we employ the max-min normalisation technique to refine the raw data. We assume that the highest and lowest values within the training set represented by xmax and xmin, respectively. The process transforms the data values in
[0,1] using the following equation:

$$x_{\mathrm{normalized}}={\frac{1}{\tau}}$$
$$x_{\operatorname*{max}}-x_{\operatorname*{min}}$$
$$\frac{x-x_{\operatorname*{min}}}{x_{\operatorname*{min}}}$$

| Month   | Max      | Min     | Median   | Mean    | Std    | Skewness   | Kurtosis   |
|---------|----------|---------|----------|---------|--------|------------|------------|
| SA      | 2834.54  | 119.6   | 1240.97  | 1135.00 | 419.97 | -0.16      | 0.47       |
| NSW     | 9575.59  | 4530.54 | 6636.68  | 6721.05 | 902.91 | 0.25       | -0.42      |
| VIC     | 8148.52  | 1976.53 | 4194.06  | 4239.37 | 788.26 | 0.54       | 2.18       |
| TAS     | 1398.93  | 770.52  | 1079.82  | 1082.54 | 92.08  | 0.18       | -0.26      |
| QLD     | 8873.19  | 3859.83 | 5497.31  | 5736.49 | 924.75 | 0.73       | 0.23       |
| SA      | 12523.61 | -1000.0 | 23.08    | 35.43   | 180.14 | 42.41      | 2701.58    |
| NSW     | 15500.0  | -120.0  | 93.35    | 82.64   | 179.12 | 72.52      | 6168.07    |
| VIC     | 316.21   | -937.19 | 19.15    | 31.28   | 71.74  | -0.49      | 7.96       |
| TAS     | 15493.4  | -51.65  | 83.85    | 76.35   | 169.75 | 84.00      | 7617.79    |
| QLD     | 1250.0   | -122.19 | 92.77    | 85.46   | 80.11  | 1.83       | 15.90      |

Here, xnormalized represents the normalised time series, and x denotes the original time series.









To implement cross-validation, we first divide the dataset into three parts:
the training set, validation set, and test set. We choose the validation and test sets each with 10% of the entire dataset. Furthermore, the dataset underwent cumulative sum (cumsum) pre-processing before being subjected to scaling.

$$A S$$

4.2. Assessment Metrics 4.2.1. Root Mean Square Error (RMSE)
RMSE measures the average magnitude of the errors between predicted
(ˆyi) and actual (yi) values. Squaring the differences emphasizes larger errors, and taking the square root provides an interpretable metric in the same unit as the target variable. RMSE is sensitive to outliers due to the squaring effect.

$$(R M S E)$$
$${\mathrm{RMSE}}={\sqrt{\frac{\sum_{i=1}^{n}(y_{i}-{\hat{y}}_{i})^{2}}{n}}}\qquad\qquad\qquad(12)$$

4.2.2. Mean Absolute Percentage Error (MAPE)
MAPE represents the average percentage difference between predicted
(ˆyi) and actual (yi) values. It is particularly useful when dealing with variables of different scales, as it normalizes the error by the magnitude of the actual values. However, MAPE can be problematic when the actual values are close to zero.

$${\mathrm{MAPE}}={\frac{1}{n}}\sum_{i=1}^{n}\left({\frac{|y_{i}-{\hat{y}}_{i}|}{|y_{i}|}}\right)\times100\qquad\qquad(13)$$

## 4.3. Base Models

In our study, we have employed various deep learning models as the foundation or base models, also referred to as learners. These models are selected for their proficiency in capturing intricate patterns and dependencies within data. The following are the base models utilised in our research:

## 1. Long Short-Term Memory (Lstm): Lstm Is A Type Of Recurrent

neural network (RNN) designed to retain long-term dependencies in sequential data, making it effective for tasks involving time-series or sequential information.

2. Gated Recurrent Unit (GRU): Similar to LSTM, GRU is another variant of RNN designed to address the vanishing gradient problem. It simplifies the architecture while maintaining the capability to capture dependencies in sequential data.

3. Hybrid LSTM-GRU Model: This model combines elements of both LSTM and GRU architectures, leveraging their respective strengths to enhance overall performance.

4. Highway LSTM Model: The Highway LSTM model incorporates highway networks with LSTM units, allowing for a more controlled flow of information through the network. This can be beneficial in learning hierarchical representations.

5. Transformer Model: The Transformer model is a non-recurrent architecture that utilises self-attention mechanisms to capture dependencies across different positions in the input sequence simultaneously. It has demonstrated remarkable success in various natural language processing tasks.

## 4.4. Comparison Models

We conduct a comprehensive comparison of our proposed models, DPE
and PaDPE, against several state-of-the-art models, encompassing both classical and contemporary approaches. The aim is to evaluate the effectiveness of our models in capturing complex relationships within the data. The comparison includes the following models:

## 1. Adaptive Boosting

2. Gradient Boosting 3. K-Nearest Neighbours 4. Combined Regression Strategy (COBRA)
This comprehensive selection of base and comparison models provides a thorough foundation for evaluating the proposed models' capabilities and understanding their potential advantages in the context of the specific tasks under consideration.

## 4.5. Hyperparameter Tuning

In the pursuit of a rigorous and equitable comparison among various models, hyper-parameter optimization through cross-validation is employed. The hyper-parameter search space, as delineated in Table 3, serves as a crucial framework for this optimization process. Certain parameters remain constant throughout the optimisation, maintaining uniformity across all pertinent models. These fixed parameters include a batch size set to 32, a learning rate fixed at 0.001, and a fixed number of epochs at 80.

For models DPE and PaDPE, specific hyper-parameters undergo meticulous tuning through this process. Notably, the parameters subject to tuning encompass the distance parameter denoted as ϵ, the number of machines represented by α, and the fraction denoted as ln
. The specific range for these hyper-parameters is elucidated in Table 3, guiding the optimisation process to attain optimal model performance.

## 5. Empirical Results And Discussion

Tables 5 and 6 provide a detailed comparison of different forecasting models applied to distinct time series, using metrics like Root Mean Square Error
(RMSE) and Mean Absolute Percentage Error (MAPE). Bold highlights in the tables indicate instances where a specific model excels for a given time series. Importantly, the DPE model consistently shows exceptional accuracy across most datasets. While the proposed PaDPE model outperforms others in certain datasets, there is noticeable variability in its results. Additionally, XGBoost ensemble models consistently demonstrate outstanding accuracy compared to their counterparts, highlighting their strong predictive capabilities.

5.1. Performance evaluation over multivariate time series forecasting





In this research, we apply the proposed models on a bitcoin finance dataset. A visual representations of the raw price and volume of the dataset are available in Figures 6 and 7 respectively. The figures also present a side-by-side view of DPE predictions on respective test datasets, providing a detailed understanding of the model's predictive strengths. Specifically, the closing and volume prices for the Bitcoin dataset were meticulously studied, shedding light on the model's effectiveness in capturing intricate patterns within financial time series data.

## 5.1.1. Statistical Comparison Using Wilcoxon'S Test

Despite these notable performances, selecting the most suitable forecasting method based only on error metrics is challenging due to the competitive outcomes among models. Further analysis is conducted using statistical tests to probe differences among all models. This indicates substantial differences in forecasting models' performances across the eight datasets. The use of statistical tests adds depth to the analysis beyond error metrics, providing insights into the comparative strengths and weaknesses of the forecasting models under consideration.

Table 7 and 8 showcase the results of statistical comparisons involving the proposed models: DPE, PaDPE, and other models used for comparison.

These tables display the average ranks, with the model achieving the lowest rank considered the most favourable in terms of performance. The proposed models DPE and PaDPE consistently attains a lower average rank across all tables, as illustrated in Tables 7 and 8.

## 5.2. Abliation Study

5.2.1. Comparative analysis of Two Tuning Methods : BOA and Grid based tuning The suggested model comprises two crucial elements: BOA hyper-parameter tuning and the proposed methodologies, DPE and PaDPE. To delve into the significance of each component, we conduct an ablation study. This entails the formulation and assessment of five variants, each representing a distinct combination of the model's components. These variants are systematically evaluated across diverse datasets, enabling us to gauge the necessity and impact of each element. The overall performance is then averaged across all datasets, and errors are normalised to accentuate variations among them.

The five variants under examination are:
- GridCOBRA: The DPE utilises grid search for parameter optimisation.

- BOACOBRA: The combined regression strategy utilises BOA to optimise parameters in original COBRA.

- GridDPE: The DPE utilises grid search for parameter optimisation. - BOADPE: The DPE utilises both the BOA for parameter optimisation.

- BOAPaDPE: The PaDPE utilises both the BOA for parameter optimisation. - GridPaDPE: The PaDPE utilises gridserach for parameter optimisation.

The bar-plots shows the performance of different variations of COBRA in sequential prediction setup with respect to RMSE in Figure-8 and Figure-9 respectively. The above comparison between the proposed BOA methodologies and their grid-based counterparts reveals that BOA based models consistently outperform the Grid-search based models. This underlines the robustness and effectiveness of the BOA methodologies in enhancing the study's overall outcomes. Moreover, BOADPE outperforms all models in both the metrics considered in this paper.



## 5.3. Some Analysis On Rmse And Model Parameters

We adapt a sensitivity analysis for both the proposed methodologies, namely DPE and PaDPE and conduct a simulation study by systematically varying the number of machines represented by the parameter α , while maintaining a constant optimal value for ε . Subsequently, we varied the parameter ε while keeping α fixed.

These approaches allow us to assess the robustness and performance of both DPE and PaDPE under different conditions.  By systematically altering key parameters, namely α and ε , we gained insights into how these variations impact the outcomes of the simulation studies.

## 5.3.1. Varying The Number Of Machines

In Figure-10, we systematically explore the interplay between machine numbers, denoted as alpha, and the Mean Squared Error (MSE). We vary alpha values within the range of 1 to 5 and observe a consistent reduction in the Mean Squared Error providing optimal α at 5 for DJI dataset. The



above study also indicates that more number of models together improve DPE accuracy, ultimately resulting in a noteworthy reduction in errors.

5.3.2.  Varying the distance parameter e We also explore the relation between the distance parameter epsilon and Mean Squared Error (MSE). The study involves a systematic variation of epsilon values, ranging from 0.001 to 0.01. We keep the alpha parameter at a constant value. Figure-11 shows the curve for MSE with respect to ε convex in nature, finally providing the minimum value of ε at 0.004.

Our findings provide valuable information on the sensitivity of the proposed methodologies to changes in the number of machines ( α ) and the threshold parameter, ε . This comprehensive analysis enhances our understanding of the behaviour and effectiveness of DPE and PaDPE, contributing to the refinement of these methodologies in all other datasets.



## 6. Dynamic Prediction

We assess our model's effectiveness through dynamic predictions, wherein the model operates through dynamically changing scalers. The scaler takes step-by-step update and we fed the scaled data to the model.  After obtaining the predictions we inverse-scaled the result and concatenate the same with past data. Time-lagged entries help to preserve temporal context, and we define a new scaler for the next iteration.  This iterative process ensures adaptability to evolving data patterns.

The dynamic predictions depicted in Figure-12 showcase the future predictive capabilities of the proposed models. These plots illustrate the predictions conducted on the dynamic scaler, with subsequent inverse scaling concerning dynamic scaler. The visualisations does not strongly emphasise the models' proficiency in dynamic predictions, since the picture is zoomed



closely in ten successive prediction. However, It captures better signal capture for volume than prices. It depends on the practitioner how much accuracy required for certain purpose. We need more improvement and better design in this respect.

## 7. Conclusion

Dynamic-Based Proximity Ensemble Method and Partitioned Dynamic-
Based Proximity Ensemble Method are two proposed variations which exhibit superior performance over a state-of-the-art comparative models. The efficacy of our proposed methodology is further validated through its ability to capture complex temporal patterns across diverse datasets, including cryptocurrency, stock index, and short-term load forecasting. This research contributes to the advancement of forecasting techniques in an arbitrary mul-



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

[1] Abbasimehr, H., Paki, R., 2021. Prediction of covid-19 confirmed cases combining deep learning methods and bayesian optimization. Chaos, Solitons & Fractals 142, 110511.

[2] Alizadeh, B., Bafti, A.G., Kamangir, H., Zhang, Y., Wright, D.B.,
Franz, K.J., 2021. A novel attention-based lstm cell post-processor coupled with bayesian optimization for streamflow prediction. Journal of Hydrology 601, 126526.

[3] Biau, G., Fischer, A., Guedj, B., Malley, J.D., 2016. Cobra: A combined regression strategy. Journal of Multivariate Analysis 146, 18–28.

[4] Chung, J., Gulcehre, C., Cho, K., Bengio, Y., 2014. Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv:1412.3555 .

[5] De Livera, A.M., Hyndman, R.J., Snyder, R.D., 2011. Forecasting time series with complex seasonal patterns using exponential smoothing.

Journal of the American statistical association 106, 1513–1527.

[6] Fan, J., Wang, X., Wu, L., Zhou, H., Zhang, F., Yu, X., Lu, X., Xiang, Y., 2018. Comparison of support vector machine and extreme gradient boosting for predicting daily global solar radiation using temperature and precipitation in humid subtropical climates: A case study in china. Energy conversion and management 164, 102–111.

[7] Fathi, O., 2019. Time series forecasting using a hybrid arima and lstm model. Velvet Consulting , 1–7.

[8] Fu, R., Zhang, Z., Li, L., 2016. Using lstm and gru neural network methods for traffic flow prediction, in: 2016 31st Youth academic annual conference of Chinese association of automation (YAC), IEEE. pp. 324– 328.

[9] Hochreiter, S., Schmidhuber, J., 1997. Long short-term memory. Neural computation 9, 1735–1780.

[10] Islam, M.S., Hossain, E., 2021. Foreign exchange currency rate prediction using a gru-lstm hybrid network. Soft Computing Letters 3, 100009.

[11] Juditsky, A., Nemirovski, A., 2000. Functional aggregation for nonparametric regression. The Annals of Statistics 28, 681–712.

[12] Ma, J., Ding, Y., Cheng, J.C., Jiang, F., Gan, V.J., Xu, Z., 2020. A lagflstm deep learning network based on bayesian optimization for multisequential-variant pm2. 5 prediction. Sustainable Cities and Society 60, 102237.

[13] Mart´ınez, F., Fr´ıas, M.P., P´erez, M.D., Rivera, A.J., 2019. A methodology for applying k-nearest neighbor to time series forecasting. Artificial Intelligence Review 52, 2019–2037.

[14] Mojirsheibani, M., 1999. Combining classifiers via discretization. Journal of the American Statistical Association , 600–609.

[15] Snoek, J., Larochelle, H., Adams, R.P., 2012. Practical bayesian optimization of machine learning algorithms. Advances in neural information processing systems 25.

[16] Tay, F.E., Cao, L., 2001. Application of support vector machines in financial time series forecasting. omega 29, 309–317.

[17] Vuong, P.H., Dat, T.T., Mai, T.K., Uyen, P.H., et al., 2022. Stock-price forecasting based on xgboost and lstm. Computer Systems Science &
Engineering 40.

[18] Wang, J., Chen, Y., 2021. Adaboost-based integration framework coupled two-stage feature extraction with deep learning for multivariate exchange rate prediction. Neural Processing Letters 53, 4613–4637.

[19] Yamak, P.T., Yujian, L., Gadosey, P.K., 2019. A comparison between arima, lstm, and gru for time series forecasting, in: Proceedings of the 2019 2nd international conference on algorithms, computing and artificial intelligence, pp. 49–55.

[20] Yang, Y., 2000. Combining different procedures for adaptive regression.

Journal of multivariate analysis 74, 135–161.

[21] Yang, Y., 2004. Aggregating regression procedures to improve performance. Bernoulli 10, 25–47.

[22] Zhou, H., Zhang, S., Peng, J., Zhang, S., Li, J., Xiong, H., Zhang, W.,
2021. Informer: Beyond efficient transformer for long sequence timeseries forecasting, in: Proceedings of the AAAI conference on artificial intelligence, pp. 11106–11115.

[23] Zilly, J.G., Srivastava, R.K., Koutnık, J., Schmidhuber, J., 2017. Recurrent highway networks, in: International conference on machine learning, PMLR. pp. 4189–4198.

| Model                 | Parameter                      | Values                         |    |    |      |
|-----------------------|--------------------------------|--------------------------------|----|----|------|
| LSTM                  | nodes                          | [16, 32, 50, 64, 96, 100, 128] |    |    |      |
| Layers                | [0, 1, 2, 3]                   |                                |    |    |      |
| Optimizer             | Adam                           |                                |    |    |      |
| Activation            | [ReLU, tanh]                   |                                |    |    |      |
| Dropout Rate          | (0, 0.5)                       |                                |    |    |      |
| GRU                   | nodes                          | [16, 32, 50, 64, 96, 100, 128] |    |    |      |
| Layers                | [0, 1, 2, 3]                   |                                |    |    |      |
| Optimizer             | Adam                           |                                |    |    |      |
| Activation            | [ReLU, tanh]                   |                                |    |    |      |
| Dropout Rate          | (0, 0.5)                       |                                |    |    |      |
| Hybrid LSTM           | LSTM nodes                     | [16, 32, 50, 64, 96, 100, 128] |    |    |      |
| GRU nodes             | [16, 32, 50, 64, 96, 100, 128] |                                |    |    |      |
| LSTM Layers           | [0, 1, 2, 3]                   |                                |    |    |      |
| Optimizer             | Adam                           |                                |    |    |      |
| Activation            | [ReLU, tanh, sigmoid]          |                                |    |    |      |
| Dropout Rate          | (0, 0.5)                       |                                |    |    |      |
| Highway LSTM          | LSTM nodes                     | [16, 32, 50, 64, 96, 100, 128] |    |    |      |
| Layers                | [1, 2, 3, 4, 5]                |                                |    |    |      |
| t bias                | (−5, 5)                        |                                |    |    |      |
| Optimizer             | Adam                           |                                |    |    |      |
| acti h                | ReLU                           |                                |    |    |      |
| acti t                | sigmoid                        |                                |    |    |      |
| learning rate         | (1e − 6, 1e − 2)               |                                |    |    |      |
| Transformer           | nodes                          | (32, 200, 2)                   |    |    |      |
| Layers                | [1, 2, 3, 4, 5]                |                                |    |    |      |
| Optimizer             | Adam                           |                                |    |    |      |
| Activation            | [ReLU, tanh, sigmoid]          |                                |    |    |      |
| d k / d v             | [32, 64, 96]                   |                                |    |    |      |
| learning rate         | (1e − 5, 1e − 2)               |                                |    |    |      |
| Dropout Rate          | (0, 0.5)                       |                                |    |    |      |
| feedforward dimension | (32, 200, 2)                   |                                |    |    |      |
| Number of heads       | [1, 2, 4, 8, 12]               |                                |    |    |      |
| DPE-based models      | ϵ                              | (0, 1) 1 2 3                   | 4  |    |      |
| α                     | [                              | ,                              | ,  | ,  | , 1] |
| 5                     | 5                              | 5                              | 5  |    |      |
| n1 n                  | (0, 1)                         |                                |    |    |      |

| AdaBoost      | estimators                   | [10, 50, 100, 200, 300, 400, 500]   |
|---------------|------------------------------|-------------------------------------|
| learning Rate | [10−3 , 10−2 , 10−1 ]        |                                     |
| XGBoost       | estimators                   | [10, 50, 100, 200, 300, 400, 500]   |
| depth         | [1, 2, 3, 4, 5]              |                                     |
| subsample     | [0.5, 0.6, 0.7, 0.8, 0.9]    |                                     |
| child weight  | [2, 4, 6, 8, 10]             |                                     |
| K-NN          | neighbours                   | [1, 2, 3, 4, 5]                     |
| weights       | [uniform, distance]          |                                     |
| P             | [1, 2, 3, 4, 5]              |                                     |
| α             | [ 1 , 2 , 3 , 4 , 1] 5 5 5 5 |                                     |
| n             | (0, 1)                       |                                     |
| l             |                              |                                     |

 



| Method       | Avg. Rank   | p-value   |
|--------------|-------------|-----------|
| DPE†         | 2.94        |           |
| PaDPE†       | 3.000       | 2e − 1    |
| COBRA        | 8.50        | 1e − 2    |
| K-NN         | 9.94        | 7e − 3    |
| XGBoost      | 6.50        | 1e − 1    |
| AdaBoost     | 7.13        | 5e − 2    |
| Transformer  | 7.31        | 7e − 3    |
| Highway-LSTM | 8.25        | 3e − 2    |
| Hybrid-LSTM  | 5.56        | 1e − 1    |
| GRU          | 6.63        | 7e − 2    |
| LSTM         | 5.94        | 1e − 1    |

| Method       | Avg. Rank   | p-value   |
|--------------|-------------|-----------|
| DPE†         | 2.88        |           |
| PaDPE†       | 2.94        | 5e − 1    |
| COBRA        | 7.75        | 1e − 1    |
| K-NN         | 9.25        | 7e − 3    |
| XGBoost      | 5.63        | 4e − 1    |
| AdaBoost     | 7.31        | 3e − 2    |
| Transformer  | 8.38        | 7e − 3    |
| Highway-LSTM | 8.50        | 7e − 2    |
| Hybrid-LSTM  | 5.38        | 1e − 1    |
| LSTM         | 6.50        | 1e − 1    |
| GRU          | 6.63        | 5e − 1    |
