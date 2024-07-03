$$
\text { 数学新星网 * 学生专栏 }
$$

www.nsmath.cn/xszl

# 2016 年中国国家队选拔考试平面几何试题评析 

Telv Cohl

(中国台湾 嘉义)

本文分析讨论第 57 届国际数学奥林匹克中国国家队选拔考试中的五道平面几何试题, 给出个人看法和解答, 欢迎读者批评指正.

题 1. 在圆内接六边形 $A B C D E F$ 中, $A B=B C=C D=D E$. 若线段 $A E$内一点 $K$ 满足 $\angle B K C=\angle K F E, \angle C K D=\angle K F A$, 证明: $K C=K F$.

分析 首先, 容易看出这个图形没有那么任意, 所以一个自然的问题是: 该如何画出满足题目中条件的图形? 为此可以先想办法从给定的性质求出更多的限制条件. 由给定的角度条件可得

$$
\angle B K D=\angle B K C+\angle C K D=\angle K F E+\angle K F A=\angle A F E
$$

所以 $A B C D E F$ 外接圆的圆心 $O$ 在 $\odot(B K D)$ 上.

现在我们已经可以构造出这个图形了: 先作出一以 $O$ 为圆心的圆并且在圆上取两点 $B, D$. 作出劣弧 $\overparen{B D}$ 的中点 $C$ 和 $C$ 关于 $O B, O D$ 的对称点 $A, E$.再取 $K$ 为 $\odot(B O D)$ 与 $A E$ 的其中一个交点. 最后在 $\odot O$ 上取一点 $F$ 使得 $\angle C K D=\angle K F A$ 即可 $(\angle B K D=\angle A F E$ 会保证 $\angle B K C=\angle K F E)$.

画出精准的图后不难发现 $K B / / F A, K D / / F E$, 这给出了 $F$ 一个很好的刻画. 既然平行的条件比原本给定的角度条件好用 (更有往后发展的可能), 所以考虑用同一法, 即假设 $F^{*}$ 满足 $K B / / F^{*} A, K D / / F^{*} E$, 接着想办法证明 $F^{*}$ 在 $\odot O$ 上且满足原题给定的角度条件和 $K C=K F^{*}$.

$F^{*}$ 在 $\odot O$ 上是显然的, 因为由之前的讨论我们知道弧 $\overparen{B D}$ 在 $\odot(B O D)$ 对应的角度与弧 $\overparen{A E}$ 在 $\odot O$ 中对应的角度相同, 所以 $F^{*}$ 在 $\odot O$ 上. 注意到原题的角度条件结合平行等价于 $K C$ 与 $K F^{*}$ 是 $\angle B K D$ 的一对等角线, 所以可以考虑作出 $C$ 关于 $\triangle B K D$ 的等角共轭点再证明它在 $K F^{*}$ 上 (作出等角共轭点常常有
意想不到的效果, 在许多题目中都有用到). 动手画之后会发现 $C$ 关于 $\triangle B K D$的等角共轭点好像就是 $F^{*}$ ? 如果能证明这件事那就成功证明 $F^{*}$ 就是 $F$ 了.

由对称性只需证明 $B C, B F^{*}$ 是 $\angle K B D$ 的一对等角线. 这也是容易的, 因为 $\angle F^{*} B K=\angle B F^{*} A=\angle D B C$. 至此我们已经证明 $F \equiv F^{*}$. 最后只须注意到 $O B=O D \Rightarrow K O$ 是 $\angle B K D$ 的外角平分线, 所以 $C$ 与 $F$ 关于 $K O$ 对称.



图 1

由以上的想法就产生了以下的证明:

