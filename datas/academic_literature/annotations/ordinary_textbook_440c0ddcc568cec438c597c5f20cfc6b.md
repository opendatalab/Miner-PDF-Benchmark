$$
\text { 数学新星网 米教师专栏 }
$$

www.nsmath.cn/jszl

# 课本上的公理可以证明吗? 

金磊

(西安交大附中, 710043)

本讲适合所有学过初中几何的人.

我们都学过初中平面几何, 也都大概了解所谓的公理系统, 即由一些基本的结论作为公理结合定义可以证明其余的所有的其他结论(也可以统称为定理).我们也知道公理体系往往有两个基本特征:

(i) 相互之间不矛盾;

(ii) 个数尽可能的少.

但是我们几乎都不知道, 这些公理能否减少 (即公理之间能否互相推证) 以及如何由这些公理推出其他定理. 以通用的北师大版初中数学教材为例, 其中的公理 (书中称为“基本事实”)有以下九条:

(1) 直线公理: 过两点有且只有一条直线.

(2) 线段公理: 两点之间, 线段最短.

(3) 垂直性质: 同一平面内, 经过一点, 有且只有一条直线与已知直线垂直.

(4) 两条直线被第三条直线所截, 如果同位角相等, 那么这两条直线平行.

(5) 平行公理: 过直线外一点有且只有一条直线与已知直线平行.

(6) 两边及夹角对应相等的两个三角形全等 (SAS).

(7) 两角及其夹边对应相等的两个三角形全等 (ASA).

(8) 三边对应相等的两个三角形全等 (SSS).

(9) 两条直线被一组平行线所截, 所得的对应线段成比例.

其实, 课本中还有很多结论都是没有证明的, 基本也算是公理. 例如:

(10) 直线外一点与直线上各点连接的所有线段中, 垂线段最短.

(11) 如果两个直角三角形的斜边和一条直角边对应相等, 那么这两个直角三角形全等 (HL).

修订日期: 2021-05-21.
当然不同版本的教材选择的公理体系不尽相同, 但是基本也都是大同小异.

我想很多人都思考过: 上述 11 个公理能互相证明吗? 最少需要多少个公理就能得到其他的剩下的公理呢?

本人经过一些思索、学习及探究, 获得了一些进展. 让我们先从三角形内角和说起.

例 1 证明三角形的内角和为平角.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-02.jpg?height=334&width=460&top_left_y=695&top_left_x=798)

证明 如图, 过 $A$ 作 $A E / / B C$, 由平行性质, 即“两直线平行, 同位角相等以及内错角相等”, 知 $\angle D A E=\angle B, \angle E A C=\angle C$, 从而

$$
\angle C+\angle B+\angle B A C=\angle E A C+\angle D A E+\angle B A C=\angle D A B=180^{\circ} .
$$

即三角形的内角和为平角.

这是一个众所周知的经典证明, 证明的关键是用到了平行线的性质一两直线平行, 同位角相等及内错角相等. 不难看出同位角相等及内错角相等是等价的, 我们重点考察其中的一个. 不妨只考虑: 两直线平行, 同位角相等.

注意! 这不是公理, 上述公理 (4) 是其逆命题, 虽然原命题和逆命题看起来很像, 但是从逻辑上讲, 他们的真假之间没有关系, 所以要分别证明. 当然往往原命题和逆命题的证明是类似的,或者可以通过其中的一个证明另一个.

那它可以证明吗? 答案是肯定的.

例 2 证明: 两条平行线被第三条直线所截,同位角相等.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-02.jpg?height=317&width=445&top_left_y=2120&top_left_x=811)

证明 反证法. 若两直线平行, 同位角不等, 如图所示, 过 $B$ 作 $\angle A B F=$ $\angle A D E$, 则由公理 (4): “同位角相等, 两直线平行”, 得 $B F / / D E$. 又 $B C / / D E$,
这与公理 (5) (平行公理): “过直线外一点有且仅有一条直线与已知直线平行”矛盾. 从而假设不成立, 原命题成立.

上述证明主要利用了公理 (4) 和公理 (5). 公理 (5) 是大名鼎鼎的平行公理,是无法证明的. 那公理 (4) 呢?

