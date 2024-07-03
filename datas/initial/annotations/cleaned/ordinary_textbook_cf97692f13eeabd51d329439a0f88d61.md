# 关于 Schur、Surányi 不等式的一些推广及证明 

李橙<br>(浙江省镇海中学, 315299)<br>指导教师: 陈科钧

匈牙利 Miklṕs Schweitzer 数学竞赛 (MSC-Hungary) 曾经考过以下不等式:

题 1 (Janos Surányi) 设实数 $a_{i} \geq 0\left(i=1,2, \cdots, n, n \in \mathbb{N}^{*}\right)$. 求证:

$$
(n-1) \sum_{i=1}^{n} a_{i}^{n}+n \prod_{i=1}^{n} a_{i} \geq\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n-1}\right) .
$$

当 $n \geq 3$ 时, 等号成立当且仅当 $a_{1}=a_{2}=\cdots=a_{n}$ 或 $a_{1}=a_{2}=\cdots=a_{n-1}>0$, $a_{n}=0$ 及其轮换.

罗马尼亚普罗伊斯蒂大学 Vasile Cirtoaje 教授也曾得到过如下类似的结果:

题 2 已知实数 $a_{i} \geq 0\left(i=1,2, \cdots, n, n \in \mathbb{N}^{*}\right)$. 求证:

$$
\sum_{i=1}^{n} a_{i}^{n}+n(n-1) \prod_{i=1}^{n} a_{i} \geq\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{a_{i}}\right)
$$

当 $n \geq 3$ 时, 等号成立当且仅当 $a_{1}=a_{2}=\cdots=a_{n}$ 或 $a_{1}=a_{2}=\cdots=a_{n-1}>0$, $a_{n}=0$ 及其轮换.

题 3 已知实数 $a_{i} \geq 0\left(i=1,2, \cdots, n, n \in \mathbb{N}^{*}\right)$. 求证:

$$
(n-1) \sum_{i=1}^{n} a_{i}^{n+1} \geq\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n}-\prod_{i=1}^{n} a_{i}\right)
$$

当 $n \geq 3$ 时, 等号成立当且仅当 $a_{1}=a_{2}=\cdots=a_{n}$ 或 $a_{1}=a_{2}=\cdots=a_{n-1}>0$, $a_{n}=0$ 及其轮换.

事实上, 在题 1,2 中令 $n=3$ 即为 3 次 Schur 不等式, 在题 3 中令 $n=3$ 即为 4 次 Schur 不等式. 那么, 对于任意次的 Schur 不等式, 我们能否得到类似的推广?

修订日期: 2023-12-25.
对于 Schur 不等式: 对任意 $a, b, c \geq 0, r \in \mathbb{R}$,

$$
\sum_{c y c} a^{r+1}(a-b)(a-c) \geq 0
$$

进行代数变形, 我们可以得到以下两种形式.

形式 1:

$$
2 \sum_{c y c} a^{r+3}+\left(\prod_{c y c} a\right)\left(\sum_{c y c} a^{r}\right) \geq\left(\sum_{c y c} a\right)\left(\sum_{c y c} a^{r+2}\right) .
$$

形式 2:

$$
\sum_{c y c} a^{r+3}+2\left(\prod_{c y c} a\right)\left(\sum_{c y c} a^{r}\right) \geq\left(\prod_{c y c} a\right)\left(\sum_{c y c} \frac{1}{a}\right)\left(\sum_{c y c} a^{r+1}\right) .
$$

基于此, 笔者提出了两个问题:

问题 1 求所有的实数 $r$, 使得对任意 $a_{1}, a_{2}, \cdots, a_{n}>0$, 都有

$$
(n-1) \sum_{i=1}^{n} a_{i}^{n+r}+\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) \geq\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n+r-1}\right) .
$$

问题 2 求所有的实数 $r$, 使得对任意 $a_{1}, a_{2}, \cdots, a_{n}>0$, 都有

$$
\sum_{i=1}^{n} a_{i}^{n+r}+(n-1)\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) \geq\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{a_{i}}\right)\left(\sum_{i=1}^{n} a_{i}^{r+1}\right) .
$$

