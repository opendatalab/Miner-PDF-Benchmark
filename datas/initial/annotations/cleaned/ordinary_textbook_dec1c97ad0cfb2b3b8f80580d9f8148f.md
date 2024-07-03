数学新星网 关教师专栏

www.nsmath.cn/jszl

# 2021 年北大数学夏令营试题解析 

肖一君 杜燕 叶梓

(学军中学教育集团文渊中学, 310012)

因为暑假疫情影响, 今年北京大学数学夏令营在线上举行, 在每个省市自治区设有 1 到 2 个考点, 考试时间为 2021 年 8 月 8 日 $8: 00-12: 00$ 和 8 月 9 日 $8: 00-12: 00$, 每天考 4 道题. 第一天题目较为容易, 第二天困难, 大约四道多题能获得一等奖. 第 $2,3,6,8$ 题是联赛模拟题风格, 3 容易, 6 中档题, 2 与 8 困难一些. $1,4,5$ 题具有北夏的风格, 不太常规, 考场上容易翻车, 但想到了又很简单,尤其是错过第 4 题就损失很大了. 第 7 题最困难, 需要熟悉单位根, 分圆多项式的性质, 有高等的背景.

## I. 试 题

1. 设 $a_{1}, a_{2}, a_{3}, a_{4}$ 是两两不同的正整数, 且不小于 80 , 满足 $a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+$ $a_{4}^{2}-4 k^{2} \in \mathbb{N}^{*}$. 求 $\left(a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}-4 k^{2}\right) \cdot k^{2}$ 的最小值.
2. 在 $\triangle A B C$ 中, $A C>B C>A B, \odot I$ 为其内切圆, $D$ 是 $A C$ 中点, $M$ 是 $\odot I$ 与 $A C$ 切点, $F$ 在 $A M$ 上, $A E \perp B I$ 于 $E, D J / / A E$ 且 $J E F$ 共线, $\odot D E F$交 $D J$ 于 $D, K$ 两点. 求证: $\odot J F K$ 与 $\odot I$ 相切.
3. 给定 $n$, 记 $a_{i}=2 i-1,(1 \leq i \leq n), b_{1}, b_{2}, \cdots, b_{n}$ 是 $2,4, \cdots, 2 n$ 的排列. 若对 $1 \leq i \neq j \leq n$, 均有

$$
\min \left\{a_{i}, b_{i}\right\}+\min \left\{a_{j}, b_{j}\right\} \neq \min \left\{a_{j}, b_{i}\right\}+\min \left\{a_{i}, b_{j}\right\},
$$

则称 $\left(b_{1}, b_{2}, \cdots, b_{n}\right)$ 为 “好排列”, 求所有好排列个数.

4. 是否存在 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 使对 $\forall x, y, z \in \mathbb{N}^{*}$, 有

$$
z+f(x)+f(f(y)) \mid x^{2}+[f(f(z))]^{2}+[f(y)]^{2} ?
$$

修订日期: 2021-08-16.

5. 设 $m, n$ 为正整数, 有根长度为 1 的火柴和一个 $m \times n$ 矩形点阵, 矩阵中同行、同列相邻两点的距离也等于 1 . 小白同学将 $m n$ 根火柴互不重叠地放在点阵中, 使得所有火柴头恰一一地覆盖了这 $m n$ 个点, 火柴尾在与火柴头相邻的点上. 称两根火柴是连接的, 如果存在一个以这两根火柴为首尾的序列, 序列中相邻两根火柴都有公共交点. 称若干根火柴是一个“图形”, 如果图形内的火柴两两连接, 图形外的任意一根火柴都不与图形内的火柴连接.

试问: 小白同学至多能摆出多少个图形?

6. 试求所有正整数 $m \leq 2021$, 使得存在正实数 $t$, 满足对任意正整数 $n$, 都有 $[t[t n]] \equiv m(\bmod 2021)$ 成立.
7. 设 $z_{1}, z_{2}, \cdots, z_{2021}$ 都是单位根, 且 $\xi=z_{1}+z_{2}+\cdots+z_{2021}$ 的模长都等于 1 . 证明: $\xi$ 也是单位根.
8. 给定正整数 $r \leq n-2$. 设 $A_{1}, A_{2}, \cdots, A_{m}$ 是 $\{1,2, \cdots, n\}$ 的 $m$ 个不同的 $r$ 元子集, 满足对任意三个不同的 $A_{i}, A_{j}, A_{k}$, 都有 $\left|A_{i} \cup A_{j} \cup A_{k}\right|>r+2$. 证明:

$$
m \leq \frac{n}{r^{2}} \mathrm{C}_{n}^{r-1}
$$

## II . 解答与评注

题 1 设 $a_{1}, a_{2}, a_{3}, a_{4}$ 是两两不同的正整数, 且不小于 80 , 满足

$$
a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}-4 k^{2} \in \mathbb{N}^{*} .
$$

求 $\left(a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}-4 k^{2}\right) \cdot k^{2}$ 的最小值.

解 构造 $\left(a_{1}, a_{2}, a_{3}, a_{4}, k\right)=(80,81,82,96,85)$, 则原式 $=85^{2}=7225$.

若 $\left(a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}-4 k^{2}\right) \cdot k^{2}<85^{2}$, 则必有

$$
80 \leq k \leq 84, a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}-4 k^{2}=1
$$

这是因为 $2 \cdot 80^{2}>85^{2}$.

$1^{\circ}$ 当 $a_{1}+a_{2}+a_{3}+a_{4} \geq 4 k$, 则

$$
4\left(a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}\right)-\left(a_{1}+a_{2}+a_{3}+a_{4}\right)^{2}=\sum_{1 \leq i<j \leq 4}\left(a_{i}-a_{j}\right)^{2} \geq 6
$$

因此, $a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2} \geq \frac{6+(4 k)^{2}}{4}=4 k^{2}+\frac{3}{2}$, 与 (1) 矛盾!
$2^{\circ}$ 当 $a_{1}+a_{2}+a_{3}+a_{4}<4 k$, 则 $a_{1}+a_{2}+a_{3}+a_{4} \leq 4 k-1$,

$$
\begin{aligned}
a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2} & \leq 80^{2}+81^{2}+82^{2}+(4 k-1-80-81-82)^{2} \text { (利用 } y=x^{2} \text { 凸性) } \\
& =19685+(4 k-244)^{2} \\
& =4 k^{2}+12\left(k-\frac{244}{3}\right)^{2}-\frac{481}{3} \\
& \left.\leq 4 k^{2}+12 \times\left(\frac{8}{3}\right)^{2}-\frac{481}{3} \text { (由 (1) 知 } 80 \leq k \leq 84\right) \\
& =4 k^{2}-75,
\end{aligned}
$$

与 (1) 矛盾!

因此, 原式 $\geq 85^{2}$. 综上, 所求最小值为 $85^{2}=7225$.

评注 本题的难点在于试出最小值与取等条件, 后面的证明分两种情况讨论是平凡的.

题 2 在 $\triangle A B C$ 中, $A C>B C>A B, \odot I$ 为其内切圆, $D$ 是 $A C$ 中点, $M$是 $\odot I$ 与 $A C$ 切点, $F$ 在 $A M$ 上, $A E \perp B I$ 于 $E, D J \| A E$ 且 $J E F$ 共线, $\odot D E F$交 $D J$ 于 $D, K$ 两点. 求证: $\odot J F K$ 与 $\odot I$ 相切.

证明 1 如图, 设直线 $A E, J E, J D$ 分别交 $B C$ 于 $O, Q, R, \odot I$ 与 $B C$ 切于点 $P$, 连结 $J P$ 与 $\odot I$ 交于点 $S$.



设 $A B=c, B C=a, A C=b$, 由 $B E$ 平分 $\angle A B C, B E \perp A E$ 知 $E$ 为 $A O$中点. 所以

$$
D E=\frac{1}{2} C O=\frac{1}{2}(a-c)=\frac{1}{2} b-\frac{1}{2}(b+c-a)=A D-A M=D M,
$$

由 $B E \perp A E, D J / / A E$ 知 $B E \perp D J$.

由定差幂线定理知

$$
J I^{2}-D I^{2}=J E^{2}-D E^{2} .
$$

于是,

$$
\begin{aligned}
J S \cdot J P & =\text { 点 } J \text { 到 } \odot I \text { 的幂 } \\
& =J I^{2}-M I^{2} \\
& =J I^{2}-D I^{2}+D M^{2} \\
& =J I^{2}-D I^{2}+D E^{2} \\
& =J E^{2} .
\end{aligned}
$$

又由 $A E \| D J, D E / \mid B C$ 得平行四边形 $D E O R$, 于是 $D R=E O=A E$. 于是

$$
\frac{J F}{J E}=\frac{D J}{D J+A E}=\frac{D J}{J R}=\frac{J E}{J Q}
$$

即

$$
J F \cdot J Q=J E^{2}=J S \cdot J P
$$

故 $P, S, F, Q$ 四点共圆.

