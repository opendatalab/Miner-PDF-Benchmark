# 2021 年 IMO 试题解答与评析 

王一川<br>(华东师范大学第二附属中学, 201203)<br>指导教师: 唐立华

2021 年第 62 届 IMO 于 7 月 $19-20$ 日举行, 受疫情影响, 今年的 IMO 改为线上举行, 中国队队员在北京大学进行考试, 考试时间为北京时间 7 月 19-20 日 $15: 30-20: 00$. 本次比赛结果为: 金牌分数线 24 分 (为历年最低), 中国队全部队员获得金牌,且获得团体总分第一及个人第一.

本届 IMO 试题优美, 难度分布合理, 其中 1,4 为简单题, 5,6 为中档题, 2,3 为难题. 第 1 天的 2,3 均有难度, 整体难度较大, 很有挑战性, 其中 2 侧重思维, 3 比较耗时, 对选手的做题能力及考场策略均有要求. 第 2 天整体难度较低, 具有国家队水平的选手或优秀的集训队队员都能拿满分.

本文将介绍本次比赛的试题及解答, 因作者水平有限, 不当之处在所难免,请读者不吝赐教.

## I. 试 题

1. 设整数 $n \geq 100$. 伊凡把 $n, n+1, \cdots, 2 n$ 的每个数写在不同的卡片上.然后他将这 $n+1$ 张卡片打乱顺序并分成两堆. 证明: 至少有一堆中包含两张卡片，使得这两张卡片上的数之和是一个完全平方数.
2. 对任意实数 $x_{1}, \cdots, x_{n}$, 证明下述不等式成立:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}-x_{j}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}+x_{j}\right|}
$$

3. 设 $D$ 是锐角三角形 $A B C(A B>A C)$ 内部一点, 使得 $\angle D A B=\angle C A D$.线段 $A C$ 上的点 $E$ 满足 $\angle A D E=\angle B C D$, 线段 $A B$ 上的点 $F$ 满足 $\angle F D A=$ $\angle D B C$, 且直线 $A C$ 上的点 $X$ 满足 $C X=B X$. 设 $O_{1}$ 和 $O_{2}$ 分别为三角形 $A D C$和三角形 $E X D$ 的外心. 证明: 直线 $B C, E F$ 和 $O_{1} O_{2}$ 共点.

修订日期: 2021-08-17.

4. 设圆 $\Gamma$ 的圆心为 $I$. 凸四边形 $A B C D$ 满足: 线段 $A B, B C, C D$ 和 $D A$都与 $\Gamma$ 相切. 设 $\Omega$ 是三角形 $A I C$ 的外接圆. $B A$ 往 $A$ 方向的延长线交 $\Omega$ 于点 $X, B C$ 往 $C$ 方向的延长线交 $\Omega$ 于点 $Z, A D$ 往 $D$ 方向的延长线交 $\Omega$ 于点 $Y, C D$ 往 $D$ 方向的延长线交 $\Omega$ 于点 $T$. 证明:

$$
A D+D T+T X+X A=C D+D Y+Y Z+Z C
$$

5. 两只松鼠 $B$ 和 $J$ 为过冬收集了 2021 枚核桃. $J$ 将核桃依次编号为 1 到 2021 , 并在它们最喜欢的树周围挖了一圈共 2021 个小坑. 第二天早上, $J$ 发现 $B$已经在每个小坑里放人了一枚核桃, 但并未注意编号. 不开心的 $J$ 决定用 2021 次操作来改变这些核桃的位置. 在第 $k$ 次操作中, $J$ 把与第 $k$ 号核桃相邻的两枚核桃交换位置. 证明: 存在某个 $k$, 使得在第 $k$ 次操作中, $J$ 交换了两枚编号为 $a$和 $b$ 的核桃, 且 $a<k<b$.
6. 设整数 $m \geq 2$. 设集合 $A$ 由有限个整数 (不一定为正) 构成, 且 $B_{1}, B_{2}$, $B_{3}, \cdots, B_{m}$ 是 $A$ 的子集. 假设对任意 $k=1,2, \cdots, m, B_{k}$ 中所有元素之和为 $m^{k}$. 证明: $A$ 包含至少 $\frac{m}{2}$ 个元素.

