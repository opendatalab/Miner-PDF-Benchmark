数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 三角形一个特定结构下的特殊点性质探究 

$$
\text { 向一铭 }
$$

(上海位育中学, 200231)

2017 年 5 月 20 日, 林天齐老师在 “我们爱几何” 微信公众号中发表了一道题:

问题 0.1 如图 1, $\triangle A B C$ 中, $I$ 为内心, $O$ 为外心, $E \in B I \cap A C, F \in C I \cap A B$. $I \in U V$, 且 $U V \perp O I, U \in E F, V \in B C$. 证明: $I V=2 U I$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-01.jpg?height=368&width=440&top_left_y=1232&top_left_x=814)

图 1

2017 年 8 月 24 日, 金磊老师在 “我们爱几何”微信公众号上发表了一道题:

问题 0.2 如图 2, $\triangle A B C$ 中, $A H_{a}$ 为高, $X_{a}$ 为 $A H_{a}$ 中点, $E=B X_{a} \cap A C, F=$ $C X_{a} \cap A B . X_{a} \in U V$, 且 $U V \perp O X_{a}, U \in E F, V \in B C$. 证明: $X_{a} V=2 U X_{a}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-01.jpg?height=422&width=460&top_left_y=2025&top_left_x=798)

图 2

修订日期: 2020-04-14.
笔者发现这两道题结构非常相似, 于是展开研究.

## I. 预备知识

为便于行文, 除特殊说明外, 约定下列字母所代表的几何意义:

$\triangle A B C$ 中, $M_{a}, M_{b}, M_{c}$ 分别为 $B C, C A, A B$ 的中点. $X_{a}, X_{b}, X_{c}$ 分别为高 $A H_{a}, B H_{b}, C H_{c}$ 的中点. $O, I, H, G, K$ 分别为外心, 内心, 垂心, 重心, 共轭重心.记三边长分别为 $a, b, c$. 半周长为 $p$, 内切圆半径 $r$, 外接圆半径 $R$. 对平面上一点 $P$, 记 $P$ 关于 $\triangle A B C$ 的赛瓦三角形为 $\triangle P_{a} P_{b} P_{c}$, 其中 $P_{a} \in B C$ 等 $(P \neq X)$. 记 $P^{*}$ 为 $P$ 关于 $\triangle A B C$ 的等角共轭点. 再设 $\frac{B P_{a}}{C P_{a}}=a_{p}, \frac{C P_{b}}{A P_{b}}=b_{p}, \frac{A P_{c}}{B P_{c}}=c_{p}$.

在指明了点 $P$ 和 $\triangle A B C$ 的基础上, 我们用 $\angle 1$ 至 $\angle 12$ 分别代表图 3 中所示的角, 用符号 $[x]$ 代表 $\cot \angle x(x=1,2, \cdots, 12)$ :

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-02.jpg?height=394&width=642&top_left_y=1111&top_left_x=707)

图 3

为方便叙述, 我们引入以下定义:

定义 1.1 对于平面上任意 $\triangle A B C$, 内部一点 $P, U \in P_{b} P_{c}, V \in B C$ 且 $U P V \perp O P$. 若 $P V=2 P U$, 则称 $P$ 关于 $A-B C$ 具有性质 $\Omega$. 而若 $P$ 关于 $A-B C, B-C A, C-A B$ 都满足性质 $\Omega$, 称 $P$ 关于 $\triangle A B C$ 满足性质 $\Omega$. 在指明了三角形和点 $P$ 的情况下, 简记为 $P$ 满足性质 $\Omega$. 为了严谨, 规定外心满足性质 $\Omega$, 且若 $P_{b} P_{c} / / B C, B C \perp O P$, 则点 $P$ 关于 $A-B C$ 具有性质 $\Omega$.

注: 当 $P$ 在三角形外时, 有完全类似的结论, 但情况繁多, 无法一一列举. 下文中笔者也是考虑点 $P$ 在形内的情况.

现在给出本文需要用到的一些其它定义或引理:

定义 1.2 平面上一点关于一个三角形的赛瓦三角形与原三角形的透视轴称为该点关于该三角形的三线性极线(trilinear polar).

引理 1.3 (余切联合定理) $\triangle A B C$ 中, 点 $X$ 为 $A B$ 边上一点, 且 $X A: X B=$
$m: n, \angle C X B=\alpha, \angle A C X=\beta$, 则

$$
\left\{\begin{array}{l}
(m+n) \cot \alpha=n \cot \angle A-m \cot \angle B, \\
m \cot \beta=(m+n) \cot \angle C+n \cot \angle A .
\end{array}\right.
$$

证明 作 $C D \perp A B$ 于 $D$. 设 $C D=h$, 则有

$$
A X=h \cot \angle A-h \cot \alpha, B X=h \cot \angle B+h \cot \alpha,
$$

由题设 $m X B=n X A$, 利用上式可得

$$
(m+n) \cot \alpha=n \cot \angle A-m \cot \angle B \text {. }
$$

作 $X E / / B C$ 交 $A C$ 于 $E$, 由平行线的性质知 $A E: C E=m: n$, 注意到 $\angle A E X=\angle C$, 在 $\triangle C A X$ 中对 $A C$ 边上一点 $E$ 使用上面的结论即得

$$
m \cot \beta=(m+n) \cot \angle C+n \cot \angle A \text {. }
$$

故引理获证!

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-03.jpg?height=366&width=523&top_left_y=1199&top_left_x=778)

图 4

