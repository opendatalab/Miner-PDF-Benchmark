# Vasile Cîrtoaje 猜测的一个新证明 

俞辰捷<br>(华东师范大学第二附属中学)<br>指导教师: 唐立华

2006年, Vasile Cîrtoaje 在 Crux Math. 的 Klamkin 问题专栏 [1] 中证明了下面的结果: 设 $k$ 和 $n$ 是正整数, 且 $k<n ; a_{1}, a_{2}, \ldots, a_{n}$ 是实数, 满足 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 则不等式

$$
\left(a_{1}+a_{2}+\ldots+a_{n}\right)^{2} \geq n\left(a_{1} a_{k+1}+a_{2} a_{k+2}+\ldots+a_{n} a_{n+k}\right)
$$

对 $n=2 k$ 或 $n=4 k$ 时成立, 其中 $a_{n+j}=a_{j}, 1 \leq j \leq n$.

在 [1] 中, Cîrtoaje 进一步猜测上面的不等式对 $2<\frac{n}{k}<4$ 也成立. 2008年, 他在 Crux Math.[2] 中证明了这个猜测, 但证明过程是十分复杂的.

本文我们给出了这个猜测的一个简洁的新证明.

定理 设 $k$ 和 $n$ 是正整数, 且 $2<\frac{n}{k}<4, a_{1}, a_{2}, \ldots, a_{n}$ 是实数, 满足 $a_{1} \leq a_{2} \leq \ldots \leq$ $a_{n}$, 则

$$
\left(a_{1}+a_{2}+\ldots+a_{n}\right)^{2} \geq n\left(a_{1} a_{k+1}+a_{2} a_{k+2}+\ldots+a_{n} a_{k+n}\right)
$$

其中 $a_{n+j}=a_{j}, 1 \leq j \leq n$.

证明 我们需用到一个熟知的结论: 若实数 $a \leq x \leq b$, 则

$$
a b \leq x(a+b-x)
$$

事实上, 这等价于 $(a-x)(b-x) \leq 0$.

其次, 将每个 $a_{i}$ 同时加一个整数 $\Delta$, 并不影响结论. 这是因为 (1) 式的左边增加了

$$
(n \Delta)^{2}+2(n \Delta) \sum_{i=1}^{n} a_{i}
$$

右边增加了

$$
n \sum_{i=1}^{n}\left[\Delta^{2}+\Delta\left(a_{i}+a_{i+k}\right]=n^{2} \Delta^{2}+2 n \Delta \sum_{i=1}^{n} a_{i}\right.
$$

两边增加部分相同. 故我们不妨设 $a_{1}>0$.
(i) 若 $3 k+1 \leq n \leq 4 k-1$, 则

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} a_{i+k} & =\sum_{i=1}^{k}\left(a_{i} a_{i+k}+a_{i} a_{n+i-k}\right)+\sum_{i=k+1}^{n-2 k}\left(a_{i} a_{i+k}+a_{i+k} a_{i+2 k}\right)+\sum_{i=n-2 k+1}^{2 k} a_{i} a_{i+k} \\
& =\sum_{i=1}^{k} a_{i}\left(a_{i+k}+a_{n+i-k}\right)+\sum_{i=2 k+1}^{n-k} a_{i}\left(a_{i-k}+a_{i+k}\right)+\sum_{i=n-2 k+1}^{2 k} a_{i} a_{i+k},
\end{aligned}
$$

考虑到对 $1 \leq i \leq k$, 有

$$
a_{i} \leq a_{n-k} \leq a_{n+i-k}<a_{n+i-k}+a_{i+k}
$$

对 $2 k+1 \leq i \leq n-k$, 有

$$
a_{i} \leq a_{n-k} \leq a_{i+k}<a_{i-k}+a_{i+k},
$$

对 $n-2 k+1 \leq i \leq 2 k$, 有

$$
a_{i} \leq a_{n-k} \leq a_{i+k} .
$$

利用 (2) 式, 可得

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} a_{i+k} & \leq \sum_{i=1}^{k} a_{n-k}\left(a_{i}+a_{i+k}+a_{n+i-k}\right)+\sum_{i=2 k+1}^{n-k} a_{n-k}\left(a_{i-k}+a_{i}+a_{i+k}-a_{n-k}\right) \\
& +\sum_{i=n-2 k+1}^{2 k} a_{n-k}\left(a_{i}+a_{i+k}-a_{n-k}\right) \\
& =a_{n-k}\left(2 \sum_{i=1}^{n} a_{i}-n a_{n-k}\right) \leq \frac{1}{n}\left[\frac{n a_{n-k}+2 \sum_{i=1}^{n} a_{i}-n a_{n-k}}{2}\right]^{2} \\
& =\frac{1}{n}\left(\sum_{i=1}^{n} a_{i}\right)^{2} .
\end{aligned}
$$

(ii) 若 $2 k+1 \leq n \leq 3 k$, 则

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} a_{i+k} & =\sum_{i=1}^{k}\left(a_{i} a_{i+k}+a_{i} a_{n+i-k}\right)+\sum_{i=k+1}^{n-k} a_{i} a_{i+k} \\
& =\sum_{i=1}^{k} a_{i}\left(a_{i+k}+a_{n+i-k}\right)+\sum_{i=k+1}^{n-k} a_{i} a_{i+k} \\
& \leq \sum_{i=1}^{k} a_{n-k}\left(a_{i+k}+a_{n+i-k}+a_{i}-a_{n-k}\right)+\sum_{i=k+1}^{n-k} a_{n-k}\left(a_{i}+a_{i+k}-a_{n-k}\right) \\
& =a_{n-k}\left(2 \sum_{i=1}^{n} a_{i}-n a_{n-k}\right) \leq \frac{1}{n}\left(\sum_{i=1}^{n} a_{i}\right)^{2} .
\end{aligned}
$$

故由 (i),(ii) 知不等式 (1) 成立.

## 参考文献

[1] Vasile Cîrtoaje, Klamkin Solutions, Klamkin01-15, Crux Math.(2006),315.

[2] Vasile Cîrtoaje, Klamkin Solutions, Klamkin01-05, Crux Math.(2008),244-246.

