数学新星网 当教师专栏

www.nsmath.cn/jszl

# 2022 年第 21 届中国女子数学奥林匹克试题解答 

翟振华

(华东师范大学, 200241)

本文给出 2022 年第 21 届中国女子数学奥林匹克试题的解答.

## I. 试题

1. 考虑所有满足以下两个条件的实数序列 $x_{0}, x_{1}, x_{2}, \cdots, x_{100}$ :

(1) $x_{0}=0$;

(2) 对任意整数 $i, 1 \leq i \leq 100$, 有 $1 \leq x_{i}-x_{i-1} \leq 2$.

求最大的正整数 $k \leq 100$, 使得对任意这样的序列 $x_{0}, x_{1}, x_{2}, \cdots, x_{100}$, 均有

$$
x_{k}+x_{k+1}+\cdots+x_{100} \geq x_{0}+x_{1}+\cdots+x_{k-1} .
$$

(上海理工大学张思汇 供题)

2. 设 $n$ 是正整数. 有 $3 n$ 支女子排球队参加锦标赛, 每两支球队之间至多比赛一场 (排球比赛没有平局). 已知该锦标赛一共比赛了 $3 n^{2}$ 场.

证明: 存在一支球队, 其胜场数与负场数均不小于 $\frac{n}{4}$.

(清华大学 艾颖华供题)

3. 在三角形 $A B C$ 中, $A B>A C, I$ 是内心, $A M$ 是中线. 设过 $I$ 且与 $B C$垂直的直线与 $A M$ 交于点 $L, I$ 关于点 $A$ 的对称点为 $J$. 证明: $\angle A B J=\angle L B I$.

(华东师范大学 罗振华供题)

4. 给定素数 $p \geq 5$. 求三个连续正整数的乘积模 $p$ 的不同余数的个数.

(中国科学院数学与系统科学研究院 王彬供题)

5. 如图所示, 在三角形 $A B C$ 中, $K, L$ 是内部两点, $D$ 为边 $A B$ 上一点.已知 $B, K, L, C$ 四点共圆, 且 $\angle A K D=\angle B C K, \angle A L D=\angle B C L$. 证明: $A K=A L$.

(华东师范大学 何忆捷供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_c4d50846bf593d4a5142g-02.jpg?height=548&width=440&top_left_y=246&top_left_x=814)

6. 求所有具有下述性质的正整数 $n$ : 存在非空有限整数集合 $A, B$, 使得对任意整数 $m$, 以下三个命题中恰有一个成立,

(i) 存在 $a \in A$, 使得 $m \equiv a(\bmod n)$;

(ii) 存在 $b \in B$, 使得 $m \equiv b(\bmod n)$;

(iii) 存在 $a \in A, b \in B$, 使得 $m \equiv a+b(\bmod n)$.

(南方科技大学 付云皓供题)

7. 设整数 $n \geq 3$. 给定凸 $n$ 边形 $P$. 一种将 $P$ 的每个顶点染成红、黄、蓝三种颜色之一的染色方式称为 “好的” , 如果 $P$ 内部任何一点都在一个以 $P$ 的三个互不同色的顶点所构成的三角形的内部或者边界上. 求好的染色方式的个数.

注：两种染色方式若在某个顶点上颜色不同就认为是不同的染色方式.

(北京大学肖梁供题)

8. 设 $x_{1}, x_{2}, \cdots, x_{11}$ 是非负实数, 且总和等于 1 . 对 $i=1,2, \cdots, 11$, 记

$$
y_{i}= \begin{cases}x_{i}+x_{i+1}, & \text { 若 } i \text { 是奇数, } \\ x_{i}+x_{i+1}+x_{i+2}, & \text { 若 } i \text { 是偶数, }\end{cases}
$$

这里 $x_{12}=x_{1}$. 记 $F\left(x_{1}, x_{2}, \cdots, x_{11}\right)=y_{1} y_{2} \cdots y_{11}$.

证明: 当 $F$ 取得最大值时, 一定有 $x_{6}<x_{8}$.

(华东师范大学 㫿振华 供题)

## II. 解答

1. 考虑所有满足以下两个条件的实数序列 $x_{0}, x_{1}, x_{2}, \cdots, x_{100}$ :

(1) $x_{0}=0$;

(2) 对任意整数 $i, 1 \leq i \leq 100$, 有 $1 \leq x_{i}-x_{i-1} \leq 2$.

求最大的正整数 $k \leq 100$, 使得对任意这样的序列 $x_{0}, x_{1}, x_{2}, \cdots, x_{100}$, 均有

$$
x_{k}+x_{k+1}+\cdots+x_{100} \geq x_{0}+x_{1}+\cdots+x_{k-1} .
$$

解. 答案是 67 .

一方面, 若 $x_{i}=2 i, 1 \leq i \leq 34, x_{34+j}=x_{34}+j=68+j, 1 \leq j \leq 66$, 则该序列满足题述条件. 我们有

$$
\sum_{j=68}^{100} x_{j}-\sum_{i=0}^{67} x_{i}=\sum_{j=1}^{33}\left(x_{67+j}-x_{34+j}\right)-\sum_{i=1}^{34} x_{i}=33^{2}-34 \times 35<0 .
$$

这个例子表明 $k \geq 68$ 时不满足要求.

另一方面, 对任意满足题述条件的数列 $x_{1}, x_{2}, \cdots, x_{100}$, 易知 $x_{i} \leq 2 i, 1 \leq$ $i \leq 100$. 对 $0 \leq s<t \leq 100$, 有不等式 $x_{t}-x_{s} \geq t-s$. 从而

