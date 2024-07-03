# 预给径向半径的凸多边形内径问题 

朱天明 吴雨桐

(北京大学数学科学学院 2019 级, 100871)

今年二月的哈佛一麻省 (HMMT) 数学竞赛中有这样一个问题:

问题 1 一个平面上的凸多边形叫做 “宽的”, 如果它在任意直线上投影的长度均不小于 1. 证明: 任一“宽的”的凸多边形都包含一个半径为 $\frac{1}{3}$ 的圆.

冷岗松教授提出一个对偶问题, 称作为预给径向半径的凸多边形内径问题:

问题 2 如果一个凸多边形内存在一点, 过该点的任意直线与凸多边形相交形成的截线段的长度均不小于 1 . 问这个凸多边形能包含一个多大的圆?

本文解决了这个问题, 即证明了如下定理:

定理 如果一个平面上的凸多边形内存在一点, 过该点的任意直线与凸多边形相交形成的截线段的长度均不小于 1 , 则该凸多边形能包含一个半径为 $\frac{\sqrt{3}}{4}$ 的圆.

先证明下面两个引理.

引理 $\mathbf{1}$ 对 $x, y, z \in\left(0, \frac{\pi}{2}\right), x+y+z=\pi$, 有以下不等式成立:

$$
\sum_{\text {cyc }}\left(\frac{\sin ^{2} x}{\cos x}-\frac{\sqrt{3}}{2} \tan x\right) \geq 0
$$

证明 考虑函数

$$
f(x)=\frac{\sin ^{2} x}{\cos x}-\frac{\sqrt{3}}{2} \tan x,
$$

则

$$
f^{\prime \prime}(x)=\frac{1+\sin ^{2} x+\cos ^{4} x-\sqrt{3} \sin x}{\cos ^{3} x} \geq 0, x \in\left(0, \frac{\pi}{2}\right),
$$

修订日期: 2019-12-08.
从而由琴生不等式:

$$
f(x)+f(y)+f(z) \geq 3 f\left(\frac{x+y+z}{3}\right)=3 f\left(\frac{\pi}{3}\right)=0,
$$

即证.

引理 2 如果一个平面上的 $\triangle A B C$ 内 (不含边界)存在一点 $K$, 过 $K$ 的任意直线与 $\triangle A B C$ 相交形成的截线段的长度均不小于 1 , 则该三角形内切圆半径 $r$至少为 $\frac{\sqrt{3}}{4}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_df0b2cbc3746037ce964g-2.jpg?height=417&width=479&top_left_y=748&top_left_x=797)

证明 过点 $K$ 作 $\angle B A C$ 的角平分线的垂线分别交直线 $A B, A C$ 于点 $P, Q$,类似定义 $R, S, T, U$. 则无论这些点位置如何, 均有 $P Q \geq 1, R S \geq 1, T U \geq 1$.我们有:

$$
K E+K F=\cos \frac{A}{2}(K Q+K P)=P Q \cos \frac{A}{2}
$$

同理有

$$
K F+K D=R S \cos \frac{B}{2}, K D+K E=T U \cos \frac{C}{2} .
$$

从而我们可知

$$
K D=\frac{1}{2}\left(R S \cos \frac{B}{2}+T U \cos \frac{C}{2}-P Q \cos \frac{A}{2}\right) .
$$

同理有另外两式, 于是

$$
\begin{aligned}
r & =\frac{2 S_{\triangle A B C}}{a+b+c}=\frac{2\left(S_{\triangle A K B}+S_{\triangle B K C}+S_{\triangle C K A}\right)}{a+b+c}=\frac{a K D+b K E+c K F}{a+b+c} \\
& =\frac{P Q \cos \frac{A}{2}(b+c-a)+R S \cos \frac{B}{2}(c+a-b)+T U \cos \frac{C}{2}(a+b-c)}{2(a+b+c)} \\
& \geq \frac{\cos \frac{A}{2}(b+c-a)+\cos \frac{B}{2}(c+a-b)+\cos \frac{C}{2}(a+b-c)}{2(a+b+c)}
\end{aligned}
$$

从而只需证明:

$$
\sum_{\mathrm{cyc}} \cos \frac{A}{2}(b+c-a) \geq \frac{\sqrt{3}}{2} \sum_{\mathrm{cyc}}(b+c-a)
$$

$$
\sum_{\mathrm{cyc}} \cos \frac{A}{2}\left(\frac{b+c-a}{2 r}\right)-\frac{\sqrt{3}}{2} \sum_{\mathrm{cyc}} \frac{b+c-a}{2 r}=\sum_{\mathrm{cyc}}\left(\frac{\cos ^{2} \frac{A}{2}}{\sin \frac{A}{2}}-\frac{\sqrt{3}}{2} \cot \frac{A}{2}\right) \geq 0
$$

在引理 1 中令

$$
x=\frac{\pi-A}{2}, y=\frac{\pi-B}{2}, z=\frac{\pi-C}{2}
$$

知最后一个不等式成立, 即证.

定理证明 考虑所有和该多边形至少三条边相切, 且在多边形内部的圆的集合 $C$.

首先说明 $C$ 非空. 对该凸多边形的任意两条边, 考虑所有与这两条边相切的圆构成的圆系, 则由凸性和连续性知, 该圆系中必有一个圆和除此两条边以外的第三条边相切, 从而 $C$ 非空.

由于从该多边形的边集中选三条边的方法数有限, 故 $C$ 有限. 取 $C$ 中面积最大(或之一)的圆 $\Gamma$, 考虑与它相切的边与 $\Gamma$ 的切点集 $T$. 若 $T$ 中任三点构成钝角三角形, 考虑 $T$ 分 $\Gamma$ 的弧中最长(或之一)的弧 $M N$, 若该弧为劣弧, 则 $M, N$关于 $\Gamma$ 的对径点 M.N. 构成的劣弧上必没有 $T$ 中的点, 则 $T$ 分 $\Gamma$ 的弧中必有一条包含 M.N., 这是更长的弧, 矛盾. 从而所有 $T$ 中的点都在 $\Gamma$ 某条直径的一侧,故可以将该圆的圆心向一侧稍移动, 再将半径稍增加, 直至与多边形的某条边 $k$相切. 再将圆心沿直线 $k$ 所在的方向平移, 半径保持不变, 直到与另一条边相切.用和说明 $C$ 非空同样的办法, 可知存在一个比 $\Gamma$ 更大的 $C$ 中的圆, 矛盾. 进而 $T$中必有三个点构成非针角三角形.

若此三个点构成直角三角形, 则存在两条直线 $p, q$, 满足 $p / / q$, 且 $p, q$ 和 $\Gamma$相切, 由多边形的凸性可知该多边形位于 $p, q$ 构成的带形中. 从而考虑垂直于 $p$的截线段, 可知

$$
r \geq \frac{1}{2}>\frac{\sqrt{3}}{4} .
$$

若此三点构成锐角三角形, 则 $\Gamma$ 在此三点的切线交出一个三角形, 由凸性可知该凸多边形在此三角形内部, $\Gamma$ 为此三角形的内切圆, 而此三角形满足引理 2 的条件, 即证.

显然, $\frac{\sqrt{3}}{4}$ 是最优的.

