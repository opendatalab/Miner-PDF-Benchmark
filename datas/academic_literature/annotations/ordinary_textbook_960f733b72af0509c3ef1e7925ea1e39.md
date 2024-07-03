数学新星网 苯学生专栏

www.nsmath.cn/xszl

# 2021 年土耳其数学奥林匹克 (第二轮) 试题解析 

王迪

(武汉市武钢三中, 430080)

指导教师: 邓晓

本文给出 2021 年土耳其数学奥林匹克 (第二轮) 试题的解答与评析, 其中第 $1,2,3,4$ 题是简单题, 第 5 题是中等难度的问题, 第 6 题是难题, 整体是一套质量不错的试题. 不当之处敬请指正.

## I. 试 题

1. 最初, 桌子上有两个盒子, 其中一个盒子是空的, 另一个盒子装满 29 个不同颜色的弹珠. 下面从装满的盒子开始, 对这两个盒子轮流进行如下操作: 每一次操作, 从当前盒子中选择一个或多个弹珠并转移到另一个盒子中. 如果每次操作所选择的弹珠组互不相同, 那么至多可以进行多少次操作?
2. 已知一个次数为 $d$ 的实系数多项式 $f(x)$ 有至少 $d$ 个系数为 1 , 且方程 $f(x)=0$ 恰有 $d$ 个实根, 求 $d$ 的最大值. (注: 多项式的根不必彼此不同)
3. 如图所示, 在三角形 $A B C$ 中, 圆 $\Gamma$ 与边 $B C$ 相切于点 $X$, 与边 $A C$ 相切于点 $Y . P$ 为边 $A B$ 上一点, 直线 $X P 、 Y P$ 分别与圆 $\Gamma$ 再次交于点 $K 、 L$, 直线 $A K 、 B L$ 分别与圆 $\Gamma$ 再次交于点 $R 、 S$. 求证: 直线 $X R 、 Y S 、 A B$ 相交于同一点.

