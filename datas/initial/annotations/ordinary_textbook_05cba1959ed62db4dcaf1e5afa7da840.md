数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2023 年保加利亚数学奥林匹克试题解析 

李汝曦 金逸航 高海岩

(长沙市长郡中学, 410002)

指导教师: 周豪

2023 年保加利亚数学奥林匹克于 4 月 8 日、 9 日两天举行. 下面笔者整理了试题及其解答, 并作了简要的评析, 供读者参考. 因笔者水平有限, 有不当之处, 恳请读者批评指正.

## I. 试 题

1. 设 $G$ 是一个至少具有六个顶点的图, 每个顶点都至少具有 3 的度数. 如果 $C_{1}, C_{2}, \cdots, C_{k}$ 是 $G$ 中所有的环, 则确定 $\operatorname{gcd}\left(\left|C_{1}\right|,\left|C_{2}\right|, \cdots,\left|C_{k}\right|\right)$ 的所有可能值, 其中 $|C|$ 表示环 $C$ 中顶点的数量.
2. 设 $\triangle A B C$ 是一个锐角三角形, $A_{1}, B_{1}, C_{1}$ 分别是与线段 $B C, C A, A B$ 相切的三个旁切圆的切点. $O_{A}, O_{B}, O_{C}$ 分别是 $\triangle A B_{1} C_{1}, \triangle B C_{1} A_{1}, \triangle C A_{1} B_{1}$ 的外心. 证明: 通过 $O_{A}, O_{B}, O_{C}$ 且分别平行于 $\angle A, \angle B, \angle C$ 的角平分线的三条直线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_a2b1edf600157b22d4d8g-01.jpg?height=499&width=714&top_left_y=1895&top_left_x=677)

3. 设 $f(x)$ 是一个具有正整数系数的多项式. 对于每个自然数 $n$, 让

修订日期: 2023-06-26.
$a_{1}^{(n)}, a_{2}^{(n)}, \cdots, a_{n}^{(n)}$ 为给定正整数, 它们在模 $n$ 时两两不同余, 且定义

$$
g(n)=\sum_{i=1}^{n} f\left(a_{i}^{(n)}\right)=f\left(a_{1}^{(n)}\right)+f\left(a_{2}^{(n)}\right)+\cdots+f\left(a_{n}^{(n)}\right) .
$$

证明: 存在一个常数 $M$, 使得对于所有满足 $m>M$ 的整数 $m$, 都有

$$
\operatorname{gcd}(m, g(m))>2023^{2023} .
$$

4. 证明: 存在唯一的点 $M$ 在凸四边形 $A B C D$ 的边 $A D$ 上, 使得当且仅当 $A B / / C D$ 时, $\sqrt{S_{A B M}}+\sqrt{S_{C D M}}=\sqrt{S_{A B C D}}$. 其中 $S_{X Y Z}$ 表示 $\triangle X Y Z$ 的面积.
5. 已知 $x_{1}, x_{2}, \cdots, x_{n}$ 是实数, 且满足 $\left|x_{1}\right|+\left|x_{2}\right|+\cdots+\left|x_{n}\right|=1$. 对于每个正整数 $n$, 试确定表达式

$$
\left|x_{1}\right|+\left|x_{1}-x_{2}\right|+\left|x_{1}+x_{2}-x_{3}\right|+\cdots+\left|x_{1}+x_{2}+\cdots+x_{n-1}-x_{n}\right|
$$

的最小可能值.

6. 在一个班级中有 26 名学生, 每个人有 5 个科目的成绩, 成绩分为三种可能的分数. 证明: 如果其中 25 名学生已经获得了他们的成绩, 那么我们可以对最后一名学生进行评分, 使得他的分数与任何其他学生在至少两个科目上不同.

## II. 解答与评注

题 1 设 $G$ 是一个至少具有六个顶点的图, 每个顶点都至少具有 3 的度数.如果 $C_{1}, C_{2}, \cdots, C_{k}$ 是 $G$ 中所有的环, 则确定 $\operatorname{gcd}\left(\left|C_{1}\right|,\left|C_{2}\right|, \cdots,\left|C_{k}\right|\right)$ 的所有可能值, 其中 $|C|$ 表示环 $C$ 中顶点的数量.

解 答案: $\operatorname{gcd}\left(\left|C_{1}\right|,\left|C_{2}\right|, \cdots,\left|C_{k}\right|\right)=1$ 或 2 .

对于简单图 $G$, 考虑 $G$ 中的极长路, 则其一个端点 $A$ 的邻域仅在此路中.

我们定义这条极长路为 $A V_{1} \cdots V_{t}\left(t \in \mathbb{N}^{*}\right)$. 由于 $d(A) \geq 3$, 知 $A$ 除了与 $V_{1}$相邻外, 还至少与异于 $V_{1}$ 的两点 $V_{i}, V_{j}$ 相邻 $(i \neq j),\{i, j\} \subseteq\{1,2, \cdots, t\}$.

由路的极长性, 知图 $G$ 中有如下的圈:

$$
\begin{array}{ll}
C_{1}: A V_{1} V_{2} \cdots V_{i} A, & \left|C_{1}\right|=i+1 ; \\
C_{2}: A V_{i} \cdots V_{j} A, & \left|C_{2}\right|=j-i+2 ; \\
C_{3}: A V_{1} V_{2} \cdots V_{j} A, & \left|C_{3}\right|=j+1 .
\end{array}
$$

