# Computing Transition Pathways for the Study of Rare Events Using Deep Reinforcement Learning 

Bo Lin ${ }^{1}$ Yangzheng Zhong ${ }^{1}$ Weiqing Ren ${ }^{1}$


#### Abstract

Understanding the transition events between metastable states in complex systems is an important subject in the fields of computational physics, chemistry and biology. The transition pathway plays an important role in characterizing the mechanism underlying the transition, for example, in the study of conformational changes of bio-molecules. In fact, computing the transition pathway is a challenging task for complex and high-dimensional systems. In this work, we formulate the path-finding task as a cost minimization problem over a particular path space. The cost function is adapted from the FreidlinWentzell action functional so that it is able to deal with rough potential landscapes. The path-finding problem is then solved using a actor-critic method based on the deep deterministic policy gradient algorithm (DDPG). The method incorporates the potential force of the system in the policy for generating episodes and combines physical properties of the system with the learning process for molecular systems. The exploitation and exploration nature of reinforcement learning enables the method to efficiently sample the transition events and compute the globally optimal transition pathway. We illustrate the effectiveness of the proposed method using three benchmark systems including an extended Mueller system and the Lennard-Jones system of seven particles.


## 1. Introduction

Understanding the transition events of dynamical systems is a fundamental but challenging task in many science problems, including chemical reaction, conformational changes of bio-molecules and nucleation events during phase transitions. For the system, the transition occurs by crossing a[^0]

typical energy barrier separating two metastable states in the presence of random perturbations. The general disparity between the effective thermal energy and the energy barrier usually leads to a long-waiting period for the system around metastable states before a sudden transition from one state to another emerges. In this setting, we call the transition as a rare event. The major interest for the study of rare events is to compute the mechanism underlying the transition events, such as the transition pathway and transition rate. In the past, a number of research works have been devoted to developing efficient approaches for investigating the transition mechanism. Well-known methods include the transition path sampling (Bolhuis et al., 2002; Dellago et al., 2002), the string method (E et al., 2002; 2005; Ren et al., 2005; Maragliano et al., 2006; E et al., 2007), the action-based method (Olender \& Elber, 1996) and the accelerated molecular dynamics (Voter, 1997). Also, the recent works in Ref. (Khoo et al., 2019; Li et al., 2019; Rotskoff et al., 2022) proposed deep learning based methods for computing the committor function, which is a central object in the transition path theory for understanding the transition mechanism (Ren et al., 2005; E \& Vanden-Eijnden, 2010).

The transition pathway in the zero-temperature limit is characterized by the minimum energy path (MEP). The MEP is a path defined in the configuration space along which the tangent of the path is parallel to the potential force. Classical methods for identifying the MEP include the nudged elastic band method (Jónsson et al., 1998), the string method (E et al., 2002; 2005; Ren et al., 2005; Maragliano et al., 2006; E et al., 2007) and the conjugate peak refinement method (Fischer \& Karplus, 1992). The Freidlin-Wentzell theory of large deviations provides a variational characterization of the most likelihood path via a path-based action functional. Based on this characterization, Ref. (E et al., 2004; Zhou et al., 2008; Heymann \& Vanden-Eijnden, 2008) developed the minimum action methods for computing the minimum action path by minimizing the functional over a path space where the two ends of path are constrained to particular states. Also, the Onsager-Machlup functional, first introduced by Onsager and Machlup (Onsager \& Machlup, 1953), was used to compute the most probable path associated with a finite-time horizon for systems at finite noise in many applications (Wang et al., 2010; Fujisaki et al., 2010;

Du et al., 2021). From another perspective, one can recast the variational formulation of the transition path as a finitehorizon optimal control problem (Fleming, 1977; Grafke \& Vanden-Eijnden, 2019). The control problem was recently solved by a reinforcement learning algorithm (Guo et al., 2024).

The situation is quite different when the potential energy surface is rough, which is the general case for practical molecular systems. In this case, the ensemble of transition paths can be characterized by a tube in the configuration space connecting the metastable states inside which the transition occurs with high probability (Ren et al., 2005). The rough potential energy surface contains numerous saddle points, most of which are separated by energy barriers comparable to or less than the thermal energy and thus do not act as bottlenecks of the transition. As a consequence, the potential force should not be straightforwardly used in the variational characterization of the transition pathway.

In this paper, we propose a deep reinforcement learning method for computing the transition pathway of the system with rough potential landscapes. We formulate the path-finding task as a cost minimization problem over a particular path space. To tackle the difficulties arising from the roughness of the potential landscape, we adapt the FreidlinWentzell functional and propose a cost function involving an effective force function. In the zero-temperature limit, the effective force simply reduces to the potential force of the system. The formulated path-finding problem is over a constrained sequence of states in the configuration space, where the optimal times slices are determined using numerical quadratures.

In recent years, the advances in reinforcement learning algorithms have made successful applications in many sequential decision making problems, including video games, robotic control and autonomous driving. A general class of reinforcement learning algorithms are based on computation of the state-action value function, such as the Deep Q Network (DQN) algorithm (Mnih et al., 2013; 2015), the deterministic policy gradient (DPG) algorithm (Silver et al., 2014) and the deep DPG (DDPG) algorithm (Lillicrap et al., 2015). In particular, the DQN algorithm utilizes the deep neural networks as the function approximators, where target networks and replay buffer are introduced to stabilize the algorithm. Furthermore, the DDPG algorithm combined the DQN with the actor-critic approach based on the policy gradient to adapt the algorithm to a broader case with continuous and high-dimensional action space.

In this work, we solve the formulated cost minimization problem for identifying the transition pathway using the actor-critic method based on the DDPG algorithm. The critic and actor functions are parameterized by neural networks. To target the exploration in the region of interest, the method employs a stochastic policy based on the actor function with random noise and the potential force of the system for generating episodes. Also, we utilize target networks and a replay buffer to address the possible instability issue in the learning process. For molecular systems, to enhance the learning efficiency, we incorporate physical properties of the system into the critic and actor networks. The exploitation and exploration nature of reinforcement learning together with these techniques establish a stable and efficient algorithm for sampling transition events and computing the globally optimal transition pathway for highdimensional systems with rough potential landscapes. We demonstrate the effectiveness of the method using three numerical examples including a two-dimensional system, an extended Mueller system and the Lennard-Jones system of seven particles.

The paper is organized as follows. In Section 2, we introduce the background and the formulated path-finding problem and propose the reinforcement learning algorithm. The numerical examples are presented in Section 3. In Section 4, we draw the conclusions.

## 2. Method

We consider a dynamical system in the configuration space $\mathbb{R}^{d}$, which is modelled by the over-damped Langevin equation:

$$
d x_{t}=-\nabla V\left(x_{t}\right) d t+\sqrt{2 \epsilon} d W_{t}, \quad t>0
$$

where $V(x)$ is a potential function, $W_{t}$ is a standard Brownian motion and $\epsilon$ is a parameter specifying the strength of the noise which is called the temperature of the system. The equilibrium distribution of the system is known as the Boltzmann density function $\rho(x)=Z^{-1} \exp \left(-\frac{1}{\epsilon} V(x)\right)$, where $Z$ is a normalization constant. Consider the general situation where there are two metastable states $A$ and $B$ for the system. A transition pathway between the two metastable states $A$ and $B$ is defined as a curve in configuration space connecting the two states.

For a time $T>0$, we denote by $\mathbb{C}_{[0, T]}$ the set of all absolute continuous functions in the configuration space over the time interval $[0, T]$ connecting the two metastable states $A$ and $B$. The Freidlin-Wentzell action functional for a given path $\varphi \in \mathbb{C}_{[0, T]}$ is defined as

$$
S_{T}[\varphi]=\int_{0}^{T} \frac{1}{4}\left|\varphi^{\prime}(t)+\nabla V(\varphi(t))\right|^{2} d t
$$

According to the Freidlin-Wentzell theory of large deviations (Freidlin \& Wentzell, 2012), when the noise $\epsilon$ is sufficiently small, for small number $\delta>0$, the probability that the system (1) stays in the neighborhood of a given path
$\varphi \in \mathbb{C}_{[0, T]}$ over the time interval $[0, T]$ can be estimated by

$$
\mathbb{P}\left[\max _{0 \leqslant t \leqslant T}\|x(t)-\varphi(t)\|<\delta\right] \approx \exp \left(-\frac{S_{T}[\varphi]}{\epsilon}\right)
$$

Therefore, in the zero-temperature limit, the most probable transition path of the system within the time horizon $[0, T]$ can be characterized by a minimizer of the functional (2):

$$
\varphi_{T}^{*}=\underset{\varphi \in \mathbb{C}_{[0, T]}}{\arg \min } S_{T}[\varphi]
$$

The path $\varphi_{T}^{*}$ is also referred to as the minimum action path. In the infinite-time limit by letting $T$ goes to infinity, the action functional of the minimum action path, $S_{T}\left[\varphi_{T}^{*}\right]$, converges to the infimum value

$$
\inf _{T>0} \inf _{\varphi \in \mathbb{C}_{[0, T]}} S_{T}[\varphi]
$$

where the infimum is over all times $T$ and the corresponding path space $\mathbb{C}_{[0, T]}$. Furthermore, the graph limit of the minimum action path is a minimum energy path (MEP) of the system. The MEP is, by definition, a curve in the configuration space along which the tangent of the curve is parallel to the potential force $-\nabla V(x)$.

In this work, we aim to find the transition pathway with minimal action in a path space that is close to $\cup_{T} \mathbb{C}_{[0, T]}$. To deal with rough potential landscapes, we propose a cost function by adapting the Freidlin-Wentzell functional. Then we propose a deep reinforcement learning algorithm to solve the path-finding problem.

### 2.1. Formulation of the Problem

