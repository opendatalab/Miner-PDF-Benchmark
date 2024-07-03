# 一个内心关联巧合点难题 

$$
\text { 严君啸 }
$$

(浙江省镇海中学, 315000)

通过几何画板,笔者发现了这样一个问题:

问题 如图 1 所示, 在 $\triangle A B C$ 中, $I$ 为内心, $H_{1}$ 为以三条角平分线与对边交点为顶点的三角形的垂心, $H_{2}$ 为内切圆切点三角形的垂心, $A H_{2}$ 与外接圆交于另一点 $D_{0}, H_{2}$ 关于 $B C$ 边对称点为 $H_{2}^{\prime}, H_{2}^{\prime} D_{0}$ 与外接圆交于另一点 $E_{0}$, 则 $A E_{0} \perp I H_{1}$.



图 1

然而, 这个问题的证明非常困难. 笔者根据自己的思考并结合相关资料, 在本文中给出此题的几何证法.

为方便描述, 先约定下列字母标记的几何意义, 在后续行文中不再反复说明, 请读者详察.

如图 2 所示, 在 $\triangle A B C$ 中, $I, O$ 分别为内心, 外心, $I_{a}, I_{b}, I_{c}$ 分别为 $I$ 关于 $B C, C A, A B$ 的对称点, $X, Y, Z$ 分别为 $A, B, C$ 引出的角平分线与对边交点, $I_{1}, I_{2}, I_{3}$ 分别为 $A$-旁心, $B$-旁心, $C$-旁心, $H_{a}, H_{b}, H_{c}$ 分别为 $A, B, C$ 在收稿日期: 2019-02-14.

$$
{ }^{\bullet} I_{3}
$$



${ }^{\bullet} \boldsymbol{I}_{1}$

图 2

对边上的射影, $D, E, F$ 分别为内切圆与 $B C, C A, A B$ 的切点, 原题中出现的字母意义与原题相同.

文中其它的字母标记以文中当处说明为准.

## I. 预备知识

引理 $1.1^{[1]} A I_{a}, B I_{b}, C I_{c}$ 交于一点 $P(P$ 在后续行文中的意义不再改变).



图 3

证明 如图 3 所示, 设 $A I_{a}$ 与 $\odot\left(B I_{a} C\right)$ 交于另一点 $I_{a}^{\prime}$. 类似地定义 $I_{b}^{\prime}, I_{c}^{\prime}$. 则

$$
\angle C I_{b}^{\prime} I_{b}=\angle C A I_{b}=\angle C A I=\angle B A I=\angle B A I_{c}=\angle B I_{c}^{\prime} I_{c},
$$

故 $B, I_{b}^{\prime}, C, I_{c}^{\prime}$ 四点共圆.

类似地, $A, I_{a}^{\prime}, B, I_{b}^{\prime}$ 四点共圆, $C, I_{c}^{\prime}, A, I_{a}^{\prime}$ 四点共圆. 则 $A I_{a}, B I_{b}, C I_{c}$ 共点于 $\odot\left(B I_{b}^{\prime} C I_{c}^{\prime}\right), \odot\left(A I_{a}^{\prime} B I_{b}^{\prime}\right), \odot\left(C I_{c}^{\prime} A I_{a}^{\prime}\right)$ 的根心 $P$.
引理 1.2 ${ }^{[1]} \triangle X Y Z$ 和 $\triangle A B C$ 透视. 其透视轴称为 $\triangle A B C$ 的反垂足轴.

引理 $1.3^{[1]}$ 设 $R=H_{b} H_{c} \cap B C, S=H_{c} H_{a} \cap C A, T=H_{a} H_{b} \cap A B$. 则 $R, S, T$三点共线. 此线称为 $\triangle A B C$ 的垂足轴, 其是 $\triangle A B C$ 九点圆与外接圆的根轴, 而垂直于 $\triangle A B C$ 的欧拉线.

引理 $1.4^{[2]}$ 三个共透视中心的三角形两两透视轴三线共点.