所以

$$
\angle J S F=\angle P Q F=\angle D E Q=\angle D K F
$$

(因为 $D E / / B C, D, E, F, K$ 四点共圆).

所以 $J, S, F, K$ 共圆.

过 $S$ 作 $\odot(J F K)$ 的切线 $S Y$, 过 $J$ 作 $\odot(J F K)$ 的切线 $J X$,

由

$$
\angle K J X=\angle J F K=\angle J D E=\angle J R B
$$

得 $J X / / B C$, 所以

$$
\angle J S Y=\angle S J X=\angle B P S
$$

故

$$
\angle P S Y=\angle C P S \text {. }
$$

而 $B C$ 为 $\odot I$ 切线, 于是 $S Y$ 为 $\odot I$ 切线,

即 $S Y$ 为 $\odot I$ 与 $\odot(J F K)$ 公切线, 故 $\odot I$ 与 $\odot(J F K)$ 相切. 证毕!
证明 2 取 $A B$ 的中点 $G$, 设 $A B$ 与 $\odot I$ 切于 $N, B C$ 与 $\odot I$ 切于 $P$.



下面证明 $E$ 是中位线 $D G$ 与切点弦 $M P$ 交点, 即 $D G, M P, B I$ 三线共点.事实上,

$$
\angle A G E=2 \angle A B E=\angle A B C \Rightarrow G E \| B C,
$$

所以 $G E D$ 共线.

又由于

$$
\angle A M I=\angle A E I=90^{\circ} \text {, }
$$

故 $A M E I$ 共圆. 因此

$$
\angle E M C=\angle A I E=90^{\circ}-\frac{1}{2} \angle A C B=\angle P M C \text {, }
$$

所以 $M E P$ 共线.

设 $P N \cap D G=H$, 同理可知 $H I C$ 共线且 $\angle A H C=90^{\circ}$.

设 $P J \cap \odot I=S, P J \cap D G=T$, 连结 $A H, M S, F S, F T$.

下面证明 $S$ 即为 $\odot I$ 与 $\odot J K F$ 的切点.

首先, 由 $\angle A H C=90^{\circ}$, 可知 $A D=D H$, 又由 $C M=C P$, 中位线 $D H G / /$ $C P$, 可知 $\triangle A D H \sim \triangle M C P$, 同时 $A H / / M P$, 再由点 $A$ 与点 $P$ 到直线 $D G$ 距离相等知 $A H=E P$, 四边形 $A H P E$ 为平行四边形, 所以 $A E=P H$.

由 $D J / / A E / / P H$ 知,

$$
D F=A D \frac{D J}{A E+D J}=D H \frac{D J}{P H+D J}=D T \text {. }
$$

且由于 $D E / / C P$ 及等腰三角形 $C P M$ 知 $D M=D E$, 从而四边形 $M E T F$ 为等
腰梯形.

而 $\angle S M P=\angle S P B=\angle S T H$, 可知 $S T E M$ 共圆, 故 $S T E M F$ 五点共圆,即 $S T E F$ 共圆。

再结合 $E F K D$ 共圆, 可知 $J S F K$ 共圆, 即 $S$ 在 $\odot(J F K)$ 上.

过 $S$ 作 $\odot I$ 切线 $X S Y$, 可知

$$
\angle J K S=\angle J F S=\angle S T E=\angle S P C=\angle P S X=\angle J S Y
$$

所以线 $X S Y$ 也是 $\odot(J F K)$ 切线, 即 $\odot I$ 与 $\odot(J F K)$ 相切于 $S$, 证毕!

评注 两种证法都是发现 $J P$ 经过两圆的切点, 先给出 $J P$ 与一个圆的交点 $S$, 再证明一个关键的四点共圆: 证法 1 利用定差幕线转化垂直条件, $D J / / A E$提供相似比例计算, 通过圆幂证明 $P, S, F, Q$ 四点共圆; 证法 2 利用角分线 $B I$, 中位线 $D G$, 切点弦 $P M$ 三线共点性质, 以及 $A H P E$ 是平行四边形, 通过 $D J / / A E$ 导比例发现等腰梯形 $M E T F$, 然后证明 STEMF 五点共圆.最后再证明两圆相切只需过 $S$ 做出一条切线即得.

题 3 给定 $n$, 记 $a_{i}=2 i-1,(1 \leq i \leq n), b_{1}, b_{2}, \cdots, b_{n}$ 是 $2,4, \cdots, 2 n$ 的排列. 若对 $1 \leq i \neq j \leq n$, 均有

