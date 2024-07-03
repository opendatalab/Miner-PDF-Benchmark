$$
\text { 数学新星网 } \% \text { 学生专栏 }
$$

www.nsmath.cn/xszl

# 2020 罗马尼亚大师杯试题解答与评析 

韩新森<br>(浙江省乐清市知临中学, 325600 )<br>指导教师: 羊明亮

2020 罗马尼亚数学大师赛 (Romanian Master of Mathematics) 于 2 月 26 日至 3 月 1 日在罗马尼亚布加勒斯特举行. 由于受到新冠肺炎疫情的影响, 包括我国在内的几个国家无法委派代表队前往现场正式参加比赛. 经协商, 竞赛举办方同意中国、韩国、意大利、伊朗各国代表队以远程方式参加考试.

我有幸作为中国代表队的成员参加了远程考试, 成绩为 31 分, 获得金牌.

本文介绍这次考试试题的解答, 并加以评析. 请读者指正!

## I. 试 题

1. 在 $\triangle A B C$ 中, $C$ 为直角, $C D \perp A B$ 于 $D$. 令 $I$ 为 $\triangle A B C$ 内切圆 $\omega$ 的圆心, $\omega$ 与边 $B C, C A, A B$ 分别相切于点 $A_{1}, B_{1}, C_{1}$. 设 $E, F$ 分别是点 $C$ 关于直线 $C_{1} A_{1}, C_{1} B_{1}$ 的对称点, $K, L$ 分别是点 $D$ 关于直线 $C_{1} A_{1}, C_{1} B_{1}$ 的对称点. 证明: $\triangle A_{1} E I, \triangle B_{1} F I, \triangle C_{1} K L$ 的外接圆共点.
2. 设整数 $N \geq 2$, 数列 $a=\left(a_{1}, a_{2}, \cdots, a_{N}\right), b=\left(b_{1}, b_{2}, \cdots, b_{N}\right)$ 中各项均为非负整数. 对每个整数 $i \notin\{1, \cdots, N\}$, 取 $k \in\{1, \cdots, N\}$ 满足 $i-k$ 被 $N$整除, 令 $a_{i}=a_{k}, b_{i}=b_{k}$.

我们称 $a$ 是 $b-$ 调和的, 如果对于每个整数 $i$, 均有 $a_{i}$ 等于以下算术平均:

$$
a_{i}=\frac{1}{2 b_{i}+1} \sum_{s=-b_{i}}^{b_{i}} a_{i+s}
$$

现在假设 $a$ 与 $b$ 均不为常数数列, 且 $a$ 是 $b-$ 调和的, $b$ 是 $a$-调和的. 证明: $a_{1}, \cdots, a_{N}, b_{1}, \cdots, b_{N}$ 中至少有 $N+1$ 项等于零.

3. 设整数 $n \geq 3$. 一个国家有 $n$ 座机场, 且有 $n$ 家执行双向航班的航空公司.
对每家航空公司, 都存在一个奇数 $m \geq 3$ 及 $m$ 座不同的机场 $C_{1}, C_{2}, \cdots, C_{m}$,满足: 这家航空公司所执行的全部航班恰是 $C_{1}$ 与 $C_{2}$ 之间, $C_{2}$ 与 $C_{3}$ 之间, $\cdots$, $C_{m-1}$ 与 $C_{m}$ 之间, $C_{m}$ 与 $C_{1}$ 之间的那些双向航班. 证明: 存在一条由奇数趟航班组成的封闭路线, 其中不同的航班由不同的航空公司执行.
4. 用 $\mathbb{N}^{*}$ 表示所有正整数的集合. 我们称 $\mathbb{N}^{*}$ 的一个子集 $A$ 为 “无和集”,如果对 $A$ 中的任意两个(可能相同的)元素 $x, y$, 它们的和 $x+y$ 不在 $A$ 中.

求所有把无和集映到无和集的满射函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 即对任意无和集 $A$,它的像 $\{f(a) \mid a \in A\}$ 也是无和集.

