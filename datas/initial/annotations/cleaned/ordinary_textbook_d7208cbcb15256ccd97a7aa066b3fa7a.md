# 2020 年丝绸之路数学竞赛解答与评析 

## 郭尧昱

(中国人民大学附属中学, 100080)

指导教师: 张端阳

本文给出 2020 年丝绸之路数学竞赛的解析和简评. 总体而言没有难度过高的题目, 其中前两题是高中联赛中档题难度, 后两题是冬令营中档题难度. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 设 $\left\{a_{n}\right\}$ 是严格单调递增的无穷正整数数列, 满足对任意正整数 $n$, $a_{n} \leq n+2020$, 且 $a_{n+1} \mid n^{3} a_{n}-1$. 证明: 对任意正整数 $n, a_{n}=n$.
2. 如图, $\omega$ 是 $\triangle A B C$ 的外接圆, $K, L, M$ 分别是边 $A B, B C, C A$ 上的点, 满足 $C M \cdot C L=A M \cdot B L$. 延长 $L K, C A$ 交于点 $P, \triangle K M P$ 的外接圆与圆 $\omega$ 的公共弦与线段 $A M$ 交于点 $S$. 证明: $S K / / B C$.



3. 对于实系数多项式 $Q(x)=k_{n} x^{n}+k_{n-1} x^{n-1}+\cdots+k_{0}$, 若

$$
\left|k_{0}\right|=\left|k_{1}\right|+\left|k_{2}\right|+\cdots+\left|k_{n}\right| \text {, }
$$

修订日期: 2020-09-23.
则称它是“强力的”; 若 $k_{0} \geq k_{1} \geq \cdots \geq k_{n}$, 则称它是“非增的”.

设 $P(x)=a_{d} x^{d}+a_{d-1} x^{d-1}+\cdots+a_{0}$ 是各项系数非零的实系数多项式, 满足 $a_{d}>0$. 已知存在非负整数 $s, t$, 使得 $s+t>0$, 且多项式 $P(x)(x-1)^{t}(x+1)^{s}$是强力的, 证明: 多项式 $P(x)$ 和 $(-1)^{d} P(-x)$ 中至少有一个是非增的.

4. 证明: 对任意正整数 $m$, 存在正整数 $n$, 使得平面上任意 $n$ 个不同的点可以被分成 $m$ 个非空的点集, 满足它们的凸包有一个公共点.

注: 有限点集 $X$ 的凸包是指所有顶点均为 $X$ 中的点, 且包含 $X$ 中所有点的凸多边形. 这里的包含指 $X$ 中的点均在这个凸多边形的边界或内部. 这个凸多边形可以退化为线段或点, 凸多边形的任意三个顶点不共线.

## II . 解答与评注

1. 设 $\left\{a_{n}\right\}$ 是严格单调递增的无穷正整数数列, 满足对任意正整数 $n$, $a_{n} \leq n+2020$, 且 $a_{n+1} \mid n^{3} a_{n}-1$. 证明: 对任意正整数 $n, a_{n}=n$.

证明 1 因为 $\left\{a_{n}\right\}$ 是严格单调递增的正整数数列, 所以 $a_{n} \geq n$. 记 $b_{n}=a_{n}-n$, 则由条件, $0 \leq b_{n} \leq 2020$.

由 $a_{n+1}>a_{n}$, 知

$$
b_{n+1}=a_{n+1}-(n+1)>a_{n}-(n+1)=b_{n}-1 \text {, }
$$

进而由 $\left\{b_{n}\right\}$ 是整数列, 知 $b_{n+1} \geq b_{n}$.

因为数列 $\left\{b_{n}\right\}$ 有上界 2020 , 所以存在正整数 $N$ 和整数 $0 \leq c \leq 2020$, 使得当 $n \geq N$ 时, $b_{n}$ 恒等于 $c$, 从而 $a_{n}=n+c$.

这样, 当 $n \geq N$ 时,

