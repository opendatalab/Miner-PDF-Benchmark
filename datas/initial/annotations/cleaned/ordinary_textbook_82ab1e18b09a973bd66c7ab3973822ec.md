# Alzer 不等式的一个简证 

罗文林

(湖南师范大学附属中学, 410008)

在文 [1] 中, Alzer 证明了如下有趣的逆 Cauchy 不等式:

定理. 设 $a_{1} \geq a_{2} \geq \cdots \geq a_{n}>0, b_{1} \geq b_{2} \geq \cdots \geq b_{n}>0$. 则

$$
\sum_{i=1}^{n} a_{i} b_{i} \geq \frac{\left(\sum_{i=1}^{n} a_{i}^{2}\right)\left(\sum_{i=1}^{n} b_{i}^{2}\right)}{\max \left\{a_{1} \sum_{i=1}^{n} b_{i}, b_{1} \sum_{i=1}^{n} a_{i}\right\}}
$$

这个不等式对参加数学竞赛的学生来说被认为是一个难题. 本短文介绍我们最近找到的一个证明, 它是十分简短的.

证明 对 $n$ 用归纳法.

当 $n=1$ 时,(1) 显然成立.

假设结论对 $n-1$ 成立, 现考虑 $n$ 的情况. 由归纳假设知

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} b_{i} & =a_{1} b_{1}+\sum_{i=2}^{n} a_{i} b_{i} \\
& \geq a_{1} b_{1}+\frac{\left(\sum_{i=2}^{n} a_{i}^{2}\right)\left(\sum_{i=2}^{n} b_{i}^{2}\right)}{\max \left\{a_{2} \sum_{i=2}^{n} b_{i}, b_{2} \sum_{i=2}^{n} a_{i}\right\}}
\end{aligned}
$$

注意到 (1) 关于 $a_{1}, \cdots, a_{n}$ 和 $b_{1}, \cdots, b_{n}$ 均是齐次的, 因此不妨设 $a_{1}=1$, $b_{1}=1$, 注意到此时 $1 \geq a_{2} \geq \cdots \geq a_{n}>0,1 \geq b_{2} \geq \cdots \geq b_{n}>0$, 现记 $\sum_{i=1}^{n} a_{i}^{2}=A, \sum_{i=1}^{n} b_{i}^{2}=B, \max \left\{\sum_{i=1}^{n} a_{i}, \sum_{i=1}^{n} b_{i}\right\}=X$, 由 (2) 可得

$$
\sum_{i=1}^{n} a_{i} b_{i} \geq 1+\frac{\left(\sum_{i=2}^{n} a_{i}^{2}\right)\left(\sum_{i=2}^{n} b_{i}^{2}\right)}{\max \left\{\sum_{i=2}^{n} a_{i}, \sum_{i=2}^{n} b_{i}\right\}}=1+\frac{(A-1)(B-1)}{X-1}
$$

收稿日期: 2016-12-23; 修订日期: 2017-02-17.
因此由 (3) 知要证不等式

$$
\sum_{i=1}^{n} a_{i} b_{i} \geq \frac{A B}{X}
$$

只需证明

$$
1+\frac{(A-1)(B-1)}{X-1} \geq \frac{A B}{X}
$$

而通过简单的恒等变形知

$$
(4) \Leftrightarrow(X-A)(X-B) \geq 0 \text {. }
$$

下证 (5), 事实上

$$
\begin{aligned}
X & =\max \left\{\sum_{i=1}^{n} a_{i}, \sum_{i=1}^{n} b_{i}\right\} \geq \sum_{i=1}^{n} a_{i} \\
& =\left(\sum_{i=1}^{n} a_{i}\right) a_{1} \\
& \geq \sum_{i=1}^{n} a_{i}^{2}=A .
\end{aligned}
$$

同理 $X \geq B$. 故 (5) 成立.

这样就证明了结论对 $n$ 成立. 故定理得证.

## 参考文献

[1] Alzer H. On a converse Cauchy inequality of D. Zagier [J]. Archiv der Mathematik, 1992, 58(2): 157-159.

