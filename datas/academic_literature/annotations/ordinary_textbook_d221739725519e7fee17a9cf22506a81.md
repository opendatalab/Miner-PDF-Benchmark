# 2019 年清华 “飞测” 数学试题解析 

羊明亮

(浙江省乐清知临中学, 325600)

2019 年 6 月 1 日, 清华大学在浙江, 上海, 湖南, 广州等地举行了数学“飞测”,其题目新颖, 难度适当. 下面我们给出这次飞测试题, 解答及短评, 供大家参考.

## I. 试 题

1. 给定以 $O$ 为圆心的圆周 $\odot O$, 求正整数 $n$ 的最大值, 使得存在圆内两个不同的点 $A, B$ 以及圆周上 $n$ 个不同的点 $P_{1}, \ldots, P_{n}$, 使得 $O P_{i}$ 平分 $\angle A P_{i} B$. 特殊地,当 $B$ 在射线 $P A$ 上, $O$ 也在射线 $P A$ 上时, 称 $O P$ 平分 $\angle A P B$.
2. 给定 $n, k$ 为正整数. 设 $x_{1}, \ldots x_{n}$ 为 $(0,1)$ 中的互异实数, 求

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\{x_{i}-x_{j}\right\}^{k}
$$

的最小值. 其中 $\{x\}$ 表示 $x$ 的小数部分, 即 $\{x\}=x-[x],[x]$ 为不大于 $x$ 的最大整数.

3. 给定一个关于 $x, y, z$ 的实系数多项式

$$
f(x, y, z)=\sum_{i, j, k \in \mathbb{N}} C_{i, j, k} x^{i} y^{j} z^{k}
$$

其中 $C_{i, j, k}$ 中只有有限项不为 0 . 记其次数 $d=\max \left\{i+j+k \mid C_{i, j, k} \neq 0\right\}$, 对于任一实数集 $A$, 定义 $S=\left\{(x, y, z) \in A^{3} \mid f(x, y, z)=0\right\}$. 求证: 若 $d>0$, 则 $|S| \leq d|A|^{2}$.

4. 给定有限集 $X$, 设 $A_{1}, \ldots, A_{n}$ 为 $X$ 的互异子集 $\left(n \in \mathbb{N}^{*}\right)$, 定义

$$
b_{k}=\left|\left\{x \in X \mid x \in A_{i_{1}} \cap \ldots \cap A_{i_{k}}, 1 \leq i_{1}<i_{2}<\ldots<i_{k} \leq n\right\}\right|, 1 \leq k \leq n .
$$

证明: $\prod_{k=1}^{n} b_{k} \leq \prod_{k=1}^{n}\left|A_{k}\right|$.

修订日期: 2019-06-30.

## II . 解答与评注

题 1 给定以 $O$ 为圆心的圆周 $\odot O$, 求正整数 $n$ 的最大值, 使得存在圆内两个不同的点 $A, B$ 以及圆周上 $n$ 个不同的点 $P_{1}, \ldots, P_{n}$, 使得 $O P_{i}$ 平分 $\angle A P_{i} B$.特殊地,当 $B$ 在射线 $P A$ 上, $O$ 也在射线 $P A$ 上时, 称 $O P$ 平分 $\angle A P B$.

解 所求 $n$ 为 4 .

以 $O$ 为原点, $\odot O$ 半径为单位长度, 建立如下复平面. 并以各点的小写字母表示它们对应的复数. 即点 $A$ 对应的复数为 $a$, 点 $B$ 对应的复数为 $b$, 点 $P_{i}$ 对应的复数为 $p_{i}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_2670a5f513ea9e4ad8a5g-2.jpg?height=517&width=580&top_left_y=884&top_left_x=744)

一方面, 取 $a=-\frac{1}{2}, b=\frac{1}{2}$, 则对 $p_{1}=1, p_{2}=\mathrm{i}, p_{3}=-1, p_{4}=-\mathrm{i}(\mathrm{i}=\sqrt{-1})$这四个复数所对应的点 $P_{j}(1 \leq j \leq 4)$ 均满足 $O P_{j}$ 平分 $\angle A P_{j} B$. 故 $n=4$ 可以取到。

另一方面, 注意到: 对 $1 \leq j \leq n ，$