证明 设 $A B$ 与 $D E$ 交于 $T$. 由 $\angle B K D=\angle A F E$ 和 $B D / / A E$ 可得 $T$ 是 $\odot(B K D)$ 与 $\odot(A E F)$ 的外位似中心, 所以若 $F^{*}$ 是 $K$ 在以 $T$ 为中心使 $\odot(B K D) \mapsto \odot(A E F)$ 的位似下的像, 则 $\triangle B D K$ 与 $\triangle A E F^{*}$ 位似. 由 $\angle F^{*} B K=\angle B F^{*} A=\angle D B C$ 和 $\angle F^{*} D K=D F^{*} E=\angle C D B$ 可得 $C, F^{*}$ 是 $\triangle B D K$ 的一对等角共轭点, 所以 $\angle K F^{*} A=\angle C K D, \angle K F^{*} E=\angle B K C$, 从而 $F^{*} \equiv F$.

设 $O$ 是 $\triangle A E F$ 的外心. 因为 $\angle B O D=\angle A F E=\angle B K D$, 又注意到 $O B=O D$, 可得 $O$ 是 $\odot(B D K)$ 中弧 $\overparen{B D}$ 的中点. 因此 $K O$ 是 $\angle B K D$ 的外角平分线, 从而 $C, F$ 关于 $K O$ 对称.

评论 本题一开始给的条件并不太好用, 这类型的题目中比较好的情形不外乎:

1). 经过简单推敲就能找出好用的条件 (如本题); 或者,

2). 能直接看出给定限制的一般情形.

比较麻烦的情形即 1) 和 2) 都不满足 (如 2014 IMO Shortlist G7), 这时就需要比较多的猜测和验证.
顺带一提, 本题也能作出 $B K, D K$ 与圆的第二个交点 $B^{*}, D^{*}$ 并且设 $F^{*}$ 是弧 $\widehat{B^{*} D^{*}}$ 的中点, 再证明 $F^{*} \equiv F$.



图 2

题 2. 四边形 $A B C D$ 内接于圆 $O, \angle A, \angle C$ 的内角平分线相交于点 $I$, $\angle B, \angle D$ 的内角平分线相交于点 $J$, 直线 $I J$ 不经过点 $O$, 且与边 $A B, C D$ 的延长线分别交于点 $P, R$, 与边 $B C, D A$ 分别交于点 $Q, S$. 线段 $P R, Q S$ 的中点分别为 $M, N$. 证明: $O M \perp O N$.

分析 $I$ 和 $J$ 的位置很奇怪, 以前没看过这两个点的什么性质. 比较直观的只有 $\operatorname{dist}(I, D A)=\operatorname{dist}(I, A B), \operatorname{dist}(I, B C)=\operatorname{dist}(I, C D)$ 和 $\operatorname{dist}(J, A B)=$ $\operatorname{dist}(J, B C), \operatorname{dist}(J, C D)=\operatorname{dist}(J, D A)$. 但是这对直线 $I J$ 的刻画应该没什么帮助, 也就是说比较难将 $I J$ 看成满足某些距离关系或面积关系的点的点集. 虽然对 $I, J$ 不了解, 但是 $A I, C I, B J, D J$ 的另外四个交点都是很好刻画的（内心或旁心), 所以暂且先将 $I, J$ 当成由这四个内 (旁)心产生出来的点.

取 $P R, Q S$ 的中点 $M, N$ 也是挺奇怪的, 可能的方向是去证明 $(\odot O, \odot(P R))$, $(\odot O, \odot(Q S))$ 的根轴相互垂直, 或者作出过 $P, R$ 且平行 $O M$ 的直线 $\tau_{P}, \tau_{R}$ 看看有没有经过位置比较好的点. 由此不难发现 $\tau_{R}$ 经过弧 $\overparen{A C}$, 弧 $\overparen{B D}$ 的中点. 如果能证明这件事, 那么由对称性即可得 $O M \perp O N$.

设 $A I, B J$ 与 $\odot O$ 再交于 $A^{*}, B^{*}$, 我们只需证明 $R, A^{*}, B^{*}$ 共线. 首先应该会想到利用帕斯卡定理, 也就是找圆内接六边形 $C D ? A^{*} B^{*}$ ? 或 $C D ? B^{*} A^{*}$ ?,
但是由于不知道该怎么造出直线 $I J$, 所以直接帕斯卡是不可行的. 再来直观上比较可能的方向是利用笛沙格定理, 即在 $I J$ 上找两点 $Y, Z$ 去证明 $\left(\triangle C A^{*} Y, \triangle D B^{*} Z\right)$ 或 $\left(\triangle C B^{*} Y, \triangle D A^{*} Z\right)$ 是线透视的. 或者去寻找某个过 $\left(R, A^{*}\right),\left(R, B^{*}\right)$ 并且经过一些容易刻化的点的圆, 再将共线转换成角度等式,但是现有的点中貌似没能支持这个想法.

