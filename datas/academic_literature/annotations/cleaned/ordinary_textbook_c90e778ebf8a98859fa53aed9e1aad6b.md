# 伪内切圆的若干性质 

## 陈嘉昊

(清华大学, 100084)

题 1 设 $\triangle A B C$ 内心为 $I, A B>B C>A C$, 它的三个伪内切圆的切点为 $D, D_{1}, D_{2} ; E, E_{1}, E_{2} ; F, F_{1}, F_{2}$, 记

$$
E_{2} F_{1} \cap E F=X, F_{2} D_{1} \cap F D=Y, D_{2} E_{1} \cap D E=Z
$$

证明: $X, Y, Z$ 共线且此直线与 $\triangle A B C$ 的内切圆相切.

注 据我了解潘成华老师已经研究过 $X, Y, Z$ 共线这个性质, 但我目前找到的资料没有提出相切的.



证明 我们依次证明以下性质:

性质 $1 B D_{1}: D_{1} E_{2}: E_{2} A=(p-b):(a+b-p):(p-a)$;

$$
E_{2} F_{1} / / B C, D_{2} E_{1} / / A B, F_{2} D_{1} / / A C .
$$

证明 由

$$
\frac{B E_{2}}{A B}=\frac{I E_{2}}{c \sin \frac{B}{2}}=\frac{2 r}{c \sin B}=\frac{2 S}{p c \sin B}=\frac{a}{p}
$$

Email: jh-chen17@mails.tsinghua.edu.cn 修订日期: 2021-01-11.
可以推出 $B D_{1}: D_{1} E_{2}: E_{2} A=p-b: a+b-p: p-a$, 另外两边也有类似的式子, 且由此可得 $E_{2} F_{1} / / B C, D_{2} E_{1} / / A B, F_{2} D_{1} / / A C$.

性质 $2 A X \perp O I, B Y \perp O I, C Z \perp O I$.

证明 注意到经过以 $A$ 为中心, $\sqrt{A B \cdot A C}$ 为反演半径的反演变换后, $D$ 变成 $\triangle A B C$ 角 $A$ 内的旁切圆切点, 故易知下面这些比例式和其对称的式子:

$$
\frac{B D}{C D}=\frac{c(p-b)}{b(p-c)}, \frac{A D}{B D}=\frac{b}{p-b} \text { (也可以用其它方法算得)， }
$$

于是

$$
\begin{aligned}
\frac{E_{2} X}{F_{1} X}=\frac{S_{\triangle E_{2} E F}}{S_{\triangle F_{1} E F}} & =\frac{\frac{A E_{2}}{A B} S_{\triangle E B F}-\frac{B E_{2}}{A B} S_{\triangle E A F}}{\frac{F_{1} C}{A C} S_{\triangle E A F}-\frac{F_{1} A}{A C} S_{\triangle E C F}} \\
& =\frac{\frac{A E_{2}}{A B} \cdot \frac{B F}{F A} \cdot \frac{B E}{A E}-\frac{B E_{2}}{A B}}{\frac{F_{1} C}{A C}-\frac{A F_{1}}{A C} \cdot \frac{C F}{A F} \cdot \frac{C E}{A E}} \\
& =\frac{\frac{p-a}{p} \cdot \frac{a}{p-a} \cdot \frac{a(p-b)}{b(p-a)}-\frac{a}{p}}{\frac{a}{p}-\frac{p-a}{p} \cdot \frac{a(p-c)}{c(p-a)} \cdot \frac{a}{p-a}}=\frac{c(a-b)}{b(c-a)} .
\end{aligned}
$$

设 $A X$ 和 $B C$ 交于 $M$, 内切圆在 $B C, A C$ 上的切点为 $N, K$. 则:

$$
\begin{aligned}
& M N^{2}+M B \cdot M C-A K^{2} \\
= & \left(\frac{a+c-b}{2}-a \cdot \frac{c a-c b}{a c-a b}\right)^{2}+\left(a \cdot \frac{c a-c b}{a c-a b}\right)\left(a \cdot \frac{b c-b a}{a c-a b}\right)-\left(\frac{b+c-a}{2}\right)^{2} \\
= & \left(\frac{c^{2}+b^{2}-a b-a c}{2(c-b)}\right)^{2}+\left(\frac{c a-c b}{c-b}\right)\left(\frac{b c-b a}{c-b}\right)-\left(\frac{b+c-a}{2}\right)^{2} \\
= & \frac{\left(c^{2}+b^{2}-a b-a c\right)^{2}+4 b c(a-b)(c-a)-(c-b)^{2}(b+c-a)^{2}}{4(c-b)^{2}} \\
= & \frac{[c(c-a)-b(a-b)]^{2}+4 b c(a-b)(c-a)-(c-b)^{2}(b+c-a)^{2}}{4(c-b)^{2}} \\
= & \frac{[c(c-a)+b(a-b)]^{2}-(c-b)^{2}(b+c-a)^{2}}{4(c-b)^{2}}=0,
\end{aligned}
$$

即

$$
M N^{2}+M B \cdot M C=A K^{2},
$$

也就是说 $M, A$ 对内切圆, 外接圆圆幂之差相等, 故 $A X \perp O I$. 同理, $B Y, C Z$ 也和 $O I$ 垂直, 由此可知 $A X, B Y, C Z$ 平行.

最后我们回到原题. 由性质 1 知:

$$
X F_{1} / / E_{1} F_{2}, Y F_{2} / / F_{1} D_{2} .
$$

结合性质 2 中的 $A X / / B Y$ 可知:

$$
\triangle Y B F_{2} \sim \triangle A X F_{1} \Rightarrow \frac{Y F_{2}}{B F_{2}}=\frac{A F_{1}}{X F_{1}}
$$

又由性质 1 可知:

$$
\frac{E_{1} F_{2}}{B F_{2}}=\frac{b+c-p}{p-b}=\frac{p-a}{c+a-p}=\frac{A F_{1}}{D_{2} F_{1}}
$$

即

$$
\frac{E_{1} F_{2}}{B F_{2}}=\frac{A F_{1}}{D_{2} F_{1}} \Rightarrow \frac{Y F_{2}}{E_{1} F_{22}}=\frac{D_{2} F_{1}}{X F_{1}}
$$

由此可知 $\triangle Y F_{2} E_{1}$ 与 $\triangle D_{2} F_{1} X$ 位似, 从而 $Y D_{2}, X E_{1}, F_{1} F_{2}$ 三线共点, 对六边形 $Y X F_{1} D_{2} E_{1} F_{2}$ 用布利安香定理的逆定理及 $\odot I$ 和其余五边相切可知: $X Y$ 与 $\odot I$ 相切, 同理 $X Z$ 也与 $\odot I$ 相切.

题 2 其余记号同上, 设 $A_{2}, B_{2}, C_{2}$ 为三角形 $A B C$ 的三个内切圆切点, 证明: $\triangle A O D, \triangle B O E, \triangle C O F, \triangle I D A_{2}, \triangle I E B_{2}, \triangle I F C_{2}$ 的外接圆共点.

证明 $D_{1} D_{2} \cap B C=P_{a}$, 类似定义 $P_{b}, P_{c}$. 我们断言: $P_{a}, P_{b}, P_{c}$ 共线, 且其与 $O I$ 的交点 $S$ 就是本题中六圆的公共点.

我们先证明以下性质:

性质 $3 P_{a}, P_{b}, P_{c}$ 共线.

证明由性质 1 和梅涅劳斯定理易证.

性质 4 直线 $P_{a} P_{b} P_{c}$ 与 $O I$ 垂直.