引理 1.5 ${ }^{[3]}$ 若 $\triangle A B C$ 和 $\triangle A_{1} B_{1} C_{1}$ 满足: $A$ 关于 $B_{1} C_{1}$ 的垂线, $B$ 关于 $C_{1} A_{1}$的垂线, $C$ 关于 $A_{1} B_{1}$ 的垂线三线共点, 则称 $\triangle A B C$ 和 $\triangle A_{1} B_{1} C_{1}$ 正交, 所共点 $Q$ 称为 $\triangle A B C$ 关于 $\triangle A_{1} B_{1} C_{1}$ 的正交中心. 若 $\triangle A B C$ 和 $\triangle A_{1} B_{1} C_{1}$ 正交,则 $A_{1}$ 关于 $B C$ 的垂线, $B_{1}$ 关于 $C A$ 的垂线, $C_{1}$ 关于 $A B$ 的垂线三线亦共点, 所共点 $Q_{1}$ 即为 $\triangle A_{1} B_{1} C_{1}$ 关于 $\triangle A B C$ 的正交中心.

引理 1.6 ${ }^{[3]}$ (P. Sondat 定理) 两个透视且正交的 $\triangle A B C, \triangle A_{1} B_{1} C_{1}$, 透视轴为 $d$, 透视中心为 $T, \triangle A B C$ 关于 $\triangle A_{1} B_{1} C_{1}$ 的正交中心为 $Q, \triangle A_{1} B_{1} C_{1}$ 关于 $\triangle A B C$ 的正交中心为 $Q_{1}$, 则 $T, Q, Q_{1}$ 在同一条垂直于 $d$ 的直线上.

引理 $1.7^{[4]} \triangle I B C, \triangle I C A, \triangle I A B$ 和 $\triangle A B C$ 的四条欧拉线共点. 该点称为 $\triangle A B C$ 的Schiffler 点.

引理 1.8 ${ }^{[5]}$ 设 $O_{1}, O_{2}, O_{3}$ 分别为 $\triangle O B C, \triangle O C A, \triangle O A B$ 的外心,则 $A O_{1}, B O_{2}, C O_{3}$ 共点 $K$. 该点称为 $\triangle A B C$ 的 Kosnita 点, 其是 $\triangle A B C$ 九点圆心的等角共轭点.

## II. 证明 $I H_{1}$ 平行于 $\triangle A B C$ 的欧拉线

引理 $2.1 I$ 在 $P H_{1}$ 上.



图 4
证明 如图 4 所示, 设

$$
\begin{array}{r}
Q=Y H_{1} \cap Z X, R=X H_{1} \cap Y Z, S=A X \cap Y Z, \\
T=Y Z \cap B C, U=A I_{a} \cap B C, V=B I_{b} \cap C A .
\end{array}
$$

由于 $U A, U S, U I, U X$ 构成调和线束, $\angle I U X=\angle I_{a} U X$, 故 $U S \perp U X$, 即 $U S \perp B C$. 显然由调和点列, $T$ 为 $\angle B A C$ 外角平分线与 $B C$ 交点, 故 $A T \perp A I$.故 $A, S, U, T$ 四点共圆. 又注意到 $A, R, X, T$ 四点共圆, $R, S, U, X$ 四点共圆, 故

$$
\angle I U S=\angle A U S=\angle A T S=\angle A X R=\angle R U S .
$$

因此 $I$ 在 $U R$ 上. 对 $\triangle A B U$ 和 $\triangle X Y R$ 运用 Desargue 定理, 有 $X R$ 与 $A P$ 的交点在 $\triangle A B C$ 的反垂足轴上. 同理, $Y Q$ 与 $B P$ 的交点也在 $\triangle A B C$ 的反垂足轴上. 故对 $\triangle A B P$ 和 $\triangle X Y H_{1}$ 运用 Desargue 定理的逆定理, $I$ 在 $P H_{1}$ 上.

引理 2.2 设 $\{J\}=H_{c} H_{a} \cap C A,\{K\}=H_{a} H_{b} \cap A B, T$ 是 $\angle H_{a} J C$ 和 $\angle H_{a} K B$两条内角平分线交点,则 $A, T, I_{a}$ 三点共线.



图 5

证明 如图 5 所示, 设 $L=A I_{a} \cap B C, U, V$ 分别为 $Y$ 在 $A B, B C$ 上的射影, $R, S$ 分别为 $Z$ 在 $B C, C A$ 上的射影. 由于