![](https://cdn.mathpix.com/cropped/2024_02_26_a4b14bcda5e215f219d6g-1.jpg?height=392&width=422&top_left_y=2137&top_left_x=817)

修订日期: 2022-03-07.

4. 锐角三角形 $A B C$ 中, 点 $D 、 E$ 分别是边 $B C 、 A C$ 上的点, 且使得 $B D 、 C E$ 分别平分 $\angle A B C 、 \angle B C A$. 点 $D$ 在边 $B C 、 B A$ 上的投影分别是 $P 、 Q$, 点 $E$ 在边 $C A 、 C B$ 上的投影分别是 $R 、 S$. 设 $A P$ 与 $C Q$ 交于点 $X, A S$与 $B R$ 交于点 $Y, B X$ 与 $C Y$ 交于点 $Z$, 求证: $A Z \perp B C$.
5. 正整数 $a, b, c, d$ 满足 $\left\{a \cdot b^{n}+c \cdot d^{n}: n=1,2,3, \cdots\right\}$ 的素因数只有有限个, 求证: $b=d$.
6. 某校有 2021 位同学, 其中每一个同学恰有 $k$ 个朋友 (朋友关系是相互的), 已知不存在三位同学, 使得他们两两之间互为朋友关系, 求 $k$ 的最大值.

## II. 解答与评注

题 1 最初, 桌子上有两个盒子, 其中一个盒子是空的, 另一个盒子装满 29 个不同颜色的弹珠. 下面从装满的盒子开始, 对这两个盒子轮流进行如下操作:每一次操作, 从当前盒子中选择一个或多个弹珠并转移到另一个盒子中. 如果每次操作所选择的弹珠组互不相同, 那么至多可以进行多少次操作?

解 考虑将 29 个弹珠标记为 $1,2, \cdots, 29$, 两个盒子记为 $a 、 b$, 开始时 $b$ 盒为空的.

先证明操作次数 $\leq 2^{29}-2$. 由于 $\{1,2, \cdots, 29\}$ 的非空子集只有 $2^{29}-1$ 个,假设能操作 $2^{29}-1$ 次, 则每种弹珠组合恰被操作一次, 从而每个弹珠被操作 $2^{28}$次, 所以最终状态下所有弹珠都在 $a$ 盒. 又 $2^{29}-1$ 是奇数,则最后一次操作是从 $a$ 盒取出一些弹珠到 $b$ 盒, 与最终状态下弹珠都在 $a$ 盒, 矛盾. 所以操作次数 $\leq 2^{29}-2$.

下给出操作次数为 $2^{29}-2$ 的方案. 任意取定集合 $\{3,4, \cdots, 29\}$ 的非空子集 $A$, 依次进行如下操作：

(1) $a$ 盒中取 $A \cup\{1,2\}$ 放入 $b$ 盒 ;

(2) $b$ 盒中取 $A \cup\{1\}$ 放入 $a$ 盒;

(3) $a$ 盒中取 $A$ 放入 $b$ 盒;

(4) $b$ 盒中取 $A \cup\{2\}$ 放入 $a$ 盒.

此 4 次操作后所有弹珠仍在 $a$ 盒中, 且操作了 $A \cup\{1,2\}, A \cup\{1\}, A \cup\{2\}, A$这 4 个组合.

所以, 可依次对 $\{3,4, \cdots, 29\}$ 的所有非空子集进行上述操作, 然后再从 $a$盒中取 $\{1,2\}$ 放入 $b$ 盒, $b$ 盒中取 $\{2\}$ 放回 $a$ 盒, 共操作了 $2^{29}-2$ 次.
评注 首先要发现 $2^{29}-1$ 是不可行, 构造需要一点探索, 29 可推广到 $n(n \geq 2)$, 结果为 $2^{n}-2$, 证明是一样的. 本题亦可归纳构造, 将命题加强为最终状态下, 1 在 $b$ 盒, $2,3, \cdots, n$ 在 $a$ 盒, 且仅有 $\{1\}$ 未操作过. 利用 $n=k$ 的情形证 $n=k+1$ 时, 先操作 $2^{k}-2$ 次至 $a$ 盒中为 $2,3, \cdots, k, k+1, b$ 盒中仅有 1 (未操作含 $k+1$ 的集合), 设操作的集合依次为 $A_{1}, A_{2}, \cdots, A_{2^{k}-2}$, 再将 $k+1$放入 $b$ 盒, 将 $k+1,1$ 放回 $a$ 盒, 再对 $A_{i} \cup\{k+1\}\left(i=1,2, \cdots, 2^{k}-2\right)$ 依次操作, 共操作了 $2^{k+1}-2$ 次, 且满足最终状态的要求.

题 2 已知一个次数为 $d$ 的实系数多项式 $f(x)$ 有至少 $d$ 个系数为 1 , 且方程 $f(x)=0$ 恰有 $d$ 个实根, 求 $d$ 的最大值. (注: 多项式的根不必彼此不同)

解 $1 d$ 的最大值为 4.

当 $d=4$ 时, 取

$$
f(x)=x^{4}+x^{3}-4 x^{2}+x+1=(x-1)^{2}\left(x^{2}+3 x+1\right) \text {, }
$$

则 $f(x)=0$ 有 4 个实根.

下证 $d \geq 5$ 不符合要求. 假设 $d \geq 5$ 时,

$$
f(x)=x^{d}+x^{d-1}+\cdots+x+1-c x^{\alpha}, 0 \leq \alpha \leq d, c \in \mathbb{R},
$$

且 $f(x)=0$ 有 $d$ 个实根, 则

$$
(x-1) f(x)=x^{d+1}-1-c x^{\alpha+1}+c x^{\alpha}=0
$$

有 $d+1$ 个实根. 所以 $c \neq 0$, 方程

$$
[(x-1) f(x)]^{\prime}=(d+1) x^{d}-c(\alpha+1) x^{\alpha}+c \alpha x^{\alpha-1}=0
$$

有 $d$ 个实根, 且 0 至多被算一次.

$\alpha=0$ 时, 不成立.

$1 \leq \alpha \leq d$ 时,

$$
h(x)=(d+1) x^{d-\alpha+1}-c(\alpha+1) x+c \alpha=0
$$

至少有 $d-1$ 个实根. 于是

$$
h^{\prime}(x)=(d+1)(d-\alpha+1) x^{d-\alpha}-c(\alpha+1)=0
$$

有 $d-2$ 个实根, 所以 $d-2 \leq 2 \Rightarrow d \leq 4$, 矛盾!

解 2 只证明 $d \geq 5$ 不符合要求. 假设 $d \geq 5$ 时,

$$
f(x)=a_{d} x^{d}+a_{d-1} x^{d-1}+\cdots+a_{1} x+a_{0}, a_{d} \neq 0,
$$

$f(x)=0$ 有 $d$ 个实根 $r_{1}, r_{2}, \cdots, r_{d}$.

若 $a_{0}=a_{1}=a_{2}=1$, 由韦达定理得,

$$
\begin{aligned}
& r_{1} r_{2} \cdots r_{d}=(-1)^{d} \frac{a_{0}}{a_{d}}=(-1)^{d} \frac{1}{a_{d}} \\
& r_{1} r_{2} \cdots r_{d} \sum_{i=1}^{d} \frac{1}{r_{i}}=(-1)^{d-1} \frac{a_{1}}{a_{d}}=(-1)^{d-1} \frac{1}{a_{d}}, \\
& r_{1} r_{2} \cdots r_{d} \sum_{1 \leq i<j \leq d} \frac{1}{r_{i} r_{j}}=(-1)^{d-2} \frac{a_{2}}{a_{d}}=(-1)^{d-2} \frac{1}{a_{d}},
\end{aligned}
$$

所以 $\sum_{i=1}^{d} \frac{1}{r_{i}}=-1, \sum_{1 \leq i<j \leq d} \frac{1}{r_{i} r_{j}}=1$, 从而

$$
\sum_{i=1}^{d} \frac{1}{r_{i}^{2}}=\left(\sum_{i=1}^{d} \frac{1}{r_{i}}\right)^{2}-2 \sum_{1 \leq i<j \leq d} \frac{1}{r_{i} r_{j}}=-1
$$

矛盾！

所以 $a_{0}, a_{1}, a_{2}$ 必有一个不为 1 , 可得 $a_{d}=a_{d-1}=a_{d-2}=1(d \geq 5)$.

类似地, 由韦达定理得

$$
\sum_{i=1}^{d} r_{i}=-1, \sum_{1 \leq i<j \leq d} r_{i} r_{j}=1
$$

所以 $\sum_{i=1}^{d} r_{i}^{2}=-1$, 矛盾!

评注 法一关键的一步是将原多项式乘以 $(x-1)$, 新多项式非零系数少, 从而非零实根不多. 这里利用不同实根之间一定有导函数的根及 $d$ 重根求导变为 $d-1$ 重可对导函数的根给出很好的判断. 法二 $f(x)=0$ 的根都是实根, 利用韦达定理, 从两头系数均为 1 分析, 可得矛盾.

题 3 如图所示, 在三角形 $A B C$ 中, 圆 $\Gamma$ 与边 $B C$ 相切于点 $X$, 与边 $A C$ 相切于点 $Y . P$ 为边 $A B$ 上一点, 直线 $X P 、 Y P$ 分别与圆 $\Gamma$ 再次交于点 $K 、 L$, 直线 $A K 、 B L$ 分别与圆 $\Gamma$ 再次交于点 $R 、 S$. 求证: 直线 $X R 、 Y S 、 A B$ 相交于同一点.

证明 对圆内接六边形 $Y Y X K R L$ 使用 Pascal 定理知, $A P, X Y, L R$ 三线共点.

对圆内接六边形 $X X Y L S K$ 使用 Pascal 定理知, $B P, X Y, K S$ 三线共点.

所以, $K S, L R, A B$ 三线共点.

对圆内接六边形 $Y L R X K S$ 使用 Pascal 定理知, $S Y$ 与 $X R$ 的交点、 $K S$与 $L R$ 的交点和 $P$ 三点共线.

而点 $P$ 和 $K S$ 与 $L R$ 的交点均在 $A B$ 上, 所以 $X R 、 Y S 、 A B$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_a4b14bcda5e215f219d6g-5.jpg?height=734&width=528&top_left_y=218&top_left_x=770)

