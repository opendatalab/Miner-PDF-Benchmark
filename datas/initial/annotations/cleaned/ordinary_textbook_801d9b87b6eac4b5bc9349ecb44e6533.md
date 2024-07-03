# 2021 年第二届百年老校数学竞赛试题解答 

王彬

(中国科学院数学与系统科学研究院, 100190)

第二届百年老校数学竞赛于 2021 年 8 月 1 日至 5 日在浙江省宁波中学举行. 下面介绍本次考试试题及解答.

## I. 试题

1. 某班有10名同学计划在暑假举行若干次聚会, 要求每名同学至多参加三次聚会, 并且任意两名同学至少在一次聚会中相遇.

求最大的正整数 $m$, 使得无论如何安排符合上述要求的聚会, 都一定存在某次聚会有至少 $m$ 名同学参加.

(清华附中王彗兴供题)

2. 求最大的实数 $\lambda$, 使得不等式

$$
\sum_{k=1}^{n} x_{k}^{3}\left(x_{k}-x_{k-1}\right) \geq \frac{1}{4}+\frac{\lambda}{n}
$$

对任意正整数 $n$ 以及任意实数 $0=x_{0} \leq x_{1} \leq x_{2} \leq \cdots \leq x_{n}=1$ 均成立.

(宁波中学顾寅 供题)

3. 给定正整数 $L$. 记

$$
a_{n}=L+1 !+2 !+\cdots+n !, \quad n=1,2,3, \cdots .
$$

证明：对任意素数 $p>20210802$, 存在无穷多个非负整数对 $(m, k)$, 满足 $a_{m+1}, a_{m+2}, \ldots, a_{m+100}$ 这 100 个数都能被 $p^{k}$ 整除, 并且都不能被 $p^{k+1}$ 整除.

(苏州中学 朱否克供题)

4. 已知素数 $p, q$ 满足 $p=2 q+1$.

证明: 存在正整数 $m$ 使得 $m p$ 的十进制表示的各位数字之和是 2 或 3 .

(清华附中 黄鹤 供题)

5. 如图, $\odot O$ 是 $\triangle A B C$ 的外接圆, $D$ 是弧 $\widehat{B C}$ (不含 $A$ ) 上一点, $S$ 为弧 $\widehat{B A C}$ 的中点. $P$ 为线段 $S D$ 上一点, 过 $P$ 作 $D B$ 的平行线交 $A B$ 于点 $E$, 过 $P$ 作 $D C$ 的平行线交 $A C$ 于点 $F$, 过 $O$ 作 $S D$ 的平行线交弧 $\widehat{B D C}$ 于点 $T$.已知 $\odot O$ 上的点 $Q$ 满足 $\angle Q A P$ 被 $A T$ 平分.

证明: $Q E=Q F$.

(南京师大附中 王子扬 供题)



6. 给定素数 $p \geq 5$. 称 $1,2, \cdots, p$ 的排列 $a_{1}, a_{2}, \cdots, a_{p}$ 为 “好排列”, 如果对 $k=1,2, \cdots, p$ 均有 $a_{k} \neq k$, 并且 $a_{1}+2 a_{2}+\cdots+p a_{p}$ 是 $p$ 的倍数.

求 “好排列” 的个数除以 $p^{2}-p$ 的余数.

(镇海中学 沈虎跃 供题)

## II. 解答

1. 某班有10名同学计划在暑假举行若干次聚会, 要求每名同学至多参加三次聚会, 并且任意两名同学至少在一次聚会中相遇.

求最大的正整数 $m$, 使得无论如何安排符合上述要求的聚会, 都一定存在某次聚会有至少 $m$ 名同学参加.

解. 设有 $n$ 次聚会, 聚会人数分别为 $x_{1}, x_{2}, \ldots, x_{n}$ (均为正整数). 我们有:

$$
\begin{gathered}
x_{1}+x_{2}+\cdots+x_{n} \leq 10 \times 3=30 \\
\left(\begin{array}{c}
x_{1} \\
2
\end{array}\right)+\left(\begin{array}{c}
x_{2} \\
2
\end{array}\right)+\cdots+\left(\begin{array}{c}
x_{n} \\
2
\end{array}\right) \geq\left(\begin{array}{c}
10 \\
2
\end{array}\right)=45
\end{gathered}
$$

