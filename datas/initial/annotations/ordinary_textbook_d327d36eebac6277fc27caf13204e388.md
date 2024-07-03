数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2023 年韩国数学奥林匹克试题解析 

王康印<br>(湖南师范大学附属中学, 410006)<br>指导教师: 刘伟才

2023 年韩国奥林匹克于今年 3 月 25 日、 26 日两天举行. 下面笔者整理了试题及其解答, 并作了简要的评析, 供读者参考. 因笔者水平有限, 有不当之处,恳请读者批评指正.

## I. 试 题

1. 在 $\triangle A B C$ 中, $A B<A C$, 点 $D$ 和点 $E$ 分别在线段 $A B$ 和 $A C$ 上 (异于端点). 点 $P$ 满足 $P B=P D, P C=P E$. 点 $X$ 在 $\triangle A B C$ 外接圆的不含点 $B$的弧 $\overparen{A C}$ 上 (异于 $A, C$ ). 设直线 $X A$ 和 $\triangle A D E$ 的外接圆的另一个交点为 $Y$.求证: $P X=P Y$.
2. 函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$满足对任意正实数 $x$, 存在正实数 $y$, 使得

$$
(x+f(y))(y+f(x)) \leq 4,
$$

且符合要求的 $y$ 的个数是有限的. 求证: 对任意正实数 $x<y$, 都有 $f(x)>f(y)$.
3. $p$ 为奇素数, 设 $A(n)$ 为集合 $\{1,2, \cdots, n\}$ 的全体元素之和为 $p$ 的倍数的子集的个数. 求证: 若 $2^{p-1}-1$ 不是 $p^{2}$ 的倍数, 则对任意整数 $k$, 存在无穷多个正整数 $m$ 使得 $\frac{A(m)-k}{p} \in \mathbb{Z}$.

4. 求所有正整数 $n$, 使得 $2^{n}-1$ 没有大于 7 的素因子.
5. 给定正整数 $n$, 和 $n$ 个盒子 $B_{1}, B_{2}, \cdots, B_{n}$. 按照下述规则在盒子中放入小球: 选择两个正整数 $1 \leq j \leq i \leq n$, 在满足 $j \leq k \leq i$ 的每个盒子 $B_{k}$ 中各放入一个小球. 设开始时每个盒子中的小球数依次为 $x_{1}, x_{2}, \cdots, x_{n}$, 其中 $x_{i}(1 \leq$ $i \leq n)$ 均为正整数. 设将每个盒子中的小球数量变为 3 的倍数所需要的最小操[^0]作次数为 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$. 对所有不同的初始状态, 求 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的最大值. (若 $x_{1}, x_{2}, \cdots, x_{n}$ 均为 3 的倍数, 则 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)=0$.)
6. 对正整数 $n \geq 3$ 和实数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$, 求证:

$$
\sum_{i=1}^{n} a_{i}\left(b_{i}-b_{i+3}\right) \leq \frac{3 n}{8} \sum_{i=1}^{n}\left(\left(a_{i}-a_{i+1}\right)^{2}+\left(b_{i}-b_{i+1}\right)^{2}\right) .
$$

其中 $a_{n+1}=a_{1}$, 对 $i=1,2,3, b_{n+i}=b_{i}$.

## II. 解答与评注

题 1 在 $\triangle A B C$ 中, $A B<A C$, 点 $D$ 和点 $E$ 分别在线段 $A B$ 和 $A C$ 上 (异于端点). 点 $P$ 满足 $P B=P D, P C=P E$. 点 $X$ 在 $\triangle A B C$ 外接圆的不含点 $B$的弧 $\overparen{A C}$ 上 (异于 $A, C$ ). 设直线 $X A$ 和 $\triangle A D E$ 的外接圆的另一个交点为 $Y$.求证: $P X=P Y$.