$$
\min \left\{a_{i}, b_{i}\right\}+\min \left\{a_{j}, b_{j}\right\} \neq \min \left\{a_{j}, b_{i}\right\}+\min \left\{a_{i}, b_{j}\right\}
$$

则称 $\left(b_{1}, b_{2}, \cdots, b_{n}\right)$ 为“好排列”, 求所有好排列个数.

解 设好排列有 $f_{n}$ 种, 补充定义 $f_{0}=1$, 易知 $f_{1}=1$.

对 4 个不同的数 $a_{i}, a_{j}, b_{i}, b_{j}$, 不妨先考虑 $a_{i}$ 最小情况, 则

$$
\begin{aligned}
\min \left\{a_{i}, b_{i}\right\} & +\min \left\{a_{j}, b_{j}\right\} \neq \min \left\{a_{i}, b_{j}\right\}+\min \left\{a_{j}, b_{i}\right\}, \\
& \Leftrightarrow \min \left\{a_{j}, b_{j}\right\} \neq \min \left\{a_{j}, b_{i}\right\}, \\
& \Leftrightarrow a_{j} \text { 不同时小于 } b_{i}, b_{j}, \\
& \Leftrightarrow a_{i}, a_{j} \text { 不同时小于 } b_{i}, b_{j} .
\end{aligned}
$$

结合上述分析知

(1) 成立当且仅当 $a_{i}, a_{j}$ 不同时小于 (大于) $b_{i}, b_{j}$.

回到题设 $b_{1}=2 t(1 \leq t \leq n)$, 当 $t \geq 2$ 时, 有 $a_{1}=1, a_{2}=3$ 均小于 $b_{1}$. 所以由 $(2)$ 知只能 $b_{2}=2$, 依此类推可得 $b_{3}=4, \cdots, b_{t}=2 t-2$. 故 $b_{1}, b_{2}, \cdots, b_{t}$恰用完 $2,4, \cdots, 2 t$.
根据题目的平移不变性知 $b_{t+1}, \cdots, b_{n}$ 的好排列数量为 $f_{n-t}$, 且与 $b_{1}, b_{2}, \cdots, b_{t}$ 合并仍满足 $(2)$. 这是因为 $a_{t+1}, \cdots, a_{n}$ 总大于 $b_{1}, b_{2}, \cdots, b_{t}$, 而 $b_{t+1}, \cdots, b_{n}$ 总大于 $a_{1}, a_{2}, \cdots, a_{t}$. 故仍是好排列. 因此,

$$
f_{n}=\sum_{t=1}^{n} f_{n-t}=\sum_{i=0}^{n-1} f_{i}, n \in \mathbb{N}^{*}
$$

从而, $f_{n+1}=\sum_{i=0}^{n} f_{i}=2 f_{n}$, 故 $f_{n}=2^{n-1}, n \in \mathbb{N}^{*}$.

评注 本题是一道有意思的组合型代数问题, 首先要转化题目的条件为 $a_{i}, a_{j}$ 不同时小于 $b_{i}, b_{j}$, 再动手计算前面的 $b_{i}$, 找到规律, 化归到 $n$ 较小的情形,从而发现其实是一个递推的形式.

题 4 是否存在 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 使对 $\forall x, y, z \in \mathbb{N}^{*}$, 有

$$
z+f(x)+f(f(y)) \mid x^{2}+[f(f(z))]^{2}+[f(y)]^{2} ?
$$

解 不存在. 取 $x=1$, 任取 $y \in \mathbb{N}^{*}$, 再取 $z$ 使 $4 \mid f(f(x))+f(y)+z$, 则

$$
[f(f(z))]^{2}+[f(y)]^{2}+1 \equiv 0 \quad(\bmod 4) .
$$

但完全平方数模 4 余 0 或 1 . 故上式左边模 4 余 1,2 或 3 , 矛盾!

故不存在满足题意的 $f$.

评注 本题只需考虑模 4 就解决了, 考场上很多同学看到这个较为复杂的函数方程, 不太敢动手做, 类似 2011 年高中数学联赛加试第 2 题多项式问题, 也是只需考虑模 4 就很轻松拿下, 但当时做对的同学并不多.

题 5 设 $m, n$ 为正整数, 有根长度为 1 的火柴和一个 $m \times n$ 矩形点阵, 矩阵中同行、同列相邻两点的距离也等于 1 . 小白同学将 $m n$ 根火柴互不重叠地放在点阵中, 使得所有火柴头恰一一地覆盖了这 $m n$ 个点, 火柴尾在与火柴头相邻的点上. 称两根火柴是连接的, 如果存在一个以这两根火柴为首尾的序列, 序列中相邻两根火柴都有公共交点. 称若干根火柴是一个“图形”, 如果图形内的火柴两两连接, 图形外的任意一根火柴都不与图形内的火柴连接.