记 $S_{1}=x_{1}+\cdots+x_{n}, S_{2}=x_{1}^{2}+\cdots+x_{n}^{2}$, 则 $S_{2}-S_{1} \geq 90$ 可知 $S_{2} \geq 4 S_{1}$, 即

$$
\max \left\{x_{1}, \ldots, x_{n}\right\} \geq \frac{x_{1}^{2}+\cdots+x_{n}^{2}}{x_{1}+\cdots+x_{n}} \geq 4
$$

若上式等号成立, 则必须 $x_{1}=\cdots=x_{n}=4$, 并且 $S_{1}=x_{1}+\cdots+x_{n}=30$,这样可得 $n=7.5$ 导致矛盾. 所以我们有 $\max \left\{x_{1}, \ldots, x_{n}\right\} \geq 5$, 即一定存在某次聚会有至少 5 名同学参加, 即 $m=5$ 满足题意.

另一方面, 我们给出 10 名同学参加聚会的一种安排方式: 共 $A, B, C, D, E, F$六次聚会, 每次聚会恰好有 5 名同学参加, 下面的 10 个三元子集分别表示 10 名同学各参加哪三次聚会:

$$
\begin{aligned}
& \{A B C\},\{C D E\},\{A E F\},\{B D F\},\{A B D\}, \\
& \{A D E\},\{B C E\},\{B E F\},\{C D F\},\{A C F\}
\end{aligned}
$$

易知 $A, B, C, D, E, F$ 中的每一个在上述 10 个三元子集中恰好出现 5 次, 并且这 10 三元子集两两相交 (因为 10 对互补的三元子集均恰好出现一个). 即每次聚会都恰好有 5 名同学参加, 并且任意两名同学至少在一次聚会中相遇. 这意味着 $m \geq 6$ 不满足题意.

因此所求的最大正整数 $m$ 是 5 .

注记. 另一种构造

$$
\begin{aligned}
& \{A B C\},\{A B C\},\{B E F\},\{B E F\},\{C D F\}, \\
& \{C D F\},\{A B D\},\{A E F\},\{A D E\},\{C D E\} .
\end{aligned}
$$

2. 求最大的实数 $\lambda$, 使得不等式

$$
\sum_{k=1}^{n} x_{k}^{3}\left(x_{k}-x_{k-1}\right) \geq \frac{1}{4}+\frac{\lambda}{n}
$$

对任意正整数 $n$ 以及任意实数 $0=x_{0} \leq x_{1} \leq x_{2} \leq \cdots \leq x_{n}=1$ 均成立.

解法一. 设 $A=\sum_{k=1}^{n} x_{k}^{3}\left(x_{k}-x_{k-1}\right), B=\sum_{k=1}^{n} x_{k-1}^{3}\left(x_{k}-x_{k-1}\right)$, 则

$$
\begin{aligned}
A+B & =\sum_{k=1}^{n}\left(x_{k}^{3}+x_{k-1}^{3}\right)\left(x_{k}-x_{k-1}\right) \\
& \geq \frac{1}{2} \sum_{k=1}^{n}\left(x_{k}^{3}+x_{k}^{2} x_{k-1}+x_{k} x_{k-1}^{2}+x_{k-1}^{3}\right)\left(x_{k}-x_{k-1}\right) \\
& =\frac{1}{2} \sum_{k=1}^{n}\left(x_{k}^{4}-x_{k-1}^{4}\right)=\frac{1}{2} .
\end{aligned}
$$

$$
\begin{aligned}
A-B & =\sum_{k=1}^{n}\left(x_{k}^{3}-x_{k-1}^{3}\right)\left(x_{k}-x_{k-1}\right) \\
& =\sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right)^{2}\left(x_{k}^{2}+x_{k} x_{k-1}+x_{k-1}^{2}\right) \\
& \geq \frac{3}{4} \sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right)^{2}\left(x_{k}^{2}+2 x_{k} x_{k-1}+x_{k-1}^{2}\right) \\
& =\frac{3}{4} \sum_{k=1}^{n}\left(x_{k}^{2}-x_{k-1}^{2}\right)^{2} \\
& \geq \frac{3}{4} \times \frac{1}{n}\left(\sum_{k=1}^{n}\left(x_{k}^{2}-x_{k-1}^{2}\right)\right)^{2}=\frac{3}{4} \times \frac{1}{n} .
\end{aligned}
$$

