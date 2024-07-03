数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2020 年美国数学国家队选拔考试试题解析 

梁敬勋<br>(浙江省杭州学军中学, 310012)<br>指导教师: 边红平

【指导教师按语】近几年来, 因为有大量前 IMO 金牌得主参与命题和培训, 所以美国数学奥林匹克代表队是公认的世界顶级强队, 其命题总有很强的高等数学(古典)背景, 引领着竞赛命题的潮流.

这是 2020 年美国代表队选拔的第二轮考题, 解析部分反映的是梁敬勋同学作为一个竞赛选手最原始的解题思维, 因此解法不一定是最简单的.

## I. 试 题

1. 对一个满足

$$
1=\frac{b_{1}}{1^{2}}>\frac{b_{2}}{2^{2}}>\frac{b_{3}}{3^{2}}>\frac{b_{4}}{4^{2}}>\cdots
$$

的正整数列 $\left\{b_{m}\right\}, r$ 为满足 $\frac{b_{n}}{n^{2}} \geq r$ 总成立的最大实数. 对满足条件的所有正整数列, 求 $r$ 的一切可能值.

2. 两圆 $\Gamma_{1}, \Gamma_{2}$ 的外公切线 $\ell_{1}, \ell_{2}$ 交于 $T$. 记 $\ell_{1}$ 切 $\Gamma_{1}$ 于 $A, \ell_{2}$ 切 $\Gamma_{2}$ 于 $B$. 圆 $\Omega$ 过 $A$ 和 $B$ 交 $\Gamma_{1}$ 于 $C$ 且交 $\Gamma_{2}$ 于 $D$, 且 $A B C D$ 为凸四边形. $A C$ 与 $B D$ 交于 $X$, 且 $A D$ 与 $B C$ 交于 $Y$. 证明: $T, X, Y$ 共线.
3. $\alpha \geq 1$ 为一给定的大于等于 1 的实数. 赫菲斯(希腊火神, 简称 $A$ ) 和波塞冬(希腊海神, 简称 $B$ ) 轮流在一个无穷大的方格表上玩游戏. 游戏开始前, $B$ 先把有限个方格标为洪水格. 之后每轮 $A$ 先行动, 把若干(至少 1 个)长 1 的方格边界变为堤坝, 要求第 $n$ 轮结束时, 全部堤坝由若干连续长 1 的方格边界构成, 组成一个长度不超过 $\alpha n$ 的不自交的折线或者一个单圈(构成圈意味着之后无法再增加堤坝了). 之后 $B$ 行动, 把所有与洪水格相邻, 且没有被堤坝直接隔开的格

修订日期: 2020-03-23.
子也标记为洪水格. 求一切 $\alpha$, 使得对任意开局和 $A$ 的一切策略, $B$ 总可以在若干轮后, 用堤坝组成一个围住所有洪水格的圈(进而拯救世界).

4. 对于简单图 $G$, 定义 $G^{\prime}$ 如下:

(1) $G^{\prime}$ 的顶点集与 $G$ 相同;

(2) 对于不同顶点 $u, v$, 在 $G^{\prime}$ 中 $u, v$ 之间有边当且仅当在 $G$ 中 $u$ 和 $v$ 与至少一个点同时相连.

证明: 若 $G$ 是有限简单图且 $G$ 与 $\left(G^{\prime}\right)^{\prime}$ 同构, 则 $G$ 与 $G^{\prime}$ 也同构.

注: 两个简单图 $G_{1}=\left(V_{1}, E_{1}\right)$ 和 $G_{2}=\left(V_{2}, E_{2}\right)$ 同构, 是指存在双射 $f: V_{1} \rightarrow V_{2}$, 使得 $\{u, v\} \in E_{1}$, 当且仅当 $\{f(u), f(v)\} \in E_{2}$.

5. 求所有正整数 $n \geq 2$, 使得存在正整数 $m$ 和整系数多项式 $P(x)$, 满足

(1) $m>1$ 且 $\operatorname{gcd}(m, n)=1$;

(2) $n$ 不整除 $P(0), P^{2}(0), \cdots, P^{m-1}(0)$ 中的任何一个;

(3) $n$ 整除 $P^{m}(0)$.

其中, $P^{k}$ 表示 $P$ 的 $k$ 次迭代, 例如 $P^{1}(0)=P(0), P^{2}(0)=P(P(0))$.

6. 设 $P_{1} P_{2} \cdots P_{100}$ 为平面上的圆内接 100 边形. 对正整数 $i$, 定义点 $Q_{i}$ 为对角线 $P_{i-2} P_{i+1}$ 和 $P_{i-1} P_{i+2}$ 的交点, 并规定 $P_{i+100}=P_{i}$. 已知平面上一点 $P$ 使得 $P P_{i} \perp P_{i-1} P_{i+1}$ 对任意正整数 $i$ 成立. 证明: $Q_{1}, Q_{2}, \cdots, Q_{100}$ 共圆.

## II . 解答与评注

1. 对一个满足

$$
1=\frac{b_{1}}{1^{2}}>\frac{b_{2}}{2^{2}}>\frac{b_{3}}{3^{2}}>\frac{b_{4}}{4^{2}}>\cdots,
$$

的正整数列 $\left\{b_{m}\right\}, r$ 为满足 $\frac{b_{n}}{n^{2}} \geq r$ 总成立的最大实数. 对满足条件的所有正整数列, 求 $r$ 的一切可能值.

解 $r$ 为 $\left[0, \frac{1}{2}\right]$ 内的全体实数.

一方面, 由于 $b_{n} \in \mathbb{N}_{+}$, 故 $\frac{b_{n}}{n^{2}}>0, \forall n \in \mathbb{N}_{+}$. 由条件,

$$
r=\inf _{n \in \mathbb{N}_{+}} \frac{b_{n}}{n^{2}}=\lim _{n \rightarrow+\infty} \frac{b_{n}}{n^{2}}
$$

故 $r \geq 0$. 因为 $b_{1}=1=\frac{1 \times 2}{2}$, 假设

$$
b_{n-1} \leq \frac{n(n-1)}{2}(n \geq 2)
$$

则

$$
\frac{b_{n}}{n^{2}}<\frac{b_{n-1}}{(n-1)^{2}} \leq \frac{n(n-1)}{2(n-1)^{2}}=\frac{n}{2(n-1)} .
$$

故

$$
\begin{aligned}
b_{n} & <\frac{n^{3}}{2(n-1)} \\
& =\frac{n}{2} \cdot \frac{(n-1)(n+1)+1}{n-1} \\
& =\frac{n(n+1)}{2}+\frac{n}{2(n-1)} \\
& \leq \frac{n(n+1)}{2}+1 .
\end{aligned}
$$

从而由归纳原理, 总有 $b_{n} \leq \frac{n(n+1)}{2}$. 故

$$
\frac{b_{n}}{n^{2}} \leq \frac{n+1}{2 n} \Rightarrow r=\lim _{n \rightarrow+\infty} \frac{b_{n}}{n^{2}} \leq \lim _{n \rightarrow+\infty} \frac{n+1}{2 n}=\frac{1}{2}
$$

从而 $0 \leq r \leq \frac{1}{2}$.

另一方面, $\left[0, \frac{1}{2}\right]$ 的每个数均可作为 $r$ 的值. 记

$$
\left\{c_{n}\right\}_{n=1}^{+\infty}: c_{n}=\frac{n(n+1)}{2}
$$

(1) $r=\frac{1}{2}$ 时, 取 $\left\{b_{n}\right\}=\left\{c_{n}\right\}$ 即可. 易见 $\frac{c_{1}}{1^{2}}=1, n \geq 2$ 时,

