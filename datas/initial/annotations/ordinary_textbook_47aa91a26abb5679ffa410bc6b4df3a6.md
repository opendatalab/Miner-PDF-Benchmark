# 2021 年国家集训队第二轮选拔试题解析 

$$
\text { 王一川 唐立华 }
$$

(华东师范大学第二附属中学, 201203)

2021 年 4 月 5 日- 4 月 13 日, 中国国家队第二轮选拔在有千年校史的姑苏名校苏州中学举行, 集训队员和教练们下榻的三元宾馆更是以清乾隆 46 年钱棨连中三元而得名. 这似乎预示着今年的中国国家队的好运, 果然中国队于今年 7 月中旬在俄罗斯圣彼特堡举办的 IMO 竞赛中荣获个人、金牌数和团体总分三项第一. 本次第二轮选拔试题新颖, 难度分布合理, 具有较好的选拔功能, 其中第 5、6 两天均为“易中难” (无交换顺序) 的难度分布, 且难题难度很大, 非常贴合 IMO; 第 7 天整体难度较大, 体现出选拔功能; 第 8 天则相对容易. 其中, 笔者个人认为 5.2 和 8.6 这 2 个题为最佳试题! 以下解答是由第一作者根据考试时的解法整理而成, 不当之处在所难免, 敬请大家不吝赐教.

## I. 试 题

5.1 凸 $n(n \geq 5)$ 边形 $\Omega: P_{1} P_{2} \cdots P_{n}$ 的所有对角线无三线共点于 $\Omega$ 内部. 证明: 可以在每个四边形 $P_{i} P_{j} P_{k} P_{l}(1 \leq i<j<k<l \leq n)$ 内部选出一个不在任何 $\Omega$ 的对角线上的点, 使得所选出的 $\left(\begin{array}{l}n \\ 4\end{array}\right)$ 个点两两不同, 且任意两点所确定的线段与至少一条 $\Omega$ 的对角线相交.

5.2 给定 2021 个互不相同的正整数 $a_{1}, a_{2}, \cdots, a_{2021}$, 归纳定义数列 $\left\{a_{n}\right\}$如下: 对每个整数 $n \geq 2022, a_{n}$ 是在 $a_{1}, a_{2}, \cdots, a_{n-1}$ 中未出现的且不是乘积 $a_{n-1} a_{n-2} \cdots a_{n-2021}$ 的约数的最小正整数. 证明: 存在正整数 $M$, 使得所有不小于 $M$ 的正整数都在数列 $\left\{a_{n}\right\}$ 中出现.

5.3 求最大的正实数 $C$, 使得对任意整数 $n \geq 2$, 存在实数 $x_{1}, x_{2}, \cdots, x_{n} \in$ $[-1,1]$ 满足

$$
\prod_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right) \geq C^{\frac{n(n-1)}{2}}
$$

修订日期: 2021-07-30.

6.4 对每个正整数 $N$, 记 $N$ 的正约数个数为 $\tau(N), N$ 的两两不同的素因子个数为 $\omega(N), N$ 的素因子个数(计入重数)为 $\Omega(N)$. 证明: 对任意正整数 $n$, 有

$$
\sum_{m=1}^{n} 5^{\omega(m)} \leq \sum_{k=1}^{n}\left\lfloor\frac{n}{k}\right\rfloor \tau(k)^{2} \leq \sum_{m=1}^{n} 5^{\Omega(m)}
$$

这里, $\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数.

6.5 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$ 满足: 对于任意 $x, y \in \mathbb{R}$,

$$
f\left(x f(y)+y^{2021}\right)=y f(x)+(f(y))^{2021} .
$$

6.6 证明存在正实数 $\lambda$ 满足：对任意正整数 $m$, 如果平面直角坐标系中 $\triangle A B C$ 的三个顶点的横纵坐标均为整数, 并且 $\triangle A B C$ 内部 (不含边界) 有且仅有一个点的横纵坐标均为 $m$ 的整数倍, 则 $\triangle A B C$ 的面积小于 $\lambda m^{3}$.

7.1 给定整数 $n \geq 2$. 求最小的正整数 $m$, 使得存在 $n^{2}$ 个两两不同的正实数 $x_{i, j}(1 \leq i, j \leq n)$ 满足以下条件:

(1) 对任意 $i, j, x_{i, j}=\max \left\{x_{i, 1}, x_{i, 2}, \cdots, x_{i, j}\right\}$ 或 $x_{i, j}=\max \left\{x_{1, j}, x_{2, j}, \cdots, x_{i, j}\right\}$;

(2) 对任意 $i$, 至多存在 $m$ 个下标 $k$, 使得 $x_{i, k}=\max \left\{x_{i, 1}, x_{i, 2}, \cdots, x_{i, k}\right\}$;

(3) 对任意 $j$, 至多存在 $m$ 个下标 $k$, 使得 $x_{k, j}=\max \left\{x_{1, j}, x_{2, j}, \cdots, x_{k, j}\right\}$.

7.2 如图所示, 锐角 $\triangle A B C(A B<A C)$ 的内心是 $I$, 外接圆是 $\odot O . M$ 和 $N$ 分别是弧 $\widehat{B A C}$ 和 $\widehat{B C}$ 的中点. $D$ 是 $\overparen{A C}$ 上一点, 满足 $A D / / B C . \triangle A B C$ 在 $\angle B A C$ 内的旁切圆与边 $B C$ 相切于点 $E$. 点 $F$ 在 $\triangle A B C$ 内, 满足 $I F / / B C$ 且 $\angle B A F=\angle C A E$. 设直线 $N F$ 与 $\odot O$ 的另一个交点是 $R$, 直线 $A F$ 与 $D I$ 相交于点 $K$, 直线 $A R$ 与 $I F$ 相交于点 $L$. 证明: $N K \perp M L$.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-02.jpg?height=523&width=560&top_left_y=1823&top_left_x=748)

7.3 记 $S(k)$ 为正整数 $k$ 在十进制表示下的所有数码之和. 求所有整数 $n \geq 2$和有理数 $\beta \in(0,1)$, 使得存在 $n$ 个两两不同的正整数 $a_{1}, a_{2}, \cdots, a_{n}$, 满足: 对于 $\{1,2, \cdots, n\}$ 的任意 $r(r \geq 2)$ 元子集 $I$, 有 $S\left(\sum_{i \in I} a_{i}\right)=\beta \cdot \sum_{i \in I} S\left(a_{i}\right)$.

8.4 对所有实数 $x_{1}, x_{2}, \cdots, x_{60} \in[-1,1]$, 求

$$
\sum_{i=1}^{60} x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)
$$

的最大可能值, 这里 $x_{0}=x_{60}, x_{61}=x_{1}$.

8.5 求最小的正实数 $\alpha$, 使得对面积为 1 的任意凸多边形 $P$, 存在平面上一点 $M$ 使得 $P \cup Q$ 的凸包的面积不超过 $\alpha$. 这里 $Q$ 为 $P$ 关于点 $M$ 的中心对称图形.

8.6. 给定整数 $n \geq 2$. 有 $2 n^{2}$ 位选手参加中国象棋比赛, 每两位选手恰对亦一局, 结果可有平局. 已知

(1) 对任意三位选手甲、乙、丙, 若甲胜乙, 且乙胜丙, 则甲胜丙;

(2) 所有比赛中平局的场数不超过 $\frac{n^{3}}{16}$.

证明: 可从这 $2 n^{2}$ 位选手中选出 $n^{2}$ 位选手, 并适当记作 $P_{i j}(1 \leq i, j \leq n)$, 使得对任意 $i, j, i^{\prime}, j^{\prime} \in\{1,2, \cdots, n\}$, 若 $i>i^{\prime}$, 则 $P_{i j}$ 胜 $P_{i^{\prime} j^{\prime}}$.

## II . 解答与评注

5.1 凸 $n(n \geq 5)$ 边形 $\Omega: P_{1} P_{2} \cdots P_{n}$ 的所有对角线无三线共点于 $\Omega$ 内部. 证明: 可以在每个四边形 $P_{i} P_{j} P_{k} P_{l}(1 \leq i<j<k<l \leq n)$ 内部选出一个不在任何 $\Omega$ 的对角线上的点, 使得所选出的 $\left(\begin{array}{l}n \\ 4\end{array}\right)$ 个点两两不同, 且任意两点所确定的线段与至少一条 $\Omega$ 的对角线相交.

证明 设对角线将 $\Omega$ 分成若干个区域 $U_{1}, U_{2}, \cdots, U_{t}$, 则只需使选出的 $\left(\begin{array}{l}n \\ 4\end{array}\right)$ 个点两两在不同区域中.

