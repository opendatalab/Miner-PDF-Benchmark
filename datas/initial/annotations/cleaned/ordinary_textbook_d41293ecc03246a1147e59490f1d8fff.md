数学新星网 $*$ 聂子佩专栏

www.nsmath.cn/nzpzl

# 两道方格表染色问题的归纳解法和分治策略 

聂子佩

在本文中我们将探讨两个与方格表染色有关的竞赛问题, 首先是第 7 届全苏联数学奥林匹克十年级组第三题, 这题的出现显然是由于在 Conway 的生命游戏中得到的启发.

问题 1. 在无限大的方格棋盘上选择 $n$ 个方格组成集合 $G_{0}$. 在初始时刻 $G_{0}$ 中的方格都被染成黑色, 其余方格都被染成白色. 在每个接下来的时刻 $t=$ $1,2, \cdots$, 我们按以下规则将所有方格同时染色: 若方格 $(x, y),(x+1, y),(x, y+1)$中至少有两个在上一时刻是白色, 则 $(x, y)$ 将会变成白色; 反之, 若方格 $(x, y)$, $(x+1, y),(x, y+1)$ 中至少有两个在上一时刻是黑色, 则 $(x, y)$ 将会变成黑色.令 $G_{k}$ 是时刻 $t=k$ 中被染成黑色的方格的集合. 证明 $G_{n}=\emptyset$.

首先, 我们想证明在每个时刻黑色方格的数量会严格减少. 然而, 这是不成立的. 尽管这样, 我们仍然可以用数学归纳法证明此题. 下面这个归纳解法并非笔者的创作, 而是当时十年级的学生 A. Gomilko 在考场上的解答. 该考生因此拿了特别奖, 这个解法也收录在苏淳编著的《苏联中学生数学奥林匹克试题汇编 (1961-1992)》一书中.

欲证命题对 $n=0$ 成立. 假设命题对任何非负整数 $k<n$ 成立, 我们将证明它也对 $n$ 成立.

取最小的矩形 $R$, 使得 $R$ 是包括 $G_{0}$ 中的所有方格在内的一些方格的并集.记 $G_{0}^{\prime}$ 为 $G_{0}$ 中所有不在 $R$ 的最下面一行的所有方格的集合, 同样, 记 $G_{0}^{\prime \prime}$ 为 $G_{0}$中所有不在 $R$ 的最左边一列的所有方格的集合. 注意到 $R$ 的最下面一行不会影响在它之上的方格的未来, $R$ 的最左边一列同样也不会影响在它右边的方格的未来. 对初始集合 $G_{0}^{\prime}$ 与 $G_{0}^{\prime \prime}$ 利用归纳假设, 我们可以推断 $G_{n-1}$ 只可能包含 $R$的左下角这一个方格. 故 $G_{n}=\emptyset$. 命题得证.

现在, 我们将使用分治策略作出另一种解答. 所谓分治策略, 即是把一个关[^0]于整体的命题分为一些关于部分的命题逐个击破, 正如使用鸽巢原理的关键在于如何选择鸽巢一样, 使用分治策略的关键在于如何选择小命题.

用反证法, 设 $v_{n} \in G_{n}$. 对 $1 \leq k \leq n$, 若已经选好了 $v_{k} \in G_{k}$, 由规则知, 我们可以选择 $v_{k-1} \in G_{k-1}$, 使得 $v_{k-1}$ 在 $v_{k}$ 的右边或者上面, 且与 $v_{k}$ 恰有一条公共边. 对 $1 \leq k \leq n$, 若 $v_{k-1}$ 在 $v_{k}$ 的右边, 令 $R_{k}$ 为 $v_{k}$ 所在的列中不在 $v_{k}$ 的下面的所有方格的集合; 反之, 若 $v_{k-1}$ 在 $v_{k}$ 的上面, 令 $R_{k}$ 为 $v_{k}$ 所在的行中不在 $v_{k}$ 的左边的所有方格的集合. 我们可以证明这些 $R_{k}$ 两两不交, 且与 $G_{0} \backslash\left\{v_{0}\right\}$都有交点. 如此, 便有了 $\left|G_{0}\right| \geq n+1$.

