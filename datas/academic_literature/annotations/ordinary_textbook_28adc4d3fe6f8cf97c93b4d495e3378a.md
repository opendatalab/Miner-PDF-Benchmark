# 好题与妙解（七） 

## — 2018 年新星秋季精品班两次测试题解析

冷岗松 罗振华 吴尉迟

2018 年 11 月, 上海数学新星秋季精品班举行了两次测试 (小考). 每次测试四道题, 时间为两个半小时. 这两次测验试题有趣、难度适中, 下面就介绍这些试题及给出相应的解答. 我们将用题 $1 . x$ 表示第 1 次测试的第 $x$ 题, 题 $2 . y$ 的意义类似.

## I. 试 题

题 1.1 点 $E, F$ 分别是 $\triangle A B C$ 边 $A B, A C$ 上的点. $\triangle A E F$ 的外接圆交 $\triangle A B C$ 的外接圆于点 $M$. 点 $D$ 是点 $M$ 关于直线 $E F$ 的对称点, 点 $O$ 是 $\triangle A B C$的外心. 证明: 点 $D$ 在线段 $B C$ 上当且仅当 $O, A, E, F$ 四点共圆.

题 1.2 设 $n$ 是正整数, $c$ 是正实数. 已知实数 $x_{1}, x_{2}, \cdots, x_{2 n}$ 满足 $x_{1}+x_{2}+$ $\cdots+x_{2 n}=c$ 且 $\left|x_{k+1}-x_{k}\right|<\frac{c}{n}, \forall 1 \leq k \leq 2 n\left(x_{2 n+1}=x_{1}\right)$. 证明: 存在 $n$ 个整数 $i_{1}, i_{2}, \cdots, i_{n}$, 使得:

$$
\left|x_{i_{1}}+\cdots+x_{i_{n}}-\frac{c}{2}\right|<\frac{c}{2 n}
$$

题 1.3 有 $n$ 个人两两打一局乒乓球, 如果有 4 个人 $A, B, C, D$ 满足 $A$ 胜 $B$, $B$ 胜 $C, C$ 胜 $D, D$ 胜 $A$, 则称此四人为一个 “四边联”, 问：至多有多少个 “四边联”?

题 1.4 已知 $\left\{a_{n}\right\}_{n \geq 1}$ 是正整数序列, $\left\{p_{n}\right\}_{n \geq 1}$ 是素数序列, 且对任意正整数 $n$, 有

$$
p_{n} \mid a_{n}, a_{n+1}=\frac{a_{n}}{p_{n}}\left(p_{n}^{1009}-1\right) .
$$

证明: 存在正整数 $m$, 使得 $2018 \mid a_{m}$.[^0]题 2.1 在不等边三角形 $A B C$ 中, $G, H$ 分别为它的重心和垂心. 记 $w_{1}$ 为过点 $A, B$ 且与直线 $B C$ 相切的圆, $\omega_{2}$ 为过点 $A, C$ 且与直线 $B C$ 相切的圆. $\omega_{1}, \omega_{2}$两圆交于点 $A, P_{A}$. 类似定义 $P_{B}, P_{C}$. 求证: $G, H, P_{A}, P_{B}, P_{C}$ 五点共圆.

题 $2.2\left\{a_{i}\right\}_{i \geq 1}$ 是不增的非负整数数列, 其最小值为 0 . 对于整数 $j$, 记 $b_{j}$ 为满足 $a_{i} \geq j$ 的下标 $i$ 的个数. 证明: 可重集 $\left\{a_{1}+1, a_{2}+2, \cdots, a_{i}+i, \cdots\right\}$ 与 $\left\{b_{1}+1, b_{2}+2, \cdots, b_{j}+j, \cdots\right\}$ 相等.

题 2.3 设 $n$ 是一个正整数, 以 $\{1,2 \cdots, 2 n\}$ 的所有 $n$ 元子集为顶点的无向图满足: 若 $n$ 元子集 $A, B$ 满足 $B=\{1,2 \cdots, 2 n\} \backslash A$ 或 $B=\{2 n+1-i: i \in A\}$,则 $A, B$ 有边相连. 求这个无向图的连通分支个数.

题 2.4 称一个正整数序列 $\left\{a_{n}\right\}_{n \geq 1}$ 是斐波那契型数列, 若其满足递推关系: $a_{n+2}=a_{n+1}+a_{n}, \forall n \geq 1$. 问: 是否能把正整数集分划成无穷多个斐波那契型数列? 说明理由.

