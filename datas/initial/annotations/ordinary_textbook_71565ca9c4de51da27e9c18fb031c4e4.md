数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 第 6 届人大附中数学竞赛加试试题解析 

李天勤 王衔邦 王秉润<br>(中国人民大学附属中学, 100080)

2023 年第 6 届人大附中数学奥林匹克竞赛 (RMO) 于 2023 年 12 月 30 日进行, 比赛形式与全国高中数学联合竞赛相同. 本文介绍加试试题及解答, 第一、二题由李天勤提供, 第三题由王衔邦提供, 第四题由王秉润提供.

## I. 试 题

一、如图, 等腰梯形 $A B C D$ 内接于 $\odot O$. 过 $B$ 作 $B D$ 的垂线与直线 $D A$ 交于点 $P$. 直线 $D O$ 与直线 $B C$ 交于点 $Q$, 直线 $P Q$ 与直线 $A C$ 交于点 $R$. 设平面上的点 $S$ 满足 $C$ 是线段 $S Q$ 的中点, 直线 $D S$ 与 $\odot O$ 交于异于 $D$ 的点 $M$. 证明: $\angle R M O=90^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_f7eda959735ded4c359eg-01.jpg?height=537&width=865&top_left_y=1576&top_left_x=593)

二、设正实数 $a_{1}, a_{2}, \cdots, a_{2023}$ 满足 $a_{1} a_{2} \cdots a_{2023}=1$. 记

$$
T=\left\{(i, j, k): 1 \leq i<j<k \leq 2023, a_{i}+a_{j}+a_{k}<3\right\} .
$$

求 $|T|$ 的最大可能值.

三、设 $n$ 是正整数. 在一个由 $n^{2}$ 个边长为 1 的小正方形构成的 $n \times n$ 正方形网格中, 有 $n$ 块奶酪放置在 $n$ 个不同的格点上. 一只老鼠从左上角出发, 它

修订日期: 2024-01-09.
只能沿着网格线行走. 设 $f(n)$ 为最小的正整数, 满足无论 $n$ 块奶酪如何放置,老鼠都可以选择一条总长度不超过 $f(n)$ 的路径, 使得这条路径可以经过所有奶酪. 证明: 对任意正实数 $\varepsilon$, 存在正实数 $N$, 满足对任意正整数 $n>N$, 均有

$$
(\sqrt{2}-\varepsilon) n^{1.5} \leq f(n) \leq(\sqrt{3}+\varepsilon) n^{1.5} .
$$

四、设 $m$ 是不小于 3 的正奇数. 证明: 存在正整数 $x$ 及正整数 $a, b$, 使得在 $a+1, a+2, \cdots, a+b$ 这 $b$ 个正整数中, 恰有 20232024 个数 $y$ 同时满足 $y \equiv-1$ $(\bmod m)$ 且 $y^{2} \equiv 1(\bmod x)$; 恰有 2023 个数 $z$ 同时满足 $z \equiv 1(\bmod m)$ 且 $z^{2} \equiv 1(\bmod x)$.

## II. 解答与评注

一、如图, 等腰梯形 $A B C D$ 内接于 $\odot O$. 过 $B$ 作 $B D$ 的垂线与直线 $D A$ 交于点 $P$. 直线 $D O$ 与直线 $B C$ 交于点 $Q$, 直线 $P Q$ 与直线 $A C$ 交于点 $R$. 设平面上的点 $S$ 满足 $C$ 是线段 $S Q$ 的中点, 直线 $D S$ 与 $\odot O$ 交于异于 $D$ 的点 $M$. 证明: $\angle R M O=90^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_f7eda959735ded4c359eg-02.jpg?height=522&width=843&top_left_y=1395&top_left_x=618)

证明 1 一方面, 注意到

$$
\angle A P B=180^{\circ}-\angle P B Q=180^{\circ}-90^{\circ}-\angle C B D=\angle O D C \text {, }
$$

且 $\angle P A B=\angle D C Q$, 所以 $\triangle A B P \sim \triangle C Q D$, 于是 $\frac{P A}{A B}=\frac{D C}{C Q}=\frac{A B}{C Q}$.

另一方面, 由于 $\angle M A C=\angle M D C$ 且 $\angle M C A=180^{\circ}-\angle A D M=\angle D S C$,所以 $\triangle A M C \sim \triangle D C S$, 于是 $\frac{A M}{M C}=\frac{D C}{C S}$.

给合两方面知

$$
\left(\frac{A M}{M C}\right)^{2}=\left(\frac{D C}{C S}\right)^{2}=\left(\frac{A B}{C Q}\right)^{2}=\frac{P A}{C Q}
$$