## II . 解答与评注

1. 设整数 $n \geq 100$. 伊凡把 $n, n+1, \cdots, 2 n$ 的每个数写在不同的卡片上.然后他将这 $n+1$ 张卡片打乱顺序并分成两堆. 证明: 至少有一堆中包含两张卡片，使得这两张卡片上的数之和是一个完全平方数.

证明 只需选取整数 $k \geq 2$, 使 $n \leq 2 k^{2}-4 k<2 k^{2}+4 k \leq 2 n$. 这是因为若如此, 则三张卡片 $2 k^{2}-4 k, 2 k^{2}+1,2 k^{2}+4 k$ 两两和为完全平方数, 由抽庹原理,必有两张在同一堆.

取最大正整数 $k$, 使 $2 k^{2}+4 k \leq 2 n$, 则 $2(k+1)^{2}+4(k+1)>2 n$, 即 $n<k^{2}+4 k+3$.

我们说明 $n \leq 2 k^{2}-4 k$, 为此只需证明 $k^{2}+4 k+3 \leq 2 k^{2}-4 k$.

若 $k \geq 9$, 易验证 $k^{2}+4 k+3 \leq 2 k^{2}-4 k \Leftrightarrow k(k-8) \geq 3$.

若 $k \leq 8$, 则 $n<k^{2}+4 k+3 \leq 8^{2}+4 \cdot 8+3=99$, 与 $n \geq 100$ 矛盾.

故 $n \leq 2 k^{2}-4 k$, 这样选取的 $k$ 即符合要求. 原题得证.

评注 本题是简单题. 计算的时候会发现题中的 100 还是比较紧的, 所以有些解法需要讨论较小的 $n$. 另外, 本题无法分辨是组合还是数论, 不能推测出第 2
天的题型.

2. 对任意实数 $x_{1}, \cdots, x_{n}$, 证明下述不等式成立:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}-x_{j}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}+x_{j}\right|}
$$

证明 对 $n$ 归纳.

$n=1$ 时结论显然.

$n \geq 2$ 时, 若 $x_{1}, x_{2}$ 含 0 或同正负, 结论显然.

若 $x_{1}, x_{2}$ 异正负, 设 $\left|x_{1}\right|=a,\left|x_{2}\right|=b$, 不妨设 $a \geq b$, 则

原不等式 $\Leftrightarrow \sqrt{2 a}+\sqrt{2 b}+2 \cdot \sqrt{a-b} \geq 2 \cdot \sqrt{a+b}$.

注意到

$$
\begin{aligned}
\sqrt{2 a}+\sqrt{2 b}+2 \cdot \sqrt{a-b} & \geq 2 \cdot \sqrt{2 b}+2 \cdot \sqrt{a-b} \\
& \geq 2 \cdot \sqrt{2 b+(a-b)} \\
& =2 \cdot \sqrt{a+b}
\end{aligned}
$$

故结论成立.

$n \geq 3$ 时, 假设 $n$ 更小时结论成立.

先作调整, 任取 $d \in \mathbb{R}$, 将 $x_{1}, \cdots, x_{n}$ 调整为 $x_{1}+d, \cdots, x_{n}+d$, 则原不等式左边不变, 右边变为 $\sum_{i, j=1}^{n} \sqrt{\left|x_{i}+x_{j}+2 d\right|}$, 记为 $f(d)$.

函数 $y=\sqrt{|2 x|}$ 的图像如下图:

![](https://cdn.mathpix.com/cropped/2024_02_26_1615ab04df0b21753461g-03.jpg?height=502&width=594&top_left_y=1702&top_left_x=731)

即: 在 $(-\infty, 0]$ 递减, 在 $[0,+\infty)$ 递增, 且在两部分分别是上凸的.

而 $f(d)$ 可看作若干个上图所示函数的平移的叠加, 从而假设所有 $\frac{-x_{i}-x_{j}}{2}$ 将 $(-\infty,+\infty)$ 分成若干段, 则 $f$ 在每一个有限段上上凸, 在两侧的无限段上单调 (且趋于 $\pm \infty$ 时 $f$ 值充分大), 故可将 $d$ 取为某个 $\frac{-x_{i}-x_{j}}{2}$, 使 $f$ 最小, 作此调整后原不等式变强, 此时存在一对 $x_{i}, x_{j}$ (允许相同) 和为 0 .
不妨设 $x_{1}=0$ 或 $x_{1}+x_{2}=0$.

情形 $1 x_{1}=0$. 此时原不等式

$$
\begin{aligned}
& \Leftrightarrow \sum_{i, j=2}^{n} \sqrt{\left|x_{i}-x_{j}\right|}+2 \cdot \sum_{i=2}^{n} \sqrt{\left|x_{i}\right|} \leq \sum_{i, j=2}^{n} \sqrt{\left|x_{i}+x_{j}\right|}+2 \cdot \sum_{i=2}^{n} \sqrt{\left|x_{i}\right|} \\
& \Leftrightarrow \sum_{i, j=2}^{n} \sqrt{\left|x_{i}-x_{j}\right|} \leq \sum_{i, j=2}^{n} \sqrt{\left|x_{i}+x_{j}\right|},
\end{aligned}
$$

由归纳假设, 原不等式成立.

情形 $2 x_{1}+x_{2}=0$. 此时原不等式等价于

$$
\begin{aligned}
& \sum_{i, j=1}^{2} \sqrt{\left|x_{i}-x_{j}\right|}+\sum_{i, j=3}^{n} \sqrt{\left|x_{i}-x_{j}\right|}+2 \cdot \sum_{i=3}^{n}\left(\sqrt{\left|x_{1}-x_{i}\right|}+\sqrt{\left|x_{2}-x_{i}\right|}\right) \\
& \leq \sum_{i, j=1}^{2} \sqrt{\left|x_{i}+x_{j}\right|}+\sum_{i, j=3}^{n} \sqrt{\left|x_{i}+x_{j}\right|}+2 \cdot \sum_{i=3}^{n}\left(\sqrt{\left|x_{1}+x_{i}\right|}+\sqrt{\left|x_{2}+x_{i}\right|}\right)
\end{aligned}
$$

其中,

$$
\begin{aligned}
2 \cdot \sum_{i=3}^{n}\left(\sqrt{\left|x_{1}-x_{i}\right|}+\sqrt{\left|x_{2}-x_{i}\right|}\right) & =2 \cdot \sum_{i=3}^{n}\left(\sqrt{\left|-x_{2}-x_{i}\right|}+\sqrt{\left|-x_{1}-x_{i}\right|}\right) \\
& =2 \cdot \sum_{i=3}^{n}\left(\sqrt{\left|x_{1}+x_{i}\right|}+\sqrt{\left|x_{2}+x_{i}\right|}\right)
\end{aligned}
$$

对 $\left(x_{1}, x_{2}\right),\left(x_{3}, \cdots, x_{n}\right)$ 分别用归纳假设知

$$
\begin{aligned}
\sum_{i, j=1}^{2} \sqrt{\left|x_{i}-x_{j}\right|} & \leq \sum_{i, j=1}^{2} \sqrt{\left|x_{i}+x_{j}\right|} \\
\sum_{i, j=3}^{n} \sqrt{\left|x_{i}-x_{j}\right|} & \leq \sum_{i, j=3}^{n} \sqrt{\left|x_{i}+x_{j}\right|}
\end{aligned}
$$

(1) $+(2)+(3)$ 知原不等式也成立.

综上, 由归纳法, 原题得证.

评注 本题是困难的不等式. 本题需观察到可以作调整 $x_{i} \rightarrow x_{i}+d(\forall i)$, 这样调整后就可以归纳了. 其中的调整有多种可能的调整方法, 需尝试, 并选择一种可用的. 本题还有一些其他的 (超出竞赛范畴的) 解法, 例如本题形式上和著名不等式 $\sum \frac{a_{i} a_{j}}{i+j} \geq 0$ 比较像, 从而可能尝试积分, 但所需用到的积分公式是竞赛选手不知道的。

本题中“调整平移+归纳”的方法也可以用来解决 2009 年集训队测试第 1 天第 3 题:

$$
2 X Y \cdot \sum\left|x_{i}-y_{j}\right| \geq X^{2} \cdot \sum\left|y_{i}-y_{j}\right|+Y^{2} \cdot \sum\left|x_{i}-x_{j}\right|
$$

3. 设 $D$ 是锐角三角形 $A B C(A B>A C)$ 内部一点, 使得 $\angle D A B=\angle C A D$.线段 $A C$ 上的点 $E$ 满足 $\angle A D E=\angle B C D$, 线段 $A B$ 上的点 $F$ 满足 $\angle F D A=$
$\angle D B C$, 且直线 $A C$ 上的点 $X$ 满足 $C X=B X$. 设 $O_{1}$ 和 $O_{2}$ 分别为三角形 $A D C$和三角形 $E X D$ 的外心. 证明: 直线 $B C, E F$ 和 $O_{1} O_{2}$ 共点.

证明 (1) 记 $B C \cap E F=P$.

先证明: $B, C, E, F$ 共圆且 $D P$ 与 $\odot B C D$ 相切.

延长 $A D$ 与 $\odot B C D$ 交于 $D^{\prime}$, 则

$$
\angle A D^{\prime} C=\angle D B C=\angle A D F
$$

同理 $\angle A D^{\prime} B=\angle A D E$, 再结合 $\angle B A D=\angle C A D$ 可知 $A E D F \sim A B D^{\prime} C$, 故 $\frac{A E}{A F}=\frac{A B}{A C}$, 推出 $B, C, E, F$ 共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_1615ab04df0b21753461g-05.jpg?height=531&width=540&top_left_y=888&top_left_x=764)

