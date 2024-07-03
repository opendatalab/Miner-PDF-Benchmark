# 2021 年中国台湾 TST 试题解析 

陈实 尹一涵 杨轲屹 周韬顺 周佳一

(长沙市雅礼中学, 410007)

指导教师: 姜兴

2021 年中国台湾 TST 试题 (除供给 IMO 预选题的部分) 已经公布. 公开的大部分赛题与中国数学奥林匹克 (CMO) 难度相当. 其中代数、几何注重考察基本功, 部分组合、数论题难度较大, 需要一些独特的想法才能解决. 本文给出已公开试题的解答与评注, 限于作者水平, 不当之处敬请指正.

我们按考试时间顺序分代数 $(\mathrm{A})$ 、几何 $(\mathrm{G})$ 、数论 $(\mathrm{N})$ 、组合 $(\mathrm{C})$ 四个板块对试题进行解答与评注. 其中标注 $1.4 \mathrm{~T} 4$ 表示第 1 次选拔第 4 场考试第 4 题.

I. 代数 (A)

$1.4 \mathrm{~T} 4$ 给定正整数 $n$. 对任意满足 $\sum_{i=1}^{2 n} a_{i}=\sum_{j=1}^{2 n} b_{j}=n$ 的 $4 n$ 元非负实数组 $a_{1}, \cdots, a_{2 n}, b_{1}, \cdots, b_{2 n}$, 定义集合

$$
\begin{aligned}
& A=\left\{\left.\sum_{j=1}^{2 n} \frac{a_{i} b_{j}}{a_{i} b_{j}+1} \right\rvert\, i \in\{1,2, \cdots, 2 n\} \text { s.t. } \sum_{j=1}^{2 n} \frac{a_{i} b_{j}}{a_{i} b_{j}+1} \neq 0\right\}, \\
& B=\left\{\left.\sum_{i=1}^{2 n} \frac{a_{i} b_{j}}{a_{i} b_{j}+1} \right\rvert\, j \in\{1,2, \cdots, 2 n\} \text { s.t. } \sum_{i=1}^{2 n} \frac{a_{i} b_{j}}{a_{i} b_{j}+1} \neq 0\right\} .
\end{aligned}
$$

记 $m$ 为集合 $A \cup B$ 中的最小元, 试求 $a_{1}, \cdots, a_{2 n}, b_{1}, \cdots, b_{2 n}$ 取遍 $4 n$ 元非负实数组时, 得到的 $m$ 的最大值.

解 (陈实) $m_{\max }=\frac{n}{2}$.

一方面给出构造: 令

$$
\begin{gathered}
a_{1}=a_{2}=\cdots=a_{n}=b_{1}=\cdots=b_{n}=1 \\
a_{n+1}=a_{n+2}=\cdots=a_{2 n}=b_{n+1}=\cdots=b_{2 n}=0
\end{gathered}
$$

则 $A=B=\left\{\frac{n}{2}\right\}$.

修订日期: 2021-07-20.
另一方面给出证明: 由对称性, 不妨设 $a_{1} \geq a_{2} \geq \cdots \geq a_{k}>0$ 为 $\left(a_{1}, a_{2}, \cdots, a_{2 n}\right)$ 中所有正数, $b_{1} \geq b_{2} \geq \cdots \geq b_{t}>0$ 为 $\left(b_{1}, b_{2}, \cdots, b_{2 n}\right)$ 中所有正数. 则

$$
\sum_{j=1}^{t} \frac{a_{k} b_{j}}{a_{k} b_{j}+1} \in A
$$

且

$$
\begin{aligned}
\sum_{j=1}^{t} \frac{a_{k} b_{j}}{a_{k} b_{j}+1} & \leq \sum_{j=1}^{t} \frac{\sqrt{a_{k} b_{j}}}{2} \text { (均值不等式) } \\
& =\frac{\sqrt{a_{k}}}{2} \sum_{j=1}^{t} \sqrt{b_{j}} \\
& \leq \frac{1}{2} \sqrt{\frac{n}{k}} \sqrt{t n} \text { (柯西不等式) } \\
& =\frac{n}{2} \sqrt{\frac{t}{k}} .
\end{aligned}
$$

同理 $\sum_{i=1}^{k} \frac{a_{i} b_{t}}{a_{i} b_{t}+1} \in B$ 且不大于 $\frac{n}{2} \sqrt{\frac{k}{t}}$. 故

$$
m \leq \min \left\{\frac{n}{2} \sqrt{\frac{t}{k}}, \frac{n}{2} \sqrt{\frac{k}{t}}\right\} \leq \frac{n}{2}
$$

证毕.

评注解决本题的手法较为基础. 用常见的两点式取等可算得答案, 放缩证明的关键是在局部对每个非零加项分母使用均值不等式, 最后用柯西不等式得到答案.

2.4 T5 令 $\|x\|_{*}=\frac{(|x|+|x-1|-1)}{2}$. 试确定所有的 $f: \mathbb{N} \rightarrow \mathbb{N}$ 使得:

$$
f^{\left(\|f(x)-x\|_{*}\right)}(x)=x, \forall x \in \mathbb{N}
$$

其中: $f^{(0)}(x)=x$ 且 $f^{(n)}(x)=f\left(f^{(n-1)}(x)\right)$ 对 $n \in \mathbb{N}$ 成立.

解 (陈实) 因为

$$
\|x\|_{*}=\frac{|x|+|x-1|-1}{2}=\left\{\begin{array}{l}
|x-1|, x \geq 1 \\
|x|, x \leq 0
\end{array}\right.
$$

故使 $f(x)=x$ 或 $x+1$ 对任意 $x \in \mathbb{N}$ 都成立的所有 $f$ 满足条件.

另一方面, 我们证明: 对于满足条件的 $f$, 必对任意 $x \in \mathbb{N}$, 有 $f(x)=x$ 或 $x+1$.

以 $N$ 为顶点集作有向图 $G$, 所有弧为 $x \rightarrow f(x), x \in \mathbb{N}$, 则每个顶点出度为 1. 对弧 $x \rightarrow f(x)$, 定义跨度为 $|x-f(x)|$.
若存在 $x$ 使 $f(x) \geq x+2$, 由 $f^{(f(x)-x-1)}(x)=x$ 知存在过 $x$ 的有向圈, 又由每个点出度为 1 知此圈唯一. 设此圈共 $t$ 条弧, 其中 $r$ 条弧为正方向 $(i \rightarrow j, i<$ $j)(r<t)$, 跨度为 $a_{1}, a_{2}, \cdots, a_{r}, s$ 条弧为负方向, 跨度 $b_{1}, b_{2}, \cdots, b_{s}$, 依题意

$$
a_{1}+a_{2}+\cdots a_{r}=b_{1}+b_{2}+\cdots+b_{s}, \quad t\left|a_{i}-1, t\right| b_{i}
$$

$\bmod t$ 知 $t \mid r$, 矛盾!

若不存在 $f(x) \geq x+2$, 但存在 $x$ 使 $f(x) \leq x-1$, 由 $f^{(x-f(x))}(x)=x$ 知存在过 $x$ 的有向圈, 且该圈长度 $t$ 满足 $t \mid x-f(x)$. 注意到圈中有弧 $x \rightarrow f(x)$, 又对任意 $n \in \mathbb{N}, f(n) \leq n+1$, 故 $t \geq 1+(x-f(x))$, 矛盾!

故对任意 $x \in \mathbb{N}, f(x) \in\{x, x+1\}$.

综上所述, 所有满足条件的函数为使 $f(x)=x$ 或 $f(x)=x+1$ 对任意 $x \in \mathbb{N}$成立的所有 $f$.

评注 本题形式新颖, 解题突破口是注意到题中限制只有若干步后回到 $X$,故易将 $f$ 转化为 $\mathbb{N}$ 上有向图并分析过每个点的有向图的长度, 之后利用基础的整除分析便得到结论。

## II. 几何 $(\mathrm{G})$

$1.2 \mathrm{~T} 3$ 已知 $\triangle A B C$ 内心为 $I$, 外接圆为 $\Gamma, \Gamma$ 上不同于 $A$ 的一点 $X$ 满足 $A I=X I$, 内切圆与 $A C$ 和 $A B$ 分别切于点 $E$ 和 $F$. 令 $M_{a}, M_{b}, M_{c}$ 分别为边 $B C, C A, A B$ 中点. 记 $T$ 为 $M_{b} F$ 和 $M_{c} E$ 的交点, $A T$ 再次交 $\Gamma$ 于 $S$. 证明: $X, M_{a}, S, T$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-03.jpg?height=534&width=562&top_left_y=1778&top_left_x=747)

图 1

证明 (尹一涵) 先证明下面的引理:

引理 在平行四边形 $A E F G$ 内取一点 $C$, 过 $C$ 作 $C B / / A G$ 交 $A E$ 于 $B$. 作 $C D / / F G$ 交 $A G$ 于 $D . E D$ 交 $B G$ 于 $H$,则 $H 、 C 、 F$ 共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-04.jpg?height=311&width=694&top_left_y=204&top_left_x=687)

图 2

证明 如图 2, 设 $D C$ 交 $E F$ 于 $X, B C$ 交 $F G$ 于 $Y$. 因为

$$
\frac{A B}{B E} \cdot \frac{G D}{D A}=\frac{G Y}{Y F} \cdot \frac{F X}{X E}
$$

由 Menelaus 定理知 $B D 、 E G 、 X Y$ 交于一点或两两平行. 对 $\triangle B G Y$ 与 $\triangle D E X$使用 Desargue's 定理知 $H 、 C 、 F$ 三点共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-04.jpg?height=662&width=711&top_left_y=994&top_left_x=684)

图 3

