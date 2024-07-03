数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2020 年 OTJMO 第二季试题解答与评析 

金晟治

(浙江省温州中学, 325014)

指导教师: 邵达

OTSS (Online Test Snowy Series) 是 AoPS (Art of Problem Solving) 上新近成立的一个讨论小组, 出了不少模拟美国数学协会系列考试的模拟题. OTJMO (Online Test Junior Mathematical Olympiad) 是他们在 2020 年 12 月举行的一场线上模拟测试, 模拟美国的 USAJMO 考试. 笔者认为, 试题整体难度不大, 但部分试题形式比较新颖, 尤其是第 $2,3,6$ 题值得研究与欣赏. 其中, 第 1,4 题为容易题, 第 $2,3,5$ 题为中档题, 第 6 题比较有难度, 没有太困难的题. 本文给出了试题的解答与评析. 直于水平, 不当之处在所难免, 敬请读者不吝赐教.

## I. 试 题

1. 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{N}^{*}$, 使得对任意实数 $x, y$ 均有

$$
f^{f(x)}(y)=f(x) f(y)
$$

其中 $f^{a}(b)$ 表示 $f$ 在 $b$ 处的 $a$ 次迭代, 即 $f^{1}(b)=b, f^{a+1}(b)=f\left(f^{a}(b)\right)$.
2. $\triangle A B C$ 内接于圆 $\Gamma$. 过 $B, C$ 分别作 $\Gamma$ 的切线, 两者交于点 $X$. 在 $B C$边上取一个动点 $P$, 过 $P$ 作 $B X$ 平行线, $C X$ 平行线. 这两条直线分别与过 $A$点的 $\Gamma$ 的切线交于点 $C_{1}, B_{1}$. 直线 $C_{1} B_{1}$ 与 $B C$ 交于点 $R, \triangle P B B_{1}$ 外接圆与 $\triangle P C C_{1}$ 外接圆再次相交于 $Q$. 求证: $P Q$ 与 $R X$ 交点为定点.

3. 对正整数 $n$, 设 $A_{1}, A_{2}, \cdots, A_{n}$ 为 $n$ 个互异的 $\{1,2, \cdots, n+1\}$ 的二元子集. 求证：存在两个互异的 $\{1,2, \cdots, n+1\}$ 的子集 $S$ 和 $S^{\prime}$, 使得对任意 $1 \leqslant k \leqslant n$, 均有 $\left|A_{k} \cap S\right|=\left|A_{k} \cap S^{\prime}\right|$, 其中 $|T|$ 表示集合 $T$ 的元素个数.
4. 一个 $n \times n$ 的网格表由 $n^{2}$ 个单元格构成, 其中 $n$ 为正整数. 每个单元格修订日期: 2021-01-20.
的所有边都被绘出, 其中一些单元格的对角线也被绘出, 并且任意一个单元格中至多有一条对角线被绘出, 任意两个有公共边的单元格所绘对角线 (如果有的话) 方向不同. 求 $n$ 的所有值, 使得存在一种绘制方法, 可以从其左下角的顶点出发,一笔绘制该图形 (即每条边或者对角线恰经过一次).
5. 对正整数 $m$, 若存在一个整系数多项式 $P(x)$, 使得对任意正整数 $x$, 均有 $m$ 整除 $(P(x))^{m}-x$, 就称 $m$ 很酷.

(i) 证明所有很酷的数均不含平方因子;

(ii) 对正整数 $n$, 设 $P_{n}$ 表示所有满足 $n \leqslant p \leqslant 2 n$ 的素数 $p$ 的乘积, 求所有正整数 $n$, 使得 $P_{n}$ 很酷.
6. $\triangle A B C$ 内接于圆 $\Gamma$, 其内心为 $I$, 外心为 $O$. 圆 $\omega$ 与 $A B, A C, \Gamma$ 均相切,其中 $\omega$ 与 $\Gamma$ 切点为 $X . B C$ 的垂直平分线与直线 $A X$ 交于点 $S$. 过 $I$ 作 $B C$ 的平行线与 $\triangle A I X$ 外接圆 $\Omega$ 交于点 $K$. 直线 $K S$ 与 $\Omega$ 再次相交于 $T$. 若 $P$ 为 $\triangle T A O$外心, 求证: $T P$ 与 $\triangle B C T$ 的外接圆相切.

## II . 解答与评注

