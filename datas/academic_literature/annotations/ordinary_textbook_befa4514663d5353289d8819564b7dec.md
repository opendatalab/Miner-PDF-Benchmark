# 数学新星问题征解第一期解答 

2014.4

第一题: 设 $a, b, n$ 是正整数, $a, b \leq n$. 证明:

$$
\frac{1}{n} \sum_{k=0}^{n-1} C_{k}^{a} C_{k}^{b} \leq \frac{1}{a+b+1} C_{n}^{a} C_{n}^{b}
$$

注: 当 $m<k$ 时, 规定 $C_{m}^{k}=0$.

证明: 注意到 $n \geq k \geq a$ 时, 有

$$
\begin{aligned}
\frac{C_{k}^{a}}{C_{n}^{a}} & =\frac{k !}{(k-a) !} \cdot \frac{(n-a) !}{n !} \\
& =\frac{k(k-1) \cdots(k-a+1)}{n(n-1) \cdots(n-a+1)} \leq\left(\frac{k}{n}\right)^{a}
\end{aligned}
$$

即 $C_{k}^{a} \leq \frac{1}{n^{a}} C_{n}^{a} k^{a}$.

同理可得当 $n \geq k \geq b$ 时有

$$
C_{k}^{b} \leq \frac{1}{n^{b}} C_{n}^{b} \cdot k^{b}
$$

由 (1) 和 (2) 可得

$$
\frac{1}{n} \sum_{k=0}^{n-1} C_{k}^{a} C_{k}^{b} \leq \frac{1}{n^{a+b+1}} C_{n}^{a} C_{n}^{b} \cdot \sum_{k=0}^{n-1} k^{a+b}
$$

又注意到

$$
\begin{aligned}
n^{a+b+1} & =\sum_{k=0}^{n-1}\left((k+1)^{a+b+1}-k^{a+b+1}\right) \\
& \geq \sum_{k=0}^{n-1}(a+b+1) k^{a+b}
\end{aligned}
$$

即 $\sum_{k=0}^{n-1} k^{a+b} \leq \frac{n^{a+b+1}}{a+b+1}$.

由 (3) 和 (4) 便得所证不等式.

评注: 此问题是一个简单的 Grüss 型不等式. 用上面方法还可证明如下的 Grüss 不等式:

$$
\frac{1}{n} \sum_{k=0}^{n-1} C_{k}^{i} C_{k}^{j} C_{k}^{m}-\frac{1}{n^{3}} C_{n+1}^{i+1} C_{n+1}^{j+1} C_{n+1}^{m+1} \leq \frac{1}{8} C_{n}^{i} C_{n}^{j} C_{n}^{m}
$$

其中 $n \geq 1,1 \leq i, j, m \leq n, i, j, m \in N^{*}$.

用上面的方法还可证明如下的 Grüss-Landau 不等式: 设 $a_{k} \geq 0, k=$ $0,1, \cdots, n, A_{n}=\sum_{k=0}^{n} C_{n}^{k} a_{k}$, 则

$$
\frac{1}{n} \sum_{k=0}^{n-1} A_{k}^{2}-\frac{1}{n^{2}}\left(\sum_{k=0}^{n} A_{k}\right)^{2} \leq \frac{4}{45}\left(A_{n}-A_{0}\right)^{2}
$$

这被选作 2013 年国家集训队测试题, 公认是当年难度很高的一道试题.

第一题也可用归纳法证明，篇幅甚至更短.

第二题: 设 $G$ 是一个简单图, $\bar{G}$ 是 $G$ 的补图. 已知 $G$ 和 $\bar{G}$ 都是联通的, 求 $G$ 和 $\bar{G}$ 的直径之和的最大值.

注: 图 $G$ 的直径是 $G$ 中任何两点距离的最大者.

## 解 1 (根据郑州外国语学校朱书聪同学的解答整理而成):

用 $G^{\prime}$ 表示 $G$ 的补图. 设 $|G|=n$, 则 $n \geq 4$, 否则, $G, G^{\prime}$ 中必有一个不连通, 矛盾. 设 $G$ 和 $G^{\prime}$ 的直径分别为 $n$ 和 $r$, 先证明 $k+r \leq \max \{6, n+1\}$.

