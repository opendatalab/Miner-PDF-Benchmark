# 一类函数方程的演变 

汤继尧

(湖南省雅礼中学, 410007)

数学问题的提出和推广经常是从简单到复杂的一个演变过程. 本文介绍一个实例, 即展示一个简单函数问题发展到一般问题的过程. 先看下面的简单问题:

问题 1. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 使得对 $\forall x, y \in \mathbf{N}^{*}$, 均有 $x y \mid f(x) f(y)$.

解 对 $\forall x \in \mathbf{N}^{*}$, 由条件得 $x^{2} \mid(f(x))^{2}$, 所以 $x \mid f(x)$. 故 $f(x)=x h(x)$, 其中的 $h(x)$ 是 $\mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$ 上的函数.

经检验, 这样的 $f$ 符合题意.

问题 1 似乎有点平凡, 条件要求较弱, 这诱发我们改变一下问题的条件, 从而产生了下面的问题 2:

问题 2. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 使得对 $\forall x, y \in \mathbf{N}^{*}$, 均有

$$
x y \mid f(x) f(y)-1 \text {. }
$$

问题 2 似乎不太简单 (因为有些同学做的不太顺利). 下面介绍问题 2 的两种解法.

解法 1. 因为对 $\forall x, y \in \mathbf{N}^{*}$, 均有 $x y \mid f(x) f(y)-1$. 所以 $(y, f(x))=1$. 由 $y$ 的任意性知 $f(x)=1$. 经检验, $f(x)=1$ 符合题意, 故问题的解为 $f(x)=1$.

解法 2. 由于对 $\forall x, y_{1}, y_{2} \in \mathbf{N}^{*}$, 均有

$$
x\left|f(x) f\left(y_{1}\right)-1, \quad x\right| f(x) f\left(y_{2}\right)-1,
$$

所以 $x \mid f\left(y_{1}\right)-f\left(y_{2}\right)$ 对 $\forall x \in \mathbf{N}^{*}$ 成立. 因而有 $f\left(y_{1}\right)=f\left(y_{2}\right)$ 对 $\forall y_{1}, y_{2} \in \mathbf{N}^{*}$都成立. 故 $f(x)$ 为定值, 记为 $S(S>0)$. 即 $x^{2} \mid S^{2}-1$ 对 $\forall x \in \mathbf{N}^{*}$ 成立, 故

收稿日期: 2017-01-11； 修订日期: 2017-04-18;
$S=1$, 即 $f(x)=1$, 经检验, 符合题意.

利用问题 2 的解法 1 , 我们提出并解决了下面的问题 3:

问题 3. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 使得对 $\forall x, y \in \mathbf{N}^{*}$, 均有

$$
f(x) f(y) \mid(f(x)-y)(f(y)-x)-1 .
$$

问题 3 的解答与问题 2 的解法 1 类似, 本文省略不写.

随后我们将问题 3 在形式上稍加改变, 得到了下面的问题 4:

问题 4. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 使得对 $\forall x, y \in \mathbf{N}^{*}$, 均有

$$
f(x) f(y) \mid(f(x)-x)(f(y)-y)-1 .
$$

通过分析知, 问题 2 的解法 1 对问题 4 并不适用, 但解法 2 是可以发展借用的. 下面是我最初找到的问题 4 的解法.

解 对函数值域分两种情况讨论.

(i) 若 $f$ 的值域为无限集. 则对 $\forall x, y_{1}, y_{2} \in \mathbf{N}^{*}$, 均有

$$
\begin{aligned}
& f(x) \mid(f(x)-x)\left(f\left(y_{1}\right)-y_{1}\right)-1, \\
& f(x) \mid(f(x)-x)\left(f\left(y_{2}\right)-y_{2}\right)-1,
\end{aligned}
$$

于是 $f(x) \mid\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}\right)-y_{2}\right)$.

又因为 $f$ 的值域为无限集, 所以 $f\left(y_{1}\right)-y_{1}=f\left(y_{2}\right)-y_{2}$, 否则取

$$
f(x)>\left|\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}-y_{2}\right)\right)\right|,
$$