所以 $A \geq \frac{1}{4}+\frac{3}{8} \times \frac{1}{n}$, 即 $\lambda=\frac{3}{8}$ 满足题目要求.

另一方面, 我们取 $x_{k}=\sqrt{\frac{k}{n}}, k=0,1, \ldots, n$. 此时

$$
\begin{aligned}
A+B-\frac{1}{2} & =\frac{1}{2} \sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right)^{2}\left(x_{k}^{2}-x_{k-1}^{2}\right)=\frac{1}{2 n} \sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right)^{2} \\
& \leq \frac{1}{2 n} \times \max _{k}\left\{\left(x_{k}-x_{k-1}\right)\right\}=\frac{1}{2 n} \times\left(x_{1}-x_{0}\right)=\frac{1}{2 n \sqrt{n}} \\
A-B-\frac{3}{4} \times \frac{1}{n} & =\frac{1}{4} \sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right)^{4} \leq \frac{1}{4} \times \max _{k}\left\{\left(x_{k}-x_{k-1}\right)^{3}\right\}=\frac{1}{4} \frac{1}{n \sqrt{n}}
\end{aligned}
$$

即此时我们有 $A \leq \frac{1}{4}+\frac{3}{8} \times \frac{1}{n}+\frac{3}{8} \times \frac{1}{n \sqrt{n}}$, 这样满足题意的 $\lambda$ 需要满足

$$
\frac{1}{4}+\frac{3}{8} \times \frac{1}{n}+\frac{3}{8} \times \frac{1}{n \sqrt{n}} \geq A \geq \frac{1}{4}+\frac{\lambda}{n} \Rightarrow \lambda \leq \frac{3}{8}+\frac{3}{8 \sqrt{n}}
$$

对所有正整数 $n$ 均成立. 故 $\lambda \leq \frac{3}{8}$, 即满足题目要求的最大实数 $\lambda$ 是 $\frac{3}{8}$.

注记.一般的, 对于区间 $[0,1]$ 的下凸函数 $f(x)$, 我们有

$$
A=\sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right) \times f\left(x_{k}\right) \geq \int_{0}^{1} f(x) \mathrm{d} x+\frac{1}{2 n} \times\left(\int_{0}^{1} \sqrt{f^{\prime}(x)} \mathrm{d} x\right)^{2} .
$$

我们取 $B=\sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right) \times f\left(x_{k-1}\right)$, 由凸性有: $A+B \geq 2 \int_{0}^{1} f(x) \mathrm{d} x$.以及

$$
\begin{aligned}
n(A-B) & =n \sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right)\left(f\left(x_{k}\right)-f\left(x_{k-1}\right)\right) \\
& \geq\left(\sum_{k=1}^{n} \sqrt{\left(x_{k}-x_{k-1}\right)\left(f\left(x_{k}\right)-f\left(x_{k-1}\right)\right)}\right)^{2} \\
& =\left(\sum_{k=1}^{n} \sqrt{\left(x_{k}-x_{k-1}\right) \int_{x_{k-1}}^{x_{k}} f^{\prime}(x) \mathrm{d} x}\right)^{2} \\
& \geq\left(\sum_{k=1}^{n} \int_{x_{k-1}}^{x_{k}} \sqrt{f^{\prime}(x)} \mathrm{d} x\right)^{2}=\left(\int_{0}^{1} \sqrt{f^{\prime}(x)} \mathrm{d} x\right)^{2} .
\end{aligned}
$$

特别的, 当 $f(x)=x^{m}$ 时, $\int_{0}^{1} f(x) \mathrm{d} x=\frac{1}{m+1}, \int_{0}^{1} \sqrt{f^{\prime}(x)} \mathrm{d} x=\frac{2 \sqrt{m}}{m+1}$, 我们有

$$
\sum_{k=1}^{n}\left(x_{k}-x_{k-1}\right) \times x_{k}^{m} \geq \frac{1}{m+1}+\frac{2 m}{(m+1)^{2}} \times \frac{1}{n}
$$

