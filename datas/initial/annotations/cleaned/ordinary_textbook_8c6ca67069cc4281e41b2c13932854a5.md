# 2018 年清北测试试题解析 

段钦瀚

(湖南省雅礼中学, 长沙, 410007)

今年 6 月份北京大学和清华大学相继在部分省市进行了数学学科竞赛测试, 考试时间均为 3 个小时, 测试均有四道题. 本文给出这些题目的解答及一些评价.

## I. 试 题

## 一、 北大测试试题

1. 在 $\triangle A B C$ 中, $\angle A B C=100^{\circ}, \angle A C B=65^{\circ}, M, N$ 分别是边 $A B, A C$ 上的点, 且满足 $\angle M C B=55^{\circ}, \angle N B C=80^{\circ}$. 求 $\angle N M C$.
2. 求出所有非负实系数多项式 $P(x)$ 满足

$$
P(\sin x)+P(\cos x)=1, \forall x \in \mathbb{R} .
$$

3. 已知存在一个由非零实数组成的 $2018 \times 2018$ 数表满足: 数表中任意一个数等于其所在行和列其余 4034 个数的和的 $k$ 分之一, 求整数 $k$ 的所有可能值.
4. $P(x)$ 是一个非负整系数非零多项式. 已知存在正整数 $a$, 使得数列 $a_{1}=a, a_{n+1}=P\left(a_{n}\right)$ 满足: 集合 $A=\left\{p \mid p\right.$ 为某项 $a_{n}$ 的素因数 $\}$ 为有限集, 求所有满足条件的 $P(x)$.

## 二、 清华测试试题

1. 设正实数 $a_{1}, a_{2}, \cdots$ 满足 $a_{1}+a_{2}+\cdots+a_{n} \leq n^{2}, \forall n \in \mathbb{N}^{+}$. 求证: 对 $\forall n \in \mathbb{N}^{+}$,

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}>\frac{1}{4} \log _{2} n .
$$

收稿日期: 2018-07-10； 修订日期: 2018-08-05.

2. 给定凸多边形 $A_{1} A_{2} \cdots A_{n}$. 证明: 存在凸多边形内部一点 $P$, 使得对任意过点 $P$ 的直线 $l, l$ 与凸多边形 $A_{1} A_{2} \cdots A_{n}$ 的边界交于 $U, V$ 两点, 且满足

$$
\frac{1}{2} \leq \frac{P U}{P V} \leq 2
$$

3. 设 $n$ 为大于 100 的正整数. 对任意不超过 $n$ 的素数 $p$, 记 $\alpha_{p}$ 为 $n$ ! 中 $p$ 的次数, 证明: 可以对每个不超过 $n$ 的素数 $p$, 指定一个不超过 $n$ 的互不相同的正整数 $\beta_{p}$, 使得 $1+\alpha_{p} \mid \beta_{p}$.
4. 设 $n, a, b \in \mathbb{N}^{+}, a \leq b \leq n-a, X=\{1,2, \cdots, n\}$, 给定 $A_{0}$ 为 $X$ 的 $a$ 元子集.

(1) 设 $A \subseteq X,|A|=a,\left|A \cap A_{0}\right|=i$, 对 $0 \leq j \leq a$, 求满足以下条件的集合 $B$ 的个数:

$$
A \subseteq B \subseteq X,|B|=b,\left|B \cap A_{0}\right|=j
$$

(2) 证明: 可以给每个 $X$ 的 $b$ 元子集 $B$ 赋上实数 $f(B)$, 使得对 $A \subseteq X,|A|=$ $a$, 均满足:

$$
\sum_{\substack{A \subseteq B \subseteq X,|B|=b}} f(B)=\left\{\begin{array}{ll}
0, & A \neq A_{0} \\
1, & A=A_{0}
\end{array} .\right.
$$

## II. 解答和评注

## 一、北大测试试题

1. 在 $\triangle A B C$ 中, $\angle A B C=100^{\circ}, \angle A C B=65^{\circ}, M, N$ 分别是边 $A B, A C$ 上的点, 且满足 $\angle M C B=55^{\circ}, \angle N B C=80^{\circ}$. 求 $\angle N M C$.



解 设 $\angle N M C=\alpha$. 对 $\triangle M N C, \triangle M N B, \triangle C N B$ 运用正弦定理有

$$
\begin{aligned}
\frac{C N}{\sin \alpha} & =\frac{M N}{\sin \angle M C N}=\frac{M N}{\sin 10^{\circ}} ; \\
\frac{M N}{\sin 20^{\circ}} & =\frac{M N}{\sin M B N}=\frac{B N}{\sin N M B}=\frac{B N}{\sin \left(\alpha+25^{\circ}\right)} \\
\frac{B N}{\sin 65^{\circ}} & =\frac{B N}{\sin \angle B C N}=\frac{C N}{\sin \angle N B C}=\frac{C N}{\sin 80^{\circ}} .
\end{aligned}
$$

三式相乘可知: $\sin \alpha \sin 20^{\circ} \sin 65^{\circ}=\sin 10^{\circ} \sin \left(\alpha+25^{\circ}\right) \sin 80^{\circ}$, 从而

$$
\frac{\sin \left(\alpha+25^{\circ}\right)}{\sin \alpha}=\frac{\sin 20^{\circ} \sin 65^{\circ}}{\sin 10^{\circ} \sin 80^{\circ}}=\frac{\sin 20^{\circ} \cos 25^{\circ}}{\sin 10^{\circ} \cos 10^{\circ}}=\frac{\sin 50^{\circ}}{\sin 25^{\circ}},
$$

则

$$
\angle N M C=\alpha=25^{\circ} .
$$

另解 过 $B$ 作 $B C$ 的垂线分别交 $A C, M C$ 于点 $D, E$. 连接 $M D, E N$.



由题意可知 $\angle A B D=\angle N B D=\angle M C A=10^{\circ}$, 故 $M, D, C, B$ 与 $E, N, C, B$均四点共圆, 所以 $\angle E N D=\angle E B C=\angle M D E=90^{\circ}$, 则 $M, D, E, N$ 四点共圆.故 $\angle N M C=\angle B D C=90^{\circ}-\angle B C A=25^{\circ}$.

评析 这是一道简单题. 但这类题目需要短时间内做出来, 则用三角计算比几何做法更为保险. 还有一些其他想法, 例如注意到 $C$ 为 $\triangle M N B$ 的旁心.

2. 求出所有非负实系数多项式 $P(x)$ 满足

$$
P(\sin x)+P(\cos x)=1, \forall x \in \mathbb{R} .
$$

解 由题意可知: 对 $\forall x \in \mathbb{R}$, 有

$$
P(\sin x)+P(\cos x)=1=P(\sin (-x))+P(\cos (-x))=P(-\sin x)+P(\cos x) \text {. }
$$

所以 $P(\sin x)=P(-\sin x), \forall x \in \mathbb{R}$. 即

$$
P(t)=P(-t), \forall t \in[-1,1] \text {. }
$$

故 $P(x)$ 在 $[-1,1]$ 上为偶函数. 又 $P(x)$ 为非负实系数多项式, 故 $P(x)$ 无奇次项 (奇次项系数为 0 ). 否则对 $x \in(0,1], P(x)>P(-x)$, 矛盾!

由此可知, 存在非负实系数多项式 $Q(x)$ 满足 $P(x)=Q\left(x^{2}\right), \forall x \in \mathbb{R}$. 则 $Q\left(\sin ^{2} x\right)+Q\left(\cos ^{2} x\right)=1, \forall x \in \mathbb{R}$. 即

$$
Q(t)+Q(1-t)=1, t \in[0,1] .
$$

设 $Q(x)=\sum_{i=0}^{n} a_{i} x^{i}$, 其中实数 $a_{0}, a_{1}, \cdots, a_{n} \geq 0, a_{n} \neq 0$. 令 $x=0$, 则

$$
Q(0)+Q(1)=\sum_{i=0}^{n} a_{i}+2 a_{0}=1
$$

令 $x=\frac{1}{2}$, 则

$$
Q\left(\frac{1}{2}\right)+Q\left(\frac{1}{2}\right)=\sum_{i=0}^{n} 2^{1-n} a_{i}=1
$$

若 $n \geq 2$, 则 $\sum_{i=0}^{n} 2^{1-n} a_{i}<\sum_{i=0}^{n} a_{i}+2 a_{0}$, 矛盾!

故 $n \leq 1$, 且 $a_{1}+2 a_{0}=1$. 经检验显然成立.

因此满足题意的所有 $P(x)$ 为 $P(x)=c x^{2}+\frac{1-c}{2}, c \in[0,1]$.

评析 从非负系数角度考虑发现 $P(x)$ 仅有偶次项, 之后难度不大.

3. 已知存在一个由非零实数组成的 $2018 \times 2018$ 数表满足: 数表中任意一个数等于其所在行和列其余 4034 个数的和的 $k$ 分之一, 求整数 $k$ 的所有可能值.

解 设第 $i$ 行第 $j$ 列上的非零实数为 $a_{i j}$, 第 $i$ 行所有实数和为 $S_{i}$, 第 $j$ 列所有实数和为 $T_{j}, A=\sum_{i, j=1}^{2018} a_{i j}, 1 \leq i, j \leq 2018$. 则

$$
S_{i}=\sum_{j=1}^{2018} a_{i j}, T_{j}=\sum_{i=1}^{2018} a_{i j}, A=\sum_{i=1}^{2018} S_{i}=\sum_{j=1}^{2018} T_{j}
$$

由题意, 对于某个 $a_{i j}, 1 \leq i, j \leq 2018$ 有

$$
a_{i j}=\frac{1}{k}\left(\sum_{\substack{1 \leq r \leq 2018 \\ r \neq i}} a_{r j}+\sum_{\substack{1 \leq s \leq 2018 \\ s \neq j}} a_{i s}\right)=\frac{1}{k}\left(S_{i}+T_{j}-2 a_{i j}\right)
$$

即

$$
(k+2) a_{i j}=S_{i}+T_{j}
$$

所以

$$
\begin{aligned}
(k+2) A & =(k+2) \sum_{i, j=1}^{2018} a_{i j}=\sum_{i, j=1}^{2018}\left(S_{i}+T_{j}\right) \\
& =2018\left(\sum_{i=1}^{2018} S_{i}+\sum_{j=1}^{2018} T_{j}\right)=4036 A .
\end{aligned}
$$

若 $A \neq 0$, 则 $k=4034$. 将所有方格均填 1 可知 $k=4034$ 成立.

若 $A=0$, 则

$$
(k+2) S_{i}=(k+2) \sum_{j=1}^{2018} a_{i j}=\sum_{j=1}^{2018}\left(S_{i}+T_{j}\right)=2018 S_{i}+A=2018 S_{i} .
$$

即 $(k-2016) S_{i}=0$. 同理可知 $(k-2016) T_{j}=0$.

若存在 $i \in\{1,2, \cdots, 2018\}, S_{i} \neq 0$ 或 $T_{j} \neq 0$, 则 $k=2016$. 将前 1009 行所有方格填 1 , 其余方格填 -1 可知 $k=2016$ 成立.
否则 $S_{1}=S_{2}=\cdots=S_{2018}=T_{1}=T_{2}=\cdots=T_{2018}=0$. 又

$$
(k+2) a_{i j}=S_{i}+T_{j}=0,
$$

故 $k=-2$. 当 $k=-2$ 时, 将方格表中所有方格按照国际象棋盘的方式放入 $1,-1$ (即将 $1,-1$ 间隔着放入方格表中, 使得有公共边的两相邻方格内的数不同), 故 $k=-2$ 成立!

综上所述, $k=4034,-2,2016$.

评析难度不大且中规中矩的组合题. 考虑 $S_{i}, T_{j}$ 的性质是自然的, 唯一要注意的是需要细致的考虑避免漏解.
4. $P(x)$ 是一个非负整系数非零多项式. 已知存在正整数 $a$, 使得数列 $a_{1}=a, a_{n+1}=P\left(a_{n}\right)$ 满足: 集合 $A=\left\{p \mid p\right.$ 为某项 $a_{n}$ 的素因数 $\}$ 为有限集, 求所有满足条件的 $P(x)$.

解 考虑满足题意的 $P(x)$, 则存在正整数 $a$ 使得集合 $A$ 为有限集. 设 $A=\left\{p_{1}, p_{2}, \cdots, p_{t}\right\}$, 其中 $p_{1}, p_{2}, \cdots, p_{t}$ 为互不相同的素数.

显然 $P(x)$ 存在最小非零项, 设这一项为 $c x^{\alpha}(c, \alpha \in \mathbb{N}, c \neq 0)$.

若 $\alpha=0$, 令

$$
P^{(0)}(x)=x, P^{(n)}(x)=P\left(P^{(n-1)}(x)\right)\left(n \in \mathbb{N}^{*}\right) .
$$

由 $P\left(a_{n}\right) \equiv c\left(\bmod a_{n}\right)$ 及数学归纳法易知 $P^{(k)}\left(a_{n}\right) \equiv P^{(k-1)}(c)\left(\bmod a_{n}\right)$.即对任意的正整数 $n, k$ 均有

$$
a_{n+k} \equiv P^{(k-1)}(c)\left(\bmod a_{n}\right) .
$$

则 $\left(a_{n+k}, a_{n}\right) \leq P^{(k-1)}(c)$ 为仅依赖于 $k$ 的常数.

当 $P(x)=c(x \in \mathbb{R})$ 时显然符合题意. 否则, 由于 $P(x)$ 为非负整系数多项式, 则 $P(x)>x(x \geq 1)$. 故

$$
a_{n+1} \geq a_{n}+1, P^{(0)}(c)<P^{(1)}(c)<\cdots<P^{(t-1)}(c) .
$$

取正整数 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{t}$ 使得 $p_{i}^{\alpha_{i}}>P^{(t-1)}(c), i=1,2, \cdots, t$. 令 $T=\prod_{i=1}^{t} p_{i}^{\alpha_{i}}$.

由于 $a_{n+1} \geq a_{n}+1\left(n \in \mathbb{N}^{*}\right)$, 则 $\left\{a_{n}\right\}$ 为严格递增正整数序列. 因此存在正整数 $M$, 使得 $a_{M}>T$.

考虑下面 $t$ 个数 $a_{M}, a_{M+1}, \cdots, a_{M+t}$, 则有 $a_{M+t}>a_{M+t-1}>\cdots>a_{M}>T$.而由 $A$ 的定义可知: $a_{M}, a_{M+1}, \cdots, a_{M+t}$ 均可表示为 $p_{1}^{\gamma_{1}} p_{2}^{\gamma_{2}} \cdots p_{t}^{\gamma_{t}}$ 的形式. 故存在 $j \in\{1,2, \cdots, t\}$ 使得 $p_{j}^{\alpha_{j}} \mid a_{M}$, 否则 $a_{M} \leq \prod_{i=1}^{t} p_{i}^{\alpha_{i}-1}<T$, 矛盾!
同样对于 $a_{M+1}, \cdots, a_{M+t}$ 有上述结论.

因此, 由抽屉原理, 存在 $1 \leq j \leq t, 0 \leq k<l \leq t$ 使得 $p_{j}^{\alpha_{j}} \mid a_{M+k}$ 且 $p_{j}^{\alpha_{j}} \mid a_{M+l}$. 所以有

$$
p_{j}^{\alpha_{j}} \leq\left(a_{M+k}, a_{M+l}\right) \leq P^{(l-k-1)}(c) \leq P^{(t-1)}(c)<p_{j}^{\alpha_{j}} .
$$

矛盾!

若 $\alpha \geq 1$, 则有 $a_{n}^{\alpha} \mid a_{n+1}$. 令

$$
b_{n}=\frac{a_{n+1}}{a_{n}^{\alpha}}\left(n \in \mathbb{N}^{+}\right)
$$

则 $\left\{b_{n}\right\}$ 仍为整数数列.

设 $B=\left\{p \mid p\right.$ 为某项 $b_{n}$ 的素因数 $\}$. 显然 $B \subseteq A$, 故 $B$ 亦为有限集.

设 $B=\left\{q_{1}, q_{2}, \cdots, q_{s}\right\}$, 其中 $q_{1}, q_{2}, \cdots, q_{s}$ 为互不相同的素数.

当 $P(x)=c x^{\alpha}$ 时, 显然满足题意. 否则有 $b_{n+1} \geq b_{n}+1\left(n \in \mathbb{N}^{+}\right)$. 由于 $a_{n} \mid a_{n+1}\left(n \in \mathbb{N}^{+}\right)$, 又注意到对于 $k \in \mathbb{N}^{+}$, 有

$$
\frac{P\left(a_{n+k}\right)}{a_{n+k}^{\alpha}} \equiv c\left(\bmod a_{n+k}\right)
$$

则 $b_{n+k} \equiv c\left(\bmod a_{n+1}\right)$, 所以 $b_{n+k} \equiv c\left(\bmod b_{n}\right)$, 故 $\left(b_{n+k}, b_{n}\right) \leq c$.

取正整数 $\beta_{1}, \beta_{2}, \cdots, \beta_{s}$, 使得 $q_{i}^{\beta_{i}}>c, i=1,2, \cdots, s$. 令 $S=\prod_{i=1}^{s} q_{i}^{\beta_{i}}$.

再取正整数 $N$, 使得 $b_{N}>S$.

同理, 由抽屉原理知, 存在 $1 \leq j \leq s, 0 \leq k<l \leq s$, 使得 $q_{j}^{\beta_{j}} \mid b_{N+k}$ 且 $q_{j}^{\beta_{j}} \mid b_{N+l}$. 所以

$$
q_{j}^{\beta_{j}} \leq\left(b_{N+k}, b_{N+l}\right) \leq c<q_{j}^{\beta_{j}}
$$

矛盾!

综上所述, $P(x)=c x^{\alpha}\left(c \in \mathbb{N}^{+}, \alpha \in \mathbb{N}\right)$.

评析 本题具有一定的难度与区分度. 但这是一个很经典的题型, 即素因子个数有限无限问题.一般而言, 我们考虑假设某个整数系列 $\left\{a_{n}\right\}$ 可被有限个素数幂的乘积表示, 然后利用条件, 找到一个不依赖于下标 $n$ 的常数作为界限, 那么当 $a_{n}$ 有某些条件时即可导出矛盾. 寻找常熟常见的手法就有取某两项的最大公约数. 但本题难点在于它存在这样一个陷阱: 我们考虑到 $P(x)$ 是整系数多项式, 因此具有性质: $x-y \mid P(x)-P(y)(x, y \in \mathbb{Z})$, 希望利用这一性质找到所需的常数, 然而这样的处理得到的是 $\left\{a_{n}\right\}$ 的差分形式, 与 $\left\{a_{n}\right\}$ 本身性质有所偏离,从而做起来特别困难. 另一个难点在于, 怎样将 $\alpha \geq 1$ 的情形划归到 $\alpha=0$ 的证明, 需要注意这里考虑用 $\frac{P(x)}{x^{\alpha}}$ 代替 $P(x)$ 是不正确的.

## 二、 清华测试试题

1. 设正实数 $a_{1}, a_{2}, \cdots$ 满足 $a_{1}+a_{2}+\cdots+a_{n} \leq n^{2}, \forall n \in \mathbb{N}^{+}$. 求证: 对 $\forall n \in \mathbb{N}^{+}$,

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}>\frac{1}{4} \log _{2} n .
$$

