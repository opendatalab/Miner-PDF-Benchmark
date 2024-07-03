# 对一道 IMO 预选题的探究 

$$
\text { 卢圣 }
$$

(广西钦州市新兴街 30 号祥和景都 2 栋 2 单元, 535000)

第 52 届 IMO 预选题中有如下一道平面几何题:

如图 1, $\triangle A B C$ 中, $G$ 为重心, $E, F$ 为 $C A, A B$ 的中点, 圆 $\Gamma$ 过 $E, F$ 且与 $\triangle A B C$ 外接圆切于点 $T$ (异于 $A$ ), $A D \perp B C$ 于 $D$. 证明: $T, D, G$ 三点共线.



图 1

该题条件中的圆 $\Gamma$ 过三角形两边的中点且与外接圆相切, 结构新颖、饶有趣味. 笔者通过对该题的研究, 得到圆 $\Gamma$ 的一些基本性质, 并得到该圆与三角形垂心的等截共轭点的等角共轭点与欧拉线相关的性质. 现将有关结论整理成文,供读者参考.

注 1 如图 2, $P, Q$ 两点满足

$$
\angle B A P=\angle Q A C, \angle P B A=\angle C B Q, \angle B C P=\angle Q C A \text {, }
$$

则称 $P, Q$ 为关于 $\triangle A B C$ 的等角共轭点.

注 2 如图 3, 过 $\triangle A B C$ 的顶点作交于 $P$ 的三条直线分别交对边于 $D, E, F$, $X, Y, Z$ 为 $D, E, F$ 关于 $B C, C A, A B$ 中点的对称点, 则 $A X, B Y, C Z$ 三点共线, 设该点为 $Q$, 则称 $P, Q$ 关于 $\triangle A B C$ 的等截共轭点.

收稿日期: 2018-07-22.



图 2



图 3

为便于进一步的探索, 先看文献 [1] 对该题的证明.

证明 若 $A B=A C$, 则题中图形关于直线 $A D$ 对称, 结论是显然的.

若 $A B \neq A C$, 如图 4, 设 $O$ 为 $\triangle A B C$ 的外心, $M$ 为 $B C$ 中点, 延长 $M O$ 与 $E F$ 交于 $J$. 由重心性质知 $\triangle A B C$ 与 $\triangle M E F$ 位似, $G$ 为位似中心.



图 4

易知 $E F / / B C, O M \perp B C$, 所以 $M J \perp E F$ 于 $J$.

所以 $D, J$ 为 $\triangle A B C$ 与 $\triangle M E F$ 的位似对应点, 所以 $D, G, J$ 共线. 易知 $\triangle A F E$ 与 $\triangle A B C$ 位似, $A$ 为位似中心, 所以 $\triangle A F E$ 与 $\triangle A B C$ 的外接圆相切于 $A$.

由根心定理知过 $A, T$ 作 $\triangle A B C$ 外接圆的切线与 $E F$ 共点, 设为 $P$. 所以 $A, P, T, O, J$ 五点共圆于 $O P$ 为直径的圆. 易知 $E F$ 垂直平分 $A D$. 所以 $\angle P J D=\angle P J A=\angle P T A=\angle P A T=\angle P J T$. 故 $J, D, T$ 三点共线, 所以 $J, G, D, T$ 共线.

至此题目证明完成, 但是还有一些疑问. 题设中的圆 $\Gamma$ 在一般的三角形中都存在吗? 还是命题人仅仅在特殊的三角形中画出的特殊图形而已? 因此, 在进一步探索之前首先需要解决题设中圆 $\Gamma$ 存在性的问题. 对于上述疑问, 答案是肯定的.

下面证明一般的三角形中题设中的圆 $\Gamma$ 一定存在. 证明仍旧参照图 4 , 但是
条件表述作出下列调整:

如图 4, $\triangle A B C$ 三边互不相等, $E, F$ 分别为 $C A, A B$ 的中点, 过 $A$ 作 $\triangle A B C$外接圆的切线与直线 $E F$ 交于 $P$, 过 $P$ 作 $\triangle A B C$ 外接圆的另一条切线, 切点为 $T$, 则 $\triangle T E F$ 的外接圆与 $\triangle A B C$ 外接圆相切于点 $T$.

证明 易知 $E F$ 为边 $B C$ 所对的中位线,所以 $\triangle A B C$ 与 $\triangle A F E$ 位似,且 $A$ 为位似中心, 所以 $\triangle A B C$ 及 $\triangle A F E$ 的外接圆相切于点 $A$, 所以 $P A$ 为 $\triangle A E F$ 的外接圆的切线, 故有 $P T^{2}=P A^{2}=P E \cdot P F$, 即 $\frac{P T}{P E}=\frac{P F}{P T}$. 所以有 $\triangle P E T \sim \triangle P T F$, 故 $\angle P T F=\angle P E T$.

因此 $P T$ 与 $\triangle T E F$ 的外接圆相切, 即 $P T$ 为 $\triangle A B C$ 及 $\triangle T E F$ 的外接圆的公切线. 所以 $\triangle A B C$ 及 $\triangle T E F$ 的外接圆相切.

上述证明肯定地回答了题设中圆 $\Gamma$ 存在性, 也给出了具体的作图方法. 下面开始探索圆 $\Gamma$ 的具体性质. 先约定, 下文讨论的 $\triangle A B C$ 三边互不相等, 文中将不再一一指出.

性质 1 如图 5, $\triangle A B C$ 中, $G$ 为重心, $E, F$ 为 $C A, A B$ 的中点, 圆 $\Gamma$ 过 $E, F$且与 $\triangle A B C$ 外接圆切于点 $T$ (异于 $A$ ), $A D \perp B C$ 于 $D$, 过 $A$ 作 $B C$ 的平行线与 $\triangle A B C$ 外接圆交于 $L$, 则 $T, D, G, L$ 四点共线.



图 5

证明 如图 5, 设 $B C$ 中点为 $M, L K \perp B C$ 于 $K$. 易知四边形 $A B C L$ 为等腰梯形, 四边形 $A D K L$ 为矩形. 所以 $B D=C K$. 故 $M$ 为 $D K$ 中点, 所以有 $\frac{D M}{L A}=\frac{M G}{A G}=\frac{1}{2}$.

从而 $\triangle G D M$ 与 $\triangle G L A$ 位似, $G$ 为位似中心, 所以 $D, G, L$ 共线. 由 $T, D, G$共线, 所以 $T, D, G, L$ 四点共线.

性质 2 如图 6, $\triangle A B C$ 中, $E, F$ 为 $C A, A B$ 的中点, 圆 $\Gamma$ 过 $E, F$ 且与 $\triangle A B C$ 外接圆切于点 $T$ (异于 $A$ ), 则 $A T$ 关于 $\triangle A B C$ 外接圆的极点在 $\triangle A B C$外接圆与九点圆的根轴上.



图 6

证明 如图 6, 易知 $\triangle A F E$ 与 $\triangle A B C$ 位似, $A$ 为位似中心. 所以 $\triangle A F E$ 与 $\triangle A B C$ 的外接圆相切与 $A$.

由根心定理知过 $A, T$ 作 $\triangle A B C$ 外接圆的切线与 $E F$ 共点, 设为 $P$, 故 $P$ 为 $A T$ 关于 $\triangle A B C$ 外接圆的极点. 易知 $P T^{2}=P A^{2}=P E \cdot P F$. 所以 $P$ 对 $\triangle A B C$外接圆及九点圆的幂相等. 所以 $P$ 在 $\triangle A B C$ 外接圆与九点圆的根轴上.

性质 3 如图 7, $\triangle A B C$ 中, $E, F$ 为 $C A, A B$ 的中点, 圆 $\Gamma$ 过 $E, F$ 且与 $\triangle A B C$ 外接圆切于 $T$ (异于 $A$ ) , $A D \perp B C$ 于 $D$, 则