$$
\frac{A U}{H_{c} U}=\frac{A Y}{C Y}=\frac{A B}{C B}=\frac{A H_{a}}{C H_{c}}=\frac{A J}{H_{c} J}
$$

故 $J U$ 是 $\angle H_{a} J C$ 的内角平分线, 故 $J, T, U$ 共线. 同理, $V$ 在 $J T$ 上, $R, S$ 在 $K T$ 上. 设

$$
T_{1}=A I_{a} \cap U V, T_{2}=A I_{a} \cap R S, W=A I \cap Y Z
$$

对 $\triangle A B L$ 和截线 $V T_{1} U$ 运用 Menelaus 定理, 注意到 $B V=B U$, 我们有

$$
\frac{A T_{1}}{L T_{1}}=\frac{A U}{L V}
$$

同理,

$$
\frac{A T_{2}}{L T_{2}}=\frac{A S}{L R}
$$

又由 $L A, L I, L W, B C$ 构成调和线束且 $B C$ 平分 $\angle I L I_{a}$, 可得 $W L \perp B C$.故

$$
\frac{L V}{L R}=\frac{W Y}{W Z}=\frac{A Y}{A Z}=\frac{A U}{A S}
$$

结合 (1), (2) 可得, $T_{1}=T_{2}=T$. 故 $A, T, I_{a}$ 三点共线.

引理 $2.3 I P$ 平行于 $\triangle A B C$ 的欧拉线.



图 6

证明 如图 6 所示, 设

$$
J=H_{c} H_{a} \cap C A, K=H_{a} H_{b} \cap A B, L=H_{b} H_{c} \cap B C,
$$

$X_{1}$ 是 $\angle H_{a} J C$ 和 $\angle H_{a} K B$ 两条内角平分线交点. 类似地定义 $Y_{1}, Z_{1}$.

由引理 2.2, $X_{1}$ 在 $A I_{a}$ 上, $Y_{1}$ 在 $B I_{b}$ 上, $Z_{1}$ 在 $C I_{c}$ 上. 故由引理 1.4, $\triangle A B C, \triangle I_{a} I_{b} I_{c}, \triangle X_{1} Y_{1} Z_{1}$ 两两透视轴三线共点. 导角易得 $A I \perp I_{b} I_{c}, A I \perp$ $Y_{1} Z_{1}$. 故 $I_{b} I_{c} / / Y_{1} Z_{1}$. 同理,

$$
I_{c} I_{a} / / Z_{1} X_{1}, I_{a} I_{b} / / X_{1} Y_{1}
$$

故 $\triangle I_{a} I_{b} I_{c}$ 与 $\triangle X_{1} Y_{1} Z_{1}$ 位似, 其透视轴为无穷远线, 故 $\triangle A B C$ 与 $\triangle I_{a} I_{b} I_{c}$ 的透视轴 $d$ 平行于 $\triangle A B C$ 与 $\triangle X_{1} Y_{1} Z_{1}$ 的透视轴 $K J L$, 即 $\triangle A B C$ 的垂足轴. 由 P.Sondat 定理, $d$ 垂直于 $\triangle A B C, \triangle I_{a} I_{b} I_{c}$ 的正交中心 $I$ 与透视中心 $P$ 的连线.又由引理 $1.3, I P$ 平行于 $\triangle A B C$ 的欧拉线.
由引理 2.1 和引理 $2.3, I H_{1}$ 平行于 $\triangle A B C$ 的欧拉线.

注 本部分证明根据 Telv Cohl (台湾) 在 AoPS 上的英文证明整理.

## III. 引理 2.3 的另一种证明途径

为避免深奥的 P. Sondat 定理,笔者想到了另一种位似证明方法.

引理 $3.1 \triangle D E F$ 的 Kosnita 点 $K_{1}$ 是 $I P$ 的中点.



图 7

证明 如图 7 所示, 设 $M_{a}, M_{b}, M_{c}$ 分别为 $A I, B I, C I$ 的中点, 则 $M_{a}, M_{b}, M_{c}$分别为 $\triangle I E F, \triangle I F D, \triangle I D E$ 的外心. 故 $D M_{a}, E M_{b}, F M_{c}$ 三线共点 $K_{1}$.

