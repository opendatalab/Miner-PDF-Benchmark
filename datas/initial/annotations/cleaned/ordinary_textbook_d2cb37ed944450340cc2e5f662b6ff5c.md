# 三角形莱斯特定理的证明 

张輇圭 ${ }^{1}$ 卢圣 ${ }^{2}$

(1. 北京大学数学科学学院 2014 级 2 班 100871 ;

2. 广西钦州市新兴街 30 号祥和景都 2 栋 2 单元 535000 )

文献 [1] 提到三角形如下一个优美的定理:

定理 (莱斯特). 三角形的外心, 九点圆心和第一, 第二费马点四点共圆.

该圆称为三角形的莱斯特 (Laster) 圆. 可惜的是文献 [1] 并没有给出这个优美定理的证明, 我们经过研究, 得到该定理的一个纯几何的证明, 现整理成文供大家参考.

由于证明涉及到很多近代欧氏几何的内容, 为确保证明过程流畅, 我们将这些内容以引理的形式给出, 这些引理也揭示了三角形的第一、第二费马点, 第一、第二等力点, 共轭重心, 拿破仑三角形等近代欧氏几何概念的联系. 引理中参考文献没有证明的, 我们也将给出证明.

引理 $\mathbf{1}^{[2]}$. 如图 1, 过圆外的一点 $P$ 作圆的两切线 $P A, P B$, 过 $P$ 作圆的一条割线交圆于 $C, D$, 交 $A B$ 于 $Q$, 则 $P, C, Q, D$ 构成调和点列且 $\frac{C P}{P D}=\frac{C Q}{Q D}=\frac{C B^{2}}{B D^{2}}$.



图 1



图 2

引理 $2^{[3]}$. 如图 2, 以 $\triangle A B C$ 的三边为边向外作等边三角形 $\triangle B C D$, $\triangle C A E, \triangle A B F$, 则

(1) $A D=B E=C F$;

(2) $A D, B E, C F$ 共点, 称为第一费马点;

(3) 第一费马点为三个外侧正三角形的外接圆的公共点. 向内作三个等边三角形也有三个类似的结论, 此时三线及三圆所共的点为第二费马点.

注. 费马点也称等角中心. ${ }^{[3]}$

引理 $3^{[3]}$. 三角形的三个阿波罗尼 (Apollonius) 圆与其外接圆正交.

注. 以三角形一角的内外角平分线与对边两个交点连成的线段为直径的圆称为阿波罗尼圆. 当三角形为等腰三角形时, 顶角所对应的阿波罗尼圆退化为底边的中垂线, 此为需要注意的一种特殊情形. 每个三角形都有三个阿波罗尼圆.

引理 $4^{[4]}$. 与 $\triangle A B C$ 外接圆切于 $B$ 和 $C$ 的切线交于 $P$, 则直线 $A P$ 为 $\angle B A C$ 所对的共轭中线 (又称类似中线, 陪位中线 ${ }^{[5]}$ ).

引理 $5^{[3]} . \triangle A B C$ 的第一, 第二费马点 $R, R^{\prime}$ 的等角共轮点分别为第一, 第二等力点 $S, S^{\prime}, \triangle A B C$ 的外心, 共轮重心分别为 $O, K$, 则 $O, S, K, S^{\prime}$ 为一组调和点列, 且 $\frac{S O}{O S^{\prime}}=\frac{S A^{2}}{S^{\prime} A^{2}}$.

注. 等力点又称正则点, 等积点 ${ }^{[1]}$; 三角形的三条共轭中线共点, 该点称为共轭重心, 也有文献称为类似重心或陪位重心 ${ }^{[5]}$.

引理 5 证明 第一, 第二费马点与第一, 第二等力点互为等角共轭点见文献 [3], 我们仅证明引理的后半部分.

如图 3, 以 $B C$ 为边向 $\triangle A B C$ 外侧作正 $\triangle B C D$, 记 $\triangle A B C$ 的外接圆半径为 $R$.