经过一些探索, 我们得到了如下的令人惊讶的结果:

定理 1 给定正整数 $n$, 对任意 $a_{1}, a_{2}, \cdots, a_{n}>0$ (在 $r>-1$ 时将定义域延拓至 $\left.a_{1}, a_{2}, \cdots, a_{n} \geq 0\right)$, 且对任意实数 $r$, 有

$$
(n-1) \sum_{i=1}^{n} a_{i}^{n+r}+\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) \geq\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n+r-1}\right) .
$$

在 $n \geq 3$ 时，等号适用于 $a_{1}=a_{2}=\cdots=a_{n}$, 且在 $r>-1$ 时，等号也适用于 $a_{1}=a_{2}=\cdots=a_{n-1}>0, a_{n}=0$ 及其轮换.

特别地, 取 $r=0$ 即为题 1 , 取 $r=1$ 即为题 3 .

定理 2 给定正整数 $n$, 对任意 $a_{1}, a_{2}, \cdots, a_{n}>0$ (在 $r>-1$ 时将定义域延拓至 $\left.a_{1}, a_{2}, \cdots, a_{n} \geq 0\right)$, 且对任意实数 $r$, 有

$$
\sum_{i=1}^{n} a_{i}^{n+r}+(n-1)\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) \geq\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{a_{i}}\right)\left(\sum_{i=1}^{n} a_{i}^{r+1}\right) .
$$

在 $n \geq 3$ 时，等号适用于 $a_{1}=a_{2}=\cdots=a_{n}$, 且在 $r>-1$ 时，等号也适用于 $a_{1}=a_{2}=\cdots=a_{n-1}>0, a_{n}=0$ 及其轮换.

特别地, 取 $r=0$ 即为题 2 .
证明 由于对于 $n=1,2$ 的情况, (1) (2) 均为恒等式, 故只需考虑 $n \geq 3$的情形.

我们首先考虑 $r>-1$ 且 $a_{1}, a_{2}, \cdots, a_{n}$ 中有 0 的情况, 不妨 $a_{n}=0$.

对于 (1), 此时 (1) 等价于

$$
(n-1) \sum_{i=1}^{n-1} a_{i}^{n+r} \geq\left(\sum_{i=1}^{n-1} a_{i}\right)\left(\sum_{i=1}^{n-1} a_{i}^{n+r-1}\right)
$$

由于 $n+r-1>1$, 由 Chebyshev 不等式知上式成立, 等号适用于 $a_{1}=a_{2}=$ $\cdots=a_{n-1}$.

对于 (2), 此时 (2) 等价于

$$
\sum_{i=1}^{n-1} a_{i}^{n+r} \geq\left(\prod_{i=1}^{n-1} a_{i}\right)\left(\sum_{i=1}^{n-1} a_{i}^{r+1}\right)
$$

由 AM-GM 知

$$
\left(\prod_{i=1}^{n-1} a_{i}\right)\left(\sum_{i=1}^{n-1} a_{i}^{r+1}\right) \leq \frac{1}{n-1}\left(\sum_{i=1}^{n-1} a_{i}^{n-1}\right)\left(\sum_{i=1}^{n-1} a_{i}^{r+1}\right) .
$$

由于 $r+1>0$, 由 Chebyshev 不等式知

$$
\frac{1}{n-1}\left(\sum_{i=1}^{n-1} a_{i}^{n-1}\right)\left(\sum_{i=1}^{n-1} a_{i}^{r+1}\right) \leq \sum_{i=1}^{n-1} a_{i}^{n+r}
$$

故成立, 等号适用于 $a_{1}=a_{2}=\cdots=a_{n-1}$.

下面考虑 $a_{1}, a_{2}, \cdots, a_{n}>0$ 的情况.

我们记不等式 (1) 为 $p(n, r)$, 不等式 (2) 为 $q(n, r)$.

在 $p(n, r)$ 中令 $b_{i}=\frac{1}{a_{i}}$, 则可知

