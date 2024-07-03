# 对数凹多项式应用与介绍 

倪弘康 孙孟越<br>(华东师范大学第二附属中学, 201203)

我们先来看两个试题. 第一个是一道 ICM (International Mathematical Competition for University Students) 试题:

问题 1. 设 $k$ 是一个正整数. 对每个非负整数 $n$, 定义 $f(n)$ 是不等式 $\left|x_{1}\right|+\left|x_{2}\right|+\cdots+\left|x_{k}\right| \leq n$ 的整数解 $\left(x_{1}, x_{2}, \ldots, x_{k}\right) \in \mathbb{Z}^{k}$ 的个数. 求证: 对任意正整数 $n$ 有 $f(n-1) \cdot f(n+1) \leq f(n)^{2}$.

证明 我们先试着求出 $f(n)$ 的显示表达. 我们可以采用母函数或者组合手段, 这里我们采用后者.

当 $x_{1}, x_{2}, \ldots, x_{k}$ 中恰有 $m(0 \leq m \leq k)$ 个非零项时, 其非零项用所谓的 “插板法” 可以求出有 $\left(\begin{array}{c}n \\ m\end{array}\right) \cdot 2^{m}$, 而非零项的位置选择共有 $\left(\begin{array}{c}k \\ k-m\end{array}\right)$ 种. 故我们得到

$$
f(n)=\sum_{m=0}^{k}\left(\begin{array}{c}
n \\
n-m
\end{array}\right) \cdot\left(\begin{array}{c}
k \\
m
\end{array}\right) \cdot 2^{m}
$$

可以发现 $f(n)$ 正好是多项式 $Q_{n}(x) \stackrel{\text { def }}{=}(1+x)^{n}(1+2 x)^{k}$ 的 $x^{n}$ 项系数.

设多项式 $Q_{n-1}(x)=(1+x)^{n-1}(1+2 x)^{k}$ 的 $x^{n-1}, x^{n}, x^{n+1}$ 项系数分别为 $a_{n-1}, a_{n}, a_{n+1}$, 则 $f(n-1)=a_{n-1}$. 由 $Q_{n}(x)=(1+x) Q_{n-1}(x)$ 知, $f(n)=$ $a_{n-1}+a_{n}$. 由 $Q_{n+1}(x)=\left(1+2 x+x^{2}\right) Q_{n-1}(x)$ 知, $f(n+1)=a_{n-1}+2 a_{n}+a_{n+1}$.进而

$$
\begin{aligned}
& f(n-1) f(n+1) \leq f(n)^{2} \\
\Leftrightarrow & a_{n-1}\left(a_{n-1}+2 a_{n}+a_{n+1}\right) \leq\left(a_{n}+a_{n-1}\right)^{2} \\
\Leftrightarrow & a_{n-1} a_{n+1} \leq a_{n}^{2} .
\end{aligned}
$$

这时候, 问题转化为 $Q_{n-1}(x)$ 的系数上来. 但单项系数并不容易处理. 我们猜测可能 $Q_{n-1}(x)$ 的每一项 $x^{i}$ 的系数 $a_{i}$ 都满足 $a_{i-1} a_{i+1} \leq a_{i}^{2}$.

收稿日期: 2018-04-06； 修订日期: 2018-04-25.
我们可以建立如下命题: 称一个实系数多项式 $P(x)=b_{0}+b_{1} x+b_{2} x^{2}+$ $\cdots+b_{k} x^{k}$ 为对数凹的, 若 $b_{n}^{2} \geq b_{n-1} b_{n+1}$ 对所有正整数 $1 \leq n \leq k-1$ 成立.

引理 若正系数多项式 $P(x)$ 是对数凹的, 则 $(1+x) P(x)$ 也是正系数多项式, 且 $(1+x) P(x)$ 是对数凹的.

引理证明 显然 $(1+x) P(x)$ 是正系数多项式. 事实上,

$(1+x) P(x)=b_{0}+\left(b_{0}+b_{1}\right) x+\left(b_{1}+b_{2}\right) x^{2}+\cdots+\left(b_{k}+b_{k-1}\right) x^{k}+x_{k+1}$.

当 $n=1$ 时, 我们有 $\left(b_{0}+b_{1}\right)^{2} \geq b_{0}\left(b_{1}+b_{2}\right) \Leftarrow b_{1}^{2} \geq b_{0} b_{2}$.

当 $1<n<k$ 时, 我们有

$$
\begin{aligned}
& \left(b_{n-1}+b_{n}\right)^{2}-\left(b_{n-2}+b_{n-1}\right)\left(b_{n}+b_{n+1}\right) \\
= & \left(b_{n-1}^{2}-b_{n-2} b_{n}\right)+\left(b_{n} b_{n-1}-b_{n-2} b_{n+1}\right)+\left(b_{n}^{2}-b_{n-1} b_{n+1}\right) .
\end{aligned}
$$

由于 $b_{n-1}^{2} \geq b_{n-2} b_{n}>0, b_{n}^{2} \geq b_{n-1} b_{n+1}>0$, 两式相乘得到

$$
b_{n} b_{n-1} \geq b_{n-2} b_{n+1}>0
$$

