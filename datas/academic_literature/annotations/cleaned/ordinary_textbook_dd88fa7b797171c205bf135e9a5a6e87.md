# 关于差的平方积的一类代数不等式 

刘奔

(山东大学, 济南, 250100)

在高中数学学习时, 我们注意到下面十分简单的问题: 当正数 $x, y$ 满足 $x^{2}+y^{2}=1$ 时, $(x-y)^{2}$ 的最大值为 1 . 但当 $x, y$ 的取值范围改为实数集时，同样问题的最大值却是 2. 这诱发我们研究在各种条件下，差的平方积 $\prod_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2}$ 的最大值问题.

我们首先发现若四个实变量 $a_{1}, a_{2}, a_{3}, a_{4}$ 满足 $a_{1}^{2}+a_{2}^{2}+a_{3}^{2}+a_{4}^{2}=1$, 则 $\prod_{1 \leq i<j \leq 4}\left(a_{j}-a_{i}\right)^{2}$ 的最大值为 $\frac{1}{108}$. 事实上, 我们证明了如下关于四个变元差的积的如下代数不等式:

问题 1. 设 $a_{1}, a_{2}, a_{3}, a_{4} \in \mathbf{R}$, 则

$$
108 \prod_{1 \leq i<j \leq 4}\left(a_{j}-a_{i}\right)^{2} \leq\left(\sum_{i=1}^{4} a_{i}^{2}\right)^{6}
$$

等号当 $a_{1}, a_{2}, a_{3}, a_{4}$ 与多项式 $f(x)=x^{4}-6 x^{2}+3$ 的根成比例时成立.

证明 考虑多项式 $f(x):=x^{4}-6 x^{2}+3$. 不难求得 $f$ 有四个实根 $\pm \sqrt{3 \pm \sqrt{6}}$,这里的两个 $\pm$ 号独立选取. 令 $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{4}$ 为 $f$ 的四个实根的升序排列. 我们先证明对 $1 \leq i \leq 4$, 有

$$
\sum_{j \neq i} \frac{1}{\alpha_{i}-\alpha_{j}}=\frac{1}{2} \alpha_{i}
$$

首先容易检验 $f$ 满足方程 $f^{\prime \prime}-x f^{\prime}+4 f=0$, 于是可得

$$
\frac{f^{\prime \prime}\left(\alpha_{i}\right)}{f^{\prime}\left(\alpha_{i}\right)}=\alpha_{i}
$$

再定义多项式 $f_{i}(x):=\frac{f(x)}{\left(x-\alpha_{i}\right)}, 1 \leq i \leq 4$, 那么有

$$
\frac{f_{i}^{\prime}(x)}{f_{i}(x)}=\sum_{j \neq i} \frac{1}{x-\alpha_{j}}
$$

收稿日期: 2017-04-12; 修订日期: 2017-06-12.
于是

$$
\frac{f_{i}^{\prime}\left(\alpha_{i}\right)}{f_{i}\left(\alpha_{i}\right)}=\sum_{j \neq i} \frac{1}{\alpha_{i}-\alpha_{j}}
$$

另一方面, 由于

$$
\begin{aligned}
f(x) & =\sum_{k=0}^{4} \frac{f^{(k)}\left(\alpha_{i}\right)}{k !}\left(x-\alpha_{i}\right)^{k} \\
& =f^{\prime}\left(\alpha_{i}\right)\left(x-\alpha_{i}\right)+\frac{1}{2} f^{\prime \prime}\left(\alpha_{i}\right)\left(x-\alpha_{i}\right)^{2}+\left(x-\alpha_{i}\right)^{3} g_{i}(x),
\end{aligned}
$$

其中 $g_{i}(x)$ 是一次多项式, 可得

$$
f_{i}(x)=f^{\prime}\left(\alpha_{i}\right)+\frac{1}{2} f^{\prime \prime}\left(\alpha_{i}\right)\left(x-\alpha_{i}\right)+\left(x-\alpha_{i}\right)^{2} g_{i}(x)
$$

从而有

$$
\begin{aligned}
f_{i}\left(\alpha_{i}\right) & =f^{\prime}\left(\alpha_{i}\right) \\
f_{i}^{\prime}\left(\alpha_{i}\right) & =\frac{1}{2} f^{\prime \prime}\left(\alpha_{i}\right)
\end{aligned}
$$

最后由 $(2),(3),(4),(5)$ 可知 (1) 成立.

直接计算可知

$$
\sum_{i=1}^{4} \alpha_{i}^{2}=12
$$

以及

$$
\prod_{1 \leq i<j \leq 4}\left(\alpha_{i}-\alpha_{j}\right)^{2}=2^{10} \times 3^{3}
$$

下面我们来证明原不等式.

