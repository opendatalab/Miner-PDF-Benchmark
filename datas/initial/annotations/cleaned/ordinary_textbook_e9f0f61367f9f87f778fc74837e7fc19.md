# 调和级数部分和尾项的估计 

朱磊克

(江苏省苏州中学, 215000)

在估计调和数列部分和时, 一个经典的方法就是对这个调和级数按 2 的幂次分段估计, 每一段的和都可以缩放成大于 0.5 , 小于 1 . 这里就可以引出一个问题, 即:

问题 对于给定的 $n$ 项调和级数部分和, 从 $\frac{1}{n}$ 开始, 往前数多少项, 求和能刚好超过 1 ? 即使得 $\sum_{i=k}^{n} \frac{1}{i}>1$ 成立的最大的 $k$ 是多少?

本文给出了一个具体的值, 并给出了证明. 以此为基础, 给出了 2010 年高中数学联赛第三题 (不等式) 更加精确的上界.

断言 $n \geq 3$ 时, 满足 $\sum_{i=k}^{n} \frac{1}{i}>1$ 成立的最大的 $k$ 等于 $\left[\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}\right]$, 记 $m_{0}=\left[\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}\right]$, 则有

$$
\sum_{i=m_{0}+1}^{n} \frac{1}{i}<1<\sum_{i=m_{0}}^{n} \frac{1}{i}
$$

其中 $[x]$ 表示不超过 $x$ 的最大整数.

下面给出具体的证明. 为方便起见, 我们记满足条件的最大的 $k$ 为 $k_{0}$.

引理 1 对于大于 1 的整数 $k$, 下面的式子始终成立:

$$
\frac{1}{k}>\frac{1}{2} \ln \left(\frac{k+1}{k-1}\right)-\frac{1}{3(k-1) k(k+1)} .
$$

证明 考虑函数 $g(x)=\frac{1}{x}-\frac{1}{2} \ln \left(\frac{x+1}{x-1}\right)-\frac{1}{3(x-1) x(x+1)}$, 求导可得

$$
g^{\prime}(x)=-\frac{2}{3(x-1)^{2} x^{2}(x+1)^{2}}<0
$$

修订日期: 2023-08-14.
因此 $g(x)$ 在 $x \in[2,+\infty)$ 单调递减, 于是我们可以知道 $g(x)>\lim _{x \rightarrow+\infty} g(x)=0$. $x$ 取离散的整数值, 即可知道引理 1 成立.

引理 2 记 $m_{0}=\left[\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}\right]$, 则 $\sum_{k=m_{0}}^{n} \frac{1}{k}>1$.

证明 求导可知, $h(x)=\ln x(x+1)-\frac{1}{6 x(x+1)}$ 单调递增. 于是,

$$
\begin{aligned}
\sum_{k=m_{1}}^{n} \frac{1}{k}> & \sum_{k=m_{1}}^{n}\left(\frac{1}{2} \ln \left(\frac{k+1}{k-1}\right)-\frac{1}{3(k-1) k(k+1)}\right) \\
= & \ln \frac{n(n+1)}{m_{1}\left(m_{1}-1\right)}+\frac{1}{6 n(n+1)}-\frac{1}{6 m_{1}\left(m_{1}-1\right)} \\
> & \ln n(n+1)+\frac{1}{6 n(n+1)}-\ln \left(\frac{\sqrt{n(n+1)}}{e}-\frac{1}{2}\right)\left(\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}\right) \\
& -\frac{1}{6\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)} \\
= & 1+\ln \left(1+\frac{1}{4\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)}\right)+\frac{1}{6 n(n+1)}-\frac{1}{6\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)} \\
> & 1+\frac{1}{6 n(n+1)}>1 .
\end{aligned}
$$

(1) 式成立是因为

$$
\ln \left(1+\frac{\frac{1}{4}}{\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)}\right)-\frac{1}{6\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)} \geq 0
$$

对于函数

$$
t(x)=\ln \left(1+\frac{x}{4}\right)-\frac{1}{6} x, t^{\prime}(x)=\frac{1}{4+x}-\frac{1}{6}>0 \text {, }
$$

在 $x<1$ 时恒成立, 且

$$
\frac{1}{\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)}<\frac{1}{\frac{n(n+1)}{3^{2}}-\frac{1}{4}} \leq \frac{1}{\frac{4}{3}-\frac{1}{4}}<1,
$$

从而

$$
\ln \left(1+\frac{\frac{1}{4}}{\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)}\right)-\frac{1}{6\left(\frac{n(n+1)}{e^{2}}-\frac{1}{4}\right)}>\ln (1+0)-0=0 .
$$

