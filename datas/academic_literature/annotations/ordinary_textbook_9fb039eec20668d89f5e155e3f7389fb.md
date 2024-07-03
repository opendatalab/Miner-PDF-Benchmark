# 第五十期问题征解解答与点评 

张端阳

第一题 定义函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 满足 $f(1)=1$, 且对任意整数 $n \geq 2$, 若 $n$ 的素因数标准分解为 $\prod_{i=1}^{m} p_{i}^{\alpha_{i}}$, 则 $f(n)=\prod_{i=1}^{m} \alpha_{i}^{p_{i}}$.

问：对给定的正整数 $n$, 迭代序列 $f(n), f^{(2)}(n), f^{(3)}(n), \cdots$ 是否最终一定周期? 若是, 求最小正周期的最大可能值; 若不是, 给出所有的反例.

(华南师大附中学生 戴子一 供题)

## 解 (根据衢州二中向阳天同学的解答整理):

先证明两个引理.

引理 1 设 $x_{1}, x_{2}, \cdots, x_{t} \geq 2$, 则 $\prod_{i=1}^{t} x_{i} \geq \sum_{i=1}^{t} x_{i}$.

证明 对 $t$ 归纳.

当 $t=1$ 时显然成立. 当 $t=2$ 时,

$$
x_{1} x_{2}-\left(x_{1}+x_{2}\right)=\left(x_{1}-1\right)\left(x_{2}-1\right)-1 \geq 0 .
$$

假设 $t \geq 3$ 且 $t-1$ 时成立, 来看 $t$ 时的情形.

由归纳假设和 $t=2$ 时的情形,

$$
\prod_{i=1}^{t} x_{i}=\prod_{i=1}^{t-1} x_{i} \cdot x_{t} \geq \sum_{i=1}^{t-1} x_{i} \cdot x_{t} \geq \sum_{i=1}^{t-1} x_{i}+x_{t}=\sum_{i=1}^{t} x_{i}
$$

归纳证毕.

引理 2 设 $x \geq 2, y \in \mathbb{N}_{+}$, 则 $x^{y} \geq x y$.

证明 由伯努利不等式,

$$
x^{y-1} \geq 2^{y-1}=(1+1)^{y-1} \geq 1+(y-1) \cdot 1=y
$$

再同乘以 $x$ 即证.

回到原题. 我们证明对任意正整数 $n, n \geq f(f(n))$.

当 $n=1$ 时显然成立. 对 $n \geq 2$, 设 $n$ 的素因数标准分解为 $\prod_{i=1}^{m} p_{i}^{\alpha_{i}}$, 再设 $\prod_{i=1}^{m} \alpha_{i}$的所有素因子为 $q_{1}, q_{2}, \cdots, q_{t}$, 且 $f(n)=\prod_{i=1}^{m} \alpha_{i}^{p_{i}}$ 的素因数标准分解为 $\prod_{j=1}^{t} q_{j}^{\beta_{j}}$, 则

$$
\beta_{j}=\sum_{i=1}^{m} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right), j=1,2, \cdots, t .
$$

此时

$$
f(f(n))=\prod_{j=1}^{t} \beta_{j}^{q_{j}}=\prod_{j=1}^{t}\left(\sum_{i=1}^{m} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right)\right)^{q_{j}}
$$

又

$$
n=\prod_{i=1}^{m} p_{i}^{\alpha_{i}}=\prod_{i=1}^{m} p_{i}^{\prod_{j=1}^{t} q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)}}
$$

所以只需证明

$$
\prod_{i=1}^{m} p_{i}^{\prod_{j=1}^{t} q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)}} \geq \prod_{j=1}^{t}\left(\sum_{i=1}^{m} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right)\right)^{q_{j}} .
$$

由引理 1,

$$
\prod_{j=1}^{t} q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)}=\prod_{\substack{1 \leq j \leq t \\ \nu_{q_{j}}\left(\alpha_{i}\right)>0}} q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)} \geq \sum_{\substack{1 \leq j \leq t \\ \nu_{q_{j}}\left(\alpha_{i}\right)>0}} q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)}
$$