由对称性, 不妨设 $a_{1} \leq a_{2} \leq a_{3} \leq a_{4}$. 由 AM-GM 不等式以及 Cauchy 不等式, 有

$$
\begin{aligned}
\prod_{1 \leq i<j \leq 4}\left(\frac{a_{i}-a_{j}}{\alpha_{i}-\alpha_{j}}\right)^{2} & \leq\left(\frac{1}{6} \sum_{1 \leq i<j \leq 4} \frac{a_{i}-a_{j}}{\alpha_{i}-\alpha_{j}}\right)^{12} \\
& =\left(\frac{1}{6} \sum_{i=1}^{4} a_{i} \sum_{j \neq i} \frac{1}{\alpha_{i}-\alpha_{j}}\right)^{12} \\
& =\left(\frac{1}{12} \sum_{i=1}^{4} a_{i} \alpha_{i}\right)^{12} \\
& \leq \frac{1}{12^{12}}\left(\sum_{i=1}^{4} a_{i}^{2}\right)^{6}\left(\sum_{i=1}^{4} \alpha_{i}^{2}\right)^{6}
\end{aligned}
$$

这里第三行的等号用到了 (1), 再将 (6), (7) 代入上式, 即得要证不等式.
分析上述证明过程不难发现等号成立当且仅当诸 $a_{i}$ 为诸 $\alpha_{i}$ 的一个排列的倍数.

用类似问题 1 的证明方法, 我们还证明了如下的问题.

问题 2. 设 $a_{1}, a_{2}, a_{3}, a_{4} \in \mathbf{R}$, 则

$$
108 \cdot \prod_{1 \leq i<j \leq 4}\left(a_{j}-a_{i}\right)^{2} \leq\left(\frac{\sum_{i=1}^{4} a_{i}^{2}}{\sum_{i=1}^{4} a_{i}}\right)^{12}
$$

等号当 $a_{1}, a_{2}, a_{3}, a_{4}$ 与 $\alpha_{i}+\sqrt{3}$ 成比例时成立, 其中 $\alpha_{i}$ 为 $f(x)=x^{4}-6 x^{2}+3$ 的 4 个根.

证明 不妨设 $a_{1}+a_{2}+a_{3}+a_{4} \geq 0, a_{1} \leq a_{2} \leq a_{3} \leq a_{4}$, 令 $\beta_{i}:=\alpha_{i}+\sqrt{3}$, $1 \leq i \leq 4$, 这里诸 $\alpha_{i}$ 的意义同题 1 . 那么 (1) 式成为

$$
\frac{\sqrt{3}}{2}+\sum_{j \neq i} \frac{1}{\beta_{i}-\beta_{j}}=\frac{1}{2} \beta_{i}
$$

直接计算可知

$$
\begin{gathered}
\sum_{i=1}^{4} \beta_{i}=4 \sqrt{3}, \\
\sum_{i=1}^{4} \beta_{i=1}^{2}=24, \\
\prod_{1 \leq i<j \leq 4}\left(\beta_{i}-\beta_{j}\right)^{2}=2^{10} \times 3^{3} .
\end{gathered}
$$

由 AM-GM 不等式以及 Cauchy 不等式, 有

$$
\begin{aligned}
& \left(\frac{1}{4 \sqrt{3}} \sum_{i=1}^{4} a_{i}\right)^{12} \prod_{1 \leq i<j \leq 4}\left(\frac{a_{i}-a_{j}}{\beta_{i}-\beta_{j}}\right)^{2} \\
\leq & \left(6 \times \frac{1}{12} \times \frac{1}{4 \sqrt{3}} \sum_{i=1}^{4} a_{i}+\frac{1}{12} \sum_{1 \leq i<j \leq 4} \frac{a_{i}-a_{j}}{\beta_{i}-\beta_{j}}\right)^{24} \\
= & \left(\frac{1}{12} \sum_{i=1}^{4} a_{i}\left(\frac{\sqrt{3}}{2}+\sum_{j \neq i} \frac{1}{\beta_{i}-\beta_{j}}\right)\right)^{24} \\
= & \left(\frac{1}{24} \sum_{i=1}^{4} a_{i} \beta_{i}\right)^{24} \\
\leq & \frac{1}{24^{24}}\left(\sum_{i=1}^{4} a_{i}^{2}\right)^{12}\left(\sum_{i=1}^{4} \beta_{i}^{2}\right)^{12}
\end{aligned}
$$

这里第三行的等号用到了 (8), 再将 (10), (11) 代入上式, 即得所证不等式. 利用 (9), 不难发现等号成立当且仅当诸 $a_{i}$ 为诸 $\beta_{i}$ 的一个排列的倍数.

进一步, 我们证明了一个包括题 1 和题 2 的更一般的结论, 这就是下面的

定理 1. 设 $n$ 是正整数 $(n \geq 2), x_{1}, x_{2}, \cdots, x_{n} \in \mathbf{R}, r \geq 0$, 则

