# 凹数列的反向柯西不等式 

牟晓生

(哈佛大学, xiaoshengmu@fas.harvard.edu)

## 1. 问题背景

设 $f(x), g(x)$ 是区间 $[0,1]$ 上的非负函数, 那么我们有连续形式的柯西不等式:

$$
\int_{0}^{1} f(x) g(x) d x \leq\left(\int_{0}^{1} f^{2}(x) d x\right)^{\frac{1}{2}} \cdot\left(\int_{0}^{1} g^{2}(x) d x\right)^{\frac{1}{2}} .
$$

类似地, 如果 $a_{1}, a_{2}, \ldots, a_{n} ; b_{1}, b_{2}, \ldots, b_{n}$ 是两个非负数列, 则有:

$$
\sum_{i=1}^{n} a_{i} b_{i} \leq\left(\sum_{i=1}^{n} a_{i}^{2}\right)^{\frac{1}{2}} \cdot\left(\sum_{i=1}^{n} b_{i}^{2}\right)^{\frac{1}{2}}
$$

反向柯西不等式的研究试图在一定条件下给出与上面反向的不等式, 即左边大于等于右边的常数倍. 这方面的第一个结果由 Polya 和 Szego 得到:

定理 1 (Polya-Szego, 1925) 如果 $f(x) \in[a, A], g(x) \in[b, B]$, 则有:

$$
\int_{0}^{1} f(x) g(x) d x \geq \frac{2 \sqrt{a b A B}}{a b+A B} \cdot\left(\int_{0}^{1} f^{2}(x) d x\right)^{\frac{1}{2}} \cdot\left(\int_{0}^{1} g^{2}(x) d x\right)^{\frac{1}{2}} .
$$

这个不等式的离散形式也成立.

我们知道柯西不等式在 $\frac{f(x)}{g(x)}$ 为常数时取等号. 由于限制 $f(x), g(x)$ 的大小也就限制了它们比值的取值范围, 这样上面的结果就很好理解了. 同样地, 通过假设 $f(x)$ 与 $g(x)$ 都是凹函数也能起到限制 $\frac{f(x)}{g(x)}$ 的效果, 从而得到下面的结论:

定理 2 (Gruss '35, Bellman '56, Barnes '69, Borell '73) 如果 $f(x)$与 $g(x)$ 都是 $[0,1]$ 区间上非负的凹函数, 则有:

$$
\int_{0}^{1} f(x) g(x) d x \geq \frac{1}{2} \cdot\left(\int_{0}^{1} f^{2}(x) d x\right)^{\frac{1}{2}} \cdot\left(\int_{0}^{1} g^{2}(x) d x\right)^{\frac{1}{2}} .
$$

注意到这里的常数 $\frac{1}{2}$ 是最优的, 在 $f(x)=x, g(x)=1-x$ 时取等号.

本文考虑定理 2 的离散形式. 我们将证明:
定理 3 设 $a_{1}, a_{2}, \ldots, a_{n} ; b_{1}, b_{2}, \ldots, b_{n}(n \geq 2)$ 是两个非负的凹数列, 即对每个 $2 \leq i \leq n-1$ 有 $2 a_{i} \geq a_{i-1}+a_{i+1}, 2 b_{i} \geq b_{i-1}+b_{i+1}$. 则有:

$$
\sum_{i=1}^{n} a_{i} b_{i} \geq \frac{n-2}{2 n-1} \cdot\left(\sum_{i=1}^{n} a_{i}^{2}\right)^{\frac{1}{2}} \cdot\left(\sum_{i=1}^{n} b_{i}^{2}\right)^{\frac{1}{2}}
$$

等号在 $a_{i}=i-1, b_{i}=n-i$ 时取到.

据笔者所知, 定理 3 在现有文献中仍是一个猜想. Barnes 曾在论文中指出他关于定理 2 的方法不适用于一般离散的情况, 而只能解决两个数列均单调的特殊情况. 下一节我们先给出那个问题的简洁证明.

## 2. 单调情形的简洁证明

这一节我们假设两个数列都是单调数列, 在此附加条件下证明定理 3 . 由于可以将一个数列中的每一项乘上常数而不改变问题条件与结论, 我们不妨假设 $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} b_{i}=\frac{n(n-1)}{2}$. 此时有如下引理:

引理 4 设 $a_{1}, a_{2}, \ldots, a_{n}$ 是一个单调的非负凹数列, 且满足 $\sum_{i=1}^{n} a_{i}=\frac{n(n-1)}{2}$.则

$$
\sum_{i=1}^{n} a_{i}^{2} \leq \sum_{i=1}^{n}(i-1)^{2}=\frac{n(n-1)(2 n-1)}{6} .
$$

证明 不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 由 Karamata 不等式, 只需证明对每个 $1 \leq k \leq n-1$ 有

$$
\sum_{i=k+1}^{n} a_{i} \leq \sum_{i=k+1}^{n}(i-1)
$$

注意到对每个 $1 \leq j \leq k<i \leq n$, 由凹数列性质有

$$
a_{j} \geq \frac{j-1}{i-1} \cdot a_{i}+\frac{i-j}{i-1} \cdot a_{1} \geq \frac{j-1}{i-1} \cdot a_{i} .
$$

重写为 $\frac{i-1}{j-1} \cdot a_{j} \geq a_{i}$, 对 $i$ 求和得到

$$
\frac{\sum_{i=k+1}^{n}(i-1)}{j-1} \cdot a_{j} \geq \sum_{i=k+1}^{n} a_{i}, \forall 1 \leq j \leq k .
$$

如果 $\sum_{i=k+1}^{n} a_{i}>\sum_{i=k+1}^{n}(i-1)$, 那么由上面的不等式可知 $a_{j}>j-1, \forall 1 \leq j \leq k$.这样导致所有 $a_{i}$ 的和大于 $\sum_{i=1}^{n}(i-1)$, 与引理条件矛盾. 于是引理得证!

回到定理 3 的证明. 我们知道 (1) 式右边至多是 $\frac{n(n-1)(n-2)}{6}$. 另一方面,

$$
2 \sum_{i=1}^{n} a_{i} b_{i}=\sum_{i=1}^{n}\left(a_{i}+b_{i}\right)^{2}-\sum_{i=1}^{n} a_{i}^{2}-\sum_{i=1}^{n} b_{i}^{2}
$$

$$
\begin{aligned}
& \geq \frac{1}{n}\left(\sum_{i=1}^{n}\left(a_{i}+b_{i}\right)\right)^{2}-\frac{n(n-1)(2 n-1)}{3} \\
& =n(n-1)^{2}-\frac{n(n-1)(2 n-1)}{3}=\frac{n(n-1)(n-2)}{3} .
\end{aligned}
$$

这样就证明了 (1) 式.

如果引理 4 的结论对一般凹数列也成立, 那么用同样的证明即可得到完整的定理 3. 很遗憾, $\sum_{i=1}^{n} a_{i}^{2}$ 的最大值并不在 $a_{i}=i-1$ (或 $a_{i}=n-i$ ) 时取到. 我们有下面的结论:

引理 $\mathbf{5}$ (Khintchine) 设 $a_{1}, a_{2}, \ldots, a_{n}(n \geq 3)$ 是一个非负凹数列, 且满足 $\sum_{i=1}^{n} a_{i}=\frac{n(n-1)}{2}$. 则

$$
\sum_{i=1}^{n} a_{i}^{2} \leq \sum_{i=1}^{n-1}\left(\frac{n(i-1)}{n-2}\right)^{2}=\frac{n^{2}(n-1)(2 n-3)}{6(n-2)} .
$$

证明 我们采取一个间接的策略, 假设 $\sum_{i=1}^{n} a_{i}^{2}$ 取到最大值, 从而导出数列的一些性质以便最后直接验证 (3) 式. 这个方法之后还会用到.

在所有满足 $\sum_{i=1}^{n} a_{i}=\frac{n(n-1)}{2}$ 的非负凹数列中取一个使得 $\sum_{i=1}^{n} a_{i}^{2}$ 最大. 由紧集和连续函数的性质, 最大值是取到的.

我们首先证明至多存在一个 $j(2 \leq j \leq n-1)$, 使得 $2 a_{j}>a_{j-1}+a_{j+1}$.

假设不然, 则存在 $1<j_{1}<j_{2}<n$ 使得

$$
2 a_{j_{1}}>a_{j_{1}-1}+a_{j_{1}+1} \text { 且 } 2 a_{j_{2}}>a_{j_{2}-1}+a_{j_{2}+1} \text {. }
$$

