# 一道新星几何测试题的探讨 

王琛<br>(浙江省乐清市乐成寄宿中学，325600)<br>指导教师: 羊明亮

2017 年秋季上海新星数学奥林匹克中有这样一道题:

题 1. 如图, 四边形 $A B C D$ 内接于圆 $O$, 且 $A B \cdot C D=B C \cdot A D$. 四边形的对边 $A B, C D$ 交于点 $K$, 对角线 $A C, B D$ 交于点 $J$ ( $O, J$ 不重合). 过点 $K$作 $O J$ 的垂线, 分别与直线 $B D, A C$ 交于点 $E, F$. 以 $E F$ 为直径的圆与线段 $O J$ 交于点 $T$. 证明: $K T$ 平分 $\angle E T F$.

![](https://cdn.mathpix.com/cropped/2024_02_26_7645b011da5bd004a006g-1.jpg?height=583&width=688&top_left_y=1299&top_left_x=684)

该题难度适中, 图形蕴含丰富的几何性质, 是道较好的几何题.

下文将给出三道与本题在图形上有很大关联的几何题, 并由题 3 与题 4 分别给出题 1 的两个证明.

为方便理解, 题 2, 3,4 及其证明中各点使用的符号均与题 1 保持一致.

题 2. 在 $\triangle T E F$ 中, 已知 $\angle E T F=90^{\circ}, H$ 为过顶点 $T$ 的高的垂足, 设 $J$为线段 $T H$ 内部的一点, $B$ 为线段 $E J$ 上一点, 使得 $F B=F T$. $C$ 为线段 $F J$上的一点, 使得 $E C=E T . P$ 为 $E C$ 与 $B F$ 的交点, 证明: $P B=P C \cdot{ }^{[1]}$.

(第 53 届 IMO 试题)

收稿日期: 2017-12-14； 修订日期: 2018-01-29.
证明 设 $\triangle J E F$ 的垂心为 $O, F J, E J$ 分别交 $O E, O F$ 于点 $M, N$. 则由 $F J \perp O E, O H \perp E F$ 知 $O, M, H, F$ 四点共圆.

由射影定理, $E C^{2}=E T^{2}=E H \cdot E F=E M \cdot E O$.

则由射影定理的逆定理知 $\angle E C O=90^{\circ}$.

同理, $\angle F B O=90^{\circ}$.

又注意到, $E, M, N, F$ 四点共圆, 又由射影定理, $O C^{2}=O M \cdot O E=O N \cdot O F=O B^{2}$.

故 $O B=O C$. 从而 $\mathrm{R}_{\mathrm{t}} \triangle O B P \cong \mathrm{R}_{\mathrm{t}} \triangle O C P$,因此 $P B=P C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_7645b011da5bd004a006g-2.jpg?height=416&width=491&top_left_y=443&top_left_x=1248)

探索题 2 的图形可得题 3.

题 3. 已知不等边 $\triangle T E F$ 满足 $\angle E T F=90^{\circ}, T H \perp E F, H$ 为垂足, $J$ 为线段 $T H$ 上的一点, $B$ 为线段 $E J$ 上的一点, 使得 $F B=F T$. $C$ 为线段 $F J$ 上的一点, 使得 $E C=E T . \triangle H B C$ 的外接圆与线段 $E F$ 的第二个交点为 $K($ 异于点 $H$ ). 证明: $K T$ 平分 $\angle E T F \cdot{ }^{[2]}$

(2013 美国国家队选拔考试)

证明 设 $\triangle J E F$ 的垂心为 $O, \triangle H B C$ 的外接圆与 $T H$ 的第二个交点为 $Q$ (异于点 $H$ ).

同题 2 证明, 有 $O B=O C, \angle O B F=\angle O C E=90^{\circ}$.

又 $O H \perp E F$, 故 $O, B, H, F$ 四点共圆. 于是 $\angle B O Q=\angle B F K ; \angle B Q O=180^{\circ}-\angle B Q H=$ $180^{\circ}-\angle B K E=\angle B K F$.

因此 $\triangle B Q O \sim \triangle B K F$.

同理 $\triangle C Q O \sim \triangle C K E$.

