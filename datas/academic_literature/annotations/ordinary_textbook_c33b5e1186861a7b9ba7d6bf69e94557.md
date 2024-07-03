数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年美国数学奥林匹克试题解析 

韦晨徐子健

(北京十一学校, 100039)

指导教师: 许鹏辉

本文给出 2021 年美国数学奥林匹克 (USAMO) 试题的解答与评析. 不当之处, 请指正.

## I. 试 题

1. 在锐角 $\triangle A B C$ 外部分别作长方形 $B C C_{1} B_{2}, C A A_{1} C_{2}$, 和 $A B B_{1} A_{2}$, 且满足

$$
\angle B C_{1} C+\angle C A_{1} A+\angle A B_{1} B=\pi .
$$

证明: 直线 $B_{1} C_{2}, C_{1} A_{2}$, 和 $A_{1} B_{2}$ 共点.

2. 一个国家公园由平面上若干条小路和它们的交叉点组成. 假设

(1) 每条小路的两个端点是不同的交叉点,

(2) 每个交叉点恰是三条小路的端点,

(3) 任意两条小路只在端点处相交,

(4) 任意两个交点之间最多有一条小路连接.

下图给出一种可能的平面国家公园的设计, 其中包括 6 个交叉点和 9 条小路.

![](https://cdn.mathpix.com/cropped/2024_02_26_7f3d825a92bd4c2a00bbg-01.jpg?height=271&width=468&top_left_y=2126&top_left_x=794)

一个游客在国家公园里按如下方式步行游览: 她从某个交叉点出发沿某条修订日期: 2021-05-19.
小路行走, 在这条小路尽头的交叉点处她向左转进入下一条小路继续行走, 在下一条小路尽头的交叉点处她向右转, 这样一直走下去并在每次小路尽头的交叉点处交替左转和右转, 直到她回到出发的交叉点. 对所有国家公园可能的设计和游客可能的出发点, 求在游客游览过程中经过某一交叉点次数的最大可能值.

3. 从一个空白的 $n \times n(n \geq 2)$ 棋盘开始, 每一分钟可对棋盘做如下三个操作之一:

（1）如果棋盘上有构成 $L-$ 形状的三个方格 $\underset{x}{x}$ (不允许旋转)内都没有石子,则可以在这三个方格内各放一颗石子;

(2) 如果某一列中每个方格内都各有一颗石子, 则可以将这列方格中所有的石子取走;

(3) 如果某一行中每个方格内都各有一颗石子, 则可以将这行方格中所有的石子取走.

求所有正整数 $n \geq 2$, 使得可以经过若干次(至少一次)操作后,棋盘上没有石子。

4. 设 $S$ 是由正整数组成的有限集, 满足对每个正整数 $s \in S$ 和它的每个正约数 $d$, 都存在唯一的正整数 $t \in S$, 使得 $\operatorname{gcd}(s, t)=d$ (正整数 $s$ 和 $t$ 可以相等).试确定集合 $S$ 中元素个数的所有可能值.
5. 给定整数 $n>4$. 求下列 $2 n$ 元方程组的所有正实数解:

$$
\begin{aligned}
a_{1}=\frac{1}{a_{2 n}}+\frac{1}{a_{2}}, & a_{2} & =a_{1}+a_{3}, \\
a_{3}=\frac{1}{a_{2}}+\frac{1}{a_{4}}, & a_{4} & =a_{3}+a_{5}, \\
a_{5}=\frac{1}{a_{4}}+\frac{1}{a_{6}}, & a_{6} & =a_{5}+a_{7}, \\
\vdots & & \vdots \\
a_{2 n-1}=\frac{1}{a_{2 n-2}}+\frac{1}{a_{2 n}}, & a_{2 n} & =a_{2 n-1}+a_{1} .
\end{aligned}
$$

6. 设 $A B C D E F$ 为一个凸六边形, 满足 $A B / / D E, B C / / E F, C D / / F A$,且

$$
A B \cdot D E=B C \cdot E F=C D \cdot F A \text {. }
$$

分别记线段 $A D, B E, C F$ 的中点为 $X, Y, Z$. 证明: $\triangle A C E$ 的外心, $\triangle B D F$ 的外心, 和 $\triangle X Y Z$ 的垂心三点共线.

## II. 解答与评注

1. 在锐角 $\triangle A B C$ 外部分别作长方形 $B C C_{1} B_{2}, C A A_{1} C_{2}$, 和 $A B B_{1} A_{2}$, 且满足

$$
\angle B C_{1} C+\angle C A_{1} A+\angle A B_{1} B=\pi .
$$

证明: 直线 $B_{1} C_{2}, C_{1} A_{2}$, 和 $A_{1} B_{2}$ 共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_7f3d825a92bd4c2a00bbg-03.jpg?height=1194&width=1422&top_left_y=691&top_left_x=314)