注: 一个函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$ 称为满射, 如果对于每个整数 $n$, 都存在一个正整数 $m$ 使得 $f(m)=n$.

5. 在 $x y-$ 坐标平面中, 横纵坐标都为整数的点称为格点, 所有顶点均为格点的多边形称为“格点多边形”.

令 $\Gamma$ 为一个凸的格点多边形. 证明: 可将 $\Gamma$ 置于另一个凸的格点多边形 $\Omega$内, 使得所有 $\Gamma$ 的顶点都落在 $\Omega$ 的边界上, 并且 $\Omega$ 恰有一个顶点不是 $\Gamma$ 的顶点.

6. 对每个整数 $n \geq 2$. 记 $F(n)$ 为 $n$ 最大的素因子. 一个 “奇异对” 是一对不同的素数 $p$ 和 $q$, 使得没有整数 $n \geq 2$ 满足 $F(n) F(n+1)=p q$. 证明: 存在无穷多对奇异对.

## II . 解答与评注

1. 在 $\triangle A B C$ 中, $C$ 为直角, $C D \perp A B$ 于 $D$. 令 $I$ 为 $\triangle A B C$ 内切圆 $\omega$ 的圆心, $\omega$ 与边 $B C, C A, A B$ 分别相切于点 $A_{1}, B_{1}, C_{1}$. 设 $E, F$ 分别是点 $C$ 关于直线 $C_{1} A_{1}, C_{1} B_{1}$ 的对称点, $K, L$ 分别是点 $D$ 关于直线 $C_{1} A_{1}, C_{1} B_{1}$ 的对称点. 证明: $\triangle A_{1} E I, \triangle B_{1} F I, \triangle C_{1} K L$ 的外接圆共点.



证明 设 $\triangle A B C$ 的三个内角分别为 $A, B, C$. 在直线 $C_{1} I$ 上取点 $P$ 满足
$\angle P C D=45^{\circ}$. 易知 $C B_{1} I A_{1}$ 为正方形. 下证: $K, I, C$ 共线.

因为

$$
C P=\sqrt{2} C_{1} D=\sqrt{2} C_{1} K, \quad C I=\sqrt{2} B_{1} I=\sqrt{2} C_{1} I,
$$

所以 $\frac{C P}{C_{1} K}=\frac{C I}{C_{1} I}$. 又

$$
\angle I C P=45^{\circ}-\angle I C D=\angle B C D=90^{\circ}-B,
$$

且

$$
\begin{aligned}
\angle I C_{1} K & =\angle A_{1} C_{1} K-\angle A_{1} C_{1} I \\
& =\angle B C_{1} A_{1}-\angle A_{1} C_{1} I \\
& =90^{\circ}-\frac{1}{2} B-\frac{1}{2} B=90^{\circ}-B
\end{aligned}
$$

故 $\angle I C P=\angle I C_{1} K$. 因此, $\triangle I C P \sim \triangle I C_{1} K$. 于是, $\angle C I P=\angle C_{1} I K$, 即 $C, I, K$共线, 且 $\angle C_{1} K I=\angle C P I=135^{\circ}$.

同理, $C, I, L$ 共线, 且 $\angle C_{1} L I=45^{\circ}$. 设 $C_{1}$ 关于 $C I$ 的对称点为 $T$, 则 $C_{1} K T L$ 为正方形. 下证: $\triangle A_{1} E I, \triangle B_{1} F I, \triangle C_{1} K L$ 的外接圆均过点 $T$.

由 $C_{1} K T L$ 为正方形知, $C_{1}, K, T, L$ 共圆. 注意到

$$
\begin{aligned}
\angle F B_{1} I & =\angle F B_{1} C_{1}+\angle I B_{1} C_{1} \\
& =\angle C B_{1} C_{1}+\angle I B_{1} C_{1} \\
& =90^{\circ}+\frac{1}{2} A+\frac{1}{2} A=90^{\circ}+A
\end{aligned}
$$

且

