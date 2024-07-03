Data-driven Semi-supervised Machine Learning with Surrogate Safety Measures for Abnormal Driving Behavior Detection Lanxin Zhang\#
Faculty of Civil Engineering and Geosciences Delft University of Technology, Delft, The Netherlands, 2628 CN Email: zhanglx2018@hotmail.com Yongqi Dong\#,*
Faculty of Civil Engineering and Geosciences Delft University of Technology, Delft, The Netherlands, 2628 CN
Email: y.dong-4@tudelft.nl Haneen Farah Faculty of Civil Engineering and Geosciences Delft University of Technology, Delft, The Netherlands, 2628 CN Email: h.farah@tudelft.nl Arkady Zgonnikov Faculty of Mechanical, Maritime and Materials Engineering Delft University of Technology, Delft, The Netherlands, 2628 CN
Email: a.zgonnikov@tudelft.nl Bart van Arem Faculty of Civil Engineering and Geosciences Delft University of Technology, Delft, The Netherlands, 2628 CN Email: b.vanArem@tudelft.nl
\# These authors contributed equally to this work and should be considered as co-first authors. * Corresponding author.

Submitted [30 November 2023]
2

## Abstract

Detecting abnormal driving behavior is critical for road traffic safety and the evaluation of drivers' behavior. 

With the advancement of machine learning (ML) algorithms and the accumulation of naturalistic driving data, many ML models have been adopted for abnormal driving behavior detection. Most existing MLbased detectors rely on (fully) supervised ML methods, which require substantial labeled data. However, ground truth labels are not always available in the real world, and labeling large amounts of data is tedious. Thus, there is a need to explore unsupervised or semi-supervised methods to make the anomaly detection process more feasible and efficient. To fill this research gap, this study analyzes large-scale real-world data revealing several abnormal driving behaviors (e.g., sudden acceleration, rapid lane-changing) and develops a Hierarchical Extreme Learning Machines (HELM) based semi-supervised ML method using partly labeled data to accurately detect the identified abnormal driving behaviors. Moreover, previous ML-based approaches predominantly utilize basic vehicle motion features (such as velocity and acceleration) to label and detect abnormal driving behaviors, while this study seeks to introduce Surrogate Safety Measures 
(SSMs) as the input features for ML models to improve the detection performance. Results from extensive experiments demonstrate the effectiveness of the proposed semi-supervised ML model with the introduced SSMs serving as important features. The proposed semi-supervised ML method outperforms other baseline semi-supervised or unsupervised methods regarding various metrics, e.g., delivering the best accuracy at 99.58% and the best F-1 measure at 0.9913. The ablation study further highlights the significance of SSMs for advancing detection performance.

Keywords: Abnormal driving behavior, Semi-supervised machine learning, Hierarchical extreme learning machines, Self-supervised training, Surrogate safety measure 

## Introduction

Road traffic safety has become a growing concern worldwide. The World Health Organization (1)
reported that approximately 1.35 million people died in car crashes in 2018, with over 30 million suffering non-fatal injuries. These accidents not only resulted in disabilities but also caused significant economic loss, reaching as high as 3% of the gross domestic product in some countries. It is alarming that in 92.9% of accidents, human factors were identified as contributing factors (2). This highlights the urgent need to identify abnormal driving behaviors and find ways to prevent or mitigate accidents caused by such abnormal human driving behaviors. 

Driving behavior encompasses various variables and factors, including driving performance, environmental awareness, risk-taking propensity, and reasoning abilities (3). Abnormal driving behavior refers to actions that deviate from safe and normal driving, posing risks to oneself, passengers, and other road users. Examples of such behavior include excessive speeding, tailgating, and erratic lane changes (4). These abnormal driving behaviors frequently engender severe traffic altercations, including collisions, crashes, and other minor incidents, thereby underscoring the necessity of addressing and precluding these actions. Precise and efficacious monitoring of aberrant driving behaviors is integral to augmenting driving safety, enhancing driver cognition of driving patterns, and attenuating prospective road accidents.

