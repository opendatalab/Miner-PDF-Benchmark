# 2018 IMO shortlist 题解析 

依嘉

(中国人民大学附属中学, 100080)

指导老师: 陈晨（学而思数学竞赛主教练）

这是 2018 年 IMO 的预选题及解答. 每年的 IMO 六道试题都是各国领队从当年的 IMO 预选题中通过投票选出来的, 而预选题是由主办国成立一个选题委员会从各国提供的大量问题中遴选而得. 由于IMO 的预选题有一年的保密期,因此目前我们只能看到 2018 年及之前的预选题. 2018 年的预选题共有 28 道, 代数、组合、几何和数论每个板块各 7 道题.

IMO 的预选题是专家们通过讨论选择出来的, 绝大多数质量很高, 风格与IMO 考题类似, 非常适合准备冬令营及以上考试的同学们参考并作为训练资料.

由于作者水平有限, 时间仓促, 难免会有疏漏, 请读者指正.

## I. 代数

A 1. 求所有的函数 $f: \mathbb{Q}_{>0} \rightarrow \mathbb{Q}_{>0}$, 使得对任意 $x, y \in \mathbb{Q}_{>0}$, 均有

$$
f\left(x^{2} f(y)^{2}\right)=f(x)^{2} f(y) .
$$

解答 1. 显然 $f(x)=1$ 满足条件, 下面证明 $f(x)=1$ 是唯一解.

将 $y=1, x=\frac{1}{f(1)}$ 代入原式, 得到 $f\left(\frac{1}{f(1)}\right)=1$.

将 $y=\frac{1}{f(1)}$ 代入原式, 得到 $f\left(x^{2}\right)=f(x)^{2}$, 代入原式有 $(f(x f(y)))^{2}=$ $f(x)^{2} f(y)$, 即

$$
f(y)=\left(\frac{f(x f(y))}{f(x)}\right)^{2}
$$

所以对任意 $y \in \mathbb{Q}_{>0}, f(y)$ 为有理数的平方.

若 $\forall y$ 有 $f(y)$ 为有理数的 $2^{k}$ 次幂, 将其代入 (1) 式可知 $f(y)$ 为有理数的 $2^{k+1}$次幕.

由数学归纳法, $\forall y \in \mathbb{Q}_{>0}, n \in \mathbb{N}, f(y)$ 为有理数的 $2^{n}$ 次幂.
故 $f(y) \equiv 1$.

解答 2. 注意到 $f\left(f(y)^{2} f(z)^{2}\right)=f(y) f(f(z))^{2}=f(z) f(f(y))^{2}$, 因此有

为有理数的平方.

$$
\frac{f(y)}{f(z)}=\left(\frac{f(f(y))}{f(f(z))}\right)^{2}
$$

与解答 1 中类似可知 $\forall y, z \in \mathbb{Q}_{>0}, n \in \mathbb{N}$ 有 $\frac{f(y)}{f(z)}$ 为有理数的 $2^{n}$ 次幂. 故 $\frac{f(y)}{f(z)}=1 \Rightarrow f(x) \equiv c$, 代入原式有 $c^{3}=c \Rightarrow c=1$.

综上 $f(x) \equiv 1$.

注 1. 解答 2 的要点是将原式左端的 $x^{2} f(y)^{2}$ 变为对称结构, 为此只需令 $x=f(z)$.

注 2. 这道函数方程相对比较不常规, 其不同之处主要是在于对有理数的处理, 说明函数值为有理数的 2 的方幂. 这道题虽然不难, 但如果想不到的话也有可能无从下手.

A 2. 求所有的正整数 $n \geq 3$, 使得存在实数 $a_{1}, a_{2}, \ldots, a_{n}, a_{n+1}=a_{1}, a_{n+2}=$ $a_{2}$, 满足对于任意 $i=1,2, \ldots, n$, 均有

$$
a_{i} a_{i+1}+1=a_{i+2} .
$$

解答 1. 由题目条件, 有 $a_{i+2}\left(a_{i+2}-1\right)=a_{i} a_{i+1} a_{i+2}=a_{i}\left(a_{i+3}-1\right)$, 故

$$
a_{i+2}^{2}-a_{i+2}=a_{i} a_{i+3}-a_{i}
$$

将等式两边关于 $i$ 求和得到

$$
\begin{gathered}
\sum_{i}\left(a_{i+2}^{2}-a_{i+2}\right)=\sum_{i}\left(a_{i} a_{i+3}-a_{i}\right) \\
\Rightarrow \sum_{i} a_{i}^{2}-\sum_{i} a_{i} a_{i+3}=0 \\
\Rightarrow \sum_{i}\left(a_{i}-a_{i+3}\right)^{2}=0 .
\end{gathered}
$$

所以有

$$
a_{i}=a_{i+3}, \forall i .
$$

若 $3 \nmid n$, 由 (2) 式可知 $a_{1}=a_{2}=\ldots=a_{n}=c$, 则 $c^{2}+1=c$, 不存在这样的 $c$.

若 $3 \mid n$, 由 (2) 式知数列必为

$$
a_{1}, a_{2}, a_{3}, a_{1}, a_{2}, a_{3}, \ldots, a_{1}, a_{2}, a_{3}
$$

的结构. 原条件此时等价于

$$
\left\{\begin{array}{l}
a_{1} a_{2}+1=a_{3} \\
a_{2} a_{3}+1=a_{1} \\
a_{3} a_{1}+1=a_{2}
\end{array}\right.
$$

易知 $a_{1}=a_{2}=-1, a_{3}=2$ 满足条件.

综上, 满足条件的全体 $n$ 为所有 3 的倍数.

注. 此题思路与 A 1 类似, 都是找到一个具有对称性的式子, 再用两种方式将题目条件用到该式中,得到容易处理的等式.

解答 2. 易知, $3 \mid n$ 时, $a_{3 k}=a_{3 k+1}=-1, a_{3 k+2}=2$ 满足题目条件. 下面证明 $3 \nmid n$ 时不存在满足条件的数列. 我们先证明数列 $\left\{a_{i}\right\}$ 满足如下 4 个结论.

为了记号方便, 我们令 $a_{n+k}=a_{k}, k$ 为任意正整数.

结论 1. 不存在相邻两项都非负.

证明. 反证法. 若存在 $a_{i}, a_{i+1} \geq 0$, 则 $a_{i+2}=a_{i} a_{i+1}+1 \geq 1$, 由归纳法易知 $a_{i} \geq 1$ 对任意正整数 $i$ 成立. 所以 $\sum_{i=1}^{n} a_{i} a_{i+1} \geq \sum_{i=1}^{n} a_{i}$, 而原题条件对 $i$ 求和有 $\sum_{i=1}^{n} a_{i} a_{i+1}+n=\sum_{i=1}^{n} a_{i}$. 矛盾.

结论 2. 不存在 0.

证明. 反证法. 若 $a_{i}=0$, 则 $a_{i+1}=1$, 与结论 1 矛盾.

结论 3. 若相邻两项都是负数, 则之后一项大于 1 .

证明. 可由题目条件直接得到.

结论 4. 不存在相邻5项的正负依次为 “负、负、正、负、正”

证明. 反证法. 若 $a_{i}, a_{i+1}, \ldots a_{i+4}>0$ 为 “负、负、正、负、正”, 由结论 3 可知 $a_{i+2}>1$, 又 $a_{i+3} a_{i+2}+1=a_{i+4}>0$, 所以 $a_{i+3}>-1$.

由题目条件 $a_{i+4}=a_{i+3} a_{i+2}+1<1$, 所以 $a_{i+5}=a_{i+3} a_{i+4}+1>0$,即 $a_{i+4}, a_{i+5}$ 都为正数, 与结论 1 矛盾.

由结论 1-4 可以推出, $\left\{a_{i}\right\}$ 为正负交替或 “负、负、正” 循环.

若 $3 \nmid n$, 则不可能为 “负、负、正” 循环, 必为正负交替, 故 $n$ 为偶数. 不妨设 $a_{1}<0$, 则 $a_{2 k}>0, a_{2 k+1}<0$.

结合题目条件可知,

$$
\begin{gathered}
0>a_{2 k} a_{2 k+1}>-1, \\
a_{2 k+1} a_{2 k+2}<-1
\end{gathered}
$$

将(1),(2)式分别关于 $k=1,2, \ldots, \frac{n}{2}$ 求乘积, 得到

$$
\begin{aligned}
& \left|\prod_{i=1}^{n} a_{i}\right|>1, \\
& \left|\prod_{i=1}^{n} a_{i}\right|<1 .
\end{aligned}
$$

矛盾。

因此 $3 \nmid n$ 时不存在解. 满足条件的全体 $\mathrm{n}$ 为所有 3 的倍数.

注. 这是2018年 IMO 的试题. 证法一的关键是观察到（1）这个等式, 相对简洁. 而证法二则是直接讨论其正负和大小关系, 相对自然, 但略繁琐.

A 3. 给定一个正整数组成的集合 $S$, 求证以下两个命题中一定有一个成立:

1) $S$ 中存在两个不同的有限子集 $F$ 和 $G$, 使得 $\sum_{x \in F} \frac{1}{x}=\sum_{x \in G} \frac{1}{x}$;
2) 存在一个正有理数 $r<1$, 使得对任意 $S$ 的有限子集 $F$, 均有 $\sum_{x \in F} \frac{1}{x} \neq r$.

解答. 反证法. 反设两命题都不成立, 则 $\forall r \in \mathbb{Q} \cap(0,1)$, 恰有一个有限集 $F \subset S$, 满足 $\sum_{x \in F} \frac{1}{x}=r$.

设 $S$ 中除 1 之外的元素从小到大为 $a_{1}, a_{2}, \ldots$ 先给出如下 3 个结论.

结论 1. $\forall a_{n} \in S$, 若 $a_{n} \neq 2$, 则 $\exists i$, s.t. $a_{n}=2 a_{i}$.

证明. 设有限集 $A \subset S$, 满足

$$
\sum_{x \in A} \frac{1}{x}=\frac{2}{a_{n}}
$$

下面分两种情况讨论:

(1) $a_{n} \in A$. 令 $B=A \backslash\left\{a_{n}\right\}$, 则 $B$ 和 $a_{n}$ 是 $S$ 的两个不同的有限子集且

$$
\sum_{x \in B} \frac{1}{x}=\sum_{x \in\left\{a_{n}\right\}} \frac{1}{x}=\frac{1}{a_{n}}
$$

与假设矛盾.

(2) $a_{n} \notin A$.

对 $A$ 中元素 $a_{k}$, 若 $a_{k}>a_{n}$, 设有限集 $C \subset S$ 满足 $\sum_{x \in C} \frac{1}{x}=\frac{1}{a_{n}}-\frac{1}{a_{k}}$, 易知 $a_{n} \notin C$, 而

$$
\sum_{x \in A \backslash\left\{a_{k}\right\}} \frac{1}{x}=\frac{2}{a_{n}}-\frac{1}{a_{k}}=\sum_{x \in C \cup\left\{a_{n}\right\}} \frac{1}{x}
$$

又注意到 $a_{n} \notin A \backslash\left\{a_{k}\right\}, a_{n} \in C \cup\left\{a_{n}\right\}$, 因此 $A \backslash\left\{a_{k}\right\}$ 和 $C \cup\left\{a_{n+1}\right\}$ 是 $S$的两个不同的有限子集. 故上式与假设矛盾.

所以 $\forall a_{k} \in A$, 有 $a_{k}<a_{n}$. 因此 $\forall a_{k}, a_{l} \in A, \frac{1}{a_{k}}+\frac{1}{a_{l}}>\frac{2}{a_{n}}=\sum_{x \in A} \frac{1}{x}$, 所以 $|A|=1$, 即 $A=\left\{a_{i}\right\}$ 且 $2 a_{i}=a_{n}$.

故结论成立.

结论 2. $\forall$ 素数 $p$, 正整数 $n, \exists s \in S$, 使得 $p^{n} \mid s$.

证明. 设有限集 $A \subset S$ 满足

$$
\sum_{x \in A} \frac{1}{x}=\frac{1}{p^{n}}
$$

设等式左端通分后相加为 $\frac{l}{m}$, 则 $m$ 为 $A$ 中元素的最大公约数, 且 $m=p^{n} l$.

若 $\forall x \in A$ 都有 $p^{n} \nmid x$, 则有 $p^{n} \nmid m$, 与 $m=p^{n} l$ 矛盾.

因此 $\exists s \in A$, 使得 $p^{n} \mid s$. 故结论成立.

结论 3. $a_{n+1} \geq 2 a_{n}$.

证明. 反证法. 若 $a_{n+1}<2 a_{n}$, 设有限集 $A \in S$ 满足

$$
\sum_{x \in A} \frac{1}{x}=\frac{1}{a_{n}}-\frac{1}{a_{n+1}}
$$

因为 $\frac{1}{a_{n}}-\frac{1}{a_{n+1}}<\frac{1}{a_{n+1}}$, 故 $a_{n+1} \notin A$.

我们有

$$
\sum_{x \in A \cup\left\{a_{n+1}\right\}} \frac{1}{x}=\frac{1}{a_{n}}=\sum_{x \in\left\{a_{n}\right\}} \frac{1}{x}
$$

与假设矛盾. 故结论成立.

下面给出 2 种不同的方法, 第一种用到结论 1 和结论 2 , 第二种用到结论 3.

方法 1. 设有限集 $B \in S$ 满足 $\sum_{x \in B}=\frac{1}{3}$, 则存在 $a_{k} \in B$, s.t. $3 \mid a_{k}$ (由结论2).

所以 $S$ 中必有 3 的倍数.

令 $a_{m}$ 为 $S$ 中最小的 3 的倍数, 则由结论 1 可知, 存在 $a_{i} \in$ S, s.t. $a_{m}=2 a_{i}$,因此 $3 \mid a_{i}$, 与 $a_{m}$ 是 $S$ 中最小的 3 的倍数矛盾.

故题目中两命题一定有一个成立.

方法 2. 由结论 3 知 $a_{n} \geq 2^{n}$, 所以有

$$
\sum_{n=0}^{\infty} \frac{1}{a_{n}} \leq 1
$$

(1) 若上式不取等, 取有理数 $t$ 满足 $\sum_{n=0}^{\infty} \frac{1}{a_{n}}<t<1$. 则 $t$ 无法表示成 $S$ 中有限个元素的倒数和. 矛盾.

(2) 若上式取等, 则 $a_{n}=2^{n}$, 易知 $\frac{1}{3}$ 无法表示成 $S$ 中有限个元素的倒数和（ $\frac{1}{3}$在 2 进制中是无限小数）.

矛盾.

故题目中两命题一定有一个成立.

注. 此题用反证法后, 可由假设推出很多结论, 除上述两种方法外, 还有其它方法用这些结论导出矛盾, 在此不一一列举. 下面再给出两个上面没列出的结论:

结论 4. 对 $s \in S$, 有理数 $0<t, t+\frac{k}{s}<1$. 设有限集 $A, B \in S$ 满足

$$
\sum_{x \in A} \frac{1}{x}=t, \sum_{x \in B} \frac{1}{x}=t+\frac{k}{s}
$$

若 $k$ 为偶数, 则 $A, B$ 都包含 $s$ 或都不包含 $s$; 若 $k$ 为奇数, 则 $A, B$ 恰有一个包含 $s$.

证明. 只需证明 $k=1$ 时, $A, B$ 恰有一个包含 $s$.

(1) 若 $s \notin A$, 则 $\sum_{x \in A \cup\{s\}} \frac{1}{x}=t+\frac{1}{s}$, 因此 $B=A \cup\{s\}$. 结论成立.

(2) 若 $s \in B$, 则 $\sum_{x \in B \backslash\{s\}} \frac{1}{x}=t$, 因此 $A=B \backslash\{s\}$. 结论成立.

(3) 若 $s \in A, s \notin B$, 结论成立.

综上可知结论成立.

结论 5. 若正整数 $m, n$ 满足 $m \geq n$, 则 $\forall t \in\left[\frac{1}{a_{n}}, \sum_{i=n}^{m} \frac{1}{a_{i}}\right]$, 有 $a_{n} \in A$, 其中 $A$为 $S$ 中倒数和为 $t$ 的有限子集.

证明: 设

$$
\begin{gathered}
\sum_{i=n}^{k} \frac{1}{a_{i}} \leq t \leq \sum_{i=n}^{k+1} \frac{1}{a_{i}} \\
r=t-\sum_{i=n}^{k} \frac{1}{a_{i}}
\end{gathered}
$$

设 $B$ 是 $S$ 中倒数和为 $r$ 的有限子集, 由于 $r \leq \frac{1}{a_{k+1}}<\frac{1}{a_{k}}$, 所以 $a_{n}, a_{n+1}, \ldots, a_{k} \notin$ $B$. 而

$$
\sum_{x \in B \cup\left\{a_{n}, a_{n+1}, \ldots, a_{k}\right\}} \frac{1}{x}=t
$$