$$
\begin{aligned}
O P_{j} \text { 平分 } \angle A P_{j} B & \Leftrightarrow \measuredangle A P_{j} O=\measuredangle O P_{j} B \\
& \Leftrightarrow \arg \frac{p_{j}-a}{p_{j}}=\arg \frac{p_{j}}{p_{j}-b} \\
& \Leftrightarrow \frac{\left(p_{j}-a\right)\left(p_{j}-b\right)}{p_{j}^{2}} \in \mathbb{R} \\
& \Leftrightarrow \frac{\left(p_{j}-a\right)\left(p_{j}-b\right)}{p_{j}^{2}}=\frac{\overline{\left(p_{j}-a\right)\left(p_{j}-b\right)}}{\overline{p_{j}^{2}}} \\
& \Leftrightarrow \frac{\left(p_{j}-a\right)\left(p_{j}-b\right)}{p_{j}^{2}}=\left(1-\bar{a} p_{j}\right)\left(1-\bar{b} p_{j}\right) \\
& \Leftrightarrow \overline{a b} p_{j}^{4}-(\bar{a}+\bar{b}) p_{j}^{3}+(a+b) p_{j}-a b=0,
\end{aligned}
$$

故 $p_{1}, p_{2}, \ldots, p_{n}$ 均为方程

$$
\overline{a b} x^{4}-(\bar{a}+\bar{b}) x^{3}+(a+b) x-a b=0
$$

的根, 因为 $a, b$ 不全为 0 , 则该方程不恒成立, 故 $n \leq 4$.
综上, 所求 $n$ 的最大值为 4 .

评注 此题笔者暂时还不知道纯平几解法, 复数计算是自然的, 因为角平分线用复数较容易表示。

题 2 给定 $n, k$ 为正整数. 设 $x_{1}, \ldots x_{n}$ 为 $(0,1)$ 中的互异实数, 求

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\{x_{i}-x_{j}\right\}^{k}
$$

的最小值. 其中 $\{x\}$ 表示 $x$ 的小数部分, 即 $\{x\}=x-[x],[x]$ 为不大于 $x$ 的最大整数.

解 所求解为

$$
\frac{1^{k}+2^{k}+\ldots+(n-1)^{k}}{n^{k-1}}
$$

一方面, 取

$$
x_{i}=\frac{2 i-1}{2 n}, i=1,2, \ldots, n \text {. }
$$

则

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\{x_{i}-x_{j}\right\}^{k} & =\sum_{i=1}^{n} \sum_{t=1}^{n}\left\{x_{i}-x_{i+t}\right\}^{k} \quad(\text { 下标模 } n) \\
& =\sum_{i=1}^{n} \sum_{t=1}^{n}\left\{-\frac{t}{n}\right\}^{k} \\
& =n \sum_{t=1}^{n-1}\left(-\frac{t}{n}+1\right)^{k}+0 \quad\left(t=n \text { 时, }\left\{-\frac{t}{n}\right\}=0\right) \\
& =\frac{1^{k}+2^{k}+\ldots+(n-1)^{k}}{n^{k-1}} .
\end{aligned}
$$

故 $\frac{1^{k}+2^{k}+\ldots+(n-1)^{k}}{n^{k-1}}$ 可以取到.

另一方面, 我们证明: 对于任意 $x_{1}, \ldots x_{n}$ 为 $(0,1)$ 中的互异实数,

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\{x_{i}-x_{j}\right\}^{k} \geq \frac{1^{k}+2^{k}+\ldots+(n-1)^{k}}{n^{k-1}}
$$

由对称性, 不妨设 $x_{1}<x_{2}<\ldots<x_{n}$, 则

$$
\begin{array}{rlr}
\text { 原式 } & =\sum_{i=1}^{n} \sum_{t=0}^{n-1}\left\{x_{i+t}-x_{i}\right\}^{k} \quad(\text { 下标模 } n) \\
& \geq n \sum_{t=0}^{n-1}\left(\frac{\sum_{i=1}^{n}\left\{x_{i+t}-x_{i}\right\}}{n}\right)^{k} \quad(\text { 幕平均不等式 }) \\
& =n \sum_{t=1}^{n-1}\left(\frac{\sum_{i=1}^{n}\left\{x_{i+t}-x_{i}\right\}}{n}\right)^{k}
\end{array}
$$