$$
n+c+1 \mid n^{3}(n+c)-1 \text {. }
$$

因为

$$
n^{3}(n+c)-1 \equiv(c+1)^{3}-1 \quad(\bmod n+c+1)
$$

所以

$$
n+c+1 \mid(c+1)^{3}-1 \text {. }
$$

取 $n$ 使得 $n+c+1>(c+1)^{3}-1$, 则 $(c+1)^{3}-1=0$, 解得 $c=0$. 于是当 $n \geq N$ 时, $a_{n}=n$.

又由 $\left\{a_{n}\right\}$ 严格单调递增, 知当 $n<N$ 时, 也有 $a_{n}=n$.

综上, 命题得证.
证明 2 因为 $\left\{a_{n}\right\}$ 是严格单调递增的正整数数列, 所以 $a_{n+1} \geq n+1$. 又由条件, $a_{n+1} \leq n+2021$, 所以 $n+1 \leq a_{n+1} \leq n+2021$.

由 $a_{n+1} \mid n^{3} a_{n}-1$, 知 $\left(a_{n+1}, n\right)=1$. 当 $2021 ! \mid n$ 时, $\left(a_{n+1}, 2021 !\right)=1$, 所以 $a_{n+1} \neq n+2, n+3, \cdots, n+2021$, 故 $a_{n+1}=n+1$.

由 $\left\{a_{n}\right\}$ 严格单调递增, 知当 $i \leq n$ 时, 也有 $a_{i}=i$.

因为有无穷多个正整数能被 2021 ! 整除, 所以命题得证.

评注 注意到 $a_{n}$ 的取值范围有限, 且数列严格递增, 故可在 $n$ 较大时确定 $a_{n}$的取值, 再反推 $n$ 较小时的情形. 上述先研究较大的 $n$, 再反推的方法在很多数列问题中均可见到.

2. 如图, $\omega$ 是 $\triangle A B C$ 的外接圆, $K, L, M$ 分别是边 $A B, B C, C A$ 上的点, 满足 $C M \cdot C L=A M \cdot B L$. 延长 $L K, C A$ 交于点 $P, \triangle K M P$ 的外接圆与圆 $\omega$ 的公共弦与线段 $A M$ 交于点 $S$. 证明: $S K / / B C$.



证明 对 $\triangle P L C$ 及截线 $A K B$ 用梅涅劳斯定理得,

$$
\frac{P K}{K L} \cdot \frac{L B}{B C} \cdot \frac{C A}{A P}=1
$$

所以

$$
\frac{P K}{K L}=\frac{B C}{L B} \cdot \frac{A P}{C A} .
$$

由条件, $C M \cdot C L=A M \cdot B L$, 即

$$
\frac{C L}{B L}=\frac{A M}{C M}
$$

于是由比例的性质,

$$
\frac{B C}{B L}=\frac{C A}{C M} \text {. }
$$

这样,

$$
\frac{P K}{K L}=\frac{C A}{C M} \cdot \frac{A P}{C A}=\frac{A P}{C M}
$$

设 $\triangle K M P$ 的外接圆与圆 $\omega$ 的公共弦为 $D E$. 由相交弦定理,

$$
S A \cdot S C=S D \cdot S E=S P \cdot S M
$$

即

$$
\frac{S A}{S M}=\frac{S P}{S C}
$$

于是由比例的性质,

$$
\frac{S P}{S C}=\frac{S P-S A}{S C-S M}=\frac{A P}{C M}
$$

结合 (1)、(2) 得,

$$
\frac{P K}{K L}=\frac{S P}{S C}
$$

故 $S K / / B C$.

评注 本题本质是直线型问题, 考察对边比例的转化. 也可以将两个比例设为基本量, 用它们表示其他的比例, 这种方法更代数一些, 不如上面的方法美观.

3. 对于实系数多项式 $Q(x)=k_{n} x^{n}+k_{n-1} x^{n-1}+\cdots+k_{0}$, 若