考虑一个辅助数列 $\left\{\delta_{i}\right\}_{i=1}^{n}$ ：当 $1 \leq i \leq j_{1}$ 时 $\delta_{i}=i-1$; 当 $j_{2} \leq i \leq n$时 $\delta_{i}=\lambda(i-n)$ (其中 $\lambda$ 是待定的正数); 当 $j_{1}<i<j_{2}$ 时 $\delta_{i}=\frac{j_{2}-i}{j_{2}-j_{1}} \cdot \delta_{j_{1}}+\frac{i-j_{1}}{j_{2}-j_{1}} \cdot \delta_{j_{2}}$.从几何角度来说, $n$ 个点 $\left(i, \delta_{i}\right)$ 连接成三个线段, 而拐点恰好出现在 $i=j_{1}, j_{2}$.

易知存在唯一的 $\lambda$ 使得 $\sum_{i} \delta_{i}=0$. 这时考虑两个数列 $a_{i}^{\prime}=a_{i}+\epsilon \cdot \delta_{i}$ 以及 $a_{i}^{\prime \prime}=a_{i}-\epsilon \cdot \delta_{i}$, 它们的和都等于 $\frac{n(n-1)}{2}$. 注意到数列 $\left\{a_{i}\right\}$ 是凹的, 并且在 $i=$ $j_{1}, j_{2}$ 处是严格凹的. 而数列 $\pm\left\{\delta_{i}\right\}$ 在 $i \neq j_{1}, j_{2}$ 处是线性的, 所以对充分小的正数 $\epsilon$, 数列 $\left\{a_{i}^{\prime}\right\},\left\{a_{i}^{\prime \prime}\right\}$ 都是凹的. 又由于 $\delta_{1}=\delta_{n}=0, a_{1}^{\prime}=a_{1}^{\prime \prime}=a_{1}, a_{n}^{\prime}=a_{n}^{\prime \prime}=a_{n}$都是非负的. 由凹数列的性质, $\left\{a_{i}^{\prime}\right\}$ 与 $\left\{a_{i}^{\prime \prime}\right\}$ 都是非负的. 故 $\left\{a_{i}^{\prime}\right\},\left\{a_{i}^{\prime \prime}\right\}$ 都是符合条件的数列, 但是

$$
\sum_{i} a_{i}^{\prime 2}+\sum_{i} a_{i}^{\prime \prime 2}-2 \sum_{i} a_{i}^{2}=2 \epsilon^{2} \sum_{i} \delta_{i}^{2}>0
$$

与 $\sum_{i} a_{i}^{2}$ 的最大性相矛盾!
所以我们证明了存在 $k(1 \leq k \leq n)$, 使得 $a_{1}, a_{2}, \ldots, a_{k}$ 是等差数列,而 $a_{k}, a_{k+1}, \ldots, a_{n}$ 也是等差数列. 如果 $k=1$ 或 $k=n$, 那么 $\left\{a_{i}\right\}$ 是单调的.

考虑辅助数列 $\delta_{i}=i-\frac{n+1}{2}$. 如果 $a_{1}, a_{n}>0$, 则 $\left\{a_{i} \pm \epsilon \delta_{i}\right\}$ 都是非负的凹数列, 且其中一个的平方和比 $\left\{a_{i}\right\}$ 大. 所以只可能 $a_{1}=0$ 或者 $a_{n}=0$, 再由 $\sum_{i} a_{i}=\frac{n(n-1)}{2}$ 可知 $a_{i}=i-1$ 或者 $a_{i}=n-i$.

这样我们再次得到引理 4 的结论, 即当 $\left\{a_{i}\right\}$ 单调时 $\sum_{i} a_{i}^{2}$ 的最大值是 $\frac{n(n-1)(2 n-1)}{6}<\frac{n^{2}(n-1)(2 n-3)}{6(n-2)}$.

接下来假设 $1<k<n$, 我们证明 $a_{1}=a_{n}=0$. 如果 $a_{1}>0$, 考虑下面的辅助数列 $\delta_{i}$ : 当 $k \leq i \leq n$ 时 $\delta_{i}=n-i$; 当 $1 \leq i<k$ 时 $\delta_{i}=n-k-\lambda(k-i)$. 取唯一的 $\lambda$ 使得 $\sum_{i} \delta_{i}=0$, 那么和上面一样可以证明 $\left\{a_{i} \pm \epsilon \delta_{i}\right\}$ 都是和为 $\frac{n(n-1)}{2}$ 的非负凹数列. 这与 $\sum_{i} a_{i}^{2}$ 最大相矛盾!

