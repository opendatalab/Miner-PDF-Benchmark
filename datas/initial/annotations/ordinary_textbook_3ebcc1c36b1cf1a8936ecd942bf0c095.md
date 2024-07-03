数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 对一类离散形式 Gronwall 型不等式的研究 

何忆捷<br>(华东师范大学数学系, 200241)

在 2014 年国际数学奥林匹克中国国家集训队选拔 [1] 中, 有如下问题:

问题 1. 对任意一个实数列 $\left\{x_{n}\right\}$, 定义数列 $\left\{y_{n}\right\}$ 如下:

$$
y_{1}=x_{1}, \quad y_{n+1}=x_{n+1}-\left(\sum_{i=1}^{n} x_{i}^{2}\right)^{\frac{1}{2}}, \quad n \geq 1
$$

求最小的正数 $\lambda$, 使得对任意实数列 $\left\{x_{n}\right\}$ 及一切正整数 $m$, 均有

$$
\frac{1}{m} \sum_{i=1}^{m} x_{i}^{2} \leq \sum_{i=1}^{m} \lambda^{m-i} y_{i}^{2}
$$

实际上, 问题 1 源于对一类离散形式 Gronwall 型不等式的研究. 本文详细介绍这一研究, 并对结果进行若干讨论.

## 1. 研究背景及本文的主要工作

在 1919 年, T.H.Gronwall [2] 提出了如下定理 (Gronwall 引理):

定理 A. 对 $[0, \infty)$ 上的非负可积函数 $u(t), v(t)$ 及非负实数 $a$, 若

$$
u(t) \leq a+\int_{0}^{t} v(s) u(s) d s, \quad t \geq 0
$$

则

$$
u(t) \leq a \exp \left(\int_{0}^{t} v(s) d s\right), \quad t \geq 0
$$

这一定理在微分方程解的存在性、唯一性、稳定性等研究中具有重要意义.

此后研究者们给出了多种变化形式的 Gronwall 型不等式. 其中, D. Willett 与 J.S.W.Wong [3] 提出并证明了如下离散化形式的 Gronwall 型不等式:
定理 B. 对非负实数 $a_{n}, b_{n}, c_{n}, x_{n}(n=1,2, \cdots)$ 及实数 $r \geq 1$, 若

$$
x_{n} \leq a_{n}+b_{n}\left(\sum_{i=1}^{n-1} c_{i} x_{i}^{r}\right)^{\frac{1}{r}}, \quad n=1,2, \cdots
$$

则

$$
\sum_{i=1}^{n} c_{i} x_{i}^{r} \leq\left(1-\left(1-p_{n}\right)^{\frac{1}{r}}\right)^{-r} \sum_{i=1}^{n} a_{i}^{r} c_{i} p_{i}, \quad n=1,2, \cdots
$$

其中 $p_{k}=\prod_{i=1}^{k}\left(1+b_{i}^{r} c_{i}\right)^{-1}, k=1,2, \cdots$.

H. Alzer [4] 对 [3] 的证明方法予以改进, 并将 (1) 加强为

$$
\sum_{i=1}^{n} c_{i} x_{i}^{r} \leq\left(p_{1}^{\frac{1}{r}}-\left(p_{1}-p_{n}\right)^{\frac{1}{r}}\right)^{-r} \sum_{i=1}^{n} a_{i}^{r} c_{i} p_{i}, \quad n=1,2, \cdots
$$

其中, 由 $0<p_{n} \leq p_{1} \leq 1$ 及 $r \geq 1$, 可知

$$
\left(p_{1}^{\frac{1}{r}}-\left(p_{1}-p_{n}\right)^{\frac{1}{r}}\right)^{-r} \leq\left(1-\left(1-p_{n}\right)^{\frac{1}{r}}\right)^{-r} .
$$

在 [4] 的这一结果中, 若取 $b_{n}=b>0, c_{n}=1(n=1,2, \cdots)$, 则得到序列 $\left\{x_{n}\right\}$ 的一个本质估计:

$$
\sum_{i=1}^{n} x_{i}^{r} \leq C(n) \cdot \sum_{i=1}^{n} \frac{a_{i}^{r}}{d^{i}}, \quad n=1,2, \cdots,
$$

其中 $d=1+b^{r}, C(n)=\left(\left(\frac{1}{d}\right)^{\frac{1}{r}}-\left(\frac{1}{d}-\frac{1}{d^{n}}\right)^{\frac{1}{r}}\right)^{-r}$.

本文在 $b_{n}=b>0, c_{n}=1(n=1,2, \cdots)$ 这一特殊情况下作进一步研究. 首先证明下述定理.

定理. 给定实数 $b>0, r \geq 1$, 若非负实数列 $\left\{a_{n}\right\},\left\{x_{n}\right\}$ 满足

