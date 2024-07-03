# 2019 年俄罗斯数学奥林匹克试题评析 

袁祉祯<br>(湖北省武钢三中, 430080)<br>指导教师: 邓晓

2019 年第 45 届俄罗斯数学奥林匹克于 2019 年 4 月 22 日至 27 日在俄罗斯彼尔姆举行. 本次竞赛由湖北省选派 6 名中学生参加, 我有幸成为其中的一员,参加了十年级的比赛并获得了金牌.下面我们整理了今年十年级和十一年级的试题及其解答, 并作简要的评析, 不当之处, 恳请读者批评指正!

## I. 十年级

题 1. 平面上的每一个点 $A$ 都赋予了一个实数 $f(A)$, 且对任意三角形 $A B C$,当 $M$ 为 $\triangle A B C$ 的重心时, 总有 $f(M)=f(A)+f(B)+f(C)$. 证明: 对平面上的任何点 $A$, 总有 $f(A)=0$.

证明 对任意两个不同的点 $A, B$, 设 $A, B$ 的中点为 $C, A C$ 的中点为 $D$. 过点 $D$ 作两条与 $A B$ 不同的直线 $l_{1}, l_{2}$, 在 $l_{1}$ 上取点 $X, Y$, 且 $D$ 为 $X Y$ 的中点,在 $l_{2}$ 上取点 $M, N$, 且 $\overrightarrow{M D}=3 \overrightarrow{N D}$. 则由 $D$ 为 $X Y, A C$ 的中点得 $\triangle M X Y$ 与 $\triangle M A C$ 的重心都为 $N$. 所以

$$
f(N)=f(M)+f(X)+f(Y)=f(M)+f(A)+f(C),
$$

即有

$$
f(X)+f(Y)=f(A)+f(C) .
$$

又 $\overrightarrow{D B}=3 \overrightarrow{D C}$ 且 $D$ 为 $X Y$ 中点, 则 $C$ 为 $\triangle B X Y$ 重心. 所以

$$
f(C)=f(B)+f(X)+f(Y)
$$

代入 (1) 式可得

$$
f(A)+f(B)=0 \text {. }
$$

修订日期: 2019-07-10.
由 $A, B$ 任意性知任意一点 $A$, 再取两个不同点 $B, C$ 有

$$
\begin{aligned}
& f(A)+f(B)=0, \\
& f(A)+f(C)=0, \\
& f(B)+f(C)=0 .
\end{aligned}
$$

由 $(2)+(3)-(4)$ 知 $f(A)=0$. 故得证.

评析 此题是一个简单题, 有多种不同的证明方法. 此题看似为几何, 实则为代数题. 而且, 对 $c \neq 3$, 条件改为 $c f(M)=f(A)+f(B)+f(C)$, 结论依然成立.

题 2. 帕莎和沃瓦在玩如下的一个游戏, 在这个游戏中他们两人依次采取行动, 帕莎先行动. 最初, 他们拥有一块很大的橡皮泥. 帕莎的一次行动是把已经有的橡皮泥泥块中的一块切成任意大小的三块, 而沃瓦的一次行动是把已经有的橡皮泥泥块中的两块捏成一块. 如果某次行动之后在所有的橡皮泥泥块中出现了 100 块重量相等的橡皮泥泥块, 那么帕莎就获胜了. 请问: 沃瓦能阻止帕莎获胜吗?

解 不妨设橡皮泥质量为 300. 帕莎必胜.

其策略为: 当出现了一块质量为正整数且不小于 3 的橡皮泥时, 设其质量为 $k \geq 3$, 帕莎将其分成质量分别为 1,1 与 $k-2$ 的三块.

若场上所有橡皮泥质量为正整数, 易知帕莎和沃瓦的操作都会保持所有泥块的质量为正整数. 而每次帕莎操作后泥块数量增加 2 , 每次沃瓦操作后泥块数减少 1 , 故每一轮操作后橡皮泥块数量会增加. 而所有泥块质量和为定值 300 , 每块质量 $\geq 1$, 所以必有某一时刻帕莎无法使用该策略. 此时每一块橡皮泥的质量为 1 或 2 .

结合 $300=1 \times 100+2 \times 100$ 知质量为 1 的泥块与质量为 2 的泥块至少有一种出现了 100 块, 则帕莎获胜.

评析 此题是个容易的组合题. 若能注意到每轮橡皮泥个数增加且帕莎能保持橡皮泥质量为某一数的整数倍这一性质, 想到后面的证明方法都是自然的. 一个有趣的问题是考虑帕莎几回合后能保证胜利.

题 3. 一个星际酒店正好有 100 个客房, 它们分别能够容纳 101 个, 102 个, $\cdots, 200$ 个客人. 这些客房里一共住有 $n$ 个客人. 现在酒店即将有一位 VIP 客人到达, 酒店老板想为这位 VIP 客人单独提供一间客房. 为了达到这个目的,
老板可以选择 $A, B$ 两间房, 在不改变房间 $B$ 的容客量的情况之下, 把客房 $A$ 的所有客人搬到客房 $B$, 从而 VIP 客人可以住进房间. 求 $n$ 的最大值, 使得无论最初的 $n$ 个客人是如何分布在各个客房里的, 酒店老板都能够用上述方式为 VIP 客人提供一间房.

解 $n$ 的最大值为 8824 .

当 $n=8824$ 时, 设第 $i$ 个房间有 $x_{i}$ 个客人, $i=1,2, \cdots, 100$. 所以 $0 \leq x_{i} \leq$ $100+i$ 且

$$
\sum_{i=1}^{100} x_{i}=8824
$$

若酒店老板不能如愿, 则对任意 $1 \leq i<j \leq 100$, 有 $x_{i}+x_{j}>100+j$. 故

$$
x_{i}+x_{j} \geq 101+j
$$

否则可将第 $i$ 个客房的人移至第 $j$ 个客房. 故

$$
\begin{aligned}
\sum_{i=1}^{100} x_{i}=\sum_{i=1}^{50}\left(x_{i}+x_{101-i}\right) & \geq \sum_{i=1}^{50}(101+(101-i)) \\
& =202 \times 50-\frac{50 \times 51}{2}=8825
\end{aligned}
$$