$$
\begin{aligned}
\angle T I B_{1} & =\angle C I T-\angle C I B_{1}=\angle C I C_{1}-45^{\circ} \\
& =360^{\circ}-\frac{1}{2} C-B-90^{\circ}-45^{\circ} \\
& =180^{\circ}-B=90^{\circ}+A,
\end{aligned}
$$

故 $\angle F B_{1} I=\angle T I B_{1}$. 又

$$
T I=C_{1} I=B_{1} I=C B_{1}=F B_{1} .
$$

所以 $F B_{1} I T$ 为等腰梯形. 因此, $F, B_{1}, I, T$ 共圆.

同理, $E, A_{1}, I, T$ 共圆.

证毕.

评注 这是一道不太难的几何题, 但其证明共圆的方式比较特殊, 利用了正方形及等腰梯形, 值得注意.

2. 设整数 $N \geq 2$, 数列 $a=\left(a_{1}, a_{2}, \cdots, a_{N}\right), b=\left(b_{1}, b_{2}, \cdots, b_{N}\right)$ 中各项均为非负整数. 对每个整数 $i \notin\{1, \cdots, N\}$, 取 $k \in\{1, \cdots, N\}$ 满足 $i-k$ 被 $N$整除, 令 $a_{i}=a_{k}, b_{i}=b_{k}$.

我们称 $a$ 是 $b$-调和的, 如果对于每个整数 $i$, 均有 $a_{i}$ 等于以下算术平均:

$$
a_{i}=\frac{1}{2 b_{i}+1} \sum_{s=-b_{i}}^{b_{i}} a_{i+s}
$$

现在假设 $a$ 与 $b$ 均不为常数数列, 且 $a$ 是 $b-$ 调和的, $b$ 是 $a$-调和的. 证明: $a_{1}, \cdots, a_{N}, b_{1}, \cdots, b_{N}$ 中至少有 $N+1$ 项等于零.

证明 我们先证明: $\forall i \in \mathbb{Z}, a_{i}, b_{i}$ 中必有 0 .

否则, 可考虑非空集合 $\left\{a_{i}, b_{i} \mid i \in \mathbb{Z}, a_{i} \neq 0\right.$ 且 $\left.b_{i} \neq 0\right\}$ 的最大值, 记为 $M$.不妨设 $a_{k}=M, b_{k} \neq 0, k \in \mathbb{Z}$.

若存在 $-b_{k} \leq s \leq b_{k}$ 使 $a_{k+s}>a_{k}$, 则由 $M$ 的最大性知 $b_{k+s}=0$. 于是

$$
\sum_{t=-a_{k+s}}^{a_{k+s}} b_{k+s+t}=0
$$

即对 $\forall-a_{k+s} \leq t \leq a_{k+s}$, 有 $b_{k+s+t}=0$. 而

$$
|s| \leq b_{k} \leq M<a_{k+s},
$$

故在上式中取 $t=-s$, 可得 $b_{k}=0$, 这与 $b_{k} \neq 0$ 矛盾.

因此, 对 $\forall-b_{k} \leq s \leq b_{k}$, 有 $a_{k+s} \leq a_{k}$. 结合

$$
a_{k}=\frac{1}{2 b_{k}+1} \sum_{s=-b_{k}}^{b_{k}} a_{k+s}
$$

立得对 $\forall-b_{k} \leq s \leq b_{k}$, 有 $a_{k+s}=a_{k}$.

若存在 $-b_{k} \leq s \leq b_{k}$ 使 $b_{k+s}=0$, 则有

$$
\sum_{t=-a_{k+s}}^{a_{k+s}} b_{k+s+t}=0
$$

得对 $\forall-a_{k+s} \leq t \leq a_{k+s}$, 有 $b_{k+s+t}=0$. 注意到

$$
|s| \leq b_{k} \leq M=a_{k+s},
$$

故在上式中取 $t=-s$, 可得 $b_{k}=0$ 与 $b_{k} \neq 0$ 矛盾.

