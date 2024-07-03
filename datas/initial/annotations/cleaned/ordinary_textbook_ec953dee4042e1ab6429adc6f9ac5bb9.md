数学新星网 兴学生专栏

www.nsmath.cn/xszl

# 2020 年普特南数学竞赛试题浅析 

## 周世龙

(武汉大学, 430079)

2020 年第 81 届普特南数学竞赛因疫情延期, 最终于北京时间 2021 年 2 月 21 日在线上举行, 面向美国高校开放. 形式与往年相同, 试题分 $A, B$ 两组, 每组各 6 题, 规定时间各为三小时.

总体来看, 本次试题难度适中, 但计算量大, 对书写有一定要求. 题目大多较为初等, 相比往年分析的比例略有提升, 且没有出现线性代数题. 总体来说,是较好的训练素材.

本文旨在给出全部题目尽量忠实的翻译和 (一种) 解题方法, 供读者参考.由于笔者水平有限, 若文章中存在疏漏之处, 恳请读者指正!

## I. 试 题

A1. 有多少个正整数 $N$ 满足以下三个条件?

(i) $N$ 被 2020 整除;

(ii) $N$ 的十进制表示有至多 2020 位;

(iii) $N$ 的十进制表示是由一串 1 后接一串 0 构成的.

A2. 设 $k$ 为一非负整数. 求

$$
\sum_{j=0}^{k} 2^{k-j}\left(\begin{array}{c}
k+j \\
j
\end{array}\right)
$$

A3. 设 $a_{0}=\frac{\pi}{2}$, 并令 $a_{n}=\sin \left(a_{n-1}\right), n \geq 1$. 确定 $\sum_{n=1}^{\infty} a_{n}^{2}$ 是否收玫.

A4. 考虑一画有 $N+2$ 个方格的水平条带, 其中首尾两个方格涂黑, 其余方格仍为白色. 随机地选取一白色方格, 并等概率地选取该方格的一个相邻格,若它不是黑色则将它涂黑. 重复这一过程, 直至所有剩余白色方格的相邻方格都为黑色. 令 $w(N)$ 表示剩余白色方格数量的数学期望, 求 $\lim _{N \rightarrow \infty} \frac{w(N)}{N}$.

修订日期: 2021-03-10.

A5. 设 $a_{n}$ 为满足 $\sum_{k \in S} F_{k}=n$ 的正整数集 $S$ 的数量, 这里 $\left(F_{k}\right)_{k \geq 1}$ 为 Fibonacci 数列, 满足 $F_{k+2}=F_{k+1}+F_{k}$, 初值为 $F_{1}=1, F_{2}=1, F_{3}=2, F_{4}=3$.求使得 $a_{n}=2020$ 的最大正整数 $n$.

A6. 对于某一正整数 $N$, 函数 $f_{n}$ 定义如下:

$$
f_{N}(x)=\sum_{n=0}^{N} \frac{N+\frac{1}{2}-n}{(N+1)(2 n+1)} \sin (2 n+1) x .
$$

求使得 $f_{N}(x) \leq M$ 对于所有 $N$ 和所有实数 $x$ 成立的最小常数 $M$.

B1. 对于正整数 $n$, 定义 $d(n)$ 为 $n$ 的二进制表示下的数字和 (例如, $d(13)=$ $1+1+0+1=3)$. 令

$$
S=\sum_{k=1}^{2020}(-1)^{d(k)} k^{3}
$$

求 $S$ 模 2020 的值.

B2. 设 $k, n$ 为满足 $1 \leq k<n$ 的整数. Alice 和 Bob 玩一个游戏: 在一条直线上排有 $n$ 个洞, 这些洞中有 $k$ 个塞子. 在游戏的开始, 塞子位于最左边的 $k$ 个洞. 一次合法的移动指将某塞子移至其右端的某个空洞中. 两玩家交替移动, 由 Alice 开始. 当塞子被挪动至最右边 $k$ 个洞时游戏结束, 此时不能进行下一次移动的玩家输掉游戏. 对于哪些 $n$ 和 $k$ 的值, Alice 有必胜策略?

B3. 令 $x_{0}=1, \delta$ 为某一满足 $0<\delta<1$ 的常数. 递归地, 对于 $n=$ $0,1,2, \cdots, x_{n+1}$ 从区间 $\left[0, x_{n}\right]$ 中随机取出, 令 $Z$ 为使得 $x_{n}<\delta$ 的最小正整数值.将 $Z$ 的数学期望表示为 $\delta$ 的函数 (注: 这里的 “随机取出” 是指 $x_{n+1} \sim U\left[0, x_{n}\right]$ ).

B4. $n$ 为某一正整数, 并用 $V_{n}$ 表示 $(2 n+1)$ 维数组 $\mathbf{v}=\left(s_{0}, s_{1}, \cdots, s_{2 n-1}, s_{2 n}\right)$组成的集合, 其中 $s_{0}=s_{2 n}=0$, 并且 $\left|s_{j}-s_{j-1}\right|=1$ 对 $j=1,2, \cdots, 2 n$ 成立. 定义

$$
q(\mathbf{v})=1+\sum_{j=1}^{2 n-1} 3^{s_{j}}
$$

并设 $M(n)$ 为 $\frac{1}{q(\mathbf{v})}$ 的均值, 这里 $\mathbf{v} \in V_{n}$. 计算 $M(2020)$.

B5. 对于 $j \in\{1,2,3,4\}$, 令 $z_{j}$ 为满足 $\left|z_{j}\right|=1$ 且 $z_{j} \neq 1$ 的复数. 证明

$$
3-z_{1}-z_{2}-z_{3}-z_{4}+z_{1} z_{2} z_{3} z_{4} \neq 0
$$

B6. 令 $n$ 为一正整数. 证明

$$
\sum_{k=1}^{n}(-1)^{\lfloor k(\sqrt{2}-1)\rfloor} \geq 0
$$

其中, $\lfloor x\rfloor$ 表示不小于 $x$ 的最小整数.

## II. 解答与评注

A1. 有多少个正整数 $N$ 满足以下三个条件?

(i) $N$ 被 2020 整除;

(ii) $N$ 的十进制表示有至多 2020 位;

（iii） $N$ 的十进制表示是由一串 1 后接一串 0 构成的.

解 满足条件的正整数 $N$ 有 $504 \times 1009$ 个.

由条件(iii), 设某一满足题目要求的正整数为 $N=\overbrace{11 \cdots 1}^{x \text { 个 }} \overbrace{00 \cdots 0}^{y \text { 个 }}$.

从条件来看, (i) $\Leftrightarrow 20 \mid N$ 且 $101 \mid N$.

显然 $20 \mid N \Leftrightarrow y \geq 2$; 而 $101|N \Leftrightarrow 4| x$. 下面对此稍作说明.

注意到 $(10,101)=1$, 故 $N$ 是否被 101 整除取决于 $x$; 而 $1111=101 \times 11$,故当 $4 \mid x$ 时, 由于 $1111|\overbrace{11 \cdots 1}^{x \text { 个 }} \Rightarrow 101| N$.

另外, 注意到若 4 不整除 $x$ 或 $y<2$, 则 $N$ 不能被 2020 整除.

而条件(ii) $\Leftrightarrow x+y \leq 2020$. 至此我们完成了条件的等价转换.

下面开始求解. 令 $n$ 表示满足条件的正整数 $N$ 的个数, 并令

