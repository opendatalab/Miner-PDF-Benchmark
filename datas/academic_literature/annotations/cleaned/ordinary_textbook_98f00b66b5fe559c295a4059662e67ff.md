# 三角形的伪外接圆 

黄子宸 ${ }^{1}$ 卢圣 ${ }^{2}$

(1. 浙江省宁波市象山县第三中学 315700 ;

2. 广西钦州市新兴街 30 号祥和景都 2 栋 2 单元 535000 )

本文对平面几何一个新的几何构型进行研究, 获得了一系列有趣的结果, 现将有关研究结果整理成文供大家参考.

## 一. 从一道预选题谈起

第 43 届 IMO 有如下一道平面几何预选题:

问题. 已知锐角 $\triangle A B C$ 的内切圆 $\odot I$ 与边 $B C$ 切于点 $K, A D$ 是 $\triangle A B C$的高, $M$ 是 $A D$ 的中点. 如果 $N$ 是 $\odot I$ 与 $K M$ 的交点, 证明: $\odot I$ 与 $\triangle B C N$ 的外接圆相切于点 $N$.

该试题所要证明的结论 (过三角形两个顶点且与内切圆相切的圆) 是一个新出现的几何构型, 这引起了笔者研究的兴趣. 下面我们逐步探索这个几何构型的性质.

为区别于学界对伪内切圆的称呼, 我们将过三角形两顶点且与内切圆相切的圆称为三角形的伪外接圆. 由对等的思想我们不难看出, 三角形对应着三个伪外接圆 (如图 1-1).

为便于行文, 先约定下列符号的几何意义:

$\triangle A B C$ 中, $\omega_{1}, \omega_{2}, \omega_{3}$ 表示过 $\angle A, \angle B, \angle C$ 所对边的



图 1-1 两个顶点的三个伪外接圆, $S, R, p$ 表示 $\triangle A B C$ 的面积, 外接圆半径, 半周长, $a, b, c$ 表示三边长, $I, I_{1}, I_{2}, I_{3}$ 表示 $\triangle A B C$ 的内心和三个旁心, $r, r_{a}, r_{b}, r_{c}$ 表示 $\triangle A B C$ 的内切圆和旁切圆半径. $D, E, F$ 表示三个伪外接圆与内切圆的切点.内切圆与三边切于 $X, Y, Z$ 三点.

以上约定的符号及字母, 我们将在文中直接使用, 不再一一反复作说明, 文
中其余字母标记以文中说明为准, 请读者详察.

## 二. 一系列引理

下面给出的一系列引理, 将会在全文的论述中反复使用到, 请读者先熟悉.为确保论证的流畅, 在此统一给出这些引理.

引理 1. $P$ 为 $\odot O_{1}$ 与 $\odot O_{2}$ 的交点, $A B$ 为 $\odot O_{2}$ 的一条弦, $A B$ 切 $\odot O_{1}$ 于 $Q$,则 $P Q$ 平分 $\angle A P B$ 的充要条件是 $\odot O_{1}$ 与 $\odot O_{2}$ 内切.

引理 1 证明不难, 不再赘述.

引理 $2^{[1]} \cdot \cos ^{2} \frac{A}{2}=\frac{p(p-a)}{b c}, \cos ^{2} \frac{B}{2}=\frac{p(p-b)}{c a}, \cos ^{2} \frac{C}{2}=\frac{p(p-c)}{a b}$;

$\sin ^{2} \frac{A}{2}=\frac{(p-b)(p-c)}{b c}, \sin ^{2} \frac{B}{2}=\frac{(p-c)(p-a)}{c a}, \sin ^{2} \frac{C}{2}=\frac{(p-a)(p-b)}{a b}$.

引理 $3^{[1]}$. 与 $\triangle A B C$ 外接圆切于 $B$ 和 $C$ 的切线交于 $P$, 则直线 $A P$ 为 $\angle B A C$ 所对的共轭中线 (又称类似中线, 陪位中线).

引理 $\mathbf{4}^{[1]} . \quad p(p-a)=r_{b} r_{c}, p(p-b)=r_{c} r_{a}, p(p-c)=r_{a} r_{b}$,

$$
(p-b)(p-c)=r r_{a}, \quad(p-c)(p-a)=r r_{b}, \quad(p-a)(p-b)=r r_{c}
$$

引理 $5^{[1]} \cdot r=4 R \sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}, \quad r_{a}=4 R \sin \frac{A}{2} \cos \frac{B}{2} \cos \frac{C}{2}$,

$$
r_{b}=4 R \cos \frac{A}{2} \sin \frac{B}{2} \cos \frac{C}{2}, \quad r_{c}=4 R \cos \frac{A}{2} \cos \frac{B}{2} \sin \frac{C}{2} .
$$

引理 $\mathbf{6}^{[2]} . S=\frac{a b c}{4 R}=r p=\sqrt{r r_{a} r_{b} r_{c}}=2 R^{2} \sin A \sin B \sin C$.

引理 $7^{[2]} \cdot \sin 2 A+\sin 2 B+\sin 2 C=4 \sin A \sin B \sin C$.

引理 8. $\frac{a^{2}}{r_{a}}+\frac{b^{2}}{r_{b}}+\frac{c^{2}}{r_{c}}=4(R+r)$.

引理 8 的证明 由引理 5 得

$$
r_{b} r_{c}=4 R^{2} \cos ^{2} \frac{A}{2} \sin B \sin C=b c \cos ^{2} \frac{A}{2},
$$

所以

$$
a^{2} r_{b} r_{c}=a^{2} b c \cos ^{2} \frac{A}{2}=4 S R^{2} \sin A(1+\cos A)=4 S R^{2}\left(\sin A+\frac{1}{2} \sin 2 A\right) .
$$

同理

$$
b^{2} r_{c} r_{a}=4 S R^{2}\left(\sin B+\frac{1}{2} \sin 2 B\right), c^{2} r_{a} r_{b}=4 S R^{2}\left(\sin C+\frac{1}{2} \sin 2 C\right) .
$$

结合引理 7 得

$$
\begin{aligned}
& a^{2} r_{b} r_{c}+b^{2} r_{c} r_{a}+c^{2} r_{a} r_{b} \\
= & 4 S R^{2}\left(\frac{1}{2} \sin 2 A+\frac{1}{2} \sin 2 B+\frac{1}{2} \sin 2 C+\sin A+\sin B+\sin C\right) \\
= & 4 S R^{2}(2 \sin A \sin B \sin C+\sin A+\sin B+\sin C) \\
= & 4 S\left[2 R^{2} \sin A \sin B \sin C+\frac{R}{2}(2 R \sin A+2 R \sin B+2 R \sin C)\right] \\
= & 4 S(S+R p) .
\end{aligned}
$$

所以

$$
\frac{a^{2}}{r_{a}}+\frac{b^{2}}{r_{b}}+\frac{c^{2}}{r_{c}}=\frac{a^{2} r_{b} r_{c}+b^{2} r_{c} r_{a}+c^{2} r_{a} r_{b}}{r_{a} r_{b} r_{c}}=\frac{4 S r(S+R p)}{S^{2}}=4(R+r) .
$$

引理 $\mathbf{9}^{[2]} \cdot r_{a}+r_{b}+r_{c}=4 R+r$.

引理 $10^{[3]} . r^{2}+r_{a}^{2}+r_{b}^{2}+r_{c}^{2}=16 R^{2}-\left(a^{2}+b^{2}+c^{2}\right)$.

