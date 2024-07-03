# 数学新星网 炩学生专栏 <br> www.nsmath.cn/xszl 

## 2020 伊朗 TST (第一轮) 解答与评析

梁敬勋

(浙江杭州学军中学, 310012)

指导老师: 边红平

伊朗数学奥林匹克国家队选拔一般有三轮共 18 个题. 伊朗的试题总体质量很高, 有些题目难度极大, 总是给我们的竞赛选手留下深刻的印象.

本文是 2020 年伊朗国家队选拔赛 (第一轮) 试题的解答. 由于能力有限, 难免有不当疏漏之处, 敬请读者批评指正.

## I. 试题

1. 给一个完全图的每条边赋上互不相同的正数, 使得对于图中任意一个三角形, 其某一边上的数字等于另外两边上的数字之和. 证明: 可以给这个图的每个顶点赋值, 使得每条边上的数字等于这条边两个端点上的数字之差(的绝对值).
2. 设 $\triangle A B C$ 的外心为 $O . D, E$ 分别在边 $A C, A B$ 上, $P, Q, R, S$ 是平面上的点, 满足 $P, R$ 和 $C$ 在直线 $A B$ 的异侧, $Q, S$ 和 $B$ 在直线 $A C$ 的异侧, 且 $D, A, P, R$ 共圆, $E, A, Q, S$ 共圆, $\triangle B C E \sim \triangle A D Q, \triangle C B D \sim \triangle A E P$ (顶点按此顺序对应), $\angle A R E=\angle A S D=\angle B A C$. 若 $R S \| P Q$, 证明: $R E, D S, A O$ 三线共点.
3. 我们定义一个正整数 $n$ 是 “有趣的” , 如果对 $1,2, \cdots, n$ 的任意排列 $\sigma$,都存在多项式 $P_{1}, P_{2}, \cdots, P_{n}$ 和 $\varepsilon>0$, 满足:
1) $P_{1}(0)=P_{2}(0)=\cdots=P_{n}(0)$
2) $\forall-\varepsilon<x<0, P_{1}(x)>P_{2}(x)>\cdots>P_{n}(x)$
3) $\forall 0<x<\varepsilon, P_{\sigma(1)}(x)>P_{\sigma(2)}(x)>\cdots>P_{\sigma(n)}(x)$

求所有 “有趣的” 正整数 $n$.

4. 函数 $g:[0,1] \rightarrow \mathbb{R}$ 满足如下性质: 将区间 $[0,1]$ 任意分成两个不交的非空
集合 $A, B$, 一定存在 $x \in A, g(x) \in B$ 或存在 $x \in B, g(x) \in A$. 且 $\forall x \in[0,1]$, 有 $g(x)>x$. 证明: 存在无穷多个 $x \in[0,1]$ 使得 $g(x)=1$.
5. 给定整数 $k$, 证明存在无穷多互异正整数对 $(m, n)$ 满足:

$$
n+s(2 n)=m+s(2 m), k n+s\left(n^{2}\right)=k m+s\left(m^{2}\right)
$$

其中 $s$ 是数码和函数.

6. 给定 $n$ 个正数, 是否一定可以找到一个凸 $n+2$ 边形和它的一个三角剖分, 使得剖分三角形的直径 (即三角形的最长边) 为给定的 $n$ 个正数.

## II. 解答

1. 给一个完全图的每条边赋上互不相同的正数, 使得对于图中任意一个三角形, 其某一边上的数字等于另外两边上的数字之和. 证明: 可以给这个图的每个顶点赋值, 使得每条边上的数字等于这条边两个端点上的数字之差(的绝对值).

证明. 设赋值最大的边为 $e=u v$, 赋值为 $a$.

我们给顶点作如下赋值: 给点 $v$ 赋值 0 . 对 $\forall v^{\prime} \in V, v^{\prime} \neq v$, 给 $v^{\prime}$ 赋的值等于 $v v^{\prime}$ 的赋值.

下证该赋值满足要求.

任取 $v_{1}, v_{2} \in V, v_{1}, v_{2} \neq u, v$. 首先 $u$ 的赋值为 $a$. 设 $v v_{1}, u v_{1}, v v_{2}, u v_{2}$ 赋值分别为 $b, c, d, f$. 则 $v_{1}, v_{2}$ 赋值为 $b, d$.