1. 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{N}^{*}$, 使得对任意实数 $x, y$ 均有

$$
f^{f(x)}(y)=f(x) f(y)
$$

其中 $f^{a}(b)$ 表示 $f$ 在 $b$ 处的 $a$ 次迭代, 即 $f^{1}(b)=b, f^{a+1}(b)=f\left(f^{a}(b)\right)$.

解 设 $f$ 的值域为 $S$, 则 $S \subseteq \mathbb{Z}_{+}, S \neq \varnothing$. 对任意 $a, b \in S$, 设 $f(x)=a$, $f(y)=b$, 则由题设知 $f^{f(x)}(y)=f(x) f(y)$, 即 $f^{f(x)-1}(f(y))=f(x) f(y)$, 亦即

$$
f^{a-1}(b)=a b .
$$

若存在 $a \in S, a \neq 1$, 下面证明对任意 $k \in \mathbb{Z}_{+}$,

$$
f^{(a-1) k}(a)=a^{k+1}
$$

当 $k=1$ 时, 在 $(*)$ 中取 $b=a$ 即知成立.

假设 $f^{(a-1) k}(a)=a^{k+1}$ 成立, 则 $a^{k+1} \in S$.

考察 $f^{(a-1)(k+1)}(a)$, 在 $(*)$ 中取 $b=a^{k+1} \in S$, 有

$$
f^{(a-1)(k+1)}(a)=f^{a-1}\left(f^{k(a-1)}(a)\right)=f^{a-1}\left(a^{k+1}\right)=a \cdot a^{k+1}=a^{k+2},
$$

由归纳法即知 $(* *)$ 成立.

特别地, 在 $(*)$ 中取 $k=1$, 得 $a^{2}=f^{(a-1)}(a) \in S$. 取 $k=a+1$, 得 $f^{a^{2}-1}(a)=$
$a^{a+2}$. 而在 $(*)$ 中用 $\left(a^{2}, a\right)$ 代替 $(a, b)$, 得 $f^{a^{2}-1}(a)=a \cdot a^{2}=a^{3}$, 即有 $a^{a+2}=a^{3}$,这在 $a \neq 1$ 时不成立!

故 $S=\{1\}$, 即对任意 $x \in \mathbb{R}, f(x)=1$, 这显然是满足条件的解.

评注 本题需要对题目方程有一定的理解与想法, 容易发现 $(*)$ 是本质, 接下来的想法就是寻找值域中的数代入 $(*)$. 发现 $(*)$ 的右边在 $S$ 中, 于是不断将 $(*)$式右边得到的代入左边即可.
2. $\triangle A B C$ 内接于圆 $\Gamma$. 过 $B, C$ 分别作 $\Gamma$ 的切线, 两者交于点 $X$. 在 $B C$边上取一个动点 $P$, 过 $P$ 作 $B X$ 平行线, $C X$ 平行线. 这两条直线分别与过 $A$点的 $\Gamma$ 的切线交于点 $C_{1}, B_{1}$. 直线 $C_{1} B_{1}$ 与 $B C$ 交于点 $R, \triangle P B B_{1}$ 外接圆与 $\triangle P C C_{1}$ 外接圆再次相交于 $Q$. 求证: $P Q$ 与 $R X$ 交点为定点.

证明 1 先证明下面的引理.

引理 $\Gamma_{1}, \Gamma_{2}$ 为平面上两圆, 对平面上任一点 $P$, 设 $f(P)=$ 幂 ${ }_{P, \Gamma_{1}}-$ 幂 $P_{, \Gamma_{2}}$,即 $P$ 到圆 $\Gamma_{1}, \Gamma_{2}$ 的圆幂差. 则 $f(P)$ 为线性函数, 即任意共线三点 $A, B, C$,有 $\frac{f(A)-f(B)}{f(B)-f(C)}=\frac{\overline{A B}}{\overline{B C}}$, 其中 $\overline{A B}, \overline{B C}$ 表示有向线段长.

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-03.jpg?height=551&width=1060&top_left_y=1392&top_left_x=498)

证明设 $\Gamma_{1}, \Gamma_{2}$ 圆心分别为 $O_{1}, O_{2}$, 半径分别为 $R_{1}, R_{2}$, 则

(i) 若 $O_{1}=O_{2}$, 则 $f(P)=R_{2}^{2}-R_{1}^{2}$ 为定值, 显然知引理成立.