至此, 我们证明了: $\forall k \in \mathbb{Z}$, 若 $a_{k}=M$ 且 $b_{k} \neq 0$, 则 $a_{k+1}=M$ 且 $b_{k+1} \neq 0$.

由此结合简单的归纳法即知 $\forall k \in \mathbb{Z}, a_{k}=M$ 且 $b_{k} \neq 0$, 这与 $a$ 不为常数数列矛盾. 因此, $\forall i \in \mathbb{Z}, a_{i}, b_{i}$ 中必有 0 .

再证明: 存在 $i \in \mathbb{Z}$, 使 $a_{i}=b_{i}=0$.

因为 $(*)$ 及 $a, b$ 均不为常数数列, 所以存在 $i \in \mathbb{Z}$ 使得 $a_{i}=b_{i+1}=0$. 此时,
假设 $a_{i+1} \neq 0$ 且 $b_{i} \neq 0$, 则

$$
0=a_{i}=\frac{1}{2 b_{i}+1} \sum_{s=-b_{i}}^{b_{i}} a_{i+s} \geq \frac{a_{i+1}}{2 b_{i}+1}>0
$$

矛盾. 故 $a_{i+1}, b_{i}$ 中有 0 . 从而 $(* *)$ 成立.

由 $(*)$ 与 $(* *)$, 立即得到 $a_{1}, \cdots, a_{N}, b_{1}, \cdots, b_{N}$ 中至少 $N+1$ 项为 0 .

评注 这是一道简单题, 只需要采用极端原理再根据大小关系去分析. 顺带一提, 对 $(* *)$ 稍加改进马上可以得到本题最佳的界为 $N+2$.

3. 设整数 $n \geq 3$. 一个国家有 $n$ 座机场, 且有 $n$ 家执行双向航班的航空公司.对每家航空公司, 都存在一个奇数 $m \geq 3$ 及 $m$ 座不同的机场 $C_{1}, C_{2}, \cdots, C_{m}$,满足: 这家航空公司所执行的全部航班恰是 $C_{1}$ 与 $C_{2}$ 之间, $C_{2}$ 与 $C_{3}$ 之间, $\cdots$, $C_{m-1}$ 与 $C_{m}$ 之间, $C_{m}$ 与 $C_{1}$ 之间的那些双向航班. 证明: 存在一条由奇数趟航班组成的封闭路线, 其中不同的航班由不同的航空公司执行.

证明 我们将问题转化为图论语言:

考虑 $n$ 个点间的 $n$ 个奇圈(不必不同), 证明: 可以从其中若干个圈中各取一条边, 使得取出的边也构成一个奇圈.

我们取出若干条来自互不相同的奇圈的边, 构成图 $G$, 满足 $G$ 中无圈(包括无重边). 考虑上述取法中使 $G$ 所含连通分支数最少的取法.

此时 $G$ 中至多 $n-1$ 条边, 因此必有某个奇圈的边不在 $G$ 中出现, 记此圈为 $A$. 则对 $A$ 的每条边的两个顶点, 它们必在 $G$ 的同一个连通分支内. 否则, 将此边添入 $G$ 后, $G$ 中仍无圈, 且连通分支个数减少, 与 $G$ 的定义矛盾.

于是, 圈 $A$ 的所有顶点均在 $G$ 的同一连通分支内, 此连通分支为一棵树, 记为 $T$.

任取 $T$ 中一点 $w$. 对 $T$ 中任意两顶点 $u, v$, 记 $d(u, v)$ 为 $u$ 与 $v$ 在 $T$ 中的距离, 则易知

$$
d(u, v) \equiv d(u, w)+d(v, w) \quad(\bmod 2)
$$

因为 $A$ 为一个圈, 所以

$$
\sum_{e_{u v} \in A} d(u, v) \equiv \sum_{e_{u v} \in A}(d(u, w)+d(v, w)) \equiv 0 \quad(\bmod 2)
$$