例 3 求证: 同位角相等, 两直线平行.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-03.jpg?height=288&width=602&top_left_y=650&top_left_x=727)

证明 反证法. 如图, 若 $\angle A B C=\angle A D E$, 且 $B C, D E$ 不平行, 则它们必相交于点 $F$, 由 “三角形外角大于不相邻内角”, 知 $\angle A B C>\angle A D E$, 从而与已知 $\angle A B C=\angle A D E$ 矛盾, 故假设不成立, 则原命题成立.

这似乎完成了全部的证明. 但是仔细玩磨一下, 上述证明中“三角形外角大于不相邻内角” 是如何证明的呢?

常见的证明方法是由 “三角形内角和为 $180^{\circ}$ ” 知三角形的外角等于不相邻的两个内角之和. 从而得到三角形的外角大于不相邻的内角.

这里明显出现了问题, 因为用到了例 1 中的三角形内角和为 $180^{\circ}$ 的结论,这是典型的循环论证. 能否不利用三角形内角和为 $180^{\circ}$ 来证明 “三角形外角大于不相邻内角”呢?

答案也是肯定的!

例 4 不利用三角形内角和为 $180^{\circ}$, 证明三角形外角大于不相邻内角.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-03.jpg?height=251&width=668&top_left_y=2039&top_left_x=700)

证明 如图, 倍长中线 $B E$ 到 $F$, 则 $A E=C E, B E=E F$, 且 $\angle A E B=$ $\angle C E F$ (对顶角相等), 则

$$
\triangle A E B \cong \triangle C E F(\mathrm{SAS})
$$

因此 $\angle A=\angle A C F$. 又 $F$ 点在 $\angle A C D$ 内部, 故

$$
\angle A C F<\angle A C D,
$$

故三角形外角大于不相邻内角.

这里确实没有利用三角形内角和为 $180^{\circ}$, 证明了三角形外角大于不相邻内角. 但是用到了对顶角相等(这个很容易证明), 还用到了公理 (6) SAS.

这样就基本完成了三角形内角和这个系列的证明, 而且顺便证明了公理 (4).

下面我们得寸进尺、得陇望蜀, 看看公理 (6) 能否证明? 这只要用到全等的定义即可.

全等的定义为: 能够完全重合的两个图形全等.

例 5 求证: 两边及夹角对应相等的两个三角形全等. (SAS)

已知: $\triangle A B C$ 和 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 中, $A B=A^{\prime} B^{\prime}, \angle A=\angle A^{\prime}, A C=A^{\prime} C^{\prime}$.

证明: $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}$.
![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-04.jpg?height=322&width=712&top_left_y=1306&top_left_x=677)

证明 把两个三角形的两个角 $\angle A$ 和 $\angle A^{\prime}$ 重合(即顶点和两个边所在的射线都重合).

由 $A B=A^{\prime} B^{\prime}$ 知 $B$ 和 $B^{\prime}$ 重合, 同理 $C$ 和 $C^{\prime}$ 重合.

从而 $\triangle A B C$ 和 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 完全重合, 由定义即 $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}$.

上述证法初看有点无赖, 但是仔细推敲严格利用定义是没问题的. 类似的,我们可以证明公理(7).

例 6 求证: 两角及其夹边对应相等的两个三角形全等. (ASA)

已知: 如果 $\triangle A B C$ 和 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 中, $\angle B=\angle B^{\prime}, B C=B^{\prime} C^{\prime}, \angle C=\angle C^{\prime}$.

证明: $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}$.

证明 把两个三角形的两个角 $\angle B$ 和 $\angle B^{\prime}$ 的两个边所在的射线重合.

由 $C B=C^{\prime} B^{\prime}$ 知 $C$ 和 $C^{\prime}$ 重合. 由 $\angle C=\angle C^{\prime}$ 知 $C A, C^{\prime} A^{\prime}$ 所在的射线重
![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-05.jpg?height=292&width=736&top_left_y=211&top_left_x=660)

合, 由两条直线最多只有一个交点知 $A$ 和 $A^{\prime}$ 重合,