$$
\begin{aligned}
p(n, r) & \Leftrightarrow(n-1) \sum_{i=1}^{n} b_{i}^{-n-r}+\frac{\sum_{i=1}^{n} b_{i}^{-r}}{\prod_{i=1}^{n} b_{i}} \geq\left(\sum_{i=1}^{n} \frac{1}{b_{i}}\right)\left(\sum_{i=1}^{n} b_{i}^{-n-r+1}\right) \\
& \Leftrightarrow q(n,-n-r)
\end{aligned}
$$

即 $p\left(n, r_{1}\right) \Leftrightarrow q\left(n, r_{2}\right)$, 其中 $r_{1}+r_{2}=-n$.

我们考虑对 $n$ 使用数学归纳法.

$n=3$ 时, 由前面我们知道(1) (2) 均等价于 Schur 不等式, 等号适用于 $a_{1}=a_{2}=a_{3}$.

下面 $n \geq 4$.

(i) 首先证明若对任意 $r \in \mathbb{R}, p(n-1, r)$ 成立, 则对任意 $r \geq 1-n, p(n, r)$也成立.

不妨设 $a_{1} \geq a_{2} \geq \cdots \geq a_{n-1} \geq a_{n}>0$, 且 $\sum_{i=1}^{n-1} a_{i}=1$, 则知 $a_{n} \leq \frac{1}{n-1}$.
由对任意 $r \in \mathbb{R}, p(n-1, r)$ 成立知:

要证:

$$
\left(\prod_{i=1}^{n-1} a_{i}\right)\left(\sum_{i=1}^{n-1} a_{i}^{r}\right) \geq \sum_{i=1}^{n-1} a_{i}^{n+r-2}-(n-2) \sum_{i=1}^{n-1} a_{i}^{n+r-1}
$$

$$
\begin{aligned}
& (n-1) \sum_{i=1}^{n-1} a_{i}^{n+r}+(n-1) a_{n}^{n+r}+a_{n}\left(\prod_{i=1}^{n-1} a_{i}\right)\left(\sum_{i=1}^{n-1} a_{i}^{r}+a_{n}^{r}\right) \\
\geq & \left(1+a_{n}\right)\left(\sum_{i=1}^{n-1} a_{i}^{n+r-1}+a_{n}^{n+r-1}\right) .
\end{aligned}
$$

将(3) 代入(4) 知只需证:

$$
\begin{aligned}
& {\left[(n-1) \sum_{i=1}^{n-1} a_{i}^{n+r}-\sum_{i=1}^{n-1} a_{i}^{n+r-1}\right]+a_{n}\left[\sum_{i=1}^{n-1} a_{i}^{n+r-2}-(n-1) \sum_{i=1}^{n-1} a_{i}^{n+r-1}\right]} \\
& +a_{n}^{r+1}\left[\left(\prod_{i=1}^{n-1} a_{i}\right)+(n-2) a_{n}^{n-1}-a_{n}^{n-2}\right] \geq 0 .
\end{aligned}
$$

由伯努利不等式知:

$$
\begin{aligned}
& \prod_{i=1}^{n-1} a_{i}+(n-2) a_{n}^{n-1}-a_{n}^{n-2} \\
= & \prod_{i=1}^{n-1}\left(a_{n}+a_{i}-a_{n}\right)+(n-2) a_{n}^{n-1}-a_{n}^{n-2} \\
\geq & a_{n}^{n-1}+\left(1-(n-1) a_{n}\right) a_{n}^{n-2}+(n-2) a_{n}^{n-1}-a_{n}^{n-2} \\
= & 0
\end{aligned}
$$

故我们只需证明:

$$
\left[(n-1) \sum_{i=1}^{n-1} a_{i}^{n+r}-\sum_{i=1}^{n-1} a_{i}^{n+r-1}\right]+a_{n}\left[\sum_{i=1}^{n-1} a_{i}^{n+r-2}-(n-1) \sum_{i=1}^{n-1} a_{i}^{n+r-1}\right] \geq 0
$$