于是

$$
\prod_{i=1}^{m} p_{i}^{\prod_{j=1}^{t} q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)}} \geq \prod_{j=1}^{t} \prod_{\substack{1 \leq i \leq m \\ \nu_{q_{j}}\left(\alpha_{i}\right)>0}} p_{i}^{q_{j}^{\nu_{q_{j}}\left(\alpha_{i}\right)}}
$$

又

$$
\sum_{i=1}^{m} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right)=\sum_{\substack{1 \leq i \leq m \\ \nu_{q_{j}}\left(\alpha_{i}\right)>0}} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right)
$$

所以为了记号上的简便, 可不妨设所有 $\nu_{q_{j}}\left(\alpha_{i}\right)$ 均大于 0 . 此时只需证明, 对 $j=1,2, \cdots, t$, 均有

$$
\prod_{i=1}^{m} p_{i}^{q_{j}^{\nu_{j}\left(\alpha_{i}\right)}} \geq\left(\sum_{i=1}^{m} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right)\right)^{q_{j}}
$$

由引理 2 ,

$$
\prod_{i=1}^{m} p_{i}^{q_{j}^{\nu_{j}\left(\alpha_{i}\right)}} \geq \prod_{i=1}^{m} p_{i}^{q_{j} \nu_{q_{j}}\left(\alpha_{i}\right)}=\left(\prod_{i=1}^{m} p_{i}^{\nu_{q_{j}}\left(\alpha_{i}\right)}\right)^{q_{j}}
$$

再由引理 1 和引理 2,

$$
\prod_{i=1}^{m} p_{i}^{\nu_{q_{j}}\left(\alpha_{i}\right)} \geq \sum_{i=1}^{m} p_{i}^{\nu_{q_{j}}\left(\alpha_{i}\right)} \geq \sum_{i=1}^{m} p_{i} \nu_{q_{j}}\left(\alpha_{i}\right)
$$

由此即证.

这样, $\left\{f^{(2 k)}(n)\right\}$ 和 $\left\{f^{(2 k+1)}(n)\right\}$ 都是不增的正整数序列, 从而存在正整数 $K$,使得对任意整数 $k \geq K$, 均有 $f^{(k+2)}(n)=f^{(k)}(n)$. 故 $\left\{f^{(k)}(n)\right\}$ 最终一定周期, 且
最小正周期不超过 2.

另一方面, 因为 $f(8)=9, f(9)=8$, 所以当 $n=8$ 时, $\left\{f^{(k)}(n)\right\}$ 的最小正周期等于 2 .

综上, 迭代序列 $\left\{f^{(k)}(n)\right\}$ 最终一定周期, 且最小正周期最大为 2.

评注 (1). 事后发现, 本题已在美国数学月刊 2007 年第 8 期 11315 号问题中出现过。

(2). 福州延安中学李奕铭, 广州大学附属中学何金喜, 筧州二中周胤帆, 温州中学徐吴祁, 人大附中杨元箎, 华南师范大学附属中学彭子晋, 天津市第一中学张航领等同学也给出了本题的正确解答.

第二题 如图, 在 $\triangle A B C$ 中, $H$ 为垂心. 以 $A H$ 为半径的圆 $H$ 分别交 $A B, A C$于点 $D, E, D C$ 交 $B E$ 于点 $F . A^{\prime}$ 为 $A$ 关于圆 $H$ 的对径点. 以 $A H$ 为底, 作等腰 $\triangle M A H$, 其中 $\angle M A B, \angle A B C, \angle A C B$ 构成等差数列. 以其腰为半径的圆 $M$ 交以 $A F$ 为直径的圆 $G$ 于点 $N$. 设 $\triangle B H C$ 的外心为 $O$, 延长 $O A^{\prime}$ 交圆 $G$ 于点 $S$, 延长 $A S$ 交 $N F$ 于点 $K$.