所以 $A=B \cup\left\{a_{n}, a_{n+1}, \ldots, a_{k}\right\}$, 故 $a_{n} \in A$.

结论 $1 、 3 、 4 、 5$ 的发现主要利用两个基本结论:

(1) 若有理数 $t<\frac{1}{k}$, 则 $S$ 中倒数和为 $t$ 的有限子集 $A$ 一定不含 $k$.

(2) 对有理数 $0<c<1$, 若 $S$ 中倒数和为 $a, b$ 的有限子集 $A, B$ 交为空且 $a+b=c$, 则 $S$ 中倒数和为 $c$ 的有限子集一定是 $A \cup B$. （解答中主要利用集合 $B$ 只有 1 个元素的情况）

A 4. $a_{0}, a_{1}, a_{2}, \ldots$ 为一个实数列, 它满足 $a_{0}=0, a_{1}=1$, 对任意 $n \geq 2$, 均存在 $1 \leq k \leq n$, 使得

$$
a_{n}=\frac{a_{n-1}+\ldots+a_{n-k}}{k} .
$$

求 $a_{2018}-a_{2017}$ 可能的最大值.

解答. 最大值为 $\frac{2016}{2017^{2}}$.

当

$$
a_{0}=0, a_{1}=1, a_{2}=1, \ldots, a_{2016}=1, a_{2017}=\frac{2016}{2017}, a_{2018}=\frac{2016+\frac{2016}{2017}}{2017}
$$

时, $a_{2018}-a_{2017}=\frac{2016}{2017^{2}}$.下证 $a_{2018}-a_{2017} \leq \frac{2016}{2017^{2}}$.

定义 $a_{n, k}=\frac{a_{n-1}+a_{n-2}+\ldots+a_{n-k}}{k}$.

对给定 $n$, 定义 $\max _{k} a_{n, k}=B_{n}, \min _{k} a_{n, k}=C_{n}$, 则 $C_{n} \leq a_{n} \leq B_{n}$, 有

$$
\begin{aligned}
B_{n+1}-C_{n+1} & =\frac{a_{n}+i a_{n, i}}{i+1}-\frac{a_{n}+j a_{n, j}}{j+1} \\
& \leq \frac{a_{n}+i B_{n}}{i+1}-\frac{a_{n}+j C_{n}}{j+1} \\
& =\frac{i}{i+1}\left(B_{n}-a_{n}\right)+\frac{j}{j+1}\left(a_{n}-C_{n}\right) \\
& \leq \frac{n}{n+1}\left(B_{n}-a_{n}\right)+\frac{n}{n+1}\left(a_{n}-C_{n}\right) \\
& =\frac{n}{n+1}\left(B_{n}-C_{n}\right) .
\end{aligned}
$$

又由 $B_{2}-C_{2}=\frac{1}{2}$, 有 $B_{n}-C_{n} \leq \frac{1}{n}$, 所以

$$
\begin{aligned}
a_{2018}-a_{2017} & =\frac{a_{2017}+k a_{2017, k}}{k+1}-a_{2017} \\
& =\frac{k}{k+1}\left(a_{2017, k}-a_{2017}\right) \\
& \leq \frac{2016}{2017}\left(B_{2017}-C_{2017}\right) \leq \frac{2016}{2017^{2}} .
\end{aligned}
$$

注 1.在看到题目时, 首先考察 $a_{3}-a_{2}, a_{4}-a_{3}, \ldots$ 的最大值. 易知当 $a_{0}=0, a_{1}=1, a_{2}=\frac{1}{2}, a_{3}=\frac{1+\frac{1}{2}}{2}$ 时, $a_{3}-a_{2}$ 最大.当 $a_{0}=0, a_{1}=1, a_{2}=1, a_{3}=\frac{2}{3}, a_{4}=\frac{1+1+\frac{2}{3}}{3}$ 时, $a_{4}-a_{3}$ 最大.

由此可以猜测当 $a_{0}=0, a_{1}=1, a_{2}=1, \ldots, a_{2016}=1, a_{2017}=\frac{2016}{2017}, a_{2018}=$ $\frac{2016+\frac{2016}{2017}}{2017}$ 时, $a_{2018}-a_{2017}$ 最大. 此时 $a_{2018}-a_{2017}=\frac{2016}{2017^{2}}$.

注 2. 此题不容易直接通过观察序列 $\left\{a_{n}\right\}$ 估计出答案, 而如果观察序列 $a_{n, n}, a_{n, n-1}, \ldots, a_{n, 1}$, 则很容易估计固定 $n$ 时该序列的最大最小值之差(注意到, 当 $n$ 变为 $n+1$ 时, 该序列的变化是: 选取原先序列中一个数 $a_{n, k}$ 添加到序列最后, 再把原先序列的每一项 $a_{n, i}$ 变为它与 $a_{n, k}$ 的加权平均 $\left.\frac{i a_{n, i}+a_{n, k}}{i+1}\right)$. 事实上由此还可看出, 解答中的 $B_{n}, C_{n}$ 恰好是 $a_{n, n-1} a_{n, n}$.

A 5. 求所有的 $f:(0, \infty) \rightarrow \mathbb{R}$, 使得对任意 $x, y>0$, 均有

$$
\left(x+\frac{1}{x}\right) f(y)=f(x y)+f\left(\frac{y}{x}\right) .
$$

解答 1 . 取 $y=x^{n}$, 代入原式有

$$
f\left(x^{n+1}\right)-\left(x+\frac{1}{x}\right) f\left(x^{n}\right)+f\left(x^{n-1}\right)=0 .
$$

设数列 $a_{n}=f\left(x^{n}\right)$, 则上式是数列 $\left\{a_{n}\right\}$ 的线性递推式, 即

$$
a_{n+2}-\left(x+\frac{1}{x}\right) a_{n+1}+a_{n}=0,
$$

从而 $a_{n}=A x^{n}+B x^{-n}$.

注意到若 $f(x)$ 是函数方程的解, 则 $f(x)-f(1) x$ 也是解, 故可设 $f(1)=0$,从而 $a_{0}=0, B=-A$.

所以

$$
f\left(x^{n}\right)=A\left(x^{n}-x^{-n}\right), \forall x \neq 1,
$$

其中 $A$ 为由 $x$ 决定的常数.

$$
\begin{aligned}
& \forall a \neq 1, b \neq 1, a b \neq 1, \text { 设 } \\
& f\left(a^{n}\right)=A\left(a^{n}-a^{-n}\right), f\left(b^{n}\right)=B\left(b^{n}-b^{-n}\right), f\left(a^{n} b^{n}\right)=C\left(a^{n} b^{n}-a^{-n} b^{-n}\right),
\end{aligned}
$$

将 $x=\frac{b^{n}}{a^{n}}, y=a^{n} b^{n}$ 代入原式有

$$
f\left(a^{2 n}\right)+f\left(b^{2 n}\right)-\left(\frac{b^{n}}{a^{n}}+\frac{a^{n}}{b^{n}}\right) f\left(a^{n} b^{n}\right)=0 .
$$

于是

$$
A\left(a^{2 n}-a^{-2 n}\right)+B\left(b^{2 n}-b^{-2 n}\right)-\left(\frac{b^{n}}{a^{n}}+\frac{a^{n}}{b^{n}}\right) C\left(a^{n} b^{n}-a^{-n} b^{-n}\right)=0
$$

整理得

$$
(A-C) a^{2 n}+(B-C) b^{2 n}-\left[(A-C) a^{-2 n}+(B-C) b^{-2 n}\right]=0 .
$$

让 $n \rightarrow+\infty, n \rightarrow-\infty$, 分析上式左端的大小可知 $A=B=C$.

所以 $f(x)=A\left(x+\frac{1}{x}\right)+k x$, 其中 $A, k$ 为任意常数. 代入原题易知 $f(x)$ 满足条件.

解答 2. 设 $a_{n}=f\left(x^{n}\right)$, 与解答1 中同理可知 $a_{n}=A x^{n}+B x^{-n}$.

设 $f\left(2^{n}\right)=A_{0} 2^{n}+B_{0} 2^{-n}$.

注意到若 $f(x)$ 是函数方程的解, 则 $f(x)-A_{0} x-B_{0} \frac{1}{x}$ 也是解. 故可设 $f\left(2^{n}\right)=$ $0, \forall n \in \mathbb{Z}$. 对正实数 $t \neq 1$, 设 $f\left(t^{n}\right)=C t^{n}+D t^{-n}$.

由于 $f\left(t^{0}\right)=0$, 故 $D=-C$, 即 $f\left(t^{n}\right)=C\left(t^{n}-t^{-n}\right)$.

将 $x=2 t, y=2$ 代入原式, 有 $f\left(\frac{1}{t}\right)+f(4 t)=\left(2 t+\frac{1}{2 t}\right) f(2)=0$. 故 $f(4 t)=$ $-f\left(\frac{1}{t}\right)=C\left(t-\frac{1}{t}\right)$.

类似地, 将 $x=\frac{t}{2}, y=\frac{1}{2}$ 代入原式, 可以得到

$$
f\left(\frac{t}{4}\right)=C\left(t-\frac{1}{t}\right) .
$$

将 $x=4, y=t$ 代入原式有

$$
f(4 t)+f\left(\frac{t}{4}\right)=\left(4+\frac{1}{4}\right) f(t) .
$$

注. 意到

$$
f(4 t)=f(t)=f\left(\frac{t}{4}\right)=C\left(t-\frac{1}{t}\right)
$$

由上面两式有 $\left(4+\frac{1}{4}-2\right) C\left(t-\frac{1}{t}\right)=0 \Rightarrow C=0$.

此时 $f(x) \equiv 0$.

故 $f(x)=A x+B \frac{1}{x}$.

解答 3. 任取 $a>1$.

代入 $x=y=t$ 有

$$
\left(t+\frac{1}{t}\right) f(t)=f\left(t^{2}\right)+f(1)
$$

代入 $x=\frac{t}{a}, y=a t$ 有

$$
\left(\frac{t}{a}+\frac{a}{t}\right) f(a t)=f\left(t^{2}\right)+f\left(a^{2}\right)
$$

代入 $x=a^{2} t, y=t$ 有

$$
\left(a^{2} t+\frac{1}{a^{2} t}\right) f(t)=f\left(a^{2} t^{2}\right)+f\left(\frac{1}{a^{2}}\right) .
$$

代入 $x=y=a t$ 有

$$
\left(a t+\frac{1}{a t}\right) f(a t)=f\left(a^{2} t^{2}\right)+f(1)
$$

(1) - (2) $+k($ (3) - (4)) 得到

$$
\left(a+\frac{1}{a}-a^{3}-\frac{1}{a^{3}}\right) f(t)=c_{1} t+c_{2} \frac{1}{t}
$$

其中 $k=\frac{\left(\frac{t}{a}+\frac{a}{t}\right)}{\left(a t+\frac{1}{a t}\right)}$ 以消掉 $f(a t), c_{1}, c_{2}$ 为仅与 $a$ 相关的常数.

故 $f(t)=A t+B \frac{1}{t}$.

注. 这道函数方程是一个很有意思的题目, 其答案相对好猜, 但并不容易去证明. 证法 1 和 2 都是通过其递推公式去分析, 其本身想到数列的递推公式就不是很容易. 证法 3 是直接能通过赋值得到解答, 过程很短, 但如果希望自己用这种类型的办法去做的话就要不停的去 “撞” 可能需要的式子.

A 6. 给定正整数 $m, n \geq 2$, 已知实系数多项式 $f\left(x_{1}, \ldots, x_{n}\right)$ 满足

$$
f\left(x_{1}, \ldots, x_{n}\right)=\left\lfloor\frac{x_{1}+\ldots+x_{n}}{m}\right\rfloor, \forall x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-1\} .
$$

求证 $f$ 的总次数至少为 $n$.

解答. 先证明下面关于多项式差分的基本结论:

引理 1. 设 $g(x)$ 为多项式, 多项式 $h(x)=g(x+m)-g(x)$ 则

$$
\begin{cases}\operatorname{deg} h=\operatorname{deg} g-1, & \operatorname{deg} g \geq 1 ; \\ h \equiv 0, & \operatorname{deg} g=0 .\end{cases}
$$

引理 1 的证明. 设 $g(x)=a_{n} x^{n}+\ldots+a_{1} x+a_{0}, a_{n} \neq 0$. 直接计算可知 $h(x)$的最高次项为 $m n a_{n} x^{n-1}$. 故 $\operatorname{deg} h=n-1=\operatorname{deg} g-1$.

引理 2. 设 $g\left(x_{1}, \ldots, x_{n}\right)$ 为多项式, 多项式 $h$ 为 $g$ 关于 $x_{i}$ 的差分, 即 $h\left(x_{1}, \ldots, x_{n}\right)=g\left(x_{1}, \ldots, x_{i-1}, x_{i}+1, x_{i+1}, \ldots, x_{n}\right)-g\left(x_{1}, \ldots, x_{i-1}, x_{i}, x_{i+1}, \ldots, x_{n}\right)$,则 $\operatorname{deg} h \leq \operatorname{deg} g-1$. ( 0 多项式的次数定义成 $-\infty$ )

引理 2 的证明. 只需对单项式证明该结论.

设

$$
g\left(x_{1}, \ldots, x_{n}\right)=x_{1}^{k_{1}} x_{2}^{k_{2}} \ldots x_{n}^{k_{n}}
$$

则

$$
g\left(x_{1}, \ldots, x_{i-1}, x_{i}+1, x_{i+1}, \ldots, x_{n}\right)=x_{1}^{k_{1}} \ldots x_{i-1}^{k_{i-1}}\left(x_{i}+1\right)^{k_{i}} x_{i+1}^{k_{i+1}} \ldots x_{n}^{k_{n}}
$$

上式右端展开后最高此项为 $x_{1}^{k_{1}} x_{2}^{k_{2}} \ldots x_{n}^{k_{n}}$, 因此减去 $g\left(x_{1}, \ldots, x_{n}\right)$ 后最高次项消掉, 故 $\operatorname{deg} h \leq \operatorname{deg} g-1$.

回到原题. 设 $g(x)$ 为满足

$$
g(x)=\left\lfloor\frac{x}{m}\right\rfloor, \forall x \in\{0,1, \ldots,(m-1) n\}
$$

的次数不超过 $(m-1) n$ 的多项式. (由拉格朗日插值可知存在这样的 $g(x)$.)

记 $h(x)=g(x+m)-g(x)$, 则

$$
h(x)=1, \forall x \in\{0,1, \ldots,(m-1) n-m\} .
$$

又因为 0,1 是 $g(x)$ 的零点, 且 $g(x)$ 不恒为 0 , 所以 $\operatorname{deg} g \geq 2$.

由引理 1 有 $\operatorname{deg} h=\operatorname{deg} g-1 \geq 1$, 所以 $h(x)-1$ 不恒为 0 , 且有至少 $(m-$ 1) $n-m+1$ 个零点, 故 $\operatorname{deg} h \geq(m-1) n-m+1$.

$$
\Rightarrow \operatorname{deg} g \geq(m-1) n-m+2 \geq n \text {. }
$$

用 $\Delta_{b_{1}, b_{2}, \ldots, b_{n}} f\left(x_{1}, \ldots, x_{n}\right)$ 表示 $f$ 依次关于 $x_{i}$ 做 $b_{i}$ 次差分得到的多项式, $\Delta_{n} g(x)$ 表示 $g$ 关于 $x$ 做 $n$ 次差分得到的多项式.

由于

$$
f\left(x_{1}, \ldots, x_{n}\right)=g\left(x_{1}+\ldots+x_{n}\right), \forall x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-1\}
$$

所以

$$
\Delta_{1,1, \ldots, 1} f\left(x_{1}, \ldots, x_{n}\right)=\Delta_{n} g\left(x_{1}+\ldots+x_{n}\right), \forall x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-2\}
$$

因为 $n \leq \operatorname{deg} g \leq(m-1) n$,

所以 $\Delta_{n} g$ 不恒为 0, 且 $\operatorname{deg} \Delta_{n} g \leq(m-2) n$.

$\Rightarrow \Delta_{n} g$ 至多 $(m-2) n$ 个零点.

$\Rightarrow\{0,1, \ldots,(m-2) n\}$ 中必有一个不是 $\Delta_{n} g$ 的零点, 设为 $t$.

取 $x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-2\}$, 使得 $x_{1}+\ldots+x_{n}=t$, 则

$$
\Delta_{1,1, \ldots, 1} f\left(x_{1}, \ldots, x_{n}\right)=\Delta_{n} g(t) \neq 0,
$$

因此 $\operatorname{deg} \Delta_{1,1, \ldots, 1} f \geq 0$.

由引理 2 知, $\operatorname{deg} f \geq n+\operatorname{deg} \Delta_{1,1, \ldots, 1} f \geq n$.

注. 在开始做题时, 注意到在 $x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-1\}$ 时， $f$ 的值由 $\left(x_{1}+\ldots+x_{n}\right)$ 的值完全决定, 因此可以试着用 $f\left(x_{1}, \ldots, x_{n}\right)=g\left(x_{1}+\ldots+x_{n}\right)$
构造一个符合条件的函数.