$$
\left|\sum_{k=1}^{n} x_{k}\right|_{1 \leq i<j \leq n}^{r} \prod_{1}\left(x_{i}-x_{j}\right)^{2} \leq c_{n, r}\left(\sum_{k=1}^{n} x_{k}^{2}\right)^{\frac{n^{2}-n+r}{2}}
$$

其中

$$
c_{n, r}:=(n r)^{\frac{r}{2}}\left(n^{2}-n+r\right)^{-\frac{n^{2}-n+r}{2}} \prod_{k=1}^{n} k^{k}
$$

等号成立当且仅当诸 $x_{k}(1 \leq k \leq n)$ 与多项式 $H_{n}\left(x+\sqrt{\frac{r}{n}}\right)$ 的所有根成比例, 其中多项式序列 $\left\{H_{n}\right\}_{n \in \mathbf{N}}$ 的定义为:

$$
H_{n}(x)=\sum_{k=0}^{\left[\frac{n}{2}\right]}(-1)^{k}(2 k-1) ! !\left(\begin{array}{c}
n \\
2 k
\end{array}\right) x^{n-2 k}
$$

$H_{n}$ 被称作 Hermite 多项式, 它必有 $n$ 个实根. 其中还约定 $0^{0}=1$.

问题 1 , 问题 2 分别为 $(n, r)=(4,0)$, 以及 $(n, r)=(4,12)$ 的情形. 因为定理 1 的证明较为复杂, 且直于本文的任务, 这里省略了证明.

作为定理 1 的一个应用, 在定理 1 中取 $r=0$ 便有

推论 1. 设 $n$ 是正整数 $(n \geq 2), a_{1}, a_{2}, \cdots, a_{n} \in \mathbf{R}$ 且满足 $\sum_{k=1}^{n} a_{k}^{2}=1$, 则 $\prod_{1 \leq i<j \leq n}\left(a_{j}-a_{i}\right)^{2}$ 的最大值为 $\left(n^{2}-n\right)^{-\frac{n^{2}-n}{2}} \prod_{k=1}^{n} k^{k}$.

我们还注意到了下面已知的不等式 (如 [1] 中出现过):

设 $a_{1}, a_{2}, a_{3}, a_{4}$ 是非负实数, 则

$$
12^{6} \prod_{1 \leq i<j \leq 4}\left(a_{j}-a_{i}\right)^{2} \leq\left(\sum_{i=1}^{4} a_{i}\right)^{12} .
$$

我们采用相似于定理 1 的证明方法也推广 (12) 到一般情况, 建立了下面的定理 2.

定理 2. 设 $n$ 是正整数 $(n \geq 2), \alpha \geq-1, x_{1}, x_{2}, \cdots, x_{n}$ 是非负实数, 则

$$
\left(\prod_{k=1}^{n} x_{k}\right)^{\alpha+1} \prod_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2} \leq c_{n, \alpha}\left(\sum_{k=1}^{n} x_{k}\right)^{n(\alpha+n)},
$$

其中

$$
c_{n, \alpha}:=(n(\alpha+n))^{-n(\alpha+n)} \prod_{k=1}^{n}\left(k^{k}(\alpha+k)^{\alpha+k}\right) .
$$

等号成立当且仅当诸 $x_{k}(1 \leq k \leq n)$ 与多项式 $L_{n}^{(\alpha)}(x)$ 的所有根成比例. 其中多项式序列 $\left\{L_{n}^{(\alpha)}\right\}_{n \in \mathbf{N}}$ 的定义为:

$$
L_{n}^{(\alpha)}(x)=\sum_{k=0}^{n}(-1)^{k} k !\left(\begin{array}{c}
\alpha+n \\
k
\end{array}\right)\left(\begin{array}{l}
n \\
k
\end{array}\right) x^{n-k},
$$

$L_{n}^{(\alpha)}$ 被称作 Laguerre 多项式, 它必有 $n$ 个非负实根.

取 $(n, \alpha)=(4,-1)$, 可得不等式 (12). 此外, 在定理 2 中取 $\alpha=-1$ 可得

推论 2 . 设 $n \geq 2$ 是正整数, $x_{1}, x_{2}, \cdots, x_{n}$ 是非负实数且 $\sum_{i=1}^{n} x_{i}=1$, 则 $\prod_{1 \leq i<j \leq n}\left(x_{j}-x_{i}\right)^{2}$ 的最大值为 $(n(n-1))^{-n(n-1)} \prod_{k=1}^{n} k^{n}(k-1)^{k-1}$.

## 参考文献

[1] 韩京俊. 初等不等式的证明方法 $[\mathrm{M}]$. 第二版, 哈尔滨: 哈尔滨工业大学出版社, 2014.

