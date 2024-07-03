# 一个双二次型不等式问题 

林逸沿 1 , 刘胤辰 ${ }^{2}$

(1. 浙江省温州育英国际实验学校, 325014；2. 上海市上海中学, 200231)

林逸沿提出了如下问题:

问题. 已知 $b_{1}<b_{2}<\cdots<b_{n}$ 为正实数, 求对任意满足 $a_{1}+a_{2}+\cdots+a_{n}=1$的非负实数 $a_{1} 、 a_{2} 、 \cdots 、 a_{n}$, 都有 $\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j} \leq \frac{1}{4} b_{n-1} b_{n}$ 成立的充要条件。

刘胤辰给出了充要条件并证明了如下定理:

定理. 设 $b_{1}<b_{2}<\cdots<b_{n}$ 为正实数, $n \geq 3$ 为整数. 则不等式

$$
\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j} \leq \frac{1}{4} b_{n-1} b_{n}
$$

对任意满足 $a_{1}+a_{2}+\cdots+a_{n}=1$ 的非负实数 $a_{1} 、 a_{2} 、 \cdots 、 a_{n}$ 成立的充要条件是

$$
\sum_{j=k}^{n} \frac{1}{b_{j}} \leq \frac{n-k}{b_{k}}
$$

对任意的 $k \in\{1,2, \cdots, n-2\}$ 成立.

证明. 首先证明充分性.

设 $f\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j}$, 首先说明当 $f\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 取最大值时，有 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$.

假设命题不成立, 则必然存在 $k$, 使得 $a_{k}>a_{k+1}$, 考察

$$
\begin{gathered}
f\left(a_{1}, \cdots, a_{k+1}, a_{k}, \cdots, a_{n}\right)-f\left(a_{1}, \cdots, a_{k}, a_{k+1}, \cdots, a_{n}\right) \\
\quad=\left(a_{k+1}-a_{k}\right)\left(b_{k}-b_{k+1}\right)\left(\sum_{i=1}^{k-1} b_{i} a_{i}+\sum_{i=k+2}^{n} b_{i} a_{i}\right) \leq 0
\end{gathered}
$$

这与最大性矛盾! 故当 $f\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 取最大值时, 有 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$.

于是设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 在此条件下, 我们用数学归纳法证明 (1) 式.

当 $n=3$ 时, 设 $f\left(a_{1}, a_{2}, a_{3}\right)=b_{1} b_{2} a_{1} a_{2}+b_{1} b_{3} a_{1} a_{3}+b_{2} b_{3} a_{2} a_{3}$. 在 (2) 式中取
$n=3, k=1$ 知, $\frac{1}{b_{1}}+\frac{1}{b_{2}}+\frac{1}{b_{3}} \leq \frac{2}{b_{1}}$, 即有 $b_{1}\left(b_{2}+b_{3}\right) \leq b_{2} b_{3}$, 故

$$
\begin{aligned}
f\left(a_{1}, a_{2}, a_{3}\right) & =b_{1} a_{1}\left(b_{2} a_{2}+b_{3} a_{3}\right)+b_{2} b_{3} a_{2} a_{3} \\
& \leq b_{1} a_{1}\left(b_{2}+b_{3}\right) a_{3}+b_{2} b_{3} a_{2} a_{3} \\
& \leq b_{2} b_{3} a_{1} a_{3}+b_{2} b_{3} a_{2} a_{3} \\
& =b_{2} b_{3}\left(a_{1}+a_{2}\right) a_{3} \leq \frac{1}{4} b_{2} b_{3}
\end{aligned}
$$

可知 $n=3$ 时 (1) 式成立.

假设当 $n=m$ 时 (1) 式成立, 则当 $n=m+1$ 时, 若 $a_{1}=0$, 则对 $b_{2}, b_{3}, \cdots, b_{n}$ 及 $a_{2}, a_{3}, \cdots, a_{n}$ 利用归纳假设可知 (1) 式成立; 若 $a_{1}>0$, 则考虑

$$
g\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j}-\frac{1}{4} b_{n-1} b_{n}+\lambda\left(a_{1}+a_{2}+\cdots+a_{n}-1\right)
$$

由Lagrange乘数法,

$$
\frac{\partial g}{\partial a_{i}}=b_{i} \sum_{j \neq i} b_{j} a_{j}+\lambda=0(i=1,2, \cdots, n), \frac{\partial g}{\partial \lambda}=a_{1}+\cdots+a_{n}-1
$$

设 $M=\sum_{i=1}^{n} b_{i} a_{i}$, 则

$$
\lambda=-b_{i}\left(M-a_{i} b_{i}\right)(i=1,2, \cdots, n)
$$

于是,

$$
a_{i}=\frac{M}{b_{i}}+\frac{\lambda}{b_{i}^{2}}(i=1,2, \cdots, n)
$$

故

$$
M=\sum_{i=1}^{n} b_{i} a_{i}=n M+\lambda \sum_{i=1}^{n} \frac{1}{b_{i}} \Rightarrow M=-\frac{\lambda}{n-1} \sum_{i=1}^{n} \frac{1}{b_{i}}
$$

故

$$
a_{i}=\frac{\lambda}{b_{i}}\left(\frac{1}{b_{i}}-\frac{1}{n-1} \sum_{i=1}^{n} \frac{1}{b_{i}}\right), \sum_{i=1}^{n} a_{i}=\lambda\left(\sum_{i=1}^{n} \frac{1}{b_{i}^{2}}-\frac{1}{n-1}\left(\sum_{i=1}^{n} \frac{1}{b_{i}}\right)^{2}\right)=1 .
$$

