# 第四十七期问题征解解答与点评 

张端阳

第一题 在圆内接四边形 $A B C D$ 中, 对角线 $A C, B D$ 交于点 $E$, 延长 $A B, D C$交于点 $M$, 延长 $A D, B C$ 交于点 $N$. 设 $\triangle A B E$ 的外接圆与直线 $B C$ 交于点 $P$, $\triangle A D E$ 的外接圆与直线 $C D$ 交于点 $Q$, 直线 $P Q, M N$ 交于点 $L$.

证明: (1) $A L \perp A C ;(2)$ 直线 $B Q, P D$ 的交点在直线 $A L$ 上.

(成都树德中学学生 李雨航 供题)

证明 (根据嘉兴一中姚云皓同学的解答整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_f803a7ef5fd2eba84bbbg-1.jpg?height=705&width=880&top_left_y=1304&top_left_x=588)

(1) 因为

$$
\angle A E P=\angle A B P=\angle A D C=\angle C E Q,
$$

所以 $L, P, E, Q$ 共线.

设 $F$ 是完全四边形 $N A D C M B$ 的密克点, 由 Brocard 定理, $F$ 在 $M N$ 上, 且 $E F \perp M N$.

结合 $F, B, A, N$ 共圆, 知

$$
\angle F L E=\angle P N L+\angle N P L=\angle F A B+\angle B A E=\angle F A E \text {. }
$$

于是 $F, E, A, L$ 共圆, 故 $\angle L A E=\angle E F M=90^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_f803a7ef5fd2eba84bbbg-2.jpg?height=765&width=880&top_left_y=300&top_left_x=588)

(2) 因为

$$
\angle E A Q=\angle E D Q=\angle E A B=\angle E P B
$$

所以 $A, P, C, Q$ 和 $B, P, D, Q$ 分别共圆.

设直线 $A L$ 与 $A, B, C, D$ 所共圆及 $A, P, C, Q$ 所共圆分别交于点 $H 、 I, J$ 是 $H I$ 的中点.

由 (1) 知 $\angle I Q M=\angle H D C=90^{\circ}$, 所以 $J$ 在 $D Q$ 的中垂线上. 同理, $J$ 也在 $B P$ 的中垂线上, 故 $J$ 是 $B, P, D, Q$ 所共圆的圆心.

对圆内接四边形 $B P D Q$, 对角线交于点 $E$, 一组对边交于点 $C$. 因为 $C E \perp A L$,且 $A L$ 经过圆心 $J$, 所以由 Brocard 定理知 $D P, B Q, A L$ 交于一点.

综上, 命题得证.

评注 (1). 本题本质上与 2018 年美国数学奥林匹克第五题相同:

在圆内四边形 $A B C D$ 中, 直线 $A C$ 与 $B D$ 交于点 $E$, 直线 $A B$ 与 $C D$ 交于点 $F$, 直线 $B C$ 与 $D A$ 交于点 $G$, 已知 $\triangle A B E$ 的外接圆与 $B C$ 交于 $B, P$, 且 $C, B, P, G$ 按此顺序排列, $\triangle A D E$ 的外接圆与直线 $C D$ 相交于 $D, Q$, 且 $C, Q, D, F$按此顺序排列. 证明: 若直线 $F P$ 与 $G Q$ 相交于 $M$, 则 $\angle M A C=90^{\circ}$.

(2). 除了解答中的方法, 常见的方法还有利用梅涅劳斯定理、调和、反演等.

(3). 江苏省扬州中学林圣, 福州三中李佳鸿, 哈尔滨师范大学附属中学汤盛宣, 海亮初级中学王圣迪, 江苏省昆山中学李子腾, 南昌二中万暗翔, 宁波市第十五中学庄子曰, 䨉州二中周幻帆, 上海市实验学校潘柏桦, 深圳高级中学丁立轩, 深圳
中学邓博文, 巴蜀中学王瑜, 人大附中叶天宸、袁奕等同学也给出了本题的正确解答.

第二题 令 $n=2022, m=37$. 求最小的正实数 $c$, 使得存在非负实数 $x_{i}, y_{i}$ $(i=1,2, \cdots, n)$, 满足:

(1) $x_{i} x_{i+1} \geq \sum_{j=i}^{i+m-1} y_{j}$ 对任意 $i=1,2, \cdots, n$ 成立, 其中下标按模 $n$ 理解;

(2) $\sum_{i=1}^{n} y_{i}=1, \sum_{i=1}^{n} x_{i}=c$.

(上海中学学生 江城 供题)

## 解 (根据巴蜀中学王瑜同学整理):

取 $x_{1}=x_{2}=\cdots=x_{38}=1$ 且 $y_{38}=1$, 其余变量均为 0 , 此时条件成立且 $c=38$. 下面证明总有 $c \geq 38$.

因为 $1=\sum_{i=1}^{n} y_{i} \geq \sum_{j=i}^{i+m-1} y_{j}$, 所以结合 (1) 知,

$$
\min \left\{1, x_{i} x_{i+1}\right\} \geq \sum_{j=i}^{i+m-1} y_{j}
$$

求和得,

$$
\sum_{i=1}^{n} \min \left\{1, x_{i} x_{i+1}\right\} \geq \sum_{i=1}^{n} \sum_{j=i}^{i+m-1} y_{j}=m .
$$

因此只需证明, 对 $1 \leq k \leq 19$, 若

$$
\sum_{i=1}^{n} \min \left\{1, x_{i} x_{i+1}\right\} \geq 2 k-1
$$

则 $\sum_{i=1}^{n} x_{i} \geq 2 k$.

对 $k$ 归纳.

当 $k=1$ 时, 若存在 $i$ 使 $x_{i} x_{i+1} \geq 1$, 则 $x_{i}+x_{i+1} \geq 2 \sqrt{x_{i} x_{i+1}} \geq 2$, 命题成立.若对任意 $i$ 都有 $x_{i} x_{i+1}<1$, 则条件即为

$$
\sum_{i=1}^{n} x_{i} x_{i+1} \geq 1
$$

因为 $n \geq 4$, 所以由熟知的结论,

$$
\left(\sum_{i=1}^{n} x_{i}\right)^{2} \geq 4 \sum_{i=1}^{n} x_{i} x_{i+1} \geq 4
$$

开方即证.

假设命题对 $k-1$ 成立, 来看 $k$ 时的情形.

构造图 $G(V, E)$, 其中 $V=\left\{v_{1}, v_{2}, \cdots, v_{n}\right\}, v_{i} v_{i+1} \in E$ 当且仅当 $x_{i} x_{i+1} \geq 1$.
若 $|E| \geq 2 k$, 则存在 $k$ 条端点互不相同的边. 对每条这样的边 $v_{i} v_{i+1}$, 对应的 $x_{i}+x_{i+1} \geq 2 \sqrt{x_{i} x_{i+1}} \geq 2$, 因此相加知命题得证.

若 $|E| \leq 2 k-1$, 则这些边的端点至多有 $4 k-2$ 个. 对于余下至少 $n-4 k+2>2$个点, 若其中有两个下标 (模 $n$ 意义下) 差不为 1 且对应的 $x$ 均非零, 设为 $v_{r}, v_{s}$. 令 $x_{r}^{\prime}=x_{r}+\varepsilon, x_{s}^{\prime}=x_{s}-\varepsilon$, 其余 $x_{j}^{\prime}=x_{j}$, 此时 $\sum_{i=1}^{n} x_{i}^{\prime}=\sum_{i=1}^{n} x_{i}$. 因为 $\sum_{i=1}^{n} \min \left\{1, x_{i} x_{i+1}\right\}$中无 $x_{r} x_{s}$ 项, 所以关于 $\varepsilon$ 在一个含 0 的闭区间上是一次函数, 于是当 $\varepsilon$ 取为区间的一个端点时 $\sum_{i=1}^{n} \min \left\{1, x_{i} x_{i+1}\right\}$ 更大 (条件仍成立). 此时要么 $v_{r}, v_{s}$ 中至少有一个连边, 要么 $x_{r}, x_{s}$ 中至少有一个为 0 .

