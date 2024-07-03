数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2022 年越南 TST 试题解答与评析 

刘家瑜<br>(长沙市雅礼中学, 410007)<br>指导教师: 申东

本年度越南 TST 试题的难度与 CMO 试题的难度基本相当. 3,4 两个几何题比较漂亮, 难度比 CMO 稍小, 1, 2, 5 题中等难度, 第 6 题较难.

## I. 试 题

1. 已知函数 $\varphi(x)=x^{2} e^{a x}$ ( $a$ 为给定实数). 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意 $x, y \in \mathbb{R}$, 都有 $f(\varphi(x)+f(y))=y+\varphi(f(x))$.
2. 给定一个凸 2022 面体. 随机选择 3 个面, 并在上面填数 $26,4,2022$ (每个面上填 1 个数). 甲想在每个其它的面上填一个实数, 使得它是每个与之有公共棱的面上的实数的平均数. 证明: 有且仅有一种填数的方法.
3. 平行四边形 $A B C D$ 的对角线交于点 $I . \triangle A B I$ 内有一点 $G$, 使得 $\angle I A G=\angle I B G \neq 45^{\circ}-\frac{\angle A I B}{4}$. 设 $E$ 为 $C$ 在 $A G$ 上的投影, $F$ 为 $D$ 在 $B G$ 上的投影. $\triangle B E F$ 的 $E$-中线和 $\triangle A E F$ 的 $F$-中线交于点 $H$.

(1) 证明: $A F, B E, I H$ 三线共点 (记该点为 $L$ ).

(2) $C E, D F$ 相交于点 $K$, 设 $\odot L A B, \odot E I J, \odot F I J$ 的圆心分别为 $J, M, N$.证明: $\odot G A B, \odot K C D$ 的连心线和 $E M, F N$ 三线共点.

4. 锐角不等边 $\triangle A B C$ 的外心为 $O, B C$ 边的中点为 $I$. 直线 $O I$ 分别交 $A B, A C$ 于点 $E, F . D$ 为 $A$ 关于 $O$ 的对称点, $G$ 为 $A$ 关于 $\triangle A E F$ 外心的对称点, $K$ 为 $O$ 关于 $\triangle O B C$ 外心的对称点.

(1) 证明: $D, G, K$ 三点共线.

(2) 设 $M, N$ 分别是 $K B, K C$ 上的点, 满足 $I M \perp A C, I N \perp A B . I K$ 的[^0]垂直平分线交 $M N$ 于点 $H, I H$ 分别交 $A B, A C$ 于点 $P, Q$. 证明: $\triangle A P Q$ 的外接圆与圆 $O$ 的另一个交点 (不同于 $A$ ) 在直线 $A I$ 上.

5. 对于实数 $x$, 若存在 $b \in\{2,3, \cdots, 2022\}$, 使得 $x$ 在 $b$ 进制下可表示为有限小数, 则称 $x$ 为 “漂亮数”. 证明: 仅存在有限个正整数 $n(n \geq 4)$, 使得对于任意正整数 $m \in\left(\frac{2}{3} n, n\right)$, 两数 $\frac{n}{m-n}, \frac{n-m}{m}$ 当中至少有一个漂亮数.
6. 已知集合 $A \in\{1,2, \cdots, 4044\}$. 甲将其中 2022 个数染成白色, 剩余 2022 个数染成黑色. 对于每个 $i \in A$, 所有小于 $i$ 的白色数与所有大于 $i$ 的黑色数之和称为 $i$ 的 “重要数”. 求所有可能的正整数 $k$, 使得存在自然数 $m$ 和一种染色方式, 满足有 $k$ 个数的重要数为 $m$.

## II. 解答与评注

题 1 已知函数 $\varphi(x)=x^{2} e^{a x}$ ( $a$ 为给定实数). 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意 $x, y \in \mathbb{R}$, 都有 $f(\varphi(x)+f(y))=y+\varphi(f(x))$.

解 先证明 $f$ 为一一映射.

记 $f(\varphi(x)+f(y))=y+\varphi(f(x))$ 为 (1) 式. 在 (1) 式中令 $x=0$, 并注意到 $\varphi(0)=0$, 可得

$$
f(f(y))=y+\varphi(f(0)) .
$$

一方面, 由 (2) 知, 当 $y$ 遍历 $\mathbb{R}$ 时, $f(f(y))$ 也遍历 $\mathbb{R}$, 故 $f$ 为满射.

另一方面, 若 $f\left(y_{1}\right)=f\left(y_{2}\right)$, 则由 (2) 可得

$$
y_{1}+\varphi(f(0))=f\left(f\left(y_{1}\right)\right)=f\left(f\left(y_{2}\right)\right)=y_{2}+\varphi(f(0)) \Rightarrow y_{1}=y_{2},
$$

故 $f$ 为单射.

综上, $f$ 为一一映射.

由 (1), (2) 可得

$$
f(\varphi(x)+f(y))=f(f(y))-\varphi(f(0))+\varphi(f(x)),
$$

注意到 $f$ 为满射, 可用 $y$ 代替上式中的 $f(y)$, 得

$$
f(\varphi(x)+y)=f(y)-\varphi(f(0))+\varphi(f(x))
$$

在 (3) 中用 $\varphi(y)$ 代替 $y$, 得

$$
f(\varphi(x)+\varphi(y))=f(\varphi(y))-\varphi(f(0))+\varphi(f(x))
$$

在 (4) 中交换 $x, y$, 得

$$
f(\varphi(x)+\varphi(y))=f(\varphi(x))-\varphi(f(0))+\varphi(f(y))
$$

由 (4), (5) 可得

$$
f(\varphi(y))+\varphi(f(x))=f(\varphi(x))+\varphi(f(y)),
$$

在上式中令 $y=0$, 可得

$$
f(0)+\varphi(f(x))=f(\varphi(x))+\varphi(f(0)) .
$$

由 (3), (6) 可得

$$
f(\varphi(x)+y)=f(y)+f(\varphi(x))-f(0) .
$$

注意到 $\varphi(x)$ 为连续函数且 $\varphi(0)=0, \varphi(1)=e^{a}>0$, 由 (7) 可得

$$
f(x+y)=f(y)+f(x)-f(0)
$$

对于 $x \in\left[0, e^{a}\right], y \in \mathbb{R}$ 成立.

令 $g(x)=f(x)-f(0)$, 则由上可知, $g(x+y)=g(y)+g(x)$ 对于 $x \in$ $\left[0, e^{a}\right], y \in \mathbb{R}$ 成立.

又由 (6) 可得,

