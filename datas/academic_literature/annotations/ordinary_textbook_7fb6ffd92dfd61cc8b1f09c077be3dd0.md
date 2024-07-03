数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2020 年保加利亚数学竞赛试题解答与评析 

曾彦翔

(湖南省雅礼中学, 410007)

指导教师: 彭喜

保加利亚 2020 年数学奥林匹克试题, 命题角度新鲜, 题目简洁而富有挑战性, 是一套质量较高的数学奥林匹克试题. 全部的 6 个题中, 第 $1,2,4$ 题属简单题, 第 3 题和第 6 题属中档题, 第 5 题则为比较困难的问题.

## I. 试 题

1. 在 $\triangle A B C$ 中, 点 $Q, P, R$ 分别在线段 $A B, A Q, B C$ 上. $A R$ 与 $C P, C Q$的交点分别记作点 $M, N$. 若 $B C=B Q, C P=A P, C R=C N, \angle B P C=$ $\angle C R A$. 证明: $M P+N Q=B R$.
2. 已知实数 $a_{1}, a_{2}, \cdots, a_{n}$ 的和为 2 , 实数 $b_{0}, b_{1}, \cdots, b_{n}$ 满足 $b_{0}=b_{n}=0$,且 $\left|b_{i}-b_{i-1}\right| \leq a_{i}$, 其中 $i=1,2, \cdots, n$. 证明:

$$
\sum_{i=1}^{n} a_{i}\left(b_{i}+b_{i-1}\right) \leq 2
$$

3. 设 $a_{1}$ 为整数, 且对任意正整数 $n$, 有 $a_{n+1}=a_{n}^{2}-a_{n}-1$. 证明: 对任意正整数 $n, a_{n+1}$ 和 $2 n+1$ 互素.
4. 是否存在正整数 $m>4$ 和 $n$, 使得以下方程有解?
(1) $\left(\begin{array}{c}m \\ 3\end{array}\right)=n^{2}$;
(2) $\left(\begin{array}{c}m \\ 4\end{array}\right)=n^{2}+9$.
5. 平面上有 $n$ 个顶点, 其中的某些点之间有边相连, 这些边被染成黑白两色, 使得各存在一个同色哈密顿回路. 已知边 $A B$ 和 $B C$ 是白色, 证明: 我们可以将所有边重新进行红蓝染色, 使得 $A B$ 和 $B C$ 为红色, 且并非所有黑白边都被对应染成红蓝边, 且染色后各存在一个同色哈密顿回路.[^0]
6. 给定非常数实系数多项式 $f(x)$, 及严格单调递增且无界的实数列 $\left\{a_{i}\right\}_{i=1}^{\infty}$ 满足 $a_{i+1}<a_{i}+2020$. 将 $\left\lfloor f\left(a_{1}\right)\right\rfloor,\left\lfloor f\left(a_{2}\right)\right\rfloor, \cdots$ 依次排成一列数,其数码按顺序构成一个无穷数列 $\left\{s_{k}\right\}_{k=1}^{\infty}$, 其中 $s_{k} \in\{0,1, \cdots, 9\}, k=1,2, \cdots$.给定正整数 $n$, 证明: 对正整数 $k$, 在所有 $\overline{s_{n(k-1)+1} s_{n(k-1)+2} \cdots s_{n k}}$ 中, 所有 $n$ 位数都出现过.

## II . 解答与评注

1. 在 $\triangle A B C$ 中, 点 $Q, P, R$ 分别在线段 $A B, A Q, B C$ 上. $A R$ 与 $C P, C Q$的交点分别记作点 $M, N$. 若 $B C=B Q, C P=A P, C R=C N, \angle B P C=$ $\angle C R A$. 证明: $M P+N Q=B R$.