矛盾. 故 $f(x)-x$ 为定值, 记为 $S$. 则对 $\forall x \in \mathbf{N}^{*}$, 均有 $(f(x))^{2} \mid S^{2}-1$, 因此 $S= \pm 1$. 但由于 $f(1)>0=1-1$, 所以 $S \neq-1$. 故 $S=1$, 即 $f(x)=x+1$.

(ii) 若 $f$ 的值域为有限集. 记 $T$ 为所有 $f(x)\left(x \in \mathbf{N}^{*}\right)$ 的最小公倍数, 则由条件知 $f(T) \mid(f(T)-T)^{2}-1$, 从而有 $f(T) \mid T^{2}-1$. 又由于 $f(T) \mid T$, 因此 $f(T)=1$.

此外, 对 $\forall x, y_{1}, y_{2} \in \mathbf{N}^{*}$, 同 (i) 可知

$$
f(x) \mid\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}\right)-y_{2}\right),
$$

从而

$$
T \mid\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}\right)-y_{2}\right) .
$$

故

$$
f(x)-x \equiv f(T)-T \equiv 1 \quad(\bmod T)
$$

记 $f(x)=h(x) T+x+1$ (其中 $h(x) \in \mathbf{Z}$ ). 对 $\forall x+1 \leq T, x \in \mathbf{N}^{*}$, 因为

$$
h(x) T+x+1=f(x) \mid(f(x)-x)(f(T)-T)-1,
$$

从而有

$$
h(x) T+x+1=f(x) \mid x+1 .
$$

又因为 $h(x) T+x+1=f(x)>0,1<x+1 \leq T$, 所以

$$
h(x) \geq 0,
$$

同时又有 $x+1 \geq f(x)=h(x) T+x+1$, 即

$$
h(x) \leq 0
$$

综合 (1), (2) 得, $h(x)=0$. 故对 $\forall x+1 \leq T$, 都有 $f(x)=x+1$.

若 $T \geq 3$, 则 $f(T-2)=T-1$. 由 $f(T) \mid T$ 知 $T-1 \mid T$. 由 $T \geq 3$ 知矛盾!所以 $T=1$ 或 2 .

若 $T=2$, 由 $f(x) \equiv x+1(\bmod T)$ 知, 当 $x$ 为奇数时, $f(x)=2$. 特别地, $f(1)=f(3)=2$. 于是, $f(1) f(3) \mid(f(1)-1)(f(3)-3)-1$, 即 $4 \mid-2$, 矛盾.

从而 $T=1$, 即 $f(x)=1$.

综上所述, $f(x)=x+1$ 或 $f(x)=1$.

然而在讨论此题时, 有同学告诉我, 可取 $x=y=1$, 则

$$
f^{2}(1) \mid(f(1)-1)^{2}-1=f^{2}(1)-2 f(1),
$$

故 $f(1)=1$ 或 2 . 然后对 $f(1)$ 的值进行讨论可很好地解决此问题. 这诱发我们对问题 4 进行改造, 以避开首先讨论初始值的做法. 首先想到的改造方式是:

问题 5. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 使得对 $\forall x, y \in \mathbf{N}^{*}$, 均有

$$
f(x) \mid(f(x)-x)(f(y)-y)-1 .
$$

然而这样的改造提醒了题的解法思路, 太直白. 故我采取了另一种改造方式:

问题 6. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 存在 $N_{0} \in \mathbf{N}^{*}$, 使得对 $\forall x, y \in \mathbf{N}^{*}$,
$x y \geq N_{0}$, 均有

$$
f(x) f(y) \mid(f(x)-x)(f(y)-y)-1 .
$$

解 对函数值域分两种情况讨论.

(i) 若 $f$ 的值域为无限集. 则对 $\forall x \in \mathbf{N}^{*} \cap\left[N_{0},+\infty\right), y_{1}, y_{2} \in \mathbf{N}^{*}$, 均有

$$
\begin{aligned}
& f(x) \mid(f(x)-x)\left(f\left(y_{1}\right)-y_{1}\right)-1 \\
& f(x) \mid(f(x)-x)\left(f\left(y_{2}\right)-y_{2}\right)-1 .
\end{aligned}
$$