将上式看作 $a_{n}$ 的一次函数知只需在 $a_{n}=0$ 和 $a_{n}=\frac{1}{n-1}$ 时成立即可.

$1^{\circ} a_{n}=0$, 由 Chebyshev 不等式 (这里用到 $n+r-1 \geq 0$ )

$$
(n-1) \sum_{i=1}^{n-1} a_{i}^{n+r} \geq\left(\sum_{i=1}^{n-1} a_{i}\right)\left(\sum_{i=1}^{n-1} a_{i}^{n+r-1}\right)=\sum_{i=1}^{n-1} a_{i}^{n+r-1}
$$

知成立.

$2^{\circ} a_{n}=\frac{1}{n-1}$, 由 AM-GM 不等式

$$
(n-1) a_{i}^{n+r}+\frac{1}{n-1} a_{i}^{n+r-2} \geq 2 a_{i}^{n+r-1}
$$

求和即知成立.

故对任意 $r \geq 1-n, p(n, r)$ 成立, 且等号适用于 $a_{1}=a_{2}=\cdots=a_{n}$.

(ii) 然后证明若对任意 $r \in \mathbb{R}, q(n-1, r)$ 成立, 且对任意 $r \geq 1-n, p(n, r)$成立, 则对任意 $r \geq 1-n, q(n, r)$ 也成立.
由对任意 $r \in \mathbb{R}, q(n-1, r)$ 成立知:

$$
a_{j} \cdot\left(\sum_{i \neq j} a_{i}^{n+r-1}\right)+(n-2)\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i \neq j} a_{i}^{r}\right) \geq\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i \neq j} \frac{1}{a_{i}}\right)\left(\sum_{i \neq j} a_{i}^{r+1}\right) .
$$

对于任意 $1 \leq j \leq n$ 求和可知:

$$
\begin{aligned}
& \left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n+r-1}\right)-\sum_{i=1}^{n} a_{i}^{n+r}+(n-1)(n-2)\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) \\
& \geq\left(\prod_{i=1}^{n} a_{i}\right)\left[(n-2)\left(\sum_{i=1}^{n} \frac{1}{a_{i}}\right)\left(\sum_{i=1}^{n} a_{i}^{r+1}\right)+\sum_{i=1}^{n} a_{i}^{r}\right] .
\end{aligned}
$$

又由对任意 $r \geq 1-n, p(n, r)$ 成立知:

$$
\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n+r-1}\right) \leq(n-1) \sum_{i=1}^{n} a_{i}^{n+r}+\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) .
$$

代入知:

$$
\begin{aligned}
& (n-2) \sum_{i=1}^{n} a_{i}^{n+r}+(n-1)(n-2)\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{r}\right) \\
& \geq(n-2)\left(\prod_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{a_{i}}\right)\left(\sum_{i=1}^{n} a_{i}^{r+1}\right) .
\end{aligned}
$$

两边约去 $(n-2)$ 即知 $\forall r \geq 1-n, q(n, r)$ 成立, 且等号适用于 $a_{1}=a_{2}=\cdots=a_{n}$.

(iii) 由于 $p\left(n, r_{1}\right) \Leftrightarrow q\left(n, r_{1}\right)$, 其中 $r_{1}+r_{2}=-n$. 可知对任意 $r \leq-1$, $p(n, r), q(n, r)$ 也都成立, 归纳毕.

故对于 $a_{1}, a_{2}, \cdots, a_{n}>0$ 的情形定理 1,2 也成立, 且等号适用于 $a_{1}=a_{2}=$ $\cdots=a_{n}$.

对于Surányi 不等式有如下推广:

引理 $\quad f: I \mapsto \mathbb{R}$ 在 $I$ 上连续且三阶可微, 满足对任意 $x \in I, f^{\prime \prime}(x) \geq 0$, $f^{\prime \prime \prime}(x) \geq 0$, 正整数 $n \geq 3, a_{k} \in I, k=1,2, \cdots, n$, 则

