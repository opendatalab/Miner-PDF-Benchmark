# 2020 伊朗 TST（第一轮）试题解析 

梁敬勋<br>(浙江杭州学军中学, 310012<br>指导教师: 边红平

伊朗数学奥林匹克国家队选拔一般有三轮共 18 个题. 伊朗的试题总体质量很高, 有些题目难度极大, 总是给我们的竞赛选手留下深刻的印象.

本文是 2020 年伊朗国家队选拔赛 (第一轮) 试题的解答. 由于能力有限, 难免有不当疏漏之处, 敬请读者批评指正.

## I. 试 题

1. 给一个完全图的每条边赋上互不相同的正数, 使得对于图中任意一个三角形, 其某一边上的数字等于另外两边上的数字之和. 证明: 可以给这个图的每个顶点赋值, 使得每条边上的数字等于这条边两个端点上的数字之差(的绝对值).
2. 设 $\triangle A B C$ 的外心为 $O . D, E$ 分别在边 $A C, A B$ 上, $P, Q, R, S$ 是平面上的点, 满足 $P, R$ 和 $C$ 在直线 $A B$ 的异侧, $Q, S$ 和 $B$ 在直线 $A C$ 的异侧, 且 $D, A, P, R$ 共圆, $E, A, Q, S$ 共圆, $\triangle B C E \sim \triangle A D Q, \triangle C B D \sim \triangle A E P$ (顶点按此顺序对应), $\angle A R E=\angle A S D=\angle B A C$. 若 $R S / / P Q$, 证明: $R E, D S, A O$ 三线共点.
3. 我们定义一个正整数 $n$ 是 “有趣的”, 如果对 $1,2, \cdots, n$ 的任意排列 $\sigma$, 都存在多项式 $P_{1}, P_{2}, \cdots, P_{n}$ 和 $\varepsilon>0$, 满足:

(1) $P_{1}(0)=P_{2}(0)=\cdots=P_{n}(0)$;

(2) $\forall-\varepsilon<x<0, P_{1}(x)>P_{2}(x)>\cdots>P_{n}(x)$;

(3) $\forall 0<x<\varepsilon, P_{\sigma(1)}(x)>P_{\sigma(2)}(x)>\cdots>P_{\sigma(n)}(x)$.

求所有 “有趣的” 正整数 $n$.

修订日期: 2020-04-27.

4. 函数 $g:[0,1] \rightarrow \mathbb{R}$ 满足如下性质: 将区间 $[0,1]$ 任意分成两个不交的非空集合 $A, B$, 一定存在 $x \in A, g(x) \in B$ 或存在 $x \in B, g(x) \in A$. 且 $\forall x \in[0,1]$,有 $g(x)>x$. 证明: 存在无穷多个 $x \in[0,1]$ 使得 $g(x)=1$.
5. 给定整数 $k$, 证明存在无穷多互异正整数对 $(m, n)$ 满足:

$$
n+s(2 n)=m+s(2 m), k n+s\left(n^{2}\right)=k m+s\left(m^{2}\right),
$$

其中 $s$ 是数码和函数.

6. 给定 $n$ 个正数, 是否一定可以找到一个凸 $n+3$ 边形和它的一个三角剖分, 使得剖分出的各三角形外接圆直径为给定的 $n$ 个正数?

## II. 解答与评注

1. 给一个完全图的每条边赋上互不相同的正数, 使得对于图中任意一个三角形, 其某一边上的数字等于另外两边上的数字之和. 证明: 可以给这个图的每个顶点赋值, 使得每条边上的数字等于这条边两个端点上的数字之差(的绝对值).

![](https://cdn.mathpix.com/cropped/2024_02_26_8814b5469edf7aba427cg-2.jpg?height=431&width=554&top_left_y=1412&top_left_x=751)

证明 设赋值最大的边为 $e=u v$, 赋值为 $a$.

我们给顶点作如下赋值: 给点 $v$ 赋值 0 . 对 $\forall v^{\prime} \in V, v^{\prime} \neq v$, 给 $v^{\prime}$ 赋的值等于 $v v^{\prime}$ 的赋值.

下证该赋值满足要求.

任取 $v_{1}, v_{2} \in V, v_{1}, v_{2} \neq u, v$. 首先 $u$ 的赋值为 $a$. 设 $v v_{1}, u v_{1}, v v_{2}, u v_{2}$ 赋值分别为 $b, c, d, f$. 则 $v_{1}, v_{2}$ 赋值为 $b, d$.

我们验证:

(1) $u v_{1}$ 赋值 $c=|a-b|, u v_{2}$ 赋值 $f=|a-d|$;

(2) $v_{1} v_{2}$ 赋值为 $|b-d|$.

(1): 在 $\triangle u v v_{1}$ 中, 由 $a$ 的最大性, $a=b+c$. 同理, $a=d+f$. 故 (1) 成立.

(2): $\triangle v v_{1} v_{2}$ 中, 若 $v_{1} v_{2}$ 赋值非 $|b-d|$, 则只能为 $b+d$. 考察 $\triangle u v_{1} v_{2}$, 要么 $b+d=c+f$, 要么 $b+d=|c-f|$.

若为前者, 结合 $b+c=a=d+f$ 知 $b=f$, 与各边赋值不同矛盾!

若为后者, 则 $b+d=|c-f|=|b-d|$, 与 $b, d>0$ 矛盾!

故 $v_{1} v_{2}$ 赋值为 $|b-d|$.

综上, 该赋值符合.

评注 顶点的赋值几乎是确定的, 要描述顶点的赋值, 只需知道相互之间的大小. 故希望找一个最小元, 取赋值最大的边可以定位极大元与极小元.

2. 设 $\triangle A B C$ 的外心为 $O . D, E$ 分别在边 $A C, A B$ 上, $P, Q, R, S$ 是平面上的点, 满足 $P, R$ 和 $C$ 在直线 $A B$ 的异侧, $Q, S$ 和 $B$ 在直线 $A C$ 的异侧, 且 $D, A, P, R$ 共圆, $E, A, Q, S$ 共圆, $\triangle B C E \sim \triangle A D Q, \triangle C B D \sim \triangle A E P$ (顶点按此顺序对应), $\angle A R E=\angle A S D=\angle B A C$. 若 $R S \| P Q$, 证明: $R E, D S, A O$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_8814b5469edf7aba427cg-3.jpg?height=528&width=460&top_left_y=1255&top_left_x=821)

证明 我们证明 $R, S \in \odot O$.

由 $\angle P A E=\angle D C B$ 可知, $P A$ 与 $\odot O$ 相切, 即 $P A \perp A O$. 同理, $Q A \perp A O$.故 $P, A, Q$ 共线. 设直线 $A P$ 交 $\odot A R E$ 于点 $A, L$, 则 $\angle A L E=\angle A R E$. 所以 $\angle A L E=\angle C A B$, 又 $\angle L A E=\angle A C B$ 知 $\triangle A E L \sim \triangle C B A$, 且 $P, D$ 为对应点.注意到

$$
\angle R L A=\angle R L E+\angle E L A=\angle R A E+\angle E A C=\angle R A C,
$$

又 $\angle R P L=\angle R D A$, 故 $\triangle R L P \sim \triangle R A D$. 由 $\triangle A E L \sim \triangle C B A$ 及 $P, D$ 的对应关系, 结合上述相似知 $D, P$ 也为该相似的对应点. 故 $\triangle R A P \sim \triangle R C D$. 从而

$$
\angle P A R=\angle A C R \Rightarrow P A \text { 与 } \odot(C A R) \text { 相切 } \Rightarrow R \in \odot O \text {. }
$$

同理, $S \in \odot O$.
现在, $R S / / P Q$, 故 $R S \perp A O$, 从而 $A R=A S$. 又

$$
\angle E R S=\angle E R A-\angle A R S=\angle D S A-\angle A S R=\angle D S R
$$

故 $R E, S D$ 交在 $R S$ 中垂线 $A O$ 上,得证!

评注 本题难以画出标准圆, 故退而求其次, 先不看 $P Q / / R S$, 分析图形的性质. 此时作标准圆即可发现 $R, S \in \odot O$.

3. 我们定义一个正整数 $n$ 是 “有趣的”, 如果对 $1,2, \cdots, n$ 的任意排列 $\sigma$, 都存在多项式 $P_{1}, P_{2}, \cdots, P_{n}$ 和 $\varepsilon>0$, 满足:

(1) $P_{1}(0)=P_{2}(0)=\cdots=P_{n}(0)$;

(2) $\forall-\varepsilon<x<0, P_{1}(x)>P_{2}(x)>\cdots>P_{n}(x)$;

(3) $\forall 0<x<\varepsilon, P_{\sigma(1)}(x)>P_{\sigma(2)}(x)>\cdots>P_{\sigma(n)}(x)$.

求所有“有趣的”正整数 $n$.

解 所求有趣的正整数 $n$ 为 $1,2,3$.

对一个非零多项式 $f(x)=\sum_{k=0}^{m} a_{k} x^{k}$, 称使 $a_{k} \neq 0$ 的最小的 $k$ 对应的项 $a_{k} x^{k}$称为 $f$ 的 “特征”. 显然, $|x|$ 充分小时 $f(x)$ 的正负取决于 $f$ 的特征的正负.

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
P_{3}(x)-P_{4}(x)>0 \Rightarrow Q_{1}(x)+Q_{2}(x)>0 \Rightarrow x^{\alpha_{2}}>0
$$

$$
P_{2}(x)-P_{3}(x)>0 \Rightarrow Q_{1}(x)+Q_{2}(x)+Q_{3}(x)<0 \Rightarrow x^{\alpha_{2}}<0
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

评注 本题容易想到用差分的特征来判断正负. 但是引入 $Q_{i}=P_{\sigma(i)}-P_{\sigma(i+1)}$会使 $P_{i}-P_{i+1}$ 表示起来不方便. 本题的关键是各 $Q_{i}$ 的特征都是正系数的, 从而使加式中特征不会相互抵消, 使得 $P_{i}-P_{i+1}$ 有可能研究.

4. 函数 $g:[0,1] \rightarrow \mathbb{R}$ 满足如下性质: 将区间 $[0,1]$ 任意分成两个不交的非空集合 $A, B$, 一定存在 $x \in A, g(x) \in B$ 或存在 $x \in B, g(x) \in A$. 且 $\forall x \in[0,1]$,有 $g(x)>x$. 证明: 存在无穷多个 $x \in[0,1]$ 使得 $g(x)=1$.

证明 反证法, 若仅有有限个 $x \in[0,1]$ 使 $g(x)=1$, 记这些 $x$ 组成集合 $S$.

首先, $S \neq \emptyset$. 否则, 取 $A=\{1\}, B=[0,1)$, 由题意, 要么存在 $x \in A, g(x) \in B$或存在 $x \in B, g(x) \in A$. 注意到 $g(x)>x, \forall x \in[0,1]$. 故存在 $x \in B, g(x) \in A$,此时 $g(x)=1$, 矛盾!

其次, 由 $g(x)>x, \forall x \in[0,1]$, 知 $1 \notin S$.

设 $S$ 的最大元为 $\alpha$. 取

$$
A=\left\{x \mid x \in[0,1] \text { 且存在 } k \in \mathbb{N}^{*} \text { 使 } g^{(k)}(x)=1\right\} \text {, }
$$

其中 $g^{(k)}=\underbrace{g \circ \cdots \circ g}_{k \text { 个 } g}$. 则 $A$ 非空集, 记 $A^{*}=A \cup\{1\}$.
任取 $x \in A$, 有

$$
g^{(k)}(x)=1 \Rightarrow g^{(k-1)}(x) \leq \alpha \Rightarrow x \leq \alpha<1
$$

取 $B=[0,1] \backslash A^{*}$, 则 $B \neq \emptyset$. 由题意, 要么存在 $x \in A^{*}, g(x) \in B$ 或存在 $x \in B, g(x) \in A^{*}$.

若为前者, 由 $x \in A^{*}$, 设 $g^{(k)}(x)=1($ 显然 $x \neq 1), k \in \mathbb{N}^{*}$. 由 $1 \notin B$ 知, $k \geq 2$. 故 $g^{(k-1)}(g(x))=1$, 从而 $g(x) \in A$, 矛盾!

若为后者, 由 $A$ 的定义知, $g(x) \neq 1$. 由 $g(x) \in A$, 设 $g^{(k)}(g(x))=1, k \in \mathbb{N}^{*}$,即 $g^{(k+1)}(x)=1$, 故 $x \in A$, 矛盾!

综上, 反证假设不成立, $S$ 为无限集.

评注 要充分利用条件必须取习钻的 $A, B$. 因此想到反证法就很容易.

5. 给定整数 $k$, 证明存在无穷多互异正整数对 $(m, n)$ 满足:

$$
n+s(2 n)=m+s(2 m), \quad k n+s\left(n^{2}\right)=k m+s\left(m^{2}\right),
$$

其中 $s$ 是数码和函数.

证明 首先注意到一个事实:

设 $n \in \mathbb{N}^{*}, n$ 的个位数不是 0 和 $5, t \in \mathbb{N}^{*}, 10^{t}>2 n$, 则

$$
s\left(10^{t}-n\right)=9 t+1-s(n), s\left(2\left(10^{t}-n\right)\right)=9 t+2-s(2 n) \text {. }
$$

事实上, 设 $n=\left(\overline{a_{1} a_{2} \cdots a_{t}}\right)_{10}, a_{i} \in \mathbb{N}, 0 \leq a_{i} \leq 9$, 则 $a_{t} \neq 0$. 从而

$$
10^{t}-n=\left(\overline{\left(9-a_{1}\right)\left(9-a_{2}\right) \cdots\left(9-a_{t-1}\right)\left(10-a_{t}\right)}\right)_{10} .
$$

设 $2 n=\left(\overline{b_{1} b_{2} \cdots b_{t}}\right)_{10} ，$

$$
2\left(10^{t}-n\right)=2 \cdot 10^{n}-2 n=\left(\overline{1\left(9-b_{1}\right)\left(9-b_{2}\right) \cdots\left(9-b_{t-1}\right)\left(10-b_{t}\right)}\right)_{10} .
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

$10^{t}-m+s\left(2\left(10^{t}-m\right)\right)=10^{t}-m+9 t+2-s(2 m)=10^{t}-n-s\left(2\left(10^{t}-n\right)\right)$

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
9+s(18)=12+s(24)=18, s(81)=s(144)=9 \text {. }
$$

$k>0$ 时, 取充分大的 $t$, 对 $(9,12)$ 依次作用 $\Gamma_{1, t}, \Gamma_{1,3 t}, \cdots, \Gamma_{1,3^{k-1} t}$, 得到的像即在 $S_{k}$ 中, 从而取不同的 $t$ 即得: $S_{k}$ 有无穷个元素.

对 $k \leq 0$, 则 $1-k>0$. 取 $(m, n) \in S_{1-k}$, 由前述知 $S_{1-k}$ 为无限集. $t$ 充分大
时, 有 $\Gamma_{2, t}(m, n) \in S_{k}$, 取不同的 $t$ 即知: $S_{k}$ 为无限集.

评注 本题要同时控制 $s(2 n)$ 与 $s\left(n^{2}\right)$, 恐怕难以直接构造, 但递归结构很强.另外, 由于 $n+s(2 n)=m+s(2 m)$, 故 $m, n$ 很接近, 这引导我们用形如 “ $10^{k}+n$ ”的递归构造。

6. 给定 $n$ 个正数, 是否一定可以找到一个凸 $n+3$ 边形和它的一个三角剖分, 使得剖分出的各三角形外接圆直径为给定的 $n$ 个正数?

## 解 答案是肯定的.

设题设的 $n$ 个正数为 $d_{1} \leq d_{2} \leq \cdots \leq d_{n}$. 取 $t_{k}=d_{1}-\varepsilon k, k=1,2, \cdots, n+1$.其中 $\varepsilon>0$ 待定. 令 $\varepsilon$ 充分小, 使 $t_{n+1}>0$.

下作 $n$ 个三角形 $\triangle A_{k} B_{k} C_{k}, k=1,2, \cdots, n$. 作直径为 $d_{k}$ 的圆 $\omega_{k}$. 任取 $A_{k} \in \omega_{k}$. 由于 $t_{k}<d_{1} \leq d_{k}$, 可取 $C_{k} \in \omega_{k}$ 使 $A_{k} C_{k}=t_{k}$. 在劣弧 $A_{k} C_{k}$ 内取点 $B_{k}$, 使 $A_{k} B_{k}=t_{k+1}$. 不妨设 $A_{k}, B_{k}, C_{k}$ 逆时针排列.

按如下方式连接各三角形:

注意到 $A_{k} B_{k}=A_{k+1} C_{k+1}=t_{k+1}$, 将各三角形平移使各 $A_{1}, A_{2}, \cdots, A_{n+1}$ 重合于同一点 $O$, 绕 $O$ 转动各三角形, 使 $A_{k} B_{k}$ 与 $A_{k+1} C_{k+1}$ 重合 $(1 \leq k \leq n-1)$.如此得到一个 $n+3$ 边形 $\Omega$. 下证: 可取 $\varepsilon$ 充分小, 使 $\Omega$ 为凸多边形.
![](https://cdn.mathpix.com/cropped/2024_02_26_8814b5469edf7aba427cg-8.jpg?height=440&width=1058&top_left_y=1545&top_left_x=473)

一方面, $\varepsilon \rightarrow 0^{+}$时, $\angle B_{k} A_{k} C_{k} \rightarrow 0^{+}$. 故 $\varepsilon \rightarrow 0^{+}$时, $\angle C_{1} O B_{n} \rightarrow 0^{+}(<\pi)$.

另一方面, 考察 $\angle C_{k} B_{k} B_{k+1}$. 要让 $\angle C_{k} B_{k} A_{k}+\angle A_{k+1} C_{k+1} B_{k+1} \leq \pi$.

设 $\omega_{k}$ 中 $A_{k} B_{k}$ 所对圆心角为 $2 \alpha_{k}\left(0<\alpha_{k}<\frac{\pi}{2}\right)$, 则

$$
t_{k+1}=d_{k} \sin \alpha_{k}
$$

$\varepsilon \rightarrow 0^{+}$时, $C_{k} \rightarrow B_{k}, B_{k} C_{k}$ 趋于圆 $\omega_{k}$ 在 $B_{k}$ 处的切线, 故 $\angle A_{k} B_{k} C_{k}$ 趋于 $\pi-\alpha_{k}$.同理, $\angle A_{k+1} C_{k+1} B_{k+1}$ 趋于 $\alpha_{k+1}$.

设 $\theta_{k}=\lim _{\varepsilon \rightarrow 0^{+}} \alpha_{k}$ (注意 $\alpha_{k}$ 为 $\varepsilon$ 的连续函数, 但 $\theta_{k}$ 为定值), 则 $\theta_{k}>0$, 且由 (1)
知, $d_{1}=d_{k} \sin \theta_{k}$, 令 $\varepsilon \rightarrow 0^{+}$, 则由 $d_{k} \leq d_{k+1}$ 知, $\theta_{k} \geq \theta_{k+1}$. 故

$$
\angle A_{k} B_{k} C_{k}+\angle A_{k+1} C_{k+1} B_{k+1} \rightarrow \pi-\theta_{k}+\theta_{k+1}<\pi\left(\varepsilon \rightarrow 0^{+}\right)
$$

从而可取充分小的 $\varepsilon$ 使 $\Omega$ 为凸多边形.

现在, $\Omega$ 是凸 $n+3$ 边形, 且各 $\triangle A_{k} B_{k} C_{k}$ 形成 $\Omega$ 的剖分, 外接圆直径分别为 $d_{1}, d_{2}, \cdots, d_{n}$. 故答案是肯定的.

评注 本题违背直观的一点在于 $\triangle A_{k} B_{k} C_{k}$ 尺寸随 $k$ 变小, 而外接圆半径随 $k$ 变大. 但其与本题的目标相容得很好: 尺寸近似时, 外接圆半径越大的三角形越“钝” (有一个很大的内角), 越适合放在凸多边形的角上.

