# AMM 第 12169 号问题的解法 

刘胤辰

(上海市上海中学, 200231)

本文给出美国数学月刊 (AMM) 第 12169 号问题的一个解法.

给定整数 $n \geq 2$. 求最小的正实数 $\alpha$, 使得

$$
(n-1) \sqrt{1+\alpha \sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}}+\prod_{i=1}^{n} x_{i} \geq \sum_{i=1}^{n} x_{i}
$$

对所有非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 成立.

解 $\alpha$ 的最大值为 $\frac{1}{n-1}$.

首先令 $x_{1}=x_{2}=\cdots=x_{n-1}=a, x_{n}=0$, 则条件不等式变为

$$
(n-1) \sqrt{1+\alpha(n-1) a^{2}} \geq(n-1) a,
$$

于是 $\frac{1}{a^{2}}+\alpha(n-1) \geq 1$. 令 $a \rightarrow \infty$, 可得

$$
\alpha(n-1) \geq 1 \Rightarrow \alpha \geq \frac{1}{n-1}
$$

下证 $\alpha=\frac{1}{n-1}$ 时结论成立, 即证:

$$
(n-1) \sqrt{1+\frac{1}{n-1} \sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}}+\prod_{i=1}^{n} x_{i} \geq \sum_{i=1}^{n} x_{i}
$$

由对称性, 不妨设

$$
0 \leq x_{1} \leq x_{2} \leq \cdots \leq x_{s}<1 \leq x_{s+1} \leq \cdots \leq x_{n}
$$

若 $s=0$ 或 $s=n$, 则由贝努利不等式,

$$
\text { (1) 的左边 } \geq n-1+\prod_{i=1}^{n} x_{i} \geq \sum_{i=1}^{n} x_{i} \text {. }
$$

下设 $1 \leq s \leq n-1$. 并记

$$
A=s-\sum_{i=1}^{s} x_{i}, \quad B=\sum_{j=s+1}^{n} x_{j}-(n-s),
$$[^0]则 $A, B \geq 0$. 且

$$
\begin{aligned}
\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2} & \geq \sum_{i=1}^{s} \sum_{j=s+1}^{n}\left(x_{i}-x_{j}\right)^{2} \\
& =\sum_{i=1}^{s} \sum_{j=s+1}^{n}\left(1-x_{i}+x_{j}-1\right)^{2} \\
& =\sum_{i=1}^{s}\left(1-x_{i}\right)^{2}(n-s)+2 A B+\sum_{j=s+1}^{n}\left(x_{j}-1\right)^{2} s
\end{aligned}
$$

再由 Cauchy 不等式知，

$$
\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2} \geq \frac{(n-s) A^{2}}{s}+\frac{s B^{2}}{n-s}+2 A B
$$

(i) 若 $0 \leq A \leq 1$. 则由贝努利不等式,

$$
\begin{aligned}
\prod_{i=1}^{n} x_{i} & =\left(x_{1} \cdots x_{s}\right)\left(x_{s+1} \cdots x_{n}\right) \\
& \geq\left(x_{1}+\cdots+x_{s}-(s-1)\right)\left(x_{s+1}+\cdots+x_{n}-(n-s-1)\right) \\
& =(1-A)(B+1) .
\end{aligned}
$$

注意到 (1) 的右边 $=B-A+n$, 结合 (2), (3) 知要证 (1), 只需证

$(n-1) \sqrt{1+\frac{1}{n-1}\left(\frac{(n-s) A^{2}}{s}+\frac{s B^{2}}{n-s}+2 A B\right)}+(1-A)(B+1) \geq B-A+n$.

将上式第二项移项, 再平方, 并整理得

$$
\frac{(n-s) A^{2}}{s}+\frac{s B^{2}}{n-s} \geq \frac{A^{2} B^{2}}{n-1} .
$$

若 $A, B$ 中有一项为 0 , 则 (4) 显然成立.

下设 $A, B$ 均不为 0 . 这时 (4) 等价于

$$
\frac{(n-s)}{s B^{2}}+\frac{s}{(n-s) A^{2}} \geq \frac{1}{n-1}
$$

注意到 $s \geq 1,0<A \leq 1$ 及

$$
\frac{s}{(n-s) A^{2}} \geq \frac{1}{(n-1) A^{2}} \geq \frac{1}{n-1},
$$

故 (5) 成立.

(ii) 若 $A>1$, 则由 $\prod_{i=1}^{n} x_{i}>0$ 和 (2) 知,

$$
\text { (1) 的左边 } \geq(n-1) \sqrt{1+\frac{1}{n-1}\left(\frac{(n-s) A^{2}}{s}+\frac{s B^{2}}{n-s}+2 A B\right)}
$$

而

$$
\text { (1) 的右边 }<B+n-1 \text {. }
$$

故要证 (1) 仅需证明

$$
(n-1) \sqrt{1+\frac{1}{n-1}\left(\frac{(n-s) A^{2}}{s}+\frac{s B^{2}}{n-s}+2 A B\right)} \geq B+n-1
$$

注意到上式左边关于 $A$ 单增, 故只需证 $A=1$ 的情形:

$$
(n-1) \sqrt{1+\frac{1}{n-1}\left(\frac{(n-s)}{s}+\frac{s B^{2}}{n-s}+2 B\right)} \geq B+n-1 .
$$

两边平方并整理可知, 要证上式等价于

$$
\frac{n-s}{s}+\frac{s B^{2}}{n-s} \geq \frac{B^{2}}{n-1}
$$

由 $1 \leq s \leq n-1$ 知 $\frac{s B^{2}}{n-s} \geq \frac{B^{2}}{n-1}$, 故 (6) 成立.

综上便知 (1) 成立!


[^0]:    修订日期: 2020-04-01.

