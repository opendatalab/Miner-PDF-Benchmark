$$
\text { 数学新星网 } \% \text { 学生专栏 }
$$

www.nsmath.cn/xszl

# 一道几何难题的证明 

Telv Cohl

(中国台湾 嘉义)

去年 AoPS 论坛上的网友 LeVietAn 在高中数奥的几何版上贴了如下的一道题目:

问题 设 $P, Q$ 为 $\triangle A B C$ 的一对等角共轭点且 $G_{P}, G_{Q}$ 分别为 $P, Q$ 关于 $\triangle A B C$ 的垂足三角形的重心. 设 $M, N$ 分别为 $P Q, G_{P} G_{Q}$ 的中点. 证明：若 $P Q$平行于 $G_{P} G_{Q}$, 则 $M N$ 经过 $\triangle A B C$ 的外心.

当时笔者一时没有解出来. 直到今年初, 笔者发现这道题仍然未解, 所以重新思考了这道题, 经过了一些探索后终于给出了证明. 证明中用到许多有趣且新颖的引理, 本文将仔细介绍这道题目的证明和其中用到的引理的其他应用.在第一节中先介绍一些本文中会用到的名词和一些基本性质, 第二节介绍一些常见的引理, 第三节介绍原题的证明中用到的主要引理, 第四节给出原题的证明, 第五节介绍在第二节和第三节中的引理的一些应用. 在本文中的问题/引理/证明后的括号内的黑粗体字表示该问题/引理/证明的提出者在 AoPS 论坛上的网名.

## 1. 基本名词介绍

定义 1.1 给定三角形 $\triangle A B C$ 与一点 $P$. 设 $D, E, F$ 分别为 $B C, C A, A B$ 的中点, 则称使得 $\triangle A B C \cup P$ 与 $\triangle D E F \cup Q$ 位似的点 $Q$ 为 $P$ 关于 $\triangle A B C$ 的补点 (complement). 换句话说, $Q$ 为 $P$ 在位似 $\left(G,-\frac{1}{2}\right)$ 下的像, 其中 $G$ 为 $\triangle A B C$的重心. 反过来我们称 $P$ 为 $Q$ 关于 $\triangle A B C$ 的反补点 (anticomplement).

定义 1.2 给定三角形 $\triangle A B C$ 与一点 $P$. 设 $\triangle D E F$ 为 $P$ 关于 $\triangle A B C$ 的西瓦三角形, 则称 $\triangle A B C$ 与 $\triangle D E F$ 的透视轴为 $P$ 关于 $\triangle A B C$ 的三线性极线 (trilinear polar). 反过来说, 对于任意一条直线 $\gamma$, 都存在一点 $R$ 使得 $\gamma$ 为 $R$[^0]关于 $\triangle A B C$ 的三线性极线, 且称 $R$ 为 $\gamma$ 关于 $\triangle A B C$ 的三线性极点 (trilinear pole).

一个熟知的三线性极线的性质如下:

性质 1.1 给定三角形 $\triangle A B C$ 与一点 $P$. 设 $P^{*}$ 为 $P$ 关于 $\triangle A B C$ 的等角共轭点 (等距共轭点), 则一点 $Q$ 关于 $\triangle A B C$ 的三线性极线经过 $P$ 当且仅当 $P^{*}$关于 $\triangle A B C$ 的三线性极线经过 $Q$ 关于 $\triangle A B C$ 的等角共轭点 (等距共轭点).

这个性质只是简单的射影几何习题, 所以证明留给读者.

定义 1.3 给定三角形 $\triangle A B C$ 与一点 $P$. 过 $P$ 分别作 $A P, B P, C P$ 的垂线与 $B C, C A, A B$ 交于点 $D, E, F$, 则 $D, E, F$ 共线. 我们称这条直线为 $P$ 关于 $\triangle A B C$ 的正交截线 (orthotransversal).

在介绍下一个名词之前, 先回忆一些 $\triangle A B C$ 外接圆雉曲线的性质:

性质 1.2 对任一条 $\triangle A B C$ 的外接圆锥曲线 $\mathcal{C}$ (即经过 $A, B, C$ 三点的圆锥曲线), $\mathcal{C}$ 上的点关于 $\triangle A B C$ 的等角共轭点 (等距共轭点) 的点集为一条直线.反过来说, 对任意一条直线 $\ell, \ell$ 上的点关于 $\triangle A B C$ 的等角共轭点 (等距共轭点)的点集为 $\triangle A B C$ 的外接圆锥曲线.

由此可以将性质 1.1 改写成以下比较常见的形式:

性质 1.1 $1^{\prime}$ 给定三角形 $\triangle A B C$ 与一点 $P$. 设 $P^{*}$ 为 $P$ 关于 $\triangle A B C$ 的等角共轨点 (等距共轭点), 则一点 $Q$ 关于 $\triangle A B C$ 的三线性极线经过 $P$ 当且仅当 $Q$ 在 $P^{*}$ 关于 $\triangle A B C$ 的三线性极线关于 $\triangle A B C$ 的等角共轭像 (等距共轭像) 上.

定义 1.4 称 $\triangle A B C$ 的欧拉线关于 $\triangle A B C$ 的等角共轭像为 $\triangle A B C$ 的 Jerabek 双曲线.

注意到 $\triangle A B C$ 的外接圆为无穷远直线关于 $\triangle A B C$ 的等角共轨像, 所以一条直线 $\tau$ 与 $\odot(A B C)$ 的交点关于 $\triangle A B C$ 的等角共轭点为 $\tau$ 关于 $\triangle A B C$ 的等角共轭像 $\mathcal{H}$ 与无穷远直线的交点. 由此可知 $\tau$ 经过 $\triangle A B C$ 的外心 (即 $\mathcal{H}$ 经过 $\triangle A B C$ 的垂心) 当且仅当 $\mathcal{H}$ 为一等轴双曲线, 并且此时 $\tau$ 与 $\odot(A B C)$ 的交点关于 $\triangle A B C$ 的西姆松线平行于 $\mathcal{H}$ 的渐近线. 特别的, Jerabek 双曲线为一条等轴双曲线.

