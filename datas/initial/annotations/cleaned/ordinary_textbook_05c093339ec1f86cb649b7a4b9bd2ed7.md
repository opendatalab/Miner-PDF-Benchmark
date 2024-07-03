# 好题与妙解（八） 

## —-2019 年新星春季精品营两次测试题解析

冷岗松 罗振华 吴尉迟

2019 年 4 月, 上海数学新星秋季精品营举行了两次测试 (小考). 每次测试四道题, 时间为两个半小时. 这两次测验试题有趣、难度适中, 下面就介绍这些试题及给出相应的解答. 我们将用题 $1 . x$ 表示第 1 次测试的第 $x$ 题, 题 $2 . y$ 的意义类似.

## I. 试 题

题 1.1 已知 $\triangle A B C$ 是锐角三角形, $P$ 为 $C B$ 延长线上一点且满足 $A B=$ $B P, Q$ 为 $B C$ 延长线上一点且满足 $A C=C Q . \triangle A B C$ 的顶点 $A$ 所对应的旁切圆 $\odot J$ 切 $A B, A C$ 延长线于 $D, E$. 直线 $D P$ 与 $E Q$ 交于点 $F$, 证明: $A F \perp F J$.

题 1.2 一个学校有 300 个学生, 其中不存在三个学生, 他们两两是朋友. 已知每位学生至多有 $n$ 个朋友, 且对每个正整数 $m(1 \leq m \leq n)$, 存在一个学生, 其恰有 $m$ 个朋友. 求 $n$ 的最大值.

题 1.3 已知正实数 $a$ 是方程

$$
z^{n}+\left(\operatorname{Re} a_{n-1}\right) z^{n-1}-\left|a_{n-2}\right| z^{n-2}-\cdots-\left|a_{1}\right| z-\left|a_{0}\right|=0
$$

的根, 其中 $a_{0}, a_{1}, \cdots, a_{n-1}$ 为复数. 证明: 多项式

$$
f(z)=z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}
$$

的根 $z$ 满足 $\operatorname{Re} z \leq a$.

题 1.4 设 $b>1$ 是整数. 对每个正整数 $n$, 令 $u_{b}(n)$ 为 $n$ 在 $b$ 进制表示下的非零数字的个数. 证明: 对于任意给定的正整数 $n$ 和 $k$, 存在正整数 $m$ 使得 $u_{b}(m n)=u_{b}(n)+k$.[^0]题 2.1 设 $n \geq 2$ 是给定的整数, 求最小的常数 $\lambda=\lambda(n)$ 使得不等式

$$
\frac{a_{1}-b_{1}}{a_{1}+b_{1}}+\frac{a_{2}-b_{2}}{a_{2}+b_{2}}+\cdots+\frac{a_{n}-b_{n}}{a_{n}+b_{n}} \leq \lambda
$$

对所有满足 $a_{1}+a_{2}+\cdots+a_{n}=b_{1}+b_{2}+\cdots+b_{n}$ 的正实数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}$, $b_{2}, \cdots, b_{n}$ 均成立.

题 $2.2 n$ 个选手参加一比赛, 每两个人至多进行一场比赛, 且没有平局. 已知对于任一由不超过 $m$ 个选手构成的集合 $X$, 存在一名不属于 $X$ 的选手, 其击败过 $X$ 中所有选手. 证明: $m+1 \leq\left\lfloor\log _{2}(n+1)\right\rfloor$.

题 2.3 在非等腰 $\triangle A B C$ 中, 点 $M$ 是边 $B C$ 中点, 以 $A M$ 为直径的圆交 $\triangle A B C$ 的外接圆 $\odot O$ 与另一点 $A^{\prime}$. 点 $A^{\prime}$ 在 $A B, A C$ 上的射影分别为 $D, E$. 证明: 过点 $M$ 且与 $A O$ 平行的直线平分线段 $D E$.

题 2.4 证明: 存在无穷多个正整数 $n$, 使得 $n$ 不能写成 $2^{a}+3^{b}-5^{c}$ 的形式,其中 $a, b, c$ 是非负整数.

## II. 解 答

题 1.1 已知 $\triangle A B C$ 是锐角三角形, $P$ 为 $C B$ 延长线上一点且满足 $A B=$ $B P, Q$ 为 $B C$ 延长线上一点且满足 $A C=C Q . \triangle A B C$ 的顶点 $A$ 所对应的旁切圆 $\odot J$ 切 $A B, A C$ 延长线于 $D, E$. 直线 $D P$ 与 $E Q$ 交于点 $F$, 证明: $A F \perp F J$.