$$
\begin{aligned}
& =n \sum_{t=1}^{n-1}\left(\frac{\sum_{i=1}^{n-t}\left(x_{i+t}-x_{i}\right)+\sum_{i=n-t+1}^{n}\left(1+x_{i+t}-x_{i}\right)}{n}\right)^{k} \\
& =n \sum_{t=1}^{n-1}\left(\frac{n-t}{n}\right)^{k}=\frac{1^{k}+2^{k}+\ldots+(n-1)^{k}}{n^{k-1}} .
\end{aligned}
$$

综上, 所求解为

$$
\frac{1^{k}+2^{k}+\ldots+(n-1)^{k}}{n^{k-1}}
$$

评注 此题属于简单题, 关键在于用一种“将 $x_{1}, x_{2}, \ldots, x_{n}$ 置于圆周上”的观点来看待原式中的小数部分.

题 3 给定一个关于 $x, y, z$ 的实系数多项式

$$
f(x, y, z)=\sum_{i, j, k \in \mathbb{N}} C_{i, j, k} x^{i} y^{j} z^{k}
$$

其中 $C_{i, j, k}$ 中只有有限项不为 0 . 记其次数 $d=\max \left\{i+j+k \mid C_{i, j, k} \neq 0\right\}$, 对于任一实数集 $A$, 定义 $S=\left\{(x, y, z) \in A^{3} \mid f(x, y, z)=0\right\}$. 求证: 若 $d>0$, 则 $|S| \leq d|A|^{2}$.

证明 我们证明如下更一般的结论.

对于 $n \in \mathbb{N}^{+}$及 $n$ 元非零实系数多项式

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{\alpha_{1}, \ldots, \alpha_{n} \in \mathbb{N}} C_{\alpha_{1}, \ldots, \alpha_{n}} x_{1}^{\alpha_{1}} x_{2}^{\alpha_{2}} \ldots x_{n}^{\alpha_{n}}
$$

$\left(C_{\alpha_{1}, \ldots, \alpha_{n}}\right.$ 中只有有限项不为 0 ), 记 $\operatorname{deg} f=\max \left\{\alpha_{1}+\ldots+\alpha_{n} \mid C_{\alpha_{1}, \ldots, \alpha_{n}} \neq 0\right\}$, 对于任一有限实数集 $A$, 定义 $S=\left\{\left(x_{1}, \ldots, x_{n}\right) \in A^{n} \mid f\left(x_{1}, \ldots, x_{n}\right)=0\right\}$, 则

$$
|S| \leq \operatorname{deg} f \cdot|A|^{n-1}
$$

原题即为 $(*)$ 中 $n=3, \operatorname{deg} f>0$ 的情形.

(*) 的证明: 对 $n$ 归纳.

当 $n=1$ 时, 即 “一元 $d$ 次非零实系数方程至多 $d$ 个不同实根”, 显然成立.

假设 $n=m\left(m \in \mathbb{N}^{+}\right)$时结论成立.

当 $n=m+1$ 时, 以下通过对 $\operatorname{deg} f$ 进行归纳证明, 从而证明命题成立.

当 $\operatorname{deg} f=0$ 时结论明显成立.

假设 $\operatorname{deg} f=k\left(k \in \mathbb{N}^{+}\right)$时结论成立, 那么当 $\operatorname{deg} f=k+1$ 时, 我们需证明:对于 $x_{1}, x_{2}, \ldots, x_{m}, x_{m+1} \in A$, 则

$$
|S| \leq(k+1) \cdot|A|^{m}
$$

以下分两种情形讨论:

(1) 若对 $x \in A$, 记 $f_{x}\left(x_{1}, x_{2}, \cdots, x_{m}\right)=f\left(x_{1}, x_{2}, \cdots, x_{m}, x\right)$,

且 $f_{x}\left(x_{1}, x_{2}, \cdots, x_{m}\right)$ 均不为零多项式, 由 $n=m$ 时的归纳假设可知,

