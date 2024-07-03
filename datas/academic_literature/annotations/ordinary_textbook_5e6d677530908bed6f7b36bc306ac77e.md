# 2022 年北大数学学科探究拓展活动试题解答与评析 

习子博

(湖南省长沙市长郡中学, 410221)

指导教师: 陈家烦

2022 年 11 月 19 日和 20 日进行了两场考试, 每天上午各一场, 每场考 4 道题, 共 8 题. 试题第二天明显难于第一天, 其中第 $3,7,8$ 是困难题, 第 4 题有一定难度, 第 $1,2,5,6$ 题属于简单题. 笔者水平有限, 本文给出的解答不当之处敬请批评指正.

## I. 试 题

1. 多项式序列 $P_{n}(x)$ 满足

$$
P_{0}(x)=0, P_{1}(x)=x, P_{n}(x)=\left(P_{n-1}(x)\right)^{3}+2 P_{n-1}(x)-P_{n-2}(x)+2022 .
$$

求 $P_{n}(x)$ 的正实根和负实根的个数.

2. 锐角 $\triangle A B C$ 中, 垂心为 $H$. 以 $B C$ 为直径的圆 $\omega$ 上一点 $D$ 满足 $D B<$ $D C$ 且 $D H / / B C, D H$ 垂直平分线交 $\omega$ 于点 $E, F . \angle E H F$ 与其邻补角的平分线分别交 $A C, A B$ 于点 $J, K$. 求证: $J K$ 平分 $A H$.
3. 求证: 对任意整数 $t$, 存在互不相同的素数 $p_{1}, p_{2}, p_{3}$ 和正整数 $\alpha_{1}, \alpha_{2}, \alpha_{3}$满足:

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv t \quad\left(\bmod p_{1} p_{2} p_{3}\right)
$$

4. 称一个集合 $A$ 是超级的, 如果它满足 $|A+A|=|A-A|$. 其中

$$
A+A=\{x+y \mid x \in A, y \in A\}, A-A=\{x-y \mid x \in A, y \in A\} .
$$

求证: 存在正常数 $c$ 使得对任意正整数 $n$, 至少存在 $\left[c \cdot 2^{n}\right]$ 个 $\{0,1,2, \cdots, n-1\}$的子集是超级的.

修订日期: 2023-03-06.

5. 称平面上一个闭图形是好的, 如果它是凸的且内部不含格点. 称一个好的闭图形是极好的, 如果它不被任何好的闭图形真包含. 求证: 极好的有界闭图形是三角形或四边形.
6. 对于正整数 $n$, 小于或等于 $n$ 且与 $n$ 互质的正整数 (包括 1 ) 的个数, 记作 $\phi(n)$, 称为欧拉函数. 求证：对于任意正整数 $n>1, \phi(1), \phi(2), \cdots, \phi(n)$ 可以分成和相同的两组.
7. $G$ 为一个无向简单图,

$$
|V(G)|=400,|E(G)|=20000 \text {. }
$$

求证: 存在 $G$ 的顶点集的二分划 $V(G)=V_{1} \bigcup V_{2}$, 使得

$$
\left|E\left(V_{i}\right)\right| \leq 5024, \quad i=1,2
$$

8. 数列 $\left\{a_{n}\right\}$ 满足

$$
a_{0}=1, a_{n+1}=\sum_{\substack{i, j, k \geq 0 \\ i+j+k=n}} a_{i} a_{j} a_{k}
$$

对任意 $n \geq 0$ 成立. 求数列 $\left\{a_{n}\right\}$ 的通项.

## II. 解答与评注

题 1 多项式序列 $P_{n}(x)$ 满足

$$
P_{0}(x)=0, P_{1}(x)=x, P_{n}(x)=\left(P_{n-1}(x)\right)^{3}+2 P_{n-1}(x)-P_{n-2}(x)+2022 .
$$

求 $P_{n}(x)$ 的正实根和负实根的个数.

## 解 答案为

