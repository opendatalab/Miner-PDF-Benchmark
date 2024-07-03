数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2018 年春季上海新星数学奥林匹克试题解析 

吴尉迟 ${ }^{1}$ 罗振华 ${ }^{2}$ 叶思 ${ }^{1}$

(1. 上海大学数学系, $200444 ; 2$. 上海四季教育, 200070)

2018 年春季上海新星数学奥林匹克于 2018 年 4 月 25 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答.

## I. 试 题

1. 设正整数 $n \geq 2$, 非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{i=1}^{n} x_{i}=n$. 求

$$
\left(\sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor\right)\left(\sum_{i=1}^{n}\left\{x_{i}\right\}\right)
$$

的最大值, 其中 $\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数, $\{x\}=x-\lfloor x\rfloor$.

(中国人民大学附属中学 张端阳 供题)

2. 圆 $\Gamma_{1}$ 与圆 $\Gamma_{2}$ 交于 $P, Q$ 两点. 直线 $l$ 是过点 $P$ 的动直线, $l$ 与圆 $\Gamma_{1}$ 的另一个交点为 $A, l$ 与圆 $\Gamma_{2}$ 的另一个交点为 $B(A, B$ 都不同于 $P)$. 过 $A, B$ 分别作圆 $\Gamma_{1}$ 与圆 $\Gamma_{2}$ 的切线, 这两条切线交于点 $C$. 当直线 $l$ 绕 $P$ 旋转一圈时, 求 $\triangle A B C$ 的外心 $O$ 的轨迹.

(上海大学 吴尉迟 叶思 供题)

3. 一座城堡的周围有 $n$ 个军事要塞和 $n$ 个瞭望点, 这些要塞和瞭望点都分布在同一个圆周上. 每个瞭望点安排一名士兵值班, 在某个时间段内, $n$ 个士兵先后沿圆周按逆时针方向运动到最近的一个未接收报告的要塞报告观测到的情况, 其中每个要塞只听取一个士兵的报告, 每次都是当一个士兵报告完毕之后另一个士兵才出发进行下一次报告. 证明: 不管士兵以何种次序出发, 各个士兵

收稿日期: 2018-04-29.
运动的路程之和是定值.

(深圳高级中学 冯跃峰 供题)

4. (1) 设 $\alpha, n, k$ 是正整数, $n \geq k, p$ 是素数, 且满足 $p^{\alpha} \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$, 证明: $p^{\alpha} \leq n$.

(2) 设正整数 $n, k$ 满足 $n \geq k^{2} \geq 64$, 证明: $\left(\begin{array}{l}n \\ k\end{array}\right)$ 有一个大于 $k$ 的素因子.

(上海四季教育 罗振华 供题)
5. $\odot O_{1}$ 与 $\odot O_{2}$ 交于 $A, B$ 两点, 过 $A$ 的直线分别交 $\odot O_{1}, \odot O_{2}$ 于点 $C, D$,满足 $O_{1}, O_{2}, C, D$ 四点共圆, 记该圆为 $\Gamma$. 设 $E$ 是 $C O_{2}$ 与 $D O_{1}$ 的交点, $I$ 是线段 $B E$ 与圆 $\Gamma$ 的交点. 证明: $I$ 是 $\triangle C B O_{2}$ 和 $\triangle D B O_{1}$ 的内心.

(中国人民大学附属中学 张端阳 供题)
6. $n$ 是给定的正整数. 对于 $n$ 元数组 $\bar{a}=\left(a_{1}, \cdots, a_{n}\right)$, 记

$$
S(\bar{a})=\sum_{i=1}^{n} 3^{i-1} a_{i}, \quad T(\bar{a})=\sum_{i=1}^{n} \frac{a_{i}}{3^{i-1}} .
$$

设 $m, k$ 是正整数且满足 $m \geq 2 k$, 定义

$$
A=\left\{\bar{a}=\left(a_{1}, \cdots, a_{n}\right) \mid k=S(\bar{a}) \text {, 其中 } a_{i} \in \mathbb{Z},\left|a_{i}\right| \leq m, i=1, \cdots, n\right\} \text {. }
$$

证明:

$$
\frac{\sum_{\bar{a} \in A} T(\bar{a})}{|A|} \leq k
$$

其中 $|A|$ 表示 $A$ 的元素个数.

(哈佛大学 吴昊 供题)

## II. 解 答

题 1. 设正整数 $n \geq 2$, 非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{i=1}^{n} x_{i}=n$. 求

$$
\left(\sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor\right)\left(\sum_{i=1}^{n}\left\{x_{i}\right\}\right)
$$