我们验证:

(1) $u v_{1}$ 赋值 $c=|a-b|, u v_{2}$ 赋值 $f=$ $|a-d|$.

![](https://cdn.mathpix.com/cropped/2024_02_26_6bb2a7c15746a751d381g-2.jpg?height=477&width=620&top_left_y=1675&top_left_x=1118)

(2) $v_{1} v_{2}$ 赋值为 $|b-d|$.

(1): 在 $\triangle u v v_{1}$ 中, 由 $a$ 的最大性, $a=b+c$. 同理, $a=d+f$. 故 (1) 成立.

(2): $\triangle v v_{1} v_{2}$ 中, 若 $v_{1} v_{2}$ 赋值非 $|b-d|$, 则只能为 $b+d$. 考察 $\triangle u v_{1} v_{2}$, 要么 $b+d=c+f$, 要么 $b+d=|c-f|$.

若为前者, 结合 $b+c=a=d+f$ 知 $b=f$, 与各边赋值不同矛盾!

若为后者, 则 $b+d=|c-f|=|b-d|$, 与 $b, d>0$ 矛盾!

故 $v_{1} v_{2}$ 赋值为 $|b-d|$.
综上, 该赋值符合.

注. 顶点的赋值几乎是确定的, 要描述顶点的赋值, 只需知道相互之间的大小. 故希望找一个最小元, 取赋值最大的边可以定位极大元与极小元.

2. 设 $\triangle A B C$ 的外心为 $O . D, E$ 分别在边 $A C, A B$ 上, $P, Q, R, S$ 是平面上的点, 满足 $P, R$ 和 $C$ 在直线 $A B$ 的异侧, $Q, S$ 和 $B$ 在直线 $A C$ 的异侧, 且 $D, A, P, R$ 共圆, $E, A, Q, S$ 共圆, $\triangle B C E \sim \triangle A D Q, \triangle C B D \sim \triangle A E P$ (顶点按此顺序对应), $\angle A R E=\angle A S D=\angle B A C$. 若 $R S \| P Q$, 证明: $R E, D S, A O$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_6bb2a7c15746a751d381g-3.jpg?height=665&width=596&top_left_y=907&top_left_x=747)

证明. 我们证明 $R, S \in \odot O$.

由 $\angle P A E=\angle D C B$ 可知, $P A$ 与 $\odot O$ 相切, 即 $P A \perp A O$. 同理, $Q A \perp A O$.故 $P, A, Q$ 共线. 设直线 $A P$ 交 $\odot A R E$ 于点 $A, L$, 则 $\angle A L E=\angle A R E$. 所以 $\angle A L E=\angle C A B$, 又 $\angle L A E=\angle A C B$ 知 $\triangle A E L \sim \triangle C B A$, 且 $P, D$ 为对应点.注意到

$$
\angle R L A=\angle R L E+\angle E L A=\angle R A E+\angle E A C=\angle R A C,
$$

又 $\angle R P L=\angle R D A$, 故 $\triangle R L P \sim \triangle R A D$. 由 $\triangle A E L \sim \triangle C B A$ 及 $P, D$ 的对应关系, 结合上述相似知 $D, P$ 也为该相似的对应点. 故 $\triangle R A P \sim \triangle R C D$. 从而

$$
\angle P A R=\angle A C R \Rightarrow P A \text { 与 } \odot(C A R) \text { 相切 } \Rightarrow R \in \odot O \text {. }
$$

同理, $S \in \odot O$.

现在, $R S \| P Q$, 故 $R S \perp A O$, 从而 $A R=A S$. 又

$$
\angle E R S=\angle E R A-\angle A R S=\angle D S A-\angle A S R=\angle D S R,
$$

故 $R E, S D$ 交在 $R S$ 中垂线 $A O$ 上, 得证!
注. 本题难以画出标准圆, 故退而求其次, 先不看 $P Q \| R S$, 分析图形的性质. 此时作标准圆即可发现 $R, S \in \odot O$.

