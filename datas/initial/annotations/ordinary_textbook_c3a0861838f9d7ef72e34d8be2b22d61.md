数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 关于单调凸序列的 Erdös-Szekeres 定理 

石泽晖 1 施柯杰 ${ }^{2}$

(1. 吉林大学附属中学, 长春, 130021; 2. 复旦大学附属中学, 上海, 200433)

## 1. 引 言

1935 年, Erdös 和 Szekeres 证明了两个组合学中的重要结果, 即现在所熟知的 Erdös-Szekeres 定理 [1].

定理 A (Erdös-Szekeres). 对任意正整数 $n \geq 3$, 令 $N(n)$ 表示满足如下条件的 $N$ 的最小整数: 平面上任意 $N$ 个满足无三点共线的点, 都能找到 $n$ 个点使其构成一个凸多边形的顶点. 则 $N(n) \leq\left(\begin{array}{c}2 n-4 \\ n-2\end{array}\right)+1$.

这个问题受 Klein 启发, 她提出并证明了任意五个满足无三点共线的平面上的点总能找到四个点组成一个凸多边形的顶点. 随后, Szekeres 证明了定理 A 中 $N=N(n)$ 的存在性, 并给出了粗略估计; Erdös 用不同的方法证明了 $N(n)$的 $\left(\begin{array}{c}2 n-4 \\ n-2\end{array}\right)+1$ 这一上界. 值得一提的是, Szekeres 和 Klein 在定理 A 得到圆满解决后不久就喜结连理, 故 Erdös 将定理 A 戏称作是 “Happy Ending” 定理.

定理 B (Erdös-Szekeres). 设 $a, b$ 为正整数, 令 $N(a, b)$ 表示满足下列条件的 $N$ 的最小整数：任意由 $N$ 个不同实数构成的序列必包含长度为 $a$ 的递增子列或长度为 $b$ 的递减子列. 则

$$
N(a, b) \leq(a-1)(b-1)+1 .
$$

截至目前, 有很多关于定理 B 的不同证明. 如 Steel 在文 [2] 中收集了 7 个不同证明, 包括 Seidenberg 用抽屉原理的简短证明 [3]. 最近, 文献 [4] 也给出了定理 B 的新证明.

Erdös-Szekeres 定理因其形式优美, 描述初等直观而备受关注, 成为组合学中基本定理之一. 它有很多与几何, 凸体, 抽象组合等相关的推广, 可参见文献 $[2,4,5]$ 等. 而文献 $[6]$ 是一篇有关在凸位置处的点的 Erdös-Szekeres 定理的非常

收稿日期: 2015-11-14； 修订日期: 2016-07-15.
好的综述.

本文我们主要讨论关于单调凸序列的 Erdös-Szekeres 定理, 即考虑如下问题:

问题 1. 对任意由 $N=N(r, s)$ 个不同实数构成的序列, 均可以选出长度为 $r$ 的单调凸序列或长度为 $s$ 的单调凹序列. 则 $N=N(r, s)$ 的最小值是多少?

我们先叙述凸序列的定义.

若实数序列 $\left\{x_{n}\right\}$ 满足对任意 $k=1,2, \cdots$, 均有 $x_{k-1}+x_{k+1} \geq 2 x_{k}$, 则称序列 $\left\{x_{n}\right\}$ 是凸序列. 若实数序列 $\left\{x_{n}\right\}$ 满足 $x_{k-1}+x_{k+1} \leq 2 x_{k}, k=1,2, \cdots$, 则称序列 $\left\{x_{n}\right\}$ 是凹序列.

本文我们证明了如下结果:

定理 1. 设 $r, s$ 为正整数, 令 $N(r, s)$ 表示满足下列条件的 $N$ 的最小整数:对任意由 $N$ 个不同实数构成的序列, 均可以选出长度为 $r$ 的单调凸序列或长度为 $s$ 的单调凹序列. 则

$$
N(r, s)=\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)^{2}+1
$$

## 2. 主要结果证明

为证明定理 1 , 我们需要先证明下面一些引理.

引理 1 (Erdös-Szekeres). 设 $m, n$ 为正整数,则任意由 $m n+1$ 个不同实数构成的数列 $a_{1}, \cdots, a_{m n+1}$ 必包含长为 $m+1$ 的递增子列或长为 $n+1$ 的递减子列。

引理 1 即定理 $\mathrm{B}$, 证明可参阅文 $[3,7]$.