由 $a_{n} \geq a_{1}>0$ 知 $a_{n}, a_{1}>0$. 在 (2) 中取 $n=m+1, k=1$ 知, $\sum_{i=1}^{n} \frac{1}{b_{i}} \leq \frac{n-1}{b_{1}}$. 而又

$$
\frac{1}{b_{n}}<\frac{n}{(n-1) b_{n}}<\frac{1}{n-1} \sum_{i=1}^{n} \frac{1}{b_{i}} \leq \frac{1}{b_{1}}
$$

故由

$$
a_{n}=\frac{\lambda}{b_{n}}\left(\frac{1}{b_{n}}-\frac{1}{n-1} \sum_{i=1}^{n} \frac{1}{b_{i}}\right)>0
$$

知 $\lambda<0$. 但由

$$
a_{1}=\frac{\lambda}{b_{1}}\left(\frac{1}{b_{1}}-\frac{1}{n-1} \sum_{i=1}^{n} \frac{1}{b_{i}}\right)>0
$$

知 $\lambda>0$, 矛盾! 这就说明 $g\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 取到最大值时, 一定有 $a_{1}=0$, 与假设 $a_{1}>0$ 矛盾!

综上 $n=m+1$ 时 (1) 式得证, 由归纳原理知 (1) 式成立.

接下来证明必要性.

假设 (2) 式不成立, 即存在 $k \in\{1,2, \cdots, n-2\}$, 满足 $\sum_{i=k}^{n} \frac{1}{b_{i}}>\frac{n-k}{b_{k}}$.

令

$$
a_{1}=\cdots=a_{k-1}=0, a_{i}=\frac{\left(B-\frac{1}{b_{i}}\right) \frac{1}{b_{i}}}{A}(i=k, \cdots, n)
$$

其中 $A=\frac{1}{n-k}\left(\sum_{i=k}^{n} \frac{1}{b_{i}}\right)^{2}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}, \quad B=\frac{1}{n-k} \sum_{i=k}^{n} \frac{1}{b_{i}}(i=k, \cdots, n)$. 注意到

$$
B>\frac{1}{b_{k}}, A=\frac{1}{n-k}\left(\sum_{i=k}^{n} \frac{1}{b_{i}}\right)^{2}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}>\frac{1}{b_{k}} \sum_{i=k}^{n} \frac{1}{b_{i}}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}>0,
$$

故可知 $a_{i}>0(i=k, \cdots, n)$. 且

$$
\sum_{i=1}^{n} a_{i}=\sum_{i=k}^{n} a_{i}=\frac{B \sum_{i=k}^{n} \frac{1}{b_{i}}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}}{A}=\frac{A}{A}=1,
$$

则

$$
\begin{aligned}
\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j} & =\sum_{k \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j} \\
& =\frac{1}{A^{2}} \sum_{k \leq i<j \leq n}\left(B-\frac{1}{b_{i}}\right)\left(B-\frac{1}{b_{j}}\right) \\
& =\frac{1}{2 A^{2}}\left(\left(\begin{array}{c}
n-k+1 \\
2
\end{array}\right) B^{2}-(n-k)^{2} B^{2}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}\right) \\
& =\frac{1}{2 A^{2}}\left(-(n-k)(n-k-1) B^{2}+(n-k)^{2} B^{2}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}\right) \\
& =\frac{1}{2 A^{2}}\left((n-k) B^{2}-\sum_{i=k}^{n} \frac{1}{b_{i}^{2}}\right)=\frac{1}{2 A} .
\end{aligned}
$$

故 $\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j}>\frac{1}{4} b_{n-1} b_{n}$ 等价于 $\frac{1}{2 A}>\frac{1}{4} b_{n-1} b_{n}$, 即 $A<\frac{2}{b_{n-1} b_{n}}$, 亦即

$$
\left(\frac{1}{b_{n-1}}+\frac{1}{b_{n}}\right)^{2}+\frac{1}{b_{k}^{2}}+\cdots+\frac{1}{b_{n-2}^{2}}>\frac{1}{n-k}\left(\sum_{i=k}^{n} \frac{1}{b_{i}}\right)^{2},
$$

而由 Cauchy 不等式知

$$
\frac{1}{b_{k}^{2}}+\cdots+\frac{1}{b_{n-2}^{2}}+\left(\frac{1}{b_{n-1}}+\frac{1}{b_{n}}\right)^{2} \geq \frac{1}{n-k}\left(\sum_{i=k}^{n} \frac{1}{b_{i}}\right)^{2}
$$

当 $\frac{1}{b_{k}}=\cdots=\frac{1}{b_{n-2}}=\frac{1}{b_{n-1}}+\frac{1}{b_{n}}(k \leq n-2)$ 时等号成立, 而这与 $\sum_{i=k}^{n} \frac{1}{b_{i}}>\frac{n-k}{b_{k}}$ 矛盾!故可知 $\frac{1}{2 A}>\frac{1}{4} b_{n-1} b_{n}$ 成立. 于是 $\sum_{1 \leq i<j \leq n} b_{i} b_{j} a_{i} a_{j}$ 的最大值必然大于 $\frac{1}{4} b_{n-1} b_{n}$, 矛盾!
综上知 (2) 式成立, 必要性得证.

