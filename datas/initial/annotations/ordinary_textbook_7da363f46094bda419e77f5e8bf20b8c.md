# 好题与妙解 (六) 

-2017 年新星秋季精品班两次测试题

## 冷岗松 吴尉迟叶思

2017 年 11 月 19 日和 21 日, 上海数学新星秋季精品班举行了两次测试 (小考). 每次测试四道题, 时间为两个半小时. 本次介绍这两次测试试题的解答. 我们将用题 $1 . x$ 表示第 1 次测试的第 $x$ 题, 题 $2 . y$ 的意义类似. 值得指出的是, 其中一些解法由长郡中学李帅, 巴蜀中学关典, 雅礼中学段钦瀚同学提供, 在此表示感谢.

## I. 试 题

题 1.1 设 $A B$ 是圆 $\odot O$ 的直径, $C D$ 是 $\odot O$ 的一条垂直于 $A B$ 的弦, $E$ 是 $C O$ 的中点, $A E$ 与 $\odot O$ 交于 $F$, 线段 $B C$ 与 $A F, D F$ 分别交于 $M, L, \triangle D L M$的外接圆与 $\odot O$ 交于 $K$. 证明: $K M=M B$.

题 1.2 设 $n \geq 2$ 是给定的正整数, 对任意满足 $a_{k} \geq a_{1}+\cdots+a_{k-1}$, $k=2, \cdots, n$ 的正实数 $a_{1}, a_{2}, \cdots, a_{n}$, 求

的最大值.

$$
S=\frac{a_{1}}{a_{2}}+\frac{a_{2}}{a_{3}}+\cdots+\frac{a_{n-1}}{a_{n}}
$$

题 1.3 设 $\left\{x_{i}\right\}_{i=1}^{\infty}$ 是一个正整数序列, 使得对每一对正整数 $m, n$ 有 $x_{m n} \neq$ $x_{m(n+1)}$. 证明: 存在一个正整数 $i$ 使得 $x_{i} \geq 2017$.

题 1.4 设 $A$ 和 $B$ 是两个有限集, 求满足下列性质的映射 $f: A \rightarrow A$ 的个数: 存在两个映射 $g: A \rightarrow B$ 和 $h: B \rightarrow A$ 使得

$$
g(h(x))=x, \forall x \in B \text { 且 } h(g(x))=f(x), \forall x \in A \text {. }
$$

题 2.1 设 $n$ 是正整数, $n \geq 2$, 证明:

$$
\prod_{k=2}^{n}\left(1+\frac{1}{2^{k}}\right)<2
$$

收稿日期: 2017-12-05.
题 2.2 设 $I$ 是非等腰 $\triangle A B C$ 的内心, 内切圆 $\odot I$ 与 $B C, C A$ 的切点分别为 $D, E, H$ 是 $\triangle A B I$ 的垂心, $K=A I \cap B H, L=B I \cap A H$. 证明: $\odot I$ 与 $\triangle D K H$的外接圆及 $\triangle E L H$ 的外接圆三圆共点.

题 2.3 已知 $X$ 是一个有限集. $X=A_{1} \cup \cdots \cup A_{10}, X=B_{1} \cup \cdots \cup B_{10}$ 是满足如下性质的两个分划: 若 $A_{i} \cap B_{j}=\emptyset, 1 \leq i, j \leq 10$, 则 $\left|A_{i} \cup B_{j}\right| \geq 10$. 求 $|X|$ 的最小值.

题 2.4 设 $m$ 是一个给定的正整数, $d$ 是它的一个正因子. 已知 $\left\{a_{i}\right\}_{i=0}^{\infty}$和 $\left\{b_{i}\right\}_{i=0}^{\infty}$ 是两个由正整数构成的等差数列, 满足: 存在正整数 $i, j, k, l$ 使得 $\left(a_{i}, b_{j}\right)=1,\left(a_{k}, b_{l}\right)=m$. 证明: 存在正整数 $t, s$ 使得 $\left(a_{t}, b_{s}\right)=d$.

## II. 解 答

题 1.1 设 $A B$ 是圆 $\odot O$ 的直径, $C D$ 是 $\odot O$ 的一条垂直于 $A B$ 的弦, $E$ 是 $C O$ 的中点, $A E$ 与 $\odot O$ 交于 $F$, 线段 $B C$ 与 $A F, D F$ 分别交于 $M, L, \triangle D L M$的外接圆与 $\odot O$ 交于 $K$. 证明: $K M=M B$.