$$
\left|k_{0}\right|=\left|k_{1}\right|+\left|k_{2}\right|+\cdots+\left|k_{n}\right|
$$

则称它是“强力的”; 若 $k_{0} \geq k_{1} \geq \cdots \geq k_{n}$, 则称它是“非增的”.

设 $P(x)=a_{d} x^{d}+a_{d-1} x^{d-1}+\cdots+a_{0}$ 是各项系数非零的实系数多项式, 满足 $a_{d}>0$. 已知存在非负整数 $s, t$, 使得 $s+t>0$, 且多项式 $P(x)(x-1)^{t}(x+1)^{s}$是强力的, 证明: 多项式 $P(x)$ 和 $(-1)^{d} P(-x)$ 中至少有一个是非增的.

证明 先证明 $t \leq 1$.

若 $t \geq 2$, 记多项式

$$
Q(x)=P(x)(x-1)^{t-2}(x+1)^{s},
$$

则 $Q(x)$ 是实系数多项式, 首项系数为正, 且 $Q(x)(x-1)^{2}$ 是强力的.

设

$$
Q(x)(x-1)^{2}=k_{n} x^{n}+k_{n-1} x^{n-1}+\cdots+k_{0},
$$

则 $k_{n}>0$, 且 $\left|k_{0}\right|=\left|k_{1}\right|+\left|k_{2}\right|+\cdots+\left|k_{n}\right|$. 取 $x=1$ 得,

$$
k_{n}+k_{n-1}+\cdots+k_{0}=0,
$$

所以

$$
\left|k_{0}\right|=\left|k_{n}+k_{n-1}+\cdots+k_{1}\right| .
$$

这样,

$$
\left|k_{1}\right|+\left|k_{2}\right|+\cdots+\left|k_{n}\right|=\left|k_{n}+k_{n-1}+\cdots+k_{1}\right|,
$$

结合 $k_{n}>0$, 知 $k_{n-1}, \cdots, k_{1}$ 均非负.

设

$$
Q(x)(x-1)=j_{n-1} x^{n-1}+j_{n-2} x^{n-2}+\cdots+j_{0},
$$

则

$$
\begin{aligned}
Q(x)(x-1)^{2} & =\left(j_{n-1} x^{n-1}+j_{n-2} x^{n-2}+\cdots+j_{0}\right)(x-1) \\
& =j_{n-1} x^{n}+\left(j_{n-2}-j_{n-1}\right) x^{n-1}+\cdots+\left(j_{0}-j_{1}\right) x-j_{0}
\end{aligned}
$$

由上面的论证, $j_{n-1}>0$ 且 $j_{n-2}-j_{n-1}, \cdots, j_{0}-j_{1}$ 均非负, 所以

$$
0<j_{n-1} \leq j_{n-2} \leq \cdots \leq j_{1} \leq j_{0}
$$

但在 $(*)$ 中取 $x=1$ 得,

$$
j_{n-1}+j_{n-2}+\cdots+j_{0}=0
$$

矛盾!

再证明 $s \leq 1$.

对实系数多项式 $R(x)=b_{r} x^{r}+b_{r-1} x^{r-1}+\cdots+b_{0}$, 记

$$
\overline{R(x)}=(-1)^{r} R(-x)=b_{r} x^{r}+(-1) b_{r-1} x^{r-1}+\cdots+(-1)^{r} b_{0} .
$$

由定义, 若 $R(x)$ 是强力的, 则 $\overline{R(x)}$ 也是强力的.

注意到对实系数多项式 $A(x), B(x)$,

$$
\overline{A(x) B(x)}=(-1)^{\operatorname{deg} A+\operatorname{deg} B} A(-x) B(-x)=\overline{A(x)} \cdot \overline{B(x)}
$$

因为 $P(x)(x-1)^{t}(x+1)^{s}$ 是强力的, 所以

