数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2020 网络空间数学竞赛试题解答与评析 

李金珉 肖佳劼

(重庆巴蜀中学, 400013)

首届网络空间数学竞赛于 2020 年 7 月 13 日至 14 日通过网络竞赛的方式举行. 竞赛共分两天考试, 每天 5 小时考 4 道题目, 参赛者多为今年参加 IMO 的各国国家队. 中国六名国家队员参加了本次比赛, 并取得了不错的成绩.

这次竞赛虽然声称难度接近 IMO, 可作为 IMO 的赛前模拟, 但笔者认为难度并不够. 总共 8 个题中, $1,2,3,5,6$ 是比较容易的题, 属于高中联赛中偏简单的难度. 7,8 是中档题, 与 $\mathrm{CMO}$ 中档题难度相当. 只有第 4 题属于比较困难的问题.

下面提供对这次比赛题目的解答与评注. 欢迎读者批评指正.

## I. 试 题

1. 在一个 $n \times n$ 的方格板上, 主对角线是指沿左上角至右下角的对角线上的 $n$ 个单位方格. 现希望将若干个 $\square$ 形状的骨牌放置在这方格板上, 使得每个骨牌恰好覆盖三个单位方格, 骨牌可以旋转. 要求每个主对角线上的方格均未被覆盖, 每个非主对角线上的方格恰好被覆盖一次. 问对怎样的整数 $n \geq 2$ 可以做到上述覆盖?
2. 设 $f(x)=3 x^{2}+1$. 证明: 对任意正整数 $n$, 乘积

$$
f(1) \cdot f(2) \cdots \cdots f(n)
$$

至多有 $n$ 个不同素因子.

3. 在 $\triangle A B C$ 中, $A B>B C . D$ 是线段 $B C$ 上的动点, 点 $E$ 在 $\triangle A B C$ 外接圆上, 满足 $E$ 与 $A$ 在 $B C$ 的异侧, 且 $\angle B A E=\angle D A C$. 设 $I$ 为 $\triangle A B D$ 的内心, $J$ 为 $\triangle A C E$ 的内心. 证明: 直线 $I J$ 经过一个不依赖于 $D$ 的定点.[^0]
4. 设 $n$ 为正奇数, $n \times n$ 的方格棋盘上的某些方格被染成绿色, 国王只能在绿格中行走. 它每步可从一个绿格走到与这个绿格有公共点的另一个绿格. 若国王可以从任一绿格经有限步走到另一绿格. 证明: 国王可用不超过 $\frac{n^{2}-1}{2}$ 步从任一绿格走到另一绿格.
5. 黑板上写了 2020 个正整数. 每过一分钟, 祖鸣擦去黑板上的两个数, 并写上这两个数的和、差、积、商之一. 例如: 若祖鸣擦去数 6 和 3 , 则他可以写下集合

$$
\{6+3,6-3,3-6,6 \times 3,6 \div 3,3 \div 6\}=\left\{9,3,-3,18,2, \frac{1}{2}\right\}
$$

中的任意一个数. 经过 2019 分钟后, 祖鸣在黑板上写下单独一个数 -2020 .

证明: 祖鸣也可以用同样的初始 2020 个数, 在同样的规则下最后写下单独一个数 2020 .

6. 求所有的整数 $n \geq 3$, 使得下述命题成立: 若 $\mathcal{P}$ 是一个凸 $n$ 边形, 满足有 $n-1$ 条边长度相同, $n-1$ 个内角大小相同, 则 $\mathcal{P}$ 是一个正 $n$ 边形.
7. 将一个 $n \times n$ 方格纸的 $n^{2}$ 个小方格每一个染成黑色或白色. 记 $a_{i}$ 是第 $i$ 行中白色方格个数, $b_{i}$ 是第 $i$ 列中黑色方格个数. 在所有染色方式下, 求 $\sum_{i=1}^{n} a_{i} b_{i}$的最大取值.
8. 已知正实数无穷序列 $a_{1}, a_{2}, \cdots$, 满足对任意正整数 $n$, 都有

$$
\frac{a_{1}+a_{2}+\cdots+a_{n}}{n} \geq \sqrt{\frac{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n+1}^{2}}{n+1}} .
$$

证明: 序列 $a_{1}, a_{2}, \cdots$ 是常数序列.

## II . 解答与评注

1. 在一个 $n \times n$ 的方格板上, 主对角线是指沿左上角至右下角的对角线上的 $n$ 个单位方格. 现希望将若干个 $\square$ 形状的骨牌放置在这方格板上, 使得每个骨牌恰好覆盖三个单位方格, 骨牌可以旋转. 要求每个主对角线上的方格均未被覆盖, 每个非主对角线上的方格恰好被覆盖一次. 问对怎样的整数 $n \geq 2$ 可以做到上述覆盖?