For a small number $\gamma>0$, we consider a path space $\mathbb{C}_{\gamma}$ consisting of continuous piecewise linear functions, whose graph is a polygonal chain connecting the two states $A$ and $B$. Each path $\varphi(t)$ in the space $\mathbb{C}_{\gamma}$ is represented by a sequence of states $\left(z_{0}, \ldots, z_{N}\right)$ in the configuration space, together with the corresponding time points $\left(t_{0}, \ldots, t_{N}\right)$ (See Fig. 1). The sequence $\left(z_{0}, \ldots, z_{N}\right)$ forms a polygonal chain connecting $A$ and $B$ where the line segments are of equal length $\gamma$ except the last one, i.e.

$$
\begin{aligned}
& z_{0}=A ; \quad z_{N}=B \\
& \gamma=\left|z_{i}-z_{i+1}\right|, 0 \leqslant i \leqslant N-2 \\
& \gamma \geqslant\left|z_{N-1}-z_{N}\right|
\end{aligned}
$$

Over the time interval $\left[t_{i}, t_{i+1}\right]$, the path $\varphi(t)$ is a straight line connecting $z_{i}$ and $z_{i+1}$ with uniform derivatives,

$$
\varphi(t)=z_{i}+\frac{z_{i+1}-z_{i}}{h_{i}}\left(t-t_{i}\right), \quad t_{i} \leqslant t \leqslant t_{i+1}
$$

where the time slice $h_{i}=t_{i+1}-t_{i}$. We denote the function $\varphi^{i}(t)=\varphi\left(t+t_{i}\right)$ for $t \in\left[0, h_{i}\right]$. One can show that



Figure 1. Schematic illustration of an absolute continuous path (black solid line) connecting the two metastable states $A$ and $B$, which is approximated by a path $\varphi(t)$ (green dashed line) in $\mathbb{C}_{\gamma}$ represented by a polygonal chain with a sequence of states $\left(z_{0}, \ldots, z_{N}\right)$.

the set $\cup_{\gamma>0} \mathbb{C}_{\gamma}$ is a dense subset of $\cup_{T>0} \mathbb{C}_{[0, T]}$ (See Appendix A). Next, we consider the following action minimization problem restricted to the path space $\mathbb{C}_{\gamma}$ for computing the transition pathway of the system,

$\inf _{\varphi \in \mathbb{C}_{\gamma}} \sum_{i=0}^{N-1} \tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right), \quad$ where

$\tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right)=\int_{0}^{h_{i}}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V\left(\varphi^{i}(t)\right)\right|^{2} d t$.

The optimization problem is, in principle, over a finite set of states $\left(z_{0}, \ldots, z_{N}\right)$ in the configuration space subject to the constraints (5), together with the time slices $\left(h_{0}, \ldots, h_{N-1}\right)$.

Optimal Time Slices. In the problem (6), for a particular sequence of states $\left(z_{0}, \ldots, z_{N}\right)$, each optimal time slice $h_{i}^{*}$ is a minimizer to the individual integral $\tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right)$. However, it is not straightforward to obtain an analytical solution for $h_{i}^{*}$ in general as the integral involves the potential force. Instead, one can compute an optimal solution $h_{i}^{*}$ by approximating the integral $\tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right)$ using a mid-point numerical quadrature,

$$
\begin{gathered}
\min _{h_{i}} \tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right) \approx \min _{h_{i}} h_{i}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V\left(z_{i+1 / 2}\right)\right|^{2} \\
=2\left|z_{i+1}-z_{i}\right| \cdot\left|\nabla V\left(z_{i+1 / 2}\right)\right| \\
\quad+2\left\langle z_{i+1}-z_{i}, \nabla V\left(z_{i+1 / 2}\right)\right\rangle
\end{gathered}
$$

where the mid-point $z_{i+1 / 2}=\left(z_{i}+z_{i+1}\right) / 2$ and the minimum value for $\tilde{L}$ is achieved at $h_{i}^{*}=\mid z_{i+1}-$ $z_{i}|/| \nabla V\left(z_{i+1 / 2}\right) \mid$. We denote the minimum value in Eq. (7) by $R\left(z_{i}, z_{i+1}\right)$ and refer to it as the cost between $z_{i}$ and $z_{i+1}$. In principle, the integral $\tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right)$ in Eq. (6) can be approximated using any suitable numerical quadratures (See Appendix B).

Therefore, the task of finding the optimal transition path
in the space $\mathbb{C}_{\gamma}$ as in Eq. (6) can be formulated as a cost minimization problem over the states $\left(z_{0}, \ldots, z_{N}\right)$ :

$$
\underset{\left(z_{0}, \ldots, z_{N}\right)}{\arg \min } \sum_{i=0}^{N-1} R\left(z_{i}, z_{i+1}\right)
$$

where the states $\left(z_{0}, \ldots, z_{N}\right)$ representing a transition path $\varphi(t)$ are subject to the constraints in Eq. (5).

Effective Force. The situation is quite different when the potential energy surface is rough, which is the typical case for practical molecular systems. In this case, the rough potential energy surface may contain numerous saddle points, most of which do not act as bottleneck of the transition as potential barriers separating those saddle points are less than or comparable to the thermal energy (Ren et al., 2005). As a consequence, the Freidlin-Wentzell path functional as in Eq. (2) directly involving the potential force is no longer valid for quantifying the transition events.

For a particular line segment connecting $z_{i}$ and $z_{i+1}$ in the path, consider the original dynamics (1) starting from the mid-point $z_{i+1 / 2}$ :

$$
d x_{t}=-\nabla V\left(x_{t}\right) d t+\sqrt{2 \epsilon} d W_{t}, \quad x_{0}=z_{i+1 / 2}
$$

For $h>0$, integrating both sides of the equation over the time interval $[0, h]$ gives

$$
x_{h}=z_{i+1 / 2}-\int_{0}^{h} \nabla V\left(x_{t}\right) d t+\xi, \quad \xi \sim \mathcal{N}(0,2 \epsilon h)
$$

We treat the potential force in the integral as a uniform value around the state $z_{i+1 / 2}$ and refer to it as the effective force at $z_{i+1 / 2}$. The formal definition of the effective force at $z_{i+1 / 2}$ is given by

$$
F_{\epsilon}\left(z_{i+1 / 2}\right)=\mathbb{E}_{\epsilon}\left[\frac{x_{h}-x_{0}}{h}: x_{0}=z_{i+1 / 2}\right]
$$

where the expectation is over a state ensemble of the system at time $h$ starting from the state $z_{i+1 / 2}$ at the temperature $\epsilon$. In practice, we approximate the effective force $F_{\epsilon}\left(z_{i+1 / 2}\right)$ using $M$ short trajectories following the dynamics (9) over the time interval $[0, h]$ where the state at time $h$ for each trajectory is denoted by $x_{j}^{e}$,

$$
F_{\epsilon}\left(z_{i+1 / 2}\right) \approx \frac{1}{M} \sum_{j=1}^{M} \frac{x_{j}^{e}-z_{i+1 / 2}}{h}
$$

We then define the cost function

$$
\begin{aligned}
R_{\epsilon}\left(z_{i}, z_{i+1}\right)= & \min _{h_{i}} h_{i}\left|\frac{z_{i+1}-z_{i}}{h_{i}}-F_{\epsilon}\left(z_{i+1 / 2}\right)\right|^{2} \\
= & 2\left|z_{i+1}-z_{i}\right| \cdot\left|F_{\epsilon}\left(z_{i+1 / 2}\right)\right| \\
& -2\left(z_{i+1}-z_{i}\right) \cdot F_{\epsilon}\left(z_{i+1 / 2}\right) .
\end{aligned}
$$

Note that the cost function reduces to the Freidlin-Wentzell cost in Eq. (7) when $\epsilon$ and $h$ tends to zero since the expectation (10) asymptotically converges to the potential force $-\nabla V\left(z_{i+1 / 2}\right)$. For simplicity, we denote by $R_{0}$ the zerotemperature cost function $R$ as defined in Eq. (7). For the system with rough potential landscapes at temperature $\epsilon$, the transition pathway connecting $A$ and $B$ can be computed by solving the cost minimization problem

$$
\underset{\left(z_{0}, \ldots, z_{N}\right)}{\arg \min } \sum_{i=0}^{N-1} R_{\epsilon}\left(z_{i}, z_{i+1}\right)
$$

where the states $\left(z_{0}, \ldots, z_{N}\right)$ in the configuration space are subject to the constraints in Eq. (5).

### 2.2. Reinforcement Learning Method

To solve the path-finding problem in Eq. (13), we define a Markov decision process with a state space $\mathcal{X}=\mathbb{R}^{d}$ and continuous action space $\mathcal{A}=\left\{x \in \mathbb{R}^{d}:|x|=1\right\}$. During the process, an agent interacts with the environment at discrete time steps. At each step, the agent takes an action, observes the next state and receives a running cost (or reward). Specifically, we set the transition dynamics and cost function $r(s, a)$ to be deterministic and consistent with the problem (13), i.e. the next state after taking action $a_{t}$ at state $s_{t}$ is given by $s_{t+1}=s_{t}+\gamma \cdot a_{t}$ and the received cost is defined as $r_{t}=R_{\epsilon}\left(s_{t}, s_{t+1}\right)$ as in Eq. (7) for $\epsilon=0$ or Eq. (12) for $\epsilon>0$. The terminal condition is that the agent arrives in the region $\Omega_{\gamma}=\left\{x \in \mathbb{R}^{d}:|x-B|<\gamma\right\}$.

The agent's behaviour is described by a policy $\pi$, which gives the action $\pi(s)$ for each state $s$. For a given policy $\pi$, the return from a state $s_{t}$ is defined as the sum of future costs, $R_{t}=r_{t}+\cdots+r_{T}$, where $T$ denotes the terminal time of the process. Our goal is to learn a policy $\pi^{*}$ which minimizes the return for each state $s \in \mathcal{X}$. The state-action function $Q(s, a)$ associated with the optimal policy $\pi^{*}$ is defined as the return after taking action $a$ at $s$ and thereafter following the policy $\pi^{*}$. Many reinforcement learning algorithms for computing the function $Q(s, a)$ are based on a recursive relationship known as the Bellman equation:

$$
Q\left(s_{t}, a_{t}\right)=r\left(s_{t}, a_{t}\right)+\min _{b \in \mathcal{A}} Q\left(s_{t+1}, b\right)
$$

To deal with the task with continuous action space, here we use an actor-critic approach based on the DDPG algorithm (Lillicrap et al., 2015). The critic function is the state-action function $Q(s, a)$ which is parameterized using a neural network $\tilde{Q}_{\theta}(s, a): \mathcal{X} \times \mathcal{A} \rightarrow[0,1]$,

$$
Q_{\theta}(s, a)= \begin{cases}\lambda \tilde{Q}_{\theta}(s, a), & s \notin \Omega_{\gamma} \\ R_{\epsilon}(s, B), & s \in \Omega_{\gamma}\end{cases}
$$

where $\lambda>0$ is predefined parameter which specifies the range of the critic function as $[0, \lambda]$. The actor function
$\mu(s)=\arg \min _{a} Q(s, a)$ corresponding to the optimal policy specifies the optimal action at each state. To construct an actor network mapping states to unit vectors in $\mathbb{R}^{d}$, we represent the actor function as a normalized vector based the cosines of a hidden actor $\tilde{\mu}_{\theta}: \mathbb{R}^{d} \rightarrow \mathbb{R}^{d}$,

$$
\mu_{\theta}(s)=\Theta\left[\cos \left(\tilde{\mu}_{\theta}(s)\right)\right],
$$

where $\Theta[v]=v /|v|$ is the normalization function with an input vector $v \in \mathbb{R}^{d}$. Note that the actor function is periodic over the hidden actor $\tilde{\mu}_{\theta}(s)$ with period $2 \pi$.

Data Generation. We sample data by generating episodes where the initial states are produced from a particular distribution $p(s)$ and subsequently the action of the agent is selected based on a stochastic policy. To facilitate the exploration of possible transition pathways, we add noise to the hidden actor function $\tilde{\mu}_{\theta}$ in the selection of action. Meanwhile, we aim to target the exploration in the region of interest which excludes states in the configuration space with low equilibrium densities $\rho(x)$. Thus, we take the action conducted at step $t$ as $a_{t}=\Theta\left[\tilde{a}_{t}\right]$, where

$$
\tilde{a}_{t}= \begin{cases}\cos \left(\tilde{\mu}_{\theta}\left(s_{t}\right)\right), & \text { with probability } p_{1} \\ -\nabla V\left(s_{t}\right), & \text { with probability } p_{2} \\ \cos \left(\tilde{\mu}_{\theta}\left(s_{t}\right)+\xi_{t}\right), & \text { with probability } 1-p_{1}-p_{2}\end{cases}
$$

where $\xi_{t} \in \mathbb{R}^{d}$ is sampled from a Gaussian distribution and $p_{1} \geqslant 0, p_{2} \geqslant 0,1-p_{1}-p_{2} \geqslant 0$.

We use a replay buffer $\mathcal{R}$ with fixed size $N_{R}$ to store the sampled transitions, where the oldest ones will be discarded when new samples are appended to the buffer. The critic function $Q(s, a)$ can be learned off-policy, allowing us to maintain a large-size replay buffer and sample a mini-batch from the buffer for training neural networks at each step.

Policy Evaluation. Target neural networks are often employed in reinforcement learning algorithms to address the instability issue when nonlinear and large scale neural networks are used. Here we duplicate the critic and actor networks as the target networks $Q_{\theta}^{\prime}(s, a), \mu_{\theta}^{\prime}(s)$ each time after a particular number of steps. The target networks will be used to compute the target values in the temporal-difference (TD) loss function for training the critic network,

$$
\begin{aligned}
L_{Q}(\theta) & =\frac{1}{|\mathcal{B}|} \sum_{\left(s_{t}, a_{t}, r_{t}, s_{t+1}\right) \in \mathcal{B}}\left|Q_{\theta}\left(s_{t}, a_{t}\right)-y_{t}\right|^{2} \\
y_{t} & =r_{t}+Q_{\theta}^{\prime}\left(s_{t+1}, \mu_{\theta}^{\prime}\left(s_{t+1}\right)\right)
\end{aligned}
$$

Here we use the stochastic gradient descent to train the neural networks, and $\mathcal{B}=\left\{\left(s_{t}, a_{t}, r_{t}, s_{t+1}\right)\right\}$ is a batch of transitions sampled from the replay buffer.

Policy Gradient. The actor network is trained using the gradient of an average return $J_{\mu}$ over the batch states with
Algorithm 1 Reinforcement learning for computing the optimal transition pathway at temperature $\epsilon$.

Initialize critic and actor networks $Q_{\theta}(s, a)$ and $\mu_{\theta}(s)$.

Initialize target networks: $Q_{\theta}^{\prime} \leftarrow Q_{\theta}, \mu_{\theta}^{\prime} \leftarrow \mu_{\theta}$, and initialize replay buffer $\mathcal{R}$.

for step $=1$ to maxstep do

Sample initial state $s_{0}$ from distribution $p(s)$.

for $t=0$ to maxtime do

Select action $a_{t}$ according to policy (16);

Update new state $s_{t+1}=s_{t}+\gamma \cdot a_{t}$

Sample $M$ trajectories starting from $s_{t+1 / 2}=$

$\frac{1}{2}\left(s_{t}+s_{t+1}\right)$ with time $h$ and estimate $F_{\epsilon}\left(s_{t+1 / 2}\right)$ as in Eq. (11);

Compute cost $r_{t}=R_{\epsilon}\left(s_{t}, s_{t+1}\right)$

Store $\left(s_{t}, a_{t}, r_{t}, s_{t+1}\right)$ in $\mathcal{R}$;

Sample a batch $\mathcal{B}=\left\{\left(s_{t}^{i}, a_{t}^{i}, r_{t}^{i}, s_{t+1}^{i}\right)\right\}$ from $\mathcal{R}$;

Compute target values

$$
y_{t}^{i}=r_{t}^{i}+Q_{\theta}^{\prime}\left(s_{t+1}^{i}, \mu_{\theta}^{\prime}\left(s_{t+1}^{i}\right)\right)
$$

Update critic $Q_{\theta}$ using the loss function (17);

Update actor $\mu_{\theta}$ using the sampled policy gradients in Eq. (18);

Exit if terminal condition $s_{t+1} \in \Omega_{\gamma}$ is met.

end

if $\bmod \left(\right.$ step $\left.^{\text {step }}{ }_{0}\right)=0$ then

Update target networks $Q_{\theta}^{\prime} \leftarrow Q_{\theta}, \mu_{\theta}^{\prime} \leftarrow \mu_{\theta}$.

end

end

Output: The critic and actor functions $Q_{\theta}(s, a), \mu_{\theta}(s)$.

respect to the actor parameters by applying the chain rule,

$$
\nabla_{\theta} J_{\mu}=\left.\frac{1}{|\mathcal{B}|} \sum_{s_{t} \in \mathcal{B}} \nabla_{a} Q_{\theta}\left(s_{t}, a\right)\right|_{a=\mu_{\theta}\left(s_{t}\right)} \cdot \nabla \mu_{\theta}\left(s_{t}\right)
$$

Physics-based Learning. General molecular systems are usually invariant to certain transformations of the system, such as translation, rotation of the configuration and reindexing of particles of the same species in the system. The physical properties can be described by a transformation function $x^{\prime}=\mathcal{T}(x)$ mapping a given configuration $x$ and its equivalent ones to a representative configuration $x^{\prime}$. We make the learning process respect the physical properties. In the critic and actor networks, the state-action input $(s, a)$ is transformed into $\left(s^{\prime}, a^{\prime}\right)$ by $\mathcal{T}$ before fed into the network. For the actor network, we restore the output $\tilde{a} \in \mathcal{A}$ to $\tilde{a}^{\prime} \in$ $\mathcal{A}$ by the inverse of $\mathcal{T}$, where $\mathcal{A}$ denotes the action space. Learning over an effective manifold of the configuration space can enhance the efficiency of the algorithm.

A pseudocode for describing the reinforcement learning algorithm is presented in Algorithm 1. Once the actor network
is trained, one can compute a transition pathway with states $\left\{z_{t}\right\}_{0 \leqslant t \leqslant T}$ by performing the iterative procedure:

$$
z_{t+1}=z_{t}+\gamma \cdot \mu_{\theta}\left(z_{t}\right), t \geq 0 ; \quad z_{0}=A
$$

until the terminal condition $z_{T-1} \in \Omega_{\gamma}$ is satisfied and we set $z_{T}=B$.

Remark 1: The proposed method is able to compute the globally optimal transition pathway. Traditional methods for computing the transition pathway including the nudged elastic band method (Jónsson et al., 1998), the string method (E et al., 2002; 2007) and the minimum action method (E et al., 2004; Heymann \& Vanden-Eijnden, 2008) are suffering from the issue of metastability, as they are performing an iterative procedure in the path space starting from a particular path. The solution relies on the initial guess of path. In the general case with multiple transition pathways (for example, in conformational changes of bio-molecules), suitable initial guess is usually not straightforwardly available. In this case, these methods may get trapped in the neighborhood of a locally optimal solution and produce a path that is far away from the globally optimal one. On the other hand, as in the stochastic policy (16), the proposed reinforcement learning algorithm is able to explore the entire configuration space due to the randomness term and focus on the transition region of interest based on the optimal policy introduced by the actor function. The exploration-exploitation balance makes the proposed method able to compute the globally optimal path in the whole configuration space.

Remark 2: There are a number of reinforcement learning algorithms developed recently with substantial improvements over the DDPG algorithm, such as the twin delayed deep deterministic policy gradient algorithm (TD3) (Fujimoto et al., 2018) and the soft actor-critic algorithm (Haarnoja et al., 2018). In this work, we propose a framework of formulating the path-finding problem for dynamical systems and employing RL algorithms to solve the problem. Besides the basic DDPG algorithm, the proposed method enjoys the flexibility of combining with advanced techniques from other RL algorithms, for instance, twin Q-functions and target policy smoothing in TD3, to improve the performance of the method. This might be helpful in specific implementations and will be tested in future works.

