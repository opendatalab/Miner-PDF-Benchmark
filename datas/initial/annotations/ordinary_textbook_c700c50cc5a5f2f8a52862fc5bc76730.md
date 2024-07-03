# 2021 年波兰数学奥林匹克试题解析 

曾午午 曾彦翔唐自远

(长沙市雅礼中学, 410007)

指导教师: 彭熹

2021 年波兰数学奥林匹克试题难度适中, 题目简洁, 方法灵活, 是一套很不错的奥林匹克试题. 以下是本次比赛的试题解答与评注, 其中未特别标注的解法由三位作者共同完成.

## I. 试 题

1. 对于给定的自然数 $k$, 用 $p_{i}(i=1,2, \cdots, k)$ 表示从小到大的第 $i$ 个素数,记 $N=p_{1} p_{2} \cdots p_{k}$. 证明: 在集合 $\{1,2, \cdots, N\}$ 中恰有 $\frac{N}{2}$ 个数被奇数个 $p_{i}$ 整除.
2. 设 $n$ 为正整数. 对于整数 $0 \leq i \leq j \leq n$, 实数 $f(i, j)$ 满足如下条件:

(1) 对任意整数 $0 \leq i \leq n$, 均有 $f(i, i)=0$;

(2) 对任意满足 $0 \leq i \leq j \leq k \leq l \leq n$ 的整数 $i, j, k, l$, 均有

$$
0 \leq f(i, l) \leq 2 \max \{f(i, j), f(j, k), f(k, l)\}
$$

证明:

$$
f(0, n) \leq 2 \sum_{k=1}^{n} f(k-1, k)
$$

3. $\triangle A B C$ 内接于圆 $\omega$, 点 $P$ 为 $\omega$ 上除 $A, B, C$ 外任意一点, 直线 $A P, B C$交于 $D$, 直线 $B P, C A$ 交于 $E$, 直线 $C P, A B$ 交于 $F$. 设过 $A P, B C$ 中点的直线为 $\ell_{1}$, 过 $B P, C A$ 中点的直线为 $\ell_{2}$, 过 $C P, A B$ 中点的直线为 $\ell_{3}$, 点 $X, Y, Z$ 分别为 $D, E, F$ 到 $\ell_{1}, \ell_{2}, \ell_{3}$ 的垂足. 设 $Q$ 为 $\triangle X Y Z$ 的外心. 证明: 当点 $P$ 移动时, $Q$ 在一定圆上.
4. 证明: 对任意的正实数 $a, b$ 以及正整数 $n$, 都有

$$
(a+b)^{n}-a^{n}-b^{n} \geq \frac{2^{n}-2}{2^{n-2}} a b(a+b)^{n-2}
$$[^0]

![](https://cdn.mathpix.com/cropped/2024_02_26_56964553ed888c176876g-2.jpg?height=720&width=848&top_left_y=297&top_left_x=615)

第 3 题图

5. 凸六边形 $A B C D E F$ 中, $\angle F A B+\angle B C D+\angle D E F=360^{\circ}$ 且 $\angle A E B=$ $\angle A D B$. 设直线 $A B, D E$ 交于点 $P$, 证明: $\triangle A F E, \triangle B C D$ 的外心与 $P$ 共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_56964553ed888c176876g-2.jpg?height=851&width=512&top_left_y=1299&top_left_x=772)

第 5 题图

6. 给定圆 $\omega$ 及正整数 $d$. Hansel 在圆上作若干条弦, 满足如下条件: 每条弦的端点至少为 $d$ 条不同弦的端点. 证明: 存在一条弦, 至少与 $\frac{d^{2}}{4}$ 条弦在圆内或圆上相交.

注: 证明本题的简化版, 即存在一条弦至少与 $\frac{d^{2}}{8}$ 条弦在圆内或圆上相交, 可得 2 分.

## II. 解答与评注

1. 对于给定的自然数 $k$, 用 $p_{i}(i=1,2, \cdots, k)$ 表示从小到大的第 $i$ 个素数,记 $N=p_{1} p_{2} \cdots p_{k}$. 证明: 在集合 $\{1,2, \cdots, N\}$ 中恰有 $\frac{N}{2}$ 个数被奇数个 $p_{i}$ 整除.

