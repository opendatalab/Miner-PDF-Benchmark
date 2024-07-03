# 一道 IMO 预选题加强结果的通法与妙解 

段钦瀚

(湖南省雅礼中学, 长沙, 410007)

首先介绍一道第 34 届 IMO 预选题中的一道题:

问题 1. 如果一个 (互异) 正整数的有限集合的所有元素之和是集合中所有数的公倍数, 则称这个集合为 “和倍集”. 求证：正整数的每个有限集合都是某个和倍集的子集。

分析 我们首先对这个题有个初步判断：设集合 $M$ 的元素和为 $S(M)$, 所有元素的最小公倍数为 $T(M)$. 那么希望对于集合 $X=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$, 存在集合 $Y$ 使得 $X \subseteq Y$ 且 $T(Y) \mid S(Y)$. 虽然已经得到的已知量 $S(X), T(X)$ 并无直接关系, 但我们知道 $S(X), T(X) \geq \max \left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$, 为了保证加入的元素与 $X=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$ 中的元素不重复, 故希望通过加入一些比 $S(X)$, 或 $T(X)$大的且与 $S(X), T(X)$ 有关的互不相同的数放入 $Y$ 使得 $T(Y) \mid S(Y)$. 故只需看作对于给定的正整数 $s, t$, 取数 $a_{1}, a_{2} \cdots, a_{n}$ 使得

$$
\left[t, a_{1}, a_{2}, \cdots, a_{n}\right] \mid s+\sum_{i=1}^{n} a_{i}
$$

一个好的想法是考虑 2 的幂, 这是因为 2 的幂求和直接得到的是较高次数的 2 的幂.

证明 设给定的有限集为 $S=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$ ，令

$$
s=\sum_{i=1}^{n} a_{i}, m=\left[a_{1}, a_{2}, \cdots, a_{n}\right]
$$

设 $m=2^{k} n$, 其中 $n$ 和 $k$ 都是非负整数且 $n$ 为奇数, 设 $n$ 的二进制展开式为

$$
n=\varepsilon_{0}+2 \varepsilon_{1}+\cdots+2^{t} \varepsilon_{t},
$$

其中 $\varepsilon_{i} \in\{0,1\}, i=0,1, \cdots, t$, 且 $\varepsilon_{0}=\varepsilon_{t}=1$.

将集合 $A=\left\{2^{i} s \mid 1 \leq i \leq t, \varepsilon_{i}=1\right\}$ 并入给定的集合 $S$, 于是扩充后的集合收稿日期: 2018-03-04； 修订日期: 2018-04-25.
所有数和为 $n s$. 最后, 再将集合 $\left\{2^{j} n s \mid j=0,1, \cdots, l-1\right\}, l=\max \{k, t\}$ 并入上述集合, 则所得集合 $T$ 中所有数之和为 $2^{l} n s$. 这个数被 $m$ 整除, 从而被每个 $a_{i}$ 整除, 同时又可被上述的诸 $2^{i} s, 2^{j} n s$ 整除, 故 $T$ 为和倍集.

上述方法的确可以使元素和为所有元素的公倍数, 笔者在此基础上将其加强, 希望元素和恰为所有元素的最小公倍数.

问题 2. 如果一个 (互异) 正整数的有限集合的所有元素之和是集合中所有数的最小公倍数, 则称这个集合为 “好集”. 求证：正整数的每个有限集合都是某个好集的子集。

分析 不难发现考虑 2 的幂的和得到较高次数的 2 的幂可以解决整除问题,但对于最小公倍数这一限制难以达到, 故 2 的幂可能难以保证, 我们希望通过其他手段去满足.

我们假设这个给出的集合为 $T=\left\{d_{1}, d_{2}, \cdots, d_{n}\right\}$. 设

$$
A=\left[d_{1}, d_{2}, \cdots, d_{n}\right], \quad B=\sum_{i=1}^{n} d_{i}
$$

现在要扩充集合 $T$ 使得扩充后的集合所得到的 $A=B$, 因此首先我们不妨将 $A, B$ 的公因数提出来, 即希望 $(A, B)=1$. 现在要想得到 $A=B$, 我们不妨分两步走, 第一步先保证 $A \mid B$ 或 $B \mid A$, 再进一步得到相等.

想要 $A \mid B$ 并不容易 (此即为问题 1 ), 但要保证 $B \mid A$ 很容易, 例如令新的集合为 $T \cup\{2 B, 3 B\}$, 这个集合的元素和即为 $6 B$, 且这个集合的公倍数为 $6 B$的倍数. 因此我们希望先满足 $B \mid A$.

我们假设完成第一步后新的集合为

$$
T=\left\{d_{1}, d_{2}, \cdots, d_{n}, x_{1}, x_{2}, \cdots, x_{m}\right\}
$$