注意到, 每个凸四边形 $P_{i} P_{j} P_{k} P_{l}(1 \leq i<j<k<l \leq n)$ 可对应到对角线 $P_{i} P_{k}, P_{j} P_{l}$ 的交点, 称这样的交点为 “结点”, 设所有结点是 $X_{1}, X_{2}, \cdots, X_{m}$ $\left(m=\left(\begin{array}{l}n \\ 4\end{array}\right)\right)$. 我们希望 $P_{i} P_{j} P_{k} P_{l}$ 内选出的点所在区域与结点 $P_{i} P_{k} \cap P_{j} P_{l}$ 相邻(称结点 $K$ 与区域 $\alpha$ 相邻当且仅当 $K$ 是 $\alpha$ 的一个顶点).

现在考虑下述操作: 对任意非空子集 $\Gamma \subseteq\left\{X_{1}, X_{2}, \cdots, X_{m}\right\}$, 设 $\Gamma$ 的凸包是 $S, S$ 是点或线段或凸多边形, 取 $S$ 的一个顶点 $X_{j}$ ( $X_{j}$ 不在 $S$ 某条边界内部).

断言 存在一个与 $X_{j}$ 相邻的区域 $\alpha, \alpha$ 不与 $\Gamma$ 中其他结点相邻.

证明 设过 $X_{j}$ 的对角线为 $l_{1}, l_{2}$, 与 $X_{j}$ 相邻的区域是 $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{4}$, 如下图.

用反证法, 假设存在结点 $Y_{1}, Y_{2}, Y_{3}, Y_{4} \in \Gamma \backslash\left\{X_{j}\right\}, Y_{1}, Y_{2}, Y_{3}, Y_{4}$ 分别与 $\alpha_{1}$, $\alpha_{2}, \alpha_{3}, \alpha_{4}$ 相邻 $\left(Y_{1}, Y_{2}, Y_{3}, Y_{4}\right.$ 可能相同). 显然线段 $Y_{1} Y_{2}$ 与 $l_{2}$ 有公共点(记为 $Z_{1}$ ),线段 $Y_{3} Y_{4}$ 与 $l_{2}$ 有公共点 (记为 $Z_{2}$ ), 且 $Z_{1}, Z_{2}$ 在 $X_{j}$ 两侧.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-04.jpg?height=394&width=696&top_left_y=203&top_left_x=680)

故可依次推出 $Z_{1}, Z_{2}, X_{j}$ 在 $Y_{1}, Y_{2}, Y_{3}, Y_{4}$ 的凸包内, 其中 “ $X_{j}$ 在 $Y_{1}, Y_{2}, Y_{3}, Y_{4}$的凸包内”与 “ $X_{j}$ 是 $\Gamma$ 凸包的一个顶点”矛盾!

故(1)得证.

现在考虑从 $X_{1}, X_{2}, \cdots, X_{m}$ 中, 每次去掉凸包上一个点.

不妨设对 $1 \leq i \leq m, X_{i}$ 是 $X_{i}, X_{i+1}, \cdots, X_{m}$ 的凸包的一个顶点(否则重排), 由(1)知: 对 $1 \leq i \leq m$, 可取出一个与 $X_{i}$ 相邻的区域 $V_{i}, V_{i}$ 与 $X_{i+1}, \cdots, X_{m}$均不相邻. 显然 $V_{1}, V_{2}, \cdots, V_{m}$ 两两不同. 对 $1 \leq i \leq m$, 令 $X_{i}$ 对应的凸四边形中取出的点在区域 $V_{i}$ 中即可.

原题得证.

评注 本题是简单的组合几何问题, 有多种解法, 本解答利用了对角线交点 $P_{i} P_{k} \cap P_{j} P_{l}$, 用 Hall 定理也可以做出本题.

5.2 给定 2021 个互不相同的正整数 $a_{1}, a_{2}, \cdots, a_{2021}$, 归纳定义数列 $\left\{a_{n}\right\}$如下: 对每个整数 $n \geq 2022, a_{n}$ 是在 $a_{1}, a_{2}, \cdots, a_{n-1}$ 中未出现的且不是乘积 $a_{n-1} a_{n-2} \cdots a_{n-2021}$ 的约数的最小正整数. 证明: 存在正整数 $M$, 使得所有不小于 $M$ 的正整数都在数列 $\left\{a_{n}\right\}$ 中出现.

证明 (I) 首先用代数方法估计 $\left\{a_{n}\right\}$ 的增长速度.

熟知存在常数 $C>0$, 使得任意 $n \in \mathbb{Z}^{+}, n$ 的正约数个数 $\tau(n)<C \cdot n^{0.0001}$.

注意到: 对 $n \geq 2022, a_{n}$ 不能取的值为 $a_{1}, a_{2}, \cdots, a_{n-1}$ 及 $a_{n-1} \cdots a_{n-2021}$的正约数, 共 $n-1+\tau\left(a_{n-1} \cdots a_{n-2021}\right)$ 个数, 故

$$
\begin{aligned}
a_{n} & \leq n+\tau\left(a_{n-1} \cdots a_{n-2021}\right) \\
& \leq n+C \cdot\left(a_{n-1} \cdots a_{n-2021}\right)^{0.0001} \\
& \leq n+C \cdot \max \left\{a_{n-1}, \cdots, a_{n-2021}\right\}^{\frac{2021}{10000}} .
\end{aligned}
$$

注意到 $n \geq \max \left\{a_{1}, \cdots, a_{2021}\right\}+1$ 时,

$$
\max \left\{a_{1}, \cdots, a_{n}\right\} \geq n>\max \left\{a_{1}, \cdots, a_{2021}\right\}
$$

故可设 $\max \left\{a_{1}, \cdots, a_{n}\right\}=a_{m}, 2022 \leq m \leq n$, 由(1)知

$$
\begin{aligned}
\max \left\{a_{1}, \cdots, a_{n}\right\} & =a_{m} \\
& \leq m+C \cdot \max \left\{a_{m-1}, \cdots, a_{m-2021}\right\}^{\frac{2021}{1000}} \\
& \leq n+C \cdot \max \left\{a_{1}, \cdots, a_{n}\right\}^{\frac{1}{2}}
\end{aligned}
$$

解得

$$
\max \left\{a_{1}, \cdots, a_{n}\right\} \leq\left(\frac{C}{2}+\sqrt{\frac{C^{2}}{4}+n}\right)^{2} \quad\left(\forall n \geq \max \left\{a_{1}, \cdots, a_{2021}\right\}+1\right)
$$

特别地 $a_{n} \leq\left(\frac{C}{2}+\sqrt{\frac{C^{2}}{4}+n}\right)^{2}$, 这表明:

存在常数 $k>0$, 使 $a_{n} \leq n+k \cdot \sqrt{n}\left(\forall n \in \mathbb{Z}^{+}\right)$.

(II) 接下来解决原问题, 任取一个不在 $\left\{a_{n}\right\}$ 中的正整数 $x$, 由于 $\left\{a_{n}\right\}$ 中只有有限项 $\leq x$, 故 $n$ 充分大时 $a_{n}>x$, 此时 $a_{n}$ 不取 $x$ 的理由一定是: $x$ 整除 $a_{n-1} \cdots a_{n-2021}$. 故

$$
x \mid a_{n-1} \cdots a_{n-2021} \text {. (对任意充分大的 } n \text { ) }
$$

断言 $1 x$ 无大于 $10^{4}$ 的素因子.

证明 用反证法. 若存在素数 $p \mid x, p>10^{4}$, 则由(3)知：对充分大的 $n$, $p \mid a_{n-1} \cdots a_{n-2021}$, 即 $a_{n-1}, \cdots, a_{n-2021}$ 中有 $p$ 的倍数. 于是存在常数 $L$, 使得对任意 $n \in \mathbb{Z}^{+}, a_{1}, \cdots, a_{n}$ 中 $p$ 的倍数的个数 $\geq \frac{n}{2021}-L$. 进而

$$
\max \left\{a_{1}, \cdots, a_{n}\right\} \geq \max _{\substack{1 \leq i \leq n \\ p \mid a_{i}}}\left\{a_{i}\right\} \geq p \cdot\left(\frac{n}{2021}-L\right)
$$

结合(2)知

$$
n+k \cdot \sqrt{n} \geq p \cdot\left(\frac{n}{2021}-L\right)
$$

令 $n$ 充分大即得矛盾 $\left(\right.$ 因为 $\left.1<\frac{P}{2021}\right)$.

断言 2 对任意素数幕 $p^{\alpha} \mid x$, 有 $\alpha \leq 10^{8}$.

