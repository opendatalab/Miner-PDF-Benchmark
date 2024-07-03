数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2016 年中国西部数学邀请赛 

王广廷

(上海市上海中学, 200231)

四川绵阳

$$
\text { 第一天 }
$$

8 月 15 日 8:00-12:00

1. 设实数 $a, b, c, d$ 满足 $a b c d>0$. 证明: 存在 $a, b, c, d$ 的一个排列 $x, y, z, w$,使得

$$
2(x z+y w)^{2}>\left(x^{2}+y^{2}\right)\left(z^{2}+w^{2}\right)
$$

(刘诗雄 供题)

证法一 假设对 $a, b, c, d$ 的任意一个排列 $(x, y, z, w)$, 都有

$$
2(x z+y w)^{2} \leq\left(x^{2}+y^{2}\right)\left(z^{2}+w^{2}\right) .
$$

则对排列 $(a, b, c, d)$ 有

$$
2(a b+c d)^{2} \leq\left(a^{2}+c^{2}\right)\left(b^{2}+d^{2}\right)
$$

对排列 $(a, d, c, b)$ 有

$$
2(a c+d b)^{2} \leq\left(a^{2}+d^{2}\right)\left(c^{2}+b^{2}\right)
$$

对排列 $(a, b, d, c)$ 有

$$
2(a d+b c)^{2} \leq\left(a^{2}+b^{2}\right)\left(d^{2}+c^{2}\right)
$$

将以上三式相加得,

$$
\begin{array}{r}
2\left(a^{2} b^{2}+c^{2} d^{2}+a^{2} c^{2}+b^{2} d^{2}+a^{2} d^{2}+b^{2} c^{2}\right)+12 a b c d \\
\quad \leq 2\left(a^{2} b^{2}+c^{2} d^{2}+a^{2} c^{2}+b^{2} d^{2}+a^{2} d^{2}+b^{2} c^{2}\right)
\end{array}
$$

收稿日期: 2016-08-29.
即 $a b c d \leq 0$. 这与 $a b c d>0$ 矛盾, 证毕!

证法二 取 $x, z$ 是 $a, b, c, d$ 中最大的两个, $y, w$ 是 $a, b, c, d$ 中最小的两个. 下证这样的排列满足要求.

事实上, 因为

$$
\left(x^{2}+y^{2}\right)\left(z^{2}+w^{2}\right)-(x z+y w)^{2}=(x w-y z)^{2},
$$

所以只需证明

$$
(x z+y w)^{2}>(x w-y z)^{2},
$$

即

$$
|x z+y w|>|x w-y z| .
$$

因为 $x y z w>0$, 所以 $x, z$ 的符号相同, $y, w$ 的符号相同. 注意到当同时改变 $x, z$ 或 $y, w$ 的符号时, 式 (*) 不变, 因此可不妨设 $x, y, z, w$ 都大于 0 . 此时

$$
|x z+y w|=x z+y w>x z>\max \{x w, y z\}>|x w-y z| .
$$

(*) 式成立, 故结论得证.

2. 如图, 设 $\odot O_{1}$ 与 $\odot O_{2}$ 相交于点 $P, Q$, 它们的一条外公切线分别与 $\odot O_{1}, \odot O_{2}$ 相切于点 $A, B$. 过点 $A, B$ 的圆 $\Gamma$ 分别与 $\odot O_{1}, \odot O_{2}$ 交于点 $D, C$. 证明: $\frac{C P}{C Q}=\frac{D P}{D Q}$.

(张端阳 供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_136b2b83847a9e4a1310g-2.jpg?height=454&width=645&top_left_y=1943&top_left_x=360)

第 2 题图