所以存在 $1<k<n$ 使得

$$
a_{i}=\frac{i-1}{k-1} \cdot a_{k}, \quad 1 \leq i \leq k, \quad \text { 以及 } \quad a_{i}=\frac{n-i}{n-k} \cdot a_{k}, \quad k<i \leq n .
$$

利用 $\sum_{i} a_{i}=\frac{n(n-1)}{2}$ 可知 $a_{k}=n$, 于是可以直接求出

$$
\sum_{i} a_{i}^{2}=n^{2} \cdot\left(\sum_{i=1}^{k}\left(\frac{i-1}{k-1}\right)^{2}+\sum_{i=k+1}^{n}\left(\frac{n-i}{n-k}\right)^{2}\right)=\frac{n^{2}}{6} \cdot\left(2 n-2+\frac{1}{k-1}+\frac{1}{n-k}\right) .
$$

由于 $\frac{1}{x}$ 是凸函数, 容易看出上面最右边的式子在 $k=2$ 或 $k=n-1$ 时最大. 最大值是 $\frac{n^{2}}{6} \cdot\left(2 n-2+1+\frac{1}{n-2}\right)=\frac{n^{2}}{6} \cdot \frac{(n-1)(2 n-3)}{n-2}$, 于是引理得证!

## 3. 一般数列的证明

这一节我们证明定理 3 对一般的非负凹数列 $\left\{a_{i}\right\},\left\{b_{i}\right\}$ 都成立.

不妨假设 $\sum_{i} a_{i}=\sum_{i} b_{i}=\frac{n(n-1)}{2}$. 只需证明在这些条件下有

$$
\sum_{i} a_{i} b_{i} \geq \frac{n-2}{2 n-1} \sum_{i} a_{i}^{2}
$$

如果 (4) 式成立, 那么对称地有

$$
\sum_{i} a_{i} b_{i} \geq \frac{n-2}{2 n-1} \sum_{i} b_{i}^{2}
$$

于是 (1) 式一定成立.

为证 (4) 式, 用上一节的调整法可知只需考虑三种情况:

(i) $a_{i}=i-1,1 \leq i \leq n$,

(ii) $a_{i}=n-i, 1 \leq i \leq n$ 或者
(iii) 存在 $1<k<n$ 使得 $a_{i}=\frac{i-1}{k-1} \cdot n, 1 \leq i \leq k$, 以及 $a_{i}=\frac{n-i}{n-k} \cdot n, k<i \leq n$.

先考虑前两种(对称的)情况, 此时只要证明

$$
\sum_{i=1}^{n}(i-1) b_{i} \geq \frac{n(n-1)(n-2)}{6}
$$

由于左边是 $b_{i}$ 的线性和, 我们可以再用调整法使得数列 $\left\{b_{i}\right\}$ 也属于上面三种情况之一, 详见角注. ${ }^{1}$

如果 $b_{i}=i-1, \sum_{i} a_{i} b_{i}=\frac{n(n-1)(2 n-1)}{6}$. 如果 $b_{i}=n-i, \sum_{i} a_{i} b_{i}=\frac{n(n-1)(n-2)}{6}$.最后假设数列 $\left\{b_{i}\right\}$ 属于情况(iii), 此时我们将 $2 \sum_{i} a_{i} b_{i} \geq \frac{n(n-1)(n-2)}{3}$ 改写为

$$
\sum_{i}\left(a_{i}+b_{i}\right)^{2} \geq \sum_{i} a_{i}^{2}+\sum_{i} b_{i}^{2}+\frac{n(n-1)(n-2)}{3}
$$

也就是

$$
\begin{aligned}
\sum_{i}\left(a_{i}+b_{i}-n+1\right)^{2} & \geq \sum_{i} a_{i}^{2}+\sum_{i} b_{i}^{2}-\frac{n(n-1)(2 n-1)}{3} \\
& =\sum_{i} b_{i}^{2}-\frac{n(n-1)(2 n-1)}{6} .
\end{aligned}
$$

由于 $a_{1}=b_{1}=0,(5)$ 式左边至少是 $(n-1)^{2}$. 而由引理 $5,(5)$ 式右边至多是

$$
\frac{n^{2}(n-1)(2 n-3)}{6(n-2)}-\frac{n(n-1)(2 n-1)}{6}=\frac{n(n-1)^{2}}{3(n-2)} \leq(n-1)^{2} .
$$

