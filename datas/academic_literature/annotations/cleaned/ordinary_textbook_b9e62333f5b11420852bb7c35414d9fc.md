# 一个双二次型不等式问题的充要条件 

黄嘉俊

(北京大学, 100187)

文 [1] 证明了如下定理:

定理 1 设 $b_{1}<b_{2}<\cdots<b_{n}$ 为正实数, $n \geq 3$ 为整数. 则不等式

$$
\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j} \leq \frac{1}{4} b_{n-1} b_{n}
$$

对任意满足 $a_{1}+a_{2}+\cdots+a_{n}=1$ 的非负实数 $a_{1}, a_{2}, \cdots, a_{n}$ 成立的充要条件是

$$
\sum_{j=k}^{n} \frac{1}{b_{j}} \leq \frac{n-k}{b_{k}}
$$

对任意的 $k \in\{1,2, \cdots, n-2\}$ 成立.

本文给出了上述定理的一个改进. 下面定理中的 (3) 式与 (1) 式中 $k=n-2$时的条件等价.

定理 2 设 $b_{1}<b_{2}<\cdots<b_{n}$ 为正实数, $n \geq 3$ 为整数. 则不等式

$$
\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j} \leq \frac{1}{4} b_{n-1} b_{n}
$$

对任意满足 $a_{1}+a_{2}+\cdots+a_{n}=1$ 的非负实数 $a_{1}, a_{2}, \cdots, a_{n}$ 成立的充要条件是

$$
b_{n-2} \leq \frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}}
$$

证明 首先证明必要性.

取

$$
a_{1}=a_{2}=\cdots=a_{n-3}=0, a_{n-2}=2 t, a_{n-1}=a_{n}=\frac{1}{2}-t, 0<t<\frac{1}{2}
$$

此时 (1) 式即为

$$
2 t\left(\frac{1}{2}-t\right) b_{n-2} b_{n-1}+2 t\left(\frac{1}{2}-t\right) b_{n-2} b_{n}+\left(\frac{1}{2}-t\right)^{2} b_{n-1} b_{n} \leq \frac{1}{4} b_{n-1} b_{n}
$$

修订日期: 2020-06-15.
合并同类项两端再同除以 $t$ 得

$$
2\left(\frac{1}{2}-t\right) b_{n-2} b_{n-1}+2\left(\frac{1}{2}-t\right) b_{n-2} b_{n-1} \leq \frac{4-t}{4} b_{n-1} b_{n}
$$

令 $t \rightarrow 0^{+}$得, $b_{n-2}\left(b_{n-1}+b_{n}\right) \leq b_{n-1} b_{n}$, 必要性得证.

下证充分性. 记

$$
S=a_{1}+a_{2}+\cdots+a_{n-2}, T=a_{n-1}, U=a_{n},
$$

则 $S+T+U=1$. 易知

$$
\sum_{1 \leq i<j \leq n-2} a_{i} a_{j} \leq \frac{(n-3) S^{2}}{2(n-2)}
$$

由 $b_{i}$ 的单调性和 (3) 式知

$$
b_{i} \leq \frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}}, \forall 1 \leq i \leq n-2 .
$$

结合 (4) 式, 我们有

$$
\begin{aligned}
\sum_{1 \leq i<j \leq n-2} b_{i} b_{j} a_{i} a_{j} & \leq\left(\frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}}\right)^{2} \sum_{1 \leq i<j \leq n-2} a_{i} a_{j} \\
& \leq\left(\frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}}\right)^{2} \frac{(n-3) S^{2}}{2(n-2)} \\
& \leq\left(\frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}}\right)^{2} S^{2} .
\end{aligned}
$$

其中最后一个式子利用了 $\frac{n-3}{2(n-2)} \leq 1, \forall n \geq 3$. 又注意到,

$$
\begin{aligned}
\sum_{i=1}^{n-2} b_{i} a_{n-1} b_{n-1} a_{i}+\sum_{i=1}^{n-2} b_{i} a_{i} b_{n} a_{n} & \leq\left(\sum_{i=1}^{n-2} \frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}} a_{i}\right)\left(b_{n-1} T+b_{n} U\right) \\
& =S \cdot \frac{b_{n-1} b_{n}}{b_{n-1}+b_{n}}\left(b_{n-1} T+b_{n} U\right) \\
& =b_{n-1} b_{n} \frac{b_{n-1} S T+b_{n} S U}{b_{n-1}+b_{n}} .
\end{aligned}
$$

故要证明 (2) 式只需证:

$$
\frac{b_{n-1} b_{n}}{\left(b_{n-1}+b_{n}\right)^{2}} S^{2}+\frac{b_{n-1} S T+b_{n} S U}{b_{n-1}+b_{n}}+T U \leq \frac{1}{4}
$$

事实上,

$$
\begin{aligned}
& \frac{1}{4}(S+T+U)^{2}-\frac{b_{n-1} b_{n}}{\left(b_{n-1}+b_{n}\right)^{2}} S^{2}-\frac{b_{n-1} S T+b_{n} S U}{b_{n-1}+b_{n}}-T U \\
= & \frac{\left(b_{n-1}-b_{n}\right)^{2}}{4\left(b_{n-1}+b_{n}\right)^{2}} S^{2}+\frac{b_{n}-b_{n-1}}{2\left(b_{n-1}+b_{n}\right)} S T+\frac{b_{n-1}-b_{n}}{2\left(b_{n-1}+b_{n}\right)} S U+\frac{1}{4}(T-U)^{2} \\
= & \frac{\left(b_{n-1}-b_{n}\right)^{2}}{4\left(b_{n-1}+b_{n}\right)^{2}} S^{2}+\frac{\left(b_{n}-b_{n-1}\right)(T-U)}{2\left(b_{n-1}+b_{n}\right)} S+\frac{1}{4}(T-U)^{2}
\end{aligned}
$$

$$
=\left(\frac{b_{n}-b_{n-1}}{2\left(b_{n-1}+b_{n}\right)} S+\frac{1}{2}(T-U)\right)^{2} \geq 0
$$

充分性得证.

## 参考文献

[1] 林逸沿, 刘胤辰. 一个双二次型不等式问题 $[\mathrm{J}]$, 数学新星网. 学生专栏, 2021-06-15 期.

