# 探究 2022 年联赛 $\mathrm{A}$ 卷加试几何题 

金磊

(西安交大附中, 710043)

2022 年全国中学生数学奥林匹克竞赛 (预赛) 暨 2022 年全国高中数学联合竞赛于 9 月 11 日举行, 除了部分省份因为疫情原因推迟考试外, 其余各省都有序组织了考试.

其中 A 卷二试的第一题为平面几何题, 题目为:

题 1 如下图, 在凸四边形 $A B C D$ 中, $\angle A B C=\angle A D C=90^{\circ}$, 对角线 $B D$ 上一点 $P$ 满足 $\angle A P B=2 \angle C P D$, 线段 $A P$ 上两点 $X 、 Y$ 满足 $\angle A X B=2 \angle A D B$, $\angle A Y D=2 \angle A B D$, 证明: $B D=2 X Y$.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-1.jpg?height=417&width=502&top_left_y=1476&top_left_x=777)

本文拟分析本题的解题思路, 并将其推广.

思路: 先尝试作出准确的图形, 分析图形的基本性质.

显然点 $A 、 B 、 C 、 D$ 在以 $A C$ 为直径的圆上. 首先要在 $B D$ 上确定一点 $P$, 使得 $\angle A P B=2 \angle D P C$. 似乎 $P$ 很不好确定, 只能先画一个近似的草图. 其次要在 $A P$ 上确定两点 $X 、 Y$, 满足 $\angle A X B=2 \angle A D B, \angle A Y D=2 \angle A B D$. 这个不难, 设 $A C$ 中点为 $O$ (即圆心), 由 $\angle A X B=2 \angle A D B$ 得 $\angle A X B=\angle A O B$,则 $A 、 O 、 X 、 B$ 四点共圆. 同理 $A 、 Y 、 O 、 D$ 四点共圆. 如下图.

但是条件 $\angle A P B=2 \angle D P C$ 很难用.

修订日期: 2022-12-08.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-2.jpg?height=482&width=646&top_left_y=190&top_left_x=705)

下面考虑一般的作图问题: 如下图, 设 $A 、 B$ 为直线 $D E$ 异侧两点, 在直线 $D E$ 上求作点 $C$ 使得 $\angle A C D=2 \angle B C E$.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-2.jpg?height=286&width=640&top_left_y=902&top_left_x=708)

这是一个经典的作图问题, 可以参考初版于 1958 年的国内的平面几何名著 [1] 中例题 94, 此书上的作法是: 作以 $B$ 为圆心, $B$ 到 $E D$ 距离为半径的圆, 过 $A$ 作此圆切线, 与 $E D$ 相交, 靠近 $D$ 的交点即为满足条件的 $C$ 点.

还有一个思路是, 容易发现 $\angle B C A=\angle B C D$. 故可以在 $D E$ 上取点 $F$ 满足 $B F=B A$ 且 $F$ 靠近 $D$, 然后再作 $\angle F B A$ 角平分线与 $D E$ 的交点 $C$ 即为所求.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-2.jpg?height=486&width=1464&top_left_y=1730&top_left_x=296)

上述两种作法的证明是显然的. 有了作法, 就可以利用此条件得到一些基本的几何性质了.

下面尝试从结果入手, 要证明 $B D=2 X Y$, 基本思路是截长或补短, 即把长线段等分或者短线段倍长, 发现似乎意义不大.

另一个思路就是相似, $X Y$ 在 $\triangle O X Y$ 中, $B D$ 在 $\triangle C D B$ 或 $\triangle B D A$ 中,
发现似乎有 $\triangle O X Y \sim \triangle C D B$, 这个不难证明: $\angle O Y X=\angle O D A=\angle O A D=$ $\angle D B C$, 同理 $\angle O X Y=\angle B D C$, 即得.

下面的难点在于如何由 $\angle A P B=2 \angle D P C$ 证明两个三角形的相似比为 2 .

在作法一的基础上, 容易想到延长 $A P$ 到 $M$, 则 $C P$ 平分 $\angle M P D$, 从而过 $C$ 作 $A P 、 B P$ 垂线 $C M 、 C N$, 则 $C M=C N$.

结合 $\triangle O X Y \sim \triangle C D B$, 欲证 $B D=2 X Y$, 需证其相似比为 2 , 考虑到 $O$为 $A C$ 中点, 想到作 $O K \perp A P$ 于 $K$. 从而即得 $C N=C M=2 O K$, 这就得到了第一种证明.

