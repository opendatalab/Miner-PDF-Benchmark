# 数学新星问题征解第三期解答 

2014.6

第一题: 设 $v_{1}, v_{2}, \cdots, v_{n}$ 是 $\mathbf{R}^{m}$ 中的 $n$ 个单位向量. 证明: 存在 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n} \in\{-1,1\}$ 使得

$$
\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right| \geq \sqrt{n}
$$

注: 对于任意的 $x=\left(x_{1}, x_{2}, \cdots, x_{m}\right) \in \mathbf{R}^{m}$, 定义 $|x|=\sqrt{x_{1}^{2}+x_{2}^{2}+\cdots+x_{m}^{2}}$.

(㫿振华供题)

## 证明一 (根据陆一平同学和朱书聪同学的解答整理):

对 $n$ 进行数学归纳.

当 $n=1$ 时结论显然成立.

假设当 $n=k(k \in \mathbf{N}, k>1)$ 时结论也成立, 即存在 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{k} \in$ $\{-1,1\}$ 使得

$$
\left|\sum_{i=1}^{k} \varepsilon_{i} v_{i}\right| \geq \sqrt{k}
$$

下面考虑 $n=k+1$ 的情况.

由于

$\left|\sum_{i=1}^{k} \varepsilon_{i} v_{i}+v_{k+1}\right|^{2}+\left|\sum_{i=1}^{k} \varepsilon_{i} v_{i}-v_{k+1}\right|^{2}=2\left|\sum_{i=1}^{k} \varepsilon_{i} v_{i}\right|^{2}+2\left|v_{k+1}\right|^{2} \geq 2(\sqrt{k})^{2}+2=2(k+1)$.

故由抽屟原理知存在 $\varepsilon_{k+1} \in\{-1,1\}$ 使得

$$
\left|\sum_{i=1}^{k} \varepsilon_{i} v_{i}+\varepsilon_{k+1} v_{k+1}\right|^{2} \geq \frac{2(k+1)}{2}=k+1 .
$$

即结论对于 $n=k+1$ 时也成立.

综上, 由归纳假设原理便知结论成立.

## 证明二 (根据饶正昊同学的解答整理):

设 $v_{i}=\left(a_{1 i}, a_{2 i}, \cdots, a_{m i}\right), i=1,2, \cdots, n$, 则由 $\left|v_{i}\right|=1$ 知

$$
\sum_{j=1}^{m} a_{j i}^{2}=1, i=1,2, \cdots, n
$$

记 $S=\{-1,1\}$, 则对任意的 $\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}\right) \in S^{n}$ 有

$$
\begin{aligned}
\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right|^{2} & =\sum_{j=1}^{m}\left(\sum_{i=1}^{n} \varepsilon_{i} a_{j i}\right)^{2} \\
& =\sum_{j=1}^{m}\left(\sum_{i=1}^{n} a_{j i}^{2}+2 \sum_{1 \leq i<k \leq n} \varepsilon_{i} \varepsilon_{k} a_{j i} a_{j k}\right) \\
& =\sum_{i=1}^{n} \sum_{j=1}^{m} a_{j i}^{2}+2 \sum_{j=1}^{m} \sum_{1 \leq i<k \leq n} \varepsilon_{i} \varepsilon_{k} a_{j i} a_{j k} \\
& =n+2 \sum_{j=1}^{m} \sum_{1 \leq i<k \leq n} \varepsilon_{i} \varepsilon_{k} a_{j i} a_{j k} .
\end{aligned}
$$

故

