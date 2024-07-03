# 第二十四期问题征解解答与点评 

牟晓生

第一题. 在 $\triangle A B C$ 中, $A B>A C, I$ 是内心, $A I$ 交外接圆 $\odot O$ 于另一点 M. $\angle B I C$ 的外角平分线交 $B C$ 的延长线于 $E$, 点 $F, N$ 分别是 $I E, I A$ 的中点. $M F$ 交 $\odot O$ 于另一点 $K, K N$ 交 $\odot O$ 于另一点 $J$. 证明: 过 $J$ 的直径平行于 $A I$.

(浙江桐乡高级中学学生 顾文影 供题)

证明 (根据杭州二中刘浩宇同学的解答整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_437ce8ac100a0c6525c8g-1.jpg?height=620&width=845&top_left_y=1198&top_left_x=591)

如图, 设 $\triangle A B C$ 的三个垂心分别为 $I_{a}, I_{b}, I_{c}$, 则 $I$ 为 $\triangle I_{a} I_{b} I_{c}$ 的垂心. 设 $I K$交 $I_{a} E$ 于 $L$, 由于 $I M=M I_{a}, I F=F E$, 故 $I L=2 I K$. 注意到 $\triangle A B C$ 的外接圆为 $\triangle I_{a} I_{b} I_{c}$ 的九点圆, 它与 $\triangle I_{a} I_{b} I_{c}$ 的外接圆的外位似中心为 $I$, 位似比为 $1: 2$, 故 $L$ 在 $\triangle I_{a} I_{b} I_{c}$ 的外接圆上. 设这个圆的圆心为 $V$, 且它与 $B C$ 交于 $P, Q$ 两点.

由于 $I O=O V, I M=M I_{a}$, 得到 $I_{a} V / / O M$, 所以 $I_{a} V \perp B C$. 故 $I_{a}$ 为圆 $V$ 上 $P Q$ 弧的中点. 所以 $\angle I_{a} I_{b} P=\angle I_{a} Q P=\angle I_{a} P C$. 由此得到

$$
I_{a} P^{2}=I_{a} C \cdot I_{a} I_{b}=I_{a} I \cdot I_{a} A .
$$

类似地由于 $\angle I_{a} L P=\pi-\angle I_{a} Q P=\angle I_{a} P E$, 得到

$$
I_{a} P^{2}=I_{a} L \cdot I_{a} E
$$

结合上面两式得到 $I_{a} I \cdot I_{a} A=I_{a} L \cdot I_{a} E$, 所以 $A, I, L, E$ 共圆. 由位似知 $N, I, K, F$共圆.

考虑以 $M$ 为圆心, 过 $B, I, C, I_{a}$ 的圆. 令 $T$ 为优弧 $B C$ 的中点, 也就是 $O M$延长线与圆 $M$ 的交点. 则 $I T$ 为 $\angle B I C$ 的内角平分线, 于是 $I T \perp I E$. 所以

$$
\angle M I T=\frac{\pi}{2}-\angle N I F=\frac{\pi}{2}-\angle N K F=\frac{\pi}{2}-\angle J B M=\angle O J M .
$$

因此 $\angle J O M=\angle I M T$, 即 $J O / / A I$.

评注 华南师范大学附属中学冯宣瑞, 浙江省镇海中学严君啸, 湖北省武汉二中朱天明, 江苏省苏州中学吴雨桐, 江苏省徐州一中陈博文, 湖南省长郡中学常杰, 天津市实验中学解尧平等同学以及上海四季教育罗振华老师也给出了本题的正确解答.

第二题. 给定正整数 $n \geq 2$. 已知非负实数 $a_{1}, a_{2}, \ldots, a_{n}$ 的和为 1 , 求 $a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}+2 \sqrt{a_{1} a_{2} \cdots a_{n}}$ 的最大值与最小值.

(东北育才学校 张雷 供题)

## 解 (根据武钢三中游阳同学的解答整理):