图 3

由于 $R$ 与 $S$ 为等角共轭点, 所以 $\angle S C A=\angle B C R=\angle B D A, \angle S A C=$ $\angle B A D$, 故 $\triangle A S C \sim \triangle A B D$, 从而 $\frac{S C}{B D}=\frac{A C}{A D}$. 同理 $\frac{B S}{C D}=\frac{B A}{D A}$.
又 $B D=C D$, 故 $\frac{S C}{B S}=\frac{A C}{A B}$. 同理 $\frac{S^{\prime} C}{B S^{\prime}}=\frac{A C}{A B}$. 因此 $S, S^{\prime}$ 在以 $B, C$ 为定点, $\frac{A C}{A B}$ 为定比的 Apollonius 圆上. 同理 $S, S^{\prime}$ 也在 $\triangle A B C$ 的另外两个 Apollonius 圆上. 所以 $\triangle A B C$ 的三个 Apollonius 圆交于 $S, S^{\prime}$ 两点

记 $\triangle A B C$ 的三个 Apollonius 圆为 $\odot O_{1}, \odot O_{2}, \odot O_{3}$. 由引理 3 知 $O$ 到 $\odot O_{1}, \odot O_{2}, \odot O_{3}$ 的幂为 $R^{2}$, 即 $O$ 在 $\odot O_{1}, \odot O_{2}, \odot O_{3}$ 的根轴上, 所以 $O, S, S^{\prime}$三点共线.

设外接圆与 $\odot O_{1}$ 的另一交点为 $M$, 由 Apollonius 圆的性质知 $\frac{B M}{C M}=\frac{B A}{C A}$,即四边形 $A B M C$ 为调和四边形. 由引理 4 知 $A M$ 为边 $B C$ 的共轭中线, 所以 $A M$ 过 $K$, 即 $K$ 对外接圆和 $\odot O_{1}$ 的幕相等.

同理 $K$ 对外接圆和 $\odot O_{2}, \odot O_{3}$ 的幂相等. 所以 $K$ 对外接圆, $\odot O_{1}, \odot O_{2}, \odot O_{3}$四圆的幂相等. 故 $O, S, K, S^{\prime}$ 共线.

由引理 1 知 $O, S, K, S^{\prime}$ 成调和点列且 $\frac{S O}{O S^{\prime}}=\frac{S A^{2}}{S^{\prime} A^{2}}$.

引理 $6^{[3]}$. 三角形的重心为内外拿破仑三角形的中心.

注. 外拿破仑三角形是指以三角形的三边为边向三角形的外侧所作三个正三角形的中心组成的三角形. 向内侧所作三个正三角形所得三个中心所成的三角形为内拿破仑三角形 ${ }^{[1]}$.

引理 6 证明 我们仅证外拿破仑三角形的情形, 内拿破仑三角形的情形类似.

如图 4, 以 $B C$ 为边向 $\triangle A B C$ 外侧作正 $\triangle B C D, \triangle O_{1} O_{2} O_{3}$为 $\triangle A B C$ 的外拿破仑三角形, $B C$ 中点为 $M, \triangle A B C$ 重心为 $G$.

由重心性质易知 $\frac{M G}{G A}=\frac{M O_{1}}{O_{1} D}=\frac{1}{2}$, 故 $O_{1} G / / A D$.

由引理 2 知, $A D$ 是以 $A B, A C$ 为边分别向外侧所作的正三角形的外接圆的根轴. 所以 $A D \perp O_{2} O_{3}$, 故 $O_{1} G \perp O_{2} O_{3}$.



图 4

同理 $O_{2} G \perp O_{3} O_{1}, O_{3} G \perp O_{1} O_{2}$.

故 $G$ 为 $\triangle O_{1} O_{2} O_{3}$ 的中心.

