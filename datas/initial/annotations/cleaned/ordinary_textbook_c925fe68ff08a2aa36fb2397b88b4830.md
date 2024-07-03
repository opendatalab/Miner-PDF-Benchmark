$$
\text { 数学新星网 } \% \text { 学生专栏 }
$$

www.nsmath.cn/xszl

# 一个图形性质的探索 

李博文 谢金龙

(湖南师范大学附属中学, 410008)

指导教师: 苏林

## 一. 从一道新星征解问题谈起

数学新星网问题征解第 10 期有如下一道平面几何题:

问题已知 $\triangle A B C$ 的内心为 $I, B-$ 旁心, $C-$ 旁心分别为 $I_{B}, I_{C}$, 内切圆在边 $B C, C A, A B$ 上的切点为 $D, E, F$, 旁切圆在线段 $B C, C A, A B$ 上的切点, 分别为 $D^{\prime}, E^{\prime}, F^{\prime}, I_{B} E$ 交 $I_{C} F$ 于 $Q . M$ 为 $Q I$ 的中点. $\angle B A C$ 的角平分线交 $B C$于 $T$. 过 $T$ 作 $T N \perp B C$ 交 $I D^{\prime}$ 于 $N$. 证明: $\angle B A N=\angle C A M$.

该问题中 “ $I_{B} E$ 与 $I_{C} F$ 的交点 $Q$ ” 是一个新出现的几何构型, 这引起了笔者研究的兴趣. 下面我们逐步探索这个几何构型的性质.

为便于行文, 先约定以下符号的几何意义:

$\triangle A B C$ 中, $a, b, c$ 表示三边长, $I, I_{A}, I_{B}, I_{C}$ 表示内心和三个旁心, $D, E, F$ 表示内切圆与三边的切点. $D^{\prime}, E^{\prime}, F^{\prime}$ 表示三个旁切圆与三边内部的切点, $O, O^{\prime}$ 表示 $\triangle A B C, \triangle I_{A} I_{B} I_{C}$ 的外心.

以上约定的符号及字母, 我们将在文中直接使用, 不再反复说明. 其余字母标记以文中说明为准.

## 二. 性质探索

性质 1. $I_{A} D, I_{B} E, I_{C} F$ 三线共点, 且这个点为 $\triangle D E F$ 和 $\triangle I_{A} I_{B} I_{C}$ 的位似中心。

这个性质由 $\triangle D E F, \triangle I_{A} I_{B} I_{C}$ 对应边平行即得.

我们说这个点为 $Q$, 该性质在关于点 $Q$ 性质的研究中起到基础性的作用,在文中接下来的论证中将多次用到.

收稿日期: 2017-05-23; 修订日期: 2017-06-29.
性质 1 的一个直接推论是 $Q, I, O$ 三点共线.

性质 2. $\odot O$ 中 $\widehat{B A C}$ 的中点为 $M, M I$ 交 $B C$ 于 $L$, 则 $A, Q, L$ 三点共线.

证明 熟知 $M$ 为 $I_{B} I_{C}$ 的中点.

又由 $\triangle B I C \sim \triangle I_{C} I I_{B}$ 知 $I L$ 为 $\triangle B I C$的陪位中线. 因此

$$
\frac{B L}{C L}=\frac{B I^{2}}{C I^{2}}
$$

设 $A L$ 交 $E F$ 于 $P$, 则有



$$
\begin{aligned}
\frac{F P}{E P} & =\frac{\sin \angle F A P}{\sin \angle E A P}=\frac{\sin \angle B A L}{\sin \angle C A L}=\frac{B L \sin \angle A B C}{C L \sin \angle A C B} \\
& =\frac{B I^{2}}{C I^{2}} \cdot \frac{A C}{A B}=\frac{B I}{C I} \cdot \frac{\sin \angle A I C}{\sin \angle I A C} \cdot \frac{\sin \angle I A B}{\sin \angle A I B}=\frac{B I}{C I} \cdot \frac{\cos \angle A B I}{\cos \angle A C I} \\
& =\frac{B F}{C E}=\frac{A F^{\prime}}{A E^{\prime}}=\frac{A F^{\prime}}{\cos \angle F A I_{C}} \cdot \frac{\cos \angle E^{\prime} A I_{B}}{A E^{\prime}}=\frac{A I_{C}}{A I_{B}} .
\end{aligned}
$$