证明 用反证法. 假设 $a>10^{8}$, 由(3)知: 对充分大的 $n, p^{10^{8}} \mid a_{n-1} \cdots a_{n-2021}$,进而 $a_{n-1}, \cdots, a_{n-2021}$ 中存在 $p^{10^{4}}$ 的倍数, 于是存在常数 $L^{\prime}$, 使得对任意 $n \in \mathbb{Z}^{+}$, $a_{1}, \cdots, a_{n}$ 中 $p^{10^{4}}$ 的倍数个数 $\geq \frac{n}{2021}-L^{\prime}$, 进而

$$
\max \left\{a_{1}, \cdots, a_{n}\right\} \geq \max _{\substack{1 \leq i \leq n \\ p^{10^{4}} \mid a_{i}}}\left\{a_{i}\right\} \geq p^{10^{4}} \cdot\left(\frac{n}{2021}-L^{\prime}\right)
$$

结合(2)知

$$
n+k \sqrt{n} \geq p^{10^{4}} \cdot\left(\frac{n}{2021}-L^{\prime}\right)
$$

令 $n$ 充分大即得矛盾 (因为 $\frac{p^{10^{4}}}{2021} \geq \frac{2^{10^{4}}}{2021}>1$ ).
结合断言 1,2 知: $x \mid \prod_{\text {素数 } p \leq 10^{4}} p^{10^{8}}$, 进而

$$
x \leq \prod_{\text {素数 } p \leq 10^{4}} p^{10^{8}} \leq\left(10^{4} !\right)^{10^{8}},
$$

取 $M=\left(10^{4} !\right)^{10^{8}}+1$, 即符合原题要求.

评注 本题是中等难度的数论问题, 本题形式和 2018 加试 4 比较像, 可以先考虑类似加试题地考虑每一项的素因子分解, 但发现做不出, 必须寻找新的方法, 经过尝试发现可以用正约数个数估计来估计 $\left\{a_{n}\right\}$ 增长速度 (事实上, 题目中写“不是 $a_{n-1} \cdots a_{n-2021}$ 的正约数” 而不是“不整除 $a_{n-1} \cdots a_{n-2021}$ ” 也提示了这一点) 进而做出本题, 本题形式传统而解法新颖, 个人认为是本届集训队出得最好的题.

5.3 求最大的正实数 $C$, 使得对任意整数 $n \geq 2$, 存在实数 $x_{1}, x_{2}, \cdots, x_{n} \in$ $[-1,1]$ 满足

$$
\prod_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right) \geq C^{\frac{n(n-1)}{2}}
$$

解 不妨设 $1 \geq x_{1} \geq \cdots \geq x_{n} \geq-1$ (否则重排), 于是可设 $x_{i}=\cos \theta_{i}$ $(1 \leq i \leq n), 0 \leq \theta_{1} \leq \cdots \leq \theta_{n} \leq \pi$. 考虑复数 $p_{j}=e^{i \theta_{j}}, q_{j}=e^{-i \theta_{j}}(1 \leq j \leq$ $n), p_{1}, \cdots, p_{n}, q_{n}, \cdots, q_{1}$ 是单位圆上依次排列的 $2 n$ 个复数, 设它们对应点 $A_{1}, A_{2}, \cdots, A_{2 n}$, 则对 $1 \leq j<k \leq n$,

$$
\begin{aligned}
x_{j}-x_{k} & =\cos \theta_{j}-\cos \theta_{k} \\
& =2 \cdot \sin \frac{\theta_{k}-\theta_{j}}{2} \cdot \sin \frac{\theta_{k}+\theta_{j}}{2} \\
& =\frac{1}{2}\left|p_{j}-p_{k}\right| \cdot\left|q_{j}-p_{k}\right| \quad(\text { 正弦定理 }) \\
& =\frac{1}{2} \cdot\left|A_{j} A_{k}\right| \cdot\left|A_{2 n+1-j} A_{k}\right| \\
& =\frac{1}{2} \cdot \sqrt{\left|A_{j} A_{k}\right| \cdot\left|A_{2 n+1-j} A_{k}\right| \cdot\left|A_{j} A_{2 n+1-k}\right| \cdot\left|A_{2 n+1-j} A_{2 n+1-k}\right|},
\end{aligned}
$$

进而

$$
\prod_{1 \leq j<k \leq n}\left(x_{j}-x_{k}\right)=\left(\frac{1}{2}\right)^{\mathrm{C}_{n}^{2}} \cdot \sqrt{\prod_{\substack{1 \leq j<k \leq 2 n \\ j+k \neq 2 n+1}}\left|A_{j} A_{k}\right|}
$$

将所有弦 $A_{j} A_{k}(1 \leq j<k \leq 2 n$, 含 $j+k=2 n+1$ 者) 按下标差分 $n$ 组:

$$
\begin{aligned}
& \Omega_{1}: A_{1} A_{2}, A_{2} A_{3}, \cdots, A_{2 n} A_{1}, \\
& \Omega_{2}: A_{1} A_{3}, A_{2} A_{4}, \cdots, A_{2 n} A_{2},
\end{aligned}
$$

$$
\begin{array}{r}
\Omega_{n-1}: A_{1} A_{n}, A_{2} A_{n+1}, \cdots, A_{2 n} A_{n-1} \\
\Omega_{n}: A_{1} A_{n+1}, A_{2} A_{n+2}, \cdots, A_{n} A_{2 n}
\end{array}
$$

对 $1 \leq t \leq n-1, \Omega_{t}$ 中所有弦圆周角之和 $\leq t \cdot \pi$.

$\Omega_{t}$ 中有 $\lambda_{t} \in\{2 n-2,2 n\}$ 条弦 $A_{j} A_{k}$ 满足 $j+k \neq 2 n+1$. 其中,

$$
t \pi \leq(n-1) \pi \leq \lambda_{t} \cdot \frac{\pi}{2}
$$

记 $\Omega_{t}$ 中满足 $j+k \neq 2 n+1$ 的弦的长度乘积为 $p_{t}$, 由琴生不等式,

$$
p_{t} \leq\left(2 \cdot \sin \frac{t \pi}{\lambda_{t}}\right)^{\lambda_{t}} \leq 2^{2 n} \cdot\left(\sin \frac{t \pi}{\lambda_{t}}\right)^{2 n-2} \leq 2^{2 n} \cdot\left(\sin \frac{t \pi}{2 n-2}\right)^{2 n-2}
$$

又注意到, 显然 $\Omega_{n}$ 中满足 $j+k \neq 2 n+1$ 的弦长乘积 $\leq 2^{n}$, 故

$$
\begin{aligned}
\prod_{\substack{1 \leq j<k \leq 2 n \\
j+k \neq 2 n+1}}\left|A_{j} A_{k}\right| & \leq 2^{n} \cdot \prod_{t=1}^{n-1} 2^{2 n} \cdot\left(\sin \frac{t \pi}{\lambda_{t}}\right)^{2 n-2} \\
& =2^{3 n-2} \cdot\left(\prod_{t=1}^{n-1} 2 \cdot \sin \frac{t \pi}{2 n-2}\right)^{2 n-2} \\
& =2^{3 n-2} \cdot(2 \cdot \sqrt{n-1})^{2 n-2} .
\end{aligned}
$$

代入(1)知:

$$
\prod_{1 \leq j<k \leq n}\left(x_{j}-x_{k}\right) \leq\left(\frac{1}{2}\right)^{\mathrm{C}_{n}^{2}} \cdot 2^{\frac{3 n-2}{2}} \cdot(2 \cdot \sqrt{n-1})^{n-1}
$$

由此即知原题中的 $C$ 必满足 $C \leq \frac{1}{2}$.

另一方面, 对任意 $n \geq 2$, 令 $A_{1} A_{2} \cdots A_{2 n}$ 是凸 $2 n$ 边形, 相应地

$$
\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\left(\cos \frac{\pi}{2 n}, \cos \frac{3 \pi}{2 n}, \cdots, \cos \frac{(2 n-1) \pi}{2 n}\right) .
$$

此时

$$
\prod_{\substack{1 \leq j<k \leq 2 n \\ j+k \neq 2 n+1}}\left|A_{j} A_{k}\right| \geq \prod_{\substack{1 \leq j<k \leq 2 n \\ k-j \neq n}}\left|A_{j} A_{k}\right|=\prod_{t=1}^{n-1}\left(2 \cdot \sin \frac{t \pi}{2 n}\right)^{2 n}=(\sqrt{n})^{2 n}>1 .
$$

代入(1)知

