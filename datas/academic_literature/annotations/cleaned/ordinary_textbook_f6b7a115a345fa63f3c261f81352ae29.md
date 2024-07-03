数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2023 年上海新星秋季数学奥林匹克试题解析 

胡珏伟 1 吴尉迟 ${ }^{2}$ 罗振华 2

(1. 上海大学, 200444；2. 华东师范大学, 200241)

2023 年上海新星秋季数学奥林匹克于 2023 年 12 月 01 日 $8: 00-12: 00$ 在上海举行. 下面介绍此次考试的试题和解答. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 点 $I$ 是 $\triangle A B C$ 的内心, $\odot O$ 是其外接圆. 点 $C$ 关于 $\odot O$ 的对径点为 $D$.点 $A_{1}$ 是 $\triangle A B C$ 的 $A-$ 旁切圆与 $B C$ 的切点, 点 $B_{1}$ 是 $\triangle A B C$ 的 $B-$ 旁切圆与 $A C$ 的切点. 证明: $I D$ 关于 $I C$ 的对称直线与直线 $A_{1} B_{1}$ 垂直.

(华东师范大学 罗振华供题)

2. 求所有的整数 $n \geq 3$, 使得存在正实数 $a_{1}<a_{2}<\cdots<a_{n}$, 满足

$$
a_{1} a_{2}-a_{3}, \quad a_{2} a_{3}-a_{4}, \quad \cdots, \quad a_{n-1} a_{n}-a_{1}, \quad a_{n} a_{1}-a_{2}
$$

按此顺序构成一个等比数列.

(中国人民大学附属中学张端阳供题)

3. 求所有的非平方数的正整数 $n$, 使得关于正整数 $x, y$ 的不定方程 $x^{2}-4 y^{2}=n$ 有奇数个解.

(华东师范大学 吴尉迟 供题)

4. 设 $a_{1}, a_{2}, \cdots, a_{2023}$ 均为非负实数满足 $a_{1}+a_{2}+\cdots+a_{2023}=1$. 求

的最大值, 其中 $a_{2024}=a_{1}$.

$$
\sum_{i=1}^{2023} \min \left\{a_{i}, a_{i+1}\right\}^{2}
$$

(西安交通大学学生 林逸沿 供题)

修订日期: 2023-12-17.

5. 点 $H$ 是 $\triangle A B C$ 的垂心, 点 $E, F$ 分别是边 $A C, A B$ 上高的垂足. 点 $M$为线段 $B C$ 的中点. 延长 $A H, B H, C H$ 再次交外接圆于点 $K, Q, P . K F, K E$再次交外接圆于点 $S, T$. 证明: 若 $S, H, M$ 三点共线, 则 $S Q, P T, A C$ 三线共点.

(清华大学学生 江城 供题)

6. 给定正整数 $n \geq 2 k$ 和正整数 $e_{1}, e_{2}, \cdots, e_{k}$, 其中

$$
e_{1}+\cdots+e_{k}=\left(\begin{array}{c}
n \\
2
\end{array}\right)
$$

证明: 可以用 $k$ 种颜色 $1,2, \cdots, k$ 将完全图 $K_{n}$ 染色, 满足:

(1) 颜色 $i$ 的边恰有 $e_{i}$ 条;

(2) 对任意 $K_{n}$ 中四个点, 连接他们的边中至多使用了五种颜色.

(华威大学 吴茁供题)

## II. 解答与评注

题 1 点 $I$ 是 $\triangle A B C$ 的内心, $\odot O$ 是其外接圆. 点 $C$ 关于 $\odot O$ 的对径点为 $D$. 点 $A_{1}$ 是 $\triangle A B C$ 的 $A-$ 旁切圆与 $B C$ 的切点, 点 $B_{1}$ 是 $\triangle A B C$ 的 $B-$ 旁切圆与 $A C$ 的切点. 证明: $I D$ 关于 $I C$ 的对称直线与直线 $A_{1} B_{1}$ 垂直.