$P_{n}(x)$ 正实根有 $\left\{\begin{array}{ll}\text { 无穷个 }, \quad n=0 \\ 0 \text { 个 }, \quad n \geq 1\end{array} \quad, P_{n}(x)\right.$ 负实根有 $\begin{cases}\text { 无穷个, } & n=0 \\ 0 \text { 个, } & n=1 \\ 1 \text { 个, } & n \geq 2\end{cases}$

$n=0$ 时, 任意 $x \in \mathbb{R}$ 均为 $P_{0}(x)=0$ 的根, 故 $P_{0}(x)$ 有无穷多个正实根及负实根.

下对 $n$ 归纳证明

$$
P_{n}^{\prime}(x)>0 \text { 且 } P_{n}^{\prime}(x)>P_{n-1}^{\prime}(x), \quad n \in \mathbb{N}^{+}
$$

对任意 $x \in \mathbb{R}$ 成立.
对 $n$ 归纳, $n=1$ 时

$$
P_{1}^{\prime}(x)=1>0, P_{1}^{\prime}(x)>P_{0}^{\prime}(x)=0 .
$$

设 $k=n-1$ 时上述结论成立, $k=n$ 时,

$$
\begin{aligned}
P_{n}^{\prime}(x) & =\left(\left(P_{n-1}(x)\right)^{3}+2 P_{n-1}(x)-P_{n-2}^{\prime}(x)+2022\right) \\
& =3 P_{n-1}^{\prime}(x) P_{n-1}^{2}(x)+2 P_{n-1}^{\prime}(x)-P_{n-2}^{\prime}(x) .
\end{aligned}
$$

由归纳假设, $P_{n-1}^{\prime}(x)>0$, 而 $P_{n-1}^{2}(x) \geq 0$, 则

$$
\begin{aligned}
P_{n}^{\prime}(x) & \geq 2 P_{n-1}^{\prime}(x)-P_{n-2}^{\prime}(x) \\
& =P_{n-1}^{\prime}(x)+\left(P_{n-1}^{\prime}(x)-P_{n-2}^{\prime}(x)\right) \\
& >P_{n-1}^{\prime}(x) .(\text { 归纳假设 })
\end{aligned}
$$

故 $k=n$ 时结论成立.

因此对任意 $n \geq 1, P_{n}^{\prime}(x)$ 单调递增, 故 $P_{n}(x)$ 至多一个实根. 而

$$
\operatorname{deg} P_{n}(x)=3 \cdot \operatorname{deg} P_{n-1}(x)=3^{n-1} \cdot \operatorname{deg} P_{1}(x)=3^{n-1}
$$

故 $P_{n}(x)$ 至少有一个实根. 故 $P_{n}(x)(n \geq 1)$ 恰有一个实根.

下再对 $n$ 归纳证明 $n \geq 2$ 时,

$$
P_{n}(0)>P_{n-1}(0) \text { 且 } P_{n}(0)>0 \text {. }
$$

对 $n$ 归纳, $n=2$ 时

$$
P_{2}(x)=x^{3}+2 x+2022, P_{2}(0)=2022>0=P_{1}(0),
$$

结论成立.

设 $k=n-1$ 时结论成立, $k=n(n \geq 3)$ 时.

由归纳假设 $P_{n-1}(x) \geq 0$, 于是

$$
\begin{aligned}
P_{n}(0) & =\left(P_{n-1}(0)\right)^{3}+2 P_{n-1}(0)-P_{n-2}(0)+2022 \\
& >2 P_{n-1}(0)-P_{n-2}(0) \\
& >P_{n-1}(0) . \text { (归纳假设) }
\end{aligned}
$$

即 $n$ 时结论成立.

于是 $n \geq 2$ 时, 对任意 $x \in \mathbb{R}_{+}$有

$$
P_{n}(x)>P_{n}(0)>0
$$

因此 $n \geq 2$ 时 $P_{n}(x)$ 的实根必为负实根.

$n=1$ 时 $P_{1}(x)=0 \Leftrightarrow x=0$, 即 $P_{1}(x)$ 无正实根及负实根.
综上所述:

$$
P_{n}(x) \text { 正实根有 }\left\{\begin{array} { l l } 
{ \text { 无穷个 } , \quad n = 0 } \\
{ 0 \text { 个, } \quad n \geq 1 }
\end{array} \quad , P _ { n } ( x ) \text { 负实根有 } \left\{\begin{array}{ll}
\text { 无穷个, } & n=0 \\
0 \text { 个, } & n=1 \text {. } \\
1 \text { 个, } & n \geq 2
\end{array}\right.\right.
$$

评注 本题是一个简单的代数多项式题, 稍作思考就知从导数入手, 用归纳法证明 $P_{n}(x)$ 单调递增及 $P_{n}(0)>0(n \geq 2)$ 即可.

题 2 锐角 $\triangle A B C$ 中, 垂心为 $H$. 以 $B C$ 为直径的圆 $\omega$ 上一点 $D$ 满足 $D B<D C$ 且 $D H / / B C, D H$ 垂直平分线交 $\omega$ 于点 $E, F . \angle E H F$ 与其邻补角的平分线分别交 $A C, A B$ 于点 $J, K$. 求证: $J K$ 平分 $A H$.

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-04.jpg?height=682&width=614&top_left_y=1104&top_left_x=687)

证明 1 设 $D, H$ 关于 $B C$ 对称点为 $D^{\prime}, H^{\prime}$, 则 $D^{\prime} \in \omega$.

设 $B X \perp A C$ 于 $X, C Y \perp A B$ 于 $Y, A Z \perp B C$ 于 $Z$, 则 $A, H, Z, H^{\prime}$ 共线. 由 $H, H^{\prime}$ 关于 $B C$ 对称, 知 $H^{\prime}$ 在 $\triangle A B C$ 外接圆上.

设 $A H$ 中点为 $M, \angle E H F$ 角分线交 $E F$ 于 $L$. 由 $D, H$ 关于 $E F$ 对称, 结合角平分线定理,

$$
\frac{E H}{H F}=\frac{E L}{L F}=\frac{E D}{D F}
$$

故 $D L$ 平分 $\angle E D F$.

又由于 $E F \perp D H, D H / / B C$, 有 $E F \perp B C$. 因此 $C$ 为弧 $(E C F)$ 中点, 所以 $D C$ 平分 $\angle E D F$. 由此可得 $D, L, C$ 共线.
此时

$$
\begin{aligned}
\angle L C D^{\prime} & =\angle D C D^{\prime}=2 \angle D C B=2 \angle L D H \quad(B C / / D H) \\
& =\angle L D H+\angle L H D(L D=L H)=\angle H L C .
\end{aligned}
$$

因此 $H L / / C D^{\prime}$. 故 $B D^{\prime}$ 平行于 $\angle E H F$ 外角平分线 $H K$.

设

$$
H J \cap D^{\prime} B=P, K H \cap C D^{\prime}=Q .
$$

由

$$
H P / / D^{\prime} Q, H Q / / P D^{\prime},
$$

知

$$
\angle P D^{\prime} Q=\angle B D^{\prime} C=90^{\circ} \text {. }
$$

故 $H P D^{\prime} Q$ 为矩形, 因此 $H, P, D^{\prime}, Q$ 共圆.

以 $H$ 为中心, $-A H \cdot H Z$ 为幂进行反演, 则 $A, Z$ 互反, $C, Y$ 互反, $B, X$ 互反. 由 $M$ 为 $A H$ 中点, 又 $Z$ 为 $H H^{\prime}$ 中点, 知 $M$ 反演点为 $H^{\prime}$. 由

$$
H P \perp P B, H X \perp X J
$$

知 $B P X J$ 共圆. 故 $J, P$ 互反, 同理 $K, Q$ 互反. 故

$$
K, M, J \text { 共线 } \Leftrightarrow H, P, Q, H^{\prime} \text { 共圆. }
$$

由 $D^{\prime}, H^{\prime}$ 与 $D, H$ 关于 $B C$ 对称, 有 $D^{\prime} H^{\prime} / / B C$. 因此由 $H H^{\prime} \perp B C$, 知 $H H^{\prime} \perp$ $H^{\prime} D^{\prime}$, 而

$$
H Q \perp Q D^{\prime}, H P \perp P D^{\prime}
$$

有 $H, P, D^{\prime}, H^{\prime}, Q$ 共圆. 因此 $K, M, J$ 共线, 即 $K J$ 平分 $A H$, 证毕.

证明 2 (龙泽鍂) 设 $A H$ 中点为 $M, E F$ 中点为 $N$. 延长 $K H, J H$ 分别交直线 $B C$ 于 $X, Y$. 连接 $Y F, X F, E D, E H, E B, E X, N H$.

由 $B C$ 为 $E F$ 的中垂线, 有 $E Y=Y F$. 又由题意, $Y H$ 为 $\angle E H F$ 的平分线,则有 $E, H, F, Y$ 四点共圆. 同理, $E, Y, X, F$ 四点公圆. 故 $E, H, X, F, Y$ 五点共圆. 因此

$$
\angle E B F=\angle E D F=\angle E H F=\angle E X F \text {. }
$$

故 $B, X$ 关于 $N$ 对称. 同理, $C, Y$ 关于 $N$ 对称. 由

$$
K H \perp H Y, A H \perp Y C,
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-06.jpg?height=734&width=734&top_left_y=198&top_left_x=661)

故 $\angle A H K=\angle H Y C$.

又知 $\angle K A H=\angle H C Y$, 则有

$$
\triangle A K H \sim \triangle C H Y \quad(M, N \text { 分别为对应边中点), }
$$

故 $\angle A M K=\angle H N C$. 同理, 有

$$
\triangle H A J \sim \triangle X B H \quad(M, N \text { 分别为对应边中点 }),
$$

故

$$
\angle H M J=\angle H N X=\angle H N C=\angle A M K .
$$

又 $A, M, H$ 共线, 则有 $K, M, J$ 共线. 得证.

评注 本题是一个难度偏中下的几何题, 方法一是用消点法, 思考如何将 $K$, $J$ 转化为较好的点, 以 $H$ 为中心反演, 从而通过共圆解决共线问题. 方法二是考虑图形中的相似, 通过相似对应从而解决问题.

题 3 求证: 对任意整数 $t$, 存在互不相同的素数 $p_{1}, p_{2}, p_{3}$ 和正整数 $\alpha_{1}, \alpha_{2}, \alpha_{3}$ 满足:

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv t \quad\left(\bmod p_{1} p_{2} p_{3}\right)
$$

证明 先考虑 $t=1,2,3$ 的情形.

当 $t=1$ 时, 取

$$
p_{1}=3, p_{2}=5, p_{3}=53, \alpha_{1}=1, \alpha_{2}=5, \alpha_{3}=1 \text {, }
$$

此时

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv 1 \quad(\bmod 3 \cdot 5 \cdot 53) .
$$

当 $t=2$ 时, 取

$$
\begin{gathered}
p_{1}=2, p_{2}=3, p_{3}=5, \\
\alpha_{1}=(3-1)(5-1), \alpha_{2}=(2-1)(5-1), \alpha_{3}=(2-1)(3-1),
\end{gathered}
$$

此时由 Fermat 小定理知

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv 2 \quad(\bmod 2 \cdot 3 \cdot 5)
$$

当 $t=3$ 时, 取

$$
p_{1}=3, p_{2}=5, p_{3}=7, \alpha_{1}=4, \alpha_{2}=3, \alpha_{3}=1 \text {, }
$$

此时

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv 3 \quad(\bmod 3 \cdot 5 \cdot 7) .
$$

在 $t \neq 1,2,3$ 时有 $|t-2| \geq 2$, 即 $t-2$ 有质因子. 下面分三种情况讨论:

(1) $t-2$ 有至少 3 个不同质因子, 记为 $p_{1}, p_{2}, p_{3}$. 此时

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv t \quad\left(\bmod p_{1} p_{2} p_{3}\right)
$$

等价于

$$
p_{1}\left|p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}}-2, p_{2}\right| p_{1}^{\alpha_{1}}+p_{3}^{\alpha_{3}}-2, p_{3} \mid p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-2
$$

