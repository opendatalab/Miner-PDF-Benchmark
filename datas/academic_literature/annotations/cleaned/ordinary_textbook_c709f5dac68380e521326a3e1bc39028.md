# 好题与妙解（九） 

- 2019 年新星夏季精品营两次测试题解析

冷岗松 罗振华 吴尉迟

2019 年 5 月底, 上海数学新星夏季精品营举行了两次测试 (小考). 每次测试四道题, 时间为两个小时 50 分钟. 这两次测验试题较为有趣, 下面就介绍这些试题及给出相应的解答. 我们将用题 $1 . x$ 表示第 1 次测试的第 $x$ 题, 题 $2 . y$ 的意义类似. 西安交大附中的金磊老师也参与了其中几何题的讨论, 在此表示感谢。

## I. 试 题

题 1.1 设 $n \geq 16$ 是整数, $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且满足

$$
a_{1}+a_{2}+\cdots+a_{n}=1, \quad a_{1}+2 a_{2}+\cdots+n a_{n}=2 .
$$

证明:

$$
\left(a_{2}-a_{1}\right) \sqrt{2}+\left(a_{3}-a_{2}\right) \sqrt{3}+\cdots+\left(a_{n}-a_{n-1}\right) \sqrt{n}<0 .
$$

题 1.2 求所有的正整数 $a, b, c$, 使得

$$
\left(2^{a}-1\right)\left(3^{b}-1\right)=c !
$$

题 1.3 点 $O$ 是 $\triangle A B C$ 外接圆圆心, 含点 $A$ 的弧 $\widehat{B C}$ 的中点为 $S$, 点 $T$ 在不包含点 $A$ 的弧 $\overparen{B C}$ 上. 点 $M$在 $\odot O$ 上且 $S M / / O T$. 点 $P$ 在线段 $S M$ 上. 过点 $P$ 作 $M B$ 的平行线交 $A B$ 于点 $F$; 过点 $P$ 作 $M C$ 的平行线交 $A C$ 于点 $E$. 点 $Q$ 在 $\odot O$ 上, 使得 $A T$ 是 $\angle P A Q$ 的角平分线. 证明: $Q E=Q F$.



修订日期: 2019-06-25.
题 1.4 设 $A_{1}, A_{2}, \cdots, A_{n}(n \geq 2)$ 是一条直线上的线段, 满足

(1) $A_{i} \cap A_{i+1} \neq \emptyset, \forall 1 \leq i \leq n-1$.

(2) $\forall 1 \leq i<j \leq n$, 如果 $i-j$ 是偶数, 则 $A_{i} \cap A_{j} \neq \emptyset$.

求最大的 $k=k(n)$ 使得存在一点, 它属于至少 $k$ 个线段.

题 2.1 设 $x, y, z$ 是非零复数, 求

$$
F=\min \left\{\frac{|x-y|}{|z|}, \frac{|y-z|}{|x|}, \frac{|z-x|}{|y|}\right\}
$$

的最大值.

题 2.2 如图, $M$ 为圆外切四边形 $A B C D$ 边 $B C$ 上一点, $X, Y, Z$ 分别为 $\triangle M A B, \triangle M C D, \triangle M A D$ 内心, $X Z$交 $A M$ 于 $Q, Y Z$ 交 $D M$ 于 $P, H$ 为 $\triangle X Y Z$ 垂心. 证明: $P, H, Q$ 共线.



题 2.3 设图 $G$ 的顶点集为 $V$, 边集为 $E,|V|=n \geq 5$. 现在用两种颜色染 $G$的边 (每条边染且仅染一种颜色), 使得不存在同色的长为 $3,4,5$ 的圈. 证明:

$$
|E| \leq\left\lfloor\frac{n^{2}}{3}\right\rfloor
$$

题 2.4 设 $p$ 是素数, 序列 $\left\{u_{n}\right\}$ 定义为: 当 $0 \leq n \leq p-1$ 时, $u_{n}=n$; 当 $n \geq p$ 时, $u_{n}=p u_{n+1-p}+u_{n-p}$. 证明:

$$
v_{p}\left(u_{n}\right)=v_{p}(n),
$$

其中 $v_{p}(m)$ 表示使得 $p^{k} \mid m$ 的最大整数 $k$.

## II . 解 答

题 1.1 设 $n \geq 16$ 是整数, $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且满足

$$
a_{1}+a_{2}+\cdots+a_{n}=1, \quad a_{1}+2 a_{2}+\cdots+n a_{n}=2 .
$$

证明:

$$
\left(a_{2}-a_{1}\right) \sqrt{2}+\left(a_{3}-a_{2}\right) \sqrt{3}+\cdots+\left(a_{n}-a_{n-1}\right) \sqrt{n}<0 .
$$

证明 由条件知, $a_{1}=a_{3}+2 a_{4}+\cdots+(n-2) a_{n}$. 要证不等式等价于

