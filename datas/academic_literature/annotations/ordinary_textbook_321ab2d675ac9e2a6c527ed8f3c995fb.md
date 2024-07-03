# 2022 年土耳其 TST 试题解答与评析 

葛琦晖<br>(华东师范大学第二附属中学, 201203)<br>指导教师: 周建新

本文给出 2022 年土耳其 TST 试题解答与评析, 笔者认为今年的土耳其 $\mathrm{TST}$ 总体难度中等, 以简单题和中档题为主, $6 、 9$ 两题有一定难度, 问题简洁优美, 具有训练价值. 限于水平, 不当之处请各位指正.

## I. 试 题

1. 求所有素数 $p, q$, 使得 $2^{p}=2^{q-2}+q$ !.
2. 求所有函数 $f: \mathbb{Q}^{+} \rightarrow \mathbb{Q}$, 使得对任意正有理数 $x, y$, 均有

$$
f(x)+f(y)=\left(f(x+y)+\frac{1}{x+y}\right)(1-x y+f(x y)) \text {. }
$$

3. 在 $\triangle A B C$ 中, $I$ 为内心, 内切圆与 $B C, C A, A B$ 分别切于点 $D, E, F$. 设 $l$ 是过 $I$ 的一条直线, 点 $A, B, C$ 在 $l$ 上的投影为 $X, Y, Z$. 求证: $D X, E Y, F Z$三线共点.
4. 三个圆 $\omega_{1}, \omega_{2}$ 和 $\Gamma$ 在直线 $l$ 的同侧, $\omega_{1}, \omega_{2}$ 分别与 $l$ 切于点 $K, L$, 分别与 $\Gamma$ 切于 $M, N$. 已知 $\omega_{1}, \omega_{2}$ 不相交, 它们的半径也不相同. 过 $K, L$ 的圆与 $\Gamma$ 交于 $A, B$. 设 $R, S$ 是 $M, N$ 关于 $l$ 的对称点. 求证: $A, B, R, S$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_42a8375e6b418a3e86bcg-01.jpg?height=403&width=399&top_left_y=2146&top_left_x=817)

修订日期: 2022-05-07.

5. 圆周上有 2022 个点将圆周 2022 等分, 求 $k$ 的最大值使得存在 $k$ 段弧,每条弧的端点均在这 2022 个点中, 满足这 $k$ 段弧的长度互不相同且互不包含.
6. 对整系数多项式 $P(x)$ 和素数 $p$, 若不存在整数 $n$ 使得 $p \mid P(n)$, 就称 $P$排除 $p$. 是否存在一个五次整系数多项式 $P(x)$ 恰好只排除一个素数, 且没有有理根?
7. 设 $x, y, z$ 是正实数, 求

$$
x y+y z+z x+\frac{1}{x}+\frac{2}{y}+\frac{5}{z}
$$

的最小值.

8. 在 $\triangle A B C$ 中, $I$ 为内心, $A B<B C<C A$. 设三角形 $I B C, I A C, I A B$的垂心分别为 $H_{A}, H_{B}, H_{C} . H_{B} H_{C}$ 与 $B C$ 交于 $K_{A}$, 过 $I$ 作 $H_{B} H_{C}$ 的垂线, 与 $B C$ 交于 $L_{A}$, 类似定义 $K_{B}, L_{B}, K_{C}, L_{C}$. 求证: $K_{A} L_{A}=K_{B} L_{B}+K_{C} L_{C}$.
9. 求 $k$ 的最大值使得对任意一个 2022 个顶点的森林, 可以从中选出 $k$ 个顶点, 使得任意一个选出的点至多与两个选出的点相连.

## II. 解答与评注

题 1 求所有素数 $p, q$, 使得 $2^{p}=2^{q-2}+q$ !.

解 $(p, q)=(3,3),(7,5)$.

当 $q<7$ 时, 只有上述两解. 下设 $q \geq 7$, 此时 $2^{p} \equiv 2^{q-2}(\bmod 7)$, 从而 $p \equiv q-2(\bmod 3)$. 因为 $p, q$ 是大于 3 的素数, 故 $p \equiv 2(\bmod 3), q \equiv 1(\bmod 3)$.由于 $p>q-2$, 两边比较 2 的幂次得 $v_{2}(q !)=q-2$. 而