矛盾!

故酒店老板一定能够如愿.

当 $n \geq 8825$ 时, 构造: 先在前 50 个房间均安排 76 个客人, 第 $i$ 个房间安排 $25+i$ 人, $i=51,52, \cdots, 100$, 则共安排了 $76 \times 50+\sum_{i=51}^{100}(25+i)=8825$ 人, 剩下的 $n-8825$ 人随意安排, 则对任意两房间 $i<j$. 若 $j \leq 50$, 则两房间人数和为 $76 \times 2>j+100>i+100$.

若 $i \leq 50<j$, 则两房间人数和为 $76+25+j>j+100>i+100$.

若 $50<i<j$, 则两房间人数和为 $25+i+25+j>j+100>i+100$.

故老板总不能如愿.

评析此题是个正常的代数题. 将 100 个客房人数设为 $x_{1}, x_{2}, \cdots, x_{100}$, 并用其转化条件都不难, 唯一的难点在于在估计人数方面知道哪些不等式是无用的,哪些不等式是本质的. 实际上, 只有当 $i \leq 50<j$ 时, 关于 $i, j$ 房间对应的不等式才是本质的. 注意到极端情况为 $x_{1} \leq x_{2} \leq \cdots \leq x_{100}$ 是自然的, 然后再进行后面的放缩与构造。

题 4. 设 $\triangle A B C$ 是一个锐角三角形且 $A C<B C$. 一个通过 $A, B$ 两点的圆与线段 $A C, B C$ 除点 $A$ 和点 $B$ 之外的另两个交点分别为点 $A_{1}$ 和点 $B_{1} . \triangle A B C$
的外接圆与 $\triangle A_{1} B_{1} C$ 的外接圆交于除 $C$ 之外的一点 $P$. 线段 $A B_{1}$ 与线段 $B A_{1}$交于点 $S$. 设点 $Q$ 与点 $R$ 分别为点 $S$ 关于直线 $C A$ 与直线 $C B$ 的对称点. 证明: $P, Q, R, C$ 四点共圆.



证明 过点 $S$ 作 $C B, C A$ 垂线分别交于 $C A, C B$ 于 $M, N$. 因为 $\triangle A B C$ 为锐角三角形, 所以 $M, N$ 存在且分别在 $C A_{1}, C B_{1}$ 延长线上.

过点 $M, N$ 作 $C A, C B$ 垂线交于点 $T$, 则 $M, S, N, T$ 构成平行四边形且 $S$ 为 $\triangle C M N$ 的垂心, $M N \perp C S$.

设 $T$ 关于 $C A, C B$ 对称点为 $T_{1}, T_{2}, M, N$ 分别为 $T T_{1}, T T_{2}$ 的中点. 再由平行四边形 $M S N T$ 知 $T_{1} T_{2}$ 过点 $S$, 且 $T_{1} T_{2}$ 与 $M N$ 平行, 即 $T_{1} T_{2} \perp C S$. 又 $A, A_{1}, B_{1}, B$ 共圆, 所以 $\triangle A_{1} S A$ 与 $\triangle B_{1} S B$ 相似,而

$$
\angle A_{1} M S=\angle C M S=90^{\circ}-\angle A C B=\angle C N S=\angle B_{1} N S,
$$

且

$$
\angle M A_{1} S=\angle A A_{1} S=\angle B B_{1} S=\angle N B_{1} S,
$$

因此 $\triangle A_{1} S M$ 与 $\triangle B_{1} N S$ 相似, 故

$$
\frac{A_{1} A}{B_{1} B}=\frac{A_{1} S}{B_{1} S}=\frac{A_{1} M}{B_{1} N}
$$

所以

$$
\frac{A_{1} A}{A_{1} M}=\frac{B_{1} B}{B_{1} N}
$$

过点 $A_{1}, B_{1}$ 分别作 $C A, C B$ 垂线交于 $Y$, 过点 $A, B$ 作 $C A, C B$ 垂线交于点 $X$, 而 $T M \perp C A, T N \perp C B$. 由 $M, A, A_{1}$ 共线, $N, B, B_{1}$ 共线, 两直线不平行重合且 $\frac{A_{1} A}{A_{1} M}=\frac{B_{1} B}{B_{1} N}$ 得 $Y, X, T$ 共线. 而 $C, P, A_{1}, B_{1}, Y$ 共圆, 直径为 $C Y$, $C, P, A, B, X$ 共圆, 直径为 $C X$, 则 $\angle C P Y=90^{\circ}=\angle C P X$, 所以 $P, X, Y$ 共线, $\angle C P T=90^{\circ}$.
而 $Q, S$ 与 $T_{1}, T$ 分别关于 $C A$ 对称, 所以 $\angle C Q T=\angle C S T_{1}=90^{\circ}$, 同理 $\angle C R T=90^{\circ}$. 这样

$$
\angle C P T=\angle C Q T=\angle C R T=90^{\circ} \text {, }
$$

所以 $C, P, Q, T, R$ 共圆, 得证.

评析 此题是一个较为困难的几何题. 考虑到每个点的刻化方式都比较基础, 所以从计算的角度做该题是可行的. 笔者的做法为一种证明四点共圆的通用方法: 找出欲证圆的一条直径去证明三组垂直(或作出两组垂直证明第三组).由于此题 $P$ 的特殊性质, 可转化为证明四点共线的问题, 之后的证明是自然的.

题 5. 在一个幼儿园里, 一个保育员拿出 $n>1$ 个全等的长方形硬纸板并把这 $n$ 个硬纸板分发给 $n$ 个小朋友, 每个小朋友正好拿到一个硬纸板. 每个小朋友再把拿到的硬纸板切成若干个全等的正方形 (不同的小朋友得到的正方形的大小可能不一样). 设所得到的全部正方形的个数是一个质数. 证明: 最初的硬纸板必定是一个正方形.

证明 设长方形为 $a \times b$ 型, 第 $i$ 个小朋友的正方形边长为 $x_{i} \in \mathbb{R}^{+}, i=$ $1,2, \cdots, n$.

