数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年捷克一斯洛伐克一波兰一奥地利联合竞赛试题解答与评析 

陈铭意 温玟杰 刘家瑜

(湖南省长沙市雅礼中学, 410007)

指导教师: 申东

本年度试题简洁优美, 难度比 2020 年度的试题稍低. 1, 2, 4, 5 属基础题, 与全国高中数学联赛 1,2 题难度相当, 6 属于中档题, 与联赛第 3 题难度相当, 3 属于较难题, 与联赛第 4 题的难度相当.

## I. 试 题

1. 求所有的四元正整数组 $(a, b, c, d)$, 使得

$$
\operatorname{gcd}(a, b, c, d)=1 \text {, 且 } a|b+c, b| c+d, c|d+a, d| a+b \text {. }
$$

2. 锐角 $\triangle A B C$ 中, 内切圆 $\omega$ 与边 $B C$ 切于点 $D$, 设 $I_{a}$ 表示角 $A$ 所对的旁心, $M$ 为 $D I_{a}$ 的中点. 求证: $\triangle B M C$ 的外接圆与圆 $\omega$ 相切.
3. 对两个顶点互不相同的凸多边形 $P_{1}$ 和 $P_{2}$, 记它们位于对方的边上的顶点总数为 $f\left(P_{1}, P_{2}\right)$. 对 $n \geq 4$, 求 $\max \left\{f\left(P_{1}, P_{2}\right) \mid P_{1}\right.$ 与 $P_{2}$ 为凸 $n$ 边形 $\}$.
4. 求满足以下条件的 2021 元正整数组的个数: 3 为其中一项, 且任意相邻两项的差的绝对值不超过 1.
5. 数列 $\left\{a_{n}\right\}$ 满足:

$$
a_{1}=1, a_{n}=\left\{\begin{array}{l}
a_{n-1}+3, n-1 \in\left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\} \\
a_{n-1}+2, n-1 \notin\left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\}
\end{array}, n \geq 2\right.
$$

证明: 对任意正整数 $n$, 均有 $a_{n}<(\sqrt{2}+1) n$.

6. 锐角 $\triangle A B C$ 中, 点 $A, A_{b}, B_{a}, B, B_{c}, C_{b}, C, C_{a}, A_{c}$ 按顺序分布在其三条修订日期: 2021-08-17.
边上. 设 $\odot A A_{b} C_{a}$ 与 $\odot A A_{c} B_{a}$ 交于另一点 $A_{1}\left(A_{1} \neq A\right)$, 并类似定义 $B_{1}, C_{1}$. 已知 $A_{1}, B_{1}, C_{1}$ 这三个点互异且不共线. 证明: 直线 $A A_{1}, B B_{1}, C C_{1}$ 过同一个点,且该点在 $\triangle A_{1} B_{1} C_{1}$ 的外接圆上.

## II . 解答与评注

1. 求所有的四元正整数组 $(a, b, c, d)$, 使得

$$
\operatorname{gcd}(a, b, c, d)=1 \text {, 且 } a|b+c, b| c+d, c|d+a, d| a+b \text {. }
$$

解 (温玟杰) 不妨设 $a=\max \{a, b, c, d\}$, 则 $b+c \leq 2 a$, 由 $a \mid b+c$ 可得 $b+c=2 a$ 或 $a$.

(1) 当 $b+c=2 a$ 时, 有 $b=c=a \geq d$, 由 $b|c+d \Rightarrow a| d \Rightarrow a \leq d$, 所以, $a=d$, 又 $\operatorname{gcd}(a, b, c, d)=1$, 得 $(a, b, c, d)=(1,1,1,1)$ 满足条件.

(2) 当 $b+c=a$ 时, 有 $b|c+d, c| b+d$, (1) 及 $d \mid 2 b+c$.

若 $(b, c) \neq 1$, 则存在素数 $p$, 使得 $p \mid b$, 且 $p \mid c$, 有 $p \mid a$, 又由 (1) $\Rightarrow p \mid d$, 即有 $p \mid \operatorname{gcd}(a, b, c, d)$, 这与 $\operatorname{gcd}(a, b, c, d)=1$ 矛盾, 故有 $(b, c)=1$. 又由 (1) 可得, $b|b+c+d, c| b+c+d$, 于是, $b c \mid b+c+d$. (3)

下面分三类讨论:

$1^{\circ}$. 当 $c=1$ 时, 由 (1), (2) 得, $b|1+d, d| 2 b+1$. (4)于是,

若 $b=1$, 则 $d \mid 3$, 又 $d \leq a=2$, 故 $d=1$, 得 $(a, b, c, d)=(2,1,1,1)$ ；

