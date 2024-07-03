$$
\text { 数学新星网 当教师专栏 }
$$

www.nsmath.cn/jszl

# Fake USAMO 2020 试题解答与评析 

华接春 陈家烦

(长沙市长郡中学, 410002)

因为 COVID-19 疫情的原因, 今年的 USAMO 不能如期举办, AOPS 网站举办了一次线上的比赛, 命名为 Fake USAMO, 题目值得研究和欣赏. 本文给出了解答和评析.

## I. 试 题

1. 设 $C$ 是一个正整数, 正整数数列 $a_{1}, a_{2}, a_{3}, \cdots$ 满足 $a_{n+1}=\sqrt{a_{n}^{3}-C a_{n}}$对所有正整数 $n$ 都成立. 证明: 存在正整数 $N$ 使得 $a_{N}=a_{N+1}=a_{N+2}=\cdots$.
2. 给定正整数 $n$, Ankan 将 $1+2+\cdots+2 n$ 个点排列成 $2 n$ 行等边三角形阵 (向上摆放的). 定义一个关联是连接一点与在它下方的两点中一个线段, 对于给定的序列 $a_{1}, a_{2}, \cdots, a_{2 n}, a_{1}+a_{2}+\cdots+a_{2 n}=n, a_{i} \leq i, i=1,2, \cdots 2 n$. Bankan 从第 $i$ 行去掉 $a_{i}$ 个点, $i=1,2, \cdots, 2 n$. Ankan 希望画出 $n^{2}$ 个关联使得每个点恰在一个关联中. 若无论 Bankan 怎样选择去掉的点, Ankan 都能达到目的, 则称数列 $a_{1}, a_{2}, \cdots, a_{2 n}$ 为好的. 求好的数列的个数.
3. 不等边 $\triangle A B C$ 的外心为 $O$, 内心为 $I$. 内切圆 $\varpi$ 与边 $B C, C A, A B$ 分别相切于点 $D, E, F$. 记 $T$ 为 $D$ 在边 $E F$ 上的垂足. 直线 $A T$ 与 $\triangle A B C$ 的外接圆再次相交一点 $X \neq A . \triangle A E X$ 和 $\triangle A F X$ 的外接圆与圆 $\varpi$ 分别相交两点 $P \neq E$ 和 $Q \neq F$. 证明: 直线 $E Q, F P, O I$ 三线共点.
4. 有 $n$ 个学生坐在 MOP 教室里, 开始时他们每个人手上没有硬币. Evan 老师每分钟都会进行以下操作: 他挑选了两个拿着相同数量硬币的学生, 设为 $k$枚. 若 $k=0$ 时, 那么老师恰给他选出的二人中某一人发一枚硬币; 当 $k \neq 0$ 时，老师从其中一个同学处取出一枚硬币, 并将其交给他挑选的另一名学生. 直到最

修订日期: 2020-05-17.

