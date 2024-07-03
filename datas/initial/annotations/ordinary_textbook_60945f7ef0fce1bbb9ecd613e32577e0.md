数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2022 年北大数学夏令营试题解析 

张端阳<br>(中国人民大学附属中学, 100080)

炎热的八月, 北京大学如期举办了每年一次的数学夏令营. 本次夏令营进行了两天测试, 每天四道题. 题目质量较高, 且不少有高等背景. 本文给出题目的解答以及简评, 不当之处敬请批评指正.

## I. 试 题

1. 设 $n$ 是一个正整数, 在 $1,2, \cdots, n$ 中等可能地随机选取一个数. 甲乙轮流猜测所选的这个数, 甲先开始. 若猜测的数不为选出的数, 则双方可得知选出的数与猜测的数的大小关系. 在双方均采取最优策略 (使自己猜出的概率最大)的情况下, 求甲先猜出的概率.
2. 设数列 $\left\{f_{n}\right\}_{-\infty}^{+\infty}$ 满足只有 $f_{1}, f_{2}, \cdots, f_{2022}$ 可能不为 0 . 令

$$
M(n)=\max _{r, s \geq 0} \frac{\sum_{i=n-r}^{n+s}\left|f_{i}\right|}{r+s+1}
$$

证明:

$$
\sum_{n=1}^{2023}|M(n)-M(n-1)| \leq \sum_{n=1}^{2023}\left|f_{n}-f_{n-1}\right|
$$

3. 对三维欧氏空间中的任意一点 $P$ 及正实数 $r$, 用 $B_{r}(P)$ 表示以 $P$ 为球心、 $r$ 为半径的球及其内部. 证明: 存在正整数 $n$, 使得不存在满足如下三个条件的 $n$ 个集合 $B_{r_{i}}\left(P_{i}\right), 1 \leq i \leq n$ :

(a) $r_{i} \geq 1,1 \leq i \leq n$;

(b) $B_{r_{i}}\left(P_{i}\right) \cap B_{1}(O) \neq \emptyset, 1 \leq i \leq n$, 其中 $O=(0,0,0)$ 表示原点;

(c) 当 $i \neq j$ 时, $P_{i} \notin B_{r_{j}}\left(P_{j}\right)$.

4. 小坤生活在 2022 维空间中. 有一次他得到了一个由 $3^{2022}$ 个各边长为 1 的 2022 维小立方体沿格线拼成的、各边长为 3 的 2022 维大立方体. 对每个 $1 \leq m \leq 2021$, 他想要知道如果他沿格线不重叠地从大立方体中切下由 $2^{m}$ 个小立方体构成的、边长为 2 或 1 的长方体, 那么他能切下的长方体的最大可能数量 $f(m)$.

我们虽然不知道他有没有实现他的想法, 但想必聪明如你至少知道是否有一个 $m$ 满足 $f(m) \geq 806 f(m+1)$. 你能说说到底有没有这个 $m \in$ $\{1,2, \cdots, 2020\}$, 以及为什么吗?

5. 已知实数 $c$ 满足对任意正整数 $n, n^{c}$ 是整数. 证明: $c$ 是整数.
6. 设 $a_{i j}(1 \leq i, j \leq 2022)$ 是绝对值不超过 2022 的整数, 证明:

$$
\prod_{i=1}^{2022}\left(\sum_{j=1}^{2022} a_{i j}^{2}\right) \geq\left(\sum_{j=1}^{2022} \prod_{i=1}^{2022} a_{i j}\right)^{2}
$$

并求出使等号成立的数组 $a_{i j}$ 的个数.

7. 如图, $\triangle A B C$ 的外接圆是 $\Omega$, 外心是 $O . D, E$ 是 $\Omega$ 的一对对径点, $\Omega$ 在 $D$处的切线分别交直线 $B C, A B$ 于点 $J, L, \Omega$ 在 $E$ 处的切线分别交直线 $B C, A C$于点 $K, M$. 设 $\triangle A D J, \triangle A E K$ 的外接圆交于另一点 $F, \triangle A D L, \triangle A E M$ 的外接圆交于另一点 $N$, 证明: 若 $N$ 在直线 $A O$ 上, 则 $F$ 也在.