$$
\prod_{1 \leq j<k \leq n}\left(x_{j}-x_{k}\right) \geq\left(\frac{1}{2}\right)^{\mathrm{C}_{n}^{2}}
$$

故原题所求 $C$ 最大值为 $\frac{1}{2}$.

评注 本题是困难的不等式问题, 首先猜测构造, 注意到 $\left\{x_{i}\right\}$ 的分布是“两端密, 中间疏”, 由此猜测可能是一列 $\cos$ (即半圆在直径上的投影), 进而可作三角换元, 将本题归结于熟悉的问题, 估计单位圆上弦长的乘积.

6.4 对每个正整数 $N$, 记 $N$ 的正约数个数为 $\tau(N), N$ 的两两不同的素因子个数为 $\omega(N), N$ 的素因子个数(计入重数) 为 $\Omega(N)$. 证明: 对任意正整数 $n$, 有

$$
\sum_{m=1}^{n} 5^{\omega(m)} \leq \sum_{k=1}^{n}\left\lfloor\frac{n}{k}\right\rfloor \tau(k)^{2} \leq \sum_{m=1}^{n} 5^{\Omega(m)}
$$

这里, $\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数.

证明 注意到 $\left\lfloor\frac{n}{k}\right\rfloor$ 表示 $1,2, \cdots, n$ 中 $k$ 的倍数的个数, 故

$$
\sum_{k=1}^{n}\left\lfloor\frac{n}{k}\right\rfloor \cdot \tau(k)^{2}=\sum_{k=1}^{n}\left(\tau(k)^{2} \cdot \sum_{\substack{1 \leq m \leq n \\ k \mid m}} 1\right)=\sum_{m=1}^{n}\left(\sum_{k \mid m} \tau(k)^{2}\right)
$$

从而只需证明: 对任意 $m \geq 1$, 有

$$
5^{\omega(m)} \leq \sum_{k \mid m} \tau(k)^{2} \leq 5^{\Omega(m)}
$$

$m=1$ 时(1显然, 下设 $m \geq 2$ (不是归纳).

设 $m$ 的素因子分解为 $p_{1}^{\alpha_{1}} \cdots p_{t}^{\alpha_{t}}$, 则 $m$ 的所有正约数为 $p_{1}^{\beta_{1}} \cdots p_{t}^{\beta_{t}}$, 其中 $0 \leq \beta_{1} \leq \alpha_{1}, \cdots, 0 \leq \beta_{t} \leq \alpha_{t}$, 且

$$
\tau\left(p_{1}^{\beta_{1}} \cdots p_{t}^{\beta_{t}}\right)^{2}=\left(\beta_{1}+1\right)^{2} \cdots\left(\beta_{t}+1\right)^{2}
$$

故

$$
\sum_{k \mid m} \tau(k)^{2}=\sum_{\substack{0 \leq \beta_{1} \leq \alpha_{1} \\ 0 \leq \beta_{t} \leq \alpha_{t}}}\left(\beta_{1}+1\right)^{2} \cdots\left(\beta_{t}+1\right)^{2}=\prod_{i=1}^{t}\left(1^{2}+2^{2}+\cdots+\left(\alpha_{i}+1\right)^{2}\right)
$$

于是

$$
\text { (1) } \Leftrightarrow 5^{t} \leq \prod_{i=1}^{t}\left(1^{2}+2^{2}+\cdots+\left(\alpha_{i}+1\right)^{2}\right) \leq 5^{\alpha_{1}+\cdots+\alpha_{t}} \text {. }
$$

只需证: 对任意 $\alpha \in \mathbb{Z}^{+}$, 有

$$
5 \leq 1^{2}+2^{2}+\cdots+(\alpha+1)^{2} \leq 5^{\alpha} .
$$

记

$$
S(\alpha)=1^{2}+2^{2}+\cdots+(\alpha+1)^{2}=\frac{(\alpha+1)(\alpha+2)(2 \alpha+3)}{6}
$$

则 $S(1)=5$, 且 $\alpha \geq 1$ 时

$$
\frac{S(\alpha+1)}{S(\alpha)}=\frac{\alpha+2}{\alpha+1} \cdot \frac{\alpha+3}{\alpha+2} \cdot \frac{2 \alpha+5}{2 \alpha+3} \in\left[1, \frac{2}{1} \cdot \frac{3}{2} \cdot \frac{5}{3}\right]=[1,5]
$$

归纳易知 $S(\alpha) \in\left[5,5^{\alpha}\right]$ 对任意 $\alpha \geq 1$ 成立, (2)得证.

进而原题得证.

评注 本题是简单的数论不等式, 类似的问题还有 2014 集训队第三天第 1 题 (2014 年那个题更难).

6.5 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$ 满足: 对于任意 $x, y \in \mathbb{R}$,

$$
f\left(x f(y)+y^{2021}\right)=y f(x)+(f(y))^{2021} .
$$

解 记原题条件为 $P(x, y)$.

显然, 若 $f$ 常值, 则只能 $f \equiv 0$. 下设 $f$ 非常值.

断言 1 对 $d \in \mathbb{R} \backslash\{0\}$, 有 $f(d) \neq 0$.

证明 用反证法, 若 $f(d)=0$, 对任意 $x \in \mathbb{R}$, 由 $P(x, d)$ 知

$$
f\left(d^{2021}\right)=d f(x)+f(d)^{2021} \text {. }
$$

于是

$$
f(x)=\frac{1}{d} \cdot\left(f\left(d^{2021}\right)-f(d)^{2021}\right)
$$

推出 $f$ 常值函数, 矛盾.

断言 $2 \quad f(1)=1$.

证明 对任意 $x \in \mathbb{R}$, 由 $P(x, 1)$ 知

$$
f(x f(1)+1)=f(x)+f(1)^{2021} .
$$

由断言 1 知 $f(1) \neq 0$, 进而对任意 $x \in \mathbb{R}$,

$$
f(x f(1)+1) \neq f(x)
$$

只能 $f(1)=1$.

断言 $3 \quad f(x+1)=f(x)+1, \quad \forall x \in \mathbb{R}$.

证明 由 $P(x, 1)$ 知

$$
f(x f(1)+1)=f(x)+f(1)^{2021},
$$

结合 $f(1)=1$ 即知 $f(x+1)=f(x)+1$.

由断言 2,3 知 $f(n)=n, \forall n \in \mathbb{Z}$.

断言 $4 \quad f(x+f(y))=f(x)+y, \quad \forall x, y \in \mathbb{R}$.

证明 $y=0$ 时, 由 $f(0)=0$ 知断言 4 成立. 下设 $y \neq 0$.

固定 $y$, 任取 $z \in \mathbb{R}$, 由 $P(z, y), P(z+1, y)$ 知:

$$
\begin{gathered}
f\left(z f(y)+y^{2021}\right)=y f(z)+f(y)^{2021} \\
f\left(z f(y)+f(y)+y^{2021}\right)=y f(z+1)+f(y)^{2021}
\end{gathered}
$$

两式相减得

$$
f\left(z f(y)+f(y)+y^{2021}\right)-f\left(z f(y)+y^{2021}\right)=y(f(z+1)-f(z))=y
$$

由断言 1 知 $f(y) \neq 0$, 故 $z f(y)+y^{2021}$ 取遍 $\mathbb{R}$, 从而

$$
f(x+f(y))-f(x)=y, \quad \forall x \in \mathbb{R} .
$$

断言 $5 \quad f(f(y))=y, \quad \forall y \in \mathbb{R}$.

证明 在断言 4 中取 $x=0$ 即可.

断言 $6 \quad f(x+y)=f(x)+f(y), \quad \forall x, y \in \mathbb{R}$.

证明 在断言 4 中用 $f(y)$ 替换 $y$ 即可.

断言 $7 \quad f(x y)=f(x) f(y), \quad \forall x, y \in \mathbb{R}$.

证明 由断言 5 知: 原题条件可写为

$$
f(x f(y))+f\left(y^{2021}\right)=y f(x)+f(y)^{2021}, \quad \forall x, y \in \mathbb{R}
$$

在上式中令 $x=0$, 可知

$$
f\left(y^{2021}\right)=f(y)^{2021}, \quad \forall y \in \mathbb{R}
$$

进而

$$
f(x f(y))=y f(x), \quad \forall x, y \in \mathbb{R}
$$

在上式中用 $f(y)$ 替换 $y$ 得

$$
f(x y)=f(x) f(y), \quad \forall x, y \in \mathbb{R} .
$$

结合断言 6,7 易知 $f$ 在 $[0,+\infty)$ 上不减, 这是由于对任意 $u \geq v \geq 0$, 存在 $\alpha_{1}, \alpha_{2} \in \mathbb{R}, u=\alpha_{1}^{2}+\alpha_{2}^{2}, v=2 \alpha_{1} \alpha_{2}$, 从而

$$
f(u)-f(v)=f\left(\alpha_{1}^{2}+\alpha_{2}^{2}\right)-f\left(2 \alpha_{1} \alpha_{2}\right)=f\left(\alpha_{1}\right)^{2}+f\left(\alpha_{2}\right)^{2}-2 f\left(\alpha_{1}\right) f\left(\alpha_{2}\right) \geq 0 .
$$

于是 $f$ 在 $[0,+\infty)$ 上满足柯西方程, 结合 $f(1)=1$ 知

$$
f(x)=x, \quad \forall x \in[0,+\infty),
$$

再由断言 6 知

$$
f(-x)=f(0)-f(x)=-x, \quad x \geq 0
$$

故

$$
f(x)=x, \forall x \in \mathbb{R}
$$

显然 $f(x)=x, \forall x \in \mathbb{R}$ 满足要求.

故所求函数为

$$
\begin{aligned}
& 1^{\circ} \quad f(x)=x, \quad \forall x \in \mathbb{R} \\
& 2^{\circ} \quad f(x)=0, \quad \forall x \in \mathbb{R} .
\end{aligned}
$$

解答完毕!

评注 本题是中等难度的函数方程, 关键的一步是取出 $P(x+1, y), P(x, y)$差分.

6.6 证明存在正实数 $\lambda$ 满足: 对任意正整数 $m$, 如果平面直角坐标系中 $\triangle A B C$ 的三个顶点的横纵坐标均为整数, 并且 $\triangle A B C$ 内部 (不含边界) 有且仅有一个点的横纵坐标均为 $m$ 的整数倍, 则 $\triangle A B C$ 的面积小于 $\lambda m^{3}$.

证明 称横纵坐标均为 $m$ 倍的点为“ $m$ 倍点”.

首先考虑仿射变换

$$
(x, y) \rightarrow(a x+b y, c x+d y)
$$

其中 $a, b, c, d \in \mathbb{Z},\left|\begin{array}{ll}a & c \\ b & d\end{array}\right|=1$. 该变换的好处是: 我们可不妨设某条直线是水平线.

回到原题. 由 Pick's 定理, 只需证 $\triangle A B C$ 内 (含边界)整点数 $\leq \Theta\left(m^{3}\right)$. 将所有整点按横, 纵坐标 $\bmod m$ 分成 $m^{2}$ 类, 只需证 $\triangle A B C$ 内每一类整点数 $\leq \Theta(m)$.

具体地, 任取 $x_{0}, y_{0} \in \mathbb{Z}$, 称满足 $x \equiv x_{0}, y \equiv y_{0}(\bmod m)$ 的 $(x, y)$ 是“好点”.我们证明 $\triangle A B C$ 内 “好点”个数 $\leq \Theta(m)$.

断言 对每条直线 $l, l$ 上至多 $2 m+100$ 个好点在 $\triangle A B C$ 内.

证明 用反证法. 假设 $l \cap \triangle A B C$ 含 $\geq 2 m+101$ 个好点(作仿射, 平移, 不妨设 $l$ 水平).

设 $\triangle A B C$ 内唯一“ $m$ 倍点” 是 $O$, 考虑 $O, l$ 的位置关系, 有 2 种:

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-11.jpg?height=406&width=422&top_left_y=1853&top_left_x=540)

