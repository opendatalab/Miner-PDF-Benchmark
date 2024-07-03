数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2023 年数学新星研修论坛的几道数论题目 

赖力

(北京大学, 100871)

在 2023 年 8 月 3-10 日于上海举办的数学新星研修论坛中, 我与同学们交流讨论了九道数论问题. 这些题目来自于美国数学月刊 (AMM) 以及不同年代的几篇数学论文.

陈澍同学给出了第 4 题 (Morley 同余式) 的一个简洁证明; 周嘉豪同学简化了第 6 题的证明; 翁斌同学加强了第 7 题的结论. 另外还有多位同学对一些题目给出了不同的解答, 在此我一并感谢. 前面提到的几位同学的证明均比题目来源处的原始证明更加简洁, 这印证了“数学新星” 的寓意. 我也受到鼓舞, 于是将这几道题目的解答进行了整理, 期待它们能够给更多的同学带来启发.

毫无疑问, 这些题目会有不同的、更简便的解答方式. 限于时间与水平, 我在此文中没有追求一题多解或者最简解答. 作为我个人对题目难度的一个大致判断:题目 1、2、5 的难度大约在高中数学联赛的水平, 其余题目的难度则超过了联赛.

## I. 题 目

1. 我们用 $\{x\}$ 表示实数 $x$ 的小数部分. 设 $p, q$ 是两个互素的正整数, 其中 $p>q>1$. 求证: 存在无穷多个正整数 $n$ 使得

$$
\left\{\frac{p^{n}}{q^{n}}\right\}>\frac{1}{p}
$$

2. 对任何正整数 $k$, 我们记 $p_{k}$ 为第 $k$ 个素数, 记 $a_{k}=p_{k} p_{k+1}$ (例如 $a_{1}=2 \cdot 3$, $\left.a_{2}=3 \cdot 5, a_{3}=5 \cdot 7, a_{4}=7 \cdot 11, \cdots\right)$. 一个正整数 $m$ 被称作 “好数”, 如果 $m$ 可以表示成 $m=\prod_{k=1}^{\infty} a_{k}^{s_{k}}$ 的形式, 其中 $\left\{s_{k}\right\}_{k \geq 1}$ 是非负整数数列, 且仅有有限个 $k$ 使得 $s_{k} \neq 0$ (例如, $1, a_{2} a_{3}^{3} a_{9}^{2}, a_{5}^{2} a_{8}^{7}, a_{4}$ 均是好数). 我们将前 $n$ 个正整数 $1,2, \ldots, n$ 中好数的个数记作 $f(n)$. 求证: 对任何正整数 $n$, 我们有

$$
\frac{1}{2}\lfloor\sqrt{n}\rfloor \leq f(n) \leq\lfloor\sqrt{n}\rfloor
$$[^0]

3. 求证: 不定方程 $y^{2}=3^{a}+2^{b}+1$ 的全部正整数解为 $(y, a, b)=(6,1,5),(6,3,3)$.
4. 求证 Morley 同余式: 对于任何素数 $p \geq 5$, 我们有

$$
(-1)^{\frac{p-1}{2}}\left(\begin{array}{c}
p-1 \\
\frac{p-1}{2}
\end{array}\right) \equiv 4^{p-1} \quad\left(\bmod p^{3}\right)
$$

5. 设 $P(X)=\sum_{i=0}^{n} a_{i} X^{i}$ 是一个 $n$ 次多项式, 且它的所有系数 $a_{0}, a_{1}, \ldots, a_{n}$ 均属于集合 $\{-1,1\}$. 求证:

$$
\operatorname{ord}_{X=1} P(X)<2^{v_{2}(n+1)}
$$

其中 $\operatorname{ord}_{X=1} P(X)=\max \left\{k \in \mathbb{N} \cup\{0\} \mid(X-1)^{k}\right.$ 整除 $\left.P(X)\right\}$ 为 $P(X)$ 在 $X=1$处的根的重数, 而 $v_{2}(n+1)=\max \left\{k \in \mathbb{N} \cup\{0\} \mid 2^{k}\right.$ 整除 $\left.n+1\right\}$ 为 $n+1$ 含 2 的幂次.

6. 已知正整数 $n$ 满足

$$
v_{2}(\sigma(n))>\log _{2} n,
$$

求证: $n$ 一定是若干个互不相同的 Mersenne 素数的乘积.

注: $\sigma(n)=\sum_{d \mid n} d$ 表示 $n$ 的正约数之和. $v_{2}(m)$ 表示正整数 $m$ 含 2 的幂次, 即满足 $2^{k} \mid m$ 的最大的非负整数 $k$. 我们称满足 $p+1$ 是 2 的方幂的素数 $p$ 为 Mersenne 素数.

7. 我们记 $S_{2}(n)$ 为 $n$ 在二进制表示下的数字和.

(1) 求证: 对任何实数 $\alpha \in[0,+\infty)$, 以及对于 $\alpha=+\infty$, 均存在一列正整数 $\left\{n_{k}\right\}_{k \geq 1}$ 使得

$$
\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=\alpha
$$

(2) 求证: 存在无穷多个正整数 $n$ 使得

$$
\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)} \leq \frac{4\left(\log _{2} \log _{2} n\right)^{2}}{\log _{2} n} .
$$

8. 设 $p$ 是一个奇素数. 我们定义 Fekete 多项式

$$
f_{p}(z)=\sum_{a=0}^{p-1}\left(\frac{a}{p}\right) z^{a}
$$

这里 $\left(\frac{a}{p}\right)$ 是 Legendre 符号. 求证: $f_{p}(z)$ 至少有 $\frac{p-1}{2}$ 个根在单位圆周上.

9. 求证: 对任何正整数 $m, n$, 区间 $\left[m, m+10 n^{\frac{3}{2}}\right]$ 中存在 $n$ 个两两不同的正整数 $a_{1}, a_{2}, \ldots, a_{n}$ 使得 $k \mid a_{k}, k=1,2, \ldots, n$.

## II. 解答与评注

题 1 我们用 $\{x\}$ 表示实数 $x$ 的小数部分. 设 $p, q$ 是两个互素的正整数, 其中 $p>q>1$. 求证: 存在无穷多个正整数 $n$ 使得

$$
\left\{\frac{p^{n}}{q^{n}}\right\}>\frac{1}{p}
$$

证明 对任何正整数 $n$, 我们记 $x_{n}=\left\lfloor\frac{p^{n}}{q^{n}}\right\rfloor, y_{n}=\left\{\frac{p^{n}}{q^{n}}\right\}$. 则我们有

$$
x_{n+1}+y_{n+1}=\frac{p^{n+1}}{q^{n+1}}=\frac{p}{q}\left(x_{n}+y_{n}\right)
$$

于是

$$
q x_{n+1}-p x_{n}=p y_{n}-q y_{n+1}, \quad \forall n \in \mathbb{N} .
$$

我们用反证法. 假设本题结论不成立, 则存在 $n_{0}$ 使得对任何正整数 $n \geq n_{0}$ 有 $0 \leq y_{n} \leq \frac{1}{p}$. 由于 $\operatorname{gcd}(p, q)=1$ 且 $q>1$, 故 $y_{n} \neq 0$, 所以

$$
0<y_{n} \leq \frac{1}{p}, \quad \forall n \geq n_{0}
$$

式 (2) 推出

$$
-1<p \cdot 0-q \cdot \frac{1}{p}<p y_{n}-q y_{n+1}<p \cdot \frac{1}{p}-q \cdot 0=1, \quad \forall n \geq n_{0}
$$

注意到 (1) 式左端是整数, 由于区间 $(-1,1)$ 中的整数仅有 0 , 故

$$
p y_{n}-q y_{n+1}=0, \quad \forall n \geq n_{0} .
$$

这表明 $\left\{y_{n}\right\}_{n \geq n_{0}}$ 是一个公比为 $\frac{p}{q}$ 的等比数列, 于是

$$
y_{n}=\left(\frac{p}{q}\right)^{n-n_{0}} y_{n_{0}}, \quad \forall n \geq n_{0}
$$

但是 $\frac{p}{q}>1, y_{n_{0}}>0$, 当 $n \rightarrow+\infty$ 上式推出 $y_{n} \rightarrow+\infty$, 与 $(2)$ 矛盾.

评注 一个未被解决的研究性问题是: 数列 $\left\{\left(\frac{3}{2}\right)^{n}\right\}, n=1,2,3, \cdots$ 是否在区间 $[0,1]$ 中稠密?