![](https://cdn.mathpix.com/cropped/2024_02_26_fb553d60484aed51f237g-02.jpg?height=508&width=494&top_left_y=203&top_left_x=790)

题 3 图

后老师不能再做任何操作就结束. 证明: 在该操作结束时一定使得每个学生都按某种顺序各自持有 $0,1,2, \cdots, n-1$ 枚硬币.

5. 求所有无界函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$, 满足以下条件: 对成等差数列的三个整数 $a, b, c$, 有 $f(a), f(b), f(c)$ 按某种排列也成等差数列.
6. 函数 $f: \mathbb{N}^{+} \rightarrow \mathbb{N}^{+}$满足以下两个条件:

(1) 对任意的有限正整数数列 $a_{1}, a_{2}, \cdots, a_{k}, f\left(a_{1}\right)+f\left(a_{2}\right)+\cdots+f\left(a_{k}\right)$ 整除 $f\left(a_{1}+a_{2}+\cdots+a_{k}\right)$;

(2) 存在一个正整数 $m$ 使得 $f(m) \neq m f(1)$.

证明: 存在一个正整数 $n$, 使得 $\operatorname{gcd}(f(n), f(n+1), f(n+2), \cdots)>2020^{n}$.

## II. 解 答

题 1 设 $C$ 是一个正整数, 正整数数列 $a_{1}, a_{2}, a_{3}, \cdots$ 满足 $a_{n+1}=\sqrt{a_{n}^{3}-C a_{n}}$对所有正整数 $n$ 都成立. 证明: 存在正整数 $N$ 使得 $a_{N}=a_{N+1}=a_{N+2}=\cdots$.

证明 1 (于文騫) 由于 $a_{n+1}=\sqrt{a_{n}^{3}-C a_{n}}$, 故

$$
a_{n+1}^{2}=a_{n}^{3}-C a_{n}=a_{n}\left(a_{n}^{2}-C\right) .
$$

令 $b_{n}=\left(a_{n}, C\right)$, 则

$$
b_{n}^{2}\left|a_{n}\left(a_{n}^{2}-C\right) \Rightarrow b_{n}^{2}\right| a_{n+1}^{2} \Rightarrow b_{n}\left|a_{n+1} \Rightarrow b_{n}\right| b_{n+1},
$$

故 $\left\{b_{n}\right\}$ 不减. 而 $b_{n} \mid C$, 则 $b_{n} \leq C$, 即 $\left\{b_{n}\right\}$ 有界. 故由 $\left\{b_{n}\right\}$ 为正整数, 知 $\left\{b_{n}\right\}$ 最终为常数数列.

设对于 $n \geq N, b_{n}=t$. 令 $d_{n}=\frac{a_{n}}{t}, C=t C^{\prime}$. 下仅考虑 $n \geq N$, 则

$$
a_{n+1}^{2}=a_{n}\left(a_{n}^{2}-C\right),
$$

得

$$
d_{n+1}^{2}=d_{n}\left(t \cdot d_{n}^{2}-C^{\prime}\right) .
$$

易知 $\left(d_{n}, t \cdot d_{n}^{2}-C^{\prime}\right)=\left(d_{n}, C^{\prime}\right)=1$, 故 $d_{n}$ 为平方数. 同理 $d_{n+1}$ 为平方数, 则

$$
d_{n+1}^{2} \text { 为四次方数 } \Rightarrow d_{n} \text { 为四次方数 } \Rightarrow d_{n+1} \text { 为四次方数 } \Rightarrow \cdots \text {. }
$$

可推出 $\forall k \in \mathbb{N}^{+}, d_{n}$ 为 $2^{k}$ 次方数, 故 $d_{n}=1$, 即 $a_{n}=t$ 为常数.

证明 2 (廖子豪) 由 $a_{n+1}=\sqrt{a_{n}^{3}-C a_{n}}$, 知 $C=a_{n}^{2}-\frac{a_{n+1}^{2}}{a_{n}}$.

引理 1 若 $a_{n+1}>a_{n}$, 则 $a_{n+2}>a_{n+1}$.

证明 由(1)式可知:

$$
a_{n+1}^{2}-a_{n}^{2}=\frac{a_{n+2}^{2}}{a_{n+1}}-\frac{a_{n+1}^{2}}{a_{n}}>0,
$$

假设 $a_{n+2} \leq a_{n+1}$, 则

$$
\frac{a_{n+2}^{2}}{a_{n+1}}-\frac{a_{n+1}^{2}}{a_{n}}<a_{n+2}-a_{n+1}<0
$$

矛盾!

引理 2 若 $p$ 为素数, 对任意 $n \in \mathbb{N}^{+}$, 有 $v_{p}\left(a_{n}\right) \leq v_{p}(c)$. 特别地, $p \mid a_{n} \Rightarrow$ $p \mid c$.

证明 假设存在 $n \in \mathbb{N}^{+}$, 使 $v_{p}\left(a_{n}\right)>v_{p}(c)$, 则

$$
v_{p}\left(a_{n}^{2}\right)=2 v_{p}\left(a_{n}\right)>v_{p}(c) .
$$

由(1)式知:

$$
\begin{aligned}
& v_{p}\left(\frac{a_{n+1}^{2}}{a_{n}}\right)=v_{p}\left(a_{n}^{2}-c\right)=v_{p}(c) \\
\Leftrightarrow & v_{p}\left(a_{n+1}\right)=\frac{v_{p}\left(a_{n}\right)+v_{p}(c)}{2}>v_{p}(c) \\
\Leftrightarrow & v_{p}\left(a_{n+1}\right)-v_{p}(c)=\frac{v_{p}\left(a_{n}\right)-v_{p}(c)}{2} .
\end{aligned}
$$

类似归纳可知: 对任意 $k \in \mathbb{N}^{+}$, 有

$$
v_{p}\left(a_{n+k}\right)-v_{p}(c)=\frac{v_{p}\left(a_{n}\right)-v_{p}(c)}{2^{k}} \in \mathbb{Z}
$$

令 $2^{k}>v_{p}\left(a_{n}\right)-v_{p}(c)$, 矛盾!

回到原题:

(1) $\forall n \in \mathbb{N}^{+}, a_{n+1} \leq a_{n}$, 结合 $\left\{a_{n}\right\}$ 为正整数数列, 知其必为最终常数;

(2) $\exists n \in \mathbb{N}^{+}, a_{n+1}>a_{n}$, 由引理 $1, a_{n}<a_{n+1}<a_{n+2}<\cdots$, 故 $\left\{a_{n}\right\}$ 无上界, 但由引理 2 , 数列 $\left\{a_{n}\right\}$ 的素因子集有限, 且在 $\left\{a_{n}\right\}$ 中幕次有界, 则 $\left\{a_{n}\right\}$ 有上
界, 矛盾!

综上: 存在一个正整数 $N$ 使得 $a_{N}=a_{N+1}=a_{N+2}=\cdots$.

评注 本题难度不大, 方法一从 $\left(a_{n}, C\right)$ 的不减性入手, 直接考虑充分大的情况,想法较自然; 方法二是通过考虑 $C$ 的素因子在 $a_{n}$ 中的幂次, 从大小上推出矛盾.

题 2 给定正整数 $n$, Ankan 将 $1+2+\cdots+2 n$ 个点排列成 $2 n$ 行等边三角形阵 (向上摆放的). 定义一个关联是连接一点与在它下方的两点中一个线段,对于给定的序列 $a_{1}, a_{2}, \cdots, a_{2 n}, a_{1}+a_{2}+\cdots+a_{2 n}=n, a_{i} \leq i, i=1,2, \cdots 2 n$. Bankan 从第 $i$ 行去掉 $a_{i}$ 个点, $i=1,2, \cdots, 2 n$. Ankan 希望画出 $n^{2}$ 个关联使得每个点恰在一个关联中. 若无论 Bankan 怎样选择去掉的点, Ankan 都能达到目的, 则称数列 $a_{1}, a_{2}, \cdots, a_{2 n}$ 为好的. 求好的数列的个数.

解 (雷思聪) 对于好数列 $\left\{a_{i}\right\}_{i=1}^{2 n}$, 先证明如下一个性质:

$$
a_{1}=a_{3}=\cdots=a_{2 n-1}=0, a_{2 n} \leq n
$$

我们对三角形阵进行黑白染色, 奇数行的点染黑色, 偶数行的点染白色, 则黑点数为 $n^{2}$, 白点数为 $n^{2}+n$, 又注意到每个关联连接了一白一黑, 且任何一个点不出现在多个关联中, 因为连了 $n^{2}$ 个关联, 所以有 $n^{2}$ 个黑点未被去掉, 这样全部黑点未去掉, 则 $a_{1}=a_{3}=\cdots=a_{2 n-1}=0$. 又因为至多去掉 $n$ 个点, 所以 $a_{2 n} \leq n$.

因此我们可将 $a_{2 k+1}$ 全视作 “ 0 ”. 定义“好段”为满足 $(0,0, \cdots, k)$ 的形式, $k \in \mathbb{N}^{+}$. 下面我们证明:好数列的充要条件是 $a_{2}, a_{4}, \cdots, a_{2 n}$ 可被分成若干好段.

首先证明必要性. 先证明:若 $a_{2 k}=t$, 则 $a_{2 k-2}=\cdots=a_{2 k-2(t-1)}=0, k, t \in$ $\mathbb{N}^{+}$且 $t \geq 2$.

我们对三角形阵上的点进行标号 $b_{i j}$, 其中 $i$ 表示行数, $j$ 表示此点位于第 $i$行的从左至右第 $j$ 个位置, 并记所有黑点组成集合为 $X$, 所有白点组成集合为 $Y$,若 $a_{2 k}=t$, 且存在 $q$ 使得 $a_{2 k-2 q} \geq 1,1 \leq q \leq t-1, q \in \mathbb{N}^{+}$.

由已证性质可知

$$
a_{2 k-1}=a_{2 k-3}=\cdots=a_{2 k-2 q+1}=0
$$

先去掉 $b_{2 k, 1}, \cdots, b_{2 k, t}$ 与 $b_{2 k-2 q 1}$, 记

$$
Y^{\prime}=Y \backslash\left\{b_{2 k, 1}, \cdots, b_{2 k, t} ; b_{2 k-2 q, 1}\right\}
$$

若此时数列是好的, 则关联形成了 $X \rightarrow Y^{\prime}$ 的单射 $f$, 考虑

$$
Z=\left\{b_{2 k-2 q+2 i+1, j_{i}} \mid 0 \leq i \leq q-1,1 \leq j_{i} \leq i+1\right\} \subseteq X
$$

则

$$
|Z|=1+\cdots+q=\frac{q(q+1)}{2}
$$

而

$$
|f(Z)|=2+\cdots+q=\frac{q(q+1)}{2}-1<|Z|,
$$

与 $f$ 为单射矛盾! 由此得必要性成立.

再证充分性. 因为 $a_{2 n}=k \geq 2$, 所以易知可将剩余 $2 n-k$ 个点与第 $2 n-1$行的点形成关联, 此时, 第 $2 n-1$ 行仅剩 $k-1$ 个点未关联, 因为第 $2 n-2$ 行没有点被去掉, 所有可将 $k-1$ 点与 $2 n-2$ 行的点形成关联, 接下来将第 $2 n-2$ 行已关联的点视作被去掉的点, 化归为 $\left(a_{1}, a_{2}, \cdots, a_{2 n-3}, k-1\right)$ 的情况, 此时仍是好数列. 当 $k=1$ 时, 容易化归为 $n-1$ 的情形. 递推易知充分性成立!

最后进行计数. 一个好数列要求 $a_{2 n} \neq 0$, 建立 $\left\{a_{2}, a_{4}, \cdots, a_{2 n-2}\right\}$ 的所有子集到好数列的对应. 对于一个子集 $\left\{a_{2 i_{1}}, \cdots, a_{2 i_{t}}\right\}$, 所对应的好数列满足

$$
\left\{\begin{array}{l}
a_{2 i_{1}}=i_{1}, \\
a_{2 i_{j+1}}=i_{j+1}-i_{j}, 1 \leq j \leq t-1, \\
a_{2 n}=n-i t, \\
a_{2 i}=0, i \neq\left\{i_{1}, \cdots, i_{t}, n\right\} .
\end{array}\right.
$$

由以上充要条件的说明, 易知这是一一对应.

故好数列数 $=\left\{a_{2}, a_{4}, \cdots, a_{2 n-2}\right\}$ 的子集数量 $=2^{n-1}$.

评注 此题是一道中等偏易的组合题, 适合通过小情况进行试探来入手, 解题的关键在于发掘好数列的充要条件以及一些特殊位置的特殊之处(比如每行第一点). 构造映射计数的手法有一定技巧性, 这一步用归纳法也是不难得到的.

题 3 不等边 $\triangle A B C$ 的外心为 $O$, 内心为 $I$. 内切圆 $\varpi$ 与边 $B C, C A, A B$分别相切于点 $D, E, F$. 记 $T$ 为 $D$ 在边 $E F$ 上的垂足. 直线 $A T$ 与 $\triangle A B C$ 的外接圆再次相交一点 $X \neq A . \triangle A E X$ 和 $\triangle A F X$ 的外接圆与圆 $\varpi$ 分别相交两点 $P \neq E$ 和 $Q \neq F$. 证明: 直线 $E Q, F P, O I$ 三线共点.

证明 1 (刘尧瑞, 刘楚才) 取 $\odot A E F$ 与 $\odot A B C$ 的交点 $R$, 则

$$
\angle R F A=\angle R E A, \angle R B A=\angle R C A, \Rightarrow \triangle R F B \sim \triangle R E C \Rightarrow \frac{R F}{R E}=\frac{B F}{E C}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_fb553d60484aed51f237g-06.jpg?height=626&width=640&top_left_y=201&top_left_x=708)

熟知 $\frac{B F}{E C}=\frac{F T}{T E}$, 故 $R T$ 平分 $\angle F R E$. 又 $R, I$ 在 $\odot A E F$ 上, $R I$ 平分 $\angle F R E$, 故 $R, T, I$ 共线. 延长 $A R, E F$ 交于 $V$, 由 $\angle I R A=90^{\circ}, V, F, T, E$ 为调和点列. (1)由

$$
\angle T X P=\angle A X P=\angle P E C=\angle P F E=\angle P F T
$$

故 $F, T, P, X$ 共圆. 同理 $E, T, Q, X$ 共圆. 于是由根心定理 $P F, E Q, T X$ 共点于 $K$. 又由根心定理, $F Q, A X, P E$ 共点于 $U$. 延长 $E F, P Q$ 交于 $V^{\prime}$, 则对完全四边形 $V^{\prime} Q P E U F$ 知 $V^{\prime} F T E$ 为调和点列.

由(1), (2)知 $V \equiv V^{\prime}$, 即 $R A, E F, P Q$ 三线共点于 $V$. 注意到

$$
U F \cdot U Q=U A \cdot U X, V F \cdot V E=V R \cdot V A,
$$

因此 $U V$ 为内切圆与外接圆根轴, 故 $I O \perp U V$. 由 Brocard 定理知 $I K \perp U V \Rightarrow$ $K, I, O$ 共线.

证明 2 (范竣杰)设 $\triangle A B C$ 与 $A, B, C$ 对应的旁心 $I_{A}, I_{B}, I_{C}$, 弧 $B A C$ 中点为 $N$. 熟知 $N, D, X$ 共线. 由

$$
\angle N X C=\angle N C D \Rightarrow \triangle N D C \sim \triangle N C X \Rightarrow \frac{N C}{C D}=\frac{N X}{X C}
$$

又

$$
N C=N I_{C}, D C=E C \Rightarrow \frac{N I_{C}}{E C}=\frac{N X}{X C}
$$

结合 $\angle I_{C} N X=\angle E C X$ 知

$$
\triangle I_{C} N X \sim \triangle E C X \Rightarrow \angle N I_{C} X=\angle C E X \Rightarrow I_{C} A E X \text { 共圆. }
$$

延长 $I_{C} F$ 交 $\odot I$ 于 $P^{\prime}$, 则 $\angle F P^{\prime} E=\angle A E F=\angle E A N \Rightarrow A I_{C} P^{\prime} E$ 共圆. 因此 $I_{C} X P^{\prime} E A$ 共圆, 故 $P^{\prime} \equiv P$. 同理, $A F Q X I_{B}$ 共圆. 由导角易知 $P Q I_{B} I_{C}$ 共圆,
由根心定理 $P I_{C}, Q I_{B}, A X$ 共点于 $K$. 注意到 $\triangle I_{A} I_{B} I_{C}$ 与 $\triangle D E F$ 位似, 故 $K$为位似中心. 记 $\triangle I_{A} I_{B} I_{C}$ 外心为 $W$, 熟知 $I, O, W$ 共线. 又 $K, I, W$ 共线, 故 $K, I, O, W$ 共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_fb553d60484aed51f237g-07.jpg?height=716&width=719&top_left_y=453&top_left_x=677)

