# 从等差数列到凸数列 

冷岗松胡珏伟

(上海大学, 200444)

编者按：本文是在第一作者十多年前一个讲义的基础上由第二作者整理修改而成。

围绕着等差数列一一种最简单和最重要的数列, 一些杰出的数学家谱写新的传奇. 其中关于等差数列的有名的范德瓦尔登 (Vander Waerden) 定理被誉为数论的 “三颗明珠” 之一. 菲尔兹奖获得者陶哲轩因证明了 “素数中存在任意长的等差数列” 这一非凡结论, 使数学界一度为之振奋.

本文回归等差数列的初等认识, 收集了不少关于等差数列的有趣问题, 并研究了等差数列的推广一凸数列中的若干问题.

## 1. 寻找等差数列

例 1 对任意的正整数 $n$, 问无穷序列 $1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \cdots$ 中是否存在 $n$ 项的等差数列?

解 答案是肯定的, 可以直接构造出 $n$ 项的等差数列:

$$
\frac{1}{n !}, \frac{2}{n !}, \cdots, \frac{n-1}{n !}, \frac{n}{n !}
$$

在例 1 的基础上, 并注意到等比数列取对数后即为等差数列, 我们可以提出下面的问题.

例 2 设 $a>1$, 考虑无穷集合

$$
A=\{\sqrt{a}, \sqrt[3]{a}, \sqrt[4]{a}, \cdots\}
$$

(1) 对任给的正整数 $n$, 问 $A$ 是否包含一个 $n$ 项的等比数列?

(2) 问 $A$ 是否包含一个无穷项的等比数列?
解 (1) 要在 $a^{\frac{1}{2}}, a^{\frac{1}{3}}, a^{\frac{1}{4}}, \cdots$ 中找 $n$ 项的等比数列, 等价于要在 $\frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \cdots$ 序列中找 $n$ 项的等差数列. 由例 1 , 我们便马上构造出 $n$ 项的等比数列

$$
a^{\frac{1}{n !}}, a^{\frac{2}{n !}}, \cdots, a^{\frac{n-1}{n !}}, a^{\frac{n}{n !}} .
$$

(2) 答案是否定的. 若不然, 设存在一个以 $x_{1}$ 为首项, 公比为 $q$ 的无穷项的等比数列. 注意到 $A \subset(1, \sqrt{a}]$, 我们有

$$
1 \leq x_{1} q^{n} \leq \sqrt{a}
$$

其中 $x_{1} \geq 1, q>0, q \neq 1$.

如果 $0<q<1$, 则对上式左边的不等式令 $n \longrightarrow \infty$ 便得矛盾.

如果 $q>1$, 则对上式右边的不等式令 $n \longrightarrow \infty$ 便得矛盾.

例 2 还可推广到更一般的情况如下:

例 3 设 $a>1, a_{1}, a_{2}, \cdots, a_{n}, \cdots$ 是一个无穷的由正整数组成的非常数的等差数列, 考虑

$$
A=\left\{a^{\frac{1}{a_{1}}}, a^{\frac{1}{a_{2}}}, a^{\frac{1}{a_{3}}}, \cdots\right\} .
$$

(1) 对任给的正整数 $n$, 问 $A$ 是否包含一个 $n$ 项的等比数列?

(2) 问 $A$ 是否包含一个无穷项的等比数列?

解 (1) 设等差数列 $\left\{a_{n}\right\}_{n=1}^{\infty}$ 的公差为 $d$, 记

$$
N=a_{1}(1+d)(1+2 d) \cdots(1+(n-1) d) \text {, }
$$

则

$$
N, \frac{N}{1+d}, \frac{N}{1+2 d}, \cdots, \frac{N}{1+(n-1) d}
$$

都是 $\left\{a_{n}\right\}$ 中的项, 这是因为它们都具有 $a_{1}+k d$ 的形式. 这样

$$
\frac{1}{N}, \frac{1+d}{N}, \frac{1+2 d}{N}, \cdots, \frac{1+(n-1) d}{N}
$$

就是 $\frac{1}{a_{1}}, \frac{1}{a_{2}}, \frac{1}{a_{3}}, \cdots$ 中 $n$ 项的等差数列. 因此 $a^{\frac{1}{N}}, a^{\frac{1+d}{N}}, a^{\frac{1+2 d}{N}}, \cdots, a^{\frac{1+(n-1) d}{N}}$ 就是 $A$ 中 $n$ 项的等比数列.

(2) 的解法完全同于例 2, 留给读者练习.

意犹未尽, 注意到 $A$ 中元素实际上是指数函数 $f(x)=a^{\frac{1}{x}}$ 在 $x=1,2, \cdots$ 的函数值, 如果我们换一个函数, 即考虑幂函数 $f(x)=x^{k}$ 在 $x=1,2, \cdots$ 处的值, 也即考虑无穷集合 $B=\left\{1^{k}, 2^{k}, 3^{k}, \cdots\right\}$. 我们有什么结果呢?

显见 $B$ 中既存在任意有限项的等比数列, 也存在无穷项的等比数列, 如 $\left\{2^{k}\right.$, $\left.4^{k}, 8^{k}, \cdots\right\}$. 那么 $B$ 中是否存在等差数列呢? 下面的第一个问题就自然产生了:
问题 设无穷集合 $B=\left\{1^{k}, 2^{k}, 3^{k}, \cdots\right\}(k \geq 2)$ 中是否存在有限项的等差数列?

