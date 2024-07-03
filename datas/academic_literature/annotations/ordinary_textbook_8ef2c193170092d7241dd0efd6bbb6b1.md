# 一类 “分数之和不为整数” 问题的快速证明 

施柯杰

(上海大学数学系博士生, 200444)

B.H. Brown 在 [1] 中提出了如下经典的数论问题:

题 1 . 设整数 $m, n>0$, 则和

$$
S=\frac{1}{m}+\frac{1}{m+1}+\cdots+\frac{1}{m+n}
$$

不是整数.

著名数学家柯召和孙琦编著的《初等数论 100 例》(见 [2]) 中收录了此题.我们先介绍他们的解法.

证明 设 $m+i=2^{\lambda_{i}} h_{i}, \lambda_{i} \geq 0, h_{i}$ 是奇数, $i=0,1, \cdots, n$. 因为 $m, m+$ $1, \cdots, m+n$ 中至少有一个偶数, 所以至少有一个 $i$ 使得 $\lambda_{i} \geq 1$. 设 $\lambda$ 是 $\lambda_{0}, \lambda_{1}, \cdots, \lambda_{n}$ 中最大的数, 则存在 $0 \leq k \leq n$, 使得

$$
m+k=2^{\lambda} h_{k}
$$

我们证明, 这样的 $k$ 是唯一的. 若不然, 则存在 $0 \leq k<j \leq n$, 使得

$$
m+k=2^{\lambda} h_{k}, \quad m+j=2^{\lambda} h_{j},
$$

则 $h_{k}<h_{j}$. 故有偶数 $l$ 使得 $h_{k}<l<h_{j}$. 因此在连续自然数 $m+k+1, m+k+$ $2, \cdots, m+j$ 中必有一项为

$$
2^{\lambda} l=2^{\lambda+1} \cdot \frac{l}{2}
$$

这与 $\lambda$ 的最大性矛盾. 这就证明了存在唯一的 $0 \leq k \leq n$, 使得

$$
m+k=2^{\lambda} h_{k},
$$

其中 $h_{k}$ 是奇数.

下面证明和 $S$ 不是整数. 设 $h=h_{0} \cdot h_{1} \cdots h_{n}$, 则由 $\lambda$ 的最大性与 $k$ 的唯一性, 以及 (1) 式, 得

$$
2^{\lambda-1} h S=2^{\lambda-1} h\left(\frac{1}{2^{\lambda_{0}} h_{0}}+\cdots+\frac{1}{2^{\lambda_{n}} h_{n}}\right)=M+\frac{2^{\lambda-1} h}{2^{\lambda} h_{k}}
$$

其中 $M$ 是整数. 而 $\frac{h}{h_{k}}$ 是奇数, 从而 $\frac{2^{\lambda-1} h}{2^{\lambda} h_{k}}=\frac{h}{2 h_{k}}$ 不是整数. 由 (2) 可得, 和 $S$ 不是整数.

本文将介绍一种快速解决这类分数之和不为整数问题的证明方法, 该方法源自文 [3]. 首先看下面这道关于素数倒数之和的例子.

题 2. 设 $p_{1}, p_{2}, \cdots$ 为全体素数, 满足 $2=p_{1}<p_{2}<\cdots$, 则和 $S=\sum \frac{1}{p_{r}}$ 不是整数.

分析与解 记 $S_{n}=\frac{1}{p_{1}}+\frac{1}{p_{2}}+\cdots+\frac{1}{p_{n}}$. 注意到前几项部分和:

$$
S_{1}=\frac{1}{2}, \quad S_{2}=\frac{1}{2}+\frac{1}{3}=\frac{5}{6}, \quad S_{3}=\frac{1}{2}+\frac{1}{3}+\frac{1}{5}=\frac{31}{30} .
$$

我们只需证明: 对 $n \geq 1$,

$$
S_{n}=\sum_{r=1}^{n} \frac{1}{p_{r}}=\frac{O_{n}}{E_{n}}
$$

其中 $E_{n}$ 是偶数, $O_{n}$ 是奇数. 事实上, 形如 $\frac{O_{n}}{E_{n}}$ 的任何一个有理数都不可能是整数, 故可立得 $S_{n}$ 不是整数.