解 首先, 非主对角线上的方格共有 $n^{2}-n$ 个. 若能恰好覆盖, 必须 $3 \mid n^{2}-n$,即 $n \equiv 0,1(\bmod 3)$.

下面考虑 $n$ 较小的情形. 由于主对角线上下的方格不可能被骨牌同时覆盖,
故只考虑主对角线下方的 $\frac{n^{2}-n}{2}$ 个方格能否被骨牌覆盖.


$n=3$ 时, 可以.

$n=4$ 时, 要覆盖格 $A$, 只有一种放法, 这样下面三个方格无法覆盖, 故不可以.

$n=6$ 时, 同样要覆盖格 $A, B$ 放法必唯一. 剩下 $3 \times 3$的方格要被 3 块骨牌覆盖, 但每个角只能被一块骨牌覆盖,故也不可以.

$n=7,10,12$ 时, 都可以. 构造如下:



$\mathrm{n}=7$



$\mathrm{n}=10$



$\mathrm{n}=12$

下证: 若命题对 $n$ 成立, 则对 $n+6$ 也成立, $n \geq 3$.

只需考虑主对角线下的最后六行, 形如



右边的阶梯图形即为 $n=7$ 的结论, 能被骨牌覆盖. 而对左边 $6 \times(n-1)$ 的长方形方格表, 由于 $n-1 \geq 2$, 必存在非负整数 $a, b$, 使得 $n-1=2 a+3 b$. 只需将 $a$个 $6 \times 2$ 与 $b$ 个 $6 \times 3$ 如下图顺次相接即可.

综上, 所求的 $n$ 为满足 $n \equiv 0,1(\bmod 3)$ 且 $n \neq 4,6, n \geq 3$ 的所有数.

评注归纳构造不难想到, 一些相对较大的奠基如 $n=10,12$ 需要花一些时间。

2. 设 $f(x)=3 x^{2}+1$. 证明: 对任意正整数 $n$, 乘积

$$
f(1) \cdot f(2) \cdots \cdots f(n)
$$

至多有 $n$ 个不同素因子.

证明 对 $n$ 用归纳法.

当 $n=1$ 时, $f(n)=4$, 只有一个素因子 2 , 故命题成立.

下设命题对 $n-1(n \geq 2)$ 成立. 考虑满足 $p \mid f(n)$, 且 $p \nmid f(1) f(2) \cdots f(n-1)$的素数 $p$. 显然 $p \neq n$.

若 $p<n$, 则 $1 \leq n-p<n$, 且 $f(n-p) \equiv f(n) \equiv 0(\bmod p)$. 故 $p \mid$ $f(1) f(2) \cdots f(n-1)$, 矛盾!

若 $n<p<2 n$, 则 $1 \leq p-n<n$, 且 $f(p-n) \equiv f(n) \equiv 0(\bmod p)$, 也矛盾!

于是必有 $p \geq 2 n>\sqrt{f(n)}$, 故这样的 $p$ 至多只有一个, 再由归纳假设, 即知命题对 $n$ 也成立.

评注 本题是个简单题, 归纳法不难想到. $\bmod p$ 平移也是常用技巧.

3. 在 $\triangle A B C$ 中, $A B>B C . D$ 是线段 $B C$ 上的动点, 点 $E$ 在 $\triangle A B C$ 外接圆上, 满足 $E$ 与 $A$ 在 $B C$ 的异侧, 且 $\angle B A E=\angle D A C$. 设 $I$ 为 $\triangle A B D$ 的内心, $J$ 为 $\triangle A C E$ 的内心. 证明: 直线 $I J$ 经过一个不依赖于 $D$ 的定点.

证明 设 $\triangle A B C$ 的内心为 $P$. 延长 $B P$ 交 $\triangle A B C$ 外接圆于 $Y$, 则 $Y$ 为 $\triangle A P C$ 外接圆圆心 $($ 这个外接圆记为 $\odot Y)$.



由于 $A B>B C, \odot Y$ 必与 $B C$ 延长线交于点 $T$, 且 $B A=B T$. 即 $T$ 为定点.
又 $Y$ 在 $\triangle A E C$ 外接圆上, 且为弧 $\overparen{\mathrm{AC}}$ 中点. 故 $\triangle A E C$ 内心 $J$ 在线段 $Y E$ 上. 又 $A B>B C$, 故 $J, A$ 在 $B C$ 同侧, 于是射线 $T J$ 必与线段 $B Y$ 相交. 设交点为 $I^{\prime}$,则 $\triangle B I^{\prime} A \cong \triangle B I^{\prime} T$, 故