因为 $A^{*} I \cap B^{*} J$ 和 $C I \cap D J$ 的位置都很好 (这两个点的连线根本就是 $\angle(A D, B C)$ 的角平分线), 所以考虑证明 $\triangle A^{*} C I$ 和 $\triangle B^{*} D J$ 线透视应该是可行的, 只需证明 $A^{*} C \cap B^{*} D$ 在 $\angle(A D, B C)$ 的角平分线上. 这也是容易的, 因为这个点根本就是由 $B C, C D, D A$ 形成的三角形的内心.



图 3

由以上的想法就产生了以下的证明:

证明 设 $A I, B J, C I, D J$ 与 $\odot O$ 再交于 $A^{*}, B^{*}, C^{*}, D^{*}$. 容易看出 $\left(A^{*}, C^{*}\right)$, $\left(B^{*}, D^{*}\right)$ 关于 $O$ 对称, 所以 $A^{*} B^{*} C^{*} D^{*}$ 是矩形. 因为 $C I \cap D J, C A^{*} \cap D B^{*}$,和 $I A^{*} \cap J B^{*}$ 都在 $\angle(A D, B C)$ 的角平分线上, 所以由笛沙格定理 ( $\triangle A^{*} C I$ 和 $\left.\triangle B^{*} D J\right)$ 可得 $A^{*} B^{*}, C D, I J$ 共点, 即 $R, A^{*}, B^{*}$ 共线. 同理可得 $P, C^{*}, D^{*}$ 共线.所以 $O M / / A^{*} B^{*} / / C^{*} D^{*}$. 同理 $O N / / B^{*} C^{*} / / D^{*} A^{*}$. 所以 $O M \perp O N$.

评论 本题出现许多以前没见过的点. 这类型的题目通常不是极简单 (如本题) 就是极难 (如 2011 IMO Shortlist G8), 难点在于要在短时间内要发现很多性质. 另外这道题应该没办法通过 $O M / / A^{*} B^{*} / / C^{*} D^{*}$ 这步做出来.

题 3. $P$ 为锐角 $\triangle A B C$ 内一点, $D, E, F$ 分别是 $P$ 关于 $B C, C A, A B$ 的对称点, $A P, B P, C P$ 的延长线与 $\triangle A B C$ 的外接圆分别交于点 $L, M, N$. 证明: $\triangle P D L, \triangle P E M, \triangle P F N$ 的外接圆交于除 $P$ 外的另一点 $T$.
分析 这道题其实是 anti-steiner 点的常见性质, 对熟悉 anti-steiner 点的人来说这题是非常容易的. 利用 anti-steiner 点的证明如下: 设 $H$ 为 $\triangle A B C$ 的垂心且 $A H$ 与 $\triangle A B C$ 的外接圆再交于 $X$. 设 $T$ 为 $P H$ 关于 $\triangle A B C$ 的 anti-steiner point. 因为 $H, X$ 关于 $B C$ 对称, 所以 $D, T, X$ 共线. 注意到 $P D / / A X$, 由 Reim's 定理之逆 ( $T-X-D$ 和 $L-A-P)$ 可得 $D, L, P, T$ 共圆. 同理可得 $T \in \odot(P E M)$ 和 $T \in \odot(P F N)$.

注 对任一在 $\triangle A B C$ 外接圆上的点 $U, U$ 关于 $B C, C A, A B$ 的对称点共线而且这条直线经过 $\triangle A B C$ 的垂心, 这条直线称为 $U$ 关于 $\triangle A B C$ 的 steiner 线.反过来说, 任一条经过 $\triangle A B C$ 的垂心的直线 $l$ 关于 $B C, C A, A B$ 的对称直线共点于 $\triangle A B C$ 的外接圆上一点. 这个点称为 $l$ 关于 $\triangle A B C$ 的 anti-steiner 点.