若 $b=2$, 则 $d \mid 5$, 又 $d \leq a=3$, 故 $d=1$, 得 $(a, b, c, d)=(3,2,1,1)$ ；

若 $b \geq 3$, 则 $d \leq a=b+1<2 b-1$, 故由 (4) 知, $d=b-1, b-1 \mid 2 b+1$, 因此 $b-1 \mid 3$, 故 $b=4, d=3$, 得 $(a, b, c, d)=(5,4,1,3)$.

$2^{\circ}$. 当 $c \geq 2$ 且 $b=1$ 时, 由 (1), (2) 得, $c|1+d, d| c+2$. (5)于是,

若 $c=2$, 则 $2|d+1, d| 4$, 又 $d \leq a=3$, 故 $d=1$, 得 $(a, b, c, d)=(3,1,2,1)$;

若 $c \geq 3$, 则 $d \leq a=c+1<2 c-1$, 故由 (5) 知, $d=c-1, c-1 \| c+2$, 因此 $c-1 \mid 3$, 故 $c=4, d=3$, 得 $(a, b, c, d)=(5,1,4,3)$.

$3^{\circ}$. 当 $b \geq 2$ 且 $c \geq 2$ 时, 若 $b=c=2$, 则由 (2), (3) 得, $4 \mid d$ 且 $d \mid 6$, 矛盾! 故 $b, c$ 不全为 2 , 又 $d \leq a=b+c<2 b c-b-c(\because b c>b+c \Leftrightarrow(b-1)(c-1)>1)$,故由 (2), (3) 得, $d=b c-b-c, b c-b-c \mid 2 b+c$. (6) 又由 $d=b c-b-c \leq a=b+c$得, $(b-2)(c-2) \leq 4$. (7), 于是:

若 $b=2$, 则由 (6) 知, $c-2|c+4 \Rightarrow c-2| 6$, 结合 $(b, c)=1$, 得 $c=3$ 或 5 ,从而, $(a, b, c, d)=(5,2,3,1)$ 或 $(7,2,5,3)$;
若 $c=2$, 则由 (6) 知, $b-2|2 b+2 \Rightarrow b-2| 6$, 同上得 $b=3$ 或 5 , 从而, $(a, b, c, d)=(5,3,2,1)$ 或 $(7,5,2,3)$ ；

若 $b \geq 3$ 且 $c \geq 3$, 由 (7) 可知, $3 \leq b, c \leq 6$, 又 $b \neq c(\because(b, c)=1)$, 所以 $b, c$ 中必有一个为 3 (否则 $(b-2)(c-2) \geq 2 \times 3>4$ ), 枚举可知, 只有 $(a, b, c, d)=(7,3,4,5)$, 满足条件.

综上, 满足条件的四元正整数组 $(a, b, c, d)=(1,1,1,1),(2,1,1,1),(3,2,1,1)$, $(5,4,1,3),(3,1,2,1),(5,1,4,3),(5,2,3,1),(7,2,5,3),(5,3,2,1),(7,5,2,3),(7,3,4,5)$及其轮换.

评注 对整除的轮换对称式求解, 我们常常借助于有界性和分类讨论. 本题入手不难, 分类的切入点也不尽不同, 需要细致, 避免漏解.

2. 锐角 $\triangle A B C$ 中, 内切圆 $\omega$ 与边 $B C$ 切于点 $D$, 设 $I_{a}$ 表示角 $A$ 所对的旁心, $M$ 为 $D I_{a}$ 的中点. 求证: $\triangle B M C$ 的外接圆与圆 $\omega$ 相切.

![](https://cdn.mathpix.com/cropped/2024_02_26_aa3bbb06f0436b073061g-03.jpg?height=848&width=556&top_left_y=1232&top_left_x=750)

证明 (陈铭意) 设 $\triangle A B C$ 内心为 $I, M D$ 的延长线交圆 $\omega$ 于另一点 $T$, 记 $T D$ 的中点为 $N$. 则有

$$
\angle I N I_{a}=\angle I B I_{a}=\angle I C I_{a}=90^{\circ} .
$$

从而 $I, N, B, I_{a}, C$ 五点共圆.

于是, 由圆幂定理得:

$$
B D \cdot D C=N D \cdot D I_{a}=2 N D \cdot D M=T D \cdot D M \text {. }
$$

从而 $T, B, M, C$ 四点共圆.

设 $I_{a}$ 在 $B C$ 边上的射影为点 $D_{1}$, 则 $D_{1} M=\frac{1}{2} D I_{a}=D M$, 即 $M$ 在 $D D_{1}$ 中垂线上. 又注意到 $B D=C D_{1}$, 可得 $M$ 在 $B C$ 中垂线上, 所以 $B M=C M$.(2)

如图, 过 $T$ 作圆 $\omega$ 切线 $T P$, 则

$$
\begin{aligned}
\angle P T B & =\angle P T D-\angle B T D \\
& =\angle B D T-\angle B T D \quad(\because T P, D B \text { 均为圆 } \omega \text { 的切线 }) \\
& =\angle B D T-\angle C T D \quad(1),(2) \Rightarrow T M \text { 平分 } \angle B T C) \\
& =\angle T C B .
\end{aligned}
$$