$$
x_{n} \leq a_{n}+b \cdot\left(\sum_{i=1}^{n-1} x_{i}^{r}\right)^{\frac{1}{r}}, \quad n=1,2, \cdots
$$

则

$$
\sum_{i=1}^{n} x_{i}^{r} \leq n^{r-1} \cdot \sum_{i=1}^{n} d^{n-i} a_{i}^{r}, \quad n=1,2, \cdots
$$

其中 $d=1+b^{r}$.

在此基础上, 本文给出如下事实:

(i) 若将 (5) 中的 $n^{r-1} d^{n}$ 记为 $C_{1}(n)$, 则当 $r>1$ 时, 有 $\lim _{n \rightarrow \infty} \frac{C_{1}(n)}{C(n)}=0$, 这意味着当 $n$ 充分大时, (5) 对 (3) 的上界估计作了改进. 当 $r=1$ 时, 有 $C_{1}(n)=C(n)$.

(ii) 在 (5) 中, $d$ 不能改进为更小的正数.

(iii) 在 $r>1$ 的情况下, 对任意正数 $M$, 存在满足 (4) 的非负实数列
$\left\{a_{n}\right\},\left\{x_{n}\right\}$ 及正整数 $m$, 使得

$$
\sum_{i=1}^{m} x_{i}^{r}>M \cdot \sum_{i=1}^{m} d^{m-i} a_{i}^{r}
$$

这意味着不能将 (5) 中的 $n^{r}-1$ 改进为任意一个常数值 $M$.

最后, 本文说明问题 1 与本研究的关联.

## 2. 定理的证明及相关讨论

先证明一个引理.

引理. 设实数 $r \geq 1$, 则对任意正数 $k, u, v$, 有

$$
(u+v)^{r} \leq(k+1)^{r-1} u^{r}+\left(1+\frac{1}{k}\right)^{r-1} v^{r} .
$$

证明 由齐次性, 不妨令 $v=1$, 只需证明对一切正数 $u$, 有

$$
f(u)=(k+1)^{r-1} u^{r}+\left(1+\frac{1}{k}\right)^{r-1}-(u+1)^{r} \geq 0 .
$$

当 $r=1$ 时, 结论显然成立. 当 $r>1$ 时, 由于

$$
\begin{aligned}
f^{\prime}(u) & =r(k+1)^{r-1} u^{r-1}-r(u+1)^{r-1} \\
& =r\left((u+k u)^{r-1}-(u+1)^{r-1}\right) \begin{cases}>0, & k u>1, \\
=0, & k u=1, \\
<0, & 0<k u<1,\end{cases}
\end{aligned}
$$

所以

$$
f(u) \geq f\left(\frac{1}{k}\right)=(k+1)^{r-1} \cdot \frac{1}{k^{r}}+\left(1+\frac{1}{k}\right)^{r-1}-\left(\frac{1}{k}+1\right)^{r}=0 .
$$

引理证毕.

下面给出定理的证明.

定理证明 当 $n=1$ 时, 由 (4) 知 $x_{1}^{r} \leq a_{1}^{r}$, 即 (5) 成立.

假设 (5) 在 $n=k$ 时成立, 下面考虑 $n=k+1$ 时的情形.

由 (4), 并在 (6) 中令 $u=a_{k+1}, v=b \cdot\left(\sum_{i=1}^{k} x_{i}^{r}\right)^{\frac{1}{r}}$, 可得

$$
x_{k+1}^{r} \leq\left(a_{k+1}+b \cdot\left(\sum_{i=1}^{k} x_{i}^{r}\right)^{\frac{1}{r}}\right)^{r} \leq(k+1)^{r-1} a_{k+1}^{r}+\left(1+\frac{1}{k}\right)^{r-1} b^{r} \cdot \sum_{i=1}^{k} x_{i}^{r},
$$

结合 $1 \leq\left(1+\frac{1}{k}\right)^{r-1}, d=1+b^{r}$ 及归纳假设, 可知

$$
\sum_{i=1}^{k+1} x_{i}^{r} \leq(k+1)^{r-1} a_{k+1}^{r}+\left(1+\left(1+\frac{1}{k}\right)^{r-1} b^{r}\right) \cdot\left(\sum_{i=1}^{k} x_{i}^{r}\right)
$$

$$
\begin{aligned}
& \leq(k+1)^{r-1} a_{k+1}^{r}+\left(\left(1+\frac{1}{k}\right)^{r-1} d\right) \cdot\left(k^{r-1} \cdot \sum_{i=1}^{k} d^{k-i} a_{i}^{r}\right) \\
& =(k+1)^{r-1} a_{k+1}^{r}+(k+1)^{r-1} \cdot \sum_{i=1}^{k} d^{k+1-i} a_{i}^{r} \\
& =(k+1)^{r-1} \cdot \sum_{i=1}^{k+1} d^{k+1-i} a_{i}^{r},
\end{aligned}
$$