3. 我们定义一个正整数 $n$ 是 “有趣的” , 如果对 $1,2, \cdots, n$ 的任意排列 $\sigma$,都存在多项式 $P_{1}, P_{2}, \cdots, P_{n}$ 和 $\varepsilon>0$, 满足:
1) $P_{1}(0)=P_{2}(0)=\cdots=P_{n}(0)$
2) $\forall-\varepsilon<x<0, P_{1}(x)>P_{2}(x)>\cdots>P_{n}(x)$
3) $\forall 0<x<\varepsilon, P_{\sigma(1)}(x)>P_{\sigma(2)}(x)>\cdots>P_{\sigma(n)}(x)$

求所有 “有趣的” 正整数 $n$.

解. 所求有趣的正整数 $n$ 为 $1,2,3$.

对一个非零多项式 $f(x)=\sum_{k=0}^{m} a_{k} x^{k}$, 称使 $a_{k} \neq 0$ 的最小的 $k$ 对应的项 $a_{k} x^{k}$称为 $f$ 的“特征”. 显然, $|x|$ 充分小时 $f(x)$ 的正负取决于 $f$ 的特征的正负.

首先, $n \geq 4$ 是不符合的. 为此, 容易看出仅需证 $n=4$ 的情形.

取 $\sigma$ 使: $\sigma(1)=3, \sigma(2)=1, \sigma(3)=4, \sigma(4)=2$. 下证不存在符合的 $P_{1}, P_{2}, P_{3}, P_{4}$ 及 $\varepsilon>0$.

反证法, 假设存在符合的 $P_{1}, P_{2}, P_{3}, P_{4}$ 及正数 $\varepsilon$. 记

$$
Q_{1}=P_{3}-P_{1}, Q_{2}=P_{1}-P_{4}, Q_{3}=P_{4}-P_{2},
$$

则 $x>0$ 且 $x$ 充分小时, $Q_{1}, Q_{2}, Q_{3}$ 均为正值. 设 $Q_{1}, Q_{2}, Q_{3}$ 的特征依次为 $c_{1} x^{\alpha_{1}}, c_{2} x^{\alpha_{2}}, x_{3}^{\alpha_{3}}$, 则 $c_{1}, c_{2}, c_{3}>0$. 据此 $\varepsilon_{1} Q_{1}+\varepsilon_{2} Q_{2}+\varepsilon_{3} Q_{3}\left(\varepsilon_{1}, \varepsilon_{2}, \varepsilon_{3} \in\{0,1\}\right.$ 且不全为 0$)$ 的特征的次数必为 $\alpha_{1}$ 或 $\alpha_{2}$ 或 $\alpha_{3}$, 即不会出现最低次项相互抵消的情况.

(1) $\alpha_{1}=\min \left\{\alpha_{1}, \alpha_{2}, \alpha_{3}\right\}$, 则由于 $-\varepsilon<x<0$ 时,

$$
\begin{gathered}
P_{3}(x)-P_{4}(x)>0 \Rightarrow Q_{1}(x)+Q_{2}(x)>0 \Rightarrow x^{\alpha_{1}}>0 \\
P_{2}(x)-P_{3}(x)>0 \Rightarrow Q_{1}(x)+Q_{2}(x)+Q_{3}(x)<0 \Rightarrow x^{\alpha_{1}}<0
\end{gathered}
$$

矛盾!

(2) $\alpha_{2}=\min \left\{\alpha_{1}, \alpha_{2}, \alpha_{3}\right\}$, 类似地, $-\varepsilon<x<0$ 时,

$$
\begin{gathered}
P_{3}(x)-P_{4}(x)>0 \Rightarrow Q_{1}(x)+Q_{2}(x)>0 \Rightarrow x^{\alpha_{2}}>0 \\
P_{2}(x)-P_{3}(x)>0 \Rightarrow Q_{1}(x)+Q_{2}(x)+Q_{3}(x)<0 \Rightarrow x^{\alpha_{2}}<0
\end{gathered}
$$

矛盾!

(3) $\alpha_{3}=\min \left\{\alpha_{1}, \alpha_{2}, \alpha_{3}\right\}$, 则 $-\varepsilon<x<0$ 时,

$$
\begin{gathered}
0<P_{1}(x)-P_{2}(x)=Q_{2}(x)+Q_{3}(x) \Rightarrow x^{\alpha_{3}}>0 \\
0>P_{3}(x)-P_{2}(x)=Q_{1}(x)+Q_{2}(x)+Q_{3}(x) \Rightarrow x^{\alpha_{3}}<0
\end{gathered}
$$

