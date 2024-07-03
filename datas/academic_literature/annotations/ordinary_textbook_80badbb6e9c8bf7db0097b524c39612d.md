# 一个几何问题的再探讨 

王安睿

(清华大学附属中学, 100084)

本文将主要讨论如下的 “四内心共圆”命题, 记录笔者对这个题目的一些思考, 综合整理了一些关于这个问题的结果, 并尝试给出其的一种证明:

命题 1 如图 1, 圆外切四边形 $A B C D$ 中, 内切圆圆心为 $I$, 点 $P$ 为平面上一点, 设 $\angle A P C$ 的内角平分线与线段 $A C$ 交于点 $Q, \angle B P D$ 的内角平分线与线段 $B D$ 交于点 $R$. 若 $Q 、 I 、 R$ 共线(允许重合), 则 $\triangle P A B 、 \triangle P B C$ 、 $\triangle P C D 、 \triangle P D A$ 的内心共圆.
![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-01.jpg?height=626&width=1086&top_left_y=1366&top_left_x=496)

图 1

这里画两张图的原因我们在之后将尝试进行解释(和下文第 1 部分的分类有关).

全文主要分 4 个部分:

第 1 部分中我们将所有满足命题 1 条件的平面上的点 $P$ 分成两类(这么做的原因主要是我们发现这两类点各自具有独特的性质, 而它们之间又有密切的联系).

修订日期: 2021-10-11.
第 2、3 部分分别对这两类点做一些讨论, 并给出命题 1 的一种证明方法.

第 4 部分补充一些相关的结论供有兴趣的读者参考.

由于笔者水平有限, 不当之处恳请读者指正.

## 几点说明

一、阅读本文不需要特别的前置知识, 但希望读者能提前了解如下一些内容, 它们在后文中将多次用到(本文暂不给出证明, 用到的时候会指出):

1. 等角共轭点(等角线)的概念与基本性质, 如: 一个点关于三角形三边的对称点所构成的三角形的外心是这个点关于三角形的等角共轭点, 等等.
2. 圆外切四边形(本文均假设是凸四边形)的基本性质, 如: 对边之和相等、牛顿定理(圆外切四边形对角线中点的连线过内切圆圆心), 等等.
3. 三弦定理(托勒密定理).
4. 圆内接四边形密克点的基本性质. 具体如下, 这里对点的记号仅在此处使用:

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-02.jpg?height=651&width=720&top_left_y=1342&top_left_x=682)

图 2

如图 2, 设凸四边形 $A B C D$ 内接于圆 $O$, 直线 $A B 、 C D$ 交于点 $E$. 直线 $A D 、 B C$ 交于点 $F$, 线段 $A C 、 B D$ 交于点 $G$. 设四边形 $A B C D$ 的密克点为点 $H$. 则我们有:

$4.1 H$ 在直线 $E F$ 上, $H$ 在直线 $O G$ 上.

$4.2 O G \perp E F$.

$4.3 B 、 O 、 D 、 H$ 四点共圆.且 $A 、 O 、 C 、 H$ 四点共圆.
二、为便于行文, 在此我们作如下约定:

1. 本文将边分析边证明, 尝试介绍整个命题的证明思路.
2. 本文的证明过程中处理角度关系时暂不采用多值有向角的叙述方式, 处理长度关系时(如梅涅劳斯定理等)暂不采用有向线段的形式.这使得本文的大多证明过程都 “依赖”于具体的图形, 但我们认为这些证明是可以适用于一般情形的, 只要做适当的修正即可(如把角相等改成互补, 等等).
3. 本文中的字母标记以当处说明为准.但一般的, 我们记四边形 $A B C D$ 表示命题 1 中的圆外切四边形, 点 $I$ 为其内切圆圆心.点 $P$ 为平面上一点, 点 $Q$ 表示 $\angle A P C$ 内角平分线与线段 $A C$ 的交点, 点 $R$ 表示 $\angle B P D$ 内角平分线与线段 $B D$ 的交点. 点 $M$ 在直线 $A C$ 上使 $A 、 Q 、 C 、 M$ 成调和点列, 点 $N$ 在直线 $B D$ 上使 $B 、 R 、 D 、 N$ 成调和点列. (中点均对应无穷远点)
4. 当点 $X 、 Y 、 Z$ 三点共线时 ( $Y$ 在线段 $X Z$ 上), 规定退化的 $\triangle X Y Z$ 的内心为点 $Y$.

## 第 1 部分: 分类

本部分我们将给出具体的分类方法. 这里先要提供一种作出所有满足命题 1 条件的点 $P$ 的作图方法, 而在作图的过程中, 我们会看到分类的依据.

## 一种作图方法

首先我们发现, 想直接确定出什么样的点 $P$ 能使得 $Q 、 I 、 R$ 共线是不容易的, 所以在作图时将条件反过来, 即先使 $Q 、 I 、 R$ 共线, 再得到点 $P$ (通过构造阿波罗尼兹圆取交点的方式).

具体方法如下: (如图 3)

第一步: 过点 $I$ 作直线 $k$ 分别与线段 $A C 、 B D$ 交于点 $Q 、 R$.

第二步: 在直线 $A C 、 B D$ 上分别取点 $M 、 N$, 使得 $A 、 Q 、 C 、 M$ 成调和点列, 而 $B 、 R 、 D 、 N$ 成调和点列.

注 1. 当点 $Q 、 R$ 不为 $A C 、 B D$ 中点时, 这总是可以做到的.若点 $Q 、 R$ 同时为 $A C 、 B D$ 中点 (牛顿定理保证), 我们不妨取 $M 、 N$ 为无穷远点, 具体说明见本部分最后的内容。

2. 取出点 $M 、 N$ 作图方法见本文最后的附录二.

第三步: 分别以线段 $Q M 、 R N$ 为直径作圆, 取点 $P$ 为两圆交点. 由阿波罗尼兹圆的基本性质, 我们知道 $P Q$ 为 $\angle A P C$ 的内角平分线而 $P R$ 为 $\angle B P D$ 的

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-04.jpg?height=611&width=930&top_left_y=243&top_left_x=583)

图 3

内角平分线, 又此时 $Q 、 I 、 R$ 共线, 故这样得到的点 $P$ 是满足命题 1 条件的.

说明: 容易看出, 这种方法可以作出所有满足命题 1 条件的点 $P$. 而在第三步中我们可以先认为两圆一定有两个交点.(点 $P$ 轨迹如图 4, 其实是一条三次曲线的一部分和一条四次曲线的一部分拼接在一起的)

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-04.jpg?height=780&width=871&top_left_y=1346&top_left_x=524)

图 4

下面我们开始进行分类, 这么做的原因主要因为在图 3 中, 我们发现直线 $k$ 其实会经过两圆的某个交点(即图 3 中 $P_{2}$ ), 这个性质是值得注意的.

## 分类方法

为把问题较为严谨的说清楚, 我们将重新定义点 $P_{2}$. 在此先证明如下两个
引理:

引理 1 如图 5, 圆外切四边形 $A B C D$ 中, $I$ 为内切圆圆心.点 $P$ 为形外一点, 则:

$$
\angle C P I=\angle A P I \Leftrightarrow \measuredangle A P B=\measuredangle D P C \Leftrightarrow \angle B P I=\angle D P I
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-05.jpg?height=608&width=822&top_left_y=621&top_left_x=614)

图 5