$$
\begin{aligned}
& -a_{1} \sqrt{2}+a_{2}(\sqrt{2}-\sqrt{3})+\cdots+a_{n-1}(\sqrt{n-1}-\sqrt{n})+a_{n} \sqrt{n}<0 \\
\Leftrightarrow & -\left(a_{3}+2 a_{4}+\cdots+(n-2) a_{n}\right) \sqrt{2}+a_{2}(\sqrt{2}-\sqrt{3})+\cdots+
\end{aligned}
$$

$$
\begin{aligned}
& a_{n-1}(\sqrt{n-1}-\sqrt{n})+a_{n} \sqrt{n}<0 \\
\Leftrightarrow & a_{2}(\sqrt{2}-\sqrt{3})+a_{3}(\sqrt{3}-\sqrt{4}-\sqrt{2})+a_{4}(\sqrt{4}-\sqrt{5}-2 \sqrt{2})+\cdots+ \\
& a_{n-1}(\sqrt{n-1}-\sqrt{n}-(n-3) \sqrt{2})+a_{n}(\sqrt{n}-(n-2) \sqrt{2})<0 .
\end{aligned}
$$

注意到当 $n \geq 16$ 时, $\sqrt{n}-(n-2) \sqrt{2}<0$. 故在上式中, $a_{2}, a_{3}, \cdots, a_{n}$ 的系数均小于 0, 故成立.

评注 这是一道简单的代数题, 约 $60 \%$ 同学做对此题. 此题只需将 $a_{1}$ 代入所证不等式, 便可得 $a_{i}(2 \leq i \leq n)$ 的系数均为负数.

题 1.2 求所有的正整数 $a, b, c$, 使得

$$
\left(2^{a}-1\right)\left(3^{b}-1\right)=c ! .
$$

解 所求 $(a, b, c)$ 为 $(1,1,2),(2,1,3),(2,2,4),(4,2,5),(6,4,7)$.

我们需要用到以下熟知结论, 即升幂定理:

引理 设 $a, n \in \mathbb{N}^{*}, a>1, p$ 为素奇数, 且 $p \mid a-1$, 则

$$
v_{p}\left(a^{n}-1\right)=v_{p}(a-1)+v_{p}(n),
$$

其中, $v_{q}(m)$ 表示正整数 $m$ 中所含素数 $q$ 的幂次.

回到原题. 当 $c=1,2$ 时, 经枚举知此时解为 $(a, b, c)=(1,1,2)$.

下设 $c \geq 3$, 则 $3 \mid c$. 又 $\left(3,3^{b}-1\right)=1$, 故 $3 \mid 2^{a}-1$. 从而 $2 \mid a$.

记 $a=2 t(t \in \mathbb{N})$. 则由引理知,

$$
v_{3}\left(2^{a}-1\right)=v_{3}\left(\left(2^{2}\right)^{t}-1\right)=1+v_{3}(t)
$$

而

$$
v_{3}\left(2^{a}-1\right)=v_{3}(c !)=\sum_{m=1}^{+\infty}\left[\frac{c}{3^{m}}\right]
$$

先考虑 $c \geq 9$ 的情形. 则

$$
\left[\frac{c}{3^{m}}\right] \geq\left[\frac{c}{3}\right]+\left[\frac{c}{9}\right] \geq \frac{c-2}{3}+1
$$

从而, $v_{3}(t) \geq \frac{c-2}{3}$, 故 $t \geq 3^{\frac{c-2}{3}}$.于是,

$$
c !=\left(2^{a}-1\right)\left(s^{b}-1\right) \geq 2^{2 \cdot 3^{\frac{c-2}{3}}}
$$

当 $c=9$ 时, 经检验上式不成立. 又对任意 $c \geq 10, \frac{c !}{(c-1) !}=c$,

$$
\frac{2^{2 \cdot 3^{\frac{c-2}{3}}}}{2^{2 \cdot 3^{\frac{c-3}{3}}}}=2^{2 \cdot 3^{\frac{c-3}{3}}\left(3^{\frac{1}{3}}-1\right)}>2^{\frac{1}{2} \cdot 3^{\frac{c-3}{3}}}>c .
$$

故该式对任意 $c \geq 9$ 均不成立.

对 $c \leq 8$ 的情况, 枚举即知此时解为 $(2,1,3),(2,2,4),(4,2,5),(6,4,7)$.

综上, 所有解为 $(a, b, c)=(1,1,2),(2,1,3),(2,2,4),(4,2,5),(6,4,7)$.

评注 此题是中等难度的数论题, 约 $33 \%$ 的同学做对此题. 此题的关键在于利用升幕定理和勒让德公式对等式两边关于 3 的幂次进行估计,得到 $c \geq 9$ 时不成立. 对于较小的 $c$ 采取枚举的策略.

值得指出的是, 对等式两边关于 2 的幂次估计, 或同时进行 2,3 幕次的估计,都是可行的. 需要注意的是关于素数 2 的升幂定理与奇素数时有所不同, 这是容易混淆的。