$$
\begin{aligned}
\sum_{\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}\right) \in S^{n}}\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right|^{2} & =2^{n} \cdot n+2 \sum_{\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}\right) \in S^{n}} \sum_{j=1}^{m} \sum_{1 \leq i<k \leq n} \varepsilon_{i} \varepsilon_{k} a_{j i} a_{j k} \\
& =2^{n} \cdot n+2 \sum_{j=1}^{m} \sum_{1 \leq i<k \leq n} a_{j i} a_{j k} \cdot\left(\sum_{\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}\right) \in S^{n}} \varepsilon_{i} \varepsilon_{k}\right) \\
& =2^{n} \cdot n+2 \sum_{j=1}^{m} \sum_{1 \leq i<k \leq n} a_{j i} a_{j k} \cdot\left(2^{n-2} \sum_{\left(\varepsilon_{i}, \varepsilon_{k}\right) \in S^{2}} \varepsilon_{i} \varepsilon_{k}\right) .
\end{aligned}
$$

又因为

$$
\sum_{\left(\varepsilon_{i}, \varepsilon_{k}\right) \in S^{2}} \varepsilon_{i} \varepsilon_{k}=1 \times 1+1 \times(-1)+(-1) \times 1+(-1) \times(-1)=0
$$

所以

$$
\sum_{\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}\right) \in S^{n}}\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right|^{2}=2^{n} \cdot n
$$

故由抽屟原理便知存在 $\left(\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}\right) \in S^{n}$ 使得

$$
\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right|^{2} \geq \frac{2^{n} \cdot n}{2^{n}}=n
$$

即

$$
\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right| \geq \sqrt{n}
$$

评注: 本问题是数学新星问题征解第一期的第三题 (Barany 等人的

问题) 的反问题. 由本题的证明二可看出, 实际上我们证明了 $\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right|^{2}$ 的数学期望为 $n$.

第二题: 设 $k$ 是一个给定的正整数, $X=\left\{x \in \mathbf{N}^{*} \mid x \leq 6 k, x \equiv 1,2,3\right.$ $(\bmod 6)\}$. 求满足下列条件的正整数对 $(p, q)$ 的个数:

(1) $p<q$ 且 $(p, q)=1$;

(2) 存在 $X$ 的一个分划 $X=A \cup B \quad(A \cap B=\emptyset)$ 使得

$$
p \cdot\left(\sum_{a \in A} a\right)=q \cdot\left(\sum_{b \in B} b\right)
$$

(冯跃峰供题)

## 证明 (根据饶正昊同学的解答整理):

设 $X_{k}=\left\{x \in \mathbf{N}^{*} \mid x \leq 6 k, x \equiv 1,2,3(\bmod 6)\right\}$, 则 $\sum_{x \in X_{k}} x=9 k^{2}-3 k$.

下面证明: 对任意的 $1 \leq t \leq 9 k^{2}-3 k, t \in \mathbf{N}^{*}$, 均存在 $T \subseteq X_{k}$, 使得 $\sum_{x \in T} x=t$.

对 $k$ 用数学归纳.

当 $k=1,2,3$ 时容易验证结论成立.

假设结论对 $k \geq 3$ 成立, 下面考虑 $k+1$ 的情况, 则

$$
\sum_{x \in X_{k+1}} x=9(k+1)^{2}-3(k+1)=9 k^{2}+15 k+6
$$

若 $1 \leq t \leq 9 k^{2}-3 k$, 则由 $X_{k} \subseteq X_{k+1}$ 及归纳假设便知结论成立.

若 $9 k^{2}-3 k+1 \leq t \leq 9 k^{2}+15 k+6$, 令 $t^{\prime}=t-(18 k+6)$, 则 $9 k^{2}-21 k-5 \leq$ $t^{\prime} \leq 9 k^{2}-3 k$. 又由 $k \geq 3$ 知 $9 k^{2}-21 k-5 \geq 1$, 故 $1 \leq t^{\prime} \leq 9 k^{2}-3 k$. 因此, 由归纳假设知存在 $T^{\prime} \subseteq X_{k}$ 使得 $\sum_{x \in T^{\prime}} x=t^{\prime}$. 令 $T=T^{\prime} \cup\{6 k+1,6 k+2,6 k+3\}$,即有 $\sum_{x \in T} x=t^{\prime}+(18 k+6)=t$. 即结论对 $k+1$ 时也成立.