$$
v_{2}(q !)=q-q \text { 在二进制下数字和, }
$$

故 $q=2^{a}+1(q$ 是奇数 $)$, 这与 $q \equiv 1(\bmod 3)$ 矛盾.

评注 这是一道较简单的数论题, 关键在于用 $v_{2}(n !)=n-s_{2}(n)$ 得到 $q$ 是 2 的幕加 1 , 解法中同余和幂次分析都是不定方程中的常用方法.

题 2 求所有函数 $f: \mathbb{Q}^{+} \rightarrow \mathbb{Q}$, 使得对任意正有理数 $x, y$, 均有

$$
f(x)+f(y)=\left(f(x+y)+\frac{1}{x+y}\right)(1-x y+f(x y))
$$

解 将条件记为 $P(x, y)$. 由 $P(1,1)$ 得 $2 f(1)=\left(f(2)+\frac{1}{2}\right) f(1)$.

情形 $1 \quad f(1) \neq 0$, 设 $f(1)=r$, 则 $f(2)=\frac{3}{2}$.
由 $P(1,2)$ 得

$$
f(3)+\frac{1}{3}=\frac{f(1)+f(2)}{f(2)-1}=2 r+3,
$$

即 $f(3)=2 r+\frac{8}{3}$. 由 $P(1,3)$ 得

$$
f(4)+\frac{1}{4}=\frac{f(1)+f(3)}{f(3)-2}=\frac{9 r+8}{6 r+2}
$$

由 $P(2,2)$ 得

$$
\left(f(4)+\frac{1}{4}\right)(f(4)-3)=3,
$$

解得 $f(4)=-1$ 或 $\frac{15}{4}$.

若 $f(4)=\frac{15}{4}$, 则 $\frac{9 r+8}{6 r+2}=4$, 从而 $r=0$, 矛盾. 故只能 $f(4)=-1, \frac{9 r+8}{6 r+2}=-\frac{3}{4}$,

从而 $f(1)=r=-\frac{19}{27}, f(3)=\frac{34}{27}$.

由 $P(1,4)$ 得

$$
f(5)+\frac{1}{5}=\frac{f(1)+f(4)}{f(4)-3}=\frac{23}{54}
$$

即 $f(5)=\frac{61}{270}$. 由 $P(1,5)$ 得

$$
f(6)+\frac{1}{6}=\frac{f(1)+f(5)}{f(5)-4}=\frac{129}{1019} .
$$

由 $P(2,3)$ 得

$$
f(6)-5=\frac{f(2)+f(3)}{f(5)+\frac{1}{5}}>0,
$$

所以 $5<f(6)=\frac{129}{1019}-\frac{1}{6}$ 矛盾.

情形 $2 f(1)=0$, 设 $f(2)=t$. 由 $P\left(x, \frac{1}{x}\right)$ 得

$$
f(x)+f\left(\frac{1}{x}\right)=0, \quad \forall x \in \mathbb{Q}^{+}
$$

由 $P(1,2)$ 得

$$
f(3)+\frac{1}{3}=\frac{f(2)}{f(2)-1}=\frac{t}{t-1}
$$

由 $P(1,3)$ 得

$$
f(4)+\frac{1}{4}=\frac{f(3)}{f(3)-2}=\frac{2 t+1}{7-4 t}
$$

由 $P\left(\frac{1}{2}, \frac{1}{2}\right)$ 得

$$
2 f\left(\frac{1}{2}\right)=1-\frac{1}{4}+f\left(\frac{1}{4}\right),
$$

即

$$
-2 f(2)=1-\frac{1}{4}-f(4),
$$

故 $2 t=\frac{2 t+1}{7-4 t}-1$, 解得 $t=\frac{3}{2}$ 或 $-\frac{1}{2}$.
若 $f(2)=-\frac{1}{2}$, 则 $f(3)=0, f(4)=-\frac{1}{4}$.

由 $P(1,4), P(1,5)$ 依次得

$$
f(5)=-\frac{8}{65}, f(6)=\frac{2}{67}-\frac{1}{6} \text {. }
$$

由 $P(2,3)$ 得