令

$$
\left(p_{2}-1\right)\left(p_{3}-1\right)\left|\alpha_{1},\left(p_{1}-1\right)\left(p_{3}-1\right)\right| \alpha_{2},\left(p_{1}-1\right)\left(p_{2}-1\right) \mid \alpha_{3},
$$

由 Fermat 小定理知上述三式皆成立. 即原结论成立.

(2) $t-2$ 恰有 2 个不同质因子, 记为 $p_{1} p_{2}$. 设

$$
t-2=\varepsilon p_{1}^{k_{1}} \cdot p_{2}^{k_{2}}\left(\varepsilon \in\{-1,1\}, k_{1}, k_{2} \in \mathbb{Z}^{+}\right),
$$

下选取 $p_{3}$, 使

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv t \quad\left(\bmod p_{1} p_{2} p_{3}\right)
$$

此时需满足如下三个等式同时成立.

$$
\begin{aligned}
& p_{1} \mid p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}}-2 \\
& p_{2} \mid p_{1}^{\alpha_{1}}+p_{3}^{\alpha_{3}}-2 \\
& p_{3} \mid p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-t
\end{aligned}
$$

令

$$
p_{2}-1\left|\alpha_{1}, p_{1}-1\right| \alpha_{2},\left(p_{1}-1\right)\left(p_{2}-1\right) \mid \alpha_{3},
$$

由 Fermat 小定理知 (1)(2) 式成立. 而

$$
(3) \Leftrightarrow p_{3} \mid p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-\varepsilon p_{1}^{k_{1}} p_{2}^{k_{2}}-2,
$$

其中 $\varepsilon \in\{-1,1\}$. 因为

$$
p_{2}-1\left|\alpha_{1}, p_{2}\right| p_{1}^{\alpha_{1}}-1
$$

所以

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-\varepsilon p_{1}^{k_{1}} p_{2}^{k_{2}}-1 \equiv 0 \quad\left(\bmod p_{2}\right)
$$

其中 $\varepsilon \in\{-1,1\}$. 故

$$
\left(p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-\varepsilon p_{1}^{k_{1}} p_{2}^{k_{2}}-2, p_{1} p_{2}\right)=1
$$

其中 $\varepsilon \in\{-1,1\}$.

选取 $\alpha_{1}$ 使

$$
\alpha_{1}>k_{1}+k_{2}+1, \alpha_{2}>k_{1}+k_{2}+1
$$

则

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-\varepsilon p_{1}^{k_{1}} p_{2}^{k_{2}}-2>0
$$

选取 $p_{3}$ 为

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-\varepsilon p_{1}^{k_{1}} p_{2}^{k_{2}}-2
$$

的质因子, 其中 $\varepsilon \in\{-1,1\}$.

此时 $p_{1}, p_{2}, p_{3}$ 互不相同, (1)(2)(3) 式皆成立. 即原结论成立.

(3) $t-2$ 恰有 1 个质因子, 记为 $p_{1}$. 设

$$
t-2=\varepsilon p_{1}^{k}
$$

其中 $\varepsilon \in\{-1,1\}$, 下选取 $p_{2}, p_{3}$, 使

$$
\begin{gathered}
p_{1} \mid p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}}-2 \\
p_{2} \mid p_{1}^{\alpha_{1}}+p_{3}^{\alpha_{3}}-\varepsilon p_{1}^{k}-2(\varepsilon \in\{-1,1\}) \\
p_{3} \mid p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}-\varepsilon p_{1}^{k}-2(\varepsilon \in\{-1,1\})
\end{gathered}
$$

同时即可.

令

$$
\left(p_{1}-1\right)\left(p_{3}-1\right)\left|\alpha_{2},\left(p_{1}-1\right)\left(p_{2}-1\right)\right| \alpha_{3}
$$

由 Fermat 小定理,

$$
p_{1} p_{3}\left|p_{2}^{\alpha_{2}}-1, p_{1} p_{2}\right| p_{3}^{\alpha_{3}}-1
$$

故 (4) 式成立.

(5)(6)式成立 $\Leftrightarrow p_{2} p_{3} \mid p_{1}^{\alpha_{1}} \pm p_{1}^{k}-1$ $\Leftrightarrow$ 存在 $\alpha_{1} \in \mathbb{Z}^{+}$使 $p_{1}^{\alpha_{1}} \pm p_{1}^{k}-1$ 有至少 2 个不同质因子

其中

$$
\left(\left(p_{1}^{\alpha_{1}} \pm p_{1}^{k}-1, p_{1}\right)=1\right) .
$$

令 $\pm p_{1}^{k}-1=s \in \mathbb{Z}$, 有 $\left(s, p_{1}\right)=1$. 下证存在 $\alpha_{1} \in \mathbb{Z}^{+}, p_{1}^{\alpha_{1}}+s$ 至少 2 个不同质因子.

用反证法, 若这样的 $\alpha_{1}$ 不存在. 此时, 存在 $u>0$ 使 $p_{1}^{u}+s>2$, 故 $p_{1}^{u}+s$ 有质因子 $q \neq p$, 因此存在 $l \in \mathbb{Z}^{+}, p_{1}^{u}+s=q^{l}$, 令

$$
\varphi\left(q^{l+1}\right) \mid \alpha_{1}-u\left(\alpha_{1}>u\right)
$$

则

$$
\begin{aligned}
\varphi\left(q^{l+1}\right) \mid \alpha_{1}-u & \Rightarrow q^{l+1} \mid p^{\alpha_{1}-u}-1 \\
& \Rightarrow q^{l+1} \mid p^{\alpha_{1}-u}-1 \\
& \Rightarrow q^{l+1} \mid p^{\alpha_{1}}-p_{1}^{u} \\
& \Rightarrow q^{l} \mid p_{1}^{\alpha_{1}}-p_{1}^{u}+p_{1}^{u}+s=p_{1}^{\alpha_{1}}+s .
\end{aligned}
$$

而

$$
p^{\alpha_{1}}+s>p_{1}^{u}+s=q^{l},
$$

故 $p_{1}^{\alpha_{1}}+s$ 除 $q$ 外有其他质因子, 与反设矛盾.

