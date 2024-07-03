数学新星网 $\%$ 邹瑾专栏

www.nsmath.cn/zjzl

# 2017 年中国西部数学邀请赛试题与解答 

邹瑾

1. 已知素数 $p$ 和正整数 $n$ 满足: $\prod_{k=1}^{n}\left(k^{2}+1\right)$ 能被 $p^{2}$ 整除. 求证: $p<2 n$.

(王广廷 供题)

证明 按照 $\prod_{k=1}^{n}\left(k^{2}+1\right)$ 中的因子所含 $p$ 的幂次分情况讨论:

(1) 若存在 $k(1 \leq k \leq n)$, 使得 $p^{2} \mid k^{2}+1$. 则 $p^{2} \leq n^{2}+1$, 即

$$
p \leq \sqrt{n^{2}+1}<2 n .
$$

(2) 若对任意的 $k(1 \leq k \leq n), k^{2}+1$ 不能被 $p^{2}$ 整除. 由条件, 知存在 $1 \leq j \neq k \leq n$, 使得 $p \mid\left(j^{2}+1\right)$ 且 $p \mid\left(k^{2}+1\right)$. 则 $p \mid\left(k^{2}-j^{2}\right)$, 即 $p \mid(k-j)(k+j)$.

(1) 若 $p \mid(k-j)$, 则 $p \leq k-j \leq n-1<2 n$;

(2) 若 $p \mid(k+j)$, 则 $p \leq k+j \leq n+n-1=2 n-1<2 n$.

综上可知, $p<2 n$.

评注 这个问题刚开始给出的条件是 $\prod_{k=1}^{n}\left(k^{3}+1\right)$ 能被 $p^{2}$ 整除, 让参赛同学证明 $p<2 n$. 经过命题组讨论, 基于如下两个方面的考虑将条件 $\prod_{k=1}^{n}\left(k^{3}+1\right)$ 改为 $\prod_{k=1}^{n}\left(k^{2}+1\right)$ : 一是作为第一题要降低难度, 二是数论中讨论 $n^{2}+1$ 的因子的问题较多见, 给参赛选手一种亲切感. 其实这两个条件的差别仅仅在于多进行了一次因式分解, 也就是要用到立方和公式.

2. 设 $n$ 是一个正整数, 使得存在正整数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足

$$
x_{1} x_{2} \cdots x_{n}\left(x_{1}+x_{2}+\cdots+x_{n}\right)=100 n
$$

求 $n$ 的最大可能值.

(邹瑾 供题)

解 $n$ 的最大可能值为 9702 .

收稿日期: 2017-08-16.
由已知, $x_{1} x_{2} \cdots x_{n}\left(x_{1}+x_{2}+\cdots+x_{n}\right)=100 n$.

显然 $x_{1}+x_{2}+\cdots+x_{n} \geq 1+1+\cdots+1=n$, 故 $x_{1} x_{2} \cdots x_{n} \leq 100$. 显然等号无法成立, 故 $x_{1} x_{2} \cdots x_{n} \leq 99$. 而

$$
\begin{aligned}
x_{1} x_{2} \cdots x_{n} & =\left[\left(x_{1}-1\right)+1\right]\left[\left(x_{2}-1\right)+1\right] \cdots\left[\left(x_{n}-1\right)+1\right] \\
& \geq\left(x_{1}-1\right)+\left(x_{2}-1\right)+\cdots+\left(x_{n}-1\right)+1 \\
& =x_{1}+x_{2}+\cdots+x_{n}-n+1,
\end{aligned}
$$

故

$$
x_{1}+x_{2}+\cdots+x_{n} \leq x_{1} x_{2} \cdots x_{n}+n-1 \leq n-98 .
$$

于是 $99(n-98) \geq 100 n$, 解得 $n \leq 99 \times 98=9702$.

此时取 $x_{1}=99, x_{2}=x_{3}=\cdots=x_{9702}=1$ 可使等号成立.

3. 如图, 在 $\triangle A B C$ 中, $D$ 为边 $B C$ 上一点, 设 $\triangle A B D$ 和 $\triangle A C D$ 的内心分别为 $I_{1}$ 和 $I_{2}, \triangle A I_{1} D$ 和 $\triangle A I_{2} D$ 的外心分别为 $O_{1}$ 和 $O_{2}$, 直线 $I_{1} O_{2}$ 与 $I_{2} O_{1}$ 交于点 $P$. 求证: $P D \perp B C$.