## 3. Numerical Examples

To illustrate the effectiveness of the proposed method, we apply Algorithm 1 to three benchmark systems including a two-dimensional system, a ten-dimensional system with an extended Mueller potential and the Lennard-Jones system of seven particles. The first system is adapted from Ref. (E et al., 2007) which exhibits two typical transition pathways connecting the metastable states. The latter two systems have been extensively studied in previous works (Khoo et al., 2019; Li et al., 2019; Dellago et al., 1998; Evans et al., 2023). To validate the accuracy of the computed transition pathway, one can compute a reference solution of the transition pathway using the string method or transition tube by constructing the committor function landscape. Thus, the three examples can be used to benchmark the proposed method.

We parameterize the critic and actor functions using fullyconnected neural networks with two hidden layers and put the hyperbolic tangent function $(\tanh )$ as the activation unit in the network. In the critic network $\tilde{Q}_{\theta}$, as specified in Eq. (14), we put a sigmoid function on the output layer and set $\lambda=1000$. In the hidden actor $\tilde{\mu}_{\theta}$ as in Eq. (15), there is no activation function acting on the output layer.

In the three examples, we generate episodes in parallel with initial states sampled from a mixed distribution. Specifically, $30 \%$ of the initial states are taken as the metastable state $A$ while the remaining are sampled from the equilibrium distribution of the system at a particular temperature $\epsilon^{\prime}$. The latter part of initial states are collected by simulating the Langevin equation (1) of the system. In the exploration policy (16), we take $p_{1}=1 / 3, p_{2}=1 / 3$ and $\xi_{t}$ is sampled from the Gaussian distribution $\mathcal{N}(0, \pi / 4)$. The neural networks are trained using the stochastic gradient descent with the Adam optimizer (Kingma \& Ba, 2015) and batch size 5000. With a batch of data points sampled from the replay buffer, we train the critic and actor networks repeatedly for 10 times using the temporal-difference loss function (17) and the sampled policy gradient in Eq. (18), respectively. The target networks are updated every 10 training steps. The parameters in Algorithm 1 used for the three examples are shown in the table in Appendix C.

### 3.1. A Two-dimensional System

To illustrate the ability of the method for predicting the globally optimal transition pathway, we first consider a twodimensional (2D) system with two typical transition pathways. The potential function of the system, as adapted from Ref. (E et al., 2007), is given by

$$
V(x, y)=\left[\left(1-x^{2}-y^{2}\right)^{2}+\frac{y^{2}}{x^{2}+y^{2}}\right](1+g(y))
$$

where $g(y)=1 /(1+\exp (-y))$ denotes the sigmoid function. For the system, there are two metastable states at $A=(-1,0)$ and $B=(1,0)$, corresponding to two local minima of the potential $V$.

The system has two minimum energy paths (MEP) connecting $A$ and $B$. We first compute reference solutions for the two paths using the string method (E et al., 2007). The string is represented by 501 points in the 2D plane. We perform the string method twice, in which the initial strings are taken
as straight lines connecting the two points $(-0.5,0.5)$ and $(0.5,0.5)$ and connecting $(-0.5,-0.5)$ and $(0.5,-0.5)$, respectively. Plots of the two computed MEPs are shown in the upper panel of Fig. 2, which resemble upper/lower semicircles connecting $A$ and $B$ in the 2D plane. For convenience, we refer to the two curves as upper/lower MEPs. Also shown in the lower panel of Fig. 2 is the potential energy (19) of the system along the two paths, from which one can observe that the upper MEP has a energy barrier of $\Delta V \simeq 2$, whereas lower MEP has a barrier of $\Delta V \simeq 1$. Therefore, the lower MEP is the globally optimal transition pathway between $A$ and $B$, especially when the magnitude of noise is much less than 1 , i.e. $\epsilon \ll 1$.

With the lower MEP, denoted by $\varphi$, one can quantitatively evaluate the path $\varphi_{\theta}$ computed by the proposed method. Note that $\varphi$ is parameterized by the normalized arc-length $\alpha$ of the path. We first re-parameterize $\varphi_{\theta}$ with its normalized arc-length and then evaluate $\varphi_{\theta}$ using the relative error:

$$
e_{\varphi}=\frac{\left\|\varphi_{\theta}(\alpha)-\varphi(\alpha)\right\|}{\|\varphi(\alpha)\|}
$$

where the norm is defined as $\|\phi(\alpha)\|=$ $\sqrt{\frac{1}{n_{e}} \sum_{i=1}^{n_{e}}\left|\phi\left(i / n_{e}\right)\right|^{2}}$ for a function $\phi$ using $n_{e}=100$ discrete points.

We apply Algorithm 1 with 700 training steps to compute the transition pathway, in 20 independent runs with random initialization on the critic and actor networks. In the path-finding problem (13), we take the path space $C_{\gamma}$ with $\gamma=0.1$ and set $\epsilon=0$. All of the computed paths using the proposed method are close to the lower MEP, as shown in the upper panel of Fig. 2. The lower panel of the figure shows the potential function along the computed path, which agrees well with the potential along the lower MEP. The statistics of relative error for the paths defined in Eq. (20) in the 20 runs is $e_{\varphi}=0.0060 \pm 0.0020$. The results demonstrate the accuracy of the methods for computing the transition pathway.

As a comparison, we also apply the string method with random initialization to the system in 20 independent runs. On each run, the initial string is taken as a straight line randomly sampled on the 2D plane. Specifically, one end point $x_{a}$ of the line is sampled from $\mathcal{U}([-1.5,0) \times[-1.5,1.5])$ and the other end point $x_{b}$ is sampled from $\mathcal{U}((0,1.5] \times[-1.5,1.5])$, where $\mathcal{U}(\cdot)$ indicates the uniform distribution. In the total 20 runs, the string method is convergent to the lower MEP for 11 runs and to the upper MEP for the remaining runs. The results demonstrate that the proposed method statistically outperforms the string method for computing the globally optimal transition pathway.


Figure 2. Plots of the MEPs computed using the string method and the transition pathway computed from the actor network $\mu_{\theta}(s)$ (Upper). Plots of the potential function $V(x)$ along the three paths (Lower). The two MEPs are referred to as the upper/lower MEPs. The contour lines in the upper panel indicate the potential function $V(x)$ in Eq. (19).

### 3.2. Extended Mueller System

To illustrate the effectiveness of the method for dealing with high-dimensional systems and rough energy landscapes, we consider the Mueller potential embedded in the tendimensional space,

$$
V(x)=V_{m}\left(x_{1}, x_{2}\right)+\frac{1}{2 \sigma^{2}} \sum_{i=3}^{10} x_{i}^{2}, \quad x \in \mathbb{R}^{10}
$$



Figure 3. Plots of the computed transition pathway $\varphi_{\theta}(\alpha)$ between the metastable states $A$ and $B$ and the minimum energy path (MEP) $\varphi(\alpha)$ which are projected on the $\left(x_{1}, x_{2}\right)$ plane. The inset plot shows the potential function along the two paths. The contour lines indicate the potential function $V(x)$ in Eq. (21).

where $V_{m}\left(x_{1}, x_{2}\right)$ is the Mueller potential for the first two dimensions,

$$
\begin{aligned}
V_{m}\left(x_{1}, x_{2}\right)= & \sum_{i=1}^{4} D_{i} \exp \left[a_{i}\left(x_{1}-X_{i}\right)^{2}\right. \\
& \left.+b_{i}\left(x_{1}-X_{i}\right)\left(x_{2}-Y_{i}\right)+c_{i}\left(x_{2}-Y_{i}\right)^{2}\right] \\
& +\omega \sin \left(2 k \pi x_{1}\right) \sin \left(2 k \pi x_{2}\right)
\end{aligned}
$$

and another 8 harmonic functions are added for the remaining dimensions with the parameter $\sigma$ specifying the strength of the harmonic terms. The parameters $\omega$ and $k$ control the roughness of the potential landscape. We take the two metastable states as $A=(-0.558,1.441,0, \ldots, 0)$ and $B=(0.623,0.028,0, \ldots, 0)$, which corresponds to two local minimum points of the potential function $V(x)$.

In this example, we take the parameters except $\omega, k$ from Ref. (Li et al., 2019) and consider two cases for the potential function (21) with different values of $\omega$. In the first case $(\omega=0)$, the potential landscape is smooth and we apply the method to compute the transition pathway for the system in the zero-temperature limit. In the second case ( $\omega>$ 0 ), the potential landscape is rather rugged with numerous saddle points and we compute the transition pathway at the temperature $\epsilon=10$.

Smooth Mueller Potential. In the first case, we set the parameter $\omega=0$. For the example, we compute the optimal transition pathway in the path space $\mathbb{C}_{\gamma}$ with $\gamma=0.1$ and apply Algorithm 1 to solve the problem (13) with $\epsilon=0$. In the algorithm, we conduct 1000 training steps; at each step, we generate episodes according to the exploration policy (16) and train the critic and actor networks.



Figure 4. Plots of the temporal-difference (TD) loss function $L_{Q}$ and the average return $J_{\mu}$ versus the training steps in Algorithm 1.



Figure 5. Plot of the relative error for the path $\varphi_{\theta}$ computed from the actor network $\mu_{\theta}(s)$ versus the training steps in Algorithm 1. The error is defined in Eq. (20).

In Fig. 3, we plot the transition pathway $\varphi_{\theta}$ computed from the actor network $\mu_{\theta}(s)$, which is projected on the $\left(x_{1}, x_{2}\right)$ plane. Also shown is the minimum energy path $\varphi$ computed using the string method (E et al., 2007). The inset plot in Fig. 3 shows the potential function along the two paths. In Fig. 3, one can observe that the two paths are almost indistinguishable to each other and the method accurately predicts the potential barrier separating the two metastable states via the computed transition pathway. With $\varphi$, the relative error for $\varphi_{\theta}$ as defined in Eq. (20) under 10 independent runs is $e_{\varphi}=0.0203 \pm 0.0061$. The results demonstrate the accuracy of the proposed reinforcement learning algorithm for predicting the transition pathway of high-dimensional systems.