(1) 若 $n, r$ 中有一个不小于 4 , 不妨设 $k \geq 4$, 并设 $A, B$ 是 $G$ 的直径的两个端点. 对 $G$ 中的任意顶点 $G$, 定义 $f(G)$ 为 $A, G$ 之间在 $G$ 中的距离,特别地, $f(A)=0$.

易知, 对 $G$ 中的任意两个顶点 $P, Q$, 若 $P, Q$ 在 $G$ 中相连, 则 $\mid f(P)-$ $f(Q) \mid \leq 1$. 事实上, 不妨设 $f(P) \leq f(Q)$, 则由于 $P$ 与 $A$ 在 $G$ 中的距离为 $f(P)$, 而 $P, Q$ 在 $G$ 中相连, 故 $f(Q) \leq f(P)+1$, 于是 $|f(P)-f(Q)| \leq 1$.

由此可见, 对 $G$ 中的任意两个顶点 $P, Q$, 若 $|f(P)-f(Q)| \geq 2$, 则 $P, Q$在 $G$ 中不相连, 从而在 $G^{\prime}$ 中相连.

下面证明: $r \leq 2$.

事实上, 我们证明, 对于 $G^{\prime}$ 中的任意两个顶点 $P, Q, P, Q$ 在 $G^{\prime}$ 中距离不大于 2 .

(i) 若 $|f(P)-f(Q)| \geq 2$, 则 $P, Q$ 在 $G$ 中不相连, 从而 $P, Q$ 在 $G^{\prime}$ 中距离为 1 , 结论成立.

(ii) 若 $|f(P)-f(Q)|=0$, 则 $f(P)=f(Q)$. 显然 $f(P)=f(Q) \neq 0$, 否则 $P=Q=A$, 矛盾. 若 $f(P)=f(Q)=1$, 则在 $G$ 中 $P, A$ 相连, $Q, A$ 相连,而 $f(B) \geq 4$, 于是在 $G$ 中 $P, B$ 不连, $Q, B$ 不连, 所以在 $G^{\prime}$ 中有一条路:
$P \rightarrow B \rightarrow Q$, 结论成立; 若 $f(P)=f(Q) \geq 2$, 则在 $G$ 中 $P, A$ 不相连, $Q, A$不相连, 从而在 $G^{\prime}$ 中有一条路: $P \rightarrow A \rightarrow Q$, 结论成立.

(iii) 若 $|f(P)-f(Q)|=1$, 不妨设 $f(P)-f(Q)=1$, 若 $f(P)=1$, 则 $f(Q)=0$, 从而 $P, A$ 相连, $Q=A$, 但 $f(B) \geq 4$, 所以在 $G$ 中 $P, B$ 不连, $Q, B$不连, 所以在 $G^{\prime}$ 中有一条路: $P \rightarrow B \rightarrow Q$, 结论成立; 若 $f(P)=f(Q) \geq 2$,则在 $G$ 中 $P, A$ 不相连, $Q, A$ 不相连, 从而在 $G^{\prime}$ 中有一条路: $P \rightarrow A \rightarrow Q$,结论成立.

综上便证明了 $r \leq 2$.

因为 $G$ 中连接 $A, B$ 的路有 $k+1$ 个顶点 (含 $A, B$ ), 且这些顶点互异,否则不是最短路, 于是 $k+1 \leq n$, 所以 $k+r \leq k+2 \leq n+1$.

(2) 若 $k, r$ 都不大于 3 , 则 $k+r \leq 6$.

由 (1) 和 (2) 可得 $k+r \leq \max \{6, n+1\}$.

另一方面, 当 $G$ 是长为 $n-1$ 的链时, $k+r=\max \{6, n+1\}$.

事实上, 若 $n=4$, 则 $G$ 与 $G^{\prime}$ 都是长为 3 的链, $k+r=3+3=$ $\max \{6, n+1\}$.

若 $n \geq 5$, 则 $k=n-1$, 对任意两点 $P, Q$, 如果 $P, Q$ 在 $G$ 中不相连,则 $P, Q$ 在 $G^{\prime}$ 中的距离为 1. 如果 $P, Q$ 在 $G$ 中相连, 则 $P, Q$ 在 $G^{\prime}$ 中的距离不小于 2. 因为 $P, Q$ 在 $G^{\prime}$ 中的度都是 $n-3$, 其度的和为 $2 n-6$, 于是, 由抽屉原理, 其余 $n-2$ 个点中, 至少有一个点向 $P, Q$ 之间连边数 $\geq \frac{2 n-6}{n-2}=\frac{(n-1)+(n-5)}{n-2} \geq \frac{n-1}{n-2}>1$, 所以至少有一个点与 $P, Q$ 都有边相连, 所以 $P, Q$ 在 $G^{\prime}$ 中的距离为 2 . 所以, $k+r=(n-1)+2=n+1=\max \{6, n+1\}$.