题 1.3 点 $O$ 是 $\triangle A B C$ 外接圆圆心, 含点 $A$ 的弧 $\widehat{B C}$ 的中点为 $S$, 点 $T$ 在不包含点 $A$ 的弧 $\overparen{B C}$ 上. 点 $M$ 在 $\odot O$ 上且 $S M / / O T$. 点 $P$ 在线段 $S M$ 上. 过点 $P$ 作 $M B$ 的平行线交 $A B$ 于点 $F$; 过点 $P$ 作 $M C$ 的平行线交 $A C$ 于点 $E$. 点 $Q$ 在 $\odot O$ 上, 使得 $A T$ 是 $\angle P A Q$ 的角平分线. 证明: $Q E=Q F$.



证明 因为 $F P / / B M, E P / / C M$, 所以

$$
\frac{F B}{P M}=\frac{\sin \angle P M B}{\sin \angle F B M}=\frac{\sin \angle P M C}{\sin \angle E C M}=\frac{E C}{P M},
$$

即 $F B=E C$. 又 $S B=S C$ 且 $\angle S B F=\angle S C E$, 故 $\triangle S B F \cong \triangle S C E$. 从而, $S F=S E$.

于是, 要证 $Q E=Q F$, 只需证 $S Q \perp E F$.

又由 $\triangle S B F \cong \triangle S C E$ 知, $\angle S F A=\angle S E A$, 故 $S, A, F, E$ 四点共圆. 而 $\angle A F P+\angle A E P=\angle A B M+\angle A C E=180^{\circ}$, 故 $A, F, P, E$ 四点共圆. 从而,
$S, A, F, P, E$ 五点共圆.

$$
\begin{aligned}
\angle E S Q+\angle S E F & =\angle E S P+\angle P S Q+180^{\circ}-\angle S A F \\
& =\angle E A P+\angle M A Q+90^{\circ}-\frac{1}{2} \angle B A C \\
& =\angle E A P+\angle M A T+\angle T A Q+90^{\circ}-\frac{1}{2} \angle B A C \\
& =\angle E A T+\angle M A T+90^{\circ}-\frac{1}{2} \angle B A C \\
& =\angle C A T+\angle J A T+90^{\circ}-\frac{1}{2} \angle B A C \\
& =90^{\circ} .
\end{aligned}
$$

其中, $S, T$ 关于 $Q O$ 对径点分别为 $J, K$. 则 $\overparen{J T}=\widehat{K S}=\overparen{T M}$. 即 $S Q \perp E F$. 从而 $Q F=Q E$.

评注 这是一道中等难度的几何题, 考试中约 $49 \%$ 的同学做对此题. 本解法先通过全等三角形导出 $S E=S F$, 这就把结论转化为证明 $S Q \perp E F$, 只需利用 $S, A, F, P, E$ 五点共圆及导角不难证明此结论.

题 1.4 设 $A_{1}, A_{2}, \cdots, A_{n}(n \geq 2)$ 是一条直线上的线段, 满足

(1) $A_{i} \cap A_{i+1} \neq \emptyset, \forall 1 \leq i \leq n-1$.

(2) $\forall 1 \leq i<j \leq n$, 如果 $i-j$ 是偶数, 则 $A_{i} \cap A_{j} \neq \emptyset$.

求最大的 $k=k(n)$ 使得存在一点, 它属于至少 $k$ 个线段.

证明 $k_{\max }=\left[\frac{n+3}{2}\right]$.

(1) 先证 $k_{\max } \geq\left[\frac{n+3}{2}\right]$.

不妨设 $A_{1}, \cdots, A_{n}$ 分布在数轴上, $A_{i}$ 对应区间 $\left[x_{i}, y_{i}\right]$. 设

$$
S_{1}=\{i \mid 1 \leq i \leq n, i \text { 为奇数 }\}, S_{2}=\{i \mid 1 \leq i \leq n, i \text { 为偶数 }\} \text {. }
$$

由条件 $(2)$ 和海莱定理知,

$$
\bigcap_{i \in S_{1}} A_{i} \neq \emptyset, \bigcap_{i \in S_{2}} A_{i} \neq \emptyset .
$$

取 $a \in \bigcap_{i \in S_{1}} A_{i}, b \in \bigcap_{i \in S_{2}} A_{i}$. 不妨设 $a \leq b\left(a>b\right.$ 的情形类似可证), 设 $y_{k}=$ $\min _{i \in S_{1}}\left\{y_{i}\right\}$, 那么对任意 $j \in S_{1}$, 由于 $A_{k} \cap A_{j} \neq \emptyset$, 故 $x_{j} \leq a \leq y_{k} \leq y_{j}$, 从而 $\left[a, y_{k}\right] \subset A_{j}$.

对 $k \pm 1 \in S_{2}, b \in A_{k \pm 1}, A_{k \pm 1} \cap A_{k} \neq \emptyset$.