设 $\odot D E F$ 在 $D$ 处切线 $\alpha, \odot B D C D^{\prime}$ 在 $D, D^{\prime}$ 处切线 $\beta, \beta^{\prime}$, 则

$$
\begin{aligned}
\measuredangle(\alpha, A D) & =\measuredangle\left(A D, \beta^{\prime}\right) \quad(\text { 由相似 }) \\
& =\measuredangle(\beta, A D) \quad\left(\text { 在 } \odot B D C D^{\prime} \text { 中 }\right)
\end{aligned}
$$

故 $\alpha / / \beta$, 进而 $\alpha=\beta$, 即 $\odot B D C, \odot D E F$ 相切. 再对 $\odot B C D, \odot D E F, \odot B C E F$应用根心定理知 $D P$ 与 $\odot B D C$ 相切.

(2) 取 $\triangle A B C$ 外接圆 $\widehat{B C}, \widehat{B A C}$ 中点, $N, M$, 过 $C$ 作 $\odot A D C$ 切线与 $M N$交于 $Z$, 设 $Z D$ 与 $\odot A D C$ 交于另一点 $Y$.

断言 $Y$ 在 $\odot D E X$ 上.

取 $Z X$ 上一点 $L$, 使 $Z L \cdot Z X=Z D \cdot Z Y=Z C^{2}$, 则 $X, L, D, Y$ 共圆且 $\triangle Z L C \sim \triangle Z C X$, 从而

$$
\angle Z L C=\angle X C Z=\angle N D C,
$$

其中 $\angle X C Z=\angle N D C$ 是因为 $Z C$ 与 $\odot A C D$ 相切.

故 $N, L, D, C$ 共圆, 从而

$$
\angle D L X=\angle D C N=\angle D C B+\angle B C N=\angle A D E+\angle D A C=\angle D E C,
$$

推出 $X, L, D, E$ 共圆, 进而 $X, L, D, E, Y$ 五点共圆, 特别地, $Y$ 在 $\odot D E X$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_1615ab04df0b21753461g-06.jpg?height=753&width=468&top_left_y=206&top_left_x=794)