证明 设 $I D$ 关于 $I C$ 的对称直线为 $l, I_{C}$ 为 $\triangle A B C$ 的 $C$-旁心, $\odot I_{c}$ 分别切 $C B, C A$ 延长线于点 $A_{2}, B_{2}, I I_{c}$ 交 $\odot O$ 于点 $E$. 由鸡爪定理知 $E I_{c}=E I$, 结合 $\angle D E C=90^{\circ}$ 知 $\angle D I_{c} I=\angle D I I_{c}$, 因此 $D I_{C} / / l$.

记 $B C=a, C A=b, A B=c, p=\frac{1}{2}(a+b+c)$, 则

$$
C A_{2}=C B_{2}=p, C A_{1}=p-b, C B_{1}=p-a,
$$

$$
B A_{1}=A B_{1}=p-c, A_{1} A_{2}=b, B_{1} B_{2}=a .
$$

故

$$
A_{1} I_{C}^{2}-B_{1} I_{C}^{2}=A_{1} A_{2}^{2}+A_{2} I_{c}^{2}-\left(B_{1} B_{2}^{2}-B_{2} I_{c}^{2}\right)=b^{2}-a^{2}
$$

又由于

$$
C D^{2}-A_{1} D^{2}=B C^{2}-B A_{1}^{2}, C D^{2}-B_{1} D^{2}=A C^{2}-A B_{1}^{2} .
$$

两式相减有

$$
A_{1} D^{2}-B_{1} D^{2}=b^{2}-a^{2} .
$$

故

$$
A_{1} I_{C}{ }^{2}-B_{1} I_{C}{ }^{2}=A_{1} D^{2}-B_{1} D^{2}
$$

因此 $A_{1} B_{1} \perp D I_{C}$, 从而 $A_{1} B_{1} \perp l$.

评注 此题是简单的几何题, 考试中约 $50 \%$ 做对此题. 问题的关键是作出旁切圆 $\odot I_{c}$, 将问题转化为证明 $I_{c} D \perp A_{1} B_{1}$. 便可利用等差幂线定理得到证明.

题 2 求所有的整数 $n \geq 3$, 使得存在正实数 $a_{1}<a_{2}<\cdots<a_{n}$, 满足

$$
a_{1} a_{2}-a_{3}, \quad a_{2} a_{3}-a_{4}, \quad \cdots, \quad a_{n-1} a_{n}-a_{1}, \quad a_{n} a_{1}-a_{2}
$$

按此顺序构成一个等比数列.

解 设公比为 $q$. 由序关系知

$$
a_{1} a_{2}-a_{3}<a_{n} a_{1}-a_{2}, \quad a_{n-1} a_{n}-a_{1}>a_{n} a_{1}-a_{2},
$$

所以 $q<0$. 进而

$$
a_{1} a_{2}-a_{3}<a_{n} a_{1}-a_{2}<0<a_{n-1} a_{n}-a_{1},
$$

所以 $-1<q<0$.

若 $n \geq 4$, 则由 $(*)$ 及 $-1<q<0$ 知

$$
a_{2} a_{3}-a_{4}<a_{n-1} a_{n}-a_{1}=q^{n-3}\left(a_{2} a_{3}-a_{4}\right) .
$$

又 $a_{2} a_{3}-a_{4}>0$, 所以 $q^{n-3}>1$, 与 $-1<q<0$ 矛盾 ! 故 $n=3$.

当 $n=3$ 时, 取 $a_{1}=\frac{1}{4}, a_{2}=\frac{1}{2}$, 则

$$
\left(\frac{1}{2} a_{3}-\frac{1}{4}\right)^{2}=\left(\frac{1}{8}-a_{3}\right)\left(\frac{1}{4} a_{3}-\frac{1}{2}\right) .
$$

解得 $a_{3}=\frac{25+3 \sqrt{41}}{32}>\frac{1}{2}$, 满足要求.

综上, 所求正整数只有 3 .
评注 此题是中等的代数题, 考试中约 $11 \%$ 做对此题. 问题的关键在于发现 $-1<q<0$ 并比较第二项和倒数第二项的大小关系. 实际测试中很多学生没有注意到这一点.

