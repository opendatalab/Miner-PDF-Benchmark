Paper

# Proposed Modified Computational Model For The Amoeba-Inspired Combinatorial Optimization Machine

Yusuke Miyajima A 1 *and Masahito Mochizuki* A 1 1 *Department of Applied Physics, Waseda University, Okubo, Shinjuku-ku,*
Tokyo 169-8555 Received October 27, 20XX; Revised December 29, 20XX; Published July 1, 20XX
Abstract: A single-celled amoeba can solve the traveling salesman problem through its shapechanging dynamics. In this paper, we examine roles of several elements in a previously proposed computational model of the solution-search process of amoeba and three modifications towards enhancing the solution-search preformance. We find that appropriate modifications can indeed significantly improve the quality of solutions. It is also found that a condition associated with the volume conservation can also be modified in contrast to the naive belief that it is indispensable for the solution-search ability of amoeba. A proposed modified model shows much better performance.

Key Words: natural computing, amoeba-inspired machine, traveling salesman problem, combinatorial optimization

## 1. Introduction

In the modern information society, conventional Neumann-type computers face a serious problem of increased complexity and cost in computation. While the information processing capacity of computers is predicted to reach its limits because of the limit of Moore's law and the von Neumann bottleneck, the required computing power is increasing exponentially. Under these circumstances, new efficient domain-specific computational architectures beyond the von Neumann type are demanded [1]. The serious problem particularly appears in combinatorial optimization problems [2]. Recently, the Ising machine has been proposed as a solution and its practical applications are being investigated [3–7]. There, the combinatorial optimization problem is mapped onto the ground-state search of the Ising model, which is originally a mathematical model of magnetic materials [8, 9]. On the other hand, research has been intensively conducted to construct combinatorial optimization machines that mimic the information processing of living organisms. This is because organisms often perform sophisticated information processing such as image recognitions, sound recognitions, and optimizations with low energy consumption.

One of the simplest and most useful machines of such kinds is a computing technology inspired by the information processing of the amoeboid organism [10, 11]. This technology exploits the dynamics of unicellular slime mold, which transforms its body in response to the surroundings for survival. Specifically, it exploits the behaviors of the body to stretch for getting food and to shrink for avoiding light [12]. As demonstrated in the previous experimental study, unicellular slime molds are able to solve optimization problems such as mazes [13, 14], satisfiability problems [15], and traveling salesman problems (TSP) [16–18]. The superior solution-search capability derives from the shapechanging dynamics of amoeba, where the law of conservation of total volume is satisfied [18]. In other words, slime molds have high ability of the information processing despite being unicellular organisms and lacking a central information-processing mechanism. This situation has attracted attention as a model for an autonomous decentralized parallel computing architecture of high efficiency beyond the von Neumann architecture. However, motion of slime molds is as slow as 10−5 m/s, making it difficult to use them as practically usable machines. Therefore, research interest has focused on attempts to implement the information-processing processes of slime molds with physical devices as amoeba-inspired combinatorial optimization machines [19–24]. For simplicity, we will refer to slime mold as amoeba hereafter.

To realize the amoeba-inspired machines, a computational model (algorithm) for the solution-search process of amoeba should be constructed first [25–27]. An important model has been proposed by Aono and his coworkers, which is named Amoeba TSP algorithm [26]. Its physical implementation using analogue electronic circuits has been demonstrated by a subsequent experiment [24]. The model has turned out to describe well the amoeba dynamics and resulting solution-search ability. However, we do not have sufficient knowledge about roles of elements constituting the model on its solutionsearch ability. For example, the fluctuations expected to exist in the amoeba dynamics are taken into account using uniformly distributed random numbers within a certain range. However, the necessity of the fluctuations for the optimization ability is not trivial. Moreover, it has not been clarified how the optimization performance is affected if we change the distribution of random numbers. Insights into the role of each element in the model are expected to provide the guide for constructing the amoeba-inspired machines with higher solution-search ability.

In this paper, we study roles, effects, and (un)necessities of several elements of the Amoeba TSP
algorithm by examining how modifications of the elements affect the optimization performance of the algorithm. It is found that appropriate modifications can significantly improve the optimization performance. On the basis of these examinations, we propose a modified model named Improved Amoeba TSP algorithm, which turns out to provide much better solutions in terms of the number of iterations and the route length. It has also turned out that even a condition originating from the volume conservation law assumed in the original model can be modified for the high solution-search ability in contrast to the naive belief, which may release us from the related constraints against the physical implementation.