矛盾!

综上, $n \geq 4$ 不符合.

另一方面, 显然 $n=1,2$ 是符合的, 下验证 $n=3$ 符合. 取 $\varepsilon=\frac{1}{100}$.

(1) $\sigma(1)=1, \sigma(2)=2, \sigma(3)=3$, 取 $P_{1}(x)=x^{4}+x^{2}, P_{2}(x)=x^{2}, P_{3}(x)=0$.

(2) $\sigma(1)=1, \sigma(2)=3, \sigma(3)=2$, 取 $P_{1}(x)=x^{3}+x^{2}, P_{2}(x)=0, P_{3}(x)=x^{3}$.

(3) $\sigma(1)=2, \sigma(2)=1, \sigma(3)=3$, 取 $P_{1}(x)=x^{2}, P_{2}(x)=x^{2}+x^{3}, P_{3}(x)=0$.

(4) $\sigma(1)=2, \sigma(2)=3, \sigma(3)=1$, 取 $P_{1}(x)=0, P_{2}(x)=x+x^{2}, P_{3}(x)=x$.

(5) $\sigma(1)=3, \sigma(2)=1, \sigma(3)=2$, 取 $P_{1}(x)=x^{2}, P_{2}(x)=0, P_{3}(x)=x^{2}+x$.

(6) $\sigma(1)=3, \sigma(2)=2, \sigma(3)=1$, 取 $P_{1}(x)=0, P_{2}(x)=x, P_{3}(x)=x+x^{3}$.

综上, 所求的有趣数为 $1,2,3$.

注. 本题容易想到用差分的特征来判断正负. 但是引入 $Q_{i}=P_{\sigma(i)}-P_{\sigma(i+1)}$会使 $P_{i}-P_{i+1}$ 表示起来不方便. 本题的关键是各 $Q_{i}$ 的特征都是正系数的, 从而使加式中特征不会相互抵消, 使得 $P_{i}-P_{i+1}$ 有可能研究.

4. 函数 $g:[0,1] \rightarrow \mathbb{R}$ 满足如下性质: 将区间 $[0,1]$ 任意分成两个不交的非空集合 $A, B$, 一定存在 $x \in A, g(x) \in B$ 或存在 $x \in B, g(x) \in A$. 且 $\forall x \in[0,1]$, 有 $g(x)>x$. 证明: 存在无穷多个 $x \in[0,1]$ 使得 $g(x)=1$.

证明. 反证法, 若仅有有限个 $x \in[0,1]$ 使 $g(x)=1$, 记这些 $x$ 组成集合 $S$.

首先, $S \neq \emptyset$. 否则, 取 $A=\{1\}, B=[0,1)$, 由题意, 要么存在 $x \in A, g(x) \in B$或存在 $x \in B, g(x) \in A$. 注意到 $g(x)>x, \forall x \in[0,1]$. 故存在 $x \in B, g(x) \in A$,此时 $g(x)=1$, 矛盾!

其次, 由 $g(x)>x, \forall x \in[0,1]$, 知 $1 \notin S$.

设 $S$ 的最大元为 $\alpha$. 取

$$
A=\left\{x \mid x \in[0,1] \text { 且存在 } k \in \mathbb{N}^{*} \text { 使 } g^{(k)}(x)=1\right\} \text {, }
$$

其中 $g^{(k)}=\underbrace{g \circ \cdots \circ g}_{k \text { 个 } g}$. 则 $A$ 非空集, 记 $A^{*}=A \cup\{1\}$.

任取 $x \in A$, 有

$$
g^{(k)}(x)=1 \Rightarrow g^{(k-1)}(x) \leq \alpha \Rightarrow x \leq \alpha<1,
$$

取 $B=[0,1] \backslash A^{*}$, 则 $B \neq \emptyset$. 由题意, 要么存在 $x \in A^{*}, g(x) \in B$ 或存在 $x \in B, g(x) \in A^{*}$.

若为前者, 由 $x \in A^{*}$, 设 $g^{(k)}(x)=1($ 显然 $x \neq 1), k \in \mathbb{N}^{*}$. 由 $1 \notin B$ 知, $k \geq 2$. 故 $g^{(k-1)}(g(x))=1$, 从而 $g(x) \in A$, 矛盾!

