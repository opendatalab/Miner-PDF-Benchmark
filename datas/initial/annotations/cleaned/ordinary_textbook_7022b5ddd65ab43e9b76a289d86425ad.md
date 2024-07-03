# 一道 NSMO 试题的命题过程 

林逸沿<br>(浙江省温州育英国际实验学校, 325014)<br>指导教师: 孙涛

今年春季的 NSMO 第 6 题系笔者提供. 这个试题可表述为:

如图 1 所示, 已知 $\triangle A B C$ 的外接圆为 $\Gamma, D$ 为 $B C$ 中点. $E$ 在 $\triangle A B C$ 内,满足 $\angle B A D=\angle C A E$, 且 $\angle B E C=90^{\circ} . M$ 在 $B C$ 上, 满足 $\angle E M D=\angle A D M$.延长 $A M$ 交 $\Gamma$ 于 $L, K$ 为线段 $A L$ 上一点, 满足 $\angle A B K=\angle C D L$. 设 $A N \perp B C$交 $B C$ 于 $N$, 证明: $K L=2 D N$.



图 1

本文将描述笔者的大致命题过程, 由于笔者能力有限, 不足之处请指正.

## 一、灵感来源

此题的灵感来源为 $A E$ 为 $\angle B A C$ 的平分线时的构型, 这类题目并不少见,而笔者受到启发的主要为以下两个题目:

题 1 如图 2 所示, 已知 $\triangle A B C$, 延长 $\angle B A C$ 的平分线于点 $P$, 使得 $\angle B P C=90^{\circ}$, 设 $P$ 在 $B C$ 上的射影为 $D$, 证明: $\angle A D C=2 \angle A P C$.

(2019 年 12 月 23 日 我们爱几何)[^0]



图 2



图 3

证明 如图 3, 设 $\angle B A C$ 的外角平分线交 $B C$ 于 $E, A P$ 交 $B C$ 于 $F$, 易知 $B 、 C 、 F 、 E$ 为调和点列, 且 $\angle P A E=90^{\circ}=\angle P D E \Rightarrow P 、 D 、 A 、 E$ 共圆, 可知 $\angle A D C=\angle A P E$, 又 $\angle B P C=90^{\circ}$, 故由调和点列的性质知 $P C$ 平分 $\angle F P E$, 可知命题成立.

注 此题颇为精巧, 引入调和点列来刻画直角, 再由共圆倒角从而隐去辅助线, 那对一般的调和点列是否能有类似操作呢? 由题 1 可以得到很多结论, 例如取 $B C$ 的中点为 $M$, 有 $\angle M P F=\angle D A P$, 但调和点列的刻画使得点 $P$ 的性质并不独特, 对点 $P$ 是否有更好的刻画呢?

题 2 如图 4, 在圆内接四边形 $A B C D$ 中, $A B>B C, A D>D C, I 、 J$ 分别为 $\triangle A B C 、 \triangle A D C$ 的内心. 以 $A C$ 为直径的圆交线段 $B I$ 于 $X$, 交 $J D$ 的延长线于 $Y$. 证明: 若 $B 、 I 、 J 、 D$ 四点共圆, 则 $X 、 Y$ 关于 $A C$ 对称.

(2016 年中国国家队选拔考试)

笔者在解答此题时发现, 如果设 $X$ 在 $A C$ 上的射影为 $L$, 则 $B 、 L 、 D$ 共线,而证明恰好可以将题 1 与题 2 相结合得到, 如图 5.



图 4



图 5

证明 由 $B 、 I 、 J 、 D$ 共圆可知 $\angle B I J+\angle J D B=180^{\circ} \Rightarrow I J \perp A C$,设 $B I$ 交弧 $A D C$ 于点 $N, D J$ 交弧 $A B C$ 于点 $M, M N$ 交 $A C$ 于 $K$, 则易知 $M N / / I J, K$ 为 $A C$ 中点. 而又由内心的性质可知 $M J=M A, N I=N A$, 设 $B N 、 D M$ 交于点 $Y$, 则有 $\frac{M Y}{N Y}=\frac{M J}{N I}=\frac{M A}{N A}=\frac{K A}{K N}=\frac{K X}{K N}$, 可知 $\triangle X K N \sim \triangle M Y N$,故 $\angle D M N=\angle K X N$, 结合题 1 知 $B 、 L 、 D$ 共线.
注通过此题 $X$ 有了独特的刻画, 而令人感到惊奇的是其竟与双心四边形有关, 使笔者思考其是否有推广形式.

## 二、提出问题与解决

考虑题 1 中的调和点列, 除了内外角平分线所形成的调和点列外, 具有独特性质的调和点列陪位中线所形成的调和点列肯定为首选,于是笔者提出了点 $E:$ 已知 $\triangle A B C, D$ 为 $B C$ 中点. 设 $E$ 为 $\triangle A B C$ 内一点, $\angle B E C=90^{\circ}$, 且 $\angle B A D=\angle C A E$, 以此为研究对象.

根据题 1 中的证明, 我们会联想到添出调和点列, 于是如图 6 , 设 $A E$ 交 $B C$于 $X$, 且设过 $A$ 作 $\odot(A B C)$ 的切线交 $B C$ 于 $F$, 容易得到 $B 、 C 、 X 、 F$ 为调和点列. 考虑题 1 中的 $P 、 D 、 A 、 E$ 共圆, 那么不妨作 $\triangle A E F$ 的外接圆, 交 $B C$于点 $M$, 则

$$
\angle E M X=\angle E A F=\angle X A C+\angle C A F=\angle B A D+\angle A B D=\angle A D C,
$$