回到原题. 如图 3, 设以 $I$ 为圆心, $I A$ 为半径的圆交 $A B, A C$ 于不同于 $A$ 的两点 $F^{\prime}, E^{\prime} . E^{\prime} F^{\prime}$ 交 $A I$ 于 $M^{\prime}$. 连接 $X E^{\prime}, X F^{\prime}, X B, X C, X M^{\prime}, X M_{a}$.

因为 $A, X, E^{\prime}, F^{\prime}$ 四点共圆, 故 $\angle X E^{\prime} C=\angle X F^{\prime} B$, 又 $\angle X C E^{\prime}=\angle X B F^{\prime}$,故 $\triangle X E^{\prime} C \sim \triangle X F^{\prime} B$, 所以 $\triangle X F^{\prime} E^{\prime} \sim \triangle X B C$.

由于 $B M_{a}=M_{a} C, F^{\prime} M^{\prime}=M^{\prime} E^{\prime}$, 故 $M^{\prime} 、 M_{a}$ 为 $\triangle X F^{\prime} E^{\prime} \sim \triangle X B C$ 中的相似对应点, 从而 $\triangle X M^{\prime} M_{a} \sim \triangle X E^{\prime} C$, 得

$$
\angle X M_{a} M^{\prime}=\angle X C E^{\prime}=\angle X S A .
$$

又因为 $E 、 F$ 为内切圆切点, 所以 $A M^{\prime}$ 垂直平分 $E F$, 而 $E F$ 为 $\triangle A E^{\prime} F^{\prime}$的中位线, 故四边形 $M^{\prime} F A E$ 为平行四边形. 又因为四边形 $A M_{c} M_{a} M_{b}$ 为平行四边形, 由引理知 $M_{a} 、 M^{\prime} 、 T$ 三点共线, 故 $\angle T M_{a} X=\angle X M_{a} M^{\prime}=\angle X S A$. 所以 $X, M_{a}, S, T$ 四点共圆. 原题证毕.
评注 本题中 $T$ 点难以刻画, 解题关键在于注意到 $X$ 为两圆交点. 通过作出 $E^{\prime} 、 F^{\prime}$, 构造旋转相似对应点进行角度的转化. 解决本题的整体想法比较自然,但解题中容易误入歧途, 忽视 $E^{\prime} 、 F^{\prime}$ 的重要性.

$2.1 \mathrm{~T} 3$ 凸四边形 $A B C D$ 满足四条边的边长互异, 且 $A C$ 垂直 $B D$. 令 $\odot O_{1}, \odot O_{2}$ 分别是 $\triangle A B D, \triangle C B D$ 的外接圆. 证明: $A O_{2}, C O_{1}$, 以及 $\triangle A B C$ 和 $\triangle A D C$ 各自的欧拉线共点.

注: 三角形的欧拉线是指其外心, 重心和垂心所共直线.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-05.jpg?height=405&width=562&top_left_y=811&top_left_x=747)

图 4

证明 1 (陈实) 如图 5, 只需证明 $A O_{2}, C O_{1}$ 及 $\triangle A B C$ 的欧拉线共点, 设 $A B$ 中点 $E, B C$ 中点 $F$. 设 $F O_{2}$ 与 $E O_{1}$ 交于 $\triangle A B C$ 外心 $K, A F$ 与 $C E$ 交于 $\triangle A B C$ 重心 $G, A O_{2}$ 与 $C O_{1}$ 交于 $X, A C$ 中点为 $M, A O_{1}$ 交 $C O_{2}$ 于 $Y$, 只需证明 $G 、 X 、 K$ 三点共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-05.jpg?height=543&width=514&top_left_y=1653&top_left_x=771)

图 5

由 $O_{1} O_{2} / / A C$ 及梯形性质知 $X 、 Y 、 M$ 三点共线. 再对 $\triangle A O_{1} E$ 和 $\triangle C O_{2} F$使用 Desargue's 定理 $K 、 Y 、 B$ 三点共线.

对 $\triangle M Y B$ 及三边上点 $X, K, G$, 由 Menelaus 定理逆定理知只需证

$$
\frac{M G}{G B} \cdot \frac{B K}{K Y} \cdot \frac{Y X}{X M}=1
$$

而 $\frac{M G}{G B}=\frac{1}{2}$ ( $G$ 为重心), 于是

$$
\begin{aligned}
\frac{M G}{G B} \cdot \frac{B K}{K Y} \cdot \frac{Y X}{X M} & =\frac{1}{2} \cdot \frac{Y X}{X M} \cdot \frac{B K}{K Y}=\frac{A M}{A C} \cdot \frac{Y X}{X M} \cdot \frac{B K}{K Y}(M \text { 为中点 }) \\
& =\frac{Y O_{2}}{O_{2} C} \cdot \frac{B K}{K Y}\left(\text { 对 } \triangle M Y C \text { 及截线 } A X O_{2} \text { 用 Menelaus 定理 }\right),
\end{aligned}
$$

再对 $\triangle B C Y$ 及截线 $K O_{2} F$ 用 Menelaus 定理得 $\frac{Y O_{2}}{O_{2} C} \cdot \frac{C F}{F B} \cdot \frac{B K}{K Y}=1$, 而 $F$ 为 $B C$ 中点, 故

$$
\frac{Y O_{2}}{O_{2} C} \cdot \frac{B K}{K Y}=1
$$

即 (1) 式得证, 原题证毕.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-06.jpg?height=637&width=506&top_left_y=841&top_left_x=772)

图 6

证明 2(周韬顺) 如图 6, 设 $O$ 为 $\triangle A B C$ 外心, $H$ 为其垂心, 则只需证明 $A O_{2}, C O_{1}, O H$ 共点 (另一组共点同理可得).

(1) 当 $O_{1}$ 与 $O_{2}$ 重合时, $O$ 也与其重合, 结论成立.

(2) 当 $O_{1}$ 与 $O_{2}$ 不重合时, $O$ 也不与 $O_{1}$ 及 $O_{2}$ 重合.

因为 $O_{1} O_{2} \perp B D, A C \perp B D, O O_{1} \perp B A, C H \perp B A, O O_{2} \perp B C, A H \perp$ $B C$. 所以 $O_{1} O_{2} / / A C, O O_{1} / / C H, O O_{2} \perp A H$. 故 $\triangle O O_{1} O_{2}$ 与 $\triangle H C A$ 位似, 所以 $O H 、 C O_{1} 、 A O_{2}$ 共点. 原题证毕.

评注 本题较为基础, 解决的方法可以利用与重心有关的比例及梅涅劳斯定理得到三点共线, 也可以通过找平行、垂直线段, 用位似解决问题.

$2.2 \mathrm{~T} 3$ 已知 $\triangle A B C$ 的外接圆为 $\Gamma$, 分别选取 $C A$ 和 $A B$ 上的点 $E$ 和 $F$. 令 $\triangle A E F$ 的外接圆和 $\Gamma$ 再次交于点 $X$. 令 $\triangle A B E$ 和 $\triangle A C F$ 的外接圆再次交于点 $K$. 直线 $A K$ 与 $\Gamma$ 再次交于异于点 $A$ 的点 $M$, 且 $N$ 为点 $M$ 关于直线 $B C$ 的对称点. 直线 $X N$ 与 $\Gamma$ 再次交于异于点 $X$ 的点 $S$. 证明: 直线 $S M$ 平行于 $B C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-07.jpg?height=637&width=673&top_left_y=198&top_left_x=700)

图 7

证明 (周韬顺) 如图 7, 设 $\triangle A B C 、 \triangle A B E 、 \triangle A C F$ 外心为 $O 、 O_{1} 、 O_{2}$,作 $S^{\prime} M / / B C$ 交圆 $\Gamma$ 于不同于 $M$ 的一点 $S^{\prime}, X S^{\prime}$ 交 $B C$ 于 $D$, 交 $M N$ 于 $N^{\prime}$.由对称性有 $\widehat{B S^{\prime}}=\widehat{C M}$, 故 $\angle B X S^{\prime}=\angle C A M$, 同理 $\angle C X S^{\prime}=\angle B A M$.

因为 $O O_{1} \perp A B, O O_{2} \perp A C$,所以

$$
\begin{gathered}
\angle B O O_{1}=\angle A C B \\
\angle B O_{1} O=180^{\circ}-\angle A E B=\angle B E C,
\end{gathered}
$$

故 $\triangle B O_{1} O \sim \triangle B E C$, 所以 $\frac{O_{1} O}{C E}=\frac{B O}{B C}$, 同理 $\frac{O_{2} O}{B F}=\frac{C O}{B C}$, 故 $\frac{C E}{B F}=\frac{O O_{1}}{O O_{2}}$.

又因为 $O_{1} O_{2} \perp A K$, 所以

$$
\angle O O_{1} O_{2}=\angle B A K, \angle O O_{2} O_{1}=\angle C A K,
$$

从而

$$
\frac{C E}{B F}=\frac{O O_{1}}{O O_{2}}=\frac{\sin \angle O O_{2} O_{1}}{\sin \angle O O_{1} O_{2}}=\frac{\sin \angle C A M}{\sin \angle B A M}=\frac{\sin \angle B X S^{\prime}}{\sin \angle C X S^{\prime}}
$$

由两相交圆性质得 $\triangle B F X \sim \triangle C E X$, 所以

$$
\frac{B X}{C X}=\frac{B F}{C E}=\frac{\sin \angle C X S^{\prime}}{\sin \angle B X S^{\prime}}
$$

故 $D$ 是 $B C$ 中点. 由对称性, $D S^{\prime}=D M$, 进而 $D N^{\prime}=D M$, 故 $N$ 与 $N^{\prime}$ 重合.所以 $S$ 与 $S^{\prime}$ 重合, 故 $S M / / B C$. 原题证毕.