$$
\left|\left\{\left(x_{1}, x_{2}, \ldots, x_{m}\right) \in A^{m} \mid f_{x}\left(x_{1}, x_{2}, \ldots, x_{m}\right)=0\right\}\right| \leq(k+1)|A|^{m-1} .
$$

故

$$
|S| \leq|A| \cdot(k+1) \cdot|A|^{m-1}=(k+1)|A|^{m} .
$$

结论成立.

(2) 若存在 $x_{0} \in A, f_{x_{0}}\left(x_{1}, x_{2}, \ldots, x_{m}\right)$ 为零多项式, 那么

$$
\left(x_{m+1}-x_{0}\right) \mid f\left(x_{1}, x_{2}, \ldots, x_{m+1}\right),
$$

记

$$
\begin{aligned}
& f^{*}\left(x_{1}, \ldots x_{m+1}\right)=\frac{f\left(x_{1}, x_{2}, \ldots x_{m+1}\right)}{x_{m+1}-x_{0}}, \\
& S^{*}=\left\{\left(x_{1}, x_{2}, \ldots, x_{m+1}\right) \in A^{m+1} \mid f^{*}\left(x_{1}, x_{2}, \ldots, x_{m+1}\right)=0\right\},
\end{aligned}
$$

可知 $\operatorname{deg} f^{*}=\operatorname{deg} f-1$. 由归纳假设可知,

$$
\left|S^{*}\right| \leq k|A|^{m}
$$

又由

$$
S \subseteq S^{*} \cup\left\{\left(x_{1}, \ldots, x_{m}, x_{0}\right) \mid x_{1}, x_{2}, \cdots, x_{m} \in A\right\}
$$

则

$$
|S| \leq(k+1)|A|^{m}
$$

故结论成立.

综合 (1), (2) 知, $\operatorname{deg} f=k+1$ 时, $n=m+1$ 的结论成立, 即 (*) 成立.

特别地, 原命题成立, 证毕!

评注 此题需特别小心零多项式情形, 这导致给定 $x, y$ 后可能不止 $d$ 个 $z$ 使 $f(x, y, z)=0$, 意识到这一点后此题思路十分清晰.

对一般的多元多项式 $g(x, y, z)$ 和 $f(x, y, z)$, 是无法在 “对满足 $g(x, y, z)=0$的实数解 $(x, y, z)$ 均有 $f(x, y, z)=0$ ”的条件下推出 $g(x, y, z) \mid f(x, y, z)$, 这一点需要小心.

题 4 给定有限集 $X$, 设 $A_{1}, \ldots, A_{n}$ 为 $X$ 的互异子集 $\left(n \in \mathbb{N}^{*}\right)$, 定义

$$
b_{k}=\left|\left\{x \in X \mid x \in A_{i_{1}} \cap \ldots \cap A_{i_{k}}, 1 \leq i_{1}<i_{2}<\ldots<i_{k} \leq n\right\}\right|, 1 \leq k \leq n
$$

证明: $\prod_{k=1}^{n} b_{k} \leq \prod_{k=1}^{n}\left|A_{k}\right|$.

证明 记 $a_{k}=\left|A_{k}\right|, k=1,2, \ldots, n$. 不妨设 $a_{1} \geq a_{2} \geq \ldots \geq a_{n}$, 记

$$
T_{k}=A_{1} \cup A_{2} \cup \ldots \cup A_{k}, k=1,2, \ldots, n .
$$

对 $x \in T_{k}$, 记

$$
d_{k}(x)=\left|\left\{i \mid 1 \leq i \leq k, x \in A_{i}\right\}\right| .
$$

下面我们证明: 对 $1 \leq k \leq n$,

$$
b_{1}+b_{2}+\ldots+b_{k} \geq a_{1}+a_{2}+\ldots+a_{k} .
$$

事实上, 对 $1 \leq i \leq k, b_{i}$ 不小于出现在 $A_{1}, \ldots A_{k}$ 中至少 $i$ 个集合的元素的个数, 即 $b_{i} \geq\left|\left\{x \mid d_{k}(x) \geq i\right\}\right|$. 故