题 3 求所有的非平方数的正整数 $n$, 使得关于正整数 $x, y$ 的不定方程 $x^{2}-4 y^{2}=n$ 有奇数个解.

解 设 $n$ 的质因数分解为

$$
n=2^{\alpha} \prod_{i=1}^{s} p_{i}^{\alpha_{i}} \prod_{i=1}^{t} q_{j}^{\beta_{j}}
$$

其中 $p_{i}, q_{j}$ 均为质数且 $p_{i} \equiv 1(\bmod 4), q_{j} \equiv 3(\bmod 4)$. 令

$$
u=x-2 y, v=x+2 y
$$

则不定方程 $x^{2}-4 y^{2}=n$ 有奇数个解等价于

$$
\left\{\begin{array}{l}
u v=n \\
u \equiv v \quad(\bmod 4) \\
u<v
\end{array}\right.
$$

的解的数量为奇数. 由 $n$ 为非平方数, 故不考虑 $u<v$ 条件的解的数量必须是奇数的两倍. 即正因子的个数是奇数的两倍. 下面分三种情况讨论:

(1) 若解满足 $u \equiv v \equiv 1$ 或 $3(\bmod 4)$, 则 $\alpha=0$ 且 $\sum_{i=1}^{t} \beta_{j}$ 是偶数. $n$ 的正因子的个数

$$
\prod_{i=1}^{s}\left(\alpha_{i}+1\right) \prod_{i=1}^{t}\left(\beta_{j}+1\right)
$$

为奇数的两倍. 此时恰存在一个 $\alpha_{i}$ 为奇数且为 $4 k+1$ 型, 即 $n=p^{4 k+1} m^{2}$, 其中 $p$ 是素数满足 $p \equiv 1(\bmod 4), m$ 为奇数且与 $p$ 互素.

(2) 若解满足 $u \equiv v \equiv 2(\bmod 4)$, 则 $\alpha=2$. 同上述讨论可知

$$
\prod_{i=1}^{s}\left(\alpha_{i}+1\right) \prod_{i=1}^{t}\left(\beta_{j}+1\right)
$$

为奇数的两倍. 此时恰存在一个 $\alpha_{i}$ 或 $\beta_{j}$ 为奇数且为 $4 k+1$ 型, 即 $n=4 p^{4 k+1} m^{2}$,其中 $p$ 是素数, $m$ 为奇数且与 $p$ 互素.

(3) 若解满足 $u \equiv v \equiv 0(\bmod 4)$, 则 $\alpha \geqslant 4$ 且此时 $u$ 和 $v$ 都是 4 的倍数. 需满足

$$
(\alpha-3) \prod_{i=1}^{s}\left(\alpha_{i}+1\right) \prod_{i=1}^{t}\left(\beta_{j}+1\right)
$$

为奇数的两倍. 此时又分为如下两种情况讨论:

(1) 若 $\alpha$ 为偶数, 则与上述情况相同需要恰存在一个 $\alpha_{i}$ 或 $\beta_{j}$ 为奇数且为 $4 k+1$ 型, 即 $n=2^{\alpha} p^{4 k+1} m^{2}$, 其中 $\alpha \geq 4$ 为偶数 $p$ 是素数, $m$ 为奇数且与 $p$ 互素.

(2) 若 $\alpha$ 为奇数, 则需满足 $\alpha \equiv 1(\bmod 4)$ 且 $\alpha_{i}$ 和 $\beta_{j}$ 均为偶数, 即 $n=2^{\alpha} m^{2}$,其中 $\alpha \equiv 1(\bmod 4)$ 且 $\alpha \geq 5, m$ 为奇数.

综上, 即找出了所有满足条件的 $n$.

评注 此题是中等的数论题, 考试中约 $14 \%$ 做对此题. 本题的关键在于发现两个因子模 4 同余, 然后按余数分类对正因子个数讨论就可以得到所有的 $n$.

题 4 设 $a_{1}, a_{2}, \cdots, a_{2023}$ 均为非负实数满足 $a_{1}+a_{2}+\cdots+a_{2023}=1$. 求

$$
\sum_{i=1}^{2023} \min \left\{a_{i}, a_{i+1}\right\}^{2}
$$

的最大值, 其中 $a_{2024}=a_{1}$.

解 不妨设 $a_{2023}=\min _{1 \leq i \leq 2023}\left\{a_{i}\right\}$. 有

$$
\begin{aligned}
\sum_{i=1}^{2023} \min \left\{a_{i}, a_{i+1}\right\}^{2} & \leq \sum_{i=1}^{2023} a_{i} \cdot a_{i+1} \\
& \leq \sum_{i=1}^{2022} a_{i} \cdot a_{i+1}+a_{2023} a_{1} \\
& \leq\left(a_{1}+a_{3}+\cdots+a_{2023}\right)\left(a_{2}+a_{4}+\cdots+a_{2022}\right) \\
& \leq \frac{1}{4}\left(a_{1}+a_{2}+\cdots+a_{2023}\right)^{2} \\
& =\frac{1}{4} .
\end{aligned}
$$

在 $a_{1}=a_{2}=\frac{1}{2}, a_{3}=\cdots=a_{2023}=0$ 时可取等.

综上, $\sum_{i=1}^{2023} \min \left\{a_{i}, a_{i+1}\right\}^{2}$ 的最大值为 $\frac{1}{4}$.

评注 此题是中等偏易的代数题, 考试中约 $42 \%$ 做对此题. 容易猜到最大值为 $\frac{1}{4}$. 进而在证明中想到如下著名不等式:

$$
\sum_{i=1}^{n} a_{i} \cdot a_{i+1} \leq \frac{1}{4}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}, \quad \forall n \geq 4
$$