若为后者, 由 $A$ 的定义知, $g(x) \neq 1$. 由 $g(x) \in A$, 设 $g^{(k)}(g(x))=1, k \in \mathbb{N}^{*}$,即 $g^{(k+1)}(x)=1$, 故 $x \in A$, 矛盾!

综上, 反证假设不成立, $S$ 为无限集.

注. 要充分利用条件必须取习钻的 $A, B$. 因此想到反证法就很容易.

5. 给定整数 $k$, 证明存在无穷多互异正整数对 $(m, n)$ 满足:

$$
n+s(2 n)=m+s(2 m), k n+s\left(n^{2}\right)=k m+s\left(m^{2}\right) \text {, }
$$

其中 $s$ 是数码和函数.

证明. 首先注意到一个事实:

设 $n \in \mathbb{N}^{*}, n$ 的个位数不是 0 和 $5, t \in \mathbb{N}^{*}, 10^{t}>2 n$, 则

$$
s\left(10^{t}-n\right)=9 t+1-s(n), s\left(2\left(10^{t}-n\right)\right)=9 t+2-s(2 n) \text {. }
$$

事实上, 设 $n=\left(\overline{a_{1} a_{2} \cdots a_{t}}\right)_{10}, a_{i} \in \mathbb{N}, 0 \leq a_{i} \leq 9$, 则 $a_{t} \neq 0$. 从而

$$
10^{t}-n=\left(\overline{\left(9-a_{1}\right)\left(9-a_{2}\right) \cdots\left(9-a_{t-1}\right)\left(10-a_{t}\right)}\right)_{10} .
$$

设 $2 n=\left(\overline{b_{1} b_{2} \cdots b_{t}}\right)_{10}$,

$$
2\left(10^{t}-n\right)=2 \cdot 10^{n}-2 n=\left(\overline{1\left(9-b_{1}\right)\left(9-b_{2}\right) \cdots\left(9-b_{t-1}\right)\left(10-b_{t}\right)}\right)_{10}
$$

于是, (1) 成立.

对 $k \in \mathbb{Z}$, 记

$S_{k}=\left\{(m, n) \mid m, n \in \mathbb{N}^{*}, m \neq n\right.$ 且 $\left.n+s(2 n)=m+s(2 m), k n+s\left(n^{2}\right)=k m+s\left(m^{2}\right)\right\}$.

原命题即证 $S_{k}$ 为无限集.

下面引入两个变换. 这两个变换都只是针对 $S_{k}$ 的部分元素.

对 $(m, n) \in S_{k}, m$ 与 $n$ 的个位数都不是 0 和 $5, t \in \mathbb{N}^{*}, 10^{t}>m^{2}+n^{2}, 10^{t}>$ $2 m, 10^{t}>2 n$ 定义 $\Gamma_{1, t}: S_{k} \rightarrow S_{k+1}$ 为

$$
\Gamma_{1, t}(m, n)=\left(10^{t}+m, 10^{t}+n\right) .
$$

我们证明 $\left(10^{t}+m, 10^{t}+n\right) \in S_{k+1}$.

事实上，

$$
10^{t}+m+s\left(2\left(10^{t}+m\right)\right)=10^{t}+2+m+s(2 m)=10^{t}+n+s\left(2\left(10^{t}+n\right)\right),
$$

且有

$$
\begin{aligned}
& (k+1)\left(10^{t}+m\right)+s\left(\left(10^{t}+m\right)^{2}\right) \\
= & (k+1) 10^{t}+(k+1) m+s\left(10^{2 t}+2 m \cdot 10^{t}+m^{2}\right) \\
= & (k+1) 10^{t}+(k+1) m+s\left(m^{2}\right)+1+s(2 m) \\
= & (k+1) 10^{t}+[m+s(2 m)]+\left[k m+s\left(m^{2}\right)\right]+1 \\
= & (k+1) 10^{t}+[n+s(2 n)]+\left[k n+s\left(n^{2}\right)\right]+1 \\
= & (k+1) 10^{t}+(k+1) n+s\left(n^{2}\right)+1+s(2 n) \\
= & (k+1)\left(10^{t}+n\right)+s\left(\left(10^{t}+n\right)^{2}\right) .
\end{aligned}
$$