本节的最后, 提一下 $\triangle A B C$ 的内切圆雉曲线的基本性质.

性质 1.3 任一条与 $\triangle A B C$ 的边相切的圆锥曲线的焦点为 $\triangle A B C$ 的一对
等角共轭点. 反过来说, 对任一对 $\triangle A B C$ 的等角共轭点 $J, K$, 都存在一条以 $J, K$ 为焦点且与 $B C, C A, A B$ 相切的圆锥曲线 $\mathcal{O}$.

由圆雉曲线的光学性质可知, 若 $K_{A}$ 为 $K$ 关于 $B C$ 的对称点, 那么 $J K_{A}$ 与 $B C$ 的交点即为 $\mathcal{O}$ 与 $B C$ 的切点. 特别的, 当这条内切圆锥曲线为抛物线时, 它的一个焦点与它和无穷远直线的切点重合, 所以它的另一个焦点在 $\odot(A B C)$ 上.

## 2. 基本引理及证明

引理 2.1 (2009 IMO 第二题的推广) 给定三角形 $\triangle A B C$. 设 $E, F$ 分别为 $C A, A B$ 上的点且 $E F$ 与 $\triangle A B C$ 的外接圆交于 $M$ 和 $N$. 设 $P, Q, R, S$ 分别为 $B E, C F, E F, M N$ 的中点, 则 $P, Q, R, S$ 共圆.

证法一 设 $E^{\prime}, F^{\prime}$ 分别为 $E, F$ 关于 $S$ 的对称点. 由 Klamkin 定理 (蝴蝶定理的推广) 可得 $B E^{\prime}$ 与 $C F^{\prime}$ 的交点 $D$ 在 $\triangle A B C$ 的外接圆上, 所以由 $S P / / D B, S Q / / D C$ 可得 $\angle P S Q=\angle B D C=\angle B A C$. 另一方面, 显然有 $R P / / A B$ 和 $R Q / / A C$, 所以 $\angle P R Q=\angle B A C=\angle P S Q$. 故 $P, Q, R, S$ 共圆.



图一

证法二 设 $O$ 为 $\triangle A B C$ 的外心且 $A^{\prime}$ 为 $A$ 关于 $O$ 的对称点, $H$ 为 $\triangle A E F$的垂心且 $J$ 为 $A^{\prime} H$ 的中点. 由 $O J / / A H$ 可得 $O J \perp E F$, 所以 $O, S, J$ 共线.

另一方面, 注意到 $P J / / A^{\prime} B / / E H$ 和 $P R / / A B$ 可得 $\angle J P R=90^{\circ}$, 所以 $J, P, R, S$ 共圆. 同理, $Q$ 也在这个圆上, 所以 $J, P, Q, R, S$ 共圆.



图二

注 这个引理也能利用帕斯卡定理证明, 但本质与证法一是一样的.

引理 2.2 给定四边形 $A B C D$ 与其一内切圆锥曲线 $\mathcal{C}$. 设 $A B$ 与 $C D$ 交于点 $E, B C$ 与 $D A$ 交于点 $F$. 则 $\mathcal{C}$ 的中心 $O$ 在完全四边形 $A B C F D E$ 的牛顿线 (经过 $A C, B D, E F$ 中点的直线) 上.

证明 设 $\mathcal{C}$ 分别与 $A B, D A, B C$ 切于点 $X, Y, Z$ 并且 $M, N$ 分别为 $X Z, X Y$的中点. 设 $R, S$ 分别为 $E F$ 与 $A C, B D$ 的交点. $K$ 为满足 $K A / / X Y, K B / / X Z$的点且 $T$ 为 $A B$ 上使得 $K T / / E F$ 的点. 因为 $O$ 关于 $\mathcal{C}$ 的极线为无穷远直线,所以 $B O$ 关于 $\mathcal{C}$ 的极点为 $X Z$ 上的无穷远点. 故 $B O$ 经过 $X Z$ 的中点 $M$. 同理可得 $A, N, O$ 共线.

由 $A(B, D ; S, C)=-1=C(B, D ; S, A)$ 可得 $S$ 为 $A C$ 关于 $\mathcal{C}$ 的极点, 所以 $S$ 在 $A$ 关于 $\mathcal{C}$ 的极线 $X Y$ 上. 同理可得 $R \in X Z$.

由 $A(X, Y ; N, K)=-1=B(X, Z ; M, K)$ 得 $F, K, O$ 共线. 又 $\triangle B K T \sim$ $\triangle X R E, \triangle A K T \sim \triangle X S E$, 故

$$
\frac{T A}{T B}=\frac{T A}{T K} \cdot \frac{T K}{T B}=\frac{E X}{E S} \cdot \frac{E R}{E X}=\frac{E R}{E S} .
$$

所以当 $\mathcal{C}$ 变动时, $T$ 是 $A B$ 上一定点且 $K$ 在一定直线上变动, 结合 $T(K, O ; B, F)=B(K, O ; X, Z)=-1$ 可得 $O$ 在一过 $T$ 的定直线 $\ell$ 上. 由 $E F / / T K$ 可得 $\ell$ 经过 $E F$ 的中点. 同理 $\ell$ 也经过 $A C$ 与 $B D$ 的中点, 所以 $\ell$ 即为完全四边形 $A B C F D E$ 的牛顿线.



图三

注 这个引理表明完全四边形的牛顿线即为与完全四边形的边相切的圆锥曲线的中心集合. 换句话说, 任一对四边形的等角共轭点对的中点在由这个四边形的边形成的完全四边形的牛顿线上.

引理 2.3 (treegoner) 给定三角形 $\triangle A B C$ 与一点 $P$. 设 $\triangle D E F$ 为 $P$ 关于 $\triangle A B C$ 的西瓦三角形且 $\omega$ 为 $P$ 关于 $\triangle D E F$ 的垂足圆, 则 $P$ 关于 $\triangle A B C$ 的正交截线为 $P$ 关于 $\omega$ 的极线。