$$
\begin{aligned}
g(\varphi(x)) & =f(\varphi(x))-f(0)=\varphi(f(x))-\varphi(f(0)) \\
& \geq-\varphi(f(0)),(\text { 注意 } \varphi(f(x)) \geq 0)
\end{aligned}
$$

这表明, 当 $x \in\left[0, e^{a}\right]$ 时, $g(x) \geq-\varphi(f(0))$ 有下界.

由柯西方程性质知, $g(x)=c x(x \in \mathbb{R})$, 故 $f(x)=c x+b(c, b \in \mathbb{R}, x \in \mathbb{R})$.将其代回 (1) 式可得, $c^{2}=1$ 及 $c \varphi(x)+(c+1) b=\varphi(c x+b)$.

若 $c=-1$, 则 $\varphi(x)+\varphi(-x+b)=0$, 注意到当 $x \neq 0$ 时, $\varphi(x)>0$, 故 $\varphi(x)+\varphi(-x+b)=0$ 不会恒成立, 矛盾.

故 $c=1$, 有 $\varphi(x)+2 b=\varphi(x+b)$, 结合 $\varphi(0)=0$ 可得 $\varphi(b)=2 b, \varphi(-b)=$ $-2 b$, 而 $\varphi(x) \geq 0$ 恒成立. 故 $b=0$, 此时 $f(x)=x(x \in \mathbb{R})$.

检验可知, $f(x)=x(x \in \mathbb{R})$ 是原方程的解.

评注 本题的关键是转化为柯西方程形式后求解, 需要熟练掌握柯西方程的相关知识和基本方法.

题 2 给定一个凸 2022 面体. 随机选择 3 个面, 并在上面填数 26, 4, 2022 (每个面上填 1 个数). 甲想在每个其它的面上填一个实数, 使得它是每个与之有公共棱的面上的实数的平均数. 证明: 有且仅有一种填数的方法.
证明 先证明存在性.

设 2022 个面为 $P_{1}, P_{2}, \cdots, P_{2022}$. 若 $P_{i}, P_{j}$ 有公共棱, 则称它们“相邻”. 不妨设 26, 4, 2022 分别填在 $P_{1}, P_{2}, P_{3}$ 上. 我们先将一只小虫放在面 $P_{i}$ 上, 每过 1 秒, 小虫等概率地移动到相邻的某个面上, 且小虫移动到 $P_{1}, P_{2}, P_{3}$ 之一后就不再移动. 记时刻 $j$ 小虫在面 $P_{k}$ 上的概率为 $P_{k}^{i}(j)$ (特别地, $P_{1}^{1}(j), P_{2}^{2}(j), P_{3}^{3}(j)$恒为 1). 则有 $P_{i}^{i}(0)=1, \sum_{k=1}^{2022} P_{k}^{i}(j)=1, P_{1}^{i}(j), P_{2}^{i}(j), P_{3}^{i}(j)$ 单调不减.

我们在面 $P_{i}$ 上填数

$$
t_{i}=\lim _{j \rightarrow+\infty}\left(26 P_{1}^{i}(j)+4 P_{2}^{i}(j)+2022 P_{3}^{i}(j)\right) .
$$

有 $t_{1}=26, t_{2}=4, t_{3}=2022$, 符合题意.

且当 $i>3$ 时,

$$
\begin{aligned}
t_{i} & =\lim _{j \rightarrow+\infty}\left(26 P_{1}^{i}(j)+4 P_{2}^{i}(j)+2022 P_{3}^{i}(j)\right) \\
& =\lim _{j \rightarrow+\infty}\left(\sum_{P_{l} \text { 与 } P_{i} \text { 相邻 }}\left(26 P_{1}^{l}(j-1)+4 P_{2}^{l}(j-1)+2022 P_{3}^{l}(j-1)\right)\right)
\end{aligned}
$$

$\cdot$ $\frac{1}{\text { 与 } P_{i} \text { 相邻的面数 }}$

$=\frac{1}{\text { 与 } P_{i} \text { 相邻的面数 }} \sum_{P_{l} \text { 与 } P_{i} \text { 相邻 }} t_{l}$ (此即与 $P_{i}$ 有公共棱的面上的实数的平均数 $)$.

存在性得证.

再证明唯一性.

假设还有满足条件的另一组数 $t_{i}^{\prime}(1 \leq i \leq 2022)$, 其中 $t_{1}^{\prime}=26, t_{2}^{\prime}=4, t_{3}^{\prime}=$ 2022. 我们令 $x_{i}=t_{i}^{\prime}-t_{i}$, 则 $x_{1}=x_{2}=x_{3}=0$, 数组 $x_{i}(1 \leq i \leq 2022)$ 对应代替 $t_{i}(1 \leq i \leq 2022)$, 也满足每个面 $\left(P_{1}, P_{2}, P_{3}\right.$ 除外 $)$ 上的数等于与之有公共棱的面上的实数的平均数.

若 $\max _{4 \leq i \leq 2022} x_{i}=M>0$, 考虑到 $M$ 等于与之有公共棱的面上的实数的平均数, 结合 $M$ 最大性可得, 任意与填 $M$ 的面相邻的面上也只能填 $M$, 由连通性,可得面 $P_{1}, P_{2}, P_{3}$ 上也填写 $M$, 即 $x_{1}=x_{2}=x_{3}=0=M>0$, 矛盾.

若 $\min _{4 \leq i \leq 2022} x_{i}<0$, 类似可得矛盾. 故 $\min _{4 \leq i \leq 2022} x_{i}=\max _{4 \leq i \leq 2022} x_{i}=0$, 有 $x_{i}=0(1 \leq i \leq 2022)$. 于是数组 $t_{i}^{\prime}(1 \leq i \leq 2022)$ 与数组 $t_{i}(1 \leq i \leq 2022)$ 完全相同, 亦矛盾. 唯一性得证.

综上, 有且仅有一种填数的方法.

评注 本题比较新颖. 借助概率方法证明存在性很有意思, 用反证法和极端原理证明唯一性是经典手法.
题 3 平行四边形 $A B C D$ 的对角线交于点 $I . \triangle A B I$ 内有一点 $G$, 使得 $\angle I A G=\angle I B G \neq 45^{\circ}-\frac{\angle A I B}{4}$. 设 $E$ 为 $C$ 在 $A G$ 上的投影, $F$ 为 $D$ 在 $B G$ 上的投影. $\triangle B E F$ 的 $E$ - 中线和 $\triangle A E F$ 的 $F$-中线交于点 $H$.

(1) 证明: $A F, B E, I H$ 三线共点 (记该点为 $L$ ).

