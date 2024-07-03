# 竞赛图中的两个有趣结论 

廖悦辛<br>(华中师范大学第一附属中学, 430223)

本文介绍竞赛图中两个有趣结论的证明, 文中需要用到如下几个常用的引理 (见文 [1]).

引理 1 竞赛图 $K_{n}$ 中存在一条长为 $n-1$ 的哈密顿路.

引理 2 竞赛图 $K_{n}$ 有一个唯一强连通分支的成链状的排列, 其排列为: $K_{1}, K_{2}, \cdots, K_{h}$, 满足对任意的 $i, j(i<j)$, 不存在从 $K_{j}$ 到 $K_{i}$ 的弧.

引理 3 任何一个强连通竞赛图 $K_{n}$, 均有一条哈密顿圈.

引理 4 顶点个数大于 3 的竞赛图 $K_{n}$ 中至少存在 2 个不同的顶点 $x$ 和 $y$,使得 $K-x, K-y$ 均为强竞赛图.

下面介绍两个结论及其证明.

结论 1 (穆恩定理) 设 $p \geq 4,3 \leq n \leq p$, 则 $p$ 阶强连通竞赛图任何一个节点都在长度为 $n$ 的圈上

证法一 (穆恩) 设 $v$ 是强连通竞赛图 $D$ 的任意一个节点. 对 $n$ 归纳, 首先证明点 $v$ 在长度为 3 的圈上. 令 $S=N^{+}(v), T=N^{-}(v)$ 分别是 $v$ 的出度点、入度点的点集, 则 $S, T, E(S, T)$ 均为非空集合. 所以 $v$ 在长度为 3 的圈上.

现在不妨设 $v$ 在一个长度为 $k$ 的圈上 $(3 \leq k<p)$, 我们证明其在长度为 $k+1$ 的圈上. 设 $C=\left(v_{1}, v_{2}, \cdots, v_{k}\right)$ 是过 $v$ 长度为 $k$ 的圈, 记 $v=v_{1}$. 若存在一点 $u$ 不为 $C$ 中的点, 使得 $N^{+}(u) \cap C \neq \emptyset, N^{-}(u) \cap C \neq \emptyset$, 则存在 $i(1 \leq i \leq k)$使得 $\left(u, v_{i+1}\right) \in E\left(v_{i}, u\right) \in E$,

于是 $C^{\prime}=\left(v_{1}, v_{2}, \cdots, v_{i}, u, v_{i+1}, \cdots, v_{k}, v_{1}\right)$ 是过 $v$ 长度为 $k+1$ 的圈. 另一面, 若任意一个不在点集 $C$ 中的点, 或者 $N^{+}(u) \cap C \neq \emptyset$, 或者 $N^{-}(u) \cap C \neq \emptyset$,[^0]则令

$$
S=\left\{u \notin C \mid N^{+}(u) \cap C \neq \emptyset\right\}, \quad T=\left\{u \notin C \mid N^{-}(u) \cap C \neq \emptyset\right\} .
$$

显然, $S \neq \emptyset, T \neq \emptyset$. 则 $E(S, T) \neq \emptyset$. 设 $u, w \in E(S, T)$, 则 $u \in S, w \in T$. 故 $C^{\prime \prime}=\left(v_{1}, u, w, v_{3}, \cdots, v_{k}, v_{1}\right)$ 是过 $v_{1}$ 的长度为 $k+1$ 的圈.

综上, 由数学归纳法, 知原命题成立.

证法二 (笔者) 对于 $T$ 中任意一个节点 $V$, 当强竟赛图 $T$ 顶点数为 3 , 结论平凡. 若强竞赛图 $T$ 的顶点数大于 3 , 由于 $T$ 是一个强竞赛图, 由引理 3 知 $v$ 必在强竞赛图 $\mathrm{T}$ 的哈密顿有向回路上, 即 $T$ 中包含一个包含 $v$ 长度为 $p$ 的有向圈.则根据引理 $2, T$ 至少存在两个互异的顶点 $\{x, y\}$ 使得 $T-x, T-y$ 均为强竞赛图.