引理 1.4 设 $P$ 是 $\triangle A B C$ 内一点, 则 $\frac{B P_{a}}{C P_{a}}=\frac{S_{\triangle A B P}}{S_{\triangle A C P}}$, 其中 $S_{\triangle X Y Z}$ 表示 $\triangle X Y Z$的面积.

该结论容易证明, 在此不再赘述.

引理 $1.5 \triangle A B C$ 中, 点 $A, B, C$ 关于 $\odot O$ 的切线分别交 $B C, C A, A B$ 于 $P, Q, R$. 则 $P, Q, R$ 三点共线(勒莫恩线), 且 $P Q R \perp O K$.

证明 如图 5 , 由极线的基本性质可知只需证明 $K$ 关于 $\odot O$ 的极线过 $P$.

延长 $A K$ 交 $\odot O$ 于 $F$, 由于 $A K$ 是 $\triangle A B C$ 的 $A-$ 陪位中线, 故 $A B F C$ 为调和四边形, 由调和四边形的性质知 $A, F$ 关于 $\odot O$ 的两条切线与直线 $B C$ 三线共点, 从而 $P F$ 是 $\odot O$ 的切线 ${ }^{[1]}$.

注意到 $A F$ 为 $P$ 关于 $\odot O$ 的极线, 则 $P$ 关于 $\odot O$ 的极线过 $K$, 从而 $K$ 关于 $\odot O$ 的极线过 $P$. 故引理获证!

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-04.jpg?height=405&width=506&top_left_y=223&top_left_x=775)

图 5

引理 1.6 设 $P$ 是 $\triangle A B C$ 内一点, $P$ 在三边的垂足为 $D, E, F$. 则

$$
C D=\frac{P E+P D \cdot \cos \angle C}{\sin \angle C}
$$

证明 当 $\angle C$ 是锐角或直角时, 过 $P$ 作 $A C$ 的平行线交 $B C$ 于 $X$, 过 $X$ 作 $A C$ 的垂线, 垂足为 $Y$. 则

$$
\frac{P E}{\sin \angle C}=\frac{X Y}{\sin \angle C}=C X, P D \cdot \cot \angle C=P D \cdot \cot \angle P X D=D X
$$

故

$$
C D=D X+X C=P D \cdot \cot \angle C+P E \cdot \csc \angle C=\frac{P E+P D \cdot \cos \angle C}{\sin \angle C} .
$$

当 $\angle C$ 是钝角时,

$$
\frac{P E}{\sin \angle C}=\frac{X Y}{\sin \angle C}=C X, P D \cdot \cot \angle C=-P D \cdot \cot \angle P X D=-D X,
$$

故

$$
C D=-D X+X C=P D \cdot \cot \angle C+P E \cdot \csc \angle C=\frac{P E+P D \cdot \cos \angle C}{\sin \angle C} .
$$

引理获证!

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-04.jpg?height=391&width=485&top_left_y=1872&top_left_x=794)

图 6

定义 1.7 (三线坐标) 平面上任取一个 $\triangle A B C$, 三线坐标是一组有序的三元数, 它是 $\triangle A B C$ 所在平面上一点到三边的有向距离的比值. 这三边的顺序约定为 $B C, C A, A B$, 而距离的方向以各边的向外的法线方向为正. 任一点 $P$ 的三
线坐标以 $(x: y: z)$ 记之, 例如重心的三线坐标为 $\left(\frac{1}{a}: \frac{1}{b}: \frac{1}{c}\right)$.

引理 $1.8^{[2]}$ 设互不重合的三点 $P, Q, R$ 关于 $\triangle A B C$ 的三线坐标为 $\left(x_{1}: y_{1}:\right.$ $\left.z_{1}\right),\left(x_{2}: y_{2}: z_{2}\right),\left(x_{3}: y_{3}: z_{3}\right)$, 则 $P, Q, R$ 三点共线等价于

$$
\left|\begin{array}{lll}
x_{1} & y_{1} & z_{1} \\
x_{2} & y_{2} & z_{2} \\
x_{3} & y_{3} & z_{3}
\end{array}\right|=0 .
$$

## II. 三线性极线的启发一性质 $\Omega$ 的一个等价条件

问题 0.1 和问题 0.2 的相似性启发了笔者对于一般情况的思考. 除了内心和高中点, 重心、垂心也满足性质 $\Omega$. 在证明这几个问题的时候, 笔者发现它们的证明方法都不太一样, 这与问题本身的相似性不一致. 于是笔者开始思考, 或许有一个一般的方法, 对这类问题都能有效.

2017 年 5 月 21 日, 台湾嘉义的平面几何爱好者 TelvCohl 发现了该问题与三线性极线之间直接的关系, 从而在一定程度上揭示了相似性的原因, 并将问题转换成了一个方便处理的问题.

我们先来看 TelvCohl 发现的这个定理:

定理 2.1 ${ }^{[3]} \triangle A B C$ 中, 设点 $P$ 的三线性极线为 $t$, 过 $P$ 作 $t$ 的平行线交 $P_{b} P_{c}$于 $U, B C$ 于 $V$, 则 $P V=2 P U$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-05.jpg?height=506&width=799&top_left_y=1703&top_left_x=637)

图 7

证明 如图 $7, P_{b} P_{c}$ 交 $B C$ 于 $J, P_{a} P_{b}$ 交 $A B$ 于 $K, U V$ 交 $J A$ 于 $L$.