In Fig. 4, we show plots of the temporal-difference loss function $L_{Q}$ and the average return $J_{\mu}$ over the whole replay buffer versus the training step. Also, we show the performance of the actor network, i.e. the relative error for $\varphi_{\theta}$,


Figure 6. Plot of two generated episodes starting from the state $A$ (Upper) and scatter plot of the states $\left\{s_{t}^{i}\right\}$ in the replay buffer (Lower) at the last training step of Algorithm 1.

versus the training steps in Fig. 5. From the figures, one can observe that the two losses and error are all convergent to low values after about 400 training steps, which indicates the stability of the algorithm for the system. A scatter plot of the states $\left\{s_{t}^{i}\right\}$ in the replay buffer, projected on the $\left(x_{1}, x_{2}\right)$ plane, at the last training step of the algorithm is shown in Fig. 6, together with two generated episodes starting from the state $A$. We observe that the generated data points cluster around the minimum energy path (MEP) as shown in Fig. 3, with adequate sampling densities everywhere along the path, and the two episodes are guided towards the state $B$ along the MEP with exploration randomness. The results demonstrate that the proposed method is capable of exploring the region regarding transition and sampling transition events efficiently.

Rugged Mueller Potential. In the second case, we set the parameters $\omega=9, k=5$ and apply Algorithm 1 to compute the optimal transition pathway at $\epsilon=10$. The



Figure 7. Plots of the transition pathway between the metastable states $A$ and $B$ computed from the actor network $\mu_{\theta}(s)$ and the transition tube computed by mapping a committor function landscape of the system, for the rugged potential case at $\epsilon=10$. The inset plot shows the potential function along the computed path.

parameters in the algorithm are set as those in the previous case. Additionally, we take $h=5 \times 10^{-4}$ for generating short trajectories of the system to estimate the function $F_{\epsilon}(z)$ as in Eq. (11).

Plots of the transition pathway computed from the actor network $\mu_{\theta}(s)$ and the potential function along the path are shown in Fig. 7. We validate the solution using a transition tube of the system inside which the transition occurs with high probability (Ren et al., 2005). Specifically, we compute the transition tube at $\epsilon=10$ by mapping a committor function landscape of the system (See Appendix D). As observed from Fig. 7, the computed transition pathway locates near the center of the transition tube, which demonstrates the proposed method is able to predict the transition pathway for high-dimensional systems with rough potential landscapes.

### 3.3. Lennard-Jones System

To illustrate the ability of the algorithm to deal with molecular systems, we apply the method to study a rearrangement process of the Lennard-Jones system, which is a cluster of seven particles on the plane. The system is relatively simple but serves as a good example to benchmark the proposed method.

In the system, the particles are interacting via the LennardJones porential function

$$
V\left(y_{1}, \ldots, y_{7}\right)=\sum_{i<j} 4 \epsilon_{0}\left[\left(\frac{\sigma_{0}}{r_{i j}}\right)^{12}-\left(\frac{\sigma_{0}}{r_{i j}}\right)^{6}\right]
$$



Figure 8. Two typical stable configurations of the Lennard-Jones cluster where particle 1 (in red color) is either at the center (Left) or surface (Right) of the cluster.

where $\left(y_{1}, \ldots, y_{7}\right)$ denotes the position-vector of the seven particles, $r_{i j}=\left|y_{i}-y_{j}\right|$ is the Euclidean distance between particle $i$ and particle $j$ and $\epsilon_{0}, \sigma_{0}$ specify the energy unit and distance unit in the potential function, respectively. In this example, we take $\epsilon_{0}=1$ and $\sigma_{0}=1$. In a typical equilibrium state which minimizes the potential (22), the cluster of seven particles forms a hexagon. For the system, we are interested in studying the rearrangement process where a particular particle is escaping from the center of the cluster to its surface (Dellago et al., 1998; E et al., 2002). Specifically, we look at particle 1 as the migrating particle during the process. Fig. 8 displays two typical stable configurations of the cluster corresponding to the transition process. We next apply Algorithm 1 to the system for computing a pathway for the transition.

As indicated by the bond-based potential function in Eq. (22), the system is equivalent to any rotation or translation of the cluster, as well as re-indexing of the particles in the system. Based on the properties, we construct a transformation function $\mathcal{T}(x)$ which maps a given configuration $x$ and its equivalent ones to a representative configuration. We incorporate $\mathcal{T}(x)$ into the critic and actor networks to make the learning process reflect the physical properties. The details could be found in Appendix E.

In the example, we solve the path-finding problem (13) over the path space $\mathbb{C}_{\gamma}$ with $\gamma=0.2$ at the temperature $\epsilon=0$. We use the the reinforcement learning algorithm 1 to solve the problem by generating episodes using the policy (16) and training the critic and actor networks.

The identified transition pathway as computed from the actor network $\mu_{\theta}(s)$ is shown in Fig. 9. The results agree well with one transition pathway identified in Ref. (Dellago et al., 1998), which demonstrates that our method is able to predict the transition pathway for the cluster of particles.

## 4. Conclusions

In this work, we proposed a deep reinforcement learning algorithm for computing the transition pathway between the



Figure 9. Plots of eight states along the computed transition pathway for the Lennard-Jones system $((a) \sim(h))$. During the transition process, particle 1 is migrating from the center of the cluster to its surface.

metastable states of dynamical systems. It was demonstrated that the proposed method is able to sample the transition events efficiently and thus to predict the globally optimal transition pathway. We illustrated the ability of the method using three model systems.

The proposed method provides a new perspective for investigating the transition mechanism of systems with rough potential energy surfaces. In the future works, we intend to apply the method to more complex systems. Another direction for future works is to consider the generalized task of predicting the transition pathway for systems with varying or unseen parameters.

## Acknowledgement

The work of B. Lin and W. Ren is partially supported by A*STAR under its AME Programmatic programme: Explainable Physics-based AI for Engineering Modelling \& Design (ePAI) [Award No. A20H5b0142].

## References

Bolhuis, P. G., Chandler, D., Dellago, C., and Geissler, P. L. Transition path sampling: Throwing ropes over rough mountain passes, in the dark. Annu. Rev. Phys. Chem., 53 $(1): 291-318,2002$.

Dellago, C., Bolhuis, P. G., and Chandler, D. Efficient transition path sampling: Application to lennard-jones cluster rearrangements. J. Chem. Phys., 108(22):9236$9245,1998$.

Dellago, C., Bolhuis, P. G., and Geissler, P. L. Transition path sampling. Adv. Chem. Phys., 123:1-78, 2002.

Du, Q., Li, T., Li, X., and Ren, W. The graph limit of the minimizer of the onsager-machlup functional and its
computation. Science China Mathematics, 64:239-280, 2021.

E, W. and Vanden-Eijnden, E. Transition-path theory and path-finding algorithms for the study of rare events. Аппи. Rev. Phys. Chem., 61:391-420, 2010.

E, W., Ren, W., and Vanden-Eijnden, E. String method for the study of rare events. Phys. Rev. B, 66(5):052301, 2002.

E, W., Ren, W., and Vanden-Eijnden, E. Minimum action method for the study of rare events. Commun. Pure Appl. Math., 57(5):637-656, 2004.

E, W., Ren, W., and Vanden-Eijnden, E. Finite temperature string method for the study of rare events. J. Phys. Chem. B, 109(14):6688-6693, 2005.

E, W., Ren, W., and Vanden-Eijnden, E. Simplified and improved string method for computing the minimum energy paths in barrier-crossing events. J. Chem. Phys., 126(16), 2007.

Evans, L., Cameron, M. K., and Tiwary, P. Computing committors in collective variables via mahalanobis diffusion maps. Applied and Computational Harmonic Analysis, $64: 62-101,2023$.

Fischer, S. and Karplus, M. Conjugate peak refinement: an algorithm for finding reaction paths and accurate transition states in systems with many degrees of freedom. Chem. Phys. Lett., 194(3):252-261, 1992.

Fleming, W. H. Exit probabilities and optimal stochastic control. Applied Mathematics and Optimization, 4:329$346,1977$.

Freidlin, M. I. and Wentzell, A. D. Random Perturbations of Dynamical Systems. Springer Press, Berlin, Heidelberg, 2012.

Fujimoto, S., Hoof, H., and Meger, D. Addressing function approximation error in actor-critic methods. In Proceedings of the 35th International Conference on Machine Learning, volume 80, pp. 1587-1596. PMLR, 2018.

Fujisaki, H., Shiga, M., and Kidera, A. Onsager-machlup action-based path sampling and its combination with replica exchange for diffusive and multiple pathways. J. Chem. Phys., 132(13), 2010.

Grafke, T. and Vanden-Eijnden, E. Numerical computation of rare events via large deviation theory. Chaos: An Interdisciplinary Journal of Nonlinear Science, 29(6), 2019.
Guo, J., Gao, T., Zhang, P., Han, J., and Duan, J. Deep reinforcement learning in finite-horizon to explore the most probable transition pathway. Physica D: Nonlinear Phenomena, 458:133955, 2024.

Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In Proceedings of the 35th International Conference on Machine Learning, volume 80, pp. 1861-1870. PMLR, 2018.

Heymann, M. and Vanden-Eijnden, E. The geometric minimum action method: A least action principle on the space of curves. Commun. Pure Appl. Math., 61(8):1052-1117, 2008.

Jónsson, H., Mills, G., and Jacobsen, K. W. Nudged elastic band method for finding minimum energy paths of transitions. In Classical and quantum dynamics in condensed phase simulations, pp. 385-404. World Scientific, 1998.