第二个关键点是注意到在 $x_{1}, \ldots, x_{n} \in\{0,1, \ldots, m-1\}$ 时, 对 $f\left(x_{1}, \ldots, x_{n}\right)$求关于 $x_{i}$ 的差分后的值, 等于对 $g$ 求差分后 $g\left(x_{1}+\ldots+x_{n}\right)$ 的值. 这样就可以通过估计 $g$ 次数的下界来给出 $f$ 次数的下界.

A 7. 对于满足 $a+b+c+d=100$ 的非负实数 $a, b, c, d$, 求

的最大值.

$$
S=\sqrt[3]{\frac{a}{b+7}}+\sqrt[3]{\frac{b}{c+7}}+\sqrt[3]{\frac{c}{d+7}}+\sqrt[3]{\frac{d}{a+7}}
$$

解答. $a=c=1, b=d=49$ 时, $S$ 取得最大值 $\frac{8}{\sqrt[3]{7}}$.

下面用三种方法证明 $S \leq \frac{8}{\sqrt[3]{7}}$.

方法 1. 由卡尔松不等式有

$$
S^{3} \leq(\sqrt{a}+\sqrt{b}+\sqrt{c}+\sqrt{d})^{2}\left(\frac{1}{a+7}+\frac{1}{b+7}+\frac{1}{c+7}+\frac{1}{d+7}\right)
$$

构造局部不等式, 显然

$$
\begin{aligned}
& \frac{(x-1)^{2}(x-7)^{2}}{x^{2}+7} \geq 0 \\
\Rightarrow & x^{2}-16 x+7+\frac{64 x^{2}}{x^{2}+7} \geq 0 \\
\Rightarrow & x^{2}-16 x+71 \geq \frac{448}{x^{2}+7}
\end{aligned}
$$

所以

$$
\begin{aligned}
S^{3} & \leq(\sqrt{a}+\sqrt{b}+\sqrt{c}+\sqrt{d})^{2}\left(\frac{1}{a+7}+\frac{1}{b+7}+\frac{1}{c+7}+\frac{1}{d+7}\right) \\
& \leq(\sqrt{a}+\sqrt{b}+\sqrt{c}+\sqrt{d})^{2} \frac{1}{448}\left[\sum_{a}(a-16 \sqrt{a}+71)\right] \\
& =\frac{1}{448}\left(\sum_{a} \sqrt{a}\right)^{2}\left(384-16 \sum_{a} \sqrt{a}\right) \\
& =\frac{1}{56}\left(\sum_{a} \sqrt{a}\right)\left(\sum_{a} \sqrt{a}\right)\left(48-2 \sum_{a} \sqrt{a}\right) \\
& \leq \frac{1}{56} \cdot 16^{3} .
\end{aligned}
$$

所以 $S \leq 16 \sqrt[3]{\frac{1}{56}}=\frac{8}{\sqrt[3]{7}}$.

方法 2. 将 $a, b, c, d$ 重排为 $x, y, z, w$, 使得 $x \leq y \leq z \leq w$. 由排序不等式有

$$
S \leq \sqrt[3]{\frac{x}{w+7}}+\sqrt[3]{\frac{w}{x+7}}+\sqrt[3]{\frac{y}{z+7}}+\sqrt[3]{\frac{z}{y+7}}
$$

下面证明局部不等式

$$
\sqrt[3]{\frac{x}{w+7}}+\sqrt[3]{\frac{w}{x+7}} \leq \sqrt[3]{\frac{x+w+14}{7}}
$$

注意到对不全为 0 的非负实数 $X, Y, Z$, 有

$$
X^{3}+Y^{3}+3 X Y Z-Z^{3}=(X+Y-Z) A
$$

其中 $A=X^{2}+Y^{2}+Z^{2}-X Y+X Z+Y Z>0$.

因此 $X^{3}+Y^{3}+3 X Y Z \leq Z^{3} \Leftrightarrow X+Y \leq Z$.

所以 $(2)$ 式等价于

$$
\frac{a}{b+7}+\frac{b}{a+7}+3 \sqrt[3]{\frac{a b(a+b+14)}{7(a+7)(b+7)}} \leq \frac{a+b+14}{7}
$$

用均值不等式, 有

$$
\begin{aligned}
& \frac{a}{b+7}+\frac{b}{a+7}+3 \sqrt[3]{\frac{a b(a+b+14)}{7(a+7)(b+7)}} \\
& \leq \frac{a}{b+7}+\frac{b}{a+7}+\frac{a(b+7)}{7(a+7)}+\frac{b(a+7)}{7(b+7)}+\frac{7(a+b+14)}{(a+7)(b+7)} \\
& =\frac{a+b+14}{7}
\end{aligned}
$$

因此 (2) 式成立. 同理可得

$$
\sqrt[3]{\frac{y}{z+7}}+\sqrt[3]{\frac{z}{y+7}} \leq \sqrt[3]{\frac{y+z+14}{7}}
$$

由 (1),(2),(4) 及卡尔松不等式有

$$
\begin{aligned}
S & \leq \sqrt[3]{\frac{x+w+14}{7}+\sqrt[3]{\frac{y+z+14}{7}}} \\
& \leq \sqrt[3]{\left(\frac{1}{\sqrt{7}}+\frac{1}{\sqrt{7}}\right)^{2}(x+y+z+w+28)} \\
& =\frac{8}{\sqrt[3]{7}}
\end{aligned}
$$

方法 3. 由 Hölder 不等式有

$$
\begin{aligned}
S^{3} & \leq\left(\sum_{a} \frac{a}{a+7}\right)\left(\sum_{a} \frac{1}{a+7}\right)\left(\sum_{a}(a+7)\right) \\
& =\left(4-7 \sum_{a} \frac{1}{a+7}\right)\left(\sum_{a} \frac{1}{a+7}\right) \cdot 128 \\
& =7\left(\frac{4}{7}-\sum_{a} \frac{1}{a+7}\right)\left(\sum_{a} \frac{1}{a+7}\right) \cdot 128 \\
& \leq 7 \cdot\left(\frac{2}{7}\right)^{2} \cdot 128 \\
& =\frac{512}{7} .
\end{aligned}
$$

故 $S \leq \frac{8}{\sqrt[3]{7}}$.

注 1. 这是一个很难的题目, 解答要分为若干部分且每个部分都不是很好去得到.

注 2. 开始做题时, 先猜 $S$ 的最大值:

(1)

$a=b=c=d=25$ 时, $S=4 \sqrt[3]{\frac{25}{32}}$.

$(2)$

$a=100, b=c=d=0$ 时, $S=\sqrt[3]{\frac{100}{7}}$.

(3) $a=c=50, b=d=0$ 时, $S=4 \sqrt[3]{\frac{25}{28}}$.

情况 (3) 最大, 因此猜测两大两小, 即 $a=c=x, b=d=y$ 时 $S$ 最大. 此时

$$
S=2\left(\sqrt[3]{\frac{x}{y+7}}+\sqrt[3]{\frac{y}{x+7}}\right)
$$

由于 $y=50-x$, 代入后上式右端可看成 $x$ 的函数 $f(x)$. 通过分析 $f$ 的导数可知 $x=1,49$ 时 $f$ 取最大值. 因此猜测 $S$ 最大值为 $\frac{8}{\sqrt[3]{7}}$, 在 $a=c=1, b=d=49$时取到.

注 3. 方法 2 中的局部不等式 $\sqrt[3]{\frac{x}{w+7}}+\sqrt[3]{\frac{w}{x+7}} \leq \sqrt[3]{\frac{x+w+14}{7}}$ 也可以用Hölder 不等式证明：由 Hölder 不等式有

$(x+7)(w+7)(x+w+14)=(x+7)(w+7)((x+7)+(w+7)) \geq(\sqrt[3]{7 x(x+7)}+\sqrt[3]{7 w(w+7)})^{3}$,两端同时开 3 次方, 再移项即可得到方法 2 中的局部不等式. 此办法以及上述解法三并非作者想出, 是审稿人提出的巧妙想法, 这里表示感谢.

## II. 组合

C 1. 给定正整数 $n \geq 3$, 求证存在一个满足以下性质的 $2 n$ 元正整数的集合 $S$ ：对任意 $m=2,3, \cdots, n, S$ 均可被分为和相同的两个子集, 其中一个子集有 $m$ 个元素.

解答 1 . 对 $n$ 归纳.

$n=3$ 时, 取 $S=\{1,2,3,4,5,9\}$, 则 $3+9=1+2+4+5,1+2+9=3+4+5$.

$n=4$ 时, 取 $S=\{1,2,3,4,5,6,10,11\}$, 则 $10+11=1+2+3+4+5+6$,

$5+6+10=1+2+3+4+11,1+4+6+10=2+3+5+11$.

假设 $n=k$ 时结论成立, 下证 $n=k+2$ 时结论成立.

设 $S_{0}=\left\{a_{1}, a_{2}, \ldots, a_{2 k}\right\}$, 满足对任意 $m=2,3, \ldots, k, S_{0}$ 均可被分为和相
同的两个子集, 其中一个子集有 $m$ 个元素. 设 $r=\frac{a_{1}+a_{2}+\ldots+a_{2 k}}{2}$, 由于 $S_{0}$ 满足上述条件, 因此 $r>a_{i}, \forall a_{i} \in S_{0}$. 令 $S=S_{0} \cup\{r, r+1,2 r, 2 r+1\}$.

$m=2$ 时, $\{2 r, 2 r+1\}$ 与 $S \backslash\{2 r, 2 r+1\}$ 元素和相同.

$m=3$ 时, $\{r, r+1,2 r\}$ 与 $S \backslash\{r, r+1,2 r\}$ 元素和相同.

$4 \leq m \leq k+2$ 时, 由假设, $S_{0}$ 可被分为和相同的两个子集 $A, B$, 其中 $|A|=m-2$, 则 $A \cup\{r, 2 r+1\}$ 与 $S \backslash(A \cup\{r, 2 r+1\})$ 元素和相同.

综上, $S$ 满足题目中的性质. 故 $n=k+2$ 时结论成立.

由数学归纳原理, 对正整数 $n \geq 3$ 结论成立.

解答 2 . 直接构造.

令 $a_{1}=2^{m}, a_{3}=2^{m-1}, a_{5}=2^{m-2}, \ldots, a_{2 n-3}=2^{m-(n-2)}$

$a_{2}=2^{m}-1, a_{4}=2^{m-1}-1, a_{6}=2^{m-2}-1, \ldots, a_{2 n-2}=2^{m-(n-2)}-1$

注意到 $a_{2}=a_{3}+a_{4}, a_{4}=a_{5}+a_{6}, \ldots, a_{2 n-4}=a_{2 n-3}+a_{2 n-2}$, 所以

$2^{m+1}-1=a_{1}+a_{2}=a_{1}+a_{3}+a_{4}=a_{1}+a_{3}+a_{5}+a_{6}=\ldots=a_{1}+a_{3}+\ldots+a_{2 n-3}+a_{2 n-2}$因此只需要取合适的 $a_{2 n-1}, a_{2 n}$, 使得 $a_{1}+a_{2}+\ldots+a_{2 n}=2^{m+2}-2$ 即可.

为此只需 $a_{2 n-1}+a_{2 n}=2^{m+1-(n-2)}+(n-1)-2$ 即可.

注. 这道题目条件的要求比较松, 因此构造方法有很多, 经过试验就不难能做出.

C 2. 甲和乙在 $20 \times 20$ 的棋盘上做游戏,一开始棋盘是空的. 每回合, 甲在一个空格内放一个骑士, 使得新放的这个骑士不能攻击任何已经放置的其他骑士, 然后乙选择一个空格放置一个皇后. 当一个人不能动时, 游戏结束. 求甲最多能保证放置多少个骑士。

解答. 对 $20 \times 20$ 的棋盘黑白相间染色. 甲每次都在白格中放骑士, 由于骑士只能攻击异色格中的棋子, 所以这样放置的棋子不会被之前放置的骑士攻击. 因此无论乙如何放置, 甲至少可放 $\frac{200}{2}=100$ 个骑士.

另一方面, 在棋盘中取一个 $4 \times 4$ 的区域, 按图 1 可分成 $A, B, C, D$ 四组. 让乙遵循下面的规则放置: 无论甲放何处, 乙放在和甲同一组, 且不能被甲放置的骑士攻击格子处（例如若甲放在左上角的 $\mathrm{A}$ 格子, 则乙将棋子放在右下角的 $\mathrm{A}$ 格子处）. 若乙遵循此规则放置, 则每组中甲只能放置一个骑士. 因此甲在此 $4 \times 4$区域内之多放置 4 个骑士.

注意到可以将 $20 \times 20$ 的棋盘分为 $5 \times 5=25$ 个 $4 \times 4$ 的区域. 若无论甲放置在哪个区域, 乙都在此区域内遵循上面的规则放置, 则甲最多放置 $25 \times 4=100$

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-16.jpg?height=325&width=339&top_left_y=266&top_left_x=867)

图 1

个骑士.

综上, 甲可以保证放置 100 个骑士.

注. 这是去年IMO 的第四题, 难度不大. 开始做题时如果没有思路, 可以去尝试一下简单的情况, 比如 4 乘 4 的棋盘.

C 3. 给定正整数 $n$. 一条小河里从左到右有 $n+1$ 片荷叶. 一开始, 有 $n$ 个小青蛙都在最左边的荷叶上. 每过一秒钟, 会有一只小青蛙移动: 如果它从一片有 $k$ 只小青蛙的荷叶上开始, 则它可以向右跳至多 $k$ 步 (每次跳动都只能到相邻的荷叶）. 求证至少要过

$$
\left\lceil\frac{n}{1}\right\rceil+\left\lceil\frac{n}{2}\right\rceil+\left\lceil\frac{n}{3}\right\rceil+\ldots+\left\lceil\frac{n}{n}\right\rceil
$$

秒, 小青蛙们才有可能全部跳到最右边的荷叶上.

解答. 将青蛙编号为 $1 \sim n$, 规定每次移动都让一只荷叶上编号最大的青蛙跳动.

若某一秒钟, 有一只青蛙 $A$ 向右跳了 $t$ 步. 则在它跳跃之前, 它所在的荷叶上至少有 $t$ 只青蛙, 又由上面的规定, 青蛙 $A$ 是这些青蛙中编号最大的一个. 因此青蛙 $A$ 的编号大于等于 $t$.

故编号为 $i$ 的青蛙每次至多跳 $i$ 步. 因此编号为 $i$ 的青蛙至少需 $\left\lceil\frac{n}{i}\right\rceil$ 次移动才能到达最右边的荷叶.

因此所有青蛙到最右边的荷叶上至少要 $\left\lceil\frac{n}{1}\right\rceil+\left\lceil\frac{n}{2}\right\rceil+\left\lceil\frac{n}{3}\right\rceil+\ldots+\left\lceil\frac{n}{n}\right\rceil$ 秒.

注 1. 事实上题目中的 $\left\lceil\frac{n}{1}\right\rceil+\left\lceil\frac{n}{2}\right\rceil+\left\lceil\frac{n}{3}\right\rceil+\ldots+\left\lceil\frac{n}{n}\right\rceil$ 为我们提供了思路. 可以想到, 若一只青蛙每次跳至多1步, 一只每次跳至多 2 步, $\cdots . . .$. , 一只每次跳至多 $n$步, 则此题得证.

注 2. 此类问题经常可以规定”运动的是哪只”. 例题:

一群蚂蚁在 $10 \times 10$ 的方格表上走动, 方向为上下左右, 速度为每秒一格. 若行进方向为一左一右的两只蚂蚁相遇, 则移动方向改为一上一下; 若方向为一
上一下的两只蚂蚁相遇, 则改为一左一右. 证明: 所有蚂蚁都会掉下棋盘.

解答思路: 规定每次相遇, 向右的蚂蚁变为向上; 向上的蚂蚁变为向右; 向左的蚂蚁变为向下; 向下的蚂蚁变为向左. 则每只蚂蚁要么一直向上或向右, 要么一直向下或向左. 因此一定掉下棋盘.

C 4. 一个反帕斯卡三角指的是一列有限的三角形放置的正数, 第一行放置一个, 第二行两个, 第三行三个等等, 使得除了最后一行外, 每一行的任意一个数字都等于它下面一行左右两个数字之差的绝对值. 例如, 下图就是一个恰由 1 到 10 组成的四行反帕斯卡三角.

求问能否找到一个恰由 1 到 $1+2+\ldots+2018$ 组成的 2018 行反帕斯卡三角?

解答. 不能找到满足条件的反帕斯卡三角.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-17.jpg?height=528&width=686&top_left_y=1615&top_left_x=685)

图 2

反证法. 若存在这样的反帕斯卡三角, 设 $a_{1}=a_{2}-b_{2}, a_{2}=a_{3}-$ $b_{3}, \ldots, a_{n-1}=a_{n}-b_{n}$. 其中 $n=2018, a_{1}$ 为三角形最上方的数, $a_{i}, b_{i}$ 为 $a_{i-1}$ 下方与其相邻的两个数（如图 2）. 则