从而 $\triangle A B C$ 和 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 完全重合. 即 $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}$.

上述证明中除了利用定义, 还用到“两条直线最多只有一个交点”, 这是“显然” 的, 但是也应该要给出证明的. 正像有人说的, 数学题只有两种: 这也要证和这也能证？事实上我们在上述例 3 的证明中也默认的用到了本结论. 下面证明本结论.

例 7 求证: 两直线相交, 只能有一个交点.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-05.jpg?height=240&width=376&top_left_y=1179&top_left_x=840)

证明 反证法. 假设两直线不交于一点: 如果有两个或以上, 这样过两点就可以做两条直线. 这个与公理 (1): 过两点有且只有一条直线的“直线公理”产生矛盾, 所以假设错误.

即两直线相交, 只能有一个交点.

上述证明也体现了公理 (1) 的用处, 否则很多人可能会和我一样, 认为公理 (1) 是没有用、可有可无的.

上述公理中全等判定公理还有公理 (9) $S S S$ 没有证明, 这个也能如法炮制,类似上面两个完成证明吗?

答案是否定的, 因为虽然可以让两个顶点重合, 即一条边重合, 由 $B A=B A^{\prime}$和 $C A=C A^{\prime}$ 及 $A, A^{\prime}$ 在 $B C$ 同侧并不能得到 $A, A^{\prime}$ 重合. 当然有人会说了, 那就是以 $B$ 为圆心 $B A$ 为半径画圆和以 $C$ 为圆心 $C A$ 为半径画圆, 两个圆在 $B C$的同侧最多只能有一个交点, 所以 $A, A^{\prime}$ 必然重合. 这里面最大的问题是这两个圆在 $B C$ 同侧最多只有一个交点这也是需要证明的！当然这也是可以证明的，但是并不容易, 有兴趣的读者可以自行探究.

那有没有更简洁的方法证明 $S S S$ 判定呢?
例 8 求证: 三边对应相等的两个三角形全等. (SSS)

已知: 在 $\triangle A B C$ 和 $\triangle D E F$ 中, $A B=D E, B C=E F, A C=D F$.

证明: $\triangle A B C \cong \triangle D E F$.
![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-06.jpg?height=384&width=784&top_left_y=460&top_left_x=634)

证明 在 $\triangle A B C$ 的另一侧作 $\triangle G B C \cong \triangle D E F$, 联结 $A G$. 由 $A B=G B$, 知 $\angle B A G=\angle B G A \quad$ (等边对等角).

由 $A C=G C$, 知

$$
\angle C A G=\angle C G A \text { (等边对等角). }
$$

于是

$$
\angle B A G+\angle C A G=\angle B G A+\angle C G A \quad \text { (等量加等量和相等), }
$$

即

$$
\angle B A C=\angle B G C=\angle E D F,
$$

因此 $\triangle A B C \cong \triangle D E F(\mathrm{SAS})$.

此方法据说是古希腊数学家斐洛 (Philo) 的证明, 巧妙的利用了等腰三角形性质一“等边对等角”解决了本题. 当然, 一个自然的问题是“等边对等角” 如何证明呢?

例 9 证明等边对等角.

已知: 在 $\triangle A B C$ 中, $A B=A C$.

证明: $\angle B=\angle C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-06.jpg?height=311&width=502&top_left_y=2277&top_left_x=777)
证明 在 $\triangle A B C$ 和 $\triangle A C B$ 中, 由

$$
\begin{array}{ll}
A B=A C & \text { (已知 }), \\
\angle A=\angle A & \text { (公用 }), \\
A C=A B & \text { (已知 }),
\end{array}
$$

得

$$
\triangle A B C \cong \triangle A C B \quad \text { (SAS) }
$$

故 $\angle B=\angle C$.

上述证明巧妙使用 $S A S$ 证明此三角形与自己全等, 妙不可言. 当然本题也可以使用添加角平分线、高线等方法证明. 类似的利用 $A S A$ 即可证明等角对等边.

下面看公理 (2): “两点之间距离最短” 可以证明吗?

不难发现此公理等价于“三角形两边之和大于第三边”.