(i) $b>y_{k}$, 则由 $b$ 定义知, $y_{k \pm 1} \geq b>y_{k}$, 结合条件 (2) 可得, $x_{k \pm 1} \leq y_{k}$. 于是, $y_{k} \in A_{k \pm 1}$, 故 $y_{k}$ 属于至少 $\left|S_{1}\right|+1=\left[\frac{n+1}{2}\right]+1=\left[\frac{n+3}{2}\right]$ 条线段.
(ii) $b \leq y_{k}$, 则 $b \in\left[a, y_{k}\right]$, 故由 $y_{k}$ 的极小性知, $b \in A_{i}, \forall 1 \leq i \leq n$. 所以 $b$ 属于至少 $n \geq\left[\frac{n+3}{2}\right]$ 条线段 $(n \geq 2)$.

(2) 下证 $k_{\max } \leq\left[\frac{n+3}{2}\right]$.

记 $t=\left[\frac{n}{2}\right], t \in \mathbb{N}$. 令 $A_{2 k-1}=[0, k], A_{2 k}=[k, t+1](k=1,2, \cdots, t) . A_{n}=$ $[0, t+1]$ (若 $n$ 为奇数). 先验证该构造满足题设条件

对于 (1), $k \in A_{2 k-1} \cap A_{2 k},[k, k+1] \subset A_{2 k} \cap A_{2 k+1}(k=l, 2, \cdots, t)$.

对于 (2), 若 $i, j$ 同奇,则 $0 \in A_{i} \cap A_{j}$; 若 $i, j$ 同偶, 则 $1 \in A_{i} \cap A_{j}$;

注意到 $[0, t+1]$ 上任意一点, 至多包含在 $\left[\frac{n+1}{2}\right]+1=\left[\frac{n+3}{2}\right]$ 条线段中. 故 $k \leq\left[\frac{n+3}{2}\right]$.

综上, $k_{\max }=\left[\frac{n+3}{2}\right]$.

评注 这是一道较难的组合题, 考试中约 $16 \%$ 的同学做对此题. 此题的想法是对下标按奇偶分类, 再由海莱定理可取所有奇下标的 $A_{i}$ 的公共点 $a$ 和所有偶下标的 $A_{i}$ 的公共点 $b$. 再对 $a, b$ 和 $A_{i}$ 的端点进行位置分析可得 $k_{\max }$ 的下界.

$k_{\text {max }}$ 的上界需要构造例子, 但也并不容易, 一个可行的方案是: 先取一个足够大的闭区间, 令所有奇下标 $A_{i}$ 均包含该区间左端点, 所有偶下标 $A_{i}$ 均包含该区间右端点, 这样便保证了条件 (2). 为了使 $k$ 尽可能小和保证条件 (1) 成立, 想法是使某些 $A_{i}, A_{i+1}$ 的交点恰好一个. 故可取 $A_{2 k-1}, A_{2 k}$ 恰一个交点, 且奇下标 $A_{i}$ 右端点严格增, 偶下标 $A_{i}$ 左端点自然需严格减。

题 2.1 设 $x, y, z$ 是非零复数, 求

$$
F=\min \left\{\frac{|x-y|}{|z|}, \frac{|y-z|}{|x|}, \frac{|z-x|}{|y|}\right\}
$$

的最大值.

解法 1 设 $x, y, z$ 分别对应复平面的点 $X, Y, Z$, 则

$$
F=\min \left\{\frac{X Y}{O Z}, \frac{Y Z}{O X}, \frac{Z X}{O Y}\right\} .
$$

设 $\triangle X Y Z$ 的重心为 $G$. 由重心性质知,

$$
\begin{aligned}
O X^{2}+O Y^{2}+O Z^{2} & =G X^{2}+G Y^{2}+G Z^{2}+3 O G^{2} \\
& \geq G X^{2}+G Y^{2}+G Z^{2} \\
& =\frac{1}{3}\left(X Y^{2}+Y Z^{2}+Z X^{2}\right)
\end{aligned}
$$

故 $\frac{X Y}{O Z}, \frac{Y Z}{O X}, \frac{Z X}{O Y}$ 至少有一个不大于 $\sqrt{3}$. 这说明 $F \leq \sqrt{3}$.

另一方面, 当 $\triangle X Y Z$ 是正三角形且 $O$ 是重心时, $F=\sqrt{3}$.
解法 2 (重庆育才中学刘艺程) 一方面, 取 $(x, y, z)=\left(1, \frac{-1+\sqrt{3} \mathrm{i}}{2}, \frac{-1-\sqrt{3} \mathrm{i}}{2}\right)$, 有 $F=\sqrt{3}$.

另一方面, 若 $F>\sqrt{3}$, 则 $|x-y|>\sqrt{3}|z|$, 从而