注 这个引理其实只是圆外切四边形的一个性质，读者可以给出自己的证明. 如直接利用圆外切四边形巨龙曲线(斜环索线)的相关结论即可, 但本文暂不采用这种写法, 而是直接进行三角函数的计算, 仅供参考.

证明 我们只考虑右侧的情形, 左侧的证明完全类似.注意到:

$$
\measuredangle A P B=\measuredangle D P C
$$

等价于：

$$
\frac{P C \cdot \sin \angle C P B}{P C \cdot \sin \angle C P D}=\frac{P A \cdot \sin \angle A P D}{P A \cdot \sin \angle A P B}
$$

等价于：

$$
\frac{B C \cdot \sin \angle C B P}{C D \cdot \sin \angle C D P}=\frac{A D \cdot \sin \angle A D P}{A B \cdot \sin \angle A B P}
$$

等价于：

$$
A B \cdot B C \cdot \sin \angle A B P \cdot \sin \angle C B P=A D \cdot C D \cdot \sin \angle C D P \cdot \sin \angle A D P
$$

等价于(积化和差公式):

$A B \cdot B C \cdot[\cos \angle A B C-\cos (2 \angle I B P)]=A D \cdot C D \cdot[\cos \angle A D C-\cos (2 \angle I D P)]$
等价于(移项):

$$
\begin{array}{r}
A B \cdot B C \cdot \cos \angle A B C-A D \cdot C D \cdot \cos \angle A D C \\
=A B \cdot B C \cdot \cos (2 \angle I B P)-A D \cdot C D \cdot \cos (2 \angle I D P)
\end{array}
$$

等价于(二倍角公式):

$$
\begin{aligned}
& A B \cdot B C \cdot 2 \cdot \sin ^{2} \angle I B P-A D \cdot C D \cdot 2 \cdot \sin ^{2} \angle I D P \\
&=A B \cdot B C \cdot(1-\cos \angle A B C)-A D \cdot C D \cdot(1-\cos \angle A D C)
\end{aligned}
$$

等价于:

$$
\begin{aligned}
& A B \cdot B C \cdot 2 \sin ^{2} \angle I B P-A D \cdot C D \cdot 2 \sin ^{2} \angle I D P \\
& =\frac{1}{2}\left[A C^{2}-(A B-B C)^{2}-A C^{2}+(A D-D C)^{2}\right]=0
\end{aligned}
$$

等价于:

$$
\frac{\sin ^{2} \angle I B P}{\sin ^{2} \angle I D P}=\frac{A D \cdot C D}{A B \cdot B C}
$$

由圆外切四边形基本性质知(利用正弦定理即可):

$$
\frac{A D \cdot C D}{A B \cdot B C}=\frac{I D^{2}}{I B^{2}}
$$

故得:

$$
\measuredangle A P B=\measuredangle D P C \Leftrightarrow \frac{\sin \angle I B P}{\sin \angle I D P}=\frac{I D}{I B}
$$

这表明:

$$
\measuredangle A P B=\measuredangle D P C \Leftrightarrow \angle B P I=\angle D P I
$$

引理得证!

由引理 1 我们可以得到如下引理 2 :

引理 2 如图 6, 圆外切四边形 $A B C D$ 中, 内切圆圆心为 $I$, 过点 $I$ 作直线 $k$ 分别与线段 $A C 、 B D$ 交于点 $Q 、 R$ (均不为中点). 在直线 $A C 、 B D$ 上分别取点 $M 、 N$, 使得 $A 、 Q 、 C 、 M$ 成调和点列, 而 $B 、 R 、 D 、 N$ 成调和点列.则有: 直线 $k \perp M N$.

证明 这的证明只需用到阿波罗尼兹圆的基本性质(调和点列 + 垂直得到角平分线), 并利用同一法及引理 1 即可.

至此, 我们可以给出如下的分类定义: (如图 7)

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-07.jpg?height=694&width=916&top_left_y=261&top_left_x=567)

图 6

定义 1 设过三点 $I 、 R 、 Q$ 的直线 $k$ 与直线 $M N($ 定义同引理 2 )交于点 $P_{2}$. 由引理 2 得: $P_{2} Q$ 为 $\angle A P_{2} C$ 的内角平分线, 同时 $P_{2} R$ 为 $\angle B P_{2} D$ 的内角平分线. 则点 $P_{2}$ 是满足命题 1 条件的, 我们把这样得到的点 $P_{2}$ 称为共线类的.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-07.jpg?height=643&width=920&top_left_y=1409&top_left_x=568)

图 7

定义 2 已知共线类点 $P_{2}$ 在以线段 $R N$ 为直径的圆上, 也在以线段 $Q M$ 为直径的圆上. 设这两个圆的另一个交点为点 $P_{1}$, 则 $P_{1}$ 也是满足命题 1 条件的，我们把这样得到的点 $P_{1}$ 称为非共线类的.

定义 3 我们称定义 1 与定义 2 中所得的两个满足命题 1 条件的点 $P_{1} 、 P_{2}$ 是相伴的.
到此, 我们完成了对平面上所有满足命题 1 条件的点 $P$ 的分类, 这为我们后面的分析奠定了基础.

注 1. 我们把线段 $A C 、 B D$ 中垂线的交点 $P^{\prime \prime}$ 归到非共线类的, 并记点 $P^{\prime \prime}$ 与某个无穷远点相伴(我们认为这是合理的, 但后面如果要取出某个非共线类点所相伴的共线类点来分析时，我们都会对其为中垂线的交点这一特殊情形单独讨论).

2. 注意四边形 $A B C D$ 的四个顶点既是共线类也是非共线类的.

## 第 2 部分: 共线类

本部分我们将对点 $P$ 是共线类的这一种情形来证明命题 1.(这里我们约定,在本部分中, 点 $P$ 都是共线类的)

首先由共线类的定义, 我们可以看出, 此时点 $P$ 具有如下性质:

性质 $1 P$ 一定在凸四边形 $A B C D$ 形外.

性质 2 直线 $P I$ 同时为 $\angle A P C 、 \angle B P D$ 的内角平分线, 即 $P 、 I 、 Q 、 R$四点共线(这是重要的), 记为直线 $k$.

性质 $3 \measuredangle A P B=\measuredangle D P C$.

接下来我们将对点 $P$ 的性质做进一步的探索.

通过作图(画出四内心所在圆的作图过程), 我们会立刻发现: “四内心所在圆的圆心 (记为 $O$ ) 也在直线 $k$ 上”.

又经过一定量的尝试, 我们还会发现: “四内心组成的四边形对角线的交点(记为 $J$ )也在直线 $k$ 上”.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-08.jpg?height=580&width=1105&top_left_y=1926&top_left_x=470)

图 8
现在总结一下我们通过作图发现但还未证明的点 $P$ 的性质：(如图 8)

性质 4 四内心共圆. (这是命题 1)

性质 5 四内心所在圆的圆心 $O$ 也在直线 $k$ 上.

性质 6 四内心组成的四边形对角线的交点 $J$ 也在直线 $k$ 上.

下面我们尝试对这三条性质进行证明:

由于这些性质具有高度的对称性, 即四个内心的地位是“基本”对等的, 所以笔者一直考虑如何整体的刻画这四个内心所构成的四边形来证明.经过一段时间的思考, 并不能给出有效的方式, 没有实质性的进展.

但当我们把目光仅仅聚焦在整个图形的一个局部时, 问题似乎便迎刃而解了？而答案就藏在图中一系列的角度关系中(等角共轭).

具体对于角度关系的分析如下:

首先设 $\triangle P B C 、 \triangle P C D 、 \triangle P D A$ 的内心分别为点 $G 、 E 、 F$. 我们暂时只考虑这三个内心, 确切的说, 先只考虑点 $E 、 F$ 和 $\triangle P I D$.(如图 9)

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-09.jpg?height=602&width=874&top_left_y=1338&top_left_x=608)

图 9

由本部分性质 2 知, 直线 $P I$ 为 $\angle A P C$ 内角平分线, 则

$$
\angle E P I=\frac{1}{2} \angle A P C-\frac{1}{2} \angle D P C=\frac{1}{2} \angle A P D=\angle F P D,
$$

即直线 $P E 、 P F$ 关于 $\angle I P D$ 成等角线. 又有: $\angle I D F=\frac{1}{2} \angle A D C+\frac{1}{2} \angle A D P$. 故

$$
\angle I D F+\angle E D P=\frac{1}{2}(\angle A D C+\angle A D P+\angle C D P)=180^{\circ} .
$$

即直线 $D E 、 D F$ 关于 $\angle I D P$ 成等角线.

故: 点 $E 、 F$ 关于 $\triangle I P D$ 等角共轭.
同样考虑知: 点 $E 、 G$ 关于 $\triangle I P C$ 等角共轭. (如图 10 )

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-10.jpg?height=679&width=943&top_left_y=320&top_left_x=565)

图 10

然后其实我们可以暂时降低证明的目标, 即先不去证四个内心的性质, 而是证明三个内心的性质 (一步一步来). 通过比对想要证明的目标性质 $4 、 5$, 我们可以先尝试证明如下一个命题:

命题 $2 \triangle E F G$ 的外心在直线 $P I$ 上.

而由上面关于等角共轭的分析, 我们发现, 其实可以将 $\triangle P D C$ 、点 $E 、 F 、 G$ 及直线 $P I$ 从整个大的结构中抽取出来单独进行处理(即消去其余所有的点而不影响我们的思考).

具体写出来便是本部分中最为关键而精彩的一个引理.

引理 3 如图 11, 在 $\triangle X Y Z$ 中, $T$ 为内心, $W$ 为平面上任一点(其实对位置有一定的要求, 如不在三边上, 但这里不展开细节了), 点 $T$ 关于 $\triangle X Y W$ 、 $\triangle X Z W$ 的等角共轭点分别为点 $U 、 V$. 设 $\triangle U V T$ 外心为 $S$. 则 $S$ 在直线 $X W$ 上.

注 这个引理的证明其实只需要用到等角共轭点的一些基本性质, 读者可完成自己的证明.下面给出笔者的证明过程以供参考.

证明 由等角共轭点的定义, 我们知道:

$$
\angle U X W=\angle T X Y=\frac{1}{2} \angle Y X Z=\angle T X Z=\angle V X W
$$

而如果 $S$ 在直线 $X W$ 上, 结合 $S U=S V$, 我们可以猜测: 其实 $S$ 就是直线 $X W$ 与 $\triangle X U V$ 外接圆的另一个交点.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-11.jpg?height=648&width=871&top_left_y=241&top_left_x=590)

图 11

(下面利用同一法)如图 12, 设直线 $X W$ 与 $\triangle X U V$ 外接圆的另一个交点为点 $S^{\prime}$. 下面证明 $S$ 与 $S^{\prime}$ 重合.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-11.jpg?height=619&width=828&top_left_y=1301&top_left_x=631)

图 12

首先已有 $S^{\prime} U=S^{\prime} V$, 作 $T$ 关于直线 $X W$ 的对称点 $T^{\prime}$, 为证明 $S^{\prime}$ 是 $\triangle T U V$ 的外心, 知只需证: $S^{\prime}$ 是 $\triangle T^{\prime} U V$ 的外心.

结合 $\angle U S^{\prime} V=180^{\circ}-\angle U X V=180^{\circ}-\angle Y X Z$ 知只要证:

$$
\angle U T^{\prime} V=90^{\circ}-\frac{1}{2} \angle Y X Z
$$

注意到:

$$
\angle U T^{\prime} V=\angle U T^{\prime} X+\angle V T^{\prime} X
$$

下面分别计算 $\angle U T^{\prime} X$ 和 $\angle V T^{\prime} X$.

首先回顾一下等角共轭点之间的角度关系.

如图 13, 在 $\triangle X W Z$ 中, $T 、 V$ 是一对等角共轭点. 设 $T$ 关于边 $X W$ 的对称点为点 $T^{\prime}$, 则 $\angle V T^{\prime} X=180^{\circ}-\angle W T Z$.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-12.jpg?height=751&width=803&top_left_y=567&top_left_x=615)

图 13

这个的证明只需注意到 $V$ 是 $T$ 关于三边的对称点所构成的三角形的外心即可, 具体过程留给读者.

回到 (6), 知 $\angle U T^{\prime} X=\angle W T Y$ 且 $\angle V T^{\prime} X=180^{\circ}-\angle W T Z$. 故:

$$
\angle U T^{\prime} V=\angle W T Y+180^{\circ}-\angle W T Z=90^{\circ}-\frac{1}{2} \angle Y X Z
$$

这表明: $S^{\prime}$ 与 $S$ 重合. 则 $S$ 在直线 $X W$ 上, 引理得证.

由引理立刻得到命题 2 得证. 不仅如此, 图中还有另外三个类似的结论. 若设 $\triangle P A B$ 的内心为点 $H$, 则将四个结论写出来如下：(外心在同一条直线上!)

1. $\triangle E F G$ 的外心在直线 $P I$ 上.
2. $\triangle E H G$ 的外心在直线 $P I$ 上.
3. $\triangle E F H$ 的外心在直线 $P I$ 上.
4. $\triangle H F G$ 的外心在直线 $P I$ 上.

由此立即可以看出, 当四边形 $E F H G$ 不退化的时候, $\triangle E F G$ 的外心、 $\triangle E H G$ 的外心、 $\triangle E F H$ 的外心、 $\triangle H F G$ 的外心一定要是同一个点(否则是四个不同的点, 但这是不可能的).
这表明: $E 、 F 、 H 、 G$ 四点共圆, 且圆心 $O$ 在直线 $k$ (即直线 $P I$ )上. 性质 4、5 同时得证.

则当点 $P$ 为共线类时, 命题 1 成立.

此时我们先不去考虑点 $P$ 是非共线类时的情形, 因为我们对共线类的点 $P$ 还有一个性质, 即性质 6 尚未给出证明.

这里我们直接去证明共线类点 $P$ 的一个综合性的结论, 即如下性质 7:

性质 7 点 $P$ 是四边形 $E F H G$ 的密克点.

证明 我们首先补充一个引理:

引理 4 引理 3 成立的同时又有: $S 、 U 、 X 、 V$ 四点共圆.

这由引理 3 的证明过程(同一法)可以直接得到.

回到性质 7 的证明: 由性质 4 知 $E 、 F 、 H 、 G$ 四点共圆, 圆心为 $O$.

又由引理 4 知 $E 、 H 、 O 、 P$ 四点共圆, 且 $G 、 F 、 O 、 P$ 四点共圆.

即点 $P$ 是 $\triangle E H O$ 的外接圆与 $\triangle G F O$ 的外接圆的另一个交点.

由圆外接四边形密克点基本性质(如图 14 )知, 点 $P$ 是四边形 $E F H G$ 的密克点, 性质 7 得证.