$$
\angle B A I^{\prime}=\angle B T I^{\prime}=\angle C T J=\angle C A J
$$

又

$$
\angle B A E=\angle D A C \Rightarrow \angle B A D=\angle E A C \Rightarrow \angle B A I=\angle C A J .
$$

而 $I, I^{\prime}$ 均在线段 $B Y$ 上, 故 $I, I^{\prime}$ 为同一个点. 于是 $I J$ 必过不依赖于 $D$ 的定点 $T . T$ 在 $B C$ 延长线上, $B T=B A$.

评注 首先需猜出这个定点. 当 $D$ 离 $B$ 很近时, $I$ 也离 $B$ 很近. 此时 $E$ 离 $C$很近, $J$ 离 $C$ 也很近. 故 $I J$ 能无限接近于 $B C$. 这个定点应在 $B C$ 上. 然后精细作图观察不难发现 $A, P, J, C, T$ 均共圆, 之后的推导是简单的.

4. 设 $n$ 为正奇数, $n \times n$ 的方格棋盘上的某些方格被染成绿色, 国王只能在绿格中行走. 它每步可从一个绿格走到与这个绿格有公共点的另一个绿格. 若国王可以从任一绿格经有限步走到另一绿格. 证明: 国王可用不超过 $\frac{n^{2}-1}{2}$ 步从任一绿格走到另一绿格.

证明 若两个格子有公共点, 则称它们相邻. 如果格子序列 $A_{0}, A_{1}, \cdots, A_{m}$满足 $A_{i}$ 只与 $A_{i-1}$ 和 $A_{i+1}$ 相邻 $(1 \leq i \leq m-1), A_{0}$ 只与 $A_{1}$ 相邻, $A_{m}$ 只与 $A_{m-1}$相邻, 称此格子序列为一条链. 它的长度为 $m$, 包含格子数为 $m+1$. 题目即要证明 $n \times n$ 棋盘上的每条链长度均 $\leq \frac{n^{2}-1}{2}$. 这是因为每两个绿格之间的最短路径必然是一条链.

下面证明加强命题: 对 $n \times n$ 棋盘上任意若干条链. 如果不同链上的格子都互不相邻. 那么这些链的总长度不超过 $\frac{n^{2}-1}{2}$.

这里可设每条链长度均 $\geq 1$, 这样可排除单个格子构成的链.

若记所有链的集合为 $L=\left\{l_{1}, l_{2}, \cdots, l_{n}\right\}$, 则链的条数为 $|L|$. 再记所有链包含的格子集合为 $\bar{L}$, 则需要证明:

$$
|\bar{L}| \leq \frac{n^{2}-1}{2}+|L|
$$

用归纳法. 当 $n=1$ 时, $|\bar{L}| \leq 1 \leq|L|$. 显然成立.

当 $n=3$ 时:

(1) 若 $3 \times 3$ 棋盘有一行或一列全在 $\bar{L}$ 中, 则它们必在同一条链上, 由对称性只需考虑两种情况:

(1) 中间一行在 $\bar{L}$ 中, 那么其他格子都不能在 $\bar{L}$ 中, 故 $|\bar{L}|=3 \leq \frac{3^{2}-1}{2}$.

(2) 第一行在 $\bar{L}$ 中, 那么第二行格子都不能在 $\bar{L}$ 中.

若 $|L|=1$, 则第一行为唯一一条链, $|L|=3 \leq \frac{3^{2}-1}{2}$.

若 $|L| \geq 2$, 则 $|\bar{L}| \leq 6 \leq \frac{3^{2}-1}{2}+|L|$, 均成立.

(2) 若每行每列均不全在 $\bar{L}$ 中, 则 $|\bar{L}| \leq 6$. 若 $|L| \geq 2$, 由(1)中讨论知 (*) 成立,于是只需考虑 $|L|=1$, 即只有一条链的情况.

若 $|\bar{L}| \leq 5$, 则 $|\bar{L}| \leq \frac{3^{2}-1}{2}+|L|$.

若 $|\bar{L}|=6$, 则每行每列恰有两个格子. 若每行两个格子都不相邻, 则这六个格子不构成一条链. 若某行两个格子相邻, 则与这行相邻的一行中与那两个格子相邻的两个格子都不在链中, 不然会与链的定义矛盾. 于是 $|L|=1$ 时, $|\bar{L}|<6$,故 $(*)$ 对 $n=3$ 成立.