图 4

对于不熟悉 anti-steiner 点的人这题也是不难的. 画完图就会发现 $T$ 根本就在 $\triangle A B C$ 的外接圆上, 所以由对称性只需证明 $\odot(P E M)$ 与 $\odot(P F N)$ 有一异于 $P$ 且在 $\odot(A B C)$ 上的交点. 这等价于要证 $\measuredangle P F N+\measuredangle M E P=\measuredangle B P C-\measuredangle B A C$,但是目前对 $\measuredangle P F N$ 没什么太好的了解. 所以先考虑别的方向. 注意到图形中所有的点的位置在以 $P$ 为中心且固定 $\odot(A B C)$ 的反演 $\Phi$ 下的位置都很好刻画,所以可以考虑证明在 $\Phi$ 下的等价命题.

在 $\Phi$ 下 $L, M, N$ 的像分别为 $A, B, C$, 而 $D, E, F$ 的像分别为 $\odot(M P N)$, $\odot(N P L), \odot(L P M)$ 的圆心 (设为 $\left.D^{*}, E^{*}, F^{*}\right)$. 因为 $\odot(A B C)$ 在 $\Phi$ 下整体上
不变. 所以只需要证明 $B E^{*}, C F^{*}$ 的交点在 $\odot(A B C)$ 上. 看着图不难发现 (猜测) $\triangle B L C$ 与 $\triangle E^{*} L F^{*}$ 正向相似, 而这也很容易由算等角证明, 所以 $L$ 是 $B \mapsto E^{*}, C \mapsto F^{*}$ 的旋似中心. 因此 $L$ 在 $\odot(B S C)$ 上, 其中 $S \equiv B E^{*} \cap C F^{*}$, 也就是说 $S$ 在 $\odot(A B C)$ 上.

由以上的想法就产生了如下的证明:

证明 考虑以 $P$ 为中心交换 $(A, L),(B, M),(C, N)$ 的反演 $\Phi . D, E, F$ 的像 $D^{*}, E^{*}, F^{*}$ 分别为 $\odot(M P N), \odot(N P L), \odot(L P M)$ 的圆心. 因为 $E^{*} F^{*}$ 是 $P L$的中垂线, 所以 $\angle L E^{*} F^{*}=\angle L N C=\angle L B C, \angle L F^{*} E^{*}=\angle L M B=\angle L C B$,从而 $\triangle B L C \sim \triangle E^{*} L F^{*}$, 这表示 $L$ 是 $B E^{*} \mapsto C F^{*}$ 的旋似中心. 因此 $S \equiv$ $B E^{*} \cap C F^{*}$ 在 $\odot(L B C) \equiv \odot(A B C)$ 上. 同理可得 $C F^{*} \cap A D^{*} \in \odot(A B C)$. 所以 $A D^{*}, B E^{*}, C F^{*}$ 共点于 $\odot(A B C)$ 上. 这表示在变换 $\Phi$ 之前的图形中, $\odot(P D L)$, $\odot(P E M), \odot(P F N), \odot(A B C)$ 有一公共点.



图 5

评论 这道题其实是一个老结论. 曾经出现在许多论文和论坛上 (例如: AoPS). 顺带一提, 在几何题 (尤其是难题) 的证明中利用 anti-steiner 点刻画外接圆上一点是很常见的, 而利用 steiner 线计算角度也是常用手段.

题 4. 圆内接四边形 $A B C D$ 的对角线相交于点 $P$, 存在一个圆 $\Gamma$ 与 $A B, B C, A D, D C$ 的延长线分别相切于点 $X, Y, Z, T$. 圆 $\Omega$ 经过 $A, B$ 两点,且与圆 $\Gamma$ 外切于点 $S$. 证明: $S P \perp S T$.