引理 $11^{[2]} \cdot \sin ^{2} \frac{A}{2}+\sin ^{2} \frac{B}{2}+\sin ^{2} \frac{C}{2}=\frac{2 R-r}{2 R}$.

引理 $12^{[2]} \cdot r_{a} r_{b}+r_{b} r_{c}+r_{c} r_{a}=p^{2}$.

引理 $13^{[2]} . b c+c a+a b=p^{2}+4 R r+r^{2}$.

引理 14 ${ }^{[4]}$. 如图 2-1, 小圆 $\odot P$ 与大圆 $\odot O$ 内切, 大圆的两条弦 $A B, C D$ 与 $\odot P$ 切于 $M, N$, 则 $\triangle A B C, \triangle D B C$ 的内心 $I_{1}, I_{2}$ 在 $M N$ 上.

引理 15 ${ }^{[5]}$ 。如图 2-2, 圆内接四边形 $A B C D, I_{1}, I_{2}, I_{3}, I_{4}$ 为 $\triangle A B C, \triangle D B C$, $\triangle A C D, \triangle A B D$ 的内心, $K$ 为 $\triangle A B D$ 的 $\angle D$ 所对的旁心, $J$ 为 $\triangle A C D$ 的 $\angle A$所对的旁心, 则四边形 $I_{1} I_{2} I_{3} I_{4}$ 为矩形, 且 $K, I_{1}, I_{2}, J$ 四点共线.



图 2-1



图 2-2

引理 16. 如图 2-3, $\omega_{1}$ 与 $A B$ 交于 $B, H$, 与 $A C$ 交于 $C, G . \triangle A G H$ 的 $\angle A$所对的旁心为 $J$, 则 $J$ 与 $\triangle A B C$ 的 $\angle A$ 所对的旁心 $I_{1}$ 关于内切圆互为反演点.
引理 16 的证明 如图 2-3, 以 $A$ 为反演中心, $A$ 对 $\omega_{1}$ 的幕为反演幂作反演变换. 在该变换下, $B \rightarrow H, C \rightarrow G, \omega_{1}$ 的像保持不变. 所以 $\triangle A G H$ 的外接圆变换为直线 $B C$.

设 $Y \rightarrow M, Z \rightarrow N$. 从而内切圆变换为过 $M N$且与 $\omega_{1}$ 相切的圆, 设为圆 $\Gamma$. 由于内切圆与 $B C$ 相切,所以圆 $\Gamma$ 与 $A B, A C$ 切于 $N, M$, 且与 $\triangle A G H$ 的外接圆相切. 由曼海姆定理知 $\triangle A G H$ 的 $\angle A$ 所对的旁心 $J$ 为 $M N$ 中点. 由引理 14 知 $\triangle G B C, \triangle H B C$ 的内心 $P, Q$ 在 $M N$ 上. 由曼海姆定理知 $P, Q$ 为 $X Y, X Z$的中点, 即为 $I C, I B$ 与 $X Y, X Z$ 的交点. 从而以内切圆为反演圆的情况下, $B \rightarrow Q, C \rightarrow P$. 由内 (旁)心性质知 $I, B, I_{1}, C$ 四点共圆. 所以在以内切圆为



图 2-3 反演圆的情况下该圆变换为直线 $P Q$, 从而 $I I_{1}$ 与 $P Q$的交点为 $I_{1}$ 关于内切圆的反演点, 而该交点为 $J$, 所以 $J$ 与 $I_{1}$ 关于内切圆互为反演点

引理 $17^{[5]}$. 共轭中线将对边内分成邻边平方的比.

引理 $18^{[6]} . M, N$ 是 $\triangle A B C$ 边 $B C$ 所在直线上的两点, 则 $A M, A N$ 为 $\angle B A C$ 的两条等角线的充要条件是

$$
\frac{B M}{C M} \cdot \frac{B N}{C N}=\frac{A B^{2}}{A C^{2}}
$$

## 三. 三角形的伪外接圆的系列性质

下面我们逐步探索三角形的伪外接圆的性质.

## （一）基本性质

该性质在三角形的伪外接圆中起到基础性的作用, 在本文接下来的论证中将多次用到.

性质 1. $D, X, I_{1}$ 共线, 且 $\omega_{1}$ 过 $X I_{1}$ 的中点.

证明 如图 3-1-1, 设 $L$ 为 $D X$ 的中点, 延长 $D X$ 交伪外接圆于 $J$, 延长 $X J$至 $I^{\prime}$ 使 $J X=J I^{\prime}$. 易知

$$
B X \cdot C X=J X \cdot X D=\frac{1}{2} X I^{\prime} \cdot X D=X I^{\prime} \cdot X L \text {. }
$$

所以 $B, I^{\prime}, C, L$ 四点共圆. 取 $I I^{\prime}$ 的中点 $K$, 则 $K J / / I X$. 由 $I X \perp B C$, 所以
$K J \perp B C$. 由引理 1 知 $J B=J C$, 故 $K J$ 垂直平分 $B C$.

又易知 $I L \perp D X$, 所以 $K$ 在 $L I^{\prime}$ 的垂直平分线上, 从而 $K$ 为圆 $B I^{\prime} C L$ 的圆心. 而 $K I=K L$, 因此 $B, I^{\prime}, C, L, I$ 五点共圆, 直径为 $I I^{\prime}$. 于是 $B I \perp B I^{\prime}$, $C I \perp C I^{\prime}$. 故 $I^{\prime}$ 为 $\angle A$ 所对的旁心, 即 $D, X, I_{1}$ 三点共线.



图 3-1-1



图 3-1-2

性质 1 对 $\omega_{1}, \omega_{2}$ 也成立, 证明方法一样, 不再赘述. 事实上, 性质 1 的逆命题也是成立的, 并可以给出伪外接圆的另一个作图方法.

性质 $\mathbf{1}^{\prime}$. 直线 $I_{1} X$ 交内切圆于 $D$, 则 $\triangle B C D$ 的外接圆与内切圆相切于点 $D$.

证明 如图 3-1-2, 取 $D X, I_{1} X$ 的中点 $L, J$, 易知 $I L \perp D X, B I \perp B I_{1}$, $C I \perp C I_{1}$, 从而 $B, I_{1}, C, L, I$ 五点共圆, 直径为 $I I_{1}$. 因此

$$
B X \cdot C X=I_{1} X \cdot X L=\frac{1}{2} I_{1} X \cdot X D=J X \cdot X D
$$

所以 $B, J, C, D$ 四点共圆.

取旁切圆 $\odot I_{1}$ 与 $B C$ 的切点 $X_{1}$, 易知 $B X_{1}=C X, J X=J X_{1}, \angle J X C=$ $\angle J X_{1} B$. 所以 $\triangle J X C \cong \triangle J X_{1} B$. 从而 $J B=J C$, 即得 $\angle B D X=\angle C D X$. 故由引理 1 知圆 $B J C D$ 与内切圆相切于点 $D$.

## (二) 若干结合关系

性质 2. $D X, E Y, F Z$ 三线共点, 且该点为三个伪外接圆的根心.

证明 如图 3-2, 取 $\triangle A B C$ 的三个旁心 $I_{1}, I_{2}, I_{3}$, 设 $D I_{1}, E I_{2}, F I_{3}$ 分别与 $\omega_{1}, \omega_{2}, \omega_{3}$ 交于另外的 $J, K, L$.