(2) $C E, D F$ 相交于点 $K$, 设 $\odot L A B, \odot E I J, \odot F I J$ 的圆心分别为 $J, M, N$.证明: $\odot G A B, \odot K C D$ 的连心线和 $E M, F N$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_7fa2899be582c1ce48f4g-05.jpg?height=837&width=1002&top_left_y=684&top_left_x=527)

证明 (1) $I$ 为 Rt $\triangle A E C$ 中斜边 $A C$ 的中点, 故 $I A=I E$. 同理, $I B=I F$.又

$$
\angle B I F=180^{\circ}-2 \angle I B F=180^{\circ}-2 \angle I A E=\angle A I E \text {, }
$$

故

$$
\angle A I F=\angle B I E \text {. }
$$

所以

$$
\triangle A I F \cong \triangle E I B
$$

由 $\triangle B E F$ 的 $E$ - 中线和 $\triangle A E F$ 的 $F$-中线交于 $H$ 得,

$$
S_{\triangle B E H}=S_{\triangle F E H}=S_{\triangle A F H} .
$$

设 $I H$ 分别交 $A F, B E$ 于点 $L_{1}, L_{2}$, 则

$$
\frac{L_{1} H}{L_{1} I}=\frac{S_{\triangle A F H}}{S_{\triangle A I F}}, \frac{L_{2} H}{L_{2} I}=\frac{S_{\triangle B E H}}{S_{\triangle B I E}},
$$

结合 (2), (3) 可得 $\frac{L_{1} H}{L_{1} I}=\frac{L_{2} H}{L_{2} I}$. 故 $L_{1}, L_{2}$ 重合, 即 $A F, B E, I H$ 三线共点.

(2) 设 $\odot G A B, \odot K C D$ 的半径分别为 $R_{1}, R_{2}$, 记两圆的圆心分别为 $O_{1}, O_{2}$.

由 $\angle A G B=\angle F G E=180^{\circ}-\angle D K C, A B=D C$ 可得

$$
R_{1}=\frac{A B}{2 \sin \angle A G B}=\frac{D C}{2 \sin \angle D K C}=R_{2}
$$

故 $\triangle A O_{1} B \cong \triangle C O_{2} D$, 又 $\triangle A I B \cong \triangle C I D$. 故四边形 $A I B O_{1} \cong$ 四边形 $C I D O_{2}$. 显然 $I$ 为这两个四边形的位似中心, 故 $I$ 为 $O_{1} O_{2}$ 的中点.

又由(2)可得 $\angle I B E=\angle I F A$, 所以 $L, B, I, F$ 四点共圆.

同理, $L, A, I, E$ 四点共圆.

所以, $I$ 为完全四边形 $F A L B E G$ 的密克尔点.

延长 $F I$ 交 $\odot A L E$ 于 $F^{\prime}$, 延长 $E I$ 交 $\odot B F L$ 于 $E^{\prime}$. 则有

$$
\angle I F^{\prime} E=\angle I A E=\angle I B F=\angle I E^{\prime} F \text {, }
$$

所以, $F, E^{\prime}, F^{\prime}, E$ 四点共圆, 于是, $E^{\prime} I \cdot I E=F I \cdot I F^{\prime}$.

故

$$
\begin{aligned}
F J^{2}-E J^{2} & =F \text { 到 } \odot J \text { 的幂 }-E \text { 到 } \odot J \text { 的幂 } \\
& =F A \cdot F L-E B \cdot E L \\
& =F I \cdot F F^{\prime}-E I \cdot E E^{\prime} \\
& =F I \cdot\left(F I+I F^{\prime}\right)-E I \cdot\left(E I+I E^{\prime}\right) \\
& =F I^{2}-E I^{2} .(\text { 用到 (6) }
\end{aligned}
$$

由定差幂线定理的逆定理可得: $I J \perp E F$.

又 $I J \perp M N$. (因为 $I J$ 为 $\odot E I J, \odot F I J$ 的根轴)

所以 $M N / / E F$.

取点 $X$, 使得 $X F / / N I$ 且 $X E / / M I$, 则 $\triangle X E F$ 与 $\triangle I M N$ 位似. 所以, $F N, E M, X I$ 三线共点. 结合(4)可知, 只需证明点 $O_{1}$ 在 $X I$ 上.

注意到

$$
\begin{aligned}
\angle E I F & =360^{\circ}-\angle B I F-\angle A I E+\angle A I B \\
& =360^{\circ}-2\left(180^{\circ}-2 \angle I B G\right)+\angle A I B \\
& =4\left(\angle I B G+\frac{\angle A I B}{4}\right) \neq 180^{\circ},
\end{aligned}
$$

故 $I, E, F$ 三点不共线.

而 $\angle I F X=\angle N I F=90^{\circ}-\angle I J F=\angle J F E$. 同理 $\angle I E X=\angle J E F$. 所以, $X, J$ 为 $\triangle I E F$ 的一对等角共轭点.

于是, 要证明 (7), 只需证明 $\angle J I F=\angle O_{1} I E$. 结合 (1)可知, 只需证明
$\angle A I J=\angle B I O_{1}$. 又 $\angle A I J+\angle B I J=\angle A I B=\angle B I O_{1}+\angle A I O_{1}$, 故只需证明

$$
\frac{\sin \angle A I J}{\sin \angle B I J} \cdot \frac{\sin \angle A I O_{1}}{\sin \angle B I O_{1}}=1
$$

由正弦定理, 得

$$
\begin{aligned}
\frac{\sin \angle A I J}{\sin \angle B I J} \cdot \frac{\sin \angle A I O_{1}}{\sin \angle B I O_{1}} & =\frac{\frac{\sin \angle A I J}{A J}}{\frac{\sin \angle B I J}{B J}} \cdot \frac{\frac{\sin \angle A I O_{1}}{A O_{1}}}{\frac{\sin \angle B O_{1}}{B O_{1}}}=\frac{\frac{\sin \angle I A J}{I J}}{\frac{\sin \angle I B J}{I J}} \cdot \frac{\frac{\sin \angle I A O_{1}}{I O_{1}}}{\frac{\sin \angle I B O_{1}}{I O_{1}}} \\
& =\frac{\sin \angle I A J \sin \angle I A O_{1}}{\sin \angle I B J \sin \angle I B O_{1}},
\end{aligned}
$$

又

$$
\begin{aligned}
\angle I A J+\angle I B O_{1} & =\angle J A B+\angle O_{1} B A+\angle B A I+\angle A B I \\
& =\left(90^{\circ}-\angle A L B\right)+\left(\angle A G B-90^{\circ}\right)+180^{\circ}-\angle A I B \\
& =(\angle A G B-\angle A I B)-\angle A L B+180^{\circ} \\
& =\angle G A I+\angle G B I-\angle A L I-\angle B L I+180^{\circ}=180^{\circ},
\end{aligned}
$$

(由(5)知, $\angle A L I=\angle G B I=\angle G A I=\angle B L I$ ).

同理, $\angle I B J+\angle I A O_{1}=180^{\circ}$. 结合(9)可得, (8)成立. 证毕.

评注 本题简洁自然. 第 (1) 问难度不大, 第 (2) 问需要大胆的猜想和细致的观察, 熟练位似、等角共轭等基本的几何模型及三角计算.

题 4 锐角不等边 $\triangle A B C$ 的外心为 $O, B C$ 边的中点为 $I$. 直线 $O I$ 分别交 $A B, A C$ 于点 $E, F . D$ 为 $A$ 关于 $O$ 的对称点, $G$ 为 $A$ 关于 $\triangle A E F$ 外心的对称点, $K$ 为 $O$ 关于 $\triangle O B C$ 外心的对称点.

(1) 证明: $D, G, K$ 三点共线.

(2) 设 $M, N$ 分别是 $K B, K C$ 上的点, 满足 $I M \perp A C, I N \perp A B . I K$ 的垂直平分线交 $M N$ 于点 $H, I H$ 分别交 $A B, A C$ 于点 $P, Q$. 证明: $\triangle A P Q$ 的外接圆与圆 $O$ 的另一个交点 (不同于 $A$ ) 在直线 $A I$ 上.

证明 (1) 不妨设 $A B<A C$, 记 $\triangle A B C$ 的外接圆半径为 $R$, 三个内角分别为 $A, B, C . O I$ 为 $B C$ 的中垂线且 $K$ 在 $O I$ 上.

由 $A E \perp B D, A F \perp C D, E F \perp B C$ 可得 $\triangle A E F \sim \triangle D B C$. 又 $G$ 为 $A$关于 $\odot A E F$ 的对径点, $A$ 为 $D$ 关于 $\odot D B C$ 的对径点, 所以 $G, A$ 也是相似对应点. 故四边形 $A E G F \sim$ 四边形 $D B A C$. 两个相似形的 5 组对应边互相垂直,可得 $A G \perp A D$. 于是,

$$
\tan \angle O D G=\frac{A G}{A D}=\frac{A F}{D C}=\frac{A C-F C}{D C}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_7fa2899be582c1ce48f4g-08.jpg?height=740&width=439&top_left_y=218&top_left_x=817)