$$
f(6)-5=\frac{f(2)+f(3)}{f(5)+\frac{1}{5}}=-\frac{13}{2}
$$

矛盾.

所以 $f(2)=\frac{3}{2}, f\left(\frac{1}{2}\right)=-\frac{3}{2}$.

设 $u, v \in \mathbb{N}^{+}$, 对 $u+v$ 归纳证明 $f\left(\frac{u}{v}\right)=\frac{u}{v}-\frac{v}{u}$.

当 $u+v=2,3$ 时结论成立, 假设结论对和较小的 $u, v$ 成立.

(1) 当 $u>v$ 时, 由 $P\left(\frac{u-v}{v}, 1\right)$ 得

$$
f\left(\frac{u-v}{v}\right)=\left(f\left(\frac{u}{v}\right)+\frac{v}{u}\right) \cdot\left(1-\frac{u-v}{v}+f\left(\frac{u-v}{v}\right)\right) .
$$

由归纳假设, $f\left(\frac{u-v}{v}\right)=\frac{u-v}{v}-\frac{v}{u-v}$. 所以

$$
\frac{u(u-2 v)}{v(u-v)}=\left(f\left(\frac{u}{v}\right)+\frac{v}{u}\right) \cdot \frac{u-2 v}{u-v} .
$$

$u \neq 2 v$ 时, 由上式得 $f\left(\frac{u}{v}\right)=\frac{u}{v}-\frac{v}{u}, u=2 v$ 时, 已证 $f(2)=\frac{3}{2}$.

(2) 当 $u<v$ 时, (1) 中已证明 $f\left(\frac{v}{u}\right)=\frac{v}{u}-\frac{u}{v}$, 又由 $f\left(\frac{u}{v}\right)+f\left(\frac{v}{u}\right)=0$, 所以 $f\left(\frac{u}{v}\right)=\frac{u}{v}-\frac{v}{u}$.

所以 $f(x)=x-\frac{1}{x}, \forall x \in \mathbb{Q}^{+}$. 此时条件

$$
\text { 右边 }=(x+y)\left(1-\frac{1}{x y}\right)=x-\frac{1}{x}+y-\frac{1}{y}=\text { 左边, }
$$

$f$ 满足条件.

综上, $f(x)=x-\frac{1}{x}, \forall x \in \mathbb{Q}^{+}$.

评注 这是一道中等难度的函数方程, 但过程较长, 大致方法是对 $f(4), f(6)$的值算两次得到关系或推出矛盾, 其中有两种情形可以用几乎相同的路线推出矛盾, 有一种情形需要通过归纳得到解, 这在有理数函数方程中是常用的.

题 3 在 $\triangle A B C$ 中, $I$ 为内心, 内切圆与 $B C, C A, A B$ 分别切于点 $D, E, F$.设 $l$ 是过 $I$ 的一条直线, 点 $A, B, C$ 在 $l$ 上的投影为 $X, Y, Z$. 求证: $D X, E Y, F Z$三线共点.

证明 在三角形 $F X D$ 中,

$$
\frac{\sin \angle F D X}{F X}=\frac{\sin \angle D F X}{D X} .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_42a8375e6b418a3e86bcg-05.jpg?height=491&width=551&top_left_y=200&top_left_x=770)

在三角形 $E X D$ 中,

$$
\frac{\sin \angle X D E}{E X}=\frac{\sin \angle D E X}{D X} .
$$

两式相除, 结合 $A, F, X, I, E$ 五点共圆, 有

$$
\frac{\sin \angle F D X}{\sin \angle X D E}=\frac{\sin \angle D F X}{\sin \angle D E X} \cdot \frac{F X}{E X}=\frac{\sin \angle D F X}{\sin \angle D E X} \cdot \frac{\sin \angle X A F}{\sin \angle X A E} .
$$

同理

$$
\begin{aligned}
& \frac{\sin \angle D E Y}{\sin \angle Y E F}=\frac{\sin \angle E D Y}{\sin \angle E F Y} \cdot \frac{\sin \angle Y B D}{\sin \angle Y B F}, \\
& \frac{\sin \angle E F Z}{\sin \angle Z F D}=\frac{\sin \angle F E Z}{\sin \angle F D Z} \cdot \frac{\sin \angle Z C E}{\sin \angle Z C D} .
\end{aligned}
$$