故 $(*)$ 得证.

回到原题. 注意到每个满足条件的正整数对 $(p, q)$ 与正整数对 $\left(\sum_{a \in A} a, \sum_{b \in B} b\right)$之间存在着一一对应的关系, 故要求满足条件的正整数对 $(p, q)$ 的个数,
就变为求正整数对 $\left(\sum_{a \in A} a, \sum_{b \in B} b\right)$ 的个数, 又因为

$$
\sum_{a \in A} a+\sum_{b \in B} b=\sum_{x \in X} x
$$

则求正整数对 $\left(\sum_{a \in A} a, \sum_{b \in B} b\right)$ 的个数就转化为求 $\sum_{b \in B} b$ 的取值个数.

由 $p<q$, (1) 及

$$
\frac{\sum_{b \in B} b}{\sum_{a \in A} a}=\frac{p}{q}<1
$$

便知

$$
\sum_{b \in B} b<\frac{\sum_{x \in X} x}{2}=\frac{9 k^{2}-3 k}{2}
$$

即

$$
\sum_{b \in B} b \leq \frac{9 k^{2}-3 k}{2}-1
$$

再由 $(*)$ 知, $\sum_{b \in B} b$ 可取到 $\left\{1,2, \cdots, \frac{9 k^{2}-3 k}{2}-1\right\}$ 中的所有值, 故 $\sum_{b \in B} b$ 有 $\frac{9 k^{2}-3 k}{2}-$ 1 个可能值, 则满足条件的正整数数对 $(p, q)$ 也有 $\frac{9 k^{2}-3 k}{2}-1$ 个.

第三题: 给定正整数 $m, n, r$, 其中 $1<m<n$. 在 $m \times n$ 方格表中选出若干个方格, 使得每行每列选出的方格数不超过 $r$, 试求 $a$ 的最小值, 使得总可以用 $a$ 种颜色对选出的方格进行染色, 使得每行每列都不存在 3 个同色的方格.

(上海中学学生陆一平供题)

## 解 (冯跃峰老师的解答):

用 $\lceil x\rceil$ 表示不小于 $x$ 的最小整数, 则显然有 $a \geq\left\lceil\frac{r}{2}\right\rceil$.

实际上, 由于一行可能选取了 $r$ 个格, 而该行每种颜色的格至多有 2 个, 所以由抽屉原理, 颜色种数 $a \geq\left\lceil\frac{r}{2}\right\rceil$.

下面只需证明: 总可以用 $a=\left\lceil\frac{r}{2}\right\rceil$ 种颜色对选出的方格进行染色, 使得每行每列都不存在 3 个同色的方格.

为此, 用 $m$ 个点表示方格表的 $m$ 行, 另 $n$ 个点表示其 $n$ 列, 两个顶点相邻当且仅当该两顶点对应的行与列相交处的方格被选取, 得到一个二部图 $G_{m, n}$.
因为每一行 (列) 选取的方格数就是该行 (列) 对应点连的边数, 所以题目的条件变成二部图 $G_{m, n}$ 中所有点的度都不大于 $r$. 下面要用 $a=\left\lceil\frac{r}{2}\right\rceil$种颜色对 $G_{m, n}$ 的边进行染色, 使得同一个顶点引出的边中不存在 3 条同色的边.

记二部图 $G_{m, n}$ 的两部分的顶点集分别为 $A=\left\{A_{1}, A_{2}, \cdots, A_{m}\right\}, B=$ $\left\{B_{1}, B_{2}, \cdots, B_{n}\right\}$, 在 $A$ 中增补 $n-m$ 个点: $A_{m+1}, A_{m+2}, \cdots, A_{n}$, 得到新的二部图 $G^{\prime}=G_{n, n}$.

由于增加了 $n-m$ 个孤立点, 图中每个顶点的度不增加, 从而 $G^{\prime}$ 每个顶点的度仍不大于 $r$.