证明 设 $\triangle X Y Z$ 为 $P$ 关于 $\triangle D E F$ 的垂足三角形. 过 $P$ 且垂直 $A P$ 的直线分别与 $B C, F D, D E$ 交于 $A_{1}, U, V$. 由对称性, 只需要证明 $A_{1}$ 在 $P$ 关于 $\odot(X Y Z)$ 的极线上. 显然 $D, P, Y, Z$ 在一以 $D P$ 为直径的圆上, 所以由 $U V \perp D P$ 可得 $U V, Y Z$ 关于 $\angle E D F$ 逆平行, 从而 $U, V, Y, Z$ 共圆.



图四
设 $U V$ 与 $Y Z$ 交于 $J$. 因为

$$
J P^{2}=J Y \cdot J Z=J U \cdot J V
$$

所以结合 $\left(A_{1}, P, ; U, V\right)=-1$ 可得 $J$ 为 $A_{1} P$ 的中点且 $J$ 在点圆 $P$ 与 $\odot(X Y Z)$的根轴 $\tau$ 上. 注意到 $\tau$ 在位似 $(P, 2)$ 下的像即为 $P$ 关于 $\odot(X Y Z)$ 的极线, 所以 $A_{1}$ 在 $P$ 关于 $\odot(X Y Z)$ 的极线上.

引理 2.4 给定三角形 $\triangle A B C$ 与一点 $P$. 设 $\Omega$ 为 $P$ 关于 $\triangle A B C$ 的垂足圆.则 $P$ 关于 $\triangle A B C$ 的三线性极线, $P$ 关于 $\triangle A B C$ 的正交截线与 $P$ 关于 $\Omega$ 的极线共点.

证明 设 $\triangle D E F$ 为 $P$ 关于 $\triangle A B C$ 的反西瓦三角形且 $C A$ 与 $F D$ 交于 $B_{1}$, $A B$ 与 $D E$ 交于 $C_{1}$. 过 $P$ 且垂直 $B P$ 的直线分别与 $C A, F D$ 交于 $Y_{1}, E_{1}$. 过 $P$且垂直 $C P$ 的直线分别与 $A B, D E$ 交于 $Z_{1}, F_{1}$. 由引理 2.3 得 $E_{1} F_{1}$ 为 $P$ 关于 $\Omega$ 的极线. 由笛沙格定理 ( $\triangle B_{1} E_{1} Y_{1}$ 和 $\left.\triangle C_{1} F_{1} Z_{1}\right)$ 可得 $B_{1} C_{1}, E_{1} F_{1}, Y_{1} Z_{1}$ 共点,注意到 $B_{1} C_{1}$ 和 $Y_{1} Z_{1}$ 分别为 $P$ 关于 $\triangle A B C$ 的三线性极线和正交截线, 所以结论得证.



图五

当引理 2.4 中的 $P$ 点在 $\triangle A B C$ 的外接圆上时,就得到以下的推论.

推论 2.5 设 $P$ 为 $\triangle A B C$ 的外接圆上的点, 则 $P$ 关于 $\triangle A B C$ 的 steiner 线, $P$ 关于 $\triangle A B C$ 的三线性极线, $P$ 关于 $\triangle A B C$ 的正交截线共点.

引理 2.6 (buratinogigle) 设 $P$ 为 $\triangle A B C$ 的外接圆 $\odot O$ 上的一点. 则 $P$关于 $\triangle A B C$ 的 steiner 线与 $P$ 关于 $\triangle A B C$ 的正交截线的交点 $Q$ 在 $\triangle A B C$ 的

Jerabek 双曲线上.

证明 (Luis González) 设过 $P$ 且垂直 $B P$ 的直线分别与 $C A, \odot O$ 交于 $E, B^{\prime}$. 过 $P$ 且垂直 $C P$ 的直线分别与 $A B, \odot O$ 交于 $F, C^{\prime}$. 由帕斯卡定理 $\left(A B B^{\prime} P C^{\prime} C\right)$ 可得 $P$ 关于 $\triangle A B C$ 的正交截线 $E F$ 经过 $O$. 设 $H$ 为 $\triangle A B C$ 的垂心且 $A H$ 与 $\odot O$ 再交于 $T$. 设 $L$ 为 $P$ 关于 $B C$ 的对称点. 因为 $H$ 与 $T$ 关于 $B C$ 对称, 所以 $P$ 关于 $\triangle A B C$ 的 steiner 线 $H L$ 与 $B C, P T$ 共点于 $U$. 由帕斯卡定理 $\left(A T P C^{\prime} C B\right)$ 可得 $F, U, V \equiv A H \cap C C^{\prime}$ 共线, 所以由帕斯卡定理之逆 $(A H Q O C B)$ 可得 $A, B, C, O, H, Q$ 在一条圆锥曲线上, 即 $Q$ 在 $\triangle A B C$ 的 Jerabek 双曲线 上.



图六

由推论 2.5 和引理 2.6 可得以下推论.

推论 2.7 设 $P$ 为 $\triangle A B C$ 的外接圆上一点且 $P$ 关于 $\triangle A B C$ 的 steiner 线,三线性极线, 正交截线分别为 $\mathcal{S}_{P}, \mathcal{T}_{P}, \mathcal{O}_{P}$, 则 $\mathcal{S}_{P}, \mathcal{T}_{P}, \mathcal{O}_{P}$ 中任两条直线平行当且仅当这两条直线平行于 $\triangle A B C$ 的 Jerabek 双曲线的其中一条渐近线, 并且此时 $P$ 为 $\triangle A B C$ 的欧拉线与 $\odot(A B C)$ 的其中一个交点.

## 3. 主要引理及证明

引理 3.1 设 $P, Q$ 为 $\triangle A B C$ 的一对等角共轭点. 设 $\triangle Q_{a} Q_{b} Q_{c}$ 为 $Q$ 关于 $\triangle A B C$ 的垂足三角形且 $G$ 为 $\triangle Q_{a} Q_{b} Q_{c}$ 的重心. 则 $G Q$ 垂直于 $P$ 关于 $\triangle A B C$的三线性极线.

