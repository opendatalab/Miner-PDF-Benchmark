$$
\text { 数学新星网 * 学生专栏 }
$$

www.nsmath.cn/xszl

# 一类特殊完美六边形的黄氏点 

张峻铭

(南开大学 2018 级数学伯苓班, 300071)

摘要. 本文基于一个四圆共点的结论, 引发了对于一个特殊的完美六边形的一对黄氏点的性质的一连串的思考, 最终证明了一系列的命题与结论, 并构造了数个有意思的特殊情形.

关键词. 完美六边形; 黄氏点; 封腾定理; 圆锥曲线; Euler线.

## I. 记号和引理

以下, 将列出一些本文中将用到的记号以及基本引理. 本文中, 未提到关于哪个三角形做变换时默认关于原三角形进行变换.

给定 $\triangle A B C$, 其外心, 垂心和重心分别被记为 $O, H$ 和 $G$; 当. 和 .*在同一段中被使用时, 其总被认为是原给定三角形 $\triangle A B C$ 的一对等角共轭点; $i$. 将被记为点. 关于 $\odot(A B C)$ 的反演点; 除非特别说明, 我们用 $\triangle \cdot_{1} \cdot 2 \cdot 3, \triangle{ }_{a} \cdot{ }_{b}{ }^{c}$ 来表示. 关于 $\triangle A B C$ 的 Ceva 三角形和垂足三角形 (e.g. 定理 5.1); 除此之外, 我们通常用 $\triangle D E F$ 来表示 $\triangle A B C$ 的垂三角形 (e.g. 引理 3.2 ).

下面是一些我们将会用到的经典引理.

引理 1.1 给定 $\triangle A B C$ 和一点 $X$, 则 $\measuredangle B X C+\measuredangle B X^{*} C=\measuredangle B A C$.

证明 参见文献 [8] 的 $\S 238$.

引理 1.2 给定 $\triangle A B C$ 和一点 $X$, 则 $\measuredangle B X C+\measuredangle B i X C=2 \measuredangle B A C$.

证明 参见文献 [8] 的 $\S 75$.

引理 1.3 给定 $\triangle A B C$, 则一直线的等角共轭像为一外接圆锥曲线. 特别地, 过 $O$ 的一直线的等角共轭像经过 $A, B, C, H$, 是一个等轴双曲线.

证明 参见文献 [4] 的 Theorem 3.17 和 Problem 19.

修订日期: 2021-09-20;
引理 1.4 给定一圆 $\Gamma$, 令 $X, Y, P, Q \in \Gamma, P Q \cap X Y=R$, 则

$$
\frac{R X}{R Y}=\frac{P X}{P Y} \cdot \frac{Q X}{Q Y}
$$

证明 由文献 [8] 的 $\S 84$, 此引理显然.

## II. 问题的提出

笔者在 2019 年 8 月的时候无意间发现了一个四圆共点相关的命题.

命题 2.1 平面上给定一三角形 $A B C$, 平面上有四点 $X, P, Q, R$, 满足 $A B C X \backsim A E F P \backsim D B F Q \backsim D E C R$, 则 $\odot(E F P), \odot(F D Q), \odot(D E R)$, $\odot(P Q R)$ 共点 $Y$.

证明并不困难, 简单导角即可.



证明 设 $\odot(E F P)$ 与 $\odot(F D Q)$ 除 $F$ 外的交点为点 $Y$. 则

$$
\measuredangle D Y E=\measuredangle D Y F+\measuredangle F Y E=\measuredangle D Q F+\measuredangle F P E=\measuredangle D R E,
$$

于是 $Y$ 在 $\odot(D E R)$ 上.

由相似对应易得 $\triangle P Q F \backsim \triangle A D F$, 于是

$$
\measuredangle P Q Y=\measuredangle F Q Y+\measuredangle P Q F=\measuredangle F D Y+\measuredangle A D F=\measuredangle A D Y
$$

同理可得 $\measuredangle A D Y=\measuredangle P R Y$.

于是 $Y$ 也在 $\odot(P Q R)$ 上.
注 $2.1 P E R D Q F$ 事实上是一个完美六边形, 所以这里的点 $Y$ 恰为一个"黄氏点”. 在本文后半部分，我们将给出完美六边形及"黄氏点”的具体定义，并讨论这个完美六边形的另一个"黄氏点”。

一个自然的问题是, 能不能不借助这样的多圆共点, 而只凭借单独的点 $X$和常见的几何变换刻画出 $Y$ 呢? 答案是肯定的. 以下沿用命题 2.1 的记号.

定理 $2.1 Y$ 是 $(i X)^{*}$ 关于极圆的反演点.

证明 我们采用同一的思路, 记 $(i X)^{*}$ 关于极圆的反演点为 $Y^{\prime}$, 于是只需证明 $Y^{\prime}$ 在 $\odot(P E F)$ 上, 而后由对称性即可得结论成立, 而这只需要证 $\measuredangle F Y^{\prime} E=$ $\measuredangle B X C$. 在极圆反演下, $F Y^{\prime}$ 变为 $\odot\left(C H(i X)^{*}\right), E Y^{\prime}$ 变为 $\odot\left(B H(i X)^{*}\right)$, 由反演的保角性,

$$
\begin{aligned}
\measuredangle F Y^{\prime} E & =\measuredangle(i X)^{*} B H+\measuredangle H C(i X)^{*}=\measuredangle B(i X)^{*} C+\measuredangle C H B \\
& =\measuredangle B A C-\measuredangle B i X C+\measuredangle B A C=\measuredangle B O C-\measuredangle B i X C \\
& =\measuredangle B X C .
\end{aligned}
$$

于是 $Y^{\prime} \equiv Y$, 结论成立.



结合下面的引理, 我们可以得到一个有趣的推论.