若某一时刻 $|E| \geq 2 k$, 则由上面的讨论即证.

若否, 则这些不连边的 $v_{i}$ 中至多有两个对应的 $x_{i}$ 非零 (当恰有两个时这两个 $v_{i}$ 下标差为 1 ). 此时必存在 $j$, 使得 $v_{j}$ 与 $v_{j-1}, v_{j+1}$ 中恰一个连边, 而另一个对应的 $x$ 是 0 . 这是因为有多于两个点不连边, 所以必有一个对应的 $x$ 为 0 . 取一段极长的连续的 0 , 则两端之外的下一个数非零. 由前面的证明, 这两数对应顶点一定有一个连边, 记此顶点为 $v_{j}$ 即可. 现在不妨设 $j=1$, 且 $v_{1} v_{2}$ 连边, $x_{n}=0$.

这时

$$
\min \left\{1, x_{n} x_{1}\right\}+\min \left\{1, x_{1} x_{2}\right\}+\min \left\{1, x_{2} x_{3}\right\} \leq 2,
$$

所以

$$
\sum_{i=3}^{n-1} \min \left\{1, x_{i} x_{i+1}\right\} \geq(2 k-1)-2=2(k-1)-1
$$

于是由归纳假设 (将 $x_{1}, x_{2}$ 视为 0 ), $\sum_{i=3}^{n} x_{i} \geq 2 k-2$. 又 $x_{1}+x_{2} \geq 2 \sqrt{x_{1} x_{2}} \geq 2$, 故 $\sum_{i=1}^{n} x_{i} \geq 2 k$.

归纳证毕

综上, 所求最小值为 38 .

评注 本题源于对 2020 年全国高中数学联赛加试 (A 卷)第二题的讨论:

给定整数 $n \geq 3$. 设 $a_{1}, a_{2}, \cdots, a_{2 n}, b_{1}, b_{2}, \cdots, b_{2 n}$ 是 $4 n$ 个非负实数, 满足

$$
a_{1}+a_{2}+\cdots+a_{2 n}=b_{1}+b_{2}+\cdots+b_{2 n}>0
$$

且对任意 $i=1,2, \cdots, 2 n$, 有 $a_{i} a_{i+2} \geq b_{i}+b_{i+1}$ (这里 $a_{2 n+1}=a_{1}, a_{2 n+2}=a_{2}, b_{2 n+1}=$ $\left.b_{1}\right)$. 求 $a_{1}+a_{2}+\cdots+a_{2 n}$ 的最小值.

本题与原题做法区别很大, 本题做法只能解决 $m$ 是奇数的情形, 原题 $m$ 是偶数.
第三题 对正整数 $m$, 设集合 $A_{m}=\{2022 m-2021,2022 m-2020, \cdots, 2022 m\}$.是否存在正整数 $t$ 及集合 $B_{1}, B_{2}, \cdots, B_{t}$, 满足 $B_{i} \subseteq A_{i}, 1 \leq i \leq t$, 且对任意正整数 $N$ ，存在 $1 \leq i \leq t$ ，使得 $N$ 的正因子集与 $A_{i}$ 的交集恰为 $B_{i}$ ?

(重庆南开中学学生 沈星余 供题)

解 (根据供题者的解答整理)：存在.

构造数列 $\left\{a_{n}\right\}: a_{1}=1$, 对 $n \geq 1$,

$$
a_{n+1}=\frac{1}{2022}\left(2022 a_{n}-2021\right)\left(2022 a_{n}-2020\right) \cdots\left(2022 a_{n}\right)+a_{n}
$$

则对 $k=1,2, \cdots, 2022, A_{a_{n}}$ 中的第 $k$ 个元素 $2022 a_{n}-2022+k$ 整除 $A_{a_{n+1}}$ 中的第 $k$ 个元素

$$
\begin{aligned}
& 2022 a_{n+1}-2022+k \\
= & \left(2022 a_{n}-2021\right)\left(2022 a_{n}-2020\right) \cdots\left(2022 a_{n}\right)+2022 a_{n}-2022+k .
\end{aligned}
$$