因为

$$
\begin{aligned}
\angle D F X+\angle E F Y & =(\angle D F A-\angle A F X)+(\angle E F B+\angle Y F B) \\
& =\angle D F A+\angle A I X+\angle E F B+\angle Y I B-180^{\circ} \\
& =\angle D F E+\angle A I B=180^{\circ},
\end{aligned}
$$

所以 $\sin \angle D F X=\sin \angle E F Y$, 同理有另外两式, 故

$$
\frac{\sin \angle D F X}{\sin \angle D E X} \cdot \frac{\sin \angle E D Y}{\sin \angle E F Y} \cdot \frac{\sin \angle F E Z}{\sin \angle F D Z}=1 .
$$

因为 $A X / / B Y$, 所以 $\sin \angle X A F=\sin \angle Y B F$, 同理有另外两式, 故

$$
\frac{\sin \angle X A F}{\sin \angle X A E} \cdot \frac{\sin \angle Y B D}{\sin \angle Y B F} \cdot \frac{\sin \angle Z C E}{\sin \angle Z C D}=1 .
$$

从而

$$
\frac{\sin \angle F D X}{\sin \angle X D E} \cdot \frac{\sin \angle D E Y}{\sin \angle Y E F} \cdot \frac{\sin \angle E F Z}{\sin \angle Z F D}=1 .
$$

在三角形 $D E F$ 中, 由角元塞瓦定理, $D X, E Y, F Z$ 三线共点.

评注 这道题作为第三题略容易, 为了利用角元塞瓦定理, 要表示出三个正弦的比, 发现分子分母可以约尽而无需计算.
题 4 三个圆 $\omega_{1}, \omega_{2}$ 和 $\Gamma$ 在直线 $l$ 的同侧, $\omega_{1}, \omega_{2}$ 分别与 $l$ 切于点 $K, L$, 分别与 $\Gamma$ 切于 $M, N$. 已知 $\omega_{1}, \omega_{2}$ 不相交, 它们的半径也不相同. 过 $K, L$ 的圆与 $\Gamma$交于 $A, B$. 设 $R, S$ 是 $M, N$ 关于 $l$ 的对称点. 求证: $A, B, R, S$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_42a8375e6b418a3e86bcg-06.jpg?height=571&width=537&top_left_y=451&top_left_x=745)

证明 设 $\omega_{1}, \Gamma$ 的内公切线与 $\omega_{2}, \Gamma$ 的内公切线交于 $P$, 则 $P M=P N$, $\angle L K M=\angle P M K, \angle K L N=\angle P N L$, 所以 $\angle L K M+\angle L N M=180^{\circ}$, 所以 $K, L, M, N$ 四点共圆.

$(A B K L),(K L N M), \Gamma$ 三圆两两根轴 $A B, K L, M N$ 交于一点 $Q$ (因为 $\omega_{1}, \omega_{2}$ 半径不同, 不可能两两平行)由对称性 $R S$ 也过 $Q$, 且 $Q R \cdot Q S=$ $Q M \cdot Q N=Q A \cdot Q B$, 所以 $A, B, R, S$ 四点共圆.

评注 这是一道简单的几何题, 本题中的 $K, L, M, N$ 是 $\omega_{1}, \omega_{2}$ 的逆对应点(与此类似的问题是 2019 年 CMO 的第 2 题), 再取出位似中心利用线段乘积相等就证明了共圆。

题 5 圆周上有 2022 个点将圆周 2022 等分, 求 $k$ 的最大值使得存在 $k$ 段弧,每条弧的端点均在这 2022 个点中, 满足这 $k$ 段弧的长度互不相同且互不包含.

解 $k$ 的最大值为 1011 .

设圆周上的 2022 个点顺时针依次为 $1,2, \cdots, 2022$, 解答中的弧 $(i, j)$ 表示 $i$ 顺时针到 $j$ 的弧. 先给出构造: 弧 $(i, 2 i), i=1,2, \cdots, 1011$ 这 1011 段弧满足条件.

下面证明满足条件的弧至多 1011 段.

设圆周上相邻两点的弧长为 1 , 假设存在 1012 段弧