![](https://cdn.mathpix.com/cropped/2024_02_26_e5c3db66a96074af79a1g-2.jpg?height=545&width=546&top_left_y=1121&top_left_x=755)

证明 设 $A$ 在圆 $(A D E)$ 和圆 $(A B C)$ 上的对径点分别为 $A_{1}, A_{2}$. 则可得 $\angle A D A_{1}=\angle A E A_{1}=\angle A B A_{2}=\angle A C A_{2}=\angle A Y A_{1}=\angle A X A_{2}=90^{\circ}$,设线段 $A_{1} A_{2}, B D, C E, X Y$ 的中点分别为 $P^{\prime}, M, N, K$, 则

$$
P^{\prime} M \perp A B, P^{\prime} N \perp A C
$$

从而 $P^{\prime} B=P^{\prime} D, P^{\prime} C=P^{\prime} E$, 故 $P^{\prime}$ 与 $P$ 重合.

于是 $P K \perp A X$, 进而 $P X=P Y$. 证毕.

评注 本题是简单题, 用直角梯形中位线的几何性质即可.

题 2 函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$满足对任意正实数 $x$, 存在正实数 $y$, 使得

$$
(x+f(y))(y+f(x)) \leq 4,
$$

且符合要求的 $y$ 的个数是有限的. 求证: 对任意正实数 $x<y$, 都有 $f(x)>f(y)$.
证明 (李由) 记 $g(x, y)=(x+f(y))(y+f(x))$, 假设存在 $0<a<b$, 使得 $f(a) \leq f(b)$, 则由题意, 存在 $c>0$, 满足 $(c+f(b))(b+f(c)) \leq 4$.

若集合 $F=\{x \mid f(x) \leq f(b), a<x<b\}$ 是无限集, 则对任意 $x \in F$, 有

$$
g(c, x)=(c+f(x))(x+f(c)) \leq(c+f(b))(b+f(c)) \leq 4,
$$

即对 $c$ 而言, 满足 $g(c, x) \leq 4$ 的正数 $x$ 有无穷多, 矛盾.

故集合 $H=\{x \mid f(x)>f(b), a<x<b\}$ 是无限集.

若

$$
T=\{y \mid \text { 存在 } x \in H, g(x, y) \leq 4\}
$$

是有限集合, 必存在某个 $y_{0} \in T$, 满足有无穷多个 $x \in H$, 使得 $g\left(x, y_{0}\right) \leq 4$, 矛盾; 若 $T$ 是无限集, 则对任意 $y \in T$, 存在 $x_{0} \in H$, 有 $g\left(y, x_{0}\right) \leq 4$. 而

$$
g(a, y)=(a+f(y))(y+f(a)) \leq\left(x_{0}+f(y)\right)\left(y+f\left(x_{0}\right)\right)=g\left(y, x_{0}\right) \leq 4
$$

即有无穷多个 $y$, 使得 $g(a, y) \leq 4$, 矛盾.

综上可得假设矛盾, 故对任意正实数 $x<y$, 都有 $f(x)>f(y)$.

评注 此题属于中档题. 需要用反证法, 并利用大小关系导出一些基本性质,并将其反复运用即可. 值得注意的是条件中的 4 不是本质的, 可以换成任意一个正实数.

题 $3 p$ 为奇素数, 设 $A(n)$ 为集合 $\{1,2, \cdots, n\}$ 的全体元素之和为 $p$ 的倍数的子集的个数. 求证: 若 $2^{p-1}-1$ 不是 $p^{2}$ 的倍数, 则对任意整数 $k$, 存在无穷多个正整数 $m$ 使得 $\frac{A(m)-k}{p} \in \mathbb{Z}$.

证明 待定 $n=s p$, 考虑生成函数 $(1+x)\left(1+x^{2}\right) \cdots\left(1+x^{s p}\right)$, 任取某个 $p$次单位根 $\varepsilon(\neq 1)$, 熟知

(1) $1+\varepsilon^{k}+\varepsilon^{2 k}+\cdots+\varepsilon^{(p-1) k}=\left\{\begin{array}{l}0, p \nmid k \\ p, p \mid k\end{array}\right.$;

(2) $(1+\varepsilon)\left(1+\varepsilon^{2}\right) \cdots\left(1+\varepsilon^{p-1}\right)\left(1+\varepsilon^{p}\right)=2$;

故集合 $\{1,2, \cdots, n\}$ 的全体元素之和为 $p$ 的倍数的子集的个数

$$
\begin{aligned}
A(s p) & =\frac{1}{p} \sum_{k=0}^{p-1}\left(1+\varepsilon^{k}\right)\left(1+\varepsilon^{2 k}\right) \cdots\left(1+\varepsilon^{s p k}\right) \\
& =\frac{1}{p} \sum_{k=0}^{p-1}\left[\left(1+\varepsilon^{k}\right)\left(1+\varepsilon^{2 k}\right) \cdots\left(1+\varepsilon^{p k}\right)\right]^{s} \\
& =\frac{1}{p}\left[2^{s p}+(p-1) 2^{s}\right]
\end{aligned}
$$

$$
=2^{s}\left(\frac{2^{s(p-1)}-1}{p}+1\right)
$$

又由费马小定理, $2^{p-1} \equiv 1(\bmod p)$, 故

$$
\frac{2^{s(p-1)}-1}{p}=\frac{2^{p-1}-1}{p}\left(2^{(s-1)(p-1)}+\cdots+2^{p-1}+1\right) \equiv s \frac{2^{p-1}-1}{p} \quad(\bmod p) .
$$

由 $p^{2} \nmid 2^{p-1}-1$, 可令 $t \cdot \frac{2^{p-1}-1}{p} \equiv 1(\bmod p)$, 从而对任意整数 $k$, 取

$$
m=s p=(p x-k+1) t(p-1) p \text {, 其中 } x>\frac{k-1}{p}, x, t \in \mathbb{N} \text {, }
$$

于是

$$
\begin{aligned}
A(m) & =A(s p)=2^{s}\left(\frac{2^{s(p-1)}-1}{p}+1\right) \equiv s \frac{2^{p-1}-1}{p}+1 \\
& \equiv(p x-k+1) t(p-1) \frac{2^{p-1}-1}{p}+1 \equiv k \quad(\bmod p)
\end{aligned}
$$

即 $\frac{A(m)-k}{p} \in \mathbb{Z}$, 且易知 $m$ 有无穷多个.

评注 此题思维难度不大, 主要考察数论方面的基本功. 需要观察到 $A(p k)$便于计算, 并通过生成函数和单位根性质计算 $A(p k)$, 进一步增加条件即可.

题 4 求所有正整数 $n$, 使得 $2^{n}-1$ 没有大于 7 的素因子.

解 容易验证, 对 $n \leq 12$ 时, $n=1,2,3,4,6$ 满足题意.

当 $n \geq 13$ 时, 若 $n$ 有大于 3 的素因子 $p$, 则取 $2^{p}-1$ 的素因子 $q$, 有 $2^{n} \equiv 2^{p} \equiv 1(\bmod q)$, 知 2 对模 $q$ 的阶为 $p$, 又由费马小定理 $2^{q-1} \equiv 1(\bmod q)$,故 $p \mid q-1$, 故 $q-1 \geq 2 p \geq 10$, 于是 $q>11$, 且 $q \mid 2^{n}-1$, 故 $n$ 不符合题意.

若 $n$ 的素因子都不大于 3 , 设 $n=2^{\alpha} \cdot 3^{\beta}$,

若 $\alpha \geq 3$, 则 $2^{8}-1 \mid 2^{n}-1$, 故 $17 \mid 2^{n}-1$, 不符合题意,

若 $\alpha \leq 2$, 则 $3^{\beta}=\frac{n}{2^{\alpha}}>\frac{13}{4}>3$, 得 $\beta \geq 2$, 故 $2^{9}-1 \mid 2^{n}-1$, 即 $73 \mid 2^{n}-1$,不符合题意.

综上, $n=1,2,3,4,6$ 为所求.

评注 本题是数论基础题, 只需用到阶的性质再适当讨论即可.

题 5 给定正整数 $n$, 和 $n$ 个盒子 $B_{1}, B_{2}, \cdots, B_{n}$. 按照下述规则在盒子中放入小球：选择两个正整数 $1 \leq j \leq i \leq n$, 在满足 $j \leq k \leq i$ 的每个盒子 $B_{k}$ 中各放入一个小球。设开始时每个盒子中的小球数依次为 $x_{1}, x_{2}, \cdots, x_{n}$,其中 $x_{i}(1 \leq i \leq n)$ 均为正整数. 设将每个盒子中的小球数量变为 3 的倍数所需要的最小操作次数为 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$. 对所有不同的初始状态, 求
$f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的最大值.

注: 若 $x_{1}, x_{2}, \cdots, x_{n}$ 均为 3 的倍数, 则 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)=0$.

解 (刘家宏, 王康印) $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的最大值为 $\left[\frac{2 n+4}{3}\right]$.

我们先证明 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right) \leq\left[\frac{2 n+4}{3}\right]$.

