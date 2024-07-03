# 一道 IMO 代数预选题的推广 

何振宇

(华中师范大学第一附属中学, 430223)

我们先看下面一道 IMO 预选题:

题 1. 求最大的实数 $Q$, 使得对于所有正整数 $n$ 和所有实数 $x_{0}, x_{1}, \cdots, x_{n}$ $\left(0=x_{0}<x_{1}<\cdots<x_{n}\right)$, 有

$$
\sum_{i=1}^{n} \frac{1}{x_{i}-x_{i-1}} \geq Q \sum_{i=1}^{n} \frac{i+1}{x_{i}}
$$

(第 57 届 IMO 预选题)

解 $Q_{\max }=\frac{4}{9}$.

一方面, 取 $x_{i}=\sum_{k=1}^{i} k(k+1), i \geq 1$, 则

$$
\begin{gathered}
\sum_{i=1}^{n} \frac{1}{x_{i}-x_{i-1}}=\sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{n+1} \\
\sum_{i=1}^{n} \frac{i+1}{x_{i}}=\sum_{i=1}^{n} \frac{3}{i(i+2)}=\frac{9}{4}-\frac{3}{2}\left(\frac{1}{n+1}+\frac{1}{n+2}\right) .
\end{gathered}
$$

这样, 要使原不等式成立, 必须

$$
Q \leq \frac{1-\frac{1}{n+1}}{\frac{9}{4}-\frac{3}{2}\left(\frac{1}{n+1}+\frac{1}{n+2}\right)}, \forall n \in \mathbb{N}^{*}
$$

令 $n \rightarrow+\infty$, 得 $Q \leq \frac{4}{9}$.

另一方面, 只需考虑 $n \geq 2$ 的情况. 由 Cauchy 不等式, 知 $\forall 2 \leq i \leq n$, 有

$$
\frac{9}{x_{i}-x_{i-1}}+\frac{(i-1)^{2}}{x_{i-1}} \geq \frac{(i+2)^{2}}{x_{i}} \text {. }
$$

从而

$$
\begin{aligned}
& 9 \sum_{i=1}^{n} \frac{1}{x_{i}-x_{i-1}}-4 \sum_{i=1}^{n} \frac{i+1}{x_{i}} \\
= & \sum_{i=2}^{n}\left(\frac{9}{x_{i}-x_{i-1}}+\frac{(i-1)^{2}}{x_{i-1}}-\frac{(i+2)^{2}}{x_{i}}\right)+\frac{n^{2}}{x_{n}} \geq 0 .
\end{aligned}
$$

收稿日期: 2018-09-26; 修订日期: 2018-12-13.
即

$$
\sum_{i=1}^{n} \frac{1}{x_{i}-x_{i-1}} \geq \frac{4}{9} \sum_{i=1}^{n} \frac{i+1}{x_{i}}
$$

在研究这道预选题时, 我们发现它与一个递归方程解的存在性等价.

如果存在一个无穷实数序列 $\left\{x_{n}\right\}_{n=1}^{\infty}$ 满足递归方程

$$
x_{n}=f\left(x_{n-1}, \cdots, x_{n-k}\right) \text {, }
$$

其中 $k$ 是某个小于 $n$ 的正整数, 则称递归方程 $(*)$ 在 $\mathbb{R}$ 上有解.

我们首先证明了如下命题:

命题 递归方程