$$
(n-1) \sum_{k=1}^{n} f\left(a_{k}\right)+n f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq \sum_{1 \leq i, j \leq n} f\left(\frac{n-1}{n} a_{i}+\frac{1}{n} a_{j}\right) .
$$

特别地, 取 $f(x)=e^{x}$ 即为题 1. 证明参见 [1].

笔者依据其形式, 将题 2 推广为:

定理 $3 f: I \mapsto \mathbb{R}$ 在 $I$ 上连续且三阶可微, 满足对任意 $x \in I, f^{\prime \prime}(x) \geq 0$, $f^{\prime \prime \prime}(x) \geq 0$, 正整数 $n \geq 3, a_{k} \in I, k=1,2, \cdots, n$, 则

$$
\sum_{k=1}^{n} f\left(a_{k}\right)+n(n-1) f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq \sum_{1 \leq i, j \leq n} f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}+\frac{1}{n}\left(a_{i}-a_{j}\right)\right) .
$$

特别地, 取 $f(x)=e^{x}$ 即为题 2 .

证明 我们考虑对 $n$ 使用数学归纳法.

$n=3$ 时, 上式等价于引理.

下面 $n \geq 4$.

考虑上式在 $n-1$ 时成立, 我们将

$$
1 \leq p \leq n, \frac{n-1}{n} a_{k}+\frac{1}{n} a_{p}(1 \leq k \leq n \text { 且 } k \neq p)
$$

代入知:

$$
\begin{aligned}
& \sum_{k \neq p} f\left(\frac{n-1}{n} a_{k}+\frac{1}{n} a_{p}\right)+(n-1)(n-2) f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \\
& \geq \sum_{\substack{1 \leq i, j \leq n \\
i \neq p, j \neq p}} f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}+\frac{1}{n}\left(a_{i}-a_{j}\right)\right) .
\end{aligned}
$$

对于对任意 $1 \leq p \leq n$ 求和可知:

$$
\begin{aligned}
& \sum_{1 \leq i, j \leq n} f\left(\frac{n-1}{n} a_{i}+\frac{1}{n} a_{j}\right)-\sum_{k=1}^{n} f\left(a_{k}\right)+n(n-1)(n-2) f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \\
& \geq(n-2) \sum_{1 \leq i, j \leq n} f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}+\frac{1}{n}\left(a_{i}-a_{j}\right)\right)+n f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right),
\end{aligned}
$$

又由引理知:

$$
\sum_{1 \leq i, j \leq n} f\left(\frac{n-1}{n} a_{i}+\frac{1}{n} a_{j}\right) \leq(n-1) \sum_{k=1}^{n} f\left(a_{k}\right)+n f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right)
$$

代入知:

$$
\begin{aligned}
& (n-2) \sum_{k=1}^{n} f\left(a_{k}\right)+n(n-1)(n-2) f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \\
& \geq(n-2) \sum_{1 \leq i, j \leq n} f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}+\frac{1}{n}\left(a_{i}-a_{j}\right)\right) .
\end{aligned}
$$

两边约去 $(n-2)$ 知对 $n$ 的情况也成立, 即证.

评注 该定理可以看作对导函数下凸 (由下可知上凸也同样成立) 的下凸函数的 Popoviciu 不等式的加强:

Popoviciu 不等式 ${ }^{[4]} \quad f: I \mapsto \mathbb{R}$ 在 $I$ 上下凸, 正整数 $n \geq 3, a_{k} \in I, k=$ $1,2, \cdots, n$, 则

$$
\sum_{k=1}^{n} f\left(a_{k}\right)+n(n-2) f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq(n-1) \sum_{k=1}^{n} f\left(\frac{1}{n-1} \sum_{j \neq k} a_{j}\right) .
$$

事实上由 Jensen 不等式知: 对任意 $1 \leq j \leq n$,

$$
\sum_{i \neq j} f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}+\frac{1}{n}\left(a_{i}-a_{j}\right)\right) \geq(n-1) f\left(\frac{1}{n-1} \sum_{t \neq j} a_{t}\right)
$$

求和即可得 Popoviciu 不等式.