证明 先证:

$$
\sum_{i=2}^{2^{m}} \frac{1}{a_{i}}>\frac{m}{4}
$$

对非负整数 $k$, 由柯西不等式得

$$
\left(\sum_{i=2^{k}+1}^{2^{k+1}} a_{i}\right)\left(\sum_{i=2^{k}+1}^{2^{k+1}} \frac{1}{a_{i}}\right) \geq 2^{2 k}
$$

则

$$
\sum_{i=2^{k}+1}^{2^{k+1}} \frac{1}{a_{i}} \geq \frac{2^{2 k}}{\sum_{i=2^{k}+1}^{2^{k+1}} a_{i}}>\frac{2^{2 k}}{\sum_{i=1}^{2^{k+1}} a_{i}} \geq \frac{2^{2 k}}{2^{2 k+2}}=\frac{1}{4}
$$

故

$$
\sum_{i=2}^{2^{m}} \frac{1}{a_{i}}=\sum_{k=0}^{m-1}\left(\sum_{i=2^{k}+1}^{2^{k+1}} \frac{1}{a_{i}}\right)>\frac{m}{4}
$$

(1) 式得证.

在 $(1)$ 式中取 $m=\left\lfloor\log _{2} n\right\rfloor$, 得

$$
\sum_{i=2}^{n} \frac{1}{a_{i}}>\frac{1}{4}\left\lfloor\log _{2} n\right\rfloor
$$