而 $\triangle M_{a} M_{b} M_{c}$ 与 $\triangle A B C, \triangle D E F$ 与 $\triangle I_{a} I_{b} I_{c}$ 分别关于 $I$ 以 $1: 2$ 的位似比位似, $K_{1}$ 在此位似变换下的像即为 $P$. 故 $K_{1}$ 是 $I P$ 中点.

引理 3.2 如图 8 所示, 设 $J_{a}, J_{b}, J_{c}$ 分别为 $\triangle I B C, \triangle I C A, \triangle I A B$ 的外心，则 $\triangle A B C$ 的 Schiffler 点 $S$ 是 $\triangle J_{a} J_{b} J_{c}$ 的 Kosnita 点.



图 8
证明 设 $J_{a}$ 关于 $B C$ 的对称点为 $J_{a}^{\prime}$, 则 $J_{a}^{\prime} I$ 的中点即为 $\triangle I B C$ 的九点圆心. 又 $J_{a}$ 是 $I I_{1}$ 中点, 故 $I_{1} J_{a}^{\prime}$ 与 $\triangle I B C$ 的欧拉线关于 $I$ 以 $2: 1$ 的位似比位似.又 $J_{a}$ 为 $\triangle I_{1} B C$ 的外心, 则 $J_{a}^{\prime} I_{1}$ 的中点即为 $\triangle I_{1} B C$ 的九点圆心. 由于 $\triangle A B C$是 $\triangle I_{1} I_{2} I_{3}$ 的垂足三角形, $B C$ 是 $I_{2} I_{3}$ 的逆平行线, 故由引理 1.8 , 结合等角共轭性质, $J_{a}^{\prime} I_{1}$ 过 $\triangle I_{1} I_{2} I_{3}$ 的 Kosnita 点.

由于 $\triangle I_{1} I_{2} I_{3}$ 与 $\triangle J_{a} J_{b} J_{c}$ 关于 $I$ 以 $2: 1$ 的位似比位似, 故 $\triangle I B C$ 的欧拉线过 $\triangle J_{a} J_{b} J_{c}$ 的 Kosnita 点. 同理, $\triangle I C A, \triangle I A B$ 的欧拉线均过 $\triangle J_{a} J_{b} J_{c}$ 的 Kosnita 点. 故 $\triangle A B C$ 的 Schiffler 点 $S$ 是 $\triangle J_{a} J_{b} J_{c}$ 的 Kosnita 点.

下面完成对引理 2.3 的证明.

证明 易得引理 3.2 中 $\triangle J_{a} J_{b} J_{c}$ 与 $\triangle D E F$ 位似, 则其外心 $O, I$ 与 Kosnita 点 $S, K_{1}$ 各是一对位似对应点. 故 $O S / / I K_{1}$. 由引理 3.1, $I K_{1}$ 即为 $I P$. 由引理 1.7 及引理 $3.2, O S$ 即为 $\triangle A B C$ 的欧拉线. 故 $I P$ 平行于 $\triangle A B C$ 的欧拉线.

## IV. 证明 $A E_{0}$ 垂直于 $\triangle A B C$ 的欧拉线

引理 4.1 设 $O I_{1}$ 与 $B C$ 交于 $G_{1}$, 则 $\angle B A G_{1}=\angle C A H_{2}$.



图 9

证明 如图 9 所示, 以顶点字母表示 $\triangle A B C$ 的内角. 则

$$
\begin{aligned}
\frac{B G_{1}}{C G_{1}} & =\frac{S_{\triangle O B I_{1}}}{S_{\triangle O C I_{1}}}=\frac{\frac{1}{2} \cdot O B \cdot I_{1} B \cdot \sin \left(\frac{\pi}{2}-A+\frac{\pi}{2}-\frac{B}{2}\right)}{\frac{1}{2} \cdot O C \cdot I_{1} C \cdot \sin \left(\frac{\pi}{2}-A+\frac{\pi}{2}-\frac{C}{2}\right)} \\
& =\frac{\cos \frac{C}{2} \cdot \sin \left(A+\frac{B}{2}\right)}{\cos \frac{B}{2} \cdot \sin \left(A+\frac{C}{2}\right)}=\frac{\cos \frac{C}{2} \cdot \cos \frac{A-C}{2}}{\cos \frac{B}{2} \cdot \cos \frac{A-B}{2}},
\end{aligned}
$$

故