进一步, 对任意 $n<m, A_{a_{n}}$ 中的第 $k$ 个元素整除 $A_{a_{m}}$ 中的第 $k$ 个元素.

取 $t=a_{2^{2022}}$, 对 $1 \leq n \leq 2^{2022}$, 令 $B_{a_{n}}$ 为 $2022 a_{n}$ 与 $C_{a_{n}}$ 中每个元素的差所构成的集合, 其中 $C_{a_{1}}, C_{a_{2}}, \cdots, C_{a_{22022}}$ 为 $\{0,1, \cdots, 2021\}$ 的全体子集, 且元素个数单调不增. 对 $1 \sim t$ 中的其余 $i$, 令 $B_{i}$ 为 $A_{i}$ 的任意子集. 下面证明此构造满足要求.

若不然, 存在 $N$ 不合题. 令 $N$ 的正因子集与 $A_{i}$ 的交为 $B_{i}^{\prime}, C_{i}^{\prime}$ 为 $2022 i$ 与 $B_{i}^{\prime}$中每个元素的差所构成的集合. 由 $(*)$, 对任意 $n<m$, 若 $A_{a_{n}}$ 的第 $k$ 个元素属于 $B_{a_{n}}^{\prime}$, 则 $A_{a_{m}}$ 的第 $k$ 个元素属于 $B_{a_{m}}^{\prime}$, 于是 $C_{a_{n}}^{\prime} \supseteq C_{a_{m}}^{\prime}$.

假设对任意 $1 \leq n \leq 2^{2022}$, 都有 $B_{a_{n}}^{\prime} \neq B_{a_{n}}$, 则 $C_{a_{n}}^{\prime} \neq C_{a_{n}}$. 因为 $C_{a_{1}}$ 是全集,所以 $C_{a_{1}}^{\prime} \subsetneq C_{a_{1}}$.

记 $i_{1}=1$, 对 $1 \leq s \leq 2022$, 当 $i_{s}$ 已构造且满足 $C_{a_{i_{s}}}^{\prime} \subsetneq C_{a_{i_{s}}}$ 时, 取 $i_{s+1}$ 满足 $C_{a_{i_{s+1}}}=C_{a_{i_{s}}}^{\prime}$. 因为 $C_{a_{1}}, C_{a_{2}}, \cdots, C_{a_{2} 2022}$ 的元素个数单调不增, 且 $\left|C_{a_{i_{s+1}}}\right|<\left|C_{a_{i_{s}}}\right|$,所以 $i_{s+1}>i_{s}$. 于是 $C_{a_{i_{s}}}^{\prime} \supseteq C_{a_{i_{s+1}}}^{\prime}$, 从而 $C_{a_{i_{s+1}}}^{\prime} \subseteq C_{a_{i_{s+1}}}$, 又 $C_{a_{i_{s+1}}}^{\prime} \neq C_{a_{i_{s+1}}}$, 故 $C_{a_{i_{s+1}}}^{\prime} \subsetneq C_{a_{i_{s+1}}}$.

这样,

$$
C_{a_{i_{2022}}}^{\prime} \subsetneq C_{a_{i_{2022}}}=C_{a_{i_{2021}}}^{\prime} \subsetneq C_{a_{i_{2021}}}=\cdots \subsetneq C_{a_{i_{2}}}=C_{a_{i_{1}}}^{\prime} \subsetneq C_{a_{i_{1}}},
$$

所以

$$
\left|C_{a_{i_{2022}}}^{\prime}\right|<\left|C_{a_{i_{2021}}}^{\prime}\right|<\cdots<\left|C_{a_{i_{1}}}^{\prime}\right|<2022 .
$$

从而 $\left|C_{a_{i_{2022}}}^{\prime}\right|=0$, 故 $C_{a_{i_{2022}}}^{\prime}=\emptyset=C_{a_{i_{2022}}}$, 与假设矛盾 $!$

因此存在 $1 \leq n \leq 2^{2022}$, 使得 $B_{a_{n}}^{\prime}=B_{a_{n}}$, 这便说明上述构造满足要求.
综上, 结论得证.