$$
a_{n}=a_{1}+b_{2}+b_{3}+\ldots+b_{n}
$$

又因为

$$
a_{n} \leq 1+2+\ldots+2018
$$

所以 $a_{1}, b_{2}, b_{3}, \ldots, b_{n}$ 为 $1,2, \ldots, 2018$ 的一个排列.

下面用两种方法导出矛盾:

方法 1. 设 $a_{n}$ 和 $b_{n}$ 中靠左边的那个数为第 $n$ 行第 $t$ 个数.

设 $A$ 为由第 $2019-t+i$ 行前 $i$ 个数构成的三角形, 其中 $1 \leq i \leq t-1$.

设 $B$ 为由第 $t+1+i$ 行后 $i$ 个数构成的三角形, 其中 $1 \leq i \leq 2017-t$. (如图 3)

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-18.jpg?height=522&width=677&top_left_y=944&top_left_x=695)

图 3

则 $A, B$ 中所有数均大于等于 2019. 易知 $A, B$ 中必有一个有至少 1008 行, 不妨设 $A$ 至少有 1008 行. 可取 $c_{1}=c_{2}-d_{2}, c_{2}=c_{3}-d_{3}, \ldots, c_{1007}=c_{1008}-d_{1008}$,其中 $c_{1}$ 为 $A$ 最上方的数, $c_{i}, d_{i}$ 为 $c_{i-1}$ 下方与其相邻的两个数（类似 $a_{n}, b_{n}$ 的构造）. 易知 $c_{i}, d_{i}$ 都在 $A$ 中, 故有

$$
\begin{aligned}
c_{1008} & =c_{1}+d_{2}+b_{3}+\ldots+b_{1008} \\
& \geq 2019+2020+\ldots+3026 \\
& >1+2+\ldots+2018,
\end{aligned}
$$

矛盾.

故不存在满足条件的反帕斯卡三角形.

方法 2. 设 $A=1+2+\ldots+2017$, 我们来考察三角形中大于等于 $A$ 的数的个数:

首先, 三角形最下面一行中除 $b_{n-1}$ 下面的两个数外若有两个相邻的数都至少为 $A$, 设他们为 $x, y$ 且 $x=y+z$, 其中 $z$ 为 $x$ 和 $y$ 上方的数. 由
于 $z \notin\left\{a_{1}, b_{2}, \ldots, b_{n}\right\}$, 故 $z>2018$, 有

$$
x=y+z>A+2018=1+2+\ldots+2018
$$

与假设矛盾. 因此最下面一行除 $b_{n-1}$ 下面的两个数外不存在两个相邻的数都大于等于 $A$. 因此最下面一行至多 1010 个数大于等于 $A$.

其次, 设 $b_{i}$ 上方的两个数中不是 $a_{i-1}$ 的那个数为 $c_{i-1}$ （如图 4, 对有些 $i$ 可能没有 $c_{i}$ ). 若在前 2017 行中, 有某数 $x \geq A$, 设它下面两个数为 $y, z$,且 $z=x+y$, 则 $y \leq 2018$, 因此 $y \in\left\{b_{2}, b_{3}, \ldots, b_{n}\right\}$. 故 $x=a_{k}$ 或 $x=c_{k}$, 其中 $k$为 $x$ 所在行数.

若 $k \leq 2016$, 因为 $z>x \geq A$, 所以 $z=a_{k+1}$ 或 $z=c_{k+1}$. 此时若 $x=c_{k}$,则 $z$ 与 $a_{k+1}$ 在 $b_{k+1}$ 的两侧, 故 $z$ 不是 $a_{k+1}$ 或 $c_{k+1}$, 矛盾. 因此所有 $c_{i}$ 中至多一个数大于等于 $A$.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-19.jpg?height=525&width=671&top_left_y=1145&top_left_x=704)

图 4

由于

$$
\begin{aligned}
a_{n-64} & =a_{n}-b_{n}-b_{n-1}-\ldots-b_{n-63} \\
& =1+2+\ldots+2018-b_{n}-b_{n-1}-\ldots-b_{n-63} \\
& \leq 1+2+\ldots+2018-1-2-\ldots-64 \\
& <A,
\end{aligned}
$$

因此 $i \leq n-64$ 时, $a_{i}<A$. 故所有 $a_{i}$ 中至多 64 个数大于等于 $A$.

综上, 三角形中至多 $1010+1+64=1075$ 个数大于等于 $A$. 而 1 到 $1+2+$ $\ldots+2018$ 中有 2019 个数大于等于 $A$, 矛盾.

故不存在满足条件的反帕斯卡三角形.

注. 这是去年 IMO 的第三题. 做题的开始要先猜到答案是不行, 这是因为直观上数越多这个表格的限制就越多, 也越难满足. 两个方法的突破口都是要看到
最下面一行某个数是由1至2018累加得到的, 之后的过程就相对自然了.

C 5. 给定正整数 $k$, 一个网球比赛委员会准备安排 $2 k$ 个运动员的比赛, 使得每两个运动员均赛过一次. 由于场地限制, 每天只能进行一场比赛. 组委会必须负担每一位运动员从第一场比赛到最后一场比赛之间的住宿费用（第一场比赛前一天入住旅馆, 最后一次比赛后当天离开旅馆）。旅馆每天收费一元, 求组委会在安排住宿上至少要花多少钱?

解答 1. 设这 $2 k$ 个人分别在第 $A_{1}<A_{2}<\ldots<A_{2 k}$ 天进行首次比赛,在第 $B_{2 k}<B_{2 k-1}<\ldots<B_{1}$ 天最后一次比赛（注意第 $A_{i}, B_{i}$ 天不一定是同一个人首次和末次比赛）.显然所有比赛一共要打 $\left(\begin{array}{c}2 k \\ 2\end{array}\right)$ 天. 住宿所需费用为 $\sum_{i=1}^{2 k} B_{i}-\sum_{i=1}^{2 k} A_{i}+2 k$.

当 $0 \leq i \leq k$ 时, 由于第 $A_{i+1}$ 天之前只有 $i$ 个人打过比赛, 第 $B_{i+1}$ 天之后只剩 $i$ 个人打比赛, 因此有 $A_{i+1} \leq\left(\begin{array}{l}i \\ 2\end{array}\right)+1, B_{i+1} \geq\left(\begin{array}{c}2 k \\ 2\end{array}\right)-\left(\begin{array}{l}i \\ 2\end{array}\right)$ 因此

$$
B_{i+1}-A_{i+1}+1 \geq\left(\begin{array}{c}
2 k \\
2
\end{array}\right)-2\left(\begin{array}{l}
i \\
2
\end{array}\right)
$$

当 $k+1 \leq i \leq 2 k-1$ 时, 用 $S$ 表示第 $A_{i+1}$ 天之前打过比赛的人构成的集合， $T$ 表示第 $B_{i+1}$ 天之后剩下的人构成的集合. 则 $|S|=|T|=i$. 又因为共有 $2 k$个人, 因此 $|S \cap T| \geq 2(i-k)$. 记 $V_{X}$ 表示集合 $X$ 的所有二元子集构成的集合.由容斥原理, 在第 $A_{i+1}$ 天之前和第 $B_{i+1}$ 天之后进行的比赛至多有

$$
\left|V_{S} \cup V_{T}\right|=\left(\begin{array}{c}
|S| \\
2
\end{array}\right)+\left(\begin{array}{c}
|T| \\
2
\end{array}\right)-\left(\begin{array}{c}
|S \cap T| \\
2
\end{array}\right)
$$

场, 因此

$$
B_{i+1}-A_{i+1}+1 \geq\left(\begin{array}{c}
2 k \\
2
\end{array}\right)-2\left(\begin{array}{l}
i \\
2
\end{array}\right)+\left(\begin{array}{c}
2(i-k) \\
2
\end{array}\right)
$$

将(1),(2)式对 $i$ 求和后有

$$
\begin{aligned}
& \sum_{i=1}^{2 k} B_{i}-\sum_{i=1}^{2 k} A_{i}+2 k \\
\geq & \sum_{i=0}^{k}\left(\left(\begin{array}{c}
2 k \\
2
\end{array}\right)-2\left(\begin{array}{l}
i \\
2
\end{array}\right)\right)+\sum_{i=k+1}^{2 k-1}\left(\left(\begin{array}{c}
2 k \\
2
\end{array}\right)-2\left(\begin{array}{c}
i \\
2
\end{array}\right)+\left(\begin{array}{c}
2(i-k)) \\
2
\end{array}\right)\right) \\
= & 2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k .
\end{aligned}
$$

故住宿费用至少 $2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k$ 元.

构造: 设这 $2 \mathrm{k}$ 个人为 $a_{1}, a_{2}, \cdots, a_{k}$ 和 $b_{1}, b_{2}, \cdots, b_{k}, a b$ 表示 $a$ 和 $b$ 打比赛.按下述方法安排比赛:

$$
a_{1} a_{2}, \quad a_{1} a_{3}, a_{2} a_{3}, \quad a_{1} a_{4}, a_{2} a_{4}, a_{3} a_{4}, \quad \cdots \quad, \quad a_{1} a_{k}, a_{2} a_{k}, \cdots, a_{k-1} a_{k}
$$

$$
\begin{gathered}
a_{1} b_{1}, a_{2} b_{1}, \cdots, a_{k-1} b_{1}, \quad a_{1} b_{2}, \cdots, a_{k-2} b_{2}, \quad \cdots \quad, \quad a_{1} b_{k-2}, a_{2} b_{k-2}, \quad a_{1} b_{k-1} \\
a_{1} b_{k}, \quad a_{2} b_{k-1}, a_{2} b_{k}, \quad a_{3} b_{k-2}, a_{3} b_{k-1}, a_{3} b_{k}, \quad \cdots \quad, \quad a_{k} b_{1}, a_{k} b_{2}, \cdots a_{k} b_{k} \\
b_{1} b_{2}, b_{1} b_{3}, \cdots, b_{1} b_{k}, \quad \cdots \quad, \quad b_{k-2} b_{k-1}, b_{k-2} b_{k}, \quad b_{k-1} b_{k}
\end{gathered}
$$

则 $a_{i}$ 首次比赛在第 $\left(\begin{array}{c}i-1 \\ 2\end{array}\right)+1$ 天, 末次比赛在第 $k(k-1)+\left(\begin{array}{c}i+1 \\ 2\end{array}\right)$ 天.

$b_{i}$ 首次比赛在第 $k(k-1)-\left(\begin{array}{c}k+1-i \\ 2\end{array}\right)+1$ 天, 末次比赛在第 $\left(\begin{array}{c}2 k \\ 2\end{array}\right)-\left(\begin{array}{c}k-i \\ 2\end{array}\right)$ 天. 可以算得共需 $2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k$ 元住宿费.

综上, 住宿费至少 $2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k$ 元.

解答 2. 构造同解答 1 ,下面来说明住宿费不少于 $2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k$ 元.

引理. $n$ 对实数 $\left\{a_{1}, b_{1}\right\},\left\{a_{2}, b_{2}\right\}, \cdots,\left\{a_{n}, b_{n}\right\}$, 设 $c_{i}=\min \left\{a_{i}, b_{i}\right\}, d_{i}=$ $\max \left\{a_{i}, b_{i}\right\}$, 则有

$$
\left(\max _{i} c_{i}-\min _{i} c_{i}\right)+\left(\max _{i} d_{i}-\min _{i} d_{i}\right) \leq\left(\max _{i} a_{i}-\min _{i} a_{i}\right)+\left(\max _{i} b_{i}-\min _{i} b_{i}\right) .
$$

引理的证明. 设 $A=\max _{i} a_{i}, B=\max _{i} b_{i}$, 设 $\max _{i} c_{i} \in\left\{a_{j}, b_{j}\right\}$, 由于 $a_{j} \leq$ $A, b_{j} \leq B$, 所以有

$$
\begin{gathered}
\max _{i} c_{i}=\min \left\{a_{j}, b_{j}\right\} \leq \min \{A, B\}, \\
\max _{i} d_{i}=\max \left\{a_{1}, \cdots, a_{n}, b_{1}, \cdots, b_{n}\right\}=\max \{A, B\}
\end{gathered}
$$

将上面两式相加有

$$
\max _{i} c_{i}+\max _{i} d_{i} \leq A+B=\max _{i} a_{i}+\max _{i} b_{i} \text {. }
$$

同理有

$$
\min _{i} c_{i}+\min _{i} d_{i} \geq \min _{i} a_{i}+\min _{i} b_{i}
$$

$(2),(3)$ 相减可得(1)式, 故引理成立.

回到原题, 对 $k$ 归纳. 易知 $k=1$ 时住宿费不小于 $2+\frac{1}{2}-\frac{1}{2}=2$ 元. 假设对 $k-1$ 结论成立, 下证对 $k$ 结论也成立.

设所有运动员为 $a_{1}, \cdots, a_{2 k}$. 选定 $i<j$, 可对比赛顺序作下列操作: 对所有 $l \neq i, j$, 若 $a_{i} a_{l}$ 在 $a_{j} a_{l}$ 之后比赛, 则将这两场比赛的日期对调.

由引理可知, 每次每次操作后住宿费不变或减少.

设 $X=\sum_{i=1}^{k(2 k-1)}(i \cdot f(i))$, 其中 $f(i)$ 为第 $i$ 天比赛的两人编号之和（即若第 $i$ 天是 $a_{j}$ 与 $a_{l}$ 比赛, 则 $f(i)=j+l$ ). 易知每次操作后 $X$ 减少, 又因为 $X$一定大于 0 , 故有限次操作后, 比赛顺序不再被任何操作改变. 此时比赛满足:
对 $i<j, a_{i} a_{l}$ 一定在 $a_{j} a_{l}$ 之前比赛. 下面均假设比赛满足此条件.

设 $a_{i}$ 在第 $t_{i}$ 天打首场比赛, 第 $r_{i}$ 打末场比赛. 设去掉 $a_{1}, a_{2 k}$ 参与的比赛后, $a_{i}$ 在第 $t_{i}^{\prime}$ 天首场比赛,第 $r_{i}^{\prime}$ 天末场比赛, $2 \leq i \leq 2 k-1$.

对 $2 \leq i \leq 2 k-1$, 由于 $a_{i}$ 入住期间, $a_{1}$ 和 $a_{2 k}$ 均不参与的比赛共有 $r_{i}^{\prime}-t_{i}^{\prime}+1$场. 又因为

$$
a_{1} a_{i}, a_{1} a_{i+1}, \cdots, a_{1} a_{2 k-1}, a_{1} a_{2 k}, a_{2} a_{2 k}, \cdots, a_{i} a_{2 k}
$$

必定按上述顺序比赛, 因此 $a_{i}$ 入住期间有 $a_{1}$ 或 $a_{2 k}$ 参与的比赛至少 $2 k$ 场. 因此有

$$
r_{i}-t_{i}+1 \geq r_{i}^{\prime}-t_{i}^{\prime}+1+2 k
$$

又因为第一天比赛一定是 $a_{1} a_{2}$, 最后一天一定是 $a_{2 k-1} a_{2 k}$ 比赛, $a_{1} a_{2 k}$ 既是 $a_{1}$ 最后一场比赛也是 $a_{2 k}$ 首场比赛. 因此 $t_{1}=1, r_{2 k}=k(2 k-1), t_{2 k}=r_{1}$, 故

$$
r_{1}-t_{1}+r_{2 k}-t_{2 k}=k(2 k-1)-1 .
$$

又由归纳假设有

$$
\sum_{i=2}^{2 k-1}\left(r_{i}^{\prime}-t_{i}^{\prime}+1\right) \geq 2(k-1)^{3}+\frac{1}{2}(k-1)^{2}-\frac{1}{2}(k-1)
$$

由(4)(5)(6)式可知

$$
\begin{aligned}
\sum_{i=1}^{2 k}\left(r_{i}-t_{i}+1\right) & \geq 2(k-1)^{3}+\frac{1}{2}(k-1)^{2}-\frac{1}{2}(k-1)+2 k(2 k-2)+k(2 k-1)-1+2 \\
& =2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k
\end{aligned}
$$

所以结论对 $k$ 成立.

由数学归纳原理, 对任何正整数 $k$, 住宿费至少 $2 k^{3}+\frac{1}{2} k^{2}-\frac{1}{2} k$ 元.

注. 这道题同样应该从 $\mathrm{k}$ 较小的情况入手, 去考虑什么时候总住宿费最少. 两种证法的本质都是首尾配对去估计, 证法一采取了直接放缩的手段, 证法二则使用了归纳法. 这道题的计算量很大, 做题时要避免算错答案的情况.

C 6. 给定不同的正整数 $a$ 和 $b$, 小明在一个起初空白的无限大的黑板上进行如下操作:

1) 如果, 黑板上存在两个相同的数字, 则他可以选取其中一对, 将它们其中一个用它加 $a$ 得到的数替代, 另一个用它加 $b$ 得到的数替代;
2) 如果黑板上不存在两个相同的数字, 则写下两个 0 .

求证最终黑板上只能有有限个数字.
解答. 令 $M=3 \times 2^{2 a b+2 a+2 b}$ 我们证明更强的结论: 若在某一时刻 $t$, 黑板上有 $M$ 个数字, 则之后不可能再执行操作 2.

反证法. 若结论不成立, 则在时刻 $t$ 之后只能执行有限次操作 1 , 设做完这有限次操作 1 后的时间为 $t^{\prime}$. 不妨设 $\operatorname{gcd}(a, b)=1 （$ 若 $\operatorname{gcd}(a, b)=d \neq 1$, 用 $\frac{a}{d}, \frac{b}{d}$代替 $a, b$ ). 若某次操作 1 将两个 $n$ 变为 $n+a, n+b$, 我们称该次操作的 “旧数字”为 $n$.

设在时刻 $t^{\prime}$ 前通过操作得到 $n$ 的次数为 $f(n)$. 黑板上每个数字刚出现时都是 0 , 故 $f(0)=M$. 对正整数 $n$, 有 $f(n)$ 个数字变成过 $n$, 由于 $t^{\prime}$ 时刻不能再做操作 1 , 因此最终至多剩 1 个 $n$, 故恰有 $\left\lfloor\frac{f(n)}{2}\right\rfloor$ 次旧数字为 $n$ 的操作 1 . 注意到每次旧数字为 $n-a$ 或 $n-b$ 的操作恰得到 1 个数字 $n$, 且数字 $n$ 只能由这两种操作, 因此有

$$
f(n)=\left\lfloor\frac{f(n-a)}{2}\right\rfloor+\left\lfloor\frac{f(n-b)}{2}\right\rfloor .
$$

对整数 $x \in[a b, a b+a+b]$, 由于 $x, x-a, \cdots, x-(b-1) a$ 除以 $b$ 所得余数互不相同, 因此一定有一个是 $b$ 的倍数, 故 $x$ 可以写成 $k_{1} a+k_{2} b$ 的形式 ( $k_{1}, k_{2}$ 是非负整数). 由(1)式有 $f(n)+1 \geq\left\lfloor\frac{f(n-a)}{2}\right\rfloor+1 \geq\left\lfloor\frac{f(n-a)+1}{2}\right\rfloor$, 同理 $f(n)+1 \geq\left\lfloor\frac{f(n-b)+1}{2}\right\rfloor$. 因此

$$
f(x)+1=f\left(k_{1} a+k_{2} b\right)+1 \geq \frac{f\left(\left(k_{1}-1\right) a+k_{2} b\right)+1}{2} \geq \cdots \geq \frac{f(0)+1}{2^{k_{1}+k_{2}}} \geq 3,
$$

故

$$
f(x) \geq 2, \forall x \in\{a b, a b+1, \cdots, a b+a+b\} .
$$

若对非负整数 $k$ 有

$$
f(x) \geq 2, \forall x \in\{k+a b, k+a b+1, \cdots, k+a b+a+b\}
$$

由(1)式可知 $f(k+a b+a+b+1)=\left\lfloor\frac{f(k+a b+b+1)}{2}\right\rfloor+\left\lfloor\frac{f(k+a b+a+1)}{2}\right\rfloor \geq 2$, 因此

$$
f(x) \geq 2, \forall x \in\{(k+1)+a b,(k+1)+a b+1, \cdots,(k+1)+a b+a+b\}
$$

由数学归纳原理, 对任意非负整数 $k,(2)$ 式成立. 因此 $\forall x \geq a b$, 有 $f(x) \geq 2$, 这与 $t^{\prime}$ 时刻前只做有限次操作矛盾.

故黑板上不能出现多于 $M$ 个数字.

注. 自己做这道题时, 不难会发现最终这个操作会有“循环” , 但这个内容本身并不好说明. 解答的巧妙之处在于其构造了 $f$ 来表示一个数出现的次数, 并且可以得到不同数出现次数之间的递推关系.

C 7. 考察 2018 个任三个不共点的两两相交的圆. 这些圆将平面分为了若干个不交的区域. 注意到, 每个圆上必有偶数个交点. 对于每个圆, 将其上的所有交点交替染为黄色或蓝色. 于是每个点共被染过两次色, 如果这两次颜色相同, 则它最终被染为该颜色, 如果不同色它最终被染为绿色. 求证, 如果存在一个圆, 其上有2061个点均为绿色, 则存在一个区域, 其边界上的交点均为绿色.

解答. 我们先给出两种方法证明下述引理:

引理. 在题目条件下, 可以将所有圆分为 $A, B$ 两类, 满足同类圆之间的交点为绿色, 不同类的圆的交点不是绿色.

证明 1. 先按下述方法将所有区域染成黑白两色: 若一个区域在偶数个圆的内部, 则染为白色, 否则染为黑色. 易知有公共边的两个区域不同色（因为它们分别在公共边所在圆的内部和外部, 而在其它圆的同侧）.

对每个圆, 将该圆的每段弧规定方向, 使其从黄色顶点指向蓝色顶点. 由于圆上的点交替染为黄蓝两色, 因此圆上弧的方向是顺时针和逆时针交替排列的. 又由相邻区域不同色可知, 同一圆上每段弧左侧的区域颜色相同（弧的方向为顺时针时左侧是圆的外部, 逆时针时左侧是圆的内部, 如图5）. 将所有圆分为 $A, B$ 两类: 若一个圆上所有弧的左侧的区域是黑色, 则此圆是 $A$ 类, 否则为 $B$ 类.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-24.jpg?height=522&width=237&top_left_y=1578&top_left_x=915)

图 5

设 $P$ 是两圆交点, 在两个圆上分别取一段以 $P$ 为端点的弧 $\alpha, \beta$. 若 $P$ 点在两个圆上的颜色不同, 则弧 $\alpha, \beta$ 左侧区域颜色相同（图 6 左侧）, 故两圆在同一类中. 若 $P$ 在两个圆上的颜色相同, 则弧 $\alpha, \beta$ 左侧区域颜色不同, 两圆不在同一类中（图 6 右侧）. 因此交点 $P$ 的颜色是绿色当且仅当过 $P$ 的两个圆是同一类的. 故引理成立.

证明 2 . 我们将涂蓝色记为 +1 , 涂黄色记为 -1 , 为每个交点赋值, 值为该点
![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-25.jpg?height=478&width=1210&top_left_y=246&top_left_x=413)

图 6

被染的两次颜色对应的数之积. 则一个点最终为绿色当且仅当该点值为 -1 .

下面我们证明两个结论:

结论 1 : 两个圆的两个交点处的值相同.

结论 2: 三个圆中, 每两个圆选取一个交点, 则选出的三个点处的值有 1 个或 3 个等于 -1 .

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-25.jpg?height=483&width=740&top_left_y=1409&top_left_x=612)

图 7

设两个圆交于 $A, B$ 两点（上面的值也用 $A, B$ 表示）, 设 $A=(-1)^{x} \times$ $(-1)^{y}$, 其中 $A$ 点在第一个圆上的颜色是黄色时, $x$ 为奇数, 否则为偶数, $A$ 点在第二个圆上的颜色是黄色时, $y$ 为奇数, 否则为偶数. 设从 $A$ 到 $B$ 的两段弧上的交点个数（不含 $A, B$ ) 分别为 $a, b$, 由于每个圆与这两段弧共有偶数个交点, 因此 $a+b$ 为偶数, 故 $B=(-1)^{x+a+1} \times(-1)^{y+b+1}=A$, 结论 1 成立.

在三个圆中, 无论它们位置关系如何, 都可找到三个点 $A, B, C$ 使得它们是一个区域的顶点（如图8）. 设此区域的三条边上分别有 $a, b, c$ 个顶点（不含 $A, B, C)$, 设 $A=(-1)^{y} \times(-1)^{z}, B=(-1)^{x} \times(-1)^{z+c+1}, C=(-1)^{x+a+1} \times$
![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-26.jpg?height=280&width=1242&top_left_y=270&top_left_x=384)

图 8

$(-1)^{y+b+1}$. 由于每个其它圆和这个区域的边界有偶数个交点, 因此 $a+b+c$ 为偶数. 故 $A \times B \times C=(-1)^{2 x+2 y+2 z+a+b+c+3}=-1$, 所以 $A, B, C$ 中有奇数个 -1 ,结论2成立.

任意选定一个圆, 将这个圆及与其交点为绿色的圆归为 $A$ 类, 与其交点不为绿色的点归为 $B$ 类. 由结论 1 和结论 2 知, $A$ 类中的两圆交点为绿色, $B$ 类中的两圆交点为绿色, $A$ 类圆与 $B$ 类圆交点不是绿色. 引理成立.

回到原题, 若存在一个有 2061 个绿色点的圆, 不妨设此圆是 $A$ 类的. 因为每两个圆交于两点, 所以该圆至少与 1031 个圆是同一类的, 故至少有 1032 个圆是 $A$ 类, 因此 $B$ 类圆至多 986 个.

由欧拉公式 $V+F-E=2$, 其中 $V, F, E$ 分别为顶点数、面数、边数. 每个圆上有 $2 \times 2017$ 段弧, 故 $E=2 \times 2017 \times 2018$. 每个圆上有 $2 \times 2017$ 个顶点, 每个顶点在两个圆上, 故 $V=\frac{2 \times 2017 \times 2018}{2}=2017 \times 2018$. 因此共有 $F=2+2017 \times 2018$个区域。

下面用两种方法证明此题:

方法 1. 反证法. 假设每个区域都有非绿色的顶点.

将蓝色记为 +1 , 黄色记为 -1 , 为每个点赋值, 值为该点被染的两次颜色对应的数之和（注意这里和引理的证明2中赋值不同）.

对某一个有 $n$ 个顶点的区域, 它的顶点上数字之和是这些点上 $2 n$ 个颜色对应的数字之和, 又因为边界上每条弧的两个端点颜色为一黄一蓝（它们在该弧所在圆上相邻）, 因此这 $2 n$ 个颜色中蓝色和黄色各有 $n$ 个. 故这些顶点总数字和为 0 . 由假设, 这些点不全是 0 , 因此该区域至少有两个非 0 顶点. 故每个区域至少两个非绿色顶点.

设共有 $t$ 个非绿色的顶点, 设有 $m$ 个 $B$ 类圆, 由引理可知 $t=2 m(2018-m)$.由 $m \leq 986$ 可知

$$
t \leq 2 \times 986 \times 1032
$$

又因为共有 $2+2017 \times 2018$ 个区域, 每个区域至少两个非绿色顶点, 每个非绿色交点作为 4 个区域的顶点, 所以

$$
4 t \geq 2 \times(2+2017 \times 2018) .
$$

因此

$$
t>2 \times 986 \times 1032
$$

矛盾.

方法 2. 我们证明：必有一个区域, 它的边界全部由同类圆上的弧组成.

反证法, 假设每个区域的边界都包含但不全是 $B$ 类圆的弧.

设共有 $m$ 个 $B$ 类圆. 设所有区域为 $X_{1}, X_{2}, \cdots, X_{n}(n=2+2017 \times 2018)$.我们称两个 $B$ 类圆的交点为 “ $B$ 交点”, 称 $B$ 类圆上的弧为 “ $B$ 弧”,$A$ 类圆上的弧为 “ $A$ 弧”. 设 $X_{i}$ 的边界上有 $a_{i}$ 段 $B$ 弧, $b_{i}$ 个 $B$ 交点. 由于每个 $B$交点是 4 个区域的顶点, 共有 $m(m-1)$ 个 $B$ 交点, 因此

$$
\sum_{i=1}^{n} b_{i}=4 m(m-1)
$$

每个 $B$ 类圆上有 4034 段弧, 共有 $4034 \times m$ 段 $B$ 弧. 又因为每段弧在两个区域的边界上, 因此

$$
\sum_{i=1}^{n} a_{i}=8068 m
$$

在区域 $X_{i}$ 的边界上, 每个 $B$ 交点是 2 个 $B$ 弧的端点, 而每个 $B$ 弧至多有两个端点是 $B$ 交点, 因此

$$
2 b_{i} \leq 2 a_{i} .
$$

由于 $X_{i}$ 的边界包含但不全是 $B$ 弧, 因此必存在一个 $B$ 弧与一个 $A$ 弧相邻, 则这个 $B$ 弧至多 1 个端点是 $B$ 交点. 因此 (3) 式不取等, 故 $a_{i} \geq b_{i}+1$, 对 $i$ 求和有

$$
\sum_{i=1}^{n} a_{i} \geq \sum_{i=1}^{n} b_{i}+2+2017 \times 2018
$$

由(1),(2),(4)可知

$$
4(2018-m) m \geq 2+2017 \times 2018 \text {. }
$$

又由 $M \leq 986$, 有

$$
4(2018-m) m \leq 4 \times 986 \times 1032<2+2017 \times 2018
$$

与(5)式矛盾.

故存在一个区域, 边界上的弧都在同一类圆上, 故该区域边界上的交点均为
绿色.

注 1. 这道题目中同样有很多性质, 自己做题的过程应该就是不断地得到一个又一个性质的过程. 条件中的 2018 太大了, 自己应该先从两至三个圆入手. 另外,应该可以观察到 2061 是由 2018 加上根号 2018 得到的.

注 2. 做这道题时很重要的一步是发现引理中的结论. 引理的证明 1 中将区域黑白染色的想法来源于这个事实一一平面上任一可以自交的封闭曲线将平面分成的区域都可以二染色, 使得相邻区域颜色不同.

## III. 几何

G 1. 记 $\Gamma$ 为锐角三角形 $A B C$ 的外接圆. $D$ 和 $E$ 分别为线段 $A B$ 和 $A C$上的点, 满足 $A D=A E$. 线段 $B D$ 与 $C E$ 的垂直平分线分别交劣弧 $A B$ 和劣弧 $A C$ 于点 $F$ 与 $G$. 求证 $D E \| F G$.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-28.jpg?height=1014&width=1014&top_left_y=1229&top_left_x=521)

图 9

解答 1. 作 $\angle B A C$ 平分线 $A P$ 交 $\Gamma$ 于点 $P$, 设直线 $G E, F D$ 交 $\Gamma$ 于 $G_{1}, F_{1}$.连结 $A F_{1}, A G_{1}, C G, B F$, 有 $\angle A G_{1} E=\angle A C G=\angle C E G=\angle A E G_{1}$, 故 $A G_{1}=$ $A E$. 同理有 $A F_{1}=A D$.

因此 $A G_{1}=A F_{1}$, 可知 $\overparen{A G}_{1}=\overparen{A F}_{1}$. 又由 $\angle F B A=\angle F D B$, 即 $\overparen{A F}=$
$\overparen{B F}+\overparen{A F}_{1}$, 有 $\overparen{B F}=\overparen{F G}_{1}$, 同理有 $\overparen{C G}=\overparen{G F}_{1}$.

于是 $\overparen{A G}+\overparen{F P}=\overparen{A F_{1}}+\overparen{F_{1} G}+\overparen{F B}+\overparen{B P}=\overparen{A G_{1}}+\overparen{C G}+\overparen{F G_{1}}+\overparen{C P}=$ $\overparen{A F}+\overparen{G P}$, 故 $\overparen{A G}+\overparen{F P}=180^{\circ}$, 所以 $F G \perp A P$. 又 $D E \perp A P$, 故 $F G \| D E$.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-29.jpg?height=862&width=836&top_left_y=580&top_left_x=610)

图 10

解答 2. 在不含 $A$ 点的弧 $C \overparen{B} A$ 上取点 $K$, 弧 $B \overparen{C} A$ 上取点 $J$, 使得 $B J=$ $A D=C K$. 则 $\overparen{B J}=\overparen{C K}$. 又由 $P$ 是 $\overparen{B C}$ 中点, 有 $\overparen{K P}=\overparen{P J}$.

设 $B D, C E$ 中点分别为 $H_{1}, H_{2}$. 则 $A H_{1}=H_{1} B+B J, A H_{2}=H_{2} C+C K$.由阿基米德折弦定理有 $F$ 是 $A \widehat{B} J$ 的中点, $G$ 是 $A \overparen{C} K$ 的中点.

由于 $G$ 是 $A \widehat{C} K$ 的中点, $P$ 是 $\widehat{K} J$ 的中点因此 $\widehat{G P}=\frac{1}{2} \widehat{A J}$, 其中 $\widehat{A J}$ 是不过点 $B$ 的弧. 所以 $\overparen{A F}+\overparen{G P}=\frac{1}{2} A \overparen{B} J+\frac{1}{2} \overparen{A J}=180^{\circ}$, 所以 $F G \perp A P$. 又 $D E \perp A P$,故 $F G \| D E$.

