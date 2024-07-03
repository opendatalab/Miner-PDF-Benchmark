数学新星网 实学生专栏

www.nsmath.cn/xszl

# 两道匈牙利数学竞赛问题的评析 

于翔宇

(吉林大学附属中学, 长春, 130021)

匈牙利是最早开展中学生数学竞赛的国家之一, 他们的数学杂志及各级别竞赛中命制了许多不错的问题. 本文中我们将讨论其中的两个问题.

问题 $1(\mathrm{KöMaL}, \mathrm{A} 647)$ 设 $k$ 是一个非负整数, 证明: 仅存在有限多个正整数 $n$, 使得存在两个不相交的集合 $A, B$. 满足 $A \cup B=\{1,2, \cdots, n\}$ 且

$$
\left|\prod_{a \in A} a-\prod_{b \in B} b\right|=k
$$

分析 在问题 1 中, 比较关键的是寻求一条利用 $\left|\prod_{a \in A} a-\prod_{b \in B} b\right|=k$ 来限制 $A, B$, 进而限制 $n$ 的途径. 能走的不外乎大小估计和整除分析两条路. 因为大小估计似乎并不容易进行, 所以我们先从整除分析来入手.

考虑一个素数 $p$ 在等式两边的整除性, 注意到由于 $A \cup B$ 是 $\{1,2, \cdots, n\}$的一个分划, 那么对于素数 $p \leq n$. 必有

$$
p \mid \prod_{a \in A} a \cdot \prod_{b \in B} b
$$

这时, 如果 $p \mid k$, 那么我们似乎得不到什么有力的限制. 不过, 如果 $k \neq 0$, 那么 $k$ 的素因子只有有限多个, 这对充分大的 $n$ 起到的影响或许不大. 下面我们先考虑 $k$ 为正整数的情形.

对于 $p \leq n, p \nmid k$ 的素数 $p$, 我们可以从 $\left|\prod_{a \in A} a-\prod_{b \in B} b\right|=k$ 中得到一个关键信息, 这就是：

$$
\prod_{a \in A} a \text { 和 } \prod_{b \in B} b \text { 恰有一个能被 } p \text { 整除. }
$$

而这一信息可谓是很强的限制, 因为这时只要 $A$ 或 $B$ 中的某一个包含了一个 $p$的倍数, 我们就可以判定 $p$ 的所有倍数都在该集合中. 这样我们可以从素数 $p$的倍数联系到素数 $q$ 的倍数 (只要 $p q \leq n,(p, k)=(q, k)=1$ ), 最终会导致大部

收稿日期: 2016-04-23; 修订日期: 2016-06-25.
分的素数及其倍数要在同一个集合中, 这就从大小上带来了矛盾.

从上述分析入手, 我们给出如下的证明.

证明 若 $k=0$, 则 $\prod_{a \in A} a=\prod_{b \in B} b$. 故

$$
n !=\prod_{a \in A} a \cdot \prod_{b \in B} b
$$

是完全平方数. 但由 Chebyshev 定理 (见注 1 ), 对 $n \geq 2$, 区间 $\left(\frac{n}{2}, n\right]$ 中存在一个素数. 设素数 $p \in\left(\frac{n}{2}, n\right]$, 则容易得到 $p \| n !$. 故 $n$ ! 不是完全平方数, 即这时不存在符合要求的 $n$.

若 $k \geq 1$, 则大于 $k$ 的素数都与 $k$ 互素. 故对于素数 $q$, 满足 $k<q \leq n$, 且 $\left\{q, 2 q, \cdots,\left[\frac{n}{q}\right] \cdot q\right\}$ 在同一个集中.

那么我们取一个素数 $p>k$. 这时考虑满足要求的 $n>2 p^{2}$, 不妨设分划后 $p \in A$, 则

$$
\left\{p, 2 p, \cdots,\left[\frac{n}{p}\right] p\right\} \subseteq A,
$$