分析 要证明的关系中有用到 $P$ 点, 所以不妨先由双圆四边形的熟知结论
给出 $P$ 点更多的性质 (比较常见的双圆四边形图形是内切圆的情形, 而旁切圆的情形会有相应的结论, 所以当不确定怎么处理旁切圆的状况时可以先想想内切圆的情形), 从而 $P$ 在 $X T$ 和 $Y Z$ 上. 将辅助线画上后不难发现 $X T \perp Y Z$.

要直接得出结论可能比较难. 先来看看 $S$ 应该有什么样的性质. 由阿波罗尼斯问题 (PPC) 的解很自然想到做过 $S$ 且与 $\Gamma$ 相切的直线 (即 $\Gamma, \Omega$ 的根轴) 与 $A B$ 的交点 $J$. 容易看出 $J$ 要满足 $J A \cdot J B=J X^{2}$, 所以对 $S$ 点至少有了比较好的刻画了: 作出 $V \equiv A B \cap Y Z$ (熟知 $(A, B ; V, X)=-1)$ 和 $X V$ 的中点 $J$, 再做过 $J$ 且与 $\Gamma$ 相切的直线, 切点即为 $S$.

有了 $J$ 点后自然会想将 $\angle P S T$ 拆成 $\angle P S J$ 和 $\angle T S J=\angle T X S=\angle V X S-$ $\angle V X T$ 来处理, 所以问题转化成证明 $\angle P S J+\angle V X S=180^{\circ}-\angle X V P \Leftrightarrow$ $\angle P S X+\angle X V P=180^{\circ}$, 即 $P, S, V, X$ 共圆. 这也是容易的, 由 $J$ 点的构造方式不难得出 $J$ 到这四个点等距.

由以上的想法就产生了如下的证明:

证明 设 $J$ 是 $S X$ 关于 $\Gamma$ 的极点且 $A B$ 与 $Y Z$ 交于 $V$. 熟知 $P$ 在 $X T, Y Z$上且 $(A, B ; V, X)=-1$, 所以由 $J X^{2}=J S^{2}=J A \cdot J B$ 可得 $J$ 是 $V X$ 的中点. 因为 $X T, Y Z$ 分别平行于 $\angle(A B, C D), \angle(B C, A D)$ 的角平分线, 所以由 $A, B, C, D$ 共圆可得 $X T \perp Y Z$. 因此 $P, S, V, X$ 在一以 $J$ 为圆心的圆上, 故 $\angle P S T=\angle P S X-\angle T S X=\angle P V A-\angle T X V=90^{\circ}$.



图 6

评论 本题将常用的双圆四边形图形的辅助线画一画之后自然的就能推出证明 (连猜测都不用), 是很简单的一道题. 通常圆外切四边形的题目可以先尝
试将常见的 (Newton 定理) 的辅助线画出来, 或者考虑以内切圆为基圆反演, 将原题转换成圆内接四边形的题目 (当然是在反演后图形不要太差的状况才考虑这样做).

另外本题也能利用反演证明. 同上述的证明有 $P$ 在 $X T$ 和 $Y Z$ 上且 $X T$ 垂直 $Y Z$. 现在考虑以 $\Gamma$ 为基圆的反演. 则 $A, B$ 的像 $A^{*}, B^{*}$ 分别为 $X Z, X Y$ 的中点, $\Omega$ 的像为一过 $A^{*}, B^{*}$ 且与 $\Gamma$ 相切的圆. 咦? 这个圆站在 $\triangle X Y Z$ 的角度来看根本就是 2011 IMO Shortlist G4 中的圆, 而预选题的结论 (推论) 是 $P S$ 与 $\Gamma$ 的第二个交点 $K$ 满足 $X K / / Y Z$, 所以只需要证明这个 $K$ 点恰好是 $T$ 的对径点即可. 这并不难, 注意到 $X T \perp Y Z$ 就能得到 $X T \perp X K$, 即 $K$ 是 $T$ 在 $\Gamma$ 中的对径点, 故 $S P \perp S T$.



图 7