设

$$
A_{1}=\left[d_{1}, d_{2}, \cdots, d_{n}, x_{1}, x_{2}, \cdots, x_{m}\right], \quad B_{1}=\sum_{i=1}^{n} d_{i}+\sum_{i=1}^{m} x_{i}
$$

且满足

$$
A_{1}=\left[d_{1}, d_{2}, \cdots, d_{n}, x_{1}, x_{2}, \cdots, x_{m}\right]=k\left(\sum_{i=1}^{n} d_{i}+\sum_{i=1}^{m} x_{i}\right)=k B_{1}, k \in \mathbb{N}^{*} .
$$

再进一步对 $T_{1}$ 扩充, 这时自然地希望扩充的元素均为 $B_{1}$ 的倍数, 从而可以提出公因数 $B_{1}$, 而提出 $B_{1}$ 后则我们可以将这一步操作看作如下命题:

命题 1. 对于任意正整数 $k$, 存在正整数 $l$ 与 $a_{1}, a_{2}, \cdots, a_{l}$ 满足如下条件:

(1) $a_{1}, a_{2}, \cdots, a_{l}, k$ 互不相等;

(2) $\left[a_{1}, a_{2}, \cdots, a_{l}, k\right]=1+\sum_{i=1}^{l} a_{i}$.

事实上, 上述的 $l$ 取为 $k+1$ 时是成立的, 可以利用加强命题的数学归纳法证明, 是一道不错的训练题. 这是这个证明的关键性引理, 但并非异想天开, 是通过推理自然得到的. 由此, 整体思路大致出来, 但还要注意保证集合的元素互异性.

下面给出笔者关于问题 2 的证明:

证法一 首先证明一个引理:

引理 对任意 $k \in \mathbb{N}^{*}$, 存在正整数 $a_{1}, a_{2}, \ldots, a_{k+1}>1$, 满足 $a_{1}, a_{2}, \cdots, a_{k+1}, k$互不相等且

$$
\left[a_{1}, a_{2}, \cdots, a_{k+1}, k\right]=1+\sum_{i=1}^{k+1} a_{i}
$$

引理证明 对 $k$ 归纳证明.

当 $k=1$ 时, 取 $a_{1}=2, a_{2}=3$ 满足题意.

当 $k=2$ 时, 取 $a_{1}=3, a_{2}=8, a_{3}=12$ 满足题意.

假设命题对 $k(k \geq 2)$ 成立, 考虑 $k+1$ 的情形:

由归纳假设, 存在 $b_{i}(i=1,2, \cdots, k+1)$ 使得 $b_{1}, b_{2}, \cdots, b_{k+1}, k$ 互不相等且满足

$$
\left[b_{1}, b_{2}, \cdots, b_{k+1}, k\right]=\sum_{i=1}^{k+1} b_{i}+1
$$

令 $a_{i}=(k+1) b_{i}, i=1,2, \cdots, k+1, a_{k+2}=k$, 则显然有

$$
a_{i} \geq k \geq 2>1(1 \leq i \leq k+2)
$$

因为 $b_{1}, b_{2}, \cdots, b_{k+1}$ 互不相等且均大于 1 , 所以 $a_{1}, a_{2}, \cdots, a_{k+2}, k+1$ 互不相等. 从而

$$
\begin{aligned}
\sum_{i=1}^{k+2} a_{i}+1 & =\sum_{i=1}^{k+1}(k+1) b_{i}+k+1=(k+1)\left(\sum_{i=1}^{k+1} b_{i}+1\right) \\
& =(k+1)\left[b_{1}, b_{2}, \cdots, b_{k+1}, k\right]=\left[a_{1}, a_{2}, \cdots, a_{k+1}, k(k+1)\right] \\
& =\left[a_{1}, a_{2}, \cdots, a_{k+1}, k, k+1\right]=\left[a_{1}, a_{2}, \cdots, a_{k+1}, a_{k+2}, k+1\right]
\end{aligned}
$$

因此命题对 $k+1$ 成立, 由归纳原理, 引理获证.

回到原题. 对于给定的正整数集合 $T=\left\{d_{1}, d_{2}, \cdots, d_{n}\right\}$. 设

$$
A=\left[d_{1}, d_{2}, \cdots, d_{n}\right], \quad B=\sum_{i=1}^{n} d_{i}, \quad D=(A, B), \quad m=\frac{A}{D}, \quad l=\frac{B}{D},
$$

则 $(m, l)=1$.
当 $n=1$ 时 $T$ 显然为好集, 考虑 $n \geq 2$ 的情况, 则 $B>d_{i}(1 \leq i \leq n)$.