$$
\left(i_{1}, j_{1}\right),\left(i_{2}, j_{2}\right), \cdots,\left(i_{1012}, j_{1012}\right)
$$

满足条件. 若这些弧的长度都大于 1 , 则 $\left(i_{1}, j_{1}-1\right), \cdots,\left(i_{1012}, j_{1012}-1\right)$ 也满足
条件, 故可不妨设有一段长为 1 的弧 $\left(i_{1012}, j_{1012}\right)=(2022,1)$, 因为这段弧不被其他弧包含, 所以其余 1011 段弧均包含于弧 $(1,2022)$. 不妨设

$$
1 \leq i_{1}<i_{2}<i_{3}<\cdots<i_{1011}<2022
$$

( $i$ 相同的两段弧必有包含关系, 所以 $i_{1}, i_{2}, \cdots, i_{1012}$ 互不相同), 则

$$
1<j_{1}<j_{2}<j_{3}<\cdots<j_{1011} \leq 2022 .
$$

因为这 1012 段弧的长度互不相同, 所以存在弧 $\left(i_{m}, j_{m}\right)$ 的长度大于 1011 , 但

$$
j_{1011} \geq j_{m}+1011-m \geq i_{m}+1012+1011-m \geq 2023
$$

矛盾.

综上, $k$ 的最大值为 1011 .

评注 这是一道中等难度的组合最值问题, 通过小情况的尝试不难猜到答案. 证明部分注意每条弧可以缩短相同长度仍满足条件, 可设存在一条长为 1 的弧, 而取出长为 1 的弧相当于将圆周“剪断成线段”, 之后结合不等式简单估计就能完成证明.

题 6 对整系数多项式 $P(x)$ 和素数 $p$, 若不存在整数 $n$ 使得 $p \mid P(n)$, 就称 $P$ 排除 $p$. 是否存在一个五次整系数多项式 $P(x)$ 恰好只排除一个素数, 且没有有理根?

解 存在, 我们证明 $P(x)=\left(x^{2}+x+1\right)\left(2 x^{3}+1\right)$ 满足条件.

显然 $P(x)$ 没有有理根且排除 2 , 下证对任意素数 $p>2$, 存在整数 $n$ 使得 $p \mid P(n)$.

当 $p=3$ 时, $3 \mid P(1)$.

当 $p \equiv 1(\bmod 3)$ 时, $\left(\frac{-3}{p}\right)=1$, 同余方程 $(2 x+1)^{2} \equiv-3(\bmod p)$ 有解, 所以存在整数 $n$ 使得 $p \mid n^{2}+n+1$.

当 $p \equiv 2(\bmod 3)$ 时, 若 $1 \leq a, b<p, a^{3} \equiv b^{3}(\bmod p)$, 由费马小定理 $a^{p-1} \equiv b^{p-1}(\bmod p)$, 从而 $a=a^{(3, p-1)} \equiv b^{(3, p-1)}=b(\bmod p)$, 所以当 $x$ 遍历模 $p$ 完系时, $x^{3}$ 也遍历模 $p$ 完系, 因此存在整数 $n$ 使得 $p \mid 2 n^{3}+1$.

综上, 我们证明了 $P(x)=\left(x^{2}+x+1\right)\left(2 x^{3}+1\right)$ 满足条件.

评注 本题先要意识到答案是存在的, 构造不唯一, 可让 $P(x)$ 是一个二次多项式与一个三次多项式并利用二次剩余中的结果.
题 7 设 $x, y, z$ 是正实数, 求

$$
x y+y z+z x+\frac{1}{x}+\frac{2}{y}+\frac{5}{z}
$$

的最小值.

解 由均值不等式:

$$
\begin{aligned}
x y+\frac{1}{3 x}+\frac{1}{2 y} & \geq 3 \sqrt[3]{\frac{1}{6}} \\
y z+\frac{3}{2 y}+\frac{3}{z} & \geq 3 \sqrt[3]{\frac{9}{2}} \\
z x+\frac{2}{3 x}+\frac{2}{z} & \geq 3 \sqrt[3]{\frac{4}{3}}
\end{aligned}
$$

