# 第四十二期问题征解解答与点评 

张端阳

第一题 求所有的整数 $n \geq 2$, 使得可以将 $\{1,2, \cdots, n\}$ 的所有置换编号为 $\sigma_{1}, \sigma_{2}, \cdots, \sigma_{n !}$ ，满足对任意 $j(1 \leq j \leq n !)$ ，均有

$$
\sigma_{j}(k) \neq \sigma_{j+1}(k), \quad \forall k \in\{1,2, \cdots, n\}
$$

其中 $\sigma_{n !+1}=\sigma_{1}$.

(上海大学 冷岗松 供题)

解 (根据清华大学王一川同学的解答整理):

易知 $n=2$ 满足要求, $n=3$ 不满足要求. 下面证明 $n \geq 4$ 均满足要求.

称 $\left(p_{1}, p_{2}, \cdots, p_{n}\right)$ 与 $\left(q_{1}, q_{2}, \cdots, q_{n}\right)$ 是 $1,2, \cdots, n$ 的 “错位置换”, 如果对任意 $1 \leq k \leq n$ 都有 $p_{k} \neq q_{k}$.

作简单图 $G, G$ 的顶点是 $1,2, \cdots, n$ 的所有置换, 在错位置换之间连边. 本题即证 $G$ 中有哈密顿圈.

注意到 $G$ 中有 $(n-1)$ ! 个 $n-$ 团:

$$
G(\varphi)=\{(x, x+\varphi(1), \cdots, x+\varphi(n-1)) \mid x=1,2, \cdots, n\},
$$

这里 $\varphi$ 取遍 $1,2, \cdots, n-1$ 的所有置换.

熟知 $1,2, \cdots, n-1$ 的每个置换恰有

$$
(n-1) !\left(\frac{1}{2 !}-\frac{1}{3 !}+\cdots+\frac{(-1)^{n-1}}{(n-1) !}\right)<\frac{(n-1) !}{2}
$$

个错位置换. 由 Dirac 定理, 可将 $1,2, \cdots, n-1$ 的所有置换排成一圈 $\varphi_{1}, \varphi_{2}, \cdots$, $\varphi_{(n-1) !}$, 使得任意相邻两个不是错位置换.

对 $1 \leq i \leq(n-1)$ !, 因为 $\varphi_{i}$ 与 $\varphi_{i+1}$ 不是错位置换 $\left(\varphi_{(n-1) !+1}=\varphi_{1}\right)$, 所以存在 $1 \leq k \leq n-1$ 使 $\varphi_{i}(k)=\varphi_{i+1}(k)$. 这样, 对任意 $1 \leq x \leq n$, 存在 $1 \leq y \leq n$, 使得

$$
x-y \not \equiv 0, \varphi_{i}(1)-\varphi_{i+1}(1), \cdots, \varphi_{i}(n-1)-\varphi_{i+1}(n-1) \quad(\bmod n),
$$

此时 $\left(x, x+\varphi_{i}(1), \cdots, x+\varphi_{i}(n-1)\right)$ 与 $\left(y, y+\varphi_{i+1}(1), \cdots, y+\varphi_{i+1}(n-1)\right)$ 连边.
从而 $G\left(\varphi_{i}\right)$ 与 $G\left(\varphi_{i+1}\right)$ 之间有 $n$ 条边构成匹配.

现在, 可依次选取边 $e_{1}, e_{2}, \cdots, e_{(n-1) !}$ ! 使得它们两两无公共顶点且 $e_{i}$ 连结 $G\left(\varphi_{i}\right)$ 与 $G\left(\varphi_{i+1}\right)$. 因为 $G\left(\varphi_{1}\right), G\left(\varphi_{2}\right), \cdots, G\left(\varphi_{(n-1) !}\right)$ 都是 $n-$ 团, 所以由此便能得到 $G$ 的一个哈密顿圈.

综上, 所求为所有大于 1 且不等于 3 的整数.

评注 新星征解第七期第四题和第 32 届冬令营第四题也是有关全体排列的结构的问题.

第二题 设 $\triangle A B C$ 的内心为 $I$, 内切圆 $\odot I$ 与 $B C, C A, A B$ 分别切于点 $D, E, F$.设 $L$ 是 $\triangle D E F$ 的垂心, $H$ 是 $\triangle A B C$ 的垂心, $A H$ 与 $B C$ 交于点 $U, M$ 为 $A U$ 的中点, $M L$ 与 $A I$ 交于点 $X$. 证明: $I, X, H, U$ 四点共圆.