从而

$$
\sum_{i=1}^{n} \frac{1}{a_{i}}>1+\frac{1}{4}\left\lfloor\log _{2} n\right\rfloor>\frac{1}{4} \log _{2} n .
$$

命题得证.

另证 1 不妨设 $a_{1} \leq a_{2} \leq \cdots$. 事实上, 设 $a_{i_{1}} \leq a_{i_{2}} \leq \cdots \leq a_{i_{n}}$, 则显然对于任意正整数 $n$,

$$
a_{i_{1}}+a_{i_{2}}+\cdots+a_{i_{n}} \leq \sum_{i=1}^{n} a_{i} \leq n^{2} \quad \text { 且 } \quad \frac{1}{a_{i_{1}}}+\frac{1}{a_{i_{2}}}+\frac{1}{a_{i_{n}}} \geq \sum_{j=1}^{n} \frac{1}{a_{j}} \text {. }
$$

令

$$
S_{m}=\sum_{i=1}^{m}\left(2 i-1-a_{i}\right)=m^{2}-\sum_{i=1}^{m} a_{m} \geq 0, x_{k}=\frac{1}{a_{k}(2 k-1)}>0 .
$$

由于 $(2 i-1) a_{i}<(2 i+1) a_{i+1}, i \in \mathbb{N}^{+}$, 故 $x_{i}>x_{i+1}, i \in \mathbb{N}^{+}$. 则由 Abel 求和公式,有