三式相加, 原式 $\geq 3 \sqrt[3]{36}$. 当 $x=2 \sqrt[3]{\frac{1}{36}}, y=3 \sqrt[3]{\frac{1}{36}}, z=6 \sqrt[3]{\frac{1}{36}}$ 时等号成立.

评注 这是一道简单的代数题, 根据取等拆项利用均值不等式就能完成.

题 8 在 $\triangle A B C$ 中, $I$ 为内心, $A B<B C<C A$. 设三角形 $I B C, I A C, I A B$的垂心分别为 $H_{A}, H_{B}, H_{C} . H_{B} H_{C}$ 与 $B C$ 交于 $K_{A}$, 过 $I$ 作 $H_{B} H_{C}$ 的垂线, 与 $B C$ 交于 $L_{A}$, 类似定义 $K_{B}, L_{B}, K_{C}, L_{C}$. 求证: $K_{A} L_{A}=K_{B} L_{B}+K_{C} L_{C}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_42a8375e6b418a3e86bcg-08.jpg?height=554&width=554&top_left_y=1371&top_left_x=748)

证明 设 $\triangle A B C$ 的内切圆 $\odot I$ 与 $B C, C A, A B$ 切于 $K_{A}^{\prime}, K_{B}^{\prime}, K_{C}^{\prime}$, 则 $K_{C}^{\prime}, I, H_{C}$ 共线, $K_{B}^{\prime}, I, H_{B}$ 共线.

由 $\angle K_{C}^{\prime} B H_{C}=90^{\circ}-\frac{1}{2} \angle B A C=\angle K_{B}^{\prime} C H_{B}$, 得 $\triangle K_{C}^{\prime} B H_{C} \sim \triangle K_{B}^{\prime} C H_{B}$,故

$$
\frac{B H_{C}}{C H_{B}}=\frac{B K_{C}^{\prime}}{C K_{B}^{\prime}}=\frac{B K_{A}^{\prime}}{C K_{A}^{\prime}}
$$

因为 $B H_{C} / / C H_{B}$, 所以

$$
\frac{B K_{A}}{C K_{A}}=\frac{B H_{C}}{C H_{B}}=\frac{B K_{A}^{\prime}}{C K_{A}^{\prime}}
$$

故 $K_{A}=K_{A}^{\prime}$, 同理 $K_{B}=K_{B}^{\prime}, K_{C}=K_{C}^{\prime}$, 即 $K_{A}, K_{B}, K_{C}$ 是 $\odot I$ 与三边的切点.
再证明: $L_{A}, L_{B}, L_{C}$ 分别是 $B C, C A, A B$ 的中点.

设 $B C, C A, A B$ 的中点为 $M_{A}, M_{B}, M_{C}$, 只需证明 $I M_{A} \perp H_{B} H_{C}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_42a8375e6b418a3e86bcg-09.jpg?height=428&width=485&top_left_y=400&top_left_x=797)

设 $B I, C I$ 分别与 $K_{B} K_{C}$ 交于 $X, Y, B I$ 与 $K_{A} K_{B}$ 交于 $Z, C I$ 与 $K_{A} K_{C}$ 交于 $W$.

因为

$$
\angle B X K_{C}=\angle A K_{C} K_{B}-\angle A B I=\frac{1}{2} \angle A C B=\angle I K_{A} K_{B}
$$

所以 $I, K_{A}, X, K_{B}$ 四点共圆. 又 $I, K_{A}, C, K_{B}$ 四点共圆, 所以 $I, K_{A}, C, X, K_{B}$五点共圆, 所以 $\angle C X I=90^{\circ}, C, X, H_{A}$ 共线. 从而 $\angle M_{A} X B=\angle M_{A} B X=$ $\angle A B X$, 所以 $M_{A} X / / A B, X$ 在 $M_{A} M_{B}$ 上.

同理, $B, Y, H_{A}$ 共线, $W, Z$ 均在 $M_{B} M_{C}$ 上.