$$
\begin{aligned}
\frac{\sin \angle B A G_{1}}{\sin \angle C A G_{1}} & =\frac{B G_{1} \cdot \sin B}{C G_{1} \cdot \sin C} \\
& =\frac{\cos \frac{C}{2} \cdot \cos \frac{A-C}{2} \cdot 2 \sin \frac{B}{2} \cdot \cos \frac{B}{2}}{\cos \frac{A}{2} \cdot \cos \frac{A-B}{2} \cdot 2 \sin \frac{C}{2}} \\
& =\frac{\sin \frac{B}{2} \cdot \cos \frac{A-C}{2}}{\sin \frac{C}{2} \cdot \cos \frac{A-B}{2}} .
\end{aligned}
$$

而由于

$$
\begin{aligned}
\frac{\sin \angle B A H_{2}}{\sin \angle C A H_{2}} & =\frac{F H_{2} \cdot \sin \angle A F H_{2}}{E H_{2} \cdot \sin \angle A E H_{2}}=\frac{\sin \angle F E H_{2} \cdot \sin \angle A F H_{2}}{\sin \angle E F H_{2} \cdot \sin \angle A E H_{2}} \\
& =\frac{\cos \angle D F E \cdot \sin \left(B+\frac{C}{2}\right)}{\cos \angle D E F \cdot \sin \left(C+\frac{B}{2}\right)} \\
& =\frac{\sin \frac{C}{2} \cdot \sin \left(B+\frac{C}{2}\right)}{\sin \frac{B}{2} \cdot \sin \left(C+\frac{B}{2}\right)}=\frac{\sin \frac{C}{2} \cdot \cos \frac{A-B}{2}}{\sin \frac{B}{2} \cdot \cos \frac{A-C}{2}},
\end{aligned}
$$

显然 $H_{2}$ 在形内, $G_{1}$ 在 $B C$ 边上,故 $\angle B A G_{1}=\angle C A H_{2}$.

引理 4.2 $2^{[6,7]}$ 设 $G_{1}, G_{2}, G_{3}$ 分别为 $O I_{1}, O I_{2}, O I_{3}$ 与 $B C, C A, A B$ 的交点,则 $A G_{1}, B G_{2}, C G_{3}$ 共点于 $\triangle A B C$ 的 Schiffler 点 $S$.

由引理 4.1 与 4.2, $\triangle A B C$ 的 Schiffler 点 $\mathrm{S}$ 与 $H_{2}$ 是 $\triangle A B C$ 的一对等角共轭点.

引理 4.3 如图 10 所示, $P_{1}, P_{2}$ 是 $\triangle A B C$ 的一对等角共轨点, $A P_{1}, A P_{2}$分别与外接圆交于另一点 $Q_{1}, Q_{2}, T$ 为弧 $B A C$ 上一点, $T Q_{2}$ 交 $B C$ 于 $R$,则 $\angle A T P_{1}=\angle P_{2} R B$.



图 10

证明 易得 $Q_{1} Q_{2} / / B C, \angle T R C=\angle T A P_{1}$. 由于

$$
\angle T Q_{1} C=\angle R Q_{2} C, \angle Q_{1} T C=\angle Q_{1} A C=\angle Q_{2} A B=\angle Q_{2} C R
$$

故 $\triangle Q_{1} T C \sim \triangle Q_{2} C R$. 因此 $\frac{Q_{2} R}{Q_{2} C}=\frac{Q_{1} C}{Q_{1} T}$, 即

$$
Q_{2} R \cdot Q_{1} T=Q_{1} C \cdot Q_{2} C
$$

因为 $\angle P_{1} Q_{1} C=\angle P_{2} Q_{2} C$,

$$
\begin{aligned}
\angle Q_{1} P_{1} C & =\angle P_{1} A C+\angle A C P_{1}=\angle Q_{2} A B+\angle P_{2} C B \\
& =\angle Q_{2} C B+\angle P_{2} C B=\angle Q_{2} C P_{2}
\end{aligned}
$$

故 $\triangle Q_{1} P_{1} C \sim \triangle Q_{2} C P_{2}$. 因此 $\frac{Q_{1} P_{1}}{Q_{1} C}=\frac{Q_{2} C}{Q_{2} P_{2}}$, 即