故知

$$
\begin{aligned}
\operatorname{gcd}\left(\left|C_{1}\right|,\left|C_{2}\right|, \cdots,\left|C_{k}\right|\right) \mid \operatorname{gcd}\left(\left|C_{1}\right|,\left|C_{2}\right|,\left|C_{3}\right|\right) & =\operatorname{gcd}(i+1, j-i+2, j+1) \\
& =\operatorname{gcd}(i+1,2, j+1) \mid 2 .
\end{aligned}
$$

所以 $\operatorname{gcd}\left(\left|C_{1}\right|, \cdots\left|C_{k}\right|\right)$ 为 1 或 2 .

构造如下:

(1) $\operatorname{gcd}\left(\left|C_{1}\right|, \cdots,\left|C_{k}\right|\right)=1, K_{6}$ 即可.

(2) $\operatorname{gcd}\left(\left|C_{1}\right|, \cdots,\left|C_{k}\right|\right)=2$, 如图.

![](https://cdn.mathpix.com/cropped/2024_02_26_a2b1edf600157b22d4d8g-03.jpg?height=543&width=556&top_left_y=505&top_left_x=750)

所以 $\operatorname{gcd}\left(\left|C_{1}\right|, \cdots\left|C_{k}\right|\right)$ 为 1 或 2 .

评注 这是一道较为简单的图论问题. 我们可以通过相互之间有关系的多个带弦圈分析, 从而限制最大公因数的取值. 这里一个常见的手段就是极长路分析.

题 2 设 $\triangle A B C$ 是一个锐角三角形, $A_{1}, B_{1}, C_{1}$ 分别是与线段 $B C, C A, A B$相切的三个旁切圆的切点. $O_{A}, O_{B}, O_{C}$ 分别是 $\triangle A B_{1} C_{1}, \triangle B C_{1} A_{1}, \triangle C A_{1} B_{1}$ 的外心. 证明: 通过 $O_{A}, O_{B}, O_{C}$ 且分别平行于 $\angle A, \angle B, \angle C$ 的角平分线的三条直线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_a2b1edf600157b22d4d8g-03.jpg?height=457&width=642&top_left_y=1802&top_left_x=707)

证明 1 考虑 $\triangle A B C$ 的旁心三角形 $I_{A} I_{B} I_{C}$ 及内心 $I$, 熟知 $I_{A} I_{B} I_{C} I$ 为垂心组.

从 $I_{A}$ 引 $B C$ 的垂线 $l_{A}$, 类似地定义 $l_{B}, l_{C}$. 由于 $I_{A} A \perp I_{C} I_{B}$ 及 $I_{C}, B, C, I_{B}$四点共圆, 知 $l_{A}, I_{A} I$ 为 $\angle B I_{A} C$ 的等角线. 同理, $l_{B}, I_{B} I$ 为 $\angle C I_{B} A$ 的等角线,
$l_{C}, I_{C} I$ 为 $\angle B I_{C} A$ 的等角线. 所以 $l_{A}, l_{B}, l_{C}$ 交于点 $I$ 关于 $\triangle I_{A} I_{B} I_{C}$ 的等角共轪点 $Y$.

因为

$\angle Y A_{1} B=\angle Y C_{1} B=90^{\circ}, \angle Y C_{1} A=\angle Y B_{1} A=90^{\circ}, \angle Y A_{1} C=\angle Y B_{1} C=90^{\circ}$,

所以 $O_{A}, O_{B}, O_{C}$ 为 $A Y, B Y, C Y$ 的中点. 所以 $\triangle O_{A} O_{B} O_{C}$ 与 $\triangle A B C$ 位似.则通过 $O_{A}, O_{B}, O_{C}$ 且分别平行于 $\angle A, \angle B, \angle C$ 的角平分线的三条直线交于 $\triangle O_{A} O_{B} O_{C}$ 的内心 $X$, 即证.

评注 这是一道偏中档难度的几何题. 通过“过三个旁切圆切点引出的对应边垂线交于一点”这一熟知结论进一步导出位似即可. 对于这样的三共圆问题.使用 Miquel 点刻画是相当方便的.

