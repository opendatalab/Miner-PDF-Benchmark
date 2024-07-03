# 第 62 届 IMO 全真模拟试题解析 

$$
\text { 王一川 }
$$

(清华大学, 100084)

指导教师: 唐立华

为准备 IMO, 笔者于 2021 年 6 月 5 日、 6 日举办了第 62 届国际数学奥林匹克全真模拟, 其中的试题均由笔者提供. 本文将介绍本次模拟的试题与解答,并简单介绍各题的创作过程. 直于水平, 不当之处在所难免, 敬请读者不吝赐教.

## I. 试 题

$$
\text { 第一天 }
$$

2021 年 6 月 5 日, 星期六

1. 在圆内接凸四边形 $A B C D$ 中, $\angle A B C<\angle B C D<90^{\circ}, A B<B C$, $C D<D A . E$ 是边 $B C$ 上一点, 满足 $A B=B E$. 过点 $A, B, E$ 的圆与对角线 $B D$ 交于不同于 $B$ 的另一点 $P . F$ 是边 $A D$ 上一点, 满足 $\frac{A F}{E F}=\frac{A P}{C P}=\frac{C P}{E P}$. 证明:过点 $A, F, P$ 的圆与直线 $B D$ 相切.
2. 给定整数 $n \geq 3$. 设 $V$ 是 $n$ 个城市构成的集合, 某些城市之间有单向道路连接, 每两个城市之间至多有一条道路. 对任意整数 $k \geq 3$ 以及 $V$ 的 $k$ 元子集 $I$, 称 $I$ 是 “圈状的”, 如果可以将 $I$ 中的城市适当记为 $I=\left\{a_{1}, a_{2}, \cdots, a_{k}\right\}$, 使得对 $i=1,2, \cdots, k$, 存在从 $a_{i}$ 到 $a_{i+1}$ 的单向道路, 这里 $a_{k+1}=a_{1}$.

求具有下述性质的最小正整数 $m$ : 对任意一种连接道路的方式, 若 $V$中每个城市均至多属于 2 个圈状的集合, 则可以将 $V$ 中的城市适当标号为 $1,2, \cdots, n$, 使得至多存在 $m$ 条道路从标号较小的城市通向标号较大的城市.

3. 设非负实数 $a_{1}, a_{2}, \cdots, a_{2021}$ 满足对 $k=1,2, \cdots, 2021$, 有 $a_{k}^{2}+3 a_{k+1} \geq 8$,这里 $a_{2022}=a_{1}$. 求 $a_{1}+a_{2}+\cdots+a_{2021}$ 的最小可能值.

修订日期: 2022-03-03.

$$
\text { 第二天 }
$$

2021 年 6 月 6 日, 星期日

4. 对于 $1,2, \cdots, 61$ 的排列 $\pi=\left(p_{1}, p_{2}, \cdots, p_{61}\right), \Omega_{\pi}$ 是下述在甲、乙两人之间的游戏: 从甲开始, 两人轮流地在黑板上写下一共 61 个实数 $a_{1}, a_{2}, \cdots, a_{61}$ (即: 甲写 $a_{1}$, 乙写 $a_{2}$, 甲写 $a_{3}$, 乙写 $a_{4}, \cdots$, 甲写 $a_{61}$ ), 若多项式

$$
P(x)=x^{62}+a_{p_{61}} x^{61}+\cdots+a_{p_{2}} x^{2}+a_{p_{1}} x+1
$$

无实根, 则甲胜; 否则乙胜.

求使 $\Omega_{\pi}$ 中甲有必胜策略的排列 $\pi$ 的个数.

5. 给定素数 $p$ 以及正整数 $n, k, p>n>k \geq 1$. 设 $A$ 是正整数集的 $n$ 元子集,满足 $A$ 中的元素均不被 $p$ 整除. 对于 $A$ 的任意子集 $I$, 称 $I$ 是“好的”，如果 $|I| \geq k$, 且多项式

$$
f(x)=\prod_{i \in I}(i x+1)
$$

中 $x^{k}$ 项的系数被 $p$ 整除.

证明: $A$ 的好的子集的个数不超过 $\frac{2 k}{\sqrt[3]{n}} \cdot 2^{n}$.

注: 如果证明了比 $\frac{2 k}{\sqrt[3]{n}} \cdot 2^{n}$ 更弱的结果, 会根据你的结果适当给分.

6. 在 $n \times n(n \geq 2)$ 方格表中, 每个小方格被染为红、黄两种颜色之一. 对于给定的整数 $n \geq 2$ 、染色方式 $\Gamma$ 以及正整数 $k$, 考虑在每个小方格中填一个不超过 $k$ 的正整数, 定义 $f_{n, \Gamma}(k)$ 为满足下述条件的填数方法数:

(1) 方格表左上角、右下角小方格填数均为 1 ;

(2) 任意两个有公共边的异色小方格的填数的差的绝对值均为 1 .

是否存在整数 $n \geq 2$ 以及染色方式 $\Gamma$, 使得 $f_{n, \Gamma}(61)$ 是偶数, 且 $f_{n, \Gamma}(62)$ 是奇数?

## II. 参考答案与评分标准

题 1 在圆内接凸四边形 $A B C D$ 中, $\angle A B C<\angle B C D<90^{\circ}, A B<B C$, $C D<D A$. $E$ 是边 $B C$ 上一点, 满足 $A B=B E$. 过点 $A, B, E$ 的圆与对角线 $B D$ 交于不同于 $B$ 的另一点 $P . F$ 是边 $A D$ 上一点, 满足 $\frac{A F}{E F}=\frac{A P}{C P}=\frac{C P}{E P}$. 证明:过点 $A, F, P$ 的圆与直线 $B D$ 相切.

证明 (I) 先证明: 线段 $A D$ 上存在一点 $K$, 满足 $\triangle A K P$ 外接圆与 $B D$ 相切, 且 $\frac{A K}{E K}=\frac{A P}{C P}$.
注意到 $\angle A P B=\angle A E B=90^{\circ}-\frac{1}{2} \angle A B E<90^{\circ}$, 于是 $\angle A P D>90^{\circ}$, 进而 $A D>P D$. 于是可令 $K$ 为线段 $A D$ 上一点, 满足 $D K \cdot D A=D P^{2}$.

从而 $\triangle D K P \sim \triangle D P A$, 且 $\triangle A K P$ 外接圆与 $B D$ 相切. 以下验证 $\frac{A K}{E K}=\frac{A P}{C P}$.

首先证明 $A P \cdot E P=B P^{2}-B E^{2}$.



记 $A E \cap B P=X$, 由 $\angle A P X=\angle B P E$ 及 $\angle P A X=\angle P B E$ 知 $\triangle A P X \sim$ $\triangle B P E$, 由 $\angle B P E=\angle B A E=\angle B E X$ 知 $\triangle B E P \sim \triangle B X E$, 故

$$
A P \cdot E P=B P \cdot X P=B P^{2}-B X \cdot B P=B P^{2}-B E^{2} .
$$

结论 (1) 得证.

结合 (1) 及 $\frac{A P}{C P}=\frac{C P}{E P}$, 知 $C P^{2}=B P^{2}-B E^{2}$.

取线段 $B E$ 上一点 $T$, 使 $B T \cdot B C=B E^{2}$, 则 $B T \cdot B C=B E^{2}=B A^{2} \Rightarrow$ $\triangle B A T \sim \triangle B C A$, 且由 (2) 知: $C P^{2}=B P^{2}-B T \cdot B C$. 考虑 $B$ 到以 $P$ 为圆心, $P C$ 为半径的圆的幂可知 $P T=P C$.

注意到

$\triangle B A T \sim \triangle B C A \Rightarrow \angle T A E=\angle B A E-\angle B A T=\angle B E A-\angle B C A=\angle C A E$,

且 $\angle P A E=\angle P B E=\angle D A C \Rightarrow \angle C A E=\angle D A P$, 故 $\angle T A E=\angle C A E=$ $\angle D A P$, 再结合 $\angle A K P=\angle A P B=\angle A E T$ 即知 $\triangle T A E \sim \triangle P A K$, 从而 $A T \cdot A K=A E \cdot A P$, 再结合

$$
\angle P A T=\angle T A E+\angle E A P=\angle D A P+\angle E A P=\angle D A E
$$

即知 $\triangle A P T \sim \triangle A K E$, 于是 $\frac{A K}{E K}=\frac{A P}{T P}=\frac{A P}{C P}$.



(II) 再证明: $F=K$.

用反证法. 假设 $F \neq K$, 则 $F, K$ 是线段 $A D$ 上两点, 满足 $\frac{A K}{E K}=\frac{A F}{E F}=\frac{A P}{C P}$.
设 $\{F, K\}=\left\{L_{1}, L_{2}\right\}, A, L_{1}, L_{2}, D$ 依次排列, 则