![](https://cdn.mathpix.com/cropped/2024_02_26_881ecd6a40edb8be6cdcg-02.jpg?height=748&width=831&top_left_y=1599&top_left_x=612)

8. 设 $p$ 是奇素数, 非负整数 $d<\frac{p-1}{2}$. 证明: 至多存在 $10 p$ 个系数在 $\{0,1, \cdots, p-1\}$ 中的 $d$ 次多项式 $f$, 满足

$$
\left|\left\{i \in\{1,2, \cdots, p\}: p \mid f(i)-2^{i}\right\}\right|>\sqrt{p d} .
$$

## II. 解答与评注

题 1 设 $n$ 是一个正整数, 在 $1,2, \cdots, n$ 中等可能地随机选取一个数. 甲乙轮流猜测所选的这个数, 甲先开始. 若猜测的数不为选出的数, 则双方可得知选出的数与猜测的数的大小关系. 在双方均采取最优策略 (使自己猜出的概率最大) 的情况下，求甲先猜出的概率.

解 因为本题只涉及数的相对大小关系, 所以对任意 $n$ 个不同的数, 甲先猜出的概率都相同.

下面对 $n$ 归纳证明, 先手面对 $n$ 个数时先猜出的概率为 $\frac{\left[\frac{n+1}{2}\right]}{n}$.

当 $n=1,2$ 时命题显然成立, 假设命题对小于 $n$ 的正整数都成立, 来看 $n$ 时的情形.

设甲第一次猜的数为 $m$, 有 $\frac{1}{n}$ 的概率直接猜中. 若没猜中, 则有 $\frac{m-1}{n}$ 的概率还剩 $m-1$ 个数, 有 $\frac{n-m}{n}$ 的概率还剩 $n-m$ 个数, 然后相当于乙变成先手.

由归纳假设, 先手先猜出的概率不小于 $\frac{1}{2}$, 于是乙为使自己先猜出的概率最大应选择猜有效的数, 这样就完全转化为归纳假设. 从而乙先猜出的概率分别为 $\frac{\left[\frac{m}{2}\right]}{m-1}$ 和 $\frac{\left[\frac{n-m+1}{2}\right]}{n-m}$, 故甲先猜出的概率为

$$
\begin{aligned}
& \frac{1}{n}+\frac{m-1}{n}\left(1-\frac{\left[\frac{m}{2}\right]}{m-1}\right)+\frac{n-m}{n}\left(1-\frac{\left[\frac{n-m+1}{2}\right]}{n-m}\right) \\
= & 1-\frac{1}{n}\left(\left[\frac{m}{2}\right]+\left[\frac{n-m+1}{2}\right]\right) \\
= & \begin{cases}1-\frac{1}{n}\left(\frac{m}{2}+\frac{n-m}{2}\right)=\frac{1}{2}, & m, n \text { 偶 } \\
1-\frac{1}{n}\left(\frac{m-1}{2}+\frac{n-m+1}{2}\right)=\frac{1}{2}, & m \text { 奇, } n \text { 偶 } \\
1-\frac{1}{n}\left(\frac{m}{2}+\frac{n-m+1}{2}\right)=\frac{n-1}{2 n}, & m \text { 偶, } n \text { 奇 } \\
1-\frac{1}{n}\left(\frac{m-1}{2}+\frac{n-m}{2}\right)=\frac{n+1}{2 n}, & m, n \text { 奇 }\end{cases}
\end{aligned}
$$

最大为 $\frac{\left[\frac{n+1}{2}\right]}{n}$. 归纳证毕.

综上, 所求结果为 $\frac{\left[\frac{n+1}{2}\right]}{n}$.

评注 本题难度较低, 注意到每猜一次都可以化归成已解决的情况即可.不过要注意, 归纳中要说明乙不能通过猜一个无效的数来“让先”以提高胜率.这是要保证逻辑的严谨. 有趣的是, 有同学看错了条件, 以为猜完后只能得到“是”或“否”, 居然恰好能得到正确的答案.
题 2 设数列 $\left\{f_{n}\right\}_{-\infty}^{+\infty}$ 满足只有 $f_{1}, f_{2}, \cdots, f_{2022}$ 可能不为 0 . 令

$$
M(n)=\max _{r, s \geq 0} \frac{\sum_{i=n-r}^{n+s}\left|f_{i}\right|}{r+s+1}
$$

证明:

$$
\sum_{n=1}^{2023}|M(n)-M(n-1)| \leq \sum_{n=1}^{2023}\left|f_{n}-f_{n-1}\right| .
$$

证明 先证明一个引理.

引理 若 $M(n) \geq M(n-1), M(n+1)$, 则称 $M(n)$ 是极大值, 类似定义极小值. 我们有: 若 $M(n)$ 是极大值, 则 $M(n)=\left|f_{n}\right|$.

证明 设 $M(n)=\frac{\sum_{i=n-r}^{n+s}\left|f_{i}\right|}{r+s+1}$, 其中 $r, s \geq 0$, 则

$$
\begin{aligned}
(r+s+1) M(n) & =\sum_{i=n-r}^{n+s}\left|f_{i}\right| \\
& =\sum_{i=n-r}^{n-1}\left|f_{i}\right|+\left|f_{n}\right|+\sum_{i=n+1}^{n+s}\left|f_{i}\right| \\
& \leq r M(n-1)+\left|f_{n}\right|+s M(n+1) \\
& \leq(r+s) M(n)+\left|f_{n}\right|
\end{aligned}
$$

于是 $M(n) \leq\left|f_{n}\right|$.

又由定义, $M(n) \geq\left|f_{n}\right|$, 故 $M(n)=\left|f_{n}\right|$. 引理证毕.

回到原题. 因为 $\left\{f_{n}\right\}$ 在两边均为 0 , 所以可设

$$
0<a_{1}<b_{1}<\cdots<a_{k}<b_{k}<a_{k+1}<2023
$$

使得 $M\left(a_{i}\right)$ 是极大值, $M\left(b_{i}\right)$ 是极小值.

由引理, $M\left(a_{i}\right)=\left|f_{a_{i}}\right|$, 又 $M\left(b_{i}\right) \geq\left|f_{b_{i}}\right|$, 所以

$$
\begin{aligned}
& \sum_{n=1}^{2023}|M(n)-M(n-1)| \\
= & \left(M\left(a_{1}\right)-M(0)\right)+\sum_{i=1}^{k}\left(M\left(a_{i}\right)-M\left(b_{i}\right)\right)+\sum_{i=1}^{k}\left(M\left(a_{i+1}\right)-M\left(b_{i}\right)\right) \\
& +\left(M\left(a_{k+1}\right)-M(2023)\right) \\
\leq & \left(\left|f_{a_{1}}\right|-\left|f_{0}\right|\right)+\sum_{i=1}^{k}\left(\left|f_{a_{i}}\right|-\left|f_{b_{i}}\right|\right)+\sum_{i=1}^{k}\left(\left|f_{a_{i+1}}\right|-\left|f_{b_{i}}\right|\right)+\left(\left|f_{a_{k+1}}\right|-\left|f_{2023}\right|\right) \\
\leq & \sum_{n=1}^{a_{1}}\left|f_{n}-f_{n-1}\right|+\sum_{i=1}^{k} \sum_{n=a_{i}+1}^{b_{i}}\left|f_{n}-f_{n-1}\right|+\sum_{i=1}^{k} \sum_{n=b_{i}+1}^{a_{i+1}}\left|f_{n}-f_{n-1}\right|
\end{aligned}
$$

$$
\begin{aligned}
& +\sum_{n=a_{k+1}+1}^{2023}\left|f_{n}-f_{n-1}\right| \\
= & \sum_{n=1}^{2023}\left|f_{n}-f_{n-1}\right|,
\end{aligned}
$$

其中倒数第二步用到了三角不等式.

综上, 命题得证.

评注 这题的感觉是像 $M(n)$ 这种“平均函数”会减小数列的振幅. 而注意到极小值会变大, 就会自然会考虑极大值的变化, 之后再按极小值和极大值分段也就顺理成章了. 本题 $M(n)$ 的定义来自离散化的哈代一李特尔伍德极大函数 (Hardy-Littlewood maximal function).

题 3 对三维欧氏空间中的任意一点 $P$ 及正实数 $r$, 用 $B_{r}(P)$ 表示以 $P$ 为球心、 $r$ 为半径的球及其内部. 证明: 存在正整数 $n$, 使得不存在满足如下三个条件的 $n$ 个集合 $B_{r_{i}}\left(P_{i}\right), 1 \leq i \leq n$ :

(a) $r_{i} \geq 1,1 \leq i \leq n$;

(b) $B_{r_{i}}\left(P_{i}\right) \cap B_{1}(O) \neq \emptyset, 1 \leq i \leq n$, 其中 $O=(0,0,0)$ 表示原点;

(c) 当 $i \neq j$ 时, $P_{i} \notin B_{r_{j}}\left(P_{j}\right)$.

证明 只需证若 $n$ 个球 $B_{r_{i}}\left(P_{i}\right), 1 \leq i \leq n$ 满足三个条件, 则 $n$ 有上界.

先证明一个引理.

引理 $B_{r_{i}}\left(P_{i}\right) \cap B_{2}(O)$ 包含一个直径为 1 的球, 从而其体积不小于 $\frac{\pi}{6}$.

证明 若 $\left|O P_{i}\right| \leq 1$, 则在射线 $O P_{i}$ 上截一点 $Q$, 使得 $\left|P_{i} Q\right|=1$. 由 $r_{i} \geq 1$,知 $B_{r_{i}}\left(P_{i}\right) \cap B_{2}(O)$ 包含以 $P_{i} Q$ 为直径的球.

若 $\left|O P_{i}\right|>1$, 则在射线 $O P_{i}$ 上顺次截两点 $Q, R$, 使得 $|O Q|=|Q R|=1$. 由 $B_{r_{i}}\left(P_{i}\right) \cap B_{1}(O) \neq \emptyset$ 知 $Q \in B_{r_{i}}\left(P_{i}\right)$, 所以 $B_{r_{i}}\left(P_{i}\right) \cap B_{2}(O)$ 包含以 $Q R$ 为直径的球. 引理证毕.

回到原题. 因为 $B_{2}(O)$ 的体积 $\frac{32 \pi}{3}$ 是 $\frac{\pi}{6}$ 的 64 倍, 所以存在一点 $P$ 被至少 $\frac{n}{64}$个 $B_{r_{i}}\left(P_{i}\right)$ 包含, 设它们为 $B_{r_{i}}\left(P_{i}\right), 1 \leq i \leq k$, 其中 $k \geq \frac{n}{64}$.

由条件 (c), 对任意 $1 \leq i<j \leq k$, 都有 $\left|P_{i} P_{j}\right|>\left|P P_{i}\right|,\left|P P_{j}\right|$, 于是 $\angle P_{i} P P_{j}>\frac{\pi}{3}$, 即 $\overrightarrow{P P}_{i}, 1 \leq i \leq k$ 两两之间的夹角均大于 $\frac{\pi}{3}$. 显然 $k$ 有上界 (事实上可以证明 $k \leq 12$ ), 故 $n$ 有上界.

评注 因为我们只需证 $n$ 存在上界, 所以引理相当于免费加强了条件. 之
后是“球冠十三球” 问题的弱化版, 也是三维情形的接吻数问题 (kissing number problem).

题 4 小坤生活在 2022 维空间中. 有一次他得到了一个由 $3^{2022}$ 个各边长为 1 的 2022 维小立方体沿格线拼成的、各边长为 3 的 2022 维大立方体. 对每个 $1 \leq m \leq 2021$, 他想要知道如果他沿格线不重叠地从大立方体中切下由 $2^{m}$ 个小立方体构成的、边长为 2 或 1 的长方体, 那么他能切下的长方体的最大可能数量 $f(m)$.

我们虽然不知道他有没有实现他的想法，但想必聪明如你至少知道是否有一个 $m$ 满足 $f(m) \geq 806 f(m+1)$. 你能说说到底有没有这个 $m \in$ $\{1,2, \cdots, 2020\}$, 以及为什么吗?

## 解 结论是肯定的.

记题中由 $2^{m}$ 个小立方体构成的、边长为 2 或 1 的长方体为 $A_{m}$, 记维数为 $n$ 时的 $f(m)$ 为 $f(n, m)$.

首先, 证明当 $n \geq 2$ 时 $f(n, n-1)=2 n$.

一方面, 注意到与位于大立方体中心的小立方体相邻的小立方体恰有 $2 n$个, 而每个 $A_{n-1}$ 至少包含其中一个, 所以 $f(n, n-1) \leq 2 n$.

另一方面, 建立 $n$ 维空间直角坐标系, 使得构成大立方体的 $3^{n}$ 个小立方体的中心点为 $\{-1,0,1\}^{n}$. 我们可以直接切下如下 $2 n$ 个 $A_{n-1}$ :

$$
\begin{aligned}
& \left\{\left(a_{1}, \cdots, a_{n}\right) \mid a_{1}, \cdots, a_{i-1} \in\{-1,0\}, a_{i}=-1, a_{i+1}, \cdots, a_{n} \in\{0,1\}\right\}, \\
& \quad\left\{\left(a_{1}, \cdots, a_{n}\right) \mid a_{1}, \cdots, a_{i-1} \in\{0,1\}, a_{i}=1, a_{i+1}, \cdots, a_{n} \in\{-1,0\}\right\},
\end{aligned}
$$

其中 $i=1,2, \cdots, n$.

其次, 估计 $f(n, n-2)$ 的下界.

将 $n$ 维大立方体分为上中下三层, 每层是一个有 $n-1$ 条边为 3 、一条边为 1 的大立方体. 在上中两层以相同的方式切下 $f(n-1, n-3)$ 个 $A_{n-3}$, 并将相同位置的两个 $A_{n-3}$ 合并为一个 $A_{n-2}$. 在下层直接切下 $f(n-1, n-2)=2(n-1)$个 $A_{n-2}$, 因此

$$
f(n, n-2) \geq f(n-1, n-3)+2(n-1) .
$$

累加得，

$$
f(n, n-2) \geq f(2,0)+2(2+3+\cdots+(n-1))=n^{2}-n+2 .
$$

从而

$$
f(2022,2020)>2022^{2}-2022>806 \times 2 \times 2022=806 f(2022,2021)
$$

故 $m=2020$ 满足要求.

评注 本题最大也是唯一的难点就是猜出正确的 $m$, 容易想到只有当 $m$ 很小或很大时才能求出 $f(m)$ 或给出估计. 题中的 806 是考试日期.

题 5 已知实数 $c$ 满足对任意正整数 $n, n^{c}$ 是整数. 证明: $c$ 是整数.

证明 对函数 $f(x)$, 记 $\Delta f(x)=f(x+1)-f(x)$, 归纳定义 $\Delta^{t+1} f(x)=$ $\Delta\left(\Delta^{t} f(x)\right)$.

先证明一个引理.

引理 对任意 $m$ 次可导函数 $f(x)$ 和实数 $x_{0}$, 均存在 $\xi \in\left(x_{0}, x_{0}+m\right)$, 使得 $\Delta^{m} f(x)=f^{(m)}(\xi)$, 其中 $f^{(m)}$ 为 $f$ 的 $m$ 阶导数.

证明 对 $m$ 归纳.

当 $m=1$ 时由拉格朗日微分中值定理即证. 假设 $m$ 时成立, $m+1$ 时,

$$
\Delta^{m+1} f\left(x_{0}\right)=\Delta^{m}\left(f\left(x_{0}+1\right)-f\left(x_{0}\right)\right) .
$$

由归纳假设, 存在 $\xi \in\left(x_{0}, x_{0}+m\right)$, 使得

$$
\Delta^{m}\left(f\left(x_{0}+1\right)-f\left(x_{0}\right)\right)=f^{(m)}(\xi+1)-f^{(m)}(\xi) .
$$

又由拉格朗日微分中值定理, 存在 $\xi_{0} \in(\xi, \xi+1) \subseteq\left(x_{0}, x_{0}+m+1\right)$, 使得

$$
f^{(m)}(\xi+1)-f^{(m)}(\xi)=f^{(m+1)}\left(\xi_{0}\right) .
$$

于是命题对 $m+1$ 也成立.

归纳证毕.

回到原题. 显然 $c \geq 0$, 假设 $c$ 不是整数, 设 $c$ 的整数部分是 $k$.

令 $f(x)=x^{c}, n$ 为正整数. 由引理, 存在 $\xi \in(n, n+k+1)$, 使得

$$
\Delta^{k+1} f(n)=f^{(k+1)}(\xi)=c(c-1) \cdots(c-k) \xi^{c-k-1} .
$$

由条件, 对任意 $n$ 左边均为整数. 但由 $k<c<k+1$ 知, 当 $n$ 充分大 (进而 $\xi$ 充分大) 时, 右边属于区间 $(0,1)$, 矛盾!

综上, 命题得证.

评注 KöMaL 杂志 A. 751 是一道形式和方法均类似的问题:
设 $c$ 是正实数. 若对每个正整数 $n, 1^{c}, 2^{c}, \cdots, n^{c}$ 中至少有 $1 \%$ 是整数, 则 $c$是整数.

不过对于没见过这一做法的学生来说本题很难开展.

题 6 设 $a_{i j}(1 \leq i, j \leq 2022)$ 是绝对值不超过 2022 的整数, 证明:

$$
\prod_{i=1}^{2022}\left(\sum_{j=1}^{2022} a_{i j}^{2}\right) \geq\left(\sum_{j=1}^{2022} \prod_{i=1}^{2022} a_{i j}\right)^{2}
$$

并求出使等号成立的数组 $a_{i j}$ 的个数.

证明 先对 $n \geq 3$ 归纳证明: 对任意实数 $a_{i j}(1 \leq i \leq n, 1 \leq j \leq 2022)$, 都有

$$
\prod_{i=1}^{n}\left(\sum_{j=1}^{2022} a_{i j}^{2}\right) \geq\left(\sum_{j=1}^{2022} \prod_{i=1}^{n} a_{i j}\right)^{2}
$$

并且等号成立的条件为, 存在 $1 \leq i \leq n$ 使得 $a_{i j}=0(1 \leq j \leq 2022)$, 或者存在 $1 \leq j \leq 2022$ 使得 $a_{i j^{\prime}}=0\left(1 \leq i \leq n, 1 \leq j^{\prime} \leq 2022, j^{\prime} \neq j\right)$.

当 $n=3$ 时, 由柯西不等式,

$$
\begin{aligned}
\prod_{i=1}^{3}\left(\sum_{j=1}^{2022} a_{i j}^{2}\right) & \geq\left(\sum_{j=1}^{2022}\left|a_{1 j} a_{2 j}\right|\right)^{2}\left(\sum_{j=1}^{2022} a_{3 j}^{2}\right) \\
& \geq\left(\sum_{j=1}^{2022} a_{1 j}^{2} a_{2 j}^{2}\right)\left(\sum_{j=1}^{2022} a_{3 j}^{2}\right) \\
& \geq\left(\sum_{j=1}^{2022} \prod_{i=1}^{3} a_{i j}\right)^{2} .
\end{aligned}
$$

其中第二个不等号的取等条件为 $a_{1 j} a_{2 j}$ 至多一个非零, 不妨设 $a_{1 j} a_{2 j}=0(2 \leq$ $j \leq 2022$ ). 若 $a_{11} a_{21}=0$, 则不等式右边为 0 , 于是左边也为 0 , 此时存在 $i$ 使得 $a_{i j}=0(1 \leq j \leq 2022)$, 满足第一种取等条件. 若 $a_{11} a_{21} \neq 0$, 则由柯西不等式的取等条件知 $a_{1 j}=a_{2 j}=0(2 \leq j \leq 2022)$, 进而易知 $a_{3 j}=0(2 \leq j \leq 2022)$, 满足第二种取等条件.

归纳的过程只是完全重复上述步骤, 故略去.

最后我们来计算等号成立时数组的个数.

在全部 $4045^{2022 \times 2022}$ 个数组中, 恰有 $\left(4045^{2022}-1\right)^{2022}$ 个数组不满足第一种取等条件, 有 $2022 \times 4044^{2022}$ 个数组不满足第一种取等条件但满足第二种取等条件. 于是所求结果为 $4045^{2022 \times 2022}-\left(4045^{2022}-1\right)^{2022}+2022 \times 4044^{2022}$.

评注 仔细观察可以发现不等式两边项数相差过大, 所以其实相当松, 只有取等条件要略加小心.
题 7 如图, $\triangle A B C$ 的外接圆是 $\Omega$, 外心是 $O . D, E$ 是 $\Omega$ 的一对对径点, $\Omega$ 在 $D$ 处的切线分别交直线 $B C, A B$ 于点 $J, L, \Omega$ 在 $E$ 处的切线分别交直线 $B C, A C$于点 $K, M$. 设 $\triangle A D J, \triangle A E K$ 的外接圆交于另一点 $F, \triangle A D L, \triangle A E M$ 的外接圆交于另一点 $N$, 证明: 若 $N$ 在直线 $A O$ 上, 则 $F$ 也在.

![](https://cdn.mathpix.com/cropped/2024_02_26_881ecd6a40edb8be6cdcg-09.jpg?height=682&width=1110&top_left_y=544&top_left_x=473)

证明 当 $A B=A C$ 时, 由对称性知结论成立, 下不妨设 $A B>A C$.

如图, 设直线 $D E$ 与 $\triangle A D J, \triangle A E K, \triangle A D L, \triangle A E M$ 外接圆的第二交点分别为 $P, Q, R, S$. 易知 $\triangle A R E \sim \triangle A L D$, 所以由 $A E \perp A D$, 知 $A R \perp A L$. 同理, $A P \perp A J, A Q \perp A K, A S \perp A M$.

过 $A$ 作 $\Omega$ 的切线 $l$, 再过 $A$ 作 $D E$ 的垂线交 $B C, D E$ 于点 $U, V$.

由条件, $O$ 在 $\triangle A D L$ 和 $\triangle A E M$ 外接圆的根轴 $A N$ 上, 于是

$$
O S \cdot O E=O R \cdot O D
$$

因为 $O E=O D$, 所以 $O S=O R$, 于是 $A R, A S ; A O, R S$ 四条直线的方向成调和线束, 故与它们垂直的方向 $A B, A C ; l, A U$ 也成调和线束.

设 $l$ 交直线 $B C$ 于点 $T$, 则 $B, C ; U, T$ 成调和点列. 于是 $U$ 在 $T$ 关于 $\Omega$ 的极线上, 所以该极线就是 $A U$. 因为 $D E$ 过 $O$ 且与 $A U$ 垂直, 所以 $D E$ 经过 $T$.

因为 $D J / / U V / / E K$ 且 $D, E ; V, T$ 成调和点列, 所以 $J, K ; U, T$ 也成调和点列. 于是 $A J, A K ; A U, A T$ 成调和线束, 故与它们垂直的方向 $A P, A Q ; P Q, A O$也成调和线束, 从而 $O P=O Q$.

这样,

$$
O P \cdot O D=O Q \cdot O E
$$

故 $O$ 在 $\triangle A D J$ 和 $\triangle A E K$ 外接圆的根轴 $A F$ 上.
综上, 命题得证.

评注 这种证明某点在两圆根轴上且根轴性质并不好的题, 过该点作直线与圆相交, 转化为圆幂是常见的思路. 本题之后的处理就是简单的倒调和罢了.值得一提的是哪怕本题的圆如此之多, 考生们仍提供了三角、复数乃至建系的计算做法.

题 8 设 $p$ 是奇素数, 非负整数 $d<\frac{p-1}{2}$. 证明: 至多存在 $10 p$ 个系数在 $\{0,1, \cdots, p-1\}$ 中的 $d$ 次多项式 $f$, 满足

$$
\left|\left\{i \in\{1,2, \cdots, p\}: p \mid f(i)-2^{i}\right\}\right|>\sqrt{p d}
$$

证明 设满足条件的多项式为 $f_{1}, f_{2}, \cdots, f_{k}$, 我们来证明 $k<10 p$.

对 $1 \leq t \leq k, 1 \leq i \leq p$, 用 $a_{t i}$ 表示 $f_{t}(i)-2^{i}$ 模 $p$ 的余数.

由拉格朗日定理, 对任意 $t_{1} \neq t_{2}$, 有

$$
\begin{aligned}
& \left|\left\{i \in\{1,2, \cdots, p\}: a_{t_{1} i}=a_{t_{2} i}\right\}\right| \\
= & \left|\left\{i \in\{1,2, \cdots, p\}: f_{t_{1}}(i) \equiv f_{t_{2}}(i)(\bmod p)\right\}\right| \leq d
\end{aligned}
$$

故

$$
\sum_{1 \leq t_{1}<t_{2} \leq k}\left|\left\{i \in\{1,2, \cdots, p\}: a_{t_{1} i}=a_{t_{2}}\right\}\right| \leq \mathrm{C}_{k}^{2} \cdot d
$$

另一方面, 记 $b_{i 0}, b_{i 1}, \cdots, b_{i(p-1)}$ 分别为 $a_{1 i}, a_{2 i}, \cdots, a_{k i}$ 中 $0,1, \cdots, p-1$ 的数目, 显然有

$$
\sum_{i=1}^{p} \sum_{j=0}^{p-1} b_{i j}=k p
$$

记 $s=\sum_{i=1}^{p} b_{i 0}$, 由条件, $s>k \sqrt{p d}$.

利用组合数的凸性得,

$$
\begin{aligned}
& \sum_{1 \leq t_{1}<t_{2} \leq k}\left|\left\{i \in\{1,2, \cdots, p\}: a_{t_{1} i}=a_{t_{2} i}\right\}\right| \\
= & \sum_{i=1}^{p} \sum_{j=0}^{p-1} \mathrm{C}_{b_{i j}}^{2} \geq p \cdot \mathrm{C}_{\frac{s}{p}}^{2}+p(p-1) \cdot \mathrm{C}_{\frac{k p-s}{p(p-1)}}^{2} \\
= & \frac{s}{2}\left(\frac{s}{p}-1\right)+\frac{1}{2}(k p-s)\left(\frac{k p-s}{p(p-1)}-1\right) \\
= & \frac{1}{2}\left(\frac{s^{2}}{p-1}-\frac{2 k s}{p-1}+\frac{k^{2} p}{p-1}-k p\right) .
\end{aligned}
$$

上式作为关于 $s$ 的二次函数, $k \sqrt{p d}$ 在对称轴 $s=k$ 的右侧, 所以上式有下界

$$
\frac{1}{2}\left(\frac{k^{2} p d}{p-1}-\frac{2 k^{2} \sqrt{p d}}{p-1}+\frac{k^{2} p}{p-1}-k p\right) .
$$

结合之前的上界, 我们得到

$$
\frac{1}{2}\left(\frac{k^{2} p d}{p-1}-\frac{2 k^{2} \sqrt{p d}}{p-1}+\frac{k^{2} p}{p-1}-k p\right) \leq \mathrm{C}_{k}^{2} \cdot d
$$

化简得,

$$
k^{2}\left(\frac{p d}{p-1}-\frac{2 \sqrt{p d}}{p-1}+\frac{p}{p-1}\right)-k p \leq k(k-1) d
$$

即

$$
k\left(\frac{p d}{p-1}-\frac{2 \sqrt{p d}}{p-1}+\frac{p}{p-1}-d\right) \leq p-d,
$$

即

$$
k(\sqrt{p}-\sqrt{d})^{2} \leq(p-1)(p-d) .
$$

因为 $d<\frac{p}{2}$, 所以

$$
k \leq \frac{(p-1)(\sqrt{p}+\sqrt{d})}{\sqrt{p}-\sqrt{d}}<p \cdot \frac{1+\frac{1}{\sqrt{2}}}{1-\frac{1}{\sqrt{2}}}<10 p
$$

综上, 命题得证.

评注 此题跟 $2^{i}$ 毫无关系, 次数的上界 $d$ 也仅仅是限制了不同多项式的取值重合次数. 唯一的放缩仍是基本的算两次加柯西不等式的技巧, 但复杂的题面掩盖了简单的本质, 使得大部分学生望而生却. 孙牧聪同学指出题中的 $10 p$可以加强为 $(2+\sqrt{2}) p$.

