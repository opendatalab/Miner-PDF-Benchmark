# $\mathrm{KöMaL}$ 征解问题 A. 769 的一个解答 

李逸凡<br>(上海市上海中学, 200231)<br>指导教师: 王广廷

匈牙利数学杂志 $\mathrm{KöMaL}$ 在 2020 年 2 月的一道征解问题如下:
A. 769 求所有由不同的正整数组成的三元数组 $(a, b, c)$, 满足存在一个由正整数组成的集合 $S$, 使得对于任意正整数 $n$ 都有 $a n, b n, c n$ 三个整数中有且仅有一个属于 $S$.

证明 先证明如下引理:

引理 给定 $(\alpha, \beta)=1,1 \leq \alpha \leq \beta$, 若对任意充分大的 $n$, 可将 $1, \cdots, n$ 染色, 使对任意 $1 \leq x \leq n-\beta$ 均有 $x, x+\alpha, x+\beta$ 中恰一个被染色, 则 $0, \alpha, \beta$ 构成 $\bmod 3$ 完系.

引理证明 取 $n>2^{\beta}+\beta$.

考虑 $(x, \cdots, x+\beta-1)(x=1, \cdots, n-\beta+1)$. 由于染色情况至多只有 $2^{\beta}$种,

因此 $\exists 1 \leq x<y \leq n-\beta+1$ 使 $(x, \cdots, x+\beta-1)$ 与 $(y, \cdots, y+\beta-1)$ 染色情况相同(即 $x+t$ 与 $y+t$ 同时被染或不被染 $t=0, \cdots, \beta-1$ ).

设 $x, \cdots, y-1$ 中有 $u$ 个数被染色. 定义

$$
f_{1}(t)=\left\{\begin{array}{ll}
0, & t \text { 未被染色 } \\
1, & t \text { 被染色 }
\end{array} \quad(x \leq l \leq y-1) .\right.
$$

定义 $f(t)=f_{1}(l)($ 这里 $t \equiv l(\bmod y-x))$ 且 $\left.x \leq l \leq y-1\right)$, 则当 $x \leq t \leq y-1$时

$$
f(t)+f(t+\alpha)+f(t+\beta)=1 .
$$[^0]因此

$$
\begin{aligned}
y-x & =\sum_{t=x}^{y-1} f(t)+f(t+\alpha)+f(t+\beta) \\
& =\sum_{t=x}^{y-1} f(t)+\sum_{t=x+\alpha}^{y-1+\alpha} f(t)+\sum_{t=x+\beta}^{y-1+\beta} f(t) \\
& =3 u .
\end{aligned}
$$

当 $t \in \mathbb{Z}$ 时 $\exists l$ 使 $t \equiv l(\bmod y-x)$ 且 $x \leq l \leq y-1$, 则

$$
f(t)+f(t+\alpha)+f(t+\beta)=f(l)+f(l+\alpha)+f(l+\beta)=1 .
$$

若存在 $t$ 使 $f(t)=f(t+\alpha)=f(t+2 \alpha)=0$, 则有

$$
f(t+\beta)=1, f(t+\alpha+\beta)=1 .
$$

这是因为

$$
f(t)+f(t+\alpha)+f(t+\beta)=1, f(t+\alpha)+f(t+2 \alpha)+f(t+\alpha+\beta)=1 .
$$

而这与

$$
f(t+\beta)+f(t+\alpha+\beta)+f(t+2 \beta)=1
$$

矛盾. 所以

$$
f(t)+f(t+\alpha)+f(t+2 \alpha) \geq 1, \quad t \in \mathbb{Z}
$$

此时

$$
\begin{aligned}
y-x & =\sum_{t=x}^{y-1} f(t)+f(t+\alpha)+f(t+2 \alpha) \\
& \geq 3 u=y-x \quad \Rightarrow \text { 只能取等. }
\end{aligned}
$$

故

$$
f(t)+f(t+\alpha)+f(t+2 \alpha)=1, \quad \forall t=x, \cdots, y-1
$$

即

$$
f(t)+f(t+\alpha)+f(t+2 \alpha)=1, \quad \forall t \in \mathbb{Z}
$$

因此

$$
f(t)=f(t+3 \alpha), \quad \forall t \in \mathbb{Z}
$$

同理

$$
f(t)=f(t+3 \beta), \quad \forall t \in \mathbb{Z}
$$

取 $s, t \in \mathbb{Z}$ 使 $\alpha s-\beta t=1$. 则

$$
f(t)=f(t+3 \alpha s)=f(t+3 \alpha s-3 \beta t)=f(t+3) .
$$

再结合 $f(t)+f(t+\alpha)+f(t+\beta)=1$, 可得 $0, \alpha, \beta$ 构成 $\bmod 3$ 完系.

回到原题. 不妨设 $a=\min \{a, b, c\}$. 记

$$
q_{1}=\frac{b}{a}, q_{2}=\frac{c}{a}
$$

则 $q_{1}, q_{2}$ 为正有理数.

$1^{\circ}$ 若不存在 $\alpha, \beta \in \mathbb{Z}^{+}$使 $q_{1}^{\alpha}=q_{2}^{\beta}$.

考虑 $a, b, c$ 的所有不同素因子 $p_{1}, \cdots, p_{l}$, 则由素因子唯一分解定理. 可设