![](https://cdn.mathpix.com/cropped/2024_02_26_05e3e17018645bbe1b5dg-02.jpg?height=577&width=612&top_left_y=1296&top_left_x=722)

下面的解法属于湖南省长郡中学李帅同学. 他还指出题中的条件 $C D \perp A B$是多余的.

证明 延长 $K M$ 交 $\odot O$ 于点 $T$, 连接 $A K, K D, M O, T M, T O, T B, B K$.

因为 $D, K, M, L$ 四点共圆, 所以 $\angle C M K=\angle K D F$, 从而 $\overparen{K F}=\overparen{K C}+\overparen{T B}$,因此 $\overparen{C F}=\overparen{B T}$, 故 $\overparen{C T}=\widehat{B F}$.

要证 $M K=M B$, 只需证 $M O \perp K B$, 即等价证明

$$
\begin{aligned}
M O / / A K & \Leftrightarrow \angle O M K=\angle A K M \Leftrightarrow \angle O M K=\angle A B T \\
& \Leftrightarrow O, M, T, B \text { 四点共圆 } \Leftrightarrow \angle O M B=\angle O T B \\
& \Leftrightarrow \angle O M B=\angle O B T \Leftrightarrow \angle O M B=\frac{1}{2} \widehat{A T}=\frac{1}{2}(\widehat{A C}+\overparen{C T})
\end{aligned}
$$

$$
\begin{aligned}
& \Leftrightarrow \angle O M B=\frac{1}{2}(\widehat{A C}+\overparen{B F}) \Leftrightarrow \angle O M B=\angle A M C \\
& \Leftrightarrow \triangle C M E \backsim \triangle B M O \text { (因为 } \angle O B M=\angle E C M) .
\end{aligned}
$$

对 $\triangle O B C$ 和截线 $A E M$ 用 Menelaus 定理可知

$$
\frac{C M}{M B} \cdot \frac{B A}{A O} \cdot \frac{O E}{E C}=1
$$

所以 $\frac{C M}{B M}=\frac{1}{2}=\frac{C E}{B O}$, 又因为 $\angle O B M=\angle E C M$, 所以 $\triangle C M E \sim \triangle B M O$.

评注 这个问题的难度超出我们的预期, 只有 $32 \%$ 的同学做对此题. 此题图形较为复杂, 且三角和代数方法很难奏效, 对几何能力的要求很高. 遗憾的是命题者没有发现题中的条件 $C D \perp A B$ 是多余的. 事实上, 当 $A, B, C, D$ 这四个点已经确定时, 点 $E, F, M$ 也被唯一确定, 所以点 $T$ 也唯一确定, 故点 $K$ 也唯一确定 (可以发现, 点 $K$ 的位置与点 $D$ 无关).

题 1.2 设 $n \geq 2$ 是给定的正整数, 对任意满足 $a_{k} \geq a_{1}+\cdots+a_{k-1}$, $k=2, \cdots, n$ 的正实数 $a_{1}, a_{2}, \cdots, a_{n}$, 求

的最大值.

$$
S=\frac{a_{1}}{a_{2}}+\frac{a_{2}}{a_{3}}+\cdots+\frac{a_{n-1}}{a_{n}}
$$

解法一 满足要求的最大值是 $\frac{n}{2}$.

为了证明这个, 记 $A_{k}=a_{1}+\cdots+a_{k}, k=0, \cdots, n-1$, 并约定 $A_{0}=a_{0}=0$.由题意可知, $A_{k} \leq a_{k+1}, k=0, \cdots, n-1$,

$$
\begin{aligned}
S & =\sum_{k=1}^{n-1} \frac{a_{k}}{a_{k+1}}=\sum_{k=1}^{n-1} \frac{A_{k}-A_{k-1}}{a_{k+1}}=\sum_{k=1}^{n-2} A_{k}\left(\frac{1}{a_{k+1}}-\frac{1}{a_{k+2}}\right)+\frac{A_{n-1}}{a_{n}} \\
& \leq \sum_{k=1}^{n-2} a_{k+1}\left(\frac{1}{a_{k+1}}-\frac{1}{a_{k+2}}\right)+1=\sum_{k=1}^{n-2}\left(1-\frac{a_{k+1}}{a_{k+2}}\right)+1 \\
& =n-1+\frac{a_{1}}{a_{2}}-\sum_{k=1}^{n-1} \frac{a_{k}}{a_{k+1}} \\
& \leq n-\sum_{k=1}^{n-1} \frac{a_{k}}{a_{k+1}}=n-S .
\end{aligned}
$$

因此, $S \leq \frac{n}{2}$, 当 $a_{k}=2^{k-2} a_{1}, k=2,3, \cdots, n$, 其中 $a_{1} \in \mathbb{R}^{+}$时等号成立. 故 $S$ 的最大值为 $\frac{n}{2}$.

下面介绍重庆巴蜀中学关典同学证明 $S \leq \frac{n}{2}$ 的解法.

解法二 为证 $S \leq \frac{n}{2}$. 用归纳法证明更强一点的结论:

$$
T_{n}=\frac{a_{1}}{a_{2}}+\cdots+\frac{a_{n-2}}{a_{n-1}}+\frac{a_{n-1}}{a_{1}+\cdots+a_{n-1}} \leq \frac{n}{2}, n \geq 2
$$

$n=2$ 时, $T_{n} \leq 1$ 显然成立.

$n=3$ 时, $T_{3}=\frac{a_{1}+a_{2}}{a_{2}}+\frac{a_{2}}{a_{1}+a_{2}}-1$, 令 $\frac{a_{1}+a_{2}}{a_{2}}=x$, 则 $x \in(1,2]$.

这时 $T_{3}=x+\frac{1}{x}-1 \leq 2+\frac{1}{2}-1=\frac{3}{2}$.

假设结论对 $n-1(n \geq 4)$ 成立, 即有 $T_{n-1} \leq \frac{n-1}{2}$. 下考虑 $n$ 的情况.

这时若能证明下面的不等式

$$
\frac{a_{n-2}}{a_{n-1}}+\frac{a_{n-1}}{a_{1}+\cdots+a_{n-1}} \leq \frac{a_{n-2}}{a_{1}+\cdots+a_{n-2}}+\frac{1}{2}
$$

则由归纳假设和 $(*)$ 知

$$
\begin{aligned}
T_{n} & =T_{n-2}+\frac{a_{n-2}}{a_{n-1}}+\frac{a_{n-1}}{a_{1}+\cdots+a_{n-1}} \\
& \leq T_{n-2}+\frac{a_{n-2}}{a_{1}+\cdots+a_{n-2}}+\frac{1}{2} \\
& =T_{n-1}+\frac{1}{2} \leq \frac{n-1}{2}+\frac{1}{2}=\frac{n}{2},
\end{aligned}
$$

这说明结论对 $n$ 成立.

下证 $(*)$.

注意到 $(*)$ 等价于

$$
\frac{a_{n-2}\left(a_{1}+\cdots+a_{n-1}\right)+a_{n-1}^{2}}{a_{n-1}\left(a_{1}+\cdots+a_{n-1}\right)} \leq \frac{2 a_{n-2}+a_{1}+\cdots+a_{n-2}}{2\left(a_{1}+\cdots+a_{n-2}\right)} .
$$

记 $A=a_{1}+\cdots+a_{n-2}$, 则上式等价于

$$
\begin{aligned}
& 2 a_{n-2} A^{2}+2 a_{n-2} a_{n-1} A+2 A a_{n-1}^{2} \\
\leq & \left(2 a_{n-2}+A\right) a_{n-1}^{2}+\left(2 a_{n-1}+A\right) A a_{n-1}
\end{aligned}
$$

即

$$
\left(2 a_{n-2}-A\right) a_{n-1}^{2}+A^{2} a_{n-1} \geq 2 a_{n-1} A^{2} .
$$

下证上式成立:

由条件知 $a_{n-1} \geq A, 2 a_{n-2}-A \geq 0$. 故

$$
\left(2 a_{n-2}-A\right) a_{n-1}^{2}+A^{2} a_{n-1} \geq\left(2 a_{n-2}-A\right) A^{2}+A^{2} \cdot A=2 a_{n-2} A^{2} .
$$

故 $(*)$ 得证.

评注 此题难度超过我们的预期, 仅有 $15 \%$ 的同学做对. 上述解法 1 的要点是首先运用 Abel 变换进行恒等变形, 但变形后的式子不能直接求最大值, 而是要用条件将它放缩为含 $S$ 的代数式. 上述解法 2 的要点是不能直接对 $S$ 用归纳法 (因为并不能断定 $\frac{a_{n-1}}{a_{n}} \leq \frac{1}{2}$, 用归纳假设得到的结果弱于结论), 而要采用加强的归纳法, 即转而证明更强一点的结果 $T_{n} \leq \frac{n}{2}$. 这样便将问题转化为证明 (*)
式. $(*)$ 式的证明如果处理不当会相当繁琐, 但如果将 $a_{n-1}$ 看作主变元, 将它转化为关于 $a_{n-1}$ 的二次不等式就不难处理了. 有多位同学采用上述加强归纳法来证明本题.

题 1.3 设 $\left\{x_{i}\right\}_{i=1}^{\infty}$ 是一个正整数序列, 使得对每一对正整数 $m, n$ 有 $x_{m n} \neq x_{m(n+1)}$. 证明: 存在一个正整数 $i$ 使得 $x_{i} \geq 2017$.

证明 我们称正整数 $i<j$ 是 “连通的” , 若存在正整数 $m, n$ 使得 $i=m n$, $j=m(n+1)$. 由题设知, 若 $i, j$ 是连通的, 则 $x_{i} \neq x_{j}$.

为证结论, 只需证 $\left\{x_{i}\right\}_{i=1}^{\infty}$ 中有 2017 个不同的项. 为此, 只需证明存在 $\left\{x_{i}\right\}_{i=1}^{\infty}$ 的一个子序列 $x_{i_{1}}, \cdots, x_{i_{2017}}$ 使得 $i_{1}, \cdots, i_{2017}$ 中的任何两项均是连通的.

下面, 我们用归纳方法证明更一般的结论：对任意正整数 $k \geq 2$, 正整数集 $\mathbb{N}^{*}$ 中能选出 $k$ 个不同的正整数 $i_{1}, \cdots, i_{k}$ 使得其中任两项均是连通的.

$k=2$ 时, 结论显然成立.

假设结论对 $k$ 成立, 即存在两两连通的 $k$ 个正整数 $i_{1}, i_{2}, \cdots, i_{k}$. 现考虑 $k+1$ 的情况.

注意到对任意正整数 $i<j, i, j$ 是连通的当且仅当 $j-i \mid i$. 这样如果 $i, j$ 是连通的, 则对任意满足 $i \mid a$ 的正整数 $a$ 有 $a+i$ 与 $a+j$ 也是连通的.

现记 $A=i_{1} i_{2} \cdots i_{k}$, 则由归纳假设知下面的 $k+1$ 个数: $A, A+i_{1}, \cdots, A+i_{k}$中的任何两项均是连通的. 这说明结论对 $k+1$ 成立.

评注 此题是一个难度适中的问题. 它本质上可转化为下面问题: 对任给的正整数 $k$, 存在 $\mathbb{N}^{*}$ 的一个 $k$ 元子集 $S$ 满足对 $S$ 中的任意两个元 $i<j$ 有 $j-i \mid i$.

这使我们联想到早年一个十分类似的问题, 处理手法也一样. 它是 1998 年 USAMO 的问题: 对任给正整数 $k$, 存在 $\mathbb{N}^{*}$ 的一个 $k$ 元子集 $S$ 使得对任意 $i, j \in S, i \neq j$ 有 $(j-i)^{2} \mid i j$.

这类存在性为题用归纳构造方法处理十分有效. 注意到除式是差的形式,因此我们在归纳假设的基础上利用平移变化来进行构造, 当然选择好平移量是一个关键.

题 1.4 设 $A$ 和 $B$ 是两个有限集, 求满足下列性质的映射 $f: A \rightarrow A$ 的个数：存在两个映射 $g: A \rightarrow B$ 和 $h: B \rightarrow A$ 使得

$$
g(h(x))=x, \forall x \in B \text { 且 } h(g(x))=f(x), \forall x \in A \text {. }
$$

解 答案为 $\left(\begin{array}{l}|A| \\ |B|\end{array}\right)|B|^{|A|-|B|}$.

由 $g(h(x))=x, \forall x \in B$ 知 $h$ 是单射, $g$ 是满射, 从而 $|B| \leq|A|$.

由 $h(g(x))=f(x), \forall x \in A$ 成立知 $f$ 值域是 $h(B)=\{h(x): x \in B\}$.

注意到

$$
f(h(x))=h(g(h(x)))=h(x), \forall x \in B,
$$

故 $f$ 可以表示成如下形式

$$
f(x)=\left\{\begin{array}{ll}
x, & x \in h(B) \\
\varphi(x), & x \in A \backslash h(B)
\end{array},\right.
$$

其中 $\varphi$ 是 $A \backslash h(B) \rightarrow h(B)$ 的任一映射.

下面说明所有能表示成下形式的 $f$ 一定存在映射 $g: A \rightarrow B$ 和 $h: B \rightarrow A$满足条件:

$$
f(x)=\left\{\begin{array}{ll}
x, & x \in A^{\prime} \subset A,\left|A^{\prime}\right|=|B| \\
\varphi(x), & x \in A \backslash A^{\prime}
\end{array},\right.
$$

其中 $\varphi$ 是 $A \backslash A^{\prime} \rightarrow A^{\prime}$ 的任一映射.

取 $B \rightarrow A^{\prime}$ 上的一个一一映射 $l(x)$.

事实上, 设 $h_{1}(x)$ 是 $A^{\prime} \rightarrow A^{\prime}$ 上的恒同映射, 令

$$
h: B \rightarrow A^{\prime} \subset A: \quad h(x)=h_{1}(l(x))=l(x), \quad \forall x \in B
$$

再取映射 $g_{1}: A \rightarrow A^{\prime}:$

$$
g_{1}(x)= \begin{cases}x, & x \in A^{\prime} \\ \varphi(x), & x \in A \backslash A^{\prime}\end{cases}
$$

令映射 $g: A \rightarrow B: g(x)=l^{-1}\left(g_{1}(x)\right), \forall x \in A$.

易证 $g(h(x))=x, x \in B$ 且 $h(g(x))=f(x), \forall x \in A$.

又 $(*)$ 式的 $A^{\prime}$ 的选取有 $\left(\begin{array}{c}|A| \\ |B|\end{array}\right)$ 种方法, 而 $\varphi(x)$ 的选取有 $|B|^{|A|-|B|}$ 种方法,故形如 $(*)$ 式的 $f$ 的个数为 $\left(\left.\begin{array}{l}|A| \\ |B|\end{array}|| B\right|^{|A|-|B|}\right.$ 个, 这也是满足条件的 $f$ 的个数.

评注 此题是一个难题. 仅有 $2.8 \%$ 的人完全做对此题.

有几位学生将 $f(x)$ 写成如下形式

$$
f(x)=\left\{\begin{array}{ll}
x, & x \in h(B) \\
\varphi(x), & x \in A \backslash h(B)
\end{array},\right.
$$

其中 $\varphi$ 是 $A \backslash h(B) \rightarrow A$ 的任一映射, 从而断定这样的 $f$ 个数为 $\left(\begin{array}{l}|A| \\ |B|\end{array}\right)|A|^{|A|-|B|}$,
这是错误的, 其原因是忽略了讨论 $f(x)$ 的值域.

另外, 此题学生常犯的另一个错误是, 发现了 $f(x)$ 具有的形式后便马上给出 $f$ 的计算结果, 便解毕. 事实上, 我们还需要证明具有形式 $(*)$ 的 $f$ 一定可以找到满足要求的 $g$ 和 $h$, 这是严谨性的基本要求.

题 2.1 设 $n$ 是正整数, $n \geq 2$, 证明:

$$
\prod_{k=2}^{n}\left(1+\frac{1}{2^{k}}\right)<2
$$

证明 注意到对 $0<x<1$ 有 $1+x<\frac{1}{1-x}$. 故

$$
\prod_{k=2}^{n}\left(1+\frac{1}{2^{k}}\right)<\frac{1}{\prod_{k=2}^{n}\left(1-\frac{1}{2^{k}}\right)}
$$

由 Bernoulli 不等式

$$
\prod_{k=2}^{n}\left(1-\frac{1}{2^{k}}\right) \geq 1-\sum_{k=2}^{n} \frac{1}{2^{k}}>1-\frac{\frac{1}{4}}{1-\frac{1}{2}}=\frac{1}{2}
$$

综合 (1), (2) 立得结论.

评注 此题为简单题, 大多数学生做对了此题.

i) 上面的解法的关键是如何利用 Bernoulli 不等式, 因此 (1) 式的转换是必要的.

ii) 不少学生用加强归纳的方法证明 $\prod_{k=2}^{n}\left(1+\frac{1}{2^{k}}\right)<2-\frac{1}{2^{n-2}}$.

iii) 此题还可以用著名的分析不等式: $\ln (1+x)<x, \forall x \in(0, \infty)$ 来证明.

题 2.2 设 $I$ 是非等腰 $\triangle A B C$ 的内心, 内切圆 $\odot I$ 与 $B C, C A$ 的切点分别为 $D, E, H$ 是 $\triangle A B I$ 的垂心, $K=A I \cap B H, L=B I \cap A H$. 证明: $\odot I$ 与 $\triangle D K H$ 的外接圆及 $\triangle E L H$ 的外接圆三圆共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_05e3e17018645bbe1b5dg-07.jpg?height=591&width=868&top_left_y=1989&top_left_x=591)
证明 由条件可知, $\angle I D B=90^{\circ}=\angle I K B$, 所以 $B, K, D, I$ 四点共圆. 又 $\angle A L B=90^{\circ}=\angle A K B$, 所以 $B, K, L, A$ 四点也共圆. 因此

$$
\begin{aligned}
\angle B K D & =180^{\circ}-\angle B I D=180^{\circ}-\left(90^{\circ}-\frac{1}{2} \angle A B C\right) \\
& =180^{\circ}-\angle B A L=\angle B K L .
\end{aligned}
$$

因此, $K, D, L$ 共线.

由 $A, E, L, I$ 四点共圆 $\left(\angle A E I=\angle A L I=90^{\circ}\right)$ 有

$$
\begin{aligned}
\angle A L E & =\angle A I E=90^{\circ}-\frac{1}{2} \angle C A B \\
& =90^{\circ}-\angle B A I=90^{\circ}-\angle B A K \\
& =\angle A B K .
\end{aligned}
$$

又由 $L, A, B, K$ 四点共圆知, $\angle A B K=180^{\circ}-\angle A L K$. 所以 $K, E, L$ 共线. 故 $K, D, E, L$ 四点共线.

设 $S$ 是 $\triangle D K H$ 外接圆和 $\triangle E L H$ 外接圆的第二个交点. 则

$$
\begin{aligned}
\angle D S E & =360^{\circ}-\angle D S H-\angle H S E=\angle D K H+180^{\circ}-\angle H L E \\
& =\angle L K H+\angle H L K=180^{\circ}-\angle K H L .
\end{aligned}
$$

又 $H, L, I, K$ 四点共圆, 故

$$
\begin{aligned}
180^{\circ}-\angle K H L & =\angle K I L=\angle A I B=180^{\circ}-\angle I B A-\angle I A B \\
& =180^{\circ}-\frac{1}{2} \angle C B A-\frac{1}{2} \angle C A B .
\end{aligned}
$$

所以

$$
\angle D S E=180^{\circ}-\frac{1}{2} \angle C B A-\frac{1}{2} \angle C A B .
$$

另一方面, 设内切圆 $\odot I$ 与边 $A B$ 切于点 $F$. 则 $A, F, I, E$ 及 $B, F, I, D$ 分别四点共圆. 因此

$$
\begin{aligned}
\angle D F E & =\angle D F I+\angle I F E=\angle D B I+\angle I A E \\
& =\frac{1}{2} \angle C B A+\frac{1}{2} \angle C A B .
\end{aligned}
$$

故

$$
\angle D F E+\angle D S E=180^{\circ} .
$$

这说明 $S$ 在 $\triangle D E F$ 的外接圆上, 即为 $\triangle A B C$ 的内切圆上一点.

这就证明了 $\odot I$ 与 $\triangle D K H$ 的外接圆及 $\triangle E L H$ 的外接圆共点 $S$.
评注 此题难度不大, 上面的解法利用导角得到了 $E, L, D, K$ 四点共线, 进而由角的关系得到结果. 事实上, $H, S, I, F$ 也是四点共线的.

题 2.3 已知 $X$ 是一个有限集. $X=A_{1} \cup \cdots \cup A_{10}, X=B_{1} \cup \cdots \cup B_{10}$ 是满足如下性质的两个分划: 若 $A_{i} \cap B_{j}=\emptyset, 1 \leq i, j \leq 10$, 则 $\left|A_{i} \cup B_{j}\right| \geq 10$. 求 $|X|$ 的最小值.

解 $|X|$ 的最小值为 50 .

我们先证明 $|X| \geq 50$.

考虑集合 $A_{1}, \cdots, A_{10}, B_{1}, \cdots, B_{10}$ 中元素个数最少的集合, 不妨设为 $A_{1}$.记 $\left|A_{1}\right|=a$, 则 $A_{1}$ 至多与 $B_{1}, \cdots, B_{10}$ 中 $a$ 个集合相交. 不妨设

$$
\left|A_{1} \cap B_{i}\right| \neq \emptyset, i=1, \cdots, k \text { 且 } A_{1} \cap B_{i}=\emptyset, i=k+1, \cdots, 10 \text {, }
$$

其中 $k \leq a$. 故 $\left|A_{1} \cup B_{i}\right| \geq 10, i=k+1, \cdots, 10$. 从而对 $\forall i \geq k+1$ 有 $\left|B_{i}\right| \geq 10-\left|A_{1}\right|=10-a$. 由 $\left|A_{1}\right|$ 的最小性知 $B_{1}, \ldots, B_{k}$ 的元素个数均不小于 5. 从而

$$
\begin{aligned}
|X| & =\left|B_{1} \cup \cdots \cup B_{10}\right|=\left|B_{1}\right|+\cdots+\left|B_{k}\right|+\left|B_{k+1}\right|+\cdots+\left|B_{10}\right| \\
& \geq k \cdot a+(10-k)(10-a)=50+2 \cdot(5-k)(5-a) .
\end{aligned}
$$

i) 若 $a \leq 5$, 则 $k \leq 5$, 此时由上式知 $|X| \geq 50$;

