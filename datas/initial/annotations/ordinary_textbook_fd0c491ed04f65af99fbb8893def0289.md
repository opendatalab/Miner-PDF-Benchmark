# 第三届国际大都市竞赛数学试题评析 

罗振华 ${ }^{1}$ 羊明亮 ${ }^{2}$

(1. 上海四季教育, 200070；2. 浙江省乐清市知临中学, 325600)

第三届国际大都市竞赛 (IOM) 于 2018 年 9 月 2 日至 9 月 7 日在莫斯科举行, 此次比赛邀请了 30 多个国际知名的大都市参赛, 其中中国仅上海参赛. 比赛共分四个学科: 数学、物理、化学、计算机. 其中数学比赛采用标准 IMO 赛制,分两天, 每天四个半小时三道题, 每题 7 分.

比赛分金银铜牌, 金牌线是 36 分, 银牌线是 22 分, 铜牌线是 15 分. 全场唯一的满分是莫斯科选手 Oleg Smirnov, 中国上海的两名选手分别是蒋天泽 (上海中学) 与金及凯 (华东师范大学第二附属中学), 两名选手均是 37 分排名并列第二并获得金牌.

综合往年的 IOM 试题来看, 它的难度分配是一、四题比较简单 (部分题目是初中竞赛难度), 二、五题中等难度 (联赛二试难度), 三、六题比较困难 (冬令营最后一题难度). 题目风格是典型的俄罗斯竞赛风格, 组合与几何的题目质量很高.

## I. 试 题

1. 在实数范围内解下述方程组