综上可知, 引理 2 成立.

引理 $3 \frac{1}{k}<\ln \left(\frac{k+0.5}{k-0.5}\right)-\frac{1}{12 k(k+1)(k+2)}$ 对所有正整数 $k$ 成立.

证明 定义函数:

$$
f(x)=\frac{1}{x}-\ln \left(\frac{x+0.5}{x-0.5}\right)+\frac{1}{12 x(x+2)(x+1)}
$$

$$
\begin{aligned}
f^{\prime}(x) & =\frac{1}{4\left(x^{2}-0.25\right) x^{2}}-\frac{3 x^{2}+6 x+2}{12 x^{2}(x+1)^{2}(x+2)^{2}} \\
& >\frac{3(x+2)^{2}-3 x^{2}-6 x-2}{12 x^{2}(x+1)^{2}(x+2)^{2}}>0 .
\end{aligned}
$$

从而,

$$
f(x)<\lim _{x \rightarrow \infty} f(x)=0 .
$$

从而引理 3 成立.

引理 4 记 $m_{1}=\left[\frac{n+0.5}{e}+\frac{1}{2}\right]$, 则有 $\sum_{k=m_{1}+1}^{n} \frac{1}{k}<1$.

## 证明

$$
\sum_{k=m_{1}+1}^{n} \frac{1}{k}<\sum_{k=m_{1}+1}^{n} \ln \left(\frac{k+0.5}{k-0.5}\right)=\ln \frac{n+0.5}{m_{1}+0.5}<\ln \frac{n+0.5}{\frac{n+0.5}{e}+\frac{1}{2}-1+\frac{1}{2}}=1
$$

下面给出断言的证明.

证明 综合引理 2 和引理 4 , 我们可以得到:

$$
m_{0} \leq k_{0} \leq m_{1}
$$

下面我们证明： $k_{0}=m_{0}$.

直接验证可知,

| $n$ | $k_{0}$ | $\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}$ (近似值) | $m_{0}$ |
| :---: | :---: | :---: | :---: |
| 3 | 1 | 1.77 | 1 |
| 4 | 2 | 2.15 | 2 |
| 5 | 2 | 2.51 | 2 |
| 6 | 2 | 2.88 | 2 |
| 7 | 3 | 3.25 | 3 |

下面考虑 $n \geq 8$ 时, 注意到,

$$
\begin{aligned}
\frac{n+0.5}{e}-\frac{1}{2} & <\frac{n}{e}+\frac{1}{2}<\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2} \\
& <\frac{\sqrt{n(n+1)+0.25}}{e}+\frac{1}{2} \\
& =\frac{n+0.5}{e}+\frac{1}{2} .
\end{aligned}
$$

因此,

$$
m_{1}-1 \leq m_{0} \leq m_{1}
$$

情况 $1 m_{0}=m_{1}$, 结合 $(2)$ 可知, $k_{0}=m_{0}$.
情况 $2 m_{0}=m_{1}-1$. 此时, $\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}<m_{1}$.

利用引理 3 可知,

$$
\begin{aligned}
& \sum_{k=m_{0}+1}^{n} \frac{1}{k}=\sum_{k=m_{1}}^{n} \frac{1}{k}<\sum_{k=m_{1}}^{n}\left(\ln \frac{k+0.5}{k-0.5}-\frac{1}{12 k(k+1)(k+2)}\right) \\
& <\ln \frac{n+0.5}{\sqrt{n(n+1) / e}}+\frac{1}{24(n+1)(n+2)} \\
& -\frac{1}{24(\sqrt{n(n+1)} / e+1.5)(\sqrt{n(n+1)} / e+0.5)} \\
& =1+\frac{1}{2} \ln \left(1+\frac{1}{4 n(n+1)}\right) \\
& +\frac{1}{24(n+1)(n+2)}-\frac{1}{24\left(\frac{n(n+1)}{e^{2}}+2 \frac{\sqrt{n(n+1)}}{e}+0.75\right)} \\
& <1+\frac{1}{8 n(n+1)}+\frac{1}{24 n(n+1)}-\frac{4}{24 n(n+1)}=1
\end{aligned}
$$

(3) 式成立是因为 $n \geq 8$ 时, 恒有

$$
\frac{n(n+1)}{4}>\left(\frac{n(n+1)}{e^{2}}+\frac{2 \sqrt{n(n+1)}}{e}+0.75\right) .
$$

事实上, 当 $n \geq 8$ 时,