引理 2.1 等轴双曲线在一个关于其上一点为圆心的圆做反演时, 其像是一条斜环锁线, 自交点就是反演中心.

证明 参见文献 [1].
推论 2.1 当 $X$ 在一条过外心 $O$ 的直线上时, $Y$ 在一条自交点为垂心 $H$的斜环锁线上.

证明 由引理 1.3 , 定理 2.1 和引理 2.1 显然.

注 2.2 笔者事实上是先发现了这个结论, 才得出了定理 2.1 的结果.

下面我们将 $X \mapsto Y$ 这个变换记作 $f$. 由 $f$ 的定义以及 定理 2.1, 都可以容易地看出 $f(B C)=E F$, 那么一个自然的问题是, 对于 $B C$ 上的一点 $X, f(X)$ 会落到 $E F$ 上的什么位置呢? 我们将在下一节中给出结论.

## III. 两个相似的命题

对 $B C$ 上的一点 $X$, 我们先给出 $f(X)$ 的一个性质.

定理 3.1 给定 $\triangle A B C$ 和一点 $X \in B C$, 则 $f(X) \in E F$ 且 $\triangle A O X$ 和 $\triangle D H f(X)$ 逆相似.



证明 为方便书写, 我们还是置 $Y:=f(X)$, 则 $Y$ 自然在 $E F$ 上. 设 $A B, C$与 $\odot(B H C)$ 的第二交点为 $B^{\prime}, C^{\prime}, B^{\prime} H, C^{\prime} H$ 分别交 $E F$ 于 $S, T$. 由

$$
\angle A C^{\prime} H=\angle H B C=\angle C A H
$$

得到 $H A=H C^{\prime}$, 同理 $H A=H B^{\prime}$, 于是 $H$ 是 $\triangle A B^{\prime} C^{\prime}$ 的外心, 由极圆反演下 $D, S, T$ 与 $A, B^{\prime}, C^{\prime}$ 互变, 故恰有

$$
\triangle D S T \backsim \triangle A B^{\prime} C^{\prime} \backsim \triangle A C B,
$$

且 $H$ 为 $\triangle D S T$ 外心. 下面由 $X$ 在 $B C$ 上, 故 $B, O, C, i X$ 共圆, $B, H, C,(i X)^{*}$共圆, 于是

$$
\measuredangle B i X C=\measuredangle B O C=\measuredangle B^{\prime} H C^{\prime}=\measuredangle B^{\prime}(i X)^{*} C^{\prime} \text {, }
$$

且 $\measuredangle C^{\prime} A(i X)^{*}=\measuredangle i X A B^{\prime}$, 又 $\triangle A B^{\prime} C^{\prime} \backsim \triangle A C B$, 于是我们有 $A B C i X \backsim$ $A C^{\prime} B^{\prime}(i X)^{*}$, 于是

$$
\begin{aligned}
\frac{S Y}{T Y} & =\frac{S Y}{B^{\prime}(i X)^{*}} \cdot \frac{C^{\prime}(i X)^{*}}{T Y} \cdot \frac{B^{\prime}(i X)^{*}}{C^{\prime}(i X)^{*}} \\
& =\frac{H Y}{H B^{\prime}} \cdot \frac{H C^{\prime}}{H Y} \cdot \frac{C i X}{B i X} \\
& =\frac{C X}{B X} \cdot \frac{B O}{C O}=\frac{C X}{B X} .
\end{aligned}
$$

这推出了 $X$ 和 $Y$ 恰为 $\triangle A B C \backsim \triangle D T S$ 中的相似对应点, 于是 $\triangle A O X \backsim$ $\triangle D H Y$, 且为逆相似.

注 3.1 由 $A O, A H$ 为一对等角线且 $\angle O A X=\angle H D Y$, 我们可以取出 $A X$ 的等角线, 可以看出它必与 $D Y$ 平行. 这将对我们后面的研究有巨大的帮助.

虽然我们基本搞清了 $f(X)$ 的位置, 但有时注 3.1 不是很方便. 能不能把这种不对称的问题转化成一个对称的问题, 从而通过另一组点之间的映射搞出一些关系呢? 我们可以提出一个新的问题了. 对于平面上任一点 $P$, 在什么情况下, $\triangle f\left(P_{1}\right) f\left(P_{2}\right) f\left(P_{3}\right)$ 与 $\triangle A B C$ 透视? 这里我们借助几何画板来猜测一下.



经过一系列的推理和猜测, 笔者提出了如下两个极度相近的命题.
先给出 $[5]$ 中的一个定义.

定义 3.1 直线 $O H$ 与 $\odot(A B C)$ 两交点离 $H$ 较近的为 $X_{1113}$, 较远的为 $X_{1114}$.

命题 3.1 给定 $\triangle A B C$, 令 $X:=X_{1113}, Y:=X_{1114} . P$ 为 Euler 线上一点,记 $f\left(P_{1}\right), f\left(P_{2}\right), f\left(P_{3}\right)$ 分别为 $U, V, W$. 则有

(1) $A U, B V, C W$ 共点 $Q$;

(2) $Q$ 在 Euler 线上;

(3) $\frac{Q X}{Q Y}=\frac{P X}{P Y} \cdot \frac{H X}{H Y}$.

命题 3.2 给定 $\triangle A B C$, 令 $X:=X_{1113}, Y:=X_{1114} . P$ 为 $\odot(A B C)$ 上一点,记 $f\left(P_{1}\right), f\left(P_{2}\right), f\left(P_{3}\right)$ 分别为 $U, V, W$. 则有

(1) $A U, B V, C W$ 共点 $Q$;

(2) $Q$ 在 $\odot(A B C)$ 上;

(3) $\frac{Q X}{Q Y}=\frac{P X}{P Y} \cdot \frac{H X}{H Y}$.