因为 $C$ 关于 $\odot I$ 的极线过 $Z$, 所以 $Z$ 关于 $\odot I$ 的极线过 $C$, 又 $C X \perp Z I$, 所以 $Z$ 的极线为 $C X$ (过 $H_{A}$ ). 同理, $W$ 的极线为 $B Y$ (过 $H_{A}$ ). 故 $H_{A}$ 的极线为 $Z W$, 也为 $M_{B} M_{C}$. 同理 $H_{B}$ 的极线为 $M_{A} M_{C}, H_{C}$ 的极线为 $M_{A} M_{B}$. 所以 $M_{A}$ 的极线为 $H_{B} H_{C}$, 从而 $I M_{A} \perp H_{B} H_{C},(*)$ 得证.

因为 $A B<B C<C A$, 所以

$$
K_{A} L_{A}=\frac{A C-A B}{2}, K_{B} L_{B}=\frac{B C-A B}{2}, K_{C} L_{C}=\frac{A C-B C}{2} .
$$

因此 $K_{A} L_{A}=K_{B} L_{B}+K_{C} L_{C}$.

评注 这是一个中等难度的几何题, 关键在于给出 $K_{A}, L_{A}$ 的刻划, 主要难点是 $I M_{A} \perp H_{B} H_{C}$ 的证明, 这里将内心的常用结构添出后利用配极证明了 $M_{A}$关于 $\odot I$ 的极线为 $H_{B} H_{C}$. 本题中 $I M_{A} \perp H_{B} H_{C}$ 的结论可用于证明如下的 2005 年全俄数学奥林匹克十年级第 4 题:

$w_{B}, w_{C}$ 是 $\triangle A B C$ 的 $B-$ 旁切圆和 $C-$ 旁切圆, $w_{B}^{\prime}$ 是 $w_{B}$ 关于 $A C$ 中点对称得到的圆, $w_{C}^{\prime}$ 是 $w_{C}$ 关于 $A B$ 中点对称得到的圆. 求证: $w_{B}^{\prime}$ 与 $w_{C}^{\prime}$ 的根轴平分 $\triangle A B C$ 的周长.

注意 $A$ 在 $w_{B}^{\prime}$ 与 $w_{C}^{\prime}$ 的根轴上及 $w_{B}^{\prime}, w_{C}^{\prime}$ 的圆心分别是 $H_{B}$ 和 $H_{C}$.
题 9 求 $k$ 的最大值使得对任意一个 2022 个顶点的森林, 可以从中选出 $k$ 个顶点, 使得任意一个选出的点至多与两个选出的点相连.

解 $k$ 的最大值是 1517 .

取 505 个 4 个点的星状树和 2 个孤立点, 注意到每个星状树中至多选 3 个顶点, 所以整个森林至多选 $505 \times 3+2=1517$ 个点.

另一方面, 我们对 $n$ 归纳证明: 任意一个 $n$ 个顶点的森林可以选出 $\left\lceil\frac{3 n}{4}\right\rceil$ 个顶点使得任意一个选出的点至多与两个选出的点相连.

$n=1,2,3,4$ 时结论成立, 假设结论对较小的 $n$ 成立, 考虑 $n$ 的情形, 只需对 $n$ 个顶点的树 $T$ 证明. 若 $T$ 中每个顶点的度不超过 2 , 则 $T$ 中所有顶点均可选出.

下设 $T$ 中存在一个点 $v$ 的度 $\geq 3$, 将 $v$ 删去后各连通分支有 $n_{1}, n_{2}, \cdots, n_{k}$ $(k \geq 3)$ 个点, $n_{1}+n_{2}+\cdots+n_{k}=n-1$.

情形 $1 n_{1}, n_{2}, \cdots, n_{k}$ 均不是 4 的倍数.

由归纳假设, 可以在删去 $v$ 后的 $k$ 个树中各取 $\left\lceil\frac{3 n_{1}}{4}\right\rceil,\left\lceil\frac{3 n_{2}}{4}\right\rceil, \cdots,\left\lceil\frac{\left.3 n_{k}\right\rceil}{4}\right\rceil$ 个点满足要求, 从而 $T$ 中可选取 $\left\lceil\frac{3 n_{1}}{4}\right\rceil+\left\lceil\frac{3 n_{2}}{4}\right\rceil+\cdots+\left\lceil\frac{3 n_{k}}{4}\right\rceil$ 个点满足要求.

设 $n_{i}=4 q_{i}+r_{i}, r_{i} \in\{1,2,3\}, q_{i} \in \mathbb{N}$, 则