$$
0^{\circ} \leq \angle A E L_{1} \leq A E L_{2} \leq \angle A E D \leq 180^{\circ},
$$

且由角平分线定理,

$$
\frac{A L_{1}}{E L_{1}}=\frac{A L_{1}}{E L_{2}} \Rightarrow \angle A E L_{1}+\angle A E L_{2}=180^{\circ},
$$

于是 $\sin \angle A E L_{1}=\sin \angle A E L_{2} \geq \sin \angle A E D$, 进而

$$
\frac{A D}{E D}=\frac{\sin \angle A E D}{\sin \angle D A E} \leq \frac{\sin \angle A E L_{1}}{\sin \angle L_{1} A E}=\frac{A L_{1}}{E L_{1}}=\frac{A P}{C P}=\sqrt{\frac{A P}{E P}}
$$

设 $\angle A P D=\angle E P D=\theta \in\left[\frac{\pi}{2}, \pi\right]$, 则由余弦定理,

$$
\frac{A D^{2}}{E D^{2}}=\frac{A P^{2}+D P^{2}-2 \cos \theta \cdot A P \cdot D P}{E P^{2}+D P^{2}-2 \cos \theta \cdot E P \cdot D P}
$$

结合 (4) 知

$$
\frac{A P^{2}+D P^{2}-2 \cos \theta \cdot A P \cdot D P}{E P^{2}+D P^{2}-2 \cos \theta \cdot E P \cdot D P} \leq \frac{A P}{E P}
$$

进而 $\frac{A P^{2}+D P^{2}}{E P^{2}+D P^{2}} \leq \frac{A P}{E P}$, 去分母, 因式分解得

$$
(A P-E P)\left(A P \cdot E P-D P^{2}\right) \leq 0 .
$$

注意到, $\frac{A P}{E P}=\frac{\sin \angle A B P}{\sin \angle E B P}$ (正弦定理) $=\frac{A D}{C D}>1$, 即 $A P>E P$. 从而

$$
(5) \Rightarrow A P \cdot E P \leq D P^{2} \Rightarrow D P^{2} \geq A P \cdot E P=C P^{2} \Rightarrow D P \geq C P \text {. }
$$

又注意到 $(2) \Rightarrow B P \geq C P$, 于是由 $D P \geq C P$ 及 $B P \geq C P$ 知

$$
\angle P B C+\angle P D C \leq \angle P C B+\angle P C D=\angle B C D,
$$

从而 $\angle B C D \geq 90^{\circ}$, 与题意矛盾! 故只能 $F=K$.

结合 (I), (II) 即知: $\triangle A F P$ 外接圆与 $B D$ 相切, 原题得证.

评分标准 1 . 所有正确的解答均给 7 分. 基本正确但有 (可以立即纠正的)小错误, 酌情扣 $0-2$ 分. 不完整的证明, 按以下有效步骤给分:

2. 证明逆命题, 共 5 分:

证明 $A P \cdot E P=B P^{2}-B E^{2}$, 给 1 分;

证明 $\odot(P, P C)$ 与 $B C$ 的另一交点 $C^{\prime}$ 满足 $B C \cdot B C^{\prime}=B A^{2}$, 再给 1 分.

3. 验证 $F$ 的唯一性, 共 2 分:

用反证法, 推出 $\frac{A D}{E D} \leq \frac{A P}{C P}$, 给 1 分.

评注 本题是中等偏易的几何题, 其中逆命题部分较容易, 验证 $F$ 的唯一性稍有难度. 但有些选手没注意到要验证唯一性. 在做涉及反证、同一、条件型、或没有配图的几何题时需注意严谨推导.
题 2 给定整数 $n \geq 3$. 设 $V$ 是 $n$ 个城市构成的集合, 某些城市之间有单向道路连接, 每两个城市之间至多有一条道路. 对任意整数 $k \geq 3$ 以及 $V$ 的 $k$ 元子集 $I$, 称 $I$ 是“圈状的”，如果可以将 $I$ 中的城市适当记为 $I=\left\{a_{1}, a_{2}, \cdots, a_{k}\right\}$, 使得对 $i=1,2, \cdots, k$, 存在从 $a_{i}$ 到 $a_{i+1}$ 的单向道路, 这里 $a_{k+1}=a_{1}$.

求具有下述性质的最小正整数 $m$ ：对任意一种连接道路的方式，若 $V$中每个城市均至多属于 2 个圈状的集合, 则可以将 $V$ 中的城市适当标号为 $1,2, \cdots, n$, 使得至多存在 $m$ 条道路从标号较小的城市通向标号较大的城市.

解 结论是: 所求 $m$ 最小值为 $\left[\frac{n-1}{2}\right]$.

将城市看作顶点, 单向道路看作有向边, 作有向图 $G(V, E)$.

(I) 先给出使 $m<\left[\frac{n-1}{2}\right]$ 不成立的构造:

如下图:(共 $\left[\frac{n-1}{2}\right]$ 个三角形. 若 $2 \mid n$, 则再加一个孤立点.)



此时所有圈状的集合即为 $\left[\frac{n-1}{2}\right]$ 个三角形. 显然每个城市至多属于 2 个圈状的集合, 且任意将城市标号后, 每个三角形中至少存在一条边从小连到大, 共至少 $\left[\frac{n-1}{2}\right]$ 个这样的边.

(II) 再证明 $m=\left[\frac{n-1}{2}\right]$ 符合要求.

熟知有结论: “在无圈有向图中, 可将顶点从左到右排成一列, 使得每条边均从左连向右."

故只需证明: 可在 $G$ 中去掉 $\leq\left[\frac{n-1}{2}\right]$ 条边, 使 $G$ 中无圈.

对 $n \geq 1$ 归纳证明 (1).

$n=1,2$ 时 (1) 显然. 下设 $n \geq 3$, 且 $n$ 更小时 (1) 成立.

断言 1 每个圈状的集合 $I$ 的诱导子图中恰有一个哈密顿圈.

证明 用反证法, 假设有 $\geq 2$ 个, 设为 $\Gamma_{1}, \Gamma_{2}$. 设

$$
\Gamma_{1}: v_{1} \rightarrow v_{2} \rightarrow \cdots \rightarrow v_{|I|} \rightarrow v_{1}
$$

注意到 $\Gamma_{2}$ 中有一条边不在 $\Gamma_{1}$ 中, 不妨设为 $v_{1} \rightarrow v_{t}(3 \leq t \leq|I|-1)$, 则 $v_{1}, v_{t}$ 将 $\Gamma_{1}$ 分成两段:

$$
\left\{\begin{array}{cl}
v_{2}, \cdots, v_{t-1} & (\text { 称为红点 }) \\
v_{t+1}, \cdots, v_{|I|} & \text { (称为蓝点 })
\end{array}\right.
$$

注意到红点、蓝点均存在 $\geq 1$ 个, 且所有红点、蓝点为 $\Gamma_{2}$ 上连续 $|I|-2$ 个点, 故其中必存在相邻的一对红点、蓝点, 即存在 $2 \leq i \leq t-1$ 及 $t+1 \leq j \leq|I|$,使 $v_{i}, v_{j}$ 之间有边.

从而, 若将 $v_{1}, \cdots, v_{|I|}$ 排在圆周上, 则 $v_{1} v_{t}, v_{i} v_{j}$ 是相交的弦. 于是可将 $\Gamma_{1}$ 重新记为 $u_{1} \rightarrow \cdots \rightarrow u_{|I|} \rightarrow u_{1}$, 使得存在 $1 \leq i_{1}<i_{2}<i_{3}<i_{4} \leq|I|$, 满足存在边 $u_{i_{1}} \leftarrow u_{i_{3}}$ 及 $u_{i_{2}} \leftarrow u_{i_{4}}$. 于是

$$
u_{i_{1}} \rightarrow u_{i_{1}+1} \rightarrow \cdots \rightarrow u_{i_{3}} \rightarrow u_{i_{1}}, u_{i_{2}} \rightarrow u_{i_{2}+1} \rightarrow \cdots \rightarrow u_{i_{4}} \rightarrow u_{i_{2}}
$$

均是圈. 从而 $u_{i_{2}}$ 在 3 个圈状的集合

$$
\left\{u_{1}, \cdots, u_{|I|}\right\},\left\{u_{i_{1}}, \cdots, u_{i_{3}}\right\},\left\{u_{i_{2}}, \cdots, u_{i_{4}}\right\}
$$

中, 矛盾. 故断言 1 得证.

现在设所有的圈状的集合是 $A_{1}, \cdots, A_{m^{\prime}}\left(m^{\prime} \geq 1\right)$.

(若 $m^{\prime}=0$, 则 (1) 显然.)

情形 $1 A_{1}, \cdots, A_{m^{\prime}}$ 中存在两个集合交集大小 $\geq 2$.

不妨设 $\left|A_{1} \cap A_{2}\right| \geq 2$, 且 $\left|A_{1}\right| \geq\left|A_{2}\right|$.

设 $A_{1}$ 中的圈是 $p_{1} \rightarrow \cdots \rightarrow p_{r} \rightarrow p_{1}, A_{2}$ 中的圈是 $q_{1} \rightarrow \cdots \rightarrow q_{s} \rightarrow q_{1}$, $r \geq s \geq 3$. 适当地标记, 使 $p_{1}=q_{1}$ 且 $p_{r} \notin A_{2}$ (先选定 $p_{1}$, 使 $p_{1} \in A_{2}$ 且 $p_{r} \notin A_{2}$,再选定 $q_{1}$ 即可).

由 $\left|A_{1} \cap A_{2}\right| \geq 2$ 知 $\left\{p_{2}, \cdots, p_{r}\right\} \cap A_{2} \neq \varnothing$, 于是可取 $h$ 是最大正整数, 满足 $p_{h} \in A_{2}$ 且 $h \leq r$ (显然 $h<r$ ), 设 $p_{h}=q_{g}, h \geq 2, g \geq 2$, 则

$$
p_{1}=q_{1} \rightarrow \cdots \rightarrow q_{g}=p_{h} \rightarrow \cdots \rightarrow p_{r} \rightarrow p_{1}
$$

是简单有向圈 (因为 $p_{h+1}, \cdots, p_{r} \notin\left\{q_{1}, \cdots, q_{s}\right\}$ ), 于是

$$
B=\left\{q_{1}, \cdots, q_{g}, p_{h+1}, \cdots, p_{r}\right\}
$$

是圈状的.

由于 $p_{r} \notin A_{2}$ 且 $p_{r} \in B$, 故 $A_{2} \neq B$, 于是圈状的集合 $A_{2}, B$ 中的圈均含边 $q_{1} \rightarrow q_{2}$. 去掉边 $q_{1} \rightarrow q_{2}$, 由题意, 对 $\varepsilon \in\{1,2\}$, 包含 $q_{\varepsilon}$ 的圈状的集合只有 $A_{2}, B$,再结合断言 1 知: 含 $q_{\varepsilon}$ 的圈只有 $A_{2}, B$ 中的两个圈, 从而去掉 $q_{1} \rightarrow q_{2}$ 后, $q_{1}, q_{2}$均不在任何圈上, 再对除 $q_{1}, q_{2}$ 外的顶点应用归纳假设即知 (1) 成立.

情形 $2 A_{1}, \cdots, A_{m^{\prime}}$ 两两交集大小 $\leq 1$.

作简单无向图 $H$ : 顶点集为 $\left\{1, \cdots, m^{\prime}\right\}$, 对 $1 \leq i<j \leq m^{\prime}$, 在 $i, j$ 之间连边当且仅当 $\left|A_{i} \cap A_{j}\right|=1$.

断言 $2 H$ 中无圈.
证明 用反证法. 假设有圈, 取最小圈 $j_{1}-j_{2}-\cdots-j_{M}-j_{1}(M \geq 3)$, 约定 $j_{M+1}=j_{1}$. 对 $1 \leq i \leq M$, 设 $A_{j_{i}} \cap A_{j_{i+1}}=\left\{w_{i}\right\}$.

现在取 $G$ 中的有向圈:

$$
Z: w_{1} \rightsquigarrow w_{2} \rightsquigarrow \cdots \rightsquigarrow w_{M} \rightsquigarrow w_{1} . \quad\left(\text { 约定 } w_{M+1}=w_{1}\right)
$$

这里对 $1 \leq i \leq M, w_{i} \rightsquigarrow w_{i+1}$ 表示在 $A_{j_{i+1}}$ 的圈中从 $w_{i}$ 走到 $w_{i+1}$.

由“ $j_{1}-\cdots-j_{M}-j_{1}$ 圈长最小”知: $A_{j_{1}}, \cdots, A_{j_{M}}$ 之间, 属于 $\geq 2$ 个集合的城市只有 $w_{1}, \cdots, w_{M}$, 进而可知 $Z$ 是简单圈, 于是 $Z$ 中的顶点构成圈状的集合,记为 $Z^{*}$. 显然 $Z^{*} \neq A_{j_{1}}, A_{j_{2}}$, 这是由于

$$
\left|Z^{*} \cap\left\{w_{1}, \cdots, w_{M}\right\}\right|=M \geq 3,
$$

而

$$
\left|A_{j_{1}} \cap\left\{w_{1}, \cdots, w_{M}\right\}\right|=\left|A_{j_{2}} \cap\left\{w_{1}, \cdots, w_{M}\right\}\right|=2 .
$$

故 $w_{1}$ 在 3 个圈状的集合 $A_{j_{1}}, A_{j_{2}}, Z^{*}$ 中, 矛盾.

从而断言 2 得证!

于是 $H$ 是一个森林, 从而 $H$ 的边数 $\leq m^{\prime}-1$. 再结合 “每个城市至多属于 $A_{1}, \cdots, A_{m^{\prime}}$ 中 2 个集合”, 由容斥原理知:

$$
n \geq\left|\bigcup_{i=1}^{m^{\prime}} A_{i}\right|=\sum_{i=1}^{m^{\prime}}\left|A_{i}\right|-\sum_{1 \leq i<j \leq m^{\prime}}\left|A_{i} \cap A_{j}\right| \geq 3 m^{\prime}-\left(m^{\prime}-1\right)=2 m^{\prime}+1
$$

于是 $m^{\prime} \leq \frac{n-1}{2}$, 进而 $m^{\prime} \leq\left[\frac{n-1}{2}\right]$, 在 $A_{1}, \cdots, A_{m^{\prime}}$ 中各去掉一条边即知 (1)成立.

综上, 由归纳法知 (1) 得证. 进而原题所求 $m$ 最小值为 $\left[\frac{n-1}{2}\right]$.

评分标准 1 . 所有正确的解答均给 7 分. 基本正确但有 (可以立即纠正的)小错误，酌情扣 $0-2$ 分. 不完整的证明, 按以下有效步骤给分:

2. 猜测答案并给出构造, 给 1 分.
3. 证明“每个圈状集合中有唯一哈密顿圈”, 给 1 分.
4. 完成“存在 2 个圈交 $\geq 2$ ”时的归纳过渡，共 2 分:

证明存在 2 个圈有公共边, 给 1 分.

5. 完成“不存在 2 个圈交 $\geq 2$ ”时的证明, 共 3 分:

证明 $H$ 无圈, 给 2 分.

评注 本题是中等难度的图论题, 是一道较为传统的组合最值问题. 分好几个步骤, 全部拿满不容易, 但没做出也能拿一定分数. 其中构造辅助图 $H$ 的一步
看似玄妙, 其实通过尝试构造不难诱导出.

题 3 设非负实数 $a_{1}, a_{2}, \cdots, a_{2021}$ 满足对 $k=1,2, \cdots, 2021$, 有 $a_{k}^{2}+3 a_{k+1} \geq$ 8 , 这里 $a_{2022}=a_{1}$. 求 $a_{1}+a_{2}+\cdots+a_{2021}$ 的最小可能值.

解 结论是: $a_{1}+a_{2}+\cdots+a_{2021}$ 的最小可能值为 $2020 \sqrt{2}+\frac{8}{3}$.

一方面, 令 $\left(a_{1}, \cdots, a_{2021}\right)=\left(2 \sqrt{2}, 0,2 \sqrt{2}, 0, \cdots, 2 \sqrt{2}, 0, \frac{8}{3}\right)$, 显然符合要求,且 $a_{1}+a_{2}+\cdots+a_{2021}=2020 \sqrt{2}+\frac{8}{3}$.

另一方面, 我们证明总有 $a_{1}+\cdots+a_{2021} \geq 2020 \sqrt{2}+\frac{8}{3}$.

引理 1 若 $x \geq 3-2 \sqrt{2}, y \geq 0, x^{2}+3 y \geq 8$, 则 $x+y \geq 2 \sqrt{2}$.

证明 若 $x \geq 2 \sqrt{2}$, 则结论显然. 下设 $3-2 \sqrt{2} \leq x \leq 2 \sqrt{2}$. 此时

$$
x+y \geq x+\frac{8-x^{2}}{3}=2 \sqrt{2}+\frac{1}{3} \cdot(2 \sqrt{2}-x)(x-(3-2 \sqrt{2})) \geq 2 \sqrt{2}
$$

引理 1 得证!

引理 2 若 $x \geq 0, z \geq 0,0 \leq y \leq 3-2 \sqrt{2}, x^{2}+3 y \geq 8, y^{2}+3 z \geq 8$, 则 $x+y+z \geq 2 \sqrt{2}+\frac{8}{3}$.

证明 由条件知 $x+y+z \geq \sqrt{8-3 y}+y+\frac{8-y^{2}}{3}$ (记为 $f(y)$ ). 显然在 $[0,3-2 \sqrt{2}]$上 $f$ 是凸的 (二阶导 $\leq 0)$, 故 $f(y) \geq \min \{f(0), f(3-2 \sqrt{2})\}$.

这里 $f(0)=2 \sqrt{2}+\frac{8}{3}, f(3-2 \sqrt{2})=\sqrt{6 \sqrt{2}-1}+2 \sqrt{2}$.

易知 $\sqrt{6 \sqrt{2}-1} \geq \frac{8}{3}$.

$$
\left(\Leftarrow 6 \sqrt{2} \geq \frac{73}{9} \Leftarrow 54 \sqrt{2} \geq 73 \Leftarrow 10(5 \sqrt{2}-7)+(4 \sqrt{2}-3) \geq 0 .\right)
$$

故 $f(y) \geq \min \{f(0), f(3-2 \sqrt{2})\} \geq 2 \sqrt{2}+\frac{8}{3}$.

引理 2 得证!

引理 3 若 $x \geq \frac{3}{2}, y \geq 3-2 \sqrt{2}, x^{2}+3 y \geq 8$, 则 $x+y \geq \frac{17}{3}-2 \sqrt{2}$.

证明 若 $x>\sqrt{8-3(3-2 \sqrt{2})}=\sqrt{6 \sqrt{2}-1}$, 则将 $x$ 调整为 $\sqrt{6 \sqrt{2}-1}$, 条件仍成立, 且结论变强.

下设 $x \leq \sqrt{6 \sqrt{2}-1}$, 由条件知 $x+y \geq x+\frac{8-x^{2}}{3}$ (记为 $g(x)$ ). 显然 $g$在 $\left[\frac{3}{2}, \sqrt{6 \sqrt{2}-1}\right]$ 上二阶导 $\leq 0$, 故 $g(x) \geq \min \left\{g\left(\frac{3}{2}\right), g(\sqrt{6 \sqrt{2}-1})\right\}$. 其中 $g(\sqrt{6 \sqrt{2}-1})=\sqrt{6 \sqrt{2}-1}+3-2 \sqrt{2} \geq \frac{8}{3}+3-2 \sqrt{2}=\frac{17}{3}-2 \sqrt{2}$, 且 $g\left(\frac{3}{2}\right)=$ $\frac{41}{12} \geq 3 \geq \frac{17}{3}-2 \sqrt{2}$.

故引理 3 得证.

回到原题. 将 $a_{1}, \cdots, a_{2021}$ 排在圆周上, 称一项 $a_{k}$ 是 “大项” 当且仅当 $a_{k} \geq \frac{3}{2}$,否则称为“小项”. 显然不存在相邻两个小项. (因为 $\left(\frac{3}{2}\right)^{2}+3 \cdot \frac{3}{2}<8$ )
情形 1 每个小项均 $\geq 3-2 \sqrt{2}$.

由“不存在相邻小项” 知: 可将 $a_{1}, \cdots, a_{2021}$ 在圆周上分成若干段, 每一段为“大项”或“大项、小项”。

一个“大项”的值 $\geq \frac{3}{2} \geq \frac{17}{6}-\sqrt{2}$;

一个“大项、小项”中两项的算术平均 $\geq \frac{17}{6}-\sqrt{2}$. (由引理 3 )

故

$$
\begin{aligned}
a_{1}+\cdots+a_{2021} & \geq 2021 \cdot\left(\frac{17}{6}-\sqrt{2}\right) \\
& =2021 \sqrt{2}+2021 \cdot\left(\frac{17}{6}-2 \sqrt{2}\right) \\
& =2021 \sqrt{2}+\frac{2021}{6 \cdot(17+12 \sqrt{2})} \\
& \geq 2020 \sqrt{2}+\frac{8}{3} .
\end{aligned}
$$

情形 2 存在一个小项 $<3-2 \sqrt{2}$.

由“不存在相邻小项” 及 “2021 是奇数”知: 存在相邻大项.

不妨设 $a_{1}, a_{2021}$ 是大项.

取最大下标 $t$, 使 $a_{t}<3-2 \sqrt{2}$, 显然 $2 \leq t \leq 2020$. 由引理 2 知

$$
a_{t-1}+a_{t}+a_{t+1} \geq 2 \sqrt{2}+\frac{8}{3}
$$

由 $t$ 最大知 $a_{t+1}, \cdots, a_{2020} \geq 3-2 \sqrt{2}$, 于是由引理 1 知 $a_{t+1}, \cdots, a_{2021}$ 中任相邻两项和 $\geq 2 \sqrt{2}$, 且 $a_{2021} \geq \frac{3}{2}>\sqrt{2}$. 无论 $t$ 的奇偶性, 均可得

$$
a_{t+2}+\cdots+a_{2021} \geq \sqrt{2} \cdot(2020-t) .
$$

由“不存在相邻小项” 及 “ $a_{1}$ 是大项”知: 可将 $a_{1}, \cdots, a_{t-2}$ 分成若干段, 每段为“大项”或“大项、小项”。

若为“大项”, 则该项 $\geq \frac{3}{2} \geq \sqrt{2}$;

若为“大项、小项”, 则由引理 1 , 这两项的算术平均 $\geq \sqrt{2}$.

故

$$
a_{1}+\cdots+a_{t-2} \geq \sqrt{2} \cdot(t-2) \text {. }
$$

(1) $+(2)+(3)$ 得 $a_{1}+\cdots+a_{2021} \geq 2020 \sqrt{2}+\frac{8}{3}$.

故总有 $a_{1}+\cdots+a_{2021} \geq 2020 \sqrt{2}+\frac{8}{3}$.

评分标准 1 . 所有正确的解答均给 7 分. 基本正确但有 (可以立即纠正的)小错误, 酌情扣 $0-2$ 分. 不完整的证明, 按以下有效步骤给分:

2. 猜测答案并给出构造, 给 1 分.

## 3. 三个引理各 1 分.

4. 完成情形 1 给 1 分, 完成情形 2 再给 2 分.

评注 1. 可以看出, 原解答的方法只对变元个数 $n$ 是充分大的奇数奏效. 对于一般的 $n$, 结论是: $a_{1}+\cdots+a_{n}$ 的最小值是

$$
\begin{cases}n \cdot \sqrt{2} & (n \text { 是偶数 }) \\ (n-1) \cdot \sqrt{2}+\frac{8}{3} & (n \text { 是不小于 } 5 \text { 的奇数 }) . \\ n \cdot \frac{\sqrt{41}-3}{2} & (n=1,3)\end{cases}
$$

其中, $n$ 是不小于 5 的奇数的情形可由原解答作如下调整解决: 将情形 1,2 的分界点 $3-2 \sqrt{2}$ 改为 1 , 相应地, 引理 2 中 $y$ 的范围改为 $[0,1]$, 引理 3 改为 “若 $1 \leq x \leq \frac{\sqrt{41}-3}{2}, y \geq 0, x^{2}+3 y \geq 8$, 则 $x+y \geq \frac{10}{3}$ ". 具体的细节留给读者.

2. 本题是困难的不等式, 一些选手发现用归纳法可以每次去掉最小的一项及其前一项, 从而猜测并尝试证明 $n=5$ 时最小值为 $4 \sqrt{2}+\frac{8}{3}$, 但实际上 $n=5$比 $n=2021$ 还要难. 如果能够尝试将归纳法展开, 不难发现其中蕴涵着“大项、小项”的结构, 这样看来原题更像一个数列不等式, 可以感觉出 $n$ 充分大是有好处的, 进而诱导出本题的解法.

题 4 对于 $1,2, \cdots, 61$ 的排列 $\pi=\left(p_{1}, p_{2}, \cdots, p_{61}\right), \Omega_{\pi}$ 是下述在甲、乙两人之间的游戏: 从甲开始, 两人轮流地在黑板上写下一共 61 个实数 $a_{1}, a_{2}, \cdots, a_{61}$ (即: 甲写 $a_{1}$, 乙写 $a_{2}$, 甲写 $a_{3}$, 乙写 $a_{4}, \cdots$, 甲写 $a_{61}$ ), 若多项式

$$
P(x)=x^{62}+a_{p_{61}} x^{61}+\cdots+a_{p_{2}} x^{2}+a_{p_{1}} x+1
$$

无实根, 则甲胜; 否则乙胜.

求使 $\Omega_{\pi}$ 中甲有必胜策略的排列 $\pi$ 的个数.

解 设 $p_{r}=60, p_{s}=61$.

情形 $12 \mid s$.

我们给出甲的必胜策略:

$a_{1}, a_{3}, \cdots, a_{59}$ 任取, 最后令 $a_{61}$ (即 $a_{p_{s}}$ ) 是充分大正实数. 则 $a_{p_{s}}$ 充分大时,由均值不等式知:

对 $s+1 \leq i \leq 61$, 有 $\frac{x^{62}}{100}+a_{p_{i}} x^{i}+\frac{a_{p_{s}} x^{s}}{100}=0(\forall x \in \mathbb{R})$;

对 $1 \leq i \leq s-1$, 有 $\frac{1}{100}+a_{p_{i}} x^{i}+\frac{a_{p_{s}} x^{s}}{100}>0(\forall x \in \mathbb{R})$.

将以上各式累加得 $P(x)>0(\forall x \in \mathbb{R})$, 故 $P$ 无实根.
情形 $22 \nmid s$.

我们给出乙的必胜策略:

记 $\alpha=2^{\frac{1}{s}}, \beta=-1$, 则 $\alpha^{s}+2 \beta^{s}=0$, 且 $\alpha^{r}+2 \beta^{r}=2^{\frac{r}{s}}+2 \cdot(-1)^{r} \neq 0$. (因为 $r \neq s$ )

令 $a_{2}, a_{4}, \cdots, a_{58}$ 任取. 在选取 $a_{60}$ (即 $\left.a_{p_{r}}\right)$ 时, 令

$$
\left(\alpha^{62}+2 \beta^{62}+3\right)+\sum_{\substack{1 \leq i \leq 61 \\ i \neq s}} a_{p_{i}} \cdot\left(\alpha^{i}+2 \beta^{i}\right)=0
$$

(由 $\alpha^{r}+2 \beta^{r} \neq 0$ 知这样的 $a_{p_{r}}$ 存在)

结合 $\alpha^{s}+2 \beta^{s}=0$ 知: 无论乙如何选取 $a_{p_{s}}$ (即 $a_{61}$ ), 均有

$$
\left(\alpha^{62}+2 \beta^{62}+3\right)+\sum_{1 \leq i \leq 61} a_{p_{i}} \cdot\left(\alpha^{i}+2 \beta^{i}\right)=0,
$$

即 $P(\alpha)+2 \cdot P(\beta)=0$. 从而无论 $P(\alpha), P(\beta)$ 正负性如何, 均可推出 $P$ 在 $[\beta, \alpha]$上有实根.

综上, 甲有必胜策略当且仅当 $2 \mid s$, 易知这样的排列有 $30 \cdot 60$ ! 个. (先选取 $s$, 共 30 种, 再选取 $p_{i}(i \neq s)$, 共 60 ! 种.)

故原题所求排列个数为 $30 \cdot 60$ !.

评分标准 1 . 所有正确的解答均给 7 分. 基本正确但有 (可以立即纠正的)小错误，酌情扣 $0-2$ 分. 不完整的证明, 按以下有效步骤给分:

2. 猜测结论, 给 1 分.

$3 . s$ 偶时甲的策略, 共 3 分.
4. $s$ 奇时乙的策略，共 3 分.

评注 本题是简单的多项式结合博亦的问题, 答案不太好猜, 但整体难度不大还是可以较快做出的。

题 5 给定素数 $p$ 以及正整数 $n, k, p>n>k \geq 1$. 设 $A$ 是正整数集的 $n$ 元子集, 满足 $A$ 中的元素均不被 $p$ 整除. 对于 $A$ 的任意子集 $I$, 称 $I$ 是“好的”，如果 $|I| \geq k$, 且多项式

$$
f(x)=\prod_{i \in I}(i x+1)
$$

中 $x^{k}$ 项的系数被 $p$ 整除.

证明: $A$ 的好的子集的个数不超过 $\frac{2 k}{\sqrt[3]{n}} \cdot 2^{n}$.

注: 如果证明了比 $\frac{2 k}{\sqrt[3]{n}} \cdot 2^{n}$ 更弱的结果, 会根据你的结果适当给分.
证明 记 $A$ 的好的子集的个数是 $S$. 设 $A$ 中模 $p$ 余 $1,2, \cdots, p-1$ 的元素各有 $c_{1}, \cdots, c_{p-1}$ 个, 记 $c=\max \left\{c_{1}, \cdots, c_{p-1}\right\}$.

(I) 先证明: $S \leq \frac{2 k c}{n} \cdot 2^{n}$.

对 $j \geq 0$ 及 $I \subseteq A$, 记

$$
\sigma_{j}(I)=\sum_{\substack{Y \subseteq I \\|Y|=j}} \prod_{y \in Y} y .
$$

则好的子集即为满足 $|I| \geq k$ 且 $p \mid \sigma_{k}(I)$ 的子集.

任取 $k+1 \leq r \leq n$ 及 $A$ 的 $r$ 元子集 $I$, 再任取 $x \in I$. 注意到对 $j \geq 1$, 有

$$
\sigma_{j}(I)=\sigma_{j}(I \backslash\{x\})+x \cdot \sigma_{j-1}(I \backslash\{x\}),
$$

即:

$$
\sigma_{j}(I \backslash\{x\})=\sigma_{j}(I)-x \cdot \sigma_{j-1}(I \backslash\{x\})
$$

结合 $\sigma_{0}(I \backslash\{x\})=1$, 由归纳法易知对 $0 \leq j \leq k$, 若固定 $I$, 则 $\sigma_{j}(I \backslash\{x\})$ 可看作关于 $x$ 的 $j$ 次多项式, 且首项系数为 $\pm 1$. 于是由拉格朗日定理, 对固定的 $I$,满足 $p \mid \sigma_{k}(I \backslash\{x\})$ 的 $x$ 在 $\bmod p$ 意义下至多有 $k$ 种可能. 再结合 $c$ 的定义可知:对固定的 $I$, 满足 $p \mid \sigma_{k}(I \backslash\{x\})$ 的 $x$ 的个数不超过 $c k$.

由此可推出: 对任意 $k \leq r \leq n-1$ 及 $r+1$ 元集 $I_{0} \subseteq A, I_{0}$ 的 $r+1$ 个 $r$ 元子集中至多 $c k$ 个是好的, 从而 $A$ 的 $r$ 元好子集个数 $\leq \mathrm{C}_{n}^{r} \cdot \frac{c k}{r+1}$. 于是

$$
\begin{aligned}
S & \leq \sum_{r=k}^{n-1} \mathrm{C}_{n}^{r} \cdot \frac{c k}{r+1}+1 \quad(+1 \text { 是考虑 } n \text { 元好子集 }) \\
& =\sum_{r=k}^{n-1} \mathrm{C}_{n+1}^{r+1} \cdot \frac{c k}{n+1}+1 \\
& \leq \sum_{r=k}^{n-1} \mathrm{C}_{n+1}^{r+1} \cdot \frac{c k}{n+1}+\mathrm{C}_{n+1}^{1} \cdot \frac{c k}{n+1} \\
& \leq \sum_{r=-1}^{n} \mathrm{C}_{n+1}^{r+1} \cdot \frac{c k}{n+1} \\
& =2^{n+1} \cdot \frac{c k}{n+1} \\
& =\frac{2 c k}{n+1} \cdot 2^{n} .
\end{aligned}
$$

结论 (1) 得证.

(II) 再证明 $S \leq \frac{k}{\sqrt{c}} \cdot 2^{n}$.

设 $c=c_{t}, A_{1}$ 是 $A$ 中模 $p$ 不余 $t$ 的元素的集合, $A_{2}$ 是 $A$ 中模 $p$ 余 $t$ 的元素的集合, 则 $\left|A_{1}\right|=n-c$ 且 $\left|A_{2}\right|=c$.
任取 $I \subseteq A_{1}$, 考虑在 $I$ 中加入 $x$ 个模 $p$ 余 $t$ 的元素得到 $I_{x}(0 \leq x \leq c)$. 注意到

$$
\sigma_{k}\left(I_{x}\right) \equiv \sum_{i=0}^{k} \sigma_{k-i}(I) \cdot t^{i} \cdot \mathrm{C}_{x}^{i} \quad(\bmod p)
$$

由 $p>n>k$ 知: 上式中每个组合数中 $i$ ! 均不是 $p$ 的倍数. 从而对于固定的 $I$, 在 $\bmod p$ 意义下 $\sigma_{k}\left(I_{x}\right)$ 可看作关于 $x$ 的 $k$ 次多项式, 且首项系数 $\equiv \frac{t^{k}}{k !} \not \equiv 0$ $(\bmod p)$. 故由拉格朗日定理, 对固定的 $I$, 满足 $p \mid \sigma_{k}\left(I_{x}\right)$ 的 $x$ 在 $\bmod p$ 意义下至多有 $k$ 种可能, 再结合 $c \leq n<p$ 知: 这样的 $x$ 的个数 $\leq k$. 进而可推出: 对固定的 $I \subseteq A_{1}$, 与 $A_{1}$ 的交恰为 $I$ 的 $2^{c}$ 个 $A$ 的子集中, 至多有 $k \cdot \mathrm{C}_{c}^{\left[\frac{c}{2}\right]}$ 个是好的.于是

$$
S \leq \frac{k \cdot \mathrm{C}_{c}^{\left[\frac{c}{2}\right]}}{2^{c}} \cdot 2^{n} \leq \frac{k}{\sqrt{c}} \cdot 2^{n}
$$

其中

$$
\begin{aligned}
\frac{\mathrm{C}_{c}^{\left\lceil\frac{c}{2}\right]}}{2^{c}} & =\frac{\mathrm{C}_{c}^{\left\lceil\frac{c}{2}\right\rceil}}{2^{c}}=\frac{\mathrm{C}_{2 \cdot\left\lceil\frac{c}{2}\right\rceil}^{\left\lceil\frac{c}{2}\right\rceil}}{2^{2 \cdot\left\lceil\frac{c}{2}\right\rceil}}=\prod_{i=1}^{\left\lceil\frac{c}{2}\right\rceil} \frac{2 i(2 i-1)}{4 i^{2}}=\prod_{i=1}^{\left\lceil\frac{c}{2}\right\rceil} \frac{2 i-1}{2 i} \\
& \leq \prod_{i=1}^{\left\lceil\frac{c}{2}\right\rceil} \sqrt{\frac{2 i-1}{2 i+1}}=\frac{1}{\sqrt{2 \cdot\left\lceil\frac{c}{2}\right\rceil+1}} \leq \frac{1}{\sqrt{c}} .
\end{aligned}
$$

