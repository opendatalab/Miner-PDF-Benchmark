# Non-Stationary Stochastic Global Optimization Algorithms 

Jonatan Gomez . Carlos Rivera

the date of receipt and acceptance should be inserted later


#### Abstract

Gomez (2019) proposes a formal and systematic approach for characterizing stochastic global optimization algorithms. Using it, Gomez formalizes algorithms with a fixed next-population stochastic method, i.e., algorithms defined as stationary Markov processes. These are the cases of standard versions of hill-climbing, parallel hill-climbing, generational genetic, steady-state genetic, and differential evolution algorithms. This paper continues such a systematic formal approach. First, we generalize the sufficient conditions convergence lemma from stationary to non-stationary Markov processes. Second, we develop Markov kernels for some selection schemes. Finally, we formalize both simulated-annealing and evolutionary-strategies using the systematic formal approach.


Keywords Evolutionary Algorithms $\cdot$ Non-stationary Markov Kernel . Convergence Analysis $\cdot$ Evolutionary Strategies $\cdot$ Simulated Annealing $\cdot$ Selection Mechanism

Mathematics Subject Classification (2010) MSC $68 \mathrm{~T} 20 \cdot$ MSC $65 \mathrm{~K} 10$[^0]

```
Algorithm 1 Stochastic Global Optimization Algorithm - SGOAL.
\(\operatorname{SGOAL}(n)\)
\(t=0\)
\(P_{0}=\operatorname{INITPOP}(n)\)
while \(\neg \operatorname{END}\left(P_{t}, t\right)\) do
\(P_{t+1}=\operatorname{NextPop}\left(P_{t}\right)\)
\(t=t+1\)
return \(\operatorname{BEST}\left(P_{t}\right)\)
```


## 1 Introduction

This section provides a brief introduction to the systematic formalization proposed by Gomez (2019). Such systematic formalization of stochastic global optimization algorithms (SGoALs in short), is carried on Markov kernels terms. Gomez can formalize SGoALs with fixed NextPor stochastic method, i.e., SGoALs that can be characterized as stationary Markov processes. That is the case of the hill-climbing (Russell and Norvig (2009)), the parallel hillclimbing, the generational genetic (De Jong (1975); Holland (1975); Mitchell (1996)), the steady-state genetic (Goldberg and Deb (1991)), and the differential evolution (Das and Suganthan (2011); Storn and Price (1997)) algorithms. However, SGOALs such as the Simulated Annealing (Kirkpatrick et al. (1983)), Evolutionary Strategies (Beyer and Schwefel (2002)), or any algorithm using parameter control/adaptation techniques (Eiben et al. (1999)) cannot be characterized as stationary Markov processes.

### 1.1 Stochastic Global Optimization

The problem of finding a point $x^{*} \in \Omega \subseteq \Phi$ where a function $f: \Phi \rightarrow \mathbb{R}$ reaches its best/optimal value $\left(f^{*}\right)$, is considered as a global optimization problem, see equation 1. Here, $\Phi$ is the solution space, $\Omega$ is the feasible region, $x^{*}$ is the optimizer, $f$ is the objective function, and $\triangleleft$ is the optimization relation: $\triangleleft$ is $<$ if minimizing and it is $>$ if maximizing.

$$
\text { optimize }(f: \Phi \rightarrow \mathbb{R})=x^{*} \in \Omega \subseteq \Phi \mid(\forall y \in \Omega)\left(f\left(x^{*}\right) \unlhd f(y)\right)
$$