This paper is structured as follows. In Section 2, a formalism of the TSP proposed by Hopfield and Tank is introduced [28]. Section 3 describes the concept of amoeba-inspired combinatorial optimization machine for solving the TSP. Specifically, an experiment with a biological slime mold and a computational model named Amoeba TSP algorithm are introduced. In Section 4, the parameters and conditions of the experiment and numerical simulations are described. In Section 5, we argue three elements of the model that characterize the Amoeba TSP algorithm and examine how modifications of these elements affect the optimization performance. In Section 6, a computational model named Improved Amoeba TSP algorithm is proposed. Section 7 is devoted to the summary.

## 2. Formalism Of The Traveling Salesman Problem

We first present a formalism of the TSP [29]. The TSP is a problem to find the shortest route for a given map which satisfies the condition that every city must be visited (only) once. When the number of cities is n, the number of candidate solutions is (n − 1)!/2, which increases exponentially with increasing n. The TSP is known as one of the NP-hard problems, that is, no algorithm can solve this problem within polynomial computational time. Therefore, it is a popular approach in practical cases to search an approximate solution by heuristic algorithms. In our study, we attempt to obtain an approximate solution using the amoeba-inspired combinatorial optimization algorithm.

We start with a brief introduction of the formalism proposed by Hopfield and Tank. For the n-city TSP, n 2 binary variables xV k(= 0, 1) are used to represent the routes, where the indices V (= 1, 2, · · · , n) and k(= 1, 2, · · · , n) represent a labeling number of the cities and a visiting order of the cities, respectively. Here, xV k = 1(0) means that the city labeled as V is (is not) visited at the kth order. The cost function to be optimized in the searching procedure is defined as,

E({xV k}) = − 1 2 Xn V =1 Xn U=1 Xn k=1 Xn l=1 WV k,U l xV k xU l. (1)
Two constraints of the TSP are given by the following equations,

$$\sum_{k=1}^{n}x_{Vk}=1,\qquad\quad\sum_{V=1}^{n}x_{Vk}=1.\tag{1}$$

The former constraint prohibits revisiting once-visited cities, and the second constraint prohibits visiting more than one city simultaneously. The TSP is reduced to a problem to search a combination of n 2 binary variables {xV k} which minimizes the cost function in Eq. (1) with satisfying the constraints.

Here, the cost W*V k,U l* is concerned with the distance between two cities and the penalty for violation of the constraints, which is defined by,