![](https://cdn.mathpix.com/cropped/2024_02_26_f68cdd0045a5e5341996g-2.jpg?height=379&width=506&top_left_y=1027&top_left_x=775)

证明 如图, 作 $\angle B C S=\angle Q C P$, 使得射线 $C S$ 与线段 $A B$ 相交, 设 $C S$交 $A B$ 于点 $S$.

于是, $\angle S C P=\angle R C N$, 而 $\angle B P C=\angle C R A$, 故 $\triangle S C P \sim \triangle N C R$.又 $C R=C N$, 故 $C S=C P=A P, \angle B S C=\angle M P A$.

由 $\angle B P C=\angle C R A$ 知 $B, P, M, R$ 四点共圆, 故 $\angle P M A=\angle S B C$, 于是 $\triangle B C S \cong \triangle M A P$.

设 $\angle B A C=\alpha$, 则 $\angle P C A=\alpha, \angle C N R=\angle C R N=\angle C P S=2 \alpha, \angle C S P=$ $2 \alpha$.

由 $C R=C N$ 及 $B C=B Q$ 知

$$
\angle B Q C=\angle B C Q=180^{\circ}-\angle C N R-\angle C R N=180^{\circ}-4 \alpha
$$

故 $\angle S C Q=\angle C S Q=2 \alpha$, 这即 $Q S=Q C$. 于是

$$
\begin{aligned}
M P+N Q & =B S+(C Q-C N) \\
& =B S+S Q-C R \\
& =B C-C R=B R
\end{aligned}
$$

命题得证.
评注 本题是一道简单的几何问题. 首先注意到欲证式的每一项都不能直接转化, 于是考虑等式两边同时添加一些项, 这亦是条件中许多线段相等所暗示的. 进一步, 便可知只需证明存在线段 $A B$ 上的点 $S$, 使得 $C S=C P$, $Q S=Q C$. 为此, 可以先按任一条件取出 $S$ 点, 再导角证明另一组等式即可.

2. 已知实数 $a_{1}, a_{2}, \cdots, a_{n}$ 的和为 2 , 实数 $b_{0}, b_{1}, \cdots, b_{n}$ 满足 $b_{0}=b_{n}=0$,且 $\left|b_{i}-b_{i-1}\right| \leq a_{i}$, 其中 $i=1,2, \cdots, n$. 证明:

$$
\sum_{i=1}^{n} a_{i}\left(b_{i}+b_{i-1}\right) \leq 2
$$

证明 记 $S_{i}=\sum_{k=1}^{i} a_{k}, T_{i}=\sum_{k=i}^{n} a_{k}$, 其中 $i=1,2, \cdots, n$. 补充定义 $S_{0}=$ $T_{n+1}=0, S_{n+1}=T_{0}=2$. 则对 $i=0,1, \cdots, n$ 都有

$$
S_{i}+T_{i+1}=2
$$

且 $\left\{S_{i}\right\}_{i=0}^{n+1}$ 单调不减, $\left\{T_{i}\right\}_{i=0}^{n+1}$ 单调不增. 注意到如下的局部不等式

$$
\begin{aligned}
& b_{i} \leq\left|b_{i}\right| \leq \sum_{k=1}^{i}\left|b_{k}-b_{k-1}\right| \leq \sum_{k=1}^{i} a_{k}=S_{i}, \\
& b_{i} \leq\left|b_{i}\right| \leq \sum_{k=i+1}^{n}\left|b_{k}-b_{k-1}\right| \leq \sum_{k=i+1}^{n} a_{k}=T_{i+1} .
\end{aligned}
$$

取 $i$ 为最小的使 $S_{i} \geq T_{i+1}$ 的 $i$, 则 $S_{i-1} \leq 1, T_{i+1} \leq 1$. 于是

$$
\begin{aligned}
\sum_{j=1}^{n} a_{j}\left(b_{j}+b_{j-1}\right)= & \sum_{j=1}^{i-1} a_{j}\left(b_{j}+b_{j-1}\right)+a_{i}\left(b_{i}+b_{i-1}\right)+\sum_{j=i+1}^{n} a_{j}\left(b_{j}+b_{j-1}\right) \\
\leq & \sum_{j=1}^{i-1} a_{j}\left(S_{j}+S_{j-1}\right)+a_{i}\left(S_{i-1}+T_{i+1}\right)+\sum_{j=i+1}^{n} a_{j}\left(T_{j}+T_{j+1}\right) \\
= & \sum_{j=1}^{i-1}\left(S_{j}^{2}-S_{j-1}^{2}\right)+\left(2-S_{i-1}-T_{i+1}\right)\left(S_{i-1}+T_{i+1}\right) \\
& +\sum_{j=i+1}^{n}\left(T_{j}^{2}-T_{j+1}^{2}\right) \\
= & 2-2\left(S_{i-1}-1\right)\left(T_{i+1}-1\right) \leq 2 .
\end{aligned}
$$

评注 本题是一道较为简单的代数题. 条件 $\left|b_{i}-b_{i-1}\right| \leq a_{i}$ 和 $\sum_{i=1}^{n} a_{i}=2$ 意味着 $\left\{b_{i}\right\}$ 不能有着很大的波动幅度, 自然地想到用 $\left\{a_{i}\right\}$ 的前缀和与后缀和来刻画对 $\left\{b_{i}\right\}$ 的限制. 另外，前缀和方法与差分方法都是处理序列不等式的有效工具.

3. 设 $a_{1}$ 为整数, 且对任意正整数 $n$, 有 $a_{n+1}=a_{n}^{2}-a_{n}-1$. 证明: 对任意正整数 $n, a_{n+1}$ 和 $2 n+1$ 互素.

证明 对于素数 $p$, 若 $p \mid a_{n}$, 则由数列的递推式知 $a_{n+2 k-1} \equiv-1(\bmod p)$, $a_{n+2 k} \equiv 1(\bmod p)$, 其中 $k=1,2, \cdots$. 这意味着数列中至多有一项为 $p$ 的倍数,故我们只需证明:

对于任意的素数 $p$, 若存在正整数 $k$ 使得 $p \mid a_{k}$, 则 $k<\frac{p+1}{2}$.

固定素数 $p>5$, 记 $V=\{0,1, \cdots, p-1\}, E=\left\{(u, v) \mid v \equiv u^{2}-u-1\right.$ $(\bmod p), u, v \in V\}$, 并以此构建有向图 $G(V, E)$. 由于每个点的出度为 1 , 故 $G$是若干形态为基环树 (树增加一条边) 的连通分支之并. 由于 0 所在的连通分支上的唯一的环已经确定为 $1 \rightarrow(p-1) \rightarrow 1$, 故只需证明, 以 0 为终点的链的长度不超过 $\frac{p-3}{2}$. 记以 0 为终点的最长链为 $V_{1} V_{2} \cdots V_{t}$, 其中 $V_{t}=0$.

引理 至多一个 $v$ 使得其入度恰为 1 , 对于其它入度不为 0 的点 $v$, 其入度恰为 2 .

证明 对于某个入度至少为 1 的点 $v$, 由定义, 存在 $u \in V$ 使得 $u^{2}-u-1 \equiv v$ $(\bmod p)$, 这即

$$
u \equiv 2^{-1}(1 \pm \sqrt{4 v+5}) \quad(\bmod p)
$$

其中 $2^{-1}$ 表示 2 的乘法逆元, 为 $\frac{p+1}{2}, \sqrt{x}$ 表示模 $p$ 意义下 $x$ 的平方根, 满足 $(\sqrt{x})^{2} \equiv x(\bmod p)$.

由条件, $4 v+5$ 在模 $p$ 意义下的平方根存在, 若 $v$ 入度恰为 1 , 则 $4 v+5$ 在模 $p$ 意义下的平方根唯一, 即 $4 v+5 \equiv 0$, 这样的 $v$ 显然是唯一的. 对于其它的 $v, 4 v+5$ 在模 $p$ 意义下的平方根恰有两个, 故其入度恰为 2 , 引理证毕.

回到原题. 设 $A=\left\{u \mid \exists i \in\{1,2, \cdots, t-1\}:\left(u, V_{i}\right) \in E\right\}$. 由于每个点出度恰为 1 , 结合引理, 知 $|A| \geq 2(t-1)-1=2 t-3$, 且这些点与 $V_{t-1}, 0,1, p-1,2$互异（因为由定义, 边 $(0, p-1),(1, p-1),(p-1,1),(2,1)$ 存在, 而 $G$ 的任意连通分支均为基环树）, 故 $|V| \geq|A|+5$, 即 $t \leq \frac{p-2}{2}$.

于是, 以 0 为终点的最长链长度不超过 $\left\lfloor\frac{p-2}{2}\right\rfloor=\frac{p-3}{2}$, 命题对 $p>5$ 得证.

![](https://cdn.mathpix.com/cropped/2024_02_26_f68cdd0045a5e5341996g-4.jpg?height=269&width=286&top_left_y=2284&top_left_x=608)

$p=3$ 时 $G$ 的形态

![](https://cdn.mathpix.com/cropped/2024_02_26_f68cdd0045a5e5341996g-4.jpg?height=279&width=491&top_left_y=2279&top_left_x=974)

$p=5$ 时 $G$ 的形态
对于 $p=3$ 和 $p=5$, 我们可以画出其对应的 $G$, 可知结论亦成立, 故命题得证.

评注 这是一道中等难度的数论题. 显而易见地, 我们必定要将与 $2 n+1$ 互素转化成与 $p$ (素数) 互素的问题. 而本题仅仅给了一个数列的递推式, 且我们不可能解出其通项, 故只能分析在模意义下的递推式的一些内在联系, 直观地则是考虑映射 $f: \mathbb{Z} / p \rightarrow \mathbb{Z} / p, f(x)=x^{2}-x-1$ 的等价图，而这便是解模意义下的二次方程. 最后寻找相异代表元的组合处理手法是经典的.

4. 是否存在正整数 $m>4$ 和 $n$, 使得以下方程有解?
(1) $\left(\begin{array}{c}m \\ 3\end{array}\right)=n^{2}$;
(2) $\left(\begin{array}{c}m \\ 4\end{array}\right)=n^{2}+9$.

解 (1) 存在. 事实上, $m=50, n=140$ 是唯一可能的解.

(2) 不存在. 将二项式系数拆开, 可得

$$
24\left(n^{2}+9\right)=m(m-1)(m-2)(m-3)=\left(m^{2}-3 m+1\right)^{2}-1,
$$

这即 $\left(m^{2}-3 m+1\right)^{2}=24 n^{2}+217$. 两边同时模 7 得

$$
\left(m^{2}-3 m+1\right)^{2} \equiv 3 n^{2} \quad(\bmod 7)
$$

但注意到 3 不为模 7 的二次剩余, 所以

$$
n \equiv 0 \quad(\bmod 7), m^{2}-3 m+1 \equiv 0 \quad(\bmod 7) .
$$

但 $7^{2} \nmid 217$, 矛盾! 故此方程无整数解.

评注这是一道中等偏易的数论题. 第一问是一个熟知的经典问题, Meyer, Wilhelm Franz 于 1878 年便已证明, 此方程的所有正整数解为 $(m, n)=$ $(3,1),(4,2),(50,140)$, 但对于不知道此结论的同学做起来仍稍有难度. 第二问的关键则在于观察到模 7 即可得出结论, 这是因为 7 是化简后的式子中常数项 217 的素因子, 取模、消项亦是做不定方程题的一个常用思路.

5. 平面上有 $n$ 个顶点, 其中的某些点之间有边相连, 这些边被染成黑白两色, 使得各存在一个同色哈密顿回路. 已知边 $A B$ 和 $B C$ 是白色, 证明: 我们可以将所有边重新进行红蓝染色, 使得 $A B$ 和 $B C$ 为红色, 且并非所有黑白边都被对应染成红蓝边, 且染色后各存在一个同色哈密顿回路.

证明 定义: 称 4-正则图 $G(V, E)$ 的边集的一个无序划分 $\{X, Y\}$ 为一个哈密顿分解, 当且仅当 $X$ 与 $Y$ 分别构成哈密顿回路. 对于边 $u, v$, 用 $P_{G}(u, v)$
表示使得 $u, v$ 在同一边集内的哈密顿分解所构成的集合, 用 $Q_{G}(u, v)$ 表示使得 $u, v$ 在不同边集内的哈密顿分解所构成的集合, 用 $R_{G}$ 表示 $G$ 的所有哈密顿分解构成的集合. 我们先证明如下引理:

引理 ${ }^{[1]}$ 对任意的 4-正则图 $G(V, E)$, 及任意的 $u, v \in E$, 有
A. $\left|P_{G}(u, v)\right|$ 为偶数.
B. $\left|Q_{G}(u, v)\right|$ 为偶数.
C. $\left|R_{G}\right|$ 为偶数.

证明 对于连接着同一个顶点的四条边 $w, w_{1}, w_{2}, w_{3}$, 注意到

$$
\left|R_{G}\right|=\left|P_{G}\left(w, w_{1}\right)\right|+\left|P_{G}\left(w, w_{2}\right)\right|+\left|P_{G}\left(w, w_{3}\right)\right|,
$$

因此, 在同一个图中, 命题 $\mathrm{A}$ 蕴含着命题 C. 而对于任意两条边, 有 $\left|P_{G}(u, v)\right|+$ $\left|Q_{G}(u, v)\right|=\left|R_{G}\right|$, 因此, 在同一个图中, 命题 $\mathrm{A}, \mathrm{C}$ 蕴含着命题 B.

我们对 $N=|V(G)|$ 来归纳证明 A 命题. 在 $\left|R_{G}\right|=0$ 时, 命题平凡, 故下设 $\left|R_{G}\right| \geq 1$.

在 $N=3$ 时, $G$ 的形态唯一, 只能是 ${ }^{2} K_{3}$ (每一条边复制一遍的完全图 $K_{3}$ ）, 此时显然地有 $\left|P_{G}(u, v)\right| \in\{0,2,4\}$, 为偶数.

假设命题 $\mathrm{A}, \mathrm{B}, \mathrm{C}$ 对于 $N-1$ 成立, 考虑 $N$ 时的命题:

先证明, 在 $u, v$ 有公共顶点时, $P_{G}(u, v)$ 为偶数. 设 $u=w_{1}, v=w_{2}, w_{3}, w_{4}$为某一个顶点 $x$ 连出的全部 4 条边, 其中边 $w_{i}(i=1,2,3,4)$ 连接着点 $x, x_{i}$.将 $G$ 中的顶点 $x$ 删去, 边 $w_{1}, w_{2}, w_{3}, w_{4}$ 删去, 并添加 $w_{5}=x_{1} x_{2}, w_{6}=x_{3} x_{4}$,得到的新图记作 $G^{\prime}$, 则 $G^{\prime}$ 是 4- 正则的, 且 $\left|V\left(G^{\prime}\right)\right|=N-1$. 于是, 每一个使得 $w_{1}, w_{2}$ 在同一边集内的 $G$ 的哈密顿分解, 与某个使得 $w_{5}, w_{6}$ 在不同边集内的 $G^{\prime}$ 的哈密顿分解一一对应, 由归纳假设, 即 $\left|P_{G}(u, v)\right|=\left|P_{G}\left(w_{1}, w_{2}\right)\right|=$ $\left|Q_{G^{\prime}}\left(w_{5}, w_{6}\right)\right| \equiv 0(\bmod 2)$.

![](https://cdn.mathpix.com/cropped/2024_02_26_f68cdd0045a5e5341996g-6.jpg?height=411&width=420&top_left_y=2010&top_left_x=818)

由之前的分析, 这蕴含着 $\left|R_{G}\right| \equiv 0(\bmod 2)$. 因此, 在 $u=v$ 时, 有

$$
\left|P_{G}(u, v)\right|=\left|P_{G}(u, u)\right|=\left|R_{G}\right| \equiv 0 \quad(\bmod 2)
$$

下面考虑 $u, v$ 没有公共顶点时的情形. 由最初的假设, $G$ 存在至少一个哈密顿分解, 因此, 存在一系列的边 $u=W_{0}, W_{1}, W_{2}, \cdots, W_{t-1}, W_{t}=v$, 使得 $W_{i}$与 $W_{i+1}$ 有公共顶点对 $i=0,1, \cdots, t-1$ 均成立.

注意到如下显然的事实：对于任意的三条边 $x, y, z$, 有 $Q_{G}(x, y)=$ $P_{G}(x, z) \Delta P_{G}(z, y)$, 其中 $\Delta$ 表示集合的对称差. 这是因为, $x$ 与 $y$ 分别属于两个边集, 当且仅当 $z$ 恰与其中一个属于同一边集. 由此可知

$$
\begin{aligned}
\left|P_{G}\left(W_{0}, W_{i+1}\right)\right| & =\left|R_{G}\right|-\left|Q_{G}\left(W_{0}, W_{i+1}\right)\right| \\
& \equiv 0-\left|P_{G}\left(W_{0}, W_{i}\right) \Delta P_{G}\left(W_{i}, W_{i+1}\right)\right| \\
& \equiv\left|P_{G}\left(W_{0}, W_{i}\right)\right|+\left|P_{G}\left(W_{i}, W_{i+1}\right)\right| \\
& \equiv\left|P_{G}\left(W_{0}, W_{i}\right)\right| \quad(\bmod 2)
\end{aligned}
$$

这即

$\left|P_{G}(u, v)\right|=\left|P_{G}\left(W_{0}, W_{t}\right)\right| \equiv\left|P_{G}\left(W_{0}, W_{t-1}\right)\right| \equiv \cdots \equiv\left|P_{G}\left(W_{0}, W_{1}\right)\right| \equiv 0 \quad(\bmod 2)$

因此命题 A 对 $N$ 亦成立, 即命题 A, B, C 对 $N$ 成立, 归纳完毕. 这即证明了引理.

回到原题. 取题述的 $n$ 个点为顶点, 任取黑白哈密顿回路各一个为边, 构成的图记作 $G(V, E)$, 则 $G$ 是 $4-$ 正则的. 由引理, $\left|P_{G}(A B, B C)\right| \equiv$ $0(\bmod 2)$. 而这些边按黑白染色的方式划分, 本身即为一个哈密顿分解,且 $A B, B C$ 属于同一个边集（均为白色）, 这即 $\left|P_{G}(A B, B C)\right| \geq 1$, 且为偶数,于是 $\left|P_{G}(A B, B C)\right| \geq 2$.

这说明 $G$ 存在另一种哈密顿分解, 且 $A B, B C$ 同属一个边集. 将这些边按所属边集进行红蓝染色, 其它不在 $G$ 中的边任意染色, 则分别存在一个红色和蓝色的哈密顿回路, 且并非所有黑白边都被对应染成红蓝边, 命题得证.

评注 本题是一道困难的组合问题. 可以观察到, 本题的设问仅仅是引理的一个极其特殊的情况, 但为了证明问题, 似乎不可避免地要连带着归纳证明全部 $A, B, C$ 部分. 事实上, 找到一个可以归纳的命题并非易事, 往往需要如本题的引理一般, 附加许多额外的命题一起归纳。

通常, 我们先尝试直接归纳证明原问题, 但往往会发现, 所给的条件并不足以完成归纳, 我们必须添加一些条件, 而这导致的将是还需归纳证明这些命题.在一些问题中（例如本题），我们可以将这一过程不断迭代，最终将找到一个可以归纳的问题.

从题目角度来看, 去证明引理比证明原题将简单许多, 尽管引理相比原题证
明地更多一些, 但另一方面,引理给出了一个完整的、可归纳的命题.

事实上, 本题的引理早在 1978 年便已由 A.G. Thomason 证明. 在近年的竞赛题中, 有关哈密顿回路的问题则较为少见. 另外, 在限定的时间内做好本题并非易事。

6. 给定非常数实系数多项式 $f(x)$, 及严格单调递增且无界的实数列 $\left\{a_{i}\right\}_{i=1}^{\infty}$ 满足 $a_{i+1}<a_{i}+2020$. 将 $\left\lfloor f\left(a_{1}\right)\right\rfloor,\left\lfloor f\left(a_{2}\right)\right\rfloor, \cdots$ 依次排成一列数,其数码按顺序构成一个无穷数列 $\left\{s_{k}\right\}_{k=1}^{\infty}$, 其中 $s_{k} \in\{0,1, \cdots, 9\}, k=1,2, \cdots$.给定正整数 $n$, 证明: 对正整数 $k$, 在所有 $\overline{s_{n(k-1)+1} s_{n(k-1)+2} \cdots s_{n k}}$ 中, 所有 $n$ 位数都出现过.

证明 设 $f(x)=\sum_{i=0}^{r} p_{i} x^{i}, g(x)=\frac{f(x+1)}{f(x)}$, 则有

$$
\begin{aligned}
\lim _{x \rightarrow \infty} g(x) & =\lim _{x \rightarrow \infty} \frac{f(x+1)}{f(x)}=\lim _{x \rightarrow \infty} \frac{\sum_{i=0}^{r}\left(\sum_{j=i}^{r}\left(\begin{array}{l}
j \\
i
\end{array}\right) p_{j}\right) x^{i}}{\sum_{i=0}^{r} p_{i} x^{i}} \\
& =\lim _{x \rightarrow \infty} \frac{\sum_{i=0}^{r}\left(\sum_{j=i}^{r}\left(\begin{array}{l}
j \\
i
\end{array}\right) p_{j}\right) x^{i-r}}{\sum_{i=0}^{r} p_{i} x^{i-r}}=\frac{p_{r}}{p_{r}}=1 .
\end{aligned}
$$

记 $b_{i}=a_{i+1}-a_{i}$, 则 $b_{i}<2020$. 不妨设 $f$ 首项系数为正, 则对于足够大的 $m$ 有

$$
1<\frac{f\left(a_{m+1}\right)}{f\left(a_{m}\right)}=\frac{f\left(a_{m}+b_{m}\right)}{f\left(a_{m}\right)}<\frac{f\left(a_{m}+2020\right)}{f\left(a_{m}\right)}=\prod_{i=a_{m}}^{a_{m}+2019} g(i) .
$$

而 $\lim _{x \rightarrow \infty} g(x)=1$, 故 $\lim _{m \rightarrow \infty} \frac{f\left(a_{m+1}\right)}{f\left(a_{m}\right)}=1$.

对于 $n$ 位数 $c=\overline{u_{1} u_{2} \cdots u_{n}}$, 记 $d=\overline{u_{1} u_{2} \cdots u_{n} 0 \cdots u_{1} u_{2} \cdots u_{n} 0}(10 \times c$ 重复 $n$ 遍).

注意到 $\frac{(d+1) \times 10^{T}}{d \times 10^{T}}=\frac{d+1}{d}>1$, 由前述及介值原理, 对于足够大的 $T$, 存在 $i$使得

$$
\left\lfloor f\left(a_{i}\right)\right\rfloor \in\left[d \times 10^{T},(d+1) \times 10^{T}\right) .
$$

这即 $\left\lfloor f\left(a_{i}\right)\right\rfloor$ 具有 $d$ 前缀.

因此, $\left\{s_{k}\right\}_{k=1}^{\infty}$ 中存在连续的 $n(n+1)$ 位恰为 $d$, 这即, 在所有的

$$
\overline{s_{n(k-1)+1} s_{n(k-1)+2} \cdots s_{n k}}
$$

中, $c$ 出现过. 由 $c$ 的任意性知命题成立.

评注 本题是一道中等难度的代数题. 此类问题, 通常值的前若干位是可以取到任意值的, 这是一个介值原理的经典结论. 本题的条件则更具导向性, 由于考虑的数列中含有取整函数, 故不可能用数论手段处理值的末位.

## 参考文献

[1] Dragomir Grozev's Math Blog. Bulgarian NMO, 2020, part I. https://dgrozev. wordpress.com/2020/07/06/bulgarian-nmo-2020-part-i/


[^0]:    修订日期: 2020-08-23.