(3) 最后证原题结论.

为证 $O_{1} O_{2}, B C, E F$ 共线, 只要证 $O_{1}, O_{2}, P$ 共线, 只要证 $P D=P Y$, 其中 $D, Y$ 为 $\odot A D C, \odot E X D$ 两交点.

![](https://cdn.mathpix.com/cropped/2024_02_26_1615ab04df0b21753461g-06.jpg?height=605&width=640&top_left_y=1262&top_left_x=705)

由于

$$
Z B^{2}=Z C^{2}=Z D \cdot Z Y
$$

故

$$
\triangle Z B D \sim \triangle Z Y B, \triangle Z C D \sim \triangle Z Y C
$$

故

$$
\frac{B D}{B Y}=\sqrt{\frac{D Z}{Y Z}}=\frac{C D}{C Y}
$$

进而 $\frac{B D}{C D}=\frac{B Y}{C Y}$, 进而

$$
\frac{B Y}{C Y}=\frac{B D}{C D}=\sqrt{\frac{B P}{C P}} \text { (因为 } D P \text { 与 } \odot B C D \text { 相切), }
$$

故 $\triangle P C Y \sim \triangle P Y B$, 从而

$$
P Y=\sqrt{P C \cdot P B}=P D
$$

进而原题得证.

评注 本题是困难的非条件几何题. 本题的一大难点是不太能算, 直接导比例导不出来, 需要观察到很多纯几何的性质, 若用计算法也要用到一些巧妙的操作. 本题的另一难点是耗时, 无论用什么方法都会花很长时间, 再加上第 2 题较困难不一定能做出, 对考场策略及心态也有较高的要求. 本题作为一个非条件型的几何题当然有很多解法, 大家可自行参考纯几何吧及 AOPS.

集训队测试的时候有选手表示: “这几何题怎么出得这么难! 第一次在正式考场上没做出几何题!"

IMO 的时候又有选手表示: “第一次在正式考场上没做出几何题!”

4. 设圆 $\Gamma$ 的圆心为 $I$. 凸四边形 $A B C D$ 满足: 线段 $A B, B C, C D$ 和 $D A$都与 $\Gamma$ 相切. 设 $\Omega$ 是三角形 $A I C$ 的外接圆. $B A$ 往 $A$ 方向的延长线交 $\Omega$ 于点 $X, B C$ 往 $C$ 方向的延长线交 $\Omega$ 于点 $Z, A D$ 往 $D$ 方向的延长线交 $\Omega$ 于点 $Y, C D$ 往 $D$ 方向的延长线交 $\Omega$ 于点 $T$. 证明:

$$
A D+D T+T X+X A=C D+D Y+Y Z+Z C .
$$

证明 注意到 $A I, C I$ 是 $\angle X A Y, \angle Z C T$ 外角平分线, 故 $I$ 是 $\widehat{X A Y}$ 中点,也是 $\widehat{T C Z}$ 中点, 故 $X Y, T Z$ 均与 $\odot A I C$ 过 $I$ 的切线平行, 得 $X Y / / T Z$, 由 $X Y / / T Z$ 知

$$
T X=Y Z
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_1615ab04df0b21753461g-07.jpg?height=662&width=534&top_left_y=1939&top_left_x=750)
又注意到

$$
\begin{aligned}
A D+D T+X A & =A H+H D+D T+X A \\
& =A E+G D+D T+X A \\
& =X A+A E+T D+D G \\
& =X E+T G .
\end{aligned}
$$

同理

$$
C D+D Y+Z C=Y H+Z F .
$$

其中由勾股定理,

$$
X E=\sqrt{X I^{2}-E I^{2}}=\sqrt{Y I^{2}-H I^{2}}=Y H .
$$

同理 $T G=Z F$.

故

$$
A D+D T+X A=C D+D Y+Z C .
$$

(1) $+(4)$ 即得原题结论.

评注 本题是简单的几何题, 注意到弧中点后就不难了. 本题形式上和 2020 年 CMO 第 4 题比较像: 两题均不用构造巧妙的辅助点, 且要证结论都是含 + 号的形式对称的等式.