如果 $G^{\prime}$ 中存在某个顶点的度小于 $r$, 不妨设 $d\left(A_{i}\right)<r$, 又每个顶点的度不大于 $r$, 那么

$$
\sum_{i=1}^{n} d\left(B_{i}\right)=\left\|G^{\prime}\right\|=\sum_{i=1}^{n} d\left(A_{i}\right)<n r
$$

所以, $G^{\prime}$ 中必定存在某个 $B_{j}(1 \leq j \leq n)$, 使 $d\left(B_{j}\right)<r$.

在 $G^{\prime}$ 中增添边 $A_{i} B_{j}$ (可为重边), 使顶点 $A_{i}, B_{j}$ 的度都增加 1 , 其他顶点的度不变, 从而增加新的边后, 图中每个顶点的度仍不大于 $r$. 如此继续下去, 直至每个顶点的度都不小于 $r$, 记此时的图为 $G^{\prime \prime}$.

显然, $G^{\prime \prime}$ 的每个顶点的度都为 $r$, 即 $G^{\prime \prime}$ 是一个 $r$ - 正则二部图 (允许有重边), 由 Hall 定理 (可把重边看作一条边), 正则二部图存在完美匹配,取出其中一个完美匹配 $P_{1}$, 在图中去掉 $P_{1}$ 的边, 则每个点都去掉一条边,得到的图仍是正则二部图, 又存在完美匹配 $P_{2}$, 又在图中去掉 $P_{2}$ 的边,则每个点又都去掉一条边, 得到的图仍是正则二部图. 如此下去, 直至取出第 $r$ 个完美匹配 $P_{r}$.

显然, 每个顶点引出的 $r$ 条边分别属于 $r$ 个不同的完美匹配. 现在, 将完美匹配 $P_{i}\left(1 \leq i \leq\left\lceil\frac{r}{2}\right\rceil\right)$ 的边都染第 $i$ 种颜色, 完美匹配 $P_{j}\left(\left\lceil\frac{r}{2}\right\rceil+1 \leq j \leq r\right)$的边都染第 $\left(j-\left\lceil\frac{r}{2}\right\rceil\right)$ 种颜色, 则同一个顶点处没有 3 条边同色.

现在, 在 $G^{\prime \prime}$ 中去掉新增加的边得到图 $G^{\prime}$, 则 $G^{\prime}$ 在同一个顶点处没有 3 条边同色. 最后在 $G^{\prime}$ 中去掉新增加的 $n-m$ 个点得到图 $G$, 则 $G$ 在同一个顶点处没有 3 条边同色, 染色合乎要求.

综上所述, $a_{\min }=\left\lceil\frac{r}{2}\right\rceil$.
第四题: 设正整数 $n>1, z_{1}, z_{2}, \cdots, z_{n}$ 是复数, 证明:

$$
\sum_{k=1}^{n}\left|1+z_{k}\right|+\frac{1}{n-1} \sum_{1 \leq i<j \leq n}\left|1+z_{i} z_{j}\right| \geq \sum_{k=1}^{n}\left|z_{k}\right|
$$

## 证明一 (根据周蕴坤同学的解答整理):

首先证明引理: 对任意的 $1 \leq i<j \leq n$ 有

$$
\left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right| \geq\left|z_{i}\right|+\left|z_{j}\right| .
$$

记 $\left|z_{i}\right|=r_{i},\left|z_{j}\right|=r_{j}$, 则由 $(*)$ 式关于 $z_{i}, z_{j}$ 的对称性, 不妨设 $r_{i} \geq r_{j} \geq 0$.下面分三种情况进行讨论.

(1) 当 $r_{i} \geq r_{j} \geq 1$ 时.