下证若 $(*)$ 对 $n$ 成立, 则对 $n+4$ 也成立.

把 $(n+4) \times(n+4)$ 的棋盘分为两部分, 中心的 $n \times n$ 个格子记为 $T$. 最外面两层格子记为 $M$, 则

$$
|M|=(n+4)^{2}-n^{2}=8 n+16 \text {. }
$$

于是 $L$ 中每条链都在 $M, T$ 中交替出现(也可能完整包含在 $M$ 或 $T$ 中). 在 $M$或 $T$ 中连续出现的每段均为 $M$ 或 $T$ 中的链.



把 $M$ 中所有这些段的集合记为 $L_{M}, T$ 中所有这些段集合记为 $L_{T}$, 则 $L_{T}, L_{M}$ 中各自不同链上任意两个格子都不相邻. 于是由归纳假设,

$$
\left|\overline{L_{T}}\right| \leq \frac{n^{2}-1}{2}+\left|L_{T}\right| .
$$

由 $|\bar{L}|=\left|\overline{L_{T}}\right|+\left|\overline{L_{M}}\right|$, 还需估计 $\left|\overline{L_{M}}\right|$.

对棋盘最外面一层的格子 $u$. 若 $u$ 在 $\overline{L_{M}}$ 中, $u$ 不在角上, 且与 $u$ 有公共边的棋盘最外面第二层的格子 $v$ 也在 $\overline{L_{M}}$ 中, 则称 $u$ 为坏格. 由链的最短性可知每个坏格必为 $L_{M}$ 中某条链的端点, 且也为 $L$ 中某条链的端点.



将 $L_{M}$ 中的链拆分为三部分.

$$
L_{M}=A \cup B \cup C,
$$

其中 $A$ 中链无坏格, $B$ 中链恰含一个坏格, $C$ 中链恰含两个坏格, 则 $C$ 中每条链均为 $L$ 中的链, 即 $C \subset L$.

对 $L$ 中除 $C$ 外的链, 它要么含在 $T$ 中, 要么在 $T$ 和 $M$ 中交替出现, 即为

$$
\left(l_{A} \text { 或 } l_{B} \text { 或 } \emptyset\right)-l_{T}-l_{A}-l_{T}-l_{A}-\cdots-l_{A}-l_{T}-\left(l_{A} \text { 或 } l_{B} \text { 或 } \emptyset\right)
$$

的形式. 其中 $l_{A}, l_{B}, l_{T}$ 分别表示 $A, B, T$ 中某条链. $l_{A}, l_{B}, l_{T}$ 均可作为 $L$ 中两链的开头或结尾, 但中间连接两段 $l_{T}$ 的 $L_{M}$ 中的链只能在 $A$ 中, 不能在 $B$ 或 $C$ 中. 这样把中间的每段 $l_{A}$ 与它之后的一段 $l_{T}$ 抵消. 不改变 $L$ 中链的条数. 即 $\left|L_{T}\right|-|A|$ 不超过 $L$ 中除 $C$ 外链的条数. 于是

$$
\begin{aligned}
\left|L_{T}\right|-|A| \leq|L|-|C| & \Rightarrow\left|L_{T}\right| \leq|L|-|C|+|A| \\
& \Rightarrow\left|\overline{L_{T}}\right| \leq \frac{n^{2}-1}{2}+|L|-|C|+|A|
\end{aligned}
$$

要证 $(*)$, 只需证明

$$
\left|\overline{L_{M}}\right| \leq 4 n+8+|C|-|A|=\frac{|M|}{2}+|C|-|A| .
$$

将 $L_{M}$ 中所有链上的坏格均删去. 由于坏格只能作为链的端点, 且不存在只由坏格构成的链. 故剩下的格子仍构成一些链, 且条数不变. 把这些链的集合记为 $L_{M^{\prime}}$, 则

$$
\left|L_{M^{\prime}}\right|=\left|L_{M}\right|=|A|+|B|+|C|
$$

且

$$
\left|\overline{L_{M^{\prime}}}\right|=\left|\overline{L_{M}}\right|-|B|-2|C| \text {. }
$$

于是只需证明

$$
\left|\overline{L_{M^{\prime}}}\right|+|B|+2|C| \leq \frac{|M|}{2}+|C|-|A|,
$$

即

$$
\left|\overline{L_{M^{\prime}}}\right|+\left|L_{M^{\prime}}\right| \leq \frac{|M|}{2} .
$$