证明 设 $Q_{a} G, Q_{b} G, Q_{c} G$ 分别再与 $\odot\left(Q_{a} Q_{b} Q_{c}\right)$ 交于 $D, E, F$. 设 $P$ 关于
$\triangle A B C$ 的三线性极线分别与 $B C, C A, A B$ 交于 $P_{A}, P_{B}, P_{C}$. 因为

$$
P\left(P_{A}, A ; B, C\right)=-1=\left(Q_{a} G, Q_{b} Q_{c} ; Q_{a} Q_{c}, Q_{a} Q_{b}\right)
$$

且注意到 $A P, B P, C P$ 分别垂直 $Q_{b} Q_{c}, Q_{a} Q_{c}, Q_{a} Q_{b}$, 因此 $P P_{A} \perp Q_{a} G$. 熟知 $\triangle Q_{a} Q_{b} Q_{c}$ 的外心为 $P Q$ 的中点, 所以 $P P_{A}$ 为 $Q_{a} D$ 的中垂线在位似 $(Q, 2)$ 下的像, 从而 $P_{A}$ 为 $Q$ 在 $\odot\left(Q Q_{a} D\right)$ 中的对径点. 同理可得 $Q P_{B}, Q P_{C}$ 分别为 $\odot\left(Q Q_{b} E\right), \odot\left(Q Q_{c} F\right)$ 的直径. 因为

$$
Q_{a} G \cdot G D=Q_{b} G \cdot G E=Q_{c} G \cdot G F
$$

所以 $\odot\left(Q Q_{a} D\right), \odot\left(Q Q_{b} E\right), \odot\left(Q Q_{c} F\right)$ 有共同的根轴 $G Q$, 表示这三个圆的圆心连线 (经过 $Q P_{A}, Q P_{B}, Q P_{C}$ 的中点直线) 垂直于 $G Q$, 因此 $P$ 关于 $\triangle A B C$ 的三线性极线 $\overline{P_{A} P_{B} P_{C}}$ 垂直于 $G Q$.



图七

注 利用类似的方法可以证明过 $Q$ 且垂直于 $P$ 关于 $\triangle A B C$ 的正交截线 的直线经过 $\triangle Q_{a} Q_{b} Q_{c}$ 的垂心.

引理 3.2 给定三角形 $\triangle A B C$ 与一定点 $M$. 设 $P, P^{*}$ 为 $\triangle A B C$ 的一对等角共轨点且 $\tau$ 为 $P^{*}$ 关于 $\triangle A B C$ 的三线性极线. 则若 $\measuredangle(\tau, M P)$ 为给定的角度 $\theta$,那么 $P$ 点在一条过 $M$ 和 $\triangle A B C$ 的共轭重心 $K$ 的圆锥曲线 $\Gamma_{(M, \theta)}$ 上.

证明 事实上, 由 $P$ 点的构造方式 (对给定的 $M$ 和 $\theta$ ) 就能得出这个引理.设 $\ell$ 为一条经过 $M$ 的直线, $\ell^{*}$ 为一条经过 $M$ 且满足 $\measuredangle\left(\ell^{*}, \ell\right)=\theta$ 的直线. 如果 $P$ 在 $\ell$ 上使得 $\measuredangle(\tau, M P)=\theta$, 则 $\tau$ 平行于 $\ell^{*}$, 这表示 $\tau, \ell^{*}$ 与无穷远直线共点. 因
为无穷远直线为 $\triangle A B C$ 的重心 $G$ 关于 $\triangle A B C$ 的 三线性极点, 所以如果 $Q^{*}$ 是 $\ell^{*}$ 关于 $\triangle A B C$ 的 三线性极点, 那么 $P^{*}, Q^{*}, G$ 在一条 $\triangle A B C$ 的外接圆雉曲线上, 由此可得 $K P$ 经过 $Q^{*}$ 关于 $\triangle A B C$ 的等角共轭点 $Q$. 反过来说, 如果 $K Q$ 与 $\ell$ 交于 $P$, 那么 $\tau$ 与 $\ell^{*}$ 平行.

我们只需要证明当 $\ell$ 绕着 $M$ 旋转时, 线束 $\ell$ 与线束 $K Q$ 射影对应即可, 这样就表明两线束的对应直线交点 $P$ 在一条经过 $M, K$ (两线束的线束中心) 的圆雉曲线上. 因为经过 $M$ 的线束关于 $\triangle A B C$ 的 三线性极点的集合为 $\triangle A B C$的一条外接圆锥曲线 $\mathcal{C}$, 所以当 $\ell$ 绕着 $M$ 旋转时, $Q^{*}$ 在 $\mathcal{C}$ 上移动, 由此就能推出 $Q$ 在 $\mathcal{C}$ 关于 $\triangle A B C$ 的等角共轭像 $\mathcal{C}^{*}$ (为一条直线) 上移动.

因为 $\ell^{*}$ 和 $A Q^{*}$ 与 $B C$ 的交点关于 $B, C$ 调和共轭, 所以当 $\ell$ 变动时线束 $A Q^{*}$ 与线束 $\ell^{*}$ 射影对应. 显然当 $\ell$ 变动时线束 $\ell, \ell^{*}$ 射影对应 (两线束的对应直线只相差角度 $\theta$ ) 且线束 $A Q^{*}, A Q$ 射影对应 (两线束的对应直线关于 $\angle A$ 的角平分线对称), 所以线束 $\ell$ 与线束 $A Q$ 射影对应, 从而点列 $\ell \cap \mathcal{C}^{*}$ 与点列 $Q$ 射影对应, 故线束 $\ell$ 与线束 $K Q$ 射影对应.

由推论 2.7 可知对任一点 $M, \Gamma_{\left(M, 90^{\circ}\right)}$ 经过 $\triangle A B C$ 的 Jerabek 双曲线 与无穷远直线的交点, 所以就得到以下推论.