对比归纳解法和分治策略, 我们发现, 由于归纳解法只需要考虑边界上的情况, 我们常常可以得到比较简洁的证明, 但当边界的条件有所改变时, 我们的证明就需要有所改变, 且如果还有关键变量没有在结论中明示出来的话, 我们还要把它找出来并纳入归纳假设; 而如果采用分治策略, 边界情况的改变就不会对证明产生那么大的变化了. 从这个意义上来说, 采用分治策略得到的解答也许会更加本质一些.

我们再来看一题, 它是第三十三届中国数学奥林匹克的第五题.

问题 2. 设 $n \geq 3$ 为一个奇数. 我们将 $n \times n$ 的方格棋盘中的每个方格染成黑色或白色. 称两个方格相邻, 如果它们同色且有公共的顶点. 称两个方格 $a, b$连通，如果存在一列方格 $c_{1}, \cdots, c_{k}$, 其中 $c_{1}=a, c_{k}=b$, 且对 $i=1,2, \cdots, k-1$, $c_{i}$ 与 $c_{i+1}$ 相邻. 求最大的正整数 $M$, 使得存在一种染色方式令棋盘中的 $M$ 个方格两两不连通.

为了简化记号, 我们将每个方格赋以坐标 $(x, y)$, 其中 $x, y \in\{1,2, \cdots, n\}$,称 $x$ 坐标为 $k$ 的所有方格的集合为 $C_{k}$, 称 $y$ 坐标为 $k$ 的所有方格的集合为 $R_{k}$.此外, 令简单图 $G=(V, E(G))$ 的顶点集 $V$ 为所有方格的集合, 两顶点相邻当且仅当它们对应的方格相邻. 由定义可知, 两顶点在图 $G$ 中属于同一个连通分支当且仅当它们对应的方格连通. 于是, 存在 $M$ 个两两不连通的方格当且仅当图 $G$ 至少有 $M$ 个连通分支.

经过一些试验, 可以猜测答案为 $\frac{(n+1)^{2}}{4}+1$, 这个数字当存在 $\frac{(n+1)^{2}}{4}$ 个两两不连通的白色方格时出现. 我们考虑使用归纳法解决问题 2. 对方格棋盘的边长归纳是一个好主意, 保持 $n$ 的奇偶性也是重要的, 但是如果没有强度合适的归纳假设让我们利用, 我们将无功而返. 所幸, 如下的辅助命题是有效的.

命题 1. 设奇数 $n \geq 3$, 则 $n \times n$ 的方格棋盘的任何二染色方式所对应的图
$G$ 至多有 $\frac{(n+1)^{2}}{4}+\delta_{0}(G)$ 个连通分支. 其中我们定义

$$
\delta_{0}(G)= \begin{cases}1, & \text { 若 }(1, n) \text { 与 }(2, n) \text { 异色且 }(n, 1) \text { 与 }(n, 2) \text { 异色; } \\ 0, & \text { 若 }(1, n) \text { 与 }(2, n) \text { 同色或 }(n, 1) \text { 与 }(n, 2) \text { 同色. }\end{cases}
$$

证明 为了进一步简化记号, 对于 $V$ 的子集 $V_{0}$, 我们定义 $V_{0}$ 的传递闭包为 $\overline{V_{0}}=\left\{v \in V\right.$ : 存在 $v_{0} \in V_{0}$ 使得 $v$ 与 $v_{0}$ 在图 $G$ 中属于同一个连通分支 $\}$.

注意到, 如果 $v \in V$ 与 $V_{0}$ 中两个异色方格均有公共顶点, 则 $v \in \overline{V_{0}}$; 同样地, 如果异色方格 $v_{1}, v_{2} \in V$ 与 $V_{0}$ 中的某个方格均有公共顶点, 则 $v_{1} \in \overline{V_{0}}$ 或者 $v_{2} \in \overline{V_{0}}$. 我们定义 $f\left(V_{0}\right)$ 为导出子图 $G\left[\overline{V_{0}}\right]$ 中连通分支的个数. 于是我们的工作即是要估计 $f(V)$.

当 $n=3$ 时, 方格 $(2,2)$ 与所有方格均有公共顶点, 故 $V \backslash \overline{\{(2,2)\}}$ 的所有顶点同色, 故 $f(V \backslash \overline{\{(2,2)\}})+1 \leq 5$, 当且仅当 $\overline{\{(2,2)\}}=C_{2} \cup R_{2}$ 方可取等. 于是,命题 1 对 $n=3$ 成立.