题 5 点 $H$ 是 $\triangle A B C$ 的垂心, 点 $E, F$ 分别是边 $A C, A B$ 上高的垂足. 点 $M$为线段 $B C$ 的中点. 延长 $A H, B H, C H$ 再次交外接圆于点 $K, Q, P . K F, K E$再次交外接圆于点 $S, T$. 证明: 若 $S, H, M$ 三点共线, 则 $S Q, P T, A C$ 三线共点.

证明 作 $A$ 在 $\odot O$ 上的对径点 $A^{\prime}$, 有 $H M A^{\prime}$ 共线, 故 $\angle A S H=90^{\circ}$. 因此



$H, A, E, F, S$ 共圆. 注意到

$$
\angle B A K=90^{\circ}-B=\angle A^{\prime} B C=\angle A^{\prime} A C
$$

而

$$
\angle B A K=\angle F S H=\angle K A A^{\prime}
$$

故 $\frac{1}{3} A+B=90^{\circ}$. 即 $A+3 B=270^{\circ}$ 或者说 $2 B=C+90^{\circ}$.

要证明 $S Q, P T, A C$ 三线共点等价于证明

$$
\frac{A T}{T Q} \cdot \frac{Q C}{C P} \cdot \frac{P S}{S A}=1
$$

由 $A B, S K, P C$ 三线共点, 有

$$
\frac{A S}{S P} \cdot \frac{P B}{B K} \cdot \frac{K C}{A C}=1
$$

由 $\angle B A K=\angle B C P$, 有 $P B=B K$, 故

$$
\frac{A S}{S P}=\frac{A C}{C K}
$$

同理由 $A C, T K, Q B$ 三线共点, 有

$$
\frac{A B}{B K} \cdot \frac{C K}{C Q} \cdot \frac{Q T}{T A}=1
$$

由 $C K=C Q$, 知

$$
\frac{Q T}{T A}=\frac{B K}{A B}
$$

因此

考虑到

$$
\begin{aligned}
\frac{A T}{T Q} \cdot \frac{Q C}{C P} \cdot \frac{P S}{S A}=1 & \Leftrightarrow \frac{A B}{B K} \cdot \frac{Q C}{C P} \cdot \frac{C K}{A C}=1 \\
& \Leftrightarrow \frac{C P}{Q C}=\frac{A B}{A C} \cdot \frac{C K}{B K} .
\end{aligned}
$$

$$
\frac{A B}{A C} \cdot \frac{C K}{B K}=\frac{A B}{A C} \cdot \frac{C H}{B H}=\frac{\sin C}{\sin B} \cdot \frac{\cos C}{\cos B}=\frac{\sin 2 C}{\sin 2 B}
$$

