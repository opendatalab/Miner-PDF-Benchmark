# Computing Transition Pathways For The Study Of Rare Events Using Deep Reinforcement Learning

## Bo Lin 1 Yangzheng Zhong 1 **Weiqing Ren** 1 Abstract

Understanding the transition events between metastable states in complex systems is an important subject in the fields of computational physics, chemistry and biology. The transition pathway plays an important role in characterizing the mechanism underlying the transition, for example, in the study of conformational changes of bio-molecules. In fact, computing the transition pathway is a challenging task for complex and high-dimensional systems. In this work, we formulate the path-finding task as a cost minimization problem over a particular path space.

The cost function is adapted from the FreidlinWentzell action functional so that it is able to deal with rough potential landscapes. The path-finding problem is then solved using a actor-critic method based on the deep deterministic policy gradient algorithm (DDPG). The method incorporates the potential force of the system in the policy for generating episodes and combines physical properties of the system with the learning process for molecular systems. The exploitation and exploration nature of reinforcement learning enables the method to efficiently sample the transition events and compute the globally optimal transition pathway. We illustrate the effectiveness of the proposed method using three benchmark systems including an extended Mueller system and the Lennard-Jones system of seven particles.

## 1. Introduction

Understanding the transition events of dynamical systems is a fundamental but challenging task in many science problems, including chemical reaction, conformational changes of bio-molecules and nucleation events during phase transitions. For the system, the transition occurs by crossing a typical energy barrier separating two metastable states in the presence of random perturbations. The general disparity between the effective thermal energy and the energy barrier usually leads to a long-waiting period for the system around metastable states before a sudden transition from one state to another emerges. In this setting, we call the transition as a rare event. The major interest for the study of rare events is to compute the mechanism underlying the transition events, such as the transition pathway and transition rate. In the past, a number of research works have been devoted to developing efficient approaches for investigating the transition mechanism. Well-known methods include the transition path sampling (Bolhuis et al., 2002; Dellago et al., 2002), the string method (E et al., 2002; 2005; Ren et al., 2005; Maragliano et al., 2006; E et al., 2007), the action-based method (Olender & Elber, 1996) and the accelerated molecular dynamics (Voter, 1997). Also, the recent works in Ref. (Khoo et al., 2019; Li et al., 2019; Rotskoff et al., 2022) proposed deep learning based methods for computing the committor function, which is a central object in the transition path theory for understanding the transition mechanism (Ren et al., 2005; E & Vanden-Eijnden, 2010).

The transition pathway in the zero-temperature limit is characterized by the minimum energy path (MEP). The MEP is a path defined in the configuration space along which the tangent of the path is parallel to the potential force. Classical methods for identifying the MEP include the nudged elastic band method (Jonsson et al. ´ , 1998), the string method (E
et al., 2002; 2005; Ren et al., 2005; Maragliano et al.,
2006; E et al., 2007) and the conjugate peak refinement method (Fischer & Karplus, 1992). The Freidlin-Wentzell theory of large deviations provides a variational characterization of the most likelihood path via a path-based action functional. Based on this characterization, Ref. (E et al.,
2004; Zhou et al., 2008; Heymann & Vanden-Eijnden, 2008)
developed the minimum action methods for computing the minimum action path by minimizing the functional over a path space where the two ends of path are constrained to particular states. Also, the Onsager-Machlup functional, first introduced by Onsager and Machlup (Onsager & Machlup, 1953), was used to compute the most probable path associated with a finite-time horizon for systems at finite noise in many applications (Wang et al., 2010; Fujisaki et al., 2010; Du et al., 2021). From another perspective, one can recast the variational formulation of the transition path as a finitehorizon optimal control problem (Fleming, 1977; Grafke &
Vanden-Eijnden, 2019). The control problem was recently solved by a reinforcement learning algorithm (Guo et al.,
2024).

The situation is quite different when the potential energy surface is rough, which is the general case for practical molecular systems. In this case, the ensemble of transition paths can be characterized by a tube in the configuration space connecting the metastable states inside which the transition occurs with high probability (Ren et al., 2005). The rough potential energy surface contains numerous saddle points, most of which are separated by energy barriers comparable to or less than the thermal energy and thus do not act as bottlenecks of the transition. As a consequence, the potential force should not be straightforwardly used in the variational characterization of the transition pathway.

In this paper, we propose a deep reinforcement learning method for computing the transition pathway of the system with rough potential landscapes. We formulate the path-finding task as a cost minimization problem over a particular path space. To tackle the difficulties arising from the roughness of the potential landscape, we adapt the FreidlinWentzell functional and propose a cost function involving an effective force function. In the zero-temperature limit, the effective force simply reduces to the potential force of the system. The formulated path-finding problem is over a constrained sequence of states in the configuration space, where the optimal times slices are determined using numerical quadratures.

In recent years, the advances in reinforcement learning algorithms have made successful applications in many sequential decision making problems, including video games, robotic control and autonomous driving. A general class of reinforcement learning algorithms are based on computation of the state-action value function, such as the Deep Q Network
(DQN) algorithm (Mnih et al., 2013; 2015), the deterministic policy gradient (DPG) algorithm (Silver et al., 2014) and the deep DPG (DDPG) algorithm (Lillicrap et al., 2015). In particular, the DQN algorithm utilizes the deep neural networks as the function approximators, where target networks and replay buffer are introduced to stabilize the algorithm.

Furthermore, the DDPG algorithm combined the DQN with the actor-critic approach based on the policy gradient to adapt the algorithm to a broader case with continuous and high-dimensional action space.

In this work, we solve the formulated cost minimization problem for identifying the transition pathway using the actor-critic method based on the DDPG algorithm. The critic and actor functions are parameterized by neural networks. To target the exploration in the region of interest, the method employs a stochastic policy based on the actor function with random noise and the potential force of the system for generating episodes. Also, we utilize target networks and a replay buffer to address the possible instability issue in the learning process. For molecular systems, to enhance the learning efficiency, we incorporate physical properties of the system into the critic and actor networks.

The exploitation and exploration nature of reinforcement learning together with these techniques establish a stable and efficient algorithm for sampling transition events and computing the globally optimal transition pathway for highdimensional systems with rough potential landscapes. We demonstrate the effectiveness of the method using three numerical examples including a two-dimensional system, an extended Mueller system and the Lennard-Jones system of seven particles.

The paper is organized as follows. In Section 2, we introduce the background and the formulated path-finding problem and propose the reinforcement learning algorithm.

The numerical examples are presented in Section 3. In Section 4, we draw the conclusions.

## 2. Method

We consider a dynamical system in the configuration space R

d, which is modelled by the over-damped Langevin equation:

$$d x_{t}=-\nabla V(x_{t})d t+\sqrt{2\epsilon}d W_{t},\quad t>0\qquad(1)$$
2
where V (x) is a potential function, Wt is a standard Brownian motion and ϵ is a parameter specifying the strength of the noise which is called the temperature of the system. The equilibrium distribution of the system is known as the Boltzmann density function ρ(x) = Z
−1exp(−
1 ϵ V (x)), where Z is a normalization constant. Consider the general situation where there are two metastable states A and B for the system. A transition pathway between the two metastable states A and B is defined as a curve in configuration space connecting the two states.

For a time T > 0, we denote by C[0,T]the set of all absolute continuous functions in the configuration space over the time interval [0, T] connecting the two metastable states A and B. The Freidlin-Wentzell action functional for a given path φ ∈ C[0,T]is defined as

$$S_{T}[\varphi]=\int_{0}^{T}{\frac{1}{4}}\left|\varphi^{\prime}(t)+\nabla V(\varphi(t))\right|^{2}d t.\tag{2}$$

According to the Freidlin-Wentzell theory of large deviations (Freidlin & Wentzell, 2012), when the noise ϵ is sufficiently small, for small number δ > 0, the probability that the system (1) stays in the neighborhood of a given path φ ∈ C[0,T] over the time interval [0, T] can be estimated by

$$\mathbb{P}\left[\operatorname*{max}_{0\leqslant t\leqslant T}\|x(t)-\varphi(t)\|<\delta\right]\approx\exp\left(-{\frac{S_{T}[\varphi]}{\epsilon}}\right).$$

Therefore, in the zero-temperature limit, the most probable transition path of the system within the time horizon [0, T]
can be characterized by a minimizer of the functional (2):

