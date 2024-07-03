# 一道不等式的上界构造的探索过程 

孙孟越

(华东师范大学第二附属中学, 201203)

笔者在 2016 年 7 月准备全国高中数学联赛的时候, 遇到过这样一个问题:

题 A. 实数 $a, b$ 满足对任意实数 $x$, 均有 $a \cos x+b \cos 2 x \geq-1$, 求 $a+b$ 的最大值.

原题解答直接令 $x=\frac{2 \pi}{3}$, 得到 $a+b \leq 2$. 另外当 $a=\frac{4}{3}, b=\frac{2}{3}$ 时, $a \cos x+b \cos 2 x=\frac{1}{3}(2 \cos x+1)^{2}-1 \geq-1$. 故 $a+b$ 的最大值为 2 .

尽管解答的备注指出了想要让 $f(x)=a \cos x+b \cos 2 x$, 使得 $f\left(\frac{2 \pi}{3}\right)=$ $1, f^{\prime}\left(\frac{2 \pi}{3}\right)=0$, 得到了这个解答. 但是这个 $\frac{2 \pi}{3}$ 的选取以及 $a, b$ 的构造我认为仍是一个神来之笔.

5 个月之后, 我偶然发现 2003 年中国集训队第六次测试中, 出现了如下试题:

题 B. 设 $g(\theta)=\lambda_{1} \cos \theta+\lambda_{2} \cos 2 \theta+\cdots+\lambda_{n} \cos n \theta$, 其中 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}, \theta$是实数. 若对所有实数 $\theta$, 恒有 $g(\theta) \geq-1$, 求证: $\lambda_{1}+\lambda_{2}+\cdots+\lambda_{n} \leq n$.

这个题目的过程很短, 其核心步骤是发现恒等式

$$
g(0)+g\left(\frac{2 \pi}{n+1}\right)+g\left(\frac{4 \pi}{n+1}\right)+\cdots+g\left(\frac{2 n \pi}{n+1}\right)=0 .
$$

从而可以推出 $g(0) \leq n$.

我想, $n$ 可能就是最佳的上界了. 因为 $n=2$ 的时候就是题 $\mathrm{A}$. 但是对 $n$, 证明仍然是困难的. 对一般的 $n, g^{\prime}(\theta)$ 也不好处理. 题 A 备注中的方法难以推广.

先来探求一些 $g$ 的性质, 假设这样的一个 $g$ 存在. 我们可以把 $\cos (k \theta)$ 展开成关于 $\cos (\theta)$ 的多项式 (即 $k$ 次切比雪夫多项式，也可用归纳法证明存在这个多项式). 故存在一个 $n$ 次多项式 $f(x)$, 使得 $g(\theta)$ 可以写成 $f(\cos \theta)$, 其中 $f(x)$的自变量 $x$ 在 $[-1,1]$ 中, 且恒有 $f(x) \geq-1$.

收稿日期: 2017-04-15； 修订日期: 2017-05-28.
至此, 我们把问题转化成为了多项式 $f$ 上的问题.

仔细观察题 B 中等号成立条件, 我们需要多项式 $f(x)+1$ 在 $x=\cos \frac{2 k \pi}{n+1}$ $(k=1,2, \cdots, n)$ 的时候都取到极小值 0 .

而 $\cos \frac{2 k \pi}{n+1}(k=1,2, \cdots, n)$ 在 $(-1,1)$ 内的每个数都出现了两次, 所以可以考虑给 $f(x)+1$ 安排一个二次因式 $\left(x-\cos \frac{2 k \pi}{n+1}\right)\left(x-\cos \frac{2(n+1-k) \pi}{n+1}\right)$ (注意这里有 $\cos \frac{2 k \pi}{n+1}=\cos \frac{2(n+1-k) \pi}{n+1}$, 所以 $x$ 在 $\cos \frac{2 k \pi}{n+1}$ 的邻域变化时, $f(x)+1$ 是不会变号的).

若数 $\cos \frac{2 k \pi}{n+1}(k=1,2, \cdots, n)$ 中出现了 -1 , 那么给 $f(x)+1$ 安排一个一次因式 $(x+1)$ 即可 (因为有 $x \geq-1)$.

通过这样子的分析, 我们可以猜测, 如果 $f$ 存在, 那么形式一定是

$$
f(x)+1=A\left(x-\cos \frac{2 \pi}{n+1}\right)\left(x-\cos \frac{4 \pi}{n+1}\right) \cdots\left(x-\cos \frac{2 n \pi}{n+1}\right),
$$

