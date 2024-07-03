# Non-Stationary Stochastic Global Optimization Algorithms

Jonatan Gomez · **Carlos Rivera**
the date of receipt and acceptance should be inserted later Abstract **Gomez (2019) proposes a formal and systematic approach for characterizing stochastic global optimization algorithms. Using it, Gomez formalizes algorithms with a fixed next-population stochastic method, i.e., algorithms**
defined as stationary Markov processes. These are the cases of standard versions of hill-climbing, parallel hill-climbing, generational genetic, steady-state genetic, and differential evolution algorithms. This paper continues such a systematic formal approach. First, we generalize the sufficient **conditions convergence lemma from stationary to non-stationary Markov processes. Second, we**
develop Markov kernels for some selection schemes. Finally, we formalize both simulated-annealing and evolutionary-strategies using the systematic formal approach.

Keywords Evolutionary Algorithms · **Non-stationary Markov Kernel** · Convergence Analysis · Evolutionary Strategies · **Simulated Annealing** ·
Selection Mechanism Mathematics Subject Classification (2010) MSC 68T20 · **MSC 65K10**
J. Gómez Computer Systems Engineering Engineering School Universidad Nacional de Colombia E-mail: jgomezpe@unal.edu.co C. Rivera Computer Systems Engineering Engineering School Universidad Nacional de Colombia E-mail: cariveram@unal.edu.co Algorithm 1 **Stochastic Global Optimization Algorithm -** SGoal.

SGoal(n)
1: t = 0 2: P0 = **InitPop**(n)
3: while ¬End(Pt , t) do 4: Pt+1 = **NextPop**( Pt )
5: t = t + 1 6: return **best**(Pt)

## 1 Introduction

This section provides a brief introduction to the systematic formalization proposed by Gomez (2019). Such systematic formalization of stochastic global optimization algorithms (SGoals **in short), is carried on Markov kernels**
terms. Gomez can formalize SGoal**s with fixed** NextPop **stochastic method,** i.e., SGoals that can be characterized as stationary Markov processes. **That**
is the case of the hill-climbing (Russell and Norvig (2009)), the parallel hillclimbing, the generational genetic (De Jong (1975); Holland (1975); Mitchell (1996)), the steady-state genetic (Goldberg and Deb (1991)), and the differential evolution (Das and Suganthan (2011); Storn and Price (1997)) algorithms.

However, SGoal**s such as the Simulated Annealing (Kirkpatrick et al. (1983)),**
Evolutionary Strategies (Beyer and Schwefel (2002)), or any algorithm using parameter control/adaptation techniques (Eiben et al. (1999)) cannot be characterized as stationary Markov processes.

## 1.1 Stochastic Global Optimization

The problem of finding a point x
∗ ∈ Ω ⊆ Φ where a function f : Φ → R **reaches**
its best/optimal value (f
∗**), is considered as a global optimization problem,**
see equation 1. Here, Φ is the solution space, Ω **is the feasible region,** x
∗**is the**
optimizer, f is the objective function, and ⊳ **is the optimization relation:** ⊳ is
< if minimizing and it is > **if maximizing.**
optimize (f : Φ → R) = x
∗ ∈ Ω ⊆ Φ | (∀y ∈ Ω) (f (x
∗) E f (y)) (1)
A stochastic global optimization algorithm (SGoal**) iteratively generates**
a (possibly) better population of candidate solutions using a stochastic operation, see algorithm 1. Here, InitPop : N → Ωn **initializes a population** P
having size n, NextPop : Ωn → Ωn **stochastically generates a new population from the current one,** Best : Ωn → Ω **obtains the fittest individual (see**
equation 2), and End : Ωn × N → Bool **is a stopping condition. Notice that if**
there is a Markov kernel characterizing the NextPop **method, the stochastic**
sequence (Pt: t ≥ 0) **becomes a Markov process.**