设 $A Q$ 交 $E F$ 于 $P^{\prime}$, 则由性质 1 有 $\frac{F P^{\prime}}{E P^{\prime}}=\frac{A I_{C}}{A I_{B}}$.

因此 $P \equiv P^{\prime}, A, Q, L$ 共线.

性质 3. 设边 $B C, A C, A B$ 的中点分别为 $M_{A}, M_{B}, M_{C}$, 则 $I_{A} M_{A}, I_{B} M_{B}, I_{C} M_{C}$三线共点, 且这个点为点 $Q$ 关于 $\triangle A B C$ 的等角共轭点.

证明 易知 $\triangle A B C$ 为 $\triangle I_{A} I_{B} I_{C}$ 的垂足三角形, 所以 $\triangle I_{A} B C, \triangle I_{A} I_{B} I_{C}$ 关于 $I_{A}$ 反向位似. 因此, $I_{A} M_{A}$ 为 $\triangle I_{A} I_{B} I_{C}$ 的 $I_{A}$-陪位中线.

同理, $I_{B} M_{B}, I_{C} M_{C}$ 也是 $\triangle I_{A} I_{B} I_{C}$ 的陪位中线.

所以 $I_{A} M_{A}, I_{B} M_{B}, I_{C} M_{C}$ 三线共点, 且这个点为 $\triangle I_{A} I_{B} I_{C}$ 的陪位重心.

$A^{\prime}$.

过 $I_{C}$ 作平行于 $A B$ 的直线, 过 $I_{B}$ 作平行于 $A C$ 的直线, 两直线交于点 $A^{\prime}$.类似地定义点 $B^{\prime}, C^{\prime}$.

由性质 1 知 $\triangle I_{A} I_{B} I_{C}$ 的外接圆为 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 的内切圆, 故 $A^{\prime} I_{C}=A^{\prime} I_{B}$, $B^{\prime} I_{C}=B^{\prime} I_{A}, C^{\prime} I_{B}=C^{\prime} I_{A}$.

熟知 $A^{\prime} I_{A}, B^{\prime} I_{B}, C^{\prime} I_{C}$ 共点, 记这个点为 $I^{\prime}$.

则完全四边形 $A^{\prime} I_{C} B^{\prime} I^{\prime} C^{\prime} I_{B}$ 的对角线 $A^{\prime} I^{\prime}$ 被另两条对角线调和分割, 设 $A I_{A}$ 交 $I_{B} I_{C}$ 于 $K$, 则 $A^{\prime}, I^{\prime}, K, I_{A}$ 成调和点列.

另一方面, $I^{\prime}$ 即为 $\triangle I_{A} I_{B} I_{C}$ 的陪位重心. 由于 $A^{\prime}, I^{\prime}, K, I_{A}$ 成调和点列,而 $\angle I_{A} A K=90^{\circ}$, 所以 $\angle A^{\prime} A K=\angle I^{\prime} A K$, 而 $\angle A^{\prime} A K=\angle I^{\prime} A C+\angle I_{B} A C=$ $\angle I^{\prime} A C+\angle I_{B} I_{A} I_{C} . \angle A^{\prime} A K=\angle I_{C} A^{\prime} A+\angle A^{\prime} I_{C} A=\angle I_{C} A^{\prime} A+\angle I_{C} I_{A} I_{B}$. 因此 $\angle I_{C} A^{\prime} A=\angle I^{\prime} A C$.

由性质 $1, Q, A, A^{\prime}$ 共线. 而 $A F / / I_{C} A^{\prime}$, 所以 $\angle F A Q=\angle I_{C} A^{\prime} A=\angle I^{\prime} A C$.

对点 $B$, 点 $C$, 同理有类似的结论.