试问: 小白同学至多能摆出多少个图形?

解 该同学至多摆出 $\left[\frac{m}{2}\right] \cdot\left[\frac{n}{2}\right]$ 个图形.

一方面, 先证明至多摆出 $\left[\frac{m}{2}\right] \cdot\left[\frac{n}{2}\right]$ 个.

将点阵的点视为图中的点, 将每根火柴的头与尾所在的点连一条边, 形成图
$G$. 则每个图形即图 $G$ 的一个连通分支. 根据题意, 每个点都会被一根火柴的头所覆盖, 即连通分支每个顶点都有一条专属的边与之对应, 故连通分支的边数不小于顶点数, 故每个连通分支必包含一个圈. 因此图形总数不超过不相交的圈的总数 $k$, 下证明: $k \leqslant\left[\frac{m}{2}\right] \cdot\left[\frac{n}{2}\right]$.

我们称每个圈最上面和最下面的不交横线为好横线, 最左边与最右边的不交坚线为好坚线, 显然每条好横 (坚) 线均至少占据两个顶点.

(1) 当 $m, n$ 中至少有一个数为偶, 不妨设 $m$ 为偶, 因为每一行有 $n$ 个顶点,故至多产生 $\left[\frac{n}{2}\right]$ 条好横线, 而 $k$ 个不交圈至少有 $2 k$ 条好横线, 所以 $2 k \leqslant m \cdot\left[\frac{n}{2}\right]$,即

$$
k \leqslant \frac{m}{2} \cdot\left[\frac{n}{2}\right]=\left[\frac{m}{2}\right] \cdot\left[\frac{n}{2}\right] .
$$

(2) 当 $m, n$ 均为奇数时, 设 $m=2 a+1, n=2 b+1$, 则每行至多产生 $b$ 条好横线, 故至多产生 $(2 a+1) b$ 条好横线. 注意每列有奇数个点, 故要么有奇数 (至少是 3 ) 个点落在一个圈中, 则此圈中间的行一定会有两个点, 相当于浪费一条好横线; 要么这一列有一个点不在任何一个圈中, 则此点与其左右相邻的点都不会相连作为好横线, 也会浪费一条好横线. 故至少浪费了 $b$ 条好横线, 于是 $2 k \leqslant(2 a+1) b-b$, 即 $k \leqslant a b=\left[\frac{m}{2}\right] \cdot\left[\frac{n}{2}\right]$.

另一方面, 给出构造:

1) 当 $m, n$ 均为偶数.



2) 当 $m, n$ 一奇一偶, 不妨设 $m$ 为偶数.



3) 当 $m, n$ 均为奇数.



评注 本题的难点在于正确理解题意, 然后发现每个图形即是一个连通分支, 且边数恰等于顶点数, 故每个图形都有一个圈, 于是容易给出构造, 证明只需关注每个圈最外围的好线。

题 6 试求所有正整数 $m \leq 2021$, 使得存在正实数 $t$, 满足对任意正整数 $n$,都有 $[t[t n]] \equiv m(\bmod 2021)$ 成立.

解 所求 $m=2020$ 或 2021 .

一方面, 取 $t=2021$, 则对任意 $n \in \mathbb{N}^{+},[t[t n]] \equiv 2021(\bmod 2021)$, 再取 $t$为方程 $x^{2}-2021 x-2021=0$ 的正根, 则 $2021<t<2022$, 且

$$
\begin{aligned}
{[t[t n]] } & =\left[t^{2} n-t\{t n\}\right]=[2021 t n+2021 n-t\{t n\}] \\
& =2021[t n]+2021 n+[(2021-t)\{t n\}] \\
& \equiv-1 \equiv 2020 \quad(\bmod 2021) .
\end{aligned}
$$

故 $m=2020$ 或 2021 满足要求.

另一方面, 下证 $m$ 只能取 2020 或 2021.

当 $t$ 为有理数时, 设 $t=\frac{p}{q}, p, q \in \mathbb{N}^{*},(p, q)=1$.

令 $n=q^{2}$ 得 $m \equiv p^{2}(\bmod 2021)$, 令 $n=2 q^{2}$ 得 $m \equiv 2 p^{2}(\bmod 2021)$, 于是 $2021 \mid p^{2}$, 故 $43 \mid p^{2}$ 且 $47 \mid p^{2}$, 所以 $43 \mid p$ 且 $47 \mid p$, 即 $2021 \mid p$, 同时 $m \equiv 0$ $(\bmod 2021)$, 故 $m=2021$.

