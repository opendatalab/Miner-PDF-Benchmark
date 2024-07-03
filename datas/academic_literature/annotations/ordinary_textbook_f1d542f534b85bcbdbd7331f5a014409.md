数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年保加利亚数学奥林匹克试题解析 

曾午午

(湖南省雅礼中学, 410007)

指导教师: 彭熹

2021 年保加利亚数学奥林匹克试题与往年相比, 整体难度偏易, 但质量仍然较高, 保持了一贯简洁优美的风格, 其中第三题为较困难的问题, 以下是这次比赛的试题和解答.

## I. 试 题

1. 某城市有 4 条南北向的道路, 以及 $n \geq 3$ 条东西向的道路, 这些道路互相交叉, 形成了 $4 n$ 个路口. 这些路口将每条南北向道路分为 $n-1$ 段街道, 每条东西向道路分为 3 段街道. 现在, 市长需要尽可能少的关闭一些路口, 使得城市中没有闭合回路 (即从任意一段街道出发, 不回头的话, 无法经过若干个路口之后回到原来的位置).

(1) 证明: 恰有 $n$ 个路口被关闭.

(2) 证明: 如果四个角落的路口均没有被关闭, 且你可以从任意一个街道走到任意另一个街道, 则恰有 3 个边界上的路口被关闭 (注: 边界指第一条或第四条南北向道路, 或者第一条或第 $n$ 条东西向道路).

2. 如图所示, 锐角 $\triangle A B C$ 外心为 $O$, 在过 $C$ 点的高上取一点 $T$, 使 $\angle T B A=\angle A C B$. 若直线 $C O$ 与边 $A B$ 交于点 $K$, 证明: $A B$ 中垂线、过 $A$ 点的高、直线 $K T$ 三线共点.
3. 求所有函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$, 使得对任意正实数 $x, y$,