情形 1 (可能 $\mathrm{O}$ 在 1 上)

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-11.jpg?height=411&width=420&top_left_y=1853&top_left_x=1115)

情形 2

## 【情形 1】

过 $O$ 作 $l_{0} / / l$, 设 $P=A O \cap l$.

若 $|O P|>m \cdot|A O|$, 则将 $A O$ 延长 $m$ 倍可得 $\triangle A B C$ 内另一点 “ $m$ 倍点”, 矛
盾.

若 $|O P| \leq m \cdot|A O|$, 则线段长度:

$$
l_{0} \cap \triangle A B C \text { 长度 } \geq \frac{1}{m+1} \cdot(l \cap \triangle A B C \text { 长度 })>\frac{2 m+10}{m+1} \cdot m>2 m \text {, }
$$

于是 $l_{0} \cap \triangle A B C$ 上有另一 “ $m$ 倍点”, 矛盾.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-12.jpg?height=351&width=394&top_left_y=561&top_left_x=842)

## 【情形 2】

过 $O$ 作 $l_{0} / / l$, 过 $C$ 作 $l_{c} / / l$, 设 $P=A O \cap l_{c}$.

若 $|A P|>(m+1) \cdot|A O|$, 则将 $A O$ 延长 $m$ 倍可得另一点 “ $m$ 倍点”, 矛盾.

若 $(m+1) \cdot|A O| \geq|A P| \geq|A O|$, 则

$$
\begin{aligned}
l_{0} \cap \triangle A B C \text { 长度 } & \geq \frac{1}{m+1} \cdot\left(l_{c} \cap \triangle A B C \text { 长度 }\right) \\
& \geq \frac{1}{m+1} \cdot(l \cap \triangle A B C \text { 长度 }) \\
& >\frac{2 m+10}{m+1} \cdot m \\
& >2 m,
\end{aligned}
$$

于是 $l_{0} \cap \triangle A B C$ 上有另一 “ $m$ 倍点”, 矛盾.

若 $|A O| \geq|A P| \geq 0$, 则

$$
l_{0} \cap \triangle A B C \text { 长度 } \geq l \cap \triangle A B C \text { 长度 }>2 m \text {, }
$$

也矛盾.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-12.jpg?height=485&width=371&top_left_y=2036&top_left_x=845)

故断言得证.
现在证明(1): 若 $\triangle A B C$ 内好点数 $\leq 10^{8}$, 则(1)成立.

下设 $\triangle A B C$ 内好点数 $>10^{8}$, 则由抽庹, $\triangle A B C$ 内存在两好点 $R, S$ 横, 纵坐标 $\bmod 100 m$ 得到的二元组相同, 于是线段 $R S$ 上有 101 个好点, 记 $\delta$ 为直线 $R S$,不妨设 $\delta$ 即为直线 $y=y_{0}$ (作仿射, 平移).

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-13.jpg?height=289&width=420&top_left_y=541&top_left_x=818)

易知 $\triangle A B C \cap\left(\right.$ 直线 $\left.y=y_{0}+m\right)$ 至多含 2 个 “好点”. 否则, 可设 $y=y_{0}$ 上含好点 $\left(z, y_{0}\right),\left(z+2 m, y_{0}\right), y=y_{0}+m$ 上有好点 $\left(w, y_{0}+m\right),\left(w+2 m, y_{0}+m\right)$,作仿射平移, 不妨设 $z=w$, 则上述四点围成的长方形内有 2 个 $m$ 倍点, 矛盾.

同理 $\triangle A B C \cap\left(\right.$ 直线 $\left.y=y_{0}-m\right)$ 上也至多 2 个“好点”.

进而对整数 $i \geq 2, \triangle A B C \cap\left(\right.$ 直线 $\left.y=y_{0}+i m\right)=\varnothing$. 否则

$$
\triangle A B C \cap\left(y=y_{0}+m\right) \text { 长度 } \geq \frac{1}{2} \cdot\left(\triangle A B C \cap\left(y=y_{0}\right) \text { 长度 }\right) \geq 50 m \text {, }
$$

推出 $\triangle A B C \cap\left(y=y_{0}+m\right)$ 上有 $\geq 10$ 个“好点”.

同理对于 $i \leq-2$, 故

$\triangle A B C$ 内好点数 $\leq 2+(2 m+100)$ (由断言 $)+2 \leq \Theta(m)$,

(1)成立.

故11得证. 进而原题得证.

评注 本题是困难的组合几何问题, 有多种解法, 在各种解法中基本都要用到“将 $A O$ 延长 $m$ 倍”, 同时还要观察到其他方面的很多性质, 才能做出本题.

7.1 给定整数 $n \geq 2$. 求最小的正整数 $m$, 使得存在 $n^{2}$ 个两两不同的正实数 $x_{i, j}(1 \leq i, j \leq n)$ 满足以下条件:

(1) 对任意 $i, j, x_{i, j}=\max \left\{x_{i, 1}, x_{i, 2}, \cdots, x_{i, j}\right\}$ 或 $x_{i, j}=\max \left\{x_{1, j}, x_{2, j}, \cdots, x_{i, j}\right\}$;

(2) 对任意 $i$, 至多存在 $m$ 个下标 $k$, 使得 $x_{i, k}=\max \left\{x_{i, 1}, x_{i, 2}, \cdots, x_{i, k}\right\}$;