$$
Q_{2} P_{2} \cdot Q_{1} P_{1}=Q_{1} C \cdot Q_{2} C .
$$

联立 (1),(2) 得 $\frac{Q_{2} R}{Q_{2} P_{2}}=\frac{Q_{1} P_{1}}{Q_{1} T}$, 又 $\angle P_{1} Q_{1} T=\angle P_{2} Q_{2} R$, 故 $\triangle P_{1} Q_{1} T \sim \triangle R Q_{2} P_{2}$. 故 $\angle A P_{1} T=\angle P_{2} R T$. 结合 $\angle T R C=\angle T A P_{1}$ 可知 $\angle A T P_{1}=\angle P_{2} R B$.

引理 4.4 如图 11 所示, $P_{1}, P_{2}$ 是 $\triangle A B C$ 的一对等角共轭点, $P_{2}$ 关于 $B C$的对称点为 $P_{2}^{\prime}, A P_{2}$ 与外接圆交于另一点 $Q_{2}, Q_{2} P_{2}^{\prime}$ 与外接圆交于另一点 $W$, 则 $O P_{1} \perp A W$.



图 11

证明 设 $A^{\prime}$ 为 $A$ 关于外接圆的对径点, $A^{\prime} P_{1}$ 与外接圆交于另一点 $T, T Q_{2}$交 $B C$ 于 $R$, 则 $A T \perp A^{\prime} T$. 由引理 4.3, $P_{2} R \perp B C$. 故 $R$ 为 $P_{2} P_{2}^{\prime}$ 中点. 设 $P_{2} Q_{2}$中点为 $M$. 因为 $\angle A A^{\prime} P_{1}=\angle P_{2} Q_{2} R$,

$$
\begin{aligned}
\angle A P_{1} A^{\prime} & =90^{\circ}+\angle P_{1} A T=90^{\circ}+\angle P_{1} A C+\angle T A C \\
& =90^{\circ}+\angle Q_{2} A B+\angle T A C=90^{\circ}+\angle Q_{2} R B=\angle P_{2} R Q_{2},
\end{aligned}
$$

故 $\triangle A P_{1} A^{\prime} \sim \triangle P_{2} R Q_{2}$. 由 $O, M$ 分别为 $A A^{\prime}, P_{2} Q_{2}$ 中点, 得 $\triangle O P_{1} A^{\prime} \sim \triangle M R Q_{2}$.故

$$
\angle O P_{1} A^{\prime}=\angle M R Q_{2}=\angle T Q_{2} W=\angle T A W
$$

故由 $A T \perp A^{\prime} P_{1}$, 知 $O P_{1} \perp A W$.

由引理 4.4, $\triangle A B C$ 的 Schiffler 点 $S$ 满足 $O S \perp A E_{0}$, 即 $A E_{0}$ 垂直于 $\triangle A B C$的欧拉线。

综上, 由 $I H_{1}$ 平行于 $\triangle A B C$ 的欧拉线, $A E_{0}$ 垂直于 $\triangle A B C$ 的欧拉线, 得 $A E_{0} \perp I H_{1}$. 原问题得证.

## 参考文献

[1] C. Kimberling, Central Points and Central Lines in the Plane of a Triangle $[\mathrm{J}]$. Mathematics Magazine, 1994, 67(3):163 187.

[2] 梅向明,刘增贤,王汇淳,王智秋. 高等几何(第三版) $[\mathrm{M}]$. 北京: 高等教育出版社, 2008.

[3] 梁延堂. 关于两个三角形成正交透视的几个定理及其应用 $[\mathrm{J}]$. 兰州大学学报(自然科学版), 2002, 38(1):18 21 .

[4] K.Schiffier, G.R.Veldkamp, W.A.Vander Spek, Problem 1018 and Solution[J]. Crux Math, 1985,11:51; 1986,12:150 152.

[5] J. Rigby. Brief Notes on Some Forgotten Geometrical Theorems [J]. Mathematics \& Informatics Quarterly, 1997, 7:156 158.

[6] 严君啸. 一个 Schiffler 点性质的纯几何证明[J]. 中等数学, 2019, 1:19 20.

[7] L.Emelyanov, T.Emelyanova. A Note on the Schiffler Point[J]. Forum Geom, 2003,3:113 116 .