$$W_{V k,U l}=\left\{\begin{array}{l}{{-\lambda}}\\ {{-\mu}}\\ {{-\nu\cdot d(V,U)}}\\ {{-\nu\cdot d(V,U)}}\\ {{-\nu\cdot d(V,U)}}\\ {{0}}\end{array}\right.$$
−λ (V = U ∧ k ̸= l),
−µ (V ̸= U ∧ k = l),
−ν · d(*V, U*) (V ̸= U ∧ |k − l| = 1),
−ν · d(*V, U*) (V ̸= U ∧ k = n ∧ l = 1),
−ν · d(*V, U*) (V ̸= U ∧ k = 1 ∧ l = n),
0 (otherwise).
$$\left(1\right)$$
$$\left(2\right)$$
$(V=U\wedge k\neq l)$,  $(V\neq U\wedge k=l)$,  $(V\neq U\wedge|k-l|=1)$,  $(V\neq U\wedge k=n\wedge l=1)$,  $(V\neq U\wedge k=1\wedge l=n)$,  $($otherwise$).  
Here λ, µ and ν are positive parameters, and d(*V, U*) represents the distance between two cities V and U. The parameters λ and µ, respectively, give costs for the penalty when the constraints in Eq. (2) are violated, while ν gives a cost proportional to the distance between two cities visited successively. The fourth and the fifth costs are concerned with the distance between the final and initial cities (The salesman must come back to the initial city finally). The value of the cost function is proportional to the route length when the constraints are satisfied. Note that the cost function in this formulation does not explicitly include the penalty terms for satisfying the constraints such as Pn k=1 xV k − 1 and Pn V =1 xV k − 1 in contrast to other optimization machines, e.g., Ising machines.

In this study, we evaluate the results obtained by the amoeba-based optimization machine and the computational models (algorithms) in terms of the following three criteria,
- Success rate for finding an approximate solution within the given time or number of iterations,

- Average of time or number of iterations required to find an approximate solution, - Average of the normalized route length for the obtained solutions
The averages in the latter two are taken over all the successful trials of the solution search. The normalized route length of an obtained solution is defined as Rcalc/Rest, where Rcalc and Rest are the route length of the obtained solution and the estimated mean route length, respectively. A smaller average of Rcalc/Rest means that the amoeba-based optimization machine or the computational model is capable of finding a solution with a shorter route length.

## 3. Amoeba-Inspired Combinatorial Optimization Machine 3.1 Experiment

Aono and coworkers experimentally demonstrated that the shape-changing dynamics of amoeba induced by environmental stimuli, i.e., nutrient and light, can be used for efficient searches for approximate solutions of the TSP [16]. Figure 1(a) shows schematics of the amoeba-based device and the optical feedback system used in the experiment, while Figs. 1(c) and 1(d) show initial and final states of the amoeba-based device. The device is set on an agarose plate with nutrient. The optical feedback system consists of a PC, a projector and a video camera. The device is composed of a central hub

![3_image_0.png](3_image_0.png)

part and n 2lanes to represent solutions of the TSP. Each lane corresponds to one continuous variable XV k ∈ [0, 1] for V = 1, 2, · · · , n and k = 1, 2, · · · , n and thus is referred to as the lane V k. The body of amoeba in a lane is called branch. The variable XV k is defined as the ratio of area occupied by the amoeba to the total area in the lane V k, which is referred to as length of the branch in the lane V k. The cost function with binary variables {xV k} in Eq. (1) is adopted in the experiment. The continuous variables XV k are translated to the binary variable xV k where xV k equals to 1 (0) when XV k equals to (is less than) unity. Namely, xV k takes 1 only when the lane is fully occupied by the branch. We read out a solution {xV k} of the TSP from a state of the branches of amoeba {XV k} in this manner in the experiment.

The optical feedback system illuminates the lanes and updates the state of the branches so as to minimize the cost function. The value of XV k is measured by the video camera, and LV k defined by Eq. (4) is calculated from all the values of XV k by the PC. Here LV k is a function of an integer variable t representing the number of time step. A time step corresponds to six seconds.

$$L_{Vk}(t+1)=1-\sigma_{1000,-0.5}\left(\sum_{U=1}^{n}\sum_{l=1}^{n}W_{Vk,Ul}\ \sigma_{35,0.6}(X_{Ul}(t))\right).\tag{4}$$  **void function defined by**
Here $\sigma_{\gamma,\theta}$ is a sigmoid function defined by,. 
defined by $\!\,$. 
$$\sigma_{\gamma,\theta}(x)=\frac{1}{1+\exp(-\gamma(x-\theta))}.$$
1 + exp(−γ(x − θ)). (5)
$$\left(5\right)$$

The lane V k will (will not) be illuminated by the projector when LV k is greater (less) than 0.5. We call a combination of the step functions θ(LV k − 0.5) for all the lanes as the illumination pattern for each step. The amoeba basically elongates its branches in non-illuminated lanes to efficiently absorb the nutrient from the agarose plate. On the contrary, the amoeba basically contracts its branches in illuminated lanes to avoid the light stimuli. The illumination is a penalty to prevent amoeba from choosing solutions with significantly long route lengths or those violating the constraints in Eq. (2).

In the initial state, the amoeba occupies only the hub part of device and does not occupy any lanes at all, that is, XV k = 0 for all sets of V k [Fig. 1(c)]. The operation for calculating the illumination pattern {θ(LV k−0.5)} and updating a state of the branches {XV k} by illumination or non-illumination is iterated to minimize the cost function. Finally, only the n lanes are fully occupied with amoeba's branches and the others are empty, that is, XV k equals to 1 for n sets of indices V k [Fig. 1(d)].

Eventually, an approximate solution is obtained [Fig. 1(b)].

According to the results of this experiment [26], the approximate solutions are obtained for almost all the trials and the average time required to obtain a solution increases linearly to the number of cities n. It has also turned out that the average of the normalized route lengths Rcalc/Rest takes 0.9 almost irrespective of n. Although the number of candidate solutions grows exponentially with increasing n, the amoeba is able to efficiently find an approximate solution with a reasonable route length. The detailed observation provides us an insight that this high solution-search ability of the amoeba originates from the fluctuating dynamics. The amoeba sometimes elongates (contracts) its branches even though the corresponding lane is (is not) illuminated. These slightly fluctuating responses enable to escape from local optimal solutions and to explore wider space of solutions in the searching process.

However, it takes several ten minutes to find an approximate solution for real amoebas. This time scale is too long for practical use. Therefore, it is necessary to implement this high solution-searching capability of amoeba on a physical combinatorial optimization machine.

## 3.2 Computational Model: Amoeba Tsp Algorithm

A computational model named Amoeba TSP algorithm has been proposed to reproduce the results of above experiment [26]. This model describes the time evolution of amoeba's branches in the lanes XV k(t) by the following equation,

$$X_{Vk}(t+1)=\left\{\begin{array}{ll}X_{Vk}(t)-O_{Vk}(t+1)+\xi_{Vk}(t+1)&(L_{Vk}(t+1)>0.5),\\ X_{Vk}(t)+I_{Vk}(t+1)+\xi_{Vk}(t+1)&(L_{Vk}(t+1)\leq0.5).\end{array}\right.\tag{6}$$

In this mode, the value of XV k can take an arbitrary real number and is not restricted to [0, 1] unlike the experiment. The state of the branches {XV k} is updated according to this equation. Here the variables OV k (IV k) are amounts of contraction (elongation) of a branch in the lane V k when the lane is (is not) illuminated. The variables ξV k ∈ [−*δ, δ*] are uniform random numbers describing intrinsic fluctuations in the dynamics of amoeba branches.

First, LV k(t + 1) is calculated from XV k(t) using Eq. (4) with the costs W*V k,U l* in Eq. (3) for all the sets of V k. Next, the branch lengths XV k(t) are updated to XV k(t+ 1) using Eq. (6) based on the values of LV k. Iterating the calculations of the illumination pattern {θ(LV k − 0.5)} and updating the state of the branches {XV k} alternately, we obtain an approximate solution of the TSP. We perform these two procedure based on Eq. (4) and Eq. (6) for all lanes as one iteration step. Here, the number of iterations is given by a integer t and the variables updated in every iteration step are defined as functions of t.

The variables OV k(t) and IV k(t) are defined by,

$$\begin{array}{l l}{{}}&{{{\cal O}_{V k}(t+1)=\left\{\begin{array}{l l}{{2\Delta^{\mathrm{out}}\sigma_{20,0,6}(X_{V k}(t))}}&{{(L_{V k}(t+1)>0.5)}}\\ {{0}}&{{(L_{V k}(t+1)\leq0.5)}}\end{array}\right.}}\\ {{}}&{{{\mathrm{}}}}\\ {{}}&{{{\mathrm{}}}}\\ {{I_{V k}(t+1)=\left\{\begin{array}{l l}{{\left(\Delta^{\mathrm{in}}+\sum_{V=1}^{n}\sum_{k=1}^{n}{{\cal O}_{V k}(t+1)+S(t)\right)/L^{\mathrm{off}}(t+1)}}&{{(L^{\mathrm{off}}(t+1)>0)}}\\ {{0}}&{{(L^{\mathrm{off}}(t+1)=0)}}\end{array}\right.}}\end{array}\right.}}\end{array}$$

with

$$\quad(7)$$
$$(8)$$
$$S(t+1)=\left\{\begin{array}{ll}0&(L^{\rm off}(t+1)>0)\\ S(t)+\Delta^{\rm in}+\sum_{V=1}^{n}\sum_{k=1}^{n}O_{Vk}(t+1)&(L^{\rm off}(t+1)=0)\end{array}\right.\tag{9}$$

Here ∆out and ∆in are parameters representing the degree of the contraction and the elongation of branches. The variable L
off(t) is the number of non-illuminated lanes.

Roughly speaking, Eq. (7) means that when LV k(t + 1) > 0.5, the branch in the lane V k should contract approximately by 2∆out if the original length XV k(t) is longer than a certain value of ∼ 0.6.

On the other hand, Eq. (8) means that there are three contributions to the elongation of branch in the lane V k when LV k(t+ 1) ≤ 0.5. The first contribution associated with ∆in assumes that a certain amount (∆in) of amoeba's body consistently leaks out from the hub part towards the lane part, and it results in the elongation of each branch by ∆in/Loff via equitable distribution when the number of non-illuminated lanes is L
off. The second term associated with OV k(t + 1) means that a sum of the contracted portions of the illuminated branches are redistributed equally to the non-illuminated lanes.

The elongation of branch occurs mostly by equitable distribution of the sum of the contracted amounts of branches in illuminated lanes as well as the constant leak from the hub part to the L
off non-illuminated lanes. However, there should be a case that all the lanes are illuminated, i.e., L
off = 0.

In such a case, these contributions are stocked at the moment, and will be leaked to non-illuminated lanes equally when L
off becomes nonzero. The variable S(t) defined in Eq. (9) describes this situation, and this is the third contribution to the elongation described in Eq. (8).

In addition, the following condition is imposed in the computational model to reproduce the experimental results,

$$\sum_{V k\in\mathrm{off}}\left\{I_{V k}(t+1)+\xi_{V k}(t+1)\right\}-\sum_{V k\in\mathrm{on}}\left\{O_{V k}(t+1)-\xi_{V k}(t+1)\right\}\approx\Delta^{\mathrm{in}}.$$
$$(10)$$

Here PV k∈off (PV k∈on) denotes the summation over the non-illuminated (illuminated) lanes. This condition represents a law of conservation where the sum of the elongated (positive) and contracted
(negative) amounts of the branches equals to ∆in constantly at every iteration step, which is the amount of leak from the hub part to the lanes. This condition is introduced by an idea that if the sum of XV k increases by a certain constant rate per unit time, the time required for the solution search is expected to be proportional to n, because the sum of XV k becomes n in the end. The variable S(t) is introduced to satisfy this condition at every iteration step as long as L
off ̸= 0.

In the previous simulation in Ref. [26], they perform 1000 trials of a solution search for the TSP
with 10 to 20 cities by using the original Amoeba TSP algorithm. The obtained results coincide well with those in the experiment. The approximate solutions are obtained for almost all the trials and the average number of iterations turns out to be proportional to n. Moreover, the average of the normalized route length Rcalc/Rest takes a constant value of 0.9 irrespective of the number of cities n.

It should be mentioned that although the number of iterations is proportional to n, the total CPU time for the calculation is, in fact, proportional to n 5. The serial process of CPU requires computational time proportional to n 4for treating the n 4components of the cost tensor W*V k,U l* to calculate the illumination pattern LV k(t). Therefore, only the computational model is not sufficient for the practical application. We need to physically implement the model as a combinatorial optimization machine where the serial calculation by CPU is substituted with parallel physical phenomena to realize the efficient solution search. However, the physical implementation of the Amoeba TSP algorithm is difficult, and only an attempt using analog electronic circuits has succeeded in this challenge so far [24]. The difficulty stems partly from the strict condition of Eq. (10). In this paper, we propose a modified computational model of the amoeba-inspired combinatorial optimization machine, which, we expect, is suitable for physical implementation.

## 4. Calculation Conditions

We present the values of parameters in the numerical simulations and how to determine them before introducing the results.

## 4.1 Parameters

Table I shows the values of parameters used in our numerical simulations. The parameters λ and µ give costs as penalties to the revisiting once-visited city and the simultaneous visits to multiple cities, respectively. Their values are fixed at λ=0.5 and µ=0.5 throughout the numerical simulations.

The parameter ν gives the cost proportional to the route length. Importantly, the costs for violating the constraints must be larger than those for increasing in the route length. On the other hand, the difference between route lengths should be evaluated as large as possible. On the basis of these two policies, the value of ν is determined by the following procedure. We consider combinations of three cities (V1, V2, V3) out of n cities and the routes from V1 to V3 via V2 where the route length is d(V1, V2) + d(V2, V3). The value of ν is determined so as to satisfy the following inequality,

$V_1,V_2)+d(V_2,V_2)\}\leq i$
ν · max{d(V1, V2) + d(V2, V3)} ≤ min{*λ, µ*}. (11)
We also consider that the value of ν should be set as close as possible to ν
∗ where,

$\{\lambda,\mu\}$. 
$\left(11\right)_0$
 $\nu^*\equiv\dfrac{\min\{\lambda,\mu\}}{\max\{d(V_1,V_2)+d(V_2,V_3)\}}.$  when n=20. 
$$\left(12\right)$$
. (12)
For example, we set ν=0.00176 when n=20.

The parameter δ gives upper and lower bounds of the uniform random number ξV k in the Amoeba TSP algorithm. The parameters ∆out and ∆in are fixed at ∆out=0.001 and ∆in=0.001 throughout the present work.

  \begin{table} \begin{tabular}{l c c c c} \hline $\lambda$ & $\mu$ & $\delta$ & $\Delta^{\rm out}$ & $\Delta^{\rm in}$ \\ \hline $0.5$ & $0.5$ & $0.003$ & $0.001$ & $0.001$ \\ \hline \end{tabular} \\ \hline \end{tabular} \end{table} Table 1: Parameter values used for the numerical simulations. 
Maps of TSP are produced such that all the distances between two cities are given by a set of normal random numbers with a mean of 100 and a standard deviation of 17, with which Rest approximately equals to 100n for the n-city TSP.

## 4.2 Conversion To The Solution

In our numerical simulations, we abort the iteration to obtain an approximate solution {Xbin V k } when the binary variables Xbin V k ≡ θ(XV k − 0.99) satisfy the following conditions,

$$\sum_{V=1}^{n}X_{V k}^{\mathrm{bin}}=1,\qquad\quad\sum_{k=1}^{n}X_{V k}^{\mathrm{bin}}=1.$$
$$(13)$$

In the iteration process, we check whether the conditions are satisfied at every iteration step.

## 5. Modifications Of The Model

We focus on the following three elements A, B, and C, which characterize the Amoeba TSP algorithm, and examine how their modifications affect the optimization performance,
(Element A) The fluctuation ξV k is given by a uniform random number,
(Element B) The sum of XV k increases by ∆in at every iteration step as described in Eq. (10),
(Element C) Sigmoid functions are used in Eq. (4) for LV k(t + 1) and in Eq. (7) for OV k.

We perform 1000 solution-search trials for the 20-city TSP using a computational model with a modification in one of these three elements. We compare the obtained results with those obtained by the original algorithm to judge which elements are substantially important for the optimization performance.

## 5.1 Modifications Of Element A We First Examine The Following Two Types Of Modifications For Element A, That Is,

(A-1) Removing the fluctuations by setting ξV k=0,
(A-2) Using normal random numbers for the fluctuations ξV k.

Table II shows the results obtained by the modified models together with those obtained by the original model using uniform random numbers ranging in [−0.003, 0.003] for the fluctuations. Noticeably, we cannot obtain an approximate solution in any of 1000 trials with the modification (A-1), which clearly indicates that the solution-search ability of amoeba indeed relies on the fluctuations in its dynamics. For the modification (A-2), we examine the normal random numbers with a mean of 0 and a standard deviation of 0.003 for ξV k and find that the number of iterations is significantly suppressed by 29% as compared with the original algorithm, while the success rate does not change so much.

Summarizing the results of these examinations, we conclude that the fluctuation ξV k is indispensable for the solution-search procedure, and normal random numbers are more suitable for efficient searches, which can significantly reduce the required number of iterations as compared with uniform random numbers.

| the trials in which the modified algorithm successfully finds an approximate solution within 3000 iterations (Success rate), the average number of iterations required to find an approximate solution (Average number of iterations), and the average of the normalized route lengths of obtained solutions (Average of Rcalc/Rest). The results obtained by the original Amoeba TSP algorithm is presented for comparison.   |              |                              |                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------------------------|-----------------------|
| Modification                                                                                                                                                                                                                                                                                                                                                                                                                   | Success rate | Average number of iterations | Average of Rcalc/Rest |
| (A-1)                                                                                                                                                                                                                                                                                                                                                                                                                          | 0.000        | ——                           | ——                    |
| (A-2)                                                                                                                                                                                                                                                                                                                                                                                                                          | 0.986        | 1326.8                       | 0.941                 |
| Original                                                                                                                                                                                                                                                                                                                                                                                                                       | 0.992        | 1870.6                       | 0.951                 |

## 5.2 Modifications Of Element B

We next examine the following four types of modifications for Element B, that is,
(B-1) Replacing IV k(t) with 0.9IV k(t) in Eq. (6),
(B-2) Replacing IV k(t) with 1.1IV k(t) in Eq. (6),
(B-3) Setting ∆in at zero in Eqs. (8) and (9),
(B-4) Replacing L
off with n in Eq. (8).

Table III shows the results obtained by the modified models together with those obtained by the original model. Concerning the modifications (B-1) and (B-2), the increase rate IV k of XV k when LV k ≤ 0.5 is suppressed by 10% for the former, while it is enhanced by 10% for the latter. The conservation law in Eq. (10) is violated by these modifications. For the modification (B-3), the constant leak from the hub part to the lanes ∆in is set to be zero. With this modification, a sum of the elongated and contracted amounts of the branches is always cancelled except for the contributions from the fluctuations. For the modification (B-4), L
off in Eq. (8) is repalced with the number of cities n, which is based on an idea that L
off finally becomes n when a solution is obtained. This modification releases us from counting the number L
off of non-illuminated lanes at every iteration step. Moreover, this modification is expected to boost the solution search by enhancing the increase rate IV k at each step because n should be much smaller than L
off particularly in the early stage of the iteration.

According to Table III, we find that a larger increase rate IV k of XV k at every step results in the better performance in terms of the number of iterations and the route length. In particular, the modification (B-4) reduces the number of iterations by 44% as compared to the original Amoeba TSP algorithm. On the contrary, the success rate is not improved by any of these modifications.

So far, it has been naively believed that nonlocal correlations among branches manifested by the conservation law are indispensable to reproduce the solution-search ability of amoeba. Namely, we assume that a sum of the elongated (positive) and contracted (negative) amounts of branches should constantly equal to the amount of leak ∆in from the amoeba body in the hub part. However, our study has demonstrated that the conservation rule is not required to solve TSP for the amoeba TSP algorithm. Moreover, it has turned out that much better solutions can be obtained if the conservation rule is removed. Surprisingly, the excellent solution-search ability of amoeba turns out to be attributable only to its fluctuating dynamics associated with its shape deformation.

| Table III.   | Optimization results obtained by the modifications of Element B.   |                              |                       |
|--------------|--------------------------------------------------------------------|------------------------------|-----------------------|
| Modification | Success rate                                                       | Average number of iterations | Average of Rcalc/Rest |
| (B-1)        | 0.990                                                              | 1937.4                       | 0.957                 |
| (B-2)        | 0.992                                                              | 1817.4                       | 0.949                 |
| (B-3)        | 0.996                                                              | 1989.7                       | 0.958                 |
| (B-4)        | 0.994                                                              | 1049.3                       | 0.912                 |
| Original     | 0.992                                                              | 1870.6                       | 0.951                 |

## 5.3 Modifications Of Element C

We finally examine the following three types of modifications for Element C, that is,
(C-1) Replacing the sigmoid function σ20,0.6(x) in Eq. (7) with 1, (C-2) Replacing the sigmoid function σ1000,−0.5(x) in Eq. (4) with the step fumction θ(x + 0.5),
(C-3) Replacing the sigmoid function σ35,0.6(x) in Eq. (4) with the step fumction θ(x − 0.6).

Table IV shows the results obtained by the modified models together with those obtained by the original model. For the modification (C-1), the decrease rate OV k of XV k when LV k > 0.5 becomes independent of XV k. We find that the number of iterations is reduced by 48% as compared with the original Amoeba TSP algorithm by this modification. For the modification (C-2), the sigmoid function σ1000,−0.5(x) in Eq. (4) is replaced with the step function θ(x + 0.5). According to Table IV,
we learn that the results are not affected so much by these modifications. For the modification (C-3),
the sigmoid function σ35,0.6 in Eq. (4) is replaced with the step function with θ(x − 0.6). Table IV
shows that the success rate becomes much worse with this modification, i.e., typically less than half of those obtained by the original algorithm. Moreover, the number of iterations becomes 1.4 times larger than those for the original algorithm.

These results offer several insights into the Amoeba TSP model to achieve a better optimization with less computational time. First, the decrease rate OV k of XV k in Eq. (7) should be given as a constant 2∆out without depending on the value of XV k. Second, the sigmoid function σ1000,−0.5 in Eq. (4)
should be replaced with the step function. On the other hand, σ35,0.6 is necessary to search approximate solutions of the TSP. Note that the argument of σ1000,−0.5,PnU=1 Pn l=1 WV k,U lσ35,0.6(XU l(t)),
corresponds to the derivative of the cost function in Eq. (1) by xV k when σ35,0.6 is replaced with the step function with a threshold 0.6 and xV k is defined as θ(XV k − 0.6). Owing to the finite slope of σ35,0.6, the combination of XV k resulting in larger cost, PnU=1 Pn l=1 WV k,U lσ35,0.6(XU l(t))(≤ −0.5),
is sometimes allowed in the solution-searching process and thus the computational model is able to search in wider solution space without trapped in certain local optimal solutions.

## 6. Improved Amoeba Tsp Model

According to the above examinations, we have found three modifications that can improve the optimization results significantly,

| Table IV.    | Optimization results obtained by the modifications of Element C.   |                              |                       |
|--------------|--------------------------------------------------------------------|------------------------------|-----------------------|
| Modification | Success rate                                                       | Average number of iterations | Average of Rcalc/Rest |
| (C-1)        | 1.000                                                              | 974.5                        | 0.952                 |
| (C-2)        | 0.991                                                              | 1874.8                       | 0.953                 |
| (C-3)        | 0.460                                                              | 2578.7                       | 1.000                 |
| Original     | 0.992                                                              | 1870.6                       | 0.951                 |

- Using normal random numbers for the fluctuations ξV k (A-2),

- Replacing L
off with the number of cities n (B-4),
- Replacing the sigmoid function σ20,0.6(x) in Eq. (7) with unity (C-1).
In Table V, we also summarize items of the optimization improved by each modification. We construct a computational model named Improved Amoeba TSP algorithm by applying the three modifications to the Amoeba TSP algorithm. We perform 1000 solution-search trials for the n-city TSPs with n=10-100 by using the Improved Amoeba TSP algorithm.

| + and − denote excellent, good and bad effects for each criterion, respectively. The symbol 0 denotes a neutral effect.   |              |                              |                       |
|---------------------------------------------------------------------------------------------------------------------------|--------------|------------------------------|-----------------------|
| Modification                                                                                                              | Success rate | Average number of iterations | Average of Rcalc/Rest |
| (A-2)                                                                                                                     | −            | +                            | +                     |
| (B-4)                                                                                                                     | 0            | ++                           | +                     |
| (C-1)                                                                                                                     | +            | ++                           | 0                     |

The results are summarized in Table VI. We first learn that approximate solutions are obtained in all the 1000 trials for all the choices of n. When n=20 for example, the Improved Amoeba TSP
algorithm requires reduced number of iterations to obtain an approximate solution as compared to the original Amoeba TSP algorithm. This high efficiency enables us to solve the TSP with n greater than 20 within reasonable computational time. Figures 2(a) and 2(b) show the n dependence of the average number of iterations and the average of Rcalc/Rest, respectively. The number of iterations grows proportionally to √n. This scaling relation is nontrivial and surprising, and it holds irrespective of the distribution pattern of distances between cities. Moreover, the average of Rcalc/Rest decreases gradually but monotonically as n increases, and is expected to be comparable to or even smaller than that for the original algorithm when n is large enough. These results indicate that the Improved algorithm is superior to the original algorithm in terms of the efficiency and certainty of the solution search.

## 7. Conclusion

To conclude, we proposed an improved computational model of the amoeba-inspired combinatorial optimization machine, named Improved Amoeba TSP model, through examining the original model proposed by Aono *et al*. First, we focused on three elements in the original model and examined how each of these elements affects the optimization performance. Appropriate modifications of these elements were found to significantly improve the optimization results. Importantly, it turned out that the volume conservation law assumed in the original model is not necessarily required to realize the high solution-search ability in contrast to our naive belief. This justifies the modification, which might release us from possible related constraints and restrictions against the physical implementation. Next, we constructed the Improved Amoeba TSP model by applying these three modifications to the original model. The proposed model indeed provides noticeably improved results in terms of the number of iterations and the route length. In particular, we found that the number of iterations scales to order √n for the number of cities n, which is significantly suppressed as compared to the scaling to order n for the original model. Our study offers the guides to enhancing the solution-search