现在假设命题 1 对给定的奇数 $n \geq 3$ 成立, 我们要证明它对 $n+2$ 也成立.令 $V_{n}=V \backslash\left(C_{n+1} \cup C_{n+2} \cup R_{n+1} \cup R_{n+2}\right)$ 以及 $V_{n}^{+}=V \backslash\left(C_{n+2} \cup R_{n+2}\right)$. 由归纳假设, 我们有 $f\left(V_{n}\right) \leq \frac{(n+1)^{2}}{4}+\delta_{0}\left(G\left[V_{n}\right]\right)$.

考虑导出子图 $G\left[V \backslash \overline{V_{n}^{+}}\right]$的连通分支的数目与有公共边的同色方格对 $\left\{v_{1}, v_{2}\right\} \subseteq V_{n}^{+} \backslash V_{n}$ 的数目的关系. 注意到 $G\left[V \backslash \overline{V_{n}^{+}}\right]$的任何两个不属于同一个连通分支的方格没有公共顶点. 对 $G\left[V \backslash \overline{V_{n}^{+}}\right]$的一个连通分支 $S$, 若 $S=\{(1, n+2)\}$ 或者 $S=\{(n+2,1)\}$, 则恰有一对有公共边的方格对 $\left\{v_{1}, v_{2}\right\} \subseteq V_{n}^{+} \backslash V_{n}$, 使得 $S$ 中的某个方格与 $v_{1}, v_{2}$ 均有公共顶点，故而 $v_{1}$ 与 $v_{2}$ 同色; 若 $S \neq\{(1, n+2)\}$ 且 $S \neq\{(n+2,1)\}$ 且 $S \cap$ $\{(n+1, n+2),(n+2, n+2),(n+2, n+1)\}=\emptyset$, 则至少有两对有公共边的方格对 $\left\{v_{1}, v_{2}\right\} \subseteq V_{n}^{+} \backslash V_{n}$, 使得 $S$ 中的某个方格与 $v_{1}, v_{2}$ 均有公共顶点, 同样有 $v_{1}$ 与 $v_{2}$ 同色; 此外满足 $S \cap\{(n+1, n+2),(n+2, n+2),(n+2, n+1)\} \neq \emptyset$的连通分支 $S$ 至多只有一个. 由于没有重复计算的情况，我们可以把所有贡献加起来, 得到有公共边的同色方格对 $\left\{v_{1}, v_{2}\right\} \subseteq V_{n}^{+} \backslash V_{n}$ 的数目不少于 $2 f\left(V \backslash \overline{V_{n}^{+}}\right)-3-\delta_{0}(G)$, 故导出子图 $G\left[\overline{V_{n}^{+}} \backslash V\right]$ 的连通分支的数目不多于 $2 n-2 f\left(V \backslash \overline{V_{n}^{+}}\right)+4+\delta_{0}(G)$.

由于 $G\left[\overline{V_{n}^{+}} \backslash V\right]$ 的任意两个相邻的连通分支中至少有一个包含于 $\overline{V_{n}}$, 又由于当 $\delta_{0}\left(G\left[V_{n}\right]\right)=1$ 时 $(1, n+1)$ 与 $(n+1,1)$ 所在的连通分支均包含于 $\overline{V_{n}}$, 故
$G\left[V_{n}^{+} \backslash \overline{V_{n}}\right]$ 的连通分支数目不多于

