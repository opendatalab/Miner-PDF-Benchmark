数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 几道国家集训队平面几何题的命题经历 

何忆捷 林天齐

(华东师范大学数学系, 200241)

我们先来看几组有趣的图片:
![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-01.jpg?height=400&width=1148&top_left_y=928&top_left_x=480)

图 1: 海螺
![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-01.jpg?height=318&width=1242&top_left_y=1502&top_left_x=410)

图 2：省鱼
![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-01.jpg?height=500&width=1148&top_left_y=1986&top_left_x=474)

图 3: 风车

收稿日期: 2016-05-31; 修订日期: 2016-06-15.
![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-02.jpg?height=426&width=1298&top_left_y=202&top_left_x=412)

图 4: 蜗牛
![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-02.jpg?height=456&width=1228&top_left_y=780&top_left_x=424)

图 5：帆船

以上每组图片中, 左侧的图正是今年中国国家集训队测试题的图形 (见文献 $[1,2]$ ). 有意思的是, 在集训队前期准备与命题讨论中, 我们发现这些图形似乎均有生动的实物特征, 便给它们取了 “海螺”、“风车” 等代号, 以方便讨论. 实际上, 除了 “鲨鱼” 这一代号是事后补上的, 其余代号已为本届集训队教练组所熟知.

这 5 道题中，“海螺”、“鲨鱼”、“蜗牛”、“帆船” 是本文两位作者的创作与讨论成果. 下面依次介绍这 4 道题的由来.

## 1. “海螺” 的来历

创作本题的原始想法是: 在 $\triangle A B C$ 的边 $B C$ 上取一点 $D$, 外接圆弧 $\widehat{B C}$ 上取点 $E, F$, 使得 $\triangle D E F$ 与 $\triangle A B C$ 具有位似关系, 考虑此时点 $D$ 的性质.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-02.jpg?height=334&width=349&top_left_y=2220&top_left_x=859)

图 1-1
笔者试图用 $\triangle A B C$ 的基本量来表示 $\frac{B D}{D C}$, 以刻画点 $D$ 的位置, 但发现结果十分复杂. 这时突然想尝试一下, 如果在 $\overparen{A B}, \widehat{A C}$ 所在弓形内, 按类似方式取出两个与 $\triangle A B C$ 位似的三角形, 并设它们在边 $A B, A C$ 上的顶点分别是 $X, Y$, 那么 $A D, B Y, C X$ 三线是否共点? 换言之, $\frac{B D}{D C}, \frac{C Y}{Y A}, \frac{A X}{X B}$ 这三个复杂式子的乘积有没有可能恰好可约分?

笔者试图通过几何画板作近似图 (鉴于 $D, X, Y$ 的刻画比较麻烦) 来排除这种可能性, 但反而越来越觉得像共点, 便将精度调细, 尺寸调大, 并使三边长度两两相差较大, 几经拖动观察后, 确信结论并不正确 (下图是笔者的实验数据).

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-03.jpg?height=802&width=1056&top_left_y=810&top_left_x=500)

图 1-2

于是笔者另起炉灶. 鉴于 $\triangle A B C$ 与 $\triangle D E F$ 位似, 如果再反向延长 $D F$, $D E$, 与 $\triangle A B C$ 的外接圆分别交于点 $P, Q$, 那么就有 $\overparen{A P}=\widehat{C F}=\widehat{B E}=\widehat{A Q}$.再取出 $\widehat{B C}$ 的中点 $M$, 那么 $(D P, D A, D Q)$ 与 $(D E, D M, D F)$ 似乎具有某种对等关系.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-03.jpg?height=491&width=502&top_left_y=2053&top_left_x=777)

图 1-3
经过思考发现, 还需补上一个条件 $\overparen{P Q}=\overparen{E F}$, 方可产生对称关系, 进而得到 $\angle B A D=\angle A D Q=\angle M D F, \angle C A D=\angle A D P=\angle M D E$. 通过条件的修饰,便初步得到如下问题:

问题 1.1 在圆内接六边形 $A B E M F C$ 中, $B E=E M=M F=F C$, 过 $E, F$ 分别作 $A B, A C$ 的平行线, 两者交于点 $D$. 若 $D$ 恰好在线段 $B C$ 上, 证明: $\angle B A D=\angle M D F$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-04.jpg?height=472&width=506&top_left_y=672&top_left_x=772)