$$
n_{x}:=\#\{N \mid N \text { 形如 } \overbrace{11 \cdots 1}^{x \text { 个 }} \overbrace{00 \cdots 0}^{y \text { 个 }}, y \geq 2\},
$$

则

$$
n_{x}=2020-(x+2)+1=2019-x \text {. }
$$

从而

$$
n=\sum_{\substack{4 \mid x \\ 0<x<2020}}(2019-x)=\sum_{k=1}^{504}(2019-4 k)=504 \times 1009
$$

评注 较为简单的一道小题, 注意计算上不要出错.

A2. 设 $k$ 为一非负整数. 求

$$
\sum_{j=0}^{k} 2^{k-j}\left(\begin{array}{c}
k+j \\
j
\end{array}\right)
$$

解 该表达式的值为 $4^{k}$.

令

$$
S_{k}:=\sum_{j=0}^{k} 2^{k-j}\left(\begin{array}{c}
k+j \\
j
\end{array}\right)
$$

并规定 $\left(\begin{array}{c}n \\ -1\end{array}\right)=0, \forall n \in \mathbb{N}^{*}$.
利用熟知的恒等式 $\left(\begin{array}{l}n \\ k\end{array}\right)=\left(\begin{array}{c}n-1 \\ k\end{array}\right)+\left(\begin{array}{c}n-1 \\ k-1\end{array}\right)$, 我们可以得到

$$
\begin{aligned}
S_{k} & =\sum_{j=0}^{k} 2^{k-j}\left(\left(\begin{array}{c}
k+j-1 \\
j
\end{array}\right)+\left(\begin{array}{c}
k+j-1 \\
j-1
\end{array}\right)\right) \\
& =\sum_{j=0}^{k} 2^{k-j}\left(\begin{array}{c}
k+j-1 \\
j
\end{array}\right)+\sum_{j=1}^{k} 2^{k-j}\left(\begin{array}{c}
k+j-1 \\
j-1
\end{array}\right) \\
& =2 \sum_{j=0}^{k-1} 2^{k-1-j}\left(\begin{array}{c}
k-1+j \\
j
\end{array}\right)+\left(\begin{array}{c}
2 k-1 \\
k
\end{array}\right)+\sum_{j=0}^{k-1} 2^{k-1-j}\left(\begin{array}{c}
k+j \\
j
\end{array}\right) \\
& =2 S_{k-1}+\left(\begin{array}{c}
2 k-1 \\
k-1
\end{array}\right)+\frac{1}{2} \sum_{j=0}^{k-1} 2^{k-j}\left(\begin{array}{c}
k+j \\
j
\end{array}\right) \\
& =2 S_{k-1}+\frac{1}{2}\left(\left(\begin{array}{c}
2 k \\
k
\end{array}\right)+\sum_{j=0}^{k-1} 2^{k-1-j}\left(\begin{array}{c}
k+j \\
j
\end{array}\right)\right) \\
& =2 S_{k-1}+\frac{1}{2} S_{k} .
\end{aligned}
$$

从而 $S_{k}=4 S_{k-1}, k \in \mathbb{N}^{*}$.

又注意到 $S_{0}=1$, 故 $S_{k}=4^{k}$.

评注 这是一个优雅的组合恒等式.

上面给出的做法是纯粹的代数运算. 需要指出的是, 该恒等式有较为简单的组合意义, 留给读者思考.

A3. 设 $a_{0}=\frac{\pi}{2}$, 并令 $a_{n}=\sin \left(a_{n-1}\right), n \geq 1$. 确定 $\sum_{n=1}^{\infty} a_{n}^{2}$ 是否收玫.

解 该数项级数发散.

首先注意到 $\lim _{n \rightarrow \infty} a_{n}=0$. 这是因为 $\left\{a_{n}\right\}$ 单调递减且有界, 故极限存在. 从而

$$
\lim _{n \rightarrow \infty} a_{n}=\lim _{n \rightarrow \infty} \sin a_{n-1}=\lim _{n \rightarrow \infty} \sin a_{n} \Rightarrow \lim _{n \rightarrow \infty} a_{n}=0 .
$$

我们下面来级数的一般项进行阶的估计.

引理 成立 $a_{n} \sim \sqrt{\frac{3}{n}}, n \rightarrow \infty$.

证明 由于数列 $\left\{a_{n}\right\}$ 以 0 为极限, 所以

$$
a_{n}=\sin a_{n-1}=a_{n-1}-\frac{1}{6} a_{n-1}^{3}+O\left(a_{n-1}^{5}\right), n \rightarrow \infty .
$$

对于 $\beta \in \mathbb{R}$, 注意到

$$
\begin{aligned}
a_{n}^{\beta}-a_{n-1}^{\beta} & =\sin ^{\beta} a_{n-1}-a_{n-1}^{\beta} \\
& =\left(a_{n-1}-\frac{1}{6} a_{n-1}^{3}+O\left(a_{n-1}^{5}\right)\right)^{\beta}-a_{n-1}^{\beta} \\
& =a_{n-1}^{\beta}\left(1-\frac{1}{6} a_{n-1}^{2}+O\left(a_{n-1}^{4}\right)\right)^{\beta}-a_{n-1}^{\beta}
\end{aligned}
$$

$$
=a_{n-1}^{\beta}\left(-\frac{\beta}{6} a_{n-1}^{2}+O\left(a_{n-1}^{4}\right)\right) .
$$

在上式中取 $\beta=-2$, 可以得到

$$
\begin{aligned}
a_{n}^{-2}-a_{n-1}^{-2} & =\frac{1}{3}+O\left(a_{n-1}^{2}\right)=\frac{1}{3}+o(1), n \rightarrow \infty \\
\Rightarrow \frac{1}{a_{n}^{2}} & =\sum_{k=1}^{n}\left(\frac{1}{a_{k}^{2}}-\frac{1}{a_{k-1}^{2}}\right)+\frac{1}{a_{0}^{2}}=\frac{1}{3} n+O\left(\sum_{k=1}^{n} a_{k-1}^{2}\right)+\frac{4}{\pi^{2}} \\
& =\frac{1}{3} n+\frac{4}{\pi^{2}}+o(n) \sim \frac{1}{3} n, n \rightarrow \infty .
\end{aligned}
$$

这就证明了引理.

而结合引理及比较审玫法, 显然 $a_{n}^{2}$ 与 $O\left(\frac{1}{n}\right)$ 同阶, 从而该数项级数发散.

评注 本题是一道有意思且难度中等的数学分析习题.

就笔者的视角看, 本题的关键在于对该级数发散有直观的认识. 在此基础上, 不论是如上直接对阶进行估计, 或是用归纳法证明存在一个一般项不超过 $a_{n}$ 的发散级数, 都是可行的.

A4. 考虑一画有 $N+2$ 个方格的水平条带, 其中首尾两个方格涂黑, 其余方格仍为白色. 随机地选取一白色方格, 并等概率地选取该方格的一个相邻格,若它不是黑色则将它涂黑. 重复这一过程, 直至所有剩余白色方格的相邻方格都为黑色. 令 $w(N)$ 表示剩余白色方格数量的数学期望, 求 $\lim _{N \rightarrow \infty} \frac{w(N)}{N}$.

解 该极限值为 $\frac{1}{e}$.

首先, 通过观察可以得到 $w(0)=0, w(1)=w(2)=1$. 下面来求 $w(n)$ 的递推式.