Machine learning (ML)-based approaches have shown great promise in detecting abnormal driving behaviors. They can learn complex patterns, adapt to changing scenarios, handle large and diverse datasets, and detect unusual behaviors with optimized processes (5). However, most of the available studies adopted fully-supervised ML models to do the detection, and few of them explored un-supervised or semisupervised ML methods. While in the real world, ground truth labels are sometimes missing or inaccurate, pluslabeling large amounts of data is tedious and even dangerous under certain critical situations. Therefore, examining and developing unsupervised or semi-supervised methods is imperative to engender more feasible and efficient abnormal driving behavior detection.

On the other hand, Surrogate Safety Measures (SSMs) show promise as robust indicators and proxy measurements of sustainable road safety that can supplement or replace traditional historical crash analyses. Since SSMs do not rely directly on crash data, employing them allows proactive road safety assessment without the need to collect crash data (6). This obviates crash data collection and enables investigating areas before any crashes occur. As Tarko (7) notes, SSMs facilitate detecting excessive crash risk, better understanding crash-precipitating conditions, and estimating countermeasure efficacy. To effectively assess and predict road safety, SSMs have gained popularity as indirect safety indicators using proxy variables correlated with safety outcomes. By providing insights into potential safety issues, SSMs help prioritize improvement efforts. Wang et al. (8) categorize SSMs into two classes: time-based, deceleration-based, and energy-based SSMs, e.g., time-to-collision (TTC), post-encroachment time (PET), time-to-crash/accident 
(TC/TA), deceleration rate to avoid a crash (DRAC), that apply thresholds to identify traffic conflicts, extensively utilized in road safety research (6, *9, 10*). There is no doubt SSMs can serve as important features in various tasks. However, for abnormal driving behavior detection, previous studies predominantly employed basic vehicle motion as features to label and detect behaviors, and seldom explored the benefits of SSMs.

To fill the aforementioned research gaps, this study aims to develop a novel data-driven approach for abnormal driving behavior detection using real-world naturalistic driving data and leveraging semisupervised ML with self-supervised training to enhance the performance and effectiveness of the detection system. Specifically, this study first analyzes a large-scale dataset, i.e., the CitySim dataset (11), with vivid visualizations and extracts various abnormal driving behaviors. Then, the study develops a Hierarchical Extreme Learning Machines (HELM) based semi-supervised ML model using unlabeled data to carry out self-supervised pre-training and leveraging only partly labeled data to fine-tune the model for accurately detecting the identified abnormal driving behaviors. Furthermore, this study conducts a significative ablation study introducing Surrogate Safety Measures (SSMs) as the input features for the developed semisupervised ML model to further advance the detection performance. Extensive experiments verified the proposed method, especially with the proposed semi-supervised HELM model using SSMs in its input features outperforms other baseline models, delivering the best accuracy at 99.58% and the best F1-measure at 0.9913.

In short, by bridging the gap and addressing the limitations of existing methods, this research endeavors to improve road safety and reduce accidents caused by abnormal driving behaviors. It addresses the limitations of traditional supervised approaches and overcomes the scarcity of labeled abnormal driving data. The study analyzes open-sourced datasets and provides meaningful insights into understanding and categorizing human driving behavior. The conclusions elucidated in this manuscript constitute the bedrock for constructing more precise and resilient models for detecting aberrant driving behavior. 

## Related Work

A number of studies have investigated abnormal driving behaviors, with Chen et al. (12) and Kim et al. (13) putting forth definitions that reflect divergent conceptualizations of driving conduct between Eastern and Western cultures as shown in **Table 1**. The Western driving culture emphasises whether the vehicle's location complies with regulations, whereas the Eastern prioritizes speed modulation, potentially shaped by population density and vehicle volume. Through a comprehensive literature review, the current study delineates abnormal driving as a function of position and velocity, concentrating on abrupt starts, emergency braking, as well as rapid and close lane changes.