对 $n=1,2,3$, 枚举可得 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的最大值分别为 $2,2,3$, 考虑 $g\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\left(-x_{1}, x_{1}-x_{2}, \cdots, x_{n-1}-x_{n}, x_{n}\right)=\left(t_{1}, t_{2}, \cdots, t_{n+1}\right)$, 则设操作中将 $x_{j}, \cdots, x_{i}(1 \leq j \leq i \leq n)$ 每个数增加 1 , 相当于将 $t_{j}$ 变为 $t_{j}-1$, 将 $t_{i+1}$ 变为 $t_{i+1}+1$, 其他 $t_{k}(k \neq i+1, j)$ 不变, 且操作前后 $t_{1}+t_{2}+\cdots+t_{n+1}=0$不变, 操作目标是使得

$$
t_{1} \equiv t_{2} \equiv \cdots \equiv t_{n+1} \equiv 0 \quad(\bmod 3)
$$

假设 $n \leq k$ 时, 都有 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right) \leq\left[\frac{2 n+4}{3}\right]$, 则 $n=k+1$ 时,

情形 $1 t_{1}, t_{2}, \cdots, t_{k+2}$ 中有模 3 余 0 的数 $t_{s}$, 则我们操作时不选择 $t_{s}$, 故由归纳假设, 操作次数不超过 $\left[\frac{2 k+4}{3}\right] \leq\left[\frac{2(k+1)+4}{3}\right]$.