A stochastic global optimization algorithm (SGOAL) iteratively generates a (possibly) better population of candidate solutions using a stochastic operation, see algorithm $\square$ Here, INitPop : $\mathbb{N} \rightarrow \Omega^{n}$ initializes a population $P$ having size $n$, NextPop : $\Omega^{n} \rightarrow \Omega^{n}$ stochastically generates a new population from the current one, BEST : $\Omega^{n} \rightarrow \Omega$ obtains the fittest individual (see equation (2), and END : $\Omega^{n} \times \mathbb{N} \rightarrow$ Bool is a stopping condition. Notice that if there is a Markov kernel characterizing the NextPop method, the stochastic sequence $\left(P_{t}: t \geq 0\right)$ becomes a Markov process.

$$
\operatorname{BeST}(x)=x_{i} \mid \forall_{k=1}^{n} f\left(x_{i}\right) \unlhd f\left(x_{k}\right) \wedge f\left(x_{i}\right) \triangleleft \forall_{k=1}^{i-1} f\left(x_{k}\right)
$$

1.2 Markov Process

A function $K: \Omega_{1} \times \Sigma_{2} \rightarrow[0,1]$, with $\left(\Omega_{1}, \Sigma_{1}\right)$ and $\left(\Omega_{2}, \Sigma_{2}\right)$ measurable spaces, is called a (Markov) kernel if the following two conditions hold:

1. Function $K_{x, \bullet}: A \mapsto K(x, A)$ is a probability measure for each fixed $x \in \Omega_{1}$
2. Function $K_{\bullet, A}: x \mapsto K(x, A)$ is a measurable function for each fixed $A \in \Sigma_{2}$.

Gomez considers kernels having transition densities. If the transition density $K: \Omega_{1} \times \Omega_{2} \rightarrow[0,1]$ exists, then the transition kernel can be defined using equation 3

$$
K(x, A)=\int_{A} K(x, y) d y
$$

Composition of two kernels ( $K_{1}$ and $K_{2}$ ) is defined in terms of the kernel multiplication operator, see equation [4], Since the kernel multiplication is an associative operator Fristedt and Gray (1997), the ordered composition of $n$ transition kernels $K_{1}, \ldots, K_{n}$ is the product kernel $K_{n} \circ K_{n-1} \circ \ldots \circ K_{1}$.

$$
\left(K_{2} \circ K_{1}\right)(x, A)=\int K_{2}(y, A) K_{1}(x, d y)
$$

Finally, the probability to transit to some set $A \in \Sigma$ within $t$ steps when starting at state $x \in \Omega$, using kernel $K$, is given by equation [5. While the probability that such a Markov process is in set $A \in \Sigma$ at step $t \geq 0$, when $p: \Sigma \rightarrow[0,1]$ is the initial distribution of subsets, is given by equation 6 .

$$
\begin{aligned}
K^{(t)}(x, A)= \begin{cases}K(x, A) & \text { if } t=1 \\
\int_{\Omega} K^{(t-1)}(y, A) K(x, d y) & \text { if } t>1\end{cases} \\
\operatorname{Pr}\left\{X_{t} \in A\right\}= \begin{cases}p(A) & \text { if } t=0 \\
\int_{\Omega} K^{(t)}(x, A) p(d x) & \text { if } t>0\end{cases}
\end{aligned}
$$

### 1.3 Convergence

Gomez (2019) amends the convergence approach of Rudolph (1996) by defining the set of $\epsilon$-states, i.e., a set with closeness function value less than $\epsilon \in \mathbb{R}^{+}$. Let $\Omega \subseteq \Phi$ be a set, $f: \Phi \rightarrow \mathbb{R}$ be an objective function, $\epsilon>0$ be a real number, $x \in \Omega^{m}$, with $m$ the size of the population, and $d(x)=f(\operatorname{BESt}(x))-f^{*}$.

1. $x$ is an $\epsilon$-state iff $x \in \Omega_{\epsilon}^{m}=\left\{x \in \Omega^{m}: d(x)<\epsilon\right\}$,
2. $x$ is an $\bar{\epsilon}$-state (closed) iff $x \in \Omega_{\bar{\epsilon}}^{m}=\left\{x \in \Omega^{m}: d(x) \leq \epsilon\right\}$,
3. $x$ is an $\widehat{\epsilon}$-state (adherent) iff $x \in \Omega_{\hat{\epsilon}}^{m}=\left\{x \in \Omega^{m}: d(x)=\epsilon\right\}$.

Proposition 1. Let $P_{t} \in \Omega^{n}$ be the population maintained by an SGoal. A SGoal converges to the global optimum if its associated random sequence $\left(D_{t}=d\left(P_{t}\right): t \geq 0\right)$, converges completely to zero, i.e., equation $\square$ holds for every $\epsilon>0$.

$$
\lim _{t \rightarrow \infty} \sum_{i=1}^{t} \operatorname{Pr}\left\{\left|D_{t}\right|>\epsilon\right\}<\infty
$$

## 2 Generalizing the Systematic Formal Approach to Non-Stationary SGOALS

For a non-stationary (or non-homogeneous) Markov process, the transition probabilities (kernel) may change over time (Bowerman (1974)). Suppose that $K_{t}$ is the transition kernel applied at time $t>0$ of a non-stationary Markov process. Then, the transition kernel of such non-stationary Markov process at time $t$ is defined as $K^{(t)}=K_{t} \circ K_{t-1} \circ \ldots \circ K_{1}$. Clearly, we can rewrite the transition kernel of a non-stationary Markov process (equation [8) to resemble equation 5 .

$$
K^{(t)}(x, A)= \begin{cases}K_{1}(x, A) & \text { if } t=1 \\ \int_{\Omega} K^{(t-1)}(y, A) K_{t}(x, d y) & \text { if } t>1\end{cases}
$$

Now we are in the position of generalizing Lemma 71 in Gomez (2019) to non-stationary Markov processes.

Lemma 2. If for all $t \geq 1$ we have that $K_{t}\left(x, \Omega_{\epsilon}\right) \geq \delta>0$ for all $x \in \Omega_{\epsilon}^{c}$ and $K_{t}\left(x, \Omega_{\epsilon}\right)=1$ for all $x \in \Omega_{\epsilon}$, then $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq 1-(1-\delta)^{t}$ holds for $t \geq 1$.

Proof. We just rewrite the proof of Lemma 71 in Gomez (2019) (Gomez uses induction on $t$ ) but taking care of the non-stationary property of the Markov process. For $t=1$ we have that $K^{(t)}\left(x, \Omega_{\epsilon}\right)=K_{t}\left(x, \Omega_{\epsilon}\right)$ (equation (5)), so $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq \delta$ (condition lemma), therefore $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq 1-(1-\delta)^{t}(t=$ 1 and numeric operations). Here, we will use the notation (as Gomez did) $K^{(t)}\left(y, \Omega_{\epsilon}\right)=K_{y}^{(t)}\left(\Omega_{\epsilon}\right)$ to reduce the visual length of the equations.

$$
\begin{array}{ll}
K_{x}^{(t+1)}\left(\Omega_{\epsilon}\right) & \\
=\int_{\Omega} K_{y}^{(t)}\left(\Omega_{\epsilon}\right) K_{t}(x, d y) & \text { (equation 5) } \\
=\int_{\Omega_{\epsilon}} K_{y}^{(t)}\left(\Omega_{\epsilon}\right) K_{t}(x, d y)+\int_{\Omega_{\epsilon}^{c}} K_{y}^{(t)}\left(\Omega_{\epsilon}\right) K_{t}(x, d y) & \left(\Omega=\Omega_{\epsilon} \cup \Omega_{\epsilon}^{c}\right) \\
=\int_{\Omega_{\epsilon}} K_{t}(x, d y)+\int_{\Omega_{\epsilon}^{c}} K_{y}^{(t)}\left(\Omega_{\epsilon}\right) K_{t}(x, d y) & \\
=K_{t}\left(x, \Omega_{\epsilon}\right)+\int_{\Omega_{\epsilon}^{c}} K_{y}^{(t)}\left(\Omega_{\epsilon}\right) K_{t}(x, d y) & \\
& \text { (If } \left.y \in \Omega_{\epsilon}, K_{y}^{(t)}\left(\Omega_{\epsilon}\right)=1\right) \\
\geq K_{t}\left(x, \Omega_{\epsilon}\right)+\left[1-(1-\delta)^{t}\right] \int_{A_{\epsilon}^{c}} K_{t}(x, d y) & \\
\geq K_{t}\left(x, \Omega_{\epsilon}\right)+\left[1-(1-\delta)^{t}\right] K_{t}\left(x, \Omega_{\epsilon}^{c}\right) & \text { (Induction hypothesis) } \\
\geq K_{t}\left(x, \Omega_{\epsilon}\right)+K_{t}\left(x, \Omega_{\epsilon}^{c}\right)-(1-\delta)^{t} K_{t}\left(x, \Omega_{\epsilon}^{c}\right) & \\
\geq 1-(1-\delta)^{t}\left(1-K_{t}\left(x, \Omega_{\epsilon}\right)\right) & \text { (Probability) } \\
\geq 1-(1-\delta)^{t}(1-\delta) & \text { (condition lemma) } \\
\geq 1-(1-\delta)^{t+1} &
\end{array}
$$

Finally, Theorem 72 in Gomez (2019) also holds for non-stationary Markov processes. So, in order to show convergence of a non-stationary SGOAL it is sufficient to prove that the SGOAL satisfies the condition of lemma 2 .

Theorem 3. (Theorem 72 in Gomez (201g) - a corrected version of Theorem 1 in Rudolph (1996)) A SGOAL whose stochastic kernel satisfies $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq$ $1-(1-\delta)^{t}$ for all $t \geq 1$ will converge to the global optimum $\left(f^{*}\right)$ of a welldefined real-valued function $f: \Phi \rightarrow \mathbb{R}$, defined in an arbitrary space $\Omega \subseteq \Phi$, regardless of the initial distribution $p(\cdot)$.

Proof. See proof of Theorem 72 in Gomez (2019).

## 3 Selection Schemes Formalization

A Selection Scheme, is a method of selecting a group of individuals from a population (Blickle and Thiele (1996)). Many schemes define an individual selection mechanism s1: $\Omega^{\lambda} \rightarrow \Omega$, and selects a group of individuals by repeatedly applying s1. In this paper, we study the uniform, fitness proportional, tournament (Miller et al. (1995)), roulette, and ranking selection schemes:

1. A uniform scheme (UNIFORM1: $\Omega^{\lambda} \rightarrow \Omega$ ) gives to each candidate solution $i=1,2, \ldots, \lambda$, the same selection's probability $p\left(x_{i}\right)=\frac{1}{\lambda}$.
2. A fitness proportional scheme (PROportional1: $\Omega^{\lambda} \rightarrow \Omega$ ) gives to each candidate solution $i=1,2, \ldots, \lambda$, a selection's probability $p\left(x_{i}\right)$ such that $p\left(x_{i}\right)<p\left(x_{j}\right)$ if $f\left(x_{j}\right) \triangleleft f\left(x_{i}\right)$ and $p\left(x_{i}\right)=p\left(x_{j}\right)$ if $f\left(x_{i}\right)=f\left(x_{j}\right)$.
3. A tournament scheme (TOURNAMENT $1^{m}: \Omega^{\lambda} \rightarrow \Omega$ ) of size $m$ chooses $m$ individuals using a UNIFORM scheme and selects an individual from these using a ProportIONAL1 scheme, TOURNAMENT1 ${ }^{m}=$ PROPORTIONAL1 $^{\circ}$ UNIFORM $^{m}$.
4. A roulette scheme (RouletTe1: $\Omega^{\lambda} \rightarrow \Omega$ ) is a fitness proportional one where $p\left(x_{i}\right)=\frac{\text { rate }\left(x_{i}\right)}{\sum_{i=1}^{\text {rate }\left(x_{i}\right)}}$ with rate $\left(x_{i}\right)<\operatorname{rate}\left(x_{j}\right)$ if $f\left(x_{j}\right) \triangleleft f\left(x_{i}\right)$ and rate $\left(x_{i}\right)=\operatorname{rate}\left(x_{j}\right)$ if $f\left(x_{i}\right)=f\left(x_{j}\right)$. If $f\left(x_{i}\right) \geq 0$ for all $i=1,2, \ldots, \lambda$ and maximizing then rate $\left(x_{i}\right)$ can be set to $f\left(x_{i}\right)$.
5. A ranking scheme (RANKING1: $\left.\Omega^{\lambda} \rightarrow \Omega\right)$ is a roulette one with rate $\left(x_{i}\right)=$ $1+\left|\left\{x_{k}: f\left(x_{i}\right) \triangleleft f\left(x_{k}\right)\right\}\right|$.

Proposition 4. If $\mathrm{s} 1: \Omega^{\lambda} \rightarrow \Omega$ is a selection scheme with kernel $K_{\mathrm{s} 1}$ then $\mathrm{s}: \Omega^{\lambda} \rightarrow \Omega^{\mu}$ has kernel $K_{\mathrm{s}}=\circledast_{i=1}^{\mu} K_{\mathrm{s} 1}$.

Corollary 5. If $\mathrm{s} 1$ is based on a probability function then $K_{\mathrm{s}}$ is a kernel.

Corollary 6. The Uniform, Proportional, Tournament, Roulette and RANKING selection schemes have Markov kernels.

## 4 Simulated Annealing (SA)

### 4.1 Concept

The Simulated Annealing algorithm (SA) considers the idea behind the process of heating and cooling a material to recrystallize it, see algorithm [2, When the temperature decreases, the material settles into a more ordered state, and the state into which they settle is not always the same. This state tends to have low energy compared when the material is in the presence of high temperature (Simon (2013)). If we consider energy as a cost function, we can use this approach to minimize cost functions. Therefore, SA is an stochastic algorithm that works with a single-individual that generates a single candidatesolution $x$ (parent) and sets a high temperature to explore the search space. Then, some variation mechanism generates a new candidate-solution $x^{\prime}$ (child) and measures its cost. A replacement policy, that fitness function and the temperature, picks one individual between the father and the child. Finally, a process decreases the temperature looking for each new solution having less energy.

Clearly, the replacement policy in algorithm 2 (lines $6, \ldots, 11$ ) is not elitist. This allows SA to expand the search but can lead to the loss of some good candidate-solutions. In practice, it is normal to keep track of the best solution found so farSimon (2013). If this is done, the replacement policy is an elitist one.

### 4.2 Formalization

To formalize and characterize (SA), we use the approach proposed by Gomez (2019). We rewrite algorithm 2 in terms of individual non-stationary stochas-

```
Algorithm 2 Simulated Annealing Simon (2013)
SiMULATED ANNEALING
    \(T=\) initial temperature \(>0\)
    \(\alpha(T)=\) cooling function: \(\alpha(T) \in[0, T]\) for all \(T\)
    Initialize a candidate solution \(x_{0}\) to minimization problem \(f(x)\)
    while \(\neg\) TerminationCondition() do
        Generate a candidate solution \(x\)
        if \(f(x)<f\left(x_{0}\right)\)
            \(x_{0}=x\)
        else
            \(r=U[0,1]\)
            if \(r<\exp \left[\left(f\left(x_{0}\right)-f(x)\right) / T\right]\)
                \(x_{0}=x\)
        \(T=\alpha(T)\)
```

```
Algorithm 3 Simulated Annealing in terms of VR methods
\(\operatorname{NeXTPoP}_{S A}(\mathrm{x})\)
    \(x^{\prime}=\operatorname{VARIATE}_{S A}(\mathrm{x})\)
    \(x^{\prime}=\operatorname{Replace}_{S A_{T}}\left(\mathrm{x}^{\prime}, \mathrm{x}\right)\)
    UpdateParameters \((\mathrm{T})\)
    return \(x^{\prime}\)
```

tic methods, see algorithm 3 This new algorithm is in terms of VARIATIONREPLACEMENT methods. Observe that algorithms 2 and 3 are equivalents. Line 5 of algorithm 2 is the method VARIATE V $_{S A}$ (line 1) of algorithm [3) lines 6 to 11 of algorithm 2 is the method $\operatorname{ReplaCE}_{S A}$ (line 2) of algorithm (3) Finally, line 12 of algorithm 2 and method UpdateParameters (line 3) perform the same task.

Now, we concentrate on characterizing (SA) as a VR stochastic method and analyzing its convergence through non-stationary Markov kernels.

Proposition 7. If $\operatorname{Replace}_{S A}(x, x)$ is an elitist method, then it can be characterized by the Markov Kernel $R_{S A}: \Omega^{2} \times \Sigma \longrightarrow[1,0]$ defined as

$$
K_{R_{S A}}=\pi_{1} \circ s_{2}
$$

Proof. It is defined in the same way that the method of $\mathrm{R}_{H C}$ in Gomez (2019). So the proof uses the same argument that lemma 75 of Gomez (2019).

Proposition 8. if the stochastic method VARIATE $_{A S_{T}}$ can be characterized by a non-stationary Markov kernel $V_{S A_{T}}^{(t)}: \Omega \times \Sigma \longrightarrow[1,0]$ and condition of proposition $\square$ are fulfilled then method the $\mathrm{NextPop}_{S} A(x)$ can be described as a VR non-stationary Markov Kernel defined as

$$
K_{S A}^{(t)}=K_{R} \circ K_{V_{S A_{T}}}^{(t)}
$$

Proof. $K_{S A}^{(t)}$ is a kernel composition under the given conditions.

Proposition 9. if $\operatorname{Replace}_{S A}$ is an elitist method, then $\mathrm{NextPop}_{S A}$ can be characterized by an elitist non-stationary Markov kernel.

Proof. This proof uses the same argument as proposition 77 in Gomez (2019).

### 4.3 Convergence

![](https://cdn.mathpix.com/cropped/2024_05_09_0c29bb3351a13a6f2cf3g-08.jpg?height=46&width=1177&top_left_y=731&top_left_x=248)
$\operatorname{VARIATE~}_{A S_{T}}$ is optimal strictly bounded from zero then $\operatorname{NEXTPOP}_{S A}$ is optimal strictly bounded from zero.

Proof. Follows from definition 67, lemma 68, and definition 69 in Gomez (2019) and proposition 9 that establish that NEXTPoP $_{S A}$ can be characterized by an elitist kernel, and this is optimal strictly bounded from zero.

Theorem 11. SA will converge to the global optimum if $\operatorname{Replace}_{S} A$ is elitist and if VARIATE $_{A S_{T}}$ is optimal strictly bounded from zero.

Proof. Follows from corollary [10, and propositions [7, [7 and 9,

## 5 Evolutionary Strategies (es)

### 5.1 Concept

Evolutionary Strategies $(\mu / \rho+\lambda)$-ES are a type of Evolutionary Algorithms that apply mutation, recombination, and selection operators to a population of individuals Bever and Schwefel (2002), see algorithm [4 Every individual is an ES that has two parts: the candidate solution $(x)$ and the set of endogenous strategy parameters ( $s$ ) used to control the mutation operator (Bever and Schwefel (2002)). An ES randomly initializes the population, line 2 , and evolves both parts of the individual (lines 5-9) up to certain endingcondition is fulfilled (line 3). The set of endogenous parameters are exposed to evolution (lines 6 and 8) before producing a child candidate solution (line 7 and 9) to introduce variety. The new individual is a composition of a set of selected candidate solutions (line 5). ES generates a new population of $\lambda$ new individuals each generation (line 4). Finally, ES selects a final population using two possible approaches. The $(\mu+\lambda)$-ES approach that selects the best $\mu$ individuals among the $\mu$ parents and $\lambda$ children or the $(\mu, \lambda)$-ES that selects the best $\mu$ individuals from the $\lambda$ children (notice that $\lambda \geq \mu$ in this case). In this work, we study both of them.

```
Algorithm 4 Evolutionary strategies described by Bever and Schwefel (2002)
\(\operatorname{ES}(\mu / \rho+\lambda)\)
    \(g=0\)
    INITIALIZE \(\left(P_{q}^{(0)}:=\left\{\left(y_{m}^{(0)}, s_{m}^{(0)}, F\left(y_{m}^{(0)}\right)\right), m=1, \ldots, \mu\right\}\right)\)
    while \(\neg\) TERMINATIONCONDITION() do
        for \(l=1\) to \(\lambda\) do
                \(a_{l}=\operatorname{MARRIAGE}\left(P_{q}^{g}, \rho\right)\)
            \(s_{l}=\) ReCOMBINATION \(_{s}\left(a_{l}\right)\)
            \(y_{l}=\) RECOMBINATION \(_{y}\left(a_{l}\right)\)
            \(s_{l}^{\prime}=\operatorname{Mutation~}_{s}\left(s_{l}\right)\)
            \(y_{l}^{\prime}=\operatorname{Mutation}_{s}\left(y_{l}, s_{l}^{\prime}\right)\)
            \(F_{l}^{\prime}=F\left(y_{l}^{\prime}\right)\)
        \(P_{0}^{g}=\left\{\left(y_{l}^{\prime}, s_{l}^{\prime}, F_{l}^{\prime}\right), l=1, \ldots, \lambda\right\}\)
        if \((\mu, \lambda)\) then
            \(P_{q}^{g+1}=\operatorname{SeLetTion}\left(P_{0}^{g}, \mu\right)\)
        else \((\mu+\lambda)\)
        \(\mathrm{g}=\mathrm{g}+1\)
            \(P_{q}^{g+1}=\operatorname{Selection}\left(P_{0}^{g}, P_{q}^{g}, \mu\right)\)
```


### 5.2 Formalization

To formalize and characterize $(\mu / \rho+\lambda)$-ES, we rewrite algorithm 4 in terms of individual non-stationary stochastic methods, see algorithm5. This follows the approach in Gomez (2019) that express the algorithms in terms of VariationReplacement methods to study their convergence properties.

Notice that algorithms 4 and 5 are equivalents: lines 4-11 in algorithm 4 is method Variate(P) (line 1) in the NextPop method of algorithm [5, Also, lines 12-15 in algorithm 4 are line 2 in the NEXTPoP method of algorithm [5. Using this characterization, we proceed to characterize each method of algorithm 5 through non-stationary Markov kernels.

With the object of characterizing $(\mu / \rho+\lambda)$-ES we need to establish some non-stationary Markov kernels. First, we study the Variate method (line 1, method NextPop, algorithm (5).

Following definition 53 in Gomez (2019), we can express the variation method VARIATE: $\Omega^{\mu} \longrightarrow \Omega^{\lambda}$ as a joined stochastic method.

$$
\operatorname{Variate}(P)=\prod_{i=1}^{\lambda} \operatorname{NextSubPop}_{i}(P)
$$

Where NextSubPop: $\Omega^{\mu} \longrightarrow \Omega$ chooses $\rho$ individuals from the population, combines the $\rho$ individuals, generates a child and finally mutates the strategy and the child.

Proposition 12. If lines 8 and 9 of method UpdateStrategies of algorithm 5 can be characterized by non-stationary kernels $X: \mathbb{R}^{\rho} \times \mathscr{B}(\mathbb{R})^{\otimes \rho} \longrightarrow[0,1]$ and $V S^{(t)}: \mathbb{R} \times \mathscr{B}(\mathbb{R}) \longrightarrow[0,1]$ respectively. UPDATESTRATEGIES can be characterized by a non-stationary kernel $U S^{(t)}: \mathbb{R}^{\rho} \times \mathscr{B}(\mathbb{R}) \longrightarrow[0,1]$ defined as:

$$
K_{U S}^{(t)}=K_{V S}^{(t)} \circ K_{X S}
$$

```
\(\overline{\text { Algorithm } 5 \text { Evolutionary strategies algorithm - NextPop method described }}\)
in terms of VR methods
\(\mathrm{NextSubPop}_{i}(\mathrm{P})\)
1: \(a=\operatorname{PickParents}(P)\)
\(q=\operatorname{Xover}_{a}(P)\)
UpdateStrategies \(_{a}(\mathrm{~s}, i)\)
\(q^{\prime}=\operatorname{Variate}_{s}(q)\)
return \(q^{\prime}\)
UpdateStrategies \(_{a}(s, i)\)
1: \(s^{\prime}=\operatorname{XoverStrategie}_{a}(s)\)
\(2: s_{i}=\operatorname{VariateStRategie}\left(s^{\prime}\right)\)
Variate(P)
for \(i=1\) to \(\lambda\) do
    \(Q_{i}=\operatorname{NextSubPop}_{i}(P)\)
return \(Q\)
\(\mathrm{NextPop}_{\Psi}(\mathrm{P})\)
\(Q^{\prime}=\operatorname{Variate}(\mathrm{P})\)
\(Q=\operatorname{Replace} \Psi\left(\mathrm{P}, Q^{\prime}\right)\)
return \(Q\)
```

Proof. It is in terms of kernel composition, follows from definition 25 of Gomez (2019).

Proposition 13. If lines 2 and 4 of algorithm 5 can be characterized by nonstationary Markov kernels $\mathrm{XOVER}_{a}:\left(\Omega^{\rho} \times \Sigma\right) \longrightarrow[0,1]$ and VARIATE $_{s}:(\Omega \times$ $\Sigma) \longrightarrow[0,1]$ respectively, then the method NextSubPop can be characterized by the kernel NextSubPop: $\left(\Omega^{\rho} \times \Sigma\right) \longrightarrow[0,1]$ defined as the non-stationary kernel:

![](https://cdn.mathpix.com/cropped/2024_05_09_0c29bb3351a13a6f2cf3g-10.jpg?height=84&width=824&top_left_y=1540&top_left_x=422)

Proof. It is in terms of kernel composition, follows from definition 25 of Gomez $(2019)$.

Proposition 14. If NextSUbPop can be characterized by a non-stationary Markov kernel, the stochastic method VARIATE $^{(t)}$ can be characterized by a kernel $V: \Omega^{\mu} \times \Sigma^{\otimes \mu} \longrightarrow[0,1]$ defined as

$$
K_{\text {VARIATE }}^{(t)}=\left[\circledast_{i=1}^{\lambda}\left[K_{\mathrm{NEXTSUBPop}_{i}}\right]\right]
$$

Proof. It is a join stochastic method, follows from definition 55 and proposition 56 of Gomez (2019).

Proposition 15. The stochastic method $\operatorname{Replace}()_{(\mu+\lambda)}$ used in line 2 of method NextPop, can be characterized by the kernel $R_{\mu, \mu+\lambda}: \Omega^{\mu+\lambda} \times \Sigma^{\otimes \mu} \longrightarrow$ $[0,1]$ defined as $K_{R_{\mu, \mu+\lambda}}=\pi_{\{1, \ldots, \mu\}} \circ s_{\mu+\lambda, \mu+\lambda-1}$ and the stochastic method
$\operatorname{Replace}_{(\mu, \lambda)}$, can be characterized by the kernel $R_{\mu, \lambda}: \Omega^{\lambda} \times \Sigma^{\otimes \mu} \longrightarrow[0,1$ defined as $K_{R_{\mu, \lambda}}=\pi_{\{1, \ldots, \mu\}}{ }^{\circ s_{\lambda, \lambda-1}}$

Proof. $K_{R_{\mu}}$ and $K_{R_{\mu+\lambda}}$ are kernels composition. Follows from definition 25 in Gomez (2019).

![](https://cdn.mathpix.com/cropped/2024_05_09_0c29bb3351a13a6f2cf3g-11.jpg?height=49&width=1210&top_left_y=581&top_left_x=246)
ateStRategie and, VaRiates can be described by Markov kernels fulfilling the conditions of 12 and 13, evolutionary Strategies can be described by a VR kernel.

$$
K_{E S}=K_{R} \circ K_{V}
$$

where:

$$
\begin{gathered}
K_{V}=K_{\mathrm{VARIATE}} \\
K_{R}=K_{R_{\mu, \lambda}} \text { or } K_{R}=K_{R_{\mu+\lambda}}
\end{gathered}
$$

Proof. Follows from propositions 12, 13, 14 and 15 ,

### 5.3 Convergence

Proposition 17. The $\operatorname{NextPOP}_{(\mu / \rho+\lambda)-E S}$ is an elitist stochastic method that can be characterized by an elitist stochastic kernel

Proof. Let $k \in[1, \mu]$ be the index of the best individual in population $P$, then $f(B E S T(P))=f\left(P_{k}\right)$. Since $P \subseteq\{P \cup \operatorname{Variate}(P)\}$ and the method Replace is elitist. It is clear that $f(B E S T(P \cup \operatorname{Variate}(P))) \unlhd f\left(P_{k}\right)$.

Corollary 18. If conditions of proposition 12 and 13 are satisfied and VARIATEs is optimal strictly bounded from zero then the method $\mathrm{NEXTPOP}_{\mu+\lambda}$ is optimal strictly from zero.

Proof. Follows from definition 67, lemma 68, and definition 69 of Gomez (2019) and proposition 17 that establish that an elitist kernel is optimal strictly bounded from zero.

Theorem 19. $(\mu / \rho+\lambda)$-ES will converge to the global optimum if methods PickParentS and Variate $_{s}^{(t)}$ can be characterized by stationary or nonstationary Markov kernels and VARIATE is optimal strictly bounded from zero.

Proof. Follows from theorem 3 and corollary 18

## 6 Conclusion

In this paper we have generalized the conditions of convergence to the global optimum from stationary to non-stationary Markov process that are present in the work of stochastic global optimization algorithms: a systematic approach proposed by Gomez (2019). We formalize some selection schemes to generalize the theory to cover as many variations of each algorithm as possible. Also, we formalized and characterized both simulated-annealing and evolutionarystrategies using the developed theory. There, we established which conditions must be fulfilled to achieve a global convergence in both algorithms. Our future work will concentrate on using the proposed approach to formalize as many stationary and non-stationary SGoAL as possible, and extending and developing the theory for several particular methods that can be considered SGoALs.

## References

Beyer HG, Schwefel HP (2002) Evolution strategies - a comprehensive introduction. Natural Computing 1:3-52, DOI 10.1023/A:1015059928466

Blickle T, Thiele L (1996) A comparison of selection schemes used in evolutionary algorithms. Evolutionary Computation 4(4):361-394, DOI 10.1162/ evco.1996.4.4.361, URL https://doi.org/10.1162/evco.1996.4.4.361 https://doi.org/10.1162/evco.1996.4.4.361

Bowerman BL (1974) Nonstationary markov decision processes and related topics in nonstationary markov chains. PhD thesis, University of Iowa, URL https://lib.dr.iastate.edu/rtd/6327

Das S, Suganthan PN (2011) Differential evolution: A survey of the state-ofthe-art. IEEE Transactions on Evolutionary Computation 15(1):4-31, DOI $10.1109 /$ TEVC.2010.2059031

De Jong K (1975) An analysis of the Behavior of a class of genetic adaptive systems. PhD thesis, University of Michigan

Eiben AE, Hinterding R, Michalewicz Z (1999) Parameter control in evolutionary algorithms. IEEE Transactions in Evolutionary Computation 3(2):124141

Fristedt BE, Gray LF (1997) A Modern Approach to Probability Theory. Springer Science \& Business Media

Goldberg DE, Deb K (1991) A comparative analysis of selection schemes used in genetic algorithms. In: Foundations of Genetic Algorithms, Morgan Kaufmann, pp 69-93

Gomez J (2019) Stochastic global optimization algorithms: A systematic formal approach. Information Sciences 472:53 76, DOI https://doi.org/10.1016/j.ins.2018.09.021, URL http://www.sciencedirect.com/science/article/pii/S0020025517305248

Holland JH (1975) Adaptation in Natural and Artificial Systems. The University of Michigan Press

Kirkpatrick S, Gelatt CD, Vecchi MP (1983) Optimization by simulated annealing. Science 220(4598):671-680, DOI 10.1126/science.220.4598. 671, URL https://science.sciencemag.org/content/220/4598/671 https://science.sciencemag.org/content/220/4598/671.full.pdf

Miller BL, Miller BL, Goldberg DE, Goldberg DE (1995) Genetic algorithms, tournament selection, and the effects of noise. Complex Systems 9:193-212

Mitchell M (1996) An introduction to genetic algorithms. MIT Press

Rudolph G (1996) Convergence of evolutionary algorithms in general search spaces. In: In Proceedings of the Third IEEE Conference on Evolutionary Computation, IEEE Press, Piscataway (NJ, pp 50-54

Russell S, Norvig P (2009) Artificial Intelligence: A Modern Approach, 3rd edn. Prentice Hall Press, Upper Saddle River, NJ, USA

Simon D (2013) Evolutionary Optimization algorithms. Wiley

Storn R, Price K (1997) Differential evolution - a simple and efficient heuristic for global optimization over continuous spaces. J of Global Optimization 11(4):341-359, DOI 10.1023/A:1008202821328, URL https://doi.org/10.1023/A:1008202821328


[^0]:    J. Gómez

    Computer Systems Engineering

    Engineering School

    Universidad Nacional de Colombia

    E-mail: jgomezpe@unal.edu.co

    C. Rivera

    Computer Systems Engineering

    Engineering School

    Universidad Nacional de Colombia

    E-mail: cariveram@unal.edu.co