(ii) 若 $O_{1} \neq O_{2}$, 设 $O_{1} O_{2}$ 中垂线为 $l$, 用 $d_{P}$ 表示点 $P$ 到 $l$ 的有向距离, $O_{2}$一侧为正. 设 $H$ 为 $P$ 在 $O_{1} O_{2}$ 上的射影, 则

$$
\begin{aligned}
f(P) & =\left(P O_{1}^{2}-R_{1}^{2}\right)-\left(P O_{2}^{2}-R_{2}^{2}\right) \\
& =\left(P O_{1}^{2}-P O_{2}^{2}\right)-R_{1}^{2}+R_{2}^{2} \\
& =\overline{H O_{1}^{2}}-{\overline{H O_{2}}}^{2}-R_{1}^{2}+R_{2}{ }^{2} \\
& =\left(\overline{H O_{1}}+\overline{H O_{2}}\right) \cdot\left(\overline{H O_{1}}-\overline{H O_{2}}\right)-R_{1}{ }^{2}+R_{2}{ }^{2}
\end{aligned}
$$

$$
=2 d_{P} \cdot O_{1} O_{2}-R_{1}^{2}+R_{2}^{2}
$$

故 $\frac{f(A)-f(B)}{f(B)-f(C)}=\frac{d_{A}-d_{B}}{d_{B}-d_{C}}=\frac{\overline{A B}}{\overline{B C}}$ 成立!

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-04.jpg?height=848&width=916&top_left_y=410&top_left_x=567)

回到原题. 对平面上一点 $S$, 定义 $f(S)=$ 幕 $S, \odot\left(B P B_{1}\right)-$ 幕 $_{S, \odot\left(C P C_{1}\right)}$.

设 $Q P \cap X R=T$, 则 $T$ 在 $\odot\left(B P B_{1}\right)$ 与 $\odot\left(C P C_{1}\right)$ 根轴上, 得 $f(T)=0$. 由引理知

$$
\frac{f(X)}{f(R)}=\frac{\overline{X T}}{\overline{R T}}
$$

由圆幂定理, $f(R)=R P \cdot R B-R P \cdot R C=R P \cdot B C$.

设 $X B$ 交 $\odot\left(B P B_{1}\right)$ 于 $U \neq B, X C$ 交 $\odot\left(C P C_{1}\right)$ 于 $U \neq C$, 则 $\angle U B P=$ $\pi-\angle P B X=\pi-\angle P C X=\pi-\angle C P B_{1}=\angle B P B_{1}$. 故 $U B_{1} P B$ 为等腰梯形,则 $U B=P B_{1}$. 同理 $U C=P C_{1}$, 故

$$
\begin{aligned}
f(X) & =X B \cdot X U-X C \cdot X U \\
& =\left(X B^{2}+X B \cdot B U\right)-\left(X C^{2}+X C \cdot C U\right) \\
& =X B \cdot(B U-C U) \\
& =X B \cdot\left(P B_{1}-P C_{1}\right) .
\end{aligned}
$$

当 $P$ 在运动时, 射线 $R P, R A$ 不变, $P C_{1}, P B_{1}$ 方向不变, 故 $R P B_{1} C_{1}$ 四点形状不变, 因此 $\frac{P B_{1}}{P R}, \frac{P C_{1}}{P R}$ 均为定值, 故

$$
\frac{f(X)}{f(R)}=\frac{X B \cdot\left(P B_{1}-P C_{1}\right)}{R P \cdot B C}=\frac{X B}{B C} \cdot\left(\frac{P B_{1}}{P R}-\frac{P C_{1}}{P R}\right)
$$

为定值, 故 $\frac{\overline{X T}}{\overline{R T}}$ 为定值, 即 $T$ 分定线段 $X R$ 比例为定值, 故 $T$ 为定点.
评注 该解法的动机在于要证明的结论是一条根轴分一条定线段的比例为定值, 于是自然地想到圆幂差线性这一熟知结论.

证明 2 设 $R A$ 分别交 $\odot\left(B P B_{1}\right)$ 与 $\odot\left(C P C_{1}\right)$ 于另一点 $U, V$, 则 $\angle C V A=$ $\angle B P C_{1}=\angle X B C=\angle B A C$, 因此 $\triangle C V A \sim \triangle C A B, V$ 为与 $P$ 无关的定点.同理 $\triangle B U A \sim \triangle B A C, U$ 为与 $P$ 无关的定点.