题 $2\left(1950\right.$, Erdös) 对任何正整数 $k$, 我们记 $p_{k}$ 为第 $k$ 个素数, 记 $a_{k}=p_{k} p_{k+1}$ (例如 $a_{1}=2 \cdot 3, a_{2}=3 \cdot 5, a_{3}=5 \cdot 7, a_{4}=7 \cdot 11, \cdots$ ). 一个正整数 $m$ 被称作“好数”, 如果 $m$ 可以表示成 $m=\prod_{k=1}^{\infty} a_{k}^{s_{k}}$ 的形式, 其中 $\left\{s_{k}\right\}_{k \geq 1}$ 是非负整数数列, 且仅有有限个 $k$ 使得 $s_{k} \neq 0$ (例如, $1, a_{2} a_{3}^{3} a_{9}^{2}, a_{5}^{2} a_{8}^{7}, a_{4}$ 均是好数). 我们将前 $n$ 个正整数 $1,2, \ldots, n$ 中好数的个数记作 $f(n)$. 求证: 对任何正整数 $n$, 我们有

$$
\frac{1}{2}\lfloor\sqrt{n}\rfloor \leq f(n) \leq\lfloor\sqrt{n}\rfloor
$$

题目来源 Paul Erdös, Number of integers of special form. The American Mathematical Monthly 1950, Problem 635.

证明 首先我们证明好数的表示方式是唯一的. 假设

$$
m=\prod_{k=1}^{\infty} a_{k}^{s_{k}}=\prod_{k=1}^{\infty} a_{k}^{s_{k}^{\prime}}
$$

其中 $s_{k}, s_{k}^{\prime}(k \in \mathbb{N})$ 是非负整数, 且只有有限项非零. 利用 $a_{k}=p_{k} p_{k+1}$ 将 $m$ 写为标准的素因子分解, 我们有

$$
m=p_{1}^{s_{1}} \prod_{k=2}^{\infty} p_{k}^{s_{k}+s_{k-1}}=p_{1}^{s_{1}^{\prime}} \prod_{k=2}^{\infty} p_{k}^{s_{k}^{\prime}+s_{k-1}^{\prime}}
$$

于是由算术基本定理的唯一性部分, 我们有 $s_{1}=s_{1}^{\prime}, s_{k}+s_{k-1}=s_{k}^{\prime}+s_{k-1}^{\prime}$, $\forall k=2,3, \ldots$ 由此易得 $s_{k}=s_{k}^{\prime}, \forall k \in \mathbb{N}$. 即好数的表示方式是唯一的.

现在定义映射 $g:\{$ 全体好数 $\} \longrightarrow\{$ 正的完全平方数 $\}$ 如下：设好数 $m$ 的唯一表示为 $m=\prod_{k=1}^{\infty} a_{k}^{s_{k}}$, 其中 $s_{k}(k \in \mathbb{N})$ 是非负整数, 且只有有限项非零, 则我们定义 $g(m)=\prod_{k=1}^{\infty} p_{k}^{2 s_{k}}$. 显然 $g(m)$ 是正的完全平方数.

我们断言 $g$ 是单射. 事实上, 若两个好数 $m=\prod_{k=1}^{\infty} a_{k}^{s_{k}}$ 与 $m^{\prime}=\prod_{k=1}^{\infty} a_{k}^{s_{k}^{\prime}}$ 使得 $g(m)=g\left(m^{\prime}\right)$, 则由 $g$ 的定义, 有 $\prod_{k=1}^{\infty} p_{k}^{2 s_{k}}=\prod_{k=1}^{\infty} p_{k}^{2 s_{k}^{\prime}}$. 从而由算术基本定理的唯一性部分, 我们得到 $s_{k}=s_{k}^{\prime}, \forall k \in \mathbb{N}$. 于是 $m=m^{\prime}$.

注意到 $a_{k}>p_{k}^{2}, \forall k \in \mathbb{N}$. 故对于任何好数 $m$, 我们有 $g(m) \leq m$. 于是当 $m$ 是好数且 $m \leq n$ 时, 有 $g(m)$ 是正的完全平方数且 $g(m) \leq n$. 这表明 $g$ 的限制给出了以下的单射:

\{不超过 $n$ 的好数 $\} \longrightarrow\{$ 不超过 $n$ 的正的完全平方数 $\}$.

比较两个集合的元素个数, 我们便得到 $f(n) \leq\lfloor\sqrt{n}\rfloor$.

另一方面, 我们定义映射 $h:\{$ 全体奇完全数 $\} \longrightarrow\{$ 好数 $\}$ 如下：由算术基本定理, 任何奇完全数 $m$ 可以唯一的写成 $m=\prod_{k=1}^{\infty} p_{k+1}^{2 s_{k}}$ 的形式, 其中 $s_{k}(k \in \mathbb{N})$ 是非负整数, 且只有有限项非零, 则我们定义 $h(m)=\prod_{k=1}^{\infty} a_{k}^{s_{k}}$. 由于好数的表示方式唯一, 故 $h$ 是单射. 注意到 $a_{k}<p_{k+1}^{2}, \forall k \in \mathbb{N}$, 故对任何奇完全平方数 $m$, 我们有 $h(m) \leq m$. 于是 $h$ 的限制给出以下的单射:

\{不超过 $n$ 的奇完全平方数 $\} \longrightarrow\{$ 不超过 $n$ 的好数 $\}$.

比较集合的元素个数, 我们便得到 $\frac{1}{2}\lfloor\sqrt{n}\rfloor \leq f(n)$.

评注 构造单射、满射是常用的估计集合元素个数的方法.
题 $3\left(2011\right.$, Leitner) 求证: 不定方程 $y^{2}=3^{a}+2^{b}+1$ 的全部正整数解为 $(y, a, b)=(6,1,5),(6,3,3)$.

## 题目来源 $\quad[5$, Theorem 3.1].

证明 设正整数 $y, a, b$ 满足 $y^{2}=3^{a}+2^{b}+1$.

当 $a=1$ 时, 有 $(y+2)(y-2)=2^{b}$. 故 $y+2, y-2$ 均是 2 的方幂. 设 $y+2=2^{b_{1}}$, $y-2=2^{b_{2}}$, 其中 $b_{1}, b_{2}$ 为非负整数, $b_{1}>b_{2}$. 则

$$
4=(y+2)-(y-2)=2^{b_{1}}-2^{b_{2}} .
$$

比较前式左右两端含 2 的幂次得到 $b_{2}=v_{2}(4)=2$, 故 $y=6$. 解得 $(y, a, b)=$ $(6,1,5)$. 易验证此解的确满足原不定方程.

当 $b=3$ 时, 有 $(y+3)(y-3)=3^{a}$. 故 $y+3, y-3$ 均是 3 的方幂. 设 $y+3=3^{a_{1}}$, $y-3=3^{a_{2}}$, 其中 $a_{1}, a_{2}$ 为非负整数, $a_{1}>a_{2}$. 则

$$
6=(y+3)-(y-3)=3^{a_{1}}-3^{a_{2}},
$$

比较前式左右两端含 3 的幂次得到 $a_{2}=v_{3}(6)=1$, 故 $y=6$. 解得 $(y, a, b)=$ $(6,3,3)$. 易验证此解的确满足原不定方程.

以下设 $a \neq 1$ 且 $b \neq 3$. 我们将证明此时无解.

因 $a \neq 1$, 故 $a \geq 2$, 我们有 $3^{a} \equiv 0(\bmod 9)$. 代入原不定方程, 得

$$
y^{2} \equiv 2^{b}+1 \quad(\bmod 9) \text {. }
$$

注意 $y^{2}$ 模 9 的余数只可能为 $0,1,4,7$. 而 $2^{6} \equiv 1(\bmod 9)$,