例 10 求证: 三角形两边之和大于第三边.

证明: $\triangle A B C$ 中, $A B+A C>B C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-07.jpg?height=520&width=488&top_left_y=1439&top_left_x=790)

证明 延长 $B A$ 至 $D$, 使 $A D=A C$, 联 $C D$. 由

$$
\angle B C D>\angle A C D=\angle D,
$$

有

$$
B D>B C \text { (大角对大边). }
$$

即 $A B+A C>B C$.

此证明利用了,三角形中“等边对等角”及 “大角对大边”. 自然的问题是, 如何证明“大角对大边”呢？
常见的证明方法是利用三角形两边之和大于第三边证明. 如何绕开三角形两边之和大于第三边证明呢?

例 11 求证: 大角对大边.

已知: $\triangle A B C$ 中, $\angle C>\angle B$.

证明: $A B>A C$.

思路 1 用反证法转化为大边对大角.

证明 1 反证法. 如果结论不成立, 则要么 $A B=A C$, 要么 $A B<A C$.

(1) 如果 $A B=A C$, 可得 $\angle B=\angle C$, 与 $\angle C>\angle B$ 矛盾;

(2) 如果 $A B<A C$, 根据大边对大角, 得 $\angle B>\angle C$, 与 $\angle C>\angle B$ 矛盾.

表明 (1), (2) 两种可能都不会发生, 于是只能成立 $A B>A C$.

下证大边对大角:

在 $A B$ 上截取 $A D=A C$, 联结 $D C$. 则

$$
\angle A C B>\angle A C D=\angle A D C>\angle B .
$$

综上, 大角对大边得证.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-08.jpg?height=414&width=422&top_left_y=1381&top_left_x=817)

思路 2 利用内角和直接证明.

证明 2 在 $\angle A C B$ 内部作

$$
\angle B C D=\frac{1}{2}(\angle A C B-\angle B),
$$

则 $D$ 必在线段 $A B$ 上. 由三角形内角和得三角形外角等于不相邻的两内角之和,得

$$
\angle A D C=\angle B+\angle B C D=\frac{1}{2}(\angle A C B+\angle B)=\angle A C D \text {, }
$$

则

$$
A C=A D<A B
$$

即大角对大边.
上述两种证法各有千秋, 证法一是《几何原本》中欧几里得的证明, 利用了反证法, 将其巧妙的转化为其逆命题, 然后得证. 顺便又证明了 “大边对大角”.

证法二是本人的想法, 利用前面已经证明的三角形内角和也能曲径通幽.

公理 (3) 也不难证明,

例 12 证明同一平面内, 经过一点, 有且只有一条直线与已知直线垂直.
![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-09.jpg?height=352&width=622&top_left_y=640&top_left_x=724)

证明 反证法. 若 $A$ 在直线外, 过 $A$ 有两条直线 $A B, A C$ 与已知直线垂直,则

$$
\angle A B C=\angle A C B=90^{\circ} \text {, }
$$

由三角形内角和为 $180^{\circ}$, 知 $\angle B A C=0^{\circ}$, 矛盾. 从而假设不成立, 原命题成立.

若点在直线上, 同理可得矛盾.

当然公理 (10) 也可以证明.

例 13 证明从直线外一点到这条直线上的各点所联结的线段中, 和这条直线垂直的线段最短.

证明 显然 $\angle B C A=90^{\circ}>\angle A B C$, 由例 10 的大角对大边知 $A B>A C$, 从而本结论成立.

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-09.jpg?height=280&width=414&top_left_y=1942&top_left_x=821)

公理 (11) 也可以证明.

例 14 斜边和一组直角边对应相等的两个直角三角形彼此全等. (HL)

已知: 在 $\triangle A B C$ 和 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 中, $A C=A^{\prime} C^{\prime}, B C=B^{\prime} C^{\prime}, \angle C=\angle C^{\prime}=$ $90^{\circ}$. 证明: $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}$.
![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-10.jpg?height=268&width=1052&top_left_y=250&top_left_x=501)

## 思路 1 类似例 8.

