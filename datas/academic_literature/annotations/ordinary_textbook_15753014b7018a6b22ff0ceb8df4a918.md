数学新星网 $*$ 教师专栏

www.nsmath.cn/jszl

# 2018 年高中数学联赛几何题的解法研究及推广 

金磊

(西安交通大学附属中学, 710043)

本文研究了 2018 年高中数学联赛加试第二题, 准备系统总结本人接触到及想到的所有思路和解法, 对各种解法对比总结, 并对此题进行推广.

题目 如图 1, $\triangle A B C$ 为锐角三角形, $A B<A C, M$ 为边 $B C$ 的中点, $D 、 E$分别为 $\triangle A B C$ 的外接圆上弧 $\widehat{B A C}$ 和弧 $\widehat{B C}$ 的中点, $F$ 为 $\triangle A B C$ 内切圆在 $A B$ 边上的切点, $G$ 为 $A E$ 与 $B C$ 的交点, $N$ 在线段 $E F$ 上, 满足 $N B \perp A B$. 证明：若 $B N=E M ，$ 则 $D F \perp F G$.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-1.jpg?height=506&width=460&top_left_y=1369&top_left_x=798)

图 1

首先看本题的八种证法:

设 $\triangle A B C$ 外心为 $O$, 其内心为 $I$, 显然 $E M O D$ 共线且 $D A G M$ 共圆, 因此欲证 $D F \perp F G$, 即证 $F$ 在此圆上, 只需证明 $F$ 与四点中某三点共圆即可.

思路 1: 倒比例.

证法 1 如图 2, 作 $E T \perp A B$ 于 $T$, 则 $\triangle A T E \sim \triangle C M E, I F / / E T, E I=E C$, $\triangle A B G \sim \triangle A E C$, 故

$$
B F=B N \frac{F T}{E T}=E M \frac{A T}{E T} \frac{I E}{A E}=E M \frac{C M}{E M} \frac{C E}{A E}=B M \frac{B G}{A B},
$$

修订日期: 2019-01-18.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-2.jpg?height=497&width=466&top_left_y=191&top_left_x=795)

图 2

即

$$
B A \times B F=B M \times B G
$$

则 $A F G M$ 共圆. 则 $D F \perp F G$.

思路 2: 得到 $\triangle E B N \cong \triangle I E M$, 再得 $I F E M$ 共圆.

证法 2 由内心性质 (鸡爪定理) 知: $E B=E I, \angle A B E=\angle A G C$. 则

$$
\angle E B N=\angle M E I \text {. }
$$

由 $B N=E M$ 及 $E B=E I$, 得

$$
\triangle E B N \cong \triangle I E M(S A S)
$$

又 $I F / / B N$, 则

$$
\angle I M D=\angle B N F=\angle I F E,
$$

从而 $I F E M$ 共圆. 则

$$
\angle A F M=90^{\circ}+\angle I F M=90^{\circ}+\angle I E M=\angle A G M \text {, }
$$

故 $A F G M$ 共圆, 则 $D F \perp F G$. 证毕.

若设 $\triangle A B C$ 边角为 $a, b, c, A, B, C$. 容易算出:

$$
B F=\frac{a+c-b}{2}, \quad B M=\frac{a}{2}, \quad B G=\frac{a c}{b+c} .
$$

欲证 $A F G M$ 共圆, 需证 $B F \times B A=B G \times B M$, 即证

$$
\frac{a+c-b}{2} c=\frac{a}{2} \frac{a c}{b+c}
$$

即证

$$
a b+a c=a^{2}+b^{2}-c^{2} .
$$

下述几种证法都是得到 $(*)$ 式.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-3.jpg?height=568&width=511&top_left_y=190&top_left_x=778)

图 3

思路 3: 得到 $\triangle F B E \sim \triangle M G I$, 然后计算.

证明 3 如图 3, 由证法 2 得 $\triangle E B N \cong \triangle I E M$, 则 $\triangle E B F \sim \triangle I G M$, 从而

$$
\begin{aligned}
\frac{G M}{F B}=\frac{I G}{E B} & =1-\frac{G E}{E B}=1-\frac{G C}{A C}=1-\frac{a}{b+c} \\
& \Rightarrow \frac{\frac{a}{2}-\frac{a c}{b+c}}{\frac{a+c-b}{2}}=1-\frac{a}{b+c}
\end{aligned}
$$

化简即得 $(*)$ 式.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-3.jpg?height=525&width=514&top_left_y=1362&top_left_x=768)

图 4

思路 4: 作出 $\triangle N^{\prime} B N \cong \triangle G E M$.

证法 4 如图 4 , 作 $N^{\prime} N \perp B N, N^{\prime}$ 在 $B E$ 上, 同上有

$$
\angle N B N^{\prime}=\angle M E G,
$$

则

$$
\triangle N B N^{\prime} \cong \triangle M E G(A S A)
$$

故 $N N^{\prime}=M G, N N^{\prime} / / A B$, 则