第四题 给定奇素数 $p$. 求不定方程 $a b+c d=p$ 的满足 $\min \{a, b\} \geq \max \{c, d\}$的正整数解 $(a, b, c, d)$ 的个数.

(北京大学学生 张志成 供题)

## 解 (根据上海中学江城同学的解答整理):

设集合

$$
A=\left\{(a, b, c, d) \in \mathbb{N}_{+}^{4} \mid p=a b+c d, a \geq c, b \geq d\right\}
$$

对每个 $v=(a, b, c, d) \in A$, 定义区间 $I_{v}=\left[\frac{c}{b}, \frac{a}{d}\right)$. 注意到固定 $b, c$ 或固定 $a, d$ 后可唯一地确定 $v$, 且 $\operatorname{gcd}(b, c)=\operatorname{gcd}(a, d)=1$, 故所有 $I_{v}$ 的左端点互不相同、右端点也互不相同.

引理 1 若不存在 $u \in A$ 使 $I_{v}$ 的左端点等于 $I_{u}$ 的右端点, 则 $I_{v}$ 的左端点 $\frac{c}{b} \leq \frac{2}{p+1}$.

证明 $\quad$ 取 $t \in \mathbb{N}$ 使 $0<a-t c \leq c$.

若 $t \geq 1$, 则 $u=(c, d+t b, a-t c, b) \in A$, 且 $I_{u}$ 的右端点为 $\frac{c}{b}$, 矛盾!

于是 $t=0$, 从而 $a=c=1, b+d=p$. 再由 $b \geq d$ 知 $\frac{c}{b} \leq \frac{2}{p+1}$.

引理 1 得证.

引理 2 若不存在 $u \in A$ 使 $I_{v}$ 的右端点等于 $I_{u}$ 的左端点, 则 $I_{v}$ 的右端点 $\frac{a}{d} \geq \frac{p+1}{2}$.

证明与引理 1 类似.

回到原题. 对 $r>0$, 记

$$
A(r)=\{(a, b, c, d) \in A \mid a>r d, r b \geq c\},
$$

则对 $v \in A, v \in A(r)$ 当且仅当 $r \in I_{v}$. 我们将这些 $I_{v}$ 首尾相接 (如 $[x, y),[y, z)$ 可以合成 $[x, z)$ ), 由引理, 合成后的每个大区间都包含 $\left[\frac{2}{p+1}, \frac{p+1}{2}\right)$. 这表明 $r \in\left[\frac{2}{p+1}, \frac{p+1}{2}\right)$时, $|A(r)|$ 是定值.

易知

$$
A\left(\frac{2}{p+1}\right)=\left\{(1, b, 1, d) \mid b, d \in \mathbb{N}_{+}, b+d=p, b \geq d\right\}
$$

所以 $\left|A\left(\frac{2}{p+1}\right)\right|=\frac{p-1}{2}$, 于是 $|A(1)|=\frac{p-1}{2}$. 又原方程比 $A(1)$ 恰多一个解 $(1, p-1$, $1,1)$, 故原方程的解数为 $\frac{p+1}{2}$.

评注 (1). 本题是供题者在研究下述结论时得到的:
对奇素数 $p$, 不定方程 $a b+c d=p$ 的满足 $a, b, c, d<\sqrt{p}$ 的正整数解 $(a, b, c, d)$的个数为

$$
4(\varphi(1)+\varphi(2)+\cdots+\varphi([\sqrt{p}]))-p-1 .
$$

该结论也可以用来证明第 32 期征解第四题:

设 $p \equiv 3(\bmod 8)$ 是素数, 且 $p>3$. 证明存在正整数 $a, b, c<\sqrt{p}$, 使得 $p=a^{2}+b c$.

(2). 用本题结论可以证明费马两平方和定理.

事实上, 当素数 $p \equiv 1(\bmod 4)$ 时, $\frac{p+1}{2}$ 是奇数, 所以对合 $(a, b, c, d) \mapsto(b, a, d, c)$有不动点 $(a, a, c, c)$, 故 $p=a^{2}+c^{2}$ 可以表示为两个平方数之和.

致谢 感谢人大附中关乃粼同学仔细审阅了第二题和第三题的解答, 并补充了若干细节.