(张端阳 供题)

证明 因为 $O_{1} A=O_{1} I_{1}=O_{1} D$, 所以由内心的性质, $O_{1}$ 是 $\triangle A B D$ 外接圆弧 $A D$ 的中点. 延长 $B I_{1}, D I_{2}$ 交于点 $J_{1}$, 则 $J_{1}$ 是 $\triangle A B D$ 角 $B$ 内的旁心, 且 $O_{1}$是 $I_{1} J_{1}$ 的中点. 同理, 延长 $D I_{1}, C I_{2}$ 交于点 $J_{2}$, 则 $J_{2}$ 是 $\triangle A C D$ 角 $C$ 内的旁心,且 $O_{2}$ 是 $I_{2} J_{2}$ 的中点.

过 $D$ 作 $D P^{\prime} \perp B C$ ，只需证明 $I_{1} O_{2}, I_{2} O_{1}, D P^{\prime}$ 三线共点. 对 $\triangle D I_{1} I_{2}$ 用角元塞瓦定理知, 只需证明

$$
\frac{\sin \angle P^{\prime} D I_{2}}{\sin \angle P^{\prime} D I_{1}} \cdot \frac{\sin \angle D I_{1} O_{2}}{\sin \angle O_{2} I_{1} I_{2}} \cdot \frac{\sin \angle O_{1} I_{2} I_{1}}{\sin \angle D I_{2} O_{1}}=1 .
$$

事实上, 由 $O_{2} J_{2}=O_{2} I_{2}$ 知 $S_{\triangle O_{2} I_{1} J_{2}}=S_{\triangle O_{2} I_{1} I_{2}}$,所以

$$
\frac{\sin \angle D I_{1} O_{2}}{\sin \angle O_{2} I_{1} I_{2}}=\frac{\sin \angle O_{2} I_{1} J_{2}}{\sin \angle O_{2} I_{1} I_{2}}=\frac{\frac{2 S_{\triangle O_{2} I_{1} J_{2}}}{I_{1} J_{2} \cdot I_{1} O_{2}}}{\frac{2 S_{\triangle O_{2} I_{1} I_{2}}}{I_{1} I_{2} \cdot I_{1} O_{2}}}=\frac{I_{1} I_{2}}{I_{1} J_{2}}
$$



同理, $\frac{\sin \angle O_{1} I_{2} I_{1}}{\sin \angle D I_{2} O_{1}}=\frac{I_{2} J_{1}}{I_{1} I_{2}}$. 又 $\frac{\sin \angle P^{\prime} D I_{2}}{\sin \angle P^{\prime} D I_{1}}=\frac{\cos \angle C D I_{2}}{\cos \angle B D I_{1}}$, 所以只需证明

$$
\frac{I_{2} J_{1} \cdot \cos \angle C D I_{2}}{I_{1} J_{2} \cdot \cos \angle B D I_{1}}=1
$$

即 $I_{2} J_{1}$ 和 $I_{1} J_{2}$ 在 $B C$ 上的投影长度相同.
设 $I_{1}, I_{2}, J_{1}, J_{2}$ 在 $B C$ 上的投影分别为 $H_{1}, H_{2}, K_{1}, K_{2}$, 则

$$
\begin{aligned}
H_{2} K_{1} & =D K_{1}-D H_{2} \\
& =\frac{1}{2}(A B+A D-B D)-\frac{1}{2}(A D+C D-A C) \\
& =\frac{1}{2}(A B+A C-B C)
\end{aligned}
$$



同理, $H_{1} K_{2}=\frac{1}{2}(A B+A C-B C)$. 所以 $H_{2} K_{1}=H_{1} K_{2}$, 命题得证.

评注 本题有如下的等价形式:

如图, $\odot O_{1}$ 与 $\odot O_{2}$ 交于 $A, B$ 两点, 过 $A$ 作两条垂直的射线分别与 $\odot O_{1}, \odot O_{2}$ 交于点 $C, D$. 设直线 $D O_{1}, C O_{2}$ 交于点 $P$, 则 $\angle P A D=\angle B A C$.