推论 3.3 在引理 3.2 的记号下, 对任一点 $M, \Gamma_{\left(M, 90^{\circ}\right)}$ 与 $\triangle A B C$ 的 Jerabek 双曲线位似。

特别的, 设 $O$ 和 $H$ 分别为 $\triangle A B C$ 的外心和垂心. 以下两个特例是比较有意思的.

推论 3.3.1(IDMasterz, XmL) $\Gamma_{\left(H, 90^{\circ}\right)}$ 为三角形 $\triangle A B C$ 的 Jerabek 双曲线.

推论 3.3.2 $\Gamma_{\left(O, 90^{\circ}\right)}$ 经过三角形 $\triangle A B C$ 的内心, 旁心, 外心, 共轭重心.

这两个推论的证明都是容易的, 只需要验证所描述的圆雉曲线上五点满足 $\Gamma_{(M, \theta)}$ 的定义即可.

引理 3.4 设 $D_{1}, E_{1}, F_{1}$ 分别为 $B C, C A, A B$ 上的点且 $G_{1}$ 为 $\triangle D_{1} E_{1} F_{1}$ 的重心. 设 $D_{2}, E_{2}, F_{2}$ 分别为 $B C, C A, A B$ 上的点且 $G_{2}$ 为 $\triangle D_{2} E_{2} F_{2}$ 的重心. $P$点为满足有向距离比

$$
\operatorname{dist}(P, B C): \operatorname{dist}(P, C A): \operatorname{dist}(P, A B)=\frac{1}{D_{1} D_{2}}: \frac{1}{E_{1} E_{2}}: \frac{1}{F_{1} F_{2}}
$$

的点. 则 $G_{1} G_{2}$ 平行于 $P$ 关于 $\triangle A B C$ 的三线性极线 $\tau_{P}$.
证明 首先先证明如下引理:

引理 3.4.1 给定 $\triangle A B C$ 与两点 $E \in C A, F \in A B$. 设 $P$ 为满足有向距离比

$$
\operatorname{dist}(P, B C): \operatorname{dist}(P, C A): \operatorname{dist}(P, A B)=\frac{1}{B C}: \frac{1}{C E}: \frac{1}{F B}
$$

的点. 则 $E F$ 平行于 $P$ 关于 $\triangle A B C$ 的三线性极线 $\varsigma$.



图八

引理 3.4.1 的证明设 $\varsigma$ 分别与 $C A, A B$ 交于 $Y, Z$. 因为 $[P C B]=[P B F]$,所以 $B P$ 平分 $C F$, 得 $(B C, B F ; B P, C F)=-1=B(C, F ; P, Y)$, 这表示 $C F$ 与 $B Y$ 平行. 同理可得 $B E / / C Z$, 所以由小帕斯普定理可得 $E F / / Y Z \equiv \varsigma$. 引理得证.



图九
回到原题. 过 $D_{1}, D_{2}$ 分别作 $A B, A C$ 的平行线交于 $T$. 设 $E, F$ 分别为使得 $D_{2} E_{1} E_{2} E, D_{1} F_{2} F_{1} F$ 为平行四边形的点. 因为 $E_{1} G_{1}$ 经过 $F_{1} D_{1}$ 的中点 $U$ 且 $\frac{G_{1} U}{E G_{1}}=\frac{1}{2}$, 所以 $G_{1}$ 为 $\triangle F E_{1} F_{2}$ 的重心, 从而 $F G_{1}$ 经过 $E_{1} F_{2}$ 的中点 $V$ 且 $\frac{G_{1} V}{F G_{1}}=\frac{1}{2}$.

同理可得 $E G_{2}$ 经过 $V$ 且 $\frac{G_{2} V}{E G_{2}}=\frac{1}{2}$, 所以 $E F / / G_{1} G_{2}$.

设 $P^{*}$ 为使得 $\triangle A B C \cup P$ 与 $\triangle T D_{1} D_{2} \cup P^{*}$ 位似的点. 由引理 3.4.1 可得 $E F$平行于 $P^{*}$ 关于 $\triangle T D_{1} D_{2}$ 的三线性极线, 从而 $G_{1} G_{2}$ 平行于 $P^{*}$ 关于 $\triangle T D_{1} D_{2}$的三线性极线, 故 $G_{1} G_{2} / / \tau_{P}$.

推论 3.5 给定 $\triangle A B C$ 与两点 $P, Q$. 设 $\triangle P_{a} P_{b} P_{c}, \triangle Q_{a} Q_{b} Q_{c}$ 分别为 $P, Q$关于 $\triangle A B C$ 的垂足三角形. 设 $J$ 为 $\odot(A B C)$ 上一点且 $J$ 关于 $\triangle A B C$ 的西姆松线平行于 $P Q$. 则 $\triangle P_{a} P_{b} P_{c}, \triangle Q_{a} Q_{b} Q_{c}$ 的重心连线平行于 $J$ 关于 $\triangle A B C$ 的三线性极线。

证明 设 $J_{a}, J_{b}, J_{c}$ 分别为 $J$ 到 $B C, C A, A B$ 的垂足. 由引理 3.4 可知只需要证明

$$
J J_{a}: J J_{b}: J J_{c}=\frac{1}{P_{a} Q_{a}}: \frac{1}{P_{b} Q_{b}}: \frac{1}{P_{c} Q_{c}} .
$$

因为 $\triangle J B J_{c} \sim \triangle J C J_{b}$, 所以注意到 $A J$ 关于 $\angle A$ 的等角线垂直于 $J$ 关于 $\triangle A B C$ 的西姆松线 $\overline{J_{a} J_{b} J_{c}}$ 可得

$$
\frac{J J_{b}}{J J_{c}}=\frac{J C}{J B}=\frac{\sin \angle J A C}{\sin \angle J A B}=\frac{\cos \angle(P Q, A B)}{\cos \angle(P Q, A C)}=\frac{P_{c} Q_{c}}{P_{b} Q_{b}}
$$

同理可得另外两个比例关系, 所以推论 3.5 得证.