5. 两只松鼠 $B$ 和 $J$ 为过冬收集了 2021 枚核桃. $J$ 将核桃依次编号为 1 到 2021 , 并在它们最喜欢的树周围挖了一圈共 2021 个小坑. 第二天早上, $J$ 发现 $B$已经在每个小坑里放人了一枚核桃, 但并未注意编号. 不开心的 $J$ 决定用 2021 次操作来改变这些核桃的位置. 在第 $k$ 次操作中, $J$ 把与第 $k$ 号核桃相邻的两枚核桃交换位置. 证明: 存在某个 $k$, 使得在第 $k$ 次操作中, $J$ 交换了两枚编号为 $a$和 $b$ 的核桃, 且 $a<k<b$.

证明 对 $1 \leq k \leq 2021$, 设第 $k$ 次操作后 $1, \cdots, k$ 号核桃所在坑构成集合 $P_{k}$, 并约定 $P_{0}=\varnothing$.

用反证法, 假设原题结论不成立, 考虑 $P_{k-1}$ 与 $P_{k}(k=1, \cdots, 2021)$ 的关系: 设第 $k$ 次操作中 $k$ 号核桃所在坑为 $H_{j}, H_{j}$ 左, 右的坑为 $H_{j-1}, H_{j+1}$, 则除 $H_{j-1}, H_{j}, H_{j+1}$ 外其余坑是否属于 $P_{k-1}, P_{k}$ 的状态相同.

(1) 若 $k$ 号核桃两侧的核桃编号均小于 $k$, 则

$$
H_{j-1} \in P_{k-1}, H_{j} \notin P_{k-1}, H_{j+1} \in P_{k-1}
$$

$$
H_{j-1} \in P_{k}, H_{j} \in P_{k}, H_{j+1} \in P_{k}
$$

(2) 若 $k$ 号核桃两侧的核桃编号均大于 $k$, 则

$$
\begin{gathered}
H_{j-1} \notin P_{k-1}, H_{j} \notin P_{k-1}, H_{j+1} \notin P_{k-1} \\
H_{j-1} \notin P_{k}, H_{j} \in P_{k}, H_{j+1} \notin P_{k}
\end{gathered}
$$

观察 (1) (2) 知: $P_{k-1} \subseteq P_{k}, P_{k} \backslash P_{k-1}=\left\{H_{j}\right\}$.

现在对 $1 \leq k \leq 2020$, 设 $P_{k}$ 中的坑构成圆周上若干段, 各段长度构成无序组 $\alpha_{k}$, 对 $2 \leq k \leq 2020$, 观察 (1) (2) 知:

- 或者 $\alpha_{k}$ 为 $\alpha_{k-1}$ 中加入一项 1 (对应 (2))
- 或者 $\alpha_{k}$ 为 $\alpha_{k-1}$ 中去掉两项, 并加入其和再加 1 (对应 (1))

结合 $\alpha_{1}=(1)$, 归纳易知 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{2020}$ 中各项均为奇数, 而另一方面,显然 $\alpha_{2020}=(2020)$, 矛盾.

故反证法不成立. 原题得证.

评注 本题是中等难度的组合题, 其中“考虑第 $k$ 步后 $1, \cdots, k$ 号核桃的位置的集合”的操作看起来很巧妙, 这一步可通过下述方法诱导出: (反证法)

先取一个 $t$, 使初始时 $1, \cdots, t$ 号核桃两两不相邻, 考虑前 $t$ 次操作, 则可以看作“对初始顺序作调整, 且操作直接从 $(t+1)$ 号核桃开始”, 如果取最大的这样的 $t$, 则操作 $t+1$ 时交换两个小核桃也可看作 “调整初始顺序, 操作从 $t+2$ 开始”. 反复如此, 会发现全部不用操作了, 再仔细分析这个过程就可以诱导出原题做法。

