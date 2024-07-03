# Paper 

## Proposed modified computational model for the amoeba-inspired combinatorial optimization machine

Yusuke Miyajima (1) ${ }^{1}$ and Masahito Mochizuki (1) ${ }^{1}$<br>${ }^{1}$ Department of Applied Physics, Waseda University, Okubo, Shinjuku-ku,<br>Tokyo 169-8555

Received October 27, 20XX; Revised December 29, 20XX; Published July 1, 20XX


#### Abstract

A single-celled amoeba can solve the traveling salesman problem through its shapechanging dynamics. In this paper, we examine roles of several elements in a previously proposed computational model of the solution-search process of amoeba and three modifications towards enhancing the solution-search preformance. We find that appropriate modifications can indeed significantly improve the quality of solutions. It is also found that a condition associated with the volume conservation can also be modified in contrast to the naive belief that it is indispensable for the solution-search ability of amoeba. A proposed modified model shows much better performance.


Key Words: natural computing, amoeba-inspired machine, traveling salesman problem, combinatorial optimization

## 1. Introduction

In the modern information society, conventional Neumann-type computers face a serious problem of increased complexity and cost in computation. While the information processing capacity of computers is predicted to reach its limits because of the limit of Moore's law and the von Neumann bottleneck, the required computing power is increasing exponentially. Under these circumstances, new efficient domain-specific computational architectures beyond the von Neumann type are demanded [1]. The serious problem particularly appears in combinatorial optimization problems [2]. Recently, the Ising machine has been proposed as a solution and its practical applications are being investigated [3-7]. There, the combinatorial optimization problem is mapped onto the ground-state search of the Ising model, which is originally a mathematical model of magnetic materials $[8,9]$. On the other hand, research has been intensively conducted to construct combinatorial optimization machines that mimic the information processing of living organisms. This is because organisms often perform sophisticated information processing such as image recognitions, sound recognitions, and optimizations with low energy consumption.

One of the simplest and most useful machines of such kinds is a computing technology inspired by the information processing of the amoeboid organism [10, 11]. This technology exploits the dynamics
of unicellular slime mold, which transforms its body in response to the surroundings for survival. Specifically, it exploits the behaviors of the body to stretch for getting food and to shrink for avoiding light [12]. As demonstrated in the previous experimental study, unicellular slime molds are able to solve optimization problems such as mazes [13, 14], satisfiability problems [15], and traveling salesman problems (TSP) [16-18]. The superior solution-search capability derives from the shapechanging dynamics of amoeba, where the law of conservation of total volume is satisfied [18]. In other words, slime molds have high ability of the information processing despite being unicellular organisms and lacking a central information-processing mechanism. This situation has attracted attention as a model for an autonomous decentralized parallel computing architecture of high efficiency beyond the von Neumann architecture. However, motion of slime molds is as slow as $10^{-5} \mathrm{~m} / \mathrm{s}$, making it difficult to use them as practically usable machines. Therefore, research interest has focused on attempts to implement the information-processing processes of slime molds with physical devices as amoeba-inspired combinatorial optimization machines [19-24]. For simplicity, we will refer to slime mold as amoeba hereafter.

To realize the amoeba-inspired machines, a computational model (algorithm) for the solution-search process of amoeba should be constructed first [25-27]. An important model has been proposed by Aono and his coworkers, which is named Amoeba TSP algorithm [26]. Its physical implementation using analogue electronic circuits has been demonstrated by a subsequent experiment [24]. The model has turned out to describe well the amoeba dynamics and resulting solution-search ability. However, we do not have sufficient knowledge about roles of elements constituting the model on its solutionsearch ability. For example, the fluctuations expected to exist in the amoeba dynamics are taken into account using uniformly distributed random numbers within a certain range. However, the necessity of the fluctuations for the optimization ability is not trivial. Moreover, it has not been clarified how the optimization performance is affected if we change the distribution of random numbers. Insights into the role of each element in the model are expected to provide the guide for constructing the amoeba-inspired machines with higher solution-search ability.

In this paper, we study roles, effects, and (un)necessities of several elements of the Amoeba TSP algorithm by examining how modifications of the elements affect the optimization performance of the algorithm. It is found that appropriate modifications can significantly improve the optimization performance. On the basis of these examinations, we propose a modified model named Improved Amoeba TSP algorithm, which turns out to provide much better solutions in terms of the number of iterations and the route length. It has also turned out that even a condition originating from the volume conservation law assumed in the original model can be modified for the high solution-search ability in contrast to the naive belief, which may release us from the related constraints against the physical implementation.

This paper is structured as follows. In Section 2, a formalism of the TSP proposed by Hopfield and Tank is introduced [28]. Section 3 describes the concept of amoeba-inspired combinatorial optimization machine for solving the TSP. Specifically, an experiment with a biological slime mold and a computational model named Amoeba TSP algorithm are introduced. In Section 4, the parameters and conditions of the experiment and numerical simulations are described. In Section 5, we argue three elements of the model that characterize the Amoeba TSP algorithm and examine how modifications of these elements affect the optimization performance. In Section 6, a computational model named Improved Amoeba TSP algorithm is proposed. Section 7 is devoted to the summary.

## 2. Formalism of the traveling salesman problem

We first present a formalism of the TSP [29]. The TSP is a problem to find the shortest route for a given map which satisfies the condition that every city must be visited (only) once. When the number of cities is $n$, the number of candidate solutions is $(n-1) ! / 2$, which increases exponentially with increasing $n$. The TSP is known as one of the NP-hard problems, that is, no algorithm can solve this problem within polynomial computational time. Therefore, it is a popular approach in practical cases to search an approximate solution by heuristic algorithms. In our study, we attempt to obtain
an approximate solution using the amoeba-inspired combinatorial optimization algorithm.