因此总存在 $\alpha_{1} \in \mathbb{Z}^{+}, p_{1}^{\alpha_{1}} \pm p_{1}^{k}-1$ 有至少 2 个不同质因子. 令 $p_{2}, p_{3}$ 为这其中 2 个质因子, 则 $\left(p_{1}, p_{2}, p_{3}, \alpha_{1}, \alpha_{2}, \alpha_{3}\right)$ 符合 (4)(5)(6) 式. 即

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv t \quad\left(\bmod p_{1} p_{2} p_{3}\right)
$$

故原结论成立.

综上所述, 对任意 $t \in \mathbb{Z}$, 总存在不同质数 $p_{1}, p_{2}, p_{3}$ 及 $\alpha_{1}, \alpha_{2}, \alpha_{3} \in \mathbb{Z}^{+}$, 有

$$
p_{1}^{\alpha_{1}}+p_{2}^{\alpha_{2}}+p_{3}^{\alpha_{3}} \equiv t \quad\left(\bmod p_{1} p_{2} p_{3}\right)
$$

证毕.

评注 笔者开始时和多数人一样, 会想从原根及狄利克雷大定理中获得一些结果, 或是取特定几组 $p_{1}, p_{2}, p_{3}$ 直接解决问题, 如取 $(5,7,23)$ 或 $(7,11,17)$.但在本质上 $p_{1}, p_{2}, p_{3}$ 是难以控制的, 从而先控制 $\alpha_{1}, \alpha_{2}, \alpha_{3}$, 通过费马小定理解决 $p_{1}, p_{2}, p_{3}$ 的选取与模数.
题 4 称一个集合 $A$ 是超级的, 如果它满足 $|A+A|=|A-A|$. 其中

$$
A+A=\{x+y \mid x \in A, y \in A\}, A-A=\{x-y \mid x \in A, y \in A\} .
$$

求证: 存在正常数 $c$ 使得对任意正整数 $n$, 至少存在 $\left[c \cdot 2^{n}\right]$ 个 $\{0,1,2, \cdots, n-1\}$的子集是超级的.

## 证明 先证一个引理.

引理 存在正常数 $c>0$, 使 $\{0,1, \cdots, n-1\}(n>200)$ 至少有 $\left[c \cdot 2^{n}\right]$ 个子集 $A$, 使

$$
\begin{gathered}
A+A=\{0,1, \cdots, 2(n-1)\} \\
A-A=\{-(n-1),-(n-2), \cdots,-1,0,1,2, \cdots, n-1\}
\end{gathered}
$$

此时

$$
|A+A|=|A-A|=2 n-1
$$

引理证明 记

$$
\begin{gathered}
X=\{0,1,2, \cdots, 2(n-1)\} \\
Y=\{-(n-1),-(n-2), \cdots,-1,0,1,2, \cdots, n-1\}
\end{gathered}
$$

令

$$
0,1,2 \cdots, 100 \text { 及 } n-101, n-100, \cdots, n-1 \in A \text {, }
$$

这样的 $A$ 有 $\frac{2^{n}}{2^{202}}$ 个.

对 101, 102, $\cdots, n-102$ 中每一个元素独立的有 $\frac{1}{2}$ 的概率在 $A$ 中. 此时有

$$
0,1,2, \cdots, 200 \text { 及 } 2 n-202,2 n-201, \cdots, 2(n-1) \in A+A \text {. }
$$

若在 $201 \leq i \leq n-1$ 时有 $i \notin A+A$, 则

并非 $A$ 的子集,

$$
\{0, i\},\{1, i-1\}, \cdots,\left\{\left[\frac{i}{2}\right], i-\left[\frac{i}{2}\right]\right\}
$$

$P_{r}(\{j, i-j\}$ 不包含于 $A) \leq 1-\left(\frac{1}{2}\right)^{2}=\frac{3}{4} . \quad\left(0 \leq j \leq\left[\frac{i}{2}\right]\right)$.

故

$$
P_{r}(i \notin(A+A)) \leq\left(\frac{3}{4}\right)^{\left[\frac{i}{2}\right]+1} \leq\left(\frac{3}{4}\right)^{\left[\frac{i}{2}\right]}
$$

同理, 在 $n \leq i \leq 2 n-203$ 时, 需满足

$$
\{n-1, i-(n-1)\}, \cdots,\left\{\left[\frac{i}{2}\right], i-\left[\frac{i}{2}\right]\right\}
$$

并非 $A$ 的子集, 故

$$
P_{r}(i \notin(A+A)) \leq\left(\frac{3}{4}\right)^{n-\left[\frac{i}{2}\right]} .
$$

因此

$$
\begin{aligned}
P_{r}((A+A) \neq X) & \leq \sum_{i=201}^{n-1} P_{r}(i \notin(A+A))+\sum_{i=n}^{2 n-203} P_{r}(i \notin(A+A)) \\
& \leq \sum_{i=201}^{n-1}\left(\frac{3}{4}\right)^{\left[\frac{i}{2}\right]}+\sum_{i=n}^{2 n-203}\left(\frac{3}{4}\right)^{n-\left[\frac{i}{2}\right]} \\
& \leq 2 \cdot \sum_{i=100}^{+\infty}\left(\frac{3}{4}\right)^{i}+2 \cdot \sum_{i=100}^{+\infty}\left(\frac{3}{4}\right)^{i} \\
& =16 \cdot\left(\frac{3}{4}\right)^{100}
\end{aligned}
$$

对 $A-A$ 同理, 由 $0,1, \cdots, 100$ 及 $n-101, n-100, \cdots, n-1 \in A$ 知

$$
n-201, n-200, \cdots, n-1 \in A-A \text {. }
$$

对 $i>0, i \leq n-202$, 若 $i \notin A-A$, 则

$$
P_{r}(\{0, i\} \cdot\{1, i+1\}, \cdots,\{n-i-1, n-1\} \text { 均不包含于 } A) \leq\left(\frac{3}{4}\right)^{n-i} \text {. }
$$

故

$$
\begin{aligned}
P_{r}((A-A) \neq Y) & \leq \sum_{i=1}^{n-202}\left(\frac{3}{4}\right)^{n-i} \\
& \leq\left(\frac{3}{4}\right)^{100}+\left(\frac{3}{4}\right)^{101}+\cdots \\
& =4 \cdot\left(\frac{3}{4}\right)^{100} .
\end{aligned}
$$

因此

$$
\begin{aligned}
P_{r}((A+A)=X \text { 且 }(A-A)=Y) & \geq 1-4 \cdot\left(\frac{3}{4}\right)^{100}-16 \cdot\left(\frac{3}{4}\right)^{100} \\
& >1-20 \cdot \frac{1}{2^{20}} \\
& >\frac{1}{2} .
\end{aligned}
$$

则满足 $(A+A)=X$ 且 $(A-A)=Y$ 集合至少有

$$
\frac{2^{n}}{2^{202}} \cdot \frac{1}{2}=\frac{2^{n}}{2^{203}}
$$

个, 令 $c=\frac{1}{2^{203}}$, 引理得证.

由引理, 在 $n>200$ 时, 所有 $(A+A)=X$ 及 $(A-A)=Y$ 的 $A$ 都是超级的

$$
|A+A|=|A-A|=2 n-1 .
$$

原题中令 $c=\frac{1}{2^{203}}$, 则在 $n>200$ 时结论成立. 在 $n \leq 200$ 时, $\{0,1,2, \cdots$, $n-1\}$ 子集仅有

$$
2^{n}<\frac{1}{c}=2^{203}
$$

个. 令 $c=\frac{1}{2^{203}}$, 在 $n \leq 200$ 时仍符合条件.