故结论 (2) 得证.

结合 $(1)(2)$ 知

$$
\begin{aligned}
S & \leq \min \left\{\frac{2 k c}{n}, \frac{k}{\sqrt{c}}\right\} \cdot 2^{n} \\
& \leq\left(\frac{2 k c}{n}\right)^{\frac{1}{3}} \cdot\left(\frac{k}{\sqrt{c}}\right)^{\frac{2}{3}} \cdot 2^{n} \\
& \leq \frac{2 k}{\sqrt[3]{n}} \cdot 2^{n} .
\end{aligned}
$$

命题得证.

评分标准 所有正确的解答均给 7 分. 基本正确但有 (可以立即纠正的)小错误, 酌情扣 $0-2$ 分. 不完整的证明, 按以下有效步骤给分:

在 (A), (B) 两部分中选取分数较高的一部分:

(A) 1 . 解决 $k=1$ 的情形, 给 1 分.

2 . 对于某个固定的 $k \geq 2$, 给出 $o\left(2^{n}\right)$ 的估计, 再给 3 分.

(B) 1 . 证明 $S \leq \frac{2 k c}{n} \cdot 2^{n}$ ，共 3 分:

证明 $x(\bmod p)$ 至多 $k$ 种可能, 给 1 分.

2. 证明 $S \leq \frac{k}{\sqrt{c}} \cdot 2^{n}$, 共 3 分:

证明 $x(\bmod p)$ 至多 $k$ 种可能, 给 1 分.

评注 本题是困难的组合数论问题. 首先需要观察到若 $A$ 中元素 $\bmod p$ 互不相同, 则较容易使用组合方法给出估计 (即 (1)); 还需要从反面考虑, 当有一种余数出现很多时有另一种估计 (即 (2)), 将两种方法平均一下即得到原题所需. 这需要观察到很多的性质. 这里的一个难点是直观上感觉这样估计不太够,从而试图再找其他方法, 另一个难点是生成函数方法的误导. 本题中 “两种方法加权平均” 的方法在新星征解 39 期第 4 题中也出现过, 本题更难的一点是: 该征解题有一部分很简单, 而本题两部分都不容易.

一个笔者未解决的问题是: 本题的结果能否继续改进? 能否改进为 $O\left(\frac{k}{\sqrt{n}} \cdot 2^{n}\right)$ ? 留给有兴趣的读者思考.

题 6 在 $n \times n(n \geq 2)$ 方格表中, 每个小方格被染为红、黄两种颜色之一.对于给定的整数 $n \geq 2$ 、染色方式 $\Gamma$ 以及正整数 $k$, 考虑在每个小方格中填一个不超过 $k$ 的正整数, 定义 $f_{n, \Gamma}(k)$ 为满足下述条件的填数方法数:

(1) 方格表左上角、右下角小方格填数均为 1 ;

(2) 任意两个有公共边的异色小方格的填数的差的绝对值均为 1 .

是否存在整数 $n \geq 2$ 以及染色方式 $\Gamma$, 使得 $f_{n, \Gamma}(61)$ 是偶数, 且 $f_{n, \Gamma}(62)$ 是奇数?

解法 1 (王一川) 结论是: 存在.

令 $n=66$, 将 $n \times n$ 表格分成两部分 $U_{1}, U_{2}$, 如下图:



分别将 $U_{1}, U_{2}$ 间隔地染色, 且左上角、右下角异色.

此时原题要求 (2) 即为: $U_{1}$ 内部任两个相邻小方格填数之差为 1 或 -1 , 类似对于 $U_{2}$. 从而, 由对称性, 只需证明: $U_{1}$ 内部的填数方法数在 $k=61$ 时是偶
数, 在 $k=62$ 时是奇数.

$k=61$ 时, 注意到第 1 行第 $1,2, \cdots, 65$ 个方格的填数的奇偶性必为奇、偶、奇、偶、… 奇. 先将 $U_{1}$ 中除了第 1 行第 65 格外其他方格填数, 设第 1 行第 64 格填 $2 i(i \in\{1, \cdots, 30\})$, 则第 1 行第 65 格有 2 种填法: $2 i-1$ 或 $2 i+1$.故填数方法数是偶数.

以下考虑 $k=62$ :

任取一个奇数行, 考虑 $U_{1}$ 在该行中的 $1 \times 65$ 表格, 记为:

| $A_{1}$ | $A_{2}$ | $\cdots$ | $A_{65}$ |
| :--- | :--- | :--- | :--- |

设 $A_{1}, \cdots, A_{65}$ 中的填数为 $x_{1}, \cdots, x_{65}$, 则 $2 \nmid x_{1}$.

我们说明: 当且仅当 $x_{1}=1$ 时, 对 $A_{2}, \cdots, A_{65}$ 的填数方法数是奇数.

注意到: 当 $x_{1}, \cdots, x_{64}$ 确定时, 若 $x_{64}=62$, 则 $x_{65}$ 恰一种填法;其他情况中 $x_{65}$ 均恰有两种填法. 从而只需考虑满足 $x_{64}=62$ 且 $x_{65}=61$ 的填数方法数.

当 $x_{1}=2 t+1(t \in\{0,1, \cdots, 30\})$ 及 $x_{64}=62$ 确定时, 我们考虑 $x_{2}, \cdots, x_{63}$的取法数: 设

$$
\left(y_{1}, y_{2}, \cdots, y_{63}\right)=\left(x_{64}-x_{63}, x_{63}-x_{62}, \cdots, x_{2}-x_{1}\right),
$$

则只需使序列 $y_{1}, \cdots, y_{63}$ 满足: $y_{1}, \cdots, y_{63} \in\{-1,1\}, y_{1}, \cdots, y_{63}$ 中任意前若干项中 1 的个数 $\geq-1$ 的个数, 且其中共有 $62-t$ 个 1 及 $t+1$ 个 -1 , 且 $y_{1}, \cdots, y_{62}$不全为 1 .

由 Hook length 定理，若去掉 “ $y_{1}, \cdots, y_{62}$ 不全为 1 ” 的条件，则这样的 $\left(y_{1}, \cdots, y_{63}\right)$ 的个数是

$$
\frac{63 !}{(t+1) ! \cdot(61-2 t) ! \cdot \prod_{i=63-2 t}^{63-t} i}
$$

记上式的值为 $S$, 则

$$
\begin{aligned}
S & =\frac{63 ! \cdot(62-2 t)}{(t+1) ! \cdot(63-t) !} \\
& =\mathrm{C}_{63}^{t} \cdot \frac{62-2 t}{t+1} \\
& =2 \cdot \mathrm{C}_{63}^{t} \cdot \frac{63-t}{t+1}-\mathrm{C}_{63}^{t} \cdot \frac{64}{t+1} \\
& =2 \cdot \mathrm{C}_{63}^{t+1}-\mathrm{C}_{64}^{t+1} .
\end{aligned}
$$

由 Lucas 定理知 $2 \mid \mathrm{C}_{64}^{t+1}$, 进而 $2 \mid S$. 又注意到, 若 $y_{1}=\cdots=y_{62}=1$, 则只能 $t=0$ 且 $y_{63}=-1$. 从而 $t \neq 0$ 时, $S$ 即为 $\left(y_{1}, \cdots, y_{63}\right)$ 的个数; $t=0$ 时, $S-1$为 $\left(y_{1}, \cdots, y_{63}\right)$ 的个数. 由此即知 (1) 得证!
下面计算 $U_{1}$ 的填数方法数:

先填第 1 列. 当第 1 列确定时, 若第 1 列第 $1,3,5, \cdots, 65$ 格不全为 1 , 则剩下部分的填法数是偶数;否则是奇数. 而使 “第 1 列第 $1,3,5, \cdots, 65$ 格全为 1 ” 的填法只有 $1,2,1,2, \cdots, 1,2$ 这 1 种. 故 $U_{1}$ 的填法数是奇数, 进而 $f_{66, \Gamma}(62)$ 是奇数.

综上, 这样的构造即符合要求.

解法 2 (路原) 存在.

令 $n=64$, 下构造染色. 如图:



将棋盘分为 2 个部分. 最上、最下各为 1 排格子, 每部分有 32 个凸起. 对每个区域, 将其中的格红黄相间染色, 且 $A$ 红 $B$ 黄. 下证此染色符合要求.

(I) 黑白两区域的标数互不影响.

对黑白区域上任意两相邻格 $X, Y, X$ 黑 $Y$ 白.

经过黑区域作从 $A$ 至 $X$ 的路, 过白区域从 $Y$ 至 $B$ 的路. 可知 $A \rightarrow X \rightarrow$ $Y \rightarrow B$ 上有奇数个格. 因此若 $A \rightarrow X$ 上有奇数格, 则 $Y \rightarrow B$ 上有偶数格, 故 $X$ 黄 $Y$ 黄. 若 $A \rightarrow X$ 上有偶数格, 则同理, 故 $X, Y$ 为红. 综上, 有 $X, Y$ 同色,故黑、白区域上相邻格均同色, 故它们互不干扰. 由黑白两区全等知棋盘上标数方法数为黑区域标数方法数的平方.

(II) $k=61$ 时有偶数种标数.

考虑黑区最左侧, 设 $U$ 上标 $l, V$ 上标 $m$.

由奇偶性知 $2 \mid l$ 且 $2 \nmid m$. 因为 $m=l+1$ 或 $l-1$, 考虑到 $2 \leq l \leq 60$, 故不论从 $A$ 到 $U$ 如何标, $V$ 可标 $l+1, l-1$ 中任一个, 故总有 2 种填法, 故黑区域有偶数种标法. 证毕.

(III) $k=62$ 时, 对黑区域的任一个凸起, 如下图:



断言: 这 62 格在 $C$ 标 1 时有奇数种标法, 在 $C$ 标 3 时有偶数种标法.

同(II)考虑 $D, E$ 可知 $D$ 标偶数. 且不标 62 时有偶数种标法.

下设 $D$ 为 $62, E, F$ 为 61 . 若 $C$ 为 $1, C \rightarrow F$ 有 61 格, 仅有 $1,2,3, \cdots, 61$ 一个标法, 为奇数个. 若 $C$ 为 3 , 可知 $C \rightarrow F$ 为: $3,4, \cdots, k, k-1, k, k+1, \cdots, 61(k=$ $3,4, \cdots, 61)$ 或 $3,4, \cdots, 61,62,61$ 共 60 种标法, 为偶数个.

(IV) $k=62$ 有奇数种标法.



由(III)知, 若 $C_{1}, \cdots, C_{31}$ 中有 3 , 则黑区域有偶数标法. 否则, $C_{1}, \cdots, C_{31}$均标 1 , 最上一排标 $1,2,1,2, \cdots, 1,2$, 由(III)知黑区域有奇数种标法.

因此黑区域共有奇数种标法, 棋盘共奇数种标法.

综上, 该染法符合要求.

解法 3 (韦晨) 存在.

$A, B$ 分别间隔染色使左上角为红, 右下角为黄, 则 $A, B$ 两区域间无限制.

记 $\Omega_{61}$ 为 $\leq 61$ 的方法数 (仅填 $A$ 区域), $K_{62}$ 为有至少一个 62 的方法数 (仅填 $A$ 区域).下证 $2 \mid \Omega_{61}$ 且 $2 \nmid K_{62}$.

对于 $\Omega_{61}$, 考虑填好了除 $\rightarrow$ 指的那个格的其他格, 则必必偶, 故 $\rightarrow$ 有两
种填法, 故 $2 \mid \Omega_{61}$.



若有至少一个 62 , 则由大小知只有出可能为 62 , 且若出为 62 , 则其他位置唯一, 故 $2 \nmid K_{62}$. 所以

$$
\begin{aligned}
& f_{n, \Gamma}(61)=\Omega_{61}^{2} \equiv 0(\bmod 2) \\
& f_{n, \Gamma}(62)=\left(\Omega_{61}+K_{62}\right)^{2} \equiv 1(\bmod 2)
\end{aligned}
$$

评分标准 1 . 所有正确的解答均给 7 分. 基本正确但有 (可以立即纠正的)小错误, 酌情扣 $0-2$ 分. 不完整的证明, 按以下有效步骤给分:

2. 给出可验证的正确构造, 给 1 分.
3. 验证 $f(61)$ 偶、 $f(62)$ 奇各 3 分:

若只在一条链上讨论了填数方法数 (而没有构造或没验证构造), 根据得到的结论酌情给 $0-2$ 分.

评注 1 . 可以先作一些简单推导:

(1) 没有不含左上、右下的连通分支 (否则作变换 $x \rightarrow 63-x$ 可知 $f(62)$偶);

(2) 存在一个连通分支大小 $\geq 62$ (否则显然 $f(61)=f(62))$. 由此可排除掉很小的 $n$.

2. 本题是中等偏难的组合构造题, 形式新颖. 本题有多种解法, 需要选手有创造性地设计染色, 根据需要适当对染色方式增加限制 (从而易于计数), 并灵活运用各种方法进行计数, 很好地考察了选手的创造力及灵活性. 本题有一个难
点是 $n$ 是可以任选的, 并没有要求充分大, 但思考时经常会带着 $n$ 充分大来思考. 个人认为本题是整套试卷中出得最好的一题.

总评 本套试题整体难度稍大, 每一天均有较易的题、中档的题、以及难题, 其中难题难度很大, 容易题也不能一下就做出来, 区分度主要体现在 2,6 两题, 第二天 5,6 两题反序则对考场策略有所要求. 个人认为每题均有一定的优美性, 其中 5,6 两题最为优美. 本套题能做到 $5+7+1+7+0+7=27$ 分就很好了.

## III. 试题创作过程

用 “题 $i$ ” 表示第 $i$ 题, “题 $i$. $\mathrm{a}$ " “题 $i$. b 等表示与第 $i$ 题相关的若干个问题.

第 1 题.

本题的灵感来源是集训队测试第二阶段期间在网上看到的一道错题:

题 1.a. $\triangle A B C$ 中, $A B=A C, B C$ 的中点是 $M, E, F$ 分别在 $A B, A C$ 上, $A E=A F$, 以 $A$ 为圆心, $A E$ 为半径作圆, $P$ 是此圆上一点, 且 $P C^{2}=P E \cdot P F$.证明: $B, C, P, I$ 共圆, 其中 $I$ 是 $\triangle A B C$ 的内心.

虽然题 1. $\mathrm{a}$ 是错题, 但其中 $P C^{2}=P E \cdot P F$ 的条件个人觉得比较有意思.集训队测试结束后笔者对这一结构进行研究, 为方便起见, 将 " $A E=A F=A P$ "改为 “ $A E=A F, A, E, F, P$ 共圆”, 最终得到了题 1 的逆命题. 为使题目描述美观, 改成了题 1 的形式, 这样还需要验证题 1 中 $F$ 的唯一性. 经探索发现加上 $\angle B C D<90^{\circ}$ 的条件即可使 $F$ 唯一.

## 第 2 题.

本题的灵感来源是某机构的集训队模拟中的一道错题:

题 2.a. 设 $n$ 为正整数.一个网络有 $n^{2}$ 个节点, 任意两个节点间至多有一条双向信自传输通道. 对于正整数 $k\left(3 \leq k \leq n^{2}\right)$ 以及节点 $A_{0}$, 如果一条信息可以从节点 $A_{0}$ 出发, 沿着信息传输通道经过 $k-1$ 个节点 $A_{1}, A_{2}, \cdots, A_{k-1}$, 最终返回 $A_{0}$ (其中节点 $A_{0}, A_{1}, A_{2}, \cdots, A_{k-1}$ 两两不同), 则称节点 $A_{0}$ 是 “ $k$-周期” 的.

已知该网络共有超过 $n^{2}+\frac{3}{2} n$ 条信息传输通道, 且当任意一个节点故障时,剩余节点中任意两个节点间仍可以传输信息. 证明: 存在正整数 $k\left(3 \leq k \leq n^{2}\right)$,使得 “ $k$-周期”的节点超过 $k$ 个.