注意到 $C P_{b} A P B P_{a}$ 是完全四边形, 而完全四边形的一条对角线被另一条对角线调和分割, 故 $B, A, P_{c}, K$ 为调和点列, 所以 $J V, J L, J U, J K$ 成调和线束. 又 $L V / / t$, 于是 $U$ 为 $L V$ 中点.
类似可知 $J B, J U, J P, J A$ 成调和线束, 于是 $V, U, P, L$ 成调和点列, 由调和点列的性质知 $L U \cdot P V=P U \cdot L V$.

又 $L V=2 L U$, 代入上面的式子可得 $P V=2 P U$.

定理 2.1 之逆 $\triangle A B C$ 中, 设点 $P$ 的三线性极线为 $t$, 过 $P$ 作一直线交 $P_{b} P_{c}$于 $U$, 交 $B C$ 于 $V$, 且 $P V=2 P U$, 则 $U V / / t$.

证明 如图 7, 仍有 $V, U, P, L$ 成调和点列, 所以 $U$ 是 $L V$ 中点, 因此 $U V / / t$.

问题本身要证明的这个线段比例命题有时难以处理, 但通过定理 2.1 , 这个命题变为了一个更加简洁对称的命题, 即转化为了刻画三线性极线的问题. 在很多时候, 定理 2.1 大大地简化了问题的解答. 下面提供三个例子.

问题 2.2 证明内心 $I$ 关于 $A-B C$ 具有性质 $\Omega$ (问题 0.1).

证明 设 $A$ 所对的旁心为 $I_{1}$, 类似定义 $I_{2}, I_{3}$. 设 $\triangle I_{1} I_{2} I_{3}$ 的外心为 $O^{\prime}$. 注意到 $I, O$ 分别是 $\triangle I_{1} I_{2} I_{3}$ 的垂心、九点圆圆心, 故 $I, O, O^{\prime}$ 共线.

设 $I_{a} I_{c} \cap A C=S, I_{b} I_{c} \cap B C=X$. 因为 $C, A, I_{b}, S$ 成调和点列, 且 $B I_{b}$ 平分 $\angle A B C$, 所以 $B I_{b} \perp B S$, 即 $S, I_{3}, I_{1}$ 共线. 同理 $X, I_{3}, I_{2}$ 共线.

又因 $A, C, I_{3}, I_{1}$ 共圆, 故 $S$ 在 $\odot(A B C), \odot\left(I_{1} I_{2} I_{3}\right)$ 的根轴上, 进而 $S X$ 是这两圆的根轴, 得 $S X \perp O^{\prime} O, S X \perp O I \Rightarrow S X / / U V$. 由定理 2.1, $I V=2 I U$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-06.jpg?height=834&width=997&top_left_y=1682&top_left_x=541)

图 8
用类似的方法可以证明旁心也满足性质 $\Omega$.

问题 2.3 证明共轭重心 $K$ 关于 $A-B C$ 具有性质 $\Omega$.

证明 如图 9 , 过 $A, B$ 分别作 $\odot O$ 的切线, 分别交 $B C, A C$ 于 $P, Q$.

由引理1.5, $K_{b}, K_{c}, P$ 共线, $K_{a}, K_{c}, Q$ 共线, 且 $O K \perp P Q$. 所以 $P Q$ 是 $K$ 关于 $\triangle A B C$ 的三线性极线. 再由定理 2.1 可知 $K V=2 K U$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-07.jpg?height=626&width=719&top_left_y=658&top_left_x=660)

图 9

问题 2.4 证明 $X_{b}$ 关于 $A-B C$ 具有性质 $\Omega$.

证明 我们先来证明 $X_{a}$ 关于 $A-B C$ 具有性质 $\Omega$ (问题 0.2 ). 如图 10 , 延长 $F E$ 交 $B C$ 于 $X$, 取 $H_{a} X$ 中点 $Y$, 设 $A H_{a}$ 交 $E F$ 于 $Z$. 因 $B, C, H_{a}, X$ 成调和点列, 故 $Y X_{a}^{2}-X_{a} A^{2}=Y H_{a}^{2}=Y C \cdot Y B=O Y^{2}-O A^{2}$. 于是 $O X_{a} \perp A Y$. 即 $U V / / A Y, V$ 为 $H_{a} Y$ 中点. 由 $A, X_{a}, Z, H_{a}$ 成调和点列可得 $X_{a} H_{a}=3 X_{a} Z$.

直线 $U V$ 截 $\triangle Z H_{a} X$, 由 Menelaus 定理得:

$$
\frac{U Z \cdot X_{a} H_{a} \cdot V X}{U X \cdot X_{a} Z \cdot V H_{a}}=1
$$

则

$$
\frac{U Z}{U X}=\frac{1}{9}
$$

再由直线 $Z H_{a}$ 截 $\triangle X U V$, 由 Menelaus 定理得:

$$
\frac{Z U \cdot X_{a} V \cdot H_{a} X}{Z X \cdot X_{a} U \cdot H_{a} V}=1
$$

则

$$
\frac{X_{a} V}{X_{a} U}=2
$$

即 $X_{a} V=2 X_{a} U$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-08.jpg?height=431&width=594&top_left_y=207&top_left_x=731)

图 10

回到原题, 如图 11, 设 $X_{b}$ 关于 $\triangle A B C$ 的塞瓦三角形为 $\triangle X_{b_{a}} X_{b_{b}} X_{b_{c}}$, 延长 $X_{b_{b}} X_{b_{c}}$ 交 $B C$ 于 $L$, 延长 $X_{b_{a}} X_{b_{c}}$ 交 $A C$ 于 $M$, 再延长 $V U$ 交 $A C$ 于 $P$, 设 $U V$交 $X_{b_{a}} X_{b_{c}}$ 于 $S$.