情形 $2 t_{1}, t_{2}, \cdots, t_{k+2}$ 中没有数模 3 余 0 , 由 $k+2 \geq 5$, 知必有 3 个数模 3 同余, 设

$$
t_{i} \equiv t_{j} \equiv t_{k} \quad(\bmod 3)(i<j<k)
$$

若 $t_{i} \equiv 1(\bmod 3)$, 则先对 $t_{i}, t_{k}$ 操作一次, 再对 $t_{j}, t_{k}$ 操作一次, 则两次操作后

$$
t_{i}^{\prime}=t_{i}-1, t_{j}^{\prime}=t_{j}-1, t_{k}^{\prime}=t_{k}+2,
$$

故 $t_{i}^{\prime} \equiv t_{j}{ }^{\prime} \equiv t_{k}{ }^{\prime} \equiv 0(\bmod 3)$, 后面操作中 $t_{i}{ }^{\prime}, t_{j}{ }^{\prime}, t_{k}{ }^{\prime}$ 保持不变, 故由归纳假设,

$$
f\left(x_{1}, x_{2}, \cdots, x_{k+1}\right) \leq\left[\frac{2(k-2)+4}{3}\right]+2=\left[\frac{2(k+1)+4}{3}\right] .
$$

若 $t_{i} \equiv 2(\bmod 3)$, 则先对 $t_{i}, t_{k}$ 操作一次, 再对 $t_{i}, t_{j}$ 操作一次, 则两次操作后

$$
t_{i}^{\prime}=t_{i}-2, t_{j}^{\prime}=t_{j}+1, t_{k}^{\prime}=t_{k}+1
$$

故 $t_{i}{ }^{\prime} \equiv t_{j}{ }^{\prime} \equiv t_{k}{ }^{\prime} \equiv 0(\bmod 3)$, 后面操作中 $t_{i}{ }^{\prime}, t_{j}{ }^{\prime}, t_{k}{ }^{\prime}$ 保持不变, 同样由归纳假设,

$$
f\left(x_{1}, x_{2}, \cdots, x_{k+1}\right) \leq\left[\frac{2(k-2)+4}{3}\right]+2=\left[\frac{2(k+1)+4}{3}\right],
$$

综上, 由数学归纳法原理,

$$
f\left(x_{1}, x_{2}, \cdots, x_{n}\right) \leq\left[\frac{2 n+4}{3}\right]
$$