评注 本题主要思路是用同一法消去后产生的点, 将“直线平行于 $B C$ ”化归为证明 $\frac{C E}{B F}=\frac{\sin \angle C A K}{\sin \angle B A K}$. 上式有多种证明方法, 除解答所给证明外也可通过 $K$ 点寻找相似得出比例.

$2.3 \mathrm{~T} 3$ 已知不等边三角形 $A B C$ 的外心和垂心分别为 $O$ 和 $H . \triangle A H O$ 内
部的点 $P$ 满足 $\angle A H P=\angle P O A$. 点 $M$ 是线段 $\overline{O P}$ 的中点. 令 $B M$ 和 $C M$ 分别再次交 $\triangle A B C$ 的外接圆于点 $X$ 和 $Y$. 证明: 直线 $X Y$ 过 $\triangle A P O$ 的外心.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-08.jpg?height=751&width=691&top_left_y=361&top_left_x=682)

图 8

证明 (尹一涵) 如图 8, 过 $M$ 作 $O P$ 垂线交 $X Y$ 于 $U$, 交 $B C$ 于 $V$. 设 $A$ 关于 $O P$ 的对称点为 $A^{\prime} . A P$ 交 $\odot(A B C)$ 于不同于 $A$ 的一点 $N, A H$ 交 $\odot(A B C)$于不同于 $A$ 的一点 $K$. 连接 $A^{\prime} O, A^{\prime} N$.

由蝴蝶定理,

$$
O M \perp U V \Rightarrow M U=M V \text {. }
$$

因为 $U V$ 为 $O P$ 中垂线, 故 $U 、 V$ 关于 $O P$ 对称. 因为

$$
\angle P O A^{\prime}=\frac{1}{2} \angle A O A^{\prime}=\angle A N A^{\prime}
$$

所以 $O 、 P 、 A^{\prime} 、 N$ 四点共圆. 设此圆为 $\omega$.

设 $A^{\prime} K \cap \omega=A^{\prime} 、 L$, 连接 $P L$. 因为

$$
\angle P L A^{\prime}=\angle A N A^{\prime}=\angle A K A^{\prime}
$$

所以 $A K / / P L$, 而

$$
\angle A K A^{\prime}=\angle P O A^{\prime}=\angle A O P=\angle P H A \Rightarrow \angle H P L=\angle K L P,
$$

所以四边形 $P H K L$ 为等腰梯形. 由于 $H 、 K$ 关于 $B C$ 对称, 故 $B C$ 为 $P L$ 的中垂线. 进而 $V$ 为 $P L$ 与 $O P$ 的垂直平分线交点, $V$ 为 $\triangle O P L$ 外心.

因为 $A^{\prime} 、 P 、 O 、 N 、 L$ 五点共圆, 故 $V$ 为 $\triangle A^{\prime} P O$ 外心, 从而

$$
V O=V P=V A^{\prime}=U A=U O=U P
$$

故 $U$ 为 $\triangle A P O$ 外心. 证毕.
评注 本题中 $P$ 点较难刻画, 作出 $O P$ 的中垂线是比较自然的. 若熟悉“蝴蝶定理”便可注意到 $M U=M V . \triangle A P O$ 不容易处理, 考虑处理与其对称的 $\triangle A^{\prime} P O$, 问题便迎刃而解.

$3.2 \mathrm{~T} 3 \triangle A B C$ 满足 $A B<A C$, 记其 $A-$ 旁心为 $I_{a}$. 令 $D$ 为 $I_{a}$ 在边 $B C$ 上的投影, $X$ 为 $A I_{a}$ 和 $B C$ 的交点, 点 $A C, A B$ 上的点 $Y, Z$ 满足 $X, Y, Z$ 三点共一条垂直于 $A I_{a}$ 的线. $\triangle A Y Z$ 的外接圆再次交 $A I_{a}$ 于 $U$. 记 $\triangle A B C$ 外接圆过 $A$ 点的切线交 $B C$ 于 $T$, 线段 $T U$ 交 $\triangle A B C$ 的外接圆于 $V$. 证明: $\angle B A V=\angle D A C$.

证明 (尹一涵) 我们先介绍伪内切圆相关性质: 如图 9, 在 $\triangle A B C$ 中, 设 $F$为 $A-$ 伪内切圆的切点, $M$ 为 $\widehat{B A C}$ 中点. $I$ 为 $\triangle A B C$ 内心, $D$ 为 $\triangle A B C$ 内切圆在 $B C$ 上的切点, $E$ 为 $\triangle A B C A-$ 旁切圆在 $B C$ 上的切点. 则有: $M 、 I 、 F$三点共线, $\angle F A C=\angle E A B$. 类似的, 对于伪旁切圆也有相应的性质.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-09.jpg?height=503&width=500&top_left_y=1139&top_left_x=778)

图 9

回到原题. 如图 10, 设 $A-$ 伪内切圆与外接圆切点为 $V^{\prime}, A-$ 伪旁切圆与外接圆切点为 $W . W V^{\prime} \cap C B=T^{\prime}$. 内切圆 $\odot I$ 与 $B C$ 切点为 $E$. 连接 $A E$ 、 $A V^{\prime} 、 A W 、 D W 、 E V^{\prime}$.

由上述伪内切圆性质知: $N, I, V^{\prime}$ 共线, $N, I_{a}, W$ 共线. 且

$$
\angle V^{\prime} A B=\angle D A C, \angle E A B=\angle W A C .
$$

所以 $\angle E A C=\angle W A B$, 故 $\triangle A C E \sim \triangle A W B$. 所以

$$
\angle A E C=\angle A B W=\angle A V^{\prime} W
$$

故 $\triangle A D E \sim \triangle A W V^{\prime}$, 进而 $\angle A W T^{\prime}=\angle A D T^{\prime} \Rightarrow A, D, W, T^{\prime}$ 四点共圆. 同理, $A, E, V^{\prime}, T^{\prime}$ 共圆.

由于 $\triangle A D W \sim \triangle A E V^{\prime}$, 故 $W D, E V^{\prime}$ 交于 $\odot(A B C)$ 上一点 $F$, 且 $A F / / B C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-10.jpg?height=774&width=714&top_left_y=201&top_left_x=662)

图 10

所以

$$
\angle W A T^{\prime}=\angle W D T^{\prime}=\angle W F A,
$$

则 $T^{\prime} A$ 为 $\odot(A B C)$ 切线, 故 $T$ 与 $T^{\prime}$ 重合.

取 $A-$ 伪内切圆圆心为 $O$, 则 $O$ 在 $A I$ 上. 设 $W V^{\prime} \cap A M=U^{\prime}$, 则

$$
\frac{A U^{\prime}}{U^{\prime} M}=\frac{\sin \angle A V^{\prime} U^{\prime} \cdot A V^{\prime}}{\sin \angle U^{\prime} V^{\prime} M \cdot V^{\prime} M}=\frac{\sin \angle A E D}{\sin \angle X A E} \cdot \frac{\sin \angle A D X}{\sin \angle D A X}=\frac{A X^{2}}{D X \cdot X E}
$$

故

$$
\frac{A M}{A U^{\prime}}=\frac{U^{\prime} M}{A U^{\prime}}+1=\frac{D X \cdot X E+A X^{2}}{A X^{2}} .
$$

因为 $\triangle A X B \sim \triangle A C M$, 得

$$
A X \cdot A M=A B \cdot A C
$$

所以

$$
\begin{aligned}
B E \cdot E C & =\frac{B C^{2}-(A B-A C)^{2}}{4} \\
& =\sin ^{2} \frac{\angle C A B}{2} \cdot A B \cdot A C \\
& =\sin ^{2} \frac{\angle C A B}{2} \cdot A X \cdot A M,
\end{aligned}
$$

从而

$$
\begin{aligned}
D X \cdot X E & =(X B-E B) \cdot(X C-E B)=X C \cdot X B-B C \cdot E B+E B^{2} \\
& =X C \cdot X B-E C \cdot E B \\
& =A X \cdot X M-\sin ^{2} \frac{\angle C A B}{2} \cdot A X \cdot A M .
\end{aligned}
$$

由 (1)、(2) 知

$$
\begin{aligned}
\frac{A O}{A U^{\prime}} & =A O \cdot \frac{D X \cdot X E+A X^{2}}{A X^{2} \cdot A M} \\
& =A O \cdot \frac{\cos ^{2} \frac{\angle C A B}{2} \cdot A X \cdot A M}{A X^{2} \cdot A M} \\
& =\frac{\cos ^{2} \frac{\angle C A B}{2} \cdot A O}{A X} .
\end{aligned}
$$

因为 $\cos ^{2} \frac{\angle C A B}{2} \cdot A O=A I$, 所以 $\frac{A O}{A U^{\prime}}=\frac{A I}{A X}$, 故 $U^{\prime}$ 在 $\odot(A X Y)$ 上.

故 $U^{\prime}$ 与 $U$ 重合, 从而 $V^{\prime}$ 与 $V$ 重合, $\angle V A B=\angle D A C$. 原题证毕.

评注 本题图形较为复杂, 但若熟悉伪内切圆与伪旁切圆的相关性质, 便可找到突破口. 解题关键是注意到两个切点与 $T$ 共线, 之后用同一法解决问题.

3.4 T6 菱形 $A B C D$ 的中心为 $O . P$ 是边 $A B$ 上一点. 令 $I, J, L$ 分别是 $\triangle P C D, \triangle P A D, \triangle P B C$ 的内心, $H$ 和 $K$ 分别是 $\triangle P L B$ 和 $\triangle P J A$ 的垂心. 证明: $O I \perp H K$.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-11.jpg?height=605&width=500&top_left_y=1231&top_left_x=778)

图 11

证明 (陈实) 如图 11. 由于 $P K \perp A C 、 P H \perp B D 、 A C \perp B D$, 故原题只需证明 $\angle P K H=\angle I O C$, 即 $\tan \angle P K H=\tan \angle I O C$,