证明: (1) $A, N, O$ 三点共线; (2) $B, C, K$ 三点共线.

(长郡中学学生 李汝曦 供题)

## 证明 (根据福州延安中学李奕铭同学的整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_d69edc3f1453fb5435eeg-3.jpg?height=622&width=694&top_left_y=1665&top_left_x=681)

(1) 因为 $A N$ 是圆 $M$ 与圆 $G$ 的根轴, 所以只需证明 $O$ 到圆 $M$ 与圆 $G$ 的幕相等.

一方面, 由 $\angle M A B, \angle A B C, \angle A C B$ 构成等差数列, 知 $\angle M A B=2 B-C$, 所以

$$
\angle M H A=\angle M A H=(2 B-C)+\left(90^{\circ}-B\right)=90^{\circ}+B-C .
$$

又

$$
\angle A H O=\angle A H B+\angle B H O=\left(180^{\circ}-C\right)+B,
$$

所以

$$
\angle M H O=\angle A H O-\angle M H A=90^{\circ} \text {, }
$$

于是 $O$ 到圆 $M$ 的幕为 $O H^{2}$.

另一方面, 由 $H A=H D$ 且 $C H \perp A D$ 知 $\angle A D C=A$. 同理, $\angle A E B=A$, 所以

$$
\angle B D C=\angle B E C=180^{\circ}-A=\angle B H C,
$$

于是 $B, D, H, E, C$ 五点共圆, 且以 $O$ 为圆心.

用 $\operatorname{Pow}(X)$ 表示点 $X$ 到圆 $O$ 的幂. 对圆内接四边形 $B D E C$, 熟知 $A F^{2}=$ $\operatorname{Pow}(A)+\operatorname{Pow}(F)$, 所以

$$
\begin{aligned}
O G^{2} & =\frac{1}{2}\left(O A^{2}+O F^{2}\right)-\frac{1}{4} A F^{2} \\
& =\frac{1}{2}(\operatorname{Pow}(A)+\operatorname{Pow}(F))+O H^{2}-\frac{1}{4} A F^{2} \\
& =\frac{1}{4} A F^{2}+O H^{2}=A G^{2}+O H^{2} .
\end{aligned}
$$

于是 $O$ 到圆 $G$ 的幂 $O G^{2}-A G^{2}=O H^{2}$.

故 $O$ 到圆 $M$ 与圆 $G$ 的幂均为 $O H^{2}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_d69edc3f1453fb5435eeg-4.jpg?height=671&width=765&top_left_y=1503&top_left_x=634)

(2) 延长 $D A^{\prime}, E A^{\prime}$ 分别交圆 $O$ 于点 $B^{\prime}, C^{\prime}$, 由 $\angle A D A^{\prime}=\angle A E A^{\prime}=90^{\circ}$, 知 $B B^{\prime}, C C^{\prime}$ 是圆 $O$ 的直径.

对圆内接六边形 $B E C^{\prime} C D B^{\prime}$ 用 Pascal 定理得 $O, A^{\prime}, F$ 共线, 所以由 $\angle A S F=$ $90^{\circ}$ 知 $O F \perp A K$. 又由 $\angle A N F=90^{\circ}$ 知 $A O \perp F K$, 所以 $K$ 是 $\triangle A O F$ 的垂心.

对圆内接四边形 $B D E C$ 用 Brocard 定理, 知 $K$ 是 $D E$ 与 $B C$ 的交点, 故 $B, C, K$ 共线.
评注 (1). 雗州二中周胤帆同学指出, 点 $N$ 满足 $\angle H N C=3 \angle H B C, \angle H N B=$ $3 \angle H C B$, 在 2023 年伊朗国家队选拔考试第六题中也出现了这个点.