由性质 1 知 $I_{1}, I_{2}, I_{3}$ 分别在直线 $D X, E Y, F Z$ 上. 由内 (旁) 心性质及切点三角形性质知 $I_{2} I_{3} / / Y Z, I_{3} I_{1} / / Z X, I_{1} I_{2} / / X Y$. 所以 $\triangle I_{1} I_{2} I_{3}$ 与 $\triangle X Y Z$
位似. 故 $I_{1} X, I_{2} Y, I_{3} Z$ 三线共点, 即 $D X, E Y, F Z$ 三线共点, 设该点为 $U$.

由性质 1 知 $J, K, L$ 分别为 $X I_{1}, Y I_{2}, Z I_{3}$ 的中点. 所以 $L J / / Z X$. 于是 $\angle D F L=\angle D F Z=\angle D X Z=\angle D J L$. 因此 $D, F, J, L$ 四点共圆. 故 $D U \cdot J U=F U \cdot L U$.

同理 $D U \cdot J U=E U \cdot K U$, 即 $U$ 对 $\omega_{1}, \omega_{2}, \omega_{3}$ 的幂相等. 所以 $U$ 为 $\omega_{1}, \omega_{2}$, $\omega_{3}$ 的根心.



图 3-2



图 3-3

性质 3. $A D, B E, C F$ 三线共点.

证明 如图 3-3, 由性质 2 知 $D X, E Y, F Z$ 三线共点. 由塞瓦定理有

$$
\frac{Z D}{D Y} \cdot \frac{Y F}{F X} \cdot \frac{X E}{E Z}=1
$$

又

$$
\frac{S_{\triangle A B D}}{S_{\triangle A C D}}=\frac{A B \cdot Z D \cdot \sin \angle A Z D}{A C \cdot D Y \cdot \sin \angle A Y D}=\frac{A B \cdot Z D \cdot \sin \angle D Y Z}{A C \cdot D Y \cdot \sin \angle D Z Y}=\frac{A B \cdot Z D^{2}}{A C \cdot D Y^{2}}
$$

同理

$$
\frac{S_{\triangle B C E}}{S_{\triangle B A E}}=\frac{B C \cdot X E^{2}}{A B \cdot E Z^{2}}, \quad \frac{S_{\triangle C A F}}{S_{\triangle C B F}}=\frac{A C \cdot Y F^{2}}{B C \cdot F X^{2}} .
$$

所以

$$
\frac{S_{\triangle A B D}}{S_{\triangle A C D}} \cdot \frac{S_{\triangle B C E}}{S_{\triangle B A E}} \cdot \frac{S_{\triangle C A F}}{S_{\triangle C B F}}=\left(\frac{Z D}{D Y} \cdot \frac{X E}{E Z} \cdot \frac{Y F}{F X}\right)^{2}=1 .
$$

因此 $A D, B E, C F$ 三线共点.

性质 4. 直线 $A D, B E, C F$ 分别交 $\omega_{1}, \omega_{2}, \omega_{3}$ 于另一点 $K, J, T$, 直线 $B T$, $C J$ 交于 $L$, 直线 $C K, A T$ 交于 $M$, 直线 $A J, B K$ 交于 $N$, 则 $A L, B M, C N$ 三线共点.

证明 如图 3-4, 设直线 $A D, B E, C F$ 分别交 $B C, C A, A B$ 于 $P, Q, R$. 易知

$$
\frac{A B \cdot \sin \angle B A L}{A C \cdot \sin \angle C A L}=\frac{S_{\triangle A B L}}{S_{\triangle A C L}}=\frac{A B \cdot B L \cdot \sin \angle A B L}{A C \cdot C L \cdot \sin \angle A C L} .
$$

因此

$$
\begin{aligned}
\frac{\sin \angle B A L}{\sin \angle C A L} & =\frac{B L}{C L} \cdot \frac{\sin \angle A B L}{\sin \angle A C L} \\
& =\frac{\sin \angle B C L}{\sin \angle C B L} \cdot \frac{\sin \angle A B L}{\sin \angle A C L} \\
& =\frac{\sin \angle B C J}{\sin \angle A C J} \cdot \frac{\sin \angle A B T}{\sin \angle C B T}
\end{aligned}
$$

又由

$$
\frac{B J}{Q J}=\frac{S_{\triangle B J C}}{S_{\triangle Q J C}}=\frac{B C \cdot \sin \angle B C J}{Q C \cdot \sin \angle A C J}
$$

所以

$$
\frac{\sin \angle B C J}{\sin \angle A C J}=\frac{B J}{B C} \cdot \frac{Q C}{Q J}
$$

同理

$$
\frac{\sin \angle A B T}{\sin \angle C B T}=\frac{B C}{C T} \cdot \frac{T R}{B R}
$$

将 (2),(3) 代人 (1), 得

$$
\frac{\sin \angle B A L}{\sin \angle C A L}=\frac{B J}{C T} \cdot \frac{Q C}{Q J} \cdot \frac{T R}{B R}
$$

同理

$$
\begin{aligned}
& \frac{\sin \angle C B M}{\sin \angle A B M}=\frac{C T}{A K} \cdot \frac{A R}{T R} \cdot \frac{P K}{C P}, \\
& \frac{\sin \angle A C T}{\sin \angle B C T}=\frac{A K}{B J} \cdot \frac{B P}{P K} \cdot \frac{Q J}{A Q} .
\end{aligned}
$$

将 (4),(5),(6) 三式相乘并结合性质 3 得

$$
\frac{\sin \angle B A L}{\sin \angle C A L} \cdot \frac{\sin \angle C B M}{\sin \angle A B M} \cdot \frac{\sin \angle A C T}{\sin \angle B C T}=\frac{Q C}{A Q} \cdot \frac{A R}{B R} \cdot \frac{B P}{C P}=1 .
$$

由角元塞瓦定理知 $A L, B M, C N$ 三线共点.



图 3-4



图 3-5
性质 5. 过 $D, E, F$ 作内切圆的切线, 分别交 $B C, C A, A B$ 于 $P, Q, R$, 则 $P$, $Q, R$ 共线且该线垂直于 $O I$.

证明 如图 3-5, 易知 $D P$ 也为 $\omega_{1}$ 的切线. 所以 $D P^{2}=P B \cdot P C$, 即 $P$ 对内切圆的幂等于 $P$ 对 $\triangle A B C$ 外接圆的幂. 所以 $P$ 在内切圆和 $\triangle A B C$ 外接圆的根轴上. 同理, $Q, R$ 在内切圆和 $\triangle A B C$ 外接圆的根轴上. 故 $P, Q, R$ 共线且该线垂直与 $O I$.

注. 性质 5 为北京人大附中杨泓暕同学提出并证明.

## (三) 一些比例关系

性质 6. 设 $\omega_{2}$ 交 $A B$ 于 $T, \omega_{3}$ 交 $A C$ 于 $L$, 则 $\frac{Z T}{Z B}=\frac{Y L}{Y C}$.

证明 如图 3-6, 取 $Y Z$ 的中点 $M$. 由引理 3 得 $\angle Z E M=\angle A E Y=\angle Y E C$. 注意到 $\angle M Z E=$ $\angle C Y E$, 得 $\triangle M Z E \sim \triangle C Y E$, 从而 $\angle Z M E=$ $\angle Y C E$. 于是 $M, E, C, Y$ 四点共圆.

因此 $\angle Z T E=180^{\circ}-\angle A C E=\angle E M Y$,所以 $M, E, T, Z$ 四点共圆. 于是 $\angle Z T M=$ $\angle Z E M=\angle A E Y=\angle Y E C=\angle Y M C$. 注意到