由引理 3 , 知强竞赛图 $T-x$ 中任意一个顶点均在长度为 $p-1$ 的有向圈上,强竞赛图 $T-y$ 中任意一个顶点也在长度为 $p-1$ 的有向圈上, 由于 $x, y$ 互异,故 $v$ 至少属于 $T-x, T-y$ 之一. 故 $T$ 中存在一个包含 $v$ 长度为 $p-1$ 的有向圈.类似递推, 强竞赛图 $T$ 中顶点逐渐减少, 最后 $v$ 在强竞赛图 $T_{4}$ 时, $T$ 中存在一个包含 $v$ 的长度为 3 的有向圈.

由 $v$ 的任意性, 我们可以依次找到过任意节点长度为 $p, p-1, \cdots, 3$ 的圈.命题得证.

评注 笔者的解法出发点基于强竞赛图的递归特性的探寻.

下面介绍一则笔者根据这个结论自编的一个组合问题:

问题 若给定 $N>M>1$, 若任意两个城市有来往的航线, 一个人坐飞机游遍 $N$ 个城市. 每两个城市去或往一次. $m \rightarrow n$ 表示从 $m$ 乘航线去 $n$. 已知若有 $M$ 个城市满足 $A_{0} \rightarrow A_{1} \rightarrow \cdots \rightarrow A_{M}$, 则有 $A_{0} \rightarrow A_{M}$, 证明: 可将 $N$ 个城市排为 $1,2, \cdots N$ 的一个排列满足任意 $i, j, i \geq j+M+1$ 时有 $i \rightarrow j$.

证明 首先证明如下的引理.

引理 5 给定无哈密顿圈的竞赛图 $G$, 则其可以划分为两个非空子集 $M, N$,使得任意 $m \in M, n \in N$, 在 $G$ 中有 $m \rightarrow n$ 的边.

引理证明 利用 “贪心算法” 的想法, 先考虑极端情况, 若存在一点 $u \in G$,对任意 $v \in G \backslash\{u\}$, 均有 $u \rightarrow v$, 令 $M=\{u\}, N=G \backslash\{u\}$ 即可. 若均有 $v \rightarrow u$,则令 $N=\{u\}, M=G \backslash\{u\}$ 即可.
接下来则只需要考虑每一个点均有出度和入度的情形, 易知此时必会形成圈. 不妨去边数最大的圈 $a_{1} \rightarrow \cdots \rightarrow a_{t} \rightarrow a_{1}(t \leq n-1)$. 取 $x \in G \backslash A$,则若存在 $a_{i}, a_{i+1}$, 使得 $a_{i} \rightarrow x \rightarrow a_{i+1}$, 则会形成边数边数更大的圈, 矛盾.故对不在 $G-A$ 的点 $x$, 恒有 $a_{i} \rightarrow x$ 或 $x \rightarrow a_{i}(i=1,2 \cdots t)$. 设满足前者 $x$ 的点集为 $B$, 满足后者 $x$ 的点集为 $C$. 任取 $b \in B, c \in C$, 若 $c \rightarrow b$ 则有 $a_{1} \rightarrow c \rightarrow b \rightarrow a_{2} \rightarrow \cdots \rightarrow a_{t} \rightarrow a_{1}$. 形成了更大圈, 矛盾. 故恒有 $b \rightarrow c$. 此时取 $M=B, N=C \cup A$ 满足题意. 引理 5 得证.

回到原题. 将城市视为点, 航线视为弧, 构造竞赛图 $G$. 接下来说明 $N$ 个城市构成的竞赛图中没有长度大于 $M$ 的圈. 若存在长度大于 $M$ 的圈, 不妨设为 $a_{1} \rightarrow \cdots \rightarrow a_{t} \rightarrow a_{1}(t \geq M+1)$ 而其为强连通的子图, 由结论一其必存在长度为 $M+1$ 的圈, 与题设若 $a_{0} \rightarrow a_{1} \rightarrow \cdots \rightarrow a_{M}$, 则有 $a_{0} \rightarrow a_{M}$ 矛盾. 故该图所有圈长均不超过 $M$.