评注 本题对熟悉 Pascal 定理的人来说是简单题, 图形结构容易让人联想到 Pascal 定理, 剩下工作不算困难. 可能出现三线平行的情况, 对问题无影响.

题 4 锐角三角形 $A B C$ 中, 点 $D 、 E$ 分别是边 $B C 、 A C$ 上的点, 且使得 $B D 、 C E$ 分别平分 $\angle A B C 、 \angle B C A$. 点 $D$ 在边 $B C 、 B A$ 上的投影分别是 $P 、 Q$, 点 $E$ 在边 $C A 、 C B$ 上的投影分别是 $R 、 S$. 设 $A P$ 与 $C Q$ 交于点 $X, A S$与 $B R$ 交于点 $Y, B X$ 与 $C Y$ 交于点 $Z$, 求证: $A Z \perp B C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_a4b14bcda5e215f219d6g-5.jpg?height=523&width=642&top_left_y=1549&top_left_x=707)

证明 设 $B X$ 交 $A C$ 于 $T$, 由塞瓦定理以及 $B P=B Q, D P=D Q$ 知,

$$
\frac{A T}{T C}=\frac{A Q}{Q B} \cdot \frac{B P}{C P}=\frac{A Q}{C P}=\frac{\tan \angle A D Q}{\tan \angle C D P}=\frac{\tan \angle A C B}{\tan \angle B A C}
$$