$$
\left\{\begin{array}{l}
(x-1)(y-1)(z-1)=x y z-1 \\
(x-2)(y-2)(z-2)=x y z-2
\end{array} .\right.
$$

2. 已知凸四边形 $A B C D$ 外切于圆 $\omega, P Q$ 为圆 $\omega$ 的垂直于 $A C$ 的直径. 设直线 $B P$ 与 $D Q$ 相交于 $X$, 直线 $B Q$ 与 $D P$ 相交于 $Y$. 证明: 点 $X$ 和 $Y$ 均在直线 $A C$ 上.
3. 设 $k$ 为正整数, 且满足 $p=8 k+5$ 为素数. 整数 $r_{1}, r_{2}, \cdots, r_{2 k+1}$ 满足收稿日期: 2018-09-20； 修订日期: 2018-10-21.
$0, r_{1}^{4}, r_{2}^{4}, \cdots, r_{2 k+1}^{4}$ 除以 $p$ 所得的余数两两不同. 证明:

$$
\prod_{1 \leq i<j \leq 2 k+1}\left(r_{i}^{4}+r_{j}^{4}\right) \equiv(-1)^{\frac{k(k+1)}{2}} \quad(\bmod p)
$$

4. 已知 $k$ 是正整数, 且 $1=d_{0}<d_{1}<\cdots<d_{m}=4 k$ 为 $4 k$ 的所有正因数.证明: 存在 $i \in\{1,2, \cdots, m\}$, 使得 $d_{i}-d_{i-1}=2$.
5. Ann 和 Max 在一个 $100 \times 100$ 的棋盘上玩游戏. 首先, Ann 在每个格子内填写一个 1 到 10000 的整数, 且每个数只能使用一次. 接下来 Max 在棋盘最左边的一列挑选一个格子并在其中放入一枚硬币, 他为了让硬币到达棋盘最右边的一列会进行若干步操作. 每次操作硬币会被移到与原方格有一条边或一个顶点相邻的格子, 每到一个格子 (包括初始位置), Max 需向 Ann 支付与格子中所填数等额的硬币. Max 希望支付尽可能少的钱, 而 Ann 希望适当填数来最大化自己的收益. 如果两人都采取最佳策略, 那么 Max 需要向 Ann 支付多少枚硬币?
6. $\triangle A B C$ 的内切圆与边 $B C, A C$ 分别相切于点 $D, E$. 设 $P$ 为内切圆的劣弧 $D E$ 上一点, 且满足 $\angle A P E=\angle D P B$. 线段 $A P, B P$ 分别交线段 $D E$ 于点 $K, L$. 求证: $2 K L=D E$.

## II. 解 答

以下各题的解答均翻译整理自官方公布的标准答案, 其中第三题与第六题收录了乐清市知临中学的胡子晗同学与郑立瑜同学的解法.

1. 在实数范围内解下述方程组

$$
\left\{\begin{array}{l}
(x-1)(y-1)(z-1)=x y z-1 \\
(x-2)(y-2)(z-2)=x y z-2
\end{array} .\right.
$$

解 方程组可以化简为

$$
\left\{\begin{array}{l}
x y+y z+z x=x+y+z \\
x y+y z+z x=2(x+y+z)-3
\end{array},\right.
$$

可以解得

$$
\left\{\begin{array}{l}
x+y+z=3 \\
x y+y z+z x=3
\end{array} .\right.
$$

故

$$
(x+y+z)^{2}=x y+y z+z x
$$

配方可得

$$
(x-y)^{2}+(y-z)^{2}+(z-x)^{2}=0 .
$$

所以 $x=y=z$, 从而

$$
x=y=z=1 \text {. }
$$

代入原方程, 满足条件. 所以方程的解为 $\left\{\begin{array}{l}x=1 \\ y=1 \\ z=1\end{array}\right.$.

评注 这是一个简单的方程问题, 在得到 $x+y+z=3$ 与 $x y+y z+z x=3$后结合两者之间的不等关系可以立即得到结论. 像这种变元个数多于方程个数的问题, 一般都可以考虑使用不等式, 利用不等式的取等条件得到方程的解.

2. 已知凸四边形 $A B C D$ 外切于圆 $\omega, P Q$ 为圆 $\omega$ 的垂直于 $A C$ 的直径. 设直线 $B P$ 与 $D Q$ 相交于 $X$, 直线 $B Q$ 与 $D P$ 相交于 $Y$. 证明: 点 $X$ 和 $Y$ 均在直线 $A C$ 上.

证明 由于点 $P$ 和 $Q$ 地位对等, 故不妨设 $P$ 在 $\triangle A C D$ 中, $Q$ 在 $\triangle A B C$ 中.

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-03.jpg?height=617&width=597&top_left_y=1630&top_left_x=752)

第一步, 我们证明点 $X$ 在 $A C$ 上.

记 $\triangle A B C$ 和 $\triangle A C D$ 的内切圆分别为 $\omega_{1}$ 和 $\omega_{2}$, 并记这两个内切圆分别与 $A C$ 切于 $X_{1}, X_{2}$. 下面我们证明 $B P$ 经过 $X_{1}, D Q$ 经过 $X_{2}$ 并且 $X_{1}=X_{2}$. 这样就说明 $X=X_{1}=X_{2}$, 且点 $X$ 在 $A C$ 上.
由三角形的切线长公式, 有

$$
\begin{aligned}
& A X_{1}=\frac{1}{2}(A B+A C-B C) \\
& A X_{2}=\frac{1}{2}(A C+A D-C D) .
\end{aligned}
$$

由于四边形 $A B C D$ 有内切圆, 故 $A B+C D=B C+A D$, 则有

$$
A X_{1}-A X_{2}=\frac{1}{2}(A B-B C-A D+C D)=0 .
$$

从而 $X_{1}=X_{2}$.

注意到直线 $B A$ 与 $B C$ 是两圆 $\omega$ 和 $\omega_{1}$ 的外公切线, 从而存在一个以 $B$ 为位似中心的位似变换, 把 $\omega$ 变为 $\omega_{1}$. 注意到 $X_{1}$ 关于 $\omega$ 的切线与 $P$ 关于 $\omega_{1}$ 的切线平行, 从而在上述位似变换下 $P$ 变为 $X_{1}$. 所以 $B, P, X_{1}$ 共线.

同理, $D, Q, X_{2}$ 共线.

这就证明了点 $X$ 在 $A C$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-04.jpg?height=596&width=774&top_left_y=1164&top_left_x=641)

第二步, 我们证明点 $Y$ 也在 $A C$ 上.

记 $\triangle A B C$ 的 $B$-旁切圆与 $\triangle A C D$ 的 $D$-旁切圆分别为 $\gamma_{1}$ 与 $\gamma_{2}$, 并记这两个旁切圆分别与 $A C$ 切于 $Y_{1}, Y_{2}$. 与第一步的证明类似, 我们证明 $B Q$ 经过 $Y_{1}$, $D P$ 经过 $Y_{2}$ 并且 $Y_{1}=Y_{2}$. 这样就说明 $Y=Y_{1}=Y_{2}$, 且点 $Y$ 在 $A C$ 上.

由三角形的切线长公式,

$$
\begin{aligned}
& C Y_{1}=\frac{1}{2}(A B+A C-B C), \\
& C Y_{2}=\frac{1}{2}(A C+A D-C D) .
\end{aligned}
$$

又由 $A B+C D=B C+A D$, 知 $C Y_{1}=C Y_{2}$, 从而 $Y_{1}=Y_{2}$.

可作一个以 $B$ 为位似中心的位似变换, 把 $\omega$ 变为 $\gamma_{1}$. 注意到 $Q$ 关于 $\omega$ 的切线与 $Y_{1}$ 关于 $\gamma_{1}$ 的切线平行. 故在此位似变换下, $Q$ 变为 $Y_{1}$, 所以 $B, Q, Y_{1}$ 共线.
同理, $D, P, Y_{2}$ 共线.

这就证明了点 $Y$ 在 $A C$ 上.

综上所述, 命题获证.

评注 这是一道图形优美且难度适中的几何题, 解答的核心在于把四边形的内切圆位似变换到三角形的内切圆或旁切圆, 利用内切圆或旁切圆的切点的性质导出结论. 本题使用位似变换的手法与一道早年内切圆相关的 IMO 试题类似。

3. 设 $k$ 为正整数, 且满足 $p=8 k+5$ 为素数. 整数 $r_{1}, r_{2}, \cdots, r_{2 k+1}$ 满足 $0, r_{1}^{4}, r_{2}^{4}, \cdots, r_{2 k+1}^{4}$ 除以 $p$ 所得的余数两两不同. 证明:

$$
\prod_{1 \leq i<j \leq 2 k+1}\left(r_{i}^{4}+r_{j}^{4}\right) \equiv(-1)^{\frac{k(k+1)}{2}}(\bmod p)
$$

证法一 取出模 $p$ 的原根 $g$. 由于 $p-1$ 是 4 的倍数, 可知模 $p$ 的 4 次剩余有 $2 k+1$ 个, 分别为 $1, g^{4}, g^{8}, \cdots, g^{8 k}$, 从而 $r_{1}^{4}, \cdots, r_{2 k+1}^{4}$ 在模 $p$ 意义下是上述 $2 k+1$ 个数的一个排列.

定义从 $\{0,1, \cdots, 2 k\}$ 到 $\{0,1, \cdots, 2 k\}$ 的映射 $f$ 为: 对任意 $j \in\{0,1, \cdots, 2 k\}$, $f(j)$ 为 $2 j$ 除以 $2 k+1$ 所得的余数.

由定义 $2 k+1 \mid 2 j-f(j)$, 故 $4(2 k+1) \mid 8 j-4 f(j)$, 即为 $p-1 \mid 8 j-4 f(j)$.由费马小定理可知

$$
g^{8 j} \equiv g^{4 f(j)} \quad(\bmod p), j=0,1, \cdots, 2 k .
$$

将所求式作变形

$$
\begin{aligned}
\prod_{1 \leq i<j \leq 2 k+1}\left(r_{i}^{4}+r_{j}^{4}\right) & \equiv \prod_{1 \leq i<j \leq 2 k+1} \frac{r_{j}^{8}-r_{i}^{8}}{r_{j}^{4}-r_{i}^{4}} \\
& \equiv \prod_{0 \leq i<j \leq 2 k} \frac{g^{8 j}-g^{8 i}}{g^{4 j}-g^{4 i}} \\
& \equiv \prod_{0 \leq i<j \leq 2 k} \frac{g^{4 f(j)}-g^{4 f(i)}}{g^{4 j}-g^{4 i}}(\bmod p) .
\end{aligned}
$$

而

$$
g^{4 f(j)}-g^{4 f(i)}= \pm\left(g^{4 \max (f(j), f(i))}-g^{4 \min (f(j), f(i))}\right)
$$

上式当 $f(j)>f(i)$ 时取正号, 当 $f(j)<f(i)$ 取负号.

当 $(i, j)$ 遍历 $0 \leq i<j \leq 2 k$ 的所有情形时, $(\min (f(j), f(i)), \max (f(j), f(i)))$
也遍历所有情形. 故

$$
\prod_{0 \leq i<j \leq 2 k} \frac{g^{4 f(j)}-g^{4 f(i)}}{g^{4 j}-g^{4 i}}=(-1)^{N}
$$

其中 $N$ 是满足 $i<j$ 且 $f(i)>f(j)$ 的 $(i, j)$ 的数目, 而上述情况发生当且仅当

$$
i=1,2, \cdots, k ; j=k+1, \cdots, k+i
$$

故

$$
N=1+2+\cdots+k=\frac{k(k+1)}{2} .
$$

所以结论成立.

证法二 (胡子晗) 因为 $p$ 是素数, 故存在模 $p$ 的原根, 记 $g$ 为其中一个原根.

对于 $p \mid x$, 有 $x^{4} \equiv 0(\bmod p)$,

对于 $p \nmid x$, 有 $(x, p)=1$, 存在 $1 \leq \alpha \leq p-1$, 使得 $x \equiv g^{\alpha}(\bmod p)$, 则 $x^{4} \equiv g^{4 \alpha}(\bmod p)$, 故 $x^{4}$ 模 $p$ 的取值仅有 $0, g^{4}, g^{8}, \cdots, g^{4(p-1)}$. 而

$$
g^{\alpha} \equiv 1 \quad(\bmod p) \Leftrightarrow p-1 \mid \alpha,
$$

故 $x^{4}$ 模 $p$ 的取值恰有 $0, g^{4}, g^{8}, \cdots, g^{8 k+4}$ 这 $2 k+2$ 个不同的值. 因此在模 $p$ 的意义下, $r_{1}^{4}, r_{2}^{4}, \cdots, r_{2 k+1}^{4}$ 恰为 $g^{4}, g^{8}, \cdots, g^{8 k+4}$ 的一个排列, 从而

$$
\begin{aligned}
\prod_{1 \leq i<j \leq 2 k+1}\left(r_{i}^{4}+r_{j}^{4}\right) & \equiv \prod_{1 \leq i<j \leq 2 k+1}\left(g^{4 i}+g^{4 j}\right) \\
& \equiv \prod_{i=1}^{2 k} g^{4 i(2 k+1-i)} \prod_{d=1}^{2 k}\left(g^{4 d}+1\right)^{2 k+1-d} \\
& \equiv \prod_{i=1}^{2 k} g^{4 i(2 k+1-i)} \prod_{d=1}^{k}\left(g^{4 d}+1\right)^{2 k+1-d}\left(g^{(2 k+1-d) \times 4}+1\right)^{d} \\
& \equiv g^{(p-1) \cdot \frac{2(k+1)(2 k+1)}{3}}\left(\prod_{d=1}^{k}\left(g^{4 d}+1\right)\right)^{2 k+1} \cdot \prod_{d=1}^{k} \frac{1}{g^{4 d^{2}}} \\
& \equiv g^{(p-1) \cdot \frac{k(k+1)}{2}}\left(\prod_{d=1}^{k}\left(g^{4 d}+1\right)\right)^{2 k+1} \\
& \equiv\left(\prod_{d=1}^{k}\left(g^{4 d}+1\right)\right)^{2 k+1}(\bmod p) .
\end{aligned}
$$

考虑 $\prod_{d=1}^{k}\left(g^{8 i}-1\right)$. 当 $2 \mid k$ 时, 有

$$
\prod_{i=1}^{k}\left(g^{8 i}-1\right) \equiv \prod_{i=1}^{\frac{k}{2}}\left(g^{8 i}-1\right) \cdot \prod_{j=\frac{k}{2}+1}^{k}\left(g^{8 j}-g^{8 k+4}\right)
$$

$$
\begin{aligned}
& \equiv \prod_{i=1}^{\frac{k}{2}}\left(g^{8 i}-1\right) \cdot \prod_{j=\frac{k}{2}+1}^{k}(-1) \cdot g^{8 j} \cdot \prod_{j=\frac{k}{2}+1}^{k}\left(g^{8(k-j)+4}-1\right) \\
& \equiv \prod_{i=1}^{k}\left(g^{4 i}-1\right) \cdot(-1)^{\frac{k}{2}} \cdot g^{\left(\frac{3 k}{2}+1\right) \frac{k}{2} \times 4} \quad(\bmod p) .
\end{aligned}
$$

故

$$
\begin{aligned}
\left(\prod_{i=1}^{k}\left(g^{8 i}-1\right)\right)^{2 k+1} & \equiv\left(\prod_{i=1}^{k}\left(g^{4 i}-1\right) \cdot(-1)^{\frac{k}{2}}\right)^{2 k+1} g^{\left(\frac{3 k}{2}+1\right) \frac{k}{2}(p-1)} \\
& \equiv\left(\prod_{i=1}^{k}\left(g^{4 i}-1\right)\right)^{2 k+1} \cdot(-1)^{\frac{k}{2}} \quad(\bmod p) .
\end{aligned}
$$

从而

$$
\left(\prod_{i=1}^{k}\left(g^{4 i}+1\right)\right)^{2 k+1} \equiv(-1)^{\frac{k}{2}} \quad(\bmod p)
$$

上面用到 $p \nmid \prod_{i=1}^{k}\left(g^{4 i}-1\right)$.

当 $2 \nmid k$ 时, 有

$$
\begin{aligned}
\prod_{i=1}^{k}\left(g^{8 i}-1\right) & \equiv \prod_{i=1}^{\frac{k-1}{2}}\left(g^{8 i}-1\right) \prod_{j=\frac{k+1}{2}}^{k}\left(g^{8 j}-g^{8 k+4}\right) \\
& \equiv \prod_{i=1}^{\frac{k-1}{2}}\left(g^{8 i}-1\right) \prod_{j=\frac{k+1}{2}}^{k}(-1) \cdot g^{8 j} \cdot \prod_{j=\frac{k+1}{2}}^{k}\left(g^{8(k-j)+4}-1\right) \\
& \equiv \prod_{i=1}^{k}\left(g^{4 i}-1\right) \cdot(-1)^{\frac{k+1}{2}} g^{4 \cdot \frac{k+1}{2} \cdot \frac{3 k+1}{2}}(\bmod p) .
\end{aligned}
$$

故

$$
\begin{aligned}
\left(\prod_{i=1}^{k}\left(g^{8 i}-1\right)\right)^{2 k+1} & \equiv\left(\prod_{i=1}^{k}\left(g^{4 i}-1\right) \cdot(-1)^{\frac{k+1}{2}}\right)^{2 k+1} \cdot g^{(p-1) \cdot \frac{k+1}{2} \cdot \frac{3 k+1}{2}} \\
& \equiv\left(\prod_{i=1}^{k}\left(g^{4 i}-1\right)\right)^{2 k+1} \cdot(-1)^{\frac{k+1}{2}}(\bmod p) .
\end{aligned}
$$

故

$$
\left(\prod_{i=1}^{k}\left(g^{4 i}+1\right)\right)^{2 k+1} \equiv(-1)^{\frac{k+1}{2}} \quad(\bmod p)
$$

上式也用到 $p \nmid \prod_{i=1}^{k}\left(g^{4 i}-1\right)$.

综上所述, 有

$$
\left(\prod_{i=1}^{k}\left(g^{4 i}-1\right)\right)^{2 k+1} \equiv(-1)^{\frac{k(k+1)}{2}} \quad(\bmod p)
$$

从而

$$
\prod_{1 \leq i<j \leq 2 k+1}\left(r_{i}^{4}+r_{j}^{4}\right) \equiv(-1)^{\frac{k(k+1)}{2}} \quad(\bmod p) .
$$

证毕!

评注 本题是一道有相当难度的数论题. 考虑用原根表示 $r_{i}$ 是很重要的想法, 这是后续式子化简的基础. 证法一十分巧妙, 用平方差公式把题中四次式变为了八次式除以四次式, 再用同余的性质整体消去了一个不为零的项, 对正负号的个数稍作计算就能得出结论. 证法二略微繁琐, 不过想法很基本, 主要是用配对和原根的性质不断化简, 再对 $k$ 的奇偶分类讨论一下就能证得结论.

4. 已知 $k$ 是正整数, 且 $1=d_{0}<d_{1}<\cdots<d_{m}=4 k$ 为 $4 k$ 的所有正因数.证明: 存在 $i \in\{1,2, \cdots, m\}$, 使得 $d_{i}-d_{i-1}=2$.

证明 假设结论不成立. 这意味着若 $d \mid 4 k$ 且 $d+2 \mid 4 k$, 则 $d+1 \mid 4 k$. 注意到若 $a \mid 4 k$ 且 $4 \nmid a$, 则 $2 a \mid 4 k$. 利用上述性质我们可以从 $(1,2)$ 开始, 找到无穷多对整数 $(a, a+1)$, 使得 $a$ 与 $a+1$ 都整除 $4 k$ 且 $a$ 与 $a+1$ 都不被 4 整除.

若 $(a, a+1)$ 满足 $a$ 与 $a+1$ 都整除 $4 k$ 且 4 既不整除 $a$ 也不整除 $a+1$, 那么 $2 a$ 与 $2 a+2$ 也都是 $4 k$ 的因数, 由假设知 $2 a+1$ 也是 $4 k$ 的约数. $2 a$ 与 $2 a+2$是相邻的偶数, 必有一个不是 4 的倍数. 这就说明 $(2 a, 2 a+1)$ 与 $(2 a+1,2 a+2)$中有一对是满足前述要求的.

这种可以操作一直进行下去, 这样就得到无穷多对整数, 且每次操作后整数对中的最小数都严格递增. 这就得到了 $4 k$ 的一个无穷的因子集合, 矛盾!

故假设不成立, 原命题获证.

评注 这是一道简单的数论题. 用反证法是比较自然的, 利用 $4 k$ 的因数的性质并结合反证法的假设可以不断得找到相邻的整数对都是 $4 k$ 的因数, 这种操作可以一直进行下去, 这就与 $4 k$ 的有限性矛盾了.

5. Ann 和 Max 在一个 $100 \times 100$ 的棋盘上玩游戏. 首先, Ann 在每个格子内填写一个 1 到 10000 的整数, 且每个数只能使用一次. 接下来 Max 在棋盘最左边的一列挑选一个格子并在其中放入一枚硬币, 他为了让硬币到达棋盘最右边的一列会进行若干步操作. 每次操作硬币会被移到与原方格有一条边或一个顶点相邻的格子, 每到一个格子 (包括初始位置), Max 需向 Ann 支付与格子中所填数等额的硬币. Max 希望支付尽可能少的钱, 而 Ann 希望适当填数来最大化
自己的收益. 如果两人都采取最佳策略, 那么 Max 需要向 Ann 支付多少枚硬币?

解答 答案是 500000 枚硬币.

下界 / Ann 的策略:

首先我们说明 Ann 至少可以拿到 500000 枚硬币. Ann 按下如图所示的方式在棋盘上填数.

| 1 | 200 | 201 | 400 | $\cdots$ | 9800 | 9801 | 10000 |
| ---: | ---: | ---: | ---: | :--- | ---: | ---: | ---: |
| 2 | 199 | 202 | 399 | $\ldots$ | 9799 | 9802 | 9999 |
| 3 | 198 | 203 | 398 | $\ldots$ | 9798 | 9803 | 9998 |
| 4 | 197 | 204 | 397 | $\ldots$ | 9797 | 9804 | 9997 |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\ldots$ | $\ldots$ | $\ldots$ |
| 98 | 103 | 298 | 303 | $\ldots$ | 9703 | 9898 | 9903 |
| 99 | 102 | 299 | 302 | $\ldots$ | 9702 | 9899 | 9902 |
| 100 | 101 | 300 | 301 | $\ldots$ | 9701 | 9900 | 9901 |

考虑 Max 走的任意一条路径, 对 $1 \sim 50$ 中的任意整数 $n$, 第 $2 n-1$ 列与第 $2 n$ 列的相邻两格所填之和至少为 $200(2 n-1)$.

故 Max 至少要花费 $200 \times(1+3+5+\cdots+99)=500000$ 枚硬币.

## 上界 / Max 的策略:

对于棋盘中数字的任意一种填法. 我们将棋盘分成 50 个水平放置的 $2 \times 100$的小矩形. 由于棋盘中所有数之和为 50005000 , 可以找到一个小矩形, 小矩形中所有数之和不大于 1000100 . 对于所选小矩形的每一列, 我们从这列的两个数中选最小数所在的方格. 则这些选中的方格就构成由左至右的一条路径, 记这条路径上所有数之和为 $S$. 在小矩形中的每一列的两个数中, 最大数比最小数至少大 1. 那么这个小矩形中所有数之和至少为 $2 S+100$. 这说明 $2 S+100 \leq 1000100$,则 $S \leq 500000$.

这说明棋盘中的数不管怎么填, Max 可以选择一条路径, 使得他至多需要支付 500000 枚硬币。

综上可知, 答案为 500000 枚硬币.

评注 这是一道中等难度的组合问题. 为了 Max 支付更多的钱, 这就需要相邻两列的所有相邻方格所填数之和相差不能太大 (相差太大就会出现有的路径上的数之和很大而有的很小), 很自然得会想到以 $S$ 型去填数, 这就得到了构造.证明的想法是做局部估计, 先找一个 $2 \times 100$ 的小矩形, 使得它们中所填数之和
尽可能小, 再从这个小矩形的每一列中选出最小的数, 这样就得到了一个很小的上界. 综合两方面就得到了解答.
6. $\triangle A B C$ 的内切圆与边 $B C, A C$ 分别相切于点 $D, E$. 设 $P$ 为内切圆的劣弧 $D E$ 上一点, 且满足 $\angle A P E=\angle D P B$. 线段 $A P, B P$ 分别交线段 $D E$ 于点 $K, L$. 求证: $2 K L=D E$.

证法一 我们需要如下的引理.

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-10.jpg?height=594&width=391&top_left_y=745&top_left_x=838)

引理 在 $\triangle A B C$ 中, $A A_{1}$ 是过 $A$ 的中线. 过 $B, C$ 分别作 $\triangle A B C$ 的外接圆的切线, 这两条切线交于 $A_{2}$, 则有 $\angle B A A_{1}=\angle C A A_{2}$.

引理的证明 由于

$$
\frac{A_{1} B}{A_{1} C}=\frac{A B \cdot \sin \angle B A A_{1}}{A C \cdot \sin \angle C A A_{1}}
$$

又 $A_{1} B=A_{1} C$, 从而

$$
\frac{\sin \angle B A A_{1}}{\sin \angle C A A_{1}}=\frac{A C}{A B}
$$

在 $\triangle A B A_{2}$ 中, 由正弦定理有

$$
\frac{\sin \angle B A A_{2}}{\sin \angle A B A_{2}}=\frac{A_{2} B}{A_{2} A}
$$

同理,

$$
\frac{\sin \angle C A A_{2}}{\sin \angle A C A_{2}}=\frac{A_{2} C}{A_{2} A}
$$

又 $A_{2} B=A_{2} C$, 上两式相除得

$$
\frac{\sin \angle B A A_{2}}{\sin \angle A B A_{2}}=\frac{\sin \angle C A A_{2}}{\sin \angle A C A_{2}}
$$

即

$$
\frac{\sin \angle C A A_{2}}{\sin \angle B A A_{2}}=\frac{\sin \angle A C A_{2}}{\sin \angle A B A_{2}}
$$

注意到 $A_{2} B, A_{2} C$ 是圆的切线, 所以

$$
\triangle A B A_{2}=180^{\circ}-\angle A C B, \angle A C A_{2}=180^{\circ}-\angle A B C .
$$

则

$$
\frac{\sin \angle A C A_{2}}{\sin \angle A B A_{2}}=\frac{\sin \angle A B C}{\sin \angle A C B}=\frac{A C}{A B}
$$

故

$$
\frac{\sin \angle B A A_{1}}{\sin \angle C A A_{1}}=\frac{\sin \angle C A A_{2}}{\sin \angle B A A_{2}}
$$

又

$$
\angle B A C=\angle B A A_{1}+\angle C A A_{1}=\angle C A A_{2}+\angle B A A_{2},
$$

所以 $\angle B A A_{1}=\angle C A A_{2}$. 引理获证.

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-11.jpg?height=625&width=731&top_left_y=1041&top_left_x=660)

回到原题. 记 $F$ 为内切圆与边 $A B$ 的切点, $M, N$ 分别为线段 $E F$ 与 $D F$的中点, 连接 $P M, P N$. 由引理, $\angle A P E=\angle F P M, \angle D P B=\angle F P N$, 从而 $\angle A P E=\angle F P N$, 即 $\angle K P E=\angle N P F$. 又 $P, E, D, F$ 四点共圆, 从而

$$
\angle P E K=\angle P E D=\angle P F N \text {. }
$$

所以 $\triangle P E K \sim \triangle P F N$. 则

$$
\frac{E K}{F N}=\frac{P E}{P F}, E K=F N \cdot \frac{P E}{P F}=\frac{D F \cdot P E}{2 P F} .
$$

同理,

$$
\triangle P D L \sim \triangle P F M, D L=\frac{E F \cdot P D}{2 P F} .
$$

这样

$$
E K+D L=\frac{D F \cdot P E+E F \cdot P D}{2 P F} .
$$

而由托勒密定理,

$$
D F \cdot P E+E F \cdot P D=D E \cdot P F
$$

故

$$
E K+D L=\frac{1}{2} D E
$$

则有

$$
K L=D E-E K-D L=\frac{1}{2} D E
$$

综上可知, 结论成立.

## 证法二 (郑立瑜)

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-12.jpg?height=648&width=596&top_left_y=972&top_left_x=730)