![](https://cdn.mathpix.com/cropped/2024_02_26_136b2b83847a9e4a1310g-2.jpg?height=597&width=605&top_left_y=1803&top_left_x=1088)

解答配图

证明 由蒙日定理, 直线 $A D, Q P, B C$ 交于一点, 设为 $K$. 联结 $A P, A Q, B P, B Q$.
因为 $\triangle K P D \sim \triangle K A Q$, 所以 $\frac{D P}{A Q}=\frac{K P}{K A}$; 因为 $\triangle K P A \sim \triangle K D Q$, 所以 $\frac{A P}{D Q}=\frac{K A}{K Q}$. 将两式相乘得,

$$
\frac{A P \cdot D P}{A Q \cdot D Q}=\frac{K P}{K Q}
$$

同理, $\frac{B P \cdot C P}{B Q \cdot C Q}=\frac{K P}{K Q}$, 从而

$$
\frac{A P \cdot D P}{A Q \cdot D Q}=\frac{B P \cdot C P}{B Q \cdot C Q}
$$

延长 $P Q$ 交 $A B$ 于点 $M$. 因为 $\triangle A Q M \sim \triangle P A M$, 所以

$$
\frac{A Q}{A P}=\frac{A M}{P M}=\frac{Q M}{A M}
$$

于是

$$
\left(\frac{A Q}{A P}\right)^{2}=\frac{A M}{P M} \cdot \frac{Q M}{A M}=\frac{Q M}{P M}
$$

同理, $\left(\frac{B Q}{B P}\right)^{2}=\frac{Q M}{P M}$. 从而

$$
\left(\frac{A Q}{A P}\right)^{2}=\left(\frac{B Q}{B P}\right)^{2}, \quad \frac{A Q}{A P}=\frac{B Q}{B P}
$$

由式 (1), (2) 知,

$$
\frac{D P}{D Q}=\frac{C P}{C Q}
$$

证毕.

3. 给定正整数 $n, k, k \leq n-2$. 设实数集 $\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$ 的任意 $k$ 元子集的元素和的绝对值不超过 1 . 证明: 若 $\left|a_{1}\right| \geq 1$, 则对任意的 $2 \leq i \leq n$, 都有

$$
\left|a_{1}\right|+\left|a_{i}\right| \leq 2
$$

(冷岗松 供题)

证明 不妨设 $a_{1} \geq 1$, 此时要证结论成立, 只须证明对任意 $2 \leq j \leq n$ 有 $a_{j} \geq a_{1}-2$ 且 $a_{j} \leq 2-a_{1}$. 记 $[n]=\{1,2, \cdots, n\}$.

先证 $a_{j} \geq a_{1}-2$.

设 $2 \leq j \leq n$, 取 $[n]$ 的两个 $k$ 元子集 $I, J$, 使得 $I \backslash J=\{1\}, J \backslash I=\{j\}$. 由条件知

$$
\sum_{s \in I} a_{s} \leq 1, \quad \sum_{s \in J} a_{s} \geq-1
$$

将这两个不等式作差可得 $a_{1}-a_{j} \leq 2$, 即 $a_{j} \geq a_{1}-2$.

再证 $a_{j} \leq 2-a_{1}$.
记 $S=\left\{i \in[n] \mid a_{i}>0\right\}$, 则 $1 \in S$. 假设 $|S| \geq k$, 取 $S$ 的一个 $k$ 元子集 $I$,使得 $1 \in I$, 由条件知

$$
0<\sum_{s \in I \backslash\{1\}} a_{s} \leq 1-a_{1} \leq 0,
$$

矛盾! 故 $|S| \leq k-1$. 因此

$$
|[n] \backslash(S \cup\{j\})| \geq n-k \geq 2
$$

从而存在 $i^{\prime} \neq j^{\prime} \in[n] \backslash\{1, j\}$, 使得 $a_{i^{\prime}} \leq 0, a_{j^{\prime}} \leq 0$. 现选取 $[n]$ 的两个 $k$ 元子集 $I$ 和 $I^{\prime}$, 使得 $I \backslash I^{\prime}=\{1, j\}, I^{\prime} \backslash I=\left\{i^{\prime}, j^{\prime}\right\}$. 由条件知

$$
\sum_{s \in I} a_{s} \leq 1, \quad \sum_{s \in I^{\prime}} a_{s} \geq-1
$$

将两个不等式相减可得

$$
a_{j}+a_{1}-a_{i^{\prime}}-a_{j^{\prime}} \leq 2,
$$

故

$$
a_{j} \leq 2-a_{1}+a_{i^{\prime}}+a_{j^{\prime}} \leq 2-a_{n}
$$

证毕.

4. 定义 $n$ 元整数组的一次变换为:

$$
\left(a_{1}, a_{2}, \cdots, a_{n-1}, a_{n}\right) \rightarrow\left(a_{1}+a_{2}, a_{2}+a_{3}, \cdots, a_{n-1}+a_{n}, a_{n}+a_{1}\right)
$$

求所有的正整数对 $(n, k), n, k \geq 2$, 满足: 对任意的 $n$ 元整数组 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$,在有限次变换后所得数组中每一个数都是 $k$ 的倍数.

(张新泽 供题)

解 $(n, k)=\left(2^{p}, 2^{q}\right), p, q \in N^{*}$.

引理 记 $n$ 元整数组 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 经过 $t$ 次变换后所得的数组为 $\left(a_{1}^{(t)}, a_{2}^{(t)}, \cdots, a_{n}^{(t)}\right)$, 则

$$
a_{i}^{(t)}=a_{i} \mathrm{C}_{t}^{0}+a_{i+1} \mathrm{C}_{t}^{1}+\cdots+a_{i+t} \mathrm{C}_{t}^{t}, \quad i=1,2, \cdots, n .
$$

引理证明 用数学归纳法.

当 $t=1$ 时结论显然成立.

设 $a_{i}^{(t)}=a_{i} \mathrm{C}_{t}^{0}+a_{i+1} \mathrm{C}_{t}^{1}+\cdots+a_{i+t} \mathrm{C}_{t}^{t}, i=1,2, \cdots, n$. 则

$a_{i}^{(t+1)}=a_{i}^{(t)}+a_{i+1}^{(t+1)}$

$$
\begin{aligned}
& =\left(a_{i} \mathrm{C}_{t}^{0}+a_{i+1} \mathrm{C}_{t}^{1}+\cdots+a_{i+t} \mathrm{C}_{t}^{t}\right)+\left(a_{i+1} \mathrm{C}_{t}^{0}+a_{i+2} \mathrm{C}_{t}^{1}+\cdots+a_{i+1+t} \mathrm{C}_{t}^{t}\right) \\
& =a_{i} \mathrm{C}_{t}^{0}+a_{i+1}\left(\mathrm{C}_{t}^{1}+\mathrm{C}_{t}^{0}\right)+a_{i+2}\left(\mathrm{C}_{t}^{2}+\mathrm{C}_{t}^{1}\right)+\cdots+a_{i+t}\left(\mathrm{C}_{t}^{t}+\mathrm{C}_{t}^{t-1}\right)+a_{i+1+t} \mathrm{C}_{t}^{t} \\
& =a_{i} \mathrm{C}_{t+1}^{0}+a_{i+1} \mathrm{C}_{t+1}^{1}+\cdots+a_{i+t+1} \mathrm{C}_{t+1}^{t+1}
\end{aligned}
$$

引理证毕.

回到原题.

一方面, 我们证明 $n, k$ 均为 2 的幂.

注意到每次变换后所得的 $n$ 个数之和是变换前 $n$ 个数之和的 2 倍, 令 $a_{1}=1, a_{2}=a_{3}=\cdots=a_{n}=0$.

由题设存在有限次变换 (不妨设为 $m$ 次) 使得所得的每个数均为 $k$ 的倍数,因此 $m$ 次变换后所得的 $n$ 个数之和为 $2^{m}$, 故 $k \mid 2^{m}$, 即 $k$ 为 2 的幂.

于是, $m$ 次变换后所得的每个数均为 2 的倍数, 进而以后的每次变换后所得的数均为 2 的倍数.

取 $2^{s}>m, s \in \mathbb{N}^{*}$. 注意到 $\mathrm{C}_{2^{s}}^{i}=\frac{2^{s}}{i} \mathrm{C}_{2^{s}-1}^{i-1}\left(1 \leq i \leq 2^{s}-1\right)$ 为偶数, 则经过 $2^{s}$ 次变换后有

$$
a_{1}^{\left(2^{s}\right)} \equiv a_{1}+a_{1+2^{s}} \equiv 0 \quad(\bmod 2) .
$$

故 $a_{1+2^{s}}=1=a_{1}$. 因此, $n \mid 2^{s}$, 即 $n$ 为 2 的幂.

另一方面, 我们说明当 $(n, k)=\left(2^{p}, 2^{q}\right), p, q \in \mathbb{N}^{*}$ 时, 任意 $n$ 元整数组 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 均能经过有限次变换使得到的每个数均为 $k$ 的倍数.

结合引理及 $\mathrm{C}_{2^{s}}^{i}$ 是偶数, 对数组 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 经过 $n=2^{p}$ 次变换后, 有

$$
a_{i}^{(n)} \equiv a_{i}+a_{i+n} \equiv 0 \quad(\bmod 2), i=1,2, \cdots, n
$$

再将 $\left(\frac{1}{2} a_{1}^{(n)}, \frac{1}{2} a_{2}^{(n)}, \cdots, \frac{1}{2} a_{n}^{(n)}\right)$ 经过 $n=2^{p}$ 次变换得到的每个数也均为偶数, 即 $a_{i}^{(2 n)} \equiv 0(\bmod 4), i=1,2, \cdots, n$.

由归纳原理有 $a_{i}^{(q n)} \equiv 0\left(\bmod 2^{q}\right), i=1,2, \cdots, n$. 即每个数均为 $k=2^{q}$ 的倍数.

综上, 结论成立.

$$
\text { 第二天 }
$$

8 月 16 日 8:00-12:00

5. 证明: 存在无穷多个正整数组 $(a, b, c)$, 满足 $a, b, c$ 两两互素, 且 $a b+c$, $b c+a, c a+b$ 两两互素.
证明 取正整数 $k$ 满足 $k-1$ 不是 5 的倍数.

下证正整数组 $(2 k-1,2 k, 2 k+1)$ 满足题中要求.

事实上, 显然有 $2 k-1,2 k, 2 k+1$ 两两互素, 且

$$
\begin{aligned}
& (2 k-1) 2 k+(2 k+1)=4 k^{2}+1, \\
& 2 k(2 k+1)+(2 k-1)=4 k^{2}+4 k-1, \\
& (2 k+1)(2 k-1)+2 k=4 k^{2}+2 k-1 .
\end{aligned}
$$

因为 $4 k^{2}+1$ 是奇数, 所以

$\left(4 k^{2}+1,4 k^{2}+4 k-1\right)=\left(4 k^{2}+1,4 k-2\right)=\left(4 k^{2}+1,2 k-1\right)=(2,2 k-1)=1$.

又 $k-1$ 不是 5 的倍数, 因此

$$
\left(4 k^{2}+1,4 k^{2}+2 k-1\right)=\left(4 k^{2}+1,2 k-2\right)=\left(4 k^{2}+1, k-1\right)=(5, k-1)=1 .
$$

最后，

$$
\left(4 k^{2}+4 k-1,4 k^{2}+2 k-1\right)=\left(4 k^{2}+4 k-1,2 k\right)=1 .
$$

从而 $(2 k-1,2 k, 2 k+1)$ 的确满足题中要求, 故满足题中要求的正整数组有无穷多个.

6. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是 $n$ 个非负实数, 记 $S_{k}=\sum_{i=1}^{k} a_{i}, 1 \leq k \leq n$. 证明:

$$
\sum_{i=1}^{n}\left(a_{i} S_{i} \sum_{j=1}^{n} a_{j}^{2}\right) \leq \sum_{i=1}^{n}\left(a_{i} S_{i}\right)^{2}
$$

(王广廷 供题)

证法一 令 $b_{i}=a_{i} S_{i}, c_{i}=\sum_{j=1}^{n} a_{j}^{2}, i=1,2, \cdots, n$. 则原不等式等价于

$$
\sum_{i=1}^{n} b_{i} c_{i} \leq \sum_{i=1}^{n} b_{i}^{2}
$$

注意到对 $1 \leq i \leq n$, 有

$$
\begin{aligned}
B_{i} & =b_{1}+b_{2}+\cdots+b_{i} \\
& =a_{1} S_{1}+a_{2} S_{2}+\cdots+a_{i} S_{i} \\
& \leq\left(a_{1}+a_{2}+\cdots+a_{i}\right) S_{i} \\
& =S_{i}^{2}
\end{aligned}
$$

故由阿贝尔恒等式有

$$
\begin{aligned}
\sum_{i=1}^{n} b_{i} c_{i} & =\sum_{i=1}^{n-1} B_{i}\left(c_{i}-c_{i+1}\right)+B_{n} c_{n} \\
& \leq \sum_{i=1}^{n-1} a_{i} S_{i}^{2}+B_{n} c_{n} \\
& \leq \sum_{i=1}^{n} a_{i} S_{i}^{2}=\sum_{i=1}^{n} b_{i}^{2} .
\end{aligned}
$$

故 $(*)$ 式成立, 所以原不等式成立.

证法二 注意到下面的恒等式

$$
\sum_{i=1}^{n}\left(a_{i} S_{i} \sum_{j=i}^{n} a_{j}^{2}\right)=\sum_{j=1}^{n}\left(a_{j}^{2} \sum_{i=1}^{j} a_{i} S_{i}\right) .
$$

故要证明原不等式, 只须证明

$$
\sum_{j=1}^{n}\left(a_{j}^{2} \sum_{i=1}^{j} a_{i} S_{i}\right) \leq \sum_{j=1}^{n} a_{j}^{2} S_{j}^{2}
$$

对 $1 \leq j \leq n$, 比较上式两端 $a_{j}^{2}$ 的系数, 要使得上式成立, 只须

$$
\sum_{i=1}^{j} a_{i} S_{i} \leq S_{j}^{2}
$$

事实上, $\sum_{i=1}^{j} a_{i} S_{i} \leq\left(\sum_{i=1}^{j} a_{j}\right) S_{j}=S_{j}^{2}$. 故上式成立. 所以, 原不等式成立.

7. 如图, $A B C D$ 为圆内接四边形, $\angle B A C=\angle D A C$. 设 $\odot I_{1}, \odot I_{2}$ 分别为 $\triangle A B C, \triangle A D C$ 的内切圆. 证明: $\odot I_{1}, \odot I_{2}$ 的某一条外公切线与 $B D$ 平行.

(羊明亮 供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_136b2b83847a9e4a1310g-7.jpg?height=503&width=482&top_left_y=1870&top_left_x=433)

第 7 题图

![](https://cdn.mathpix.com/cropped/2024_02_26_136b2b83847a9e4a1310g-7.jpg?height=503&width=479&top_left_y=1873&top_left_x=1154)

解答配图

证明 如图, 设 $I$ 为 $\triangle A B D$ 的内心, 连接 $B I$. 过 $I$ 作 $\odot I_{1}$ 的一条切线, 切点
为 $E$, 交 $A B$ 于点 $M$.

由熟知的结论 (鸡爪定理) $C I=C B$ 以及 (圆外切四边形对边长度之和相等) $C I+M B=C B+M I$ 知 $M B=M I$, 从而 $\angle M B I=\angle M I B$. 注意到 $I$ 为 $\triangle A B D$ 的内心, 有 $\angle M B I=\angle D B I$. 所以 $\angle M I B=\angle D B I$, 由此 $I E / / B D$.

同理, 过 $I$ 作 $\odot I_{2}$ 的一条切线, 切点为 $F$, 有 $I F / / B D$.

故 $E, I, F$ 三点共线, 即 $\odot I_{1}, \odot I_{2}$ 的一条外公切线 $E F$ 与 $B D$ 平行.

8. 给定整数 $m, n, 2 \leq m<n,(m, n)=1$. 求最小的整数 $k$, 满足：对集合 $\{1,2, \cdots, n\}$ 的任意 $m$ 元子集 $I$, 若 $\sum_{i \in I} i>k$, 则存在 $n$ 个实数 $a_{1} \leq a_{2} \leq \cdots \leq$ $a_{n}$, 使得

$$
\frac{1}{m} \sum_{i \in I} a_{i}>\frac{1}{n} \sum_{i=1}^{n} a_{i}
$$

(邹瑾 供题)

解 满足条件的最小整数 $k=\frac{m n+m-n+1}{2}$.

首先证明当 $k=\frac{m n+m-n+1}{2}$ 时满足条件.

对集合 $\{1,2, \cdots, n\}$ 的满足 $\sum_{i \in I} I>k$ 的 $m$ 元子集 $I$, 设 $I=\left\{i_{1}, i_{2}, \cdots, i_{m}\right\}$,其中 $1 \leq i_{1}<i_{2}<\cdots<i_{m} \leq n$.

注意到由 $(m, n)=1$, 可得

$$
\begin{aligned}
\sum_{r=1}^{m}\left[(r-1) \frac{n}{m}\right] & =\frac{1}{2}\left(\sum_{r=1}^{m-1}\left[r \cdot \frac{n}{m}\right]+\sum_{r=1}^{m-1}\left[(m-r) \cdot \frac{n}{m}\right]\right) \\
& =\frac{1}{2} \cdot(n-1) \cdot(m-1),
\end{aligned}
$$

因此

$$
\sum_{r=1}^{m}\left(\left[(r-1) \frac{n}{m}\right]+1\right)=k<\sum_{r=1}^{m} i_{r}
$$

从而存在 $1 \leq r \leq m$ 使得 $i_{r}>\left[(r-1) \frac{n}{m}\right]+1$.

取 $a_{1}=\cdots=a_{i_{r}-1}=0, a_{i_{r}}=a_{i_{r}+1}=\cdots=a_{n}=1$, 则

$$
\frac{1}{m} \cdot \sum_{i \in I} a_{i}=\frac{m-r+1}{m}, \quad \frac{1}{n} \cdot \sum_{i=1}^{n} a_{i}=\frac{n-i_{r}+1}{n},
$$

由 $i_{r}>\left[(r-1) \frac{n}{m}+1\right]$ 及 $i_{r}$ 为整数可得 $i_{r}>(r-1) \frac{n}{m}+1$. 于是

$$
\frac{1}{m} \sum_{i \in I} a_{i}>\frac{1}{n} \sum_{i=1}^{n} a_{i}
$$

结论成立.

下面证明当 $k<\frac{m n+m-n+1}{2}$ 时不满足条件.
取 $i_{r}=\left[(r-1) \frac{n}{m}\right]+1, r=1,2, \cdots, m$, 则 $I=\left\{i_{1}, i_{2}, \cdots, i_{m}\right\} \subseteq\{1,2, \cdots, n\}$,且与前面类似可得

$$
\sum_{i \in I} i=\frac{m n+m-n+1}{2}>k
$$

对 $n$ 个实数 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 有

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} & =\sum_{r=1}^{m-1}\left(\sum_{i=i_{r}}^{i_{r}+1} a_{i}\right)+\sum_{i=i_{m}}^{n} a_{i} \\
\geq & \sum_{r=1}^{m-1} a_{i_{r}}\left(i_{r+1}-i_{r}\right)+a_{i_{m}}\left(n-i_{m}+1\right) \\
& =i_{1}\left(-a_{i_{1}}\right)+i_{2}\left(a_{i_{1}}-a_{i_{2}}\right)+\cdots+i_{m}\left(a_{i_{m}-1}-a_{i_{m}}\right)+(n+1) a_{i_{m}} \\
& \geq 1 \cdot\left(-a_{i_{1}}\right)+\left(\frac{n}{m}+1\right)\left(a_{i_{1}}-a_{i_{2}}\right)+\cdots \\
& \quad+\left((m-1) \frac{n}{m}+1\right)\left(a_{i_{m}}-a_{i_{m}}\right)+(n+1) a_{i_{m}} \\
& =\frac{n}{m}\left(a_{i_{1}}+a_{i_{2}}+\cdots+a_{i_{m}}\right),
\end{aligned}
$$

于是有

$$
\frac{1}{n} \sum_{i=1}^{n} a_{i} \geq \frac{1}{m} \sum_{i \in I} a_{i}
$$

结论不成立.

综上所述, 所求最小整数 $k=\frac{m n+m-n+1}{2}$.