设 $B U \cap C V=K$, 则 $K$ 为定点. $\angle B U Q+\angle C V Q=\angle C P Q+\angle B P Q=\pi$,得 $K U V Q$ 共圆, 该圆为定圆. 而 $\angle U Q P=\pi-\angle U B P=\pi-2 \angle A B C$ 为定角,故 $Q P$ 与定圆 $\odot(K U V)$ 的另一交点为定点, 设该点为 $T$.

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-05.jpg?height=825&width=945&top_left_y=861&top_left_x=561)

下证 $X, T, R$ 共线.

由 $\angle T K U=\pi-\angle T Q U=\angle U B C$, 知 $K T / / B C$, 故 $\angle K T V=\pi-\angle B U A=$ $\pi-\angle B A C=\pi-\angle B C X=\langle K T, C X\rangle$, 因此 $C X / / T V$, 同理 $B X / / T U$. 设 $U T, V T$分别交直线 $B C$ 于 $M, N$, 则

$$
\frac{B M}{M R}=\frac{\sin \angle B U M}{\sin \angle R U M} \cdot \frac{\sin \angle U R B}{\sin \angle U B R}=\frac{\sin \angle A R B}{\sin 2 B} \cdot \frac{\sin \angle K U T}{\sin 2 C},
$$

这里用到 $\angle R U M=\angle V K T=\angle K C B$.

同理,

$$
\frac{C N}{N R}=\frac{\sin \angle A R C}{\sin 2 C} \cdot \frac{\sin \angle K V T}{\sin 2 B}
$$

故 $\frac{B M}{M R}=\frac{C N}{N R}$. 设 $U M, V N$ 分别交 $X R$ 于 $T_{1}, T_{2}$, 则

$$
\frac{X T_{1}}{T_{1} R}=\frac{B M}{M R}=\frac{C N}{N R}=\frac{X T_{2}}{T_{2} R}
$$

得 $T_{1}=T_{2}$, 故 $T$ 在 $X R$ 上.
评注 该解法中, 关心运动过程中的不变的量, 注意到 $P C_{1}, P B_{1}$ 为夹在 $R B, R A$ 间方向不变的线段, 利用逆平行的观点即可发现定点 $U, V$, 进而发现 $\angle U Q P, \angle V Q P$ 为定角, 故 $\odot(U Q V)$ 为定圆, 且 $Q P$ 与该定圆另一交点为定点, 之后证明该定点在 $X R$ 上, 转化为直线型问题, 容易解决.

3. 对正整数 $n$, 设 $A_{1}, A_{2}, \cdots, A_{n}$ 为 $n$ 个互异的 $\{1,2, \cdots, n+1\}$ 的二元子集. 求证：存在两个互异的 $\{1,2, \cdots, n+1\}$ 的子集 $S$ 和 $S^{\prime}$, 使得对任意 $1 \leqslant k \leqslant n$, 均有 $\left|A_{k} \cap S\right|=\left|A_{k} \cap S^{\prime}\right|$, 其中 $|T|$ 表示集合 $T$ 的元素个数.

证明 用图论的语言叙述这个问题:

$n+1$ 个点构成的简单图 $G$, 边数为 $n$, 求证: 存在顶点的子集 $S \neq S^{\prime}$, 使得 $G$ 中每一条边的两个顶点, 要么均在 $S$ 与 $S^{\prime}$ 中, 要么均不在 $S$ 与 $S^{\prime}$ 中, 要么恰有一个在 $S$ 中, 也恰有一个不在 $S^{\prime}$ 中.

设 $G$ 有 $k$ 个连通分支 $G_{1}, G_{2}, \cdots, G_{k}, G_{i}$ 的顶点数为 $v_{i}$, 边数为 $e_{i}, v_{i} \geqslant 1$, $e_{i} \geqslant 0$, 则

$$
\sum_{i=1}^{k} v_{i}=n+1>n=\sum_{i=1}^{k} e_{i}
$$

因此存在 $i$, 使 $v_{i}>e_{i}$, 故 $e_{i} \leqslant v_{i}-1$. 结合 $G_{i}$ 连通知 $G_{i}$ 为一个树(可以为一个孤立点或一条边), 则 $G_{i}$ 为一个二部图, 设两部分顶点为 $U, V, U \cap V=\varnothing$, $|U \cup V|=v_{i} \neq 0$, 允许 $U, V$ 之一为空. 取 $S=U, S^{\prime}=V$, 则对 $G_{i}$ 中的每一条边, 恰有一点在 $S$ 中, 另一点在 $S^{\prime}$ 中, 对 $G_{i}$ 以外的每一条边, 其两顶点均不在 $S$与 $S^{\prime}$ 中, 满足要求.