![](https://cdn.mathpix.com/cropped/2024_02_26_968d88bb16b832a2516dg-05.jpg?height=564&width=832&top_left_y=1723&top_left_x=609)

于是必有 $y^{2} \equiv 2^{b}+1 \equiv 0(\bmod 9)$ ，且

$$
b \equiv 3 \quad(\bmod 6)
$$

由 $(3)$ 以及 $b \neq 3$, 我们有 $b \geq 9$. 从而 $2^{b} \equiv 0(\bmod 16)$. 代入原不定方程, 得到

$$
y^{2} \equiv 3^{a}+1 \quad(\bmod 16)
$$

注意 $y^{2}$ 模 16 的余数只可能为 $0,1,4,9$. 而 $3^{4} \equiv 1(\bmod 16)$,

![](https://cdn.mathpix.com/cropped/2024_02_26_968d88bb16b832a2516dg-06.jpg?height=370&width=880&top_left_y=269&top_left_x=588)

故必有 $y^{2} \equiv 3^{a}+1 \equiv 4(\bmod 16)$, 且

$$
a \equiv 1 \quad(\bmod 4)
$$

由 $(4)$ 以及 $3^{4} \equiv 1(\bmod 5)$, 我们有 $3^{a} \equiv 3(\bmod 5)$. 代入原不定方程, 得到

$$
y^{2} \equiv 2^{b}+4 \quad(\bmod 5)
$$

注意 $y^{2}$ 模 5 的余数只可能为 $0,1,4$. 由 (3) 知 $b$ 为奇数, 故 $b$ 模 4 余 1,3 , 而

![](https://cdn.mathpix.com/cropped/2024_02_26_968d88bb16b832a2516dg-06.jpg?height=207&width=830&top_left_y=1050&top_left_x=613)

故必有 $y^{2} \equiv 2^{b}+4 \equiv 1(\bmod 5)$, 且 $b \equiv 1(\bmod 4)$. 结合 $(3)$, 我们得到

$$
b \equiv 9 \quad(\bmod 12)
$$

由 Fermat 小定理知 $2^{12} \equiv 1(\bmod 13)$, 于是 $(5)$ 推出 $2^{b} \equiv 2^{9} \equiv 5(\bmod 13)$.代入原不定方程, 得到

$$
y^{2} \equiv 3^{a}+6 \quad(\bmod 13)
$$

注意 $y^{2}$ 模 13 的余数只可能为 $0,1,3,4,9,10,12$. 而 $3^{3} \equiv 1(\bmod 13)$,

![](https://cdn.mathpix.com/cropped/2024_02_26_968d88bb16b832a2516dg-06.jpg?height=298&width=864&top_left_y=1781&top_left_x=602)

故必有 $y^{2} \equiv 3^{a}+6 \equiv 9(\bmod 13)$, 且 $a \equiv 1(\bmod 3)$. 结合 $(4)$, 我们得到

$$
a \equiv 1 \quad(\bmod 12)
$$

最后考虑模 7 . 由于 $3^{6} \equiv 1(\bmod 7)$, 由 $(6)$ 我们得到 $3^{a} \equiv 3(\bmod 7)$. 由 $(3)$我们有 $3 \mid b$, 而 $2^{3} \equiv 1(\bmod 7)$, 故 $2^{b} \equiv 1(\bmod 7)$. 代入原不定方程, 我们得到

$$
y^{2} \equiv 3+1+1 \equiv 5 \quad(\bmod 7)
$$

这不可能! (因为 $y^{2}$ 模 7 的余数只可能为 $0,1,2,4$.) 所以当 $a \neq 1$ 且 $b \neq 3$ 时原不定方程无解.
综上, 原不定方程的所有正整数解为 $(y, a, b)=(6,1,5),(6,3,3)$.

评注 解不定方程的常用方法有: 1. 同余、2. 因式分解、3. 比较素数幕次.本解答中前两种方法均发挥了作用. 对于指数型的不定方程, 在初等的范围里考虑同余是最常用的办法.

题 $4(1895$, Morley) 求证 Morley 同余式: 对于任何素数 $p \geq 5$, 我们有

$$
(-1)^{\frac{p-1}{2}}\left(\begin{array}{c}
p-1 \\
\frac{p-1}{2}
\end{array}\right) \equiv 4^{p-1} \quad\left(\bmod p^{3}\right)
$$

题目来源 $[6]$.

证明 (陈澍) 对于任何 $a, b \in\{0,1\}$, 我们记

$$
S_{a}=\sum_{\substack{0<i<p \\ i \equiv a \\(\bmod 2)}} \frac{1}{i}, \quad S_{a, b}=\sum_{\substack{0<i<j<p \\ i \equiv a}} \frac{1}{i j}
$$

引理 1 设 $p$ 是奇素数. 则我们有

$$
\begin{aligned}
2^{p-1} & \equiv 1+p S_{1}+p^{2} S_{1,1} \quad\left(\bmod p^{3}\right) \\
(-1)^{\frac{p-1}{2}}\left(\begin{array}{c}
p-1 \\
\frac{p-1}{2}
\end{array}\right) & \equiv 2^{p-1}\left(1-p S_{0}+p^{2} S_{0,0}\right) \quad\left(\bmod p^{3}\right)
\end{aligned}
$$

证明 我们有

![](https://cdn.mathpix.com/cropped/2024_02_26_968d88bb16b832a2516dg-07.jpg?height=223&width=1008&top_left_y=1505&top_left_x=524)

$$
\begin{aligned}
& =\prod_{\substack{0<i<p \\
i \equiv 1 \\
(\bmod 2)}}\left(1+\frac{p}{i}\right) \\
& \equiv 1+p S_{1}+p^{2} S_{1,1} \quad\left(\bmod p^{3}\right)
\end{aligned}
$$

故 (7) 得证. 而

$$
\begin{aligned}
& (-1)^{\frac{p-1}{2}}\left(\begin{array}{c}
p-1 \\
\frac{p-1}{2}
\end{array}\right)=(-1)^{\frac{p-1}{2}} \frac{(p-1) !}{\left(\frac{p-1}{2}\right) !^{2}}=(-1)^{\frac{p-1}{2}} 2^{p-1} \frac{(p-1) !}{(p-1) ! !^{2}} \\
& =(-1)^{\frac{p-1}{2}} 2^{p-1} \frac{(p-2) ! !}{(p-1) ! !}=(-1)^{\frac{p-1}{2}} 2^{p-1} \frac{\prod_{\substack{0<i<p \\
(\bmod 2)}}(p-i)}{\left.\prod_{\substack{0<i<p \\
i \equiv 0}} i \bmod 2\right)} \\
& =2^{p-1} \prod_{\substack{0<i<p \\
i \equiv 0 \\
(\bmod 2)}}\left(1-\frac{p}{i}\right) \\
& \equiv 2^{p-1}\left(1-p S_{0}+p^{2} S_{0,0}\right) \quad\left(\bmod p^{3}\right)
\end{aligned}
$$

故 (8) 得证. 引理 1 证毕.

引理 2 设素数 $p \geq 5$. 则我们有

$$
\begin{aligned}
S_{1} \equiv-S_{0} \quad\left(\bmod p^{2}\right) \\
S_{1,1} \equiv S_{0,0} \quad(\bmod p)
\end{aligned}
$$

证明 由 Wolstenholme 定理 (仅这里用到了 $p \geq 5$ ), 我们有

$$
S_{0}+S_{1}=\sum_{i=1}^{p-1} \frac{1}{i} \equiv 0 \quad\left(\bmod p^{2}\right)
$$

故 (9) 得证. 而 (10) 是因为

![](https://cdn.mathpix.com/cropped/2024_02_26_968d88bb16b832a2516dg-08.jpg?height=154&width=897&top_left_y=845&top_left_x=585)

$$
\begin{aligned}
& \equiv \sum_{\substack{0<k<l<p \\
k \equiv l \equiv 0 \\
(\bmod 2)}} \frac{1}{k l} \equiv S_{0,0} \quad(\bmod p) .
\end{aligned}
$$

引理 2 证毕.

回到原题, 对任何素数 $p \geq 5$, 我们有

$$
\begin{aligned}
(-1)^{\frac{p-1}{2}}\left(\begin{array}{c}
p-1 \\
\frac{p-1}{2}
\end{array}\right) & \equiv 2^{p-1}\left(1-p S_{0}+p^{2} S_{0,0}\right) \quad\left(\bmod p^{3}\right) \quad(\text { 式 }(8)) \\
& \equiv 2^{p-1}\left(1+p S_{1}+p^{2} S_{1,1}\right) \quad\left(\bmod p^{3}\right) \quad(\text { 引理 } 2) \\
& \equiv 2^{p-1} \cdot 2^{p-1} \quad\left(\bmod p^{3}\right) \quad(\text { 式 }(7)) \\
& \equiv 4^{p-1} \quad\left(\bmod p^{3}\right) .
\end{aligned}
$$

证毕.

题 5 设 $P(X)=\sum_{i=0}^{n} a_{i} X^{i}$ 是一个 $n$ 次多项式, 且它的所有系数 $a_{0}, a_{1}, \ldots, a_{n}$均属于集合 $\{-1,1\}$. 求证:

$$
\operatorname{ord}_{X=1} P(X)<2^{v_{2}(n+1)} \text {. }
$$

其中 $\operatorname{ord}_{X=1} P(X)=\max \left\{k \in \mathbb{N} \cup\{0\} \mid(X-1)^{k}\right.$ 整除 $\left.P(X)\right\}$ 为 $P(X)$ 在 $X=1$处的根的重数, 而 $v_{2}(n+1)=\max \left\{k \in \mathbb{N} \cup\{0\} \mid 2^{k}\right.$ 整除 $\left.n+1\right\}$ 为 $n+1$ 含 2 的幂次.

题目来源 Tamás Erdélyi, Zeros of polynomials with unit coefficients. The American Mathematical Monthly 2009, Problem 11437.

证明 (Richard Stong) 记 $r=v_{2}(n+1)$, 设 $n+1=2^{r} s$, 其中 $s$ 是奇数. 我们用反证法, 假设 $X=1$ 是多项式 $P(X)$ 的至少 $2^{r}$ 重根, 则 $X=1$ 是 $P(X)$ 的
$2^{r}-1$ 阶导数 $P^{\left(2^{r}-1\right)}(X)$ 的根. 于是有

$$
0=\frac{1}{\left(2^{r}-1\right) !} P^{\left(2^{r}-1\right)}(1)=\sum_{i=2^{r}-1}^{n} a_{i}\left(\begin{array}{c}
i \\
2^{r}-1
\end{array}\right)
$$

由于 $a_{i}= \pm 1 \equiv 1(\bmod 2)$, 我们得到

$$
0=\sum_{i=2^{r}-1}^{n} a_{i}\left(\begin{array}{c}
i \\
2^{r}-1
\end{array}\right) \equiv \sum_{i=2^{r}-1}^{n}\left(\begin{array}{c}
i \\
2^{r}-1
\end{array}\right) \quad(\bmod 2)
$$

利用裂项 $\left(\begin{array}{c}i \\ 2^{r}-1\end{array}\right)=\left(\begin{array}{c}i+1 \\ 2^{r}\end{array}\right)-\left(\begin{array}{c}i \\ 2^{r}\end{array}\right)$, 我们有

$$
\sum_{i=2^{r}-1}^{n}\left(\begin{array}{c}
i \\
2^{r}-1
\end{array}\right)=\left(\begin{array}{c}
n+1 \\
2^{r}
\end{array}\right)=\left(\begin{array}{c}
2^{r} s \\
2^{r}
\end{array}\right)
$$

由 (11), (12) 我们得到 $\left(\begin{array}{c}2^{r} s \\ 2^{r}\end{array}\right)$ 是偶数. 但根据 Lucas 定理, $\left(\begin{array}{c}2^{r} s \\ 2^{r}\end{array}\right)$ 是奇数, 矛盾. 于是 $P(X)$ 在 $X=1$ 处根的重数严格小于 $2^{r}$, 证毕.

评注 John E. Littlewood 问: 对于一个次数为 $n$, 系数为 $\pm 1$ 的多项式 $P(X)$,它在 $X=1$ 处的根的重数的最大可能值是多少? (以下我们把系数是 $\pm 1$ 的多项式称作 Littlewood 多项式.)

例子: 当 $n+1=2^{m}$ 为 2 的方幂时, 多项式 $P(X)=\prod_{k=0}^{m-1}\left(X^{2^{k}}-1\right)$ 是一个 $n$ 次的 Littlewood 多项式, 并且 $\operatorname{ord}_{X=1} P(X)=m=\log _{2}(n+1)$.

1997 年, Boyd [2] 证明了: 对任何 $\varepsilon>0$, 存在 $n_{0}(\varepsilon)$, 使得对任何次数为 $n \geq n_{0}(\varepsilon)$ 的 Littlewood 多项式我们有

$$
\operatorname{ord}_{X=1} P(X) \leq(1+\varepsilon) \frac{\ln ^{2} n}{\ln \ln n}
$$

题 6 (2021, Amdeberhan, Moll, Sharma, and Villamizar) 已知正整数 $n$ 满足

$$
v_{2}(\sigma(n))>\log _{2} n,
$$

求证: $n$ 一定是若千个互不相同的 Mersenne 素数的乘积.

注: $\sigma(n)=\sum_{d \mid n} d$ 表示 $n$ 的正约数之和. $v_{2}(m)$ 表示正整数 $m$ 含 2 的幂次, 即满足 $2^{k} \mid m$ 的最大的非负整数 $k$. 我们称满足 $p+1$ 是 2 的方幂的素数 $p$ 为 Mersenne 素数.

题目来源 $[1$, Theorem 1.3]

证明 我们先证明两个引理.

引理 1 设素数 $p$ 不是 Mersenne 素数, $\alpha$ 是任何正整数; 或者 $p$ 是 Mersenne 素数, 但正整数 $\alpha \geq 2$. 则我们有

$$
v_{2}\left(\sigma\left(p^{\alpha}\right)\right) \leq \log _{2}\left(p^{\alpha}\right)-1
$$

证明 若 $p=2$ 或者 $\alpha$ 是偶数, 则 $\sigma\left(p^{\alpha}\right)=1+p+p^{2}+\cdots+p^{\alpha}$ 是奇数. 此时 $v_{2}\left(\sigma\left(p^{\alpha}\right)\right)=0$, 而 $\log _{2}\left(p^{\alpha}\right) \geq \log _{2}(2)=1$, 故结论成立. 以下设 $p$ 是奇素数且 $\alpha$ 为奇数.

注意

$$
\sigma\left(p^{\alpha}\right)=\frac{p^{\alpha+1}-1}{p-1}=(p+1) \cdot \frac{p^{2 \cdot \frac{\alpha+1}{2}}-1}{p^{2}-1} .
$$

由于 $4 \mid p^{2}-1$, 由升幂引理, 我们有 $v_{2}\left(p^{2 \cdot \frac{\alpha+1}{2}}-1\right)=v_{2}\left(p^{2}-1\right)+v_{2}\left(\frac{\alpha+1}{2}\right)$. 于是欲证的不等式等价于

$$
\begin{aligned}
& \log _{2}\left(p^{\alpha}\right) \geq v_{2}\left(\sigma\left(p^{\alpha}\right)\right)+1 \\
\Leftrightarrow & \log _{2}\left(p^{\alpha}\right) \geq v_{2}(p+1)+v_{2}(\alpha+1) \\
\Leftrightarrow & p^{\alpha} \geq 2^{v_{2}(p+1)} \cdot 2^{v_{2}(\alpha+1)} .
\end{aligned}
$$

如果 $\alpha \geq 3$, 则

$$
\begin{aligned}
p^{\alpha} & \geq p \cdot 3^{\alpha-1}=p \cdot(1+2)^{\alpha-1} \\
& \geq p \cdot\left(1+(\alpha-1) \cdot 2+2^{\alpha-1}\right) \\
& >p \cdot(2 \alpha+2)>(p+1)(\alpha+1) \\
& \geq 2^{v_{2}(p+1)} \cdot 2^{v_{2}(\alpha+1)},
\end{aligned}
$$

结论成立. 剩下的情况是 $\alpha=1, p>2$ 且 $p$ 不是 Mersenne 素数. 此时 $p+1$ 不是 2 的方幂, 故 $2^{v_{2}(p+1)} \leq \frac{p+1}{3}$. 于是

$$
p^{\alpha}=p>\frac{p+1}{3} \cdot 2 \geq 2^{v_{2}(p+1)} \cdot 2^{v_{2}(\alpha+1)} \text {, }
$$

结论成立. 引理 1 证毕.

引理 2 设 $q_{1}, q_{2}, \ldots, q_{s}$ 是若干个不同的 Mersenne 素数 $(s \geq 0)$. 则

$$
v_{2}\left(\sigma\left(q_{1} q_{2} \cdots q_{s}\right)\right)<\log _{2}\left(q_{1} q_{2} \cdots q_{s}\right)+1 .
$$

证明 (周嘉豪) 我们有 $\sigma\left(q_{1} q_{2} \cdots q_{s}\right)=\left(1+q_{1}\right)\left(1+q_{2}\right) \cdots\left(1+q_{s}\right)$. 由于 $1+q_{i}$均是 2 的方幂, 故 $v_{2}\left(\sigma\left(q_{1} q_{2} \cdots q_{s}\right)\right)=\log _{2}\left(\left(1+q_{1}\right)\left(1+q_{2}\right) \cdots\left(1+q_{s}\right)\right)$. 欲证的不等式等价于 $\left(1+q_{1}\right)\left(1+q_{2}\right) \cdots\left(1+q_{s}\right)<2 q_{1} q_{2} \cdots q_{s}$, 等价于

$$
\prod_{i=1}^{s}\left(1-\frac{1}{1+q_{i}}\right)>\frac{1}{2}
$$

根据 Bernoulli 不等式, 我们有

$$
\prod_{i=1}^{s}\left(1-\frac{1}{1+q_{i}}\right) \geq 1-\sum_{i=1}^{s} \frac{1}{1+q_{i}}
$$

于是只用证明 $\sum_{i=1}^{s} \frac{1}{1+q_{i}}<\frac{1}{2}$. 由于 $1+q_{i},(i=1,2, \ldots, s)$ 是两两不同的 2 的方幂, 且至少是 4, 故

$$
\sum_{i=1}^{s} \frac{1}{1+q_{i}}<\sum_{k=2}^{\infty} \frac{1}{2^{k}}=\frac{1}{2}
$$

引理 2 证毕.

回到原题, 根据算术基本定理, 任何一个正整数 $n$ 可以表示成以下的形式:

$$
n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{t}^{\alpha_{t}} q_{1} q_{2} \cdots q_{s}
$$

其中 $t, s$ 是非负整数(可以为零); $p_{1}, p_{2}, \ldots, p_{t}, q_{1}, q_{2}, \ldots, q_{s}$ 是 $t+s$ 个两两不同的素数; $\alpha_{1}, \alpha_{2} \ldots, \alpha_{t}$ 是正整数; $q_{1}, q_{2}, \ldots, q_{s}$ 是两两不同的 Mersenne 素数; 而对于每个 $i \in\{1,2, \ldots, t\}$, 要么 $p_{i}$ 不是 Mersenne 素数, 要么 $p_{i}$ 是 Mersenne 素数但 $\alpha_{i} \geq 2$.

根据引理 1 , 我们有

$$
v_{2}\left(\sigma\left(p_{i}^{\alpha_{i}}\right)\right) \leq \log _{2}\left(p_{i}^{\alpha_{i}}\right)-1, \quad i=1,2, \ldots, t
$$

根据引理 2 , 我们有

$$
v_{2}\left(\sigma\left(q_{1} q_{2} \cdots q_{s}\right)\right)<\log _{2}\left(q_{1} q_{2} \cdots q_{s}\right)+1 .
$$

将上面所有式子相加并利用 $\sigma(\cdot)$ 是积性函数, 我们得到

$$
v_{2}(\sigma(n))<\log _{2}(n)-t+1
$$

如果 $v_{2}(\sigma(n))>\log _{2}(n)$, 则上式推出 $t<1$, 只能 $t=0$, 于是 $n$ 形如

$$
n=q_{1} q_{2} \cdots q_{s}
$$

所以 $n$ 是若干个两两不同的 Mersenne 素数的乘积 (显然 $n \neq 1$, 故 $s \geq 1$ ). 证毕.

题 7 我们记 $S_{2}(n)$ 为 $n$ 在二进制表示下的数字和.

(1) (1992, IMO 预选题) 求证: 对任何实数 $\alpha \in[0,+\infty)$, 以及对于 $\alpha=+\infty$,均存在一列正整数 $\left\{n_{k}\right\}_{k \geq 1}$ 使得

$$
\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=\alpha
$$

(2) (1978, Stolarsky) 求证: 存在无穷多个正整数 $n$ 使得

$$
\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)} \leq \frac{4\left(\log _{2} \log _{2} n\right)^{2}}{\log _{2} n}
$$

题目来源 $[8]$.

证明 (1) 我们先证明一个引理.
引理 记 $m_{k}=2^{2^{k}-1}-\sum_{j=1}^{k} 2^{2^{k}-2^{j}}, k \in \mathbb{N}$. 则我们有

$$
S_{2}\left(m_{k}\right)=2^{k}-k, \quad S_{2}\left(m_{k}^{2}\right)=1+\frac{k(k-1)}{2}
$$

证明 对任何整数 $A>a_{1}>a_{2}>\cdots>a_{k} \geq 0$, 我们有

$$
\begin{aligned}
& 2^{A}-2^{a_{1}}-2^{a_{2}}-\cdots-2^{a_{k}} \\
& =\left(2^{A}-2^{a_{1}+1}\right)+\left(2^{a_{1}}-2^{a_{2}+1}\right)+\cdots+\left(2^{a_{k-2}}-2^{a_{k-1}+1}\right)+\left(2^{a_{k-1}}-2^{a_{k}}\right) \\
& =(\underbrace{11 \cdots 1}_{A-a_{1}-1 \text { 个 } 1} 0 \underbrace{11 \cdots 1}_{a_{1}-a_{2}-1 \text { 个 } 1} 0 \cdots \underbrace{11 \cdots 1}_{a_{k-2}-a_{k-1}-1 \text { 个 } 1} 0 \underbrace{11 \cdots 1}_{a_{k-1}-a_{k} \text { 个 } 1} \underbrace{00 \cdots 0}_{a_{k} \text { 个 } 0})_{2},
\end{aligned}
$$

故

$$
\begin{aligned}
& S_{2}\left(2^{A}-2^{a_{1}}-2^{a_{2}}-\cdots-2^{a_{k}}\right) \\
= & \left(A-a_{1}-1\right)+\left(a_{1}-a_{2}-1\right)+\cdots+\left(a_{k-2}-a_{k-1}-1\right)+\left(a_{k-1}-a_{k}\right) \\
= & A-a_{k}-k+1 .
\end{aligned}
$$

特别地, 取 $A=2^{k}-1, a_{j}=2^{k}-2^{j},(j=1,2, \ldots, k)$, 我们得到

$$
S_{2}\left(m_{k}\right)=2^{k}-k
$$

又, 我们计算 $m_{k}^{2}$ 如下:

$$
\begin{aligned}
m_{k}^{2} & =2^{2^{k+1}-2}-\sum_{j=1}^{k} 2^{2^{k+1}-2^{j}}+\left(\sum_{j=1}^{k} 2^{2^{k}-2^{j}}\right)^{2} \\
& =2^{2^{k+1}-2}-\sum_{j=1}^{k} 2^{2^{k+1}-2^{j}}+\sum_{j=1}^{k} 2^{2^{k+1}-2^{j+1}}+\sum_{(i, j): 1 \leq i<j \leq k} 2^{2^{k+1}-2^{i}-2^{j}+1} \\
& =2^{0}+\sum_{(i, j): 1 \leq i<j \leq k} 2^{2^{k+1}-2^{i}-2^{j}+1}
\end{aligned}
$$

注意 $\{0\} \cup\left\{2^{k+1}-2^{i}-2^{j}+1\right\}_{1 \leq i<j \leq k}$ 中的数两两不同, 故

引理证毕.

$$
S_{2}\left(m_{k}^{2}\right)=1+\frac{k(k-1)}{2}
$$

回到原题, 我们分以下几步.

第一步: 先考虑 $\alpha \in[0,1)$ 的情况. 此时记 $\theta=\frac{1+\alpha}{1-\alpha}$, 则 $\theta \geq 1$ 并且 $\frac{\theta-1}{\theta+1}=\alpha$. 我们取

$$
n_{k}=2^{t_{k}} m_{k}-1 \text {, 其中 } t_{k}=\left\lfloor\theta 2^{k}\right\rfloor \text {. }
$$

注意 $m_{k}$ 是奇数. 如果记 $m_{k}$ 的二进制表示为 $m_{k}=\left(\overline{d_{v} d_{v-1} \cdots d_{1} d_{0}}\right)_{2}$, 则个位数 $d_{0}=1$. 我们有

$$
n_{k}=2^{t_{k}} m_{k}-1=(\overline{d_{v} d_{v-1} \cdots d_{1} 0 \underbrace{11 \cdots 1}_{t_{k} \text { 个 } 1}})_{2} \text {, }
$$

所以

$$
S_{2}\left(n_{k}\right)=S_{2}\left(m_{k}\right)-1+t_{k}=\left\lfloor\theta 2^{k}\right\rfloor+2^{k}-k-1 .
$$

而

$$
n_{k}^{2}=2^{2 t_{k}} m_{k}^{2}-2^{t_{k}+1} m_{k}+1=2^{t_{k}+1}\left(2^{t_{k}-1} m_{k}^{2}-m_{k}\right)+1 .
$$

记 $m_{k}^{2}$ 与 $m_{k}$ 的二进制表示分别为 $m_{k}^{2}=\left(\overline{c_{u} c_{u-1} \cdots c_{1} c_{0}}\right)_{2}, m_{k}=\left(\overline{d_{v} d_{v-1} \cdots d_{1} d_{0}}\right)_{2}$.则由 $m_{k}$ 是奇数知 $c_{0}=d_{0}=1$. 记 $d_{j}^{\prime}=1-d_{j}, j=0,1, \ldots, v$. 注意 $m_{k}<2^{2^{k}-1}$, 而 $t_{k} \geq 2^{k}$, 故 $2^{t_{k}-1}>m_{k}$. 所以 $v<t_{k}-1$, 故 $n_{k}^{2}$ 的二进制表示为

$$
n_{k}^{2}=(\overline{c_{u} c_{u-1} \cdots c_{1} 0 \underbrace{11 \cdots 1}_{t_{k}-v-2 \text { 个 } 1} d_{v}^{\prime} d_{v-1}^{\prime} \cdots d_{1}^{\prime}(\underbrace{00 \cdots 0}_{t_{k} \text { 个 } 0} 1})_{2},
$$

我们有

$$
\begin{aligned}
S_{2}\left(n_{k}^{2}\right) & =\left(S_{2}\left(m_{k}^{2}\right)-1\right)+\left(t_{k}-S_{2}\left(m_{k}\right)\right)+1 \\
& =S_{2}\left(m_{k}^{2}\right)-S_{2}\left(m_{k}\right)+t_{k} \\
& =\left\lfloor\theta 2^{k}\right\rfloor-2^{k}+\frac{k(k+1)}{2}+1 .
\end{aligned}
$$

于是

$$
\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=\lim _{k \rightarrow \infty} \frac{\left\lfloor\theta 2^{k}\right\rfloor-2^{k}+\frac{k(k+1)}{2}+1}{\left\lfloor\theta 2^{k}\right\rfloor+2^{k}-k-1}=\frac{\theta-1}{\theta+1}=\alpha .
$$

第二步: 我们来证明如果存在一列正整数 $\left\{n_{k}\right\}_{k \geq 1}$ 使得 $\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=\alpha$ 并且 $\lim _{k \rightarrow \infty} S_{2}\left(n_{k}\right)=+\infty$, 则存在另一列正整数 $\left\{N_{k}\right\}_{k \geq 1}$ 使得 $\lim _{k \rightarrow \infty} \frac{S_{2}\left(N_{k}^{2}\right)}{S_{2}\left(N_{k}\right)}=\alpha+1$ 并且 $\lim _{k \rightarrow \infty} S_{2}\left(N_{k}\right)=+\infty$.

事实上, 取

$$
N_{k}=2^{T_{k}} n_{k}+1 \text {, 其中 } T_{k}=n_{k}+1 \text {. }
$$

则显然 $S_{2}\left(N_{k}\right)=S_{2}\left(n_{k}\right)+1$. (于是从 $\lim _{k \rightarrow \infty} S_{2}\left(n_{k}\right)=+\infty$ 推出 $\lim _{k \rightarrow \infty} S_{2}\left(N_{k}\right)=+\infty$.)而 $N_{k}^{2}=2^{T_{k}+1}\left(2^{T_{k}-1} n_{k}^{2}+n_{k}\right)+1$. 由于 $2^{T_{k}-1}>n_{k}$, 故

$$
S_{2}\left(N_{k}^{2}\right)=S_{2}\left(n_{k}^{2}\right)+S_{2}\left(n_{k}\right)+1 .
$$

所以

$$
\frac{S_{2}\left(N_{k}^{2}\right)}{S_{2}\left(N_{k}\right)}=\frac{S_{2}\left(n_{k}^{2}\right)+S_{2}\left(n_{k}\right)+1}{S_{2}\left(n_{k}\right)+1}=\frac{\frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}+1+\frac{1}{S_{2}\left(n_{k}\right)}}{1+\frac{1}{S_{2}\left(n_{k}\right)}}
$$

利用 $\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=\alpha$ 以及 $\lim _{k \rightarrow \infty} S_{2}\left(n_{k}\right)=+\infty$, 我们便推出

$$
\lim _{k \rightarrow \infty} \frac{S_{2}\left(N_{k}^{2}\right)}{S_{2}\left(N_{k}\right)}=\frac{\alpha+1+0}{1+0}=\alpha+1
$$

由前两步的结论, 我们固定 $\alpha$ 的小数部分, 对 $\alpha$ 的整数部分进行归纳, 便
可证明对任何 $\alpha \in[0,+\infty)$, 存在一列正整数 $\left\{n_{k}\right\}_{k \geq 1}$ 使得 $\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=\alpha$ 并且 $\lim _{k \rightarrow \infty} S_{2}\left(n_{k}\right)=+\infty$.

最后, 对于 $\alpha=+\infty$, 我们取 $n_{k}=\sum_{j=1}^{k} 2^{2^{j}}$. 则

$$
n_{k}^{2}=\sum_{j=1}^{k} 2^{2^{j+1}}+\sum_{(i, j): 1 \leq i<j \leq k} 2^{2^{i}+2^{j}+1}
$$

于是 $S_{2}\left(n_{k}\right)=k, S_{2}\left(n_{k}^{2}\right)=\frac{k(k+1)}{2}$, 所以 $\lim _{k \rightarrow \infty} \frac{S_{2}\left(n_{k}^{2}\right)}{S_{2}\left(n_{k}\right)}=+\infty$. 至此 (1) 小问全部得证.

(2) (翁斌) 我们证明以下更强的结论:

(i) 对任何正整数 $n$, 我们有

$$
\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)} \geq \frac{1}{\log _{2}(n+1)}
$$

(ii) 存在常数 $C>0$, 使得存在无穷多个正整数 $n$, 满足

$$
\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)} \leq \frac{C}{\log _{2} n}
$$