## II. 解 答

题 1.1 点 $E, F$ 分别是 $\triangle A B C$ 边 $A B, A C$ 上的点. $\triangle A E F$ 的外接圆交 $\triangle A B C$ 的外接圆于点 $M$. 点 $D$ 是点 $M$ 关于直线 $E F$ 的对称点, 点 $O$ 是 $\triangle A B C$的外心. 证明: 点 $D$ 在线段 $B C$ 上当且仅当 $O, A, E, F$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_3447bd95d34d1d350ccag-02.jpg?height=505&width=740&top_left_y=1575&top_left_x=658)

证明 不妨设 $M$ 在劣弧 $\overparen{A B}$ 上. 则我们有

$$
\angle A E F=\angle A M F<\angle A M C=\angle A B C,
$$

因此线 $E F$ 交线 $B C$ 于一点 $G$, 使得 $B$ 在 $C, G$ 之间. 在完全四边形 $A F C B G E$中, $\triangle A B C$ 的外接圆与 $\triangle A E F$ 的外接圆交于 $M$ 点, 则 $M$ 是这个完全四边形的密克点, 从而 $M, G, B, E$ 和 $M, F, C, G$ 分别四点共圆. 从而

$$
D \in B C \Leftrightarrow \angle M G E=\angle C G E
$$

$$
\begin{aligned}
& \Leftrightarrow \angle A E M=2 \angle A B M=\angle A O M \\
& \Leftrightarrow O, A, E, F \text { 四点共圆. }
\end{aligned}
$$

评注 这是一道简单的几何题, 把直线 $F E$ 和 $C B$ 延长后交出一个完全四边形, 可以发现 $M$ 是这个完全四边形的密克点, 再利用密克点的几何性质能找到另外两组四点共圆, 最后通过导角就可以证得结论.

题 1.2 设 $n$ 是正整数, $c$ 是正实数. 已知实数 $x_{1}, x_{2}, \cdots, x_{2 n}$ 满足 $x_{1}+x_{2}+$ $\cdots+x_{2 n}=c$ 且 $\left|x_{k+1}-x_{k}\right|<\frac{c}{n}, \forall 1 \leq k \leq 2 n\left(x_{2 n+1}=x_{1}\right)$. 证明: 存在 $n$ 个整数 $i_{1}, i_{2}, \cdots, i_{n}$, 使得:

$$
\left|x_{i_{1}}+\cdots+x_{i_{n}}-\frac{c}{2}\right|<\frac{c}{2 n} .
$$

证明 令 $a_{i}=\max \left\{x_{2 i-1}, x_{2 i}\right\}, b_{i}=\min \left\{x_{2 i-1}, x_{2 i}\right\}, 1 \leq i \leq n$.

记 $S_{k}=a_{1}+a_{2}+\cdots+a_{n-k}+b_{n-k+1}+\cdots+b_{n}, 0 \leq k \leq n$. 其中, $S_{0}=$ $a_{1}+a_{2}+\cdots+a_{n}$. 故有

$$
S_{0} \geq \frac{c}{2} \geq S_{n}
$$

又注意到对任意 $0 \leq k \leq n-1$, 有

$$
S_{k}-S_{k+1}<\frac{c}{n}
$$

故由离散介值定理知, 存在 $0 \leq m \leq n$, 使得

$$
\left|S_{m}-\frac{c}{2}\right|<\frac{c}{2 n} .
$$

事实上, 若不存在. 则由 $S_{0} \geq \frac{c}{2} \geq S_{n}$ 知

$$
S_{0} \geq \frac{c}{2}+\frac{c}{2 n}, S_{n} \leq \frac{c}{2}-\frac{c}{2 n} .
$$

从而必存在最小的下标 $k$, 使得

$$
S_{k} \geq \frac{c}{2}+\frac{c}{2 n}>\frac{c}{2}-\frac{c}{2 n} \geq S_{k+1}
$$

则 $S_{k}-S_{k+1} \geq \frac{c}{n}$, 这与前面导出的 $S_{k}$ 的性质矛盾.

从而命题得证.