证明 1 (曾午午) 对于 $n \in \mathbb{N}^{*}$, 记 $Q_{n}=\left\{i: p_{i} \mid n, i \in\{1,2, \cdots, k\}\right\}$, 则 $\left|Q_{n}\right|$ 即整除 $n$ 的 $p_{i}$ 的个数.

对于整数 $1 \leq n \leq \frac{N}{2}$, 注意到 $\frac{N}{2}$ 为奇数, 故 1 恰属于 $Q_{n}, Q_{\frac{n+N}{2}}$ 中的一者;而对于整数 $2 \leq i \leq k, p_{i}$ 整除 $\frac{N}{2}$, 故 $i$ 同时属于或同时不属于 $Q_{n}, Q_{\frac{n+N}{2}}$.

这表明 $\left|Q_{n}\right|,\left|Q_{n+N / 2}\right|$ 一奇一偶, 即恰有 $\frac{N}{2}$ 个 $n$ 被奇数个 $p_{i}$ 整除.

本题也可以直接对满足条件的数的个数进行计算.

证明 2 (曾彦翔) 用 $A$ 表示集合 $\{1,2, \cdots, N\}$ 中被奇数个 $p_{i}$ 整除的数的个数, 记 $K=\{1,2, \cdots, k\}$, 则

$$
A=\sum_{\substack{I \subset K \\|I| \text { odd }}} \varphi\left(\frac{N}{\prod_{x \in I} p_{x}}\right)
$$

注意到对任意正整数 $n$ 恒有 $\sum_{d \mid n, d>0} \varphi(d)=n$, 故为证明 $A=\frac{N}{2}$, 只需证明 $B=\frac{N}{2}$, 这里

$$
\begin{aligned}
B & =\sum_{\substack{I \subset K \\
|I| \text { odd }}} \varphi\left(\prod_{x \in I} p_{x}\right)=\sum_{I \subset K} \prod_{x \in I}\left(p_{x}-1\right) \\
& =\frac{1}{2}\left(\prod_{x=1}^{k}\left(1+\left(p_{x}-1\right)\right)-\prod_{x=1}^{k}\left(1-\left(p_{x}-1\right)\right)\right) \\
& =\frac{1}{2}(N-0)=\frac{N}{2} .
\end{aligned}
$$

评注 本题较易, 用配对和直接统计都不难证明. 遇到“恰一半”的题目, 配对是常用的方法, 从小情况也能观察出规律. 若没有想到恰当的配对方法, 我们也可以用欧拉函数的有关性质对 $A$ 进行统计.

2. 设 $n$ 为正整数. 对于整数 $0 \leq i \leq j \leq n$, 实数 $f(i, j)$ 满足如下条件:

(1) 对任意整数 $0 \leq i \leq n$, 均有 $f(i, i)=0$;

(2) 对任意满足 $0 \leq i \leq j \leq k \leq l \leq n$ 的整数 $i, j, k, l$, 均有

$$
0 \leq f(i, l) \leq 2 \max \{f(i, j), f(j, k), f(k, l)\}
$$

证明:

$$
f(0, n) \leq 2 \sum_{k=1}^{n} f(k-1, k)
$$

证明 1 (唐自远) 我们证明加强命题 $\mathcal{P}(m)$ : 在原条件下, 对任意自然数 $x$,都有

$$
f(x, x+m) \leq 2 \sum_{k=1}^{m} f(x+k-1, x+k) \text {. }
$$

对 $m$ 使用第二数学归纳法, 在 $m \leq 3$ 时 $\mathcal{P}(m)$ 显然成立. 以下假设 $\mathcal{P}(1), \mathcal{P}(2), \cdots, \mathcal{P}(m-1)$ 均成立, 我们证明 $\mathcal{P}(m)$ 也是成立的.

反证法，假设存在一个自然数 $x_{0}$ 使得

$$
f\left(x_{0}, x_{0}+m\right)>2 \sum_{k=1}^{m} f\left(x_{0}+k-1, x_{0}+k\right)
$$

则 $f\left(x_{0}, x_{0}+m\right)$ 比每个 $2 f\left(x_{0}+k-1, x_{0}+k\right)(k=1,2, \cdots, m)$ 都要大. 结合条件知, 对 $k=2, \cdots, m-3$, 以下不等关系成立:

$$
\begin{aligned}
f\left(x_{0}, x_{0}+m\right) & \leq 2 \max \left\{f\left(x_{0}, x_{0}+1\right), f\left(x_{0}+2, x_{0}+m\right)\right\} \\
& =2 f\left(x_{0}+2, x_{0}+m\right) ; \\
f\left(x_{0}, x_{0}+m\right) & \leq 2 \max \left\{f\left(x_{0}, x_{0}+k\right), f\left(x_{0}+k+1, x_{0}+m\right)\right\} ; \\
f\left(x_{0}, x_{0}+m\right) & \leq 2 \max \left\{f\left(x_{0}, x_{0}+m-2\right), f\left(x_{0}+m-1, x_{0}+m\right)\right\} \\
& =2 f\left(x_{0}, x_{0}+m-2\right) .
\end{aligned}
$$

由介值原理, 存在一个整数 $1 \leq k \leq m-3$, 使得以下两式同时成立:

$$
\begin{aligned}
f\left(x_{0}, x_{0}+m\right) & \leq 2 \max \left\{f\left(x_{0}, x_{0}+k\right), f\left(x_{0}+k+1, x_{0}+m\right)\right\} \\
& =2 f\left(x_{0}+k+1, x_{0}+m\right) ; \\
f\left(x_{0}, x_{0}+m\right) & \leq 2 \max \left\{f\left(x_{0}, x_{0}+k+1\right), f\left(x_{0}+k+2, x_{0}+m\right)\right\} \\
& =2 f\left(x_{0}, x_{0}+k+1\right) .
\end{aligned}
$$

以上两式相加, 并结合 $k+1, m-k-1$ 时的归纳假设就有

$$
\begin{aligned}
f\left(x_{0}, x_{0}+m\right) & \leq f\left(x_{0}, x_{0}+k+1\right)+f\left(x_{0}+k+1, x_{0}+m\right) \\
& \leq 2 \sum_{k=1}^{m} f\left(x_{0}+k-1, x_{0}+k\right)
\end{aligned}
$$

与反证假设矛盾! 故命题 $\mathcal{P}(m)$ 成立, 进而知原命题 $(\mathcal{P}(n), x=0)$ 成立.

本题还有另一种完成第二归纳的方法, 方法如下:
证明 2 (曾彦翔) 仍归纳证明按证明 1 定义的加强命题 $\mathcal{P}(m)$, 并不妨设 $\mathcal{P}(i)(i=1,2, \cdots, m-1)$ 均成立.

记 $S=\sum_{k=1}^{m} f\left(x_{0}+k-1, x_{0}+k\right)$, 我们只需证明 $f\left(x_{0}, x_{0}+m\right) \leq 2 S$.

取最大的 $p$ 使

$$
A=\sum_{k=1}^{p} f\left(x_{0}+k-1, x_{0}+k\right) \leq \frac{S}{2}
$$

取最小的 $q$ 使

$$
B=\sum_{k=q+1}^{m} f\left(x_{0}+k-1, x_{0}+k\right) \leq \frac{S}{2} \text {. }
$$

情形 $1: q-p \geq 2$. 记

$$
a=f\left(x_{0}+p, x_{0}+p+1\right), b=f\left(x_{0}+q-1, x_{0}+q\right) .
$$

由条件可得 $A+a+b+B \leq S$. 但由 $p$ 的最大性和 $q$ 的最小性知 $A+a>\frac{S}{2}$, $b+B>\frac{S}{2}$, 矛盾.

情形 $2: q-p \leq 1$. 则

$$
\begin{aligned}
f\left(x_{0}, x_{0}+m\right) & \leq 2 \max \left\{f\left(x_{0}, x_{0}+p\right), f\left(x_{0}+p, x_{0}+q\right), f\left(x_{0}+q, x_{0}+m\right)\right\} \\
& \leq 2 \max \left\{2 A, f\left(x_{0}+p, x_{0}+q\right), 2 B\right\} \leq 2 S
\end{aligned}
$$

故命题 $\mathcal{P}(m)$ 成立, 归纳完毕.