$$
\frac{T B}{T C}=\frac{A B \cdot B D}{A C \cdot C D}
$$



图 7

证明 如图 7, 过 $A$ 作 $B C$ 的平行线与 $\triangle A B C$ 外接圆交于 $L$, 易知 $A B=L C$.

由性质 1 知 $T, D, L$ 共线, 所以 $\angle D T C=\angle L T C=\angle B T A$. 故 $\triangle A B T \sim$ $\triangle C D T$. 从而

$$
\frac{T C}{T A}=\frac{C D}{A B}
$$

由 $\angle A T C=\angle A B C=\angle B C L=\angle B T L=\angle B T D$, 所以 $\triangle T A C \sim \triangle T B D$.从而有

$$
\frac{T B}{T A}=\frac{B D}{A C}
$$

由 (1), (2) 式得

$$
\frac{T B}{T C}=\frac{A B \cdot B D}{A C \cdot C D} .
$$

证毕!

性质 4 如图 8, 在 $\triangle A B C$ 中, $E, F$ 为 $C A, C B$ 的中点, 圆 $\Gamma$ 过 $E, F$ 且与 $\triangle A B C$ 的外接圆切于 $T$ (并于 $A$ ), $A D \perp B C$ 于 $D, K$ 在 $B C$ 上且 $B D=C K$, 则 $A T, A K$ 为 $\angle B A C$ 的一对等角线.



图 8

证明 如图 8, 设 $B C$ 中点为 $M, M$ 在 $E F$ 射影为 $J$, 过 $A$ 作 $B C$ 的平行线与 $\triangle A B C$ 外接圆交于 $L$.

由前述证明知 $T, D, J, L$ 共线且 $\triangle M E F$ 与 $\triangle A B C$ 位似. 所以 $J, D$ 为 $\triangle M E F$ 与 $\triangle A B C$ 的位似对应点, 所以

$$
\frac{E J}{J F}=\frac{B D}{D C}=\frac{C K}{K B} .
$$

易知 $\triangle A F E$ 与 $\triangle A B C$ 位似, $A$ 为位似中心, 所以 $J, K$ 为 $\triangle A F E$ 与 $\triangle A B C$ 的位似对应点. 故 $A, J, K$ 共线且 $J$ 为 $A K$ 中点, 所以 $\angle J D C=\angle J K B=\angle A J F$.因此

$$
\angle C D T=180^{\circ}-\angle J D C=180^{\circ}-\angle A J F=\angle A J E .
$$

由性质 1 知 $\angle D T C=\angle L T C=\angle B C A=\angle J E A$, 所以 $\triangle T C D \sim \triangle E A J$, 所以

$$
\angle B A T=\angle B C T=\angle D C T=\angle J A E=\angle K A C .
$$

所以 $A T, A K$ 为 $\angle B A C$ 的一对等角线.

性质 5 如图 9, 在 $\triangle A B C$ 中, $E, F$ 为 $C A, A B$ 的中点, 圆 $\Gamma$ 过 $E, F$ 且与 $\triangle A B C$ 外接圆切于点 $T$ (异于 $A$ ), 则

$$
\frac{T B \cdot T C}{T A^{2}}=|\cos B \cos C| .
$$



图 9

证明 在此仅证明锐角三角形的情形. 针角三角形的情形完全类似.

如图 9, 作 $A D \perp B C$ 于 $D$, 过 $A$ 作 $B C$ 的平行线交 $\triangle A B C$ 外接圆于 $L$, 作 $L K \perp B C$ 于 $K$. 由前述证明知 $T, D, L$ 共线, 四边形 $A D K L$ 为矩形, $B D=C K$.所以 $A K=D L$.

由性质 4 知 $\angle B A T=\angle K A C$. 所以 $\triangle B A T \sim \triangle K A C$, 故

$$
\frac{B A}{T A}=\frac{A K}{A C}=\frac{D L}{A C}, A B \cdot A C=A T \cdot D L
$$