$$
(x-y)(\bar{x}-\bar{y})>3 z \bar{z} \Leftrightarrow x \bar{x}+y \bar{y}-x \bar{y}-\bar{x} y>3 z \bar{z} .
$$

同理,

$$
y \bar{y}+z \bar{z}-y \bar{z}-\bar{y} z>3 x \bar{x}, z \bar{z}+x \bar{x}-z \bar{x}-\bar{z} x>3 y \bar{y}
$$

三式相加得，

$$
\begin{aligned}
& x \bar{x}+y \bar{y}+z \bar{z}+x \bar{y}+\bar{x} y+y \bar{z}+\bar{y} z+\bar{x} z+x \bar{z}<0 \\
\Leftrightarrow & (x+y+z)(\bar{x}+\bar{y}+\bar{z})<0 .
\end{aligned}
$$

即 $|x+y+z|^{2}<0$, 矛盾.

综上知, $F_{\max }=\sqrt{3}$.

评注 此题是中等偏易的几何不等式题, 考试中约 $43 \%$ 的同学做对. 此题的关键是从几何的观点出发, 先猜出取等条件, 再利用平均值原理(或者反证法)给出证明: 证 1 利用重心的性质和平均值原理给出了证明; 证 2 通过复数运算给出了一个漂亮的证明.

此题也可以分别设出 $x, y, z$ 的实部和虚部, 进行类似于证 2 的运算可以得到结论; 抑或分别设出 $x, y, z$ 的模长和辐角,利用嵌入不等式来证明.

题 2.2 如图, $M$ 为圆外切四边形 $A B C D$ 边 $B C$ 上一点, $X, Y, Z$ 分别为 $\triangle M A B, \triangle M C D, \triangle M A D$ 内心, $X Z$ 交 $A M$ 于 $Q, Y Z$ 交 $D M$ 于 $P, H$ 为 $\triangle X Y Z$ 垂心. 证明: $P, H, Q$ 共线.


证明 (湖南省雅礼中学白鹏飞) 如图所示, 过 $X, Y, Z$ 分别做 $B M, M C, A M$的垂线, 垂足分别为 $T, S, R$. 由内切圆性质, 得

$M R=\frac{M A+M D-A D}{2}, M T=\frac{M A+M B-A B}{2}, M S=\frac{M D+M C-C D}{2}$.

因为四边形 $A B C D$ 为圆外切四边形, 所以 $A B+C D=A D+B C$, 故

$$
M T+M S=\frac{M A+M D+B C-A B-C D}{2}=\frac{M A+M D-A D}{2}=M R .
$$

由 $Z M, X M, Y M$ 分别为 $\angle A M B, \angle A M D, \angle D M C$ 的角平分线知,

$$
M X \cdot \sin \angle Y M Z=M X \cdot \sin \left(90^{\circ}-\angle X M T\right)=M X \cdot \sin \angle M X T=M T
$$

同理, $M Y \cdot \sin \angle X M Z=M S, M Z \cdot \sin \angle X M Y=M R$. 又 $M R=M+M S$, 故

$$
M Z \cdot \sin \angle X M Y=M X \cdot \sin \angle Y M Z+M Y \cdot \sin \angle X M Z
$$

由三弦定理, $M, X, Z, Y$ 四点共圆. 设该圆为 $\omega$, 且分别交 $M A, M D$ 于 $U, V$, 则 $\angle V X Z=\angle Z M V$, 又

$$
\angle H X Z=90^{\circ}-\angle X Z Y=90^{\circ}-(\angle X M B+\angle Y M C)=\angle Z M V
$$

故 $X, H, V$ 三点共线. 同理, $R, H, Y$ 三点共线, 所以 $H$ 为 $X V, Y U$ 的交点. 对圆内接六边形 $X Z Y U M V$ 应用帕斯卡定理得 $P, H, Q$ 三点共线.

评注此题是中等偏难的几何题, 考试中约 $18 \%$ 的同学做对. $M, X, Z, Y$ 四点共圆其实是 2018 保加利亚数学奥林匹克第四题, 用三弦定理证来证明是比较简洁的做法, 然后注意到 $P, H, Q$ 是一个圆内接六边形三组对边的交点, 使用 Pascal 定理即可证得结论.

题 2.3 设图 $G$ 的顶点集为 $V$, 边集为 $E,|V|=n \geq 5$. 现在用两种颜色染 $G$的边 (每条边染且仅染一种颜色), 使得不存在同色的长为 $3,4,5$ 的圈. 证明:

$$
|E| \leq\left\lfloor\frac{n^{2}}{3}\right\rfloor
$$

证明 只需证: 若 $G$ 为 $n(n \geq 5)$ 阶简单图, 且无长为 $3,4,5$ 的圈, 则 $G$ 的边数 $\leq \frac{n^{2}}{6}$.

当 $n=5$ 时, 由 $G$ 中无长为 $3,4,5$ 的圈知, $G$ 中无圈, 故