(3) 对任意 $j$, 至多存在 $m$ 个下标 $k$, 使得 $x_{k, j}=\max \left\{x_{1, j}, x_{2, j}, \cdots, x_{k, j}\right\}$.

解 结论是: $m$ 最小为 $\left\{\begin{array}{ll}\frac{n+2}{2}, & (2 \mid n) \\ \frac{n+3}{2}, & (2 \nmid n)\end{array}\right.$.
将 $x_{i, j}$ 排成 $n \times n$ 表格:

$$
\begin{array}{cccc}
x_{1,1} & x_{1,2} & \cdots & x_{1, n} \\
x_{2,1} & x_{2,2} & \cdots & x_{2, n} \\
\vdots & \vdots & & \vdots \\
x_{n, 1} & x_{n, 2} & \cdots & x_{n, n}
\end{array}
$$

称满足 $x_{i, j}=\max \left\{x_{i, 1}, \cdots, x_{i, j}\right\}$ 的 $x_{i, j}$ 是 “行好的”, 满足 $x_{i, j}=\max \left\{x_{1, j}, \cdots, x_{i, j}\right\}$的 $x_{i, j}$ 是 “列好的”.

(I) 先给出构造:

将 $n \times n$ 表格分成 4 部分 $\Omega_{1}, \Omega_{2}, \Omega_{3}, \Omega_{4},\left(r=\left[\frac{n}{2}\right], s=\left\lceil\frac{n}{2}\right\rceil\right)$.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-14.jpg?height=303&width=394&top_left_y=931&top_left_x=845)

令 $\Omega_{i}(1 \leq i \leq 4)$ 中的数均在 $(i, i+1)$ 中, 且 $\Omega_{1}, \Omega_{4}$ 中的数从左下到右上递增, $\Omega_{2}, \Omega_{3}$ 中的数从右上到左下递增.

例如: 若 $r=2, s=3$, 则 $\Omega_{2}$ 中可以填:

| 2.4 | 2.2 | 2.1 |
| :--- | :--- | :--- |
| 2.6 | 2.5 | 2.3 |

此时, 对 $1 \leq i \leq r$, 第 $i$ 行中 $x_{i, 1}, \cdots, x_{i, r+1}$ 是行好的, 对 $r+1 \leq i \leq n$, 第 $i$行中 $x_{i, 1}, x_{i, r+1}, x_{i, r+2}, \cdots, x_{i, n}$ 是行好的. 类似对于列.

故每一行(列) 中行(列)好的数的个数 $\leq \max \{s+1, r+1\}= \begin{cases}\frac{n+2}{2}, & 2 \mid n \\ \frac{n+3}{2}, & 2 \nmid n\end{cases}$

(II) 再证明 $m \geq\left[\frac{n+3}{2}\right]$.

显然, 第一行(列)中的数列均是列(行)好的.

对 $2 \leq i \leq n$, 设第 $i$ 行有 $\lambda_{i}$ 个数是行好的, 第 $i$ 列有 $\mu_{i}$ 个数是列好的.

由于对 $2 \leq i, j \leq n, x_{i, j}$ 或者行好, 或者列好, 故

$$
\sum_{i=2}^{n}\left(\lambda_{i}-1\right)+\sum_{i=2}^{n}\left(\mu_{i}-1\right) \geq(n-1)^{2}
$$

进而

$$
m \geq \max \left\{\lambda_{2}, \cdots, \lambda_{n}, \mu_{2}, \cdots, \mu_{n}\right\}
$$

$$
\begin{aligned}
& \geq \frac{1}{2(n-1)} \cdot\left(\sum_{i=2}^{n} \lambda_{i}+\sum_{i=2}^{n} \mu_{i}\right) \\
& \geq \frac{1}{2(n-1)} \cdot\left(2(n-1)+(n-1)^{2}\right) \\
& =\frac{n+1}{2} .
\end{aligned}
$$

现在用反证法, 假设 “ $m<\frac{n+2}{2}, 2 \mid n$ ”或 “ $m<\frac{n+3}{2}, 2 \nmid n$ ”, 由(2)知只能 $m=$ $\frac{n+1}{2}, 2 \nmid n$, 且(1), (2)中各 $\geq$ 号均取等. 这表明:

$$
\lambda_{2}=\cdots=\lambda_{n}=\mu_{2}=\cdots=\mu_{n}=\frac{n+1}{2},
$$

且每个 $x_{i, j}(2 \leq i, j \leq n)$ 不能同时行好, 列好(由(2). 考虑 $x_{i, j}((i, j) \neq(1,1))$ 中最大项 $x_{i_{0}, j_{0}}$.

若 $i_{0}, j_{0} \geq 2$, 则 $x_{i_{0}, j_{0}}$ 同时行好, 列好, 矛盾.

若 $1 \in\left\{i_{0}, j_{0}\right\}$, 不妨设 $i_{0}=1, j_{0} \geq 2$, 则第 $j_{0}$ 列中只有 $x_{1, j_{0}}$ 是列好的, 而

$$
\mu_{j_{0}}=\frac{n+1}{2} \geq \frac{3+1}{2}=2,
$$

矛盾.

故反证法不成立.

综上, 所求 $m$ 最小值为 $\left\{\begin{array}{ll}\frac{n+2}{2}, & (2 \mid n) \\ \frac{n+3}{2}, & (2 \nmid n)\end{array}\right.$.

评注 本题是中等难度的组合题, 本题的解答看似简单, 实际上有很多地方可能会卡住(例如猜测答案、构造).

7.2 如图所示, 锐角 $\triangle A B C(A B<A C)$ 的内心是 $I$, 外接圆是 $\odot O . M$ 和 $N$ 分别是弧 $\widehat{B A C}$ 和 $\widehat{B C}$ 的中点. $D$ 是 $\overparen{A C}$ 上一点, 满足 $A D / / B C . \triangle A B C$ 在 $\angle B A C$ 内的旁切圆与边 $B C$ 相切于点 $E$. 点 $F$ 在 $\triangle A B C$ 内, 满足 $I F / / B C$ 且 $\angle B A F=\angle C A E$. 设直线 $N F$ 与 $\odot O$ 的另一个交点是 $R$, 直线 $A F$ 与 $D I$ 相交于点 $K$, 直线 $A R$ 与 $I F$ 相交于点 $L$. 证明: $N K \perp M L$.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-15.jpg?height=480&width=534&top_left_y=2150&top_left_x=767)
证明 取 $B C$ 中点 $Z$. 熟知 $I Z / / A E$ 且 $\triangle N I Z \sim \triangle N M I$, 且

$$
\angle B A F=\angle C A E \Rightarrow \angle F A I=\angle E A I,
$$

故

$$
\angle F A I=\angle E A I=\angle Z I N=\angle I M N .
$$

这表明: $A F, M I$ 的交点在 $\odot O$ 上, 记为 $T$.

设 $N T \cap D I=Y$, 设 $\angle I N M=\alpha, \angle I M N=\beta$, 设 $F I \cap M N=H$. 注意到 $T M, T N$ 是 $\angle A T D$ 内、外角平分线, 故 $T A, T M, T D, T N$ 调和线束. 从而 $Y, K, I, D$ 调和点列, 进而 $N Y, N K, N I, N D$ 调和线束, 因此

$$
\frac{\sin \angle I N K}{\sin \angle T N K}=\frac{\sin \angle I N D}{\sin \angle T N D}=\frac{\sin 2 \alpha}{\cos (\alpha-\beta)}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-16.jpg?height=542&width=1136&top_left_y=1028&top_left_x=470)

另一方面, 在 $\triangle M A I$ 中, 由角元塞瓦,

$$
\begin{aligned}
\frac{\sin \angle A M L}{\sin \angle I M L} & =\frac{\sin \angle M A L}{\sin \angle I A L} \cdot \frac{\sin \angle A I L}{\sin \angle M I L} \\
& =-\tan \angle M A L \cdot \frac{\cos \alpha}{\cos \beta} \\
& =\tan \angle M N F \cdot \frac{\cos \alpha}{\cos \beta} .
\end{aligned}
$$

由 $\angle I H N=\angle I T N=90^{\circ}$ 知 $I, T, N, H$ 共圆, 进而 $\angle I T H=\alpha$, 在 $\triangle F N T$ 中,由角元塞瓦，

$$
\begin{aligned}
\tan \angle M N F & =\frac{\sin \angle F N H}{\sin \angle H F N} \\
& =\frac{\sin \angle H N T}{\sin \angle H T N} \cdot \frac{\sin \angle H T F}{\sin \angle H F T} \\
& =\frac{\cos \beta}{\cos \alpha} \cdot \frac{\sin 2 \alpha}{\cos (\alpha-\beta)} .
\end{aligned}
$$

