数学新星网 $*$ 教师专栏

www.nsmath.cn/jszl

# 2022 年上海新星春季数学奥林匹克试题解析 

吴尉迟 1 胡珏伟 2 冷岗松 2

(1. 华东师范大学, 200241；2. 上海大学, 200444)

2022 年上海新星春季数学奥林匹克于 2022 年 4 月分两次网络自测, 每次两个小时, 三道题. 下面介绍此次考试的试题和解答. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 如图, 在 $\triangle A B C$ 中, 过 $B, C$ 的圆 $O$ 分别交边 $A B, A C$ 于点 $D, E, H$ 为 $B E$ 与 $C D$ 的交点, $F, G$ 分别在边 $A B, A C$ 上且满足 $A D=B F, A E=C G$, $K$ 为 $\triangle A F G$ 的外心. 求证: $A K / / O H$.

(清华大学学生 严君啸供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_02c3be22abaa8f94e9c9g-1.jpg?height=634&width=516&top_left_y=1639&top_left_x=770)

2. 设非负实数 $a_{1}, a_{2}, \cdots, a_{15}$ 满足 $a_{1}+a_{2}+\cdots+a_{15}=1$. 求 $\sum_{1 \leq i<j \leq 15}\left(\frac{3}{2}\right)^{i+j} a_{i} a_{j}$的最大值.

(温州育英国际学校学生 林逸沿 供题)

修订日期: 2022-05-27.

3. 设 $G$ 是 $n(n \geq 2)$ 个顶点的简单图. 已知存在图 $G$ 的顶点集 $V(G)$ 的一个分划 $\left\{V_{1}, V_{2}, \cdots, V_{k}\right\}$, 使得对任意 $i, j(1 \leq i<j \leq k)$, 均存在不相邻的 $x \in V_{i}, y \in V_{j}$. 证明: 可以用不超过 $n-k+1$ 种颜色将 $V(G)$ 染色, 使得任意相邻顶点不同色.

(上海大学 冷岗松 供题)

4. 设非负整数 $a_{1}, a_{2}, \cdots, a_{2022}$ 的和为 2022 . 用 $x$ 表示满足 $a_{i}+a_{i+1} \geq 3$ 的 $i$ 的个数; 用 $y$ 表示满足 $a_{i} \neq a_{i+1}$ 的 $i$ 的个数, 其中 $i \in\{1,2, \cdots, 2022\}, a_{2023}=$ $a_{1}$. 求 $x+y$ 的最大可能值.

(中国人民大学附属中学 张端阳 供题)

5. 我们称正整数 $n$ 为 “好数”, 若存在整数 $k \geq 2$ 使得 $n$ 是某个正整数的 $k$ 次幂. 证明: 存在无穷多个不能表示为两个“好数”之和的正整数.

(华东师范大学 吴尉迟 供题)

6. 求最小的实数 $\lambda$, 使得对任意正整数 $n$ 及任意非负实数 $x_{1}, x_{2}, \cdots, x_{n}$,均有

$$
\sum_{i=1}^{n}\left(m_{i}-a_{i}\right)^{2} \leq \lambda \sum_{i=1}^{n} x_{i}^{2}
$$

其中对 $1 \leq i \leq n, m_{i}$ 和 $a_{i}$ 分别表示 $x_{1}, x_{2}, \cdots, x_{i}$ 的中位数和算术平均数.

(中国人民大学附属中学 张端阳 供题)

## II. 解答与评注

题 1 如图, 在 $\triangle A B C$ 中, 过 $B, C$ 的圆 $O$ 分别交边 $A B, A C$ 于点 $D, E, H$ 为 $B E$ 与 $C D$ 的交点, $F, G$ 分别在边 $A B, A C$ 上且满足 $A D=B F, A E=C G$, $K$ 为 $\triangle A F G$ 的外心. 求证: $A K / / O H$.

证明 设直线 $D E, B C$ 交于 $Q$. 由布洛卡定理, $O H \perp A Q$. 故要证 $O H / / K A$,只需证 $K A \perp A Q$.