$$
\begin{aligned}
\sum_{j=67}^{100} x_{j}-\sum_{i=0}^{66} x_{i} & =\sum_{j=1}^{34}\left(x_{66+j}-x_{32+j}\right)-\sum_{i=1}^{32} x_{i} \\
& \geq 34^{2}-\sum_{i=1}^{32} 2 i \\
& =34^{2}-32 \times 33>0 .
\end{aligned}
$$

综上所述, 所求最大的 $k$ 为 67 .

2. 设 $n$ 是正整数. 有 $3 n$ 支女子排球队参加锦标赛, 每两支球队之间至多比赛一场 (排球比赛没有平局). 已知该锦标赛一共比赛了 $3 n^{2}$ 场.

证明：存在一支球队，其胜场数与负场数均不小于 $\frac{n}{4}$.

证. 反证法, 假设结论不成立. 设球队 $P_{1}, \cdots, P_{k}$ 的胜场数均小于 $\frac{n}{4}$, 其余 $3 n-k$ 支球队 $Q_{1}, \cdots, Q_{3 n-k}$ 的胜场数均不小于 $\frac{n}{4}$. 由反证法假设可知 $Q_{1}, \cdots, Q_{3 n-k}$ 的负场数均小于 $\frac{n}{4}$. 由于所有球队的胜场总数为 $3 n^{2}$, 必有一支球队的胜场数不少于 $n$, 从而 $3 n-k>0$.

$P_{1}, \cdots, P_{k}$ 之间的比赛场数不超过他们的胜场数之和, 因此不超过 $\frac{n k}{4}$. 类似地, $Q_{1}, \cdots, Q_{3 n-k}$ 之间的比赛场数不超过他们的负场数之和, 因此小于 $\frac{n(3 n-k)}{4}$ (这里用到了 $3 n-k>0)$.

而 $\left\{P_{1}, \cdots, P_{k}\right\}$ 与 $\left\{Q_{1}, \cdots, Q_{3 n-k}\right\}$ 之间的比赛至多 $k(3 n-k)$ 场. 由此可知总比赛场数 $N$ 满足

$$
N<\frac{n k}{4}+\frac{n(3 n-k)}{4}+k(3 n-k) \leq \frac{3 n^{2}}{4}+\frac{9 n^{2}}{4}=3 n^{2}
$$

与条件矛盾. 因此反证法假设不成立, 原命题成立.

3. 在三角形 $A B C$ 中, $A B>A C, I$ 是内心, $A M$ 是中线. 设过 $I$ 且与 $B C$直的直线与 $A M$ 交于点 $L, I$ 关于点 $A$ 的对称点为 $J$. 证明: $\angle A B J=\angle L B I$.

证. 我们需要如下引理.

引理: $\triangle A B C$ 中, 内心为 $I$, 内切圆 $\odot I$ 切三边 $B C, C A, A B$ 于 $A_{1}, B_{1}, C_{1}$.设 $A_{1} I$ 交 $B_{1} C_{1}$ 于 $L$, 则 $A L$ 过 $B C$ 的中点 $M$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c4d50846bf593d4a5142g-04.jpg?height=434&width=642&top_left_y=614&top_left_x=707)

引理的证明: 过 $L$ 作 $B C$ 的平行线交 $A C$ 于 $X$, 交 $A B$ 于 $Y$. 连结 $I B_{1}$, $I C_{1}, I X, I Y$.

由 $A_{1} L \perp B C, X Y \| B C$ 知 $A_{1} L \perp X Y$. 从而 $\angle I L X=\angle I B_{1} X=90^{\circ}$, 则 $I L X B_{1}$ 四点共圆. 同理, $I L C_{1} Y$ 四点共圆. 于是 $\angle I X B_{1}=\angle I L B_{1}=\angle I Y C_{1}$.

再结合 $\angle I B_{1} X=\angle I C_{1} Y=90^{\circ}, I B_{1}=I C_{1}$, 可知 $\triangle I B_{1} X \cong \triangle I C_{1} Y$. 故 $I X=I Y$.

又注意到 $I L \perp X Y$, 故 $L$ 是 $X Y$ 的中点. 结合 $X Y \| B C$ 可知 $A L$ 过 $B C$的中点 $M$. 引理获证.

回到原题, 设 $\triangle A B C$ 的内切圆 $\odot I$ 切三边 $B C, C A, A B$ 分别于点 $A_{1}, B_{1}, C_{1}$.由引理知 $L$ 位于 $B_{1} C_{1}$ 上. 设 $S$ 为 $B I$ 中点, $T$ 为 $A S$ 上一点满足 $\angle T B S=$ $\angle B A S$.