另一方面, 定义 $T(a, b)$ 考虑给数组 $(a, b)$ 赋值, 其中 $(a, b)$ 为在模 3 意义下考虑, 设

$$
T(1,0)=T(2,1)=T(0,2)=2,
$$

$$
\begin{aligned}
& T(0,1)=T(1,2)=T(2,0)=1 \\
& T(0,0)=T(1,1)=T(2,2)=0
\end{aligned}
$$

则

$$
\begin{gathered}
T(a, b)=T(a+1, b+1), \\
T(a+1, b)=T(a, b)-1 T(a, b)+2, \\
T(a, b+1)=T(a, b)-2 T(a, b)+1,
\end{gathered}
$$

记 $S\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\sum_{i=1}^{n-1} T\left(x_{i}, x_{i+1}\right)$, 考虑每一次操作后 $S$ 取值的变化.

(1) 若 $y_{1}, y_{n}$ 均末操作, 则最多有两个 $T$ 值发生变化, $S^{\prime} \geq S-3$.

(2) 若 $y_{1}$ 被操作, 则 $S^{\prime} \geq S-1$.

(3) 若 $y_{n}$ 被操作, 则 $S^{\prime} \geq S-2$.

下面令

$$
y_{i}= \begin{cases}1, i \equiv 1 & (\bmod 3) \\ 0, i \equiv 2 & (\bmod 3) \\ 2, i \equiv 3 & (\bmod 3)\end{cases}
$$

则

$$
S\left(y_{1}, y_{2}, \cdots, y_{n}\right)=\sum_{i=1}^{n-1} T\left(y_{i}, y_{i+1}\right)=2 n-2
$$

则 $y_{1}$ 被操作两次, 要想 $S$ 取值最终为 0 , 则操作次数不小于 $\left\lceil\frac{2 n-2+2 \times 2}{3}\right\rceil=\left[\frac{2 n+4}{3}\right]$.

综上, $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的最大值为 $\left[\frac{2 n+4}{3}\right]$.

评注 此题有一定难度, 数学归纳法的想法是自然的, 而类似差分的处理可以让我们对一些量的关系观察的更清楚. 构造和验证的难度不小, 注意到相邻对的差受操作的影响较小, 于是按照对相邻对按差分类赋值进行分析即可.

题 6 对正整数 $n \geq 3$ 和实数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$, 求证:

$$
\sum_{i=1}^{n} a_{i}\left(b_{i}-b_{i+3}\right) \leq \frac{3 n}{8} \sum_{i=1}^{n}\left(\left(a_{i}-a_{i+1}\right)^{2}+\left(b_{i}-b_{i+1}\right)^{2}\right)
$$

其中 $a_{n+1}=a_{1}$, 对 $i=1,2,3, b_{n+i}=b_{i}$.

证明 先证明如下引理:

引理 对 $n \geq 3, a_{1}, a_{2}, \cdots, a_{n} \in \mathbb{R}$, 有

$$
16 \sum_{i=1}^{n}\left(a_{i}-\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}\right)^{2} \leq n^{2} \sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2}
$$

引理证明 1 (王康印) 注意到

$$
\begin{aligned}
& 16 \sum_{i=1}^{n}\left(a_{i}-\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}\right)^{2} \\
& =16 \sum_{i=1}^{n}\left[a_{i}^{2}+\left(\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}\right)^{2}-2 a_{i} \frac{a_{1}+a_{2}+\cdots+a_{n}}{n}\right] \\
& =\frac{16}{n}\left(n \sum_{i=1}^{n} a_{i}^{2}-\left(\sum_{i=1}^{n} a_{i}\right)^{2}\right) \\
& =\frac{16}{n} \sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2} .
\end{aligned}
$$

设 $a_{n+i}=a_{i}, 1 \leq i \leq n$. 注意到对 $1 \leq i<j \leq n$, 当 $j-i \leq \frac{n-1}{2}$ 时,

$$
\begin{aligned}
\left(a_{i}-a_{j}\right)^{2} & =\left[\left(a_{i}-a_{i+1}\right)+\cdots+\left(a_{j-1}-a_{j}\right)\right]^{2} \\
& \leq\left[\left(a_{i}-a_{i+1}\right)^{2}+\cdots+\left(a_{j-1}-a_{j}\right)^{2}\right](j-i)
\end{aligned}
$$