ii) 若 $a>5$, 由 $A_{1}$ 是 $A_{1}, \cdots, A_{10}$ 中元素个数最少的集合知 $|X| \geq 10 a>50$.

故 $|X| \geq 50$.

另一方面, $|X|$ 能取到 50 , 例如, 取

$$
\begin{gathered}
A_{1}=B_{1}=\{1,2,3,4,5\}, A_{2}=B_{2}=\{6,7,8,9,10\} \\
\cdots, A_{10}=B_{10}=\{46,47,48,49,50\} .
\end{gathered}
$$

显然它们满足条件, 这时 $X=\{1,2, \cdots, 50\}$.

评注 由题设知, 若 $A_{i} \cap B_{j}=\emptyset$, 则 $\left|B_{j}\right| \geq 10-\left|A_{i}\right|$, 这个不等式可以估计与 $A_{i}$ 不相交的 $B_{j}$ 的元素个数的下界. 因而自然想到用极端原理来估计余下的 $B_{j}$.

题 2.4 设 $m$ 是一个给定的正整数, $d$ 是它的一个正因子. 已知 $\left\{a_{i}\right\}_{i=0}^{\infty}$和 $\left\{b_{i}\right\}_{i=0}^{\infty}$ 是两个由正整数构成的等差数列, 满足: 存在正整数 $i, j, k, l$ 使得 $\left(a_{i}, b_{j}\right)=1,\left(a_{k}, b_{l}\right)=m$. 证明: 存在正整数 $t, s$ 使得 $\left(a_{t}, b_{s}\right)=d$.