题 2.a 的解答中直接将问题转换成 “图中存在两个等长的圈”, 但仔细读题就会发现其实还要求这两个圈的顶点集不同.

受此启发, 我们提出了“圈状集”的定义, 并设计了一个与“圈状集”有关的中等难度的图论题, 即题 2 . 事实上, 最终在题 2 中“圈状集” 和圈差别并不大.

## 第 3 题.

本题最初的灵感来源是 2020 联赛加试第 2 题:

题 3.a. 给定整数 $n \geq 3$. 设 $a_{1}, a_{2}, \cdots, a_{2 n}, b_{1}, b_{2}, \cdots, b_{2 n}$ 是 $4 n$ 个非负实数,满足 $a_{1}+a_{2}+\cdots+a_{2 n}=b_{1}+b_{2}+\cdots+b_{2 n}>0$, 且对任意 $i=1,2, \cdots, 2 n$, 有 $a_{i} a_{i+2} \geq b_{i}+b_{i+1}$ (这里 $a_{2 n+1}=a_{1}, a_{2 n+2}=a_{2}, b_{2 n+1}=b_{1}$ ).

求 $a_{1}+a_{2}+\cdots+a_{2 n}$ 的最小值.

从形式上, 题 3.a 属于“轮换条件族不等式”, 与 2017 年 CMO 第 6 题的“全对称条件族”有所不同.

但题 3.a 中对轮换条件族的用法只是将这些条件全加起来, 还是转换成了一个普通的不等式.

受此启发, 笔者希望编一道轮换条件族不等式题, 并希望只将条件全加起来是做不出的. 于是随手写了几个条件族, 发现在 $a_{k}^{2}+3 a_{k+1} \geq 8$ 的条件下估计 $a_{1}+a_{2}+\cdots+a_{n}$ 的最小值比较有意思. 经尝试解决了 $2 \mid n$ 的情形, 得到了下面的问题:

题 3.b. 给定正偶数 $n$. 设非负实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足对 $k=1,2, \cdots, n$,有 $a_{k}^{2}+3 a_{k+1} \geq 8$, 这里 $a_{n+1}=a_{1}$. 求 $a_{1}+a_{2}+\cdots+a_{n}$ 的最小可能值.

题 3.b 是联赛级别中中等偏难的问题, 本来打算投给新星测试, 但惨遭拒绝.

于是这题被留到了 IMO 模拟. 考虑到作为第 3 题应加大难度, 于是继续研究 $n$ 是奇数的情形, 经尝试解决了 $n$ 是充分大奇数的情形, 得到题 3. 再借助软件调整分界点, 解决了一般的 $n$,但这已经太难不适合竞赛了.

## 第 4 题.

本题是希望命制一道简单的代数题, 考虑到第 3 题是不等式, 于是希望第 4 题是一个关于多项式的问题. 参考 2019 年 CMO 第 6 题, 首先提出了如下研究方向:

题 4.a. 对于 $1,2, \cdots, 62$ 的一个排列 $p_{1}, p_{2}, \cdots, p_{62}$, 考虑下述游戏: 从甲开始，甲乙两人轮流地在黑板上写下一共 62 个实数 $a_{1}, a_{2}, \cdots, a_{62}$, 最后在黑板上写下两个多项式:

$$
\begin{aligned}
& P(x)=x^{62}+b_{1} x^{61}+\cdots+b_{61} x+b_{62}, \\
& Q(x)=x^{62}+b_{62} x^{61}+\cdots+b_{2} x+b_{1}
\end{aligned}
$$

其中 $b_{p_{i}}=a_{i}, i=1,2, \cdots, 62$. 若 $P(x)$ 有实根且 $Q(x)$ 无实根, 则乙胜;否则甲胜.

对哪些排列哪一方有必胜策略?
经短时间思考, 解决了部分排列的情况, 对于 $p_{61} \equiv p_{62} \equiv 0(\bmod 2)$ 的情形没有完全解决. 根据已解决的部分, 首先设计了如下问题:

题 4.b. 对于 $\{1,2, \cdots, 62\}$ 的 31 元子集 $A, \Omega_{A}$ 是下述在甲、乙两人之间的游戏: 首先乙在黑板上写下 $1,2, \cdots, 62$ 的一个排列 $p_{1}, p_{2}, \cdots, p_{62}$, 需满足 $\left\{p_{1}, p_{2}, \cdots, p_{31}\right\}=A$, 接下来从甲开始，两人轮流地在黑板上写下一共 62 个实数 $a_{1}, a_{2}, \cdots, a_{62}$ (即: 依次对 $i=1,2, \cdots, 31$, 甲写 $a_{2 i-1}$, 乙写 $\left.a_{2 i}\right)$, 最后乙在黑板上写下两个多项式:

$$
\begin{aligned}
& P(x)=x^{62}+b_{1} x^{61}+\cdots+b_{61} x+b_{62} \\
& Q(x)=x^{62}+b_{62} x^{61}+\cdots+b_{2} x+b_{1}
\end{aligned}
$$

其中 $b_{p_{i}}=a_{i}, i=1,2, \cdots, 62$. 若 $P(x)$ 有实根且 $Q(x)$ 无实根, 则乙胜;否则甲胜。

求使 $\Omega_{A}$ 中乙有必胜策略的集合 $A$ 的个数.

后来又对题 $4 . \mathrm{a}$ 进行了思考, 发现 $p_{61} \equiv p_{62} \equiv 0(\bmod 2)$ 时甲只要让 $Q(x)$有实根即可. 而为什么之前没有做出来, 恐怕是因为 $P(x)$ 的迷惑性较强, 且结论不是很好猜, 且探索未知问题时确实不保证问题是可做的.

最后作为第 4 题, 为降低难度, 改成题 4 的形式.

## 第 5 题.

本题的灵感来源是 2016 年集训队测试第二天第 6 题:

题 5.a. 设 $m, n$ 为整数, $n \geq m \geq 2, S$ 是一个 $n$ 元整数集合. 证明: $S$ 至少有 $2^{n-m+1}$ 个子集, 每个子集的元素和均被 $m$ 整除. (这里空集的元素和约定为 0.)

考虑在题 $5 . \mathrm{a}$ 中估计子集个数的上界. 为方便起见, 将模数取为素数 $p$, 当然还需要令集合中的元素均不是 $p$ 的倍数. 利用生成函数容易给出一个上界估计.

考虑问题能否继续改造. 突然想到能不能将“元素和”推广为“ $k$ 次基本对称多项式值”, 于是提出如下研究方向:

题 5.b. 给定素数 $p$ 以及正整数 $n, k$. 设 $A$ 是正整数集的 $n$ 元子集, 满足 $A$中的元素均不被 $p$ 整除. 对于 $A$ 的任意子集 $I$, 称 $I$ 是“好的”，如果 $|I| \geq k$ ，且多项式 $f(x)=\prod_{i \in I}(i x+1)$ 中 $x^{k}$ 项的系数被 $p$ 整除.

试估计 $A$ 的好的子集的个数的上界.

对于一般的 $k \geq 2$, 生成函数就不能奏效了, 需转而考虑组合方法. 经尝试发现若加上 “ $A$ 中元素 $\bmod p$ 互不相同”, 则比较好处理, 于是首先编制了下面
的中等难度的问题:

题 5.c. 给定素数 $p$ 以及正整数 $n, k, p>n>k \geq 1$. 设 $A$ 是 $\{1,2, \cdots, p-1\}$的 $n$ 元子集. 对于 $A$ 的任意子集 $I$, 称 $I$ 是“好的”，如果 $|I| \geq k$, 且多项式

$$
f(x)=\prod_{i \in I}(i x+1)
$$

中 $x^{k}$ 项的系数被 $p$ 整除.

证明: $A$ 的好的子集的个数不超过 $\frac{2 k}{n+1} \cdot 2^{n}$.

题 5.c 于 $2020-2021$ 寒假期间完成, 但当时笔者水平不足, 对一般的 $A$ 没有想出什么非平凡的估计. 后来集训队测试结束后笔者又重新考虑了题 $5 . b$, 并想到了一个比较好的估计, 就产生了题 5 .

考虑到本题难度太大, 为防止全场 0 分, 增设了 $k=1$ 的 1 分, 但遗憾的是还是没人得分.

## 第 6 题.

本题的灵感来源是某晚做梦时梦到了一个奇怪的方格表问题, 具体内容已记不清, 大概是在表格中填 $1, \cdots, 6$, 但表格中有些边变成了圆弧, 如下图:



醒来后, 受此启发, 希望命制一道方格填数的问题, 而这些圆弧边像是将若干对相邻方格标记为好对. 正巧当时还希望命制一道有趣的构造题, 于是想到可以让选手选取圆弧边, 要求填数方法数满足一些条件. 为对圆弧边的选取增加适当限制, 引入了二染色. 再经过一些尝试完善问题, 即得到了题 6 .

