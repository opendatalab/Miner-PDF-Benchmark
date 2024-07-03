# $\mathrm{KöMaL}$ 征解问题 A. 764 的一个解答 

王琇<br>(湖南师范大学附属中学, 410006)<br>指导教师: 汤礼达

匈牙利数学杂志 $\mathrm{KöMaL}$ 在 2019 年 12 月的一道征解问题如下:
A. 764 称多边形的一条对角线是“好的”，如果其完全在该多边形的内部或外侧. 证明: 对任意一个 $n$ 边形, 其至少有 $\frac{3}{2}(n-3)$ 条对角线是好的.

本文将给出上述问题的一个解答, 并说明所给下界是最佳的.

证明 设所给多边形为 $P, P$ 的顶点的集合为 $V, V$ 的凸包为 $\Omega$. 因为 $V$ 是 $\mathbb{R}^{2}$ 上的有限点集, 任三点不共线, 故存在 $P$ 的三角剖分(即一个以 $V$ 为顶点集合的平面图, 其每个面均为三角形).

$P$ 的边界与 $\Omega$ 的边界围成了若干个多边形, 同样地可以对这些多边形进行三角剖分. 这样一来我们得到了 $\Omega$ 的一个三角剖分 $\mathcal{T}$, 使得 $P$ 的各边均为 $\mathcal{T}$ 所得的线段.
![](https://cdn.mathpix.com/cropped/2024_02_26_1b9631eb217cf99205fbg-1.jpg?height=290&width=712&top_left_y=1806&top_left_x=681)

用 $E$ 表示三角剖分 $\mathcal{T}$ 所得线段组成的集合. 设集合

$$
\begin{gathered}
A=\{e \in E \mid e \text { 在 } \Omega \text { 的边界上, 且 } e \text { 是 } P \text { 的边 }\}, \\
B=\{e \in E \mid e \text { 在 } \Omega \text { 的边界上, 且 } e \text { 不是 } P \text { 的边 }\}, \\
C=\{e \in E \mid e \text { 在 } \Omega \text { 的内部, 且 } e \text { 是 } P \text { 的边 }\},
\end{gathered}
$$

$$
D=\{e \in E \mid e \text { 在 } \Omega \text { 的内部, 且 } e \text { 不是 } P \text { 的边 }\} \text {. }
$$

并记 $|A|=a,|B|=b,|C|=c,|D|=d$.

因为 $P$ 恰有 $n$ 条边, 故 $a+c=n$. 下面证明 $a+2 b \leqslant n$.

事实上, 对任意 $e \in B, P$ 的边界被 $e$ 的两端点分为两段, 其中一段落在 $e$ 与另一段边界围成的多边形内部. 设这一段的边组成集合 $I(e)$, 则显然 $I(e) \subseteq C,|I(e)| \geqslant 2$. 注意到 $I(e)(e \in B)$ 两两不相交, 故

$$
2 b \leqslant \bigcup_{e \in B}|I(e)| \leqslant c
$$

即 $a+2 b \leqslant a+c=n$.

因为 $\Omega$ 的边界上顶点数目恰为 $a+b$, 所以 $\Omega$ 内部的顶点数目恰为 $n-a-b$.

引理 $1 . a+2 b+d=2 n-3$.

证明 进行基本的计数. 设 $\mathcal{T}$ 有 $k$ 个面, 则由 Euler 公式可得

$$
n-(a+b+c+d)+k=1 .
$$

由于 $\mathcal{T}$ 的每个面都是三角形, 故对 $E$ 中的线段算两次可得

$$
3 k=(a+b)+2(c+d)
$$

将上式代入消去 $k$ 得

$$
2 a+2 b+c+d=3 n-3 .
$$

结合 $a+c=n$ 消去 $c$ 即知 $a+2 b+d=2 n-3$. 引理 1 得证.

显然 $B \cup D$ 中的元素均为好的对角线, 因此如果 $a+b \leqslant \frac{n+3}{2}$, 则由引理 1 有

$$
b+d=(a+2 b+d)-(a+b) \geqslant(2 n-3)-\frac{n+3}{2}=\frac{3}{2}(n-3)
$$

知此时结论成立. 下面假设 $a+b>\frac{n+3}{2}$, 则由 $a+2 b \leqslant n$ 知 $b<\frac{n-3}{2}$.

对任意 $e \in D$, 因为 $e$ 在 $\Omega$ 的内部, 故恰有两个 $\mathcal{T}$ 的三角形面以 $e$ 为边. 这两个三角形除了共用 $e$ 之外还有四条边, 如果这四条边顺次围成一个凸四边形,那么此凸四边形异于 $e$ 的对角线也是好的,并且不属于 $B \cup D$. 这样的 $e$ 称为 “极好的”, 下面估计极好的线段数.

如果 $e \in D$ 不是极好的, 由 $V$ 中任意三点不共线知恰存在 $e$ 的一个端点 $v$,使得上述两个三角形在 $v$ 处的内角和大于 $\pi$, 这样的 $v$ 当然在 $\Omega$ 的内部. 将这样的 $e$ 与 $v$ 配成一个对子, 则每个不是极好的 $e$ 恰在一个对子中.

引理 2. 每个 $\Omega$ 内部的顶点 $v$ 至多在两个对子中.
![](https://cdn.mathpix.com/cropped/2024_02_26_1b9631eb217cf99205fbg-3.jpg?height=308&width=648&top_left_y=203&top_left_x=705)

证明 考虑全体以 $v$ 为端点的 $E$ 中线段 $e_{1}, e_{2}, \ldots, e_{k}, e_{i}$ 逆时针旋转到 $e_{i+1}$ 的角度为 $\theta_{i} \in(0, \pi)$ (下标模 $k$ 理解, 如图是 $k=5$ 的情形), 只要证明至多有两个 $i$ 使得 $e_{i} \in D$ 且 $\theta_{i-1}+\theta_{i}>\pi$.

![](https://cdn.mathpix.com/cropped/2024_02_26_1b9631eb217cf99205fbg-3.jpg?height=494&width=491&top_left_y=827&top_left_x=788)

1. $k \geq 4$. 若存在 $1 \leqslant i<j \leqslant n, 1<j-i<n-1$ 使得 $\theta_{i-1}+\theta_{i}>\pi$, $\theta_{j-1}+\theta_{j}>\pi$, 则

$$
2 \pi=\theta_{1}+\theta_{2}+\ldots \theta_{k} \geqslant\left(\theta_{i-1}+\theta_{i}\right)+\left(\theta_{j-1}+\theta_{j}\right)>2 \pi
$$

矛盾! 由此易知至多有两个 $i$ 满足 $\theta_{i-1}+\theta_{i}>\pi$.
2. $k=3$. 因为 $v$ 是 $P$ 的顶点, 故至少两个 $e_{i}$ 不属于 $D$, 余下至多一个 $e_{i} \in D$, 结论当然成立. 引理 2 得证.

由引理 2 , 不是极好的线段数目至多为 $2(n-a-b)$, 故至少有 $d-2(n-a-b)$ 条极好的线段.

每条极好的线段对应着一条不在 $B \cup D$ 中的好的对角线, 显然这样的对应是单射. 故综上所述, 好的对角线数目至少为

$$
\begin{aligned}
(b+d)+d-2(n-a-b) & =2 a+3 b+2 d-2 n \\
& =2(a+2 b+d)-b-2 n \\
& \left.\geqslant 2(2 n-3)-\frac{n-3}{2}-2 n \quad \text { (用到了引理 } 1\right) \\
& =\frac{3}{2}(n-3) .
\end{aligned}
$$

故原题得证.
我们可以对每个 $n \geqslant 3$ 给出相应的多边形 $P$, 使得 $P$ 中恰有 $\left\lceil\frac{3}{2}(n-3)\right\rceil$ 条好的对角线. 由此便说明了原题中下界的最优性.

构造 1. $n=2 k+1$. 在单位圆上取点 $A_{1}, A_{2}, \ldots, A_{2 k}$, 使得 $A_{2 i-1}, A_{2 i}$ 的纵坐标均为 $\frac{i}{10 k}$, 且 $A_{2 i-1}$ 在 $A_{2 i}$ 的左边 $(1 \leqslant i \leqslant k)$. 过 $A_{1}, A_{2 k}$ 作单位圆的切线相交于点 $A_{2 k+1}$, 并令 $P=A_{1} A_{2} \ldots A_{2 k+1} A_{1}$.

此时好的对角线有且仅有

$$
A_{2 i-1} A_{2 i+1}, A_{2 i} A_{2 i+2}, A_{2 k+1} A_{2 i+1}(1 \leqslant i \leqslant k-1)
$$

一共 $3(k-1)=\left\lceil\frac{3}{2}(n-3)\right\rceil$ 条.

![](https://cdn.mathpix.com/cropped/2024_02_26_1b9631eb217cf99205fbg-4.jpg?height=388&width=574&top_left_y=871&top_left_x=747)
2. $n=2 k$. 只需要在 $n=2 k+1$ 时的构造中, 将边 $A_{2 k-1} A_{2 k}, A_{2 k} A_{2 k+1}$ 替换为边 $A_{2 k-1} A_{2 k+1}$ 即可.

此时好的对角线有且仅有

$$
\begin{gathered}
A_{2 i} A_{2 i+2}, A_{2 k+1} A_{2 i+1}(1 \leqslant i \leqslant k-2) ; \\
A_{2 i-1} A_{2 i+1}(1 \leqslant i \leqslant k-1) ;
\end{gathered}
$$

$$
A_{2 k-2} A_{2 k+1},
$$

一共 $2(k-2)+(k-1)+1=\left\lceil\frac{3}{2}(n-3)\right\rceil$ 条.

![](https://cdn.mathpix.com/cropped/2024_02_26_1b9631eb217cf99205fbg-4.jpg?height=388&width=580&top_left_y=1973&top_left_x=744)

评注 首要的问题在于如何判定一条对角线是好的, 因此我们的基本想法是研究 $P$ 的三角剖分. 剖分所得三角形的边要么是 $P$ 的边, 要么是完全在 $P$ 内
部的好的对角线, 满足要求. 进一步由于题述允许完全在外侧的对角线, 故转而考虑凸包的三角剖分.

经过计数可以发现在某些情况下问题已经解决, 其余情形我们希望找到更多的好对角线. 因为三角剖分通常不止一种, 所以可以在一些局部位置进行调整, 这就引发我们考虑极好的对角线以及其对应的凸四边形. 从而得到以上证明.

构造部分则相对简单, 我们借用了与 2019 年罗马尼亚大师杯第四题相类似的“漏斗形”结构, 这可以让 $P$ 内部的对角线尽量少. 为了减少 $P$ 外侧的对角线数目, 我们让“漏斗”伸出很多根“刺”即可达到要求.

致谢 感谢李先颖博士提出的宝贵建议.