证法一 注意到 $m$ 可逐次除以它们若干素因子得到 $d$, 这样只需证对 $m$ 的任意素因子 $p$, 存在正整数 $\alpha, \beta$ 使得 $\left(a_{\alpha}, b_{\beta}\right)=\frac{m}{p}$.
由于 $\left(a_{k}, b_{l}\right)=m$. 故 $\frac{a_{k}}{p}, \frac{b_{l}}{p}$ 必有一项不能被 $m$ 整除. 不妨设 $\frac{a_{k}}{p}$ 不能被 $m$整除.

设等差数列 $\left\{a_{i}\right\},\left\{b_{j}\right\}$ 的公差分别为 $u, v$, 则 $a_{i}=a_{0}+i u, b_{j}=b_{0}+j v$.

下分两种情况:

1) 若 $p \nmid v$. 令 $\alpha=k, \beta=l+\frac{a_{k}}{p}$. 这时 $b_{\beta}=b_{l}+\frac{a_{k} v}{p}$.

注意到 $\frac{m}{p}\left|a_{k}, \frac{m}{p}\right| b_{\beta}$, 又 $p \nmid v$ 且 $m \nmid \frac{a_{k}}{p}$, 所以 $m \nmid b_{\beta}$. 这说明 $\frac{m}{p}$ 是 $a_{\alpha}, b_{\beta}$ 的公因子, 且 $m$ 不是它们的公因子.