其中, $\sum_{e_{u v} \in A}$ 指对 $A$ 中所有边求和, $e_{u v}$ 为 $u, v$ 间的边. 注意到 $A$ 的边数为奇数,故存在 $e_{u v} \in A$ 使 $2 \mid d(u, v)$. 考虑由 $e_{u v}$ 及 $u$ 到 $v$ 在 $T$ 中的路径围成的圈, 其长度为 $d(u, v)+1$ 为奇数. 于是, 找到了一个由不同圈的边构成的奇圈.
评注 此题寻找圈的想法是在生成树上加边, 这是一个十分常用的手法. 值得一提的是, 2019 年大师杯的第 3 题也可以基于此想法做.

4. 用 $\mathbb{N}^{*}$ 表示所有正整数的集合. 我们称 $\mathbb{N}^{*}$ 的一个子集 $A$ 为“无和集”,如果对 $A$ 中的任意两个(可能相同的)元素 $x, y$, 它们的和 $x+y$ 不在 $A$ 中.

求所有把无和集映到无和集的满射函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 即对任意无和集 $A$,它的像 $\{f(a) \mid a \in A\}$ 也是无和集.

注: 一个函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$ 称为满射, 如果对于每个整数 $n$, 都存在一个正整数 $m$ 使得 $f(m)=n$.

解 所求 $f$ 为 $f(x)=x\left(x \in \mathbb{N}^{*}\right)$.

我们先证明: $\forall a \in \mathbb{N}^{*}, f(2 a)=2 f(a)$.

任取 $a \in \mathbb{N}^{*}$. 因为 $f$ 为满射, 所以存在 $b \in \mathbb{N}^{*}$ 使 $f(b)=2 f(a)$. 注意到 $\{f(a), f(b)\}$ 不为无和集. 于是, 必有 $b=\frac{a}{2}$ 或 $b=2 a$ 之一成立. 我们对 $a$ 所含 2 的幂次 $\alpha$ 用数学归纳法, 证明: $f(2 a)=2 f(a)$.

当 $\alpha=0$ 即 $a$ 为奇数时, 满足 $f(b)=2 f(a)$ 的 $b$ 只能为 $2 a$, 即 $f(2 a)=2 f(a)$.假设结论对 $\alpha-1\left(\alpha \in \mathbb{N}^{*}\right.$ 成立). 下面考虑 $\alpha$ 的情形.

对 $\frac{a}{2}$, 其所含 2 的幂次为 $\alpha-1$, 故由归纳假设, 有 $f(a)=2 f\left(\frac{a}{2}\right)$. 又 $f(2 a)=$ $2 f(a)$ 与 $f\left(\frac{a}{2}\right)=2 f(a)$ 中至少一者成立, 因此只能为 $f(2 a)=2 f(a)$.

于是, 我们证明了 $\forall a \in \mathbb{N}^{*}, f(2 a)=2 f(a)$.

再证: $f$ 为单射.

否则, 假设存在 $a, b \in \mathbb{N}^{*}, a<b$ 使 $f(a)=f(b)$, 则 $\{a, 2 b\}$ 为无和集且 $\{f(a), f(2 b)\}$ 不为无和集, 矛盾.

接着证: $\forall n \in \mathbb{N}^{*}, f(n)=n f(1)$.

因为 $f$ 为双射, 故可设 $c \in \mathbb{N}^{*}$ 使 $f(c)=n f(1)$. 任取 $s \in \mathbb{N}^{*}, s>\max _{1 \leq t \leq 2 c} f(t)$,对 $\forall a \in \mathbb{N}^{*}$, 若 $f(a) \geq s$, 则 $a>2 c$.

对 $\forall 0 \leq i \leq n$, 设 $u_{i} \in \mathbb{N}^{*}$ 使 $f\left(u_{i}\right)=s+i \cdot f(1)$. 于是, 对 $\forall 0 \leq i \leq n-1$,因为 $\left\{f(1), f\left(u_{i}\right), f\left(u_{i+1}\right)\right\}$ 不为无和集, 所以 $\left\{1, u_{i}, u_{i+1}\right\}$ 不为无和集.