$$c)=x_{i}\mid\forall_{k=1}^{n}f\left(x_{i}\right)\trianglelefteq f\left(x_{i}\right)$$

Best (x) = xi| ∀n k=1f (xi) E f (xk) ∧ f (xi) ⊳ ∀
i−1 k=1f (xk) (2)
1.2 Markov Process A function K : Ω1 × Σ2 → [0, 1], with (Ω1, Σ1) and (Ω2, Σ2) **measurable**
spaces, is called a (Markov) kernel **if the following two conditions hold:**
1. Function Kx,• : A 7→ K(x, A) **is a probability measure for each fixed** x ∈ Ω1 2. Function K•,A : x 7→ K(x, A) **is a measurable function for each fixed**
A ∈ Σ2.

Gomez considers kernels having transition densities. If the transition density K : Ω1 ×Ω2 → [0, 1] **exists, then the transition kernel can be defined using**
equation 3.

$$K\left({x,A}\right)=\int_A{K\left({x,y}\right)dy}\tag{3}$$ Composition of two kernels ($K_1$ and $K_2$) is defined in terms of the kernel. 
$$({\boldsymbol{3}})$$

multiplication operator, see equation 4. Since the kernel multiplication is an associative operator Fristedt and Gray (1997), the ordered **composition of** n transition kernels K1, ..., Kn is the product kernel Kn ◦ Kn−1 ◦ **. . .** ◦ K1.

$$\left(K_{2}\circ K_{1}\right)\left(x,A\right)=\int K_{2}\left(y,A\right)K_{1}\left(x,d y\right)$$

Finally, the probability to transit to some set A ∈ Σ within t **steps when**
starting at state x ∈ Ω, using kernel K**, is given by equation 5. While the** probability that such a Markov process is in set A ∈ Σ at step t ≥ 0**, when** p : Σ → [0, 1] **is the initial distribution of subsets, is given by equation** 6.

$$K^{(t)}\left(x,A\right)=\begin{cases}K\left(x,A\right)&\text{if}t=1\\ \int\limits_{\Omega}K^{\left(t-1\right)}\left(y,A\right)K\left(x,dy\right)&\text{if}t>1\end{cases}\tag{5}$$  $$Pr\left\{X_{t}\in A\right\}=\begin{cases}p\left(A\right)&\text{if}t=0\\ \int\limits_{\Omega}K^{\left(t\right)}\left(x,A\right)p\left(dx\right)&\text{if}t>0\end{cases}\tag{6}$$

1.3 Convergence Gomez (2019) amends the convergence approach of Rudolph (1996) by defining the set of ǫ**-states, i.e., a set with closeness function value less than** ǫ ∈ R
+**. Let**
Ω ⊆ Φ be a set, f : Φ → R be an objective function, ǫ > 0 **be a real number,**
x ∈ Ωm, with m the size of the population, and d (x) = f (Best (x)) − f
∗.

1. x is an ǫ-state iff x ∈ Ωm ǫ = {x ∈ Ωm : d (x) < ǫ},
2. x is an ǫ-state (closed) iff x ∈ Ωm ǫ = {x ∈ Ωm : d (x) ≤ ǫ},
3. x is an bǫ-state (adherent) iff x ∈ Ωm bǫ = {x ∈ Ωm : d (x) = ǫ}.

Proposition 1. Let Pt ∈ Ωn *be the population maintained by an* SGoal.

A SGoal *converges to the global optimum if its associated random sequence*
(Dt = d (Pt) : t ≥ 0)*, converges completely to zero, i.e., equation 7 holds for* every ǫ > 0.

$$\operatorname*{lim}_{t\rightarrow\infty}\sum_{i=1}^{t}P r\left\{|D_{t}|>\epsilon\right\}<\infty$$
$$\left(7\right)$$

## 2 Generalizing The Systematic Formal Approach To Non-Stationary Sgoals