读者可自行证明这两种形式的等价性.



4. 给定整数 $n, k, n \geq k \geq 2$. 甲、乙两人在一张每个小方格都是白色的 $n \times n$ 的方格纸上玩游戏: 两人轮流选择一个白色小方格将其染为黑色，甲先进行. 如果某个人染色后, 每个 $k \times k$ 的正方形中都至少有一个黑色小方格, 则游戏结束, 此人获胜. 问谁有必胜策略?

(翟振华 供题)

解 将方格纸按从上到下标记行, 从左到右标记列.

若 $n \leq 2 k-1$, 则甲将第 $k$ 行第 $k$ 列的小方格染为黑色后, 每个 $k \times k$ 正方形中至少有一个黑格, 因此甲获胜.

下面假设 $n \geq 2 k$. 我们证明当 $n$ 是奇数时, 甲有获胜策略: 当 $n$ 是偶数时,乙有获胜策略.

对于一个已经有若干个方格染为黑色的局面: 如果有两个不相交的 $k \times k$正方形所含的全是白格, 并且方格纸内白格总数为奇数, 我们称其为 “好局面” ; 如果有两个不相交的 $k \times k$ 正方形所含的全是白格, 并且方格纸内白格总数为偶数, 称其为 “坏局面”.

我们证明当某人面对好局面时, 他有获胜策略.

假设甲面对好局面, 他先取定两个不相交的 $k \times k$ 正方形 $A$ 和 $B$, 其中都是白格. 由于白格总数为奇数, 可选取不在 $A, B$ 中的另一个白格, 将它染为黑色,此时白格总数为偶数, 且 $A, B$ 中仍然都是白格, 因此变为一个坏局面.

轮到乙面对坏局面, 如果他染色后, 仍有两个不相交的 $k \times k$ 正方形中都是白格, 此时白格总数是奇数, 又回到好局面. 如果他染色后, 不存在两个
不相交的 $k \times k$ 正方形, 注意到此时至少有一个全白格的 $k \times k$ 正方形, 设 $A_{1}, \cdots, A_{m}$ 是所有全白格的 $k \times k$ 正方形, 则它们两两相交, 故必包含于某个 $(2 k-1) \times(2 k-1)$ 的正方形 $S$, 因此 $S$ 的中心方格 $P$ 是 $A_{1}, \cdots, A_{m}$ 的公共格.这样甲将 $P$ 染为黑色后, 所有 $k \times k$ 正方形中都含有黑格, 于是甲获胜.

总之, 当某人面对好局面时, 他可以在自己的下一回合获胜或是仍面对好局面, 而游戏必在有限步内结束, 因此他有获胜策略. 由上述论证亦可知, 当某人面对坏局面时, 他要么让对方下一回合即可获胜, 要么留给对方好局面, 因此对方有获胜策略. 在 $n \geq 2 k$ 时, 由于四个角上的 $k \times k$ 正方形互不相交, 且一开始都是白格, 因此当 $n$ 是奇数时,一开始是好局面, 甲有获胜策略; 当 $n$ 是偶数时,一开始是坏局面, 乙有获胜策略.

5. 设 9 个正整数 $a_{1}, a_{2}, \cdots, a_{9}$ (可以相同), 满足: 对任意 $1 \leq i<j<k \leq 9$,都存在与 $i, j, k$ 不同的 $l, 1 \leq l \leq 9$, 使得 $a_{i}+a_{j}+a_{k}+a_{l}=100$. 求满足上述要求的有序 9 元数组 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$ 的个数.

(何忆捷 供题)

解 对满足条件的正整数组 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$, 将 $a_{1}, a_{2}, \cdots, a_{9}$ 从小到大排列为 $b_{1} \leq b_{2} \leq \cdots \leq b_{9}$. 由条件知, 分别存在 $l \in\{4,5, \cdots, 9\}$ 及 $l^{\prime} \in\{1,2, \cdots, 6\}$,使得

$$
b_{1}+b_{2}+b_{3}+b_{l}=b_{l^{\prime}}+b_{7}+b_{8}+b_{9}=100
$$

注意到

$$
b_{l^{\prime}} \geq b_{1}, \quad b_{7} \geq b_{2}, \quad b_{8} \geq b_{3}, \quad b_{9} \geq b_{l}
$$