证明 1 如下图, 设 $A C$ 中点为 $O, C$ 在 $B D, C$ 在 $A P, O$ 在 $A P$ 上的射影分别为 $N, M, K$.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-3.jpg?height=583&width=628&top_left_y=1002&top_left_x=720)

由 $\angle A P B=2 \angle C P D$ 知 $P C$ 平分 $\angle D P M$, 从而 $C N=C M$. 由 $\angle A X B=$ $2 \angle A D B$ 得 $\angle A X B=\angle A O B$, 则 $A 、 O 、 X 、 B$ 四点共圆.

同理 $A 、 Y 、 O 、 D$ 四点共圆. 故

$$
\angle O Y X=\angle O D A=\angle O A D=\angle D B C .
$$

同理 $\angle O X Y=\angle B D C$. 所以 $\triangle O X Y \sim \triangle C D B$.

由中位线定理知 $C M=2 O K$. 从而即得

$$
\frac{B D}{X Y}=\frac{N C}{O K}=\frac{M C}{O K}=2,
$$

即 $B D=2 X Y$.

在作法二的基础上, 需证相似比为 2 , 即 $B C=2 O Y$, 想到在 $A P$ 上取点 $Q$,使得 $P Q=P B$, 再结合等角即得 $\triangle C P Q \cong \triangle C P B$, 则可得 $C Q / / O Y$, 再注意到 $O$ 为 $A C$ 中点, 由中位线定理得 $B C=C Q=2 O Y$. 这样基本就得到了第二种证法.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-4.jpg?height=420&width=502&top_left_y=207&top_left_x=777)

证明 2 如图, 设 $A C$ 中点为 $O$, 则点 $A 、 B 、 C 、 D$ 在以 $A C$ 为直径的圆 $O$ 上.

在 $A P$ 上取点 $Q$, 使得 $P Q=P B$. 同证法 1 得 $\triangle O X Y \sim \triangle C D B$.

由 $\angle A P B=2 \angle D P C$, 得

$$
\begin{aligned}
\angle A P C & =\angle A P D+\angle C P D \\
& =180^{\circ}-2 \angle D P C+\angle D P C \\
& =180^{\circ}-\angle D P C=\angle B P C .
\end{aligned}
$$

故 $\triangle C P Q \cong \triangle C P B$. 从而 $\angle P Q C=\angle C B P=\angle P Y O$, 于是 $C Q / / O Y$. 即 $O Y$ 为 $\triangle A C Q$ 的中位线, 故 $C Q=2 O Y$. 于是

$$
\frac{B D}{X Y}=\frac{B C}{O Y}=\frac{C Q}{O Y}=2
$$

即 $B D=2 X Y$.

与 $\mathrm{A}$ 卷同时考试的 $\mathrm{B}$ 卷的加试第一题为:

题 2 如下图, $A B C D$ 共圆且顺次排列, $A C$ 经过圆心 $O, P$ 在线段 $B D$上, 且 $\angle A P C=\angle B P C, X 、 Y$ 在线段 $A P$ 上, 且 $A O X B, A Y O D$ 共圆, 求证: $B D=2 X Y$.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-4.jpg?height=480&width=514&top_left_y=1967&top_left_x=768)

容易发现 B 卷的题目是 A 卷题目的简化版, 但也基本将其核心的考察点一等角及相似、中位线等体现了出来.
今年这个几何题目别出心裁, 大家交口称赞. 所以我就一直在努力尝试将其推广, 题 1 中的第一个二倍角即 $\angle A P B=2 \angle C P D$ 是本几何结构的精华和难点所在, 等价于 $\angle A P C=\angle C P B$, 等价于 $C$ 到 $P A 、 P D$ 距离相等, 这个精华性质应该保留, 当然其本身应该很难再推广. 后两个二倍角 $\angle A X B=2 \angle A D B$, $\angle A Y D=2 \angle A B D$ 显然就是为了使得 $A O X B, A Y O D$ 共圆, 经过我的实验, 似乎两个二倍角没法再推广。但是其等价性质 $A O X B, A Y O D$ 共圆似乎有希望推广.