此时 $L_{M^{\prime}}$ 中的链均没有坏格.

先考虑四个角上 $2 \times 2$ 的情况, 它们至多只能包含 $\left|\overline{L_{M^{\prime}}}\right|$ 中两个格子.

(1) 若恰包含两个格子, 则只能为这个 $2 \times 2$ 的两条对角线之一. 若它为包含顶角的对角线, 则把它换为另一条对角线上的两个格子, 不影响 $\left|\overline{L_{M^{\prime}}}\right|$ 和 $\left|L_{M^{\prime}}\right|$的值.



(2) 若恰包含一个格子, 若这个格子在顶角格子所在的对角线上, 那么可把这个格子平移到另一条对角线上, 这样 $\left|\overline{L_{M^{\prime}}}\right|$ 不变, $\left|L_{M^{\prime}}\right|$ 不会减小.



于是, 总可假设四个角上 $2 \times 2$ 中 $\overline{L_{M^{\prime}}}$ 的格子都在不包含顶角的那条对角线上.

然后, 对于边上的格子, 如果它在里面一层, 则把它移到外面一层, $\left|\overline{L_{M^{\prime}}}\right|$ 不变, $\left|L_{M^{\prime}}\right|$ 也不会减小.


这样, 又可进一步假设 $\overline{L_{M^{\prime}}}$ 中格子全在棋盘的最外层.

最后如果棋盘最外层除了四个顶角外还有至少两个空的格子, 任取一个把它加入 $\overline{L_{M^{\prime}}}$ 后, $\left|\overline{L_{M^{\prime}}}\right|$ 增加 $1,\left|L_{M^{\prime}}\right|$ 不变或减少 $1 .\left|\overline{L_{M^{\prime}}}\right|+\left|L_{M^{\prime}}\right|$ 仍不会减少.



这样操作下去, 直到最外层除四个角外的格子只有一个空格. 此时

$$
\left|L_{M^{\prime}}\right|=1,\left|\overline{L_{M^{\prime}}}\right|=\frac{|M|}{2}-1 .
$$

由于在操作过程中 $\left|\overline{L_{M^{\prime}}}\right|+\left|L_{M^{\prime}}\right|$ 不会减少, 故一定有 $\left|\overline{L_{M^{\prime}}}\right|+\left|L_{M^{\prime}}\right| \leq \frac{|M|}{2}$.

至此, 加强命题证毕, 原命题也成立.

评注 本题是本次比赛的最难一题. 参赛选手仅一人得 5 分, 一人得 4 分(满分 7 分).

图论中的一个研究分支即为研究图的一些特殊子图或导出子图, 本题即为在图中找出导出子图为尽可能长的路.

求图的最长导出路径往往属于 NP-hard 问题. 即使对简单的 $n$ 维超立方体,也只在 $n \leq 8$ 时有精确的最大值. 另外还可进一步考虑图的多条导出路径的总长度. 这个想法正是本题证明过程中的加强命题.

本题证明的核心是注意到了路径在边界的“拐弯”情况. 它不能直角拐弯. 这样在边界附近的格子就不会太多. 这样就想到了对最外两层用归纳法, 之后就是一些技术性的处理细节。

有兴趣的读者可以考虑 $n$ 为偶数的情况 (不难). 以及 $n \times n \times n$ 的三维立方体的情况. 另外若国王只允许直走, 不允许斜走, 也可考虑相应的二维及三维情况.

5. 黑板上写了 2020 个正整数. 每过一分钟, 祖鸣擦去黑板上的两个数, 并写上这两个数的和、差、积、商之一. 例如: 若祖鸣擦去数 6 和 3 , 则他可以写下集合

$$
\{6+3,6-3,3-6,6 \times 3,6 \div 3,3 \div 6\}=\left\{9,3,-3,18,2, \frac{1}{2}\right\}
$$

中的任意一个数. 经过 2019 分钟后, 祖鸣在黑板上写下单独一个数 -2020 .

证明: 祖鸣也可以用同样的初始 2020 个数, 在同样的规则下最后写下单独一个数 2020 .

证明 对正整数 $n \geq 2$, 我们归纳证明如下命题:

若开始黑板上有 $n$ 个正整数, 祖鸣经过 $n-1$ 分钟后, 在黑板上写下单独一个数 $-m$, 其中 $m$ 为任意正整数, 那么他也可以用同样的初始 $n$ 个数, 在同样的规则下最后写下单独一个数 $m$.

当 $n=2$ 时, 设初始正整数为 $A$ 和 $B$. 要得到负整数 $-m$, 必进行减法操作.不妨设 $-m=A-B$, 则 $m$ 可由 $B-A$ 得到.