解答 3. 设 $\triangle A B C$ 外心为 $O, F^{\prime}, G^{\prime}$ 分别为 $\overparen{A B}, \overparen{A C}$ 中点, $F^{\prime \prime}, G^{\prime \prime}$ 分别为 $F, G$ 对径点, $M, N, H_{1} . H_{2}$ 分别为 $A B, A C, B D, C E$ 中点. 由于 $\widetilde{A F}^{\prime}+\overparen{P G^{\prime}}=$ $\frac{1}{2} \overparen{A B}+\frac{1}{2} \overparen{B C}+\frac{1}{2} \overparen{A C}=180^{\circ}$, 所以 $F^{\prime} G^{\prime} \perp A P$.

点 $F$ 到直径 $F^{\prime} F^{\prime \prime}$ 的距离为 $H_{1} M=B M-B H_{1}=\frac{1}{2} B A-\frac{1}{2} B D=\frac{1}{2} A D$, 同理点 $G$ 到直径 $G^{\prime} G^{\prime \prime}$ 的距离也为 $\frac{1}{2} A E=\frac{1}{2} A D$, 故 $\widehat{F^{\prime}} F=\widehat{G^{\prime}} G$. 所以 $F^{\prime} G^{\prime} \| F G$,所以 $F G \perp A P$. 又因为 $E D \perp A P$, 故 $E D \| F G$.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-30.jpg?height=925&width=899&top_left_y=263&top_left_x=584)

图 11

注. 这是一道容易的题目. 阿基米德折弦定理的证明是去构造全等三角形.

G 2. 三角形 $A B C$ 中 $A B=A C, M$ 为 $B C$ 中点. $P$ 为满足 $P B<P C$且 $P A$ 平行于 $B C$ 的一点. 点 $X$ 和 $Y$ 分别在直线 $P B$ 和 $P C$ 上, 且满足 $B$ 在线段 $P X$ 上, $C$ 在线段 $P Y$ 上, 且有 $\angle P X M=\angle P Y M$. 求证 $A, P, X, Y$ 四点共圆.

解答 1. 过点 $X$ 作 $P X$ 的垂线交直线 $A M$ 于点 $G$. 由 $G, X, B, M$ 共圆有 $\angle C Y M=\angle B X M=\angle B G M=\angle C G M$, 所以 $C, Y, M, G$ 共圆. 所以 $\angle C Y G=$ $\angle C M A=90^{\circ}$. 所以 $\angle P X G=\angle P Y G=\angle P A G=90^{\circ}$, 故 $P, G, X, Y, A$ 五点共圆.

解答 $\mathbf{2}$. 由三弦定理, $A, P, X, Y$ 共圆等价于

$$
\begin{gathered}
P A \sin \angle B P C+P X \sin \angle A P C=P Y \sin \angle A P B \\
\Leftrightarrow P A \sin \angle B P C+P X \sin \angle P C B=P Y \sin \angle P B C \\
\Leftrightarrow P A \cdot B C+P X \cdot P B=P Y \cdot P C .
\end{gathered}
$$

设 $\triangle B M X$ 和 $\triangle C M Y$ 的外接圆分别为 $\odot O_{1}, \odot O_{2}$, 由题目条件可知: $\odot O_{1}, \odot O_{2}$半径相等, 且关于直线 $A M$ 对称. 故 $P Y \cdot P C-P X \cdot P B=O_{2} P^{2}-O_{1} P^{2}=$

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-31.jpg?height=871&width=754&top_left_y=267&top_left_x=662)

图 12

$2 P A \cdot O_{1} O_{2}=P A \cdot B C$. 故(1)式成立. 所以 $A, P, X, Y$ 共圆.

注. 这也是一道比较容易的题目. 解法一的核心是做出 $\mathrm{G}$ 点, 同时三角计算也有多种方法。

G 3. 给定一个单位圆 $\omega$. 一个三角形组成的集合 $T$ 被称为 “好的”，如果它满足:

1) $T$ 中三角形均以 $\omega$ 为外接圆 ;

2） $T$ 中任意两个三角形没有公共内点.

求所有的正实数 $t$, 使得对任意正整数 $n$, 均存在一组 $n$ 个的 “好的” 三角形, 其中每个的周长均大于 $t$.

解答. $t$ 为所有小于等于 4 的数.

若 $t \leq 4$, 取圆 $\omega$ 的一条直径 $A X_{0}$, 在 $\omega$ 上取点 $X_{n}$, 使得 $\sin \alpha<\frac{1}{2 n}$, 其中 $\alpha$为 $\angle X_{0} A X_{n}$. 取 $\widehat{X_{0} X_{n}}$ 的 $n$ 等分点 $X_{1}, \cdots, X_{n-1}$. 因为 $X_{i} A+X_{i-1} A+X_{i} X_{i-1}>$ $4 \cos \alpha+2 \frac{\sin \alpha}{n}>4 \cos ^{2} \alpha+4 \sin ^{2} \alpha=4$, 所以 $T=\left\{\triangle A X_{i} X_{i-1} \mid i=1,2, \cdots, n\right\}$满足条件.

下面用两种方法说明 $t>4$ 时, 好三角形数量有上界.

方法 1. 设 $t=4+\epsilon$. 设 $T$ 中所有三角形的最短边为 $A_{1} B_{1}, \cdots, A_{n} B_{n}$,则 $A_{i} B_{i}>\epsilon$, 所以 $\widehat{A_{i} B_{i}}>\epsilon$. 又因为 $A_{i} B_{i}$ 是三角形中最短边, 所以 $\widehat{A_{i} B_{i}} \leq 120^{\circ}$

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-32.jpg?height=662&width=711&top_left_y=266&top_left_x=684)

图 13

若 $\widehat{A_{i} B_{i}}$ 与 $\widehat{A_{j} B_{j}}$ 有公共部分, 则必有其中一段弧在另一段弧内部, 不妨设 $\widehat{A_{i} B_{i}}$在 $\widehat{A_{j}} B_{j}$ 内部. 则 $A_{i} B_{i}$ 所在的三角形的顶点 $A_{i}, B_{i}, C_{i}$ 都在弧 $A_{j} B_{j}$ 上, 又因 $\omega$的内接三角形周长小于 6 , 所以 $\epsilon<2$, 故 $A_{i} B_{i}+A_{i} C_{i}+B_{i} C_{i}<3 \epsilon<4+\epsilon$, 矛盾.因此 $\widetilde{A_{1} B_{1}}, \cdots, \widehat{A_{n} B_{n}}$ 互不重合, 故 $n<\frac{2 \pi}{\epsilon}$.

方法 2. 设 $t=4+\epsilon$. 则对 $\mathrm{T}$ 中的三角形 $A B C$, 有 $A B, B C, B C>\epsilon$.则 $\sin \angle A=\frac{B C}{2}>\frac{\epsilon}{2}$, 因此

$$
S_{\triangle A B C}=\frac{1}{2} A B \cdot A C \cdot \sin \angle A>\frac{\epsilon^{3}}{4} .
$$

故 $n<\frac{4 \pi}{\epsilon^{3}}$.

注. 这道题相对难的部分是t大于 4 的证明, 这里有不止一种办法, 但使用面积是最快捷的办法.

G 4. 点 $T$ 在三角形 $A B C$ 内部. 记 $A_{1}, B_{1}, C_{1}$ 分别为 $T$ 关于 $B C, C A, A B$的对称点, $\Omega$ 为三角形 $A_{1} B_{1} C_{1}$ 的外接圆. 设直线 $A_{1} T, B_{1} T, C_{1} T$ 分别与 $\Omega$ 再次交与 $A_{2}, B_{2}, C_{2}$. 求证 $A A_{2}, B B_{2}, C C_{2}$ 与 $\Omega$ 共点.

解答. 设直线 $A A_{2}$ 交圆于另一点 $P$. 注意到点 $A$ 是 $\triangle B_{1} C_{1} T$ 的外心, 所以 $\angle C_{1} A B=\frac{1}{2} \angle T A C_{1}=\angle T B_{1} C_{1}=\angle C_{1} A_{2} B_{2}$. 同理可得 $\angle C_{1} B A=\angle C_{1} B_{2} A_{2}$,所以 $\triangle C_{1} B A \sim \triangle C_{1} B_{2} A_{2}$, 因此有 $\triangle C_{1} B_{2} B \sim \triangle C_{1} A_{2} A$. 故 $\angle P B_{2} C_{1}=\angle P A_{2} C_{1}=$ $\angle B B_{2} C_{1}$, 所以 $B_{2}, B, P$ 共线. 同理可知 $C_{2}, C, P$ 共线.

$A A_{2}, B B_{2}, C C_{2}$ 与 $\Omega$ 都过点 $P$, 因此它们共点.

注. 类似要证很多个对象共点的问题, 一般都是先通过其中两个对象作出这个点, 再证明其它的对象也过这个点. 这个题目想到要做出点 $\mathrm{P}$ 之后就会变得容

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-33.jpg?height=1002&width=974&top_left_y=247&top_left_x=541)

图 14

易许多。

G 5. 三角形 $A B C$ 中, 记其外接圆为 $\omega$, 内心为 $I$. 一条不过 $A, B, C, I$ 的直线 $\ell$ 分别交 $A I, B I, C I$ 于点 $D, E, F$; 线段 $A D, B E, C F$ 的中垂线 $x, y, z$ 决定了一个三角形 $\Theta$. 求证 $\Theta$ 的外接圆与 $\omega$ 相切.

解答. 不妨设点 $E$ 在线段 $D F$ 上 (如图). 令 $X^{\prime}, Y^{\prime}, Z^{\prime}$ 为弧 $\overparen{B C}, \overparen{A C}, \overparen{A B}$中点. 由鸡爪定理 $Y^{\prime} A=Y^{\prime} I, Z^{\prime} A=Z^{\prime} I$, 因此 $Z^{\prime} Y^{\prime}$ 是 $A I$ 的中垂线, 同理 $X^{\prime} Z^{\prime}$是 $B I$ 中垂线, $X^{\prime} Y^{\prime}$ 是 $C I$ 中垂线. 因此

$$
X^{\prime} Z^{\prime}\left\|X Z, X^{\prime} Y^{\prime}\right\| X Y, Y^{\prime} Z^{\prime} \| Y Z
$$

设 $X^{\prime} Z^{\prime}$ 和 $X Z$ 的距离为 $d_{2}, X^{\prime} Y^{\prime}$ 和 $X Y$ 的距离为 $d_{3}, Y^{\prime} Z^{\prime}$ 和 $Y Z$ 的距离为 $d_{1}$.则我们有 $d_{1}=\frac{1}{2} I D, d_{2}=\frac{1}{2} I E, d_{3}=\frac{1}{2} I F$.

取弧 $\widehat{X^{\prime}} Z^{\prime}$ 上一点 $M$ 使得 $\frac{M Z^{\prime}}{M X^{\prime}}=\frac{I D}{I F}$, 过 $M$ 分别做 $Y^{\prime} Z^{\prime}, X^{\prime} Z^{\prime}, X^{\prime} Y^{\prime}$ 的垂线, 垂足为 $H_{1}, H_{2}, H_{3}$. 由西姆松定理 $H_{1}, H_{2}, H_{3}$ 共线.

因为 $\angle M Z^{\prime} H_{1}=\angle M X^{\prime} H_{3}$, 所以 $\triangle M Z^{\prime} H_{1} \sim \triangle M X^{\prime} H_{3}$. 所以

$$
\frac{M H_{1}}{M H_{3}}=\frac{M Z^{\prime}}{M X^{\prime}}=\frac{I D}{I F}
$$

又因为 $M H_{1}, I D$ 都与 $Z^{\prime} Y^{\prime}$ 垂直, 所以 $M H_{1} \| I D$, 同理 $M H_{3}\left\|I F, M H_{2}\right\| I E$.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-34.jpg?height=1128&width=1188&top_left_y=247&top_left_x=434)

图 15

所以 $\triangle M H_{1} H_{3} \sim \triangle I D F$. 所以 $H_{1} H_{3} \| D F$, 易知 $\triangle M H_{1} H_{2} \sim \triangle I D E$. 因此

$$
M H_{1}: M H_{2}: M H_{3}=I D: I E: I F=d_{1}: d_{2}: d_{3} \text {. }
$$

设 $\frac{M H_{1}+d_{1}}{M H_{1}}=t$, 则由 (1),(2)可知 $\triangle X_{1} Y_{1} Z_{1}$ 以点 $M$ 为位似中心放大 $t$ 倍后为 $\triangle X Y Z$. 故它们的外接圆也以 $M$ 为位似中心, 因此两圆相切于点 $M$.

注. 这道题的关键在于发现两个圆关于圆上一个点位似, 后面计算边比例的部分也有一定难度。

G 6. 一个凸四边形 $A B C D$ 满足 $A B \cdot C D=B C \cdot D A$. 四边形内部的一个点 $X$ 满足 $\angle X A B=\angle X C D, \angle X B C=\angle X D A$. 求证 $\angle A X B+\angle C X D=180^{\circ}$.

解答. 做 $\triangle B C X$ 和 $\triangle A D X$ 的外接圆交于点 $L$. 因为 $\angle A L X+\angle C L X=$ $\angle A D X+180^{\circ}-\angle C B X=180^{\circ}$, 所以点 $A, L, C$ 共线.

设 $\frac{D A}{D C}=\frac{B A}{B C}$ 可知点 $D, B$ 在距 $A, C$ 比值为定值的阿波罗尼兹圆上, 设圆心为 $O$. 由阿波罗尼兹圆的性质有 $O A \cdot O C=O D^{2}=O B^{2}$, 故 $\triangle O A D \sim$ $\triangle O D C, \triangle O A B \sim \triangle O B C$. 所以

$$
\angle O D L=\angle O D A+\angle A D L=\angle O C D+180^{\circ}-\angle A X L
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-35.jpg?height=933&width=1536&top_left_y=273&top_left_x=311)

图 16

$$
\angle O B L=\angle O B C-\angle C B L=\angle O A B-\angle C X L .
$$

由上面两式有

$$
\begin{aligned}
\angle O D L+\angle O B L & =\angle O C D+180^{\circ}-\angle A X L+\angle O A B-\angle C X L \\
& =\angle O C D+180^{\circ}-\angle A X C+\angle O A B \\
& =\angle O C D+\angle X C A+\angle X A C+\angle O A B \\
& =\angle X C D+180^{\circ}-\angle X A B \\
& =180^{\circ} .
\end{aligned}
$$

因此 $O, D, B, L$ 共圆. 又因为 $O D=O B$, 所以 $\angle O L D=\angle O L B$, 故 $\angle A X D+$ $\angle B X C=\angle O L D+180^{\circ}-\angle B L O=180^{\circ}$.

注. 这是 2018 年 IMO 的第六题. 这道题开始会比较难入手, 但做出第一步后后面的步骤就相对顺理成章了. 此外, 走向IMO上面还收录了两种证法, 有兴趣的同学可以看一下.

G 7. 锐角三角形 $A B C$ 中 $O$ 为外心, $\Omega$ 为外接圆. 记 $P$ 为 $\Omega$ 上不同于 $A, B, C$ 及它们对径点的一点. 分别记三角形 $A O P, B O P, C O P$ 的外心为 $O_{A}, O_{B}, O_{C}, \ell_{A}, \ell_{B}, \ell_{C}$ 分别为过 $O_{A}, O_{B}, O_{C}$ 而垂直于 $B C, C A, A B$ 的直线. 求证 $\ell_{A}, \ell_{B}, \ell_{C}$ 围成的三角形的外接圆与 $O P$ 相切.