并且有 $D E^{2}=D X \cdot D F \Rightarrow \angle D E X=\angle D F E=\angle E A M$. 引入了点 $M$ 后, 笔者开始思考点 $M$ 其它的独特性质.



图 6

然而利用题 1 的方法点 $M$ 的性质仍然不够独特, 于是笔者联想到题 2 , 打算通过题 2 来试探究 $M$ 的性质.

如图 7 , 设 $\triangle A B C$ 的外接圆为 $\Gamma$, 设 $A M$ 延长交 $\Gamma$ 于 $L, A E$ 延长交 $\Gamma$于 $T$. 对比题 2 中的点 $X 、 L 、 D 、 N 、 M$, 其前四个点分别对应着这里的点 $E 、 M 、 L 、 T$, 模仿题 2 的辅助线, 设 $T D$ 交 $\Gamma$ 于 $S$, 并连接 $S L$. 但这里并没有一些特征点(例如内心等), 于是笔者从消点的角度考虑. 要想消去圆上的未知点,最简单的办法是将边化成正弦, 由前面所描述的 $M$ 的性质, 很容易想到 $\angle T S L$
是已知的, 而又 $\angle S D C$ 为已知, 故考虑设出 $S L$ 与 $B C$ 的交点 $Y$, 对 $\triangle S D Y$ 用正弦定理. 考虑 $\sin \angle D E T$, 容易得到 $\sin \angle D E T=\frac{D C \cdot A S}{A B \cdot A C} \sin \angle A D C$ (详见参考答案), 由正弦定理可知

$$
\frac{S Y}{D Y}=\frac{\sin \angle A D C}{\sin \angle D S Y}=\frac{\sin \angle A D C}{\sin \angle T A L}=\frac{A C \cdot A B}{D C \cdot A S}
$$

而又

$$
B Y=\frac{S B \cdot B L}{S B \cdot B L+S C \cdot C L} \cdot B C, S Y=\frac{\sin \angle S B Y}{\sin \angle B S Y} \cdot B Y, D Y=B T-B D
$$

将其代入 (1)式及 $A S / / B C$ 可得到 $A C \cdot B L-A B \cdot C L=B C \cdot A S$.



图 7

此时 $L$ 的独特性质已经体现出来, 考虑其与 Ptolemy 定理十分相似, 结合 Ptolemy 定理可得

$$
\left\{\begin{array}{l}
A C \cdot B L-A B \cdot C L=B C \cdot A S \\
A B \cdot C L-A C \cdot B L=B C \cdot A L
\end{array} \Rightarrow A B \cdot C L=D C \cdot(A L-A S) .\right.
$$

如图 8 , 引入 $A L$ 上的一点 $K$, 使得 $A K=A L-A S$, 则可得到 $\triangle A B K \sim$ $\triangle C D L$, 故有 $K L=A S$. 为隐蔽辅助线, 设 $A$ 在 $B C$ 的投影为 $N$, 将 $A S$ 换成 $2 D N$, 于是便得本题.



图 8

## 三、改进题目描述

笔者经过一些同学的解答整理后发现以 $B C$ 为直径的圆这一描述会使解题人的思维方向更具方向, 于是为增加干扰, 将 $\angle B E C=90^{\circ}$ 作为以直径的圆的代替描述. 同时根据同学的解答可以发现此题中 $\angle D E X=\angle E A M$ 的倒角过程普遍都是通过引入地位对称的另一点, 结合相交弦定理来证明, 此思路自然流畅, 笔者在答案中也改进了这一过程.

同时胡俊浦、凌晨同学给出了一个非常漂亮的证明, 其思想在于将 $K L$用相似来表示, 从而进行消点, 但这样的方法难以想到, 原因在于 $\triangle A B K \backsim$ $\triangle C D L$ 先入为主, 导致解题人多半会往直接应用 $\triangle A B K \sim \triangle C D L$ 来表示 $K L$这个方向想. 笔者曾思考是否将 $A C \cdot B L-A B \cdot C L=B C \cdot A S$ 作为题目, 这样证法二便基本上被否决掉, 但考虑到题目的入手方向和图形的美观, 笔者决定不做变动.

## 四、题后思考

此题主要分三个大步骤: 一是对 $K$ 的处理, 二是证明 $\angle D E X=\angle E A M$, 三是对所证结论转化后的证明. 笔者认为此题的难度在能否把握题目的证明方向,解题的每一步实际上与所证的结论之间并没有很直接的关系, 并且笔者认为此题中添出 $S L$ 与 $B C$ 的交点并运用正弦定理这一步是较难想到的, 并不直接.

此题考察解题者在陌生结构下的解题, 考验学生的解题与思维能力而非死记模型, 但如果仔细研究过与题 1 和题 2 的话, 此题也是相当容易的.

当然此题的缺点也是相当明显, 偏向于挖掘几何性质的证明并不多, 大部分都需要大量的倒比例来进行证明, 导致此题在解题上很不美观. 有兴趣的读者可翻阅纯几何吧, 上面的证明都相当精彩.

## 五、结语

可以发现此题的命题过程具有相当大的一般性, 并且实际上根据此题的证明我们可以给题 2 另一个思路, 即不妨设出 $A C$ 与 $M D$ 的交点 $Z$, 对 $\triangle M K Z$运用正弦定理, 同样可以证明题 2 的结论. 当然这里的角平分线和陪位中线都与中点有良好的性质, 有兴趣的读者可以考虑在其他特殊情形甚至是一般情形下的探究与推广.


[^0]:    修订日期: 2020-05-06.