$$
\begin{aligned}
& {\left[\frac{1}{2} \max \left\{2 n-2 f\left(V \backslash \overline{V^{+}}\right)+4+\delta_{0}(G)-2 \delta_{0}\left(G\left[V_{n}\right]\right), 0\right\}\right.} \\
= & \max \left\{n-f\left(V \backslash \overline{V_{n}^{+}}\right)+2+\delta_{0}(G)-\delta_{0}\left(G\left[V_{n}\right]\right), 0\right\} \\
= & n-f\left(V \backslash \overline{V_{n}^{+}}\right)+2+\delta_{0}(G)-\delta_{0}\left(G\left[V_{n}\right]\right),
\end{aligned}
$$

其中最后一步是因为 $f\left(V \backslash \overline{V_{n}^{+}}\right)-\delta_{0}(G) \leq n+1 \leq n+2-\delta_{0}\left(G\left[V_{n}\right]\right)$.

最后, 我们得到

$$
\begin{aligned}
f(V)= & f\left(V_{n}\right)+f\left(V_{n}^{+} \backslash \bar{V}_{n}\right)+f\left(V \backslash \overline{V_{n}^{+}}\right) \\
\leq & \left(\frac{(n+1)^{2}}{4}+\delta_{0}\left(G\left[V_{n}\right]\right)\right)+\left(n-f\left(V \backslash \overline{V_{n}^{+}}\right)+2+\delta_{0}(G)\right. \\
& \left.-\delta_{0}\left(G\left[V_{n}\right]\right)\right)+f\left(V \backslash \overline{V_{n}^{+}}\right) \\
= & \frac{(n+3)^{2}}{4}+\delta_{0}(G) .
\end{aligned}
$$

即, 命题 1 对 $n+2$ 成立.

接下来, 我们将给出利用分治策略得到的另一种解答.

定义集合 $B$ 为所有黑色的方格 $v$ 使得 $v$ 是图 $G$ 中 $v$ 所在的连通分支里 $x$坐标最大的方格中 $y$ 坐标最大的; 定义集合 $W$ 为所有白色的方格 $v$ 使得 $v$ 是图 $G$ 中 $v$ 所在的连通分支里 $x$ 坐标最小的方格中 $y$ 坐标最大的. 注意到, 图 $G$ 的连通分支的个数等于 $|B \cup W|$. 下面的命题 2 和命题 3 是 $B$ 和 $W$ 的两个局部性质, 这些足以给出我们想要的估计.

命题 2. 若 $(x, y) \in B \backslash\left(C_{n} \cup R_{n}\right)$, 则 $\left(C_{x} \cup C_{x+1} \cup C_{x+2}\right) \cap\left(R_{y} \cup R_{y-1} \cup\right.$ $\left.R_{y-2}\right) \cap W=\emptyset$. 类似地, 若 $(x, y) \in W \backslash\left(C_{1} \cup R_{n}\right)$, 则 $\left(C_{x} \cup C_{x-1} \cup C_{x-2}\right) \cap\left(R_{y} \cup\right.$ $\left.R_{y-1} \cup R_{y-2}\right) \cap B=\emptyset$.

证明 假设 $(x, y) \in B \backslash\left(C_{n} \cup R_{n}\right)$, 由定义, 我们知道 $(x+1, y),(x+1, y+1)$, $(x, y+1)$ 是白色的, 且若 $y>1$, 我们知道 $(x+1, y-1)$ 也是白色的. 由于 $\left(C_{x} \cup C_{x+1} \cup C_{x+2}\right) \cap\left(R_{y} \cup R_{y-1} \cup R_{y-2}\right)$ 中的任何白色方格都在图 $G$ 中 $(x, y+1)$所在的连通分支里, 故由定义它们都不属于 $W$. 于是, 命题的前一半得证.

由对称性, 我们可以得到对后一半的证明.

命题 3. 若 $(x, n) \in B$ 且 $(x+1, n) \in W$, 则 $\left(C_{x-1} \cup C_{x} \cup C_{x+1}\right) \cap B=\{(x, n)\}$且 $\left(C_{x} \cup C_{x+1} \cup C_{x+2}\right) \cap W=\{(x+1, n)\}$.

证明 假设 $(x, n) \in B$ 且 $(x+1, n) \in W$. 若 $C_{x}$ 不全是黑色方格或者 $C_{x+1}$
不全是白色方格, 取 $y$ 坐标最大的方格 $v$, 使得 $v \in C_{x}$ 且为白色方格, 或者 $v \in C_{x+1}$ 且为黑色方格, 则 $v$ 与 $(x, n)$ 或者 $(x+1, n)$ 在图 $G$ 中属于同一个连通分支. 由 $B$ 和 $W$ 的定义, 我们得到矛盾. 故 $C_{x}$ 全是黑色方格而且 $C_{x+1}$ 全是白色方格. 由于 $C_{x-1}$ 的每一个黑色方格都在图 $G$ 中 $(x, n)$ 所在的连通分支中, 且 $C_{x+2}$ 的每一个白色方格都在图 $G$ 中 $(x+1, n)$ 所在的连通分支中, 由 $B$ 和 $W$的定义, 命题得证.

对正整数 $k \leq \frac{n-3}{2}$, 若 $(2 k+1, n)$ 是白色的, 我们估计 $\mid\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap B\right) \cup$ $\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap W\right) \mid$. 由定义, 方格 $(2 k+2, n-1),(2 k+2, n),(2 k+1, n-1)$均不属于 $W$, 所以