评注 本题是一道有一定难度的几何题. 法一利用垂直导共线, 法二则发现 $K$ 为 $\odot I, \odot W$ 位似中心, 利用位似性质证明共线, 这都是十分经典的手法.

题 4 有 $n$ 个学生坐在 MOP 教室里, 开始时他们每个人手上没有硬币. Evan 老师每分钟都会进行以下操作: 他挑选了两个拿着相同数量硬币的学生, 设为 $k$枚. 若 $k=0$ 时, 那么老师恰给他选出的二人中某一人发一枚硬币; 当 $k \neq 0$ 时,老师从其中一个同学处取出一枚硬币, 并将其交给他挑选的另一名学生. 直到最后老师不能再做任何操作就结束. 证明: 在该操作结束时一定使得每个学生都按某种顺序各自持有 $0,1,2, \cdots, n-1$ 枚硬币.

证明 (于文骞) 对 $n$ 归纳.

(1) 当 $n=2$ 时显然成立;

(2) 假设 $n$ 时命题成立. 当 $n+1$ 时, 设这 $n+1$ 个学生拥有的硬币数为 $a_{1}, a_{2}, \cdots, a_{n+1}$. 最初 $a_{1}=a_{2}=\cdots=a_{n+1}=0$. 每次 Evan 操作两个同为 0 的时, 不妨设 Evan 给编号小的 $a_{i}$ 一枚硬币, 这样 $a_{n+1}$ 将永远保持 0 不变. 故可不妨设操作两个 0 时都为 $a_{n+1}$ 与某个 $a_{i}$. 由于操作结束时至多一个 0 , 且 $a_{n+1}$ 总是 0 , 故其余 $a_{i}$ 都大于 0 , 即它们均与 $a_{n+1}$ 一起被操作过. 对于 $i=1,2, \cdots, n$,分别找到 $a_{i}$ 第一次被操作的时刻, 显然是与 $a_{n+1}$ 操作, 并将其移至所有操作的最前面, 这不会改变最终状态, 也不会使中间的某一步操作不合法. 故前 $n$ 步操
作后，