$$
\begin{aligned}
& =\frac{2 R \sin B-\frac{R \sin A}{\cos C}}{2 R \cos B} \\
& =\frac{\sin (B-C)}{2 \cos B \cos C}
\end{aligned}
$$

$K$ 为 $O$ 在 $\odot O B C$ 上的对径点, $\therefore \angle O B K=\angle O C K=90^{\circ} . \therefore O D^{2}=$ $O B^{2}=O I \cdot O K . \therefore \angle O D K=\angle O I D=90^{\circ}+\angle T I B$. (设 $D$ 关于 $I$ 的对称点为 $T$, 由熟知结论, $T$ 为 $\triangle A B C$ 的垂心). 于是,

$$
\begin{aligned}
\tan \angle O D K & =-\cot T I B=-\frac{B I-B T \cos \angle T B C}{B T \sin \angle T B C} \\
& =-\frac{\frac{\sin A}{2 \cos B}-\sin C}{\cos C}=-\frac{\sin (B-C)}{2 \cos B \cos C}
\end{aligned}
$$

由(1), (2)得, $\angle O D G+\angle O D K=180^{\circ}$. 故 $D, G, K$ 三点共线.

(2) 延长 $A I$ 交 $\odot O$ 于点 $X$, 设 $\triangle I X K$ 的外心为 $H^{\prime}$, 则 $H^{\prime}$ 在 $A K$ 的中垂线上, 我们证明 $H^{\prime}, M, N$ 共线. 这只需证明

$$
\frac{\sin \angle I H^{\prime} M}{\sin \angle K H^{\prime} M}=\frac{\sin \angle I H^{\prime} N}{\sin \angle K H^{\prime} N}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_7fa2899be582c1ce48f4g-08.jpg?height=536&width=420&top_left_y=2062&top_left_x=818)
对 $\triangle I H^{\prime} K$ 及点 $M, N$, 由角元塞瓦定理得

$$
\begin{aligned}
& \frac{\sin \angle I H^{\prime} M}{\sin \angle K H^{\prime} M} \cdot \frac{\sin \angle H^{\prime} K M}{\sin \angle M K I} \cdot \frac{\sin \angle K I M}{\sin \angle H^{\prime} I M}=1 \\
& \frac{\sin \angle I H^{\prime} N}{\sin \angle K H^{\prime} N} \cdot \frac{\sin \angle H^{\prime} K N}{\sin \angle N K I} \cdot \frac{\sin \angle K I N}{\sin \angle H^{\prime} I N}=1
\end{aligned}
$$

又 $O I \cdot I K=I B \cdot I C=A I \cdot I X$, 所以 $O, K, A, X$ 共圆.

$\therefore \angle H^{\prime} I K=\angle H^{\prime} K I=\angle I X K-90^{\circ}=\angle A O I-90^{\circ}=90^{\circ}-(B-C)$,

于是,

$$
\begin{aligned}
& \angle N K I=\angle M K I=90^{\circ}-A, \\
& \angle H^{\prime} K M=\angle H^{\prime} K I-\angle M K I=180^{\circ}-2 B, \\
& \angle H^{\prime} K N=2 C, \angle K I M=C, \\
& \angle H^{\prime} I M=90^{\circ}-B, \angle K I N=B, \\
& \angle H^{\prime} I N=90^{\circ}+C .
\end{aligned}
$$

故由(4), (5)可得,

$$
\begin{aligned}
& \frac{\sin \angle I H^{\prime} M}{\sin \angle K H^{\prime} M}=\frac{\sin \angle M K I}{\sin \angle H^{\prime} K M} \cdot \frac{\sin \angle H^{\prime} I M}{\sin \angle K I M}=\frac{\cos A}{\sin 2 B} \cdot \frac{\cos B}{\sin C}=\frac{\cos A}{2 \sin B \sin C} . \\
& \frac{\sin \angle I H^{\prime} N}{\sin \angle K H^{\prime} N}=\frac{\sin \angle N K I}{\sin \angle H^{\prime} K N} \cdot \frac{\sin \angle H^{\prime} I N}{\sin \angle K I N}=\frac{\cos A}{\sin 2 C} \cdot \frac{\cos C}{\sin B}=\frac{\cos A}{2 \sin B \sin C} .
\end{aligned}
$$