对 $(m, n) \in S_{k}, m$ 与 $n$ 的个位数不是 0 和 $5, t \in \mathbb{N}^{*}, 10^{t}>m^{2}+n^{2}, 10^{t}>$ $2 m, 10^{t}>2 n,(10, m n)=1$, 定义 $\Gamma_{2, t}: S_{k} \rightarrow S_{1-k}$ 为

$$
\Gamma_{2, t}(m, n)=\left(10^{t}-m, 10^{t}-n\right) .
$$

此时, $10 \nmid 10^{t}-m, 10 \nmid 10^{t}-n$. 我们证明 $\left(10^{t}-m, 10^{t}-n\right) \in S_{1-k}$. 事实上, 仅需注意到

$$
10^{t}-m+s\left(2\left(10^{t}-m\right)\right)=10^{t}-m+9 t+2-s(2 m)=10^{t}-n-s\left(2\left(10^{t}-n\right)\right)
$$

且

$$
\begin{aligned}
& (1-k)\left(10^{t}-m\right)+s\left(\left(10^{t}-m\right)^{2}\right) \\
= & (1-k)\left(10^{t}-m\right)+s\left(10^{2 t}-2 m \cdot 10^{t}+m^{2}\right) \\
= & (1-k)\left(10^{t}-m\right)+9 t+1-s(2 m)+s\left(m^{2}\right) \\
= & (1-k) 10^{t}+\left(k m+s\left(m^{2}\right)\right)-(m+s(2 m))+9 t+1 \\
= & (1-k) 10^{t}+\left(k n+s\left(n^{2}\right)\right)-(n+s(2 n))+9 t+1 \\
= & \left.(1-k)\left(10^{t}-n\right)+s\left(\left(10^{t}-n\right)^{2}\right)\right)
\end{aligned}
$$

现在, 注意到 $(9,12) \in S_{0}$, 即有

$$
9+s(18)=12+s(24)=18, s(81)=s(144)=9 .
$$

$k>0$ 时, 取充分大的 $t$, 对 $(9,12)$ 依次作用 $\Gamma_{1, t}, \Gamma_{1,3 t}, \cdots, \Gamma_{1,3^{k-1} t}$, 得到的像即在 $S_{k}$ 中, 从而取不同的 $t$ 即得: $S_{k}$ 有无穷个元素.

对 $k \leq 0$, 则 $1-k>0$. 取 $(m, n) \in S_{1-k}$, 由前述知 $S_{1-k}$ 为无限集. $t$ 充分大时, 有 $\Gamma_{2, t}(m, n) \in S_{k}$, 取不同的 $t$ 即知: $S_{k}$ 为无限集.

注. 本题要同时控制 $s(2 n)$ 与 $s\left(n^{2}\right)$, 恐怕难以直接构造, 但递归结构很强.另外, 由于 $n+s(2 n)=m+s(2 m)$, 故 $m, n$ 很接近, 这引导我们用形如 “ $10^{k}+n$ ”
的递归构造。

6. 给定 $n$ 个正数, 是否一定可以找到一个凸 $n+2$ 边形和它的一个三角剖分, 使得剖分三角形的直径（即三角形的最长边）为给定的 $n$ 个正数.

解. 答案是肯定的.

设给定的 $n$ 个正数为 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 作两条平行的直线 $l_{1}, l_{2}$, 其距离为 $\varepsilon(>) 0$ 待定. 取 $A_{0} \in l_{1}$, 并在 $l_{2}$ 上取 $B_{0}, B_{1}$, 使得

$$
A_{0} B_{0}=\frac{a_{1}}{2}, A_{0} B_{1}=a_{1} .
$$

注意到只要 $\varepsilon<\frac{a_{1}}{2}$, 这就是可行的, 并约定 $B_{0}, B_{1}$ 尽量靠左(如图).

