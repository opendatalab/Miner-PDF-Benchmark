# 数学新星网 $\%$ 冷岗松专栏 

www.nsmath.cn/lgszl

## 一个 Helly 型组合问题

冷岗松施柯杰

匈牙利的 Kömal 杂志 A608 (2014) 是一道十分有趣的组合问题, 可叙述如下:

问题 1. 设平面上的凸多边形 $P_{1}, P_{2}, P_{3}$ 满足对任意的 $A \in P_{1}, B \in P_{2}, C \in$ $P_{3}, \triangle A B C$ 的面积不超过 1 . 证明: $P_{1}, P_{2}, P_{3}$ 中某两个的面积之和不超过 8 .

供题人是匈牙利的 Tamas Fleiner 教授. Fleiner 教授是近年来 Kürschak competition 委员会的主席, 而 Kürschak competition 是匈牙利最重要也是历史最悠久的数学竞赛. Fleiner 教授来信告诉我们, 这个 Helly 型组合问题是 Kürschak competition 的预选题, 因考虑到它作为考试题可能太难, 因而他们提出了一个简化版本作为 2013 年 Kürschak competition 的试题, 这就是:

问题 2. 设平面上的凸多边形 $P_{1}, P_{2}, P_{3}$ 满足对任意 $A \in P_{1}, B \in P_{2}, C \in P_{3}$, $\triangle A B C$ 的面积不超过 1 . 证明:

(i) $P_{1}, P_{2}, P_{3}$ 中至少有一个面积不超过 4 ；

(ii) 可以构造具有上述性质的三个凸多边形 $P_{1}, P_{2}, P_{3}$ 使得其中两个的面积都大于 4 .

问题 1 的难度真的像 Fleiner 教授所说一样吗? 这两年, 我们把这个问题给过多位高手征解, 但仅有深圳的女学生吴东晓 (2015 年中国国家集训队队员) 给出了一个解答. 对于中学生来说, 这可真是个难题!

## 问题 1 的解 (根据吴东晓解答整理):

不妨设 $P_{1}, P_{2}, P_{3}$ 中 $P_{1}$ 的直径 (即凸多边形内部两点的最大距离) 最大, 并设 $P_{1}$ 的直径为 $A_{1} A_{2}$. 设 $A_{1} A_{2}$ 所在直线为 $x$ 轴. 对任意一点 $M$, 记 $x_{M}, y_{M}$ 分别为 $M$ 的横坐标和纵坐标, 则任取 $P_{2}$ 中一点 $B, P_{3}$ 中一点 $C$, 下证

$$
\left|y_{B}-y_{C}\right| \leq \frac{4}{\left|A_{1} A_{2}\right|}
$$

由对称性不妨设 $\left|y_{B}\right| \geq\left|y_{C}\right|$, 且 $y_{B} \geq 0$ (否则以 $x$ 轴为对称轴翻转图形即
可), 那么 $B, C$ 的位置关系有以下三种情况:

(i) $C$ 在 $\angle A_{1} B A_{2}$ 内. 此时

$$
\frac{1}{2}\left|A_{1} A_{2}\right|\left(y_{B}-y_{C}\right)=S_{A_{1} B A_{2} C}=S_{\triangle A_{1} B C}+S_{\triangle A_{2} B C} \leq 2
$$

故

$$
y_{B}-y_{C} \leq \frac{4}{\left|A_{1} A_{2}\right|}
$$

(ii) $C$ 在 $\angle A_{1} B A_{2}$ 外, 且在 $x$ 轴下方. 不妨设 $C$ 与 $A_{2}$ 在直线 $A_{1} B$ 的两侧,此时

$$
\frac{1}{2}\left|A_{1} A_{2}\right|\left(y_{B}-y_{C}\right)=S_{A_{1} A_{2} B}+S_{A_{1} A_{2} C} \leq S_{\triangle A_{1} B C} \leq 1
$$

故

$$
y_{B}-y_{C} \leq \frac{2}{\left|A_{1} A_{2}\right|} \leq \frac{4}{\left|A_{1} A_{2}\right|}
$$

(iii) $C$ 在 $\angle A_{1} B A_{2}$ 外, 且在 $x$ 轴上方. 不妨设 $C$ 与 $A_{2}$ 在直线 $A_{1} B$ 的两侧,作平行四边形 $A_{1} B^{\prime} B C$, 则 $y_{B^{\prime}}=y_{B}-y_{C} \leq y_{B}$, 从而

$$
\frac{1}{2}\left|A_{1} A_{2}\right|\left(y_{B}-y_{C}\right)=S_{\triangle A_{1} A_{2} B^{\prime}} \leq S_{\triangle A_{2} B C} \leq 1
$$

故