$$
\sum_{i=1}^{n}\left(\frac{1}{a_{i}}-\frac{1}{2 i-1}\right)=\sum_{i=1}^{n} \frac{2 i-1-a_{i}}{a_{i}(2 i-1)}=S_{n} x_{n}+\sum_{i=1}^{n-1} S_{i}\left(x_{i}-x_{i+1}\right) \geq 0 .
$$

令

$$
f(x)=x-\frac{1}{2} \log _{2}(x+1)
$$

则

$$
f(0)=0, f^{\prime}(x)=1-\frac{1}{(x+1) \ln 4}>0(x>0) .
$$

因此 $f(x) \geq 0(x \geq 0)$.

令 $x=\frac{1}{i}, i \in \mathbb{N}^{+}$, 则有

$$
\frac{1}{i} \geq \frac{1}{2} \log _{2}\left(\frac{i+1}{i}\right)
$$

所以有

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{1}{a_{i}} \geq \sum_{i=1}^{n} \frac{1}{2 i-1} \geq \frac{1}{2} \sum_{i=1}^{n} \frac{1}{i} & \geq \frac{1}{4} \sum_{i=1}^{n} \log _{2}\left(\frac{i+1}{i}\right) \\
& =\frac{1}{4} \log _{2}(n+1)>\frac{1}{4} \log _{2} n .
\end{aligned}
$$

证毕!

则有

另证 2 设 $S_{n}=\sum_{i=1}^{n} a_{n}, n \in \mathbb{N}^{+}$, 则 $S_{n}=a_{n}+S_{n-1}(n \geq 2)$. 由柯西不等式,

$$
\frac{(n+1)^{2}}{S_{n}} \leq \frac{4}{a_{n}}+\frac{(n-1)^{2}}{S_{n-1}} \quad(n \geq 2)
$$

所以

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{2 i+1}{S_{i}} & =\sum_{i=1}^{n}\left(\frac{(i+1)^{2}}{S_{i}}-\frac{i^{2}}{S_{i}}\right) \\
& \leq \sum_{i=2}^{n}\left(\frac{4}{a_{i}}+\frac{(i-1)^{2}}{S_{i-1}}+\frac{i^{2}}{S_{i}}\right)+\frac{4}{a_{1}}-\frac{1}{S_{1}} \\
& <4 \sum_{i=1}^{n} \frac{1}{a_{i}} .
\end{aligned}
$$

故

$$
\sum_{i=1}^{n} \frac{1}{a_{i}}>\sum_{i=1}^{n} \frac{2 i+1}{4 S_{i}}>\sum_{i=1}^{n} \frac{1}{2 i}>\frac{1}{4} \log _{2} n .
$$

证毕!

评析 第一种证法类似于调和级数发散的证明,把数列分成若干段证明每
一段的和大于某个常数, 这里用柯西不等式分段放缩可以证得每一段大于 $\frac{1}{4}$.第二种证明类似于优超不等式的证法, 先把数列按从小到大顺序重排, 然后注意到递增关系与分段和的符号, 利用 Abel 变换公式就可以证得结论. 当然,当然, 也可以直接由优超或 Karamata 不等式直接得到 $\sum_{i=1}^{n}\left(\frac{1}{a_{i}}-\frac{1}{2 i-1}\right) \geq 0$. 不过由于这里放缩不需要取等, 所以用柯西不等式裂项也可以证明, 注意不等式 $\sum_{i=1}^{n} \frac{1}{a_{i}}>\sum_{i=1}^{n} \frac{2 i+1}{4 S_{i}}$ 只需要条件 $a_{1}, a_{2}, \cdots, a_{n}>0$.

2. 给定凸多边形 $A_{1} A_{2} \cdots A_{n}$. 证明: 存在凸多边形内部一点 $P$, 使得对任意过点 $P$ 的直线 $l, l$ 与凸多边形 $A_{1} A_{2} \cdots A_{n}$ 的边界交于 $U, V$ 两点, 且满足

$$
\frac{1}{2} \leq \frac{P U}{P V} \leq 2
$$

证明 如下图所示, 考虑 $\mathrm{C}_{n}^{3}$ 个三角形 $\triangle A_{i} A_{j} A_{k}(1 \leq i<j<k \leq n)$ 中面积最大的三角形 (如果有多个任选一个), 不妨设这个三角形为 $\triangle A B C$. 过点 $A, B, C$ 分别作对边的平行线, 交于点 $A^{\prime}, B^{\prime}, C^{\prime}$, 则凸多边形 $A_{1} A_{2} \cdots A_{n}$ 被 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 覆盖, 否则存在面积更大的三角形, 与最大性矛盾!



取点 $P$ 为 $\triangle A B C$ 的重心, 下面说明点 $P$ 满足题意.

任取过 $P$ 的直线 $l$, 设 $l$ 与凸多边形 $A_{1} A_{2} \cdots A_{n}$ 的边界交于 $U, V$ 两点. 如图所示, 不妨设 $U$ 在 $\triangle A^{\prime} B C$ 中, $V$ 在 $\triangle A B^{\prime} C$ 中且 $P U \geq P V$, 设 $l$ 与 $A C, A^{\prime} C^{\prime}$分别交于 $V^{\prime}, U^{\prime}$, 则 $P U^{\prime} \geq P U, P V^{\prime} \leq P V$.