考虑长方形的边的分割知 $\frac{a}{x_{i}} \in \mathbb{Z}^{+}, \frac{b}{x_{i}} \in \mathbb{Z}^{+}, i=1,2, \cdots, n$. 所以 $\frac{a}{b} \in \mathbb{Q}^{+}$.

设 $\frac{a}{b}=\frac{p}{q}, p, q \in \mathbb{N}^{+}$, 且 $(p, q)=1$, 由 Bezout 定理知, 存在 $u, v \in \mathbb{Z}$ 使得

$$
u p+v q=1
$$

所以

$$
\frac{a}{x_{i} p}=\frac{b}{x_{i} q}=\frac{a}{x_{i}} u+\frac{b}{x_{i}} v \in \mathbb{Z}, i=1,2, \cdots, n .
$$

故正方形的总数为

$$
\sum_{i=1}^{n}\left(\frac{a}{x_{i}} \cdot \frac{b}{x_{i}}\right)=p q \sum_{i=1}^{n}\left(\frac{a}{x_{i} p} \cdot \frac{b}{x_{i} q}\right)
$$

为质数.

由 $n>1$ 得

$$
\sum_{i=1}^{n}\left(\frac{a}{x_{i} p} \cdot \frac{b}{x_{i} q}\right)
$$

为大于 1 的整数, 所以 $p q=1, p=q=1, a=b$.

即原长方形为正方形, 得证.

评析 此题是个简单数论题, 将原矩形长宽设出, 运用最基础的质数的定义
即可推出结论.

题 6. 设 $L$ 是锐角三角形 $A B C$ 的角 $\angle B$ 的角平分线与 $A C$ 边的交点. 而点 $D$ 和点 $E$ 分别为 $\triangle A B C$ 的外接圆中劣弧 $A B$ 与劣弧 $B C$ 的中点. 点 $P$ 和点 $Q$分别为线段 $B D$ 与线段 $B E$ 延长线上的两点, 且满足: $\angle A P B=\angle C Q B=90^{\circ}$.证明: 线段 $B L$ 的中点在直线 $P Q$ 上.



证明 延长 $B P, B Q$ 至 $P_{1}, Q_{1}$, 使得 $B P_{1}=2 B P, B Q_{1}=2 B Q$.

由 $A P \perp B P, C Q \perp B Q$ 得 $\triangle A P_{1} B, \triangle C Q_{1} B$ 为等腰三角形. 所以

$$
\angle P_{1} A B=180^{\circ}-2 \angle A B P \text {. }
$$

又点 $D$ 为劣弧 $A B$ 的中点, 则

$$
\angle A B P=\angle A B D=\frac{1}{2} \angle A C B, \quad \angle P_{1} A B=180^{\circ}-\angle A C B
$$

同理 $\angle Q_{1} C B=180^{\circ}-\angle B A C$. 所以

$$
\angle P_{1} A B+\angle B A C+\angle B C A+\angle B C Q_{1}=360^{\circ} \text {, }
$$

进而 $A P_{1}$ 与 $C Q_{1}$ 平行. 又 $B L$ 平分 $\angle A B C$, 知

$$
\frac{A L}{L C}=\frac{A B}{B C}=\frac{A P_{1}}{C Q_{1}}
$$

所以图形 $L A P_{1}$ 与图形 $L C Q_{1}$ 相似 (可能为退化三角形), 所以 $P_{1}, L, Q_{1}$ 共线.

取 $B L$ 中点 $L_{1}$. 因为 $\overrightarrow{B L}=2 \overrightarrow{B L_{1}}, \overrightarrow{B P_{1}}=2 \overrightarrow{B P}, \overrightarrow{B Q_{1}}=2 \overrightarrow{B Q}$, 由位似知 $P, L_{1}, Q$ 共线, 即 $P Q$ 过 $B L$ 的中点.

评析 此题是个常规的几何题, 运用中位线或者倍长线段后, 可将结论转化为相似形的问题, 后面的共线是容易的.
题 7. 24 个学生参加一个数学圈的活动. 对任何一个由 6 个学生组成的一个队，老师可以认定这个队要么优秀要么良好. 对参加这次数学圈活动的 24 个学生, 老师想把他们分为 4 个队, 每个队有 6 名学生. 请问: 是否可能存在这种情况: 每一个这样的划分都正好有三个优秀的队或一个优秀的队，而且至少有一个划分正好出现三个优秀的队, 至少有另一个划分正好出现一个优秀的队?

证明 该情况是存在的. 对 21 个学生赋值 0 , 剩下 3 个学生赋值 1 . 对任意一队 6 人, 若所有人赋值之和为奇数, 则为优秀, 否则为良好. 所以, 任一划分, 24 个学生赋值和 3 , 是一个奇数, 所以每个队赋值和有 3 个奇数或一个奇数, 即 3 个优秀队或 1 个优秀队.

而划分为 $000000 ; 000000 ; 000000 ; 000111$ 时, 有一个优秀队.

划分为 $000000 ; 000001 ; 000001 ; 000001$ 时, 有三个优秀的队.

故满足题意.

评析 此题不难, 若一开始猜错结论很容易误入歧途. 此题本质上与 6,24 无关, 对一般的 $n, 4 n$ 均有结论成立. 从考虑整体的角度去构造容易些, 而且构造不唯一。

题 8. 设 $P(x)$ 是一个整系数, 非常数的多项式, 设 $n$ 是一个正整数. 序列 $a_{0}, a_{1}, \cdots$ 按照下面的公式确定: $a_{0}=n, a_{k}=P\left(a_{k-1}\right)$, 这里 $k$ 为任意的正整数.假设对每个正整数 $b$ 上述序列中都包含某个大于 1 的正整数的 $b$ 次幂. 证明: $P(x)$ 是一个一次多项式.

证明 由整系数多项式的性质, 对任意的 $x \neq y, x, y \in \mathbb{Z}$, 有

$$
(x-y) \mid(P(x)-P(y)) \text {. }
$$

首先, 对任意的正整数 $c,\left\{a_{n}\right\}$ 中有一项为大于 1 的整数的 $c$ 次幂 $\geq 2^{c} \geq c$,所以 $\left\{a_{n}\right\}$ 无上界.