评注 本题的两种证法都使用了加强命题的归纳. 方法一最后一步类似于介值原理的处理手法, 找到一个合适的 $k$ 并分两段使用归纳假设; 方法二使用贪心算法的思想直接构造分段点 $p$.
3. $\triangle A B C$ 内接于圆 $\omega$, 点 $P$ 为 $\omega$ 上除 $A, B, C$ 外任意一点, 直线 $A P, B C$交于 $D$, 直线 $B P, C A$ 交于 $E$, 直线 $C P, A B$ 交于 $F$. 设过 $A P, B C$ 中点的直线为 $\ell_{1}$, 过 $B P, C A$ 中点的直线为 $\ell_{2}$, 过 $C P, A B$ 中点的直线为 $\ell_{3}$, 点 $X, Y, Z$ 分别为 $D, E, F$ 到 $\ell_{1}, \ell_{2}, \ell_{3}$ 的垂足. 设 $Q$ 为 $\triangle X Y Z$ 的外心. 证明: 当点 $P$ 移动时, $Q$ 在一定圆上.

证明 设 $B C, C A, A B, P A, P B, P C$ 的中点分别为 $M, N, L, U, V, W$.由中位线的性质知 $U L \stackrel{\|}{=} \frac{1}{2} P B \stackrel{\|}{=} M W$, 故 $U L M W$ 构成平行四边形, 对角线 $M U, L W$ 中点重合, 记为 $T$. 同理, $N V$ 中点也为 $T$.

设 $O, H$ 分别为 $\triangle A B C$ 的外心和垂心, $S$ 为 $P H$ 中点. 则由垂外心的性质知 $S U \stackrel{\|}{=} \frac{1}{2} A H \stackrel{\|}{=} O M$, 故 $S U O M$ 为平行四边形. 再由 $O M \perp B C, O U \perp A P$知 $S U \perp B C, S M \perp A P$, 即 $D$ 为 $\triangle S U M$ 垂心.