解法二. 固定正整数 $n$, 对任意的实数 $0=x_{0} \leq x_{1} \leq x_{2} \leq \cdots \leq x_{n}=1$, 设 $\sum_{k=1}^{n} x_{k}^{3}\left(x_{k}-x_{k-1}\right)$ 的最小值为 $A_{n}$.

考虑 $A_{n}$ 与 $A_{n-1}$ 的递推关系, 记 $y=x_{n-1}, y_{k}=\frac{x_{k}}{x_{n-1}}=\frac{x_{k}}{y}, k=1,2, \ldots, n-$ 1 , 则

$$
\sum_{k=1}^{n} x_{k}^{3}\left(x_{k}-x_{k-1}\right)=1-y+y^{4} \sum_{k=1}^{n-1} y_{k}^{3}\left(y_{k}-y_{k-1}\right) .
$$

因此

$$
A_{n}=\max _{y}\left\{(1-y)+y^{4} \times A_{n-1}\right\}=1-\frac{3}{4} \times \frac{1}{\sqrt[3]{4 A_{n-1}}} .
$$

题目所需的 $\lambda$ 是对任意正整数 $n$ 都有: $A_{n} \geq \frac{1}{4}+\frac{\lambda}{n}$, 即 $B_{n}=\frac{1}{4 A_{n}-1} \leq \frac{n}{4 \lambda}$对任意 $n$ 成立. $A_{1}=1, B_{1}=\frac{1}{3}$, 我们看看 $B_{n}$ 的变化情况.

$$
\begin{aligned}
B_{n} & =\frac{1}{4 A_{n}-1}=\frac{1}{3-3 \frac{1}{\sqrt[3]{4 A_{n-1}}}}=\frac{\sqrt[3]{4 A_{n-1}}}{3\left(\sqrt[3]{4 A_{n-1}}-1\right)} \\
& =\frac{\sqrt[3]{4 A_{n-1}}\left(1+\sqrt[3]{4 A_{n-1}}+\left(\sqrt[3]{4 A_{n-1}}\right)^{2}\right)}{3\left(4 A_{n-1}-1\right)} \\
& =\frac{1}{4 A_{n-1}-1}+\frac{\sqrt[3]{4 A_{n-1}}+\left(\sqrt[3]{4 A_{n-1}}\right)^{2}+4 A_{n-1}-3}{3\left(4 A_{n-1}-1\right)} \quad\left(\text { 记 } t=\sqrt[3]{4 A_{n-1}}\right) \\
& =\frac{1}{4 A_{n-1}-1}+\frac{t+t^{2}+t^{3}-3}{3\left(t^{3}-1\right)}=B_{n-1}+\frac{t^{2}+2 t+3}{3\left(t^{2}+t+1\right)}
\end{aligned}
$$

即 $\left\{B_{n}\right\}$ 数列的增量

$$
B_{n}-B_{n-1}=\frac{t^{2}+2 t+3}{3\left(t^{2}+t+1\right)} \in\left[\frac{1}{3}, \frac{2}{3}\right], \quad \text { 因为 } t=\sqrt[3]{4 A_{n-1}}>1
$$

这样由归纳法易得 $B_{n}<\frac{2 n}{3}$, 即 $\lambda=\frac{3}{8}$ 满足题意.

另一方面, 当 $n$ 充分大时, $B_{n}$ 无界增长, $A_{n}$ 接近于 $\frac{1}{4}, t=\sqrt[3]{4 A_{n-1}}$ 接近于 1 , 增量 $B_{n}-B_{n-1}$ 接近于 $\frac{2}{3}$. 即对任意的 $\alpha<\frac{2}{3}$, 当 $n$ 足够大时都有 $B_{n}-B_{n-1}>\frac{\alpha}{2}+\frac{1}{3}$, 这样 $B_{n}>\alpha n$ 对充分大的 $n$ 成立.

因此当 $\lambda>\frac{3}{8}$ 即 $\frac{1}{4 \lambda}<\frac{2}{3}$ 时, 对充分大的 $n$ 有 $B_{n}>\frac{n}{4 \lambda}$, 即这样的 $\lambda$ 不合题意.