$$
\Rightarrow \frac{P H}{P K}=\frac{\sin \angle I O C}{\sin \angle I O D}=\frac{I C \sin \angle I C O}{I D \sin \angle I D O} .
$$

注意到

$$
\begin{aligned}
\angle H P L & =90^{\circ}-\angle P L O=90^{\circ}-\left(180^{\circ}-\angle P L B\right) \\
& =\angle P L B-90^{\circ}=\frac{1}{2} \angle P C B=\angle L C B,
\end{aligned}
$$

且

$$
\angle P H L=\angle P B L=\angle C B L \text {, }
$$

所以 $\triangle P H L \sim \triangle C B L$, 故 $P H=C B \cdot \frac{P L}{L C}$, 同理得 $P K=A D \cdot \frac{P J}{J D}$. 故

$$
\begin{aligned}
\frac{P H}{P K} & =\frac{P L}{L C} \cdot \frac{D J}{P J}=\frac{\sin \frac{1}{2} \angle P C B}{\sin \frac{1}{2} \angle C P B} \cdot \frac{\sin \frac{1}{2} \angle A P D}{\sin \frac{1}{2} \angle A D P} \\
& =\frac{\sin \frac{1}{2} \angle P C B}{\sin \frac{1}{2} \angle A D P} \cdot \frac{\sin \frac{1}{2} \angle A P D}{\sin \frac{1}{2} \angle C P B} \\
& =\frac{\sin \angle I C O}{\sin \angle I D O} \cdot \frac{\sin \angle C D I}{\sin \angle D C I} \\
& =\frac{I C \sin \angle I C O}{I D \sin \angle I D O} .
\end{aligned}
$$

(其中 $\angle I C L=\frac{1}{2} \angle B C D=\angle A C B, \angle I C O=\angle L C B$ )

即 (1) 式成立, 原题证毕.

评注 本题较为简单, 利用原题中各个垂直关系容易将 $O I \perp H K$ 转化为比例关系. 之后的比例关系转化有多种形式, 但容易出现繁琐的计算, 利用图中角度关系与相似关系可简化比例关系。

## III. 数论 $(\mathrm{N})$

$1.3 \mathrm{~T} 3$ 求所有满足 $x^{2}+4^{y}=5^{z}$ 的正整数组 $(x, y, z)$.

解 (周韬顺) 满足条件的正整数组为 $(x, y, z)=(3,2,2),(1,1,1),(11,1,3)$.下面给出证明:

首先, 方程两边模 2 得 $x$ 为奇数. 下按 $y$ 分为两种情况讨论:

(1) $y \geq 2$ 时, 有 $5^{z} \equiv x^{2}+4^{y} \equiv 1(\bmod 8)$, 于是 $2 \mid z$. 设 $z=2 p$, 则有

$$
x^{2}+\left(2^{y}\right)^{2}=\left(5^{p}\right)^{2} \text {. }
$$

因为 $\left(2^{y}, 5^{p}\right)=1$, 所以存在 $a, b$ 使得

$$
2^{y}=2 a b, 5^{p}=a^{2}+b^{2},(a, b)=1,
$$

可设 $a=1 b=2^{y-1}$, 则

$$
5^{p}=1+\left(2^{y-1}\right)^{2}
$$

当 $y=2$ 时, $p=1$ 符合条件; $y \geq 3$ 时, 由于

$$
5^{p} \equiv 1+\left(2^{y-1}\right)^{2} \equiv 1 \quad(\bmod 8)
$$

故 $2 \mid p$. 所以

$$
\left(5^{\frac{p}{2}}-2^{y-1}\right)\left(5^{\frac{p}{2}}+2^{y-1}\right)=1
$$

矛盾. 故 $(x, y, z)=(3,2,2)$ 是此情况的唯一解.

(2) $y=1$ 时, 则 $5^{z} \equiv x^{2}+4 \equiv 5(\bmod 8)$, 故 $z$ 为奇数, 设 $z=2 r+1$, 记
$a=5^{r}$, 原方程即为 $x^{2}+4=5 a^{2}$.

若 $a \equiv x(\bmod 4)$, 则令 $u=\frac{3 x+5 a}{4}, v=\frac{3 a+x}{4}$, 反之则令 $u=\frac{3 x-5 a}{4}, v=\frac{3 a-x}{4}$.两种情况均有 $u^{2}-5 v^{2}=-1$, 由 Pell 方程的解的性质知, 该方程的所有解为 $u+\sqrt{5} v=(2+\sqrt{5})^{2 n-1}\left(n \in \mathbb{N}^{*}\right)$, 代回整理可得

$$
a=\frac{\sqrt{5}}{5}\left[\left(\frac{1+\sqrt{5}}{2}\right)^{k}-\left(\frac{1-\sqrt{5}}{2}\right)^{k}\right]
$$

其中 $a \equiv x(\bmod 4)$ 时 $k \equiv 1(\bmod 6), a \neq \equiv x(\bmod 4)$ 时 $k \equiv 5(\bmod 6)$.

考察

$$
a=\frac{\sqrt{5}}{5}\left[\left(\frac{1+\sqrt{5}}{2}\right)^{2 n+1}-\left(\frac{1-\sqrt{5}}{2}\right)^{2 n+1}\right]=\frac{1}{2^{2 n}} \sum_{i=0}^{n} \mathrm{C}_{2 n+1}^{2 i+1} 5^{i}(n \in \mathbb{N}),
$$

设 $\alpha=V_{5}(2 n+1)\left(2 n+1\right.$ 含 5 的幂次), 由于对 $i \in \mathbb{N}_{+}$, 记 $S_{5}(2 i+1)$ 为 $2 i+1$的 5 进制数码和, 则

$$
V_{5}((2 i+1) !)=\frac{2 i+1-S_{5}(2 i+1)}{5-1}<\frac{2 i+1}{5-1}<i
$$

故 $V_{5}\left(\mathrm{C}_{2 n+1}^{2 i+1} 5^{i}\right)>\alpha$, 所以 $V_{5}(a)=\alpha$, 故 $\alpha=r$, 从而

$$
a=5^{r}=5^{\alpha} \leq 2 n+1 .
$$

又 $n \geq 3$ 时, 有

$$
a>\frac{1}{2^{2 n}} \mathrm{C}_{2 n+1}^{2 n-1} \cdot 5^{n-1}=\frac{5^{n-1} \cdot n}{2^{2 n}} \cdot(2 n+1)>2 n+1,
$$

矛盾;

$n \leq 2$ 时, $a=1,5$ 是唯二解, 所以此时方程的解为 $(x, y, z)=(1,1,1)$ 或 $(11,1,3)$.

综上, 满足条件的正整数组为 $(x, y, z)=(3,2,2),(1,1,1),(11,1,3)$.

评注 本题综合性较强, 是一道中等难度的数论题. 本题考察了同余法、勾股方程、Pell 方程和素因子分析. 问题的解决都是运用比较基本的手法, 这类问题第一步通常是对指数的奇偶性分类讨论.

$2.1 \mathrm{~T} 4$ 正整数集 $S$ 满足对每对 $a, b \in S$, 都存在 $c \in S$ 使得 $c^{2}$ 整除 $a(a+b)$.证明: 存在 $a \in S$ 使得 $a$ 整除 $S$ 中每个元素.

证明 (周佳一) 用反证法. 取 $c_{0}=\min S, b_{0}$ 是 $S$ 中最小的不被 $c_{0}$ 整除的数.取最小的 $b_{1} \in S$ 使 $b_{1}^{2} \mid c_{0}\left(c_{0}+b_{0}\right)$.

若 $c_{0} \mid b_{1}$, 则 $c_{0}^{2}\left|c_{0}\left(c_{0}+b_{0}\right) \Rightarrow c_{0}\right| b_{0}$, 矛盾. 故 $b_{1}$ 不被 $c_{0}$ 整除, 由 $b_{0}$ 的最小性知 $b_{1} \geq b_{0}$.
故

$$
c_{0}\left(c_{0}+b_{0}\right) \geq b_{0}^{2} \Rightarrow b_{0} \leq \frac{1+\sqrt{5}}{2} c_{0}
$$

从而 $b_{0}<2 c_{0}$. 逐步取最小的 $b_{k+1} \in S$ 使 $b_{k+1}^{2} \mid c_{0}\left(c_{0}+b_{k}\right)$.

断言 对任意 $k \geq 0$, 有 $b_{k}<2 c_{0}, c_{0}$ 不整除 $b_{k}$.

证明 若已有 $b_{k-1}<2 c_{0}, c_{0}$ 不整除 $b_{k-1}(k \geq 1)$, 则

$$
b_{k}^{2} \leq c_{0}\left(c_{0}+b_{k-1}\right)<4 c_{0}^{2}
$$

即 $b_{k}<2 c_{0}$. 且若 $c_{0} \mid b_{k}$, 则 $c_{0}\left|\left(c_{0}+b_{k-1}\right), c_{0}\right| b_{k-1}$, 矛盾. 从而由归纳原理知断言成立.

设 $c_{0}\left(c_{0}+b_{k}\right)=b_{k+1}^{2} q_{k}$, 由断言可知

$$
c_{0}^{2}<c_{0}\left(c_{0}+b_{k}\right)<3 c_{0}^{2} \Rightarrow q_{k} \in\{1,2\} .
$$

记 $d_{k}=\operatorname{gcd}\left(c_{0}, b_{k}\right)$, 注意到

$$
d_{k}^{2}\left|2 b_{k+1}^{2} \Rightarrow d_{k}\right| b_{k+1} \Rightarrow d_{k} \mid d_{k+1},
$$

故

$$
d_{1} \leq d_{2} \leq d_{3} \cdots \leq d_{k} \cdots \text {. }
$$