6. 设整数 $m \geq 2$. 设集合 $A$ 由有限个整数 (不一定为正) 构成, 且 $B_{1}, B_{2}$, $B_{3}, \cdots, B_{m}$ 是 $A$ 的子集. 假设对任意 $k=1,2, \cdots, m, B_{k}$ 中所有元素之和为 $m^{k}$. 证明: $A$ 包含至少 $\frac{m}{2}$ 个元素.

证明 设 $A=\left\{a_{1}, \cdots, a_{n}\right\}$, 用反证法, 假设 $n<\frac{m}{2}$.

将 $B_{i}$ 看作向量 $\overrightarrow{v_{i}}=\left(\epsilon_{i, 1}, \cdots, \epsilon_{i, n}\right)$, 其中 $\epsilon_{i, j}=\left\{\begin{array}{l}0,\left(a_{j} \notin B_{i}\right) \\ 1,\left(a_{j} \in B_{i}\right)\end{array}\right.$

首先选取 $\mu_{1}, \cdots, \mu_{m} \in\{-m+1,-m+2, \cdots, m-1\}$ (不全为 0 ), 使

$$
\sum_{i=1}^{m} \mu_{i} \cdot \overrightarrow{v_{i}}=\overrightarrow{0}
$$

考虑所有形如 $\sum_{i=1}^{m} \lambda_{i} \vec{v}_{i}$ 的向量, 其中 $\left(\lambda_{1}, \cdots, \lambda_{m}\right) \in\{0,1, \cdots, m-1\}^{m}$, 这样作出了 $m^{m}$ 个向量.
另一方面, 这样的向量每一项 $\in\{0,1, \cdots, m(m-1)\}$, 共 $n$ 个维度.

故这样的向量的可能值个数 $\leq(m(m-1)+1)^{n} \leq m^{2 n}<m^{m}$, 由抽屉原理,必有两组 $\left(\lambda_{1}, \cdots, \lambda_{m}\right) \neq\left(\lambda_{1}^{\prime}, \cdots, \lambda_{m}^{\prime}\right)$ 对应到同一向量, 令 $\left(\mu_{1}, \cdots, \mu_{m}\right)=$ $\left(\lambda_{1}-\lambda_{1}^{\prime}, \cdots, \lambda_{m}-\lambda_{m}^{\prime}\right)$ 即可.

由 (1) 知: 对 $1 \leq j \leq n$, 有 $\sum_{i=1}^{m} \mu_{i} \epsilon_{i, j}=0$, 进而

$$
\begin{aligned}
& \sum_{j=1}^{n}\left(a_{j} \cdot \sum_{i=1}^{m} \mu_{i} \epsilon_{i, j}\right)=0 \\
& \Rightarrow \sum_{i=1}^{m}\left(\mu_{i} \cdot \sum_{j=1}^{n} \epsilon_{i, j} \cdot a_{j}\right)=0 \\
& \Rightarrow \sum_{i=1}^{m} \mu_{i} \cdot m^{i}=0
\end{aligned}
$$

取最小的 $t$, 使 $\mu_{t} \neq 0$, 则 $\sum_{i=1}^{m} \mu_{i} m^{i} \equiv \mu_{t} m^{t} \not \equiv 0\left(\bmod m^{t+1}\right)$, 矛盾.

故反证法不成立, 原题得证.

评注 本题是中等难度的加性组合题, 分两部分: 一是不能对 $m, m^{2}, \cdots, m^{m}$配上 $[-m+1, m-1]$ 中的不全 0 的系数使之和为 0 , 二是对 $\overrightarrow{v_{1}}, \cdots, \overrightarrow{v_{m}}$ 配上合适的系数使之和为 0 . 两部分分别都是经典问题, 但合在一起就比较有趣了, 需要选手寻找中间的桥梁, 这与 2021 年集训队测试第 1 天第 2 题比较像. 本题从形式上看比较像一个线性代数题, 可能会去尝试线性空间, 但最后发现并不需要线性空间, 而且 $\overrightarrow{v_{i}}$ 中每项均为 0 或 1 (而不是一般的与 $m$ 互素) 非常重要.