且

$$
\frac{C P}{Q C}=\frac{\sin \angle P B C}{\cos C}=\frac{\sin \left(90^{\circ}-A+B\right)}{\cos C}=\frac{\sin \left(4 B-180^{\circ}\right)}{\cos \left(2 B-90^{\circ}\right)}=\frac{\sin 2 C}{\sin 2 B}
$$

故命题成立.

评注 此题是较难的几何题, 考试中约 $20 \%$ 做对此题. 首先对于 $S$ 可以刻画为 $A H$ 直径的圆和外接圆的交点, 结合一些简单性质可以导出 $A+3 B=270^{\circ}$以及 $A S, E F, B C$ 共点. 利用前者很好完成一个计算证明, 利用后者继续发现 $S Q, E F, A T ; A S, P T, E F$ 共点(Pascal) 并利用调和可以得到结论.

题 6 给定正整数 $n \geq 2 k$ 和正整数 $e_{1}, e_{2}, \cdots, e_{k}$, 其中

$$
e_{1}+\cdots+e_{k}=\left(\begin{array}{c}
n \\
2
\end{array}\right)
$$

证明: 可以用 $k$ 种颜色 $1,2, \cdots, k$ 将完全图 $K_{n}$ 染色, 满足:

(1) 颜色 $i$ 的边恰有 $e_{i}$ 条;

(2) 对任意 $K_{n}$ 中四个点, 连接他们的边中至多使用了五种颜色.

证明 1 不妨设该完全图的顶点为 $v_{1}, \cdots, v_{n}$. 记满足条件 (2) 的染色为好的. 我们对 $k$ 归纳. $k \leq 6$ 时问题显然成立. 设问题对于小于 $k$ 的情况均成立, 来看 $k$ 的情况. 不妨设 $e_{1} \geq \cdots \geq e_{k}>0$. 则 $e_{k} \leq \frac{1}{k}\left(\begin{array}{c}n \\ 2\end{array}\right)$, 且由 $n \geq 2 k$ 知 $e_{1} \geq \frac{1}{k}\left(\begin{array}{l}n \\ 2\end{array}\right) \geq n-1$. 设 $t$ 为最小的满足条件 $\left(\begin{array}{l}t \\ 2\end{array}\right)+t(n-t) \geq e_{k}$ 的正整数. 由最小性,

$$
\left(\begin{array}{c}
t-1 \\
2
\end{array}\right)+(t-1)(n-t+1)<e_{k}
$$

故

$$
\left(\begin{array}{l}
t \\
2
\end{array}\right)+t(n-t)-e_{k}<n-t \leq e_{1}
$$

考虑 $\left(\begin{array}{l}t \\ 2\end{array}\right)+t(n-t)$ 条包含 $v_{n-t+1}, \cdots, v_{n}$ 之一作为顶点的边构成的集合 $S$.由上述不等式知, 我们可以用颜色 $k$ 将 $S$ 中 $e_{k}$ 条染色, 并将剩余的边染为颜色 1. 此外, 注意到

$$
\left(\begin{array}{c}
\frac{n}{k} \\
2
\end{array}\right)+\frac{n}{k}\left(n-\frac{n}{k}\right)=\frac{n}{2 k}\left(2 n-\frac{n}{k}-1\right) \geq \frac{n}{2 k}(n-1)=\frac{1}{k}\left(\begin{array}{l}
n \\
2
\end{array}\right) \geq e_{k},
$$

故由 $t$ 的最小性知 $t \leq \frac{n}{k}$. 因此

$$
n-t \geq n\left(1-\frac{1}{k}\right) \geq 2(k-1)
$$

记 $e_{1}^{\prime}=e_{1}-\left(\begin{array}{l}t \\ 2\end{array}\right)-t(n-t)+e_{k}, e_{i}^{\prime}=e_{i}(2 \leq i \leq k-1)$, 则

$$
e_{1}^{\prime}+e_{2}^{\prime}+\cdots+e_{k-1}^{\prime}=\left(\begin{array}{c}
n-t \\
2
\end{array}\right) \text {. }
$$