We start with a brief introduction of the formalism proposed by Hopfield and Tank. For the $n$-city TSP, $n^{2}$ binary variables $x_{V k}(=0,1)$ are used to represent the routes, where the indices $V(=1,2, \cdots, n)$ and $k(=1,2, \cdots, n)$ represent a labeling number of the cities and a visiting order of the cities, respectively. Here, $x_{V k}=1(0)$ means that the city labeled as $V$ is (is not) visited at the $k$ th order. The cost function to be optimized in the searching procedure is defined as,

$$
E\left(\left\{x_{V k}\right\}\right)=-\frac{1}{2} \sum_{V=1}^{n} \sum_{U=1}^{n} \sum_{k=1}^{n} \sum_{l=1}^{n} W_{V k, U l} x_{V k} x_{U l}
$$

Two constraints of the TSP are given by the following equations,

$$
\sum_{k=1}^{n} x_{V k}=1, \quad \sum_{V=1}^{n} x_{V k}=1
$$

The former constraint prohibits revisiting once-visited cities, and the second constraint prohibits visiting more than one city simultaneously. The TSP is reduced to a problem to search a combination of $n^{2}$ binary variables $\left\{x_{V k}\right\}$ which minimizes the cost function in Eq. (1) with satisfying the constraints. Here, the cost $W_{V k, U l}$ is concerned with the distance between two cities and the penalty for violation of the constraints, which is defined by,

$$
W_{V k, U l}= \begin{cases}-\lambda & (V=U \wedge k \neq l) \\ -\mu & (V \neq U \wedge k=l) \\ -\nu \cdot d(V, U) & (V \neq U \wedge|k-l|=1) \\ -\nu \cdot d(V, U) & (V \neq U \wedge k=n \wedge l=1) \\ -\nu \cdot d(V, U) & (V \neq U \wedge k=1 \wedge l=n) \\ 0 & (\text { otherwise })\end{cases}
$$

Here $\lambda, \mu$ and $\nu$ are positive parameters, and $d(V, U)$ represents the distance between two cities $V$ and $U$. The parameters $\lambda$ and $\mu$, respectively, give costs for the penalty when the constraints in Eq. (2) are violated, while $\nu$ gives a cost proportional to the distance between two cities visited successively. The fourth and the fifth costs are concerned with the distance between the final and initial cities (The salesman must come back to the initial city finally). The value of the cost function is proportional to the route length when the constraints are satisfied. Note that the cost function in this formulation does not explicitly include the penalty terms for satisfying the constraints such as $\sum_{k=1}^{n} x_{V k}-1$ and $\sum_{V=1}^{n} x_{V k}-1$ in contrast to other optimization machines, e.g., Ising machines.

In this study, we evaluate the results obtained by the amoeba-based optimization machine and the computational models (algorithms) in terms of the following three criteria,

- Success rate for finding an approximate solution within the given time or number of iterations,
- Average of time or number of iterations required to find an approximate solution,
- Average of the normalized route length for the obtained solutions

The averages in the latter two are taken over all the successful trials of the solution search. The normalized route length of an obtained solution is defined as $R_{\text {calc }} / R_{\text {est }}$, where $R_{\text {calc }}$ and $R_{\text {est }}$ are the route length of the obtained solution and the estimated mean route length, respectively. A smaller average of $R_{\text {calc }} / R_{\text {est }}$ means that the amoeba-based optimization machine or the computational model is capable of finding a solution with a shorter route length.

## 3. Amoeba-inspired combinatorial optimization machine

### 3.1 Experiment