Khoo, Y., Lu, J., and Ying, L. Solving for high-dimensional committor functions using artificial neural networks. Research in the Mathematical Sciences, 6:1-13, 2019.

Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. In Proceedings of the 3rd International Conference on Learning Representations, 2015.

Li, Q., Lin, B., and Ren, W. Computing committor functions for the study of rare events using deep learning. J. Chem. Phys., 151(5), 2019.

Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D. Continuous control with deep reinforcement learning. arXiv preprint arXiv:1509.02971, 2015.

Maragliano, L., Fischer, A., Vanden-Eijnden, E., and Ciccotti, G. String method in collective variables: Minimum free energy paths and isocommittor surfacesg. J. Chem. Phys., 125(5), 2006.

Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013.

Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., Graves, A., Riedmiller, M., Fidjeland, A. K., Ostrovski, G., Petersen, S., Beattie, C., Sadik, A., Antonoglou, I., King, H., Kumaran, D., Wierstra, D., Legg, S., and Hassabis, D. Human-level control through deep reinforcement learning. Nature, 518(7540): 529-533, 2015.

Olender, R. and Elber, R. Calculation of classical trajectories with a very large time step: Formalism and numerical examples. J. Chem. Phys., 105(20):9299-9315, 1996.

Onsager, L. and Machlup, S. Fluctuations and irreversible processes. Physical Review, 91(6):1505, 1953.

Ren, W., Vanden-Eijnden, E., Maragakis, P., and E, W. Transition pathways in complex systems: Application of the finite-temperature string method to the alanine dipeptide. J. Chem. Phys., 123(13):6688-6693, 2005.

Rotskoff, G. M., Mitchell, A. R., and Vanden-Eijnden, E. Active importance sampling for variational objectives dominated by rare events: Consequences for optimization and generalization. In Mathematical and Scientific Machine Learning, pp. 757-780, 2022.

Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., and Riedmiller, M. Deterministic policy gradient algorithms. In Proceedings of the 31st International Conference on Machine Learning, volume 32, pp. 387-395, 2014.

Voter, A. F. Hyperdynamics: Accelerated molecular dynamics of infrequent events. Phys. Rev. Lett., 78(20):3908, 1997.

Wang, J., Zhang, K., and Wang, E. Kinetic paths, time scale, and underlying landscapes: A path integral framework to study global natures of nonequilibrium systems and networks. J. Chem. Phys., 133(12), 2010.

Zhou, X., Ren, W., and E, W. Adaptive minimum action method for the study of rare events. J. Chem. Phys., 128 (10), 2008.

## A. The path space $\mathbb{C}_{\gamma}$.

Theorem A.1. The set $\bigcup_{\gamma>0} \mathbb{C}_{\gamma}$ is a dense subset of $\bigcup_{T>0} \mathbb{C}_{[0, T]}$.

Proof. For a path $\varphi(t)$ in $\bigcup_{\gamma>0} \mathbb{C}_{\gamma}$ which is continuous and represented by a finite number of line segments, one can easily see that the path is absolute continuous. Thus, $\bigcup_{\gamma>0} \mathbb{C}_{\gamma}$ is a subset of $\bigcup_{T>0} \mathbb{C}_{[0, T]}$.

Suppose $\varphi(t) \in \mathbb{C}_{[0, T]}$ for a number $T>0$. Given $\epsilon>0$, we shall prove that there exists $\gamma>0$ and a $\psi(t) \in \mathbb{C}_{\gamma}$ such that

$$
\max _{t \in[0, T]}|\psi(t)-\varphi(t)|<3 \epsilon
$$

In the following, when we consider a polygonal curve, we assume the time derivative of the curve on each line segment is constant.

Since $\varphi$ is absolute continuous, it is uniformly continuous. Thus, there exists $\delta>0$ such that

$$
\left|\varphi\left(t_{1}\right)-\varphi\left(t_{2}\right)\right|<\epsilon, \quad \forall\left|t_{1}-t_{2}\right|<\delta .
$$

Let $0=t_{0}<t_{1}<\cdots<t_{n}=T$ such that $\left|t_{i}-t_{i-1}\right|<\delta$ and $\varphi\left(t_{i-1}\right) \neq \varphi\left(t_{i}\right)$ for $1 \leqslant i \leqslant n$. Then $\left|\varphi\left(t_{i}\right)-\varphi\left(t_{i-1}\right)\right|<\epsilon$ for $1 \leqslant i \leqslant n$.

We first construct a polygonal curve $\psi_{0}(t), 0 \leqslant t \leqslant T$ such that

$$
\max _{t \in[0, T]}\left|\psi_{0}(t)-\varphi(t)\right|<2 \epsilon
$$

Let $\psi_{0}(t)$ be a polygonal curve with vertices at the times $\left\{t_{i}\right\}_{0 \leqslant i \leqslant n}$ and

$$
\psi_{0}\left(t_{i}\right)=\varphi\left(t_{i}\right), \quad 0 \leqslant i \leqslant n
$$

Then for arbitrary time interval $\left[t_{i-1}, t_{i}\right]$ and $t \in\left[t_{i-1}, t_{i}\right]$, we have

$$
\begin{aligned}
\left|\psi_{0}(t)-\varphi(t)\right| & \leqslant\left|\psi_{0}(t)-\psi_{0}\left(t_{i-1}\right)\right|+\left|\psi_{0}\left(t_{i-1}\right)-\varphi\left(t_{i-1}\right)\right|+\left|\varphi\left(t_{i-1}\right)-\varphi(t)\right| \\
& =\left|\psi_{0}(t)-\psi_{0}\left(t_{i-1}\right)\right|+\left|\varphi\left(t_{i-1}\right)-\varphi(t)\right| \\
& \leqslant\left|\psi_{0}\left(t_{i}\right)-\psi_{0}\left(t_{i-1}\right)\right|+\left|\varphi\left(t_{i-1}\right)-\varphi(t)\right| \\
& =\left|\varphi\left(t_{i}\right)-\varphi\left(t_{i-1}\right)\right|+\left|\varphi\left(t_{i-1}\right)-\varphi(t)\right| \\
& <2 \epsilon .
\end{aligned}
$$

The last inequality is due to the uniform continuity (24) of $\varphi$. Hence, we have proved the inequality (25). Next, we construct a polygonal curve $\psi(t), 0 \leqslant t \leqslant T$ with line segments of uniform length such that

$$
\max _{t \in[0, T]}\left|\psi(t)-\psi_{0}(t)\right|<\epsilon
$$

Denote the length of line segments in $\psi_{0}$ by

$$
\gamma_{i}=\left|\psi_{0}\left(t_{i}\right)-\psi_{0}\left(t_{i-1}\right)\right|, \quad 1 \leqslant i \leqslant n
$$

and the minimum length by

$$
\gamma=\min _{1 \leqslant i \leqslant n}\left|\psi_{0}\left(t_{i}\right)-\psi_{0}\left(t_{i-1}\right)\right| .
$$

Since $\gamma_{i}=\left|\varphi\left(t_{i}\right)-\varphi\left(t_{i-1}\right)\right|>0$, we have $\gamma>0$. By the definition (26) of $\psi_{0}$ and the uniform continuity (24) of $\varphi$, we have $\gamma<\epsilon$. We write the segment length in $\psi_{0}$ as a sum of a multiple of the minimum length and a residual value, i.e.

$$
\gamma_{i}=k_{i} \gamma+2 l_{i}, \quad \text { where } k_{i} \in \mathbb{N}^{*} \text { and } 0 \leqslant 2 l_{i}<\gamma \text {. }
$$

To construct the polygonal curve $\psi$, we first let $\psi\left(t_{i}\right)=\psi_{0}\left(t_{i}\right)$ for $0 \leqslant i \leqslant n$. Then we shall carefully define $\psi$ on each interval $\left[t_{i-1}, t_{i}\right]$ for $1 \leqslant i \leqslant n$.

We first consider the case where $l_{i}>0$. Denote the time slice $\Delta t=t_{i}-t_{i-1}$. Let $\beta$ be a unit vector that is normal to the $i$ th line segment of $\psi_{0}$, i.e.

$$
\left\langle\beta, \psi_{0}\left(t_{i-1}\right)-\psi_{0}\left(t_{i}\right)\right\rangle=0
$$

On the interval $\left[t_{i-1}, t_{i}\right]$, we let the polygon curve $\psi$ to have vertices $\left\{\psi\left(t_{i-1}\right), \psi\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right), \psi\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right), \psi\left(t_{i}\right)\right\}$ where

$$
\begin{aligned}
\psi\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right) & =\psi_{0}\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)+\sqrt{\gamma^{2}-l_{i}^{2}} \beta \\
\psi\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right) & =\psi_{0}\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right)+\sqrt{\gamma^{2}-l_{i}^{2}} \beta
\end{aligned}
$$

The specific form of $\psi$ on $\left[t_{i-1}, t_{i}\right]$ is defined as

$$
\psi\left(t_{i-1}+t\right)= \begin{cases}\psi_{0}\left(t_{i-1}+t\right)+\frac{\gamma_{i} t}{l_{i} \Delta t} \sqrt{\gamma^{2}-l_{i}^{2}} \beta, & t \in\left[0, \frac{l_{i}}{\gamma_{i}} \Delta t\right] \\ \psi_{0}\left(t_{i-1}+t\right)+\sqrt{\gamma^{2}-l_{i}^{2}} \beta, & t \in\left[\frac{l_{i}}{\gamma_{i}} \Delta t, \Delta t-\frac{l_{i}}{\gamma_{i}} \Delta t\right] \\ \psi_{0}\left(t_{i-1}+t\right)+\frac{\gamma_{i}(\Delta t-t)}{l_{i} \Delta t} \sqrt{\gamma^{2}-l_{i}^{2}} \beta, & t \in\left[\Delta t-\frac{l_{i}}{\gamma_{i}} \Delta t, \Delta t\right]\end{cases}
$$

One can verify that the following distance is equal to the minimum length $\gamma$ as defined in Eq. (28),