For a non-stationary (or non-homogeneous) Markov process, the transition probabilities (kernel) may change over time (Bowerman **(1974)). Suppose**
that Kt is the transition kernel applied at time t > 0 **of a non-stationary**
Markov process. Then, the transition kernel of such non-stationary Markov process at time t is defined as K(t) = Kt ◦ Kt−1 ◦ . . . ◦ K1**. Clearly, we can**
rewrite the transition kernel of a non-stationary Markov process (equation 8) to resemble equation 5.

$$K^{\left(t\right)}\left(x,A\right)=\begin{cases}K_{1}\left(x,A\right)&\text{if}t=1\\ \int\limits_{\Omega}K^{\left(t-1\right)}\left(y,A\right)K_{t}\left(x,dy\right)&\text{if}t>1\end{cases}\tag{8}$$

Now we are in the position of generalizing Lemma 71 in Gomez (2019) to non-stationary Markov processes.

Lemma 2. If for all t ≥ 1 *we have that* Kt (x, Ωǫ) ≥ δ > 0 *for all* x ∈ Ωc ǫ and Kt (x, Ωǫ**) = 1** for all x ∈ Ωǫ*, then* K(t)(**x, Ω**ǫ) ≥ 1 − (1 − δ)
t*holds for* t ≥ 1.

Proof. **We just rewrite the proof of Lemma 71 in Gomez (2019) (Gomez uses** induction on t**) but taking care of the non-stationary property of the Markov**
process. For t = 1 we have that K(t)(x, Ωǫ) = Kt (x, Ωǫ) **(equation 5), so** K(t)(x, Ωǫ) ≥ δ (condition lemma), therefore K(t)(**x, Ω**ǫ) ≥ 1 − (1 − δ)
t(t =
1 **and numeric operations). Here, we will use the notation (as Gomez did)**
K(t)(y, Ωǫ) = K
(t)
y (Ωǫ) to reduce the visual length of the equations.

K
(t+1)
x (Ωǫ)

![4_image_0.png](4_image_0.png)

ˆ

![4_image_1.png](4_image_1.png)