的最大值, 其中 $\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数, $\{x\}=x-\lfloor x\rfloor$.

解 当 $n$ 是偶数时, 由均值不等式,

$$
\begin{aligned}
\left(\sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor\right)\left(\sum_{i=1}^{n}\left\{x_{i}\right\}\right) & \leq\left(\sum_{i=1}^{n}\left(\left\lfloor x_{i}\right\rfloor+\left\{x_{i}\right\}\right)\right)^{2} \\
& =\frac{1}{4}\left(\sum_{i=1}^{n} x_{i}\right)^{2}=\frac{n^{2}}{4} .
\end{aligned}
$$

当 $x_{1}=\cdots=x_{\frac{n}{2}}=\frac{1}{2}, x_{\frac{n}{2}+1}=\cdots=x_{n}=\frac{3}{2}$ 时可以取到等号.

当 $n$ 是奇数时,

$$
\begin{aligned}
& \left(\sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor\right)\left(\sum_{i=1}^{n}\left\{x_{i}\right\}\right)^{2} \\
= & \frac{1}{4}\left(\sum_{i=1}^{n}\left(\left\lfloor x_{i}\right\rfloor+\left\{x_{i}\right\}\right)\right)^{2}-\frac{1}{4}\left(\sum_{i=1}^{n}\left(\left\lfloor x_{i}\right\rfloor-\left\{x_{i}\right\}\right)\right)^{2} \\
= & \frac{1}{4}\left(\sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor\right)^{2}-\frac{1}{4}\left(2 \sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor-\sum_{i=1}^{n} x_{i}\right)^{2} \\
= & \frac{n^{2}}{4}-\frac{1}{4}\left(2 \sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor-n\right)^{2} \\
\leq & \frac{n^{2}-1}{4}
\end{aligned}
$$

最后不等号是因为 $2 \sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor$ 是偶数, $n$ 是奇数, 所以 $\left|2 \sum_{i=1}^{n}\left\lfloor x_{i}\right\rfloor-n\right| \geq 1$. 且当 $x_{1}=\cdots=x_{\frac{n-1}{2}}=\frac{1}{2}, x_{\frac{n+1}{2}}=1, x_{\frac{n+3}{2}}=\cdots=x_{n}=\frac{3}{2}$ 时可以取到等号.

综上, 所求最大值当 $n$ 是偶数时为 $\frac{n^{2}}{4}$, 当 $n$ 是奇数时为 $\frac{n^{2}-1}{4}$.

评注 此题是一道简单而优雅的代数题, 考试中绝大多数同学做对了此题.

题 2. 圆 $\Gamma_{1}$ 与圆 $\Gamma_{2}$ 交于 $P, Q$ 两点. 直线 $l$ 是过点 $P$ 的动直线, $l$ 与圆 $\Gamma_{1}$ 的另一个交点为 $A, l$ 与圆 $\Gamma_{2}$ 的另一个交点为 $B(A, B$ 都不同于 $P)$. 过 $A, B$ 分别作圆 $\Gamma_{1}$ 与圆 $\Gamma_{2}$ 的切线, 这两条切线交于点 $C$. 当直线 $l$ 绕 $P$ 旋转一圈时, 求 $\triangle A B C$ 的外心 $O$ 的轨迹.

解 设 $\triangle Q O_{1} O_{2}$ 的外接圆为 $\Gamma$, 我们证明 $O$ 的轨迹是 $\Gamma \backslash\left\{Q, O_{1}, O_{2}\right\}$.



先证明 $O$ 在 $\Gamma \backslash\left\{Q, O_{1}, O_{2}\right\}$ 上.

为此只须证明 $O, O_{1}, Q, O_{2}$ 四点共圆. 事实上, 由 $A C, B C$ 分别是圆 $\Gamma_{1}, \Gamma_{2}$的切线知, $\angle C A B=\angle A Q P, \angle C B A=\angle B Q P$. 从而

$$
\angle A C B=\pi-\angle C A B-\angle C B A=\pi-(\angle A Q P+\angle B Q P)=\pi-\angle A Q B
$$

故 $C, A, Q, B$ 四点共圆, 这说明 $O$ 也是 $\triangle A Q B$ 的外心, 因此 $O A=O Q=O B$.又 $O_{1} A=O_{1} Q, O_{2} Q=O_{2} B$, 所以

$$
O O_{1} \perp A Q, O O_{2} \perp B Q
$$

则 $\angle O_{1} O O_{2}=\pi-\angle A Q B$. 又