$$
\frac{c_{n-1}}{(n-1)^{2}}=\frac{n}{2(n-1)}>\frac{n+1}{2 n}=\frac{c_{n}}{n^{2}},
$$

且 $\lim _{n \rightarrow+\infty} \frac{c_{n}}{n^{2}}=\frac{1}{2}$.

(2) $r=0$ 时, 取 $b_{n}=1, \forall n \in \mathbb{N}_{+}$即可.

(3) $0<r<\frac{1}{2}$ 时, 记 $\left\{a_{n}\right\}_{n=1}^{+\infty}$ 为:

$$
a_{n}=[r n(n+1)]+2 n, \forall n \in \mathbb{N}_{+}
$$

由于 $r<\frac{1}{2}$, 故存在 $N \in \mathbb{N}_{+}, n \geq N$ 时, $a_{n}<c_{n}$. 取

$$
b_{n}= \begin{cases}c_{n}, & n \leq N . \\ a_{n}, & n>N .\end{cases}
$$

下验证 $b_{n}$ 符合. 显然 $r=\lim _{n \rightarrow+\infty} \frac{b_{n}}{n^{2}}$, 仅需证

$$
\frac{b_{n-1}}{(n-1)^{2}}>\frac{b_{n}}{n^{2}}, \forall n \in \mathbb{N}_{+}
$$

$n \leq N$ 时, 由 $\frac{c_{n-1}}{(n-1)^{2}}>\frac{c_{n}}{n^{2}}$ 既得.

$n=N+1$ 时,

$$
\frac{b_{n-1}}{(n-1)^{2}}=\frac{c_{n-1}}{(n-1)^{2}}>\frac{c_{n}}{n^{2}}>\frac{a_{n}}{n^{2}}=\frac{b_{n}}{n^{2}},
$$

符合.

$$
\begin{aligned}
& n>N+1 \text { 时, 记 } \epsilon=\{r n(n+1)\}, \epsilon^{\prime}=\{r n(n-1)\}, \text { 则 } \\
& \begin{aligned}
\frac{b_{n-1}}{(n-1)^{2}}-\frac{b_{n}}{n^{2}} & =\frac{r n(n-1)+2(n-1)-\epsilon^{\prime}}{(n-1)^{2}}-\frac{r n(n+1)+2 n-\epsilon}{n^{2}} \\
& =r\left(\frac{n}{n-1}-\frac{n+1}{n}\right)+\frac{2}{n-1}-\frac{2}{n}-\frac{\epsilon^{\prime}}{(n-1)^{2}}+\frac{\epsilon}{n^{2}} \\
& >0+\frac{2}{n(n-1)}-\frac{1}{(n-1)^{2}}+0 \\
& \geq 0, \quad(n \geq 2)
\end{aligned}
\end{aligned}
$$

故 $\left\{b_{n}\right\}$ 符合.

从而 $r$ 的所有可能值组成集合 $\left[0, \frac{1}{2}\right]$.

评注 $r$ 的上界只要通过特例探索, 用贪心算法即可得到. 而构造时需要兼顾整数和增长速度, 设定为 $\left[r n^{2}+a n\right]$ 后要取比较大的 $a$ 才能平衡“[ ] ”的不确定性.

2. 两圆 $\Gamma_{1}, \Gamma_{2}$ 的外公切线 $\ell_{1}, \ell_{2}$ 交于 $T$. 记 $\ell_{1}$ 切 $\Gamma_{1}$ 于 $A, \ell_{2}$ 切 $\Gamma_{2}$ 于 $B$. 圆 $\Omega$ 过 $A$ 和 $B$ 交 $\Gamma_{1}$ 于 $C$ 且交 $\Gamma_{2}$ 于 $D$, 且 $A B C D$ 为凸四边形. $A C$ 与 $B D$ 交于 $X$, 且 $A D$ 与 $B C$ 交于 $Y$. 证明: $T, X, Y$ 共线.



证明 设 $\ell_{2}$ 与 $\Gamma_{1}$ 切于 $E, \ell_{1}$ 与 $\Gamma_{2}$ 切于 $F$. 设 $B X \cap A E=Z, E X \cap B F=S$.由 $X C \cdot X A=X D \cdot X B$, 可得 $X$ 在 $\Gamma_{1}, \Gamma_{2}$ 根轴上. 又 $A F$ 中点, $B E$ 中点均在 $\Gamma_{1}, \Gamma_{2}$ 的根轴上, 故 $X$ 在梯形 $A E B F$ 中位线上, 从而

$$
X Z=X B, X E=X S \Rightarrow \text { 四边形 } E Z S B \text { 为平行四边形 } \Rightarrow Z S / / B E \text {. }
$$

$\measuredangle(A Z, A E)=\measuredangle(B E, B F)=\measuredangle(S Z, S F) \Rightarrow A, Z, S, F$ 共圆. 设此圆圆心为 $O$. 设 $U$ 使 $\overrightarrow{C X}=\overrightarrow{X U}$, 则四边形 $B C Z U, S C E U$ 为平行四边形. 由

$$
\measuredangle(F D, D Z)=\measuredangle(F D, D B)=\measuredangle(F T, F B)=\measuredangle(A T, A Z),
$$

可知 $A, Z, D, F$ 共圆, 即 $D \in \odot O$. 由

$$
\measuredangle(S U, U A)=\measuredangle(E C, C U)=\measuredangle(E A, A F)=-\measuredangle(A Z, Z S)=\measuredangle(S Z, Z A),
$$

可知 $A, Z, U, S$ 共圆, 即 $U \in \odot O$.

设 $E S$ 与 $\odot O$ 另一交点为 $V$, 且 $U D \cap B F=L$. 对 $\odot O$ 的内接六边形 $A Z D V S F$ 用 Pascal 定理:

$$
A Z \cap S V=E, Z D \cap S F=B, D V \cap F A \triangleq T^{\prime},
$$

有 $E, B, T^{\prime}$ 共线. 故

$$
T^{\prime}=B E \cap A F \equiv T .
$$

从而 $E, B, T$ 共线. 对 $\odot O$ 的内接六边形 $A U D V S F$ 用 Pascal 定理:

$$
A U \cap V S=X, U D \cap S F=L, D V \cap F A=T,
$$

故 $X, L, T$ 共线.

现在, 设 $X T \cap Z U=W, X T \cap A Z=K, X T \cap A D=Y^{\prime}$. 由 $X, L, T$ 共线,及 $X$ 在梯形 $A E B F$ 中位线上, 知 $X K=X L$. 对 $\odot O$ 中过 $X$ 的两弦 $A U, D Z$用蝴蝶定理之逆, 由 $X K=X L, K \in A Z, L \in U D$, 知 $O X \perp X T$. 对 $\odot O$ 中过 $X$ 的两弦 $A U, D Z$ 用蝴蝶定理,

$$
W=Z U \cap X T, Y^{\prime}=A D \cap X T, O X \perp X T \Rightarrow X W=X Y^{\prime}
$$

又由

$$
U Z / / B C, X U=X C \Rightarrow Y^{\prime} \in B C .
$$

故

$$
Y^{\prime}=B C \cap A D \equiv Y .
$$

从而 $X, Y, T$ 共线, 得证!

评注 $(1)$. 要满足 $A B C D$ 为凸四边形需要 $\Gamma_{1}$ 与 $\Gamma_{2}$ 相交.