过 $M$ 作 $\odot O$ 切线与直线 $A C$ 交于点 $R^{\prime}$, 则 $\triangle M C R^{\prime} \sim \triangle A M R^{\prime}$, 从而

$$
\frac{A R^{\prime}}{R^{\prime} C}=\frac{S_{\triangle A M R^{\prime}}}{S_{\triangle M C R^{\prime}}}=\left(\frac{A M}{M C}\right)^{2}=\frac{P A}{C Q}
$$

进而 $P, Q, R^{\prime}$ 共线. 这表明 $R^{\prime}=R$, 于是直线 $R M$ 与 $\odot O$ 相切, 即 $\angle R M O=90^{\circ}$.证毕!

![](https://cdn.mathpix.com/cropped/2024_02_26_f7eda959735ded4c359eg-03.jpg?height=494&width=786&top_left_y=564&top_left_x=652)

证明 2 设 $D O$ 与 $\odot O$ 交于点 $F$, 由 $D F$ 是 $\odot O$ 的直径知 $P, B, F$ 共线. 对圆内接六边形 $D A C B F F$ 用 Pascal 定理得 $D A \cap B F=P, A C \cap F F, D F \cap B C=Q$共线, 从而 $R F$ 与 $\odot O$ 相切.

由于 $Q C=C S$, 故 $D F, D S ; D C, D A$ 是调和线束, 于是 $A M C F$ 是调和四边形. 由 $R F$ 与 $\odot O$ 相切知 $R M$ 与 $\odot O$ 相切, 即 $\angle R M O=90^{\circ}$. 证毕!

二、设正实数 $a_{1}, a_{2}, \cdots, a_{2023}$ 满足 $a_{1} a_{2} \cdots a_{2023}=1$. 记

$$
T=\left\{(i, j, k): 1 \leq i<j<k \leq 2023, a_{i}+a_{j}+a_{k}<3\right\} .
$$

求 $|T|$ 的最大可能值.

解 1 (叶语行) $|T|$ 的最大值为 $\left(\begin{array}{c}2022 \\ 3\end{array}\right)$.

一方面, 取 $a_{2}=a_{3}=\cdots=a_{2023}=\frac{1}{2}, a_{1}=2^{2022}$, 则容易知道

$$
T=\{(i, j, k): 2 \leq i<j<k \leq 2023\}
$$

于是 $|T|=\left(\begin{array}{c}2022 \\ 3\end{array}\right)$.

另一方面, 记

$$
S=\left\{(i, j, k): 1 \leq i<j<k \leq 2023, a_{i}+a_{j}+a_{k} \geq 3\right\}
$$

我们证明 $|S| \geq\left(\begin{array}{c}2022 \\ 2\end{array}\right)$, 从而立即证明原题.

先证明: 若正实数 $x_{1}, x_{2}, \cdots, x_{2022}$ 的和不小于 2022 , 则如下集合的大小不小于 $\left(\begin{array}{c}2021 \\ 2\end{array}\right)$ :

$$
S_{1}=\left\{(i, j, k): 1 \leq i<j<k \leq 2022, a_{i}+a_{j}+a_{k} \geq 3\right\}
$$

事实上, 考察 $x_{1}, x_{2}, \cdots, x_{2022}$ 的 2022 ! 个排列, 对每个排列, 将其每相邻三个分为一组, 共有 $\frac{2022}{3}=674$ 组. 易知这 674 个三元组中至少有一个在 $S_{1}$ 中.而注意到每个三元组恰好被 $674 \cdot 3 ! \cdot 2019 !=: K$ 个排列包含, 故

$$
K \cdot\left|S_{1}\right| \geq 2022 !
$$

立即得到 $\left|S_{1}\right| \geq\left(\begin{array}{c}2021 \\ 2\end{array}\right)$.

回到原题. 不妨设 $a_{1} \geq a_{2} \geq \cdots \geq a_{l} \geq 1>a_{l+1} \geq \cdots \geq a_{2023}$, 其中 $1 \leq l \leq 2023$. 如果 $l \geq 300$, 则对任意 $1 \leq i<j<k \leq l$, 均有 $(i, j, k) \in S$, 故

$$
S \geq\left(\begin{array}{l}
l \\
3
\end{array}\right) \geq\left(\begin{array}{c}
2022 \\
2
\end{array}\right)
$$

如果 $1 \leq l \leq 299$, 我们有 $a_{1}+\cdots+a_{l}+a_{l+2}+\cdots+a_{2023} \geq 2022$, 由已证结论, $S$ 中至少有 $\left(\begin{array}{c}2021 \\ 2\end{array}\right)$ 个三元组不包含 $l+1$. 下证明至少有 2021 个 $S$ 中的三元组包含 $l+1$, 从而

$$
|S| \geq\left(\begin{array}{c}
2021 \\
2
\end{array}\right)+2021=\left(\begin{array}{c}
2022 \\
2
\end{array}\right)
$$

完成证明. 分如下情况讨论:

(1) 若 $l=1$, 则任意 $3 \leq k \leq 2023$ 都有 $(1,2, k) \in S$, 成立;

(2) 若 $2 \leq l \leq 299$ 且 $a_{1}+a_{l+1}+a_{2023} \geq 3$, 则任意包含 $1, l+1$ 的三元组都在 $S$ 中, 成立;

(3) 若 $2 \leq l \leq 299$ 且 $a_{1}+a_{l+1}+a_{2023}<3$. 则我们有

$$
a_{2}+a_{3}+\cdots+a_{l}+a_{l+2}+\cdots+a_{2022} \geq 2020
$$

从而

$$
\begin{aligned}
& a_{1}+a_{l+1}+a_{2024-l} \\
\geq & \frac{\left(a_{1}+\cdots+a_{l}\right)+\left(a_{l+1}+\cdots+a_{2 l}\right)+\left(a_{2024-l}+\cdots+a_{2023}\right)}{l} \\
\geq & \frac{2023-(2023-3 l)}{l}=3,
\end{aligned}
$$

且

$$
\begin{aligned}
& a_{2}+a_{l+2}+a_{2024-l} \\
\geq & \frac{\left(a_{2}+\cdots+a_{l}\right)+\left(a_{l+2}+\cdots+a_{2 l}\right)+\left(a_{2024-l}+\cdots+a_{2022}\right)}{l-1} \\
\geq & \frac{2020-(2023-3 l)}{l-1}=3,
\end{aligned}
$$

进而对任意 $l+3 \leq k \leq 2024-l$ 都有 $(1, l+1, k),(2, l+2, k) \in S$.

综上所述, 至少有 2021 个 $S$ 中的三元组包含 $l+1$, 即证!
解 2 同解法 1 给出构造并定义集合 $S$.

我们对所有满足 $n \equiv 1(\bmod 3)$ 的正整数 $n$ 归纳证明下述结论: 设数列 $f(n)$ 满足 $f(4)=0$, 且对任意正整数 $n \geq 7$,

$$
f(n)=\min \left\{\left(\begin{array}{c}
n-1 \\
2
\end{array}\right), f(n-3)+\left(\begin{array}{c}
\frac{n+2}{3} \\
2
\end{array}\right)\right\} \text {. }
$$

若正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $a_{1} a_{2} a_{3} \cdots a_{n} \geq 1$, 记

$$
S_{n}=\left\{(i, j, k): 1 \leq i<j<k \leq n \text { 且 } a_{i}+a_{j}+a_{k} \geq 3\right\} \text {, }
$$

则 $\left|S_{n}\right| \geq f(n)$.

对 $n$ 归纳. 当 $n=4$ 时, 显然有 $\left|S_{n}\right| \geq 0$ 成立. 假设 $n-3$ 时结论成立, 考虑 $n$ 时的情形.

不妨设 $a_{1} \leq a_{2} \leq a_{3} \leq \cdots \leq a_{n}$.

情形 $1 \quad(1,2, n) \in S_{n}$.

此时由序关系知, 对任意正整数 $1 \leq i<j \leq n-1$, 均有 $(i, j, n) \in S_{n}$. 于是 $\left|S_{n}\right| \geq\left(\begin{array}{c}n-1 \\ 2\end{array}\right) \geq f(n)$, 成立.

情形 $2 \quad(1,2, n) \notin S_{n}$.

此时由均值不等式,

$$
a_{1} a_{2} a_{n} \leq\left(\frac{a_{1}+a_{2}+a_{n}}{3}\right)^{3}<3
$$

从而 $a_{3} a_{4} \cdots a_{n-1} \geq 1$. 对 $a_{3}, a_{4}, \cdots, a_{n-1}$ 这 $n-3$ 个数使用归纳假设知, 若记

$$
S_{n}^{\prime}=\left\{(i, j, k): 3 \leq i<j<k \leq n-1 \text { 且 } a_{i}+a_{j}+a_{k} \geq 3\right\},
$$

则 $\left|S_{n}^{\prime}\right| \geq f(n-3)$.

断言 $\left(\frac{2 n-2}{3}, \frac{2 n+1}{3}, n\right) \in S_{n}$.

证明 假设 $\left(\frac{2 n-2}{3}, \frac{2 n+1}{3}, n\right) \notin S_{n}$, 则 $a_{\frac{2 n-2}{3}}+a_{\frac{2 n+1}{3}}+a_{n}<3$, 结合 $a_{1} \leq a_{2} \leq$ $a_{3} \leq \cdots \leq a_{\frac{2 n+1}{3}}$ 知

$$
a_{1}+a_{2}+\cdots+a_{\frac{2 n+1}{3}} \leq \frac{2 n+1}{3} \cdot \frac{a_{\frac{2 n-2}{}}^{3}+a_{\frac{2 n+1}{3}}}{2}<\frac{\frac{2 n+1}{3}}{2}\left(3-a_{n}\right) .
$$

从而结合均值不等式, 有

$$
a_{1} a_{2} \cdots a_{\frac{2 n+1}{3}} \leq\left(\frac{a_{1}+a_{2}+\cdots+a_{\frac{2 n+1}{3}}}{\frac{2 n+1}{3}}\right)^{\frac{2 n+1}{3}}<\left(\frac{3-a_{n}}{2}\right)^{\frac{2 n+1}{3}} .
$$

又由于 $a_{n} \geq 1$, 从而 $\frac{3-a_{n}}{2} \leq 1$, 结合均值不等式,

$$
\begin{aligned}
a_{1} a_{2} a_{3} \cdots a_{n} & <\left(\frac{3-a_{n}}{2}\right)^{\frac{2 n+1}{3}} a_{n}^{\frac{n-1}{3}} \leq\left(\frac{3-a_{n}}{2} \cdot \frac{3-a_{n}}{2} \cdot a_{n}\right)^{\frac{n-1}{3}} \\
& \leq\left(\frac{\frac{3-a_{n}}{2}+\frac{3-a_{n}}{2}+a_{n}}{3}\right)^{n-1}=1,
\end{aligned}
$$

矛盾！于是假设不成立, 断言得证.

回到原题. 由断言知, 对任意正整数 $\frac{2 n-2}{3} \leq i<j \leq n-1,(i, j, n) \in S_{n}$, 从而

$$
\left|S_{n}\right| \geq\left|S_{n}^{\prime}\right|+\left(\begin{array}{c}
\frac{n+2}{3} \\
2
\end{array}\right) \geq f(n)
$$

成立.

归纳证毕.

设 $m$ 是最小的正整数, 使得 $\frac{1}{6}(m(m+1)(m+2)-6)>\left(\begin{array}{c}3 m \\ 2\end{array}\right)$. 下面证明, 若 $n=3 k+1$, 则

$$
f(n)=\left\{\begin{array}{ll}
\left(\begin{array}{c}
n-1 \\
2
\end{array}\right), & k \geq m \\
\frac{1}{6}(k(k+1)(k+2)-6), & k<m
\end{array} .\right.
$$

先对 $k<m$ 归纳证明 $f(n)=\frac{1}{6}(k(k+1)(k+2)-6)$.

注意到 $k=1$ 时 $f(4)=0$, 符合题意. 假设 $k-1$ 时成立, 则

$$
\begin{aligned}
f(n) & =\min \left\{\left(\begin{array}{c}
n-1 \\
2
\end{array}\right), f(n-3)+\left(\begin{array}{c}
\frac{n+2}{3} \\
2
\end{array}\right)\right\} \\
& =\min \left\{\frac{1}{6}((k-1) k(k+1)-6)+\frac{k(k+1)}{2},\left(\begin{array}{c}
n-1 \\
2
\end{array}\right)\right\} .
\end{aligned}
$$

由于 $k<m$, 故 $\frac{1}{6}(k(k+1)(k+2)-6) \leq\left(\begin{array}{c}3 k \\ 2\end{array}\right)$, 从而 $f(n)=\frac{1}{6}(k(k+1)(k+2)-6)$,成立

再对 $k \geq m$ 归纳证明 $f(n)=\left(\begin{array}{c}n-1 \\ 2\end{array}\right)$.

当 $k=m$ 时, 由 $m$ 的定义知

$$
\begin{aligned}
f(n) & =\min \left\{\left(\begin{array}{c}
n-1 \\
2
\end{array}\right), f(n-3)+\left(\begin{array}{c}
\frac{n+2}{3} \\
2
\end{array}\right)\right\} \\
& =\min \left\{\frac{1}{6}(k(k+1)(k+2)-6),\left(\begin{array}{c}
n-1 \\
2
\end{array}\right)\right\}=\left(\begin{array}{c}
n-1 \\
2
\end{array}\right) .
\end{aligned}
$$

假设 $k>m$ 且 $k-1$ 时成立, 注意到

$$
\begin{aligned}
f(n) & =\min \left\{\left(\begin{array}{c}
n-1 \\
2
\end{array}\right), f(n-3)+\left(\begin{array}{c}
\frac{n+2}{3} \\
2
\end{array}\right)\right\} \\
& =\min \left\{\left(\begin{array}{c}
n-4 \\
2
\end{array}\right)+\left(\begin{array}{c}
\frac{n+2}{3} \\
2
\end{array}\right),\left(\begin{array}{c}
n-1 \\
2
\end{array}\right)\right\}=\left(\begin{array}{c}
n-1 \\
2
\end{array}\right)
\end{aligned}
$$

其中最后一步用到了 $\frac{1}{2} m(m+1)>9 m-6$ (否则, 显然 $m \geq 3$, 所以

$\frac{1}{6}(m(m+1)(m+2)-6)<(9 m-6) \cdot \frac{m+2}{3}=3 m^{2}+4 m-4<\frac{3 m(3 m-1)}{2}=\left(\begin{array}{c}3 m \\ 2\end{array}\right)$,矛盾!), 这表明 $m^{2}-17 m>-12$, 于是 $m \geq 17$, 进而 $k^{2}-17 k \geq m^{2}-17 m \geq$ -12 , 从而 $\frac{1}{2} k(k+1)>9 k-6$. 由此知 $\left(\begin{array}{c}k+1 \\ 2\end{array}\right)>9 k-6=\left(\begin{array}{c}3 k \\ 2\end{array}\right)-\left(\begin{array}{c}3 k-3 \\ 2\end{array}\right)$, 即 $\left(\begin{array}{c}\frac{n+2}{3} \\ 2\end{array}\right)>\left(\begin{array}{c}n-1 \\ 2\end{array}\right)-\left(\begin{array}{c}n-4 \\ 2\end{array}\right)$, 成立.
归纳证毕.

注意到 $\left(\begin{array}{c}2022 \\ 2\end{array}\right)=1011 \times 2021<\frac{1}{6} \cdot 674^{3}$, 所以 $m<674$, 进而由 $(*)$ 知 $f(2023)=\left(\begin{array}{c}2022 \\ 2\end{array}\right)$, 故 $|S| \geq\left(\begin{array}{c}2022 \\ 2\end{array}\right)$.

三、设 $n$ 是正整数. 在一个由 $n^{2}$ 个边长为 1 的小正方形构成的 $n \times n$ 正方形网格中, 有 $n$ 块奶酪放置在 $n$ 个不同的格点上. 一只老鼠从左上角出发, 它只能沿着网格线行走. 设 $f(n)$ 为最小的正整数, 满足无论 $n$ 块奶酪如何放置,老鼠都可以选择一条总长度不超过 $f(n)$ 的路径, 使得这条路径可以经过所有奶酪. 证明: 对任意正实数 $\varepsilon$, 存在正实数 $N$, 满足对任意正整数 $n>N$, 均有

$$
(\sqrt{2}-\varepsilon) n^{1.5} \leq f(n) \leq(\sqrt{3}+\varepsilon) n^{1.5} .
$$

证明 我们将证明 $\sqrt{2} n \sqrt{n}-10 n \leq f(n) \leq \sqrt{3} n \sqrt{n}+10 n$ 对任意正整数 $n$成立. 这样, 对任意 $\varepsilon>0$, 我们取 $N=\left\lceil\frac{10^{6}}{\varepsilon}\right\rceil$ 即可满足题目条件.

先证明: 对任意正整数 $n$, 均有 $f(n) \geq \sqrt{2} n \sqrt{n}-5 n$. 以网格的左下角为原点, 坐标轴平行于网格边界建立平面直角坐标系, 且右上角的坐标为 $(n, n)$, 那么网格的所有格点即为矩形 $R=[0, n] \times[0, n]$ 内的所有整点. 对矩形 $[0, n] \times[0, n]$内的任意一点 $X$, 定义 $f(X)$ 为与 $X$ Manhattan 距离最近的点. 其中, 两点 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$ 的 Manhattan 距离定义为 $d(A, B)=\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right|$.

令 $M=\left\lfloor\sqrt{\frac{n}{2}}\right\rfloor$. 我们取出点集

$$
S=\left\{\left(\frac{s \sqrt{n}}{\sqrt{2}}, \frac{t \sqrt{n}}{\sqrt{2}}\right): s, t \in \mathbb{N}, s+t \equiv 1 \quad(\bmod 2), s, t \leq 2 M\right\} .
$$

由 $\sqrt{2} M \leq n$, 从而 $S \subset R$; 且我们有

$$
|S|>2 M^{2} \geq 2\left(\frac{\sqrt{n}}{\sqrt{2}}-1\right)^{2} \geq n-4 \sqrt{n}
$$

并且对 $S$ 中任意两个不同的点 $A, B$, 都满足 $d(A, B) \geq \sqrt{2 n}$. 于是我们对每个 $X \in S$, 让一块奶酪放在 $f(X)$ 处, 剩余 $\max \{0, n-|S|\}$ 块奶酪任意放置. 那么前 $|S|$ 块奶酪两两之间的 Manhattan 距离一定大于 $\sqrt{2 n}-1$, 从而经过所有奶酪的路径长度应至少为

$$
(\sqrt{2 n}-1)(|S|-1) \geq(\sqrt{2 n}-1)(n-4 \sqrt{n}) \geq \sqrt{2} n \sqrt{n}-10 \sqrt{n} \text {. }
$$

再证明: 对任意正整数 $n$, 均有 $f(n) \leq \sqrt{3} n \sqrt{n}+10 n$. 即对任意一种奶酪的放置方式, 都可以找到长度不超过 $\sqrt{3} n \sqrt{n}+5 n$ 经过所有的奶酪.

对 $l<r$, 定义在 $[l, r)$ 中向右遍历的过程为: 将纵坐标 $\in[l, r)$ 的所有奶酪取出, 并且按照横坐标从小到大排列为 $A_{1}, A_{2}, \cdots, A_{t}$. 先走到点 $(0, l)$, 然后依
次按照最短路径经过 $A_{1}, A_{2}, \cdots, A_{t}$, 最后走到 $(n, r)$. 对称地, 定义在 $[l, r)$ 中向左遍历的过程为: 先走到点 $(n, l)$, 然后依次按照最短路径经过 $A_{t}, A_{t-1}, \cdots, A_{1}$后, 走到 $(0, r)$. 考虑这一过程所需要路径的长度: 如果是向右遍历, 那么横向一直向右移动, 长度为 $n$; 设 $A_{1}, A_{2}, \cdots, A_{t}$ 的纵坐标分别为 $y_{1}, y_{2}, \cdots, y_{t}$, 我们有纵向移动距离恰等于

$$
\left|y_{1}-l\right|+\sum_{i=1}^{t-1}\left|y_{i+1}-y_{i}\right|+\left|r-y_{t}\right|
$$

于是过程所需要的路径长度为

$$
\begin{aligned}
L & =n+\left|y_{1}-l\right|+\sum_{i=1}^{t-1}\left|y_{i+1}-y_{i}\right|+\left|r-y_{t}\right| \\
& \leq n+(r-l)+\sum_{i=1}^{t} w\left(A_{i}\right),
\end{aligned}
$$

其中 $w\left(A_{i}\right)=\max \left\{y_{i}-l, r-y_{i}\right\}$.

同理, 对于向左遍历, 同样可以推出路径长度 $L \leq n+(r-l)+\sum w\left(A_{i}\right)$. 接下来, 我们希望将 $[0, n]$ 表示为若干首尾相接的区间 $[l, r)$ 之并, 每一段都向左或向右遍历, 且满足左右交替. 这样显然所有奶酪都会被经过, 且总路径长度等于

$$
\sum_{[l, r)}\left(n+(r-l)+\sum_{l \leq y\left(C_{i}\right)<r} w\left(C_{i}\right)\right)=n m+n+\sum_{i=1}^{n} w\left(C_{i}\right)
$$

其中 $m$ 为划分的区间个数, $C_{1}, C_{2}, \cdots, C_{n}$ 是所有奶酪的位置.

待定正整数 $S$. 等概率随机选取整数 $0 \leq b<S$, 规定划分出的区间的端点是所有 $\bmod S=b$ 且 $\in(0, n)$ 的整数. 则我们有 $m \leq \frac{n}{S}+1$. 对于每个奶酪所在的坐标 $C_{i}(x, y)$, 设 $y \in[l, r)$, 其中 $[l, r)$ 是某个划分出的区间. 因为 $|r-l| \leq S$,所以对任意自然数 $p \leq S$, 满足 $w\left(C_{i}\right) \geq S-p$ 的 $b$ 的个数一定不超过 $2 p$. 所以

$$
\begin{aligned}
S \cdot \mathbb{E}\left[w\left(C_{i}\right)\right] & \leq(S-1)+(S-1)+(S-2)+(S-2)+\cdots+\left\lfloor\frac{S}{2}\right\rfloor+\left\lfloor\frac{S}{2}\right\rfloor \\
& \leq \frac{3 S^{2}}{4}+S
\end{aligned}
$$

进而我们有

$$
\mathbb{E}\left[\sum_{i=1}^{n} w\left(C_{i}\right)\right] \leq \frac{3 n S}{4}+n
$$

从而找到的路径长度期望不超过

$$
n m+n+\frac{3 n S}{4}+n \leq \frac{n^{2}}{S}+\frac{3 n S}{4}+2 n .
$$

取 $S=\left\lceil\frac{2 \sqrt{3} n}{3}\right\rceil$, 得到找到的路径长度期望不超过 $\sqrt{3} n \sqrt{n}+10 n$, 进而存在一条满足要求且长度不超过该数的路径, 即证!
综上, 命题得证.

评注 (江城) 事实上, 本题的最佳系数是 $\sqrt{2}$. 我们采用同样的随机化方法,但证明实际上路径长度期望不超过 $\sqrt{2} n^{1.5}+O(n)$. 注意到不等式

$$
\left|y_{i+1}-y_{i}\right| \leq w\left(A_{i}\right)+w\left(A_{i+1}\right)-S,
$$

从而可得当分界点随机选取时, 每个点的贡献可当作 $2 w\left(A_{i}\right)-S$ (除 $O\left(\frac{n}{S}\right)$ 个点外），而因为 $w\left(A_{i}\right)$ 可以看做 $\frac{S}{2}$ 到 $S$ 的一个均匀分布, 所以 $2 w\left(A_{i}\right)-S$ 的期望约等于

$$
2 \cdot \frac{3 S}{4}-S=\frac{S}{2}
$$

所以，可得路径长度期望不超过

$$
\frac{n^{2}}{S}+\frac{n S}{2}+O(n)
$$

取 $S=\sqrt{2 n}$ 立即得到 $f(n) \leq \sqrt{2} n^{1.5}+O(n)$, 得证!

上述过程可以有直观的解释方式：每次行走时强迫先从起点走到中间线 $\frac{l+r}{2}$, 再从中间线走到下一个点. 这样每个点行走到中间线距离的期望即为 $\frac{r-l}{4}$,将两边贡献相加即为一半的区间长度.

四、设 $m$ 是不小于 3 的正奇数. 证明: 存在正整数 $x$ 及正整数 $a, b$, 使得在 $a+1, a+2, \cdots, a+b$ 这 $b$ 个正整数中, 恰有 20232024 个数 $y$ 同时满足 $y \equiv-1$ $(\bmod m)$ 且 $y^{2} \equiv 1(\bmod x)$; 恰有 2023 个数 $z$ 同时满足 $z \equiv 1(\bmod m)$ 且 $z^{2} \equiv 1(\bmod x)$.

证明 记 $N=20232024, N^{\prime}=2023$. 对正整数 $x$, 记

$$
A_{x}=\left\{t: t^{2} \equiv 1 \quad(\bmod x)\right\} .
$$

如果 $y \in A_{x}$ 且 $y \equiv-1(\bmod m)$, 则将 $y$ 染为红色; 如果 $y \in A_{x}$ 且 $y \equiv 1$ $(\bmod m)$, 则将 $y$ 染为蓝色. 则原题等价于要找到一段区间里的所有整数中, 恰有 $N$ 个红点、 $N^{\prime}$ 个蓝点.

我们证明更强的命题: 存在满足要求的 $(x, a, b)$, 并且 $x$ 与 $m$ 互质.

注意到, 我们只需要找到两个区间 $I_{1}, I_{2}$, 各自包含 $N$ 个红点, 且包含的蓝点个数分别为 $N_{1}, N_{2}$, 其中 $N_{1}>N^{\prime}>N_{2}$. 这样, 我们考虑从 $I_{1}$ 变化到 $I_{2}$ 的过程: 每次变化中, 可以让左端点或右端点加 1 或减 1 ; 或者在左端点为红点、右端点 +1 为红点的时候让区间向右平移 1 ; 相反地向左平移 1 . 总之, 可以在保证区间内红点数仍为 $N$ 的同时确保蓝点个数变化不超过 1 , 且最终可以到达 $I_{2}$.
于是, 一定存在中间的一个时刻使得蓝点个数恰等于 $N^{\prime}$, 从而完成证明.

当 $(x, m)=1$ 时, 因为对任意 $l, l, l+x, \cdots, l+(m-1) x$ 要么全在 $A_{x}$ 中, 要么全部不在 $A_{x}$ 中, 故对任意正整数 $L, A_{x} \cap[L, L+m x)$ 中 $\bmod m=0,1, \cdots, m-1$的元素个数均相同. 即: 任意连续 $m x$ 个点中红点与蓝点个数相同. 故易知可以找到 $I_{1}$ 使得它包含 $N$ 个红点和 $\geq N>N^{\prime}$ 个蓝点.

我们接下来证明: 存在 $x$ 和一个区间 $I$, 使得该区间内没有蓝点, 且红点个数 $\geq N$, 从而取 $I$ 的一个包含 $N$ 个红点的子区间 $I_{2}$ 即证.

取出一列质数 $p_{1}, p_{2}, \cdots$, 满足如下条件: $p_{1}=2$; 对任意正整数 $i \geq 2$, 均有

$$
p_{i} \equiv 1 \quad\left(\bmod m \cdot \prod_{j=1}^{i-1} p_{j}\right)
$$

熟知对任意正整数 $k$, 均存在 $\bmod k=1$ 的质数, 故可以归纳地构造出满足条件的无穷数列 $\{p\}$.

断言 对任意正整数 $n$, 令 $M=p_{1} p_{2} \cdots p_{n}$. 则 $1 \leq y \leq M$ 且 $y^{2} \equiv 1$ $(\bmod M)$ 的 $y$ 一定满足 $y \equiv 1(\bmod m)$.

证明 对 $2 \leq j \leq n$, 记 $y_{n, j}$ 为唯一满足 $1 \leq y \leq M, y \equiv-2\left(\bmod p_{j}\right)$, $y \equiv 0\left(\bmod \frac{M}{p_{j}}\right)$ 的 $y$.

我们将证明如下事实: $y_{n, 2}+\cdots+y_{n, n}=M-2$; 并且对任意 $2 \leq i \leq n$, $y_{n, i} \equiv 0(\bmod m)$. 对 $n$ 归纳. $n=1$ 时显然成立. 假设命题对 $n-1$ 成立, 来看 $n$ 时的情形. 因为

$$
p_{n} \equiv 1 \quad\left(\bmod m \cdot \prod_{i=1}^{n-1} p_{i}\right)
$$

所以易知对 $2 \leq i \leq n-1$ 有 $y_{n, i}=p_{n} y_{n-1, i}$, 保持 $m$ 的倍数. 并且因为 $2 p_{n}-2$是 $p_{1} p_{2} \cdots p_{n-1}$ 的倍数, 所以 $y_{n, n}=2 p_{n}-2$ 也为 $m$ 的倍数. 同时,

$$
\begin{aligned}
\sum_{i=2}^{n} y_{n, i} & =p_{n} \cdot \sum_{i=2}^{n-1} y_{n-1, i}+\left(2 p_{n}-2\right) \\
& =p_{n}\left(p_{1} p_{2} \cdots p_{n-1}-2\right)+2 p_{n}-2 \\
& =M-2 .
\end{aligned}
$$

完成归纳.

注意到, $y^{2} \equiv 1(\bmod M)$ 等价于对任意 $1 \leq i \leq n, y \equiv 1\left(\bmod p_{i}\right)$ 或 $y \equiv-1\left(\bmod p_{i}\right)$. 取出所有满足 $y \equiv-1\left(\bmod p_{i}\right)$ 的 $i \geq 2$ 构成集合 $S$, 则

$$
y \equiv 1+\sum_{i \in S} y_{n, i}(\bmod M)
$$

由 $1+y_{n, 2}+\cdots+y_{n, n}=M-1<M$, 在 (2) 中, 如果 $y \leq M$, 则一定有

$$
y=1+\sum_{i \in S} y_{n, i} \equiv 1 \quad(\bmod m)
$$

从而断言成立.

回到原题. 对正整数 $n$, 记 $x=p_{1} p_{2} \cdots p_{n}$. 取正整数 $u$ 满足 $u x \equiv-2$ $(\bmod m)$, 根据断言, 我们可以取 $I=[u x,(u+1) x)$, 使得其中只有红点. 我们只需要红点的个数 $\geq N$, 而这只用 $2^{n-1} \geq N$, 取 $n>\log _{2} N+1$ 即可!

综上, 命题得证.