$$
\begin{aligned}
& \left|\psi\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)-\psi\left(t_{i-1}\right)\right| \\
= & \left|\psi_{0}\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)-\psi_{0}\left(t_{i-1}\right)+\sqrt{\gamma^{2}-l_{i}^{2}} \beta\right| \\
= & \left(\left|\psi_{0}\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)-\psi_{0}\left(t_{i-1}\right)\right|^{2}+\left(\gamma^{2}-l_{i}^{2}\right)\right)^{\frac{1}{2}} \\
= & \left(\left(\frac{l_{i}}{\gamma_{i}} \Delta t \frac{\left|\psi_{0}\left(t_{i}\right)-\psi_{0}\left(t_{i-1}\right)\right|}{\Delta t}\right)^{2}+\left(\gamma^{2}-l_{i}^{2}\right)\right)^{\frac{1}{2}} \\
= & \gamma
\end{aligned}
$$

Similarly, we have

$$
\left|\psi\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right)-\psi\left(t_{i}\right)\right|=\gamma
$$

Also, one can show that the distance between $\psi\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)$ and $\psi\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right)$ is a multiple of $\gamma$,

$$
\begin{aligned}
& \left|\psi\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right)-\psi\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)\right| \\
= & \left|\psi_{0}\left(t_{i}-\frac{l_{i}}{\gamma_{i}} \Delta t\right)-\psi_{0}\left(t_{i-1}+\frac{l_{i}}{\gamma_{i}} \Delta t\right)\right| \\
= & \frac{t_{i}-t_{i-1}-\frac{2 l_{i}}{\gamma_{i}} \Delta t}{\Delta t}\left|\psi_{0}\left(t_{i}\right)-\psi_{0}\left(t_{i-1}\right)\right| \\
= & \frac{\Delta t-\frac{2 l_{i}}{\gamma_{i}} \Delta t}{\Delta t} \gamma_{i} \\
= & k_{i} \gamma .
\end{aligned}
$$

In sum, the curve $\psi$ over $\left[t_{t-1}, t_{i}\right]$ as defined in Eq. (29) is composed of three line segments with the lengths $\gamma, k_{i} \gamma$ and $\gamma$, respectively. One can treat $\psi$ over $\left[t_{t-1}, t_{i}\right]$ as a polygon curve of $k_{i}+2$ line segments with uniform length $\gamma$. Thus, we see that the constructed curve $\psi \in \mathbb{C}_{\gamma}$.

For another case where $l_{i}=0$, we simply set $\psi(t)=\psi_{0}(t), t \in\left[t_{i-1}, t_{i}\right]$. Then $\psi$ over $\left[t_{i-1}, t_{i}\right]$ can be regarded as a polygon curve of $k_{i}$ line segments with uniform length $\gamma$. Also in this case, the constructed curve $\psi \in \mathbb{C}_{\gamma}$.

Moreover, in the latter case $l_{i}=0$, we have $\max _{t \in\left[t_{i-1}, t_{i}\right]}\left|\psi(t)-\psi_{0}(t)\right|=0$. In the case $l_{i}>0$, we have

$$
\max _{t \in\left[t_{i-1}, t_{i}\right]}\left|\psi(t)-\psi_{0}(t)\right|=\left|\sqrt{\gamma^{2}-l_{i}^{2}} \beta\right| \leqslant \gamma<\epsilon
$$

This proves the inequality (27). Therefore, combing the inequality (25) and (27), we find a path $\psi \in \mathbb{C}_{\gamma}$ such that

$$
\begin{aligned}
\max _{t \in[0, T]}|\psi(t)-\varphi(t)| & \leqslant \max _{t \in[0, T]}\left|\psi(t)-\psi_{0}(t)\right|+\max _{t \in[0, T]}\left|\psi_{0}(t)-\varphi(t)\right| \\
& <\epsilon+2 \epsilon \\
& =3 \epsilon
\end{aligned}
$$

## B. Numerical quadratures for approximating the integral in problem (6).

One can use a numerical quadrature with $m$ grid points to approximate the integral as in problem (6), where $m$ is a positive integer. We discretize the time interval $\left[0, h_{i}\right]$ using $m$ uniform points: $t_{j}=(j-1 / 2) / m \cdot h_{i}, 1 \leqslant j \leqslant m$. Denote the position of the path $\varphi^{i}(t)$ at time $t_{j}$ by

$$
z_{i}^{j}=\varphi^{i}\left(t_{j}\right)=z_{i}+\frac{j-1 / 2}{m}\left(z_{i+1}-z_{i}\right), \quad 1 \leqslant j \leqslant m
$$

Then the integral in the problem (6) can be approximated by

$$
\begin{aligned}
\tilde{L}\left(z_{i}, z_{i+1} ; h_{i}\right) & \approx \frac{h_{i}}{m} \sum_{j=1}^{m}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V\left(z_{i}^{j}\right)\right|^{2} \\
& \geqslant 2\left|z_{i+1}-z_{i}\right| \cdot \sqrt{\frac{1}{m} \sum_{j=1}^{m}\left|\nabla V\left(z_{i}^{j}\right)\right|^{2}}+2\left\langle z_{i+1}-z_{i}, \frac{1}{m} \sum_{j=1}^{m} \nabla V\left(z_{i}^{j}\right)\right\rangle
\end{aligned}
$$

where the minimum value is achieved by setting

$$
h_{i}^{*}=\left|z_{i+1}-z_{i}\right| / \sqrt{\frac{1}{m} \sum_{j=1}^{m}\left|\nabla V\left(z_{i}^{j}\right)\right|^{2}}
$$

By setting $m=1$, the cost function (30) reduces to the one in Eq. (7) using the mid-point quadrature as in the paper.

## C. The parameters in Algorithm 1 used for the numerical examples in Section 3.

Table 1. The parameters in Algorithm 1 used for the 2D system, extended Mueller system and Lennard-Jones system of seven particles.

