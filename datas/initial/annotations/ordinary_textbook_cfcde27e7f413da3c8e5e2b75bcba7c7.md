# 一道几何问题的推广 

付艺渲<br>(山东省实验中学, 250002)

本文的讨论源于下面已知几何问题的研究:

题目 $\triangle A B C$ 中, $D$ 为 $\angle C$ 平分线上一点, 在其垂足圆上取任意一点 $H$, 射线 $C H$ 交 $\odot G D H$ 于 $I$. 证明: $D I$ 为 $\angle A I B$ 的内或外角平分线 (图 1 为内角平分线).

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-1.jpg?height=614&width=625&top_left_y=1241&top_left_x=721)

图 1

若 $D$ 为 $\triangle A B C$ 的内心 $I$, 这一问题是为人所熟知的 (困难的) 命题. 事实上,可以将问题进一步推广为下述形式:

命题 1 如图 2, 在 $\triangle A B C$ 中, $D, E, F$ 分别是 $B C, C A, A B$ 上的点, $\triangle D E F$对 $\triangle A B C$ 的密克点为 $P . G$ 是 $\odot D E F$ 上的点, $A G$ 与 $\odot P D G$ 交于 $H, H P$ 与 $\odot B H C$ 交于 $X . A P$ 与 $\odot A B C$ 交于 $S$. 求证: $S X / / P D$.

笔者在探索这个问题的过程中, 发现了关于等角共轭点和圆雉曲线的一些有趣的几何性质. 蒖于相关资料的缺乏和个人能力所限, 得到的结果可能并非独

收稿日期: 2018-11-13.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-2.jpg?height=617&width=691&top_left_y=200&top_left_x=705)

图 2

创的, 在这里隐请广大读者指正.

## I. 一些基本的引理

我们首先作出如下约定:

1. 文章中将多次出现这样的描述: $B$ 在某个圆 $\omega$ 上, $A B$ 与圆 $\omega$ 再次交于点 $C$, 这是指在直线 $A B$ 上取点 $C$ 满足 $\overline{A B} \cdot \overline{A C}=\rho(A)$, 其中 $\rho(A)$ 为 $A$ 到圆 $\omega$ 的幂.
2. 对于 $\triangle A B C, \varphi$ 是以 $A$ 为中心, $\sqrt{A B \cdot A C}$ 为半径的反演变换, $\theta$ 是以 $\angle B A C$ 的平分线为对称轴的反射变换. $H=\varphi \cdot \theta$, 则称 $H$ 为 Iran 式反演. 在不致引起误解的情形下, 简写为以 $A$ 为中心的 Iran 式反演.

本小节建立如下几个引理.

引理 1 设 $P, Q$ 为关于 $\triangle A B C$ 的一对等角共轭点, 以 $A$ 为中心作 Iran 式反演, $P, Q$ 的像点仍为关于 $\triangle A B C$ 的等角共轭点.

证明 利用反演变换的保角性可以证得结论.

这个结论在指出之后是显然的. 它表明取等角共轭点和作 Iran 式反演这两个映射满足交换律.

引理 $2 \triangle A B C$ 的一条外接圆锥曲线的关于三角形本身的等角共轭像为一条直线。

证明 如图 3, 设 $P, Q, R$ 是雉线上三点, $P_{1}, Q_{1}, R_{1}$ 分别为 $P, Q, R$ 的等角共轭点, 则

$$
\left[A B, A P_{1} ; A Q_{1}, A R_{1}\right]=[A C, A P ; A Q, A R]
$$

$$
\begin{aligned}
& =[B C, B P ; B Q, B R] \\
& =\left[B A, B P_{1} ; B Q_{1}, B R_{1}\right]
\end{aligned}
$$

其中 $\left[l_{1}, l_{2} ; l_{3}, l_{4}\right]$ 表示四条直线的交比.

由交比的几何性质可得 $P_{1}, Q_{1}, R_{1}$ 三点共线.

故引理获证.

值得注意的是上述命题 (引理 2) 的逆命题也是正确的, 即一条不过 $A, B, C$三点的直线关于 $\triangle A B C$ 的等角共轭像为 $\triangle A B C$ 的外接圆锥曲线.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-3.jpg?height=657&width=831&top_left_y=791&top_left_x=612)

图 3

引理 3 给定 $\triangle A B C, D$ 是平面上一点, $A D$ 与 $\odot B C D$ 再次交于点 $P$. 则 $P$在 $\triangle A B C$ 的定外接锥线上等价于 $D$ 在过 $A$ 的定圆上.