当 $t$ 为无理数时, 由狄利克雷定理, 存在 $n \in \mathbb{N}^{*}$ 使得 $\{n t\}<1-\{t\}$, 故 $[(n+1) t]=[n t]+[t]$, 则

$$
m \equiv[t[t(n+1)]] \equiv[t[t n]+t[t]] \quad(\bmod 2021)
$$

下面有两种可能, 要么

$$
[t[t n]+t[t]] \equiv[t[t n]]+[t[t]] \equiv 2 m \quad(\bmod 2021)
$$

要么

$$
[t[t n]+t[t]] \equiv[t[t n]]+[t[t]]+1 \equiv 2 m+1 \quad(\bmod 2021)
$$

即 $m \equiv 2 m$ 或 $2 m+1(\bmod 2021) ，$

故 $m \equiv 2020$ 或 $2021(\bmod 2021)$.

综上, 所求 $m$ 为 2020 或 2021 .

评注 本题的结果非常漂亮, 通过讨论 $t$ 是否有理数, 在 $t$ 是无理数时给出合适的条件, 打开里面的取整符号, 容易分析出 $m$ 只能是 2020 或 2021. 对 $m=2020$ 的构造, 由前面讨论知 $t$ 应取无理数, 比较好操作的无理数当然是一元二次方程的无理根, 待定系数设 $t$ 是 $x^{2}=a x+b$ 的正无理根, 则

$$
[t[t n]]=\left[t^{2} n-t\{t n\}\right]=[a t n+b n-t\{t n\}]=a[t n]+b n+[(a-t)\{t n\}]
$$

在模 2021 意义下, 取 $a=b=2021$ 就非常自然了.

题 7 设 $z_{1}, z_{2}, \cdots, z_{2021}$ 都是单位根, 且 $\xi=z_{1}+z_{2}+\cdots+z_{2021}$ 的模长都等于 1 . 证明: $\xi$ 也是单位根.

证明 首先证明下述几个引理.

引理 1 若整系数多项式 $f(x)$ 所有根的模长为 1 , 则称 $f$ 为好多项式, 同时 $f$ 每个根均为单位根.

证明 设

$$
f(x)=a_{n} x^{n}+\cdots+a_{1} x+a_{0}=\left(x-w_{1}\right)\left(x-w_{2}\right) \cdots\left(x-w_{n}\right) \in \mathbb{Z}[x],
$$

这里 $\left|w_{j}\right|=1,1 \leq j \leq n$.

一方面由韦达定理知 $a_{k}(0 \leq k \leq n)$ 是 $\mathrm{C}_{n}^{k}$ 个模长为 1 的复数之和, 故 $\left|a_{k}\right| \leq 2^{n}$, 从而只有有限个 $n$ 次好多项式 $f$, 故 $n$ 次好多项式的根也只有有限个.另一方面，

$$
\begin{aligned}
& f(\sqrt{x}) \cdot f(-\sqrt{x}) \\
& =\left(\sum_{\substack{k \text { 为偶 } \\
0 \leqslant k \leqslant n}} a_{k} x^{\frac{k}{2}}+\sqrt{x} \sum_{\substack{k \text { 为奇 } \\
0 \leqslant k \leqslant n}} a_{k} x^{\frac{k-1}{2}}\right)\left(\sum_{\substack{k \text { 为偶 } \\
0 \leqslant k \leqslant n}} a_{k} x^{\frac{k}{2}}-\sqrt{x} \sum_{\substack{k \text { 为奇 } \\
0 \leqslant k \leqslant n}} a_{k} x^{\frac{k-1}{2}}\right)
\end{aligned}
$$

$$
=\left(\sum_{\substack{k \text { 为偶 } \\ 0 \leqslant k \leqslant n}} a_{k} x^{\frac{k}{2}}\right)^{2}-x\left(\sum_{\substack{k \text { 为奇 } \\ 0 \leqslant k \leqslant n}} a_{k} x^{\frac{k-1}{2}}\right)^{2} \in \mathbb{Z}[x],
$$

同时

$$
f(\sqrt{x}) \cdot f(-\sqrt{x})=\prod_{j=1}^{n}\left(-x+w_{j}^{2}\right)
$$