(华南师大附中学生 戴子一 复旦大学学生 张泽豪 供题)

## 证明 (根据清华大学严君啸同学的解答整理):



只需证明 $A I \cdot A X=A H \cdot A U$.

延长 $A I, M D$ 交于点 $I_{A}$, 熟知 $I_{A}$ 是 $\triangle A B C$ 角 $A$ 内的旁心.

易知

$$
A H \cdot A U=A B \cdot A C \cdot \cos A=A I \cdot A I_{A} \cdot \cos A
$$

于是只需证明

$$
A X=A I_{A} \cdot \cos A
$$

事实上, 因为 $L D / / X I_{A}, I D / / A M$, 所以

$$
X I_{A}=L D \cdot \frac{M I_{A}}{M D}=L D \cdot \frac{A I_{A}}{A I}
$$

设 $K$ 是 $E F$ 的中点, 则

$$
L D=2 I K=2 A I \sin ^{2} \frac{A}{2}
$$

于是

$$
\frac{X I_{A}}{A I_{A}}=\frac{L D}{A I}=2 \sin ^{2} \frac{A}{2}
$$

故

$$
\frac{A X}{A I_{A}}=1-\frac{X I_{A}}{A I_{A}}=1-2 \sin ^{2} \frac{A}{2}=\cos A
$$

综上, 命题得证.

评注 (1). 供题者指出, 若设 $B H$ 与 $A C$ 交于点 $V, C H$ 与 $A B$ 交于点 $W$, 则 $X$ 是 $\triangle A V W$ 角 $A$ 内的旁心.

(2). 东北育才学校朱家庆, 青岛二中高林凯, 深圳中学吴家睿, 长郡中学杨谨瑜等同学也给出了本题的正确解答.

第三题 设 $a_{1}, a_{2}, \cdots, a_{2021}$ 是非负实数, 满足 $a_{1}+a_{2}+\cdots+a_{2021}=1$. 求

$$
\sum_{i=1}^{2021} \min \left\{a_{i}, a_{i+1}\right\} \cdot \min \left\{a_{i+1}, a_{i+2}\right\}
$$

的最大值, 其中 $a_{2022}=a_{1}, a_{2023}=a_{2}$.

(温州育英国际实验学校学生 林逸沿 供题)

## 解 (根据北京大学黄嘉俊同学的解答整理):

将 2021 换为一般的整数 $n \geq 3$, 并记

$$
S=\sum_{i=1}^{n} \min \left\{a_{i}, a_{i+1}\right\} \cdot \min \left\{a_{i+1}, a_{i+2}\right\}
$$

我们证明

$$
S_{\max }= \begin{cases}\frac{1}{8}, & n \geq 8 \\ \frac{1}{n}, & 3 \leq n \leq 7\end{cases}
$$

一方面, 当 $3 \leq n \leq 7$ 时, 取 $a_{1}=a_{2}=\cdots=a_{n}=\frac{1}{n}$, 则 $S=\frac{1}{n}$.

当 $n \geq 8$ 时, 取 $a_{1}=\alpha, a_{2}=a_{3}=a_{4}=\frac{1}{4}, a_{5}=\beta, a_{6}=\cdots=a_{n}=0$, 其中 $\alpha, \beta$是和为 $\frac{1}{4}$ 的非负实数, 则

$$
S=\frac{\alpha}{4}+\frac{1}{16}+\frac{\beta}{4}=\frac{1}{8} .
$$

另一方面, 记 $b_{i}=\min \left\{a_{i}, a_{i+1}\right\}$, 下面证明

$$
\sum_{i=1}^{n} b_{i} b_{i+1} \leq \begin{cases}\frac{1}{8}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}, & n \geq 8 \\ \frac{1}{n}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}, & 3 \leq n \leq 7\end{cases}
$$

先证明对任意 $n \geq 3$,

$$
\sum_{i=1}^{n-2} b_{i} b_{i+1} \leq \frac{1}{8}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}
$$

当 $n=5$ 时, 由对称性, 不妨设 $b_{2} \leq b_{3}$. 则

$$
\begin{aligned}
b_{1} b_{2}+b_{2} b_{3}+b_{3} b_{4} & \leq\left(b_{1}+b_{2}+b_{4}\right) b_{3} \\
& \leq \frac{1}{8}\left(b_{1}+b_{2}+b_{4}+2 b_{3}\right)^{2} \\
& \leq \frac{1}{8}\left(a_{1}+a_{2}+a_{5}+a_{3}+a_{4}\right)^{2}
\end{aligned}
$$