采用同一法. 过 $A$ 作 $A K$ 的垂线, 交直线 $B C$ 于点 $Q^{\prime}$. 要证 $K A \perp A Q$, 只需证 $Q, Q^{\prime}$ 重合.

一方面,

$\frac{B Q^{\prime}}{Q^{\prime} C}=\frac{S_{\triangle A B Q^{\prime}}}{S_{\triangle A C Q^{\prime}}}=\frac{A B}{A C} \frac{\sin \angle B A Q^{\prime}}{\sin \angle C A Q^{\prime}}=\frac{A B}{A C} \frac{\sin \angle F A Q^{\prime}}{\sin \angle G A Q^{\prime}}=\frac{A B}{A C} \frac{\sin \left(180^{\circ}-\angle A G F\right)}{\sin \angle A F G}$

![](https://cdn.mathpix.com/cropped/2024_02_26_02c3be22abaa8f94e9c9g-3.jpg?height=565&width=1236&top_left_y=203&top_left_x=410)

$$
=\frac{A B}{A C} \frac{\sin \angle A G F}{\sin \angle A F G}=\frac{A B}{A C} \cdot \frac{A F}{A G}=\frac{A B}{A C} \cdot \frac{B D}{C E} .
$$

另一方面, 注意到 $\triangle A B E \sim \triangle A C D$, 我们有 $\frac{B E}{C D}=\frac{A B}{A C}$. 从而

于是,

$$
\frac{B Q}{Q C}=\frac{S_{\triangle B D E}}{S_{\triangle C D E}}=\frac{B D \cdot B E}{C D \cdot C E}=\frac{A B}{A C} \cdot \frac{B D}{C E} .
$$

$$
\frac{B Q^{\prime}}{Q^{\prime} C}=\frac{B Q}{Q C}
$$

所以 $Q=Q^{\prime}$.

评注 这是中等偏易的几何题, 考查学生对于角度关系与边长关系的转化能力. 借由布洛卡定理将问题转化为证明 $A Q$ 为 $\odot K$ 的切线. 这可以通过将比例导到 $\triangle A B C$ 内, 用同一法证明. 计算方式多样, 也可以通过圆幂定理计算.

题 2 设非负实数 $a_{1}, a_{2}, \cdots, a_{15}$ 满足 $a_{1}+a_{2}+\cdots+a_{15}=1$. 求 $\sum_{1 \leq i<j \leq 15}\left(\frac{3}{2}\right)^{i+j} a_{i} a_{j}$的最大值.

证明 记 $f\left(a_{1}, a_{2}, \cdots, a_{15}\right)=\sum_{1 \leq i<j \leq 15}\left(\frac{3}{2}\right)^{i+j} a_{i} a_{j}$.

连续函数在有界闭区间上有最大值. 故 $f$ 有最大值. 我们先证明: 若 $f\left(a_{1}, a_{2}, \cdots, a_{15}\right)$ 取到最大值, 可不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{15}$.

事实上, 若存在 $k(1 \leq k \leq 14)$, 使得 $a_{k}>a_{k+1}$, 考虑

$$
\begin{aligned}
& f\left(a_{1}, \cdots, a_{k}, a_{k+1}, \cdots, a_{15}\right)-f\left(a_{1}, \cdots, a_{k+1}, a_{k}, \cdots, a_{15}\right) \\
= & \left(\left(\frac{3}{2}\right)^{k+1}-\left(\frac{3}{2}\right)^{k}\right)\left(a_{k+1}-a_{k}\right)\left(\sum_{i=1}^{k-1}\left(\frac{3}{2}\right)^{i} a_{i}+\sum_{i=k+2}^{15}\left(\frac{3}{2}\right)^{i} a_{i}\right) \leq 0,
\end{aligned}
$$

故可调整 $a_{k}, a_{k+1}$ 的位置.

当 $a_{1} \leq a_{2} \leq \cdots \leq a_{15}$ 时, 注意到

$$
\left(\frac{3}{2}\right)^{i}\left(\left(\frac{3}{2}\right)^{i+1}+\cdots+\left(\frac{3}{2}\right)^{15}\right) \leq\left(\frac{3}{2}\right)^{29}(i=1,2, \cdots, 12)
$$

$$
\begin{aligned}
& \Leftrightarrow\left(\frac{3}{2}\right)^{i}\left(\left(\frac{3}{2}\right)^{16}-\left(\frac{3}{2}\right)^{i+1}\right) \leq \frac{1}{2}\left(\frac{3}{2}\right)^{29} \\
& \Leftrightarrow 3\left(\frac{3}{2}\right)^{2 i}-2\left(\frac{3}{2}\right)^{16}\left(\frac{3}{2}\right)^{i}+\left(\frac{3}{2}\right)^{29} \geq 0 \\
& \Leftrightarrow\left(\frac{3}{2}\right)^{i} \leq \frac{\left(\frac{3}{2}\right)^{15}}{3},
\end{aligned}
$$

而 $\left(\frac{3}{2}\right)^{i} \leq\left(\frac{3}{2}\right)^{12}=\frac{8}{27}\left(\frac{3}{2}\right)^{15}<\frac{1}{3}\left(\frac{3}{2}\right)^{15}$, 可知结论成立.

故

$$
\sum_{i=1}^{12}\left(\frac{3}{2}\right)^{i} a_{i}\left(\sum_{j=i+1}^{15}\left(\frac{3}{2}\right)^{j} a_{j}\right) \leq\left(\frac{3}{2}\right)^{29}\left(a_{1}+\cdots+a_{12}\right) a_{15}
$$

于是

$$
\begin{aligned}
& \sum_{1 \leq i<j \leq 15}\left(\frac{3}{2}\right)^{i+j} a_{i} a_{j} \\
\leq & \left(\frac{3}{2}\right)^{27}\left(a_{13} a_{14}+\frac{3}{2} a_{13} a_{15}+\frac{9}{4}\left(\sum_{i=1}^{12} a_{i}+a_{14}\right) a_{15}\right) \\
\leq & \left(\frac{3}{2}\right)^{27}\left(a_{13}\left(\sum_{i=1}^{12} a_{i}+a_{14}\right)+\frac{3}{2} a_{13} a_{15}+\frac{9}{4}\left(\sum_{i=1}^{12} a_{i}+a_{14}\right) a_{15}\right) .
\end{aligned}
$$

于是问题转化为:

已知 $a+b+c=1, a, b, c \geq 0$, 求 $a b+\frac{3}{2} a c+\frac{9}{4} b c$ 的最大值.

而

$$
a b+\left(\frac{3}{2} a+\frac{9}{4} b\right)(1-a-b)=-\frac{9}{4}\left(b-\frac{9-11 a}{18}\right)^{2}-\frac{95}{144}\left(a-\frac{9}{95}\right)^{2}+\frac{54}{95}
$$

故当 $a=\frac{9}{95}, b=\frac{42}{95}, c=\frac{44}{95}$ 时, 取到最大值 $\frac{54}{95}$.

综上, 当 $a_{1}=a_{2}=\cdots=a_{12}=0, a_{13}=\frac{9}{95}, a_{14}=\frac{42}{95}, a_{15}=\frac{44}{95}$ 时, $\sum_{1 \leq i<j \leq 15}\left(\frac{3}{2}\right)^{i+j} a_{i} a_{j}$ 取到最大值 $\frac{16}{95} \cdot\left(\frac{3}{2}\right)^{30}$.

评注 本题是中等难度的代数题. 上面的做法是观察到 $f$ 取最大值时, $a_{i}$ 应为单调不减排列. 利用单调性将问题转化为三元不等式问题, 再用配方法得到最大值. 本题也可以通过证明

$$
f\left(a_{1}, a_{2}, \cdots, a_{15}\right) \leq f\left(0, a_{2}+\frac{1}{3} a_{1}, a_{3}+\frac{1}{3} a_{1}, a_{4}+\frac{1}{3} a_{1}, a_{5}, \cdots, a_{15}\right)
$$

这样的不等式, 不断将前 12 个 $a_{i}$ 调整到 0 , 进而转化为三元不等式问题.

本题可以将 15 推广到 $n \geq 3$ 的整数.

题 3 设 $G$ 是 $n(n \geq 2)$ 个顶点的简单图. 已知存在图 $G$ 的顶点集 $V(G)$ 的一个分划 $\left\{V_{1}, V_{2}, \cdots, V_{k}\right\}$, 使得对任意 $i, j(1 \leq i<j \leq k)$, 均存在不相邻的 $x \in V_{i}, y \in V_{j}$. 证明: 可以用不超过 $n-k+1$ 种颜色将 $V(G)$ 染色, 使得任意相邻顶点不同色.
证明 记 $\chi(G)$ 表示满足要求的最少的颜色数目, 所证即为 $\chi(G) \leq n-k+1$.

对 $k$ 归纳.

当 $k=2$ 时, 将不相邻的两个顶点染颜色 1 , 其余 $n-2$ 个顶点分别染颜色 $2,3, \cdots, n-1$, 故 $\chi(G) \leq n-1$, 结论成立.

假设结论在不超过 $k-1(k \geq 3)$ 时成立, 现考虑 $k$ 的情形.

由归纳假设, 我们有 $\chi\left(G-V_{k}\right) \leq n-\left|V_{k}\right|-(k-1)+1$, 其中 $G-V_{k}$ 表示 $G$ 删去 $V_{k}$ 及其所连的边后, 所得到的图.

设 $\alpha$ 是 $G-V_{k}$ 的一个使用颜色 $1, \cdots, n-\left|V_{k}\right|-k+2$ 的染色. 用颜色 $n-\left|V_{k}\right|-k+3, \cdots, n-k+2$ 给 $V_{k}$ 中的顶点染色, 这样就把 $\alpha$ 扩充成 $G$ 的一个染色. 为了减少 1 种颜色, 我们希望对这个图重新染色.

由假设可知, 每个 $V_{i}(1 \leq i \leq k-1)$ 都包含一个顶点 $y_{i}, y_{i}$ 与 $V_{k}$ 的某个点 $x_{i}$ 不相邻. 那么一定会有一种颜色仅出现在集合 $\left\{y_{1}, y_{2}, \cdots, y_{k-1}\right\}$ 上, 这是因为这个集合外的顶点数目仅为 $n-k+1$. 不妨设 1 为这种颜色且 $y_{1}, \cdots, y_{m}$ 颜色为 1 . 现在用顶点 $x_{i}(1 \leq i \leq m)$ 的颜色对顶点 $y_{i}$ 进行重新染色. 显然得到的染色是好的并且只用了 $n-k+1$ 种颜色.

评注 这是一道中等偏难的图论题. 对 $k$ 用归纳法是自然的想法. 在归纳过渡中, 关键是将每个 $V_{i}(i=1,2, \cdots k-1)$ 与 $V_{k}$ 中某个点不相邻的点取出, 对其中某种颜色的点进行重新染色.

题 4 设非负整数 $a_{1}, a_{2}, \cdots, a_{2022}$ 的和为 2022 . 用 $x$ 表示满足 $a_{i}+a_{i+1} \geq$ 3 的 $i$ 的个数; 用 $y$ 表示满足 $a_{i} \neq a_{i+1}$ 的 $i$ 的个数, 其中 $i \in\{1,2, \cdots, 2022\}$, $a_{2023}=a_{1}$. 求 $x+y$ 的最大可能值.

解 由题意, 满足 $a_{i}+a_{i+1} \geq 1$ 的 $i$ 至少有 $y$ 个, 进而满足 $a_{i}+a_{i+1}=1$ 或 2 的 $i$ 至少有 $y-x$ 个. 于是

又 $y \leq 2022$, 所以

$$
4044=\sum_{i=1}^{2022}\left(a_{i}+a_{i+1}\right) \geq 3 x+(y-x)=2 x+y .
$$

$$
x+y=\frac{1}{2}((2 x+y)+y) \leq \frac{1}{2}(4044+2022)=3033 .
$$

若 $x+y=3033$, 则上述不等式都取到等号, 此时 $a_{i}+a_{i+1}=1$ 或 3 .于是 $a_{1}, a_{2}, \cdots, a_{2022}$ 奇偶交替, 其中有奇数个奇数, 和应为奇数, 矛盾! 故 $x+y \leq 3032$.

另一方面, 当这 2022 个数为 $\underbrace{0303 \cdots 03}_{505 \text { 组 }} \underbrace{0101 \cdots 01}_{505 \text { 组 }} 02$ 时, 它们的和为 2022 ,
且 $x=1010, y=2022$, 从而 $x+y=3032$. 综上, 所求最大值为 3032 .

评注 本题是相对容易的组合题, 可以通过对较小的偶数 $n$ 试验, 发现取极值时的构造, 再进行论证.

对于一般的正整数 $n \geq 4$, 当 $n \equiv 2(\bmod 4)$ 时, 结果为 $\left[\frac{3 n}{2}\right]-1$; 当 $n \not \equiv 2$ $(\bmod 4)$ 时, 结果为 $\left[\frac{3 n}{2}\right]$. 构造如下:

若 $n=4 k$, 取 $\underbrace{0303 \cdots 03}_{k \text { 组 }} \underbrace{0101 \cdots 01}_{k \text { 组 }}$, 此时 $x=2 k, y=4 k$;

若 $n=4 k+1$, 取 $\underbrace{0303 \cdots 03}_{k \text { 组 }} \underbrace{1010 \cdots 10}_{k \text { 组 }} 1$, 此时 $x=2 k, y=4 k+1$;

若 $n=4 k+2$, 取 $\underbrace{0303 \cdots 03}_{k \text { 组 }} \underbrace{0101 \cdots 01}_{k \text { 组 }} 02$, 此时 $x=2 k, y=4 k+2$;

若 $n=4 k+3$, 取 $\underbrace{1212 \cdots 12}_{k+1 \text { 组 }} \underbrace{1010 \cdots 10}_{k \text { 组 }} 0$, 此时 $x=2 k+2, y=4 k+2$.

题 5 我们称正整数 $n$ 为 “好数”, 若存在整数 $k \geq 2$ 使得 $n$ 是某个正整数的 $k$ 次幂. 证明: 存在无穷多个不能表示为两个“好数”之和的正整数.

证明 设 $n$ 是足够大的正整数, 我们估计所有小于 $n$ 的正整数中不能表示为两好数之和的数的个数的下界.

一方面, 由于平方数模 4 余 0 或 1 , 所以模 4 余 3 正整数均不能表示成两个平方数之和.

另一方面, 小于 $n$ 的正整数若能表示成如下形式:

$$
i^{k}+j^{l}
$$

其中 $i, j$ 为正整数, $k \geq 3$ 且 $l \geq 2$. 则我们有 $i<n^{1 / 3}, j<n^{1 / 2}$.

若 $i \geq 2$, 则 $k<\log _{2} n$; 若 $j \geq 2$, 则 $l<\log _{2} n$.

补充定义当 $i=1$ 时, $k=3$; 当 $j=1$ 时, $l=2$. 则恒有 $k, l \leq \log _{2} n$, 因此由乘法原理, 小于 $n$ 的正整数中, 至多存在 $n^{5 / 6}\left(\log _{2} n\right)^{2}$ 个可表示成 $(*)$ 的形式.

我们考虑小于 $n$ 中模 4 余 3 的正整数, 其中存在至少 $\left[\frac{n}{4}\right]-n^{5 / 6}\left(\log _{2} n\right)^{2}$ 个数不能表示成两个好数的和. 注意到当 $n \rightarrow \infty$ 时, $\left[\frac{n}{4}\right]-n^{5 / 6}\left(\log _{2} n\right)^{2} \rightarrow \infty$, 故命题成立.

评注 本题是中等难度的数论题. 上面的做法是估计形如 $i^{k}+j^{l}(i, j \in$ $\left.\mathbb{N}^{*}, k, l \geq 2\right)$ 的数的个数的上界. $k=l=2$ 时, 利用同余方法估计; 其余情形可以利用乘法原理估计。

题 6 求最小的实数 $\lambda$, 使得对任意正整数 $n$ 及任意非负实数 $x_{1}, x_{2}, \cdots, x_{n}$,
均有

$$
\sum_{i=1}^{n}\left(m_{i}-a_{i}\right)^{2} \leq \lambda \sum_{i=1}^{n} x_{i}^{2}
$$

其中对 $1 \leq i \leq n, m_{i}$ 和 $a_{i}$ 分别表示 $x_{1}, x_{2}, \cdots, x_{i}$ 的中位数和算术平均数.

解 先证明当 $\lambda=2$ 时不等式成立. 设 $y_{1}, y_{2}, \cdots, y_{n}$ 是 $x_{1}, x_{2}, \cdots, x_{n}$ 的一个排列, 使得 $y_{1} \geq y_{2} \geq \cdots \geq y_{n}$. 下面证明对任意 $1 \leq i \leq n$,

$$
\left|m_{i}-a_{i}\right| \leq \frac{y_{1}+y_{2}+\cdots+y_{\left[\frac{i}{2}\right]}}{i}
$$

事实上, 由对称性, 可不妨设 $x_{1} \geq x_{2} \geq \cdots \geq x_{i}$. 当 $i=2 k+1$ 时,

$$
\begin{aligned}
m_{i}-a_{i} & =x_{k+1}-\frac{x_{1}+x_{2}+\cdots+x_{2 k+1}}{2 k+1} \\
& \leq x_{k+1}-\frac{(k+1) x_{k+1}}{2 k+1}=\frac{k x_{k+1}}{2 k+1} \\
& \leq \frac{y_{1}+y_{2}+\cdots+y_{k}}{2 k+1}, \\
a_{i}-m_{i} & =\frac{x_{1}+x_{2}+\cdots+x_{2 k+1}}{2 k+1}-x_{k+1} \\
& \leq \frac{x_{1}+x_{2}+\cdots+x_{k}+(k+1) x_{k+1}}{2 k+1}-x_{k+1} \\
& \leq \frac{y_{1}+y_{2}+\cdots+y_{k}}{2 k+1},
\end{aligned}
$$

于是

$$
\left|m_{i}-a_{i}\right| \leq \frac{y_{1}+y_{2}+\cdots+y_{k}}{2 k+1} .
$$

当 $i=2 k$ 时,

$$
\begin{aligned}
m_{i}-a_{i} & =\frac{x_{k}+x_{k+1}}{2}-\frac{x_{1}+x_{2}+\cdots+x_{2 k}}{2 k} \\
& \leq \frac{x_{k}+x_{k+1}}{2}-\frac{\frac{k}{2}\left(x_{k}+x_{k+1}\right)}{2 k}=\frac{x_{k}+x_{k+1}}{4} \\
& \leq \frac{y_{1}+y_{2}+\cdots+y_{k}}{2 k}, \\
a_{i}-m_{i}= & \frac{x_{1}+x_{2}+\cdots+x_{2 k}}{2 k}-\frac{x_{k}+x_{k+1}}{2} \\
\leq & \frac{x_{1}+x_{2}+\cdots+x_{k}+\frac{k}{2}\left(x_{k}+x_{k+1}\right)}{2 k}-\frac{x_{k}+x_{k+1}}{2} \\
\leq & \frac{y_{1}+y_{2}+\cdots+y_{k}}{2 k}
\end{aligned}
$$

于是

$$
\left|m_{i}-a_{i}\right| \leq \frac{y_{1}+y_{2}+\cdots+y_{k}}{2 k}
$$

回到原题. 结合 Hardy 不等式 $(p=2$ 时) 得,

$$
\sum_{i=1}^{n}\left(m_{i}-a_{i}\right)^{2} \leq \sum_{k=1}^{n}\left(\frac{1}{(2 k)^{2}}+\frac{1}{(2 k+1)^{2}}\right)\left(y_{1}+y_{2}+\cdots+y_{k}\right)^{2}
$$

$$
\begin{aligned}
& \leq \frac{1}{2} \sum_{k=1}^{n}\left(\frac{y_{1}+y_{2}+\cdots+y_{k}}{k}\right)^{2} \\
& \leq 2 \sum_{k=1}^{n} y_{k}^{2}=2 \sum_{i=1}^{n} x_{i}^{2}
\end{aligned}
$$

另一方面, 当取 $n=2 N+1$, 且 $x_{1}, x_{2}, \cdots, x_{2 N+1}$ 为

$$
0,0, \frac{1}{\sqrt{1}}, 0, \frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{3}}, \cdots, 0, \frac{1}{\sqrt{N}}
$$