$$
a_{n+1}=0, a_{1}=a_{2}=\cdots=a_{n}=1 .
$$

对于之后每步操作出 $a_{i}=0$ 时, 均可在之后的操作中找到第一次 $a_{i}$ 操作, 同上将该操作移至该步之后, 并将两步操作视为一个整体, 则对于 $a_{1}-1, a_{2}-$ $1, \cdots, a_{n}-1$ 可视作 $n$ 时操作. 由归纳假设最终

$$
\left\{a_{1}-1, a_{2}-1, \cdots, a_{n}-1\right\}=\{0,1, \cdots, n-1\},
$$

即

$$
\left\{a_{1}, a_{2}, \cdots, a_{n+1}\right\}=\{0,1, \cdots, n\} .
$$

评注 此方法巧妙地将 $n+1$ 的情况化归为 $n$ 的情况, 值得借鉴. 另外, 由本方法中交换操作顺序的想法, 容易直接证明所有的操作顺序本质都是等同的.

题 5. 求所有无界函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$, 满足以下条件: 对成等差数列的三个整数 $a, b, c$, 有 $f(a), f(b), f(c)$ 按某种排列也成等差数列.

解 (于文骞) 先证明: $f$ 为单射. 否则, 若 $\exists x, y \in \mathbb{Z}, f(x)=f(y)=d$, 不妨设 $y>x=0$ (由平移不变性). 对 $k \in \mathbb{Z}$, 考虑 $k y,(k+1) y,(k+2) y$, 结合归纳易证 $\forall t \in \mathbb{Z}, f(t y)=d$. 令