首先考虑最大值. 当 $n=2$ 时, $f\left(a_{1}, a_{2}\right)=\frac{3}{2}-2\left(\sqrt{a_{1} a_{2}}-\frac{1}{2}\right)^{2} \leq \frac{3}{2}$, 最大值在 $a_{1}=a_{2}=\frac{1}{2}$ 时取到. 当 $n \geq 3$ 时将证明最大值为 1 , 在 $a_{1}=1, a_{2}=\cdots=$ $a_{n}=0$ 时取到. 为此只需证明

$$
\sqrt{a_{1} a_{2} \cdots a_{n}} \leq \sum_{i<j} a_{i} a_{j}
$$

如果 $n=3$, 则上面的式子可由 $\sqrt{a_{1} a_{2} a_{3}\left(a_{1}+a_{2}+a_{3}\right)} \leq a_{1} a_{2}+a_{1} a_{3}+a_{2} a_{3}$ 导出. 如果 $n \geq 4$, 则右边至少是 $a_{1} a_{2}+a_{3} a_{4} \geq 2 \sqrt{a_{1} a_{2} a_{3} a_{4}} \geq \sqrt{a_{1} a_{2} \ldots a_{n}}$.

下面求最小值. 当 $n=2$ 时易知 $f \geq 1$, 在 $a_{1}=1, a_{2}=0$ 时取到. 当 $n \geq 3$时固定 $a_{3}, \ldots, a_{n}$, 则

$$
a_{1}^{2}+a_{2}^{2}+2 \sqrt{a_{1} a_{2} a_{3} \ldots a_{n}}=\left(a_{1}+a_{2}\right)^{2}-2 a_{1} a_{2}+2 \sqrt{a_{1} a_{2} a_{3} \ldots a_{n}}
$$

为关于 $\sqrt{a_{1} a_{2}}$ 的开口向下的二次函数. 所以取到最小值要么是 $a_{1}=a_{2}$, 要么 $a_{1} a_{2}=0$. 因此, 当整个函数取到最小值时要么 $a_{1}=\cdots=a_{n}$, 要么存在某个 $a_{i}=0$. 前一种情况下答案是 $\frac{1}{n}+2 \sqrt{\frac{1}{n^{n}}}$, 后一种情况下答案是 $\frac{1}{n-1}$. 两者比较, $n \leq 4$ 时后一种情况更小, 而 $n \geq 5$ 时前一种情况更小.

评注 江苏省天一中学李一笑同学以及重庆南开中学一位未留名的同学 (网名“土拨鼠”) 也给出了本题的正确解答.
第三题. 已知 $\triangle A B C$ 内接于圆 $O, D$ 为内切圆 $\odot I$ 与 $B C$ 的切点, $T$ 为 $A$-伪旁切圆切点. 直线 $T D$ 与圆 $O$ 交于另一点 $E$, 直线 $A E$ 与 $B C$ 的延长线交于 $L . X$ 在 $B C$ 边上, 满足 $X C=L C . Y$ 为 $B L$ 的中垂线与 $X I$ 的交点. 证明: $\frac{X I}{Y I}=\frac{2(p-c)}{p-b}$, 其中 $p$ 是 $\triangle A B C$ 的半周长.

注: $T$ 为 $A$-伪旁切圆切点: $T$ 在圆 $O$ 上, 且过 $T$ 的一个圆与 $A B, A C$ 的延长线及圆 $O$ 相切.

(上海复旦附中青浦分校学生 林扬渊 供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_437ce8ac100a0c6525c8g-3.jpg?height=503&width=825&top_left_y=765&top_left_x=610)

## 证明 (根据根据华南师范大学附属中学冯宣瑞同学的解答整理):