图 3-6 $\angle T Z M=\angle M Y C$, 故 $\triangle T Z M \sim \triangle M Y C$, 从而 $T Z \cdot Y C=Z M \cdot M Y$. 同理 $L Y \cdot Z B=Z M \cdot M Y$. 所以 $\frac{Z T}{Z B}=\frac{Y L}{Y C}$.

性质 7. $\omega_{1}$ 与 $C A$ 交于另一点 $G$, 与 $A B$ 交于另一点 $H ; \omega_{2}$ 与 $A B$ 交于另一点 $J$, 交 $B C$ 于另一点 $K ; \omega_{3}$ 交 $B C$ 于另一点 $L$, 交 $C A$ 于另一点 $T$, 则

$$
\frac{G D}{D H} \cdot \frac{J E}{E K} \cdot \frac{L F}{F T}=\frac{L X}{X K} \cdot \frac{G Y}{Y T} \cdot \frac{J Z}{Z H}=1 .
$$

证明 如图 3-7, 由引理 1 知 $D X, D Y, D Z$ 平分 $\angle B D C, \angle C D G, \angle B D H$, 故

$$
\frac{H D}{H Z}=\frac{B D}{B Z}=\frac{B D}{B X}=\frac{C D}{C X}=\frac{C D}{C Y}=\frac{D G}{G Y}
$$

即 $\frac{G D}{D H}=\frac{G Y}{Z H}$. 同理

$$
\frac{J E}{E K}=\frac{J Z}{X K}, \quad \frac{L F}{F T}=\frac{L X}{Y T}
$$

结合性质 6 得

$\frac{G D}{D H} \cdot \frac{J E}{E K} \cdot \frac{L F}{F T}=\frac{G Y}{Z H} \cdot \frac{J Z}{X K} \cdot \frac{L X}{Y T}=\frac{J Z}{Y T} \cdot \frac{L X}{Z H} \cdot \frac{G Y}{X K}=\frac{B Z}{C Y} \cdot \frac{C X}{Z A} \cdot \frac{A Y}{B X}=1$.



图 3-7



图 3-8

性质 8. 设 $\omega_{1}, \omega_{2}, \omega_{3}$ 两两相交于 $P, Q, R$, 则 $\frac{Q D}{D R} \cdot \frac{R E}{E P} \cdot \frac{P F}{F Q}=1$.

证明 如图 3-8, 由性质 2 知 $D X, B Q, C R$ 三线共点于 $\omega_{1}, \omega_{2}, \omega_{3}$ 的根心 $U$,由引理 1 及正弦定理可得

$$
\frac{Q D}{D R}=\frac{\sin \angle Q B D}{\sin \angle D C R}=\frac{\sin \angle Q B D}{\sin \angle B D U} \cdot \frac{\sin \angle C D U}{\sin \angle D C R}=\frac{U D}{B U} \cdot \frac{C U}{U D}=\frac{C U}{B U} .
$$

同理

$$
\frac{R E}{E P}=\frac{A U}{C U}, \quad \frac{P F}{F Q}=\frac{B U}{A U}
$$

所以

$$
\frac{Q D}{D R} \cdot \frac{R E}{E P} \cdot \frac{P F}{F Q}=\frac{C U}{B U} \cdot \frac{A U}{C U} \cdot \frac{B U}{A U}=1
$$

注. 性质 8 由北京人大附中杨泓暕同学证明.

性质 9. 直线 $A D$ 交 $B C$ 与 $J$, 则 $\frac{B J}{C J}=\left(\frac{B X}{C X}\right)^{3}$.

证明 如图 3-9, 取 $X Z$ 的中点 $M$. 由引理 1 及引理 3 知 $\angle Z D M=$ $\angle B D X=\angle X D C$. 又易知 $\angle M Z D=\angle C X D$, 从而 $\triangle Z D M \sim \triangle X D C$. 所以

$$
Z D=\frac{X D \cdot Z M}{X C}=\frac{X D \cdot Z X}{2 X C}
$$

同理 $Y D=\frac{X D \cdot Y X}{2 X B}$. 故

$$
\frac{Z D}{Y D}=\frac{X B}{X C} \cdot \frac{Z X}{Y X}=\frac{X B}{X C} \cdot \frac{\sin \angle Z X B}{\sin \angle Y X C}=\frac{X B}{X C} \cdot \frac{\cos \frac{B}{2}}{\cos \frac{C}{2}} .
$$

则由性质 3 的证明及引理 2 知

$$
\begin{aligned}
\frac{B J}{J C}=\frac{S_{\triangle A B D}}{S_{\triangle A C D}} & =\frac{A B \cdot Z D^{2}}{A C \cdot Y D^{2}}=\frac{c}{b} \cdot\left(\frac{X B}{X C}\right)^{2} \cdot \frac{\cos ^{2} \frac{B}{2}}{\cos ^{2} \frac{C}{2}} \\
& =\left(\frac{X B}{X C}\right)^{2} \cdot \frac{p-b}{p-c}=\left(\frac{X B}{X C}\right)^{3}
\end{aligned}
$$



图 3-9



图 3-10

性质 10. 直线 $A D$ 交 $\omega_{1}$ 于另一点 $K$, 则 $\frac{B K}{C K}=\left(\frac{B X}{C X}\right)^{2}$.

证明 如图 3-10, 设直线 $A D$ 交 $B C$ 于 $J$, 由引理 1 及性质 9 得

$$
\begin{aligned}
\frac{B K}{C K} & =\frac{\sin \angle B D K}{\sin \angle C D K}=\frac{\sin \angle A D B}{\sin \angle A D C} \\
& =\frac{S_{\triangle A B D}}{S_{\triangle A C D}} \cdot \frac{C D}{B D}=\frac{B J}{C J} \cdot \frac{C X}{B X} \\
& =\left(\frac{B X}{C X}\right)^{3} \cdot \frac{C X}{B X}=\left(\frac{B X}{C X}\right)^{2} .
\end{aligned}
$$

推论. (字母标记同性质 10) 由性质 9 及性质 10 得 $\left(\frac{B K}{C K}\right)^{3}=\left(\frac{B J}{C J}\right)^{2}$.

(四) 一些计算公式

性质 11. $\mu_{1}, \mu_{2}, \mu_{3}$ 表示 $\omega_{1}, \omega_{2}, \omega_{3}$ 半径, 则

(1) $\mu_{1}=\frac{1}{4}\left(r_{a}+\frac{a^{2}}{r_{a}}\right), \mu_{2}=\frac{1}{4}\left(r_{b}+\frac{b^{2}}{r_{b}}\right), \mu_{3}=\frac{1}{4}\left(r_{c}+\frac{c^{2}}{r_{c}}\right)$;

(2) $\mu_{1}+\mu_{2}+\mu_{3}=2 R+\frac{5}{4} r$;

(3) $\left(4 \mu_{1}-r_{a}\right)\left(4 \mu_{2}-r_{b}\right)\left(4 \mu_{3}-r_{c}\right)=16 R^{2} r$;

(4) $\mu_{1} r_{a}+\mu_{2} r_{b}+\mu_{3} r_{c}+\frac{1}{4} r^{2}=4 R^{2}$.

证明 (1) 仅证 $\omega_{1}$ 的情形, 其余的情形类似可得.

如图 3-11, $M$ 为 $B C$ 中点, $D I_{1}$ 交 $\omega_{1}$ 于 $J, \omega_{1}$ 圆心为 $V_{1}$, 其余字母标记同文前的约定.

由性质 1 知 $\angle X B J=\angle C D J=\angle B D J$, 所以 $\triangle B J X \sim \triangle D J B$. 结合引理 4 得

