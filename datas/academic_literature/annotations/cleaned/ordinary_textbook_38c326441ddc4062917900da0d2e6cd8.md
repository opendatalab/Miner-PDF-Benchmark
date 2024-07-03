# 2022 年 IMO 试题解答 

万宇康<br>(湖南师范大学附属中学, 410006)<br>指导教师: 陈天择 苏林

本文介绍 2022 年 IMO 试题的解法. 这些解法, 均属作者独立完成. 不当之处, 请指正.

## I. 试 题

1. 有两种不同的硬币 $A$ 与 $B$. 现共 $n$ 个 $A$ 硬币及 $n$ 个 $B$ 硬币, 将它们任排成一列, 称连续一段相同的硬币为“同花段”. 给定正整数 $k \leq 2 n$, 可重复下列操作: 找出包含从左数起第 $k$ 个硬币之最长同花段, 然后将这个同花段中所有硬币移到整列硬币最左边.

求所有 $(n, k)$, 使不论最初状态如何, 都可经一些操作使最左边 $n$ 个硬币相同.

2. 用 $\mathbb{R}^{+}$表示所有正实数构成的集合, 求所有映射 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$, 使对所有 $x \in \mathbb{R}^{+}$都恰好有一个 $y \in \mathbb{R}^{+}$满足

$$
x f(y)+y f(x) \leq 2 .
$$

3. 令 $k$ 为一个正整数, $S$ 是由有限多个奇素数构成的集合, 证明: 至多只有一种方式将 $S$ 所有元素排成一个圆圈(旋转与反射视为同一种), 使圆圈上任相邻两数乘积都可以表示成 $x^{2}+x+k$ 的形式, 其中 $x$ 是某正整数.
4. 令 $A B C D E$ 为一凸五边形且满足 $B C=D E$. 假设在 $A B C D E$ 内部存在一点 $T$ 使得 $T B=T D, T C=T E$ 且 $\angle A B T=\angle T E A$. 令直线 $A B$ 分别与直线 $C D$ 和 $C T$ 交于点 $P$ 和 $Q$, 假设 $P, B, A, Q$ 在同一直线上按照此序列排列.令直线 $A E$ 分别与直线 $C D$ 和 $D T$ 交于点 $R$ 和 $S$, 假设 $R, E, A, S$ 在同一直线上按照此序列排列. 证明 $P, S, Q, R$ 四点共圆.

修订日期: 2022-10-15.

5. 求出所有三元正整数组 $(a, b, p)$, 满足 $p$ 是素数且

$$
a^{p}=b !+p
$$

6. 令 $n$ 为一个正整数,一个“北欧方阵” 是一个包含 1 至 $n^{2}$ 所有整数的 $n \times n$ 方格表, 其中每个方格内恰有一个数. 称两个不同方格为相邻的, 如果它们有公共边. 称一个方格为 “山谷”, 若其内的数比它所有邻格内的数都小. 一条 “上坡路径”指一个包含一或多个方格的序列, 满足:

(i) 序列的第一个方格是山谷;

(ii) 序列中随后的每个方格都和前一方格相邻;

(iii) 序列中方格内所写的数递增.

试求一个北欧方阵中上坡路径数量的最小可能值, 以 $n$ 的函数表示之.

## II. 解答与评注

题 1 有两种不同的硬币 $A$ 与 $B$. 现共 $n$ 个 $A$ 硬币及 $n$ 个 $B$ 硬币, 将它们任排成一列, 称连续一段相同的硬币为“同花段”. 给定正整数 $k \leq 2 n$, 可重复下列操作: 找出包含从左数起第 $k$ 个硬币之最长同花段, 然后将这个同花段中所有硬币移到整列硬币最左边。

求所有 $(n, k)$, 使不论最初状态如何, 都可经一些操作使最左边 $n$ 个硬币相同.

解 所求 $(n, k)$ 为

$$
L=\left\{(n, k) \mid n \in \mathbb{Z}^{+}, n \leq k \leq \frac{3 n+1}{2}\right\}
$$