由性质 3 知 $\triangle A B T \sim \triangle C D T$, 有 $\frac{T C}{T A}=\frac{T D}{T B}$, 则

$$
T B \cdot T C=T D \cdot T A
$$

由 (1), (2) 两式得

$$
A B \cdot A C \cdot T B \cdot T C=T A^{2} \cdot T D \cdot D L=T A^{2} \cdot B D \cdot D C
$$

所以

$$
\frac{T B \cdot T C}{T A^{2}}=\frac{B D \cdot D C}{A B \cdot A C}=\cos B \cos C
$$

性质 6 如图 10, $\triangle A B C$ 中, $M, E, F$ 为 $B C, C A, A B$ 的中点, 圆 $\Gamma_{2}$ 过 $M, F$且与 $\triangle A B C$ 外接圆切于点 $Y$ (异于 $B$ ), 圆 $\Gamma_{3}$ 过 $M, E$ 且与 $\triangle A B C$ 外接圆切于点 $Z$ (异于 $C$ ), $B P, C Q$ 为 $C A, A B$ 所对的高, 则 $Y, P, Q, Z$ 四点共圆.



图 10
证明 如图 10, 设 $A B C$ 的重心为 $G$, 过 $B$ 作 $A C$ 的平行线, 过 $C$ 作 $A B$ 的平行线分别与 $\triangle A B C$ 外接圆交于 $U, V$.

由性质 1 知 $U, G, P, Y$ 及 $V, G, Q, Z$ 分别四点共线, 且 $U G=2 P G, V G=$ $2 Q G$. 易知 $G Y \cdot G U=G Z \cdot G V$. 所以

$$
G P \cdot G Y=\frac{1}{2} G Y \cdot G U=\frac{1}{2} G Z \cdot G V=G Q \cdot G Z
$$

所以 $Y, P, Q, Z$ 四点共圆.

推论 $Y Z, P Q, B C$ 三线共点.

证明 易知 $B, C, P, Q$ 四点共圆. 由根心定理知 $Y Z, P Q, B C$ 三线共点.

性质 7 如图 11, $\triangle A B C$ 中, $H$ 为垂心, $M, E, F$ 为 $B C, C A, A B$ 的中点, 圆 $\Gamma_{1}$ 过 $E, F$ 且与 $\triangle A B C$ 外接圆切于点 $T$ (异于 $A$ ), 圆 $\Gamma_{2}$ 过 $M, F$ 且与 $A B C$ 外接圆切于点 $Y$ (异于 $B$ ), 圆 $\Gamma_{3}$ 过 $M, E$ 且与 $\triangle A B C$ 外接圆切于点 $Z$ (异于 $C$ ),则 $A T, B Y, C Z$ 三线共点, 该点为 $H$ 的等截共轭点的等角共轮点, 且为外接圆与九点圆的根轴关于外接圆的极点.



图 11

证明 如图 11, 由性质 2 知 $A T$ 过 $\triangle A B C$ 外接圆与九点圆的根轴关于 $\triangle A B C$ 外接圆的极点, 设为点 $S$. 同理, $B Y, C Z$ 也过点 $S$. 由于 $\triangle A B C$ 外接圆与九点圆的根轴垂直于 $\triangle A B C$ 的欧拉线. 所以点 $S$ 在 $\triangle A B C$ 欧拉线上.

下面证明 $S$ 为 $H$ 的等截共轭点的等角共轭点. 设 $A H$ 与 $B C$ 交于 $D, K$ 在 $B C$ 上且 $B D=C K$.

由性质 4 知 $A T, A K$ 为 $\triangle B A C$ 的一对等角线. 所以 $A T$ 经过 $H$ 的等截共轭点的等角共轭点. 同理, $B Y, C Z$ 也过 $H$ 的等截共轭点的等角共轭点. 所以 $S$为 $H$ 的等截共轭点的等角共轭点.

事实上, 性质 7 可以表述为: 三角形的垂心的等截共轭点的等角共轭点在欧拉线上, 且该点为外接圆与九点圆的根轴关于外接圆的极点.