题 5. 圆内接四边形 $A B C D$ 中, $A B>B C, A D>D C, I, J$ 分别是 $\triangle A B C, \triangle A D C$ 的内心. 以 $A C$ 为直径的圆与线段 $I B$ 交于点 $X$, 与 $J D$ 的延长线交于点 $Y$. 证明: 若 $B, I, J, D$ 共圆, 则 $X, Y$ 关于 $A C$ 对称.

分析 首先不难注意到只需证明 $\angle C A X=\angle C A Y$. 再来, 由 $B, D, I, J$ 共圆可得 $A B C D$ 有内切圆 (熟知的结论). 所以原题根本就是一个与双圆四边形有关的问题, 可以先想想双圆四边形的性质. 作出内切圆圆心 $T$ 后, 我们的目标是证明 $A C$ 是 $\angle X A Y$ 的角平分线, 但是 $A T$ 是 $\angle B A D$ 的角平分线, 所以只需要证明 $2 \angle T A C=\angle B A X+\angle D A Y$.

观察 $\angle T A C$ 不难发现它好像就等于 $\angle B A X$ (和 $\angle D A Y$ )? 如果能证明这件事那么就做完了. 注意到 $T$ 和 $X$ 都在 $\angle B$ 的角平分线上, 所以 $\angle T A C=\angle B A X$
$\Leftrightarrow T, X$ 是 $\triangle A B C$ 的一对等角共轭点 (比单纯的角度关系有更多可能的切入点). 因为单一个角不好处理, 所以可以考虑等角共轭点与两个交有关的性质.注意到一对 $\triangle A B C$ 的等角共轭点 $P, Q$ 必须满足 $\measuredangle B P C+\measuredangle B Q C=\measuredangle B A C$ ，所以要证明 $T, X$ 是 $\triangle A B C$ 的等角共轭点只须证明 $\angle C T A-\angle C B A=90^{\circ}$, 而这想必是不难的, 因为这已经是一个只跟双圆四边形的基本图形有关的角度关系了.

由以上的想法就产生了如下的证明:

证明 因为 $B I, D J$ 分别过 $\odot(A B C D)$ 中弧 $\overparen{A C}$ 的两中点 $M, N$, 所以由 Reim's 定理 (注意到 $A C \perp M N$ ) 可得 $I J$ 垂直 $M N$, 即 $\odot I$ 与 $A C$ 的切点和 $\odot J$与 $A C$ 的切点重合 (设为 $H$ ). 因为

$$
A H=\frac{1}{2}(A B+A C-B C)=\frac{1}{2}(A C+A D-C D) \text {, }
$$

所以 $A B+C D=B C+A D$, 这表示 $A B C D$ 有一内切圆 $\odot T$ (Urquhart 定理).

因为 $\angle C T A-\angle C B A=\angle B A T+\angle B C T=\frac{1}{2}(\angle B A D+\angle B C D)=90^{\circ}$, 又注意到 $T, X$ 都在 $\angle B$ 的角平分线上, 可得 $T, X$ 为 $\triangle A B C$ 的一对等角共轭点.从而 $\angle X A C=\angle B A T=\frac{1}{2} \angle B A D$. 同理 $\angle Y A C=\frac{1}{2} \angle B A D$, 所以 $X$ 和 $Y$ 关于 $A C$ 对称.



图 8

评论 这道题的前半部分 $(B, D, I, J$ 共圆 $\Rightarrow A B C D$ 有内切圆 $)$ 是一个老结论了, 记得应该是以前的奥数题, 这个结论也可以利用根心定理说明 $\angle A, \angle B, \angle D$ 的角平分线共点得到. 而后半部分的关键 $\angle B A X=\angle T A C$ 也不难发现, 算是简单的一题.
最后谈一下个人的经验：做几何题时往往会有很多看似可行的想法, 如何选择要先试哪个想法就依赖于以往的经验了. 通常经验比较丰富的人会能比较准确的找到可行的路, 所以平常练习题目和阅读别的做法是很重要的. 上面我的想法只是提供当参考, 当中有很多过程是依靠个人直觉和经验, 所以如果觉得奇怪也是正常的, 因为每个人的思考方式不会完全一致.

