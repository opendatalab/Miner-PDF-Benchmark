$$
\text { 数学新星网 } \% \text { 学生专栏 }
$$

www.nsmath.cn/xszl

# 一个大集构造问题 

陈博文

(江苏省徐州市第一中学, 221140)

在冯跃峰老师的《组合构造》一书中, 第 141-142 页有一道例题:

问题 设 $n$ 为正奇数, $M$ 是 $n$ 个非零复数的集合, 对 $M$ 的任何子集 $A$, 定义 $S(A)$ 为 $A$ 中各元素之和, 其中规定 $S(\emptyset)=0$. 设 $A \subseteq M$, 如果对任意 $B \subseteq M$,有 $|S(A)| \geq|S(B)|$. 则称 $A$ 为 $M$ 的一个大集. 求 $M$ 的大集个数最大值.

书中给出了 $M$ 的大集个数的最大值为 $2 n$.

遗留问题是当 $n$ 为偶数时, 大集个数的最大值是多少? 本文给出这一问题的分析与解答.

分析与解 原解答中已经证明: 不论 $n$ 是奇数还是偶数, 大集个数都不超过 $2 n$.

(1) $n=2$ 时, $|S(\emptyset)|=0, \emptyset$ 不能为大集, 而 $M$ 有 3 个非空子集, 从而大集个数不超过 3 .

设 $M=\left\{1, \frac{-1+\sqrt{3} \mathrm{i}}{2}\right\}$, 则这三个子集均为大集.

综上, 所求最大值为 3 .

(2) $n \geq 4$ 时, 设 $n=2 k, k \in \mathbb{N}^{*}, k \geq 2$.

下面给出一种构造, 使大集个数为 $2 n$.

思路是将 $n=2 k-1$ 情形的其中一个复数拆成两个复数的和, 为使原有性质保持相似, 可将其中一个新复数的模长变得尽可能小. 为方便划分半集, 应使新复数的幅角变化范围易于控制.

下面给出具体构造: 取

$$
z_{j}=e^{2 \pi \mathrm{i} \frac{j}{2 k-1}}, j=1,2, \cdots, 2 k-2
$$[^0]注意到 $1-e^{\mathrm{i} \theta}=2 \sin \frac{\theta}{2} e^{\mathrm{i} \frac{\theta-\pi}{2}}$, 可得

$$
\begin{aligned}
\sum_{j=1}^{k-1} z_{j} & =\frac{2 \pi \mathrm{i} \frac{j}{2 k-1}\left(1-e^{\frac{2 \pi \mathrm{i}}{2 k-1}}(k-1)\right)}{1-e^{2 \pi \mathrm{i} \frac{1}{2 k-1}}} \\
& =\frac{e^{\frac{2 \pi \mathrm{i}}{2 k-1}} 2 \sin \frac{k-1}{2 k-1} \pi e^{\mathrm{i} \pi\left(\frac{k-1}{2 k-1}-\frac{1}{2}\right)}}{2 \sin \frac{\pi}{2 k-1} e^{\mathrm{i} \pi\left(\frac{k-1}{2 k-1}-\frac{1}{2}\right)}} \\
& =\frac{\sin \frac{k-1}{2 k-1} \pi}{\sin \frac{1}{2 k-1} \pi} e^{\mathrm{i} \frac{k}{2 k-1} \pi}
\end{aligned}
$$

令

$$
r=\frac{\sin \frac{k-1}{2 k-1} \pi}{\sin \frac{1}{2 k-1} \pi}
$$

则

$$
\sum_{j=1}^{k-1} z_{j}=r e^{\mathrm{i} \frac{k}{2 k-1} \pi}, r>0
$$

取

$$
z_{2 k-1}=-r e^{\mathrm{i} \frac{k}{2 k-1} \pi}\left(1-e^{-\mathrm{i} \varepsilon}\right)=2 \sin \frac{\varepsilon}{2} r e^{\left(\frac{1}{4 k-2} \pi-\frac{\varepsilon}{2}\right) \mathrm{i}}
$$

其中 $\varepsilon$ 为充分小的正数, 使得

$$
\arg \left(z_{2 k-1}\right) \in\left(\frac{\pi}{4(2 k-1)}, \frac{\pi}{2 k-1}\right),
$$

且

$$
\arg \left(1-z_{2 k-1}\right)=\left(-\frac{\pi}{2 k-1}, \frac{\pi}{4(2 k-1)}\right)
$$

(这是能够办到的, 因为 $\varepsilon \rightarrow 0$ 时, $\arg \left(z_{2 k-1}\right) \rightarrow \frac{\pi}{4(2 k-1)}, \arg \left(1-z_{2 k-1}\right) \rightarrow 0$ )

取

$$
z_{2 k}=1-z_{2 k-1}, M=\left\{z_{1}, z_{2}, \cdots, z_{2 k}\right\}
$$

则

$$
z_{1}+z_{2}+\cdots+z_{2 k}=\sum_{j=1}^{2 k-1} e^{2 \pi \mathrm{i} \frac{j}{2 k-1}}=0
$$

且

$$
\begin{gathered}
\arg \left(z_{1}\right)=\frac{2}{2 k-1} \pi \\
\arg \left(-z_{k-1}\right)=-\frac{\pi}{2 k-1} \\
\arg \left(-z_{k}\right)=\frac{\pi}{2 k-1} \\
\arg \left(z_{2 k-2}\right)=-\frac{2}{2 k-1} \pi
\end{gathered}
$$

知 $z_{2 k-1}$ 和 $z_{2 k}$ 落在 $O_{z_{k-1}}$ 和 $O_{z_{k}}$ 两条直线的内夹角内. 按逆时针方向为 $z_{1}, z_{2}, \cdots, z_{2 k-2}, z_{2 k}, z_{2 k-1}$.

从而在 $4 k$ 个半集中, 有 $4 k-2$ 个, $z_{2 k-1}$ 和 $z_{2 k}$ 或者不出现, 或者同时出现,易知这 $4 k-2$ 个半集模为

$$
\frac{\sin \frac{k-1}{2 k-1} \pi}{\sin \frac{1}{2 k-1} \pi}=r
$$

只有一种划分方式将 $z_{2 k-1}$ 和 $z_{2 k}$ 割裂开, 这两个半集为 $\left\{z_{1}, z_{2}, \cdots, z_{k-1}, z_{2 k-1}\right\}$和 $M \backslash\left\{z_{1}, z_{2}, \cdots, z_{k-1}, z_{2 k-1}\right\}$.

对于前者, 因为 $z_{1}+z_{2}+\cdots+z_{k-1}+z_{2 k-1}=r e^{\mathrm{i} \frac{k}{2 k-1} \pi} \cdot e^{-\mathrm{i} \varepsilon}$, 从而它的模为 $r$; 对于后者, 其模为

$$
\begin{aligned}
& \left|S(M)-S\left(\left\{z_{1}, z_{2}, \cdots, z_{k+1}, z_{2 k-1}\right\}\right)\right| \\
= & \left|0-\left(z_{1}+z_{2}+\cdots+z_{k+1}+z_{2 k-1}\right)\right| \\
= & r .
\end{aligned}
$$

从而 $4 k$ 个半集模相等, 又大集存在, 且为某半集, 故 $4 k$ 个半集全为大集. 至此,问题已解决.

下面是 $n=6$ 时的示意图.

![](https://cdn.mathpix.com/cropped/2024_02_26_bb6db2a493b3e9544f1eg-3.jpg?height=805&width=874&top_left_y=1428&top_left_x=591)


[^0]:    收稿日期: 2018-07-05； 修订日期: 2018-09-25.