类似于 Ramsey 数 $[8]$ 的定义, 对若干个实数构成的序列 $A$, 记 $P(A), Q(A)$分别为从 $A$ 中选出的凸子列与凹子列的最大长度, 记 $r(p, q)$ 为使 $P(A)=$ $p, Q(A)=q$ 的最长不减序列 $A$ 的长度. 称 $r(p, q)$ 为 Ramsey 数.

由定义, 当 $n \geq 2$ 时, $r(n, 2)=r(2, n)=n$.

对于 Ramsey 数 $r(p, q)$, 我们有如下结论.

引理 2. 当 $p \geq 2, q \geq 2$ 时, Ramsey 数 $r(p, q)$ 满足

$$
r(p, q)=r(p-1, q)+r(p, q-1) \text {. }
$$

证明 一方面, 设 $B$ 为使 $P(B)=p-1, Q(B)=q$ 的一个最长不减列, 记为

$$
B=\left\{b_{1}, b_{2}, \cdots, b_{r(p-1, q)}\right\}, \quad b_{1} \leq b_{2} \leq \cdots \leq b_{r(p-1, q)}
$$

设 $C$ 为使 $P(C)=p, Q(C)=q-1$ 的一个最长不减列, 记为

$$
C=\left\{c_{1}, c_{2}, \cdots, c_{r(p, q-1)}\right\}, \quad c_{1} \leq c_{2} \leq \cdots \leq c_{r(p, q-1)} .
$$

不妨令

$$
c_{1}-b_{r(p-1, q)}>\max \left\{c_{r(p, q-1)}-c_{1}, b_{r(p-1, q)}-b_{1}\right\},
$$

否则可将 $C$ 中元素同时加上一个定值. 令 $A=B \cup C$, 从而 $|A|=|B|+|C|$, 则显然满足 $P(A) \geq p, Q(A) \geq q$.

若 $P(A) \geq p+1$, 则 $A$ 中最长凸子列至少有 $B$ 中一项和 $C$ 中两项, 即存在 $1 \leq i \leq r(p-1, q), 1 \leq j<l \leq r(p, q-1)$, 使得 $b_{i}+c_{l} \geq 2 c_{j}$, 但注意到

$$
b_{r(p-1, q)}+c_{r(p, q-1)} \geq b_{i}+c_{l} \geq 2 c_{j} \geq 2 c_{1}>b_{r(p-1, q)}+c_{r(p, q-1)}
$$

矛盾! 故 $P(A)=p$.

同样的, 若 $Q(A) \geq q+1$, 则 $A$ 中最长凹子列至少有 $B$ 中两项与 $C$ 中一项,即存在 $1 \leq i<j \leq r(p-1, q), 1 \leq j \leq r(p, q-1)$, 使得 $b_{i}+c_{l} \leq 2 b_{j}$ ，而

$$
b_{1}+c_{1} \leq b_{i}+c_{l} \leq 2 b_{j} \leq 2 b_{r(p-1, q)}<b_{1}+c_{1},
$$

矛盾! 故 $Q(A)=q$.

故 $A$ 为使 $P(A)=p, Q(A)=q$ 的不减数列, 所以

$$
r(p, q) \geq|A|=r(p-1, q)+r(p, q-1)
$$

另一方面, 假设存在不减序列 $A$, 使得 $P(A)=p, Q(A)=q$, 且满足

$$
|A| \geq r(p-1, q)+r(p, q-1)+1 .
$$

记 $A=\left\{x_{1}<x_{2}<\cdots<x_{|A|}\right\}$.

由 Ramsey 数 $r(p, q)$ 的定义, 对

$$
x_{1}, x_{2}, \cdots, x_{r(p-1, q)+1}
$$

这 $r(p-1, q)+1$ 个数中必有长为 $p$ 的凸子列或长为 $q+1$ 的凹子列, 但 $Q(A)=q<q+1$, 故 $x_{1}, x_{2}, \cdots, x_{r(p-1, q)+1}$ 中必有长为 $p$ 的凸子列, 记为

$$
x_{i_{1}} \leq x_{i_{2}} \leq \cdots \leq x_{i_{p}}
$$

又对于 $x_{r(p-1, q)+1}, \cdots, x_{r(p-1, q)+r(p, q-1)+1}$ 这 $r(p, q-1)+1$ 个数中必有长为 $p+1$的凸子列或长为 $q$ 的凹子列, 但 $P(A)=p<p+1$, 故

$$
x_{r(p-1, q)+1}, \cdots, x_{r(p-1, q)+r(p, q-1)+1}
$$

中必有长为 $q$ 的凹子列, 记为