| U.S. National Highway Traffic Safety Administration   | Korea Ministry of Land, Infrastructure and Transport   |
|-------------------------------------------------------|--------------------------------------------------------|
| (NHTSA)                                               | (MOLIT)                                                |
| Weaving                                               | Sudden start                                           |
| Swerving                                              | Speeding                                               |
| Sideslipping                                          | Long-standing speeding                                 |
| Fast U-turn                                           | Sudden braking                                         |
| Turning with a wide radius                            | Sudden overtaking                                      |
| Sudden braking.                                       | Sudden changing lanes                                  |
| ---                                                   | Sudden turning                                         |

Machine learning (ML)-based approaches for detecting abnormal driving behaviors have garnered substantial research attention and exhibited robust performance. Both supervised and unsupervised methodologies have been commonly utilized in prior investigations of abnormal driving studies. Supervised techniques necessitate labeled data during model training, whereby the system ascertains the mapping between inputs and outputs to categorize and predict new data points. For example, Jia et al. (14) devised a model integrating long short-term memory (LSTM) neural network and convolutional neural network 
(CNN) architectures to pinpoint instances of extreme acceleration and deceleration. Shahverdy et al. (15) proposed a lightweight 1-dimensional CNN (1D-CNN) exhibiting high efficiency and low computational overhead for classifying driver actions. Ryan et al. (16) simulated an end-to-end model leveraging CNN to contrast human and autonomous vehicle driving patterns.

Conversely, unsupervised machine learning techniques entail training models using raw, unlabeled data. This approach is frequently utilized during exploratory phases to derive insights from the dataset. As an illustration, Mohammadnazar et al. (3) developed an architecture leveraging unsupervised machine learning to quantify driving performance and categorize driving styles across diverse spatial contexts. Feng et al. (17) proposed a Support Vector Clustering methodology to classify driving manners robustly. Extant literature denotes substantial challenges in accurately identifying anomalies through solely unsupervised machine learning. As Chandola et al. (18) concluded from their review, unsupervised anomaly detection approaches often demonstrate inferior detection rates and heightened false positive rates on real-world problems. Correspondingly, Pimentel et al. (19) discovered via benchmark assessments that complete dependency on unsupervised outlier detection is imprudent, as these techniques fail to detect all anomalies. Erfani et al. (20) further contended that purely unsupervised methodologies lack the learning guidance to 4 precisely differentiate normal from aberrant patterns. Synthesizing these conclusions, utilizing only unsupervised ML without any labeled data to achieve accurate anomaly detection is hardly possible. Even if viable, the detection performance based on pure unsupervised ML is highly possible to be further enhanced by labeled data. Therefore, the research consensus firmly denotes the necessity for making use of at least partially labeled data to supervise and augment anomaly detection capabilities with semi-supervised ML approaches.

Regarding the features utilized as inputs for ML models, traditional indicators such as velocity, acceleration, and steering angle have been extensively employed (*14, 16, 21–23*). For example, Lim & Yang (16) considered vehicular data comprising velocity, acceleration, steering angle, and gas pedal position and leveraged a CNN model to estimate driver drowsiness, workload, and distraction levels. Planek et al. (23) collected lateral vehicle position, steering angle, and speed-related information and implemented a Support Vector Machine (SVM) model to differentiate between normal and intoxicated driving states. Incorporating Surrogate Safety Measures into ML-based methods is supposed to be promising for various tasks but has seldom been investigated yet. To the best knowledge of the authors and after extensive review, only one study was found to be relevant, i.e., Lu et al. (24) integrated the representation of TTC together with the driver maneuver profiles into a deep unsupervised learning and clustering method with their proposed Transformer encoder based model to identify traffic conflicts and non-conflicts. However, they only investigated situations of one intersection and one roundabout in the USA, neglecting other various types of driving anomalies, especially those related to highway driving. 

Investigating the potential of semi-supervised approaches, which utilize both labeled and unlabeled examples, is imperative to enhance abnormal driving behavior detection, yet scarce existing research has explored this direction. By harnessing the additional information from unlabeled data, semi-supervised learning can uncover subtle patterns and behaviors that conventional supervised or unsupervised techniques may overlook. This study endeavors to address this research lacuna. Moreover, input features are fundamental for ML-based approaches; to augment detection performance, examining more efficacious features is prudent. In this vein, this study seeks to ascertain the benefits of SSMs, specifically the customized two-dimensional Time to Collision (2D-TTC), as input variables and conducts ablation analyses to verify its efficacy in upgrading abnormal driving behavior identification.