我们将初始的 $N$ 个白色方格从左至右依次编号 $1,2, \cdots, n$. 据题意, 不难分析当 $N \geq 3$ 时, 编号为 $1, N$ 的白色方格和两端的黑色方格被选中的概率均为 $\frac{1}{2 N}$, 其余方格被选中的概率为 $\frac{1}{N}$. 而选定编号为 $k(1 \leq k \leq N)$ 并涂黑后, 其左侧有 $k-1$ 个白色方格, 右侧有 $N-k$ 个白色方格.据此我们就能得到

$$
w(N+1)=\frac{w(N)}{2(N+1)} \times 2+\sum_{k=1}^{N-1} \frac{1}{N+1}(w(k)+w(N-k))+\frac{w(N+1)}{2(N+1)} \times 2 .
$$

上式经整理, 得到

$$
N w(N+1)=2 \sum_{k=1}^{N-1} w(k)+w(N), N \in \mathbb{N}^{*}
$$

用 $N-1$ 替 $N$, 并比较两式, 得到二阶递推:

$$
\begin{aligned}
N w(N+1) & =(N-1) w(N)-w(N-1)+2 w(N-1)+w(N) \\
& =N w(N)+w(N-1)
\end{aligned}
$$

整理得

$$
w(N+1)=w(N)+\frac{w(N-1)}{N}, N \in \mathbb{N}^{*}
$$

下面回到原题. 为求该极限, 我们考虑母函数

$$
f(z):=\sum_{n=1}^{\infty} \frac{w(n-1)}{n} z^{n}
$$

不难发现

$$
\begin{aligned}
f^{\prime}(z) & =\sum_{n=1}^{\infty} w(n-1) z^{n-1}=z+\sum_{n=3}^{\infty}\left(w(n-2)+\frac{w(n-3)}{n-2}\right) z^{n-1} \\
& =z\left(1+f^{\prime}(z)+f(z)\right) .
\end{aligned}
$$

解该微分方程, 得到

$$
f(z)=\frac{C}{e^{z}(1-z)}-1, C \in \mathbb{R}
$$

又由 $w(0)=0 \Rightarrow C=1$. 最后只需考察 $f(z)$ 的麦克劳林展开式, 立即得到

$$
\frac{w(N)}{N+1}=f^{(N+1)}(0)=\sum_{j=0}^{N+1} \frac{(-1)^{j}}{j !} \Rightarrow \lim _{N \rightarrow \infty} \frac{w(N)}{N+1}=\sum_{j=0}^{\infty} \frac{(-1)^{j}}{j !}=\frac{1}{e} .
$$

从而 $\lim _{N \rightarrow \infty} \frac{w(N)}{N}=\frac{1}{e}$, 即证.

评注 表面上是道概率论问题, 实际上建立递推式的过程是自然的, 麻烦的点还是求递推数列的极限.

这里利用母函数是直觉上较易想到的方法, 也是较为一般的手段. 也许有更简单的解法.

A5. 设 $a_{n}$ 为满足 $\sum_{k \in S} F_{k}=n$ 的正整数集 $S$ 的数量, 这里 $\left(F_{k}\right)_{k \geq 1}$ 为 Fibonacci 数列, 满足 $F_{k+2}=F_{k+1}+F_{k}$, 初值为 $F_{1}=1, F_{2}=1, F_{3}=2, F_{4}=3$.求使得 $a_{n}=2020$ 的最大正整数 $n$.

解 我们来说明, 最大的正整数 $n=F_{4040}-1$.

在开始证明前, 我们给出如下定理, 它有时也被称为 “Fibonacci 进制表示”.

定理 对于任意正整数 $n$, 存在唯一数集 $S \subset \mathbb{N}^{*}$, 使得 $n=\sum_{k \in S} F_{k}$, 其中 $S$中元素两两不相邻, 即 $\forall k_{1} \neq k_{2}, k_{1}, k_{2} \in S$, 必有 $\left|k_{1}-k_{2}\right| \geq 2$.

定理的证明概要如下:

存在性可由贪心算法导出. 对 $\forall n \in \mathbb{N}^{*}$, 记 $k_{1}:=\max \left\{k \in \mathbb{N}^{*} \mid F_{k} \leq n\right\}$, $n_{1}:=n-F_{k_{1}}$. 易见 $n_{1}<F_{k_{1}-1}$. 重复上述过程, 我们递归地得到数列 $\left\{k_{i}\right\}_{i=1}^{r}$.记 $S:=\left\{k_{i} \mid 1 \leq i \leq r\right\}$, 易验证 $S$ 符合我们的要求.
对于唯一性, 我们不妨假设存在两个数集 $S, S^{\prime}$, 使得 $n=\sum_{k \in S} F_{k}=\sum_{k \in S^{\prime}} F_{k}$.

考虑 $T_{1}:=S \backslash S^{\prime}, T_{2}:=S^{\prime} \backslash S$. 若 $T_{1}=\varnothing$, 由两集合元素和相等可以导出 $T_{2}=\varnothing$, 这说明 $S=S^{\prime}$; 否则不失一般性, 设 $\max T_{1}<\max T_{2}$, 我们用 $\sqcup$ 表示集合的无交并, 不难见得

$$
\sum_{k \in T_{1}} F_{k}<F_{\max T_{1}+1} \leq F_{\max T_{2}} \leq \sum_{k \in T_{2}} F_{k} .
$$

从而

$$
\sum_{k \in S} F_{k}=\sum_{k \in\left(S \cap S^{\prime}\right) \sqcup T_{1}} F_{k}<\sum_{k \in\left(S \cap S^{\prime}\right) \sqcup T_{2}} F_{k}=\sum_{k \in S^{\prime}} F_{k}
$$

立得矛盾, 从而唯一性得证, 定理证毕.

由上述定理保证, 对任意正整数 $n$, 我们有如下表示: $n:=\left(\overline{b_{k} b_{k-1} \cdots b_{2}}\right)_{F}$,其中 $b_{i} \in\{0,1\}, 2 \leq i \leq k, b_{k}=1$, 且相邻两项不同时为 1 .

下面的引理是本题的关键性结论.

引理 设 $n=\left(\overline{b_{k} b_{k-1} \cdots b_{2}}\right)_{F}$, 其中 $b_{k}=1$, 则成立 $a_{n} \geq a_{F_{k}}=\left[\frac{k}{2}\right]+1$.

证明 对 $k$ 用数学归纳法. $k=2,3,4,5$ 的情形是成立的, 只需对 $n=$ $1,2, \cdots, 12$ 分别验证引理即可.

对 $\forall \tilde{n}=\left(\overline{b_{k} b_{k-1} \cdots b_{2}}\right)_{F}$, 假定 $a_{\tilde{n}} \geq\left[\frac{k}{2}\right]+1$.

下考虑 $n=\left(\overline{c_{k+2} c_{k+1} \cdots c_{2}}\right)_{F}$, 其中 $c_{k+2}=1$, 我们来说明

$$
a_{n} \geq\left[\frac{k+2}{2}\right]+1=\left[\frac{k}{2}\right]+2 .
$$

我们来对 $c_{k}$ 进行分类讨论.

(i) 若 $c_{k}=1$, 则 $n=c_{k+2} F_{k+2}+\tilde{n}, \tilde{n}:=\left(\overline{c_{k} \cdots c_{2}}\right)_{F}$.