评注 从题目中的二元集可联想到图论, 转化为图论问题后就直观了许多,后面的处理方法十分常规.

4. 一个 $n \times n$ 的网格表由 $n^{2}$ 个单元格构成, 其中 $n$ 为正整数. 每个单元格的所有边都被绘出, 其中一些单元格的对角线也被绘出, 并且任意一个单元格中至多有一条对角线被绘出，任意两个有公共边的单元格所绘对角线 (如果有的话) 方向不同. 求 $n$ 的所有值, 使得存在一种绘制方法, 可以从其左下角的顶点出发,一笔绘制该图形 (即每条边或者对角线恰经过一次).

解 所求 $n$ 为 $1,2,3$, 构造以格点为顶点的图. 如图所示, 可知每一点度数均为偶数, 且为连通图, 故可一笔画.

下证: $n \geqslant 4$ 时不存在可一笔画的绘法.

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-07.jpg?height=411&width=939&top_left_y=206&top_left_x=564)

从左至右分别为 $n=1,2,3$ 的情形

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-07.jpg?height=474&width=426&top_left_y=722&top_left_x=815)

$n \geqslant 4$ 的情形

假设 $n \geqslant 4$ 使 $n \times n$ 存在一种可一笔画的绘法(不关心一笔画的起点), 则将其看作以格点为顶点的图(如图). 图中奇度顶点不超过 2 个, 因此存在上、下、左、右边界(不含四个角上的顶点)之一, 使该边界上 $n-1$ 个点的度数均为偶数, 不妨设为左边界. 考察左上角顶点下方的点, 依次记为 $A_{1}, A_{2}, A_{3}, \cdots$,则 $A_{1}, A_{2}, A_{3}$ 都应是偶度. 因此 $A_{1}, A_{2}, A_{3}$ 都应再连出一条对角线. 若 $A_{1}$ 所连对角线指向右上, 则 $A_{2}$ 所连对角线只能与其不同向, 指向右下, 此时 $A_{3}$ 不可再画出对角线, 矛盾! 若 $A_{1}$ 所连对角线指向右下, 则 $A_{2}$ 无法连出对角线, 矛盾!

故 $n \geqslant 4$ 均不满足.

评注 第一步转化为考虑奇度点十分显然, 而边界上的点原本度为 3 , 稍加尝试即可.

5. 对正整数 $m$, 若存在一个整系数多项式 $P(x)$, 使得对任意正整数 $x$, 均有 $m$ 整除 $(P(x))^{m}-x$, 就称 $m$ 很酷.

(i) 证明所有很酷的数均不含平方因子;

(ii) 对正整数 $n$, 设 $P_{n}$ 表示所有满足 $n \leqslant p \leqslant 2 n$ 的素数 $p$ 的乘积, 求所有正整数 $n$, 使得 $P_{n}$ 很酷.

(i) 证明 设 $m$ 有平方因子, 设 $p^{2} \mid m, p$ 为素数. 若 $m$ 很酷, $P(x) \in \mathbb{Z}[x]$ 满
足对任意 $x \in \mathbb{Z}_{+}, m \mid P(x)^{m}-x$, 则取 $x=p$, 于是有 $p^{2} \mid P(p)^{m}-p, m \geqslant 2$.若 $p \mid P(p)$, 则 $p^{2} \mid P(p)^{m}$, 故 $p^{2} \nmid P(p)^{m}-p$, 矛盾! 若 $p \nmid P(p)$, 则 $p \nmid P(p)^{m}$,故 $p^{2} \nmid P(p)^{m}-p$ 矛盾!

(ii) 解 我们证明: 对任意 $n \in \mathbb{Z}_{+}, n \neq 2, P_{n}$ 都很酷 (以下同余式中的分数均按数论倒数理解).

当 $n \geqslant 3$ 时, 考察每一个素数 $p, n \leqslant p \leqslant 2 n$, 若存在 $0 \leqslant i<j \leqslant p-1$, 使得 $i^{P_{n}} \equiv j^{P_{n}}(\bmod p)$, 则 $i \neq 0$. 于是