$$
\begin{aligned}
\sum_{i=1}^{k} b_{i} & \geq \sum_{i=1}^{k}\left(\sum_{x \in T_{k}, d_{k}(x) \geq i} 1\right)=\sum_{x \in T_{k}} d_{k}(x) \\
& =\sum_{x \in T_{k}} \sum_{x \in A_{i}} 1=\sum_{i=1}^{k} \sum_{x \in A_{i}} 1 \\
& =\sum_{i=1}^{k} a_{i} .
\end{aligned}
$$

$(*)$ 证毕. 并且由 $(*)$ 证明过程知

$$
\sum_{i=1}^{n} b_{i}=\sum_{i=1}^{n} a_{i}
$$

下记

$$
S_{k}=\sum_{i=1}^{k} b_{i}, \quad R_{k}=\sum_{i=1}^{k} a_{i}, 1 \leq k \leq n
$$

则 $S_{k} \geq R_{k}$. 原不等式在 $a_{n}=0$ 时显然成立, 此时 $b_{n}=0$.

当 $a_{n}>0$ 时, $a_{1} \ldots a_{n}>0$, 要证明原不等式成立, 即证明

$$
\prod_{k=1}^{n} \frac{b_{k}}{a_{k}} \leq 1
$$

只需证明

$$
\sum_{k=1}^{n} \frac{b_{k}}{a_{k}} \leq n .(\mathrm{A}-\mathrm{G} \text { 不等式 })
$$

注意到

$$
\sum_{k=1}^{n} \frac{b_{k}}{a_{k}}=\sum_{k=1}^{n-1}\left(\frac{1}{a_{k}}-\frac{1}{a_{k+1}}\right) S_{k}+\frac{S_{n}}{a_{n}} \quad \text { (Abel 公式) }
$$

$$
\begin{aligned}
& \leq \sum_{k=1}^{n-1}\left(\frac{1}{a_{k}}-\frac{1}{a_{k+1}}\right) R_{k}+\frac{R_{n}}{a_{n}} \quad\left(a_{k} \geq a_{k+1}, R_{n}=S_{n}, R_{k} \leq S_{k}\right) \\
& =\sum_{k=1}^{n} \frac{a_{k}}{a_{k}} \quad \text { (Abel 公式) } \\
& =n=\text { 右式. }
\end{aligned}
$$

则 $\sum_{i=1}^{n} \frac{b_{i}}{a_{i}} \leq n$ 成立, 故

$$
\prod_{k=1}^{n} b_{k} \leq \prod_{k=1}^{n}\left|A_{k}\right|
$$

成立. 证毕!

评注 此题后半部分证明原不等式的方法类似于优超不等式的证明. 事实上 (*) 即优超条件, 原不等式为优超不等式的特例.

此题也可利用优化一步到位.

首先, 基于集合与元素的对偶观点, 记 $T=A_{1} \cup \ldots \cup A_{n}$, 并对 $x \in T$, 记 $C(x)=\left\{i \mid x \in A_{i}\right\}$. 则 $b_{k}=|\{x \in T|| C(x) \mid \geq k\}|$. 类似于原解答知,

$$
b_{1}+\ldots+b_{n}=a_{1}+\ldots+a_{n}
$$

对 $x, y \in T$,

$$
|C(x)| \leq|C(y)| .
$$

若 $C(x) \backslash C(y) \neq \emptyset$, 设 $j \in C(x) \backslash C(y)$, 即 $x \in A_{j}, y \notin A_{j}$. 那么, 将 $A_{j}$ 中元素 $x$改为 $y$, 并设

$$
|C(x)|=a,|C(y)|=b .
$$

则变化后 $\left|A_{1}\right|, \ldots,\left|A_{n}\right|$ 不变, $b_{a}$ 减 $1, b_{b+1}$ 加 1 , 其余 $b_{k}$ 不变, 有 $b_{1} b_{2} \cdots b_{n}$ 增大 (因变化后 $b_{a}$ 不小于 $b_{b+1}$ ).

故可不妨设: 若 $|C(x)| \leq|C(y)|$, 则 $C(x) \subseteq C(y)$.

如此易知, 不妨设 $\left|A_{1}\right| \geq\left|A_{2}\right| \geq \ldots \geq\left|A_{n}\right|$, 则 $\left|A_{i}\right|=b_{i}, 1 \leq i \leq n$, 原命题显然成立.

有时组合上的优化因更好地利用了组合意义, 比代数上的调整更为有力.