综上所述, 所求 $k+r$ 的最小值为 $\max \{6, n+1\}$.

## 解 2 (冯跃峰老师提供):

用 $G^{\prime}$ 表示 $\mathrm{G}$ 的补图, 设 $|G|=n$, 则 $n \geq 4$. 否则, $G, G^{\prime}$ 中必有一个不连通, 矛盾.

用 $d(G), d\left(G^{\prime}\right)$ 分别表示 $G$ 和 $G^{\prime}$ 的直径, 用 $d(A, B), d^{\prime}(A, B)$ 分别表示两点 $A, B$ 在 $G$ 和 $G^{\prime}$ 中的距离, 我们将 $G$ 和 $G^{\prime}$ 作在一个图中, 其中 $G$ 的边用实边表示, $G^{\prime}$ 的边用虚边表示.

先证明下面的结论: 若 $d(G) \geq 3$, 则 $d\left(G^{\prime}\right) \leq 3$.

实际上, 设 $A, B$ 是 $G$ 的直径的两个端点, 则 $d(A, B) \geq 3$, 于是 $A B$ 为虚边, 且对 $A, B$ 外的任意一点 $P, P A, P B$ 不能都是实边, 否则 $d(A, B)=2$,矛盾. 所以 $P A, P B$ 中至少有一条是虚边.
考虑任意两个点 $M, N$, 如果 $\{M, N\}=\{A, B\}$, 则 $d^{\prime}(M, N)=1$. 如果 $M \in\{A, B\}, N \notin\{A, B\}$, 则因 $N A, N B$ 中至少有一条是虚边, 且 $A B$ 是虚边, 所以 $d^{\prime}(M, N) \leq 2$. 如果 $N \in\{A, B\}, M \notin\{A, B\}$, 则同理有 $d^{\prime}(M, N) \leq$ 2. 如果 $M \notin\{A, B\}, N \notin\{A, B\}$, 则因 $M A, M B$ 中至少有一条是虚边, $N A, N B$ 中至少有一条是虚边, 且 $A B$ 是虚边, 所以 $d^{\prime}(M, N) \leq 3$. 于是, 不论哪种情况, 都有 $d^{\prime}(M, N) \leq 3$, 所以 $d\left(G^{\prime}\right) \leq 3$.

进一步可知, 若 $d(G) \geq 4$, 则 $d\left(G^{\prime}\right) \leq 2$. 否则, $d\left(G^{\prime}\right) \geq 3$, 在上述结论中将 $G$ 换成 $G^{\prime}$, 有 $d(G) \leq 3$, 与 $d(G) \geq 4$ 矛盾.

下面证明: $d(G)+d\left(G^{\prime}\right) \leq \max \{6, n+1\}$.

(1) 若 $d(G) \leq 3, d\left(G^{\prime}\right) \leq 3$, 则 $d(G)+d\left(G^{\prime}\right) \leq 6 \leq \max \{6, n+1\}$.

(2) 若 $d(G) \geq 4$, 则由上面所证, 有 $d\left(G^{\prime}\right) \leq 2$. 又 $G$ 中连接 $A, B$ 的路有 $d(G)+1$ 个顶点 (含 $A, B$ ), 且这些顶点互异, 否则不是最短路, 于是 $d(G)+1 \leq n$. 所以, $d(G)+d\left(G^{\prime}\right) \leq(n-1)+2=n+1 \leq \max \{6, n+1\}$.

另一方面, 当 $G$ 是长为 $n-1$ 的链时, $d(G)+d\left(G^{\prime}\right)=\max \{6, n+1\}$. 实际上, 若 $n=4$, 则 $G$ 与 $G^{\prime}$ 都是长为 3 的链, $d(G)+d\left(G^{\prime}\right)=3+3=6=$ $\max \{6, n+1\}$.