若 $u_{i+1}=2 u_{i}$, 则

$$
f(1)+f\left(u_{i}\right)=f\left(u_{i+1}\right)=2 f\left(u_{i}\right),
$$

得 $u_{i}=1$, 矛盾. 若 $u_{i}=2 u_{i+1}$, 则

$$
f\left(u_{i}\right)>f\left(u_{i+1}\right)>f\left(u_{i}\right),
$$

矛盾. 于是, 必有 $u_{i+1}-u_{i}= \pm 1$.

又 $\forall 0 \leq i \leq n-2$, 由 $f\left(u_{i}\right) \neq f\left(u_{i+2}\right)$ 知 $u_{i} \neq u_{i+2}$. 从而, 有

$$
u_{i+1}-u_{i}=u_{i+2}-u_{i+1}
$$

因此, $u_{i+1}-u_{i}(i=0,1, \cdots, n-1)$ 全为 1 或全为 -1 . 于是, $u_{n}-u_{0}= \pm n$.

因为 $\left\{f(c), f\left(u_{0}\right), f\left(u_{n}\right)\right\}$ 不为无和集, 所以 $\left\{c, u_{0}, u_{n}\right\}$ 不为无和集. 由

$$
f\left(u_{n}\right)>f\left(u_{0}\right) \geq s
$$

知 $u_{0}, u_{n}>2 c$. 若 $u_{n}=2 u_{0}$, 则

$$
f(c)+f\left(u_{0}\right)=f\left(u_{n}\right)=2 f\left(u_{0}\right),
$$

得 $c=u_{0}$, 矛盾. 若 $u_{0}=2 u_{n}$, 则

$$
f\left(u_{0}\right)>f\left(u_{n}\right)>f\left(u_{0}\right),
$$

矛盾. 于是, 必有 $u_{n}-u_{0}= \pm c$.

因此, $c=n$. 即 $\forall n \in \mathbb{N}^{*}, f(n)=n f(1)$. 最后, 结合 $f$ 为满射立知 $f(n)=$ $n, \forall n \in \mathbb{N}^{*}$. 容易验证, 上述 $f$ 满足要求.

因此, 所求 $f$ 为 $f(x)=x\left(x \in \mathbb{N}^{*}\right)$.

评注 这是一道简单的函数方程, 从尽量简单 (二元, 三元) 的无和集入手即可比较容易地做出.

5. 在 $x y$ - 坐标平面中, 横纵坐标都为整数的点称为格点, 所有顶点均为格点的多边形称为“格点多边形”.

令 $\Gamma$ 为一个凸的格点多边形. 证明: 可将 $\Gamma$ 置于另一个凸的格点多边形 $\Omega$内, 使得所有 $\Gamma$ 的顶点都落在 $\Omega$ 的边界上, 并且 $\Omega$ 恰有一个顶点不是 $\Gamma$ 的顶点.

证明 我们先证明: 若格点三角形 $\triangle A B C$ 面积为 $\frac{1}{2}$, 则对任意格点向量(即横纵分量均为整数的分量)均可表示为 $k \cdot \overrightarrow{A B}+l \cdot \overrightarrow{A C}(k, l \in \mathbb{Z})$ 的形式.

取点 $D$ 使 $A B D C$ 为平行四边形. 由 Pick 定理知平行四边形 $A B C D$ 除四个顶点外不含别的格点, 即 $\forall u, v \in[0,1), u, v$ 不全为 0 , 均有 $u \cdot \overrightarrow{A B}+v \cdot \overrightarrow{A C}$不为格点向量. 再取 $\forall p, q \in \mathbb{Z}$, 可知 $(p+u) \cdot \overrightarrow{A B}+(q+v) \cdot \overrightarrow{A C}$ 也不为格点向量.于是, $\forall k, l \in \mathbb{R}, k, l$ 不全为整数, 必有 $k \cdot \overrightarrow{A B}+l \cdot \overrightarrow{A C}$ 不为格点向量. 又任意格点向量必能化为 $k \cdot \overrightarrow{A B}+l \cdot \overrightarrow{A C}(k, l \in \mathbb{R})$ 形式. 故其中的 $k, l \in \mathbb{Z},(*)$ 获证.