由归纳假设知 $a_{\tilde{n}} \geq\left[\frac{k}{2}\right]+1$.

另外, 注意到当 $n \geq 4$ 时, 存在数集 $S \subset\{1,2, \cdots, k\}, \tilde{n}=\sum_{j \in S} F_{j}$, 且 $k \notin S$. (这一结论不难说明, 留给读者)

从而

$$
n=\sum_{j \in S \cup\{k+2\}} F_{j}=\sum_{j \in S \cup\{k, k+1\}} F_{j} .
$$

这给出了 $n$ 的另一种分解方法, 因此有 $a_{n} \geq a_{\tilde{n}}+1=\left[\frac{k}{2}\right]+2$.

(ii) 若 $c_{k}=0$, 不妨设 $t:=\max \left\{s \in \mathbb{N}^{*} \mid s \leq k-1, c_{s}=1\right\}, \tilde{n}$ 意义同上,则 $n=c_{k+2} F_{k+2}+\tilde{n}$.

于是 $F_{k+2}$ 可分解为

$$
\sum_{\substack{t_{i} \text { 互异 } \\ t_{i}>t}} F_{t_{i}} .
$$

这样的分解方式有 $\left[\frac{k+1-t}{2}\right]+1$ 种, 结合 $t \leq k-1 \Rightarrow\left[\frac{k+1-t}{2}\right]+1 \geq 2$.

由归纳假设, $a_{\tilde{n}} \geq\left[\frac{t}{2}\right]+1 \geq 2$.

当 $\left(\left[\frac{k+1-t}{2}\right]+1,\left[\frac{t}{2}\right]+1\right) \neq(2,2)$ 时, 我们有

$a_{n} \geq\left(\left[\frac{t}{2}\right]+1\right)\left(\left[\frac{t}{2}\right]+1\right) \geq\left[\frac{k+1-t}{2}\right]+1+\left[\frac{t}{2}\right]+1+1 \geq\left[\frac{k}{2}\right]+2$.

而注意到

$$
\left(\left[\frac{k+1-t}{2}\right]+1,\left[\frac{t}{2}\right]+1\right)=(2,2) \Rightarrow k \leq 5
$$

这些情形已经在归纳假设中被验证成立. 故归纳完毕, 引理得证.

回到原题, 结合引理知满足题意的 $n$ 一定不超过 $F_{4040}-1$. 最后只需说明 $a_{F_{4040}-1}=2020$. 这部分没有本质困难, 交由读者验证.

评注 这是一道思维难度不高, 但很考验书写的题目。

“Fibonacci 进制”是竞赛试题中出现频率较高的题材之一, 对此较为熟悉的读者经过摸索可以很快地得到引理的结论, 但证明它需要处理不少的细节.

A6. 对于某一正整数 $N$, 函数 $f_{n}$ 定义如下:

$$
f_{N}(x)=\sum_{n=0}^{N} \frac{N+\frac{1}{2}-n}{(N+1)(2 n+1)} \sin (2 n+1) x .
$$

求使得 $f_{N}(x) \leq M$ 对于所有 $N$ 和所有实数 $x$ 成立的最小常数 $M$.

解 最小常数 $M=\frac{\pi}{4}$.

首先, 不妨设 $x \in[0,2 \pi]$.

作为引理, 我们给出如下(熟知的)和式.

引理 1 对 $\forall N \in \mathbb{N}^{*}$, 恒成立如下和式:

$$
\begin{aligned}
& \sum_{n=0}^{N} \cos (2 n+1) x=\frac{\sin (2 N+2) x}{2 \sin x} \\
& \sum_{n=0}^{N} \sin (2 n+1) x=\frac{1-\cos (2 N+2) x}{2 \sin x}
\end{aligned}
$$

证明是容易的, 等式两端同乘 $2 \sin x$ 后积化和差即可.

对于题目给出的函数 $f_{N}$, 我们有如下两个结论:

引理 2 成立 $f_{N}(x) \leq f_{N}\left(\frac{\pi}{2}\right), \forall x \in[0,2 \pi]$.

证明 首先, 我们对 $f_{N}$ 进行如下的代数变形:

$$
\begin{aligned}
f_{N}(x) & =\sum_{n=0}^{N} \frac{(N+1)-\left(n+\frac{1}{2}\right)}{(N+1)(2 n+1)} \sin ((2 n+1) x) \\
& =\sum_{n=0}^{N}\left(\frac{1}{2 n+1}-\frac{1}{2(N+1)}\right) \sin ((2 n+1) x) .
\end{aligned}
$$

求导, 得 (结合引理 1 )

$$
\begin{aligned}
f_{N}^{\prime}(x) & =\sum_{n=0}^{N} \cos ((2 n+1) x)-\frac{1}{2(N+1)} \sum_{n=0}^{N}(2 n+1) \cos ((2 n+1) x) \\
& =\frac{\sin ((2 N+2) x)}{2 \sin x}-\frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{1}{2(N+1)} \sum_{n=0}^{N} \sin ((2 n+1) x)\right) \\
& =\frac{\sin ((2 N+2) x)}{2 \sin x}-\frac{(2 N+2) \sin x \sin ((2 N+2) x)-(1-\cos ((2 N+2) x)) \cos x}{4(N+1) \sin ^{2} x} \\
& =\frac{(1-\cos (2 N+2) x) \cos x}{4(N+1) \sin ^{2} x} .
\end{aligned}
$$

$(* *)$ 式虽然有多个导零点, 但经观察可以得知 $f^{\prime}$ 的正负性由 $\cos x$ 确定, 亦

即

$$
\operatorname{sgn}\left(f_{N}^{\prime}(x)\right)=\operatorname{sgn}(\cos x)
$$

从而可以立即得到 $f_{N}$ 在 $[0,2 \pi]$ 上存在唯一极大值点 $x=\frac{\pi}{2}$.

故 $f_{N}(x) \leq f_{N}\left(\frac{\pi}{2}\right)$, 引理 2 得证.

引理 3 成立 $f_{N}\left(\frac{\pi}{2}\right) \leq f_{N+2}\left(\frac{\pi}{2}\right), \forall N \in \mathbb{N}^{*}$.

证明 由于

$$
\begin{aligned}
f_{N}\left(\frac{\pi}{2}\right) & =\sum_{n=0}^{N}(-1)^{n}\left(\frac{1}{2 n+1}-\frac{1}{2(N+1)}\right) \\
& =\sum_{n=0}^{N}(-1)^{n} \frac{1}{2 n+1}-\frac{1}{2(N+1)}-\frac{1}{2(N+1)} \mathbf{1}_{\{2 \mid N\}} .
\end{aligned}
$$

其中 $1_{X}$ 为集合 $X$ 的示性函数.

至此只需对 $N$ 的奇偶性进行讨论即可.

(i) 若 $N$ 为奇数, 则

$$
f_{N+2}\left(\frac{\pi}{2}\right)-f_{N}\left(\frac{\pi}{2}\right)=\frac{1}{2 N+3}-\frac{1}{2 N+5}>0 ;
$$

(ii) 若 $N$ 为偶数, 则

$$
f_{N+2}\left(\frac{\pi}{2}\right)-f_{N}\left(\frac{\pi}{2}\right)=\frac{1}{2 N+5}-\frac{1}{2 N+3}-\frac{1}{2 N+6}+\frac{1}{2 N+2}>0 .
$$