其中, $A$ 是一个待定的, 与 $n$ 有关的正常数.

我们还需要 $n=g(0)=f(1)$, 从而可以解得 $A=\frac{2^{n}}{n+1}$.

但是, $g$ 的形式仍然不十分明朗 ( $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 的存在性仍很难说明).

于是我们对较小的 $n$, 把 $f(x)$ 还原成 $g(\theta)$. 希望能够有一个简单的 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 的刻画. 试验后, 猜测有:

$$
\begin{aligned}
g(\theta) & =\frac{2}{n+1}(n \cos \theta+(n-1) \cos 2 \theta+(n-2) \cos 3 \theta+\cdots+\cos n \theta) \\
& =\frac{1-\cos (n+1) \theta}{(n+1)(1-\cos \theta)}-1 .
\end{aligned}
$$

其中, 第二个等号在 $\cos \theta \neq 1$ 的时候均成立.

至此, 我基本得到了等号成立的条件. 归纳法应该可以很好地证明上式右端的等号 (也可以采用复数证明). 稍加分析, 这应该也是唯一的等号成立的式子.至此得到了一个新题目.

题 C. (改编自 2003 中国) 已知实数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 和 $g(\theta)=\lambda_{1} \cos \theta+$ $\lambda_{2} \cos 2 \theta+\cdots+\lambda_{n} \cos n \theta$. 若对所有实数 $\theta$ 有 $g(\theta) \geq-1$, 求 $\lambda_{1}+\lambda_{2}+\cdots+\lambda_{n}$最大值.故有

解 记 $\theta_{k}=\frac{2 k \pi}{n+1}, k=0,1, \cdots, n$. 熟知对 $m=1,2, \cdots, n$ 有 $\sum_{k=0}^{n} \cos m \theta_{k}=0$.

$$
\sum_{k=0}^{n} g\left(\theta_{k}\right)=\sum_{m=1}^{n} \sum_{k=0}^{n} \lambda_{m} \cos m \theta_{k}=0
$$

从而

$$
\lambda_{1}+\lambda_{2}+\cdots+\lambda_{n}=g(0)=-\sum_{k=1}^{n} g\left(\theta_{k}\right) \leq n
$$

下面说明等号可以成立. 取 $\lambda_{k}=\frac{2(n+1-k)}{n+1}(k=1,2, \cdots, n)$, 有

$$
g(\theta)=\frac{2}{n+1}(n \cos \theta+(n-1) \cos 2 \theta+(n-2) \cos 3 \theta+\cdots+\cos n \theta) .
$$

下面证明: 若 $\cos \theta \neq 1$, 就有

$$
\begin{gathered}
g(\theta)+1=\frac{1-\cos (n+1) \theta}{(n+1)(1-\cos \theta)}(\geq 0) \\
\Leftrightarrow 2(\cos \theta-1)(n \cos \theta+(n-1) \cos 2 \theta+(n-2) \cos 3 \theta+\cdots+\cos n \theta) \\
=\cos (n+1) \theta+(n+1)(1-\cos \theta)-1 .
\end{gathered}
$$

我们对 $n$ 用数学归纳法来证明 (2). 奠基是显然的, 设 $n-1$ 时命题成立, 考虑 $n$时, 由归纳假设只要证明

$$
\begin{aligned}
& 2(\cos \theta-1)(\cos n \theta+\cos (n-1) \theta+\cdots+\cos \theta) \\
= & \cos (n+1) \theta-\cos n \theta+1-\cos \theta \\
\Leftrightarrow & \frac{\cos \theta-1}{\sin \frac{\theta}{2}}\left(\sin \left(n+\frac{1}{2}\right) \theta-\sin \frac{\theta}{2}\right)=-2 \sin \left(n+\frac{1}{2}\right) \theta \cdot \sin \frac{\theta}{2}+1-\cos \theta
\end{aligned}
$$

由 $1-\cos \theta=2 \sin ^{2} \frac{\theta}{2}$, 上式是不难证明的. 故命题对 $n$ 成立, 由归纳原理知, (2)成立.

综上所述, $\lambda_{1}+\lambda_{2}+\cdots+\lambda_{n}$ 最大值为 $n$.

## 参考文献

[1] 走向 IMO 数学奥林匹克试题集锦 (2003) [M]. 2003 年 IMO 中国国家集训队教练组编, 上海: 华东师范大学出版社, 2003.9.