从而

![](https://cdn.mathpix.com/cropped/2024_02_26_7645b011da5bd004a006g-2.jpg?height=420&width=491&top_left_y=1635&top_left_x=1245)

$$
\frac{F K}{F T}=\frac{F K}{F B}=\frac{O Q}{O B}=\frac{O Q}{O C}=\frac{E K}{E C}=\frac{E K}{E T} .
$$

即

$$
\frac{F K}{E K}=\frac{F T}{E T}
$$

由角平分线定理的逆定理知, $K T$ 平分 $\angle E T F$.

事实上我们可以发现, 题 1 的条件与题 3 的条件是等价的, 两题的图形与要证明的结论也一模一样, 也就是说, 题 1 和题 3 实际上是同一道题!
于是将题 1 转化为题 3 , 我们得到题 1 的第一个证明.

题 1 证法一由于四边形 $A B C D$ 内接于圆 $O$, 点 $J, K$ 分别为其对角线和对边的交点, 故点 $J$ 关于 $\odot O$ 的极线过点 $K$.

又 $O J \perp E F$, 故直线 $E F$ 即为点 $J$ 关于 $\odot O$ 的极线.

设直线 $A D, B C$ 交于点 $L$, 则由密克点的性质知, $O J$ 与点 $J$ 关于 $\odot O$ 的极线 $E F$ 的交点 $H$ 为完全四边形 $A B C D K L$ 的密克点.

故 $B, C, H, K$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_7645b011da5bd004a006g-3.jpg?height=499&width=682&top_left_y=750&top_left_x=687)

又因为直线 $A C$ 过点 $J$, 由配极定理, $\odot O$ 在点 $A$ 处的切线, 在点 $C$ 处的切线及直线 $E F$ 三线共点.

又由 $A B \cdot C D=B C \cdot A D$ 知四边形 $A B C D$ 为调和四边形. 故 $\odot O$ 在点 $A$处的切线, 在点 $C$ 处的切线以及直线 $B D$ 三线共点.

从而上述三条直线与直线 $E F$ 四线共点, 且交点为 $E$. 于是有

$$
\angle O C E=90^{\circ} ; O E \perp A C .
$$

设直线 $O E, F A$ 交于点 $M$, 则 $O, M, H, F$ 四点共圆.

于是由射影定理, $E C^{2}=E M \cdot E O=E H \cdot E F=E T^{2}$. 故 $E C=E T$.

同理, $F B=F T$.

综合 (1), (2), 我们将条件转化为了题 3 的条件.

结合题 3 的证明知题 1 的结论成立.

依据题 3 中 $K$ 点的不关于 $\angle E T F$ 的性质, 可将题 3 改编为题 4 .

题 4. 在锐角 $\triangle O E F$ 中, 以 $O E$ 为直径的圆 $\Gamma_{1}$ 分别与边 $E F, O F$ 交于点 $H, N$. 以 $O F$ 为直径的圆 $\Gamma_{2}$ 分别与边 $E F, O E$ 交于点 $H, M . E N$ 的延长线交圆 $\Gamma_{2}$ 于点 $D, F M$ 的延长线交圆 $\Gamma_{1}$ 于点 $A, \triangle A H D$ 的外接圆交 $E F$ 于点 $H, K$. 证明: $\triangle M N K$ 的外接圆与直线 $E F$ 相切.

证明 设线段 $E N, F M$ 分别与圆 $\Gamma_{2}$, 圆 $\Gamma_{1}$ 交于点 $B, C$,