故尝试将 $O$ 从圆心中解放出来, 进一步将 $A C$ 为直径也去掉, 即圆上任取四点 $A B C D$, 如果在 $A C$ 上任取点 $H$, 作圆 $A H B 、 A H D$, 对于 $B D$ 上任意点 $P$, 都有 $\triangle H Y X$ 形状是固定的, 这是相交两圆公共弦的核心性质. 下面希望得到一个关于 $X Y$ 长度的关系, 显然 $X Y$ 在逐渐变大, 所以 $X Y$ 没有最值.

还有什么好的性质呢? 不妨 “想的美”! 在 $\angle A P B=2 \angle C P D$ 的基础上, 希望 $\frac{X Y}{B D}$ 能够有很好的表示. 结合题 1 的证明, 最自然的想法是 $\frac{X Y}{B D}=\frac{A H}{A C}$, 因为当 $A C$ 为直径且 $H$ 为圆心时此比例为 $\frac{1}{2}$. 另一方面, 联赛题目的证明中有 $\triangle H X Y \sim \triangle C D B$, 从而这个结果很“合理”.

但是我在几何画板上度量了其结果, 发现结论不对, 这当然也不难理解, 因为此时是没有 $\triangle H X Y \sim \triangle C D B$ 的. 我仔细观察 $\frac{X Y}{B D}$ 和 $\frac{A H}{A C}$ 的结果, 发现虽然他们不相等, 但是他们的和却是 1 ! 即 $\frac{X Y}{B D}=\frac{C H}{A C}$, 这个结果很意外, 也很优美,我又仔细检查了数据, 改变图形形状, 发现确实没问题, 从而我就得到了如下这个“意外惊喜”的推广结果.

题 3 如下图, $A B C D$ 共圆, $H$ 在 $A C$ 上, 且 $A H X B, A Y H D$ 共圆, $P$ 在 $B D$ 上, 且 $\angle B P A=2 \angle D P C, A Y X P$ 共线, 求证: $\frac{X Y}{B D}=\frac{C H}{A C}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-5.jpg?height=468&width=514&top_left_y=1916&top_left_x=768)

下面尝试如何证明本题, 粗看本题似乎就是联赛题目的简单推广, 好像可以如法炮制证明即可. 但是仔细思考发现, 本题中是没有 $\triangle H X Y \sim \triangle C D B$ 这个关键的条件的, 所以本题与联赛题可以说是貌合而神离, 难度增加了不少. 至少
不能直接按图索骥得到. 但是我还是不死心, 毕竟这个题目是那个题目的推广,而且其核心性质 $\angle A P B=2 \angle C P D$ 也相同, 应该会有不少地方可以互相借鉴.

从而如下图所示, 我做出两个三角形的高线, 及 $C$ 在 $A P$ 上的垂线 $C K$.则有

$$
\frac{A H}{C A}=\frac{H L}{C K}=\frac{H L}{C L}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-6.jpg?height=531&width=583&top_left_y=654&top_left_x=742)

这个估计有用, 但是应该还不够, 主要是两个三角形 $\triangle H X Y$ 和 $\triangle C D B$ 都没法传递, 最好能找个两个有关系的三角形与这两个三角形相似.

对于 $\triangle H X Y$, 为所谓的相交两圆的特征三角形, 一个熟知的结论是其与两圆圆心 $O, O^{\prime}$ 及 $H$ 构成的三角形相似, 而且对于两圆作出两个圆中心也是在情理之中的. 顺便也可以做出大圆圆心 $M$, 由垂直可得 $\triangle M O O^{\prime} \sim \triangle C D B$, 这样基本就有了思路. 最后只需再证明 $M$ 到 $O O^{\prime}$ 距离为 $C H$ 的一半即可, 这个不难得到. 最后将上述证明整理如下.

证明 1 设圆 $A H B, A H D, A B D$ 圆心分别为 $O, O^{\prime}, M . O O^{\prime}$ 与 $A H$ 交点为 $I, C$ 在 $P D, P A$ 上垂足为 $J 、 K, M$ 在 $O O^{\prime}, A C$ 上垂足为 $N, G$.

由圆心得垂直, 从而有

$$
\angle H O O^{\prime}=\angle H X Y, \angle H O^{\prime} O=\angle H Y X
$$

故 $\triangle H X Y \sim \triangle H O O^{\prime}$.

类似地,

$$
\angle M O O^{\prime}=\angle B A C=\angle B D C, \angle M O^{\prime} O=\angle D A C=\angle D B C \text {, }
$$

于是 $\triangle C D B \sim \triangle M O O^{\prime}$.