即 (5) 在 $n=k+1$ 时也成立. 由数学归纳法知, 定理得证.

以下进行相关的讨论, 先对前文所指出的事实 (i), (ii), (iii) 予以证明.

(i) 的证明 注意到 $d=1+b^{r}>1$, 有 $\lim _{n \rightarrow \infty} \frac{1}{d^{n-1}}=0$, 于是

$$
\begin{aligned}
C(n) & =\left(\left(\frac{1}{d}\right)^{\frac{1}{r}}-\left(\frac{1}{d}-\frac{1}{d^{n}}\right)^{\frac{1}{r}}\right)^{-r}=d \cdot\left(1-\left(1-\frac{1}{d^{n-1}}\right)^{\frac{1}{r}}\right)^{-r} \\
& \sim d \cdot\left(\frac{1}{r} \cdot \frac{1}{d^{n-1}}\right)^{-r}=d^{(n-1) r+1} \cdot r^{r} \quad(n \rightarrow \infty),
\end{aligned}
$$

从而

$$
\frac{C_{1}(n)}{C(n)} \sim \frac{n^{r-1} d^{n}}{d^{(n-1) r+1} \cdot r^{r}}=\frac{1}{r^{r}} \cdot\left(\frac{n}{d^{n-1}}\right)^{r-1} \quad(n \rightarrow \infty) .
$$

由于 $\lim _{n \rightarrow \infty} \frac{n}{d^{n-1}}=0$, 这表明当 $r>1$ 时, 有 $\lim _{n \rightarrow \infty} \frac{C_{1}(n)}{C(n)}=0$.

另一方面, 当 $r=1$ 时, 显然有 $C_{1}(n)=d^{n}=C(n)$. 证毕.

(ii) 的证明 取非负实数列 $\left\{a_{n}\right\},\left\{x_{n}\right\}$ 满足

$$
x_{1}=a_{1}=1, \quad x_{n}=b \cdot d^{\frac{n-2}{r}}, \quad a_{n}=0 \quad(n=2,3, \cdots),
$$

则对任意整数 $n \geq 2$, 有

$$
\sum_{i=1}^{n-1} x_{i}^{r}=1+\sum_{i=2}^{n-1} b^{r} d^{i-2}=1+b^{r} \cdot \frac{d^{n-2}-1}{d-1}=1+\left(d^{n-2}-1\right)=d^{n-2}
$$

故 (4) 恰好为等式 (因而成立), 而当 $n=1$ 时 (4) 亦成立.

若正数 $d_{1}$ 满足对任意正整数 $n$, 皆有

$$
\sum_{i=1}^{n} x_{i}^{r} \leq n^{r-1} \cdot \sum_{i=1}^{n} d_{1}^{n-i} a_{i}^{r}
$$

由于此时 $\sum_{i=1}^{n} x_{i}^{r}=d^{n-1}$, 且 $\sum_{i=1}^{n} d_{1}^{n-i} a_{i}^{r}=n^{r-1} d_{1}^{n-1}$, 代入后整理可得

$$
\left(\frac{d}{d_{1}}\right)^{n-1} \leq n^{r-1}
$$

故必有 $\frac{d}{d_{1}} \leq 1$, 即 $d_{1} \geq d$. 这表明 (5) 中的 $d$ 不能改进为更小的正数. 证毕.
(iii) 的证明 取非负实数列 $\left\{a_{n}\right\},\left\{x_{n}\right\}$ 满足

$$
x_{1}=a_{1}=1, \quad x_{n}=(\lambda+b) \cdot \mu^{\frac{n-2}{r}}, \quad a_{n}=\lambda \cdot \mu^{\frac{n-2}{r}} \quad(n=2,3, \cdots),
$$

其中 $\lambda>0$ 为待定常数, $\mu=(\lambda+b)^{r}+1$. 注意, 这里

$$
\mu-d=\left((\lambda+b)^{r}+1\right)-\left(1+b^{r}\right)=(\lambda+b)^{r}-b^{r}>0
$$

对任意整数 $n \geq 2$, 有

$\sum_{i=1}^{n} x_{i}^{r}=1+\sum_{i=2}^{n-1}(\lambda+b)^{r} \cdot \mu^{i-2}=1+(\lambda+b)^{r} \cdot \frac{\mu^{n-2}-1}{\mu-1}=1+\left(\mu^{n-2}-1\right)=\mu^{n-2}$,故

$$
a_{n}+b \cdot\left(\sum_{i=1}^{n-1} x_{i}^{r}\right)^{\frac{1}{r}}=\lambda \cdot \mu^{\frac{n-2}{r}}+b \cdot \mu^{\frac{n-2}{r}}=x_{n}
$$