当 $n=4$ 时, 对 $a_{1}, a_{2}, a_{3}, a_{4}, 0$ 应用 5 个数的情形即可.

当 $n=3$ 时, 对 $a_{1}, a_{2}, a_{3}, 0,0$ 应用 5 个数的情形即可.

下面对 $n$ 归纳. 假设 $n \geq 6$ 且 $3 \sim n-1$ 时结论成立, 来看 $n$ 时的情形.

记

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\frac{1}{8}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}-\sum_{i=1}^{n-2} b_{i} b_{i+1}
$$

设 $d=\min \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 我们希望将一个 $a_{i}$ 调整至 0 , 即证

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq f\left(a_{1}-d, a_{2}-d, \cdots, a_{n}-d\right)
$$

记 $a_{i}^{\prime}=a_{i}-d, b_{i}^{\prime}=b_{i}-d$, 则 $a_{i}^{\prime} \geq 0, b_{i}^{\prime}=\min \left\{a_{i}^{\prime}, a_{i+1}^{\prime}\right\}$, 且

$$
\begin{aligned}
f\left(a_{1}, a_{2}, \cdots, a_{n}\right)= & \frac{1}{8}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}+n d\right)^{2}-\sum_{i=1}^{n-2}\left(b_{i}^{\prime}+d\right)\left(b_{i+1}^{\prime}+d\right) \\
= & \frac{1}{8}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right)^{2}+\frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right) d+\frac{n^{2}}{8} d^{2} \\
& -\sum_{i=1}^{n-2} b_{i}^{\prime} b_{i+1}^{\prime}-\left(b_{1}^{\prime}+2 \sum_{i=2}^{n-2} b_{i}^{\prime}+b_{n-1}^{\prime}\right) d-(n-2) d^{2} \\
f\left(a_{1}-d, a_{2}-\right. & \left.d, \cdots, a_{n}-d\right)=\frac{1}{8}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right)^{2}-\sum_{i=1}^{n-2} b_{i}^{\prime} b_{i+1}^{\prime}
\end{aligned}
$$

于是只需证明

$$
\frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right) d+\left(\frac{n^{2}}{8}-n+2\right) d^{2} \geq\left(b_{1}^{\prime}+2 \sum_{i=2}^{n-2} b_{i}^{\prime}+b_{n-1}^{\prime}\right) d
$$

因为 $\frac{n^{2}}{8}-n+2 \geq 0, d \geq 0$, 所以只需证明

$$
\frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right) \geq b_{1}^{\prime}+2 \sum_{i=2}^{n-2} b_{i}^{\prime}+b_{n-1}^{\prime} .
$$

当 $n=6$ 时,

$$
\begin{aligned}
b_{1}^{\prime}+2 b_{2}^{\prime}+2 b_{3}^{\prime}+2 b_{4}^{\prime}+b_{5}^{\prime} & \leq a_{1}^{\prime}+2 \cdot \frac{3 a_{2}^{\prime}+a_{3}^{\prime}}{4}+2 \cdot \frac{a_{3}^{\prime}+a_{4}^{\prime}}{2}+2 \cdot \frac{a_{4}^{\prime}+3 a_{5}^{\prime}}{4}+a_{6}^{\prime} \\
& \leq \frac{3}{2}\left(a_{1}^{\prime}+a_{2}^{\prime}+a_{3}^{\prime}+a_{4}^{\prime}+a_{5}^{\prime}+a_{6}^{\prime}\right) .
\end{aligned}
$$

当 $n=7$ 时,

$$
\begin{aligned}
& b_{1}^{\prime}+2 b_{2}^{\prime}+2 b_{3}^{\prime}+2 b_{4}^{\prime}+2 b_{5}^{\prime}+b_{6}^{\prime} \\
\leq & a_{1}^{\prime}+2 \cdot \frac{7 a_{2}^{\prime}+a_{3}^{\prime}}{8}+2 \cdot \frac{9 a_{3}^{\prime}+7 a_{4}^{\prime}}{16}+2 \cdot \frac{7 a_{4}^{\prime}+9 a_{5}^{\prime}}{16}+2 \cdot \frac{a_{5}^{\prime}+7 a_{6}^{\prime}}{8}+a_{7}^{\prime} \\
\leq & \frac{7}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+a_{3}^{\prime}+a_{4}^{\prime}+a_{5}^{\prime}+a_{6}^{\prime}+a_{7}^{\prime}\right) .
\end{aligned}
$$