仍由圆外接四边形密克点基本性质知, 性质 6 得证.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-13.jpg?height=702&width=922&top_left_y=1531&top_left_x=561)

图 14

至此, 关于共线类点 $P$ 的性质探索与证明就可以告一段落了.

对本部分的整个证明过程做一个简单的总结:

整个证明的关键是我们通过研究图中的角度关系, 将关于四内心的整体结构拆成了四个“相似”的关于三内心的部分结构, 而部分结构是容易处理的.
这种“将一个大结构拆分成若干个“互不影响”的小结构, 再对每个小结构进行分析, 最终由小结构得到的结论去证明原本大的命题”的思想是值得读者关注的! (我们在引理 3 的证明过程中也采用了这种想法)

下图(图 15 ) 为本部分中点 $P$ 的性质的小汇总, 供参考.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-14.jpg?height=917&width=1108&top_left_y=518&top_left_x=500)

图 15

## 第 3 部分: 非共线类

本部分我们将探讨一些关于非共线类点 $P$ 的性质, 并对点 $P$ 是非共线类的这一种情形来证明命题 1. (除特殊说明外, 本部分中点 $P$ 都是非共线类的, 且不沿用第 2 部分中各点的符号, 记点 $P^{\prime}$ 为与点 $P$ 相伴的共线类点)

首先, 非共线类的定义是一个“否定形式” 的命题, 它暂时不能给出点 $P$ 直接的性质.(但其实后面我们会指出, $P$ 与一个共线类点 $P^{\prime}$ 相伴就是能帮助我们研究 $P$ 的一个非常有力的性质) 这里我们先去研究此时点 $P$ 有何特别的性质.

具体如下:

如图 16, (各点含义同第 1 部分), 设线段 $A C$ 与线段 $B D$ 交于点 $E$, 而点 $P^{\prime}$ 是与点 $P$ 相伴的共线类点, 则由第 1 部分结果知: $M 、 P^{\prime} 、 N$ 共线且 $I 、 Q 、 R 、 P^{\prime}$ 四点共线.

又由非共线类的定义知: 点 $P$ 是完全四边形 $R E N P^{\prime} M Q$ 的密克点. 故得如下性质:
性质 $8 P 、 Q 、 E 、 R$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-15.jpg?height=671&width=1037&top_left_y=367&top_left_x=521)

图 16

由此我们知又可如下“定义”非共线类点 $P$ :

定义 4 非共线类又可称为共圆类的.

由性质 8 结合角平分线我们可以去分析推导出图中的一些角度关系:

如图 16, 由 $P 、 Q 、 E 、 R$ 四点共圆, 我们知:

$$
\angle P R E+\angle P Q E=180^{\circ}
$$

又

$$
\angle P R E=\angle P B D+\frac{1}{2} \angle B P D
$$

且

$$
\angle P Q E=\angle P C A+\frac{1}{2} \angle A P C
$$

故:

$$
\begin{aligned}
& \frac{1}{2}(\angle B P A+\angle C P D)+\angle A P D+\angle P B D+\angle P C A=180^{\circ} \\
\Rightarrow & \frac{1}{2}(\angle B P A+\angle C P D)+\angle A P D+\angle B P C-\angle B E C=180^{\circ} \\
\Rightarrow & 360^{\circ}-\frac{1}{2}(\angle B P A+\angle C P D)-\angle B E C=180^{\circ} \\
\Rightarrow & \angle B P A+\angle C P D=2 \angle A E B .
\end{aligned}
$$

由此得到非共线类点 $P$ 又一个性质:
性质 9 在图 16 中, 有 $\angle B P A+\angle C P D=2 \angle A E B$.

同样的, 我们有 $\angle B P C+\angle A P D=2 \angle A E D$.

注 这个性质是依赖于图 16 的, 即此时点 $P$ 在形内.要特别指出的是, 对某些圆外切四边形 $A B C D$, 非共线类点 $P$ 是可以在形外的(如图 17 ). 但其实在形外时也有类似的角度关系, 具体留给有兴趣的读者.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-16.jpg?height=594&width=1016&top_left_y=651&top_left_x=520)

图 17

下面开始本部分命题 1 的证明: (需要说明的是, 这里的证明过程其实不需要用到上述两条性质, 但上述两条性质在其他地方会用到(本文暂不涉及), 故提前给出)

我们要继续寻找非共线类点 $P$ 的刻画, 通过一定量的作图尝试, 我们发现了如下一条特别的性质, 而正是此条性质, 可以帮助我们给出命题 1 的证明.

性质 10 如图 18, 设 $\triangle P C D 、 \triangle P D A 、 \triangle P A B 、 \triangle P B C$ 的内心分别为点 $F 、 G 、 H 、 J$. 又记直线 $H G$ 与直线 $J F$ 交于点 $K$, 直线 $H J$ 与直线 $G F$ 交于点 $L$. 则直线 $P K$ 为 $\angle B P D$ 的外角平分线, 直线 $P L$ 为角 $A P C$ 的外角平分线.

证明 我们先给出一个引理:

引理 5 如图 19, 任给凸四边形 $X Y Z W$, 点 $O$ 为平面上任意一点(但不在四边形的边上(线段). 设 $\triangle O X Y 、 \triangle O Y Z 、 \triangle O Z W 、 \triangle O W X$ 的内心分别为点 $M 、 N 、 U 、 V$. 设直线 $M V$ 与直线 $N U$ 交于点 $S$.

则直线 $O S$ 是 $\angle Y O W$ 的外角平分线的充要条件是:

$$
O X \cdot O Y \cdot Z W+O W \cdot O Z \cdot X Y=O X \cdot O W \cdot Y Z+O Y \cdot O Z \cdot X W
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-17.jpg?height=848&width=1082&top_left_y=267&top_left_x=493)

图 18

注条件里点 $O$ 不在四边形的边上(线段)是一定需要的, 这保证了 $\angle Y O W$ 的外角平分线与直线 $M V$ 、直线 $N U$ 不重合. (当点 $O$ 在四边形的边上时, 结论不成立)

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-17.jpg?height=605&width=999&top_left_y=1565&top_left_x=540)

图 19

引理证明 (这里我们将多次使用内外角平分线定理. 此处对点的记号仅在本引理中使用)

如图 20, 设直线 $X M$ 与线段 $O Y$ 交于点 $E$, 直线 $X V$ 与线段 $O W$ 交于点 $F$, 直线 $Z N$ 与线段 $O Y$ 交于点 $H$, 直线 $Z U$ 与线段 $O W$ 交于点 $G$.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-18.jpg?height=579&width=1006&top_left_y=233&top_left_x=525)

图 20

设直线 $E F 、 M V$ 交于点 $S_{1}$, 由角平分线定理及梅涅劳斯定理知:

$$
1=\frac{E S_{1}}{S_{1} F} \cdot \frac{F V}{V X} \cdot \frac{X M}{M E}=\frac{E S_{1}}{S_{1} F} \cdot \frac{O F}{O X} \cdot \frac{O X}{O E}=\frac{E S_{1}}{S_{1} F} \cdot \frac{O F}{O E}
$$

则:

$$
\frac{E S_{1}}{S_{1} F}=\frac{O E}{O F}
$$

故 $S_{1}$ 在 $\angle Y O W$ 的外角平分线上.

同样设直线 $H G 、 N U$ 交于点 $S_{2}$, 则 $S_{2}$ 在 $\angle Y O W$ 的外角平分线上.