因此满足题目要求的最大实数 $\lambda$ 是 $\frac{3}{8}$.

3. 给定正整数 $L$. 记

$$
a_{n}=L+1 !+2 !+\cdots+n !, \quad n=1,2,3, \cdots .
$$

证明：对任意素数 $p>20210802$, 存在无穷多个非负整数对 $(m, k)$, 满足 $a_{m+1}, a_{m+2}, \ldots, a_{m+100}$ 这 100 个数都能被 $p^{k}$ 整除, 并且都不能被 $p^{k+1}$ 整除.

证. 对素数 $p$ 与正整数 $n$, 记 $\nu_{p}(n)$ 为满足 $p^{k} \mid n$ 的最大非负整数 $k$.

题目所证即数列 $\left\{a_{n}\right\}$ 中有无穷多个长为 100 的段 $\left(a_{m+1}, a_{m+2}, \ldots, a_{m+100}\right)$有相同的 $\nu_{p}(\cdot)$ 值. 我们证明

引理. 对任意正整数 $N, A_{N}=\left\{a_{p N-1}, a_{p N}, a_{p N+1}, \ldots, a_{p N+p-1}\right\}$ 中存在脚标连续的 100 个数有相同的 $\nu_{p}(\cdot)$ 值.

我们记 $\beta=\beta_{N}=\nu_{p}\left((p N)\right.$ !), 即 $A_{N}$ 中的 $p+1$ 个数模 $p^{\beta}$ 同余.

若 $\nu_{p}\left(a_{p N-1}\right)<\beta$, 则对任意 $m \geq p N$ 均有 $\nu_{p}\left(a_{m}\right)=\nu_{p}\left(a_{p N-1}\right)$, 引理成立.

若 $\nu_{p}\left(a_{p N-1}\right) \geq \beta$, 则 $A_{N}$ 中的数都被 $p^{\beta}$ 整除. 设 $A_{N}$ 中被 $p^{\beta+1}$ 整除的数依次为 $a_{t_{1}}, a_{t_{2}}, \ldots, a_{t_{l}}$. 其中 $p N-1 \leq t_{1}<t_{2}<\cdots<t_{l} \leq p N+p-1$. 若引理不成立, 则 $t_{i+1}-t_{i} \leq 100, i=1,2, \ldots, l-1$, 以及 $t_{1} \leq p N+99, t_{l} \geq p N+p-100$.

对某个 $i=1,2, \ldots, l-1$, 记 $t_{i+1}-t_{i}=k$, 我们考虑:

$$
\begin{aligned}
a_{t_{i+1}}-a_{t_{i}}= & \left(t_{i}+1\right) !+\left(t_{i}+2\right) !+\cdots+\left(t_{i}+k\right) ! \\
= & \left(t_{i}+1\right) ! \times\left[1+\left(t_{i}+2\right)+\left(t_{i}+2\right)\left(t_{i}+3\right)\right. \\
& \left.+\cdots+\left(t_{i}+2\right)\left(t_{i}+3\right) \ldots\left(t_{i}+k\right)\right]
\end{aligned}
$$

由 $p N \leq t_{i}+1 \leq p N+p-1$, 可知 $\nu_{p}\left(\left(t_{i}+1\right) !\right)=\nu_{p}((p N) !)=\beta$ ，

因此 $p^{\beta+1} \mid a_{t_{i+1}}-a_{t_{i}}=a_{t_{i}+k}-a_{t_{i}}$ 意味着

$$
p \mid 1+\left(t_{i}+2\right)+\left(t_{i}+2\right)\left(t_{i}+3\right)+\cdots+\left(t_{i}+2\right)\left(t_{i}+3\right) \ldots\left(t_{i}+k\right) .
$$

我们考虑多项式序列

$$
\begin{gathered}
f_{1}(t)=1, f_{2}(t)=1+(t+2), f_{3}(t)=1+(t+2)+(t+2)(t+3), \\
f_{k}(t)=1+(t+2)+(t+2)(t+3)+\cdots+(t+2)(t+3) \ldots(t+k), k=2,3, \ldots
\end{gathered}
$$

我们得到: 若 $t_{i+1}-t_{i}=k$ 则 $f_{k}\left(t_{i}\right) \equiv 0(\bmod p)$.