当 $n \geq 8$ 时,

$$
b_{1}^{\prime}+2 \sum_{i=2}^{n-2} b_{i}^{\prime}+b_{n-1}^{\prime} \leq a_{1}^{\prime}+2 \sum_{i=2}^{n-2} a_{i}^{\prime}+a_{n-1}^{\prime} \leq \frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right)
$$

从而我们可以设 $a_{i}$ 中有一个为 0 .

(1) 当 $a_{1}=0$ (或 $\left.a_{n}=0\right)$ 时, 对 $a_{2}, a_{3}, \cdots, a_{n}$ 用归纳假设得,

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\frac{1}{8}\left(a_{2}+\cdots+a_{n}\right)^{2}-\sum_{i=2}^{n-2} b_{i} b_{i+1} \geq 0 .
$$

(2) 当 $a_{2}=0$ (或 $\left.a_{n-1}=0\right)$ 时, 对 $a_{3}, a_{4}, \cdots, a_{n}$ 用归纳假设得,

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq \frac{1}{8}\left(a_{3}+\cdots+a_{n}\right)^{2}-\sum_{i=3}^{n-2} b_{i} b_{i+1} \geq 0 .
$$

(3) 当 $a_{3}=0\left(\right.$ 或 $\left.a_{n-2}=0\right)$ 时, 对 $a_{4}, \cdots, a_{n}$ 用归纳假设得,

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq \frac{1}{8}\left(a_{4}+\cdots+a_{n}\right)^{2}-\sum_{i=4}^{n-2} b_{i} b_{i+1} \geq 0
$$

(4) 当 $a_{i}=0(4 \leq i \leq n-3)$ 时, 分别对 $a_{1}, a_{2}, \cdots, a_{i-1}$ 与 $a_{i+1}, a_{i+2}, \cdots, a_{n}$ 用归纳假设得,

$$
\begin{aligned}
& f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \\
= & \frac{1}{8}\left(a_{1}+\cdots+a_{i-1}+a_{i+1}+\cdots+a_{n}\right)^{2}-\sum_{j=1}^{i-3} b_{j} b_{j+1}-\sum_{j=i+1}^{n-2} b_{j} b_{j+1} \\
\geq & \frac{1}{8}\left(a_{1}+\cdots+a_{i-1}\right)^{2}+\frac{1}{8}\left(a_{i+1}+\cdots+a_{n}\right)^{2}-\sum_{j=1}^{i-3} b_{j} b_{j+1}-\sum_{j=i+1}^{n-2} b_{j} b_{j+1} \\
\geq & 0 .
\end{aligned}
$$

(*) 归纳得证.

回到原题.

(1) 当 $n \geq 8$ 时, 记

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\frac{1}{8}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}-\sum_{i=1}^{n} b_{i} b_{i+1}
$$

设 $d=\max \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 我们仍希望将一个 $a_{i}$ 调至 0 .

记 $a_{i}^{\prime}=a_{i}-d, b_{i}^{\prime}=b_{i}-d$, 则

$$
\begin{aligned}
& f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq f\left(a_{1}-d, a_{2}-d, \cdots, a_{n}-d\right) \\
\Longleftrightarrow & \frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right) d+\left(\frac{n^{2}}{8}-n\right) d^{2} \geq 2 \sum_{i=1}^{n} b_{i}^{\prime} d \\
\Longleftarrow & \frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right) \geq 2 \sum_{i=1}^{n} b_{i}^{\prime} .
\end{aligned}
$$

因为

$$
2 \sum_{i=1}^{n} b_{i}^{\prime} \leq 2\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right) \leq \frac{n}{4}\left(a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{n}^{\prime}\right)
$$

所以成立.

从而我们可以设 $a_{i}$ 中有一个为 0 . 由对称性, 不妨设 $a_{n}=0$. 对 $a_{1}, a_{2}, \cdots, a_{n-1}$用 $(*)$ 得,

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\frac{1}{8}\left(a_{1}+a_{2}+\cdots+a_{n-1}\right)^{2}-\sum_{i=1}^{n-3} b_{i} b_{i+1} \geq 0
$$

(2) 当 $3 \leq n \leq 7$ 时, 不妨设 $a_{n}$ 最小. 对 $a_{1}, \cdots, a_{n-1}, a_{n}, \underbrace{a_{n}, \cdots, a_{n}}_{8-n \text { 个 }}$ 使用 8 个数的情形, 得