之全体元素.

一方面, 若 $(n, k) \notin L$, 给出构造如下:

当 $1 \leq k<n$ 时, 令最初状态为:



则此状态一直不变, 不合条件.

当 $k \geq \frac{3 n}{2}+1$ 时(此时必有 $n \geq 2,\left\lfloor\frac{n}{2}\right\rfloor \geq 1$ ), 有 $2 n-k \leq\left\lfloor\frac{n}{2}\right\rfloor-1$, 令最初状态为:


下以 $X$ 代表连续 $\left\lceil\frac{n}{2}\right\rceil$ 个或 $\left\lfloor\frac{n}{2}\right\rfloor$ 个“A", $Y$ 代表连续 $\left\lceil\frac{n}{2}\right\rceil$ 个或 $\left\lfloor\frac{n}{2}\right\rfloor$ 个“B". 最初为 $X, Y, X, Y$, 一轮后为 $Y, X, Y, X$, 又一轮后为 $X, Y, X, Y$, 回到最初状态并将重复循环, 不合条件.

另一方面. 证明 $(n, k) \in L$, 符合题意.

记 $g$ 为硬币列中相邻不同类硬币对的个数. 如果操作过程中出现第 $1,2, \cdots, n$ 枚硬币同类情形, 则已满足条件. 如果操作过程中始终不出现第 $1,2 \cdots, n$ 枚硬币同类情形:

对每次操作, $g$ 变化量

$$
\Delta g=\alpha+\beta
$$

其中