$$
S=\left\{n \in \mathbb{Z}|| f(n)\left|>\max _{|i|<|n|}\right| f(i)|,| n \mid>3 y\right\}
$$

由无界性知 $S$ 为无限集, 任取 $n_{0} \in S$, 不妨设 $n_{0}>0$, 记 $f\left(n_{0}\right)=t$. 对 $r \in$ $\{1,2,3\},\left(n_{0}<0\right.$ 时类似 $\left.r \in\{-1,-2,-3\}\right)$ 由题意知 $f(r y), f\left(n_{0}\right), f\left(2 r y-n_{0}\right)$成等差数列. 由 $n>3 y$ 知

$$
|r y|<n_{0},\left|2 r y-n_{0}\right|<n_{0} \Rightarrow|t|>|d|,|t|>\left|f\left(2 r y-n_{0}\right)\right|,
$$

故 $f\left(2 r y-n_{0}\right)$ 最多有两个取值 $\left\{\frac{d+t}{2}, 2 d-t\right\}$.

但 $f\left(2 y-n_{0}\right), f\left(4 y-n_{0}\right), f\left(6 y-n_{0}\right)$ 也成等差数列, 且三者中必有两者相同, 故均相同. 同前易知 $\forall k \in \mathbb{Z}, f\left(2 k y-n_{0}\right)$ 为常值. 由 $S$ 为无限集, 其中必有三个 $\bmod 2 y$ 同余, 且绝对值不同. 设为 $n_{1}, n_{2}, n_{3}$, 则 $n_{1}, n_{2}, n_{3}$ 中又有两个对应的 $f\left(2 k y-n_{i}\right)$, 同为 $\frac{d+f\left(n_{i}\right)}{2}$ 或 $2 d-f\left(n_{i}\right)$. 这推出 $f\left(n_{i}\right)=f\left(n_{j}\right)$, 而 $\left|n_{i}\right| \neq\left|n_{j}\right|$, 与 $S$ 的定义矛盾, 即 $f$ 为单射.