|  | Parameters | 2D system | Mueller system | Lennard-Jones system |
| :---: | :---: | :---: | :---: | :---: |
| க্் | Network structure <br> Activation on hidden layers <br> Activation on output layer <br> $\lambda$ | $4-50-50-1$ <br> $\tanh$ <br> sigmoid <br> 1000 | $20-50-50-1$ <br> $\tanh$ <br> sigmoid <br> 1000 | $24-100-100-1$ <br> $\tanh$ <br> sigmoid <br> 1000 |
|  | Network structure <br> Activation on hidden layers <br> Activation on output layer | $2-50-50-2$ <br> $\quad \tanh$ <br> None | 10-50-50-10 <br> $\quad$ tanh <br> None | 12-100-100-12 <br> tanh <br> None |
|  | $\gamma$ in the path space $\mathbb{C}_{\gamma}$ <br> Numerical quadrature in cost $R_{\epsilon}$ <br> $(M, h)$ in estimating $F_{\epsilon}$ | 0.1 <br> mid-point scheme <br> - | 0.1 <br> mid-point scheme <br> $\left(1000,5 \times 10^{-4}\right)$ | 0.2 <br> mid-point scheme <br> - |
|  | maxstep (\# of training steps) <br> maxtime (maximum length of one episode) <br> \# of episodes per training step <br> Temperature $\epsilon^{\prime}$ for sampling initial states <br> $\left(p_{1}, p_{2}\right)$ in exploration policy <br> Distribution for $\xi_{t}$ in exploration policy <br> step $p_{0}$ for target networks <br> buffer size $N_{R}$ | 700 <br> 50 <br> 50 <br> 0.3 <br> $(1 / 3,1 / 3)$ <br> $\mathcal{N}(0, \pi / 4)$ <br> 10 <br> $10^{5}$ | 1000 <br> 100 <br> 50 <br> 20 <br> $(1 / 3,1 / 3)$ <br> $\mathcal{N}(0, \pi / 4)$ <br> 10 <br> $10^{5}$ | 1000 <br> 100 <br> 100 <br> 0.3 <br> $(1 / 3,1 / 3)$ <br> $\mathcal{N}(0, \pi / 4)$ <br> 10 <br> $10^{6}$ |
| 盘 | Optimizer <br> Learning rate <br> Batch size $\|\mathcal{B}\|$ | Adam <br> $10^{-3}$ <br> 5000 | Adam <br> $10^{-3}$ <br> 5000 | Adam <br> $10^{-3}$ <br> 5000 |

## D. Computing the transition tube for the Mueller system.

For the Mueller system with potential function (21), we define the two metastable set $S_{A}, S_{B}$ with radius $r_{0}$ around the states $A, B$ as

$$
S_{A}=\left\{x \in \mathbb{R}^{10}:\left|\left(x_{1}, x_{2}\right)-\left(A_{1}, A_{2}\right)\right|<r_{0}\right\}, \quad S_{B}=\left\{x \in \mathbb{R}^{10}:\left|\left(x_{1}, x_{2}\right)-\left(B_{1}, B_{2}\right)\right|<r_{0}\right\}
$$

with $r_{0}=0.1$, where $\left(A_{1}, A_{2}\right)$ and $\left(B_{1}, B_{2}\right)$ denote the first two numbers in the coordinates of $A$ and $B$, respectively. The first hitting time of the two sets $S_{A}$ and $S_{B}$ is defined as

$$
\tau_{A}(z)=\inf _{t>0}\left\{x_{t} \in S_{A}: x_{0}=z\right\}, \quad \tau_{B}(z)=\inf _{t>0}\left\{x_{t} \in S_{B}: x_{0}=z\right\}
$$

The committor function $q(x)$ is defined in the configuration space, which is the probability that the system starting from $x$ first arrives in $S_{B}$ rather than $S_{A}$ :

$$
q(x)=\operatorname{Prob}\left[\tau_{A}(x)>\tau_{B}(x)\right]
$$

A mathematical description for the committor function is given by the backward Kolmogorov equation with the Dirichlet boundary conditions:

$$
\left\{\begin{array}{l}
\nabla V(x) \cdot \nabla q(x)-\epsilon \Delta q(x)=0, \quad x \in \Omega \backslash\left(S_{A} \cup S_{B}\right) \\
q(x)=0, x \in \partial S_{A} ; \quad q(x)=1, x \in \partial S_{B}
\end{array}\right.
$$

We compute the committor function $q_{m}\left(x_{1}, x_{2}\right)$ for the 2D Mueller system with the potential $V_{m}\left(x_{1}, x_{2}\right)$ at $\epsilon=10$ by solving the partial differential equation (31) using the finite element method. The computational domain is taken as


Figure 10. Plots of the computed transition tube and its centerline for the potential function $V_{m}\left(x_{1}, x_{2}\right)$ at $\epsilon=10$ with different confidence levels, $\nu=0.68$ (Left) and $\nu=0.95$ (Right). The contour lines indicate the potential function.

$\Omega=[-1.5,1] \times[-0.5,2]$. Then the committor function $q(x)$ for the 10D Mueller system with the potential (21) is given by $q\left(x_{1}, \ldots, x_{10}\right)=q_{m}\left(x_{1}, x_{2}\right)$.

The committor function itself is a good reactive coordinate for describing the transition of the system. As illustrated in Ref. (Ren et al., 2005), the transition tube can be characterized by the iso-committor surfaces of the committor function. For the 10D Mueller system considered in the numerical example, the transition events can be characterized by the transition tube corresponding to the first two dimensions $\left(x_{1}, x_{2}\right)$.

Next, we compute the transition tube for the two-dimensional potential $V_{m}\left(x_{1}, x_{2}\right)$ at $\epsilon=10$. To approximate the isocommittor surfaces, we divide the configuration space into sub-regions using a transition pathway (e.g. the minimum energy path corresponding to the potential $V_{m}\left(x_{1}, x_{2}\right)$ with $\left.\omega=0\right)$. Specifically, the transition pathway $\varphi$ is represented by $N_{p}=185$ states $z_{1}, \ldots, z_{N_{p}} \in \mathbb{R}^{2}$ with equal distance. Denote the committor function $q_{m}\left(x_{1}, x_{2}\right)$ on these points by $q_{i}=q_{m}\left(z_{i}\right), 1 \leq i \leq N_{p}$. Note that $q_{1}<\cdots<q_{N_{p}}$. We approximate the $q_{i}$-isocommittor surface using the region

$$
\Omega_{i}=\left\{\left(x_{1}, x_{2}\right) \in \mathbb{R}^{2}:\left(q_{i-1}+q_{i}\right) / 2<q_{m}\left(x_{1}, x_{2}\right)<\left(q_{i}+q_{i+1}\right) / 2\right\}, \quad 1 \leq i \leq N_{p}
$$

where $q_{0}=-q_{1}$ and $q_{N_{p}+1}=2-q_{N_{p}}$.

We discretize the computational domain $\Omega$ using a mesh with $500 \times 500$ grid points. The set of grid points is denoted by $\left\{X_{k}\right\}_{k \in \mathcal{I}}$. Denote by $\mathcal{I}_{i}$ the indices of the grid points in $\left\{X_{k}\right\}_{k \in \mathcal{I}}$ which locate inside the region $\Omega_{i}$,

$$
\mathcal{I}_{i}=\left\{k \in \mathcal{I}: X_{k} \in \Omega_{i}\right\} \quad 1 \leq i \leq N_{p}
$$

We assign the following Gibbs-Boltzmann weight to each grid point in $\left\{X_{k}\right\}_{k \in \mathcal{I}_{i}}$ in the region $\Omega_{i}$,

$$
w_{k}=\frac{1}{Z_{i}} \exp \left[-\frac{V_{m}\left(X_{k}\right)}{\epsilon}\right], \quad k \in \mathcal{I}_{i}
$$

where the normalization constant $Z_{i}=\sum_{k \in \mathcal{I}_{i}} \exp \left[-V_{m}\left(X_{k}\right) / \epsilon\right]$. The centerline of the transition tube can be represented by the weighted average of the grid points on each region $\Omega_{i}$ :

$$
c_{i}=\sum_{k \in \mathcal{I}_{i}} w_{k} \cdot X_{k}, \quad 1 \leq i \leq N_{p}
$$

To represent the transition tube, we sort the weights and choose a subset $\left\{X_{k}\right\}_{k \in \mathcal{J}_{i}}$ of $\left\{X_{k}\right\}_{k \in \mathcal{I}_{i}}$ containing the least number
of gird points with the largest weights $w_{k}$ such that

$$
\sum_{k \in \mathcal{J}_{i}} w_{k} \geq \nu
$$

where $\nu \in[0,1]$ denotes the confidence level. Then the transition tube is represented by a collection of grid point sets, $\left\{X_{k}\right\}_{k \in \mathcal{J}_{i}}, 1 \leq i \leq N_{p}$.

In Fig. 10, we show the plots of the computed transition tube and its centerline using two different values for $\nu(\nu=0.68$ and $\nu=0.95$ ). In the numerical example, we take $\nu=0.68$, as shown in upper panel of Fig. 7.

## E. Construction of the transformation function $\mathcal{T}(x)$ for the Lennard-Jones system.

Since the Lennard-Jones system is invariant to translation of the particles in the system, we fix the coordinate of particle 1 at the origin, i.e. $y_{1}=(0,0)$ in the example. Thus the system is defined in the 12 -dimensional space with the configuration $x=\left(y_{2}, \ldots, y_{7}\right)$, where $y_{i}$ denotes the coordinate of particle $i$.

Before introducing the transformation function, we define two angle functions as follows.

Definition. The angle $f(u, v) \in[0, \pi]$ between two nonzero vectors $u=\left(u_{1}, u_{2}\right)$ and $v=\left(v_{1}, v_{2}\right)$ in $\mathbb{R}^{2}$ is defined as

$$
f(u, v)=\arccos \left(\frac{\langle u, v\rangle}{|u| \cdot|v|}\right)
$$

Then we define the oriented angle between $u$ and $v$ as

$$
\eta(u, v)= \begin{cases}f(u, v), & \left\langle u^{\prime}, v\right\rangle \geq 0 \\ 2 \pi-f(u, v), & \left\langle u^{\prime}, v\right\rangle<0\end{cases}
$$

where the vector $u^{\prime}=\left(-u_{2}, u_{1}\right)$. Note that $\eta(u, v) \in[0,2 \pi]$.

Next, we construct a transformation function $\mathcal{T}(x)$ for the system in a two-step procedure.

## (1) Rotating the cluster

We compute the mean vector

$$
\bar{y}=\frac{1}{6}\left(y_{2}+\cdots+y_{7}\right)
$$

Let $k$ be the number that solves

$$
k=\underset{2 \leq i \leq 7}{\arg \min } f\left(y_{i}, \bar{y}\right) .
$$

Using the particle $k$, we set the angle

$$
\beta=\eta\left(y_{k}, e_{x}\right)
$$

where $e_{x}$ denotes the unit vector $e_{x}=(1,0)$, and construct the rotation matrix

$$
D_{\beta}=\left[\begin{array}{cc}
\cos \beta & -\sin \beta \\
\sin \beta & \cos \beta
\end{array}\right]
$$

We rotate the cluster with configuration $x$ to $x^{\prime}=\left(y_{2}^{\prime}, \ldots, y_{7}^{\prime}\right)$,

$$
y_{i}^{\prime}=D_{\beta}\left[\begin{array}{l}
y_{i 1} \\
y_{i 2}
\end{array}\right], \quad 2 \leq i \leq 7
$$

where $y_{i}=\left(y_{i 1}, y_{i 2}\right)$ denotes the coordinates of particle $i$. In the new configuration $x^{\prime}$, the particle $k$ is on the $x$-axis.



Figure 11. Illustration of the two-step procedure for the transformation function $\mathcal{T}(x)$ using two example clusters of the Lennard-Jones system.

## (2) Re-indexing the particles

We sort the angles $\left\{\eta\left(e_{x}, y_{i}^{\prime}\right)\right\}, 2 \leq i \leq 7$ of the particles and obtain the particle sequence $\left(y_{\tau(2)}^{\prime}, \ldots, y_{\tau(7)}^{\prime}\right)$, where $(\tau(2), \ldots, \tau(7))$ denote the indices of the sorted particles.

Therefore, the transformation function is defined as: $\mathcal{T}(x)=\left(y_{\tau(2)}^{\prime}, \ldots, y_{\tau(7)}^{\prime}\right)$. In Fig. 11, we use two example clusters of the Lennard-Jones system to illustrate the above procedure for $\mathcal{T}(x)$.

To incorporate the transformation function $\mathcal{T}(x)$ into the critic and actor networks. We compute the critic function $Q_{\theta}$ and actor function $\mu_{\theta}$ at the state $s \in \mathbb{R}^{12}$ and action $a$ which is a unit vector in $\mathbb{R}^{12}$ as follows. We compute $s^{\prime}=\mathcal{T}(s)$ with rotation matrix $D_{\beta}$ and indices $(\tau(2), \ldots, \tau(7))$. Then we compute the transformed action $a^{\prime}$ from $a$ using the same rotation $D_{\beta}$ and index function $\tau$. The critic function at $(s, a)$ is given by $Q_{\theta}\left(s^{\prime}, a^{\prime}\right)$.

Denote $\tilde{a}=\mu_{\theta}\left(s^{\prime}\right)$ and let $\tau^{-1}$ be the inverse function of $\tau$. We compute the transformed action $\tilde{a}^{\prime}$ from $\tilde{a}$ using the rotation $D_{-\beta}$ and index function $\tau^{-1}$. The actor function at $s$ is given by $\tilde{a}^{\prime}$.


[^0]:    ${ }^{1}$ Department of Mathematics, National University of Singapore, 10 Lower Kent Ridge Road 119076, Singapore. Correspondence to: Bo Lin $<$ matboln @ nus.edu.sg $>$, Weiqing Ren $<$ matrw@nus.edu.sg $>$.