若 $X_{b_{a}} X_{b_{c}} / / A C$, 易知 $B A=B C$, 此时 $X_{b} V=2 X_{b} U$.

若 $X_{b_{a}} X_{b_{c}}$ 与 $A C$ 不平行, 则由前面问题 0.2 的证明可知 $P X_{b}=2 X_{b} S$, 由定理 2.1 之逆, $M L / / U V$, 再由定理 $2.1, X_{b} V=2 X_{b} U$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-08.jpg?height=466&width=592&top_left_y=1269&top_left_x=732)

图 11

性质 $\Omega$ 的叙述仅关于三角形中某两个点的选取对称. 而由定理 2.1, 我们可以看出性质 $\Omega$ 关于 $A, B, C$ 的选取皆对称. 此处对问题 2.4 的证明就便是这种对称性的体现.一般地, 我们可以给出以下定理:

定理 2.5 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 关于 $A-B C$ 满足性质 $\Omega \Leftrightarrow P$ 满足性质 $\Omega$.

因此下文中我们将不再使用 $A-B C$ 及类似的记号, 而直接说某点满足性质 $\Omega$. 现在我们可以给出性质 $\Omega$ 的第一个等价条件:

定理 2.6 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 关于 $\triangle A B C$ 满足性质 $\Omega \Leftrightarrow P$ 关于 $\triangle A B C$ 的三线性极线和它关于 $\triangle A B C$ 外接圆的极线平行或点 $P$ 是 $\triangle A B C$ 外
心、重心中的某一个.

这由定理 2.1 及其逆命题可直接推出, 需要注意外心不存在极线, 以及重心不存在三线性极线.

定理 2.6 不但给了我们解这类问题的一个思路, 而且还给了我们一个十分简洁的等价条件. 下面我们将以此为基础进一步转化问题.

## III. 性质 $\Omega$ 的其它等价条件

笔者发现, 使用定理 2.1 来解决这类问题中的某些问题有点力不从心. 比如证明 $X_{a}$ 的等角共轭点满足性质 $\Omega$, 此时使用定理 2.1 似乎功效甚少. 于是笔者开始思考还有没有其它方法来转化这类问题.

定理 3.1 对于任意的 $\triangle A B C$ 和其内部一点 $X$, 设 $X$ 关于 $\triangle A B C$ 的三线性极线为 $a, X$ 关于 $\triangle A B C$ 外接圆的极线为 $b, X$ 关于 $\triangle A B C$ 的塞瓦三角形和圆内接塞瓦三角形的透视轴为 $c$, 则 $a / / b \Leftrightarrow a / / c, a / / b \Leftrightarrow b / / c$.

证明 如图 12, 设 $X$ 关于 $\triangle A B C$ 的塞瓦三角形为 $\triangle D E F$, 圆内接塞瓦三角形为 $\triangle G R J$. 设 $D E \cap G R=K, A B \cap G R=M, A B \cap D E=Q, D F \cap G J=L$, $J G \cap C A=N, C A \cap D F=P$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-09.jpg?height=956&width=868&top_left_y=1578&top_left_x=591)

图 12
对 $\triangle A D Q$ 及截线 $G K M$ 使用 Menelaus 定理, 得

$$
\frac{D G \cdot A M \cdot Q K}{D K \cdot Q M \cdot A G}=1
$$

从而

$$
\frac{A M}{Q M}=\frac{D K \cdot A G}{D G \cdot Q K}
$$

同理有

$$
\frac{A N}{N P}=\frac{D L \cdot A G}{D G \cdot P L}
$$

所以

$$
a\left\|b \Leftrightarrow \frac{A M \cdot N P}{Q M \cdot A N}=1 \Leftrightarrow \frac{D K \cdot P L}{Q K \cdot D L}=1 \Leftrightarrow a\right\| c .
$$

再对 $\triangle A G M$ 和截线 $D K Q$ 使用 Menelaus 定理

$$
\frac{A D \cdot G K \cdot M Q}{A Q \cdot M K \cdot G D}=1
$$

从而

$$
\frac{M Q}{A Q}=\frac{M K \cdot G D}{A D \cdot G K}
$$

同理有

$$
\frac{N P}{A P}=\frac{N L \cdot G D}{A D \cdot G L}
$$

故

$$
a / / b \Leftrightarrow \frac{M Q \cdot A P}{A Q \cdot N P}=1 \Leftrightarrow \frac{M K \cdot G L}{G K \cdot N L}=1 \Leftrightarrow b / / c .
$$

综上可知, 命题获证!

定理 3.2 对于 $\triangle A B C$ 和其内部一点 $X$, 则点 $X$ 满足性质 $\Omega \Leftrightarrow([6]-$ $[1])([3]-[8])=([3]-[2])([6]-[7])$.

证明 仍如图 12 , 为了保证刚才定义的点存在, 我们先来证明一些特殊情况:

(1) 当 $D F / / A C 、 B A \neq B C$ 时,

左边成立时, $A C=2 F D$, 即 $X$ 为重心, 此时右边显然成立. 右边成立时, 因为 $[3]-[8]=[3]-[2] \neq 0$, 所以右边等价于 $[6]-[1]=[6]-[7]$, 无论它是否等于 0 , 左边都成立. 结论成立.