注意到 $d_{k} \leq c_{0}$, 即数列 $\left\{d_{k}\right\}$ 是有界的正整数数列, 故存在 $t$ 使得

$$
d_{t}=d_{t+1}=d_{t+2}=\cdots \triangleq d
$$

记 $c_{0}=d c_{0}^{\prime}, b_{k}=d b_{k}^{\prime}(k \geq t)$, 故

$$
c_{0}^{\prime}\left(c_{0}^{\prime}+b_{k}^{\prime}\right)=b_{k+1}^{\prime 2} q_{k}(k \geq t) .
$$

由于 $\left(c_{0}^{\prime}, b_{k+1}^{\prime}\right)=1$, 故 $c_{0}^{\prime} \mid q_{k}$. 因为 $c_{0}^{\prime}$ 不整除 $b_{k}{ }^{\prime}$, 故 $c_{0}{ }^{\prime} \neq 1$. 从而

$$
q_{k}=2(k \geq t), c_{0}^{\prime}=2,
$$

即有

$$
2\left(2+b_{k}^{\prime}\right)=2 b_{k+1}^{\prime 2} \Rightarrow b_{k+1}^{\prime}{ }^{2}=b_{k}^{\prime}+2<\left(b_{k}^{\prime}\right)^{2}\left(b_{k}^{\prime} \geq c_{0}^{\prime}+1=3\right)
$$

即 $b_{k+1}{ }^{\prime}<b_{k}^{\prime}$, 但 $\left\{b_{k}^{\prime}\right\}$ 是正整数数列, 矛盾! 原题证毕.

评注 本题是难度较大的数论题. 首先, 题中要求的 $a$ 为 $\min S$, 利用唯一的条件产生出数列 $\left\{b_{n}\right\}$, 核心是注意到 $\left\{d_{n}\right\}$ 的最终稳定, 剩下的过程较为自然.

$3.1 \mathrm{~T} 4$ 正整数数列 $a_{1}, a_{2}, \cdots$ 满足 $a_{1}=2021$ 和 $\sqrt{a_{n+1}-a_{n}}=\left\lfloor\sqrt{a_{n}}\right\rfloor$. 证明: 此数列中存在无穷多个奇数和无穷多个偶数.

证明 (周佳一) 用反证法, 假设存在 $N \in \mathbb{N}^{*}$, 使得任意 $m, n \geq N, a_{m}$ 与 $a_{n}$
奇偶性相同, 则对任意 $n \geq N$,

$$
2 \mid a_{n+1}-a_{n}=\left[\sqrt{a_{n}}\right]^{2},
$$

记

$$
\left[\sqrt{a_{n}}\right]=2 b_{n},\left(b_{n} \in \mathbb{N}^{*}\right) n \geq N .
$$

则 $4 b_{n}^{2} \leq a_{n} \leq 4 b_{n}^{2}+4 b_{n}$, 故

$$
4 b_{n}^{2}+4 b_{n}^{2} \leq a_{n}+\left[\sqrt{a_{n}}\right]^{2}=a_{n+1} \leq 4 b_{n}^{2}+4 b_{n}+4 b_{n}^{2} .
$$

即

$$
\left(2 \sqrt{2} b_{n}\right)^{2} \leq\left(\sqrt{a_{n+1}}\right)^{2} \leq 8 b_{n}^{2}+4 b_{n}<\left(2 \sqrt{2} b_{n}+1\right)^{2},
$$

故

$$
2 \sqrt{2} b_{n} \leq \sqrt{a_{n+1}}<2 \sqrt{2} b_{n}+1
$$

从而

$$
\left[\sqrt{a_{n+1}}\right] \in\left\{\left[2 \sqrt{2} b_{n}\right],\left[2 \sqrt{2} b_{n}\right]+1\right\} .
$$

又因为 $2 \mid 2 b_{n+1}=\left[\sqrt{a_{n+1}}\right]$, 故 $\left[\sqrt{a_{n+1}}\right]$ 是 $\left\{\left[2 \sqrt{2} b_{n}\right],\left[2 \sqrt{2} b_{n}\right]+1\right\}$ 中的偶数.

若 $\left[2 \sqrt{2} b_{n}\right]$ 为偶数, 则有 $2 b_{n+1}=\left[2 \sqrt{2} b_{n}\right]$, 故

$$
2 \sqrt{2} b_{n}-1<2 b_{n+1}<2 \sqrt{2} b_{n} \Rightarrow \sqrt{2} b_{n}-\frac{1}{2}<b_{n+1}<\sqrt{2} b_{n}
$$

若 $\left[2 \sqrt{2} b_{n}\right]$ 为奇数, 则有 $2 b_{n+1}=\left[2 \sqrt{2} b_{n}\right]+1$, 故

$$
2 \sqrt{2} b_{n}<2 b_{n+1}<2 \sqrt{2} b_{n}+1 \Rightarrow \sqrt{2} b_{n}<b_{n+1}<\sqrt{2} b_{n}+\frac{1}{2}
$$

下面考虑连续的三项 $b_{n}, b_{n+1}, b_{n+2}$, 分情况讨论:

(1) 若 $\left[2 \sqrt{2} b_{n}\right],\left[2 \sqrt{2} b_{n+1}\right]$ 均为偶数, 则

$$
\begin{gathered}
2 b_{n+1}=\left[2 \sqrt{2} b_{n}\right], 2 b_{n+2}=\left[2 \sqrt{2} b_{n+1}\right] . \\
b_{n+2}<\sqrt{2} b_{n+1}<\sqrt{2}\left(\sqrt{2} b_{n}\right)=2 b_{n}, \\
b_{n+2}>\sqrt{2} b_{n+1}-\frac{1}{2}>\sqrt{2}\left(\sqrt{2} b_{n}-\frac{1}{2}\right)-\frac{1}{2}=2 b_{n}-\frac{\sqrt{2}+1}{2} .
\end{gathered}
$$

从而

$$
b_{n+2}=2 b_{n}-1,\left[\sqrt{a_{n+2}}\right]=4 b_{n}-2 \Rightarrow a_{n+2} \leq\left(4 b_{n}-1\right)^{2},
$$

由

$$
a_{n+2}=\left[\sqrt{a_{n}}\right]^{2}+\left[\sqrt{a_{n+1}}\right]^{2}+a_{n}=4 b_{n}^{2}+4 b_{n+1}^{2}+a_{n}, \quad \text { 及 } a_{n} \geq 4 b_{n}^{2},
$$

知

$$
\left(4 b_{n}-1\right)^{2} \geq a_{n+2}=4 b_{n}^{2}+4 b_{n+1}^{2}+a_{n} \geq 8 b_{n}^{2}+4 b_{n+1}^{2}
$$

故

$$
2 b_{n}^{2}-2 b_{n}+\frac{1}{4} \geq b_{n+1}^{2} .
$$

但 $b_{n+1}^{2}>\left(\sqrt{2} b_{n}-\frac{1}{2}\right)^{2}=2 b_{n}^{2}-\sqrt{2} b_{n}+\frac{1}{4}$. 矛盾!

(2) $\left[2 \sqrt{2} b_{n}\right],\left[2 \sqrt{2} b_{n+1}\right]$ 均为奇数, 则

$$
\begin{gathered}
2 b_{n+1}=\left[2 \sqrt{2} b_{n}\right]+1,2 b_{n+2}=\left[2 \sqrt{2} b_{n+1}\right]+1 \\
b_{n+2}<\sqrt{2} b_{n+1}+\frac{1}{2}<\sqrt{2}\left(\sqrt{2} b_{n}+\frac{1}{2}\right)+\frac{1}{2}=2 b_{n}+\frac{\sqrt{2}+1}{2} \\
b_{n+2}>\sqrt{2} b_{n+1}>\sqrt{2}\left(\sqrt{2} b_{n}\right)=2 b_{n} .
\end{gathered}
$$

故

$$
\begin{aligned}
b_{n+2}= & 2 b_{n}+1,\left[\sqrt{a_{n+2}}\right]=4 b_{n}+2 \\
& \Rightarrow a_{n+2} \geq\left(4 b_{n}+2\right)^{2}
\end{aligned}
$$

由

$$
a_{n+2}=4 b_{n}^{2}+a_{n}+4 b_{n+1}^{2} \text { 及 } a_{n} \leq 4 b_{n}^{2}+4 b_{n}
$$

知

$$
\left(4 b_{n}+2\right)^{2} \leq 8 b_{n}^{2}+4 b_{n}+4 b_{n+1}^{2},
$$

故

$$
2 b_{n}^{2}+3 b_{n}+1 \leq b_{n+1}^{2},
$$

但

$$
b_{n+1}^{2}<\left(\sqrt{2} b_{n}+\frac{1}{2}\right)^{2}=2 b_{n}^{2}+\sqrt{2} b_{n}+\frac{1}{4}
$$

矛盾!

（3）若 $\left[2 \sqrt{2} b_{n}\right]$ 为偶数, $\left[2 \sqrt{2} b_{n+1}\right]$ 为奇数. 则

$$
2 b_{n+1}=\left[2 \sqrt{2} b_{n}\right], 2 b_{n+2}=\left[2 \sqrt{2} b_{n+1}\right]+1 .
$$

从而

$$
\begin{aligned}
& b_{n+2}>\sqrt{2} b_{n+1}>\sqrt{2}\left(\sqrt{2} b_{n}-\frac{1}{2}\right)=2 b_{n}-\frac{\sqrt{2}}{2} \\
& b_{n+2}<\sqrt{2} b_{n+1}+\frac{1}{2}<\sqrt{2}\left(\sqrt{2} b_{n}\right)+\frac{1}{2}=2 b_{n}+\frac{1}{2}
\end{aligned}
$$

故 $b_{n+2}=2 b_{n}$.