考虑

$$
T=\{|f(i+1)-f(i)| \mid i \in \mathbb{Z}\}
$$

由 $T \subseteq \mathbb{N}^{+}$知 $T$ 中存在最小数 $w$, 不妨设 $f(1)=w, f(0)=0$. 则由 $f(i), f(i+$ 1), $f(i+2)$ 成等差数列知

$$
\frac{|f(i+1)-f(i)|}{|f(i+2)-f(i+1)|}=1 \text { 或 } 2 \text { 或 } \frac{1}{2} \text {. }
$$

结合 $w$ 的最小性归纳易证 $\forall x \in T, w \mid x$, 故 $\forall i \in \mathbb{Z}, w \mid f(i)$. 令 $g(x)=\frac{f(x)}{w}$,易知 $g(x)$ 仍满足条件, 且 $g(0)=0, g(1)=1$.

易知 $g(-1), g(2) \in\{-1,2\}$, 而且 $g(-1) \neq g(2)$.

(i) 若 $g(-1)=-1, g(2)=2$. 结合单射归纳易证 $g(n) \equiv n$ 即为唯一解.

(ii) 若 $g(-1)=2, g(2)=-1$. 考虑 $g(-3), g(-1), g(1)$ 成等差数列知 $g(-3)=3$. 考虑 $g(-3), g(-2), g(-1)$ 成等差数列知 $g(-2)=4$, 则 $g(-2), g(0)$, $g(2)$ 不成等差数列, 矛盾! 无解.

故 $g(n)=n$ 为唯一解, 得 $f(n)=k n+b, k \neq 0$ 为 $f(n)$ 的所有解.

评注 本题难度中等, 不证单射性, 不优化直接分类讨论也可以解决本题. 本方法证明单射的手段对处理类似问题有一定借鉴意义;单射性有更简单的证明方法. 反设 $\exists a, b, \in \mathbb{Z}, f(a)=f(b)=t$, 不妨设 $a=0$, 易知 $\forall k \in \mathbb{Z}, f(k b)=t$,任取 $c \in\{0,1, \cdots, 2 b-1\}$, 则对于 $k \in \mathbb{Z}, f(c), f(k b), f(2 k b-c)$ 成等差数列, 则 $f(2 k b-c)$ 最多三个取值, 故 $f(n)$ 取值有限, 即 $f(n)$ 有界, 矛盾! 本题去掉无界性也可求出所有解, 感兴趣的读者不妨尝试下.