![](https://cdn.mathpix.com/cropped/2024_02_26_c4d50846bf593d4a5142g-04.jpg?height=711&width=640&top_left_y=1863&top_left_x=708)

下面证明 $B, T, L$ 共线.
由 $\angle T B S=\angle B A S$ 知 $\triangle B S T \sim \triangle A S B$, 故 $B S^{2}=S A \cdot S T$. 又 $B S=S I$,从而 $I S^{2}=S A \cdot S T$, 于是 $\triangle I S T \sim \triangle A S I$, 因此

$$
\angle B T I=\angle B T S+\angle I T S=\angle A B I+\angle A I B=180^{\circ}-\angle B A I .
$$

设 $H$ 为 $\triangle A I B$ 的垂心. 由垂心性质, $\angle B H I=\angle B A I$. 故 $B, T, I, H$四点共圆. 从而 $\angle S T H=\angle B T H-\angle B T S=\angle B I H-\angle A B I=90^{\circ}$, 结合 $\angle A C_{1} H=90^{\circ}$, 可知 $A, C_{1}, T, H$ 四点共圆, 且 $A H$ 为这个圆的直径. 于是

$$
\begin{aligned}
\angle I T C_{1} & =\angle H T C_{1}-\angle H T I=180^{\circ}-\angle H A C_{1}-\angle H B I \\
& =180^{\circ}-\left(90^{\circ}-\angle A B I\right)-\left(90^{\circ}-\angle A B I-\angle B A I\right) \\
& =2 \angle A B I+\angle B A I .
\end{aligned}
$$

又

$$
\angle I L B_{1}=\angle I C_{1} L+\angle L I C_{1}=\frac{1}{2} \angle B A C+\angle A B A_{1}=\angle B A I+2 \angle A B I
$$

故 $\angle I T C_{1}=\angle I L B_{1}$, 从而 $I, T, C_{1}, L$ 四点共圆. 由此得 $\angle I T L=\angle I C_{1} L=$ $\angle B A I$, 从而 $\angle I T L=\angle I C_{1} L=\angle B A I$, 所以 $B, T, L$ 共线, $\angle L B I=\angle T B I=$ $\angle B A S$.

而 $A S$ 是 $\triangle B I J$ 的中位线, 故 $A S \| B J, \angle B A S=\angle A B J$. 所以 $\angle A B J=$ $\angle L B I$, 结论获证.

4. 给定素数 $p \geq 5$. 求三个连续正整数的乘积模 $p$ 的不同余数的个数.

解. 记集合 $D=\{0,1, \ldots, p-1\}$, 记多项式 $f(x)=(x-1) x(x+1)=x^{3}-x$.本题的同余以及同余符号 “三” 均表示模 $p$ 同余. 对 $k=0,1,2,3$, 记

$$
B_{k}=\{b \in D \mid \text { 恰有 } k \text { 个 } a \in D \text { 使得 } f(a) \equiv b\} \text {. }
$$

考虑 $B_{2}$ 中的元素 $b$, 即存在 $a_{1} \not \equiv a_{2}$, 使得 $f\left(a_{1}\right) \equiv f\left(a_{2}\right) \equiv b$. 此时 $0 \equiv\left(a_{1}^{3}-a_{1}\right)-\left(a_{2}^{3}-a_{2}\right)=\left(a_{1}-a_{2}\right)\left(a_{1}^{2}+a_{1} a_{2}+a_{2}^{2}-1\right) \Rightarrow a_{1}^{2}+a_{1} a_{2}+a_{2}^{2} \equiv 1$.

这样对 $a_{3}=-a_{1}-a_{2}$, 有 $a_{3}^{2}+a_{3} a_{1}+a_{1}^{2}=\left(a_{1}+a_{2}\right)^{2}-\left(a_{1}+a_{2}\right) a_{1}+a_{1}^{2} \equiv 1$ 可推出 $f\left(a_{3}\right) \equiv f\left(a_{1}\right) \equiv b$, 由 $B_{2}$ 的定义知 $a_{3}$ 与 $a_{1}, a_{2}$ 之一同余, 因此 $a_{2} \equiv-2 a_{1}$ 或 $a_{1} \equiv-2 a_{2}$, 不妨设为前者, 此时 $a_{1}^{2}+a_{1} a_{2}+a_{2}^{2} \equiv 3 a_{1}^{2} \equiv 1,3 b \equiv 3 a_{1}^{3}-3 a_{1} \equiv-2 a_{1}$.当 3 是模 $p$ 的二次剩余时, $a_{1}$ 有两个; 当 3 不是模 $p$ 的二次剩余时, $a_{1}$ 不存在.因此满足条件的 $a_{1}$ 恰有 $1+\left(\frac{3}{p}\right)$ 个, 对应的 $b$ 也恰有 $1+\left(\frac{3}{p}\right)$ 个, 即 $\left|B_{2}\right|=1+\left(\frac{3}{p}\right)$.

显然 $\left|B_{1}\right|+2\left|B_{2}\right|+3\left|B_{3}\right|=|D|=p$.

另一方面考虑满足 $" f(u) \equiv f(v)$ 且 $u \not \equiv v$ ” (称之为碰撞) 的 $(u, v)$,
这等价于 $u^{2}+u v+v^{2} \equiv 1$ 且 $u-v \not \equiv 0$. 在换元 $(x, y) \equiv\left(\frac{u-v}{2}, \frac{u+v}{2}\right)$ (即 $(u, v) \equiv(x+y, y-x)$, 这样 $(x, y)$ 与 $(u, v)$ 一一对应) 后转化为 $x^{2}+3 y^{2} \equiv 1$且 $x \not \equiv 0$.

我们考虑模 $p$ 意义下满足 $x^{2}+3 y^{2} \equiv 1$ (即 $(3 y)^{2} \equiv 3-3 x^{2}$ ) 的 $(x, y)$的个数

$$
\begin{aligned}
T & =\sum_{x=1}^{p} 1+\left(\frac{3-3 x^{2}}{p}\right)=p+\left(\frac{-3}{p}\right) \sum_{x=1}^{p}\left(\frac{x^{2}-1}{p}\right)=p+\left(\frac{-3}{p}\right) \sum_{x=2}^{p}\left(\frac{\left(\frac{x+1}{x-1}\right)}{p}\right) \\
& =p+\left(\frac{-3}{p}\right) \sum_{x-1=1}^{p-1}\left(\frac{1+\frac{2}{x-1}}{p}\right)=p+\left(\frac{-3}{p}\right) \sum_{z=1}^{p-1}\left(\frac{z+1}{p}\right)=p-\left(\frac{-3}{p}\right) .
\end{aligned}
$$

上式用到了 $z=\frac{2}{x-1}$ 遍历模 $p$ 的缩系, 以及 $\sum_{k=1}^{p}\left(\frac{k}{p}\right)=0$. 这 $T$ 个 $(x, y)$中使得 $x \equiv 0\left(\right.$ 即 $\left.3 y^{2} \equiv 1\right)$ 的恰有 $1+\left(\frac{3}{p}\right)$ 个, 因此碰撞的有序对 $(u, v)$ 的个数是

$$
M=T-1-\left(\frac{3}{p}\right)=p-\left(\frac{-3}{p}\right)-1-\left(\frac{3}{p}\right)=T-\left|B_{2}\right|
$$

这样碰撞的无序对 $(u, v)$ 恰有 $\frac{M}{2}$ 个. 由于 $B_{3}$ 中的元素对应 3 次碰撞, $B_{2}$ 中的元素对应 1 次碰撞, $B_{1}$ 与 $B_{0}$ 中的元素对应 0 次碰撞, 因此 $\left|B_{2}\right|+3\left|B_{3}\right|=\frac{M}{2}$.

这样 $\left|B_{3}\right|=\frac{M-2\left|B_{2}\right|}{6}$, 因此 $f(x)$ 模 $p$ 的所有可能的余数的个数为

$$
\begin{aligned}
\left|B_{1}\right|+\left|B_{2}\right|+\left|B_{3}\right| & =p-\left|B_{2}\right|-2\left|B_{3}\right|=p-\frac{M+\left|B_{2}\right|}{3} \\
& =p-\frac{T}{3}=\frac{2 p+\left(\frac{-3}{p}\right)}{3}=\left\lfloor\frac{2 p+1}{3}\right\rfloor .
\end{aligned}
$$

注 1. 计算解数 $T$ 的另一种思路是:

考虑同余方程 $x^{2}+3 y^{2} \equiv z^{2}$ 等价于 $3 y^{2} \equiv z^{2}-x^{2}=(z+x)(z-x)$ 共有 $p^{2}$个解 $(y \equiv 0$ 的恰有 $2 p-1$ 个解, $y \equiv 1$ 的恰有 $p-1$ 个解, $\ldots$ ). 其中 $z \equiv 0$ 的解数为

$$
m_{0}=1+(p-1)\left[1+\left(\frac{-3}{p}\right)\right]
$$

其余 $z \equiv 1, z \equiv 2, \ldots, z \equiv p-1$ 的解数相等（可用 $(x, y, z) \leftrightarrow(k x, k y, k z)$ 将 $z \equiv 1$ 的解与 $z \equiv k$ 的解一一对应), 均为 $T=\frac{p^{2}-m_{0}}{p-1}=p-\left(\frac{-3}{p}\right)$.