## Dataset And Data Analysis A. Description Of The Data

To conduct data-driven research, a high-quality dataset is imperative. After extensive exploration, the current study utilizes the CitySim dataset (11), comprising video-based trajectory data concentrating on traffic safety in the United States. The CitySim dataset encompasses vehicle trajectory information extracted from videos captured by 12 drones, spanning six road geometry typologies, including freeway segments, signalized intersections, and stop-controlled junctions. The dataset furnishes precise positional details in various formats, including pixels, feet, and GPS coordinates, alongside data on velocity, heading angle, and vehicle lane numbers. **Table 2** provides the fields of the raw data record and provides one example accessible within the dataset.

To bolster the research objectives, supplementary features are derived from the CitySim dataset, encompassing longitudinal acceleration, lateral acceleration, *inter-vehicle distance*, and two-dimensional time-to-collision (2D-TTC). Through assimilating these computed variables with the native dataset, the current study endeavors to augment the data foundations requisite for the model. Notably, the dataset's high precision, with measurements accurate to approximately 10 centimeters, furnishes further reliability and suitability for this research. Before presenting the methodological details, **Table 3** exhibits examples of the data used after the processing. The upcoming methodology section will delineate the precise calculations to derive the additional features from the raw CitySim dataset.

TABLE 2 Data sample of the CitySim dataset

| Feautres        | Value   |
|-----------------|---------|
| frameNum        | 0       |
| carId           | 582     |
| carCenterX (ft) | 462.4   |
| carCenterY (ft) | 184.8   |
| headX (ft)      | 469.6   |
| headY (ft)      | 184.8   |
| tailX (ft)      | 455.3   |
| tailY (ft)      | 184.8   |
| Speed (mph)     | 39.5    |
| Heading (°)     | 180.7   |
| laneId          | 10      |

Table notation: ft---feet; mph---miles per hour; ° --- *degree*

## Table 3 Data Examples After Data Processing

| frameNum                                                                      | carCenterX   | carCenterY (m)   | Speed (m/s)   | Heading   | 2D-TTC   | Distance   | Abnormal=1/   |
|-------------------------------------------------------------------------------|--------------|------------------|---------------|-----------|----------|------------|---------------|
| (m)                                                                           | (°)          | (s)              | (m)           | Normal=0  |          |            |               |
| 10                                                                            | 53.258       | 32.155           | 14.985        | 359.632   | 1.110    | 0.482      | 1             |
| 1737                                                                          | 251.998      | 27.466           | 11.095        | 359.742   | 104.794  | 131.453    | 0             |
| 1739                                                                          | 248.537      | 31.095           | 12.300        | 359.707   | 6001.553 | 128.168    | 0             |
| 1760                                                                          | 251.607      | 27.355           | 11.064        | 359.656   | 110.943  | 131.392    | 0             |
| 11940                                                                         | 128.567      | 31.653           | 16.368        | 359.220   | 0.415    | 0.593      | 1             |
| 11966                                                                         | 127.897      | 31.653           | 16.217        | 359.082   | 0.376    | 0.482      | 1             |
| 11981                                                                         | 127.115      | 31.653           | 16.218        | 358.865   | 0.295    | 0.457      | 1             |
| 12000                                                                         | 126.836      | 31.542           | 16.277        | 358.864   | 0.311    | 0.387      | 1             |
| Table notation: the original distance measure "feet" is converted to "meter". |              |                  |               |           |          |            |               |

## B. Abnormal Driving Behaviors Identified In The Dataset

Based on the reviewed literature's classification and definition of abnormal driving behavior (check section *RELATED WORK*), this section illustrates the specific abnormal driving behaviors observed in the examined CitySim dataset. Each abnormal behavior is associated with one or two indicators, measured or calculated at various locations.

## Rapid Acceleration And Emergency Brake Behavior