$$
\left\{\begin{array}{l}
b_{1}=c \\
b_{k}=c+\sqrt{b_{k-1}^{2}-k}
\end{array}\right.
$$

在 $\mathbb{R}$ 上有解的充要条件是: 对 $\forall n \in \mathbb{N}^{*}, \forall a_{i} \in \mathbb{R}, i=1,2, \cdots, n$ 有

$$
c^{2} \sum_{i=1}^{n} \frac{1}{a_{i}} \geq \sum_{i=1}^{n} \frac{i+1}{\sum_{k=1}^{i} a_{k}}
$$

注意到上述命题中的递归方程 $b_{k}=c+\sqrt{b_{k-1}^{2}-k}$ 可重写为 $\left(b_{k}-c\right)^{2}=$ $b_{k-1}^{2}-k$. 这启发我们研究更一般的递归方程 $\left(x_{k}-c\right)^{2}=x_{k-1}^{2}-f(k)$ 有解的条件. 因此, 我们建立了如下定理:

定理 设 $c>0, f(x) \in \mathbb{R}[x]$, 且满足 $f(n)>0, \forall n \in \mathbb{N}^{*}$, 则递归方程

$$
\left\{\begin{array}{l}
\Omega_{1}=c \\
\left(\Omega_{n}-c\right)^{2}=\Omega_{n-1}^{2}-f(n)
\end{array}\right.
$$

有解的充要条件是 $f(x)$ 恒为 $\left(0, c^{2}\right]$ 上的常数或 $f(x)=u x+v$, 其中 $u>0, v \geq 0$且满足

$$
\frac{u}{2 \sqrt{u+v}}+\sqrt{u+v} \leq c .
$$

## $\S 1$. 命题的证明

这一节, 我们给出命题的证明.

命题的证明 必要性: 若 (1) 成立, 记 $S_{i}=\sum_{i=1}^{k} a_{k}$, 则由 Cauchy 不等式知, 对 $\forall n \in \mathbb{N}^{*}, a_{i} \in \mathbb{R}^{+}, i=1, \cdots, n$, 有

$$
c^{2} \sum_{i=1}^{n} \frac{1}{a_{i}}-\sum_{i=1}^{n} \frac{i+1}{S_{i}}=\sum_{i=2}^{n}\left(\frac{c^{2}}{a_{i}}+\frac{b_{i-1}^{2}-i}{S_{i-1}}-\frac{b_{i}^{2}}{S_{i}}\right)+\frac{\left(b_{n+1}-c\right)^{2}}{S_{n}}
$$

$$
=\sum_{i=2}^{n}\left(\frac{c^{2}}{a_{i}}+\frac{\left(b_{i}-c\right)^{2}}{S_{i-1}}-\frac{b_{i}^{2}}{S_{i}}\right)+\frac{\left(b_{n+1}-c\right)^{2}}{S_{n}} \geq 0 .
$$

充分性: 重复上节 IMO 预选题的解法, 知 (2) 成立当且仅当 $c \geq \frac{3}{2}$, 下面只需说明 (1) 成立等价于 $c \geq \frac{3}{2}$.

事实上, 假设 $0<c<\frac{3}{2}$.

考虑数列 $\left\{\frac{n+2}{2}\right\}$ (恰是 $c=\frac{3}{2}$ 时的 $\left\{b_{n}\right\}$ ) 与 $\left\{b_{n}\right\}$ 的对应项的差.

注意 $n \geq 2$ 时,

$$
\begin{aligned}
\frac{n+2}{2}-b_{n} & =\frac{n+2}{2}-c-\sqrt{b_{n-1}^{2}-n} \\
& >\frac{n-1}{2}-\sqrt{b_{n-1}^{2}-n} \\
& =\frac{\left(\frac{n-1}{2}\right)^{2}-\left(b_{n-1}^{2}-n\right)}{\frac{n-1}{2}+\sqrt{b_{n-1}^{2}-n}} \\
& =\frac{\left(\frac{n+1}{2}\right)^{2}-b_{n-1}^{2}}{\frac{n-1}{2}+\sqrt{b_{n-1}^{2}-n}} \\
& =\left(\frac{n+1}{2}-b_{n-1}\right) \cdot \frac{\frac{n+1}{2}+b_{n-1}}{\frac{n-1}{2}+\sqrt{b_{n-1}^{2}-n}} .
\end{aligned}
$$

又 $\frac{1+2}{2}-b_{1}=\frac{3}{2}-c>0$, 故对 $n$ 归纳易知 $\frac{n+2}{2}-b_{n}>0, \forall n \in \mathbb{N}^{*}$. 从而 $b_{n-1}>\frac{n+1}{n-1} \cdot \sqrt{b_{n-1}^{2}-n}$. 再利用 (1)式, 知

$$
\frac{n+2}{2}-b_{n}>\frac{n+1}{n-1}\left(\frac{n+1}{2}-b_{n-1}\right), \forall n \geq 2 .
$$

进而

$$
\frac{n+2}{2}-b_{n}>\prod_{k=2}^{n} \frac{k+1}{k-1}\left(\frac{3}{2}-c\right)=\frac{n(n+1)}{2}\left(\frac{3}{2}-c\right), \forall n \geq 2 .
$$

取 $n \in \mathbb{N}^{*}$ 使 $\frac{1}{n_{0}}+\frac{1}{n_{0}\left(n_{0}+1\right)} \leq \frac{3}{2}-c$, 则 $b_{n_{0}}<0$. 但

$$
b_{n_{0}}=c+\sqrt{b_{n_{0}-1}^{2}-n_{0}} \geq c>0,
$$

矛盾! 这说明 (1) 成立, 必须 $c \geq \frac{3}{2}$.

另一方面, 若 $c \geq \frac{3}{2}$, 则对 $n$ (加强) 归纳可证 $\left\{b_{t}\right\}_{t-1}^{n}$ 存在, 且 $b_{n} \geq \frac{1}{2} n+1$. 所以此时 (1) 成立.

综上, 充分性得证.

## $\S 2$. 定理的证明

定理的证明 (i) 当 $\operatorname{deg} f=0$ 时, 设 $f$ 恒等于 $\mu$ ( $\mu$ 是正常数). 则

$$
\left(\Omega_{n}-c\right)^{2}=\Omega_{n-1}^{2}-\mu, \forall n>1
$$

有解的充要条件是 $\Omega_{n-1} \geq \sqrt{\mu}$.
特别地, $\Omega_{2}$ 存在的充要条件是 $\Omega_{1} \geq \sqrt{\mu}$, 即 $c \geq \sqrt{\mu}$. 而 $c \geq \sqrt{\mu}$ 时, 对 $n$ 归纳易证 $\{\Omega\}_{n=1}^{+\infty}$ 存在. 因此 $f$ 恒等于 $\mu$ ( $\mu$ 是正常数) 对 $\{\Omega\}_{n=1}^{+\infty}$ 存在的充要条件是 $c \geq \sqrt{\mu}$.

(ii) 当 $\operatorname{deg} f \in \mathbb{N}^{*}$ 时, 因为 $f(n)>0, \forall n>0$, 故 $f(x)$ 的首项系数大于 0 , 因此存在 $x_{0}>0$, 使 $f^{\prime}(x)>0, \forall x \geq x_{0}$. 从而存在 $n_{0} \in \mathbb{N}^{*}, n_{0}>1$ 使得

$$
f(n+1) \geq f(n), \forall n \geq n_{0}
$$

假设存在 $n_{1} \geq n_{0}$, 使 $\Omega_{n_{1}} \leq \Omega_{n_{1}-1}$, 则

$$
\left(\Omega_{n_{1}+1}-c\right)^{2}-\left(\Omega_{n_{1}}-c\right)^{2}=\Omega_{n_{1}}^{2}-\Omega_{n_{1}-1}^{2}-\left(f\left(n_{1}+1\right)-f\left(n_{1}\right)\right) \leq 0,
$$

即 $\Omega_{n_{1}+1} \leq \Omega_{n_{1}}$. 从而

$$
\Omega_{n_{1}-1} \geq \Omega_{n_{1}} \geq \Omega_{n_{1}+1} \geq \cdots
$$

由 $f(x)$ 的首项系数大于 0 , 知存在 $\alpha \geq n_{1}, \alpha \in \mathbb{N}^{*}$ 使 $f(\alpha)>\Omega_{n_{1}-1}^{2}$, 那么 $f(\alpha)>\Omega_{\alpha}^{2}$, 于是

$$
0>\Omega_{\alpha}^{2}-f(\alpha)=\left(\Omega_{\alpha+1}-c\right)^{2}
$$

矛盾! 从而 $\Omega_{n} \geq \Omega_{n-1}, \forall n \geq n_{0}$. 进而

$$
\Omega_{n-1}^{2}-f(n)=\left(\Omega_{n}-c\right)^{2} \geq\left(\Omega_{n-1}-c\right)^{2} \Rightarrow \Omega_{n-1} \geq \frac{1}{2 c}\left(c^{2}+f(n)\right), \forall n \geq n_{0}
$$

但

$$
\left(\Omega_{n}-c\right)^{2}=\Omega_{n-1}^{2}-f(n)<\Omega_{n-1}^{2} \Rightarrow \Omega_{n}<\Omega_{n-1}+c, \forall n>1,
$$

又 $\Omega_{1}=c$, 故 $\Omega_{n} \leq n c, \forall n \geq 1$. 于是

$$
(n-1) c \geq \Omega_{n-1} \geq \frac{1}{2 c}\left(c^{2}+f(n)\right), \forall n \geq n_{0} \Rightarrow \operatorname{deg} f=1 \text {. }
$$

设 $f(x)=u x+v$, 则 $u>0, v \geq 0$. 记

$$
S_{n}=\frac{u}{2 \sqrt{u+v}} n+\sqrt{u+v}, \forall n \in \mathbb{N}^{*}
$$

假设 $0<c<S_{1}$, 则 $S_{1}>\Omega_{1}$, 且

$$
\left(S_{n}-c\right)^{2}>\left(S_{n}-S_{1}\right)^{2}=\frac{u^{2}}{4(u+v)}(n-1)^{2}=S_{n-1}^{2}-f(n),
$$

从而

$$
\begin{aligned}
S_{n}-\Omega_{n} & =S_{n}-c-\left(\Omega_{n}-c\right)>\sqrt{S_{n-1}^{2}-f(n)}-\sqrt{\Omega_{n-1}^{2}-f(n)} \\
& =\left(S_{n-1}^{2}-\Omega_{n-1}^{2}\right) \cdot \frac{1}{\sqrt{S_{n-1}^{2}-f(n)}+\sqrt{\Omega_{n-1}^{2}-f(n)}} \\
& =\left(S_{n-1}-\Omega_{n-1}\right) \frac{S_{n-1}+\Omega_{n-1}}{\sqrt{S_{n-1}^{2}-f(n)}+\sqrt{\Omega_{n-1}^{2}-f(n)}}, \forall n>1 .
\end{aligned}
$$

又 $S_{1}>\Omega_{1}$, 故对 $n$ 归纳易证 $S_{n}>\Omega_{n}, \forall n \in \mathbb{N}^{*}$. 进一步, 有

$$
\begin{aligned}
& \frac{\Omega_{n}}{\sqrt{\Omega_{n}^{2}-f(n+1)}}>\frac{S_{n}}{\sqrt{S_{n}^{2}-f(n+1)}} \\
\Rightarrow & \frac{S_{n}+\Omega_{n}}{\sqrt{S_{n}^{2}-f(n+1)}+\sqrt{\Omega_{n}^{2}-f(n+1)}}>\frac{S_{n}}{\sqrt{S_{n}^{2}-f(n+1)}} \\
= & \frac{\frac{u}{2 \sqrt{u+v}} n+\sqrt{u+v}}{\frac{u}{2 \sqrt{u+v}} n}=1+\frac{2 u+2 v}{u} \cdot \frac{1}{n},
\end{aligned}
$$

结合 (5) 知,

$$
\begin{aligned}
& \frac{S_{n+1}-\Omega_{n+1}}{S_{n}-\Omega_{n}}>1+\frac{2 u+2 v}{u} \frac{1}{n} \geq 1+\frac{2}{n}, \forall n \in \mathbb{N}^{*} \\
\Rightarrow & S_{n}-\Omega_{n}>\prod_{k=1}^{n-1}\left(1+\frac{2}{k}\right)\left(S_{1}-\Omega_{1}\right)=\frac{n(n+1)}{2}\left(S_{1}-c\right), \forall n>1,
\end{aligned}
$$

于是

$$
\Omega_{n}<S_{n}-\frac{n(n+1)}{2}\left(S_{1}-c\right), \forall n>1
$$

注意右边是关于 $n$ 的首项系数为负的二次函数, 故存在 $n \in \mathbb{N}^{*}$, 使

$$
S_{n}-\frac{h(h+1)}{2}\left(S_{1}-c\right)<0,
$$

所以 $\Omega_{n}<0$, 矛盾! 因此 $c \geq S_{1}$.

当 $c \geq S_{1}$ 时, 对 $m$ 归纳可证存在 $\left\{\Omega_{n}\right\}_{n=1}^{m}$, 且 $\Omega_{m} \geq S_{m}$. 故 $\left\{\Omega_{n}\right\}_{n=1}^{+\infty}$ 存在.

综上所述, 递归方程有解的充要条件是 $f(x)=\mu\left(\mu \in\left(0, c^{2}\right]\right)$ 或 $f(x)=$ $u x+v\left(u>0, v \geq 0\right.$ 满足 $\left.\frac{u}{2 \sqrt{u+v}}+\sqrt{u+v} \leq c\right)$.