设 $2 \leq n \leq k$ 时, 上述命题成立, 则对 $n=k+1$, 分几种情况讨论

(1) 若最后一次操作为减法. 设 $-m=A-B$, 则 $m$ 可由 $B-A$ 得到.

(2) 若最后一次操作为乘法或除法. 设 $-m=A * B$. (* 为乘或除 ), 则 $A, B$中必有一个为负数, 设为 $C(C=A$ 或 $C=B)$. 那么 $C$ 必为开始的 $r(2 \leq r \leq k)$个数经历 $r-1$ 次操作得到. 由归纳假设知 $-C$ 也可由这 $r$ 个数经 $r-1$ 次操作得到. 这样, 将 $A * B$ 中的 $C$ 替换为 $-C$ 即可得到 $m$.

(3) 若最后一次操作为加法. 设 $-m=A+B$, 可不妨设 $A$ 为负数, 由 (2) 中同样分析可知能得到 $-A$, 则 $m$ 可由 $(-A)-B$ 得到.

综上可知加强命题成立, 于是原命题也成立

评注 本题是个简单题. 通过考虑较小的 $n$ 即可看出所有情况.

6. 求所有的整数 $n \geq 3$, 使得下述命题成立: 若 $\mathcal{P}$ 是一个凸 $n$ 边形, 满足有 $n-1$ 条边长度相同, $n-1$ 个内角大小相同, 则 $\mathcal{P}$ 是一个正 $n$ 边形.

解 设 $\mathcal{P}$ 为凸多边形 $P_{1} P_{2} \cdots P_{n}$ ，

$$
\angle P_{1} P_{2} P_{3}=\angle P_{2} P_{3} P_{4}=\cdots=\angle P_{n-2} P_{n-1} P_{n}=\angle P_{n-1} P_{n} P_{1}=\pi-\theta,
$$

则 $\theta \in\left(\frac{\pi}{n-1}, \frac{2 \pi}{n-1}\right)$.

将 $\mathcal{P}$ 放在复平面上, 使得 $P_{1}$ 为原点, $P_{2}$ 在实轴正方向上. 用 $z_{j}$ 表示 $P_{j}$ 所处位置 $(j=1,2, \cdots, n)$, 则对 $1 \leq j \leq n$, 有

$$
z_{j+1}-z_{j}=\left|P_{j} P_{j+1}\right| \cdot e^{i(j-1) \theta},
$$

其中 $P_{n+1}=P_{1}, z_{n+1}=z_{1}=0$. 由 $\mathcal{P}$ 的 $n-1$ 条边长相同. 设对 $1 \leq j \leq n, j \neq m$,有

$$
\left|p_{j} p_{j+1}\right|=x>0
$$

为定值, 另设

$$
\left|p_{m} p_{m+1}\right|=h
$$

则

$$
\begin{aligned}
0 & =\sum_{j=1}^{n}\left(z_{j+1}-z_{j}\right)=\sum_{j=1}^{n} x \cdot e^{i(j-1) \theta}+(h-x) e^{i(m-1) \theta} \\
& =x \cdot \frac{e^{i n \theta}-1}{e^{i \theta}-1}+(h-x) e^{i(m-1) \theta} \\
& =x \cdot e^{\frac{i(n-1) \theta}{2}} \cdot \frac{\sin \frac{n \theta}{2}}{\sin \frac{\theta}{2}}+(h-x) e^{i(m-1) \theta} .
\end{aligned}
$$

若 $\sin \frac{n \theta}{2}=0$, 由 $\theta \in\left(\frac{\pi}{n-1}, \frac{2 \pi}{n-1}\right)$, 必有 $\theta=\frac{2 \pi}{n}$. 此时 $h=x$, 故 $\mathcal{P}$ 的所有内角相等. 所有边长相同, 即 $\mathcal{P}$ 必为正 $n$ 边形.

若 $\sin \frac{n \theta}{2} \neq 0$, 此时 $h \neq x$, 于是

故

$$
e^{i \theta\left(\frac{n-1}{2}-(m-1)\right)}=\frac{x-h}{x} \cdot \frac{\sin \theta}{\sin \frac{n \theta}{2}} \in \mathbb{R},
$$

$$
\left(\frac{n+1}{2}-m\right) \theta=k \pi,(k \in \mathbb{Z}) \text {. }
$$

当 $n$ 为偶数时, $\frac{n+1}{2}-m \neq 0$, 故 $k \neq 0$, 于是

矛盾.