设直线 $E F 、 H G$ 的交点为点 $T$. 则知: 直线 $O S$ 是 $\angle Y O W$ 的外角平分线 $\Leftrightarrow$ 点 $T$ 在 $\angle Y O W$ 的外角平分线上. 由角平分线定理及梅涅劳斯定理知这又等价于

$$
\frac{O H}{O G} \cdot \frac{G F}{F O} \cdot \frac{O E}{E H}=1
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-18.jpg?height=640&width=939&top_left_y=1887&top_left_x=570)

图 21
又知(利用内角平分线定理, 不妨 $O E>O H$ ):

$$
O H=\frac{O Z}{Y Z+O Z} \cdot O Y, O E=\frac{O X}{X Y+O X} \cdot O Y, E H=O E-O H
$$

故:

$$
\begin{aligned}
\frac{O H \cdot O E}{E H} & =\frac{\frac{O Z}{Y Z+O Z} \cdot \frac{O X}{X Y+O X} \cdot O Y^{2}}{\left(\frac{O X}{X Y+O X}-\frac{O Z}{Y Z+O Z}\right) \cdot O Y} \\
& =\frac{O Z \cdot O X \cdot O Y}{O X \cdot Y Z-O Z \cdot X Y}
\end{aligned}
$$

同样有: (读者可以认为此时有 $O F>O G$, 如果我们用向量的形式写就不会有这个问题)

$$
\frac{O F \cdot O G}{G F}=\frac{O Z \cdot O X \cdot O W}{O X \cdot Z W-O Z \cdot X W}
$$

代入立得原等价于:

$$
\frac{O Z \cdot O X \cdot O Y}{O X \cdot Y Z-O Z \cdot X Y}=\frac{O Z \cdot O X \cdot O W}{O X \cdot Z W-O Z \cdot X W}
$$

此等价于:

$$
O X \cdot O Y \cdot Z W+O W \cdot O Z \cdot X Y=O X \cdot O W \cdot Y Z+O Y \cdot O Z \cdot X W \text {. }
$$

引理得证!

回到性质 10 的证明, 由引理 5 知只需证：(虽然是要证两条外角平分线, 但其实它们都等价于下式)

$$
P A \cdot P B \cdot C D+P C \cdot P D \cdot A B=P B \cdot P C \cdot A D+P A \cdot P D \cdot B C .
$$

但现在我们对非共线类点 $P$ 的认识足以帮助我们证明这个看起来略显复杂的等式吗？关于 3 条边相乘我们有什么办法呢？

答案却是: 我们在之前已经证明了这个等式! 在哪里? 就是在共线类的证明里!

接下来给出本部分最为精彩的一步转化, 这便是本文最开始所说的“共线类点与非共线类点之间密切的联系”.具体方法如下:

首先, 如果点 $P$ 是线段 $A C 、 B D$ 中垂线的交点, 则 $P A=P C$ 且 $P B=$ $P D$, 结合圆外切四边形基本性质： $A D+B C=A B+C D$ 知 (14) 式得证.

下设点 $P$ 不是线段 $A C 、 B D$ 中垂线的交点. 如图 22 , 我们再次取出非共线类点 $P$ 所相伴的共线类点 $P^{\prime}$.

由阿波罗尼兹圆的性质知:

$$
\frac{P C}{P A}=\frac{P^{\prime} C}{P^{\prime} A}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-20.jpg?height=663&width=922&top_left_y=268&top_left_x=567)

图 22

$$
\frac{P D}{P B}=\frac{P^{\prime} D}{P^{\prime} B}
$$

在 (14) 式两边同时除以 $P A \cdot P B$ 知 (14) 式等价于:

$$
C D+\frac{P C}{P A} \cdot \frac{P D}{P B} \cdot A B=\frac{P C}{P A} \cdot A D+\frac{P D}{P B} \cdot B C
$$

又由 (15)、(16) 式知: (17) 式等价于:

$$
C D+\frac{P^{\prime} C}{P^{\prime} A} \cdot \frac{P^{\prime} D}{P^{\prime} B} \cdot A B=\frac{P^{\prime} C}{P^{\prime} A} \cdot A D+\frac{P^{\prime} D}{P^{\prime} B} \cdot B C
$$

在 (18) 式两边同时乘以 $P^{\prime} A \cdot P^{\prime} B$ 知 (18) 式等价于:

$$
P^{\prime} A \cdot P^{\prime} B \cdot C D+P^{\prime} C \cdot P^{\prime} D \cdot A B=P^{\prime} B \cdot P^{\prime} C \cdot A D+P^{\prime} A \cdot P^{\prime} D \cdot B C .
$$

由引理 5 知这等价于: 性质 10 要对共线类点 $P^{\prime}$ 也成立. 由第 2 部分图 15 (结合圆内接四边形密克点的基本性质), 我们知道性质 10 对共线类点 $P^{\prime}$ 是自然成立的!

我们便证明了性质 10.

下面我们来完成对非共线类点 $P$ 命题 1 的证明:

首先利用性质 10 , 我们来继续分析推导图中的一些角度、长度关系. (如图 23 )

知直线 $P K$ 为 $\angle B P D$ 外角平分线, 故:

$$
\begin{aligned}
\angle G P K & =\angle G P D+\angle D P K \\
& =\frac{1}{2} \angle A P D+90^{\circ}-\frac{1}{2} \angle B P D
\end{aligned}
$$

$$
\begin{aligned}
& =90^{\circ}-\frac{1}{2} \angle B P A \\
& =90^{\circ}-\angle H P A
\end{aligned}
$$

故:

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-21.jpg?height=919&width=1125&top_left_y=517&top_left_x=477)

图 23

$$
\begin{aligned}
P H \cdot \sin \angle G P K & =P H \cdot \cos \angle H P A \\
& =\frac{1}{2}(P A+P B-A B)
\end{aligned}
$$

同样有另外三个等式:

$$
\begin{aligned}
P F \cdot \sin \angle G P L & =\frac{1}{2}(P D+P C-C D) \\
P G \cdot \sin \angle H P K & =\frac{1}{2}(P A+P D-D A) \\
P J \cdot \sin \angle F P K & =\frac{1}{2}(P B+P C-B C)
\end{aligned}
$$

则: (利用圆外切四边形基本性质： $A B+C D=A D+B C$ )

$$
\begin{aligned}
P H \cdot \sin \angle G P K+P F \cdot \sin \angle G P L & =\frac{1}{2}(P A+P B-A B)+\frac{1}{2}(P D+P C-C D) \\
& =\frac{1}{2}(P A+P B+P D+P C-A B-C D) \\
& =\frac{1}{2}(P A+P B+P D+P C-A D-B C) \\
& =P G \cdot \sin \angle H P K+P J \cdot \sin \angle F P K
\end{aligned}
$$

注 我们要特别指出的是图中有三组角度关系:

$\angle G P K=\angle J P L, \quad \angle H P L+\angle F P K=180^{\circ}, \angle H P J+\angle F P G=180^{\circ}$,

所以使用正弦值的时候是可以在同组内互换.

至此, 由 (24) 式及上面的三组角度关系, 我们对完全四边形 FGHJLK 与点 $P$ 的关联已经非常清楚了, 则我们将这个小结构从原命题的大结构中抽取出来, 单独研究(即下面给出的命题), 并最终证明 $F 、 G 、 H 、 J$ 四点共圆(即命题 1 ).

下面来证明如下命题:

命题 3 如图 24, 给定四边形 $F G H J$, 直线 $G F 、 H J$ 交于点 $L$, 直线 $H G 、 J F$ 交于点 $K$. 若存在一点 $P$ (形内), 满足:

$$
\angle G P K=\angle J P L
$$

且

$$
P H \cdot \sin \angle G P K+P F \cdot \sin \angle J P K=P G \cdot \sin \angle H P K+P J \cdot \sin \angle F P K \quad \text { (二) }
$$

则：F、G、H、J 四点共圆!

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-22.jpg?height=625&width=1056&top_left_y=1549&top_left_x=520)

图 24

注 1. 题干里点 $P$ 在形内其实是不需要的, 即结论对平面上任意一点 $P$ 都是成立的, 但条件 $(一)(二)$ 需要做相应的改动 (如把 (一) 中相等改为互补, 等等),本文暂不讨论. 指出这点的原因主要是非共线类点 $P$ 其实可以在 $A B C D$ 形外的, 如图 17, 则那时 $P$ 也在 $F G H J$ 形外.

2. 本命题可以看作三弦定理逆定理的一种推广形式(取 $P$ 为某个顶点, 如点 $F$ 即为三弦定理逆定理), 但它的证明是需要用到三弦定理的!

证明 首先由完全四边形等角线定理知：(即由条件 (一)推出点 $P$ 关于四边的垂足四点共圆, 而下面两个等式均与此等价)

$$
\begin{aligned}
& \angle H P L+\angle F P K=180^{\circ} \\
& \angle H P J+\angle F P G=180^{\circ}
\end{aligned}
$$

又如图 25, 设直线 $P K$ 与 $\triangle P J F$ 的外接圆再次交于点 $S$ (这里不妨假设 $S$ 在线段 $P K$ 上).

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-23.jpg?height=545&width=914&top_left_y=938&top_left_x=591)

图 25

则由三弦定理知:

$$
P F \cdot \sin \angle J P K-P J \cdot \sin \angle F P K=P S \cdot \sin \angle J P F
$$

同样如图 26, 设直线 $P K$ 与 $\triangle P H G$ 的外接圆再次交于点 $T$ (由前面的假设知 $T$ 也在在线段 $P K$ 上). 则由三弦定理知:

$$
P G \cdot \sin \angle H P K-P H \cdot \sin \angle G P K=P T \cdot \sin \angle H P G
$$

由条件(二)结合 $(26) 、(27)$ 式立得:

$$
P S \cdot \sin \angle J P F=P T \cdot \sin \angle H P G
$$

再由 (25) 式知:

$$
\angle J P F+\angle H P G=180^{\circ}
$$

则有:

$$
\sin \angle J P F=\sin \angle H P G
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-24.jpg?height=554&width=920&top_left_y=257&top_left_x=588)

图 26

代入 (28) 式知: (可以认为上面的正弦值不为 0 )

$$
P S=P T
$$

又 $S 、 T$ 在点 $P$ 同侧, 这表明 $S 、 T$ 重合! 故:

$$
K F \cdot K J=K S \cdot K P=K T \cdot K P=K G \cdot K H
$$

则 $F 、 G 、 H 、 J$ 四点共圆.命题得证!

由性质 10 与命题 3 , 知: 命题 1 对非共线类点 $P$ 也是成立的!

至此, 本部分也要告一段落了.简单总结如下:

本部分证明的关键是性质 10 与命题 3. 而在性质 10 的证明中我们并未对较不熟悉的非共线类点 $P$ 去讨论, 而是转化到我们已经有一定结果的共线类点 $P^{\prime}$ 去分析, 这种想法也是重要的.

对于提取出命题 3 来探讨，也是再次用到了第 2 部分总结中一研究小结构的思想, 望引起读者的注意.

最后, 由于下面这个结论较为重要(有了它之后, 结合引理 5 我们便知道性质 10 对所有满足命题 1 条件的点 $P$ 均成立, 进而利用命题 3 我们就可以证明命题 1 了), 我们在此再次指出:

性质 11 给定圆外切四边形 $A B C D$, 点 $P$ 为平面上满足命题 1 条件的一点(共线类、非共线类均可), 则有:

$$
P A \cdot P B \cdot C D+P C \cdot P D \cdot A B=P B \cdot P C \cdot A D+P A \cdot P D \cdot B C
$$

注 关于这个性质其实有一个非常直接的证法(即另一种转化的方法), 甚至
不需要用到上面的所有结果! 只需注意到, 由角平分线定理, 我们有:

$$
\begin{aligned}
& \frac{P A}{P C}=\frac{A Q}{C Q} \\
& \frac{P B}{P D}=\frac{B R}{D R}
\end{aligned}
$$

这样我们便消去了点 $P$, 再利用 $Q 、 I 、 R$ 共线这一条件经过一定量的比例计算推导, 就可以得到证明了! 具体留给有兴趣的读者.

## 第 4 部分：相关结论补充

由第 2 部分与第 3 部分的证明过程知我们已经完成了对命题 1 的证明.而本部分中我们简要补充一些相关的结论, 有兴趣的读者可对这些结论给出自己的证明, 本文附上的证明过程仅供参考. (本部分中字母以相关说明为准)

## 一、几个逆命题

命题 4 如图 27, 给定圆外切四边形 $A B C D$, 点 $P$ 为形外一点, 满足:

$$
\measuredangle A P B=\measuredangle D P C
$$

则点 $P$ 为共线类的.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-25.jpg?height=799&width=736&top_left_y=1505&top_left_x=640)

图 27

证明 只需证此时直线 $P I$ 同时为 $\angle A P C 、 \angle B P D$ 的内角平分线即可, 由第 1 部分引理 1 知成立.
命题 5 如图 28, 给定圆外切四边形 $A B C D$, 线段 $A C 、 B D$ 交于点 $E$. 点 $P$ 为平面上一点, 设 $\angle A P C$ 的内角平分线与线段 $A C$ 交于点 $Q, \angle B P D$ 的内角平分线与线段 $B D$ 交于点 $R$. 若 $P 、 R 、 E 、 Q$ 四点共圆.则: 点 $P$ 为非共线类的(共圆类的).

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-26.jpg?height=600&width=606&top_left_y=568&top_left_x=722)

图 28

证明 首先, 若 $R$ 为线段 $B D$ 中点, 则 $P R \perp B D$, 由 $P 、 R 、 E 、 Q$ 四点共圆知 $P Q \perp A C$, 故 $Q$ 为线段 $A C$ 中点, 由牛顿定理知 $I 、 R 、 Q$ 共线且点 $P$ 为线段 $A C 、 B D$ 中垂线的交点, 则 $P$ 为非共线类的, 成立.

下设 $R$ 不为线段 $B D$ 中点, 则 $Q$ 不为线段 $A C$ 中点. 在直线 $A C 、 B D$ 上分别取点 $N$. 使 $B 、 R 、 D 、 N$ 成调和点列. 则 $P N$ 为 $\angle B P D$ 外角平分线, 故 $P R \perp P N$.

如图 29, 作 $N P^{\prime}$ 垂直直线 $R Q$ 于点 $P^{\prime}$, 直线 $N P^{\prime}$ 与直线 $A C$ 交于点 $M$.