事实上, 由于 $n$ 的二进制表示中有 $S_{2}(n)$ 个数字是 1 , 故

$$
n \geq 2^{0}+2^{1}+\cdots+2^{S_{2}(n)-1}=2^{S_{2}(n)}-1,
$$

即 $S_{2}(n) \leq \log _{2}(n+1)$. 又 $S_{2}\left(n^{2}\right) \geq 1$, 故 $\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)} \geq \frac{1}{\log _{2}(n+1)}$. (i) 得证.

对于 (ii), 我们考虑以下多项式

$$
f(x)=2 x^{4}+2 x^{3}-x^{2}+2 x+2,
$$

直接计算得

$$
f(x)^{2}=4 x^{8}+8 x^{7}+4 x^{5}+17 x^{4}+4 x^{3}+8 x+4
$$

这里的关键性质是 $f(x)^{2}$ 的系数均是非负整数. 取 $n=f\left(2^{k}\right)$, 其中正整数 $k$ 充分大, 则我们有

$$
S_{2}(n)=k+4, \quad S_{2}\left(n^{2}\right)=8, \quad \log _{2}(n)<4 k+2
$$

于是我们有

$$
\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)}=\frac{8}{k+4}<\frac{32}{\log _{2}(n)}
$$

形如 $n=f\left(2^{k}\right), k$ 充分大的正整数 $n$ 显然有无穷多个, 故 (ii) 得证. 至此 (2) 小问得证.