注意到 $f_{k}(t)$ 是关于 $k-1$ 次首一多项式. 由拉格朗日定理, 即有限域 $F_{p}$ 上的多项式的根的个数不超过该多项式的次数, 因此在模 $p$ 意义下至多有 $k-1$ 个 $t$ 使得 $f_{k}(t) \equiv 0(\bmod p)$. 即 $t_{i+1}-t_{i}=k$ 的情况至多出现 $k-1$ 次.

这就意味着 $t_{2}-t_{1}, t_{3}-t_{2}, \ldots, t_{l}-t_{l-1}$ 这些数的分布情况是:

没有 1 ，至多有一个 2 , 至多有两个 $3, \ldots$, 至多有 $k-1$ 个 $k, \ldots$, 至多有 99 个 100 , 没有 101 以上的. 这样

$$
t_{l}-t_{1}=\sum_{i=1}^{l-1}\left(t_{i+1}-t_{i}\right) \leq 0 \times 1+1 \times 2+\cdots+99 \times 100=\frac{99 \times 100 \times 101}{3}
$$

$$
t_{l}-t_{1} \geq(p N+p-100)-(p N+99)=p-199
$$

所以 $p \leq 333300+199<333500$. 这与题设 $p>20210802$ 矛盾, 这意味着对任意的正整数 $N, p+1$ 元组 $a_{p N-1}, a_{p N}, a_{p N+1}, \ldots, a_{p N+p-1}$ 中存在脚标连续的 100 个数的 $\nu_{p}(\cdot)$ 值相同. 因此符合题意的 $(m, k)$ 有无穷多对.

4. 已知素数 $p, q$ 满足 $p=2 q+1$.

证明: 存在正整数 $m$ 使得 $m p$ 的十进制表示的各位数字之和是 2 或 3 .

证. $p=2,3$ 不合题意, 若 $p=5$ 则取 $m p=20$ 即可. 下面假设 $p \geq 7$.

由费马小定理 $p \mid 10^{p-1}-1=10^{2 q}-1=\left(10^{q}+1\right)\left(10^{q}-1\right)$ 可知 $p \mid 10^{q}+1$或 $p \mid 10^{q}-1$. 前者意味着取 $m p=10^{q}+1$ 满足条件. 若是 $p \mid 10^{q}-1$, 我们断言 $A=\left\{10^{0}, 10^{1}, 10^{2}, \ldots, 10^{q-1}\right\}$ 中的数模 $p$ 两两不同余, 即有 $q$ 个不同的余数.

这是因为若有 $10^{a} \equiv 10^{b}(\bmod p),(0 \leq a<b \leq q-1)$ 则 $10^{b-a} \equiv 1$ $(\bmod p)$, 由 $b-a$ 与 $q$ 互素以及裴蜀定理知存在正整数 $u, v$ 使得 $u(b-a)-v q=1$,这样

$$
1 \equiv\left(10^{b-a}\right)^{u}=10^{v q+1}=\left(10^{q}\right)^{v} \times 10 \quad(\bmod p)
$$

这意味着 $p \mid 10-1=9$ 即 $p=3$, 不合题意. 因此 $A=\left\{10^{0}, 10^{1}, 10^{2}, \ldots, 10^{q-1}\right\}$中的数模 $p$ 两两不同余. 设它们的余数是 $B=\left\{r_{1}, r_{2}, \ldots, r_{q}\right\} \subseteq\{1,2, \ldots, p-1\}$.

考虑 $\frac{p-5}{2}$ 个抽屉, 它们覆盖了除了 $\left\{0,1, \frac{p-1}{2}, p-2, p-1\right\}$ 之外的所有余数:

$$
\{2, p-3\},\{3, p-4\}, \ldots,\left\{\frac{p-3}{2}, \frac{p+1}{2}\right\}
$$

若某个抽屉里的两个余数都在 $B$ 中出现, 不妨设 $10^{a} \equiv k, 10^{b} \equiv p-1-k$ , 则 $m p=10^{a}+10^{b}+1$ 是 $p$ 的倍数, 满足题意.