故 $b_{n} b_{n-1}-b_{n-2} b_{n+1} \geq 0$, 因此 (1) 右端 3 个括号均为非负实数, (1) 右边 $\geq 0$.

当 $n=k$ 时, 类似于 $n=1$ 的情形. 引理成立.

回到原题. 不难验证 $(1+2 x)^{k}$ 是正系数多项式, 且是对数凹的. 由引理及归纳法知, 正系数多项式 $(1+x)^{n-1}(1+2 x)^{k}$ 也是对数凹的. 结论成立.

同样的技术可以应用在如下一道 AMM (The American Mathematical Monthly) 征解题中.

问题 2. 设 $s, t$ 是给定的自然数, $s \leq t$, 令

$$
a_{n}=\left(\begin{array}{l}
n \\
s
\end{array}\right)+\left(\begin{array}{c}
n \\
s+1
\end{array}\right)+\cdots+\left(\begin{array}{l}
n \\
t
\end{array}\right)
$$

证明: $a_{n}^{2} \geq a_{n-1} a_{n+1}, \forall n \geq 1, n \in \mathbb{Z}^{+}$.

证明 称一个实系数多项式 $P(x)=b_{0}+b_{1} x+b_{2} x^{2}+\cdots+b_{k} x^{k}$ 为对数凹的,若 $b_{n}^{2} \geq b_{n-1} b_{n+1}$ 对所有正整数 $1 \leq n \leq k-1$ 成立.

引理 若正系数多项式 $P(x)$ 是对数凹的, 则 $(1+x) P(x)$ 也是正系数多项式, 且 $(1+x) P(x)$ 是对数凹的.

引理证明同上一题.

回到原题. 对任意的 $n$, 我们记 $f(n, u)$ 为多项式 $(1+x)^{n}\left(1+x+x^{2}+\cdots+\right.$ $\left.x^{t-s}\right)$ 的 $x^{u}$ 项系数.
考虑一个固定的 $n$, 则有 $a_{n}=\left(\begin{array}{c}n \\ s\end{array}\right)+\left(\begin{array}{c}n \\ s+1\end{array}\right)+\cdots+\left(\begin{array}{c}n \\ t\end{array}\right)=f(n, t)$. 并且注意 $f(n, t)=f(n-1, t)+f(n-1, t-1)$. 故

$$
\begin{aligned}
a_{n-1} & =f(n-1, t) \\
a_{n} & =f(n-1, t)+f(n-1, t-1) \\
a_{n+1} & =f(n+1, t)=f(n, t)+f(n, t-1) \\
& =f(n-1, t)+2 f(n-1, t-1)+f(n-1, t-2) .
\end{aligned}
$$

则我们有

$$
a_{n}^{2} \geq a_{n+1} a_{n-1} \Leftrightarrow f(n-1, t-1)^{2} \geq f(n-1, t-2) f(n-1, t)
$$

由于正系数多项式 $1+x+x^{2}+\cdots+x^{t-s}$ 是对数凹的, 由引理得到正系数多项式 $(1+x)^{n-1}\left(1+x+x^{2}+\cdots+x^{t-s}\right)$ 也是对数凹的, 这推出 $f(n-1, t-1)^{2} \geq$ $f(n-1, t-2) f(n-1, t)$. 结论成立.

其实, 在组合、代数、几何、计算机科学、概率、统计中, 对数凹序列经常出现. 在文献 [5] 的记号下, 对数凹的定义与我们给出的定义相同. 上述证明过程中可以看出 $P(x)$ 的系数是正的是不能删去的. 实际上, 在文献 [5] 及更广泛的研究中, 这一条件被无中间零项 (no internal zero) 所取代 (即对数列 $\left\{a_{i}\right\}$, 不存在下标 $i<j<k$ 使得 $\left.a_{i} \neq 0, a_{j}=0, a_{k} \neq 0\right)$.

定理. 若 $P(x)$ 与 $Q(x)$ 是正系数多项式且是对数凹的, 则 $P(x) \cdot Q(x)$ 也是对数凹的.

事实上, 这个定理曾在文 [1], [2] (第 8 章节, 定理 1.2), [3], [4] 中出现. 本文两位作者也提出了这个问题, 倪弘康也独立给出了这个定理的证明, 他给出的证明与 [1] 中的证明本质相同. 应用此定理, 可以立刻得到题目中的上面两个题目中的引理.

## 参考文献

[1] Woong, Kook. On the Product of Log-concave Polynomials[J]. INTEGERS:

Electronic Journal of Combinatorial Number Theory, (6)2006.

[2] S. Karlin. Total Positivity[M]. vol. I. Stanford University Press, 1968.

[3] K.V. Menon. On the Convolution of Logarithmically Concave Sequences[J]. Proceedings of the American Mathematical Society, (23)1969: 439-441.

[4] R. Stanley. Log-concave and Unimodal Sequences in Algebra, Combinatorics, and Geometry[J]. Annals of the New York Academy of Sciences, (576)1989: 500-535.

[5] R. Stanley. Enumerative Combinatorics[M]. Cambridge University Press, 1997.