评注 这是一道题面新颖、难度适中的不等式问题. 上述解法的关键在于利用题设条件找出若干个 $n$ 元数组, 使得相邻两个数组的所有数之和具有介值性,再由离散介值定理就可以证得结论。
题 1.3 有 $n$ 个人两两打一局乒乓球, 如果有 4 个人 $A, B, C, D$ 满足 $A$ 胜 $B, B$ 胜 $C, C$ 胜 $D, D$ 胜 $A$, 则称此四人为一个 “四边联”, 问：至多有多少个 “四边联”?

解 将 $n$ 个人看作 $n$ 阶有向图上的点, 若 $A$ 胜 $B$, 则连边 $A \rightarrow B$.

首先, 注意到以下三个小结论:

(1) 四点中至多存在一个长度为 4 的有向圈.

(2) 四点中若有一个点的出度或者入度为 3 , 则此四点不构成四边联, 反之亦然.

(3) 四点中最多有两点的出度或者入度为 3.

称平面上四点 $A, B, C, D$ 构成一个坏组 $(A, B C D)$ 若 $A \rightarrow B, A \rightarrow C, A \rightarrow$ $C, A \rightarrow D$ 或 $A \leftarrow B, A \leftarrow C, A \leftarrow D$. 于是, 若四点中有坏组, 则它们不构成四边联, 且一个四点组中至多出现两个坏组, 不同的四点组出现的坏组一定不同.

设每个点的出度为 $a_{1}, a_{2}, \cdots, a_{n}$, 则坏组的个数为

$$
\sum_{i=1}^{n}\left(\left(\begin{array}{c}
a_{i} \\
3
\end{array}\right)+\left(\begin{array}{c}
n-1-a_{i} \\
3
\end{array}\right)\right)
$$

(1) 当 $n$ 为奇数时, 设 $n=2 k+1, k \in \mathbb{N}^{*}$, 则坏组的个数

$$
\sum_{i=1}^{n}\left(\left(\begin{array}{c}
a_{i} \\
3
\end{array}\right)+\left(\begin{array}{c}
n-1-a_{i} \\
3
\end{array}\right)\right) \geq(2 k+1) \cdot 2\left(\begin{array}{l}
k \\
3
\end{array}\right)
$$

故不是四边联的四点组的个数大于等于 $(2 k+1)\left(\begin{array}{l}k \\ 3\end{array}\right)$, 所以四边联的个数小于等于

$$
\left(\begin{array}{c}
2 k+1 \\
4
\end{array}\right)-(2 k+1)\left(\begin{array}{l}
k \\
3
\end{array}\right)=\frac{k(k-1)(k+1)(2 k+1)}{6} .
$$

(2) 当 $n$ 为偶数时, 设 $n=2 k, k \in \mathbb{N}^{*}$, 则坏组的个数

$$
\sum_{i=1}^{n}\left(\left(\begin{array}{c}
a_{1} \\
3
\end{array}\right)+\left(\begin{array}{c}
n-1-a_{i} \\
3
\end{array}\right)\right) \geq 2 k\left(\left(\begin{array}{c}
k-1 \\
3
\end{array}\right)+\left(\begin{array}{l}
k \\
3
\end{array}\right)\right)
$$

故不是四边联的四点组的个数大于等于 $k\left(\left(\begin{array}{c}k-1 \\ 3\end{array}\right)+\left(\begin{array}{l}k \\ 3\end{array}\right)\right)$, 所以四边联的个数小于等于

$$
\left(\begin{array}{c}
2 k+1 \\
4
\end{array}\right)-k\left(\left(\begin{array}{c}
k-1 \\
3
\end{array}\right)+\left(\begin{array}{l}
k \\
3
\end{array}\right)\right)=\frac{k(k-1)(k+1)(2 k-3)}{6} .
$$

下面证明等号均可以取到.

(1)当 $n$ 为奇数时, 由上述讨论知, 只须使每点出入度均为 $k$, 且每个非四边联的四点组都有两个坏组. 将 $2 k+1$ 个点顺时针编号 $0,1, \cdots, 2 k$, 并令 $A \rightarrow B$, 当 $(B-A) \bmod n \in\{1,2, \cdots, k\}$ 时; 令 $A \leftarrow B$, 当 $(B-A) \bmod n \in$ $\{k+1, k+2, \cdots, 2 k\}$ 时. 则不难验证每个点的出入度均为 $k$. 对于每个非四
边联的四点组, 设 $A \rightarrow B, A \rightarrow C, A \rightarrow D$, 且 $B, C, D$ 顺时针依次排列, 则必有 $B \rightarrow C, B \rightarrow D, C \rightarrow D$, 故有两个坏组 $(A, B C D)$ 和 $(D, A B C)$,于是等号可以取到.

