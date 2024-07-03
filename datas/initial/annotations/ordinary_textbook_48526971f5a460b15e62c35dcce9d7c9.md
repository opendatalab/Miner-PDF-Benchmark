数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 对 2021 年 IMO 预选题 G8 的推广与证明 

张峻铭

(南开大学陈省身数学研究所, 300071)

2022 年的 IMO 刚刚结束, 同时保密了一年的 2021 年 IMO 预选题也在官网 $[1]$ 上放出. 本文将给出几何板块第 8 题的推广与证明.

## 1. 问题叙述

我们首先给出原始的问题.

问题 1.1 令 $\omega$ 为 $\triangle A B C$ 的外接圆, $\Omega_{A}$ 为其与线段 $B C$ 相切的旁切圆. 设 $\omega$ 与 $\Omega_{A}$ 交于 $X, Y$ 两点. 设 $P, Q$ 分别为 $A$ 在 $\Omega_{A}$ 在 $X, Y$ 处的切线上的投影. $\odot(A P X)$ 在 $P$ 处的切线与 $\odot(A Q Y)$ 在 $Q$ 处的切线交于 $R$. 证明: $A R \perp B C$.

本文中, 我们将会证明如下的推广.

问题 1.2 设 $\triangle A B C$ 的 $A$-旁切圆与外接圆交于 $X, Y, A$-旁切圆在 $X, Y$ 处的切线交于 $Z$, 设 $P, Q$ 分别为 $X Z, Y Z$ 上的点, 满足 $A, P, Q, Z$ 共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_384b1e7ecf56db8d564dg-1.jpg?height=694&width=414&top_left_y=1846&top_left_x=821)

修订日期: 2022-07-23.
设 $\odot(A P X)$ 在 $P$ 处的切线与 $\odot(A Q Y)$ 在 $Q$ 处的切线交于 $R$. 证明: $\measuredangle A P Z=\measuredangle A S B$, 其中 $\measuredangle$ 表示有向角.

当 $\measuredangle A P Z=90^{\circ}$ 时, 问题 1.2 就退化为问题 1.1.

## 2. 预备知识

我们首先介绍一下有向角的语言.

定义 2.1 对平面上的任意两条直线 $\ell$ 与 $\ell^{\prime}$, 定义 $\angle\left(\ell, \ell^{\prime}\right)$ 为 $\ell$ 逆时针旋转至首次与 $\ell^{\prime}$ 平行或重合时所经过的角度. 对平面上任意三点 $X, Y, Z$, 定义 $\measuredangle X Y Z=\measuredangle(X Y, Y Z)$.

借助有向角的语言, 我们可以忽视序关系, 而将四点共圆的充要条件改写为:

定理 2.1 平面上四点 $A, B, C, D$ 共圆当且仅当 $\measuredangle A C B=\measuredangle A D B$.

接下来我们介绍一个著名的 Simson 定理的推广:

定理 2.2 设 $X$ 在 $\odot(A B C)$ 上, $D, E, F$ 分别在 $B C, C A, A B$ 上, 满足

$$
\measuredangle(X D, B C)=\measuredangle(X E, C A)=\measuredangle(X F, A B),
$$

则 $D, E, F$ 共线. 反之, 若 $\measuredangle(X D, B C)=\measuredangle(X E, C A)$, 且 $D, E, F$ 共线, 则 $\measuredangle(X D, B C)=\measuredangle(X F, A B)$.

证明 由条件知 $X, C, D, E$ 共圆, 于是

$$
\measuredangle X D E=\measuredangle X C E=\measuredangle X C A=\measuredangle X B A=\measuredangle X B F
$$

故 $D, E, F$ 共线等价于 $\measuredangle X D E=\measuredangle X D F$ ，等价于 $\measuredangle X B F=\measuredangle X D F$ ，等价于 $X, B, F, D$ 共圆, 等价于 $\measuredangle(X D, B C)=\measuredangle(X F, A B)$.

注 2.1 当 $D$ 是 $X$ 在 $B C$ 上的投影时, 上述定理就退化为 Simson 定理.

我们还需要 Poncelet 的闭合定理, 不过只需要三角形版本的, 此处不做证明. 对于一般情形的证明, 可以参看 [2].

定理 2.3 (Poncelet 闭合定理, $\boldsymbol{n}=\mathbf{3}$, 旁切版本) 给定 $\triangle A B C$ 及其 $A$-旁切圆 $c$. 设 $D$ 是 $\odot(A B C)$ 上一点, 其对 $c$ 的切线分别交 $\odot(A B C)$ 于不同于 $D$ 的一点 $E, F$, 则 $E F$ 亦为 $c$ 的切线.

沿用上述定理的记号, 我们考虑极限情形, 使 $D$ 沿 $\odot(A B C)$ 趋近于
$\odot(A B C)$ 与 $c$ 的交点, 立刻得到如下推论.