![](https://cdn.mathpix.com/cropped/2024_02_26_56964553ed888c176876g-6.jpg?height=725&width=854&top_left_y=206&top_left_x=595)

图 3-1

故 $D X$ 过 $S$, 同理知 $E Y, F Z$ 均过 $S$. 此时 $\angle S X T=\angle S Y T=\angle S Z T=90^{\circ}$,故 $S, T, X, Y, Z$ 五点共圆, 且该圆以 $S T$ 为直径, 即 $Q$ 为 $S T$ 中点.

![](https://cdn.mathpix.com/cropped/2024_02_26_56964553ed888c176876g-6.jpg?height=497&width=520&top_left_y=1202&top_left_x=768)

图 3-2

不妨设 $O$ 为复平面原点, 并用某点的粗体表示该点在复平面上所对应的复数. 则有

$$
\begin{aligned}
\mathbf{H} & =\mathbf{A}+\mathbf{B}+\mathbf{C}, \quad \mathbf{S}=\frac{\mathbf{P}+\mathbf{A}+\mathbf{B}+\mathbf{C}}{2}, \\
\mathbf{T} & =\frac{\mathbf{P}+\mathbf{A}+\mathbf{B}+\mathbf{C}}{4}, \quad \mathbf{Q}=\frac{3}{8}(\mathbf{P}+\mathbf{A}+\mathbf{B}+\mathbf{C}),
\end{aligned}
$$

故 $Q$ 在以 $O H$ 连线的第三个八等分点为圆心, 半径为 $\frac{3 r}{8}$ 的圆上, 这里 $r$ 为 $\triangle A B C$ 外接圆半径.

评注 作图后容易观察到两组三线共点, 难点在于猜出第二组三线共点所共的点即为 $P H$ 中点, 随后的证明都是自然的. 本题在证明 $D X, E Y, F Z$ 三线共点时, 也可以利用圆幂差的线性性质并结合余弦定理进行计算. 最后一步证明 $Q$ 在定圆上也可以取出圆心并用几何方法证明. 本题是若干结论的叠加, 有一定
难度.

4. 证明: 对任意的正实数 $a, b$ 以及正整数 $n$, 都有

$$
(a+b)^{n}-a^{n}-b^{n} \geq \frac{2^{n}-2}{2^{n-2}} a b(a+b)^{n-2} .
$$

证明 1 (唐自远) 不等式两边关于 $a, b$ 齐次, 故不妨设 $a+b=2$. 记 $a=1+x, b=1-x$, 则 $x \in(-1,1)$. 只需证明

$$
(1+x)^{n}+(1-x)^{n}+\left(2^{n}-2\right)\left(1-x^{2}\right) \leq 2^{n} \text {. }
$$

将上式左边用二项式定理展开, 其中 $x$ 的奇次幂全部抵消, 结合 $x$ 的定义域知 $x^{2 k} \leq x^{2}\left(k \in \mathbb{N}^{*}\right)$, 故

$$
\begin{aligned}
\text { (A) LHS } & =2+\sum_{k=1}^{\lfloor n / 2\rfloor}\left(\begin{array}{c}
n \\
2 k
\end{array}\right) x^{2 k}+\left(2^{n}-2\right)-\left(2^{n}-2\right) x^{2} \\
& \leq 2+\sum_{k=1}^{\lfloor n / 2\rfloor}\left(\begin{array}{c}
n \\
2 k
\end{array}\right) x^{2}+\left(2^{n}-2\right)-\left(2^{n}-2\right) x^{2} \\
& =2^{n} .
\end{aligned}
$$

证明 2 (曾午午) 仍不妨设 $a+b=2$, 并设 $0 \leq a \leq 1$. 在 $n=1,2,3$ 时不难验证不等式成立, 下设 $n \geq 4$.

考察函数 $f(x)=x^{n}+(2-x)^{n}+\left(2^{n}-2\right) x(2-x)(0 \leq x \leq 1)$, 有

$$
\begin{aligned}
f^{\prime}(x) & =n x^{n-1}-n(2-x)^{n-1}+\left(2^{n}-2\right)(2-2 x), \\
f^{\prime \prime}(x) & =n(n-1) x^{n-2}+n(n-1)(2-x)^{n-2}-2\left(2^{n}-2\right), \\
f^{\prime \prime \prime}(x) & =n(n-1)(n-2)\left(x^{n-3}-(2-x)^{n-3}\right) \leq 0,
\end{aligned}
$$

所以

$$
\begin{aligned}
& f^{\prime}(0)=2^{n+1}-4-n \cdot 2^{n-1}<0, f^{\prime}(1)=0, \\
& f^{\prime \prime}(0)=n(n-1) \cdot 2^{n-2}-2^{n+1}+4>0, \\
& f^{\prime \prime}(1)=2 n(n-1)-2^{n+1}+4<0 .
\end{aligned}
$$

于是 $f^{\prime \prime}(x)$ 在 $(0,1)$ 上有唯一零点 $t$, 则 $f^{\prime}(x)$ 在 $[0, t)$ 上单调递增, 在 $(t, 1]$上单调递减.

于是 $f^{\prime}(x)$ 在 $(0,1)$ 上有唯一零点 $s$, 则 $f(x)$ 在 $[0, s)$ 上单调递减, 在 $(s, 1]$上单调递增.

而 $f(0)=f(1)=2^{n}$, 故 $f(x) \leq 2^{n}$ 在定义域上恒成立. 即证.
评注 本题较易. 证法二较为直接, 用齐次化转化为单变量问题, 随后求导证明. 证法一中运用了对称化处理的技巧, 绕开了求导, 更简便地完成了证明. 两种思路本质上都是将双变量转化为单变量, 这往往也是解决此类问题的一个突破 ロ。

5. 凸六边形 $A B C D E F$ 中, $\angle F A B+\angle B C D+\angle D E F=360^{\circ}$ 且 $\angle A E B=$ $\angle A D B$. 设直线 $A B, D E$ 交于点 $P$, 证明: $\triangle A F E, \triangle B C D$ 的外心与 $P$ 共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_56964553ed888c176876g-8.jpg?height=443&width=751&top_left_y=732&top_left_x=661)

证明 1 (曾午午) 设 $\triangle A F E, \triangle B C D$ 外心分别为 $O_{1}, O_{2}$, 设 $P A$ 交 $\odot O_{1}$ 于另一点 $G, P E$ 交 $\odot O_{2}$ 于另一点 $H$. 由 $\angle A E B=\angle A D B$ 知 $A, E, D, B$ 四点共圆. 故 $\angle P H G=\angle E A G=\angle B D P, G H / / B D$. 又 $\angle F A B+\angle B C D+\angle D E F=$ $360^{\circ}$, 故

$$
\begin{aligned}
\angle B O_{2} D=2 \angle B C D & =2\left(\left(180^{\circ}-\angle D E F\right)+\left(180^{\circ}-\angle F A B\right)\right) \\
& =2(\angle F E P+\angle F A P) \\
& =\angle F O_{1} H+\angle G O_{1} F \\
& =\angle G O_{1} H .
\end{aligned}
$$

于是 $\triangle O_{1} G H \sim \triangle O_{2} B D$.

再由 $G H / / B D$ 知这组相似是位似. 故 $P, O_{1}, O_{2}$ 共线.

证明 2 (曾彦翔, 唐自远) 同上知 $A, B, D, E$ 共圆, 记 $P A \cdot P B=P D \cdot P E=$ $r^{2}$. 在射线 $P F$ 上取一点 $X$ 使得 $P F \cdot P X=r^{2}$. 则 $A, B, F, X$ 共圆, $D, E, F, X$共圆, 故

$$
\angle B X D=\angle P A F+\angle P E F=360^{\circ}-\angle F A B-\angle F E D=\angle B C D,
$$

故 $X$ 在 $\odot O_{2}$ 上. 考察以 $P$ 为中心, $r^{2}$ 为反演幂的反演变换 $\varphi$, 则

$$
\varphi: A \rightleftharpoons B, E \rightleftharpoons D, F \rightleftharpoons X, \odot(A E F) \rightleftharpoons \odot(B D X)
$$

故 $O_{1} O_{2}$ 的连线过反演中心 $P$, 命题得证.
评注 本题较易. 其中证明一更为简便, 利用一步位似直接完成证明; 事实上从结论看, $P$ 也只能为两圆的位似中心. 证明二利用两圆关于位似中心互反的性质, 选取适当的反演幂亦可. 题面中和为 $360^{\circ}$ 的条件略显奇怪,一开始应当忽略.

6. 给定圆 $\omega$ 及正整数 $d$. Hansel 在圆上作若干条弦, 满足如下条件: 每条弦的端点至少为 $d$ 条不同弦的端点. 证明: 存在一条弦, 至少与 $\frac{d^{2}}{4}$ 条弦在圆内或圆上相交.

注: 证明本题的简化版, 即存在一条弦至少与 $\frac{d^{2}}{8}$ 条弦在圆内或圆上相交, 可得 2 分.

证明 (曾午午) 设所有端点顺时针依次为 $A_{1}, A_{2}, \cdots, A_{n}$, 以下端点的下标按模 $n$ 理解.

当 $i-j=t \in\left\{1,2, \cdots,\left[\frac{n}{2}\right]\right\}$ 时, 称弦 $A_{i} A_{j}$ 的长度为 $t$. 取长度不小于 $\frac{d}{2}$ 的长度最小的弦, 容易证明这样的弦存在, 不妨设为 $A_{n} A_{T+1}$, 这里 $\frac{d}{2} \leq T+1<\frac{n}{2}$.结合最小性, 知两端点都在 $A_{1}, A_{2}, \cdots, A_{T}$ 的弦至多有

$$
\frac{T(T-1)}{2}-\frac{\left(T-\left\lceil\frac{d}{2}\right\rceil\right)\left(T-\left\lceil\frac{d}{2}\right\rceil+1\right)}{2}
$$

条. 而这 $T$ 个点各发出至少 $d$ 条弦, 它们发出的其余的弦都将与 $A_{n} A_{T+1}$ 相交,共有不少于

$$
\begin{aligned}
T d & -2\left(\frac{T(T-1)}{2}-\frac{\left(T-\left\lceil\frac{d}{2}\right\rceil\right)\left(T-\left\lceil\frac{d}{2}\right\rceil+1\right)}{2}\right) \\
& =\left(d-2\left\lceil\frac{d}{2}\right]+2\right) T+\left\lceil\frac{d}{2}\right\rceil\left(\left\lceil\frac{d}{2}\right\rceil-1\right) \geq \frac{d^{2}}{4}
\end{aligned}
$$

条, 即至少 $\frac{d^{2}}{4}$ 条弦与 $A_{n} A_{T+1}$ 相交, 命题得证.

评注 本题初看难以下手, 没有与之相关的定理, 从整体考虑也会毫无头绪.这时可以固定一条弦进行考虑, 让尽量多的弦与之相交, 这需要两端点都在一侧的弦上, 便有了这个利用极端原理的做法. 对于这种题面简洁而难以入手的题目, 要谨防用力过猛, 不妨尝试从一些轻巧的手段出发, 或许会有意想不到的效果.


[^0]:    修订日期: 2021-10-10.