![](https://cdn.mathpix.com/cropped/2024_02_26_a2b1edf600157b22d4d8g-04.jpg?height=565&width=562&top_left_y=1054&top_left_x=747)

证明 2 如图, 作 $\triangle A B C$ 外接圆 $O$, 内心 $I$, 取优弧 $(A C B) 、(B A C) 、(A B C)$的中点 $X, Y, Z$.

由于

$$
A B_{1}=B A_{1}=\frac{1}{2}(A B+A C-B C), X A=X B, \angle B_{1} A X=\angle A_{1} B X
$$

所以 $\triangle A B_{1} X \cong \triangle B A_{1} X$, 得 $\angle C B_{1} X=\angle C A_{1} X$, 知 $B_{1} C X A_{1}$ 四点共圆.

又

$$
\angle B C X=\angle B A X=\frac{1}{2}\left(180^{\circ}-\angle A X B\right)=90^{\circ}-\frac{1}{2} \angle A C B \text {, }
$$

所以 $\angle I C X=\angle B C X+\angle B C I=90^{\circ}$, 即 $I C \perp C X$.

同理 $I A \perp A Y, I B \perp B Z$.

故知 $O_{A}, O$ 均在 $A Y$ 的垂直平分线上, $O_{B}, O$ 均在 $B Z$ 的垂直平分线上, $O_{C}, O$ 均在 $C X$ 的垂直平分线上. 从而 $O_{B} O / / I B, O_{A} O / / I A, O_{C} O / / I C$.

所以所求三线共点于外心 $O$.
评注 这个解法需要一定的观察力, 我们猜测到了三线共的点是 $\triangle A B C$ 的外心，由于 $O_{A}, O_{B}, O_{C}$ 也是外心, 通过两圆的公共弦的垂直平分线进行刻画，从而导出 $O O_{A}, O O_{B}, O O_{C}$ 分别平行于三条角平分线, 证明了结论. 要注意到, 轮换的全等构造是常用的手法.

题 3 设 $f(x)$ 是一个具有正整数系数的多项式. 对于每个自然数 $n$, 让 $a_{1}^{(n)}, a_{2}^{(n)}, \cdots, a_{n}^{(n)}$ 为给定正整数, 它们在模 $n$ 时两两不同余, 且定义

$$
g(n)=\sum_{i=1}^{n} f\left(a_{i}^{(n)}\right)=f\left(a_{1}^{(n)}\right)+f\left(a_{2}^{(n)}\right)+\cdots+f\left(a_{n}^{(n)}\right) .
$$

证明: 存在一个常数 $M$, 使得对于所有满足 $m>M$ 的整数 $m$, 都有

$$
\operatorname{gcd}(m, g(m))>2023^{2023}
$$

证明 1 先证明如下引理:

引理 对于 $n, d \in \mathbb{N}^{*}$, 记 $f(n, d)=\sum_{k=1} k^{d}$. 则 $f(n, d)$ 可以表示为 $\frac{n g(n, d)}{h(d)}$ 的形式, 其中 $h(d)$ 为与 $d$ 有关的常数, $g(n, d)$ 为与 $n$ 有关的整系数多项式.

证明 我们对 $d$ 归纳地证明问题:

(1) 首先 $f(n, 1)=\frac{n(n+1)}{2}$, 故 $d=1$ 时, 取 $g(n, 1)=n+1, h(1)=2$ 即可.

(2) 假若命题在 $1,2, \cdots, d-1$ 的情形均成立时, 讨论命题在 $d$ 的情形:

注意到 $(n+1)^{d+1}-n^{d+1}$ 二项式展开为 $\sum_{i=0}^{d} C_{d+1}^{i} n^{i}$. 所以

$$
\begin{aligned}
(n+1)^{d+1}-1^{d+1} & =\sum_{k=1}^{n}\left((k+1)^{d+1}-k^{d+1}\right) \\
& =\sum_{k=1}^{n} \sum_{i=0}^{d} C_{d+1}^{i} k^{i}=\sum_{i=0}^{d} C_{d+1}^{i}\left(\sum_{k=1}^{n} k^{i}\right) \\
& =\sum_{i=0}^{d} C_{d+1}^{i} f(n, i) .
\end{aligned}
$$

故

$$
(d+1) f(n, d)=n\left(n^{d}+C_{d+1}^{1} n^{d-1}+\cdots+C_{d+1}^{2} n+C_{d+1}^{1}\right)-\sum_{i=0}^{d-1} C_{d+1}^{i} f(n, i)
$$

对右式用 $i=0,1, \cdots d-1$ 的归纳假设, 通分后将两边同除以 $d+1$ 即知 $f(n, d)$成立. 故归纳假设成立, 引理得证.

回到原题. 由于 $f \in \mathbb{Z}_{+}[x]$, 不妨设 $f(x)=\sum_{i=0}^{d} a_{i} x^{i}\left(a_{i} \in \mathbb{N}^{*}\right)$, 则

$$
g(n) \equiv \sum_{i=1}^{n} f(i) \equiv \sum_{i=0}^{d} a_{i} f(n, i) \quad(\bmod n)
$$

而由于

$$
\begin{aligned}
\operatorname{gcd}(n, g(n)) & =\operatorname{gcd}\left(\sum_{i=0}^{d} a_{i} f(n, i), n\right) \\
& \geq \operatorname{gcd}(\operatorname{gcd}(f(n, 1), n), \operatorname{gcd}(f(n, 2), n), \cdots, \operatorname{gcd}(f(n, d), n)) \\
& \geq \operatorname{gcd}\left(\frac{n}{\operatorname{gcd}(n, h(1))}, \frac{n}{\operatorname{gcd}(n, h(2))}, \cdots, \frac{n}{\operatorname{gcd}(n, h(1))}\right) \\
& >\frac{1}{\prod_{i=1}^{d} h(i)}
\end{aligned}
$$

取 $M=\prod_{i=1}^{d} h(i) \cdot 2023^{2023}$, 则知对 $\forall m>M$ 有 $\operatorname{gcd}(m, g(m))>2023^{2023}$ 成立.

评注 多项式求和问题易联想到幂和, 再结合常识以及幂和计算的方式易给出引理, 问题随之迎刃而解.

证明 2 因为 $f \in \mathbb{Z}[x]$, 令 $f(x)=\sum_{i=0}^{k} a_{i} x^{i}\left(a_{i} \in N\right)$, 知

$$
\begin{gathered}
\operatorname{gcd}(m, g(m))=\operatorname{gcd}(m, f(1)+\cdots+f(m)) \\
\sum_{i=1}^{m} f(i)=\sum_{i=1}^{m} \sum_{j=0}^{k} a_{j} j^{j}=\sum_{j=0}^{k} a_{j} \sum_{i=1}^{m} i^{j} .
\end{gathered}
$$

接下来我们对 $j$ 归纳证明: 对任意 $0 \leq j \leq k$, 均有

$$
m \mid(j+1) ! \sum_{i=1}^{m} i^{j}
$$

(1) 当 $j=0$ 时, 知 $(j+1) ! \sum_{i=j}^{m} i^{j}=m$ ，成立.

（2）假若命题对 $1,2, \cdots, n-1$ 的情况均成立, 讨论 $n$ 时的情形:

$$
\sum_{i=1}^{m} i^{n+1} \equiv \sum_{i=1}^{m}(i+1)^{n+1}=\sum_{i=0}^{n+1}\left(\begin{array}{c}
n+1 \\
n+1-i
\end{array}\right)\left(\sum_{j=1}^{m} j^{i}\right) \quad(\bmod m) .
$$

所以

$$
\left(\begin{array}{c}
n+1 \\
n+1
\end{array}\right)\left(\sum_{i=1}^{m} i^{0}\right)+\cdots+\left(\begin{array}{c}
n+1 \\
1
\end{array}\right)\left(\sum_{j=1}^{m} i^{n}\right) \equiv 0 \quad(\bmod m) .
$$

由归纳假设, 知 $m \mid(n+1) ! \sum_{i=1}^{m} i^{n}$ 成立. (*) 得证.

所以

$$
\left.\frac{m}{(k+1) !} \right\rvert\, \operatorname{gcd}(m, f(1)+\cdots+f(m))=\operatorname{gcd}(m, g(m))
$$

此时, 取 $M>2023^{2023}(k+1)$ !, 则 $\forall m>M$, 有 $\operatorname{gcd}(m, g(m))>2023^{2023}$.

评注 这里相当于是把解法一的 $h(i)$ 具体化了, 本质上与方法一并无很大区
别. 对于最大公因数大于某数的问题, 在最大公因数内寻找严格递增的因式是一个自然的想法, 这样便可以在严格递增的未知量充分大时达到我们的放缩目标.

题 4 证明: 存在唯一的点 $M$ 在凸四边形 $A B C D$ 的边 $A D$ 上, 使得当且仅当 $A B / / C D$ 时, $\sqrt{S_{A B M}}+\sqrt{S_{C D M}}=\sqrt{S_{A B C D}}$. 其中 $S_{X Y Z}$ 表示 $\triangle X Y Z$ 的面积.

证明 1 设

$$
\begin{aligned}
& \text { 命题 } P: A B / / C D, \\
& \text { 命题 } Q: \sqrt{S_{A B M}}+\sqrt{S_{C D M}}=\sqrt{S_{A B C D}} .
\end{aligned}
$$

则命题 $Q \Leftrightarrow 4 S_{A B M} S_{C D M}=S_{B C M}^{2}$.

构建平面直角坐标系, 且确定这些点的坐标为:

$$
A(0,0), B\left(b_{1}, b_{2}\right), C\left(c_{1}, c_{2}\right), D(0,1), M(0, m), m \in(0,1)
$$

则

$$
\begin{aligned}
& 4 S_{A B M} S_{C D M}=S_{B C M}^{2} \Leftrightarrow 4 b_{1} c_{1} m(1-m)=\left(b_{1} c_{2}-b_{2} c_{1}-m\left(b_{1}-c_{1}\right)\right)^{2} \\
\Leftrightarrow & m^{2}\left(b_{1}+c_{1}\right)^{2}+2 m\left(\left(c_{1}-b_{1}\right)\left(b_{1} c_{2}-b_{2} c_{1}\right)-2 b_{1} c_{1}\right)+\left(c_{1} b_{2}-c_{2} b_{1}\right)^{2}=0
\end{aligned}
$$

要使 $P \Leftrightarrow Q$, 必使 $(*)$ 式 $\Delta=0$, 否则存在不依赖于 $P$ 使 $Q$ 成立的 $M$, 则 $P \nLeftarrow Q$.

由 $\Delta=0$ 可得 $\left(b_{1} c_{2}-b_{2} c_{1}-b_{1}\right)\left(b_{1} c_{2}-b_{2} c_{1}+c_{1}\right)=0$.

因为 $b_{1} c_{2}-b_{2} c_{1}=2 S_{A B C}>0$, 所以

$$
b_{1}=b_{1} c_{2}-b_{2} c_{1} \Leftrightarrow b_{1}=\frac{b_{2} c_{1}}{c_{2}-1} \Leftrightarrow \frac{b_{1}}{b_{2}}=\frac{c_{1}}{c_{2}-1} \Leftrightarrow A B / / C D .
$$

此时 $M$ 有唯一解.

评注 将 $M$ 的唯一性转化为 $\triangle=0$ 来叙述问题以达到证明目的.

证明 2 设

命题 $P: A B / / C D$,

命题 $Q: \sqrt{S_{A B M}}+\sqrt{S_{C D M}}=\sqrt{S_{A B C D}}$.

则命题 $Q \Leftrightarrow 4 S_{A B M} S_{C D M}=S_{B C M}^{2}$. (知 $\left.M \neq A, D\right)$

要证明仅有唯一的点 $M$ 使得命题 $P \Leftrightarrow$ 命题 $Q$ 成立, 则仅需证明:

(1) 命题 $P$ 成立时, 仅有唯一的点 $M$ 使得命题 $Q$ 成立;

(2) 命题 $P$ 不成立时, 仅有唯一的点 $M$ 使得命题 $Q$ 恒不成立.
对于情形(1): 令 $A B=a, C D=c, M$ 到 $A B$ 距离为 $b, M$ 到 $D C$ 距离为 $d$.

由 $2 \sqrt{a b c d} \leq(a+c)(b+d)$ 知

$$
2 \sqrt{S_{A B M} S_{C D M}} \leq S_{B C M}
$$

取等时当且仅当 $\frac{A M}{B M}=\frac{a}{c}$. 所以命题 $P$ 成立时, 仅有唯一一个 $M$ 使得命题 $Q$ 成立, (1) 即证.

对于情形(2): 在 $A D$ 上取 $D^{\prime}$, 使 $C D^{\prime} / / A B$.

若 $\angle A B C+\angle B C D<180^{\circ}$, 则 $D \in A D^{\prime}$, 对 $M \in A D$, 有

$$
2 \sqrt{S_{A B M} S_{C D M}}<2 \sqrt{S_{A B M} S_{C D M}} \leq S_{B C M}
$$

此时 $\forall M \in A D$, 命题 $Q$ 均不成立.

若 $\angle A B C+\angle B C D>180^{\circ}$, 则 $D^{\prime} \in A D$.

取 $M^{\prime}$ 使得 $2 \sqrt{S_{A B M^{\prime}} S_{C M^{\prime}}}=S_{B C M^{\prime}}$, 知 $2 \sqrt{S_{A B M} S_{C D M^{\prime}}}>S_{B C M^{\prime}}$ 恒成立.对于 $M \in A M^{\prime} \cup M^{\prime} D^{\prime}$, 知有 $2 \sqrt{S_{A B M} S_{C D M}}<S_{B C M}$.

固定 $A, B, C, D^{\prime}$, 令 $f(M)=2 \sqrt{S_{A B M} S_{C D M}}-S_{B C M}$, 知

$$
f(M)=\sqrt{\frac{M D}{M D^{\prime}}} \sqrt{S_{A B M} S_{C D^{\prime} M}}-S_{B C M}
$$

总能找到合适的 $D$ 使得 $f(M)=0$.

故对于线段 $A M$ 与 $M^{\prime} D$ 上的点 $M$, 均可在命题 $P$ 不成立时使得命题 $Q$成立.

对于线段 $D^{\prime} D$ (不包含 $D$ 点) 上点 $M$, 知 $\sqrt{S_{A B M}}, S_{B C M}$ 在某个 $M$ 下为定值, 而 $\sqrt{S_{C D M}} \in(0,+\infty)$. 故必存在 $D$, 使得 $f(M)=0$.

所以知除 $M^{\prime}$ 外的 $M$, 均有情况使得在命题 $P$ 不成立时有命题 $Q$ 成立. 情形 $(2)$ 得证.

综上所述, 原命题得证.

评注 本题属于中档题.原题要求我们证明存在唯一的 $M$ 使得 $P \Leftrightarrow Q$, 我们可以从 $P \Rightarrow Q$ 的若干性质进行入手, 借助算线性变化分析来证明该结论, 之后题目就变得简单了.

题 5 已知 $x_{1}, x_{2}, \cdots, x_{n}$ 是实数, 且满足 $\left|x_{1}\right|+\left|x_{2}\right|+\cdots+\left|x_{n}\right|=1$. 对于每个正整数 $n$, 试确定表达式

$$
\left|x_{1}\right|+\left|x_{1}-x_{2}\right|+\left|x_{1}+x_{2}-x_{3}\right|+\cdots+\left|x_{1}+x_{2}+\cdots+x_{n-1}-x_{n}\right|
$$

的最小可能值.
解 1 令 $S_{k}=x_{1}+\cdots+x_{k}, S_{0}=0$.

设 $a_{n}$ 为使得

$$
a_{n}\left(\left|x_{i}\right|+\cdots+\left|x_{1}+\cdots+x_{n-1}-x_{n}\right|\right) \geq\left|x_{1}\right|+\cdots+\left|x_{n}\right|, n \geq 2
$$

成立的最小正数, 易知 $a_{n} \geq \frac{1}{2}$. 即

$$
a_{n} \sum_{k=1}^{n}\left|S_{k-1}-x_{i}\right| \geq \sum_{k=1}^{n}\left|x_{k}\right|
$$

又有局部不等式

$$
\left|S_{k-1}-x_{k}\right|+\sum_{i=1}^{k-1}\left|x_{i}\right| \geq\left|x_{k}\right|
$$

所以

$$
\begin{aligned}
2 a_{n} \sum_{k=1}^{n+1}\left|S_{k-1}-x_{k}\right| & \geq\left|S_{n}-x_{n+1}\right|+2 a_{n} \sum_{k=1}^{n}\left|S_{k-1}-x_{k}\right| \\
& \geq\left|S_{n}-x_{n+1}\right|+2 \sum_{k=1}^{n}\left|x_{k}\right| \\
& \geq\left|x_{n+1}\right|+\sum_{i=1}^{n}\left|x_{k}\right| \\
& =\sum_{k=1}^{n+1}\left|x_{k}\right| .
\end{aligned}
$$

注意到 $a_{n+1} \leq 2 a_{n}$, 所以 $a_{n} \leq 2^{n-1}$, 当 $x_{1}=x_{2}=\frac{1}{2^{n-1}}, x_{i}=\frac{1}{2^{n-i+1}}(3 \leq i \leq$ $n)$ 时取到等号. 故

$$
\sum_{k=1}^{n}\left|S_{k-1}-x_{k}\right| \geq \frac{1}{2^{n-1}}=2^{1-n}
$$

所以表达式的最小值为 $2^{1-n}$.

解 2 所求的最小可能值为 $\frac{1}{2^{n-1}}$.

一方面, 我们取 $x_{1}=x_{2}=\frac{1}{2^{n-1}}, x_{i}=\frac{1}{2^{n-i+1}}(3 \leq i \leq n)$, 符合题意.

此时 $\left|x_{1}\right|=\frac{1}{2^{n-1}},\left|x_{1}-x_{2}\right|=\left|x_{1}+x_{2}-x_{3}\right|=\left|x_{1}+x_{2}+x_{3}-x_{4}\right|=\cdots=$ $\left|x_{1}+\cdots+x_{n-1}-x_{n}\right|=0$, 则

$$
\left|x_{1}\right|+\left|x_{1}-x_{2}\right|+\cdots+\left|x_{1}+x_{2}+\cdots+x_{n-1}-x_{n}\right|=\frac{1}{2^{n-1}} .
$$

另一方面, 我们证明:

$$
\left|x_{1}\right|+\left|x_{1}-x_{2}\right|+\cdots+\left|x_{1}+x_{2}+\cdots+x_{n-1}-x_{n}\right| \geq \frac{1}{2^{n-1}}
$$

由于 $\left|x_{1}\right|+\cdots+\left|x_{n}\right|=1$, 故上式等价于证明

$$
2^{n-1}\left(\left|x_{1}\right|+\left|x_{1}-x_{2}\right|+\cdots+\left|x_{1}+x_{2}+\cdots+x_{n-1}-x_{n}\right|\right) \geq\left|x_{1}\right|+\cdots+\left|x_{n}\right| .
$$

$$
\begin{array}{r}
\text { 令 } x_{1}=y_{1}, x_{1}-x_{2}=y_{2}, \cdots, x_{1}+\cdots+x_{n-1}-x_{n}=y_{n} . \text { 则 } x_{1}=y_{1}, x_{2}= \\
y_{1}-y_{2}, x_{3}=2 y_{1}-y_{2}-y_{3}, x_{i}=2^{i-2} y_{1}-2^{i-3} y_{2}-\cdots-y_{i-1}-y_{i}(4 \leq i \leq n) .
\end{array}
$$

因此只需证:

$$
\begin{aligned}
& 2^{n-1}\left|y_{1}\right|+2^{n-1}\left|y_{2}\right|+\cdots+2^{n-1}\left|y_{n}\right| \\
\geq & \left|y_{1}\right|+\left|y_{1}-y_{2}\right|+\cdots+\left|2^{n-2} y_{1}-2^{n-3} y_{2}-\cdots-y_{n-1}-y_{n}\right| .
\end{aligned}
$$

由绝对值不等式, $(*)$ 中的

$$
\begin{aligned}
\text { 右边 } & \leq\left(1+1+2^{1}+\cdots+2^{n-2}\right)\left|y_{1}\right|+\left(1+1+\cdots+2^{n-3}\right)\left|y_{2}\right|+\cdots+\left|y_{n}\right| \\
& =2^{n-1}\left|y_{1}\right|+2^{n-2}\left|y_{2}\right|+\cdots 2^{1}\left|y_{n-1}\right|+\left|y_{n}\right| \\
& \leq 2^{n-1}\left|y_{1}\right|+2^{n-1}\left|y_{2}\right|+\cdots+2^{n-1}\left|y_{n}\right|=\text { 左边. }
\end{aligned}
$$

故 $(*)$ 成立, 所求的最小可能值为 $\frac{1}{2^{n-1}}$.

评注 先结合式子的特征对简单情形进行分析得出一般情形的构造, 然后利用绝对值不等式进行放缩来证明. 本题也可通过调整、归纳等方式解决, 属于中档题.

题 6 在一个班级中有 26 名学生, 每个人有 5 个科目的成绩, 成绩分为三种可能的分数. 证明: 如果其中 25 名学生已经获得了他们的成绩, 那么我们可以对最后一名学生进行评分, 使得他的分数与任何其他学生在至少两个科目上不同.

证明 用五元数组 $\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right)$ 表示某名学生的成绩, 其中 $x_{i} \in$ $\{1,2,3\}$ 表示第 $i$ 科的分数 $(i \in\{1,2,3,4,5\})$.