利用引理 5 , 可以将 $G$ 分为 $k$ 个不相交的组 $A_{1}, A_{2}, \cdots \cdots A_{k}$, 任意 $i<j, x \in$ $A_{i}, y \in A_{j}$, 有 $x \rightarrow y$, 且每个 $A_{i}$ 均有哈密顿圈. 而 $A_{i}$ 的长度至多为 $M$, 将 $A_{1}$ 的人排列为 $1,2 \cdots,\left|A_{1}\right|$, 满足 $\left|A_{1}\right| \rightarrow 1$, 将 $A_{2}$ 的人排列为 $\left|A_{1}\right|+1,\left|A_{1}\right|+$ $2, \cdots,\left|A_{1}\right|+\left|A_{2}\right|$, 满足 $\left|A_{1}\right|+\left|A_{2}\right| \rightarrow\left|A_{1}\right|+1$. 以此类推, 可以对剩下组的点做这样的排序, 满足这个人所乘航线都是从每组最后一个城市通往第一个城市, 排好后按以上排列顺序将 $N$ 个城市排为对应的 $1,2, \cdots, N$, 其具有如下性质: 若 $i \geq j+M-1$, 因为每组至多 $M$ 个城市, 若 $i, j$ 同组, 则 $j$ 为该组第一个城市, $i$为最后一个城市, 有 $i \rightarrow j$; 若 $i, j$ 不同组, 则 $i$ 所在组号大于 $j$ 所在组号, 也有 $i \rightarrow j$.

综上, 以上排序满足题意.

结论 $2 n$ 阶竞赛图中的哈密顿链个数为奇数.

证法一 ([3]) 利用调整的思想, 设 $T$ 是一个竞赛图, $h(T)$ 为 $T$ 中的哈密顿链的个数. 设 $T$ 的顶点集为 $\left\{V_{1}, V_{2}, \cdots, V_{n}\right\}$ 将 $V_{i}$ 与 $V_{j}$ 的边改变方向得到一个新的图 $T^{\prime}$.

只需证明 $h(T)+h\left(T^{\prime}\right) \equiv 0(\bmod 2)$. 这是因为若有 $h(T)+h\left(T^{\prime}\right) \equiv 0$ $(\bmod 2)$, 则有 $h(T) \equiv h\left(T^{\prime}\right)(\bmod 2)$, 可知所有自同构的竞赛图的哈密顿链个数均模 2 同余. 又注意到存在链: 任取 $i<j$, 均有 $V_{i} \rightarrow V_{j}$, 则这个竞赛图有且仅有一条链 $V_{1} \rightarrow V_{2} \rightarrow \cdots \rightarrow V_{n}$, 即知所有竞赛图哈密顿链个数均为奇数.
设 $e$ 为 $V_{i} V_{j}$. 我们对 $h(T)+h\left(T^{\prime}\right)$ 分类计数:

$$
\begin{aligned}
h(T)+h\left(T^{\prime}\right) & \equiv h(T-e)+h(\text { 带 } e)+h\left(T^{\prime}-e\right)+h\left(\text { 带 } e^{\prime}\right) \\
& =h(T-e)+h(\text { 带 } e)+h(T-e)+h\left(\text { 带 } e^{\prime}\right) \\
& =h(T-e)+h\left(T+e^{\prime}\right) \\
& =h(T-e \text { 全反向 })+h\left(T+e^{\prime}\right) .
\end{aligned}
$$

注意到 $T-e$ 全反向与 $T+e^{\prime}$ 互为补图, 故 $h(T)+h\left(T^{\prime}\right) \equiv 0(\bmod 2)$ 等价任意竞赛图 $G, h(G) \equiv h\left(G^{\prime}\right)(\bmod 2)$, 这里 $G^{\prime}$ 表示 $G$ 的补图.

令 $A_{i}$ 为含边 $e_{i}$ 的 $n$ 阶双向完全图的哈密顿链组成的集合, $S$ 表示 $n$ 阶双向完全图中的哈密顿链的个数. 利用容斥原理,

$$
h\left(G^{\prime}\right)=\sum_{k \geq 0} \sum_{a_{1} \leq a_{2} \cdots \leq a_{k}}\left|A_{a_{1}} \cap A_{a_{2}} \cap \cdots \cap A_{a_{k}}\right|(-1)^{k}(k=0 \text { 时表示全集 }) .
$$

注意到 $\left|A_{a_{1}} \cap A_{a_{2}} \cap \cdots \cap A_{a_{k}}\right|=(V(G)-k)$ ! 为偶 $(k<V(G)-1) ; \mid A_{a_{1}} \cap A_{a_{2}} \cap \cdots \cap$ $A_{a_{k}} \mid$ 为 $0(k \geq V(G)$ 时 $)$ ，为 $h(G)(k=V(G)-1$ 时 $)$, 故 $h(G) \equiv h\left(G^{\prime}\right)(\bmod 2)$,故 $h(G)+h\left(G^{\prime}\right) \equiv 0(\bmod 2)$. 取 $G=T$, 故 $h(T)+h\left(T^{\prime}\right) \equiv 0(\bmod 2)$.