这两个命题如此相像, 硬要说没有联系是不可能的, 那么联系在哪呢? 下面这个引理将是一个“桥梁”。

引理 3.1 给定两非位似三角形 $\triangle A B C$ 和 $\triangle D E F$, 则存在 $Q$ 使得 $A P / /$ $D Q, B P / / E Q, C P / / F Q$ 的 $P$ 的轨迹是 $\triangle A B C$ 的一条外接圆锥曲线并上无穷远线.

证明 当 $P$ 在无穷远线上时, 结论显然成立. 下面考虑 $P$ 不为无穷远
点的情况. 这时相当于作 $\triangle D^{\prime} E^{\prime} C$ 与 $\triangle D E F$ 位似, 则有 $B E^{\prime}$ 与 $A D^{\prime}$ 交点即为 $P$. 所以问题转化为求 $A D^{\prime}$ 与 $B E^{\prime}$ 交点的轨迹, 我们取三组这样的 $D^{\prime} E^{\prime}$, 并证明它们对应的 $P$ 在同一条 $\triangle A B C$ 的外接雉线上, 不妨设这三组为 $D^{\prime} E^{\prime} P^{\prime}, D^{\prime \prime} E^{\prime \prime} P^{\prime \prime}, D^{\prime \prime \prime} E^{\prime \prime \prime} P^{\prime \prime \prime}$. 而由

$$
A\left(C P^{\prime}, P^{\prime \prime} P^{\prime \prime \prime}\right)=\left(C D^{\prime}, D^{\prime \prime} D^{\prime \prime \prime}\right)=\left(C E^{\prime}, E^{\prime \prime} E^{\prime \prime \prime}\right)=B\left(C P^{\prime}, P^{\prime \prime} P^{\prime \prime \prime}\right)
$$

推出 $A, B, C, P^{\prime}, P^{\prime \prime}, P^{\prime \prime \prime}$ 共雉线.

下面应该很明显了，“外接圆 $\cup$ 直线”和“无穷远线 $\cup$ 外接圆雉曲线”间只差上一个等角共轭, 但我们为了得到一个可以直接使用的推论, 还需要一个著名的 Cevian Nest 作为引理.

引理 3.2 给一 $\triangle A B C$, 有一内接三角形 $\triangle D E F, \triangle D E F$ 又有一内接三角形 $\triangle L M N$, 则

(1) $\triangle A B C$ 与 $\triangle D E F$ 透视;

(2) $\triangle D E F$ 和 $\triangle L M N$ 透视;

(3) $\triangle A B C$ 与 $\triangle L M N$ 透视;

这三者其中任何两个可以推出第三个.

## 证明

$$
\text { (1) } \Leftrightarrow \prod_{c y c} \frac{A E}{A F}=1 ;(2) \Leftrightarrow \prod_{c y c} \frac{L E}{L F}=1 ;(3) \Leftrightarrow \prod_{c y c} \frac{\sin \angle L A E}{\sin \angle L A F}=1 ;
$$

又

$$
\frac{\sin \angle L A F}{\sin \angle L A E}=\frac{\sin \angle L A F}{\sin \angle A L F} \cdot \frac{\sin \angle A L E}{\sin \angle L A E}=\frac{L F}{A F} \cdot \frac{A E}{L E},
$$

于是

$$
(3) \Leftrightarrow \prod_{c y c} \frac{L E}{L F} \cdot \frac{A F}{A E}=1
$$

于是显然结论成立.

所以可以有如下的引理.

引理 3.3 给定 $\triangle A B C$, 过 $D, E, F$ 分别作 $A P, B P, C P$ 的平行线, 并分别交 $E F, F D, D E$ 三边于 $L, M, N$, 则 $A L, B M, C N$ 共点 $Q$ 当且仅当 $P$ 的等角共轮点在 Euler 线或 $\odot(A B C)$ 上.

证明 由引理 $3.2, A L, B M, C N$ 共点当且仅当 $D L, E M, F N$ 共点, 再由引理 3.1, 这等价于 $P$ 在某外接圆锥曲线或无穷远线上. 由 $P$ 为 $\triangle A B C$ 垂心或
外心时 $D L, E M, F N$ 共点成立, 于是 $A L, B M, C N$ 共点等价于 $P$ 在 Jerabek 双曲线或者无穷远线上, 也即等价于 $P$ 的等角共轭点在 Euler 线或 $\odot(A B C)$ 上.

到了这里, 结合着注 3.1 其实已经可以看出, 命题 3.1 (1) 和命题 3.2 (1) 均成立了. 但为了证明这二者的 (2) 和 (3), 我们还需要做一些工作.

定理 3.2 给定 $\triangle A B C$, 任取 $X \in\left\{X_{1113}, X_{1114}\right\}, A X$ 交 $E F$ 于 $U$, 作 $A P / / D U$ 交 $\odot(A B C)$ 于点 $P$, 则有 $X P / / B C$.

证明 考虑 $\triangle H B C$ 的极圆反演, 这将 $H$ 和 $D$ 互变, $E F$ 和 $\odot(A B C)$ 互变,于是 $U$ 与 $X$ 互变, 因此 $U, X, H, D$ 共圆. 故

$$
\angle P A H=\angle U D H=\angle A X O=\angle O A X
$$

于是 $A X$ 和 $A P$ 是 $\angle B A C$ 的等角线, 于是结论成立.

注 3.2 对于可能的两种情况 $X U$ 和 $X^{\prime} U^{\prime}$. 稍加导角可以发现 $A, U, D, U^{\prime}$共圆.

下面我们可以先来看命题 3.1 的证明了.

证明 $P$ 在 Euler 线上时, 由 注 3.1 和引理 3.3, 可知(1)成立. 设 $A X, A Y$分别交 $E F$ 于 $X^{\prime}, Y^{\prime}$,于是