将(3)带入(2)得

$$
\frac{\sin \angle A M L}{\sin \angle I M L}=\frac{\sin 2 \alpha}{\cos (\alpha-\beta)}
$$

结合(1)知:

$$
\frac{\sin \angle I N K}{\sin \angle T N K}=\frac{\sin \angle A M L}{\sin \angle I M L}
$$

又注意到: $A M \perp I N, I M \perp T N$, 故

$$
\angle I N K=\angle A M L, \angle T N K=\angle I M L,
$$

进而 $M L \perp N K$, 原题得证!

评注 本题是简单几何题, 注意到 $A M \perp I N, I M \perp T N$, 从而为证明 $M L \perp N K$,只需证: $\frac{\sin \angle A M L}{\sin \angle I M L}=\frac{\sin \angle I N K}{\sin \angle T N K}$, 导角元塞瓦就可以了.

7.3 记 $S(k)$ 为正整数 $k$ 在十进制表示下的所有数码之和. 求所有整数 $n \geq 2$和有理数 $\beta \in(0,1)$, 使得存在 $n$ 个两两不同的正整数 $a_{1}, a_{2}, \cdots, a_{n}$, 满足: 对于 $\{1,2, \cdots, n\}$ 的任意 $r(r \geq 2)$ 元子集 $I$, 有 $S\left(\sum_{i \in I} a_{i}\right)=\beta \cdot \sum_{i \in I} S\left(a_{i}\right)$.

解 结论是: 所求 $(n, \beta)$ 为使 $2 \leq n \leq 10, \beta \in(0,1) \cap \mathbb{Q}$ 的 $(n, \beta)$.

(I) 先给出 $2 \leq n \leq 10$ 的构造: 将 $a_{1}, \cdots, a_{n}$ 按数码分若干段, 每一段为(空白表示 0$)$ :

(I 类段)

$$
a_{1}: 099 \cdots 991 \quad \text { (s个9) }
$$

a2: $\quad 1$

an: $\quad 1$

(II类段)

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-17.jpg?height=254&width=205&top_left_y=1849&top_left_x=911)

取 $n$ 个 I 类段(轮换, 所有 $s$ 相同), $t$ 个 II 类段, 则

$$
S\left(a_{1}\right)=\cdots=S\left(a_{n}\right)=9 s+n+t,
$$

对 $I \subseteq\{1, \cdots, n\},|I| \geq 2$,

$$
S\left(\sum_{i \in I} a_{i}\right)=|I| \cdot n+|I| \cdot t
$$

只需选出 $s, t \in \mathbb{Z}^{+}$使 $n+t=\beta \cdot(9 s+n+t)$, 这显然可以做到.

(II) 再说明 $n \geq 11$ 不可行.
反证法: 假设 $n \geq 11$, 不妨设 $n=11$.

显然 $a_{1}$ 加 $a_{2}$ 时进位, 故可取 $T$ 为最小非负整数, 使得存在一对 $a_{i}, a_{j}(i \neq j)$相加时在 $10^{T}$ 位进位.

设 $a_{1}, \cdots, a_{11}$ 的 $10^{T}$ 位为 $x_{1}, \cdots, x_{11}$, 不妨设 $9 \geq x_{1} \geq \cdots \geq x_{11}=0$, 由于某对 $a_{i}, a_{j}$ 相加在 $10^{T}$ 位进位, 故 $x_{1}+x_{2} \geq 10$. 注意到, 对 $I_{1}, I_{2} \subseteq\{1, \cdots, 11\}, I_{1} \cap$ $I_{2}=\varnothing,\left|I_{1}\right|,\left|I_{2}\right| \geq 2$, 由于

$$
S\left(\sum_{i \in I_{1}} a_{i}\right)+S\left(\sum_{i \in I_{2}} a_{i}\right)=S\left(\sum_{i \in I_{1} \cup I_{2}} a_{i}\right)
$$

故 $\sum_{i \in I_{1}} a_{i}, \sum_{i \in I_{2}} a_{i}$ 相加不进位.

特别地, $\sum_{i \in I_{1}} x_{i}, \sum_{i \in I_{2}} x_{i}$ 相加在个位不进位.

易知 $x_{10} \neq 0$ (否则 $\left(x_{1}+x_{10}\right),\left(x_{2}+x_{11}\right)$ 相加进位, 矛盾), 故 $x_{10} \geq 1$. 现在将 $x_{1}, \cdots, x_{11}$ 分若干组 (允许有数不在任何组中), 每组 $\geq 2$ 个数, 各组数之和的个位数之和 $\geq 10$.

若(2)如成立, 则将各组之和依次相加, 即与(1)矛盾. 下面说明(2)成立.

先取出尽可能多的二元组, 每个二元组的和的个位数 $\geq 2$. 若取出了 5 个二元组, 则(2)成立. 下设至多取出 4 个二元组, 则剩下 $\geq 3$ 个数, 且剩下的数中, 无两数 $\in[1,4]$, 无两数 $\in[6,9]$, 故必剩下 0 或 5 至少一个.

若剩下的数有 0 , 则可推出剩下的数为 $0,1, \cdots, 1(\geq 2$ 个 1$)$, 矛盾.

故至少剩下一个 5 , 进而剩下的数只能是 “若干个 5 ”或“若干个 5 , 一个 6 ”, 将剩下的数三个三个一组, 设有 $m(0 \leq m \leq 4)$ 个二元组, $\left[\frac{11-2 m}{3}\right]$ 个三元组, 则各组数之和的个位数之和 $\geq 2 \cdot m+5 \cdot\left[\frac{11-2 m}{3}\right]$, 易验证 $m=0,1, \cdots, 4$ 时均有

$$
2 \cdot m+5 \cdot\left[\frac{11-2 m}{3}\right] \geq 10
$$

(2)成立. 故可推出矛盾!

结合 (I), (II) 即得原题所需结论.

评注 本题是困难的组合题, 第一个难点在猜答案, 有多种可能的方向, 构造也有一定难度, 不一定一下就能想到, 需要作一定尝试, 事实上, 若答案是“对某些 $n, \beta$ 不是空也不是全部”, 则在证明部分可能需要作大量讨论;若答案是“对每个 $n, \beta$ 或者空, 或者全部”, 则在构造部分要达到 $\beta$ 很小, 需要构造很多的进位, 本题最终的答案是后一种, 在证明的部分, 需首先猜到只需考虑第 1 个进位的那一位,进而归结于一个关于 $x_{1}, \cdots, x_{11}$ 的小问题, 最后的这个小问题还需要选取合适的分类讨论的方法(在考场时间内能讨论完). 本题是第二轮选拔最难的一题.

8.4 对所有实数 $x_{1}, x_{2}, \cdots, x_{60} \in[-1,1]$, 求

$$
\sum_{i=1}^{60} x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)
$$

的最大可能值, 这里 $x_{0}=x_{60}, x_{61}=x_{1}$.

解 注意到

$$
\sum_{i=1}^{60} x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)=\frac{1}{3} \sum_{i=1}^{60}\left(x_{i+1}-x_{i}\right)^{3} .
$$

对 $1 \leq i \leq 60$, 记 $y_{i}=x_{i+1}-x_{i}$, 由 $x_{i}, x_{i+1} \in[-1,1]$ 知 $y_{i} \in[-2,2]$, 进而

$$
\left(y_{i}-2\right)\left(y_{i}+1\right)^{2} \leq 0,
$$

即

$$
y_{i}^{3} \leq 3 y_{i}+2
$$

从而

$$
\sum_{i=1}^{60} x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)=\frac{1}{3} \cdot \sum_{i=1}^{60} y_{i}^{3} \leq \frac{1}{3} \cdot \sum_{i=1}^{60}\left(3 y_{i}+2\right)=40
$$

另一方面, 令 $\left(x_{1}, \cdots, x_{60}\right)=(1,0,-1,1,0,-1, \cdots, 1,0,-1)$. 此时

$$
\sum_{i=1}^{60} x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)=40
$$

故

$$
\sum_{i=1}^{60} x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)
$$

的最大值为 40 .

评注 本题是简单的不等式, 注意到 $\sum x_{i}^{2}\left(x_{i+1}-x_{i-1}\right)$ 就是 $\frac{1}{3} \cdot \sum\left(x_{i+1}-x_{i}\right)^{3}$就可以了。