证明 设 $\odot J$ 切 $B C$ 于点 $G$, 连结 $A G, J D, J E$.

由 $A D, A E$ 是 $\odot J$ 的切线知 $A, D, J, E$ 四点共圆, 且该圆以 $A J$ 直径. 注意到 $B D=B G$, 又 $B P=B A$, 所以 $\triangle B D P \cong B A G$, 于是 $\angle P D B=\angle A G B$. 同
理, $\angle Q E C=\angle A G C$. 从而

$$
\angle A D P+\angle A E Q=\angle A G B+\angle A G C=180^{\circ},
$$

故

$$
\angle A D F+\angle A E F=360^{\circ}-(\angle A D P+\angle A E Q)=180^{\circ},
$$

所以 $A, D, F, E$ 四点共圆. 从而 $A, D, J, F, E$ 五点共圆, 且 $A J$ 为这个圆的直径,故 $A F \perp F J$.

评注 这是一道简单的几何题, 得分率约 $94 \%$. 解题的关键是利用全等三角形和导角, 得到 $A, D, F, E$ 四点共圆, 从而证得结论.

题 1.2 一个学校有 300 个学生, 其中不存在三个学生, 他们两两是朋友. 已知每位学生至多有 $n$ 个朋友, 且对每个正整数 $m(1 \leq m \leq n)$, 存在一个学生, 其恰有 $m$ 个朋友. 求 $n$ 的最大值.

解 $n$ 的最大值为 200 .

将问题转化为图论问题, 用 $A_{i}(1 \leq i \leq 300)$ 表示第 $i$ 个学生, 若 $A_{i}, A_{j}$ 是朋友, 则 $A_{i} A_{j}$ 连边, 记所得的图为 $G$, 题目条件变为:

(1) $G$ 中不存在三角形;

(2) 每个点的度小于等于 $n$;

(3) 存在度为 $m(1 \leq m \leq n)$ 的点.

我们构造 300 个点的二部图. 第一组为 $A_{1}, \cdots, A_{100}$, 第二组为 $A_{101}, A_{102}, \cdots$, $A_{300}$, 其中, $A_{i}(i=1, \cdots, 100)$ 与 $A_{100+i}, \cdots, A_{300}$ 连边, 则

$$
d\left(A_{i}\right)=201-i, 1 \leq i \leq 100, d\left(A_{100+j}\right)=j, 1 \leq j \leq 200 \text {, }
$$

满足条件.

下证 $n \leq 200$.

取度为 $n$ 的点, 不妨设为 $A_{n+1}$, 且该点与 $A_{1}, A_{2}, \cdots, A_{n}$ 有边. 故由该图无三角形知, $A_{1}, A_{2}, \cdots, A_{n}$ 中任两点无边, 故其中任意点的度至多为 $300-n$. 从而度为 $301-n$ 到 $n-1$ 的点均在 $A_{n+2}, \cdots, A_{300}$ 中, 于是有

$$
n-1-(301-n)+1 \leq 300-(n+2)+1,
$$

即有 $n \leq 200$.

评注 此题是中等难度的组合题, 得分率约 $63 \%$. 此题的关键是考查朋友最
多的学生, 利用题设条件对该学生的朋友和剩余的学生进行分析, 从而得到 $n$ 的范围. 构造是相对容易的.

题 1.3 已知正实数 $a$ 是方程

$$
z^{n}+\left(\operatorname{Re} a_{n-1}\right) z^{n-1}-\left|a_{n-2}\right| z^{n-2}-\cdots-\left|a_{1}\right| z-\left|a_{0}\right|=0
$$

的根, 其中 $a_{0}, a_{1}, \cdots, a_{n-1}$ 为复数. 证明: 多项式

$$
f(z)=z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}
$$

的根 $z$ 满足 $\operatorname{Re} z \leq a$.

证明 用反证法.

设 $f(z)$ 的根 $z$ 满足 $\operatorname{Re} z>a$, 则 $a^{-1}>(\operatorname{Re} z)^{-1}>|z|^{-1}$, 且