(2). 山东省东营市第一中学扈景轩, 东北师大附中白淞禹, 广饶一中李耀文,广州大学附属中学何金喜, 广州市天河外国语学校陈泓道, 宁波市第十五中学庄子曰, 武汉市七一中学杨子奥, 长沙市一中李俊贤、黄诚、刘恒宇, 温州中学徐吴祁,人大附中杨元䉀, 华南师范大学附属中学彭子晋, 天津市第一中学张航领等同学也给出了本题的正确解答.

第三题 给定正整数 $k$. 对于一条由 $k$ 条线段组成的不自交的折线 (相邻的两条线段不共线), 考虑每条线段所在的直线, 求这样的直线条数的最小值.

(北大附中学生 高学文 供题)

## 解 (根据供题者的解答整理):

记

$$
a_{n}=n\left[\frac{n-1}{2}\right]+\frac{3+(-1)^{n}}{2}=\left\{\begin{array}{ll}
\frac{1}{2}\left(n^{2}-n\right)+1, & n \text { 是奇数 } \\
\frac{1}{2}\left(n^{2}-2 n\right)+2, & n \text { 是偶数 }
\end{array},\right.
$$

则 $\left\{a_{n}\right\}$ 是递增的正整数数列, 且 $a_{1}=1, a_{2}=2$.

记 $m=\min _{a_{n} \geq k} n$, 我们证明直线条数的最小值为 $m$.

当 $k=1$ 时 $m=1$, 当 $k=2$ 时 $m=2$, 结论均显然成立.

当 $k \geq 3$ 时, 设折线为 $P_{0} P_{1} \cdots P_{k}, P_{0} P_{1}, P_{1} P_{2}, \cdots, P_{k-1} P_{k}$ 所在的不同直线为 $l_{1}, l_{2}, \cdots, l_{x}$, 其中任两条直线的交点称为结点.

先证明 $x \geq m$.

当 $x$ 是奇数时, 因为 $P_{1}, P_{2}, \cdots, P_{k-1}$ 是互异的结点, 所以 $k-1 \leq \mathrm{C}_{x}^{2}=a_{x}-1$.于是 $a_{x} \geq k$, 故 $x \geq m$.

当 $x$ 是偶数时, 由 $l_{i}$ 上至多有 $x-1$ 个结点, 知 $P_{1} P_{2}, P_{2} P_{3}, \cdots, P_{k-2} P_{k-1}$ 中至多有 $\left[\frac{x-1}{2}\right]$ 条在 $l_{i}$ 上 (相邻两条不同在 $l_{i}$ 上). 因为 $l_{1}, l_{2}, \cdots, l_{x}$ 包含 $P_{1} P_{2}, P_{2} P_{3}, \cdots$, $P_{k-2} P_{k-1}$, 所以 $k-2 \leq x \cdot\left[\frac{x-1}{2}\right]=a_{x}-2$. 于是 $a_{x} \geq k$, 故 $x \geq m$.

再证明存在由 $k$ 条线段组成的不自交的折线被 $m$ 条直线包含.

只需构造 $k=a_{m}$ 时的情形.

设 $n$ 是大于 2 的偶数.

当 $m=n-1$ 时, 设 $A_{1}, A_{2}, \cdots, A_{n-1}$ 是正 $n-1$ 边形的顶点, 按逆时针排列.令直线 $l_{i}=A_{i} A_{i+\frac{n}{2}-1}(1 \leq i \leq n-1)$, 下标按模 $n-1$ 理解.
对 $1,2, \cdots, \frac{n}{2}-1$ 中与 $\frac{n}{2}-1$ 同奇偶的 $t$, 先将如下多边形的边染上红色, 其余边染上黑色:

$$
Q_{1,1+t} Q_{1+t, 2} Q_{2,2+t} Q_{2+t, 3} \cdots Q_{n-1, n-1+t} Q_{n-1+t, 1}
$$

其中 $Q_{i, j}$ 是 $l_{i}$ 与 $l_{j}$ 的交点, 且将 $Q_{i, i}$ 忽略. 记 $A_{1} A_{\frac{n}{2}+1}$ 上从 $A_{1}$ 开始的第 $2\left[\frac{n}{4}\right]$ 个点为 $C$, 再将线段 $A_{1} C$ 上的红与黑互换.

此时红色线段即为满足要求的折线（不计最两端的线段）, 下图是 $m=11$ 时的例子:

![](https://cdn.mathpix.com/cropped/2024_02_26_d69edc3f1453fb5435eeg-6.jpg?height=599&width=606&top_left_y=774&top_left_x=745)

当 $m=n$ 时, 先作直线 $l$ 平行于 $l_{\frac{n}{2}+1}$, 且 $A_{2} \sim A_{\frac{n}{2}}$ 位于 $l$ 与 $l_{\frac{n}{2}+1}$ 之间. 再将 $l$逆时针旋转一个小角度得到直线 $l_{n}$.

设 $l_{\frac{n}{2}+1}$ 与 $l_{n}$ 交于点 $B_{1}$, 再对 $2 \leq k \leq \frac{n}{2}$, 设过 $A_{k}$ 的两条直线交 $l_{n}$ 于点 $B_{2 k-2}, B_{2 k-1}$, 使得 $B_{1}, B_{2}, \cdots, B_{n-1}$ 在 $l_{n}$ 上顺次排列.

在 $m=n-1$ 的基础上将 $A_{k} Q_{k-1, \frac{n}{2}+k}, A_{k} Q_{k, \frac{n}{2}+k}\left(2 \leq k \leq \frac{n}{2}-1\right)$ 及 $A_{\frac{n}{2}} Q_{\frac{n}{2}-1,1}$染黑, 将 $A_{1} B_{1}, B_{n-3} B_{n-1}, B_{n-1} A_{\frac{n}{2}}$ 及 $B_{2 k-3} B_{2 k-2}, A_{k} B_{2 k-2}, A_{k} B_{2 k-1}\left(2 \leq k \leq \frac{n}{2}-1\right)$染红.

此时红色线段即为满足要求的折线 (不计最两端的线段), 下图是 $m=8$ 时的例子:

![](https://cdn.mathpix.com/cropped/2024_02_26_d69edc3f1453fb5435eeg-6.jpg?height=292&width=1083&top_left_y=2107&top_left_x=478)

综上, 所求为最小的正整数 $n$, 使得

$$
n\left[\frac{n-1}{2}\right]+\frac{3+(-1)^{n}}{2} \geq k .
$$

评注 人大附中杨元簏, 华南师范大学附属中学彭子晋, 天津市第一中学张航领, 江苏省锡山高级中学宣则宁等同学也给出了本题的正确解答.

第四题 求所有的函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意实数 $x, y$, 均有

$$
f\left(x^{3}\right)+f\left(y^{3}\right)=\left(f\left(x^{2}\right)-f(x y)+f\left(y^{2}\right)\right)(f(x)+f(y)),
$$

且 $f$ 在 $(2,3)$ 上单调.

(上海中学学生 杨镇 供题)

## 解 (根据浙江学军文渊中学董镇宇同学的解答整理):

记原方程为 $P(x, y)$.

由 $P(0,0)$ 知 $f(0)=f(0)^{2}$, 所以 $f(0)=0$ 或 1 .

由 $P(x, 0)$ 知 $f\left(x^{3}\right)+f(0)=f\left(x^{2}\right)(f(x)+f(0))$; 由 $P(x, x)$ 知 $f\left(x^{3}\right)=f\left(x^{2}\right) f(x)$.结合两式知 $f(0)=f\left(x^{2}\right) f(0)$.

情形 $1 f(0)=1$.

此时 $f\left(x^{2}\right)=1$, 所以 $f\left(x^{3}\right)=f(x)$, 且对任意 $x \geq 0$ 均有 $f(x)=1$. 代回原方程得, $f(x)+f(y)=(1-f(x y)+1)(f(x)+f(y))$, 即

$$
(f(x)+f(y))(f(x y)-1)=0 .
$$

令 $x>0, y<0$ 得, $f(y)=-1$ 或 $f(x y)=1$.

若存在 $y<0$ 使 $f(y) \neq-1$, 则对任意 $x>0$ 均有 $f(x y)=1$. 由此知对任意 $y<0$ 均有 $f(y)=1$, 进而 $f(x) \equiv 1$.

若对任意 $y<0$ 均有 $f(y)=-1$, 则 $f(x)=\left\{\begin{array}{ll}1, & x \geq 0 \\ -1, & x<0\end{array}\right.$.

情形 $2 \quad f(0)=0$.

由 $f\left(x^{3}\right)=f\left(x^{2}\right) f(x)$ 知 $f(1)=f(1)^{2}$, 所以 $f(1)=0$ 或 1 .

情形 $2.1 f(1)=0$ 时, 由 $P(x, 1)$ 知

$$
f\left(x^{3}\right)=\left(f\left(x^{2}\right)-f(x)\right) f(x)=f\left(x^{3}\right)-f(x)^{2},
$$

所以 $f(x)^{2}=0$, 即 $f(x) \equiv 0$.

情形 $2.2 f(1)=1$ 时, 由 $P(x, 1)$ 知

$$
\begin{aligned}
f\left(x^{3}\right)+1 & =\left(f\left(x^{2}\right)-f(x)+1\right)(f(x)+1) \\
& =f\left(x^{3}\right)+f\left(x^{2}\right)-f(x)^{2}+1,
\end{aligned}
$$

于是 $f\left(x^{2}\right)=f(x)^{2}$, 从而 $f\left(x^{3}\right)=f\left(x^{2}\right) f(x)=f(x)^{3}$, 且对任意 $x \geq 0$ 均有 $f(x) \geq 0$.
代回原方程得，

$$
f(x)^{3}+f(y)^{3}=\left(f(x)^{2}-f(x y)+f(y)^{2}\right)(f(x)+f(y)),
$$

即

$$
(f(x)+f(y))(f(x y)-f(x) f(y))=0,
$$

所以 $f(x)+f(y)=0$ 或 $f(x y)=f(x) f(y)$.

因为 $f\left(x^{2}\right)=f(x)^{2}, f\left(x^{3}\right)=f(x)^{3}$, 所以由 $f(x)$ 在 $(2,3)$ 上单调, 知 $f(x)$在 $(4,9),(8,27),(16,81), \cdots$ 上均单调. 于是 $f(x)$ 在 $[5,25]$ 上单调, 进而 $f(x)$ 在 $[\sqrt{5}, 5],[\sqrt[4]{5}, \sqrt{5}], \cdots$ 上单调. 故 $f(x)$ 在 $(1,+\infty)$ 上单调.

(1) 存在 $t>1$ 使 $f(t)=0$ 时, 由 $f$ 在 $[1,+\infty)$ 上非负且单调, 知 $f(x)$ 在 $(1, t]$上恒为 0 或在 $[t,+\infty)$ 上恒为 0 . 因为 $f\left(x^{2}\right)=f(x)^{2}$, 所以对任意 $x>1$ 均有 $f(x)=0$.

对 $0<x<1, f\left(\frac{1}{x}\right)=0$. 由 $(*)$ 知 $f(x)+f\left(\frac{1}{x}\right)=0$ 或 $f(x) f\left(\frac{1}{x}\right)=f(1)=1$, 所以只能为前者且 $f(x)=0$.

在 $(*)$ 中令 $x<0, y>0, y \neq 1$ 得 $f(x)=0$ 或 $f(x y)=0$. 对任意 $x, z<0, x \neq$ $z$, 若 $f(x) \neq 0$, 则 $f(z)=f\left(x \cdot \frac{z}{x}\right)=0$. 故当 $x<0$ 时 $f(x)$ 至多有一个不为 0 .

由 $f(-1)^{2}=f(1)=1$ 知 $f(-1)= \pm 1$, 所以 $f(x)=\left\{\begin{array}{ll} \pm 1, & x=-1 \\ 0, & x<0, x \neq-1\end{array}\right.$.

故 $f(x)=\left\{\begin{array}{ll}1, & x= \pm 1 \\ 0, & x \neq \pm 1\end{array}\right.$ 或 $f(x)= \begin{cases}1, & x=1 \\ -1, & x=-1 . \\ 0, & x \neq \pm 1\end{cases}$

(2) 对任意 $t>1$ 均有 $f(t) \neq 0$ 时, 对任意 $x, y>1$ 均有 $f(x y)=f(x) f(y)$.

令 $g(x)=\ln f\left(e^{x}\right), x>0$, 则 $g(x+y)=g(x)+g(y)$, 且由 $f$ 单调知 $g$ 单调. 由柯西方程的理论, 知存在实数 $k$ 使 $g(x)=k x$, 于是 $f(x)=x^{k}, x>1$.

对 $0<x<1$, 由 $f(x)$ 在 $[0,+\infty)$ 上非负及 $(*)$, 知 $f(x) f\left(\frac{1}{x}\right)=f(1)=1$, 所以 $f(x)=x^{k}, 0<x<1$.

对 $x<0, f(x)^{2}=f\left(x^{2}\right)=x^{2 k}$, 所以 $f(x)=|x|^{k}$ 或 $-|x|^{k}$.

若存在 $t, s<0$ 使 $f(t)<0, f(s)>0$, 则 $t \neq s$.

在 $(*)$ 中令 $x=t, y=s$, 由 $f(t s)>0>f(t) f(s)$ 知 $f(t)+f(s)=0$, 于是 $(-t)^{k}=(-s)^{k}$. 所以 $k=0$, 故当 $x>0$ 时 $f(x)=1$, 当 $x<0$ 时 $f(x)= \pm 1$.

在 $(*)$ 中令 $x<0, y>0$ 得 $f(x)=-1$ 或 $f(x y)=f(x)$. 注意 $f(s)=1$, 所以对任意 $y>0$ 有 $f(s y)=f(s)=1$, 特别取 $y=\frac{t}{s}$ 知 $f(t)=1$, 矛盾!
从而当 $x<0$ 时 $f(x)=|x|^{k}$ 或 $f(x)=-|x|^{k}$.

故 $f(x)=\left\{\begin{array}{ll}0, & x=0 \\ |x|^{k}, & x \neq 0\end{array}\right.$ 或 $f(x)= \begin{cases}0, & x=0 \\ |x|^{k}, & x>0 . \\ -|x|^{k}, & x<0\end{cases}$

综上, 所求 $f(x)$ 有 7 个: $f(x) \equiv 0 ; f(x) \equiv 1 ; f(x)=\left\{\begin{array}{ll}1, & x \geq 0 \\ -1, & x<0\end{array}\right.$;

$f(x)=\left\{\begin{array}{ll}1, & x= \pm 1 \\ 0, & x \neq \pm 1\end{array} ; f(x)=\left\{\begin{array}{ll}1, & x=1 \\ -1, & x=-1 ; \\ 0, & x \neq \pm 1\end{array} ; f(x)=\left\{\begin{array}{ll}0, & x=0 \\ |x|^{k}, & x \neq 0\end{array}(k \in \mathbb{R}) ;\right.\right.\right.$

$f(x)= \begin{cases}0, & x=0 \\ |x|^{k}, & x>0(k \in \mathbb{R}), \text { 均容易验证满足原方程. } \\ -|x|^{k}, & x<0\end{cases}$

评注 (1). 本题中的 “单调” 指的是不严格单调, 有同学只解决了严格单调的情形.

(2). 温州中学徐昊祁, 人大附中杨元䉀、孟繁钰, 天津市第一中学张航领等同学也给出了本题的正确解答.