图 1-4

该问题相对容易, 那么它的逆命题是否也成立? 难度如何?

若隐去平行关系, 并将 $\angle B A D=\angle M D F, \angle C A D=\angle M D E$ 作为条件给出, 那么可以反过来证得两组平行关系. 但如果直接要求证明 $A B / / D E$, 相当于给出了如何刻画 $D$ 的提示, 这样题目的难度上升不明显. 因此再进行探索, 同时修改了题目中的字母, 得到如下两种 “版本”：

问题 1.2 在圆内接六边形 $A B C D E F$ 中, $A B=B C=C D=D E$. 若线段 $A E$ 内一点 $K$ 满足 $\angle B K C=\angle K F E, \angle C K D=\angle K F A$, 证明: $A B, F K, D E$三线共点.

问题 1.3 在圆内接六边形 $A B C D E F$ 中, $A B=B C=C D=D E$. 若线段 $A E$ 内一点 $K$ 满足 $\angle B K C=\angle K F E, \angle C K D=\angle K F A$, 证明: $K C=K F$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-04.jpg?height=469&width=474&top_left_y=2084&top_left_x=791)

图 1-5
最终教练组选择了问题 1.3 作为集训队测试题. 为增加图形的活泼性, 在作图时让 $A E$ 有所倾斜, 而 $K A, K B, K C, K D, K E$ 逐渐伸展, 犹如海螺的形态 (如图 1-5).

## 2. “鲨鱼”的来历

在任意三角形中, 三条内角的平分线交于一点一内心. 然而在四边形里,仅有圆外切四边形具有类似性质. 笔者将 “圆外切四边形” 的性质弱化, 研究一般情形下四边形各内角平分线产生的交点的性质, 随后又添加了 “四边形有外接圆” 这一条件, 这样便能通过圆弧的相等, 从侧面反映 “角平分线” 这一属性, 使各几何对象之间的关联性质较为丰富.

不难发现, 下图中圆内接四边形 $A B C D$ 各内角平分线围成的凸四边形有外接圆. 其证明不难, 且这一性质本质上并不依赖于四边形 $A B C D$ 是否有外接圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-05.jpg?height=463&width=500&top_left_y=1205&top_left_x=778)

图 2-1

笔者转向一个更有意思的问题一如果考虑对角的角平分线的交点, 这样的交点有什么样的性质呢?

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-05.jpg?height=414&width=500&top_left_y=1963&top_left_x=778)

图 2-2

如图所示, $I, J$ 就是要研究的新点. 不妨将直线 $I J$ (记为 $l$ ) 作为研究的对象. 为了更充分地利用圆的性质, 将四个内角的角平分线延长, 与圆 $O$ 产生四个
交点 $A_{1}, B_{1}, C_{1}, D_{1}$, 易知它们是一个矩形的四个顶点.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-06.jpg?height=460&width=782&top_left_y=301&top_left_x=637)

图 2-3

通过几何画板明显可以发现, 直线 $l$ 与四边形 $A B C D$ 四边所在直线的交点实际上在矩形 $A_{1} B_{1} C_{1} D_{1}$ 的四边所在直线上. 至此已隐含地得到了如下结论:

问题 2.1 四边形 $A B C D$ 内接于圆 $O, \angle A, \angle C$ 的平分线相交于点 $I$, $\angle B, \angle D$ 的平分线相交于点 $J, C I, D J$ 的延长线与圆 $O$ 分别交于点 $C_{1}, D_{1}$. 证明: $A B, C_{1} D_{1}, I J$ 三线共点或相互平行.

起初笔者给出了一个复数证明, 后来又发现了一种笛沙格定理的巧妙证法.

问题 2.1 中, 点 $C_{1}, D_{1}$ 对解题的提示较强. 为了隐藏矩形 $A_{1} B_{1} C_{1} D_{1}$, 取 $P R$ 的中点 $M$, 则直线 $O M$ 与矩形的一边平行; 取 $Q S$ 的中点 $N$, 则 $O N$ 与矩形的另一边平行. 这样便得到 $O M \perp O N$. 至此 “鲨鱼” 的形状初现端倪, 而 $O M, O N$ 则如一对锋利的牙齿. 笔者将问题整理如下:

问题 2.2 如图 2-4, 四边形 $A B C D$ 内接于圆 $O, \angle A, \angle C$ 的平分线相交于点 $I, \angle B, \angle D$ 的平分线相交于点 $J$, 直线 $I J$ 不经过点 $O$, 且与边 $A B, C D$ 的延长线分别交于点 $P, R$, 与边 $B C, D A$ 分别交于点 $Q, S$. 线段 $P R, Q S$ 的中点分别为 $M, N$. 证明: $O M \perp O N$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-06.jpg?height=426&width=702&top_left_y=2037&top_left_x=677)

图 2-4

## 3. “蜗牛” 的来历

本题源于对双圆四边形的研究. 起初是考虑双圆四边形内切圆在一边上的切点具有哪些性质, 通过探索切点在内切圆上的对径点, 偶然发现了如下结论:

问题 3.1 如图 3-1, 在双圆四边形 $A B C D$ 中, $T$ 是内切圆 $\omega$ 在 $C D$ 边上的切点, $T U$ 是 $\omega$ 的直径, $P$ 是对角线 $A C, B D$ 的交点, $S U$ 是 $\omega$ 内过点 $P$ 的弦.证明: $\triangle S A B$ 的外接圆 $\pi$ 与圆 $\omega$ 相切于点 $S$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-07.jpg?height=617&width=574&top_left_y=731&top_left_x=747)

图 3-1

该结论是对双圆四边形切点性质的一个刻画. 笔者借助 “阿波罗尼斯圆”的相关知识给出了该结论的证明.

接下来进行的改造是重新刻画点 $S$ 的性质一将 $\pi$ 描述成: “过点 $A, B$, 且与 $\omega$ 相切的圆” (可以证明这样的圆是唯一确定的), 将证明的结论改述成垂直关系: $S P \perp S T$, 这样就可以达到隐藏直径 $T U$ 的目的 (不过这种描述对于利用相切两圆位似来解决问题提供了便利). 至此形成如下问题:

问题 3.2 在双圆四边形 $A B C D$ 中, $T$ 是内切圆 $\omega$ 在 $C D$ 边上的切点, $P$是对角线 $A C, B D$ 的交点, 一个圆 $\pi$ 经过 $A, B$ 两点, 且与圆 $\omega$ 内切于点 $S$. 证明: $S P \perp S T$.

此后, 考虑到题目的图形过于拥挤, 不够舒展美观, 便通过类比, 将 “内切圆”改为 “旁切圆”，提出下述问题:

问题 3.3 如图 3-2, 圆内接四边形 $A B C D$ 的对角线相交于点 $P$, 存在一个圆 $\Gamma$ 与 $A B, B C, A D, D C$ 的延长线分别相切于点 $X, Y, Z, T$. 圆 $\Omega$ 经过 $A, B$ 两点, 且与圆 $\Gamma$ 外切于点 $S$. 证明: $S P \perp S T$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-08.jpg?height=557&width=717&top_left_y=201&top_left_x=675)

图 3-2

经过验证, 问题 3.3 的结论仍是正确的, 证明思路与问题 3.2 相仿. 这样, 蜗牛便从壳里探出脑袋, 与集训队队员正式见面了.

## 4. “帆船” 的来历

本题创作的原始想法是: 在圆内接四边形 $A B C D$ 中, 研究 $\triangle A B C, \triangle A D C$的内心 $I, J$ 所具有的性质.

笔者考虑 “ $B, I, J, D$ 四点共圆” 的等价命题. 通过角度计算发现, 这等价于 $I J \perp A C$, 进而又等价于 $A B C D$ 有内切圆, 即 $A B C D$ 是双圆四边形. 于是得到一个相对平凡的问题:

问题 4.1 如图 4-1, 在圆内接四边形 $A B C D$ 中, $I, J$ 分别为 $\triangle A B C, \triangle A D C$的内心. 证明: $A B C D$ 有内切圆, 当且仅当 $B, I, J, D$ 四点共圆或共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-08.jpg?height=465&width=502&top_left_y=1778&top_left_x=774)