$$
\sum_{i=1}^{n-2} b_{i} b_{i+1}+(9-n) a_{n}^{2}+a_{n} b_{1} \leq \frac{1}{8}\left(a_{1}+\cdots+a_{n}+(8-n) a_{n}\right)^{2} .
$$

因为 $b_{n-1}=b_{n}=a_{n}$, 所以

$$
\begin{aligned}
\sum_{i=1}^{n} b_{i} b_{i+1} & \leq \frac{1}{8}\left(a_{1}+\cdots+a_{n}+(8-n) a_{n}\right)^{2}-(8-n) a_{n}^{2} \\
& \leq \frac{1}{n}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2},
\end{aligned}
$$

其中最后一步由柯西不等式可证.

综上, 当 $n=2021$ 时, 所求最大值为 $\frac{1}{8}$.

## 评注 供题者对本题有如下评注:

这是一个有一定困难的不等式. 先是要对一般的 $n$ 的取等有一个大概的猜测,通过去掉最小项进行归纳, 将 2021 变为 8 , 进而对 $n=8$ 进行讨论, 讨论中有很多细节需要注意。

第四题 设数列 $\left\{a_{n}\right\}$ 满足: $a_{1}, a_{2}$ 是大于 3 的整数, $a_{n+1}=a_{n}+3\left\lceil\frac{a_{n-1}}{2 n}\right\rceil, n \geq 2$.证明: 存在无穷多个正整数 $m$, 使得 $a_{1}, a_{2}, \cdots, a_{m}$ 都不整除 $a_{m+1}$.

(华东师大二附中学生 王一川 供题)

## 证明 (根据供题者的解答整理):

先证明三个引理.

引理 1 存在正实数 $T$, 使得对任意 $n$ 均有 $a_{n} \leq T \cdot n^{\frac{3}{2}}$.

证明 显然 $a_{1}, a_{2}, \cdots$ 是正整数且 $a_{2} \leq a_{3} \leq \cdots$. 注意到对 $n \geq 3$,

$$
a_{n+1}=a_{n}+3\left\lceil\frac{a_{n-1}}{2 n}\right\rceil \leq a_{n}+\frac{3}{2 n} a_{n}+3,
$$

即

$$
a_{n+1}+6(n+1) \leq\left(1+\frac{3}{2 n}\right)\left(a_{n}+6 n\right) \text {. }
$$

结合伯努利不等式得,

$$
a_{n+1}+6(n+1) \leq\left(\frac{n+1}{n}\right)^{\frac{3}{2}}\left(a_{n}+6 n\right),
$$

所以对 $n \geq 3$,

$$
a_{n}+6 n \leq n^{\frac{3}{2}} \cdot \frac{a_{3}+18}{3^{\frac{3}{2}}} .
$$

故取 $T=\max \left\{\frac{a_{3}+18}{3^{\frac{3}{2}}}, \frac{a_{2}}{2^{\frac{3}{2}}}, a_{1}\right\}$ 即可. 引理 1 证毕.

引理 2 对给定的正整数 $t$, 当 $n$ 充分大时 $a_{n} \geq 1.1^{t}(n+1)$.

证明 对 $t$ 归纳.

当 $t=1$ 时, 因为对 $n \geq 2$ 有 $a_{n+1}-a_{n} \geq 3$, 所以当 $n$ 充分大时 $a_{n} \geq 1.1(n+1)$,结论成立.

假设 $t \geq 2$ 且 $t-1$ 时结论成立, 当 $n$ 充分大时,

$$
a_{n+1}-a_{n}=3\left\lceil\frac{a_{n-1}}{2 n}\right\rceil \geq 3\left\lceil\frac{1.1^{t-1} n}{2 n}\right\rceil \geq 1.5 \cdot 1.1^{t-1} .
$$

故当 $n$ 充分大时, $a_{n} \geq 1.1^{t}(n+1)$, 结论成立.

引理 2 归纳证毕.

引理 3 对给定的正整数 $d$, 当 $n$ 充分大时

$$
\left(a_{n+d+1}-a_{n+d}\right)-\left(a_{n+1}-a_{n}\right) \in\{-3,0,3\} .
$$

证明 因为