$$
q_{1}=p_{1}^{\alpha_{1}} \cdots p_{l}^{\alpha_{l}}, q_{2}=p_{1}^{\beta_{1}} \cdots p_{l}^{\beta_{l}}, \quad\left(\alpha_{i}, \beta_{i} \in \mathbb{Z}\right)
$$

则 $\left(\alpha_{1} \cdots \alpha_{l}\right)$ 与 $\left(\beta_{1} \cdots \beta_{l}\right)$ 线性无关. 因此必存在 $1 \leq i<j \leq l$ 使 $\alpha_{i} \beta_{j} \neq \alpha_{j} \beta_{i}$.记 $S_{1}$

为除了 $P_{i}$ 与 $P_{j}$ 之外的所有素数与 $q_{1}, q_{2}$ 构成的集合, 则每个正整数均可唯一地写成 $n=q_{1}^{\theta_{1}} q_{2}^{\theta_{2}} \cdots q_{i}^{\theta_{i}}$ 的形式(其中 $q_{1}, \cdots, q_{t}$ 为 $S_{1}$ 中的不同元素, $\theta_{1}, \cdots, \theta_{t}$ 为有理数), 并记 $f_{1}(n)=\theta_{1}-\theta_{2}$. 若 $q_{1} n, q_{2} n$ 均为正整数, 则 $f_{1}\left(q_{1} n\right)=$ $f_{1}(n)+1, f_{1}\left(q_{2} n\right)=f_{1}(n)-1$. 构造 $S: n \in S$ 当且仅当 $f_{1}(n) \in \underset{k \in \mathbb{Z}}{\cup}[3 k, 3 k+1)$,则对任意正整数 $n$,

$$
f_{1}(b n)=f_{1}(a n)+1, f_{1}(c n)=f_{1}(a n)-1 .
$$

由此知 $a n, b n, c n$ 中恰有一个在 $S$ 中.

$2^{\circ}$ 若存在 $\alpha, \beta \in \mathbb{Z}^{+}$使 $q_{1}^{\alpha}=q_{2}^{\beta}$ 可设 $(\alpha, \beta)=1$, 则 $q=\sqrt[\beta]{q_{1}}$, 为有理数. 记 $q=\frac{u}{v}$ 且 $(u, v)=1, u, v \in \mathbb{Z}^{+}$.

若 $0, \alpha, \beta$ 取遍 $\bmod 3$ 完系. 取 $p \mid u v$ 记 $v_{p}(q)=r$ 则 $r \in \mathbb{Z}$ 且 $r \neq 0$. 构造 $S: n \in S$ 当且仅当 $v_{p}(n)$ 模 $3 r$ 余 0 或 1 或 $\cdots$ 或 $r-1$, 则对任意 $n \in \mathbb{Z}^{+}$,

$$
\begin{aligned}
& v_{p}(b n)=v_{p}(a n)+\beta r \\
& v_{p}(c n)=v_{p}(a n)+\alpha r .
\end{aligned}
$$

在 $\bmod 3 r$ 意义下

$$
\left\{v_{p}(a n), v_{p}(b n), v_{p}(c n)\right\}=\left\{v_{p}(a n), v_{p}(a n)+r, v_{p}(a n)+2 r\right\} .
$$

所以 $a n, b n, c n$ 中恰有一个在 $S$ 中.

若 $0, \alpha, \beta$ 不构成 $\bmod 3$ 完系. 不妨设 $\alpha<\beta$. 假设存在这样的 $S$, 对 $\forall m$ 可取 $n \in \mathbb{Z}$, 使 $n, n \cdot q, \cdots, n \cdot q^{m-1}$ 均为 $a$ 的倍数, 则对 $\forall t \in\{0,1, \cdots, m-$
$1\}, n \cdot q^{t}, n \cdot q^{\alpha+t}, n \cdot q^{\beta+t}$ 中恰一个在 $S$ 中. 因此可对 $0, \cdots, m-1+\beta$ 进行染色, 使 $t, t+\alpha, t+\beta$ 中恰一个被染色, 由引理可知矛盾.

综上, 若不存在 $\alpha, \beta \in \mathbb{Z} \backslash\{0\}$ 使 $\left(\frac{b}{a}\right)^{\alpha}=\left(\frac{c}{a}\right)^{\beta}$, 则 $S$ 存在. 若存在 $\alpha, \beta \in$ $\mathbb{Z} \backslash\{0\}$ 使 $\left(\frac{b}{a}\right)^{\alpha}=\left(\frac{c}{a}\right)^{\beta}$, 则可设 $(\alpha, \beta)=1$, 当 $0, \alpha, \beta$ 构成 $\bmod 3$ 完系时存在,否则不存在.

评注 这道题主要有两个难点. 其一是意识到本题与 $a, b, c$ 本身无关, 而只与 $a, b, c$ 之间的比例有关, 并着手从 $\log _{\frac{b}{a}} \frac{c}{a}$ 是否为有理数进行讨论. 其二是最后一种情况的证明, 这需要一些探索. 在这里笔者发现 “连续的” 的三个数不能同时属于 $S$, 这会导致 $S$ 中的数 “过多” 进而得出矛盾.


[^0]:    修订日期: 2020-03-29.