证明由 $\angle P_{a} I C=\angle A D_{2} D_{1}-\angle A C I=\frac{\angle A B C}{2}=\angle I B C$, 故 $\triangle P_{a} I C \sim$ $\triangle P_{a} B I$. 因此 $P_{a} O^{2}-P_{a} I^{2}=R^{2}$ ( $R$ 为 $\triangle A B C$ 外接圆半径). 同理

$$
P_{b} O^{2}-P_{b} I^{2}=P_{c} O^{2}-P_{c} I^{2}=R^{2},
$$

由定差幂线定理知直线 $P_{a} P_{b} P_{c}$ 与 $O I$ 垂直.

性质 $5 I_{b} I_{c}, E F, B C, D_{1} D_{2}, A_{3} D$ 五线共点于 $P_{a}$ ( $A_{3}$ 为弧 $B C$ 的中点).


证明 先证明 $I_{b}, I_{c}, P_{a}$ 共线. 对 $\triangle B I C$ 用梅涅劳斯定理知只需证:

$$
\frac{B I_{b}}{I I_{b}} \cdot \frac{I I_{c}}{C I_{c}} \cdot \frac{C P_{a}}{B P_{a}}=1 \Leftrightarrow \frac{B E_{1}}{A_{2} E_{1}} \cdot \frac{A_{2} F_{2}}{C F_{2}} \cdot \frac{C D_{2}}{B D_{1}}=1,
$$

其中, $A_{2}$ 为内切圆切点. 此式由性质 1 易证.

由熟知结论, $D D_{1}, D D_{2}$ 分别过弧 $\overparen{A B}, \overparen{A C}$ 的中点 $C_{3}, B_{3}$, 对 $D A_{3} A C B B_{3}$用帕斯卡定理可知 $I D_{2}, B C, A_{3} D$ 共点, 即 $A_{3} D$ 通过 $P_{a}$. 另由熟知结论易知 $A_{3} E_{1} E, A_{3} F_{2} F$ 分别三点共线, 且

$$
A_{3} E_{1} \cdot A_{3} E=A_{3} F_{2} \cdot A_{3} F=A_{3} C^{2},
$$

故 $E_{1}, E, F_{2}, F$ 四点共圆. 而由性质 1 导比例易证 $P_{a} B \cdot P_{a} C=P_{a} E_{1} \cdot P_{a} F_{2}$, 故 $E_{1}, F_{2}, A_{3}, D$ 四点共圆, 由根心定理可知 $I D_{2}, F_{2} E_{1}, E F$ 三点共线.

综上所述: $I_{b} I_{c}, E F, B C, D_{1} D_{2}, A_{3} D$ 五线共点于 $P_{a}$.



回到原题, 证明 $I A_{2} D S P_{a}$ 共圆相对容易得多, 只需证 $\angle I D P_{a}=90^{\circ}$ 即可.

由 $P_{a} I^{2}=P_{a} C \cdot P_{a} B=P_{a} D \cdot P_{a} A_{3}$ 及 $\angle P_{a} I A_{3}=90^{\circ}$ 即知此结论成立 (用到了性质 4,5). 而 $A O D S$ 四点共圆的证明需要导角和一点陪位中线的基本知识:

$$
\begin{aligned}
\angle A D S & =\angle I D S-\angle A D I \\
& =90^{\circ}+\angle P_{a} I S-\left(2 \angle A D D_{1}-\angle D_{1} D D_{2}\right) \quad\left(A D \text { 为 } \triangle D D_{1} D_{2}\right. \text { 陪位中线) } \\
& \left.=90^{\circ}+\angle O I D_{1}-\angle A D B+90^{\circ}-\frac{\angle A}{2} \quad \text { (由熟知结论 } D D_{1} \text { 平分 } \angle A D B\right) \\
& =\frac{\angle A}{2}+\angle B+\angle O I D_{1} \\
& =90^{\circ}-\angle O A I+\angle O I D_{1} \\
& =\angle A O S
\end{aligned}
$$

即 $A O D S$ 四点共圆.