得证.

回到原题. 结合上述两引理, 直接可以得到

$$
\begin{aligned}
f_{N}(x) & \leq f_{N}\left(\frac{\pi}{2}\right) \leq \lim _{N \rightarrow \infty} f_{N}\left(\frac{\pi}{2}\right)=\sum_{n=0}^{\infty}(-1)^{n} \frac{1}{2 n+1} \\
& =\left.\arctan x\right|_{x=1}=\frac{\pi}{4}, \forall N \in \mathbb{N}^{*}, x \in[0,2 \pi] .
\end{aligned}
$$

通过上述讨论, 可见最小常数为 $M=\frac{\pi}{4}$.

评注 面对此题, 给人的第一感觉是 $f_{N}$ 的形式较为复杂. 好在很容易发
现 $f_{N}$ 可以做代数变形 (即 $(*)$ 式).

本题的难点在于 $f_{N}^{\prime}(x)$ 有多个零点, 从而难以讨论极大值点. 我们用引理 2 避开了这一困难, 之后的讨论就水到渠成了.

另外， $f_{N}$ 的形式容易让人猜测是否与 Fourier 分析有关. 其实读者也可以发现 $\lim _{N \rightarrow \infty} f_{N}\left(\frac{\pi}{2}\right)$ 其实是某一方波函数的 Fourier 级数, 具体可参见 $[1]$.

B1. 对于正整数 $n$, 定义 $d(n)$ 为 $n$ 的二进制表示下的数字和 (例如, $d(13)=$ $1+1+0+1=3)$. 令

$$
S=\sum_{k=1}^{2020}(-1)^{d(k)} k^{3}
$$

求 $S$ 模 2020 的值.

解 $S \equiv 1990(\bmod 2020)$.

我们定义 $f(k):=(-1)^{d(k)} k^{3}$. 来证明一关键结论:

引理 成立

$$
\sum_{n=16 k}^{16 k+15} f(k)=0, \forall k \in \mathbb{N}
$$

证明 注意到, $\forall k \in \mathbb{N}$,

$$
\begin{aligned}
f(16 k)+f(16 k+1) & =(-1)^{d(16 k)}\left((16 k)^{3}-(16 k+1)^{3}\right) \\
& =(-1)^{d(16 k)}-\left(768 k^{2}+48 k+1\right)
\end{aligned}
$$

同理可以计算得到

$$
\begin{aligned}
& f(16 k+2)+f(16 k+3)=(-1)^{d(16 k)}\left(768 k^{2}+240 k+19\right) \\
& f(16 k+4)+f(16 k+5)=(-1)^{d(16 k)}\left(768 k^{2}+432 k+61\right) \\
& f(16 k+6)+f(16 k+7)=(-1)^{d(16 k)}-\left(768 k^{2}+624 k+127\right)
\end{aligned}
$$

因此

$$
\sum_{n=16 k}^{16 k+7} f(k)=(-1)^{d(16 k)}-48
$$

同理可验证

$$
\sum_{n=16 k+8}^{16 k+15} f(k)=(-1)^{d(16 k)} 48
$$

故确有 $\sum_{n=16 k}^{16 k+15} f(k)=0$, 引理得证.

回到原题, 可见

$$
S=\sum_{n=1}^{2020} f(n)=\sum_{n=0}^{2020} f(n)=\sum_{n=0}^{2015} f(n)+\sum_{n=2016}^{2020} f(n)
$$

$$
\begin{aligned}
& =\sum_{k=0}^{125} \sum_{n=16 k}^{16 k+15} f(n)+\sum_{n=2016}^{2020} f(n)=\sum_{n=2016}^{2020} f(n) \\
& \equiv(-4)^{3}-(-3)^{3}-(-2)^{3}+(-1)^{3}=-30 \equiv 1990 \quad(\bmod 2020)
\end{aligned}
$$

评注 看起来有点吓人的题目, $d(k)$ 的定义让人一时不知怎么处理.

不过稍作尝试后就不难注意到, $(-1)^{d(n)}$ 有较为规律的正负交错的特性, 从而考虑某些项求和后是否为常数, 问题至此也就基本解决了.

B2. 设 $k, n$ 为满足 $1 \leq k<n$ 的整数. Alice 和 Bob 玩一个游戏: 在一条直线上排有 $n$ 个洞, 这些洞中有 $k$ 个塞子. 在游戏的开始, 塞子位于最左边的 $k$ 个洞. 一次合法的移动指将某塞子移至其右端的某个空洞中. 两玩家交替移动，由 Alice 开始.当塞子被挪动至最右边 $k$ 个洞时游戏结束, 此时不能进行下一次移动的玩家输掉游戏. 对于哪些 $n$ 和 $k$ 的值, Alice 有必胜策略?

解 我们来说明: 当且仅当 $k, n$ 不全为偶数时, Alice 有必胜策略.

为叙述简便，做如下简化：将 $n$ 个洞从左到右分别用编号 $1,2, \cdots, n$ 代指;将 Alice 称为 A, Bob 称为 B; 对于 $k$ 个塞子, $n$ 个洞的游戏, 用二元数组 $(k, n)$代指; 另外, 我们用 $i \mapsto j$ 表示将 $i$ 处塞子移至 $j$ 的一次操作, 其中 $j$ 处在操作前没有塞子(要求 $i<j$ ).

先对 $(k, n)$ 均为偶数的情形进行讨论, 用引理的形式呈现如下.

引理 当 $k, n$ 均为偶数时, B 有必胜策略.

证明 记 $T_{i}:=\{2 i-1,2 i\}, 1 \leq i \leq \frac{n}{2}$. 对于 $\forall x \in T_{i}$, 我们记 $\bar{x}$ 为 $T_{i}$ 中另一元素.

$\mathrm{B}$ 的策略如下: $\mathrm{A}$ 进行操作 $x \in T_{i} \mapsto y \in T_{j}$ 时, $\mathrm{B}$ 进行操作 $\bar{x} \mapsto \bar{y}$. 这一操作总是合法的 (读者可自行验证). 因此 $\mathrm{B}$ 总能在 $\mathrm{A}$ 后相应地走一步, 从而 $\mathrm{B}$ 依据上述策略必胜, 引理得证.

下面只需说明, 当 $k, n$ 不全为偶数时, $\mathrm{A}$ 有必胜策略.分情况讨论如下:

(i) $k$ 为偶数, $n$ 为奇数: $\mathrm{A}$ 取第一步操作为 $1 \mapsto k+1$, 不难看出经这一步后, 可以认为此时游戏变为 $(k, n-1)$ 情形, 此时 $\mathrm{A}$ 为后手;

(ii) $k$ 为偶数, $n$ 为奇数: $\mathrm{A}$ 取第一步操作为 $k \mapsto n$, 不难看出经这一步后,可以认为此时游戏变为 $(k-1, n-1)$ 情形, 此时 $\mathrm{A}$ 为后手;

(iii) $k$ 为偶数, $n$ 为奇数: $\mathrm{A}$ 取第一步操作为 $1 \mapsto n$, 不难看出经这一步后,可以认为此时游戏变为 $(k-1, n-2)$ 情形, 此时 $\mathrm{A}$ 为后手;
以上三种情形覆盖了所有情况, 且据引理知这三种情形 $\mathrm{A}$ 均有必胜策略.

综合以上讨论, 我们完成了证明.