则知 $P 、 R 、 N 、 P^{\prime}$ 四点共圆. 结合 $P 、 R 、 E 、 Q$ 四点共圆, 由密克定理知 $P 、 Q 、 M 、 P^{\prime}$ 四点共圆. 则: $P Q \perp P M$. 结合 $P Q$ 为 $\angle A P C$ 内角平分线, 知 $P M$ 为 $\angle A P C$ 外角平分线. 故: $A 、 Q 、 C 、 M$ 成调和点列. 结合 $Q P^{\prime} \perp Q M$, 知: $P^{\prime} Q$ 为 $\angle A P^{\prime} C$ 内角平分线. 又 $P^{\prime} R$ 为 $\angle B P^{\prime} D$ 内角平分线,故: $\measuredangle A P^{\prime} B=\measuredangle D P^{\prime} C$ (且 $P^{\prime}$ 一定在形外).由命题 4 知: $P^{\prime}$ 为共线类的, 进而, $P$ 为非共线类的.

命题 6 如图 30, 给定圆内接四边形 $F G H J$, 直线 $G F 、 H J$ 交于点 $L$, 直线 $H G 、 J F$ 交于点 $K$.点 $P$ (形内) 满足:

$$
\measuredangle K P G=\measuredangle J P L
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-27.jpg?height=725&width=1102&top_left_y=260&top_left_x=480)

图 29

则有:

$P H \cdot \sin \angle G P K+P F \cdot \sin \angle J P K=P G \cdot \sin \angle H P K+P J \cdot \sin \angle F P K$.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-27.jpg?height=546&width=901&top_left_y=1443&top_left_x=586)

图 30

注 本命题可看作三弦定理的一种推广形式.

证明 由命题 3 的证明过程立得成立.

## 二、共线类、非共线类点 $P$ 性质补充

这里我们将补充 3 个命题, 它们可看作前文所得结果的一些应用.

命题 7 如图 31, 给定圆外切四边形 $A B C D$, 内切圆圆心为 $I$. 点 $P$ 为平面
上满足命题 1 条件的一点, 则四边形 $A B C D$ 在以点 $P$ 为反演中心, 1 (任意均可)为反演幂的反演变换下的像: 四边形 $A^{\prime} B^{\prime} C^{\prime} D^{\prime}$ 也是圆外切四边形.

特别的, 若点 $P$ 为共线类的, 则四边形 $A^{\prime} B^{\prime} C^{\prime} D^{\prime}$ 的内切圆圆心为 $I$ 在该反演变换下的像 $I^{\prime}$.
![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-28.jpg?height=622&width=1110&top_left_y=523&top_left_x=474)

图 31

证明 只需证:

$$
A^{\prime} B^{\prime}+C^{\prime} D^{\prime}=A^{\prime} D^{\prime}+B^{\prime} C^{\prime} \text {. }
$$

又由反演变换的基本性质知:

$$
\begin{aligned}
A^{\prime} B^{\prime} & =\frac{A B}{P A \cdot P B} \\
C^{\prime} D^{\prime} & =\frac{C D}{P C \cdot P D} \\
A^{\prime} D^{\prime} & =\frac{A D}{P A \cdot P D} \\
B^{\prime} C^{\prime} & =\frac{B C}{P B \cdot P C}
\end{aligned}
$$

代入(33)式并两边同乘 $P A \cdot P B \cdot P C \cdot P D$ 即为第 3 部分总结中的 (30) 式, 故成立.

而关于命题中共线类点的性质的证明只需计算角度即可, 具体过程留给读者.

命题 $8^{[1]}$ 如图 32, 给定圆外切四边形 $A B C D$, 点 $P$ 为形外一点, 满足:

$$
\measuredangle A P B=\measuredangle D P C .
$$

则 $\triangle P D A 、 \triangle P A B 、 \triangle P B C 、 \triangle P C D$ 的内切圆(共 4 个圆)有一条公切线.

证明 这个命题的证明是构造性的(即我们直接定出公切线的位置, 再用同

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-29.jpg?height=620&width=1023&top_left_y=218&top_left_x=516)

图 32

## 一法证之)

如图 33, 首先由命题 4 知点 $P$ 为共线类的, 设 $\triangle P D A 、 \triangle P A B 、 \triangle P B C$ 、 $\triangle P C D$ 的内心分别为点 $I_{1} 、 I_{2} 、 I_{3} 、 I_{4}$. 设线段 $I_{1} I_{3} 、 I_{2} I_{4}$ 交于点 $J$. 则由第 2 部分性质 6 知 $J$ 在直线 $P I$ 上.

经过作图探索, 我们发现: 这条公切线经过点 $J$, 且与直线 $P I$ 关于 $\angle I_{1} J I_{2}$ 成等角线.下证明此.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-29.jpg?height=637&width=971&top_left_y=1526&top_left_x=568)

图 33

设直线 $l$ 经过点 $J$ 且与直线 $P I$ 关于 $\angle I_{1} J I_{2}$ 成等角线. 我们来证明 $l$ 为这 4 个内切圆的公切线. 由对称性, 只要证: $l$ 与 $\triangle P D A$ 的内切圆相切. 而这等价于: 点 $I_{1}$ 到直线 $l$ 和线段 $P D$ 的距离相等. (由等角线)只需证:

$$
I_{1} J \cdot \sin \angle I_{2} J I=I_{1} P \cdot \sin \angle I_{1} P D
$$

又知(见第 2 部分):

$$
\angle I_{1} P D=\angle J P I_{4}, \quad \angle I_{2} J I=\angle I_{4} J P
$$

则原等价于:

$$
I_{1} J \cdot \sin \angle I_{4} J P=I_{1} P \cdot \sin \angle J P I_{4}
$$

在 $\triangle J I_{4} P$ 中, 由正弦定理, 有:

$$
\frac{\sin \angle I_{4} J P}{\sin \angle J P I_{4}}=\frac{I_{4} P}{I_{4} J}
$$

故只需证:

$$
\frac{I_{1} P}{I_{4} P}=\frac{I_{1} J}{I_{4} J}
$$

又由第 2 部分性质 7 知: $P$ 为圆内接四边形 $I_{1} I_{2} I_{3} I_{4}$ 密克点, 则(结合 $\triangle I_{2} I_{1} P \sim$ $\left.\triangle I_{2} I_{1} P\right):$

$$
\frac{I_{1} P}{I_{4} P}=\frac{I_{1} I_{2}}{I_{4} I_{3}}=\frac{I_{1} J}{I_{4} J}
$$

成立. 即直线 $l$ 与 $\triangle P D A$ 的内切圆相切. 由对称性, 知直线 $l$ 与这 4 个内切圆都相切. 命题得证!

接下来我们给出一个“循环比例”的命题:

命题 9 如图 34, 给定圆外切四边形 $A B C D$, 点 $P$ 为共线类的.设 $\triangle P D A$ 的内切圆与线段 $A D$ 切与点 $W$. 类似定义点 $X 、 Y 、 Z$. 则有:

$$
\frac{D W}{W A} \cdot \frac{A X}{X B} \cdot \frac{B Y}{Y C} \cdot \frac{C Z}{Z D} \cdot=1
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-30.jpg?height=594&width=948&top_left_y=1902&top_left_x=545)

图 34
证明 设 $\triangle P D A 、 \triangle P A B 、 \triangle P B C 、 \triangle P C D$ 的内心分别为点 $I_{1} 、 I_{2} 、 I_{3} 、 I_{4}$.我们首先回顾等角共轭点如下一个性质:

如图 35, 在 $\triangle X Y Z$ 中, $U 、 V$ 是一对等角共轭点, 则有:

$$
X U \cdot \sin \angle Y U Z=X V \cdot \sin \angle Y V Z
$$