$$
\begin{aligned}
\left\lceil\frac{3 n_{1}}{4}\right\rceil+\cdots+\left\lceil\frac{3 n_{k}}{4}\right\rceil & =3\left(q_{1}+\cdots+q_{k}\right)+\left\lceil\frac{3 r_{1}}{4}\right\rceil+\cdots+\left\lceil\frac{3 r_{k}}{4}\right\rceil \\
& =3\left(q_{1}+\cdots+q_{k}\right)+r_{1}+\cdots+r_{k} \\
& =\frac{3(n-1)}{4}+\frac{1}{4}\left(r_{1}+\cdots+r_{k}\right) \\
& \geq \frac{3 n-3}{4}+\frac{k}{4} \geq \frac{3 n}{4} .
\end{aligned}
$$

故

$$
\left\lceil\frac{3 n_{1}}{4}\right\rceil+\left\lceil\frac{3 n_{2}}{4}\right\rceil+\cdots+\left\lceil\frac{3 n_{k}}{4}\right\rceil \geq\left\lceil\frac{3 n}{4}\right\rceil .
$$

情形 $2 n_{1}, n_{2}, \cdots, n_{k}$ 中有 4 的倍数, 不妨设 $4 \mid n_{1}$.

设 $n_{1}$ 对应的连通分支中 $u$ 与 $v$ 相连, $T$ 中删去 $u$ 剩下的连通分支各有 $m_{1}, m_{2}, \cdots, m_{l}, a$ 个点, 其中 $a=n_{2}+\cdots+n_{k}+1, m_{1}+\cdots+m_{l}=n_{1}-1$.

由归纳假设, 可以在删去 $u$ 后的 $l+1$ 个树中各取 $\left\lceil\frac{3 m_{1}}{4}\right\rceil, \cdots,\left\lceil\frac{3 m_{l}}{4}\right\rceil,\left\lceil\frac{3 a}{4}\right\rceil$个点满足要求, 从而 $T$ 中可选取 $\left\lceil\frac{3 m_{1}}{4}\right\rceil+\cdots+\left\lceil\frac{3 m_{l}}{4}\right\rceil+\left\lceil\frac{3 a}{4}\right\rceil$ 个点满足要求.

设 $m_{i}=4 q_{i}^{\prime}+r_{i}^{\prime}, r_{i}^{\prime} \in\{0,1,2,3\}, q_{i}^{\prime} \in \mathbb{N}$, 则 $4 \mid r_{1}^{\prime}+\cdots+r_{l}^{\prime}+1$, 故 $r_{1}^{\prime}+\cdots+r_{l}^{\prime} \geq 3$. 从而

$$
\left\lceil\frac{3 m_{1}}{4}\right\rceil+\cdots+\left\lceil\frac{3 m_{l}}{4}\right\rceil+\left\lceil\frac{3 a}{4}\right\rceil \geq 3\left(q_{1}^{\prime}+\cdots+q_{l}^{\prime}\right)+r_{1}^{\prime}+\cdots+r_{l}^{\prime}+\frac{3 a}{4}
$$

$$
\begin{aligned}
& =\frac{3(n-1)}{4}+\frac{1}{4}\left(r_{1}^{\prime}+\cdots+r_{l}^{\prime}\right) \\
& \geq \frac{3 n}{4},
\end{aligned}
$$

故

$$
\left\lceil\frac{3 m_{1}}{4}\right\rceil+\cdots+\left\lceil\frac{3 m_{l}}{4}\right\rceil+\left\lceil\frac{3 a}{4}\right\rceil \geq\left\lceil\frac{3 n}{4}\right\rceil
$$

$T$ 中总可选出 $\left\lceil\frac{3 n}{4}\right\rceil$ 个点满足要求.

综上, $k$ 的最大值为 1517 .

评注 本题的证明部分利用归纳法删去一个点并对剩下的树使用归纳假设,难点在于删去合适的点使 $\left\lceil\frac{3 n_{i}}{4}\right\rceil$ 之和不小于 $\left\lceil\frac{3 n}{4}\right\rceil$, 这与 $n_{i}$ 和 $n$ 模 4 余数有关, 需要分两种情形讨论.