$$
\angle O_{1} Q A=\frac{\pi}{2}-\frac{\angle A O_{1} Q}{2}=\frac{\pi}{2}-\angle A P Q=\frac{\pi}{2}-\frac{\angle B O_{2} Q}{2}=\angle O_{2} Q B
$$

故 $\angle A Q B=\angle O_{1} Q O_{2}$. 从而 $\angle O_{1} O O_{2}=\pi-\angle Q_{1} Q O_{2}$, 所以 $O, O_{1}, Q, O_{2}$ 四点共圆.

当直线 $l$ 逼近 $\Gamma_{2}$ 过 $P$ 点的切线时, $O$ 趋于 $O_{1}$. 但直线 $l$ 不能为 $\Gamma_{2}$ 过 $P$ 点的切线 (此时 $P, B$ 重合), 故 $O$ 不能取到 $O_{1}$. 同理, $O$ 不能取到 $O_{2}$.

当直线 $l$ 逼近直线 $P Q$ 时, $O$ 趋于 $Q$. 但直线 $l$ 不能为直线 $P Q$ (此时 $A, B$重合), 故 $O$ 不能取到 $Q$.

从而 $(*)$ 得证.

另一方面, 当 $O \in \Gamma \backslash\left\{Q, O_{1}, O_{2}\right\}$ 时, 我们找一条经过点 $P$ 的直线 $l$, 使得 $O$为 $\triangle A B C$ 的外心. 过 $Q$ 作 $O O_{1}$ 的垂线交圆 $\Gamma_{1}$ 于 $A$, 过 $Q$ 作 $O O_{2}$ 的垂线交圆 $\Gamma_{2}$ 于 $B(A, B$ 均不同于 $Q)$.

由于 $O_{1} A=O_{1} Q, O O_{1} \perp A Q$, 所以 $O A=O Q$. 同理 $O B=O Q$. 所以 $O$ 是 $\triangle A Q B$ 的外心.
先证 $A, P, B$ 三点共线. 因为 $O O_{1} \perp Q A, O O_{2} \perp Q B$, 所以 $\angle A Q B=$ $\pi-\angle O_{1} O O_{2}$. 又 $O, O_{1}, Q, O_{2}$ 四点共圆, 所以 $\angle O_{1} Q O_{2}=\pi-\angle O_{1} O O_{2}$. 故 $\angle A Q B=O_{1} Q O_{2}$, 则

$$
\angle A Q O_{1}=\angle B Q O_{2}, \angle A P Q=\frac{\pi}{2}-\angle O_{1} Q A, \angle B P Q=\frac{\pi}{2}+\angle O_{1} Q A .
$$

所以 $\angle A P Q+\angle B P Q=\pi$, 则 $A, P, B$ 三点共线.

取直线 $l$ 为直线 $A P B$. 过 $A, B$ 分别做 $\Gamma_{1}, \Gamma_{2}$ 的切线, 这两条切线交于点 $C$.与 $(*)$ 中的证明类似可得 $C, A, Q, B$ 四点共圆. 又因为 $O$ 是 $\triangle A Q B$ 的外心, 所以 $O$ 也是 $\triangle A B C$ 的外心.

综上可知, $O$ 的轨迹是 $\Gamma \backslash\left\{Q, O_{1}, O_{2}\right\}$.

评注 此题为轨迹问题. 此类题目在中国的比赛中很少出现, 其难点在于如何发现 $O$ 的轨迹是 $\Gamma \backslash\left\{Q, O_{1}, O_{2}\right\}$. 考试中很多同学没有证明轨迹的纯粹性, 即证明 $\Gamma \backslash\left\{Q, O_{1}, O_{2}\right\}$ 上的点都满足条件.

题 3. 一座城堡的周围有 $n$ 个军事要塞和 $n$ 个瞭望点, 这些要塞和瞭望点都分布在同一个圆周上. 每个瞭望点安排一名士兵值班, 在某个时间段内, $n$ 个士兵先后沿圆周按逆时针方向运动到最近的一个未接收报告的要塞报告观测到的情况, 其中每个要塞只听取一个士兵的报告, 每次都是当一个士兵报告完毕之后另一个士兵才出发进行下一次报告. 证明: 不管士兵以何种次序出发, 各个士兵运动的路程之和是定值.

证明 对士兵及要塞按如下规则进行编号和染色: 对每个 $i(1 \leq i \leq n)$, 如果某士兵是第 $i$ 个出发进行报告的, 则将其记上红色编号 $r_{i}$, 接收该士兵报告的要塞则记上蓝色编号 $b_{i}$. 由每个红色 $r_{i}$ 按逆时钟方向连一条到蓝色 $b_{i}$ 的弧, 称为逆弧 $i$, 则各个士兵运动的路程之和就是各个逆弧 $i(1 \leq i \leq n)$ 的长度之和.