证明 如图 4, 取 $P$ 关于 $\triangle A B C$ 的等角共轭点 $Q$, 则 $\angle B A Q=\angle D A C$, 且

$$
\angle A B Q=180^{\circ}-\angle P B C=180^{\circ}-\angle P D C=\angle A D C .
$$

故 $\triangle A B Q \sim \triangle A D C$. 那么 $A D \cdot A Q=A B \cdot A C$.

以 $A$ 为中心作 Iran 式反演, 则 $D$ 的像为 $Q$, 过 $A$ 的定圆的像为不过 $A$ 的一条直线. 结合引理 2 可知下面三个叙述相互等价:

(1) $D$ 在过 $A$ 的定圆上;

(2) $Q$ 在定直线上;

(3) $P$ 在 $\triangle A B C$ 的定外接雉线上.

故引理获证.

## II. 原问题的证明

我们先来证明如下的结果:

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-4.jpg?height=785&width=780&top_left_y=224&top_left_x=638)

图 4

结论 1 如图 5, 设 $E, F$ 为 $A C, A B$ 上的定点, $D$ 为一定点, $\odot B D F$ 和 $\odot C D E$再次交于点 $P . G$ 为 $\odot D E F$ 上一动点. $A G$ 与 $\odot G P D$ 再次交于点 $H, H P$ 与 $\odot B H C$ 再次交于点 $X$. 则 $X$ 在定直线上.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-4.jpg?height=626&width=702&top_left_y=1383&top_left_x=677)

图 5

证明 首先我们以 $P$ 为中心作反演变换, 为方便起见, 反演变换后点的字母仍保持不变.

我们现在只需要证明下面的命题:

如图 6, 若 $C, B$ 是 $D E, D F$ 上的两定点, $A$ 为一定点, $\odot E A C$ 和 $\odot B A F$ 再次交于点 $P, G$ 是 $\odot D E F$ 上一点, $D G$ 与 $\odot P A G$ 再次交于点 $H . H P$ 与 $\odot B C H$再次交于点 $X$, 则 $X$ 在一个 (广义) 圆周上.

对 $\triangle P A D$ 和点 $H$ 应用引理 3 , 知 $H$ 在一条 $\triangle P A D$ 的外接雉线上. 根据
条件, 显然有 $B, C$ 在这个轨迹上. 因此, $H$ 在一条过 $P, B, C$ 三点的雉线上. 对 $\triangle P B C$ 和 $H$ 点应用引理 3 , 知 $X$ 在定圆上.

命题获证.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-5.jpg?height=676&width=826&top_left_y=450&top_left_x=615)

图 6

可以看到, 这个结果某种程度上是命题 1 的推广, 为了得到命题 1 的证明,我们还需要做一些额外的工作, 这里的做法是取 $G$ 为一些特殊的点来确定 $X$ 所在的定直线. 以下我们回到命题 1 的图形.

首先, 取 $A, G, P, D$ 四点共圆, 则 $H=A, X=S$. 其次, 取 $A, G, D$ 三点共线, 则 $H=D \cdot \odot B H C$ 退化为直线 $B C, P D$ 与 $\odot B H C$ 的另一个交点为 $P D$ 方向上的无穷远点. 从而 $X$ 的轨迹为一条过 $S$ 点且平行于 $P D$ 的直线.

$G$ 点另外的取法有很多, 其中大部分对应的结果是非平凡的.

这样考虑问题稍显复杂, 但的确揭示了背景. 事实上同样有初等的做法, 而且并不是很复杂, 在这里略述思路.

设 $\odot P D G$ 与 $B C$ 再次交于点 $Y$, 过 $S$ 作 $P D$ 的平行线与 $B C$ 交于点 $U$, $P H$ 与 $B C$ 交于点 $V$, 则只需证明 $V B \cdot V C=V U \cdot V Y$, 这等价于 $[B, C ; V, Y]=$ $\frac{U B}{U C}$. 注意到 $[B, C ; V, Y]=[P B, P C ; P H, P Y]$, 以 $P$ 为中心, 任意半径反演, 导角可得

$$
\angle B P H=\angle A G E, \angle C P H=\angle A G F \text {. }
$$

从而有

$$
\begin{gathered}
\frac{\sin \angle C P H}{\sin \angle B P H}=\frac{\sin \angle F G A}{\sin \angle E G A}, \\
\frac{\sin \angle C P Y}{\sin \angle B P Y}=\frac{\sin \angle C P Y}{\sin \angle B D Y}=\frac{G E}{G F},
\end{gathered}
$$