若 $n \geq 5$, 则 $k=n-1$, 对任意两点 $P, Q$, 如果 $P, Q$ 在 $G$ 中不相连, 则 $P, Q$ 在 $G^{\prime}$ 中的距离为 1. 如果 $P, Q$ 在 $G$ 中相连, 则 $P, Q$ 在 $G^{\prime}$ 中的距离不小于 2. 因为 $P, Q$ 在 $G^{\prime}$ 中的度都是 $n-3$, 其度的和为 $2 n-6$, 于是, 由抽屟原理, 其余 $n-2$ 个点中, 至少有一个点向 $P, Q$ 之间连边数 $\geq \frac{2 n-6}{n-2}=$ $\frac{(n-1)+(n-5)}{n-2} \geq \frac{n-1}{n-2}>1$, 所以至少有一个点与 $P, Q$ 都有边相连, 所以 $P, Q$ 在 $G^{\prime}$ 中的距离为 2 . 所以, $d(G)+d\left(G^{\prime}\right)=(n-1)+2=n+1=\max \{6, n+1\}$.

综上所述, 所求 $d(G)+d\left(G^{\prime}\right)$ 的最小值为 $\max \{6, n+1\}$.

评注: 在图论中, 有一类广受关注的 Nordhans-Gaddum Problem, 这一类问题是对图论函数 $f(G)$ 研究

$$
f(G)+f(\bar{G})
$$

和

$$
f(G) \cdot f(\bar{G})
$$

的上界和下界. 第二题是著名图论专家 J. A. Bondy 1970 年研究 $f(G)$ 为直径时的结果. 武钢三中的黄一山同学给出了与 Bondy 相似的证法, 都是通过棱数的估计来达到目标.
第三题: 设 $v_{1}, v_{2}, \cdots, v_{n}$ 是平面上的 $n$ 个单位向量, $n$ 是奇数, 证明: 存在 $\varepsilon_{i} \in\{-1,1\}, i=1,2, \cdots, n$ 使得

$$
\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right| \leq 1
$$

## 解 1 (根据深圳第三中学吴东晓的解法整理而成):

不妨设 $v_{1}=(1,0)$, 否则将所有 $v_{i}(1 \leq i \leq n)$ 同时旋转一个角, 而 $\left|v_{i}\right|$和 $\left|\sum_{i=1}^{n} \varepsilon_{i} v_{i}\right|$ 均不变. 同时, 不妨设 $v_{2}, v_{3}, \cdots, v_{n}$ 均在上半单位圆上, 否则,若有某个 $v_{j}$ 在下半单位圆上, 则用 $-v_{j}$ 代替 $v_{j},-\varepsilon_{j}$ 代替 $\varepsilon_{j}$ 便可. 进一步,我们可设 $v_{1}, v_{2}, \cdots, v_{n}$ 按逆时针排序在上半单位圆上.

注意到 $n$ 是奇数, 要证明题中结论成立, 我们仅须证明:

$$
\left|v_{1}-v_{2}+v_{3}-v_{4}+\cdots+v_{n-2}-v_{n-1}+v_{n}\right| \leq 1
$$

为此, 令 $n=2 k+1\left(k \in \mathbf{N}^{*}\right), \alpha_{1}=v_{3}-v_{2}, \alpha_{2}=v_{5}-v_{4}, \cdots, \alpha_{k}=v_{n}-v_{n-1}$, 这时要证 (1), 转化为证

$$
\left|v_{1}+\alpha_{1}+\cdots+\alpha_{k}\right| \leq 1
$$

记 $\alpha=v_{1}+\alpha_{1}+\cdots+\alpha_{k}$, 设 $l$ 是过原点且方向平行于 $\alpha$ 的直线, 设点 $A^{\prime}(1,0)$ 和点 $C^{\prime}(-1,0)$ 在 $l$ 上的投影分别为 $A, C, l$ 与上半单位圆交于 $B$.不妨设所有向量 $\alpha_{i}$ 均不与 $l$ 相交于非端点, 否则, 记 $\alpha_{i}=\overrightarrow{P Q}$, 将 $\alpha_{i}$ 分为 $\overrightarrow{P B}$ 和 $\overrightarrow{B Q}$ 便可.

设弧 $\widehat{A^{\prime} B}$ 上的向量为 $\alpha_{1}, \cdots, \alpha_{j}$, 弧 $\widehat{B C^{\prime}}$ 上的向量为 $\alpha_{j+1}, \cdots, \alpha_{k}$. 则 $\alpha_{1}, \cdots, \alpha_{j}$ 在 $l$ 上的投影 $\beta_{1}, \cdots, \beta_{j}$ 均落在线段 $A B$ 上, 且两两无公共部分,方向均与 $\overrightarrow{A B}$ 同向. 记 $\gamma_{1}=\beta_{1}+\cdots+\beta_{j}$, 则

