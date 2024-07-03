# $\mathrm{KöMaL}$ 征解问题 A. 769 的另解 

尹顺王琇<br>(湖南师范大学附属中学, 410006)<br>指导教师: 汤礼达

匈牙利数学杂志 $\mathrm{KöMaL}$ 在 2020 年 2 月的一道征解问题如下:
A. 769 求所有由不同的正整数组成的三元数组 $(a, b, c)$, 满足存在一个由正整数组成的集合 $S$, 使得对于任意正整数 $n$ 都有 $a n, b n, c n$ 三个整数中有且仅有一个属于 $S$.

李逸凡给出了这个问题的一个解答, 这里我们再给出另外一种解.

解 设集合

$$
T=\{(d x, d y, d z) \mid x, y, z, d \in \mathbb{Z}, d \geq 0, x+y+z=0 \text { 且 } 3 \nmid x y z\} .
$$

我们证明 $(a, b, c)$ 满足题意当且仅当关于 $x, y, z$ 的不定方程组

$$
\left\{\begin{array}{l}
a^{x} b^{y} c^{z}=1, \\
x+y+z=0,
\end{array} \quad x, y, z \in \mathbb{Z},\right.
$$

的解集含于 $T$.

必要性: 先证明如下引理.

引理 $\quad$ 若 $u \in S, a b c \mid u$, 则正整数

$$
u \frac{a^{2}}{b c}, u \frac{b^{2}}{a c}, u \frac{c^{2}}{a b} \in S
$$

证明 由 $u \in S$ 及对正整数 $\frac{u}{a}$ 有

$$
\left|S \cap\left\{\frac{u}{a} \cdot a, \frac{u}{a} \cdot b, \frac{u}{a} \cdot c\right\}\right|=1,
$$

知 $u \cdot \frac{b}{a}, u \cdot \frac{c}{a} \notin S$, 同理

$$
u \cdot \frac{c}{b} \notin S
$$

修订日期: 2020-04-01.
于是由于 $\frac{u c}{a b} \in \mathbb{N}^{*}$,

$$
\left|S \cap\left\{\frac{u c}{a b} \cdot a, \frac{u c}{a b} \cdot b, \frac{u c}{a b} \cdot c\right\}\right|=\left|S \cap\left\{u \cdot \frac{c}{b}, u \cdot \frac{c}{a}, u \cdot \frac{c^{2}}{a b}\right\}\right|=1,
$$

则

$$
u \frac{c^{2}}{a b} \in S
$$

同理

$$
u \frac{a^{2}}{b c}, u \frac{b^{2}}{a c} \in S
$$

引理即证.

回到必要性的证明, 假设存在满足题意的 $(a, b, c)$, 使得存在 $x_{0}, y_{0}, z_{0} \in$ $\mathbb{Z}, x_{0}+y_{0}+z_{0}=0$, 满足 $a^{x_{0}} b^{y_{0}} c^{z_{0}}=1$, 且 $\left(x_{0}, y_{0}, z_{0}\right) \notin T$. 则 $\left(x_{0}, y_{0}, z_{0}\right) \neq$ $(0,0,0)$, 不妨设 $\operatorname{gcd}\left(x_{0}, y_{0}, z_{0}\right)=1$, 则 $3 \mid x_{0} y_{0} z_{0}$. 从而 $x_{0}, y_{0}, z_{0}$ 中恰有一个 3 的倍数, 不妨设 $3 \mid z_{0}$. 进而由 $x_{0}+y_{0}+z_{0}=0$ 知可不妨设

$$
x_{0} \equiv 1 \quad(\bmod 3), \quad y_{0} \equiv 2 \quad(\bmod 3)
$$

于是令

$$
k=\frac{2 x_{0}+y_{0}+2}{3}, l=\frac{-x_{0}-2 y_{0}-1}{3},
$$

则 $k, l$ 都是整数且

$$
a^{2 k+l-1} b^{-k-2 l} c^{-k+l+1}=a^{x_{0}} b^{y_{0}} c^{-x_{0}-y_{0}}=a^{x_{0}} b^{y_{0}} c^{z_{0}}=1 \text {. }
$$

此即

$$
\frac{1}{a}\left(\frac{a^{2}}{b c}\right)^{k}=\frac{1}{c}\left(\frac{b^{2}}{a c}\right)^{l}
$$

取正整数 $M>|k|+|l|$, 易知存在 $N \in S$ 为 $(a b c)^{|k|+|l|+2 M+1}$ 的倍数, 因 $k+M, l+$ $M$ 均为正整数, 故由引理归纳知

$$
N\left(\frac{a^{2}}{b c}\right)^{k+M}\left(\frac{b^{2}}{a c}\right)^{M}, N\left(\frac{a^{2}}{b c}\right)^{M}\left(\frac{b^{2}}{a c}\right)^{l+M} \in S
$$

且均为 $a b c$ 的倍数. 在条件中令 $n=\frac{N}{a}\left(\frac{a^{2}}{b c}\right)^{k+M}\left(\frac{b^{2}}{a c}\right)^{M}$, 则由 $(*)$ 知 $a n, c n \in S$,从而矛盾. 故假设不成立, 必要性得证.

充分性：对正整数 $n, m$, 定义 $n \sim m$ 当且仅当存在和为 0 的整数 $x, y, z$满足 $n=m \cdot a^{x} b^{y} c^{z}$. 容易验证这是 $\mathbb{N}^{*}$ 上的等价关系, 并将 $\mathbb{N}^{*}$ 划分成若干等价类,在每个等价类中取出一个代表元组成集合 $A$. 对 $u \in A$, 设 $u$ 所在的等价类为 $S_{u}$, 令

$$
S=\bigcup_{u \in A}\left\{u a^{x} b^{y} c^{z}|x, y, z \in \mathbb{Z}, x+y+z=0,3|(x-y), u a^{x} b^{y} c^{z} \in S_{u}\right\}
$$

我们验证 $S$ 满足条件.

若

$$
u a^{x_{1}} b^{y_{1}} c^{z_{1}}=u a^{x_{2}} b^{y_{2}} c^{z_{2}},
$$

其中 $\left(x_{1}, y_{1}, z_{1}\right),\left(x_{2}, y_{2}, z_{2}\right)$ 是两组和为 0 的整数, 则

$$
a^{x_{1}-x_{2}} b^{y_{1}-y_{2}} c^{z_{1}-z_{2}}=1 .
$$

由于关于 $x, y, z$ 的不定方程 $a^{x} b^{y} c^{z}=1, x, y, z \in \mathbb{Z}$, 且 $x+y+z=0$ 的解集含于 $T$, 故 $\left(x_{1}-x_{2}, y_{1}-y_{2}, z_{1}-z_{2}\right) \in T$. 注意到如果 $(x, y, z) \in T$, 则 $3 \mid(x-y)$,从而 $3 \mid\left(x_{1}-x_{2}\right)-\left(y_{1}-y_{2}\right)$, 即

$$
x_{1}-y_{1} \equiv x_{2}-y_{2} \quad(\bmod 3),
$$

于是 $S$ 定义良好.

对任意正整数 $n$, 设 $a n$ 所在的等价类代表元为 $u$, 设

$$
\text { an }=u a^{x_{0}} b^{y_{0}} c^{z_{0}} \text {, }
$$

其中 $x_{0}, y_{0}, z_{0} \in \mathbb{Z}, x_{0}+y_{0}+z_{0}=0$, 则

$$
\begin{aligned}
& b n=u a^{x_{0}-1} b^{y_{0}+1} c^{z_{0}}, b n \in S_{u}, \\
& c n=u a^{x_{0}-1} b^{y_{0}} c^{z_{0}+1}, c n \in S_{u} .
\end{aligned}
$$

由于

$$
x_{0}-y_{0},\left(x_{0}-1\right)-\left(y_{0}+1\right)=x_{0}-y_{0}-2, x_{0}-1-y_{0}
$$

模 3 互异, 其中恰有一个为 3 的倍数, 故 $a n, b n, c n$ 中恰有一个在 $S$ 中, 充分性即证.

评注 如果我们考虑 $a, b, c$ 关于 $a b c$ 的所有素因子 $p_{1}, p_{2}, \cdots, p_{k}$ 的幂次组成的 $k$ 元数组 $\alpha, \beta, \gamma$, 则命题等价于对于存在集合 $S^{\prime} \subseteq \mathbb{N}^{k}$, 满足对每个 $v \in \mathbb{N}^{k}, v+\alpha, v+\beta, v+\gamma$ 中恰有一个在 $S^{\prime}$ 中. 从一维情况考虑起, 可以知道如果 $v+\alpha+\beta+\gamma \in S$, 则 $v+3 \alpha \in S^{\prime}$, 这样就容易推出 $\alpha, \beta, \gamma$ 之间需要满足的条件. 对于多维情况, 实际上是一致的.