$$
G \text { 的边数 } \leq n-1=4 \leq \frac{n^{2}}{6} \text {. }
$$

当 $n=6$ 时, 假设 $G$ 的边数 $>\frac{n^{2}}{6}$, 即 $G$ 中至少 7 条边, 则 $G$ 中有圈, 结合 $G$中无长为 $3,4,5$ 的圈知, 此圈长为 6 . 此时, 第 7 条边与此圈比可产生一个长为

2、 4 或 5 的圈, 矛盾.

假设结论对 $n-1(n \geq 7)$ 成立, 下考虑 $n$ 的情形.

设 $G$ 的边数为 $e$. 对 $G$ 中任一点, 由归纳假设, $G$ 删去 $v$ 及 $v$ 相连的边后, $G$的边数 $\leq \frac{(n-1)^{2}}{6}$. 所以 $v$ 的度 $d(v) \geq e-\frac{(n-1)^{2}}{6}$.

于是, $2 e=\sum_{v \in G} d(v) \geq n\left(e-\frac{(n-1)^{2}}{6}\right)$, 得

$$
e \leq \frac{n(n-1)^{2}}{6(n-2)}=\frac{n^{2}+\frac{n}{n-2}}{6}<\frac{n^{2}+2}{6}
$$

又 $\frac{n^{2}+1}{6} \notin \mathbb{Z}$, 故 $e \leq \frac{n^{2}}{6}$. $(*)$ 得证.

评注 此题是中等偏难的组合题, 考试中约 $18 \%$ 的同学做对. 此题的关键是步骤是转化为证明无 $3,4,5$ 圈的图的边数 $\leq \frac{n^{2}}{6}$. 然后再利用归纳法证明结论. 在图论题的归纳过渡中, 删去顶点或边是常规的想法, 本题中是删去顶点, 利用归纳假设进行论证。

题 2.4 设 $p$ 是素数, 序列 $\left\{u_{n}\right\}$ 定义为: 当 $0 \leq n \leq p-1$ 时, $u_{n}=n$; 当 $n \geq p$ 时, $u_{n}=p u_{n+1-p}+u_{n-p}$. 证明:

$$
v_{p}\left(u_{n}\right)=v_{p}(n)
$$

其中 $v_{p}(m)$ 表示使得 $p^{k} \mid m$ 的最大整数 $k$.

证法一 先证明:

$$
v_{p}(n !) \leq n-1 \text {, 且当 } p>2 \text { 和 } n>1 \text { 时, } v_{p}(n !)<n-1 \text {. }
$$

事实上, 设 $n=\sum_{l=0}^{m} a_{l} p^{l}$, 其中 $0 \leq a_{l}<p$, 则

$$
\begin{aligned}
v_{p}(n !) & =\sum_{k=1}^{\infty}\left[\frac{n}{p^{k}}\right]=\sum_{k=1}^{\infty} \sum_{l=k}^{m} a_{l} p^{l-k}=\sum_{l=1}^{m} \sum_{k=1}^{l} a_{l} p^{k} \\
& =\sum_{l=1}^{m} \frac{a_{l} p^{l}-a_{l}}{p-1}=\frac{n-S_{p}(n)}{p-1} \leq n-1,
\end{aligned}
$$

其中 $S_{p}(n)$ 表示 $n$ 在 $p$ 进制下的数码和. 当 $p>2, n>1$ 时, 上述不等式无法取等.

再证:

$$
u_{j+i p}=\sum_{k=0}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{j+k}, \forall i, j \geq 0
$$

对 $i$ 用归纳法. $i=0$ 时, 显然成立. 假设结论小于 $i-1(i \geq 1)$ 时成立, 则

$$
u_{j+i p}=u_{j+(i-1) p}+p u_{j+1+(i-1) p}
$$

$$
\begin{aligned}
& =\sum_{k=0}^{i-1}\left(\begin{array}{c}
i-1 \\
k
\end{array}\right) p^{k} u_{j+k}+\sum_{k=0}^{i-1}\left(\begin{array}{c}
i-1 \\
k
\end{array}\right) p^{1+k} u_{j+1+k} \\
& =\sum_{k=0}^{i-1}\left(\begin{array}{c}
i-1 \\
k
\end{array}\right) p^{k} u_{j+k}+\sum_{k=1}^{i}\left(\begin{array}{c}
i-1 \\
k-1
\end{array}\right) p^{k} u_{j+k}=\sum_{k=0}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{j+k},
\end{aligned}
$$

$i$ 时, 结论仍成立.

下证 $v_{p}\left(u_{n}\right)=v_{p}(n), \forall n \geq 1$.

(1) 当 $1 \leq j<p$ 时, 有 $v_{p}\left(u_{j}\right)=v_{p}(j)=0$. 对 $i \geq 1$, 由

$$
u_{j+i p}=u_{j}+\sum_{k=1}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{j+k}
$$