考察 $n$ 个士兵的任意一种编号方式 $M$, 对其进行如下操作: 将 $M$ 中的红色编号 $r_{i-1}, r_{i}(2 \leq i \leq n)$ 分别改为 $r_{i}, r_{i-1}$ (即交换这两个士兵的出发顺序), 其余红色编号不变, 得到一种新的编号方式 $N$.

我们证明: 这两种编号方式的逆弧长度和相同.

记 $M$ 中红色编号 $r_{i-1}, r_{i}(2 \leq i \leq n)$ 对应的两个士兵为 $A, B$, 蓝色编号 $b_{i-1}, b_{i}$ 对应的两个要塞分别为 $C, D$, 则 $A, B, C, D$ 在圆周上的分布本质上只有两种可能 (如下图所示).

显然, 编号下标小于 $i-1$ 的红色编号在操作中不变, 从而其对应的蓝色编号也不变. 此外, 考察以 $A, B, C, D$ 为端点的逆弧的改变情况, $M$ 中的两段逆弧


$i-1, i$ 分别为 $\widehat{A C}, \widehat{B D}$.

对于第一种情形, 由于 $M$ 中逆弧 $i=\widehat{B D}$, 表明 $B$ 报告时距离最近的一个未接收报告的蓝点是 $D$. 当 $B$ 先于 $A$ 报告时 (编号下标 $i$ 改为 $i-1$ ), $B$ 所连的逆弧仍为 $\overparen{B D}$, 所以逆弧 $i-1$ 变为 $\overparen{B D}$. 接着 $A$ 进行报告, $A$ 报告时距离最近的一个未接收报告的蓝点是 $C$, 所以逆弧 $i$ 变为 $\overparen{A C}$. 此时, 两段逆弧 $i-1, i$ 互换,长度之和不变. 又其他逆弧的位置都不变, 于是所有逆弧的长度之和不变.

对于第二种情形, 由于 $M$ 中逆弧 $i-1=\widehat{A C}$, 说明 $C$ 较 $D$ 距离 $A$ 更近, 也就是 $C$ 较 $D$ 距离 $B$ 更近. 当 $B$ 先于 $A$ 报告时, $B$ 遇到的第一个未接收报告的蓝点是 $C$, 所以逆弧 $i-1$ 变为 $\overparen{B C}$. 接着 $A$ 进行报告, $A$ 报告时距离最近的一个未接收报告的蓝点是 $D$, 所以逆弧 $i$ 变为 $\widehat{A D}$. 此时, 注意到 $\overparen{A C}+\overparen{B D}=\widehat{A D}+\overparen{B C}$,两段逆弧 $i-1, i$ 的长度之和不变. 又其他逆弧的位置都不变, 于是所有逆弧的长度之和不变.

考察 $n$ 个士兵的任意一种编号 $M$, 设第一个士兵的编号为 $r_{x_{1}}$. 如果 $x_{1}>1$,则将 $M$ 中第一个士兵的编号改为 $r_{x_{1}-1}$, 编号为 $r_{x_{1}-1}$ 的士兵的编号改为 $r_{x_{1}}$, 得到一种新的编号方式. 如果新的编号方式中第一个士兵的编号下标仍然大于 1 ,则继续上述操作, 若干次操作后可使第一个士兵的编号变为 $r_{1}$. 类似地考察第 2 个士兵的编号, 若干次操作可使第 2 个士兵的编号变为 $r_{2}$. 如此下去, 可经过若干次操作, 使对任何 $i(1 \leq i \leq n)$, 第 $i$ 个士兵的编号变为 $r_{i}$. 由上述结论, 操作不改变编号方式的逆弧长度之和, 所以任何编号方式都与编号方式 $(1,2, \cdots, n)$ 的逆弧长度之和相同. 由此可见, 各个士兵运动的路程之和与报告顺序无关, 为定值.

评注 此题是一道中等难度的题, 得分率 $35 \%$ 左右. 证明的关键点是要发现任意一种出发次序, 都可以通过不断调整两个士兵的出发次序, 最终均变为一种特定的出发次序. 而调整的实质是证明 $n=2$ 的情形. 不少同学使用了归纳法,
同样也需要调整的思想.

题 4. (1) 设 $\alpha, n, k$ 是正整数, $n \geq k, p$ 是素数, 且满足 $p^{\alpha} \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$, 证明: $p^{\alpha} \leq n$.