$$
\begin{aligned}
\left(\frac{1}{2} a\right)^{2}+\left(\frac{1}{2} r_{a}\right)^{2} & =B M^{2}+J M^{2}=B J^{2} \\
& =J X \cdot J D=J X(J X+X D) \\
& =J X^{2}+J X \cdot X D \\
& =J X^{2}+B X \cdot C X \\
& =J X^{2}+r r_{a} .
\end{aligned}
$$

从而

$$
J X^{2}=\left(\frac{1}{2} a\right)^{2}+\left(\frac{1}{2} r_{a}\right)^{2}-r r_{a}
$$



图 3-11

易知 $V_{1} J / / I X$, 所以

$$
J X=J D-X D=J D-\frac{r}{\mu_{1}} J D=J D\left(1-\frac{r}{\mu_{1}}\right) .
$$

从而

$$
\begin{aligned}
1-\frac{r}{\mu_{1}} & =\frac{J X}{J D}=\frac{J X^{2}}{J X \cdot J D}=\frac{J X^{2}}{B J^{2}} \\
& =\frac{\left(\frac{1}{2} a\right)^{2}+\left(\frac{1}{2} r_{a}\right)^{2}-r r_{a}}{\left(\frac{1}{2} a\right)^{2}+\left(\frac{1}{2} r_{a}\right)^{2}} .
\end{aligned}
$$

故 $\mu_{1}=\frac{1}{4}\left(r_{a}+\frac{a^{2}}{r_{a}}\right)$.

(2) 由引理 8 及引理 9 得

$$
\begin{aligned}
\mu_{1}+\mu_{2}+\mu_{3} & =\frac{1}{4}\left(r_{a}+r_{b}+r_{c}+\frac{a^{2}}{r_{a}}+\frac{b^{2}}{r_{b}}+\frac{c^{2}}{r_{c}}\right) \\
& =\frac{1}{4}(4 R+r+4 R+4 r) \\
& =2 R+\frac{5}{4} r .
\end{aligned}
$$

(3) 由引理 6 得

$$
\left(4 \mu_{1}-r_{a}\right)\left(4 \mu_{2}-r_{b}\right)\left(4 \mu_{3}-r_{c}\right)=\frac{a^{2}}{r_{a}} \cdot \frac{b^{2}}{r_{b}} \cdot \frac{c^{2}}{r_{c}}=\frac{r(4 R S)^{2}}{S^{2}}=16 R^{2} r .
$$

(4) 由引理 10 知

$$
\mu_{1} r_{a}+\mu_{2} r_{b}+\mu_{3} r_{c}+\frac{1}{4} r^{2}=\frac{1}{4}\left(r_{a}^{2}+a^{2}+r_{b}^{2}+b^{2}+r_{c}^{2}+c^{2}+r^{2}\right)=4 R^{2}
$$

性质 12. 设 $\omega_{1}$ 与 $C A, A B$ 交于 $M, N$, 直线 $D X$ 交 $\omega_{1}$ 于另一点 $J, V_{1}$ 为 $\omega_{1}$圆心，则

(1)

$$
\begin{array}{ll}
D X=r \sqrt{\frac{r_{a}}{\mu_{1}-r}}, & D J=\mu_{1} \sqrt{\frac{r_{a}}{\mu_{1}-r}}, \\
D B=(p-b) \sqrt{\frac{\mu_{1}}{\mu_{1}-r}}, & D C=(p-c) \sqrt{\frac{\mu_{1}}{\mu_{1}-r}}, \\
D Y=\frac{X Y \cdot D X}{2 B X}, & D Z=\frac{X Z \cdot D X}{2 C X}, \\
Z N=\frac{(p-a)(p-b)^{2}}{a c} . & Y M=\frac{(p-a)(p-c)^{2}}{a b}, \\
D N=\frac{(p-a)(p-b)^{2}}{a c} \sqrt{\frac{\mu_{1}}{\mu_{1}-r}}, & D M=\frac{(p-a)(p-c)^{2}}{a b} \sqrt{\frac{\mu_{1}}{\mu_{1}-r}} .
\end{array}
$$

(2) $A$ 对 $\omega_{1}$ 的幂为 $\frac{r(p-a)(r+4 R)}{a}, B$ 对 $\omega_{2}$ 的幂为 $\frac{r(p-b)(r+4 R)}{b}$, $C$ 对 $\omega_{3}$ 的幂为 $\frac{r(p-c)(r+4 R)}{c}$.

证明 如图 3-12, 由性质 11 知 $J X^{2}=r_{a}\left(\mu_{1}-r\right)$. 所以

$$
\begin{aligned}
D X & =\frac{B X \cdot C X}{J X}=\frac{(p-b)(p-c)}{\sqrt{r_{a}\left(\mu_{1}-r\right)}}=\frac{r r_{a}}{\sqrt{r_{a}\left(\mu_{1}-r\right)}}=r \sqrt{\frac{r_{a}}{\mu_{1}-r}}, \\
D J & =\frac{\mu_{1}}{r} D X=\mu_{1} \sqrt{\frac{r_{a}}{\mu_{1}-r}} .
\end{aligned}
$$

由托勒密定理得 $B J(B D+C D)=D J \cdot B C$, 由角平分线结论得 $\frac{B D}{C D}=\frac{B X}{C X}$.又由性质 11 易知 $B J^{2}=\mu_{1} r_{a}$, 结合上面两式得

$$
D B=(p-b) \sqrt{\frac{\mu_{1}}{\mu_{1}-r}}, \quad D C=(p-c) \sqrt{\frac{\mu_{1}}{\mu_{1}-r}} .
$$

取 $X Y$ 的中点 $T$, 由引理 3 知 $\angle T D Y=\angle C D X=\angle B D X$. 又易知 $\angle D Y T=\angle D X B$, 所以 $\triangle D Y T \sim \triangle D X B$. 从而

$$
D Y=Y T \cdot \frac{D X}{B X}=\frac{X Y \cdot D X}{2 B X} .
$$

同理可得 $D Z$.

延长 $D Z$ 交 $\omega_{1}$ 于另一点 $K$. 由

$$
K Z=D K-D Z=\frac{\mu_{1}}{r} D Z-D Z=\frac{\mu_{1}-r}{r} D Z,
$$

所以

