# 2019 年 USAMO 试题解答与评析 

## 谢柏庭 潘至璇

(浙江省乐清知临中学, 325600)

指导教师: 羊明亮

2019 年美国数学奥林匹克于 4 月 18,19 日两天进行, 其试题题面新颖, 解答思路具有代表性. 下面我们整理了试题的解答并加以短评, 以供读者参考.

题 1. 函数 $f: \mathbb{N}^{+} \rightarrow \mathbb{N}^{+}$满足: 对所有正整数 $n$ 都有

$$
\underbrace{f(f(\cdots f(n) \cdots))}_{f(n) \text { 个 } f}=\frac{n^{2}}{f(f(n))}
$$

求 $f(1000)$ 的所有可能值.

解 所求为全体正偶数.

一方面, 对给定的正偶数 $2 k, k \in \mathbb{N}^{*}$, 取

$$
\left\{\begin{array}{l}
f(1000)=2 k \\
f(2 k)=1000 \\
f(n)=n, \quad n \neq 2 k, 1000
\end{array}\right.
$$

容易验证 $f$ 满足要求. 故 $f(1000)$ 可取到任一正偶数.

另一方面, 我们证明 $f(1000)$ 不能为正奇数. 我们以 $f^{(t)}$ 表示 $f$ 的 $t$ 次迭代, $t \in \mathbb{N}^{+}$.

下面我们证明 $f$ 为单射.

对于正整数 $m, l \in \mathbb{N}^{+}$, 若 $f(m)=f(l)$, 在原式中令 $n=m, l$ 知

$$
\begin{aligned}
m^{2} & =f^{(f(m))}(m) \cdot f^{(2)}(m) \\
& =f^{(f(m)-1)}(f(m)) \cdot f^{(2)}(m) \\
& =f^{(f(l)-1)}(f(l)) \cdot f^{(2)}(l) \\
& =f^{(f(l))}(l) \cdot f^{(2)}(l)
\end{aligned}
$$

修订日期: 2019-06-10.

$$
=l^{2} \text {. }
$$

结合 $m, l \in \mathbb{N}^{+}$知 $m=l$. 故 $f$ 为单射.

因此为证 $f(1000)$ 不为正奇数, 只需证明对 $2 \nmid m$, 有

$$
f(m)=m
$$

下面对 $m$ 归纳证明该命题.

$m=1$ 时, 原式中令 $n=1$, 有

$$
f^{(2)}(1) \cdot f^{(f(1))}(1)=1 .
$$

结合 $f^{(2)}(1), f^{(f(1))}(1) \in \mathbb{N}^{+}$知

$$
f^{(2)}(1)=f^{(f(1))}(1)=1 \text {. }
$$

在原式中令 $n=f(1)$ 知

$$
f^{(2)}(f(1)) \cdot f(f(1))=f^{2}(1) .
$$

这里用到了 $f(f(1))=1$.

故 $f^{2}(1)=f(1)$. 结合 $f(1) \in \mathbb{N}^{+}$知 $f(1)=1, m=1$ 时命题成立!

设 $m$ 为小于 $2 k+1$ 的正奇数时结论成立 $\left(k \in \mathbb{N}^{+}\right)$.

当 $m=2 k+1$ 时, 在原式中令 $n=m$ 知

$$
f^{(2)}(m) \cdot f^{(f(m))}(m)=m^{2} .
$$

而由归纳假设及 $(*)$ 知 $f^{(2)}(m), f^{(f(m))}(m)$ 均不为小于 $m$ 的奇数. 又 $2 \nmid m$, 故

$$
f^{(2)}(m)=f^{(f(m))}(m)=m .
$$

在原式中令 $n=f(m)$, 结合 $2 \nmid m, f(f(m))=m$ 知

$$
f^{2}(m)=f^{(2)}(m) \cdot f^{(m)}(f(m))=f(m) \cdot m .
$$

故 $f(m)=m, m=2 k+1$ 时结论成立!

归纳即知 (*) 成立, 有 $f(1000)$ 不为正奇数.

综合两方面知所求为全体正偶数.

评析 数论型函数方程中的归纳法一般有两种:

(1) 一般的对 $n$ 进行归纳;

(2) 对 $n$ 不同素因子归纳.

一般用 (2) 的情况更多, 这体现数论中“积性”的好处. 但需要注意的是, 归纳法只需找到一个可递降的量即可. 因此切记具体条件分析, 特别地小心“大小”的条件. 例如: 对于素数 $p, p-1$ 的素因子均小于 $p$, 这可能也是“递降”的途径.
题 2. 设圆内接四边形 $A B C D$ 满足 $A D^{2}+B C^{2}=A B^{2}$, 四边形 $A B C D$对角线交于 $E$, 点 $P$ 在边 $A B$ 上使 $\angle A P D=\angle B P C$. 证明: 直线 $P E$ 平分线段 $C D$.



证明 设 $A B, C D$ 中点为 $M, N, E N$ 交 $A B$ 于 $Q$. 我们证明 $P \equiv Q$.

由于 $\triangle C E D \sim \triangle B E A$, 且 $N, M$ 为相似对应点, 故

$$
\angle M E B=\angle N E C=\angle A E Q
$$

得 $E Q$ 为 $\triangle A E B$ 中 $\angle E$ 内的陪位中线, 结合 $\triangle A E D \sim \triangle B E C$, 有

$$
\frac{A Q}{B Q}=\left(\frac{E A}{E B}\right)^{2}=\left(\frac{A D}{B C}\right)^{2}
$$

又

$$
A B^{2}=A D^{2}+B C^{2},
$$

故

$$
\frac{A D^{2}}{A B^{2}}=\frac{A D^{2}}{A D^{2}+B C^{2}}=\frac{A Q}{A Q+B Q}=\frac{A Q}{A B}
$$

即 $A D^{2}=A B \cdot A Q$, 结合 $\angle Q A D=\angle D A B$, 知 $\triangle Q A D \sim \triangle D A B$, 有

$$
\angle D Q A=\angle B D A \text {. }
$$

类似地, $\angle C Q B=\angle B C A$. 故

$$
\angle D Q A=\angle B D A=\angle B C A=\angle C Q B
$$

又注意到对线段 $A B$ 上一点 $X$,

$$
\begin{aligned}
& \angle D X A=\angle X D B+\angle D B A \text { 关于 } B X \text { 递增; } \\
& \angle C X B=\angle C A B+\angle X C A \text { 关于 } B X \text { 递减, }
\end{aligned}
$$

故 $A B$ 上至多一点 $P$ 满足 $\angle C P B=\angle D P A$. 结合 $\angle D Q A=\angle C Q B$ 知

$$
P \equiv Q
$$

有 $E P$ 平分 $D C$. 证毕!
评析 简单题. 此法由结论倒推得到, 需说明 $P$ 的唯一性.

题 3. 设 $K$ 为所有十进制表示中不含数码 7 的正整数构成的集合. 求所有系数非负的整系数多项式 $f$, 使得对任意 $n \in K$, 均有 $f(n) \in K$.

解 所求为 $f(n)=10^{\alpha} n+m, \alpha \in \mathbb{N}, m=0$ 或 $m<10^{\alpha}$ 且 $m \in K$; 或 $f(n)=m, m \in K$.

一方面, 这样的 $f$ 显然满足要求 (因 $f(n)$ 十进制表示中非零数码要么为 $n$的数码, 要么为 $m$ 的数码).

另一方面, 对满足要求的 $f$, 我们先证明一个引理.

引理 若正整数 $a$ 满足对 $n \in K$, $a n \in K$, 则 $a$ 为 10 的幂.

证明 设

$$
\begin{aligned}
& \frac{8}{a}=\sum_{i=0}^{+\infty} x_{i} \cdot 10^{-(\beta+i)}, \\
& \frac{7}{a}=\sum_{i=0}^{+\infty} y_{i} \cdot 10^{-(\beta+i)}, \\
& \frac{1}{a}=\sum_{i=0}^{+\infty} z_{i} \cdot 10^{-(\beta+i)},
\end{aligned}
$$

其中 $\beta$ 为非负整数, $x_{i}, y_{i}, z_{i} \in\{0,1, \cdots, 9\}, x_{0}>0$, 且 $\left\{x_{i}\right\},\left\{y_{i}\right\},\left\{z_{i}\right\}$ 均不为最终全为 9 的数列. 由于 $\frac{1}{a}>\frac{1}{10} \cdot \frac{8}{a}$, 故

$$
z_{0}+10^{-1} \cdot z_{1}>0
$$

下考虑 $z_{0}$ 是否为 0 .

(I) $z_{0}>0$, 那么 $x_{0} \geq y_{0}+z_{0} \geq y_{0}+1$.

(i) 若 $y_{0} \neq 7$, 则因 $\left\{y_{i}\right\}$ 不会最终全为 9 , 必存在 $j \in \mathbb{N}^{+}$, 满足

$$
\frac{7}{a} \leq 10^{-\beta} \cdot y_{0}+9\left(10^{-(\beta+1)}+\cdots+10^{-(\beta+j)}\right)<10^{-\beta}\left(y_{0}+1\right)<\frac{8}{a},
$$

故有

$$
a\left(10^{j} y_{0}+9\left(10^{j-1}+\cdots+10^{0}\right)\right) \in\left[7 \cdot 10^{j+\beta}, 8 \cdot 10^{j+\beta}\right)
$$

其首位为 7 且不在 $K$ 中, 但

$$
10^{j} y_{0}+9\left(10^{j-1}+\cdots+10^{0}\right) \in K,
$$

与引理条件矛盾!

(ii) 若 $y_{0}=7$, 此时

$$
x_{0} \geq y_{0}+1=8, \frac{8}{a} \geq 8 \cdot 10^{-\beta} \text {. }
$$

若 $\frac{8}{a}>8 \cdot 10^{-\beta}$, 则 $\frac{7}{a}<10^{-\beta} \cdot 8<\frac{8}{a}$, 有

$$
8 a \in\left(7 \cdot 10^{\beta}, 8 \cdot 10^{\beta}\right),
$$

首位为 7 不在 $K$ 中, 但 $8 \in K$, 这与引理条件矛盾! 故

$$
\frac{8}{a}=8 \cdot 10^{-\beta},
$$

有 $a=10^{\beta}$ 为 10 的幂.

(II) $z_{0}=0$, 由 $z_{0}+10^{-1} z_{1}>0$ 知 $z_{1}>0$. 此时, $\frac{1}{a}<10^{-\beta}$, 有

$$
\frac{7}{a}<10^{-\beta} \cdot 7
$$

即 $y_{0}<7$.

若 $x_{0}>y_{0}$, 类似于 (I) 的 (i) 知这与引理条件矛盾!

因此 $x_{0}=y_{0}$, 有 $x_{0}, y_{0}<7$. 下考虑 $x_{1}$ 与 $y_{1}$. 由于

$$
10 x_{0}+x_{1} \geq 10 y_{0}+y_{1}+10 z_{0}+z_{1}
$$

有

$$
x_{1} \geq y_{1}+z_{1} \geq y_{1}+1
$$

类似于 (I) 知

$$
\frac{1}{a}=10^{-(\beta+1)}
$$

但此时 $x_{0}=0$, 与 $x_{0} \neq 0$ 矛盾!

综合 (I), (II) 知 $a$ 为 10 的幂, 引理证毕!

回到原题. 设

$f(n)=a_{k} x^{k}+a_{k-1} x^{k-1}+\cdots+a_{1} x+a_{0}, a_{k}, \cdots, a_{0} \in \mathbb{N}, k \in \mathbb{N}, a_{k}>0$.

我们先证明 $k \leq 1$. 否则, 若 $k \geq 2$, 取

$$
n_{0}=\left(3 \cdot 10^{\alpha}+c\right) \cdot 10^{\gamma}
$$

$\alpha, \gamma, c$ 待定, $\alpha, \gamma, c \in \mathbb{N}^{*}$. 由于 $3^{k-1} \cdot k \cdot a_{k}$ 必不为 10 的幂, 由引理知, 存在 $c \in K$, 使 $3^{k-1} k a_{k} c \notin K$. 取 $\alpha$ 满足

$$
10^{\alpha}>3^{k} \cdot c^{k} a_{k} \cdot 2^{k}
$$

取 $\gamma$ 满足

$$
10^{\gamma}>a_{k}\left(3 \cdot 10^{\alpha}+c\right)^{k}+\cdots+a_{1}\left(3 \cdot 10^{\alpha}+c\right)+a_{0}
$$

那么

$$
f\left(n_{0}\right)=a_{0}+a_{1}\left(3 \cdot 10^{\alpha}+c\right) \cdot 10^{\gamma}+\cdots+a_{k-1}\left(3 \cdot 10^{\alpha}+c\right)^{k-1} \cdot 10^{\gamma(k-1)}
$$

$$
+10^{\gamma k}\left(a_{k} \mathrm{C}_{k}^{0} 3^{k} c^{0} \cdot 10^{\alpha k}+a_{k} \mathrm{C}_{k}^{1} 3^{k-1} c^{1} \cdot 10^{\alpha(k-1)}+\cdots+a_{k} \mathrm{C}_{k}^{k} 3^{0} c^{k} \cdot 10^{\alpha \cdot 0}\right)
$$

其十进制表示为

$$
\begin{gathered}
a_{k} \mathrm{C}_{k}^{0} 3^{k} c^{0}, a_{k} \mathrm{C}_{k}^{1} 3^{k-1} c^{1}, \cdots, a_{k} \mathrm{C}_{k}^{k} 3^{0} c^{k} \\
a_{k-1}\left(3 \cdot 10^{\alpha}+c\right)^{k-1}, \cdots, a_{1}\left(3 \cdot 10^{\alpha}+c\right), a_{0}
\end{gathered}
$$

间加上若干 “ 0 ”后首尾拼接而成 (用到 $\alpha, \gamma$ 定义).

又 $a_{k} \mathrm{C}_{k}^{1} 3^{k-1} c^{1} \notin K$, 故 $f\left(n_{0}\right) \notin K$. 而由 $c \in K$ 知 $n_{0} \in K$, 这与对 $n \in K$ 有 $f(n) \in K$ 矛盾! 故 $k \leq 1$.

当 $k=0$ 时, $f(n)=m, m$ 为常数. 此时 $m \in K$ 显然!

当 $k=1$ 时, 设 $f(n)=a n+m$, 取 $n=10^{\delta} \cdot n_{1}, 10^{\delta}>m, n_{1} \in \mathbb{N}^{*}$, 有对 $n_{1} \in K, a n_{1} \in K ; m \in K$ 或 $m=0$ (因对 $n \in K, f(n) \in K$ ).

结合引理知 $a$ 为 10 的幂, 可设

$$
f(n)=10^{\alpha} n+m, m \in K \text { 或 } m=0, \alpha \in \mathbb{N} \text {. }
$$

此时若 $m \geq 10^{\alpha}$, 设 $10^{\alpha+i_{0}} \leq m<10^{\alpha+i_{0}+1}, i_{0} \in \mathbb{N}$, 并设 $m$ 首位为 $j_{0}$.

取 $n=\left(17-j_{0}\right) \cdot 10^{i_{0}}$, 则

$$
f(n)=\left(17-j_{0}\right) \cdot 10^{\alpha+i_{0}}+m=17 \cdot 10^{\alpha+i_{0}}+A
$$

其中 $A<10^{\alpha+i_{0}}$, 那么 $10^{\alpha+i_{0}}$ 位对应的数码为 7 , 不在 $K$ 中.

又 $1 \leq j_{0} \leq 9$, 有 $n \in K$, 这与对 $n \in K, f(n) \in K$ 矛盾! 故 $m<10^{\alpha}$.

综上, 所求 $f$ 为 $f(n)=10^{\alpha} n+m, \alpha \in \mathbb{N}, m=0$; 或 $m \in K$ 且 $m<10^{\alpha}$; 或 $f(n)=m, m \in K$.

评析 此题是循序渐进的好题.

(I) 先处理最简单的情形, 即引理.

为使一个正整数中必含某个数码, 有两种想法.

(1) 数论方法: 同余;

(2) 代数方法:

$A \cdot 10^{\alpha+1}+B \cdot 10^{\alpha} \leq x<A \cdot 10^{\alpha+1}+(B+1) \cdot 10^{\alpha}(B \in\{0,1, \cdots, 9\})$,则 $x$ 含 $B$. 常用弱化: $A=0$.

此题 (1) 也可行, 可尝试用模 10 构一个个位为 8 的数 $C$, 再用 $10^{\gamma} C-D$ 的形式得到 7 来解决大部分情形. 而对于 (2), 我们在原解答基础上再做一步特化.

考虑 $1, a, a^{2}, \cdots$ 它们均在 $K$ 中, 而其中必有一数首位为 7 (由 Dirichlet 定理易证!)

(II) 对复杂情形, 我们希望利用简单情形, 需构造“一次项”. 因此我们构造了“分段”的形式, 这在数码问题中常用. 数码中重要的部分有两种:

一是“分段”，保持了每一段自身的性质.

二是段与段的交界点, 可能相加后发生进位导致突变.

题 4. 给定正整数 $n$, 确定有多少种方式选取 $(n+1)^{2}$ 个集合 $S_{i j} \subseteq$ $\{1,2, \cdots, 2 n\}$, 其中 $i, j=0,1, \cdots, n$, 满足以下两个条件:

(1) 对任意 $i, j \in\{0,1, \cdots, n\}$, 集合 $S_{i, j}$ 有 $i+j$ 个元素;

(2) 对任意 $0 \leq i \leq k \leq n, 0 \leq j \leq l \leq n$, 均有 $S_{i, j} \subseteq S_{k, 1}$.

解 所求为 $(2 n) ! \cdot 2^{n^{2}}$. 我们分两步确定所求集族:

(I) 我们先确定集合链

$$
S_{0,0} \subseteq S_{0,1} \subseteq \cdots \subseteq S_{0, n} \subseteq S_{1, n} \subseteq \cdots \subseteq S_{n, n}
$$

注意到, 由 (1) 有 $S_{0,0}=\emptyset, S_{n, n}=\{1,2, \cdots, 2 n\}$, 并且由 (1), (2) 有: 该链上除 $S_{0,0}$ 外的每个集合, 恰比它的前一个集合多一个元素.

设这样的元素从左往右依次为 $a_{1}, a_{2}, \cdots, a_{2 n}$, 则该集合链与序列 $a_{1}, a_{2}, \cdots$, $a_{2 n}$ 一一对应, 其即为

$$
\emptyset \subseteq\left\{a_{1}\right\} \subseteq\left\{a_{1}, a_{2}\right\} \subseteq \cdots \subseteq\left\{a_{1}, a_{2}, \cdots, a_{2 n}\right\}
$$

并且 $a_{1}, \cdots, a_{2 n}$ 为 $1,2, \cdots, 2 n$ 的一个排列.

故这样的集合链恰为 $(2 n)$ ! 条.

(II) 我们再依次确定 $\left(S_{i, 0}, \cdots, S_{i, n-1}\right)(i=1,2, \cdots, n)$, 使它们满足

$$
S_{i-1, j} \subseteq S_{i, j} \subseteq S_{i, j+1}
$$

且

$$
\left|S_{i, j}\right|=i+j, 0 \leq j \leq n-1,1 \leq i \leq n .
$$

对给定的 $m \in \mathbb{N}, m \leq n-1$. 当 $S_{i, j}(0 \leq i \leq m, 0 \leq j \leq n)$ 及 $S_{m+1, k+1}$, $S_{m+1, k+2}, \cdots, S_{m+1, n}$ 均已确定时 $(0 \leq k \leq n-1)$, 由于

$$
\left|S_{m, k}\right|=m+k,\left|S_{m+1, k+1}\right|=m+k+2 .
$$

故可设

$$
S_{m+1, k+1} \backslash S_{m, k}=\{a, b\}
$$

恰存在 2 个 $A$ 满足

$$
S_{m, k} \subseteq A \subseteq S_{m+1, k+1}
$$

且

$$
|A|=m+k+1 \text {. }
$$

即 $S_{m, k} \cup\{a\}$ 与 $S_{m, k} \cup\{b\}$. 故此时 $S_{m+1, k}$ 有两种选择.

由此即知: 当 $S_{i, j}(0 \leq i \leq m, 0 \leq j \leq n)$ 均已给定时,

$$
\left(S_{m+1,0}, \cdots, S_{m+1, n-1}\right)
$$

共 $2^{n}$ 个选择, 故 $S_{i, j}(1 \leq i \leq n, 0 \leq j \leq n-1)$ 共 $2^{n^{2}}$ 种选择. 并且, 在如此确定整个集族后, 对 $0 \leq i \leq r \leq n, 0 \leq j \leq l \leq n$, 有

$$
S_{i, j} \subseteq S_{i, j+1} \subseteq \cdots \subseteq S_{i, l} \subseteq S_{i+1, l} \subseteq \cdots \subseteq S_{r, l}
$$

满足条件 (2). 而满足条件的集族显然满足确定过程中条件.

因此, 这样确定的集族即为所求. 综合 (I), (II), 所求为 $(2 n) ! \cdot 2^{n^{2}}$ 种 (用到乘法原理).

综上, 所求为 $(2 n) ! \cdot 2^{n^{2}}$.

评析 此题属于简单题, 找到一个简单的生成方法即可. “先定边界再往中间”是常用方法. 应注意一一对应并非显然.

题 5. 黑板上写有两个有理数 $\frac{m}{n}$ 和 $\frac{n}{m}$, 其中 $m, n$ 是互素的正整数. 每一步,埃文可以选取黑板上的两个数 $x, y$, 在黑板上添上它们的算术平均 $\frac{x+y}{2}$, 或添上它们的调和平均 $\frac{2 x y}{x+y}$. 试确定所有 $(m, n)$, 使得埃文可在有限步内在黑板上写下数 1 .

解 所求为 $\left(k, 2^{\alpha}-k\right), \alpha \in \mathbb{N}^{*}, k$ 为小于 $2^{\alpha}$ 的正奇数.

一方面, 我们先归纳证明对 $\beta \in \mathbb{N}^{*}$ 及小于 $2^{\beta}$ 的正奇数 $l$,

$$
\frac{l}{2^{\beta}} \cdot \frac{m}{n}+\frac{2^{\beta}-l}{2^{\beta}} \cdot \frac{n}{m}
$$

可写在黑板上.

$\beta=1$ 时, 此即 $\frac{1}{2}\left(\frac{n}{m}+\frac{m}{n}\right)$ 可写在黑板上, 结论显然成立.

设 $\beta=\gamma$ 时结论成立.

当 $\beta=\gamma+1$ 时, 若 $l<2^{\gamma}$, 由归纳假设

$$
\frac{l}{2^{\gamma}} \cdot \frac{m}{n}+\frac{2^{\gamma}-l}{2^{\gamma}} \cdot \frac{n}{m}
$$

可写在黑板上. 故

$$
\frac{l}{2^{\gamma+1}} \cdot \frac{m}{n}+\frac{2^{\gamma+1}-l}{2^{\gamma+1}} \cdot \frac{n}{m}=\frac{1}{2}\left(\left(\frac{l}{2^{\gamma}} \cdot \frac{m}{n}+\frac{2^{\gamma}-l}{2^{\gamma}} \cdot \frac{n}{m}\right)+\frac{n}{m}\right)
$$

可写在黑板上.
若 $2^{\gamma} \leq l<2^{\gamma+1}$, 由 $2 \nmid l$ 知 $2^{\gamma}<l<2^{\gamma+1}$. 由归纳假设,

$$
\frac{l-2^{\gamma}}{2^{\gamma}} \cdot \frac{m}{n}+\frac{2^{r+1}-l}{2^{r}} \cdot \frac{n}{m}
$$

可写在黑板上. 故

$$
\frac{l}{2^{\gamma+1}} \cdot \frac{m}{n}+\frac{2^{\gamma+1}-l}{2^{\gamma}} \cdot \frac{n}{m}=\frac{1}{2}\left(\left(\frac{l-2^{\gamma}}{2^{\gamma}} \cdot \frac{m}{n}+\frac{2^{\gamma+1}-l}{2^{\gamma}} \cdot \frac{n}{m}\right)+\frac{m}{n}\right)
$$

可写在黑板上.

故 $\beta=\gamma+1$ 时结论成立, 归纳即知 $(*)$ 成立.

由 $(*)$ 知, 当 $(m, n)=\left(k, 2^{\alpha}-k\right)$ 时,

$$
1=\frac{k}{2^{\alpha}} \cdot \frac{2^{\alpha}-k}{k}+\frac{2^{\alpha}-k}{2^{\alpha}} \cdot \frac{k}{2^{\alpha}-k}
$$

可写在黑板上, 故 $\left(k, 2^{\alpha}-k\right)$ 满足要求.

另一方面, 对满足要求的 $(m, n)$, 我们证明 $m+n$ 为 2 的幂.

设 $m+n=2^{\alpha} \cdot P, \alpha \in \mathbb{N}, 2 \nmid P, P \in \mathbb{N}^{*}$, 下证 $P=1$.

我们先递推的确定 $\left\{P_{t}\right\}_{t \geq 1}: P_{1}$ 集合为 $\frac{m}{n}$ 与 $\frac{n}{m}$ 构成的集合, $P_{t}$ 为所有 $P_{t-1}$中某两数 (不必不同) 的算术平均或调和平均的数构成的集合.

下面对 $t$ 进行归纳证明: 对 $\frac{x}{y} \in P_{t}, x, y$ 互素, 有

$$
P \mid x+y
$$

$t=1$ 时结论显然成立.

设 $t=r$ 时结论成立. 则当 $t=r+1$ 时, 考虑 $\frac{x}{y}$ 的来源, 设其为 $\frac{x_{1}}{y_{1}}$ 与 $\frac{x_{2}}{y_{2}}$ 的算术平均或调和平均, 其中 $x_{1}$ 与 $y_{1}, x_{2}$ 与 $y_{2}$ 互素, $\frac{x_{1}}{y_{1}}, \frac{x_{2}}{y_{2}} \in P_{r}$.

由归纳假设, $P\left|x_{1}+y_{1}, P\right| x_{2}+y_{2}$, 故

$$
\operatorname{gcd}\left(P, 2 y_{1} y_{2}\right)=1
$$

这里用到 $x_{1}$ 与 $y_{1}, x_{2}$ 与 $y_{2}$ 互素.

下面分两种情况讨论:

(I) $\frac{x}{y}=\frac{1}{2}\left(\frac{x_{1}}{y_{1}}+\frac{x_{2}}{y_{2}}\right)$, 则

$$
\frac{x+y}{y}=\frac{\left(x_{1}+y_{1}\right) y_{2}+\left(x_{2}+y_{2}\right) y_{1}}{2 y_{1} y_{2}}
$$

又 $P\left|x_{1}+y_{1}, P\right| x_{2}+y_{2}, \operatorname{gcd}\left(P, 2 y_{1} y_{2}\right)=1$ (用到 $(\star)$ 及 $P$ 为奇数), 故

$$
P \mid x+y
$$

(II) $\frac{x}{y}=\frac{2 \frac{x_{1}}{y_{1}} \cdot \frac{x_{2}}{y_{2}}}{\frac{x_{1}}{y_{1}}+\frac{x_{2}}{y_{2}}}$, 则

$$
\frac{y}{x}=\frac{1}{2}\left(\frac{y_{1}}{x_{1}}+\frac{y_{2}}{x_{2}}\right)
$$

有

$$
\frac{y+x}{x}=\frac{1}{2} \frac{\left(x_{1}+y_{1}\right) x_{1}+\left(x_{2}+y_{2}\right) x_{1}}{x_{1} x_{2}} .
$$

类似于 (I) 知 $P \mid x+y$. 综合 (I), (II) 知

$$
P \mid x+y
$$

归纳即知 $(* *)$ 获证!

又由 $(* *)$ 及 1 在某个 $P_{t}$ 中知 $P \mid 1+1$, 故 $P=1$ (用到 $2 \nmid P$ ). 故 $m+n$ 为 2 的幕, 为 $2^{\alpha}$. 结合 $m, n$ 为互质正整数知

$$
(m, n)=\left(k, 2^{\alpha}-k\right), \alpha \in \mathbb{N}^{*}, k \text { 为小于 } 2^{\alpha} \text { 的正奇数 }
$$

综上, 所求为 $\left(k, 2^{\alpha}-k\right), \alpha \in \mathbb{N}^{*}, k$ 为小于 $2^{\alpha}$ 的正奇数.

评析 典型的单人操作问题中的运算问题. 经典的思路是找不变量, 对运算次数归纳, 这样有助于“化整为零”. 此题由 $(*)$ 可猜出答案, 自然猜不变量 $m+n$与 2 的幂有关, 便不难发现 (**), 即证.

题 6. 求所有实系数多项式 $P$, 满足对任意非零实数 $x, y, z$, 若 $2 x y z=$ $x+y+z$, 则

$$
\frac{P(x)}{y z}+\frac{P(y)}{z x}+\frac{P(z)}{x y}=P(x-y)+P(y-z)+P(z-x) .
$$

解 所求 $P(x)=t\left(x^{2}+3\right), t \in \mathbb{R}$.

一方面, 当 $P(x)=t\left(x^{2}+3\right)$ 时, 对非零实数 $x, y, z$ 满足 $2 x y z=x+y+z$, 有

$$
\begin{aligned}
\sum_{c y c} \frac{P(x)}{y z} & =t \sum_{c y c} \frac{x^{3}+3 x}{x y z}=\frac{t}{x y z}\left(\sum_{c y c} x^{3}+6 x y z\right) \\
& =\frac{t}{x y z}\left(\frac{1}{2}\left(\sum_{c y c} x\right)\left(\sum_{c y c}(x-y)^{2}\right)+9 x y z\right) \\
& =t\left(\sum_{c y c}(x-y)^{2}+9\right)=\sum_{c y c} P(x-y),
\end{aligned}
$$

故 $P(x)=t\left(x^{2}+3\right)$ 满足要求, 其中第二行等式用到恒等式

$$
\sum_{c y c} x^{3}=\left(\sum_{c y c} x\right)\left(\frac{1}{2} \sum_{c y c}(x-y)^{2}\right)+3 x y z
$$

另一方面, 对满足要求的 $P(x)$, 我们证明其必形如 $t\left(x^{2}+3\right), t \in \mathbb{R}$.

$$
\begin{array}{r}
\text { 记 } Q(x, y, z)=\sum_{c y c} x P(x)-x y z \sum_{c y c} P(x-y), \text { 由条件知 } \\
Q\left(x, y, \frac{x+y}{2 x y-1}\right)=0,
\end{array}
$$

对 $x \neq 0, y \neq 0, x+y \neq 0$ 且 $2 x y \neq 1$ 的所有实数 $x, y$ 成立.

那么可在 $(*)$ 两边同乘以 $(2 x y-1)^{\alpha}, \alpha$ 为充分大的正整数, 使 $(*)$ 变为 $R(x, y)=0$, 其中 $R$ 为关于 $x, y$ 的多项式. 而任意给定 $x=x_{0}$ 为非零实数时,因存在无数个 $y$, 满足 $y \neq 0, y+x_{0} \neq 0,2 x_{0} y \neq-1$, 故存在无数个 $y \in \mathbb{R}$, 使得 $R\left(x_{0}, y\right)=0$. 故对 $y \in R, R\left(x_{0}, y\right)=0$. 故对 $x, y \in \mathbb{R}, R(x, y)=0$. 进而对 $x, y \in \mathbb{C}, R(x, y)=0$.

下取 $(x, y)=(u,-u), u \in \mathbb{R}$, 有 $R(u,-u)=0$, 即 $Q(u,-u, 0)=0$. 即

$$
u(P(u)-P(-u))=0 .
$$

有 $P(u)=P(-u)$ 对 $u \in \mathbb{R}$ 成立.

再取 $(x, y)=\left(x, \frac{\mathrm{i}}{\sqrt{2}}\right), \mathrm{i}=\sqrt{-1}$, 有 $R\left(x, \frac{\mathrm{i}}{\sqrt{2}}\right)=0$, 由于

$$
\frac{x+\frac{\mathrm{i}}{\sqrt{2}}}{2 x \cdot \frac{\mathrm{i}}{\sqrt{2}}-1}=-\frac{\mathrm{i}}{\sqrt{2}}
$$

有 $Q\left(x, \frac{\mathrm{i}}{\sqrt{2}},-\frac{\mathrm{i}}{\sqrt{2}}\right)=0$. 从而

$$
\begin{aligned}
& x P(x)+\frac{\mathrm{i}}{\sqrt{2}}\left(P\left(\frac{\mathrm{i}}{\sqrt{2}}\right)-P\left(-\frac{\mathrm{i}}{\sqrt{2}}\right)\right) \\
= & \frac{1}{2} x\left(P\left(x-\frac{\mathrm{i}}{\sqrt{2}}\right)+P(\sqrt{2} \mathrm{i})+P\left(-\frac{\mathrm{i}}{\sqrt{2}}-x\right)\right) .
\end{aligned}
$$

结合 (1) 知, 此即

$$
2 P(x)-P\left(x-\frac{\mathrm{i}}{\sqrt{2}}\right)-P\left(x+\frac{\mathrm{i}}{\sqrt{2}}\right)=P(\sqrt{2} \mathrm{i}) .
$$

下设 $P(x)=a_{n} x^{n}+\cdots+a_{1} x+a_{0}, a_{n} \neq 0$.

我们证明 $n \leq 2$. 这是因为 $n \geq 3$ 时, (2) 式左边 $x^{n-2}$ 的系数为

$$
-2 a_{n} \mathrm{C}_{n}^{2} \cdot\left(\frac{\mathrm{i}}{\sqrt{2}}\right)^{2} \neq 0
$$

而 $(2)$ 式右边为常数, 这不可能!

结合 (1) 可设 $P(x)=c x^{2}+d$, 代入 (2) 知 $c=-2 c+d$, 故 $d=3 c$. 即有 $P(x)$形如 $t\left(x^{2}+3\right), t \in \mathbb{R}$.

综合两方面知, 所求为

$$
P(x)=t\left(x^{2}+3\right), t \in \mathbb{R} .
$$

评析 此题关键在于意识到条件 $x+y+z=2 x y z$ 为“一次式”, 可解出 $z$, 从而使问题变为二元多项式问题, 再通过赋特殊值简化. 要小心这“两步走”, 先窥探本质, 再“加码”优化. 固然直接比较 $R(x, y)$ 系数“可行”, 但明显麻烦, 不如再想一步: 是否有特殊值.
此题代 $\left(x, x, \frac{2 x}{2 x^{2}-1}\right),\left(x, \frac{1}{x}, x+\frac{1}{x}\right)$ 均可行, 不如此法简明. 另外, 多元多项式的整除问题一般需用到 $\mathbb{C}$ 上条件, $\mathbb{R}$ 上除非像此题有 “全在 $\mathbb{R}$ 上的零点”, 否则不可行. 即: “若 $R(x, y, z)=0$ 时, $Q(x, y, z)=0$, 对 $x, y, z \in R$ 成立, 不一定有 $R(x, y, z) \mid Q(x, y, z)$, 这一点需留心.