若不熟悉 Legendre 符号, 也可以先得到 $0 \leq m_{0} \leq 2 p$, 从而推出 $x^{2}+3 y^{2} \equiv 1$的解数 $T \in\{p-1, p, p+1\}$, 后续可得本题答案为 $p-\frac{T}{3}$ 是整数, 也可得到结果.

注 2. 解数 $T=p-\left(\frac{-3}{p}\right)$ 的另一种理解是: 对每个 $y$, 满足 $x^{2} \equiv 1-3 y^{2}$ 的
$x$ 的个数是 $1+\left(\frac{1-3 y^{2}}{p}\right)$, 因此

$$
\begin{aligned}
T-p & =\sum_{y=0}^{p-1}\left(\frac{1-3 y^{2}}{p}\right) \equiv \sum_{y=0}^{p-1}\left(1-3 y^{2}\right)^{\frac{p-1}{2}} \\
& =\sum_{y=0}^{p-1}\left((-3)^{\frac{p-1}{2}} y^{p-1}+\cdots+1\right) \equiv(-3)^{\frac{p-1}{2}}(p-1)=-\left(\frac{-3}{p}\right) .
\end{aligned}
$$

5. 如图所示, 在三角形 $A B C$ 中, $K, L$ 是内部两点, $D$ 为边 $A B$ 上一点.已知 $B, K, L, C$ 四点共圆, 且 $\angle A K D=\angle B C K, \angle A L D=\angle B C L$. 证明: $A K=A L$.

证. 如图所示，