设 $M$ 为 $A C$ 的中点, 则 $M, P, B$ 三点共线且 $\frac{P M}{P B}=\frac{1}{2}$. 由于 $A C / / A^{\prime} C^{\prime}$, 则

$$
1 \leq \frac{P U}{P V} \leq \frac{P U^{\prime}}{P V^{\prime}}=\frac{P B}{P M}=2 .
$$

另证 先证如下引理.

引理 设凸四边形 $A B C D$ 两条对角线 $A C, B D$ 交于点 $O$. 点 $U, V$ 分别在线段 $A B$ 和线段 $C D$ 上,则

$$
\min \left\{\frac{O A}{O C}, \frac{O B}{O D}\right\} \leq \frac{O U}{O V} \leq \max \left\{\frac{O A}{O C}, \frac{O B}{O D}\right\}
$$



引理的证明 过 $V$ 做 $A B$ 的平行线交 $O C$ 于 $C^{\prime}$, 交 $O D$ 于 $D^{\prime}$. 则 $C^{\prime}$ 在线段 $O C$ 上, $D^{\prime}$ 在线段 $O D$ 外; 或者 $C^{\prime}$ 在线段 $O C$ 外, $D^{\prime}$ 在线段 $O D$ 上.

不妨设 $C^{\prime}$ 在线段 $O C$ 上, $D^{\prime}$ 在线段 $O D$ 外. 则

$$
\frac{O U}{O V}=\frac{O A}{O C^{\prime}}=\frac{O B}{O D^{\prime}}, \quad O C^{\prime} \leq O C, O D^{\prime} \geq O D
$$

于是

$$
\frac{O A}{O C} \leq \frac{O U}{O V} \leq \frac{O B}{O D}
$$

引理获证.

回到原题. 先说明如果凸多边形内部存在一点 $P$, 使得对凸多边形任一顶点 $A$, 直线 $A P$ 交凸多边形于另一点 $B$, 都有 $\frac{P A}{P B} \leq 2$, 则这个点 $P$ 也满足题目要求.



设过 $P$ 的直线交 $A_{i} A_{i+1}$ 于 $U$, 交 $A_{j} A_{j+1}$ 于 $V$.

设直线 $P A_{i}$ 和 $P A_{i+1}$ 分别交直线 $A_{j} A_{j+1}$ 于 $A_{j}^{\prime}$ 和 $A_{j+1}^{\prime}$, 则由引理知,

$$
\frac{P U}{P V} \leq \max \left\{\frac{P A_{i+1}}{P A_{j+1}^{\prime}}, \frac{P A_{i}}{P A_{j}^{\prime}}\right\} \leq \max \left\{\frac{P A_{i+1}}{P B_{i+1}}, \frac{P A_{i}}{P B_{i}}\right\} \leq 2
$$

同理, $\frac{P V}{P U} \leq 2$. 故

$$
\frac{1}{2} \leq \frac{P U}{P V} \leq 2
$$

下面证明存在一个点 $P$ 满足上述条件.

作凸多边形形内的凸集 $P_{i}$, 其边界围成的凸 $n$ 多边形与 $A_{1} A_{2} \cdots A_{n}$ 关于点 $A_{i}$ 按照 $\frac{2}{3}$ 的比例位似, $i=1,2, \cdots, n$. 因此, 若点 $P$ 在 $P_{i}$ 中, 设 $A_{i} P$ 交凸多边形于另一点 $Q$, 则 $\frac{P A_{i}}{P Q} \leq 2$.



故我们只需证明 $P_{1} \cap P_{2} \cap \cdots \cap P_{n} \neq \emptyset$.

对任意 $1 \leq i<j<k \leq n$, 设 $\triangle A_{i} A_{j} A_{k}$ 的重心为点 $G$, 则 $G \in P_{i} \cap P_{j} \cap P_{k}$.

事实上, 取点 $J, k$ 分别在线段 $A_{i} A_{j}, A_{i} A_{k}$ 上且满足 $\frac{A_{i} J}{A_{j} J}=\frac{A_{i} K}{A_{k} K}=2$. 则由凸集 $P_{i}$ 的定义可知 $J, K \in P_{i}$. 又显然 $J, K, G$ 三点共线, 故 $G \in P_{i}$. 同理则有 $G \in P_{i} \cap P_{j} \cap P_{k}$, 故 $P_{i} \cap P_{j} \cap P_{k} \neq \emptyset$.

由海莱定理, $P_{1} \cap P_{2} \cap \cdots \cap P_{n} \neq \emptyset$, 故本题得证.

评析两种做法考虑的方式不同. 前一种希望直接构造, 由于题目要求是一个范围, 从而希望利用直径, 最大三角形等方式控制其范围, 然后去寻找特殊点.而 $2: 1$ 的比例容易联想到重心, 故从质心或者某个特殊三角形的重心出发去构造, 或许小情况对题目的构造有所启发; 另一种方式希望证明其存在性. 因而选取凸多边形上一点, 找到由这个点得到的满足条件的范围, 然后希望证明存在一个点在每个范围中, 这就让人联想到了海莱定理. 但为了避免运用无穷多个凸集的海莱定理 (这个定理证明用到了数学分析中的有限覆盖定理), 因而考虑转化为对顶点产生的凸集运用有限凸集的海莱定理.