所以, $B T \perp A C$, 即 $B Z \perp A C$. 同理可得, $C Z \perp A B$,

所以, 点 $Z$ 是三角形 $A B C$ 的垂心, $A Z \perp B C$.

评注 考虑塞瓦定理是自然的, 经过计算可发现 $Z$ 为垂心.
题 5 正整数 $a, b, c, d$ 满足 $\left\{a \cdot b^{n}+c \cdot d^{n}: n=1,2,3, \cdots\right\}$ 的素因数只有有限个, 求证: $b=d$.

证明 不妨设 $(a, c)=(b, d)=1$. 假设 $\left\{a \cdot b^{n}+c \cdot d^{n}: n=1,2,3, \cdots\right\}$ 的素因数有限且 $b \neq d$, 设这些素因数为 $p_{1}, p_{2}, \cdots p_{k}$, 则对每个正整数 $n$,

$$
a \cdot b^{n}+c \cdot d^{n}=p_{1}^{\alpha_{1, n}} p_{2}^{\alpha_{2, n}} \cdots p_{k}^{\alpha_{k, n}}
$$

当 $m-n \in\{1,2, \cdots, k\}$ 时,

$$
\left(a \cdot b^{n}+c \cdot d^{n}, a \cdot b^{m}+c \cdot d^{m}\right) \mid a \cdot b^{m}+c \cdot d^{m}-\left(a \cdot b^{n}+c \cdot d^{n}\right) b^{m-n},
$$

即

$$
\left(a \cdot b^{n}+c \cdot d^{n}, a \cdot b^{m}+c \cdot d^{m}\right) \mid c d^{n}\left(b^{m-n}-d^{m-n}\right),
$$

类似地

$$
\left(a \cdot b^{m}+c \cdot d^{m}, a \cdot b^{n}+c \cdot d^{n}\right) \mid a b^{n}\left(b^{m-n}-d^{m-n}\right) .
$$

所以,

$$
\begin{aligned}
& \left(a \cdot b^{m}+c \cdot d^{m}, a \cdot b^{n}+c \cdot d^{n}\right) \mid\left(a b^{n}\left(b^{m-n}-d^{m-n}\right), c d^{n}\left(b^{m-n}-d^{m-n}\right)\right), \\
& \left(a \cdot b^{m}+c \cdot d^{m}, \quad a \cdot b^{n}+c \cdot d^{n}\right) \mid\left(b^{m-n}-d^{m-n}\right) \cdot\left(a b^{n}, c d^{n}\right) .
\end{aligned}
$$

又 $\left(a b^{n}, c d^{n}\right) \mid\left(a, c d^{n}\right) \cdot\left(b^{n}, c d^{n}\right)$ 及 $(a, c)=(b, d)=1$, 知 $\left(a b^{n}, c d^{n}\right) \mid a c$,

所以,

$$
\left(a \cdot b^{m}+c \cdot d^{m}, a \cdot b^{n}+c \cdot d^{n}\right) \leq a c\left|b^{m-n}-d^{m-n}\right| \leq a c\left|b^{k}-d^{k}\right| .
$$

而当 $n$ 充分大后, $p_{1}^{\alpha_{1, n}}, p_{2}^{\alpha_{2, n}}, \cdots, p_{k}^{\alpha_{k, n}}$ 中必有一个大于 $a c\left|b^{k}-d^{k}\right|$, 将其记为 $g_{n}$.

又 $g_{n}, g_{n+1}, \cdots, g_{n+k}$ 中必有两个是同一个素数的幂, 所以存在 $n \leq i<$ $j \leq n+k$, 使得

$$
\left(g_{i}, g_{j}\right)>a c\left|b^{k}-d^{k}\right|
$$

从而

$$
\left(a \cdot b^{i}+c \cdot d^{i}, a \cdot b^{j}+c \cdot d^{j}\right)>a c\left|b^{k}-d^{k}\right|,
$$