而若存在 $0 \leq i<j, i, j \in \mathbb{Z}$, 使得 $a_{i}=a_{j}$, 则

$$
a_{i+1}=P\left(a_{i}\right)=P\left(a_{j}\right)=a_{j+1} .
$$

从 $i$ 项开始 $\left\{a_{n}\right\}$ 为周期数列, 矛盾! 故 $\left\{a_{n}\right\}$ 中项两两不同. 而

$$
\left(a_{i}-a_{i-1}\right) \mid\left(P\left(a_{i}\right)-P\left(a_{i-1}\right)\right), \forall i \in \mathbb{N}^{+},
$$

即 $\left(a_{i}-a_{i-1}\right) \mid\left(a_{i+1}-a_{i}\right)$. 则递推知 $\forall i, j \in \mathbb{N}^{+}$, 有

$$
\left(a_{i}-a_{i-1}\right) \mid\left(a_{i+j}-a_{i+j-1}\right),
$$

所以

$$
a_{i+j} \equiv a_{i+j-1} \equiv \cdots \equiv a_{i-1} \quad\left(\bmod a_{i}-a_{i-1}\right)
$$

因此从第 $i-1$ 项起所有项均与 $a_{i-1}$ 模 $a_{i}-a_{i-1}$ 同余.

而对任意 $p^{\alpha} \| a_{i}-a_{i-1}, p$ 为素数, $\alpha \in \mathbb{N}^{+}$, 有 $\varphi\left(p^{\alpha}\right) \mid \varphi\left(\left|a_{i}-a_{i-1}\right|\right)$, 且

$$
\varphi\left(\left|a_{i}-a_{i-1}\right|\right) \geq \varphi\left(p^{\alpha}\right) \geq \alpha
$$

其中 $\varphi(x)$ 为欧拉函数.

由欧拉定理得对任意 $x \in \mathbb{Z}, s \in \mathbb{N}^{+}$有

$$
x^{s \cdot \varphi\left(\left|a_{i}-a_{i-1}\right|\right)} \equiv 0 \text { 或 } 1 \quad\left(\bmod p^{\alpha}\right) .
$$

取充分大的 $s$ 使 $2^{s \cdot \varphi\left(\left|a_{i}-a_{i-1}\right|\right)}$ 大于 $a_{i-1}$ 前的所有项. 而 $\left\{a_{n}\right\}$ 中必有一项为大于 1 的整数的 $s \cdot \varphi\left(\left|a_{i}-a_{i-1}\right|\right)$ 次幂. 所以该项与 $a_{i-1}$ 模 $a_{i}-a_{i-1}$ 同余, 则存在 $y \in \mathbb{N}^{+}$, 使得

$$
a_{i-1} \equiv y^{s \cdot \varphi\left(\left|a_{i}-a_{i-1}\right|\right)} \quad\left(\bmod a_{i}-a_{i-1}\right)
$$

故

$$
a_{i-1}\left(a_{i-1}-1\right) \equiv y^{s \cdot \varphi\left(\left|a_{i}-a_{i-1}\right|\right)}\left(y^{s \cdot \varphi\left(\left|a_{i}-a_{i-1}\right|\right)}-1\right) \equiv 0 \quad\left(\bmod a_{i}-a_{i-1}\right) .
$$

所以

$$
\left(a_{i}-a_{i-1}\right) \mid a_{i-1}\left(a_{i-1}-1\right), \forall i \in \mathbb{N}^{+}
$$

又存在 $N \in \mathbb{N}^{+}$, 使 $i \geq N$, 时, $\left|a_{i}\right|>2$, 则此时 $a_{i}\left(a_{i}-1\right)>0$, 所以

$$
\left|a_{i+1}-a_{i}\right| \leq a_{i}\left(a_{i}-1\right), 2 a_{i}-a_{i}^{2} \leq a_{i+1} \leq a_{i}^{2}
$$

因此

$$
2 a_{i}-a_{i}^{2} \leq P\left(a_{i}\right) \leq a_{i}^{2}
$$

对任意 $i \in \mathbb{N}^{+}, i \geq N$ 成立.

又 $\left\{a_{n}\right\}$ 无上界, 所以可取 $a_{i}$ 充分大, 当 $P(x)$ 不为一次多项式时, $P(x)$ 只能为二次多项式且首项系数为 $\pm 1$.

情形 1: $P(x)=x^{2}+b x+c, b, c \in \mathbb{Z}$, 则

$$
\left(a_{i}^{2}+a_{i}(b-1)+c\right)\left|\left(a_{i}^{2}-a_{i}\right),\left(a_{i}^{2}+a_{i}(b-1)+c\right)\right|\left(b a_{i}+c\right), i \in \mathbb{N}^{+}, i \geq N
$$

取 $a_{i}$ 充分大则可得 $b=c=0$, 所以 $a_{i}=n^{2^{i}}$, 而 $\left\{a_{n}\right\}$ 中有一项为大于 1 的整数的 $2 n+1$ 次幕. 所以该项为

$$
n^{2^{i} 0}=y^{2 n+1}(y \geq 2) .
$$

因为 $\left(2^{i_{0}}, 2 n+1\right)=1$, 所以存在 $z \in \mathbb{N}^{+}, z \geq 2$ 使得

$$
n=z^{2 n+1} \geq 2^{2 n+1}>n
$$

矛盾!

情形 2: $P(x)=-x^{2}+b x+c, b, c \in \mathbb{Z}$, 则

$$
\left(-a_{i}^{2}+a_{i}(b-1)+c\right)\left|\left(a_{i}^{2}-a_{i}\right),\left(-a_{i}^{2}+a_{i}(b-1)+c\right)\right|(2-b) a_{i}-c
$$

取 $a_{i}$ 充分大则可得 $b=2, c=0$. 所以

$$
a_{i}=1-(n-1)^{2^{i}}, i \in \mathbb{N}^{+} \text {. }
$$

故 $a_{i} \leq 1, \forall i \in \mathbb{N}^{+}$. 这与 $\left\{a_{i}\right\}_{i \in \mathbb{N}^{+}}$无上界矛盾!

