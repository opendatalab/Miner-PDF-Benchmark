数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年高联第四题在 $n$ 充分大时的最优结果 

汪秉原

(北京大学, 100871)

【原题】求具有下述性质的最小正数 $c$ ：对任意整数 $n \geq 4$, 以及集合 $A \subseteq\{1,2, \ldots, n\}$, 若 $|A|>c n$, 则存在函数 $f: A \rightarrow\{1,-1\}$, 满足

$$
\left|\sum_{a \in A} f(a) \cdot a\right| \leq 1
$$

(2021 年全国高中数学联赛 A 卷加试第四题)

【思路分析】本题的答案是 $\frac{2}{3}$. 构造是 $n=6, A=\{1,4,5,6\}$.

原题中 $n=6$ 时的反例难以推广到一般的 $n$ 的情形, 同时, 观察标答可发现其中的不等式估计无法取等. 因此, 我们有理由认为, 在 $n$ 充分大的时候, 所求的 $c$ 是小于 $\frac{2}{3}$ 的.

另一方面, 我们注意到, 当正整数 $m$ 模 4 余 1 或 2 时, 取 $A=\{1,2, \cdots m\}$.因为

$$
\sum_{i=1}^{m} i=\frac{m(m+1)}{2}
$$

为奇数, 所以对任意的 $f: A \rightarrow\{1,-1\}$, 均有

$$
\left|\sum_{a \in A} f(a) \cdot a\right| \geq 1
$$

那么对于 $2 A=\{2,4, \cdots 2 m\}$, 及任意的 $f: 2 A \rightarrow\{1,-1\}$, 均有

$$
\left|\sum_{a \in A} f(a) \cdot a\right| \geq 2
$$

取正整数 $m$ 模 4 余 1 或 2 ,

$$
m=\frac{n}{2}-O(1)
$$

此时 $2 A$ 即为一个 $n / 2-O(1)$ 元的, 含于 $\{1,2, \cdots n\}$ 中的集合, 且不存在映射

修订日期: 2021-12-23.
$f: A \rightarrow\{1,-1\}$, 使得

$$
\left|\sum_{a \in A} f(a) \cdot a\right| \leq 1
$$

因为这个反例的构造对任意的 $n$ 均成立, 我们猜测:

【猜测】对任意正整数 $n \geq 4$, 记 $c_{n}$ 为满足下述结论的最小正整数: 对于任意的集合 $A \subseteq\{1,2, \cdots n\}$, 若 $|A| \geq c_{n}$, 则存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

那么, $\left|c_{n}-\frac{n}{2}\right|=O(1)$.

按照这个猜测进行一番探索, 最终可以证明以下结论:

【目前最佳结果】对任意的正整数 $n \geq 564$, 记 $c_{n}$ 为满足下述结论的最小正整数: 对于任意的集合 $A \subseteq\{1,2, \cdots n\}$, 若 $|A|>c_{n}$, 则存在 $A$ 的划分 $B \cup C$使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

那么,

当 $n=8 k+2,8 k+3$ 时, $c_{n}=4 k+1$;

当 $n=8 k+4,8 k+5,8 k+6,8 k+7$ 时, $c_{n}=4 k+2$;

当 $n=8 k+8,8 k+9$ 时, $c_{n}=4 k+3$. ( $k$ 为正整数)

这就是 $n$ 充分大时的最优结果, 下面给出其证明.

【证明】一方面, 给出构造:

当 $n=8 k+2,8 k+3$ 时 $A=\{2,4, \cdots 8 k+2\}$ 有 $4 k+1$ 个元素, $\sum_{a \in A} a$ 模 4 余 2 , 由于 $A$ 是偶数集, 故对 $A$ 的划分 $B \cup C,\left|\sum_{b \in B} b-\sum_{c \in C} c\right|$ 为偶数. 如果

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right|=0
$$

则 $B, C$ 中元素和均为 $\frac{\sum_{a \in A} a}{2}$ 是奇数, 与 $A$ 为偶数集矛盾. 从而

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \geq 2
$$

即存在 $|A|=c_{n}$, 不存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