时, $m_{1}=m_{2}=\cdots=m_{2 N+1}=0$, 且

所以

$$
\begin{aligned}
& a_{2 k+1}=\frac{\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\cdots+\frac{1}{\sqrt{k}}}{2 k+1}>\frac{2 \sqrt{k+1}-2}{2 k+1}, \\
& a_{2 k+2}=\frac{\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\cdots+\frac{1}{\sqrt{k}}}{2 k+2}>\frac{2 \sqrt{k+1}-2}{2 k+2} .
\end{aligned}
$$

$$
\begin{aligned}
\sum_{i=1}^{2 N+1}\left(m_{i}-a_{i}\right)^{2} & =\sum_{i=1}^{2 N+1} a_{i}^{2} \\
& >\sum_{k=1}^{N-1}\left(\frac{1}{(2 k+1)^{2}}+\frac{1}{(2 k+2)^{2}}\right)(2 \sqrt{k+1}-2)^{2} \\
& >2 \sum_{k=1}^{N-1} \frac{(\sqrt{k+1}-1)^{2}}{(k+1)^{2}}>2 \sum_{k=1}^{N-1}\left(\frac{1}{k+1}-\frac{2}{(k+1)^{\frac{3}{2}}}\right) \\
& =2 \sum_{k=2}^{N} \frac{1}{k}-4 \sum_{k=2}^{N} \frac{1}{k^{\frac{3}{2}}} .
\end{aligned}
$$