设 $A P, B P$ 与内切圆的另一交点分别为 $U, V$, 内切圆切 $A B$ 于点 $F$. 由

$$
\angle A P E=\angle D P B, \angle P U E=\angle P D E
$$

知 $\triangle P E U \sim \triangle P L D$. 故 $P U \cdot P L=P E \cdot P D$. 同理 $P V \cdot P K=P E \cdot P D$.

以 $P$ 为反演中心, $P E \cdot P D$ 为反演幂进行反演变换, 再将图形关于 $\angle U P V$的内角平分线做反射变换.

设 $X$ 在上述复合变换下的象为 $X^{\prime}$, 并记作 $X \rightarrow X^{\prime}$. 由前证易知:

$$
E \leftrightarrow D ; K \leftrightarrow V, L \leftrightarrow U .
$$

由 $P, U, V, F$ 共圆知 $F^{\prime}, D, E$ 共线.

又 $P, E, U, F$ 构成调和四边形, 故 $U^{\prime}$ 是线段 $E^{\prime} F^{\prime}$ 的中点. 即 $L$ 是线段 $F^{\prime} D$的中点.

同理, $K$ 是线段 $F^{\prime} E$ 的中点. 故

$$
D E=D F^{\prime}+F^{\prime} E=2 L F^{\prime}+2 F^{\prime} K=2 L K .
$$

证毕!

评注 这是一道非常困难的几何题, 解答不长但十分难想, 中国的两位选手均未做出此题. 证法一所用的引理是个常见的几何性质, 但想到用这个引理来解此题却颇为不易. 使用引理可以把 $\angle A P E$ 与 $\angle D P B$ 这两个很难处理的角导成了三角形中线与边的夹角, 再结合相似三角形和托勒密定理不难证得结论.

证法二所用的反演变换通常称之为 “Iran 式反演”, 这样的反演通常应用到如下两种模型中.

1. 圆内的平行线

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-13.jpg?height=434&width=437&top_left_y=848&top_left_x=815)

2. 完全四边形中的 Miguel 点

![](https://cdn.mathpix.com/cropped/2024_02_26_24effe936c326d5b9cfcg-13.jpg?height=325&width=440&top_left_y=1408&top_left_x=814)

本题中我们进行上述变换的动机是注意到了 $\angle A P E=\angle D P B \Leftrightarrow D E / / U V$.应用一些反演的基本性质就不难确定 $F^{\prime}$ 的位置及其特殊性.