$$
A(X Y, H Q)=A\left(X^{\prime} Y^{\prime}, H U\right)=D\left(X^{\prime} Y^{\prime}, H U\right),
$$

我们在 $A$ 再做出这组线束的平行线, 并关于 $\angle B A C$ 做一个等角共轭, 结合注 2.1 和定理 2.2 就有

$$
\begin{aligned}
A(X Y, H Q) & =D\left(X^{\prime} Y^{\prime}, H U\right)=A(X Y, O P) \\
& =(X Y, O P)=B(X Y, O P) \\
& =B(X Y, H Q),
\end{aligned}
$$

于是 $Q$ 确实在 $X Y H$ 也即 Euler 线上, 并且有

$$
\frac{H X / H Y}{Q X / Q Y}=\frac{O X / O Y}{P X / P Y}=\frac{1}{P X / P Y}
$$

故

$$
\frac{Q X}{Q Y}=\frac{P X}{P Y} \cdot \frac{H X}{H Y}
$$

亦成立.
注 3.3 若上述证明中的比例用有向线段表示, 则还需要添加一个负号, 因为 $\overline{\overline{O X}}=-1$, 即

$$
\frac{\overline{Q X}}{\overline{Q Y}}=-\frac{\overline{P X}}{\overline{P Y}} \cdot \frac{\overline{H X}}{\overline{H Y}}
$$



我们欲要照葫芦画瓢来进行命题 3.2 的证明,但这里有一个小问题, 便是想要确定 $Q$ 在外接圆至少需要除去三顶点之外三点, 但我们如今只有 $X_{1113}, X_{1114}$这两点, 那我们还需要再找一个起到之前证明中垂心 $H$ 作用的点, 这也不算困难, 我们直接取 $P$ 为 $A$ 的对径点 $A^{\prime}$, 那么结合注 3.1, 容易看出 $Q$ 事实上应当会落到 $H$ 关于 $B C$ 的对称点 $H^{\prime}$, 并且结合引理 1.4, 自然有 $\frac{H^{\prime} X}{H^{\prime} Y}=\frac{A^{\prime} X}{A^{\prime} Y} \cdot \frac{H X}{H Y}$.

下面还有一个事情需要交待, 那就是圆里线束的单比利用正弦定理显然可以通过弦长的比来表示. 现在万事俱备, 让我们来完成这个证明.


证明 $P$ 在 $\odot(A B C)$ 上时, 由注 3.1 和引理 3.3 可知(1)成立. 设 $A X, A Y$分别交 $E F$ 于 $X^{\prime}, Y^{\prime}$, 取 $P$ 为 $A$ 的对径点 $A^{\prime}, H$ 关于 $B C$ 的对称点 $H^{\prime}$. 于是 $A\left(Q H^{\prime}, X Y\right)=A\left(U H^{\prime}, X^{\prime} Y^{\prime}\right)=D\left(U H^{\prime}, X^{\prime} Y^{\prime}\right)$, 下面在 $A$ 再做出这组线束的平行线, 并关于 $\angle B A C$ 做一个等角共轨, 结合注 3.1 和定理 3.2 就有

$A\left(Q H^{\prime}, X Y\right)=D\left(U H^{\prime}, X^{\prime} Y^{\prime}\right)=A\left(P A^{\prime}, X Y\right)=B\left(P A^{\prime}, X Y\right)=B\left(Q H^{\prime}, X Y\right)$,

于是 $Q$ 在 $A B H^{\prime} X Y$ 共的二次曲线也即 $\odot(A B C)$ 上, 且 $\left(P A^{\prime}, X Y\right)=\left(Q H^{\prime}, X Y\right)$说明了

$$
\frac{H^{\prime} X / H^{\prime} Y}{Q X / Q Y}=\frac{A^{\prime} X / A^{\prime} Y}{P X / P Y}
$$

故

$$
\frac{Q X}{Q Y}=\frac{P X}{P Y} \cdot \frac{H X}{H Y}
$$

亦成立.

注 3.4 下面先来将单比推广到复平面上, 对于平面上三点 $A, B, C$, 定义 $B$ 分 $A C$ 的单比 $(A C B)=\frac{\overline{A B}}{C B}=\frac{A-B}{C-B}$, 容易看出这无关复平面 0 和 1 的选取, 并且与我们通常所说的直线上的单比是一致的. 那在这种观点下命题 3.1 和命题 3.2 的 (3) 都可以被改写为

$$
\frac{\overline{Q X}}{\overline{Q Y}}=-\frac{\overline{P X}}{\overline{P Y}} \cdot \overline{\overline{H X}}
$$

我们将会在 Section 5 中用到这一点.

## IV. 一些特例

以下将会给出一些定理 2.1 , 命题 3.1 和命题 3.2 的直接或间接的特例形式.由于是特例, 笔者就不再给出证明, 但直接用这两个命题去做它们难免有高射炮打蚊子之嫌, 也希望读者能够就这些题目给出简便初等的证明. 但是定理 4.8 请读者务必细细思考一下, 因为我们后面会用到它.

定理 4.1 给定 $\triangle A B C, I, I_{2}$ 分别是内心和 $B$-旁心, $I$ 在 $B C$ 上投影是 $D$, $C I_{2}$ 中点为 $E$, 则 $A, D, C, E$ 共圆.

定理 4.2 给定 $\triangle A B C$, 其 $B$-旁心是 $I_{2}, D$ 是 $B C$ 上一点, 设 $\odot(A C D)$ 与 $C I_{2}$ 的第二交点为 $U, U$ 在 $A I_{2}, A C$ 上的投影分别为 $V, W$. 则 $A U, C V, I_{2} W$ 共点等价于 $A B+B D=A C+C D$.