又显然 $G, I$ 分别为 $A C, A H$ 中点, $M N / / A C$, 从而

$$
C H=A C-A H=2 A G-2 A I=2 G I=2 M N,
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-7.jpg?height=631&width=628&top_left_y=193&top_left_x=700)

故

$$
\frac{X Y}{B D}=\frac{X Y}{O O^{\prime}} \frac{O O^{\prime}}{B D}=\frac{H L}{H I} \frac{M N}{C J}=\frac{H L}{C J} \frac{2 M N}{2 H I}=\frac{H L}{C K} \frac{C H}{A H}=\frac{A H}{A C} \frac{C H}{A H}=\frac{C H}{A C}
$$

即 $\frac{X Y}{B D}=\frac{C H}{A C}$.

这就是我的编题和解答过程.

我把此题发到我的公众号 “金磊讲几何构型”上作为征解问题, 得到国内几何高手的热烈回应, 其中最常见的解法是武江铮、陈舜、占岩、严君啸等给出的如下解法.

![](https://cdn.mathpix.com/cropped/2024_02_26_ef0472cb6d2b3e791794g-7.jpg?height=580&width=629&top_left_y=1486&top_left_x=702)

证明 2 如图, 设 $D H 、 B H$ 交圆于 $T 、 S, A V, H U, C R, C Q$ 为相应直线的垂线.

依题意 $\angle H Y X=\angle H D A=\angle T S A$, 同理 $\angle H X Y=\angle A T S$.

故 $\triangle H X Y \sim \triangle A T S$.

又 $C R=C Q$, 由正弦定理可得

$$
\frac{C R}{A V}=\frac{C D \cdot \sin \angle C D B}{A T \cdot \sin \angle A T S}=\frac{C D \cdot C B}{A T \cdot A S}
$$

从而即得

$$
\begin{aligned}
\frac{X Y}{B D} \cdot \frac{A C}{H C} & =\frac{X Y}{S T} \cdot \frac{S T}{B D} \cdot \frac{A C}{H C} \\
& =\frac{H U}{A V} \cdot \frac{T H}{B H} \cdot \frac{A C}{H C} \\
& =\frac{H U}{C Q} \cdot \frac{C R}{A V} \cdot \frac{T H}{B H} \cdot \frac{A C}{H C} \\
& =\frac{A H}{A C} \cdot \frac{C D \cdot C B}{A T \cdot A S} \cdot \frac{T H}{B H} \cdot \frac{A C}{H C} \\
& =\frac{A H}{H C} \cdot \frac{C H \cdot H B}{H T \cdot A H} \cdot \frac{T H}{B H} \\
& =1 .
\end{aligned}
$$

即 $\frac{X Y}{B D}=\frac{C H}{A C}$.

其大体思路是发现 $\triangle H X Y \sim \triangle A S T$, 然后将线段比例通过高线转化为另外的线段之比, 最后通过圆中的相似得到结果. 解答似乎比我的更简洁、自然.

最后, 做一简单总结评价.

题 1 中 $A 、 O 、 X 、 B$ 及 $A 、 Y 、 O 、 D$ 分别四点共圆不难得到. $\triangle O X Y \sim$ $\triangle C D B$ 也容易发现. 其难点一直集中于如何使用 $\angle A P B=2 \angle D P C$ 这个条件.上述两种纯几何证法的关键都是通过作图方法诱导得到的. 其中证法一是参考答案的方法, 不难发现两种证法有异曲同工之妙. 这也体现了在解题中几何作图的重要性, 所以希望读者不要忽视作图, 很多时候, 作图的过程就是解题的过程.

不过平心而论, 本题难度还是不低的, 作为加试第一个题目门槛有点高, 似乎给了学生一个下马威, 应该没有达到“送分”的效果. 学生中不少几何高手都在此题上折腰, 或者虽然解决了, 但是花费了大量的时间和精力. 所以很多人觉得本题虽然是加试第一题, 但是比往年的第一题几何难很多, 甚至比往年的第二题几何都要难.

题 3 是本人附骥尾对本题的推广, 难度增加了不少, 不过其解法基本也都是在题 1 解答基础上的加深.

当然除了上述解法, 也有人是通过相似及正弦定理或者托勒密定理计算得到的. 这里不再赘述.

## 参考文献

[1] 梁绍鸿, 初等数学复习及研究 (平面几何) [M]. 哈尔滨工业大学出版社, 2008.