当 $n=1$ 时, 由前面讨论, (3) 式成立.

假设当 $n=k$ 时, $S_{k}=\sum_{r=1}^{k} \frac{1}{p_{r}}=\frac{O_{k}}{E_{k}}$. 则

$$
S_{k+1}=\sum_{r=1}^{k+1} \frac{1}{p_{r}}=\frac{O_{k}}{E_{k}}+\frac{1}{p_{k+1}}=\frac{p_{k+1} O_{k}+E_{k}}{p_{k+1} E_{k}}
$$

由于 $p_{k+1}$ 是奇数, 则 $p_{k+1} O_{k}+E_{k}$ 也是奇数, 记为 $O_{k+1}$; 又 $p_{k+1} E_{k}$ 是偶数, 记为 $E_{k+1}$. 故当 $n=k+1$ 时, (3) 式成立.

因此对任意 $n \geq 1,(3)$ 式成立, 结论得证.

题 2 解法的关键是注意到任意一个形如上述 $\frac{O_{n}}{E_{n}}$ 的分数都不是整数, 并利用了这类分数所具有的一些基本性质. 具体地, 我们记

$$
A=\left\{\frac{r}{s}: r \text { 为奇数, } s \text { 为偶数 }\right\}, B=\left\{\frac{r}{s}: s \text { 为奇数 }\right\} .
$$

对任一有理数 $a$, 有 $a \in A$ 或者 $a \in B$ 且 $A \cap B=\emptyset$. 注意到集合 $A$ 中的元素都不是整数, 并且集合 $A, B$ 满足如下性质:

(i) 如果 $a \in A$ 且 $b \in B$, 则 $a+b \in A$;

(ii) 如果 $a \in B$ 且 $b \in B$, 则 $a+b \in B$;

(iii) 如果 $a \in A$, 则 $\frac{1}{2} a \in A$.

类似题 2 , 要证明和 $S$ 不为整数, 只需利用 (i)-(iii) 证明部分和 $S_{n} \in A$ 即可.

下面我们用此方法给出题 1 的解答.
题 1 的解法二 对任意给定的正整数 $m \geq 1$, 我们对 $n \geq 1$ 归纳证明:

$$
S_{n}=\frac{1}{m}+\frac{1}{m+1}+\cdots+\frac{1}{m+n} \in A
$$

即对任意连续的 $n$ 个正整数归纳证明, 与初始值 $m$ 无关.

当 $n=1$ 时,

$$
\frac{1}{m}+\frac{1}{m+1}=\frac{2 m+1}{m(m+1)} \in A
$$

假设当 $1 \leq n \leq k$ 时, (4) 式成立. 则当 $n=k+1$ 时, 将 $S_{k+1}$ 按分母奇偶性拆开, 得

$$
\frac{1}{m}+\frac{1}{m+1}+\cdots+\frac{1}{m+k}+\frac{1}{m+k+1}=\sum \frac{1}{2 r-1}+\sum \frac{1}{2 s} .
$$

由性质 (ii), 得 $\sum \frac{1}{2 r-1} \in B$. 再由归纳假设及性质 (iii), 有 $\sum \frac{1}{2 s} \in A$. 则由性质 (i)得, $S_{k+1} \in A$.

因此对 $m, n>0$,

$$
\frac{1}{m}+\frac{1}{m+1}+\cdots+\frac{1}{m+n} \in A
$$

结论得证.

最后, 作为练习, 请读者自行证明下面的问题.

题 3. 设 $n$ 为正整数, 证明 $S_{n}=\sum_{r=1}^{n} \frac{1}{r}$ 不是整数.

## 参考文献

[1] B.H. Brown, Problems for solution: E46 [J], Amer. Math. Monthly. 40(1933), 360-361

[2] 柯召, 孙琦, 初等数论 100 例 [M], 哈尔滨工业大学出版社, 2011, 2-3.

[3] N. Lord, Quick proofs that certain sums of fractions are not integers [J], Math. Gaz. 99(2015), 128-130.

