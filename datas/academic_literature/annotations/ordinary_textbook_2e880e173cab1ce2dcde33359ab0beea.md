# 数学新星问题征解第五期解答 

2014.10

第一题: $Q$ 同学参加某次考试, 考试共由 $4 a+1$ 道题组成, 每题有 4 个选项, 只有一个是对的, 且概率都为 $\frac{1}{4}$. 每题选对得 4 分, 选错不得分, 不选得 1 分. 已知金牌分数线为 $4 b+1$ 分, 其中 $a, b$ 为正整数且满足 $4(4 a+1) \geq 4 b+1, b \geq \frac{4}{3} a$. 若 $Q$ 同学所有题都不会做, 问他将多少个题选出答案可使获金牌的概率最大?

(东北师大附中学生 浦鸿铭 供题)

## 证明 (根据吴东晓同学的解答整理):

设 $Q$ 选了 $i(i \in \mathbf{N})$ 个题, 则在 $i$ 个题中, $Q$ 答对 $k(k \in \mathbf{N})$ 个题的概率为 $C_{i}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{i-k}(k=0,1, \cdots, i)$, 即 $Q$ 得分为 $4 k+(4 a+1-i)$ 的概率是 $C_{i}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{i-k}(k=0,1, \cdots, i)$. 当 $b-a+\frac{i}{4} \leq k \leq i$ 时, 有 $4 k+(4 a+1-i) \geq 4 b+1$.故 $Q$ 获金牌的概率为

$$
P(i)=\sum_{b-a+\frac{i}{4} \leq k \leq i} C_{i}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{i-k}
$$

问题即要求 $P(i)(0 \leq i \leq 4 a+1)$ 在何值时取得最大值.

当 $i<\frac{4}{3}(b-a)$ 时, $P(i)=0$, 故下面只需考虑 $i \geq \frac{4}{3}(b-a)$ 的情况.

当 $4 \nmid i$ 且 $i<4 a+1$ 时, 有

$$
\begin{aligned}
P(i) & =\sum_{b-a+\frac{i}{4} \leq k \leq i} C_{i}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{i-k} \\
& \leq \sum_{b-a+\frac{i}{4} \leq k \leq i} C_{i+1}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{i+1-k} \\
& <\sum_{b-a+\frac{i+1}{4} \leq k \leq i+1} C_{i+1}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{i+1-k} \\
& =P(i+1)
\end{aligned}
$$

当 $i=4 c\left(c \in \mathbf{Z}^{+}\right)$且 $i<4 a$ 时, 有

$$
\begin{aligned}
P(i)=P(4 c) & =\sum_{b+c-a}^{4 c} C_{4 c}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{4 c-k} \\
& \leq \sum_{b+c-a}^{4 c} C_{4 c+4}^{k+1}\left(\frac{1}{4}\right)^{k+1}\left(\frac{3}{4}\right)^{4 c+4-k-1} \\
& <\sum_{b+c+1-a}^{4 c+4} C_{4 c+4}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{4 c+4-k} \\
& =P(4 c+4) .
\end{aligned}
$$

综上所述, $P(i)$ 的最大值只可能是 $P(4 a)$ 或 $P(4 a+1)$. 又因为

$$
\begin{aligned}
P(4 a+1) & =\sum_{b+1}^{4 a+1} C_{4 a+1}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{4 a+1-k} \\
& <\sum_{b+1}^{4 a+1} C_{4 a}^{k-1}\left(\frac{1}{4}\right)^{k-1}\left(\frac{3}{4}\right)^{4 a+1-k} \\
& =\sum_{b}^{4 a} C_{4 a}^{k}\left(\frac{1}{4}\right)^{k}\left(\frac{3}{4}\right)^{4 a-k} \\
& =P(4 a),
\end{aligned}
$$

故

$$
\max _{0 \leq i \leq 4 a+1} P(i)=P(4 a),
$$

即 $Q$ 同学将 $4 a$ 个题选出答案可使获金牌的概率最大.

第二题: 证明: 对任意素数 $p$, 存在无穷多个正整数对 $(m, n)$ 使得 $[n \sqrt{p}]=\frac{3 m^{2}-m}{2}$.

(山东历城二中学生 齐仁睿 供题)

## 证明 (根据齐仁睿同学的解答整理):

当 $\left\{\frac{3 m^{2}-m}{2 \sqrt{p}}\right\}>1-\frac{1}{\sqrt{p}}$ 时, 取 $n=\left[\frac{3 m^{2}-m}{2 \sqrt{p}}\right]+1$, 便易知结论成立. 故只需证明满足 $\left\{\frac{3 m^{2}-m}{2 \sqrt{p}}\right\}>1-\frac{1}{\sqrt{p}}$ 的 $m$ 可以任意大.