![](https://cdn.mathpix.com/cropped/2024_02_26_7645b011da5bd004a006g-4.jpg?height=454&width=691&top_left_y=207&top_left_x=682)

显然, $O H, E N, F M$ 为 $\triangle O E F$ 的三条高. 于是有

$$
O M \cdot O E=O N \cdot O F
$$

又 $O E, O F$ 分别为圆 $\Gamma_{1}$, 圆 $\Gamma_{2}$ 的直径, 则由射影定理,

$$
O B^{2}=O N \cdot O F=O D^{2} ; O A^{2}=O M \cdot O E=O C^{2} .
$$

从而

$$
O A=O B=O C=O D .
$$

即 $A, B, C, D$ 四点共圆于以 $O$ 为圆心的圆上. 因此

$$
\begin{aligned}
\angle O D K & =\angle O D A+\angle A D K \\
& =\left(90^{\circ}-\frac{1}{2} \angle A O D\right)+\angle A H E \\
& =90^{\circ}-\frac{1}{2} \angle A O D+\frac{1}{2} \angle A O C \\
& =90^{\circ}-\frac{1}{2} \angle D O C \\
& =\angle O D C .
\end{aligned}
$$

故 $K, C, D$ 三点共线.

同理, $K, A, B$ 三点共线.

则由 $A, B, C, D$ 四点共圆知 $\triangle K A C \sim \triangle K B D$.

又由 $O E \perp A C, O F \perp B D$ 得点 $M, N$ 分别为线段 $A C, B D$ 的中点. 故

$$
\triangle K M C \sim \triangle K N B .
$$

所以 $\angle K M C=\angle K N B$, 故

$$
\angle K M E=90^{\circ}-\angle K M C=90^{\circ}-\angle K N B=\angle K N F \text {. }
$$

因此

$$
\begin{aligned}
\angle K M N & =180^{\circ}-\angle O M N-\angle E M K \\
& =180^{\circ}-\angle O F E-\angle F N K
\end{aligned}
$$

$$
=\angle N K F \text {. }
$$

故 $\triangle K M N$ 的外接圆与直线 $E F$ 相切.

题 4 的条件与题 1 的条件也是等价的.

模仿题 4 的证明, 得到题 1 的另一个证明.

题 1 证法二 设 $O J, O E, O F$ 分别交 $E F, A C, B D$ 于点 $H, M, N$.

![](https://cdn.mathpix.com/cropped/2024_02_26_7645b011da5bd004a006g-5.jpg?height=502&width=685&top_left_y=654&top_left_x=688)

同证明 1 知, $O E \perp A C, O F \perp B D$, 且 $M, N$ 分别为线段 $A C, B D$ 的中点.

由于 $A, B, C, D$ 四点共圆, 故 $\triangle K A C \sim \triangle K B D$. 因此 $\triangle K M C \sim \triangle K N B$.即 $\angle K M C=\angle K N B$. 从而 $\angle K M E=\angle K N F$, 于是 $\angle K M N=\angle N K F$. 即 $\triangle K M N$ 的外接圆与 $E F$ 相切.

则由正弦定理及射影定理，

$$
\begin{aligned}
\left(\frac{E K}{F K}\right)^{2} & =\frac{\sin \angle E M K \cdot \frac{M K}{\sin \angle M E K}}{\sin \angle F N K \cdot \frac{N K}{\sin \angle N F K}} \cdot \frac{\sin \angle E M K \cdot \frac{E M}{\sin \angle M K E}}{\sin \angle F N K \cdot \frac{F N}{\sin \angle N K F}} \\
& =\frac{\sin \angle N F K}{\sin \angle M E K} \cdot\left(\frac{M K}{N K} \cdot \frac{\sin \angle N K F}{\sin \angle M K E}\right) \cdot \frac{E M}{F N} \\
& =\frac{O E}{O F} \cdot 1 \cdot \frac{\cos \angle M E F}{\cos \angle N F E} \\
& =\frac{E H}{F H}=\left(\frac{E T}{F T}\right)^{2}
\end{aligned}
$$

故

$$
\frac{E K}{F K}=\frac{E T}{F T} .
$$

由角平分线定理的逆定理知 $K T$ 平分 $\angle E T F$.

需要指出的是, 证明 1 以及证明 2 (尤其是证明 1) 并不是自然的, 但它们对图形挖掘得比较透彻, 并且联系了多个题目, 对掌握题 1 的图形是有很大帮助的.

题 1 还有一些不依赖于题 3 及题 4 的证明, 这里不再一一给出.

## 参考文献

[1] 熊斌 提供. 第 53 届 IMO 试题解答 [J]. 中等数学, 2012.09.

[2] 冯祖鸣提供, 李建泉 翻译. 2013 美国国家队选拔考试 [J]. 中等数学, 2014.08.