定理 4.3 给定 $\triangle A B C$, 直线 $A i H$ 与 $E F$ 交于 $Q, R$ 是 $A B$ 上一点且 $D R$
与 $\triangle B D F$ 的 Euler 线平行, 则有 $D, F, Q, R$ 共圆.

定理 4.4 给定 $\triangle A B C, C l$ 是 Clawson 点, $I$ 是内心, 直线 $I C l$ 与 $O H$ 交于点 $T$, 直线 $A T$ 与 $E F$ 交于 $P$, 设 $\triangle B D F$ 外心为 $O^{\prime}, D$-旁心为 $J, O^{\prime} J$ 与直线 $A B$ 交于点 $Q$, 则 $D, Q, F, P$ 共圆.

定理 4.5 给定 $\triangle A B C$, 九点圆心为 $N, H$ 关于 $E F$ 的对称点为 $H^{\prime}$, 直线 $A H^{\prime}$ 交 $H N$ 于 $P, \triangle B D F$ 的切线三角形的外心是 $O^{\prime}$, 直线 $D O^{\prime}$ 交 $A B$ 于 $Q$, $\odot(D F Q)$ 与 $E F$ 的第二交点是 $R$, 直线 $A R$ 与 $H N$ 交于 $S$, 则有 $P, H, N, S$ 为调和点列.

定理 4.6 给定 $\triangle A B C$, 陪位重心为 $K, P$ 是 $H K$ 的三线性极点, $\triangle D B F$的 Euler 线关于 $A B, B C$ 的对称直线交于点 $Q, D Q$ 交 $A B$ 于 $R, A P$ 交 $E F$ 于 $S$, 则有 $D, F, S, R$ 共圆.

定理 4.7 给定 $\triangle A B C$, 其切点三角形的垂心为 $H^{\prime}, \triangle B D F$ 的 Feuerbach 点为 $P, B F$ 中点为 $M$, 过 $D$ 作与 $M P$ 平行的直线交 $A B$ 于 $Q$. 设直线 $H H^{\prime}$ 的逆 Steiner 点为 $R$, 直线 $A R$ 交 $E F$ 于 $S$, 则有 $D, F, S, Q$ 共圆.

定理 4.8 给定 $\triangle A B C$, 直线 $A i D$ 交直线 $E F$ 于点 $Q$, 则有 $D Q \perp E F$.

## V. 一些想法

本节的主要目的是为了说明笔者是通过什么蛛丝马迹发现的命题 3.1 和命题 3.2 中的结论.

定义命题 3.1 和命题 3.2 中 $P \mapsto Q$ 的映射为 $g$, 记 $\widetilde{X}: O H \cup \odot(A B C)$ 即 $g: \widetilde{X} \rightarrow \widetilde{X}, g(P)=Q$. 下面仍记 Euler 线与外接圆的两个交点为 $X, Y$, 我们考虑”赋单比"这个操作, 即

$$
\begin{gathered}
l: \mathbb{R}^{2} \rightarrow \mathbb{C} P^{1} \\
P \mapsto \frac{\overline{P X}}{\overline{P Y}} .
\end{gathered}
$$

显然有 $l(X)=0, l(Y)=\infty, l(O H)=\mathbb{R} \cup\{\infty\}, l(\odot(A B C))=\mathbb{R} \sqrt{-1} \cup\{\infty\}$.记 $l(H)=k$, 于是命题 3.1 和命题 3.2 的 (2) (3) 无非是说如下图表



交换.
这事实上说明了 $g$ 起到了在 $\widetilde{X}$ 上的后继的作用, 利用 $\widetilde{X}$, 还可以定义 $\widetilde{X}$ 上面类似乘法的运算.

定理 5.1 设 $U_{1}, U_{2}$ 在 $\odot(A B C)$ 上, $U_{1} U_{2}$ 与 $O H$ 交于 $V$, 则 $g\left(U_{1}\right), g(V), U_{2}$共线。

证明 由引理 1.4, 命题 3.1 和命题 3.2 , 结论显然.

下面还有一个定理, 是发现原来的结论的直接原因.

定理 $5.2 U$ 是 $\odot(A B C)$ 上一点, 于是 $U g(U)$ 与以垂心 $H$ 为焦点, $X Y$ 长轴的椭圆相切。

证明 取 $H, U, g(U)$ 关于 $O$ 的对称点 $D e, U^{\prime}, g(U)^{\prime}$, 则 $g(D e)=O$, 由定理 5.1, 有 $U^{\prime}, H, g(U)$ 共线, $g(U)^{\prime}, D e, U$ 共线, 于是

$$
\angle H g(U) U=\angle D e U g(U)=90^{\circ},
$$

作 $H T / / U O$ 交 $U g(U)$ 于 $T$, 则有

$$
\frac{g(U) T}{T U}=\frac{g(U) H}{H U^{\prime}}=\frac{g(U)^{\prime} D e}{D e U}
$$

故 $D e T / / g(U) O$. 故有 $U g(U)$ 是 $\angle H T D e$ 的外角分线. 且

$$
\begin{aligned}
H T+D e T & =(H g(U)+D e U) \csc \angle O U g(U) \\
& =U^{\prime} g(U) \csc \angle O U g(U) \\
& =U^{\prime} U=X Y
\end{aligned}
$$

于是 $T$ 在定理中提到的椭圆上且 $U g(U)$ 与其切于点 $T$.



下面我们进入本文的后半部分. 但开始本文的一些结论之前需要一些预备知识.

## VI. 完美六边形与黄氏点简介

以下定义和证明均来自于文献 [3].

定义 6.1 平面上一个六边形 $A B C D E F$, 如果其在复平面上的比满足

$$
\frac{\overline{A B}}{\overline{B C}} \cdot \frac{\overline{C D}}{\overline{D E}} \cdot \frac{\overline{E F}}{\overline{F A}}=-1
$$