$$\varphi_{T}^{*}=\operatorname*{arg\,min}_{\varphi\in\mathbb{C}_{[0,T]}}S_{T}[\varphi].$$
ST [φ]. (3)
The path φ
∗
T
is also referred to as the minimum action path. In the infinite-time limit by letting T goes to infinity, the action functional of the minimum action path, ST [φ
∗
T
],
converges to the infimum value

$$\operatorname*{inf}_{T>0}\operatorname*{inf}_{\varphi\in\mathbb{C}_{[0,T]}}S_{T}[\varphi],$$

ST [φ], (4)
where the infimum is over all times T and the corresponding path space C[0,T]. Furthermore, the graph limit of the minimum action path is a minimum energy path (MEP) of the system. The MEP is, by definition, a curve in the configuration space along which the tangent of the curve is parallel to the potential force −∇V (x).

In this work, we aim to find the transition pathway with minimal action in a path space that is close to ∪T C[0,T].

To deal with rough potential landscapes, we propose a cost function by adapting the Freidlin-Wentzell functional. Then we propose a deep reinforcement learning algorithm to solve the path-finding problem.

## 2.1. Formulation Of The Problem

For a small number γ > 0, we consider a path space Cγ consisting of continuous piecewise linear functions, whose graph is a polygonal chain connecting the two states A and B. Each path φ(t) in the space Cγ is represented by a sequence of states (z0*, . . . , z*N ) in the configuration space, together with the corresponding time points (t0*, . . . , t*N )
(See Fig. 1). The sequence (z0*, . . . , z*N ) forms a polygonal chain connecting A and B where the line segments are of equal length γ except the last one, *i.e.*

$$\begin{array}{l l}{{z_{0}=A;}}&{{z_{N}=B;}}\\ {{\gamma=\left|z_{i}-z_{i+1}\right|,\;0\leqslant i\leqslant N-2;}}\\ {{\gamma\geqslant\left|z_{N-1}-z_{N}\right|.}}\end{array}$$
$${\mathrm{(5)}}$$

Over the time interval [ti, ti+1], the path φ(t) is a straight line connecting zi and zi+1 with uniform derivatives,

$$\varphi(t)=z_{i}+\frac{z_{i+1}-z_{i}}{h_{i}}(t-t_{i}),\quad t_{i}\leqslant t\leqslant t_{i+1}$$  where the time slice $h_{i}=t_{i+1}-t_{i}$. We denote the func
where the time slice hi = ti+1 − ti. We denote the function φ i(t) = φ(t + ti) for t ∈ [0, hi]. One can show that

$$({\mathfrak{I}})$$



the set ∪γ>0Cγ is a dense subset of ∪T >0C[0,T](See Appendix A). Next, we consider the following action minimization problem restricted to the path space Cγ for computing the transition pathway of the system,

$$\inf_{\varphi\in\mathbb{C}_{\gamma}}\sum_{i=0}^{N-1}\tilde{L}(z_{i},z_{i+1};h_{i}),\quad\text{where}$$  $$\tilde{L}(z_{i},z_{i+1};h_{i})=\int_{0}^{h_{i}}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V(\varphi^{i}(t))\right|^{2}dt.\tag{6}$$  The result is the second-order-order-valued function $\varphi$ of the 
The optimization problem is, in principle, over a finite set of states (z0*, . . . , z*N ) in the configuration space subject to the constraints (5), together with the time slices
(h0*, . . . , h*N−1).

Optimal Time Slices. In the problem (6), for a particular sequence of states (z0*, . . . , z*N ), each optimal time slice h
∗ i is a minimizer to the individual integral L˜(zi, zi+1; hi).

However, it is not straightforward to obtain an analytical solution for h
∗ i in general as the integral involves the potential force. Instead, one can compute an optimal solution h
∗ i by approximating the integral L˜(zi, zi+1; hi) using a mid-point numerical quadrature,

$$\min_{h_{i}}\tilde{L}(z_{i},z_{i+1};h_{i})\approx\min_{h_{i}}h_{i}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V(z_{i+1/2})\right|^{2}$$ $$=2|z_{i+1}-z_{i}|\cdot|\nabla V(z_{i+1/2})|$$ $$\qquad+2\langle z_{i+1}-z_{i},\nabla V(z_{i+1/2})\rangle.\tag{7}$$

where the mid-point zi+1/2 = (zi + zi+1)/2 and the minimum value for L˜ is achieved at h
∗
i = |zi+1 −
zi||∇V (zi+1/2)|. We denote the minimum value in Eq. (7) by R(zi, zi+1) and refer to it as the cost between zi and zi+1. In principle, the integral L˜(zi, zi+1; hi) in Eq. (6) can be approximated using any suitable numerical quadratures (See Appendix B).

Therefore, the task of finding the optimal transition path in the space Cγ as in Eq. (6) can be formulated as a cost minimization problem over the states (z0*, . . . , z*N ):

$$\operatorname*{arg\,min}_{(z_{0},\ldots,z_{N})}\sum_{i=0}^{N-1}R(z_{i},z_{i+1}),$$
4
where the states (z0*, . . . , z*N ) representing a transition path φ(t) are subject to the constraints in Eq. (5). Effective Force. The situation is quite different when the potential energy surface is rough, which is the typical case for practical molecular systems. In this case, the rough potential energy surface may contain numerous saddle points, most of which do not act as bottleneck of the transition as potential barriers separating those saddle points are less than or comparable to the thermal energy (Ren et al., 2005). As a consequence, the Freidlin-Wentzell path functional as in Eq. (2) directly involving the potential force is no longer valid for quantifying the transition events.

For a particular line segment connecting zi and zi+1 in the path, consider the original dynamics (1) starting from the mid-point zi+1/2:

$$dx_{t}=-\nabla V(x_{t})dt+\sqrt{2\epsilon}dW_{t},\quad x_{0}=z_{i+1/2}.\tag{9}$$

For h > 0, integrating both sides of the equation over the time interval [0, h] gives

$$x_{h}=z_{i+1/2}-\int_{0}^{h}\nabla V(x_{t})d t+\xi,\quad\xi\sim\mathcal{N}(0,2\epsilon h).$$

We treat the potential force in the integral as a uniform value around the state zi+1/2 and refer to it as the effective force at zi+1/2. The formal definition of the effective force at zi+1/2 is given by

$$F_{\epsilon}(z_{i+1/2})=\mathbb{E}_{\epsilon}\left[\frac{x_{h}-x_{0}}{h}:x_{0}=z_{i+1/2}\right],\tag{10}$$  in the notation is not that we would be of the set 
where the expectation is over a state ensemble of the system at time h starting from the state zi+1/2 at the temperature ϵ.

In practice, we approximate the effective force Fϵ(zi+1/2)
using M short trajectories following the dynamics (9) over the time interval [0, h] where the state at time h for each trajectory is denoted by x e j
,

$$F_{\epsilon}(z_{i+1/2})\approx{\frac{1}{M}}\sum_{j=1}^{M}{\frac{x_{j}^{e}-z_{i+1/2}}{h}}.$$
h. (11)
We then define the cost function

$$R_{\epsilon}(z_{i},z_{i+1})=\min_{h_{i}}h_{i}\left|\frac{z_{i+1}-z_{i}}{h_{i}}-F_{\epsilon}(z_{i+1/2})\right|^{2}\tag{12}$$ $$=2|z_{i+1}-z_{i}|\cdot\left|F_{\epsilon}(z_{i+1/2})\right|$$ $$\qquad-2(z_{i+1}-z_{i})\cdot F_{\epsilon}(z_{i+1/2}).$$
$$(8)$$

Note that the cost function reduces to the Freidlin-Wentzell cost in Eq. (7) when ϵ and h tends to zero since the expectation (10) asymptotically converges to the potential force
−∇V (zi+1/2). For simplicity, we denote by R0 the zerotemperature cost function R as defined in Eq. (7). For the system with rough potential landscapes at temperature ϵ, the transition pathway connecting A and B can be computed by solving the cost minimization problem

$$\begin{array}{c}\mbox{arg\,min}\\ (z_{0},...,z_{N})\end{array}\sum_{i=0}^{N-1}R_{\epsilon}(z_{i},z_{i+1}),\tag{13}$$