(4) 若 $\left[2 \sqrt{2} b_{n}\right]$ 为奇数, $\left[2 \sqrt{2} b_{n+1}\right]$ 为偶数. 则

$$
2 b_{n+1}=\left[2 \sqrt{2} b_{n}\right]+1,2 b_{n+2}=\left[2 \sqrt{2} b_{n+1}\right] .
$$

故

$$
\begin{gathered}
b_{n+2}>\sqrt{2} b_{n+1}-\frac{1}{2}>\sqrt{2}\left(\sqrt{2} b_{n}\right)-\frac{1}{2}=2 b_{n}-\frac{1}{2} \\
b_{n+2}<\sqrt{2} b_{n+1}<\sqrt{2}\left(\sqrt{2} b_{n}+\frac{1}{2}\right)=2 b_{n}+\frac{\sqrt{2}}{2} .
\end{gathered}
$$

故 $b_{n+2}=2 b_{n}$.

综合 (1)、(2)、(3)、(4) 的讨论, 有如下结论:

集合 $A=\left\{\left[2 \sqrt{2} b_{N+2 t}\right]\right\}(t=0,1,2 \cdots)$ 中各元素奇偶性相同,

集合 $B=\left\{\left[2 \sqrt{2} b_{N+2 t+1}\right]\right\}(t=0,1,2 \cdots)$ 中各元素奇偶性相同, 集合 $A 、 B$ 的奇偶性不同. 且对任意 $n \geq N$, 有 $b_{n+2}=2 b_{n}$. 不妨设

$$
A=\left\{\left[2 \sqrt{2} b_{N+2 t}\right]\right\}=\left\{\left[2 \sqrt{2} b_{N} \cdot 2^{t}\right]\right\}(t=0,1,2 \cdots)
$$

中全是偶数, 由于

$$
\left[2 \sqrt{2} b_{N} \cdot 2^{t+1}\right] \in\left\{2\left[2 \sqrt{2} b_{N} \cdot 2^{t}\right], 2\left[2 \sqrt{2} b_{N} \cdot 2^{t}\right]+1\right\}
$$

知

$$
\left[2 \sqrt{2} b_{N} \cdot 2^{t+1}\right]=2\left[2 \sqrt{2} b_{N} \cdot 2^{t}\right]
$$

故

$$
\left\{2 \sqrt{2} b_{N} \cdot 2^{t+1}\right\}=2\left\{2 \sqrt{2} b_{N} \cdot 2^{t}\right\}=2^{t+1}\left\{2 \sqrt{2} b_{N}\right\} .
$$

令 $t$ 充分大, 此时 $\left\{2 \sqrt{2} b_{N} \cdot 2^{t+1}\right\}>1$, 矛盾!

综上所述, 反证假设不成立! 故 $\left\{a_{n}\right\}$ 中有无穷多项奇数, 无穷多项偶数.

评注 本题解决过程较为繁杂, 但每一步的想法都是直接的. 解题过程中估计连续三项是为了把 $\left[2 \sqrt{2} b_{n}\right]$ 的无理数 $\sqrt{2}$ 消去. 核心的结论是 $\left[2 \sqrt{2} b_{n}\right]$ 是奇偶交替的, 此后利用小数部分的有界性即可解决问题.

$3.2 \mathrm{~T} 4$ 给定正整数 $n$. 我们称一个正整数 $m$ 为 $n$-好的, 当且仅当存在至多 $2 n$ 个不同的素数 $p$ 满足 $p^{2} \mid m$.

(a) 证明: 对互素的正整数 $a, b$, 存在正整数 $x, y$ 使得 $a x^{n}+b y^{n}$ 是 $n$-好的.

(b) 证明: 对任意 $k$ 个满足 $\operatorname{gcd}\left(a_{1}, \cdots, a_{k}\right)=1$ 的正整数 $a_{1}, \cdots, a_{k}$, 存在正整数 $x_{1}, \cdots, x_{k}$ 使得 $a_{1} x_{1}^{n}+a_{2} x_{2}^{n}+\cdots+a_{k} x_{k}^{n}$ 是 $n$-好的.
注: $a_{1}, \cdots, a_{k}$ 不必是两两互异的.

证明 (杨轲屹) 仅证明 (b) 即可.

设 $2=p_{1}<p_{2}<\cdots$ 为所有素数的排列.

断言 对充分大的正整数 $r$, 存在 $x_{1}, x_{2}, \cdots, x_{k}$ 使得

$$
\left(\prod_{i=1}^{r} p_{i}, \sum_{i=1}^{k} a_{i} x_{i}^{n}\right)=1
$$

证明 由中国剩余定理知: 只需证明对任意 $1 \leq l \leq r$, 存在正整数 $x_{1}, x_{2}, \cdots, x_{k}$ 使得

$$
\left(p_{l}, \sum_{i=1}^{k} a_{i} x_{i}^{n}\right)=1
$$

令 $s$ 为最小的正整数使 $p_{l} \nmid a_{s}$, (由 $\left(a_{1}, a_{2}, \cdots, a_{k}\right)=1$ 知 $s$ 存在). 令

$$
x_{i} \equiv 1 \quad\left(\bmod p_{l}\right)(1 \leq i \leq s), x_{j} \equiv 0 \quad\left(\bmod p_{l}\right)(j>s)
$$

即可. 断言成立.

取 $r$ 满足 $p_{r}$ 大于 $\prod_{i=1}^{k} a_{i}$ 的最大素因子, 且 $r>n$, 设 $\left(b_{1}, \cdots, b_{k}\right)$ 为符合 $(1)$的一组正整数解, 设 $\sum_{i=2}^{k} a_{i} b_{i}^{n}$ 所有大于 $p_{r}$ 的素因子为 $q_{1}, q_{2}, \cdots, q_{s}$, 则

$$
\left(a_{1}, \prod_{i=1}^{s} q_{i}\right)=1
$$

记

$$
\prod_{i=1}^{r} p_{i} \prod_{i=1}^{s} q_{i}=m
$$

令 $x_{1}=t m+1$ ( $t$ 待定 $), x_{i}=b_{i}(2 \leq i \leq k)$.

下证: 存在充分大的 $N$, 使得 $(0, N]$ 之间存在 $t_{0} \in \mathbb{Z}_{+}$使无小于 $\sqrt{N}$ 的素数 $p$ 满足

$$
p^{2} \mid \sum_{i=2}^{k} a_{i} b_{i}^{n}+a_{1}\left(t_{0} m+1\right)^{n}
$$

对素数 $p_{l}, l>r, p_{l} \neq q_{i}(i=1,2, \cdots, s)$. 由模 $p_{l}^{2}$ 原根存在性与 $p_{l} \neq q_{i}$ 知:至多有 $n$ 个 $j$ 使 $x_{1} \equiv j\left(\bmod p_{l}^{2}\right)$ 时, $p_{l}^{2} \mid \sum_{i=1}^{k} a_{i} x_{i}^{n}$; 将这些同余类删去, 则满足 (2) 的 $t_{0}$ 的个数大于 $N-\left(\sum_{r+1 \leq i<\sqrt{N}}\left\lceil\frac{N}{p_{i}^{2}}\right\rceil\right) \cdot n$.

注意有

$$
N-\left(\sum_{r+1 \leq i<\sqrt{N}}\left\lceil\frac{N}{p_{i}^{2}}\right\rceil\right) \cdot n \geq N-\left(\sum_{r+1 \leq i<\sqrt{N}} \frac{1}{p_{i}^{2}}\right) \cdot n \cdot N-\sqrt{N} \cdot n
$$

$$
\geq\left(1-\frac{n}{2 r+1}\right) N-\sqrt{N} \cdot n
$$

因 $2 r+1>n, N$ 充分大时上式大于 $1,(2)$ 得证.

对于满足 (2) 的 $N$ 及 $t_{0}$, 若 $\sum_{i=2}^{k} a_{i} b_{i}^{n}+a_{1}\left(t_{0} m+1\right)^{n}$ 不是 $n$-好的, 则有 $2 n+1$个不同素数 $p$ 满足

$$
p^{2} \mid \sum_{i=2}^{k} a_{i} b_{i}^{n}+a_{1}\left(t_{0} m+1\right)^{n}
$$

由 (2) 知 $p>\sqrt{N}$, 故

$$
N^{2 n+1} \leq \sum_{i=2}^{k} a_{i} b_{i}^{n}+a_{1}\left(t_{0} m+1\right)^{n} \leq \sum_{i=2}^{k} a_{i} b_{i}^{n}+a_{1}(N m+1)^{n}
$$

这在 $N$ 充分大时矛盾. 原题证毕.

## IV. 组合 $(\mathrm{C})$

$1.1 \mathrm{~T} 2$ 给定满足 $k \leq 2 n^{2}$ 的正整数 $n$ 和 $k$. Lee 和 Sunny 在一张 $2 n \times 2 n$的方格纸上玩如下游戏. 首先, Lee 在每个方格中填入不超过 1 的非负实数, 使得方格纸上所有数之和恰为 $k$. 然后, Sunny 将方格纸裁成若干小块, 只需使得每个小块都是由若干完整且相连的方格组成, 且每个小块上方格中所有数之和至多为 1 , 而对小块的具体形状没有要求. (如果方格有公共边, 我们称其是相连的 ) 令 $M$ 为裁切出的小块数量, Lee 希望 $M$ 尽可能大, Sunny 希望尽可能小. 试确定两人都采取最佳策略时 $M$ 的值.

解 (杨轲屹) 两人都采取最佳策略时 $M=2 k-1$, 给出 Lee 的构造: 在 $2 n \times 2 n$ 方格表中任取 $2 k-1$ 个方格分别填入实数