(2) 设正整数 $n, k$ 满足 $n \geq k^{2} \geq 64$, 证明: $\left(\begin{array}{l}n \\ k\end{array}\right)$ 有一个大于 $k$ 的素因子.

证明 (1) 由 Legendre 定理知, $\left(\begin{array}{l}n \\ k\end{array}\right)$ 中 $p$ 的幂次为

$$
\sum_{l=1}^{\alpha_{1}}\left(\left\lfloor\frac{n}{p^{l}}\right\rfloor-\left\lfloor\frac{k}{p^{l}}\right\rfloor-\left\lfloor\frac{n-k}{p^{l}}\right\rfloor\right)
$$

其中 $\alpha_{1}$ 是非负整数且 $p^{\alpha_{1}} \leq n<p^{\alpha_{1}+1}$.

注意到不等式 $0 \leq\lfloor a+b\rfloor-\lfloor a\rfloor-\lfloor b\rfloor \leq 1, \forall a, b \in \mathbb{R}$, 故上述 $\alpha_{1}$ 个项的和中每一项的值是 0 或 1 , 所以它们的和不超过 $\alpha_{1}$, 即 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 中 $p$ 的幂次至多为 $\alpha_{1}$.

由 $p^{\alpha} \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$ 知, $\left(\begin{array}{l}n \\ k\end{array}\right)$ 中 $p$ 的幂次至少为 $\alpha$, 故 $\alpha \leq \alpha_{1}$, 所以 $p^{\alpha} \leq p_{1}^{\alpha} \leq n$. 结论成立.

(2) 令 $\pi(k)$ 表示不超过 $k$ 的素数的个数.

先证: 当 $k \geq 8$ 时, $\pi(k) \leq \frac{k}{2}$.

事实上, 当 $k \geq 8$ 时, $\pi(8)=4$. 当 $k \geq 9$ 时, 1,9 与所有大于等于 4 的偶数都不是素数, 这些数共有 $\left\lfloor\frac{k}{2}\right\rfloor+1$ 个, 故

$$
\pi(k) \leq k-\left\lfloor\frac{k}{2}\right\rfloor-1 \leq \frac{k}{2}
$$

假设 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 没有大于 $k$ 的素因子, 由算术基本定理知 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 可以写成不同素数幂的乘积, 由 (1) 的结论, 每一个素数幂都大不于 $k$, 一共有至多 $\pi(k)$ 个不同的素数幂, 所以

$$
\left(\begin{array}{l}
n \\
k
\end{array}\right) \leq n^{\pi(k)} \leq n^{\frac{k}{2}}
$$

另一方面, 注意到

$$
\left(\begin{array}{l}
n \\
k
\end{array}\right)=\frac{n}{k} \cdot \frac{n-1}{k-1} \cdot \frac{n-2}{k-2} \cdots \frac{n-k+1}{1}>\left(\frac{n}{k}\right)^{k} .
$$

结合以上两个不等式知

$$
\left(\frac{n}{k}\right)^{k} \leq n^{\frac{k}{2}}
$$

即有 $n<k^{2}$, 这与 $n \geq k^{2}$ 矛盾. 故结论成立.

评注 此题的背景是 Sylvester 定理: 当 $n>k$ 时, $n, n+1, \cdots, n+k-1$ 中一定有一个数含有一个大于 $k$ 的素因子. 此题来源于Erdös 的论文 “A Theorem of Sylvester and Schur.” 这是 Erdös在 20 岁的论文, 文中给出了 Sylvester 定理的一个漂亮的初等证明 (此前 Erdös 证明了 Sylvester 定理的特例 Chebyshev 定理), 在此论文中, Erdös 分了多种情况作不等式估计, 本题是其中较为简单的一
种情况.

本题得分率为 $28 \%$ 左右, 有一定区分度, 考试中绝大多数同学都做对了第一问. 第一问只要想到了 Legendre 定理或者 Kummer 定理, 很快就可以得出结论. 第二问的关键是在反证法证明中用算数基本定理把 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 写成素数幂的乘积,然后使用第一问的结论. 为了降低题目难度, 我们设置了第一问, 具有很强的提示作用, 给了第二问一个明确的做题方向.

题 5. $\odot O_{1}$ 与 $\odot O_{2}$ 交于 $A, B$ 两点, 过 $A$ 的直线分别交 $\odot O_{1}, \odot O_{2}$ 于点 $C, D$,满足 $O_{1}, O_{2}, C, D$ 四点共圆, 记该圆为 $\Gamma$. 设 $E$ 是 $C O_{2}$ 与 $D O_{1}$ 的交点, $I$ 是线段 $B E$ 与圆 $\Gamma$ 的交点. 证明: $I$ 是 $\triangle C B O_{2}$ 和 $\triangle D B O_{1}$ 的内心.