则称其为完美六边形。

通过复数乘法的几何意义, 容易看出命题 2.1 中 $E P F Q D R$ 为完美六边形.

注 6.1 事实上, 验证可知 $A B C D E F, A B F D E C, A C B D F E, A E C D B F$均为完美六边形.

下面我们引入黄利兵老师 2008 年 6 月份提出的"黄氏点”定理来作为命题 2.1 的推广.

定理 6.1 $A B C D E F$ 是一个完美六边形, 则 $\odot(F A B), \odot(B C D), \odot(D E F)$, $\odot(A C E)$ 共点.

证明 设 $\odot(A C E)$ 与 $\odot(A B F)$ 的第二交点为 $X$. 则有 $\frac{\overline{A E}}{\overline{A X}} \cdot \overline{\overline{C X}}$ 和 $\frac{\overline{A X}}{\overline{A F}} \cdot \frac{\overline{B F}}{\overline{B X}}$都是实数. 故将两式相乘, 再由完美六边形的定义, 有 $\frac{\overline{B D}}{\overline{B X}} \cdot \overline{\overline{C X}}$ 也是实数, 因此 $X$也在 $\odot(B C D)$ 上, 同理另一侧也有共圆, 于是定理成立.

注 6.2 这样的点 $X$ 记作完美六边形的“黄氏点”, 可以看出一个完美六边形一般会对应两个不同的“黄氏点”。

这就能看出注 2.1 中说的是什么意思了, 本文前半部分都是探讨其中一个点, 下面我们在 Section 8 中就要去探讨另一个点了.

## VII. 逆 Steiner 点和封腾定理

我们来建立一些封腾定理相关的知识体系, 以便于后文引用. 先回忆一下逆 Steiner 点的定义.

定理 7.1 给定一 $\triangle A B C$, 考虑一条过 $H$ 的直线 $l$, 则 $l$ 关于 $\triangle A B C$ 三边的对称直线交于 $\odot(A B C)$ 上一点 $S_{l}$, 这点称作 $l$ 的逆 Steiner 点.

证明 参见 [8] 的 $\S 333$.

由于外心 $O$ 是中点三角形 $\triangle G_{1} G_{2} G_{3}$ 的垂心, 所以对平面上任意一点 $P \neq O$, 可以考虑 $O P$ 关于 $\triangle G_{1} G_{2} G_{3}$ 的逆 Steiner 点, 这使得我们的目光转移
向如下的封腾定理.

定理 7.2 给定一 $\triangle A B C$, 对平面上任意一点 $P \neq O, O P$ 关于中点三角形 $\triangle G_{1} G_{2} G_{3}$ 的逆 Steiner 点 $X$ 是 $\odot\left(G_{1} G_{2} G_{3}\right)$ 与 $P$ 关于 $\triangle A B C$ 的垂足圆一个交点. 并且若设 $P$ 关于 $\triangle A B C$ 的垂足三角形为 $\triangle P_{a} P_{b} P_{c}$, 则有 $P_{a} X, G_{2} G_{3}, P_{b} P_{c}$共点.

证明 参见文献 [8] 的 $\S 402$.

下面我们来做一个小引理, 它在某种程度上刻画了过顶点的直线与九点圆的两个交点. 并将在我们后面的证明中起到重要作用.

引理 7.1 给定 $\triangle A B C, X$ 是 $B C$ 上一点, $O X$ 关于中点三角形 $\triangle G_{1} G_{2} G_{3}$的逆 Steiner 点为 $P, A X$ 与外接圆第二交点为 $U, A P$ 与九点圆的第二交点为 $V$, 则 $V$ 是 $U$ 的补点且 $A i X$ 和 $A P$ 是 $\angle B A C$ 的一对等角线.

证明 设 $P$ 关于 $G_{2} G_{3}$ 的对称点为 $P^{\prime}, A$ 在 $B C$ 上的投影为 $H_{1}$. 则由定理 7.2, $P^{\prime}$ 在 $O X$ 上, 且由于 $P, G_{2}, G_{3}, H_{1}$ 共圆, 故 $P^{\prime}, G_{2}, G_{3}, A$ 共圆, 显然有 $A O$是此圆直径, 于是 $\angle A P^{\prime} O=90^{\circ}$, 故有 $A, P^{\prime}, H_{1}, X$ 共圆, 且由 $G_{2} G_{3}$ 是 $A H_{1}$中垂线知 $P$ 也在此圆上. 于是有 $\measuredangle G_{1} V P=\measuredangle G_{1} H_{1} P=\measuredangle X A P$, 故 $A U / / G_{1} V$ ，又 $\odot(A B C)$ 的补像是 $\odot\left(G_{1} G_{2} G_{3}\right)$, 故 $V$ 为 $G$ 的补点. 而 $\measuredangle i X A O=\measuredangle O X A=$ $\measuredangle P^{\prime} H_{1} A=\measuredangle H_{1} A P$,于是结论成立.



有了这些东西后, 就可以来看最后一部分内容了.

## VIII. 另一个黄氏点

定理 8.1 平面上给定一三角形 $\triangle A B C$, 平面上有四点 $X, P, Q, R$, 满足 $A B C X \backsim A E F P \backsim D B F Q \backsim D E C R$, 则 $\odot(Q F P), \odot(R D Q), \odot(P E R)$, $\odot(D E F)$ 共点 $Y^{\prime}$.

证明 容易看出 $P E R Q D F$ 是一个完美六边形, 于是由定理 6.1 立得结论成立.

类似第一节的思考, 如何不用多圆共点做出这个点 $Y^{\prime}$ 呢? 相信读者已经可以猜测出如下定理了. 下面为叙述方便, 记 $O X$ 关于中点三角形 $\triangle G_{1} G_{2} G_{3}$ 的逆 Steiner 点为 $S(X)$.