所以(3)式成立. $H^{\prime}, M, N$ 共线. 从而 $H^{\prime}=H, H$ 为 $\triangle I X K$ 的外心.

$\therefore \angle B P Q=B-\angle B I H=B-\left(90^{\circ}-\angle H I K\right)=B-(B-C)=C$.

$\therefore B, P, C, Q$ 共圆. $\therefore P I \cdot I Q=B I \cdot I C=A I \cdot I X$.

$\therefore X$ 在 $\odot A P Q$ 上.

即 $\triangle A P Q$ 的外接圆与圆 $O$ 的另一个交点 $X$ 在直线 $A I$ 上. 证毕.

评注 本题难度不大, 方法经典. 需要从整体上分析图形的结构并熟练同一法及三角计算.

题 5 对于实数 $x$, 若存在 $b \in\{2,3, \cdots, 2022\}$, 使得 $x$ 在 $b$ 进制下可表示为有限小数, 则称 $x$ 为 “漂亮数”. 证明: 仅存在有限个正整数 $n(n \geq 4)$, 使得对于任意正整数 $m \in\left(\frac{2}{3} n, n\right)$, 两数 $\frac{n}{m-n}, \frac{n-m}{m}$ 当中至少有一个漂亮数.

证明 我们先证明如下引理.

引理 存在 $N_{0}$, 当正整数 $n>N_{0}$ 时, 必有

$$
\frac{\varphi(n)}{3}>2+2^{w(n)}+\left(\frac{\ln n}{\ln 2}+1\right)\left(\frac{\ln n}{\ln 3}+1\right) \ldots\left(\frac{\ln n}{\ln 2022}+1\right) .
$$

其中 $\varphi(n)$ 为欧拉函数, $w(n)$ 为 $n$ 的素因子的个数.
命题.

证明 设 $n=\prod_{i=1}^{t} p_{i}^{\alpha_{i}}\left(p_{i}\right.$ 为互异的素数, $\left.\alpha_{i} \in \mathbb{N}_{+}\right)$. 我们只需证明下面两个

命题 (1): 存在 $N_{1}$, 当正整数 $n>N_{1}$ 时,

$$
\frac{\varphi(n)}{6}>2+2^{w(n)}
$$

命题 (2): 存在 $N_{2}>2022$, 当正整数 $n>N_{2}$ 时,

$$
\frac{\varphi(n)}{6}>\left(\frac{\ln n}{\ln 2}+1\right)\left(\frac{\ln n}{\ln 3}+1\right) \ldots\left(\frac{\ln n}{\ln 2022}+1\right)
$$

对于命题 (1), 注意到

$$
\begin{aligned}
& 2+2^{w(n)}=2+2^{t} \leq 2^{t+1} \\
& \varphi(n)=\prod_{i=1}^{t} p_{i}^{\alpha_{i}-1}\left(p_{i}-1\right) \geq \prod_{i=1}^{t} \frac{p_{i}^{\alpha_{i}}}{2}\left(\because p_{i}-1 \geq \frac{p_{i}}{2}\right) .
\end{aligned}
$$

故只需 $\frac{\prod_{i=1}^{t} \frac{p_{i}^{\alpha_{i}}}{2}}{6}>2^{t+1}$, 即只需 $\prod_{i=1}^{t} \frac{p_{i}^{\alpha_{i}}}{4}>12$.

当 $n$ 足够大时, 上式显然成立, 命题 (1) 得证.

对于命题 (2), 注意到

$$
\begin{aligned}
& \left(\frac{\ln n}{\ln 2}+1\right)\left(\frac{\ln n}{\ln 3}+1\right) \cdots\left(\frac{\ln n}{\ln 2022}+1\right) \\
& <2^{2021} \cdot \frac{(\ln n)^{2021}}{\ln 2 \cdots \ln 2022}\left(\because n>N_{2}>2022 \geq i \geq 2 \text { 时, } \frac{\ln n}{\ln i}+1<2 \frac{\ln n}{\ln i}\right) \\
& <2^{2021}(\ln n)^{2021}, \\
& \varphi(n)=\prod_{i=1}^{t} p_{i}^{\alpha_{i}-1}\left(p_{i}-1\right) \geq \prod_{i=1}^{t} \frac{p_{i}^{\alpha_{i}}}{2}=\frac{n}{2^{t}} .
\end{aligned}
$$

故只需 $\frac{n}{6 \cdot 2^{t}}>2^{2021}(\ln n)^{2021}$, 即只需 $\frac{n}{(\ln n)^{2021 \cdot 2^{t}}}>6 \cdot 2^{2021}$.

又 $n \geq p_{1} \cdots p_{t} \geq 2 \cdot 3^{t-1}, \therefore t \leq \log _{3}\left(\frac{3}{2} n\right), \therefore 2^{t} \leq\left(\frac{3}{2} n\right)^{\frac{\ln 2}{\ln 3}}$,

故只需

$$
\frac{n^{1-\frac{\ln 2}{\ln 3}}}{(\ln n)^{2021}}>6 \cdot 2^{2021} \cdot\left(\frac{3}{2}\right)^{\frac{\ln 2}{\ln 3}} .
$$

当 $n$ 足够大时, 上式成立 (取自然对数可知, $\frac{n^{1-\frac{\ln 2}{\ln 3}}}{(\ln n)^{2021}}$ 在 $n$ 足够大时递增且无上界), 命题 (2) 得证. 引理证毕.

回到原题.

当 $n>N_{0}$ 时 (满足引理的 $\left.n>N_{0}\right)$, 设满足 $m \in\left(\frac{2}{3} n, n\right)$ 且 $(m, n)=1$ 的 $m$ 的个数为 $S$. 则

$$
S=\left(\left\lceil\frac{n}{3}\right\rceil-1\right)-\left(\left\lceil\frac{\left\lceil\frac{n}{3}\right\rceil-1}{p_{1}}\right]+\cdots+\left[\frac{\left\lceil\frac{n}{3}\right\rceil-1}{p_{t}}\right]\right)+\sum_{1 \leq i<j \leq t}\left[\frac{\left\lceil\frac{n}{3}\right\rceil-1}{p_{i} p_{j}}\right]-\cdots
$$