$\alpha=\left\{\begin{array}{ll}-2, & \text { 此前第 } k \text { 至 } 2 n \text { 枚硬币不全同类(取走了中间部分的连续段) } \\ -1, & \text { 此前第 } k \text { 至 } 2 n \text { 枚硬币全同类(取走了最后一段的连续段) }\end{array}\right.$,

$\beta= \begin{cases}0, & \text { 此前第 } 1 \text { 与第 } k \text { 枚硬币同类(取走的连续段与原第一块同类) } \\ 1, & \text { 此前第 } 1 \text { 与第 } k \text { 枚硬币异类(取走的连续段与原第一块异类) }\end{cases}$

则 $\Delta g \leq 0$. 操作充分多次后, 必有 $\Delta g=0$ 恒成立, 则此时恒有第 $k, k+1, \cdots, 2 n$枚硬币同类, 第 $1, k$ 枚硬币异类, 每次操作移动一个第 $2 n$ 枚硬币所在同花段.

称一个同花段 $M$ 是“极长同花段”, 如果不存在同花段 $N$, 使 $M \neq N$, 且 $M$中硬币都在 $N$ 中. 那么任两极长同花段无公共硬币, 任一硬币恰在一个极长同花段中. 设此时极长同花段从左至右依次为

$$
C_{1}, D_{1}, C_{2}, D_{2}, \cdots, C_{m}, D_{m}, \quad\left(m \in \mathbb{N}^{+}\right)
$$

则 $D_{m}$ 至少有 $2 n-k+1$ 个硬币.

一次操作后, 为

$$
D_{m}, C_{1}, D_{1}, C_{2}, D_{2}, \cdots, C_{m},
$$

则 $C_{m}$ 至少有 $2 n-k+1$ 个硬币.

又一次操作后, 为

$$
C_{m}, D_{m}, C_{1}, D_{1}, C_{2}, D_{2}, \cdots, D_{m-1},
$$

则 $D_{m-1}$ 至少有 $2 n-k+1$ 个硬币.

若干次操作后回到

$$
C_{1}, D_{1}, C_{2}, D_{2}, \cdots, C_{m}, D_{m}
$$

而

$$
2 m(2 n-k+1) \leq 2 n<4(2 n-k+1) \text {. }
$$

故 $m=1,(n, k)$ 满足条件.

即证.

评注 利用不变及循环特例排除情况, 利用赋值单调性说明操作变化, 均为操作问题常用手法.

题 2 用 $\mathbb{R}^{+}$表示所有正实数构成的集合, 求所有映射 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$, 使对所有 $x \in \mathbb{R}^{+}$都恰好有一个 $y \in \mathbb{R}^{+}$满足

$$
x f(y)+y f(x) \leq 2 .
$$

解 所求 $f$ 为

$$
f(x)=\frac{1}{x} \quad\left(x \in \mathbb{R}^{+}\right) .
$$

一方面, 当 $f(x)=\frac{1}{x}$ 时: 对 $y \neq x$, 有

$$
x f(y)+y f(x)=\frac{x}{y}+\frac{y}{x}>2,
$$

对 $y=x$, 有

$$
x f(y)+y f(x)=\frac{x}{y}+\frac{y}{x} \leq 2 .
$$

$f$ 满足条件.

另一方面, 下证必有:

$$
f(x)=\frac{1}{x} \quad\left(x \in \mathbb{R}^{+}\right) .
$$

对每个 $x \in \mathbb{R}^{+}$, 记 $g(x)$ 为唯一正实数使

$$
x f(g(x))+g(x) f(x) \leq 2 .
$$

由(1)知 $g(g(x))=x$.

假设存在 $x \in \mathbb{R}^{+}$使 $g(x) \neq x$, 则 $g(g(x)) \neq g(x)$. 由条件

$$
\begin{gathered}
x f(x)+x f(x)>2, \\
g(x) f(g(x))+g(x) f(g(x))>2 .
\end{gathered}
$$

则

$$
f(x)>\frac{1}{x}, f(g(x))>\frac{1}{g(x)} .
$$

代入(1), 有:

$$
2>\frac{x}{g(x)}+\frac{g(x)}{x}>2
$$

矛盾.

故对每个 $x \in \mathbb{R}^{+}$, 有 $g(x)=x$, 则由 (1), 对任意 $x \in \mathbb{R}^{+}$有

$$
f(x) \leq \frac{1}{x},
$$

对任意 $y \in \mathbb{R}^{+}(y \neq x)$, 有

$$
2<x f(y)+y f(x) \leq \frac{x}{y}+y f(x) .
$$

则

$$
x f(x)>2 \frac{x}{y}-\frac{x^{2}}{y^{2}}=1-\left(1-\frac{x}{y}\right)^{2} .
$$

又

$$
\lim _{y \rightarrow x}\left(1-\left(1-\frac{x}{y}\right)^{2}\right)=1
$$

则

$$
x f(x) \geq 1
$$

结合 (2), 知 $f(x)=\frac{1}{x}$.

综上,

$$
f(x)=\frac{1}{x}\left(x \in \mathbb{R}^{+}\right) .
$$

即为满足题意的所有映射.

评注 使用题目给出的对应关系寻求有力结论.

题 3 令 $k$ 为一个正整数, $S$ 是由有限多个奇素数构成的集合, 证明: 至多只有一种方式将 $S$ 所有元素排成一个圆圈(旋转与反射视为同一种), 使圆圈上任相邻两数乘积都可以表示成 $x^{2}+x+k$ 的形式, 其中 $x$ 是某正整数.

证明 首先给出如下定义:

定义 对任意奇素数 $p, q$, 如果 $p q$ 可表示为 $x^{2}+x+k(x \in \mathbb{Z})$ 的形式, 则记为 $p R q$.

引理 若互异奇素数 $u, p, q$ 使 $u, p<q$, 且 $u R q, p R q$, 那么 $u R p$.

证明 注意到, $u q<q^{2}, p q<q^{2}$, 那么

$u q, \quad p q \in\left\{0^{2}+0+k, 1^{2}+1+k, \cdots,(q-1)^{2}+(q-1)+k\right\}$.
又注意到:如果 $l, n \in\{0,1, \cdots, q-1\}(l \neq n)$ 满足

$$
l^{2}+l+k \equiv n^{2}+n+k \quad(\bmod q)
$$

相减得:

$$
l+n+1 \equiv 0 \quad(\bmod q)
$$

则必有

$$
l+n=q-1
$$

不妨设 $u<p$, 考虑到

$$
u q \equiv p q \equiv 0 \quad(\bmod q)
$$

则存在

$$
0 \leq r<\frac{q-1}{2}(r \in \mathbb{Z})
$$

使

$$
u q=r^{2}+r+k, p q=(q-1-r)^{2}+(q-1-r)+k
$$

从而

$$
p-u=q-2 r-1
$$

则

$$
2 r+1=q-p+u \text {. }
$$

从而

$$
(q-p+u)^{2}+4 k-1=4\left(r^{2}+r+k\right)=4 u q .
$$

则

$$
u^{2}+p^{2}+q^{2}-2 u p-2 u q-2 p q+4 k-1=0 .
$$

那么

$$
4 p u=(q-p-u)^{2}+4 k-1 .
$$

即

$$
p u=\left(\frac{u+p-q-1}{2}\right)^{2}+\frac{u+p-q-1}{2}+k .
$$

那么 $u R p$.

即证.

回到原题. 我们仅需考虑存在一种把 $S$ 中元素排在图周上而且满足条件的
方法的情形.

按题目要求排列, 设圆周上素数依次为 $P_{1}, P_{2}, \cdots, P_{m}(m=|s|$, 仅需考察 $m \geq 4$ 时), 下标模 $m$ 理解. 下对任意 $1 \leq i, j \leq m(i \neq j)$, 如果 $P_{i} R P_{j}$, 那么在 $P_{i}, P_{j}$ 之间连一条线段 (以下对素数以及放素数的点用同一记号). 从而 $P_{i}, P_{i+1}$连线段 $(1 \leq i \leq m)$, 我们下面证明得到了 $m$ 边形 $P_{1} P_{2} \cdots P_{m}$ 的一个三角剖分.

设

$$
P_{i 1}=\max \left\{P_{1}, P_{2}, \cdots, P_{m}\right\}
$$

由 $P_{i_{1}-1} R P_{i_{1}}, P_{i_{1}} R P_{i_{1}+1}$ 有(由引理) $P_{i_{1}-1} R P_{i_{1}+1}$, 即 $P_{i_{1}-1} P_{i_{1}+1}$ 连线段.

对多边形 $P_{1} P_{2} \cdots P_{i 1-1} P_{i 1+1} \cdots P_{m}$, (它每相邻顶点都用线段相连), 可重复上述操作, 即得存在 $m-3$ 条 $m$ 边形 $P_{1} P_{2} \cdots P_{m}$ 对角线, 它们给出 $m$ 边形的一个三角剖分. 所以, 共连至少 $2 m-3$ 条线段. 记 $A=\{p \mid p R q, p<q, p, q \in s\}$,即

$$
|A| \geq 2 m-3
$$

注意到, 对每个奇素数 $q$, 存在至多 2 个奇素数 $p<q$ 使 $p R q$.

事实上, 假设奇素数 $\alpha<\beta<\gamma<q$ 使

$$
\alpha R q, \beta R q, \gamma R q \text {. }
$$

由 $0<\alpha q<\beta q<\gamma q<q^{2}$ 知: 存在

$$
i, l, n \in\{0,1, \cdots, q-1\} \quad(i<l<n)
$$

使

$$
\alpha q=i^{2}+i+k, \beta q=l^{2}+l+k, \gamma q=n^{2}+n+k .
$$

由(1)有

$$
i+l=i+n=l+n=q-1,
$$

矛盾. 记

$$
A_{q}=\{p \mid p R q, p<q, p \in s\}
$$

有

$$
\begin{aligned}
|A| & =\sum_{q \in s}\left|A_{q}\right| \\
& \leq 1+\sum_{q \in s, q \text { 不为最小或次小数 }}\left|A_{q}\right| \\
& \leq 1+2(m-2)
\end{aligned}
$$

$$
=2 m-3 \text {. }
$$

结合(2), (3), 知(2)等号成立, 故恰连 $2 m-3$ 条线段, 它们给出 $m$ 边形 $P_{1} P_{2} \cdots P_{m}$的一个三角剖分. 视 $P_{1}, P_{2}, \cdots, P_{m}$ 为点, 线段为边, 得简单图 $G$.

下面证明唯一性. 假设 $G$ 有一个不同于 $P_{1} P_{2} \cdots P_{m}$ 的 Hamilton 圈 $C$, 则 $C$至少含三角剖分中一条对角线 $P_{g} P_{h}$. 在三角剖分中, 将 $P_{g} P_{h}$ 一侧点染为红色,另一侧点染为蓝色, $P_{g}, P_{h}$ 不染色. 在 $C$ 中, $P_{g}, P_{h}$ 相邻, 故存在一个红点与一个蓝点相邻. 由三角剖分不存在对角线相交, 这不可能, 故 $G$ 只有一个 Hamilton 圈, 即证.

评注 注意到相邻元素在大小关系约束下的性质, 转化为图论问题解决.

题 4 令 $A B C D E$ 为一凸五边形且满足 $B C=D E$. 假设在 $A B C D E$ 内部存在一点 $T$ 使得 $T B=T D, T C=T E$ 且 $\angle A B T=\angle T E A$. 令直线 $A B$ 分别与直线 $C D$ 和 $C T$ 交于点 $P$ 和 $Q$, 假设 $P, B, A, Q$ 在同一直线上按照此序列排列. 令直线 $A E$ 分别与直线 $C D$ 和 $D T$ 交于点 $R$ 和 $S$, 假设 $R, E, A, S$ 在同一直线上按照此序列排列. 证明 $P, S, Q, R$ 四点共圆.



证明 因为 $T B=T D, T C=T E, B C=D E$. 所以 $\triangle T B C \cong \triangle T D E$. 因为

$$
\begin{gathered}
\angle S T E=\pi-\angle E T D=\pi-\angle C T B=\angle Q T B, \\
\angle S E T=\angle A E T=\angle A B T=\angle Q B T .
\end{gathered}
$$

所以 $\triangle S T E \sim \triangle Q T B$. 故

$$
\frac{S T}{T Q}=\frac{T E}{T B}=\frac{T C}{T D}
$$

因此

$$
S T \cdot T D=Q T \cdot T C,
$$

从而 $S, C, D, Q$ 四点共圆. 此时

$$
\angle S R P=\angle S D C-\angle T S E=\angle S Q C-\angle T Q B=\angle S Q P
$$

故 $P, S, Q, R$ 共圆.

评注 简单的几何题, 利用基础条件得到全等-相似-共圆即可.

题 5 求出所有三元正整数组 $(a, b, p)$, 满足 $p$ 是素数且

$$
a^{p}=b !+p
$$

解 一方面, 易验如下两组解满足题目条件:

$$
(a, b, p)=(2,2,2),(3,4,3) \text {. }
$$

另一方面, 我们证明 $(a, b, p)$ 只有(1)中两组解.

首先 $b<2 p$. 因为假设 $b \geq 2 p$, 则 $p^{2} \mid b !$, 故 $p \mid a^{p}$ 但 $p^{2} \nmid a^{p}$, 从而 $p \mid a$, 矛盾.从而 $b<2 p$.

如果 $p=2$, 则对 $b=1,2,3$, 有 $b !+p=3,4,8$. 从而 $(a, b, p)=(2,2,2)$.

如果 $p=3$, 则对 $b=1,2,3,4,5$, 有 $b !+p=4,5,9,27,123$. 从而 $(a, b, p)=(3,4,3)$.

如果 $p \geq 5$. 下证原方程无解.

(1) 若 $b \geq p$. 则 $p \leq b<2 p$. 由 $p \mid b$ ! 知 $p \mid a^{p}$, 则 $p \mid a$. 注意到 $a^{p}=b !+p$.则 $\operatorname{gcd}\left(a^{p}, b !\right)=p$. 所以 $a$ 的素因子要么等于 $p$, 要么大于 $b$.

当 $a$ 有大于 $b$ 的素因子时, 有 $a>b p$. 则

$$
b !+p=a^{p}>b^{p} p^{p} .
$$

又

$$
p|b !+p, p| b^{p} p^{p}
$$

则 $b ! \geq b^{p} p^{p}$. 又

$$
b !=p ! \cdot \frac{b !}{p !}<p^{p} b^{b-p}<b^{p} p^{p}
$$

矛盾.

当 $a$ 没有大于 $b$ 素因子时, $a$ 为 $p$ 幕次. 由 $p>3$. 知

$$
\begin{gathered}
b !+p<(2 p)^{2 p}+p=4^{p} p^{2 p}+p<p^{3 p}+p \\
p|b !+p, p|(2 p)^{2 p}+p, p \mid p^{3 p}
\end{gathered}
$$

有:

$$
a^{p}=b !+p<p^{3 p}
$$

则 $a=p, p^{2}$.

对任意正整数 $l$, 记 $v_{2}(l)$ 为 $l$ 标准分解中 2 的幂次. 对于 $a=p^{2}$, 考虑到

$$
\begin{aligned}
v_{2}\left(a^{p}-p\right) & =v_{2}\left(p^{2 p-1}-1\right)=v_{2}(p-1)+v_{2}\left(\sum_{k=0}^{2 p-2} p^{k}\right) \\
& =v_{2}(p-1)<v_{2}(b !)
\end{aligned}
$$

矛盾.

对于 $a=p$. 如 $a=p=5$, 有 $b !=5^{5}-5=3120$. 又 $6 !<3120<7 !$, 矛盾.

如 $a=p>5$.

$$
\begin{aligned}
v_{2}\left(p^{p-1}-1\right) & =v_{2}\left(\left(1+\left(p^{2}-1\right)\right)^{\frac{p-1}{2}}-1\right) \\
& =v_{2}\left(\sum_{i=1}^{\frac{p-1}{2}} \mathrm{C}_{\frac{p-1}{2}}^{i}\left(p^{2}-1\right)^{i}\right) \\
& =v_{2}\left(\sum_{i=1}^{\frac{p-1}{2}} \mathrm{C}_{\frac{p-1}{2}}^{i}\left(p^{2}-1\right)^{i-1}\right)+v_{2}\left(p^{2}-1\right)
\end{aligned}
$$

而对 $i=1,2, \cdots, \frac{p-1}{2}$, 有

$$
\begin{aligned}
v_{2}\left(\mathrm{C}_{\frac{p-1}{2}}^{i}\left(p^{2}-1\right)^{i-1}\right) & =(i-1) v_{2}\left(p^{2}-1\right)+v_{2}\left(\mathrm{C}_{\frac{p-1}{2}}^{i}\right) \\
& \geq 3 i-3+v_{2}\left(\frac{p-1}{2 i} \mathrm{C}_{\frac{p-3}{2}}^{i-1}\right) \\
& \geq 3 i-3+v_{2}\left(\frac{p-1}{2}\right)-v_{2}(i) \\
& \geq 3\left(2^{v_{2}(i)}-1\right)+v_{2}\left(\frac{p-1}{2}\right)-v_{i}(2) \\
& \geq 3 v_{2}(i)-v_{2}(i)+v_{2}\left(\frac{p-1}{2}\right) \\
& \geq v_{2}\left(\frac{p-1}{2}\right)
\end{aligned}
$$

仅在 $i=1$ 时, 上述等号全成立. 此时

$$
\begin{aligned}
v_{2}\left(p^{p-1}-1\right) & =v_{2}\left(\mathrm{C}_{\frac{p-1}{2}}^{1}\left(p^{2}-1\right)^{1-1}\right)+v_{2}\left(p^{2}-1\right) \\
& =v_{2}\left(\frac{p-1}{2}\right)+v_{2}(p-1)+v_{2}(p+1) \\
& <v_{2}(2)+v_{2}\left(\frac{p-1}{2}\right)+v_{2}(p-1)+v_{2}(p+1) \\
& \leq v_{2}(b !), \quad(\text { 用到 } p>5)
\end{aligned}
$$

又

$$
\begin{gathered}
v_{2}\left(a^{p}-p\right)=v_{2}\left(p^{p}-p\right)-v_{2}\left(p^{p-1}-1\right), \\
b !=a^{p}-p,
\end{gathered}
$$

矛盾.

(2) 若 $b<p$. 则

$$
a^{p}=b !+p<b^{p}+p<b^{p}+p b^{p-1}<(b+1)^{p}
$$

故 $a \leq b$, 则 $a<p$.

而 $a^{p}=b !+p>1$, 则 $a>1$. 任取 $a$ 的素因子 $q$, 有 $q \leq a \leq b<p$, 则

$$
q\left|a^{p}, q\right| b !
$$

则 $q \mid p$. 矛盾. 故 $p \geq 5$ 时原方程无解. 综上, $(a, b, p)=(2,2,2),(3,4,3)$.

评注考察素因子, 需要细致分类.

题 6 令 $n$ 为一个正整数, 一个“北欧方阵” 是一个包含 1 至 $n^{2}$ 所有整数的 $n \times n$ 方格表, 其中每个方格内恰有一个数. 称两个不同方格为相邻的, 如果它们有公共边. 称一个方格为 “山谷”, 若其内的数比它所有邻格内的数都小. 一条“上坡路径”指一个包含一或多个方格的序列, 满足:

(i) 序列的第一个方格是山谷;

(ii) 序列中随后的每个方格都和前一方格相邻;

(iii) 序列中方格内所写的数递增.

试求一个北欧方阵中上坡路径数量的最小可能值, 以 $n$ 的函数表示之.

解 一个北欧方阵中上坡路径的最小可能值为 $2 n^{2}-2 n+1$.

一方面, 我们证明至少共 $2 n^{2}-2 n+1$ 条上坡路径.

对任一二元集 $\{\alpha, \beta\}$ ( $\alpha, \beta$ 为相邻方格), 下面找一条上坡路径 $l_{\{\alpha, \beta\}}$, 使 $l_{\{\alpha, \beta\}}$ 至少含两方格, 且最后两格为 $\alpha, \beta$ 排列.

不妨设 $\beta$ 标数小于 $\alpha$. 我们任选邻格 $\gamma$, 使 $\gamma$ 标数小于 $\beta$ 标数, 再任选 $\gamma$ 邻格, 使其标数小于 $\gamma$ 标数, $\cdots$, 最后到达山谷. 那么即得到满足要求的上坡路径.

由 $l_{\{\alpha, \beta\}}$ 性质知, 对互异的 $\{\alpha, \beta\}$ ( $\alpha, \beta$ 为相邻方格), 必有 $l_{\{\alpha, \beta\}}$ 互异.

而 $\{\alpha, \beta\}$ ( $\alpha, \beta$ 为相邻方格)共 $2 n^{2}-2 n$ 组, 填 1 的方格自成一上坡路径, 从而共至少 $2 n^{2}-2 n+1$ 条上坡路径.

另一方面, 可以证明, 可做到恰有 $2 n^{2}-2 n+1$ 条上坡路经.
引理 1 对任意一棵有根树 $T$. 我们可给 $T$ 每个顶点标上 $1,2 \cdots,|T|$ 中一个数, 使不同点标数互异. 而且, 对每个非根 (根记为 $R$ ) 的顶点 $v$, 如果存在一条由 $v$ 至 $R$ 顶点不重的路径经过 $v^{\prime}\left(v^{\prime}\right.$ 可以为 $R$, 但不可为 $\left.v\right)$, 则 $v$ 标数大于 $v^{\prime}$.

证明 对 $|T|$ 归纳. $|T|=2$ 时令 $R$ 标 1 , 另一点标 2 即可.

设 $|T|=m-1(m \geq 3)$ 时已证, 下考察 $|T|=m$ 时.

取 $T$ 一片叶子 $L$. 设 $T$ 顶点集为 $V$.

考察树 $T[V \backslash\{L\}]$ ( $T$ 限制在 $V \backslash\{L\}$ 上子图). 对 $T \subset V \backslash\{L\}$ 按归纳假设标数, 再给 $L$ 标 $|T|$.

这种标法满足条件(因为对任一 $v \in V \backslash\{L\}$, 在 $T$ 中 $v$ 至 $R$ 任一路径不经过 $L)$ ，归纳完毕.

引理 2 可以为 $n \times n$ 方格表黑白二染色使:

(1) 任两白格不相邻,

(2) 以方格表黑方格为顶点, 相邻黑方格连边作图 $T$, 则 $T$ 为树.

证明 记方格表从上至下第 $i$ 行, 从左至右第 $j$ 列公共格为 $A_{i j}, 1 \leq i, j \leq n$.

对 $n \equiv 2,3(\bmod 3)$. 令

$$
A_{i j}(i=1, j \not \equiv 5 \quad(\bmod 6)), A_{i j}(i \neq 1, j \equiv 2 \quad(\bmod 3))
$$

及

$$
A_{i j}\left(i \neq 1, j \equiv 1,3 \quad(\bmod 3), i \equiv \frac{(-1)^{\left[\frac{j+2}{3}\right]-1}}{2} \quad(\bmod 2)\right)
$$

为黑格.

对 $n=1(\bmod 3)$. 令

$$
A_{i j}(i=1, j \not \equiv 4 \quad(\bmod 6)), A_{i j}(i \neq 1, j \equiv 1 \quad(\bmod 3))
$$

及

$$
A_{i j}\left(i \neq 1, j \equiv 0,2 \quad(\bmod 3), i \equiv \frac{(-1)^{\left[\frac{j}{3}\right]-1}}{2} \quad(\bmod 2)\right)
$$

为黑格.

上述构造满足条件, 引理 2 得证. 下图为 $n=12$ 构造示例.

回到原题. 用引理 2 方式为方格表染色, 为引理 2 中 $T$ 任取一根. 再依引理 1 方式为 $T$ 标数. 对引理 2 中白格任标数 $|T|+1,|T|+2, \cdots,|T|+2 n$, 则黑格标数总小于白格标数. 对任一二元集 $\{\alpha, \beta\}$ ( $\alpha, \beta$ 为相邻方格), 有唯一的上坡路径 $l$, 使 $l$ 至少含两方格, 且最后的两格为 $\alpha, \beta$ 排列. 事实上, 只有唯一的山谷 $(T$的根).



如果 $\alpha, \beta$ 均为黑格, 那么 $\alpha, \beta$ 为 $T$ 中相邻点. 由有根树性质, $T$ 中有唯一的路径 $p_{\alpha}$ 由 $\alpha$ 至 $T$ 的根, 有唯一路径 $p_{\beta}$ 由 $\beta$ 至 $T$ 的根, 且 $\beta$ 在 $p_{\alpha}$ 中与 $\alpha$ 在 $p_{\beta}$中恰一个成立. 所以 $l$ 唯一(不妨 $\beta$ 在 $p_{\alpha}$ 中, 那么 $l$ 必为 $p_{\alpha}$ 中方格之排列).

如果 $\alpha, \beta$ 中至少一个为白格.

不妨设 $\alpha$ 为白格, 由引理 2 条件, $\beta$ 为黑格, 由有根树性质, $T$ 中有唯一的路径由 $\beta$ 至 $T$ 的根, $l$ 唯一.

综上, $l$ 唯一. 从而含至少 2 个方格的上坡路径至多 $2 n^{2}-2 n$ 条.

而山谷只有一个. 上坡路径至多 $2 n^{2}-2 n+1$ 条. 构造完毕, 即证.

评注 利用图论结构, 构造相应的染色方式即可. 在猜出结论后, 容易探索构造方法。

