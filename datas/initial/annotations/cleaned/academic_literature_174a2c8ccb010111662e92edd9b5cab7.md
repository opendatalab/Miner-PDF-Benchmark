# Data-driven Semi-supervised Machine Learning with Surrogate Safety Measures for Abnormal Driving Behavior Detection 

## Lanxin Zhang\#

Faculty of Civil Engineering and Geosciences

Delft University of Technology, Delft, The Netherlands, 2628 CN

Email: zhanglx2018@hotmail.com

## Yongqi Dong ${ }^{\#, *}$

Faculty of Civil Engineering and Geosciences

Delft University of Technology, Delft, The Netherlands, 2628 CN

Email: y.dong-4@tudelft.nl

## Haneen Farah

Faculty of Civil Engineering and Geosciences

Delft University of Technology, Delft, The Netherlands, 2628 CN

Email: h.farah@tudelft.nl

Arkady Zgonnikov

Faculty of Mechanical, Maritime and Materials Engineering

Delft University of Technology, Delft, The Netherlands, 2628 CN

Email: a.zgonnikov@tudelft.nl

## Bart van Arem

Faculty of Civil Engineering and Geosciences

Delft University of Technology, Delft, The Netherlands, 2628 CN

Email: b.vanArem@tudelft.nl

\# These authors contributed equally to this work and should be considered as co-first authors.

* Corresponding author.

Submitted [30 November 2023]


#### Abstract

Detecting abnormal driving behavior is critical for road traffic safety and the evaluation of drivers' behavior. With the advancement of machine learning (ML) algorithms and the accumulation of naturalistic driving data, many ML models have been adopted for abnormal driving behavior detection. Most existing MLbased detectors rely on (fully) supervised ML methods, which require substantial labeled data. However, ground truth labels are not always available in the real world, and labeling large amounts of data is tedious. Thus, there is a need to explore unsupervised or semi-supervised methods to make the anomaly detection process more feasible and efficient. To fill this research gap, this study analyzes large-scale real-world data revealing several abnormal driving behaviors (e.g., sudden acceleration, rapid lane-changing) and develops a Hierarchical Extreme Learning Machines (HELM) based semi-supervised ML method using partly labeled data to accurately detect the identified abnormal driving behaviors. Moreover, previous ML-based approaches predominantly utilize basic vehicle motion features (such as velocity and acceleration) to label and detect abnormal driving behaviors, while this study seeks to introduce Surrogate Safety Measures (SSMs) as the input features for ML models to improve the detection performance. Results from extensive experiments demonstrate the effectiveness of the proposed semi-supervised ML model with the introduced SSMs serving as important features. The proposed semi-supervised ML method outperforms other baseline semi-supervised or unsupervised methods regarding various metrics, e.g., delivering the best accuracy at $99.58 \%$ and the best F-1 measure at 0.9913 . The ablation study further highlights the significance of SSMs for advancing detection performance.


Keywords: Abnormal driving behavior, Semi-supervised machine learning, Hierarchical extreme learning machines, Self-supervised training, Surrogate safety measure

## INTRODUCTION

Road traffic safety has become a growing concern worldwide. The World Health Organization (1) reported that approximately 1.35 million people died in car crashes in 2018, with over 30 million suffering non-fatal injuries. These accidents not only resulted in disabilities but also caused significant economic loss, reaching as high as $3 \%$ of the gross domestic product in some countries. It is alarming that in $92.9 \%$ of accidents, human factors were identified as contributing factors (2). This highlights the urgent need to identify abnormal driving behaviors and find ways to prevent or mitigate accidents caused by such abnormal human driving behaviors.

Driving behavior encompasses various variables and factors, including driving performance, environmental awareness, risk-taking propensity, and reasoning abilities (3). Abnormal driving behavior refers to actions that deviate from safe and normal driving, posing risks to oneself, passengers, and other road users. Examples of such behavior include excessive speeding, tailgating, and erratic lane changes (4). These abnormal driving behaviors frequently engender severe traffic altercations, including collisions, crashes, and other minor incidents, thereby underscoring the necessity of addressing and precluding these actions. Precise and efficacious monitoring of aberrant driving behaviors is integral to augmenting driving safety, enhancing driver cognition of driving patterns, and attenuating prospective road accidents.

Machine learning (ML)-based approaches have shown great promise in detecting abnormal driving behaviors. They can learn complex patterns, adapt to changing scenarios, handle large and diverse datasets, and detect unusual behaviors with optimized processes (5). However, most of the available studies adopted fully-supervised ML models to do the detection, and few of them explored un-supervised or semisupervised ML methods. While in the real world, ground truth labels are sometimes missing or inaccurate, plus labeling large amounts of data is tedious and even dangerous under certain critical situations. Therefore, examining and developing unsupervised or semi-supervised methods is imperative to engender more feasible and efficient abnormal driving behavior detection.

On the other hand, Surrogate Safety Measures (SSMs) show promise as robust indicators and proxy measurements of sustainable road safety that can supplement or replace traditional historical crash analyses. Since SSMs do not rely directly on crash data, employing them allows proactive road safety assessment without the need to collect crash data (6). This obviates crash data collection and enables investigating areas before any crashes occur. As Tarko (7) notes, SSMs facilitate detecting excessive crash risk, better understanding crash-precipitating conditions, and estimating countermeasure efficacy. To effectively assess and predict road safety, SSMs have gained popularity as indirect safety indicators using proxy variables correlated with safety outcomes. By providing insights into potential safety issues, SSMs help prioritize improvement efforts. Wang et al. (8) categorize SSMs into two classes: time-based, deceleration-based, and energy-based SSMs, e.g., time-to-collision (TTC), post-encroachment time (PET), time-to-crash/accident (TC/TA), deceleration rate to avoid a crash (DRAC), that apply thresholds to identify traffic conflicts, extensively utilized in road safety research $(6,9,10)$. There is no doubt SSMs can serve as important features in various tasks. However, for abnormal driving behavior detection, previous studies predominantly employed basic vehicle motion as features to label and detect behaviors, and seldom explored the benefits of SSMs.