$$
\underbrace{\frac{1}{2}+\epsilon, \frac{1}{2}+\epsilon, \cdots, \frac{1}{2}+\epsilon}_{\text {共 } 2(k-1) \text { 个 } \frac{1}{2}+\epsilon}, 1-2(k-1) \epsilon(\epsilon \text { 充分小 }) \text {, 其余填入 } 0 \text {. }
$$

则不存在两非零实数可被划分至一个块中 (否则, 若某块中有两个以上非零实数则其总和必大于 1 ,矛盾. ), 此时 Sunny 至少将方格表划分为 $2 k-1$ 块.

下证: Sunny 至多将方格表划分为 $2 k-1$ 块.

断言 Lee 不管如何在 $1 \times l$ 的方格表中填入和不超过 $k$ 且属于 $[0,1]$ 的实数, Sunny 总能将其剪为至多 $2 k-1$ 个小块满足题目要求.

证明 对 $k$ 进行归纳, $k=1$ 时结论显然,

若 $k=t-1$ 时结论成立, 考虑 $k=t$ 时设从左到右第 $r$ 个方格中的数为 $a_{r}$, $s$ 为最小的使 $\sum_{r=1}^{s} a_{r}>1$ 的数.

若不存在 $s$, 则 Sunny 剪一块即可, 若 $s$ 存在, 则剪下由左至右第 1 至 $s-1$
格作为第一块, 再剪下第 $s$ 格作为第二块, 由 $\sum_{r=1}^{s} a_{r}>1$ 知剩下的方格中数之和不超过 $t-1$. 对剩下方格用归纳假设知其可剪为至多 $2 t-3$ 段, 符合要求. 故一共至多剪为 $2 t-1$ 块. 由归纳原理知断言成立.

回到原题.