图 4-1

由于圆内接四边形 $A B C D$ 中关于 $\triangle A B C, \triangle B C D, \triangle C D A, \triangle D A B$ 的内心的关联性质早已有不少结果, 笔者一直没想到新的命题突破口. 经过长时间的盲目状态后, 突然意识到, 本图形的性质曾在自己改编的一个问题中出现过!
问题 4.2 如图 4-2, 在锐角 $\triangle A B C$ 中, $A B>A C, I$ 为内心, $I D \perp B C$ 于点 $D, I D$ 延长线上一点 $E$ 满足 $\angle B E C=180^{\circ}-\frac{1}{2} \angle B A C$, 线段 $A I$ 内一点 $F$ 满足 $\angle B F C=90^{\circ}$. 证明: $A, F, D, E$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-09.jpg?height=442&width=488&top_left_y=453&top_left_x=790)

图 4-2

问题 4.2 当时是从下述题目改编的:

问题 4.3 如图 4-3, 在锐角 $\triangle A B C$ 中, $A B>A C, I$ 为内心, 线段 $I D$ 与 $B C$ 垂直相交, 且满足 $\angle I B D+\angle I C D=90^{\circ}$. 作 $D P \perp B I$ 于点 $P, D Q \perp C I$ 于点 $Q$. 证明: $\angle B A P=\angle I A Q$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-09.jpg?height=449&width=506&top_left_y=1386&top_left_x=775)

图 4-3

在改编过程中, 问题 4.2 中对点 $E, F$ 的刻画 “ $\angle B E C=180^{\circ}-\frac{1}{2} \angle B A C$ ”及 “ $\angle B F C=90^{\circ}$ ” 令笔者印象颇深. 仔细对比发现, 问题 4.1 中 “ $I$ 为 $\triangle A B C$的内心” , “ $I J \perp A C$ ”, 以及 “ $\angle A J C=90^{\circ}+\frac{1}{2} \angle A D C=180^{\circ}-\frac{1}{2} \angle A B C$ ” 这样的性质, 与问题 4.2 的图形性质刚好匹配.

于是在问题 4.1 的基础上, 作以 $A C$ 为直径的圆, 与射线 $I B, J D$ 分别交于点 $X, Y$, 并记 $I J \perp A C$ 于点 $P$ (如图 4-4 所示), 那么可以推出 $B, X, P, J$ 四点共圆, 且同理得 $D, Y, I, P$ 四点共圆.

结合 $B, I, J, D$ 共圆, 进一步可知, $\angle I P X=\angle I B J=\angle I Y J=\angle J P Y$, 这也等价于 $X, Y$ 关于 $A C$ 对称. 至此发现了以下结论:

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-10.jpg?height=508&width=577&top_left_y=200&top_left_x=748)

图 4-4

问题 4.4 如图 4-5, 圆内接四边形 $A B C D$ 中, $A B>B C, A D>D C, I, J$分别是 $\triangle A B C, \triangle A D C$ 的内心. 以 $A C$ 为直径的圆与线段 $I B$ 交于点 $X$, 与 $J D$的延长线交于点 $Y$. 证明: 若 $B, I, J, D$ 共圆, 则 $X, Y$ 关于 $A C$ 对称.

![](https://cdn.mathpix.com/cropped/2024_02_26_c834e3bcda7b72fdcec1g-10.jpg?height=503&width=580&top_left_y=1125&top_left_x=744)

图 4-5

在问题 4.4 中, “ $A B>B C, A D>D C$ ” 仅用于限定图形位置关系, 而非本质条件. 图 4-5 十分简洁, $\triangle A B C, \triangle A D C$ 胜似两片风帆. 在问题 4.3 与问题 4.2 的助推下, “帆船” 扬帆起航!

## 参考文献

[1] Telv Cohl, 2016 年中国国家队选拔考试平面几何试题评析 [J]. 数学新星网.学生专栏, 2016-04-13 期.

[2] 熊斌, 2016 中国国家集训队选拔考试 [J]. 中等数学, 2016-05 期, 23-27.