注意到当 $j-i>\frac{n-1}{2}$ 时,

$$
\begin{aligned}
\left(a_{i}-a_{j}\right)^{2} & =\left(a_{n+i}-a_{j}\right)^{2}=\left[\left(a_{j}-a_{j+1}\right)+\cdots+\left(a_{n+i-1}-a_{n+i}\right)\right]^{2} \\
& \leq\left[\left(a_{j}-a_{j+1}\right)^{2}+\cdots+\left(a_{n+i-1}-a_{n+i}\right)^{2}\right](n+i-j)
\end{aligned}
$$

故

$$
\begin{aligned}
& \frac{16}{n} \sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2}=\frac{8}{n} \sum_{1 \leq i, j \leq n}\left(a_{i}-a_{j}\right)^{2}=\frac{8}{n} \sum_{i=1}^{n} \sum_{j=i}^{n+i-1}\left(a_{i}-a_{j}\right)^{2} \\
& =\frac{8}{n}\left[\sum_{k=1}^{\left[\frac{n-1}{2}\right]} \sum_{i=1}^{n}\left(a_{i}-a_{i+k}\right)^{2}+\sum_{k=\left[\frac{n-1}{2}\right]+1}^{n-1} \sum_{i=1}^{n}\left(a_{i}-a_{i+k}\right)^{2}\right] \\
& \leq \frac{8}{n}\left[\sum_{k=1}^{\left[\frac{n-1}{2}\right]}\left(k \sum_{i=1}^{n} \sum_{j=i}^{i+k-1}\left(a_{j}-a_{j+1}\right)^{2}\right)+\sum_{k=\left[\frac{n-1}{2}\right]+1}^{n-1}(n-k) \sum_{i=1}^{n} \sum_{j=i+k}^{n+i-1}\left(a_{j}-a_{j+1}\right)^{2}\right] \\
& =\frac{8}{n}\left[\sum_{j=1}^{n}\left(a_{j}-a_{j+1}\right)^{2}\left(1^{2}+2^{2}+\cdots+\left[\frac{n-1}{2}\right]^{2}\right)\right. \\
& \left.+\sum_{j=1}^{n}\left(a_{j}-a_{j+1}\right)^{2}\left(1^{2}+2^{2}+\cdots+\left(n-\left[\frac{n-1}{2}\right]-1\right)^{2}\right)\right] \\
& =\frac{8}{n}\left[\left(1^{2}+2^{2}+\cdots+\left[\frac{n-1}{2}\right]^{2}\right)+\left(1^{2}+2^{2}+\cdots+\left(n-\left[\frac{n-1}{2}\right]-1\right)^{2}\right)\right] \\
& \cdot \sum_{j=1}^{n}\left(a_{j}-a_{j+1}\right)^{2}
\end{aligned}
$$

上面 $(*)$ 式因为 $\sum_{j=i}^{i+k-1}\left(a_{j}-a_{j+1}\right)^{2}$ 表示和式 $\sum_{j=1}^{n}\left(a_{j}-a_{j+1}\right)^{2}$ 中连续 $k$ 项的和, 故
每一项 $\left(a_{j}-a_{j+1}\right)^{2}$ 在和式 $\sum_{i=1}^{n}\left(\sum_{j=i}^{i+k-1}\left(a_{j}-a_{j+1}\right)^{2}\right)$ 中恰出现 $k$ 次, $(*)$ 式后面部分类似.

接下来我们只需证明下列不等式成立:

$\frac{8}{n}\left[\left(1^{2}+2^{2}+\cdots+\left[\frac{n-1}{2}\right]^{2}\right)+\left(1^{2}+2^{2}+\cdots+\left(n-\left[\frac{n-1}{2}\right]-1\right)^{2}\right)\right] \leq n^{2}$.

当 $n=2 k+1(k \geq 1)$ 时, $(* *)$ 左边等于

$$
\frac{16}{2 k+1}\left(1^{2}+2^{2}+\cdots+k^{2}\right)=\frac{8}{3} k(k+1)<\frac{8}{3}\left(\frac{k+k+1}{2}\right)^{2}<(2 k+1)^{2}=n^{2}
$$