![](https://cdn.mathpix.com/cropped/2024_02_26_22ee18c0b158d9328a31g-20.jpg?height=431&width=437&top_left_y=544&top_left_x=815)

图 12

按如图 12 方式为方格表标号, 则可将其视为 $1 \times 4 n^{2}$ 的方格表, 由断言知两人都采取最佳策略时 $M=2 k-1$. 证毕.

评注 本题较容易猜出答案, 证明中运用降维考虑的常用思想.

1.4 T6 给定正整数 $n$ 和 $N=n^{2021}$. 现有 2021 个以 $O$ 为圆心的同心圆,和从 $O$ 点发出的 $N$ 条均匀分布的射线. 在这 $2021 N$ 个圆与射线的交点中, 一部分已被染成红色, 其余的尚未染色. 现已知无论如何从每个圆上选取一个点,总存在一个角度 $\theta$ 使得在进行以 $O$ 为旋转中心, $\theta$ 为旋转角的旋转后, 所有选取的点都被旋转到原本红色点的位置. 证明: 开始时染红的点数量的最小值为 $2021 n^{2020}$.

证明 (陈实) 一方面, 设 2021 个圆为 $C_{1}, C_{2}, \cdots, C_{2021}$, 设圆 $C_{i}$ 与 $N$ 条射线交点所成的集合为 $S_{i}$, 其中红点组成集合 $R_{i}(i=1,2, \cdots, 2021)$, 记

$$
S_{i}=\left\{P_{i, 1}, P_{i, 2}, \cdots, P_{i, N}\right\}
$$

对于 $S_{1} \times S_{2} \times \cdots \times S_{2021}$ 中两个有序点组 $\left(P_{1, i_{1}}, P_{2, i_{2}}, \cdots, P_{2021, i_{2021}}\right)$ 与 $\left(P_{1, j_{1}}, P_{2, j_{2}}, \cdots, P_{2021, j_{2021}}\right)$, 定义它们是 “同轴的” 当且仅当存在一个角度 $\theta$ 使得在进行以 $O$ 为旋转中心, $\theta$ 为旋转角的旋转后, 每个 $P_{t, i_{t}}$ 旋转为 $P_{t, j_{t}}(t=$ $1,2, \cdots, 2021)$. 那么 “同轴” 是一种等价关系, 将 $S_{1} \times S_{2} \times \cdots \times S_{2021}$ 划为若干等价类, 注意同一等价类中不同点组的同一位置不相同 (否则旋转后完全相同).故等价类至少 $\frac{N^{2021}}{N}=N^{2020}$ 个.
依题意知 $R_{1} \times R_{2} \times \cdots \times R_{2021}$ 覆盖所有等价类, 从而

$$
\left|R_{1}\right| \cdot\left|R_{2}\right| \cdots\left|R_{2021}\right| \geq N^{2020}
$$

故

$$
\left|R_{1}\right|+\left|R_{2}\right|+\cdots+\left|R_{2021}\right| \geq 2021 N^{\frac{2020}{2021}}
$$

即红点至少 $2021 n^{2020}$ 个.

另一方面, 给出构造: 将 $N$ 条直线依次标为 $0,1, \cdots, N-1$, 对每个圆 $C_{i}$,设 $C_{i}$ 与第 $j$ 号直线交于点 $P_{i, j}(i=1,2, \cdots, 2021 ; j=0,1, \cdots, N-1)$, 将 $0,1, \cdots, N-1$ 在 $n$ 进制下写为 2021 位数 (每一位均可为 0 ), 从小至大为第 1 位,第 2 位, 第 2021 位. 令 $R_{i}=\left\{P_{i, j} \mid j\right.$ 在 $n$ 进制下第 $i$ 位为 0$\}, i=1, \cdots, 2021$.

只需证明对任意 2020 个数 $d_{1}, d_{2}, \cdots, d_{2020}$, 存在 $P_{1, i_{1}} \in R_{1}, P_{2, i_{2}} \in$ $R_{2}, \cdots, P_{2021, i_{2021}} \in R_{2021}$, 使得

$$
i_{k}+d_{k} \equiv i_{k+1} \quad(\bmod N)
$$

对 $k=1,2, \cdots, 2020$ 成立. 即找一个数 $t$, 在 $n$ 进制下 $t$ 第一位为 $0, t+d_{1}$ 第二位为 $0, t+d_{1}+\cdots+d_{k}$ 第 $k+1$ 位为 $0(k=1,2, \cdots, 2020)$. 只需依次确定 $t$的第一位, ‥, 第 2021 位即可, 故构造符合条件. 证毕.

评注 本题难度中等.结论的形式提示使用均值不等式证明 $\left|R_{1}\right| \cdot\left|R_{2}\right| \cdots \cdots$ $\left|R_{2021}\right| \geq N^{2020}$, 注意用等价类来刻画旋转关系.构造的关键是用 2021 维数组 (2021位数), 之后对 $R_{i}$ 的构造则水到渠成.

$2.4 \mathrm{~T} 6$ 给定两正整数 $k \leq n$. IMO 国内有 $n$ 个村庄, 其中某些之间有道路相连. 对任意两个村庄, 它们之间的距离被定义为从其中一个村庄到另外一个村庄所经过的最小道路数. 倘若不可能从一个村庄到另一个, 那么它们之间的距离被定义为无穷.

刚刚抵达 IMO 国的 Alice 正在某处进行隔离观察,所以她并不了解村庄间道路的布局, 但她知道 $n$ 和 $k$ 的值. 她想要知道距离最远的两个村庄之间距离是否有限, 为此, 在每通拨给 IMO 办公室的电话中, 她选择两个村庄, 询问它们之间距离是大于, 等于还是小于 $k$. 办公室将诚实地回答 (无穷距离是大于的).

证明: Alice 可以在 $\frac{2 n^{2}}{k}$ 通电话之内确定最远的两个村庄之间距离是否无穷.

证明 (杨轩屹、周隀顺) 将题目转化为图论语言: 村庄视为点, 道路视为边. Alice 可以采取如下策略: 初始时选取一点, 记为初始点 $v_{1}$, 询问该点与其余所有点的点对的距离, 记为第 1 次操作. 对任何时刻, 定义:

“小点”: 不为 $v_{1}$, 存在另一点与该点距离被询问且回答为小于 $k$.

“亮点”: 不为 $v_{1}$ 或小点, 存在一点 (不为 $v_{1}$ 与小点) 与其的点对尚未被询问,且存在另一点与其构成的点对已被询问, 询问结果等于 $k$.

“暗点”: 不为 $v_{1}$ 或小点, 与其他非 $v_{1}$ 或小点的点的距离均被询问过, 且存在另一点与其构成点对被询问, 询问结果等于 $k$.

“大点”: 图中不为小点、亮点、暗点、 $v_{1}$ 的点.

初始时, 所有点除 $v_{1}$ 外均为大点.

定义 Alice 的第一次操作之后的一次操作: 若某个时刻图中存在大点与亮点, 则选取任意亮点, 询问其与剩余所有大点与亮点构成的点对 (已问过的点对不再询问). 此操作完成后该亮点必变为暗点或小点. 图中不存在大点或亮点时终止操作, 此时,

(1) 若图中无大点, 则图连通.

(2) 若图中无亮点且有大点, 则任意大点不与除大点以外的点连边, 即图不连通. (其中图是否连通等价于所有距离是否有穷.)

故 Alice 的操作有限步内必可得到正确的结果.

下证: Alice 可在 $\frac{2 n^{2}}{k}$ 步内得到结果.

设 $m$ 次操作得到结果, $m=1$ 时结论平凡. 不妨设 $m \geq 2$. 对 $i \geq 2$, 设第 $i$ 次操作 Alice 选取的亮点为 $v_{i}$. 则对任意 $1 \leq i<j \leq m, v_{i}$ 与 $v_{j}$ 的距离大于等于 $k$, 否则第 $i$ 次操作时 $v_{j}$ 变成了“小点”, 矛盾.

记 $v_{1}$ 到 $v_{2}$ 长为 $k$ 的路径为 $l_{1}$, 对 $i \geq 2$, 存在某点与 $v_{i}$ 的距离为 $k$, 取该点到 $v_{i}$ 长为 $k$ 的路径 $l_{i}$, 记

$$
A_{i}=\left\{v \in l_{i} \mid 0 \leq v \text { 与 } v_{i} \text { 的距离 } \leq\left\lceil\frac{k}{2}\right\rceil-1\right\}\left(v_{i} \in A_{i}\right) .
$$

于是 $\left|A_{i}\right|=\left\lceil\frac{k}{2}\right\rceil$, 且由 $v_{i}$ 两两距离大于等于 $k$ 知 $A_{i}$ 两两不交, 故 $m\left\lceil\frac{k}{2}\right\rceil \leq n$, 所以 $m \leq \frac{n}{\left\lceil\frac{k}{2}\right\rceil} \leq \frac{2 n}{k}$. 又因为每次操作最多询问 $n$ 次, 所以询问总数 $\leq m n \leq \frac{2 n^{2}}{k}$.证毕.

评注 本题是一道难度较大的组合题. 通过尝试, 猜出本题的构造较为容易,可通过具体分析对构造进行较小的调整使之符合要求. 构造的可行性证明关键在于对不必询问的点对计数, 此类问题的解决应有意识地寻找计数对象. 最后一步的放缩可以加以改进, 可通过估计每次操作的询问次数将上界改进为 $\frac{n^{2}}{k}$.

$3.1 \mathrm{~T} 2$ 我们用平面上的一个点表示一座城市. 已知现有 $n \geq 2$ 个城市, 且对其中每个城市 $X$, 存在一个城市 $N(X)$ 离这座城市严格地比其他城市离这座
都近. 政府在且仅在每对城市 $X$ 和 $N(X)$ 之间修了一条路. 并且我们知道, 从任意一座城市出发, 总能经过一系列路到达其他任何城市. 我们称一个城市 $Y$ 为近郊的, 如果它是离某个城市 $X$ 最近的城市 $N(X)$. 证明: 至少存在 $\frac{n-2}{4}$ 个近郊的城市.

证明 (周韬顺) 构造图 $G, G$ 的顶点为所有城市, 其中每个 $X$ 向 $N(X)$ 连一条有向边, 则 $G$ 有 $n$ 条边, 又由题中条件知 $G$ 是弱连通的, 故 $G$ 恰有一个圈. 设有 $m$ 个近郊的城市, 注意到对于城市 $A, X, B$, 若 $\angle A X B \leq 60^{\circ}$, 则

$$
|A B| \leq|A X| \text { 或 }|A B| \leq|B X| \text {, }
$$

所以

当 $|A X| \geq|B X|$ 时, $A \rightarrow X$ 不可能成立, 否则 $|A B|>|A X| \geq|B X|$.

对任意近郊的城市 $X$, 设

$$
N\left(A_{1}\right)=N\left(A_{2}\right)=\cdots=N\left(A_{k}\right)=X
$$

若 $k \geq 6$, 则存在 $A_{i} \neq A_{j}$ 使 $\angle A_{i} X A_{j} \leq 60^{\circ}$, 由 (1) 知矛盾.

若 $k=5$, 设 $B=N(X)$, 若 $B \notin\left\{A_{1}, A_{2}, \cdots, A_{5}\right\}$, 由于对任意 $i \neq j$ 有 $\angle A_{i} X A_{j}>60^{\circ}$, 所以存在 $i$ 使 $\angle B X A_{i} \leq 60^{\circ}$, 由 $|B X| \leq\left|A_{i} X\right|$ 及 (1) 知矛盾.

所以 $B \in\left\{A_{1}, A_{2}, \cdots, A_{5}\right\}$, 故 $B \rightarrow X \rightarrow B$ 是 $G$ 中的圈, 因此使 $\operatorname{deg}(x)=$ 5 的 $x$ 至多 2 个, 故对 $G$ 的边计数有 $n=|E(G)| \leq 4 m+2$, 所以有 $m \geq \frac{n-2}{4}$. 原题证毕.

评注 本题主要思路是分析局部性质 (即控制入度) 来估计 $m$ 的下界. 需要对这种每个点发出一条边的图论模型有一定了解: 每个连通分支由一个圈及其入流树构成。

$3.3 \mathrm{~T} 3$ 给定正整数 $n$ 和 $k$ 满足 $n \geq k+1$. 在一个星球上有 $n$ 个国家, 其中某些国家之间建立了外交关系, 使得每个国家都至少 $k$ 个其他国家建交. 一个邪恶的大反派想要挑战国家间的关系, 因此他执行了以下计划:

(1) 首先他选定了两个国家 $A$ 和 $B$, 并命令他们分别领导同盟 $A$ 和 $B$, (因此 $A \in \mathrm{A}$ 且 $B \in \mathrm{B})$.

(2) 其他任何国家独立地选择是否要加入同盟 $A$ 或 $B$.

(3) 在所有其他国家做出选择后, 对加入不同同盟的 $X \in \mathrm{A}$ 和 $Y \in \mathrm{B}$, 终止两国间的外交关系.

证明: 无论国家间开始的外交关系是怎样的, 大反派总能选取两个国家 $A$ 和
$B$ 使得无论其他国家选择加入哪个同盟, 都有至少 $k$ 对外交关系被终止.

证明 (周佳一) 对于一个图 $G=(V ; E)$ 是简单图, $X \subseteq V$. 定义:

$f(X)=\mid\left\{e \in E \mid e\right.$ 的一端在 $X$ 中, 另一端在 $X^{c}$ 中 $\} \mid\left(X^{c}=V \backslash X\right)$,

$G$ 中两个点 $x, y$ 的割是边集 $F \subseteq E$, 使得在 $G$ 中删去 $F$ 中的边后可以将 $G$ 划分为两个连通分支 $X 、 Y$, 使得 $x \in X, y \in Y$.

断言 对 $X, Y \subseteq V$, 总有:

$$
\begin{gathered}
f(X)+f(Y) \geq f(X \cup Y)+f(X \cap Y) \\
f(X)+f(Y) \geq f(X \backslash Y)+f(Y \backslash X)
\end{gathered}
$$

证明 对于 $B \subseteq A \subseteq V$, 以及 $x \notin A, x \in V$, 易知

$$
f(A \cup\{x\})-f(A) \leq f(B \cup\{x\})-f(B)
$$

从而, 对于 $M, M \cap A=\varnothing, M \subseteq V$, 有

$$
f(A \cup M)-f(A) \leq f(B \cup M)-f(B) .
$$

取 $B=X \cap Y, M=Y \backslash X, A=X$, 则有

$$
f(X \cup Y)-f(X) \leq f(Y)-f(X \cap Y),
$$

(1) 得证.

$$
\begin{aligned}
& \text { 又由 } \\
& \begin{aligned}
f(X \backslash Y)+f(Y \backslash X) & =f\left(X \cap Y^{c}\right)+f\left(\left(X \cup Y^{c}\right)^{c}\right)=f\left(X \cap Y^{c}\right)+f\left(X \cup Y^{c}\right) \\
& \leq f(X)+f\left(Y^{c}\right)=f(X)+f(Y),
\end{aligned}
\end{aligned}
$$

(2) 得证.

回到原题: 作图 $G=(V ; E), V$ 代表 $n$ 个国家, 两点连边当且仅当对应的两国建交. 原题转化为: 可以在 $V$ 中选取 2 个点 $x, y$ 使得 $x, y$ 的最小割的边数大于等于 $k$. 对于两点 $a \neq b$ 和点集 $A, B, a \in A, b \in B, A \cap B=\varnothing, A \cup B=V$.定义 $A 、 B$ 是 $a 、 b$ 的最小分割方式, 如果 $f(A)=a, b$ 最小割的边数.

任取两点 $x \neq y$ 及它们的最小分割的方式 $X 、 Y, x \in X, y \in Y$, 若 $|X|$ 或 $|Y|$ 中有一者为 1 , 不妨设 $|X|=1$, 则 $f(X)=\operatorname{deg}(x) \geq k$, 那么在最初选定 $x, y$后, 至少有 $k$ 对外交关系终止, 原题得证.

下设 $u \neq x, u \in X$, 取出 $x$ 与 $u$ 的最小分割方式 $T, T^{c}$, 其中 $u \in T$.

$y \notin T$ 时, 由 (1) 知

$$
f(T)+f(X) \geq f(T \cup X)+f(T \cap X),
$$

又 $f(X \cup T) \geq f(X)$, 故

$$
f(T \cap X) \leq f(T) .
$$

也就是说 $X \cap T,(X \cap T)^{c}$ 也是 $x, u$ 的最小分割方式, $x \notin X \cap T$.

$y \in T$ 时, 由 (2) 知

$$
f(T)+f(X) \geq f(T \backslash X)+f(X \backslash T)
$$

$T \backslash X,(T \backslash X)^{c}$ 是 $x, y$ 的最小分割方式, 故

$$
f(X) \leq f(T \backslash X), f(T) \geq f(X \backslash T)
$$

$X \backslash T 、(X \backslash T)^{c}$ 也是 $x, u$ 的最小割方式, $u \notin X \backslash T$.

由以上讨论, 可得到一些最小分割方式使得 $X \supsetneqq X_{1} \supsetneqq X_{2} \supsetneqq \cdots X_{k}$, 直到 $\left|X_{k}\right|=1$, 此时 $f\left(X_{k}\right) \geq k$. 证毕.

评注 本题有一定难度, 解题的核心是一个直接的想法: 若 $|X|$ 或 $|Y|=1$, 则命题是显然的, 于是想从一组最小割出发逐步严格缩小 $X$ 或 $Y$ 的规模. 进而考虑 $X \cap T$ 与 $X \backslash T$ 这两个集合, 得到 (1) (2) 两个充分的不等式, 验证其正确后问题便得以解决.