综上所述, 令 $c=\frac{1}{2^{203}}$ 时结论成立, 证毕.

评注 本题属于中等难度, 考场上做出的人不多, 从题中可以发现, 在 $A+A$ 及 $A-A$ 不为 $X, Y$ 时, $A$ 的取值将会变得十分复杂, 从而可令 $A+A=$ $X, A-A=Y$, 之后通过固定两侧的数再使用概率方法解决问题.

题 5 称平面上一个闭图形是好的, 如果它是凸的且内部不含格点. 称一个好的闭图形是极好的, 如果它不被任何好的闭图形真包含. 求证: 极好的有界闭图形是三角形或四边形.

证明 先证一个引理.

引理 所有极好的凸图形是凸多边形

引理证明 取出一个极好的平面凸图形 $S$, 因为 $S$ 为有界凸图形, 所以存在一个凸多边形 $A$ 包含 $S$ (如下图).

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-12.jpg?height=365&width=383&top_left_y=1548&top_left_x=811)

下构造序列

$$
A=A_{0} \supseteq A_{1} \supseteq A_{2} \supseteq \cdots \supseteq A_{n}, \quad n \in \mathbb{N}
$$

$A_{i}(0 \leq i \leq n)$ 为凸多边形使 $S \subseteq A_{n}$ 且 $A_{n}$ 内部无格点. (不含边界)

(1) $A$ 内部没有格点, 令 $n=0$, 即满足序列条件.

(2) 设 $A$ 内部有格点, 归纳构造 $A_{i}$.

$i=0$ 时, $A_{0}=A$, 设对 $j \leq i, A_{j}$ 都已构造, 且 $A_{i}$ 内部有格点.

$j=i+1$ 时, 取出 $A_{i}$ 内部的格点 $X$.

由 $S$ 内部无格点, 知 $X$ 在 $S$ 内部或边界上. 又因为 $S$ 为凸集, 则可以过 $X$
作一条直线 $l$, 使 $S$ 在 $l$ 某一侧的半平面(记为 $L$ )内, 如下图.

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-13.jpg?height=377&width=600&top_left_y=337&top_left_x=731)

令 $A_{i+1}$ 为 $L$ 与 $A_{i}$ 交集, 因为 $L, A_{i}$ 为凸集, 所以 $A_{i+1}$ 为凸集, 得出 $A_{i+1}$ 为凸多边形, 且 $A_{i+1} \subseteq A_{i}$, 相较于 $A_{i}, A_{i+1}$ 内部至少减少一个格点 $X$.

又由于 $A_{0}$ 内部仅有有限个格点, 知序列构造总会停止, 即 $n$ 存在. 此时 $S \subseteq A_{n}$ 且 $A_{n}$ 内部无格点, 由极好的有界闭图形性质知 $S=A_{n}$.

因此 $S$ 为凸多边形, 引理得证.

回到原题, 由引理, 此时所有极好的凸图形为多边形, 取出一个极好凸图形 $S$, 下证每条边上都有一个格点.

若否, 在边 $A B$ 上无格点, 设 $A, B$ 另一邻点分别为 $C, D(C$ 可能与 $D$ 重合).

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-13.jpg?height=268&width=394&top_left_y=1485&top_left_x=837)

延长 $C A, C B$, 作 $X Y / / A B, X Y$ 为距 $A B$ 最近且 $X Y$ 上有格点的边. 将 $A, B$ 顶点换为 $X, Y$, 则 $S$ 真包含于一个好的凸图形. 矛盾. 因此,每条边上至少存在一个格点.

设

$$
S=A_{1} A_{2} \cdots A_{n}, A_{n+1}=A_{1}
$$

$A_{i} A_{i+1}$ 上取格点 $B_{i}(n \geq 3)$, 则 $B_{1} B_{2} \cdots B_{n}$ 内无格点时有 $n=3$ 或 4.

若此结论不成立, 选取面积最小的 “极好的” 平面闭凸边形, 使其非三角形或四边形, 将此图形记为 $S$. 取出 $S$ 中任意 5 个顶点 $A, B, C, D, E$, 坐标为

$$
A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right), C\left(x_{3}, y_{3}\right), D\left(x_{4}, y_{4}\right), E\left(x_{5}, y_{5}\right)
$$

由抽屈原理, $x_{1} \sim x_{5}$ 中至少存在 3 个模 2 相同, 设 $x_{1}, x_{2}, x_{3}$ 模 2 相同, 由抽庹
原理, $y_{1}, y_{2}, y_{3}$ 模 2 至少有 2 个相同, 则不妨设

$$
y_{1} \equiv y_{2}(\bmod 2), x_{1} \equiv x_{2}(\bmod 2)
$$

故 $A B$ 中点 $M$ 为格点, 而 $A, B$ 为 $S$ 的顶点, 则 $M$ 在 $S$ 边界或内部, 而 $S$ 内部不存在格点, 因此 $M$ 在 $S$ 边界上, $A, B$ 为 $S$ 的相邻两个顶点.

设凸多边形 $S$ 为 $A B A_{1} A_{2} \cdots A_{K}$, 记 $S^{\prime}$ 为凸多边形 $A M A_{1} A_{2} \cdots A_{K}$, 则 $S^{\prime}$在 $S$ 内部, 因此 $S^{\prime}$ 内部不含格点, 故 $S^{\prime}$ 为好的闭图形. 而 $S^{\prime}$ 面积 $<S$ 面积, 这与 $S$ 面积最小性矛盾.

此时可得所有极好的凸图形为三角形或四边形. 证毕!

评注作为第二天考试的第一题, 是个十分简单的题目. 需注意凸图形的描述与修改, 一步一步用极好的图形条件进行证明.

题 6 对于正整数 $n$, 小于或等于 $n$ 且与 $n$ 互质的正整数 (包括 1 ) 的个数,记作 $\phi(n)$, 称为欧拉函数. 求证: 对于任意正整数 $n>1, \phi(1), \phi(2), \cdots, \phi(n)$可以分成和相同的两组.

证明 先证一个引理.

引理 对一个正整数序列 $a_{1}, a_{2}, \cdots, a_{n}, a_{1}=1$. 记可重集合

$$
S=\left\{a_{i 1}+a_{i 2}+\cdots+a_{i k} \mid 1 \leq i_{1}<i_{2}<\cdots<i_{k} \leq n, k \in \mathbb{Z}^{+}\right\}
$$

$T$ 为 $S$ 去重后的集合, 若对任意 $1 \leq i \leq n-1$, 有

$$
a_{i+1} \leq a_{1}+a_{2}+\cdots+a_{i}+1
$$

则

$$
T=\left\{1,2, \cdots, a_{1}+a_{2}+\cdots+a_{n}\right\} .
$$

引理证明 对 $n$ 归纳证明此引理. $n=1$ 时 $a_{1}=1, S=T=\{1\}$, 结论成立.

设 $n-1$ 时引理成立, $n$ 时, 由归纳假设, 对任意 $1 \leq i \leq n-2$ 有

$$
a_{i+1} \leq a_{1}+a_{2}+\cdots+a_{i}+1
$$

故

$$
\left\{1,2, \cdots, a_{1}+a_{2}+\cdots+a_{n-1}\right\} \subseteq S
$$

因此

$$
\left\{1,2, \cdots, a_{1}+a_{2}+\cdots+a_{n-1}\right\} \subseteq T
$$

对任意 $1 \leq i \leq a_{1}+a_{2}+\cdots+a_{n-1}$, 有 $i+a_{n} \in S$, 故