结合 (1) 知, (2) 中的不等号均为等号, 故 $b_{2}=b_{3}=\cdots=b_{8}$.

因此可设 $\left(b_{1}, b_{2}, \cdots, b_{9}\right)=(x, y \cdots, y, z)$, 其中 $x \leq y \leq z$.

由条件知, 使 $x+y+z+b_{l}=100$ 的 $b_{l}$ 的值只能是 $y$, 即

$$
x+2 y+z=100 \text {. }
$$

(1) 当 $x=y=z=25$ 时, 有 $\left(b_{1}, b_{2}, \cdots, b_{9}\right)=(25,25, \cdots, 25)$, 此时得到一组 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$.

(2) 当 $x, z$ 中恰有一个等于 $y$ 时, 记另一个为 $w$, 由 (3) 知 $w+3 y=100$.该条件也是充分的. 此时 $y$ 可以取 $1,2, \cdots, 24,26,27, \cdots, 33$ 这 32 种不同值,每个 $y$ 值对应一组 $\left(b_{1}, b_{2}, \cdots, b_{9}\right)$, 进而对应 9 组不同的 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$, 共有 $32 \times 9=288$ 个数组 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$.

(3) 当 $x<y<z$ 时, 由条件知, 存在某个 $b_{l} \in\{x, y, z\}$, 使得 $3 y+b_{l}=100$,与 (3) 比较知, $y+b_{l}=x+z$, 故必有 $b_{l}=y$, 进而 $y=25, x+z=50$. 该条件也是充分的. 此时, 对 $x=1,2, \cdots, 24$, 每个 $x$ 值对应一组 $\left(b_{1}, b_{2}, \cdots, b_{9}\right)$, 进而对应 $9 \times 8=72$ 组不同的 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$, 共有 $24 \times 72=1728$ 个数组 $\left(a_{1}, a_{2}, \cdots, a_{9}\right)$.

综合 (1), (2), (3) 知, 符合条件的数组个数是 $1+288+1728=2017$.

6. 如图, 在锐角 $\triangle A B C$ 中, 点 $D 、 E$ 分别在边 $A B 、 A C$ 上, 线段 $B E 、 D C$ 交于点 $H$, 点 $M 、 N$ 分别为线段 $B D 、 C E$ 的中点. 证明: 点 $H$ 为 $\triangle A M N$ 的垂心的充要条件是 $B 、 C 、 E 、 D$ 四点共圆且 $B E \perp C D$.



(石泽晖 供题)

证明 延长 $M H$ 交 $A C$ 于点 $P$, 延长 $N H$ 交 $A B$ 于点 $Q$.

先证明充分性：由于 $B 、 C 、 E 、 D$ 四点共圆，故 $\angle B D H=\angle C E H$. 又 $B E \perp C D$, 从而 $\triangle D H B 、 \triangle E H C$均为直角三角形, 注意到点 $M 、 N$ 分别为斜边 $B D 、 C E$的中点, 故 $\angle M D H=\angle M H D, \angle M H B=\angle M B H$. 从而

$$
\begin{aligned}
\angle E H P+\angle H E C & =\angle M H B+\angle H D B \\
& =\angle M B H+\angle H D B=90^{\circ},
\end{aligned}
$$



即 $M H \perp A C$. 同理 $N H \perp A B$, 从而点 $H$ 为 $\triangle A M N$ 的垂心.

再证明必要性: 若点 $H$ 为 $\triangle A M N$ 的垂心, 则 $M P \perp A N, N Q \perp A M$, 从而

$$
\frac{D Q}{Q B}=\frac{D H \cdot \sin \angle D H Q}{B H \cdot \angle B H Q}=\frac{D H \cdot \sin \angle C H N}{B H \cdot \sin \angle E H N}=\frac{D H \cdot E H}{B H \cdot C H} .
$$

同理 $\frac{E P}{P C}=\frac{D H \cdot E H}{B H \cdot C H}$, 故 $\frac{E P}{P C}=\frac{D Q}{Q B}$. 利用比例性质及 $D M=M B, E N=N C$可知:

$$
\frac{E C}{P C}=\frac{D B}{Q B} \Rightarrow \frac{N C}{P C}=\frac{M B}{Q B} \Rightarrow \frac{N C}{P N}=\frac{M B}{Q M} \Rightarrow \frac{E N}{P N}=\frac{D M}{Q M}
$$

又因为点 $H$ 为 $\triangle A M N$ 的垂心, 故 $\angle D M H=\angle E N H$, 从而有 $\frac{Q M}{M H}=$ $\frac{P N}{N H}$, 因此 $\frac{D M}{M H}=\frac{E N}{N H}$, 从而 $\triangle D M H \sim \triangle E N H$, 故 $\angle M D H=\angle N E H$, 因此 $B 、 C 、 E 、 D$ 四点共圆.

设 $B C E D$ 的外心为 $O$, 易知 $O M \perp A B$, 从而 $O M / / N H$, 同理 $O N / / M H$,故四边形 $M H N O$ 为平行四边形, 因此 $M H=O N$. 过点 $B$ 作 $M H$ 平行线交 $D C$ 于 $X$, 注意到 $M$ 为 $A B$ 中点, 故 $B X=2 M H=2 O N$, 由熟知的外心性质
可知 $X$ 为 $\triangle B C E$ 的垂心, 从而 $C X \perp B D$, 即 $A C \perp B D$.

7. 设正整数 $n=2^{\alpha} \cdot q$, 其中 $\alpha$ 为非负整数, $q$ 为奇数. 证明: 对任意正整数 $m$, 方程 $x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=m$ 的整数解 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的个数能被 $2^{\alpha+1}$ 整除.

(王广廷供题)

证法一 设方程 $x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=m$ 的解的个数为 $N(m)$. 设 $\left(x_{1}, x_{2}\right.$, $\left.\cdots, x_{n}\right)$ 是方程 $x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=m$ 的一个非负整数解. 不妨设其中有 $k$ 个非零项, 注意到 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 的每个分量有正负两种情况, 则恰好对应原方程的 $2^{k}$ 个整数解. 设 $S_{k}$ 是该方程的恰有 $k(k=1,2, \cdots, n)$ 个非零项的非负整数解的个数. 则

$$
N(m)=\sum_{k=1}^{n} 2^{k} \cdot S_{k}
$$

因为 $k$ 个非零项的非负整数解有 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 种位置可选, 故 $\left.\left(\begin{array}{l}n \\ k\end{array}\right) \right\rvert\, S_{k}$.

故要证明 $2^{\alpha+1} \mid N(m)$, 只需证明: $2^{\alpha-k+1} \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$.

注意到 $\left(\begin{array}{l}n \\ k\end{array}\right)=\frac{n(n-1) \cdots(n-k+1)}{k !}$, 分子中 2 的因子个数至少为 $\alpha$, 而分母中的 2 的因子个数为

$$
\sum_{i=1}^{\left[\log _{2} k\right]}\left[\frac{k}{2^{i}}\right]<\sum_{i=1}^{\infty} \frac{k}{2^{i}}=k
$$

故分母的 2 的因子至多有 $k-1$ 个, 所以 $2^{\alpha-k+1} \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$. 即 $2^{\alpha-k+1} \mid N(m)$.

评注 这个问题中要证明 $2^{\alpha-k+1} \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$, 实际也可以用 Kummer 定理处理. Kummer 定理是指: 设 $n, i$ 是正整数且 $i \leq n, p$ 是素数, 则 $p^{t} \|\left(\begin{array}{l}n \\ k\end{array}\right)$ 当且仅当在 $p$进制中, $(n-i)+i$ 发生了至多 $t(t \geq 0)$ 次进位.

证法二 记 $f(n, m)$ 为该方程整数解的个数. 首先证明如下关于 $f(n, m)$ 的递推关系:

引理 $f(2 n, m)=2 f(n, m)+\sum_{k=1}^{m-1} f(n, k) f(n, m-k)$.

引理证明 设 $\left(x_{1}, x_{2}, \cdots, x_{2 n}\right)$ 是方程 $x_{1}^{2}+x_{2}^{2}+\cdots+x_{2 n}^{2}=m$ 的一个解. 设

$$
x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=k .
$$