$$
\left|z+a_{n-1}\right| \geq \operatorname{Re}\left(z+a_{n-1}\right)>a+\operatorname{Re} a_{n-1} .
$$

由题设条件知

$$
a+\operatorname{Re} a_{n-1}=\left|a_{n-2}\right| a^{-1}+\left|a_{n-3}\right| a^{-2}+\cdots+\left|a_{0}\right| a^{-(n-1)} .
$$

结合上面两式与 $a^{-1}>|z|^{-1}$ 知,

$$
\begin{aligned}
\left|z+a_{n-1}\right| & \geq\left|a_{n-2}\right| a^{-1}+\left|a_{n-3}\right| a^{-2}+\cdots+\left|a_{0}\right| a^{-(n-1)} \\
& >\left|a_{n-2}\right||z|^{-1}+\left|a_{n-3}\right||z|^{-2}+\cdots+\left|a_{0}\right||z|^{-(n-1)}
\end{aligned}
$$

两边同乘以 $|z|^{n-1}$ 可得,

$$
\left|z^{n}+a_{n-1} z^{n-1}\right|-\left|a_{n-2}\right||z|^{n-2}-\cdots-\left|a_{0}\right|>0,
$$

再结合三角不等式可知，

$$
\begin{aligned}
|f(z)| & =\left|z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0}\right| \\
& \geq\left|z^{n}+a_{n-1} z^{n-1}\right|-\left|a_{n-2}\right||z|^{n-2}-\cdots-\left|a_{0}\right|>0
\end{aligned}
$$

这与 $z$ 是 $f$ 的根矛盾! 故有 $\operatorname{Re} z \leq a$.

评注 这是一道有一定难度的代数问题, 约 $25 \%$ 的学生做出. 该问题的题面新颖, 但处理问题的手法却是典型的: 即将根代入原方程后除以它的最高次幂或第二高次幂, 从而转化为它的模的倒数的方程来处理, 通常这种方法叫做刘维尔方法。

题 1.4 设 $b>1$ 是整数. 对每个正整数 $n$, 令 $u_{b}(n)$ 为 $n$ 在 $b$ 进制表示下的非零数字的个数. 证明: 对于任意给定的正整数 $n$ 和 $k$, 存在正整数 $m$ 使得 $u_{b}(m n)=u_{b}(n)+k$.
证明 对 $k$ 用归纳法.

先证 $k=1$ 的情形.

令 $n=\sum_{i=0}^{d-1} c_{i} b^{i}$, 其中 $c_{i} \in\{0,1, \ldots, b-1\}, d=\left\lfloor\log _{b}(n)\right\rfloor+1$.

设 $c_{j}$ 是最小的指标使得 $c_{j} \neq 0$. 我们分两种情况:

(i) $c_{j} \geq 2$. 取正整数 $r, s$, 满足 $r>s+d>2 d$ 且 $n \mid b^{r}-b^{s}$. 则

$$
M=b^{r}-b^{s}+b^{s-j} n \equiv 0 \quad(\bmod n),
$$

于是,

$$
M=b^{r}+\sum_{i=j+1}^{d-1} c_{i} b^{i+s-j}+\left(c_{j}-1\right) b^{s}
$$

从而 $u_{b}(M)=u_{b}(n)+1$, 此时令 $m=\frac{M}{n}$ 即可.

(ii) $c_{j}=1$, 取正整数 $r, s$, 满足 $r>s+d>2 d$ 且 $n \mid b^{r}-b^{s}$. 则

$$
M=b^{r}-b^{s}+b^{s-j+1} n \equiv 0 \quad(\bmod n),
$$

于是

$$
M=b^{r}+\sum_{i=j+1}^{d-1} c_{i} b^{s-j+1+i}+(b-1) b^{s}
$$

故 $u_{b}(M)=u_{b}(n)+1$, 令 $m=\frac{M}{n}$ 即可.

这就证明了 $k=1$ 的情形.

假设 $k$ 时成立, 考虑 $k+1$ 时的情形.

由归纳假设, 存在 $m_{k}$, 使得 $u_{b}\left(m_{k} n\right)=u_{b}(n)+k$. 再由 $k=1$ 的情形知, 存在 $m$, 使得

$$
u_{b}\left(m m_{k} n\right)=u_{b}\left(m_{k} n\right)+1=u_{b}(n)+k+1 .
$$

此时, 取 $m_{k+1}=m m_{k}$ 即可.