$$
\left(\frac{i}{j}\right)^{P_{n}} \equiv 1 \quad(\bmod p)
$$

结合

$$
\left(\frac{i}{j}\right)^{p-1} \equiv 1 \quad(\bmod p)
$$

故

$$
\left(\frac{i}{j}\right)^{\left(P_{n}, p-1\right)} \equiv 1 \quad(\bmod p)
$$

而 $P_{n}$ 中的每一个素因子均在 $[n, 2 n]$ 中, $\frac{p-1}{2}$ 的素因子均不超过 $\frac{p-1}{2} \leqslant \frac{2 n-1}{2}<n$,故 $\left(P_{n}, p-1\right)=1$. 因此 $i \equiv j(\bmod p)$, 故 $i=j$, 矛盾!

故 $0^{P_{n}}, 1^{P_{n}}, \cdots,(p-1)^{P_{n}}(\bmod p)$ 互不相同, 恰好为 $0,1,2, \cdots, p-1$ 的排列,故对任意 $i \in\{0,1, \cdots, p-1\}$, 存在 $a_{i} \in\{0,1, \cdots, p-1\}$, 使得 $a_{n}^{P_{n}} \equiv i(\bmod p)$.

取整系数多项式

$$
Q_{p}(x) \equiv \sum_{i=0}^{p-1} \prod_{0 \leqslant j \leqslant p-1, j \neq i} \frac{x-i}{j-i} \cdot a_{i}(\bmod p)
$$

则对任意 $0 \leqslant i \leqslant p-1$, 有

$$
Q_{p}(i)^{P_{n}} \equiv a_{i}^{P_{n}} \equiv i \quad(\bmod p)
$$

故

$$
p \mid Q_{p}(x)^{P_{n}}-x, \forall x \in \mathbb{Z}
$$

设 $[n, 2 n]$ 中全部素数为 $p_{1}, p_{2}, \cdots, p_{t}$,则这样得到 $t$ 个多项式

$$
Q_{p_{1}}(x), Q_{p_{2}}(x), \cdots, Q_{p_{t}}(x),
$$

满足上述条件.

对这些多项式中的相同次数的项的系数分别使用中国剩余定理, 知存在整系数多项式 $P(x)$, 使得 $P(x)$ 与 $Q_{p_{i}}(x)$ 对应项系数 $\bmod p_{i}$ 都同余, $i=1,2, \cdots, t$.

故对任意 $x, i$, 有 $p_{i} \mid P(x)^{p_{n}}-x$, 故 $P_{n} \mid P(x)^{p_{n}}-x$, 即 $P_{n}$ 很酷.

$n=1$ 时, $P_{1}=2$, 取 $P(x)=x$ 即知 $P_{1}=2$ 很酷.
$n=2$ 时, $P_{2}=6$, 由于任何平方数 $\bmod 3$ 不余 2 , 故 $6 \nmid P(2)^{6}-2$, 故 $P_{2}=6$不是很酷的.

综上,所求 $n$ 为所有不等于 2 的正整数.

评注 第 (ii) 问中模数为若干素数之积, 自然想到分解为素数分别处理, 构造多项式时利用 Lagrange 插值多项式也是常见方法, 最后本质上就是要证明 $x^{P_{n}}$ $(\bmod p)$ 可取遍完系, 指数上的素因子结构清晰, 于是不难想到考虑阶.
6. $\triangle A B C$ 内接于圆 $\Gamma$, 其内心为 $I$, 外心为 $O$. 圆 $\omega$ 与 $A B, A C, \Gamma$ 均相切,其中 $\omega$ 与 $\Gamma$ 切点为 $X . B C$ 的垂直平分线与直线 $A X$ 交于点 $S$. 过 $I$ 作 $B C$ 的平行线与 $\triangle A I X$ 外接圆 $\Omega$ 交于点 $K$. 直线 $K S$ 与 $\Omega$ 再次相交于 $T$. 若 $P$ 为 $\triangle T A O$外心, 求证: $T P$ 与 $\triangle B C T$ 的外接圆相切.

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-09.jpg?height=731&width=854&top_left_y=1071&top_left_x=607)

证明 1 设弧 $\overparen{B C}$ 中点 $M$, 弧 $\widehat{B A C}$ 中点 $N$, 由内切圆性质知 $N, I, X$ 共线.