综上所述, 命题得证.

证法二 (上海中学杨铮) 记竞赛图 $G$ 的顶点组成的集合为 $V$, 对任意 $l \in N$ 和 $V$ 中的 $L+1$ 个顶点 $V_{0}, V_{1}, \cdots, V_{L}$, 记 $G\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 为将 $G$ 中所有连接 $V_{i}$ 和 $V_{i+1}$ 的边都改成双向 (即两个方向均有, $i \in\{0,1, \cdots, L-1\}$ ) 后得到的图. 特别的, 任取 $V_{0} \in V$, 有 $G\left(V_{0}\right)=G$. 对 $G\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 中一条哈密顿链 $S$, 称 $S$ 是好的当且仅当 $S$ 有一条子链 $\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 或 $\left(V_{L}, V_{L-1}, \cdots, V_{0}\right)$特别的, 对 $V$ 中的任意一个顶点 $V_{0}, G\left(V_{0}\right)=G$ 中任意一条哈密顿链都是好的.默认边集为空集的链是空的.

下面加强命题: 对 $l \in N(0 \leq l \leq n-1)$ 和 $V$ 中 $L+1$ 个顶点 $V_{0}, V_{1}, \cdots, V_{L}$有 $G\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 在 $L=0$ 时为奇数个好链, $L \neq 0$ 时为偶数个好链.

对 $L$ 采取反向归纳.

当 $L=n-1$ 时, $G\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 中所有好链为 $\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 和 $\left(V_{L}, V_{L-1} \cdots, V_{0}\right)$. 因此 $G$ 在 $n=1$ 时有 1 条好链. $n \geq 2$ 时, 有 2 条好链.命题成立.

下设 $L=L^{\prime}+1$ 时命题成立 $\left(L^{\prime} \in N, L^{\prime} \leq n-2\right)$. 并记 $L=L^{\prime}+1$ 时, $G\left(V_{0}, V_{1}, \cdots, V_{L}\right)$ 中好链个数为 $P\left(L^{\prime}+1\right)$.

再考虑 $L=L^{\prime}$ 的情况. 对任意 $L^{\prime}+1$ 个顶点 $V_{0}, V_{1}, \cdots, V_{L^{\prime}}$, 先证明对任意
$t \in\left\{0, L^{\prime}\right\}$ 和 $v \in U \backslash\left\{V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right\}$ 若将 $\left\{V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right\}$ 中 $V_{t}, V$ 的边改变方向, 则 $G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)$ 中好链数量奇偶性不变.

注意到当 $v t, v$ 的边改变方向时, 记原先 $V_{t}, V$ 间的边为 $e$, 现在 $V_{t}, V$ 间的边为 $e^{\prime}$, 并记原来好链的集合为 $L_{1}$, 将 $e$ 换为 $e^{\prime}$ 后链的集合为 $L_{2}$, 则 $L_{1} \backslash L_{2}=\left\{L \mid L \in L_{1}, e\right.$ 为 $L_{2}$ 的一条边 $\}, L_{2} \backslash L_{1}=\left\{L \mid L \in L_{2}, e\right.$ 为 $L_{1}$ 的一条边 $\}$.而 $G\left(V_{0}, V_{1}, \cdots, v_{L^{\prime}}\right)$ 加上 $e^{\prime}$ 即为

$$
G\left(V, V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)(t=0), \quad G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}, v\right)\left(t=L^{\prime}\right)
$$

不妨将其简记为 $G\left(V_{0}, V_{1}, \cdots, v_{L^{\prime}}\right)^{\prime}$, 则

$$
\left(L_{1} \backslash L_{2}\right) \cup\left(L_{2} \backslash L_{1}\right)=\left\{L \mid L \text { 在 } G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)^{\prime} \text { 中的好链 }\right\} \text {. }
$$

故由归纳假设 $P\left(L^{\prime}+1\right)$ 知 $\left|\left(L_{1} \backslash L_{2}\right) \cup\left(L_{2} \backslash L_{1}\right)\right|$ 为偶数, 故