$$
\pi \leq|k \pi|=\left|\frac{n+1}{2}-m\right| \cdot|\theta|<\frac{n-1}{2} \cdot \frac{2 \pi}{n-1}=\pi
$$

这说明当 $n$ 为偶数时, $\mathcal{P}$ 必为正多边形.

当 $n$ 为奇数时, 由偶数时的情况. 若 $k \neq 0, \mathcal{P}$ 仍必为正多边形, 故应检验 $k=0$ 的情况. 此时必有 $m=\frac{n+1}{2}$, 于是

得

$$
x \cdot \frac{\sin \frac{n \theta}{2}}{\sin \frac{\theta}{2}}+(h-x)=0
$$

$$
h=x \cdot\left(1-\frac{\sin \frac{n \theta}{2}}{\sin \frac{\theta}{2}}\right)
$$

可令 $\theta=\frac{2 \pi}{n}+\epsilon, \epsilon$ 为充分小的正数, 则 $\theta \in\left(\frac{\pi}{n-1}, \frac{2 \pi}{n-1}\right)$. 又

$$
\sin \frac{\theta}{2}=\sin \left(\frac{\pi}{n}+\frac{\epsilon}{2}\right)>0, \sin \frac{n \theta}{2}=\sin \left(\pi+\frac{n \epsilon}{2}\right)<0
$$

当 $\epsilon$ 充分小时, 有

$$
h=x \cdot\left(1-\frac{\sin \frac{n \theta}{2}}{\sin \frac{\theta}{2}}\right)>x
$$

此时 $\mathcal{P}$ 的 $n-1$ 个内角相等, 但与另一个内角不相等, $n-1$ 条边长相同, 但与另一条边长不相同. $\mathcal{P}$ 不是正多边形.
综上所述, 满足条件的 $n$ 为所有大于 3 的偶数.

评注 本题方法实质上是把所有边的向量求和, 这是一个经典的方法. 可参考 IMO 1990 年的最后一题, 以及 2007 年集训队测验的第一题.

7. 将一个 $n \times n$ 方格纸的 $n^{2}$ 个小方格每一个染成黑色或白色. 记 $a_{i}$ 是第 $i$ 行中白色方格个数, $b_{i}$ 是第 $i$ 列中黑色方格个数. 在所有染色方式下, 求 $\sum_{i=1}^{n} a_{i} b_{i}$的最大取值。

解 记 $S_{n}=\sum_{i=1}^{n} a_{i} b_{i}$. 若同时交换第 $i$ 行和第 $j$ 行, 以及第 $i$ 列和第 $j$ 列. 显然 $S_{n}$ 的值不变. 故不妨设 $a_{1} \geq a_{2} \geq \cdots \geq a_{n}$.

考虑这样的染法: 第 $i$ 行最右边的 $a_{i}$ 个方格染成白色, 其余染成黑色.

设第 $i$ 列有 $b_{i}^{\prime}$ 个黑格, 并记 $S_{n}^{\prime}=\sum_{i=1}^{n} a_{i} b_{i}^{\prime}$.

由于白色方格被尽量靠右, 故前 $k$ 列的黑格个数

$$
b_{1}^{\prime}+b_{2}^{\prime}+\cdots+b_{k}^{\prime} \geq b_{1}+b_{2}+\cdots+b_{k}(1 \leq k \leq n)
$$

由 Abel 变换可知 $S_{n}^{\prime} \geq S_{n}$. 于是要求 $S_{n}$ 的最大值, 只需考虑每行白格均在最右侧, 且个数递减的染法即可.

下面用归纳法证明

$$
\max S_{n}=\frac{(n-1) n(n+1)}{3}
$$

$n=1$ 时, $S_{n}=1 \cdot 0=0$, 显然成立.

设 $n$ 时成立, 当 $n+1$ 时, 由行列对称性可设第一行第一列的格子 $(1,1)$ 染成白色, 且第 1 列有 $t$ 个白格, 则它们为 $(1,1),(2,1), \cdots,(t, 1), 1 \leq t \leq n+1$.考虑去掉第一行第一列得到的 $n \times n$ 方格表, 设它第 $i$ 行有 $a_{i}^{\prime}$ 个白格, 第 $i$ 列有 $b_{i}^{\prime}$ 个黑格, 则