(2). 本题若以 $\Gamma_{1}, \Gamma_{2}$ 为基本量, 则 $A, B$ 的位置难刻画. 上面的做法以 $A E B F$ 这一等腰梯形为基本量, 隐去 $\Gamma_{1}, \Gamma_{2}$. 但相应地, $C, D$ 的定义变复杂. 通过分析角度发现 $\odot O$ 可替代 $\Gamma_{1}, \Gamma_{2}$ 直接定义 $C, D$. 这样的问题归结为一个圆上一些弦的交点导出的共线问题, 从而可用 Pascal 定理进行逐个消点. 这是从条件入手的做法.

(3). 从结论入手的做法如下:仅需证

$$
\frac{d(Y ; A C)}{d(Y ; B D)}=\frac{d(T ; A C)}{d(T ; B D)}
$$

且 $Y, T$ 在 $A C, B D$ 的一个对顶角内, 而

$$
\frac{d(T ; A C)}{d(T ; B D)}=\frac{A T \sin \angle C A T}{B T \sin \angle D B T}=\frac{r_{1} \sin \angle C A T}{r_{2} \sin \angle D B T}=\frac{A C}{B D}=\frac{d(Y ; A C)}{d(Y ; B D)},
$$

仅需再对 $Y, T$ 的位置做些讨论.
3. $\alpha \geq 1$ 为一给定的大于等于 1 的实数. 赫菲斯(希腊火神, 简称 $A$ )和波塞冬(希腊海神, 简称 $B$ )轮流在一个无穷大的方格表上玩游戏. 游戏开始前, $B$ 先把有限个方格标为洪水格. 之后每轮 $A$ 先行动, 把若干(至少 1 个)长 1 的方格边界变为堤坝, 要求第 $n$ 轮结束时, 全部堤坝由若干连续长 1 的方格边界构成, 组成一个长度不超过 $\alpha n$ 的不自交的折线或者一个单圈(构成圈意味着之后无法再增加堤坝了). 之后 $B$ 行动, 把所有与洪水格相邻, 且没有被堤坝直接隔开的格子也标记为洪水格. 求一切 $\alpha$, 使得对任意开局和 $A$ 的一切策略, $B$ 总可以在若干轮后, 用堤坝组成一个围住所有洪水格的圈(进而拯救世界).

解 所求的 $\alpha$ 为 $(2,+\infty)$ 内的全体数.

根据题设, 所有方格都是单位正方形. 建立以格线为轴的直角坐标系, 对平面上两点 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$. 记

$$
d(A, B)=\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right| \text { (称为 } A, B \text { 的 “距离”). }
$$

对平面上 2 个方格, 其距离定义为其中心的距离. 对任一平面方格 $A$ 及正整数 $n$, 记

$$
\Gamma_{A}(n)=\{B \mid B \text { 为某方格, } d(A, B) \leq n\},
$$

称这种图形为“阶梯形”.

一方面, 若 $\alpha>2$, 则火神(下简记为甲)有必胜策略:

首先, 不妨海神(下简记为乙)开始时注入的方格恰形如阶梯形(若不然, 显然可取某阶梯形 $\Gamma$ 盖住乙所选的所有格. 将乙选的格改成 $\Gamma$ 显然对乙更为有利).

设该阶梯形为 $\Gamma_{A}(n)$, 其最上方的方格的上边界记为 $X_{1} Y_{1}$, 其中 $X_{1}$ 为左侧的顶点. $X_{1} Y_{1}$ 所在直线为 $l_{1}$. 将 $l_{1}$ 上 $X_{1}$ 左侧的格点依次标为 $X_{2}, X_{3}, \cdots$, 类似定义 $Y_{1}, Y_{2}, \cdots$.

甲的策略分为两阶段

(1) 甲首先建墙壁 $X_{1} Y_{1}$, 之后每一轮甲将墙壁往左右各延展一格(则洪水始终在 $l_{1}$ 下方). 由于 $\alpha>2$, 故存在 $m_{1} \in \mathbb{N}_{+}$使

$$
\alpha m_{1}>2 m_{1}-1+4 n+4 .
$$

则到第 $\left(m_{1}+1\right)$ 轮时甲停止前述操作, 改为: 将墙壁左侧往左延伸 $(n+1)$ 格, 再



往下延伸 $(n+1)$ 格. 对右边类似处理. 这些都是合法的, 设此时坚直的墙壁分别位于 $l_{2}, l_{3}$ 上, 则洪水均位于直线 $l_{2}, l_{3}$ 之间.

(2) 接下来, 甲每次将左右的墙壁往下延展一格. 同样地, 存在 $m_{2} \in \mathbb{N}_{+}$使

$$
\alpha m_{2}>2 m_{2}+4\left(m_{1}+n+2\right) \text {. }
$$

则甲重复上述操作 $m_{2}$ 次后, 第 $\left(m_{2}+1\right)$ 次改为将两侧墙壁向下延伸 $m_{1}+n+2$个单位, 并用水平墙壁连接两侧墙壁底部. 易验证该策略是符合的.

故 $\alpha>2$ 符合.

另一方面, 当 $\alpha \leq 2$ 时, 下证:甲没有必胜策略.

乙任选一格 $A_{0}$ 注入洪水, 之后令洪水自行扩张. 下证: 甲无论如何也无法圈住所有洪水.

反证法, 若不然, 假设甲在第 $m$ 轮形成了封闭的提坎 $C$ 圈住所有洪水. 由于第 $(m-1)$ 轮甲尚未成功, 故该轮至少有一个新格 $A_{m-1}$ 被注入洪水. 由洪水注入的规则, 有一条由方格组成的链

$$
A_{0}-A_{1}-\cdots-A_{m-1}
$$

使 $A_{i}$ 与 $A_{i+1}$ 相邻 $(0 \leq i \leq m-2)$, 且 $A_{i}$ 为第 $i$ 轮新注入洪水的格 $(1 \leq i \leq$ $m-1)$. 用 $P_{i}$ 表示 $A_{i}$ 的中心, 则

$$
L: P_{0}-P_{1}-\cdots-P_{m-1}
$$

为一条折线. 将穿过方格中心且与格线平行的直线称为 “好线”, 任取一条好线 $\ell$,用 $f(l)$ 表示 $C$ 中与 $l$ 相交的边数. $C$ 中每边恰与一条好线相交, 故

$$
|C|=\sum_{l \text { 为好线 }} f(l),
$$

考虑 $\ell \cap L$, 其为由一些点与一些线段组成的集合(不同的线段无公共点, 这里的线段为 $L$ 某些边之并).



我们在每条线段中选出下标较小的端点, 连同其它点组成集合 $S_{\ell}$, 如上图中 $S_{\ell}=\left\{P_{3}, P_{6}, P_{11}, P_{20}\right\}$.

断言 $1 \quad f(l) \geq 2\left|S_{\ell}\right|$.

证明 将 $\ell \cap L$ 上的点视为长为 0 的线段. 设 $\ell$ 上所有这些线段从左到右为

$$
X_{i} Y_{i},(i=1,2, \cdots, r), r=\left|S_{\ell}\right| \text {, }
$$

其中 $X_{i}$ 在 $Y_{i}$ 左侧. 由 $C$ 的定义, $X_{1}$ 左侧及 $Y_{1}$ 右侧 $\ell$ 均与 $C$ 的某边相交. 又易见在 $Y_{i}$ 与 $X_{i+1}$ 之间 $\ell$ 必与 $C$ 某边相交, 否则我们将 $L$ 中 $Y_{i}$ 与 $X_{i+1}$ 之间的部分删去, 改为沿 $Y_{i} X_{i+1}$ 走, 则得一条更短的(两点之间线段最短)从 $P_{0}$ 到 $P_{m-1}$的路, 不与 $C$ 相交, 与 $A_{m-1}$ 为第 $m-1$ 轮新注入的矛盾!