(1') 当 $D F / / A C 、 B A=B C$ 时, 此时左边右边都成立, 结论成立.

(2) 当 $G J / / A C$ 时, 此时 $X$ 在线段 $A C$ 中垂线上, 左边成立时, 有 $B A=B C$,右边成立; 右边成立时, $([6]-[1])([3]-[8])=0$.

若 $[6]-[1]=0$, 则 $X$ 为外心, 左边成立;
若 $[3]-[8]=0$, 则 $B A=B C$, 左边成立. 结论成立.

(3) 当 $G J / / F D$ 时

如图 13, 有 $F, D, C, A$ 共圆, $\angle B C X=\angle B A G=\angle B C G$. 设 $U V X W \perp$ $O X, U \in D F, V \in J G, W \in A C$. 由蝴蝶定理, $X V=X W$. 左边成立时, $X V=2 X U \Rightarrow D X=D G, F X=F J$. 故 $B C \perp X G, A B \perp X J$. 得 $X$ 是垂心,右边成立.

右边成立时, $([3]-[2])([6]-[7])=0$. 当 $[3]=[2]$ 时, $B A=B C$, 左边成立;当 [6] = [7] 时, $X$ 为垂心, 如图 13, $X V=X W, U X=U V \Rightarrow X W=2 X U$. 左边成立. 结论成立.

当三组线 $D F, G J, C A ; D E, G R, B A ; E F, J R, B C$ 每一组中任两条直线都不平行时, 如图 12, 有

$$
\frac{\sin (\angle 1-\angle 6)}{\sin \angle 1}=\frac{A G}{M G}, \frac{\sin (\angle 7-\angle 6)}{\sin \angle 7}=\frac{D G}{K G}
$$

得

$$
\frac{M G}{K G}=\frac{A G \cdot \sin \angle 1 \cdot \sin (\angle 7-\angle 6)}{D G \cdot \sin \angle 7 \cdot \sin (\angle 1-\angle 6)}, \frac{N G}{L G}=\frac{A G \cdot \sin \angle 2 \cdot \sin (\angle 8-\angle 3)}{D G \cdot \sin \angle 8 \cdot \sin (\angle 2-\angle 3)}
$$

由定理 2.6, 定理 3.1, $X H=2 X I \Leftrightarrow L K / / M N \Leftrightarrow \frac{M G}{K G}=\frac{N G}{L G}$, 代入上式,

$$
\begin{aligned}
\frac{M G}{K G}=\frac{N G}{L G} & \Leftrightarrow \frac{\sin \angle 1 \cdot \sin (\angle 7-\angle 6)}{\sin \angle 7 \cdot \sin (\angle 1-\angle 6)}=\frac{\sin \angle 2 \cdot \sin (\angle 8-\angle 3)}{\sin \angle 8 \cdot \sin (\angle 2-\angle 3)} \\
& \Leftrightarrow \frac{\cos \angle 6-\sin \angle 6 \cdot[1]}{\cos \angle 6-\sin \angle 6 \cdot[7]}=\frac{\cos \angle 3-\sin \angle 3 \cdot[2]}{\cos \angle 3-\sin \angle 3 \cdot[8]} \\
& \Leftrightarrow \frac{[6]-[1]}{[6]-[7]}=\frac{[3]-[2]}{[3]-[8]} \\
& \Leftrightarrow([6]-[1])([3]-[8])=([3]-[2])([6]-[7]) .
\end{aligned}
$$

综上, 在任何情况下, 原命题成立.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-11.jpg?height=457&width=479&top_left_y=1930&top_left_x=797)

图 13

推论 3.3 对于 $\triangle A B C$ 和其内部一点 $X$, 则点 $X$ 满足性质 $\Omega \Leftrightarrow([4]-$
$[5])([1]-[10])=([4]-[9])([1]-[6]) \Leftrightarrow([5]-[4])([2]-[11])=([5]-[12])([2]-[3])$.

推论 3.4 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 关于 $\triangle A B C$ 满足性质 $\Omega \Leftrightarrow([1]-$ $[7])([3]-[2])=([2]-[8])([6]-[1])$.

证明 由定理 3.2, 点 $P$ 关于 $\triangle A B C$ 满足性质 $\Omega$

$$
\begin{aligned}
& \Leftrightarrow([6]-[1])([3]-[8])=([3]-[2])([6]-[7]) \\
& \Leftrightarrow([6]-[1])([3]-[2]+[2]-[8])=([3]-[2])([6]-[1]+[1]-[7]) \\
& \Leftrightarrow([1]-[7])([3]-[2])=([2]-[8])([6]-[1]) .
\end{aligned}
$$

命题获证!

推论 3.5 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 关于 $\triangle A B C$ 满足性质 $\Omega \Leftrightarrow([3]-$ $[11])([5]-[4])=([2]-[3])([4]-[12]) \Leftrightarrow([5]-[9])([1]-[6])=([6]-[10])([4]-[5])$.

经过定理 3.2 的转换, 我们已经将性质 $\Omega$ 转换为一个三角式子了. 但其中涉及 [7], [8] 之类的不好处理的余切值. 下面我们通过几个定理去除这些余切值.

定理 $3.6([1]-[7])\left(a_{p}-a_{p} b_{p}\right)=([2]-[8])\left(1-a_{p} b_{p}\right)$.

证明 由引理 1.3 , 并由 $a_{p} b_{p} c_{p}=1$ 可知:

$$
\begin{aligned}
{[1] } & =\frac{a}{B P_{a}} \cdot \cot \angle A+\frac{C P_{a}}{B P_{a}} \cdot \cot \angle B=\frac{1+a_{p}}{a_{p}} \cdot \cot \angle A+\frac{1}{a_{p}} \cdot \cot \angle B \\
{[2] } & =\frac{a}{C P_{a}} \cdot \cot \angle A+\frac{B P_{a}}{C P_{a}} \cdot \cot \angle C=\left(1+a_{p}\right) \cdot \cot \angle A+a_{p} \cdot \cot \angle C \\
{[7] } & =\frac{b}{A P_{b}} \cdot \cot \angle A P_{a} C+\frac{C P_{b}}{A P_{b}} \cdot[2]=\frac{b_{p}+1}{a_{p}+1} \cdot\left(\cot \angle B-a_{p} \cdot \cot \angle C\right)+b_{p} \cdot[2] \\
& =b_{p} \cdot\left(1+a_{p}\right) \cdot \cot \angle A+\frac{b_{p}+1}{a_{p}+1} \cdot \cot \angle B+a_{p} b_{p} \cdot \cot \angle C \\
{[8] } & =\frac{c}{A P_{c}} \cdot \cot \angle A P_{a} B+\frac{B P_{c}}{A P_{c}} \cdot[1] \\
& =\left(\frac{1}{c_{p}}+1\right) \cdot\left(\frac{1}{a_{p}+1} \cdot\left(a_{p} \cdot \cot \angle C-\cot \angle B\right)\right)+\frac{1}{c_{p}} \cdot[1] \\
& =\left(\frac{1+a_{p}}{a_{p} c_{p}}\right) \cdot \cot \angle A+\frac{1-a_{p} c_{p}}{a_{p} c_{p}\left(a_{p}+1\right)} \cdot \cot \angle B+\frac{a_{p}\left(c_{p}+1\right)}{c_{p}\left(a_{p}+1\right)} \cdot \cot \angle C \\
& =b_{p}\left(1+a_{p}\right) \cdot \cot \angle A+\frac{b_{p}-1}{a_{p}+1} \cdot \cot \angle B+\frac{a_{p} b_{p}+1}{b_{p} c_{p}+1} \cdot \cot \angle C
\end{aligned}
$$

作差, 整理得:

$$
\begin{aligned}
& {[1]-[7]=\left(1-a_{p} b_{p}\right) \cdot\left(\frac{1+a_{p}}{a_{p}} \cdot \cot \angle A+\frac{1}{a_{p}\left(1+a_{p}\right)} \cdot \cot \angle B+\frac{a_{p}}{1+a_{p}} \cdot \cot \angle C\right)} \\
& {[2]-[8]=\left(1-b_{p}\right) \cdot\left(\left(1+a_{p}\right) \cdot \cot \angle A+\frac{1}{1+a_{p}} \cdot \cot \angle B+\frac{a_{p}^{2}}{1+a_{p}} \cdot \cot \angle C\right)}
\end{aligned}
$$

于是有 $([1]-[7])\left(a_{p}-a_{p} b_{p}\right)=([2]-[8])\left(1-a_{p} b_{p}\right)$.

推论 $3.7([3]-[11])\left(a_{p}-1\right)=([4]-[12])\left(a_{p}-a_{p} b_{p}\right),([5]-[9])\left(a_{p} b_{p}-1\right)=$ $([6]-[10])\left(a_{p}-1\right)$.

推论 $3.8 \frac{[1]-[7]}{[2]-[8]}$ 是仿射不变量.

定理 3.9 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 关于满足性质 $\Omega$ 是 $[1]+[3]+[5]=$ $[2]+[4]+[6]$ 的充分必要条件.

证明 先证明如下的引理:

引理 3.10 设点 $P$ 在 $\triangle A B C$ 内部, 记 $P$ 到 $B C 、 C A 、 A B$ 的距离分别为 $d_{a} 、 d_{b} 、 d_{c}$. 则

$$
\left([4]^{2}-[5]^{2}\right) d_{a}^{2}+\left([2]^{2}-[3]^{2}\right) d_{b}^{2}+\left([6]^{2}-[1]^{2}\right) d_{c}^{2}=0 .
$$

证明 设 $P$ 在 $B C 、 C A 、 A B$ 上的垂足为 $D_{a} 、 D_{b} 、 D_{c}$. 则有

$$
\begin{aligned}
& \left([4]^{2}-[5]^{2}\right) d_{a}^{2}+\left([2]^{2}-[3]^{2}\right) d_{b}^{2}+\left([6]^{2}-[1]^{2}\right) d_{c}^{2}=0 \\
\Leftrightarrow & \left(\frac{D_{a} C^{2}}{d_{a}^{2}}-\frac{D_{a} B^{2}}{d_{a}^{2}}\right) \cdot d_{a}^{2}+\left(\frac{D_{b} A^{2}}{d_{b}^{2}}-\frac{D_{b} C^{2}}{d_{b}^{2}}\right) \cdot d_{b}^{2}+\left(\frac{D_{c} B^{2}}{d_{c}^{2}}-\frac{D_{c} A^{2}}{d_{c}^{2}}\right) \cdot d_{c}^{2}=0 \\
\Leftrightarrow & P C^{2}-P B^{2}+P A^{2}-P C^{2}+P B^{2}-P A^{2}=0
\end{aligned}
$$

引理得证.

回到原题, 设 $x=S_{\triangle B C P} 、 y=S_{\triangle A C P} 、 z=S_{\triangle A B P}$. 由引理 1.4, $a_{p}=$ $\frac{z}{y}, b_{p}=\frac{x}{z}, c_{p}=\frac{y}{x}$.