当 $k=2$ 时, 显然存在三项的等差数列 $\{1,25,49\}$, 但不存在 4 项的等差数列. 当 $k \geq 3$ 时, 问题等价于方程 $x^{k}+y^{k}=2 z^{k}$ 是否有正整数解? 答案是没有正整数解, 但证明却是十分困难的. 它和著名的费马大定理有等同的难度, 它是在怀尔斯 (Wiles) 解决费马大定理后, 由 Diamond 和 Ribet 合作证明的, 现被称作 Diamond-Ribet 定理. 这可参看他们的论文 “ $l$-adic modular deformations and Wiles's main conjecture”，刊登在专著 Modular forms and Fermat's lats theorem (Boston,MAa,1995)357-371,Springer,New York,1997. 当然对集合 B 除了这个高深的问题, 另一个问题却是简单而有趣的, 这就是下面的例 4.

例 4 问集合 $B=\left\{1,2^{k}, 3^{k}, \cdots\right\}(k \geq 2)$ 中是否存在无穷项的等差数列.

解 答案是否定的. 若不然, 假设存在一个公差为 $d$ 的无穷等差数列 $\left\{a_{n}\right\} \subset$ $B$. 当 $n>d$, 则

$$
(n+1)^{k}-n^{k} \geq 2 n+1>d .
$$

这说明 $B$ 中从某一项起后面的任何两项之差均大于 $d$, 矛盾!

把等差数列与等比数列交织在一起的一些问题, 也是十分有趣的. 我们仍然从简单的开始.

例 5 正整数的无穷等差数列 $\left\{a_{n}\right\}$ 中是否一定包含一个无穷的等比数列?

解 答案是肯定的. 不妨设这个等差数列 $\left\{a_{n}\right\}$ 的首项为 $a$, 公差为 $d$.

(1) 若 $d=0$, 则原等差数列是常数列, 结论显然成立;

(2) 若 $d \neq 0$, 这时注意到

$$
a(1+d)^{k}=a(1+A d)=a+B d \in\{a+n d\}
$$

其中 $A, B$ 为非负整数. 因此子序列 $\left\{a(1+d)^{k}\right\}$ 就是所求的等比数列.

这个问题的思想可用在下面稍难一些问题的解中.

例 6(1999 年罗马尼亚国家队选拔考试试题) 证明: 对任何正整数 $n(n \geq 3)$,存在 $n$ 个正整数的等差数列 $a_{1}, a_{2}, \cdots, a_{n}$ 和 $n$ 个正整数的等比数列 $b_{1}, b_{2}, \cdots, b_{n}$满足

$$
b_{1}<a_{1}<b_{2}<a_{2}<\cdots<b_{n}<a_{n} .
$$

证明 只要构造出满足条件的正有理等差数列和正有理等比数列, 然后将它们同乘以一个适当的倍数便得到了符合条件的正整数列.
考虑序列

$$
B_{k}=\left(1+\frac{1}{m}\right)^{k}, \quad k=1,2, \cdots, n
$$

其中 $m$ 为待定的正整数.

显然 $B_{k}$ 是一个等比数列, 且当 $k \geq 2$ 时,

$$
B_{k}>1+\frac{k}{m}
$$

另一方面, $k \leq n$, 选取 $m>n^{2}$ 的正整数, 则

$$
\begin{aligned}
B_{k} & =1+\frac{k}{m}+\frac{k(k-1)}{2 ! m^{2}}+\cdots+\frac{k !}{k ! m^{k}} \\
& \leq 1+\frac{k}{m}+\frac{n(n-1)}{2 ! m^{2}}+\cdots+\frac{n(n-1) \cdots(n-k+1)}{k ! m^{k}} \\
& =1+\frac{k}{m}+\frac{1}{m}\left[\frac{1}{2 !} \cdot \frac{n(n-1)}{m}+\cdots+\frac{1}{k !} \cdot \frac{n(n-1) \cdots(n-k+1)}{m^{k-1}}\right] \\
& <1+\frac{k}{m}+\frac{1}{m}\left(\frac{1}{2 !}+\cdots+\frac{1}{k !}\right) \\
& <1+\frac{k+1}{m},
\end{aligned}
$$

上式的最后一步用到了一个著名的简单不等式:

$$
\frac{1}{2 !}+\frac{1}{3 !}+\cdots+\frac{1}{k !}<1(k \geq 2)
$$

现在我们对上面选定的 $m>n^{2}$, 令 $A_{k}=1+\frac{k+1}{m}, k=1,2, \cdots, n$, 则 $A_{k}$ 是等差数列, 且有

$$
B_{1}<A_{1}<B_{2}<A_{2}<\cdots<B_{n}<A_{n} .
$$

再令 $a_{k}=m^{n} A_{k}, b_{k}=m^{n} B_{k}$, 则 $\left\{a_{n}\right\},\left\{b_{n}\right\}$ 分别是 $n$ 个正整数的等差数列和等比数列且满足

$$
b_{1}<a_{1}<b_{2}<a_{2}<\cdots<b_{n}<a_{n} .
$$

在正整数被分类后, 从某一类中发现等差数列的最有效工具就是著名的范德瓦尔登定理. 较粗略的范德瓦尔登定理可叙述为: 如果正整数 $\mathbb{Z}^{+}$被分划成有限种颜色类, 则存在任意长的同色等差数列. 较精确的范德瓦尔登定理可叙述为 “对任意给定的正整数 $N$ 和 $l$, 存在 $W(l, N)$ 使得当 $n>W(l, N)$ 时集合 $\{1,2, \cdots, n\}$ 被 $N$ 染色后一定存在 $l$ 项的等差数列”. 这里我们仅介绍前一定理的一个有趣应用.

例 7 将平面上的所有整点染红色和蓝色之一, 问是否存在顶点同色且边长比属于 $\left\{1, \frac{1}{2}, \frac{1}{3}, \frac{2}{3}\right\}$ 的矩形?
解 存在.