$$
\left|\gamma_{1}\right| \leq|A B|
$$

同样, $\alpha_{j+1}, \cdots, \alpha_{k}$ 在 $l$ 上的投影 $\beta_{j+1}, \cdots, \beta_{k}$ 均落在线段 $B C$ 上, 两两无公共部分, 方向均与 $\overrightarrow{B C}$ 相同. 记 $\gamma_{2}=\beta_{j+1}+\cdots+\beta_{k}$, 则

$$
\left|\gamma_{2}\right| \leq|B C|
$$

又显然, $v_{1}$ 在 $l$ 上的投影为 $\overrightarrow{O A}$, 且 $|O A|=|O C|$. 故由向量的分解法则可知

$$
\alpha=\gamma_{1}+\overrightarrow{O A}+\gamma_{2}
$$

因此

$$
|\alpha|=|| \gamma_{1}|+| O A|-| \gamma_{2}||=|| \gamma_{1}|+| O C|-| \gamma_{2}|| .
$$

又由 (3) 和 (4) 可得

$$
\begin{gathered}
\left|\gamma_{1}\right|+|O C|-\left|\gamma_{2}\right| \geq|O C|-|B C|=-|O B|=-1 \\
\left|\gamma_{1}\right|+|O C|-\left|\gamma_{2}\right| \leq|A B|+|O A|=|O B|=1 .
\end{gathered}
$$

综合 (5) (6) 和 (7) 式便得 $|\alpha| \leq 1$, 这就是要证的 (2) 式.

## 解 2 (根据湖北武钢三中陈泽坤、黄一山的解法整理而成):

设 $n=2 k+1\left(k \in \mathbf{N}^{*}\right), v_{i}=\left(x_{i}, y_{i}\right), i=1,2, \cdots, 2 k+1$. 不妨设 $y_{i} \geq 0$, 否

则用 $-v_{i}$ 代替 $v_{i},-\varepsilon_{i}$ 代替 $\varepsilon_{i}$ 便可. 并且不妨设 $x_{1} \leq x_{2} \leq \cdots \leq x_{2 k+1}$. 下面用数学归纳法证明

$$
\left|\sum_{i=1}^{2 k+1}(-1)^{i-1} v_{i}\right| \leq 1
$$

当 $k=1$ 时结论显然成立.

假设结论对 $k$ 成立, 现考虑 $k+1$ 的情况.

首先我们叙述一个事实:

设 $f(x)=\sqrt{1-x^{2}}, x \in[-1,1]$, 则 $f(x)$ 是 $[-1,1]$ 上的凹函数, 即 $f^{\prime \prime}(x) \leq$ 0 , 故对任何的 $0 \leq d \leq 1, g_{d}(x)=f(x+d)-f(x)$ 是 $x \in[-1,1-d]$ 上的单调不增函数.

记

$$
X=\sum_{i=1}^{2 k+1}(-1)^{i-1} x_{i}, Y=\sum_{i=1}^{2 k+1}(-1)^{i-1} y_{i}
$$

下分两种情况讨论:

(i) 当 $Y \geq 0$ 时.

令

$$
\begin{gathered}
v_{1}^{\prime}=\left(x_{3}+x_{1}-x_{2}, f\left(x_{3}+x_{1}-x_{2}\right)\right) \\
v_{2}^{\prime}=\left(x_{3}, f\left(x_{3}\right)\right) \\
v_{i}^{\prime}=v_{i}, i=3,4, \cdots, 2 k+1
\end{gathered}
$$

并记

$$
v_{i}^{\prime}=\left(x_{i}^{\prime}, y_{i}^{\prime}\right), i=1,2, \cdots, 2 k+1
$$

$$
X^{\prime}=\sum_{i=1}^{2 k+1}(-1)^{i-1} x_{i}^{\prime}, Y^{\prime}=\sum_{i=1}^{2 k+1}(-1)^{i-1} y_{i}^{\prime}
$$

则显然有

$$
X^{\prime}=X
$$

又注意到 $x_{1} \leq x_{2} \leq x_{3}$, 并由事实 $\left(^{*}\right)$ 可得