![](https://cdn.mathpix.com/cropped/2024_02_26_6bb2a7c15746a751d381g-8.jpg?height=320&width=520&top_left_y=934&top_left_x=768)

待定充分小的 $\varepsilon^{\prime}>0, \delta>0$.

之后归纳地确定其余 $A_{i}, B_{j}$.

假设已有 $A_{0}, A_{1}, \cdots, A_{i} ; B_{0}, B_{1}, \cdots, B_{j}$, 使得:

(1) 其可剖分出 $i+j$ 个三角形, 直径依次为 $a_{1}, \cdots, a_{i+j}$.

(2) 其均在 $l_{1}, l_{2}$ 内侧, 且 $\varepsilon^{\prime}, \delta$ 充分小时, 各 $A_{i}$ 趋于 $l_{1}$, 各 $B_{j}$ 趋于 $l_{2}$, 其在 $l_{1}$或 $l_{2}$ 上的投影依次向左分布.

(3) $A_{k} A_{k+1}$ 与 $l_{1}$ 的夹角为 $k \delta(1 \leq k \leq i-1), B_{k} B_{k+1}$ 与 $l_{2}$ 的夹角为 $k \delta(1 \leq$ $k \leq j-1)$ 且 $A_{k} A_{k+1}=\varepsilon^{\prime}$.

下取一点 $C$, 其要么作为 $A_{i+1}$, 要么作为 $B_{j+1}$ 且使 $\triangle C A_{i} B_{j}$ 直径为 $a_{i+j+1}$,且 (2), (3) 仍满足.

![](https://cdn.mathpix.com/cropped/2024_02_26_6bb2a7c15746a751d381g-8.jpg?height=240&width=512&top_left_y=2042&top_left_x=772)

首先, $\delta, \varepsilon^{\prime}$ 充分小时, 由 (2), (3), $A_{0} A_{i} \leq i \varepsilon^{\prime}$ 可任意小, 但

$$
A_{0} B_{j} \geq A_{0} B_{0}=\frac{a_{0}}{2}
$$

故可取 $\delta, \varepsilon^{\prime}$ 使 $B_{j}$ 在 $l_{2}$ 投影在 $A_{i}$ 相应投影的左侧. 现过 $B_{j}$ 向上作射线 $l$, 其与 $l_{2}$ 夹角为 $j \delta$. 注意到 $A_{i} B_{j} \leq a_{i+j}$.
i). 若 $A_{i} B_{j}=a_{i+j+1}$. 这要求 $a_{i+j}=a_{i+j+1}$. 则取 $C$ 为 $A_{i+1}$. 使 $A_{i+1} A_{i}=\varepsilon^{\prime}$且 $A_{i+1} A_{i}$ 与 $l_{1}$ 夹角为 $i \delta, d\left(A_{i+1}, l_{1}\right)>d\left(A_{i}, l_{1}\right)$. 这样, (2), (3) 满足且 $\triangle A_{i} B_{j} A_{i+1}$直径为 $A_{i} B_{j}=a_{i+j+1}$, 因为 $\angle B_{j} A_{i+1} A_{i}$ 为钝角 (由 (2), (3) 保证).

ii). 若 $A_{i} B_{j}<a_{i+j+1}$, 则取 $C$ 为 $B_{j+1}$. 令 $C \in l$, 则 (3) 成立. 设 $B_{j} C=x$, 则欲让 $A_{i} C=a_{i+j+1}$, 仅需

$$
a_{i+j+1}^{2}=a_{i+j}^{2}+x^{2}-2 a_{i+j} x \cos \angle A_{i} B_{j} B_{j+1} .
$$

上式右边关于 $x$ 单增, 在 $x \rightarrow 0^{+}$时小于左边; 在 $x \rightarrow+\infty$ 时大于左边, 故有解 $x$, 且 $0<x<a_{i+j+1}$ (注意 (2), (3) 保证 $\varepsilon, \delta$ 充分小时, $\angle A_{i} B_{j} B_{j+1}$ 为针角). 则 $\triangle A_{i} B_{j} B_{j+1}$ 直径为 $a_{i+j+1}$, 且 $x \sin \delta \rightarrow 0$ (当 $\delta \rightarrow 0^{+}$), 故 (2) 成立.

由归纳原理, 我们定义了 $n+2$ 个点, 其满足 (1), (2), (3), 易知其为凸 $n+2$ 边形的顶点集. 由 (1) 知符合题意. 得证.

注: 本题难度不大, 表达难度很高. 在构思过程中, 首先是要将“剖分”化为“拼接”。 凸性实际上是要求内角小于 $180^{\circ}$. 故容易想到考虑出一个顶点外,其余顶点几乎共线的多边形. 但 $a_{i}=a_{i+1}$ 时会出问题, 因此需要加入一些“反向”的三角形.