所以 $Q, I^{\prime}$ 是 $\triangle A B C$ 的一组等角共轭点.

性质 4. 字母标记同性质 3. 设 $G$ 为 $\triangle A B C$ 重心, $J$ 为 $\triangle A B C$ 的 Gergonne 点. 则 $Q, G, J, I^{\prime}$ 四点共线.

证明 由性质 1 知 $Q$ 也是 $\triangle A B C$ 和 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 的位似中心, 而 $J, I^{\prime}$ 分别是 $\triangle A B C, \triangle A^{\prime} B^{\prime} C^{\prime}$ 的 Gergonne 点. 所以 $Q, J, I^{\prime}$ 共线.

注意到重心 $G$ 是 $\triangle A B C$ 和 $\triangle M_{A} M_{B} M_{C}$ 的位似中心, 由性质 3 的证明知 $A J / / M_{A} I^{\prime}, B J / / M_{B} I^{\prime}, C J / \mid$ $M_{C} I^{\prime}$.

所以 $J, I^{\prime}$ 为 $\triangle A B C, \triangle M_{A} M_{B} M_{C}$ 的一组对应点,因此 $J I^{\prime}$ 过位似中心 $G$. 从而 $Q, J, G, I^{\prime}$ 四点共线.



## 三. 另一个想法

鉴于题目中出现了旁切圆的切点, 于是笔者思考: 是否形如 $A D^{\prime}$ 的三条线段也有一些相应的结论?

我们首先给出 Negal 点的定义: $A D^{\prime}, B E^{\prime}, C F^{\prime}$ 三线所共的点即为 $\triangle A B C$的 Negal 点.

在这里, 三线共点是熟知的, 我们不再给出证明. 下面我们约定点 $N$ 即为 Negal 点.
我们给出如下两条性质:

性质 5. $N, G, I$ 共线 (点 $G$ 的定义同上).

证明 我们只需证明 $I$ 为 $\triangle M_{A} M_{B} M_{C}$ 的 Negal 点, 由位似即得命题成立.

连接 $A D$ 交 $M_{B} M_{C}$ 于 $D^{\prime \prime}$. 我们只需证明 $M_{A}, I, D^{\prime \prime}$ 共线. 由对称性可知另外两组共线. 注意到 $M_{A} D^{\prime \prime} / / A D^{\prime}$, 由位似即得结论成立.

设 $A I$ 交 $B C$ 于点 $T$. 由 Menelaus 定理之逆,只需 $\frac{A D^{\prime \prime}}{D^{\prime \prime} D} \cdot \frac{D M_{A}}{M_{A} T} \cdot \frac{T I}{I A}=1$.



注意到, $D^{\prime \prime} A=D^{\prime \prime} D$. 所以只需证明 $\frac{M_{A} D}{M_{A} T}=\frac{A I}{I T}$.

由 $I$ 为内心知 $\frac{A I}{I T}=\frac{A C}{C T}, \frac{B T}{C T}=\frac{A B}{A C}$, 又 $B T+C T=B C$. 所以

$$
B T=\frac{A B \cdot B C}{A B+A C}, C T=\frac{A C \cdot B C}{A B+A C}
$$

从而 $\frac{A C}{C T}=\frac{A B+A C}{B C}$. 而 $C D=\frac{B C+A C-A B}{2}, C M_{A}=\frac{B C}{2}$. 所以

$$
M_{A} D=\frac{A B-A C}{2}, \quad M_{A} T=\frac{B C}{2}-\frac{A C \cdot B C}{A B+A C}=\frac{(A B-A C) B C}{2(A B+A C)} .
$$

从而 $\frac{M_{A} D}{M_{A} T}=\frac{A B+A C}{B C}=\frac{A I}{I T}$, 即 $M_{A}, I, D^{\prime \prime}$ 共线, 故原命题得证.

性质 6. 点 $N$ 关于 $\triangle A B C$ 的等角共斩点是外接圆与内切圆的外位似中心.