评注 必胜策略问题, 经过对 $k, n$ 较小情形的尝试后, 不难发现 $\mathrm{A}$ 是否有必胜策略与 $k, n$ 的奇偶性相关.

$k, n$ 均为偶数时运用的配对想法是很标准的，而其他的情况可以化归为上述情形, 从而使问题得到解决.

B3. 令 $x_{0}=1, \delta$ 为某一满足 $0<\delta<1$ 的常数. 递归地, 对于 $n=$ $0,1,2, \cdots, x_{n+1}$ 从区间 $\left[0, x_{n}\right]$ 中随机取出, 令 $Z$ 为使得 $x_{n}<\delta$ 的最小正整数值.将 $Z$ 的数学期望表示为 $\delta$ 的函数 (注: 这里的 “随机取出” 是指 $x_{n+1} \sim U\left[0, x_{n}\right]$ ).

解 $E(Z)=1-\ln \delta$. 下面给出求解过程.

易由题意得到 $P(Z=1)=\delta$. 对于 $k \geq 2$, 我们有

$$
P(Z=k)=\int_{\delta}^{1} \mathrm{~d} x_{1} \int_{\delta}^{x_{1}} \mathrm{~d} x_{2} \cdots \int_{\delta}^{x_{k-2}} \mathrm{~d} x_{k-1} \int_{0}^{\delta} f\left(x_{1}, \cdots, x_{k}\right) \mathrm{d} x_{k},
$$

其中 $f\left(x_{1}, \cdots, x_{k}\right)$ 为随机变量 $\left(x_{1}, \cdots, x_{k}\right)$ 的联合概率密度.

事实上, 不难注意到 $f\left(x_{1}, \cdots, x_{k}\right)=\frac{1}{x_{1} x_{2} \cdots x_{k-1}}$. 整理得

$$
P(Z=k)=\delta \int_{\delta}^{1} \frac{\mathrm{d} x_{1}}{x_{1}} \int_{\delta}^{x_{1}} \frac{\mathrm{d} x_{2}}{x_{2}} \cdots \int_{\delta}^{x_{k-2}} \frac{\mathrm{d} x_{k-1}}{x_{k-1}} .
$$

下面求积分. 我们用数学归纳法证明

$$
P(Z=k)=\frac{\delta \ln ^{k-1} \frac{1}{\delta}}{(k-1) !}, \forall k \in \mathbb{N}^{*}
$$

$k=1$ 的情形已经证明. 设命题对 $\leq k$ 的情形均成立, 则 $k+1$ 时