推论 2.1 给定 $\triangle A B C$ 及其 $A$-旁切圆 $c$. 设 $D$ 是 $\odot(A B C)$ 与 $c$ 的一个交点, $c$ 在 $D$ 处的切线与 $\odot(A B C)$ 交于不同于 $D$ 的一点 $D^{\prime}$, 则 $\odot(A B C)$ 在 $D^{\prime}$ 处的切线亦为 $c$ 的切线.

我们也可以考虑另一个极限情形, 即 $A$ 沿 $\odot(A B C)$ 趋近于 $C$, 此时 $B$ 就是定理 2.3 中两圆的一个交点, 换言之

推论 2.2 给定一圆 $c$ 及其一弦 $A B$, 设圆 $c^{\prime}$ 与 $A B$ 切于 $B$ 且与 $c$ 在 $A$ 处的切线相切, 对 $c$ 上任意一点 $D$, 其对 $c^{\prime}$ 的切线分别交 $c$ 于不同于 $D$ 的一点 $E, F$,则 $E F$ 亦为 $c^{\prime}$ 的切线.

我们需要的另一个引理如下:

引理 2.1 给定 $\triangle A B C$ 及其内心 $I$, 设 $I$ 在 $A B$ 上的投影为 $D$, 过 $A, D$ 且与 $A C$ 相切的圆与 $\odot(A B C)$ 交于 $A, E$ 两点, 则 $E I$ 平分 $\angle A E B$, 亦平分 $\angle C E D$.

注 2.2 事实上 $E$ 是 $\triangle A B C$ 的所谓“ $C$ - 伪内切圆”的切点, 熟悉此性质的读者想必可以一眼看出, 但此处我们还是给出证明.

证明 我们采用同一法. 假设弧 $\widehat{A C B}$ 的中点为 $N, N I$ 交 $\odot(A B C)$ 于不同于 $N$ 的一点 $E^{\prime}$, 我们来证明 $E^{\prime} \equiv E$.

注意 $\angle N A B=90^{\circ}-\frac{1}{2} \angle A C B$, 故 $\angle N A I=\angle N A B-\angle B A I=\frac{1}{2} \angle A B C=$ $\angle A B I$, 故 $\angle A I E^{\prime}=\angle I A N+\angle A N I=\angle I B A+\angle A B E^{\prime}=\angle I B E^{\prime}$. 结合 $N$ 是弧 $\widehat{A C B}$ 的中点知 $\angle A E^{\prime} I=\angle I E^{\prime} B$, 故 $\triangle A E^{\prime} I \sim \triangle I E^{\prime} B$. 于是

$$
\frac{E^{\prime} A}{E^{\prime} B}=\frac{E^{\prime} A}{E^{\prime} I} \cdot \frac{E^{\prime} I}{E^{\prime} B}=\left(\frac{A I}{B I}\right)^{2} .
$$

由 Ptolemy 定理, 由于 $E^{\prime}$ 在不含点 $C$ 的弧 $A B$ 上(这是因为 $N A, N B$ 为 $\odot(A I B)$ 的切线, 而 $\angle A I B$ 为钝角, 故 $N I$ 在 $N A, N B$ 之间 $)$,

$$
E^{\prime} A \cdot B C+E^{\prime} B \cdot A C=E^{\prime} C \cdot A B .
$$

故

$$
\begin{aligned}
E^{\prime} C \cdot A D & =E^{\prime} C \cdot A B \cdot \frac{A D}{A B} \\
& =\left(E^{\prime} A \cdot B C+E^{\prime} B \cdot A C\right) \cdot \frac{A D}{A B} \\
& =E^{\prime} A \cdot\left(B C+\left(\frac{B I}{A I}\right)^{2} \cdot A C\right) \cdot \frac{A D}{A B} \\
& =E^{\prime} A \cdot\left(B C+\left(\frac{\sin \angle B A I}{\sin \angle A B I}\right)^{2} \cdot A C\right) \cdot \frac{A D}{A B}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_384b1e7ecf56db8d564dg-4.jpg?height=1336&width=917&top_left_y=203&top_left_x=661)

又由 $\measuredangle E^{\prime} A D=\measuredangle E^{\prime} C B$ 即知 $\triangle E^{\prime} A D \stackrel{ \pm}{\sim} \triangle E^{\prime} C B$. 故 $\measuredangle D A C=\measuredangle B E^{\prime} C=$ $\measuredangle D E^{\prime} A$, 即 $\odot\left(D E^{\prime} A\right)$ 与 $A C$ 相切于 $A$, 故 $E^{\prime} \equiv E$. 由弧中点及相似即知 $E I$ 平分 $\angle A E B$ 与 $\angle C E D$.

基于此我们可以得到如下结果:

引理 2.2 给定 $\triangle A B C$ 及其内心 $I$, 内切圆 $c$, 设 $I$ 在 $A B$ 上的投影为 $D$,过 $A, D$ 且与 $A C$ 相切的圆 $c^{\prime}$ 交 $c$ 的与 $B C$ 平行的切线于 $U, V$ 两点, 则分别过 $U, V$ 的 $c$ 的非 $U V$ 的切线交于 $\odot(A B C)$ 和 $c^{\prime}$ 的除 $A$ 外的另一交点 $E$.