证明 1 如图, 移动 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 使得 $A C$ 和 $A^{\prime} C^{\prime}$ 重合, $B^{\prime}$ 和 $D$ 重合且 $D, B$在 $A C$ 异侧. 由

$$
\angle A C B=\angle A C D=90^{\circ},
$$

知 $B C D$ 共线. 由 $A D=A^{\prime} B^{\prime}=A B$ 得 $\angle D=\angle B$, 故 $\angle C A B=\angle A^{\prime}$.

因此 $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}(\mathrm{ASA})$.

思路 2 利用勾股定理.

证明 2 依题意

$$
A B^{2}-A C^{2}=A^{\prime} B^{2}-A^{\prime} C^{\prime 2}
$$

由勾股定理得 $B C^{2}=B^{\prime} C^{\prime 2}$, 即 $B C=B^{\prime} C^{\prime}$, 则 $\triangle A B C \cong \triangle A^{\prime} B^{\prime} C^{\prime}$ (SAS).

公理 (9) 也是可以证明的.

例 15 证明两条直线被一组平行线所截, 所得的对应线段成比例. 即

$$
\frac{A B}{B C}=\frac{A^{\prime} B^{\prime}}{B^{\prime} C^{\prime}}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_574dc44681c8f46e8de8g-10.jpg?height=529&width=665&top_left_y=1780&top_left_x=684)

证明 用 $[A B C]$ 表示 $\triangle A B C$ 面积. 则

$$
\frac{A B}{B C}=\frac{\left[A B B^{\prime}\right]}{\left[C B B^{\prime}\right]}=\frac{\left[A^{\prime} B B^{\prime}\right]}{\left[C^{\prime} B B^{\prime}\right]}=\frac{A^{\prime} B^{\prime}}{B^{\prime} C^{\prime}}
$$

从而得证.
上述证明中面积的性质只需利用定义:“长方形的面积为长与宽的乘积”, 即可得到“三角形的面积为底乘高的一半”及其他面积的性质.

通过前面我们发现课本上的 11 个公理中, 其实我们只需使用公理 (1) 和 (5)这 2 个公理即可证明余下的 9 个公理, 自然也能得到其他的所有定理, 而且证明过程并不复杂. 上述过程是按我的思考探究过程环环相扣的给大家按倒叙呈现出来的. 当然可以按照逻辑顺序一一整理出来, 不过如果不了解上述思考过程的来龙去脉可能会觉得其中的有些证明是舍近求远、莫名其妙.

当然, 上述思路和证法并不新鲜, 事实上, 欧几里得的《几何原本》中基本就是按这个逻辑思路呈现的, 不过他是按顺序写出来, 初学者看的会有些一头雾水、不知所云的感觉. 其实钻之弥深、仰之弥高, 只有你从逻辑上想通《几何原本》以后才能明白欧几里得的良苦用心和勾深致远. 才能真正明白欧几里得的伟大.

可惜的是, 上述环环相扣的推理过程现在在教材和辅导资料上极为罕见, 至少笔者很少见到. 迄今我只在单墫单老的《平面几何的知识与问题》中看到了这个完整的体系, 上述的证明此书都有, 强烈推荐对公理体系有兴趣的读者参阅此书.

课本之所以把很多能证明的定理作为公理, 只是为了降低几何课程的难度,这是无可厚非的. 不过对于好奇心强、学有余力的学生, 相信应该会有不少人有过与我类似的疑问和思考. 应该让他们了解上述推理过程, 毕竟这里面辅助线并不复杂, 难度主要在于逻辑上如何严谨而已.

需要说明的是, 上述证明基本是按照欧几里得公理体系完成证明的, 经过 2000 年的发展, 上世纪以来希尔伯特等数学家又发现了欧几里得公理体系还有一些地方还不够严密, 在很多证明中都使用了一些默认的几何性质和结论, 所以希尔伯特又重新整理出一套更严密的希尔伯特公理体系, 此公理体系是迄今最完整的几何公理体系. 不过对于仅仅学完几何的初中学生, 只要能把欧几里得的公理体系想明白就很厉害了. 在此基础上, 有余力的读者可以进一步研究希尔伯特公理体系。