![](https://cdn.mathpix.com/cropped/2024_02_26_24fd4e014e30015926b8g-36.jpg?height=894&width=1219&top_left_y=244&top_left_x=424)

图 17

解答. 不妨设点 $P$ 在 $C$ 的对径点和 $A$ 之间的劣弧上. 设 $\ell_{B}$ 和 $\ell_{C}$ 交于 $D$, $\ell_{A}$ 和 $\ell_{C}$ 交于 $E, \ell_{B}$ 和 $\ell_{A}$ 交于 $F$.

注意到 $\angle O_{B} P O_{A}=\angle O_{B} O O_{A}=\frac{1}{2} \angle B O A=\angle B C A$. 又因为 $O_{B} F \perp$ $A C, O_{A} F \perp B C$, 所以 $\angle O_{B} F O_{A}=\angle B C A$. 因此 $\angle O_{B} P O_{A}=\angle O_{B} F O_{A}$, 故 $O_{B}, O_{A}, F, P$共圆. 有

$$
\angle P F E=\angle P O_{B} O_{A}=\frac{1}{2} \angle P O_{B} O=\angle P B O .
$$

. 同理可得

$$
\begin{aligned}
& \angle P D E=\angle P B O, \\
& \angle P D F=\angle P C O .
\end{aligned}
$$

由(1),(2)式有 $\angle P F E=\angle P D E$, 因此 $P, F, D, E$ 共圆.

又因为 $O_{A} F \perp B C, O_{B} O_{A} \perp O P$, 所以 $180^{\circ}-\angle O_{B} O_{A} F=\measuredangle(C B, O P)=$ $\angle P O B-\angle C B O$, 所以 $\angle O P F=\angle O_{B} P F-\angle O_{B} P O=180^{\circ}-\angle O_{B} O_{A} F-$ $\angle O_{B} P O=(\angle P O B-\angle C B O)-\angle P O O_{B}=\angle P O O_{B}-\angle C B O=\angle P C B-$ $\angle B C O=\angle P C O=\angle O P C$. 又由(3)式有 $\angle O P F=\angle O P C=\angle P D F$, 故 $O P$是 $\triangle D E F$ 外接圆的切线.

注. 这是几何预选题的最后一题, 但笔者自己认为其没有前面的一些题目要难. 一个精确的图会对于做这道题有很大帮助, 因为这能观察出 $\mathrm{P}$ 为切点等性质.
同时这道题目也可以使用复数法去计算得到结论.

## IV. 数论

N 1. 求所有不同正整数对 $(n, k)$, 使得存在正整数 $s$, 使得 $s n$ 和 $s k$ 的因子数相同.

解答. 若 $n \mid k$ 或 $k \mid n$, 显然对任意 $s, s n$ 和 $s k$ 因子数不同. 下证当 $n$ 和 $k$ 互不整除时, 存在 $s$ 使得 $s n, s k$ 因子数相同.

设 $n=p_{1}^{\alpha_{1}} \cdots p_{t}^{\alpha_{t}}, k=p_{1}^{\beta_{1}} \cdots p_{t}^{\beta_{t}}$, 其中 $p_{i}$ 至少是 $n$ 和 $k$ 中一个的质因数, $\alpha_{i}, \beta_{i}$ 为非负整数.

不妨设所有满足 $\alpha_{i}>\beta_{i}$ 的 $i$ 为 $1,2, \cdots, r$, 所有满足 $\alpha_{i}<\beta_{i}$ 的 $i$ 为 $r+$ $1, r+2, \cdots, r+q$.由 $n, k$ 互相不整除可知 $r, q \geq 1$.

取一个足够大的正整数 $M$ 满足 $M>\max \left\{\alpha_{1}, \cdots, \alpha_{t}, \beta_{1}, \cdots, \beta_{t}\right\}$, 令

$$
s=\prod_{i=1}^{r} p_{i}^{(r M+i)\left(\alpha_{i}-\beta_{i}\right)-\alpha_{i}-1} \prod_{i=1}^{q} p_{r+i}^{(q M+i)\left(\beta_{i}-\alpha_{i}\right)-\beta_{i}-1}
$$

则

$$
\begin{aligned}
& s n=\prod_{i=1}^{r} p_{i}^{(r M+i)\left(\alpha_{i}-\beta_{i}\right)-1} \prod_{i=1}^{q} p_{r+i}^{(q M+i-1)\left(\beta_{i}-\alpha_{i}\right)-1} \prod_{i=r+q+1}^{t} p_{i}^{\alpha_{i}}, \\
& s k=\prod_{i=1}^{r} p_{i}^{(r M+i-1)\left(\alpha_{i}-\beta_{i}\right)-1} \prod_{i=1}^{q} p_{r+i}^{(q M+i)\left(\beta_{i}-\alpha_{i}\right)-1} \prod_{i=r+q+1}^{t} p_{i}^{\alpha_{i}} .
\end{aligned}
$$

所以 $s n$ 和 $s k$ 的因子数之比为

$\frac{r M+1}{r M} \cdot \frac{r M+2}{r M+1} \cdots \cdots \frac{r M+r}{r M+r-1} \cdot \frac{q M}{q M+1} \cdot \frac{q M+1}{q M+2} \ldots . \frac{q M+q-1}{q M+q}=\frac{M+1}{M} \cdot \frac{M}{M+1}=1$.故存在满足条件的 $s$.

注. 这是一道简单的问题, 思路相对直接, 结论也较容易猜出.

N 2. 给定正整数 $n>1$. 一个 $n \times n$ 的网格里, 每个格子中写着一个整数. 已知它们满足下面的要求:

1) 格子里的所有数模 $n$ 均余 1 ;
2) 网格中任意一行或一列的数字和模 $n^{2}$ 均余 $n$.

记 $R_{i}$ 为网格第 $i$ 行中数字的乘积, $C_{j}$ 为第 $j$ 列数字的乘积, 求证和 $R_{1}+$ $\cdots+R_{n}$ 与 $C_{1}+\cdots+C_{n}$ 模 $n^{4}$ 同余.
解答 1 . 由条件 1 , 可设第 $i$ 行第 $j$ 列的数为 $a_{i j} \cdot n+1$. 则题中条件 2 等价于 $n \mid \sum_{i=1}^{n} a_{i j}$ 且 $n \mid \sum_{j=1}^{n} a_{i j}$. 有

$$
\begin{aligned}
R_{1}+R_{2}+\ldots+R_{n} \equiv & \sum_{i=1}^{n} \prod_{j=1}^{n}\left(a_{i j} n+1\right) \\
\equiv & n+\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right) n+\frac{1}{2}\left(\sum_{i=1}^{n} \sum_{j \neq k} a_{i j} a_{i k}\right) n^{2} \\
& +\frac{1}{6}\left(\sum_{i=1}^{n} \sum_{j \neq k, k \neq l, l \neq j} a_{i j} a_{i k} a_{i l}\right) n^{3}\left(\bmod n^{4}\right)
\end{aligned}
$$

注意到

$$
\begin{aligned}
& \frac{1}{2} \sum_{i=1}^{n} \sum_{j \neq k} a_{i j} a_{i k} \equiv \frac{1}{2} \sum_{i=1}^{n}\left(\left(\sum_{j=1}^{n} a_{i j}\right)^{2}-\sum_{j=1}^{n} a_{i j}^{2}\right) \\
& \equiv \frac{1}{2} \sum_{i=1}^{n}\left(\sum_{j=1}^{n} a_{i j}\right)^{2}-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}^{2} \\
& \equiv \frac{1}{2}\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right)^{2}-\sum_{i<j}^{n}\left(\sum_{k=1}^{n} a_{i k}\right)\left(\sum_{k=1}^{n} a_{j k}\right)-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}^{2} \\
& \equiv \frac{1}{2}\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right)^{2}-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}^{2}\left(\bmod n^{2}\right) \\
& \frac{1}{6} \sum_{i=1}^{n} \sum_{j \neq k, k \neq l, l \neq j} a_{i j} a_{i k} a_{i l} \equiv \frac{1}{6} \sum_{i=1}^{n} \sum_{k \neq l}\left(\left(\sum_{j=1}^{n} a_{i j}\right) a_{i k} a_{i l}-a_{i k}^{2} a_{i l}-a i k a_{i l}^{2}\right) \\
& \equiv \frac{1}{6} \sum_{i=1}^{n}\left(2 \sum_{k<l}\left(\sum_{j=1}^{n} a_{i j}\right) a_{i k} a_{i l}-2\left(\sum_{k=1}^{n} a_{i k}^{2}\right)\left(\sum_{l=1}^{n} a_{i l}\right)+2 \sum_{k=1}^{n} a_{i k}^{3}\right) \\
& \equiv \frac{1}{6} \sum_{i=1}^{n}\left(6 \sum_{k<l}\left(\sum_{j=1}^{n} a_{i j}\right) a_{i k} a_{i l}-2\left(\sum_{k=1}^{n} a_{i k}\right)^{2}\left(\sum_{l=1}^{n} a_{i l}\right)+2 \sum_{k=1}^{n} a_{i k}^{3}\right) \\
& \equiv \sum_{i=1}^{n} \sum_{k<l}\left(\sum_{j=1}^{n} a_{i j}\right) a_{i k} a_{i l}-\frac{1}{3} \sum_{i=1}^{n}\left(\sum_{k=1}^{n} a_{i k}\right)^{3}+\frac{1}{3} \sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}^{3} \\
& \equiv \sum_{i=1}^{n} \sum_{k<l}\left(\sum_{j=1}^{n} a_{i j}\right) a_{i k} a_{i l}-\frac{1}{3}\left(\sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}\right)^{3}+\sum_{i \neq j}^{n}\left(\sum_{k=1}^{n} a_{i k}\right)^{2}\left(\sum_{k=1}^{n} a_{j k}\right) \\
&+2 \sum_{i<j<l}^{n}\left(\sum_{k=1}^{n} a_{i k}\right)\left(\sum_{k=1}^{n} a_{j k}\right)\left(\sum_{k=1}^{n} a_{l k}\right)+\frac{1}{3} \sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}^{3} \\
&\left.n_{i k}\right)^{3}+\frac{1}{3} \sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}^{3}(\bmod n) .
\end{aligned}
$$

上面俩式的最后一个同余号都是因为 $n \mid \sum_{j=1}^{n} a_{i j}$.
因此有

$$
\begin{aligned}
R_{1}+\ldots+R_{n} \equiv & n+\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right) n+\left(\frac{1}{2}\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right)^{2}-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}^{2}\right) n^{2} \\
& +\left(\frac{1}{3} \sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}^{3}-\frac{1}{3}\left(\sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}\right)^{3}\right) n^{3}\left(\bmod n^{4}\right) .
\end{aligned}
$$

同理可得

$$
\begin{aligned}
C_{1}+\ldots+C_{n} \equiv & +\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right) n+\left(\frac{1}{2}\left(\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}\right)^{2}-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}^{2}\right) n^{2} \\
& +\left(\frac{1}{3} \sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}^{3}-\frac{1}{3}\left(\sum_{i=1}^{n} \sum_{k=1}^{n} a_{i k}\right)^{3}\right) n^{3}\left(\bmod n^{4}\right) .
\end{aligned}
$$

故 $R_{1}+R_{2}+\ldots+R_{n} \equiv C_{1}+C_{2}+\ldots+C_{n}\left(\bmod n^{4}\right)$.

解答 2. 与解答 1 中相同, 设第 $i$ 行第 $j$ 列的数为 $a_{i j} \cdot n+1$, 由题目条件 2 可得 $n \mid \sum_{i=1}^{n} a_{i j}$ 且 $n \mid \sum_{j=1}^{n} a_{i j}$, 因此

$$
R_{i} \equiv \prod_{j=1}^{n}\left(a_{i j} n+1\right) \equiv 1\left(\bmod n^{2}\right)
$$

同理有

$$
C_{i} \equiv 1\left(\bmod n^{2}\right) .
$$

我们设 $C_{i}=B_{i} \cdot n^{2}+1, R_{i}=Q_{i} \cdot n^{2}+1$, 于是

$R_{1} R_{2} \cdots R_{n} \equiv\left(Q_{1}+Q_{2}+\cdots+Q_{n}\right) n^{2}+1 \equiv R_{1}+R_{2}+\cdots+R_{n}-(n-1)\left(\bmod n^{4}\right)$,

$C_{1} C_{2} \cdots C_{n} \equiv\left(B_{1}+B_{2}+\cdots+B_{n}\right) n^{2}+1 \equiv C_{1}+C_{2}+\cdots+C_{n}-(n-1)\left(\bmod n^{4}\right)$.

又因为

$$
R_{1} R_{2} \cdots R_{n}=C_{1} C_{2} \cdots C_{n}
$$

故

$$
R_{1}+R_{2}+\cdots+R_{n} \equiv C_{1}+C_{2}+\cdots+C_{n}\left(\bmod n^{4}\right)
$$

注. 类似的问题一般都不会很难,做题时要多去换元, 把条件都清晰的表示出来, 之后也就基本做完了. 有兴趣的同学可以看一下今年清华金秋营的第六题.

N 3. 数列 $a_{0}, a_{1}, a_{2}, \cdots$ 由 $a_{n}=2^{n}+2^{\left\lfloor\frac{n}{2}\right\rfloor}$ 给出. 求证数列中存在无限多项可以写作另外若干项的和, 也存在无限多项不能写作其它若干项的和.
解答. $k \geq 2$ 时, 因为 $a_{0}+\cdots+a_{2 k-1}=2^{2 k}+2^{k+1}-3$, 而 $a_{2 k}=2^{2 k}+2^{k}$, 所以

$a_{2 k}$ 可以写作另外若干项的和 $\Leftrightarrow a_{0}+a_{1} \cdots+a_{2 k-1}-a_{2 k}=2^{k}-3$ 可以写作数列中若干项的和.注意到 $a_{2 k-2}>2^{k}-3$, 因此若 $2^{k}-3$ 可写作数列中若干项的和, 只能用到 $a_{0}, \cdots, a_{2 k-3}$ 中的数. 故有 $2^{k}-3$ 可写作若干项之和 $\Leftrightarrow a_{0}+a_{1}+\cdots+a_{2 k-3}-\left(2^{k}-3\right)=2^{2 k-2}$ 可写作若干项的和.类似有 $a_{4 k-6}>2^{2 k-2}$, 因此若 $2^{2 k-2}$ 可写作数列中若干项的和, 只能用到 $a_{0}, \cdots, a_{4 k-7}$中的数. 故有 $2^{2 k-2}$ 可写作若干项之和 $\Leftrightarrow a_{0}+a_{1}+\cdots+a_{4 k-7}-2^{2 k-2}=2^{4 k-6}-3$ 可写作若干项的和 $\Leftrightarrow a_{8 k-12}$ 可以写作若干项之和.

综上, 我们有

$$
a_{2 k} \text { 可以写作另外若干项的和 } \Leftrightarrow a_{8 k-12} \text { 可以写作若干项之和. }
$$

由于 $a_{6}=a_{2}+a_{3}+a_{4}+a_{5}, a_{14}$ 不能写作其它项之和(这是因为 $2^{7}-3=125$ 不能写作若干项之和), 由上面的等价关系可以得到对任意正整数 $n, a_{2 \times 4^{n}+4}$ 可以写作其它项之和, $a_{10 \times 4^{n}+4}$ 不能写作若干项之和.

注. 这道题的基本想法是去找递推关系。

N 4. 对于一个正整数列 $a_{1}, a_{2}, \cdots, a_{n}, \cdots$, 已知存在一个正整数 $k$, 使得对任意正整数 $n \geq k$,

$$
\frac{a_{1}}{a_{2}}+\frac{a_{2}}{a_{3}}+\cdots+\frac{a_{n-1}}{a_{n}}+\frac{a_{n}}{a_{1}}
$$

均为整数. 求证存在正整数 $m$, 使得对于任意 $n \geq m$, 均有 $a_{n}=a_{n+1}$.

解答. $\forall n \geq k$ 有

$$
\left(\frac{a_{1}}{a_{2}}+\cdots+\frac{a_{n}}{a_{n+1}}+\frac{a_{n+1}}{a_{1}}\right)-\left(\frac{a_{1}}{a_{2}}+\cdots+\frac{a_{n-1}}{a_{n}}+\frac{a_{n}}{a_{1}}\right)=\frac{a_{n}}{a_{n+1}}+\frac{a_{n+1}}{a_{1}}-\frac{a_{n}}{a_{1}} \in \mathbb{Z},
$$

整理得

$$
a_{1} a_{n+1} \mid a_{1} a_{n}+a_{n+1}\left(a_{n+1}-a_{n}\right) .
$$

用 $v_{p}(l)$ 表示满足 $p^{x} \mid l$ 的最大的 $x$. 下面证明两个结论:

结论 1. 对素数 $p \nmid a_{1}$, 有 $v_{p}\left(a_{n}\right)$ 单调不增.

结论 1 证明.由1式有 $a_{n+1} \mid a_{1} a_{n}$, 故有

$$
v_{p}\left(a_{n+1}\right) \leq v_{p}\left(a_{1} a_{n}\right)=v_{p}\left(a_{n}\right) .
$$

故结论1成立.

结论 2. 对素数 $p \mid a_{1}$, 有 $v_{p}\left(a_{n}\right)$ 在某一项之后为常数.
结论 2 的证明.若 $v_{p}\left(a_{n}\right)$ 单调不增, 显然结论成立.

假设存在 $n \geq k$ 使得 $v_{p}\left(a_{n+1}\right)>v_{p}\left(a_{n}\right)$, 则由(1)式知

$$
v_{p}\left(a_{1} a_{n}+a_{n+1}\left(a_{n+1}-a_{n}\right)\right) \geq v_{p}\left(a_{1} a_{n+1}\right)>v_{p}\left(a_{1} a_{n}\right)
$$

所以有

$$
v_{p}\left(a_{1} a_{n}\right)=v_{p}\left(a_{n+1}\left(a_{n+1}-a_{n}\right)\right)=v_{p}\left(a_{n+1} a_{n}\right) .
$$

故 $v_{p}\left(a_{n+1}\right)=v_{p}\left(a_{1}\right)$.

与上面同理, 若 $v_{p}\left(a_{n+2}\right)>v_{p}\left(a_{n+1}\right)$, 则 $v_{p}\left(a_{n+2}\right)=v_{p}\left(a_{1}\right)=v_{p}\left(a_{n}\right)$, 矛盾.