The acceleration data corresponding to each velocity datum in the vehicle trajectory dataset, as exhibited in **Figure 1**, facilitates statistical analysis. Extreme acceleration and deceleration coordinates can be derived, denoting abrupt variations when operators enact aberrant maneuvers such as sudden braking or accelerating. Identifying these extreme points enables the segmentation of abnormal driving conduct. A 
specific proportion of extreme acceleration can be pinpointed by statistically scrutinizing all acceleration coordinates at identical speeds across all journeys. Determining an appropriate ratio to differentiate extreme points from normal ones is imperative. A 15% threshold appears judicious based on reiterative experimentation and associated existing research (14, 25).

## Rapid Lane-Changing Behavior

Rapid lane-changing behavior is characterized by sudden and instantaneous abnormal actions that occur for a short duration. In normal driving patterns, vehicles exhibit relatively stable lateral acceleration around zero (as shown in **Figure 2**). However, for abnormal behavior, there manifests an abrupt variation in the vehicle's lateral acceleration. The majority of vehicles exhibiting lane divergence comportment demonstrate a lateral acceleration bounded by ±1 m/s2, whereby they execute lane diversions seamlessly at 6 a fixed velocity. However, the acceleration of some vehicles presents as outliers seen in Figure 3. A normal distribution with a mean of 0 and a standard deviation of 1.3 was examined. According to the characteristics of a normal distribution, approximately 68% of data falls within ±1 standard deviation from the mean.

These outliers beyond ±1 standard deviation from the mean accounted for approximately 32% of the total data points. A ratio of 16% is considered reasonable based on repeated experiments and related research ( 26 ). This satisfies the heuristic definition of outliers as observations differ significantly from most data. Examining outliers based on standard deviation thresholds aligns with statistically grounded techniques for anomaly detection using the sigma principle for normal distributions.  According to the normal distribution, a value greater than 1.3 m/s 2 and less than -1.3m/s 2 will be the filter condition for outliers.







## Close Lane-Changing Behavior

Close lane-changing behavior is characterized by sudden and instantaneous abnormal actions that occur for a short duration. Vehicles in normal driving patterns maintain a certain distance between themselves and adjacent lanes. However, during abnormal behavior, there is a significant decrease in the distance between the vehicle and adjacent lanes, indicating a close lane change. In this thesis, when the distance between two cars during lane-changing is less than 0.5 meters, it is considered severe abnormal driving behavior. In contrast, when the distance is less than 1.0 meters but greater than 0.5 meters, it is considered weak abnormal driving behavior, as seen in Figure 4.



## Methodology

This section first introduces Surrogate Safety Measures (SSMs), focusing on Two Dimensional Time-To-Collision (2D-TTC). Two ML models, i.e., Isolation Forest, and Robust Covariance, are then presented as baseline methods for comparison. Finally, a customized semi-supervised model named Hierarchical Extreme Learning Machines (HELM) is proposed and explained in detail.

## A. Surrogate Safety Measures

In the literature review, some studies have studied and employed simple surrogate safety measures 
(SSMs), such as time-to-collision (TTC). The TTC value is calculated as:

## = 1−2 (1)

$$-{\mathfrak{p}}_{2}$$

However, two salient limitations exist with the conventional TTC calculation: (1) scenarios are deemed safe when the velocity of the following vehicle is less than or equal to the lead vehicle, despite the potential for minimal relative distance between them (26); and (2) the vehicle pair is presumed to occupy the same lane, with merely lateral movements incorporated (27). To surmount these constraints of the standard TTC, the current study implements a novel TTC metric, entitled the two-dimensional TTC (2DTTC) (28):

$$2DTTC=\begin{cases}\frac{\textit{price}}{|v_{t}-v_{j}|},\textit{if the direction of DTC is the same with}(v_{t}-v_{j})\\ \textit{inf},\textit{if the direction of DTC is opposite with}(v_{t}-v_{j})\end{cases}\tag{2}$$



## Figure 5 Illustration Of 2D-Ttc.