回到原题: 对 $\Gamma$ 的每条边, 此边上的所有格点将该边分为长度相等的若干段, 称分成的这些线段为此边的基本线段, 每条基本线段的长度为此边的基本长
度. 考虑 $\Gamma$ 的基本长度最长的边, 设为 $B C$.

若 $B C$ 水平或垂直, 则易知 $\Gamma$ 只有水平与垂直的边, 故 $\Gamma$ 为矩形, 此时结论显然成立.

下考虑 $B C$ 不为水平及垂直的的情况, 不妨设如图所示, 并设 $B C$ 两邻边分别为 $A B, C D$. 如图, 可取格点 $T$ 使 $B T$ 垂直, $C T$ 水平.



将 $\triangle B C T$ 用其所含的格点进行三角剖分, 直到不能再分为止, 则这些小三角形均不含除了顶点的其他格点, 从而由 Pick 定理知它们的面积均为 $\frac{1}{2}$.

设 $B P, C Q$ 为 $B C$ 边上的基本线段. 设上述三角剖分中以 $B P$ 为边的小三角形为 $\triangle B P X$, 则 $\triangle B P X, \triangle C Q X$ 面积均为 $\frac{1}{2}$.

若 $X$ 与 $\Gamma$ 在直线 $A B$ 两侧. 设 $B U$ 为 $A B$ 边上的基本线段.

因为 $\triangle B X P$ 面积为 $\frac{1}{2}$, 所以由 $(*)$ 知存在 $k, l \in \mathbb{Z}$ 使

$$
\overrightarrow{U B}=k \cdot \overrightarrow{B X}+l \cdot \overrightarrow{B P}
$$

因为 $X, P$ 在 $A B$ 两侧且 $\angle P B X$ 为锐角, 所以 $k, l \in \mathbb{N}^{*}$. 于是,

$$
|\overrightarrow{U B}|=|k \cdot \overrightarrow{B X}+l \cdot \overrightarrow{B P}|>k|\overrightarrow{B P}| \geq|\overrightarrow{B P}|,
$$

这与 $B C$ 为基本长度最长的边矛盾.

于是 $X$ 与 $\Gamma$ 在直线 $A B$ 同侧, 同理 $X$ 与 $\Gamma$ 在直线 $C D$ 同侧. 此时, 取 $\Omega$ 为 $X$ 与 $\Gamma$ 的凸包, 易知其满足要求.

评注 这是一道十分困难的题. 有关格点的题较少见导致不太容易找到合适的方法利用好格点. 证明中的 (*) 尤为关键, 起到了从图形往代数关系转化的作用.

6. 对每个整数 $n \geq 2$. 记 $F(n)$ 为 $n$ 最大的素因子. 一个“奇异对” 是一对不同的素数 $p$ 和 $q$, 使得没有整数 $n \geq 2$ 满足 $F(n) F(n+1)=p q$. 证明: 存在无穷多对奇异对。

证明 对奇素数 $p$, 称满足 $2^{s} \equiv 1(\bmod p)$ 的最小正整数为 2 模 $p$ 的阶, 记
为 $r(p)$.

若存在两不同奇素数 $p_{1}<p_{2}$, 使得 $r\left(p_{1}\right)=r\left(p_{2}\right)$, 我们证明: $\left(2, p_{1}\right)$ 为奇异对.

记 $r=r\left(p_{1}\right)=r\left(p_{2}\right)$. 假设存在 $n \in \mathbb{N}^{*}$ 使

$$
F(n) F(n+1)=2 p_{1},
$$

则必有 $F(n), F(n+1)$ 一个为 2, 一个为 $p$. 于是, 存在 $\alpha \in \mathbb{N}^{*}$, 使 $F\left(2^{\alpha}+1\right)=p_{1}$或 $F\left(2^{\alpha}-1\right)=p_{1}$.