若 $k=0$, 则 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)=(0,0, \cdots, 0)$, 且 $x_{n+1}^{2}+x_{n+2}^{2}+\cdots+x_{2 n}^{2}=m$,这样的 $\left(x_{n+1}, x_{n+2}, \cdots, x_{2 n}\right)$ 有 $f(n, m)$ 组. 故当 $k=0$ 时, 原方程有 $f(n, m)$ 组解.

同理可知, 当 $k=m$ 时, 原方程也有 $f(n, m)$ 组解.

当 $1 \leq k \leq m-1$ 且 $k$ 为正整数时, 方程 $x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=k$ 有 $f(n, k)$
个解, 方程 $x_{n+1}^{2}+x_{n+2}^{2}+\cdots+x_{2 n}^{2}=m-k$ 有 $f(n, m-k)$ 个解. 由此可得方程 $x_{1}^{2}+x_{2}^{2}+\cdots+x_{2 n}^{2}=m$ 有 $f(n, k) f(n, m-k)$ 组解.

综上可知,

$$
f(2 n, m)=2 f(n, m)+\sum_{k=1}^{m-1} f(n, k) f(n, m-k) .
$$

回到原题. 下面证明当 $n=2^{\alpha} \cdot q$ 时, 有 $2^{\alpha+1} \mid f(n, m)$.

对 $\alpha$ 进行归纳.

当 $\alpha=0$ 时, 由于对原方程的任意一组解 $\left(x_{1}, x_{2}, \cdots, x_{n}\right),\left(-x_{1},-x_{2}, \cdots\right.$, $\left.-x_{n}\right)$ 也是该方程的一组解. 由于 $m$ 是正整数, 因此, $x_{1}, x_{2}, \cdots, x_{n}$ 不全为零.故 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 和 $\left(-x_{1},-x_{2}, \cdots,-x_{n}\right)$ 是不同的两个解. 于是原方程的解可以两两配对. 故

$$
2=2^{0+1} \mid f(n, m)
$$

假设 (1) 对 $\alpha$ 成立, 下面考虑 $\alpha+1$ 的情形. 注意到

$$
f(n, m)=2 f\left(\frac{n}{2}, m\right)+\sum_{k=1}^{m-1} f\left(\frac{n}{2}, k\right) f\left(\frac{n}{2}, m-k\right) .
$$

注意到此时 $n=2^{\alpha+1} \cdot q$, 故 $\frac{n}{2}=2^{\alpha} \cdot q$. 因此由归纳假设, 知 $2^{\alpha+1}$ 分别整除 $f\left(\frac{n}{2}, m\right), f\left(\frac{n}{2}, k\right), f\left(\frac{n}{2}, m-k\right)$, 故

$$
2^{\alpha+2}\left|2 f\left(\frac{n}{2}, m\right), 2^{2(\alpha+1)}\right| \sum_{k=1}^{m-1} f\left(\frac{n}{2}, k\right) f\left(\frac{n}{2}, m-k\right) .
$$

由于 $2(\alpha+1) \geq \alpha+2$, 因此 $2^{\alpha+2} \mid f(n, m)$.

综上可知, (1) 式成立. 所以原问题得证.

8. 设整数 $n \geq 2$, 证明：对任意正实数 $a_{1}, a_{2}, \cdots, a_{n}$, 都有

$$
\sum_{i=1}^{n} \max \left\{a_{1}, a_{2}, \cdots, a_{i}\right\} \cdot \min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\} \leq \frac{n}{2 \sqrt{n-1}} \cdot \sum_{i=1}^{n} a_{i}^{2} .
$$

(张端阳 供题)

证明 对 $n$ 用第二数学归纳法.

当 $n=2$ 时, 左式 $=a_{1} \cdot \min \left\{a_{1}, a_{2}\right\}+\max \left\{a_{1}, a_{2}\right\} \cdot a_{2}$.

若 $a_{1} \geq a_{2}$, 则原式等价于 $2 a_{1} a_{2} \leq a_{1}^{2}+a_{2}^{2}$, 命题成立;

若 $a_{1} \leq a_{2}$, 则原式等价于 $a_{1}^{2}+a_{2}^{2} \leq a_{1}^{2}+a_{2}^{2}$, 命题成立.

假设命题对所有大于等于 2 且小于 $n$ 的正整数成立, 来看 $n$ 时的情形.