where the states (z0*, . . . , z*N ) in the configuration space are subject to the constraints in Eq. (5).

## 2.2. Reinforcement Learning Method

To solve the path-finding problem in Eq. (13), we define a Markov decision process with a state space X = R
d and continuous action space A = {x ∈ R
d: |x| = 1}.

During the process, an agent interacts with the environment at discrete time steps. At each step, the agent takes an action, observes the next state and receives a running cost
(or reward). Specifically, we set the transition dynamics and cost function r(*s, a*) to be deterministic and consistent with the problem (13), *i.e.* the next state after taking action at at state st is given by st+1 = st + γ · at and the received cost is defined as rt = Rϵ(st, st+1) as in Eq. (7) for ϵ = 0 or Eq. (12) for ϵ > 0. The terminal condition is that the agent arrives in the region Ωγ = {x ∈ R
d: |x − B| < γ}.

The agent's behaviour is described by a policy π, which gives the action π(s) for each state s. For a given policy π, the return from a state st is defined as the sum of future costs, Rt = rt+*· · ·*+rT , where T denotes the terminal time of the process. Our goal is to learn a policy π
∗ which minimizes the return for each state s ∈ X . The state-action function Q(*s, a*) associated with the optimal policy π
∗is defined as the return after taking action a at s and thereafter following the policy π
∗. Many reinforcement learning algorithms for computing the function Q(*s, a*) are based on a recursive relationship known as the Bellman equation:

$$Q(s_{t},a_{t})=r(s_{t},a_{t})+\operatorname*{min}_{b\in{\mathcal{A}}}Q(s_{t+1},b).$$
$$(11)$$

To deal with the task with continuous action space, here we use an actor-critic approach based on the DDPG algorithm (Lillicrap et al., 2015). The critic function is the state-action function Q(*s, a*) which is parameterized using a neural network Q˜θ(*s, a*) : *X × A →* [0, 1],

$$Q_{\theta}(s,a)=\begin{cases}\lambda\tilde{Q}_{\theta}(s,a),&s\notin\Omega_{\gamma}\\ R_{\epsilon}(s,B),&s\in\Omega_{\gamma}\end{cases}\tag{14}$$

where λ > 0 is predefined parameter which specifies the range of the critic function as [0, λ]. The actor function µ(s) = arg mina Q(*s, a*) corresponding to the optimal policy specifies the optimal action at each state. To construct an actor network mapping states to unit vectors in R
d, we represent the actor function as a normalized vector based the cosines of a hidden actor µ˜θ : R
d → R
d,

$$\mu_{\theta}(s)=\Theta[\cos(\tilde{\mu}_{\theta}(s))],$$
µθ(s) = Θ[cos(˜µθ(s))], (15)
5
where Θ[v] = v/|v| is the normalization function with an input vector v ∈ R
d. Note that the actor function is periodic over the hidden actor µ˜θ(s) with period 2π.

Data Generation. We sample data by generating episodes where the initial states are produced from a particular distribution p(s) and subsequently the action of the agent is selected based on a stochastic policy. To facilitate the exploration of possible transition pathways, we add noise to the hidden actor function µ˜θ in the selection of action. Meanwhile, we aim to target the exploration in the region of interest which excludes states in the configuration space with low equilibrium densities ρ(x). Thus, we take the action conducted at step t as at = Θ[˜at], where

$$\tilde{a}_{t}=\begin{cases}\cos(\tilde{\mu}_{\theta}(s_{t})),&\text{with probability}p_{1}\\ -\nabla V(s_{t}),&\text{with probability}p_{2}\\ \cos(\tilde{\mu}_{\theta}(s_{t})+\xi_{t}),&\text{with probability}1-p_{1}-p_{2}\end{cases}\tag{16}$$  where $\xi_{t}\in\mathbb{R}^{d}$ is sampled from a Gaussian distribution and 
p1 ⩾ 0, p2 ⩾ 0, 1 − p1 − p2 ⩾ 0.
We use a replay buffer R with fixed size NR to store the sampled transitions, where the oldest ones will be discarded when new samples are appended to the buffer. The critic function Q(*s, a*) can be learned off-policy, allowing us to maintain a large-size replay buffer and sample a mini-batch from the buffer for training neural networks at each step.

Policy Evaluation. Target neural networks are often employed in reinforcement learning algorithms to address the instability issue when nonlinear and large scale neural networks are used. Here we duplicate the critic and actor networks as the target networks Q′θ
(*s, a*), µ
′ θ
(s) each time after a particular number of steps. The target networks will be used to compute the target values in the temporal-difference
(TD) loss function for training the critic network,

$$L_{Q}(\theta)=\frac{1}{|\mathcal{B}|}\sum_{(s_{t},a_{t},r_{t},s_{t+1})\in\mathcal{B}}\left|Q_{\theta}(s_{t},a_{t})-y_{t}\right|^{2},\tag{17}$$ $$y_{t}=r_{t}+Q_{\theta}^{\prime}(s_{t+1},\mu_{\theta}^{\prime}(s_{t+1})).$$

Here we use the stochastic gradient descent to train the neural networks, and B = {(st, at, rt, st+1)} is a batch of transitions sampled from the replay buffer.

Policy Gradient. The actor network is trained using the gradient of an average return Jµ over the batch states with

Algorithm 1 Reinforcement learning for computing the
optimal transition pathway at temperature ϵ.
Initialize critic and actor networks Qθ(*s, a*) and µθ(s).
Initialize target networks: Q′θ ← Qθ, µ
′
θ ← µθ, and initialize replay buffer R.
for step = 1 to *maxstep* do
Sample initial state s0 from distribution p(s).
for t = 0 to *maxtime* do
Select action at according to policy (16);
Update new state st+1 = st + γ · at;
Sample M trajectories starting from st+1/2 =
1
$\frac{1}{2}(s_{t}^{i}+s_{t+1})$ with time $n$ and estimate $T_{e}(s_{t+1}^{i})$ as in Eq. (11);  Compute cost $r_{t}=R_{e}(s_{t},s_{t+1})$;  Store $(s_{t},a_{t},r_{t},s_{t+1})$ in $\mathcal{R}$;  Sample a batch $\mathcal{B}=\{(s_{t}^{i},a_{t}^{i},r_{t}^{i},s_{t+1}^{i})\}$ from $\mathcal{R}$;  Compute target values  $$y_{t}^{i}=r_{t}^{i}+Q_{\theta}^{\prime}(s_{t+1}^{i},\mu_{\theta}^{\prime}(s_{t+1}^{i}));$$
(st + st+1) with time h and estimate Fϵ(st+1/2)
$$y_{t}^{i}=r_{t}^{i}+Q_{\theta}^{\prime}(s_{t+1}^{i},\mu_{\theta}^{\prime}(s_{t+1}^{i}));$$
Update critic Qθ using the loss function (17); Update actor µθ using the sampled policy gradients
in Eq. (18);
Exit if terminal condition st+1 ∈ Ωγ is met.
  **end**  **if** $\mbox{mod}(step,step_{0})=0$**then**  $\mid$ Update target networks $Q_{\theta}^{\prime}\gets Q_{\theta}$, $\mu_{\theta}^{\prime}\gets\mu_{\theta}$.  **end**
end
Output: The critic and actor functions Qθ(*s, a*), µθ(s).

respect to the actor parameters by applying the chain rule,

$$\nabla_{\theta}J_{\mu}=\frac{1}{|\mathcal{B}|}\sum_{s_{t}\in\mathcal{B}}\nabla_{a}Q_{\theta}(s_{t},a)|_{a=\mu_{\theta}(s_{t})}\cdot\nabla\mu_{\theta}(s_{t}).\tag{18}$$

Physics-based Learning. General molecular systems are usually invariant to certain transformations of the system, such as translation, rotation of the configuration and reindexing of particles of the same species in the system. The physical properties can be described by a transformation function x
′ = T (x) mapping a given configuration x and its equivalent ones to a representative configuration x
′. We make the learning process respect the physical properties. In the critic and actor networks, the state-action input (*s, a*) is transformed into (s
′, a′) by T before fed into the network.

For the actor network, we restore the output a˜ ∈ A to a˜
′ ∈
A by the inverse of T , where A denotes the action space.

Learning over an effective manifold of the configuration space can enhance the efficiency of the algorithm.