若每个抽屉里的余数均在 $B$ 至多出现一个的话, 由于 $|B|=\frac{p-1}{2}$, 所以 $\left\{0,1, \frac{p-1}{2}, p-2, p-1\right\}$ 在 $B$ 中出现至少两个, 已知 $1 \in B, 0 \notin B$, 因此其余三个余数 $\frac{p-1}{2}, p-2, p-1$ 至少有一个在 $B$ 中出现.

若 $\frac{p-1}{2} \in B$, 即有某个 $10^{a} \equiv \frac{p-1}{2}$, 则 $m p=2 \times 10^{a}+1$ 满足题意.

若 $p-2 \in B$, 即有某个 $10^{a} \equiv p-2$, 则 $m p=10^{a}+2$ 满足题意.

若 $p-1 \in B$, 有某个 $10^{a} \equiv p-1$, 则 $m p=10^{a}+1$ 满足题意.

综上所述, 存在 $p$ 的倍数的十进制数字和是 2 或 3 .

注记. 我们有更一般的结论:

若素数 $p, q$ 满足 $p=k q+1$. 则存在某个 $p$ 的倍数的十进制表示的各位数字之和不超过 $k+1$.

5. 如图, $\odot O$ 是 $\triangle A B C$ 的外接圆, $D$ 是弧 $\widehat{B C}$ (不含 $A)$ 上一点, $S$ 为弧 $\widehat{B A C}$ 的中点. $P$ 为线段 $S D$ 上一点, 过 $P$ 作 $D B$ 的平行线交 $A B$ 于点 $E$, 过 $P$ 作 $D C$ 的平行线交 $A C$ 于点 $F$, 过 $O$ 作 $S D$ 的平行线交弧 $\widehat{B D C}$ 于点 $T$.已知 $\odot O$ 上的点 $Q$ 满足 $\angle Q A P$ 被 $A T$ 平分.

证明: $Q E=Q F$.



证. 设 $O T, S D$ 分别与 $B C$ 交于点 $K, L$.

由 $\angle A E P+\angle A F P=\angle A B D+\angle A C D=\pi$ 知 $A, E, P, F$ 共圆.

由 $\angle A S P=\angle A C D=\angle A F P$ 知 $S, A, P, F$ 共圆, 即 $S, A, E, P, F$ 五点共圆.

注意 $\angle S E F=\angle S A F=\angle S B C$, 同理 $\angle S F E=\pi-\angle S A E=\angle S C B$ 可知 $\triangle S E F$ 与 $\triangle S B C$ 相似. 因此 $\frac{S E}{S F}=\frac{S B}{S C}$, 即 $S E=S F$.

$$
\begin{aligned}
2 \angle T A C & =\angle T O C=\angle T K C-\angle K C O=\angle D L C-\left(\frac{\pi}{2}-\angle A\right) \\
& =\angle D B C+\angle B D S-\left(\frac{\pi}{2}-\angle A\right)=\angle D S C+\left(\frac{\pi-\angle A}{2}\right)-\left(\frac{\pi}{2}-\angle A\right) \\
& =\angle D S C+\frac{1}{2} \angle A .
\end{aligned}
$$

由 $A T$ 平分 $\angle Q A P$ 可知:

$\angle Q A C=2 \angle T A C-\angle P A C=\angle D S C+\frac{1}{2} \angle A-\angle P S F=\frac{1}{2} \angle A+\angle F S C$.
因此

$$
\angle Q S F=\angle Q S C-\angle F S C=\angle Q A C-\angle F S C=\frac{1}{2} \angle A=\frac{1}{2} \angle E S F .
$$

即 $Q S$ 是 $\angle E S F$ 的平分线, 结合 $S E=S F$ 可知 $S Q$ 是 $E F$ 的垂直平分线,故 $Q E=Q F$.

6. 给定素数 $p \geq 5$. 称 $1,2, \cdots, p$ 的排列 $a_{1}, a_{2}, \cdots, a_{p}$ 为 “好排列”, 如果对 $k=1,2, \cdots, p$ 均有 $a_{k} \neq k$, 并且 $a_{1}+2 a_{2}+\cdots+p a_{p}$ 是 $p$ 的倍数.

求 “好排列” 的个数除以 $p^{2}-p$ 的余数.