$$
\sqrt{n(n+1)}\left(\frac{1}{2}-\frac{1}{e}\right)>8 \times\left(\frac{1}{2}-\frac{1}{2.7}\right)>1
$$

移项平方后可得, (4) 式成立.

综上所述, $k_{0}=m_{0}=\left[\frac{\sqrt{n(n+1)}}{e}+\frac{1}{2}\right]$.

题 (2010 年高中数学联赛) 给定正整数 $n \geq 3$. 非负实数 $a_{1}, a_{2, \ldots}, a_{n}$ 满足 $a_{i} \leq 1, i=1,2, \ldots, n$. 记 $A_{k}=\frac{1}{k} \sum_{i=1}^{k} a_{i}, i=1,2, \ldots, n$, 求证:

$$
\left|\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}\right| \leq \frac{n+1}{2}
$$

注 原题 $a_{1}, a_{2, \cdots}, a_{n}$ 是正实数, 这里为了方便边界的值可以取到, 改成非负实数.

利用本文所得到的结论, 我们可以证明加强命题:

$$
\left[\left|\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}\right|\right]_{\max }=\left[\frac{\sqrt{n(n+1)}}{e}-\frac{1}{2}\right] .
$$

证明 记 $S=\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}$, 则 $S=\sum_{k=1}^{n} a_{k}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right)$ 是关于 $a_{k}$ 的一次函
数, 为使 $S$ 达到最大值, 当 $1-\sum_{i=k}^{n} \frac{1}{i}>0$ 时, $a_{k}=1$; 当 $1-\sum_{i=k}^{n} \frac{1}{i} \leq 0$ 时, $a_{k}=0$.

结合本文结论可知,

$$
S=\sum_{k=1}^{k_{0}} a_{k}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right)+\sum_{k=k_{0}+1}^{n} a_{k}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right) \leq \sum_{k=k_{0}+1}^{n}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right) .
$$

又，

$$
\begin{aligned}
\sum_{k=k_{0}+1}^{n}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right) & =\left(n-k_{0}-\frac{n-k_{0}}{n}-\frac{n-k_{0}-1}{n-1}-\cdots-\frac{1}{k_{0}+1}\right) \\
& =k_{0}\left(\frac{1}{n}+\frac{1}{n-1}+\cdots+\frac{1}{k_{0}+1}\right)<k_{0}, \\
\sum_{k=k_{0}+1}^{n}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right) & =k_{0}\left(\frac{1}{n}+\frac{1}{n-1}+\cdots+\frac{1}{k_{0}+1}+\frac{1}{k_{0}}-\frac{1}{k_{0}}\right) \\
& >k_{0}-\frac{k_{0}}{k_{0}}=k_{0}-1 .
\end{aligned}
$$

从而,

$$
\left[\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}\right]_{\max }=k_{0}-1
$$

又，

$$
\begin{aligned}
\sum_{k=1}^{n} A_{k}-\sum_{k=1}^{n} a_{k} & =\sum_{k=1}^{n}\left(1-a_{k}\right)-\sum_{k=1}^{n}\left(1-A_{k}\right) \\
& =\sum_{k=1}^{n}\left(1-a_{k}\right)\left(1-\sum_{i=k}^{n} \frac{1}{i}\right) \\
& \leq \sum_{k=k_{0}+1}^{n}\left(1-\sum_{i=k}^{n} \frac{1}{i}\right)<k_{0},
\end{aligned}
$$

于是,

$$
-k_{0}<\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}<k_{0}
$$

从而,

$$
\left[\left|\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}\right|\right] \leq k_{0}-1
$$

当 $1 \leq k \leq k_{0}$ 时, $a_{k}=0$, 当 $k_{0}+1 \leq k \leq n$ 时, $a_{k}=1$, 等号成立.

综上可得，

$$
\left[\left|\sum_{k=1}^{n} a_{k}-\sum_{k=1}^{n} A_{k}\right|\right]_{\max }=k_{0}-1=\left[\frac{\sqrt{n(n+1)}}{e}-\frac{1}{2}\right] .
$$

## 参考文献

[1] Villarino M B . Ramanujan's Approximation to the nth Partial Sum of the Harmonic Series[J]. Mathematics, 2004, v5.

[2] Villarino M B . Ramanujan's Harmonic Number Expansion into Negative Powers of a Triangular Number[J]. 2007.

[3] 2011 年 IMO 中国国家集训队教练组一编. 走向IMO: 数学奥林匹克试题集锦 [M]. 上海: 华东师范大学出版社, 2011,7: 035036.