评注 本题是难度较大的数论题, 只有不到 $8 \%$ 的学生做对此题. 一个基本的观察是只需证明 $k=1$ 的情形, 之后比较自然的想法是对 $n$ 的 $b$ 进制下的非零数码进行调整, 调整的策略如下: 考虑 $n$ 的首个非零数码, 若它大于 1 , 则将这一位减少 1 , 前面若干位加上 1 , 由于 $b$ 与 $n$ 可能不互素, 再在末位补上一些 0 即可满足条件; 若首个非零数码等于 1 , 则把前述方案稍作变化仍可适用.

题 2.1 设 $n$ 是任意给定的正整数, $n \geq 2$, 求最小的常数 $\lambda=\lambda(n)$ 使得不等式

$$
\frac{a_{1}-b_{1}}{a_{1}+b_{1}}+\frac{a_{2}-b_{2}}{a_{2}+b_{2}}+\cdots+\frac{a_{n}-b_{n}}{a_{n}+b_{n}} \leq \lambda
$$

对所有满足

$$
a_{1}+a_{2}+\cdots+a_{n}=b_{1}+b_{2}+\cdots+b_{n}
$$

的正实数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$ 均成立.

解 $\lambda(n)=n-1$.

一方面, 由于 $a_{1}+a_{2}+\cdots+a_{n}=b_{1}+b_{2}+\cdots+b_{n}$, 故存在 $i_{0} \in\{1,2, \cdots, n\}$,使 $b_{i_{0}} \geq a_{i_{0}}$, 所以 $\frac{a_{i_{0}}-b_{i_{0}}}{a_{i_{0}}+b_{i_{0}}} \leq 0$. 对 $i \neq i_{0}$,

$$
\frac{a_{i}-b_{i}}{a_{i}+b_{i}} \leq\left|\frac{a_{i}-b_{i}}{a_{i}+b_{i}}\right|<1
$$

从而

$$
\sum_{i=1}^{n} \frac{a_{i}-b_{i}}{a_{i}+b_{i}}=\sum_{i \neq i_{0}} \frac{a_{i}-b_{i}}{a_{i}+b_{i}}+\frac{a_{i_{0}}-b_{i_{0}}}{a_{i_{0}}+b_{i_{0}}}<n-1+0=n-1 .
$$

另一方面, 令 $a_{2}=\cdots=a_{n}=1, b_{2}=\cdots=b_{n}=\frac{1}{p}$,

$$
a_{1}=p, b_{1}=p+(n-1)\left(1-\frac{1}{p}\right),
$$

其中 $p>n$, 则有 $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} b_{i}$, 且当 $p \rightarrow \infty$ 时,

$$
\frac{a_{1}-b_{1}}{a_{1}+b_{1}} \rightarrow 0, \frac{a_{i}-b_{i}}{a_{i}+b_{i}} \rightarrow 1, i=2,3, \cdots, n
$$

从而 $\sum_{i=1}^{n} \frac{a_{i}-b_{i}}{a_{i}+b_{i}} \rightarrow n-1$.

评注 这是一道中等难度的代数题, 得分率为 $42 \%$. 对 $a_{i}>b_{i}$ 的情形, $\frac{a_{i}-b_{i}}{a_{i}+b_{i}}$ 的最佳上界为 1 ; 对 $a_{i} \leq b_{i}$ 的情形, $\frac{a_{i}-b_{i}}{a_{i}+b_{i}}$ 的最佳上界为 0 . 由于 $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} b_{i}$, 满足 $a_{i}>b_{i}$ 的 $i$ 至多 $n-1$ 个, 故所求式的最佳上界为 $n-1$. 趋于最佳常数的例子很好构造.

题 $2.2 n$ 个选手参加一比赛, 每两个人至多进行一场比赛, 且没有平局. 已知对于任一由不超过 $m$ 个选手构成的集合 $X$, 存在一名不属于 $X$ 的选手, 其击败过 $X$ 中所有选手. 证明: $m+1 \leq\left\lfloor\log _{2}(n+1)\right\rfloor$.

证明 先转换为图论语言. 将 $n$ 选手看成有向图的顶点, 若选手 $u$ 胜了 $v$, 则连一条从 $u$ 到 $v$ 的边, 记所得的图为 $G$.

所证不等式等价于 $n \geq 2^{m+1}-1$.