因此 $P T$ 与 $\odot(T B M C)$ 切于点 $T$, 即 $P T$ 为 $\odot(T B M C)$ 与圆 $\omega$ 的公切线. 故 $\triangle B M C$ 的外接圆与圆 $\omega$ 相切. 证毕.

评注 处理两圆相切的问题, 我们常常需要借助切点. 本题的证明方法自然且具有一定的普适性, 先在圆 $\omega$ 上确定点 $T$, 再证明 $T$ 也在 $\triangle B M C$ 的外接圆上, 最后证明 $P T$ 为两圆的公切线 (事实上, 亦可证明两圆的圆心与切点共线).

3. 对两个顶点互不相同的凸多边形 $P_{1}$ 和 $P_{2}$, 记它们位于对方的边上的顶点总数为 $f\left(P_{1}, P_{2}\right)$. 对 $n \geq 4$, 求 $\max \left\{f\left(P_{1}, P_{2}\right) \mid P_{1}\right.$ 与 $P_{2}$ 为凸 $n$ 边形 $\}$.

解 (刘家瑜) 对两个顶点互不相同的凸多边形 $P_{1}$ 和 $P_{2}$, 我们有如下两个断言.

断言 1 若凸多边形 $P_{i}(i=1$ 或 2$)$ 一边 $X_{t} X_{t+1}$ 上有两个顶点 $Y_{j}, Y_{s}$ 属于 $P_{3-i}$, 则顶点 $X_{t}, X_{t+1}$ 均不在 $P_{3-i}$ 的边上.

断言 2 若凸多边形 $P_{i}(i=1$ 或 2$)$ 一边 $X_{t} X_{t+1}$ 上有 1 个顶点 $Y_{s}$ 属于 $P_{3-i}$,则顶点 $X_{t}, X_{t+1}$ 不都在 $P_{3-i}$ 的边上.

断言 1 证明 若 $X_{t}$ 在 $P_{3-i}$ 的边 $Y_{m} Y_{m+1}$ 上, 注意到凸多边形中不存在三个顶点共线, 且 $Y_{j}, Y_{s}$ 为边 $X_{t} X_{t+1}$ 上的内点 (不含端点, 因 $P_{1}$ 和 $P_{2}$ 无公共顶点),故 $Y_{m}, Y_{m+1}, Y_{j}, Y_{s}$ 互不相同, 且无任何 3 点共线 (如图 3-1), 则 $Y_{m}, Y_{m+1}, Y_{j}, Y_{s}$不构成凸集, 矛盾 (任取凸多边形若干个顶点都构成凸集). 所以, $X_{t}$ 不在 $P_{3-i}$的边上. 同理, $X_{t+1}$ 也不在 $P_{3-i}$ 的边上. 断言 1 证毕.

断言 2 证明 假设点 $X_{t}, X_{t+1}$ 都在 $P_{3-i}$ 的边上, 注意到凸多边形中不存在三个顶点共线, 且 $Y_{s}$ 为边 $X_{t} X_{t+1}$ 上的内点 (不含端点), 故 $X_{t}, X_{t+1}$ 不可能都在 $P_{3-i}$ 的同一边上, 不妨设 $X_{t}$ 在边 $Y_{m} Y_{m+1}$ 上, $X_{t+1}$ 在边 $Y_{l} Y_{l+1}$ 上.

若 $Y_{s} \in\left\{Y_{m}, Y_{m+1}, Y_{l}, Y_{l+1}\right\}$, 不妨设 $Y_{s}=Y_{l}$, 此时, $Y_{m}, Y_{m+1}, Y_{l}, Y_{l+1}$ 互不相
同, 且 $Y_{m}, Y_{m+1}$ 均不在直线 $X_{t} X_{t+1}$ 上 (如图 3-2), 则 $Y_{m}, Y_{m+1}, Y_{l}, Y_{l+1}$ 不构成凸集, 矛盾.