证明 (韦晨) 设矩形 $B C C_{1} B_{2}, C A A_{1} C_{2}, A B B_{1} A_{2}$ 的外接圆分别为 $\Gamma_{A}$, $\Gamma_{B}, \Gamma_{C}$, 并假设 $\Gamma_{A} \cap \Gamma_{B}=\{C, P\}$. 连 $P A, P B, P C$, 则有

$$
\angle A P B=(\pi-\angle A P C)+(\pi-\angle B P C)=\angle C A_{1} A+\angle B C_{1} C=\pi-\angle A B_{1} B,
$$

从而 $P$ 在矩形 $A B B_{1} A_{2}$ 的外接圆上.

注意到 $\angle A_{1} P C=\angle B_{2} P C=\frac{\pi}{2}$, 故 $A_{1}, P, B_{2}$ 三点共线. 同理可得点 $P$ 也在直线 $B_{1} C_{2}, C_{1} A_{2}$ 上, 即直线 $B_{1} C_{2}, C_{1} A_{2}$, 和 $A_{1} B_{2}$ 共点于 $P$.

评注 本题的关键在于猜出并刻画三条直线所共点 $P$, 之后导角的步骤并不困难. 但如果没有注意到交点的另一重共圆含义,那么处理起来也会十分棘手.

2. 一个国家公园由平面上若干条小路和它们的交叉点组成. 假设

(1) 每条小路的两个端点是不同的交叉点,

(2) 每个交叉点恰是三条小路的端点,

(3) 任意两条小路只在端点处相交,

(4) 任意两个交点之间最多有一条小路连接.

下图给出一种可能的平面国家公园的设计, 其中包括 6 个交叉点和 9 条小路.