连接 $I D$, 设 $H$ 为 $B L$ 中点, 则 $I D \perp B L$. 熟知 $B D=p-b, C D=p-c$.为证命题, 只要证 $\frac{X D}{D H}=\frac{2 C D}{B D}$, 也就是要证 $\frac{C L-C D}{\frac{1}{2} B L-B D}=\frac{2 C D}{B D}$. 整理后即要证 $B L \cdot C D=B D \cdot D L$. 而 $B D=B L-D L, C D=D L-C L$, 所以又等价于 $D L^{2}=B L \cdot C L$.

为证此式, 注意到熟知的结论 $\angle B A T=\angle C A D$. 于是 $\angle D A E=\angle C A D+\angle C A E=\angle B A T+\angle C A E=\angle B C T+\angle C T D=\angle L D E$.于是 $L D^{2}=L A \cdot L E=L B \cdot L C$. 命题得证!

评注 浙江省镇海中学严君啸, 江苏省天一中学李一笑以及武汉学而思巩鸿文等同学也给出了本题的正确解答.

第四题. 证明: 不存在正整数 $a, b, c$, 使得 $\frac{a}{b+c}+\frac{b}{c+a}+\frac{c}{a+b}$ 为奇数.

(北京人大附中学生 杨舍 供题)

证明 (根据供题者的解答整理):

设 $\frac{a}{b+c}+\frac{b}{c+a}+\frac{c}{a+b}=n$ 为奇数, 则

$$
\sum a(a+b)(a+c)=n(a+b)(b+c)(c+a) .
$$

我们可以将这个齐次的三元三次不定方程转化为一个标准的椭圆曲线. 具体来说, 令

$$
x=\frac{-4(a+b+2 c)(n+3)}{2 a+2 b-c+(a+b) n}, \quad y=\frac{4(n+3)(2 n+5)(a-b)}{2 a+2 b-c+(a+b) n} .
$$

则有理数 $x, y$ 满足

$$
y^{2}=x^{3}+\left(4 n^{2}+12 n-3\right) x^{2}+32(n+3) x .
$$

反过来令 $S=a+b+c$, 则

$$
\frac{a}{S}=\frac{8(n+3)-x+y}{2(4-x)(n+3)}, \quad \frac{b}{S}=\frac{8(n+3)-x-y}{2(4-x)(n+3)}, \quad \frac{c}{S}=\frac{-4(n+3)-(n+2) x}{(4-x)(n+3)}
$$

由于 $a b>0$, 可知 $(8(n+3)-x)^{2}>y^{2}$. 利用 (1) 整理得到

$$
(4-x)\left(x^{2}+4 n(n+3) x+16(n+3)^{2}\right)>0,
$$

于是 $x<4$. 再由 $c>0$ 得到 $x<0$.

下面我们证明 (1) 没有 $n$ 为奇数, $x<0$ 的有理数解. 设 $n+3=2 m$, 则

$$
y^{2}=x^{3}+\left(16 m^{2}-24 m-3\right) x^{2}+64 m x \text {. }
$$

令 $x=d \frac{r^{2}}{s^{2}}$, 这里 $d, r, s$ 为整数, $d<0$ 无平方因子, 而 $r, s>0$ 互素. 代入上面得到

$$
Z:=d r^{4}+\left(16 m^{2}-24 m-3\right) r^{2} s^{2}+64 \frac{m}{d} s^{4}
$$

为有理数的平方. 若 $d$ 不整除 $64 m$, 则存在 $d$ 的奇素因子 $q$ 不整除 $64 m$. 这样必须 $q \mid s$, 否则 $v_{q}(Z)=-1$, 与 $Z$ 是平方数矛盾. 而 $(r, s)=1$, 于是 $q$ 不整除 $r$, 导致 $v_{q}(Z)=1$, 依然矛盾.

故 $d \mid 64 m$, 也就是 $d \mid 2 m$. 由于 $Z$ 是平方数, 乘以 $4 d$ 然后配方可得

$$
\left[2 d r^{2}+\left(16 m^{2}-24 m-3\right) s^{2}\right]^{2}-(4 m-1)^{3}(4 m-9) s^{4}=4 d t^{2} .
$$