图十
引理 3.6 设 $(P, Q),(R, S)$ 为 $\triangle A B C$ 的两对等角共轭点且 $P Q / / R S$. 设 $I, I_{a}, I_{b}, I_{c}$ 分别为 $\triangle A B C$ 的内心, $A-$ 旁心, $B-$ 旁心, $C-$ 旁心. $M, N$ 分别为 $P Q, R S$ 的中点. 则 $I, I_{a}, I_{b}, I_{c}, M, N$ 在一条圆锥曲线上.

## 证明 首先证明以下两个引理.

引理 3.6.1 给定三角形 $\triangle A B C$ 与两点 $E \in C A, F \in A B$. 设 $Y$ 为 $E$关于 $A, C$ 的等距共轭点, $Z$ 为 $F$ 关于 $A, B$ 的等距共轭点. 设 $\mathcal{P}$ 为与 $B C, C A, A B, E F$ 相切的抛物 线且 $\mathcal{P}$ 与 $E F$ 相切于 $T$. 则 $T$ 与 $Y_{0}, Z_{0}$ 共线, 其中 $Y_{0}, Z_{0}$ 分别为 $Y, Z$ 关于 $\triangle A B C$ 的反补点.

引理 3.6.1 的证明 设 $A_{0}, B_{0}, C_{0}$ 分别为 $A, B, C$ 关于 $\triangle A B C$ 的反补点 且 $O$ 为 $\triangle A_{0} B_{0} C_{0}$ 为外心 (即 $\triangle A B C$ 的垂心). 因为 $\mathcal{P}$ 的焦点在 $\triangle A B C, \triangle A E F$的外接圆上, 所以 $\mathcal{P}$ 的焦点即为由 $\triangle A B C$ 和 $E F$ 形成的完全四边形 $\mathcal{Q}$ 的密克点 $M$. 设 $M^{\prime}$ 为 $M$ 关于 $E F$ 的对称点, 则 $M^{\prime} T$ 经过 $\mathcal{P}$ 的另一个焦点 (也是 $\mathcal{P}$ 的中心), 所以由引理 2.2 , 得 $M^{\prime} T$ 平行于 $\mathcal{Q}$ 的牛顿线. 熟知 $Y Z$ 平行于 $\mathcal{Q}$ 的牛顿线, 所以 $M^{\prime} T / / Y Z / / Y_{0} Z_{0}$, 因此只需证明 $M^{\prime}$ 在 $Y_{0} Z_{0}$ 上即可.

设 $M_{1}$ 为 $O$ 在 $Y_{0} Z_{0}$ 上的垂足, 以下证明 $M_{1}$ 即为 $M^{\prime}$. 因为 $M$ 是 $B F \mapsto C E$的旋似中心, 所以 $\frac{M B}{M C}=\frac{B F}{C E}=\frac{A Z}{A Y}$, 结合 $\angle B M C=\angle Z A Y$ 可得 $\triangle A Y Z \sim$ $\triangle M C B$. 另一方面, 因为 $E, F$ 分别为 $B_{0} Y_{0}, C_{0} Z_{0}$ 的中点, 所以由引理 2.1 可得 $E, F, M_{0}, M_{1}$ 共圆. 注意到 $M_{0} F / / A C$ 就得到 $\angle M_{1} E F=\angle M_{1} M_{0} F=$ $\angle Z Y A=\angle F E M$, 类似可得 $\angle M_{1} F E=\angle F E M$, 所以 $M_{1}$ 与 $M$ 关于 $E F$ 对称,故 $M_{1} \equiv M^{\prime}$.



图十一
引理 3.6.2 给定一圆雉曲线 $\mathcal{C}$ 与两定直线 $\ell, \ell_{1}$, 其中 $\ell_{1}$ 与 $\mathcal{C}$ 相切于 $T$. 设 $V$ 为 $\ell_{1}$ 上一定点, $R$ 为 $\ell$ 上一动点. 设 $T R$ 与 $\mathcal{C}$ 再交于 $S$, 过 $S$ 且与 $\mathcal{C}$ 相切的直线与 $V R$ 交于 $K$. 则当 $R$ 在 $\ell$ 上变动时, $K$ 在一条固定的圆雉曲线上. 并且如果设 $\ell$ 与 $\ell_{1}$ 交于 $J$, 那么这条圆雉曲线经过 $V$ 和 $V$ 关于 $J, T$ 的调和共轨点 $U$.

引理 3.6.2 的证明 设 $\tau$ 为 $R$ 关于 $\mathcal{C}$ 的极线且 $L \in \tau$ 为 $\ell$ 关于 $\mathcal{C}$ 的极点.因为当 $R$ 变动时, 线束 $\tau$ 与线束 $L R$ 射影对应, 所以线束 $\tau$ 与线束 $V R$ 射影对应, 则当 $R$ 变动时, $\tau$ 与 $V R$ 的交点 $P$ 在一条固定圆锥曲线 $\mathcal{H}$ 上. 当 $R$ 与 $J$ 重合时 $P$ 与 $T$ 重合, 所以 $\mathcal{H}$ 经过 $T$ 和两线束的线束中心 $L, V$. 设 $Q \equiv \tau \cap T S, X \equiv \ell \cap P T$. 因为

$$
X(P, R ; K, V)=(P, R ; K, V)=(Q, R ; S, T)=-1=X(T, J ; U, V)
$$

所以 $K, U, X$ 共线. 因为线束 $T P$ 与线束 $U X$ 射影对应 (两线束的对应直线的交点 $X$ 在一定直线 $\ell$ 上), 所以线束 $V P$ 与线束 $U X$ 射影对应, 从而两线束的对应直线的交点 $K$ 在一条固定的圆雉曲线上且这条圆锥曲线经过两线束的线束中心 $U, V$.



图十二

回到引理 3.6 的证明. 为了方便, 将原引理改述如下:

引理 3.6 ${ }^{\prime}$ 给定三角形 $\triangle A B C$ 与一无穷远点 $L$, 设 $J, K$ 为 $\triangle A B C$ 的一对等角共轮点且 $J, K, L$ 共线. $\mathcal{C}$ 为以 $J, K$ 为焦点且内切于 $\triangle A B C$ 的圆锥曲线.则 $\mathcal{C}$ 的中心 $T$ 在一条固定的圆锥曲线上.

证明 设 $J K$ 与 $B C$ 交于 $V . B C$ 关于 $J K$ 的对称直线分别与 $C A, A B$交于 $E, F$. 设 $A^{\prime}, B^{\prime}, C^{\prime}, E^{\prime}, F^{\prime}$ 分别为 $B C, C A, A B, B E, C F$ 的中点且
$G \equiv E F \cap E^{\prime} F^{\prime}$. 由引理 2.2 可知 $T$ 在 $E^{\prime} F^{\prime}$ 上. 设 $\mathcal{P}$ 为与 $B^{\prime} C^{\prime}, C^{\prime} A^{\prime}, A^{\prime} B^{\prime}, E^{\prime} F^{\prime}$相切的抛物线, 则由引理 3.6.1 可得 $G$ 为 $\mathcal{P}$ 与 $E^{\prime} F^{\prime}$ 的切点. 因为 $V G \equiv E F$ 平行于由 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 和 $E^{\prime} F^{\prime}$ 形成的完全四边形的牛顿线, 所以 $V G$ 经过 $\mathcal{P}$ 与无穷远直线的切点. 由引理 3.6.2 ( $\ell$ 和 $\ell_{1}$ 分别为 $B C$ 和无穷远直线) 可得当 $J, K$ 变动时 $T$ 在一条经过 $/ / J K, \perp J K$ 方向上的无穷远点的圆雉曲线上. 最后只需注意到 $\triangle A B C$ 的内心与旁心在这条圆锥曲线上即可.



图十三

注 引理 3.6 给出 $\triangle A B C$ 的内切圆雉曲线的主轴方向的一个刻画. 对一条中心为 $O$ 的 $\triangle A B C$ 的内切圆雉曲线, 它的主轴方向平行于经过 $O$ 和 $\triangle A B C$的内心, 旁心的双曲线的渐近线.

## 4. 主要问题证明

问题 (LeVietAn) 设 $P . Q$ 为 $\triangle A B C$ 的一对等角共轮点且 $G_{P}, G_{Q}$ 分别为 $P, Q$ 关于 $\triangle A B C$ 的垂足三角形的重心. 设 $M, N$ 分别为 $P Q, G_{P} G_{Q}$ 的中点.证明: 若 $P Q$ 平行于 $G_{P} G_{Q}$, 则 $M N$ 经过 $\triangle A B C$ 的外心.

证明 设 $O$ 为 $\triangle A B C$ 的外心, $\triangle M_{a} M_{b} M_{c}$ 为 $M$ 关于 $\triangle A B C$ 的垂足三角形. 显然 $N$ 为 $\triangle M_{a} M_{b} M_{c}$ 的重心, 所以若 $M^{\prime}$ 为 $M$ 关于 $\triangle A B C$ 的等角共轭点,那么由引理 3.1 可得 $M N$ 垂直于 $M^{\prime}$ 关于 $\triangle A B C$ 的三线性极线 $\tau$.

另一方面, 由推论 2.7 和推论 3.5 可知若 $P Q / / G_{P} G_{Q}$, 则 $P Q, G_{P} G_{Q}$ 平行于 $\triangle A B C$ 的 Jerabek 双曲线 $\mathcal{J}$ 的其中一条渐近线, 所以结合引理 3.6 得过 $M$和 $\triangle A B C$ 的内心, 旁心的圆雉曲线与 $\mathcal{J}$ 位似. 由推论 3.3 可得 $M$ 在推论 3.3.2 中描述的圆雉曲线上, 所以 $O M \perp \tau$.
由上面的讨论可知 $M, N, O$ 共线且 $\overline{M N O} \perp \tau$.



图十四

## 5. 引理的其他应用

利用第二节与第三节中的引理还能得出许多有趣的结论. 在本节将举一些应用的例子并留一些问题给读者练习.

问题 5.1 给定三角形 $\triangle A B C$ 与其垂心 $H$. 设 $P$ 为 $\triangle A B C$ 的欧拉线上一点且 $Q$ 为 $P$ 关于 $\triangle A B C$ 的等角共轭点. 则 $Q$ 关于 $\triangle A B C$ 的垂足三角形的重心在 $H Q$ 上.

证明 由引理 3.1 与推论 3.3.1 可得.

问题 5.2 设 $K$ 为 $\triangle A B C$ 的九点圆圆心关于 $\triangle A B C$ 的等角共轭点. 设 $H_{K}$ 为 $K$ 关于 $\triangle A B C$ 的垂足三角形的垂心. 证明: $H_{K} K$ 经过 $\triangle A B C$ 的外心 $O$ 且 $\overline{H_{K} O}=3 \overline{H_{K} K}$.

证明 设 $N$ 为 $\triangle A B C$ 的九点圆的圆心, 过 $N$ 且垂直 $A N$ 的直线与 $B C$ 交于 $D$. 熟知 $O$ 关于 $B C$ 的对称点 $O_{a}$ 为 $A$ 关于 $N$ 的对称点, 所以 $D$ 即为 $\triangle A O O_{a}$的外心. 设 $\odot(D)$ 与 $\odot(O)$ 再交于 $X$, 则由 $\angle X A O=\angle O X A=\angle O O_{a} N$ 可知 $A X$ 为 $A N$ 关于 $\angle A$ 的等角线, 故 $A, K, X$ 共线.

同理, 如果 $N$ 关于 $\triangle A B C$ 的正交截线 分别与 $C A, A B$ 交于 $E, F$, 那么 $\odot(E), \odot(F)$ 与 $\odot(O)$ 的第二个交点 $Y, Z$ 分别在 $B K, C K$ 上. 由 $A K \cdot K X=$ $B K \cdot K Y=C K \cdot K Z=$ 可知 $O K$ 为 $\odot(D), \odot(E), \odot(F)$ 的根轴, 所以 $O K$垂直于 $\overline{D E F}$. 另一方面, 由引理 3.1 的注解中的性质可知 $K H_{K} \perp \overline{D E F}$, 所以
$O, K, H_{K}$ 共线.