设 $q$ 是 $a_{\alpha}, b_{\beta}$ 的一个不同于 $p$ 的公因子, 则 $q\left|a_{\alpha}, q\right| b_{\beta}, q \left\lvert\, \frac{a_{\alpha}}{p}\right.$. 故 $q \left\lvert\,\left(a_{\alpha}, b_{\beta}-\frac{a_{\alpha}}{p} v\right)\right.$, 即 $q \mid\left(a_{k}, b_{l}\right)=m$. 又 $p \nmid q$, 故 $q \left\lvert\, \frac{m}{p}\right.$.

故 $\left(a_{\alpha}, b_{\beta}\right)=\frac{m}{p}$.

2) 若 $p \mid v$. 先证 $p \nmid u(*)$.

事实上, 假设 $p \mid u$, 由 $\left(a_{k}, b_{l}\right)=m$ 知 $p\left|a_{k}-k u=a_{0}, p\right| b_{l}-l u=b_{0}$. 因此 $p\left|a_{i}, p\right| b_{j}$, 这与 $\left(a_{i}, b_{j}\right)=1$ 矛盾! 故 $(*)$ 得证.

取正整数 $s$, 使得 $\frac{b_{l}}{p^{s}}$ 能被 $\frac{m}{p}$ 整除, 但不能被 $m$ 整除.