$$
\begin{aligned}
& \geq\left\lceil\frac{n}{3}\right\rceil-1-\frac{\left\lceil\frac{n}{3}\right\rceil-1}{p_{1}}-\cdots-\frac{\left\lceil\frac{n}{3}\right\rceil-1}{p_{t}}+\sum_{1 \leq i<j \leq t}\left(\frac{\left\lceil\frac{n}{3}\right\rceil-1}{p_{i} p_{j}}-1\right)-\cdots \\
& \geq\left(\left\lceil\frac{n}{3}\right\rceil-1\right)\left(1-\frac{1}{p_{1}}\right) \cdots\left(1-\frac{1}{p_{t}}\right)-2^{t} \\
& \geq\left\lceil\frac{n}{3}\right\rceil\left(1-\frac{1}{p_{1}}\right) \cdots\left(1-\frac{1}{p_{t}}\right)-2^{t}-1 \\
& \geq \frac{\varphi(n)}{3}-2^{t}-1 \\
& >1+\prod_{i=2}^{2022}\left(\log _{i} n+1\right) \quad(\text { 由引理 }) \\
& \geq 1+\prod_{i=2}^{2022}\left(1+\left[\log _{i} n\right]\right) \\
& =1+\left|\left\{\left(x_{2}, \cdots, x_{2022}\right) \mid x_{i} \in \mathbb{N}, x_{i} \leq \log _{i} n\right\}\right| .
\end{aligned}
$$

对于 $y \leq n$, 若只有不超过 2022 的素因子, 则可唯一对应 $\left(\beta_{2}, \cdots, \beta_{2022}\right)$,其中 $i^{\beta_{i}} \mid y, i^{\beta_{i}+1} \nmid y, \beta_{i} \in\left[0, \log _{i} n\right]$. 故可建立集合 $\{y \mid y \leq n, y$ 的素因子都不超过 2022$\}$ 到 $\left\{\left(x_{2}, \cdots, x_{2022}\right) \mid x_{i} \in \mathbb{N}, x_{i} \leq \log _{i} n\right\}$ 的单射. 所以

$$
\begin{aligned}
S & >1+\left|\left\{\left(x_{2}, \cdots, x_{2022}\right) \mid x_{i} \in \mathbb{N}, x_{i} \leq \log _{i} n\right\}\right| \\
& \geq 1+\mid\{y \mid y \leq n, y \text { 的素因子都不超过 } 2022\} \mid .
\end{aligned}
$$

又 $m \in\left(\frac{2}{3} n, n\right)$ 时, $n-m \in\left(0, \frac{n}{3}\right)$, 由抽屉原理可得, 当 $n>N_{0}$ 时, 存在 $m \in\left(\frac{2}{3} n, n\right),(m, n)=1$ 且 $m$ 与 $n-m$ 均存在大于 2022 的素因子, 于是两数 $\frac{n}{m-n}, \frac{n-m}{m}$ 均不是漂亮数. (注意到对 $x=\frac{p}{q} \in \mathbb{Q}$, 其中 $p, q \in \mathbb{Z},(p, q)=1, x$ 不为漂亮数的一个充分条件是 $q$ 有大于 2022 的素因子).

综上, 满足条件的 $n \leq N_{0}$ 个数有限, 命题得证.

评注本题的关键是等价转化为当 $n$ 充分大时, 一定能找到满足条件的 $m$.不等式估计是常见的手法, 而当 $n$ 充分大时, 放缩时只要注意“级别”即可.

题 6 已知集合 $A \in\{1,2, \cdots, 4044\}$.甲将其中 2022 个数染成白色, 剩余 2022 个数染成黑色. 对于每个 $i \in A$, 所有小于 $i$ 的白色数与所有大于 $i$ 的黑色数之和称为 $i$ 的“重要数”. 求所有可能的正整数 $k$, 使得存在自然数 $m$ 和一种染色方式, 满足有 $k$ 个数的重要数为 $m$.

解 若 $a, b\left(1 \leq a<b \leq 4044, a, b \in \mathbb{N}_{+}\right)$的重要数均为 $m$, 且区间 $(a, b)$中每个数的重要数都不等于 $m$, 则记 $\Delta=b-a$, 并设 $(a, b)$ 中的黑色数之和为 $S_{1}$, 白色数之和为 $S_{2}$. 我们考虑下面三种情形.
情形 (1): 当 $a, b$ 均为黑色时, 有 $S_{2}-S_{1}=b$.

若 $\Delta=1$, 则 $S_{1}=S_{2}=0$, 矛盾.

若 $\Delta=2$, 则 $S_{1}=a+1, S_{2}=0$, 或 $S_{1}=0, S_{2}=a+1$, 矛盾.

若 $\Delta=3$, 则 $S_{2}-S_{1}= \pm 1, \pm(2 a+3)$, 有 $S_{2}-S_{1} \neq b$, 矛盾.

所以, $\Delta \geq 4$, 且若 $\Delta=4$, 则区间 $(a, b]$ 中的 4 个整数必染为两黑两白 (依次为“黑白白黑”).

情形 (2): 当 $a, b$ 均为白色时, 有 $S_{1}-S_{2}=a$.

类似 (1) 可得, $\Delta \neq 1,2$.

若 $\Delta=3$, 则 $a=1, b=4,1,2,3,4$ 依次染为 “白白黑白”, 1 和 3 的重要数相等, 矛盾.

所以, $\Delta \geq 4$, 且若 $\Delta=4$, 则区间 $(a, b]$ 中的 4 个整数必染为两黑两白 (依次为“黑黑白白”).

情形 (3): 当 $a$ 为白色, $b$ 为黑色时, 有 $S_{2}-S_{1}=b-a$.

若 $\Delta=1$, 则 $S_{1}=S_{2}=0$, 矛盾.

若 $\Delta=2$, 则 $a=1, b=3$, 所以 $1,2,3$ 依次染为 “白白黑”.

若 $\Delta=3$, 则 $S_{2}-S_{1}= \pm 1, \pm(2 a+3)$, 有 $S_{2}-S_{1} \neq b-a$, 矛盾.

若 $\Delta=4$, 分类讨论可知区间 $(a, b)$ 中的整数染 “黑” 的恰好 1 个. 可能的情形如下:

- $a=2, b=6,2,3,4,5,6$ 依次染为“白白黑白黑”;
- $a=4, b=8,4,5,6,7,8$ 依次染为“白白白黑黑”.

若 $\Delta=5=S_{2}-S_{1}$, 可得 $S_{2}+S_{1}=a+1+a+2+a+3+a+4=4 a+10$为偶数. 这不可能.