![](https://cdn.mathpix.com/cropped/2024_02_26_7f3d825a92bd4c2a00bbg-04.jpg?height=277&width=485&top_left_y=730&top_left_x=777)

一个游客在国家公园里按如下方式步行游览: 她从某个交叉点出发沿某条小路行走, 在这条小路尽头的交叉点处她向左转进入下一条小路继续行走, 在下一条小路尽头的交叉点处她向右转, 这样一直走下去并在每次小路尽头的交叉点处交替左转和右转, 直到她回到出发的交叉点. 对所有国家公园可能的设计和游客可能的出发点, 求在游客游览过程中经过某一交叉点次数的最大可能值.

解 (韦晨) 在游客游览过程中经过某一交叉点次数的最大可能值为 3.

一方面, 考虑如下的国家公园设计, 其中交叉口旁边的数字为它的编号:

![](https://cdn.mathpix.com/cropped/2024_02_26_7f3d825a92bd4c2a00bbg-04.jpg?height=823&width=617&top_left_y=1730&top_left_x=682)
此时旅客有如下可能的行进路线 $\mathcal{R}$ :

$$
\begin{aligned}
& 1 \rightarrow 2 \xrightarrow{\mathrm{L}} 3 \xrightarrow{\mathrm{R}} 4 \xrightarrow{\mathrm{L}} 5 \xrightarrow{\mathrm{R}} 20 \xrightarrow{\mathrm{L}} 13 \\
& \xrightarrow{\text { R }} 14 \xrightarrow{\text { L }} 15 \xrightarrow{\text { R }} 16 \xrightarrow{\text { L }} 17 \xrightarrow{\text { R }} 6 \xrightarrow{\text { L }} 5 \\
& \xrightarrow{\text { R }} 4 \xrightarrow{\text { L }} 12 \xrightarrow{\text { R }} 11 \xrightarrow{\text { L }} 10 \xrightarrow{\text { R }} 24 \xrightarrow{\text { L }} 9 \\
& \xrightarrow{\text { R }} 20 \xrightarrow{\text { L }} 5 \quad 5 \xrightarrow{\text { R }} 6 \text { L } \quad 7 \xrightarrow[\rightarrow]{\text { L }} 8 \xrightarrow{\text { L }} 1
\end{aligned}
$$

这样, 游客经过了编号为 5 的交叉口恰好 3 次.

另一方面, 我们说明无论国家公园如何设计, 游客经过任何一个交叉口至多3次.

用反证法. 假设在某个设计下游客能经过某个交叉口 $c$ 至少 4 次. 有如下事实:

(1) 游客沿道路从 $a$ 到 $b$ 与从 $b$ 到 $a$ 的转向是相反的(分别为左转和右转).

(2) 游客经过的任意连续三个交叉口唯一确定整条回路(不考虑起点和终点).

事实 (2) 成立是因为这样三个交叉口确定了中间交叉口处的转弯方向, 从而由条件确定了之后每次的转弯方向.

由 (2) 可见: 游客的行进路线 $\mathcal{R}$ 中至多有一处相邻三项形如 $x \rightarrow y \rightarrow z$, 否则设某两次 $x \rightarrow y \rightarrow z$ 发生时后发生的那次结束之后走了 $k$ 次路回到起点, 那么从前发生的那次结束之后进行恰 $k$ 次走路之后必然也回到起点, 从而行程会提前结束, 矛盾.

断言 $\mathcal{R}$ 不可能同时存在相邻三项形如 $x \rightarrow y \rightarrow z$ 和另相邻三项形如 $z \rightarrow y \rightarrow x$.

证明 若不然, 不妨设前者较后者先发生. 设游客沿 $x, y, z$ 行进的后继依次为 $w_{1}, w_{2}, \cdots$, 即 $\mathcal{R}$ 中靠前的一段形如

$$
\cdots \rightarrow x \rightarrow y \rightarrow z \rightarrow w_{1} \rightarrow w_{2} \rightarrow \cdots,
$$

则由(1)知游客沿 $z, y, x$ 行进的前继为 $w_{1}, w_{2}, \cdots$, 即 $\mathcal{R}$ 中靠后的一段形如

$$
\cdots \rightarrow w_{2} \rightarrow w_{1} \rightarrow z \rightarrow y \rightarrow x \rightarrow \cdots
$$

这样, 必有某个正整数 $l$ 使得 $w_{l-1} \rightarrow w_{l} \rightarrow w_{l-1}\left(w_{l-1}=y\right.$ 或 $z$ 是可能发生的)作为连续的三项出现在 $\mathcal{R}$ 序列中, 但这是不可能的! 故断言为真.

由(2)以及断言可知游客 4 次经过 $c$ 的前继与后继路口对应于互不相同的无序对, 而这样的无序对只有 3 个, 矛盾!

综上所述, 所求最大可能值为 3 .
评注 这是一道新颖的组合问题, 其重点是将游客的行进过程抽象为一个三阶递推数列. 基于这一想法, 运用数列周期性的分析技巧就不难解决问题了. 本题的大致思路比较自然, 但对于一些细节的精细书写提出较高的要求.

3. 从一个空白的 $n \times n(n \geq 2)$ 棋盘开始, 每一分钟可对棋盘做如下三个操作之一:

（1）如果棋盘上有构成 $L-$ 形状的三个方格 $\frac{x \times}{x}$ (不允许旋转)内都没有石子,则可以在这三个方格内各放一颗石子;

(2) 如果某一列中每个方格内都各有一颗石子, 则可以将这列方格中所有的石子取走;

(3) 如果某一行中每个方格内都各有一颗石子, 则可以将这行方格中所有的石子取走.

求所有正整数 $n \geq 2$, 使得可以经过若千次(至少一次)操作后,棋盘上没有石子。

解 正整数 $n$ 满足要求当且仅当 $3 \mid n$.

将棋盘的行与列依次从下到上, 从左到右编号为 $0,1, \cdots, n-1$.

一方面, 当 $3 \mid n$ 时, 我们说明存在满足要求的一系列操作.

将棋盘分为 $\frac{n^{2}}{9}$ 个 $3 \times 3$ 的小棋盘. 并依次进行以下操作:

- 对每个小棋盘如妾奴所示进行两次操作 (1);
- 对第 $1,4,7, \cdots, n-2$ 行进行一次操作 (3), 即去掉这些行中的所有石子;
- 对每个小棋盘如 $\frac{x-10}{0.0}$ 所示进行一次操作 (1);
- 对第 $0,1,3,4,6,7, \cdots, n-3, n-2$ 列进行一次操作 $(2)$, 即去掉这些列中的所有石子.

容易看出经过以上操作序列后棋盘上没有石子.

另一方面, 我们说明当 $3 \nmid n$ 时不存在一系列满足要求的操作.

假设经过了以第 $i$ 行 $j$ 列为左下角的L形进行了 $a_{i, j}(0 \leq i, j \leq n-2)$ 次操作 (1), 第 $i$ 行进行了 $h_{i}(0 \leq i \leq n-1)$ 次操作 $(3)$, 第 $j$ 列进行了 $q_{j}(0 \leq i \leq n-1)$次操作 (2)后棋盘上无石子(这里我们没有考虑操作顺序). 引入未定元 $x, y$, 并将第 $i$ 行第 $j$ 列可能的石子对应于单项式 $x^{i} y^{j}$, 则

$$
(1+x+y)\left(\sum_{i=0}^{n-2} \sum_{j=0}^{n-2} a_{i, j} x^{i} y^{j}\right)=\left(\sum_{k=0}^{n-1} h_{k} x^{k}\right) \frac{y^{n}-1}{y-1}+\left(\sum_{k=0}^{n-1} q_{k} y^{k}\right) \frac{x^{n}-1}{x-1}
$$

记

$$
f(x, y)=\sum_{i=0}^{n-2} \sum_{j=0}^{n-2} a_{i, j} x^{i} y^{j}, \quad \omega=\cos \frac{2 \pi}{n}+1 \sin \frac{2 \pi}{n}
$$

注意到对 $0 \leq i, j \leq n-1$, 若 $1+\omega^{i}+\omega^{j}=0$, 则 $0,1,1+\omega^{i}$ 两两之差的模长均为 1 ,从而在复平面上的三个对应点构成正三角形. 因此 $\omega^{j}=-\left(1+\omega^{i}\right)$ 为三次本原单位根, 这导致 $3 \mid n$, 矛盾! 于是, 在 $(*)$ 中代入 $(x, y)=\left(\omega^{i}, \omega^{j}\right)(0<i, j<n)$均得到 $f(x, y)=0$. 根据组合零点定理, 注意到 $f(x, y)$ 关于 $x, y$ 的次数均不超过 $n-2$, 故 $f(x, y) \equiv 0$, 矛盾! 因此不存在满足要求的操作序列.

综上所述, 所求 $n$ 为全体 3 的倍数.

评注 本题较为困难. 首先经过一些简单的尝试不难对 3 的倍数给出构造,但对非 3 的倍数的证明并不容易. 如果从较小的情形出发探索, 可以发现我们只需关注每个 $L$ 形及每行每列的操作次数, 进而可以得到有关操作次数一些等式. 但这并不能明显地导出得到操作次数全为零, 且 $3 \nmid n$ 的条件也难以使用.这里考虑使用二元的母函数, 将原问题转化为多项式的恒等问题, 再利用单位根和组合零点定理导出矛盾. 想到母函数的话本题的证明就不那么困难了.

4. 设 $S$ 是由正整数组成的有限集, 满足对每个正整数 $s \in S$ 和它的每个正约数 $d$, 都存在唯一的正整数 $t \in S$, 使得 $\operatorname{gcd}(s, t)=d$ (正整数 $s$ 和 $t$ 可以相等).试确定集合 $S$ 中元素个数的所有可能值.

解 (徐子健) 所求 $|S|=0$ 或 $2^{k}(k=0,1,2, \cdots)$.

一方面, 我们验证以上 $|S|$ 可以取到.

当 $|S|=0$ 时结论是平凡的, 满足要求. 当 $|S|=1$ 时有 $S=\{1\}$ 满足要求.

当 $|S|=2^{k}(k=1,2, \cdots)$ 时, 设 $p_{1}, p_{2}, \cdots, p_{k}, q_{1}, \cdots, q_{k}$ 为互不相同的素数, 令

$$
S=\left\{\left(\prod_{i \in I} p_{i}\right)\left(\prod_{i \notin I} q_{i}\right) \mid I \subseteq\{1,2, \cdots, k\}\right\}
$$

容易验证上述 $S$ 满足要求.

另一方面, 我们说明 $|S|=0$ 或 $|S|$ 为 2 的幂次.

设 $S \neq \varnothing$ 且 $s \in S$. 若素数 $p$ 使得 $p^{2} \mid s$, 则存在 $t_{1}, t_{2} \in S$ 使得

$$
\operatorname{gcd}\left(s, t_{1}\right)=\frac{s}{p}, \quad \operatorname{gcd}\left(t_{1}, t_{2}\right)=1
$$

这导致 $\operatorname{gcd}\left(s, t_{2}\right)=1$. 而显然 $s \neq t_{1}$, 故使得 $\operatorname{gcd}\left(t_{2}, x\right)=1$ 的 $x \in S$ 至少有两个, 与题设相悖. 故 $S$ 中的元素无平方因子. 注意到 $s$ 的全体正约数 $d$ 与 $S$ 中使
得 $\operatorname{gcd}(s, t)=d$ 的元素 $t$ 一一对应, 故 $|S|$ 恰为 $s$ 的正约数个数, 因此 $|S|$ 只含素因子 2 .

综上所述, 所有的可能的 $|S|$ 为 0 或 $2^{k}(k=0,1,2, \cdots)$.

评注 本题从条件入手分析很容易得到所有数的正约数个数全相等, 且恰为 $|S|$, 这是很强的约束条件! 在此之后, 无论从约数个数的角度还是从选取公约数的角度都不难证明 $S$ 中的数无平方因子. 而本题的构造相对平凡, 于是问题便被完全解决了.

5. 给定整数 $n>4$. 求下列 $2 n$ 元方程组的所有正实数解:

$$
\begin{array}{ccc}
a_{1}=\frac{1}{a_{2 n}}+\frac{1}{a_{2}}, & a_{2}=a_{1}+a_{3}, \\
a_{3}=\frac{1}{a_{2}}+\frac{1}{a_{4}}, & a_{4}=a_{3}+a_{5}, \\
a_{5}=\frac{1}{a_{4}}+\frac{1}{a_{6}}, & a_{6}=a_{5}+a_{7}, \\
\vdots & \vdots \\
a_{2 n-1}=\frac{1}{a_{2 n-2}}+\frac{1}{a_{2 n}}, & a_{2 n}=a_{2 n-1}+a_{1} .
\end{array}
$$

解 (韦晨) 以下我们的下标总是按模 $2 n$ 考虑.

注意到对 $k=1,2, \cdots, n$, 均有

$$
a_{2 k}=a_{2 k-1}+a_{2 k+1}=\frac{1}{a_{2 k-2}}+\frac{2}{a_{2 k}}+\frac{1}{a_{2 k+2}} .
$$

设 $m=\min \left\{a_{2}, a_{4}, \cdots, a_{2 n}\right\}=a_{2 i}, M=\max \left\{a_{2}, a_{4}, \cdots, a_{2 n}\right\}=a_{2 j}$, 则

$$
m=\frac{2}{m}+\frac{1}{a_{2 i-2}}+\frac{1}{a_{2 i+2}} \geq \frac{2}{m}+\frac{2}{M} \geq \frac{2}{M}+\frac{1}{a_{2 j-2}}+\frac{1}{a_{2 j+2}}=M \text {. }
$$

于是 $M=m$, 故 $a_{2}=a_{4}=\cdots=a_{2 n}$. 代入 $(*)$ 与原方程组解得

$$
a_{2}=a_{4}=\cdots=a_{2 n}=2, \quad a_{1}=a_{3}=\cdots=a_{2 n-1}=1
$$

容易验证它们满足方程.

综上所述, 方程有唯一正实数解 $\left(a_{1}, a_{2}, \cdots, a_{2 n}\right)=(1,2,1,2, \cdots, 1,2)$.

评注 本题的关键在于考虑最大数和最小数并使用不等式的方法做估计.事实上这是不难想到的，因为经过简单尝试不难意识到通过恒等变形解方程组是根本不现实的.

6. 设 $A B C D E F$ 为一个凸六边形, 满足 $A B / / D E, B C / / E F, C D / / F A$,
且

$$
A B \cdot D E=B C \cdot E F=C D \cdot F A
$$

分别记线段 $A D, B E, C F$ 的中点为 $X, Y, Z$. 证明: $\triangle A C E$ 的外心, $\triangle B D F$ 的外心, 和 $\triangle X Y Z$ 的垂心三点共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_7f3d825a92bd4c2a00bbg-09.jpg?height=956&width=1016&top_left_y=533&top_left_x=537)

证明 1 (韦晨) 作平行四边形 $A B C B_{1}, B C D C_{1}, C D E D_{1}, D E F E_{1}$, $E F A F_{1}, F A B A_{1}$.

断言 $1 \triangle A C E$ 与 $\triangle B_{1} D_{1} F_{1}$ 的外心重合, $\triangle B D F$ 与 $\triangle A_{1} C_{1} E_{1}$ 的外心重合.

证明 根据平行四边形的构造, 容易看出

$$
A B_{1} \cdot A F_{1}=B C \cdot E F=C D_{1} \cdot C B_{1}=D E \cdot A B=E F_{1} \cdot E D_{1}=F A \cdot D C .
$$

于是

$$
\operatorname{Pow}\left(A,\left(B_{1} D_{1} F_{1}\right)\right)=\operatorname{Pow}\left(C,\left(B_{1} D_{1} F_{1}\right)\right)=\operatorname{Pow}\left(E,\left(B_{1} D_{1} F_{1}\right)\right),
$$

故圆 $(A C E)$ 与 $\left(B_{1} D_{1} F_{1}\right)$ 同心. 同理可得圆 $(B D F)$ 与 $\left(A_{1} C_{1} E_{1}\right)$ 同心, 故断言 1 为真.

断言 $2 X$ 同为线段 $B_{1} C_{1}$ 和线段 $E_{1} F_{1}$ 的中点.

证明 注意到 $A B_{1}$ 和 $D C_{1}$ 分别与 $B C$ 平行且相等, $A F_{1}$ 和 $D E_{1}$ 分别与 $E F$平行且相等, 于是四边形 $A B_{1} D C_{1}$ 与 $A F_{1} D E_{1}$ 均为平行四边形, 故断言 2 为真.

同理 $Y, Z$ 分别同为: $C_{1} A_{1}, F_{1} D_{1} ; A_{1} B_{1}, D_{1} E_{1}$ 的中点.
设圆 $(A C E)$ 与 $(B D F)$ 的圆心分别为 $P, Q$, 并设 $\triangle X Y Z$ 的垂心为 $H$.

由断言 1 及诸平行四边形的构造不难推出 $\triangle A_{1} C_{1} E_{1}$ 与 $\triangle D_{1} F_{1} B_{1}$ 在 $\overrightarrow{P Q}$方向上互为平移变换像. 因此, 由断言 2 知 $\triangle X Y Z$ 恰为 $\triangle A_{1} C_{1} E_{1}$ 和 $\triangle D_{1} F_{1} B_{1}$的中点三角形在 $\overrightarrow{P Q}$ 方向上的平移中点像. 又因为三角形的外心恰为其中点三角形的垂心, 故 $P, Q, H$ 三点共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_7f3d825a92bd4c2a00bbg-10.jpg?height=1051&width=1225&top_left_y=577&top_left_x=427)