最后, $Y_{i}$ 与 $X_{i+1}$ 之间 $\ell$ 与 $C$ 至少两边相交. 若不然, 封闭曲线 $C$ 将平面分为两部分, 若 $Y_{i} X_{i+1}$ 与 $C$ 恰一个交点, 则 $Y_{i}, X_{i+1}$ 在 $C$ 两侧, 与 $C$ 的取法矛盾!

故 $f(\ell) \geq 1+2(r-1)+1=2 r$. 断言 1 得证.

## 断言 2

$$
\underset{\ell \text { 为好线 }}{\cup} S_{\ell}=V(\ell)\left(=\left\{P_{0}, P_{1}, \cdots, P_{m-1}\right\}\right),
$$

且 $P_{0}$ 至少在两个 $S_{\ell}$ 中出现.

证明 对 $1 \leq i \leq m-2$, 若 $P_{i-1}, P_{i}, P_{i+1}$ 共线, 则设 $\ell$ 为过 $P_{i}$ 且与 $P_{i-1} P_{i+1}$垂直的线, 则 $P_{i} \in S_{\ell}$. 若 $P_{i-1}, P_{i}, P_{i+1}$ 不共线, 则 $P_{i} \in S_{P_{i} P_{i+1}}$. 对于 $P_{m-1}$, 设 $\ell$为过 $P_{m-1}$ 作的 $P_{m-1} P_{m-2}$ 的垂线, 则 $P_{m-1} \in S_{\ell}$. 对于 $P_{0}$, 易见过 $P_{0}$ 的任一好线 $\ell$ 均有 $P_{0} \in S_{\ell}$. 断言 2 得证.

由断言 1,2 及式 (i),

$$
\begin{aligned}
|C| & =\sum_{\ell \text { 为好线 }} f(\ell) \geq 2 \sum_{\ell \text { 为好线 }}\left|S_{\ell}\right|=2\left(\sum_{\ell \text { 为好线 }} \sum_{P \in S_{\ell}} 1\right)=2\left(\sum_{P \in V(l)} \sum_{\ell: P \in S_{\ell}} 1\right) \\
& \geq 2(2+(m-1))=2 m+2>2 m .
\end{aligned}
$$

但 $C$ 为第 $m$ 轮建成的, $|C| \leq \alpha m \leq 2 m$, 矛盾!

故 $\alpha \leq 2$ 不符.

综上, 所求为 $\alpha>2$.

评注 (1). 讨论最初一个方格注水的情况从构造入手容易猜出 $\alpha>2$, 构造
与特例完全类似, 唯一的技巧是不妨初始格局为阶梯形使我们容易用矩形给出墙的造法, 这样更好表达。

(2). 证明部分的关键是把多轮的信息合起来：为了给出墙数与轮数的关系，我们主要是利用每次洪水的分布变化来判断墙的位置.但一步步分析每次得到的信息太少, 一旦将整个过程连起来写成链 $\ell$, 则所有的条件都很好地反映到 $\ell$的参数上.

4. 对于简单图 $G$, 定义 $G^{\prime}$ 如下:

(1) $G^{\prime}$ 的顶点集与 $G$ 相同;

(2) 对于不同顶点 $u, v$, 在 $G^{\prime}$ 中 $u, v$ 之间有边当且仅当在 $G$ 中 $u$ 和 $v$ 与至少一个点同时相连.

证明: 若 $G$ 是有限简单图且 $G$ 与 $\left(G^{\prime}\right)^{\prime}$ 同构, 则 $G$ 与 $G^{\prime}$ 也同构.

注: 两个简单图 $G_{1}=\left(V_{1}, E_{1}\right)$ 和 $G_{2}=\left(V_{2}, E_{2}\right)$ 同构, 是指存在双射 $f: V_{1} \rightarrow V_{2}$, 使得 $\{u, v\} \in E_{1}$, 当且仅当 $\{f(u), f(v)\} \in E_{2}$.

证明 先证明如下引理.

引理 若 $G$ 与 $\left(G^{\prime}\right)^{\prime}$ 同构, 则 $G$ 的每个连通分支为完全图或奇圈.

证明 设 $G=(V, E), G^{\prime}=\left(V, E_{1}\right),\left(G^{\prime}\right)^{\prime}=\left(V, E_{2}\right)$. 由 $G \cong\left(G^{\prime}\right)^{\prime}$ 知存在一一映射 $\varphi: V \rightarrow V$, 使 $\forall u, v \in V, u \neq v$, 有

$$
u v \in E \Leftrightarrow \varphi(u) \varphi(v) \in E .
$$

注意到, 若有点 $u, v_{1}, v_{2}, v_{3}$, 使 $u v_{i} \in E(i=1,2,3)$, 则由 $G^{\prime}$ 定义知 $v_{1} v_{2}, v_{2} v_{3}$, $v_{1} v_{3} \in E_{1}$, 从而 $v_{1} v_{2}, v_{2} v_{3}, v_{1} v_{3} \in E_{2}$, 于是 $\varphi^{-1}\left(v_{1}\right) \varphi^{-1}\left(v_{2}\right), \varphi^{-1}\left(v_{2}\right) \varphi^{-1}\left(v_{3}\right)$, $\varphi^{-1}\left(v_{3}\right) \varphi^{-1}\left(v_{1}\right) \in E$. 也即:

若 $v_{1}, v_{2}, v_{3}$ 在 $G$ 中有公共邻点, 则 $\varphi^{-1}\left(v_{1}\right), \varphi^{-1}\left(v_{2}\right), \varphi^{-1}\left(v_{3}\right)$ 在 $G$ 中形成一个 $K_{3}$.

现在, 对 $|V|$ 归纳证明命题. $|V|=1$ 时结论显然.

假设对较小的 $|V|$ 命题成立, $|V|$ 时,

I. 若 $G$ 中有 $K_{3}$, 取 $G$ 中最大完全子图 $H,|V(H)| \geq 3$.

断言 $H$ 在 $G$ 中形成一个连通分支.

证明 若不然, 有 $v \in V(H), u \in V \backslash V(H)$, 使 $u v \in E$. 设 $V(H)=\left\{u_{1}, u_{2}, \cdots, u_{k}, v\right\}, k \geq 2$, 则


$u, u_{1}, \cdots, u_{k}$ 有公共邻点 $v$.

(1) $|V(H)| \geq 4$, 则 $k \geq 3$.
由 (i) 知: $\varphi^{-1}(u), \varphi^{-1}\left(u_{1}\right), \cdots, \varphi^{-1}\left(u_{k}\right)$ 在 $G$ 中导出完全子图. 由 $v, u_{2}, \cdots$, $u_{k}$ 有公共邻点 $u_{1}$, 结合 $(\mathrm{i})$ 知, $\varphi^{-1}(v)$ 与 $\varphi^{-1}\left(u_{2}\right)$ 相邻. 同理, $\varphi^{-1}\left(u_{i}\right)$ 与 $\varphi^{-1}(v)$相邻 $(1 \leq i \leq k)$.

由 $\varphi^{-1}\left(u_{2}\right), \cdots, \varphi^{-1}\left(u_{k}\right), \varphi^{-1}(u), \varphi^{-1}(v)$ 有公共邻点 $\varphi^{-1}\left(u_{1}\right)$, 由 (i) 知

$$
\varphi^{-2}\left(u_{2}\right), \varphi^{-2}\left(u_{3}\right), \cdots, \varphi^{-2}(u), \varphi^{-2}(v)
$$