(2) 当 $n$ 为偶数时, 只须使每点出度为 $k$ 入度为 $k-1$, 或出度为 $k-1$ 入度为 $k$, 且每个非四边联的四点组都有两个坏组.

将 $2 k$ 个点顺时针编号 $0,1, \cdots, 2 k-1$, 当 $(B-A) \bmod n \in\{1,2, \cdots, k-1\}$时, 令 $A \rightarrow B$; 当 $(B-A) \bmod n \in\{k+1, k+2, \cdots, 2 k-1\}$ 时, 令 $A \leftarrow B$;当 $(B-A) \equiv k(\bmod n)$ 时, $A \rightarrow B$ 或 $A \leftarrow B$ 任选一种方向. 则不难验证每点出度为 $k$ 入度为 $k-1$, 或出度为 $k-1$ 入度为 $k$.

对于每个非四边联的四点组, 若它们中无两点之差模 $n$ 余 $k$, 则同 (1) 的讨论可证. 若有两点 $A, B$ 满足差模 $n$ 余 $k$, 且 $A \rightarrow B$.

(a) 若顺时针依次为 $A, C, D, B$, 则 $A \rightarrow C, A \rightarrow D, C \rightarrow D, C \rightarrow B, D \rightarrow$ $B$, 有坏组 $(A, B C D),(D, A B C)$, 成立.

(b) 若顺时针依次为 $A, C, B, D$, 则 $A \rightarrow C, C \rightarrow B, B \rightarrow D, D \rightarrow A$ 为四边联, 矛盾.

(c) 若顺时针依次为 $A, B, C, D$, 则 $A \rightarrow B, B \rightarrow C, C \rightarrow D, D \rightarrow A$ 为四边联, 矛盾. 于是等号也可以取到.

综上可知, $n=2 k+1$ 时, 四边联个数最大值为 $\frac{k(k-1)(k+1)(2 k+1)}{6} ; n=2 k$ 时,四边联个数最大值为 $\frac{k(k-1)(k+1)(2 k-3)}{6}$.

评注 此题由郑州一中张甲老师提供, 这是一道中等难度的图论问题. 本题的来源是完全有向图中 3 阶循环圈个数的最大值问题, 原问题是通过计算从一点出发的同向边组成的对和使用柯西不等式进行上界的估计, 本题中循环圈的阶数由 3 变为了 4 , 不过论证所用的手法与 3 阶的情形本质相同, 只是构造部分需要更仔细的分类和说明.

题 1.4 已知 $\left\{a_{n}\right\}_{n \geq 1}$ 是正整数序列, $\left\{p_{n}\right\}_{n \geq 1}$ 是素数序列, 且对任意正整数 $n$, 有

$$
p_{n} \mid a_{n}, a_{n+1}=\frac{a_{n}}{p_{n}}\left(p_{n}^{1009}-1\right) .
$$

证明: 存在正整数 $m$, 使得 $2018 \mid a_{m}$.

证明 令 $e=1009$, 则 $e$ 是素数且 $2 e=2018$. 注意到

$$
p_{n}^{e}-1=\left(p_{n}-1\right)\left(p_{n}^{e-1}+\cdots+p_{n}+1\right),
$$

且 当 $p_{n} \neq 2$ 时, 有 $2 \mid p_{n}-1$, 故要证明原命题, 只需证存在正整数 $m$, 使得 $p_{m} \equiv 1(\bmod e)$.

反证法. 假设 $p_{n} \not \equiv 1(\bmod e), \forall n \geq 1$. 我们证明 $A_{n}=p_{n}^{e-1}+\cdots+p_{n}+1$ 的所有素因子都模 $e$ 余 1 .

令 $p$ 是 $A_{n}$ 的素因子, 则 $p \neq p_{n}$. 记 $d \geq 1$ 是 $p_{n}$ 模 $p$ 的阶, 即 $d$ 是最小的正整数使得 $p_{n}^{d} \equiv 1(\bmod p)$. 由于 $p\left|A_{n}, A_{n}\right| p_{n}^{e}-1$, 则 $p \mid p_{n}^{e}-1$, 故 $d \mid e$. 又 $e$是素数, 则 $d=1$ 或 $d=e$.