A pseudocode for describing the reinforcement learning algorithm is presented in Algorithm 1. Once the actor network is trained, one can compute a transition pathway with states
{zt}0⩽t⩽T by performing the iterative procedure:

$$z_{t+1}=z_{t}+\gamma\cdot\mu_{\theta}(z_{t}),\;t\geq0;\quad z_{0}=A$$

until the terminal condition zT −1 ∈ Ωγ is satisfied and we set zT = B.

Remark 1: The proposed method is able to compute the globally optimal transition pathway. Traditional methods for computing the transition pathway including the nudged elastic band method (Jonsson et al. ´ , *1998), the* string method (E et al., 2002; 2007) and the minimum action method (E et al., 2004; *Heymann & Vanden-Eijnden,*
2008) are suffering from the issue of metastability, as they are performing an iterative procedure in the path space starting from a particular path. The solution relies on the initial guess of path. In the general case with multiple transition pathways (for example, in conformational changes of bio-molecules), suitable initial guess is usually not straightforwardly available. In this case, these methods may get trapped in the neighborhood of a locally optimal solution and produce a path that is far away from the globally optimal one. On the other hand, as in the stochastic policy (16), the proposed reinforcement learning algorithm is able to explore the entire configuration space due to the randomness term and focus on the transition region of interest based on the optimal policy introduced by the actor function. The exploration-exploitation balance makes the proposed method able to compute the globally optimal path in the whole configuration space.

Remark 2: There are a number of reinforcement learning algorithms developed recently with substantial improvements over the DDPG algorithm, such as the twin delayed deep deterministic policy gradient algorithm (TD3) (Fujimoto et al., *2018) and the soft actor-critic algorithm (Haarnoja* et al., *2018). In this work, we propose a framework of formulating the path-finding problem for dynamical systems* and employing RL algorithms to solve the problem. Besides the basic DDPG algorithm, the proposed method enjoys the flexibility of combining with advanced techniques from other RL algorithms, for instance, twin Q-functions and target policy smoothing in TD3, to improve the performance of the method. This might be helpful in specific implementations and will be tested in future works.

## 3. Numerical Examples

To illustrate the effectiveness of the proposed method, we apply Algorithm 1 to three benchmark systems including a two-dimensional system, a ten-dimensional system with an extended Mueller potential and the Lennard-Jones system of seven particles. The first system is adapted from Ref. (E
et al., 2007) which exhibits two typical transition pathways connecting the metastable states. The latter two systems have been extensively studied in previous works (Khoo et al., 2019; Li et al., 2019; Dellago et al., 1998; Evans et al.,
2023). To validate the accuracy of the computed transition pathway, one can compute a reference solution of the transition pathway using the string method or transition tube by constructing the committor function landscape. Thus, the three examples can be used to benchmark the proposed method.

We parameterize the critic and actor functions using fullyconnected neural networks with two hidden layers and put the hyperbolic tangent function (tanh) as the activation unit in the network. In the critic network Q˜θ, as specified in Eq. (14), we put a sigmoid function on the output layer and set λ = 1000. In the hidden actor µ˜θ as in Eq. (15), there is no activation function acting on the output layer.

