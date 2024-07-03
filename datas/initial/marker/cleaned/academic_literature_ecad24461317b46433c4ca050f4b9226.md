arXiv:2401.07625v2 [stat.ME] 9 Apr 2024



Statistics



 in Survey Jae Kwang Kim



__
l_
l l



I wrote this book as a textbook for the graduate-level sampling class (Stat 521) at Iowa State University. Currently, as of January 15th **in 2024, the** book contains 12 chapters. The current version is probably good enough to understand the classical concepts in survey sampling. In the future, I plan to add more chapters with modern topics such as imputation, data integration, small area estimation, and analytic inference in survey sampling. By releasing the preliminary version to arXiv, the textbook can be accessible to the public, which I think is good for the survey community.

Please let me know by e-mail (jkim@iastate.edu) if you find any typos or errors in the current version of the book.

__
l_
l l



| Preface   | vii                                      |    |    |
|-----------|------------------------------------------|----|----|
| 1         | Introduction                             | 1  |    |
| 1.1       | Introduction                             |    | 1  |
| 1.2       | Probability sample                       |    | 2  |
| 1.3       | Basic Procedures for survey sampling     |    | 6  |
| 1.3.1     | Survey Planning                          |    | 6  |
| 1.3.2     | Design and development                   | 7  |    |
| 1.3.3     | Implementation                           | 7  |    |
| 1.3.4     | Survey Evaluation                        |    | 8  |
| 1.4       | Survey errors                            |    | 8  |
| 2         | Horvitz-Thompson estimation              | 11 |    |
| 2.1       | Introduction                             |    | 11 |
| 2.2       | Horvitz-Thompson estimation              |    | 12 |
| 2.3       | Other parameters                         |    | 17 |
| 2.4       | Discussion                               |    | 18 |
| 3         | Simple and systematic sampling designs   | 21 |    |
| 3.1       | Introduction                             |    | 21 |
| 3.2       | Simple random sampling                   |    | 21 |
| 3.3       | Implementation of simple random sampling |    | 25 |
| 3.4       | Simple random sampling with replacement  |    | 27 |
| 3.5       | Bernoulli Sampling                       |    | 29 |
| 3.6       | Systematic sampling                      |    | 30 |
| 3.7       | Entropy for sampling designs             |    | 34 |
| 4         | Stratified Sampling                      | 37 |    |
| 4.1       | Introduction                             |    | 37 |
| 4.2       | Sample size allocation                   |    | 38 |
| 4.3       | Stratum boundary determination           |    | 45 |
| 4.4       | Number of strata                         |    | 46 |
| 4.5       | Domain Estimation                        |    | 47 |

ix

| x                                                  | Contents                                         |     |     |
|----------------------------------------------------|--------------------------------------------------|-----|-----|
| 5                                                  | Sampling with Unequal probabilities              | 51  |     |
| 5.1                                                | Introduction                                     |     | 51  |
| 5.2                                                | PPS sampling                                     |     | 53  |
| 5.3                                                | Poisson sampling                                 | 55  |     |
| 5.4                                                | Maximum Entropy Sampling                         |     | 59  |
| 5.5                                                | πps sampling                                     |     | 60  |
| 5.6                                                | Systematic πps sampling                          |     | 65  |
| 6                                                  | Cluster Sampling: Single stage cluster sampling  | 67  |     |
| 6.1                                                | Introduction                                     |     | 67  |
| 6.2                                                | Single-stage cluster sampling: Equal Size Case   |     | 68  |
| 6.3                                                | Single-stage cluster sampling: Unequal Size Case |     | 73  |
| 7                                                  | Cluster Sampling: Two-stage cluster sampling     | 77  |     |
| 7.1                                                | Introduction                                     |     | 77  |
| 7.2                                                | Estimation                                       |     | 78  |
| 8                                                  | Estimation: Part 1                               | 87  |     |
| 8.1                                                | Introduction                                     |     | 87  |
| 8.2                                                | Ratio Estimation                                 |     | 87  |
| 8.3                                                | Regression Estimation                            |     | 92  |
| 9                                                  | Estimation: Part 2                               | 99  |     |
| 9.1                                                | GREG estimation                                  |     | 99  |
| 9.2                                                | Optimal Estimation                               |     | 105 |
| 9.3                                                | Model-assisted calibration                       | 109 |     |
| 9.4                                                | Generalized entropy calibration                  |     | 113 |
| 10 Variance Estimation                             | 117                                              |     |     |
| 10.1 Introduction                                  |                                                  | 117 |     |
| 10.2 Linearization approach to variance estimation |                                                  | 119 |     |
| 10.3 Replication approach to variance estimation   |                                                  | 121 |     |
| 10.3.1                                             | Random group method                              |     | 122 |
| 10.4 Jackknife method                              |                                                  | 124 |     |
| 11 Two-phase sampling                              | 129                                              |     |     |
| 11.1 Introduction                                  |                                                  | 129 |     |
| 11.2 Two-phase sampling for stratification         |                                                  | 131 |     |
| 11.3 Regression estimator for two-phase sampling   |                                                  | 135 |     |
| 11.4 Non-nested two-phase sampling                 |                                                  | 143 |     |
| 11.5 Repeated surveys                              |                                                  | 148 |     |

| Contents                                              | xi   |     |
|-------------------------------------------------------|------|-----|
| 12 Nonresponse                                        | 151  |     |
| 12.1 Introduction                                     |      | 151 |
| 12.2 Call-back                                        |      | 152 |
| 12.3 Nonresponse weighting adjustment                 |      | 153 |
| 12.4 Calibration weighting for nonresponse adjustment |      | 156 |
| Bibliography                                          | 159  |     |

__
l_
l l

## Introduction 1.1 Introduction

Suppose that we are interested in obtaining the employment rate of the US
population in a certain time. In this case, we can think of two **ways to obtain** the employment rate. One is to measure the employment status **for every** individual in the population and then take the mean of the measurement in the population. The other is to sample a subset of the population and then use the average employment status of the sample as an estimate for the employment status of the population. The former method is called census, and the latter is called sample survey. Roughly speaking, the census may obtain an accurate figure of the true employment rate, but the cost for census can be enormous. On the other hand, the sample survey can reduce the **cost greatly,** but the sample estimate can be quite different from the true population values.

In this simple example, the true employment rate of the target population is called a parameter. From the sample survey, we obtain an estimate of the parameter. There are many different ways of obtaining samples from the same population. Thus, finding the best sample (and the corresponding estimator) is one of the main goals of survey sampling.

Sample survey has the following advantages over the census:

1 1. It reduces the cost significantly. 2. It takes much less time. Thus, we can obtain information about the population in a timely manner.

3. Because we employ more trained interviewers in survey sampling, it can produce more accurate estimates.

4. Sometimes, it is the only way to get information about the target population.
The third point may sound strange, but it is often true in practice because the census may have larger non-sampling errors than the sample surveys. Because the sample survey is based only on a subset of the finite population, there is always a danger of failing to represent the population properly. The representativeness of a sample is a concept that roughly describes whether the sample can be treated as a miniature of the finite population (Kruskal and Mosteller, 1979). A representative sample can give the most **of the pictures**
1 of the finite population in a cost-effective way. When we use a subset of the population to make inferences about the population, the sample estimate can be different from the parameter to some extent. The sampling error of an estimator is the difference between the estimator and the parameter. We can reduce the sampling error in two aspects. One is to use a suitable sampling rule and the other is to use enough sample size. Note that the sampling error of an estimator ˆθ **can be written as**

$$\begin{array}{r c l}{{\hat{\theta}-\theta}}&{{=}}&{{\{\hat{\theta}-E(\hat{\theta})\}+\{E(\hat{\theta})-\theta\}.}}\end{array}$$
ˆθ)−θ}. **(1.1)**
The first term, ˆθ−E(
ˆθ), can be called the variation of ˆθ **and the second term,**
E(
ˆθ) − θ, is called the bias of ˆθ**. Increasing the sample size will reduce the**
absolute value of the variation part and using a sampling rule that guarantees unbiasedness will make the second part equal to zero.

The accuracy of an estimator is often measured by mean squared errors, which is give by

$$MSE(\hat{\theta})\equiv E\left\{(\hat{\theta}-\theta)^{2}\right\}\tag{1.2}$$ $$=\left\{Bias(\hat{\theta})\right\}^{2}+V(\hat{\theta}).$$
$$(1.1)$$

By employing a probability sampling design, we can make *Bias*(
ˆθ**) = 0. By**
increasing the sample size, we can make the variance smaller. Probability sampling will be introduced in the next section.

## 1.2 Probability Sample

Probability sampling refers to a set of sampling methods in which the selection probability in each element in the population is known and strictly positive. For example, simple random sampling assigns equal probability of selection to each element of the population. In this case, the selected sample is obtained objectively and does not involve subjective human selection. There are many different ways of obtaining probability samples, and the choice depends on the objective of the study, the cost, and the prior information available in the sampling frame. The following simple example will illustrate the basic idea.

Example 1.1. **Suppose that there are four farms in a town. The finite population consists of 4 farms in Table 1.1 and we are interested in estimating the**
average crop yield in the population. Here, the farm acreage **is the auxiliary**
information that is available in advance and the crop yield is the item of interest in the study. Suppose further that, due to the cost restriction, we want to select only n = 2 farms and estimate the average crop yield from the sample. Probability sample 3

Farm acreage and crop yield

| ID   | Acreage   | Yield (y)   |
|------|-----------|-------------|
| 1    | 4         | 1           |
| 2    | 6         | 3           |
| 3    | 6         | 5           |
| 4    | 20        | 15          |

In this case, there are six ways to select a sample of size n = 2 *from the finite* population of size N = 4**. Among the six possible samples, we select one sample and measure the crop yields from the sample. In probability sampling, we**
can select one sample randomly from the six possible samples. Here, "random" sampling means that the sample selection is determined solely by the random number generated for the sample selection, without involving any subjective human decision. To select a sample randomly, the selection probability is assigned in advance for each possible sample. Once the selection probability is assigned to each sample, the final sample is selected using a random number generated from a random-number-generating mechanism.

When selecting a sample from a finite population, there is a finite number of possible samples, and the probability distribution of the sample can be treated as a probability distribution for a discrete random variable. In this case, the probability distribution of a sample consists of all possible samples and their selection probabilities. The selection probabilities must be sum to one. Simple random sampling refers to the sampling mechanism where the selection probabilities are all equal for samples with the same sample size. **Table 1.2 shows the**
probability distribution of the sample under simple random *sampling using the* example in Table 1.1. Since there are 6 possible samples of size n = 2 **from the** population of size N = 4, the selection probabilities are all equal to 1/6**. The**
probability distribution of the sample is simply called the *sample distribution.*

Sample distribution under simple random sampling

| Sample ID   | Selection probability   |
|-------------|-------------------------|
| 1, 2        | 1/6                     |
| 1, 3        | 1/6                     |
| 1, 4        | 1/6                     |
| 2, 3        | 1/6                     |
| 2, 4        | 1/6                     |
| 3, 4        | 1/6                     |

Determining the sample distribution is equivalent to determining the sampling mechanism, the probability mechanism for sample selection. Sampling design refers to the process of determining the sampling mechanism. Form the sample distribution, we can use a random number to select a sample. For example, in Table 1.2, if the random number is 0.4 then {1,4} *is selected because* 0.4 is greater than 2/6 and less than 3/6.

Note that we can compute an estimator from the sample observations. For example, sample mean can be computed from each sample. Thus, **we can the**
sampling distribution of the sample mean from the sample distribution. Probability distribution of an estimator consists of all possible values of the estimator and their probabilities. The possible value of an estimator can be computed from the observed values in the sample. Thus, sampling distribution of an estimator is induced from the sample distribution, the probability distribution of the sample. Table 1.3 presents the sampling distribution of **the sample mean**
under the simple random sampling given by Table 1.2. From the sampling distribution table, the sample mean y¯ *is distributed as a discrete random variable* taking values on 2,3,4,8,9,10, with equal probability. Thus, we have E(¯y**) = 6**
which is equal to the population mean. Under the sampling distribution in Table 1.3, the expectation of the sample mean is equal to the population mean.

That is, sample mean is unbiased for the population mean under simple random sampling.

| Sample ID   | y value   | Sample mean (¯y)   | Selection probability   |
|-------------|-----------|--------------------|-------------------------|
| 1, 2        | 1, 3      | 2                  | 1/6                     |
| 1, 3        | 1, 5      | 3                  | 1/6                     |
| 1, 4        | 1, 15     | 8                  | 1/6                     |
| 2, 3        | 3, 5      | 4                  | 1/6                     |
| 2, 4        | 3, 15     | 9                  | 1/6                     |
| 3, 4        | 5, 15     | 10                 | 1/6                     |

Sampling distribution of sample mean under simple random sampling Unbiasedness of an estimator is a desirable property but it does not mean that your estimator in a particular sample is close to the true parameter. In the example above, if sample {1,2} **is selected, your estimate of the population**
mean is 2, which is much smaller than the truth (=6). That is, unbiasedness does not imply accuracy.

How to improve the accuracy of an estimator? One way is to increase the sample size. By increasing the sample size, the variance is reduced. If the estimator is unbiased, smaller variance means smaller mean **squared error and** it means high accuracy. Another way of improving accuracy is **to use more**
efficient sampling designs. Making an efficient sampling design by properly

## Probability Sample 5

incorporating the auxiliary information of the sampling frame is one of the main topics in survey sampling. Example 1.2 will provide an illustration for an efficient sampling design.

One thing to note from the above example is that the basis for inference is with respect to the sampling mechanism and has nothing to do with the actual value of yi **in the population. That is, the reference distribution in computing the expectation of an estimator is the probability mechanism generated**
by a repeated application of the sampling design. This approach is called the design-based approach because the sampling design is used mainly to make statistical inferences about the population, treating yi **as fixed. On the other**
hand, the model-based approach refers to an alternative approach to inferring a finite population by making model assumptions about yi **in the population.**
In survey sampling, the design-based approach is more popular because it does not rely on model assumptions, which can be difficult to verify in practice. Also, design-based approach avoids the danger of human subjectivity in sample selection, which is an important issue in government **official statistics.**
Example 1.2. *Consider the simple farm example in Example 1.1 and consider the following alternative sampling mechanism.*

An alternative sample distribution

| Sample ID   | Selection probability   |
|-------------|-------------------------|
| 1, 4        | 1/3                     |
| 2, 4        | 1/3                     |
| 3, 4        | 1/3                     |

In this new sampling design, farm unit 4 is selected with certainty, and one of the other three farms is selected with equal probability. *Table 1.5 gives the* sampling distribution of the mean estimator under this alternative sampling design.

Sampling distribution of the mean estimator under the alternative sampling design

| Sample ID   | y value   | mean estimator   | selection probability   |
|-------------|-----------|------------------|-------------------------|
| 1, 4        | 1, 15     | 4.5              | 1/3                     |
| 2, 4        | 3, 15     | 6                | 1/3                     |
| 3, 4        | 5, 15     | 7.5              | 1/3                     |

Table 1.5 shows the sampling distribution of the mean estimator under the alternative sampling design in Table 1.4. Note that each sample has observation {yk,y4}, k = 1,2,3 *and the mean estimator takes the form of* (3yk +y4)/4 because one selected yk represents three elements {y1,y2,y3} and y4 *represents* itself only. The new sampling design still provides unbiased estimation as the expectation of the mean estimator is equal to 6. However, the *variance of the* mean estimator is now 1.5, which is much lower than the variance 9.67 under simple random sampling.

As can be seen in Table 1.5, the alternative sampling design significantly reduces the sampling variance without increasing the sample size. Efficient sampling design can improve the accuracy of an estimator without increasing the sample size.

## 1.3 Basic Procedures For Survey Sampling

Survey sampling is developed to collect information about characteristics of interest from a subset of the population to build a database for analytical or descriptive purposes. The manual "Survey Methods and Practice", published by Statistics Canada (2003), provides an excellent summary of the basic procedures for sample surveys in government agencies. The life **of a survey can**
be broken down into several phases. The first is the planning phase, which is followed by the design and development phase, and then the implementation phase. Finally, the entire survey process is reviewed and evaluated. The phases of the life of a survey are described below.

## 1.3.1 Survey Planning

Survey planning is the first step in any survey sampling procedure. In the preliminary planning stage, those who are considering a sample survey should formulate the objectives of the proposed survey. The objective should include the specification of the information to be gathered and the determination of the target population, to which the findings of the survey will be extrapolated. Once a survey proposal is formulated, it is important to determine whether a new survey is necessary, considering costs and other practical constraints in conducting a new survey. Sometimes, the goal can be achieved by adding equations to an existing survey's questionnaire or by redesigning an existing survey.

If it is decided to conduct a new survey, the planning team may **proceed**
to formulate the statement of objectives and develop some appreciation of the frame options, the general sample size, the precision requirement, the data collection options and the cost. More discussion of the items in the Statement of Objectives is beyond the scope of this textbook. See Chapter 2 of Statistics Canada (2003) for more details.

The selection of a sampling frame is also an important part in **survey planning. The sampling frame ultimately defines the population to be surveyed,**
which may be different from the target population to which the **Statement** of Objective refers. In order to define the target population, the statistical agency begins with a conceptual population for which no actual list may exist. For example, the conceptual population may be all farmers. To define the target population, "farmers" must be defined. The target population is the population for which information is desired to apply. On the **other hand, the** survey population is the population that is *actually* **covered by the survey.**
The survey frame (or sampling frame) is a realized list of the **survey population. For example, in the survey of household and expenditures in the US, the**
target population is the entire resident population of the US on a particular reference date. However, in reality, we do not have addresses for those living in institutions or living without fixed addresses. Thus, the **survey population** excludes those residents in the US on the same reference date.

## 1.3.2 Design And Development

A subset of the survey population is selected from the sampling frame to collect the information we are interested in. Probability sampling, which is the main topic of this book, will be used to obtain a representative sample of the population. There are several different ways to select **a probability**
sample. The choice of the sampling design depends on several **factors such as** the availability of the sampling frame, the heterogeneity of the study variable, the target precision and the cost of the survey measurements. For a given population, a balance of sampling error with cost and timeliness is achieved through the choice of design and sample size. A more efficient estimation procedure can also be developed by incorporating the auxiliary information available throughout the finite population.

In addition to the choice of the sampling design and the estimation procedure, there are also choices of measurements to be taken and the procedures for taking these measurements. The subject matter persons, who **will be users of**
the survey data, should provide the primary input to specify **the measurements** that are needed to meet the objective of the study. Once the measurements are specified, the measurement experts (survey methodologists **or psychologists)**
begin designing the questionnaires or forms to be used to obtain the data from the sample individuals. Survey questionnaires may undergo **some pilot survey** and revision before being used in the main survey.

## 1.3.3 Implementation

Having ensured that all systems are in place, the survey can now be launched. This is the implementation phase. Interviewers are trained, the sample is selected, and information is collected, all in a manner established during the development phase. Following these activities, data processing begins. Processing activities include data capture, coding, editing, **and imputation. The** result is a well-structured and complete data set from which **it is possible to**
produce required tabulations and to analyze survey results. The confidentiality of these results is then checked and distributed. At each **step, data quality**
must be measured and monitored using methods designed and developed in the previous phase.

## 1.3.4 Survey Evaluation

Once the survey is over, the entire process can be documented **and evaluated. This involves assessments of the methods used, as well as evaluations**
of operational effectiveness and cost performance. These evaluations serve as a test of the suitability of technical practices. They also serve to improve and guide the implementation of specific concepts or components **of methodology** and operations, within and between surveys.

## 1.4 Survey Errors

Estimates obtained from a sample survey can suffer from several sources of errors. The errors of an estimator can be classified into two categories. One is the sampling error, the error due to selecting only a subset of the population, and the other is non-sampling error, the error that can be obtained even under census. Non-sampling errors consist of coverage **error, response** error, measurement error, and processing error, etc. The coverage error occurs when the sampling frame is incomplete in the sense that it does not fully cover the target population. Response error occurs when the **sampled element** does not respond to the survey. Measurement error occurs when there is a discrepancy between the actual value and the reported value **for certain study** items. Measurement error exists when there is misunderstanding of the survey questions, or due to a false answer, or due to interviewer effect. Processing error refers to the errors that occur when transferring the survey answers to the computing process system.

The coverage error, sampling error, and response error are combined to form the non-observation error because the errors are due to **not observing**
the elements in the target population. Measurement error and processing error are combined to form the error of observation because the error occurs even if we observe all elements of the population.

Table 1.6 divides the academic fields related to the sample survey into survey methodology and survey statistics and briefly summarizes the characteristics of each field. As can be seen in this table, survey **methodology is**
mainly dealt with in the Department of Sociology or Psychology as a field of social science, and survey statistics are dealt with in the Department of Statis-

## Survey Errors 9

tics as a branch of statistics. This book will mainly deal with issues related to survey statistics, and Groves et al. (2009) may be cited as **a representative** reference book for survey methodology.

Survey Methodology and Survey Statistics

Survey Methodology **Survey Statistics**

Psychology (Cognitive science), sociology **Statistics**

More interested in non-sampling errors **More interested in sampling errors** By properly asking questions, we can **Measure the uncertainty of survey errors**

reduce survey errors **and incorporate them into inference**

Questionnaire design, Survey management **Sampling design, estimation, imputation etc.**

In general, in order to reduce the coverage error among various nonsampling errors, a good sampling frame should be used. For example, when a yellow book is used to select samples, people who do not have **a landline** phone will not be sampled, so you will have to get another list **to supplement** it. Multi-frame survey, using several sampling frames, can **be considered in**
this case, but then we need to worry about duplication problem.

To reduce nonresponse error, we may need to train the interviewer, publicize the survey, manage the survey target, and give higher incentives to survey participation. The measurement error was determined by the **survey method,**
the sincerity and training level of the interviewer, and the **clarity of the survey questions. Sufficient motivation and training is also required from the**
interviewees.

In general, as the sample size increases, the sampling error **decreases, but**
the non-sampling error becomes more difficult to manage. For example, if the sample size is very large, it becomes difficult to manage interviewers, which increases the risk of non-response errors or measurement errors. Therefore, in addition to cost reduction, conducting a sampling of an appropriate size is very important in that non-sampling error can be reduced.

__
l_
l l

## Horvitz-Thompson Estimation 2.1 Introduction

We will study some theory for unbiased estimation under probability sampling designs. Let U = {1,··· ,N} **be the set of indexes of the target population.**
A probability sample is simply a subset of U, denoted by A ⊂ U**, selected by a** probability rule, called the sampling design. Let A = {A;A ⊂ U} **be the set of**
all possible samples. We have the following formal definition of the sampling distribution.

Definition 2.1. 1. Sampling distribution : probability mass function defined on A. That is, a sampling distribution P(·) *satisfies the* following properties:
(a) P (A) ∈ [0,1], ∀A ∈ A
(b) PA∈A P (A**) = 1**.

2. Random sampling ⇐⇒ P(A) < 1, *for all* A ∈ A 3. Purposive sampling ⇐⇒ P(A) = 1 *for some A* ∈ A
If the parameter of interest is a population quantity that can be written as θN = θ (yi; i ∈ U), a statistic is written as ˆθ = ˆθ (yi; i ∈ A**), which means**
that it is a function of yi **in the sample. If the statistic is used to estimate** θN ,
then it becomes an estimator. The sampling distribution of an estimator is obtained from the sample distribution. That is, as discussed in Section 1.2, the probability mass function P(A) applied to obtain A **is then used to represent**
P{
ˆθ = ˆθ (yi; i ∈ A)}**, the probability distribution or the sampling distribution**
of ˆθ**. Using the sampling distribution of the estimator, we can also compute**
the expectation and variance of the estimator. Definition 2.2.

For parameter θN *, let* ˆθ (A) = ˆθ (yi; i ∈ A) **be an estimator of** θN .

1. Expectation : E(
ˆθ) = PA∈A P (A)
ˆθ (A)
2. Variance: V (
ˆθ) = PA∈A P (A)
nˆθ (A)−E
ˆθ o2 3. Mean squared error : MSE(ˆθ) = PA∈A P(A)
nˆθ (A)−θN
o2 2 11

## 12 **Horvitz-Thompson Estimation**

Here, the expectation is taken with respect to the sampling design induced by the probability rule for A, treating {y1,y2,··· ,yN } **as fixed. As discussed in**
Chapter 1, the difference between E(
ˆθ) and θN **is called bias and an estimator**
is called an unbiased estimator when its bias is zero. When an **estimator has** high precision, it means that its variance is small, but it does not necessarily mean that its accuracy is high. The accuracy of an estimator is related to the small mean squared error of the estimator.

## 2.2 Horvitz-Thompson Estimation

Does an unbiased estimator always exist for all probability **sampling designs? To answer this question, we need the following definition of inclusion**
probabilities.

## Definition 2.3.

1. First-order inclusion probability:

$$\pi_{i}=P r\left(i\in A\right)=\sum_{A;\ i\in A}P\left(A\right)$$

2. Second-order inclusion probability, or joint inclusion *probability:*

$$\pi_{i j}=P r\left(i,j\in A\right)=\sum_{A;\ i,j\in A}P\left(A\right)$$
 *3. Probability sampling design: $\pi_i>0,\quad\forall i\in U$.*  . 
4. Measurable sampling design : πij > 0 ∀*i, j* ∈ U.

That is, the first-order inclusion probability πi **refers to the probability**
that the unit i is included in the sample. Furthermore, the second-order inclusion probability πij refers to the probability that both units, unit i and unit j, are included in the sample. Note that πii = πi **by definition. Probability sampling design is a sampling design in which all first-order inclusion**
probabilities are strictly greater than zero. Probability **sampling design is a**
sufficient condition for the existence of a design-unbiased estimator of the population total. Measurable sampling design is a sampling design in which all second-order inclusion probabilities are strictly greater than zero. Measurable sampling design is a sufficient condition for the existence of **a design unbiased** estimator of sampling variance of an unbiased estimator.

The following lemma presents some algebraic properties of the inclusion probabilities. Horvitz-Thompson estimation 13 Lemma 2.1. *The first order inclusion probabilities satisfy*

$$\sum_{i=1}^{N}\pi_{i}=n$$
$$(2.1)$$
πi = n **(2.1)**
where n *is the sample size. If the sampling design is a fixed-size sampling* design such that V (n**) = 0**,

$$\sum_{i=1}^{N}\pi_{i j}=n\pi_{j}\tag{1}$$
$$(2.2)$$

Proof. Given the sample index set A**, define the following indicator function**

$$I_{i}={\left\{\begin{array}{l l}{1}&{{\mathrm{if~}}i\in A}\\ {0}&{{\mathrm{if~}}i\notin A.}\end{array}\right.}\tag{1}$$

In this case, Ii is a random variable with E (Ii) = πi and E (IiIj ) = πij**. Furthermore, by the definition of sample size** n,

$$(2.3)$$
$$\sum_{i=1}^{N}I_{i}=n.$$
$$(2.4)$$

Thus, taking expectations of both sides of (2.4), we can obtain (2.1). Also, multiplying both sides of (2.4) and taking the expectations **again, we obtain** (2.2).

When the sample is obtained from a probability sampling design, an unbiased estimator for the total Y =PN
i=1 yi **is given by**

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i\in A}{\frac{y_{i}}{\pi_{i}}}.$$
$$(2.5)$$

This is often called Horvitz-Thompson (HT) estimator, which is originally discussed by Horvitz and Thompson (1952) and also by Narain (1951).

The following theorem presents the basic statistical properties of the HT
estimator.

Theorem 2.1. *The Horvitz-Thompson estimator, given by (2.5), satisfies the* following properties:

$$E\left({\hat{Y}}_{\mathrm{HT}}\right)=Y$$ $$V\left({\hat{Y}}_{\mathrm{HT}}\right)=\sum_{i=1}^{N}\sum_{j=1}^{N}\left(\pi_{i j}-\pi_{i}\pi_{j}\right)\frac{y_{i}}{\pi_{i}}\frac{y_{j}}{\pi_{j}}$$
$$(2.6)$$  $$(2.7)$$

Furthermore, for a fixed-size sampling design (i.e., V (n) = 0*), we have*

$$V\left(\hat{Y}_{\rm HT}\right)=-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}\left(\pi_{ij}-\pi_{i}\pi_{j}\right)\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}.\tag{2.8}$$

14 **Horvitz-Thompson estimation**
Proof. Using the sample indicator function Ii **defined in (2.3), the HT estimator can be written as**

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i=1}^{N}{\frac{y_{i}}{\pi_{i}}}I_{i}.$$
N
Treating {y1,y2,··· ,yN } **as fixed and taking expectations with respect to** Ii, we have

$$\begin{array}{r c l}{{E\left({\hat{Y}}_{\mathrm{HT}}\right)}}&{{=}}&{{\sum_{i=1}^{N}{\frac{y_{i}}{\pi_{i}}}E\left(I_{i}\right)}}\\ {{}}&{{=}}&{{\sum_{i=1}^{N}{\frac{y_{i}}{\pi_{i}}}\pi_{i}=Y}}\end{array}$$

which shows (2.6). Similarly, we have

$$\begin{array}{r c l}{{V\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{\sum_{i=1}^{N}\sum_{j=1}^{N}\frac{y_{i}}{\pi_{i}}\frac{y_{j}}{\pi_{j}}C o v\left(I_{i},I_{j}\right)}}\\ {{}}&{{=}}&{{\sum_{i=1}^{N}\sum_{j=1}^{N}\frac{y_{i}}{\pi_{i}}\frac{y_{j}}{\pi_{j}}\left(\pi_{i j}-\pi_{i}\pi_{j}\right)}}\end{array}$$

and (2.7) is proved. To show (2.8), define ∆ij = πij −πiπj **and express (2.8)**
as

$$-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}\Delta_{ij}\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}=-\sum_{i=1}^{N}\sum_{j=1}^{N}\Delta_{ij}\left(\frac{y_{i}}{\pi_{i}}\right)^{2}+\sum_{i=1}^{N}\sum_{j=1}^{N}\Delta_{ij}\frac{y_{i}}{\pi_{i}}\frac{y_{j}}{\pi_{j}}.\tag{2.9}$$

Now, using (2.2) and (2.1), we have

$$\sum_{j=1}^{N}\Delta_{i j}=\sum_{i=1}^{N}\pi_{i j}-\sum_{i=1}^{N}\pi_{i}\pi_{j}=n\pi_{i}-n\pi_{i}=0.$$

Thus, the first term on the right side of the equality in (2.9) becomes zero and (2.8) is established.

Example 2.1. Let U = {1,2,3} **be the target population and consider the**
following sampling design.

$$P\left(A\right)={\left\{\begin{array}{l l}{0.5}&{{\mathrm{~if~}}A=\left\{1,2\right\}}\\ {0.25}&{{\mathrm{~if~}}A=\left\{1,3\right\}}\\ {0.25}&{{\mathrm{~if~}}A=\left\{2,3\right\}}\end{array}\right.}$$

In this case, we have π1 = 0.5 + 0.25 = 0.75, π2 = 0.5 + 0.25 = 0.75*, and* π3 =
0.25 + 0.25 = 0.5*. Thus, the HT estimator for the total is then*

$${\hat{Y}}_{H T}={\left\{\begin{array}{l l}{y_{1}/0.75+y_{2}/0.75}\\ {y_{1}/0.75+y_{3}/0.5}\\ {y_{2}/0.75+y_{3}/0.5}\end{array}\right.}$$
$$\begin{array}{l}{{\mathit{i f}\ A=\{1,2\}}}\\ {{\mathit{i f}\ A=\{1,3\}}}\\ {{\mathit{i f}\ A=\{2,3\}}}\end{array}$$
y1/0.**75 +**y2/0.75 if A = {1,2}
y1/0.**75 +**y3/0.5 if A = {1,3}
y2/0.75 +y3/0.5 if A = {2,3}
Horvitz-Thompson estimation 15 Therefore,

$$\begin{array}{r c l}{{E\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{0.5\left(y_{1}/0.75+y_{2}/0.75\right)+0.25\left(y_{1}/0.75+y_{3}/0.5\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{+}}&{{0.25\left(y_{2}/0.75+y_{3}/0.5\right)=y_{1}+y_{2}+y_{3}}}\end{array}$$

and the HT estimator is unbiased for the population total.

The HT estimator provides an unbiased estimate under probability sampling. If πi > **0 does not hold for some elements of the population, the HT**
estimator cannot be used. Also, the HT estimator is not location-scale invariant. That is, for any constants a and b,

$${\frac{1}{N}}\sum_{i\in A}{\frac{a+b y_{i}}{\pi_{i}}}\neq a+b{\frac{1}{N}}\sum_{i\in A}{\frac{y_{i}}{\pi_{i}}}.$$

The variance formula (2.8) was independently discovered by **Sen (1953) and**
Yates and Grundy (1953). Thus, it is often called the Sen-Yates-Grundy(SYG)
variance formula. The variance will be minimized when πi ∝ yi**. That is, if**
the first-order inclusion probability is proportional to yi**, the resulting HT**
estimator under this sampling design will have zero variance. However, in practice, we cannot construct such a design because we do not **know the value**
of yi in the design stage. If there is an auxiliary variable xi **available in the** sample frame and xi is believed to be closely related to yi**, then a sampling**
design with πi ∝ xi **can lead to a very efficient sampling design.**
Now, we discuss an unbiased estimate of the variance of the HT **estimator.**
The variance formula in (2.7) or (2.8) is a population quantity and must be estimated from the sample. Generally speaking, the variance formula is a quadratic function of yi**'s in the population. Thus, to estimate the variance,** we need to assume a measurable sampling design that satisfies πij > **0 for all**
i and j**. That is, if the parameter of interest is of the form**

$$Q=\sum_{i=1}^{N}\sum_{j=1}^{N}q(y_{i},y_{j})$$
$$(2.10)$$
$$(2.11)$$

then, under measurable sampling design, an unbiased estimator of Q is

$$\hat{Q}=\sum_{i\in A}\sum_{j\in A}\frac{1}{\pi_{i j}}\;q\left(y_{i},y_{j}\right).$$
Thus, an $\mathfrak{un}$
Thus, an unbiased estimator of variance in (2.7) is

$${\hat{V}}\left({\hat{Y}}_{\mathrm{HT}}\right)=\sum_{i\in A}\sum_{j\in A}{\frac{\pi_{i j}-\pi_{i}\pi_{j}}{\pi_{i j}}}{\frac{y_{i}}{\pi_{i}}}{\frac{y_{j}}{\pi_{j}}}.$$
. **(2.11)**
Also, for fixed-sized designs, an unbiased estimator of the SYG variance formula is

$$\hat{V}\left(\hat{Y}_{\rm HT}\right)=-\frac{1}{2}\sum_{i\in A}\sum_{j\in A}\frac{\pi_{ij}-\pi_{i}\pi_{j}}{\pi_{ij}}\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}.\tag{2.12}$$

16 *Horvitz-Thompson estimation* Another statistical property of the HT estimator is consistency and asymptotic normality, which are established for sufficiently large sample sizes. For an infinite population, the consistency of the sample mean means that the sample mean converges to the population mean in probability. That is, the probability that the absolute difference between the sample **mean and the** population mean is greater than a given threshold (ǫ**) goes to zero as the** sample size increases. That is, for any ǫ > 0,

$$P r\left(\left|{\bar{y}}_{n}-{\bar{Y}}_{N}\right|>\epsilon\right)\to0\quad{\mathrm{as~}}n\to\infty.$$

In the finite population setup, the finite population is conceptualized to be a sequence of finite population with size N **also increasing. The HT estimator** of the finite population mean is given by

$${\bar{Y}}_{\mathrm{HT}}={\frac{1}{N}}{\hat{Y}}_{\mathrm{HT}}$$

and, using Chebyshev inequality,

$$P r\left(\left|\bar{Y}_{\mathrm{HT}}-\bar{Y}_{N}\right|>\epsilon\right)\leq\epsilon^{-2}V\left(\bar{Y}_{\mathrm{HT}}\right).$$
Thus, as long as $\frac{1}{2}$
$\lim\limits_{n\rightarrow\infty}V\left(\tilde{Y}_{\rm HT}\right)=0$, (2.13)
the consistency of HT estimator follows. For example, under **the simple random sampling that we will study in Chapter 3, we have**

$$V\left(\bar{Y}_{\mathrm{HT}}\right)=\frac{1}{n}\left(1-\frac{n}{N}\right)S^{2}.$$

Thus, as long as S
2**is bounded above in probability, condition (2.13) holds**
and the consistency of the HT estimator follows.

Asymptotic normality is also an important property for obtaining confidence intervals or performing hypothesis testing from the sample. Under some regularity conditions, we can establish

$${\frac{{\hat{Y}}_{\mathrm{HT}}-Y}{\sqrt{{\hat{V}}\left({\hat{Y}}_{\mathrm{HT}}\right)}}}\;{\xrightarrow{\mathcal{L}}}\;N\left(0,1\right)$$

for most sampling designs, where L
−→ **denotes convergence in probability.**
Thus, in this case, the 95% confidence interval for the population total is computed by

$$\left({\hat{Y}}_{\mathrm{HT}}-1.96{\sqrt{{\hat{V}}\left({\hat{Y}}_{\mathrm{HT}}\right)}},\quad{\hat{Y}}_{\mathrm{HT}}+1.96{\sqrt{{\hat{V}}\left({\hat{Y}}_{\mathrm{HT}}\right)}}\right).$$

A more in-depth discussion of the asymptotic normality of the HT estimator can be found in Chapter 1 of Fuller (2009).

## 2.3 Other Parameters

In the previous section, we have studied the estimation of the total of the finite population, Y =PN
i=1 yi**. In many practical situations, we estimate**
other parameters such as population quantiles or domain totals. For example, one may be interested in estimating certain characteristics (such as household income) for a certain age group (for example, over 60) of the householder. At the time of sampling, we do not know the age of the householders. In this case, one can select a sample from the household population and obtain information about the age and income in the sampled households. Let zi = 1 if i **belongs** to the particular age group of interest and zi = 0 otherwise. Also, let yi **be the**
value of the study variable (income in this example) for the element i**. The** domain mean of y **can be written as**

$$\theta_{d}=\frac{\sum_{i=1}^{N}z_{i}y_{i}}{\sum_{i=1}^{N}z_{i}}.\tag{2.14}$$

The indicator variable z is used to identify the domain inclusion in the population. If zi = 1, then the unit i **is eligible for domain estimation.**
From (2.14), we can express the domain mean as a ratio of two totals.

That is, θd = Yd/D **where** Yd =PN
i=1 ziyi, D =PN
i=1 zi**. A natural estimator**
of θd is

$${\hat{\theta}}_{d}={\frac{\sum_{i\in A}z_{i}y_{i}/\pi_{i}}{\sum_{i\in A}z_{i}/\pi_{i}}},$$

which is the ratio of two corresponding HT estimators. That is, ˆθd =
Yˆd,HT/Dˆ HT **is a special case of the ratio estimator we will study in Chapter 7. Generally speaking, the ratio estimator is not exactly unbiased, but its**
relative bias can be asymptotically negligible.

In addition to domain estimation, we are often interested in **estimating**
the population distribution. Suppose, for example, that we **are interested in** estimating the proportion of the population below a certain **poverty level.**
In this case, θp = N −1PN
i=1 I(yi < c**) is the parameter of interest, where** c is the threshold for the poverty of the household. We can use the theory of HT estimation to estimate θp by ˆθp,HT = N −1Pi∈A π
−1 iI(yi < c**). If** N is unknown, we use its HT estimator NˆHT =Pi∈A π
−1 i**. Using this idea, we can**
estimate the entire cumulative distribution function of the population, given by

$$F(y)={\frac{1}{N}}\sum_{i=1}^{N}I(y_{i}\leq y).$$
That is, we can use $\frac{1}{2}$
$${\hat{F}}(y)={\frac{1}{\sum_{i\in A}\pi_{i}^{-1}}}\sum_{i\in A}\pi_{i}^{-1}I(y_{i}\leq y).$$

18 *Horvitz-Thompson estimation* Using Fˆ(y**), we can also perform a quantile estimation. We can define the**
q% quantile (0 *< q <* 1) of the population as θq = inf{y;F(y) ≥ q}**. Its HT**
estimator can be written as ˆθq **= inf**{y;Fˆ(y) ≥ q}.

Many population parameters can be written as the solution to **the population estimating equation**

$\sum U(\theta;y_{i})=0$ (2.15)
for some estimating function U(θ;yi). For example, the 100×q**% quantile can**
be defined as U(θ;y) = I(*y < θ*)−q**. To estimate the parameter defined as the**
solution to

$$\sum_{i=1}^{N}U(\theta;y_{i})=0,$$

one can use the HT estimation idea to get

$$\sum_{i\in A}\pi_{i}^{-1}U(\theta;y_{i})=0$$
$$\begin{array}{r}{(2.16)}\end{array}$$
i U(θ;yi**) = 0 (2.16)**
as the estimating equation for θN **defined through (2.15). Binder (1983) investigated the asymptotic properties of the estimator of the form in (2.16).**

## 2.4 Discussion

In probability sampling, the HT estimator is regarded a gold **standard**
estimator because of its design-unbiasedness. One may wonder whether there is another method to consider. To investigate this, let us consider the following weighted estimator.
$${\hat{Y}}_{w}=\sum_{i\in A}w_{i}y_{i}$$
wiyi **(2.17)**
where wi is the fixed weight assigned to unit i**. The design-expectation of** Yˆw is

$$E({\hat{Y}}_{w})=\sum_{i=1}^{N}\pi_{i}w_{i}y_{i}\tag{1}$$
$$(2.17)^{\frac{1}{2}}$$
$$(2.18)$$

where π is the first-order inclusion probability of unit i**. To obtain unbiasedness, we require** PN
i=1 πiwiyi =PN
i=1 yi for all yi **in the population, which**
leads to wi = π
−1 i.

Now, suppose that we relax wi = π
−1 i**and only require** PN
i=1 πiwi = N. In Discussion 19

this case, the bias of $\hat{Y}_w$ is ... 
, the bias of $Y_{w}$ is  $$\begin{array}{rcl}\mbox{\it Bias}(\hat{Y}_{w})&=&\sum_{i=1}^{N}\pi_{i}w_{i}y_{i}-\sum_{i=1}^{N}y_{i}\\ &=&\sum_{i=1}^{N}\pi_{i}w_{i}y_{i}-N^{-1}\left(\sum_{i=1}^{N}\pi_{i}w_{i}\right)\left(\sum_{i=1}^{N}y_{i}\right)\\ &=&N\times\mbox{\it Cov}(q_{i},y_{i}),\end{array}$$
where qi = πiwi and

$$C o v(q_{i},y_{i})={\frac{1}{N}}\sum_{i=1}^{N}\left(q_{i}-{\bar{q}}_{N}\right)\left(y_{i}-{\bar{y}}_{N}\right)$$

is the population covariance between qi and yi**, using an operator notation.**
Thus, ¯qN = N −1PN
i=1 qi **= 1, we can express**

$$\frac{B i a s(\hat{Y}_{w})}{Y}\;\;=\;\;\;C o v(q_{i},y_{i})/\bar{y}_{N}$$
$=\quad\;\;Corr(q_i,y_i)\times CV(q_i)\times CV(y_i).$  . 
Note the HT estimator uses qi = 1 which leads to *Corr*(qi ,yi**) = 0 and** CV (qi) = 0. Other estimators can also achieve zero bias if *Corr*(qi,yi**) = 0.**
For example, if wi = N/n and yi is completely independent of πi**, then the**
bias of Yˆw **is also zero.**
Another class of unbiased estimator is the difference estimator of the form

$$\hat{Y}_{\rm diff}=X+\sum_{i\in A}\frac{1}{\pi_{i}}(y_{i}-x_{i}),\tag{2.19}$$

where X =PN
i=1 xi is the population total of xi**. The difference estimator is**
popular in accounting, where yi is the audit value and xi **is the book value for**
the reporting unit i**. More discussion of the difference estimator will be given** in Chapter 8.

__
l_
l l

## Simple And Systematic Sampling Designs 3.1 Introduction

Before selecting the sample, the population must be divided **into parts**
that are called *sampling units*, or *units***. These units must cover the whole** population, and they must not overlap in the sense that every **element in the** population belongs to one and only one unit. Sometimes, the appropriate unit is obvious, as in a population of light bulb, in which the unit **is the single** bulb. Sometimes there is a choice of unit. When sampling people in a town, the unit might be an individual person, the members of a family, or all persons living in the same city block. In sampling an agricultural crop, the unit might be a field, a farm, or an area of land whose shape and dimensions **are at our** disposal.

The construction of this list of sampling units, called a sampling *frame*,
is often one of the main practical problems. We use the term direct element sampling to denote sample selection from a frame that directly identifies the individual elements of the population of interest. That is, **in element sampling,**
the sampling unit is equal to the reporting unit. A selection **of elements can** take place directly from the frame. In this chapter, we first consider a simple type of sampling design in which the first-order inclusion probabilities are equal for every element in the population.

## 3.2 Simple Random Sampling

Consider the problem of selecting n **units from a finite population of size**
N**. There are** N
n
**possible samples in this case and the simplest way to select**
a sample is to select one randomly, that is, to select one realization at random with equal probability. This sampling design is called simple random sampling (SRS) without replacement , or simple random sampling. The sample distribution of the SRS of size n **is given by**

$$P(A)={\begin{cases}{\binom{N}{n}}^{-1}&{\mathrm{if}}\quad\left|A\right|=n\\ 0&{\mathrm{otherwise.}}\end{cases}}$$
$$(3.1)$$

3 22 *Simple and systematic sampling designs* From (3.1), we can obtain the first-order inclusion probability as

$$\pi_{i}$$
$ =\quad P(i\in A)$  $ =\quad\sum_{\begin{array}{l}A\in\mathcal{A}\\ \\ =\quad\dfrac{{1\choose1}{N-1\choose n-1}}{{N\choose n}}\\ \\ =\quad\dfrac{n}{N}.$  . 
Similarly, we can obtain

$$\pi_{i j}=\begin{cases}N^{-1}n&\quad\text{if}i=j\\ N^{-1}\left(N-1\right)^{-1}n\left(n-1\right)&\text{if}i\neq j.\end{cases}$$
$$(3.2)$$

Thus, the Horvitz-Thompson estimator of the population total Y =PN
i=1 yi can be written

$${\hat{Y}}_{\mathrm{HT}}={\frac{N}{n}}\sum_{i\in A}y_{i}=N{\bar{y}}.$$

and the HT estimator satisfies design-unbiasedness under the SRS design. That is, under SRS, the sample mean (¯y**) is unbiased for the population mean**
Y¯ = N −1PN
i=1 yi**. The sampling variance of the HT estimator is, by (2.8),**

$$V\left(\hat{Y}_{\rm HT}\right)=-\frac{1}{2}\sum_{i=1}^{N}\sum_{\begin{subarray}{c}j\neq i\\ j=1\end{subarray}}^{N}\left(\pi_{ij}-\pi_{i}\pi_{j}\right)\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}$$ $$=\frac{1}{2}\frac{N}{n}\frac{N-n}{N\left(N-1\right)}\sum_{i=1}^{N}\sum_{j=1}^{N}\left(y_{i}-y_{j}\right)^{2}.$$

Since

$$\sum_{i=1}^{N}\sum_{j=1}^{N}\left(y_{i}-y_{j}\right)^{2}=\sum_{i=1}^{N}\sum_{j=1}^{N}\left(y_{i}-\bar{Y}+\bar{Y}-y_{j}\right)^{2}\tag{1}$$ $$=2N\sum_{i=1}^{N}\left(y_{i}-\bar{Y}\right)^{2},$$  ain
$$(3.4)$$

we can obtain

$$\begin{array}{r c l}{{V\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{\frac{N^{2}}{n}\frac{N-n}{N}S^{2}}}\end{array}$$

Simple random sampling 23 where

$$S^{2}=\frac{1}{N-1}\sum_{i=1}^{N}\left(y_{i}-\bar{Y}\right)^{2}$$ $$=\frac{1}{2}\frac{1}{N\left(N-1\right)}\sum_{i=1}^{N}\sum_{j=1}^{N}\left(y_{i}-y_{j}\right)^{2}.$$
$$(3.5)$$

Thus, we can establish

sh $$V\left(\bar{y}_n\right)=\frac{1}{n}\frac{N-n}{N}S^2.$$ of $n=1$, (3.5) becomes _________. 
For the special case of n **= 1, (3.5) becomes**

$${\frac{1}{N}}\sum_{i=1}^{N}\left(y_{i}-{\bar{Y}}\right)^{2},$$

which is often called population variance, denoted by σ 2 y
. That is, σ 2 y can be understood as the sampling variance of the single sample observation under SRS with size n **= 1. Using the population variance, the variance formula in** (2.14) can be written as

$$V\left(\bar{y}_{n}\right)=\frac{1}{n}\left(1-\frac{n-1}{N-1}\right)\sigma_{y}^{2},\tag{3.6}$$

where 1 − (N −1)−1(n−**1) is the variance reduction factor due to withoutreplacement sampling and it is often called FPC (Finite population correction)**
term. The FPC term disappears under simple random sampling with replacement.

Now, consider variance estimation of the HT estimator under **SRS. Since**
SRS is a fixed-sized sampling design, we can use SYG variance estimation formula in (2.12) to get

$$\begin{array}{r c l}{{\hat{V}\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{-\frac{1}{2}\sum_{i\in A}\sum_{j\in A}\frac{\left(\pi_{i j}-\pi_{i}\pi_{j}\right)}{\pi_{i j}}\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\frac{1}{2}\frac{N}{n}\frac{N-n}{n(n-1)}\sum_{i\in A}\sum_{j\in A}\left(y_{i}-y_{j}\right)^{2}.}}\end{array}$$

Similarly to (3.4), we can show

$$\sum_{i\in A}\sum_{j\in A}\left(y_{i}-y_{j}\right)^{2}=2n\sum_{i\in A}\left(y_{i}-{\bar{y}}\right)^{2}.$$

Thus, we can obtain

$$\begin{array}{r c l}{{\hat{V}\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{\frac{N^{2}}{n}\frac{N-n}{N}s^{2}}}\end{array}$$
$$(3.8)$$
$$24$$

24 *Simple and systematic sampling designs*

where
$$s^{2}={\frac{1}{n-1}}\sum_{i\in A}\left(y_{i}-{\bar{y}}\right)^{2}.$$
$\text{h}$us, under. 
Thus, under SRS, we have
$$E\left(s^{2}\right)=S^{2}.$$
2. **(3.9)**
If y is dichotomous, taking either 1 or 0, the population mean of y **is equal**
to the proportion of y = 1 in the population, namely P = P r (y **= 1). In this** case, we can obtain σ 2 y = P (1−P) and the variance of the HT estimator Pˆ = ¯y of P **is then equal to**

$\left(3.9\right)$ . 
$$V\left({\hat{P}}\right)={\frac{1}{n}}\left(1-{\frac{n}{N}}\right){\frac{N}{N-1}}P\left(1-P\right)$$
and its unbiased estimator is

$${\hat{V}}\left({\hat{P}}\right)={\frac{1}{n-1}}\left(1-{\frac{n}{N}}\right){\hat{P}}\left(1-{\hat{P}}\right).$$

We now discuss the determination of the sample size n under simple random sampling. Under the significant level α**, the margin of error, denoted by**
d**, is defined to satisfy**

$$P r\left\{\left|{\hat{\theta}}-\theta\right|\leq d\right\}=1-\alpha.$$

That is, d is half of the length in the confidence interval for θ**, Thus, solving**

$$z_{\alpha/2}{\sqrt{\frac{1}{n}\left(1-{\frac{n}{N}}\right)S^{2}}}\leq d$$

with respect to n **to get**

$$n\geq\frac{S^{2}}{\left(d/z_{\alpha/2}\right)^{2}+S^{2}/N},$$
$$(3.10)$$

which provide the lower bound of the desired sample size for given d**. However,** since we usually do not know S
2 **before the sample observation, we need an**
estimate for S
2**, from a pilot survey or a similar survey in the same population.**
In many public opinion surveys, y **is a dichotomous variable and the maximum** value of S
2**in this case is 1/4 and (3.10) becomes**

$$n\geq0.25\left({\frac{z_{\alpha/2}}{d}}\right)^{2}.$$
$$(3.11)$$

For α = 0.05, zα/2
.**= 2 and the above inequality reduces to** n ≥ d
−2.

## 3.3 Implementation Of Simple Random Sampling

To implement the SRS method in practice, one may consider a draw-bydraw method as follows: In the first draw, select one element at random from the entire population U with probability 1/N. Let k1 **be the index of the**
element selected from the first draw. In the second draw, select one element at random from U − {k1} with probability 1/(N − 1). Let k2 **be the index**
of the element selected from the second draw. We can continue **the process** until the n-th draw. In the n**-th draw, select one element at random from**
U − {k1,··· , kn−1} with probability (N −n**+ 1)**−1.

In this draw-by-draw procedure, the probability of selecting n **individuals**
k1,··· , kn in order is (N −n)!/N!, and there are n! ways to order {k1,··· , kn}. Thus, the probability of selecting a sample A of n units is n**! times (**N −
n)!/N**!, which is equal to** N
n
−1**. Such a draw-by-draw method may be quite**
cumbersome if N **is very large, as it would require numbering the elements in** the population in advance and then repeating the process n **times.**
Another method of drawing a sample for SRS is the so-called random sorting method. The idea is to sort the population in a random order and then take the first n **units from the ordered population as the final sample. Sunter** (1977) showed that this random sorting method indeed implements simple random sampling. To see this, let ui be the random number for unit i, generated from the U(0,1) distribution. To select a particular sample A = {1,··· ,n}
under the descending order sorting, the largest number among {un+1,··· ,uN } should be less than the smallest number among {u1,··· ,un}.

Let X be the largest number among {un+1,··· ,uN }**. Note that the CDF**
of X is

$$\begin{array}{r c l}{{F(x)}}&{{=}}&{{P(u_{n+1}\leq x,\cdots,u_{N}\leq x)}}\\ {{}}&{{=}}&{{\prod_{i=n+1}^{N}P(u_{i}\leq x)}}\\ {{}}&{{=}}&{{x^{N-n}}}\end{array}$$

for 0 *< x <* 1. The probability of selecting A = {1,··· ,n} **is equal to**

$$P(A)=\int_{0}^{1}\left\{\prod_{i=1}^{n}P(u_{i}>x)\right\}dF(x)$$ $$=\int_{0}^{1}(1-x)^{n}(N-n)x^{N-n-1}dx$$ $$=\frac{n!(N-n)!}{N!}=\frac{1}{\binom{N}{n}}.$$
$A=\{1,\cdots,n\}$ is equal to :  . 
Thus, the random sorting method indeed implements the simple random sampling. The sorting algorithm can be computationally costly if N is large.

26 *Simple and systematic sampling designs* We now consider a different sampling method that does not require reading the population list in advance before sampling. The selection-rejection method allows the selection of SRS in a single pass through the population list, but we need to know the population size N and the sample size n**. The selectionrejection method can be described as follows:**
[Step 0] Start with k **= 1.**
[Step 1] Generate uk ∼ U(0,**1) independently.**

[Step 2] Check if $$u_{k}<\frac{n-\sum_{j=1}^{k-1}I_{j}}{N+1-k}.$$ If yes, select $k+1$ into sample and set $I_{k}=1.$ Otherwise, set $I_{k}=0.$
[Step 3] Set k = k **+ 1. If** Pk j=1 Ij < n **then goto [Step 1]. Otherwise Stop.**
Note that

$$P(k\in A\mid I_{1},\cdots,I_{k-1})={\frac{n-\sum_{j=1}^{k-1}I_{j}}{N+1-k}}$$

for k = 1*,...,N***. Note that** n −Pk−1 j=1 Ij **is the remaining sample size and**
N + 1 − k is the remaining population size at the k**-th pass. Thus, writing**
nk−1 =Pk−1 j=1 Ij ,

$$P(A)=\left[\prod_{k\in A}\frac{n-n_{k-1}}{N-(k-1)}\right]\times\left[\prod_{k\in A^{c}}\left\{1-\frac{n-n_{k-1}}{N-(k-1)}\right\}\right]$$ $$=\left\{\prod_{k=1}^{N}(N-k+1)\right\}^{-1}\left[\prod_{k\in A}(n-n_{k-1})\right]\left[\prod_{k\in A^{c}}(N-k+1-n+n_{k-1})\right]$$ $$=(N!)^{-1}\,n!(N-n)!=\frac{1}{\binom{N}{n}}.$$
$\mathbf{a}=\sum_{k=1}^{k-1}L_k$. 
The selection-rejection method implements simple random sampling, but the population size N **is needed to compute the selection probability.**
McLeod and Bellhouse (1983) proposed a novel method for implementing the SRS in a single pass through the list of records, and does not require a known population size N**. The method is later named the reservoir sampling** method (Vitter, 1985) in the sense that n **sample elements are selected in a** reservoir and then replaced if the next element in the population is selected. In the proposed reservoir method, the first n **elements of the population are**
stored in the reservoir. The k-th element (k = n+ 1,··· ,N**) is selected in the**
reservoir with probability n/k and then one of the n **elements is removed** from the reservoir with equal probability. The elements in the reservoir that remain after the final selection are the elements in the final sample. Note that Simple random sampling with replacement 27 the population size is not necessarily known. You can stop any time point of the process, then you will obtain a simple random sample from the finite population considered up to that time point.

To explain the reservoir sampling, let Uk = {1,2,··· , k} be the finite population up to element k. Let Ak **be the index set of the sample elements selected**
from the reservoir sampling. The probability of selecting element j(< k**) in the** sample can be written as

$$P(j\in A_{k}\mid U_{k})=P(j\in A_{k-1}\mid U_{k-1})P(j\in A_{k}\ \mbox{and}\ k\in A_{k}\mid U_{k},A_{k-1})\tag{3.12}$$ $$+P(j\in A_{k-1}\mid U_{k-1})P(k\notin A_{k}\mid U_{k},A_{k-1}).$$
$$\bar{\ }$$ Now, by the reservoir sampling mechanism, we obtain:
$$P(j\in A_{k}\ \text{and}\ k\in A_{k}\ |\ U_{k},A_{k-1})=P(j\in A_{k}\ |\ U_{k},A_{k-1})P(k\in A_{k}\ |\ U_{k},A_{k-1})$$ $$=\frac{n-1}{n}\times\frac{n}{k}$$  and  $$P(k\notin A_{k}\ |\ U_{k},A_{k-1})=1-\frac{n}{k}.$$  Thus, (3.12) reduces to 
Thus, $\left(3.12\right)$ reduces to ... 
$$P(j\in A_{k}\mid U_{k})=P(j\in A_{k-1}\mid U_{k-1})\times\left(\frac{k-1}{k}\right).\tag{3.13}$$  For $k=n$, $P(j\in A_{k}\mid U_{k})=1$. Thus, by (3.13), we obtain  $$P(j\in A_{k}\mid U_{k})=\frac{n}{k},\tag{3.14}$$  which is equal to the first-inclusion probability of the SRS of size $n$ from the 
finite population of size k.

## 3.4 Simple Random Sampling With Replacement

We now consider the sampling design where the sample of size n **is selected**
with equal probability with replacement. The realized sample size can be smaller than n **because the sample is selected with replacement, and thus**
allows for duplication. In the k-th sample draw, where k = 1,··· ,n, the ith element in the population is selected with probability 1/N. Let z1 **be the**
realized value of yi in the first draw. The probability distribution of z1 **is given**
by

$$z_{1}={\left\{\begin{array}{l l}{y_{1}}\\ {y_{2}}\\ {\vdots}\\ {y_{N}}\end{array}\right.}$$
$$\mathrm{with~probability~}1/N$$ $$\mathrm{with~probability~}1/N.$$

28 *Simple and systematic sampling designs* Similarly, let zk be the realized value of yi in the k-th draw. The withreplacement sampling makes z1,··· ,zn **be independently and identically distributed (IID). The mean and variance of** z1 is

$$\begin{array}{r c l}{{E\left(z_{1}\right)}}&{{=}}&{{N^{-1}\sum_{i=1}^{N}y_{i}=\bar{Y}}}\\ {{}}&{{}}&{{}}\\ {{V\left(z_{1}\right)}}&{{=}}&{{N^{-1}\sum_{i=1}^{N}\left(y_{i}-\bar{y}_{N}\right)^{2}=\sigma_{y}^{2}.}}\end{array}$$
$$\begin{array}{r}{(3.15)}\\ {\ }\end{array}$$  $$\begin{array}{r}{(3.16)}\\ {\ }\end{array}$$
. **(3.16)**
Now, since z1,··· ,zn are IID with mean Y¯ **, we can consider the following class**
of estimators:

$${\hat{\bar{Y}}}_{w}=\sum_{i=1}^{n}w_{i}z_{i}$$
$$(3.17)$$

where Pn i=1 wi **= 1. Note that** Y
ˆ¯w is unbiased regardless of the choice of wi**. To**
find the best choice of wi **in the sense of minimizing its variance, we introduce**
the following lemma.

Lemma 3.1. Let X1,··· ,Xn be n *IID realization with* E(Xi) = µ and V (Xi) =
σ 2 i
. Let w1,··· ,wn *be the fixed constants such that* Pn i=1 wi = 1*. The weighted* estimator µˆw =Pn i=1 wiXi *achieves the minimum at*

$$w_{i}^{*}={\frac{\sigma_{i}^{-2}}{\sum_{k=1}^{n}\sigma_{k}^{-2}}}.$$

Proof. The variance of ˆµw is V (ˆµw) = Pn i=1 w 2 i σ 2 i
. Using Cauchy-Schwarz inequality, we obtain

$2\cdot2\cdot1$ . 
$$\left(\sum_{i=1}^{n}w_{i}^{2}\sigma_{i}^{2}\right)\left(\sum_{i=1}^{n}\sigma_{i}^{-2}\right)\geq\left(\sum_{i=1}^{n}w_{i}\right)^{2}.$$
Since Pn i=1 wi **= 1, we have**

$$\sum_{i=1}^{n}w_{i}^{2}\sigma_{i}^{2}\geq\mathrm{Constant}$$

and the variance is minimized when wiσi ∝ σ
−1 i**, which is equivalent to** wi ∝
σ
−2 i.

Thus, the best linear unbiased estimator of the population mean Y¯ **is the**
sample mean ¯z = n
−1Pn i=1 zi **and its variance is**

$$V\left({\bar{z}}\right)={\frac{1}{n}}\sigma_{y}^{2}$$
$$(3.18)$$

y(3.18)
Bernoulli Sampling 29 The variance formula in (3.6) under SRS is smaller than the variance formula in (3.18) under SRS with replacement. The SRS with replacement is less efficient because the expected value of the actual sample size **is smaller as it** allows for duplication due to with-replacement sampling.

For variance estimation, since z1,··· ,zn **are IID, the sample variance**

$$s_{z}^{2}={\frac{1}{n-1}}\sum_{i=1}^{n}\left(z_{i}-{\bar{z}}\right)^{2}$$

can be used to estimate the population variance. Since z1,z2*,...,z*n **are IID**
with (*Y ,σ* ¯ 2
y
), we have
$E\left(s\hat{z}\right)=\sigma\hat{z}$  . 
2
2
y**(3.19)**
and the variance estimator of ¯z is
$${\bar{z}}\ {\mathrm{i}}s$$
$${\hat{V}}\left({\bar{z}}\right)={\frac{1}{n}}s_{z}^{2}.$$

The SRS with replacement is a special case of the PPS sampling **that will be** covered in Section 5.2.

## 3.5 Bernoulli Sampling

Bernoulli sampling design is a sampling design based on independent Bernoulli trials for the element in the population. That is, **the sample indicator function follows**

$$1,\quad i=1,2,\cdots,N,$$
$\left(3.20\right)^{\frac{1}{2}}$
Ii i.i.d. ∼ Bernoulli(π), i = 1,2,··· ,N, **(3.20)**
where π is the first order inclusion probability for each unit. We can **express**
π = n0/N where n0 **is the expected sample size determined before sample**
selection. In this Bernoulli sampling, the (realized) sample size follows a binomial distribution Bin(N,π**) and the fact that the realized sample size is a**
random variable can reduce the efficiency of the resulting HT estimator.

Under this Bernoulli sampling, the HT estimator of the population mean is

$${\hat{\bar{Y}}}_{\mathrm{HT}}={\frac{1}{N}}\sum_{i\in A}{\frac{y_{i}}{\pi_{i}}}={\frac{n}{n_{0}}}{\bar{y}}.$$

Thus, the HT estimator of the mean is not necessarily equal to **the mean of** the sample. The asymptotic variance of the sample mean is

$$V\left({\bar{y}}\right)={\frac{1}{n_{0}}}\left(1-{\frac{n_{0}}{N}}\right)S^{2}$$
$$(3.21)$$
2(3.21)
30 *Simple and systematic sampling designs* On the other hand, the variance of the HT estimator of the mean is

$$V\left(\widehat{Y}_{\rm HT}\right)=\frac{1}{n_{0}}\left(1-\frac{n_{0}}{N}\right)\frac{1}{N}\sum_{i=1}^{N}y_{i}^{2}\tag{3.22}$$

Thus, the sample mean is more efficient than the HT estimator in **(3.22).**
Example 3.1. **Suppose that we are interested in estimating the proportion**
of students who pass a certain test in a university and there are N=600 of students who took the test in the university. Using a Bernoulli sampling with π = 1/6*, the sample size* n = 90 *is realized. Among the 90 sample students, 60* students are found to have passed. In this case, the HT estimator of the mean is 0.9×2/3, which is different from the actual passing rate 2/3 *in the sample.*
In the extreme case, even if all the students pass the exam, the HT estimate is still 0.9.

If the sampling procedure is such that we repeat the Bernoulli sampling until the realized sample size n is equal to the expected sample size n0**, then** the resulting sampling procedure is exactly equal to the SRS of size n0**. To**
show this result, note that

i=1 Ii = n0 ! = P rI1,I2,··· ,IN ,PN i=1 Ii = n0  P r I1,I2,··· ,IN | X N P r (n = n0). (3.23) Since P r I1,I2,··· ,IN , X N i=1 Ii = n0 ! =  QN i=1 p Ii (1−p) 1−Iiif PN i=1 Ii = n0 0 otherwise = p n0 (1−p) N−n0 if PN i=1 Ii = n0 0 otherwise and P r (n = n0) = N n0 p n0 (1−p) N−n0 ,
the conditional density in (3.23) is equal to the sampling design (3.1) under SRS of size n0.

## 3.6 Systematic Sampling

Systematic sampling is an alternative method of selecting an equal probability sample, but it offers several practical advantages, particularly its simplicity of execution. In systematic sampling, a first element is drawn at random Systematic sampling 31 with equal probability, among the first G **elements in the population list. The** positive integer G is fixed in advance and is called the *sampling interval***. The** rest of the sample is determined by systematically taking every G**-th element** thereafter, until the end of the list. Thus, there are only G **possible samples,** each having the same probability of being selected. The simplicity of having only one random draw is a great advantage. For example, to select a sample of 200 students from the list of 20,000 students at Iowa State **University, we** first select one element among the first 100 students. Suppose **that the random**
integer we choose is 73. Then the students numbered 73, 173, 273, ···**, 19,973**
would be in the sample.

For a more formal definition of systematic sampling, let G **be the fixed**
sampling interval and let n be the integer part of N/G, where N **is the population size. Then,**
N = n·G+c where the integer c satisfies 0 ≤ *c < G***. In systematic sampling, we first select** one integer from {1,2··· ,G} with equal probability 1/G. If r **is selected from**
the selection, the final sample of systematic sampling is

$$A_{r}={\left\{\begin{array}{l l}{\{r,r+G,r+2G,\cdots,r+(n-1)G\}}&{{\mathrm{if~}}c<r\leq G}\\ {}&{{}}\\ {\{r,r+G,r+2G,\cdots,r+n G\}}&{{\mathrm{if~}}1\leq r\leq c.}\end{array}\right.}$$

The first order inclusion probability for each unit is πi = 1/G **but the second**
order inclusion probability is

$\pi_{ij}=\left\{\begin{array}{ll}1/G&\mbox{if}j=i+kG\mbox{for some integer}k,\\ 0&\mbox{otherwise.}\end{array}\right.$
That is, systematic sampling can be viewed as selecting one cluster at random among the a **possible clusters. In this case, the second-order inclusion probability of two units is positive only when the two units belong to the same**
cluster. Thus, an unbiased estimator of the variance of the HT estimator does not exist. Wolter (1984) discuss variance estimation under **systematic sampling. In addition, the efficiency of systematic sampling depends on the way**
the list is sorted. Such a concept can be investigated using the intracluster correlation coefficient in cluster sampling, which will be covered in Chapter 6.

In systematic sampling, the finite population U is partitioned into G **groups**
U = U1 ∪U2 **∪ ··· ∪**UG
where Ui **are mutually disjoint. The population total is then expressed as**

$$Y=\sum_{i\in U}y_{i}=\sum_{r=1}^{G}\sum_{k\in U_{r}}y_{k}=\sum_{r=1}^{G}t_{r}$$

where tr =Pk∈Ur yk**. Thus, in estimating the total, the finite population can**
be treated as a population with a elements with measurements t1,··· , tG.

32 *Simple and systematic sampling designs* The HT estimator can be written

$${\hat{Y}}_{\mathrm{HT}}={\frac{t_{r}}{1/G}}=G\sum_{k\in A}y_{k},$$
if A = Ur. Since we select SRS from the population of G elements {t1,··· , tG},
the variance is
$$\boldsymbol{V}$$
$$V\left({\hat{Y}}_{\mathrm{HT}}\right)={\frac{G^{2}}{1}}\left(1-{\frac{1}{G}}\right)S_{t}^{2}$$  $$S_{t}^{2}={\frac{1}{G-1}}\sum_{r=1}^{G}\left(t_{r}-{\bar{t}}\right)^{2}$$

$${\mathrm{ents~}}\{t_{1},\cdots,t_{G}\},$$

where

$$\begin{array}{c}{{\mathrm{and~}\bar{t}=\sum_{r=1}^{G}t_{r}/G.}}\\ {{\mathrm{~Now,~assuming~}N=n\cdot G}}\end{array}$$
$$\begin{array}{r c l}{{V\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{G\left(G-1\right)S_{t}^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{n^{2}G\sum_{r=1}^{G}\left(\bar{y}_{r}-\bar{y}_{u}\right)^{2}}}\end{array}$$

where ¯yr = tr/n and ¯yu = t/n ¯ **. Since** U = ∪
G
r=1Ur**, we can use the ANOVA**
decomposition to get

$$\begin{array}{r c l}{{S S T}}&{{=}}&{{\sum_{k\in U}\left(y_{k}-{\bar{y}}_{u}\right)^{2}=\sum_{r=1}^{G}\sum_{k\in U_{r}}\left(y_{k}-{\bar{y}}_{u}\right)^{2}}}\\ {{}}&{{=}}&{{\sum_{r=1}^{G}\sum_{k\in U_{r}}\left(y_{k}-{\bar{y}}_{r}\right)^{2}+n\sum_{r=1}^{G}\left({\bar{y}}_{r}-{\bar{y}}_{u}\right)^{2}}}\\ {{}}&{{=}}&{{S S W+S S B.}}\end{array}$$

Thus, the variance can be written V
YˆHT= nG·SSB = N ·SSB = N (SST −SSW).

If SSB is small, then ¯yr are more similar and V (YˆHT**) is small. If the SSW is** small, then V (YˆHT**) is large.**
To compare the systematic sampling and SRS in terms of variance, note that

$$\begin{array}{r c l}{{V_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\frac{1}{N-1}\sum_{k=1}^{N}\left(y_{k}-\bar{Y}_{N}\right)^{2}}}\\ {{}}&{{}}&{{}}\\ {{V_{\mathrm{SYS}}\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{n^{2}G\sum_{r=1}^{G}\left(\bar{y}_{r}-\bar{y}_{u}\right)^{2}.}}\end{array}$$

Systematic sampling 33 We can compare the variance by making additional assumptions about the finite population. Cochran (1946) introduced superpopulation model which the finite population is believed to be generated. The superpopulation model is an assumption about the finite population, and it quantifies the characteristics of the finite population in terms of a smaller number of parameters.

If the finite population is ordered randomly, then we may use an IID model, denoted by ζ: {yk}
i.i.d. ∼
µ,σ2**. In this case, we can obtain**

$$\begin{array}{r c l}{{E_{\zeta}\left\{V_{\mathrm{SRS}}\left(\hat{Y}_{H T}\right)\right\}}}&{{=}}&{{\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\sigma^{2}}}\\ {{E_{\zeta}\left\{V_{\mathrm{SYS}}\left(\hat{Y}_{H T}\right)\right\}}}&{{=}}&{{\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\sigma^{2}.}}\end{array}$$

Thus, the model expectations for the design variances are the same in the IID model.

Example 3.2. Consider a finite population of size N *with linear trend. That* is, we assume the following superpopulation model

$$E_{\zeta}\left(y_{k}\right)=\beta_{0}+\beta_{1}k,\quad V_{\zeta}\left(y_{k}\right)=\sigma^{2}.$$
2. **(3.24)**
To compute the model expectation of the design variance, we first note that, under the independence model ζ *with* Eζ (yi) = µi and Vζ (yi) = σ 2**, we can**
derive

$$E_{\zeta}\left(S^{2}\right)=\frac{1}{N-1}\sum_{i=1}^{N}\left(\mu_{i}-\bar{\mu}_{N}\right)^{2}+\sigma^{2},\tag{3.25}$$
$$(3.24)$$

where µ¯N = N −1PN
i=1 µi*. Thus, under (3.24), we obtain*

$$E_{\zeta}(S^{2})=\frac{\beta_{1}^{2}}{N-1}\sum_{i=1}^{N}\left(k-\frac{N+1}{2}\right)^{2}+\sigma^{2}$$ $$=\beta_{1}^{2}\frac{N}{N-1}\frac{N^{2}-1}{12}+\sigma^{2}$$ $$=\frac{N(N+1)\beta_{1}^{2}}{12}+\sigma^{2}$$
$$a n d\ s o$$
$$E_{\zeta}\left\{V_{\mathrm{SRS}}\left(\widehat{\widehat{Y}}_{\mathrm{HT}}\right)\right\}=\frac{1}{n}\left(1-\frac{n}{N}\right)\left\{\frac{N(N+1)\beta_{1}^{2}}{12}+\sigma^{2}\right\}.$$
. **(3.26)**
Now, to compute the model expectation of

$$V_{\mathrm{SYS}}({\widehat{\bar{Y}}}_{\mathrm{HT}})={\frac{1}{G}}\sum_{i=r}^{G}\left({\bar{y}}_{r}-{\bar{y}}_{i}\right)^{2}={\frac{G-1}{G}}S_{z}^{2},$$
$$(3.26)$$

34 **Simple and systematic sampling designs**

$$S_{z}^{2}={\frac{1}{G-1}}\sum_{r=1}^{G}\left(z_{r}-{\bar{z}}_{G}\right)^{2}$$
$z_{r}=\bar{y}_{r}$ and $\bar{z}_{G}=G^{-1}\sum_{r=1}^{G}z_{r}$, we can obtain, similarly to (3.25),
$$E_{\zeta}\left(S_{z}^{2}\right)=\frac{1}{G-1}\sum_{r=1}^{G}\{E_{\zeta}(z_{r})-E_{\zeta}(\bar{z}_{G})\}^{2}+V_{\zeta}(z).$$
 $Since\ z_r=n^{-1}\sum_{k=1}^n y_{r+(k-1)G}\ for\ r=1,\cdots,G,\ we\ have$  . 
$$E(z_{r})=\frac{1}{n}\sum_{k=1}^{n}\{\beta_{0}+\beta_{1}r+\beta_{1}(k-1)G\}=\beta_{0}+\beta_{1}r+\beta_{1}G\frac{n(n-1)}{2}$$  _and $V_{\zeta}(z_{r})=\sigma^{2}/n$. Thus,_
$$\begin{array}{r c l}{{E_{\zeta}\left(S_{z}^{2}\right)}}&{{=}}&{{\frac{\beta_{1}^{2}}{G-1}\sum_{r=1}^{G}\left\{r-\frac{G+1}{2}\right\}^{2}+\frac{\sigma^{2}}{n}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{=}}&{{\beta_{1}^{2}\frac{G}{G-1}\frac{G^{2}-1}{12}+\frac{\sigma^{2}}{n}}}\end{array}$$

and

$$E_{\zeta}\left\{V_{\rm SYS}(\widehat{Y}_{\rm HT})\right\}=\frac{G-1}{G}\left\{\beta_{1}^{2}\frac{G(G+1)}{12}+\frac{\sigma^{2}}{n}\right\}\tag{3.27}$$ $$=\frac{1}{n}\left(1-\frac{n}{N}\right)\left\{\frac{N(N+n)\beta_{1}^{2}}{12n}+\sigma^{2}\right\}.$$  _Therefore, comparing (3.26) and (3.27), we can establish that_  $$E_{\zeta}\left\{V_{\rm SYS}\left(\widehat{Y}_{\rm HT}\right)\right\}\leq E_{\zeta}\left\{V_{\rm SRS}\left(\widehat{Y}_{\rm HT}\right)\right\}.$$

## 3.7 Entropy For Sampling Designs

We now introduce a concept which gives a characterization of **sampling**
designs.

Definition 3.1. For a sample design p(·), the entropy of p(·) *is the quantity*

$$I(p)=-\sum_{A\in{\cal A}}p(A)\log\{p(A)\}\tag{3.28}$$

where Entropy for sampling designs 35 Roughly speaking, entropy is a measure of the randomness of a **probability**
distribution. The larger the entropy, the more randomly the **sample is selected.**
The following lemma shows that the Bernoulli sampling design with π =
1/**2 is the maximum entropy sampling design among all possible probability** sampling designs.

Lemma 3.2. *The maximum entropy design in* A = {A;A ⊂ U} is P(A) =
2
−N *, for all* A ⊂ U.

Proof. We are interested in maximizing I(p**) in (5.6) subject to**

$$\sum_{A\in{\mathcal{A}}}p(A)=1.$$
p(A) = 1. **(3.29)**
Using Lagrange multiplier method, we have only to find the maximizer of

$$Q(p,\lambda)=-\sum_{A\in{\mathcal{A}}}p(A)\log\{p(A)\}+\lambda\left(\sum_{A\in{\mathcal{A}}}p(A)-1\right).$$
$\left(3.29\right)$ . 
$$(3.30)$$
Solving
$$\frac{\partial}{\partial p(A)}Q(p,\lambda)=0,$$

we obtain p(A) = exp(λ−1). **(3.30)**
Now, inserting (3.30) into (3.29), we get

$$p(A)=\exp(\lambda-1).$$
$$\sum_{A\in{\mathcal{A}}}p(A)=2^{N}\exp(\lambda-1)=1.$$
$$A)=2^{-N}{\mathrm{~for~all~}}A\in{\mathcal{A}}.$$

Therefore, we obtain p(A) = 2−N for all A ∈ A.

According to Lemma 3.2, the maximum entropy is the entropy of the Bernoulli sampling design with π = 1/**2, which is equal to**

$$I(p^{*})=-\sum_{A\in{\mathcal{A}}}p^{*}(A)\log p^{*}(A)=N\log2.$$

This design is the most random among all sampling designs in the finite population of size N. The following theorem proves that simple random sampling without replacement is also a maximum entropy sampling design among the class of fixed-sample-size designs.

Theorem 3.1. The maximum entropy design with fixed sample size n *is the* simple random sampling design without replacement with a fixed sample size. 36 **Simple and systematic sampling designs**
Proof. Let An be the set of all possible samples of size n**. Using the Lagrange**
multiplier method, we only have to find the maximizer of

$$Q(p,\lambda)=-\sum_{A\in\mathcal{A}_{n}}p(A)\log\{p(A)\}+\lambda\left(\sum_{A\in\mathcal{A}_{n}}p(A)-1\right).$$  $$\frac{\partial}{\partial p(A)}Q(p,\lambda)=0,$$  is not $\lambda$.  
$\square$
$$\mathrm{Solving}$$

we obtain (3.27). Now, using

$$\sum_{A\in{\mathcal{A}}_{n}}p(A)={\binom{N}{n}}\exp(\lambda-1)=1.$$

we obtain p(A**) = 1**/
N
n for all A ∈ An.

The entropy of a simple random sampling design is

$$I(p_{\mathrm{SRS}})=-\sum_{A\in{\mathcal{A}}_{n}}{\frac{1}{{\binom{N}{n}}}}\log{\binom{N}{n}}^{-1}=\log{\binom{N}{n}}.$$

On the other hand, the systematic sampling design has a very small entropy. There are only G = N/n **possible samples, and each of these samples has 1**/G
selection probability. Thus, the entropy of systematic sampling is

$$I(p_{\mathrm{SYS}})=-\sum_{A\in{\mathcal{A}}}p(A)\log\{p(A)\}=G\cdot{\frac{1}{G}}\cdot\log\left({\frac{1}{G}}\right)=\log G,$$

which is much smaller than that of simple random sampling of size n = N/G. In fact, Pea et al. (2007) show that systematic sampling designs are minimum entropy designs.

4

## Stratified Sampling 4.1 Introduction

Stratified sampling refers to sampling designs in which the finite population is divided into several subpopulations, called strata, and **sample draws are** made independently across each strata. The formal definition of the stratified sampling can be made as follows.

Definition 4.1. *Stratified Sampling satisfies the following two conditions.*
1. The finite population is stratified into H **mutually exclusive and**
exhaustive subpopulations, called strata.

U = U1 **∪ ··· ∪**UH
and Uh ∩Ug = ∅ for h 6= g.

2. Within each population (or stratum), samples are drawn independently across the strata.

P r (i ∈ Ah, j ∈ Ag) = P r (i ∈ Ah)P r (j ∈ Ag), for h 6= g where Ah *is the index set of the sample in stratum* h, h = 1,2,··· ,H.

In stratified sampling, the sample size nh in stratum h **is under control at**
the time of sampling design. Thus, we can control the precision of the study domains. Furthermore, by allowing different sampling methods for different strata, we have more flexibility in sample selection and data **collection in** practice. Generally speaking, stratified sampling improves the efficiency of survey estimates over sample random sampling. For these reasons, stratified sampling is very popular in practice.

Let Uh = {1,··· ,Nh} **be the indices in the population elements in stratum**
h and let yhi denote the measurement of the study item y for unit i **in stratum**
h**. The population total** Y =PH
h=1 Yh **is the sum of the stratum totals** Yh = PNh i=1 yhi. The HT estimator of Y is the sum of the HT estimator of Yh**. That**
is,

$${\hat{Y}}_{\mathrm{HT}}=\sum_{h=1}{\hat{Y}}_{\mathrm{HT,}h}.$$
H
38 *Stratified Sampling* Note that Yˆ*HT ,h* is unbiased for Yh**. By the independence assumption, we**
obtain

$$V\left({\hat{Y}}_{\mathrm{HT}}\right)=\sum_{h=1}^{H}V\left({\hat{Y}}_{\mathrm{HT,}h}\right).$$

Example 4.1. *(Stratified random sampling)*
In stratified random sampling, we have SRS independently for *each stratum. In this case, the HT estimator of* Y is

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i=1}^{H}{\frac{N_{h}}{n_{h}}}\sum_{i\in A_{h}}y_{h i}=\sum_{i=1}^{H}N_{h}{\bar{y}}_{h}$$

where Nh is the size of Uh and nh is the size of Ah*. Its variance is*

$$V(\hat{Y}_{\rm HT})=\sum_{h=1}^{H}N_{h}^{2}V(\bar{y}_{h})=\sum_{h=1}^{H}\frac{N_{h}^{2}}{n_{h}}(1-\frac{n_{h}}{N_{h}})S_{h}^{2}\tag{4.1}$$
_where $\bar{Y}_{h}=N_{h}^{-1}\sum_{i=1}^{N_{h}}y_{hi}$ and $S_{h}^{2}=(N_{h}-1)^{-1}\sum_{i=1}^{N_{h}}(y_{hi}-\bar{Y}_{h})^{2}$._  **The action is the $\alpha$-function**
To estimate the variance in (4.1), we use

$${\hat{V}}({\hat{Y}}_{\mathrm{HT}})=\sum_{h=1}^{H}{\hat{V}}({\hat{Y}}_{H T,h})=\sum_{h=1}^{H}{\frac{N_{h}^{2}}{n_{h}}}(1-{\frac{n_{h}}{N_{h}}})s_{h}^{2}$$
_where $s_{h}^{2}$ is an unbiased estimator of $S_{h}^{2}$ and is given by $\cdot$._
$$s_{h}^{2}=\frac{1}{n_{h}-1}\sum_{i\in A_{h}}(y_{h i}-\bar{y}_{h})^{2}.$$

## 4.2 Sample Size Allocation

One of the important problems with stratified sampling is that, given the
total sample size P
n, how to decide the sample size nh in stratum h **such that**
H
h=1 nh = n. Such a problem is called the sample size allocation problem for
stratified sampling.
One simple way is to use the proportional allocation, where the sample
size in a stratum is proportional to the population size in the stratum. That is,
$$n_{h}=N_{h}\,{\frac{n}{N}}$$
N**(4.2)**
In this proportional allocation, the variance in (4.1) reduces to
$$V(\hat{Y}_{\mathrm{HT}})=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\sum_{h=1}^{H}\frac{N_{h}}{N}S_{h}^{2}.$$
$$(4.2)^{\frac{1}{2}}$$
$$(4.3)$$
Sample size allocation 39 Assuming that Nh **are sufficiently large, we have**

$$\sum_{h=1}^{H}\frac{N_{h}}{N}S_{h}^{2}=\frac{1}{N}\sum_{h=1}^{H}\frac{N_{h}}{N_{h}-1}\sum_{i=1}^{N_{h}}\left(y_{hi}-\bar{Y}_{h}\right)^{2}\tag{4.4}$$ $$\doteq\frac{1}{N-1}\sum_{h=1}^{H}\sum_{i=1}^{N_{h}}\left(y_{hi}-\bar{Y}_{h}\right)^{2}$$ $$\leq\frac{1}{N-1}\sum_{h=1}^{H}\sum_{i=1}^{N_{h}}\left(y_{hi}-\bar{Y}\right)^{2}=S^{2}.$$

Thus, the variance (4.3) under proportional allocation is no larger than the variance under simple random sampling. That is, stratified sampling under proportional allocation is more efficient than simple random **sampling in terms** of sampling variance. Here, the inequality in (4.4) is derived from the following equality:

$$\begin{array}{r c l}{{\sum_{h=1}^{H}\sum_{i=1}^{N_{h}}\left(y_{h i}-{\bar{Y}}\right)^{2}}}&{{=}}&{{\sum_{h=1}^{H}N_{h}\left({\bar{Y}}_{h}-{\bar{Y}}\right)^{2}+\sum_{h=1}^{H}\sum_{i=1}^{N_{h}}\left(y_{h i}-{\bar{Y}}_{h}\right)^{2},}}\end{array}$$

which is often expressed as SST = SSB + SSW. In (4.4), the equality holds when SSB = 0 which is the case when Y¯h **are all the same. That is, there is**
no between-stratum variation. Another extreme case is when **SSW = 0 which**
occurs when yhi = Y¯h**, (perfect homogeneity within stratum). In this extreme**
case, the variance (4.3) becomes zero. Hence, when stratum boundaries are formed, its statistical efficiency can be improved if the within-stratum variations are minimized, and the between-stratum variations are maximized. However, stratified sampling does not necessarily have a smaller variance than simple random sampling. In some poor sample size allocation, stratified sampling can have a larger sampling variance than simple random sampling.

Another advantage of proportional allocation is that the sampling weights are all equal. A sampling design that has equal sampling weights is called a self-weighting design. Self weighting is very convenient and popular in practice.

To guarantee an unbiased estimate, we need to impose nh ≥ **1 for all** h =
1,··· ,H. The proportional allocation satisfies the following three **conditions:**
1. nh are integer valued with nh ≥ 1 for all h = 1,··· ,H. 2. PH
h=1 nh = n 3. Nh/nh∼= N/n **as closely as possible for every** h.

To implement the proportional allocation, the Hintington-Hill method can be used as follows.

1. Calculate a set of "priority values" for each stratum h, based on 40 *Stratified Sampling* the state's apportionment population. The s**-th priority value in** stratum h **is defined as**

$$a_{h,s}={\frac{N_{h}}{\sqrt{s(s+1)}}}$$

where s **is the number of samples that the stratum has been allocated so far.**
2. Sort these values from largest to smallest. 3. Allocate a seat to a state each time one of its priority values is included in the largest 385 values in the list.
To illustrate the Huntington-Hill method, consider the following toy example of H **= 4 strata.**

Stratum Nh ah,1 ah,2 ah,3 ah,4

1 100,000 70,710 40,825 28,868 **22,361** 2 50,000 35,355 20,412 14,434 **11,180** 3 40,000 28,284 16,330 11,547 **8,944** 4 20,000 14,142 8,165 5,774 **4,472**

Now, suppose that we are interested in selecting a sample of size n **= 8 for**
proportional allocation. Due to nh ≥ **1, we first assign one sample to each**
stratum. Thus, it remains to select 4 additional sample elements. Based on the values of ah,s, the largest 4 values are a1,1 = 70710, a1,2 = 40825, a2,1 **= 35355,**
and a1,3 = 28868. Thus, the sample sizes for each stratum are n1 = 4, n2 **= 2,**
n3 = 1 and n4 **= 1. The Huntington-Hill method is currently used to allocate**
the seats of the House of Representatives. Wright (2012) provides a statistical interpretation of the Huntington-Hill method for stratified sampling.

Following the argument of Wright (2012), we can show that HuntingtonHill method is essentially minimizing

$$Q={\frac{1}{n}}\sum_{h=1}^{H}n_{h}\left({\frac{N_{h}}{n_{h}}}-{\frac{N}{n}}\right)^{2}.$$

It is the average squared distance of the representativeness of individual sample elements from N/n**. To see this, note that**

$$Q={\frac{1}{n}}\sum_{h=1}^{H}{\frac{N_{h}^{2}}{n_{h}}}-{\frac{N^{2}}{n^{2}}}.$$

Thus, for fixed n**, we only have to minimize the first quantity. Now, using**

$$\begin{array}{r c l}{{\sum_{h=1}^{H}\frac{N_{h}^{2}}{n_{h}}}}&{{=}}&{{\sum_{h=1}^{N}N_{h}^{2}-\sum_{h=1}^{H}\sum_{k=1}^{n_{h}-1}\left(\frac{1}{k}-\frac{1}{k+1}\right)N_{h}^{2}}}\\ {{}}&{{=}}&{{\sum_{h=1}^{N}N_{h}^{2}-\sum_{h=1}^{H}\sum_{k=1}^{n_{h}-1}\frac{N_{h}^{2}}{(k+1)k}}}\end{array}$$

Sample size allocation 41 we have only to maximize the second term:

$$\sum_{h=1}^{H}\sum_{k=1}^{n_{h}-1}{\frac{N_{h}^{2}}{(k+1)k}}=\sum_{h=1}^{H}\sum_{k=1}^{n_{h}-1}a_{h,k}^{2}$$
$$(4.5)$$

Therefore, by selecting the largest n−H elements from ah,k**' s, we can maximize the above quantity in (4.5).** Now consider another allocation method, which is obtained from an optimization problem. The optimal allocation is obtained by minimizing the variance of the HT estimator under the given constraint. The usual constraint is expressed in terms of the total cost. Total cost is **often expressed as**
C = c0 +PH
h=1 chnh, where c0 is the initial cost and ch is the cost of interviewing one unit in stratum h**. The following theorem is useful in determining**
the optimal allocation.

Theorem 4.1. *Assume that the sampling variance of an estimator is*

$$V\left({\hat{\theta}}\right)=\sum_{h}Q_{h}/n_{h}$$
$$(4.6)$$

$$a n d\ t h e\ t o t a l\ c o s t\ i s e$$
$$C=c_{0}+\sum_{h=1}^{H}c_{h}n_{h}.\tag{1}$$
$$(4.7)$$

The sample size allocation that minimizes (4.6) subject to (4.7) is

$$n_{h}\propto{\frac{\sqrt{Q_{h}}}{\sqrt{n_{h}}}}.$$

Proof. **By the Cauchy-Schwartz inequality, we obtain**

$$(4.8)$$
$$\left(\sum_{h}{\frac{Q_{h}}{n_{h}}}\right)\left(\sum_{h}c_{h}n_{h}\right)\geq\left(\sum_{h}{\sqrt{Q_{h}c_{h}}}\right)^{2}$$
$\boxed{\text{I}}$
where the equality holds when

$${\frac{c_{h}n_{h}}{Q_{h}/n_{h}}}=\mathrm{~constant}$$
which leads to $ (4.8)$... 
Note that (4.8) is the necessary and sufficient condition for the product of V (
ˆθ) and C **to be minimized. Thus, the same conclusion holds either when**
minimizing the variance subject to the cost constraints or minimizing the cost subject to the constraint on the variance. For the estimation of the population 42 *Stratified Sampling* total, using the variance form in (4.1), we have Qh = N2 h S
2 h and the optimal allocation is n
∗
h ∝ NhSh/
√ch. **(4.9)**
If ch are all equal and Sh **are the same across the strata, then the optimal**
allocation reduces to the proportional allocation. The optimal allocation in (4.9) is first proposed by Neyman (1934) and is often called the Neyman allocation.

If ch **are all equal, the optimal allocation using**

leads to $\theta$  . 
$$n_{h}=\frac{N_{h}S_{h}}{\sum_{h=1}^{H}N_{h}S_{h}}n$$  $$V_{\mathrm{opt}}(\hat{Y}_{\mathrm{HT}})=\frac{N^{2}}{n}\left(\sum_{h=1}^{H}W_{h}S_{h}\right)^{2}-N\sum_{h=1}^{H}W_{h}S_{h}^{2},$$
where Wh = Nh/N**. Note that, under proportional allocation, we have**

$$V_{\mathrm{prop}}(\hat{Y}_{\mathrm{HT}})=\frac{N^{2}}{n}\sum_{h=1}^{H}W_{h}S_{h}^{2}-N\sum_{h=1}^{H}W_{h}S_{h}^{2}.$$

Using Jensen's inequality, we obtain

$$\left(\sum_{h=1}^{H}W_{h}S_{h}\right)^{2}\leq\sum_{h=1}^{H}W_{h}S_{h}^{2},$$
which implies that $\frac{1}{2}$
Note that the allocation in (4.9) is derived by minimizing the variance
$$V_{\mathrm{prop}}({\hat{Y}}_{\mathrm{HT}})\geq V_{\mathrm{opt}}({\hat{Y}}_{\mathrm{HT}}).$$
of the total estimator. Instead of estimating the population total, if we are more interested in comparing the population means across strata, then the Neyman allocation in (4.9) is not necessarily optimal. For example, if we are interested in comparing the stratum means between stratum 1 **and stratum**
2, the parameter of interest is θ = Y¯1 − Y¯2 **and its unbiased estimator is** ˆθ =
y¯1 − y¯2**. In this case, given the same cost constraint, the optimal allocation**
that minimizes the variance of ˆθ **is, according to Theorem 4.1,**
$$(4.10)^{\frac{1}{2}}$$
n
∗
h ∝ Sh/
√ch, **(4.10)**
which is different from the Neyman allocation in (4.9). Thus, **the optimal**
allocation can be different for different parameters. Assuming that ch **are the**
same across strata and S
2 h are also the same across the strata, it is better to allocate the sample size proportional to Nh **if we are going to estimate the**
total, while it is better to use equal sample size if we are going to compare Sample size allocation 43 different stratum populations. When we want to achieve the two conflicting goals, we can use an allocation with nh ∝ Nα h
(0 *< α <* **1) as a compromise.**
This allocation is called a power allocation and α = 1/**2 is a popular choice.** See Bankier (1988) for more details about the sample size allocation.

Example 4.2. *Consider the population with* H = 3 *strata with the summary* data below. (The costs are all equal.)

| Stratum   | Pop'n Size (Nh)   | Sh   |
|-----------|-------------------|------|
| 1         | 100               | 50   |
| 2         | 110               | 10   |
| 3         | 120               | 5    |

Suppose that we wish to allocate the sample size n = 140 **to each stratum**
using optimal allocation. Using (4.8) with equal ch*, we obtain* n1 = 104 n2 = 23 n3 **= 13**
However, n1 = 104 *is greater than* N1 = 100*. Thus, we would take* n1 = N1 =
100 *and allocate the remaining 40 elements to strata and 3 to obtain*

$$n_{2}={\frac{110\times10}{110\times10+120\times5}}\cdot40\doteq26$$

$$a n d\ n_{3}=40-26=14.$$
and n3 = 40−**26 = 14**.
We now briefly discuss the problem of determining the sample size n **under**
stratified random sampling. Given the margin of error, we wish to find the sample size n for stratified sampling. That is, we wish to find n **such that**

$$P\left\{\left|{\hat{\theta}}-\theta\right|\leq e\right\}=1-\alpha.$$

Recall that, under proportional allocation, we have

$$V_{\mathrm{prop}}(\hat{Y}_{\mathrm{HT}})=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)S_{w}^{2}$$
$$\mathrm{where}$$
$$S_{w}^{2}=\sum_{h=1}^{H}W_{h}S_{h}^{2}.$$

Thus, under proportional allocation, you can use S
2w **instead of** S
2**in the**
sample size determination formula (3.10) under SRS. That is, use

$$e=z_{\alpha/2}\sqrt{\frac{S_{w}^{2}}{n}\Big(1-\frac{n}{N}\Big)}\Rightarrow n=\frac{z_{\alpha/2}^{2}S_{w}^{2}}{e^{2}+z_{\alpha/2}^{2}S_{w}^{2}/N}$$

for mean estimation.

## 44 **Stratified Sampling**

Example 4.3. We illustrate the advantage of the optimal sample-size allocation using the real data example of the US Agricultural Census data (agpop.dat) which is publicly available. The US agriculatural **Census data can**
also be obtained in "SDaA" package in R. The dataset consists **of 3,078 counties in the US in the year of 1992. From the population of counties, we are**
interested in using a stratified random sample of size n = 300 **to estimate the**
population total of variable "acres92", which represents number of acres devoted to farms in 1992. The stratification variable is "region" with levels S
(south), W (west), NC (north central), NE (northeast). Table 4.3 presents some summary statistics for the study variable for each stratum.

| Summary statistics for ares devoted to farms in 1992 Region Population Size Total Acres Standard Dev NE 220 0.199×108 79,365 NC 1,054 3.435×108 271,303 S 1,382 2.752×108 243,956 W 422 3.052×108 835,638 Total 3,078 9.44×108 424,686   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Now, the following table presents the variance under proportional allocation and Neyman allocation.

## Table 4.2

Sample sizes and sampling variances for estimated total acres devoted to farms in 1992

| Region      | Pop. Size   | Proportional Allocation   | Optimal Allocation   |     |            |
|-------------|-------------|---------------------------|----------------------|-----|------------|
| Sample Size | V (Yˆ h,HT) | Sample Size               | V (Yˆ h,HT)          |     |            |
| NE          | 220         | 21                        | 0.13×1014            | 5   | 0.60×1014  |
| NC          | 1,054       | 103                       | 7.16×1014            | 86  | 8.73×1014  |
| S           | 1,382       | 135                       | 7.60×1014            | 102 | 10.32×1014 |
| W           | 422         | 41                        | 27.38×1014           | 107 | 8.67×1014  |
| Total       | 3,078       | 300                       | 42.28×1014           | 300 | 28.32×1014 |

The efficiency gain due to optimal allocation over the proportional allocation is about 33%. That is, we can reduce the variance of the HT **estimator**
under proportional allocation by 33% if we employ the optimal allocation.

## 4.3 Stratum Boundary Determination

Sample size allocation is a problem of finding the suitable sample size for a given set of stratum boundaries. In some cases, we need to determine the stratum boundaries. The most popular method of finding the stratum boundaries was proposed by Dalenius and Hodges (1959).

To explain the idea of the stratification method of Dalenius and Hodges
(1959), assume for now that the population values of y **are available or at**
least a proxy values of y are all available. Let y0 and yH **be the smallest and**
largest values of y **in the finite population. The problem is to find intermediate**
stratum boundaries y1,··· ,yH−1 **such that**

$$V(\hat{Y}_{\mathrm{HT}})=\sum_{h=1}^{H}W_{h}^{2}\left(\frac{1}{n_{h}}-\frac{1}{N_{h}}\right)S_{h}^{2}$$

is a minimum, where Wh = Nh/N.

Under Neyman allocation, the above variance reduces to

$$V(\hat{\hat{Y}}_{\mathrm{HT}})=\frac{1}{n}\left(\sum_{h=1}^{H}W_{h}S_{h}\right)^{2}-\frac{1}{N}\sum_{h=1}^{H}W_{h}S_{h}^{2}.$$

Thus, if nh/Nh **are ignored, it suffices to minimize** PhWhSh.

Let f(y) be the frequency function of y**. If the strata are numerous and**
narrow, f(y**) should be approximately constant (rectangular) within a given** stratum. Hence,

$$\begin{array}{r c l}{{W_{h}}}&{{=}}&{{\int_{y_{h-1}}^{y_{h}}f(t)d t\,\dot{=}\,f_{h}(y_{h}-y_{h-1})}}\\ {{}}&{{}}&{{}}\\ {{S_{h}}}&{{\dot{=}}}&{{(y_{h}-y_{h-1})/{\sqrt{12}}}}\end{array}$$

where fh is the constant value of f(y) in stratum h. Thus, writing Z(y) =
R y y0 pf(t)dt, **we have**

$$\sum_{h=1}^{H}W_{h}S_{h}\propto\sum_{h=1}^{H}f_{h}(y_{h}-y_{h-1})^{2}\doteq\sum_{h=1}^{H}(Z_{h}-Z_{h-1})^{2},$$  where $Z_{h}=Z(y_{h})$ and  $$Z(y)=\int_{y_{0}}^{y}\sqrt{f(t)}dt.$$

Since (ZH −Z0**) is fixed,** PH
h=1(Zh−Zh−1)
2**is minimized by making (**Zh−
p Zh−1**) constant. To achieve this goal, the rule is to form the cumulative of**
p f(y) and choose the yh **so that they create equal intervals on the cumulative**
f(y) scale.

46 *4. Stratified sampling* 1. Partition the population into L(> 2H**) intervals with equal length.**
2. For each interval l, compute √fl**, the squared root of the frequency,**
and its cumulative sum.

3. Choose the boundaries of the stratum so that the sum of the √fl are about the same in each stratum.

## 4.4 Number Of Strata

In this section, we explore the relationship between the variance of Y
ˆ¯ 
P
HT =
H
h=1Why¯h and H**, the number of strata, under stratified sampling. To do**
this, we first consider the case when the stratum boundaries are determined by the values of the study variable Y **. To simplify the discussion, suppose that**
the realized population values y1,··· ,yN **are generated from a distribution**
with density f(y) with support in [*a, b***]. In this case, we can determined the**
stratum boundaries ah **in such a way that**

$$\int_{a_{h-1}}^{a_{h}}f(y)d y={\frac{1}{H}}$$

holds. That is, if yi ∈ [ah−1, ah] then unit i belongs to stratum h**. In this**
case, S
2 h obtained from (ah−1, ah**) satisfies** S
2 h ≤ (ah − ah−1)
2**. Thus, under**
proportional allocation, by (4.3),

$$V(\stackrel{{\widehat{\Sigma}}}{{Y}}_{HT})=\frac{1}{n}\left(1-\frac{n}{N}\right)\sum_{h=1}^{H}W_{h}S_{h}^{2}$$ $$\leq\frac{1}{nH}\sum_{h=1}^{H}(a_{h}-a_{h-1})^{2}$$

and, since PH
h=1(ah −ah−1)
2 ≤ (b−a)
2**is bounded, we obtain**

$$V(\hat{\hat{Y}}_{HT})=O\left(\frac{1}{nH}\right)\tag{4.12}$$  In the above, the $\hat{Y}_{HT}$ is the $\hat{Y}_{HT}$-norm of 
Here, bn = O(an) denotes that bn/an **is bounded.**
Therefore, from the result in (4.12), we can conclude that the relative efficiency of simple probability sampling increases proportionally to H. So, we can conclude that the higher the H, the better the efficiency. However, in practice, the stratum is not determined by observing the y**-values of the population in** advance, but by observing the values in the frame of the population (which we call x). From the sampling frame, we can only stratify based on the x-values Domain Estimation 47 in the frame. In this case, increasing H does not proportionally improve the efficiency. To illustrate, consider the following linear model

$$y_{i}=\alpha+\beta x_{i}+e_{i},\quad e_{i}\sim(0,\sigma_{e}^{2}).$$
). **(4.13)**
That is, the values of the finite population are generated from model (4.13).

Here, *α,β,σ*2 e **are unknown parameters.**
In this case, the model expectation of V (Y
ˆ¯HT**) in (4.11) is**

Eζ nV (Y ˆ¯HT)
o=1n
$$\begin{array}{l}{{\frac{1}{n}\sum_{h=1}^{H}W_{h}E_{\zeta}(S_{h}^{2})}}\\ {{\frac{1}{n}\sum_{h=1}^{H}W_{h}\left(\beta^{2}S_{x h}^{2}+\sigma_{e}^{2}\right)}}\\ {{\frac{1}{n}\sum_{h=1}^{H}W_{h}\left(\beta^{2}S_{x h}^{2}\right)+\frac{1}{n}\sigma_{e}^{2}.}}\end{array}$$
$\left(4.13\right)^{2}$
=1n
=1n
So, if we stratify based on x, the first term will be O(n
−1H−1**) as in (4.12),**
but the second term will be O(n
−1**), which is the part that is independent**
of H**. In other words, the higher the correlation coefficient between x and y,** the smaller the second term. If the correlation coefficient between x and y is high, the second term will be small, so we can see a lot of efficiency gain due to stratification. Otherwise, the second term becomes large, so the effect of stratification on reducing variance becomes smaller.

## 4.5 Domain Estimation

As discussed in Section 2.3, we generally want to make inferences about subpopulations as well as the whole population. Let Ud ⊂ U **be the index set** of the subpopulation for domain d. Let Nd = |Ud| **be the number of elements**
in Ud, Yd =Pi∈Ud yi be the domain total of y in domain d**, and** Y¯d = Yd/Nd be the domain mean of y **in domain** d.

To estimate domain parameters, define

$$z_{k d}=\left\{\begin{array}{l l}{{1}}&{{\mathrm{if~}k\in U_{d}}}\\ {{0}}&{{\mathrm{if~}k\notin U_{d},}}\end{array}\right.$$

for k ∈ U. Note that zid is a characteristic of the population. Using zkd**, we**
can exexpress Pk∈U
zkd = Nd**. The HT estimation of** Nd is

$$\hat{N}_{d}=\sum_{k\in U}\frac{z_{k d}I_{k}}{\pi_{k}}.$$
$$\mathcal{U}.\text{\it Strata}$$  Also, HT estimation of $Y_{d}=\sum_{k\in U_{d}}y_{k}=\sum_{k\in U}y_{k}z_{kd}$ is  $$\hat{Y}_{d}=\sum_{k\in U}\frac{y_{k}z_{kd}I_{k}}{\pi_{k}}=\sum_{k\in A}\frac{y_{k}z_{kd}}{\pi_{k}}.$$  To estimate $\bar{Y}_{d}=Y_{d}/N_{d}$, we may use 
 * *Stratified sampling* $$\;$$. 
  **Theorem 1**.: _Let $\mathcal{F}$ be a finite set of $\mathcal{F}$. Then $\mathcal{F}$ is a finite set of $\mathcal{F}$._  Proof.: Let $\mathcal{F}$ be a finite set of $\mathcal{F}$. Let $\mathcal{F}$ be a finite set of $\mathcal{F}$. Let $\mathcal{F}$ be a finite set of $\mathcal{F}$. Let $\mathcal{F}$ be a finite set of $\mathcal{F}$. Let $\mathcal{F}$ be a finite set of $\mathcal{F}$.  
which is a ratio of two HT estimators. Ratio of two unbiased estimator is not exactly unbiased as

$$E(\bar{y}_{d})=E\left(\frac{\hat{Y}_{d}}{\hat{N}_{d}}\right)\neq\frac{E(\hat{Y}_{d})}{E(\hat{N}_{d})}=\bar{Y}_{d},$$

but it is asymptotically unbiased as long as E(Nˆd) 6**= 0.**
The statistical properties of ¯yd **can be derived from the following approximation:**

y¯d =Yˆd Nˆd = f Nˆd,Yˆd  .= f (Nd,Yd) +∂ ∂Yd f (Nd,Yd) Yˆd −Yd  + ∂ ∂Nd f (Nd,Yd) Nˆd − Nd  =Yd Nd + 1 Nd Yˆd −Yd +  − Yd N2 d Nˆd − Nd  Thus, V (¯yd) .= V 1 Nd Yˆd −Y¯dNˆd . (4.14) Under SRS, result (4.14) can be written as
$$\begin{array}{r c l}{{V\left(\bar{y}_{d}\right)}}&{{\doteq}}&{{\frac{1}{N_{d}^{2}}V\left(\frac{N}{n}\sum_{i\in A}z_{i d}(y_{i}-\bar{Y}_{d})\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\frac{N^{2}}{N_{d}^{2}}\left(\frac{1}{n}-\frac{1}{N}\right)\frac{1}{N-1}\sum_{i=1}^{N}z_{i d}(y_{i}-\bar{Y}_{d})^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{\doteq}}&{{\left(\frac{1}{E(n_{d})}-\frac{1}{N_{d}}\right)\frac{1}{N_{d}-1}\sum_{i\in U_{d}}\left(y_{i}-\bar{Y}_{d}\right)^{2},}}\end{array}$$

where E(nd) = Nd(n/N**). Thus, the variance formula suggests that the variance of the domain mean estimator is asymptotically equivalent to the variance**
of the SRS mean of size E(nd) from the subpopulation Ud.

4.5 Domain estimation 49 The finite population is decomposed into G **groups. Group information**
was not available at the time of sample selection. The population size of the group g, denoted by Ng**, is known. If the group information is available from**
the sampling frame, then we can use stratified sampling. However, if group information is not available, then we can incorporate population information Ng **after sample selection. This is called post-stratification.**
The post-stratification estimator can be defined as

$$\hat{Y}_{\rm post}=\sum_{g=1}^{G}N_{g}\frac{\hat{Y}_{g}}{\hat{N}_{g}}.\tag{4.15}$$

Note that, unlike stratified sampling, the denominator terms (Nˆg**) are random.**
Using the Taylor expansion again, we obtain

$$\begin{array}{r c l}{{\hat{Y}_{\mathrm{post}}}}&{{=}}&{{\sum_{g=1}^{G}N_{g}\,\frac{\hat{Y}_{g}}{\hat{N}_{g}}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{\doteq}}&{{\sum_{g=1}^{G}N_{g}\left\{\frac{Y_{d}}{N_{d}}+\frac{1}{N_{d}}\left(\hat{Y}_{d}-\bar{Y}_{d}\hat{N}_{d}\right)\right\}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{Y+\sum_{g=1}^{G}\frac{1}{\pi_{i}}z_{i g}(y_{i}-\bar{Y}_{g}).}}\end{array}$$

Thus, the asymptotic variance can be written as

$$V\left(\hat{Y}_{\text{post}}\right)\doteq V\left\{\sum_{g=1}^{G}\sum_{i\in A}\frac{1}{\pi_{i}}z_{ig}(y_{i}-\bar{Y}_{g})\right\}.\tag{4.16}$$

Under SRS, the asymptotic variance (4.16) reduces to

$$\begin{array}{r c l}{{V\left(\hat{Y}_{\mathrm{post}}\right)}}&{{=}}&{{\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\frac{1}{N-1}\sum_{g=1}^{G}\sum_{i\in U g}\left(y_{i}-\bar{Y}_{g}\right)^{2}.}}\end{array}$$

Thus, it is essentially equal to the variance under stratified sampling with proportional allocation.

__
l_
l l 5

## Sampling With Unequal Probabilities 5.1 Introduction

We now consider unequal probability sampling designs, which is very popular in practice. In unequal probability sampling, we can improve the efficiency of the resulting point estimator by properly incorporating **the auxiliary information available in the sampling frame into the sampling design.**
Example 5.1. **Consider the following artificial example of a finite population**
of business companies. The total number of employees is available in the whole population, but the annual total income is available only for the sample.

| Company   | Size (Number of employees)   | y (Income)   |
|-----------|------------------------------|--------------|
| A         | 100                          | 11           |
| B         | 200                          | 20           |
| C         | 300                          | 24           |
| D         | 1,000                        | 245          |

If we wish to select only one company, we can consider the following two approaches.

1. Equal probability selection 2. Unequal probability selection with the selection probability proportional to size.

The sampling distribution of the total income estimator is then given by



| 11×4   | if A is sampled   |
|--------|-------------------|
| 20×4   | if B is sampled   |
| 24×4   | if C is sampled   |
| 245×4  | if D is sampled   |

and so

E(Yˆ **) = 11 + 20 + 24 + 245 = 300**

V (Yˆ ) = 154,488.

52 **Sampling with Unequal probabilities** On the other hand, for unequal probability sampling,

$${\hat{Y}}={\left\{\begin{array}{l l}{11\times16}\\ {20\times(16/2)}\\ {24\times(16/3)}\\ {245\times(16/10)}\end{array}\right.}$$
11×16 *if A is sampled*
20×(16/2) *if B is sampled*
24×(16/3) *if C is sampled*
245×(16/10) **if D is sampled**
$$a n d\ s o$$
 $\begin{array}{rcl}E(\hat{Y})&=&11+20+24+245=3000\\ V(\hat{Y})&=&14,248.\end{array}$
Thus, not surprisingly, unequal probability selection using the number of employees as the size is more efficient than the equal probability sampling mechanism. A company with many employees is likely to have more income than a company with a smaller number of employees.

In general, when the sampling frame contains information about the size of the sampling unit, the size information is often considered in the sampling design stage such that the selection probability of a unit is **proportional to** the size. Unequal probability sampling is also popular in cluster sampling, which we plan to cover in Chapter 7. If the cluster sizes are unequal, it is better to use this information in the cluster sampling. In some cases, unequal probability sampling is implicit. The following example illustrates this point.

Example 5.2. **Suppose that we are interested in estimating the percent of**
families owing home, by obtaining a sample of school children. The following table presents an artificial distribution of the population *of school children.*
In this example, the reporting unit is school children but the analysis unit is family. Thus, if we are selecting a simple random sample of **school children** then the large-sized families will be over-sampled. Thus, a **simple mean of the** sample observations will lead to biased estimation. In this **example, about 43%** of the families have their home. However, in the school-children level, among the 100,000 school children, the total number of children with home-owning families is

| Number of       | Families   | School children   |            |        |         |     |
|-----------------|------------|-------------------|------------|--------|---------|-----|
| school children | Number     | %                 | Owing Home | Number | %       |     |
| in family       | Number     | %                 |            |        |         |     |
| 4               | 5,000      | 10                | 500        | 10     | 20,000  | 20  |
| 3               | 10,000     | 20                | 3,000      | 30     | 30,000  | 30  |
| 2               | 15,000     | 30                | 6,000      | 40     | 30,000  | 30  |
| 1               | 20,000     | 40                | 12,000     | 60     | 20,000  | 20  |
| Total           | 50,000     | 100               | 21,500     | 43     | 100,000 | 100 |

20,000×0.1 + 30,000×0.3 + 30,000×0.4 + 20,000×0.6 = 35,000.

Thus, only 35% of the children belong to families with their home.

## 5.2 Pps Sampling

As seen in Example 5.1, a sampling design proportional to the **number of**
employs is quite efficient for estimating the total income of the companies in the population. In this case, the total number of employees serves the role of
measure of size (MOS), which is an auxiliary variable that reflects the magnitude of yi **in the population. A sampling that selects elements with probability**
proportional to MOS with replacement is called probability **proportional to**
size (PPS) sampling. Since it is easy to select a sample of size one with a selection probability proportional to MOS, we can repeat the selection n **times**
independently with replacement to achieve the PPS sampling of size n**. PPS**
sampling is easy to implement, as it is an with-replacement sampling, but it may have duplicated sample elements.
Let Mi be the value of MOS associated with element i **in the population.**
In this case,
$$p_{i}={\frac{M_{i}}{\sum_{i=1}^{N}M_{i}}}$$
is the probability of selecting element i **for a single draw of sample selection.**
Let ak be the index of population element in the k-th draw of the PPS sampling, In this case, ak is a random variable with probability P(ak = i) = pi,
for i ∈ U. The observed value of yi in the k**-th draw is** yak =PN
i=1 I(ak = i)yi.
Note that E(yak
) = PN
i=1 piyi **which is not necessarily equal to the population**
mean.
If we define
$$z_{k}=\frac{y_{a_{k}}}{p_{a_{k}}}=\sum_{i=1}^{N}I(a_{k}=i)\frac{y_{i}}{p_{i}},\quad k=1,2,\cdots,n,$$

then z1,z2,··· ,zn **are independently and identically distributed with the distribution**

tribution $$z_k=\left\{\begin{array}{ll}y_1/p_1&\text{with probability}p_1\\ y_2/p_2&\text{with probability}p_2\\ \vdots&\\ y_N/p_N&\text{with probability}p_N.\end{array}\right.$$ Thus, for each $k=1,\cdots,n$, we have 
$$\begin{array}{r c l}{{E\left(z_{k}\right)}}&{{=}}&{{\sum_{i=1}^{N}y_{i}}}\\ {{}}&{{}}&{{}}\\ {{V\left(z_{k}\right)}}&{{=}}&{{\sum_{i=1}^{N}p_{i}\left({\frac{y_{i}}{p_{i}}}-Y\right)^{2}.}}\end{array}$$
54 *Sampling with Unequal probabilities* Thus, we can use

$${\hat{Y}}_{\mathrm{PPS}}={\frac{1}{n}}\sum_{k=1}^{n}z_{k}={\frac{1}{n}}\sum_{k=1}^{n}{\frac{y_{a_{k}}}{p_{a_{k}}}}$$
$$\left(5.1\right)$$

as an estimator for Y =PN
i=1 yi**. The estimator in (5.1) is sometimes called**
Hansen-Hurwitz (HH) estimator, as it was first proposed by Hansen and Hurwitz (1943).

Alternatively, we can express

$${\hat{Y}}_{\mathrm{{PPS}}}={\frac{1}{n}}\sum_{k=1}^{n}z_{k}=\sum_{i\in A}w_{i}y_{i}$$

where wi = Qi/(npi**) and** Qi =Pn k=1 I(ak = i**) is the number of times that**
unit i **is selected in the sample. The HH estimator in (5.1) is a weighted sum** of the sample observations.

To discuss variance estimation of HH estimator, we first prove the following Lemma.

Lemma 5.1. Let X1,X2,··· ,Xn *be independent random variables with* E(Xi) = µ and V (Xi) = σ 2 i
. An unbiased estimator for the variance of X¯n = n
−1Pn i=1 Xi *is given by*

$${\hat{V}}\left({\bar{X}}_{n}\right)={\frac{1}{n}}{\frac{1}{n-1}}\sum_{i=1}^{n}\left(X_{i}-{\bar{X}}_{n}\right)^{2}.$$
$$\left(5.2\right)$$

Proof. Since Xi**'s are independent,**

$$V\left({\bar{X}}_{n}\right)={\frac{1}{n^{2}}}\sum_{i=1}^{n}\sigma_{i}^{2}\,.$$

Also, as we can express

$${\hat{V}}\left({\bar{X}}_{n}\right)={\frac{1}{n}}{\frac{1}{n-1}}\left\{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}-n\left({\bar{X}}_{n}-\mu\right)^{2}\right\},$$

by taking the expectation on both sides of the above term, we obtain

$$E\left\{{\hat{V}}\left({\bar{X}}_{n}\right)\right\}={\frac{1}{n}}{\frac{1}{n-1}}\left\{\sum_{i=1}^{n}\sigma_{i}^{2}-n{\frac{1}{n^{2}}}\sum_{i=1}^{n}\sigma_{i}^{2}\right\}={\frac{1}{n^{2}}}\sum_{i=1}^{n}\sigma_{i}^{2},$$
dness of $\hat{V}(\bar{X}_n)$ in (5.2). 
which proves the unbiasedness of Vˆ (X¯n**) in (5.2).**
By Lemma 5.1, an unbiased variance estimator of HH estimator **is given**
by

$$\hat{V}_{\rm PPS}=\frac{1}{n}S_{z}^{2}=\frac{1}{n}\frac{1}{n-1}\sum_{k=1}^{n}\left(\frac{y_{a_{k}}}{p_{a_{k}}}-\hat{Y}_{\rm PPS}\right)^{2}.\tag{5.3}$$

Poisson sampling 55 Using Qi **notation, we can express the above variance estimation formula as**

$$\hat{V}_{\text{PPS}}=\frac{1}{n}\cdot\frac{1}{n-1}\sum_{i\in A}Q_{i}\left(\frac{y_{i}}{p_{i}}-\hat{Y}_{\text{PPS}}\right)^{2}.$$  If $n/N$ is very small, then $Q_{i}$ are either $0$ or $1$. In this case,
is very small, then $Q_{i}$ are either 0 or 1. In this case,  $$\hat{V}_{\rm PPS}=\frac{n}{n-1}\sum_{i\in A}\left(w_{i}y_{i}-\frac{1}{n}\hat{Y}_{\rm PPS}\right)^{2}.\tag{5.4}$$

In some situation, yi has the meaning of a total value in unit i**. For example,**
yi is the total crop yield in the farm i and Mi **is the total size of the crop**
acres in form i. In this case, ¯yi **is the average crop yield per acre. In this case,**

we can express YˆPPS =  X N i=1 Mi ! × 1 n Xn k=1 y¯ak and i=1 Mi !2 × 1 n 1 n−1 Xn Vˆ YˆPPS=  X N k=1 y¯ak −Y ˆ¯PPS2 where Y ˆ¯PPS = n −1Pn k=1 y¯ak . If the parameter of interest is the mean Y¯ = PN i=1 yi PN i=1Mi = PN i=1Miy¯i PN i=1Mi , then the HH estimator is Y ˆ¯PPS = 1 n Xn k=1 y¯ak and its variance estimator is Vˆ Y ˆ¯PPS= 1 n 1 n−1 Xn k=1 y¯ak −Y ˆ¯PPS2. That is, in the mean estimation under PPS sampling, we can safely treat
y¯a1

,y¯a2

,··· ,y¯an as an IID sample with E(¯yak
) = Y¯ **and apply Lemma 5.1.**

## 5.3 Poisson Sampling

Poisson sampling is a generalization of Bernoulli sampling **by allowing unequal probability selection. In Poisson sampling, the sample selection indicator**
function Ii **follows**
Ii indep
∼ Bernoulli(πi), i = 1,2,··· ,N.

56 *Sampling with Unequal probabilities* Thus, the sampling design is

$$P(A)=\left(\prod_{k\in A}\pi_{k}\right)\times\left[\prod_{k\in A^{c}}\left(1-\pi_{k}\right)\right]$$
$$\left(5.5\right)$$

for all A ⊂ U. Here, πi **is the first-order inclusion probability. The following**
result, also presented in Tillé (2020), gives a useful interpretation of Poisson sampling.

Lemma 5.2. *The sampling design that maximizes entropy*

$$I(p)=-\sum_{A\in{\mathcal{A}}}P(A)\log\{P(A)\},$$

on A = {A;A ⊂ U} with fixed inclusion probabilities πk, k ∈ U**, is the Poisson**
sampling design. Proof. We wish to find the maximizer of I(p**) in (5.6) subject to**

$$\sum_{A\in{\mathcal{A}}}I(k\in A)P(A)=\pi_{k},\ \ k\in U$$
andX
$$\sum_{A\in{\mathcal{A}}}P(A)=1.$$

Using Lagrange multiplier method, we can construct

$$Q=-\sum_{A\in\mathcal{A}}P(A)\log\{P(A)\}+\sum_{k\in U}\theta_{k}\left\{\sum_{A\in\mathcal{A}}I(k\in A)P(A)-\pi_{k}\right\}+\lambda\left\{\sum_{A\in\mathcal{A}}P(A)-1\right\}.$$  Solving
$$(5.9)$$
$$\begin{array}{l}{{5.10)}}\\ {{}}\end{array}$$  $$\begin{array}{l}{{5.11)}}\\ {{}}\end{array}$$

Solving

$${\frac{\partial}{\partial P(A)}}Q=-1-\log\{P(A)\}+\sum_{k\in U}\theta_{k}I(k\in A)+\lambda=0,$$

we obtain

$$P(A)=\exp\left(\sum_{k\in U}\theta_{k}I_{k}-\mu\right),$$
where $I_{k}=I(k\in A)$ and $\mu=1-\lambda$. Using (5.8), we obtain:
$$\exp(\mu)=\sum_{A\subset U}\prod_{k\in A}\exp(\theta_{k})\tag{5.10}$$ $$=\prod_{k\in U}\{1+\exp(\theta_{k})\},\tag{5.11}$$

Poisson sampling 57 where the second equality follows from

$$\prod_{k\in{\cal U}}(a_{k}+b_{k})=\sum_{A\subset{\cal U}}\left\{\prod_{i\in A}a_{i}\cdot\prod_{j\in{\cal U}/A}b_{j}\right\}.$$

Also, using (5.7), we obtain

$$\begin{array}{r c l}{{\pi_{k}}}&{{=}}&{{\frac{\sum_{A\in\mathcal{A}}I(k\in A)\prod_{i\in A}\exp(\theta_{i})}{\exp(\mu)}}}\\ {{}}&{{=}}&{{\frac{\exp(\theta_{k})\sum_{A\in U/\{k\}}\prod_{i\in A}\exp(\theta_{i})}{\exp(\mu)}}}\\ {{}}&{{=}}&{{\frac{\exp(\theta_{k})\prod_{i\in U/\{k\}}\{1+\exp(\theta_{i})\}}{\exp(\mu)}}}\\ {{}}&{{=}}&{{\frac{\exp(\theta_{k})}{1+\exp(\theta_{k})}\cdot\frac{\prod_{i\in U}\{1+\exp(\theta_{i})\}}{\exp(\mu)}}}\\ {{}}&{{=}}&{{\frac{\exp(\theta_{k})}{1+\exp(\theta_{k})},}}\end{array}$$

where the third equality follows from (5.11) and the fifth equality follows from (5.10). Thus, we have exp(θk) = πk 1−πk and, by (5.9),

$$P(A)=\frac{\exp\left(\sum_{k\in A}\theta_{k}\right)}{\sum_{A\subset U}\exp\left(\sum_{k\in A}\theta_{k}\right)}$$ $$=\frac{\prod_{k\in A}\frac{\pi_{k}}{1-\pi_{k}}}{\prod_{k\in U}\frac{1}{1-\pi_{k}}}$$ $$=\left(\prod_{k\in A}\pi_{k}\right)\times\left\{\prod_{k\in A^{c}}\left(1-\pi_{k}\right)\right\}.$$

The entropy function in (5.6) is a measure of randomnesss of a **probability**
distribution. Thus, the Poisson sampling design is the most **random design** possible which respects a priori fixed first-order inclusion **probabilities (Tillé,** 2020).

Poisson sampling is rarely used in practice, but it is useful **in understanding**
the basic nature of unequal probability sampling. Under Poisson sampling, the variance of HT estimator is expressed as

$$V\left(\hat{Y}_{\rm HT}\right)=\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right)y_{i}^{2}.\tag{5.13}$$

58 *Sampling with Unequal probabilities* The following theorem provides a result for the optimal choice of πi **under**
Poisson sampling.

Theorem 5.1. Consider a Poisson sampling with first-order inclusion probability πi*. Given the same (expected) sample size, the variance of HT estimator* under Poisson sampling is minimized when πi ∝ yi. **(5.14)**
Proof. **Using the Cauchy-Schwarz inequality, we have**

$$\left(\sum_{i=1}^{N}{\frac{y_{i}^{2}}{\pi_{i}}}\right)\left(\sum_{i=1}^{N}\pi_{i}\right)\geq\left(\sum_{i=1}^{N}y_{i}\right)^{2}$$

and using the fact that PN
i=1 πi = n **is a fixed constant, we obtain (5.13) is**
minimized when (5.14) holds.

Thus, under Poisson sampling, we have only to make πi **proportional to** yi.

However, since we never observed yi **at the time of sampling design, we cannot**
use yi but instead use xi **in the population that is believed to be proportional** to yi.

Poisson sampling, as with Bernoulli sampling, has the disadvantage that the sample size n is random. In the extreme case, we may have n **equal to** zero. Thus, Poisson sampling has limited usage in practice, **but is useful in** developing theory.

If Poisson sampling is used, we can consider the following estimator which is first proposed by Hajék:

$$\hat{Y}_{\pi}=N\frac{\sum_{i\in A}\pi_{i}^{-1}y_{i}}{\sum_{i\in A}\pi_{i}^{-1}}.\tag{5.15}$$

Hajék estimator is a special case of the ratio estimator that **we will study**
in Chapter 8. The asymptotic variance can be obtained, by applying Taylor method,

$$\begin{array}{r c l}{{\hat{Y}_{\pi}}}&{{=}}&{{N\frac{\hat{Y}_{\mathrm{HT}}}{\hat{N}_{\mathrm{HT}}}}}\\ {{}}&{{\cong}}&{{N\frac{E(\hat{Y}_{\mathrm{HT}})}{E(\hat{N}_{\mathrm{HT}})}+N\frac{1}{E(\hat{N}_{\mathrm{HT}})}\left\{\hat{Y}_{\mathrm{HT}}-E(\hat{Y}_{\mathrm{HT}})\right\}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{-N\frac{E(\hat{Y}_{\mathrm{HT}})}{\{E(\hat{N}_{\mathrm{HT}})\}^{2}}\left\{\hat{N}_{\mathrm{HT}}-E(\hat{N}_{\mathrm{HT}})\right\}}}\\ {{}}&{{\cong}}&{{Y+\left(\hat{Y}_{\mathrm{HT}}-\bar{Y}\hat{N}_{\mathrm{HT}}\right).}}\end{array}$$  obtain
Thus, we obtain

we obtain  $$V(\hat{Y}_{\pi})\cong V\left\{\sum_{i\in A}\frac{1}{\pi_{i}}(y_{i}-\bar{Y})\right\}=\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right)\left(y_{i}-\bar{Y}\right)^{2}.\tag{5.16}$$
Maximum Entropy Sampling 59 Comparing (5.16) with (5.13), the variance of the HT estimator, the only difference is whether we use y 2 i or (yi − Y¯ )
2**in the variance formula. In many**
cases, we may say that the Hajek estimator is more efficient than the HT estimator under Poisson sampling asymptotically. Furthermore, the Hajek estimator is location invariant after a location transformation of the form yi → yi +c.

## 5.4 Maximum Entropy Sampling

The Poisson sampling introduced in the previous section has **the drawback**
of a random sample size. Using the fact that the Poisson sampling is a particular sampling design maximizing the entropy in (5.6) with the constraints on the first-order inclusion probabilities, we can impose an additional constraint on the sample size in the optimization problem. The resulting sampling design is called the maximum entropy sampling design, which was formally studied by Chen et al. (1994) and Tillé (2006). Maximum entropy sampling is closely related to the rejective Poisson sampling of Hájek (1981) and Fuller (2009). In fact, as we can see below, maximum entropy sampling can be implemented using rejective Poisson sampling.

Let An = {A;A ⊂ U,|A| = n} **be the set of all possible samples of size** n.

The maximum entropy sampling can be defined as maximizing the **entropy in** (5.6) subject to

$$\sum_{A\in{\mathcal{A}}_{n}}I(k\in A)P(A)=\pi_{k},\ \ k\in U$$
$$\operatorname{and}$$
andX
$$(5.17)$$
$$\sum_{A\in{\mathcal{A}}_{n}}P(A)=1.$$
$$(5.18)$$

Using the same argument for proving Lemma 5.2, the solution to this optimization problem is

$$P(A)={\left\{\begin{array}{l l}{{\frac{\exp\left(\sum_{k\in A}\theta_{k}\right)}{\sum_{A\in A_{n}}\exp\left(\sum_{k\in A}\theta_{k}\right)}}}&{{\mathrm{if~}}|A|=n}\\ {0}&{{\mathrm{otherwise,}}}\end{array}\right.}$$
$$(5.19)$$
$$(5.20)$$

where θ1,··· ,θN **are the parameters of the maximum entropy design and are**
determined by (5.17). Thus, (5.19) is the sampling design for the maximum
entropy sampling. Equation (5.17) is a system of N **equations to solve** θk. Tillé (2006) discussed a fast algorithm for computing θk **satisfying (5.17).**
Now, to compare the maximum entropy sampling with Poisson sampling,
define
$$\tilde{\pi}_{k}=\frac{\exp(\theta_{k}+C)}{1+\exp(\theta_{k}+C)}$$
1 + exp(θk +C)(5.20)
60 *Sampling with Unequal probabilities*

where $C$ is chosen to satisfy 



We can consider the rejective Poisson sampling as follows:
[Step 1] Use ˜πk **in (5.20) to select a Poisson sample.**
[Step 2] Check if the realized sample size of the Poisson sample is equal to n**, the target sample size. If yes, it is the final sample. Otherwise, goto [Step** 1].

Because the sampling design of the Poisson sampling in [Step **1] is, by (5.12),**

$${\tilde{P}}(A)={\frac{\exp\left(\sum_{k\in A}\theta_{k}+C\right)}{\sum_{A\subset U}\exp\left(\sum_{k\in A}\theta_{k}+C\right)}},$$

the maximum entropy sampling design in (5.19) can be written as

$$P(A)={\frac{\tilde{P}(A)}{\sum_{A\in{\mathcal{A}}_{n}}\tilde{P}(A)}},\ \ A\in{\mathcal{A}}_{n}.$$

Thus, P(A) in (5.19) is the conditional Poisson sampling conditional **on the** fixed sample size n.

In order to construct an algorithm to implement the maximum entropy design, it is necessary to be able to calculate the vector ˜π = (˜π1,··· ,π˜N )
′**from**
the vector π = (π1,··· ,πN )
′**. This algorithm is implemented in the function**
UPmaxentropy of 'sampling' package R developed by Tillé and **Matei (2016).**

## 5.5 Π**Ps Sampling**

The PPS sampling introduced in the previous section has many **advantages: it is very easy to implement, the estimation formula is simple. However,**
since it is a with-replacement sampling, it is inefficient in the sense that it allows for duplicated sample elements. Let xi **be the size measure that we want**
to make πi ∝ xi as close as possible. The πps(π **proportional to size) sampling**
refers to a set of sampling designs that satisfies the following conditions:

1. The sampling design is a fixed-size sampling design that does not allow for duplication.

2. The first-order inclusion probability πi **satisfies** πi ∝ xi.

3. The second order inclusion probability satisfies πij > **0 and** πij <
πiπj (i 6= j).
π*ps sampling* 61 The third condition guarantees that the SYG variance estimator is always nonnegative.

For a fixed-size design, πk ∝ xk and PN
i=1 πi = n **leads to**

$$\pi_{k}={\frac{n x_{k}}{\sum_{i=1}^{N}x_{i}}}.$$

If some xk satisfies xk > (N/n)X¯N , then we have πi > **1. Thus, the exact**
proportionality πi ∝ xi **is not always possible. In practice, the units with**
πk > 1 are automatically selected. The inclusion probabilities **are recalculated**
in the same way excluding the element that is automatically selected. That is, if k satisfies πk > 1, then we set πk **= 1 and recompute**

$$\pi_{i}=(n-1){\frac{x_{i}}{\sum_{i\neq k}x_{i}}}.$$
.
This operation is repeated until πi ≤ **1 for all element in the population.**
For n = 1, the π**ps sampling is the same as the PPS sampling. There**
are two approaches of implementing a PPS sampling of size n **= 1. One is the**
cumulative total method, and the other is the Lahiri's method. The cumulative total method is described as follows:
[Step 1] Set T0 = 0 and compute Tk = Tk−1 +xk, k = 1,2,··· ,N. [Step 2] Draw ǫ ∼ Unif (0,1). If ǫ ∈ (Tk−1/TN ,Tk/TN ), element k **is selected.**
The cumulative total method is very popular because it is easy to understand.

It needs a list of all xk **in the population.**
The other method, developed by Lahiri (1951), can be described as follows:
[Step 0] Choose M > {x1,x2,··· ,xN }. Set r **= 1.** [Step 1] Draw kr by SRS from {1,2,··· ,N}. [Step 2] Draw ǫr ∼ Unif (0,1). [Step 3] If ǫr ≤ xkr
/M, then select element kr **and stop. Otherwise, reject** kr and goto Step 1 with r = r **+ 1.**
Lahiri's method does not need a list of all xk **in the population, but requires** the knowledge of the upper bound of xk**, denoted by** M.

A formal justification for Lahiri's method can be described as follows:
πk = P r(k ∈ A)

$=\quad\;\;Pr(k\in A)$  . 
$$\begin{array}{r l}{r}&{{}={\quad}T r\left(k\in A\right)}\\ {={\quad}}&{{\sum_{r=1}^{\infty}P r(k\in A,R=r)}}\\ {={\quad}}&{{\sum_{r=1}^{\infty}P r\left\{K_{r}=k,\epsilon_{r}<{\frac{x_{k_{r}}}{M}},\bigcap_{j=1}^{r-1}(\epsilon_{j}>{\frac{x_{k_{j}}}{M}})\right\}}}\\ {={\quad}}&{{\sum_{r=1}^{\infty}{\frac{1}{N}}{\frac{x_{k}}{M}}\times\prod_{j=1}^{r-1}P r\left\{\epsilon_{j}>{\frac{x_{k_{j}}}{M}}\right\}.}\end{array}$$
62 *Sampling with Unequal probabilities*

Since  $ Pr\left(\epsilon_j>\frac{x_{kj}}{M}\right)=\sum_k Pr\left(\epsilon_j>\frac{x_{kj}}{M}\mid k_j=k\right)Pr(K_j=k)=\sum_k\left(1-\frac{x_k}{M}\right)\frac{1}{N}=1-\frac{\bar{x}_U}{M}$,
where ¯xU = N −1PN
i=1 xk**, we can obtain**

$$\begin{array}{r c l}{{\pi_{k}}}&{{=}}&{{\sum_{r=1}^{\infty}{\frac{1}{N}}{\frac{x_{k}}{M}}\left(1-{\frac{\bar{x}_{U}}{M}}\right)^{r-1}}}\\ {{}}&{{=}}&{{{\frac{x_{k}}{\sum_{i=1}^{N}x_{i}}}.}}\end{array}$$

We now discuss πps sampling for n **= 2. Most of the existing schemes for**
fixed-size πps sampling with n > **2 are quite complicated. The interested reader**
is referred to Tillé (2006). To discuss πps sampling of size n = 2, let θi **be the**
probability of selecting unit i in the first draw of the π**ps sampling and let**
θj|i be the conditional probability of selecting unit j **in the second draw given**
that unit i **is selected in the first draw. Thus, writing** pi = xi/(PN
j=1 xj **), the**
problem at hand is to find a set of θi and θj|i**satisfying**

$$(5.22)$$

πi = 2pi **(5.21)**

andX
$$\sum_{i}\theta_{i}=\sum_{j}\theta_{j|i}=1.$$
Since πij = θiθj|i +θjθi|j**(5.22)**
and, as it is a fixed-size sampling design, we can use (2.2) to get Pj6=i πij = πi, which implies

$$\pi_{i}=\theta_{i}+\sum_{j\neq i}\theta_{j}\theta_{i|j}.$$

Thus, constraint (5.21) reduces to

$$\theta_{i}+\sum_{j\neq i}\theta_{j}\theta_{i|j}=2p_{i}.$$
$$(5.23)$$

Since there are N2 unknowns with N **equations, we have many solutions to**
(5.23).

Brewer (1963) proposed using

$$\theta_{i}\propto{\frac{p_{i}\left(1-p_{i}\right)}{1-2p_{i}}}$$
$$(5.24)$$
and
$$\theta_{j|i}\propto p_{j}$$

π*ps sampling* 63 to obtain (5.23), while Durbin (1967) proposed using θi = pi and

$$\theta_{j|i}\propto p_{j}\left(\frac{1}{1-2p_{i}}+\frac{1}{1-2p_{j}}\right)\tag{5.25}$$  where
to achieve the same goal.

In Brewer's method, we first choose θj|i = pj/(1 − pi) for i 6= j **and use**
(5.23) to get

$$\begin{array}{r c l}{{2p_{i}}}&{{=}}&{{\theta_{i}+\sum_{j\neq i}\theta_{j}\frac{p_{i}}{1-p_{j}}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{=}}&{{\theta_{i}+p_{i}\left(B-\frac{\theta_{i}}{1-p_{i}}\right),}}\end{array}$$
where $B=\sum_{j=1}^{N}\theta_{j}/(1-p_{j})$. Thus, we get:
$$\theta_{i}={\frac{2p_{i}-p_{i}B}{1-{\frac{p_{i}}{1-p_{i}}}}}=(2-B){\frac{p_{i}(1-p_{i})}{1-2p_{i}}},$$

which proves (5.24).

Using (5.22), Brewer's method leads to

$$\pi_{i j}=C\cdot p_{i}p_{j}\left({\frac{1}{1-2p_{i}}}+{\frac{1}{1-2p_{j}}}\right)$$
**(5.26)**
for some C**. Now,**

j6=i πij = C · pi X j6=i pj 1 1−2pi +1 1−2pj  X = C · pi  pj 1−2pj − pi 1−2pi + 1−pi 1−2pi   = C · pi  pj 1−2pj + 1  X N X N . j=1 j=1 Because πi = X j6=i πij = 2pi, (5.27) we get πij = 2pipj 1 + K 1 1−2pi +1 1−2pj (5.28) where K =PN i=1 (1−2pi) −1pi. In Durbin (1967), we set θi = pi = πi/2 and θj|i = πij/πi with πij in (5.28).
$$(5.26)$$
Thus, we obtain (5.25).
64 *Sampling with Unequal probabilities* We now introduce one πps method proposed by Chao (1982). Chao's sampling is a special case of reservoir sampling with unequal probability of selection. The sampling plan can be described by induction. Let Uk = {1,··· , k} be the set of elements in the finite population up to the element k. Let Ak **be the**
set of sample elements selected from Uk with the first-order inclusion probability proportional to x. Let π(k;i) = P(i ∈ Ak | Uk**) be the corresponding**
first-order inclusion probability of the unit i from Uk **satisfying**

$$\pi(k;i)=n\cdot{\frac{x_{i}}{\sum_{j=1}^{k}x_{j}}}.$$
$$(5.29)$$
. **(5.29)**
Now, for Uk+1 = Uk ∪ {k + 1}**, we update the sample as follows:**
1. Select element k **+ 1 with the selection probability** pk+1 = nWk+1, where

$$W_{k+1}={\frac{x_{k+1}}{\sum_{j=1}^{k+1}x_{j}}}.$$

2. If k+ 1 is selected from Step 1, remove one element (say j**) from** Ak with probability 1/n and set Ak+1 = Ak ∪ {k + 1}/{j}**. Otherwise,**
set Ak+1 = Ak.

To explain Chao's sampling, note that we can write

$$P(j\in A_{k+1}\mid U_{k+1})=P(j\in A_{k}\mid U_{k})P(j\in A_{k+1}\ \mbox{and}\ k+1\in A_{k+1}\mid U_{k+1},A_{k})\tag{5.30}$$ $$+P(j\in A_{k}\mid U_{k})P(k+1\notin A_{k+1}\mid U_{k+1},A_{k}).$$
Now, by the Chao's sampling mechanism, we obtain
$$P(j\in A_{k+1}\ \mbox{and}\ k+1\in A_{k+1}\ |\ U_{k+1},A_{k})$$ $$=P(j\in A_{k+1}\ |\ U_{k+1},A_{k})P(k+1\in A_{k+1}\ |\ U_{k+1},A_{k})$$ $$=\frac{n-1}{n}\times p_{k+1}$$
P(k + 1 ∈/ Ak+1 | Uk+1,Ak**) = 1**−pk+1.
Thus, (5.30) reduces to
$$\operatorname{and}$$
$$\begin{array}{r c l}{{P(j\in A_{k+1}\mid U_{k+1})}}&{{=}}&{{P(j\in A_{k}\mid U_{k})\times\left(1-W_{k+1}\right).}}\end{array}$$

Now, by (5.29), we obtain

$$P(j\in A_{k+1}\mid U_{k+1})=n\cdot{\frac{x_{j}}{\sum_{j=1}^{k+1}x_{j}}}.$$
Thus, as $\log$
Thus, as long as (5.29) holds, the above procedure leads to

$$(5.31)$$
 $ \pi(k+1;i)=n\cdot\frac{x_i}{\sum_{j=1}^{k+1}x_j}$  from population $ U$. 
$$(5.32)$$
which is a $\pi$ps sampling from population $U_{k+1}$. 
Systematic π*ps sampling* 65 Remark 5.1. *In Chao's sampling, the initial sample* Sn = {1,··· ,n} for k = n does not satisfy (5.29). In fact, by (5.31),

$$\pi(k+1;j)=P(j\in S_{j}\mid U_{j})\prod_{i=j}^{k}(1-W_{i+1})=P(j\in S_{j}\mid U_{j}){\frac{\sum_{i=1}^{j}x_{i}}{\sum_{i=1}^{k+1}x_{i}}}.$$
$$N o w,\;s i n c e\;$$
_ince_  $$P(j\in S_{j}\mid U_{j})=\left\{\begin{array}{ll}1&\mbox{if$j\leq n$}\\ nW_{j}&\mbox{if$j>n$},\end{array}\right.$$

result (5.32) holds only for i > n*. The first-order inclusion probability of unit* j ≤ n *in the* (k + 1)*-th population is then*

$$\pi(k+1;j)={\frac{\sum_{i=1}^{n}x_{i}}{\sum_{i=1}^{k+1}x_{i}}}=n{\frac{{\bar{x}}_{n}}{\sum_{i=1}^{k+1}x_{i}}}={\frac{1}{n}}\sum_{i=1}^{n}{\tilde{\pi}}(k+1;i),$$
$$w h e r\;\tilde{\pi}(k+1;i)=n x_{i}/(\sum_{j=1}^{k+1}x_{j}).$$

## 5.6 Systematic Π**Ps Sampling**

Systematic π**ps sampling is similar to systematic sampling but allows for**
unequal probability of sample selection. Let a =PN
i=1 xi/n **be the sampling**
interval for systematic sampling. Assume xk < a for all k ∈ U**. (If some of**
the xk's are greater than a**, then such elements are selected in advance and**
then the systematic sampling is applied in the reduced finite **population.)** Systematic π**ps sampling can be described as follows.**

  **10 $\kappa$** **18**. 
1. Choose R ∼ Unif (0, a]
2. Unit k **is selected iff**
Lk < R+l · a ≤ Uk for some l = 0,1,··· ,n − **1, where** Lk =Pk−1 j=1 xj with L0 **= 0 and**
Uk = Lk +xk.

Example 5.3. *For example, consider the following artificial finite population* of size N = 4.

| ID   | MOS (xi)   | L   | U   |
|------|------------|-----|-----|
| 1    | 10         | 0   | 10  |
| 2    | 20         | 10  | 30  |
| 3    | 30         | 30  | 60  |
| 4    | 40         | 60  | 100 |

66 **Sampling with Unequal probabilities**
To obtain a systematic sample of size n = 2 **with the first-order inclusion**
probability proportional to xi*, note that* a = 100/2 = 50*. Thus, we first generate* R *from a uniform distribution* (0,50]. If R *belongs to* (0,10]*, we select* A =
{1,3}. If R *belongs to* (10,30], we select A = {2,4}. If R *belongs to* (30,50], we select {3,4}*. The sampling distribution of the resulting sample will be*

$$P\left(A\right)={\left\{\begin{array}{l l}{0.2,}&{{\mathrm{~if~}}A=\left\{1,3\right\}}\\ {0.4,}&{{\mathrm{~if~}}A=\left\{2,4\right\}}\\ {0.4,}&{{\mathrm{~if~}}A=\left\{3,4\right\}}\end{array}\right.}$$

To compute the first-order inclusion probability of unit k, let l **be the**
integer satisfying l · a ≤ Lk < Uk ≤ (l **+ 1)**a.

$$\begin{array}{r c l}{{P r\left(k\in A\right)}}&{{=}}&{{P r\left\{L_{k}<R+l\cdot a\leq U_{k}\right\}}}\\ {{}}&{{=}}&{{\int_{L_{k}-l\cdot a}^{U_{k}-l\cdot a}{\frac{1}{a}}d t=x_{k}/a={\frac{n x_{k}}{\sum_{k\in U}x_{k}}}.}}\end{array}$$

The systematic π**ps sampling is easy to implement but it does not allow for**
design-unbiased variance estimator, as is the case with the **classical systematic** sampling.

Cluster Sampling: Single stage cluster

## Sampling 6.1 Introduction

Element sampling designs are not always feasible when there **is no sampling**
frame for the survey units. Instead, the sampling frame is often available in the form of clusters, such as schools or districts. In this case, cluster sampling that samples clusters is commonly used. Also, cluster sampling is often costeffective in terms of reducing the travel cost and also controlling the field work of the interviewers.

In cluster sampling, the finite population is grouped into clusters. A probability sample of clusters is selected, and every element in **the selected clusters** is surveyed. Clusters are also called primary sampling units (PSUs). If a probability sample of PSUs is drawn and every element in the selected PSUs is measured, the sampling design is called single-stage cluster sampling. On the other hand, if another probability sampling is used to draw sample elements in the selected clusters, the sampling design is called a two-stage sampling design. Multi-stage sampling consists of three or more stages **of sampling. There**
is a hierarchy of sampling units: primary sampling units, secondary sampling units within the PUS, and so on. The sampling units in the last-stage sampling are called the ultimate sampling units. In this chapter, we will focus on single-stage sampling.

Let UI = {1,··· ,NI } **be the index set of clusters in the population. Let** Ui be the set of elements in the i-th cluster of size Mi. Let yij **be the measurement**
associated with element i in cluster i. The population total of y **is denoted**
by Y =PNI
i=1 Pj∈Ui yij =PNI
i=1 Yi =PNI
i=1MiY¯i, where Y¯i = Yi/Mi **is the**
population mean of y **in cluster** i.

In the single-stage sampling, we select AI from UI by probability sampling. The index set A **of the sample elements can be written as** A = ∪i∈AIUi in single-stage sampling. Let nI = |AI | **be the number of sampled clusters.** Let nA = |A| **be the number of sampled elements. Under single-stage cluster**
sampling, we have nA =Pi∈AI Mi.

6

## 6.2 Single-Stage Cluster Sampling: Equal Size Case

When the cluster size Mi is equal to M**, the following sampling design can**
be considered.

1. Simple random sampling of nI clusters from NI **clusters.**
2. Observe all the elements in the selected clusters.

Such a sampling design is called simple random cluster sampling. In this case, the HT estimator of Y =PNI
i=1 Yi is

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i\in A_{I}}{\frac{1}{\pi_{I i}}}Y_{i}={\frac{N_{I}}{n_{I}}}\sum_{i\in A_{I}}Y_{i}$$

where πIi = P(i ∈ AI **) is the cluster-level first-order inclusion probability and**
is equal to πIi = nI /NI **under simple random cluster sampling. Thus, the HT**
estimator of Y¯U = Y /(NIM**) is**

$${\hat{\bar{Y}}}_{U}={\frac{{\hat{Y}}_{H T}}{N_{I}M}}={\frac{1}{n_{I}}}{\frac{1}{M}}\sum_{i\in A_{I}}Y_{i}={\frac{1}{n_{I}}}\sum_{i\in A_{I}}{\bar{Y}}_{i}.$$

Note that Y
ˆ¯U is the sample mean of Y¯i**. Thus, the sampling variance of** Y
ˆ¯U is

$$V(\hat{Y}_{U})=\frac{1}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)\frac{1}{N_{I}-1}\sum_{i=1}^{N_{I}}\left(\bar{Y}_{i}-\bar{Y}_{U}\right)^{2}\tag{6.1}$$
$\zeta_{\bar{\nu}}((N,M)-\sum_{i=1}^{N}\bar{\nu}_{i}(N))$
where Y¯i =PM
j=1 yij/M and Y¯U = Y /(NIM) = PNI
i=1 Y¯i/NI .

To discuss the variance form in (6.1), the following ANOVA table is considered.

| ANOVA table for the population of clusters with equal size Source d.f Sum of Squares Mean SS Between cluster NI −1 SSB S 2 b 2 w Within cluster NI (M −1) SSW S Total NIM −1 SST S 2   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Here, the sum of squares are defined as below and the mean sum of squares 6.2 Equal size cluster sampling 69 are computed by dividing the sum of squares by their degrees of freedom

$$\begin{array}{r l}{S S T}&{{}=}\\ {}&{}\\ {}&{}\\ {S S B}&{{}=}\\ {}&{}\\ {}&{}\\ {S S W}&{{}=}\\ {}&{}\\ {}&{}\end{array}$$
SST =X
$$\begin{array}{l}{{\sum_{i=1}^{N_{I}}M}}\\ {{\sum_{i=1\,j=1}^{N_{I}}(y_{i j}-{\bar{Y}})^{2}}}\\ {{\sum_{i=1\,j=1}^{N_{I}}({\bar{Y}}_{i}-{\bar{Y}})^{2}}}\\ {{\sum_{i=1\,j=1}^{N_{I}}M}}\\ {{\sum_{i=1\,j=1}^{N_{I}}(y_{i j}-{\bar{Y}}_{i})^{2}.}}\end{array}$$
SSB =X
SSW =X
Note that, since SST = SSB +SSW, S
2**is a weighted average of two mean**
sum of squares terms:

$$\begin{array}{r c l}{{S^{2}}}&{{=}}&{{\frac{S S T}{N_{I}M-1}}}\\ {{}}&{{=}}&{{\frac{\left(N_{I}-1\right)S_{b}^{2}+N_{I}\left(M-1\right)S_{w}^{2}}{N_{I}M-1}}}\\ {{}}&{{\cong}}&{{\frac{S_{b}^{2}+\left(M-1\right)S_{w}^{2}}{M}.}}\end{array}$$

Thus, since SSB = M ·PNI
i=1(Y¯i −Y¯ )
2**, we have**

$=M_{\mu}\sum_{}^{}N_{}~(\bar{Y}_{i}-\bar{Y})^2$. 
$${\frac{1}{N_{I}-1}}\sum_{i=1}^{N_{I}}\left({\bar{Y}}_{i}-{\bar{Y}}_{U}\right)^{2}={\frac{S S B}{(N_{I}-1)M}}={\frac{S_{b}^{2}}{M}}$$

and the variance expression in (6.1) can be written as

$$V\left(\stackrel{{\circ}}{{Y}}_{U}\right)=\frac{1}{n_{I}M}\left(1-\frac{n_{I}}{N_{I}}\right)S_{b}^{2}.\tag{6.2}$$

Now, let's compare the variance in (6.2) with the variance of **another HT**
estimator under simple random sample of the same size, which is

$$V_{\rm SRS}\left(\hat{Y}_{U}\right)=\frac{1}{n_{IM}}\left(1-\frac{n_{IM}}{N_{IM}}\right)S^{2},\tag{6.3}$$

as n = nIM **is the size of the sampled elements. To compare (6.3) with (6.2),**
we first introduce the concept of intracluster correlation coefficient. The intracluster correlation coefficient is the population correlation coefficient between two units in the same cluster. 70 *6. Single-stage Cluster Sampling* Definition 6.1. *Intraclass correlation coefficient:*

$$\begin{array}{l}{{\rho=\frac{C o v[y_{i j},y_{i k}\mid j\neq k]}{\sqrt{V(y_{i j})}\sqrt{V(y_{i k})}}}}\\ {{=\frac{\sum_{i=1}^{N_{I}}\sum_{j\neq k}\sum(y_{i j}-\bar{Y})(y_{i k}-\bar{Y})/\sum_{i=1}^{N_{I}}M(M-1)}{\sum_{i=1}^{N_{I}}\sum_{j=1}^{M}(y_{i j}-\bar{Y})^{2}/\sum_{i=1}^{N_{I}}M}}}\\ {{=\frac{1}{M-1}\frac{\sum_{i=1}^{N_{I}}\sum_{j\neq k}\sum(y_{i j}-\bar{Y})(y_{i k}-\bar{Y})}{\sum_{i=1}^{N_{I}}\sum_{j=1}^{M}(y_{i j}-\bar{Y})^{2}}}}\end{array}$$

Using the following identity

$$\begin{array}{r c l}{{\sum_{i}\sum_{j\neq k}\sum_{k}(y_{i j}-\bar{Y})(y_{i k}-\bar{Y})}}&{{=}}&{{\sum_{i}\left\{\sum_{j}(y_{i j}-\bar{Y})\right\}^{2}-\sum_{i}\sum_{j}(y_{i j}-\bar{Y})^{2}}}\\ {{}}&{{=}}&{{M\cdot S S B-S S T,}}\end{array}$$  we can express... 
we can express

$$\rho=\frac{M\cdot SSB-SST}{(M-1)SST}=1-\frac{M}{M-1}\frac{SSW}{SST}\tag{6.4}$$

and so

$$-{\frac{1}{M-1}}\leq\rho\leq1.$$
$$(6.5)$$

The minimum value of ρ is achieved when SSB = 0 which occurs when Y¯i are all equal. The maximum value of ρ is achieved when SSW **= 0 which occurs**
when all elements are homogeneous within clusters (i.e. yij = Y¯i**). Note that**
we can also express

$$\rho=1-\frac{S S W/\{N_{I}(M-1)\}}{S S T/N_{I}M}\doteq1-\frac{S_{w}^{2}}{S^{2}}.$$
. **(6.5)**
The following lemma gives alternative expressions for the mean sum of square terms of the ANOVA table in Table 6.2 in terms of the intracluster correlation coefficient ρ.

Lemma 6.1. Using ρ*, we can express*

$$S_{b}^{2}\doteq S^{2}\{1+(M-1)\rho\}.$$
2{1 + (M −1)ρ}. **(6.6)**
Proof. From (6.4), we can use SST = SSB +SSW **to get**

$$S S B={\frac{1}{M}}\left[1+\rho\left(M-1\right)\right]S S T.$$

Now, using S
2
b = SSB/(NI − 1) .= *SSB/N*I and S
$$\mathrm{d}\ S^{2}\doteq S S T/(N_{I}M),\ \mathrm{we\get}$$
(6.6). 6.2 Equal size cluster sampling 71 By (6.6), combining (6.2) and (6.3), we can establish the following theorem, which gives an alternative expression of the sampling variance of the HT estimator in a single-stage cluster sampling design.

Theorem 6.1. *Under simple random cluster sampling, for sufficiently large* N*, the variance of HT estimator can be written*

$$V\Big{(}\hat{Y}_{\rm HT}\Big{)}\stackrel{{\mbox{\tiny$\perp$}}}{{=}}V_{\rm SRS}\left(\hat{Y}_{\rm HT}\right)\cdot\{1+(M-1)\rho\}\tag{6.7}$$  _where $\rho$ is the intracluster correlation coefficient and $V_{\rm SRS}\left(\hat{Y}_{\rm HT}\right)$ is the vari 
where ρ *is the intracluster correlation coefficient and V*SRS YˆHT*is the variance of HT estimator under SRS of equal size.*
The above theorem shows that the sampling variance of the HT estimator under simple random cluster sampling is {1 + (M −1)ρ} **times larger than** that of HT estimator under SRS of equal size. Thus, {1 + (M −1)ρ} **is the**
ratio of two variances and expresses the inverse of the relative efficiency of the simple random cluster sampling over the simple random sampling. Kish (1965) first introduced the concept of the design effect as follows.

Definition 6.2. Design effect (deff) of the sampling design p(·) *with the sample size* n = np:

$$\operatorname*{diff}\left(p,{\hat{Y}}_{H T}\right)={\frac{V_{P}\left({\hat{Y}}_{\mathrm{HT}}\mid n_{p}\right)}{V_{\mathrm{SRS}}\left({\hat{Y}}_{\mathrm{HT}}\mid n_{p}\right)}}.$$
$$(6.8)$$

In simple random cluster sampling, we have deff = 1 + (M −1)ρ. **(6.8)**
For example, if ρ = 0.1 and M = 11, deff = 2. Thus, even if ρ **is low, the design** effect can be large if M **is large.**
There are two usages of the design effect. One is to compare designs. For example, if deff > 1, then p(·) is less efficient than SRS. If deff < **1, then** p(·)
is more efficient than SRS.

The other usage is to determine the sample size. When the design effect of a design p(·**) is known, the sample size under the design is determined as**
follows.

1. Have some desired variance V
∗

2. Under SRS, you can easily find required sample size n
∗
3. Choose n
∗p **= deff**·n
∗.
72 *6. Single-stage Cluster Sampling* Then, ignoring the finite population correction term,

$$V_{p}\left(\hat{Y}_{\rm HT}\mid n_{p}^{*}\right)=V_{\rm SRS}\left(\hat{Y}_{\rm HT}\mid n_{p}^{*}\right)\cdot\ {\rm def}$$ $$=\frac{N^{2}}{n_{p}^{*}}S^{2}\cdot{\rm def}$$ $$=\frac{N^{2}}{n^{*}}S^{2}$$ $$=V^{*}.$$

The sample size n
∗is often called the *effective sample size***. It is the sample**
size required for the given V
∗**if the sample design is SRS. Given the current**
sample size n**, the effective sample size** n
∗**is calculated by**

$$n^{*}={\frac{n}{\mathrm{{{\small{{\mathrm{{diff}}}}}}}}}$$

Example 6.1. *Suppose that we are interested in estimating the population* proportion of certain characteristics by simple random cluster sampling with M = 200 *elements in the cluster. We want to have a margin of error equal to* 2% at the significant level α = 0.05*. How many sampling clusters are needed* for this design? Assume that the intracluster correlation coefficient ρ = 0.05.

To answer this question, first calculate the effective sample *size. The effective sample size is equal to* n
∗ = (0.02)−2 = 2,500*. The design effect is* 1 + 199 ∗ 0.05 .= 11*. Thus, the number of sample clusters is* 2,500 ∗ 11/**200 =**
137.5.

Example 6.2. **Assume that a simple random sample of clusters is selected**
from a population of clusters of equal size. Suppose that there are NI **clusters**
in the population and that there are M *elements in each cluster. Within the* sampled cluster, we used simple random sampling to obtain the observed values of the sample elements. The sample observations are summarized in the following ANOVA table.

## Table 6.2

Sample ANOVA table (equal cluster size M)

| Source                 | D.F.      | Sum of Squares     | Mean S.S.            |
|------------------------|-----------|--------------------|----------------------|
| Between                | nI −1     | Sample SSB (=SSSB) | s 2 b = SSSB/(nI −1) |
| 2 w = SSSW/{nI (M −1)} |           |                    |                      |
| Within                 | nI (M −1) | Sample SSW (=SSSW) | s                    |
| Total                  | nIM −1    | Sample SST (=SSST) | s 2 = SSST /(nIM −1) |

Single-stage cluster sampling: Unequal Size Case 73 In this case, we have

.$$ \begin{array}{rcl}Sample\;SSB&=&\sum_{i=1}^{n_I}M\left\{\bar{Y_i}-(n^{-1}\sum_{k=1}^n\bar{Y_k})\right\}^2\\ \\Sample\;SSW&=&\sum_{i=1}^{n_I}\sum_{j=1}^M(y_{ij}-\bar{Y_i})^2\end{array}$$  Since we have $S^{100}=1$, we have $S^{100}=1$, $S^{100}=1$, $S^{100}=1$, $S^{100}=1$. 
and Sample SST = Sample SSB + Sample SSW. Since the sampling design is the simple random cluster sampling,

$$E(s_b^2)=\frac{1}{N_I-1}\sum_{i=1}^{N_I}\left(\bar{Y_i}-\bar{Y}\right)^2=S_b^2$$  $$E(s_w^2)=\frac{1}{N_I(M-1)}\sum_{i=1}^{N_I}\left(y_{ij}-\bar{Y_i}\right)^2=S_w^2$$  $$\alpha=\alpha_{1,2}$$

and but we do not have E(s 2) = S
2*. In this case, we can use*

$$\hat{\rho}=1-\frac{s_{w}^{2}}{\hat{S}_{y}^{2}}$$  _where_  $$\hat{S}_{y}^{2}=\frac{(N-1)s_{b}^{2}+N(M-1)s_{w}^{2}}{NM}$$ $$\doteq\frac{1}{M}s_{b}^{2}+\left(1-\frac{1}{M}\right)s_{w}^{2}.$$  _In other words, we have_  $$\hat{\rho}=\frac{s_{b}^{2}-s_{w}^{2}}{s_{b}^{2}+(M-1)s_{w}^{2}}.$$

## 6.3 Single-Stage Cluster Sampling: Unequal Size Case

We now consider the case when the cluster sizes Mi **are unequal and we**
are interested in estimating the population total or population mean. If the cluster-level first-order inclusion probability is given by πIi = Pr (i ∈ AI **), the**
HT estimator of the population total is

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i\in A_{I}}{\frac{Y_{i}}{\pi_{I i}}}$$

74 *6. Cluster Sampling 1* and its variance is, under fixed-size cluster sampling,

$$V\left(\hat{Y}_{\mathrm{HT}}\right)=-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}\left(\pi_{I i j}-\pi_{I i}\pi_{I j}\right)\left(\frac{Y_{i}}{\pi_{I i}}-\frac{Y_{j}}{\pi_{I j}}\right)^{2}.$$

The variance is minimized when πIi ∝ Yi. Since we do not know Yi **in practice**
and Yi = MiY¯i, we may use πIi ∝ Mi if Y¯Ii **is believed to be independent of**
Mi.

To formally discuss the problem of optimal choice of the first-order inclusion probability, assume the following superpopulation model yij = µ+ai +eij **(6.9)**
where µ **is an unknown parameter,** ai ∼ (0,σ2a
), and eij ∼ (0,σ2 e
). The total variance of YˆHT **under the model (6.9) is**

$$\begin{array}{r c l}{{V(\hat{Y}_{\mathrm{HT}})}}&{{=}}&{{V\left(\sum_{i\in A_{I}}\pi_{I i}^{-1}M_{i}\mu\right)+E\left(\sum_{i\in A_{I}}\pi_{I i}^{-2}\gamma_{i}\right)}}\\ {{}}&{{=}}&{{V\left(\sum_{i\in A_{I}}\pi_{I i}^{-1}M_{i}\mu\right)+E\left(\sum_{i\in U_{I}}\pi_{I i}^{-1}\gamma_{i}\right),}}\end{array}$$  $\cdot V(Y_{i})=M_{i}^{2}\sigma_{i}^{2}+M_{i}\sigma_{i}^{2}$. The second term of the total v
where γi = V (Yi) = M2 i σ 2a +Miσ e
. The second term of the total variance is minimized when

$$\pi_{Ii}\propto\gamma_{i}^{1/2}=M_{i}\sigma_{a}\left(1+\frac{\sigma_{e}^{2}}{\sigma_{a}^{2}}\cdot\frac{1}{M_{i}}\right)^{1/2}.\tag{6.10}$$

The solution (6.10) is obtained by applying the following Cauchy-Schwartz inequality

$$\left(\sum_{i\in U_{I}}\pi_{I i}^{-1}\gamma_{i}\right)\left(\sum_{i\in U_{I}}\pi_{I i}\right)\geq\left(\sum_{i\in U_{I}}{\sqrt{\gamma}}_{i}\right)^{2}$$

$$(6.11)$$
2
and using that Pi∈UI
πIi **is fixed. Thus, if** σ 2 e /σ2ais small, then πIi ∝ Mi **lead**
to an optimal sampling design. On the other hand, if σ 2 e /σ2a**is large, then**
πIi ∝ M
1/2 i**can be a better design.**
We now consider the situation when the simple random cluster **sampling**
is used in spite of the fact that Mi **are unequal. The HT estimator of the total**
is

$${\hat{Y}}_{\mathrm{HT}}={\frac{N_{I}}{n_{I}}}\sum_{i\in A_{I}}Y_{i}$$
where $Y_{i}=M_{i}Y_{i}$. The variance is 
$$\begin{array}{r c l}{{V_{\mathrm{SRC}}(\hat{Y}_{\mathrm{HT}})}}&{{=}}&{{\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)S_{I}^{2}}}\end{array}$$

6.3 Unequal size cluster sampling 75 where

$$S_{I}^{2}=\frac{1}{N_{I}-1}\sum_{i\in U_{I}}\left(Y_{i}-\bar{Y}_{I}\right)^{2}=\frac{1}{N_{I}-1}\sum_{i\in U_{I}}\left(M_{i}\bar{Y}_{i}-\bar{M}\bar{Y}_{U}\right)^{2},$$

M¯ = N
−1 IPi∈UI Mi, Y¯I = N
−1 IPi∈UI
Yi**, and** Y¯U = YˆI /M¯ .

Since Mi **can be different, we extend the definition of the intracluster**
correlation coefficient to define the cluster homogeneity coefficient as follows:

$$\delta=1-\frac{\sum_{i\in U_{I}}\sum_{j\in U_{i}}\left(y_{ij}-\bar{Y}_{i}\right)^{2}/\left(N-N_{I}\right)}{\sum_{i\in U_{I}}\sum_{j\in U_{i}}\left(y_{ij}-\bar{Y}_{U}\right)^{2}/\left(N-1\right)}=1-\frac{SSW/(N-N_{I})}{SST/(N-1)}.\tag{6.12}$$

If Mi are all equal, then δ **is equal to the intracluster correlation in (6.4).**
Using δ **in (6.12), we can express the variance in (6.11) as**

$$V_{\rm SRIC}\left(\hat{Y}_{\rm HT}\right)=\left(1+\frac{N-N_{I}}{N_{I}-1}\delta\right)\bar{MS}_{y}^{2}K_{I}+C^{*}\cdot K_{I}\tag{6.13}$$  where $K_{I}=\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)$ and 
$$C^{*}=\frac{1}{N_{I}-1}\sum_{i=1}^{N_{I}}\left(M_{i}-\bar{M}\right)M_{i}\bar{Y}_{i}^{2}$$

is the population covariance between Mi and MiY¯ 2 i
. If Y¯ 2 i**are all equal, then**
we have C
∗ = Cov (Mi,Mj **). Roughly speaking, the second term in (6.13) is**
the additional variance due to the unequal cluster sizes.

Now, consider simple random sampling using the same sample size n =
nIM¯ **. In this case, the variance under SRS is**

$$\begin{array}{r c l}{{V_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right)}}&{{=}}&{{\frac{N^{2}}{n_{I}M}\left(1-\frac{n_{I}\bar{M}}{N}\right)S_{y}^{2}}}\\ {{}}&{{=}}&{{\frac{N}{N_{I}}S_{y}^{2}\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)=\bar{M}S_{y}^{2}K_{I}.}}\end{array}$$

Thus, the design effect of the simple random cluster sampling **design is**

$$\mathrm{{\operatorname*{left}={\frac{V_{\mathrm{SRC}}\left({\hat{Y}}_{\mathrm{HT}}\right)}{V_{\mathrm{SRS}}\left({\hat{Y}}_{\mathrm{HT}}\right)}}=\left(1+{\frac{N-N_{I}}{N_{I}-1}}\delta\right)+{\frac{C^{*}}{M S_{y}^{2}}}.}}$$

Therefore, there are two source of having deff > **1 in this case.**
1. δ > 0: The homogeneity of the y **values within the cluster reduces**
efficiency.

2. C
∗ > 0: The variability of cluster size reduces efficiency.

76 *6. Cluster Sampling 1* If Mi = M, then the design effect is equal to 1+ (M −1)δ**, which is consistent**
with the result in (6.8).

We now consider mean estimation under cluster sampling. If the parameter of interest is population mean, we may have two different concepts:

$$\begin{array}{r c l}{{\mu_{1}}}&{{=}}&{{\frac{1}{N_{I}}\sum_{i=1}^{N_{I}}\frac{Y_{i}}{M_{i}}=\frac{1}{N_{I}}\sum_{i=1}^{N_{I}}\bar{Y_{i}}}}\\ {{}}&{{}}&{{}}\\ {{\mu_{2}}}&{{=}}&{{\frac{1}{N}\sum_{i=1}^{N_{I}}Y_{i}=\frac{\sum_{i=1}^{N_{I}}\sum_{j=1}^{M_{i}}y_{i j}}{\sum_{i=1}^{N_{I}}M_{i}}.}}\end{array}$$

If Mi = M, then µ1 = µ2. Otherwise, the two parameters have different meanings. The first parameter µ1 is the cluster-level mean while the second parameter µ2 **is the element-level mean.**
Suppose that we are interested in estimating Y¯U = µ2**. From each sampled**
cluster i**, we observe** Mi,Y¯i
**. We can estimate the mean by a ratio of the**
estimated total of y **to the estimated total size:**

$${\hat{\hat{Y}}}_{R}={\frac{\sum_{i\in A_{I}}Y_{i}/\pi_{I i}}{\sum_{i\in A_{I}}M_{i}/\pi_{I i}}}:={\frac{{\hat{Y}}_{\mathrm{HT}}}{{\hat{N}}_{\mathrm{HT}}}}.$$

Since the ratio is a nonlinear function of two HT estimators, **we use a Taylor** linearization to get the following approximation

$$\frac{\hat{Y}_{\mathrm{HT}}}{\hat{N}_{\mathrm{HT}}}\cong\frac{Y}{N}+\frac{1}{N}\left(\hat{Y}_{\mathrm{HT}}-\frac{Y}{N}\hat{N}_{\mathrm{HT}}\right).$$

Thus, the approximate variance is

$$V\left(\hat{\hat{Y}}_{R}\right)\doteq\frac{1}{N^{2}}\left\{V(\hat{Y}_{\mathrm{HT}})-2\mu C o v(\hat{Y}_{\mathrm{HT}},\hat{N}_{\mathrm{HT}})+\mu^{2}V(\hat{N}_{\mathrm{HT}})\right\}.$$
N2
Under simple random cluster sampling, for example, the variance is

$$\begin{array}{r c l}{{V\left(\hat{\bar{Y}}_{R}\right)}}&{{\doteq}}&{{\frac{N_{I}^{2}}{n_{I}N^{2}}\left(1-\frac{n_{I}}{N_{I}}\right)\frac{1}{N_{I}-1}\sum_{i=1}^{N_{I}}\left(Y_{i}-M_{i}\bar{Y}_{U}\right)^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\frac{1}{n_{I}M^{2}}\left(1-\frac{n_{I}}{N_{I}}\right)\frac{1}{N_{I}-1}\sum_{i=1}^{N_{I}}M_{i}^{2}\left(\bar{Y}_{i}-\bar{Y}_{U}\right)^{2}}}\end{array}$$

with M¯ = N
−1 IPNI
i=1Mi = N/NI **. For variance estimation, we can use**

$$\hat{V}\left(\hat{\bar{Y}}_{R}\right)\quad=\quad\frac{1}{n_{I}M^{2}}\left(1-\frac{n_{I}}{N_{I}}\right)\frac{1}{n_{I}-1}\sum_{i\in A_{I}}M_{i}^{2}\left(\bar{Y}_{i}-\bar{Y}_{U}\right)^{2}.$$

7

# Cluster Sampling: Two-Stage Cluster Sampling

## 7.1 Introduction

In this chapter, we consider two-stage cluster sampling where the sample clusters are selected in the first stage, and the sample elements are selected in the second stage sampling. To formally state this, two-stage sampling can be described as follows:
1. Stage 1: Draw AI ⊂ UI via pI (·) 2. Stage 2: For every i ∈ AI , draw Ai ⊂ Ui via pi (· | AI )
Sample of elements is now given by A = ∪i∈AI Ai.

In two-stage sampling, we have two simplifying assumptions **about the**
second stage sampling design pi(· | AI ):
1. Invariance of the second-stage design pi (· | AI ) = pi (·**) for every**
i ∈ UI and for every AI **such that** i ∈ AI
2. Independence of the second-stage design

$$r\left(A_{i}\mid A_{I}\right)$$
$\frac{1}{2}$
P r ∪i∈AIAi | AI
=
Y
i∈AI
P r (Ai | AI )
Under independence, we have P r(k ∈ Ai,l ∈ Aj ) = P r(k ∈ Ai)P r(l ∈ Aj ), i 6= j.

If the invariance assumption does not hold, the sampling design is called twophase sampling design. The two-phase sampling design will be covered in Chapter 11.

In two-stage sampling, we use nI **to denote the cluster sample size in the**
first-stage sampling and use mi = |Ai| **to denote the sample size in cluster** i.

The number of sampled elements is equal to Pi∈AI
mi = |A|**. The first-order**
inclusion probability of element k in cluster i is a product of the clusterlevel inclusion probability and the conditional inclusion **probability given the**
cluster:
πik = P r {(ik) ∈ A} = P r (k ∈ Ai | i ∈ AI )P r (i ∈ AI ) = πk|iπIi, 78 *Cluster Sampling: Two-stage cluster sampling* where πIi is the cluster-level inclusion probability and πk|i = P r [k ∈ Ai | i ∈ AI ]
is the element-level conditional inclusion probability. In general, πk|iis a random variable (in the sense that it is a function of AI **). Under invariance, it is**
fixed.

The second-order inclusion probability between two elements can be expressed as

$$\pi_{i k,j l}=\left\{\begin{array}{l l}{{\pi_{I i}\pi_{k|i}}}&{{\mathrm{if~}i=j{\mathrm{~and~}}k=l}}\\ {{\pi_{I i}\pi_{k l|i}}}&{{\mathrm{if~}i=j{\mathrm{~and~}}k\neq l}}\\ {{\pi_{I i j}\pi_{k|i}\pi_{l|j}}}&{{\mathrm{if~}i\neq j}}\end{array}\right.$$
where πIij **is the cluster level joint inclusion probability and** πkl|i =
P r [k,l ∈ Ai | i ∈ AI ].

## 7.2 Estimation

In two-stage cluster sampling, we do not observe Yi**. Instead, we obtain**
Yˆi from the second stage sampling such that E(Yˆi | AI ) = Yi**, where the conditional expectation is taken with respect to the second-stage sampling. For**
simplicity, we use E2(Yˆi) = E(Yˆi | AI ).

The HT estimation for Y =Pi∈UI
Yi =Pi∈UI
Pk∈Ui yik **is given by**

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i\in A_{I}}{\frac{{\hat{Y}}_{i}}{\pi_{I i}}}=\sum_{i\in A_{I}}\sum_{k\in A_{i}}{\frac{y_{i k}}{\pi_{k|i}\pi_{I i}}}.$$
$$(7.1)$$
$$(7.2)$$
$$(7.3)$$

The HT estimator in (7.1) is unbiased and its variance can be computed by

$$V\left({\hat{Y}}_{\mathrm{HT}}\right)=V\left\{E\left({\hat{Y}}_{\mathrm{HT}}\mid A_{I}\right)\right\}+E\left\{V\left({\hat{Y}}_{\mathrm{HT}}\mid A_{I}\right)\right\}.$$
o. **(7.2)**
The first term is the variance due to the first-stage sampling (sampling of PSUs) and the second term is the variance due to the second-stage sampling
(sampling of SSUs). Thus, we can write

$$V\left({\hat{Y}}_{\mathrm{HT}}\right)=V_{\mathrm{PSU}}+V_{\mathrm{SSU}}$$
YˆHT= VPSU +VSSU **(7.3)**
where

$$\begin{array}{r c l}{{V_{\mathrm{PSU}}}}&{{=}}&{{V\left\{\sum_{i\in{\cal A}_{I}}\frac{Y_{i}}{\pi_{I i}}\right\}=\sum_{i\in U_{I}}\sum_{j\in U_{I}}\left(\pi_{I i j}-\pi_{I i}\pi_{I j}\right)\frac{Y_{i}}{\pi_{I i}}\frac{Y_{j}}{\pi_{I j}}}}\\ {{V_{\mathrm{SSU}}}}&{{=}}&{{E\left\{\sum_{i\in{\cal A}_{I}}\frac{1}{\pi_{I i}^{2}}V_{i}\right\}=\sum_{i\in U_{I}}\frac{V_{i}}{\pi_{I i}},}}\end{array}$$

Estimation 79

and
$$V_{i}=V\left({\hat{Y}}_{i}\mid A_{i}\right)=\sum_{k\in U_{i}}\sum_{l\in U_{i}}\left(\pi_{k l}|_{i}-\pi_{k|i}\pi_{l|i}\right){\frac{y_{i k}}{\pi_{k|i}}}{\frac{y_{i l}}{\pi_{l}|_{i}}}.$$
Example 7.1. *Consider the following two-stage sampling design.*
1. Stage One: Select nI sample clusters from NI *population clusters by simple random cluster sampling.*
2. Stage Two: Within sampled cluster i, select mi *sample elements* from Mi *population elements independently.*
Under this two-stage sampling, we have

$${\hat{Y}}_{\mathrm{HT}}={\frac{N_{I}}{n_{I}}}\sum_{i\in A_{I}}{\hat{Y}}_{i}=\sum_{i\in A_{I}}\sum_{j\in A_{i}}{\frac{N_{I}}{n_{I}}}{\frac{M_{i}}{m_{i}}}y_{i j}$$

and its variance is

$$V\left(\hat{Y}_{\rm HT}\right)=\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)S_{I}^{2}+\left(\frac{N_{I}}{n_{I}}\right)\sum_{i=1}^{N_{I}}\frac{M_{i}^{2}}{m_{i}}(1-\frac{m_{i}}{M_{i}})S_{i}^{2}\,,\tag{7.4}$$

where

$$\begin{array}{r c l}{{S_{I}^{2}}}&{{=}}&{{(N_{I}-1)^{-1}\sum_{i=1}^{N_{I}}\left(Y_{i}-\bar{Y}_{N}\right)^{2}}}\\ {{}}&{{}}&{{}}\\ {{S_{i}^{2}}}&{{=}}&{{(M_{i}-1)^{-1}\sum_{j=1}^{M_{i}}(y_{i j}-\bar{Y}_{i})^{2}.}}\end{array}$$

Now, consider the estimation of the population mean Y¯ = N −1PNI
i=1 PMi j=1 yij ,
where N =PNI
i=1Mi *is assumed to be known. In this case,*

$${\hat{Y}}_{\mathrm{HT}}={\frac{{\hat{Y}}_{\mathrm{HT}}}{N}}={\frac{N_{I}}{n_{I}N}}\sum_{i\in A_{I}}{\hat{Y}}_{i}={\frac{1}{n_{I}}}\sum_{i\in A_{I}}{\frac{{\hat{Y}}_{i}}{M}},$$

where M¯ = N
−1 IPNI
i=1Mi*. Its variance is, using (7.4),*

V Y ˆ¯HT=1 nI 1− nI NI S 2 q1 + 1 nINIM¯ 2 X NI i=1 M2 i mi 1− mi Mi S 2 2i, where S 2 q1 = (NI − 1)−1PNI i=1(qi − q¯1) 2 with qi = Yi/M¯ , q¯1 = N −1 IPNI i=1 qi, and S 2 2.
2i = (Mi −1)−1Pk∈Ui
(yik −Y¯i)
80 *Cluster Sampling: Two-stage cluster sampling* If the sampling rate for the second stage sampling is constant such that mi/Mi = f2*, then we can write*

$$\begin{array}{r c l}{{V\left(\hat{\hat{Y}}_{\mathrm{HT}}\right)}}&{{=}}&{{\frac{1}{n_{I}}(1-f_{1})S_{q1}^{2}+\frac{1}{n_{I}\bar{m}}(1-f_{2})\frac{1}{N}\sum_{i=1}^{N_{I}}M_{i}S_{2i}^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\frac{1}{n_{I}}(1-f_{1})B^{2}+\frac{1}{n_{I}\bar{m}}(1-f_{2})W^{2}}}\end{array}$$  _where $f_{1}=n_{I}/N_{I}$ and $\bar{m}=N_{I}^{-1}\sum_{i=1}^{N_{I}}m_{i}$._
$$(7.6)$$

Example 7.2. *We now consider a special case of Example 7.1 where* Mi = M
and mi = m*. In this case, (7.4) is further simplified*

$$V\left(\hat{Y}_{\rm HT}\right)=\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)\frac{M\times SSB}{N_{I}-1}+\left(\frac{N_{I}}{n_{I}}\right)\left(1-\frac{m}{M}\right)\frac{M^{2}}{m\left(M-1\right)}SSW\tag{7.5}$$ $$=\frac{N_{I}^{2}}{n}(1-\frac{n_{I}}{N_{I}})MS_{b}^{2}+\left(\frac{N_{I}^{2}}{n_{I}}\right)\left(1-\frac{m}{M}\right)\frac{M^{2}}{m}S_{w}^{2}$$

For the case of mean estimation, we can simply divide (7.5) by N2 = N2 I M2 to get

$$V(\hat{\bar{Y}}_{\mathrm{HT}})=(1-\frac{n_{I}}{N_{I}})\frac{S_{b}^{2}}{n_{I}M}+(1-\frac{m}{M})\frac{S_{w}^{2}}{n_{I}m}$$

Note that the sample size associated with the first term (VP SU *term) is* nIM while the sample size associated with the second term (VSSU *term) is* nIm.

Now, we can express the variance term in (7.6) in terms of the intracluster correlation coefficient. Using (6.5) and (6.6), the variance **term in (7.6) reduces**
to, ignoring nI /NI **term,**

$$V\left(\widehat{Y}_{\rm HT}\right)\doteq\frac{1}{n_{I}M}\left[1+\left(M-1\right)\rho\right]S^{2}+\left(1-\frac{m}{M}\right)\frac{1}{n_{I}m}\left(1-\rho\right)S^{2}\tag{7.7}$$ $$=\frac{S^{2}}{n_{I}m}\left\{1+\left(m-1\right)\rho\right\}.$$  Thus, the design effect becomes $1+\left(m-1\right)\rho$.  
Thus, the design effect becomes 1 + (m−1)ρ.

In this case of Mi = M and mi = m**, the problem of finding the optimal**
choice of m given the cost function C = c0 +c1nI +c2nIm **can be formulated**
as minimizing

$$V\left(\hat{Y}_{\rm HT}\right)=\frac{S_{b}^{2}}{n_{I}M}+(1-\frac{m}{M})\frac{S_{w}^{2}}{n_{I}m}$$ $$=\frac{1}{n_{I}}\left\{\frac{1}{M}\left(S_{b}^{2}-S_{w}^{2}\right)+\frac{1}{m}S_{w}^{2}\right\}$$

subject to C = c0 +c1nI +c2nIm.

Estimation 81 When the total cost C **is fixed, we have**

$$n={\frac{C-c_{0}}{c_{1}+c_{2}m}}$$
and the optimal choice is given by $\varepsilon$
$$m^{*}={\sqrt{\frac{c_{1}}{c_{2}}}}{\frac{M\times S_{w}^{2}}{S_{b}^{2}-S_{w}^{2}}}.$$
. **(7.8)**
The optimal solution (7.8) is obtained by applying

$$(7.8)$$

a m
+bm ≥ 2
√ab with equality if and only if m =
pa/b**. That is, since**

$$\begin{array}{r c l}{{V(\hat{\bar{Y}}_{\mathrm{HT}})\cdot(C-c_{0})}}&{{=}}&{{\left\{\frac{1}{M}\left(S_{b}^{2}-S_{w}^{2}\right)+\frac{1}{m}S_{w}^{2}\right\}(c_{1}+c_{2}m)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\mathrm{const.}+\frac{c_{1}}{m}S_{w}^{2}+\frac{c_{2}}{M}\left(S_{b}^{2}-S_{w}^{2}\right)m,}}\end{array}$$

the lower bound is achieved when

$$m=\left\{c_{1}S_{w}^{2}\right\}^{1/2}\left\{\frac{c_{2}}{M}\left(S_{b}^{2}-S_{w}^{2}\right)\right\}^{-1/2}$$

which equals to (7.8). For sufficiently large M**, the optimal solution becomes**

$$m^{*}\cong{\sqrt{\frac{c_{1}}{c_{2}}({\frac{1}{\rho}}-1)}}.$$

More generally, the objective function can be written as

$$V(\hat{\bar{Y}}_{\mathrm{HT}})=\frac{1}{n_{I}}B^{2}+\frac{1}{n_{I}\bar{m}}(1-f_{2})W^{2}.$$

In this case, the optimal solution becomes

$$m^{*}={\sqrt{\frac{c_{1}}{c_{2}}}}{\frac{W^{2}}{B^{2}-W^{2}/M}}.$$

We now discuss variance estimation under two-stage cluster **sampling.**
Theorem 7.1. *An unbiased estimator for the variance of HT estimator in*
(7.1) under two-stage sampling design is

$$\hat{V}\left(\hat{Y}_{\rm HT}\right)=\sum_{i\in A_{I}}\sum_{j\in A_{I}}\frac{\pi_{Iij}-\pi_{Ii}\pi_{Ij}}{\pi_{Iij}}\frac{\hat{Y}_{i}}{\pi_{Ii}}\frac{\hat{Y}_{j}}{\pi_{Ij}}+\sum_{i\in A_{I}}\frac{1}{\pi_{Ii}}\hat{V}_{i}\tag{7.10}$$
$$(7.9)$$
where Vˆi satisfies E(Vˆi | i ∈ AI ) = V ar(Yˆi | i ∈ AI ).
82 *Cluster Sampling: Two-stage cluster sampling* Proof. **By (7.3),**

$$V\left(\hat{Y}_{\rm HT}\right)=\sum_{i=1}^{N_{I}}\sum_{j=1}^{N_{I}}\left(\pi_{Iij}-\pi_{Ii}\pi_{Ij}\right)\frac{Y_{i}}{\pi_{Ii}}\frac{Y_{j}}{\pi_{Ij}}+\sum_{i=1}^{N_{I}}\frac{V_{i}}{\pi_{Ii}}.\tag{7.11}$$

By the independence assumption,

$$E_{2}\left({\hat{Y}}_{i}{\hat{Y}}_{j}\right)={\left\{\begin{array}{l l}{Y_{i}^{2}+V_{i}}&{{\mathrm{if~}}i=j}\\ {Y_{i}Y_{j}}&{{\mathrm{if~}}i\neq j}\end{array}\right.}$$

where E2(·**) denotes the expectation with respect to the second-stage sampling. Thus,**

$$\begin{array}{r c l}{{\sum_{i\in A_{I}}\sum_{j\in A_{I}}\frac{\pi_{I i j}-\pi_{I i}\pi_{I j}}{\pi_{I i j}}\frac{E_{2}\left(\hat{Y}_{i}\hat{Y}_{j}\right)}{\pi_{I i}\pi_{I j}}}}&{{=}}&{{\sum_{i\in A_{I}}\sum_{j\in A_{I}}\frac{\pi_{I i j}-\pi_{I i}\pi_{I j}}{\pi_{I i j}}\frac{Y_{i}Y_{j}}{\pi_{I i}\pi_{I j}}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{+}}&{{\sum_{i\in A_{I}}\frac{\pi_{I i}-\pi_{I i}^{2}}{\pi_{I i}}\frac{\mathbf{V}_{i}^{2}}{\pi_{I i}^{2}}}}\end{array}$$
and, since $E_{2}\left(\hat{V}_{i}\right)=V_{i}$, we have  $$E_{2}\left\{\hat{V}\left(\hat{Y}_{\rm HT}\right)\right\}=\sum_{i\in A_{I}}\sum_{j\in A_{I}}\frac{\pi_{I i j}-\pi_{I i}\pi_{I j}}{\pi_{I i j}}\frac{Y_{i}Y_{j}}{\pi_{I i}\pi_{I j}}+\sum_{i\in A_{I}}\frac{V_{i}}{\pi_{I i}^{2}}.$$

Taking the expectation of the above term with respect to the first-stage sampling design, it equal to the variance term in (7.11).

The variance estimation formula in (7.10) is the sum of two terms. The first term is the variance estimation formula for the first-stage sampling applied to Yˆi and the second term is the point estimator for the first-stage **sampling** applied to Vˆi**. The validity of the variance estimation formula (7.10) also holds**
even when Yˆi and Vˆi **are obtained from multi-stage sampling. That is, as long**
as E(Yˆi | AI ) = Yi and E(Vˆi | AI ) = V (Yˆi | AI **) hold, the variance estimation**
formula in (7.10) remains unbiased. Such a phenomenon was first discovered by Raj (1966).

If we use only the first term of (7.10)

$${\hat{V}}_{1}=\sum_{i\in A_{I}}\sum_{j\in A_{I}}{\frac{\pi_{I i j}-\pi_{I i}\pi_{I j}}{\pi_{I i j}}}{\frac{{\hat{Y}}_{i}}{\pi_{I i}}}{\frac{{\hat{Y}}_{j}}{\pi_{I j}}},$$

to estimate the total variance, the bias can be written

$$Bias\left(\hat{V}_{1}\right)=-\sum_{i=1}^{N_{I}}V_{i}.\tag{7.12}$$

Estimation 83 and the bias term is of order O(NI ). Since VYˆHT **is of the order** O
n
−1 I N2 I
,

the bias term is negligible when nI /NI = o**(1).**
Under the setup of Example 7.1 where Mi = M, mi = m**, the variance**
estimation formula in (7.10) reduces to  $$\hat{V}\left(\hat{Y}_{\text{HT}}\right)=\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right)\frac{1}{n_{I}-1}\sum_{i\in A_{I}}\left(\hat{Y}_{i}-\frac{1}{n_{I}}\sum_{j\in A_{I}}\hat{Y}_{i}\right)^{2}+\frac{N_{I}}{n_{I}}\sum_{i\in A_{I}}\hat{V}_{i}\tag{7.13}$$  where $\hat{Y}_{i}=M\bar{y}_{i}$ and 
$${\mathrm{where~}}{\hat{Y}}_{i}=M{\bar{y}}_{i}{\mathrm{~and~}}$$
$${\hat{V}}_{i}={\frac{M^{2}}{m}}\left(1-{\frac{m}{M}}\right){\frac{1}{m-1}}\sum_{j\in A_{i}}(y_{i j}-{\bar{y}}_{i})^{2}.$$
In the case of mean estimation, we can divide (7.10) by N2 = N2 I M2**to get**

$$\hat{V}\left(\hat{\hat{Y}}_{\rm HT}\right)=(1-\frac{n_{I}}{N_{I}})\frac{s_{b}^{2}}{n_{I}}+\frac{n_{I}}{N_{I}}(1-\frac{m}{M})\frac{s_{w}^{2}}{n_{I}m}\tag{7.14}$$
where
$$\begin{array}{r c l}{{s_{b}^{2}}}&{{=}}&{{\left(n_{I}-1\right)^{-1}\sum_{i\in A_{I}}\left(\bar{y}_{i}-\hat{\bar{Y}}\right)^{2}}}\\ {{}}&{{}}&{{}}\\ {{s_{w}^{2}}}&{{=}}&{{n_{I}^{-1}\left(m-1\right)^{-1}\sum_{i\in A_{I}j\in A_{i}}\left(y_{i j}-\bar{y}_{i}\right)^{2}.}}\end{array}$$

If f1 = nI /NI **is negligible, then we can use**

$${\hat{V}}\left({\hat{\hat{Y}}}_{\mathrm{HT}}\right)={\frac{s_{b}^{2}}{n_{I}}}$$

as a variance estimator for the mean estimator under simple random sampling.

When the cluster sizes are unequal, simple random sampling in the first stage sampling is not preferable. The following example is a **very popular** method of two-stage sampling in the case of unequal cluster sizes.

Example 7.3. *Consider the following two-stage sampling design.*
1. Stage One: Select clusters (of size nI **) by PPS sampling with**
size measure Mi.

2. Stage Two: Select elements by SRS of size m from Mi **elements**
in the sample cluster i.

We first consider estimation of population total Y =PNI
i=1 PMi j=1 yij*. Under* single-stage cluster sampling, we would have observed Yi =PMi j=1 yij *. In this* case, an unbiased estimator of Y *is given by*

$$\hat{Y}_{\text{PPS}}=\frac{N}{n_{I}}\sum_{k=1}^{n_{I}}\frac{Y_{a_{k}}}{M_{a_{k}}}\tag{7.15}$$

84 *Cluster Sampling: Two-stage cluster sampling* where ak is the index of population cluster in the k-th draw of the PPS sampling. In the two-stage sampling, we do not observe Yi *but we obtain* Yˆi = Miy¯i, where y¯i is the sample mean of elements in the cluster i*. Thus, we can use*

$$\hat{Y}_{\rm PPS}=\frac{N}{n_{I}}\sum_{k=1}^{n_{I}}\frac{\hat{Y}_{a_{k}}}{M_{a_{k}}}=\frac{N}{n_{I}}\sum_{k=1}^{n_{I}}\bar{y}_{a_{k}}\tag{7.16}$$

to estimate the total Y *. Assuming that there is no duplication of the selected* clusters, the sampling weights are all equal to N/(nIm)*, which implies that* every element in the population has the same probability of selection. The sampling design that leads to equal sampling weights is called a self-weighting design.

For estimation of the population mean Y¯ = Y /N*, we have*

$$\hat{Y}_{\text{PPS}}=\frac{1}{n_{I}}\sum_{k=1}^{n_{I}}\bar{y}_{a_{k}}\tag{7.17}$$

which takes the sample mean of the cluster means.

To discuss variance estimation, note that the point estimator (7.16) can be written as the sample mean of z1,··· ,znI where zk **are independently and**
identically distributed with the following discrete distribution:

_with probability $p_i=M_i/N,\ i=1,\cdots,N_I$._
$$z_{1}={\hat{Y}}_{i}/p_{i}$$
z1 = Yˆi/pi with probability pi = Mi*/N, i* = 1,··· ,NI .
Note that E(z1) = PNI
i=1 Yˆi*, which is unbiased for* Y =PNI
i=1 Yi as E2(Yˆi) = Yi.

For variance estimation, since YˆPPS *in (7.16) can be written as the mean of* nI independent sample of zk*s, we have*

$${\hat{V}}_{\mathrm{PPS}}\left({\hat{Y}}_{\mathrm{PPS}}\right)={\frac{1}{n_{I}}}S_{z}^{2}={\frac{1}{n_{I}}}{\frac{1}{n_{I}-1}}\sum_{k=1}^{n_{I}}(z_{k}-{\bar{z}})^{2}\,.$$
$$(7.18)$$
$$(7.19)$$
2. **(7.18)**
Variance estimation of the mean estimator (7.17) can be similarly constructed. Specifically, we can use

$${\hat{V}}_{\mathrm{PPS}}\left({\hat{Y}}_{\mathrm{PPS}}\right)={\frac{1}{n_{I}}}{\frac{1}{n_{I}-1}}\sum_{k=1}^{n_{I}}\left({\bar{y}}a_{k}-{\hat{Y}}_{\mathrm{PPS}}\right)^{2}$$
ˆ¯PPS2**(7.19)**
as an unbiased estimator for the variance of the mean estimator (7.17).

To illustrate the use of two-stage sampling in Example 7.3, consider a finite population of households in a city. The city consists of NI **clusters of houses,**
and the cluster i consists of Mi **houses. We used the following two-stage cluster**
sampling.

[Stage 1] Select nI **= 3 sample clusters by the PPS sampling with the measure**
of size equal to Mi.

Estimation 85
[Stage 2] Within each selected cluster i, select mi **= 4 sample houses by simple**
random sampling.

Once the sample households are selected, we obtain two information. One is the number of household members in the house (tij **) and the other is the** number of household members under 6 years of age (yij**). We are interested**
in estimating the proportion of the population with age under 6 in the city. That is, the parameter of interest is

$$P={\frac{\sum_{i=1}^{N_{I}}\sum_{j=1}^{M_{i}}y_{i j}}{\sum_{i=1}^{N_{i}}\sum_{i=1}^{M_{i}}t_{i j}}}:={\frac{Y}{T}}.$$





The following table gives the summary of the realized sample **household**
from the above two-stage sampling.

TABLE 7.1



 An illustrative example of two-stage cluster sample

Sample Cluster ID **Sample household ID** tij yij

1 1 8 2 1 2 7 2 1 3 7 1 1 4 6 1 2 1 8 0 2 2 12 1 2 3 10 3 2 4 11 1 3 1 4 2 3 2 5 3 3 3 5 2 3 4 6 1

The proportion of the population with age under 6 in the city is estimated by

$${\hat{P}}={\frac{{\hat{Y}}}{{\hat{T}}}}={\frac{N n_{I}^{-1}\sum_{k=1}^{n_{I}}{\bar{y}}_{k}}{N n_{I}^{-1}\sum_{k=1}^{n_{I}}{\bar{t}}_{k}}}={\frac{6/4+5/4+8/4}{28/4+41/4+20/4}}\doteq0.213$$

where the second equality follows from (7.16). To estimate the variance of Pˆ,
we use

$${\hat{V}}({\hat{P}})={\frac{1}{n_{I}}}{\frac{1}{n_{I}-1}}\left({\frac{1}{n_{I}}}\sum_{i=1}^{n_{I}}{\bar{t}}_{i}\right)^{-2}\sum_{i=1}^{n_{I}}({\bar{y}}_{i}-{\hat{\theta}}{\bar{t}}_{i})^{2}=0.005302.$$

The design effect can be computed by the ratio of Vˆ (Pˆ) under the current 86 *Cluster Sampling: Two-stage cluster sampling* sampling design to the variance of Pˆ **under simple random sampling, which is**
computed by

$${\hat{V}}_{\mathrm{SRS}}({\hat{p}})={\frac{1}{n}}{\hat{p}}(1-{\hat{p}})=\left(\sum_{i=1}^{n_{I}}\sum_{j=1}^{m_{i}}t_{i j}\right)^{-1}{\hat{p}}(1-{\hat{p}})=0.001887.$$

Thus, the estimated design effect is 0.005302/0.001887 = 2.8105.

## Estimation: Part 1 8.1 Introduction

So far, we have considered HT estimators for various sampling designs. HT
estimator is design-unbiased but does not necessarily achieve small variance. To improve the efficiency of the resulting estimator, auxiliary information is often incorporated into the estimation if the population total of the auxiliary variable is known from external sources. An estimator is called a linear estimator if it is a linear function of the sample observations of y**. That is,**

$${\hat{Y}}=\sum_{i\in A}w_{i}y_{i}$$
$$(8.1)$$
wiyi **(8.1)**
for some wi ≥ 0 that does not depend on y. If zi = xi + yi**, then the linear**
estimator applied to z satisfies Zˆ = Xˆ + Yˆ **. This property is called internal**
consistency. HT estimator is the only linear estimator that **is design unbiased.**
If auxiliary variable xi **is observed in the sample and the population total**
of xi **is known from an external source such as census or administrative data,**
we may want to achieve
$$\sum_{i\in A}w_{i}{\bf x}_{i}=\sum_{i=1}{\bf x}_{i}.\tag{8.2}$$
N
Property (8.2) is sometimes called external consistency. We will consider two examples of estimators satisfying (8.2). One is the ratio estimator, and the other is the regression estimator.

## 8.2 Ratio Estimation

Suppose that a scalar auxiliary variable xi **is available whose population**
total X =PN
i=1 xi **is known from an external source. In this case, the HT**
estimator of X, XˆHT =Pi∈A π
−1 ixi is not necessarily equal to X**. We can use**
8 88 *Estimation: Part 1* X **information to modify the HT estimator to get**

$${\hat{Y}}_{\mathrm{R}}=X{\frac{{\hat{Y}}_{\mathrm{HT}}}{{\hat{X}}_{\mathrm{HT}}}}.$$
$$(8.3)$$

Thus, ratio estimator is computed by multiplying Xˆ −1 HTX **to HT estimator of** Y
and Xˆ −1 HTX **is sometimes called ratio adjustment factor. The ratio adjustment**
factor is close to one, but not necessarily equal to one. If the realized sample satisfies XˆHT < X**, then the ratio adjustment factor is greater than one and**
YˆR > YˆHT**. In this case, the HT estimator is inflated by the ratio adjustment**
factor.

Ratio estimator is a linear estimator of the form in (8.1) and **the weight is**

$$w_{i}=\frac{1}{\pi_{i}}\times\frac{X}{\hat{X}_{\rm HT}}.\tag{8.4}$$

Thus, the final weight is computed by a product of the design weight π
e design weight $\pi_i^{-1}$ and 
the ratio adjustment factor.
We now consider the statistical properties of the ratio estimator. Note that
the ratio estimator is a nonlinear function of XˆHT and YˆHT**. Thus,**
$$E\left({\frac{{\hat{Y}}_{\mathrm{HT}}}{{\hat{X}}_{\mathrm{HT}}}}\right)\neq{\frac{E\left({\hat{Y}}_{\mathrm{HT}}\right)}{E\left({\hat{X}}_{\mathrm{HT}}\right)}}$$
and the ratio estimator is not design unbiased for Y **. To discuss the bias of** the ratio estimator, define

$${\hat{R}}={\frac{{\hat{Y}}_{\mathrm{HT}}}{{\hat{X}}_{\mathrm{HT}}}}$$
and
$$R={\frac{E\left({\hat{Y}}_{\mathrm{HT}}\right)}{E\left({\hat{X}}_{\mathrm{HT}}\right)}}.$$

The bias of Rˆ as an estimator of R is equal to E(Rˆ)−R **and it is often called**
ratio bias. To discuss ratio bias, note that

$$\begin{array}{r c l}{{C o v\left({\hat{R}},{\hat{X}}_{\mathrm{HT}}\right)}}&{{=}}&{{E\left({\hat{R}}{\hat{X}}_{\mathrm{HT}}\right)-E\left({\hat{R}}\right)E\left({\hat{X}}_{\mathrm{HT}}\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{E\left({\hat{Y}}_{\mathrm{HT}}\right)-E\left({\hat{R}}\right)E\left({\hat{X}}_{\mathrm{HT}}\right).}}\end{array}$$

Dividing both sides of the above equation by −E

$\boldsymbol{\gamma}-E\left(\hat{X}_{\text{HT}}\right)$, we. 
$$B i a s\left({\hat{R}}\right)=-{\frac{C o v\left({\hat{R}},{\hat{X}}_{\mathrm{HT}}\right)}{E\left({\hat{X}}_{\mathrm{HT}}\right)}}$$
$$(8.5)$$
Ratio Estimation 89

and so
$$B i a s\left(\hat{Y}_{R}\right)=-C o v\left(\hat{R},\hat{X}_{\mathrm{HT}}\right).$$
Even if the ratio estimator is biased, but if the bias is smaller order than its standard error, the bias can be negligible. Generally speaking, we can express
$$\frac{\hat{\theta}-\theta}{\sqrt{V\left(\hat{\theta}\right)}}=\frac{\hat{\theta}-E\left(\hat{\theta}\right)}{\sqrt{V\left(\hat{\theta}\right)}}+R.B.(\hat{\theta})\tag{8.6}$$
where

$$R.B.({\hat{\theta}})={\frac{B i a s({\hat{\theta}})}{\sqrt{V({\hat{\theta}})}}}$$

is the relative bias of ˆθ**. The first term on the right hand side of (8.6) converges**
to the standard normal distribution by the central limit theorem. Thus, when the second term converges to zero, the bias term can be safely **ignored. We** formalize the concept in the following definition.

Definition 8.1. *Bias*(
ˆθ) *is negligible*

 $$(\hat{\theta})=\frac{Bias(\hat{\theta})}{\sqrt{V(\hat{\theta})}}\to0\quad as\quad n\to\infty.$$  since ... 
In addition, since

$${\frac{\mathrm{MSE}\left({\hat{\theta}}\right)}{V({\hat{\theta}})}}=1+\left[R.B.({\hat{\theta}})\right]^{2},$$

the MSE of ˆθ **is approximately equal to** V (
ˆθ) if the bias of ˆθ **is negligible.**
Now, to discuss the relative bias of the ratio estimator, first note that the relative bias of the ratio estimator is equal to the relative bias of R**ˆ. Thus, by**
(8.5), we have

$$R.B.(\hat{Y}_{R})\Big{|}=\left|R.B.(\hat{R})\right|=\left|Corr\left(\hat{R},\hat{X}_{\rm HT}\right)\frac{\sqrt{V(\hat{X}_{HT})}}{E\left(\hat{X}_{HT}\right)}\right|\leq CV\left(\hat{X}_{HT}\right),\tag{8.7}$$

where CV (
ˆθ) = qV (
ˆθ)/E(
ˆθ**) is the coefficient of variation. For example, under**
simple random sampling,

$$C V\left({\hat{X}}_{\mathrm{HT}}\right)={\sqrt{\frac{1}{n}\left(1-{\frac{n}{N}}\right)}}{\frac{S_{x}}{\bar{X}}}.$$

Thus, the bias of the ratio estimator of negligible if one of the following conditions holds:
90 *Estimation: Part 1* 1. n **is large** 2. n/N **is large (close to one)**
3. CV (x) = Sx/X¯ **is small.**
For general sampling designs other than SRS, CV (XˆHT**) will converge to zero**
as n **increases and the bias of the ratio estimator is negligible.**
To further discuss relative bias of the ratio estimator, we use the second order Taylor expansion to get

$$\widehat{Y}_{R}\cong\bar{Y}+\left(\widehat{Y}_{\rm HT}-\bar{Y}\right)-R\left(\widehat{X}_{\rm HT}-\bar{X}\right)$$ $$-\bar{X}^{-1}\left[\left(\widehat{X}_{\rm HT}-\bar{X}\right)\left(\widehat{Y}_{\rm HT}-\bar{Y}\right)-R\left(\widehat{X}_{\rm HT}-\bar{X}\right)^{2}\right],$$
where $\widehat{\widehat{Y}}_{R}=N^{-1}\widehat{Y}_{R}$, $\widehat{\widehat{X}}_{\rm HT}=N^{-1}\widehat{X}_{\rm HT}$, and $\widehat{\widehat{Y}}_{\rm HT}=N^{-1}\widehat{Y}_{\rm HT}$. Thus,
$$\begin{split}Bias\left(\widehat{\widehat{Y}}_{R}\right)\doteq-\bar{X}^{-1}\left[Cov\left(\widehat{\widehat{X}}_{\rm HT},\widehat{\widehat{Y}}_{\rm HT}\right)-R\cdot V\left(\widehat{\widehat{X}}_{\rm HT}\right)\right].\end{split}\tag{8.9}$$

Note that the leading term of the bias of the ratio estimator is of order n
−1.

Next, we consider the variance of the ratio estimator. By (8.8), we obtain

$$\widehat{\widehat{Y}}_{R}=\widehat{Y}+\left(\widehat{\widehat{Y}}_{\mathrm{HT}}-R\widehat{\widehat{X}}_{\mathrm{HT}}\right)+O_{p}\left(n^{-1}\right),$$

where ˆθn = Op(1) denotes that ˆθn **is bounded in probability. Ignoring** Op(n
−1)

terms, we have
$$\mathrm{V}({\widehat{\hat{Y}}}_{R}-{\bar{Y}})\cong\mathrm{V}\left({\widehat{\hat{Y}}}_{\mathrm{HT}}-R{\widehat{\hat{X}}}_{\mathrm{HT}}\right).$$
b¯ HT. **(8.11)**
Therefore, the ratio estimator is better than the HT estimator if

$$-2R\cdot C o v\left(\widehat{\widehat{Y}}_{\mathrm{HT}},\widehat{\widehat{X}}_{\mathrm{HT}}\right)+R^{2}\mathrm{V}\left(\widehat{\widehat{X}}_{\mathrm{HT}}\right)<0,$$

which reduces to, under the simple random sampling,

$$\frac{1}{2}\frac{C V\left(x\right)}{C V\left(y\right)}<C o r r\left(x,y\right).$$
$$(8.12)$$

That is, under (8.12), the ratio estimator is more efficient than the HT estimator under SRS.

For variance estimation, using (8.11), we may use

$$\sum_{i\in A j\in A}{\frac{\pi_{i j}-\pi_{i}\pi_{j}}{\pi_{i j}}}{\frac{y_{i}-R x_{i}}{\pi_{i}}}{\frac{y_{j}-R x_{j}}{\pi_{j}}}.$$

However, since we do not know R, we use Rˆ **to obtain**

$$\hat{V}\left(\hat{Y}_{R}\right)=\sum_{i\in A}\sum_{j\in A}\frac{\pi_{ij}-\pi_{i}\pi_{j}}{\pi_{ij}}\frac{y_{i}-\hat{R}x_{i}}{\pi_{i}}\frac{y_{j}-\hat{R}x_{j}}{\pi_{j}}\tag{8.13}$$

Ratio Estimation 91 as a variance estimator.

We now introduce Hajék estimator of the population mean as a special case of the ratio estimator. Hajék estimator uses xi **= 1 in the ratio estimator.**
That is,

$$\hat{Y}_{\pi}=\frac{\sum_{i\in A}\pi_{i}^{-1}y_{i}}{\sum_{i\in A}\pi_{i}^{-1}}\tag{8.14}$$  $\hat{Y}_{\pi}=\frac{\sum_{i\in A}\pi_{i}^{-1}y_{i}}{\sum_{i\in A}\pi_{i}^{-1}}$ (8.14)  $\hat{Y}_{\pi}=\frac{\sum_{i\in A}\pi_{i}^{-1}y_{i}}{\sum_{i\in A}\pi_{i}^{-1}}$ (8.14) 
is the Hajék estimator of the population mean and is often more efficient than the HT estimator Yb¯ HT = N −1Pi∈A π
−1 iyi**. Using (8.10), we can obtain**

$$\hat{\bar{Y}}_{\pi}=\bar{Y}+N^{-1}\sum_{i\in A}\pi_{i}^{-1}\left(y_{i}-\bar{Y}\right)+O_{p}\left(n^{-1}\right).$$

Thus, the variance of the Hajék estimator is obtained using yi −Y¯ **instead of**
yi **in the variance formula for the HT estimator.**
In some cases, ratio itself is a parameter of interest. Domain estimation is an example of using a ratio for parameter estimation. Suppose that we are interested in the mean of y in a particular domain D**. That is, the parameter** of interest is

$$\bar{Y}_D=\frac{\sum_{i=1}^N z_i y_i}{\sum_{i=1}^N z_i}$$  $$z_i=\left\{\begin{array}{ll}1&\mbox{if}i\in D\\ 0&\mbox{if}i\notin D.\end{array}\right.$$  e  ... 
$$\begin{array}{c c}{{-}}&{{\sum_{i=1}^{N}z_{i}}}\\ {{\mathrm{where}}}&{{}}\\ {{z_{i}=\left\{\begin{array}{l l}{{1}}&{{\mathrm{if}\ i\in D}}\\ {{0}}&{{\mathrm{if}\ i\notin D.}}\end{array}\right.}}\end{array}$$  To estimate $\bar{Y}_{D}$, we use  $$\widehat{Y}_{D,\pi}=\frac{\sum_{i\in A}\pi_{i}^{-1}z_{i}y_{i}}{\sum_{i\in A}\pi_{i}^{-1}z_{i}}.$$  By the Taylor linearization, we have 
$$\bar{Y}_{D,\pi}=\bar{Y}_{D}+N_{D}^{-1}\sum_{i\in A}\pi_{i}^{-1}z_{i}\left(y_{i}-\bar{Y}_{D}\right)+O_{p}\left(n^{-1}\right)$$
where $N_{D}=\sum_{i=1}^{N}z_{i}$. Under SRS,
$$\mathrm{V}(\widehat{Y}_{D,\pi})\doteq\frac{1}{n}(1-f)\left(\frac{N}{N_{d}}\right)^{2}\frac{1}{N-1}\sum_{i=1}^{N}z_{i}(y_{i}-\bar{Y}_{D})^{2}$$ $$=\frac{1}{n}(1-f)\left(\frac{N}{N_{d}}\right)^{2}\frac{N_{d}-1}{N-1}S_{D}^{2},$$  where $S_{D}^{2}=(N_{D}-1)^{-1}\sum_{i\in D}(y_{i}-\bar{Y}_{D})^{2}.$ If the sample size is large such that  $$\frac{n_{D}}{n}\cong\frac{N_{D}}{N}\cong\frac{N_{D}-1}{N-1}$$

92 *Estimation: Part 1*

holds, we have $$\mathrm{V}(\widehat{Y}_{D,\pi})\doteq\frac{1}{n_D}(1-f)S_D^2$$ where $S_D^2$ is estimated by $s_D^2=\left(n_D-1\right)^{-1}\sum_{i\in A}z_i\left(y_i-\bar{y}_D\right)^2$. 

## 8.3 Regression Estimation

Ratio estimator is useful when there is strong positive correlation between x and y**. If the correlation is negative, the ratio estimator is actually worse** than using the HT estimator. Also, ratio estimator is not directly applicable for the vector x **cases. To overcome such limitation, we consider regression**
estimation in this section.

Suppose that the auxiliary information for unit i is denoted by a pdimensional vector xi **and its population total** X =PN
i=1 xi **is available. In the**
sample, we observe xi and yi**. In this case, regression estimator of** Y =PN
i=1 yi is defined as follows:

$$\hat{Y}_{\rm reg}=\sum_{i=1}^{N}\hat{y}_{i}\tag{8.15}$$

where ˆyi = x
′
iBˆ and

$${\hat{B}}=\left(\sum_{i\in A}\pi_{i}^{-1}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\sum_{i\in A}\pi_{i}^{-1}\mathbf{x}_{i}y_{i}.$$

If Pi∈A π
−1 ixix
′
i is singular, then its inverse does not exist. In such case, one may use the generalized inverse and still define regression estimator accordingly. For estimation of the population mean Y¯ = N −1PN
i=1 yi**, the regression**
estimator of Y¯ **is defined by**

$$\hat{\hat{Y}}_{\mathrm{reg}}=N^{-1}\sum_{i=1}^{N}{\bf x}_{i}^{\prime}\hat{B}=\bar{\bf X}^{\prime}\hat{B},$$
$$(8.16)$$

where X¯ = N −1PN
i=1 xi.

In many cases, xi includes an intercept term. If we write xi = (1,xi1**), the**
regression estimator in (8.15) reduces to

$${\bar{Y}}_{\mathrm{reg}}={\hat{B}}_{0}+{\bar{\mathbf{X}}}_{1}^{\prime}{\hat{B}}_{1}$$
Y¯reg = Bˆ0 + X¯ ′1Bˆ1 **(8.17)**
where $\tilde{\mathbf{X}}_{1}=N^{-1}\sum_{i=1}^{N}\mathbf{x}_{i1}$,  $$\hat{B}_{0}=\left(\sum_{i\in A}\pi_{i}\right)^{-1}\sum_{i\in A}\pi_{i}^{-1}\left(y_{i}-\mathbf{x}_{1i}^{\prime}\hat{B}_{1}\right)$$
$$(8.17)$$

Regression Estimation 93

$${\hat{B}}_{1}=\left[\sum_{i\in A}\pi_{i}^{-1}\left(\mathbf{x}_{i1}-{\hat{\mathbf{X}}}_{\pi1}\right)\left(\mathbf{x}_{i1}-{\hat{\mathbf{X}}}_{\pi1}\right)^{\prime}\right]^{-1}\sum_{i\in A}\pi_{i}^{-1}\left(\mathbf{x}_{i1}-{\hat{\mathbf{X}}}_{\pi1}\right)y_{i}.$$
$$(8.18)$$

Before we discuss statistical properties of the regression **estimator, we**
briefly discuss some algebraic properties of the regression **estimator. First,**
regression estimator is a linear estimator. That is, we can express the regression estimator in (8.15) as the linear form in (8.1) with

$$w_{i}={\bar{\mathbf{X}}}^{\prime}\left(\sum_{i\in A}\pi_{i}^{-1}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\pi_{i}^{-1}\mathbf{x}_{i}.$$
i xi. **(8.18)**
Note that the weights satisfy

$$\sum_{i\in A}w_{i}\mathbf{x}_{i}=\bar{\mathbf{X}}.\tag{1}$$
$$(8.19)$$

Thus, regression estimator satisfies the external consistency discussed in (8.2). Property (8.19) is also called calibration property or *benchmarking property* in the survey literature (Deville and Särndal, 1992). If the **intercept term**
is included in xi, then Pi∈A wi **= 1 holds and the regression estimator is**
location-scale invariant. That is,

$$\sum_{i\in A}w_{i}\left(a+b y_{i}\right)=a+b\sum_{i\in A}w_{i}y_{i}.$$

We now discuss statistical properties of the regression estimator. First assume that the sampling design and the HT estimators are such that

$$N^{-1}\left(\sum_{i\in A}\pi_{i}^{-1}{\bf z}_{i}{\bf z}_{i}^{\prime}-\sum_{i=1}^{N}{\bf z}_{i}{\bf z}_{i}^{\prime}\right)=O_{p}\left(n^{-1/2}\right)\tag{8.20}$$

where z
′
i = (x
′
i
,yi**). Condition (8.20) means that the HT estimator of the**
population means converge in probability to their population mean and the order of convergence of the same as that of the sample mean in the IID case.

The following lemma dervies Taylor linearization of the regression estimator.

Lemma 8.1. *Under (8.20), the regression estimator satisfes*

$$\bar{Y}_{\rm reg}=\bar{\bf X}^{\prime}B+\bar{X}^{\prime}\left(\sum_{i=1}^{N}{\bf x}_{i}{\bf x}_{i}^{\prime}\right)^{-1}\sum_{i\in A}\pi_{i}^{-1}{\bf x}_{i}\left(y_{i}-{\bf x}_{i}^{\prime}B\right)+O_{p}\left(n^{-1}\right)\tag{8.21}$$  _where $B=\left(\sum_{i=1}^{N}{\bf x}_{i}{\bf x}_{i}^{\prime}\right)^{-1}\sum_{i=1}^{N}{\bf x}_{i}y_{i}$._
and Proof. Let

94 **Estimation: Part 1**
$$\begin{array}{r c l}{{}}&{{}}&{{}}\\ {{}}&{{}}&{{}}\\ {{\left(\hat{\mathbf{C}},\hat{\mathbf{d}}\right)}}&{{=}}&{{\sum_{k\in A}\pi_{k}^{-1}\left(\mathbf{x}_{k}\mathbf{x}_{k}^{\prime}\mathbf{x}_{k}y_{k}\right)}}\\ {{}}&{{}}&{{}}\end{array}$$
$$\mathrm{and}$$
$$\begin{array}{r c l}{{(\mathbf{C},\mathbf{d})}}&{{=}}&{{\sum_{k=1}^{N}\left(\mathbf{x}_{k}\mathbf{x}_{k}^{\prime},\mathbf{x}_{k}y_{k}\right).}}\end{array}$$

The estimated regression coefficient Bˆ **can be written as**
Bˆ = f Cˆ ,dˆ
= Cˆ −1dˆ.

To compute Taylor linearization of vector Bˆ , let ˆcij be the (*i, j***)-th element**
of Cˆ and let ˆdi be the i-th element of ˆdi. Taylor linearization of Bˆ **can be**
expressed as

$$f\left(\mathbf{C},\mathbf{d}\right)\simeq f\left(\mathbf{C},\mathbf{d}\right)+\sum_{i}\left(\frac{\partial f}{\partial d_{i}}\right)\left(\hat{d}_{i}-d_{i}\right)+\sum_{i}\sum_{j}\left(\frac{\partial f}{\partial c_{ij}}\right)\left(\hat{c}_{ij}-c_{ij}\right).\tag{8.32}$$
$$(8.22)$$
Here, we have
$${\frac{\partial f}{\partial d_{i}}}=\mathbf{C}^{-1}\mathbf{e}_{i},$$

where ei is a vector where the i**-th element is 1 and the remaining elements**
are 0. Also,

$${\frac{\partial f}{\partial c_{i j}}}=-\mathbf{C}^{-1}E_{i j}\mathbf{C}^{-1}\mathbf{d}$$

where Eij = eie
′ j is a matrix where the (*i, j***)th element is 1 and the remaining**
elements are zero. Thus, (8.22) reduces to

$$\begin{array}{r l}{f\left({\hat{\mathbf{C}}},{\hat{\mathbf{d}}}\right)}&{{}\cong}&{{}f\left(\mathbf{C},\mathbf{d}\right)+\mathbf{C}^{-1}\left({\hat{\mathbf{d}}}-\mathbf{d}\right)-\mathbf{C}^{-1}\left[{\hat{\mathbf{C}}}-\mathbf{C}\right]\mathbf{C}^{-1}\mathbf{d}}\\ {}&{{}}&{{}}\\ {}&{{}}&{{=}}&{{\mathbf{B}+\mathbf{C}^{-1}\left({\hat{\mathbf{d}}}-{\hat{\mathbf{C}}}\mathbf{B}\right),}}\end{array}$$

which proves (8.21).

If xi **includes 1, we can write** a
′xi = 1 for some a **which implies** Xa = 1N
(where 1N is a vector of ones with length N**). Thus,**

$${\bar{\mathbf{X}}}^{\prime}\left(\sum_{i=1}^{N}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}=N^{-1}\left(\mathbf{1}_{N}^{\prime}X\right)\left(X^{\prime}X\right)^{-1}=N^{-1}\mathbf{a}^{\prime}X\left(X^{\prime}X\right)^{-1}=N^{-1}\mathbf{a}^{\prime},$$

Regression Estimation 95

and
$${\bar{\mathbf{X}}}^{\prime}B={\bar{Y}}\,.$$
Thus, (8.21) reduces to
$$\widehat{\bar{Y}}_{\mathrm{reg}}=\bar{Y}+N^{-1}\sum_{i\in A}\pi_{i}^{-1}\left(y_{i}-{\bf x}_{i}^{\prime}B\right)+O_{p}\left(n^{-1}\right),$$
−1, **(8.23)**
which implies that

$$\widehat{\bar{Y}}_{\mathrm{reg}}-\bar{Y}=N^{-1}\sum_{i\in A}\pi_{i}^{-1}(y_{i}-{\bf x}_{i}^{\prime}B)+o_{p}(n^{-1/2}).$$

The leading term is unbiased to zero. The asymptotic variance of the regression estimator is then

$$V\left({\widehat{\tilde{Y}}}_{\mathrm{reg}}\right)\doteq V\left\{N^{-1}\sum_{i\in A}\pi_{i}^{-1}e_{i}\right\}=\sum_{i\in U}\sum_{j\in U}\left(\pi_{i j}-\pi_{i}\pi_{j}\right){\frac{e_{i}\ e_{j}}{\pi_{i}\ \pi_{j}}},$$
, **(8.24)**
where ei = yi −x
′
iB.

Under SRS, the asymptotic variance can be written

$$\begin{array}{r c l}{{V\left(\widehat{\widehat{Y}}_{\mathrm{reg}}\right)}}&{{\doteq}}&{{\frac{1}{n}\left(1-\frac{n}{N}\right)\frac{1}{N-1}\sum_{i=1}^{N}\left(y_{i}-\mathbf{x}_{i}^{\prime}B\right)^{2},}}\end{array}$$
$$(8.23)$$
$$(8.24)$$
$$(8.25)$$
2, **(8.25)**
which leads to
$$V\left({\hat{\bar{Y}}}_{\mathrm{reg}}\right)\doteq V\left({\bar{y}}\right)\times\left(1-R^{2}\right)$$. 
where R2is the coefficient of determination for the regression of y on x **in the**
population level. Thus, the regression estimator is efficient if R2**is large, i.e.,**
when there is a strong linear relationship between y and x**. If the regression**
relation does not hold, the regression estimator is still asymptotically unbiased. Thus, the regression estimator is model-assisted, not model-dependent
(Särndal et al., 1992).

To estimate the asymptotic variance in (8.24), we use

$${\hat{V}}\left({\hat{Y}}_{\mathrm{reg}}\right)=\sum_{i\in A}\sum_{j\in A}{\frac{\pi_{i j}-\pi_{i}\pi_{j}}{\pi_{i j}}}{\frac{y_{i}-{\hat{B}}x_{i}}{\pi_{i}}}{\frac{y_{j}-{\hat{B}}x_{j}}{\pi_{j}}}.$$

Next, we consider post-stratification which is a special case of regression estimation. Suppose that the finite population is partitioned into G **mutually**
exclusive and exhaustive groups. Assume that Ng**, the population size of group**
g, are known for all g = 1,··· ,G**. In this case, the auxiliary information can**
be written as xi = (xi1,xi2,··· ,xiG)
′ where xig **is the indicator function for**
group g**. The regression estimator is**

$$\hat{Y}_{\rm reg}=\sum_{i=1}^{N}{\bf x}_{i}^{\prime}\left(\sum_{i\in A}\pi_{i}^{-1}{\bf x}_{i}{\bf x}_{i}^{\prime}\right)^{-1}\sum_{i\in A}\pi_{i}^{-1}{\bf x}_{i}y_{i}.\tag{8.26}$$

96 *Estimation: Part 1* Since

X N i=1 x ′ i = (N1,N2,··· ,NG) ′ i∈A π −1 i xix ′ i = diagNˆ1,Nˆ2,··· ,NˆG  X
where $\hat{N}_g=\sum_{i\in A}\pi_i^{-1}$
−1 ixig**, the regression estimator reduces to**

$${\hat{Y}}_{\mathrm{post}}=\sum_{g=1}^{G}\sum_{i\in A_{g}}\pi_{i}^{-1}{\frac{N_{g}}{{\hat{N}}_{g}}}y_{i}$$
yi **(8.27)**
where Ag is the set of sample indices in group g**. Thus, the final weights in**
post-stratified estimator are obtained by multiplying the design weight by the adjustment factor Nˆ −1 g Ng. Since xi **includes one, we can use (8.24) to obtain**

$$V\left(\hat{Y}_{\mathrm{post}}\right)=V\left\{\sum_{g=1}^{G}\sum_{i\in A_{g}}\pi_{i}^{-1}\left(y_{i}-\bar{Y}_{g}\right)\right\}+o\left(n^{-1}\right).$$
$$(8.27)$$
$$(8.28)$$
−1. **(8.28)**
Under SRS, the variance is

$$\begin{array}{r c l}{{V\left(\hat{Y}_{\mathrm{post}}\right)}}&{{\doteq}}&{{\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\frac{1}{N-1}\sum_{g=1}^{G}\sum_{i\in U_{g}}\left(y_{i}-\bar{Y}_{g}\right)^{2}}}\end{array}$$
$$(8.29)$$
2**(8.29)**
which is asymptotically equal to the variance of stratified sampling under proportional allocation.

Example 8.1. *(Raking ratio estimation)*
Suppose that we have I ×J groups or cells. Cell counts Nij **are not known.**
Marginal counts Ni· =PJ
j=1 Nij and N·j =PI
i=1 Nij **are known. In this case,**
we may consider the following two-way additive model

$$\begin{array}{r c l}{{E_{\zeta}\left(Y_{k}\right)}}&{{=}}&{{\alpha_{i}+\beta_{j}}}\\ {{V_{\zeta}\left(Y_{k}\right)}}&{{=}}&{{\sigma^{2}}}\end{array}$$

where αi, βj*, and* σ 2 *are unknown parameters. Define*

$$\delta_{i j k}=\left\{\begin{array}{l l}{{1}}&{{\quad i f\;k\in U_{i j}}}\\ {{0}}&{{\quad o t h e r w i s e\;.}}\end{array}\right.$$
Unfortunately, we do not observe $\delta_{ijk}$ in the population. Let $\delta_{ijk}$ be a constant. 
$\mathbf{x}_{k}=\left(\delta_{1}.,k,\delta_{2}.,\cdots,\delta_{I}.k,\delta_{.1k},\delta_{.2k},\cdots,\delta_{.Jk}\right).$
and we know PN
k=1 xk.

Regression Estimation 97 The regression estimator in this case can be written as where

$${\hat{Y}}_{\mathrm{reg}}=\sum_{i\in A}{\frac{1}{\pi_{i}}}g_{i}\left(A\right)y_{i}$$  $$g_{i}\left(A\right)=\left(\sum_{k=1}^{N}\mathbf{x}_{k}\right)^{\prime}\left(\sum_{k\in A}{\frac{1}{\pi_{k}}}\mathbf{x}_{k}\mathbf{x}_{k}^{\prime}\right)^{-1}\mathbf{x}_{i}.$$

Unfortunately, we cannot compute the inverse of Pk∈A
1 πk xkx
′
k because its rank is I +J −1*, which is not full rank. Thus, there is no unique solution* Bˆ
toX

$$\sum_{i\in A}\pi_{i}^{-1}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}{\hat{B}}=\sum_{i\in A}\pi_{i}^{-1}\mathbf{x}_{i}y_{i}.$$

The goal is to find gkA = gk (A) *such that*

$$\sum_{k\in A}\frac{g_{kA}}{\pi_{k}}\delta_{i.k}=\sum_{k=1}^{N}\delta_{i.k},\ \ i=1,2,\cdots,I\tag{8.30}$$ $$\sum_{k\in A}\frac{g_{kA}}{\pi_{k}}\delta_{.jk}=\sum_{k=1}^{N}\delta_{.jk},\ \ j=1,2,\cdots,J.\tag{8.31}$$

One way to obtain the solution to (8.30) and (8.31) is to solve **the equations** iteratively as follows:

$$\begin{array}{l l}{{1.\,\,\,S t a r t\,\,w i t h\,\,g_{k A}^{(0)}=1.}}\\ {{\delta=F-\delta=-1.}}\end{array}$$
$${\mathrm{\boldmath~\nabla~}}_{2,}\;F o r\;\delta_{i\cdot k}=1,$$
$$g_{k A}^{(t+1)}=g_{k A}^{(t)}\frac{\sum_{k=1}^{N}\delta_{i\cdot k}}{\sum_{k\in A}g_{k A}^{(t)}\delta_{i\cdot k}/\pi_{k}}.$$

It satisfies (8.30), but not necessarily satisfy (8.31).

3. For δ·jk = 1,

$$g_{k A}^{(t+2)}=g_{k A}^{(t+1)}\frac{\sum_{k=1}^{N}\delta_{.j k}}{\sum_{k\in A}g_{k A}^{(t+1)}\delta_{.j k}/\pi_{k}}.$$

It satisfies (8.31), but not necessarily satisfy (8.30).

4. Set t ← t+ 2 **and go to Step 2. Continue until convergence.**
This computation method is called raking ratio estimation and was first considered by Deming and Stephan (1940) in the Census application. See also Deville et al. (1993).

__
l_
l l

## Estimation: Part 2 9.1 Greg Estimation

In Chapter 8, we have seen that the regression estimator is an **efficient**
estimator when there is a linear relationship between y and x**. In this chapter,**
we generalize the concept of regression estimation to a more **general class of** models for developing model-assisted estimation.

To motivate the generalized regression estimator, we first introduce difference estimator. Suppose that a proxy value of yi**, denoted by** y
(0)
i**, throughout**
the population. The difference estimator of Y =PN
i=1 yi **using** y
(0)
1,··· ,y
(0)
N is defined as

$$\hat{Y}_{\rm diff}=\sum_{i=1}^{N}y_{i}^{(0)}+\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-y_{i}^{(0)}\right).\tag{9.1}$$

The difference estimator is unbiased regardless of the choice of y
(0)
i**. The variance of the difference estimator is**

$$V\left({\hat{Y}}_{\mathrm{diff}}\right)=V\left(\sum_{i\in A}{\frac{y_{i}-y_{i}^{(0)}}{\pi_{i}}}\right).$$
$\langle0\rangle_{\rm max}$
$\alpha>0$. 
!
(0)
Thus, the difference estimator is unbiased regardless of y
(0)
i**but its variances**
are different for different choice of y
(0)
i**. If** y
(0)
i**is close to the true value of** yi, then the variance will be small.

In practice, we do not know y
(0)
i**. Instead, we use auxiliary variable** xi to construct a model for yi **and develop** y
(0)
i**from the model. That is, we assume**
that the finite population is a random sample of a superpopulation model that has generated the current finite population. One of the commonly used superpopulation models is

$$\begin{array}{r c l}{{E_{\zeta}\left(y_{i}\right)}}&{{=}}&{{{\bf x}_{i}^{\prime}\beta}}\\ {{C o v_{\zeta}\left(y_{i},y_{j}\right)}}&{{=}}&{{\left\{\begin{array}{l l}{{c_{i}\sigma^{2}}}&{{\mathrm{if~}i=j}}\\ {{0}}&{{\mathrm{if~}i\neq j}}\end{array}\right.}}\end{array}$$

where ci = c (xi) is a known function of xi and β are σ 2 **are unknown parameters. Model (9.2)-(9.3) is often called the generalized regression (GREG)**
model.

9

$$(9.2)$$  $$(9.3)$$

100 *Estimation: Part 2* Under the GREG model, the (model-based) projection estimator is defined to be the sum of the predicted values in the GREG model. That is, we define

$${\hat{Y}}_{\mathrm{p}}=\sum_{i=1}^{N}{\hat{y}}_{i},\tag{1}$$

where ˆyi = x
′
iβˆc and

$$\hat{\beta}_{\rm c}=\left(\sum_{i\in A}\frac{1}{c_{i}}{\bf x}_{i}{\bf x}_{i}^{\prime}\right)^{-1}\sum_{i\in A}\frac{1}{c_{i}}{\bf x}_{i}y_{i}.\tag{9.5}$$
$$(9.4)$$

The model-based projection estimator in (9.4) is developed **under the GREG**
model in (9.3). Note that the probability limit of βˆc in (9.5) is

$$B_{c}=\left(\sum_{i=1}^{N}{\frac{\pi_{i}}{c_{i}}}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\sum_{i=1}^{N}{\frac{\pi_{i}}{c_{i}}}\mathbf{x}_{i}y_{i}.$$
$$(9.6)$$

To ensure unbiasedness in the face of model misspecification, it's crucial that the resulting estimator also be asymptotically design **unbiased (ADU).** A key condition for achieving ADU is:

$$\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-\hat{y}_{i}\right)=0.\tag{1}$$

To understand why condition (9.6) leads to ADU, note that (9.6) implies that

$$\hat{Y}_{\rm p}=\sum_{i=1}^{N}{\bf x}_{i}^{\prime}\hat{\beta}+\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-{\bf x}_{i}^{\prime}\hat{\beta}\right)\tag{9.7}$$ $$=\hat{Y}_{\rm HT}+\left({\bf X}-\hat{\bf X}_{\rm HT}\right)^{\prime}\hat{\beta}.$$

The second term of (9.7) is a bias-correction term of the mode-based projection estimator in (9.4). Note that (9.4) is equivalent to (9.7) under condition (9.6). Condition (9.6) essentially makes the bias correction term **identically equal to** zero, which implies that the projection estimator in (9.4) is design consistent. In this sense, the condition (9.6) can be called the *internally biased calibration* (IBC) condition, which is termed by Firth and Bennett (1998).

The following lemma presents a sufficient condition for the projection estimator in (9.4) to be design consistent.

Lemma 9.1. If ci *satisfies*
$$c_{i}/\pi_{i}=\lambda^{\prime}{\bf x}_{i}\,$$
′xi **(9.8)**
_for some $\lambda$, then we have $\lambda$_
$$(9.8)$$
$$\sum_{i=1}^{N}\left(y_{i}-\mathbf{x}_{i}^{\prime}B_{c}\right)=0\tag{1}$$
$$(9.9)$$
GREG estimation 101

and
$$\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-{\bf x}^{\prime}_{i}\hat{\beta}\right)=0.\tag{9.10}$$
Proof. First, by the definition of Bc**, we obtain**

$$\sum_{i=1}^{N}\left(y_{i}-\mathbf{x}_{i}^{\prime}B_{c}\right)\mathbf{x}_{i}{\frac{\pi_{i}}{c_{i}}}=\mathbf{0}.$$

Thus, pre-multiplying both sides of the above equation by λ
′**, we get**

$$\begin{array}{r c l}{{0}}&{{=}}&{{\sum_{i=1}^{N}\left(y_{i}-\mathbf{x}_{i}^{\prime}B_{c}\right)\lambda^{\prime}\mathbf{x}_{i}\frac{\pi_{i}}{c_{i}}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{=}}&{{\sum_{i=1}^{N}\left(y_{i}-\mathbf{x}_{i}^{\prime}B_{c}\right)}}\end{array}$$

where the second equality follows from (9.8). Thus, (9.9) is **proved.**
Now, to show (9.10), by the definition of β**ˆ, we have**

$$\sum_{i\in A}\left(y_{i}-\mathbf{x}_{i}^{\prime}{\hat{\boldsymbol{\beta}}}_{c}\right)\mathbf{x}_{i}^{\prime}/c_{i}=\mathbf{0},$$

which implies $\frac{1}{2}$

$$\sum_{i\in A}{\frac{1}{\pi_{i}}}\left(y_{i}-\mathbf{x}_{i}^{\prime}{\hat{\boldsymbol{\beta}}}_{c}\right)\mathbf{x}_{i}^{\prime}\lambda/c_{i}=0.$$

Thus, by (9.8), we have (9.10).

If (9.8) holds, then the projection estimator can be safely used as it satisfies ADU. If condition (9.8) does not hold, the projection estimator is not design consistent. To construct a design-consistent prediction estimator under the GREG model in (9.2)-(9.3), we use

$${\hat{Y}}_{\mathrm{{GREG}}}={\hat{Y}}_{\mathrm{{HT}}}+\left(\mathbf{X}-{\hat{\mathbf{X}}}_{\mathrm{{HT}}}\right)^{\prime}{\hat{\boldsymbol{\beta}}}_{c}$$

$$(9.11)$$

$$(9.12)$$
X− Xˆ HT′βˆc**(9.11)**
as the bias-corrected prediction estimator. Now, using (9.11), we can express

$$\begin{array}{r c l}{{\hat{Y}_{\mathrm{GREG}}}}&{{=}}&{{\hat{Y}_{\mathrm{HT}}+\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)^{\prime}B_{c}+\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)^{\prime}\left(\hat{\beta}_{c}-B_{c}\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\hat{Y}_{\mathrm{HT}}+\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)^{\prime}B_{c}+O_{p}(n^{-1}N).}}\end{array}$$

Thus, using (9.9), we obtain

$${\hat{Y}}_{\mathrm{{GREG}}}-Y=\sum_{i\in A}\pi_{i}^{-1}\left(y_{i}-\mathbf{x}_{i}^{\prime}B_{c}\right)+O_{p}(n^{-1}N),$$

102 *Estimation: Part 2* which justifies the asymptotic unbiasedness of the GREG estimator in (9.7). The asymptotic variance is approximated by

$$V\left({\hat{Y}}_{\mathrm{{GREG}}}\right)\cong V\left\{\sum_{i\in A}\pi_{i}^{-1}\left(y_{i}-\mathbf{x}_{i}^{\prime}B_{c}\right)\right\}.$$
$$(9.13)$$
. **(9.13)**
If ei = yi −x
′
iBc **were observed, the variance (9.13) would be estimated by**

$$V\left({\hat{Y}}_{\mathrm{GREG}}\right)\cong\sum_{i\in A}\sum_{j\in A}{\frac{\pi_{i j}-\pi_{i}\pi_{j}}{\pi_{i j}}}{\frac{e_{i}}{\pi_{i}}}{\frac{e_{j}}{\pi_{j}}}.$$

If we use ˆei = yi −x
′
i
βˆ instead of Ei**, a consistent variance estimator is computed by**
$${\hat{V}}_{\mathrm{GREG}}=\sum_{i\in A j\in A}{\frac{\pi_{i j}-\pi_{i}\pi_{j}}{\pi_{i j}}}{\frac{{\hat{e}}_{i}}{\pi_{i}}}{\frac{{\hat{e}}_{j}}{\pi_{j}}}.$$
. **(9.14)**
Using (9.11), we can express

$${\hat{Y}}_{\mathrm{GREG}}=\sum_{i\in A}{\hat{\omega}}_{i}y_{i},$$

where

$$(9.14)$$
$$(9.15)$$
$${\hat{\omega}}_{i}=d_{i}+\left(\mathbf{X}-{\hat{\mathbf{X}}}_{\mathrm{HT}}\right)^{\prime}\left(\sum_{k\in A}{\frac{1}{c_{k}}}\mathbf{x}_{k}\mathbf{x}_{k}^{\prime}\right)^{-1}{\frac{1}{c_{i}}}\mathbf{x}_{i},$$
$$(9.16)$$
xi, **(9.16)**
and di = π
−1 iis the design weight of unit i**. The second term in (9.16) is the**
weight adjustment term incorporating the population auxiliary information X. The final weights {ωˆi;i ∈ A} **satisfy the calibration property**

$\sum_{i\in A}\hat{\omega}_{i}\mathbf{x}_{i}=\sum_{i=1}^{N}\mathbf{x}_{i}$.  
$$(9.17)$$
Since we can express
$$\hat{\omega}_{i}=d_{i}+\hat{\lambda}^{\prime}{\bf x}_{i}/c_{i}\tag{1}$$
for some λˆ, it is linear in xi. Thus, if some individual values of xi **are extreme**
(too large or too small), then the final weights can be too large or too small, even take negative values. Also, if ci is large, then the effect of xi **on the final**
weight is reduced.

The GREG weight in (9.15) can be viewed as the solution to an optimization problem that minimizes

$$Q(\mathbf{\omega})=\sum_{i\in A}\left(\omega_{i}-d_{i}\right)^{2}c_{i}$$
$$(9.18)$$
2ci (9.18)
GREG estimation 103 subject to

$$\sum_{i\in A}\omega_{i}\mathbf{x}_{i}=\sum_{i=1}^{N}\mathbf{x}_{i}.$$
$$(9.19)$$

Constraint (9.19) is attractive as it incorporates the external auxiliary information X =PN
i=1 xi**. The calibration condition (9.19) will be satisfied with**
wi = di approximately for sufficiently large n. Thus, the solution ˆwi **to the** above optimization problem will converge in probability to di.

By the Lagrange multiplier method, it is equivalent to minimizing

$$Q(\mathbf{\omega},\lambda)={\frac{1}{2}}\sum_{i\in A}\left(\omega_{i}-d_{i}\right)^{2}c_{i}+\lambda^{\prime}\left(\mathbf{X}-\sum_{i\in A}\omega_{i}\mathbf{x}_{i}\right)$$
$$(9.20)$$

with respect to ωi and λ**. We can solve the optimization problem by computing**
the partial derivatives:

$$\begin{array}{r c l}{{\frac{\partial}{\partial\omega_{i}}}Q}&{{=}}&{{(\omega_{i}-d_{i})c_{i}-\lambda^{\prime}{\bf x}_{i}=0}}\end{array}$$

to obtain the form
$$\omega_{i}=d_{i}+\lambda^{\prime}{\bf x}_{i}/c_{i}.$$
′xi/ci. **(9.21)**
To compute λ**, we insert (9.21) to (9.19) and obtain**
$$(9.21)$$
$$\hat{\lambda}^{\prime}=\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)\left(\sum_{i\in A}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}/c_{i}\right)^{-1}.$$
i∈A
!−1
Therefore, (9.15) is obtained. Note that λˆ **will converge to zero in probability**
as Xˆ HT will converge to X **in probability.**
Constraint (9.19) is called the calibration constraint, and the estimator obtained from an optimization problem of finding the final weights subject to the calibration constraint is called the *calibration estimator*.

More generally, instead of using the squared error distance **in (9.18), we**
may consider minimizing

$Q(\mathbf{\omega})=\sum_{i\in A}d_{i}G(\omega_{i}/d_{i})c_{i}$ (9.22)
subject to the calibration constraints in (9.19), where G(·, di) : V → R **is a**
nonnegative function that is strictly convex, differentiable, and G′**(1) = 0. The**
domain V of G(·) is an interval in R. For example, G(ω) = ωlog(ω)−ω**+1, with**
possible domain V ⊆ (0,∞**), corresponds to the Kullback-Leibler divergence,**
while G(ω) = (ω−1)2, with possible domain V ⊆ (−∞,∞**), corresponds to the**
Chi-squared distance from 1.

Let ˆωi **be the solution to the above optimization problem and** Yˆ P
cal =
i∈A ωˆiyi **be the resulting calibration estimator. Under some conditions on**
G(·), Yˆcal **is asymptotically equivalent to the GREG estimator in (9.11). The**
result is summarized in the following theorem. 104 *Estimation: Part 2* Theorem 9.1. *Under some regularity conditions, the calibration estimator* Yˆcal *satisfies*

$$\hat{Y}_{\rm cal}=\hat{Y}_{\rm HT}+\left({\bf X}-\hat{\bf X}_{\rm HT}\right)^{\prime}B+o_{p}(n^{-1/2}N)\tag{9.23}$$

where

$$B=\left(\sum_{i=1}^{N}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}/c_{i}\right)^{-1}\sum_{i=1}^{N}\mathbf{x}_{i}y_{i}/c_{i}.$$

Proof. **Using Lagrange multiplier method, the optimization problem can be**
expressed as maximizing

$$Q_{1}\left(\boldsymbol{\omega},\boldsymbol{\lambda}\right)=-\sum_{i\in A}d_{i}G(\omega_{i}/d_{i})c_{i}+\boldsymbol{\lambda}^{\prime}\left(\sum_{i\in A}\omega_{i}\mathbf{x}_{i}-\sum_{i=1}^{N}\mathbf{x}_{i}\right).$$  $$\frac{\partial}{\partial\omega_{i}}Q_{1}=-g\left(\omega_{i}/d_{i}\right)c_{i}+\boldsymbol{\lambda}^{\prime}\mathbf{x}_{i}$$  $\left(\omega_{i}/d_{i}\right)$ is the $\omega_{i}$-vector vector vector.  
Since∂
where g(ω) = dG(ω)/dω**, the maximizer can be expressed as**
ω
⋆
i(λ) = dig
−1λ
′xi/ci and we obtain ˆωi = ω
⋆
i
(
ˆλ) where ˆλ **satisfies (9.19).**
Now, we can express

$${\hat{Y}}_{\mathrm{cal}}={\hat{Y}}_{\mathrm{cal}}({\hat{\mathbf{\lambda}}})=\sum_{i=1}^{N}I_{i}\omega_{i}^{\star}({\hat{\mathbf{\lambda}}})y_{i}$$

where ˆλ **satisfies (9.19), we can express**

actions (3.10), we can express  $$\hat{Y}_{\rm cal}=\sum_{i=1}^{N}I_{i}\omega_{i}^{+}(\hat{\mathbf{\lambda}})y_{i}+\underbrace{\left(\sum_{i=1}^{N}\mathbf{x}_{i}-\sum_{i=1}^{N}I_{i}\omega_{i}^{+}(\hat{\mathbf{\lambda}})\mathbf{x}_{i}\right)}_{=0}^{\prime}\gamma$$  $$\hat{Y}_{\rm cal}=\hat{Y}_{\rm cal}(\hat{\mathbf{\lambda}},\mathbf{x})$$
$$\begin{array}{r l}{{:=}}&{{\hat{Y}_{\ell}(\hat{\lambda},\gamma).}}\end{array}$$
That is, Yˆℓ(*λ, γ* ˆ ) = Yˆcal(λ**ˆ) for all** γ.

Let λ
∗be the probability limit of λˆ. Since λˆ **satisfies (9.19),** λ
∗**should**
satisfy

$$\begin{array}{c}{{E\left\{\sum_{i=1}^{N}I_{i}\omega_{i}^{\star}\left(\boldsymbol{\lambda}^{\star}\right)\mathbf{x}_{i}\mid\mathcal{F}_{N}\right\}=\sum_{i=1}^{N}\mathbf{x}_{i},}}\\ {{=\sum_{i=1}^{N}\pi_{i}\omega_{i}^{\star}(\boldsymbol{\lambda}^{\star})\mathbf{x}_{i}}}\end{array}$$

Optimal Estimation 105

which implies that
$$\omega_{i}^{\star}(\lambda^{\star})=\pi_{i}^{-\,1}=d_{i}$$
∗/ci
= 1. Since g(1) = 0 and g(·**) is one-to-one, we get** λ
∗ = 0.
Now, if we can find γ
∗**such that**
$\textrm{r}g^{-1}\left(\mathbf{x}^\prime_i\boldsymbol{\lambda}^*_i\right)\\ \textrm{Now,if we}$
$$E\left\{\frac{\partial}{\partial\lambda}\hat{Y}_{\ell}(\lambda^{*},\gamma)\mid{\cal F}\right\}=0\tag{9.24}$$
at γ = γ
∗, then the sampling error of ˆλ **can be safely ignored (Randles, 1982)**
and we can obtain

$$\hat{Y}_{\rm cal}=\hat{Y}_{\ell}(\mathbf{\lambda}^{*},\mathbf{\gamma}^{*})+o_{p}(n^{-1/2}N).\tag{9.25}$$
 Now, since $\theta$
$$\begin{array}{r c l}{{\frac{\partial}{\partial\lambda}\hat{Y}_{\ell}(\lambda^{*},\gamma)}}&{{=}}&{{\sum_{i=1}^{N}I_{i}d_{i}\frac{1}{g^{\prime}({\bf x}_{i}^{\prime}\lambda^{*}/c_{i})}\left(y_{i}-{\bf x}_{i}^{\prime}\gamma\right){\bf x}_{i}/c_{i},}}\end{array}$$

and g
′(0) > **0 is constant, we obtain**

$$\gamma^{*}=\left(\sum_{i=1}^{N}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}/c_{i}\right)^{-1}\sum_{i=1}^{N}\mathbf{x}_{i}y_{i}/c_{i}.$$
$\square$
Therefore, by (9.25) with $\gamma^*=B$, we obtain (9.23). 
See Deville and Särndal (1992) and Fuller (2002) for further **discussion of**
the calibration weighting method.

## 9.2 Optimal Estimation

So far, we have discussed a class of model-assisted estimators that improve the efficiency of the HT estimator by incorporating auxiliary information. In this section, we explore the optimality of the Generalized Regression
(GREG) estimator within a certain class of estimators. We initially demonstrate the nonexistence of the Uniformly Minimum Variance Unbiased Estimator (UMVUE) in a strictly design-based context, which was **originally discovered by Godambe and Joshi (1965) and then also proved by Basu (1971)**
with a simpler proof.

Theorem 9.2. *Let any noncensus design with* πk > 0 (k = 1,2,··· ,N) be given. Then no uniformly minimum variance estimator exists **in the class of**
all unbiased estimators of Y =PN
i=1 yi.

106 **Estimation: Part 2**
Proof. **For a given value** y
∗ = (y
∗
1
,y∗
2
,··· ,y∗N **), consider the following difference**

estimator:  $$\hat{Y}_{\rm diff}=\sum_{i=1}^{N}y_{i}^{*}+\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-y_{i}^{*}\right)\tag{9.26}$$  This estimator is unbiased regardless of ${\bf y}^{*}=(y_{1}^{*},y_{2}^{*},\cdots,y_{N}^{*})$, and its variance is assumed to be 
is zero when y = y
∗.

For an unbiased estimator Yˆ **to be considered a UMVUE, it must satisfy:**

$$V\left({\hat{Y}}\right)\leq V\left({\hat{Y}}_{\mathrm{diff}}\right),\quad\forall\mathbf{y}.$$

Given that V (Yˆdiff**) = 0 for** y = y
∗, it implies that V (Yˆ **) = 0 for** y = y
∗**. Since**
any arbitrary y
∗can be chosen, it follows that V (Yˆ ) = 0 for all y**, a condition**
that only holds for a census.

The theorem discussed above demonstrates that it is not feasible to identify the optimal estimator within the class of unbiased estimators in terms of minimizing the design variance. To address this challenge, we adjust our approach for evaluating the efficiency of estimators by incorporating the superpopulation model into our considerations. More precisely, we will examine the expected value of the design variance under the superpopulation model. This type of variance is referred to as the *anticipated variance* **and is formally**
defined as follows.

Definition 9.1. Anticipated variance of ˆθ *is defined by*

$$A V\left({\hat{\theta}}\right)=E_{\zeta}\left\{V\left({\hat{\theta}}\mid{\mathcal{F}}_{N}\right)\right\},$$

where subscript ζ denotes the distribution with respect to the superpopulation model and the conditional expectation given F = {y1,...,yN } *denotes the* design-based expectation under the sampling mechanism.

Lemma 9.2. Let ˆθ be design-unbiased for θN *. The anticipated variance of* ˆθ can be written as

$$AV\left(\hat{\theta}\right)=E_{p}\left\{Var_{\zeta}\left(\hat{\theta}\right)\right\}+Var_{p}\left\{E_{\zeta}\left(\hat{\theta}\right)\right\}-Var_{\zeta}\left(\theta_{N}\right).\tag{9.27}$$

Proof. Since ˆθ is design-unbiased for θN **, we can write**

$$A V\left({\hat{\theta}}\right)=E_{\zeta}V a r_{p}\left({\hat{\theta}}\right)=E_{\zeta}E_{p}\left({\hat{\theta}}-\theta_{N}\right)^{2}.$$
Thus, $\frac{1}{2}$
$$\begin{array}{r c l}{{}}&{{}}&{{}}\\ {{}}&{{}}&{{A V\left(\hat{\theta}\right)}}\ \ =\ \ E_{p}E_{\zeta}\left(\hat{\theta}-\theta_{N}\right)^{2}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}\ \ E_{p}E_{\zeta}\left\{\hat{\theta}-E_{\zeta}(\hat{\theta})+E_{\zeta}(\hat{\theta})-E_{\zeta}\left(\theta_{N}\right)+E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right\}^{2}}\end{array}$$

Optimal Estimation 107 and

$$\begin{array}{r c l}{{A V\left({\hat{\theta}}\right)}}&{{=}}&{{E_{p}E_{\zeta}\left\{{\hat{\theta}}-E_{\zeta}({\hat{\theta}})\right\}^{2}+E_{p}\left\{E_{\zeta}({\hat{\theta}})-E_{\zeta}\left(\theta_{N}\right)\right\}^{2}+E_{p}\left\{E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right\}^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{+2E_{p}\left\{\left({\hat{\theta}}-E_{\zeta}({\hat{\theta}})\right)\left(E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)\right\}}}\end{array}$$

and the remaining cross product terms are zero. Since

$$E_{p}\left\{\left(\hat{\theta}-E_{\zeta}(\hat{\theta})\right)\right\}=-\left(E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)$$

and

$$2E_{p}\left\{\left(\hat{\theta}-E_{\zeta}(\hat{\theta})\right)\left(E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)\right\}=2\left(E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)E_{p}\left\{\left(\hat{\theta}-E_{\zeta}(\hat{\theta})\right)\right\}$$ $$=-2\left(E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)^{2},$$

we obtain

$$\begin{array}{r c l}{{A V\left({\hat{\theta}}\right)}}&{{=}}&{{E_{p}E_{\zeta}\left\{{\hat{\theta}}-E_{\zeta}({\hat{\theta}})\right\}^{2}+E_{p}\left\{E_{\zeta}({\hat{\theta}})-E_{\zeta}\left(\theta_{N}\right)\right\}^{2}-\left\{E_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right\}^{2}}}\end{array}$$

which proves (9.27).

The following theorem presents the lower bound of the anticipated variance for a design unbiased estimator.

Theorem 9.3. Let yi *be independently distributed in the superpopulation* model. The anticipate variance of any design-unbiased estimator P
Yˆ of Y =
N
i=1 yi *satisfies*

$$E_{\zeta}\left\{V\left(\hat{Y}\mid\mathcal{F}_{N}\right)\right\}\geq\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right)Var_{\zeta}\left(y_{i}\right).\tag{9.28}$$

Proof. Write Yˆ as Yˆ = YˆHT +R where YˆHT is the HT estimator of Y **. Since**
Yˆ is design unbiased, we have E (R**) = 0 and, for fixed** j ∈ U,

$$\begin{array}{r c l}{{}}&{{}}&{{}}\\ {{0}}&{{=}}&{{E\left(R\right)}}\\ {{}}&{{=}}&{{\sum_{A\in{\mathcal{A}}}p\left(A\right)R\left(A\right)}}\\ {{}}&{{=}}&{{\sum_{A\in{\mathcal{A}};j\in{A}}p\left(A\right)R\left(A\right)+\sum_{A\in{\mathcal{A}};j\notin{A}}p\left(A\right)R\left(A\right).}}\end{array}$$

Now, since

$$V_{\zeta}\left(\hat{Y}\right)=V_{\zeta}\left(\hat{Y}_{\mathrm{HT}}\right)+V_{\zeta}\left(R\right)+2C o v_{\zeta}\left(\hat{Y}_{\mathrm{HT}},R\right),$$
108 *Estimation: Part 2*
we obtain Ep nCovζ YˆHT,Ro = Ep hEζ nYˆHT −Eζ YˆHT R oi = Ep  X j∈U Eζ (yj −Eζ (yj) Ij πjR )  =X j∈U Eζ (yj −Eζ (yj)  πjE {Ij (A)R(A)} ) =X j∈U Eζ   yj −Eζ (yj)  πj X A∈A;j∈A R(A)p(A)   = − X j∈U Eζ   yj −Eζ (yj )  πj X A∈A;j /∈A R(A)p(A)   = 0,
where the last equality follows because PA∈A;j /∈A R(A)p(A**) does not depend**

on yj . Thus, Ep nVζ Yˆ o = Ep nVζ YˆHT o+Ep Vζ (R) 	 ≥ Ep nVζ YˆHT o = Ep ( Vζ  X N i=1 yiIi πi !) = Ep (X N ) = X N i=1 σ 2 i Ii π 2 i i=1 σ 2 i πi and we have AV Yˆ = EpVζ Yˆ +VpEζ Yˆ −Vζ (Y ) ≥ EpVζ Yˆ −Vζ (Y ) ≥X N i=1 σ 2 i πi − X i∈U σ 2 i .
$$\blacksquare$$
The lower bound in (9.28) is the lower bound of the anticipated variance of any unbiased estimator. The lower bound was first discovered by Godambe and Joshi (1965) and is often called Godambe-Joshi lower bound. For a fix-ed Model-assisted calibration 109 size probability sampling design, the Godambe-Joshi lower **bound is minimized** when πi ∝ {*V ar*ζ (yi)}
1/2. **(9.29)**
To show this, we minimize PN
i=1 *V ar*ζ (yi)/πi **subject to** PN
i=1 πi = n**. The**
solution can be obtained by applying Cauchy -Schwarz inequality to get

$$\left\{\sum_{i=1}^{N}\sigma_{i}^{2}/\pi_{i}\right\}(\sum_{i=1}^{N}\pi_{i})\geq\left\{\sum_{i=1}^{N}\sigma_{i}\right\}^{2}$$  a so-called
with equality when (9.29) holds.

The following theorem, which was first proved by Isaki and Fuller (1982),
shows that the GREG estimator achieves the Godambe-Joshi lower bound asymptotically.

Theorem 9.4. Suppose that ζ is a superpopulation model with yi*'s independent and* Eζ (yi) = x
′iβ and Vζ (yi) = ciσ 2**. Then, the anticipated variance of**
the GREG estimator in (9.11) asymptotically attains the Godambe-Joshi lower bound. Proof. By (9.12), the GREG estimator is asymptotically equivalent **to the**
difference estimator in (9.12). Thus,

$$E_{\zeta}\left\{V\left(\hat{Y}_{\text{GREG}}\right)\right\}\doteq E_{\zeta}\left\{\sum_{i=1}^{N}\sum_{j=1}^{N}\left(\pi_{ij}-\pi_{i}\pi_{j}\right)\frac{y_{i}-\mathbf{x}_{i}^{\prime}B_{c}}{\pi_{i}}\frac{y_{j}-\mathbf{x}_{j}^{\prime}B_{c}}{\pi_{j}}\right\}$$ $$\doteq E_{\zeta}\left\{\sum_{i=1}^{N}\sum_{j=1}^{N}\left(\pi_{ij}-\pi_{i}\pi_{j}\right)\frac{y_{i}-\mathbf{x}_{i}^{\prime}\beta}{\pi_{i}}\frac{y_{j}-\mathbf{x}_{j}^{\prime}\beta}{\pi_{j}}\right\}$$ $$=\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right)c_{i}\sigma^{2}$$

which is equal to the Gobambe-Joshi lower bound under the superpopulation model.

## 9.3 Model-Assisted Calibration

We now turn our attention to a model-assisted approach for calibration estimation. To illustrate the concept of calibration estimation within the framework of the superpopulation model specified in equations (9.2)-(9.3), let's consider a linear estimator defined as

$${\hat{Y}}_{\omega}=\sum_{i\in A}\omega_{i}y_{i}$$

110 *Estimation: Part 2* for some ωi**. Now, note that**

$$\hat{Y}_{\omega}-Y=\left\{\sum_{i\in A}\omega_{i}\mathbf{x}_{i}^{\prime}\beta-\sum_{i=1}^{N}\mathbf{x}_{i}^{\prime}\beta\right\}+\left\{\sum_{i\in A}\omega_{i}e_{i}-\sum_{i=1}^{N}e_{i}\right\}:=C+D.\tag{9.30}$$

The first term, C, can be eliminated if the weights ωi **satisfy the calibration constraint (9.19). Consequently, our goal shifts to minimizing the model**
variance of the term D**. Note that**

$$\begin{array}{r c l}{{E_{\zeta}(D^{2}\mid I_{1},\cdots,I_{N})}}&{{=}}&{{\sum_{i\in{\cal A}}\omega_{i}^{2}c_{i}\sigma^{2}-2\sum_{i\in{\cal A}}\omega_{i}c_{i}\sigma^{2}+\sum_{i=1}^{N}c_{i}\sigma^{2}}}\end{array}$$
$$(9.31)$$

If the condition ci = λ
′xi **is met, then the calibration constraint in (9.19)**
implies that

$$\sum_{i\in A}\omega_{i}c_{i}=\sum_{i=1}^{N}c_{i}.$$

If ci = 1, then (9.8) means that xi **includes an intercept term and constraint**
(9.31) is a normalization constraint for ωi.
Therefore, under (9.8) and (9.19), minimizing the model variance of D is
equivalent to minimizing
$$Q(w)=\sum_{i\in A}\omega_{i}^{2}c_{i}.$$
ici. **(9.32)**
The optimal calibration estimator is then given by

$${\hat{Y}}_{\mathrm{opt}}=\sum_{i\in A}{\hat{\omega}}_{i}y_{i}=\sum_{i=1}^{N}\mathbf{x}_{i}^{\prime}{\hat{\beta}}_{c}$$
$$(9.32)$$
$$(9.33)$$
iβˆc**(9.33)**
where βˆc =
Pi∈A c
−1 i xix
′
i
−1Pi∈A c
−1 i xiyi**. This formulation reveals that**
the final calibration estimator can be interpreted as a projection estimator in Section 9.1.

For the regression projection estimator with ˆyi = x
′ i β**ˆ, by Lemma 9.1,**
the IBC condition in (9.6) can be met by augmenting xi **to include**
π
−1 ici**. In other words, by defining** z
′
i = (x
′ i
,π
−1 ici**) and calculating** γˆ =
Pi∈A c
−1 iziz
′
i
−1Pi∈A c
−1 iziyi**, the property of the residuals ensures that**
yˆi = z
′
i γˆ **fulfills**

$$\sum_{i\in A}\left(y_{i}-{\hat{y}}_{i}\right)\mathbf{z}_{i}c_{i}^{-1}=\mathbf{0},$$

thereby implying the IBC condition in (9.6). This approach effectively integrates additional calibration into the estimation process, enhancing its robustness against potential model misspecification.

Model-assisted calibration 111 To minimize the model variance ˆθω **while also adhering to the Asymptotically Design Unbiased (ADU) condition, our objective narrows down to**
minimizing

$$\sum_{i\in A}\omega_{i}^{2}c_{i}$$

subject to

$$\sum_{i\in A}\omega_{i}\mathbf{z}_{i}=\sum_{i=1}^{N}\mathbf{z}_{i}$$
$$(9.35)$$

where z
′
i = (x
′
i
,π
−1 ici).

Let ˆωi **be the solution to the optimization problem described above. Using**
the Lagrangian multiplier method, it can be shown that the resulting estimator can be written as where

$$\mathrm{and}$$
$$\hat{Y}_{\rm cal}=\sum_{i\in A}\hat{\omega}_{i}y_{i}=\sum_{i\in U}{\bf z}_{i}^{\prime}\hat{\gamma}+\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-{\bf z}_{i}^{\prime}\hat{\gamma}\right),\tag{9.36}$$  $$\hat{\omega}_{i}=\left(\sum_{i=1}^{N}{\bf z}_{i}\right)^{\prime}\left(\sum_{i\in A}c_{i}^{-1}{\bf z}_{i}{\bf z}_{i}^{\prime}\right)^{-1}{\bf z}_{i}/c_{i}$$  $$\hat{\gamma}=\left(\sum_{i\in A}c_{i}^{-1}{\bf z}_{i}{\bf z}_{i}^{\prime}\right)^{-1}\sum_{i\in A}c_{i}^{-1}{\bf z}_{i}y_{i}.$$  The probability density of the $N$ is the standard average total number of 
Let γ
∗ be the probability limit of ˆγ**. Using the standard argument similar**
to (9.12), we can obtain

$$N^{-1}\hat{Y}_{\mathrm{cal}}=N^{-1}\hat{Y}_{\mathrm{diff}}+O_{p}(n^{-1}),$$
where
$${\hat{Y}}_{\mathrm{diff}}=\sum_{i\in{U}}\mathbf{z}_{i}^{\prime}\gamma^{*}+\sum_{i\in{A}}{\frac{1}{\pi_{i}}}\left(y_{i}-\mathbf{z}_{i}^{\prime}\gamma^{*}\right).$$

Now, note that

$$\begin{array}{r c l}{{\hat{Y}_{\mathrm{diff}}-Y}}&{{=}}&{{\sum_{i=1}^{N}\left({\frac{I_{i}}{\pi_{i}}}-1\right)\left(y_{i}-\mathbf{z}_{i}^{\prime}\gamma^{*}\right)}}\end{array}$$

and

$$\begin{array}{r c l}{E\left\{\left(\hat{Y}_{\mathrm{diff}}-Y\right)^{2}\right\}}&{=}&{E\left\{\sum_{i=1}^{N}\left(\frac{I_{i}}{\pi_{i}}-1\right)^{2}v_{i}\right\}}\\ {}&{}&{}&{}\\ {}&{}&{=}&{\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right)v_{i}}\end{array}$$
where $v_{i}=E_{\zeta}\left\{\left(y_{i}-\mathbf{z}_{i}^{\prime}\gamma^{*}\right)^{2}\right\}\left|\mathbf{z}_{i}\right\}$.  
If the Generalized Regression (GREG) model specified in equations (9.2)-
(9.3) is accurate, then the variance component for each unit, vi**, is equal to** ciσ 2**. However, if the GREG model does not accurately represent the underlying data structure, it is possible to observe that** ciσ 2 > vi**. This discrepancy**
arises because the additional covariate π
−1 ici **improves the prediction of** yi, thus contributing to a more precise estimation.

Consequently, it can be concluded that the model-assisted calibration estimator, which employs the augmented covariate zi **for calibration, exhibits**
greater efficiency compared to the GREG estimator, especially when the superpopulation model delineated in equations (9.2)-(9.3) does not perfectly align with the actual data. This advantage underscores the robustness of the calibration approach in accommodating model inaccuracies **and improving the** accuracy of the estimate.

For general models, Wu and Sitter (2001) introduced the concept of model calibration, which integrates the working regression model directly into the calibration constraint. This approach involves using ˆmi = m(xi; ˆβ) as an estimated predictor for yi**, derived from the working regression model where**
E(Y | x) = m(x;β). If it is possible to calculate ˆmi **for every unit of the**
population, then the following equation can be employed as the calibration constraint for the weighting problem:

$$\sum_{i\in A}w_{i}(1,\hat{m}_{i})=\sum_{i=1}^{N}(1,\hat{m}_{i})\tag{9.37}$$

The uncertainty of βˆ in ˆmi **can be safely ignored in the final inference.**
Instead of using model calibration, an alternative approach involves calibrating for basis functions. This method is applicable when **the expected value**
of Y on x belongs to the span of a set of basis functions b1(x),··· , bL(x**). In**
such scenarios, the calibration estimation can utilize the **following constraint:**

$$\sum_{i\in A}w_{i}\left[b_{1}({\bf x}_{i}),\cdots,b_{L}({\bf x}_{i})\right]=\sum_{i=1}^{N}\left[b_{1}({\bf x}_{i}),\cdots,b_{L}({\bf x}_{i})\right]\tag{9.38}$$

This condition ensures that the C **term in (9.30) is nullified. As the sample size** increases, the dimension L **of the basis functions may also need to be increased.** In such instances, regularization methods can be employed to select a suitable L.

For example, Montanari and Ranalli (2005) explored the use of neural network models, while Breidt et al. (2005) applied penalized spline models for nonparametric calibration estimation. These methodologies offer a flexible framework for calibration estimation, allowing for the **accommodation of**
complex relationships between the response variable.

## 9.4 Generalized Entropy Calibration

Instead of the squared error loss in (9.32), we can consider the we now consider maximizing the generalized entropy that does not depend on the design weights, which was proposed by Kwon et al. (2024). Using (9.2)-(9.3) as a working model for model-assisted estimation, the generalized entropy method can be formulated as minimizing

$$\sum_{i\in A}c_{i}G(\omega_{i})$$

subject to (9.19) and

$$\sum_{i\in A}\omega_{i}g(d_{i})c_{i}=\sum_{i=1}^{N}g(d_{i})c_{i},$$
$$(9.39)$$
$$(9.40)$$

where g(ω) = dG(ω)/dω**. Constraint (9.40) plays the role of achieving the** ADU condition of the resulting calibration estimator and it **is also called the** debiasing constraint under model hetergeneity (Kwon et al., 2024).

The following theorem presents the √n**-consistency of the generalized entropy calibration estimator.**
Theorem 9.5. Let ωˆi **be obtained by minimizing (9.39) subject to (9.19) and**
(9.40). The resulting calibration estimator Yˆgcal =Pi∈A ωˆiyi *satisfies*

$$\hat{Y}_{\mathrm{gcal}}=\hat{Y}_{\mathrm{greg},\ell}+o_{p}(n^{-1/2}N),$$
$$u h e r e$$
∗, **(9.41)**
$$\hat{Y}_{\mathrm{greg},\ell}=\sum_{i\in{\cal U}}{\mathbf{z}_{i}^{\prime}}{\mathbf{\gamma}^{*}}+\sum_{i\in{\cal A}}\frac{1}{\pi_{i}}\left(y_{i}-{\mathbf{z}_{i}^{\prime}}{\mathbf{\gamma}^{*}}\right),$$

z
$$\mathbf{z}_{i}^{\prime}=(\mathbf{x}_{i}^{\prime},g(d_{i})c_{i}$$
,g(di)ci) and γ
∗is the probability limit of γˆ *given by*
$$\hat{\mathbf{\gamma}}=\left(\sum_{i\in A}\frac{1}{g^{\prime}(d_{i})c_{i}}\mathbf{z}_{i}\mathbf{z}_{i}^{\prime}\right)^{-1}\sum_{i\in A}\frac{1}{g^{\prime}(d_{i})c_{i}}\mathbf{z}_{i}y_{i}.\tag{9.42}$$
$$(9.41)$$
Proof. **The proof is very similar to that of Theorem 9.1. Using Lagrange multiplier method, the optimization problem can be expressed as maximizing**

$$Q_{2}\left(\pmb{\omega},\pmb{\lambda}\right)=-\sum_{i\in A}G(\omega_{i})c_{i}+\pmb{\lambda}^{\prime}\left(\sum_{i\in A}\omega_{i}\mathbf{z}_{i}-\sum_{i=1}^{N}\mathbf{z}_{i}\right).$$

Since∂
$${\frac{\partial}{\partial\omega_{i}}}Q_{2}=-g\left(\omega_{i}\right)c_{i}+\lambda^{\prime}\mathbf{z}_{i},$$

114 *Estimation: Part 2* the maximizer can be expressed as ω
⋆
i(λ) = g
−1λ
′
1xi/ci +λ2gi where gi = g(di).

Now, we can express

$$\hat{Y}_{\mathrm{gcal}}=\hat{Y}_{\mathrm{gcal}}(\hat{\mathbf{\lambda}})=\sum_{i=1}^{N}I_{i}\omega_{i}^{\star}(\hat{\mathbf{\lambda}})y_{i}$$

where ˆλ **satisfies (9.19), we can express**

satisfies (9.19), we can express  $$\hat{Y}_{\rm gcal}=\sum_{i=1}^{N}I_{i}\omega_{i}^{*}(\hat{\bf A})y_{i}+\underbrace{\left(\sum_{i=1}^{N}{\bf x}_{i}-\sum_{i=1}^{N}I_{i}\omega_{i}^{*}(\hat{\bf A}){\bf x}_{i}\right)^{\prime}}_{=0}\gamma$$ $$:=\hat{Y}_{\ell}(\hat{\bf A},\gamma).$$
Let λ
∗be the probability limit of ˆλ. Since ˆλ **satisfies (9.19),** λ
∗**should**

satisfy $$\underbrace{E\left\{\sum_{i=1}^N I_i\omega_i^*\left(\boldsymbol{\lambda}^*\right)\mathbf{z}_i\mid\mathcal{F}_N\right\}}_{=\sum_{i=1}^N\pi_i\omega_i^*\left(\boldsymbol{\lambda}^*\right)\mathbf{z}_i}=\sum_{i=1}^N\mathbf{z}_i,$$ which implies that $$\omega_i^*\left(\boldsymbol{\lambda}^*\right)=\pi_i^{-1}=d_i$$. 
or
$$g^{-1}\left(\mathbf{x}_{i}^{\prime}\lambda_{1}^{*}/c_{i}+g(d_{i})\lambda_{2}^{*}\right)=d_{i}.$$
Since g(·**) is one-to-one, we get** λ
∗
1 = 0 and λ
∗
2 **= 1.**
Now, to obtain the linearization similar to we wish to find γ
∗**such that**
(9.24) holds at γ = γ
∗**. Now, since**

$$\frac{\partial}{\partial\boldsymbol{\lambda}}\hat{Y}_{\ell}(\boldsymbol{\lambda}^{*},\boldsymbol{\gamma})=\sum_{i=1}^{N}I_{i}\frac{1}{g^{\prime}\{g^{-1}(\mathbf{z}_{i}^{\prime}\boldsymbol{\lambda}^{*}/c_{i})\}}\left(y_{i}-\mathbf{z}_{i}^{\prime}\boldsymbol{\gamma}\right)\mathbf{z}_{i}/c_{i},$$  we obtain  $$\boldsymbol{\gamma}^{*}=\left(\sum_{i=1}^{N}\frac{\pi_{i}}{g^{\prime}(d_{i})c_{i}}\mathbf{z}_{i}\mathbf{z}_{i}^{\prime}\right)^{-1}\sum_{i=1}^{N}\frac{\pi_{i}}{g^{\prime}(d_{i})c_{i}}\mathbf{z}_{i}y_{i}.$$  Therefore, we obtain (9.42).  
$$\square$$

Generalized entropy calibration 115 Note that Theorem 9.5 does not use the superpopulation model **in (9.2)-**
(9.3) as an assumption. If the GREG superpopulation model is **indeed correct,** then we obtain γ
∗ = (β
′,0)′ and

$${\hat{Y}}_{\mathrm{{greg}},\ell}=\sum_{i=1}^{N}\pmb x_{i}^{\prime}\pmb\beta+\sum_{i\in A}\frac{1}{\pi_{i}}\left(y_{i}-\pmb x_{i}^{\prime}\pmb\beta\right)+o_{p}\left(n^{-1/2}N\right),$$

which achieves the Godambe-Joshi lower bound of the anticipate variance (Godambe and Joshi, 1965).

If the superpopulation model is incorrect, Theorem 9.5 is still applicable and the asymptotic variance of Yˆgcal **is equal to**

$$V\left(\hat{Y}_{\text{greg},\ell}\right)=V\left(\sum_{i=1}^{N}y_{i}\right)+E\left\{\sum_{i=1}^{N}\left(\pi_{i}^{-1}-1\right)\left(y_{i}-\mathbf{z}_{i}^{\prime}\mathbf{\gamma}^{*}\right)^{2}\right\}.\tag{9.43}$$

On the other hand, by Theorem 9.1, the classical calibration **estimator** ˆθDS of Deville and Särndal (1992), ignoring the smaller order terms, satisfies

$$V\left(\hat{Y}_{\rm DS}\right)=V\left(\sum_{i=1}^{N}y_{i}\right)+E\left\{\sum_{i=1}^{N}\left(\pi_{i}^{-1}-1\right)\left(y_{i}-\mathbf{x}_{i}^{\prime}B\right)^{2}\right\},\tag{9.44}$$

where β
∗is the probability limit of βˆGLS **where**

$${\hat{\beta}}_{\mathrm{GLS}}=\left(\sum_{i\in A}d_{i}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}/c_{i}\right)^{-1}\sum_{i\in A}d_{i}\mathbf{x}_{i}y_{i}/c_{i}.$$

Comparing (9.43) with (9.44), the additional covariate gici in zi **can improve**
the prediction power for yi**. Thus, the proposed calibration estimator is more**
efficient than the classical calibration estimator when the superpopulation model is incorrect.

__
l_
l l 10

## Variance Estimation 10.1 Introduction

Variance estimation is an important practical problem in survey sampling.

Variance estimates are used for two purposes. One is an analytic purpose, such as constructing confidence intervals or performing hypothesis tests. The other is descriptive purposed to evaluate the efficiency of survey designs or estimates for planning surveys.

Desirable variance estimates should satisfy the following **properties:**
- It should be unbiased, or approximately unbiased.

- The variance estimator should be small. That is, the variance estimator is stable.

- It should not take negative values. - The computation should be simple.
The HT variance estimator is unbiased, but it can take negative values. In addition, computing the joint inclusion probabilities πij **can be cumbersome**
when the sample size is large.

Example 10.1. *Consider a finite population of size* N = 3 *with* y1 **= 16**,y2 =
21 and y3 = 18 *and consider the following sampling design.*

A sampling design for Example 10.1

| Sample (A)   | P (A)   | HT estimator   | HT variance estimator   |
|--------------|---------|----------------|-------------------------|
| A1 = {1,2}   | 0.4     | 50             | 206                     |
| A2 = {1,3}   | 0.3     | 50             | 200                     |
| A3 = {2,3}   | 0.2     | 60             | -90                     |
| A4 = {1,2,3} | 0.1     | 80             | -394                    |

The sampling variance of the HT estimator is 85. Note that the *HT variance estimator has expectation* 206×0.4 + 200×0.3 + (−90)×0.2 + (−394)×0.**1 = 85**
118 *Variance Estimation* but it can take negative values in some samples.

The variance estimator under PPS sampling is always nonnegative and can be computed without computing the joint inclusion probability. In practice, the PPS sampling variance estimator is often applied as an alternative variance estimator even for non-replacement sampling. The resulting variance estimator can be written

$$\hat{V}_{0}=\frac{1}{n\left(n-1\right)}\sum_{i\in A}\left(\frac{y_{i}}{p_{i}}-\hat{Y}_{\rm HT}\right)^{2}=\frac{n}{\left(n-1\right)}\sum_{i\in A}\left(\frac{y_{i}}{\pi_{i}}-\frac{1}{n}\hat{Y}_{\rm HT}\right)^{2},\tag{10.1}$$

where pi = πi/n**. The following theorem expresses the bias of the simplified**
variance estimator in (10.1) as an estimator of the variance **of the HT estimator.**
Theorem 10.1. *The simplified variance estimator in (10.1) satisfies*

$$E\left(\hat{V}_0\right)-Var\left(\hat{Y}_\text{HT}\right)=\frac{n}{n-1}\left\{Var\left(\hat{Y}_\text{PPS}\right)-Var\left(\hat{Y}_\text{HT}\right)\right\}\tag{10.2}$$  e. 
where

$$V a r\left({\hat{Y}}_{\mathrm{PPS}}\right)={\frac{1}{n}}\sum_{i=1}^{N}p_{i}\left({\frac{y_{i}}{p_{i}}}-Y\right)^{2}$$

and pi = πi/n.

Proof. Note that Vˆ0 satisfies E (X k∈A yk pk −Y +Y −YˆHT2) = E (X k∈A yk pk −Y 2)+ 2E (X k∈A yk pk −Y Y −YˆHT)+E (X k∈A Y −YˆHT2 ) . The first term is E (X k∈A yk pk −Y 2)=X N k=1 yk pk −Y 2πk = n 2V arYˆPPS and, using !

$$\sum_{k\in A}\left({\frac{y_{k}}{p_{k}}}-Y\right)=n\left(\sum_{k\in A}{\frac{y_{k}}{\pi_{k}}}-Y\right)=n\left({\hat{Y}}_{\mathrm{HT}}-Y\right),$$
the second term equals to $-2nVar\Big(\hat{Y}_{\text{HT}}\Big)$ and the last term is equal to . 
nV arYˆHT, which proves the result.
Linearization approach to variance estimation 119 In many cases, the bias term in (10.2) is positive and the simplified variance estimator conservatively estimates the variance. Under SRS, the relative bias of the simplified variance estimator (10.1) is

$$\frac{\hat{V}_{0}-Var\left(\hat{Y}_{\rm HT}\right)}{Var\left(\hat{Y}_{\rm HT}\right)}=\frac{n}{N-n}\tag{10.3}$$

and the relative bias is negligible when n/N **is negligible.**
The simplified variance estimator can be directly applicable to multistage sampling designs. Under multistage sampling design, the HT **estimator of the**
total can be written

$${\hat{Y}}_{\mathrm{HT}}=\sum_{i\in A_{I}}{\frac{{\hat{Y}}_{i}}{\pi_{I i}}}$$

where Yˆi is the estimated total for the PSU i**. The simplified variance estimator**
is then given by

$${\hat{V}}_{0}={\frac{n}{(n-1)}}\sum_{i\in A_{I}}\left({\frac{{\hat{Y}}_{i}}{\pi_{I i}}}-{\frac{1}{n}}{\hat{Y}}_{\mathrm{HT}}\right)^{2}.$$
i∈AI
Under stratified multistage cluster sampling, the simplified variance estimator can be written

$$\hat{V}_{0}=\sum_{h=1}^{H}\frac{n_{h}}{n_{h}-1}\sum_{i=1}^{n_{h}}\left(w_{hi}\hat{Y}_{hi}-\frac{1}{n_{h}}\sum_{j=1}^{n_{h}}w_{hj}\hat{Y}_{hj}\right)^{2}\tag{10.4}$$

where whi is the sampling weight for cluster i **in stratum** h.

## 10.2 Linearization Approach To Variance Estimation

When the point estimator is a nonlinear estimator, such as a ratio estimator or regression estimator, exact variance estimation for such estimates is very difficult. Instead, we often rely on linearization methods to estimate the sampling variance of such estimators.

Roughly speaking, if y is a p**-dimensional vector and when ¯**yn = Y¯ N +
Op n
−1/2holds, the Taylor linearization of g (¯yn**) can be written as**

$$g\left({\bar{\mathbf{y}}}_{n}\right)=g\left({\bar{\mathbf{Y}}}\right)+\sum_{j=1}^{p}{\frac{\partial g\left({\bar{\mathbf{Y}}}\right)}{\partial y_{j}}}\left({\bar{y}}_{j}-{\bar{Y}}_{j}\right)+O_{p}\left(n^{-1}\right).$$

120 *Variance Estimation* Thus, the variance of the linearized term of g (¯yn**) can be written**

$$V\left\{g\left({\bar{\mathbf{y}}}_{n}\right)\right\}\doteq\sum_{i=1}^{p}\sum_{j=1}^{p}{\frac{\partial g\left({\bar{\mathbf{Y}}}\right)}{\partial y_{i}}}{\frac{\partial g\left({\bar{\mathbf{Y}}}\right)}{\partial y_{j}}}C o v\left\{{\bar{y}}_{i},{\bar{y}}_{j}\right\}$$

and is estimated by

$$\hat{V}\left\{g\left(\bar{\mathbf{y}}_{n}\right)\right\}\doteq\sum_{i=1}^{p}\sum_{j=1}^{p}\frac{\partial g\left(\bar{\mathbf{y}}_{n}\right)}{\partial y_{i}}\frac{\partial g\left(\bar{\mathbf{y}}_{n}\right)}{\partial y_{j}}\hat{C}\left\{\bar{y}_{i},\bar{y}_{j}\right\}.\tag{10.5}$$

In summary, the linearization method for variance estimation can be described as follows:
1. Apply Taylor linearization and ignore the remainder terms.

2. Calculate the variance and covariance terms for each component of y¯n **using the standard variance estimation formula.**
3. Estimate the partial derivative terms (*∂g/∂y***) from the sample observation.**
Example 10.2. If the parameter of interest is R = Y / ¯ X¯ *and we use*

$${\hat{R}}={\frac{{\bar{Y}}_{\mathrm{HT}}}{X_{\mathrm{HT}}}}$$

to estimate R*, we can apply Taylor linearization to get*

$$\hat{R}=R+\bar{X}^{-1}\left(\bar{Y}_{\mathrm{HT}}-R\bar{X}_{\mathrm{HT}}\right)+O_{p}\left(n^{-1}\right)$$

and the variance estimation formula in (10.5) reduces to

$$\hat{V}\left(\hat{R}\right)\doteq\bar{X}_{\rm HT}^{-2}\hat{V}\left(\bar{Y}_{\rm HT}\right)+\bar{X}_{\rm HT}^{-2}\hat{R}^{2}\hat{V}\left(\bar{X}_{\rm HT}\right)-2\bar{X}_{\rm HT}^{-2}\hat{R}\widehat{Cov}\left(\bar{X}_{\rm HT},\bar{Y}_{\rm HT}\right).\tag{10.6}$$

If the variances and covariances of X¯HT and Y¯HT *are estimated by HT variance estimation formula, (10.6) can be estimated by*

$${\hat{V}}\left({\hat{R}}\right)\doteq{\frac{1}{{\hat{X}}_{\mathrm{HT}}^{2}}}\sum_{i\in A}\sum_{j\in A}{\frac{\pi_{i j}-\pi_{i}\pi_{j}}{\pi_{i j}}}{\frac{e_{i}\ e_{j}}{\pi_{i}\ \pi_{j}}}$$

where ei = yi −Rxˆi.

Using the result in Example 10.2, the variance of the ratio estimator YˆR =
XRˆ **is estimated by**

$$\hat{V}\left(\hat{Y}_{R}\right)\doteq\left(\frac{X}{\hat{X}_{\rm HT}}\right)^{2}\sum_{i\in A}\sum_{j\in A}\frac{\pi_{ij}-\pi_{i}\pi_{j}}{\pi_{ij}}\frac{e_{i}}{\pi_{i}}\frac{e_{j}}{\pi_{j}},\tag{10.7}$$

Replication approach to variance estimation 121 which is obtained by multiplying Xˆ −2 HTX2**to the variance formula in (8.13).**
The variance estimator in (10.7) is asymptotically equivalent to the linearization variance estimator in (8.13), but it gives a more adequate measure of the conditional variance of the ratio estimator, as advocated by Royall and Cumberland (1981). More generally, Särndal et al. (1989) proposed using

$$\hat{V}\left(\hat{Y}_{\rm GREG}\right)=\sum_{i\in A}\sum_{j\in A}\frac{\pi_{ij}-\pi_{i}\pi_{j}}{\pi_{ij}}\frac{g_{i}e_{i}}{\pi_{i}}\frac{g_{j}e_{j}}{\pi_{j}}\tag{10.8}$$

as the conditional variance estimator of the GREG estimator **of the form**
Yˆ**GREG** =Pi∈A π
−1 igiyi**, where**

$$g_{i}={\bf X}^{\prime}\left(\sum_{i\in A}\frac{1}{\pi_{i}c_{i}}{\bf x}_{i}{\bf x}_{i}^{\prime}\right)^{-1}\frac{1}{c_{i}}{\bf x}_{i}\tag{10.9}$$  and  $$e_{i}=y_{i}-{\bf x}_{i}^{\prime}\left(\sum_{i\in A}\frac{1}{\pi_{i}c_{i}}{\bf x}_{i}^{\prime}\right)^{-1}\sum_{i\in A}\frac{1}{\pi_{i}c_{i}}{\bf x}_{i}y_{i}.$$  The $g_{i}$ in (10.9) is the factor to applied to the design weight to satisfy the 
calibration constraint.
Example 10.3. *We now consider the estimation of the variance of the poststratification estimator in (8.27). To estimate the variance, the unconditional* variance estimator is given by

$$\hat{V}_{u}=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)\sum_{g=1}^{G}\frac{n_{g}-1}{n-1}s_{g}^{2}\tag{10.10}$$

where s 2 g = (ng −1)−1Pi∈Ag
(yi −y¯g)
2*. On the other hand, the conditional* variance estimator in (10.8) is given by

$$\hat{V}_{c}=\left(1-\frac{n}{N}\right)\frac{n}{n-1}\sum_{g=1}^{G}\frac{N_{g}^{2}}{n_{g}}\frac{n_{g}-1}{n_{g}}s_{g}^{2}.\tag{10.11}$$

Note that the conditional variance formula in (10.11) is very similar to the variance estimation formula under stratified sampling.

## 10.3 Replication Approach To Variance Estimation

We now consider an alternative approach to variance estimation that is based on several replicates of the original sample estimator. Such a replication approach does not use Taylor linearization, but instead generates several resamples and computes a replicate to each resample. Variability between replicates is used to estimate the sampling variance of the point estimator. Such a replication approach often uses repeated computation of the replicates using a computer. Replication methods include the random group method, jackknife, balanced repeated replication, and the bootstrap method. More details of the replication methods can be found in Wolter (2007).

## 10.3.1 Random Group Method

The random group method was first used in jute acreage surveys **in Bengal**
(Mahalanobis; 1939). The random group method is useful in understanding the basic idea for the replication approach to variance estimation. In the random group method, G **random groups are constructed from the sample, and the** point estimate is calculated for each random group sample and then combined to obtain the final point estimate. Once the final point estimate is constructed, its variance estimate is calculated using the variability of the G **random group**
estimates. There are two versions of the random group method. One is independent random group method and the other is non-independent random group method. We first consider the independent random group **method.**
The independent random group method can be described as follows.

[Step 1] Using the given sampling design, select the first random group sample, denoted by A(1), and compute ˆθ(1), an unbiased estimator of θ **from the**
first random group sample.

[Step 2] Using the same sampling design, select the second random group sample, independently from the first random group sample, and compute ˆθ(2) **from the second random group sample.**
[Step 3] Using the same procedure, obtain G **independent estimate**
ˆθ(1),··· ,
ˆθ(G)from the G **random group sample.**
[Step 4] The final estimator of θ is

$$\hat{\theta}_{\mathrm{RG}}=\frac{1}{G}\sum_{k=1}^{G}\hat{\theta}_{(k)}\tag{10.12}$$

and its unbiased variance estimator is

$$\hat{V}\left(\hat{\theta}_{\mathrm{RG}}\right)=\frac{1}{G}\frac{1}{G-1}\sum_{k=1}^{G}\left(\hat{\theta}_{(k)}-\hat{\theta}_{R G}\right)^{2}.\tag{10.13}$$

Since ˆθ(1),··· ,
ˆθ(G) are independently and identically distributed, the variance estimator in (10.13) is unbiased for the variance of ˆθRG **in (10.12). Such**
independent random group method is very easy to understand and is applicable for complicated sampling designs for selecting A(g), but the sample allows Replication approach to variance estimation 123 for duplication of sample elements and the variance estimator may be unstable when G **is small.**
We now consider non-independent random group method, which **does not**
allow for duplication of the sample elements. In the non-independent random group method, the sample is partitioned into G **groups, exhaustive and**
mutually exclusive, denoted by A = ∪
G
g=1A(g) **and then apply the sample estimation method for independent random group method, by treating the nonindependent random group samples as if they are independent. The following**
theorem expresses the bias of the variance estimator for this case.

Theorem 10.2. Let ˆθ(g) be an unbiased estimator of θ, calculated from the gth random group sample A(g)for g = 1,··· ,G**. Then the random group variance**
estimator (10.13) satisfies

$$E\left\{\hat{V}\left(\hat{\theta}_{\rm RG}\right)\right\}-V\left(\hat{\theta}_{\rm RG}\right)=-\frac{1}{G\left(G-1\right)}\sum\sum\nolimits_{i\neq j}Cov\left(\hat{\theta}_{\left(i\right)},\hat{\theta}_{\left(j\right)}\right)\tag{10.14}$$

Proof. **By (10.12), we have**

V ˆθRG=1 G2 (X G i=1 V ˆθ(i) + XX i6=j Covˆθ(i), ˆθ(j) )(10.15) and, since X G i=1 ˆθ(i) − ˆθRG2= X G i=1 ˆθ(i) −θ 2−G ˆθRG −θ 2 and using E ˆθ(i) = θ, E (X G i=1 ˆθ(i) − ˆθRG2 ) =X G i=1 V ˆθ(i) −G×V ˆθRG =1−G −1X G i=1 V ˆθ(i) −G −1XX i6=j Covˆθ(i), ˆθ(j)  which implies
which implies  $$E\left\{\hat{V}\left(\hat{\theta}_{\rm RG}\right)\right\}=G^{-2}\sum_{i=1}^{G}V\left(\hat{\theta}_{(i)}\right)-G^{-2}\left(G-1\right)^{-1}\sum\sum\nolimits_{i\neq j}Cov\left(\hat{\theta}_{(i)},\hat{\theta}_{(j)}\right).$$  Thus, using (10.15), we have (10.14).  
The right side of (10.14) is the bias of Vˆ
ˆθRG**as an estimator for the**
variance of ˆθRG**. Such bias becomes zero if the sampling for random groups is a**
with-replacement sampling. For without-replacement sampling, the covariance between the two different replicates is negative, and so the bias term becomes positive. The relative amount of bias is often negligible. The following example computes the amount of the relative bias.

Example 10.4. Consider a sample of size n *obtained from simple random* sampling of a finite population of size N. Let b = n/G *be an integer value that* is the size of A(g)*such that* A = ∪
G
g=1A(g). The sample mean of y *obtained* from A(g)is denoted by y¯(g) and the overall mean of y *is given by*

$${\hat{\theta}}={\frac{1}{G}}\sum_{g=1}^{G}{\bar{y}}_{(g)}.$$

In this case, y¯(1),··· ,y¯(G) *are not independently distributed but are identically* distributed with the same mean. By (10.15), we have

$$Var\left(\hat{\theta}\right)=\frac{1}{G}V\left(\bar{y}_{(1)}\right)+\left(1-\frac{1}{G}\right)Cov\left(\bar{y}_{(1)},\bar{y}_{(2)}\right)$$  _and since_  $$V\left(\bar{y}_{(1)}\right)=\left(\frac{1}{b}-\frac{1}{N}\right)S^{2},$$  _we have_  $$Cov\left(\bar{y}_{(1)},\bar{y}_{(2)}\right)=-\frac{1}{N}S^{2}.$$  _Thus, the bias in (10.14) reduces to_  $$\begin{array}{rcl}\mbox{Bias}\left\{\tilde{V}\left(\hat{\theta}_{RG}\right)\right\}&=&-Cov\left(\bar{y}_{(1)},\bar{y}_{(2)}\right)\\ &=&\frac{1}{N}S^{2}\end{array}$$  which is the same. It is the same as the number of 
which is often negligible. Therefore, the random group variance estimator
(10.13) can be safely used to estimate the variance of y¯n *in simple random* sampling.

The random group method provides a useful computational tool for estimating the variance of point estimators. However, the random group method is applicable only when the sampling design for A(g) **has the same structure**
as the original sample A**. The partition** A = ∪
G
g=1A(g)that leads to the unbiasedness of ˆθ(g)**is not always possible for complex sampling designs.**

## 10.4 Jackknife Method

Jackknife was first introduced by Quenouille (1956) to reduce the bias of the ratio estimator and then was suggested by Tukey (1958) to be used for Jackknife method 125 variance estimation. Jackknife is very popular in practice **as a tool for variance** estimation.

To introduce the idea of Quenouille (1956), suppose that n **independent**
observations of (xi,yi**) are available that are generated from a distribution** with mean (µx,µy). If the parameter of interest is θ = µy/µx**, then the sample**
ratio ˆθ = ¯x
−1y¯ **has a bias of order** O
n
−1**. That is, we have**

$$E\left({\hat{\theta}}\right)=\theta+{\frac{C}{n}}+O\left(n^{-2}\right).$$

If we delete the k**-th observation and recompute the ratio**

$${\hat{\theta}}^{(-k)}=\left(\sum_{i\neq k}x_{i}\right)^{-1}\sum_{i\neq k}y_{i},$$  $$E\left({\hat{\theta}}^{(-k)}\right)=\theta+{\frac{C}{n-1}}+O\left(n^{-2}\right).$$
we obtain $\frac{1}{2}$

Thus, the jackknife pseudo value defined by ˆθ(k) = nˆθ − (n−1) ˆθ
(−k)**can be**
used to compute

$$\hat{\theta}_{(.)}=\frac{1}{n}\sum_{k=1}^{n}\hat{\theta}_{(k)}\tag{10.16}$$

which has bias of order O
n
−2**. Thus, the jackknife can be used to reduce**
the bias of nonlinear estimators.

Note that if ˆθ = ¯y then ˆθ(k) = yk**. Tukey (1958) suggested using** ˆθ(k) as an approximate IID observation to obtain the following jackknife variance estimator.

$$\begin{array}{r c l}{{\hat{V}_{\mathrm{JK}}\left(\hat{\theta}\right)}}&{{=}}&{{\frac{1}{n}\frac{1}{n-1}\sum_{k=1}^{n}\left(\hat{\theta}_{(k)}-\bar{\theta}_{(\cdot)}\right)^{2}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\frac{n-1}{n}\sum_{k=1}^{n}\left(\hat{\theta}^{(-k)}-\bar{\theta}^{(\cdot)}\right)^{2}}}\end{array}$$

For the special case of ˆθn = ¯y**, we obtain**

$\hat{\theta}_n=\bar{y}$. 
$${\hat{V}}_{\mathrm{JK}}={\frac{1}{n}}{\frac{1}{n-1}}\sum_{i=1}^{n}\left(y_{i}-{\bar{y}}\right)^{2}={\frac{1}{n}}s_{y}^{2}$$
and the jackknife variance estimator is algebraically equivalent to the usual variance estimator of the sample mean under simple random sampling ignoring the finite population correction term. 126 *Variance Estimation* If we are interested in estimating the variance of ˆθ = f (¯x,y**¯), using** ˆθ
(−k) =
f x¯
(−k),y¯
(−k)**, we can construct**

$$\hat{V}_{\rm JK}\left(\hat{\theta}\right)=\frac{n-1}{n}\sum_{k=1}^{n}\left(\hat{\theta}^{(-k)}-\hat{\theta}\right)^{2}\tag{10.17}$$

as the jackknife variance estimator of ˆθ**. The jackknife replicate** ˆθ
(−k)is computed by using the same formula for ˆθ **using the jackknife weight** w
(k)
i**instead**
of the original weight wi = 1/n**, where**

$$w_{i}^{(-k)}={\left\{\begin{array}{l l}{\left(n-1\right)^{-1}}&{{\mathrm{~if~}}i\neq k}\\ {0}&{{\mathrm{~if~}}i=k.}\end{array}\right.}$$

To discuss the asymptotic property of the jackknife variance estimator in
(10.17), we use the following Taylor expansion, which is often called secondtype Taylor expansion.

Lemma 10.1. Let {Xn,Wn} *be a sequence of random variables such that* Xn = Wn +Op (rn)
where rn → 0 as n → ∞. If g (x) is a function with s**-th continuous derivatives**
in the line segment joining Xn and Wn and the s*-th order partial derivatives* are bounded, then

$$\begin{array}{r c l}{{g\left(X_{n}\right)}}&{{=}}&{{g\left(W_{n}\right)+\sum_{k=1}^{s-1}\frac{1}{k!}g^{\left(k\right)}\left(W_{n}\right)\left(X_{n}-W_{n}\right)^{k}+O_{p}\left(r_{n}^{s}\right)}}\end{array}$$

where g
(k)(a) is the k-th derivative of g (x) *evaluated at* x = a.

Now, since ¯y
(−k) −y¯ = (n−1)−1(¯y −yk**), we have**
y¯
(−k) −y¯ = Op n
−1.

For the case of ˆθ = f (¯x,y**¯), we can apply the above lemma to get**

$$\begin{array}{r c l}{{\hat{\theta}^{(-k)}-\hat{\theta}}}&{{=}}&{{\frac{\partial f}{\partial x}(\bar{x},\bar{y})\left(\bar{x}^{(-k)}-\bar{x}\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{+\frac{\partial f}{\partial y}\left(\bar{x},\bar{y}\right)\left(\bar{y}^{(-k)}-\bar{y}\right)+o_{p}\left(n^{-1}\right)}}\end{array}$$
so that n−1 n Xn k=1 ˆθ (−k) − ˆθ 2 = ∂f ∂x (¯x,y¯) 2n−1 n Xn k=1 x¯ (−k) −x¯ 2+ ∂f ∂y (¯x,y¯) 2n−1 n Xn k=1 y¯ (−k) −y¯ 2 +2∂f ∂x (¯x,y¯) ∂f ∂y (¯x,y¯) n−1 n Xn k=1 x¯ (−k) −x¯ y¯ (−k) −y¯ +op n −1.
Jackknife method 127 Thus, the jackknife variance estimator is asymptotically equivalent to the linearized variance estimator. That is, the second-type Taylor linearization leads to

$$\begin{array}{r c l}{{\hat{V}_{\mathrm{JK}}\left(\hat{\theta}\right)}}&{{=}}&{{\left\{\frac{\partial f}{\partial x}(\bar{x},\bar{y})\right\}^{2}\hat{V}\left(\bar{x}\right)+\left\{\frac{\partial f}{\partial y}(\bar{x},\bar{y})\right\}^{2}\hat{V}\left(\bar{y}\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{+2\left\{\frac{\partial f}{\partial x}(\bar{x},\bar{y})\right\}\left\{\frac{\partial f}{\partial y}(\bar{x},\bar{y})\right\}\hat{C}\left(\bar{x},\bar{y}\right)+o_{p}\left(n^{-1}\right).}}\end{array}$$

The above jackknife method is constructed under simple random sampling.

For multistage stratified sampling, jackknife replicates can be constructed by removing a cluster for each replicate. Let

$${\hat{Y}}_{\mathrm{HT}}=\sum_{h=1}^{H}\sum_{i=1}^{n_{h}}w_{h i}{\hat{Y}}_{h i}$$

be the HT estimator of Y **under stratified multistage cluster sampling. The** jackknife weights are constructed by deleting a cluster sequentially as

$$w_{h i}^{(-g j)}=\left\{\begin{array}{l l}{{0}}&{{\mathrm{if~}h=g{\mathrm{~and~}}i=j}}\\ {{(n_{h}-1)^{-1}\,n_{h}w_{h i}}}&{{\mathrm{if~}h=g{\mathrm{~and~}}i\neq j}}\\ {{w_{h i}}}&{{\mathrm{otherwise}}}\end{array}\right.$$

and the jackknife variance estimator is computed by

$$\hat{V}_{\rm JK}\left(\hat{Y}_{\rm HT}\right)=\sum_{h=1}^{H}\frac{n_{h}-1}{n_{h}}\sum_{i=1}^{n_{h}}\left(\hat{Y}_{\rm HT}^{(-h\,i)}-\frac{1}{n_{h}}\sum_{j=1}^{n_{h}}\hat{Y}_{\rm HT}^{(-h\,j)}\right)^{2}\tag{10.18}$$

where

$${\hat{Y}}_{\mathrm{HT}}^{(-g j)}=\sum_{h=1}^{H}\sum_{i=1}^{n_{h}}w_{h i}^{(-g j)}{\hat{Y}}_{h i}.$$

The following theorem presents the algebraic property of the jackknife variance estimator in (10.18).

Theorem 10.3. *The jackknife variance estimator in (10.18) is algebraically* equivalent to the simplified variance estimator in (10.4).

If $\hat{\theta}=f\left(\hat{X}_{\text{HT}},\hat{Y}_{\text{HT}}\right)$ then the jackk:  $\hat{\theta}^{(-gj)}=f\left(\hat{X}_{\text{HT}}^{(-gj)},\hat{Y}_{\text{HT}}^{(-gj)}\right).$ In this case, is computed as 
XˆHT,YˆHT**then the jackknife replicates are constructed as**
HT **. In this case, the jackknife variance estimator**
$$\hat{V}_{\rm JK}\left(\hat{\theta}\right)=\sum_{h=1}^{H}\frac{n_{h}-1}{n_{h}}\sum_{i=1}^{n_{h}}\left(\hat{\theta}^{(-hi)}-\frac{1}{n_{h}}\sum_{j=1}^{n_{h}}\hat{\theta}^{(-hj)}\right)^{2}\tag{10.19}$$
128 *Variance Estimation* or, more simply,

$$\hat{V}_{\rm JK}\left(\hat{\theta}\right)=\sum_{h=1}^{H}\frac{n_{h}-1}{n_{h}}\sum_{i=1}^{n_{h}}\left(\hat{\theta}^{(-hi)}-\hat{\theta}\right)^{2}.\tag{10.20}$$

The asymptotic properties of the above jackknife variance estimator under stratified multistage sampling can be established. For references, see Krewski and Rao (1981) or Shao and Tu (1995).

Example 10.5. *We now revisit Example 10.3 to estimate the variance of the* post-stratification estimator using the jackknife. For simplicity, assume that SRS for the sample. The post-stratification estimator is calculated as

$$\hat{Y}_{\mathrm{post}}=\sum_{g=1}^{G}N_{g}\bar{y}_{g},$$

where y¯g = n
−1 gPi∈Ag yi. Now, the k*-th replicate of* Yˆ**post** is

$$\hat{Y}_{\mathrm{post}}^{(-k)}=\sum_{g\neq h}N_{g}\bar{y}_{g}+N_{h}\bar{y}_{h}^{(-k)}$$
$$Y_{\rm post}^{(-\kappa)}=\sum_{g\neq h}N_{g}\bar{y}_{g}+N_{h}\bar{y}_{h}^{(-\kappa)}$$  _where $\bar{y}_{h}^{(-k)}=(n_{h}-1)^{-1}(n_{h}\bar{y}_{h}-y_{k})$. Thus,_  $$\hat{Y}_{\rm post}^{(-k)}-\hat{Y}_{\rm post}=N_{h}\left(\bar{y}_{h}^{(-k)}-\bar{y}_{h}\right)$$ $$=N_{h}\left(n_{h}-1\right)^{-1}(\bar{y}_{h}-y_{k})$$  _and_
$$=\quad N_{h}\left(n_{h}-1\right)\quad\left(y_{h}-y_{k}\right)$$  $$\hat{V}_{\rm JK}\left(\hat{Y}_{\rm post}\right)=\frac{n-1}{n}\sum_{k=1}^{n}\left(\hat{Y}_{\rm post}^{\left(-k\right)}-\hat{Y}_{\rm post}\right)^{2}$$ $$=\frac{n-1}{n}\sum_{g=1}^{G}N_{g}^{2}\left(n_{g}-1\right)^{-1}s_{g}^{2},$$

which, ignoring n/N term, is asymptotically equivalent to the conditional variance estimator in (10.11).

## Two-Phase Sampling 11.1 Introduction

The two-phase sampling design is a sampling design where sample selection is performed in two phases. I the first phase, the auxiliary variable x is observed, and in the second phase, the study variable y **is observed. The** second phase sample is a subset of the first phase sample.

Two-phase sampling is particularly attractive when the cost of observing x is relatively low compared to the cost of observing y**. To formalize the concept,** two-phase sampling can be described as follows:
[Step 1] From the finite population, s a first-phase sample A1 **of size** n1 is selected, and the auxiliary variable x **is observed.**
[Step 2] The first-phase sample A1 **is treated as a finite population, and a**
second-phase sample A2 of size n2 **is selected from it. Study variable** y is observed in the second-phase sample. The probability of selection for the second phase sample is often determined by the values of x **obtained from**
the first-phase sample.

Since the second-phase sample selection probability depends on the observed values of the first-phase sample, the sample inclusion probability for the second-phase sample is a random variable that changes as **the first-phase** sample changes. In this case, the standard Horvitz-Thompson (HT) estimation theory is not directly applicable.

To discuss this further, note that the overall first-order inclusion probability for the two-phase sampling design is

$$\pi_{i}=P r\left(i\in A_{2}\right)=\sum_{A_{2};i\in A_{2}}P\left(A_{2}\right)$$  $$P\left(A_{2}\right)=\sum_{A_{1};A_{2}\subset A_{1}}P_{2}\left(A_{2}\mid A_{1}\right)P_{1}\left(A_{1}\right).$$

where

Here, P1 (·**) is the sample selection probability for the first-phase sample, and** P2 (· | A1**) is the sample selection probability for the second-phase sample,**
130 *Two-phase sampling* which is conditional on the first-phase sample. Thus,

$$\begin{array}{r c l}{{\pi_{i}}}&{{=}}&{{\sum_{\left\{A_{2};\;i\in A_{2}\right\}\left\{A_{1};A_{2}\subset A_{1}\right\}}P_{2}\left(A_{2}\mid A_{1}\right)P_{1}\left(A_{1}\right)}}\\ {{}}&{{=}}&{{\sum_{\left\{A_{1};\;i\in A_{1}\right\}\left\{A_{2};A_{2}\subset A_{1}\&i\in A_{2}\right\}}}}\\ {{}}&{{=}}&{{\sum_{\left\{A_{1};\;i\in A_{1}\right\}\left\{A_{2};\;i\in A_{2}\right\}}P_{2}\left(A_{2}\mid A_{1}\right)P_{1}\left(A_{1}\right).}}\end{array}$$  In the equality above, we have to show that $i$ is a probability of such 
If we define the conditional first-order inclusion probability for the secondphase sampling as π
(2)
i|A1

= P r (i ∈ A2 | A1)
then the first order inclusion probability is

$$\pi_{i}=\sum_{A_{1};\;i\in A_{1}}\pi_{i|A_{1}}^{(2)}P_{1}\left(A_{1}\right)$$ $$=E_{1}\left(\pi_{i|A_{1}}^{(2)}\right),$$

where E1 (·**) is the expectation with respect to the first-phase sampling. Here,**
the conditional first-order inclusion probability π
(2)
i|A1 is a random variable in the sense that it is a function of x in the first phase sample A1**. The conditional**
expectation (11.1) cannot be computed because we have a single realization of the first-phase sample A1.

If the sampling design satisfies the invariance condition, as is the case in two-stage sampling, then the conditional first-order inclusion probability π
(2)
i|A1 is equal to the unconditional first-order inclusion probability π
(2)
i**. On**
this case, by (11.1), we have

$$\begin{array}{r c l}{{\pi_{i}}}&{{=}}&{{\sum_{\begin{array}{c}{{A_{1};\;\;i\in A_{1}}\end{array}}}\;P_{1}\left(A_{1}\right)\pi_{i}^{(2)}}}\\ {{}}&{{=}}&{{\pi_{i}^{(1)}\pi_{i}^{(2)}.}}\end{array}$$

In this scenario, where the sampling design satisfies the invariance condition, the Horvitz-Thompson (HT) estimator can be directly implemented.

To discuss unbiased estimation for two-phase sampling, let's first consider the following quantity

$${\hat{Y}}_{1}=\sum_{i\in A_{1}}{\frac{y_{i}}{\pi_{i}^{(1)}}}.$$

This is an unbiased estimator for the population total of y**. The task is now**
to construct an unbiased estimator of Yˆ1 **using the two-phase sample.**
Applying the Horvitz-Thompson (HT) estimation idea conditionally, we
obtain
$$\hat{Y}^{*}=\sum_{i\in A_{2}}\frac{y_{i}}{\pi_{i}^{(1)}\pi_{i|A_{1}}^{(2)}}.$$

$$(11.2)$$

If we define π
∗
i = π
(1)
iπ
(2)
i|A1

, then (11.2) can be written as Yˆ ∗ =Pi∈A2 yi/π∗
i
.

This conditionally unbiased estimator (11.2) is sometimes **called the** π
∗-
estimator.

The π
∗-estimator is conditional unbiased to Yˆ1**, which is itself an unbiased**
estimator of the population total Y **. Therefore, the** π
∗**estimator is unbiased**
unconditionally.

The variance of the π
∗**-estimator is given by**

$$V\left(\hat{Y}^{*}\right)=V\left\{E\left(\hat{Y}^{*}\mid A_{1}\right)\right\}+E\left\{V\left(\hat{Y}^{*}\mid A_{1}\right)\right\}\tag{11.3}$$ $$=V\left\{\sum_{i\in A_{1}}\frac{y_{i}}{\pi_{i}^{(1)}}\right\}+E\left\{\sum_{i\in A_{1}}\sum_{j\in A_{1}}\left(\pi_{ij|A_{1}}^{(2)}-\pi_{i|A_{1}}^{(2)}\pi_{j|A_{1}}^{(2)}\right)\frac{y_{i}}{\pi_{i}^{*}}\frac{y_{j}}{\pi_{j}^{*}}\right\}.$$

Here, π
(2)
ij|A1

= P r (i ∈ A2, j ∈ A2 | A1**) is the conditional joint inclusion probability. The variance expression in (11.3) has two parts: the first part is the**
variance due to the first-phase sampling, and the second part **is the variance**
due to the second-phase sampling.

## 11.2 Two-Phase Sampling For Stratification

Stratified sampling is one of the most popular sampling methods for improving the efficiency of point estimators. To apply stratified sampling, the stratification variables need to be available for the finite population. If that is not the case, the two-phase sampling approach can be used.

Let xi = (xi1*,...,x*iH**) be the vector of stratification variables, where** xih takes the value 1 if unit i belongs to stratum h**, and 0 otherwise. In this case,**
the auxiliary variable x **is not available in the finite population.**
The two-phase sampling for stratification can be described as follows:

1. Perform a simple random sample (SRS) of size n **from the finite population and obtain** Pi∈A1 xi = (n1,n2*,...,n*H**) where** n =PH
h=1 nh.

2. Among the nh elements in each stratum, select rh elements independently by SRS, where rh **is determined after when the first-phase**
sample is selected.
This two-phase sampling approach allows the stratification **variables to be** obtained, even when they are not directly available in the finite population.

In this two-phase sampling design, the realized sample size nh **in stratum** h is a random variable, and it follows an approximate multinomial distribution:
(n1,n2,...,nH) ∼ MN (n;W1,W2,...,WH)
132 *Two-phase sampling* where MN (n;p) denotes the multinomial distribution with parameter p**, and**
Wh = Nh/N **is the population proportion of stratum** h.

This means that the realized sample sizes across the strata follow a multinomial distribution, with the population stratum proportions Wh as the underlying probabilities, and the total sample size n **as the number of trials.**
In this two-phase sampling, the π
∗**-estimator of the population mean of** y is

$\dot{Y}_{\rm tp}=\sum_{h=1}^{H}w_{h}\bar{y}_{h2}$ (11.4)
where wh = nh/n **and ¯**yh2 = r
−1 hPi∈A2 xihyi**. Since the expectation of** wh =
nh/n is Wh = Nh/N**, the** π
∗**-estimator in (11.4) can be viewed as the stratified**
sample estimator when the stratum size Wh **is unknown. The total variance**
is, by (11.3), obtained as

$$V\left(\hat{Y}_{\rm tp}\right)=\left(\frac{1}{n}-\frac{1}{N}\right)S^{2}+E\left\{\sum_{h=1}^{H}\left(\frac{n_{h}}{n}\right)^{2}\left(\frac{1}{r_{h}}-\frac{1}{n_{h}}\right)s_{h1}^{2}\right\}\tag{11.5}$$

where
$$s_{h1}^{2}=\frac{1}{n_{h}-1}\sum_{i\in A_{1}}x_{i h}\left(y_{i}-{\bar{y}}_{h1}\right)^{2}$$  $s_{h1}^{-1}\nabla$
and $\bar{y}_{h1}=n_{h}^{-1}\sum_{i\in A_{1}}x_{ih}y_{i}$.  Also, if we define $\bar{y}_{1}=n^{-1}\sum_{h=1}^{H}n_{h}\bar{y}_{h1}$ and 

$$s_1^2\quad=\quad\frac{1}{n-1}\sum_{i\in A_1}(y_i-\bar{y}_1)^2$$. 

then we have $E\left(s_1^2\right)=S^2$ and. 
$$s_{1}^{2}\quad=\quad\sum_{h=1}^{H}\left\{\frac{n_{h}}{n-1}\,(\bar{y}_{h1}-\bar{y}_{1})^{2}+\frac{n_{h}-1}{n-1}s_{h1}^{2}\right\}.$$
Thus, (11.5) is approximately equal to

$$V\left(\hat{\tilde{Y}}_{\mathrm{tp}}\right)=E\left\{n^{-1}\sum_{h=1}^{H}w_{h}\left(\bar{y}_{h1}-\bar{y}_{1}\right)^{2}+\sum_{h=1}^{H}r_{h}^{-1}w_{h}^{2}s_{h1}^{2}\right\}.$$
$$(11.6)$$
. **(11.6)**
Here, the finite population correction term is ignored. The variance formula in
(11.6) is expressed as the sum of two terms. One is a function of the betweenstratum variance, and the other is a function of the within-stratum variance.

In computing the between-stratum variance, we used the full **sample size** n.

However, in computing the within-stratum variance, we only **used the smaller**
sample size rh within each stratum.

Therefore, if the between-stratum variance is larger than the withinstratum variance, the efficiency of the two-phase sampling estimator increases.

This is because the between-stratum variance is estimated more precisely using the larger sample size n**, compared to the within-stratum variance estimated**
with the smaller sample size rh.

In addition, the variance formula in (11.6) provides a way to **estimate the**
variance. Since (11.6) is expressed as an expectation of quantities that can be computed from the first-phase sample, we can use ¯yh2 and s 2 h2 instead of ¯yh1 and s 2 h1
, respectively, in (11.6). Thus,

$$\hat{V}\left(\hat{Y}_{\rm tp}\right)=E\left\{n^{-1}\sum_{h=1}^{H}w_{h}\left(\bar{y}_{h2}-\hat{Y}_{tp}\right)^{2}+\sum_{h=1}^{H}r_{h}^{-1}w_{h}^{2}s_{h2}^{2}\right\}\tag{11.7}$$

is an approximately unbiased estimator of the variance in (11.6). Rao (1973)
developed a formal theory for the two-phase sampling for stratification. Alternatively, instead of (11.7), we can also use the Jackknife method to estimate the variance of the two-phase sampling estimator. See Kim et **al. (2006) for** more details.

To compare the variance (11.6) of the two-phase sampling estimator with that of the simple random sampling (SRS) estimator of equal sample size r =PH
h=1 rh**, note that**

$$V\left(\hat{\tilde{Y}}_{\mathrm{SRS}}\right)=E\left\{r^{-1}\sum_{h=1}^{H}w_{h}\left(\bar{y}_{h1}-\bar{y}_{1}\right)^{2}+r^{-1}\sum_{h=1}^{H}w_{h}s_{h1}^{2}\right\}.$$

Therefore, the difference in variances is

$$V\left(\hat{Y}_{\mathrm{SRS}}\right)-V\left(\hat{Y}_{\mathrm{tp}}\right)=E\left\{\left(\frac{1}{r}-\frac{1}{n}\right)\sum_{h=1}^{H}w_{h}\left(\bar{y}_{h1}-\bar{y}_{1}\right)^{2}+\sum_{h=1}^{H}\left(\frac{1}{r}-\frac{w_{h}}{r_{h}}\right)w_{h}s_{h1}^{2}\right\}.$$
.
The first term is always positive, as *r < n***. The second term is zero under**
proportional allocation (rh = rwh**), but it can be made positive for optimal**
allocation.

This shows that the two-phase sampling estimator can be more **efficient**
than the SRS estimator, depending on the relative magnitudes of the betweenstratum and within-stratum variances and by choosing the optimal sample-size allocation for the second-phase sampling.

To discuss optimal allocation, first consider the cost function. The total cost can be expressed as

$$C=c_{1}n+\sum_{h=1}^{H}c_{2h}r_{h}$$

and, writing νh = rh/nh, the optimal allocation can be determined by mini134 *Two-phase sampling*

$${\mathrm{subject~to~}}$$
$$V=\frac{1}{n}\left\{\left(S^{2}-\sum_{h=1}^{H}W_{h}S_{h}^{2}\right)+\sum_{h=1}^{H}W_{h}S_{h}^{2}\frac{1}{\nu_{h}}\right\}$$  $$C=n\left(c_{1}+\sum_{h=1}^{H}c_{2h}W_{h}\nu_{h}\right).$$  In the following we have shown that $\mathcal{S}$ is the set of $n$-th order 
To find the optimal allocation, we have only to find the set of νh's that minimizes V ×C**. The optimal solution is**

$$\nu_{h}^{*}=\left(\frac{c_{1}}{c_{2h}}\times\frac{S_{h}^{2}}{S^{2}-\sum_{h=1}^{H}W_{h}S_{h}^{2}}\right)^{1/2}\tag{11.8}$$

which lead to

$$\frac{r_{h}^{*}}{n^{*}}=W_{h}\nu_{h}^{*}=W_{h}\left(\frac{c_{1}}{c_{2h}}\right)^{1/2}\left(\frac{S_{h}^{2}}{S^{2}-\sum_{h=1}^{H}W_{h}S_{h}^{2}}\right)^{1/2}.\tag{11.9}$$

If c2h = c2 and S
2 h = S
2w for all h**, then**

$$\frac{r^{*}}{n^{*}}=\left(\frac{c_{1}}{c_{2}}\right)^{1/2}\left(\frac{1}{\phi-1}\right)^{1/2}\tag{11.10}$$

where

$$\phi={\frac{S^{2}}{S_{w}^{2}}}$$

denotes the relative efficiency due to stratification (under proportional allocation). If c2 = 10c1 and φ = 2 then r/n =
√0.1 = 0.32.

The two-phase sampling for stratification is also a useful method for estimating parameters of subpopulations defined by specific eligibility criteria.

For example, if the population of interest is not the entire population, but a subpopulation with certain attributes, and information on **these attributes is** not available in the population frame, the two-phase sampling approach can be employed. In the first phase, the information on eligibility can be obtained from the initial sample. This allows the population to be stratified based on the eligibility criteria. Then, in the second phase, a sample is selected from the stratum of eligible groups, and the variable of interest y **is observed.**
For instance, consider a survey where the target population **is households**
with members over the age of 60. Since there may not be a household population frame with age group information, the two-phase sampling for stratification can be applied. The first phase would identify the eligible households, and the second phase would sample from this stratum of eligible households to observe the variable of interest.

This approach enables efficient estimation of parameters for **subpopulations defined by specific eligibility criteria, even when that information is not**
directly available in the population frame.

mizing

## 11.3 Regression Estimator For Two-Phase Sampling

In the previous section, the auxiliary variable x **obtained from the firstphase sample was used to design the sampling mechanism for the second-phase**
sampling. In this section, we consider the case where the auxiliary variable is used in the estimation stage, rather than used in the sampling design.
To illustrate the idea, assume the first-phase sample is a simple random
sample of size n**, and the second-phase sample is also a simple random sample**
of size r from the first-phase sample. Since we observe xi **in the first-phase**
sample, we can compute:
$${\bar{\mathbf{x}}}_{1}={\frac{1}{n}}\sum_{i\in A_{1}}\mathbf{x}_{i}$$
from the first-phase sample, and

$$\mathrm{le,~and~}$$
$$({\bar{\mathbf{x}}}_{2},{\bar{y}}_{2})={\frac{1}{r}}\sum_{i\in A_{2}}\left(\mathbf{x}_{i},y_{i}\right)$$

from the second-phase sample.

The two-phase regression estimator is then computed as

$${\bar{y}}_{\mathrm{reg,tp}}={\bar{y}}_{2}+\left({\bar{\mathbf{x}}}_{1}-{\bar{\mathbf{x}}}_{2}\right)^{\prime}{\hat{B}}$$
′ Bˆ **(11.11)**
$$\mathrm{where}$$
$$(11.11)$$
$$\hat{B}=\left(\sum_{i\in A_{2}}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\sum_{i\in A_{2}}\mathbf{x}_{i}y_{i}.$$

This two-phase regression estimator utilizes the auxiliary information x obtained from the first-phase sample to improve the estimation **of the population**
mean Y¯ .

Now, to discuss its statistical properties, note that Bˆ − B = Op(r
−1/2).

Thus, we can express have

$${\bar{y}}_{\mathrm{reg,tp}}={\bar{y}}_{2}+\left({\bar{\mathbf{x}}}_{1}-{\bar{\mathbf{x}}}_{2}\right)^{\prime}B+O_{p}\left(r^{-1}\right)$$
$$y_{\rm reg,tp}-y_{2}+({\bf x}_{1}-{\bf x}_{2})\ B+O_{p}\left(t^{\prime}\right)$$  and obtain  $$V\left(\bar{y}_{\rm reg,tp}\right)\doteq B^{\prime}V\left(\bar{\bf x}_{1}\right)B+V\left(\bar{e}_{2}\right)\tag{11.12}$$  where  $$\bar{e}_{2}=\frac{1}{r}\sum_{i\in A_{2}}\left(y_{i}-{\bf x}_{i}^{\prime}B\right).$$  The variance of $\bar{y}_{\rm reg,tp}$ is then determined. In (11.12), the total variance con 

The variance of ¯yreg,tp **is then determined. In (11.12), the total variance consists of two components:**
1. The variance explained by the regression on ¯x1, given by B′V (¯x1)B.

136 *Two-phase sampling* 2. The variance of the mean of the residuals from the second-phase sample, V (¯e2).

Therefore, under the SRS under both phases, Under simple random sampling (SRS) in both phases, the specific forms of these variance terms are provided below:

$$V\left(\bar{y}_{\rm reg,tp}\right)\doteq\left(\frac{1}{n}-\frac{1}{N}\right)B^{\prime}S_{xx}B+\left(\frac{1}{r}-\frac{1}{N}\right)S_{ee}\tag{11.13}$$

where

$$\begin{array}{r c l}{{S_{x x}}}&{{=}}&{{\frac{1}{N-1}\sum_{i=1}^{N}\left(\mathbf{x}_{i}-{\bar{\mathbf{x}}}_{N}\right)\left(\mathbf{x}_{i}-{\bar{\mathbf{x}}}_{N}\right)^{\prime}}}\\ {{}}&{{}}&{{}}\\ {{S_{e e}}}&{{=}}&{{\frac{1}{N-1}\sum_{i=1}^{N}\left(e_{i}-{\bar{e}}_{N}\right)^{2}.}}\end{array}$$

The first term in (11.13) is the variance term explained by ¯x1 **and the second** term in (11.13) is the variance of ¯yreg,tp **that is not explained by** x.

Note that the efficiency gain due to two-phase sampling can be computed as

$$\begin{array}{r c l}{{V\left(\bar{y}_{2}\right)-V\left(\bar{y}_{\mathrm{reg,tp}}\right)}}&{{=}}&{{\left(\frac{1}{r}-\frac{1}{n}\right)B^{\prime}S_{x x}B.}}\end{array}$$

The gain is larger when the regression relationship is strong (large B′*SxxB*)
and when the second-phase subsample is much smaller than the **first-phase** sample (small r/n).

For variance estimation, we can use (11.13) and estimate each component of the sample separately. That is, we may use

$$\hat{V}\left(\bar{y}_{\rm reg,tp}\right)\doteq\left(\frac{1}{n}-\frac{1}{N}\right)\hat{B}^{\prime}\hat{S}_{xx,1}B+\left(\frac{1}{r}-\frac{1}{N}\right)\hat{S}_{ee,2}\tag{11.14}$$

where

$$\begin{array}{r c l}{{\hat{S}_{x x,1}}}&{{=}}&{{\frac{1}{n-1}\sum_{i\in A_{1}}\left(\mathbf{x}_{i}-{\bar{\mathbf{x}}}_{1}\right)\left(\mathbf{x}_{i}-{\bar{\mathbf{x}}}_{1}\right)^{\prime}}}\\ {{}}&{{}}&{{}}\\ {{\hat{S}_{e e,2}}}&{{=}}&{{\frac{1}{r-1}\sum_{i\in A_{2}}\left(y_{i}-\mathbf{x}_{i}^{\prime}{\hat{B}}\right)^{2}.}}\end{array}$$

If jackknife is used, one should take into account the sampling variability of x¯1 **in the two-phase regression estimator. See Sitter (1997) and Fuller (1998)**
for more details.

Now, suppose the total cost C is given by C = c0 +c1n+c2r**, where** c0,c1 and c2 are known constants, and the sample sizes n and r are to be determined.

Regression estimator for two-phase sampling 137 We wish to find the sample sizes that minimize the variance expression in (11.13), given the total cost C.

Defining ν = r/n, we can express the variance times the term (C −c0**) as**

$$\begin{array}{r c l}{{V\times(C-c_{0})}}&{{=}}&{{(c_{1}+\nu c_{2})\left(B^{\prime}S_{x x}B+\frac{1}{\nu}S_{e e}\right)}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{\mathrm{Const.}+c_{2}B^{\prime}S_{x x}B\nu+c_{1}S_{e e}\frac{1}{\nu}.}}\end{array}$$

The optimal value of ν **that minimizes this expression is**

$$\nu^{*}=\left(\frac{c_{1}}{c_{2}}\times\frac{S_{ee}}{B^{\prime}S_{xx}B}\right)^{1/2}.\tag{11.15}$$  In the case of all 
This optimal ν
∗**can be interpreted as follows:**

1. If the regression model has strong predictive power (large B′SxxB),
then ν
∗**can be reduced, as the regression estimation becomes more**
effective.

2. If the cost of observing y **is quite high compared to the cost of**
observing x (large c2/c1**), then** ν
∗**can be reduced.**
Once ν
∗**is obtained from (11.15), the optimal value of** n
∗**can be found by**
solving the total cost equation C = c0 +c1n+c2nν∗
with respect to n.

We now consider the general situation where the first-phase sampling is not necessarily the simple random sampling. For general two-phase sampling designs, the two-phase regression estimator can be written as

$$\hat{Y}_{\rm reg,tp}=\sum_{i\in A_{1}}w_{1i}{\bf x}^{\prime}_{i}\hat{\beta}_{2}+\sum_{i\in A_{2}}w_{1i}\frac{1}{\pi_{2i|1}}\left(y_{i}-{\bf x}^{\prime}_{i}\hat{\beta}_{2}\right).\tag{11.16}$$

where $w_{1i}=1/\pi_{i}^{(1)}$ are the first-phase sampling weights, $\pi_{2i|1}=\pi_{i|A_{1}}^{(2)}$ are the 

conditional second-phase inclusion probabilities, and βˆ2 is the regression coefficient estimated from the second-phase sample. This formulation generalizes the previous expression for the two-phase regression estimator, which assumed simple random sampling in both phases. The key distinction is the incorporation of the general sampling weights and probabilities to **account for more**
complex sampling designs in the first and second phases.

Notably, the asymptotic unbiasedness of the two-phase regression estimator in equation (11.16) holds regardless of the specific method used to obtain the estimate βˆ2**from the second-phase sample. This property enhances the**
flexibility and applicability of this estimator in practical settings with diverse sampling schemes. 138 *Two-phase sampling* Now, if we assume that the vector xi **includes** π
−1 2i|1 such that x
′
i a = π
−1 2i|1 for some vector a**, the two-phase regression estimator in equation (11.16) can**
be shown to be algebraically equivalent to the following form:

$${\hat{Y}}_{\mathrm{reg,tp}}=\sum_{i\in A_{1}}w_{1i}\mathbf{x}_{i}^{\prime}{\hat{\beta}}_{2}$$

iβˆ2**(11.17)**
$$(11.17)$$
$$\hat{\beta}_{2}=\left(\sum_{i\in A_{2}}w_{1i}{\bf x}_{i}{\bf x}_{i}^{\prime}\right)^{-1}\sum_{i\in A_{2}}w_{1i}{\bf x}_{i}y_{i}.\tag{11.18}$$

This alternative form in equation (11.17) takes the structure of a projection estimator, as discussed in Kim and Rao (2012). In other words, the two-phase regression estimator can be expressed as a projection of the **observations onto**
the space spanned by the covariates xi**, with the projection coefficients given**
by βˆ2
.

Importantly, this projection estimator formulation in (11.17) is asymptotically design-unbiased, as the following condition holds:

$$\sum_{i\in A_{2}}w_{1i}\frac{1}{\pi_{2i|1}}\left(y_{i}-{\bf x}_{i}^{\prime}\hat{\beta}_{2}\right)=0\tag{11.19}$$

holds. This property ensures the asymptotic unbiasedness of the two-phase regression estimator under the assumed condition of the covariate vector xi.

To compute the asymptotic variance of the two-phase regression estimator in equation (11.16), we define β
∗to be the probability limit of the regression coefficient estimate βˆ2**. In this case, since** βˆ2 − β
∗ = Op(n
−1/2**), we can**
establish the following linearized representation of the two-phase regression estimator:
Yˆreg,tp = Yˆreg,tp,ℓ +Op(n
−1N**) (11.20)**
where the linearized estimator is given by

$$\hat{Y}_{\rm reg,tp,}\ell=\sum_{i\in A_{1}}w_{1i}{\bf x}^{\prime}_{i}\beta^{*}+\sum_{i\in A_{2}}w_{1i}\frac{1}{\pi_{2i|1}}\left(y_{i}-{\bf x}^{\prime}_{i}\beta^{*}\right).\tag{11.21}$$

This linearized form (11.21) reveals that the two-phase regression estimator Yˆreg,tp **can be expressed as the sum of a weighted mean of the first-phase**
covariates xi **multiplied by the probability limit** β
∗**, and a weighted sum of**
the residuals yi − x
′
i β
∗**from the second-phase observations. The remainder**
term Op(n
−1N**) vanishes asymptotically as the sample sizes increase.**
This linearized representation will facilitate the subsequent derivation of the asymptotic variance of the two-phase regression estimator, which can be obtained by analyzing the properties of the component terms **in equation**
(11.21).

where Regression estimator for two-phase sampling 139 Under some regularity conditions, the asymptotic variance of the twophase regression estimator Yˆreg,tp **is equivalent to the variance of the two-phase**
linearized estimator (or difference estimator) defined in equation (11.21). This variance can be expressed as

$$V\left(\hat{Y}_{\text{diff},\text{tp}}\right)=V\left(\sum_{i\in A_{1}}w_{1i}y_{i}\right)+E\left[V\left\{\sum_{i\in A_{2}}w_{1i}\frac{1}{\pi_{2i|1}}\left(y_{i}-\mathbf{x}_{i}^{\prime}\beta^{*}\right)\mid A_{1}\right\}\right].\tag{11.22}$$  If the second-phase sampling follows a Poisson scheme, then the second term 

in the above expression can be simplified to
$$V_{2}=E\left\{\sum_{i\in A_{1}}w_{1i}^{2}\left({\frac{1}{\pi_{2i|1}}}-1\right)e_{i}^{2}\right\}$$

where ei = yi −x
′
iβ
∗.

The optimal choice of the conditional second-phase inclusion probabilities π
∗
2i|1 that minimizes the variance V2 is

$$\pi_{2i\mid1}^{*}\propto w_{1i}\left[E\left\{e_{i}^{2}\mid\mathbf{x}_{i}\right\}\right]^{1/2}.$$
$$\left(11.23\right)$$. 
This optimal design of the second-phase sampling probabilities depends on the conditional variance of the residuals ei given the covariates xi**, as well as**
the first-phase sampling weights w1i.

The derivation of this asymptotic variance expression and the optimal sampling design result provides a framework for determining efficient twophase sampling strategies in practical applications.

If both phase samples are SRS, the above variance formula reduces to

$$V\left(\hat{Y}_{\mathrm{diff,tp}}\right)=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right)S_{y}^{2}+\left(\frac{N^{2}}{n}\right)^{2}\frac{n^{2}}{r}\left(1-\frac{r}{n}\right)S_{e}^{2}$$ $$=N^{2}\left(\frac{1}{n}-\frac{1}{N}\right)\left(S_{y}^{2}-S_{e}^{2}\right)+N^{2}\left(\frac{1}{r}-\frac{1}{N}\right)S_{e}^{2}$$  which is consistent with the result in (11.13).  
We now consider variance estimation for two-phase regression estimator.

Note that using the linearization formula in (11.20), we can **express**

$\hat{Y}_{\rm reg,tp,\ell}=\sum_{i\in A_{1}}w_{1i}\eta_{i}$ (11.24)

where $$\eta_{i}=\mathbf{x}_{i}^{\prime}\beta^{*}+\frac{\delta_{i}}{\pi_{2i}}\left(y_{i}-\mathbf{x}_{i}^{\prime}\beta^{*}\right)$$ is the influence function of the two-phase regression estimator and 
$$\delta_{i}=\left\{\begin{array}{c c}{{1}}&{{1}}\\ {{0}}&{{0}}\end{array}\right.$$
1 if i ∈ A2 **when is sampled in** A1 0 otherwise.

This formulation expresses the linearized two-phase regression estimator as a weighted sum of the influence functions ηi**, where the weights are the firstphase sampling weights** w1i.

The key aspects to note are:

1. The influence function ηi combines the contribution from the firstphase covariates xi **and the residual** yi−x
′
iβ
∗**from the second-phase**
observations, scaled by the inverse of the conditional second-phase inclusion probability π2i|1.

2. The indicator δi tracks whether the i**-th unit was selected in the**
second-phase sample, given that it was included in the first-phase sample.
This representation of the linearized two-phase regression estimator will facilitate the subsequent development of variance estimation procedures, as the variance can be expressed in terms of the influence functions ηi.

Note that the indicators δi **are defined across the entire finite population,**
not just the sampled units in A1. While we only observe the values of δi for i ∈ A1, we can still conceptualize the δi as being defined for all i = 1*,...,N* in the population.

Given this view of the finite population, we can apply the *reverse framework* of Fay (1992), Shao and Steel (1999), and Kim et al. (2006). In this framework, the finite population consists of two components: RN = {δ1,δ2*,...,δ*N }
and FN = {(xi,yi);i = 1*,...,N*}. The sample A1 **is then selected from this**
population according to a probability sampling design. We observe δi and xi for i ∈ A1, and observe yi for the units with δi **= 1.**
Using this setup, the total variance of the linearized two-phase regression estimator Yˆreg,tp,ℓ **can be expressed as**

$V\left(Y_{\text{reg.tp},\ell}\right)$  $$E\left\{V\left(\sum_{i\in A_{1}}w_{1i}\eta_{i}\mid\mathcal{R}_{N},\mathcal{F}_{N}\right)\mid\mathcal{F}_{N}\right\}+V\left\{E\left(\sum_{i\in A_{1}}w_{1i}\eta_{i}\mid\mathcal{R}_{N},\mathcal{F}_{N}\right)\mid\mathcal{F}_{N}\right\}$$ $$E\left\{\sum_{i=1}^{N}\sum_{j=1}^{N}\left(\pi_{1ij}-\pi_{1i}\pi_{1j}\right)\eta_{i}\eta_{j}\mid\mathcal{F}_{N}\right\}+V\left\{\sum_{i=1}^{N}\eta_{i}\mid\mathcal{F}_{N}\right\}$$ $$V_{1}+V_{2}.$$



= E

= E
:= V1 +V2.
The first term V1 **represents the sampling variance of the linearized two-phase** regression estimator, treating the δi **indicators as fixed. The second term** V2 reflects the variance due to the randomness in the δi **indicators in the influence** function ηi.

Observe that if the influence functions ηi were observed, the first component V1 of the total variance could be easily estimated using the standard Regression estimator for two-phase sampling 141 variance estimation formula. Therefore, a linearization-based variance estimator for two-phase sampling can be developed as

$$\hat{V}=\sum_{i\in A_{1}}\sum_{j\in A_{1}}\frac{\pi_{1ij}-\pi_{1i}\pi_{1j}}{\pi_{1ij}}\frac{\hat{\eta}_{i}}{\pi_{1i}}\frac{\hat{\eta}_{j}}{\pi_{1j}}\tag{11.25}$$

where the estimated influence function ˆηi **is given by**

$${\hat{\eta}}_{i}=\mathbf{x}_{i}^{\prime}{\hat{\boldsymbol{\beta}}}+{\frac{\delta_{i}}{\pi_{2i|1}}}\left(y_{i}-\mathbf{x}_{i}^{\prime}{\hat{\boldsymbol{\beta}}}\right).$$

This linearization variance estimator Vˆ **approximates the first component**
V1 **of the total variance, which can be expressed as**

$$E\left({\hat{V}}\mid{\mathcal{R}}_{N},{\mathcal{F}}_{N}\right)\cong V\left(\sum_{i\in A_{1}}w_{1i}\eta_{i}\mid{\mathcal{R}}_{N},{\mathcal{F}}_{N}\right).$$

And taking the expectation with respect to the first-phase sampling design, we have

$$E\left({\hat{V}}\mid{\mathcal{F}}_{N}\right)\cong E\left\{V\left(\sum_{i\in A_{1}}w_{1i}\eta_{i}\mid{\mathcal{R}}_{N},{\mathcal{F}}_{N}\right)\right\}=V_{1}.$$

This implies that the bias of the linearization variance estimator Vˆ **in (11.25)**
is given by

$$\begin{array}{r c l}{{\mathrm{Bias}\left(\hat{V}\right)}}&{{=}}&{{-V\left\{\sum_{i=1}^{N}\eta_{i}\mid\mathcal{F}_{N}\right\}}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{=}}&{{-\sum_{i=1}^{N}\sum_{j=1}^{N}C o v(\delta_{i},\delta_{j})\pi_{2i}^{-1}\pi_{2j}^{-1}e_{i}e_{j}.}}\end{array}$$

This bias term is of order O(N**), which is smaller than the leading order of**
V1 = O(n
−1N2) when the first-phase sampling rate is negligible (i.e., n/N .**= 0).**
Under Poisson sampling in the second phase, we can estimate the bias by

$$\widehat{\mathrm{Bias}}\left(\hat{V}\right)=-\sum_{i\in A_{1}}w_{1i}\frac{\delta_{i}}{\pi_{2i}}\left(\frac{1}{\pi_{2i}}-1\right)\left(y_{i}-{\bf x}_{i}^{\prime}\hat{\beta}\right)^{2}.$$

Replication variance estimator can be easily applied in this case. To do this, we use (11.19) to get

$${\hat{Y}}_{\mathrm{reg,tp}}=\sum_{i\in A_{1}}w_{i}\mathbf{x}_{i}^{\prime}{\hat{\beta}}_{2}={\hat{\mathbf{X}}}_{1}^{\prime}{\hat{\beta}}_{2}$$

142 *Two-phase sampling*

which is a product of two random variables. We can easily construct the
replicates of Yˆreg,tp by replacing the original weight wi **by its replication weight**
w
(k)
i**to get**
$$\hat{Y}_{\mathrm{reg,tp}}^{(k)}=\hat{\mathbf{X}}_{1}^{(k)^{\prime}}\hat{\beta}_{2}^{(k)}\,,$$  $$\hat{\mathbf{X}}^{(k)}=\sum_{i\in A_{1}}w_{i}^{(k)}\mathbf{x}_{i}$$
where

$$\operatorname{and}$$
$$\hat{\beta}_{2}^{(k)}=\left(\sum_{i\in A_{2}}w_{i}^{(k)}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\sum_{i\in A_{2}}w_{i}^{(k)}\mathbf{x}_{i}y_{i}.$$

$\text{(11,16),Using(11,19)}$. 

Note that we did not construct the replicate of π2i|1 **in (11.16). Using (11.19),**
the sampling variability of π2i|1 is safely transferred to βˆ2**. Once the replicates**
are calculated, we can use the replication variance formula **to estimate the** variance. See Park and Kim (2019) for more details of replication variance estimation under two-phase sampling.

The two-phase regression estimator can be implemented using a calibration weighting approach. Specifically, we can obtain the second-phase weights ω2i by minimizing the following quadratic objective function

$$Q(\omega_{2})=\sum_{i\in A_{2}}\left\{w_{1i}\omega_{2i}-w_{1i}\pi_{2i|1}^{-1}\right\}^{2}$$

o2**(11.26)**
subject to the calibration constraint

$$\sum_{i\in A_{2}}w_{1i}\omega_{2i}\mathbf{x}_{i}=\sum_{i\in A_{1}}w_{1i}\mathbf{x}_{i}.$$

w1ixi. **(11.27)**
The solution to the optimization problem is

$${\hat{\omega}}_{2i}=\pi_{2i|1}^{-1}+\left(\sum_{i\in A_{1}}w_{1i}\mathbf{x}_{i}-\sum_{i\in A_{2}}w_{1i}\pi_{2i|1}^{-1}\mathbf{x}_{i}\right)^{\prime}\left(\sum_{i\in A_{2}}w_{1i}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\mathbf{x}_{i}.$$
$$(11.26)$$
$$(11.27)$$

Importantly, the weighted sum Pi∈A2 w1iωˆ2iyi **is algebraically equivalent**
to the two-phase regression estimator in equation (11.16), **where the regression**
coefficient βˆ2**is obtained using the expression in (11.18). This calibration**
weighting approach provides an alternative implementation of the two-phase regression estimator, which can be useful as the regression **coefficients are** estimated indirectly from the data. The calibration constraint (11.27) ensures that the weighted sum of the first-phase covariates in the second-phase sample matches the total from the first-phase sample, thereby achieving the desired calibration.

When the auxiliary variables xi exhibit a monotone missing pattern, the calibration weighting approach can be implemented sequentially. Suppose the vector of auxiliary variables xi can be partitioned as xi = (x
(1)
i,x
(2)
i**), and the**
population total of x
(1)
i**is known. In this case, we can apply the following**
two-step calibration method:
[Step 1] Obtain w1i **by solving the calibration problem by minimizing**

$$Q_{1}(\omega_{1})=\sum_{i\in A_{1}}\left(\omega_{1i}-\pi_{1i}^{-1}\right)^{2}$$  subject to  $$\sum_{i\in A_{1}}\omega_{1i}\mathbf{x}_{i}^{(1)}=\sum_{i=1}^{N}\mathbf{x}_{i}^{(1)}.$$

[Step 2] Once the first-phase weights w1i = ˆω1i **are obtained from [Step 1],**
obtain ω2i by minimizing Q(ω2**) in (11.26), subject to the calibration constraint (11.27).**
This two-step calibration approach leverages the known population total of the first-part of the auxiliary variables x
(1)
i**to first determine the appropriate**
first-phase weights w1i**. Then, in the second step, the second-phase weights**
ω2i **are obtained by calibrating to the full set of auxiliary variables** xi.

This sequential calibration procedure is particularly useful when the auxiliary information exhibits a monotone missing pattern, allowing for efficient utilization of the available data at each phase of the sampling design.

## 11.4 Non-Nested Two-Phase Sampling

In contrast to the classical two-phase sampling framework, non-nested twophase sampling involves two independent surveys conducted on the same target population. The key distinction is that the two samples, **denoted as** A1 and A2**, are drawn independently rather than sequentially. Table 11.1 presents**
the data structure for non-nested two-phase sampling.

In the non-nested two-phase sampling, a large probability sample A1 is drawn from a finite population, collecting only the x **variable, and a smaller**
sample A2 is drawn from the same population, providing information on **both**
the y and x variables. It is assumed that the observed variable x **is comparable in the two surveys. Renssen and Nieuwenbroek (1997) formally addressed**
this non-nested two-phase sampling problem and Merkouris (2004) extended the idea further to develop regression estimation combining information from multiple surveys. Kim and Rao (2012) considered the non-nested two-phase sampling in the context of mass imputation combining two independent surveys at the population and domain levels.

TABLE 11.1 Data Structure for non-nested two-phase sampling



To illustrate the non-nested two-phase sampling approach, **let's consider**
the data structure shown in Table 11.1. This setup involves two independent samples, A1 and A2**, drawn from the same target population.**
From these two samples, we can compute two unbiased estimators of the population total X =PN
i=1 xi **for the auxiliary variable x:** Xˆ1 =Pi∈A1 π
−1 1i xi and Xˆ2 =Pi∈A2 π
−1 2i xi. Here, π1i and π2i **represent the inclusion probabilities**
for samples A1 and A2**, respectively.**
Both Xˆ1 and Xˆ2 are unbiased estimators of the population total X **under the respective sampling designs. The availability of these two unbiased**
estimators is a key feature of the non-nested two-phase sampling design, as it provides opportunities for developing enhanced estimation procedures combining information from different sources.

We can construct a combined estimator of X, denoted as Xb c**, as follows:**

$\left(11.28\right)^{2}$
$${\hat{\mathbf{X}}}_{c}=W{\hat{\mathbf{X}}}_{1}+(I-W){\hat{\mathbf{X}}}_{2},$$
Xb c = WXˆ1 + (I −W)Xˆ2, **(11.28)**
where W is a p × p symmetric matrix of constants, and p = dim(x**) is the**
dimension of the auxiliary variable x. The optimal choice of **the matrix W can** be determined using the Generalized Least Squares (GLS) method. However, other choices of W can also be used. The key idea is to leverage **the information** from these two independent surveys to obtain a more accurate **and efficient**
estimator of the population total X for the auxiliary variable x, compared to using only one of the surveys alone.

Using the combined estimator Xb c **in (11.28), we can construct the following**
projection estimator:
Ybp = Xb ′c ˆβq**(11.29)**
where the regression coefficient estimator ˆβq is defined as

$\left(11\right)$. 
$\mathrm{d}_{\mathrm{m}}x_{\mathrm{m}}$
$${\hat{\boldsymbol{\beta}}}_{q}=\left(\sum_{i\in A_{2}}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}/q_{i}\right)^{-1}\sum_{i\in A_{2}}\mathbf{x}_{i}y_{i}/q_{i}.$$

The choice of qi **in the regression coefficient estimator is somewhat arbitrary.**
Two possible choices are:
1. Using the model variance under a regression superpopulation model.

2. Using qi = π
−2 2i −π
−1 2ito compute the design-optimal regression estimator under Poisson sampling.

The key idea is that by using the combined estimator Xb c in the projection estimator Ybp**, we can leverage the information from both the A1 and A2 samples**
to obtain a more accurate prediction of the variable of interest Y. The choice
of qi **allows for some flexibility in how the regression coefficient is estimated.**
To ensure the design-consistency of the projection estimator in (11.29),
we can use the following regression estimator under non-nested two-phase sampling:
$${\hat{Y}}_{\mathrm{tp,reg}}={\hat{Y}}_{2}+\left({\hat{\mathbf{X}}}_{\mathrm{c}}-{\hat{\mathbf{X}}}_{2}\right)^{\prime}{\hat{\boldsymbol{\beta}}}_{q}$$
′ˆβq**(11.30)**
By the definition of $\widehat{\mathbf{X}}_{\mathrm{c}}$, we can also express this as: . 
By the definition of Xb c**, we can also express this as:**
$$(11.30)$$

$$\hat{Y}_{\mathrm{tp,reg}}=\hat{Y}_{2}+\left(\hat{\mathbf{X}}_{1}-\hat{\mathbf{X}}_{2}\right)^{\prime}\hat{\boldsymbol{\alpha}}_{q},$$
$$(11.31)$$
′αˆq, **(11.31)**
where $\hat{\mathbf{a}}_{q}=W\hat{\mathbf{\beta}}_{q}$. The key points are:
1. The design-consistent regression estimator Ybtp,reg **is constructed by**
adding a correction term to the projection estimator Ybp **from the**
second sample.

2. The regression estimator improves the efficiency of the design unbiased estimator Yˆ2 by substracting the projection of Yˆ2 **onto the**
augmentation space (Tsiatis, 2006), the linear space generated by the difference between the combined estimator Xb c and the estimator Xb 2 **from the second sample.**
3. Alternatively, the augmentation space can be expressed using the difference between the estimators Xb 1 and Xb 2**, weighted by** αˆ q.

The goal is to leverage the information from both samples to obtain a designconsistent regression estimator for the variable of interest Y.

Using the standard argument, we can obtain

$$\begin{array}{r c l}{{\widehat{Y}_{\mathrm{tp,reg}}}}&{{=}}&{{\widehat{Y}_{2}+\left(\widehat{\mathbf{X}}_{1}-\widehat{\mathbf{X}}_{2}\right)^{\prime}\boldsymbol{\alpha}_{q}^{*}+O_{p}(n^{-1}N)}}\end{array}$$
−1N**) (11.32)**
where α
∗
q is the probability limit of αˆq = W ˆβq
. By (11.32), we can obtain

$$(11.32)$$
of $\hat{\pmb{a}}_q=W\hat{\pmb{\beta}}_q.$ By (11.32), w. 
$$V\left(\widehat{Y}_{\mathrm{tp,reg}}\right)=(\mathbf{a}_{q}^{*})^{\prime}V\left(\widehat{\mathbf{X}}_{1}\right)\mathbf{a}_{q}^{*}+V\left(\hat{u}_{2}\right)$$
q +V (ˆu2**) (11.33)**
where ˆu2 =Pi∈A2 π
−1 2i yi −x
′
iα
∗
q
**. From the formula in (11.33), we can construct a linearized variance estimator.**
Now, we can use the calibration weighting to construct the regression estimator under non-nested two-phase sampling. For given the **design weights**
d2i = π
−1 2i
, we find the minimizer of

$$(11.33)$$
 - $\frac{1}{2}$ - (11 - 22) = ? 
$$Q\left(\boldsymbol{\omega}\right)=\sum_{i\in A_{2}}\left(\omega_{i}-d_{2i}\right)^{2}q_{i}$$

146 *Two-phase sampling*

subject to
$$\sum_{i\in A_{2}}\omega_{i}\mathbf{x}_{i}={\hat{\mathbf{X}}}_{\mathrm{c}}.$$



The solution is

$${\hat{\omega}}_{i}=d_{2i}+\left({\widehat{\mathbf{X}}}_{\mathrm{c}}-{\widehat{\mathbf{X}}}_{2}\right)^{-1}\left(\sum_{i\in A_{2}}q_{i}^{-1}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\mathbf{x}_{i}q_{i}^{-1}.$$
$${\dot{\mathrm{i}}}_{S}$$

Note that $\theta$
Note thatX
$$\sum_{i\in A_2}\hat{\omega}_i y_i=\hat{Y}_{\text{tp,reg}},$$ ... 

where Ybtp,reg **is defined in (11.31). Thus, the algebraic equivalence between**
the regression estimator and the calibration weighting estimator is established under non-nested two-phase sampling.

We now consider an extension combining information from three independent samples. Suppose that we have three independent samples, denoted by A,B, and C**, and the observed data structure is summarized in Table 11.2.**

Data Structure for three independent samples



We first consider the data structure in Case 1. In this case, we **can use**
two-step estimation procedure for combining all available **information. In the** first step, we use the generalized least squares (GLS) method **to combine** information and obtain the best linear unbiased estimator of the population total of x
′ = (x
′1
,x
′2
). Let Xˆ GLS **be the GLS estimator of** X =PN
i=1 xi.

In the second step, we construct the calibration weights in sample A**. Given**
the design weight d
(A)
i**for sample A, we find the minimizer of**

$$Q_{A}\left(\mathbf{\omega}\right)=\sum_{i\in A}\left(\omega_{i}-d_{i}^{\left(A\right)}\right)^{2}q_{i}$$
subject to $\theta$
$$\sum_{i\in A}\omega_{i}\mathbf{x}_{i}={\hat{\mathbf{X}}}_{\mathrm{GLS}}.$$

Non-nested two-phase sampling 147 The solution is

$$\hat{\omega}_{i}=d_{i}^{(A)}+\left(\hat{\mathbf{X}}_{\mathrm{GLS}}-\hat{\mathbf{X}}_{A}\right)^{\prime}\left(\sum_{i\in A}q_{i}^{-1}\mathbf{x}_{i}\mathbf{x}_{i}^{\prime}\right)^{-1}\mathbf{x}_{i}q_{i}^{-1}.$$
Note that $$\sum_{i\in A}\hat{\omega}_i y_i=\hat{Y}_{\text{reg}}$$ where $$\hat{Y}_{\text{reg}}=\hat{Y}_A+\left(\hat{\mathbf{X}}_{\text{GLS}}-\hat{\mathbf{X}}_A\right)'\hat{\boldsymbol{\beta}}_q$$ and $$\hat{\boldsymbol{\beta}}_q=\left(\sum_{i\in A}q_i^{-1}\mathbf{x}_i\mathbf{x}_i'\right)^{-1}\sum_{i\in A}q_i^{-1}\mathbf{x}_i y_i.$$ Thus, the above calibration estimator is algebraically equivalent to the bias-
Thus, the above calibration estimator is algebraically equivalent to the biascorrected regression estimator using Xb GLS **as the estimated control for** X.

Now, in Case 2, we wish to develop calibration weights for sample B**. The**
GLS step is the same as Case 1. Now, to construct the calibration weights for sample B, given the design weight d
(B)
i**for sample B, we find the minimizer**
of

$$Q_{B}\left(\mathbf{\omega}^{(B)}\right)=\sum_{i\in B}\left(\omega_{i}^{(B)}-d_{i}^{(B)}\right)^{2}q_{i}$$
subject to
$$\sum_{i\in B}\omega_i^{(B)}\mathbf{x}_{1i}=\hat{\mathbf{X}}_{1,\mathrm{GLS}}.$$

The solution is

The solution is $$\hat{\omega}_i^{(B)}=d_i^{(B)}+\left(\hat{\mathbf{X}}_{1,\mathrm{GLS}}-\hat{\mathbf{X}}_{1B}\right)'\left(\sum_{i\in B}q_i^{-1}\mathbf{x}_{1i}\mathbf{x}_{1i}^\prime\right)^{-1}\mathbf{x}_{1i}q_i^{-1}.$$  Note that $\hat{\omega}_i^{(B)}$ is a $\hat{\omega}_i^{(B)}$-independent. 
Note that  $$\sum_{i\in B}\hat{\omega}_{i}^{(B)}y_{i}=\hat{Y}_{B}+\left(\hat{\mathbf{X}}_{1,\mathrm{GLS}}-\hat{\mathbf{X}}_{1,B}\right)^{\prime}\hat{\boldsymbol{\beta}}_{1q}$$  where $\hat{Y}_{B}=\sum_{i\in B}d_{i}^{(B)}y_{i}$, $\hat{\mathbf{X}}_{1,B}=\sum_{i\in B}d_{i}^{(B)}\mathbf{x}_{1i}$, and  $$\hat{\boldsymbol{\beta}}_{1q}=\left(\sum_{i\in B}q_{i}^{-1}\mathbf{x}_{1i}\mathbf{x}_{1i}^{\prime}\right)^{-1}\sum_{i\in B}q_{i}^{-1}\mathbf{x}_{1i}y_{i}.$$  The first three different results are the above and two models.  
Therefore, the calibration weighting method can be used to combine the information in the multiple surveys effectively.

## 11.5 Repeated Surveys

Repeated surveys means that the survey measurement is taken **for the**
same population at different times. For example, in the US Current Population Survey, the employment rates are announced monthly. In **this case, the**
sample selection can be repeated at different times. In the repeated surveys, suppose that there are two different years, there are three different parameters of interest.

1. Y¯1 − Y¯2**: the difference of the population mean over two different**
years.

2. (Y¯1 +Y¯2)/**2: overall mean over the two different years.** 3. Y¯2**: the population mean at the most recent year.**
The optimal sampling design for θ1 = Y¯1 −Y¯2 **can be quite different from the**
optimal sampling design for Y¯ = (Y¯1 + Y¯2)/2. Let ¯y1 and ¯y2 **be an unbiased**
estimator of Y¯1 and Y¯2, respectively. If we use ˆθ = ¯y1 −y¯2 **to estimate** Y¯1 −Y¯2, the variance of ˆθ is minimized when *Corr*(¯y1,y¯2**) = 1. The correlation increases**
when the sample for t = 1 is the same as the sample for t **= 2. That is, it**
is the case where the same sample is used to obtain the measurement for t = 1 and for t **= 2. Such a sample is often called a panel sample. On the**
other hand, if the parameter of interest is Y¯ = (Y¯1 +Y¯2)/**2, the design of the**
panel sample increases the variance. Independent sample selection, leading to Corr(¯y1,y¯2**) = 0, is more efficient than panel sample design if we are interested**
in estimating Y¯ = (Y¯1 +Y¯2)/2.

Now, if we are interested in estimating Y¯2**, the following partial overlap**
sampling design is more efficient than the previous two sampling designs.

1. At t = 1, using an SRS of size n **to obtain** A1.

2. At t **= 2, first stratify the finite population into two strata. One**
is A1 and the other is U − A1. From the first stratum A1**, select** an SRS of size nm to obtain A2m**. From the second stratum** U − A1, select an SRS of size nu = n − nm**, independently of the first** stratum, to obtain A2u. The final sample is A2 = A2m ∪ A2u**. The**
first stratum is called "matched" stratum and the second stratum is called "unmatched" stratum.
In this case, the final sample in the matched stratum can be viewed as a two-phase sample where the first phase sample is A1 **and the second phase** sample is A2m**. Also, the final sample in the unmatched sample is also a**
two-phase stratified sample, where the first phase sample is U − A1 **and the**
second-phase sample is A2u**. The following table presents a summary of the**
two estimators in each two-phase sample. Repeated surveys 149

| Stratum   | Population Size   | Sample Size          | Estimator of Y¯   |
|-----------|-------------------|----------------------|-------------------|
| Matched   | n                 | nm                   | Y ˆ¯m ˆ¯ u        |
| Unmatched | N −n              | nu                   | Y                 |
| N         | n                 | αY ˆ¯ u + (1−α)Y ˆ¯m |                   |

Now, consider the following class of estimators indexed by a **constant** α:
Y
ˆ¯α = αY
ˆ¯u **+ (1**−α)Y
ˆ¯m. **(11.34)**
Such an estimator is a weighted average of two unbiased estimators, and is often called a composite estimator. The composite estimator is (approximately)
unbiased if the two components, Y
ˆ¯u and Y
ˆ¯m**, are (approximately) unbiased.**
The optimal value of α **that minimizes the variance of the composite estimator** is

is $$\alpha^*=\frac{V\left(\hat{\hat{Y}}_m\right)-Cov\left(\hat{\hat{Y}}_u,\hat{\hat{Y}}_m\right)}{V\left(\hat{\hat{Y}}_u\right)+V\left(\hat{\hat{Y}}_m\right)-2Cov\left(\hat{\hat{Y}}_u,\hat{\hat{Y}}_m\right)}.$$ In this case, the optimal composite estimator is 
. **(11.35)**
$$(11.35)$$
$$\hat{\bar{Y}}_{\alpha}^{*}=\alpha^{*}\hat{\bar{Y}}_{u}+(1-\alpha^{*})\,\hat{\bar{Y}}_{m}$$
and its variance is

lice is  $$V\left(\hat{\hat{Y}}_{\alpha}^{*}\right)=\frac{V\left(\hat{\hat{Y}}_{m}\right)V\left(\hat{\hat{Y}}_{u}\right)-\left\{Cov\left(\hat{\hat{Y}}_{u},\hat{\hat{Y}}_{m}\right)\right\}^{2}}{V\left(\hat{\hat{Y}}_{u}\right)+V\left(\hat{\hat{Y}}_{m}\right)-2Cov\left(\hat{\hat{Y}}_{u},\hat{\hat{Y}}_{m}\right)}.\tag{11.36}$$
To discuss the choice of unbiased estimators, we first note that the measurement at t = 1 can be treated as the auxiliary variable x **and the measurement**
at t = 2 can be treated as the study variable y**. In the unmatched stratum,** there is no auxiliary information, so we use

$${\hat{\bar{Y}}}_{u}={\frac{1}{n_{u}}}\sum_{i\in A_{2u}}y_{i}\equiv{\bar{y}}_{u}.$$

On the other hand, in the matched stratum, we can use auxiliary information to get

$${}^{I}m-y_{m}\top(x_{1}-x_{m})\,\upsilon$$  where  $$(\bar{x}_{m},\bar{y}_{m})=n_{m}^{-1}\sum_{i\in A_{2m}}\,(x_{i},y_{i})$$ $$b=\left\{\sum_{i\in A_{2m}}\,(x_{i}-\bar{x}_{m})^{2}\right\}^{-1}\sum_{i\in A_{2m}}\,(x_{i}-\bar{x}_{m})\,y_{i}.$$  Thus, the following summary can be made to the two estimators.  
$${\hat{\bar{Y}}}_{m}={\bar{y}}_{m}+({\bar{x}}_{1}-{\bar{x}}_{m})\,b$$

| Stratum                 | Estimator of Y¯   | Expectation   | Variance   |
|-------------------------|-------------------|---------------|------------|
| ˆ¯m = ¯ym + (¯x1 −x¯m)b | Y¯ +O  n −1                    | n −1  1−ρ 2  S 2 +n −1ρ 2S 2               |            |
| Matched                 | Y                 | m             |            |
| ˆ¯ u = ¯yu              | Y                 | n             |            |
| ¯                       | −1                | 2             |            |
| Unmatched               | Y                 | m S           |            |
| Also, we can show that  | Cov Y                   |  = 0.               | (11.37)    |
| ˆ¯m,Y ˆ¯ u              |                   |               |            |

Thus, the optimal solution (11.35) is

$$\alpha^{*}=\frac{n m_{u}-n_{u}^{2}\rho^{2}}{n^{2}-n_{u}^{2}\rho^{2}}$$

which is equal to α
∗ = nu/n for ρ **= 0 and equal to** α
∗ = nu/(n+nu) for ρ **= 1.**
The variance of the optimal composite estimator is then, by (11.36),

$$V\left(\hat{Y}^{*}_{\alpha}\right)=\frac{n-n_{u}\rho^{2}}{n^{2}-n_{u}^{2}\rho^{2}}S^{2}\geq\frac{1}{n}S^{2}\tag{11.38}$$

with the equality holds when nm = n or nm = 0 for ρ 6**= 0.**
The optimal allocation minimizing the variance (11.38) is

$${\frac{n_{u}}{n}}={\frac{1}{1+{\sqrt{1-\rho^{2}}}}},\ \ \ \ \ {\frac{n_{m}}{n}}={\frac{{\sqrt{1-\rho^{2}}}}{1+{\sqrt{1-\rho^{2}}}}}.$$

If ρ **is large then more sample is selected for the matched stratum. Under this** optimal allocation, the variance (11.38) reduces to

$$V\left({\hat{\hat{Y}}}_{\alpha}^{*}\right)={\frac{S^{2}}{2n}}\left(1+{\sqrt{1-\rho^{2}}}\right)$$
$$(11.39)$$
**(11.39)**
which takes the value between S
2/(2n**) and** S
2/n**. More discussion on this**
type of repeated surveys can be found in Fuller (1990).

12 Nonresponse

## 12.1 Introduction

Most surveys will have nonresponse. There are two types of nonresponse:
unit nonresponse, where the survey unit itself is nonresponsive, and item nonresponse, where only some items are nonresponsive. These nonresponses can be handled in two ways: in the case of unit nonresponse, a call-back or followup survey or nonresponse weighting adjustment can be used. For item nonresponse, imputation is commonly used.

To understand the effect of nonresponse, consider the data structure in Table 12.1.

Data structure with nonresponse

| Stratum         | Population Size   | Population Mean   | Sample Size   |
|-----------------|-------------------|-------------------|---------------|
| Respondents     | NR                | Y¯R               | nR            |
| Non-respondents | NM                | Y¯M               | nM            |
| Population      | N                 | Y                 | n             |
| ¯               |                   |                   |               |

In Table 12.1, the entire population consists of a population of respondents and a population of non-respondents. If we were to draw a sample from the entire population using simple random sampling from the entire population, we would only be able to observe the respondents in the sample. In this case, if the respondent mean ¯yR **is used to estimate the population mean,**

$$\begin{array}{r c l}{{B i a s\left(\bar{y}_{R}\right)}}&{{\doteq}}&{{\left(1-\frac{N_{R}}{N}\right)\left(\bar{Y}_{R}-\bar{Y}_{M}\right)}}\\ {{}}&{{}}&{{}}\\ {{V\left(\bar{y}_{R}\right)}}&{{\doteq}}&{{\frac{1}{n_{R}}S_{R}^{2}}}\end{array}$$

Here, two problems arise. One is that the estimate is biased. **The only way**
the bias becomes zero is if the mean of the respondents and the **mean of the** nonrespondents become equal. The other problem is that the efficiency of the estimation decreases as the sample size decreases (nR < n**). Compensating**
152 *Nonresponse* for this bias and trying to regain lost efficiency is the goal of **nonresponse** adjustment.

## 12.2 Call-Back

When an investigator calls or conducts an interview, there are several sources for nonresponse. One is refusal, which declines to participate the survey. Another one is not-at-home or non-available at the time **of survey. In**
these cases, one may need to resurvey a subset of the non-respondents reinterviewing a subset of non-respondents, which is often called follow-up survey or callback. The callback can be very effective in reducing non-response bias.

Suppose that we randomly select νnM **units from the nonrespondents of**
size nM, where 0 *< ν <* **1, to obtain the final sample, the final data set can be**
described as in Table 12.2.

| Stratum        | Population   | Original sample   | Final sample   | Final sample   |
|----------------|--------------|-------------------|----------------|----------------|
| size           | mean         | size              | mean           |                |
| Respondents    | NR           | nR                | r1 = nR        | y¯1            |
| Nonrespondents | NM           | nM                | r2 = νnM       | y¯2            |
| Population     | N            | n                 | r              |                |

If the original sample was selected by SRS, the final estimator of the final sample can be constructed as

$$\hat{\bar{Y}}_{\mathrm{cb}}=\frac{n_{R}}{n}\bar{y}_{1}+\frac{n_{M}}{n}\bar{y}_{2}.$$
$\left(12.1\right)^{2}$  . 

y¯2. **(12.1)**
Here, we also assume that r2 = νnM **units are selected by SRS for callbacks.**
In this case, we can apply the theory of two-phase sampling for stratification in Section 11.2 to show that Y
ˆ¯cb **in (12.1) is design unbiased. Also, by (11.5),**
we obtain

$$V a r\left(\hat{\bar{Y}}\right)=\frac{1}{n}\left(1-\frac{n}{N}\right)S^{2}+\frac{W_{2}S_{2}^{2}}{n}\left(\frac{1}{\nu}-1\right)$$

where W2 = N −1NM**. In many practical situations, the second phase sample**
(which is the callback sample) has a higher survey cost than the original sample. Thus, the total cost can be written as C = c0n+c1W1n+c2W2νn Nonresponse weighting adjustment 153 where c1 is the unit-level survey cost for the original sample and c2 **is the**
unit-level survey cost for the callback sample.

Using (11.8), the optimal sampling rate for the callback sample is calculated as

$$\nu^{*}=\sqrt{\frac{c_{0}+c_{1}W_{1}}{c_{2}}\times\frac{S_{2}^{2}}{S^{2}-W_{2}S_{2}^{2}}}.$$

The optimal sampling rate for the callback sample balances between the statistical efficiency and the cost efficiency.

## 12.3 Nonresponse Weighting Adjustment

We now consider the case of unit nonresponse in survey sampling. Assume that xi is observed throughout the sample, and yi is observed only if δi **= 1.**
We assume that the response mechanism does not depend on y**. Thus, we** assume that P(δ = 1 | x,y) = P(δ = 1 | x) = p(x;φ0**) (12.2)**
for some unknown vector φ0**. The first equality implies that the data are**
missing-at-random (MAR) in the sense of Rubin (1976) at the population level.

Given the response model (12.2), a consistent estimator of φ0 **can be obtained by maximizing the pseudo log-likelihood function**

$$\ell_{\mathrm{p}}\left(\phi\right)=\sum_{i\in A}\pi_{i}^{-1}\left[\delta_{i}\log\{p(\mathbf{x}_{i};\phi)\}+(1-\delta_{i})\log\{1-p(\mathbf{x}_{i};\phi)\}\right]$$

over the parameter space of φ. Note that φˆ **obtained from (12.3) can be expressed as the solution to the following pseudo-score equation**

$$(12.3)$$
$${\hat{S}}_{p}(\phi)\equiv\sum_{i\in A}{\frac{1}{\pi_{i}}}\left\{{\frac{\delta_{i}}{p(\mathbf{x}_{i};\phi)}}-1\right\}\mathbf{h}(\mathbf{x}_{i};\phi)=\mathbf{0}$$

where h(x;φ) = p(x;φ)· ∂logit{p(x;φ)}*/∂φ.*
Once φˆ is computed from (12.3) or (12.4), the propensity score (PS) **estimator of** Y =PN
i=1 yi **is given by**

$$(12.4)$$
$${\hat{Y}}_{\mathrm{PS}}=\sum_{i\in A_{R}}\pi_{i}^{-1}\{p(\mathbf{x}_{i};{\hat{\phi}})\}^{-1}y_{i},$$
$$(12.5)$$
−1yi, **(12.5)**
where AR = {i ∈ A : δi = 1} **is the set of respondents. The following theorem**
presents the asymptotic properties of the PS estimator in (12.5). 154 *Nonresponse* Theorem 12.1. *Assume that the response model (12.2) is correctly specified.*
Under some regularity conditions, the PS estimator in (12.5) satisfies YˆPS = YˆPS,ℓ +Op(n
−1N), **(12.6)**
where

_where_  $$\hat{Y}_{\rm PS,\ell}=\sum_{i\in A}\pi_{i}^{-1}{\bf h}_{i}^{\prime}B^{*}+\sum_{i\in A_{R}}\pi_{i}^{-1}p_{i}^{-1}\left(y_{i}-{\bf h}_{i}^{\prime}B^{*}\right),$$ $$B^{*}=\left\{\sum_{i=1}^{N}p_{i}^{-1}(1-p_{i}){\bf h}_{i}{\bf h}_{i}^{\prime}\right\}^{-1}\sum_{i=1}^{N}p_{i}^{-1}(1-p_{i}){\bf h}_{i}y_{i}\tag{12.7}$$  $p_{i}=p({\bf x}_{i};\phi_{0}),\mbox{and}{\bf h}_{i}={\bf h}({\bf x}_{i};\phi_{0}).$
Proof. Write YˆPS(φ) = Pi∈AR
π
−1 i{p(xi;φ)}
−1yi **and define**

$$\hat{Y}_{B}(\phi)=\hat{Y}_{\mathrm{PS}}(\phi)-\{\hat{S}_{p}(\phi)\}^{\prime}B$$

indexed by B. Note that YˆB(φˆ) = YˆPS regardless of the choice of B**. If we can**
find B∗**such that**
$$E\left\{\frac{\partial}{\partial\phi}\hat{Y}_{B}(\phi_{0})\right\}=\mathbf{0}$$
= 0 **(12.8)**
at B = B∗, then, according to Randles (1982), the effect of estimating φ can be safely ignored for the choice of B = B∗**. Now, note that**

$${\frac{\partial}{\partial\phi}}\left\{p(\mathbf{x};\phi_{0})\right\}^{-1}=-{\frac{(1-p_{i})}{p_{i}^{2}}}\mathbf{h}(\mathbf{x};\phi_{0}),$$

where pi = p(xi;φ0**). Thus, we have**

$$\begin{array}{r c l}{{E\left\{\frac{\partial}{\partial\phi}\hat{Y}_{B}(\phi_{0})\right\}}}&{{=}}&{{-\sum_{i=1}^{N}p_{i}^{-1}(1-p_{i}){\bf h}_{i}y_{i}+\sum_{i=1}^{N}p_{i}^{-1}(1-p_{i}){\bf h}_{i}{\bf h}_{i}^{\prime}B.}}\end{array}$$

Thus, Randles' condition in (12.8) is satisfied at B = B∗**in (12.7). Therefore,**
we have shown that YˆPS = YˆPS(φ0)− {Sˆp(φ0)}
′B
∗ +Op(n
−1N)
which proves (12.6).

Now, using the two-phase sampling theory, we can obtain that

$$E\left({\hat{Y}}_{\mathrm{PS},\ell}\right)=Y$$

and

$$\begin{array}{r c l}{{V\left(\hat{Y}_{\mathrm{PS},\ell}\right)}}&{{=}}&{{V\left(\hat{Y}_{\mathrm{HT}}\right)+E\left\{\sum_{i\in A}\pi_{i}^{-2}(p_{i}^{-1}-1)\left(y_{i}-\mathbf{h}_{i}^{\prime}B^{*}\right)^{2}\right\},}}\end{array}$$

Nonresponse weighting adjustment 155 where pi = p(xi;φ0).

We now discuss the estimation of the variance of the PS estimators of the form (12.5) where ˆpi = pi(φ**ˆ) is constructed to satisfy (12.4). By (12.6), we can**
write

$$\hat{Y}_{PS}=\sum_{i\in A}d_{i}\eta_{i}(\phi_{0})+O_{p}\left(n^{-1}N\right),\tag{12.9}$$  $$\eta_{i}(\phi)={\bf h}_{i}(\phi)^{\prime}B^{*}+\frac{\delta_{i}}{p_{i}(\phi)}\left\{y_{i}-{\bf h}_{i}(\phi)^{\prime}B^{*}\right\}.\tag{12.10}$$
where
To derive the variance estimator, we assume that the variance estimator P
Vˆ =
i∈A
Pj∈A Ωijqiqj satisfies *V /V* ˆ (ˆqHT |FN ) = 1 +op(1) for some Ωij **related**
to the joint inclusion probability, where ˆqHT =Pi∈A diqi for any q **with a**
finite fourth moment.

To obtain the total variance, the *reverse framework* **of Fay (1992), Shao**
and Steel (1999), and Kim et al. (2006) is considered. In this **framework,** the finite population is divided into two groups, a population of respondents and a population of nonrespondents, so the response indicator is extended to the entire population as RN = {δ1,δ2*,...,δ*N }**. Given the population, the**
sample A **is selected according to a probability sampling design. Then, we have** both respondents and nonrespondents in the sample A**. The total variance of**
ηˆHT =Pi∈A diηi **can be written as**
V (ˆηHT) = E{V (ˆηHT | RN )}+V {E(ˆηHT | RN )} := V1 +V2. **(12.11)**
The conditional variance term V (ˆηHT |RN **) in (12.11) can be estimated by**

$\hat{V}_{1}=\sum_{i\in A}\Omega_{ij}\hat{\eta}_{i}\hat{\eta}_{j}$, (12.12)
where ˆηi = ηi(φˆ) is defined in (12.10) with B∗**replaced by a consistent estimator such as**

$$\hat{B}^{*}=\left(\sum_{i\in A_{R}}d_{i}\hat{p}_{i}^{-2}(1-\hat{p}_{i})\hat{\mathbf{h}}_{i}\hat{\mathbf{h}}_{i}^{\prime}\right)^{-1}\sum_{i\in A_{R}}d_{i}\hat{p}_{i}^{-2}(1-\hat{p}_{i})\hat{\mathbf{h}}_{i}y_{i}$$
$$V_{2}.$$
$$(12.11)^{2}$$

and hˆi = h(xi;φˆ). The second term V2 **in (12.11) is**

$$\begin{array}{r c l}{{V\{E(\hat{\eta}_{\mathrm{HT}}\mid\mathcal{R}_{N})\}}}&{{=}}&{{V\left(\sum_{i=1}^{N}\eta_{i}\right)=\sum_{i=1}^{N}\frac{1-p_{i}}{p_{i}}\left(y_{i}-\mathbf{h}_{i}^{\prime}B_{z}\right)^{2}.}}\end{array}$$

A consistent estimator of V2 **can be derived as**

$$\hat{V}_{2}=\sum_{i\in A_{R}}d_{i}\frac{1-\hat{p}_{i}}{\hat{p}_{i}^{2}}\left(y_{i}-{\bf h}_{i}^{\prime}\hat{B}_{z}\right)^{2}.\tag{12.13}$$

156 *Nonresponse*

Therefore,
$\hat{V}\left(\hat{Y}_{\rm PS}\right)=\hat{V}_{1}+\hat{V}_{2}$ (12.14)
is consistent for the variance of the PS estimator defined in (12.5) with ˆpi =
pi(φˆ) satisfying (12.4), where Vˆ1 is in (12.12) and Vˆ2 **is in (12.13). When the**
sampling fraction nN −1is negligible, that is, nN −1 = o**(1), the second term** V2 can be ignored and Vˆ1 **is a consistent estimator of total variance. Otherwise,**
the second term V2 **should be taken into account so that a consistent variance**
estimator can be constructed as in (12.14).

## 12.4 Calibration Weighting For Nonresponse Adjustment

Let Yˆn =Pi∈A diyi be any design-consistent estimator of Y where di can be either design weight or the calibration weight. Unfortunately, we cannot compute Yˆn **due to nonresponse. Our goal is to construct the final weight** ωi in AR **so that**

$${\hat{Y}}_{\omega}=\sum_{i\in A_{R}}\omega_{i}y_{i}$$

can be used to estimate Y **. In addition to the response model in (12.2), we** also consider the "working" superpopulation model

$$y_{i}=\mathbf{x}_{i}^{\prime}{\boldsymbol{\beta}}+e_{i}$$
iβ +ei **(12.15)**
with E(ei | xi) = 0 and V (ei | xi) = ciσ 2**. By considering the two models, we**
can develop the final calibration weights that satisfy the double robustness property (Kim and Haziza, 2014). Note that, under (12.15), we can impose

$$\sum_{i\in A_{R}}\omega_{i}\mathbf{x}_{i}=\sum_{i\in A}d_{i}\mathbf{x}_{i}$$

as a calibration constraint incorporating the superpopulation model in (12.15). Note that

$${\hat{Y}}_{\omega}-{\hat{Y}}_{n}=\left(\sum_{i\in A_{R}}\omega_{i}\mathbf{x}_{i}-\sum_{i\in A}d_{i}\mathbf{x}_{i}\right)^{\prime}\beta+\left(\sum_{i\in A_{R}}\omega_{i}e_{i}-\sum_{i\in A}d_{i}e_{i}\right).$$
$\left(12.15\right)$ . 
$$(12.16)$$

The first term is zero when (12.16) is true. Also, the second term has zero expectation under the superpopulation model in (12.15). Therefore, as long as the superpopulation model (12.15) is correct and the MAR is maintained, then (12.16) is a sufficient condition for the unbiasedness of **the resulting** calibration estimator. Calibration weighting for nonresponse adjustment 157 In addition, we include

$$\sum_{i\in A_{R}}\omega_{i}{\hat{p}}_{i}^{-1}c_{i}=\sum_{i\in A}d_{i}{\hat{p}}_{i}^{-1}c_{i}$$
ici **(12.17)**
$$(12.17)$$

to obtain consistency under the response model in (12.2), where ˆpi = p(xi;φˆ).

To construct the objective function for optimization, we use

$$Q(\omega)=\sum_{i\in A_{R}}d_{i}\left({\frac{\omega_{i}}{d_{i}}}-1\right)^{2}c_{i}$$
2ci **(12.18)**
in the calibration problem. The final calibration weights can be obtained by minimizing (12.18) subject to (12.16) and (12.17). We also assume that λ
′xi =
ci for some λ **as in (9.8). Now, (9.8) and (12.16) imply that**

$$Q(\omega)=\sum_{i\in A_{R}}d_{i}^{-1}\omega_{i}^{2}c_{i}+\mathrm{constant}.$$

Using Lagrange multiplier method, the solution to the optimization problem can be written as

$$(12.18)$$
$${\hat{\omega}}_{i}=\left(\sum_{i\in A}d_{i}\mathbf{z}_{i}\right)^{\prime}\left(\sum_{i\in A_{R}}d_{i}\mathbf{z}_{i}\mathbf{z}_{i}^{\prime}/c_{i}\right)^{-1}\,d_{i}\mathbf{z}_{i}/c_{i},$$
$$(12.19)$$
$$(12.20)$$
dizi/ci, **(12.19)**
where ${\bf z}^{\prime}_{i}=({\bf x}^{\prime}_{i},\hat{p}^{-1}_{i}c_{i})$. Note that the final weight in (12.19 satisfies
$$\sum_{i\in A_{R}}\hat{\omega}_{i}y_{i}=\sum_{i\in A}d_{i}{\bf z}_{i}^{\prime}\hat{\gamma}_{R}:=\hat{Y}_{\mathrm{reg}},$$

where

$$\hat{\gamma}_{R}=\left(\sum_{i\in A_{R}}d_{i}\mathbf{z}_{i}\mathbf{z}_{i}^{\prime}/c_{i}\right)^{-1}\sum_{i\in A_{R}}d_{i}\mathbf{z}_{i}y_{i}/c_{i}.$$  ion of $\hat{\gamma}_{R}$,

i∈AR i∈AR By construction of ˆγR, X i∈AR dipˆ −1 iyi −z ′ iγˆR = 0 (12.21) which implies that
$$\sum_{i\in A_{R}}\hat{\omega}_{i}y_{i}\cong\sum_{i\in A}d_{i}{\bf z}_{i}^{\prime}\gamma^{*}+\sum_{i\in A_{R}}d_{i}\hat{p}_{i}^{-1}\left(y_{i}-{\bf z}_{i}^{\prime}\gamma^{*}\right):=\hat{Y}_{\mathrm{PS,reg}}$$

where γ
∗is the probability limit of ˆγR**. Using the argument in Theorem 12.1,**
we can show that YˆPS,reg **is asymptotically unbiased under the assumption**
that the response model (12.2) is specified correctly. Therefore, double robustness of the calibration estimator can be established. The regression estimator in (12.20) was first proposed by Fuller et al. (1994).

__
l_
l l

## Bibliography

Bankier, M. D. (1988). Power allocations: determining sample sizes for subnational areas. *The American Statistician***, 42:174–177.**
Basu, D. (1971). An essay on the logical foundations of survey sampling, part 1. In *Foundations of Statistical Inference, edited by V.P. Godambe and D.A.*
Sprott**, pages 203–242. Holt, Reinhart and Winston.**
Binder, D. A. (1983). On the variances of asymptotically normal estimators from complex surveys. *International Statistical Reviews***, 51:279–292.**
Breidt, F. J., Claeskens, G., and Opsomer, J. D. (2005). Model-assisted estimation for complex surveys using penalised splines. *Biometrika***, 92:831–846.**
Brewer, K. R. W. (1963). A method of systematic sampling with **unequal**
probabilities. *Australian journal of Statistics***, 5:93–105.**
Chao, M. T. (1982). A general purpose unequal probability sampling plan.

Biometrika**, 69:653–656.**
Chen, X.-H., Dempster, A. P., and Liu, J. S. (1994). Weighted **finite population**
sampling to maximize entropy. *Biometrika***, 81:457–469.**

Cochran, W. (1946). Relative accuracy of systematic and stratified random samples for a certain class of populations. *Annals of Mathematical Statistics*,
17:164–177.
Dalenius, T. and Hodges, J. L. J. (1959). Minimum variance stratification.

Journal of the American Statistical Association**, 54:88–101.**

Deming, W. E. and Stephan, F. F. (1940). On a least squares adjustment of a sampled frequency table when the expected marginal totals **are known.** Annals of Mathematical Statistics**, 11:427–444.**
Deville, J.-C. and Särndal, C.-E. (1992). Calibration estimators in survey sampling. *Journal of the American statistical Association***, 87(418):376–382.**
Deville, J. C. and Särndal, C. E. (1992). Calibration estimators in survey sampling. *Journal of the American Statistical Association***, 87:376–382.**
Deville, J. C., Särnndal, C. E., and Sautory, O. (1993). Generalized raking procedures in survey sampling. *Journal of the American Statistical Association***, 88:1013–1020.**
160 *Bibliography* Durbin, J. (1967). Design of multi-stage surveys for the estimation of sampling errors. *Applied Statistics***, 16:152–164.**

Fay, R. E. (1992). When are inferences from multiple imputation valid ? In Proceedings of the Survey Research Methods Section**, pages 227–232, Washington, DC. American Statistical Association.**
Firth, D. and Bennett, K. E. (1998). Robust models in probability sampling.

Journal of the Royal Statistical Society, Series B**, 60:3–21.**
Fuller, W. A. (1990). Analysis of repeated surveys. *Survey Methodology*,
16:167–180.

Fuller, W. A. (1998). Replication variance estimation for two-phase samples.

Statistica Sinica**, 8:1153–1164.**
Fuller, W. A. (2002). Regression estimation for sample surveys. **Survey**
Methodology**, 28:5–23.**
Fuller, W. A. (2009). *Sampling Statistic***. Wiley, Hoboken, NJ.**

Fuller, W. A., Loughin, M. M., and Baker, H. D. (1994). Regression weighting in the presence of nonresponse with application to the 1987-1988 nationwide food consumption survey. *Survey Methodology***, 20:75–85.**
Godambe, V. P. and Joshi, V. M. (1965). Admissibility and Bayes estimation in sampling finite populations, 1. *Annals of Mathematical Statistics*,
36:1707–1722.

Groves, R. M., Jr., F. J. F., Couper, M. P., Lepkowski, J. M., Singer, E., and Tourangeau, R. (2009). *Survey Methodology***. Wiley, 2nd edition.**
Hájek, J. (1981). *Sampling from a Finite Population***. Marcel Dekker.**
Hansen, M. H. and Hurwitz, W. N. (1943). On the theory of sampling from finite populations. *The Annals of Mathematical Statistics***, 14:333–362.**

Horvitz, D. G. and Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe. *Journal of the American Statistical Association***, 42:663–685.**
Kim, J. K. and Haziza, D. (2014). Doubly robust inference with missing data in survey sampling. *Statistica Sinica***, 24:375–394.**

Kim, J. K., Navarro, A., and Fuller, W. A. (2006). Replication variance estimation for two-phase stratified sampling. *Journal of the American Statistical* Association**, 101:312–320.**
Kim, J. K. and Rao, J. N. K. (2012). Combining data from two independent surveys: A model-assisted approach. *Biometrika*, 99:85–100.

Kish, L. (1965). *Survey Sampling***. John Wiley & Sons, Inc.** Krewski, D. and Rao, J. N. K. (1981). Inference from stratified samples:
properties of the linearization, jackknife and balanced repeated replication methods. *Annals of Statistics***, 9:1010–1019.**
Kruskal, W. and Mosteller, F. (1979). Representative sampling. I. nonscientific literature. *International Statistical Review***, 47:13–24.**

Kwon, Y., Kim, J. K., and Qiu, Y. (2024). Debiased calibration estimation using generalized entropy in survey sampling. available at http://arxiv.org/abs/2404.01076.

Lahiri, D. B. (1951). A method of sample selection providing **unbiased ratio**
estimates. *Bulletin of the International Statistical Institute***, 33:133–140.**
McLeod, A. I. and Bellhouse, D. R. (1983). A convenient algorithm for drawing a simple random sample. *Applied Statistics***, 32:182–184.**
Merkouris, T. (2004). Combining independent regression estimators from multiple surveys. *Journal of the American Statistical Association***, 99:1131–1139.**

Montanari, G. E. and Ranalli, M. G. (2005). Nonparametric model calibration estimation in survey sampling. *Journal of the American Statistical* Association**, 100(472):1429–1442.**
Narain, R. D. (1951). On sampling without replacement with varying probabilities. **Journal of the Indian Society of the Indian Society of Agricultural**
Statistics**, 3:169–174.**
Neyman, J. (1934). On the two different aspects of the representative method:
The method of stratified sampling and the method of purposive **selection.** Journal of the Royal Statistical Society**, 97:558–625.**
Park, S. and Kim, J. K. (2019). Mass imputation for two-phase **sampling.**
Journal of the Korean Statistical Society**, 48:578–592.**
Pea, J., Qualité, L., and Tillé, Y. (2007). Systematic sampling is a minimal support design. *Computational Statistics and Data Analysis***, 51:5591–5602.**
Quenouille, M. H. (1956). Notes on bias in estimation. *Biometrika***, 43:353–**
360.

Raj, D. (1966). Some remarks on a simple procedure of sampling without replacement. *Journal of the American Statistical Association***, 61:558–625.**
Randles, R. H. (1982). On the Asymptotic Normality of Statistics with Estimated Parameters. *The Annals of Statistics***, 10(2):462 - 474.**
Rao, J. N. K. (1973). On double sampling for stratification and analytic surveys. *Biometrika*, 60:125–133.

Renssen, R, H. and Nieuwenbroek, N. J. (1997). Aligning estimates for common variables in two or more sample surveys. *Journal of the American* Statistical Association**, 92:368–375.**
Royall, R. M. and Cumberland, W. G. (1981). The finite-population linear regression estimator and estimators of its variance—an empirical study. Journal of the American Statistical Association**, 76:924–930.**
Rubin, D. B. (1976). Inference and missing data. *Biometrika***, 63(3):581–592.**
Särndal, C., Swensson, B., and Wretman, J. (1992). **Model Assisted Survey**
Sampling**. Springer.**
Särndal, C. E., Swensson, B., and Wretman, J. H. (1989). The weighted residual technique for estimating the variance of the generalized regression estimator of the finite population total. *Biometrika***, 76:527–537.**
Sen, A. (1953). On the estimate of the variance in sampling with varying probabilities. *Journal of the Indian Society of Agricultural Statistics***, 5:119–** 127.

Shao, J. and Steel, P. (1999). Variance estimation for survey data with composite imputation and nonnegligible sampling fraction. *Journal of the American* Statistical Association**, 94:254–265.**
Shao, J. and Tu, D. (1995). *The Jackknife and Bootstrap***. Springer-Verlag,**
New York.

Sitter, R. R. (1997). Variance estimation for the regression estimator in twophase sampling. *Journal of the American Statistical Association***, 92:780–**
787.

Statistics Canada (2003). *Survey Methods and Practices***. Available at**
"http://www.statcan.gc.ca/pub/12-587-x/12-587-x2003001-eng.pdf".

Sunter, A. B. (1977). List sequential sampling with equal or unequal probabilities without replacement. *Applied Statistics***, 26:261–268.**
Tillé, Y. (2006). *Sampling Algorithms***. Springer-Verlag, New York.**
Tillé, Y. (2020). *Sampling and estimation from finite populations***. Wiley.** Tillé, Y. and Matei, A. (2016). *Sampling: Survey Sampling***. R package version**
2.8.

Tsiatis, A. A. (2006). *Semiparametric Theory and Missing Data***. Springer.** Tukey, J. W. (1958). Bias and confidence in not quite large samples. The Annals of Mathematical Statistics, 29:614–623.

Bibliography 163 Vitter, J. S. (1985). Random sampling with a reservoir. **ACM Transactions**
on Mathematical Software**, 11:37–57.**

Wolter, K. M. (1984). An investigation of some estimators of variance for systematic sampling. *Journal of the American Statistical Association***, 79:781–**
790.
Wolter, K. M. (2007). *Introduction to Variance Estimation***. Springer-Verlag,**
New York, 2 edition.

Wright, T. (2012). The equivalence of neyman optimum allocation for sampling and equal proportions for apportioning the u.s. house of representatives. *The American Statistician***, 66:217–224.**
Wu, C. and Sitter, R. R. (2001). A model-calibration approach to using complete auxiliary information from survey data. **Journal of the American**
Statistical Association**, 96(453):185–193.**
Yates, F. and Grundy, P. (1953). Selection without replacement from within strata with probabilities proportion to size. *Journal of the Royal Statistical* Society, Series B, 15:235–261.

This figure "F3.jpg" is available in "jpg"
 format from:
http://arxiv.org/ps/2401.07625v2