$$
\frac{M G}{B F}=\frac{N N^{\prime}}{B F}=\frac{E N^{\prime}}{B E}=\frac{E B-E G}{B E}
$$

$$
\Rightarrow \frac{\frac{a}{2}-\frac{a c}{b+c}}{\frac{a+c-b}{2}}=1-\frac{a}{b+c}
$$

化简即得 $(*)$ 式.

注 不难发现证法 3,4 异曲同工, 得到的比例式相同.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-4.jpg?height=489&width=508&top_left_y=538&top_left_x=774)

图 5

思路 5: 作出 $\triangle T B N \cong \triangle C M E$.

证法 5 如图 5, 作 $N T / / A E$, 且 $T$ 在 $A B$ 上, 则显然

$$
\angle B T N=\angle B A E=\angle B C E \text {, }
$$

又 $B N=E M$, 则 $N T=E C$ 且 $B T=B M$, 从而得到

$$
\begin{gathered}
T F=B T-B F=\frac{a}{2}-\frac{a+c-b}{2}=\frac{b-c}{2}, \\
F A=\frac{b+c-a}{2},
\end{gathered}
$$

又

$$
\frac{F T}{F A}=\frac{N T}{E A}=\frac{C E}{E A}=\frac{B G}{B A}
$$

即

$$
\frac{b-c}{b+c-a}=\frac{a}{b+c},
$$

化简即得 $(*)$ 式.

思路 6: 作 $\triangle B N F \cong \triangle M E X$, 得到 $\triangle F A E \sim \triangle X C E$.

证法 6 如图 6, 在线段 $M C$ 上作 $M X=B F$, 则

$$
\triangle B N F \cong \triangle M E X(S A S)
$$

故 $\angle B F N=\angle M X E$, 又 $\angle F A E=\angle X C E$, 故

$$
\triangle F A E \sim \triangle X C E
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-5.jpg?height=597&width=594&top_left_y=198&top_left_x=731)

图 6

贝刂

$$
\begin{gathered}
\frac{X C}{A F}=\frac{E C}{E A}=\frac{B G}{B A}=\frac{a}{b+c}, \\
\Rightarrow \frac{\frac{a}{2}-\frac{a+c-b}{2}}{\frac{b+c-a}{2}}=\frac{a}{b+c} .
\end{gathered}
$$

化简即得 $(*)$ 式.

注 证法 5 与 6 殊途同归, 得到的比例式完全相同,所以其本质一样.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-5.jpg?height=574&width=516&top_left_y=1415&top_left_x=770)

图 7

思路 7: 直接三角计算.

证法 7 设 $\angle B F N=\theta$, 则 $\cot \theta=\frac{B F}{B N}=\frac{B F}{E M}=\frac{B F}{B E \sin \frac{A}{2}}$. 由正弦定理得

$$
\frac{A F}{A E}=\frac{\sin \left(\theta-\frac{A}{2}\right)}{\sin \theta}=\cos \frac{A}{2}-\sin \frac{A}{2} \cot \theta=\cos \frac{A}{2}-\frac{B F}{B E},
$$

且

$$
\begin{gathered}
A E=2 R \sin \left(B+\frac{A}{2}\right), B E=2 R \sin \frac{A}{2} \\
A F=4 R \cos \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}, B F=4 R \sin \frac{A}{2} \cos \frac{B}{2} \sin \frac{C}{2}
\end{gathered}
$$

将结果代入 $(\star)$ 式得到

$$
\begin{gathered}
\frac{2 \cos \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}}{\sin \left(B+\frac{A}{2}\right)}+2 \cos \frac{B}{2} \sin \frac{C}{2}=\cos \frac{A}{2}, \\
\Rightarrow 2 \sin \frac{C}{2}\left(\sin \frac{A+B}{2}+\sin \frac{B-A}{2}+\sin \frac{A+3 B}{2}+\sin \frac{A+B}{2}\right)=\sin (A+B)+\sin B, \\
\Rightarrow 2 \sin C+4 \sin \frac{C}{2} \sin B \cos \frac{A+B}{2}=\sin C+\sin B, \\
\Rightarrow 2 \sin B \cos C=\sin C+\sin B .
\end{gathered}
$$

由正弦及余弦定理, 上式化简即得 $(*)$ 式.

思路 8: 证明 $\triangle F B D \sim \triangle G E D$.

证法 8 欲证 $\triangle F B D \sim \triangle G E D$, 需证

$$
\frac{B F}{E G}=\frac{B D}{E D}=\cos \frac{A}{2}
$$

因为

$$
B F=4 R \sin \frac{A}{2} \cos \frac{B}{2} \sin \frac{C}{2}, \quad E G=\frac{E M}{\cos \frac{B-C}{2}}=\frac{2 R \sin ^{2} \frac{A}{2}}{\cos \frac{B-C}{2}} .
$$

从而需证

$$
\frac{4 R \sin \frac{A}{2} \cos \frac{B}{2} \sin \frac{C}{2} \cos \frac{B-C}{2}}{2 R \sin ^{2} \frac{A}{2}}=\cos \frac{A}{2}
$$

即

