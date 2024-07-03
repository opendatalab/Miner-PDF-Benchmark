数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 一道代数不等式的另解 

程浩宇<br>(中国人民大学附属中学, 100080)<br>指导教师: 张端阳

2018 年秋季新星数学奥林匹克的第五题是一道优雅的不等式:

设非负实数 $x_{1}, x_{2}, \cdots, x_{2018}$ 满足 $\sum_{1 \leq i<j \leq 2018} x_{i} x_{j}=1$. 求

$$
\sum_{i=1}^{2018} \frac{1}{s-x_{i}}
$$

的最小值, 其中 $s=\sum_{i=1}^{2018} x_{i}$.

文 [1] 中给出了两种解法, 并指出在 $n \geq 6$ 时方法均有效.

本文给出了另一种解法, 一并解决了 $n=3,4,5$ 时的情形. 特别 $n=3$ 时比 [2] 中两种调整法均要简便.

题目 给定整数 $n \geq 3$, 设非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{1 \leq i<j \leq n} x_{i} x_{j}=1$. 求

$$
\sum_{i=1}^{n} \frac{1}{s-x_{i}}
$$

的最小值, 其中 $s=\sum_{i=1}^{n} x_{i}$.

解 对 $1 \leq i \leq n$, 由 $x_{i}\left(s-x_{i}\right) \leq \sum_{1 \leq i<j \leq n} x_{i} x_{j}=1$, 知

$$
\frac{1}{s-x_{i}} \geq x_{i}
$$

两边同时乘以 $x_{i}$, 并对 $i$ 求和得,

$$
\sum_{i=1}^{n} \frac{x_{i}}{s-x_{i}} \geq \sum_{i=1}^{n} x_{i}^{2}=s^{2}-2
$$[^0]注意到

$$
\sum_{i=1}^{n} \frac{x_{i}}{s-x_{i}}=\sum_{i=1}^{n}\left(\frac{s}{s-x_{i}}-1\right)=s \sum_{i=1}^{n} \frac{1}{s-x_{i}}-n
$$

所以

$$
\sum_{i=1}^{n} \frac{1}{s-x_{i}} \geq s+\frac{n-2}{s} \geq 2 \sqrt{n-2} .
$$

我们来看如何取到 $2 \sqrt{n-2}$, 这需要 $\frac{x_{i}}{s-x_{i}}=x_{i}^{2}$ 和 $s=\frac{n-2}{s}$, 即 $x_{i}=0$ 或 $x_{i}\left(s-x_{i}\right)=1$, 且 $s=\sqrt{n-2}$.

假设 $x_{r}, x_{s}, x_{t}$ 均不为 0 , 其中 $1 \leq r<s<t \leq n$. 因为 $x_{s} x_{t}+x_{r}\left(s-x_{r}\right)$ 为 $\sum_{1 \leq i<j \leq n} x_{i} x_{j}$ 中的项, 所以

$$
x_{s} x_{t}+x_{r}\left(s-x_{r}\right) \leq \sum_{1 \leq i<j \leq n} x_{i} x_{j}=1=x_{r}\left(s-x_{r}\right)
$$

故 $x_{s} x_{t} \leq 0$, 与假设矛盾!

因此 $x_{1}, x_{2}, \cdots, x_{n}$ 中至少有 $n-2$ 个 0 , 不妨设 $x_{3}=\cdots=x_{n}=0$, 则 $x_{1} x_{2}=1$. 又由

$$
x_{1}+x_{2}=s=\sqrt{n-2} \text {, 且 }\left(x_{1}+x_{2}\right)^{2} \geq 4 x_{1} x_{2} \text {, }
$$

知 $n \geq 6$.

所以只有 $n \geq 6$ 时能取到 $2 \sqrt{n-2}$.

当 $n \geq 6$ 时, 取 $x_{1}=\frac{\sqrt{n-2}+\sqrt{n-6}}{2}, x_{2}=\frac{\sqrt{n-2}-\sqrt{n-6}}{2}, x_{3}=\cdots=x_{n}=0$, 此时有

$$
\sum_{i=1}^{n} \frac{1}{s-x_{i}}=2 \sqrt{n-2}
$$

故 $n \geq 6$ 时, $\sum_{i=1}^{n} \frac{1}{s-x_{i}}$ 的最小值为 $2 \sqrt{n-2}$.

下面考虑 $n=3,4,5$ 时.

由柯西不等式

$$
\left(\sum_{i=1}^{n} \frac{x_{i}}{s-x_{i}}\right)\left(\sum_{i=1}^{n}\left(s-x_{i}\right) x_{i}\right) \geq\left(\sum_{i=1}^{n} x_{i}\right)^{2}=s^{2} .
$$

又

$$
\sum_{i=1}^{n}\left(s-x_{i}\right) x_{i}=s \sum_{i=1}^{n} x_{i}-\sum_{i=1}^{n} x_{i}^{2}=s^{2}-\sum_{i=1}^{n} x_{i}^{2}=2
$$

所以

$$
\sum_{i=1}^{n} \frac{x_{i}}{s-x_{i}} \geq \frac{s^{2}}{2}
$$

即

$$
s \sum_{i=1}^{n} \frac{1}{s-x_{i}}-n \geq \frac{s^{2}}{2}
$$

所以

$$
\sum_{i=1}^{n} \frac{1}{s-x_{i}} \geq \frac{s}{2}+\frac{n}{s}
$$

注意到 (1) 式中 $\sum_{i=1}^{n} \frac{1}{s-x_{i}} \geq s+\frac{n-2}{s}$ 对于 $n=3,4,5$ 仍然成立.

下面分两种情况讨论:

(1) $s \leq 2$ 时, 由 $\sqrt{2 n}>2, \frac{s}{2}+\frac{n}{s}$ 在 $(0,2]$ 上单调递减, 所以

$$
\frac{s}{2}+\frac{n}{s} \geq 1+\frac{n}{2}
$$

(2) $s>2$ 时, 由 $\sqrt{n-2}<2, s+\frac{n-2}{s}$ 在 $[2,+\infty)$ 上单调递增, 所以

$$
s+\frac{n-2}{s}>2+\frac{n-2}{2}=1+\frac{n}{2} .
$$

故总有 $\sum_{i=1}^{n} \frac{1}{s-x_{i}} \geq 1+\frac{n}{2}$, 当 $x_{1}=x_{2}=1, x_{3}=\cdots=x_{n}=0$ 时可取到.

综上, $\sum_{i=1}^{n} \frac{1}{s-x_{i}}$ 的最小值为 $\left\{\begin{array}{ll}1+\frac{n}{2}, & n=3,4,5 \\ 2 \sqrt{n-2}, & n \geq 6\end{array}\right.$.

## 参考文献

[1] 吴尉迟, 罗振华. 2018 年秋季上海新星数学奥林匹克试题解析 $[\mathrm{J}]$, 数学新星网. 教师专栏: 2018-12-26 期.

[2] 2003 年 IMO 中国国家集训队教练组. 走向 IMO: 数学奥林匹克试题集锦. 2003[M]. 华东师范大学出版社, 2003.


[^0]:    修订日期: 2020-04-02.

