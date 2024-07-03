# 一个几何问题的探究 

曾靖国

(法国路易大帝中学, arastelier@gmail.com)

本文源自笔者对一个几何问题的思考及探究过程. 文中运用有向角的工具获得问题完备条件, 充分体现了有向角在解决问题过程中的优越性. 现将笔者探究的过程整理成文供读者参考.

问题 如图 1, 已知 $T_{1}$ 为 $\triangle A B C$ 的外接圆, $G$ 为 $T_{1}$ 上异于 $A, B, C$ 的一点,过 $G$ 作 $A G$ 的垂线与直线 $B C$ 交于 $F$, 过 $A, G$ 作一圆 $T_{2}$, 圆心为 $O_{2}, T_{2}$ 交直线 $A B$ 于 $A, D$ 两点, 交直线 $A C$ 于 $A, E$ 两点. 那么 $O_{2}, D, E, F$ 四点在什么情况下共圆呢?

![](https://cdn.mathpix.com/cropped/2024_02_26_197660d1c81a7ee330c9g-1.jpg?height=548&width=596&top_left_y=1368&top_left_x=730)

图 1

由于当时笔者已经知道引理 1 、引理 2 的结论 (见下文), 因此先得出了当 $\triangle A B C$ 的垂心在 $T_{2}$ 上时, $O_{2}, D, E, F$ 四点共圆. 在使用几何画板后, 意外发现当 $O_{2}$ 在直线 $B C$ 上, 亦有 $O_{2}, D, E, F$ 四点共圆. 在近一步探索、引入有向角的工具后, 得出了 $O_{2}, D, E, F$ 四点共圆的充要条件.

定理 已知非直角 $\triangle A B C$ 的三边互不相等, $T_{1}$ 为 $\triangle A B C$ 的外接圆, $H$ 为 $\triangle A B C$ 的垂心, $G$ 为 $T_{1}$ 上一异于 $A, B, C$ 的一点, $G$ 不在直线 $A H$ 上, 过 $G$ 作

收稿日期: 2016-07-06; 修订日期:2016-07-27.
$A G$ 的垂线与直线 $B C$ 交于 $F$, 过 $A, G$ 作一圆 $T_{2}$, 圆心为 $O_{2}, T_{2}$ 交直线 $A B$ 于 $A, D$ 两点, 交直线 $A C$ 于 $A, E$ 两点. 则当且仅当 $O_{2}$ 在直线 $B C$ 上或 $H$ 在 $T_{2}$上时, $O_{2}, D, E, F$ 四点共圆.

其中 “非直角” ，“三边不相等” 等条件的添加, 是为避免讨论一些退化情形. 以下将给出上述定理的证明.

证明过程中 $\measuredangle$ 代表有向角, $\measuredangle\left(l_{1}, l_{2}\right)$ 代表直线 $l_{1}$ 以顺时针旋转至和 $l_{2}$ 重合所需经过的角度, 角度是以 $180^{\circ}$ 为循环, 即 $\theta \equiv 180^{\circ}+\theta$. 当为 $\measuredangle(A B, B C)$ 的情形时, 将简写为 $\measuredangle A B C$.

证明 为证明上述定理, 需首先证明下面三个引理.

引理 1 在 $\triangle A B C$ 中, 点 $D, E$ 分别在直线 $A B, A C$ 上, $F, G$ 分别为线段 $B D, C E$ 中点. 则 $\triangle A D E, \triangle A F G, \triangle A B C$ 的外接圆三圆共轴.

证明 如图 2, 令 $O_{1}, O_{3}$ 分别为 $\triangle A B C, \triangle A D E$ 的外心, $O_{2}$ 为 $O_{1} O_{3}$ 中点, $M, N$ 分别为 $O_{3} B, O_{3} C$ 的中点. 因为 $M O_{2}=O_{2} N, F M=N G$, 且 $\measuredangle O_{2} M F=$ $\measuredangle\left(B O_{1}, O_{3} D\right)=\measuredangle\left(O_{1} C, O_{3} E\right)=\measuredangle O_{2} N G$, 所以 $\triangle F M O_{2} \equiv \triangle G N O_{2}$. 因此 $O_{2} F=O_{2} G$, 又 $\measuredangle F O_{2} G=\measuredangle M O_{2} N=\measuredangle B O_{1} C$, 故 $O_{2}$ 为 $\triangle A F G$ 外心. 故 $\triangle A D E, \triangle A F G, \triangle A B C$ 的外接圆三圆共轴.

![](https://cdn.mathpix.com/cropped/2024_02_26_197660d1c81a7ee330c9g-2.jpg?height=642&width=671&top_left_y=1461&top_left_x=698)

图 2

【注】从证明过程可看出, 只要满足 $\frac{B F}{F D}=\frac{C G}{G E}$, 亦有 $\triangle A D E, \triangle A F G, \triangle A B C$的外接圆三圆共轴.

引理 2 设非直角 $\triangle A B C$ 垂心为 $H$, 圆 $T_{1}$ 过点 $A$ 分别交直线 $A B$ 于 $A, D$两点, 交直线 $A C$ 于 $A, E$ 两点. 记 $G$ 为 $B D$ 中垂线和 $C E$ 中垂线的交点. 则 $H$在圆 $T_{1}$ 上 $\Leftrightarrow G$ 在直线 $B C$ 上.
证明 如图 3, $D, E, F$ 点分别在 $A B, A C, B C$ 上, $P$ 为其密克点. 令 $G$ 为 $\triangle D E F$ 的外接圆和直线 $B C$ 的第二个交点 (若 $\triangle D E F$ 的外接圆和直线 $B C$ 相切, 取 $G=F)$. 则

$P$ 是 $\triangle A B C$ 垂心

$$
\begin{aligned}
& \Leftrightarrow \measuredangle B P C+\measuredangle B A C=\measuredangle C P A+\measuredangle C B A=\measuredangle A P B+\measuredangle A C B=180^{\circ} \\
& \Leftrightarrow \measuredangle P A C+\measuredangle C B P=180^{\circ}-2 \measuredangle A C B \text { 且 } \measuredangle B A P+\measuredangle P C B=180^{\circ}-2 \measuredangle C B A \\
& \Leftrightarrow \measuredangle F D E=180^{\circ}-2 \measuredangle A C B \text { 且 } \measuredangle D E F=180^{\circ}-2 \measuredangle C B A \\
& \Leftrightarrow \measuredangle F G E=180^{\circ}-2 \measuredangle A C B \text { 且 } \measuredangle D G F=180^{\circ}-2 \measuredangle C B A \\
& \Leftrightarrow B D \text { 中垂线和 } C E \text { 中垂线之交点在直线 } B C \text { 上. }
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_197660d1c81a7ee330c9g-3.jpg?height=640&width=788&top_left_y=888&top_left_x=637)

图 3

【注】引理 2 即为 2012 美国队选拔测试第一题, 类似的结论整理如下:

(1) $\triangle A B C$ 外心为 $O$, 圆 $T_{1}$ 过点 $A$ 交直线 $A B$ 于 $A, D$ 两点, 交直线 $A C$ 于 $A, E$ 两点. 则 $O$ 在 $T_{1}$ 上 $\Leftrightarrow$ 直线 $B C$ 上存在 $G$ 点, 使得 $D G=D B, E G=E C$.

(2) $\triangle A B C$ 内心为 $I$, 圆 $T_{1}$ 过点 $A$ 交直线 $A B$ 于 $A, D$ 两点, 交直线 $A C$ 于 $A, E$ 两点. 则 $I$ 在 $T_{1}$ 上 $\Leftrightarrow$ 直线 $B C$ 上存在 $G$ 点, 使得 $B G=D B, C G=E C$.

引理 3 设 $\triangle A B C$ 外心为 $O_{1}, D, E$ 两点分别在直线 $A B, A C$ 上, 过 $D$ 点作平行于 $B O_{1}$ 的直线 $l_{1}$, 过 $E$ 点作平行于 $C O_{1}$ 的直线 $l_{2}$. 记 $F$ 为 $l_{1}, l_{2}$ 的交点, $\triangle A D E$ 的外心为 $O_{2}$. 则 $F$ 在直线 $B C$ 上 $\Leftrightarrow O_{2}$ 在直线 $B C$ 上.

证明 因为 $\measuredangle D F E=\measuredangle B O_{1} C=2 \measuredangle B A C=\measuredangle D O_{2} E$, 所以 $O_{2}, D, E, F$ 四点共圆, 推得 $\measuredangle O_{2} F D=\measuredangle O_{2} E D=\measuredangle E D O_{2}=\measuredangle E F O_{2}$.

若 $F$ 在直线 $B C$ 上, 由 $B O_{1} / / D F$, 得 $\measuredangle B F D=\measuredangle C B O_{1}$, 同理可得 $\measuredangle O_{1} C F=\measuredangle E F C$. 因此 $\measuredangle B F D=\measuredangle E F C$, 推得 $O_{2}$ 在直线 $B C$ 上.
若 $O_{2}$ 在直线 $B C$ 上, 令直线 $l_{1}, B C$ 交于点 $F^{\prime}$, 因 $\measuredangle O_{2} F^{\prime} D=\measuredangle B F^{\prime} D=$ $\measuredangle C B O_{1}=\measuredangle E D O_{2}=\measuredangle O_{2} E D$, 所以 $O_{2}, D, E, F^{\prime}$ 四点共圆. 此时 $\measuredangle E F^{\prime} C=$ $\measuredangle E D O_{2}=\measuredangle O_{1} C B$, 于是 $E F^{\prime}$ 和 $C O_{1}$ 平行, 故 $F^{\prime}$ 与 $F$ 重合.

![](https://cdn.mathpix.com/cropped/2024_02_26_197660d1c81a7ee330c9g-4.jpg?height=534&width=594&top_left_y=435&top_left_x=731)

图 4

回到原题. 令 $O_{1}$ 为 $\triangle A B C$ 外心. 在直线 $A B$ 上取一点 $R$, 使得 $\measuredangle F D R=$ $\measuredangle D R F$, 直线 $F R, A C$ 交于点 $I . J$ 为 $D R$ 中点, $K$ 为 $I E$ 中点, 其余记号同原题.

注意到 $O_{2}, D, E, F$ 四点共圆

$$
\begin{aligned}
& \Leftrightarrow \measuredangle D O_{2} E=\measuredangle D F E=2 \measuredangle D A E \\
& \Leftrightarrow \measuredangle F I E=\measuredangle D A E-\measuredangle D R F=\measuredangle D A E-\measuredangle F D R \\
& =\measuredangle D F E-\measuredangle D A E-\measuredangle F D R=\measuredangle I E F
\end{aligned}
$$

$\Leftrightarrow F J \perp A D$ 且 $F K \perp E I \Leftrightarrow A, J, F, K, G$ 五点共圆.

由引理 1 知, $A, J, F, K, G$ 五点共圆 $\Leftrightarrow A, I, G, R$ 四点共圆 $\Leftrightarrow \measuredangle G C F=$ $\measuredangle G A R=\measuredangle G I R=\measuredangle G I F \Leftrightarrow I$ 和 $C$ 重合与 $F, I, G, C$ 四点共圆至少有一成立.

![](https://cdn.mathpix.com/cropped/2024_02_26_197660d1c81a7ee330c9g-4.jpg?height=651&width=600&top_left_y=1785&top_left_x=728)

图 5

以下分两种情形讨论:
情形 1. $I$ 和 $C$ 重合时, $R$ 也和 $B$ 重合, 此时 $F C=F E$ 且 $F D=F B$, 由引理 2 知 $I$ 和 $C$ 重合 $\Leftrightarrow H$ 在圆 $T_{2}$.

情形 2. $F, I, G, C$ 四点共圆时,

$\measuredangle O_{1} B A=90^{\circ}-\measuredangle A C B=90^{\circ}-\measuredangle I G F=\measuredangle A G I=\measuredangle A R I=\measuredangle F D A$.

同理 $\measuredangle A C O_{1}=\measuredangle A E F$. 所以 $F, I, G, C$ 四点共圆 $\Leftrightarrow D F / / B O_{1}$ 且 $E F / / C O_{1}$,于是 $F, I, G, C$ 四点共圆 $\Leftrightarrow O_{2}$ 在直线 $B C$ 上.

最后, 给出一个引理 1 在其他题目上的应用.

习题 设 $O_{1}, H$ 分别为 $\triangle A B C$ 的外心和垂心, $M$ 为 $B C$ 中点. $A B, A C$ 直线上分别取点 $D, E$, 使得 $D, H, E$ 共线且 $A D=A E$. 记 $O_{2}$ 为 $\triangle A D E$ 的外心.证明: $O_{1} O_{2}$ 平行 $M H$.

证明 令 $B H, C H$ 分别交 $A C, A B$ 于 $G, F$. 由 $A D=A E$, 知 $\angle H D A=$ $H E A$. 由垂心定义, 得 $\angle H B A=\angle H C A$, 故 $\frac{F D}{D B}=\frac{G E}{E C}$. 由引理 1 知 $\triangle A D E$, $\triangle A F G, \triangle A B C$ 的外接圆三圆共轴. 令此三圆交于 $A, K$. 因为 $\angle H F A=90^{\circ}=$ $\angle H G A$, 所以 $H$ 在 $\triangle A F G$ 的外接圆上. 因此 $\angle A K H=A G H=90^{\circ}$, 故 $K$ 在 $M H$ 直线上. 由 $M H \perp A K, O_{1} O_{2} \perp A K$, 得 $O_{1} O_{2} / / M H$.

![](https://cdn.mathpix.com/cropped/2024_02_26_197660d1c81a7ee330c9g-5.jpg?height=640&width=669&top_left_y=1459&top_left_x=702)

图 6