引理 $7^{[3]}$. 一点的垂足三角形的边，垂直于原三角形相应顶点与这点的等角共轭点的连线.

引理 $8^{[3]}$. 从两个等角共轭点到各边的垂线的垂足在一个圆上, 圆心是这两个等角共轨点连线的中点.

引理 $9^{[3]}$. 到三角形各边的距离与边长成正比的点仅有一个, 即共轮重心.
引理 10. 共轭重心是外拿破仑三角形与第一等力点的垂足三角形的位似中心，也是内拿破仑三角形与第二等力点的垂足三角形的位似中心.

引理 10 证明 我们仅证明外拿破仑三角形及第一等力点的情形, 对于内拿破仑三角形及第二等力点的情形类似可得.

如图 5, 设 $\triangle O_{1} O_{2} O_{3}$ 为 $\triangle A B C$ 的外拿破仑三角形. $R, S$ 分别为 $\triangle A B C$ 的第一费马点、第一等力点, $S$ 关于 $\triangle A B C$ 的垂足三角形为 $\triangle X Y Z, \triangle A B C$ 的三边长为 $a, b, c$.

由于 $R, S$ 是一对等角共轭点, 由引理 7 知 $A R \perp Y Z, B R \perp X Z, C R \perp X Y$.

由引理 $2, A R \perp O_{2} O_{3}, B R \perp O_{3} O_{1}, C R \perp$



图 5 $O_{1} O_{2}$. 从而 $Y Z / / O_{2} O_{3}, Z X / / O_{3} O_{1}, X Y / / O_{1} O_{2}$. 故 $O_{3} Z, O_{2} Y, O_{1} X$ 三线共点且该点为正 $\triangle O_{1} O_{2} O_{3}$ 和正 $\triangle X Y Z$ 的位似中心. 设该位似中心为 $K_{1}$.

设 $K_{1}$ 到 $\triangle A B C$ 三边的距离分别为 $d_{1}, d_{2}, d_{3}, O_{1}, O_{2}, O_{3}$ 分别到 $B C, C A, A B$的距离分别为 $h_{1}, h_{2}, h_{3}$, 正 $\triangle O_{1} O_{2} O_{3}$ 和正 $\triangle X Y Z$ 的边长分别为 $\mu, \lambda$.

由 $Y Z / / O_{2} O_{3}, Z X / / O_{3} O_{1}, X Y / / O_{1} O_{2}$ 知

$$
\frac{\lambda}{\mu-\lambda}=\frac{d_{1}}{h_{1}}=\frac{d_{2}}{h_{2}}=\frac{d_{3}}{h_{3}}
$$

易知 $h_{1}=\frac{\sqrt{3}}{6} a, h_{2}=\frac{\sqrt{3}}{6} b, h_{3}=\frac{\sqrt{3}}{6} c$, 故

$$
\frac{\sqrt{3}}{6} \cdot \frac{\lambda}{\mu-\lambda}=\frac{d_{1}}{a}=\frac{d_{2}}{b}=\frac{d_{3}}{c}
$$

由引理 9 知 $K_{1}$ 为类似重心.

引理 11. 三角形的第一费马点与第一等力点连线, 第二费马点与第二等力点连线都平行于欧拉线.

引理 11 证明 我们仅证明三角形的第一费马点与第一等力点连线平行于欧拉线. 第二费马点与第二等力点的情形的证明类似.

如图 6, $\triangle O_{1} O_{2} O_{3}$ 为 $\triangle A B C$ 的外拿破仑三角形, $O, G$ 分别为 $\triangle A B C$ 的外心、重心, $R, S$ 分别为 $\triangle A B C$ 的第一费马点、第一等力点, $M$ 为 $R S$ 的中点, $K$ 为 $\triangle A B C$ 的共轭重心, $X, Y, Z$ 为 $S$ 在 $\triangle A B C$ 三边的垂足.