令 $\alpha=k+\frac{b_{l}}{p^{s}}, \beta=l$. 这时 $a_{\alpha}=a_{k}+\frac{b_{l}}{p^{s}} u, b_{\beta}=b_{l}$.

注意到 $\frac{m}{p}\left|a_{k}, \frac{m}{p}\right| b_{l}, \frac{m}{p} \left\lvert\, \frac{b_{l}}{p^{s}}\right.$, 所以 $\frac{m}{p}$ 是 $a_{\alpha}$ 与 $b_{\beta}$ 的公因子. 又 $m \nmid \frac{b_{l}}{p^{s}}$, 且 $p \nmid u$, 所以 $m \nmid a_{\alpha}$, 从而 $m$ 不是 $a_{\alpha}, b_{\beta}$ 的公因子.

设素数 $q$ 是 $a_{\alpha}, b_{\beta}$ 不同于 $p$ 的公因子, 则 $q\left|b_{\beta}, q\right|\left(a_{\alpha}-\frac{b_{l}}{p^{s}} u\right)=a_{k}$. 即 $q \mid\left(a_{k}, b_{l}\right)=m$. 又 $q \neq p$, 所以 $q \left\lvert\, \frac{m}{p}\right.$.

这说明 $\left(a_{\alpha}, b_{\beta}\right)=\frac{m}{p}$.