3. 设 $n$ 为大于 100 的正整数. 对任意不超过 $n$ 的素数 $p$, 记 $\alpha_{p}$ 为 $n$ ! 中 $p$ 的次数, 证明: 可以对每个不超过 $n$ 的素数 $p$, 指定一个不超过 $n$ 的互不相同的正整数 $\beta_{p}$, 使得 $1+\alpha_{p} \mid \beta_{p}$.

证明 由勒让德公式

$$
\alpha_{p}=\sum_{k=1}^{\infty}\left[\frac{n}{p^{k}}\right]=\frac{n-S_{p}(n)}{p-1}
$$

其中 $S_{p}(n)$ 表示正整数 $n$ 在 $p$ 进制表示下的数码和.

考虑不超过 $n$ 的素数从小到大排列为 $2=p_{1}<p_{2}<\cdots<p_{t}$. 下面逐步构造 $\beta_{p_{1}}, \beta_{p_{2}}, \cdots, \beta_{p_{t}}$ 使得 $1+\alpha_{p} \mid \beta_{p}$.

$$
\begin{aligned}
& \text { 令 } \beta_{p_{1}}=\beta_{2}=\alpha_{2}+1, \beta_{p_{2}}=\beta_{3}=\alpha_{3}+1 \text {. 由于 } \\
& \alpha_{2}=n-S_{2}(n) \geq n-1-\log _{2} n>\frac{n}{2}>\frac{n-S_{3}(n)}{2}=\alpha_{3}(n>100),
\end{aligned}
$$

故 $\beta_{2} \neq \beta_{3}\left(\beta_{2}>\beta_{3}\right)$. 再考虑 $\beta_{5}$, 注意到

$$
3\left(\alpha_{5}+1\right)=\frac{3}{4}\left(n+4-S_{5}(n)\right)<\frac{3}{4}(n+4) \leq n(n>100)
$$

故存在 $s \in\{1,2,3\}, s\left(\alpha_{5}+1\right) \in\{1,2, \cdots, n\} \backslash\left\{\beta_{2}, \beta_{3}\right\}$. 令 $\beta_{5}=s\left(\alpha_{5}+1\right)$. 进一步考虑构造 $\beta_{7}$. 因为

$$
4\left(\alpha_{7}+1\right)=\frac{2}{3}\left(n+6-S_{7}(n)\right)<\frac{2}{3}(n+6) \leq n(n>100),
$$

故存在 $r \in\{1,2,3,4\}, r\left(\alpha_{7}+1\right) \in\{1,2, \cdots, n\} \backslash\left\{\beta_{2}, \beta_{3}, \beta_{5}\right\}$. 令 $\beta_{7}=r\left(\alpha_{7}+1\right)$.故上述构造得到的 $\beta_{2}, \beta_{3}, \beta_{5}, \beta_{7}$ 符合题意.

下面进一步构造 $\beta_{p_{5}}, \cdots, \beta_{p_{t}}$. 对于 $5 \leq k \leq t$, 假设已经构造好了 $\beta_{p_{1}}, \beta_{p_{2}}, \cdots$, $\beta_{p_{k-1}}$, 考虑到当 $k \geq 5$ 时, 有 $p_{k} \geq 2 k+1$. 由此可知

$$
\begin{aligned}
k\left(\alpha_{p_{k}}+1\right) \leq\left(\frac{p_{k}-1}{2}\right)\left(\alpha_{p_{k}}+1\right) & =\frac{1}{2}\left(n+p_{k}-1-S_{p_{k}}(n)\right) \\
& <\frac{1}{2}\left(n+p_{k}\right) \leq n .
\end{aligned}
$$

故存在 $q \in\{1,2, \cdots, k\}, q\left(\alpha_{p_{k}}+1\right) \in\{1,2, \cdots, n\} \backslash\left\{\beta_{p_{1}}, \beta_{p_{2}}, \cdots, \beta_{p_{k-1}}\right\}$.

由此构造得到的 $\beta_{p_{1}}, \beta_{p_{2}}, \cdots, \beta_{p_{t}}$ 显然符合题意, 证毕!

评析 考虑到对于 $1 \leq k \leq t$, , 均有 $\beta_{p_{k}}=q\left(\alpha_{p_{k}}+1\right)$, 我们需要 $\beta$ 不大于 $n$, 因此 $q$ 的取值是有限的, 一次性全部构造出来很有可能存在素数 $1 \leq p<p^{\prime} \leq n, \beta_{p}=\beta_{p^{\prime}}$, 故我们不急着一步到位，一步步地构造，因此自然地想从 $\beta_{p_{2}}$ 开始构造. 考虑将 $q$ 的取值估计出来, 接下来将小情况去掉以后可以很轻松地证明存在满足题意的 $q$. 值得一提的是, 我们由此题可以立刻推得如下题目的解答: $n \in \mathbb{N}, n>100$, 则 $\tau(n !) \mid n !$.

4. 设 $n, a, b \in \mathbb{N}^{+}, a \leq b \leq n-a, X=\{1,2, \cdots, n\}$, 给定 $A_{0}$ 为 $X$ 的 $a$ 元子集。

(1) 设 $A \subseteq X,|A|=a,\left|A \cap A_{0}\right|=i$, 对 $0 \leq j \leq a$, 求满足以下条件的集合 $B$ 的个数:

$$
A \subseteq B \subseteq X,|B|=b,\left|B \cap A_{0}\right|=j
$$

(2) 证明: 可以给每个 $X$ 的 $b$ 元子集 $B$ 赋上实数 $f(B)$, 使得对 $A \subseteq X,|A|=$ $a$, 均满足:

$$
\sum_{\substack{A \subseteq B \subseteq X,|B|=b}} f(B)= \begin{cases}0, & A \neq A_{0} \\ 1, & A=A_{0}\end{cases}
$$

解 (1) 满足条件的集合 $B$ 的个数为 $\mathrm{C}_{a-i}^{j-i} \mathrm{C}_{n+i-2 a}^{b-a+i-j}$.

令 $S=B \backslash A$, 则有: $S=\left(S \cap A_{0}\right) \cup\left(S \backslash A_{0}\right)$. 注意到

$$
\begin{aligned}
& \left|S \cap A_{0}\right|=j-i ; \\
& S \cap A_{0} \subseteq A_{0} \backslash A,\left|A_{0} \backslash A\right|=a-i ; \\
& \left|S \backslash A_{0}\right|=|B|-\left|A_{0} \cap B\right|-|A|+\left|A \cap A_{0}\right|=b-j-a+i ; \\
& S \backslash A_{0} \subseteq X \backslash\left(A \cup A_{0}\right), \quad\left|X \backslash\left(A \cup A_{0}\right)\right|=n+i-2 a .
\end{aligned}
$$

故 $S$ 的选取共有 $\mathrm{C}_{a-i}^{j-i} \mathrm{C}_{n+i-2 a}^{b-a+i-j}$ 种, 因此有 $\mathrm{C}_{a-i}^{j-i} \mathrm{C}_{n+i-2 a}^{b-a+i-j}$ 个满足条件的 $B$.

(2) 对于整数 $j \in[i, a]$, 将满足 $A \subseteq B \subseteq X,|B|=b,\left|A_{0} \cap B\right|=j$ 的所有集合 $B$ 赋值 $x_{j}$, 下面说明存在数组 $\left(x_{0}, x_{1}, \cdots, x_{a}\right) \in \mathbb{R}^{a+1}$ 使得

$$
\sum_{\substack{A \subseteq B \subseteq X,|B|=b}} f(B)=\left\{\begin{array}{ll}
0, & A \neq A_{0} \\
1, & A=A_{0}
\end{array} .\right.
$$

对于集合 $A \subseteq X,|A|=a,\left|A \cap A_{0}\right|=i$, 由 (1) 及 $x_{j}$ 的定义可知

$$
\sum_{A \subseteq B \subseteq X,|B|=b} f(B)=\sum_{j=i}^{a} \mathrm{C}_{a-i}^{j-i} \mathrm{C}_{n+i-2 a}^{b-a+i-j} x_{j} \quad(i=0,1, \cdots, a)
$$

设 $g(i)=\sum_{j=i}^{a} \mathrm{C}_{a-i}^{j-i} \mathrm{C}_{n+i-2 a}^{b-a+i-j} x_{j}$. 令 $g(a)=1$, 故 $\mathrm{C}_{n-a}^{b-a} x_{a}=1$, 则 $x_{a}=\frac{1}{\mathrm{C}_{n-a}^{b-a}}$.

进一步地, 令 $g(a-1)=\cdots=g(0)=0$. 由于 $g(a-1)=0, x_{a}=\frac{1}{\mathrm{C}_{n-a}^{b-a}}$, 而 $g(a-1)$ 中 $x_{a-1}$ 的系数为 $\mathrm{C}_{n-a-1}^{b-a} \neq 0$. 由此可解得 $x_{a-1}$, 依此类推可以依次解得实数 $x_{a-1}, \cdots, x_{0}$. 至此, 我们将 $X$ 的所有 $b$ 元子集赋上了某个实数且满足

$$
\sum_{\substack{A \subseteq B \subseteq X,|B|=b}} f(B)=g\left(\left|A \cap A_{0}\right|\right)
$$

由于 $g(a)=1, g(a-1)=\cdots=g(0)=0$. 故

$$
\sum_{\substack{A \subseteq B \subseteq X,|B|=b}} f(B)=\left\{\begin{array}{ll}
0, & A \neq A_{0} \\
1, & A=A_{0}
\end{array} .\right.
$$

证毕!

评析 此题难点在于看上去很复杂, 但由于第一问提示性是明显的, 极大降低了难度, 故第二问考虑将满足 $A \subseteq B \subseteq X,|B|=b,\left|A_{0} \cap B\right|=j$ 的所有集合 $B$ 赋值 $x_{j}$ 是自然的. 而说明 $x_{j}$ 有解只需要将式子一个一个解出来, 与上一题思想相同, 不必急于一次性解出所有的量, 而是通过分步骤依次解决从而逐渐得到我们想要的结果.

## III. 总 评

总的来说, 考试难度基本上和联赛相近, 也具有较好的区分度, 但联赛和两次测试题型及侧重点有所差异. 北大的测试更倾向于数学竞赛的风格, 而清华的题目高等数学的意味有点重. 尽管都是几何代数组合数论四个板块各一题, 但也可以发现, 北大的测试偏重于多项式板块, 其中多项式在代数和数论中的题型均有考察. 另外, 北大的四个题均为解答题, 这也考察学生的探索能力和细致程度 (例如北大的第三题不少人存在漏解的情况). 而清华对于几何的考察, 侧重于组合几何板块, 而并非我们所常见的几何题, 另外有趣的是, 与北大相反, 清华考察的四个题均为证明题, 且其中有三个题是证明存在性问题, 并且均可直接构造,考察同学的思维创造能力. 总而言之, 两场考试都具有对能力的全面考察, 做出三道题就具有一定的竞争力.