由引理 10 知 $\triangle O_{1} O_{2} O_{3}$ 与 $\triangle X Y Z$ 位似, 位似中心为 $K$, 设位似比为 $\lambda$.

由 $O_{1} O / / X S, O_{2} O / / Y S, O_{3} O / / Z S$, 得 $K, S, O$ 三点共线, 且 $K$ 分 $S O$ 的比为 $\lambda$.
由引理 6、引理 8 知 $M, G$ 为两个正三角形的中心, 即为一对位似对应点,故 $K, M, G$ 三点共线, 且 $K$ 分 $M G$ 的比为 $\lambda$. 从而 $M S / / G O$, 且 $\frac{M S}{G O}=\lambda$.

因此 $R S / / G O$, 且 $\frac{R S}{G O}=2 \lambda$, 即 $R S$ 平行 $\triangle A B C$ 的欧拉线.



图 6

引理 $12^{[3]}$ 。第一、第二费马点分别在内、外拿破仑三角形的外接圆上.

引理 12 证明 我们仅证明第一费马点在内拿破仑三角形的外接圆上, 第二费马点在外拿破仑三角形的外接圆上的证明类似.

如图 7, $O_{1}, V_{1}$ 为以边 $B C$ 分别向 $\triangle A B C$ 外侧和内侧所作正三角形的中心, $R$ 为 $\triangle A B C$ 的第一费马点, $\triangle V_{1} V_{2} V_{3}$ 为 $\triangle A B C$ 的内拿破仑三角形.

易知 $\angle O_{1} B C=30^{\circ}, O_{1}, V_{1}$ 关于 $B C$ 对称. 故

$$
O_{1} B=O_{1} C=O_{1} V_{1}=O_{1} R
$$

即 $B, R, V_{1}, C$ 四点共圆.

故 $\angle C R V_{1}=30^{\circ}$. 同理 $\angle C R V_{2}=30^{\circ}$. 因此 $\angle V_{2} R V_{1}=\angle C R V_{2}+\angle C R V_{1}=60^{\circ}=\angle V_{2} V_{3} V_{1}$故 $V_{1}, R, V_{3}, V_{2}$ 四点共圆.



图 7

引理 13. $\triangle A B C$ 的第一、第二等力点 $S, S^{\prime}$, 外内拿破仑三角形的外接圆半径为 $r_{1}, r_{2}$, 则 $\frac{r_{1}}{r_{2}}=\frac{A S^{\prime}}{A S}$.

引理 13 证明 如图 8, 以 $B C$ 为边分别向 $\triangle A B C$ 外侧, 内侧作正 $\triangle B C D$, $\triangle B C D^{\prime}, \triangle O_{1} O_{2} O_{3}$ 为 $\triangle A B C$ 的外拿破仑三角形, $\triangle V_{1} V_{2} V_{3}$ 为 $\triangle A B C$ 的内拿破仑三角形.

由引理 5 知 $\frac{S A}{A B}=\frac{A C}{A D}$, 即 $S A \cdot A D=A C \cdot A B$.

同理 $A S^{\prime} \cdot A D^{\prime}=A B \cdot A C$.
故 $S A \cdot A D=A S^{\prime} \cdot A D^{\prime}$, 即 $\frac{A S^{\prime}}{A S}=\frac{A D}{A D^{\prime}}$.

易知 $\triangle C O_{1} O_{2} \sim \triangle C D A$, 故 $\frac{A D}{O_{1} O_{2}}=\frac{C D}{O_{1} C}=\sqrt{3}$.

同理 $\frac{A D^{\prime}}{V_{1} V_{2}}=\sqrt{3}$. 所以

$$
\frac{r_{1}}{r_{2}}=\frac{O_{1} O_{2}}{V_{1} V_{2}}=\frac{A D}{A D^{\prime}}=\frac{A S^{\prime}}{A S}
$$



图 8



图 9

引理 14. 三角形两个费马点的连线与两个等力点的连线交于类似重心.