## 定理 $8.2 \quad Y^{\prime} \equiv S(X)$.

这次的证明可不如定理 2.1 那么轻松了, 我们需要如下两个引理的支撑.

引理 8.1 平面上一三角形 $\triangle A B C$ 以及任意一点 $X$, 若 $P$ 是 $\triangle A X_{b} X_{c}$ 的垂心, 则有 $\triangle P E F$ 与 $\triangle X B C$ 逆相似.

证明 首先

$$
\measuredangle B A P=\measuredangle X X_{c} X_{b}=\measuredangle X A C
$$

故 $A P, A X$ 是 $\angle B A C$ 的一对等角线. 又

$$
\begin{aligned}
\frac{A P}{A X} & =\frac{A P}{X_{b} X_{c}} \cdot \frac{X_{b} X_{c}}{A X} \\
& =\cot \angle B A C \cdot \sin \angle B A C \\
& =\cos \angle B A C=\frac{E F}{B C},
\end{aligned}
$$

故有 $A E F P \backsim A B C X$, 于是引理得证.

引理 8.2 给定 $\triangle A B C$ 和一点 $X$, 过 $X_{a}$ 做 $A X$ 的平行线交 $A H$ 于 $U$, 则 $\angle U S(X) X_{a}=90^{\circ}$.

证明 只需证 $U, H_{1}, X_{a}, S(X)$ 共圆. 由 $U X_{a} X A$ 是平行四边形知以 $A X$和 $U X_{a}$ 为直径的两圆是等圆, 且连心线与 $G_{2} G_{3}$ 垂直, 且 $A$ 和 $D$ 关于 $G_{2} G_{3}$对称, 于是两圆关于 $G_{2} G_{3}$ 对称, 下面由定理 7.2 知 $S(X)$ 在 $\odot\left(X_{a} X_{b} X_{c}\right)$ 上且 $S(X) X_{a}, G_{2} G_{3}, X_{b} X_{c}$ 共点, 记为点 $V$. 有 $V$ 到以 $A X$ 和 $U X_{a}$ 为直径的两圆的圆幂相等, 而

$$
\overline{V S(X)} \cdot \overline{V X_{a}}=\overline{V X_{b}} \cdot \overline{V X_{c}},
$$

因此 $S(X)$ 在以 $X_{a} U$ 为直径的圆上, 引理得证.



下面我们可以来看定理 8.2 的证明了.

证明 只要证明 $\odot(D Q R)$ 过 $S(X)$. 利用引理 8.2 知只需证明 $\angle X_{a} Q U=$ $90^{\circ}$, 由引理 8.1 知 $X X_{a} Q X_{c}$ 是平行四边形, 于是 $Q X_{c} A U$ 亦是平行四边形, 故 $\measuredangle B D Q=\measuredangle X A B=\measuredangle X_{a} U Q$, 于是 $Q$ 在以 $X_{a} U$ 为直径的圆上, 证毕!

下面我们可以仿照着 Section 3 的路数提出一个问题了, 对于平面上一点 $X$及其Ceva三角形 $\triangle X_{1} X_{2} X_{3}, X$ 满足什么条件时, 才会有 $\triangle S\left(X_{1}\right) S\left(X_{2}\right) S\left(X_{3}\right)$ 与原三角形 $\triangle A B C$ 的透视? 当 $X$ 在 $\triangle A B C$ 的三边上时, 结论是平凡的, 还有没有其他的情况呢? 回答是肯定的, 而且这时满足条件的 $X$ 其实还是我们的 “老熟人”. 下面我们分别记 $S\left(X_{1}\right), S\left(X_{2}\right), S\left(X_{3}\right)$ 为 $U, V, W$.

定理 8.3 当 $X$ 在 $\odot(A B C)$ 上时, $\triangle U V W$ 与 $\triangle A B C$ 透视.

证明 由引理 7.1 立得 $A U, B V, C W$ 都经过 $X$ 的补点, 结论显然.

注 8.1 这同时说明了透视中心的轨迹为九点圆.

既然说是老熟人那自然不可能只有一个外接圆, 来看下面的定理.

定理 8.4 当 $X$ 在 $\triangle A B C$ 的 Euler 线上时, $\triangle U V W$ 与 $\triangle A B C$ 透视.

我见到的此定理的几何法证明是由百度贴吧 id 为“forever豪 3 ” 的网友给出,十分繁复, 要用到 [2] 中的结论. 在此我们采用重心坐标的计算方法, 并顺带解决必要性的问题.

定理 8.5 $\triangle U V W$ 与 $\triangle A B C$ 透视等价于 $X$ 在 $\triangle A B C$ 的三边或 Euler 线
或外接圆上.

证明之前先看一个引理, 它来自于 [7] 的 Proposition 11.4.3, 这里不再给出证明。

引理 8.3 设点 $X(\neq O)$ 的重心坐标是 $(p, q, r)$, 则其关于外接圆的反演点 $i X$ 的重心坐标为

$$
\left(-p^{2}+\frac{c^{2}-a^{2}}{b^{2}} p q+\frac{b^{2}-a^{2}}{c^{2}} p r+\frac{a^{2}\left(b^{2}+c^{2}-a^{2}\right)}{b^{2} c^{2}} q r,,\right)
$$

后面的两项坐标即为第一项的轮换.

下面我们就定理 8.4 和定理 8.5 给出证明.

证明 由引理 7.1, $\triangle U V W$ 与 $\triangle A B C$ 透视等价于 $\triangle i X_{1} i X_{2} i X_{3}$ 与 $\triangle A B C$透视, 且这两个三角形的透视中心为等角共轭点(这在后面的计算中不会用到).设 $X$ 的重心坐标为 $(p, q, r)$, 则 $X_{1}(0, q, r)$, 于是