证明 作 $\triangle A B C$ 外接圆 $\odot O, \angle A$ 内的伪内切圆 (与 $A B, A C, \odot O$ 均相切, 且在 $\odot O$ 内部的圆) 与 $\odot O$ 切于 $S . \odot O$ 上 $\widehat{B A C}$ 中点为 $P, \widehat{B C}$ (不含 $A$ ) 中点为 $M, D I$ 交 $A D^{\prime}$ 于 $R$.


熟知 $D R$ 为内切圆 $\odot I$ 的直径, 而 $P M$ 为 $\odot O$ 直径, $P M / / R D$. 所以 $P R$与 $M D$ 的交点 $K$ 即为 $\odot O$ 与 $\odot I$ 的外位似中心.

由三位似中心定理, $A, K, S$ 三点共线.
我们只需证明 $\angle B A D^{\prime}=\angle C A S$, 由对称性可得另外两组等角线, 即得命题成立.

设 $\angle A$ 内伪内切圆与 $A B, A C$ 分别切于 $X, Y$.

由曼海姆定理, $I$ 为 $X Y$ 中点, 延长 $S X, S Y$ 交 $\odot O$ 于 $R_{C}, R_{B}$.

由位似知 $\widehat{A R C}=\widehat{B R_{C}} \cdot \widehat{A R_{B}}=\widehat{C R_{B}}$. 且 $S I$ 过 $R_{B} R_{C}$ 的中点.

另一方面, 由熟知结论, $R_{C} I=R_{C} A, R_{B} I=R_{B} A$. 又 $\widehat{A R_{C}}=\frac{\widehat{A B}}{2}=$ $\frac{\overparen{A B}-\overparen{A C}}{2}+\frac{\overparen{A C}}{2}=\overparen{P R_{B}}$, 所以 $P R_{B}=A R_{C}=R_{C} I$.

同理 $R_{B} I=P R_{C}$. 因此 $P R_{B} I R_{C}$ 为平行四边形, 所以 $P I$ 过 $R_{B} R_{C}$ 中点,即得 $P, I, S$ 共线.

由欧拉公式得 $2 R r=P I \cdot I S$, 即 $P M \cdot I D=P I \cdot S D$, 又 $\angle M P I=\angle D I S$,所以 $\triangle M P I \sim \triangle S I D, \angle I S D=\angle I M P=\angle I S A$. 所以有 $\angle D S C=\angle A S B$.

又因为 $\angle B A S=\angle D C S$, 所以 $\triangle B S A \backsim \triangle D S C$.

从而 $\frac{B A}{A S}=\frac{D C}{C S}$. 又熟知 $C D=B D^{\prime}$, 所以 $\frac{B A}{A S}=\frac{B D^{\prime}}{C S}$.

又 $\angle A B D^{\prime}=\angle A S C$, 故 $\triangle A B D^{\prime} \backsim \triangle A S C$. 故 $\angle B A D^{\prime}=\angle C A S$. 原命题得证.

## 四. 结论

至此, 我们得到了六个美妙的性质. 鉴于水平有限, 不足及遗漏在所难免.我们相信关于这两个点还有许多更加美妙的性质有待发现. 也期待大家挖掘出更多优美的性质。

最后, 笔者给出两个问题. 有兴趣的读者可以参考上面的性质给予解答.

问题 1. 已知 $\odot I$ 为 $\triangle A B C$ 的内切圆, $D, E, F$ 为内切圆在边 $B C, A C, A B$ 边上切点. $O$ 为外心, $O I$ 交 $B C$ 于 $K$, 过 $D$ 作垂直于 $E F$ 的直线交 $E F, A K$ 于 $G, H$. 证明:


$D G=G H$.

问题 2. 已知 $I, I_{D}, I_{C}$ 是 $\triangle A B C$ 的内心, $B$ 一旁心, $C$-旁心, $B I, C I$ 分别交边 $A C, A B$于 $E, F, P, Q$ 为 $A C, A B$ 的中点. $I_{B} P$ 交 $I_{C} Q$于 $J, M$ 为 $\triangle A B C$ 外接圆上 $\widehat{B A C}$ 中点. 证明: $A J, M I, E F$ 三线共点.