$$
\overline{P(x)(x-1)^{t}(x+1)^{s}}=\overline{P(x)}(\overline{x-1})^{t}(\overline{x+1})^{s}=\overline{P(x)}(x+1)^{t}(x-1)^{s}
$$

是强力的. 同上面的论证, 知 $s \leq 1$.

从而 $(s, t)=(1,1)$ 或 $(0,1)$ 或 $(1,0)$.

当 $(s, t)=(1,1)$ 时,

$$
\begin{aligned}
& P(x)(x+1)(x-1)=\left(a_{d} x^{d}+a_{d-1} x^{d-1}+\cdots+a_{0}\right)\left(x^{2}-1\right) \\
= & a_{d} x^{d+2}+a_{d-1} x^{d+1}+\left(a_{d-2}-a_{d}\right) x^{d}+\cdots+\left(a_{0}-a_{2}\right) x^{2}-a_{1} x-a_{0} .
\end{aligned}
$$

因为 $P(x)(x+1)(x-1)$ 是强力的, 所以

$$
\begin{aligned}
\left|a_{0}\right|= & \left|a_{d}\right|+\left|a_{d-1}\right|+\left|a_{d-2}-a_{d}\right|+\cdots+\left|a_{0}-a_{2}\right|+\left|a_{1}\right| \\
\geq & \left|\left(a_{0}-a_{2}\right)+\left(a_{2}-a_{4}\right)+\cdots+\left(a_{2\left[\frac{d}{2}\right]-2}-a_{2\left[\frac{d}{2}\right]}\right)+a_{2\left[\frac{d}{2}\right]}\right| \\
& +\left|a_{1}\right|+\left|a_{1}-a_{3}\right|+\cdots+\left|a_{2\left[\frac{d-1}{2}\right]+1}\right| \\
& \geq\left|a_{0}\right|+\left|a_{1}\right|+\left|a_{1}-a_{3}\right|+\cdots+\left|a_{2\left[\frac{d-1}{2}\right]+1}\right|
\end{aligned}
$$

从而

$$
a_{1}=a_{3}=\cdots=a_{2\left[\frac{d-1}{2}\right]+1}=0
$$

这与 $P(x)$ 的系数非零矛盾!

当 $(s, t)=(0,1)$ 时,

$$
\begin{aligned}
P(x)(x-1) & =\left(a_{d} x^{d}+a_{d-1} x^{d-1}+\cdots+a_{0}\right)(x-1) \\
& =a_{d} x^{d+1}+\left(a_{d-1}-a_{d}\right) x^{d}+\cdots+\left(a_{0}-a_{1}\right) x-a_{0} .
\end{aligned}
$$

因为 $P(x)(x-1)$ 是强力的, 所以

$$
\begin{aligned}
\left|a_{0}\right| & =\left|a_{d}\right|+\left|a_{d-1}-a_{d}\right|+\cdots+\left|a_{0}-a_{1}\right| \\
& \geq\left|\left(a_{0}-a_{1}\right)+\left(a_{1}-a_{2}\right)+\cdots+\left(a_{d-1}-a_{d}\right)+a_{d}\right| \\
& =\left|a_{0}\right| .
\end{aligned}
$$

从而

$$
a_{d}, a_{d-1}-a_{d}, \cdots, a_{0}-a_{1}
$$

同非负, 所以

$$
a_{0} \geq a_{1} \geq \cdots \geq a_{d}
$$

即 $P(x)$ 是非增的.

当 $(s, t)=(1,0)$ 时, $P(x)(x+1)$ 是强力的, 所以

$$
\overline{P(x)(x+1)}=\overline{P(x)} \cdot \overline{(x+1)}=\overline{P(x)}(x-1)
$$

是强力的. 这样由 $(s, t)=(0,1)$ 的情形知, $\overline{P(x)}$ 是非增的.

综上, 命题得证.

评注 本题过程较长, 关键在于发现 $x+1$ 和 $x-1$ 具有与 $P(x)$ 和 $(-1)^{d} P(-x)$相同的关系, 比较系数可知 $s$ 与 $t$ 均只能取 0 或 1 , 再讨论即可.