Aono and coworkers experimentally demonstrated that the shape-changing dynamics of amoeba induced by environmental stimuli, i.e., nutrient and light, can be used for efficient searches for approximate solutions of the TSP [16]. Figure 1(a) shows schematics of the amoeba-based device and the
optical feedback system used in the experiment, while Figs. 1(c) and 1(d) show initial and final states of the amoeba-based device. The device is set on an agarose plate with nutrient. The optical feedback system consists of a PC, a projector and a video camera. The device is composed of a central hub
![](https://cdn.mathpix.com/cropped/2024_04_26_3866e766709bfcc53f87g-04.jpg?height=518&width=1214&top_left_y=436&top_left_x=230)

(b)
![](https://cdn.mathpix.com/cropped/2024_04_26_3866e766709bfcc53f87g-04.jpg?height=502&width=1108&top_left_y=1007&top_left_x=336)

Fig. 1. (a) Experimental setup of the amoeba-based combinatorial optimization machine. (b) Example of a map of the 4-city TSP. In this experiment, the cities are labeled by alphabets, A, B, C and D. (c), (d) Initial and final states of the amoeba-based device in the experiment. The final state shown in (d) represents a solution corresponding to a traveling route in order of $\mathrm{B} \rightarrow \mathrm{C} \rightarrow \mathrm{D} \rightarrow \mathrm{A}$. The red lines and the red numbers in (b) represent the traveling route and the visiting order, respectively.

part and $n^{2}$ lanes to represent solutions of the TSP. Each lane corresponds to one continuous variable $X_{V k} \in[0,1]$ for $V=1,2, \cdots, n$ and $k=1,2, \cdots, n$ and thus is referred to as the lane $V k$. The body of amoeba in a lane is called branch. The variable $X_{V k}$ is defined as the ratio of area occupied by the amoeba to the total area in the lane $V k$, which is referred to as length of the branch in the lane $V k$. The cost function with binary variables $\left\{x_{V k}\right\}$ in Eq. (1) is adopted in the experiment. The continuous variables $X_{V k}$ are translated to the binary variable $x_{V k}$ where $x_{V k}$ equals to $1(0)$ when $X_{V k}$ equals to (is less than) unity. Namely, $x_{V k}$ takes 1 only when the lane is fully occupied by the branch. We read out a solution $\left\{x_{V k}\right\}$ of the TSP from a state of the branches of amoeba $\left\{X_{V k}\right\}$ in this manner in the experiment.

The optical feedback system illuminates the lanes and updates the state of the branches so as to minimize the cost function. The value of $X_{V k}$ is measured by the video camera, and $L_{V k}$ defined by Eq. (4) is calculated from all the values of $X_{V k}$ by the PC. Here $L_{V k}$ is a function of an integer variable $t$ representing the number of time step. A time step corresponds to six seconds.

$$
L_{V k}(t+1)=1-\sigma_{1000,-0.5}\left(\sum_{U=1}^{n} \sum_{l=1}^{n} W_{V k, U l} \sigma_{35,0.6}\left(X_{U l}(t)\right)\right)
$$

Here $\sigma_{\gamma, \theta}$ is a sigmoid function defined by,

$$
\sigma_{\gamma, \theta}(x)=\frac{1}{1+\exp (-\gamma(x-\theta))}
$$

The lane $V k$ will (will not) be illuminated by the projector when $L_{V k}$ is greater (less) than 0.5 . We call a combination of the step functions $\theta\left(L_{V k}-0.5\right)$ for all the lanes as the illumination pattern for each step. The amoeba basically elongates its branches in non-illuminated lanes to efficiently absorb the nutrient from the agarose plate. On the contrary, the amoeba basically contracts its branches in illuminated lanes to avoid the light stimuli. The illumination is a penalty to prevent amoeba from choosing solutions with significantly long route lengths or those violating the constraints in Eq. (2).

In the initial state, the amoeba occupies only the hub part of device and does not occupy any lanes at all, that is, $X_{V k}=0$ for all sets of $V k$ [Fig. 1(c)]. The operation for calculating the illumination pattern $\left\{\theta\left(L_{V k}-0.5\right)\right\}$ and updating a state of the branches $\left\{X_{V k}\right\}$ by illumination or non-illumination is iterated to minimize the cost function. Finally, only the $n$ lanes are fully occupied with amoeba's branches and the others are empty, that is, $X_{V k}$ equals to 1 for $n$ sets of indices $V k$ [Fig. 1(d)]. Eventually, an approximate solution is obtained [Fig. 1(b)].

According to the results of this experiment [26], the approximate solutions are obtained for almost all the trials and the average time required to obtain a solution increases linearly to the number of cities $n$. It has also turned out that the average of the normalized route lengths $R_{\text {calc }} / R_{\text {est }}$ takes 0.9 almost irrespective of $n$. Although the number of candidate solutions grows exponentially with increasing $n$, the amoeba is able to efficiently find an approximate solution with a reasonable route length. The detailed observation provides us an insight that this high solution-search ability of the amoeba originates from the fluctuating dynamics. The amoeba sometimes elongates (contracts) its branches even though the corresponding lane is (is not) illuminated. These slightly fluctuating responses enable to escape from local optimal solutions and to explore wider space of solutions in the searching process. However, it takes several ten minutes to find an approximate solution for real amoebas. This time scale is too long for practical use. Therefore, it is necessary to implement this high solution-searching capability of amoeba on a physical combinatorial optimization machine.

### 3.2 Computational model: Amoeba TSP algorithm

A computational model named Amoeba TSP algorithm has been proposed to reproduce the results of above experiment [26]. This model describes the time evolution of amoeba's branches in the lanes $X_{V k}(t)$ by the following equation,

$$
X_{V k}(t+1)= \begin{cases}X_{V k}(t)-O_{V k}(t+1)+\xi_{V k}(t+1) & \left(L_{V k}(t+1)>0.5\right) \\ X_{V k}(t)+I_{V k}(t+1)+\xi_{V k}(t+1) & \left(L_{V k}(t+1) \leq 0.5\right)\end{cases}
$$

In this mode, the value of $X_{V k}$ can take an arbitrary real number and is not restricted to $[0,1]$ unlike the experiment. The state of the branches $\left\{X_{V k}\right\}$ is updated according to this equation. Here the variables $O_{V k}\left(I_{V k}\right)$ are amounts of contraction (elongation) of a branch in the lane $V k$ when the lane is (is not) illuminated. The variables $\xi_{V k} \in[-\delta, \delta]$ are uniform random numbers describing intrinsic fluctuations in the dynamics of amoeba branches.

First, $L_{V k}(t+1)$ is calculated from $X_{V k}(t)$ using Eq. (4) with the costs $W_{V k, U l}$ in Eq. (3) for all the sets of $V k$. Next, the branch lengths $X_{V k}(t)$ are updated to $X_{V k}(t+1)$ using Eq. (6) based on the values of $L_{V k}$. Iterating the calculations of the illumination pattern $\left\{\theta\left(L_{V k}-0.5\right)\right\}$ and updating the state of the branches $\left\{X_{V k}\right\}$ alternately, we obtain an approximate solution of the TSP. We perform these two procedure based on Eq. (4) and Eq. (6) for all lanes as one iteration step. Here, the number of iterations is given by a integer $t$ and the variables updated in every iteration step are defined as functions of $t$.

The variables $O_{V k}(t)$ and $I_{V k}(t)$ are defined by,

$$
\begin{gathered}
O_{V k}(t+1)= \begin{cases}2 \Delta^{\mathrm{out}} \sigma_{20,0.6}\left(X_{V k}(t)\right) & \left(L_{V k}(t+1)>0.5\right) \\
0 & \left(L_{V k}(t+1) \leq 0.5\right)\end{cases} \\
I_{V k}(t+1)= \begin{cases}\left(\Delta^{\mathrm{in}}+\sum_{V=1}^{n} \sum_{k=1}^{n} O_{V k}(t+1)+S(t)\right) / L^{\mathrm{off}}(t+1) & \left(L^{\mathrm{off}}(t+1)>0\right) \\
0 & \left(L^{\mathrm{off}}(t+1)=0\right)\end{cases}
\end{gathered}
$$

with

$$
S(t+1)= \begin{cases}0 & \left(L^{\text {off }}(t+1)>0\right) \\ S(t)+\Delta^{\text {in }}+\sum_{V=1}^{n} \sum_{k=1}^{n} O_{V k}(t+1) & \left(L^{\text {off }}(t+1)=0\right)\end{cases}
$$

Here $\Delta^{\text {out }}$ and $\Delta^{\text {in }}$ are parameters representing the degree of the contraction and the elongation of branches. The variable $L^{\text {off }}(t)$ is the number of non-illuminated lanes.

Roughly speaking, Eq. (7) means that when $L_{V k}(t+1)>0.5$, the branch in the lane $V k$ should contract approximately by $2 \Delta^{\text {out }}$ if the original length $X_{V k}(t)$ is longer than a certain value of $\sim 0.6$. On the other hand, Eq. (8) means that there are three contributions to the elongation of branch in the lane $V k$ when $L_{V k}(t+1) \leq 0.5$. The first contribution associated with $\Delta^{\text {in }}$ assumes that a certain amount $\left(\Delta^{\mathrm{in}}\right)$ of amoeba's body consistently leaks out from the hub part towards the lane part, and it results in the elongation of each branch by $\Delta^{\text {in }} / L^{\text {off }}$ via equitable distribution when the number of non-illuminated lanes is $L^{\text {off }}$. The second term associated with $O_{V k}(t+1)$ means that a sum of the contracted portions of the illuminated branches are redistributed equally to the non-illuminated lanes.

The elongation of branch occurs mostly by equitable distribution of the sum of the contracted amounts of branches in illuminated lanes as well as the constant leak from the hub part to the $L^{\text {off }}$ non-illuminated lanes. However, there should be a case that all the lanes are illuminated, i.e., $L^{\text {off }}=0$. In such a case, these contributions are stocked at the moment, and will be leaked to non-illuminated lanes equally when $L^{\text {off }}$ becomes nonzero. The variable $S(t)$ defined in Eq. (9) describes this situation, and this is the third contribution to the elongation described in Eq. (8).

In addition, the following condition is imposed in the computational model to reproduce the experimental results,

$$
\sum_{V k \in \mathrm{off}}\left\{I_{V k}(t+1)+\xi_{V k}(t+1)\right\}-\sum_{V k \in \mathrm{on}}\left\{O_{V k}(t+1)-\xi_{V k}(t+1)\right\} \approx \Delta^{\mathrm{in}}
$$

Here $\sum_{V k \in \text { off }}\left(\sum_{V k \in \text { on }}\right)$ denotes the summation over the non-illuminated (illuminated) lanes. This condition represents a law of conservation where the sum of the elongated (positive) and contracted (negative) amounts of the branches equals to $\Delta^{\text {in }}$ constantly at every iteration step, which is the amount of leak from the hub part to the lanes. This condition is introduced by an idea that if the sum of $X_{V k}$ increases by a certain constant rate per unit time, the time required for the solution search is expected to be proportional to $n$, because the sum of $X_{V k}$ becomes $n$ in the end. The variable $S(t)$ is introduced to satisfy this condition at every iteration step as long as $L^{\text {off }} \neq 0$.

In the previous simulation in Ref. [26], they perform 1000 trials of a solution search for the TSP with 10 to 20 cities by using the original Amoeba TSP algorithm. The obtained results coincide well with those in the experiment. The approximate solutions are obtained for almost all the trials and the average number of iterations turns out to be proportional to $n$. Moreover, the average of the normalized route length $R_{\text {calc }} / R_{\text {est }}$ takes a constant value of 0.9 irrespective of the number of cities $n$.

It should be mentioned that although the number of iterations is proportional to $n$, the total CPU time for the calculation is, in fact, proportional to $n^{5}$. The serial process of CPU requires computational time proportional to $n^{4}$ for treating the $n^{4}$ components of the cost tensor $W_{V k, U l}$ to calculate the illumination pattern $L_{V k}(t)$. Therefore, only the computational model is not sufficient for the practical application. We need to physically implement the model as a combinatorial optimization machine where the serial calculation by CPU is substituted with parallel physical phenomena to realize the efficient solution search. However, the physical implementation of the Amoeba TSP algorithm is difficult, and only an attempt using analog electronic circuits has succeeded in this challenge so far [24]. The difficulty stems partly from the strict condition of Eq. (10). In this paper, we propose a modified computational model of the amoeba-inspired combinatorial optimization machine, which, we expect, is suitable for physical implementation.

## 4. Calculation conditions

We present the values of parameters in the numerical simulations and how to determine them before introducing the results.

### 4.1 Parameters

Table I shows the values of parameters used in our numerical simulations. The parameters $\lambda$ and $\mu$ give costs as penalties to the revisiting once-visited city and the simultaneous visits to multiple cities, respectively. Their values are fixed at $\lambda=0.5$ and $\mu=0.5$ throughout the numerical simulations. The parameter $\nu$ gives the cost proportional to the route length. Importantly, the costs for violating the constraints must be larger than those for increasing in the route length. On the other hand, the difference between route lengths should be evaluated as large as possible. On the basis of these two policies, the value of $\nu$ is determined by the following procedure. We consider combinations of three cities $\left(V_{1}, V_{2}, V_{3}\right)$ out of $n$ cities and the routes from $V_{1}$ to $V_{3}$ via $V_{2}$ where the route length is $d\left(V_{1}, V_{2}\right)+d\left(V_{2}, V_{3}\right)$. The value of $\nu$ is determined so as to satisfy the following inequality,

$$
\nu \cdot \max \left\{d\left(V_{1}, V_{2}\right)+d\left(V_{2}, V_{3}\right)\right\} \leq \min \{\lambda, \mu\}
$$

We also consider that the value of $\nu$ should be set as close as possible to $\nu^{*}$ where,

$$
\nu^{*} \equiv \frac{\min \{\lambda, \mu\}}{\max \left\{d\left(V_{1}, V_{2}\right)+d\left(V_{2}, V_{3}\right)\right\}}
$$

For example, we set $\nu=0.00176$ when $n=20$.

The parameter $\delta$ gives upper and lower bounds of the uniform random number $\xi_{V k}$ in the Amoeba TSP algorithm. The parameters $\Delta^{\text {out }}$ and $\Delta^{\text {in }}$ are fixed at $\Delta^{\text {out }}=0.001$ and $\Delta^{\text {in }}=0.001$ throughout the present work.

Table I. Parameter values used for the numerical simulations.

| $\lambda$ | $\mu$ | $\delta$ | $\Delta^{\text {out }}$ | $\Delta^{\text {in }}$ |
| :---: | :---: | :---: | :---: | :---: |
| 0.5 | 0.5 | 0.003 | 0.001 | 0.001 |

Maps of TSP are produced such that all the distances between two cities are given by a set of normal random numbers with a mean of 100 and a standard deviation of 17 , with which $R_{\text {est }}$ approximately equals to $100 n$ for the $n$-city TSP.

### 4.2 Conversion to the solution

In our numerical simulations, we abort the iteration to obtain an approximate solution $\left\{X_{V k}^{\mathrm{bin}}\right\}$ when the binary variables $X_{V k}^{\mathrm{bin}} \equiv \theta\left(X_{V k}-0.99\right)$ satisfy the following conditions,

$$
\sum_{V=1}^{n} X_{V k}^{\mathrm{bin}}=1, \quad \sum_{k=1}^{n} X_{V k}^{\mathrm{bin}}=1
$$

In the iteration process, we check whether the conditions are satisfied at every iteration step.

## 5. Modifications of the model

We focus on the following three elements A, B, and C, which characterize the Amoeba TSP algorithm, and examine how their modifications affect the optimization performance,

(Element A) The fluctuation $\xi_{V k}$ is given by a uniform random number,

(Element B) The sum of $X_{V k}$ increases by $\Delta^{\text {in }}$ at every iteration step as described in Eq. (10),

(Element C) Sigmoid functions are used in Eq. (4) for $L_{V k}(t+1)$ and in Eq. (7) for $O_{V k}$.

We perform 1000 solution-search trials for the 20-city TSP using a computational model with a modification in one of these three elements. We compare the obtained results with those obtained by the original algorithm to judge which elements are substantially important for the optimization performance.

### 5.1 Modifications of Element A

We first examine the following two types of modifications for Element A, that is,

(A-1) Removing the fluctuations by setting $\xi_{V k}=0$,

(A-2) Using normal random numbers for the fluctuations $\xi_{V k}$.

Table II shows the results obtained by the modified models together with those obtained by the original model using uniform random numbers ranging in $[-0.003,0.003]$ for the fluctuations. Noticeably, we cannot obtain an approximate solution in any of 1000 trials with the modification (A-1), which clearly indicates that the solution-search ability of amoeba indeed relies on the fluctuations in its dynamics. For the modification (A-2), we examine the normal random numbers with a mean of 0 and a standard deviation of 0.003 for $\xi_{V k}$ and find that the number of iterations is significantly suppressed by $29 \%$ as compared with the original algorithm, while the success rate does not change so much. Summarizing the results of these examinations, we conclude that the fluctuation $\xi_{V k}$ is indispensable for the solution-search procedure, and normal random numbers are more suitable for efficient searches, which can significantly reduce the required number of iterations as compared with uniform random numbers.

Table II. Optimization results obtained by the modifications of Element A. The results are evaluated by focusing on the three criteria, i.e., the rate of the trials in which the modified algorithm successfully finds an approximate solution within 3000 iterations (Success rate), the average number of iterations required to find an approximate solution (Average number of iterations), and the average of the normalized route lengths of obtained solutions (Average of $\left.R_{\text {calc }} / R_{\text {est }}\right)$. The results obtained by the original Amoeba TSP algorithm is presented for comparison.

| Modification | Success rate | Average number of iterations | Average of $R_{\text {calc }} / R_{\text {est }}$ |
| :--- | :---: | :---: | :---: |
| $(\mathrm{A}-1)$ | 0.000 | - | - |
| $(\mathrm{A}-2)$ | 0.986 | 1326.8 | 0.941 |
| Original | 0.992 | 1870.6 | 0.951 |

### 5.2 Modifications of Element B

We next examine the following four types of modifications for Element B, that is,

(B-1) Replacing $I_{V k}(t)$ with $0.9 I_{V k}(t)$ in Eq. (6),

(B-2) Replacing $I_{V k}(t)$ with $1.1 I_{V k}(t)$ in Eq. (6),

(B-3) Setting $\Delta^{\text {in }}$ at zero in Eqs. (8) and (9),

(B-4) Replacing $L^{\text {off }}$ with $n$ in Eq. (8).

Table III shows the results obtained by the modified models together with those obtained by the original model. Concerning the modifications (B-1) and (B-2), the increase rate $I_{V k}$ of $X_{V k}$ when $L_{V k} \leq 0.5$ is suppressed by $10 \%$ for the former, while it is enhanced by $10 \%$ for the latter. The conservation law in Eq. (10) is violated by these modifications. For the modification (B-3), the constant leak from the hub part to the lanes $\Delta^{\text {in }}$ is set to be zero. With this modification, a sum of the elongated and contracted amounts of the branches is always cancelled except for the contributions from the fluctuations. For the modification (B-4), $L^{\text {off }}$ in Eq. (8) is repalced with the number of cities $n$, which is based on an idea that $L^{\text {off }}$ finally becomes $n$ when a solution is obtained. This modification releases us from counting the number $L^{\text {off }}$ of non-illuminated lanes at every iteration step. Moreover, this modification is expected to boost the solution search by enhancing the increase rate $I_{V k}$ at each step because $n$ should be much smaller than $L^{\text {off }}$ particularly in the early stage of the iteration.

According to Table III, we find that a larger increase rate $I_{V k}$ of $X_{V k}$ at every step results in the better performance in terms of the number of iterations and the route length. In particular, the
modification (B-4) reduces the number of iterations by $44 \%$ as compared to the original Amoeba TSP algorithm. On the contrary, the success rate is not improved by any of these modifications.

So far, it has been naively believed that nonlocal correlations among branches manifested by the conservation law are indispensable to reproduce the solution-search ability of amoeba. Namely, we assume that a sum of the elongated (positive) and contracted (negative) amounts of branches should constantly equal to the amount of leak $\Delta^{\text {in }}$ from the amoeba body in the hub part. However, our study has demonstrated that the conservation rule is not required to solve TSP for the amoeba TSP algorithm. Moreover, it has turned out that much better solutions can be obtained if the conservation rule is removed. Surprisingly, the excellent solution-search ability of amoeba turns out to be attributable only to its fluctuating dynamics associated with its shape deformation.

Table III. Optimization results obtained by the modifications of Element B.

| Modification | Success rate | Average number of iterations | Average of $R_{\text {calc }} / R_{\text {est }}$ |
| :--- | :---: | :---: | :---: |
| (B-1) | 0.990 | 1937.4 | 0.957 |
| $(\mathrm{~B}-2)$ | 0.992 | 1817.4 | 0.949 |
| $(\mathrm{~B}-3)$ | 0.996 | 1989.7 | 0.958 |
| $(\mathrm{~B}-4)$ | 0.994 | 1049.3 | 0.912 |
| Original | 0.992 | 1870.6 | 0.951 |

### 5.3 Modifications of Element C

We finally examine the following three types of modifications for Element C, that is,

(C-1) Replacing the sigmoid function $\sigma_{20,0.6}(x)$ in Eq. (7) with 1,

(C-2) Replacing the sigmoid function $\sigma_{1000,-0.5}(x)$ in Eq. (4) with the step fumction $\theta(x+0.5)$,

(C-3) Replacing the sigmoid function $\sigma_{35,0.6}(x)$ in Eq. (4) with the step fumction $\theta(x-0.6)$.

Table IV shows the results obtained by the modified models together with those obtained by the original model. For the modification (C-1), the decrease rate $O_{V k}$ of $X_{V k}$ when $L_{V k}>0.5$ becomes independent of $X_{V k}$. We find that the number of iterations is reduced by $48 \%$ as compared with the original Amoeba TSP algorithm by this modification. For the modification (C-2), the sigmoid function $\sigma_{1000,-0.5}(x)$ in Eq. (4) is replaced with the step function $\theta(x+0.5)$. According to Table IV, we learn that the results are not affected so much by these modifications. For the modification (C-3), the sigmoid function $\sigma_{35,0.6}$ in Eq. (4) is replaced with the step function with $\theta(x-0.6)$. Table IV shows that the success rate becomes much worse with this modification, i.e., typically less than half of those obtained by the original algorithm. Moreover, the number of iterations becomes 1.4 times larger than those for the original algorithm.

These results offer several insights into the Amoeba TSP model to achieve a better optimization with less computational time. First, the decrease rate $O_{V k}$ of $X_{V k}$ in Eq. (7) should be given as a constant $2 \Delta^{\text {out }}$ without depending on the value of $X_{V k}$. Second, the sigmoid function $\sigma_{1000,-0.5}$ in Eq. (4) should be replaced with the step function. On the other hand, $\sigma_{35,0.6}$ is necessary to search approximate solutions of the TSP. Note that the argument of $\sigma_{1000,-0.5}, \sum_{U=1}^{n} \sum_{l=1}^{n} W_{V k, U l} \sigma_{35,0.6}\left(X_{U l}(t)\right)$, corresponds to the derivative of the cost function in Eq. (1) by $x_{V k}$ when $\sigma_{35,0.6}$ is replaced with the step function with a threshold 0.6 and $x_{V k}$ is defined as $\theta\left(X_{V k}-0.6\right)$. Owing to the finite slope of $\sigma_{35,0.6}$, the combination of $X_{V k}$ resulting in larger cost, $\sum_{U=1}^{n} \sum_{l=1}^{n} W_{V k, U l} \sigma_{35,0.6}\left(X_{U l}(t)\right)(\leq-0.5)$, is sometimes allowed in the solution-searching process and thus the computational model is able to search in wider solution space without trapped in certain local optimal solutions.

## 6. Improved Amoeba TSP model

According to the above examinations, we have found three modifications that can improve the optimization results significantly,

Table IV. Optimization results obtained by the modifications of Element C.

| Modification | Success rate | Average number of iterations | Average of $R_{\text {calc }} / R_{\text {est }}$ |
| :--- | :---: | :---: | :---: |
| $(\mathrm{C}-1)$ | 1.000 | 974.5 | 0.952 |
| $(\mathrm{C}-2)$ | 0.991 | 1874.8 | 0.953 |
| $(\mathrm{C}-3)$ | 0.460 | 2578.7 | 1.000 |
| Original | 0.992 | 1870.6 | 0.951 |

- Using normal random numbers for the fluctuations $\xi_{V k}(\mathrm{~A}-2)$,
- Replacing $L^{\text {off }}$ with the number of cities $n$ (B-4),
- Replacing the sigmoid function $\sigma_{20,0.6}(x)$ in Eq. (7) with unity (C-1).

In Table V, we also summarize items of the optimization improved by each modification. We construct a computational model named Improved Amoeba TSP algorithm by applying the three modifications to the Amoeba TSP algorithm. We perform 1000 solution-search trials for the $n$-city TSPs with $n=10-100$ by using the Improved Amoeba TSP algorithm.

Table V. Effects of each modification on the optimization. The symbols ++ , + and - denote excellent, good and bad effects for each criterion, respectively. The symbol 0 denotes a neutral effect.

| Modification | Success rate | Average number of iterations | Average of $R_{\text {calc }} / R_{\text {est }}$ |
| :--- | :---: | :---: | :---: |
| $(\mathrm{A}-2)$ | - | + | + |
| $(\mathrm{B}-4)$ | 0 | ++ | + |
| $(\mathrm{C}-1)$ | + | ++ | 0 |

The results are summarized in Table VI. We first learn that approximate solutions are obtained in all the 1000 trials for all the choices of $n$. When $n=20$ for example, the Improved Amoeba TSP algorithm requires reduced number of iterations to obtain an approximate solution as compared to the original Amoeba TSP algorithm. This high efficiency enables us to solve the TSP with $n$ greater than 20 within reasonable computational time. Figures 2(a) and 2(b) show the $n$ dependence of the average number of iterations and the average of $R_{\text {calc }} / R_{\text {est }}$, respectively. The number of iterations grows proportionally to $\sqrt{n}$. This scaling relation is nontrivial and surprising, and it holds irrespective of the distribution pattern of distances between cities. Moreover, the average of $R_{\text {calc }} / R_{\text {est }}$ decreases gradually but monotonically as $n$ increases, and is expected to be comparable to or even smaller than that for the original algorithm when $n$ is large enough. These results indicate that the Improved algorithm is superior to the original algorithm in terms of the efficiency and certainty of the solution search.

## 7. Conclusion

To conclude, we proposed an improved computational model of the amoeba-inspired combinatorial optimization machine, named Improved Amoeba TSP model, through examining the original model proposed by Aono et al. First, we focused on three elements in the original model and examined how each of these elements affects the optimization performance. Appropriate modifications of these elements were found to significantly improve the optimization results. Importantly, it turned out that the volume conservation law assumed in the original model is not necessarily required to realize the high solution-search ability in contrast to our naive belief. This justifies the modification, which might release us from possible related constraints and restrictions against the physical implementation. Next, we constructed the Improved Amoeba TSP model by applying these three modifications to the original model. The proposed model indeed provides noticeably improved results in terms of the number of iterations and the route length. In particular, we found that the number of iterations scales to order $\sqrt{n}$ for the number of cities $n$, which is significantly suppressed as compared to the scaling to order $n$ for the original model. Our study offers the guides to enhancing the solution-search

Table VI. Optimization results obtained by the Improved Amoeba TSP algorithm.

| Number of cities $n$ | Success rate | Average number of iterations | Average of $R_{\text {calc }} / R_{\text {est }}$ |
| :---: | :---: | :---: | :---: |
| 10 | 1.00 | 199.5 | 0.957 |
| 11 | 1.00 | 201.3 | 0.953 |
| 12 | 1.00 | 211.1 | 0.900 |
| 13 | 1.00 | 219.1 | 0.926 |
| 14 | 1.00 | 229.0 | 0.954 |
| 15 | 1.00 | 235.8 | 0.916 |
| 16 | 1.00 | 247.0 | 0.939 |
| 17 | 1.00 | 253.2 | 0.899 |
| 18 | 1.00 | 260.4 | 0.910 |
| 19 | 1.00 | 269.3 | 0.891 |
| 20 | 1.00 | 276.3 | 0.934 |
| 30 | 1.00 | 341.5 | 0.887 |
| 40 | 1.00 | 393.3 | 0.880 |
| 50 | 1.00 | 437.7 | 0.875 |
| 60 | 1.00 | 479.5 | 0.881 |
| 70 | 1.00 | 515.9 | 0.871 |
| 80 | 1.00 | 550.6 | 0.867 |
| 90 | 1.00 | 581.4 | 0.876 |
| 100 | 1.00 | 622.2 | 0.859 |

(a)

![](https://cdn.mathpix.com/cropped/2024_04_26_3866e766709bfcc53f87g-11.jpg?height=651&width=828&top_left_y=1345&top_left_x=271)

(b)

![](https://cdn.mathpix.com/cropped/2024_04_26_3866e766709bfcc53f87g-11.jpg?height=646&width=674&top_left_y=1353&top_left_x=1094)

Fig. 2. (a) City-number dependence of the average number of iterations required to obtain an approximate solution using the Improved Amoeba TSP algorithm, which turns out to scale with $\sqrt{n}$. Inset shows the comparison with results of the original Amoeba TSP algorithm [26], which scales linearly with $n$. (b) City-number dependence of the average of normalized route length $R_{\text {calc }} / R_{\text {est }}$ obtained by the Improved Amoeba TSP algorithm. The dashed lines represents $R_{\text {calc }} / R_{\text {est }}=0.9$ as a universal result of the original Amoeba TSP algorithm.

ability of the amoeba-inspired combinatorial optimization machine and gives a basis towards their implementations with physical devices.

## 8. Acknowledgment

We are indebted to Masashi Aono for insightful discussions. This work is supported by Japan Society for the Promotion of Science KAKENHI (Grant No. 20H00337, 22H05114), CREST, the Japan Science and Technology Agency (Grant No. JPMJCR20T1), and a Waseda University Grant for Special Research Projects (Project No. 2023C-140, 2023E-026, 2024C-153, 2024C-155).

## References

[1] J.L. Hennessy and D.A. Patterson, Computer Architecture: A Quantitative Approach, 6th Edition, Morgan Kaufmann Publishers, Boston, 2017.

[2] M.R. Garey and D.S. Johnson, Computers and Intractability: A Guide to the Theory of NPCompleteness, W. H. Freeman and Company, New York, 1979.

[3] M.W. Johnson, M.H.S. Amin, S. Gildert, T. Lanting, F. Hamze, N. Dickson, R. Harris, A.J. Berkley, J. Johansson, P. Bunyk, E.M. Chapple, C. Enderud, J.P. Hilton, K. Karimi, E. Ladizinsky, N. Ladizinsky, T. Oh, I. Perminov, C. Rich, M.C. Thom, E. Tolkacheva, C.J.S. Truncik, S. Uchaikin, J. Wang, B. Wilson and G. Rose, "Quantum annealing with manufactured spins," Nature, vol. 473, pp. 194-198, May 2011.

[4] M. Yamaoka, C. Yoshimura, M. Hayashi, T. Okuyama, H. Aoki and H. Mizuno, "A 20k-Spin Ising Chip to Solve Combinatorial Optimization Problems With CMOS Annealing," IEEE Journal of Solid-State Circuits, vol. 51, no. 1, pp. 303-309, January 2016.

[5] T. Inagaki, Y. Haribara, K. Igarashi, T. Sonobe, S. Tamate, T. Honjo, A. Marandi, P.L. McMahon, T. Umeki, K. Enbutsu, O. Tadanaga, H. Takenouchi, K. Aihara, K. Kawarabayashi, K. Inoue, S. Utsunomiya and H. Takesue, "A coherent Ising machine for 2000-node optimization problems," Science, vol. 354, no. 6312, pp. 603-606, October 2016.

[6] M. Aramon, G. Rosenberg, E. Valiante, T. Miyazawa, H. Tamura and H.G. Katzgraber, "PhysicsInspired Optimization for Quadratic Unconstrained Problems Using a Digital Annealer," Frontiers in Physics, vol. 7, no. 48, pp. 1-14, April 2019.

[7] H. Goto, K. Tatsumura and A.R. Dixon, "Combinatorial optimization by simulating adiabatic bifurcations in nonlinear Hamiltonian systems," Science Advances, vol. 5, no. 4, pp. 1-8, April 2019.

[8] T. Kadowaki and H. Nishimori, "Quantum annealing in the transverse Ising model," Physical Review E, vol. 58, no. 5, pp. 5355-5363, November 1998.

[9] A. Lucas, "Ising formulations of many NP problems," Frontiers in Physics, vol. 2, no. 5, pp. $1-15$, February 2014.

[10] Advances in Physarum Machines: Sensing and Computing with Slime Mould, ed. A. Adamatzky, Springer Cham, Cham, 2016.

[11] M. Aono, "Amoeba-inspired combinatorial optimization machines," Japanese Journal of Applied Physics, vol. 59, no. 6, pp. 1-12, May 2020.

[12] D. Kessler, "Plasmodial structure and motility," in Cell biology of Physarum and Didymium Vol. 1, ed. H. C. Aldrich and J. W. Daniel, p. 145, Academic Press, New York, 1982.

[13] T. Nakagaki, H. Yamada and Á. Tóth, "Maze-solving by an amoeboid organism," Nature, vol. 407, p. 470, September 2000.

[14] A. Tero, S. Takagi, T. Saigusa, K. Ito, D.P. Bebber, M.D. Fricker, K. Yumiki, R. Kobayashi and T. Nakagaki, "Rules for Biologically Inspired Adaptive Network Design," Science, vol. 327, no. 5964, pp. 439-442, January 2010.

[15] M. Aono, M. Hara and K. Aihara, "Amoeba-based neurocomputing with chaotic dynamics," Communications of the ACM, vol. 50, no. 9, pp. 69-72, September 2007.

[16] M. Aono, Y. Hirata, M. Hara and K. Aihara , "Amoeba-based Chaotic Neurocomputing: Combinatorial Optimization by Coupled Biological Oscillators," New Generation Computing, vol. 27, pp. 129-157, April 2009.

[17] L. Zhu, M. Aono, S-J. Kim and M. Hara, "Amoeba-based computing for traveling salesman problem: Long-term correlations between spatially separated individual cells of Physarum polycephalum," BioSystems, vol. 112, no. 1, pp. 1-10, April 2013.

[18] K. Iwayama, L. Zhu, Y. Hirata, M. Aono, M. Hara and K. Aihara, "Decision-making ability of Physarum polycephalum enhanced by its coordinated spatiotemporal oscillatory dynamics," Bioinspiration E3 Biomimetics, vol. 11, no. 3, pp. 456-789, April 2016.

[19] M. Aono, M. Naruse, S-J. Kim, M. Wakabayashi, H. Hori, M. Ohtsu and M. Hara, "AmoebaInspired Nanoarchitectonic Computing: Solving Intractable Computational Problems Using

Nanoscale Photoexcitation Transfer Dynamics," Langmuir, vol. 29, no. 24, pp. 7557-7564, April 2013.

[20] S. Kasai, M. Aono and M. Naruse, "Amoeba-inspired computing architecture implemented using charge dynamics in parallel capacitance network," Applied Physics Letters, vol. 103, no. 16, pp. $1-4$, October 2013.

[21] M. Aono, S. Kasai, S-J. Kim, M. Wakabayashi, H. Miwa and M. Naruse, "Amoeba-inspired nanoarchitectonic computing implemented using electrical Brownian ratchets," Nanotechnology, vol. 26, no. 23, pp. 1-8, May 2015.

[22] N. Takeuchi, M. Aono and N. Yoshikawa, "Superconductor Amoeba-Inspired Problem Solvers for Combinatorial Optimization," Physical Review Applied, vol. 11, no. 4, pp. 1-9, April 2019.

[23] Y. Hara-Azumi, N. Takeuchi, K. Hara and M. Aono, "Digital bio-inspired satisfiability solver leveraging fluctuations," Japanese Journal of Applied Physics, vol. 59, no. 4, pp. 1-10, March 2020.

[24] K. Saito, M. Aono and S. Kasai, "Amoeba-inspired analog electronic computing system integrating resistance crossbar for solving the travelling salesman problem," Scientific Reports, vol. 10, pp. 1-9, November 2020.

[25] M. Aono, S-J. Kim, L. Zhu, M. Naruse, M. Ohtsu, H. Hori and M. Hara, "Amoeba-inspired SAT Solver," Proc. NOLTA'12, pp. 586-589, October 2012.

[26] L. Zhu, S-J. Kim, M. Hara and M. Aono, "Remarkable problem-solving ability of unicellular amoeboid organism and its mechanism," Royal Society Open Science, vol. 5, no. 12, pp. 1-13, December 2018.

[27] K. Saito and S. Kasai, "Effect of feedback delays on solution quality in amoeba-inspired computing system that solves traveling salesman problem," Applied Physics Express, vol. 13, no. 11, pp. 1-5, October 2020.

[28] J.J. Hopfield and D.W. Tank, "Computing with Neural Circuits: A Model," Science, vol. 233, no. 4764 , pp. 625-633, August 1986.

[29] D.L. Applegate, R.E. Bixby, V. Chvatal, and W.J. Cook, The Traveling Salesman Problem: A Computational Study, Princeton University Press, Princeton, 2006.