$$
\begin{aligned}
Y^{\prime}-Y & =y_{1}^{\prime}-y_{2}^{\prime}-y_{1}+y_{2} \\
& =f\left(x_{3}+x_{1}-x_{2}\right)-f\left(x_{3}\right)-f\left(x_{1}\right)+f\left(x_{2}\right) \\
& =g_{x_{2}-x_{1}}\left(x_{1}\right)-g_{x_{2}-x_{1}}\left(x_{3}+x_{1}-x_{2}\right) \\
& \geq 0 .
\end{aligned}
$$

即

$$
Y^{\prime} \geq Y
$$

故, 注意到 $v_{2}^{\prime}=v_{3}^{\prime}$, 并由 (8) 和 (9) 及归纳假设可得

$$
\begin{aligned}
\left|\sum_{i=1}^{2 k+1}(-1)^{i-1} v_{i}\right| & =\sqrt{X^{2}+Y^{2}} \leq \sqrt{X^{\prime 2}+Y^{\prime 2}} \\
& =\left|\sum_{i=1}^{2 k+1}(-1)^{i-1} v_{i}^{\prime}\right|=\left|v_{1}^{\prime}+\sum_{i=4}^{2 k+1}(-1)^{i-1} v_{i}\right| \leq 1
\end{aligned}
$$

(ii) 当 $Y \leq 0$ 时.

令

$$
\begin{gathered}
v_{1}^{\prime}=(-1,0), \\
v_{2}^{\prime}=\left(-1-x_{1}+x_{2}, f\left(-1-x_{1}+x_{2}\right)\right), \\
v_{i}^{\prime}=v_{i}, i=3,4, \cdots, 2 k+1,
\end{gathered}
$$

并记

$$
\begin{gathered}
v_{i}^{\prime}=\left(x_{i}^{\prime}, y_{i}^{\prime}\right), i=1,2, \cdots, 2 k+1 \\
X^{\prime}=\sum_{i=1}^{2 k+1}(-1)^{i-1} x_{i}^{\prime}, Y^{\prime}=\sum_{i=1}^{2 k+1}(-1)^{i-1} y_{i}^{\prime}
\end{gathered}
$$

再令

$$
\begin{gathered}
v_{2 k+1}^{\prime \prime}=(1,0) \\
v_{2 k}^{\prime \prime}=\left(1-x_{2 k+1}^{\prime}+x_{2 k}^{\prime}, f\left(1-x_{2 k+1}^{\prime}+x_{2 k}^{\prime}\right)\right)
\end{gathered}
$$

$$
v_{i}^{\prime \prime}=v_{i}^{\prime}, i=1,2, \cdots, 2 k-1
$$

并记

$$
\begin{gathered}
v_{i}^{\prime \prime}=\left(x_{i}^{\prime \prime}, y_{i}^{\prime \prime}\right), i=1,2, \cdots, 2 k+1 \\
X^{\prime \prime}=\sum_{i=1}^{2 k+1}(-1)^{i-1} x_{i}^{\prime \prime}, Y^{\prime \prime}=\sum_{i=1}^{2 k+1}(-1)^{i-1} y_{i}^{\prime \prime}
\end{gathered}
$$

则显然有

$$
X^{\prime \prime}=X^{\prime}=X
$$

又注意到 $x_{1} \geq-1, x_{2 k+1}^{\prime} \leq 1$, 分别应用事实 $\left(^{*}\right)$ 可得

$$
\begin{aligned}
Y^{\prime}-Y & =y_{1}^{\prime}-y_{2}^{\prime}-y_{1}+y_{2} \\
& =f(-1)-f\left(-1-x_{1}+x_{2}\right)-f\left(x_{1}\right)+f\left(x_{2}\right) \\
& =g_{x_{2}-x_{1}}\left(x_{1}\right)-g_{x_{2}-x_{1}}(-1) \\
& \leq 0 .
\end{aligned}
$$