事实上, 由于 $\frac{3}{\sqrt{p}}$ 是无理数, $\left\{\frac{3 n}{\sqrt{p}}\right\}$ 在 $(0,1)$ 上是稠密的, 故只需证明:对任意的 $m \in \mathbf{N}_{+}$, 存在 $t \in \mathbf{N}_{+}$使得 $\left\{\frac{3(m+t)^{2}-(m+t)}{2 \sqrt{p}}\right\}$ 在 $\bmod 1$ 的意义下充分接近 $\left\{\frac{3 m^{2}-m}{2 \sqrt{p}}\right\}+\frac{3}{\sqrt{p}}$.
取 Pell 方程 $x^{2}-p y^{2}=1$ 的一组充分大的解 $(x, y)$, 令 $t=2 x$, 则有

$$
\begin{aligned}
& \frac{3(m+t)^{2}-(m+t)}{2 \sqrt{p}}-\frac{3 m^{2}-m}{2 \sqrt{p}}=\frac{1}{\sqrt{p}}\left(6 m x+6 x^{2}-x\right) \\
& =(6 m-1) \frac{x}{\sqrt{p}}+\frac{6 x^{2}}{\sqrt{p}}=(6 m-1) \sqrt{y^{2}+\frac{1}{p}}+6 x \sqrt{y^{2}+\frac{1}{p}} \\
& \equiv o(1)+6 x\left(y+\frac{\frac{1}{p}}{y+\sqrt{y^{2}+\frac{1}{p}}}\right) \equiv o(1)+\frac{6 x}{2 p y} \\
& \equiv o(1)+\frac{3}{\sqrt{p}} \quad(\bmod 1) .
\end{aligned}
$$

因此原结论成立.

第三题: 称一个矩形为 “格矩形” 当且仅当该矩形两边平行于坐标轴且四顶点均为格点. 给定无穷多个不同的格矩形, 证明: 可以从中选出无穷多个, 使得它们或者两两有覆盖关系, 或者两两不交.

(山东历城二中学生 齐仁睿 供题)

## 证明 (根据齐仁睿同学的解答整理):

首先证明一个引理：给定无穷多个两端点均为整数的闭区间 (可以有相同的), 如果任取其中无穷多个, 都有两个有交集, 则可以取出其中无穷多个使得它们两两有包含关系.

引理的证明: 如果某个区间出现无穷多次, 则引理显然成立. 故不妨设给出的闭区间两两不同.

对任意的区间, 我们定义它的层数：如果某个区间不包含其它区间,则它的层数为 1 ; 对包含其它区间的区间, 它的层数为其包含区间的最大层数加 1 . 由层数的定义便知, 同层的区间互不包含.

如果某一层的区间有无穷多个, 任取其中一个 $[a, b](a, b \in \mathbf{Z})$, 假设它包含 $m\left(m \in \mathbf{N}^{*}\right)$ 个整点, 对每个整点, 与 $[a, b]$ 的层数相同且以此点为端点的区间至多有两个 (这点的两侧各至多一个). 故至多有限个同层区间与 $[a, b]$ 相交. 因此可选出无穷多个该层的区间两两不交, 再由 $[a, b]$ 的任意性便知此时引理成立. 若不然, 每层的区间数都有限, 故存在任意大的区间层数. 易知若第 $n+1\left(n \in \mathbf{N}^{*}\right)$ 层区间存在, 则第 $n$ 层区间存在. 故每层区间构成有限集. 由于任何层数大于 1 的区间包含一个层数为 1 的区间, 故有一个层数为 1 的区间 $I_{1}$ 被无穷多个区间所包含, 即有一个层数为 2 的区间 $I_{2}$ 包含 $I_{1}$ 且被无穷多个区间所包含 (层数更高的区间包含
$I_{1}$ 时一定先包含一个 2 层的区间). 同理可以找到 $I_{3}, I_{4}, \cdots$, 其中, 对任意的 $i<j \in \mathbf{N}^{*}$ 有 $I_{i} \subseteq I_{j}$, 故引理得证.

回到原题.

考虑这些格矩形在 $x$ 轴上的投影. 若其中有无穷多个互不相交, 则它们对应的原矩形就满足要求; 若不然, 由引理可知存在 $I_{1} \subseteq I_{2} \subseteq \cdots$ 是一组两两包含的区间, 它们对应的矩形在 $y$ 轴上有无穷多的投影. 如果这些投影中有无穷多个互不相交, 则结论成立. 否则, 再次由引理可知存在 $J_{1} \subseteq J_{2} \subseteq \cdots$ 是一组两两包含的区间. 不妨设 $J_{i}$ 与 $I_{a_{i}}$ 对应同一个矩形, 我们取一个 $a_{1}, a_{2}, \cdots$ 的递增子序列 $a_{k_{1}}<a_{k_{2}}<\cdots$, 则 $J_{k_{1}}, J_{k_{2}}, \cdots$ 对应的矩形满足要求.