由 1),2) 知结论成立.

## 证法二 (雅礼中学段钦瀚)

设 $a_{n}=a_{0}+n d_{1}, b_{n}=b_{0}+n d_{2}$.

注意到 $m$ 可以连续除以它的若干素因子得到 $d$, 故只需证明对 $m$ 的任一素因子 $p$, 存在正整数 $t, s$ 使得 $\left(a_{t}, b_{s}\right)=\frac{m}{p}$.

先证明如下引理:

引理 设 $a, b, c \in \mathbb{N}^{*}$, 若 $(a, b)=1$, 则存在 $n \in \mathbb{N}^{*}$, 使得 $(a n+b, c)=1$.

引理证明任取素数 $q \mid c$, 若 $q \mid a$, 令 $n_{q}=1$; 若 $q \nmid a$, 任取 $n_{q} \not \equiv-\frac{b}{a}(\bmod q)$.

从而当 $n \equiv n_{q}(\bmod q)$ 时,有 $q \neq \equiv a n+b$. 当 $q$ 遍历 $c$ 的所有素因子时, 由中国剩余定理, 这样的 $n \in \mathbb{N}^{*}$ 是存在的, 故 $(a n+b, c)=1$.

回到原题. 令 $m=p d$. 因为 $\left(a_{k}, b_{l}\right)=m$, 故可设 $a_{k}=p d x, b_{l}=p d y$, 则有 $(x, y)=1$.
因为 $\left(a_{i}, b_{j}\right)=1$, 故 $p \nmid a_{i}$ 或 $p \nmid b_{j}$. 不妨设 $p \nmid a_{i}$, 则 $p \nmid a_{k}-a_{i}$. 所以 $p \nmid(k-i) d_{1}$, 从而有 $p \nmid d_{1}$.