$$
\begin{gathered}
4 \cos \frac{B}{2} \sin \frac{C}{2} \cos \frac{B-C}{2}=\sin A, \\
\Rightarrow 2 \cos \frac{B-C}{2}\left(\sin \frac{C+B}{2}+\sin \frac{C-B}{2}\right)=\sin (B+C), \\
\Rightarrow \sin B+\sin C=\sin (B+C)+\sin (B-C), \\
\Rightarrow \sin B+\sin C=2 \sin B \cos C .
\end{gathered}
$$

由正弦及余弦定理, $(*)$ 式化简即得上式.

注 证法 8 与证法 7 类似, 都是三角计算为主, 不过证法 8 稍微绕了点弯路.

## 其次对上述解法作一总结及简评

此题从结果入手比较容易, 显然 $D A G M$ 共圆, 因此欲证 $D F \perp F G$, 只需证明 $F$ 与四点中某三点共圆即可. 但是考虑到图形特征, 基本上证明 $A F G M$ 共圆比较靠谱, 其他的证明要么过于复杂无法完成, 要么会绕弯路, 最终还会回到 $A F G M$ 共圆或上述恒等式上来.
欲证 $A F G M$ 共圆, 要么直接导出此四边形的边角关系, 如证法 $1 、 2$, 简洁明了; 要么得到 $\triangle A B C$ 边角关系 $(*)$ 式, 如后面的六种证法.

其实还可以分析证明 $\triangle F A D \sim \triangle F I G$, 只是过程稍微复杂一点. 这样上述后 6 种证法都可与上面两种解法组合成“新”的证明, 因此从上述解法中可以得到几十种证明. 如果再适当绕点弯路, 就能得到更多的解法了, 直于篇幅, 不再赘述.

本题入手的关键是如何利用条件 $B N=E M$, 要么作出垂直如证法 1 , 要么得到全等三角形如法 $2 、 3$, 要么作出全等三角形如法 $4 、 5 、 6$, 要么直接三角计算如法 $7 、 8$. 如果要用纯几何方法, 不使用计算, 则必须作出内心, 如法 $1 、 2$; 如果不作出内心, 一般需要得到 $\triangle A B C$ 的边角恒等式上述 $(*)$ 式. 如后面的六种证法.

整体而言, 上述证法中, 1 应该是最简洁的, 而 7 应该是最不需要动脑筋的,因为 7 没有添加辅助线, 只是三角计算. 当然本题应该还有其他的解法.

再次看本题的图形应该满足的条件及如何用尺规作出来?

显然 $\triangle A B C$ 应该满足一个条件, 由上述 $(*)$ 式可以得到

$$
c=b(2 \cos C-1),
$$

而 $c \geq b \sin C$, 故

$$
2 \cos C-\sin C \geq 1
$$

从而得到

$$
C \leq \arctan \frac{3}{4}
$$

下面给出 $C$ 和 $b$ 即可得到 $c$, 从而作出准确图形.

## 最后, 将此题推广:

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-7.jpg?height=526&width=506&top_left_y=2030&top_left_x=775)

图 8
推广如图 8, $\triangle A B C$ 中, $M$ 为 $B C$ 边的中点, 点 $D$ 和 $E$ 分别为 $\triangle A B C$ 的外接圆上弧 $\widehat{B A C}$ 和弧 $\widehat{B C}$ 的中点, $F$ 为内切圆在 $A B$ 边上的切点, $G$ 为 $A E$ 与 $B C$ 的交点, $Z$ 在线段 $A B$ 上, $N Z / / E F, N B \perp A B$, 求证: 若 $B N=E M$, 则 $D Z \perp Z G$.

![](https://cdn.mathpix.com/cropped/2024_02_26_a14ed81216e45d3d93adg-8.jpg?height=534&width=514&top_left_y=515&top_left_x=771)

图 9

证明 如图 9, 设 $I$ 为 $\triangle A B C$ 的内心, 作 $E T \perp A B$ 于 $T$, 则

$$
\triangle Z B N \sim \triangle F T E, \triangle A T E \sim \triangle C M E,
$$

且

$$
I F / / E T, E I=E C, \triangle A B G \sim \triangle A E C
$$

因此

$$
B Z=B N \frac{F T}{E T}=E M \frac{A T}{E T} \frac{I E}{A E}=E M \frac{C M}{E M} \frac{C E}{A E}=B M \frac{B G}{A B},
$$

即

$$
B A \times B Z=B M \times B G
$$

则 $A Z G M$ 共圆, 从而 $A Z G M D$ 共圆, 故 $D Z \perp Z G$.

不难发现当本题中 $Z$ 与 $F$ 重合时即为原题, 上述证明完全脱胎于证法 1 , 此推广也是本人研究得到解法 1 以后, 顺势推广得到的. 这进一步说明证法 1 是最简洁而本质的. 当然也可以考虑类比剩下的七种方法证明此题, 应该也是可行的, 不过要比原来的证明复杂不少. 本证明还可以继续推广, 本文只是抛砖引玉,有兴趣的读者可以进一步研究.