$$
\left\{a_{n}, a_{n}+1, \cdots, a_{1}+a_{2}+\cdots+a_{n-1}+a_{n}\right\} \subseteq T
$$

由

$$
a_{n} \leq a_{1}+a_{2}+\cdots+a_{n-1}+1,
$$

知

$$
\left\{1,2, \cdots, a_{1}+a_{2}+\cdots+a_{n}\right\} \subseteq T
$$

又由于

$$
S \text { 中最大元素 } \leq a_{1}+a_{2}+\cdots+a_{n},
$$

故

$$
T \subseteq\left\{1,2, \cdots, a_{1}+a_{2}+\cdots+a_{n}\right\}
$$

综上

$$
T=\left\{1,2, \cdots a_{1}+a_{2}+\cdots+a_{n}\right\}
$$

引理得证.

回到原题, 对任意 $i \geq 1$, 有 $(1, i)=1$ 因此 $\phi(i) \geq 1$. 而 $\phi(i) \leq i$, 故

$$
\phi(1)+\phi(2)+\cdots+\phi(i)+1 \geq i+1 \geq \phi(i+1)
$$

对任意 $i \geq 1$ 成立.

令引理中 $a_{i}=\phi(i)$. 又由 $\phi(1)=\phi(2)=1, n \geq 3$ 时有 $\phi(n) \equiv 0(\bmod 2)$ 知

$$
\frac{\phi(1)+\phi(2)+\cdots+\phi(n)}{2} \in \mathbb{Z}_{+}
$$

对 $n>1$ 成立. 由引理, 存在

$$
1 \leq j_{1}<j_{2}<\cdots<j_{k} \leq n
$$

有

$$
\phi\left(j_{1}\right)+\phi\left(j_{2}\right)+\cdots+\phi\left(j_{k}\right)=\frac{\phi(1)+\phi(2)+\cdots+\phi(n)}{2} .
$$

令

$$
A=\left\{j_{1}, j_{2}, \cdots, j_{k}\right\}, B=\{1,2, \cdots, n\} \backslash A
$$

则

$$
\sum_{l \in A} \phi(l)=\sum_{l \in B} \phi(l)=\frac{\phi(1)+\phi(2)+\cdots+\phi(n)}{2}
$$

结论成立, 证毕!

评注 本题是个简单题, 其中的欧拉函数在命题推广后便没有用处, 在这种看似困难的问题情况下, 抓住本质情况, 从本质上解决问题. 其中该问题的引理即是完备引理, 是一个十分重要的结论.
题 $7 G$ 为一个无向简单图,

$$
|V(G)|=400,|E(G)|=20000
$$

求证: 存在 $G$ 的顶点集的二分划 $V(G)=V_{1} \bigcup V_{2}$, 使得

$$
\left|E\left(V_{i}\right)\right| \leq 5024, \quad i=1,2
$$

证明 记 $N_{G}(V)$ 为 $V$ 在图 $G$ 中的邻域, $E_{1}$ 为 $V_{1}, V_{2}$ 之间所连边的集合. 对 $u \in V_{1}$, 记 $N_{V_{1}}(u)$ 为 $u$ 在 $V_{1}$ 中的邻域, $N_{V_{2}}(u)$ 为 $u$ 在 $V_{2}$ 中的邻域.

考虑一个划分 $V(G)=V_{1} \cup V_{2}$ 使得 $\left|E_{1}\right|$ 取得最大值.

若 $\left|N_{V_{2}}(u)\right|<\left|N_{V_{1}}(u)\right|$, 令

$$
V_{1}^{\prime}=V_{1} \backslash\{u\}, V_{2}^{\prime}=V_{2} \cup\{u\}
$$

此时

$$
\left|N_{V_{1}^{\prime}}(u)\right|=\left|N_{V_{1}}(u)\right|,\left|N_{V_{2}^{\prime}}(u)\right|=\left|N_{V_{2}}(u)\right|
$$

而 $E_{1}$ 中减少 $u$ 与 $N_{V_{2}}(u)$ 中连边, 增加 $N_{V_{1}}(u)$ 中连边, 即 $\left|E_{1}\right|$ 增加 $\left|N_{V_{1}}(u)\right|-$ $\left|N_{V_{2}}(u)\right|>0$, 与 $\left|E_{1}\right|$ 最大性矛盾. 因此, 对任意 $u \in V_{1}$, 均有 $\left|N_{V_{1}}(u)\right| \leq\left|N_{V_{2}}(u)\right|$,从而

$$
\sum_{u \in V_{1}}\left|N_{V_{1}}(u)\right| \leq \sum_{u \in V_{1}}\left|N_{V_{2}}(u)\right|=\left|E_{1}\right|
$$

而

$$
\sum_{u \in V_{1}}\left|N_{V_{1}}(u)\right|=2\left|E\left(V_{1}\right)\right|
$$

故 $2\left|E\left(V_{1}\right)\right| \leq\left|E_{1}\right|$, 同理 $2\left|E\left(V_{2}\right)\right| \leq\left|E_{1}\right|$. 考虑到

$$
\left|E\left(V_{1}\right)\right|+\left|E\left(V_{2}\right)\right|+\left|E_{1}\right|=20000,
$$

若 $\left|E_{1}\right| \leq 10049$, 则

$$
\left|E\left(V_{1}\right)\right|,\left|E\left(V_{2}\right)\right| \leq\left[\frac{\left|E_{1}\right|}{2}\right] \leq 5024
$$

满足题意.

若 $\left|E_{1}\right| \geq 10050$, 且 $\left|E\left(V_{1}\right)\right|>5024$ 或 $\left|E\left(V_{2}\right)\right|>5024$. 下调整 $V_{1}, V_{2}$ 使

$$
\left|E\left(V_{1}\right)\right|,\left|E\left(V_{2}\right)\right| \leq 5024
$$

由 $10050+2 \cdot 5024>20000$, 结合 (2) 式知 $\left|E\left(V_{1}\right)\right|,\left|E\left(V_{2}\right)\right|$ 中至多一个比 5024 大. 不妨设 $\left|E\left(V_{1}\right)\right|>5024$, 则

$$
\left|E\left(V_{2}\right)\right| \leqslant 20000-10050-5025=4925 .
$$

下不断将 $V_{1}$ 中的点移动到 $V_{2}$ 中, 直到某一时刻, 此时 $\left|E\left(V_{1}\right)\right| \geq 5025$, 但任将 $V_{1}$中的一点 $v$ 移动到 $V_{2}$ 中, 均有 $\left|E\left(V_{1}\right)\right|<5025$.

下证此时 $V_{1}$ 中存在一点 $u$, 将 $u$ 移动到 $V_{2}$ 后有 $\left|E\left(V_{2}\right)\right|<5025$.

若不然, 对任意 $u \in V_{1}$ 均有

$$
\left|N_{V_{2}}(u)\right| \geq 5025-\left|E\left(V_{2}\right)\right|
$$

易见

$$
\left|E\left(V_{1}\right)\right| \geq 5025>\left(\begin{array}{c}
100 \\
2
\end{array}\right)
$$

于是 $\left|V_{1}\right| \geq 101$. 对所有 $u \in V_{1}$, 将 (3) 式求和, 有

$$
\left|V_{1}\right|\left(5025-\left|E\left(V_{2}\right)\right|\right) \leq \sum_{u \in V_{1}}\left|N_{V_{2}}(u)\right|=\left|E_{1}\right|=20000-\left|E\left(V_{1}\right)\right|-\left|E\left(V_{2}\right)\right| \text {. }
$$