当 $n=8 k+4,8 k+5,8 k+6,8 k+7$ 时, 取 $A=\{2,4, \cdots, 8 k+4\}$ 有 $4 k+2$个元素, 分析内容同上.

当 $n=8 k+8,8 k+9$ 时, 取 $A=\{2,4, \cdots, 8 k+8\} \backslash\{8 k+6\}$ 有 $4 k+3$ 个元素, 分析内容同上.

构造完毕.

另一方面, 我们证明, 当 $|A|>c_{n}$ 时, 存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

先给出一个引理. (本引理中的集合均为可重集, 并集均为可重并)

【引理】如果对正整数 $q, x_{1}, \cdots, x_{q}, y_{1}, \cdots, y_{q}$, 非负整数 $\lambda$, 正整数集合 $X, Y$ 满足:

$$
\left|\sum_{x \in X} x-\sum_{y \in Y} y\right| \leq \lambda+\sum_{i=1}^{q}\left|x_{i}-y_{i}\right|
$$

则存在集合 $M \subseteq\{1, \cdots, q\}$, 使得若记

$$
X^{+}=X \cup\left\{x_{i} \mid i \in M\right\} \cup\left\{y_{i} \mid i \notin M\right\},
$$

记

$$
Y^{+}=Y \cup\left\{y_{i} \mid i \in M\right\} \cup\left\{x_{i} \mid x \notin M\right\},
$$

则有

$$
\left|\sum_{x \in X^{+}} x-\sum_{y \in Y^{+}} y\right| \leq \max \left\{\max _{1 \leq i \leq q}\left\{\left|x_{i}-y_{i}\right|\right\}, \lambda\right\}
$$

注意, $X^{+} \cup Y^{+}$为 $X \cup Y \cup\left\{x_{1}, \cdots, x_{q}\right\} \cup\left\{y_{1}, \cdots, y_{q}\right\}$ 的一个划分.

利用离散介值原理容易证明本引理.

回到原题.

考虑任意 $A$, 使得 $|A|$ 大于目标结论中的 $c_{n}$. 记 $|A|=m$, 则 $m \geq \frac{n-1}{2}$.

我们只要证明, 一定存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

下面分两种情形讨论.

【情形 1】如果存在至少一对相邻整数同时属于 $A$.

从 $A$ 中不断地取出相邻整数对, 直到剩下的数中再也没有相邻整数, 或者取出的相邻整数对达到 28 对. 记剩下的数构成的集合为 $A^{*}$, 设取出的两两不交
的相邻整数对有 $t$ 对, 为 $\left(a_{i}, a_{i+1}\right)(i=1, \cdots, t)$. 显然 $t \leq 28$. 分两种情形讨论.

情形 1.1 若 $t=28$.

我们希望存在 $A^{*}$ 的一个划分 $B^{*} \cup C^{*}$,

$$
\left|\sum_{b \in B^{*}} b-\sum_{c \in C^{*}} c\right|
$$

不太大. 这样就可以将每一对取出的相邻正整数在 $B^{*}$ 和 $C^{*}$ 里各放一个, 以跨度 1 对两集合元素和的差进行调整, 最终调整到不超过 1 , 叙述如下:

如果存在 $A^{*}$ 的一个划分 $B^{*} \cup C^{*}$, 使

$$
\left|\sum_{b \in B^{*}} b-\sum_{c \in C^{*}} c\right| \leq 29
$$

应用引理, 存在 $B \cup C$ 为 $A$ 的一个划分, 且

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

对于情形 1.1, 下面只需证明, 一定存在这样的 $B^{*} \cup C^{*}$ (命题 $P$ ).

记 $\left\lceil\frac{n}{28+2}\right\rceil=p$, 则 $p<\frac{n}{30}+1$, 记区间 $I_{1}, I_{2}, \cdots I_{p}$ 分别为

$$
[1,31),[31,61), \cdots,[30 p-29,30 p]
$$

故 $\{1, \cdots, n\} \subseteq I_{1} \cup I_{2} \cup \cdots \cup I_{p}$.

设

$$
A^{*} \cap I_{i}=A_{i},\left[\frac{\left|A_{i}\right|}{2}\right]=r_{i}(i=1,2, \cdots, p),
$$