$$
\frac{\sin \angle C P H / \sin \angle B P H}{\sin \angle C P Y / \sin \angle B P Y}=\frac{G F \cdot \sin \angle A G F}{G E \cdot \sin \angle A G E}=\frac{A F}{A E} .
$$

余下的工作是平凡的.

## III. 相关问题及其证明

下面的结果都来自林扬渊.

1. 已知 $D$ 为 $P$ 关于 $\triangle A B C$ 的垂足圆上一点, $A D$ 交 $\odot D P X$ 于另一点 $E$.求证: $\odot A P X$ 与 $P$ 关于 $\triangle E B C$ 的垂足圆的另一交点在 $A E$ 上, $P$ 关于 $\triangle A B C$的垂足圆与 $P$ 关于 $\triangle E B C$ 的垂足圆的另一交点在 $A E$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-6.jpg?height=594&width=776&top_left_y=888&top_left_x=640)

图 7

证明 我们通过以 $P$ 为中心反演来证明这个命题, 原问题等价于:

设 $P$ 在 $E F$ 上的垂足为 $A, G$ 是 $\odot D E F$ 上任意一点, $D G$ 与 $\odot P A G$ 再次交于点 $H$, 过 $H$ 作 $P H$ 的垂线与 $D E, D F$ 交于 $J, K$. 求证: $\odot P A G$ 和 $\odot D J K$ 的交点, 一个在 $\odot D E F$ 上, 一个在直线 $A D$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-6.jpg?height=602&width=705&top_left_y=1915&top_left_x=687)

图 8
延长 $J K$ 与 $E F$ 交于 $L$, 则 $P, A, G, L, H$ 五点共圆.

设完全四边形 $D J E F L K$ 的密克点为 $M, \odot D J K M$ 再次交 $A D$ 于 $N$.

由于 $\angle M L K=\angle M F K=\angle M G H$, 因此 $M, L, G, H$ 四点共圆. 即 $M$ 在 $\odot P A G$ 上. 由于 $\angle M N D=\angle M K D=\angle M L F$, 因此 $M, N, A, L$ 四点共圆.
2. $E, F$ 在 $A C, A B$ 上, $\odot B F P, \odot C E P$ 共点于 $D, G$ 为 $\odot D E F$ 上一点, $A G$交 $\odot D P G$ 于 $H, \odot B P H$ 交 $A B$ 于 $J, \odot C P H$ 交 $A C$ 于 $K$, 求证: $E F / / J K$. (原要求 $D$ 在 $B C$ 上, 但这不必要)

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-7.jpg?height=671&width=834&top_left_y=792&top_left_x=614)

图 9

证明 同样以 $P$ 为中心反演. 则只要证明: $\odot J P K$ 与 $\odot E P F$ 切于点 $P$. 将 $G$视为动点, 当 $D, P, G$ 共线时, $H=P, J=B, K=C$, 因此只需要证明, 当 $G$ 在 $\odot D E F$ 上运动时, $\triangle J P K$ 的外心始终在一条过 $P$ 点的定直线上. 根据引理 $5, H$点在一条过 $A, P, B, C$ 的二次曲线上.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-7.jpg?height=654&width=780&top_left_y=1912&top_left_x=638)

图 10
因此, 我们只需证明如下的命题:

若 $A, B, C, D$ 是平面上的定点. $P B$ 与 $\odot A B D$ 再次交于点 $J, P C$ 与 $\odot A C D$再次交于点 $K$. 设 $\triangle D J K$ 的外心为 $f(P)$ 则当 $P$ 在一条过 $A, B, C, D$ 的定二次曲线 $\gamma$ 上时, $f(P)$ 在一条过 $D$ 的定直线上.

当 $P=D$ 时, $f(P)=D$. 考虑 $X f(P)$, 事实上 $\angle(X f(P), B P)=90^{\circ}-$ $\angle B A D$ 为定值 $\theta$. 注意到同时有 $\angle(X Y, A B)=\theta$. 对于 $Y f(P)$ 同理. 既然如此,考虑 $\gamma$ 上另一点 $Q$, 有

$$
\begin{aligned}
{[X f(P), X f(Q) ; X Y, X D] } & =[B P, B Q ; B A, B D] \\
& =[C P, C Q ; C A, C D] \\
& =[Y f(P), Y f(Q) ; Y X, Y D]
\end{aligned}
$$

因此, $P, Q, D$ 三点共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_45e519570b53152ffc04g-8.jpg?height=576&width=854&top_left_y=1094&top_left_x=607)

图 11

## 参考文献

[1] 纯几何吧 http://tieba.baidu.com/p/5546393356

[2] 纯几何吧 http://tieba.baidu.com/p/5745139088