(用 (2) 小问中的构造, 我们也可以简化 (1) 小问的证明.)

评注 2015 年, Saunders [7] 证明了对任何正有理数 $\alpha$, 存在正整数 $n$ 使得 $\frac{S_{2}\left(n^{2}\right)}{S_{2}(n)}=\alpha$.
题 8 设 $p$ 是一个奇素数. 我们定义 Fekete 多项式

$$
f_{p}(z)=\sum_{a=0}^{p-1}\left(\frac{a}{p}\right) z^{a}
$$

这里 $\left(\frac{a}{p}\right)$ 是 Legendre 符号. 求证: $f_{p}(z)$ 至少有 $\frac{p-1}{2}$ 个根在单位圆周上.

## 题目来源 $[3]$.

证明 首先我们注意到, 对任何 $k \in\{1,2, \ldots, p-1\}$, 我们有

$$
f_{p}\left(e^{2 \pi i k / p}\right)=\sum_{a=0}^{p-1}\left(\frac{a}{p}\right) e^{2 \pi i k a / p}
$$

当 $a$ 跑遍模 $p$ 的一个完全剩余系时, $k a$ 也跑遍模 $p$ 的一个完全剩余系. 作换元 $b=k a$, 则我们得到

$$
\begin{aligned}
f_{p}\left(e^{2 \pi i k / p}\right) & =\left(\frac{k}{p}\right) \sum_{a=0}^{p-1}\left(\frac{a k}{p}\right) e^{2 \pi i k a / p} \\
& =\left(\frac{k}{p}\right) \sum_{b=0}^{p-1}\left(\frac{b}{p}\right) e^{2 \pi i b / p} \\
& =\left(\frac{k}{p}\right) f_{p}\left(e^{2 \pi i / p}\right),
\end{aligned}
$$