所以当 $w$ 是 $n$ 次好多项式的根, 则 $w^{2}$ 也是, 依此类推 $w^{2^{k}}(k \in \mathbb{N})$ 都是, 由抽屟原理知存在 $0 \leq k<l$ 使得 $w^{2^{k}}=w^{2^{l}}$, 即 $w^{2^{l}-2^{k}}=1$, 故 $w$ 是单位根, 引理 1 获证!

引理 2 对任意整数 $t, \sum_{\substack{1 \leq k \leq n \\(k, n)=1}} w^{k t}$ 均是整数.

证明 首先由于 $n$ 阶分圆多项式 $\Phi_{n}(x)=\prod_{\substack{1 \leq k \leq n \\(k, n)=1}}\left(x-w^{k}\right)$ 是整系数多项式,故 $\sum_{\substack{1 \leq k \leq n \\(k, n)=1}} w^{k}$ 是整数.

所以当 $(n, t)=1$ 时, $\sum_{\substack{1 \leq k \leq n \\(k, n)=1}} w^{k t}=\sum_{\substack{1 \leq k \leq n \\(k, n)=1}} w^{k}$ 是整数, 而当 $(n, t)=d>1$ 时,

$$
\sum_{\substack{1 \leq k \leq n \\(k, n)=1}} w^{k t}=\sum_{\substack{1 \leq k \leq n \\(k, n)=1}}\left(w^{d}\right)^{\frac{t}{d} k}
$$

这里 $w^{d}$ 是 $\frac{n}{d}$ 阶单位根, 且当 $k$ 遍历模 $n$ 缩系时, $k$ 遍历模 $\frac{n}{d}$ 的缩系恰好 $d$ 次, 故 $\frac{t}{d} k$ 也遍历模 $\frac{n}{d}$ 的缩系恰好 $d$ 次, 所以由 $\Phi_{\frac{n}{d}}(x)$ 是整系数多项式知 $\sum_{\substack{1 \leq k \leq n \\(k, n)=1}} w^{k t}$ 是整数, 引理 2 获证!

引理 3 对 $n\left(n \in \mathbb{N}^{*}\right)$ 阶单位根 $w=e^{i \frac{2 \pi}{n}}$, 以及任意若干个整数 $\alpha_{1}, \alpha_{2}, \cdots$, $\alpha_{m}$, 则 $\prod_{\substack{1 \leq \leq \leq n \\(k, n)=1}}\left(x-w^{k \alpha_{1}}-w^{k \alpha_{2}}-\cdots-w^{k \alpha_{m}}\right)$ 是整系数多项式.

证明 除 $x^{n}$ 外, 上式展开后的单项式形如

$$
(-1)^{j} x^{\varphi(n)-j} \prod_{i=1}^{j} w^{l_{i} \alpha_{m_{i}}}
$$

其中 $1 \leq j \leq \varphi(n), 1 \leq l_{1}<\cdots<l_{j}<n, l_{i}$ 与 $n$ 互质, $1 \leq m_{i} \leq m, 1 \leq i \leq j$.注意到这一项可与

$$
(-1)^{j} x^{\varphi(n)-j} \prod_{i=1}^{j} w^{k l_{i} \alpha_{m_{i}}}(1 \leq k \leq n,(k, n)=1)
$$

配对, 它们的系数和为 $(-1)^{j} \sum_{\substack{1 \leq k \leq n \\(k, n)=1}}\left(\prod_{i=1}^{j} w^{l_{i} \alpha_{m_{i}}}\right)^{k}$, 利用引理 2 知系数和为整数,因此引理 3 获证！

回到原题.
不妨设 $z_{1}, z_{2}, \cdots, z_{2021}$ 均是 $n$ 次单位根. 设

$$
w=e^{i \frac{2 \pi}{n}}, z_{j}=w^{\alpha_{j}}, 1 \leq j \leq 2021, \alpha_{1} \leq \alpha_{2} \leq \cdots \leq \alpha_{2021} .
$$

设

$$
f(x)=\sum_{j=1}^{2021} x^{\alpha_{j}}, g(x)=\prod_{\substack{1 \leq k \leq n \\(k, n)=1}}\left(x-f\left(w^{k}\right)\right), h(x)=x^{\alpha_{2021}}\left(f(x) f\left(\frac{1}{x}\right)-1\right) .
$$

则由题目条件知 $|f(w)|=|\xi|=1$, 即 $f(w) f\left(\frac{1}{w}\right)-1=0$. 从而 $h(w)=0$.