又

$$
\sum_{i=1}^{2 N+1} x_{i}^{2}=\sum_{k=1}^{N} \frac{1}{k}
$$

且 $\sum_{k=1}^{\infty} \frac{1}{k}$ 发散, $\sum_{k=1}^{\infty} \frac{1}{k^{\frac{3}{2}}}$ 收玫, 所以令 $N \rightarrow \infty$ 得, $\lambda \geq 2$. 综上, 所求最小值为 2 .

评注 本题是困难的代数题. 上述解法通过将 $m_{i}-a_{i}$ 放缩为 $x_{1}, \cdots, x_{n}$ 中较大的 $\left[\frac{i}{2}\right]$ 个的算术平均的一半, 这样结合 $p=2$ 情形的 Hardy 不等式可得最优系数为 2 , 其中最优性可通过 $x_{1}, \cdots, x_{n}$ 将差不多一半的项取成与 Hardy 不等式中的最优项同阶的量得到.

Hardy 不等式如下, 其中 $A_{i}$ 取 $i^{-\frac{1}{p}}$ 时系数 $\left(\frac{p}{p-1}\right)^{p}$ 是最优的:

设 $x_{1}, x_{2}, \cdots, x_{n}$ 是非负实数, 实数 $p>1$, 则

其中 $A_{i}=\frac{x_{1}+\cdots+x_{i}}{i}$.

$$
\sum_{i=1}^{n} A_{i}^{p}<\left(\frac{p}{p-1}\right)^{p} \sum_{i=1}^{n} x_{i}^{p}
$$