图十五

设 $H$ 为 $\triangle A B C$ 的垂心. 设 $O_{K}, G_{K}$ 分别为 $K$ 关于 $\triangle A B C$ 的垂足三角形的外心, 重心. 由问题 5.1 得 $H, K, G_{K}$ 共线. 因为 $H_{K} G_{K}$ 经过 $N K$ 的中点 $O_{K}$且 $G_{K} H_{K}=2 O_{K} G_{K}$, 所以 $G_{K}$ 为 $\triangle N K H_{K}$ 的重心, 因此 $K H$ 经过 $N H_{K}$ 的中点 $M$. 由孟氏定理 $\left(\triangle O N H_{K}\right.$ 与 $\left.\overline{M K H}\right)$ 可得 $\overline{H_{K} O}=3 \overline{H_{K} K}$.



图十六

由问题 5,2 的证明很容易得到以下推论.
推论5.3 (IDMasterz, XmL) 设 $K$ 为 $\triangle A B C$ 的九点圆圆心关于 $\triangle A B C$的等角共轭点. $N_{K}$ 为 $K$ 关于 $\triangle A B C$ 的垂足三角形的九点圆圆心. 则 $K N_{K}$ 平行于 $\triangle A B C$ 的欧拉线.

问题 5.4 (Arab) 设 $I, O$ 分别为 $\triangle A B C$ 的内心, 外心. 设 $A I, B I, C I$, 分别与 $B C, C A, A B$ 交于 $D, E, F$. 证明: $O I$ 经过 $\triangle D E F$ 的九点圆圆心 $T$.

证明 (IDMasterz, XmL) 设 $I_{a}, I_{b}, I_{c}$ 分别为 $\triangle A B C$ 的 $A-$ 旁心, $B-$旁心, $C-$ 旁心. 设 $K$ 为 $O$ 关于 $\triangle I_{a} I_{b} I_{c}$ 的等角共轭点且 $\triangle K_{a} K_{b} K_{c}$ 为 $K$ 关于 $\triangle I_{a} I_{b} I_{c}$ 的垂足三角形. 熟知 $O I_{a}, O I_{b}, O I_{c}$ 分别垂直于 $E F, F D, D E$, 所以 $I D E F$ 与 $K K_{a} K_{b} K_{c}$ 位似. 注意到 $O$ 为 $\triangle I_{a} I_{b} I_{c}$ 的九点圆圆心, 所以由推论 5.3 可知 $I T$ 平行于 $\triangle I_{a} I_{b} I_{c}$ 的欧拉线 $I O$, 故 $I, O, T$ 共线.



图十七

下面这些问题也是前面几节中的引理和性质的应用, 留给读者练习.

问题 5.5 设 $O, K$ 分别为 $\triangle A B C$ 的外心, 共轭重心. $S$ 为 $\triangle A B C$ 的外接圆上一点使得 $S$ 关于 $\triangle A B C$ 的西姆松线平行于 $O K$. 证明: $S$ 关于 $\triangle A B C$ 的等距共轭点为垂直于 $\triangle A B C$ 的欧拉线方向上的无穷远点.

问题 5.6 给定 $\triangle A B C$ 与一点 $P$. 设 $\triangle D E F, \triangle P_{a} P_{b} P_{c}$ 分别为 $P$ 关于 $\triangle A B C$ 的反西瓦三角形, 垂足三角形. $Q$ 为 $P$ 在以 $\odot\left(P_{a} P_{b} P_{c}\right)$ 为基圆的反演下的像. 证明 $\triangle D P Q, \triangle E P Q, \triangle F P Q$ 的垂心共线.

问题 5.7 给定 $\triangle A B C$ 与一点 $P$. 设 $K$ 为 $\triangle A B C$ 的共轭重心, $G_{P}$ 为 $P$ 关
于 $\triangle A B C$ 的垂足三角形的重心. 设 $T$ 为 $\odot(A B C)$ 上一点且 $T$ 关于 $\triangle A B C$ 的西姆松线平行于 $K P$. 证明: $K G_{P}$ 为 $T$ 关于 $\triangle A B C$ 的三线性极线.

问题 5.8 (Luis González) 设 $O, H, G, K$ 分别为 $\triangle A B C$ 的外心，垂心，重心, 共轭重心. 设 $\triangle H_{a} H_{b} H_{c}, \triangle G_{a} G_{b} G_{c}$ 分别为 $H, G$ 关于 $\triangle A B C$ 的垂足三角形. 证明: $\triangle H_{a} H_{b} H_{c}$ 与 $\triangle G_{a} G_{b} G_{c}$ 的重心连线平行于 $O K$.

问题 5.9 (SalaF) 给定 $\triangle A B C$ 与两点 $P, Q$. 设 $\triangle P_{a} P_{b} P_{c}, \triangle Q_{a} Q_{b} Q_{c}$ 分别为 $P, Q$ 关于 $\triangle A B C$ 的垂足三角形且 $H_{P}, H_{Q}$ 分别为他们的垂心. 证明：若 $\triangle P_{a} P_{b} P_{c} \sim \triangle Q_{a} Q_{b} Q_{c}$, 则 $P H_{P} / / Q H_{Q}$.

问题 5.10 (THVSH) 设 $K$ 为 $\triangle A B C$ 的九点圆圆心关于 $\triangle A B C$ 的等角共轮点. 过 $B, C$ 且与 $\odot(A B C)$ 相切的直线交于 $D$. 设 $K_{A}$ 为 $K$ 关于 $B C$ 的对称点. 证明: $D K_{A}$ 经过 $\triangle A B C$ 的垂心.


[^0]:    收稿日期: 2016-04-24； 第一次修订：2016-05-22； 第二次修订：2016-06-01.