进而对素数 $q \in\left(k,\left[\frac{n}{p}\right]\right.$, 有

$$
\left\{q, 2 q, \cdots,\left[\frac{n}{q}\right] q\right\} \subseteq A
$$

这是因为 $q \cdot p \in A$, 从而 $q \nmid \prod_{b \in B} b$.

故 $\prod_{b \in B} b$ 的素因子只能在 $[1, k] \cup\left[\left[\frac{n}{p}\right], n\right]$ 中. 因此, 我们来估计 $\prod_{b \in B} b$ 的大小.

引入记号 $\nu_{q}(m)$ 代表素数 $q$ 在正整数 $m$ 中的幂次. 则对 $q \in[1, k] \cup\left[\left[\frac{n}{p}\right], n\right]$,

$$
\nu_{q}\left(\prod_{b \in B} b\right) \leq \nu_{q}(n !)<\frac{n}{q-1} .
$$

这是因为 $B \subseteq\{1,2, \cdots, n\}$, 而

$$
v_{q}(n !)=\sum_{i=1}^{+\infty}\left[\frac{n}{q^{i}}\right]<\sum_{i=1}^{+\infty} \frac{n}{q^{i}}
$$

其中对 $q \in[1, k]$, 有 $\frac{n}{q-1}$, 对 $q \in\left[\left[\frac{n}{p}\right], n\right]$, 有 $\frac{n}{q-1}<2 p$. 这是因为 $q-1>\frac{n}{p}-2$, 而 $n>2 p^{2}$.

于是我们有

$$
\begin{aligned}
\prod_{b \in B} b & <\left(\prod_{q \leq k} q\right)^{n} \cdot\left(\prod_{q \in\left[\left[\frac{n}{p}\right], n\right]} q\right)^{2 p} \\
& \leq(k !)^{n} \cdot\left(\prod_{q \leq n} q\right)^{2 p} .
\end{aligned}
$$

其中右式字母 $q$ 表示满足条件的素数.

而由 Erdös 引理 (见注 2 ), 得 $\prod_{q \leq n} q \leq 4^{n}$, 所以

$$
\prod_{b \in B} b<\left(k ! \cdot 4^{2 p}\right)^{n} .
$$

进而

$$
n ! \leq\left(\prod_{b \in B}\right)\left(k+\prod_{b \in B} b\right)<\left(k+k ! \cdot 4^{2 p}\right)^{n}
$$

记 $k+k ! \cdot 4^{2 p}=C,\left(C\right.$ 是常数). 而对 $n>C^{2}$, 由于

$$
n !=\left(\prod_{i=1}^{n} i(n+1-i)\right)^{\frac{1}{2}} \geq n^{\frac{n}{2}}>C^{n}
$$

所以对 $n>C^{2}, n$ 不可能符合要求.

$k \geq 1$ 的情形也得证.

评注 本题是有一定难度的, 关键在于将集合中数之积通过分解的方式估计大小, 可以说有一定的分析色彩. 另外, 本题证明中还用到了两个定理.

(1) Chebyshev 定理: 对正整数 $n \geq 2$, 区间 $\left(\frac{n}{2}, n\right]$ 中有一个素数.

这一定理是初等数论中的一个经典结果, 证明较长, 有兴趣的同学可以参阅相关书籍.

(2) Erdös 引理: 设 $q \leq n$ 是素数, 则

$$
\prod_{q \leq n} q \leq 4^{n}
$$

证明 我们对 $n$ 用第二数学归纳法.

当 $n=1,2$ 时, 直接验证即可.

假设 $n \geq 3$ 时, 该引理对 $1,2, \cdots, n-1$ 均成立. 下面考虑 $n$ 时的情形.

当 $n$ 为偶数时, 易知 $n$ 不是素数. 应用归纳假设, 得

$$
\prod_{q \leq n} q=\prod_{q \leq n-1} q \leq 4^{n-1}<4^{n}
$$

当 $n$ 为奇数时, 考察组合数 $\mathrm{C}_{n}^{\frac{n-1}{2}}$. 由于对素数 $q \in\left[\frac{n+1}{2}, n\right]$, 有 $q \left\lvert\, \mathrm{C}_{n}^{\frac{n-1}{2}}\right.$. 故

$$
\prod_{q \in\left[\frac{n+1}{2}, n\right]} q \leq \mathrm{C}_{n}^{\frac{n-1}{2}}=\frac{1}{2}\left(\mathrm{C}_{n}^{\frac{n-1}{2}}+\mathrm{C}_{n}^{\frac{n+1}{2}}\right) \leq \frac{1}{2} \cdot 2^{n}<4^{\frac{n}{2}}
$$

应用归纳假设, 得

$$
\prod_{q \leq n} q \leq 4^{\frac{n}{2}} \cdot 4^{\frac{n}{2}}=4^{n} .
$$

故引理获证.

问题 2 (Hungary NMO, 2015) 设 $a=\left\{a_{1}<a_{2}<\cdots<a_{k}\right\}$ 是一个由非负整数组成的有限集, $B=\left\{b_{1}<b_{2}<\cdots\right\}$ 是一个由非负整数组成的无限集.已知每一个非负整数都可唯一表示成 $a_{i}+b_{j}$ 的形式. 证明: 存在 $c>0$ 使得每个非负整数 $b$ 是 $B$ 中的一个元当且仅当 $b+c$ 也是 $b$ 中的一个元.

分析 问题 2 是一个与非负整数的表示法相关的问题. 每个数恰有唯一的 $a_{i}+b_{j}$ 的表示方式, 这对我们用母函数来刻画是有利的. 事实上, 如果记多项式 $A(x)=\sum_{i=1}^{k} x^{a_{i}}$, 形式幂级数 $B(x)=\sum_{j=1} x^{b_{j}}$, 那么

$$
A(x) \cdot B(x)=1+x+x^{2}+\cdots=\frac{1}{1-x} .
$$

不过, 想要从 $\frac{1}{1-x}$ 入手分析会遇到重重困难, 我们还是选择比较系数为宜.

证明 定义数列 $\left\{\varepsilon_{m}\right\}_{m \geq 0}: \varepsilon_{m} \in\{0,1\}$, 且 $\varepsilon_{m}=1$ 当且仅当 $m \in B$. 那么

$$
B(x)=\sum_{j \geq 1} x^{b_{j}}=\sum_{m \geq 0} \varepsilon_{m} x^{m}
$$

由于 $A(x)=\sum_{i=1}^{k} x^{a_{i}}$, 而 $A(x) \cdot B(x)=1+x+x^{2}+\cdots$. 所以比较两边的 $m$次项系数 (其中 $m \geq a_{k}$ ) 可知

$$
\sum_{i=1}^{k} \varepsilon_{m-a_{i}}=1
$$

事实上, 这是因为右边的 $m$ 次项 $x^{m}$ 可能是由 $x^{a_{1}}, x^{a_{2}}, \cdots, x^{a_{k}}$ 中一些与 $B(x)$中的 $x^{m-a_{i}}$ 项相乘得到的, 其系数为 $\varepsilon_{m-a_{i}}$.

接下来对 $(*)$ 式模 2 分析.

我们考虑模 2 意义下的 $\left\{\varepsilon_{m}\right\}_{m \geq 0}$, 它仍为 $0-1$ 序列, 且对 $a_{1}<a_{2}<\cdots<a_{k}$, (*) 式可视作一个 $a_{k}-a_{1}+1$ 阶递推式, 从而它在模 2 意义下必是最终周期的.进一步, 由于 2 是素数, 它也是纯周期的.

由于 $\varepsilon_{m} \in\{0,1\}$, 可见 $\left\{\varepsilon_{m}\right\}_{m \geq 0}$ 本身就是纯周期的.

设周期为 $c\left(c \in \mathbb{N}_{+}\right)$, 那么当然就有对非负整数 $b$, 满足

$$
b \in B \Leftrightarrow b+c \in B .
$$

命题得证.

评注 上述做法关键在于将数列 $b_{1}, b_{2}, \cdots$ 改用 $0-1$ 序列 $\varepsilon_{0}, \varepsilon_{1}, \cdots$ 来刻画,也就是引入 “特征函数” .
另外, 从证得的结论继续出发, 我们可以得到

$$
B(x)=\frac{1}{1-x^{c}} \sum_{j=1}^{l} x^{b_{j}}, \quad b_{1}<b_{2}<\cdots<b_{l}<c .
$$

即

$$
\left(\sum_{i=1}^{k} x^{a_{i}}\right)\left(\sum_{j=1}^{l} x^{b_{j}}\right)=\frac{1-x^{c}}{1-x}=x^{c-1}+\cdots+x+1 .
$$

所以符合要求的 $A, B$ 都可以这样生成.