解. 把排列看成是 $P=\{1,2, \ldots, p\}$ 到自身的置换(一一映射) $f: P \mapsto P$. “好排列” 即没有不动点(即对 $x=1,2, \cdots, p$ 均有 $f(x) \neq x$ ), 且 $S(f)=$ $\sum_{x=1}^{p} x f(x) \equiv 0$ 的好置换 $f$. (本题所有同余均为 $\bmod p$ 意义).

设所有好置换构成集合 $M$. 我们按照 $f(p)$ 的取值把 $M$ 分成 $p-1$ 个部分

$$
M=B_{1} \bigcup B_{2} \bigcup \cdots \bigcup B_{p-1}, \quad B_{k}=\{f \in M, f(p)=k\}, k=1,2, \ldots, p-1
$$

我们想实现 $B_{k}$ 之间的对应, 为此考虑对置换 $f$ 进行操作:

$$
T_{a}(f)(x) \equiv a^{-1} f(a x), a=1,2, \ldots, p-1
$$

其中 $a^{-1}$ 表示 $a$ 模 $p$ 的数论倒数.

若 $f \in M$, 即 $f$ 没有不动点并且 $S(f) \equiv 0$, 则 $T_{a}(f)$ 亦没有不动点, 同时

$$
S\left(T_{a}(f)\right) \equiv \sum_{k=1}^{p} k a^{-1} f(a k) \equiv a^{-2} \sum_{k=1}^{p}(a k) \times f(a k) \equiv a^{-2} S(f) \equiv 0 .
$$

所以 $T_{a}(f) \in M$.

并且若 $f \in B_{k}$, 则 $T_{a}(f) \in B_{a^{-1} k}$. 这样以来我们就找到了 $B_{k} \mapsto B_{a^{-1} k}$ 的单射, 于是 $\left|B_{1}\right|=\left|B_{2}\right|=\cdots=\left|B_{p-1}\right|$, 因而 $|M|$ 是 $(p-1)$ 的倍数.

另一方面, 我们考虑另一种操作: $R(f)(x)=f(x+1)-1$.

若 $f \in M$, 即 $f$ 没有不动点并且 $S(f) \equiv 0$, 则 $R(f)$ 亦没有不动点, 同时

$$
\begin{aligned}
S(R(f)) & =\sum_{k=1}^{p} k[f(k+1)-1]=\sum_{k=1}^{p}[(k+1) f(k+1)-f(k+1)-k] \\
& =S(f)-\sum_{k=1}^{p} f(k)-\sum_{k=1}^{p} k \equiv S(f) \equiv 0 .
\end{aligned}
$$

所以 $R(f) \in M$.

由于 $R$ 操作是以 $p$ 为周期的, 即 $R^{(p)}(f)=f$, 所以我们考虑 $f \in M$ 在 $R$操作下的最小正周期 $d=d(f)$. 由于 $d \mid p$, 只能 $d=1$ 或 $d=p$.

若 $f$ 的周期 $d=1$ 即 $f$ 满足 $f(x+1)=f(x)+1$ 对任意 $x$ 成立, 这样的 $f$
一定是 $f(x)=x+b, b=1,2, \ldots, p-1$ 的形式, 这些置换都满足 $S(f)=\sum_{x=1}^{p} x(x+b)=\sum_{x=1}^{p} x^{2}+b \sum_{x=1}^{p} x=\frac{p(p+1)(2 p+1)}{6}+b \times \frac{p(p+1)}{2} \equiv 0$,

并且没有不动点, 所以 $f(x)=x+b, b=1,2, \ldots, p-1$ 都在 $M$ 中.

若 $f$ 的周期 $d=p$, 则 $\left\{f, R(f), R^{2}(f), \ldots, R^{p-1}(f)\right\}$ 两两不同, 这 $p$ 个置换可以围成一圈, 构成 $p$ 元组.

这样可知: $M$ 中的元素除了 $p-1$ 个 $f(x)=x+b, b=1,2, \ldots, p-1$ 形式的之外, 其余的 $|M|-(p-1)$ 个元素都可以分成若干个 $p$ 元组. 因此 $|M|-(p-1)$是 $p$ 的倍数, 之前已知 $|M|$ 是 $(p-1)$ 的倍数, 于是 $|M|$ 除以 $p^{2}-p$ 的余数是 $p-1$.