证明 2 (Ankan Bhattacharya) 设 $M N P, U V W$ 分别是 $\triangle A C E, \triangle B D F$的中点三角形.

断言 1 在梯形 $A B D E$ 中, $X Y$ 与 $W N$ 的中垂线重合.

证明 注意到 $W X=\frac{1}{2} A B=Y N$, 由中位线的性质即得到.

断言 $2 \quad V, W, M, N$ 共圆.

证明 注意到

$$
W Y \cdot Y N=\frac{1}{2} D E \cdot \frac{1}{2} A B=\frac{1}{2} E F \cdot \frac{1}{2} B C=V Y \cdot Y M,
$$

由圆幂定理得到.

轮换断言 1 与断言 2 , 即 $U, V, W, M, N, P$ 共圆且圆心与 $\triangle X Y Z$ 的外心重合.

我们以 $N V P W M U$ 为单位圆建立复平面, 仍用点对应的字母表示其位置对应的复数. 设 $\triangle X Y Z$ 的垂心为 $H, \triangle A C E, \triangle B D F$ 的外心(即对应中点三角
形的垂心)分别为 $H_{1}, H_{2}$, 则

$$
\begin{aligned}
& H=X+Y+Z=\frac{A+B+C+D+E+F}{2} \\
& H_{1}=M+N+P=A+C+E \text {, } \\
& H_{2}=U+V+W=B+D+F \text {. }
\end{aligned}
$$

故 $H$ 为 $H_{1} H_{2}$ 中点, 这就完成了证明.

评注 本题证明 1 的关键在于想到向内做两组平行四边形 (这是处理对边平行六边形问题的常用技巧). 通过这些构造, 就能把较难处理的两个外心和中点三角形的垂心转化到两个内三角形中. 之后只要大胆猜到命题与外围六边形无关, 问题便迎刃而解. 证明 2 的关键在于构造更多的中点以便运用丰富的中位线信息, 而后敏锐地发现隐藏其中的六点共圆, 最后巧用复数计算完成证明.