$$
i X_{1}\left(\frac{a^{2}\left(b^{2}+c^{2}-a^{2}\right)}{b^{2} c^{2}} q r,-q^{2}+\frac{a^{2}-b^{2}}{c^{2}} q r,-r^{2}+\frac{a^{2}-c^{2}}{b^{2}} q r\right) .
$$

故直线 $A i X_{1}$ 的重心坐标为

$$
) \wedge\left(\frac{a^{2}\left(b^{2}+c^{2}-a^{2}\right)}{b^{2} c^{2}} q r,-q^{2}+\frac{a^{2}-b^{2}}{c^{2}} q r,-r^{2}+\frac{a^{2}-c^{2}}{b^{2}} q r\right)=\left(\begin{array}{c}
0 \\
r^{2}-\frac{a^{2}-c^{2}}{b^{2}} q r \\
-q^{2}+\frac{a^{2}-b^{2}}{c^{2}} q r
\end{array}\right)
$$

轮换即得 $B i X_{2}, C i X_{3}$ 的表达式, 于是三线共点等价于

$$
\left|\begin{array}{ccc}
0 & -r^{2}+\frac{b^{2}-c^{2}}{a^{2}} r p & q^{2}-\frac{c^{2}-b^{2}}{a^{2}} p q \\
r^{2}-\frac{a^{2}-c^{2}}{b^{2}} q r & 0 & -p^{2}+\frac{c^{2}-a^{2}}{b^{2}} p q \\
-q^{2}+\frac{a^{2}-b^{2}}{c^{2}} q r & p^{2}-\frac{b^{2}-a^{2}}{c^{2}} r p & 0
\end{array}\right|=0 .
$$

下面记 $\frac{b^{2}-c^{2}}{a^{2}}=A^{\prime}, \frac{c^{2}-a^{2}}{b^{2}}=B^{\prime}, \frac{a^{2}-b^{2}}{c^{2}}=C^{\prime}$, 展开上述行列式, 得

$$
\begin{aligned}
& \operatorname{pqr}\left[\left(B^{\prime}+B^{\prime} C^{\prime}\right) q^{2} r+\left(C^{\prime}+C^{\prime} A^{\prime}\right) r^{2} p+\left(A^{\prime}+A^{\prime} B^{\prime}\right) p^{2} q+\left(C^{\prime}-\right.\right. \\
& \left.\left.B^{\prime} C^{\prime}\right) q r^{2}+\left(A^{\prime}-C^{\prime} A^{\prime}\right) r p^{2}+\left(B^{\prime}-A^{\prime} B^{\prime}\right) p q^{2}+2 A^{\prime} B^{\prime} C^{\prime} p q r\right]=0 .
\end{aligned}
$$

这是一个六次方程, 其中有 $p, q, r$ 三项因子, 分别表示 $\triangle A B C$ 的三边. 下面由定理 8.3 , 剩余的三次式中必定有代表着 $\odot(A B C)$ 的 $a^{2} q r+b^{2} r p+c^{2} p q$ 的因子, 于是只剩下一个一次式, 也即代表着一条直线. 而重心 $G$ 显然满足要求( $A i G_{1}$ 经过陪位重心), 又结合定理 4.8 和引理 3.2 可得垂心也满足条件, 于是剩下的这个一次式恰代表直线 $H G$, 也就是 Euler 线, 这就完成了证明.

## IX. 后记与致谢

至此, 我们基本已经完成了对这个特殊的完美六边形的一对黄氏点的性质的挖掘, 但仍有很多不足之处, 比如定理 8.4 笔者并没有给出一个较好的几何法证明, 只得靠计算来补足; 另外, 在命题 3.1, 命题 3.2 和注 8.1 中笔者都对透视中心的轨迹进行了探究, 但定理 8.4 中透视中心的轨迹却没有提到. 事实上笔者发现这个轨迹是一条四次曲线, 其等角共轭像是一条圆锥曲线, 也即 $X$ 在 Euler 线

上时 $\triangle i X_{1} i X_{2} i X_{3}$ 与 $\triangle A B C$ 透视中心的轨迹是一条雉线, 但由于自身能力有限, 无法给出一个证明了. 但在这里给想证明这个结论或想研究这条雉线性质的读者提供一条线索吧, 笔者在 [6] 中看到了这条雉线的身影, 希望会有帮助.

最后, 笔者在此由衰地向为此文做出了巨大帮助的朋友们表示感谢! 他们分别是(以下排名不分先后): 吃喝睡 (QQ好友), 清华大学 杜俊辰, forever豪3 (贴吧 id), 南京 顾冬华. 感谢他们!

## 参考文献

[1] 崔云制, 1927 高次曲线专题, https://tieba.baidu.com/p/5900873330

[2] 杨铮, 1975 一个猜想, https://tieba.baidu.com/p/5912068572

[3] 赵勇, 完美六边形研究综述,

https://wenku.baidu.com/view/e0239e01eff9aef8941e061e.html(2011)

[4] Akopyan, A. and Zaslavsky, A., Geometry of Conics, American Mathematics Society,United State of America(2007)

[5] Kimberling,C.,Encyclopedia of Triangle Centers, https://faculty.evansville.edu/ck6/encyclopedia/ETC.html

[6] Lozada,C.E.,Re: N, NPC, Reflections ,https://groups.io/g/euclid/message/421

[7] Lozada,C.E.,Re: N, NPC, Reflections ,https://groups.io/g/euclid/message/421

[8] Douillet,P.L.,Translation of the Kimberling's Glossary into barycentrics, GNU Free Documentation License(2018)

[9] Johnson,R.A.,Advanced Euclidean Geometry, Harbin Institute of Technology Press(2012)