在 $G$ 中导出完全子图(其中 $\varphi^{-2}=\varphi^{-1} \circ \varphi^{-1}$ ). 同理,

$$
\left(\left\{\varphi^{-2}\left(v_{i}\right) \mid 1 \leq i \leq k\right\} \cup\left\{\varphi^{-2}(u), \varphi^{-2}(v)\right\}\right) \backslash\left\{\varphi^{-2}\left(v_{j}\right)\right\}(1 \leq j \leq k) .
$$

在 $G$ 中导出完全子图. 由此易见 $\left\{\varphi^{-2}\left(v_{i}\right) \mid 1 \leq i \leq k\right\} \cup\left\{\varphi^{-2}(u), \varphi^{-2}(v)\right\}$ 在 $G$中导出完全子图, 其为 $k+2$ 阶完全图, 与 $|V(H)|=k+1$ 最大矛盾!

(2) $|V(H)|=3$.

由 $u v, v v_{1} \in E \Rightarrow u v_{1} \in E_{1}$. 同理 $u v_{2} \in E_{1}$. 又易见 $v v_{1}, v v_{2}, v_{1} v_{2} \in E_{1}$.从而 $u v_{i}, v v_{i}(i=1,2), v_{1} v_{2} \in E_{1}$. 这推出 $v, v_{1}, v_{2}, u$ 在 $\left(G^{\prime}\right)^{\prime}$ 中导出 $K_{4}$. 又 $G \cong\left(G^{\prime}\right)^{\prime} \Rightarrow G$ 中有 $K_{4}$, 与 $|V(H)|=3$ 矛盾! 断言得证.


此时, $G$ 的最大完全子图 $H$ 形成 $G$ 的连通分支. 易见 $\varphi(H)$ 与 $H$ 为同阶完全子图 $(\varphi(H)=G[\{\varphi(v) \mid v \in V\}])$, 从而 $\varphi(H)$ 亦为 $G$ 某一连通分支.

设 $i, j \in \mathbb{N}_{+}$为使 $0 \leq i<j$, 且 $\varphi^{i}(H)$ 与 $\varphi^{j}(H)$ 连通, 且 $j$ 最小的正整数对 (其中 $\varphi^{k}=\varphi \circ \varphi^{k-1}, k \in \mathbb{N}_{+}$). 由归纳易有 $\varphi^{i}(H)$ 为 $G$ 的最大完全子图, 从而为 $G$ 的连通分支, 故 $\varphi^{i}(H)=\varphi^{j}(H)$.

若 $i>0$, 则由

$$
\varphi^{i}(H)=\varphi^{j}(H) \Leftrightarrow \varphi^{i-1}(H)=\varphi^{j-1}(H),
$$

与 $j$ 的最小性矛盾! 故 $i=0$. 这样我们有 $H, \varphi(H), \cdots, \varphi^{j-1}(H)$ 两两不同, 且 $\varphi^{j}(H)=H$. 这表明: 若记

$$
H^{*}=H \cup \varphi(H) \cup \cdots \cup \varphi^{j-1}(H) \text {, }
$$

则 $\left.\varphi\right|_{H^{*}}$ 为 $H^{*} \rightarrow H^{*}$ 的一一映射, 则 $\left.\varphi\right|_{G-H^{*}}$ 为 $G-H^{*} \rightarrow G-H^{*}$ 的一一映射.又 $G$ 中 $H^{*}, G-H^{*}$ 互不连通, 从而 $G-H^{*}$ 与 $\left(\left(G-H^{*}\right)^{\prime}\right)^{\prime}$ 同构, 对 $G-H^{*}$ 用
归纳假设即得结论.

II. 若 $G$ 中无 $K_{3}$.

由 (i), 知 $G$ 中每点度 $\leq 2$. 这样的 $G$ 每个连通分支为圈或路. 设 $U$ 为 $G$ 中任一连通分支的顶点集.

(1) 若 $G[U]$ 为路, 则将 $U$ 的顶点按路黑白相间染色, 则 $G^{\prime}[U]$ 为黑点与白点组成的两条路, $\left(G^{\prime}\right)^{\prime}[U]$ 则为 4 条路.



(2) 若 $G[U]$ 为偶圈, 则 $G^{\prime}[U]$ 为 2 个圈, $\left(G^{\prime}\right)^{\prime}[U]$ 为 2 个或 4 个圈.

(3) 若 $G[U]$ 为奇圈, 则 $G^{\prime}[U],\left(G^{\prime}\right)^{\prime}[U]$ 仍为 1 个奇圈.



E



$\mathrm{E}_{1}$

偶圈



E



$\mathrm{E}_{1}$

奇圈

注意到, $G$ 中不连通的两点在 $\left(G^{\prime}\right)^{\prime}$ 中仍不连通, 故 $G$ 的连通分支个数不多于 $\left(G^{\prime}\right)^{\prime}$ 的. 又 $G \cong\left(G^{\prime}\right)^{\prime}, G$ 的连通分支个数等于 $\left(G^{\prime}\right)^{\prime}$ 的. 由 (1), (2), (3) 知 $G[U]$ 必为奇圈. 从而 $G$ 的每个连通分支为奇圈.

由归纳原理, 引理成立.

由引理, $G \cong\left(G^{\prime}\right)^{\prime}$ 知 $G$ 的每个连通分支为完全图或奇圈, 从而易验证 $G \cong G^{\prime}$. 得证!

评注 (1). 本题也可以比较 $G$ 与 $\left(G^{\prime}\right)^{\prime}$ 中三角形的个数来得到限制条件.

(2). 由于 $G$ 与 $\left(G^{\prime}\right)^{\prime}$ 的联系与 $G$ 与 $G^{\prime}$ 的联系关系不大, 所以需要先求 $G \cong\left(G^{\prime}\right)^{\prime}$ 的充要条件.

5. 求所有正整数 $n \geq 2$, 使得存在正整数 $m$ 和整系数多项式 $P(x)$, 满足

(1) $m>1$ 且 $\operatorname{gcd}(m, n)=1$;

(2) $n$ 不整除 $P(0), P^{2}(0), \cdots, P^{m-1}(0)$ 中的任何一个;

(3) $n$ 整除 $P^{m}(0)$.

其中, $P^{k}$ 表示 $P$ 的 $k$ 次迭代, 例如 $P^{1}(0)=P(0), P^{2}(0)=P(P(0))$.

## 解 记

$S=\left\{n \mid n \in \mathbb{N}_{+}\right.$且有: 若 $p$ 为 $n$ 的素因子, 素数 $q<p$, 则 $\left.q \mid n\right\}$.

所求的 $n$ 为 $\mathbb{N}_{+} \backslash S$ 中全体的数.

对 $P(x) \in \mathbb{Z}[x]$, 及 $n \in \mathbb{N}_{+}$, 用 $\delta_{n}(P)$ 表示满足 $n \mid P^{m}(0)$ 的最小正整数 $m$.

引理 设 $m^{\prime} \in \mathbb{N}_{+}$使 $n \mid P^{m^{\prime}}(0)$, 则 $\delta_{n}(P) \mid m^{\prime}$.

证明 记 $m=\delta_{n}(P)$. 由假设, $n \mid P^{m}(0)$, 且 $n \nmid P^{k}(0)(1 \leq k \leq m)$. 对 $\forall k \in \mathbb{N}_{+}$, 有

$$
\begin{gathered}
P^{m}(0)-0 \mid P^{m+1}(0)-P(0), \\
P^{m+1}(0)-P(0) \mid P^{m+2}(0)-P^{2}(0), \\
\vdots \\
P^{m+k-1}(0)-P^{k-1}(0) \mid P^{m+k}(0)-P^{k}(0) .
\end{gathered}
$$