当 $n=2 k(k \geq 2)$ 时, $(* *)$ 左边等于

$$
\begin{aligned}
& \frac{4}{k}\left[\left(1^{2}+\cdots+(k-1)^{2}\right)+\left(1^{2}+\cdots+k^{2}\right)\right] \\
& =\frac{4}{k}\left[\frac{(k-1) k(2 k-1)}{6}+\frac{k(k+1)(2 k+1)}{6}\right] \\
& =\frac{8 k^{2}+4}{3}<4 k^{2}=n^{2}
\end{aligned}
$$

故 $(* *)$ 式成立, 于是引理得证.

引理证明 2 (彭满琳) 考虑对 $\sum_{i=1}^{n} a_{i}=0(n \geq 3)$, 证明:

$$
16 \sum_{i=1}^{n} a_{i}^{2} \leq n^{2} \sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2}
$$

事实上, 上面不等式等价于

$$
\sum_{i=1}^{n} a_{i} a_{i+1} \leq \frac{n^{2}-8}{n^{2}} \sum_{i=1}^{n} a_{i}^{2}
$$

而由 Fan 不等式, 有 $\sum_{i=1}^{n} a_{i} a_{i+1} \leq \cos \frac{2 \pi}{n} \sum_{i=1}^{n} a_{i}^{2}$, 故只需证明

$$
\cos \frac{2 \pi}{n} \leq \frac{n^{2}-8}{n^{2}}(n \geq 3)
$$

当 $n \geq 3$ 时, 由 $y=\frac{\sin x}{x}$ 在 $x \in\left(0, \frac{\pi}{2}\right)$ 上单调递减, 可得 $\frac{\sin x}{x}>\frac{2}{\pi}$, 故

$$
\cos \frac{2 \pi}{n}=1-2 \sin ^{2} \frac{\pi}{n}<1-2\left(\frac{2}{\pi} \times \frac{\pi}{n}\right)^{2}=\frac{n^{2}-8}{n^{2}},
$$

从而引理得证.

回到原题, 由引理及柯西不等式和均值不等式可得

$$
\begin{aligned}
& \sum_{i=1}^{n} a_{i}\left(b_{i}-b_{i+3}\right) \\
& =\sum_{i=1}^{n}\left(a_{i}-\frac{a_{1}+\cdots+a_{n}}{n}\right)\left(b_{i}-b_{i+3}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \leq \sqrt{\sum_{i=1}^{n}\left(a_{i}-\frac{a_{1}+\cdots+a_{n}}{n}\right)^{2} \sum_{i=1}^{n}\left(b_{i}-b_{i+3}\right)^{2}} \\
& \leq \sqrt{\frac{n^{2}}{16} \sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2} \sum_{i=1}^{n}\left(b_{i}-b_{i+3}\right)^{2}} \\
& =\sqrt{\frac{n^{2}}{16} \sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2} \sum_{i=1}^{n}\left[\left(b_{i}-b_{i+1}\right)+\left(b_{i+1}-b_{i+2}\right)+\left(b_{i+2}-b_{i+3}\right)\right]^{2}} \\
& \leq \sqrt{\frac{n^{2}}{16} \sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2} \sum_{i=1}^{n} 3\left[\left(b_{i}-b_{i+1}\right)^{2}+\left(b_{i+1}-b_{i+2}\right)^{2}+\left(b_{i+2}-b_{i+3}\right)^{2}\right]} \\
& =\frac{3 n}{4} \sqrt{\sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2} \sum_{i=1}^{n}\left(b_{i}-b_{i+1}\right)^{2}} \\
& \leq \frac{3 n}{4} \frac{\sum_{i=1}^{n}\left[\left(a_{i}-a_{i+1}\right)^{2}+\left(b_{i}-b_{i+1}\right)^{2}\right]}{2} .
\end{aligned}
$$

证毕.

评注 此题为二次型不等式, 其核心在于通过均值或柯西不等式处理后化为只关于 $\left\{a_{i}\right\}$ 的不等式, 然后进行恒等变形以及用柯西不等式放缩, 需要注意的是平移不变性的运用。


[^0]:    修订日期: 2023-04-11.