$$
\begin{aligned}
& \left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right| \\
& \geq\left|1+z_{i}\right|+\left|\left(1+z_{j}\right)-\left(1+z_{i} z_{j}\right)\right| \\
& =\left|1+z_{i}\right|+\left|z_{j}\right|\left|1-z_{i}\right| \\
& =\left(\left|z_{j}\right|-1\right)\left|1-z_{i}\right|+\left(\left|1+z_{i}\right|+\left|1-z_{i}\right|\right) \\
& \geq\left(\left|z_{j}\right|-1\right)\left(\left|z_{i}\right|-1\right)+\left|\left(1+z_{i}\right)+\left(z_{i}-1\right)\right| \\
& =\left(r_{j}-1\right)\left(r_{i}-1\right)+2 r_{i} \\
& =\left(r_{i}+r_{j}\right)+\left(r_{i}-r_{j}\right) r_{j}+\left(1-r_{j}\right)^{2} \\
& \geq r_{i}+r_{j}=\left|z_{i}\right|+\left|z_{j}\right| .
\end{aligned}
$$

(2) 当 $r_{i} \geq 1>r_{j} \geq 0$ 时.

若 $r_{i} r_{j} \geq 1$.

$$
\begin{aligned}
& \left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right| \\
& \geq\left|1+z_{i}\right|+\left|\left(1+z_{j}\right)-\left(1+z_{i} z_{j}\right)\right| \\
& =\left(1-\left|z_{j}\right|\right) \cdot\left|1+z_{i}\right|+\left|z_{j}\right| \cdot\left(\left|1-z_{i}\right|+\left|1+z_{i}\right|\right) \\
& \geq\left(1-\left|z_{j}\right|\right) \cdot\left(\left|z_{i}\right|-1\right)+\left|z_{j}\right| \cdot\left|\left(z_{i}-1\right)+\left(1+z_{i}\right)\right| \\
& =r_{i}+r_{j}-1-r_{i} r_{j}+2 r_{i} r_{j} \\
& \geq r_{i}+r_{j}=\left|z_{i}\right|+\left|z_{j}\right| .
\end{aligned}
$$

若 $0 \leq r_{i} r_{j}<1$.

$$
\begin{aligned}
& \left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right| \\
& \geq\left|1+z_{j}\right|+\left|\left(1+z_{i}\right)-\left(1+z_{i} z_{j}\right)\right| \\
& =\left(\left|z_{i}\right|-1\right) \cdot\left|1-z_{j}\right|+\left(\left|1-z_{j}\right|+\left|1+z_{j}\right|\right) \\
& \geq\left(\left|z_{i}\right|-1\right) \cdot\left(1-\left|z_{j}\right|\right)+\left|\left(1-z_{j}\right)+\left(1+z_{j}\right)\right| \\
& =\left(r_{i}-1\right) \cdot\left(1-r_{j}\right)+2 \\
& \geq r_{i}+r_{j}=\left|z_{i}\right|+\left|z_{j}\right| .
\end{aligned}
$$

(3) 当 $1>r_{i} \geq r_{j} \geq 0$ 时.

$$
\begin{aligned}
& \left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right| \\
& \geq\left|1+z_{j}\right|+\left|\left(1+z_{i}\right)-\left(1+z_{i} z_{j}\right)\right| \\
& =\left(1-\left|z_{i}\right|\right) \cdot\left|1+z_{j}\right|+\left|z_{i}\right| \cdot\left(\left|1-z_{j}\right|+\left|1+z_{j}\right|\right) \\
& \geq\left(1-\left|z_{i}\right|\right) \cdot\left(1-\left|z_{j}\right|\right)+\left|z_{i}\right| \cdot\left|\left(1-z_{j}\right)+\left(1+z_{j}\right)\right| \\
& =\left(1-r_{i}\right)\left(1-r_{j}\right)+2 r_{i} \\
& =\left(r_{i}+r_{j}\right)+\left(r_{i}-r_{j}\right) r_{j}+\left(r_{j}-1\right)^{2} \\
& \geq r_{i}+r_{j}=\left|z_{i}\right|+\left|z_{j}\right| .
\end{aligned}
$$