引理 14 证明 如图 9, $\triangle A B C$ 中, $R, S$ 分别为第一费马点、第一等力点, $R^{\prime}, S^{\prime}$ 分别为第二费马点、第二等力点, $G, K$ 分别为重心、共轭重心, $M, M^{\prime}$ 分别为 $R S, R^{\prime} S^{\prime}$ 的中点.

由引理 11 知 $G, M$ 两个正三角形的中心, 即为一对位似对应点. 所以 $G, M, K$ 共线. 同理 $G, M^{\prime}, K$ 共线.

由引理 5 知 $K$ 在直线 $S S^{\prime}$ 上, 又由 $R S / / R^{\prime} S^{\prime}$, 所以 $S S^{\prime}, R R^{\prime}, M M^{\prime}$ 共点于 $K$.

下面证明莱斯特定理.

定理证明 如图 10, $\triangle A B C$ 中, $R, S$ 分别为第一费马点、第一等力点, $R^{\prime}, S^{\prime}$分别为第二费马点、第二等力点, $O, G, H, N, K$ 分别为外心、重心、垂心、九点圆心、共轭重心, $M, M^{\prime}$ 分别为 $R S, R^{\prime} S^{\prime}$ 的中点, 延长 $R R^{\prime}$ 交欧拉线于 $J$. 设 $\triangle A B C$ 的外内拿破仑三角形的外接圆半径为 $r_{1}, r_{2}$.

由引理 11 知 $G$ 为 $O J$ 的中点. 又 $G H=2 O G$, 故 $J$ 为 $G H$ 的中点.

由引理 12 知 $\left(\frac{G R}{G R^{\prime}}\right)^{2}=\left(\frac{r_{2}}{r_{1}}\right)^{2}$, 由引理 13 知 $\left(\frac{A S}{A S^{\prime}}\right)^{2}=\left(\frac{r_{2}}{r_{1}}\right)^{2}$. 又由引理 5、引理 11 知

$$
\left(\frac{A S}{A S^{\prime}}\right)^{2}=\frac{S O}{S^{\prime} O}, \quad \frac{S O}{S^{\prime} O}=\frac{G S}{G R^{\prime}}
$$



图 10

从而 $\left(\frac{G R}{G R^{\prime}}\right)^{2}=\frac{G S}{G R^{\prime}}$, 即 $G R^{2}=G S \cdot G R^{\prime}$.

所以 $\triangle G R S \sim \triangle G R^{\prime} R$, 因此 $\angle G R^{\prime} R=\angle G R S=\angle R G J$.

故 $\triangle G J R \sim \triangle R^{\prime} J G$, 从而 $G J^{2}=J R \cdot J R^{\prime}$. 又由 $2 N J=G J, O J=2 G J$,得 $G J^{2}=N J \cdot O J$.

所以 $J R \cdot J R^{\prime}=N J \cdot O J$. 故 $O, N, R, R^{\prime}$ 四点共圆.

## 参考文献

[1] 吴悦辰. 三线坐标与三角形特征点 $[\mathrm{M}]$. 哈尔滨: 哈尔滨工业大学出版社, 2015: 549, 75, 63-64.

[2] 沈文选, 杨清桃. 几何瑰宝 (上) [M]. 哈尔滨: 哈尔滨工业大学出版社, 2010: 538.

[3] 约翰逊. 近代欧氏几何学 [M]. 单樽译, 哈尔滨: 哈尔滨工业大学出版社, 2012: 151, 209-210, 152, 105, 147, 152.

[4] 波拉索洛夫. 俄罗斯平面几何问题集 $[\mathrm{M}]$. 周春荔译, 哈尔滨: 哈尔滨工业大学出版社, 2009: 387 .

[5] 梁绍鸿. 初等数学复习及研究 (平面几何) [M]. 哈尔滨: 哈尔滨工业大学出版社, 2008: 162 .