因此, 我们可以对序列 $\left(e_{1}^{\prime}, e_{2}^{\prime}, \cdots, e_{k-1}^{\prime}\right)$ 用归纳假设, 将剩余的边进行好染色,使得颜色 $i$ 被用了 $e_{i}^{\prime}$ 次. 结合前述染色, 我们就得到一个对完全图 $K_{n}$ 的满足条件(1) 的染色.

最后我们只需验证该染色为好染色. 对于任意四个 $K_{n}$ 中的点, 如果它们均属于 $v_{1}, \cdots, v_{n-t}$, 则由归纳假设知连接这四个点的边最多用了五种颜色; 如果它们中包含 $v_{n-t+1}, \cdots, v_{n}$ 之一, 注意到从这些点连出的边均至多只有 $1, k$ 两种颜色, 故连接它们的边亦至多五种颜色. 证毕.

证明 2 将图中点用 $1-n$ 任意标号. 对 $n$ 使用归纳法. 当 $n=2$ 时结论显然.

假设 $n-1$ 时结论成立. 考虑 $n$ 的情形:不妨假设 $e_{1} \geq e_{2} \geq \cdots \geq e_{k}$. 有

$$
e_{1} \geq \frac{\left(\begin{array}{l}
n \\
2
\end{array}\right)}{k} \geq \frac{\left(\begin{array}{l}
n \\
2
\end{array}\right)}{\frac{n}{2}}=n-1
$$

(1) 若 $k \leq \frac{n-1}{2}$. 由 $e_{1} \geq n-1$ 知可将边 $1 n, 2 n, \cdots,(n-1) n$ 均染为 1 色.此时对点 $1,2, \cdots, n-1$ 和 $e_{1}^{\prime}=e_{1}-n-1, e_{i}^{\prime}=e_{i}(i=2,3, \cdots, n-1)$ 使用归纳假设进行染色. 下面验证这样的染色是满足题意的. 任取 $1,2, \cdots, n$ 中的四个点. 若包含点 $n$, 则与 $n$ 相连的边均为 1 色, 其余三点之间的边至多三种颜色, 满足题意;若不包含点 $n$, 由归纳假设知也满足题意.

(2) 若 $k=\frac{n}{2}$. 此时

$$
e_{k} \leq \frac{\left(\begin{array}{c}
n \\
2
\end{array}\right)}{\frac{n}{2}}=n-1
$$

将边 $1 n, 2 n, \cdots, e_{k} n$ 染为 $k$ 色, 边 $\left(e_{k}+1\right) n, \cdots,(n-1) n$ 染为 1 色. 对点 $1,2, \cdots, n-1$ 和 $e_{1}^{\prime}=e_{1}-\left(n-1-e_{k}\right), e_{i}^{\prime}=e_{i}(i=2,3, \cdots, n-1)$ 使用归纳假设进行染色. 下面验证这样的染色是满足题意的. 任取 $1,2, \cdots, n$ 中的四个点. 若包含点 $n$, 则与 $n$ 相连的边均为 1 或 $k$ 色, 其余三点之间的边至多三种颜色, 满足题意; 若不包含点 $n$, 由归纳假设知也满足题意.

综上, 命题成立.

评注 此题是困难的组合题, 考试中约 $7 \%$ 做对此题. 证明 1 是对 $k$ 进行归纳, 归纳的想法是对尽可能少的点 $v_{n-t+1}, \cdots, v_{n}$ 将与之相连的边染成 $k$ 色, 然后利用归纳假设得到结论. 证明 2 对 $n$ 进行归纳, 若 $k \leq \frac{n-1}{2}$, 将与某个点相连的所有边染成一种颜色即可使用归纳假设; 若 $k=\frac{n}{2}$, 则必须用掉一种颜色 $(k$色)后再使用归纳假设.

此外, 题中条件 $n \geq 2 k$ 可进一步放宽为 $n \geq k$. 此时, $e_{1}<n-1$ 的情况用 $e_{1}+e_{2} \geq n-1$ 即可解决.