先证明充分性. 由推论 3.4, 推论 3.5, 定理 3.6 和推论 3.7, $([6]-[1])\left(a_{p}-a_{p} b_{p}\right)=([2]-[3])\left(a_{p} b_{p}-1\right),([2]-[3])\left(1-a_{p}\right)=([4]-[5])\left(a_{p} b_{p}-a_{p}\right)$,故有

$$
\begin{aligned}
{[6]-[1]:[2]-[3]:[4]-[5] } & =a_{p} b_{p}-1: a_{p}-a_{p} b_{p}: 1-a_{p} \\
& =\frac{x}{y}-1: \frac{z}{y}-\frac{x}{y}: 1-\frac{z}{y} \\
& =x-y: z-x: y-z .
\end{aligned}
$$

由 $x-y+z-x+y-z=0$ 知 [6] - [1] $+[2]-[3]+[4]-[5]=0$, 充分性获证.

再来证明必要性. 由引理 3.10,

$$
\left([2]^{2}-[3]^{2}\right) d_{b}^{2}+\left([6]^{2}-[1]^{2}\right) d_{c}^{2}=\left([5]^{2}-[4]^{2}\right) d_{a}^{2}=d_{a}^{2}([5]-[4])([5]+[4])
$$

这时利用 $[5]-[4]=[2]-[3]+[6]-[1]$, 式 $(2)=([5]+[4])([2]-[3]+[6]-$
$[1]) d_{a}^{2}=([2]-[3])([5]+[4]) d_{a}^{2}+([6]-[1])([5]+[4]) d_{a}^{2}$. 整理得

$$
([2]-[3])([5]+[4]) d_{a}^{2}-\left([2]^{2}-[3]^{2}\right) d_{b}^{2}=\left([6]^{2}-[1]^{2}\right) d_{c}^{2}-([6]-[1])([5]+[4]) d_{a}^{2},
$$

等价于

$$
([2]-[3])\left(([5]+[4]) d_{a}^{2}-([2]+[3]) d_{b}^{2}\right)=([6]-[1])\left(([6]+[1]) d_{c}^{2}-([5]+[4]) d_{a}^{2}\right) .
$$

注意到 $z=\frac{1}{2} c \cdot d_{c}=\frac{1}{2}([1]+[6]) d_{c}^{2}$, 同理 $y=\frac{1}{2}([2]+[3]) d_{b}^{2}, x=\frac{1}{2}([4]+[5]) d_{a}^{2}$.代入 (3) 式并化简得 $(x-y)([2]-[3])=(z-x)([6]-[1])$. 由 $x 、 y 、 z$ 的对称性,得 (1) 式成立. 由推论 3.4 、推论 3.5 的充分必要性可知必要性成立.

综上, 定理得证.

该定理的证明较繁, 若有读者能通过其它方法直接证明该结论而不通过定理 3.2, 那将极大简化证明过程.

推论 3.11 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 满足性质 $\Omega \Leftrightarrow P^{*}$ 满足性质 $\Omega$.

推论 3.12 设点 $P$ 在 $\triangle A B C$ 内部, 则 $P$ 关于 $\triangle A B C$ 满足性质 $\Omega \Leftrightarrow$ $\cot \angle P M_{a} C+\cot \angle P M_{b} A+\cot \angle P M_{c} B=0$.

该推论的证明只需用到定理 3.9 和引理 1.3 .

定理 3.13 设点 $P$ 在 $\triangle A B C$ 内部, 则 $[1]+[3]+[5]=[2]+[4]+[6] \Leftrightarrow P, G, P^{*}$共线。

证明 设 $P$ 的三线坐标为 $(x: y: z)$, 则 $P^{*}(y z: x z: x y)$. 另有 $G(b c: a c: a b)$.由引理 1.8 , 右边等价于

$$
\left|\begin{array}{ccc}
b c & a c & a b \\
y z & x z & x y \\
x & y & z
\end{array}\right|=0,
$$

即 $b c x\left(y^{2}-z^{2}\right)+\operatorname{cay}\left(z^{2}-x^{2}\right)+a b z\left(x^{2}-y^{2}\right)=0$.

作 $P$ 在三边上的垂线, 垂足分别为 $D, E, F$. 由引理 1.6, 并注意到

$$
[2]=\frac{A E}{P E}=\frac{\frac{z+y \cos \angle A}{\sin \angle A}}{y}=\frac{z}{y \sin \angle A}+\cot \angle A=\frac{2 z R}{y a}+\cot \angle A
$$

等等, 则左边等价于

$$
\begin{array}{r}
{[4]-[3]+[2]-[1]+[6]-[5]=0 \Leftrightarrow \frac{y}{x c}-\frac{x}{y c}+\frac{z}{y a}-\frac{y}{z a}+\frac{x}{z b}-\frac{z}{x b}=0} \\
\Leftrightarrow b c x\left(y^{2}-z^{2}\right)+\operatorname{cay}\left(z^{2}-x^{2}\right)+a b z\left(x^{2}-y^{2}\right)=0,
\end{array}
$$

命题获证.
定理 3.14 设点 $P$ 在 $\triangle A B C$ 内部, 则 $[1]+[3]+[5]=[2]+[4]+[6] \Leftrightarrow$ $[1]^{2}+[3]^{2}+[5]^{2}=[2]^{2}+[4]^{2}+[6]^{2}$.