即 (4) 恰好为等式 (因而成立), 而当 $n=1$ 时 (4) 亦成立.

此时

$$
\begin{aligned}
\sum_{i=1}^{n} d^{n-i} a_{i}^{r} & =d^{n-1}+\sum_{i=2}^{n} d^{n-i} \lambda^{r} \mu^{i-2} \\
& =d^{n-1}+\lambda^{r} \cdot \frac{\mu^{n-1}-d^{n-1}}{\mu-d} \\
& =c_{\lambda} \mu^{n-1}+\left(1-c_{\lambda}\right) d^{n-1}
\end{aligned}
$$

其中 $c_{\lambda}=\frac{\lambda^{r}}{(\lambda+b)^{r}-b^{r}}>0$. 所以

$$
\frac{\sum_{i=1}^{n} d^{n-i} a_{i}^{r}}{\sum_{i=1}^{n} x_{i}^{r}}=\frac{c_{\lambda} \mu^{n-1}+\left(1-c_{\lambda}\right) d^{n-1}}{\mu^{n-1}}=c_{\lambda}+\left(1-c_{\lambda}\right)\left(\frac{d}{\mu}\right)^{n-1} .
$$

在 $r>1$ 的情况下, 由于 $(\lambda+b)^{r}=b^{r} \cdot\left(1+\frac{\lambda}{b}\right)^{r}>b^{r} \cdot\left(1+\frac{\lambda r}{b}\right)=b^{r}+\lambda r b^{r-1}$,故

$$
c_{\lambda}<\frac{\lambda^{r}}{\left(b^{r}+\lambda r b^{r-1}\right)-b^{r}}=\frac{\lambda^{r-1}}{r b^{r-1}} .
$$

对任意给定的正数 $M$, 由 (8) 知, 存在充分小的正数 $\lambda$, 使得 $c_{\lambda}<\frac{1}{2 M}$. 再注意到 $0<d<\mu$, 故存在正整数 $m$, 使得

$$
\left(1-c_{\lambda}\right)\left(\frac{d}{\mu}\right)^{m-1}<\left(\frac{d}{\mu}\right)^{m-1}<\frac{1}{2 M}
$$

从而, 对由这样的 $\lambda$ 所确定的数列 $\left\{a_{n}\right\},\left\{x_{n}\right\}$ 及正整数 $n=m,(7)$ 的右端小于 $\frac{1}{M}$, 此即 $\sum_{i=1}^{m} x_{i}^{r}>M \cdot \sum_{i=1}^{m} d^{m-i} a_{i}^{r}$. (iii) 得证.

最后讨论本研究与问题 1 的联系.

在定理中限定 $b=1, r=2$, 并结合 (ii), 可提出如下问题:
问题 2. 求最小的正数 $\lambda$, 使得当非负实数列 $\left\{x_{n}\right\},\left\{y_{n}\right\}$ 满足

$$
x_{n} \leq y_{n}+\left(\sum_{i=1}^{n-1} x_{i}^{2}\right)^{\frac{1}{2}}, \quad n=1,2, \cdots
$$

时，必有

$$
\sum_{i=1}^{n} x_{i}^{2} \leq n \cdot \sum_{i=1}^{n} \lambda^{n-i} y_{i}^{2}, \quad n=1,2, \cdots
$$

问题 2 中, $\lambda$ 的最小值为 2 . 注意到当 $r=2$ 时, (6) 在 $u, v$ 为实数的情形下亦成立, 因而若将 (9) 改成

$$
\left|x_{n}\right| \leq\left|y_{n}+\left(\sum_{i=1}^{n-1} x_{i}^{2}\right)^{\frac{1}{2}}\right|(n=1,2, \cdots)
$$

则前文的分析对 $\left\{x_{n}\right\},\left\{y_{n}\right\}$ 为实数列的情形仍是有效的. 特别地, 将问题 2 中实数列 $\left\{x_{n}\right\},\left\{y_{n}\right\}$ 的非负条件去掉, 并将 (9) 限定为等式, 便形成了问题 1 .

## 参考文献

[1] 2014 年 IMO 中国国家集训队教练组, 走向 IMO - 数学奥林匹克试题集锦 (2014)[M], 上海: 华东师范大学出版社, 2014.

[2] T.H.Gronwall, Note on the derivatives with respect to a parameter of the solutions of a system of differential equations[J], Ann. Math., 20(1919), 292296.

[3] D. Willett and J. S. W. Wong, On the discrete analogues of some generalizations of Gronwall's inequality[J], Monatsh. Math., 69(1965), 362-367.

[4] H. Alzer, Discrete analogues of a Gronwall-type inequality[J], Acta Math. Hungar., 72(1996), 209-213.