4. 证明: 对任意正整数 $m$, 存在正整数 $n$, 使得平面上任意 $n$ 个不同的点可以被分成 $m$ 个非空的点集, 满足它们的凸包有一个公共点.
注: 有限点集 $X$ 的凸包是指所有顶点均为 $X$ 中的点, 且包含 $X$ 中所有点的凸多边形。这里的包含指 $X$ 中的点均在这个凸多边形的边界或内部。这个凸多边形可以退化为线段或点, 凸多边形的任意三个顶点不共线.

证明 对 $m$ 归纳证明, 存在正整数 $n_{m}$ 满足要求.

当 $m=1$ 时, 取 $n_{1}=1$ 即可.

当 $m=2$ 时, 取 $n_{2}=4$. 对于平面上的 4 个不同的点 $A, B, C, D$, 若它们的凸包是四边形 $A B C D$, 则点集 $\{A, C\},\{B, D\}$ 满足要求; 若它们的凸包是三角形 $A B C$, 则点集 $\{A, B, C\},\{D\}$ 满足要求.

假设 $m \geq 2$ 且命题对所有不超过 $m$ 的正整数均成立, 来看 $m+1$ 时的情形.

令 $n_{m+1}=3 n_{m}$. 下面证明平面上任意 $3 n_{m}$ 个不同的点可以被分成 $m+1$个非空的点集, 满足它们的凸包有一个公共点.

考虑这 $3 n_{m}$ 个点的凸包, 分两种情形讨论.

情形 1 : 当凸包上的顶点个数不超过 $2 n_{m}$ 时, 将凸包上的所有顶点归入一个点集 $A$. 由归纳假设, 凸包内的不少于 $n_{m}$ 个点可以被分成 $m$ 个非空的点集, 它们的凸包有一个公共点. 因为该公共点在点集 $A$ 的凸包中, 所以命题成立.

情形 2: 当凸包上的顶点个数不少于 $2 n_{m}+1$ 时, 设凸包上的顶点依次为 $P_{1}, P_{2}, \cdots, P_{t}$, 其中 $t \geq 2 n_{m}+1$. 将

$$
P_{1}, P_{3}, P_{5}, \cdots, P_{2 n_{m}-1}, P_{2 n_{m}+1}, P_{2 n_{m}+2}, P_{2 n_{m}+3}, \cdots, P_{t}
$$

及凸包内的所有点归入一个点集 $A$. 由归纳假设, 凸包上余下的顶点 $P_{2}, P_{4}, \cdots$, $P_{2 n_{m}}$ 可以被分成 $m$ 个非空的点集 $X_{1}, X_{2}, \cdots, X_{m}$, 它们的凸包有一个公共点 $Q, Q$ 在 $P_{1}, P_{2}, \cdots, P_{t}$ 的凸包中.

因为对 $1 \leq i \leq n_{m}, \triangle P_{2 i-1} P_{2 i} P_{2 i+1}$ 中的任意一点均只在点集 $X_{1}, X_{2}, \cdots$, $X_{m}$ 中一个 (即含 $P_{2 i}$ 的点集) 的凸包中, 所以 $\triangle P_{2 i-1} P_{2 i} P_{2 i+1}$ 与 $X_{1}, X_{2}, \cdots, X_{m}$的凸包的公共区域的交集是空集, 从而 $Q$ 在多边形 $P_{1} P_{3} P_{5} \cdots P_{2 n_{m}+1}$ 中, 进而 $Q$ 在点集 $A$ 的凸包中, 命题成立.

归纳证毕。

评注 本题是一道构造性的组合问题, 主要考察对凸包的认识和运用. 在对 $m$ 归纳的过程中, 当凸包上的点较少时显然成立, 当凸包上点较多时可间隔地取凸包上的点, 保证公共点不在整体的凸包与所选点集的凸包的差集内．