下面的证法一由张端阳给出.



证法一 本题直接引用如下熟知结论:

设四边形 $A B C D$ 内接于圆 $O$, 延长 $A B, D C$ 交于点 $E$, 延长 $A D, B C$ 交于点 $F, A C, B D$ 交于点 $P$. 延长 $O P$ 交 $E F$ 于点 $G$, 则 (1) $O G \perp E F ;(2) G$ 是完全四边形 $A B C D E F$ 的密克点; (3) $G, A, O, C 、 G, B, O, D$ 分别四点共圆.


回到原题.

延长 $C D, O_{1} O_{2}$ 交于点 $F$, 延长 $C O_{1}, D O_{2}$ 交于点 $G$. 过 $E$ 作 $E B^{\prime} \perp F G$ 于点 $B^{\prime}$, 下证 $B^{\prime}$ 与 $B$ 重合.

事实上, 由上述结论, $B^{\prime}$ 是完全四边形 $C D O_{2} O_{1} F G$ 的密克点. 所以

$$
\angle O_{1} B^{\prime} G=\angle O_{1} C A=\angle O_{1} A C, \angle O_{2} B^{\prime} F=\angle O_{2} D A=\angle O_{2} A D,
$$

从而 $\angle O_{1} B^{\prime} O_{2}=\angle O_{1} A Q_{2}$. 又易知 $\triangle B^{\prime} O_{1} C \backsim \triangle B^{\prime} O_{2} D$, 所以

$$
\frac{B^{\prime} O_{1}}{B^{\prime} O_{2}}=\frac{C O_{1}}{D O_{2}}=\frac{A O_{1}}{A O_{2}}
$$

于是 $\triangle B^{\prime} O_{1} O_{2} \sim \triangle A O_{1} O_{2}$. 因为 $O_{1} O_{2}$ 是公共边, 所以 $\triangle B^{\prime} O_{1} O_{2} \cong \triangle A O_{1} O_{2}$.因此 $B^{\prime}$ 与 $A$ 关于 $O_{1} O_{2}$ 对称, 故 $B^{\prime}$ 与 $B$ 重合.



设 $\Gamma$ 的圆心是 $O$, 由 $B$ 是密克点以及熟知结论, $B, E, O$ 共线, 且 $B, C, O, O_{2}$四点共圆. 因为 $O C=O I=O O_{2}$, 所以由鸡爪定理的逆定理, $I$ 是 $\triangle C B O_{2}$ 的内心. 同理, $I$ 是 $\triangle D B O_{1}$ 的内心.

下面的证法二由李先颖博士 (2004 年 IMO 金牌得主) 提供.

证法二 由 $\angle B O_{1} C=2 \angle B A C=\angle B O_{2} D, O_{1} C=O_{1} B, O_{2} B=O_{2} D$ 知 $\triangle B C O_{1} \sim \triangle B D O_{2}$.

故 $\angle B C O_{1}=\angle C B O_{1}=\angle B D O_{2}=\angle D B O_{2}$, 设为 $\theta$.

由熟知的结论知, $\triangle B O_{1} O_{2} \sim \triangle B C D$, 所以 $\angle B C D=\angle B O_{1} O_{2}$.

注意到

$$
\begin{aligned}
\angle C O_{1} O_{2}+\angle D O_{2} O_{1} & =2 \pi-\angle O_{1} C D-\angle O_{2} D C \\
& =2 \pi-(\angle B C D-\theta)-(\angle B D C+\theta) \\
& =\pi+\angle C B D,
\end{aligned}
$$



又 $C, D, O_{1}, O_{2}$ 四点共圆及 $A B \perp O_{1} O_{2}$,

$$
\begin{aligned}
\angle C O_{1} O_{2}-\angle D O_{2} O_{1} & =\angle C O_{1} O_{2}+\angle D C O_{1}-\pi \\
& =\angle C O_{1} O_{2}+\angle B C D-\theta-\pi \\
& =\angle C O_{1} O_{2}+\angle B O_{1} O_{2}-\theta-\pi \\
& =2 \pi-\angle B O_{1} C-\theta-\pi \\
& =\pi-(\pi-2 \theta)-\theta=\theta,
\end{aligned}
$$

故由上述两式得:

$$
\angle C O_{1} O_{2}=\frac{\pi+\angle C B D+\theta}{2}=\frac{\pi}{2}+\frac{\angle C B O_{2}}{2} .
$$

设 $\triangle C B O_{2}$ 的内心为 $I_{1}, \triangle D B O_{1}$ 的内心为 $I_{2}$, 则