我们还可以观察到 $f^{\prime \prime \prime}(x) \geq 0$ 这个条件可以换为 $f^{\prime \prime \prime}(x) \leq 0$, 这是因为我们令 $g(x)=f(-x)$, 则 $g^{\prime \prime}(x)=f^{\prime \prime}(-x) \geq 0, g^{\prime \prime \prime}(x)=-f^{\prime \prime \prime}(-x) \geq 0$, 故由

$$
\begin{gathered}
(n-1) \sum_{k=1}^{n} g\left(-a_{k}\right)+n g\left(-\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq \sum_{1 \leq i, j \leq n} g\left(-\frac{n-1}{n} a_{i}-\frac{1}{n} a_{j}\right), \\
\sum_{k=1}^{n} g\left(-a_{k}\right)+n(n-1) g\left(-\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq \sum_{1 \leq i, j \leq n} g\left(-\frac{1}{n} \sum_{k=1}^{n} a_{k}-\frac{1}{n}\left(a_{i}-a_{j}\right)\right),
\end{gathered}
$$

知此时引理及定理 3 亦成立.

根据上面的结果结合 Karamata 不等式, 我们容易证明在相同条件下:

1. $p \in\left[\frac{1}{n}, \frac{1}{2}\right]$,

$$
(n-1) \sum_{k=1}^{n} f\left(a_{k}\right)+n f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq \sum_{1 \leq i, j \leq n} f\left((1-p) a_{i}+p a_{j}\right)
$$

2. $p \in\left[\frac{1}{n}, \frac{1}{n-1}\right]$,

$$
\sum_{k=1}^{n} f\left(a_{k}\right)+n(n-2) f\left(\frac{1}{n} \sum_{k=1}^{n} a_{k}\right) \geq \sum_{\substack{1 \leq i, j \leq n \\ i \neq j}} f\left([1-(n-1) p] a_{i}+p \sum_{k \neq j} a_{k}\right)
$$

更一般地, 我们猜想定理 1、2 的如下推广成立:

公开问题 $f: I \mapsto \mathbb{R}$ 在 $I$ 上连续且三阶可微, 满足对任意 $x \in I, f^{\prime \prime}(x) \geq 0$, $f^{\prime \prime \prime}(x) \geq 0$ (或 $\left.f^{\prime \prime \prime}(x) \leq 0\right)$, 正整数 $n \geq 3$, 正实数 $p \in\left(0, \frac{1}{n}\right), a_{k} \in I, k=$ $1,2, \cdots, n$, 则

(1)

$$
\begin{aligned}
& (n-1) \sum_{k=1}^{n} f\left(a_{k}\right)+\sum_{k=1}^{n} f\left([1-(n-1) p] a_{k}+p \sum_{j \neq k} a_{j}\right) \\
& \geq \sum_{1 \leq i, j \leq n} f\left((1-p) a_{i}+p a_{j}\right) .
\end{aligned}
$$

(2)

$$
\begin{aligned}
& \sum_{k=1}^{n} f\left(a_{k}\right)+(n-1) \sum_{k=1}^{n} f\left([1-(n-1) p] a_{k}+p \sum_{j \neq k} a_{j}\right) \\
& \geq \sum_{1 \leq i, j \leq n} f\left([1-(n-1) p] a_{i}+p \sum_{k \neq j} a_{k}\right) .
\end{aligned}
$$

## 参考文献

[1] 韩京俊. 代数不等式: 证明方法 $[\mathrm{M}]$. 合肥: 中国科学技术大学出版社, 2023.3

[2] Vasile Cirtoaje. 数学不等式. 第 4 卷, Jensen 不等式的扩展与加细 $[M]$.易桂如, 文湘波, 译. 哈尔滨: 哈尔滨工业大学出版社, 2022.5

[3] Pham Kim Hung. 不等式的秘密: 高级不等式. 第2 卷 $[M]$. 隋振林, 译.哈尔滨: 哈尔滨工业大学出版社, 2014.1

[4] Vasić P M, Stanković LR. Some inequalities for convex functions [J]. Math Balkanica, 1976(6): 281-288