情形 1 : 当 $m \geq 2$ 时, 由引理, 取 $k=m-1$, 则 $k \in \mathbb{N}^{*}$, 故存在 $a_{1}, a_{2}, \cdots, a_{m} \in \mathbb{N}^{*} \backslash\{1\}$ 满足 $a_{1}, a_{2}, \cdots, a_{m}, m-1$ 互不相等且

$$
\left[a_{1}, a_{2}, \cdots, a_{m}, m-1\right]=\sum_{i=1}^{m} a_{i}+1
$$

令 $R=\left\{d_{1}, d_{2}, \cdots, d_{n},(m-1) B, m B a_{1}, m B a_{2}, \cdots, m B a_{m}\right\}$, 则 $T \subset R$ 且 $R$ 为好集. 事实上, 由于 $B>d_{i}(1 \leq i \leq n), m \geq 2$, 故

$$
m B a_{j}>(m-1) B>d_{i}(1 \leq i \leq n, 1 \leq j \leq m) .
$$

又正整数 $a_{1}, a_{2}, \cdots, a_{m}$ 互不相同, 故 $R$ 中元素互不相等.

设 $R$ 的所有元素的最小公倍数为 $A_{R}$, 所有元素和为 $B_{R}$. 由于 $m=\frac{A}{D}, l=$ $\frac{B}{D},(m, m-1)=(m, l)=1$, 则有

$$
\begin{aligned}
A_{R} & =\left[d_{1}, d_{2}, \cdots, d_{n},(m-1) B, m B a_{1}, m B a_{2}, \cdots, m B a_{m}\right] \\
& =\left[\left[d_{1}, d_{2}, \cdots, d_{n}\right],(m-1) B, m B a_{1}, m B a_{2}, \cdots, m B a_{m}\right] \\
& =\left[A,(m-1) B, m B a_{1}, m B a_{2}, \cdots, m B a_{m}\right] \\
& =D\left[m,(m-1) l, m l a_{1}, m l a_{2}, \cdots, m l a_{m}\right] \\
& =D\left[m(m-1) l, m l a_{1}, m l a_{2}, \cdots, m l a_{m}\right] \\
& =D m l\left[m-1, a_{1}, a_{2}, \cdots, a_{m}\right]=D m l\left(1+\sum_{i=1}^{m} a_{i}\right) \\
& =B+\left(\frac{A}{D}-1\right) B+m B \sum_{i=1}^{m} a_{i}=B_{R} .
\end{aligned}
$$

情形 2 : 当 $m=1$ 时, 则 $A=D, A \mid B$. 设

$$
w=\frac{A(A+1)}{2}, \quad B=t A, \quad t \in \mathbb{N}^{*} \text {. }
$$

当 $t=1$ 时 $T$ 即为好集. 考虑 $t \geq 2$ 的情况.

由引理, 取 $k=w$, 则存在 $b_{1}, b_{2}, \cdots, b_{m+1} \in \mathbb{N}^{*} \backslash\{1\}$ 满足 $b_{1}, b_{2}, \cdots, b_{w+1}, w$互不相等且满足 $\left[b_{1}, b_{2}, \cdots, b_{w+1}, w\right]=1+\sum_{j=1}^{w+1} b_{j}$. 令

$$
S=\left\{d_{i}, t(A+1), t(2 A+1), 2 t(2 A+1) b_{j}(1 \leq i \leq n, 1 \leq j \leq w+1)\right\} \text {, }
$$

则 $T \subset S$ 且 $S$ 为好集.

事实上, 由于正整数 $b_{1}, b_{2}, \cdots, b_{w+1}$ 均大于 1 且互不相等, 又

$$
2 t(2 A+1) b_{j}>2 t(2 A+1)>t(2 A+1)>t(A+1)>A \geq d_{i},
$$

这里 $1 \leq i \leq n, 1 \leq j \leq w+1$, 故 $S$ 中的元素两两不同.
设 $S$ 的所有元素的最小公倍数为 $A_{S}$, 所有元素和为 $B_{S}$.

由于 $A, A+1,2 A+1$ 两两互质, $w=\frac{A(A+1)}{2}, B=t A$, 因此

$$
\begin{aligned}
A_{s} & =\left[A, t(A+1), t(2 A+1), 2 t(2 A+1) b_{1}, 2 t(2 A+1) b_{2}, \cdots, 2 t(2 A+1) b_{w+1}\right] \\
& =\left[t A(A+1)(2 A+1), 2 t(2 A+1) b_{1}, 2 t(2 A+1) b_{2}, \cdots, 2 t(2 A+1) b_{w+1}\right] \\
& =2 t(2 A+1)\left[w, b_{1}, b_{2}, \cdots, b_{w+1}\right]=2 t(2 A+1)\left(1+\sum_{j=1}^{w+1} b_{j}\right) \\
& =t A+t(A+1)+t(2 A+1)+2 t(2 A+1) \sum_{j=1}^{w+1} b_{j} \\
& =B+t(A+1)+t(2 A+1)+2 t(2 A+1) \sum_{j=1}^{w+1} b_{j}=B_{s}
\end{aligned}
$$