$$
\angle C I_{1} O_{2}=\frac{\pi}{2}+\frac{\angle C B O_{2}}{2}=\angle C O_{1} O_{2},
$$

故 $I_{1}$ 在 $C, D, O_{1}, O_{2}$ 的外接圆上.

同理, $I_{2}$ 也在这个圆上. 因为 $\angle C B O_{1}=\angle D B O_{2}$, 故 $\angle C B O_{2}$ 和 $\angle D B O_{1}$ 的角平分线重合, 故 $I_{1}, I_{2}$ 重合, 记为 $I^{\prime}$.

现延长 $B I$ 交 $\triangle B C O_{2}$ 的外接圆于 $O$. 则有鸡爪定理知: $O C=O I=O O_{2}$.所以 $O$ 是 $\triangle C I O_{2}$ 的外心, 也是 $C, D, I^{\prime}, O_{1}, O_{2}$ 外接圆圆心. 同理, 延长 $B I$ 与 $\triangle B D O_{1}$ 外接圆的交点也是 $O$ 点. 于是 $I^{\prime}$ 在 $\triangle B C O_{2}$ 和 $\triangle B D O_{1}$ 外接圆的根轴上. 因为 $E C \cdot E O_{2}=E D \cdot E O_{1}$, 所以 $E$ 也在这两个圆的根轴上, 从而 $B, I^{\prime}, E$三点共线, 故 $I^{\prime}=I$, 即 $I$ 是 $\triangle D B O_{1}$ 的内心.
下面的证法三由成都外国语学校谢思睿同学给出.

证法三 因为

$$
\begin{aligned}
& \angle B O_{1} O_{2}=\frac{1}{2} \angle B O_{1} A=\angle B C A, \\
& \angle B O_{2} O_{1}=\frac{1}{2} \angle B O_{2} A=\angle B D A
\end{aligned}
$$

所以 $\triangle B O_{1} O_{2} \sim \triangle B C D$. 又因为 $C, D, O_{2}, O_{1}$, 四点共圆, 从而 $\triangle C E O_{1} \sim$ $\triangle D E O_{2}, \triangle C D E \sim \triangle O_{1} O_{2} E$, 于是

$$
\frac{C E}{E O_{2}}=\frac{C E}{D E} \cdot \frac{D E}{O_{2} E}=\frac{C O_{1}}{D O_{2}} \cdot \frac{C D}{O_{1} O_{2}}=\frac{B O_{1}}{B O_{2}} \cdot \frac{B C}{B O_{1}}=\frac{B C}{B O_{2}}
$$



由角平分线定理知: $B E$ 平分 $\angle C B O_{2}$, 同理 $B E$ 平分 $\angle D B O_{1}$. 又因为 $I$ 在 $C, D, O_{2}, O_{1}$ 外接圆上, 所以

$$
\angle E O_{1} I+\angle E O_{2} I=\angle D C I+\angle C D I=\pi-\angle C O_{1} D .
$$

又注意到,

$$
\begin{aligned}
& \angle B O_{1} E+\angle B O_{2} E \\
= & \left(2 \pi-\angle B O_{1} C-\angle C O_{1} D\right)+\left(\angle B O_{2} D-\angle C O_{2} D\right) \\
= & 2 \pi-2 \angle C O_{1} D,
\end{aligned}
$$

所以

$$
\angle B O_{1} I+\angle B O_{2} I=\angle E O_{1} I+\angle E O_{2} I \text {. }
$$

又

$$
\frac{O_{1} E}{O_{2} E}=\frac{O_{1} C}{O_{2} D}=\frac{O_{1} B}{O_{2} B}
$$

所以,

$$
\frac{I E}{I B}=\frac{O_{1} E \cdot \sin \angle E O_{1} I}{O_{1} B \cdot \sin \angle B O_{1} I}, \frac{I E}{I B}=\frac{E O_{2} \cdot \sin \angle E O_{2} I}{B O_{2} \cdot \sin \angle B O_{2} I}
$$

于是,

$$
\frac{\sin \angle E O_{1} I}{\sin \angle B O_{1} I}=\frac{\sin \angle E O_{2} I}{\sin \angle B O_{2} I}
$$

结合 (1) 知,

$$
\angle E O_{1} I=\angle B O_{1} I, \angle E O_{2} I=\angle B O_{2} I \text {, }
$$

即 $O_{1} I$ 平分 $\angle B O_{1} E$. 又 $B I$ 平分 $\angle O_{1} B D$, 所以 $I$ 是 $\triangle D B O_{1}$ 的内心. 同理, $I$ 是 $\triangle C B O_{2}$ 的内心.