$$
y_{B}-y_{C} \leq \frac{2}{\left|A_{1} A_{2}\right|} \leq \frac{4}{\left|A_{1} A_{2}\right|}
$$

综上便知 $(*)$ 式得证.

设 $P_{2}$ 中纵坐标最大, 最小的点分别为 $B_{1}, B_{2}, P_{3}$ 中纵坐标最大, 最小的点分别为 $C_{1}, C_{2}$, 则

$$
y_{B_{1}}-y_{B_{2}}+y_{C_{1}}-y_{C_{2}} \leq\left|y_{B_{1}}-y_{C_{2}}\right|+\left|y_{C_{1}}-y_{B_{2}}\right| \leq \frac{8}{\left|A_{1} A_{2}\right|}
$$

再设 $P_{2}$ 中横坐标最大, 最小的点分别为 $B_{1}^{\prime}, B_{2}^{\prime}, P_{3}$ 中纵坐标最大, 最小的点分别为 $C_{1}^{\prime}, C_{2}^{\prime}$, 则由 $\left|A_{1} A_{2}\right|$ 的最大性知

$$
x_{B_{1}^{\prime}}-x_{B_{2}^{\prime}} \leq\left|A_{1} A_{2}\right|, \quad x_{C_{1}^{\prime}}-x_{C_{2}^{\prime}} \leq\left|A_{1} A_{2}\right| .
$$

故

$$
\begin{aligned}
S_{P_{2}}+S_{P_{3}} & \leq\left(x_{B_{1}^{\prime}}-x_{B_{2}^{\prime}}\right)\left(y_{B_{1}}-y_{B_{2}}\right)+\left(x_{C_{1}^{\prime}}-x_{C_{2}^{\prime}}\right)\left(y_{C_{1}}-y_{C_{2}}\right) \\
& \leq\left|A_{1} A_{2}\right| \cdot \frac{8}{\left|A_{1} A_{2}\right|}=8 .
\end{aligned}
$$

即 $P_{2}, P_{3}$ 的面积之和不超过 8.

问题 2 的 (i) 显然是问题 1 的直接推论, (ii) 则说明了 (i) 中结论的某种最优性.

## 问题 2 (ii) 的解 (根据王逸轩解答整理):

构造 $P_{1}, P_{2}, P_{3}$ 均是以 $O$ 为中心的正八边形, 且 $P_{1}, P_{2}$ 的外接圆半径均为 $\sqrt{2}-\varepsilon$ ( $P_{2}$ 可以是 $P_{1}$ 的一个旋转像), $P_{3}$ 的外接圆半径为 $\varepsilon$, 其中 $\varepsilon$ 是一个充分小的正数.

现对任意 $A \in P_{1}, B \in P_{2}, C \in P_{3}$, 则

$$
C A \leq C O+O A \leq \sqrt{2}, \quad C B \leq C O+O B \leq \sqrt{2}
$$

因此 $S_{\triangle A B C} \leq \frac{A C \cdot A B}{2} \leq 1$, 且

$$
S_{P_{1}}=S_{P_{2}}=(\sqrt{2}-\varepsilon)^{2} \cdot 8 \cdot \frac{1}{2} \cdot \sin 45^{\circ}=2 \sqrt{2}(\sqrt{2}-\varepsilon)^{2}>4,\left(\text { 当 } \varepsilon \rightarrow 0^{+} \text {时 }\right) \text {. }
$$

这说明我们构造的 $P_{1}, P_{2}, P_{3}$ 满足条件且 $P_{1}, P_{2}$ 的面积均大于 4 .

组合几何中著名的 Helly 定理可叙述为: 设 $\Gamma$ 是 $\mathbb{R}^{n}$ 中的一个紧凸集族, 使得其中任意 $n+1$ 个元素的交非空, 则 $\Gamma$ 中所有元素的交非空.

Helly 定理有很多推广和变形. 问题 1 这一类型问题出现在最近的 Helly 定理的相关研究中 $([1,2])$. 下面再介绍这方面的一个有趣的结果 (这里不介绍证明).

问题 $3[2]$. 设 $P_{1}, P_{2}, \cdots, P_{k}(k \geq 2)$ 是平面上的凸多边形 (有界闭集) 使得不同集合中的任意两个点的距离不超过 1 , 则存在 $1 \leq i \leq k$ 使得 $\bigcup_{j \neq i} P_{j}$ 能被直径为 1 的三个圆的并集覆盖.

## 参考文献

[1] A.V. Akopyan, Combinatorial generalizations of Jung's Theorem [J]. Discrete Compt. Geom. 49 (2013), 478-484.

[2] J. Jerómimo-Castro, A. Magazinov, P. Soberón, On a problem by Dol'nikov [J]. Discrete Math. 338 (2015), 1577-1585.