知, $v_{p}\left(u_{j+i p}\right)=v_{p}\left(u_{j}\right)=0=v_{p}(j+i p)$.

(2) 当 $j=0$ 时, 由 $u_{0}=0, u_{1}=1$ 知

$$
u_{0+i p}=\sum_{k=0}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{k}=i p+\sum_{k=2}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{k}
$$

若 $p>2$, 则对 $k>1$, 由 $(*)$ 知,

$$
v_{p}\left(\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{k}\right) \geq v_{p}(i)-v_{p}(k !)+k>v_{p}(i)-k+1+k=v_{p}(i p),
$$

结合上述两上式知,

$$
v_{p}\left(u_{i p}\right)=v_{p}\left(i p+\sum_{k=2}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) p^{k} u_{k}\right)=v_{p}(i p) .
$$

若 $p=2$. 对 $k=2$, 我们有

$$
v_{2}\left(\left(\begin{array}{l}
i \\
2
\end{array}\right) 2^{2} u_{2}\right) \geq v_{2}(i)-1+2+1=v_{2}(2 i)+1
$$

对 $k>2$, 我们有

$$
\begin{aligned}
v_{2}\left(\left(\begin{array}{l}
i \\
k
\end{array}\right) 2^{k} u_{k}\right) & \geq v_{2}(i)+v_{2}((i-1)(i-2))-v_{2}(k !)+k \\
& \geq v_{2}(i)+1-k+1+k=v_{2}(2 i)+1
\end{aligned}
$$

于是, 结合 $(* *)$ 知,

$$
v_{2}\left(u_{2 i}\right)=v_{2}\left(2 i+\left(\begin{array}{l}
i \\
2
\end{array}\right) 2^{2} u_{2}+\sum_{k=3}^{i}\left(\begin{array}{l}
i \\
k
\end{array}\right) 2^{k} u_{k}\right)=v_{2}(2 i) .
$$

证法二 (浙江省杭州二中黄启昀) 先证明: 若 $p \nmid$, 则 $p \nmid u_{n}$.

事实上, 设 $n=p i+j, 0<j \leq p-1$, 则

$$
u_{n}=p u_{n+1-p}+u_{n-p} \equiv u_{n-p} \equiv \cdots \equiv u_{j}=j \not \equiv 0 \quad(\bmod p)
$$

下证: $v_{p}\left(u_{t p^{\alpha}}\right)=v_{p}\left(t p^{\alpha}\right)=\alpha$, 其中 $(t, p)=1$.

引理 1 对任意非负整数 $n$, 均有 $p^{\alpha} \mid u_{n+p^{\alpha}}-u_{n}, \forall \alpha \in \mathbb{N}^{*}$,
引理 1 的证明 对 $\alpha$ 用归纳法.

$\alpha=1$ 时, 由题设条件知成立.

设 $(*)$ 对 $\leq \alpha-1(\alpha \geq 2)$ 时成立, 下证 $\alpha$ 时的情形. 由归纳假设 $u_{n+p^{i}} \equiv u_{i}$ $\left(\bmod p^{i}\right), \forall 1 \leq i \leq \alpha-1$ 知,

$$
\begin{aligned}
u_{n+p^{\alpha}}-u_{n} & =p\left(u_{n+1}+u_{n+1+p}+\cdots+u_{n+p^{\alpha}-p+1}\right) \\
& \equiv p\left(p\left(u_{n+1}+u_{n+p+1}+\cdots+u_{n+p^{\alpha-1}-p+1}\right)\right) \\
& \equiv p\left(u_{n+p^{\alpha-1}}-u_{n}\right) \equiv 0 \quad\left(\bmod p^{\alpha}\right)
\end{aligned}
$$

引理 2 对非负整数 $n, \alpha$, 有

$$
u_{n+p^{\alpha}}-u_{n} \equiv u_{n+p+p^{\alpha}}-u_{n+p} \quad\left(\bmod p^{\alpha+1}\right) .
$$

引理 2 的证明 $\alpha=0$ 时显然成立. 当 $\alpha \geq 1$ 时, 注意到

$$
u_{i+p^{\alpha}}-u_{i}=p\left(u_{i+1}+u_{i+p+1}+\cdots u_{i+p^{\alpha}-p+1}\right), \forall i \in \mathbb{N} .
$$

在上式中, 分别取 $i=n+p$ 和 $i=n$ 并相减可知,引理 2 结论等价于

$$
p u_{n+1} \equiv p u_{n+p^{\alpha}+1} \quad\left(\bmod p^{\alpha+1}\right) \Leftrightarrow u_{n+1} \equiv u_{n+p^{\alpha}+1} \quad\left(\bmod p^{\alpha}\right)
$$

由引理 1 便知上式成立, 从而引理 2 成立.

回到 $(*)$ 的证明.

(1) 当 $p \geq 3$ 时, 对任意正整数 $m, t, \alpha$, 由引理 1 可知