$$
\left.\left|L_{1}\right|-\left|L_{2}\right| \equiv\left|L_{1}\right|+\left|L_{2}\right| \equiv \mid L_{1} \backslash L_{2}\right) \cup\left(L_{2} \backslash L_{1}\right) \mid \equiv 0 \quad(\bmod 2),
$$

即 $\left|L_{1}\right| \equiv\left|L_{2}\right|(\bmod 2)$. 故命题 $(* *)$ 证明完毕.

再证明 $L=L^{\prime}$ 时命题成立.

$L^{\prime} \neq 0$, 反复使用 $(* *)$ 知 $G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)$ 中好链个数奇偶性和如下 $G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)^{\prime \prime}$ 中好链个数奇偶性相同. 其中 $G\left(V_{0}, V_{1}, \cdots, v_{L^{\prime}}\right)^{\prime \prime}$ 定义为是将 $G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)$ 中所有形如 $U \rightarrow V_{t}$ 的边 (此外 $U \in V \backslash\left\{V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right\}, t \in$ $\left.\left\{0, L^{\prime}, 1\right\}\right)$ 全部换为 $V_{t} \rightarrow U$ 后所得的图.

只需证明 $G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)^{\prime \prime}$ 中好链个数为偶数.

而注意到: $G\left(V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right)^{\prime \prime}$ 中的每个好链 $S, S$ 必形如 $\left(V_{0} V_{1}, \cdots, V_{L^{\prime}}\right.$, $\left.W_{1}, W_{2}, \cdots, W_{n-1-L^{\prime}}\right)$ 或 $\left(V_{L^{\prime}}, V_{L^{\prime}-1}, \cdots, V_{0}, W_{1}, W_{2}, \cdots, W_{n-1-L^{\prime}}\right)$ 的形式. 其中 $W_{1}, W_{2}, \cdots, W_{n-1-L^{\prime}}=V \backslash\left\{V_{0}, V_{1}, \cdots, V_{L^{\prime}}\right\}$. 这两种链可以两两配对, 将每个 $\left(V_{0}, V_{1} \cdots, V_{L^{\prime}}, X_{1}, X_{2}, \cdots, X_{n-1-L^{\prime}}\right)$ 和 $\left(V_{L^{\prime}}, V_{L^{\prime}-1}, \cdots, V_{1}, V_{0}, X_{1}, X_{2}, \cdots, X_{n-1-L^{\prime}}\right)$配对.

故 $L=L^{\prime}$ 时, 命题 $(*)$ 成立.

当 $L^{\prime}=0$ 时, 命题 (**) 即: 将 $G$ 的任一条边改变方向后 $G$ 的哈密顿链数量的奇偶性不变. 故只需证明某一个有 $n$ 个顶点的竞赛图有奇数条哈密顿链. 我们只需取这个竞赛图的顶点集为 $V=\left(V_{1}, V_{2}, \cdots, V_{n}\right)$, 边集 $E$ 为 $\left\{V_{i} \rightarrow V_{j} \mid 1 \leq i<j \leq n\right\}$ 则只有一条哈密顿链. 因此 $L=L^{\prime}$ 时命题成立.

综上, 由数学归纳法知任取 $L \in N(0 \leq L \leq n-1)$ 均有命题 (*) 成立.
回到原题, 将 $L=0$ 代入即为所证.

评注 这是一道形式简单, 却很困难的问题. 因为难以找到对竞赛图哈密顿链个数定量的刻画, 只能从侧面入手, 运用其他的手段去做一些变换. 调整命题.解法一通过找将 $e$ 调换方向这一神奇的变换把原命题转换为图与补图哈密顿链个数的奇偶性相同, 再通过容斥原理计数说明这一点. 解法二中杨铮同学的做法的出发点基于反复在尝试套用不断改变边的方向. 从而发现了加强命题, 进而做出对好链的定义, 然后归纳.

致谢 笔者感谢李建国老师的指导和冯跃峰老师帮忙修改了本文!

## 参考文献

[1] 王琦, 刘晓姗, 赵红銮. 强竞赛图的强连通性 [J]. 计算机工程与应用, 2007, $43(6)$.

$[2]$ 任韩. 数学奥林匹克命题人讲座 - 图论 [M]. 上海科学技术出版社, 2009.10.

[3] Titu Andreescu, Gabriel Dospinescu. Problems from the BOOK [M]. XYZ Press(2nd), 2010.08.


[^0]:    修订日期: 2019-07-04.