![](https://cdn.mathpix.com/cropped/2024_02_26_c4d50846bf593d4a5142g-07.jpg?height=542&width=437&top_left_y=954&top_left_x=815)

设 $A K, A L$ 的延长线分别与过 $B, K, L, C$ 的圆交于点 $X, Y$. 连接 $B X, B Y$. 结合条件, 得 $\angle A K D=\angle B C K=\angle B X K, \angle A L D=\angle B C L=\angle B Y L$. 所以 $D K\|B X, D L\| B Y$. 于是有

$$
\frac{A K}{A X}=\frac{A D}{A B}=\frac{A L}{A Y}
$$

又 $K, L, Y, X$ 共圆, 故由圆幂定理得

$$
A K \cdot A X=A L \cdot A Y
$$

将上面两式相乘得 $A K^{2}=A L^{2}$, 即 $A K=A L$.

6. 求所有具有下述性质的正整数 $n$ : 存在非空有限整数集合 $A, B$, 使得对任意整数 $m$, 以下三个命题中恰有一个成立,

(i) 存在 $a \in A$, 使得 $m \equiv a(\bmod n)$;

(ii) 存在 $b \in B$, 使得 $m \equiv b(\bmod n)$;

(iii) 存在 $a \in A, b \in B$, 使得 $m \equiv a+b(\bmod n)$.

解. 记 $A+B=\{a+b \mid a \in A, b \in B\}$. 题目可以理解为 $A$ 模 $n$ 的余数, $B$模 $n$ 的余数, 以及 $(A+B)$ 模 $n$ 的余数恰构成模 $n$ 的所有余数的一个划分.

(1) 若 $n>1$ 是奇数, 设 $n=2 k+1, k \in \mathbb{Z}_{>0}$. 取 $A=\{k\}, B=\{k+1, k+$ $2, \cdots, 2 k\}$, 则 $A+B=\{2 k+1,2 k+2, \cdots, 3 k\}$, 从而 $A, B, A+B$ 两两不相交,且并集恰是连续 $2 k+1$ 个数, 构成模 $2 k+1$ 的完系, 满足条件.

(2) 若 $n>1$ 满足条件, 则对任意整数 $d>1, d n$ 也满足条件. 事实上, 设 $n$所对应的集合为 $A, B$. 令

$A^{\prime}=\{a+x n \mid a \in A, x=0,1, \cdots, d-1\}, B^{\prime}=\{b+x n \mid b \in B, x=0,1, \cdots, d-1\}$我们验证 $A^{\prime}, B^{\prime}$ 对 $d n$ 满足题目要求.

由于 $A^{\prime}, B^{\prime}, A^{\prime}+B^{\prime}$ 模 $n$ 的余数恰是 $A, B, A+B$ 模 $n$ 的余数, 因此 $A^{\prime}, B^{\prime}, A^{\prime}+B^{\prime}$ 模 $n$ 的余数两两之间无交集, 当然模 $d n$ 也无交集, 故 (i),(ii),(iii)至多有一个成立. 考虑任意整数 $m$, 若存在 $a \in A$, 使得 $m \equiv a(\bmod n)$, 则 $m$ 与 $a+x n(x=0,1, \cdots, d-1)$ 之一模 $d n$ 同余, (i) 成立. 类似地, 若存在 $b \in B$, 使得 $m \equiv b(\bmod n)$, 则 (ii) 成立. 若存在 $a \in A, b \in B$, 使得 $m \equiv a+b$ $(\bmod n)$, 则 $m$ 与 $a+(b+x n)(x=0,1, \cdots, d-1)$ 之一模 $d n$ 同余, (iii) 成立.因此 (i),(ii),(iii) 恰有一个成立. $A^{\prime}, B^{\prime}$ 对 $d n$ 满足题目要求.

由 (1),(2) 可知除了 2 的方幂之外的所有整数 $n>1$ 均满足题目条件.

(3) $n=8$ 时, 容易验证 $A=\{1,2\}, B=\{3,6\}, A+B=\{4,5,7,8\}$, 满足要求. 再结合 $(2)$ 可知所有 $2^{k}(k \geq 3)$ 均满足要求.

由于 $A, B, A+B$ 均非空集, 故模 $n$ 至少有三个不同余数, $n \geq 3$, 因此 $n=1,2$ 不满足条件.

$n=4$ 时, 若 $A, B$ 模 4 只有一个余数, 则 $A+B$ 模 4 也只有一个余数, 不满足要求. 若 $A, B$ 中某个模 4 至少两个不同余数, 不妨设 $a_{1}, a_{2} \in A$ 模 4 不同余, 任取 $b \in B$, 则 $a_{1}+b, a_{2}+b$ 模 4 也不同余, 从而 $A+B$ 模 4 也至少两个余数, 也不满足要求. 因此 $n=4$ 也不满足条件.

综上所述, 所求 $n$ 为除 $1,2,4$ 外的所有正整数.

7. 设整数 $n \geq 3$. 给定凸 $n$ 边形 $P$. 一种将 $P$ 的每个顶点染成红、黄、蓝三种颜色之一的染色方式称为“好的” , 如果 $P$ 内部任何一点都在一个以 $P$ 的三个互不同色的顶点所构成的三角形的内部或者边界上. 求好的染色方式的个数.

注：两种染色方式若在某个顶点上颜色不同就认为是不同的染色方式.
解. 所有 “好的” 染色个数为

$$
f(n)= \begin{cases}2^{n}-2, & \text { 若 } n \text { 为奇数, } \\ 2^{n}-4, & \text { 若 } n \text { 为偶数. }\end{cases}
$$

记 $P$ 的顶点顺次为 $A_{1}, A_{2}, \ldots, A_{n}$. 在证明中角标按模 $n$ 理解.

首先说明好的染色恰好是所有相邻点异色且三种颜色都有的染色方式.

显然好的染色中三种颜色都有. 下证好的染色中相邻点异色. 若不然, 假设相邻点 $A_{i}, A_{i+1}$ 同色, 取 $P$ 内部一点 $X$ 非常靠近 $A_{i} A_{i+1}$ 的中点, 则 $X$ 只包含在以 $A_{i}, A_{i+1}$ 和其他某点为顶点的三角形内部, 但这样的三角形的三个顶点不异色, 故这样的染色不是好的.

下面说明相邻点异色且三种颜色都有的染色是好的. 我们用归纳法. $n=3$时. 三顶点必然异色, 此染色法是好的. 假设此结论小于 $n$ 的情形成立, 下面说明此结论对凸 $n$ 边形成立. 取三个颜色两两互异的顶点 $A, B, C\left(\right.$ 无妨 $A=A_{1}$, $B=A_{i}$, 且三点颜色分别为红、黄、蓝), 如果所取的点在 $\triangle A B C$ 边上或内部,已经满足要求, 只需分别讨论 $A B, B C, C A$ 三条对角线对应外部的 $P$ 的部分 (如果其中某条对角线是 $P$ 的一边则无需讨论该边.) 以下考虑 $A B$ 边对应的凸多边形, 即 $A_{1} A_{2} \cdots A_{i}$, 其余两种情形同理.

若 $A_{2}, A_{3}, \ldots, A_{i-1}$ 中有与 $A, B$ 异色的蓝色点, 则归纳假设说明其或边界任意一点都在某个异色三角形的边界或者内部. 若 $A_{2}, A_{3}, \ldots, A_{i-1}$ 中没有蓝色点, 因为相邻点颜色永远异色, 我们必有 $A_{2}, A_{4}, \ldots, A_{i}$ 为蓝色 ( $i$ 为偶数), 而 $A_{3}, A_{5}, \ldots, A_{i-1}$ 为红色. 这时, 三角形 $\triangle B A_{1} A_{2}, \triangle B A_{2} A_{3}, \ldots, \triangle B A_{i-1} A_{i}$ 均为异色三角形, 他们覆盖了凸多边形 $A_{1} A_{2} \cdots A_{i}$. 这完成了归纳证明。

最后计算好的染色个数, 为此我们不需要考虑几何形状. 先计算相邻点颜色不同的染色方法数, 记为 $D_{n}$. 显然 $D_{2}=D_{3}=6($ 相邻点颜色不同的二边形即理解为两个颜色不同的点). 对于 $n \geq 4$, 分为两种情况:

- $A_{n}$ 和 $A_{2}$ 异色, 则 $A_{1}$ 的颜色由 $A_{2}$ 和 $A_{n}$ 的颜色唯一决定.
- $A_{n}$ 和 $A_{2}$ 同色, 则可以将 $A_{2}$ 和 $A_{n}$ 合并变成 $B$, 则 $B A_{3} \cdots A_{n-1}$ 是一个相邻点异色的 $n-2$ 边形.

由此我们得到

$$
D_{n}=D_{n-1}+2 D_{n-2} .
$$

利用特征根可求得通项公式为 $D_{n}=2^{n}+2 \cdot(-1)^{n}$.
回到原题, 我们需要在上述计算中去掉只由两种颜色生成的染色法, 这只在 $n$ 为偶数时可能出现, 且一共有 6 种这样的染色法. 故所有好的染色个数为

$$
f(n)= \begin{cases}D_{n}=2^{n}-2, & \text { 若 } n \text { 为奇数, } \\ D_{n}-6=2^{n}-4, & \text { 若 } n \text { 为偶数. }\end{cases}
$$

8. 设 $x_{1}, x_{2}, \cdots, x_{11}$ 是非负实数, 且总和等于 1 . 对 $i=1,2, \cdots, 11$, 记

$$
y_{i}= \begin{cases}x_{i}+x_{i+1}, & \text { 若 } i \text { 是奇数, } \\ x_{i}+x_{i+1}+x_{i+2}, & \text { 若 } i \text { 是偶数, }\end{cases}
$$

这里 $x_{12}=x_{1}$. 记 $F\left(x_{1}, x_{2}, \cdots, x_{11}\right)=y_{1} y_{2} \cdots y_{11}$.

证明: 当 $F$ 取得最大值时, 一定有 $x_{6}<x_{8}$.

证. $F$ 看作关于 $x_{1}, x_{2}, \cdots, x_{11}$ 的函数是连续函数, 在有界闭集

$$
\Omega=\left\{\left(x_{1}, x_{2}, \cdots, x_{11}\right) \in\left(\mathbb{R}_{\geq 0}\right)^{11} \mid x_{1}+x_{2}+\cdots+x_{11}=1\right\}
$$

上存在最大值. 设 $F$ 在 $\left(a_{1}, a_{2}, \cdots, a_{11}\right) \in \Omega$ 处取得最大值, 显然此时 $F>0$.

(1) $a_{3}=a_{5}=a_{7}=a_{9}=a_{11}=0$.

若 $a_{3}>0$. 令 $a_{3}^{\prime}=0, a_{4}^{\prime}=a_{3}+a_{4}$, 对其它 $i$, 令 $a_{i}^{\prime}=a_{i}$. 则保持总和不变.我们证明 $F\left(a_{1}, a_{2}, \cdots, a_{11}\right)<F\left(a_{1}^{\prime}, a_{2}^{\prime}, \cdots, a_{11}^{\prime}\right)$, 这等价于

$$
\left(a_{2}+a_{3}+a_{4}\right)\left(a_{3}+a_{4}\right)\left(a_{4}+a_{5}+a_{6}\right)<\left(a_{2}^{\prime}+a_{3}^{\prime}+a_{4}^{\prime}\right)\left(a_{3}^{\prime}+a_{4}^{\prime}\right)\left(a_{4}^{\prime}+a_{5}^{\prime}+a_{6}^{\prime}\right),
$$

由 $a_{3}+a_{4}=a_{3}^{\prime}+a_{4}^{\prime}$, 以及 $a_{4}<a_{4}^{\prime}$ 可知成立. 这与 $F$ 在 $\left(a_{1}, a_{2}, \cdots, a_{11}\right)$ 处取最大值矛盾. 故 $a_{3}=0$. 类似地证明 $a_{5}=a_{7}=a_{9}=a_{11}=0$.

在 $F$ 解析式中令 $x_{3}=x_{5}=x_{7}=x_{9}=x_{11}=0$, 现将 $F$ 看作 $x_{1}, x_{2}, x_{4}, \cdots, x_{10}$的函数,

$$
F=\left(x_{1}+x_{2}\right)\left(x_{2}+x_{4}\right) x_{4}\left(x_{4}+x_{6}\right) x_{6}\left(x_{6}+x_{8}\right) x_{8}\left(x_{8}+x_{10}\right) x_{10}\left(x_{10}+x_{1}\right) x_{1} .
$$

则 $F$ 在 $\left(a_{1}, a_{2}, a_{4}, a_{6}, a_{8}, a_{10}\right)$ 处取到最大值, 显然 $a_{1}, a_{4}, a_{6}, a_{8}, a_{10}>0$.

(2) $a_{2}=0$.

反证法, 假设 $a_{2}>0$. 若 $a_{1} \leq a_{4}$, 令 $a_{1}^{\prime}=a_{1}+a_{2}, a_{2}^{\prime}=0$, 对其它 $i$, 令 $a_{i}^{\prime}=$ $a_{i}$. 则保持总和不变. 我们证明 $F\left(a_{1}, a_{2}, a_{4}, \cdots, a_{10}\right)<F\left(a_{1}^{\prime}, a_{2}^{\prime}, a_{4}^{\prime}, \cdots, a_{10}^{\prime}\right)$.

$$
\Leftrightarrow a_{1}\left(a_{10}+a_{1}\right)\left(a_{1}+a_{2}\right)\left(a_{2}+a_{4}\right)<a_{1}^{\prime}\left(a_{10}^{\prime}+a_{1}^{\prime}\right)\left(a_{1}^{\prime}+a_{2}^{\prime}\right)\left(a_{2}^{\prime}+a_{4}^{\prime}\right) .
$$

由于 $a_{1}<a_{1}^{\prime}, a_{10}+a_{1}<a_{10}^{\prime}+a_{1}^{\prime}$, 又只需证明

$$
\begin{gathered}
a_{1}\left(a_{1}+a_{2}\right)\left(a_{2}+a_{4}\right) \leq a_{1}^{\prime}\left(a_{1}^{\prime}+a_{2}^{\prime}\right)\left(a_{2}^{\prime}+a_{4}^{\prime}\right)=\left(a_{1}+a_{2}\right)\left(a_{1}+a_{2}\right) a_{4}, \\
\Leftrightarrow a_{1}\left(a_{2}+a_{4}\right) \leq a_{4}\left(a_{1}+a_{2}\right), \quad \Leftrightarrow a_{1} a_{2} \leq a_{4} a_{2},
\end{gathered}
$$

成立. 若 $a_{1} \geq a_{4}$, 则令 $a_{4}^{\prime}=a_{4}+a_{2}, a_{2}^{\prime}=0$, 对其它 $i$, 令 $a_{i}^{\prime}=a_{i}$, 同样有

$$
F\left(a_{1}, a_{2}, a_{4}, \cdots, a_{10}\right)<F\left(a_{1}^{\prime}, a_{2}^{\prime}, a_{4}^{\prime}, \cdots, a_{10}^{\prime}\right) .
$$

都与 $F$ 在 $\left(a_{1}, a_{2}, a_{4}, a_{6}, a_{8}, a_{10}\right)$ 处取到最大值矛盾. 因此 $a_{2}=0$.

在 $F$ 的解析式中再令 $x_{2}=0$, 现将 $F$ 看作 $x_{1}, x_{4}, x_{6}, x_{8}, x_{10}$ 的函数,

$$
F=x_{4}^{2}\left(x_{4}+x_{6}\right) x_{6}\left(x_{6}+x_{8}\right) x_{8}\left(x_{8}+x_{10}\right) x_{10}\left(x_{10}+x_{1}\right) x_{1}^{2} .
$$

则 $F$ 在 $\left(a_{1}, a_{4}, a_{6}, a_{8}, a_{10}\right)$ 处取到最大值.

(3) $a_{1}=a_{4}, a_{6}=a_{10}$.

设 $a_{1}^{\prime}=a_{4}^{\prime}=\frac{1}{2}\left(a_{1}+a_{4}\right), a_{6}^{\prime}=a_{10}^{\prime}=\frac{1}{2}\left(a_{6}+a_{10}\right), a_{8}^{\prime}=a_{8}$, 这样保持总和不变. 由均值不等式,

$$
\begin{aligned}
& a_{1}^{2} a_{4}^{2} \leq a_{1}^{\prime 2} a_{4}^{\prime 2}, \quad\left(a_{4}+a_{6}\right)\left(a_{10}+a_{1}\right) \leq\left(a_{4}^{\prime}+a_{6}^{\prime}\right)\left(a_{10}^{\prime}+a_{1}^{\prime}\right) \\
& a_{6} a_{10} \leq a_{6}^{\prime} a_{10}^{\prime}, \quad\left(a_{6}+a_{8}\right)\left(a_{8}+a_{10}\right) \leq\left(a_{6}^{\prime}+a_{8}^{\prime}\right)\left(a_{8}^{\prime}+a_{10}^{\prime}\right)
\end{aligned}
$$

又 $a_{8}=a_{8}^{\prime}$, 将这些式子相乘即得

$$
F\left(a_{1}, a_{4}, \cdots, a_{10}\right) \leq F\left(a_{1}^{\prime}, a_{4}^{\prime}, \cdots, a_{10}^{\prime}\right) .
$$

由于 $F$ 在 $\left(a_{1}, a_{4}, \cdots, a_{10}\right)$ 处取最大值, 因此上式等号成立, 再由均值不等式等号成立条件即得 $a_{1}=a_{4}, a_{6}=a_{10}$.

在 $F$ 的解析式中将 $x_{4}$ 用 $x_{1}$ 代替, $x_{10}$ 用 $x_{6}$ 代替, 现将 $F$ 看作 $x_{1}, x_{6}, x_{8}$的函数,

$$
F=x_{1}^{4} x_{6}^{2} x_{8}\left(x_{1}+x_{6}\right)^{2}\left(x_{6}+x_{8}\right)^{2},
$$

且 $2 x_{1}+2 x_{6}+x_{8}=1$.

(4) 下面来解方程组 (此方程组是由均值不等式配系数得到的, 在 (5) 中会用到)

$$
\frac{2}{u}+\frac{1}{u+v}=\frac{1}{v}+\frac{1}{u+v}+\frac{1}{v+1}=1+\frac{2}{v+1}, \quad u, v>0
$$

我们证明有唯一的正实数解 $u, v$, 且 $v<1$.

从第一个等式得 $\frac{2}{u}=\frac{1}{v}+\frac{1}{v+1}$, 从而 $u=\frac{2 v(v+1)}{2 v+1}$. 再从第二个等式得 $\frac{1}{v}+\frac{1}{u+v}=$ $1+\frac{1}{v+1}$, 再将 $u$ 代人, 整理为关于 $v$ 的方程

$$
4 v^{3}+5 v^{2}-4 v-4=0 .
$$

设 $f(t)=4 t^{3}+5 t^{2}-4 t-4$, 则 $f^{\prime}(t)=12 t^{2}+10 t-4$, 在 $[0,+\infty)$ 上先负后正，从而 $f(t)$ 在 $[0,+\infty)$ 上先减后增, 由于 $f(0)=-4<0, f(1)=1>0$, 故 $f$ 在 $[0,+\infty)$ 上有唯一解 $v \in(0,1)$, 进而 $u$ 也唯一确定.

(5) 设 $u, v>0$ 为满足 (4) 中方程组的解, 且设 $\frac{2}{u}+\frac{1}{u+v}=k$. 利用均值不等式, 有

$$
\begin{aligned}
& F\left(x_{1}, x_{6}, x_{8}\right)=\left(\frac{x_{1}}{u}\right)^{4}\left(\frac{x_{6}}{v}\right)^{2} x_{8}\left(\frac{x_{1}+x_{6}}{u+v}\right)^{2}\left(\frac{x_{6}+x_{8}}{v+1}\right)^{2} u^{4} v^{2}(u+v)^{2}(v+1)^{2} \\
\leq & \frac{u^{4} v^{2}(u+v)^{2}(v+1)^{2}}{7^{7}}\left(\frac{4}{u} x_{1}+\frac{2}{v} x_{6}+x_{8}+\frac{2}{u+v}\left(x_{1}+x_{6}\right)+\frac{2}{v+1}\left(x_{6}+x_{8}\right)\right)^{7} \\
= & \frac{u^{4} v^{2}(u+v)^{2}(v+1)^{2}}{7^{7}}\left(\left(\frac{4}{u}+\frac{2}{u+v}\right) x_{1}\right. \\
& \left.+\left(\frac{2}{v}+\frac{2}{u+v}+\frac{2}{v+1}\right) x_{6}+\left(1+\frac{2}{v+1}\right) x_{8}\right)^{7} \\
= & \frac{u^{4} v^{2}(u+v)^{2}(v+1)^{2}}{7^{7}}\left(2 k x_{1}+2 k x_{6}+k x_{8}\right)^{7}=\frac{u^{4} v^{2}(u+v)^{2}(v+1)^{2} k^{7}}{7^{7}} .
\end{aligned}
$$

上面等号成立当且仅当 $x_{1}: x_{6}: x_{8}=u: v: 1$, 即

$$
x_{8}=\frac{1}{2 u+2 v+1}, x_{6}=\frac{v}{2 u+2 v+1}, x_{1}=\frac{u}{2 u+2 v+1} \text {. }
$$

所以 $F$ 取到最大值当且仅当 $x_{2}=x_{3}=x_{5}=x_{7}=x_{9}=x_{11}=0, x_{1}=x_{4}=$ $\frac{u}{2 u+2 v+1}, x_{6}=x_{10}=\frac{v}{2 u+2 v+1}, x_{8}=\frac{1}{2 u+2 v+1}$. 此时 $x_{6}=v x_{8}<x_{8}$.