对每个 $i$, 取 $A_{i}$ 中的 $2 r_{i}$ 个数 ( $A_{i}$ 里剩下至多一个数没有取), 由小到大列为 $a_{i, 1}, \cdots, a_{i, r_{i}}, b_{i, r_{i}}, \cdots, b_{i, 1}$, 则

$$
\sum_{j=1}^{r_{i}}\left(b_{i, j}-a_{i, j}\right) \geq \sum_{i=1}^{r_{i}}(2 i-1)=r_{i}^{2}
$$

设剩下未被取的数构成的集合为 $A^{* *}\left(A^{* *}\right.$ 可以是空集), 则由每个数不超过 $n$ 可知:

存在 $A^{* *}$ 的划分 $B^{* *} \cup C^{* *}$, 使得

$$
\left|\sum_{b \in B^{* *}} b-\sum_{c \in C^{* *}} c\right| \leq n
$$

根据 $(3),(4)$, 只要 $n-29 \leq \sum_{i=1}^{p} r_{i}^{2}$, 就有

$$
\left|\sum_{b \in B^{* *}} b-\sum_{c \in C^{* *}} c\right| \leq \sum_{i=1}^{p} \sum_{j=1}^{r_{i}}\left|b_{i, j}-a_{i, j}\right|+29
$$

因为

$$
\begin{aligned}
A^{*}=B^{* *} & \cup C^{* *} \\
& \cup\left\{a_{i, j} \mid i=1, \cdots, p, j=1, \cdots, r_{i}\right\} \\
& \cup\left\{b_{i, j} \mid i=1, \cdots, p, j=1, \cdots, r_{i}\right\},
\end{aligned}
$$

应用引理可知, 存在 $A^{*}$ 的一个划分 $B^{*} \cup C^{*}$ 使得

$$
\left|\sum_{b \in B^{*}} b-\sum_{c \in C^{*}} c\right| \leq \max \left\{\max _{\substack{1 \leq i \leq p \\ 1 \leq j \leq r_{i}}}\left\{\left|b_{i, j}-a_{i, j}\right|\right\}, 29\right\} \leq 29
$$

(因为对任意 $i$ 和 $j, b_{i, j}$ 与 $a_{i, j}$ 同在区间 $I_{i}$ 中, 差必然不超过 29 ).

从而完成了命题 $P$ 的证明.

故下面只需证明 $n-29 \leq \sum_{i=1}^{p} r_{i}^{2}$, 即 $n-30 \leq \sum_{i=1}^{p} r_{i}^{2}$.

事实上, 因为

$$
\sum_{i=1}^{p} 2 r_{i} \geq \sum_{i=1}^{p}\left(\left|A_{i}\right|-1\right)=\left|A^{*}\right|-p=m-2 \cdot 28-p,
$$

故由柯西不等式,

$$
\begin{aligned}
\sum_{i=1}^{p} r_{i}^{2} & \geq\left(\frac{\frac{1}{2}(m-2 \cdot 28-p)}{p}\right)^{2} \cdot p \\
& \geq \frac{\left(\frac{1}{2} n-56.5-p\right)^{2}}{4 p} \\
& >\frac{\left(\frac{1}{2} n-57.5-\frac{n}{30}\right)^{2}}{4\left(\frac{n}{30}+1\right)},
\end{aligned}
$$

而解不等式

$$
\frac{\left(\frac{1}{2} n-57.5-\frac{n}{30}\right)^{2}}{4\left(\frac{n}{30}+1\right)}>n-30
$$

得只需 $n>563.53$.

由 $n \geq 564$ 知其成立.

故综上所述, 情形 1.1 下一定存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

情形 1.1 结束.

情形 1.2 若 $0<t<28$.

由前面选取 $t$ 对相邻正整数的方式可知, 此时 $A^{*}$ 中任意两数之差不小于 2 .设 $A^{*}$ 中的数从小到大依次为 $a_{1}, a_{2}, \cdots a_{m-2 t}$, 并对 $i=1,2, \cdots m-2 t-1$, 记 $x_{i}=a_{i+1}-a_{i}$.
类似情形 1.1 , 如果存在 $A^{*}$ 的一个划分 $B^{*} \cup C^{*}$, 使