$\angle A I K=\langle A M, B C\rangle=\angle A N M=90^{\circ}-\angle A X I$.

$\Rightarrow I K$ 过 $\odot(A I X)$ 圆心, 即 $I K$ 为直径

$\Rightarrow \angle I A K=\angle I X K=90^{\circ}$

$\Rightarrow N, A, K$ 共线, $M, X, K$ 共线, $S M \cdot S N=S X \cdot S A=S T \cdot S K$

$\Rightarrow M, N, K, T$ 共圆

$\Rightarrow \angle S M T=\angle S K N=\angle S X T$

$\Rightarrow S, M, X, T$ 共圆

$\Rightarrow \angle K A T=\angle K X T=\angle M S T$

$\Rightarrow N, A, T, S$ 共圆

$$
\begin{aligned}
& \Rightarrow \angle A T M=\angle A T S-\angle M T S=\pi-\angle A N S-\angle M N K=\pi-2 \angle A N O= \\
& \pi-\angle A O M \\
& \Rightarrow A, O, M, T \text { 共圆 } \\
& \Rightarrow \angle A T O=\angle A M O=90^{\circ}-\angle M N A=\angle A K I=\angle A T I \\
& \Rightarrow O, I, T \text { 共线. }
\end{aligned}
$$

结合 $O A=O M$, 知 $O A^{2}=O M^{2}=O I \cdot O T$

$\Rightarrow O B^{2}=O C^{2}=O I \cdot O T$

$\Rightarrow \triangle O B I \sim \triangle O T B, \triangle O C I \sim \triangle O T C$

故 $P T$ 与 $\odot(B T C)$ 相切

$\Leftrightarrow \angle P T C=\angle T B C$

$\Leftrightarrow \angle P T O-\angle O T C=\angle O B T-\angle O B C$

$\Leftrightarrow\left(\frac{\pi}{2}-\angle O A T\right)-\angle O C I+\angle O C B=\angle O I B$

$\Leftrightarrow \frac{\pi}{2}-\angle S M T+\angle B C I=\angle I B C+\angle T I K$

$\Leftrightarrow \frac{\pi}{2}=\angle S M T+\left(\frac{\angle A B C}{2}-\frac{\angle A C B}{2}\right)+\angle T X K$

$\Leftrightarrow \frac{\pi}{2}=(\angle S M T+\angle T S M)-\angle A M N$

$\Leftrightarrow \frac{\pi}{2}=(\pi-\angle S T M)-\left(\frac{\pi}{2}-\angle A N M\right)$

$\Leftrightarrow \angle S T M=\angle A N M$

$\Leftrightarrow N, M, T, K$ 共圆,成立.

评注该证明前半部分利用图中 $S$ 为根心及各种角度关系得到大量共圆、共线,要证明的结论关键在于刻画 $T P, T B, T C$ 的方向. $T P$ 在 $\triangle A O T$ 中利用各边的方向可刻画，难点在于 $T B, T C$ 的方向. 这里发现 $O, I, T$ 共线并结合 $A, O, M, T$ 所共圆中弧中点的结构发现 $O M^{2}=O I \cdot O T$, 从而巧妙地处理了 $T B$ 与 $T C$.

另外, 在得出 $O, I, T$ 共线后还可用反演变换处理:

证明 2 同证 1, 知 $A, O, M, T$ 共圆, $O, I, T$ 共线, $O M^{2}=O I \cdot O T$.

以 $\odot O$ 为基圆作反演变换, 则 $T \leftrightarrow I$, 点 $B, C, A$ 反形均为自身, 故 $\odot(T B C) \leftrightarrow$ $\odot(B I C)$.

设点 $O$ 在 $\odot(A O T)$ 中对径点为 $Q, O P$ 交 $A M$ 于 $R, O$ 关于 $A M$ 对称点为 $L$. 由 $O M=O A$, 知

$$
\begin{aligned}
& O Q \perp A M \\
\Rightarrow & O M^{2}=O R \cdot O Q=O L \cdot O P
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_12d4f35cd762134ea9adg-11.jpg?height=883&width=866&top_left_y=204&top_left_x=595)

注意到 $\odot(O I L)$ 与 $\odot(B I C)$ 都过点 $I$, 且都关于 $A I$ 对称, 故两圆相切于点 $I$, 即 $P T$ 与 $\odot(T B C)$ 切于点 $T$.