To fill the aforementioned research gaps, this study aims to develop a novel data-driven approach for abnormal driving behavior detection using real-world naturalistic driving data and leveraging semisupervised ML with self-supervised training to enhance the performance and effectiveness of the detection system. Specifically, this study first analyzes a large-scale dataset, i.e., the CitySim dataset (11), with vivid visualizations and extracts various abnormal driving behaviors. Then, the study develops a Hierarchical Extreme Learning Machines (HELM) based semi-supervised ML model using unlabeled data to carry out self-supervised pre-training and leveraging only partly labeled data to fine-tune the model for accurately detecting the identified abnormal driving behaviors. Furthermore, this study conducts a significative ablation study introducing Surrogate Safety Measures (SSMs) as the input features for the developed semisupervised ML model to further advance the detection performance. Extensive experiments verified the proposed method, especially with the proposed semi-supervised HELM model using SSMs in its input
features outperforms other baseline models, delivering the best accuracy at $99.58 \%$ and the best F1-measure at 0.9913 .

In short, by bridging the gap and addressing the limitations of existing methods, this research endeavors to improve road safety and reduce accidents caused by abnormal driving behaviors. It addresses the limitations of traditional supervised approaches and overcomes the scarcity of labeled abnormal driving data. The study analyzes open-sourced datasets and provides meaningful insights into understanding and categorizing human driving behavior. The conclusions elucidated in this manuscript constitute the bedrock for constructing more precise and resilient models for detecting aberrant driving behavior.

## RELATED WORK

A number of studies have investigated abnormal driving behaviors, with Chen et al. (12) and Kim et al. (13) putting forth definitions that reflect divergent conceptualizations of driving conduct between Eastern and Western cultures as shown in Table 1. The Western driving culture emphasises whether the vehicle's location complies with regulations, whereas the Eastern prioritizes speed modulation, potentially shaped by population density and vehicle volume. Through a comprehensive literature review, the current study delineates abnormal driving as a function of position and velocity, concentrating on abrupt starts, emergency braking, as well as rapid and close lane changes.

## TABLE 1 Different classification of Abnormal Driving Behavior

| U.S. National Highway Traffic Safety Administration <br> (NHTSA) | Korea Ministry of Land, Infrastructure and Transport |
| :--- | :--- |
| (MOLIT) |  |

Machine learning (ML)-based approaches for detecting abnormal driving behaviors have garnered substantial research attention and exhibited robust performance. Both supervised and unsupervised methodologies have been commonly utilized in prior investigations of abnormal driving studies. Supervised techniques necessitate labeled data during model training, whereby the system ascertains the mapping between inputs and outputs to categorize and predict new data points. For example, Jia et al. (14) devised a model integrating long short-term memory (LSTM) neural network and convolutional neural network (CNN) architectures to pinpoint instances of extreme acceleration and deceleration. Shahverdy et al. (15) proposed a lightweight 1-dimensional CNN (1D-CNN) exhibiting high efficiency and low computational overhead for classifying driver actions. Ryan et al. (16) simulated an end-to-end model leveraging CNN to contrast human and autonomous vehicle driving patterns.

Conversely, unsupervised machine learning techniques entail training models using raw, unlabeled data. This approach is frequently utilized during exploratory phases to derive insights from the dataset. As an illustration, Mohammadnazar et al. (3) developed an architecture leveraging unsupervised machine learning to quantify driving performance and categorize driving styles across diverse spatial contexts. Feng et al. (17) proposed a Support Vector Clustering methodology to classify driving manners robustly. Extant literature denotes substantial challenges in accurately identifying anomalies through solely unsupervised machine learning. As Chandola et al. (18) concluded from their review, unsupervised anomaly detection approaches often demonstrate inferior detection rates and heightened false positive rates on real-world problems. Correspondingly, Pimentel et al. (19) discovered via benchmark assessments that complete dependency on unsupervised outlier detection is imprudent, as these techniques fail to detect all anomalies. Erfani et al. (20) further contended that purely unsupervised methodologies lack the learning guidance to
precisely differentiate normal from aberrant patterns. Synthesizing these conclusions, utilizing only unsupervised ML without any labeled data to achieve accurate anomaly detection is hardly possible. Even if viable, the detection performance based on pure unsupervised ML is highly possible to be further enhanced by labeled data. Therefore, the research consensus firmly denotes the necessity for making use of at least partially labeled data to supervise and augment anomaly detection capabilities with semi-supervised ML approaches.

Regarding the features utilized as inputs for ML models, traditional indicators such as velocity, acceleration, and steering angle have been extensively employed (14, 16, 21-23). For example, Lim \& Yang (16) considered vehicular data comprising velocity, acceleration, steering angle, and gas pedal position and leveraged a CNN model to estimate driver drowsiness, workload, and distraction levels. Planek et al. (23) collected lateral vehicle position, steering angle, and speed-related information and implemented a Support Vector Machine (SVM) model to differentiate between normal and intoxicated driving states. Incorporating Surrogate Safety Measures into ML-based methods is supposed to be promising for various tasks but has seldom been investigated yet. To the best knowledge of the authors and after extensive review, only one study was found to be relevant, i.e., Lu et al. (24) integrated the representation of TTC together with the driver maneuver profiles into a deep unsupervised learning and clustering method with their proposed Transformer encoder based model to identify traffic conflicts and non-conflicts. However, they only investigated situations of one intersection and one roundabout in the USA, neglecting other various types of driving anomalies, especially those related to highway driving.

Investigating the potential of semi-supervised approaches, which utilize both labeled and unlabeled examples, is imperative to enhance abnormal driving behavior detection, yet scarce existing research has explored this direction. By harnessing the additional information from unlabeled data, semi-supervised learning can uncover subtle patterns and behaviors that conventional supervised or unsupervised techniques may overlook. This study endeavors to address this research lacuna. Moreover, input features are fundamental for ML-based approaches; to augment detection performance, examining more efficacious features is prudent. In this vein, this study seeks to ascertain the benefits of SSMs, specifically the customized two-dimensional Time to Collision (2D-TTC), as input variables and conducts ablation analyses to verify its efficacy in upgrading abnormal driving behavior identification.

## DATASET AND DATA ANALYSIS

## A. Description of the data

To conduct data-driven research, a high-quality dataset is imperative. After extensive exploration, the current study utilizes the CitySim dataset (11), comprising video-based trajectory data concentrating on traffic safety in the United States. The CitySim dataset encompasses vehicle trajectory information extracted from videos captured by 12 drones, spanning six road geometry typologies, including freeway segments, signalized intersections, and stop-controlled junctions. The dataset furnishes precise positional details in various formats, including pixels, feet, and GPS coordinates, alongside data on velocity, heading angle, and vehicle lane numbers. Table 2 provides the fields of the raw data record and provides one example accessible within the dataset.