$$
\begin{gathered}
b_{i}^{\prime}=b_{i+1}, \quad 1 \leq i \leq n, \\
a_{i}^{\prime}=\left\{\begin{array}{l}
a_{i+1}-1, \quad 1 \leq i \leq t-1 \\
a_{i+1}, \quad t \leq i \leq n
\end{array} .\right.
\end{gathered}
$$

由归纳假设

$$
S_{n}^{\prime}=\sum_{i=1}^{n} a_{i}^{\prime} b_{i}^{\prime} \leq \frac{(n-1) n(n+1)}{3} .
$$

又 $a_{1}=n+1, b_{1}=n+1-t$, 于是

$$
S_{n+1}=a_{1} b_{1}+\sum_{i=2}^{n+1} a_{i} b_{i}=a_{1} b_{1}+\sum_{i=2}^{t}\left(a_{i-1}^{\prime}+1\right) b_{i-1}^{\prime}+\sum_{i=t+1}^{n+1} a_{i-1}^{\prime} b_{i-1}^{\prime}
$$

$$
\begin{aligned}
& =a_{1} b_{1}+\sum_{i=2}^{t} b_{i}+\sum_{i=1}^{n} a_{i}^{\prime} b_{i}^{\prime} \\
& \leq(n+1)(n+1-t)+(t-1)(n+1)+\frac{(n-1) n(n+1)}{3} \\
& =(n+1) n+\frac{(n-1) n(n+1)}{3}=\frac{n(n+1)(n+2)}{3} .
\end{aligned}
$$

且若将第 $i$ 行的最右边 $n-i+1$ 个格子染成白色, 其余染成黑色, 则第 $i$ 列有 $n-i$ 个黑格. 此时,

$$
S_{n}=\sum_{i=1}^{n}(n-i+1)(n-i)=\sum_{j=1}^{n} j(j-1)=\frac{(n-1) n(n+1)}{3}
$$

故最大值可以取到.

综上所述, $\sum_{i=1}^{n} a_{i} b_{i}$ 的最大值为 $\frac{(n-1) n(n+1)}{3}$.

评注 通过交换行列简化图形是处理方格表极值问题的常用方法. 将行排序后想到列也应排序, 这样又可进一步简化问题, 之后的归纳法是容易处理的.

8. 已知正实数无穷序列 $a_{1}, a_{2}, \cdots$, 满足对任意正整数 $n$, 都有

$$
\frac{a_{1}+a_{2}+\cdots+a_{n}}{n} \geq \sqrt{\frac{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n+1}^{2}}{n+1}}
$$

证明: 序列 $a_{1}, a_{2}, \cdots$ 是常数序列.

证明 令

$$
A_{n}=\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}, Q_{n}=\sqrt{\frac{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}}{n}},
$$

则 $Q_{n} \geq A_{n} \geq Q_{n+1}$.

固定整数 $k \geq 2$, 对任意整数 $n \geq k$, 有

$$
\begin{aligned}
Q_{n}^{2}-Q_{n+1}^{2} & \geq Q_{n}^{2}-A_{n}^{2}=\frac{1}{n^{2}} \sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2} \\
& \geq \frac{1}{n^{2}} \sum_{j=k}^{n}\left[\left(a_{k}-a_{j}\right)^{2}+\left(a_{j}-a_{1}\right)^{2}\right] \\
& \geq \frac{1}{n^{2}} \sum_{j=k}^{n} \frac{1}{2}\left[\left(a_{k}-a_{j}\right)+\left(a_{j}-a_{1}\right)\right]^{2} \\
& =\frac{n-k+1}{2 n^{2}}\left(a_{k}-a_{1}\right)^{2} .
\end{aligned}
$$

于是对任意整数 $N \geq k$,

$$
Q_{k}^{2} \geq \sum_{n=k}^{N}\left(Q_{n}^{2}-Q_{n+1}^{2}\right) \geq\left(a_{k}-a_{1}\right)^{2} \sum_{n=k}^{N} \frac{n-k+1}{2 n^{2}} .
$$

当 $N \rightarrow+\infty$ 时,

$$
\sum_{n=k}^{N} \frac{n-k+1}{2 n^{2}} \rightarrow+\infty
$$

而 $a_{k}$ 为定值, 故必有 $\left(a_{k}-a_{1}\right)^{2}=0$. 由 $k$ 的任意性即知所有 $a_{k}$ 都相等.

评注 $(*)$ 式是关于算术平均和平方平均关系的常用等式, 然后若 $a_{k}$ 不全相等, 可从中挑出足够多“主项”, 使得这些项积累起来能任意大.

本文由第二作者执笔, 主要根据第一作者在考场上的解答, 对部分较长的过程作了简化, 并重写了一部分的证明.

最后感谢冷岗松教授的大力支持和胡珏伟博士的辛勤编辑.


[^0]:    修订日期: 2020-08-08.