K
(t)
y (Ωǫ) Kt (x, dy) **(equation 5)**
Ac ǫ = ˆ Ωǫ K (t) y (Ωǫ) Kt (x, dy) + ˆ Ωc ǫ K (t) = ˆ Ωǫ Kt (x, dy) + ˆ Ωc ǫ K (t) = Kt (x, Ωǫ) + ˆ Ωc ǫ K (t) ≥ Kt (x, Ωǫ) + h1 − (1 − δ) ti ˆ ≥ Kt (x, Ωǫ) + h1 − (1 − δ) tiKt (x, Ωc ≥ Kt (x, Ωǫ) + Kt (x, Ωc ǫ ) − (1 − δ) t Kt (x, Ωc ǫ ) ≥ 1 − (1 − δ) t(1 − Kt (x, Ωǫ)) (Probability) ≥ 1 − (1 − δ) ≥ 1 − (1 − δ) t+1 .

Kt (x, dy) **(Induction hypothesis)**

Finally, Theorem 72 in Gomez (2019) also holds for non-stationary Markov processes. So, in order to show convergence of a non-stationary SGoal **it is** sufficient to prove that the SGoal **satisfies the condition of lemma 2.**
Theorem 3. *(Theorem 72 in Gomez (2019) - a corrected version of Theorem* 1 in Rudolph (1996)) A SGoal *whose stochastic kernel satisfies* K(t)(**x, Ω**ǫ) ≥
1 − (1 − δ)
tfor all t ≥ 1 *will converge to the global optimum (*f
∗) of a welldefined real-valued function f : Φ → R*, defined in an arbitrary space* Ω ⊆ Φ,
regardless of the initial distribution p (·). Proof. **See proof of Theorem 72 in Gomez (2019).**

## 3 Selection Schemes Formalization

A Selection Scheme**, is a method of selecting a group of individuals from** a population (Blickle and Thiele (1996)). Many schemes define an individual selection mechanism s1: Ωλ → Ω, and selects a group of individuals by repeatedly applying s1**. In this paper, we study the uniform, fitness proportional,**
tournament (Miller et al. (1995)), roulette, and ranking selection schemes:
1. A uniform **scheme (**Uniform1: Ωλ → Ω**) gives to each candidate solution**
i = 1, 2, . . . , λ, the same selection's probability p (xi) = 1λ
.

2. A fitness proportional **scheme (**Proportional1: Ωλ → Ω**) gives to**
each candidate solution i = 1, 2, . . . , λ, a selection's probability p (xi) **such**
that p (xi) < p (xj ) if f (xj ) ⊳ f (xi) and p (xi) = p (xj ) if f (xi) = f (xj ).

y (Ωǫ) Kt (**x, dy**) (Ω = Ωǫ
 $\left(\Omega=\Omega_{\epsilon}\bigcup\Omega_{\epsilon}^{c}\right)$  $\left(\text{If}y\in\Omega_{\epsilon}\text{,}K_{y}^{\left(t\right)}\left(\Omega_{\epsilon}\right)=1\right)$  $\left(\text{def kernel}\right)$  $\left(\text{Induction hypothesis}\right)$

![4_image_2.png](4_image_2.png)

y (Ωǫ) Kt (x, dy) (If y ∈ Ωǫ, K(t)
y (Ωǫ) Kt (x, dy) **(def kernel)**
ǫ) **(def kernel)**
t(1 − δ) **(condition lemma)**
3. A tournament **scheme (**Tournament1m : Ωλ → Ω) of size m **chooses** m individuals using a Uniform **scheme and selects an individual from these**
using a Proportional1 **scheme,** Tournament1m = Proportional1 ◦
Uniformm .

4. A roulette **scheme (**Roulette1: Ωλ → Ω**) is a fitness proportional one**
where p (xi) = P **rate**(xi)
λ i=1 **rate**(xi)
with rate (xi) < rate (xj ) if f (xj ) ⊳ f (xi) and rate (xi) = rate (xj ) if f (xi) = f (xj ). If f (xi) ≥ 0 for all i = 1, 2**, . . . , λ** and maximizing then rate (xi) **can be set to** f (xi).

5. A ranking **scheme (**Ranking1: Ωλ → Ω) is a roulette one with rate (xi) =
1 + |{xk : f (xi) ⊳ f (xk)}|.

Proposition 4. If s1: Ωλ → Ω is a selection scheme with kernel Ks1 *then* s: Ωλ → Ωµ *has kernel* Ks = ⊛
µ i=1Ks1.

Corollary 5. If s1 is based on a probability function then Ks *is a kernel.*
Corollary 6. The Uniform, Proportional, Tournament, Roulette and Ranking *selection schemes have Markov kernels.*

## 4 Simulated Annealing (Sa) 4.1 Concept

The Simulated Annealing algorithm (sa**) considers the idea behind the process**
of heating and cooling a material to recrystallize it, see algorithm 2. When the temperature decreases, the material settles into a more **ordered state,** and the state into which they settle is not always the same. This state tends to have low energy compared when the material is in the presence of high temperature (Simon (2013)). If we consider energy as a cost function, we can use this approach to minimize cost functions. Therefore, SA **is an stochastic**
algorithm that works with a single-individual that generates a single candidatesolution x **(parent) and sets a high temperature to explore the search space.**
Then, some variation mechanism generates a new candidate-solution x
′**(child)**
and measures its cost. A replacement policy, that fitness function and the temperature, picks one individual between the father and the child. Finally, a process decreases the temperature looking for each new solution having less energy.

Clearly, the replacement policy in algorithm 2 (lines 6,...,11) is not elitist.

This allows sa **to expand the search but can lead to the loss of some good**
candidate-solutions. In practice, it is normal to keep track of the best solution found so farSimon (2013). If this is done, the replacement policy is an elitist one. 4.2 Formalization To formalize and characterize (sa**), we use the approach proposed by Gomez**
(2019). We rewrite algorithm 2 in terms of individual non-stationary stochas-
Algorithm 2 **Simulated Annealing Simon (2013)**
Simulated annealing 1: T = **initial temperature** > 0 2: α(T) = cooling function: α(T) ∈ [0, T] **for all** T
3: Initialize a candidate solution x0 **to minimization problem** f(x)
4: while ¬**TerminationCondition**() do 5: Generate a candidate solution x 6: if f(x) < f(x0)
7: x0 = x 8: **else**
9: r = U[0, 1]
10: if **r < exp**[(f(x0) − f(x))/T]
11: x0 = x 12: T = α(T)
Algorithm 3 Simulated Annealing in terms of VR **methods**
NextPopSA(x)
1: x
′ =VariateSA(x)
2: x
′ =**Replace**SAT
(x',x)
3: UpdateParameters(T)
4: **return** x
′

tic methods, see algorithm 3. This new algorithm is in terms of Variation-Replacement **methods. Observe that algorithms 2 and 3 are equivalents.**
Line 5 of algorithm 2 is the method VariateSA **(line 1) of algorithm 3; lines 6** to 11 of algorithm 2 is the method ReplaceSA **(line 2) of algorithm 3. Finally,**
line 12 of algorithm 2 and method UpdateParameters **(line 3) perform the**
same task.

Now, we concentrate on characterizing (sa**) as a VR stochastic method**
and analyzing its convergence through non-stationary Markov kernels.

Proposition 7. If ReplaceSA(**x, x**) is an elitist method, then it can be characterized by the Markov Kernel RSA : Ω2 × Σ −→ [1, 0] *defined as* KRSA = π1 ◦ s2 (9)
Proof. It is defined in the same way that the method of RHC **in Gomez (2019).**
So the proof uses the same argument that lemma 75 of Gomez (2019).

Proposition 8. *if the stochastic method* VariateASTcan be characterized by a non-stationary Markov kernel V
(t)
SAT
: Ω × Σ −→ [1, 0] *and condition of* proposition 7 are fulfilled then method the NextPopSA(x) can be described as a VR *non-stationary Markov Kernel defined as*

$$K_{S A}^{(t)}=K_{R}\circ K_{V s A_{T}}^{(t)}$$
$$(10)^{2}$$
VSAT**(10)**
 *Proof.* $K^{(t)}_{SA}$ is a kernel composition under the given conditions. 
Proposition 9. if ReplaceSA *is an elitist method, then* NextPopSA can be characterized by an elitist non-stationary Markov kernel. Proof. **This proof uses the same argument as proposition 77 in Gomez (2019).** 4.3 Convergence Corollary 10. *if conditions of propositions 7, 8 and 9, are fulfilled and method* VariateAST*is optimal strictly bounded from zero then* NextPopSA *is optimal strictly bounded from zero.*
Proof. **Follows from definition 67, lemma 68, and definition 69 in Gomez (2019)**
and proposition 9 that establish that NextPopSA **can be characterized by an**
elitist kernel, and this is optimal strictly bounded from zero.

Theorem 11. sa *will converge to the global optimum if* ReplaceSA is elitist and if VariateAST*is optimal strictly bounded from zero.*
Proof. **Follows from corollary 10, and propositions 7, 8 and 9.**

## 5 Evolutionary Strategies (Es) 5.1 Concept

Evolutionary Strategies (µ/ρ +, λ)-es **are a type of Evolutionary Algorithms**
that apply mutation, recombination, and selection operators to a population of individuals Beyer and Schwefel (2002), see algorithm 4. Every individual is an es that has two parts: the candidate solution (x**) and the set**
of endogenous strategy parameters (s**) used to control the mutation operator**
(Beyer and Schwefel (2002)). An es **randomly initializes the population, line**
2, and evolves both parts of the individual (lines 5-9) up to certain endingcondition is fulfilled (line 3). The set of endogenous parameters are exposed to evolution (lines 6 and 8) before producing a child candidate solution (line 7 and 9) to introduce variety. The new individual is a composition of a set of selected candidate solutions (line 5). es **generates a new population of** λ new individuals each generation (line 4). Finally, es **selects a final population**
using two possible approaches. The (µ + λ)-es **approach that selects the best** µ individuals among the µ parents and λ children or the (µ,λ)-es **that selects**
the best µ individuals from the λ children (notice that λ ≥ µ **in this case). In**
this work, we study both of them.

```
Algorithm 4 Evolutionary strategies described by Beyer and Schwefel (2002)
ES(µ/ρ +, λ)
1: g = 0
2: initialize(P
           (0)
           q : = {(y
                  (0)
                  m , s
                     (0)
                     m , F(y
                          (0)
                          m )),m = 1, ..., µ})
3: while ¬TerminationCondition() do
4: for l = 1 to λ do
5: al = Marriage(P
                    g
                   q , ρ)
6: sl = Recombinations(al)
7: yl = Recombinationy(al)
8: s
       ′
        
       l = Mutations(sl)
9: y
        ′
        
        l = Mutations(yl, s
                      ′
                      
                      l
                      )
10: F
        ′
        
        l = F(y
             ′
              
             l
              )
11: P
      g
      0 = {(y
           ′
           
           l
           , s′l
             , F′
               l
                ), l = 1, ..., λ}
12: if (µ, λ) then
13: P
         g+1
         q = Selection(P
                       g
                      0
                       , µ)
14: else (µ + λ)
15: P
         g+1
         q = Selection(P
                       g
                      0
                       , Pg
                         q , µ)
16: g = g+1

```

5.2 Formalization To formalize and characterize (µ/ρ+, λ)-es**, we rewrite algorithm 4 in terms of**
individual non-stationary stochastic methods, see algorithm 5. This follows the approach in Gomez (2019) that express the algorithms in terms of VariationReplacement methods to study their convergence properties.

Notice that algorithms 4 and 5 are equivalents: lines 4-11 in **algorithm 4 is**
method Variate**(P) (line 1) in the** NextPop **method of algorithm 5. Also,**
lines 12-15 in algorithm 4 are line 2 in the NextPop **method of algorithm 5.**
Using this characterization, we proceed to characterize each method of algorithm 5 through non-stationary Markov kernels.

With the object of characterizing (µ/ρ +, λ**)-ES we need to establish some**
non-stationary Markov kernels. First, we study the Variate **method (line 1,** method NextPop**, algorithm 5).**
Following definition 53 in Gomez (2019), we can express the variation method Variate: Ωµ −→ Ωλ **as a joined stochastic method.**

## Variate(P) = Qλ I=1 Nextsubpopi(P) **(11)**

Where NextSubPop: Ωµ −→ Ω chooses ρ individuals from the population, combines the ρ **individuals, generates a child and finally mutates the**
strategy and the child.

Proposition 12. *If lines 8 and 9 of method* UpdateStrategies *of algorithm* 5 can be characterized by non-stationary kernels X : R
ρ × B(R)
⊗ρ −→ [0, 1]
and V S(t): R×B(R) −→ [0, 1] *respectively.* UpdateStrategies *can be characterized by a non-stationary kernel* US(t): R
ρ × B(R) −→ [0, 1] *defined as:*

$$K_{U S}^{(t)}=K_{V S}^{(t)}\circ K_{X S}$$

Algorithm 5 **Evolutionary strategies algorithm - NextPop method described** in terms of VR methods NextSubPopi(P)
1: a = **PickParents**(P)
2: q = **Xover**a(P) 3: UpdateStrategiesa(s, i)
4: q
′ = **Variate**s(q)
5: **return** q
′

UpdateStrategiesa(s, i)
1: s
′ = **XoverStrategie**a(s)
2: si = **VariateStrategie**(s
′
)
Variate(P)
1: for i = 1 to λ do 2: Qi = **NextSubPop**i(P)
3: **return** Q
NextPopΨ (P)
1: Q′ = Variate(P)
2: Q = ReplaceΨ (P, Q′)
3: **return** Q
Proof. It is in terms of kernel composition, follows from definition **25 of Gomez**
(2019).

Proposition 13. *If lines 2 and 4 of algorithm 5 can be characterized by nonstationary Markov kernels* Xovera : (Ωρ × Σ) −→ [0, 1] and Variates : (Ω ×
Σ) −→ [0, 1] *respectively, then the method* NextSubPop can be characterized by the kernel NextSubPop: (Ωρ ×Σ) −→ [0, 1] *defined as the non-stationary* kernel:
K**NextSubPop** = K
(t)
Variates
◦ KXOV ER ◦ π1**,...,ρ**	 ◦ KP
Proof. It is in terms of kernel composition, follows from definition **25 of Gomez** (2019).

Proposition 14. If NextSubPop can be characterized by a non-stationary Markov kernel, the stochastic method Variate(t)can be characterized by a kernel V : Ωµ × Σ⊗µ −→ [0, 1] *defined as* K
(t)
Variate = [
λ i=1[K**NextSubPop**i
]]
Proof. It is a join stochastic method, follows from definition 55 and **proposition** 56 of Gomez (2019).

Proposition 15. *The stochastic method* Replace()(µ+λ) used in line 2 of method NextPop*, can be characterized by the kernel* Rµ,µ+λ : Ωµ+λ×Σ⊗µ −→
[0, 1] *defined as* KRµ,µ+λ = π1,...,µ	 ◦ sµ+λ,µ+λ−1 and the stochastic method Replace(µ,λ)*, can be characterized by the kernel* Rµ,λ : Ωλ × Σ⊗µ −→ [0, 1 defined as KRµ,λ = π1,...,µ	 ◦ sλ,λ−1 Proof. KRµ,λ and KRµ+λ are kernels composition. Follows from definition 25 in Gomez (2019).

Corollary 16. *If methods* PickParents, XOvera, XoverStrategiea, VariateStrategie *and,* Variates can be described by Markov kernels fulfilling the conditions of 12 and 13, evolutionary Strategies can be described by a VR
kernel.

KES = KR ◦ KV
where:

$$\alpha=K_{R_{\mu+\lambda}}$$
$$(12)^{\frac{1}{2}}$$
$\blacksquare$
KV = K**Variate**

$$K_{R}=K_{R_{\mu,\lambda}}\,\,\,o r\,\,K_{R}=K_{R_{\mu+\lambda}}$$
KR = KRµ,λ or KR = KRµ+λ**(12)**
Proof. **Follows from propositions 12, 13, 14 and 15.**
5.3 Convergence Proposition 17. The NextPop(µ/ρ+λ)−ES *is an elitist stochastic method* that can be characterized by an elitist stochastic kernel Proof. Let k ∈ [1, µ] **be the index of the best individual in population** P,
then f(BEST (P)) = f(Pk). Since P ⊆ {P ∪ Variate(P)} **and the method**
Replace is elitist. It is clear that f(**BEST** (P ∪ Variate(P))) ⊳− f(Pk).

Corollary 18. *If conditions of proposition 12 and 13 are satisfied and* Variates is optimal strictly bounded from zero then the method NextPopµ+λ *is optimal* strictly from zero.

Proof. **Follows from definition 67, lemma 68, and definition 69 of Gomez (2019)** and proposition 17 that establish that an elitist kernel is optimal strictly bounded from zero.

Theorem 19. (µ/ρ + λ*)-ES will converge to the global optimum if methods* PickParents and Variate(t)
s can be characterized by stationary or nonstationary Markov kernels and Variates is optimal strictly bounded from zero.

Proof. Follows from theorem 3 and corollary 18.

## 6 Conclusion

In this paper we have generalized the conditions of convergence to the global optimum from stationary to non-stationary Markov process that are present in the work of stochastic global optimization algorithms: a systematic approach proposed by Gomez (2019). We formalize some selection schemes to generalize the theory to cover as many variations of each algorithm as possible. Also, we formalized and characterized both simulated-annealing **and evolutionarystrategies using the developed theory. There, we established which conditions**
must be fulfilled to achieve a global convergence in both algorithms. Our future work will concentrate on using the proposed approach to **formalize as**
many stationary and non-stationary SGoal **as possible, and extending and**
developing the theory for several particular methods that can be considered SGoals.

## References

Beyer HG, Schwefel HP (2002) Evolution strategies - a comprehensive introduction. Natural Computing 1:3–52, DOI 10.1023/A:1015059928466 Blickle T, Thiele L (1996) A comparison of selection schemes **used in evolutionary algorithms. Evolutionary Computation 4(4):361–394, DOI 10.1162/**
evco.1996.4.4.361, URL https://doi.org/10.1162/evco.1996.4.4.361, https://doi.org/10.1162/evco.1996.4.4.361 Bowerman BL (1974) Nonstationary markov decision processes and related topics in nonstationary markov chains. PhD thesis, University of Iowa, URL https://lib.dr.iastate.edu/rtd/6327 Das S, Suganthan PN (2011) Differential evolution: A survey of the state-ofthe-art. IEEE Transactions on Evolutionary Computation 15(1):4–31, DOI
10.1109/TEVC.2010.2059031 De Jong K (1975) An analysis of the Behavior of a class of genetic adaptive systems. PhD thesis, University of Michigan Eiben AE, Hinterding R, Michalewicz Z (1999) Parameter control in evolutionary algorithms. IEEE Transactions in Evolutionary Computation 3(2):124–
141 Fristedt BE, Gray LF (1997) A Modern Approach to Probability **Theory.**
Springer Science & Business Media Goldberg DE, Deb K (1991) A comparative analysis of selection schemes used in genetic algorithms. In: Foundations of Genetic Algorithms, Morgan Kaufmann, pp 69–93 Gomez J (2019) Stochastic global optimization algorithms:
A systematic formal approach. Information Sciences 472:53 - 76, DOI https://doi.org/10.1016/j.ins.2018.09.021, URL
http://www.sciencedirect.com/science/article/pii/S0020025517305248 Holland JH (1975) Adaptation in Natural and Artificial Systems. The University of Michigan Press Kirkpatrick S, Gelatt CD, Vecchi MP (1983) Optimization by simulated annealing. Science 220(4598):671–680, DOI 10.1126/science.220.4598.

671, URL https://science.sciencemag.org/content/220/4598/671, https://science.sciencemag.org/content/220/4598/671.full.pdf Miller BL, Miller BL, Goldberg DE, Goldberg DE (1995) Genetic algorithms, tournament selection, and the effects of noise. Complex Systems 9:193–212 Mitchell M (1996) An introduction to genetic algorithms. MIT Press Rudolph G (1996) Convergence of evolutionary algorithms in **general search**
spaces. In: In Proceedings of the Third IEEE Conference on Evolutionary Computation, IEEE Press, Piscataway (NJ, pp 50–54 Russell S, Norvig P (2009) Artificial Intelligence: A Modern **Approach, 3rd**
edn. Prentice Hall Press, Upper Saddle River, NJ, USA
Simon D (2013) Evolutionary Optimization algorithms. Wiley Storn R, Price K (1997) Differential evolution - a simple and efficient heuristic for global optimization over continuous spaces. J of Global Optimization 11(4):341–359, DOI 10.1023/A:1008202821328, URL
https://doi.org/10.1023/A:1008202821328