若 $d=1$, 则 $p_{n} \equiv p_{n}^{1} \equiv 1(\bmod p)$, 从而

$$
A_{n} \equiv 1^{e-1}+\cdots+1 \equiv e \quad(\bmod p)
$$

由于 $p \mid A_{n}$, 故 $p \mid e$, 从而 $p=e$. 这与 $p_{n} \not \equiv 1(\bmod e)$ 矛盾. (1) 得证.

若 $d=e$, 由Fermat 小定理知 $d \mid p-1$. 由 $p$ 的任意性知, $A_{n}$ 的所有素因子都模 $e$ 余 1 .

现在令 $b_{n}$ 表示 $a_{n}$ 最大的因子, 使得 $b_{n}$ 不存在模 $e$ 余 1 的素因子. 从而有

$$
b_{n+1} \left\lvert\, \frac{b_{n}}{p_{n}}\left(p_{n}-1\right)<b_{n}\right.
$$

这说明 $\left\{b_{n}\right\}$ 是严格递减的无穷正整数列, 矛盾!

于是 $(*)$ 成立, 从而命题得证.

评注 这是一道有一定难度的与数列相关的数论问题. 上述解法的关键在于发现 $A_{n}$ 在 $p_{n} \not \equiv 1(\bmod e)$ 时所有素因子都模 $e$ 余 1 , 结合反证法可以发现 $\left\{b_{n}\right\}$是严格递减的无穷正整数列, 这就产生了矛盾, 从而命题得证.

题 2.1 在不等边三角形 $A B C$ 中, $G, H$ 分别为它的重心和垂心. 记 $w_{1}$ 为过点 $A, B$ 且与直线 $B C$ 相切的圆, $\omega_{2}$ 为过点 $A, C$ 且与直线 $B C$ 相切的圆. $\omega_{1}, \omega_{2}$两圆交于点 $A, P_{A}$. 类似定义 $P_{B}, P_{C}$. 求证: $G, H, P_{A}, P_{B}, P_{C}$ 五点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_3447bd95d34d1d350ccag-06.jpg?height=600&width=893&top_left_y=2033&top_left_x=590)
证明 延长 $A P_{A}$ 交 $B C$ 于 $D$.

注意到直线 $A P_{A}$ 是圆 $\omega_{1}$ 与圆 $\omega_{2}$ 的根轴, 从而 $D$ 到两圆的幂相等, 则有 $D B^{2}=D C^{2}$, 故 $D B=D C$. 又 $G$ 也在三角形 $A B C$ 的中线 $A D$ 上, 所以 $A, P_{A}, G, D$ 四点共线.

由 $\omega_{1}$ 与 $B C$ 相切知 $\angle P_{A} B D=\angle B A D$, 故 $\triangle P_{A} B D \sim \triangle B A D$. 则 $\angle B P_{A} D=$ $\angle A B C$. 同理, $\angle C P_{A} D=\angle A C B$. 故

$$
\angle B P_{A} C=\angle B P_{A} D+\angle C P_{A} D=\angle A B C+\angle A C B=180^{\circ}-\angle B A C .
$$

由垂心性质可知 $\angle B H C=180^{\circ}-\angle B A C$. 所以 $B, H, P_{A}, C$ 四点共圆, 从而 $\angle H P_{A} B=\angle H C B$. 故

$$
\begin{aligned}
\angle G P_{A} H & =\angle G P_{A} B+\angle H P_{A} B=\angle B P_{A} D+\angle H C B \\
& =\angle A B C+\angle H C B=90^{\circ} .
\end{aligned}
$$

这说明 $P_{A}$ 在 $G H$ 为直径的圆上. 同理, $P_{B}, P_{C}$ 也在 $G H$ 为直径的圆上.

所以 $G, H, P_{A}, P_{B}, P_{C}$ 五点共圆.

评注 这是一道中等难度的几何题. 解答的关键在于发现 $G H$ 是要证的五点所在圆的直径, 先用根轴可以导出 $A P_{A}$ 是中线, 再通过相似和四点共圆进行导角可以证明 $G P_{A}$ 与 $H P_{A}$ 垂直, 从而命题获证.