In the three examples, we generate episodes in parallel with initial states sampled from a mixed distribution. Specifically, 30% of the initial states are taken as the metastable state A while the remaining are sampled from the equilibrium distribution of the system at a particular temperature ϵ
′. The latter part of initial states are collected by simulating the Langevin equation (1) of the system. In the exploration policy (16), we take p1 = 1/3, p2 = 1/3 and ξt is sampled from the Gaussian distribution N (0*, π/*4). The neural networks are trained using the stochastic gradient descent with the Adam optimizer (Kingma & Ba, 2015) and batch size 5000. With a batch of data points sampled from the replay buffer, we train the critic and actor networks repeatedly for 10 times using the temporal-difference loss function (17)
and the sampled policy gradient in Eq. (18), respectively.

The target networks are updated every 10 training steps. The parameters in Algorithm 1 used for the three examples are shown in the table in Appendix C.

## 3.1. A Two-Dimensional System

To illustrate the ability of the method for predicting the globally optimal transition pathway, we first consider a twodimensional (2D) system with two typical transition pathways. The potential function of the system, as adapted from Ref. (E et al., 2007), is given by

$$V(x,y)=\left[(1-x^{2}-y^{2})^{2}+\frac{y^{2}}{x^{2}+y^{2}}\right](1+g(y)),\tag{19}$$  when $g(y)=1/(1+\exp(-y))$ denotes the sigmoid function.  
where g(y) = 1/(1 + exp(−y)) denotes the sigmoid function. For the system, there are two metastable states at A = (−1, 0) and B = (1, 0), corresponding to two local minima of the potential V .

The system has two minimum energy paths (MEP) connecting A and B. We first compute reference solutions for the two paths using the string method (E et al., 2007). The string is represented by 501 points in the 2D plane. We perform the string method twice, in which the initial strings are taken



as straight lines connecting the two points (−0.5, 0.5) and
(0.5, 0.5) and connecting (−0.5, −0.5) and (0.5, −0.5), respectively. Plots of the two computed MEPs are shown in the upper panel of Fig. 2, which resemble upper/lower semicircles connecting A and B in the 2D plane. For convenience, we refer to the two curves as upper/lower MEPs.

Also shown in the lower panel of Fig. 2 is the potential energy (19) of the system along the two paths, from which one can observe that the upper MEP has a energy barrier of ∆V ≃ 2, whereas lower MEP has a barrier of ∆V ≃ 1.

Therefore, the lower MEP is the globally optimal transition pathway between A and B, especially when the magnitude of noise is much less than 1, *i.e.* ϵ ≪ 1.

With the lower MEP, denoted by φ, one can quantitatively evaluate the path φθ computed by the proposed method.

Note that φ is parameterized by the normalized arc-length α of the path. We first re-parameterize φθ with its normalized arc-length and then evaluate φθ using the relative error:

$$e_{\varphi}=\frac{\|\varphi_{\theta}(\alpha)-\varphi(\alpha)\|}{\|\varphi(\alpha)\|},\tag{20}$$
where the norm is defined as $\|\phi(\alpha)\|=\sqrt{\frac{1}{n_{e}}\sum_{i=1}^{n_{e}}|\phi(i/n_{e})|^{2}}$ for a function $\phi$ using $n_{e}=100$ discrete points.  
We apply Algorithm 1 with 700 training steps to compute the transition pathway, in 20 independent runs with random initialization on the critic and actor networks. In the path-finding problem (13), we take the path space Cγ with γ = 0.1 and set ϵ = 0. All of the computed paths using the proposed method are close to the lower MEP, as shown in the upper panel of Fig. 2. The lower panel of the figure shows the potential function along the computed path, which agrees well with the potential along the lower MEP. The statistics of relative error for the paths defined in Eq. (20) in the 20 runs is eφ = 0.0060±0.0020. The results demonstrate the accuracy of the methods for computing the transition pathway.

As a comparison, we also apply the string method with random initialization to the system in 20 independent runs. On each run, the initial string is taken as a straight line randomly sampled on the 2D plane. Specifically, one end point xa of the line is sampled from U ([−1.5, 0) × [−1.5, 1.5]) and the other end point xb is sampled from U ((0, 1.5] × [−1.5, 1.5]), where U(·) indicates the uniform distribution. In the total 20 runs, the string method is convergent to the lower MEP for 11 runs and to the upper MEP for the remaining runs. The results demonstrate that the proposed method statistically outperforms the string method for computing the globally optimal transition pathway.

## 3.2. Extended Mueller System

To illustrate the effectiveness of the method for dealing with high-dimensional systems and rough energy landscapes, we consider the Mueller potential embedded in the tendimensional space,

$$V(x)=V_{m}(x_{1},x_{2})+{\frac{1}{2\sigma^{2}}}\sum_{i=3}^{10}x_{i}^{2},\quad x\in\mathbb{R}^{10}\quad{\mathrm{(21)}}$$



where Vm(x1, x2) is the Mueller potential for the first two dimensions,

$$V_{m}(x_{1},x_{2})=\sum_{i=1}^{4}D_{i}\exp[a_{i}(x_{1}-X_{i})^{2}$$ $$+b_{i}(x_{1}-X_{i})(x_{2}-Y_{i})+c_{i}(x_{2}-Y_{i})^{2}]$$ $$+\omega\sin(2k\pi x_{1})\sin(2k\pi x_{2}),$$

and another 8 harmonic functions are added for the remaining dimensions with the parameter σ specifying the strength of the harmonic terms. The parameters ω and k control the roughness of the potential landscape. We take the two metastable states as A = (−0.558, 1.441, 0*, . . . ,* 0) and B = (0.623, 0.028, 0*, . . . ,* 0), which corresponds to two local minimum points of the potential function V (x). In this example, we take the parameters except ω, k from Ref. (Li et al., 2019) and consider two cases for the potential function (21) with different values of ω. In the first case
(ω = 0), the potential landscape is smooth and we apply the method to compute the transition pathway for the system in the zero-temperature limit. In the second case (ω >
0), the potential landscape is rather rugged with numerous saddle points and we compute the transition pathway at the temperature ϵ = 10.

Smooth Mueller Potential. In the first case, we set the parameter ω = 0. For the example, we compute the optimal transition pathway in the path space Cγ with γ = 0.1 and apply Algorithm 1 to solve the problem (13) with ϵ = 0.

In the algorithm, we conduct 1000 training steps; at each step, we generate episodes according to the exploration policy (16) and train the critic and actor networks.



In Fig. 3, we plot the transition pathway φθ computed from the actor network µθ(s), which is projected on the (x1, x2)
plane. Also shown is the minimum energy path φ computed using the string method (E et al., 2007). The inset plot in Fig. 3 shows the potential function along the two paths. In Fig. 3, one can observe that the two paths are almost indistinguishable to each other and the method accurately predicts the potential barrier separating the two metastable states via the computed transition pathway. With φ, the relative error for φθ as defined in Eq. (20) under 10 independent runs is eφ = 0.0203 ± 0.0061. The results demonstrate the accuracy of the proposed reinforcement learning algorithm for predicting the transition pathway of high-dimensional systems.

In Fig. 4, we show plots of the temporal-difference loss function LQ and the average return Jµ over the whole replay buffer versus the training step. Also, we show the performance of the actor network, *i.e.* the relative error for φθ,



shown in Fig. 7. We validate the solution using a transi-
versus the training steps in Fig. 5. From the figures, one can observe that the two losses and error are all convergent to low values after about 400 training steps, which indicates the stability of the algorithm for the system.  A scatter plot of the states { s i } in the replay buffer, projected on the ( x 1 , x 2 ) plane, at the last training step of the algorithm is shown in Fig. 6, together with two generated episodes starting from the state A . We observe that the generated data points cluster around the minimum energy path (MEP) as shown in Fig. 3 , with adequate sampling densities everywhere along the path, and the two episodes are guided towards the state B along the MEP with exploration randomness. The results demonstrate that the proposed method is capable of exploring the region regarding transition and sampling transition events efficiently.

Rugged Mueller Potential. In the second case, we set the parameters ω = 9, k = 5 and apply Algorithm 1 to compute the optimal transition pathway at ε = 10. The tion tube of the system inside which the transition occurs with high probability (Ren et al., 2005 ).  Specifically, we compute the transition tube at ε = 10 by mapping a committor function landscape of the system (See Appendix D).

As observed from Fig. 7 , the computed transition pathway locates near the center of the transition tube, which demonstrates the proposed method is able to predict the transition pathway for high-dimensional systems with rough potential landscapes.

## 3.3. Lennard-Jones System

To illustrate the ability of the algorithm to deal with molecular systems, we apply the method to study a rearrangement process of the Lennard-Jones system, which is a cluster of seven particles on the plane. The system is relatively simple but serves as a good example to benchmark the proposed method.

In the system, the particles are interacting via the Lennard-
Jones potential function

$$V(y_{1},\ldots,y_{7})=\sum_{i<j}4\epsilon_{0}\left[\left(\frac{\sigma_{0}}{r_{i j}}\right)^{12}-\left(\frac{\sigma_{0}}{r_{i j}}\right)^{6}\right],\tag{22}$$





where (y1*, . . . , y*7) denotes the position-vector of the seven particles, rij = |yi − yj | is the Euclidean distance between particle i and particle j and ϵ0, σ0 specify the energy unit and distance unit in the potential function, respectively. In this example, we take ϵ0 = 1 and σ0 = 1. In a typical equilibrium state which minimizes the potential (22), the cluster of seven particles forms a hexagon. For the system, we are interested in studying the rearrangement process where a particular particle is escaping from the center of the cluster to its surface (Dellago et al., 1998; E et al., 2002). Specifically, we look at particle 1 as the migrating particle during the process. Fig. 8 displays two typical stable configurations of the cluster corresponding to the transition process.

We next apply Algorithm 1 to the system for computing a pathway for the transition.

As indicated by the bond-based potential function in Eq. (22), the system is equivalent to any rotation or translation of the cluster, as well as re-indexing of the particles in the system. Based on the properties, we construct a transformation function T (x) which maps a given configuration x and its equivalent ones to a representative configuration.

We incorporate T (x) into the critic and actor networks to make the learning process reflect the physical properties.

The details could be found in Appendix E.

In the example, we solve the path-finding problem (13) over the path space Cγ with γ = 0.2 at the temperature ϵ = 0.

We use the the reinforcement learning algorithm 1 to solve the problem by generating episodes using the policy (16)
and training the critic and actor networks.

The identified transition pathway as computed from the actor network µθ(s) is shown in Fig. 9. The results agree well with one transition pathway identified in Ref. (Dellago et al., 1998), which demonstrates that our method is able to predict the transition pathway for the cluster of particles.

## 4. Conclusions

In this work, we proposed a deep reinforcement learning algorithm for computing the transition pathway between the metastable states of dynamical systems. It was demonstrated that the proposed method is able to sample the transition events efficiently and thus to predict the globally optimal transition pathway. We illustrated the ability of the method using three model systems.

The proposed method provides a new perspective for investigating the transition mechanism of systems with rough potential energy surfaces. In the future works, we intend to apply the method to more complex systems. Another direction for future works is to consider the generalized task of predicting the transition pathway for systems with varying or unseen parameters.

## Acknowledgement

The work of B. Lin and W. Ren is partially supported by A*STAR under its AME Programmatic programme: Explainable Physics-based AI for Engineering Modelling &
Design (ePAI) [Award No. A20H5b0142].

## References

Bolhuis, P. G., Chandler, D., Dellago, C., and Geissler, P. L.

Transition path sampling: Throwing ropes over rough mountain passes, in the dark. *Annu. Rev. Phys. Chem.*, 53
(1):291–318, 2002.

Dellago, C., Bolhuis, P. G., and Chandler, D. Efficient transition path sampling: Application to lennard-jones cluster rearrangements. *J. Chem. Phys.*, 108(22):9236–
9245, 1998.

Dellago, C., Bolhuis, P. G., and Geissler, P. L. Transition path sampling. *Adv. Chem. Phys.*, 123:1–78, 2002.

Du, Q., Li, T., Li, X., and Ren, W. The graph limit of the minimizer of the onsager-machlup functional and its
computation. *Science China Mathematics*, 64:239–280, 2021.

E, W. and Vanden-Eijnden, E. Transition-path theory and path-finding algorithms for the study of rare events. Annu.

Rev. Phys. Chem., 61:391–420, 2010.

E, W., Ren, W., and Vanden-Eijnden, E. String method for the study of rare events. *Phys. Rev. B*, 66(5):052301, 2002.

E, W., Ren, W., and Vanden-Eijnden, E. Minimum action method for the study of rare events. Commun. Pure Appl.

Math., 57(5):637–656, 2004.
E, W., Ren, W., and Vanden-Eijnden, E. Finite temperature string method for the study of rare events. J. Phys. Chem.

B, 109(14):6688–6693, 2005.

E, W., Ren, W., and Vanden-Eijnden, E. Simplified and improved string method for computing the minimum energy paths in barrier-crossing events. *J. Chem. Phys.*, 126(16),
2007.

Evans, L., Cameron, M. K., and Tiwary, P. Computing committors in collective variables via mahalanobis diffusion maps. *Applied and Computational Harmonic Analysis*,
64:62–101, 2023.

Fischer, S. and Karplus, M. Conjugate peak refinement:
an algorithm for finding reaction paths and accurate transition states in systems with many degrees of freedom.

Chem. Phys. Lett., 194(3):252–261, 1992.

Fleming, W. H. Exit probabilities and optimal stochastic control. *Applied Mathematics and Optimization*, 4:329–
346, 1977.

Freidlin, M. I. and Wentzell, A. D. Random Perturbations of Dynamical Systems. Springer Press, Berlin, Heidelberg, 2012.

Fujimoto, S., Hoof, H., and Meger, D. Addressing function approximation error in actor-critic methods. In Proceedings of the 35th International Conference on Machine Learning, volume 80, pp. 1587–1596. PMLR, 2018.

Fujisaki, H., Shiga, M., and Kidera, A. Onsager–machlup action-based path sampling and its combination with replica exchange for diffusive and multiple pathways.

J. Chem. Phys., 132(13), 2010.

Grafke, T. and Vanden-Eijnden, E. Numerical computation of rare events via large deviation theory. Chaos: An Interdisciplinary Journal of Nonlinear Science, 29(6),
2019.

Guo, J., Gao, T., Zhang, P., Han, J., and Duan, J. Deep reinforcement learning in finite-horizon to explore the most probable transition pathway. *Physica D: Nonlinear* Phenomena, 458:133955, 2024.

Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In *Proceedings of* the 35th International Conference on Machine Learning, volume 80, pp. 1861–1870. PMLR, 2018.

Heymann, M. and Vanden-Eijnden, E. The geometric minimum action method: A least action principle on the space of curves. *Commun. Pure Appl. Math.*, 61(8):1052–1117, 2008.

Jonsson, H., Mills, G., and Jacobsen, K. W. Nudged elastic ´
band method for finding minimum energy paths of transitions. In Classical and quantum dynamics in condensed phase simulations, pp. 385–404. World Scientific, 1998.

Khoo, Y., Lu, J., and Ying, L. Solving for high-dimensional committor functions using artificial neural networks. *Research in the Mathematical Sciences*, 6:1–13, 2019.

Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. In *Proceedings of the 3rd International* Conference on Learning Representations, 2015.
Li, Q., Lin, B., and Ren, W. Computing committor functions for the study of rare events using deep learning. J. Chem.

Phys., 151(5), 2019.

Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D. Continuous control with deep reinforcement learning. *arXiv preprint* arXiv:1509.02971, 2015.

Maragliano, L., Fischer, A., Vanden-Eijnden, E., and Ciccotti, G. String method in collective variables: Minimum free energy paths and isocommittor surfacesg. *J. Chem.*
Phys., 125(2), 2006.

Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A.,
Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. *arXiv preprint* arXiv:1312.5602, 2013.

Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., Graves, A., Riedmiller, M.,
Fidjeland, A. K., Ostrovski, G., Petersen, S., Beattie, C.,
Sadik, A., Antonoglou, I., King, H., Kumaran, D., Wierstra, D., Legg, S., and Hassabis, D. Human-level control through deep reinforcement learning. *Nature*, 518(7540): 529–533, 2015.

Olender, R. and Elber, R. Calculation of classical trajectories with a very large time step: Formalism and numerical examples. *J. Chem. Phys.*, 105(20):9299–9315, 1996.

Onsager, L. and Machlup, S. Fluctuations and irreversible processes. *Physical Review*, 91(6):1505, 1953.

Ren, W., Vanden-Eijnden, E., Maragakis, P., and E, W. Transition pathways in complex systems: Application of the finite-temperature string method to the alanine dipeptide.

J. Chem. Phys., 123(13):6688–6693, 2005.

Rotskoff, G. M., Mitchell, A. R., and Vanden-Eijnden, E.

Active importance sampling for variational objectives dominated by rare events: Consequences for optimization and generalization. In *Mathematical and Scientific* Machine Learning, pp. 757–780, 2022.

Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., and Riedmiller, M. Deterministic policy gradient algorithms.

In Proceedings of the 31st International Conference on Machine Learning, volume 32, pp. 387–395, 2014.

Voter, A. F. Hyperdynamics: Accelerated molecular dynamics of infrequent events. *Phys. Rev. Lett.*, 78(20):3908, 1997.

Wang, J., Zhang, K., and Wang, E. Kinetic paths, time scale, and underlying landscapes: A path integral framework to study global natures of nonequilibrium systems and networks. *J. Chem. Phys.*, 133(12), 2010.

Zhou, X., Ren, W., and E, W. Adaptive minimum action method for the study of rare events. *J. Chem. Phys.*, 128
(10), 2008.

## A. The Path Space Cγ.

Theorem A.1. The set Sγ>0 Cγ is a dense subset of ST >0 C[0,T].

Proof. For a path φ(t) in Sγ>0 Cγ which is continuous and represented by a finite number of line segments, one can easily see that the path is absolute continuous. Thus, Sγ>0 Cγ is a subset of ST >0 C[0,T].

Suppose φ(t) ∈ C[0,T]for a number T > 0. Given ϵ > 0, we shall prove that there exists γ > 0 and a ψ(t) ∈ Cγ such that max t∈[0,T]
|ψ(t) − φ(t)| < 3ϵ. (23)
In the following, when we consider a polygonal curve, we assume the time derivative of the curve on each line segment is constant.

Since φ is absolute continuous, it is uniformly continuous. Thus, there exists δ > 0 such that |φ(t1) − φ(t2)| < ϵ, ∀ |t1 − t2| *< δ.* (24)
Let 0 = t0 < t1 < · · · < tn = T such that |ti − ti−1| < δ and φ(ti−1) ̸= φ(ti) for 1 ⩽ i ⩽ n. Then |φ(ti) − φ(ti−1)| < ϵ for 1 ⩽ i ⩽ n.

We first construct a polygonal curve ψ0(t), 0 ⩽ t ⩽ T such that

$\leq i\leq p$, Then $|\varphi(t_i)-\varphi|$. 
$$\operatorname*{max}_{t\in[0,T]}|\psi_{0}(t)-\varphi(t)|<2\epsilon.$$
$\eqref{eq:walpha}$. 
|ψ0(t) − φ(t)| < 2ϵ. (25)
Let ψ0(t) be a polygonal curve with vertices at the times {ti}0⩽i⩽n and

),   $0\leqslant i\leqslant$

ψ0(ti) = φ(ti), 0 ⩽ i ⩽ n. (26)
Then for arbitrary time interval [ti−1, ti] and t ∈ [ti−1, ti], we have

|ψ0(t) − φ(t)| ⩽ |ψ0(t) − ψ0(ti−1)| + |ψ0(ti−1) − φ(ti−1)| + |φ(ti−1) − φ(t)|
$$=|\psi_{0}(t)-\psi_{0}(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|$$ $$\leq|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|$$ $$=|\varphi(t_{i})-\varphi(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|$$ $$\leq2\epsilon.$$
The last inequality is due to the uniform continuity (24) of φ. Hence, we have proved the inequality (25).

Next, we construct a polygonal curve ψ(t), 0 ⩽ t ⩽ T with line segments of uniform length such that max t∈[0,T]
|ψ(t) − ψ0(t)| *< ϵ.* (27)
Denote the length of line segments in ψ0 by

$$\gamma_{i}=|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|,\quad1\leqslant i\leqslant n$$

and the minimum length by
$$\gamma=\operatorname*{min}_{1\leqslant i\leqslant n}|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|.$$
|ψ0(ti) − ψ0(ti−1)|. (28)
Since γi = |φ(ti) − φ(ti−1)| > 0, we have γ > 0. By the definition (26) of ψ0 and the uniform continuity (24) of φ, we have *γ < ϵ*. We write the segment length in ψ0 as a sum of a multiple of the minimum length and a residual value, *i.e.*
γi = kiγ + 2li, where ki ∈ N
∗and 0 ⩽ 2li *< γ.*
To construct the polygonal curve ψ, we first let ψ(ti) = ψ0(ti) for 0 ⩽ i ⩽ n. Then we shall carefully define ψ on each interval [ti−1, ti] for 1 ⩽ i ⩽ n.

We first consider the case where li > 0. Denote the time slice ∆t = ti − ti−1. Let β be a unit vector that is normal to the ith line segment of ψ0, *i.e.*
⟨*β, ψ*0(ti−1) − ψ0(ti)⟩ = 0.

On the interval [ti−1, ti], we let the polygon curve ψ to have vertices {ψ(ti−1), ψ(ti−1 +

$$(t_{i-1}),\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t),\psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t),\psi(t_{i})\}$$

where

$$\begin{aligned} \psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t) &= \psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)+\sqrt{\gamma^{2}-l_{i}^{2}}\beta, \\ \psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t) &= \psi_{0}(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)+\sqrt{\gamma^{2}-l_{i}^{2}}\beta. \end{aligned}$$ $t_{i}|$ is defined as 
The specific form of ψ on [ti−1, ti] is defined as

$$\psi(t_{t-1}+t)=\begin{cases}\psi_{0}(t_{t-1}+t)+\dfrac{\gamma_{i}t}{l_{i}\Delta t}\sqrt{\gamma^{2}-l_{i}^{2}}\beta,&t\in[0,\dfrac{l_{i}}{\gamma_{i}}\Delta t];\\ \psi_{0}(t_{t-1}+t)+\sqrt{\gamma^{2}-l_{i}^{2}}\beta,&t\in[\dfrac{l_{i}}{\gamma_{i}}\Delta t,\Delta t-\dfrac{l_{i}}{\gamma_{i}}\Delta t];\\ \psi_{0}(t_{t-1}+t)+\dfrac{\gamma_{i}(\Delta t-t)}{l_{i}\Delta t}\sqrt{\gamma^{2}-l_{i}^{2}}\beta,&t\in[\Delta t-\dfrac{l_{i}}{\gamma_{i}}\Delta t,\Delta t].\end{cases}\tag{29}$$

One can verify that the following distance is equal to the minimum length γ as defined in Eq. (28),

ng distance is equal to the minimum length $\gamma$ as defined in Eq. (2)  $$\left|\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi(t_{i-1})\right|$$ $$=\left|\psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi_{0}(t_{i-1})+\sqrt{\gamma^{2}-l_{i}^{2}}\beta\right|$$ $$=\left(|\psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi_{0}(t_{i-1})|^{2}+(\gamma^{2}-l_{i}^{2})\right)^{\frac{1}{2}}$$ $$=\left(\left(\frac{l_{i}}{\gamma_{i}}\Delta t\frac{|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|}{\Delta t}\right)^{2}+(\gamma^{2}-l_{i}^{2})\right)^{\frac{1}{2}}$$ $$=\gamma.$$
Similarly, we have
 ψ(ti − li γi ∆t) − ψ(ti)  = γ. li γi ∆t) and ψ(ti − li γi ∆t) is a multiple of γ,  ψ(ti − li γi ∆t) − ψ(ti−1 + li γi ∆t)  =  ψ0(ti − li γi ∆t) − ψ0(ti−1 + li γi ∆t)  = ti − ti−1 − 2li γi ∆t ∆t|ψ0(ti) − ψ0(ti−1)| = ∆t − 2li γi ∆t ∆tγi = kiγ.
Also, one can show that the distance between ψ(ti−1 +
In sum, the curve ψ over [tt−1, ti] as defined in Eq. (29) is composed of three line segments with the lengths γ, kiγ and γ, respectively. One can treat ψ over [tt−1, ti] as a polygon curve of ki + 2 line segments with uniform length γ. Thus, we see that the constructed curve ψ ∈ Cγ.

For another case where li = 0, we simply set ψ(t) = ψ0(t), t ∈ [ti−1, ti]. Then ψ over [ti−1, ti] can be regarded as a polygon curve of kiline segments with uniform length γ. Also in this case, the constructed curve ψ ∈ Cγ.

Moreover, in the latter case li = 0, we have maxt∈[ti−1,ti]|ψ(t) − ψ0(t)| = 0. In the case li > 0, we have

$$\operatorname*{max}_{t\in[t_{i-1},t_{i}]}|\psi(t)-\psi_{0}(t)|=\left|{\sqrt{\gamma^{2}-l_{i}^{2}}}\beta\right|\leqslant\gamma<\epsilon.$$

This proves the inequality (27). Therefore, combing the inequality (25) and (27), we find a path ψ ∈ Cγ such that

$$\max_{t\in[0,T]}|\psi(t)-\varphi(t)|\leqslant\max_{t\in[0,T]}|\psi(t)-\psi_{0}(t)|+\max_{t\in[0,T]}|\psi_{0}(t)-\varphi(t)|$$ $$<\epsilon+2\epsilon$$ $$=3\epsilon.$$
$$\square$$

## B. Numerical Quadratures For Approximating The Integral In Problem (6).

One can use a numerical quadrature with m grid points to approximate the integral as in problem (6), where m is a positive integer. We discretize the time interval [0, hi] using m uniform points: tj = (j − 1/2)/m · hi, 1 ⩽ j ⩽ m. Denote the position of the path φ i(t) at time tj by

$$z_{i}^{j}=\varphi^{i}(t_{j})=z_{i}+\frac{j-1/2}{m}(z_{i+1}-z_{i}),\quad1\leqslant j\leqslant m.$$

Then the integral in the problem (6) can be approximated by

Then the margin in the problem (30) can be approximated by  $$\hat{L}(z_{i},z_{i+1};h_{i})\approx\frac{h_{i}}{m}\sum_{j=1}^{m}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V(z_{i}^{j})\right|^{2}\tag{30}$$ $$\geqslant2|z_{i+1}-z_{i}|\cdot\sqrt{\frac{1}{m}\sum_{j=1}^{m}\left|\nabla V(z_{i}^{j})\right|^{2}+2\langle z_{i+1}-z_{i},\,\frac{1}{m}\sum_{j=1}^{m}\nabla V(z_{i}^{j})\rangle}.$$  where the minimum value is achieved by setting 
$$h_{i}^{*}=|z_{i+1}-z_{i}|\,\Bigg/\,\sqrt{\frac{1}{m}\sum_{j=1}^{m}|\nabla V(z_{i}^{j})|^{2}}\;.$$
By setting m = 1, the cost function (30) reduces to the one in Eq. (7) using the mid-point quadrature as in the paper.

## C. The Parameters In Algorithm 1 **Used For The Numerical Examples In Section** 3.

Table 1. The parameters in Algorithm 1 used for the 2D system, extended Mueller system and Lennard-Jones system of seven particles.

| Parameters                                  | 2D system                  | Mueller system         | Lennard-Jones system   |               |     |
|---------------------------------------------|----------------------------|------------------------|------------------------|---------------|-----|
| ˜Qθ                                         | Network structure          | 4-50-50-1              | 20-50-50-1             | 24-100-100-1  |     |
| Activation on hidden layers                 | tanh                       | tanh                   | tanh                   |               |     |
| Critic                                      | Activation on output layer | sigmoid                | sigmoid                | sigmoid       |     |
| λ                                           | 1000                       | 1000                   | 1000                   |               |     |
| Actor ˜µθ                                   | Network structure          | 2-50-50-2              | 10-50-50-10            | 12-100-100-12 |     |
| Activation on hidden layers                 | tanh                       | tanh                   | tanh                   |               |     |
| Activation on output layer                  | None                       | None                   | None                   |               |     |
| Problem                                     |                            | γ in the path space Cγ | 0.1                    | 0.1           | 0.2 |
| Numerical quadrature in cost Rϵ             | mid-point scheme           | mid-point scheme       | mid-point scheme       |               |     |
| (M, h) in estimating Fϵ                     | -                          | (1000, 5 × 10−4 )      | -                      |               |     |
| maxstep (# of training steps)               | 700                        | 1000                   | 1000                   |               |     |
| maxtime (maximum length of one episode)     | 50                         | 100                    | 100                    |               |     |
| # of episodes per training step             | 50                         | 50                     | 100                    |               |     |
| Temperature ϵ ′ for sampling initial states | 0.3                        | 20                     | 0.3                    |               |     |
| (p1, p2) in exploration policy              | (1/3, 1/3)                 | (1/3, 1/3)             | (1/3, 1/3)             |               |     |
| Distribution for ξt in exploration policy   | N (0, π/4)                 | N (0, π/4)             | N (0, π/4)             |               |     |
| step0 for target networks                   | 10                         | 10                     | 10                     |               |     |
| buffer size NR                              | 105                        | 105                    | 106                    |               |     |
| Algorithm Training                          | Optimizer                  | Adam                   | Adam                   | Adam          |     |
| Learning rate                               | 10−3                       | 10−3                   | 10−3                   |               |     |
| Batch size |B|                              | 5000                       | 5000                   | 5000                   |               |     |

## D. Computing The Transition Tube For The Mueller System.

For the Mueller system with potential function (21), we define the two metastable set SA, SB with radius r0 around the states A, B as SA = {x ∈ R
10 : |(x1, x2) − (A1, A2)| < r0}, SB = {x ∈ R
10 : |(x1, x2) − (B1, B2)| < r0}
with r0 = 0.1, where (A1, A2) and (B1, B2) denote the first two numbers in the coordinates of A and B, respectively. The first hitting time of the two sets SA and SB is defined as τA(z) = inf t>0
{xt ∈ SA : x0 = z}, τB(z) = inf t>0
{xt ∈ SB : x0 = z}.

The committor function q(x) is defined in the configuration space, which is the probability that the system starting from x
first arrives in SB rather than SA:
q(x) = Prob[τA(x) > τB(x)].
A mathematical description for the committor function is given by the backward Kolmogorov equation with the Dirichlet
boundary conditions:
$$\begin{cases}\nabla V(x)\cdot\nabla q(x)-\epsilon\Delta q(x)=0,\quad x\in\Omega\setminus(S_{A}\cup S_{B})\\ q(x)=0,\;x\in\partial S_{A};\quad q(x)=1,\;x\in\partial S_{B}.\end{cases}$$
(31)
We compute the committor function qm(x1, x2) for the 2D Mueller system with the potential Vm(x1, x2) at ϵ = 10 by solving the partial differential equation (31) using the finite element method. The computational domain is taken as



Ω = [− 1.5, 1] × [− 0.5, 2]. Then the committor function q ( x ) for the 10D Mueller system with the potential (21) is given by q( x 1 , . . . , x 10 ) = q m ( x 1 , x 2 ).

The committor function itself is a good reactive coordinate for describing the transition of the system. As illustrated in Ref. (Ren et al., 2005), the transition tube can be characterized by the iso-committor surfaces of the committor function. For the 10D Mueller system considered in the numerical example, the transition events can be characterized by the transition tube corresponding to the first two dimensions ( x 1 , x 2 ).

Next, we compute the transition tube for the two-dimensional potential V m ( x 1 , x 2 ) at c = 10. To approximate the isocommittor surfaces, we divide the configuration space into sub-regions using a transition pathway ( e.g. the minimum energy path corresponding to the potential V m ( x 1 , x 2 ) with ω = 0). Specifically, the transition pathway ϕ is represented by Np = 185 states z 1 , . . . , z Np E R 2 with equal distance. Denote the committor function qm ( x 1 , x 2 ) on these points by q i = q m ( z i ), 1 ≤ i ≤ N p . Note that q i < · · < q N p . We approximate the q i -isocommittor surface using the region

$$x_{2})\in\mathbb{R}^{2}:(\cdot)$$
$\frac{10}{10}$ 10. 
.$=\,2\,-\,a_1$
Ω i = {( x 1 , x 2 ) ∈ R 2 : ( q i − 1 + q i )/ 2 < q m( x 1 , x 2 ) < ( q i + q i +1 )/ 2 } ,   1 ≤ i ≤ N p where qo = −q 1 and q N +1 = 2 − q N +1 = 2 − q N +1 We discretize the computational domain Ω using a mesh with 500 × 500 grid points. The set of grid points is denoted by
{Xk}kEz. Denote by Z i the indices of the grid points in {Xk}kEz which locate inside the region Ω i ,
I = {k ∈ I : X k ∈ Ω i }   1 ≤ i ≤ N p .

We assign the following Gibbs-Boltzmann weight to each grid point in { Xk}kEZ, in the region Ω i ,

$$w_{k}={\frac{1}{Z_{i}}}\exp\left[-{\frac{V_{m}(X_{k})}{\epsilon}}\right],\quad k\in{\mathcal{I}}_{i}$$
$${\mathrm{\boldmath~\Gamma~}}_{1})/2\},\quad1\leq i\leq N_{p}$$

where the normalization constant Z i = ∑ k E z i exp [ − V i n ( X k )/ c ]. The centerline of the transition tube can be represented by the weighted average of the grid points on each region Ω i :

$$c_{i}=\sum_{k\in{\mathcal{I}}_{i}}w_{k}\cdot X_{k},\quad1\leq i\leq N_{p}.$$

To represent the transition tube, we sort the weights and choose a subset { X k } k ∈ J , of { X k } k ∈ I , containing the least number of gird points with the largest weights wk such that

$$\sum_{i\in{\mathcal{I}}_{i}}w_{k}\geq\nu,$$

where ν ∈ [0, 1] denotes the confidence level. Then the transition tube is represented by a collection of grid point sets,
{Xk}k∈Ji
, 1 ≤ i ≤ Np.

In Fig. 10, we show the plots of the computed transition tube and its centerline using two different values for ν (ν = 0.68 and ν = 0.95). In the numerical example, we take ν = 0.68, as shown in upper panel of Fig. 7.

## E. Construction Of The Transformation Function T (X) **For The Lennard-Jones System.**

Since the Lennard-Jones system is invariant to translation of the particles in the system, we fix the coordinate of particle 1 at the origin, *i.e.* y1 = (0, 0) in the example. Thus the system is defined in the 12-dimensional space with the configuration x = (y2*, . . . , y*7), where yi denotes the coordinate of particle i.

Before introducing the transformation function, we define two angle functions as follows.

Definition. The angle f(u, v) ∈ [0, π] *between two nonzero vectors* u = (u1, u2) and v = (v1, v2) in R
2*is defined as*

$$f(u,v)=\operatorname{arccos}\left({\frac{\langle u,v\rangle}{|u|\cdot|v|}}\right).$$

Then we define the oriented angle between u and v as

$$\eta(u,v)=\begin{cases}f(u,v),&\langle u^{\prime},v\rangle\geq0\\ 2\pi-f(u,v),&\langle u^{\prime},v\rangle<0\end{cases}$$

where the vector u
′ = (−u2, u1). Note that η(*u, v*) ∈ [0, 2π].

Next, we construct a transformation function T (x) for the system in a two-step procedure.

(1) Rotating the cluster We compute the mean vector

$\bar{y}$ 4. 
y¯ =
1
6
$$+\cdot\cdot\cdot+y_{7}).$$

Let k be the number that solves
$$k=\operatorname*{arg\,min}_{2\leq i\leq7}f(y_{i},{\bar{y}}).$$
Using the particle k, we set the angle β = η(yk, ex),
where ex denotes the unit vector ex = (1, 0), and construct the rotation matrix

$e_{x}$). 
$$D_{\beta}=\begin{bmatrix}\cos\beta&-\sin\beta\\ \sin\beta&\cos\beta\end{bmatrix}.$$
We rotate the cluster with configuration x to x
′ = (y
′
2
, . . . , y′7
),

$$y_{i}^{\prime}=D_{\beta}\begin{bmatrix}y_{i1}\\ y_{i2}\end{bmatrix},\quad2\leq i\leq7$$

where yi = (yi1, yi2) denotes the coordinates of particle i. In the new configuration x
′, the particle k is on the x-axis.



## (2) Re-Indexing The Particles

We sort the angles { n ( e x , y , )} , 2 < i < 7 of the particles and obtain the particle sequence ( H , (2) , . . . , Y , (7) ) , where
( r (2), . . . , r (7)) denote the indices of the sorted particles.

Therefore, the transformation function is defined as: T(x) = (y,(2), . . . ,Y,(7)). In Fig. 11, we use two example clusters of the Lennard-Jones system to illustrate the above procedure for T ( x ).

To incorporate the transformation function T ( x ) into the critic and actor networks. We compute the critic function Q b and actor function μ q at the state s ∈ R 12 and action a which is a unit vector in R 12 as follows. We compute s ′ = T ( s ) with rotation matrix D β and indices ( τ(2),...,τ(7)) . Then we compute the transformed action a ′ from a using the same rotation D β and index function τ . The critic function at ( s, a ) is given by Q θ ( s ′ , α ′ ).

Denote ā = μ q (s ′ ) and let τ − 1 be the inverse function of τ . We compute the transformed action ā ′ from ā using the rotation D − β and index function τ − 1 . The actor function at s is given by ā ′ .