$$
\left|\sum_{b \in B^{*}} b-\sum_{c \in C^{*}} c\right| \leq 2
$$

应用引理, 存在 $B \cup C$ 为 $A$ 的一个划分, 且

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

从而完成了证明.

下面证明, 一定存在这样的 $B^{*} \cup C^{*}$ (命题 $Q$ ).

设有 $k$ 个 $x_{i}=2$, 则

$$
n-1 \geq a_{m-2 t}-a_{1} \geq k \cdot 2+(m-2 t-1-k) \cdot 3=3 m-6 t-k-3,
$$

所以

$$
k \geq 3 m-6 t-n-2,
$$

将 $a_{1}, a_{2}, \cdots, a_{m-2 t}$ 进行两两配对 $\left(a_{m-2 t}, a_{m-2 t-1}\right), \cdots$, 最终配成下标相邻的 $\left[\frac{m-2 t}{2}\right]$ 对 (可能会剩下单独的 $a_{1}$, 也可能不会, 如果剩下单独的 $a_{1}$, 再人为地增加一对 $\left.\left(a_{1}, 0\right)\right)$.

设上述下标相邻的 $[(m-2 t) / 2]$ 对中有 $u$ 对差为 2 的:

$$
x_{l_{1}}=x_{l_{2}}=\cdots=x_{l_{u}}=2 \text {, }
$$

则根据容斥原理,

$$
u \geq k+\left[\frac{m-2 t}{2}\right]-(m-2 t-1)
$$

注意到剩余的对(不包括可能有的 $\left(a_{1}, 0\right)$ )的差均不小于 3 , 设剩余的对(包括可能有的 $\left.\left(a_{1}, 0\right)\right)$ 里差的最大值为 $s$, 则

$$
s+2 k+3((m-2 t-1)-k-1)<a_{m-2 t}-0 \leq n \text {. }
$$

当 $2 u \geq s-2$ 时, 应用引理, 就存在 $A^{*}=\left\{a_{1}, a_{2}, \cdots a_{m-2 t}\right\}$ 的一个划分 $B^{*} \cup C^{*}$,使得

$$
\left|\sum_{b \in B^{*}} b-\sum_{c \in C^{*}} c\right| \leq 2
$$

成立, 从而命题 $Q$ 获证.

故下面只需证 $2 u \geq s-2$.

事实上, 由 $(5),(6),(7)$,