这个的证明留给读者.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-31.jpg?height=520&width=563&top_left_y=705&top_left_x=741)

图 35

回到命题 9 的证明, 在 $\triangle P A D$ 中, 有:

$$
\frac{D W}{W A}=\frac{D I_{1} \cdot \sin \angle A I_{1} P}{A I_{1} \cdot \sin \angle D I_{1} P}
$$

故: (下面第二个等式即为第一个等式换了一下次序)

$$
\begin{aligned}
\Pi \frac{D W}{W A} & =\left(\prod \frac{D I_{1}}{A I_{1}}\right) \cdot\left(\prod \frac{\sin \angle A I_{1} P}{\sin \angle D I_{1} P}\right) \\
& =\left(\prod \frac{D I_{1}}{D I_{4}}\right) \cdot\left(\prod \frac{\sin \angle D I_{4} P}{\sin \angle D I_{1} P}\right)
\end{aligned}
$$

下面我们来证明如下两个等式:

$$
\begin{array}{r}
\Pi \frac{D I_{1}}{D I_{4}}=1 \\
\prod \frac{\sin \angle D I_{4} P}{\sin \angle D I_{1} P}=1
\end{array}
$$

注意到(见第 2 部分的分析): 点 $I_{1} 、 I_{4}$ 关于 $\triangle I D P$ 等角共轭.由上面的回顾知:

$$
\frac{D I_{1}}{D I_{4}}=\frac{\sin \angle I I_{4} P}{\sin \angle I I_{1} P}
$$

故:

$$
\prod \frac{D I_{1}}{D I_{4}}=\prod \frac{\sin \angle I I_{4} P}{\sin \angle I I_{1} P}=1
$$

同样的:

$$
\frac{\sin \angle D I_{4} P}{\sin \angle D I_{1} P}=\frac{I I_{1}}{I I_{4}}
$$

故:

$$
\prod \frac{\sin \angle D I_{4} P}{\sin \angle D I_{1} P}=\prod \frac{I I_{1}}{I I_{4}}=1
$$

命题成立.

## 三、使四内心共圆的点 $P$ 有哪些?

这里我们尝试考虑命题 1 的逆命题: 即给定圆外切四边形 $A B C D$, 平面上哪些点 $P$ 能使得 $\triangle P A B 、 \triangle P B C 、 \triangle P C D 、 \triangle P D A$ 的内心共圆? 本文并未解决这个问题，只是简单介绍一下已有的结论.

首先我们有:

1、当点 $P$ 满足命题 1 的条件时, 四内心是共圆的, 符合要求.

但还有没有其他的情况呢？其实是有的:

2、当点 $P$ 在四边形 $A B C D$ 的边上(线段)时, 四内心也是共圆的.这的证明只需利用三弦定理即可(类似非共线类的证明)

有趣的是: 这两种情况其实是统一的. 我们给出如下命题:

命题 10 给定圆外切四边形 $A B C D$, 点 $P$ 为平面上一点. 设 $\triangle P D A 、 \triangle P A B$ 、 $\triangle P B C 、 \triangle P C D$ 的内心分别为点 $I_{1} 、 I_{2} 、 I_{3} 、 I_{4}$. 若直线 $I_{1} I_{2} 、 I_{3} I_{4}$ 的交点在 $\angle B P D$ 的外角平分线上, 且直线 $I_{1} I_{4} 、 I_{2} I_{3}$ 的交点在 $\angle A P C$ 的外角平分线上.则 $I_{1} 、 I_{2} 、 I_{3} 、 I_{4}$ 四点共圆.

注 这的证明只需利用第 3 部分后半段的内容及命题 3 即可.

这个命题的逆命题目前未解, 有兴趣的读者可以尝试一下.

## 结语

在这里我们要特别指出的是: 本文中很多结果读者都可以在其他资料里找到(如下面附上的补充资料), 笔者在本文中只是将它们做了一个较为系统的整理, 并附上了证明.而关于四内心共圆的问题其实还有一些其他的结论，由于篇幅有限, 本文暂不收录.

全文证明思路总结：第 1 部分的分类为后面的探讨奠定了基础, 第 2 部分我们从感觉较为简单的情形一共线类点入手去分析命题 1 , 并通过研究小结构的
方法解决了此种情形. 第 3 部分我们采用“迂回”战术, 将对非共线类的讨论转化回对共线类的探索, 由第 2 部分所得的结果最终解决了这种情形, 则我们完成了命题 1 的证明.

而在第 3 部分的总结里面, 我们其实给出了命题 1 的“另一种”较为“直接”的证法, 望读者留意.

本文证明过程较长, 主要是将原命题拆解成了很多小的部分来探讨. 而其实每个小部分中都是对基本角度关系的分析, 和对基本长度关系的推导. 我们认为这些过程读者都是可以自己完成的, 并欢迎读者给出新的结果或证明!

## 参考文献

[1] 金春来. 用映射的观点证明一道几何题 [J]. 中等数学, 2018(8).

[2] 曹玨賀. 一道平面几何题的探索过程 [J]. 中等数学, 2016(4 期):16-19.

## 补充资料

[1] https://tieba.baidu.com/p/3856830037

给出了当点 $P$ 为线段 $A C 、 B D$ 中垂线交点时命题 1 的证明.

[2] https://tieba.baidu.com/p/6423014920

提出了第 3 部分性质 7 及第 4 部分命题 9.

[3] https://bbs.emath.ac.cn/forum.php?mod=viewthread\&tid=17486 利用代数方法来探讨命题 1 .

[4] https://artofproblemsolving.com/community/c6h1095213p5418615

## 附录一

这里我们将再给出两个命题, 它们都是与命题 1 有联系的.

命题 11 圆外切凸四边形的对角线交点、对边延长线交点、密克点都是满足命题 1 条件的.

注 其中四边形对角线交点是非共线类的, 而对边延长线交点、密克点都是共线类的.

命题 12 $2^{[2]}$ 在锐 $\angle \triangle A B C$ 中, $A B<A C, D$ 为点 $A$ 关于 $B C$ 的对称点, 平
面上一点 $P$ 满足 $\frac{A B}{A C}=\frac{P B}{P C}$, 则 $\triangle P A B 、 \triangle P B C 、 \triangle P C D 、 \triangle P D A$ 的内心共圆.

注 可知四边形 $A B C D$ 是圆外切四边形, 其内心和 $\angle B P C$ 的内角平分线与线段 $B C$ 的交点重合, 故点 $P$ 是满足命题 1 条件的.

## 附录二

给定直线 $l$ 上三个不同的点 $A 、 B 、 C$, 如何通过直尺作图找到 $l$ 上的点 $D$,使得 $A 、 B 、 C 、 D$ 成调和点列?

下面提供一种方法, 仅供参考: (如图 36)

1. 任取直线外一点 $E$, 连结 $E A 、 E B 、 E C$.
2. 在线段 $E B$ 上任取一点 $F$ (异于端点), 设直线 $A F$ 与直线 $E C$ 交于点 $G$,直线 $C F$ 与直线 $E A$ 交于点 $H$.
3. 设直线 $G H$ 与直线 $l$ 交于点 $D$, 则 $D$ 即为所求.

注 利用完全四边形基本性质即可证明点 $D$ 是满足要求的.

![](https://cdn.mathpix.com/cropped/2024_02_26_e25324370c87b862eb1ag-34.jpg?height=554&width=1156&top_left_y=1331&top_left_x=450)

图 36