$$
\left(a_{n+d+1}-a_{n+d}\right)-\left(a_{n+1}-a_{n}\right)=3\left(\left\lceil\frac{a_{n+d-1}}{2(n+d)}\right\rceil-\left\lceil\frac{a_{n-1}}{2 n}\right\rceil\right),
$$

所以只需证明当 $n$ 充分大时

$$
\left|\frac{a_{n+d-1}}{2(n+d)}-\frac{a_{n-1}}{2 n}\right| \leq 1
$$

事实上，

$$
\left|\frac{a_{n+d-1}}{2(n+d)}-\frac{a_{n-1}}{2 n}\right|
$$

$$
\begin{aligned}
& \leq\left|\frac{a_{n+d-1}}{2(n+d)}-\frac{a_{n-1}}{2(n+d)}\right|+\left|\frac{a_{n-1}}{2 n}-\frac{a_{n-1}}{2(n+d)}\right| \\
& =\left|\frac{3}{2(n+d)}\left(\left[\frac{a_{n+d-3}}{2(n+d-2)}\right]+\cdots+\left[\frac{a_{n-2}}{2(n-1)}\right]\right)\right|+\left|\frac{d}{2 n(n+d)} a_{n-1}\right| \\
& \leq\left|\frac{3}{2(n+d)} \cdot d\left[\frac{a_{n+d-3}}{2(n-1)}\right]\right|+\left|\frac{d}{2 n(n+d)} a_{n-1}\right| \\
& \leq 1
\end{aligned}
$$

其中最后一步用到引理 1 , 当 $n$ 充分大时成立.

引理 3 证毕.

回到原题. 只需证明对任意整数 $m_{0} \geq 100$, 存在整数 $m \geq m_{0}$, 使得 $a_{1}, \cdots, a_{m}$都不整除 $a_{m+1}$.

记 $l=a_{1} a_{2} \cdots a_{m_{0}}$.

由引理 3 , 存在正整数 $M$, 使得对任意 $1 \leq d \leq l$, 当 $n \geq M$ 时,

$$
\left(a_{n+d+1}-a_{n+d}\right)-\left(a_{n+1}-a_{n}\right) \in\{-3,0,3\} .
$$

不妨设 $M \geq m_{0}$, 取正整数 $l^{\prime}$, 使得 $l \mid l^{\prime}$ 且 $l^{\prime} \geq a_{M+1}-a_{M}$.

由引理 2 , 当 $n \rightarrow \infty$ 时, $\left\lceil\frac{a_{n-1}}{2 n}\right\rceil \rightarrow+\infty$, 即 $a_{n+1}-a_{n} \rightarrow+\infty$. 于是可设 $u$ 是最大的正整数, 使得 $a_{u+1}-a_{u} \leq 3 l^{\prime}$, 由 $a_{M+1}-a_{M} \leq l^{\prime}$ 知 $u \geq M$.

对 $1 \leq d \leq l$, 由 $u$ 的定义知 $a_{u+d+1}-a_{u+d}>3 l^{\prime}$; 由引理 $3, a_{u+d+1}-a_{u+d} \leq$ $3 l^{\prime}+3$. 又 $3 \mid a_{u+d+1}-a_{u+d}$, 所以 $a_{u+d+1}-a_{u+d}=3 l^{\prime}+3$.

因为 $3 l \mid 3 l^{\prime}$, 所以 $a_{u+1}, a_{u+2}, \cdots, a_{u+l+1}$ 是模 $3 l$ 意义下公差为 3 的等差数列.从而 $a_{u+1}, a_{u+2}, \cdots, a_{u+l+1}$ 中存在一项模 $3 l$ 余 1 或 2 或 3.

设 $u+1 \leq v \leq u+l+1$ 使 $a_{v} \equiv 1$ 或 2 或 $3(\bmod 3 l)$, 则 $v>u \geq M \geq m_{0}$. 由 $a_{1}, a_{2}, \cdots, a_{m_{0}} \geq 4$ 且 $l=a_{1} a_{2} \cdots a_{m_{0}}$ 知 $a_{1}, a_{2}, \cdots, a_{m_{0}}$ 都不整除 $a_{v}$. 取 $m$ 为最小的正整数, 使得 $a_{m+1} \mid a_{v}$, 此时 $m_{0} \leq m \leq v-1$. 由 $a_{1}, a_{2}, \cdots, a_{m}$ 不整除 $a_{v}$ 即知 $a_{1}, a_{2}, \cdots, a_{m}$ 不整除 $a_{m+1}$.

故满足要求的 $m$ 有无穷多个, 命题得证.