证明 我们只需证明如下的结论: 任意 $\triangle A B C$ 及其内部一点 $P$, 有

$$
[1][3]+[3][5]+[5][1]=[2][4]+[4][6]+[6][2] .
$$

注意到三角恒等式:

$$
\cot x \cot y+\cot y \cot z+\cot z \cot x=\frac{\sin (x+y+z)}{\sin x \sin y \sin z}+1 \text {, }
$$

(1) 等价于 $\frac{\sin \angle 2 \cdot \sin \angle 4 \cdot \sin \angle 6}{\sin \angle 1 \cdot \sin \angle 3 \cdot \sin \angle 5}=1$, 而这正是角元赛瓦定理.

## IV. Thomson 三次曲线

至此, 我们已经发现了许许多多满足性质 $\Omega$ 的点了, 它们是否在某一条曲线上呢?

根据定理 3.13, 在三角形形内满足性质 $\Omega$ 的点 $P$, 都会使得 $P, G, P^{*}$ 共线.一般地, 我们把一点和其等角共轭点所在直线过定点 (称为“枢点”)的点的轨迹叫做主等角三次曲线. 利用引理 1.8 进行计算可知, 主等角三次曲线有普遍方程:

$$
f_{1} x\left(y^{2}-z^{2}\right)+f_{2} y\left(z^{2}-x^{2}\right)+f_{3} z\left(x^{2}-y^{2}\right)=0,
$$

其中, 枢点 $F$ 的三线坐标为 $\left(f_{1}: f_{2}: f_{3}\right)$.

不难知道, 以重心为枢点的主等角三次曲线的方程是(也是性质 $\Omega$ 的一个等价条件):

$$
b c x\left(y^{2}-z^{2}\right)+\operatorname{cay}\left(z^{2}-x^{2}\right)+a b z\left(x^{2}-y^{2}\right)=0 .
$$

事实上, 它已经出现在定理 3.13 的证明中. 现在我们清楚了, 满足性质 $\Omega$的点确实是在一条曲线上. 一般地, 我们称以重心为枢点的主等角三次曲线为 Thomson 三次曲线(如图 14 ). 正是因为它有丰富的几何性质, 在 CTP[4] 上有许多关于这条曲线的结论.

## V. 小结与展望

小结一下我们得到的性质 $\Omega$ 的等价条件.

设 $\triangle A B C$ 内部一点 $P, U V \perp O P, P \in U V, U \in P_{b} P_{c}, V \in B C$. 设 $P$ 关于 $\triangle A B C$ 的三线性极线为 $a, P$ 关于 $\triangle A B C$ 外接圆的极线为 $b, P$ 关于 $\triangle A B C$ 的塞瓦三角形和其关于 $\triangle A B C$ 的圆内接塞瓦三角形的透视轴为 $c$. 设点 $P$ 关于

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-16.jpg?height=534&width=651&top_left_y=196&top_left_x=702)

图 14

$\triangle A B C$ 的等角共轭点为 $P^{*} . P$ 的三线坐标为 $(x: y: z)$. 下面给出一系列性质 $\Omega$的等价条件:

1. $U V / / a$
2. $a / / b$
3. $a / / c$
4. $b / / c$
5. $([6]-[1])([3]-[8])=([3]-[2])([6]-[7])$ 及类似式子
6. $([1]-[7])([3]-[2])=([2]-[8])([6]-[1])$ 及类似式子
7. $[1]+[3]+[5]=[2]+[4]+[6]$
8. $\cot \angle P M_{a} C+\cot \angle P M_{b} A+\cot \angle P M_{c} B=0$
9. $P, G, P^{*}$ 共线
10. $[1]^{2}+[3]^{2}+[5]^{2}=[2]^{2}+[4]^{2}+[6]^{2}$
11. $b c x\left(y^{2}-z^{2}\right)+\operatorname{cay}\left(z^{2}-x^{2}\right)+a b z\left(x^{2}-y^{2}\right)=0$

笔者在此提出一个相关猜想, 希望有读者能够解答:

猜想 5.1 设点 $P$ 在 $\triangle A B C$ 内部, 点 $P$ 关于 $\triangle A B C$ 的等角共轭点为 $P^{*}$,过 $P$ 且垂直于 $P M_{a}$ 的直线交 $B C$ 于 $T_{a}$. 类似定义 $T_{b}, T_{c}$. 则 $P, G, P^{*}$ 共线 $\Leftrightarrow T_{a}, T_{b}, T_{c}$ 共线, 且在共线时有 $T_{a} T_{b} T_{c} \perp P P^{*}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_40085d903bbb2e23ab09g-17.jpg?height=614&width=1106&top_left_y=218&top_left_x=475)

图 15

## VI. 结语

希望本文能起到抛砖引玉的效果, 引起几何爱好者们的注意, 并给出本文未解之题的答案. 在此特别感谢卢圣老师的指导与数学新星网的支持. 在本文的写作过程中, 笔者不仅收获到探究问题的快乐, 语言表达的严谨性也得到了一定训练.

## 参考文献

[1] 曹珏武. 叶中豪. 调和四边形及其应用 $[\mathrm{J}]$. 中等数学, 2016: no.1, 1-2.

[2] 吴悦辰. 三线坐标与三角形特征点 $[M]$. 哈尔滨工业大学出版社, 2015: 5-10.

[3] Telvcohl. 对一个题目的推广. 纯几何吧. http://tieba.baidu.com/p/5125232674.

[4] https://bernard-gibert.pagesperso-orange.fr/Exemples/k002.html.