其中用到 $P \in \mathbb{Z}[x]$, 有: $x-y \mid P(x)-P(y), \forall x, y \in \mathbb{Z}, x \neq y$. 故

$P^{m}(0) \mid P^{m+k}(0)-P^{k}(0)$ (约定 $P^{m}(0)=0$ 时含义为 $P^{m+k}(0)-P^{k}(0)=0$ ).

故

$$
P^{m+k}(0) \equiv P^{k}(0) \quad(\bmod n)
$$

由 (i), 设 $m^{\prime}=m q+r, q, r \in \mathbb{Z}, 0 \leq r<m$, 则

$$
0 \equiv P^{m^{\prime}}(0) \equiv P^{m^{\prime}-m}(0) \equiv \cdots \equiv P^{m^{\prime}-q m}(0) \equiv P^{r}(0) \quad(\bmod n)
$$

可得 $r=0$. 故 $m \mid m^{\prime}$. 引理得证.

由引理, 有 (注意 $\delta_{n}(P)$ 存在保证 $\delta_{p_{i}^{\alpha_{i}}}(P)$ 存在):

推论 若 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}, \alpha_{1}, \cdots, \alpha_{k} \in \mathbb{N}_{+}, p_{1}, \cdots, p_{k}$ 为互异素数, 则

$$
\delta_{n}(P)=\operatorname{lcm}\left(\delta_{p_{1}^{\alpha_{1}}}(P), \delta_{p_{2}^{\alpha_{2}}}(P), \cdots, \delta_{p_{k}^{\alpha_{k}}}(P)\right)
$$

证明 对 $m \in \mathbb{N}_{+}$, 我们有

$$
\begin{aligned}
n \mid P^{m}(0) & \Leftrightarrow p_{i}^{\alpha_{i}} \mid P^{m}(0), 1 \leq i \leq k, \\
& \Leftrightarrow \delta_{p_{i}^{\alpha_{i}}}(P) \mid m, 1 \leq i \leq k .
\end{aligned}
$$

最小的 $m$ 即为 $\mathrm{lcm}_{1 \leq i \leq k} \delta_{p_{i}}{ }_{i}(P)$.

不致混淆时, 用 $\delta_{n}$ 简记 $\delta_{n}(P)$.

先证: 若 $n \in S$, 则 $n$ 不合符题意.

反证法. 若 $n$ 符合题意, 则有 $m \in \mathbb{N}_{+}, m>1$ 及 $P \in \mathbb{Z}[x]$ 满足题设. 则 $m=\delta_{n}(P)=\delta_{n}$, 且 $(m, n)=1$. 设 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}$ (标准分解).
断言 $\delta_{p_{i}{ }_{i}}=1,1 \leq \beta_{i} \leq \alpha_{i}$.

证明 $\beta_{i}=1$ 时, 若 $\delta_{P_{i}}>1$, 则有素数 $q \mid \delta_{p_{i}}$.

若 $\delta_{p_{i}}>p_{i}$, 由抽庶原理, 有 $1 \leq k<l \leq p_{i}$, 使

$$
P^{k}(0) \equiv P^{l}(0) \quad\left(\bmod p_{i}\right)
$$

则归纳有

$$
P^{k+j}(0) \equiv P^{l+j}(0) \quad\left(\bmod p_{i}\right), j \in \mathbb{N} .
$$

特别地,

$$
0 \equiv P^{l+\left(\delta_{p_{i}}-l\right)}(0) \equiv P^{k+\left(\delta_{p_{i}}-l\right)}(0) \quad\left(\bmod p_{i}\right)
$$

而

$$
0<k+\left(\delta_{p_{i}}-l\right)<\delta_{p_{i}}
$$

矛盾! 故

$$
\delta_{p_{i}} \leq p_{i} \Rightarrow q \leq p \Rightarrow q \mid n .
$$

又 $q\left|\delta_{p_{i}} \Rightarrow q\right| \delta_{n}$, 与 $\left(n, \delta_{n}\right)=1$ 矛盾!

假设命题对 $\beta_{i}-1$ 成立, $\beta_{i}$ 时,

$$
\delta_{p_{i}^{\beta_{i}-1}}=1 \Rightarrow p_{i}^{\beta_{i}-1} \mid p(0)
$$

由于 $P(0)-0 \mid P^{2}(0)-P(0)$, 故

$$
P_{i}^{\beta_{i}-1} \mid P^{2}(0)
$$

类似由归纳知

$$
p_{i}^{\beta_{i}-1} \mid P^{k}(0), k \in \mathbb{N}_{+}
$$

若 $\delta_{p_{i} \beta_{i}}>1$, 则有素数 $q \mid \delta_{p_{i}^{\beta_{i}}}$. 又 $\left\{P^{k}(0)\left(\bmod p_{i}^{\beta_{i}}\right) \mid k \in \mathbb{N}_{+}\right\}$全为 $p_{i}^{\beta_{i}-1}$ 倍数,至多 $p_{i}$ 个元, 则同上推理(利用抽庶原理)可知 $\delta_{p_{i}}^{\beta_{i}} \leq p$. 从而 $q|n, q| \delta_{n}$, 与 $\left(n, \delta_{n}\right)=1$ 矛盾! 从而由归纳原理, 断言成立.

这样,

$$
m=\delta_{n}=\operatorname{lcm}_{1 \leq i \leq k} \delta_{p_{i}^{\alpha_{i}}}=1
$$

矛盾!

再证: 若 $n \notin S$, 则 $n$ 符合条件.

由 $1 \in S \Rightarrow n \geq 2$. 设

$$
n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}
$$

其中 $p_{1}<p_{2}<\cdots<p_{k}$ 为素数, $\alpha_{1}, \cdots, \alpha_{k} \in \mathbb{N}_{+}$. 由 $n \notin S \Rightarrow \exists$ 素数 $q, q<$ $q_{k}$ 且 $q \nmid n$. 记

$$
a_{i}=\left\{\begin{array}{ll}
i+1, & 0 \leq i \leq q-2 \\
0, & i=q-1
\end{array} .\right.
$$

取

$$
p_{1}(x)=\sum_{i=0}^{q-1} a_{i} \prod_{j \neq i}(x-j)(i-j)^{-1} .
$$

其中 $(i-j)^{-1}$ 为 $i-j\left(\bmod p_{k}^{\alpha_{k}}\right)$ 的数论倒数在 $\left\{0,1, \cdots, p_{k}-1\right\}$ 内的取值.由 $p_{k}>q$ 知 $|i-j|<p_{k}$. 由取法,

$$
P_{1}(i) \equiv a_{i} \quad\left(\bmod p_{k}^{\alpha_{k}}\right) .
$$

再取 $M \in \mathbb{N}_{+}$使

$$
M p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k-1}^{\alpha_{k-1}} \equiv 1 \quad\left(\bmod p_{k}^{\alpha_{k}}\right)
$$

记 $\lambda=M p_{1}^{\alpha_{1}} \cdots p_{k-1}^{\alpha_{k-1}}$. 取 $p(x)=\lambda p_{1}(x)$, 下证 $p$ 符合(取 $m=\delta_{n}(P)$ ).

首先, $\left.\frac{n}{p_{k}^{\alpha} k} \right\rvert\, p^{l}(0), \forall l \in \mathbb{N}_{+}$. 故 $\delta_{p_{i}^{\alpha_{i}}}=1(1 \leq i \leq k-1)$. 其次, 归纳易证:

$$
P^{i}(0) \equiv i \quad\left(\bmod p_{k}^{\alpha_{k}}\right)(0 \leq i \leq q-1)
$$

$i=0$ 时显然. 假设 $i-1$ 时成立, $i$ 时 $(i \leq q-1)$,

$$
P^{i}(0) \equiv P\left(P^{i-1}(0)\right) \equiv P(i-1) \equiv P_{1}(i-1) \equiv a_{i-1} \equiv i \quad\left(\bmod p_{k}^{a_{k}}\right),
$$

从而由归纳原理即得.

进一步,

$$
P^{q}(0) \equiv p(q-1) \equiv p_{1}(q-1) \equiv a_{q-1} \equiv 0 \quad\left(\bmod p_{k}^{a_{k}}\right)
$$

故 $\delta_{p_{k} a_{k}}=q$. 从而

$$
\delta_{n}=\operatorname{lcm}_{1 \leq i \leq k} \delta_{p_{i} a_{i}}=q \Rightarrow\left(\delta_{n}, n\right)=1
$$

所以多项式 $P(x)$ 符合条件.

从而所求 $n$ 之集为 $\mathbb{N}_{+} \backslash S$.

评注 考察特例很容易找到解法. $n=p(p \geq 3)$ 与 $n=2,4$ 分别代表两类情况.

6. 设 $P_{1} P_{2} \cdots P_{100}$ 为平面上的圆内接 100 边形. 对正整数 $i$, 定义点 $Q_{i}$ 为对角线 $P_{i-2} P_{i+1}$ 和 $P_{i-1} P_{i+2}$ 的交点, 并规定 $P_{i+100}=P_{i}$. 已知平面上一点 $P$ 使得
$P P_{i} \perp P_{i-1} P_{i+1}$ 对任意正整数 $i$ 成立. 证明: $Q_{1}, Q_{2}, \cdots, Q_{100}$ 共圆.



证明 设 $P P_{i} \cap P_{i-1} P_{i+1}=R_{i}$. 则由 $P P_{i} \perp P_{i-1} P_{i+1}(1 \leq i \leq 100)$ 知,

$$
P R_{i} \cdot P P_{i}=P R_{i+1} \cdot P P_{i+1}
$$

进一步, 对 $1 \leq i \leq 100, P R_{i} \cdot P P_{i}$ 为常数, 设这个常数为 $\gamma$.

断言 $1 R_{1}, R_{2}, \cdots, R_{100}$ 共圆.

证明 由于 $P_{1}, P_{2}, \cdots, P_{100}$ 共圆(记此圆为 $\left.\omega_{1}\right)$. 以 $P$ 为中心, $r$ 为反演幂作一反演 $\varphi$, 则

$$
\varphi\left(P_{i}\right)=R_{i}, \varphi\left(\omega_{1}\right)=\omega_{2}
$$

故 $R_{1}, R_{2}, \cdots, R_{100}$ 共圆 $\omega_{2}$.

断言 $2 Q_{i} Q_{i+1} / / R_{i} R_{i+1},(1 \leq i \leq 100)$.

证明 由 $P_{i}, R_{i}, R_{i+1}, P_{i+1}$ 共圆, $P_{i-1}, P_{i+2}, P_{i+1}, P_{i}$ 共圆知 $\measuredangle\left(P_{i+1} R_{i}, R_{i} R_{i+1}\right)=\measuredangle\left(P_{i+1} P_{i}, P_{i} R_{i+1}\right)=\measuredangle\left(P_{i+1} P_{i-i}, P_{i-1} P_{i+2}\right) \Rightarrow R_{i} R_{i+1} / / P_{i-1} P_{i+2}$.

引理 如果 $\triangle A B C, \triangle X Y Z$ 及平面上一点 $P$ 满足:

$$
\begin{aligned}
& P A \perp Y Z, P B \perp X Z, P C \perp X Y \\
& P X \perp B C, P Y \perp A C, P Z \perp A B,
\end{aligned}
$$

则 $A X, B Y, C Z$ 共点. (字母与原题无关)

证明 记 $Y Z \cap B C=U, X Z \cap A C=V, X Y \cap A B=W$. 设 $A U$ 的中点为 $L, B V$ 的中点为 $M, C W$ 的中点为 $N$, 且设 $P A \cap Y Z=A^{\prime}$, 类似定义



$B^{\prime}, C^{\prime}, X^{\prime}, Y^{\prime}, Z^{\prime}$, 则

$$
P A^{\prime} \cdot P A=P Y^{\prime} \cdot P Y=P C^{\prime} \cdot P C=P X^{\prime} \cdot P X=P B^{\prime} \cdot P B=P Z^{\prime} \cdot P Z
$$

设 $\triangle A B C$ 垂心为 $H$. 考察分别以 $A U, B V, C W$ 为直径的三个圆 $\odot L, \odot M, \odot N$.由 (i) 知 $P$ 到三圆等幕. 又设 $A H \cap B C=D, B H \cap A C=E, C H \cap A B=F$, 则 $D \in \odot L, E \in \odot M, F \in \odot N$. 由

$$
H A \cdot H D=H B \cdot H E=H C \cdot H F \Rightarrow H \text { 到三圆等幂. }
$$

若 $H \equiv P$, 则

$$
A H \perp B C, X H \perp B C \Rightarrow A, H, X \text { 共线. }
$$

对 $B, C$ 同理. 故 $A X, B Y, C Z$ 共点于 $H$, 得证.

若 $H \not \equiv P$, 则

$$
\odot L, \odot M, \odot N \text { 共轴 } P H \Rightarrow L, M, N \text { 共线. }
$$

记此线为 $l$. 下证: $U, V, W$ 共线.

若不然, 设 $U V \cap A B=W^{\prime} \neq W, C W^{\prime}$ 中点为 $N^{\prime}$. 在完全四边形 $(A B, A C$, $B C, U V)$ 中, 由牛顿定理知 $L, M, N^{\prime}$ 共线. 故 $N^{\prime} \in l$. 又 $N^{\prime} \neq N, N N^{\prime}$ 为 $\triangle V W W^{\prime}$ 的中位线, 故 $N N^{\prime} / / A B$, 即 $l / / A B$. 同理,

$$
l / / A C \Rightarrow A B / / l / / A C
$$

但 $A B \cap A C=A$, 矛盾！

故 $U, V, W$ 共线.

对 $\triangle A B C$ 与 $\triangle X Y Z$ 用笛沙格定理,

$$
B C \cap Y Z=U, A C \cap X Z=V, A B \cap X Y=W .
$$

由 $U, V, W$ 共线知 $A X, B Y, C Z$ 共点.

断言 $3 \quad Q_{i-1} Q_{i+1} / / R_{i-1} R_{i+1}(1 \leq i \leq 100)$.

证明 设 $P_{i-1} P_{i-3} \cap P_{i+1} P_{i+3}=Y, P_{i-2} P_{i-3} \cap P_{i+2} P_{i+3}=X$.

考察 $\triangle Y P_{i-1} P_{i+1}$ 与 $\triangle P_{i} P_{i+2} P_{i-2}$ 我们有:

$P P_{i-1} \perp P_{i} P_{i-2}, P P_{i+1} \perp P_{i} P_{i+2}, P P_{i} \perp P_{i-1} P_{i+1}, P P_{i+2} \perp Y P_{i+1}, P P_{i-2} \perp Y P_{i-1}$.

由定差幕线定理, 有 $P Y \perp P_{i+2} P_{i-2}$, 即 $\triangle Y P_{i-1} P_{i+1}$ 与 $\triangle P_{i} P_{i+2} P_{i-2}$ 正交. 这是因为