对 $m$ 用归纳法.

当 $m=1$ 时, 若 $n=2$, 则由条件, 则其中任一点到另一点有边, 这与条件矛盾. 故 $n \geq 3$.
假设命题对 $m-1$ 成立. 下证 $m$ 时的情形.

令 $d^{-}(w)$ 表示顶点 $w$ 的入度. 则

$$
\sum_{w \in V(G)} d^{-}(w) \leq\left(\begin{array}{l}
n \\
2
\end{array}\right)=\frac{n(n-1)}{2}
$$

其中 $V(G)$ 表示 $G$ 的顶点集. 由抽庹原理, 存在顶点 $v$ 使 $d^{-}(v) \leq \frac{n-1}{2}$.

令 $V^{\prime}$ 表示所有到 $v$ 有边的顶点构成的集合, 易知 $\left|V^{\prime}\right| \geq m$. 对 $V^{\prime}$ 的任一个不超过 $m-1$ 元子集 $X$, 由条件, $G$ 中存在一顶点 $u$, 使 $u$ 到 $X \cup\{v\}$ 中任一点有边. 因此, $u \in V^{\prime}$.

这说明, 对于 $V^{\prime}$ 中任一不超过 $m-1$ 元子集 $Y$, 均存在 $V^{\prime}$ 一点, 该点到 $Y$中任一点有边. 故有归纳假设知 $\left|V^{\prime}\right| \geq 2^{(m-1)+1}-1$. 从而

$$
\frac{n-1}{2} \geq d^{-}(v)=\left|V^{\prime}\right| \geq 2^{m}-1
$$

即有 $n \geq 2^{m+1}-1$. 得证.

评注 这是一道有一定难度的图论题, 得分率为 18\%. 解题的思路是在归纳法中取出入度最少的点, 考虑到这点有边的顶点构成的集合, 利用归纳假设可以证得结论.

题 2.3 在非等腰 $\triangle A B C$ 中, 点 $M$ 是边 $B C$ 中点, 以 $A M$ 为直径的圆交 $\triangle A B C$ 的外接圆 $\odot O$ 与另一点 $A^{\prime}$. 点 $A^{\prime}$ 在 $A B, A C$ 上的射影分别为 $D, E$. 证明: 过点 $M$ 且与 $A O$ 平行的直线平分线段 $D E$.

证法一 (吉大附中艾一夫) 设 $A$ 的对径点为 $K$. 由于 $\angle A A^{\prime} M=90^{\circ}$, 故 $K, M, A^{\prime}$ 共线.


注意到

$$
\begin{gathered}
\angle E D A^{\prime}=\angle E A A^{\prime}=\angle C A A^{\prime}=\angle C B A^{\prime}, \\
\angle D A^{\prime} E=\angle D A C=\angle B A C=\angle B A^{\prime} C,
\end{gathered}
$$

于是 $\triangle A^{\prime} D E \sim \triangle A^{\prime} B C$.

设 $N$ 是 $D E$ 的中点, 那么, $\triangle A^{\prime} D N \sim \triangle A^{\prime} B M$, 从而 $\triangle A^{\prime} D B \sim A^{\prime} N M$.

设直线 $N M$ 与 $A B$ 的交点为 $L$, 则

$$
\angle B L M=\angle D A^{\prime} N=\angle B A^{\prime} M=\angle B A^{\prime} K=\angle B A O
$$

于是 $M N \perp A O$.

证法二 (卢圣) 延长 $A O$ 与圆 $O$ 交于 $T$, 设 $H$ 为 $\triangle A B C$ 的垂心, $L, N, J$ 为 $D E, A H, A A^{\prime}$ 的中点, 直线 $D E, M A^{\prime}$ 交于 $S$.



易知 $T B \perp B A, T C \perp C A$. 则 $T B / / C H, C T / / B H$. 从而四边形 $B T C H$ 为平行四边形. 这推出 $T, M, H$ 共线. 易知 $T A^{\prime} \perp A^{\prime} A, M A^{\prime} \perp A^{\prime} A$. 所以 $T, M, A^{\prime}$共线. 故 $T, M, H, A^{\prime}$ 四点共线.