题 6. 函数 $f: \mathbb{N}^{+} \rightarrow \mathbb{N}^{+}$满足以下两个条件:

(1) 对任意的有限正整数数列 $a_{1}, a_{2}, \cdots, a_{k}, f\left(a_{1}\right)+f\left(a_{2}\right)+\cdots+f\left(a_{k}\right)$ 整除 $f\left(a_{1}+a_{2}+\cdots+a_{k}\right)$;

(2) 存在一个正整数 $m$ 使得 $f(m) \neq m f(1)$.

证明: 存在一个正整数 $n$, 使得 $\operatorname{gcd}(f(n), f(n+1), f(n+2), \cdots)>2020^{n}$.

证明 (郑哲皓) (1) 先证 $\exists c_{0} \in \mathbb{R}^{+}$对充分大的 $n \in \mathbb{N}^{+}, f(n) \geq 2^{n} \cdot c_{0}$.

不妨设 $f(1)=1$, 否则考虑 $f^{\prime}(x)=\frac{f(x)}{f(1)} \in \mathbb{Z}$. 因为对 $\forall n \in \mathbb{N}^{+}$,

$$
\sum_{i=1}^{n} f(1)|f(n) \Rightarrow n f(1)| f(n)
$$

取 $m=\min \{k \mid f(k) \neq k\}$, 记 $a=f(m)-m$. 对 $\forall n>a \cdot m$, 设 $n=$ $m q+r(q \geq a, 0 \leq r<m)$. 对 $\forall 0 \leq k \leq q$, 由

$$
\begin{aligned}
k \cdot m+[(q-k) m+r] \cdot 1=n & \Rightarrow k f(m)+[(q-k) m+r] \cdot f(1) \mid f(n) \\
& \Rightarrow k a+n \mid f(n) .
\end{aligned}
$$

因为 $(a, a+1)=1$, 所以 $\left\{0, a, \cdots, a^{2}\right\}$ 遍历模 $a+1$ 的完系, 则 $\exists 0 \leq k \leq q$ 使得

$$
a+1|k a+n \Rightarrow a+1| f(n)(\forall n>a) .
$$

又因为对 $n \in \mathbb{N}^{+}, f(n)+1 \mid f(n+1)$. 对 $n>a q$, 有

$$
(a+1, f(n)+1)|(f(n), f(n)+1)=1 \Rightarrow(a+1)(f(n)+1)| f(n+1),
$$

故由 $a+1 \geq 2$ 知

$$
f(n+1) \geq 2(f(n)+1) \geq 2 f(n) \geq \cdots \geq 2^{n-a m} f(a m+1) .
$$

取 $c_{0}=\frac{f(a m+1)}{2^{a m+1}}$, 则 $\forall n>a m$,

$$
f(n) \geq 2^{n-1-a m} f(a m+1)=2^{n} c_{0}
$$

(2) 再证: $\forall c \in \mathbb{R}^{+}, \exists N \in \mathbb{N}^{+}$, 对素数 $p>N$ 及 $\alpha, n \in \mathbb{N}^{+}$使得 $n>\frac{p^{\alpha}}{c}$ 必定成立 $p^{\alpha} \mid f(n)$.

先取充分大的 $t \in \mathbb{N}^{+}$, 令 $b=f(t)-t$, 由 (1) 得 $b \neq 0$, 令 $d=(b, a)$, 取 $N=a^{2} b^{2}$, 则 $(p, d)=1$, 由中国剩余定理可取