$$
\begin{aligned}
Y^{\prime \prime}-Y^{\prime} & =y_{2 k+1}^{\prime \prime}-y_{2 k}^{\prime \prime}-y_{2 k+1}^{\prime}+y_{2 k}^{\prime} \\
& =f(1)-f\left(1-x_{2 k+1}^{\prime}+x_{2 k}^{\prime}\right)-f\left(x_{2 k+1}^{\prime}\right)+f\left(x_{2 k}^{\prime}\right) \\
& =g_{x_{2 k+1}^{\prime}-x_{2 k}^{\prime}}\left(1-x_{2 k+1}^{\prime}+x_{2 k}^{\prime}\right)-g_{x_{2 k+1}^{\prime}-x_{2 k}^{\prime}}\left(x_{2 k}^{\prime}\right) \\
& \leq 0 .
\end{aligned}
$$

即有

$$
Y^{\prime \prime} \leq Y^{\prime} \leq Y \leq 0
$$

故, 注意到 $v_{1}^{\prime \prime}+v_{2 k+1}^{\prime \prime}=0$, 并由 (10) 和 (11) 及归纳假设可得

$$
\begin{aligned}
\left|\sum_{i=1}^{2 k+1}(-1)^{i-1} v_{i}\right| & =\sqrt{X^{2}+Y^{2}} \leq \sqrt{X^{\prime 2}+Y^{\prime 2}} \leq \sqrt{X^{\prime \prime 2}+Y^{\prime \prime 2}} \\
& =\left|\sum_{i=1}^{2 k+1}(-1)^{i-1} v_{i}^{\prime \prime}\right|=\left|\sum_{i=2}^{2 k}(-1)^{i-1} v_{i}^{\prime \prime}\right| \leq 1
\end{aligned}
$$

综合 (i) 和 (ii), 便知 $n=k+1$ 时结论也成立.

故由数学归纳可知结论成立.
解 3 (Barany 等):

记 $P=\operatorname{conv}\left\{ \pm v_{i}, i=1,2, \cdots, n\right\}$, 则 $P$ 是一个内接于单位圆的中心对称凸多边形. 因为用 $-v_{i}$ 代替 $v_{i}$ 不改变问题的条件与结论, 因此不妨设 $P$ 的顶点 $v_{1}, v_{2}, \cdots, v_{n},-v_{1},-v_{2}, \cdots,-v_{n}$ 按逆时针排列在单位圆上.

因 $n$ 是奇数, 我们仅须证明

$$
\left|v_{1}-v_{2}+v_{3}-\cdots-v_{n-1}+v_{n}\right| \leq 1 .
$$

为此, 令 $u=2\left(v_{1}-v_{2}+v_{3}-\cdots-v_{n-1}+v_{n}\right)$. 并令 $a_{i}=v_{i+1}-v_{i}, i=1,2, \cdots, n-$ $1, a_{n}=-v_{1}-v_{n}, w=a_{1}-a_{2}+a_{3}-\cdots+a_{n}$. 则由 $a_{i}(1 \leq i \leq n)$ 的定义有

$$
w=-2\left(v_{1}-v_{2}+v_{3}-\cdots-v_{n-1}+v_{n}\right)=-u
$$

故 $|u|=|w|$. 这样要证 (12) 式成立, 我们仅须证明

$$
|w| \leq 2
$$

设 $l$ 是过原点且方向平行于 $w$ 的一条直线, 它与 $P$ 的边界交于点 $b,-b$. 由对称性, 不妨设 $b$ 落在 $P$ 的边 $\left[v_{1},-v_{n}\right]$ 上. 故 $w$ 恰是边向量 $a_{1},-a_{2}, a_{3}, \cdots, a_{n}$ 沿平行于 $\left[v_{1},-v_{n}\right]$ 的方向在 $l$ 上的投影之和. 这些投影是不重叠的 (除了端点外), 并且恰好覆盖 $l$ 上的线段 $[b,-b]$, 故 $|w| \leq 2$, 即 (13) 式得证.

评注: 第三题似乎是一个经典问题. $n=3$ 的情况是 2007 年罗马尼亚的试题. 最近 I. Barany 等人在Discrete Math. 13(2013) 上重新研究了这个问题. 第三题是他们文章中的第一个结果.

值得注意, $n$ 是奇数的条件是必须的, 不可去掉. 他们在这一文章中还证明了如下有趣的结论: 设 $v_{1}, v_{2}, \cdots, v_{n}$ 是平面的单位向量, 则存在 $\varepsilon_{i} \in\{-1,1\}, i=1,2, \cdots, n$ 使得

$$
\left|\sum_{i=1}^{k} \varepsilon_{i} v_{i}\right| \leq 2
$$