To bolster the research objectives, supplementary features are derived from the CitySim dataset, encompassing longitudinal acceleration, lateral acceleration, inter-vehicle distance, and two-dimensional time-to-collision (2D-TTC). Through assimilating these computed variables with the native dataset, the current study endeavors to augment the data foundations requisite for the model. Notably, the dataset's high precision, with measurements accurate to approximately 10 centimeters, furnishes further reliability and suitability for this research. Before presenting the methodological details, Table 3 exhibits examples of the data used after the processing. The upcoming methodology section will delineate the precise calculations to derive the additional features from the raw CitySim dataset.

TABLE 2 Data sample of the CitySim dataset

| Feautres | Value |
| :--- | ---: |
| frameNum | 0 |
| carId | 582 |
| carCenterX (ft) | 462.4 |
| carCenterY (ft) | 184.8 |
| headX (ft) | 469.6 |
| headY (ft) | 184.8 |
| tailX (ft) | 455.3 |
| tailY (ft) | 184.8 |
| Speed (mph) | 39.5 |
| Heading $\left(^{\circ}\right)$ | 180.7 |
| laneId | 10 |

Table notation: ft---feet; mph---miles per hour; ${ }^{\circ}$--- degree

TABLE 3 Data examples after data processing

| frameNum | carCenterX <br> $(\mathbf{m})$ | carCenterY <br> $(\mathbf{m})$ | Speed $(\mathbf{m} / \mathbf{s})$ | Heading <br> $(\mathbf{})$ | 2D-TTC <br> $(\mathbf{s})$ | Distance <br> $(\mathbf{m})$ | Abnormal=1/ <br> Normal=0 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 53.258 | 32.155 | 14.985 | 359.632 | 1.110 | 0.482 |  |
| 1737 | 251.998 | 27.466 | 11.095 | 359.742 | 104.794 | 131.453 | 0 |
| 1739 | 248.537 | 31.095 | 12.300 | 359.707 | 6001.553 | 128.168 | 0 |
| 1760 | 251.607 | 27.355 | 11.064 | 359.656 | 110.943 | 131.392 | 0 |
| 11940 | 128.567 | 31.653 | 16.368 | 359.220 | 0.415 | 0.593 | 1 |
| 11966 | 127.897 | 31.653 | 16.217 | 359.082 | 0.376 | 0.482 | 1 |
| 11981 | 127.115 | 31.653 | 16.218 | 358.865 | 0.295 | 0.457 | 1 |
| 12000 | 126.836 | 31.542 | 16.277 | 358.864 | 0.311 | 0.387 | 1 |

Table notation: the original distance measure "feet" is converted to "meter".

## B. Abnormal driving behaviors identified in the dataset

Based on the reviewed literature's classification and definition of abnormal driving behavior (check section RELATED WORK), this section illustrates the specific abnormal driving behaviors observed in the examined CitySim dataset. Each abnormal behavior is associated with one or two indicators, measured or calculated at various locations.

## Rapid acceleration and emergency brake behavior

The acceleration data corresponding to each velocity datum in the vehicle trajectory dataset, as exhibited in Figure 1, facilitates statistical analysis. Extreme acceleration and deceleration coordinates can be derived, denoting abrupt variations when operators enact aberrant maneuvers such as sudden braking or accelerating. Identifying these extreme points enables the segmentation of abnormal driving conduct. A specific proportion of extreme acceleration can be pinpointed by statistically scrutinizing all acceleration coordinates at identical speeds across all journeys. Determining an appropriate ratio to differentiate extreme points from normal ones is imperative. A 15\% threshold appears judicious based on reiterative experimentation and associated existing research $(14,25)$.

## Rapid lane-changing behavior

Rapid lane-changing behavior is characterized by sudden and instantaneous abnormal actions that occur for a short duration. In normal driving patterns, vehicles exhibit relatively stable lateral acceleration around zero (as shown in Figure 2). However, for abnormal behavior, there manifests an abrupt variation in the vehicle's lateral acceleration. The majority of vehicles exhibiting lane divergence comportment demonstrate a lateral acceleration bounded by $\pm 1 \mathrm{~m} / \mathrm{s}^{2}$, whereby they execute lane diversions seamlessly at
a fixed velocity. However, the acceleration of some vehicles presents as outliers seen in Figure 3. A normal distribution with a mean of 0 and a standard deviation of 1.3 was examined. According to the characteristics of a normal distribution, approximately $68 \%$ of data falls within $\pm 1$ standard deviation from the mean. These outliers beyond $\pm 1$ standard deviation from the mean accounted for approximately $32 \%$ of the total data points. A ratio of $16 \%$ is considered reasonable based on repeated experiments and related research (26). This satisfies the heuristic definition of outliers as observations differ significantly from most data. Examining outliers based on standard deviation thresholds aligns with statistically grounded techniques for anomaly detection using the sigma principle for normal distributions. According to the normal distribution, a value greater than $1.3 \mathrm{~m} / \mathrm{s}^{2}$ and less than $-1.3 \mathrm{~m} / \mathrm{s}^{2}$ will be the filter condition for outliers.



Figure 1 Extreme longitudinal acceleration and deceleration points distribution at different speeds.



Figure 2 Illustration of the distribution of lateral acceleration.



Figure 3 Extreme lateral acceleration and deceleration points distribution at different speeds.

## Close lane-changing behavior

Close lane-changing behavior is characterized by sudden and instantaneous abnormal actions that occur for a short duration. Vehicles in normal driving patterns maintain a certain distance between themselves and adjacent lanes. However, during abnormal behavior, there is a significant decrease in the distance between the vehicle and adjacent lanes, indicating a close lane change. In this thesis, when the distance between two cars during lane-changing is less than 0.5 meters, it is considered severe abnormal driving behavior. In contrast, when the distance is less than 1.0 meters but greater than 0.5 meters, it is considered weak abnormal driving behavior, as seen in Figure 4.



Figure 4 Extreme distance points distribution at different CarID.

Based on the aforementioned criteria, the labels of the driving data samples are further examined by human experts to remove inaccurate labeling ensuring the quality of the finalized labels.

## METHODOLOGY

This section first introduces Surrogate Safety Measures (SSMs), focusing on Two Dimensional Time-To-Collision (2D-TTC). Two ML models, i.e., Isolation Forest, and Robust Covariance, are then presented as baseline methods for comparison. Finally, a customized semi-supervised model named Hierarchical Extreme Learning Machines (HELM) is proposed and explained in detail.

## A. Surrogate safety measures