若 $Y_{s}$ 与 $Y_{m}, Y_{m+1}, Y_{l}, Y_{l+1}$ 均不同, 则这 4 个点均不在直线 $X_{t} X_{t+1}$ 上 (凸多边形中不存在三个顶点共线), (如图 3-3), 可得 $Y_{s}, Y_{m}, Y_{m+1}, Y_{l}, Y_{l+1}$ 不构成凸集, 也矛盾. (边 $Y_{m} Y_{m+1}$ 与边 $Y_{l} Y_{l+1}$ 可能有一个顶点公共, 如 $Y_{m+1}=Y_{l}$, 同样得矛盾)

综上, 假设不成立, 断言 2 证毕.

![](https://cdn.mathpix.com/cropped/2024_02_26_aa3bbb06f0436b073061g-05.jpg?height=303&width=365&top_left_y=774&top_left_x=366)

图 3-1

![](https://cdn.mathpix.com/cropped/2024_02_26_aa3bbb06f0436b073061g-05.jpg?height=303&width=354&top_left_y=774&top_left_x=814)

图 3-2

![](https://cdn.mathpix.com/cropped/2024_02_26_aa3bbb06f0436b073061g-05.jpg?height=300&width=357&top_left_y=775&top_left_x=1249)

图 3-3

回到原题.

设凸多边形 $A_{1} A_{2} \cdots A_{n}$ 为 $P_{1}$, 凸多边形 $B_{1} B_{2} \cdots B_{n}$ 为 $P_{2}$.

我们定义：

$$
S_{1}\left(A_{i}\right)=\left\{\begin{array}{l}
1, A_{i} \text { 位于 } P_{2} \text { 边上 }, \\
0, \text { 否则 }
\end{array},\right.
$$

$T_{1}\left(A_{i} A_{i+1}\right)=\mid\left\{B_{j} \mid B_{j}\right.$ 位于 $A_{i} A_{i+1}$ 边上 $\} \mid\left(1 \leq i \leq n, A_{n+1}=A_{1}\right)$.

类似定义 $S_{2}\left(B_{i}\right), T_{2}\left(B_{i} B_{i+1}\right)$.

则由上述两个断言可知, 对任意 $1 \leq i \leq n$, 均有

$$
S_{1}\left(A_{i}\right)+S_{1}\left(A_{i+1}\right)+T_{1}\left(A_{i} A_{i+1}\right) \leq 2, S_{2}\left(B_{i}\right)+S_{2}\left(B_{i+1}\right)+T_{2}\left(B_{i} B_{i+1}\right) \leq 2
$$

其中 $A_{n+1}=A_{1}, B_{n+1}=B_{1}$.

又有, $P_{1}$ 位于 $P_{2}$ 边上的顶点总数

$$
N_{1}=\sum_{i=1}^{n} S_{1}\left(A_{i}\right)=\sum_{i=1}^{n} T_{2}\left(B_{i} B_{i+1}\right)
$$

$P_{2}$ 位于 $P_{1}$ 边上的顶点总数

$$
N_{2}=\sum_{i=1}^{n} S_{2}\left(B_{i}\right)=\sum_{i=1}^{n} T_{1}\left(A_{i} A_{i+1}\right)
$$

于是 $f\left(P_{1}, P_{2}\right)=N_{1}+N_{2}$. 不妨设 $N_{1} \leq N_{2}$, 则

$$
2 f\left(P_{1}, P_{2}\right)=\sum_{i=1}^{n} S_{1}\left(A_{i}\right)+\sum_{i=1}^{n} T_{2}\left(B_{i} B_{i+1}\right)+2 \sum_{i=1}^{n} S_{2}\left(B_{i}\right)
$$

$$
\begin{aligned}
& =\sum_{i=1}^{n} S_{1}\left(A_{i}\right)+\left(\sum_{i=1}^{n} S_{2}\left(B_{i}\right)+\sum_{i=1}^{n} S_{2}\left(B_{i+1}\right)+\sum_{i=1}^{n} T_{2}\left(B_{i} B_{i+1}\right)\right) \\
& \leq \frac{f\left(P_{1}, P_{2}\right)}{2}+\sum_{i=1}^{n}\left(S_{2}\left(B_{i}\right)+S_{2}\left(B_{i+1}\right)+T_{2}\left(B_{i} B_{i+1}\right)\right) \\
& \leq \frac{f\left(P_{1}, P_{2}\right)}{2}+2 n \\
& \leq \frac{4 n}{3}, \text { 又 } f\left(P_{1}, P_{2}\right) \in \mathbb{N}, \text { 于是 } \\
& \qquad \quad f\left(P_{1}, P_{2}\right) \leq\left[\frac{4 n}{3}\right] .
\end{aligned}
$$

$$
\Rightarrow f\left(P_{1}, P_{2}\right) \leq \frac{4 n}{3} \text {, 又 } f\left(P_{1}, P_{2}\right) \in \mathbb{N} \text {, 于是 }
$$

下面给出 $f\left(P_{1}, P_{2}\right)=\left[\frac{4 n}{3}\right](n \geq 4)$ 的构造. 我们分三类讨论.

(1) 当 $n=3 t+1\left(t \in \mathbb{N}_{+}\right)$时, 考虑正 $(4 t+1)$ 边形 $X_{1} X_{2} Y_{1} Y_{2} X_{3} X_{4} \cdots X_{2 t-1} X_{2 t}$ $Y_{2 t-1} Y_{2 t} X_{2 t+1}$, 设直线 $X_{2 i} Y_{2 i-1}, X_{2 i+1} Y_{2 i}$ 交点为 $X_{2 t+1+i}(1 \leq i \leq t)$, 直线 $Y_{2 j} X_{2 j+1}, X_{2 j+2} Y_{2 j+1}$ 交点为 $B_{2 t+j}(1 \leq j \leq t-1)$, 设过点 $X_{1}$ 且与 $X_{2} X_{2 t+1}$ 平行的直线为 $l_{0}$, 直线 $Y_{2 t} X_{2 t+1}$ 交 $l_{0}$ 于点 $Y_{3 t}$, 直线 $Y_{1} X_{2}$ 交 $l_{0}$ 于点 $Y_{3 t+1}$, 记多边形 $X_{1} X_{2} X_{2 t+2} X_{3} X_{4} X_{2 t+3} \cdots X_{2 t-1} X_{2 t} X_{3 t+1} X_{2 t+1}$ 为 $P_{1}$, 多边形 $Y_{1} Y_{2} Y_{2 t+1} Y_{3} Y_{4} Y_{2 t+2}$ $\cdots Y_{2 t-1} Y_{2 t} Y_{3 t} Y_{3 t+1}$ 为 $P_{2}$, 可得

$$
f\left(P_{1}, P_{2}\right)=4 t+1=\left[\frac{4 n}{3}\right]
$$

其中 $X_{1}, X_{2}, \cdots, X_{2 t+1}$ 均位于 $P_{2}$ 的边上, $Y_{1}, Y_{2}, \cdots, Y_{2 t}$ 均位于 $P_{1}$ 的边上.

(2) 当 $n=3 t-1(t \geq 2)$ 时, 在 (1) 的情形下, 将边 $X_{1} X_{2}, X_{1} X_{2 t+1}$ 收缩成一个点 $X_{1}$ (有 $X_{2}=X_{2 t+1}=X_{1}, Y_{3 t}, Y_{3 t+1}$ 不再存在), 其它所有点的相对位置不变. 则 $P_{1}$ 为多边形 $X_{1}\left(X_{2}\right) X_{2 t+2} X_{3} X_{4} X_{2 t+3} \cdots X_{2 t-1} X_{2 t} X_{3 t+1}\left(X_{2 t+1}\right), P_{2}$ 为多边形 $Y_{1} Y_{2} Y_{2 t+1} Y_{3} Y_{4} Y_{2 t+2} \cdots Y_{3 t-1} Y_{2 t-1} Y_{2 t}$, 可得

$$
f\left(P_{1}, P_{2}\right)=4 t-2=\left[\frac{4 n}{3}\right]
$$

此时 $X_{3}, X_{4} \cdots, X_{2 t}$ 均位于 $P_{2}$ 的边上, 而 $X_{1}$ 不在 $P_{2}$ 的边上, $Y_{1}, Y_{2}, \cdots, Y_{2 t}$ 均位于 $P_{1}$ 的边上.

(3) 当 $n=3 t(t \geq 2)$ 时, 考虑正 $4 t$ 边形 $X_{1} X_{2} Y_{1} Y_{2} X_{3} X_{4} \cdots X_{2 t-1} X_{2 t} Y_{2 t-1} Y_{2 t}$,设直线 $X_{2 i} Y_{2 i-1}, X_{2 i+1} Y_{2 i}$ 交点为 $X_{2 t+i}(1 \leq i \leq t-1)$, 直线 $X_{2 t} Y_{2 t-1}, X_{1} Y_{2 t}$ 交点为 $X_{3 t}$, 设直线 $Y_{2 j} X_{2 j+1}, X_{2 j+2} Y_{2 j+1}$ 交点为 $Y_{2 t+j}(1 \leq j \leq t-1)$, 直线 $Y_{2 t} X_{1}, Y_{1} X_{2}$ 交点为 $Y_{3 t}$. 记多边形 $X_{1} X_{2} X_{2 t+1} X_{3} X_{4} X_{2 t+2} \cdots X_{2 t-1} X_{2 t} X_{3 t}$ 为 $P_{1}$,多边形 $Y_{1} Y_{2} Y_{2 t+1} Y_{3} Y_{4} Y_{2 t+2} \cdots Y_{2 t-1} Y_{2 t} Y_{3 t}$ 为 $P_{2}$, 可得

$$
f\left(P_{1}, P_{2}\right)=4 t=\left[\frac{4 n}{3}\right] .
$$

其中 $X_{1}, X_{2}, \cdots, X_{2 t}$ 均位于 $P_{2}$ 的边上, $Y_{1}, Y_{2}, \cdots, Y_{2 t}$ 均位于 $P_{1}$ 的边上.
综上所述, 所求值为 $\left[\frac{4 n}{3}\right]$.

评注 本题是有关几何的组合最值问题. 我们从 $n$ 取 $4,5,6, \cdots$, 等简单情形入手, 进行一定的探索才能发现最优的构造和对应最值. 论证过程需要分析局部和整体的性质, 对一些特征量进行计算 (常常是对同一特征量从不同的角度入手算两次), 从而建立有关的等式或不等式. 另外, 解决组合几何问题常常需要借助于一些几何性质, 本题需要熟练图形的凸性.

4. 求满足以下条件的 2021 元正整数组的个数: 3 为其中一项, 且任意相邻两项的差的绝对值不超过 1 .

解 (陈铭意) 记 $S_{k}=\left\{\left(a_{1}, a_{2}, \cdots, a_{2021}\right) \mid \min _{1 \leq i \leq 2021}\left\{a_{i}\right\}=k, a_{1}, a_{2}, \cdots, a_{2021} \in\right.$ $\mathbb{N}_{+}$, 对任意 $1 \leq i \leq 2020$, 有 $\left.\left|a_{i+1}-a_{i}\right| \leq 1\right\}, k=1,2,3$. 即 $S_{k}$ 为 “最小项为 $k$ 且任意相邻两项的差的绝对值不超过 1 的所有 2021 元正整数组”构成的集合.

我们先证明: $\left|S_{k}\right|=3^{2020}(k=1,2,3)$.

记 $S_{0}=\left\{\left(a_{1}, a_{2}, \cdots, a_{2021}\right) \mid a_{1}=0, a_{2}, \cdots, a_{2021} \in \mathbb{Z}\right.$, 对任意 $1 \leq i \leq 2020$,有 $\left.\left|a_{i+1}-a_{i}\right| \leq 1\right\}$, 则 $\left|S_{0}\right|=3^{2020}$. 事实上, $a_{1}=0$, 我们依次确定 $a_{2}, \cdots, a_{2021}$的值, 而当 $a_{i}(1 \leq i \leq 2020)$ 确定后, 由 $\left|a_{i+1}-a_{i}\right| \leq 1$ 及 $a_{i+1} \in \mathbb{Z}$ 可知, $a_{i+1}$ 恰有 3 种可能的取值, 由乘法原理即得 $\left|S_{0}\right|=3^{2020}$.

对固定的 $k \in\{1,2,3\}$, 考虑映射 $f: S_{k} \rightarrow S_{0}$, 满足

$$
f\left(\left(a_{1}, a_{2}, \cdots, a_{2021}\right)\right)=\left(0, a_{2}-a_{1}, \cdots, a_{2021}-a_{1}\right) .
$$

一方面, 若存在 $\left(a_{1}, a_{2}, \cdots, a_{2021}\right),\left(a_{1}^{\prime}, a_{2}^{\prime}, \cdots, a_{2021}^{\prime}\right) \in S_{k}$, 使得

$$
f\left(\left(a_{1}, a_{2}, \cdots, a_{2021}\right)\right)=f\left(\left(a_{1}^{\prime}, a_{2}^{\prime}, \cdots, a_{2021}^{\prime}\right)\right),
$$

则对任意 $1 \leq i \leq 2021$, 均有 $a_{i}-a_{1}=a_{i}^{\prime}-a_{1}^{\prime}$, 即 $a_{i}-a_{i}^{\prime}$ 为定值, 设为 $t$, 注意到 $\left(a_{1}, a_{2}, \cdots, a_{2021}\right)$ 与 $\left(a_{1}^{\prime}, a_{2}^{\prime}, \cdots, a_{2021}^{\prime}\right)$ 中的最小项均为 $k$, 可得 $t=0$, 故 $f$ 为单射.

另一方面, 对任意 $\left(a_{1}, a_{2}, \cdots, a_{2021}\right) \in S_{0}$, 设该数组中最小项为 $x$, 则

$$
\left(a_{1}-x+k, a_{2}-x+k, \cdots, a_{2021}-x+k\right) \in S_{k},
$$

且

$$
f\left(\left(a_{1}-x+k, a_{2}-x+k, \cdots, a_{2021}-x+k\right)\right)=\left(a_{1}, a_{2}, \cdots, a_{2021}\right),
$$

故 $f$ 为满射.

综上, $f$ 为一一映射, 故 $\left|S_{k}\right|=\left|S_{0}\right|=3^{2020}(k=1,2,3)$.
又注意到各项均为 1 或 2 的 2021 元数组 (这样的数组恰有 $2^{2021}$ 个) 不符合条件, 于是, 所求数组个数 $=\sum_{k=1}^{3}\left|S_{k}\right|-2^{2021}=3^{2021}-2^{2021}$.

评注 本题中 2021 是年份数, 我们可以将其一般化为 $n$, 再考虑 $n=2,3, \cdots$等较为简单的情形, 不难猜测出一般情形下的答案. 论证的过程常常借助于递推数列或构造映射。

5. 数列 $\left\{a_{n}\right\}$ 满足:

$$
a_{1}=1, a_{n}=\left\{\begin{array}{c}
a_{n-1}+3, n-1 \in\left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\} \\
a_{n-1}+2, n-1 \notin\left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\}
\end{array}, n \geq 2 .\right.
$$

证明: 对任意正整数 $n$, 均有 $a_{n}<(\sqrt{2}+1) n$.

证明 (温玟杰, 陈铭意) 由数列 $\left\{a_{n}\right\}$ 递推关系可知,

$$
a_{n}=2 n-1+t_{n} .
$$

其中 $t_{n}=\mid\left\{k \in \mathbb{N}_{+} \mid 2 \leq k \leq n\right.$, 且 $k-1 \in\left\{a_{1}, a_{2}, \cdots, a_{k-1}\right\} \mid$, 补充定义 $t_{1}=0$.

所以, 对任意 $n \in \mathbb{N}_{+}$, 均有 $a_{n}>n-1$, 又注意到数列 $\left\{a_{n}\right\}$ 严格递增, 故对任意 $2 \leq k \leq n, a_{k}, a_{k+1}, \cdots, a_{n-1}$ 都大于 $k-1$, 从而, $n \geq 2$ 时,

$$
t_{n}=\mid\left\{k \in \mathbb{N}_{+} \mid 2 \leq k \leq n \text {, 且 } k-1 \in\left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\} \mid\right. \text {, }
$$

即 $t_{n}$ 为 $a_{1}, a_{2}, \cdots, a_{n-1}$ 中属于 $\{1,2, \cdots, n-1\}$ 的数的个数. 于是, $t_{n}$ 满足: $n \geq 2$ 时, $a_{t_{n}} \leq n-1<a_{t_{n}+1}$, 又由数列递推关系得, $a_{t_{n}+1}-a_{t_{n}} \leq 3$, 所以,

$$
n-3 \leq a_{t_{n}} \leq n-1
$$

下面归纳证明: 对任意正整数 $n$, 均有

$$
(\sqrt{2}+1)(n-1)<a_{n}<(\sqrt{2}+1) n .
$$

$n=1$ 时, (3) 式成立.

假设小于 $n(n \geq 2)$ 时, (3) 式成立, 考虑 $n$ 时的情形.

由 (1) 知, (3) $\Leftrightarrow(\sqrt{2}-1)(n-1)-1<t_{n}<(\sqrt{2}-1) n+1$.

而 $t_{n}<n$, 故由归纳假设得, $(\sqrt{2}+1)\left(t_{n}-1\right)<a_{t_{n}}<(\sqrt{2}+1) t_{n}$, 结合 (2)可知,

$\left\{\begin{array}{l}(\sqrt{2}+1)\left(t_{n}-1\right)<a_{t_{n}}<n \\ (\sqrt{2}+1) t_{n}>a_{t_{n}} \geq n-3\end{array} \Rightarrow\left\{\begin{array}{l}t_{n}<(\sqrt{2}-1) n+1 \\ t_{n}>(\sqrt{2}-1)(n-3)>(\sqrt{2}-1)(n-1)-1\end{array}\right.\right.$

故 (3) 式也成立.

综上, 由归纳原理知 (3) 式对任意正整数 $n$ 均成立, 从而原命题得证.
评注 本题是一个比较典型的数列问题. 我们从递推关系出发, 研究数列前面部分项, 可以观察出数列的增长规律, 再引入新数列描述之. 直接归纳证明题设不等式难以凑效，逆推分析的时候不难发现只需适当加强要证明的结论即可. 本题数列也蕴含别的规律. 刘家瑜同学发现数列 $\left\{a_{n}\right\}$ 满足 $a_{i+t}=2\left(a_{i}+t\right)+i-1\left(1 \leq t \leq a_{i+1}-a_{i}\right)$, 再以此为基础, 证明 $(\sqrt{2}+1)(n-1)-1<$ $a_{n}<(\sqrt{2}+1) n$ 亦可.

6. 锐角 $\triangle A B C$ 中, 点 $A, A_{b}, B_{a}, B, B_{c}, C_{b}, C, C_{a}, A_{c}$ 按顺序分布在其三条边上. 设 $\odot A A_{b} C_{a}$ 与 $\odot A A_{c} B_{a}$ 交于另一点 $A_{1}\left(A_{1} \neq A\right)$, 并类似定义 $B_{1}, C_{1}$. 已知 $A_{1}, B_{1}, C_{1}$ 这三个点互异且不共线. 证明: 直线 $A A_{1}, B B_{1}, C C_{1}$ 过同一个点,且该点在 $\triangle A_{1} B_{1} C_{1}$ 的外接圆上.

![](https://cdn.mathpix.com/cropped/2024_02_26_aa3bbb06f0436b073061g-09.jpg?height=508&width=636&top_left_y=1045&top_left_x=710)

证明 (陈铭意) 我们先证明: 直线 $A A_{1}, B B_{1}, C C_{1}$ 共点.

注意到 $A, A_{1}, B_{a}, A_{c} ; A, A_{1}, A_{b}, C_{a}$ 分别四点共圆, 有

$$
\angle A_{1} A_{b} B_{a}=\angle A_{1} C_{a} A_{c}, \angle A_{1} B_{a} A_{b}=\angle A_{1} A_{c} C_{a}
$$

于是 $\triangle A_{1} A_{b} B_{a} \sim \triangle A_{1} C_{a} A_{c}$, 于是,

$$
\left.\frac{\sin \angle B A A_{1}}{\sin \angle C A A_{1}}=\frac{B_{a} A_{1}}{A_{c} A_{1}} \text { (正弦定理 }\right)=\frac{A_{b} B_{a}}{C_{a} A_{c}},
$$

同理可证:

$$
\frac{\sin \angle A C C_{1}}{\sin \angle B C C_{1}}=\frac{C_{a} A_{c}}{B_{c} C_{b}}, \frac{\sin \angle C B B_{1}}{\sin \angle A B B_{1}}=\frac{B_{c} C_{b}}{A_{b} B_{a}} .
$$

所以,

$$
\frac{\sin \angle B A A_{1}}{\sin \angle C A A_{1}} \cdot \frac{\sin \angle A C C_{1}}{\sin \angle B C C_{1}} \cdot \frac{\sin \angle C B B_{1}}{\sin \angle A B B_{1}}=1,
$$

由角元形式塞瓦定理的逆定理可得, 直线 $A A_{1}, B B_{1}, C C_{1}$ 共点 (设为 $P$ ).

下证: $P, A_{1}, B_{1}, C_{1}$ 四点共圆.
设 $\odot\left(A B_{a} A_{c}\right), \odot\left(B C_{b} B_{a}\right)$ 交于点 $B_{a}, S$, 则

$$
\angle S A_{c} C=\angle S B_{a} A=\angle S C_{b} B
$$

于是, $S, A_{c}, C, C_{b}$ 四点共圆, 即 $\odot\left(A B_{a} A_{c}\right), \odot\left(B C_{b} B_{a}\right), \odot\left(C C_{b} A_{c}\right)$ 共点于 $S$.

从而,

$$
\angle P A_{1} S=\angle A B_{a} S=\angle B C_{b} S=\pi-\angle P B_{1} S=\angle C A_{c} S=\angle P C_{1} S
$$

点的相对位置不同时, 可能得到 $\angle P A_{1} S=\pi-\angle P C_{1} S$.

故 $P, A_{1}, B_{1}, C_{1}, S$ 五点共圆. 命题得证.

评注 本题图形看似复杂, 实际上极为对称. 我们可以先只研究局部的两个或者三个圆，导角不难发现三角形的相似，自然想到利用塞瓦定理的角元形式证明三线共点.第二问的关键是找到辅助点, 再借助多点共圆来证明四点共圆, 做出规范图则不难发现密克尔点 $S$ 在 $\odot\left(A_{1} B_{1} C_{1}\right)$ 上 (由密克尔定理也可得 $\odot\left(A B_{a} A_{c}\right), \odot\left(B C_{b} B_{a}\right), \odot\left(C C_{b} A_{c}\right)$ 共点, 由对称性, 借助另一个密克尔点亦可). 另外, 这里直接利用托勒密定理或三弦定理的逆定理来证明四点共圆也是可行的, 但计算量较大, 对导边和导三角比的要求高, 有兴趣的同学不妨一试.