结合 $\left|V_{1}\right| \geq 101$, 有

$$
101 \cdot 5025-101\left|E\left(V_{2}\right)\right| \leqslant 20000-\left|E\left(V_{1}\right)\right|-\left|E\left(V_{2}\right)\right| .
$$

故

$$
\begin{aligned}
100\left|E\left(V_{2}\right)\right| & \geq 101 \cdot 5025+\left|E\left(V_{1}\right)\right|-20000 \\
& \geq 101 \cdot 5025+5025-20000
\end{aligned}
$$

即

$$
\left|E\left(V_{2}\right)\right| \geq 4926
$$

但对每次将 $u \in V_{1}$ 移至 $V_{2}$ 过程中, 每一个 $V_{1}$ 中点在 $V_{2}$ 中度恒不小于在 $V_{1}$ 中度, 即总有 $\left|E_{1}\right| \geq 2\left|E\left(V_{1}\right)\right|$. 此时

$$
\left|E\left(V_{1}\right)\right| \geq 5025,\left|E_{1}\right| \geq 2 \cdot 5025=10050
$$

则

$$
\left|E_{1}\right|+\left|E\left(V_{1}\right)\right|+\left|E\left(V_{2}\right)\right| \geq 4926+5025+10050=20001>20000
$$

与 (2) 式矛盾. 故存在一点 $u \in V_{1}$ 将 $u$ 移至 $V_{2}$ 后,

$$
\left|E\left(V_{1}\right)\right| \leq 5024,\left|E\left(V_{2}\right)\right| \leq 5024
$$

原命题得证.

评注 本题是道困难题, 一般的想法都会取出 $E_{1}$ 最大后再进行局部调整. 但不同的调整方法会产生不同结果, 较为容易出伪证. 在本题证明中通过 $V_{1}$ 的调整很好地保持了 $\left|E_{1}\right| \geq 2\left|E\left(V_{1}\right)\right|$ 的性质, 从而最后解决问题.
题 8 数列 $\left\{a_{n}\right\}$ 满足

$$
a_{0}=1, a_{n+1}=\sum_{\substack{i, j, k \geq 0 \\ i+j+k=n}} a_{i} a_{j} a_{k}
$$

对任意 $n \geq 0$ 成立. 求数列 $\left\{a_{n}\right\}$ 的通项.

解 1 定义一个路径:一个人从坐标系 $(0,0)$ 出发, 走 $3 n$ 步到 $(2 n, n)$, 每一次可以向上走一个单位或向右走一个单位, 且不越过 $x=2 y$ 的路径称为 $D$-path,

设 $n$ 阶 $D$-path 有 $b_{n}$ 个, 定义 $b_{0}=1$

$(0,0)$

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-18.jpg?height=294&width=580&top_left_y=835&top_left_x=721)

$(8,4)$

D-path

本题结论可以由如下三个引理导出.

引理 1 对任意 $n \in \mathbb{N}$, 有 $a_{n}=b_{n}$.

证明 对 $n$ 归纳. $n=0$ 时 $a_{0}=b_{0}=1, n=1$ 时 $a_{1}=b_{1}=1$, 设在 $t \leq n$ 时都有 $a_{t}=b_{t}$ 成立, $t=n+1$ 时, 下证 $a_{n+1}=b_{n+1}$, 即证明

$$
b_{n+1}=\sum_{\substack{i, j, k \geq 0 \\ i+j+k=n}} b_{i} b_{j} b_{k}
$$

记所有的 $(2 i, i)(0 \leq i \leq n)$ 称为边格, 对所有 $(2 i+1, i)(0 \leq i \leq n)$ 称为次边格, 考虑一条 $n+1$ 阶 $D$-path, 与 $x=2 y$ 的最后一个交点记为 $(2 i, i)(0 \leq i \leq n)$特别地, $i=0$ 时对应此 $D$-path 除起点与终点外不与 $x=2 y$ 相交.

由归纳假设, 从 $(0,0) \rightarrow(2 i, i)$ 的路径为 $D$-path, 有 $b_{i}$ 条, 则从

$$
(2 i, i) \rightarrow(2(n+1), n+1)
$$

路径中不再经过边格, 再选取最大的 $j$ 使此 $D$-path 经过次边格 $(2 j+1, j)$. (由于 $D$-path 过 $(2 i+1, i)$, 从而 $j$ 必然存在)

因为 $D$-path 经过 $(2 i, i)$, 而 $(2 i, i)$ 处仅有路径

$$
(2 i, i) \rightarrow(2 i+1, i)
$$

则 $i \leq j \leq n$, 从

$$
(2 i, i) \rightarrow(2 j+1, j)
$$

的路径不与 $x=2 y$ 相交,