$$
\begin{aligned}
Z N & =\frac{Z K \cdot Z D}{B Z}=\frac{\mu_{1}-r}{r} \cdot \frac{D Z^{2}}{B Z}=\frac{\mu_{1}-r}{r(p-b)} \cdot \frac{X Z^{2} \cdot D Z^{2}}{4 C X^{2}} \\
& =\frac{\mu_{1}-r}{r(p-b)} \cdot \frac{r^{2} r_{a}}{\mu_{1}-r} \cdot \frac{X Z^{2}}{4(p-c)^{2}}=\frac{r r_{a} X Z^{2}}{4(p-b)(p-c)^{2}} \\
& =\frac{(p-b)(p-c)\left(2 r \cos \frac{B}{2}\right)^{2}}{4(p-b)(p-c)^{2}}=\frac{r^{2} \cos ^{2} \frac{B}{2}}{(p-c)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{r^{2} p(p-b)}{a c(p-c)}=\frac{r(p-b) r_{c}(p-c)}{a c(p-c)} \\
& =\frac{(p-a)(p-b)^{2}}{a c} .
\end{aligned}
$$

同理可得 $Y M$.

由角平分线结论有 $\frac{D N}{Z N}=\frac{D B}{Z B}$, 从而求得 $D N$. 同理可得 $D M$.

（2）易知

$$
\begin{aligned}
A N & =A Z-Z N=p-a-\frac{(p-a)(p-b)^{2}}{a c}=\frac{p-a}{a c}\left[a c-(p-b)^{2}\right] \\
& =\frac{(p-a)}{a c}\left[(p-b+p-c)(p-b+p-a)-(p-b)^{2}\right] \\
& =\frac{(p-a)}{a c}[(p-b)(p-c)+(p-c)(p-a)+(p-a)(p-b)] \\
& =\frac{(p-a)}{a c}\left(r r_{a}+r r_{b}+r r_{c}\right)=\frac{(p-a)\left(4 R r+r^{2}\right)}{a c} .
\end{aligned}
$$

所以 $A$ 对 $\omega_{1}$ 的幂为 $A B \cdot A N=\frac{r(p-a)(r+4 R)}{a}$. 同理可得 $B$ 对 $\omega_{2}$ 的幂为 $\frac{r(p-b)(r+4 R)}{b}, C$ 对 $\omega_{3}$ 的幂为 $\frac{r(p-c)(r+4 R)}{c}$.



图 3-12



图 3-13

性质 13. 三个伪外接圆的根心对三个伪外接圆的幂为

$$
\frac{r^{2}(2 R+r)(4 R+r)}{2(2 R-r)^{2}} .
$$

证明 如图 3-13, 字母标记同性质 2 . 由性质 2 知切聚点 $U$ 为三个伪外接圆的根心, 且 $U$ 为 $\triangle X Y Z$ 与 $\triangle I_{1} I_{2} I_{3}$ 的位似中心. 所以

$$
\begin{aligned}
\frac{S_{\triangle A B U}}{S_{\triangle A C U}} & =\frac{A B \cdot Z U \cdot \sin \angle A Z U}{A C \cdot Y U \cdot \sin \angle A Y U}=\frac{A B}{A C} \cdot \frac{I_{3} U}{I_{2} U} \cdot \frac{\sin \angle A Z I_{3}}{\angle A Y I_{2}} \\
& =\frac{A B}{A C} \cdot \frac{\sin \angle I_{3} I_{2} U}{\sin \angle I_{2} I_{3} U} \cdot \frac{\sin \angle A Z I_{3}}{\sin \angle A Y I_{2}}=\frac{A B}{A C} \cdot \frac{\sin \angle A I_{2} Y}{\sin \angle A Y I_{2}} \cdot \frac{\sin \angle A Z I_{3}}{\sin \angle A I_{3} Z} \\
& =\frac{A B}{A C} \cdot \frac{A Y}{A I_{2}} \cdot \frac{A I_{3}}{A Z}=\frac{A B}{A C} \cdot \frac{A I_{3}}{A I_{2}}=\frac{\sin C}{\sin B} \cdot \frac{\cot \angle A I_{3} I_{1}}{\cot \angle A I_{2} I_{1}}
\end{aligned}
$$

$$
=\frac{\sin C}{\sin B} \cdot \frac{\tan \frac{C}{2}}{\tan \frac{B}{2}}=\frac{\sin ^{2} \frac{C}{2}}{\sin ^{2} \frac{B}{2}}
$$

同理

$$
\frac{S_{\triangle A C U}}{S_{\triangle B C U}}=\frac{\sin ^{2} \frac{B}{2}}{\sin ^{2} \frac{A}{2}}, \quad \frac{S_{\triangle B C U}}{S_{\triangle A B U}}=\frac{\sin ^{2} \frac{A}{2}}{\sin ^{2} \frac{C}{2}} .
$$

结合引理 11 得

$$
S_{\triangle B C U}=\frac{\sin ^{2} \frac{A}{2}}{\sin ^{2} \frac{A}{2}+\sin ^{2} \frac{B}{2}+\sin ^{2} \frac{C}{2}} S=2 R S \cdot \frac{\sin ^{2} \frac{A}{2}}{2 R-r} .
$$

令 $\angle I_{1} X B=\theta$, 则 $\sin \theta=\frac{r_{a}}{I_{1} X}$. 所以

$$
\begin{aligned}
U X & =\frac{2 S_{\triangle B C U}}{a \sin \theta}=\frac{4 R S}{2 R-r} \cdot \frac{\sin ^{2} \frac{A}{2}}{a \sin \theta} \\
& =\frac{4 R S}{2 R-r} \cdot \frac{(p-b)(p-c)}{a b c \sin \theta} \\
& =\frac{a b c}{2 R-r} \cdot \frac{(p-b)(p-c)}{a b c \sin \theta} \\
& =\frac{r r_{a}}{2 R-r} \cdot \frac{I_{1} X}{r_{a}}=\frac{r_{a}}{2 R-r} I_{1} X .
\end{aligned}
$$

又 $X D=2 r \sin \theta=\frac{2 r r_{a}}{I_{1} X}$, 因此

$$
\begin{aligned}
U D & =X D-U X=\frac{2 r r_{a}}{I_{1} X}-\frac{r}{2 R-r} I_{1} X \\
& =r\left[\frac{2 r_{a}(2 R-r)-I_{1} X^{2}}{I_{1} X(2 R-r)}\right] \\
& =r\left[\frac{4 R r_{a}-2 r r_{a}-r_{a}^{2}-(b-c)^{2}}{I_{1} X(2 R-r)}\right] .
\end{aligned}
$$

又因为

$$
U J=U X+\frac{1}{2} I_{1} X=\frac{r}{2 R-r} I_{1} X+\frac{1}{2} I_{1} X=\frac{2 R+r}{2(2 R-r)} I_{1} X
$$

故 $U$ 对 $\omega_{1}$ 的幂等于

$$
\begin{aligned}
U D \cdot U J & =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[4 R r_{a}-2 r r_{a}-r_{a}^{2}-(b-c)^{2}\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[4 R r_{a}-2 r r_{a}-r_{a}^{2}-(p-b-p+c)^{2}\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[r_{a}\left(4 R-r_{a}\right)-2 r r_{a}-(p-b)^{2}-(p-c)^{2}+2(p-b)(p-c)\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[r_{a}\left(r_{b}+r_{c}-r\right)-(p-b)^{2}-(p-c)^{2}\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[r_{a} r_{b}+r_{c} r_{a}-r r_{a}-(p-b)^{2}-(p-c)^{2}\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[p^{2}-r_{b} r_{c}-r r_{a}-(p-b)^{2}-(p-c)^{2}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[p^{2}-p(p-a)-(p-b)(p-c)-(p-b)^{2}-(p-c)^{2}\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[a p+(p-b)(p-c)-(p-b+p-c)^{2}\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[a p-a^{2}+p^{2}-b p-c p+b c\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[p^{2}-p(-a+b+c)-a^{2}+b c\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[p^{2}-2 p^{2}+2 a p-a^{2}+b c\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left[a(2 p-a)-p^{2}+b c\right] \\
& =\frac{r(2 R+r)}{2(2 R-r)^{2}} \cdot\left(a b+b c+c a-p^{2}\right) \\
& =\frac{r^{2}(2 R+r)(4 R+r)}{2(2 R-r)^{2}} .
\end{aligned}
$$

## （五）其他性质拾零

性质 14. 直线 $A D$ 交圆 $\omega_{1}$ 于另一点 $K$, 则 $I K$ 平分 $\angle B K C$.

证明 如图 3-14, 以点 $A$ 为圆心, $A$ 对 $\omega_{1}$ 的幂为反演幂, 作反演变换. 在此变换下, $\omega_{1}$ 保持不变, $D, K$ 互为反演点. 设该反演下 $Y \rightarrow M, Z \rightarrow N$. 所以 $\triangle A B C$ 的内切圆的反形为 $\triangle K M N$ 的外接圆. 由于内切圆与 $\omega_{1}$ 切于 $D$, 故 $\triangle K M N$ 的外接圆与 $\omega_{1}$ 切于 $K$. 设 $\omega_{1}$ 交 $C A, A B$ 于另外两点 $L, J$, 由引理 14 知 $\triangle L B C$ 和 $\triangle J B C$ 的内心 $I^{\prime}$ 和 $I^{\prime \prime}$ 在 $M N$ 上.

注意到 $\angle I^{\prime} B I^{\prime \prime}=\angle I B C-\angle I^{\prime} B C=\frac{1}{2} \angle L B J=\frac{1}{2} \angle L C J=\angle I C B-$ $\angle I^{\prime \prime} C B=\angle I^{\prime} C I^{\prime \prime}$, 故 $B, C, I^{\prime}, I^{\prime \prime}$ 四点共圆. 因此 $\angle I I^{\prime} N=\angle I B C=\angle I B N$,从而 $B, N, I, I^{\prime}$ 四点共圆.

又由引理 1 知 $\angle N K B=\frac{1}{2} \angle J K B=\frac{1}{2} \angle J C B=\angle I^{\prime \prime} C B=\angle N I^{\prime} B$, 所以 $B, K, I^{\prime}, N$ 四点共圆. 因此 $I, N, B, K, I^{\prime}$ 五点共圆.

同理 $I, M, C, K, I^{\prime \prime}$ 五点共圆.

因为 $A Z=A Y$, 所以 $\triangle A N I \cong \triangle A M I$, 故 $\angle I K B=\angle I N A=\angle I M A=$ $\angle I K C$.

性质 15. $\omega_{1}$ 与 $C A, A B$ 交于另两点 $L, J, T$ 为 $\triangle A L J$ 的 $\angle A$ 所对的旁心,则 $D T$ 平分 $\angle J D L$.

证明 如图 3-15, 以 $A$ 为反演圆心, $A$ 对圆 $\omega_{1}$ 的幂为反演幂, 符号标记同性
质 14 的证明.

由旁心的性质知 $\angle J T A=\frac{1}{2} \angle A L J=\frac{1}{2} \angle A B C=\angle A B I$, 因此 $J, B, T, I$四点共圆. 这说明在上述反演下 $I, T$ 互为反演点. 由性质 14 的证明知 $K, B$, $N, I ; K, C, M, I$ 分别四点共圆, 故 $D, J, Z, T ; D, L, Y, T$ 分别四点共圆. 又 $\triangle A Z T \cong \triangle A Y T$, 因此 $\angle J D T=\angle B Z T=\angle C Y T=\angle L D T$.



图 3-14



图 3-15

性质 16. $\omega_{1}$ 与 $C A, A B$ 交于 $L, J, T$ 为 $\triangle A L J$ 的 $\angle A$ 所对的旁心, 直线 $A D$ 交 $\omega_{1}$ 于另一点 $K$, 则 $K, X, T, I, D$ 五点共圆.

证明 如图 3-16, 连结 $I K$ 交 $B C$ 于 $G$. 由引理 1 及性质 14 知 $\angle X D C+$ $\angle B K G=90^{\circ}$, 故

$$
\begin{aligned}
\angle X D K & =90^{\circ}-\angle K D C-\angle B K G=90^{\circ}-\angle K B C-\angle B K G \\
& =90^{\circ}-\angle C G K=\angle X I K .
\end{aligned}
$$

因此 $D, I, X, K$ 四点共圆. 由性质 15 的证明知 $D, I, T, K$ 四点共圆. 所以 $K$, $X, T, I, D$ 五点共圆.

性质 17. $\omega_{1}$ 与直线 $A B$ 交于 $B, J$, 与直线 $A C$ 交于 $C, L$, 与直线 $A D$ 交于 $D, K, \triangle A L J$ 的内心为 $T$, 则 $K T$ 平分 $\angle J K L$.

证明 如图 3-17, 设 $\triangle J B C, \triangle L B C$ 的内心为 $G, H, \triangle J B L$ 的 $\angle L$ 所对的旁心为 $M, \triangle J C L$ 的 $\angle J$ 所对的旁心为 $N$. 由内 (旁) 心性质易知 $T, J, M$ 三点共线, $T, L, N$ 三点共线.

以 $A$ 为反演中心, $A$ 对 $\omega_{1}$ 的幂为反演幂作反演变换. 则在该变换下 $\omega_{1}$ 不变, $J \rightarrow B, L \rightarrow C, D \rightarrow K$. 设 $Z \rightarrow P, Y \rightarrow Q$, 则内切圆变换为 $\triangle P Q K$ 的外接圆. 由于内切圆与 $\omega_{1}$ 相切于 $D$, 故 $\triangle P Q K$ 的外接圆与 $\omega_{1}$ 相切于 $K$, 与 $A B$,
$A C$ 相切于 $P, Q$. 由内 (旁) 心性质得 $\angle J N L=\frac{1}{2} \angle J C L=\frac{1}{2} \angle J B L=\angle J M L$,所以 $M, N, L, J$ 四点共圆.

由引理 14 及引理 15 知 $M, P, G, H, Q, N$ 共线, 因此 $\angle T N P=\angle T J L=$ $\angle T J A$. 故 $T, J, P, N$ 四点共圆. 由引理 1 得

$$
\angle P K J=\frac{1}{2} \angle B K J=\frac{1}{2} \angle B L J=\angle M L J=\angle P N J
$$

所以 $K, P, J, N$ 四点共圆. 从而 $K, P, J, T, N$ 五点共圆. 因此

$$
\angle J K T=\angle J N T=\frac{1}{2} \angle J C L=\frac{1}{2} \angle J K L .
$$

故 $K T$ 平分 $\angle J K L$.



图 3-16



图 3-17

性质 18. $\omega_{2}$ 与 $A B$ 交于 $A, J$, 与 $B C$ 交于 $C, K ; \omega_{3}$ 与 $A C$ 交于 $A, T$, 与 $B C$ 交于 $B, L . \triangle C J K, \triangle B T L$ 的内心为 $M, N, \triangle B J K$ 的 $\angle B$ 所对的旁心为 $P, \triangle C T L$ 的 $\angle C$ 所对的旁心为 $Q$, 则四边形 $M N P Q$ 为矩形, 且 $P Q / / B C$.

证明 如图 3-18, $\triangle A C K, \triangle A B L, \triangle A T L, \triangle A J K$ 的内心为 $G, H, R, S$. 由曼海姆定理知 $G, H$ 为 $X Y, X Z$ 的中点, $\triangle A J C, \triangle A B T$ 的内心都是 $Y Z$ 的中点, 设为 $W$. 由引理 14 知 $M, S$ 在 $X Z$ 上, $N, R$ 在 $X Y$ 上. 由引理 15 知, 四边形 $M G W S$, 四边形 $N H W R$ 为矩形.

以内切圆为反演圆作反演变换. 由内心结论易知 $W \rightarrow A, H \rightarrow B, G \rightarrow C$.由引理 16 知 $P \rightarrow I_{2}, Q \rightarrow I_{3}$. 由内心结论易知 $A, I, B, I_{3}$ 共圆. 从而 $W, H, Q$共线.

同理 $W, G, P$ 共线. 所以四边形 $G M H P$, 四边形 $G N H Q$ 为矩形. 由内心性质易知 $I_{2}, I_{3}, B, C$ 共圆, 所以 $P, Q, H, G$ 共圆. 从而 $P, Q, H, M, N, G$ 六点共圆. 因此 $\angle M N P=\angle M H P=90^{\circ}$.
同理 $\angle N M Q=\angle N H Q=90^{\circ}, \angle P Q M=\angle P H M=90^{\circ}$. 所以四边形 $P Q M N$ 为矩形.

又 $P, Q, I_{3}, I_{2}$ 及 $B, C, I_{3}, I_{2}$ 四点共圆, 因此 $\angle I P Q=\angle I I_{3} I_{2}=\angle I_{2} B C=$ $\angle P B C$, 所以 $P Q / / B C$.



图 3-18

性质 19. $B F, C E$ 交于 $P, C D, A F$ 交于 $Q, A E, B D$ 交于 $R$, 则 $A P, B Q$, $C R$ 三线共点, 该点为 Gergonne 点的等角共轭点, 是外接圆与内切圆的内位似中心.

证明 分两部分进行, 第一部分如图 3-19-1,证明 $A P$ 与 $A X$ 互为等角线.

如图 3-19-1, 设 $B F$ 交 $X Z$ 于 $M, C E$ 交 $X Y$于 $N$, 延长 $A P$ 交 $B C$ 于 $J$.

由引理 3 及引理 17 得

$$
\begin{aligned}
& \frac{\sin \angle A B F}{\sin \angle C B F}=\frac{S_{\triangle Z B M}}{S_{\triangle X B M}}=\frac{Z M}{X M}=\frac{Z F^{2}}{X F^{2}}, \\
& \frac{\sin \angle B C E}{\sin \angle A C E}=\frac{X E^{2}}{Y E^{2}} .
\end{aligned}
$$



图 3-19-1

$$
\frac{X E}{Y E}=\frac{X Y}{2 A Y}, \quad \frac{Z F}{X F}=\frac{2 A Z}{X Z} .
$$

对 $\triangle A B C$ 及点 $P$ 由角元塞瓦定理得

$$
\begin{aligned}
\frac{\sin \angle C A P}{\sin \angle B A P} & =\frac{\sin \angle A C E}{\sin \angle B C E} \cdot \frac{\sin \angle C B F}{\sin \angle A B F}=\left(\frac{2 Y A}{X Y}\right)^{2} \cdot\left(\frac{X Z}{2 A Z}\right)^{2} \\
& =\frac{X Z^{2}}{X Y^{2}}=\frac{\cos ^{2} \frac{B}{2}}{\cos ^{2} \frac{C}{2}}=\frac{p(p-b)}{c a} \cdot \frac{a b}{p(p-c)}=\frac{A C}{A B} \cdot \frac{B X}{C X} .
\end{aligned}
$$

从而

$$
\begin{aligned}
\frac{B J}{C J} \cdot \frac{B X}{C X} & =\frac{S_{\triangle A B P}}{S_{\triangle A C P}} \cdot \frac{B X}{C X}=\frac{A B \cdot \sin \angle B A P}{A C \cdot \sin \angle C A P} \cdot \frac{B X}{C X} \\
& =\frac{A B}{A C} \cdot \frac{A B}{A C} \cdot \frac{C X}{B X} \cdot \frac{B X}{C X}=\frac{A B^{2}}{A C^{2}} .
\end{aligned}
$$

由引理 18 知 $\angle B A P=\angle B A J=\angle C A X$, 即 $A X, A P$ 互为等角线. 所以 $A P$, $B Q, C R$ 三线共点, 该点为 Gergonne 点的等角共轭点.

第二部分证明 Gergonne 点的等角共轭点为外接圆与内切圆的内位似中心 ${ }^{[7]}$

如图 3-19-2, 设 $A X$ 的等角线交 $\triangle A B C$ 的外接圆于 $N$, 易知 $\triangle A C X \sim \triangle A N B$, 于是 $A N \cdot A X=$ $A B \cdot A C$. 设 $A N$ 交 $O I$ 于 $T$. 以 $A$ 为反演中心, $A B \cdot A C$ 为反演幂作反演变换, 再以 $\angle A$ 的角平分线为对称轴作轴对称变换.

在两个变换的合同变换下, $B \rightarrow C, X \rightarrow N$, 直线 $B C$ 变换为 $\triangle A B C$ 的外接圆, 直线 $A B$ 变换为直线 $A C$. 由于内切圆与 $B C$ 相切于 $X$, 所以内切圆在该变换下所成的圆 (设为 $\odot I^{\prime}$, 圆心为 $I^{\prime}$ ) 与 $\triangle A B C$



图 3-19-2 的外接圆相切于 $N$, 且与直线 $A B, A C$ 均相切. 故 $A$ 为内切圆与 $\odot I^{\prime}$ 的外位似中心. 设 $N$ 在内切圆上的位似对应点为 $M$, 延长 $A N$ 交 $\odot I^{\prime}$ 于 $J$. 由位似得 $\angle I M J=\angle I^{\prime} N J$. 所以 $O I^{\prime} / / M I$. 因此 $\frac{I T}{T O}=\frac{I M}{O N}=\frac{r}{R}$, 即 $T$ 为外接圆与内切圆的内位似中心.

注 1. 由上面的证明还可以得到 $A N$ 过外接圆与 $\triangle A B C$ 的 $\angle A$ 所对的旁接圆的内位似中心.

2. 第二部分同样的方法还可以证明 “三角形的 Nagel 点的等角共轭点是外接圆与内切圆的外位似中心”. 两个结论的证明留给有兴趣的读者.

## 四. 结语

至此, 我们得到了三角形的伪外接圆的十九个性质. 在研究的过程中, 我们自感对三角形的伪外接圆的圆心的研究不多, 仅得到一些关于半径的公式. 但我们相信, 三个圆心肯定也有许多美妙的性质, 在此希望有兴趣的读者能进一步研究这个方向, 弥补我们的不足.

由于水平有限, 不足及遗漏在所难免, 我们相信三角形的伪外接圆还有许多
其他更加美妙的性质有待发现, 望此文能起抛砖引玉之效, 引起读者对这个课题的关注，也期待大家挖掘出该课题更优美的性质.

致谢 作者由衰感谢湖南理工学院的萧振纲教授在本文写作过程中的悉心指导. 萧振纲教授中肯的建议以及严谨的治学态度使我们受益良多, 也使文章增色不少.

## 参考文献

[1] 波拉索洛夫. 俄罗斯平面几何问题集 [M]. 周春荔 译. 哈尔滨: 哈尔滨工业大学出版社, 2009: 387, 187, 390, 392.

[2] 杨世明. 三角形趣谈 [M]. 哈尔滨: 哈尔滨工业大学出版社, 2012: 84, 46, 88, $59,100,57$.

[3] 沈文选. 走向国际数学奥林匹克的平面几何试题诠释 (下) [M]. 哈尔滨: 哈尔滨工业大学出版社, 2007: 116.

[4] 田开斌, 潘成华, 褚小光. 关于沢山定理的若干命题 [C]. 中国初等数学研究 (2015) 卷. 哈尔滨: 哈尔滨工业大学出版社, 2015: 86-93.

[5] 约翰逊. 近代欧氏几何学 $[\mathrm{M}]$. 单樽 译. 哈尔滨: 哈尔滨工业大学出版社, 2012: 178, 148.

[6] 萧振纲. 等角线 [J]. 数学新星网: http://www.nsmath.cn/jszl, 2015.

[7] 吴悦辰. 三线坐标与三角形特征点 $[\mathrm{M}]$. 哈尔滨: 哈尔滨工业大学出版社, 2015: 40.