$$
\begin{aligned}
P(Z=k+1) & =\delta \int_{\delta}^{1} \frac{\mathrm{d} x_{1}}{x_{1}} \int_{\delta}^{x_{1}} \frac{\mathrm{d} x_{2}}{x_{2}} \cdots \int_{\delta}^{x_{k-2}} \frac{\mathrm{d} x_{k-1}}{x_{k-1}} \int_{\delta}^{x_{k-1}} \frac{\mathrm{d} x_{k}}{x_{k}} \\
& =\delta \int_{\delta}^{1} \frac{\mathrm{d} x_{1}}{x_{1}} \int_{\delta}^{x_{1}} \frac{\mathrm{d} x_{2}}{x_{2}} \cdots \int_{\delta}^{x_{k-2}} \frac{\mathrm{d} x_{k-1}}{x_{k-1}}\left(\ln x_{k-1}-\ln \delta\right) \\
& \left.=\delta \int_{\delta}^{1} \frac{\mathrm{d} x_{1}}{x_{1}} \int_{\delta}^{x_{1}} \frac{\mathrm{d} x_{2}}{x_{2}} \cdots \int_{\delta}^{x_{k-2}} \frac{\ln x_{k-1} \mathrm{~d} x_{k-1}}{x_{k-1}}+\frac{\delta \ln ^{k} \frac{1}{\delta}}{(k-1) !}+\frac{(-1)^{k-2}}{(k-1) ! 1 !}+\frac{(-1)^{k-1}}{0 ! k !}\right) \\
& =\cdots \ln ^{k} \frac{1}{\delta}\left(\frac{1}{1 !(k-1) !}+\cdots+\frac{\delta \ln ^{k} \frac{1}{\delta}}{k !} .\right. \\
& =\frac{\delta \ln ^{k} \frac{1}{\delta}}{k !} \sum_{j=1}^{k}\left(\begin{array}{l}
k \\
j
\end{array}\right)(-1)^{j}=\frac{\delta \ln ^{k} \frac{1}{\delta}}{k !} \times 1=\frac{1}{k !}
\end{aligned}
$$

标! 的等式用到了归纳假设. 从而归纳完毕.

回到原题.注意到

$$
E(Z)=\sum_{k=1}^{\infty} k P(Z=k)=\delta \sum_{k=1}^{\infty} k \frac{\delta \ln ^{k} \frac{1}{\delta}}{(k-1) !}
$$

$$
\begin{aligned}
& =\delta\left(\sum_{k=2}^{\infty} \frac{\delta \ln ^{k} \frac{1}{\delta}}{(k-2) !}+\sum_{k=1}^{\infty} \frac{\delta \ln ^{k} \frac{1}{\delta}}{(k-1) !}\right) \\
& =\delta \times \frac{1}{\delta}\left(1+\ln \frac{1}{\delta}\right)=1+\ln \frac{1}{\delta}=1-\ln \delta .
\end{aligned}
$$

评注 这是一道比较标准的概率论习题.

只要对多维随机向量的分布函数有正确的认识, 列出积分式都是不困难的,较为欶手的事情仍然是计算, 这也是本届试题的一个特点.

B4. $n$ 为某一正整数, 并用 $V_{n}$ 表示 $(2 n+1)$ 维数组 $\mathbf{v}=\left(s_{0}, s_{1}, \cdots, s_{2 n-1}, s_{2 n}\right)$组成的集合, 其中 $s_{0}=s_{2 n}=0$, 并且 $\left|s_{j}-s_{j-1}\right|=1$ 对 $j=1,2, \cdots, 2 n$ 成立. 定义

$$
q(\mathbf{v})=1+\sum_{j=1}^{2 n-1} 3^{s_{j}}
$$

并设 $M(n)$ 为 $\frac{1}{q(\mathbf{v})}$ 的均值, 这里 $\mathbf{v} \in V_{n}$. 计算 $M(2020)$.

解 $M(2020)=\frac{1}{4040}$.

对 $S \ni \mathbf{v}:=\left(s_{0}, \cdots, s_{2 n}\right)$ (注: 下文中 $\mathbf{v}$ 的定义相同), 定义 $\tilde{\mathbf{v}}:=\left(s_{0}, \cdots, s_{2 n-1}\right)$.

我们考虑二元关系 $\sim: \mathbf{v} \sim \mathbf{v}_{\mathbf{i}}$ 当且仅当存在 $0 \leq t \leq 2 n-1$, 使得

$$
\tilde{\mathbf{v}}_{\mathbf{i}}=\left(0, s_{t+1}-s_{t}, \cdots, s_{t+2 n-1}-s_{t}\right),
$$

其中下标按 $\bmod 2 n$ 理解.

容易验证 $\sim$ 是等价关系, 此处不再赘述.

从而考虑陪集族 $V_{n} / \sim=:\left\{\overline{\mathbf{v}_{\mathbf{1}}}, \cdots, \overline{\mathbf{v}_{\mathbf{r}}}\right\}$, 其中 $\mathbf{v}_{\mathbf{j}} \in \overline{\mathbf{v}_{\mathbf{j}}}, \forall 1 \leq j \leq r$.

我们来说明 $\overline{\mathbf{v}_{\mathbf{j}}}$ 中 $\frac{1}{q(\mathbf{v})}$ 的均值 (记为 $\left.M_{j}(\mathbf{v})\right)$ 为 $\frac{1}{2 n}, \forall 1 \leq j \leq r$.

为此, 不妨记 $\# \overline{\mathbf{v}_{\mathbf{j}}}=: k$, 这说明 $\mathbf{v}_{\mathbf{j}}=:\left(s_{j, 0}, \cdots, s_{j, 2 n}\right)$ 有长度为 $k$ 的循环节,从而

$$
\begin{aligned}
M_{j}(\mathbf{v}) & =\frac{1}{k} \sum_{\mathbf{v} \in \overline{\mathbf{v}}_{\mathbf{j}}} \frac{1}{q(\mathbf{v})}=\frac{1}{k} \sum_{\mathbf{v} \in \overline{\mathbf{v}_{\mathbf{j}}}} \frac{1}{1+\sum_{i=1}^{2 n-1} 3^{s_{i}}} \\
& =\frac{1}{k} \sum_{l=0}^{k-1} \frac{1}{\left(1+\sum_{i=1}^{2 n-1} 3^{s_{j, i}}\right) 3^{-s_{j, l}}}=\frac{1}{k} \sum_{l=0}^{k-1} \frac{3^{s_{j, l}}}{1+\sum_{i=1}^{2 n-1} 3^{s_{j, i}}} \\
& =\frac{1}{k} \frac{k}{2 n}=\frac{1}{2 n}, \forall 1 \leq j \leq r
\end{aligned}
$$

故显然有 $M(n)=\frac{1}{2 n}, \forall n \in \mathbb{N}^{*}$.

代入 $n=2020$, 即知 $M(n)=\frac{1}{4040}$.
评注 这是一道比较有趣的题目.

从本题的目标(求均值)来看, 我们自然会思考：能否将 $V_{n}$ 分为若干个子集,使得每一个都易求均值? 这样的想法将我们引向集合的分划, 进一步地, 自然会考虑用等价关系分划该集合。

基于以上思路进行完善, 就有了上述方案.

B5. 对于 $j \in\{1,2,3,4\}$, 令 $z_{j}$ 为满足 $\left|z_{j}\right|=1$ 且 $z_{j} \neq 1$ 的复数. 证明

$$
3-z_{1}-z_{2}-z_{3}-z_{4}+z_{1} z_{2} z_{3} z_{4} \neq 0 .
$$

证明 我们先证明如下引理:

引理 设复数 $z_{j}(1 \leq j \leq 3)$ 满足 $\left|z_{j}\right|=1$, 则如下的不等式恒成立:

$$
\left|z_{1} z_{2} z_{3}-1\right| \leq\left|z_{1}+z_{2}+z_{3}-3\right| .
$$

并且等号成立当且仅当存在某个 $1 \leq k \leq 3$ 使得 $z_{k}=1$.

证明 不妨 $z_{j}=\cos \theta_{j}+\mathrm{i} \sin \theta_{j}, \theta_{j} \in[0,2 \pi], 1 \leq j \leq 3$, 从而

$$
\begin{aligned}
& \left|z_{1}+z_{2}+z_{3}-3\right|-\left|z_{1} z_{2} z_{3}-1\right| \\
= & \sum_{j=1}^{3}\left(\left(\cos \theta_{j}-1\right)^{2}+\sin ^{2} \theta_{j}\right)-\left(\cos \left(\sum_{j=1}^{3} \theta_{j}\right)-1\right)^{2}-\sin ^{2}\left(\sum_{j=1}^{3} \theta_{j}\right) \\
= & 4-2 \sum_{j=1}^{3} \cos \theta_{j}+\cos \left(\sum_{j=1}^{3} \theta_{j}\right)=: f\left(\theta_{1}, \theta_{2}, \theta_{3}\right) .
\end{aligned}
$$

此时连续函数 $f$ 定义在紧集 $[0,2 \pi]^{3}$ 上, 从而存在最小值. 下面只需说明该函数最小值为 0 , 且最小值一定在边界上取到. 为此, 注意到

$\nabla f\left(\theta_{1}, \theta_{2}, \theta_{3}\right)=\left(2 \sin \theta_{1}-\sin \left(\sum \theta_{j}\right), 2 \sin \theta_{2}-\sin \left(\sum \theta_{j}\right), 2 \sin \theta_{3}-\sin \left(\sum \theta_{j}\right)\right)$.

故

$$
\nabla f\left(\theta_{1}, \theta_{2}, \theta_{3}\right)=0 \Leftrightarrow \sin \theta_{1}=\sin \theta_{2}=\sin \theta_{3}=\frac{\sin \left(\sum \theta_{j}\right)}{2} .
$$

此时有且仅有如下两类可能性:

(i) 若 $z:=z_{1}=z_{2}=z_{3}$, 设 $\arg z=: \theta \Rightarrow \sin \theta=\frac{1}{2} \sin (3 \theta) \Rightarrow \sin \theta=0$.

(ii) 若 $z:=z_{1}=z_{2}=\overline{z_{3}}$, 同样设

$$
\begin{aligned}
\arg z=: \theta & \Rightarrow \sin \theta=\frac{1}{2} \sin (\theta+(2 k+1) \pi)=-\frac{1}{2} \sin \theta \\
& \Rightarrow \sin \theta=0(k=0,1)
\end{aligned}
$$

而不难验证 $f(\pi, \pi, \pi)=9$ 不是极小值, 这说明 $f$ 在 $[0,2 \pi]^{3}$ 的极小值必于边界上取到.
最后只需证明在边界上不等式恒成立, 不妨 $z_{3}=1$. 即只需说明

$$
\left|z_{1} z_{2}-1\right| \leq\left|z_{1}+z_{2}-2\right| .
$$

到这里, 我们只需通过下面的演算来说明这一事实:

$$
\begin{aligned}
& \left(1-z_{1} z_{2}\right)\left(1-\overline{z_{1}} \overline{z_{2}}\right) \leq\left(2-z_{1}-z_{2}\right)\left(2-\overline{z_{1}}-\overline{z_{2}}\right) \\
\Leftrightarrow & 2-z_{1} z_{2}-\overline{z_{1}} \overline{z_{2}} \leq 6-2\left(z_{1}+\overline{z_{1}}\right)-2\left(z_{2}+\overline{z_{2}}\right)+z_{1} \overline{z_{2}}+\overline{z_{1}} z_{2} \\
\Leftrightarrow & \left(z_{1}+\overline{z_{1}}\right)\left(z_{2}+\overline{z_{2}}\right)-2\left(z_{1}+\overline{z_{1}}\right)-2\left(z_{2}+\overline{z_{2}}\right)+4 \geq 0 \\
\Leftrightarrow & \left(z_{1}+\overline{z_{1}}-2\right)\left(z_{2}+\overline{z_{2}}-2\right) \geq 0 .
\end{aligned}
$$

最后一个不等式是平凡的, 且等号成立当且仅当 $z_{1}, z_{2}$ 中至少有一者为 1 .

至此我们完成了引理的证明.下回到原题.

用反证法, 假设存在 $z_{j}, 1 \leq j \leq 4$ 使得 $3-z_{1}-z_{2}-z_{3}-z_{4}+z_{1} z_{2} z_{3} z_{4}=0$.下面来说明存在 $1 \leq k \leq 4$, 满足 $z_{k}=1$.

注意到此时有

$$
\begin{aligned}
\left(z_{1} z_{2} z_{3}-1\right) z_{4}=z_{1}+z_{2}+z_{3}-3 & \Rightarrow z_{4}=\frac{z_{1}+z_{2}+z_{3}-3}{z_{1} z_{2} z_{3}-1} \\
& \Rightarrow 1=\left|z_{4}\right|=\frac{\left|z_{1}+z_{2}+z_{3}-3\right|}{\left|z_{1} z_{2} z_{3}-1\right|} .
\end{aligned}
$$

据引理知 $z_{j}(1 \leq j \leq 3)$ 中必存在一者等于 1 , 与假设矛盾.

综合上述讨论, 我们完成了本题的证明.

评注 初看这个不等于号会让人觉得奇怪, 但稍加探索后就能发现本质上是形如引理的模长不等式.

我们用完全类似的方法, 可以将引理推广至 $n$ 元, 得到一形式优美的不等式, 这里不再赘述.

B6. 令 $n$ 为一正整数. 证明:

$$
\sum_{k=1}^{n}(-1)^{\lfloor k(\sqrt{2}-1)\rfloor} \geq 0
$$

其中， $\lfloor x\rfloor$ 表示不小于 $x$ 的最小整数.

我们这里给出一简洁而优雅的证法, 思路启发自 [2], 经整理得到.

另外, 在此题的证明过程中, 不区分 $[\cdot]$ 与 $\lfloor\cdot\rfloor$ 两符号.

证明 我们记 $a_{n}:=[n(\sqrt{2}-1)], b_{n}:=[n(\sqrt{2}+1)], \forall n \in \mathbb{N}^{*}$. 写出 $\left\{a_{n}\right\}$ 的前几项后, 可以发现每个正整数都在该数列中出现, 且仅可能出现两次或三次.

自然地, 我们希望求得哪些正整数值会出现三次. 如下的关键引理回答了
这一问题:

引理 对 $\forall t \in \mathbb{N}^{*}$, 数列 $\left\{a_{n}\right\}$ 有连续三项为 $t$ 当且仅当存在 $l \in \mathbb{N}^{*}, t=b_{l}$.

证明 设 $t$ 满足题意, 于是存在 $n \in \mathbb{N}^{*}, t=a_{n}=a_{n+1}=a_{n+2}<t+1$.

记 $l:=n-2 t$, 我们有 (注意到 $(\sqrt{2}-1)(\sqrt{2}+1)=1$ )

$$
\begin{aligned}
& t=a_{n}=a_{n+1}=a_{n+2}<t+1 \\
\Leftrightarrow & t<n(\sqrt{2}-1)<(n+2)(\sqrt{2}-1)<t+1 \\
\Leftrightarrow & t(\sqrt{2}+1)<n<t(\sqrt{2}+1)+(\sqrt{2}-1) \\
\Leftrightarrow & t(\sqrt{2}-1)<n-2 t<(t+1)(\sqrt{2}-1) \\
\Leftrightarrow & l(\sqrt{2}+1)-1<t<l(\sqrt{2}+1) \\
\Leftrightarrow & t=[l(\sqrt{2}+1)]=b_{l} .
\end{aligned}
$$

回到原题, 我们利用无穷递降法.

假设 $N:=\min \left\{n \in \mathbb{N}^{*} \mid \sum_{i=1}^{n}(-1)^{a_{i}}<0\right\}$.

由 $N$ 的定义, 首先可以得到 $(-1)^{a_{N}}=-1$, 否则

$$
\sum_{i=1}^{N-1}(-1)^{a_{i}}=\left(\sum_{i=1}^{N}(-1)^{a_{i}}\right)-1
$$

立得矛盾.

其次, $a_{N}$ 在数列 $\left\{a_{n}\right\}_{n=1}^{\infty}$ 中出现三次, 否则 $a_{N}$ 仅出现两次, 则可能有下述两种情形:

$$
a_{N}=a_{N-1}=-1, a_{N-2}=a_{N-3}=1 \Rightarrow \sum_{i=1}^{N-4}(-1)^{a_{i}}=\sum_{i=1}^{N}(-1)^{a_{i}}<0
$$

或

$$
a_{N}=-1, a_{N-1}=1 \Rightarrow \sum_{i=1}^{N-2}(-1)^{a_{i}}=\sum_{i=1}^{N}(-1)^{a_{i}}<0
$$

均得到矛盾.

从而由引理知存在 $l \in \mathbb{N}^{*}$, 使得 $a_{N}=b_{l}$. 且当 $N \geq 5$ 时, 成立

$$
\frac{N}{2}>[N(\sqrt{2}-1)]=a_{N}=b_{l}=[l(\sqrt{2}+1)] \geq l
$$

故 $N>2 l>l$, 而 $\sum_{i=1}^{n}(-1)^{a_{i}}<0 \Rightarrow\left\{b_{k}\right\}_{k=1}^{l}$ 中值为奇数的项个数多于值为偶数的项的个数. 从而

$$
\sum_{j=1}^{l}(-1)^{b_{j}}<0
$$

我们又注意到

$$
b_{k}=[k(\sqrt{2}+1)] \equiv[k(\sqrt{2}-1)]=a_{k} \quad(\bmod 2)
$$

$$
\Rightarrow \sum_{j=1}^{l}(-1)^{a_{j}}=\sum_{j=1}^{l}(-1)^{b_{j}}<0
$$

于是我们得到了 $l<N$ 使得 $\sum_{j=1}^{l}(-1)^{a_{j}}<0$, 这与 $N$ 的最小性矛盾.

这说明不存在这样的自然数 $N$, 进而题目所给的不等式恒成立.

评注 本题给出的不等式颇吸引人, 不过有着一定的难度.

对于此题, 笔者想要传达的基本都体现在上述解答中. 事实上, 不难发现对和式的正负性起决定性作用的是在 $\left\{a_{n}\right\}$ 中出现三次的整数值, 引理对这样的值给出了一个成功的刻画; 后面利用无穷递降法, 本质上也是利用数学归纳法, 将命题转化为之前讨论过的情形.

以上的解法可以被称为“巧解”, 利用的 $\left\{a_{n}\right\}$ 和 $\left\{b_{n}\right\}$ 同奇偶的性质难以推广。对于本题, 或许可以进行进一步的探索, 如考虑对怎样的 $0<r<1$, $\sum_{k=1}^{n}(-1)^{[k r]} \geq 0$ 对 $\forall n \in \mathbb{N}^{*}$ 恒成立, 有兴趣的读者可进行尝试.

## 参考文献

[1] Manjul Bhargava, Kiran Kedlaya, and Lenny Ng. Solutions to the 81st William Lowell Putnam Mathematical Competition [EB/OL], [2021-3-4]. https://kskedlaya.org/putnam-archive/2020s.pdf

[2] Putnam 2020 B6(Feburary 25, 2021) [EB/OL]. [2021-3-4].

https://artofproblemsolving.com/community/c7t441f7h2461222_putnam_2020_b6