故定理成立.

最后假设 $\left\{a_{i}\right\}$ 属于情况(iii). 由引理 5 知 (4) 式的右边至多是 $\frac{n^{2}(n-1)(2 n-3)}{6(2 n-1)}$.于是只要证明 $2 \sum_{i} a_{i} b_{i} \geq \frac{n^{2}(n-1)(2 n-3)}{3(2 n-1)}$, 即

$$
\sum_{i}\left(a_{i}+b_{i}-n\right)^{2} \geq \sum_{i} a_{i}^{2}+\sum_{i} b_{i}^{2}+\frac{n^{2}(n-1)(2 n-3)}{3(2 n-1)}-n^{2}(n-2) .
$$

如果 $\left\{b_{i}\right\}$ 属于情况 (iii), 那么 $a_{1}=b_{1}=a_{n}=b_{n}=0$. 此时 (6) 式左边至少是 $2 n^{2}$. 而由引理 (5) 可知 (6) 式右边至多是

$$
\frac{n^{2}(n-1)(2 n-3)}{3(n-2)}+\frac{n^{2}(n-1)(2 n-3)}{3(2 n-1)}-n^{2}(n-2)=n^{2} \cdot \frac{2 n^{2}-4 n+1}{(n-2)(2 n-1)} \leq 2 n^{2} \text {. }
$$[^0]如果 $\left\{b_{i}\right\}$ 属于情况 (i) 或 (ii), 那么 (6) 式左边至少是 $n^{2}$. 而由引理 4 和引理 5 可知 (6) 式右边至多是

$$
\begin{aligned}
& \frac{n^{2}(n-1)(2 n-3)}{6(n-2)}+\frac{n(n-1)(2 n-1)}{6}+\frac{n^{2}(n-1)(2 n-3)}{3(2 n-1)}-n^{2}(n-2) \\
= & n^{2}-\frac{n(n-1)\left(2 n^{2}-6 n+1\right)}{3(n-2)(2 n-1)} \leq n^{2} .
\end{aligned}
$$

故无论如何 (6) 式都成立, 我们也就完成了定理 3 的证明!


[^0]:    1 具体来说, 我们可以取数列 $\left\{b_{i}\right\}$ 使得 $\sum_{i} a_{i} b_{i}$ 最大, 并在此条件下要求满足 $2 b_{j}>b_{j-1}+b_{j+1}$的下标 $j$ 最少(称这样的下标为 “拐点”). 如果还有多个数列则尽量要求 $b_{1}, b_{n}$ 等于零. 同引理 5 的证明, 至多有一个下标 $j$ 使得 $2 b_{j}>b_{j-1}+b_{j+1}$. 否则 $\left\{b_{i} \pm \epsilon \delta_{i}\right\}$ 也符合条件, 并且 $\sum_{i} a_{i}\left(b_{i}+\epsilon \delta_{i}\right)+\sum_{i} a_{i}\left(b_{i}-\epsilon \delta_{i}\right)=2 \sum_{i} a_{i} b_{i}$ (辅助数列 $\delta_{i}$ 同引理 5 的证明). 那样由最大性得到 $\sum_{i}^{i} a_{i}\left(b_{i} \pm \epsilon \delta_{i}\right)=\sum_{i}^{i} a_{i} b_{i}$. 然而通过取适当的 $\epsilon$ 可以使得 $\left\{b_{i} \pm \epsilon \delta_{i}\right\}$ 中的一个数列比 $\left\{b_{i}\right\}$ 少一个拐点, 与我们选取 $\left\{b_{i}\right\}$ 的方法矛盾! 于是 $\left\{b_{i}\right\}$ 要么是单调的, 要么只有一个拐点. 如果单调, 我们可以用同样方法进一步证明 $b_{1}=0$ 或者 $b_{n}=0$, 于是 $b_{i}=i-1$ 或者 $b_{i}=n-i$. 如果 $2 b_{k}>b_{k-1}+b_{k+1}$ 是一个拐点, 则可以证明 $b_{1}=b_{n}=0$. 否则对适当的 $\epsilon$, 数列 $\left\{b_{i} \pm \epsilon \delta_{i}\right\}$ 也达到最大值, 并且要么少一个拐点, 要么在 $b_{1}, b_{n}$ 处多一个零.