对 $2 \leq i \leq n$, 记 $c_{i}=\frac{i}{2 \sqrt{i-1}}$, 再令 $c_{1}=1$, 容易验证 $c_{1}=c_{2}<c_{3}<\cdots<c_{n}$.
记 $M=\max \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 并设 $a_{k}=M$.

当 $k=1$ 时, 原式 $=M \sum_{i=1}^{n} \min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\}$. 因为

$$
\min \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}=\min \left\{a_{2}, \cdots, a_{n}\right\} \leq \frac{1}{n-1} \sum_{i=2}^{n} a_{i}
$$

且当 $2 \leq i \leq n$ 时, $\min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\} \leq a_{i}$, 所以

$$
\sum_{i=1}^{n} \min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\} \leq \frac{1}{n-1} \sum_{i=2}^{n} a_{i}+\sum_{i=2}^{n} a_{i}=\frac{n}{n-1} \sum_{i=2}^{n} a_{i}
$$

由均值不等式,

$$
\begin{aligned}
\text { 原式 } & \leq \frac{n}{n-1} M \sum_{i=2}^{n} a_{i} \leq \frac{n}{2 \sqrt{n-1}}\left[M^{2}+\frac{1}{n-1}\left(\sum_{i=2}^{n} a_{i}\right)^{2}\right] \\
& \leq \frac{n}{2 \sqrt{n-1}}\left(M^{2}+\sum_{i=2}^{n} a_{i}^{2}\right)=\frac{n}{2 \sqrt{n-1}} \sum_{i=1}^{n} a_{i}^{2} .
\end{aligned}
$$

当 $k=n$ 时, $\min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\}=\min \left\{a_{i}, a_{i+1}, \cdots, a_{n-1}\right\}$, 所以

$$
\text { 原式 }=\sum_{i=1}^{n-1} \max \left\{a_{1}, a_{2}, \cdots, a_{i}\right\} \cdot \min \left\{a_{i}, a_{i+1}, \cdots, a_{n-1}\right\}+M^{2} \text {. }
$$

由归纳假设，

$$
\sum_{i=1}^{n-1} \max \left\{a_{1}, a_{2}, \cdots, a_{i}\right\} \cdot \min \left\{a_{i}, a_{i+1}, \cdots, a_{n-1}\right\} \leq c_{n-1} \sum_{i=1}^{n-1} a_{i}^{2}
$$

所以

原式 $\leq c_{n-1} \sum_{i=1}^{n-1} a_{i}^{2}+M^{2}<\frac{n}{2 \sqrt{n-1}}\left(\sum_{i=1}^{n-1} a_{i}^{2}+M^{2}\right)=\frac{n}{2 \sqrt{n-1}} \sum_{i=1}^{n} a_{i}^{2}$.

当 $2 \leq k \leq n-1$ 时, 结合 $k=1$ 和 $k=n$ 时的证明得,

原式 $=\sum_{i=1}^{k-1} \max \left\{a_{1}, a_{2}, \cdots, a_{i}\right\} \cdot \min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\}+M \sum_{i=k}^{n} \min \left\{a_{i}, a_{i+1}, \cdots, a_{n}\right\}$

$\leq \sum_{i=1}^{k-1} \max \left\{a_{1}, a_{2}, \cdots, a_{i}\right\} \cdot \min \left\{a_{i}, a_{i+1}, \cdots, a_{k-1}\right\}+\frac{n-k+1}{n-k} M \sum_{i=k+1}^{n} a_{i}$

$\leq c_{k-1} \sum_{i=1}^{k-1} a_{i}^{2}+\frac{n-k+1}{2 \sqrt{n-k}}\left(M^{2}+\sum_{i=k+1}^{n} a_{i}^{2}\right)$

$=c_{k-1} \sum_{i=1}^{k-1} a_{i}^{2}+c_{n-k+1} \sum_{i=k}^{n} a_{i}^{2}<\frac{n}{2 \sqrt{n-1}} \sum_{i=1}^{n} a_{i}^{2}$.

综上, 命题得证.

评注 取 $a_{1}=\sqrt{n-1}, a_{2}=\cdots=a_{n}=1$ 可知, 常数 $\frac{n}{2 \sqrt{n-1}}$ 是最佳的.