我们称五元数组 $\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right)$ “限制” 五元数组 $\left(x_{1}^{\prime}, x_{2}^{\prime}, x_{3}^{\prime}, x_{4}^{\prime}, x_{5}^{\prime}\right)$, 如果它们在至多一维上不同 (可以全部相同).

称五元数组的前两维为“前缀”, 后三维为“后缀”.

记所有这类五元数组构成的全集为 $S$, 集合 $A \subseteq S$ 表示已获得的 25 人的成绩构成的集合, 知 $|S|=3^{5},|A|=25$.

对命题的证明使用反证法, 即假若无论最后一名同学的成绩如何, 前 25 名学生中总存在一人, 其与该人成绩不同的科目不多于一科. 则对任意 $\alpha \in S$, 存在 $\beta \in A$ 使 $\beta$ 限制 $\alpha$. 即 $A$ 中元素可限制 $S$ 中所有元素.

下面讨论 $A$ 中的元素及其对 $S$ 中元素的限制情况:

(一) 对于前缀 $\left(x_{1}, x_{2}\right)$, 其共有 $3^{2}=9$ 种不同取值, 而 $|A|=25$, 由抽展原理, 存在 $x_{1}^{*}, x_{2}^{*}$ 使 $A$ 中至多 $\left[\frac{25}{9}\right]=2$ 个数组的前缀为 $\left(x_{1}^{*}, x_{2}^{*}\right)$, 不妨设
$x_{1}^{*}=x_{2}^{*}=1$. 即 $A$ 中前缀为 $(1,1)$ 的数组至多 2 个.

