# 一道 Kürschák 比赛试题的加强 

叶奇 滕丁维<br>(浙江温州乐清市乐成寄宿中学, 325600)

2015 年, 匈牙利 Kürschák 比赛有这样一道试题:

问题 1. 设 $Q_{n}$ 是所有 $n$ 项 0,1 序列组成的集合, $A$ 是 $Q_{n}$ 的一个 $2^{n-1}$ 元子集. 证明: 至少存在 $2^{n-1}$ 个序列对 $(a, b)$, 满足 $a \in A, b \in Q_{n} \backslash A$ 且 $a, b$ 恰有一项不同.

冷岗松老师介绍了这个问题的一个推广:

定理 1. 设 $A, B$ 是 $Q_{n}$ 的一个分拆, 则至少存在 $\min \{|A|,|B|\}$ 个序列对 $(a, b) \in A \times B$, 使得 $a, b$ 恰有一项不同.

我们给出这个定理的进一步加强, 证明如下结果:

定理 2. 设 $A, B$ 是 $Q_{n}$ 的一个分拆, 则至少存在 $\frac{|A||B|}{2^{n-1}}$ 个序列对 $(a, b) \in$ $A \times B$, 使得 $a, b$ 恰有一项不同.

由于 $A, B$ 是 $Q_{n}$ 的一个分拆, 从而 $|A|$ 和 $|B|$ 至少有一项大于等于 $2^{n-1}$, 所以 $\frac{|A||B|}{2^{n-1}} \geq \min \{|A|,|B|\}$. 这就说明了定理 2 是定理 1 的加强.

下面我们给出两个证明:

证明 1. 对 $n$ 用归纳法.

当 $n=1$ 时, 结论显然成立. 假设结论对 $n-1$ 成立.

现考虑 $n$ 的情况. 设

$$
\begin{aligned}
& A_{0}=\left\{\alpha \mid \alpha \in Q_{n-1},(\alpha, 0),(\alpha, 1) \text { 均在 } A \text { 中 }\right\}, \\
& A_{1}=\left\{\alpha \mid \alpha \in Q_{n-1},(\alpha, 0),(\alpha, 1) \text { 恰有一个 } A \text { 中 }\right\}, \\
& A_{2}=\left\{\alpha \mid \alpha \in Q_{n-1},(\alpha, 0),(\alpha, 1) \text { 均在 } B \text { 中 }\right\} .
\end{aligned}
$$

则 $A_{0}, A_{1}, A_{2}$ 是 $Q_{n-1}$ 的分拆, 且 $|A|=2\left|A_{0}\right|+\left|A_{1}\right|,|B|=2\left|A_{2}\right|+\left|A_{1}\right|$.

收稿日期: 2017-01-23; 修订日期: 2017-03-20.
设存在 $x$ 对 $(a, b) \in A_{0} \times A_{1}$ 使得 $a, b$ 恰有一项不同, $y$ 对 $(a, b) \in A_{1} \times A_{2}$使得 $a, b$ 恰有一项不同, $z$ 对 $(a, b) \in A_{0} \times A_{2}$ 使得 $a, b$ 恰有一项不同. 则存在 $x+y+2 z+\left|A_{1}\right|$ 对 $(a, b) \in A \times B$ 使得 $a, b$ 恰有一项不同.

对 $A_{0}, A_{1} \cup A_{2}$ 用归纳假设得:

$$
x+z \geq \frac{\left|A_{0}\right| \cdot\left(\left|A_{1}\right|+\left|A_{2}\right|\right)}{2^{n-2}}
$$

对 $A_{0} \cup A_{1}, A_{2}$ 用归纳假设得：

$$
y+z \geq \frac{\left|A_{2}\right| \cdot\left(\left|A_{0}\right|+\left|A_{1}\right|\right)}{2^{n-2}} .
$$

因此要证明结论对 $n$ 成立, 只需证明:

$$
\frac{\left|A_{0}\right| \cdot\left(\left|A_{1}\right|+\left|A_{2}\right|\right)}{2^{n-2}}+\frac{\left|A_{2}\right| \cdot\left(\left|A_{0}\right|+\left|A_{1}\right|\right)}{2^{n-2}}+\left|A_{1}\right| \geq \frac{\left(2\left|A_{0}\right|+\left|A_{1}\right|\right)\left(2\left|A_{2}\right|+\left|A_{1}\right|\right)}{2^{n-1}} .
$$

这等价于 $2^{n-1}\left|A_{1}\right| \geq\left|A_{1}\right|^{2}$, 即 $0 \leq\left|A_{1}\right| \leq 2^{n-1}$, 显然成立. 这证明了 $n$ 的情形也成立.

证明 2. 若 $a \in A, b \in B$ 恰在第 $d_{1}<d_{2}<\cdots<d_{k}$ 个分量处不同, 则可构造 $c_{1}, c_{2}, \cdots, c_{k-1} \in Q_{n}$ 使得

$a$ 与 $c_{1}$ 恰在第 $d_{1}$ 个分量处不同, $c_{1}$ 与 $c_{2}$ 恰在第 $d_{1}$ 个分量处不同,

$$
c_{k-1} \text { 与 } c_{k} \text { 恰在第 } d_{k} \text { 个分量处不同. }
$$

从而可知 $c_{1}, c_{2}, \cdots, c_{k-1}$ 被 $a, b$ 唯一决定. 由于 $a \in A, b \in B$, 故在序列 $a, c_{1}, c_{2}, \cdots, c_{k-1}, b$ 中至少有一对相邻的 $c_{i_{0}-1}, c_{i_{0}}$ (视 $\left.c_{0}=a, c_{k}=b\right), 1 \leq i_{0} \leq k$满足 $c_{i_{0}-1} \in A$ 且 $c_{i_{0}} \in B$. 故对任意 $a \in A, b \in B$, 都至少存在一对 $\left(a^{\prime}, b^{\prime}\right) \in$ $A \times B$ 与之对应, 使得 $a^{\prime}, b^{\prime}$ 恰有一个分量不同.

另一方面, 对任意恰一个分量不同的对 $\left(a^{\prime}, b^{\prime}\right)$ (其中 $a^{\prime} \in A, b^{\prime} \in B$ ), 与其对应的对 $(a, b)$ (其中 $a \in A, b \in B$ ) 的个数不超过 $2^{n-1}$. 理由如下: 若

$$
\begin{aligned}
& a^{\prime}=\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{i}, \varepsilon_{i+1}, \cdots, \varepsilon_{n}\right), \\
& b^{\prime}=\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, 1-\varepsilon_{i}, \varepsilon_{i+1}, \cdots, \varepsilon_{n}\right) .
\end{aligned}
$$

注意到在构造与 $(a, b)$ 对应的 $\left(a^{\prime}, b^{\prime}\right)$ 时, 变化的分量的位置顺序是从小到大, 故由 $a^{\prime}, b^{\prime}$ 在第 $i$ 个分量不同可知, 前 $i$ 个分量已经做了变化, 从而 $b$ 的前 $i$ 个分量为 $\varepsilon_{1}, \varepsilon_{2}, \cdots, 1-\varepsilon_{i}$; 而第 $i+1$ 到 $n$ 个分量还没有变化, 故 $a$ 的第 $i+1$ 到 $n$ 个分量为 $\varepsilon_{i}, \varepsilon_{i+1}, \cdots, \varepsilon_{n} . a, b$ 的其他分量可以从 0,1 中自由选择, 故与 $\left(a^{\prime}, b^{\prime}\right)$ 对应的
对 $(a, b)$ 的个数至多 $2^{i-1} \cdot 2^{n-i}=2^{n-1}$. 从而这样的 $\left(a^{\prime}, b^{\prime}\right)$ 至少 $\frac{|A||B|}{2^{n-1}}$ 对.

致谢 作者感谢余水能、羊明亮老师的指导!