由于 $x$ 轴上的所有整点也均被两染色, 故由范德瓦尔登定理, 存在其上的同色的四个整点 $A_{i}\left(x_{i}, 0\right), i=1,2,3,4$ 且满足

$$
x_{2}-x_{1}=x_{3}-x_{2}=x_{4}-x_{3}=k, \quad k \in \mathbb{Z}^{+}
$$

不妨设这四点均为红色. 考虑直线 $y=k$ 上的四点

$$
B_{i}\left(x_{i}, k\right), \quad i=1,2,3,4 .
$$

若 $B_{i}$ 中两点为红色, 则结论已成立. 否则其中至少有三点为蓝色, 不妨设为 $B_{1}, B_{2}, B_{3}$. 此时考虑直线 $y=2 k$ 上的三点

![](https://cdn.mathpix.com/cropped/2024_02_26_7aed7f2acd4cf9c98231g-05.jpg?height=439&width=460&top_left_y=934&top_left_x=792)

由抽庹原理知其中必有两点同色. 若为红色, 则与对应的 $A_{i}$ 点构成满足条件的红色矩形; 若为蓝色, 则与对应的 $B_{i}$ 构成满足条件的蓝色矩形. 故总存在顶点同色的满足条件的矩形.

有时候我们也通过计数说明某些类中不存在等差数列.

例 8 设集合 $A=\{1,2, \cdots, 2005\}$, 对 $A$ 中的数进行两染色. 证明: 存在一种染色方法使 $A$ 中任何 18 项的等差数列一定存在包含两种颜色的数.

解 先计算 $\{1,2, \cdots, 2005\}$ 中包含的长 18 的等差数列的个数.

设这个等差数列为

$$
a, a+d, \cdots, a+17 d, \quad\left(a, d \in \mathbb{Z}^{+}\right)
$$

它们完全由满足条件

$$
1 \leq a \leq a+17 d \leq 2005
$$

的整数 $a, d$ 决定. 对固定的 $d, a$ 有 $2005-17 d$ 种取法, 而 $d$ 可从 1 取到 $\left[\frac{2005-1}{17}\right]=$ 117 , 故长为 18 的等差数列共有

$$
\sum_{d=1}^{117}(2005-17 d)=117234
$$

个.

另一方面, 将集合 $A$ 两染色, 有 $2^{2005}$ 种方式, 每一个长为 18 项数列中, 会有

$$
2 \cdot 2^{2005-18}=2^{2005-17}
$$

种染色方式使得它是一个同色的 18 项序列 (因为每一个不在 18 项序列中的数可任意染两色之一, 没有限制, 而整个同色的 18 项序列有两种颜色). 因此使得存在 18 项同色等差数列的染色方法数共计为

$$
117234 \times 2^{2005-17}
$$

个. 因 $2^{17}>117234$, 所以有

$$
117234 \times 2^{2005-17}<2^{2005} \text {. }
$$

故必定有一种染色方式, 其中不包含长为 18 项的同色等差数列.

评注 上面的计算方法说明 2005 可改进. 笔者认为用计算来研究存在性问题的手法值得注意, 但这种手法似乎是比较粗䊁的, 因此很难正面的导出存在同色等差数列的结论.

## 2. 等差数列的数论问题

正整数的等差数列当然可以演绎出形形色色的数论问题和组合数论问题.这方面的例子是丰富的, 下面精选几个予以介绍. 至于用到的数论定理, 下面仅列出结果. 如果您想更深入了解它们, 请参考余红兵 《奥数教程第三册》和 《数学竟赛中的数论问题》两书, 两书均由华东师大出版社出版.

先看一个简单的例子,

例 9 设 $m>1$ 是一个正整数, 一个正整数的等差数列 $\{a+n d\}\left(a, d \in \mathbb{N}^{*}\right)$ 的公差 $d$ 与 $m$ ! 互质. 证明 $\{a+n d\}$ 中 $m$ 个连续项的乘积一定被 $m$ ! 整除.

我们的求解中要用到著名的 Legendre 公式: 设 $p$ 是任意一个素数, 则 $p$ 在 $n !$ 中的幂次等于

$$
\left[\frac{n}{p}\right]+\left[\frac{n}{p^{2}}\right]+\left[\frac{n}{p^{3}}\right]+\cdots
$$

由于当 $p^{l}>n$ 时, $\left[\frac{n}{p^{l}}\right]=0$, 故这个和式中只有有限多个项非零.

证明 任取 $p$ 是 $m$ ! 的素因子, 则由 Legendre 公式知 $p$ 在 $m$ ! 的幂次等于

$$
\left[\frac{m}{p}\right]+\left[\frac{m}{p^{2}}\right]+\left[\frac{m}{p^{3}}\right]+\cdots
$$

注意到, 对 $i=1,2, \cdots$,

$$
a, a+d, \cdots, a+(m-1) d, \quad(\text { 其中 }(d, p)=1)
$$

中被 $p^{i}$ 整除的项至少为 $\left[\frac{m}{p^{i}}\right]$ 项. 因此乘积

$$
P=a(a+d)(a+2 d) \cdots(a+(m-1) d)
$$

中含 $p$ 的幂次至少为

$$
\left[\frac{m}{p}\right]+\left[\frac{m}{p^{2}}\right]+\left[\frac{m}{p^{3}}\right]+\cdots .
$$

这说明这个乘积含 $p$ 的幂次不少于 $m$ ! 中含 $p$ 的幂. 故 $m ! \mid P$.

下面是 E.Just 在 Math.Magazine 上提出的一个问题.

例 10 设等差数列 $\{a+b n\}(n \geq 1, a, b$ 都是正整数 $)$ 包含了一个整数的 $k$ 次幂. 证明: 对任意正整数 $m>0,\{a+b n\}$ 中有无穷项可表示成 $m$ 个非零整数的 $k$次幕的和.

证明 由已知存在正整数 $N$ 和 $t$ 使得

$$
a+b N=t^{k}
$$

现任意选定 $m$ 个正整数 $s_{1}, s_{2}, \cdots, s_{m}$, 并考虑下面的和式

$$
S=\left(b s_{1}+t\right)^{k}+\sum_{j=2}^{m}\left(b s_{j}\right)^{k}
$$

则

$$
S \equiv t^{k} \equiv a+b N \equiv a \quad(\bmod b) .
$$

这样由 $S \equiv a(\bmod b)$ 知存在 $n$ 使得 $S=a+b n$, 因此 $S$ 是等差数列 $\{a+b n\}$ 中的项, 且由 (1) 知它是 $m$ 个非零整数的和. 只要不断改变参数 $s_{1}, s_{2}, \cdots, s_{n}$ 的取值, 使得 $S$ 单调递增, 这样便得到 $\{a+b n\}$ 中的无穷项具有要求性质.

下面有趣的问题来自 G.Pólya, G.Segó 的名著中.

例 11 设 $a, d$ 是给定的非零的整数, 证明无穷等差数列 $a, a+d, a+2 d, \cdots$ 中一定有无穷多项有相同的素因子.

这里的解答要用到数论中著名的欧拉定理: 设 $n>1$ 为整数, $a$ 是与 $n$ 互素的任一整数, $\varphi(n)$ 为欧拉函数 (即 $\varphi(n)$ 是 $1,2, \cdots, n-1$ 中与 $n$ 互素的数的个数), 则

$$
a^{\varphi(n)} \equiv 1 \quad(\bmod n)
$$

证明 不妨设 $(a, d)=1, d \geq 1, a>d$. 由欧拉定理

$$
a^{\varphi(d)} \equiv 1 \quad(\bmod d),
$$

可得

$$
a^{k \varphi(d)} \equiv 1 \quad(\bmod d) .
$$

对所有的整数 $k \geq 1$ 成立.

上式也可重写为

$$
a^{k \varphi(d)}=1+m_{k} d,
$$

其中 $m_{k}$ 是某个正整数.

现令 $n_{k}=a m_{k}, k \geq 1$, 则我们有

$$
a+n_{k} d=a^{k \varphi(d)+1} .
$$

这个等式说明 $a$ 的任一个素因子一定是 $\{a+n d\}$ 的无穷子序列 $\left\{a+n_{k} d\right\}$ 的所有项的因子, 结论得证.

下面的问题属于 G.Cantor.

例 12 已知 $n(n \geq 3)$ 个素数形成一个公差为 $d$ 的等差数列, 证明对任何素数 $p<n$ 有 $p \mid d$.

证明 因这个素数组成的等差数列的项数 $\geq 3$, 故公差 $d$ 一定是偶数, 由此知它的首项也必须是奇数 (即不能等于 2), 也就是这个序列的所有项都必须是奇数.

设 $p_{1}<p_{2}<\cdots<p_{k}$ 是小于 $n$ 的所有素数, 我们将对 $p_{i}$ 的下标用归纳法来证明题中结论.

当 $i=1$ 时, $p_{1}=2$, 当然有 $p_{1} \mid d$. 现假设 $p_{1}, p_{2}, \cdots, p_{i-1}$ 都整除 $d$, 下证明 $p_{i} \mid d$.

设 $a, a+d, a+2 d, \cdots, a+(n-1) d$ 是由 $n$ 个素数组成的等差数列. 如果 $p_{2}=$ 3 是这个序列中的项，它必是这个序列中的第一项; 当 $i \geq 3$ 时，由归纳假设有不等式 $d>p_{1} p_{2} \cdots p_{i-1}>p_{i}$, 这时如果 $p_{i}$ 是这个序列中的项, 它也必须是第一项. 但如果 $a=p_{i}$, 则 $a+p_{i} d$ 也是这个序列的项, 它有因子 $p_{i}$, 与它是素数矛盾. 因此 $a \neq p_{i}$. 这样素数 $a, a+d, a+2 d, \cdots, a+\left(p_{i}-1\right) d$ 除以 $p_{i}$ 的余数的取值范围为 $\left\{1,2, \cdots, p_{i}-1\right\}$. 由抽庹原理知, 必有两个的余数相等. 也即有 $s, t \in\left\{1,2, \cdots, p_{i}-1\right\}$ 满足

$$
a+s d \equiv a+t d \quad\left(\bmod p_{i}\right) .
$$

因此 $a+s d-a-t d=(s-t) d$ 被 $p_{i}$ 整除, 但 $|s-t|<p_{i}$, 我们便得 $p_{i} \mid d$.

例 13(1997 年第 38 届 IMO 预选题) 一个正整数的无穷等差数列, 包含一项是整数的平方, 另一项是整数的立方.

证明: 此数列含有一项是整数的六次幂.

此题是一个十分优雅的问题, 但当时选题委员会提供的解答是冗长且乏味的 (国内几个出版物更是完全搬用). 下面我们介绍一个较简单和直接的解法.

证明 设 $a, d$ 分别是这个等差数列的首项和公差, $r$ 是 $a, d$ 的最大公因子, 即 $r=(a, d)$. 记

$$
a=r b, d=r q, b, q \in \mathbb{N}^{*}
$$

由条件知存在 $i, j, x, y \in \mathbb{N}^{*}$ 满足

$$
a+i d=x^{2}, a+j d=y^{3},
$$

即

$$
r(b+i q)=x^{2}, r(b+j q)=y^{3} .
$$

这样, 对任意的正整数 $u, v$, 我们有

$$
r^{3 u}(b+i q)^{3 u}=x^{6 u}, r^{2 v}(b+j q)^{2 v}=y^{6 v} .
$$

将这两个等式相乘可得

$$
r^{3 u+2 v}(b+i q)^{3 u}(b+j q)^{2 v}=x^{6 u} \cdot y^{6 v}=\left(x^{u} y^{v}\right)^{6}=n^{6}
$$

其中 $n=x^{u} y^{v}$.

又注意到

$$
(b+i q)^{3 u}(b+j q)^{2 v}=b^{3 u+2 v}+c q,
$$

其中 $c$ 是一个正整数.

因此我们得到

$$
r^{3 u+2 v}\left(b^{3 u+2 v}+c q\right)=n^{6}
$$

注意到 $(b, q)=1$, 用欧拉定理知对任意正整数 $k$ 有

$$
b^{6 k \varphi(q)+1}=b^{6 k \varphi(q)} \cdot b=(1+l q) b=b+b l q
$$

其中 $l$ 是一个正整数.

现在用到一个明显的事实: 每一个正整数 $z \geq 7$ 都可写成 $z=3 u+2 v(u, v>$
$0)$ 的形式. 这样存在正整数 $u, v$ 使得

$$
6 k \varphi(q)+1=3 u+2 v .
$$

对于这样选取的 $u, v,(2)$ 的左边可化为

$$
\begin{aligned}
r^{3 u+2 v}\left(b^{3 u+2 v}+c q\right) & =r^{6 k \varphi(q)+1}\left(b^{6 k \varphi(q)+1}+c q\right) \\
& =r^{6 k \varphi(q)} \cdot r(b+b l q+c q) \\
& =m^{6} \cdot r(b+B q)
\end{aligned}
$$

其中 $m=r^{k \varphi(q)}, B=b l+c$.

这样由 (2) 有

$$
m^{6} \cdot r(b+B q)=n^{6}
$$

亦即

$$
(a+B d) m^{6}=n^{6} .
$$

由此知 $m^{6} \mid n^{6}$, 进而有 $m \mid n$, 且 $p=\frac{n}{m} \in \mathbb{N}^{*}$. 这时由 (3) 便得

$$
a+B d=p^{6} \text {. }
$$

这就证明了这个数列中存在一项是整数的六次幂.

## 3. 凸数列问题

若实数列 $\left\{a_{n}\right\}$ 的一阶差分数列 $\triangle a_{n}$ 是单调不减的数列, 则称 $\left\{a_{n}\right\}$ 为凸数列, 其中 $\triangle a_{n}=a_{n+1}-a_{n}, n=0,1,2, \cdots$.

有几点值得注意:

(1) 凸数列 $\left\{a_{n}\right\}$ 可用不等式 $a_{k} \leq \frac{a_{k+1}+a_{k-1}}{2}$ 来刻划;

（2）凸性可用差分符号 $\triangle$ 来刻划 $\left(\triangle^{2} a_{n} \geq 0\right)$;

（3）显见等差数列是特殊的凸数列. 因此数列的凸性可视为数列的等距性的推广.

下面关于凸数列的等价描述定理是基本的和常用的.

定理 1 对于数列 $\left\{a_{n}\right\}$, 下面的结论 $(1) \sim(4)$ 是等价的.

(1) $\left\{a_{n}\right\}$ 是凸数列.

(2) 对任何的正整数 $m \neq n$ 有

$$
a_{n}-a_{m} \geq(n-m)\left(a_{m+1}-a_{m}\right)
$$

(3) 对任何满足 $0 \leq k<m<n$ 的三个正整数 $k, m, n$ 有

$$
\frac{a_{n}-a_{m}}{n-m} \geq \frac{a_{m}-a_{k}}{m-k}
$$

(4) 对任何满足 $m+n=p+q, 0 \leq p<m, n<q$ 的正整数 $m, n, p, q$ 有

$$
a_{p}+a_{q} \geq a_{m}+a_{n}
$$

证明是简单的, 留给读者练习.

推论 (1) 若 $\left\{a_{k}\right\}$ 为凸数列, 则对任意整数 $0 \leq i \leq k$ 有

$$
\frac{a_{i}}{i} \leq\left(\frac{1}{i}-\frac{1}{k}\right) a_{0}+\frac{a_{k}}{k}
$$

(2) 若 $\left\{a_{k}\right\}$ 是 $a_{0}=0$ 的凸数列, 则

$$
\frac{a_{1}}{1} \leq \frac{a_{2}}{2} \leq \cdots \leq \frac{a_{n}}{n} \leq \cdots
$$

关于凸数列的不等式已有丰富的结果. 下面仅列举两例

例 14(Mercer 不等式) 设 $a_{0}, a_{1}, \cdots$ 是凸数列, 则

$$
\frac{1}{2^{n}} \sum_{i=0}^{n} a_{i} C_{n}^{i} \leq \frac{1}{n+1} \sum_{i=0}^{n} a_{i} \leq \frac{1}{2}\left(a_{0}+a_{n}\right) .
$$

证明 先证右边的不等式.

由定理 1 中的 (4) 知对任意 $0 \leq i \leq n$ 有

$$
a_{i}+a_{n-i} \leq a_{0}+a_{n}
$$

因此

$$
\sum_{i=0}^{n} a_{i}+\sum_{i=0}^{n} a_{n-i} \leq(n+1)\left(a_{0}+a_{n}\right),
$$

即

$$
2 \sum_{i=0}^{n} a_{i} \leq(n+1)\left(a_{0}+a_{n}\right) .
$$

这就是要证的右边的不等式.

现对 $n$ 用归纳法证左边的不等式.

当 $n=1$ 时, 结论显然成立. 假设 $n-1$ 时结论成立, 则对 $n$ 有

$$
\begin{aligned}
\frac{1}{2^{n}} \sum_{i=0}^{n} C_{n}^{i} a_{i} & =\frac{1}{2^{n}} \sum_{i=0}^{n}\left(C_{n-1}^{i}+C_{n-1}^{i-1}\right) a_{i} \\
& =\frac{1}{2}\left(\frac{1}{2^{n-1}} \sum_{i=0}^{n-1} C_{n-1}^{i} a_{i}+\frac{1}{2^{n-1}} \sum_{i=0}^{n-1} C_{n-1}^{i} a_{i+1}\right) \\
& \leq \frac{1}{2}\left(\frac{1}{n} \sum_{i=0}^{n-1} a_{i}+\frac{1}{n} \sum_{i=1}^{n} a_{i}\right)
\end{aligned}
$$

$$
=\frac{a_{0}+a_{n}}{2 n}+\frac{a_{1}+\cdots+a_{n-1}}{n} .
$$

故要证明 $n$ 时的不等式只需证

$$
\frac{a_{0}+a_{n}}{2 n}+\frac{a_{1}+\cdots+a_{n-1}}{n} \leq \frac{a_{0}+a_{1}+\cdots+a_{n}}{n+1}
$$

这等价于

$$
(n-1)\left(a_{0}+a_{n}\right) \geq 2\left(a_{1}+a_{2}+\cdots+a_{n-1}\right) .
$$

这是成立的. 事实上, 注意到 $\left[\frac{n}{2}\right]+\left[\frac{n+1}{2}\right]=n$, 则

$$
a_{0}+a_{n} \geq a_{1}+a_{n-1} \geq a_{2}+a_{n-2} \geq \cdots \geq a_{\left[\frac{n}{2}\right]}+a_{\left[\frac{n+1}{2}\right]}
$$

故当 $n$ 为奇数时, 有

$$
\begin{aligned}
(n-1)\left(a_{0}+a_{n}\right) & \geq 2\left(\left(a_{1}+a_{n-1}\right)+\cdots+\left(a_{\left[\frac{n}{2}\right]}+a_{\left[\frac{n+1}{2}\right]}\right)\right) \\
& =2\left(a_{1}+a_{2}+\cdots+a_{n-1}\right) .
\end{aligned}
$$

当 $n$ 为偶数时, 有

$$
\begin{aligned}
(n-1)\left(a_{0}+a_{n}\right) & \geq 2\left(\left(a_{1}+a_{n-1}\right)+\cdots+\left(a_{\left[\frac{n}{2}\right]-1}+a_{\left[\frac{n+1}{2}\right]+1}\right)\right)+\left(a_{\left[\frac{n}{2}\right]}+a_{\left[\frac{n+1}{2}\right]}\right) \\
& =2\left(a_{1}+a_{2}+\cdots+a_{n-1}\right) .
\end{aligned}
$$

这就是 (1). 故结论对 $n$ 也成立.

下面的例子是德国数学家 H.Alzer 的一个结果, 我们发现了一个初等证明,并把它用作 2008 年国家集训队考试试题.

例 15 设

$$
0<x_{1} \leq \frac{x_{2}}{2} \leq \cdots \leq \frac{x_{n}}{n}, 0<y_{n} \leq y_{n-1} \leq \cdots \leq y_{1}
$$

求证:

$$
\left(\sum_{k=1}^{n} x_{k} y_{k}\right)^{2} \leq\left(\sum_{k=1}^{n} y_{k}\right)\left(\sum_{k=1}^{n}\left(x_{k}^{2}-\frac{1}{4} x_{k} x_{k-1}\right) y_{k}\right)
$$

其中 $x_{0}=0$.

注意 $\left\{x_{n}\right\}$ 本质上就是一个凸性条件, 它是 Cauchy 不等式的一种加强形式.

证明 对 $n$ 使用数学归纳法, 设原不等式为 $(*)$.

当 $n=1$ 时, $(*)$ 为恒等式.

假设 $(*)$ 对 $n-1$ 成立, 即

$$
\left(\sum_{k=1}^{n-1} x_{k} y_{k}\right)^{2} \leq\left(\sum_{k=1}^{n-1} y_{k}\right)\left(\sum_{k=1}^{n-1}\left(x_{k}^{2}-\frac{1}{4} x_{k} x_{k-1}\right) y_{k}\right)
$$

因此要证明 $(*)$, 只要证明

$$
\begin{aligned}
& \left(\sum_{k=1}^{n} x_{k} y_{k}\right)^{2}-\left(\sum_{k=1}^{n-1} x_{k} y_{k}\right)^{2} \\
\leq & \left(\sum_{k=1}^{n} y_{k}\right)\left(\sum_{k=1}^{n}\left(x_{k}^{2}-\frac{1}{4} x_{k} x_{k-1}\right) y_{k}\right)-\left(\sum_{k=1}^{n-1} y_{k}\right)\left(\sum_{k=1}^{n-1}\left(x_{k}^{2}-\frac{1}{4} x_{k} x_{k-1}\right) y_{k}\right) .
\end{aligned}
$$

化简后它等价于线性不等式:

$$
\frac{1}{4} x_{n} x_{n-1} y_{n} \leq \sum_{k=1}^{n-1} y_{k}\left(\left(x_{n}-x_{k}\right)^{2}-\frac{1}{4} x_{k} x_{k-1}-\frac{1}{4} x_{n} x_{n-1}\right) .
$$

下面我们来证明 (1).

一个自然的想法是将 $\left\{y_{k}\right\}$ 分离出来. 记

$$
z_{k}=\left(x_{n}-x_{k}\right)^{2}-\frac{1}{4} x_{k} x_{k-1}-\frac{1}{4} x_{n} x_{n-1}, 1 \leq k \leq n-1 .
$$

由于 $0<x_{1}<x_{2}<\cdots<x_{n}$, 所以 $z_{1}>z_{2}>\cdots>z_{n-1}$. 由切比雪夫不等式

$$
\sum_{k=1}^{n-1} y_{k} z_{k} \geq \frac{1}{n-1}\left(\sum_{k=1}^{n-1} y_{k}\right)\left(\sum_{k=1}^{n-1} z_{k}\right)
$$

因此要证 (1), 只要证明

$$
\frac{1}{4} x_{n} x_{n-1} y_{n} \leq \frac{1}{n-1}\left(\sum_{k=1}^{n-1} y_{k}\right)\left(\sum_{k=1}^{n-1} z_{k}\right)
$$

又

$$
\frac{1}{n-1}\left(\sum_{k=1}^{n-1} y_{k}\right) \geq y_{n}
$$

故只需证明

$$
\frac{1}{4} x_{n} x_{n-1} \leq \sum_{k=1}^{n-1} z_{k}
$$

即

$$
\frac{n}{4} x_{n} x_{n-1}+\frac{1}{4} \sum_{k=1}^{n-1} x_{k} x_{k-1}+2 \sum_{k=1}^{n-1} x_{n} x_{k} \leq(n-1) x_{n}^{2}+\sum_{k=1}^{n-1} x_{k}^{2}
$$

下面证明 (2).

事实上, 对 $1 \leq k \leq n-1$,

$$
2 x_{n} x_{k} \leq \frac{n}{k} x_{k}^{2}+\frac{k}{n} x_{n}^{2}=x_{k}^{2}+\frac{n-k}{k} x_{k}^{2}+\frac{k}{n} x_{n}^{2} \leq x_{k}^{2}+\left(\frac{(n-k) k}{n^{2}}+\frac{k}{n}\right) x_{n}^{2},
$$

所以

$$
2 \sum_{k=1}^{n-1} x_{n} x_{k} \leq \sum_{k=1}^{n-1} x_{k}^{2}+x_{n}^{2} \sum_{k=1}^{n-1}\left(\frac{(n-k) k}{n^{2}}+\frac{k}{n}\right) .
$$

又 $\frac{n}{4} x_{n} x_{n-1} \leq \frac{n-1}{4} x_{n}^{2}$, 而

$$
\frac{1}{4} \sum_{k=1}^{n-1} x_{k} x_{k-1} \leq x_{n}^{2} \sum_{k=1}^{n-1} \frac{k(k-1)}{4 n^{2}}
$$

所以

$$
\begin{aligned}
& \frac{n}{4} x_{n} x_{n-1}+\frac{1}{4} \sum_{k=1}^{n-1} x_{k} x_{k-1}+2 \sum_{k=1}^{n-1} x_{n} x_{k} \\
\leq & \sum_{k=1}^{n-1} x_{k}^{2}+x_{n}^{2}\left[\frac{n-1}{4}+\sum_{k=1}^{n-1} \frac{k(k-1)}{4 n^{2}}+\sum_{k=1}^{n-1}\left(\frac{(n-k) k}{n^{2}}+\frac{k}{n}\right)\right] \\
= & \sum_{k=1}^{n-1} x_{k}^{2}+(n-1) x_{n}^{2}
\end{aligned}
$$

从而 (2) 成立, 故原命题得证.

下面介绍 2002 年中国数学奥林匹克 (CMO) 的一个试题, 这个优雅的问题是李伟固教授创作的.

例 16(2002 年 CMO) 给定 $c \in\left(\frac{1}{2}, 1\right)$, 求最小常数 $M$ 使得对任意整数 $n \geq 2$及实数 $0<a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 只要满足

$$
\frac{1}{n} \sum_{k=1}^{n} k a_{i}=c \sum_{k=1}^{n} a_{k}
$$

就有

$$
\sum_{k=1}^{n} a_{k} \leq M \sum_{k=1}^{m} a_{k}
$$

其中 $m=[c n]$ 表示不超过 $c n$ 的最大整数.

下面的解法比原来标准解答稍微简化, 这是因为我们发现了一个有趣性质:序列 $\left\{a_{n}\right\}$ 的单调性蕴含着它的和序列 $\left\{S_{k}\right\}$ 的凸性.

解 对这个问题, 考察 $\left\{a_{k}\right\}$ 的和序列 $\left\{S_{k}\right\}$ 是自然的. 记

$$
r=c n, S_{0}=0, S_{k}=\sum_{i=1}^{k} a_{i}, \quad k=1,2, \cdots, n .
$$

于是条件 (1) 可写为

$$
\begin{aligned}
0 & =\sum_{k=1}^{n}(k-r) a_{k} \\
& =\sum_{k=1}^{n}(k-r) S_{k}-\sum_{k=1}^{n}(k-r) S_{k-1} \\
& =\sum_{k=1}^{n}(k-r) S_{k}-\sum_{k=1}^{n-1}(k+1-r) S_{k} \\
& =(n-r) S_{n}-\sum_{k=1}^{n-1} S_{k} \\
& =(n+1-r) S_{n}-\sum_{k=1}^{n} S_{k} .
\end{aligned}
$$

即

$$
\sum_{k=1}^{n} S_{k}=(n+1-r) S_{n}
$$

因序列 $\left\{a_{k}\right\}$ 可看作是它的和序列 $\left\{S_{k}\right\}$ 的差分, 因此 $\left\{a_{k}\right\}$ 是单调递减的,便蕴含着 $\left\{S_{k}\right\}$ 的二阶差分 $\triangle^{2} S_{k}>0$, 即 $\left\{S_{n}\right\}$ 是凸序列. 这样由凸序列的 Mercer 不等式 (即例 14 右边的不等式) 立得

$$
\begin{gathered}
\sum_{k=m}^{n} S_{k} \leq \frac{n-(m-1)}{2}\left(S_{m}+S_{n}\right), \\
\sum_{k=1}^{m-1} S_{k} \leq \frac{m-1}{2}\left(S_{1}+S_{m-1}\right) \leq \frac{m-1}{2} \cdot S_{m}
\end{gathered}
$$

由 (2),(3),(4) 便得

$$
\begin{aligned}
(n+1-r) S_{n} & =\sum_{k=1}^{m-1} S_{k}+\sum_{k=m}^{n} S_{k} \\
& \leq \frac{n}{2} \cdot S_{m}+\frac{n-m+1}{2} S_{n} .
\end{aligned}
$$

因此

$$
S_{n} \leq \frac{n}{n+1+m-2 r} \cdot S_{m} \leq \frac{n}{n-r} \cdot S_{m}=\frac{1}{1-c} S_{m}
$$

由此可见 $M \leq \frac{1}{1-c}$.

下面再证 $M \geq \frac{1}{1-c}$. 对 $n \geq \frac{1}{2 c-1}$, 取

$$
\begin{gathered}
a_{1}=a_{2}=\cdots=a_{m}=1 \\
a_{m+1}=a_{m+2}=\cdots=a_{n}=\frac{2 c n m-m(m+1)}{(n-m)(n+m+1)-2 c n(n-m)} \geq 1,
\end{gathered}
$$

易算得

$$
\sum_{k=1}^{n} k a_{k}=c n \sum_{k=1}^{n} a_{k}
$$

这说明这样构造的 $\left\{a_{k}\right\}$ 满足条件 (1). 这时, 注意到 $c n-1<m \leq c n$, 因此当 $n$足够大时有

$$
\begin{aligned}
M & \geq \frac{S_{n}}{S_{m}}=\frac{n}{n+m+1-2 c n} \\
& \geq \frac{n}{n-c n+1}=\frac{1}{1-c} \cdot \frac{1}{1+\frac{1}{n(1-c)}} \\
& \geq \frac{1}{1-c}\left(1-\frac{1}{n(1-c)}\right) \\
& =\frac{1}{1-c}-\frac{1}{n(1-c)^{2}} .
\end{aligned}
$$

由此可得 $M \geq \frac{1}{1-c}$.
下面介绍的是笔者提供给 2008 年 CMO 的一个问题. 它是关于凸数列的组合问题.

例 17 给定整数 $n \geq 3$. 证明: 集合 $X=\left\{1,2, \cdots, n^{2}-n\right\}$ 能写成两个不相交的非空子集的并, 使得每一个子集均不包含 $n$ 个元素 $a_{1}<a_{2}<\cdots<a_{n}$ 满足

$$
a_{k} \leq \frac{a_{k-1}+a_{k+1}}{2}, \quad(k=2,3, \cdots, n-1)
$$

证明 对 $k=1,2, \cdots, n-1$, 定义

$$
S_{k}=\left\{k^{2}-k+1, \cdots, k^{2}\right\}, T_{k}=\left\{k^{2}+1, \cdots, k^{2}+k\right\} .
$$

令

$$
S=\bigcup_{k=1}^{n-1} S_{k}, T=\bigcup_{k=1}^{n-1} T_{k}
$$

下面证明: $S, T$ 即为满足题目要求的两个子集.

首先 $S \cap T=\Phi$, 且 $S \cup T=X$.

其次, 如果 $S$ 中存在 $n$ 个元素 $a_{1}, a_{2}, \cdots, a_{n}, a_{1}<a_{2}<\cdots<a_{n}$, 满足

$$
a_{k} \leq \frac{a_{k-1}+a_{k+1}}{2}, \quad(k=2,3, \cdots, n-1)
$$

则

$$
a_{k}-a_{k-1} \leq a_{k+1}-a_{k}
$$

不妨设 $a_{1} \in S_{i}$. 由于 $\left|S_{n-1}\right|<n$, 故 $i<n-1$. 于是, $a_{1}, a_{2}, \cdots, a_{n}$ 这 $n$ 个数中至少有 $n-\left|S_{i}\right|=n-i$ 个在 $S_{i+1} \cup \cdots \cup S_{n-1}$ 中.

根据抽屉原理, 必有某个 $S_{j}(i<j<n)$ 中含有其中至少两个数, 设最小的一个为 $a_{k}$, 则 $a_{k}, a_{k+1} \in S_{j}$. 而 $a_{k-1} \in S_{1} \cup \cdots \cup S_{j-1}$, 于是,

$$
\begin{gathered}
a_{k+1}-a_{k} \leq\left|S_{j}\right|-1=j-1 \\
a_{k}-a_{k-1} \geq\left|T_{j-1}\right|+1=j
\end{gathered}
$$

则 $a_{k}-a_{k-1}>a_{k+1}-a_{k}$, 与式 (1) 矛盾.

故 $S$ 中不存在 $n$ 个元素满足题中假设. 同理, $T$ 中也不存在这样的 $n$ 个元素. 这表明 $S, T$ 即是满足要求的两个子集.

评注 此题的构造可通过特殊情况的讨论得到, 但讨论的严谨性是特别要注意的.