即

$$
f_{p}\left(e^{2 \pi i k / p}\right)=\left(\frac{k}{p}\right) f_{p}\left(e^{2 \pi i / p}\right), \quad k=1,2, \ldots, p-1 .
$$

对任何实数 $\theta$, 我们定义

$$
g(\theta)=e^{-p \pi i \theta} f_{p}\left(e^{2 \pi i \theta}\right) .
$$

利用首尾配对, 我们计算得

$$
\begin{aligned}
g(\theta) & =\sum_{a=1}^{\frac{p-1}{2}}\left(\left(\frac{a}{p}\right) e^{2 \pi i(a-p / 2) \theta}+\left(\frac{-a}{p}\right) e^{2 \pi i(p / 2-a) \theta}\right) \\
& = \begin{cases}2 \sum_{a=1}^{\frac{p-1}{2}}\left(\frac{a}{p}\right) \cos ((2 a-p) \pi \theta), & \text { 当素数 } p \equiv 1 \quad(\bmod 4), \\
2 i \sum_{a=1}^{\frac{p-1}{2}}\left(\frac{a}{p}\right) \sin ((2 a-p) \pi \theta), & \text { 当素数 } p \equiv 3 \quad(\bmod 4) .\end{cases}
\end{aligned}
$$

定义

$$
\widetilde{g}(\theta)=\left\{\begin{array}{lll}
g(\theta), & \text { 当素数 } p \equiv 1 \quad(\bmod 4), \\
i g(\theta), & \text { 当素数 } p \equiv 3 \quad(\bmod 4),
\end{array}\right.
$$

则 $\widetilde{g}(\theta)$ 是实数. 于是函数 $\widetilde{g}: \mathbb{R} \rightarrow \mathbb{R}$ 是一个实值连续函数.

由 (13) 我们有 $g\left(\frac{k}{p}\right)=(-1)^{k-1}\left(\frac{k}{p}\right) g\left(\frac{1}{p}\right), k=1,2, \ldots, p-1$. 于是当 $k \in$
$\{1,2, \ldots, k-2\}$ 且 $\left(\frac{k}{p}\right)=\left(\frac{k+1}{p}\right)$ 时我们有

$$
\widetilde{g}\left(\frac{k+1}{p}\right)=-\widetilde{g}\left(\frac{k}{p}\right)
$$

由实值连续函数的介值定理, 此时 $\widetilde{g}$ 在区间 $\left[\frac{k}{p}, \frac{k+1}{p}\right)$ 上有一个零点. 故此时 $f_{p}$ 在单位圆周上从 $e^{2 \pi i k / p}$ (含)到 $e^{2 \pi i(k+1) / p}$ (不含)的劣弧上有一个根. 又注意到 $z=1$是 $f_{p}(z)$ 的一个根, 于是 $f_{p}(z)$ 在单位圆周上的根的个数 (不计重数)

$$
\begin{aligned}
& \geq 1+\#\left\{k \in\{1,2, \ldots, p-2\} \left\lvert\,\left(\frac{k}{p}\right)=\left(\frac{k+1}{p}\right)\right.\right\} \\
& =1+\sum_{k=1}^{p-2} \frac{\left(\frac{k}{p}\right)\left(\frac{k+1}{p}\right)+1}{2} \\
& =\frac{p}{2}+\frac{1}{2} \sum_{k=1}^{p-2}\left(\frac{k}{p}\right)\left(\frac{k+1}{p}\right) \\
& =\frac{p}{2}+\frac{1}{2} \sum_{k=1}^{p-2}\left(\frac{k^{-1}}{p}\right)\left(\frac{k+1}{p}\right) \\
& =\frac{p}{2}+\frac{1}{2} \sum_{k=1}^{p-2}\left(\frac{1+k^{-1}}{p}\right) .
\end{aligned}
$$

注意到当 $k$ 跑遍模 $p$ 的一个既约剩余系时, 数论逆 $k^{-1}(\bmod p)$ 也跑遍模 $p$ 的一个既约剩余系. 而当 $k \equiv-1(\bmod p)$ 时 $k^{-1} \equiv-1(\bmod p)$. 所以当 $k$ 跑遍 $1,2, \ldots, p-2$ 时, $k^{-1}(\bmod p)$ 也跑遍 $1,2, \ldots, p-2(\bmod p)$. 于是

$$
\sum_{k=1}^{p-2}\left(\frac{1+k^{-1}}{p}\right)=\sum_{a=2}^{p-1}\left(\frac{a}{p}\right)=-1
$$

代入 (14), 我们便证明了 $f_{p}(z)$ 在单位圆周上至少有 $\frac{p-1}{2}$ 个不同的根.

评注 2000 年, Conrey, Granville, Poonen, and Soundararajan [3] 证明了 $\lim _{p \rightarrow \infty} \frac{N(p)}{p}=c_{0}$ 存在, 这里 $N(p)$ 是 $f_{p}(z)$ 在单位圆周上的根的个数 (计重数), 并且 $0.500668<c_{0}<0.500813$.

题 9 (Erdös and Pomerance) 求证: 对任何正整数 $m, n$, 区间 $\left[m, m+10 n^{\frac{3}{2}}\right]$中存在 $n$ 个两两不同的正整数 $a_{1}, a_{2}, \ldots, a_{n}$ 使得 $k \mid a_{k}, k=1,2, \ldots, n$.

题目来源 $[4$, Theorem 4].

证明 我们将使用 Hall 定理: 设 $G=\left(V_{1}, V_{2}\right)$ 是一个二部图. 则存在 $V_{1}$ 到 $V_{2}$的完全匹配当且仅当对于 $V_{1}$ 的任何一个子集 $S$, 有 $|N(S)| \geq|S|$, 其中 $N(S)$ 是 $S$的邻域.

一个推论是: 如果存在常数 $C$ 使得 $d\left(v_{1}\right) \geq C \geq d\left(v_{2}\right)$ 对任何 $v_{1} \in V_{1}$ 与任何
$v_{2} \in V_{2}$ 成立, 则存在 $V_{1}$ 到 $V_{2}$ 的完全匹配.

我们将证明以下的命题:

命题 对任何正整数 $m, n$, 区间 $(m, m+4 n\lfloor\sqrt{n}\rfloor+n\rfloor$ 中存在 $n$ 个两两不同的正整数 $a_{1}, a_{2}, \ldots, a_{n}$ 使得 $k \mid a_{k},(k=1,2, \ldots, n)$.

把区间 $(m, m+4 n\lfloor\sqrt{n}\rfloor$ 划分成 $4\lfloor\sqrt{n}\rfloor$ 个长度为 $n$ 的小区间: $(m+(s-1) n$, $m+s n\rfloor, s=1,2, \ldots, 4\lfloor\sqrt{n}\rfloor$. 对任何整数 $j$, 我们用 $\langle j\rangle$ 表示 $j$ 所在的小区间. 根据抽庹原理, 对任何 $k \in\{1,2, \ldots, n\}$, 每个小区间中均存在 $k$ 的倍数.

考虑二部图 $G_{0}=\left(I_{0}, J_{0}\right)$, 其中 $I_{0}=\{1,2, \ldots, n\}, J_{0}=(m, m+4 n\lfloor\sqrt{n}\rfloor] \cap \mathbb{Z}$.对于 $i \in I_{0}, j \in J_{0}$, 顶点 $i$ 与 $j$ 相连当且仅当 $i \mid j$. 则 $I_{0}$ 中每个顶点的度数均 $\geq 4\lfloor\sqrt{n}\rfloor$.

如果 $J_{0}$ 中每个顶点的度数均 $\leq\lfloor\sqrt{n}\rfloor$, 则由 Hall 定理, 二部图 $G_{0}$ 中存在 $I_{0}$ 到 $J_{0}$ 的完全匹配, 命题得证. 剩下的情况是: 存在 $j_{1} \in J_{0}$ 使得度数 $d_{G_{0}}\left(j_{1}\right)>\sqrt{n}$.则存在 $I_{0}$ 的子集 $K_{1}$, 满足 $\left|K_{1}\right|>\sqrt{n}$, 并且对任何 $k \in K_{1}$ 有 $k \mid j_{1}$. 此时我们取 $a_{k}=j_{1}+k,\left(k \in K_{1}\right)$, 则有 $k \mid a_{k}, a_{k} \in\left\langle j_{1}\right\rangle \cup\left\langle j_{1}+n\right\rangle$, 并且 $a_{k}\left(k \in K_{1}\right)$ 两两不同.

记 $I_{1}=I_{0} \backslash K_{1}$, 记 $J_{1}=J_{0} \backslash\left(\left\langle j_{1}-n\right\rangle \cup\left\langle j_{1}\right\rangle \cup\left\langle j_{1}+n\right\rangle\right)$. 考虑二部图 $G_{1}=\left(I_{1}, J_{1}\right)$.则 $I_{1}$ 中每个顶点的度数(在二部图 $G_{1}$ 中的度数)均 $\geq 4\lfloor\sqrt{n}\rfloor-3 \geq\lfloor\sqrt{n}\rfloor$.

如果 $J_{1}$ 中每个顶点的度数均 $\leq\lfloor\sqrt{n}\rfloor$, 则由 Hall 定理, 二部图 $G_{1}$ 中存在 $I_{1}$ 到 $J_{1}$ 的完全匹配, 命题得证. 剩下的情况是: 存在 $j_{2} \in J_{1}$ 使得度数 $d_{G_{1}}\left(j_{2}\right)>\sqrt{n}$.则存在 $I_{1}$ 的子集 $K_{2}$, 满足 $\left|K_{2}\right|>\sqrt{n}$, 并且对任何 $k \in K_{2}$ 有 $k \mid j_{2}$. 此时我们取 $a_{k}=j_{2}+k,\left(k \in K_{2}\right)$, 则有 $k \mid a_{k}, a_{k} \in\left\langle j_{2}\right\rangle \cup\left\langle j_{2}+n\right\rangle$, 并且 $a_{k}\left(k \in K_{1} \cup K_{2}\right)$ 两两不同.

注意

$$
n=\left|I_{0}\right| \geq\left|K_{1} \cup K_{2}\right|>2 \sqrt{n}
$$

故 $\sqrt{n}>2$. 记 $I_{2}=I_{1} \backslash K_{2}$, 记 $J_{2}=J_{1} \backslash\left(\left\langle j_{2}-n\right\rangle \cup\left\langle j_{2}\right\rangle \cup\left\langle j_{2}+n\right\rangle\right)$. 我们再考虑二部图 $G_{2}=\left(I_{2}, J_{2}\right)$. 则 $I_{2}$ 中每个顶点的度数(在二部图 $G_{2}$ 中的度数)均 $\geq 4\lfloor\sqrt{n}\rfloor-6 \geq\lfloor\sqrt{n}\rfloor$.

如果 $J_{2}$ 中每个顶点的度数均 $\leq\lfloor\sqrt{n}\rfloor$, 则由 Hall 定理, 二部图 $G_{2}$ 中存在 $I_{2}$ 到 $J_{2}$ 的完全匹配, 命题得证. 剩下的情况是: 存在 $j_{3} \in J_{2}$ 使得度数 $d_{G_{2}}\left(j_{3}\right)>\sqrt{n}$.则存在 $I_{2}$ 的子集 $K_{3}$, 满足 $\left|K_{3}\right|>\sqrt{n}$, 并且对任何 $k \in K_{3}$ 有 $k \mid j_{3}$. 此时我们取 $a_{k}=j_{3}+k,\left(k \in K_{3}\right)$, 则有 $k \mid a_{k}, a_{k} \in\left\langle j_{3}\right\rangle \cup\left\langle j_{3}+n\right\rangle$, 并且 $a_{k}\left(k \in K_{1} \cup K_{2} \cup K_{3}\right)$两两不同.

一般地, 设 $t$ 是一个正整数. 假设上述方式进行 $t$ 步之后仍未证明命题, 则我
们逐步得到了 $j_{1}, j_{2}, \ldots, j_{t}, K_{1}, K_{2}, \ldots, K_{t}, a_{k}\left(k \in K_{1} \cup K_{2} \cup \cdots \cup K_{t}\right)$. 它们满足: $K_{1}, K_{2}, \ldots, K_{t}$ 是 $I_{0}$ 的两两不交的子集, $\left|K_{s}\right|>\sqrt{n},(s=1,2, \ldots, t), k \mid a_{k}$, $a_{k} \in\left\langle j_{1}\right\rangle \cup\left\langle j_{1}+n\right\rangle \cup \cdots \cup\left\langle j_{t}\right\rangle \cup\left\langle j_{t}+n\right\rangle,\left(k \in K_{1} \cup \cdots \cup K_{t}\right)$. 则

$$
n=\left|I_{0}\right| \geq\left|K_{1} \cup \cdots \cup K_{t}\right|>t \sqrt{n}
$$

故 $t \leq\lfloor\sqrt{n}\rfloor$. 记 $I_{t}=I_{0} \backslash\left(K_{1} \cup K_{2} \cdots \cup K_{t}\right)$, 记

$$
J_{t}=J_{0} \backslash\left(\left\langle j_{1}-n\right\rangle \cup\left\langle j_{1}\right\rangle \cup\left\langle j_{1}+n\right\rangle \cup \cdots \cup\left\langle j_{t}-n\right\rangle \cup\left\langle j_{t}\right\rangle \cup\left\langle j_{t}+n\right\rangle\right)
$$

考虑二部图 $G_{t}=\left(I_{t}, J_{t}\right)$, 则 $I_{t}$ 中每个顶点在二部图 $G_{t}$ 中的度数均 $\geq 4\lfloor\sqrt{n}\rfloor-3 t \geq$ $\lfloor\sqrt{n}\rfloor$. 如果 $J_{t}$ 中每个顶点的度数 $\leq\lfloor\sqrt{n}\rfloor$, 则由 Hall 定理, 二部图 $G_{t}$ 中存在 $I_{t}$ 到 $J_{t}$ 的完全匹配, 命题成立. 剩下的情况: 存在 $j_{t+1} \in J_{t}$ 使得度数 $d_{G_{t}}\left(j_{t+1}\right)>\sqrt{n}$.则存在 $I_{t}$ 的子集 $K_{t+1}$, 满足 $\left|K_{t+1}\right|>\sqrt{n}$, 并且对任何 $k \in K_{t+1}$ 有 $k \mid j_{t+1}$. 此时我们取 $a_{k}=j_{t+1}+k,\left(k \in K_{t+1}\right)$, 则 $k \mid a_{k}, a_{k} \in\left\langle j_{t+1}\right\rangle \cup\left\langle j_{t+1}+n\right\rangle$.

上述过程有限步必终止(因为 $t \leq\lfloor\sqrt{n}\rfloor$ ), 而终止的方式只能是在某步时二部图 $G_{t}=\left(I_{t}, J_{t}\right)$ 存在 $I_{t}$ 到 $J_{t}$ 的完全匹配, 按此匹配定义 $a_{k}\left(k \in I_{t}\right)$, 结合之前定义好的 $a_{k}\left(k \in K_{1} \cup K_{2} \cup \cdots \cup K_{t}\right)$, 便证明了命题.

## 参考文献

[1] Tewodros Amdeberhan, Victor H. Moll, Vaishavi Sharma, and Diego Villamizar, Arithmetic properties of the sum of divisors. J. Number Theory 223 (2021), 325-349.

[2] David W. Boyd, On a problem of Byrnes concerning polynomials with restricted coefficients. Math. Comp. 66 (1997), 1697-1703.

[3] John B. Conrey, Andrew J. Granville, Bjorn Poonen, and Kannan Soundararajan, Zeros of Fekete polynomials. Ann. Inst. Fourier (Grenoble) 50 (2000), no.3, $865-889$.

[4] Paul Erdös and Carl Pomerance, Matching the natural numbers up to $n$ with distinct multiples in another interval. Nederl. Akad. Wetensch. Proc. Ser. A 83 (1980), 147-161.

[5] Dominik J. Leitner, Two exponential diophantine equations. Journal de Théorie des Nombres de Bordeaux 23 (2011), 479-487.

[6] Frank Morley, Note on the congruence $2^{4 n} \equiv(-1)^{n} \frac{(2 n) !}{(n !)^{2}}$, where $2 n+1$ is a prime. Ann. of Math. 9 (1894/95), no. 1-6, 168-170.

[7] John C. Saunders, Sums of digits in q-ary expansions. Int. J. Number Theory 11 (2015), no. 2, 593-611.

[8] Kenneth B. Stolarsky, The binary digits of a power. Proc. Amer. Math. Soc. 71 (1978), no. 1, 1-5.


[^0]:    修订日期: 2023-08-15.