矛盾! 故 $b=d$.

评注 素因子有限的一些数在充分大后都会有很大的素数幂, 进而分析连续若干项的最大公因数即可, 结合不等式可得矛盾, 数论感觉好的人, 做起来容易些.
题 6 某校有 2021 位同学, 其中每一个同学恰有 $k$ 个朋友 (朋友关系是相互的), 已知不存在三位同学, 使得他们两两之间互为朋友关系, 求 $k$ 的最大值.

解 $k$ 的最大值是 808 .

先给出构造: 将所有的同学划分为 5 个集合 $A_{1}, A_{2}, A_{3}, A_{4}, A_{5}$, 其中

$$
\left|A_{1}\right|=\left|A_{5}\right|=405,\left|A_{2}\right|=\left|A_{4}\right|=404,\left|A_{3}\right|=403
$$

记 $A_{1}=\left\{a_{1}, a_{2}, \cdots, a_{405}\right\}, A_{5}=\left\{b_{1}, b_{2}, \cdots, b_{405}\right\}$.

所有的朋友对恰为

$$
\begin{aligned}
& \left\{(x, y) \mid x \in A_{i}, y \in A_{i+1}, i=1,2,3,4\right\} \\
& \cup\left\{(x, y) \mid x \in A_{1}, y \in A_{5}, \text { 且 }\{x, y\} \neq\left\{a_{j}, b_{j}\right\}, j=1,2, \cdots, 405\right\},
\end{aligned}
$$

即对任意 $1 \leq i \leq 4, A_{i}$ 中每一位同学与 $A_{i+1}$ 的所有同学均是朋友, $A_{1}$ 与 $A_{5}$ 之间除 $a_{i}$ 和 $b_{i}(1 \leq i \leq 405)$ 不是朋友外, 其余两两是朋友.

容易验证符合题设要求, 此时 $k=808$.

下证: $k \leq 808$.

构造图 $G(V, E), V$ 为所有同学构成的集合, $E$ 为所有朋友对构成的集合.

对 $v \in V$, 记 $d(v)$ 为 $v$ 的朋友数.

若 $G$ 为二部图, 则两部分点数不同, 从而 $G$ 不可能是 $k-$ 正则图.

故 $G$ 不为二部图, 从而必有奇圈, 设 $L$ 为最短的奇圈, 其顶点构成的集合为 $U$, 由条件, $L$ 的长度 $|L|$ 至少为 5 , 显然在圈 $L$ 上不相邻的点不能连边.

对 $G$ 中点, $u \notin U$, 若 $u$ 与 $L$ 中至少 3 个点连边, 设为 $u v_{1}, u v_{2}, u v_{3} \in E$, 且 $v_{1}, v_{2}, v_{3}$ 在 $L$ 上顺次排列.

考虑如下 3 个圈 :

$$
u \rightarrow v_{1} \xrightarrow{\text { 沿圈 } L} v_{2} \rightarrow u, u \rightarrow v_{2} \xrightarrow{\text { 沿圈 } L} v_{3} \rightarrow u, u \rightarrow v_{3} \xrightarrow{\text { 沿圈 } L} v_{1} \rightarrow u,
$$

其长度之和为 $|L|+6$. 由于 $|L|$ 是奇数, 故这三个圈中必有一个为奇圈.

而除该奇圈外的两圈长度之和 $\geq 4+4=8$, 所以该奇圈的长度 $\leq|L|-2$,与 $L$ 的最短性矛盾.

故 $u$ 至多与 $L$ 中两点连边.

于是,

$$
\begin{aligned}
k|L| & =\sum_{v \in U} d(v)=2|L|+\sum_{u \notin U}(L \text { 中与 } u \text { 连边的点的个数 }) \\
& \leq 2|L|+2(2021-|L|) \\
& =4042 .
\end{aligned}
$$

所以,

$$
k \leq \frac{4042}{|L|} \leq \frac{4042}{5} \Rightarrow k \leq 808
$$

评注 取最短的奇圈及相关分析是图论中的常见手法, 构造是基于 5 个“大点”的一个圈, 再进行调整, 两部分均有一定的难度, 猜到答案对后面的解答很有帮助. 对一般的 $n, n$ 为偶数时结果为 $\frac{n}{2}, n$ 为奇数时结果为 $2\left[\frac{n}{5}\right]$.