综上所述, 命题成立.

评注 对于上述证明, 需要做出如下两点解释:

(1) 情形 2 的讨论是必要的, 因为存在某个 $d_{i}=A$ 的特殊情形.

(2) 引理中 $a_{1}, a_{2}, \cdots, a_{k+1}>1$ 原因如下: 如果存在 $b_{i}(i=1,2, \cdots, k+1)$使得 $b_{1}, b_{2}, \cdots, b_{k+1}, k$ 互不相等且满足 $b_{1}=1,\left[b_{1}, b_{2}, \cdots, b_{k+1}, k\right]=\sum_{i=1}^{k+1} b_{i}+1$.则递归构造后由于 $a_{1}=(k+1) b_{1}=k+1$, 这与 $a_{1}, a_{2}, \cdots, a_{k+2}, k+1$ 互不相等矛盾.

为了保证 $a_{1}, a_{2}, \cdots, a_{k+1}>1$, 奠基必须要有 $k=2$ 的情形, 否则由 $k=1$推到 $k=2$ 时构造得到 $a_{3}=1$.

下面介绍关于问题 2 的另一个解答.

这里感谢肖澍旸同学给作者提供了一个精巧简洁的妙解, 这个做法很好地利用了 $A_{m}^{n}\left(A_{m}^{n}=\frac{m !}{(m-n) !}\right.$ 表示从 $m$ 个不同的数中取 $n$ 个数的排列的个数, 这里 $m \geq n)$ 差分形式的整除性质, 从而确定了最小公倍数.

## 证法二 (雅礼中学 肖澍旸)

设给定的正整数有限集合为 $D=\left\{d_{1}, d_{2}, \cdots, d_{n}\right\}$, 设 $S=\sum_{i=1}^{n} d_{i}, T=\prod_{i=1}^{n} d_{i}$.

若 $T \leq 2$, 则 $D=\{1\}$ 或 $\{2\}$ 或 $\{1,2\}$. 由 $1+2+3=[1,2,3]$, 故 $\{1,2,3\}$为好集, 成立.

若 $T \geq 3$, 则 $6 \mid T$ !. 令

$$
K=D \cup\left\{\left(A_{T}^{1}-A_{T}^{0}\right) S,\left(A_{T}^{2}-A_{T}^{1}\right) S, \cdots,\left(A_{T}^{T-1}-A_{T}^{T-2}\right) S\right\}
$$

下面证明 $K$ 为好集. 显然 $K$ 中元素互不相等.

设 $K$ 的所有元素的和为 $S_{K}$, 所有元素的最小公倍数为 $T_{K}$.
一方面，

$$
S_{K}=\sum_{i=1}^{n} d_{i}+\sum_{i=1}^{T-1}\left(A_{T}^{i}-A_{T}^{i-1}\right) S=S+\left(A_{T}^{T-1}-A_{T}^{0}\right) S=S \cdot T !
$$

另一方面, 当 $m=1,2, \cdots, T-1$ 时, 由于

$$
\begin{aligned}
A_{T}^{m}-A_{T}^{m-1} & =T(T-1) \cdots(T-m+1)-T(T-1) \cdots(T-m+2) \\
& =T(T-1) \cdots(T-m+2)(T-m)
\end{aligned}
$$

所以 $A_{T}^{m}-A_{T}^{m-1} \mid T !$, 又由于 $d_{i} \mid T$ ! , 从而

$$
T_{K} \mid S \cdot T !, T_{K} \leq S \cdot T !
$$

又由于 $T \geq 3,6 \mid T$ !, 故

$$
\left[\left(A_{T}^{T-1}-A_{T}^{T-2}\right) S,\left(A_{T}^{T-2}-A_{T}^{T-3}\right) S\right]=\left[\frac{1}{2} S \cdot T !, \frac{1}{3} S \cdot T !\right]=S \cdot T !
$$

从而

$$
S \cdot T ! \mid T_{K}, T_{K} \geq S \cdot T !
$$

结合 (1),(2) 知 $T_{k}=T ! \cdot S$.

因此 $T_{k}=S \cdot T !=S_{K}$, 故 $K$ 为好集. 证毕!

评注 可以看出, 这一构造极具巧思, 利用的东西并不多, 但需要对排列数足够熟悉, 构造很见功力. 可以见得妙解一般十分精巧, 但难以想到. 因此我们在欣赏妙解的同时还应去寻找通法.

最后感谢读者的阅读, 文中如有不恰当或错误之处, 希望读者不吝指正.