$$
\begin{aligned}
& \left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap(B \backslash\{(2 k, n)\})\right) \cup\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap(W \backslash\{(2 k+1, n)\})\right) \\
= & \left(\left(\left(C_{2 k} \cup C_{2 k+1}\right) \backslash R_{n}\right) \cap B\right) \cup\left(\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \backslash\left(R_{n-1} \cup R_{n}\right)\right) \cap W\right) \\
= & \bigcup_{l=1}^{\frac{n-1}{2}}\left(\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap\left(R_{2 l-1} \cup R_{2 l}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap\left(R_{2 l-2} \cup R_{2 l-1}\right) \cap W\right)\right) .
\end{aligned}
$$

由命题 2 , 最后式子中的每一项至多有一个元素. 若 $(2 k, n) \notin B$ 或者 $(2 k+1, n) \notin$ $W$, 则 $\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap W\right)$ 至多有 $\frac{n+1}{2}$ 个元素. 反之, 若 $(2 k, n) \in B$ 且 $(2 k+1, n) \in W$, 由命题 3 , 可知 $\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup\right.\right.$ $\left.\left.C_{2 k+2}\right) \cap W\right)$ 恰有两个元素. 因此, 我们得出 $\mid\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup\right.\right.$ $\left.\left.C_{2 w+2}\right) \cap W\right) \left\lvert\, \leq \frac{n+1}{2}\right.$. 由对称性, 若 $(2 k+1, n)$ 是黑色的, 我们也可以得出相同的结论.

接下来, 我们估计 $\left|\left(C_{1} \cap B\right) \cup\left(\left(C_{1} \cup C_{2}\right) \cap W\right)\right|$. 我们有

$$
\begin{aligned}
& \left(\left(C_{1} \cap(B \backslash\{1, n\})\right) \cup\left(\left(C_{1} \cup C_{2}\right) \cap W\right)\right) \backslash\left(\left(C_{1} \cup C_{2}\right) \cap\left(R_{n-1} \cup R_{n}\right) \cap W\right) \\
= & \left(\left(C_{1} \backslash R_{n}\right) \cap B\right) \cup\left(\left(\left(C_{1} \cup C_{2}\right) \backslash\left(R_{n-1} \cup R_{n}\right)\right) \cap W\right) \\
= & \bigcup_{l=1}^{\frac{n-1}{2}}\left(\left(C_{1} \cap\left(R_{2 l-1} \cup R_{2 l}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap\left(R_{2 l-2} \cup R_{2 l-1}\right) \cap W\right)\right) .
\end{aligned}
$$

由命题 2 , 最后式子中的每一项至多有一个元素. 由于 $\left(C_{1} \cup C_{2}\right) \cap\left(R_{n-1} \cup R_{n}\right) \cap W$至多有一个元素, 我们知道 $\left|\left(C_{1} \cap B\right) \cup\left(\left(C_{1} \cup C_{2}\right) \cap W\right)\right| \leq|\{(1, n)\} \cap B|+\frac{n+1}{2}$.由对称性, 我们有 $\left|\left(\left(C_{n-1} \cup C_{n}\right) \cap B\right) \cup\left(C_{n} \cap W\right)\right| \leq|\{(n, n)\} \cap W|+\frac{n+1}{2}$.

所以, 我们知道

$$
|B \cup W|=\left|\bigcup_{k=0}^{\frac{n-1}{2}}\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap W\right)\right|
$$

$$
\begin{aligned}
& =\sum_{k=0}^{\frac{n-1}{2}}\left|\left(\left(C_{2 k} \cup C_{2 k+1}\right) \cap B\right) \cup\left(\left(C_{2 k+1} \cup C_{2 k+2}\right) \cap W\right)\right| \\
& \leq \frac{(n+1)^{2}}{4}+|\{(1, n)\} \cap B|+|\{(n, n)\} \cap W| .
\end{aligned}
$$

因此, 对任意染色方式, 若 $(n, n)$ 是黑色的, 则对应的图 $G$ 至多有 $\frac{(n+1)^{2}}{4}+1$个连通部分. 由对称性, 若 $(n, n)$ 是白色的, 我们也可以得出相同的结论.


[^0]:    收稿日期: 2017-11-23； 修订日期: 2017-12-03.