又因为 $w$ 是 $n$ 阶分圆多项式 $\Phi_{n}(x)$ 的根, 由 $\Phi_{n}(x)$ 是整系数不可约多项式知其是 $w$ 的最小多项式, 故 $\Phi_{n}(x) \mid h(x)$, 所以对 $(k, n)=1, w^{k}$ 均为 $\Phi_{n}(x)$ 的根, 故也是 $h(x)$ 的根.

于是

$$
1=f\left(w^{k}\right) f\left(\frac{1}{w^{k}}\right)=f\left(w^{k}\right) f\left(\bar{w}^{k}\right)=f\left(w^{k}\right) \overline{f\left(w^{k}\right)}=\left|f\left(w^{k}\right)\right|^{2},
$$

即 $\left|f\left(w^{k}\right)\right|=1$, 故 $g(x)$ 的根模长均为 1 , 又由引理 3 知 $g(x) \in \mathbb{Z}[x]$, 所以用引理 1 知 $f\left(w^{k}\right)$ 都是单位根, 当然 $\xi=f(w)$ 也是单位根, 证毕!

评注 本题是一道非常困难的多项式问题, 综合了数论与组合的技巧, 三个引理的结果都非常的漂亮, 尤其是引理 3 形式简洁, 结论优美, 配对的证法也很巧妙. 关于分圆多项式是整系数多项式的证明是容易的, 用归纳法与高斯引理即可, 分圆多项式在有理数域不可约的证明要困难一些, 参考 Dedekind 或者 Schur 给的证明.

题 8 给定正整数 $r \leq n-2$. 设 $A_{1}, A_{2}, \cdots, A_{m}$ 是 $\{1,2, \cdots, n\}$ 的 $m$ 个不同的 $r$ 元子集, 满足对任意三个不同的 $A_{i}, A_{j}, A_{k}$, 都有 $\left|A_{i} \cup A_{j} \cup A_{k}\right|>r+2$.证明:

$$
m \leq \frac{n}{r^{2}} \mathrm{C}_{n}^{r-1}
$$

证明 首先当 $r=1$ 时, 显然有 $m \leq n$ 成立.

下考虑 $r \geq 2$ 情况, 设 $S$ 为 $\{1,2, \cdots, n\}$ 的所有 $r-1$ 元子集组成的集合.

考虑二部图 $G, S$ 中的元素 $A$ 与 $\{1,2, \cdots, n\}$ 中元素 $x$ 分别对应一部分顶点, $A$ 与 $x$ 之间连边当且仅当 $A \cup x \in\left\{A_{1}, A_{2}, \cdots, A_{m}\right\}$. 设 $A$ 在 $G$ 中的度为 $\operatorname{deg}(A)$, 因为每个 $A_{i}(1 \leq i \leq r)$ 会产生 $m$ 条边, 故 $\sum_{A \in S} \operatorname{deg}(A)=m r$.

考虑二部图中“角” $(x, A, y)$ 的个数 $T$ (这里 $A$ 与 $x, y$ 均连边, $x, y$ 有序, 且允许 $x=y)$.
一方面, 对固定的 $A$, 有序的 $x, y$ 各有 $\operatorname{deg}(A)$ 种取法, 故 $T=\sum_{A \in S} \operatorname{deg}^{2}(A)$.

另一方面, 每个“角” $(x, A, y)$ 对应二元组 $(A \cup x, y)$, 注意二元组的数量不超过 $m n$. 如果两个不同的角 $(x, A, y)$ 与 $\left(x^{\prime}, A^{\prime}, y^{\prime}\right)$ 对应相同的二元组, 即 $A \cup x=A^{\prime} \cup x^{\prime}, y=y^{\prime}$, 所以 $x \neq x^{\prime}$, 故三个 $r$ 元集 $A \cup x, A \cup y, A^{\prime} \cup y^{\prime}$ 的并集恰为 $A \cup x \cup y$, 即为 $r+1$ 元集, 与题目条件矛盾!

故此对应关系是单射, 则 $T \leq m n$.

因此,

$$
m n \mathrm{C}_{n}^{r-1} \geq T \mathrm{C}_{n}^{r-1}=\mathrm{C}_{n}^{r-1} \sum_{A \in S} \operatorname{deg}^{2}(A) \stackrel{\text { 柯西 }}{\geq}\left(\sum_{A \in S} \operatorname{deg}(A)\right)^{2}=(m r)^{2},
$$

即 $m \leq \frac{n}{r^{2}} \mathrm{C}_{n}^{r-1}$.

评注 本题难点在于数据不好凑, 其关键在于对“角”的个数 $T$ 算两次, 然后在估计 $T$ 的上界用到一个单射, 就能够用上题目条件, 解决本问题.