若 $v_{p}\left(a_{n+2}\right)<v_{p}\left(a_{n+1}\right)$, 则 $v_{p}\left(a_{1} a_{n+1}\right)>v_{p}\left(a_{n+2}\left(a_{n+2}-a_{n+1}\right)\right)$, 故 $v_{p}\left(a_{1} a_{n+1}+a_{n+2}\left(a_{n+2}-a_{n+1}\right)\right)=v_{p}\left(a_{n+2}\left(a_{n+2}-a_{n+1}\right)\right)=v_{p}\left(a_{n+2} a_{n+2}\right)<v_{p}\left(a_{1} a_{n+2}\right)$,这与 $a_{1} a_{n+2} \mid a_{1} a_{n+1}+a_{n+2}\left(a_{n+2}-a_{n+1}\right)$ 矛盾. 故 $v_{p}\left(a_{n+2}\right)=v_{p}\left(a_{n+1}\right)=v_{p}\left(a_{1}\right)$.

同理可得 $v_{p}\left(a_{n+2}\right)=v_{p}\left(a_{n+3}\right)=v_{p}\left(a_{n+4}\right)=\cdots$.

故结论 2 成立.

由结论 1 和结论 2 知, 对任意素数 $p, v_{p}\left(a_{n}\right)$ 在某一项后为常数, 且 $a_{n}$ 的素因子必是 $a_{1}$ 或 $a_{k}$ 的素因子. 故 $a_{n}$ 在某一项后为常数.

注. 这是 IMO 的第五题. 这道题方法相对固定, 做题时应把每步都写清楚.写过程时采用若干个结论的办法会比较清楚.

N 5. 已知正整数 $x, y, z$ 和 $t$ 满足

$$
x y-z t=x+y=z+t
$$

求问 $x y$ 和 $z t$ 能否均为完全平方数?

解答. $x y$ 和 $z t$ 不能均为完全平方数.

反证法. 设 $x y, z t$ 为完全平方数.

若 $x+y$ 为奇数, 则 $x y$ 和 $z t$ 均为偶数, 所以 $x y-z t$ 为偶数, 矛盾.

因此 $x+y$ 为偶数. 设 $x+y=z+t=2 a, \frac{x-y}{2}=b, \frac{z-t}{2}=c$, 不妨设 $b, c \geq 0$.由 $x y-z t>0$ 有 $b<c$.

由原题条件可得 $2 a=c^{2}-b^{2}$. 故 $x y=\left(\frac{c^{2}-b^{2}}{2}\right)^{2}-b^{2}, z t=\left(\frac{c^{2}-b^{2}}{2}\right)^{2}-c^{2}$. 于是

$$
\begin{aligned}
x y z t & =\left(\frac{c^{2}-b^{2}}{2}\right)^{4}-\left(b^{2}+c^{2}\right)\left(\frac{c^{2}-b^{2}}{2}\right)+b^{2} c^{2} \\
& =\left[\left(\frac{c^{2}-b^{2}}{2}\right)^{2}-\frac{b^{2}+c^{2}}{2}\right]^{2}-\left(\frac{c^{2}-b^{2}}{2}\right)^{2} \\
& =N^{2}-a^{2} .
\end{aligned}
$$

其中 $N=a^{2}-\frac{b^{2}+c^{2}}{2}$, 由 $2 a=c^{2}-b^{2}$ 可知 $b, c$ 奇偶性相同, 故 $N \in \mathbb{N}^{+}$. 注意到

$$
\begin{aligned}
N^{2}-a^{2}-(N-1)^{2} & =2 N-1-a^{2} \\
& =2 a^{2}-b^{2}-c^{2}-1-a^{2} \\
& =\left(\frac{c^{2}-b^{2}}{2}\right)^{2}-b^{2}-c^{2}-1 \\
& =(c+b)^{2}\left(\frac{c-b}{2}\right)^{2}-b^{2}-c^{2}-1 \\
& \geq(c+b)^{2}-b^{2}-c^{2}-1 \geq 2 b c-1
\end{aligned}
$$

当 $b c \geq 1$ 时, $N^{2}>N^{2}-a^{2}>(N-1)^{2}$, 故 $x y z t$ 不是完全平方数, 矛盾.

当 $b c=0$ 时, 有 $b=0,4 z t=c^{4}-4 c^{2}=\left(c^{2}-2\right)^{2}-4$ 为完全平方数, 由于相差 4 的两个平方数只有 0 和 4 , 因此 $z t=0$, 矛盾.

故不存在正整数 $x, y, z, t$, 使得 $x y$ 和 $z t$ 均为完全平方数.

注. 这是一个相对比较困难的问题. 解答第四行的换元是比较关键的一步,换元之后的步骤相对固定.

N 6. 对于函数 $f:\{1,2,3, \cdots\} \rightarrow\{2,3, \cdots\}$, 已知对任意正整数对 $m, n$, 均有 $f(m+n) \mid f(m)+f(n)$; 求证存在一个整除所有 $f$ 的取值的正整数 $c>1$.

解答. 引理 $1 .(f(a), f(b)) \mid f((a, b))$.

引理 $\mathbf{1}$ 的证明 当 $m>n$ 时将 $m, m-n$ 代入原式有 $f(m) \mid f(m-n)+f(n)$因此若 $d|f(m), d| f(n)$, 则 $d \mid f(m-n)$.

因此若 $d|f(a), d| f(b)$, 对 $a$ 和 $b$ 进行辗转相除可以得到 $d \mid f((a, b))$. 故引理成立.

引理 2. $\forall k, n \in \mathbb{N}^{+}, f(k n) \leq k f(n)$.

引理 2 的证明对 $k$ 归纳. $k=1$ 时显然成立.

若结论对 $k$ 成立, 则 $f((k+1) n) \mid f(k n)+f(n) \Rightarrow f((k+1) n) \leq f(k n)+$ $f(n) \leq(k+1) f(n)$, 故结论对 $k+1$ 也成立.

由数学归纳原理, 引理成立.

设 $(f(1), f(n))=g(n)$.

将 $m=1$ 代入原式有 $g(n+1)|f(n+1)|(f(n)+f(1))$. 又因为 $g(n+1) \mid f(1)$,所以 $g(n+1) \mid f(n)$. 故 $g(n+1) \mid(f(1), f(n))=g(n)$. 于是 $g(n)$ 从某项起为常数 $c$.

若 $c>1$, 则题目结论成立. 下证 $c \neq 1$ : 若 $c=1$, 设 $\forall n \geq n_{0},(f(1), f(n))=$ 1.
从而若 $a, b>n_{0}$ 且 $(a, b)=1$, 由引理1有 $(f(a), f(b)) \mid f(1)$, 故 $(f(a), f(b)) \mid$ $(f(1), f(a))=1$. 取 $2^{t}>n_{0}$, 则

$$
f\left(2^{t}\right)\left|f\left(2^{t-1}\right)+f\left(2^{t-1}\right)=2 f\left(2^{t-1}\right)\right| 4 f\left(2^{t-2}\right)|\cdots| 2^{t} f(1),
$$

又因为 $\left(f\left(2^{t}\right), f(1)\right)=1$, 所以 $f\left(2^{t}\right) \mid 2^{t} \Rightarrow f\left(2^{t}\right) \leq 2^{t}$.

$\forall n \in \mathbb{N}^{+}$, 记 $n=k 2^{t}+\lambda, 1 \leq \lambda \leq 2^{t}$. 则由引理2有

$$
f(n) \leq k f\left(2^{t}\right)+f(\lambda) \leq k 2^{t}+f(\lambda) \leq n+C,
$$

其中 $C=\max \left\{f(1), f(2), \cdots, f\left(2^{t}\right)\right\}$.

设全体质数为 $p_{1}<p_{2}<\cdots<p_{r}<n_{0}<p_{r+1}<\cdots$, 设 $P$ 为一个大于 $n_{0}^{2}$的质数, 设 $p_{s}$ 为小于 $P(P+1) \cdots(P+C)+P$ 的最大质数, 则 $p_{s+1}-p_{s}>C$且 $p_{s} \geq P>n_{0}^{2}$.

设

$$
q_{i}= \begin{cases}p_{i}^{\alpha_{i}}, & 1 \leq i \leq r \\ p_{i}, & r<i \leq s .\end{cases}
$$

其中 $n_{0} \leq p_{i}^{\alpha_{i}} \leq n_{0}^{2}$, 易知 $n_{0} \leq q_{i} \leq p_{s}$, 且 $q_{1}, \cdots, q_{s}$ 两两互质.

设 $q_{0}=1$, 考察 $f(1), f\left(q_{1}\right), f\left(q_{2}\right), \cdots, f\left(q_{s}\right)$, 由前面的讨论可知它们两两互质. 任取 $f(1)$ 的一个质因子 $u_{0}, f\left(q_{i}\right)$ 的一个质因子 $u_{i}$. 则 $u_{0}, u_{1}, \cdots, u_{s}$是 $s+1$ 个两两不同的质数. 故存在 $0 \leq i \leq s$, 使得 $u_{i} \geq p_{s+1}>p_{s}+C$,故 $f\left(q_{i}\right) \geq u_{i}>p_{s}+C \geq q_{i}+C$,与(1)式矛盾. 故 $c \neq 1$.

综上, 题目结论成立.

注. 这是一个很难的问题. 容易观察到 $f(x)=c x$ 是函数方程的解, 此时 $c=f(1)$ 满足题目条件, 故需要讨论 $f(1)$.

N 7. 给定正整数 $n \geq 2018$, 设 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$ 为两两不同的不超过 $5 n$ 的正整数. 已知数列

$$
\frac{a_{1}}{b_{1}}, \frac{a_{2}}{b_{2}}, \cdots, \frac{a_{n}}{b_{n}}
$$

顺次成为一个等差数列, 求证它是一个常数列.

解答 $\mathbf{1}$. 反证法. 反设公差为 $\frac{c}{d}>0,(c, d)=1$.

当 $i>t$ 时, $\frac{a_{i}}{b_{i}} \geq \frac{t}{d} \Rightarrow b_{i} \leq \frac{a_{i} d}{t}$, 又 $b_{t+1}, \cdots, b_{n}$ 互不相同, 因此 $\frac{5 n d}{t} \geq \frac{a_{i} d}{t} \geq$ $n-t$, 取 $t=\left\lfloor\frac{n}{2}\right\rfloor$ 得到 $d \geq \frac{n^{2}-1}{20 n} \Rightarrow d \geq\left\lceil\frac{n^{2}-1}{20 n}\right\rceil \geq \frac{n}{20}>100$.
$\forall$ 素数幂 $p^{\alpha} \| d$, 若 $p^{\alpha} \nmid b_{i}, p^{\alpha} \nmid b_{j}$, 则

$$
\frac{(i-j) c}{d}=\frac{a_{i}}{b_{i}}-\frac{a_{j}}{b_{j}}=\frac{a_{i} \frac{b_{j}}{\left(b_{i}, b_{j}\right)}-a_{j} \frac{b_{i}}{\left(b_{i}, b_{j}\right)}}{\left[b_{i}, b_{j}\right]} .
$$

由于 $p^{\alpha} \nmid\left[b_{i}, b_{j}\right], p^{\alpha} \mid d$, 所以 $p \mid i-j$. 于是 $b_{1}, b_{2}, \cdots, b_{n}$ 中一切不被 $p^{\alpha}$ 整除的 $b_{i}$的下标 $i$ 模 $p$ 同余. 故不被 $p^{\alpha}$ 整除的 $b_{i}$ 至多 $\left\lceil\frac{n}{p}\right\rceil$ 个.

若 $p^{\alpha} \| d$, 由上面的讨论知 $b_{1}, b_{2}, \cdots, b_{n}$ 中有至少 $n-\left\lceil\frac{n}{p}\right\rceil$ 个数为 $p^{\alpha}$ 的倍数.故 $\left(n-\left\lceil\frac{n}{p}\right\rceil\right) p^{\alpha} \leq 5 n$

$$
\Rightarrow p^{\alpha} \leq \frac{5 n}{n-\frac{n}{p}-1}
$$

1) 当 $p \geq 7$ 时, (1)式左端 $\geq 7$, 右端 $\leq \frac{5 n}{\frac{6}{7} n-1} \leq 6$, 矛盾.
2) 当 $p=5$ 时, 由(1)式可得 $\alpha \leq 1$.
3) 当 $p=3$ 时,由(1)式可得 $\alpha \leq 1$.
4) 当 $p=2$ 时, 由(1)式可得 $\alpha \leq 3$.

故 $d=2^{\alpha_{1}} 3^{\alpha_{2}} 5^{\alpha_{3}}$, 其中 $\alpha_{1} \leq 3, \alpha_{2}, \alpha_{3} \leq 1$, 由 $d>100$ 可知 $d=120$.

此时 $b_{1}, \cdots, b_{n}$ 中不为 $2^{3}$ 的倍数的 $b^{i}$ 模 2 余 $r_{1}$, 不为 3 的倍数的 $b_{i}$ 模 3 余 $r_{2}$,不为 5 的倍数的 $b_{i}$ 模 3 余 $r_{3} .1,2, \cdots, n$ 中满足

$$
\left\{\begin{array}{l}
k \not r_{1}(\bmod 2), \\
k \neq r_{2}(\bmod 3), \\
k \neq r_{3}(\bmod 5) .
\end{array}\right.
$$

的 $k$ 至少有 $1 \times 2 \times 4 \times\left\lfloor\frac{n}{30}\right\rfloor=8 \times\left\lfloor\frac{n}{30}\right\rfloor$ 个数.

故至少 $8 \times\left\lfloor\frac{n}{30}\right\rfloor$ 个 $b_{k}$ 满足 $120 \mid b_{k}$, 而 $1,2, \cdots, 5 n$ 中 120 的倍数仅有 $\left\lfloor\frac{n}{24}\right\rfloor<$ $8 \times\left\lfloor\frac{n}{30}\right\rfloor$ 个, 矛盾. 故公差必为 0.

解答 2. 先证明一个引理:

引理. 对任意正整数 $n, n$ 的正约数个数 $d(n) \leq \sqrt[3]{48 n}$.

引理的证明. 对 $k$ 归纳容易证明 $k+1 \leq \sqrt[3]{8 \times 2^{k}}$, 故 $d\left(2^{k}\right) \leq \sqrt[3]{8 \times 2^{k}}$.

对 $k$ 归纳容易证明 $k+1 \leq \sqrt[3]{3 \times 3^{k}}$, 故 $d\left(3^{k}\right) \leq \sqrt[3]{3 \times 3^{k}}$.

对 $k$ 归纳容易证明 $k+1 \leq \sqrt[3]{\frac{8}{5} \times 5^{k}}$, 故 $d\left(5^{k}\right) \leq \sqrt[3]{\frac{8}{5} \times 5^{k}}$.

对 $k$ 归纳容易证明 $k+1 \leq \sqrt[3]{\frac{8}{7} \times 5^{k}}$, 故 $d\left(7^{k}\right) \leq \sqrt[3]{\frac{8}{7} \times 7^{k}}$.

对 $k$ 归纳容易证明对质数 $p>7, k+1 \leq \sqrt[3]{p^{k}}$, 故 $d\left(p^{k}\right) \leq \sqrt[3]{p^{k}}$.

综上, 设 $n=p_{1}^{k_{1}} \cdots p_{t}^{k_{t}}$, 则 $d(n)=d\left(p_{1}^{k_{1}}\right) \cdots d\left(p_{t}^{k_{t}}\right) \leq \sqrt[3]{8 \times 3 \times \frac{8}{5} \times \frac{8}{7} p_{1}^{k_{1}} \cdots p_{t}^{k_{t}}} \leq$ $\sqrt[3]{48 n}$. 故引理成立.
回到原题, 用反证法. 反设公差为 $\frac{c}{d}>0,(c, d)=1$.

设 $m=\left[b_{1}, d\right], b_{1}=m b_{1}^{\prime}, d=m d^{\prime}$. 因为 $\frac{a_{1}}{b_{1}}-\frac{a_{2}}{b_{2}}=\frac{a_{1} b_{2}-a_{2} b_{1}}{b_{1} b_{2}}=\frac{c}{d}$, 故 $d \mid b_{1} b_{2}$,故 $\left[d, b_{1}\right] \mid b_{1} b_{2}$, 所以 $m=\left[d, b_{1}\right]<25 n^{2}$. 由引理可知

$$
d(m) \leq \sqrt[3]{48 \times 25 n^{2}}<n
$$

注意到 $\frac{a_{i}}{b_{i}}=\frac{a_{1}}{b_{1}}+(i-1) \frac{c}{d}=\frac{a_{1} d^{\prime}+(i-1) c b_{1}^{\prime}}{m}$, 故 $b_{i} \mid m$, 因此 $b_{1}, b_{2}, \cdots, b_{n}$ 都是 $m$的约数. 故 $d(m) \geq n$.与 (1)式矛盾. 故公差为 0 .

注. 尽管这道题的解答不长, 但这是一个很难的问题. 本题的思路很难想, 一开始很可能不知道如何去刻画条件（尽管条件看起来很强）。尽管两种方法看起来有一些差别, 但它们的大致想法是一样的, 就是用两种办法去估计公差 $d$ 的大小.