根据前缀对 $A$ 与 $S$ 分类, $A=A_{1} \amalg A_{2} \amalg A_{3} \amalg A_{4}, S=S_{1} \amalg S_{2} \amalg S_{3} \amalg S_{4}$. 其中 $A_{1}, S_{1}$ : 前缀为 $(1,1) ; A_{2}, S_{2}$ : 前缀为 $(1,2),(2,1),(1,3),(3,1) ; A_{3}, S_{3}$ : 前缀为 $(2,2),(3,3) ; A_{4}, S_{4}$ : 前缀为 $(2,3),(3,2)$. 则

$\left|A_{1}\right|+\left|A_{2}\right|+\left|A_{3}\right|+\left|A_{4}\right|=25,\left|A_{1}\right| \leq 2,\left|S_{1}\right|=27,\left|S_{2}\right|=108,\left|S_{3}\right|=\left|S_{4}\right|=54$.

对 $A_{1}$ 中的数组 $\left(1,1, x_{3}, x_{4}, x_{5}\right)$, 其至多限制 $S_{1}$ 中 7 个数组: $\left(1,1, x_{3}, x_{4}, x_{5}\right)$, $\left(1,1, x_{3}+1, x_{4}, x_{5}\right),\left(1,1, x_{3}+2, x_{4}, x_{5}\right),\left(1,1, x_{3}, x_{4}+1, x_{5}\right),\left(1,1, x_{3}, x_{4}+2, x_{5}\right)$, $\left(1,1, x_{3}, x_{4}, x_{5}+1\right),\left(1,1, x_{3}, x_{4}, x_{5}+2\right)$ (各维按模 3 意义理解). 其至多限制 $S_{2}$中 4 个数组:

$$
\left(1,2, x_{3}, x_{4}, x_{5}\right),\left(2,1, x_{3}, x_{4}, x_{5}\right),\left(1,3, x_{3}, x_{4}, x_{5}\right),\left(3,1, x_{3}, x_{4}, x_{5}\right) .
$$

其无法限制 $S_{3} 、 S_{4}$ 中的数组(前两维均不同).

类似地, $A_{2}$ 中的数组至多限制 $S_{1}$ 中 1 个, $S_{2}$ 中 8 个, $S_{3}$ 中 1 个, $S_{4}$ 中 1 个.

$A_{3}$ 中的数组至多限制 $S_{2}$ 中 2 个, $S_{3}$ 中 7 个, $S_{4}$ 中 2 个, 无法限制 $S_{1}$.

$A_{4}$ 中的数组至多限制 $S_{2}$ 中 2 个, $S_{3}$ 中 2 个, $S_{4}$ 个中 7 个, 无法限制 $S_{1}$.

从而

$$
\left\{\begin{array}{l}
7\left|A_{1}\right|+\left|A_{2}\right| \geq\left|S_{1}\right|=27 \\
4\left|A_{1}\right|+8\left|A_{2}\right|+2\left|A_{3}\right|+2\left|A_{4}\right| \geq 108 \\
\left|A_{2}\right|+7\left|A_{3}\right|+2\left|A_{4}\right| \geq 54 \\
\left|A_{2}\right|+2\left|A_{3}\right|+7\left|A_{4}\right| \geq 54
\end{array}\right.
$$

(1) 当 $\left|A_{1}\right|=0$ 时, 由 (1) 知 $\left|A_{2}\right| \geq 27>25$, 矛盾.

(2) 当 $\left|A_{1}\right|=1$ 时, $\left|A_{2}\right|+\left|A_{3}\right|+\left|A_{4}\right|=24$.

由 (1): $\left|A_{2}\right| \geq 20 \Rightarrow\left|A_{3}\right|+\left|A_{4}\right| \leq 4$, 由 (3)(4): $2\left|A_{2}\right|+9\left|A_{3}\right|+9\left|A_{4}\right| \geq 108$,

得

$$
7\left|A_{3}\right|+7\left|A_{4}\right| \geq 60 \Rightarrow\left|A_{3}\right|+\left|A_{4}\right| \geq\left\lceil\frac{60}{7}\right\rceil=9>4
$$

矛盾!

(3) 当 $\left|A_{1}\right|=2$ 时, $\left|A_{2}\right|+\left|A_{3}\right|+\left|A_{4}\right|=23$.

由 (1): $\left|A_{2}\right| \geq 13 \Rightarrow\left|A_{3}\right|+\left|A_{4}\right| \leq 10$, 由 (3)(4): $2\left|A_{2}\right|+9\left|A_{3}\right|+9\left|A_{4}\right| \geq 108$.

得

$$
7\left|A_{3}\right|+7\left|A_{4}\right| \geq 62 \Rightarrow\left|A_{3}\right|+\left|A_{4}\right| \geq\left\lceil\frac{62}{7}\right\rceil=9
$$

不妨设 $\min \left\{\left|A_{3}\right|,\left|A_{4}\right|\right\}=\left|A_{3}\right|$, 则 $\left|A_{4}\right| \geq 5$.
若 $\left|A_{3}\right| \leq 4$, 则由(3): $31 \leq 6\left|A_{3}\right|+\left|A_{4}\right| \leq 10+5\left|A_{3}\right| \leq 30$, 矛盾!

所以 $\left|A_{3}\right| \geq 5 \Rightarrow\left|A_{3}\right|=\left|A_{4}\right|=5,\left|A_{2}\right|=13$.

综上, 仅可能的情况为 $\left|A_{1}\right|=2,\left|A_{2}\right|=13,\left|A_{3}\right|=\left|A_{4}\right|=5$.

(二) 考察后缀. 由不等式 $\left|A_{1}\right|+\left|A_{2}\right| \geq 27$ 恰好取等, 说明 $A_{1}$ 中两个数组均能限制 $S_{1}$ 中 7 个元素. 这要求 $A_{1}$ 中两个数组的后三维两两不同.

不妨设 $A_{1}=\{(1,1,1,1,1),(1,1,2,2,2)\}$, 则 $S_{1}$ 中数组已有 14 个被限制,余下 3 个数组的后缀 $(*):(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)$, $(1,3,3),(3,1,3),(3,3,1),(2,3,3),(3,2,3),(3,3,2),(3,3,3)$ 均为 $A_{2}$ 中数组的后缀, 且 $(*)$ 中的每个后缀恰为 $A_{2}$ 中一个数组的后缀.

对于 $S_{2}$ 中数组的其余 12 个后缀 $(* *):(1,1,2),(1,2,1),(2,1,1),(1,2,2)$, $(2,1,2),(2,2,1),(1,1,3),(1,3,1),(3,1,1),(1,3,3),(3,1,3),(3,3,1)$.

断言 $S_{2}$ 中后缀为 $(* *)$ 中任一个的数组 (4 个) 均不全被 $A_{1}, A_{2}$ 中数组所限制.

对此我们进行证明: 以 $(1,1,2)$ 为例, 首先它不被 $A_{1}$ 中数组限制. $A_{2}$ 中数组(后缀在 $(*)$ 中) 若能限制它, 则其后缀必为 $(1,3,2)$ 或 $(3,1,2)$, 且只能限制与其前缀相同的那一个后缀为 $(1,1,2)$ 的数组. 这样的数组 $S_{2}$ 中仅有 2 个, 故仅能限制至多 2 个, 从而 $S_{2}$ 中必有至少两个后缀为 $(1,1,2)$ 的数组不全被 $A_{1}, A_{2}$中数组所限制. 断言获证.

故对 (**) 中任一后缀, 考虑 $S_{2}$ 中以之为后缀的数组 (4 个), 其中必有至少一个被 $A_{3} \cup A_{4}$ 中数组限制. 这就要求 $A_{3} \cup A_{4}$ 中以 $(* *)$ 中 12 个后缀为后缀的数组均存在(因为 $(* *)$ 中的数组与 $S_{2}$ 中的数组已有前缀中至少一维不同). 则 $\left|A_{3} \cup A_{4}\right| \geq 12$. 但这与 $\left|A_{3} \cup A_{4}\right|=\left|A_{3}\right|+\left|A_{4}\right|=10$ 矛盾

从而假设不成立, 完成了原命题的证明.

评注 本题具有相当的复杂度. 一个入手点是先研究只有 3 个科目, 6 名学生的简单情形, 问题的处理手段是讨论前两科和后一科, 结合简单的估计, 说明存在性．这启示我们可以将成绩按照前两科分类，用类别之间的“限制” 关系列出不等式. 最后再说明极端情况不成立 (当然这需要关键的观察, 并不容易),

吸引我们的是更一般的问题, 然而哪怕仅仅在本题的基础上增加一个科目或一种可能的成绩, 命题的复杂度都会显著提升. 直于笔者水平, 这里不作分析,感兴趣的读者不妨自行尝试。