综上所述, $P(x)$ 必为一次多项式.

评析 此题是个偏难的数论题. 需要熟知结论对任意的 $x \neq y, x, y \in \mathbb{Z}$, 均有 $(x-y) \mid(P(x)-P(y))$, 并灵活应用. 因为该数列是多项式级增长, 所以当 $\operatorname{deg} P \geq 2$ 时, $\left|a_{n}\right|$ 的增长速度是很快的. 故推出 $\left(a_{i}-a_{i-1}\right) \mid a_{i-1}\left(a_{i-1}-1\right)$ 时,就可以考虑去用代数放缩了, 后面的过程虽有些繁琐, 但都是平凡的.

## II. 十一年级

题 1. 同十年级第一题.

题 2. 是否对每一对非零整数 $a$ 和非零整数 $b$, 下面的方程组

$$
\left\{\begin{array}{l}
\tan (13 x) \tan (a y)=1 \\
\tan (21 x) \tan (b y)=1
\end{array}\right.
$$

都至少有一组解, 并证明你的论断.

解 令 $a=5, b=8$ 若方程组成立, 则

$$
\begin{aligned}
13 x+a y=k \pi+\frac{\pi}{2}, & k \in \mathbb{Z} \\
21 x+b y & =l \pi+\frac{\pi}{2}, \quad l \in \mathbb{Z} .
\end{aligned}
$$

进而

$$
(21 a-13 b) y=(21 k-13 l+4) \pi,
$$

但 $21 a-13 b=1$, 所以

$$
y=m \pi, m \in Z, \tan (a y)=0 .
$$

矛盾! 故对 $(a, b)=(5,8)$ 不成立, 即不是总成立.
评析 此题较简单, 答案也很好猜, 用 Bezout 定理去构造即可.

题 3. 一个人拥有 $n$ 个彼此重量互不相同的硬币和 $n$ 个天平, 这里 $n>2$.每一次称重允许把两个硬币放到其中的一个天平的两个托盘上, 从而比较这两个硬币的重量, 再把这两个硬币从托盘上拿下. 已知这些天平中有一个 (谁也不知道是哪一个) 可能是坏的, 而且这个坏了的天平每次给出的结果是随机的 (有时给出正确的结果, 有时给出错误的结果). 确定最少的称重次数, 使得这个人能确定这些硬币中哪个才是最重的.

解 先说明 $2 n-2$ 次不能保证称出.

首先令前 $2 n-3$ 次所有天平都给出正确结果. 而对 $n$ 个硬币都赋上值, 一开始值为 0 . 当一次称重两个硬币时, 若该天平给出的结果是硬币 $A$ 的重量小于硬币 $B$ 的重量. 则将 $A$ 赋的值加 1 , 故 $2 n-3$ 次后所有赋值和为 $2 n-3<2(n-1)$,所以至多有 $n-2$ 个硬币赋值 $\geq 2$, 此时取出最重的硬币 $Y$ 与另一个赋值 $<2$ 的硬币 $X$, 则易知 $Y$ 的赋值为 0 .

情形 1: 若第 $2 n-2$ 次称重未选中 $X$, 则令天平在最后一次反映正确结果,这时所有硬币重量按真实情况排列 (记此排列为 (1), 或 $X$ 最重, 其它所有硬币按真实情况排列 (记此排列为 (2) 都是可能的.

(1) 中任取一天平为坏的均成立, (2) 中取使 $X$ 赋值加 1 的天平 (没有则任取)为坏的即成立.

情形 2: 若第 $2 n-2$ 次称重选中 $X$, 则令天平在最后一次反映结果为 $X$ 更重. 则所有硬币重量按真实情况排列 (记此排列为 (3)), 或 $X$ 最重, 其它所有硬币按真实情况排列 (记此排列为 (4)) 都是可能的.

(3) 中取最后一次的天平为坏的即成立, (4) 中取使 $X$ 赋值加 1 的天平 (没有则任取) 为坏的即成立.

综上, $2 n-2$ 次不能保证哪个最大.

对于 $2 n-1$ 次策略如下: 取天平 $1,2,3$, 每次操作, 取两个硬币分别用天平 1,2 称.

若结果一样, 则去掉轻的硬币 (该硬币一定更轻), 再将剩下的硬币继续进行操作.

若结果不一样, 则将所有剩下硬币每次取 2 个用天平 3 称 (天平 3 一定是好的), 然后去掉轻的, 剩下的继续用天平 3 称.

若 $(*)$ 一直进行到只剩一个硬币, 则去掉了 $n-1$ 个硬币, 操作了 $2 n-2<$
$2 n-1$ 次.

若 $(*)$ 进行了 $a$ 次后, 第 $2 a-1$ 次与 $2 a$ 次称重的结果不一样, 则此时还有 $n-(a-1)$ 个硬币, 其中 $a \leq n-1, a \in \mathbb{N}^{+}$, 则再用 $(\triangle)$ 称 $n-a$ 次即可. 共用 $2 a+n-a=n+a \leq 2 n-1$ 次.

故用 $2 n-1$ 次能确定最重的硬币. 所以, 最少的次数为 $2 n-1$.

评析 此题是个较难的组合问题, 可以通过小的 $n$ 的尝试猜出答案, 并知道天平个数与 $n$ 无关, 只要天平个数 $\geq 3$, 此题的结论是一样的. 对于题目的论证部分, 要根据构造部分的极端情况来给出. 要想构造两种不同最大硬币的排列,只需一个是真实的排列, 另一个与真实情况类似, 且称错的次数极少即可.

题 4. 设 $A B C D$ 是一个三棱锥. 一个球面 $\omega_{A}$ 和三棱锥的外表面 $B C D$ 及三棱锥的除面 $B C D$ 外的其它三个面相切. 另一个球面 $\omega_{B}$ 和三棱锥的外表面 $A C D$ 及三棱锥的除面 $A C D$ 之外的其它三个面相切. 设球面 $\omega_{A}$ 与平面 $A C D$交于点 $K$, 球面 $\omega_{B}$ 与平面 $B C D$ 交于 $L$ 点. 若 $X, Y$ 分别是线段 $A K$ 与线段 $B L$延长线上的点, 且满足

$$
\angle C K D=\angle C X D+\angle C B D \text {, 且 } \angle C L D=\angle C Y D+\angle C A D \text {. }
$$

证明: 点 $X$ 和点 $Y$ 到线段 $C D$ 的中点距离相等.


证明 设四面体的内切球为 $\omega$, 且切面 $B C D, C D A, D A B, A B C$ 于 $L_{1}, K_{1}, M_{1}$, $N_{1}$. 设 $\omega$ 的球心为 $O$, 半径为 $r$, 则

$$
A K_{1}=\sqrt{A O^{2}-r^{2}}=A M_{1}=A N_{1} .
$$

同理

$$
B L_{1}=B M_{1}=B N_{1}, C L_{1}=C K_{1}=C N_{1}, D L_{1}=D K_{1}=D M_{1},
$$

所以

$$
\triangle A M_{1} B \cong \triangle A N_{1} B, \quad \angle A M_{1} B=\angle A N_{1} B \triangleq \alpha_{12}
$$

同理可设

$$
\begin{aligned}
& \alpha_{13}=\angle A K_{1} C=\angle A N_{1} C, \\
& \alpha_{14}=\angle A K_{1} D=\angle A M_{1} D, \\
& \alpha_{23}=\angle B L_{1} C=\angle B N_{1} C, \\
& \alpha_{24}=\angle B L_{1} D=\angle B M_{1} D, \\
& \alpha_{34}=\angle C L_{1} D=\angle C K_{1} D,
\end{aligned}
$$

所以在 $\triangle B C D$ 中,

$$
\alpha_{23}+\alpha_{34}+\alpha_{24}=2 \pi
$$

在 $\triangle C D A$ 中,

$$
\alpha_{34}+\alpha_{14}+\alpha_{13}=2 \pi
$$

在 $\triangle D A B$ 中,

$$
\alpha_{14}+\alpha_{12}+\alpha_{24}=2 \pi
$$

在 $\triangle A B C$ 中,

$$
\alpha_{12}+\alpha_{23}+\alpha_{13}=2 \pi
$$

由 $(1)+(2)-(3)-(4)$ 得 $\alpha_{34}=\alpha_{12}$, 同理 $\alpha_{13}=\alpha_{24}, \alpha_{14}=\alpha_{23}$, 所以

$$
\angle A K_{1} C=\angle B L_{1} D \text {. }
$$

再考虑 $\omega$ 与 $\omega_{A}$ 两球均与面 $A B C, A C D, A D B$ 相切, 所以两球关于点 $A$ 位似.

设 $\omega_{A}$ 切面 $A B C, B C D, D A B$ 于 $N_{2}, L_{2}, M_{2}$, 同理可得

$$
\begin{aligned}
& A K=A N_{2}=A M_{2}, B N_{2}=B L_{2}=B M_{2} \\
& C K=C N_{2}=C L_{2}, D K=D L_{2}=D M_{2}
\end{aligned}
$$

由两球位似知 $A, K_{1}, K$ 共线, $A, M_{1}, M_{2}$ 共线, $A, N_{1}, N_{2}$ 共线. 同上可以得到 6
组三角形全等, 所以

$$
\begin{aligned}
\angle B C L_{1}+\angle B C L_{2} & =\angle B C N_{1}+\angle B C N_{2} \\
& =\angle A N_{1} C-\angle A N_{2} C \\
& =\angle A K_{1} C-\angle A K C \\
& =\angle K_{1} C D+\angle K C D \\
& =\angle L_{1} C D+\angle L_{2} C D .
\end{aligned}
$$

又

$$
\angle B C L_{1}+\angle L_{1} C D=\angle B C L_{2}+\angle L_{2} C D=\angle B C D,
$$

所以

$$
\angle B C L_{1}=\angle L_{2} C D \text {. }
$$

同理可得

$$
\angle B D L_{1}=\angle C D L_{2},
$$

所以 $L_{1}, L_{2}$ 为 $\triangle B C D$ 的等角共轭点, 进而有

$$
\begin{aligned}
\angle C X D & =\angle C K D-\angle C B D \\
& =\angle C L_{2} D-\angle C B D \\
& =\angle B C L_{2}+\angle B D L_{2} \\
& =\angle D C L_{1}+\angle C D L_{1} \\
& =\pi-\angle C L_{1} D \\
& =\pi-\angle C K_{1} D,
\end{aligned}
$$

所以 $X, K_{1}, C, D$ 共圆, 故

$$
\angle X D C=\angle X K_{1} C=\pi-\angle A K_{1} C=\pi-\angle B L_{1} D,
$$

同理

$$
\begin{gathered}
\angle C Y D=\pi-\angle C K_{1} D=\pi-\angle C L_{1} D=\angle C X D \\
\angle Y C D=\angle Y L_{1} D=\pi-\angle B L_{1} D=\angle X D C
\end{gathered}
$$

所以

$$
\triangle X C D \cong \triangle Y D C
$$

因此点 $X$ 和点 $Y$ 到线段 $C D$ 的中点距离相等. 得证.
评析 此题是一个立体几何难题. 实际上, 此题可以由立体几何完全转化为四个图形, 并考虑他们的关系. 由于内切圆, 外切圆性质和内切球, 外切球的性质类似, 可将内切球取出, 并取出所有的切点, 之后建立四个图形的关系, 后面的过程由正推或倒推都可以得到. 上述做法参考了官方答案.

题 5. 五个同心圆 $w_{1}, w_{2}, w_{3}, w_{4}, w_{5}$ 的半径 (按上述顺序) 构成一个公比为 $q$ 的等比数列. 求 $q$ 可能取到的最大值使得存在折线 $A_{0} A_{1} A_{2} A_{3} A_{4}$ 满足条件: $A_{i} \in w_{i}, i=0,1,2,3,4$, 而且折线 $A_{0} A_{1} A_{2} A_{3} A_{4}$ 正好由四条长度相等的线段 $A_{0} A_{1}, A_{1} A_{2}, A_{2} A_{3}, A_{3} A_{4}$ 组成.

解 为求最大值, 我们在 $q>1$ 的条件下考虑. 不妨设 $w_{0}$ 半径是 1 , 则显然

$$
A_{i} A_{i+1} \in\left[q^{i+1}-q^{i}, q^{i+1}+q^{i}\right], i=0,1,2,3
$$

且当 $A_{i}$ 固定, $a \in\left[q^{i+1}-q^{i}, q^{i+1}+q^{i}\right]$ 时, 必能取出 $A_{i+1} \in w_{i+1}$ 使得

$$
A_{i} A_{i+1}=a, i=0,1,2,3 .
$$

所以题设成立等价于存在 $a \in \mathbb{R}^{+}$, 使得 $a \in\left[q^{i+1}-q^{i}, q^{i+1}+q^{i}\right], i=0,1,2,3$.

因为 $q>1$, 所以

$$
\begin{aligned}
\text { 原问题 } & \Leftrightarrow a \geq q^{4}-q^{3}>0, a \leq q+1 \\
& \Leftrightarrow 0 \geq q^{4}-q^{3}-q-1=\left(q^{2}+1\right)\left(q^{2}-q-1\right) \\
& \Leftrightarrow 0 \geq q^{2}-q-1=\left(q-\frac{\sqrt{5}+1}{2}\right)\left(q+\frac{\sqrt{5}-1}{2}\right) \\
& \Leftrightarrow q \leq \frac{\sqrt{5}+1}{2} .
\end{aligned}
$$

所以, $q>1$ 时存在 $q$ 满足条件的. 故所求最大的 $q$ 为 $\frac{\sqrt{5}+1}{2}$.

评析 此题是个简单题, 只需注意到 $A_{i} A_{i+1}$ 可独立地取遍 $\left[q^{i+1}-q^{i}, q^{i+1}+q^{i}\right]$的所有实数即可.

题 6. 设 $\triangle A B C$ 是以 $B C$ 为底边的等腰三角形. 点 $D$ 是腰 $A C$ 上的一点.点 $K$ 是 $\triangle B C D$ 的外接圆的劣弧 $C D$ 上的一点. 过 $A$ 点作 $B C$ 的平行线, 该平行线与射线 $C K$ 交于点 $T$. 设点 $M$ 为线段 $D T$ 的中点, 证明: $\angle A K T=\angle C A M$.

证明 在边 $A B$ 上截取 $A D_{1}=A D$, 则四边形 $B D_{1} D C$ 为等腰梯形, $B, D_{1}, D, C$ 四点共圆. 所以 $B, D_{1}, D, K, C$ 五点共圆, 这样有

$$
\angle D_{1} K T=180^{\circ}-\angle D_{1} K C=\angle D_{1} B C=180^{\circ}-\angle D_{1} A T \text {. }
$$



所以 $D_{1}, A, T, K$ 共圆, $\angle A K T=\angle A D_{1} T$.

延长 $A M$ 至 $A_{1}$ 使得 $A_{1} M=A M$, 结合 $M$ 为 $D T$ 的中点, 知四边形 $A T A_{1} D$为平行四边形, 所以 $A_{1}, D, D_{1}$ 三点共线. 由 $A D_{1}=A D=T A_{1}$ 得四边形 $A T A_{1} D_{1}$ 为等腰梯形. 进而有

$$
\angle C A M=\angle A A_{1} T=\angle A D_{1} T=\angle A K T
$$

故得证!

评析 此题是个常规几何题, 题中点, 线是很少的, 关系也很少, 只需充分利用题中对称性将该题转化为四点共圆问题即可.

## 题 7. 同十年级第八题

题 8. 设 $n$ 是一个正整数. 现来构造一个 $3 \times 3 \times 3$ 的立方体, 这个立方体由 26 个白色的单位立方体和 1 个黑色的单位立方体构成, 且黑色的单位立方体在这个 $3 \times 3 \times 3$ 的立方体的中心. 在此基础之上再来构造一个由 $n^{3}$ 个上述 $3 \times 3 \times 3$ 的立方体构成的 $3 n \times 3 n \times 3 n$ 的立方体. 确定 $T$ 的最小值, 有可能把其中的 $T$ 个白色的单位立方体染成红色之后使得每个白色的单位立方体总和某个红色的单位立方体有一个公共的顶点。

解 $T$ 的最小值为 $n^{3}+n^{2}$.

先证: (1) 对一行 $3 n$ 个点, 可分成 $n$ 组连续 3 个点, 每 3 个点的中间点染成黑色, 其余染成白色. 将这 $3 n$ 个点中某些点染红, 使每个白点与某红点相邻, 且有 $a$ 个白点被染红, $s$ 个点被染红, 则 $s \geq n+\frac{a}{n+1}$.

(1) 的证明 对第 $3 k-1$ 列, 设有 $b_{k}$ 个点染红, $k=1,2, \cdots, n$. 设第 1 列有 $a_{0}$ 个点染红, 第 $3 k$ 与 $3 k+1$ 列共有 $a_{k}$ 个点染红, $k=1,2, \cdots, n-1$, 第 $3 n$ 列有
$a_{n}$ 个点染红. 所以

$$
s=\sum_{i=1}^{n} b_{i}+\sum_{i=0}^{n} a_{i}, a=\sum_{i=0}^{n} a_{i}
$$

考虑第 $3 k+1$ 列得

$$
a_{k}+b_{k+1} \geq 1, k=0,1,2, \cdots, n-1
$$

考虑第 $3 k$ 列得

$$
b_{k}+a_{k} \geq 1, k=1,2 \cdots, n .
$$

所以对 $i_{0} \in\{0,1, \cdots, n\}$, 有

$$
s=a_{i_{0}}+\sum_{i=0}^{i_{0}-1}\left(a_{i}+b_{i+1}\right)+\sum_{i=i_{0}+1}^{n}\left(a_{i}+b_{i}\right) \geq a_{i_{0}}+i_{0}+\left(n-i_{0}\right)=n+a_{i_{0}},
$$

故

$$
s \geq n+\frac{\sum_{i_{0}=0}^{n} a_{i_{0}}}{n+1}=n+\frac{a}{n+1}
$$

结论 (1) 得证.

再证: (2) 对一个 $3 n \times 3 n$ 的表分成 $n^{2}$ 个 $3 \times 3$ 的小块, 每个小块中间染黑,其余染白. 将这 $3 n \times 3 n$ 的表中 $s$ 个格染红使每个白格与某红格有公共点, 且有 $a$ 个白格被染红, 则 $s \geq n^{2}+\frac{a}{n+1}$.

(2) 的证明 对第 $3 k-1$ 列设有 $b_{k}$ 个格染红, $c_{k}$ 个白格染红, $k=1,2, \cdots, n$.设第 1 列有 $a_{0}$ 个格染红, 第 $3 k$ 与 $3 k+1$ 列共有 $a_{k}$ 个格染红, $k=1,2, \cdots, n-1$,第 $3 n$ 列有 $a_{n}$ 个格染红. 所以,

$$
s=\sum_{i=1}^{n} b_{i}+\sum_{i=0}^{n} a_{i}, a=\sum_{i=0}^{n} a_{i}+\sum_{i=1}^{n} c_{i}
$$

考虑第 $3 k+1$ 列, 由 (1) 得

$$
a_{k}+b_{k+1} \geq n+\frac{c_{k+1}}{n+1}, k=0,1, \cdots, n-1
$$

考虑第 $3 k$ 列, 由 (1) 得

$$
b_{k}+a_{k} \geq n+\frac{c_{k}}{n+1}, k=1,2, \cdots, n .
$$

所以对 $i_{0} \in\{0,1, \cdots, n\}$, 有

$$
\begin{aligned}
s & =\sum_{i=0}^{i_{0}-1}\left(a_{i}+b_{i+1}\right)+\sum_{i=i_{0}+1}^{n}\left(a_{i}+b_{i}\right)+a_{i_{0}} \\
& \geq \sum_{i=0}^{i_{0}-1}\left(n+\frac{c_{i+1}}{n+1}\right)+\sum_{i=i_{0}+1}^{n}\left(n+\frac{c_{i}}{n+1}\right)+a_{i_{0}}
\end{aligned}
$$

即有

$$
s \geq n^{2}+\frac{\sum_{i=1}^{n} c_{i}}{n+1}+a_{i_{0}}
$$

所以

$$
s \geq n^{2}+\frac{\sum_{i=1}^{n} c_{i}}{n+1}+\frac{\sum_{i_{0}=0}^{n} a_{i_{0}}}{n+1}=n^{2}+\frac{a}{n+1} .
$$

结论 (2) 得证.

再证: (3) 对一个 $3 n \times 3 n \times 3 n$ 的立方体分成 $n^{3}$ 个 $3 \times 3 \times 3$ 的块. 每一块中心格染黑, 其余染白. 将 $3 n \times 3 n \times 3 n$ 的立方体中 $s$ 个格染红, 使每个白格与某红格有公共点, 且有 $a$ 个白格被染红, 则 $s \geq n^{3}+\frac{a}{n+1}$.

(3) 的证明 将立方体分为 $3 n$ 层, 第一层有 $a_{0}$ 个格染红, 第 $3 k-1$ 层有 $b_{k}$个格染红, 其中有 $c_{k}$ 个白格, $k=1,2, \cdots, n$. 第 $3 k$ 与 $3 k+1$ 层共有 $a_{k}$ 个格染红, $k=1,2, \cdots, n-1$, 第 $3 n$ 层有 $a_{n}$ 个格染红. 所以,

$$
s=\sum_{i=1}^{n} b_{i}+\sum_{i=0}^{n} a_{i}, a=\sum_{i=0}^{n} a_{i}+\sum_{i=1}^{n} c_{i}
$$

考虑第 $3 k+1$ 层, 由 $(2)$ 得

$$
a_{k}+b_{k+1} \geq n^{2}+\frac{c_{k+1}}{n+1}, k=0,1, \cdots, n-1
$$

考虑第 $3 k$ 层, 由 $(2)$ 得

$$
b_{k}+a_{k} \geq n^{2}+\frac{c_{k}}{n+1}, k=1, \cdots, n .
$$

所以对 $i_{0} \in\{0,1, \cdots, n\}$, 有

$$
\begin{aligned}
s & =\sum_{i=0}^{i_{0}-1}\left(a_{i}+b_{i+1}\right)+\sum_{i=i_{0}+1}^{n}\left(a_{i}+b_{i}\right)+a_{i_{0}} \\
& \geq a_{i_{0}}+\sum_{i=0}^{i_{0}-1}\left(n^{2}+\frac{c_{i+1}}{n+1}\right)+\sum_{i=i_{0}+1}^{n}\left(n^{2}+\frac{c_{i}}{n+1}\right) .
\end{aligned}
$$

即有

$$
s \geq n^{3}+\frac{\sum_{i=1}^{n} c_{i}}{n+1}+a_{i_{0}}
$$

所以

$$
s \geq n^{3}+\frac{\sum_{i=1}^{n} c_{i}}{n+1}+\frac{\sum_{i_{0}=0}^{n} a_{i_{0}}}{n+1}=n^{3}+\frac{a}{n+1}
$$

结论 (3) 得证.
回到原题, 设染了 $T$ 个格, 由 (3) 知

$$
T \geq n^{3}+\frac{T}{n+1}
$$

则有

$$
T \geq n^{3}+n^{2}
$$

构造: 将立方体分为 $3 n$ 层, 将第 $3 k$ 层与第 1 层 $(k=1,2, \cdots, n)$ 的 $n^{2}$ 个 $3 \times 3$ 的中心均染红. 易知满足题设条件.

综上所述, $T$ 的最小值为 $n^{3}+n^{2}$.

评析 此题是个较难的组合计数题. 此题的构造是很容易想到的, 但由于三维图形的复杂与抽象性可以先去考虑简单的一维, 二维的情形, 之后再将题目加强至白格染红的个数与黑格染红个数的关系可以发现最后的式子是恰好满足构造的, 而且可以发现在题中染形如 $(a, b, c)$ 的格 ( $a, b, c$ 中无模 3 同余 2 的数) 是无意义的。