对每个奇数 $k \in\{1,2, \cdots, n\}$ 成立.
第四题: 对给定的正整数 $n \geq 8$, 证明: 存在自然数的集合 $A$ 使得 $|A|=n$且

$$
|A-A|<|A+A| \text {. }
$$

其中 $A-A=\{a-b \mid a \in A, b \in A\}, A+A=\{a+b \mid a \in A, b \in A\}$.

证明: 首先引进一些记号和定义: 首先定义 $a-A=\{a\}-A$. 如果 $a^{*} \in A$ 且使得 $A=a^{*}-A$, 则称 $A$ 关于 $a^{*}$ 对称. 如果 $A$ 关于 $a^{*}$ 对称, 则

$$
|A+A|=\left|A+\left(a^{*}-A\right)\right|=\left|a^{*}+(A-A)\right|=|A-A| \text {. }
$$

下面构造 $n=8$ 时的例子: 记

$$
A_{1}=\{0,2,3,4,7,11,12,14\} .
$$

再说明 $A_{1}$ 满足要求. 事实上, 记 $A^{*}=A_{1} \backslash\{4\}$, 注意到 $A^{*}$ 是关于 14 对称的. 所以 $\left|A^{*}+A^{*}\right|=\left|A^{*}-A^{*}\right|=\left|A_{1}-A_{1}\right|$. 又 $8 \in\left(A_{1}+A_{1}\right) \backslash\left(A^{*}+A^{*}\right)$, $A^{*}+A^{*} \subseteq A_{1}+A_{1}$, 故 $\left|A_{1}+A_{1}\right|>\left|A_{1}-A_{1}\right|, A_{1}$ 满足要求.

怎样将 $n=8$ 的结果推广到一般的 $n$ 呢? 注意 $A_{1}$ 可表示为

$$
\begin{aligned}
A_{1} & =\{0,2,3,7,11,12,14\} \cup\{4\} \\
& =\{0,2\} \cup\{3,7,11\} \cup\{14-\{0,2\}\} \cup\{4\} .
\end{aligned}
$$

这启发我们构造一般 $n(n \geq 8)$ 的例子.

记 $A^{*}=\{0,2\} \cup\{3,7,11, \cdots, 4 k-1\} \cup\{4 k, 4 k+2\}$, 其中 $k>2$, 则 $A=$ $A^{*} \cup\{4\}$ 就是满足 $|A-A|<|A+A|$ 的 $n$ 元集.

下面证明 $A$ 确实满足要求. 注意到 $A^{*}$ 关于 $4 k+2$ 对称, 因此

$$
\left|A^{*}+A^{*}\right|=\left|A^{*}-A^{*}\right| .
$$

又 $A^{*}+A^{*} \subseteq A+A$, 且 $8 \in(A+A) \backslash\left(A^{*}-A^{*}\right)$. 故, $|A+A|>\left|A^{*}+A^{*}\right|$.这样要证结论成立, 仅须证明

$$
|A-A|=\left|A^{*}-A^{*}\right| .
$$

这只须证明: $A^{*}-\{4\} \subseteq A^{*}-A^{*}$ 便可. 这个论断可有下面几个简单
事实推出:

$$
\begin{aligned}
1 & =3-2 \in A^{*}-A^{*} \\
4 & =7-3 \in A^{*}-A^{*} \\
4 k-4 & =(4 k-1)-3 \in A^{*}-A^{*} \\
4 k-2 & =4 k-2 \in A^{*}-A^{*} .
\end{aligned}
$$

证毕.

评注: 在组合数论中, 满足 $|A+A|>|A-A|$ 的集合 $A$ 叫做和比差多的集合 (more sums than differences)，简称 MSTD 集. 关于 MSTD 集的研究文献不少. 第四题是数学家 Nathanson 于 2007 年发表在J.Combin. Number Theory 杂志上一论文的结果. 这可能是整数 MSTD 集的第一个 explicit 构造.

值得指出的是, Hegary 证明了不存在 $n<8$ 的整数 MSTD 集. 我们认为, 第四题是一个很难的问题, 郑州外国语学校的朱书聪同学、大连二十四中的余佳弘同学能给出此问题的正确构造, 值得赞赏.

最后, 我们感谢冯跃峰老师帮助审查了第二题的全部解答, 修改整理了朱书聪同学的解答. 感谢岑爱国老师、李雨红老师和席东盟博士参与了第三题讨论, 指出并订正了原来的错误.