设 $r=\left(d_{1}, x\right)$, 又由于 $p \nmid d_{1},(x, y)=1$, 故 $(r, p y)=1$, 由于 $\left(\frac{d_{1}}{r}, \frac{x}{r}\right)=1$, 所以 $\left(\frac{d_{1}}{r}, \frac{p x}{r}\right)=1$.

在引理中取 $a=\frac{d_{1}}{r}, b=\frac{p x}{r}, c=p y$, 则 $(a, b)=1$. 故存在 $n \in \mathbb{N}^{*}$, 使得 $(a n+b, c)=1$. 从而 $\left(\frac{d_{1}}{r} n+\frac{p x}{r}, p y\right)=1$. 又 $(r, p y)=1$, 故 $\left(d_{1} n+p x, p y\right)=1$.

令 $t=k+n d, s=l$, 从而有 $a_{t}=a_{k}+n d d_{1}=d\left(d_{1} n+p x\right), b_{s}=d p y$, 此时有

$$
\left(a_{t}, b_{s}\right)=d\left(d_{1} n+p x, p y\right)=d .
$$

命题得证.

评注 证明一和证明二都证明了等价的命题, 即只需证 $p$ 是素数的情形. 不同的是, 证明一采用分类直接构造的方法; 证明二的要点是要证存在 $n \in \mathbb{N}^{*}$, 使得 $\left(d_{1} n+p x, p y\right)=1$, 故想到用中国剩余定理去证明引理.