由中位线的性质知 $O, N, J$ 共线且该线平行于 $T A^{\prime}$. 由 Steiner 定理 (Steiner 定理是指三角形的外接圆上一点关于三角形的 Simson 线平分该点与三角形垂心构成的线段)知 $S$ 为 $A^{\prime} H$ 中点. 从而 $N S / / A A^{\prime}, J S \| A H$. 故 $S N \perp N J$.

易知 $A, D, E, A^{\prime}$ 四点共圆且圆心为 $J$, 则 $J L \perp L S$. 所以 $J, N, L, S$ 四点共圆。由

$$
\begin{aligned}
\angle D K A & =\angle H A C+\angle D E A=\angle H A C+\angle D A^{\prime} A \\
& =90^{\circ}-\angle A C B+90^{\circ}-\angle B A A^{\prime}
\end{aligned}
$$

$$
\begin{aligned}
& =180^{\circ}-\angle A A^{\prime} B-\angle B A A^{\prime} \\
& =\angle A B A^{\prime}=\angle A T A^{\prime}=\angle A O N
\end{aligned}
$$

可知 $\angle O N L=\angle J S D=\angle A K D=\angle A O N$. 故 $N L / / A O$.

由外心, 垂心性质知 $O M=\frac{1}{2} A H=A N$, 且 $O M / / A H$. 所以 $O M$ 平行且相等于 $A N$. 所以四边形 $A O M N$ 为平行四边形. 所以 $M N / / A O$. 所以 $M, L, N$三点共线且该线平行于 $A O$. 所以过 $M$ 且平行于 $A O$ 的直线平分 $D E$.

评注 这是一道中等难度的几何题, 得分率为 $51 \%$. 本题的解法较多, 也蕴含了许多结论. 解法 1 涉及两圆相交所产生的一组相似, 以及相似对应点的使用.解法 2 综合利用了 Simson 线,垂心, 外心和中点的性质。

题 2.4 证明: 存在无穷多个正整数 $n$, 使得 $n$ 不能写成 $2^{a}+3^{b}-5^{c}$ 的形式,这里 $a, b, c$ 是非负整数.

证法一 我们证明形如 $6 k+1(k \geq 1)$ 的整数不能表示成 $2^{a}+3^{b}-5^{c}$ 的形式.

若不然, 设 $6 k+1=2^{a}+3^{b}-5^{c}$.

若 $a \geq 1$, 则 $1 \equiv 3^{b}-5^{c}(\bmod 2)$, 这与 $3^{b}, 5^{c}$ 均为奇数矛盾.

于是 $a=0$. 若 $b=0$, 则只有 $c=0$ 时, $2^{a}+3^{b}-5^{c}$ 才是正整数. 但此时 $2^{a}+3^{b}-5^{c}=1<7$, 矛盾.

若 $b \geq 1$. 则 $0 \equiv 0-5^{c}(\bmod 3)$, 不成立.

故形如 $6 k+1(k \geq 1)$ 的整数不能表示成 $2^{a}+3^{b}-5^{c}$ 的形式.

证法二 我们证明当 $n \equiv 7(\bmod 12)$ 时, $n$ 不能写成 $2^{a}+3^{b}-5^{c}$ 的形式.

注意到

$2^{a} \equiv 1,2,4,8 \quad(\bmod 12), \quad 3^{b}=1,3,9 \quad(\bmod 12), \quad 5^{c}=1,5 \quad(\bmod 12)$,

若存在非负整数 $a, b, c$, 使 $2^{a}+3^{b}-5^{c} \equiv 7(\bmod 12)$, 我们分两种情况.

1) 若 $5^{c}=1(\bmod 12)$, 则 $2^{a}+3^{b} \equiv 8(\bmod 12)$, 检验知, 不成立.
2) 若 $5^{c}=5(\bmod 12)$, 则 $2^{a}+3^{b} \equiv 0(\bmod 12)$, 检验知, 不成立.

故不存在非负整数 $a, b, c$, 使 $2^{a}+3^{b}-5^{c} \equiv 7(\bmod 12)$. 从而当 $n \equiv 7$ $(\bmod 12)$ 时, $n$ 不能写成 $2^{a}+3^{b}-5^{c}$ 的形式.

评注 这是一道中等难度的数论题, 得分率为 $42 \%$. 这类问题用同余方法是常见的思路, 关键是选取合适的模. 这里模 6 和模 12 都是可行的. 本题的难度我们在选题时没有准确评估。


[^0]:    收稿日期: 2019-05-04.