第四题: 对于 $\{1,2, \cdots, n\}$ 的一个排列 $\sigma$, 记 $f(\sigma)$ 为每次交换 $\sigma$ 的两个数, 将 $\sigma$ 变为 $\sigma_{0}=\{1,2, \cdots, n\}$ 的最少步数, 这里 $f\left(\sigma_{0}\right)=0, f(\sigma) \in$ $\{0,1,2, \cdots, n-1\}$. 记 $T(i)=\{\sigma \mid f(\sigma)=i\}, i=0,1,2, \cdots, n-1$. 求 $\sum_{i=0}^{n-1} i^{2}|T(i)|$. (深圳中学学生 周輼坤 供题)

## 证明 (根据吴东晓同学的解答整理):

首先由排列知识知, 若排列 $\sigma$ 的对应有向图有 $t\left(t \in \mathbf{N}^{*}\right)$ 个连通分支, 则从 $\sigma$ 变换到 $\sigma_{0}$ 的所需的最少对换次数即为 $n-t$.

记 $\sigma$ 对应的有向图的连通分支个数为 $g(\sigma)$, 则 $f(\sigma)=n-g(\sigma)$. 记 $1,2, \cdots, n$ 的所有排列构成的集合为 $S_{n}$, 则

$$
\sum_{i=0}^{n-1} i^{2}|T(i)|=\sum_{i=0}^{n-1} \sum_{f(\sigma)=i} i^{2}=\sum_{\sigma \in S_{n}}(n-g(\sigma))^{2}
$$

令 $G_{i}(n)=\sum_{\sigma \in S_{n}}(n-g(\sigma))^{i}$, 则有

$$
\begin{gathered}
G_{1}(1)=0 \\
G_{1}(n+1)=\sum_{\sigma \in S_{n+1}}(n+1-g(\sigma)) \\
=\sum_{\substack{\sigma \in S_{n+1} \\
\sigma(n+1)=n+1}}(n+1-g(\sigma))+\sum_{\substack{\sigma \in S_{n+1} \\
\sigma(n+1) \neq n+1}}(n+1-g(\sigma))
\end{gathered}
$$

$$
\begin{aligned}
& =\sum_{\sigma \in S_{n}}(n+1-g(\sigma)-1)+n \sum_{\sigma \in S_{n}}(n+1-g(\sigma)) \\
& =G_{1}(n)+n \cdot n !+n G_{1}(n) \\
& =(n+1) G_{1}(n)+n \cdot n !
\end{aligned}
$$

由 (1) 和 (2) 便得

$$
G_{1}(n)=n !\left(n-1-\frac{1}{2}-\cdots-\frac{1}{n}\right) .
$$

同样地,

$$
G_{2}(1)=0 \text {. }
$$

$$
\begin{aligned}
& G_{2}(n+1)=\sum_{\sigma \in S_{n+1}}(n+1-g(\sigma))^{2} \\
& =\sum_{\substack{\sigma \in S_{n+1} \\
\sigma(n+1)=n+1}}(n+1-g(\sigma))^{2}+\sum_{\substack{\sigma \in S_{n+1} \\
\sigma(n+1) \neq n+1}}(n+1-g(\sigma))^{2} \\
& =\sum_{\sigma \in S_{n}}(n+1-g(\sigma)-1)^{2}+n \sum_{\sigma \in S_{n}}(n+1-g(\sigma))^{2} \\
& =\sum_{\sigma \in S_{n}}(n-g(\sigma))^{2}+n \sum_{\sigma \in S_{n}}\left[(n-g(\sigma))^{2}+2(n-g(\sigma))+1\right] \\
& =(n+1) G_{2}(n)+2 n G_{1}(n)+n \cdot n ! .
\end{aligned}
$$

由 (3), (4) 和 (5) 便得

$$
G_{2}(n)=\left[\left(n-1-\frac{1}{2}-\cdots-\frac{1}{n}\right)^{2}+\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)-\left(1+\frac{1}{2^{2}}+\cdots+\frac{1}{n^{2}}\right)\right] \cdot n ! .
$$

故

$$
\sum_{i=0}^{n-1} i^{2}|T(i)|=G_{2}(n)=\left[\left(n-1-\frac{1}{2}-\cdots-\frac{1}{n}\right)^{2}+\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)-\left(1+\frac{1}{2^{2}}+\cdots+\frac{1}{n^{2}}\right)\right] \cdot n ! .
$$