对某个正整数 $t$ 成立. 下面分三种情况讨论:

(i) $d<0$ 为奇数. 此时知雅可比符号

$\left(\frac{d}{4 m-1}\right)=-\left(\frac{-d}{4 m-1}\right)=-(-1)^{\frac{-d-1}{2}} \cdot\left(\frac{4 m-1}{-d}\right)=-(-1)^{\frac{-d-1}{2}} \cdot\left(\frac{-1}{-d}\right)=-1$.

这里第二步用到二次互反率, 第三步则是因为 $d \mid 2 m$, 第一第四步都用了欧拉判别法. 因此存在 $4 m-1$ 的奇素因子 $p$, 使得 $\left(\frac{d}{p}\right)=-1$. 但由 (2),

$$
\left[2 d r^{2}+\left(16 m^{2}-24 m-3\right) s^{2}\right]^{2} \equiv 4 d t^{2} \quad(\bmod p)
$$

所以必须有 $p \mid 2 d r^{2}+\left(16 m^{2}-24 m-3\right) s^{2}$. 由 $p \mid 4 m-1$ 可知 $p \mid 2 d r^{2}-8 s^{2}$. 再次利用 $\left(\frac{d}{p}\right)=-1$ 得到 $p|r, p| s$, 矛盾!
(ii) $d<0$ 为偶数, 且 $m$ 为偶数. 我们有

$$
\left(\frac{d}{4 m-1}\right)=\left(\frac{-2}{4 m-1}\right) \cdot\left(\frac{-d / 2}{4 m-1}\right)=-1 \cdot(-1)^{-d / 2-1} \cdot\left(\frac{4 m-1}{-d / 2}\right)=-1 \text {. }
$$

类似上一种情况可以导出矛盾!

(iii) $d<0$ 为偶数, 且 $m$ 为奇数. 这时设 $d=-2 u$, 而由 $d \mid 2 m$ 可设 $m=k u$.则 $k, u$ 为奇数, 且

$$
Z=-2 u r^{4}+\left(16 m^{2}-24 m-3\right) r^{2} s^{2}-32 k s^{4}
$$

为平方数. 若 $s$ 为偶数, 则 $r$ 为奇数, 上式除四余二, 不可能. 故 $s$ 为奇数. 进一步地, 如果 $r$ 是奇数, 则上式除四余三, 也不可能. 因此 $r$ 是偶数. 设 $r=2 v$, 则

$$
\frac{Z}{4}=-8 u v^{4}+\left(16 m^{2}-24 m-3\right) v^{2} s^{2}-8 k s^{4}
$$

为平方数. 若 $v$ 是奇数, 则上式除八余五, 不可能. 因此 $v=2 w$, 故

$$
\frac{Z}{16}=-32 u w^{4}+\left(16 m^{2}-24 m-3\right) w^{2} s^{2}-2 k s^{4}
$$

为平方数. 若 $w$ 是奇数, 上式除四余三, 不可能. 但若 $w$ 是偶数, 上式除四余二,亦不可能. 所以综合所有情况, 总能得出矛盾!

故 (1) 没有 $n$ 为奇数, $x<0$ 的有理数解. 命题得证!

评注 (1). 本题难度比较大, 但由于涉及椭圆曲线的各种代数变形, 具有一定的启发意义. 籿圆曲线是现代数论研究中的重要对象, 有兴趣的同学可以进行拓展阅读.

(2). 本题的结论出现在 Allan MacLeod 与 Andrew Bremmer 在 2014 年的论文 “An Unusual Cubic Representation Problem” 中. 这篇论文进一步考虑了 $n$ 为偶数的情况, 并得到了部分结果. 值得一提的是, 去年网络上曾经流行一道关于苹果, 香蕉与梨的 “智力题”, 便是 $n=4$ 的情况. 虽然 $n=4$ 时有正整数解 $(a, b, c)$, 但最小的解都非常之大, 几乎不可能猜出来.