评注 此题是一道中等难度的题, 得分率在 $38 \%$ 左右. 证法一主要用布洛卡定理和完全四边形的密克点的性质; 证法二主要用了同一法和根轴的性质, 考试中也有部分同学用了类似的方法; 证法三多次导边角关系得到结论.

题 6. $n$ 是给定的正整数. 对于 $n$ 元数组 $\bar{a}=\left(a_{1}, \cdots, a_{n}\right)$, 记

$$
S(\bar{a})=\sum_{i=1}^{n} 3^{i-1} a_{i}, \quad T(\bar{a})=\sum_{i=1}^{n} \frac{a_{i}}{3^{i-1}} .
$$

设 $m, k$ 是正整数且满足 $m \geq 2 k$, 定义

$$
A=\left\{\bar{a}=\left(a_{1}, \cdots, a_{n}\right) \mid k=S(\bar{a}) \text {, 其中 } a_{i} \in \mathbb{Z},\left|a_{i}\right| \leq m, i=1, \cdots, n\right\} \text {. }
$$

证明:

$$
\frac{\sum_{\bar{a} \in A} T(\bar{a})}{|A|} \leq k
$$

其中 $|A|$ 表示 $A$ 的元素个数.

证明 把集合 $A$ 划分成两个子集 $A_{1}, A_{2}$, 其中

$$
\begin{aligned}
& A_{1}=\left\{\bar{a}=\left(a_{1}, a_{2}, \cdots, a_{n}\right) \mid \bar{a} \in A, m \leq a_{1}<-m+2 k\right\} . \\
& A_{2}=\left\{\bar{a}=\left(a_{1}, a_{2}, \cdots, a_{n}\right) \mid \bar{a} \in A,-m+2 k \leq a_{1} \leq m\right\} .
\end{aligned}
$$

对任意 $\bar{a} \in A_{1}$, 因为 $a_{1}<-m+2 k, a_{i} \leq m(i \geq 2)$, 则

$$
\begin{aligned}
T(\bar{a}) & =\sum_{i=1}^{n} \frac{a_{i}}{3^{i-1}}<(-m+2 k)+m\left(\sum_{i=2}^{n} \frac{1}{3^{i-1}}\right) \\
& =(-m+2 k)+m \frac{\frac{1}{3}\left(1-\frac{1}{3^{n-1}}\right)}{1-\frac{1}{3}} \\
& <-m+2 k+m \cdot \frac{1}{2}=2 k-\frac{m}{2} \\
& \leq k,
\end{aligned}
$$

所以

$$
\sum_{\bar{a} \in A_{1}} T(\bar{a}) \leq k\left|A_{1}\right|
$$

而对任意的 $\bar{a} \in A_{2}$, 由 $A$ 的定义知

$$
\sum_{i=1}^{n} 3^{i-1} a_{i}=k
$$

从而

$$
\left(2 k-a_{1}\right)+\sum_{i=2}^{n} 3^{i-1}\left(-a_{i}\right)=k .
$$

由 $-m+2 k \leq a_{1} \leq m,-m \leq a_{i} \leq m$ 知,

$$
-m+2 k \leq 2 k-a_{1} \leq m,-m \leq-a_{i} \leq m
$$

故

$$
\left(2 k-a_{1},-a_{2}, \cdots,-a_{n}\right) \in A_{2} .
$$

将 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 与 $\left(2 k-a_{1},-a_{2}, \cdots,-a_{n}\right)$ 配对, 每个 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 恰出现在一对中 $((k, 0, \cdots, 0)$ 的配对元素为自身 $)$, 且有

$$
T\left(a_{1}, a_{2}, \cdots, a_{n}\right)+T\left(2 k-a_{1},-a_{2}, \cdots,-a_{n}\right)=T(2 k, 0, \cdots, 0)=2 k .
$$

从而 $\sum_{\bar{a} \in A_{2}} T(\bar{a})=k\left|A_{2}\right|$, 于是

$$
\sum_{\bar{a} \in A_{2}} T(\bar{a}) \leq k\left|A_{2}\right|
$$

综上可知，

$$
\frac{\sum_{\bar{a} \in A} T(\bar{a})}{|A|} \leq k
$$

评注 此题是难题, 考试中只有不到 $5 \%$ 的同学做对. 本题的思想是分段估计. 对于 $-m+2 k \leq a_{1} \leq m$ 部分用配对估计, 对 $m \leq a_{1}<-m+2 k$ 的部分直接放缩. 考试中部分做对的同学用了归纳法, 其本质与上述解法相同.