若 $\Delta=6$, 则可知区间 $(a, b)$ 中的整数染 “黑” 的恰好 2 个. 这是因为, 若染“黑”的个数多于 2 个, 则

$$
6=S_{2}-S_{1} \leq(a+5)+(a+4)-(a+3)-(a+2)-(a+1)=3-a<6,
$$

矛盾. 若染“黑”的个数少于 2 个, 则

$$
6=S_{2}-S_{1} \geq(a+1)+(a+2)+(a+3)+(a+4)-(a+5)=3 a+5>6,
$$

也矛盾. 可能的情形如下:

- 1, 2, 3, 4, 5, 6, 7 依次染为“白黑白白黑白黑”或“白白黑黑白白黑”;
- $3,4,5,6,7,8,9$ 依次染为“白黑白白白黑黑”或“白白黑白黑白黑”;
- $5,6,7,8,9,10,11$ 依次染为“白白黑白白黑黑”或“白白白黑黑白黑”;
- 7, 8, 9, 10,11,12, 13 依次染为“白白白黑白黑黑”;
- 9, 10,11,12,13,14, 15 依次染为“白白白白黑黑黑”.

若 $\Delta=7=S_{2}-S_{1}$, 若区间 $(a, b)$ 中的整数染 “黑” 的个数多于 3 个, 则

$7=S_{2}-S_{1} \leq(a+6)+(a+5)-(a+1)-(a+2)-(a+3)-(a+4)=1-2 a<7$,

矛盾. 若区间 $(a, b)$ 中的整数染 “黑” 的个数少于 3 个, 则

$7=S_{2}-S_{1} \geq(a+1)+(a+2)+(a+3)+(a+4)-(a+6)-(a+5)=2 a-1$,

$\Rightarrow a \leq 4, b \leq 11$.

故 $b>11$ 时, 若 $\Delta=7$, 区间 $(a, b]$ 中的 7 个整数必染为 4 黑 3 白.

我们证明: 所求的 $k \leq 1013$.

假设存在自然数 $m$ 和一种染色方式, 满足有 $k(k \geq 1014)$ 个数的重要数为 $m$, 称这 $k$ 个数均为 “好数” 并设为 $a_{1}<a_{2}<\cdots<a_{k}$. 设 $a_{1}, a_{2}, \cdots, a_{k}$ 中 “黑段”的长依次为 $x_{1}, x_{2}, \cdots$, “白段” 的长依次为 $y_{1}, y_{2}, \cdots$ (记 $a_{1}, a_{2}, \cdots, a_{k}$ 中连续若干个染黑色的数为 “黑段” (至少 1 个, 连续多个相邻数染黑时取完整记为一段), 其中整数的个数为黑段的长, 类似定义 “白段” 和白段的长). 下面分四类讨论.

(1) $a_{1}$ 为黑色, $a_{k}$ 为白色. 则

$$
4043 \geq a_{k}-a_{1}=\left(a_{2}-a_{1}\right)+\left(a_{3}-a_{2}\right)+\cdots+\left(a_{k}-a_{k-1}\right) .
$$

注意到相邻的两个好数同色, 则 $\Delta \geq 4$ (情形(1), (2)), 相邻两个好数若依次染为“白黑”, 则 $\Delta=2,4,6$ 的情形至多各出现一次 (特别地, 第 (1) 类中 $\Delta>2$ ) 余下的情形 $\Delta \geq 7$ (情形(3)), 相邻两个好数若依次染为“黑白”, 则 $\Delta \geq 1$, 故

$$
\begin{aligned}
\text { 上式 } \geq & 4\left(x_{1}-1\right)+1+4\left(y_{1}-1\right)+4+4\left(x_{2}-1\right)+1+4\left(y_{2}-1\right)+6 \\
& +4\left(x_{3}-1\right)+1+4\left(y_{3}-1\right)+7+4\left(x_{4}-1\right)+\cdots+1+4\left(y_{u}-1\right) \\
= & \left(4 x_{1}+4 y_{1}-7\right)+\left(4 x_{2}+4 y_{2}-3\right)+\left(4 x_{3}+4 y_{3}-1\right)+4\left(x_{4}+y_{4}\right) \\
& +\cdots+4\left(x_{u}+y_{u}\right) \\
\geq & 4\left(x_{1}+y_{1}+x_{2}+y_{2}+\cdots+x_{u}+y_{u}\right)-11 \\
= & 4 k-11 . \quad(u \leq 3 \text { 时也成立 }) \\
\Rightarrow & k \leq\left[\frac{4054}{4}\right]=1013 . \text { 矛盾. }
\end{aligned}
$$

(2) $a_{1}$ 为黑色, $a_{k}$ 为黑色. 类似 (1) 可得

$$
4043 \geq a_{k}-a_{1}=\left(a_{2}-a_{1}\right)+\left(a_{3}-a_{2}\right)+\cdots+\left(a_{k}-a_{k-1}\right)
$$

$$
\begin{aligned}
& \geq\left(4 x_{1}+4 y_{1}-7\right)+\left(4 x_{2}+4 y_{2}-3\right)+\left(4 x_{3}+4 y_{3}-1\right)+4\left(x_{4}+y_{4}\right) \\
&+\cdots+4\left(x_{u-1}+y_{u-1}\right)+4+\left(4 x_{u}-1\right) \\
& \geq 4\left(x_{1}+y_{1}+x_{2}+y_{2}+\cdots+x_{u-1}+y_{u-1}+x_{u}\right)-8 \\
&=4 k-8 . \\
& \Rightarrow k \leq\left[\frac{4051}{4}\right]=1012 . \text { 矛盾. }
\end{aligned}
$$

(3) $a_{1}$ 为白色, $a_{k}$ 为黑色. 类似 (1) 可得

$$
\begin{aligned}
4043 \geq & a_{k}-a_{1}=\left(a_{2}-a_{1}\right)+\left(a_{3}-a_{2}\right)+\cdots+\left(a_{k}-a_{k-1}\right) \\
\geq & 4\left(y_{1}-1\right)+2+4\left(x_{1}-1\right)+1+4\left(y_{2}-1\right)+4+4\left(x_{2}-1\right) \\
& +\cdots+1+4\left(y_{u}-1\right)+7+4\left(x_{u}-1\right) \\
\geq & \left(4 x_{1}+4 y_{1}-6\right)+\left(4 x_{2}+4 y_{2}-3\right)+\left(4 x_{3}+4 y_{3}-1\right) \\
& +4\left(x_{4}+y_{4}\right)+\cdots+4\left(x_{u}+y_{u}\right) \\
\geq & 4\left(x_{1}+y_{1}+x_{2}+y_{2}+\cdots+x_{u}+y_{u}\right)-10 \\
= & 4 k-10 .
\end{aligned}
$$