8.5 求最小的正实数 $\alpha$, 使得对面积为 1 的任意凸多边形 $P$, 存在平面上一点 $M$ 使得 $P \cup Q$ 的凸包的面积不超过 $\alpha$. 这里 $Q$ 为 $P$ 关于点 $M$ 的中心对称图形.

解 结论是: $\alpha$ 最小为 2 .

(I) 一方面, 令 $P$ 是正 $\triangle A B C$.

若 $M$ 在 $P$ 外, 则 $P \cup Q=\varnothing$, 进而

$$
P \cup Q \text { 凸包面积 } \geq P \cup Q \text { 面积 }=2 \text {. }
$$

若 $M$ 在 $P$ 内, 设 $A, B, C$ 关于 $M$ 对称点为 $A^{\prime}, B^{\prime}, C^{\prime}$, 则

$P \cup Q$ 凸包面积 $\geq S_{\triangle A M B^{\prime}}+S_{\triangle B^{\prime} M C}+S_{\triangle C M A^{\prime}}+S_{\triangle A^{\prime} M B}+S_{\triangle B M C^{\prime}}+S_{\triangle C^{\prime} M A}$

$$
\begin{aligned}
& =2\left(S_{\triangle A M B}+S_{\triangle B M C}+S_{\triangle C M A}\right) \\
& =2
\end{aligned}
$$

故 $\alpha \geq 2$.

![](https://cdn.mathpix.com/cropped/2024_02_26_920881ecaf1cd4cd5ff9g-20.jpg?height=394&width=508&top_left_y=448&top_left_x=777)

(II) 另一方面, 我们说明 $\alpha=2$ 符合要求.

取 $P$ 的距离最远 (之一)的一对顶点 $A, B$, 建系, 设 $A(0,0), B(L, 0), L>0$,则

$$
P \subseteq\{(x, y) \mid 0 \leq x \leq L, y \in \mathbb{R}\} \text { (由 } A B \text { 最长). }
$$

取 $M$ 为 $\left(\frac{L}{2}, 0\right)$. 设 $P \cup Q$ 的凸包是 $R$, 由对称性, 为说明 $S_{R} \leq 2$, 只需说明 $S_{R_{1}} \leq S_{P_{1}}+S_{Q_{1}}$, 这里 $P_{1}, Q_{1}, R_{1}$ 分别是 $P, Q, R$ 与第一象限的交.

注意到 $P_{1}, Q_{1}, R_{1}$ 可看作凸函数的图像, 设 $P_{1}, Q_{1}, R_{1}$ 分别对应 $f_{1}(x), f_{2}(x)$, $g(x)(x \in[0, L])$, 则

$$
S_{P_{1}}=\int_{0}^{L} f_{1}(x) d x, S_{Q_{1}}=\int_{0}^{L} f_{2}(x) d x, S_{R_{1}}=\int_{0}^{L} g(x) d x .
$$

为说明 $S_{p_{1}}+S_{Q_{1}} \geq S_{R_{1}}$, 只需说明对 $x \in[0, L]$, 有

$$
f_{1}(x)+f_{2}(x) \geq g(x) .
$$

取定 $x$, 由 $R$ 的定义知 $g(x)$ 可表示为

$$
\frac{x-\alpha}{\beta-\alpha} \cdot f_{i}(\beta)+\frac{\beta-x}{\beta-\alpha} \cdot f_{j}(\alpha)
$$

这里 $0 \leq \alpha \leq x \leq \beta \leq L, \alpha \neq \beta, i, j \in\{1,2\}$. 由于 $f_{1}, f_{2}$ 值域 $\subseteq[0,+\infty)$, 故

$$
\begin{aligned}
g(x) & =\frac{x-\alpha}{\beta-\alpha} \cdot f_{i}(\beta)+\frac{\beta-x}{\beta-\alpha} \cdot f_{j}(\alpha) \\
& \leq \frac{x-\alpha}{\beta-\alpha} \cdot f_{1}(\beta)+\frac{\beta-x}{\beta-\alpha} \cdot f_{1}(\alpha)+\frac{x-\alpha}{\beta-\alpha} \cdot f_{2}(\beta)+\frac{\beta-x}{\beta-\alpha} \cdot f_{2}(\alpha) \\
& \leq f_{1}(x)+f_{2}(x), \quad \text { (凸性) }
\end{aligned}
$$

进而 $S_{R} \leq 2$.

综上, $\alpha$ 最小值为 2 .

评注 本题是简单的组合几何, 得到 $\alpha \geq 2$ 的构造后, 证明部分也不难.

8.6. 给定整数 $n \geq 2$. 有 $2 n^{2}$ 位选手参加中国象棋比赛, 每两位选手恰对亦一局, 结果可有平局. 已知

(1) 对任意三位选手甲、乙、丙, 若甲胜乙, 且乙胜丙, 则甲胜丙;

(2) 所有比赛中平局的场数不超过 $\frac{n^{3}}{16}$.

证明: 可从这 $2 n^{2}$ 位选手中选出 $n^{2}$ 位选手, 并适当记作 $P_{i j}(1 \leq i, j \leq n)$, 使得对任意 $i, j, i^{\prime}, j^{\prime} \in\{1,2, \cdots, n\}$, 若 $i>i^{\prime}$, 则 $P_{i j}$ 胜 $P_{i^{\prime} j^{\prime}}$.

证明 记 $t=\left\lceil\frac{n}{4}\right\rceil \in \mathbb{Z}^{+}$.

先去掉平局次数 $\geq t$ 的选手, 则去掉的选手数 $\leq \frac{\frac{n^{3}}{8}}{t} \leq \frac{n^{2}}{2}$, 故至少剩下 $\frac{3 n^{2}}{2}$名选手, 记为 $V_{1}, \cdots, V_{N}\left(N \geq \frac{3 n^{2}}{2}\right)$, 约定自己胜自己, 则“胜” 是 $V_{1}, \cdots, V_{N}$ 上的偏序关系. 作拓扑排序, 不妨设: 对 $1 \leq i, j \leq N$, 若 $V_{i}$ 胜 $V_{j}$, 则 $i \leq j$. 现在将 $V_{1}, \cdots, V_{N}$ 取出前 $n^{2}+(n-1)(2 t-2)$ 项, 分成 $2 n-1$ 段 $\Gamma_{1}, \cdots, \Gamma_{2 n-1}$, 每段依次含 $n, 2 t-2, n, 2 t-2, \cdots, n, 2 t-2, n$ 名选手, 由于

$$
n \cdot n+(n-1)(2 t-2) \leq n \cdot n+(n-1)\left(2 \cdot\left(\frac{n}{4}+1\right)-2\right)<\frac{3 n^{2}}{2}
$$

故这可以做到.

现在选取 $P_{i, j}$, 记

$$
A_{i}=\left\{P_{i, 1}, \cdots, P_{i, n}\right\} \quad(1 \leq i \leq n)
$$

令

$$
\left(A_{1}, \cdots, A_{n}\right)=\left(\Gamma_{2 n-1}, \cdots, \Gamma_{5}, \Gamma_{3}, \Gamma_{1}\right),
$$

我们验证这样就符合要求.

任取 $\alpha=P_{i, j}, \beta=P_{i^{\prime}, j^{\prime}}, i>i^{\prime}$. 设 $\alpha \in \Gamma_{p}, \beta \in \Gamma_{q}$, 由 $i>i^{\prime}$ 知 $p \equiv q \equiv 1$ $(\bmod 2)$, 且 $p<q$, 设 $\alpha=V_{r}, \beta=V_{s}$, 由于 $\Gamma_{p}, \Gamma_{q}$ 之间有一个长为 $2 t-2$ 的段, 故 $s-r \geq 2 t-1$, 进而存在 $r \leq k \leq s$, 使 $V_{r}$ 与 $V_{k}, V_{k}$ 与 $V_{s}$ 均不是平局 (因为 $V_{r}, V_{s}$平局数均 $\leq t-1)$. 从而 $V_{r}$ 胜 $V_{k}, V_{k}$ 胜 $V_{s}$, 推出 $V_{r}$ 胜 $V_{s}$.

故这样的 $P_{i, j}$ 符合要求.

原题得证!

评注 本题是中等难度的组合题, 首先注意到 $\frac{1}{16}$ 很小, 可以先考虑 $\Theta\left(n^{3}\right)$, 由此想到可以先去掉平局数很多的人(量级估计的常用手法)(事实上, 后面再具体计算 $n^{3}$ 前的系数发现 $\frac{1}{16}$ 刚好够). 后面选取 $P_{i, j}$ 有多种可能的方向, 需大胆尝试,这与 IMO 2017 第 5 题比较像, 本题是一个很好的具有选拔功能的组合题.