$$
x_{j_{1}} \leq x_{j_{2}} \leq \cdots \leq x_{j_{q}}
$$

若 $x_{1}+x_{r(p-1, q)+r(p, q-1)+1} \geq 2 x_{r(p-1, q)+1}$, 则

$$
\begin{aligned}
x_{i_{p-1}}+x_{r(p-1, q)+r(p, q-1)+1} & \geq x_{1}+x_{r(p-1, q)+r(p, q-1)+1} \\
& \geq 2 x_{r(p-1, q)+1} \\
& \geq 2 x_{i_{p}}
\end{aligned}
$$

即

$$
x_{i_{1}} \leq x_{i_{2}} \leq \cdots \leq x_{i_{p}} \leq x_{r(p-1, q)+r(p, q-1)+1}
$$

为长为 $p+1$ 的的凸子列, 与 $P(A)=p$ 的矛盾.

若 $x_{1}+x_{r(p-1, q)+r(p, q-1)+1}<2 x_{r(p-1, q)+1}$, 则

$$
x_{1}+x_{j_{2}} \leq x_{1}+x_{r(p-1, q)+r(p, q-1)+1}<2 x_{r(p-1, q)+1} \leq 2 x_{j_{1}},
$$

即 $x_{1} \leq x_{j_{1}} \leq x_{j_{2}} \leq \cdots \leq x_{j_{q}}$ 为长为 $q+1$ 的凹子列, 与 $Q(A)=q$ 矛盾.

故假设不成立, 即对任意使 $P(A)=p, Q(A)=q$ 的不减数列 $A$, 必有:

$$
|A| \leq r(p-1, q)+r(p, q-1)
$$

即

$$
r(p, q) \leq r(p-1, q)+r(p, q-1) .
$$

由 (1),(2) 可得

$$
r(p, q)=r(p-1, q)+r(p, q-1) .
$$

由引理 2 , 我们得到使 $P(A)=p, Q(A)=q$ 的不减数列 $A$ 一定是存在的, 且 $r(p, q)<\infty$.

结合引理 2, 注意到组合恒等式

$$
\left(\begin{array}{l}
n \\
r
\end{array}\right)+\left(\begin{array}{c}
n \\
r+1
\end{array}\right)=\left(\begin{array}{l}
n+1 \\
r+1
\end{array}\right)
$$

自然得到如下结果.

引理 3. 当 $p \geq 2, q \geq 2$ 时, Ramsey 数 $r(p, q)$ 满足

$$
r(p, q)=\left(\begin{array}{c}
p+q-2 \\
p-1
\end{array}\right)
$$

下面我们来证明主要定理.

定理 1. 设 $r, s$ 为正整数, 令 $N(r, s)$ 表示满足下列条件的 $N$ 的最小整数:对任意由 $N$ 个不同实数构成的序列, 均可以选出长度为 $r$ 的单调凸序列或长度为 $s$ 的单调凹序列. 则

$$
N(r, s)=\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)^{2}+1
$$

要证明定理 1 中的 (3) 式, 只需证明左侧既不小于右侧, 又不大于右侧. 即如下两个引理.

引理 4 . 所求 $N(r, s)$ 满足

$$
N(r, s) \leq\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)^{2}+1
$$

证明 当 $N=\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)^{2}+1$ 时, 记 $m=\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)+1$, 则对任意 $N$ 个实数 $x_{1}, \cdots, x_{N}$, 由引理 1, 存在

$$
1 \leq i_{1}<i_{2}<\cdots<i_{m} \leq N
$$

使得 $x_{i_{1}}, \cdots, x_{i_{m}}$ 为不增或不减的子列.

若 $x_{i_{1}}, \cdots, x_{i_{m}}$ 为不减的数列, 则当 $r^{\prime} \leq r-1, s^{\prime} \leq s-1$ 时, 由引理 3 得

$$
r\left(r^{\prime}, s^{\prime}\right) \leq r(r-1, s-1)=\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)<\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)+1 .
$$

由引理 2 知其中必有长为 $r$ 的凸子列或长为 $s$ 的凹子列, 且为单调的, 满足条件.

若 $x_{i_{1}}, \cdots, x_{i_{m}}$ 为不增的数列, 取

$$
x_{i}^{\prime}=x-x_{i}, \quad x \in \mathbb{R}, i=1,2, \cdots, N
$$