题 $2.2\left\{a_{i}\right\}_{i \geq 1}$ 是不增的非负整数数列, 其最小值为 0 . 对于整数 $j$, 记 $b_{j}$为满足 $a_{i} \geq j$ 的下标 $i$ 的个数. 证明: 可重集 $\left\{a_{1}+1, a_{2}+2, \cdots, a_{i}+i, \cdots\right\}$ 与 $\left\{b_{1}+1, b_{2}+2, \cdots, b_{j}+j, \cdots\right\}$ 相等.

证明 设 $a_{1}=n$. 由题设可知该数列从某一项开始之后均为 0 . 设数列有 $k_{i}$项为 $i(1 \leq i \leq n)$. 则

$$
b_{j}=\left\{\begin{array}{ll}
k_{j}+k_{j+1}+\cdots+k_{n}, & j \leq n \\
0, & j>n
\end{array},\right.
$$

则可重集 $\left\{a_{1}+1, a_{2}+2, \cdots, a_{i}+i, \cdots\right\}$ 为

$$
\begin{aligned}
& \{\underbrace{n+1, k_{n}}_{k_{n} \text { 项连续整数 }}, \underbrace{n+k_{n}, \cdots, n+k_{n-1}-1}_{k_{n-1} \text { 项连续整数 }}, \cdots \\
& \underbrace{i+1+k_{n}+\cdots, i+k_{n}+\cdots+k_{i}}_{k_{i} \text { 项连续整数 }}, \\
& \underbrace{k_{n}+\cdots+k_{1}+2, \cdots}_{\text {此项之后为连续整数 }}\} .
\end{aligned}
$$

其中若某个 $k_{i}=0$, 则上述集合中第 $n+1-i$ 段不出现连续整数.

$$
\begin{aligned}
& \left\{b_{1}+1, b_{2}+2, \cdots, b_{j}+j, \cdots\right\} \text { 为 } \\
& \quad\{k_{n}+\cdots+k_{1}+1, k_{n}+\cdots+k_{2}+2, \cdots, k_{n}+n, \underbrace{n+1, n}_{\text {此项之后是连续整数 }}\} .
\end{aligned}
$$

其中若某个 $k_{i}=0$, 则上述集合中数 $k_{n}+\cdots+k_{i}+i$ 不出现.

上述两个可重集的元素都是从 $n+1$ 开始的连续正整数, 每个元素出现 1 次或 2 次, 且出现 2 次的元素恰为 $i+k_{n}+\cdots+k_{i}\left(k_{i}>0\right)$ 这样的数. 故两个可重集相等.

评注 这是一道有趣的集合问题. 为了刻画题设中数列的结构, 很自然能想到用 $k_{i}$ 表示数 $i$ 在数列中出现的次数, 这样就可以用 $k_{i}$ 来表示 $b_{j}$, 从而题设中的两个可重集都可以用 $k_{i}$ 显式写出, 比较两个集合中每个元素出现的次数就可以证得结论.

题 2.3 设 $n$ 是一个正整数, 以 $\{1,2 \cdots, 2 n\}$ 的所有 $n$ 元子集为顶点的无向图满足: 若 $n$ 元子集 $A, B$ 满足 $B=\{1,2 \cdots, 2 n\} \backslash A$ 或 $B=\{2 n+1-i: i \in A\}$,则 $A, B$ 有边相连. 求这个无向图的连通分支个数.

## 解 (湖南雅礼中学王俊炎)

易知无向图中每个顶点的度数不超过 2.

对于 $\{1,2, \cdots, n\}$ 的子集 $A, B$, 我们用 $A \equiv B$ 表示 $B=\{1,2, \cdots, 2 n\} \backslash A$,用 $A \sim B$ 表示 $B=\{2 n+1-i \mid i \in A\}$.

对于 $\{1,2, \cdots, 2 n\}$ 的子集 $A, B, C$, 考虑下面两种情况:

(1) 若 $A \equiv C, A \sim B$, 且 $B \neq C$.

考虑满足 $B \equiv D$ 的集合 $D$.

若 $D=A$, 则

$$
D=\{1,2, \cdots, 2 n\} \backslash B=\{2 n+1-i \mid i \in B\}=A,
$$

从而

$$
\begin{aligned}
B & =\{1,2, \cdots, 2 n\} \backslash(\{1,2, \cdots, 2 n\} \backslash B) \\
& =\{1,2, \cdots, 2 n\} \backslash\{2 n+1-i \mid i \in B\} \\
& =\{2 n+1-i \mid i \in A\} \\
& =C,
\end{aligned}
$$

矛盾. 故 $D \neq A$.
下面证明 $D \sim C$.

若 $x \in D$, 则 $x \notin B$, 那么 $2 n+1-x \notin A, 2 n+1-x \in C$, 同理可得若 $x \in C$则 $2 n+1-x \in D$, 故 $D \sim C$.

由 (*) 知此时 $A, B, C, D$ 构成长为 4 的连通分支, 且充要条件为 $B \neq C$, 即 $A \sim B$ 且 $A \not \equiv B$. 此时必有某个 $i(1 \leq i \leq n)$ 使得 $\{i, 2 n+1-i\} \subseteq A$, 但 $A$ 不能分划成若干个形如 $\{i, 2 n+1-i\}$ 的子集( 否则便有 $A=B$ ).

(2) 若 $A \equiv C, A \sim B$, 且 $B=C$.

此时由 (1) 知, 该分支中只有两个集合, 且 $A$ 要么恰包含 $\{i, 2 n+1-i\}$ 中的一个数 (对所有 $i=1,2, \cdots, n$ ), 要么可以分划成若干个形如 $\{i, 2 n+1-i\}$ 的子集.

下面计算连通分支的个数.

当 $n=2 k$ 时, 共有 $2^{2 k}+\left(\begin{array}{c}2 k \\ k\end{array}\right)$ 个符合 (2) 的子集 $A$, 有 $\left(\begin{array}{c}4 k \\ 2 k\end{array}\right)-2^{2 k}-\left(\begin{array}{c}2 k \\ k\end{array}\right)$ 个符合 (1) 的 $A$, 故共有

$$
\frac{2^{2 k}+\left(\begin{array}{c}
2 k \\
k
\end{array}\right)}{2}+\frac{\left(\begin{array}{c}
4 k \\
2 k
\end{array}\right)-2^{2 k}-\left(\begin{array}{c}
2 k \\
k
\end{array}\right)}{4}=\frac{\left(\begin{array}{c}
4 k \\
2 k
\end{array}\right)+\left(\begin{array}{c}
2 k \\
k
\end{array}\right)+2^{2 k}}{4}
$$

个连通分支.

当 $n=2 k+1$ 时, 共有 $2^{2 k+1}$ 个符合 (2) 的子集 $A$, 有 $\left(\begin{array}{l}4 k+2 \\ 2 k+1\end{array}\right)-2^{2 k+1}$ 个符合 (1) 的 $A$, 故共有

$$
\frac{\left(\begin{array}{c}
4 k+2 \\
2 k+1
\end{array}\right)-2^{2 k+1}}{4}+\frac{2^{2 k+1}}{2}=\frac{\left(\begin{array}{c}
4 k+2 \\
2 k+1
\end{array}\right)+2^{2 k+1}}{4}
$$

个连通分支.

评注 这是一道中等难度的图论题. 问题的关键是发现每个连通分支是长度为 2 或 4 的圈, 再对 $n$ 分奇偶分别计算长度为 2 和长度为 4 的圈的个数, 这样就可以得到所求连通分支的个数.

题 2.4 称一个正整数序列 $\left\{a_{n}\right\}_{n \geq 1}$ 是斐波那契型数列, 若其满足递推关系: $a_{n+2}=a_{n+1}+a_{n}, \forall n \geq 1$. 问: 是否能把正整数集分划成无穷多个斐波那契型数列? 说明理由.

解 先证明如下的 Zerkendorf 定理.

定理 对于斐波那契型数列 $F_{0}=F_{1}=1, F_{n+2}=F_{n+1}+F_{n}, n \in \mathbb{N}$ 以及任意正整数 $n$, 存在 $k$ 及 $1 \leq i_{1}<\cdots<i_{k}$, 满足 $k \geq 1, i_{j+1}-i_{j} \geq 2, j=1,2, \cdots, k-1$,使 $n=F_{i_{1}}+\cdots+F_{i_{k}}$ 且该数列 $\left(i_{1}, \cdots, i_{k}\right)$ 唯一.
定理证明 对 $n$ 归纳证明 $i_{1}, \cdots, i_{k}$ 的存在性.

$n=1$ 时, 只能取 $i_{1}=1 ; n=2$ 时, 只能取 $i_{2}=2$.

假设对小于 $n$ 的正整数结论成立, $n$ 时, 若 $n$ 为斐波那契型数列中的一项 $F_{j}(j \geq 2)$, 取 $i_{1}=j$ 即可.

若 $n$ 不为斐波那契型数列中的一项, 则存在 $j \in \mathbb{N}_{+}$, 使 $F_{j}<n<F_{j+1}$, 则 $1 \leq n-F_{j}<n$.

对 $n-F_{j}$ 使用归纳假设知存在 $1 \leq i_{1}<\cdots<i_{k}$, 使得

$$
i_{j+1}-i_{j} \geq 2, j=1, \cdots, k-1
$$

且

$$
n-F_{j}=F_{i_{1}}+\cdots+F_{i_{k}}
$$

由于 $F_{j-1}+F_{j}=F_{j+1}$, 所以 $F_{i_{k}}<F_{j-1}$, 因此 $i_{k}<j-1$, 即 $i_{k} \leq j-2$, 从而令 $i_{k+1}=j$ 即可, 满足条件.

综上, 存在性得证.

再证唯一性. 若存在 $1 \leq i_{1}<\cdots<i_{k}$ 及 $1 \leq j_{1}<\cdots<j_{l}$ 满足

$$
\begin{gathered}
i_{j+1}-i_{j} \geq 2, j=1, \cdots k-1, \\
j_{r+1}-j_{r} \geq 2, r=1, \cdots l-1,
\end{gathered}
$$

且 $\left(i_{1}, \cdots, i_{k}\right) \neq\left(j_{1}, \cdots, j_{l}\right), n=F_{i_{1}}+\cdots+F_{i_{k}}$. 容易看到

$$
F_{i_{1}}+F_{i_{2}}<F_{i_{2}-1}+F_{i_{2}}=F_{i_{2}+1}
$$

依此类推得

$$
F_{i_{k}} \leq n<F_{i_{k}+1}
$$

同理 $F_{j_{l}} \leq n<F_{j_{l}+1}$. 所以

$$
F_{i_{k}}=F_{j_{l}}
$$

对 $n-F_{i_{k}}=n-F_{j_{l}}$, 同样讨论知 $\left(i_{1}, \cdots, i_{k}\right)=\left(j_{1}, \cdots, j_{l}\right)$ 产生矛盾!

于是唯一性得证, 故定理得证.

回到原题. 由 Zerkendorf 定理, 定义正整数的 “ $F$ 进制”, 即存在

$$
n=a_{k} F_{k}+\cdots+a_{1} F_{1}=\left(a_{k} \cdots a_{1}\right)_{(F)}, k \in \mathbb{N}_{+}
$$

其中 $a_{i} \in\{0,1\}$, 对 $\forall i, a_{i} a_{i+1}=0, i=1, \cdots, k-1, a_{k} \neq 0$.

利用这种表示, 分别依 $a_{1}=1 ; a_{1}=0, a_{2}=1 ; a_{1}=a_{2}=0, a_{3}=1 ; \cdots$ 按
行从小到大列出所有正整数:

$$
\begin{array}{cccccc}
F_{1} & F_{1}+F_{3} & F_{1}+F_{4} & F_{1}+F_{5} & F_{1}+F_{3}+F_{5} & \cdots \\
F_{2} & F_{2}+F_{4} & F_{2}+F_{5} & F_{2}+F_{6} & F_{2}+F_{4}+F_{6} & \cdots \\
F_{3} & F_{3}+F_{4} & F_{3}+F_{6} & F_{3}+F_{7} & F_{3}+F_{5}+F_{7} & \cdots \\
F_{4} & F_{4}+F_{6} & \ldots & \ldots & \ldots & \ldots
\end{array}
$$

上面每一列都是一个斐波那契型数列, 故按列把正整数集分划成了无穷多个斐波那契型数列.

从而命题得证.

评注 这是一道很好的组合数论问题. 它最早在 Kömal 杂志作为征解问题出现, 2017年美国把此题选作了集训队的考试题. 上述解法使用斐波那契数列直接构造正整数集合的分划, 需要用到斐波那契数列的深入性质 (Zerkendorf 定理), 这种做法极具巧思, 值得仔细回味。


[^0]:    收稿日期: 2018-12-15.