In general, according to literature only encounters with a minimum TTC below 1.5 second are deemed critical, with trained observers consistently applying this threshold in practice (29). This study explores the novel input feature 2D-TTC which is specially introduced and derived directly from the dataset parameters. Specifically, the vehicle angle in the dataset decomposes each vehicle's velocity into x-y coordinate components, yielding velocity vectors based on the dataset parameters. 2D-TTC is then calculated per these velocity vectors and the corresponding distance along the same direction. This approach highlights how 2D-TTC can be computed from the raw dataset by leveraging the vehicle angle data to obtain velocity vectors in coordinate space. The derived 2D-TTC is analyzed with input features like position, speed, and acceleration to evaluate anomaly detection performance using the given dataset.

$$(1)$$

## B. Baseline Models

Isolation Forest and Robust Covariance are selected as two baseline methods considering their interpretability, effectiveness, and broad utilization in various domains.

The *Isolation Forest*, initially developed by Liu et al. (30), constitutes an effective algorithm typically utilized for data anomaly detection. It is predicated on the notion that anomalous data points are more readily separable from the remainder of normal samples. To isolate an abnormal data point, the algorithm iteratively generates partitions of the sample by randomly selecting a feature attribute and subsequently randomly choosing a split value within the permissible minimum and maximum values for the selected feature attribute. Through recursive binary partitioning, data points that require fewer splits to become isolated are deemed more anomalous. 

The Isolation Forest algorithm capitalizes on the premise that anomalies are few and different, and thereby manifest topological shorter path lengths (which is elucidated by averaging this value across the trees) when random partitioning is employed. Therefore, it leverages an ensemble of isolation trees generated through such recursive random partitioning to identify anomalies, with shorter average path lengths corresponding to greater anomaly scores.

In practice, the Isolation Forest anomaly detection algorithm involves two primary phases. Firstly, a collection of isolation trees (*iTrees*) are constructed utilizing recursive partitioning on a training dataset. During recursive partitioning, splits are performed by randomly selecting an attribute and random split value to isolate a data point. Secondly, each instance in the test set is propagated through the ensemble of iTrees and assigned an *anomaly score* based on the average path length for that instance across the *iTrees*. 

Shorter average path lengths correspond to fewer partitions required to isolate the instance, indicating more anomalous behavior and higher *anomaly score*. After computing *anomaly scores* for all test instances, those data points with a score exceeding a predefined threshold specific to the domain can be classified as anomalies.

The *Robust Covariance* estimation algorithm presupposes that normal data points exhibit a Gaussian distribution, and accordingly approximates the morphology of the joint distribution (namely, estimates the mean and covariance of the multivariate Gaussian distribution) (31). 

In statistical analysis, the deviation can be gauged by the Z-score. The generalization of the Z-score for a point in the case of a p-dimensional multi-variate probability distribution with some mean μ and covariance matrix Σ is known as Mahalanobis distance 
, which is given by:
 = √( − )
Σ
−1( − ) (3)
It is premised on the fact that outliers engender an augmentation of the values (entries) in Σ, thereby rendering the diffusion of the data ostensibly more extensive. Consequently, |Σ| (the determinant) will likewise be superior, which would theoretically diminish by excising extreme events. Rousseeuw and Van Driessen (32) devised a computationally effectual algorithm capable of furnishing robust covariance approximations. The approach is predicated on the postulation that at minimum h of the n exemplars are 
"normal" (h denoting a hyperparameter). The algorithm inaugurates with k arbitrary samples containing 
(p+1) points. For each k sample, μ, Σ, and |Σ| are estimated, the distances are computed and sorted in ascending order, and the h smallest distances are employed to update the estimates. In their primordial publication, the subroutine of computing distances and revising the estimations of μ, Σ, and |Σ| is entitled a "C-step" whereby two such increments suffice to ascertain efficacious candidates (for μ and Σ) among the k arbitrary samples. In the succeeding step, a subset of magnitude m with the lowest |Σ| (the optimal candidates) is contemplated for computation until convergence, and the sole estimate whose |Σ| is minimal is furnished as output.

Please note, although Isolation Forest and Robust Covariance are usually considered unsupervised ML approaches, in this study only normal data samples are input to train them, thus, in this study, they can be regarded as semi-supervised approaches and are comparable to the proposed semi-supervised machine learning method.