化为不减数列, 则由引理 2 得, 序列 $x_{i_{1}}^{\prime}, \cdots, x_{i_{m}}^{\prime}$ 中必有长为 $r$ 的凹子列或长为 $s$ 的凸子列, 因此序列 $x_{i_{1}}, \cdots, x_{i_{m}}$ 中必有长为 $r$ 的凸子列或长为 $s$ 的凹子列,显然也为单调的, 满足条件.
故

$$
N(r, s) \leq\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)^{2}+1
$$

引理 5 . 所求 $N(r, s)$ 满足

$$
N(r, s) \geq\left(\begin{array}{c}
r+s-4 \\
r-2
\end{array}\right)^{2}+1
$$

证明 当 $N \leq\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)^{2}$ 时, 记 $m=\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)$. 由 $r(s-1, r-1)$ 的定义及存在性知, 存在不减数列 $y_{1}, \cdots, y_{m}$, 其中凸子列最长为 $s-1$, 凹子列最长为 $r-1$.令

$$
y=y_{m}-y_{1},
$$

不妨令 $y_{1}=0$ (否则整体平移即可).

注意到引理 2 第一部分证明可加强至: 存在 $x_{1}<x_{2}<\cdots<x_{r(p, q)}$ 及 $\varepsilon>0$,使得 $2 \varepsilon<\min _{i=1, \cdots, r(p, q)-1}\left\{x_{i+1}-x_{i}\right\}$, 设

$$
T_{i}=\left[x_{i}-\varepsilon, x_{i}+\varepsilon\right], i=1, \cdots, r(p, q) \text {, }
$$

则由引理 2 , 对任意序列 $z_{1}, \cdots, z_{r(p, q)}$, 其中 $z_{i} \in T_{i}$, 最长凸子列长为 $p$, 最长凹子列长为 $q$.

同样的, 考虑当 $p=r-1, q=s-1, r(p, q)=\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)$ 时, 这样一来, 不妨令 $\varepsilon>y\left(\right.$ 否则取 $x_{i}^{\prime}=t x_{i}, \varepsilon^{\prime}=t \varepsilon, t \in \mathbf{N}^{+}$且 $t>\frac{y}{\varepsilon}$ ), 取

$$
a_{i m+j}=x_{i+1}+\varepsilon-y_{j} \quad(j=1,2, \cdots, m, i=0,1, \cdots, m-1),
$$

由此, 对 $a_{i}, \cdots, a_{N}$ 而言, 每 $\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)$ 个相邻的称为一段, 每一段均为不增的, 不同段上的点为不减的.

若存在不减的长为 $r$ 的凸子列或长为 $s$ 的凹子列, 则它们的项必两两不同段, 但此时与 $(* *)$ 处 $x_{i}$ 定义矛盾; 若存在不增的长为 $r$ 的凸子列或长为 $s$ 的凹子列, 则它们必全在一段上, 平移后即相当于数列 $y_{1}, \cdots, y_{m}$ 中有长 $r$ 的凸子列或长为 $s$ 的凹子列, 这与 $(*)$ 处 $y_{i}$ 定义矛盾. 故此时不满足条件.

由此 $N(r, s) \geq\left(\begin{array}{c}r+s-4 \\ r-2\end{array}\right)^{2}+1$.

结合引理 4 和引理 5 可知, 定理得证.

## 参考文献

[1] P. Erdös and G. Szekeres, A combinatorial problem in geometry [J], Compos. Math. 2 (1935), 463-470.

[2] J. Steele, Variations on the monotone subsequence theme of Erdös and Szekeres [J]. In Discrete probability and algorithms (Minneapolis, MN, 1993), 111-131, IMA Vol. Math. Appl., 72, Springer, New York, 1995.

[3] A. Seidenberg. A simple proof of a theorem of Erdös and Szekeres [J]. J. London Math. Soc., 34 (1959), 352.

[4] G. Moshkovitz, A. Shapira, Ramsey theory, integer partitions and a new proof of the Erdös-Szekeres theorem [J], Adv. Math. 262 (2014), 1107-1129.

[5] J. Fox, J. Pach, B. Sudakov, and A. Suk. Erdös-Szekeres-type theorems for monotone paths and convex bodies [J]. Proc. London Math. Soc., 105 (2012), 953-982.

[6] W. Morris, V. Soltan, The Erdös-Szekeres problem on points in convex position-a survey [J]. Bull. Amer. Math. Soc. 37 (2000), 437-458.

[7] 施柯杰, 冷岗松. 2015 国外组合试题评析 [J]. 数学新星网 - 教师专栏, 2015-12-30 期.

[8] R. Graham, B. Rothschild and J. Spencer, Ramsey Theory [M], 2nd ed. Wiley, New York, 1990.