由 (1), (2) 和 (3) 便知 $(*)$ 式得证.

对 $(*)$ 式两边求和可得

$$
\sum_{1 \leq i<j \leq n}\left(\left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right|\right) \geq \sum_{1 \leq i<j \leq n}\left(\left|z_{i}\right|+\left|z_{j}\right|\right)
$$

故

$$
(n-1) \sum_{i=1}^{n}\left|1+z_{i}\right|+\sum_{1 \leq i<j \leq n}\left|1+z_{i} z_{j}\right| \geq(n-1) \sum_{i=1}^{n}\left|z_{i}\right|,
$$

即

$$
\sum_{i=1}^{n}\left|1+z_{i}\right|+\frac{1}{n-1} \sum_{1 \leq i<j \leq n}\left|1+z_{i} z_{j}\right| \geq \sum_{i=1}^{n}\left|z_{i}\right|
$$

## 证明二 (根据俞辰捷同学的解答整理):

引理: 对任意的 $1 \leq i<j \leq n$ 有

$$
\left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right| \geq\left|z_{i}\right|+\left|z_{j}\right| .
$$

事实上,

$$
\begin{aligned}
& \left(\left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right|\right)^{2} \\
& =\left(\left|1+z_{i}\right|+\left|1+\overline{z_{j}}\right|+\left|1+z_{i} z_{j}\right|\right)^{2} \\
& \geq\left(\left|z_{i}-\overline{z_{j}}\right|+\left|1+z_{i} z_{j}\right|\right)^{2} \\
& \geq\left|z_{i}-\overline{z_{j}}\right|^{2}+\left|1+z_{i} z_{j}\right|^{2} \\
& =\left|z_{i}\right|^{2}+\left|z_{j}\right|^{2}-2 \operatorname{Re} z_{i} z_{j}+1+\left(\left|z_{i}\right|\left|z_{j}\right|\right)^{2}+2 \operatorname{Re} \overline{z_{i} z_{j}} \\
& \geq\left|z_{i}\right|^{2}+\left|z_{j}\right|^{2}+2\left|z_{i}\right|\left|z_{j}\right| \\
& =\left(\left|z_{i}\right|+\left|z_{j}\right|\right)^{2} .
\end{aligned}
$$

故引理得证.

对引理的两边求和可得

$$
\sum_{1 \leq i<j \leq n}\left(\left|1+z_{i}\right|+\left|1+z_{j}\right|+\left|1+z_{i} z_{j}\right|\right) \geq \sum_{1 \leq i<j \leq n}\left(\left|z_{i}\right|+\left|z_{j}\right|\right)
$$

故

$$
(n-1) \sum_{i=1}^{n}\left|1+z_{i}\right|+\sum_{1 \leq i<j \leq n}\left|1+z_{i} z_{j}\right| \geq(n-1) \sum_{i=1}^{n}\left|z_{i}\right|
$$

即

$$
\sum_{i=1}^{n}\left|1+z_{i}\right|+\frac{1}{n-1} \sum_{1 \leq i<j \leq n}\left|1+z_{i} z_{j}\right| \geq \sum_{i=1}^{n}\left|z_{i}\right| .
$$

评注：第四题是罗马尼亚的 C. Tigaeru 的论文 “An inequality in the complex domain” (刊于 J. Math. Ineq. 6(2012)) 一文的主要结果, 该文的证明篇幅很长. 2014 年 6 月在国家队集训时, 张思汇拿出此问题来讨论 (事实上在此之前, 冷岗松教授就将此问题交给几位同学来研究). 开始寻找证明的过程并不十分顺利. 后来, 似乎是国家队队员的周蕴坤同学最先找到了一个分类讨论的证法 (即上面的证明一). 再后来, 俞辰捷同学发现了一个十分简捷的证法 (即上面的证明二). 值得注意, 我们认为周蕴坤同学的证明尽管篇幅较长, 但仍然是很有意义, 它指出了什么条件下这个不等式有更强的形式.