$$
\Rightarrow k \leq\left[\frac{4053}{4}\right]=1013 \text {. 矛盾. }
$$

(4) $a_{1}$ 为白色, $a_{k}$ 为白色. 类似 (1) 可得

$$
\begin{aligned}
4043 \geq & a_{k}-a_{1}=\left(a_{2}-a_{1}\right)+\left(a_{3}-a_{2}\right)+\cdots+\left(a_{k}-a_{k-1}\right) \\
\geq & \left(4 x_{1}+4 y_{1}-6\right)+\left(4 x_{2}+4 y_{2}-3\right)+\left(4 x_{3}+4 y_{3}-1\right)+4\left(x_{4}+y_{4}\right) \\
& +\cdots+4\left(x_{u-1}+y_{u-1}\right)+1+4\left(y_{u}-1\right) \\
\geq & 4\left(x_{1}+y_{1}+x_{2}+y_{2}+\cdots+x_{u-1}+y_{u-1}+y_{u}\right)-13 \\
& =4 k-13 . \\
\Rightarrow k \leq & {\left[\frac{4056}{4}\right]=1014 . }
\end{aligned}
$$

而 $k=1014$ 时，必有 $a_{1}=1, a_{2}=3, a_{3}=4, a_{4}=8, a_{5}=9, a_{6}=$ $15, a_{7}=16, a_{l}=4044$ (结合(3)中 $\Delta=2,4,6$ 的情形可知). $1,2, \cdots, 16$ 依次染为“白白黑白白白黑黑白白白黑黑黑白”, 其中白比黑多4 个. $a_{8} \geq 17>11$,结合(1),(2)中 $\Delta=4$ 及(3)中 $\Delta=7$ 的情形可知,

对于 $i \geq 7$, 若 $a_{i}, a_{i+1}$ 染为 “黑白”, 则 $a_{i+1}-a_{i}=1, a_{i}, a_{i+1}$ 相邻; 若 $a_{i}, a_{i+1}$染为“白黑”, 则 $a_{i+1}-a_{i}=7$, 区间 $\left(a_{i}, a_{i+1}\right]$ 中的数 3 白 4 黑; 若 $a_{i}, a_{i+1}$ 染为“白白”或“黑黑”, 则 $a_{i+1}-a_{i}=4$, 区间 $\left(a_{i}, a_{i+1}\right]$ 中的数 2 白 2 黑.

所以，区间 $\left(a_{7}, a_{k}\right]$ 中黑, 白的个数相等 (注意到 $a_{7}, a_{l}$ 均为白, 故区间
$\left[a_{7}, a_{l}\right]$ 中 “ $a_{i}, a_{i+1}$ 黑白对”与 “ $a_{i}, a_{i+1}$ 白黑对”个数相等. “黑白”对的情形可以看成区间 $\left(a_{i}, a_{i+1}\right]$ 中的数只有 1 个, 为白色), 于是, 区间 $[1,4044]$ 中的白比黑多 4 个, 矛盾.

综上, $k \leq 1013$.

下面我们对 $n(n \geq 4)$ 归纳. 对任意自然数 $k \in\left[0,\left[\frac{n}{2}\right]+2\right]$, 存在自然数 $m$和一种染色方式, 将 $1,2, \cdots, 2 n$ 中的 $n$ 个数染白, 另 $n$ 个数染黑, 使得恰有 $k$个数的重要数为 $m$. (重要数的定义相同)

$n=4$ 时, $0 \leq k \leq 4$. 若 $k=4$, 将 $1,2, \cdots, 8$ 依次染为“黑白白黑白黑白黑”, 则仅有 $1,2,6,7$ 的重要数均为 18 ; 若 $k=3$, 依次染为 “黑白白黑白黑黑白”, 则仅有 $1,2,6$ 的重要数均为 17 ; 若 $k=2$, 依次染为“黑黑黑黑白白白白”,则仅有 4,5 的重要数相等且均为 0 ; 若 $k=1$ 依次染为 “白白白白黑黑黑黑”, 则仅有 4 的重要数为 32 ; 若 $k=0$, 取 $m=10^{100}$, 可随便染. 故 $n=4$ 时命题成立.

若 $n=2 l(l \geq 2)$ 时命题成立, 考虑 $n=2 l+1$ 时的情形, 对于 $0 \leq k \leq l+2$,由归纳假设, 存在自然数 $m_{0}$ 和一种染色方式, 将 $1,2, \cdots, 4 l$ 中的 $2 l$ 个数染白, 另 $2 l$ 个数染黑, 使得恰有 $k$ 个数的重要数为 $m_{0}$.

若 $m_{0} \neq X-(4 l+1)$, (其中 $X$ 为区间 $[1,4 l]$ 中的所有白色数之和), 只需染黑 $4 l+1$, 染白 $4 l+2,[1,4 l]$ 中的数的染色不变, 则恰有 $k$ 个数的重要数为 $m_{0}+4 l+1$.

若 $m_{0}=X-(4 l+1)$, 只需染白 $4 l+1$, 染黑 $4 l+2,[1,4 l]$ 中的数的染色不变, 则恰有 $k$ 个数的重要数为 $m_{0}+4 l+2 .\left(4 l+1\right.$ 的重要数为 $m_{0}+8 l+3,4 l+2$的重要数为 $\left.m_{0}+8 l+2\right)$.

所以 $n=2 l+1$ 时命题成立.

再考虑 $n=2 l+2$ 时的情形.

对于 $0 \leq k \leq l+2$, 类似上面可证命题成立. 对于 $k=l+3$, 只需将 $1,2, \cdots, 4 l+4$ 依次染为“白白黑白黑黑白白黑黑白 $\cdots$ 白黑黑白白黑黑黑”, 则 $1,3,4,8,9,13, \cdots, 4 l+1$ 的重要数相同, 且与其它数的重要数不相等, 命题也成立.

综上, 所求的 $k$ 为所有不超过 1013 的自然数.

评注 本题的关键是分析猜测出临界值 1013, 证明结论需要细致的分类和大胆的放缩。另外, Aops 上的英文版试题不知道是否有误，翻译出来是“对于任意自然数, 求所有可能的正整数, 使得存在一种染色方式, 满足有 $k$ 个数的重要数为 $m$. . 这种情形笔者并没有解决, 有兴趣的同学不妨一试.


[^0]:    修订日期: 2022-05-26.