$$
p^{\alpha-1} \mid u_{m+t p^{\alpha-1}}-u_{m+(t-1) p^{\alpha-1}},
$$

结合引理 2 可知, 存在常数 $c_{m} \in \mathbb{N}$, 对任意正整数 $t$, 有

$$
u_{m+t p^{\alpha-1}}-u_{m+(t-1) p^{\alpha-1}} \equiv c_{m} p^{\alpha-1} \quad\left(\bmod p^{\alpha}\right) .
$$

进而, $u_{m+t p^{\alpha-1}} \equiv u_{m}+t c_{m} p^{\alpha-1}\left(\bmod p^{\alpha}\right)$. 于是,

$$
\sum_{t=0}^{p-1} u_{m+t p^{\alpha-1}} \equiv p u_{m}+c_{m}\left(\sum_{t=0}^{p-1} t\right) p^{\alpha-1} \equiv p u_{m} \quad\left(\bmod p^{\alpha}\right)
$$

从而, 对 $\alpha \geq 2$, 有

$$
\begin{aligned}
u_{p^{\alpha}}-u_{0} & =p\left(\left(\sum_{i=1}^{p^{\alpha-2}} u_{(i-1) p+1}\right) p+\sum_{i=1}^{p^{\alpha-2}} \sum_{t=0}^{p-1}\left(u_{(i-1) p+1+t p^{\alpha-1}}-u_{(i-1) p+1}\right)\right) \\
& \equiv p\left(u_{p^{\alpha-1}}-u_{0}\right) \quad\left(\bmod p^{\alpha+1}\right) .
\end{aligned}
$$

结合 $u_{p}=p$ 可知, $v_{p}\left(u_{p^{\alpha}}\right)=\alpha, \forall \alpha \geq 2$.

进一步, 由引理 2, 对与 $p$ 互素的整数 $t$ 有

$$
u_{t p^{\alpha}} \equiv u_{p^{\alpha}}+u_{(t-1) p^{\alpha}}-u_{0} \equiv \cdots \equiv t u_{p^{\alpha}}-t u_{0} \not \equiv 0 \quad\left(\bmod p^{\alpha+1}\right)
$$

又由引理 1,

$$
u_{t p^{\alpha}} \equiv t\left(u_{p^{\alpha}}-u_{0}\right) \equiv 0 \quad\left(\bmod p^{\alpha}\right)
$$

故 $v_{p}\left(u_{t p^{\alpha}}\right)=\alpha$. 这说明当 $p \geq 3$ 时, 结论成立.

(2) 当 $p=2$ 时, 易知

$$
4 \mid u_{n+2}-u_{n}(n \text { 为奇数 }) \text { 且 } u_{4}-u_{0} \equiv 2\left(u_{2}-u_{0}\right) \quad(\bmod 8) .
$$

对 $\alpha \geq 3$, 由引理 1,2 , 对奇数 $n$, 可设

$$
u_{n+p^{\alpha-1}}-u_{n} \equiv c p^{\alpha-1} \quad\left(\bmod p^{\alpha}\right)
$$

其中 $c \in \mathbb{N}$ 为常数. 从而

$$
\begin{aligned}
u_{p^{\alpha}}-u_{0} & =p\left(\left(\sum_{i=1}^{p^{\alpha-2}} u_{(i-1) p+1}\right) p+\sum_{i=1}^{p^{\alpha-2}} \sum_{t=0}^{1}\left(u_{(i-1) p+1+t p^{\alpha-1}}-u_{(i-1) p+1}\right)\right) \\
& \equiv p\left(\left(u_{p^{\alpha-1}}-u_{0}\right)+p^{\alpha-2} c p^{\alpha-1}\right) \\
& \equiv p\left(u_{p^{\alpha-1}}-u_{0}\right) \quad\left(\bmod p^{\alpha+1}\right) .
\end{aligned}
$$

与 $p \geq 3$ 类似可证 $(*)$.

评注 此题是较难的数论题, 考试中约 $5 \%$ 的同学做对. 此题中的 $a_{n}$ 很难求出具体的通项公式. 可行的想法是通过递归的想法. 证 1 将 $u_{n}$ 由前面的若干项表示出来, 并且系数含素数 $p$ 的幂次容易计算. 上述的解法, 将 $u_{j+i p}$ 用 $u_{j+k}(0 \leq k \leq i)$ 表出, 再利用该递推公式进行幂次的计算可得结论.

证 2 先考虑下标不被 $p$ 整除的简单情形. 对于下标被 $p$ 整除的情形, 关键是证明 $u_{p^{\alpha}}-u_{0} \equiv p\left(u_{p^{\alpha-1}}-u_{0}\right)\left(\bmod p^{\alpha+1}\right)$, 由 $u_{0}=0, u_{p}=p$ 可得 $v_{p}\left(u_{p^{\alpha}}\right)=\alpha$ ，再考虑一般的 $u_{t p^{\alpha}}(t, p$ 互素) 即可.