In the literature review, some studies have studied and employed simple surrogate safety measures (SSMs), such as time-to-collision (TTC). The TTC value is calculated as:

TTC $=\frac{D}{v_{1}-v_{2}}$

However, two salient limitations exist with the conventional TTC calculation: (1) scenarios are deemed safe when the velocity of the following vehicle is less than or equal to the lead vehicle, despite the potential for minimal relative distance between them (26); and (2) the vehicle pair is presumed to occupy the same lane, with merely lateral movements incorporated (27). To surmount these constraints of the standard TTC, the current study implements a novel TTC metric, entitled the two-dimensional TTC (2DTTC) (28):

$2 D T T C=\left\{\begin{array}{l}\frac{D T C}{\left|v_{i}-v_{j}\right|}, \text { if the direction of DTC is the same with }\left(v_{i}-v_{j}\right) \\ \text { inf, if the direction of DTC is opposite with }\left(v_{i}-v_{j}\right)\end{array}\right.$

Figure 5 Illustration of 2D-TTC.

In general, according to literature only encounters with a minimum TTC below 1.5 second are deemed critical, with trained observers consistently applying this threshold in practice (29). This study explores the novel input feature 2D-TTC which is specially introduced and derived directly from the dataset parameters. Specifically, the vehicle angle in the dataset decomposes each vehicle's velocity into $x-y$ coordinate components, yielding velocity vectors based on the dataset parameters. 2D-TTC is then calculated per these velocity vectors and the corresponding distance along the same direction. This approach highlights how 2D-TTC can be computed from the raw dataset by leveraging the vehicle angle data to obtain velocity vectors in coordinate space. The derived 2D-TTC is analyzed with input features like position, speed, and acceleration to evaluate anomaly detection performance using the given dataset.

## B. Baseline models

Isolation Forest and Robust Covariance are selected as two baseline methods considering their interpretability, effectiveness, and broad utilization in various domains.

The Isolation Forest, initially developed by Liu et al. (30), constitutes an effective algorithm typically utilized for data anomaly detection. It is predicated on the notion that anomalous data points are more readily separable from the remainder of normal samples. To isolate an abnormal data point, the algorithm iteratively generates partitions of the sample by randomly selecting a feature attribute and subsequently randomly choosing a split value within the permissible minimum and maximum values for the selected feature attribute. Through recursive binary partitioning, data points that require fewer splits to become isolated are deemed more anomalous.

The Isolation Forest algorithm capitalizes on the premise that anomalies are few and different, and thereby manifest topological shorter path lengths (which is elucidated by averaging this value across the trees) when random partitioning is employed. Therefore, it leverages an ensemble of isolation trees generated through such recursive random partitioning to identify anomalies, with shorter average path lengths corresponding to greater anomaly scores.

In practice, the Isolation Forest anomaly detection algorithm involves two primary phases. Firstly, a collection of isolation trees (iTrees) are constructed utilizing recursive partitioning on a training dataset. During recursive partitioning, splits are performed by randomly selecting an attribute and random split value to isolate a data point. Secondly, each instance in the test set is propagated through the ensemble of iTrees and assigned an anomaly score based on the average path length for that instance across the iTrees. Shorter average path lengths correspond to fewer partitions required to isolate the instance, indicating more anomalous behavior and higher anomaly score. After computing anomaly scores for all test instances, those data points with a score exceeding a predefined threshold specific to the domain can be classified as anomalies.

The Robust Covariance estimation algorithm presupposes that normal data points exhibit a Gaussian distribution, and accordingly approximates the morphology of the joint distribution (namely, estimates the mean and covariance of the multivariate Gaussian distribution) (31).

In statistical analysis, the deviation can be gauged by the Z-score. The generalization of the Z-score for a point $x_{i}$ in the case of a p-dimensional multi-variate probability distribution with some mean $\mu$ and covariance matrix $\Sigma$ is known as Mahalanobis distance $d_{i}$, which is given by:

$d_{i}=\sqrt{\left(x_{i}-\mu\right)^{T} \Sigma^{-1}\left(x_{i}-\mu\right)}$

It is premised on the fact that outliers engender an augmentation of the values (entries) in $\Sigma$, thereby rendering the diffusion of the data ostensibly more extensive. Consequently, $|\Sigma|$ (the determinant) will likewise be superior, which would theoretically diminish by excising extreme events. Rousseeuw and Van Driessen (32) devised a computationally effectual algorithm capable of furnishing robust covariance approximations. The approach is predicated on the postulation that at minimum $h$ of the $n$ exemplars are "normal" ( $h$ denoting a hyperparameter). The algorithm inaugurates with $k$ arbitrary samples containing $(p+1)$ points. For each $k$ sample, $\mu, \Sigma$, and $|\Sigma|$ are estimated, the distances are computed and sorted in ascending order, and the $h$ smallest distances are employed to update the estimates. In their primordial publication, the subroutine of computing distances and revising the estimations of $\mu, \Sigma$, and $|\Sigma|$ is entitled a "C-step" whereby two such increments suffice to ascertain efficacious candidates (for $\mu$ and $\Sigma$ ) among the $k$ arbitrary samples. In the succeeding step, a subset of magnitude $\mathrm{m}$ with the lowest $|\Sigma|$ (the optimal candidates) is contemplated for computation until convergence, and the sole estimate whose $|\Sigma|$ is minimal is furnished as output.

Please note, although Isolation Forest and Robust Covariance are usually considered unsupervised ML approaches, in this study only normal data samples are input to train them, thus, in this study, they can be regarded as semi-supervised approaches and are comparable to the proposed semi-supervised machine learning method.

## C. Hierarchical Extreme Learning Machines based Semi-supervised Machine Learning

The Hierarchical Extreme Learning Machines algorithm, originally propounded by Tang (33), constitutes an extension of the ELM algorithm that can be executed with swift training, admirable generalization, and universal approximation/classification capability. It delineates a feed-forward neural network encompassing multiple latent layers, which consists of two cardinal steps: unsupervised feature representation and supervised feature classification (34). In the primordial step, the HELM is intended to ascertain a sparse encoder in an unsupervised manner, which transduces the raw input into superior-level representation. The encoder possesses multiple latent layers and is conditioned layer by layer.

Given a training set with $N$ samples, indicated by $\left(X_{i}, Y_{i}\right)\left(X_{i} \in R^{n}, Y_{i} \in R^{t}, i=1,2,3, \ldots, N\right)$, where $X_{i}$ and $Y_{i}$ denote the feature representation and the targeted output of the $i$ th sample, respectively. Suppose the encoder consists of $K$ hidden layers, each with $L_{i}(1 \leq i \leq K)$ neurons. The output $O=$ $\left[o_{1}, o_{2}, \ldots, o_{N}\right]^{T}$ can be expressed as:

$\sum_{i=1}^{K} \beta_{i} g\left(W_{i} \cdot x_{j}+b_{j}\right)=o_{j}, j=1,2, \ldots, N$

where $g(\mathrm{x})$ is the activation function, $\beta_{i}$ is the output weight, $W_{i}$ is the input weight and $b_{j}$ is the $j$ th bias of the first hidden layer. Ideally, there should be:

$\sum_{j=1}^{N}\left\|o_{j}-Y_{j}\right\|=0$

that is, there exists $\beta_{i}, W_{i}$ and $b_{i}$ such that

$\sum \beta_{i} g\left(W_{i} \cdot x_{j}+b_{j}\right)=Y_{j}, j=1,2, \ldots, N$

which can be represented by matrixes as

$H \beta=Y$

where $H$ is the output of the hidden layer node, $\beta$ is the output weight, and $Y$ is the desired output.

$H\left(W_{1}, W_{2}, \ldots, W_{K}, b_{1}, b_{2}, \ldots, b_{K}, x_{1}, x_{2}, \ldots, x_{N}\right)=\left[\begin{array}{ccc}g_{1}\left(X_{1}\right) & \cdots & g_{K_{1}}\left(X_{1}\right) \\ \vdots & \ddots & \vdots \\ g_{1}\left(X_{N}\right) & \cdots & g_{K_{1}}\left(X_{N}\right)\end{array}\right]$

To train the single hidden layer ELM neural network is equivalent to obtaining $\hat{\beta}$ such that

$\|H \hat{\beta}-Y\|=\min _{\beta}\|H \beta-Y\|$

When choosing the mean square error (MSE) as the measure, this formula is equivalent to minimizing the following loss function:

Loss $=\sum_{j=1}^{N}\left(\sum_{i=1}^{K} \beta_{i} g\left(W_{i} \cdot x_{j}+b_{i}\right)-Y_{j}\right)^{2}$

The ELM permits the weights $\beta$ and the deviation between the latent layer and the inputs to possess arbitrary values that can be drawn from any distribution. This signifies that the learning increment solely determines the optimal weight $\beta$ between the latent layer and the output. The unmodified Extreme Learning Machine (ELM) is limited in effectively processing data contents, even with abundant hidden nodes. In this study, the customized Hierarchical ELM (HELM) was propounded to redress this inadequacy, which stacks multiple layers of ELM to engender a more profound structure. The proposed HELM-based semisupervised learning consists of two phases, i.e., self-supervised training for feature learning and supervised fine-tuning, as visualized in Figure 6.



Figure 6 The Framework of HELM-based Semi-supervised Machine Learning Method.

The HELM model is initially trained purely self-supervised on normal data samples exclusively, with all anomalous examples excluded from this training set. By minimizing a reconstruction error loss function, the stacked ELM autoencoder layers learn to capture the most salient features of the input data that represent its intrinsic normal characteristics. These extracted feature representations encapsulate the critical properties of standard system behavior. Subsequently, the learned feature embeddings are transferred to a one-class classifier, which undergoes further supervised training to obtain a decision threshold $\tau$. This threshold calibration phase notably utilizes an unseen validation dataset containing only normal data samples. Withholding this validation set during ELM feature learning prevents overfitting the threshold to any potential anomalies in the original training data. Overall, this staged procedure enables robust unsupervised feature extraction from normal data, followed by supervised threshold tuning to facilitate effective anomaly detection. Usually, a good threshold $\tau$ can be expressed by

$\tau=\gamma \cdot$ percentile $_{p}\left(\left|1-\boldsymbol{Y}^{\text {valid }}\right|\right)$

where $\boldsymbol{Y}^{\text {valid }}$ is the output of the one-class classifier, percentile $p_{p}$ is a function of the $p$ th percentile with hyperparameters $p$ and $\gamma \geq 0$.

Finally, in the deployment phase, newly observed data samples are propagated through the trained HELM model to obtain the corresponding outputs from the one-class classifier. These outputs denoted by $\boldsymbol{Y}^{\text {test }}$, are compared against the decision threshold $\tau$ established during the training process. Recall this threshold was calibrated on the separate validation dataset to avoid overfitting. The label assignment for each new test sample is then determined by thresholding its one-class output as follows:

Label $_{\boldsymbol{Y}^{\text {test }}}=\operatorname{sgn}\left(\tau-\left|1-\boldsymbol{Y}^{\text {test }}\right|\right)$

In summary, the trained HELM model derives layered feature representations of newly observed test data in a purely data-driven manner. Anomalies can be effectively detected by propagating these examples through the model and comparing the resulting one-class classifier decisions to the calibrated threshold $\tau$. This approach benefits from the model's unsupervised learning of salient features from normal training data. The deep HELM architecture can capture robust intrinsic representations to encapsulate standard system behavior. Thresholding the one-class outputs relative to $\tau$ allows identifying deviations from this learned notion of normality in deployed operation. Overall, this framework provides a selfsupervised feature learning mechanism to represent normal data and a thresholding technique for informed anomaly detection in practice. The model framework of the HELM-based semi-supervised machine learning method is delineated in Figure 6.

## EXPERIMENT AND RESULTS

## A. Dataset arrangement

This experiment mainly compares the results of inputting different feature condition models under the same model. Initially, the built training dataset contained 290,690 instances, which included noisy and inconsistent data. In this study, several techniques were employed to address these issues, such as utilizing the dropna function to eliminate instances with NULL and missing values and refining the original datasets.

The dataset itself includes the following features: frameNum, carId, carCenterXft, carCenterXm, carCenterYft, carCenterYm, headXft, headYft, tailXft, tailYft, speed (mph), speed (m/s), heading, and laneId. Next, the time interval was determined by calculating the difference in Timestamp values using frameNum between adjacent later samples and their corresponding former ones. Based on this, the speed together with acceleration (both longitudinal and lateral) for each vehicle was computed. Subsequently, using the frameNum as the index, the distances and two-dimensional time-to-collision (2D-TTC) between all relevant vehicles at the same timestamp were calculated. As the quantity of normal driving data samples is far beyond the abnormal ones, to balance the quantity of abnormal and normal data samples, this study sampled the normal driving samples. In the end, the examined dataset comprised a total of 23,605 samples, consisting of 12,125 normal instances and 11,480 anomaly instances. All anomaly instances are utilized for testing and 3,638 normal instances are adopted for testing. As anomaly instances are more critical, this study examined more anomaly instances in the estimation of model performance.

## B. Evaluation Metrics

Various metrics will be adopted to evaluate the overall performance of the selected model, and the discrimination evaluation of the optimal model can be defined based on the confusion matrix (35), as shown in Table 4.

TABLE 4 Confusion matrix and the corresponding array representation

|  | Actual Positive Class | Actual Negative Class |
| :---: | :---: | :---: |
| Predicted Positive Class | True-positive (TP) | False-negative (FN) |
| Predicted Negative Class | False positive (FP) | True-negative (TN) |

In binary classification, one class constitutes the positive class, whereas the other delineates the negative class. The positive class epitomizes the events the model endeavors to detect, i.e., abnormal driving in this study, while the negative class constitutes other contingencies, i.e., normal driving in this study. TP (True Positive) and TN (True Negative) denote the quantity of accurately classified positive and negative exemplars. In this study, TP represents the correctly detected driving anomalies, and TN constitutes the accurately detected normal driving samples. On the other hand, FP (False Positive) and FN (False Negative)
represent the number of misclassified positive and negative instances, meaning the incorrectly detected anomalies/normal instances. Accuracy, precision, and recall were computed based on these four terms.

Accuracy refers to the proportion of true results among the total number of cases examined.

Accuracy $=\frac{T P+T N}{T P+T N+F P+F N}$

Precision is utilized to gauge the accurate prediction of positive patterns among the total predicted patterns in a positive class.

Precision $=\frac{T P}{T P+F P}$

Another widely utilized measure is recall, which accounts for the proportion of actual Positives that are correctly classified:

Recall $=\frac{T P}{T P+F N}$

The F1-score is a measure combining and balancing Precision and Recall, and it is defined as the harmonic mean of Precision and Recall:

F1 - score $=2 \times \frac{\text { precision } \times \text { recall }}{\text { precision }+ \text { recall }}$

Finally, the True Positive Rate (TPR) and False Positive Rate (FPR) are also examined as evaluation metrics. As indicated in their names, TPR and FPR are calculated as

$T P R=\frac{T P}{T P+F N}$

$F P R=\frac{F P}{F P+T N}$

## C. Ablation Study Regarding Features

Three experimental settings with distinct feature representations are designed to evaluate the impact of input information on model performance. As illustrated in Table 5, Setting 1 utilizes only the raw coordinates, velocity, and vehicle angle features inherently present in the dataset. Setting 2 augments Setting 1 by incorporating two additional engineered features of lateral acceleration and inter-vehicle distance. Finally, Setting 3 further supplements Setting 2 by including a 2D-TTC feature capturing temporal proximity. By comparing results between these controlled settings, the incremental value of providing basic motion features (Setting 2) and surrogate safety measures features (Setting 3) over the raw dataset (Setting 1) can be quantified. The proposed three experimental settings serve to elucidate the effect of step-wise enriching the feature space on the learning capabilities of the model under controlled conditions.

TABLE 5 Input features in different settings

| Experimental Setting | Input Features |
| :--- | :--- |
| 1 | coordinates/velocity/angle |
| 2 | coordinates/velocity/angle/acceleration/distance |
| 3 | coordinates/velocity/angle/2D time-to-collision |

## D. Results and Comparison

The testing results of the proposed HELM model together with the two baselines are illustrated in Figures 7, 8, 9, and Table 6. In general, the HELM model outperforms Robust Covariance and Isolation Forest, with the best variant delivering the best accuracy at $99.58 \%$ and the best F-1 measure at 0.9913 .


Figure 7 Robust Covariance performance under Settings 1,2, and 3.


Figure 8 Isolation Forest performance under Settings 1,2, and 3


Figure 9 HELM performance under Settings 1, 2, and 3

TABLE 6 Comparison results under different settings

| Model | Setting | Accuracy | Precision | Recall | F1-Score | FPR | TPR |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | 1 | 0.3337 | 0.7628 | 0.1779 | 0.3735 | 0.1745 | 0.1779 |
| Robust Covariance | 2 | 0.3348 | 0.7702 | 0.1767 | 0.3762 | 0.1663 | 0.1767 |
|  | 3 | 0.9570 | 0.9487 | 0.9973 | 0.9028 | 0.1701 | 0.9973 |
|  | 1 | 0.5789 | 0.8766 | 0.5185 | 0.4680 | 0.2303 | 0.5185 |
| Isolation Forest | 2 | 0.4387 | 0.8673 | 0.3080 | 0.4219 | 0.1487 | 0.3080 |
|  | 3 | 0.9615 | 0.9517 | 1.0000 | 0.9131 | 0.1600 | $\mathbf{1 . 0 0 0 0}$ |
|  | 1 | 0.9471 | 0.9349 | 1.0000 | 0.8766 | 0.2196 | $\mathbf{1 . 0 0 0 0}$ |
| HELM | 2 | 0.9614 | 0.9561 | 0.9949 | 0.9144 | 0.1440 | 0.9949 |
|  | 3 | $\mathbf{0 . 9 9 5 8}$ | $\mathbf{0 . 9 9 6 3}$ | $\mathbf{0 . 9 9 8 3}$ | $\mathbf{0 . 9 9 1 3}$ | $\mathbf{0 . 0 1 1 8}$ | 0.9983 |

Experiments across three experimental settings demonstrate enhanced abnormal driving behavior identification capabilities by incorporating the proposed novel 2D-TTC feature. Furthermore, the proposed semi-supervised Hierarchical Extreme Learning Machine (HELM) model achieves consistently superior performance compared to the alternative baseline models in all three experimental settings.

In the baseline Setting 1, with only raw coordinates, velocity, and angle, served as the input features, the HELM model attains an accuracy of 0.9471 . Then, augmenting with acceleration and inter-vehicle distance features, in Setting 2, the accuracy of HELM is improved to 0.9614. Notably, further inclusion of the proposed 2D-TTC feature in Setting 3, the accuracy of HELM is dramatically enhanced to 0.9958, alongside with near-perfect scores for Precision (0.9963), Recall (0.9983), F1-score (0.9913), and FPR $(0.0118)$. This underscores the representational outstanding value of 2D-TTC as an important spatialtemporal feature for this task.

Similarly, unsupervised models (which work in a semi-supervised way in this study) exhibit substantial gains when endowed with 2D-TTC. For instance, the Precision and Recall of Robust Covariance are improved by over 20\%, while the Accuracy and F1-score of Isolation Forest are increased by $5 \%$ and $10 \%$, respectively. Nevertheless, the semi-supervised HELM approach outperforms these two baseline models across all metrics except for TPR.

Finally, scatter visualization of the result obtained by the proposed semi-supervised method using HELM is provided in Figure 10. From the visualization, it is further demonstrated that the HELM can distinguish between normal and abnormal driving behaviors. However, it can not tell the severe abnormal apart from the weak abnormal instances as the values of their $\left|1-\boldsymbol{Y}^{\text {test }}\right| / \tau$ are similar. How to distinguish the severity of abnormal driving behavior using semi-supervised machine learning can be an interesting future research direction.

In summary, augmenting the feature space with the proposed 2D-TTC representation consistently improves the anomaly detection capabilities across models. The HELM framework integrating 2D-TTC markedly surpasses other baseline models, demonstrating the advantages and superiority of the proposed semi-supervised learning method together with the spatial-temporal feature engineering for anomalous driving behavior identification.



Figure 11 Scatter visualization of the result obtained by Semi-supervised HELM.

## CONCLUSION AND FUTURE WORK

This study presented a semi-supervised machine learning framework leveraging Surrogate Safety Measures (SSMs) to enhance abnormal driving behavior detection. A large-scale real-world naturalistic driving dataset was analyzed and various abnormal driving behaviors were revealed and categorized in this study. A Hierarchical Extreme Learning Machines (HELM) model was proposed which harnesses unlabeled data for self-supervised pre-training and partially labeled data for fine-tuning. The two dimensional time-to-collision (2D-TTC), one type of SSM, was introduced as an important feature, with experiments demonstrating that integrating 2D-TTC significantly improves the detection accuracy by over $5 \%$ for all the tested models compared to baseline experimental feature settings.

By training on unlabeled data, and employing only a small sample of labeled data for fine-tuning, the proposed semi-supervised approach achieved competitive performance while reducing dependency on fully labeled datasets, making it well-suited for real-world applications with limited labeled data. Notably, incorporating SSMs, specifically 2D-TTC, played a pivotal role in enhancing model performance. These compelling results underscore the critical value of SSMs in effectively detecting abnormal driving behaviors across diverse ML algorithms. This fusion of semi-supervised learning and SSM utilization as input features showcases the potential for advancing abnormal driving behavior detection capabilities, with significant implications for safety-oriented research and evaluations.

While the current study focused on detection, future work should explore predictive capabilities to enable earlier identification of impending abnormal behaviors before manifestation. Developing techniques to extract robust spatial-temporal driving patterns as model inputs could further enhance performance. The adopted dataset encompassed only three abnormal driving behavior types in this study. Future research should incorporate an expanded diversity of behaviors and associated SSMs to enrich the understanding and identification of anomalies. Nevertheless, this pioneering research provides a step toward data-driven monitoring of abnormal driving for improved road traffic and transportation safety.

## ACKNOWLEDGMENTS

This work was supported by the Applied and Technical Sciences (TTW), a subdomain of the Dutch Institute for Scientific Research (NWO) through the Project Safe and Efficient Operation of Automated and Human-Driven Vehicles in Mixed Traffic (SAMEN) under Contract 17187.

## Note

Author Contributions

The authors confirm their contribution to the paper as follows: study conception and design: Y. Dong, and L. Zhang; data collection: L. Zhang and Y. Dong; analysis and interpretation of results: L. Zhang, Y. Dong, H. Farah, A. Zgonnikov, and B. van Arem; draft manuscript preparation: L. Zhang, Y. Dong, and H. Farah. All authors reviewed the results and approved the final version of the manuscript.

## REFERENCES

1. World Health Organization. Global Status Report On Road Safety 2018. World Health Organization. 2018
2. Saiprasert, C., and W. Pattara-Atikom. Smartphone Enabled Dangerous Driving Report System. Hawaii international conference on system sciences, 2013.
3. Mohammadnazar, A., R. Arvin, and A. J. Khattak. Classifying Travelers' Driving Style Using Basic Safety Messages Generated by Connected Vehicles: Application of Unsupervised Machine Learning. Transportation Research Part C: Emerging Technologies, Vol. 122, 2021. https://doi.org/10.1016/j.trc.2020.102917.
4. Academic Accelerator. Aggressive Driving: Encyclopedia, Science News \& Research Reviews. https://academic-accelerator.com/encyclopedia/aggressive-driving
5. Sarker, I. H. Machine Learning: Algorithms, Real-World Applications and Research Directions. $S N$ Computer Science. 3. Volume 2. 2021.
6. Nikolaou, D., A. Ziakopoulos, and G. Yannis. A Review of Surrogate Safety Measures Uses in Historical Crash Investigations. Sustainability (Switzerland). 9. Volume 15. 2023.
7. Tarko, A. P. Surrogate Measures of Safety. In Safe Mobility: Challenges, Methodology and Solutions (D. Lord and S. Washington, eds.), Emerald Publishing Limited, pp. 383-405. 2018.
8. Wang, C., Y. Xie, H. Huang, and P. Liu. A Review of Surrogate Safety Measures and Their Applications in Connected and Automated Vehicles Safety Modeling. Accident Analysis and Prevention, Vol. 157, 2021. https://doi.org/10.1016/j.aap.2021.106157.
9. Bonela, S. R., and B. R. Kadali. Review of Traffic Safety Evaluation at T-Intersections Using Surrogate Safety Measures in Developing Countries Context. IATSS Research. 3. Volume 46, 307321. 2022 .
10. Lu, C., X. He, H. van Lint, H. Tu, R. Happee, and M. Wang. Performance Evaluation of Surrogate Measures of Safety with Naturalistic Driving Data. Accident Analysis and Prevention, Vol. 162, 2021. https://doi.org/10.1016/j.aap.2021.106403.
11. Zheng, O., M. Abdel-Aty, L. Yue, A. Abdelraouf, Z. Wang, and N. Mahmoud. CitySim: A DroneBased Vehicle Trajectory Dataset for Safety Oriented Research and Digital Twins. Transportation Research Record : Journal of the Transportation Research Board, 2023. https://doi.org/10.1177/03611981231185768.
12. Chen, Z., J. Yu, Y. Zhu, Y. Chen, and M. Li. D3: Abnormal Driving Behaviors Detection and Identification Using Smartphone Sensors. 2015. IEEE Communications Society, and Institute of Electrical and Electronics Engineers. 2015 12th Annual IEEE International Conference on Sensing, Communication, and Networking - Workshops (SECON Workshops)
13. Kim, D. G., C. Lee, and B. J. Park. Use of Digital Tachograph Data to Provide Traffic Safety Education and Evaluate Effects on Bus Driver Behavior. Transportation Research Record, Vol. 2585, 2016, pp. 77-84. https://doi.org/10.3141/2585-09.
14. Jia, S., F. Hui, S. Li, X. Zhao, and A. J. Khattak. Long Short-Term Memory and Convolutional Neural Network for Abnormal Driving Behaviour Recognition. IET Intelligent Transport Systems, Vol. 14, No. 5, 2020, pp. 306-312. https://doi.org/10.1049/iet-its.2019.0200.
15. Hamad, F. A., R. Hasiba, D. Shahwan, and H. I. Ashqar. How Do Drivers Behave at Roundabouts in a Mixed Traffic? A Case Study Using Machine Learning. 2023. arXiv preprint arXiv:2309.13442.
16. Lim, S., and J. H. Yang. Driver State Estimation by Convolutional Neural Network Using Multimodal Sensor Data. Electronics Letters, Vol. 52, No. 17, 2016, pp. 1495-1497. https://doi.org/10.1049/el.2016.1393.
17. Yang, Q., F. Lu, J. Wang, D. Zhao, and L. Yu. Analysis of the Insertion Angle of Lane-Changing Vehicles in Nearly Saturated Fast Road Segments. Sustainability (Switzerland), Vol. 12, No. 3, 2020. https://doi.org/10.3390/su12031013.
18. Prasad, N. R., S. Almanza-Garcia, and T. T. Lu. Anomaly Detection. Computers, Materials and Continua, Vol. 14, No. 1, 2009, pp. 1-22. https://doi.org/10.1145/1541880.1541882.
19. Pimentel, M. A. F., D. A. Clifton, L. Clifton, and L. Tarassenko. A Review of Novelty Detection. Signal Processing. Volume 99, 215-249. 2014.
20. Erfani, S. M., S. Rajasegarar, S. Karunasekera, and C. Leckie. High-Dimensional and Large-Scale Anomaly Detection Using a Linear One-Class SVM with Deep Learning. Pattern Recognition, Vol. 58, 2016, pp. 121-134. https://doi.org/10.1016/j.patcog.2016.03.028.
21. Dai, J., J. Teng, X. Bai, Z. Shen, and D. Xuan. Mobile Phone Based Drunk Driving Detection. 2010. In 2010 4th International Conference on Pervasive Computing Technologies for Healthcare (pp. 18). IEEE.
22. Dhar, P., S. Shinde, and A. Bhaduri. Unsafe Driving Detection System Using Smartphone as Sensor Platform. 2014. International Journal of Enhanced Research in Management \& Computer Applications.
23. Planek, T. W., S. Sinelnikov, J. Thomas, K. Kolosh, and K. Porretta. Letter from the Editors - Fourth International Symposium on Naturalistic Driving Research. Journal of Safety Research. Volume 54, 29.
24. Lu, J., O. Grembek, and M. Hansen. Learning the Representation of Surrogate Safety Measures to Identify Traffic Conflict. Accident Analysis and Prevention, Vol. 174, 2022. https://doi.org/10.1016/j.aap.2022.106755.
25. Wang, X., A. J. Khattak, J. Liu, G. Masghati-Amoli, and S. Son. What Is the Level of Volatility in Instantaneous Driving Decisions? Transportation Research Part C: Emerging Technologies, Vol. 58, 2015, pp. 413-427. https://doi.org/10.1016/j.trc.2014.12.014.
26. Kuang, Y., X. Qu, and S. Wang. A Tree-Structured Crash Surrogate Measure for Freeways. Accident Analysis and Prevention, Vol. 77, 2015, pp. 137-148. https://doi.org/10.1016/j.aap.2015.02.007.
27. Xing, L., J. He, M. Abdel-Aty, Q. Cai, Y. Li, and O. Zheng. Examining Traffic Conflicts of up Stream Toll Plaza Area Using Vehicles' Trajectory Data. Accident Analysis and Prevention, Vol. 125, 2019, pp. 174-187. https://doi.org/10.1016/j.aap.2019.01.034.
28. Jiao, Y. A fast calculation of two-dimensional Time-to-Collision. https://github.com/YiruJiao/Two-Dimensional-Time-To-Collision. Accessed March 9, 2024.
29. Van Der Horst, R., and J. Hogema. Time-To-Collision And Collision Avoidance Systems. In Proceedings of the $6^{\text {th }}$ International Cooperation on Theories and Concepts in Traffic safety (ICTCT) workshop Salzburg
30. Liu, F. T., Ting, K. M., and Zhou, Z.-H., "Isolation Forest," 2008 Eighth IEEE International Conference on Data Mining, Pisa, Italy, 2008, pp. 413-422, doi: 10.1109/ICDM.2008.17.
31. Butakov, N. How to Build Robust Anomaly Detectors with Machine Learning. 2020. https://www.ericsson.com/en/blog/2020/4/anomaly-detection-with-machine-learning. Accessed March 9, 2024.
32. Rousseeuw, P. J., and K. Van Driessen. A Fast Algorithm for the Minimum Covariance Determinant Estimator. Technometrics, 1999. https://doi.org/10.1080/00401706.1999.10485670.
33. Tang, J., Deng, C., \& Huang, G. Bin. Extreme Learning Machine for Multilayer Perceptron. IEEE Transactions on Neural Networks and Learning Systems, 27 (4), 2016, 809-821. https://doi.org/10.1109/TNNLS.2015.2424995.
34. Chen, L., Zhang, Y. H., Huang, G., Pan, X., Wang, S. P., Huang, T., \& Cai, Y. D. Discriminating cirRNAs from other IncRNAs using a hierarchical extreme learning machine (H-ELM) algorithm with feature selection. Molecular Genetics and Genomics, 293(1), 2018, 137-149. https://doi.org/10.1007/s00438-017-1372-7.
35. M, H., and S. M.N. A Review on Evaluation Metrics for Data Classification Evaluations. International Journal of Data Mining \& Knowledge Management Process, 2015. https://doi.org/10.5121/ijdkp.2015.5201.