![](https://cdn.mathpix.com/cropped/2024_02_26_24be6ed0257adede1d51g-19.jpg?height=426&width=828&top_left_y=318&top_left_x=631)

故可以视为一条从

$$
(2 i+1, i) \rightarrow(2 j+1, j)
$$

在 $x=2 y+1$ 及其下方的路径, 即为 $j-i$ 阶 $D$-path, 有 $b_{j-i}$ 种. 从

$$
(2 j+1, j) \rightarrow(2(n+1), n+1)
$$

的路径中, 必有

$$
(2 j+1, j) \rightarrow(2 j+2, j),
$$

$D$-path 最后一步必为

$$
(2(n+1), n) \rightarrow(2(n+1), n+1)
$$

从

$$
(2 j+2, j) \rightarrow(2(n+1), n)
$$

的路径不经过边格与次边格. 因此

$$
(2 j+2, j) \rightarrow(2(n+1), n)
$$

路径在 $x=2 y+2$ 及其下方, 对应 $n-j$ 阶 $D$-path, 有 $b_{n-j}$ 条. 故

$$
\begin{aligned}
b_{n+1} & =\sum_{\substack{0 \leq i \leq j \leq n}} b_{i} b_{j-i} b_{n-j} \\
& =\sum_{\substack{i, j, k \geq 0 \\
i+j+k=n}} b_{i} b_{j} b_{k} \\
& =\sum_{\substack{i, j, k \geq 0 \\
i+j+k=n}} a_{i} a_{j} a_{k} \\
& =a_{n+1} .
\end{aligned}
$$

故 $t=n+1$ 结论成立, 由第二数学归纳法知引理 1 得证.
引理 2 将 $2 n+1$ 个 1 及 $n$ 个 -2 排列在单位圆 $3 n+1$ 分点

$$
A_{1}, A_{2}, \cdots, A_{3 n+1}
$$

上, $A_{i}$ 上标数为 $a_{i}$, 则恰存在唯一的 $i \in\{1,2, \cdots, 3 n+1\}$, 使对任意 $j \in$ $\{0,1,2, \cdots, 3 n\}$ 都有

$$
a_{i}+a_{i+1}+\cdots+a_{i+j}>0,
$$

其中下标按模 $3 n+1$ 理解.

证明 先证明 $i$ 的存在性, 令

$$
S=\left\{a_{i}+a_{i+1}+\cdots+a_{i+j} \mid i=1,2, \cdots, 3 n+1, j=0,1,2, \cdots, 3 n\right\}
$$

取出 $S$ 中最大者 $a_{l}+a_{l+1}+\cdots+a_{l+m}$ (若最大值有很多个, 取 $m$ 最小的一个),令引理 2 中 $i$ 为此处 $l$, 下证其符合引理 2 条件.

若否, 则存在 $j=0,1, \cdots, 3 n$ 有

$$
\begin{gathered}
a_{l}+a_{l+1}+\cdots+a_{l+j} \leq 0 \\
a_{l}+a_{l+1}+\cdots+a_{l+m} \geq a_{1}+a_{2}+\cdots+a_{3 n+1}=(2 n+1) \cdot 1+(-2) \cdot n=1
\end{gathered}
$$

故 $j \neq m$.

(1) 若 $0 \leq j<m$, 则

$$
a_{l+j+1}+a_{l+j+2}+\cdots+a_{l+m} \geq a_{l}+a_{l+1}+,+a_{l+m}
$$

由 $a_{l}+a_{l+1}+\cdots+a_{l+m}$ 为 $S$ 中最大者, 知 (1) 式取等, 而 $m-j-1<m$, 与选取时 $m$ 最小性矛盾.

(2) 若 $j>m$, 则

$$
a_{l+m+1}+\cdots+a_{l+j} \leq-\left(a_{l}+a_{l+1}+\cdots+a_{l+m}\right),
$$

故

$$
\begin{aligned}
a_{l+j+1}+a_{l+j+2}+\cdots+a_{l+m} & =a_{1}+a_{2}+\cdots+a_{3 n+1}-\left(a_{l+m+1}+\cdots+a_{l+j}\right) \\
& \geq 1+\left(a_{l}+a_{l+1}+\cdots+a_{l+m}\right)
\end{aligned}
$$

与 $a_{l}+a_{l+1}+\cdots+a_{l+m}$ 最大性矛盾,

因此反设不成立, 引理 2 中存在性得证.

下证其唯一性, 若存在 $i_{1} \neq i_{2}$ 符合引理 2 中条件, 则

$$
a_{i_{1}}+a_{i_{1}+1}+\cdots+a_{i_{2}-1} \geq 1, a_{i_{2}}+a_{i_{2}+1}+\cdots+a_{i_{1}-1} \geq 1
$$

对两式求和有

$$
a_{1}+a_{2}+\cdots+a_{3 n+1} \geq 1+1=2,
$$

即 $1 \geq 2$, 矛盾, 引理 2 唯一性得证.
综上所述, 引理 2 得证.

引理 3

$$
b_{n}=\frac{\left(\begin{array}{c}
3 n+1 \\
n
\end{array}\right)}{3 n+1}=\frac{(3 n) !}{(2 n+1) ! \cdot n !}
$$

证明 将每一个 $n$ 阶 $D$-path 对应为一个长为 $3 n$ 的序列

$$
y_{1}, y_{2}, \cdots, y_{3 n}
$$

其中 $y_{i}=1$ 表示在 $D$-path 中第 $i$ 步向右, $y_{i}=-2$ 表示在 $D$-path 中第 $i$ 步向上.

设在经过 $i$ 步后 $D$-path 到达 $(u, v)(u \geq 2 v)$, 则

$$
y_{1}+y_{2}+\cdots+y_{i}=u-2 v \geq 0 \text {. }
$$

令 $y_{0}=1$, 则对任意 $0 \leq i \leq 3 n$ 有

$$
y_{0}+y_{1}+\cdots+y_{i}>0
$$

将序列 $y_{0}, y_{1}, \cdots, y_{3 n}$ 按顺序排列到单位圆 $3 n+1$ 分点上. 由引理 2 , 恰存在一个 $0 \leq i \leq 3 n$, 对任意 $0 \leq j \leq 3 n$ 有

$$
y_{i}+y_{i+1}+\cdots+y_{i+j}>0
$$

而 $i=0$ 符合引理 2 条件, 故此处 $i=0$. 定义两个单位圆周标数不同为其旋转后标数不重合, 即每一个单位圆上不同标数方式恰对应一条不同的 $D$-path. 而圆周上标数有 $\left(\begin{array}{c}3 n+1 \\ n\end{array}\right)$ 种选择, 由 $(2 n+1, n)=1$ 知每一次旋转后都有一个不重合的标数. 故不同标数方式有

$$
\frac{\left(\begin{array}{c}
3 n+1 \\
n
\end{array}\right)}{3 n+1}=\frac{(3 n) !}{(2 n+1) ! n !}
$$

个. 即

$$
b_{n}=\frac{(3 n) !}{(2 n+1) ! n !}
$$

引理 3 得证.

回到原题, 结合引理 1, 引理 3, 有

$$
a_{n}=b_{n}=\frac{(3 n) !}{(2 n+1) ! n !}
$$

因此 $a_{n}$ 的通项公式为 $a_{n}=\frac{(3 n) !}{(2 n+1) ! n !}$.

解 2 (龙泽金) 记

$$
A(x)=\sum_{i=1}^{+\infty} a_{i} x^{i}
$$

为 $\left\{a_{i}\right\}_{i=1}^{+\infty}$ 的生成函数. 考虑

$$
B(x)=(A(x)+1)^{3},
$$

则

$$
\begin{aligned}
B(x) & =\left(\sum_{i=0}^{+\infty} x^{i}\right)^{3} \\
& =\sum_{\substack{i=0 \\
\infty}}^{\infty} \sum_{\substack{u+v+w=i \\
u, v, w \geq 0}} a_{u} a_{v} a_{w} \cdot x^{i} \\
& =\sum_{i=0}^{+\infty} a_{i+1} x^{i} \\
& =\frac{A(x)}{x} .
\end{aligned}
$$

故

$$
(A(x)+1)^{3} \cdot x=A(x),
$$

令 $f(x)=(x+1)^{3}$, 则有

$$
x f(A(x))=A(x) .
$$

由 Langrange 反演, 知

$$
\begin{aligned}
a_{n} & =\left[x^{n}\right] A(x)=\frac{1}{n}\left[x^{n-1}\right] f(x)^{n} \\
& =\frac{1}{n}\left[x^{n-1}\right](x+1)^{3 n}=\frac{1}{n}\left(\begin{array}{c}
3 n \\
n-1
\end{array}\right) \\
& =\frac{\left(\begin{array}{c}
3 n \\
n
\end{array}\right)}{2 n+1} .
\end{aligned}
$$

即 $a_{n}$ 的通项公式为 $a_{n}=\frac{\left(\begin{array}{c}3 n \\ n\end{array}\right)}{2 n+1}$.

评注 本题作为一道困难题, 其证明过程中需要一些定理的积累. 很多人第一想法是用母函数去解决三次方程并表示幂级数, 在笔者看来是较为困难的, 我们可从组合意义入手, 在猜出答案后构造相应组合意义. 法一本质上引理 2 为 Raney 定理的变形, 引理 1 则为 $(0,0) \rightarrow(n, n)$ 的 Dyckpath 的推广. 在有引理 1,2 支持后问题便迎刃而解. 法二中的拉格朗日反演具有一定的高等背景, 其具体形式:若 $y=f(x)$ 在 $x_{0}$ 邻域内有反函数,则

$$
x=f^{-1}(y)=x_{0}+\left.\sum_{n=1}^{\infty} \frac{1}{n !} \cdot \frac{d^{n-1}}{d z^{n-1}}\left(\frac{z-x_{0}}{f(z)-y_{0}}\right)^{n}\right|_{z=x_{0}} \cdot\left(y-y_{0}\right)^{n},
$$

拉格朗日反演公式可以很快地求出反函数, 解微分方程, 并用泰勒展开的形式写出.