$$
2 u-s+2 \geq 2\left(\frac{7}{\geq} 2 u-(n-3(m-2 t-1)+3 k-2 k+3)+2\right.
$$

$$
\begin{aligned}
& =2 u-n+3(m-2 t-1)-k-1 \\
& \stackrel{(6)}{\geq} k+2\left[\frac{m-2 t}{2}\right]+(m-2 t-1)-n-1 \\
& \stackrel{(5)}{\geq} 2\left[\frac{m-2 t}{2}\right]+(m-2 t-1)+3 m-6 t-2 n-3 \\
& \geq 5 m-10 t-2 n-5 \\
& \geq \frac{n-20 t-15}{2} \geq \frac{n-555}{2} \geq 0 .
\end{aligned}
$$

故综上所述, 情形 1.2 下一定存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

情形 1.2 结束.

结合情形 1.1 与情形 1.2 的讨论, 在情形 1 下一定存在 $A$ 的划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

情形 1 结束.

【情形 2】如果不存在一对相邻整数同时属于 $A$, 即 $A$ 中任意两数差不小于 2 .

下面分 3 种情形讨论.

情形 $2.1 \quad n=8 k+2,8 k+4$.

此时,

$$
c_{n}=\frac{n}{2}, m \geq \frac{n}{2}+1
$$

$\{1,2, \cdots n\}$ 中任意 $m$ 个数中必有两个相邻, 矛盾!

情形 $2.2 \quad n=8 k+3,8 k+5$.

此时,

$$
c_{n}=\frac{n-1}{2}, m \geq \frac{n+1}{2}
$$

$\{1,2, \cdots n\}$ 中 $m$ 个数中没有两个相邻的, 只有取 $1,3, \cdots n$ 这一种情况,

$$
\begin{aligned}
& n=8 k+3 \text { 时, } \\
& \left|1+3+5+11-7-13+\sum_{i=2}^{k}((8 i+3)-(8 i+1)-(8 i-1)+(8 i-3))\right| \\
& \quad=0 \leq 1 .
\end{aligned}
$$

$$
\begin{aligned}
& n=8 k+5 \text { 时, } \\
& \left|1+3-5+\sum_{i=1}^{k}((8 i+5)-(8 i+3)-(8 i+1)+(8 i-1))\right|=1 \leq 1 .
\end{aligned}
$$

均存在划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

情形 $2.3 n=8 k+6,8 k+7,8 k+8,8 k+9$.

此时, $\{1,2, \cdots n\}$ 中 $m$ 个数中没有两个相邻的, 又 $m \geq\left[\frac{n}{2}\right]$, 故 $m=\left[\frac{n}{2}\right]$或 $\left[\frac{n+1}{2}\right]$.

当 $m$ 元集合 $A$ 中同时存在奇数与偶数, 由于相邻两数差最大不超过 4 , 且 $m-1$ 个相邻的差中存在至少 $m-3$ 个 2 , 又因为相邻两数差中存在奇数(必为 3 ), 取包括 3 的配对, 并将剩下的重新由大到小依次配对作差(如果剩下最小数没有可配的, 看作其与 0 配对), 其中不超过 10 对的差不是 2 , 且每一对的差不超过 10 , 差为 2 的对的数量不小于 100 , 由离散介值原理显然存在划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

当所有数奇偶性相同, 下面对模 8 意义下每种 $n$ 讨论, 最后的, 尚未被证明存在使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

的划分 $B \cup C$ 的, 元素个数超过目标结论中所给 $c_{n}$ 的集合 $A$.

$n=8 k+6$ 时, 唯有 $A=\{2,4, \cdots 8 k+6\}$ 或 $A=\{1,3, \cdots 8 k+5\}$ (化为 $n=8 k+5)$. 而

$$
\left|2+4-6+\sum_{i=1}^{k}((8 i+6)-(8 i+4)-(8 i+2)+8 i)\right|=0 \leq 1
$$

$n=8 k+8$ 时, 唯有 $A=\{2,4, \cdots 8 k+8\}$ 或 $\{1,3, \cdots 8 k+7\}$ (化为 $n=8 k+7)$. 而

$$
\left|\sum_{i=0}^{k}((8 i+8)-(8 i+6)-(8 i+4)+(8 i+2))\right|=0 \leq 1
$$

$n=8 k+9$ 时, 唯有 $A=\{2,4, \cdots 8 k+8\}$ (化为 $n=8 k+8$ )或者, $A=\{1,3, \cdots 8 k+9\}$ 或从中去掉一个奇数;

$n=8 k+7$ 时, 唯有 $A=\{2,4, \cdots 8 k+6\}$ (化为 $n=8 k+6$ )或者, $A=\{1,3, \cdots 8 k+7\}$ 或从中去掉一个奇数.
情况 $(*)$ 与 $(* *)$ 的解答: 因为存在 1 或 3 , 且剩余的数由大到小依次配对作差(如果剩余最小数看作其与 0 配对), 差不为 2 的对的数量不超过 3 个, 且每个对的差不超过 10 , 差为 2 的对的数量不小于 100 , 由离散介值原理显然存在划分 $B \cup C$ 使得

$$
\left|\sum_{b \in B} b-\sum_{c \in C} c\right| \leq 1
$$

情形 2 结束.

综上所述, 原结果获证.

这一做法完全基于离散介值原理, 非常朴素. 核心思想是: 依靠“手中已有的工具”, 逐步缩小跨度. 其中最重要的证明步骤是情形 1.1 与 1.2 中的估计过程, 而情形 2 是较特殊情况的讨论, 较为繁琐.

此结论说明, 当 $n$ 充分大的时候本问题是有精确结果的. 但美中不足的是,目前还不能解决 $n$ 较小的情况. 我们猜测, 在 $n$ 不小于 13 的时候, 前面所给的 $c_{n}$表达式都正确.

【致谢】特别感谢北京大学张裬祥同学, 为我提供了宝贵的建议.