证明 设 $c$ 与 $c^{\prime}$ 的另一交点为 $E^{\prime}$, 我们使用同一法证明 $E \equiv E^{\prime}$.

过 $E^{\prime}$ 作 $c$ 的切线, 分别交 $c^{\prime}$ 于 $U^{\prime}, V^{\prime}$. 由推论 2.2 可知 $U^{\prime} V^{\prime}$ 与 $c$ 相切.设 $E^{\prime} C$ 与 $c^{\prime}$ 的另一交点为 $F$, 则 $\measuredangle D F C=\measuredangle D A E^{\prime}=\measuredangle B A E^{\prime}=\measuredangle B C E^{\prime}$, 故 $D F / / B C$. 由引理 2.1 知 $\measuredangle U^{\prime} E^{\prime} F=\measuredangle D E^{\prime} V^{\prime}$, 故 $U^{\prime} V^{\prime} / / D F$, 即 $U^{\prime} V^{\prime}$ 与 $B C$ 重合或平行.

由于 $D$ 在线段 $A B$ 上, 故 $E^{\prime}$ 在不含 $C$ 的弧 $\overparen{A B}$ 上, 故若直线 $U^{\prime} V^{\prime}$ 与直线

![](https://cdn.mathpix.com/cropped/2024_02_26_384b1e7ecf56db8d564dg-5.jpg?height=893&width=731&top_left_y=196&top_left_x=660)

$B C$ 重合, 则 $U^{\prime}, V^{\prime}$ 分别在线段 $B C$ 与 $B C$ 的延长线上, 换言之, $C$ 在 $U^{\prime}, V^{\prime}$ 之间, 此时 $c^{\prime}=\odot\left(A U^{\prime} V^{\prime}\right)$ 不可能与 $A C$ 相切. 综上, 直线 $U^{\prime} V^{\prime}$ 必与 $U V$ 重合, 故 $\left\{U^{\prime}, V^{\prime}\right\}=\{U, V\}$, 于是 $E \equiv E^{\prime}$.

## 3. 问题证明

本节中我们回到问题 1.2 的证明.

问题 3.1 设 $\triangle A B C$ 的 $A$-旁切圆与外接圆交于 $X, Y, A$-旁切圆在 $X, Y$ 处的切线交于 $Z$, 设 $P, Q$ 分别为 $X Z, Y Z$ 上的点, 满足 $A, P, Q, Z$ 共圆.

设 $\odot(A P X)$ 在 $P$ 处的切线与 $\odot(A Q Y)$ 在 $Q$ 处的切线交于 $R$. 证明: $\measuredangle A P Z=\measuredangle A S B$, 其中 $\measuredangle$ 表示有向角.

证明 设 $A$-旁切圆 $c$ 与 $B C$ 平行的切线为 $\ell, c$ 在 $X$ 处的切线与 $\odot(A B C)$ 的另一交点为 $U, X U, \odot(A B C)$ 在 $U$ 处的切线分别交 $\ell$ 于 $V, W$. 由推论 2.1 知 $U W$ 与 $c$ 相切, 对 $\triangle U V W$ 使用引理 2.2 可知 $A, U, V, W$ 共圆.

设 $\odot(A P X)$ 在 $P$ 处的切线与 $U W$ 交于 $T$, 则

$$
\begin{aligned}
\measuredangle P T U & =\measuredangle(T P, T U) \\
& =\measuredangle(T P, P U)+\measuredangle(P U, T U) \\
& =\measuredangle P A X+\measuredangle X A U \\
& =\measuredangle P A U,
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_384b1e7ecf56db8d564dg-6.jpg?height=931&width=991&top_left_y=211&top_left_x=521)

故 $A, P, U, T$ 共圆. 设 $P T$ 交 $\ell$ 于 $R_{1}$, 则由定理 2.2 知 $\measuredangle\left(A R_{1}, \ell\right)=\measuredangle A P X$. 对称地, 若设 $\odot(A Q Y)$ 在 $Q$ 处切线与 $\ell$ 交于 $R_{2}$, 亦有 $\measuredangle\left(A R_{2}, \ell\right)=\measuredangle A Q Y=\measuredangle A P X$.故 $R_{1}=R_{2} \equiv R$. 于是 $\measuredangle A S B=\measuredangle(A R, B C)=\measuredangle(A R, \ell)=\measuredangle A P X$.

## 4. 注 记

本法与 2021 IMO 命题委员会给出的两种证明方法均不相同, 但一个关键就在于猜出 $R$ 在 $A$-旁切圆的平行于 $B C$ 的切线上. 若能看到这一点, 本题的难度就会大大降低.

## 参考文献

[1] P. S. Committee, Imo 2021 shortlisted problems.

https://www.imo-official.org/problems/IMO2021SL.pdf

[2] J. L. King. Three problems in search of a measure. The American Mathematical Monthly, 101(7): 609 - 628, 1994.