$$
\left\{\begin{array}{l}
x \equiv-n\left(\bmod p^{\alpha}\right) \\
x \equiv 0(\bmod d)
\end{array}\right.
$$

且 $p^{\alpha} d<x \leq 2 p^{\alpha} d$. 再取 $z \in(0, b]$ 使 $z a \equiv x(\bmod b)$ (由 $(a, b) \mid x$ 知有解).

考虑到

$$
a z \leq a b<x \Rightarrow \exists w \in \mathbb{N}^{+}, z a+b w=x
$$

此时 $t$ 取充分大有

$$
z m+w t<(z+w) t=t \cdot \frac{x-z(a-b)}{b}<t \cdot \frac{2 x}{b}<\frac{4 t p^{\alpha} d}{2^{t} c_{0}-t}<\frac{p^{\alpha}}{c} .
$$

因此 $\exists \delta \in \mathbb{N}^{+}, n=z m+w t+\delta$, 故

$$
z f(m)+w f(t)+\delta f(1) \mid f(n),
$$

从而

$$
z a+w b+n \mid f(n)
$$

又因为 $z a+w b+n=x+n \equiv 0\left(\bmod p^{\alpha}\right)$, 所以 $p^{\alpha} \mid f(n)$, 结论成立.

(3) 再证:对 $\forall n \in \mathbb{N}^{+}, n \geq 3,[1,2, \cdots, n] \geq 2^{n-1}$.

先证一个恒等式, 对 $\forall n>1$, 有

$$
(n+1) \cdot\left[C_{n}^{0}, C_{n}^{1}, \cdots, C_{n}^{n}\right]=[1,2, \cdots, n+1]
$$

(1)先证右边整除左边, 这是因为

$$
k+1 \mid(k+1) C_{n+1}^{k+1}=(n+1) C_{n}^{k},(0 \leq k \leq n) .
$$

(2)再证左边整除右边, 只需证

$$
\left.(i+1) C_{n+1}^{i+1} \mid[1,2, \cdots, n+1] \text {, (由于 }(i+1) C_{n+1}^{i+1}=(n+1) C_{n}^{i}\right) \text {. }
$$

注意到恒等式

$$
\frac{a !}{(x+1) \cdots(x+a)}=\sum_{j=1}^{a} \frac{(-1)^{j-1} \cdot j \cdot C_{a}^{j}}{x+j} .
$$

令 $x=n-i, a=i+1$, 则

$$
\begin{aligned}
\frac{1}{C_{n+1}^{n-i}} & =\frac{(i+1) !}{(n-i+1) \cdots(n+1)} \\
& =\sum_{j=1}^{i+1} \frac{(-1)^{j-1} \cdot j \cdot C_{i+1}^{j}}{n-i+j} \\
& =(i+1) \sum_{j=1}^{i+1} \frac{(-1)^{j-1} C_{i}^{j-1}}{n-i+j} \\
& =\frac{(i+1) \cdot S}{[1,2, \cdots, n+1]}
\end{aligned}
$$

(化为分数, $S \in N^{+}$), 于是

$$
C_{n+1}^{n-i} \mid[1,2, \cdots, n+1]
$$

即

$$
C_{n+1}^{i+1} \mid[1,2, \cdots, n+1]
$$

$(*)$ 式成立.

所以对任意 $n \geq 3$,

$$
\begin{aligned}
{[1,2, \cdots, n] } & =n \cdot\left[C_{n-1}^{0}, C_{n-1}^{1}, \cdots, C_{n-1}^{n-1}\right] \\
& \geq n \cdot \max _{0 \leq i \leq n-1}\left\{C_{n-1}^{i}\right\} \\
& \geq n \cdot \frac{1}{n} \cdot \sum_{i=0}^{n-1} C_{n-1}^{i}=2^{n-1} .
\end{aligned}
$$

(4) 最后证明原题:取 $c=\left\lceil 2 \log _{2} 2020\right\rceil$, 待定 $n \in \mathbb{N}^{+}$充分大. 由 (3) 知, 对任意素数 $p>N, \alpha \in \mathbb{N}^{+}$使 $p^{\alpha}<c \cdot n$ 都有 $p^{\alpha} \mid f(k),(k \geq n)$ 这样的 $\alpha$ 即为 $[1,2, \cdots, c n]$ 中的 $p$ 幕次(对任一素数 $p$ 记 $\alpha(p)$ 为 $p$ 在 $[1,2, \cdots, c n]$ 中幕次).因此

$$
[1,2, \cdots, c n] \mid[\operatorname{gcd}(f(n), f(n+1), \cdots)] \cdot \prod_{p \leq N} p^{\alpha(p)}
$$

则 $n$ 满足 $2020^{n}>2(c n)^{N}$ 时

$\operatorname{gcd}(f(n), f(n+1), \cdots) \geq \frac{[1,2, \cdots, c n]}{\prod_{p \leq N} p^{\alpha(p)}} \geq \frac{2^{c n-1}}{(c n)^{N}}>\frac{1}{2} \cdot \frac{2020^{2 n}}{(c n)^{N}}>2020^{n}$.

评注 本题颇有难度, 难点在于结论 (2) 的诱导性不强, 加上其本身的证明也不容易. 在知道结论 (3) 并且明确目标是证明 $[1,2, \cdots, c n] \mid f(k) \cdot T(k \geq n, T$为常数)的情况下或许能反推出结论. 结论 (2) 中引入新的变量 $t, b$ 是一大亮点,这样在可控范围内引入新的参量是值得借鉴的获得更强结果的方法.