$$
\begin{aligned}
& P P_{i+2}^{2}-P P_{i-2}^{2}-Y P_{i+2}^{2}+Y P_{i-2}^{2} \\
= & \left(P P_{i+2}^{2}-P P_{i}^{2}\right)+\left(P P_{i}^{2}-P P_{i-2}^{2}\right)+\left(Y P_{i-2}^{2}-Y P_{i+2}^{2}\right) \\
= & \left(P_{i+1} P_{i+2}^{2}-P_{i+1} P_{i}^{2}\right)+\left(P_{i-1} P_{i}^{2}-P_{i-1} P_{i-2}^{2}\right)+\left(Y P_{i-2}^{2}-Y P_{i+2}^{2}\right) \\
= & \left(P_{i+1} P_{i+2}^{2}-Y P_{i+2}^{2}\right)+\left(Y P_{i-2}^{2}-P_{i-2} P_{i-1}^{2}\right)+\left(P_{i-1} P_{i}^{2}-P_{i+1} P_{i}^{2}\right) \\
= & \left(P P_{i+1}^{2}-P Y^{2}\right)+\left(P Y^{2}-P P_{i-1}^{2}\right)+\left(P P_{i-1}^{2}-P P_{i+1}^{2}\right) \\
= & 0 .
\end{aligned}
$$

对 $\triangle Y P_{i-1} P_{i+1}, \triangle P_{i} P_{i+2} P_{i-2}$ 及点 $P$ 用引理知: $P_{i} Y, P_{i-1} P_{i+2}, P_{i+1} P_{i-2}$ 三线共点, 即 $P_{i}, Q_{i}, Y$ 共线.

对 $\omega_{1}$ 内接六边形 $P_{i-1}, P_{i-3}, P_{i-2}, P_{i+1}, P_{i+3}, P_{i+2}$ 用 Pascal 定理,

$$
\begin{aligned}
& P_{i-1} P_{i-3} \cap P_{i+1} P_{i+3}=Y, \\
& P_{i-3} P_{i-2} \cap P_{i+3} P_{i+2}=X, \\
& P_{i-2} P_{i+1} \cap P_{i+2} P_{i-1}=Q_{i} .
\end{aligned}
$$

故 $X, Y, Q_{i}$ 共线. 从而 $P_{i}, Q_{i}, X, Y$ 共线.

对 $\triangle Q_{i-1} P_{i-2} P_{i-3}$ 与 $\triangle Q_{i+1} P_{i+2} P_{i+3}$ 用笛沙格定理,

$$
\begin{gathered}
Q_{i-1} P_{i-2} \cap Q_{i+1} P_{i+2}=Q_{i} \\
Q_{i-1} P_{i-3} \cap Q_{i+1} P_{i+3}=P_{i} \\
P_{i-2} P_{i-3} \cap P_{i+2} P_{i+3}=X .
\end{gathered}
$$

由 $X, P-i, Q_{i}$ 共线 $\Rightarrow Q_{i-1} Q_{i+1}, P_{i-2} P_{i+2}, P_{i-3} P_{i+3}$ 共点于 $W$.
对 $\omega_{1}$ 内接六边形 $P_{i-3}, P_{i+3}, P_{i}, P_{i-2}, P_{i+2}, P_{i-1}$ 用 Pascal 定理,

$$
\begin{aligned}
P_{i-3} P_{i+3} \cap P_{i-2} P_{i+2} & =W, \\
P_{i+3} P_{i} \cap P_{i+2} P_{i-1} & =Q_{i+1}, \\
P_{i} P_{i-2} \cap P_{i-1} P_{i-3} & \equiv U .
\end{aligned}
$$

知 $W, Q_{i+1}, U$ 共线. 同理, $W, Q_{i-1}, V \equiv P_{i} P_{i+2} \equiv P_{i+1} P_{i+3}$ 共线.

故 $W, U, Q_{i-1}, Q_{i+1}, V$ 共线.

仅需再证: $U V / / R_{i-1} R_{i+1}$. 设 $P_{i-1} P, P_{i+1} P$ 与 $\omega_{1}$ 另一交点分别为 $S, T$. 由

$$
P P_{i-1} \cdot P R_{i-1}=\gamma=P P_{i+1} \cdot P R_{i+1}
$$

知 $P_{i-1}, R_{i-1}, R_{i+1}, P_{i+1}$ 共圆. 故

$\measuredangle\left(P R_{i-1}, R_{i-1} R_{i+1}\right)=\measuredangle\left(P_{i-1} P_{i+1}, P_{i+1} R_{i+1}\right)=\measuredangle\left(P_{i-1} S, S T\right) \Rightarrow R_{i-1} R_{i+1} / / S T$.

又导角易有 $\triangle P_{i-1} U R_{i-1} \sim \triangle P_{i-2} R_{i-1} P$, 知

$$
\frac{R_{i-1} U}{R_{i-1} P_{i-1}}=\frac{R_{i-1} P}{R_{i-1} P_{i+2}}
$$

对 $V R_{i+1}$ 有类似式子. 从而

$$
\frac{U R_{i-1}}{V R_{i+1}}=\frac{R_{i-1} P \cdot R_{i-1} P_{i-1}}{R_{i+1} P \cdot R_{i+1} P_{i+1}} \cdot \frac{R_{i+1} P_{i+2}}{R_{i-1} P_{i-2}} .
$$

又

$$
R_{i-1} P_{i-1} \cdot R_{i-1} S=P_{i} R_{i-1} \cdot P_{i-2} R_{i-1}
$$

对 $T$ 也有类似式子. 故

$$
\frac{R_{i-1} P_{i-1}}{R_{i-1} P_{i-2}}=\frac{P_{i} R_{i-1}}{R_{i-1} S}
$$

带入 (ii), 有

$$
\frac{U R_{i-1}}{V R_{i+1}}=\frac{P R_{i-1}}{P R_{i+1}} \cdot \frac{P_{i} R_{i-1}}{R_{i-1} S} \cdot \frac{R_{i+1} T}{p_{i} R_{i+1}}=\frac{P_{i} R_{i-1}}{p_{i} R_{i+1}} \text { (用到 } S T / / R_{i+1} R_{i-1} \text { ). }
$$

故 $U V / / R_{i-1} R_{i+1}$, 得证.

回到原题. 由断言 2,3 知: $\triangle Q_{i-1} Q_{i} Q_{i+1} \sim \triangle R_{i-1} R_{i} R_{i+1}$. $(1 \leq i \leq 100)$ (顺向位似). 由此可归纳证得: 100 边形 $\Omega_{1}: Q_{1} Q_{2} \cdots Q_{100}$ 与 100 边形 $\Omega_{2}$ : $R_{1} R_{2} \cdots R_{100}$ 位似. 又 $\Omega_{2}$ 内接于 $\omega_{2}$, 故 $\Omega_{1}$ 内接于某圆, 得证!

评注 (1). 本题最大的难点是要加强命题. 题目的描述有一种“需要将某性质从 $Q_{i} Q_{i+1} \rightarrow Q_{i+1} Q_{i+2} \rightarrow \cdots \rightarrow Q_{i-1} Q_{i}$ 作传递才能证明断言 3 ”的可能性, 但我们舍弃了这一点. 原题无法作标图, 简化后很容易作图, 从有效性上是很强的.

(2). 本题的引理是“Sondat 定理”(两正交三角形正交中心重合必透视), 其
与条件相容得很好.

(3). 本题与 Poncelet 多边形关系密切. 过 $P_{i}$ 作圆的切线, 切线围出的多边形也共圆. 因此图中有很多射影的共线性质。