![](https://cdn.mathpix.com/cropped/2024_02_26_7b892efa3837d978a36dg-1.jpg?height=363&width=360&top_left_y=2017&top_left_x=1382)
均有

$$
f(f(x)+y) f(x)=f(x y+1) .
$$

修订日期: 2021-07-14.

4. 有两个无穷项的等差正整数列:

$$
a_{1}<a_{2}<a_{3}<\cdots ; b_{1}<b_{2}<b_{3}<\cdots
$$

已知存在无穷多对正整数 $(i, j)$, 使得 $i \leq j \leq i+2021$, 且 $a_{i} \mid b_{j}$. 求证：对任意正整数 $i$, 一定存在一个正整数 $j$, 使得 $a_{i} \mid b_{j}$.

5. 平面上是否存在 100 个点组成的集合 $S$, 使得 $S$ 中任意 10 个点的重心仍为 $S$ 中的点?
6. 如图, 在 $\triangle A B C$ 中, $A C>B C, S$ 为其外接圆 $\kappa$ 上弧 $\widehat{A C B}$ 的中点. $I$ 为其内心, 直线 $S I$ 与 $\kappa$ 再次相交于点 $T$. 已知 $D$ 为 $I$ 关于 $T$ 的对称点, $M$ 为边 $A B$ 的中点, 过 $D$ 作 $A B$ 的平行线与直线 $I M$ 交于点 $E$. 求证: $A E=B D$.

![](https://cdn.mathpix.com/cropped/2024_02_26_7b892efa3837d978a36dg-2.jpg?height=399&width=557&top_left_y=977&top_left_x=752)

## II . 解答与评注

1. 某城市有 4 条南北向的道路, 以及 $n \geq 3$ 条东西向的道路, 这些道路互相交叉, 形成了 $4 n$ 个路口. 这些路口将每条南北向道路分为 $n-1$ 段街道, 每条东西向道路分为 3 段街道. 现在, 市长需要尽可能少的关闭一些路口, 使得城市中没有闭合回路 (即从任意一段街道出发, 不回头的话, 无法经过若干个路口之后回到原来的位置).

(1) 证明: 恰有 $n$ 个路口被关闭.

(2) 证明: 如果四个角落的路口均没有被关闭, 且你可以从任意一个街道走到任意另一个街道, 则恰有 3 个边界上的路口被关闭 (注: 边界指第一条或第四条南北向道路, 或者第一条或第 $n$ 条东西向道路).

证明 称四条南北向的道路自西向东依次为 $A, B, C, D$, 道路 $X \in$ $\{A, B, C, D\}$ 上的路口自北向南依次为 $X_{1}, X_{2}, \cdots, X_{n}$. 用图论语言描述这个问题, 即将路口 $A_{i}, B_{i}, C_{i}, D_{i}(i=1,2, \cdots, n)$ 视作图 $G_{n}$ 中的顶点, 街道视作边,两个顶点相邻当且仅当顶点代表的路口之间有街道相连. 题目即要求选出尽可
能少的一些点, 使图 $G_{n}$ 中任一圈上至少有一个点被选出.

![](https://cdn.mathpix.com/cropped/2024_02_26_7b892efa3837d978a36dg-3.jpg?height=374&width=440&top_left_y=281&top_left_x=814)

(1) 首先给出恰选出 $n$ 个顶点的构造: 选出

$$
\left\{B_{i} \mid 1 \leq i \leq n, i \text { 为奇数 }\right\} \bigcup\left\{C_{i} \mid 1 \leq i \leq n, i \text { 为偶数 }\right\} .
$$

易验证这符合要求.

下面对 $n$ 归纳证明至少要选出 $n$ 个顶点.

$n=3$ 时, 假设只要选出两个顶点, 考虑 $A_{1} A_{2} B_{2} B_{1}, C_{1} C_{2} D_{2} D_{1}$ 这两个圈,每个圈上均有点被选出, 故 $A_{3}, B_{3}, C_{3}, D_{3}$ 中无点被选出. 同理 $A_{1}, B_{1}, C_{1}, D_{1}$中无点被选出. 则 $A_{2}, B_{2}, C_{2}, D_{2}$ 中恰有两个被选出, 两个未被选出, 则存在没有点被选出的圈 (如 $A_{2}, C_{2}$ 未选出时, 圈 $A_{1} A_{2} A_{3} B_{3} C_{3} C_{2} C_{1} B_{1}$ ). 矛盾! 故 $n=3$时至少要选出三个顶点.

$n=4$ 时, 考虑 $A_{1} A_{2} B_{2} B_{1}, C_{1} C_{2} D_{2} D_{1}, A_{3} A_{4} B_{4} B_{3}, C_{3} C_{4} D_{4} D_{3}$ 这四个圈,每个圈上至少选出一个顶点, 故至少要选出四个顶点.

设 $n$ 时结论已成立 $(n \geq 3)$, 则在 $n+2$ 时, 考虑 $A_{n+1} A_{n+2} B_{n+2} B_{n+1}$, $C_{n+1} C_{n+2} D_{n+2} D_{n+1}$ 这两个圈, 每个圈上至少选出一个顶点, 故这八个顶点中至少要选出两个. 接下来去掉这八个顶点及其邻边, 得到图 $G_{n}$. 由归纳假设, $G_{n}$ 中至少要选出 $n$ 个顶点, 故 $G_{n+2}$ 中至少要选出 $n+2$ 个. 故 $n+2$ 时结论也成立.

由数学归纳法, 对任意 $n \geq 3$, 至少要选出 $n$ 个顶点.

综上, 最少选出 $n$ 个顶点, 故恰有 $n$ 个路口被关闭. 证毕.

(2) 由于每条街道均可以到达, 则没有两个相邻的顶点同时被选出, 而且删去所有被选出的路口及其邻边, 没有边被重复删去且剩下的图为无圈的连通图,故它是树.

记此时的图为 $G_{n}^{\prime}$. 结合 (1) 知

$$
\begin{gathered}
\left|V\left(G_{n}\right)\right|=4 n,\left|V\left(G_{n}^{\prime}\right)\right|=4 n-n=3 n, \\
\left|E\left(G_{n}\right)\right|=4(n-1)+3 n=7 n-4,\left|E\left(G_{n}^{\prime}\right)\right|=\left|V\left(G_{n}^{\prime}\right)\right|-1=3 n-1,
\end{gathered}
$$

故总共删去了 $(7 n-4)-(3 n-1)=4 n-3$ 条边.
又 $G_{n}$ 中, 任一边界点度为 3 , 任一内点 (即非边界点且不在四个角上的点)度为 4 , 且无角上的点被选出. 设选出了 $x$ 个边界点, 由于没有边被重复删去, 则 $3 x+4(n-x)=4 n-3$, 故 $x=3$.

即恰选出了 3 个边界点, 故恰有三个边界上的路口被关闭. 证毕.

评注 本题较为简单, 没有用到复杂的定理或方法, 思路很直接. 尤其是第一问给出了一个重要结论, 降低了本题的难度. 根据题目的描述自然地想到用图论语言叙述问题, 第一问利用小圈归纳, 第二问利用删点和边, 将图变为树. 需要注意的是第 (2) 问证明中的第一句话不能省略.

2. 如图所示, 锐角 $\triangle A B C$ 外心为 $O$, 在过 $C$ 点的高上取一点 $T$, 使 $\angle T B A=\angle A C B$. 若直线 $C O$ 与边 $A B$ 交于点 $K$, 证明: $A B$ 中垂线、过 $A$ 点的高、直线 $K T$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_7b892efa3837d978a36dg-4.jpg?height=469&width=571&top_left_y=1139&top_left_x=754)

证明 设 $\triangle A B C$ 的垂心为 $H, T$ 关于边 $A B$ 的对称点为 $T^{\prime}$, 则 $C, H, T, T^{\prime}$共线, 设此线交 $\odot O$ 于 $C, E$. 则有

$$
\angle T^{\prime} B A=\angle T B A=\angle A C B,
$$

故 $T^{\prime} B$ 为 $\odot O$ 切线.

设 $C$ 的对径点为 $D$, 则 $C, O, K, D$ 共线. 设 $A E$ 与 $B D$ 交于 $F^{\prime}$. 由 $\angle C E D=$ $90^{\circ}$ 知 $D E / / A B$, 故 $O F^{\prime}$ 为 $A B$ 的中垂线.

设 $O F^{\prime}$ 交 $A H$ 于 $F$. 由 $\angle F^{\prime} A B=\angle E C B=\angle F A B$ 知 $F$ 与 $F^{\prime}$ 关于边 $A B$对称，

欲证 $O F^{\prime}, A H, K T$ 共点 $\Leftrightarrow K F T$ 共线 $\Leftrightarrow K F^{\prime} T^{\prime}$ 共线.

对(退化的)圆内接六边形 $B B A E C D$ 用 Pascal 定理,

$$
B B \cap E C=T^{\prime}, B A \cap C D=K, A E \cap B D=F^{\prime} \text {, }
$$

故 $K, F^{\prime}, T^{\prime}$ 共线. 证毕.
评注 本题重点是描述点 $T$ 和点 $F$. 从条件 $\angle T B A=\angle A C B$ 出发, 想到通过作对称点将条件转化为 $T^{\prime} B$ 是切线. 这时发现把 $F$ 关于边 $A B$ 对称后也变得很好描述, 于是局面豁然开朗, 只需证明 $K F^{\prime} T^{\prime}$ 共线, 利用 Pascal 定理即得出证明. 本题与联赛几何题难度相当.

3. 求所有函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$, 使得对任意正实数 $x, y$, 均有

$$
f(f(x)+y) f(x)=f(x y+1)
$$

解 $f(x) \equiv 1$ 或 $f(x)=\frac{1}{x}$.

在(1)中取 $x=2, y=\frac{1}{2}$, 则

$$
f\left(f(2)+\frac{1}{2}\right)=1
$$

故存在 $x_{0} \in \mathbb{R}^{+}$使 $f\left(x_{0}\right)=1$.

(1) 若当且仅当 $x=1$ 时, $f(x)=1$, 对 $x>1$, 令 $y=\frac{x-1}{x}$, 由(1)式得

$$
f\left(f(x)+\frac{x-1}{x}\right)=1
$$

故 $f(x)=\frac{1}{x}$.

对 $x<1$, 令 $y=2$, 由(1)式得

$$
f(f(x)+2) f(x)=f(2 x+1),
$$

由 $f(x)+2,2 x+1$ 均大于 1 , 则

$$
f(f(x)+2)=\frac{1}{(f(x)+2)}
$$

故

$$
\frac{f(x)}{2+f(x)}=\frac{1}{2 x+1}
$$

解得 $f(x)=\frac{1}{x}$.

于是对任意 $x \in \mathbb{R}^{+}, f(x)=\frac{1}{x}$.

(2) 若存在 $t \in \mathbb{R}^{+}, t \neq 1$ 使 $f(t)=1$.

取 $x=t$, 由(1)式得 $f(y+1)=f(t y+1)$ 对任意 $y \in \mathbb{R}^{+}$成立. 用 $t^{k} y$ 代替 $y(k=1,2, \cdots)$, 得

$$
f(y+1)=f(t y+1)=f\left(t^{2} y+1\right)=\cdots
$$

故对任意 $k \in \mathbb{N}, y \in \mathbb{R}^{+}, f(y+1)=f\left(t^{k} y+1\right)$.

用 $\frac{y}{t^{k}}$ 代替 $y$ 得对任意 $k \in \mathbb{Z}, y \in \mathbb{R}^{+}$,

$$
f(y+1)=f\left(t^{k} y+1\right) .
$$

下证对任意 $x \in \mathbb{R}^{+}, f(x)=1$.

假设存在 $x_{0} \in \mathbb{R}^{+}$使 $f\left(x_{0}\right) \neq 1$. 由 $t \neq 1$ 知对任意 $n \in \mathbb{N}^{+}$, 存在 $k \in \mathbb{Z}$ 使 $t^{k}>n, t^{-k}<\frac{1}{n}$. 故存在 $k_{1}, k_{2} \in \mathbb{Z}$ 使

$$
t^{k_{1}} x_{0}-1<0<t^{k_{2}} x_{0}-1 .
$$

取 $k \in \mathbb{Z}$ 使 $t^{k} x_{0}-1$ 与 $f\left(x_{0}\right)-1$ 同号, 在(1)中令

$$
x=x_{0}, y=\frac{f\left(x_{0}\right)-1}{t^{k} x_{0}-1}
$$

则由 $f\left(x_{0}\right)+y=t^{k} x_{0} y+1$, 有

$$
f\left(x_{0} y+1\right)=f\left(f\left(x_{0}\right)+y\right) f\left(x_{0}\right)=f\left(t^{k} x_{0} y+1\right) f\left(x_{0}\right)=f\left(x_{0} y+1\right) f\left(x_{0}\right) .
$$

故 $f\left(x_{0}\right)=1$, 与假设矛盾!

从而假设不成立, 即对任意 $x \in \mathbb{R}^{+}, f(x)=1$. 故 $f(x) \equiv 1$.

综上, $f(x)=\frac{1}{x}$ 或 $f(x) \equiv 1$. 代入原式检验知均满足题意.

评注 本题是六个题中难度最大的一题, 方法很灵活, 先代入 $y=\frac{x-1}{x}$ 猜出答案, 之后固定 $x$, 改变 $y$, 希望通过让 $f(x y+1)=f(f(x)+y)$ 来推出 $f(x)=1$.利用 $f(x y+1)=f\left(t^{k} x y+1\right)$, 问题便得以解决. 本题难度相当于 CMO 第二题、第五题.

4. 有两个无穷项的等差正整数列:

$$
a_{1}<a_{2}<a_{3}<\cdots ; \quad b_{1}<b_{2}<b_{3}<\cdots .
$$

已知存在无穷多对正整数 $(i, j)$, 使得 $i \leq j \leq i+2021$, 且 $a_{i} \mid b_{j}$. 求证: 对任意正整数 $i$, 一定存在一个正整数 $j$, 使得 $a_{i} \mid b_{j}$.

证明 设 $a_{n+1}=n d+a_{1}, b_{n+1}=n d^{\prime}+b_{1}, d, d^{\prime} \in \mathbb{N}^{+}$. 设 $d^{\prime}=q d+r, q \geq 0$, $0 \leq r<d, q, r \in \mathbb{N}$.

由题意对任意大的正整数 $M$, 存在正整数 $n>M$ 及 $k \in\{0,1, \cdots, 2021\}$,使 $a_{n+1} \mid b_{n+1+k}$. 即 $n d+a_{1} \mid(n+k) d^{\prime}+b_{1}$, 而

$$
\begin{aligned}
(n+k) d^{\prime}+b_{1} & =n d q+k q d+r n+r k+b_{1} \\
& =q\left(n d+a_{1}\right)+k q d+r n+r k+b_{1}-a_{1} q
\end{aligned}
$$

故

$$
n d+a_{1} \mid r n+k q d+r k+b_{1}-a_{1} q .
$$

而 $d>r \geq 0$, 故 $n$ 充分大时,

$$
\left|n d+a_{1}\right|>\left|k q d+r n+r k+b_{1}-a_{1} q\right| .
$$

从而存在无穷多个充分大的 $n$ 及 $0 \leq k \leq 2021$ 使

$$
k q d+r n+r k+b_{1}-a_{1} q=0
$$

故

$$
a_{1} q-b_{1}-k q d=r(n+k) \geq r n
$$

则必有 $r=0$. 于是存在 $k \in\{0,1, \cdots, 2021\}$ 使

$$
k q d+b_{1}-a_{1} q=0
$$

记

$$
k_{0}=\frac{a_{1} q-b_{1}}{q d} \in\{0,1, \cdots, 2021\}
$$

则对任意 $n \in \mathbb{N}^{+}$,

$$
\left(n+k_{0}\right) d^{\prime}+b_{1}=q\left(n d+a_{1}\right),
$$

即 $a_{n+1} \mid b_{n+1+k_{0}}$. 于是结论成立. 证毕.

评注 本题较为简单, 核心是若 $a|b| a,|>| b \mid$, 则 $b=0$. 为此先作带余除法,简单估计得余数为 0 , 从而 $k$ 为定值, 即完成证明. 本题难度略低于联赛数论题.

5. 平面上是否存在 100 个点组成的集合 $S$, 使得 $S$ 中任意 10 个点的重心仍为 $S$ 中的点?

解 不存在.

假设存在, 设 $S=\left\{A_{1}, A_{2}, \cdots, A_{100}\right\}$.

建立平面直角坐标系, 使 $y$ 轴不平行于 $S$ 中任两点的连线. 则 $S$ 中任两点的横坐标不同. 设 $A_{i}$ 的横坐标为 $x_{i}, i=1,2, \cdots, 100$. 不妨设 $x_{1}<x_{2}<\cdots<x_{100}$.记 $S_{x}=\left\{x_{1}, x_{2}, \cdots, x_{100}\right\}$. 由重心坐标公式知 $S_{x}$ 中任 10 个不同数的平均数仍在 $S_{x}$ 中. 记

$$
a_{i}=\frac{x_{1}+\cdots+x_{11}-x_{i}}{10}, i=1,2, \cdots, 11 .
$$

则 $x_{1}<a_{i}<x_{11}$, 故 $a_{1}, a_{2}, \cdots, a_{11} \in\left\{x_{2}, x_{3}, \cdots, x_{10}\right\}$, 由抽庹原理知其中必有两数相等, 设 $1 \leq i<j \leq 11, a_{i}=a_{j}$, 则 $x_{i}=x_{j}$, 与 $x_{i}$ 互不相同矛盾!

故假设不成立, 即满足条件的 $S$ 不存在. 证毕.

评注 本题十分有趣, 首先要想到将点投影到一条线上, 这可利用坐标解决;随后考虑将 100 缩小到更方便讨论的范围. 本题可简单地拓展如下:

若 $m$ 维空间中的 $n$ 个点中任 $k$ 个点的重心均在这 $n$ 个点中, 则 $n=k$, 其中
$m \geq 1, n \geq k \geq 3, m, n, k$ 均为整数.

证法完全一样.

6. 如图, 在 $\triangle A B C$ 中, $A C>B C, S$ 为其外接圆 $\kappa$ 上弧 $\widehat{A C B}$ 的中点. $I$ 为其内心, 直线 $S I$ 与 $\kappa$ 再次相交于点 $T$. 已知 $D$ 为 $I$ 关于 $T$ 的对称点, $M$ 为边 $A B$ 的中点, 过 $D$ 作 $A B$ 的平行线与直线 $I M$ 交于点 $E$. 求证: $A E=B D$.

![](https://cdn.mathpix.com/cropped/2024_02_26_7b892efa3837d978a36dg-8.jpg?height=468&width=656&top_left_y=654&top_left_x=700)

证明 设 $\overparen{A B}$ 中点为 $N$, 则 $N M S$ 共线, 且为 $A B$ 的中垂线. 设 $S I$ 交 $A B$ 于点 $K$. 由

$$
\widehat{S A}=\widehat{S B}, \angle S T B=\angle S B A=\angle S N B
$$

知

$$
\triangle S K B \sim \triangle S B T, \triangle S M B \sim \triangle S B N
$$

于是

$$
S B^{2}=S K \cdot S T=S M \cdot S N .
$$

同理

$$
N M \cdot N S=N B^{2}=N I^{2} .
$$

于是

$$
\begin{aligned}
T I^{2} & =N I^{2}-N T^{2} \\
& =N M \cdot N S-N S^{2}+S T^{2} \\
& =S T^{2}-S M \cdot S N \\
& =S T^{2}-S T \cdot S K \\
& =T K \cdot T S .
\end{aligned}
$$

又 $T$ 为 $I D$ 中点, 故 $D K I S$ 为调和点列. 又 $\angle K M S=90^{\circ}$, 故 $\angle D M K=\angle I M K$.
由 $D E / / A B$, 有

$$
\angle M E D=\angle I M K=\angle D M K=\angle E D M
$$

故 $E M=D M$. 又

$$
\angle E M A=\angle D M K, M A=M B \text {, }
$$

故 $\triangle M E A \cong \triangle M D B$, 于是 $A E=D B$. 证毕.

评注 本题难度与联赛几何题相近, 只需将欲证结论一步步转化即可. 本题没有难点, 仅用到调和点列与一个经典的模型, 即过弧中点作直线, 被弦和圆所截.