若 $F\left(2^{\alpha}+1\right)=p_{1}$, 则 $2^{\alpha} \equiv-1\left(\bmod p_{1}\right)$. 由此可知 $2 \mid r$ 且 $\alpha$ 为 $\frac{r}{2}$ 的奇数倍. 从而 $2^{\alpha} \equiv-1\left(\bmod p_{2}\right)$, 即 $p_{2} \mid 2^{\alpha}+1$. 于是,

$$
F\left(2^{\alpha}+1\right) \geq p_{2}>p_{1}
$$

与 $F\left(2^{\alpha}+1\right)=p_{1}$ 矛盾.

若 $F\left(2^{\alpha}-1\right)=p_{1}$, 则 $2^{\alpha} \equiv 1\left(\bmod p_{1}\right)$. 由此可知 $r \mid \alpha$. 从而 $2^{\alpha} \equiv 1$ $\left(\bmod p_{2}\right)$, 即 $p_{2} \mid 2^{\alpha}-1$. 于是,

$$
F\left(2^{\alpha}-1\right) \geq p_{2}>p_{1},
$$

与 $F\left(2^{\alpha}-1\right)=p_{1}$ 矛盾.

于是, $(*)$ 获证.

我们再证明: 对任意素数 $q>5$, 存在两个不同素数, 满足 2 模它们的阶均为 $4 q$.

任取 $2^{2 q}+1$ 的一个大于 5 的素因子 $p$. 设 $r(p)=r$, 则由 $2^{2 q} \equiv-1(\bmod p)$知 $2 \mid r$ 且 $2 q$ 为 $\frac{r}{2}$ 的奇数倍. 故 $r=4$ 或者 $4 q$. 若 $r=4$, 则 $p \mid 2^{4}-1$ 与 $p>5$ 为素数矛盾. 因此 $r(p)=4 q$.

于是, 只需证明 $2^{2 q}+1$ 有两个不同的大于 5 的素因子. 注意到

$$
2^{2 q}+1=(4+1)\left(4^{q-1}-4^{q-2}+\cdots-4+1\right),
$$

且其中

$$
4^{q-1}-4^{q-2}+\cdots-4+1 \equiv q \cdot 1 \not \equiv 0 \quad(\bmod 5)
$$

所以 $2^{2 q}+1$ 所含 5 的幂次至多为 1 . 显然

$$
3 \nmid 2^{2 q}+1,2 \nmid 2^{2 q}+1 .
$$

又

$$
2^{2 q}+1=2^{2 q}+2^{q+1}+1-2^{q+1}=\left(2^{q}+2^{\frac{q+1}{2}}+1\right)\left(2^{q}-2^{\frac{q+1}{2}}+1\right),
$$

其中

$$
2^{q}+2^{\frac{q+1}{2}}+1>2^{q}-2^{\frac{q+1}{2}}+1>5
$$

且

$$
\operatorname{gcd}\left(2^{q}+2^{\frac{q+1}{2}}+1,2^{q}-2^{\frac{q+1}{2}}+1\right)=\operatorname{gcd}\left(2^{q}+2^{\frac{q+1}{2}}+1,2^{\frac{q+3}{2}}\right)=1
$$

所以 $2^{2 q}+1$ 必有两个不同的大于 5 的素因子.

至此, (**) 获证.

由 $(*)$ 及 $(* *)$ 立得所证结论成立.

评注 这是一道十分有难度的数论题. 解答并不复杂, 其中的 (*) 也是自然的. 但核心难点在于 $(*)$ 的作用太强, 反而会产生很多有希望的方向, 容易让人陷进去. 这是一道十分有价值的训练题。

总评 此次大师杯的第 $1,2,4$ 题均属于中档偏简单题. 第 3 题利用了生成树的想法, 第 5 题则需要对格点有一定的了解, 第 6 题入手不难, 难在之后方向的选取. 总体来说, 这套题目难度较大, $3,5,6$ 三道题中解出一道就具有一定的竞争力.