于是 $f(x) \mid\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}\right)-y_{2}\right)$.

因为 $f$ 的值域为无限集, 所以 $f\left(y_{1}\right)-y_{1}=f\left(y_{2}\right)-y_{2}$. 故 $f(x)-x$ 为定值,记为 $S$. 则对 $\forall x \in \mathbf{N}^{*} \cap\left[N_{0},+\infty\right)$, 均有 $f(x) \mid S^{2}-1$. 所以 $S= \pm 1$. 又由于 $f(1)>0=1-1$, 于是 $S=1$, 故 $f(x)=x+1$.

(ii) 若 $f$ 的值域为有限集. 记 $T$ 为所有 $f(x)\left(x \in \mathbf{N}^{*}\right)$ 的最小公倍数. 取 $k \in \mathbf{N}^{*}, k T \geq N_{0}$, 则有 $f(k T) \mid(k T)^{2}-1$. 又因为 $f(k T) \mid T$, 所以 $f(k T)=1$.

此外, 对 $\forall x \in \mathbf{N}^{*}, y_{1}, y_{2} \in\left[N_{0},+\infty\right) \cap \mathbf{N}^{*}$, 均有

$$
\begin{aligned}
& f(x) \mid(f(x)-x)\left(f\left(y_{1}\right)-y_{1}\right)-1 \\
& f(x) \mid(f(x)-x)\left(f\left(y_{2}\right)-y_{2}\right)-1
\end{aligned}
$$

于是,

$$
f(x) \mid\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}\right)-y_{2}\right),
$$

因此,

$$
T \mid\left(f\left(y_{1}\right)-y_{1}\right)-\left(f\left(y_{2}\right)-y_{2}\right) .
$$

即对 $\forall x \in \mathbf{N}^{*}, x \geq N_{0}$, 均有

$$
f(x)-x \equiv f(k T)-k T \equiv 1 \quad(\bmod T) .
$$

所以, 当 $x \geq N_{0}$ 时,

$$
f(x) \equiv x+1 \quad(\bmod T)
$$

令 $p \geq T+1$ 的素数, 于是,

$$
f(p-1) \mid(f(p-1)-p+1)(f(k T)-k T)-1 .
$$

因此 $f(p-1) \mid p$. 又由于 $p$ 是素数, 所以 $f(p-1)=1$ 或 $p$.
再者, 因为 $p>T \geq f(p-1)$, 所以,

$$
f(p-1)=1
$$

由 Dirichlet 定理知, $S=\left\{n T+(T-1) \mid n \in \mathbf{N}^{*}\right\}$ 中存在无穷多个素数.

令 $p \in S, p \geq T+1, p$ 为素数. 由 $(2)$ 知 $f(p-1)=1$, 由 (1) 知 $f(p-1) \equiv$ $p-1+1(\bmod T)$, 所以 $T|p-1, T| 2$. 于是 $T=1$ 或 2 .

若 $T=2$, 由 $f(x) \equiv x+1(\bmod T)$, 取 $x_{1}=4 N_{0}+1, x_{2}=4 N_{0}+3$. 则 $f\left(x_{1}\right)=f\left(x_{2}\right)=2$. 由题意可知,

$$
\begin{aligned}
& f\left(x_{1}\right) f\left(x_{2}\right) \mid\left(f\left(x_{1}\right)-x_{1}\right)\left(f\left(x_{2}\right)-x_{2}\right)-1 \\
\Leftrightarrow & 4 \mid\left(2-4 N_{0}-1\right)\left(2-4 N_{0}-3\right)-1 \\
\Leftrightarrow & 4 \mid\left(4 N_{0}\right)^{2}-2,
\end{aligned}
$$

矛盾. 故 $T=1$, 即 $f(x)=1$.

综上所述, $f(x)=x+1$ 或 $f(x)=1$.

我们认为, 问题 6 已是一个具有较高难度的新的函数问题. 至此我们完成了一次有趣的问题探索演化之旅.

