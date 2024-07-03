数学新星网 帚教师专栏

www.nsmath.cn/jszl

# 2023 年日本数学奥林匹克决赛试题解析 

王卫华

(《数学竞赛之窗》编辑部, 215000)

2023 年日本数学奥林匹克和往年一样, 在 2 月 11 日举行, 四个小时解答五道试题. 今年的试题难易搭配很科学. 第 $1 、 2$ 题分别为简单的组合和平面几何,难度略低于高联加试第一题, 第 3 题是一个中等难度的代数题, 难度大致与高联加试第三题相当. 第 4 题是一个中等难度的数论题, 难度大致在高联第三题,第 5 题是一个困难的代数问题, 难度大致相当于 CMO 第三、六题.

## I. 试 题

1. 在 $5 \times 5$ 的方格表上, 沿着正方形的边放入若干块由 4 个方格组成的俄罗斯方块(如下图所示). 这些俄罗斯方块可以彼此覆盖, 但它们必须在方格表内. 已知方格表中每一格上覆盖的俄罗斯方块数目不超过 2 , 求方格表中至少被一个俄罗斯方块覆盖的方格数目的最大可能值.

注：俄罗斯方块可以旋转和翻转.



2. 锐角三角形 $A B C$ 中, 三边 $B C, C A, A B$ 的中点分别为 $D, E, F$, 过 $D$分别向边 $A B, A C$ 作垂线, 垂足为 $X$ 和 $Y$, 过 $F$ 且平行于 $X Y$ 的直线和 $D Y$交于点 $P$. 证明: $A D \perp E P$.
3. 已知 $c$ 为非负整数, 求所有无穷正整数数列 $\left\{a_{n}\right\}$, 使得对任意正整数 $n$,恰有 $a_{n}$ 个正整数 $i$ 满足 $a_{i} \leq a_{n+1}+c$.
4. 求所有的正整数 $n$, 使得 $\frac{\varphi(n)^{d(n)}+1}{n}$ 是一个整数且 $\frac{n^{\varphi(n)}-1}{d(n)^{5}}$ 不是整数.

这里, $\varphi(n)$ 表示 $1,2, \cdots, n$ 中与 $n$ 互素的整数的个数, $d(n)$ 表示 $n$ 的正约数的个数.

修订日期: 2021-03-08.

5. 设 $S=\{1,2, \cdots, 3000\}$, 求最大的整数 $X$, 满足: 对任意双射 $f: S \rightarrow S$,存在双射 $g: S \rightarrow S$, 使得

$$
\begin{aligned}
& \sum_{k=1}^{3000}(\max \{f(f(k)), f(g(k)), g(f(k)), g(g(k))\} \\
& \quad-\min \{f(f(k)), f(g(k)), g(f(k)), g(g(k))\}) \geq X
\end{aligned}
$$

## II . 解答与评注

题 1 在 $5 \times 5$ 的方格表上, 沿着正方形的边放入若干块由 4 个方格组成的俄罗斯方块(如下图所示). 这些俄罗斯方块可以彼此覆盖, 但它们必须在方格表内. 已知方格表中每一格上覆盖的俄罗斯方块数目不超过 2 , 求方格表中至少被一个俄罗斯方块覆盖的方格数目的最大可能值.

注：俄罗斯方块可以旋转和翻转.



解 首先给出一个覆盖, 使得恰有 24 个方格被俄罗斯方块覆盖. 如图 1 和图 2 的覆盖方案中, 除正方形中心的方格外, 其余 24 个方格均被覆盖



图 1



图 2

其次证明 25 不可能达到.

如图 3, 将方格表的左下角方格标上坐标 $(0,0)$, 右上角的方格标上坐标 $(4,4)$, 其余各个方格类似坐标系标上坐标, 并将两个坐标均为偶数的方格染为红色, 两个坐标均为奇数的方格染成绿色. 则红格有 9 个, 绿格有 4 个. 注意到每一个俄罗斯方块恰好覆盖一个红格和一个绿格, 则能放入方格表的俄罗斯方块至多有 8 个. 否则, 必有一个绿格被 3 个俄罗斯方块覆盖, 不合题意. 而 8 个
俄罗斯方块不能覆盖 9 个红格, 故至少被一个俄罗斯方块覆盖的方格数目必不为 25 .



图 3

评注 本题涉及俄罗斯方块的覆盖, 用染色与赋值来处理, 是自然的思路.

题 2 锐角三角形 $A B C$ 中, 三边 $B C, C A, A B$ 的中点分别为 $D, E, F$, 过 $D$分别向边 $A B, A C$ 作垂线, 垂足为 $X$ 和 $Y$, 过 $F$ 且平行于 $X Y$ 的直线和 $D Y$交于点 $P$. 证明: $A D \perp E P$.



证明 由 $D X \perp A B, D Y \perp A C$ 得 $A, X, D, Y$ 四点共圆. 又 $X Y / / F P$, 故有

$$
\angle D P F=\angle D Y X=\angle D A X
$$

所以 $A, F, D, P$ 四点共圆.

注意到 $D F / / A C$, 则 $D F \perp D P$, 从而 $F A \perp A P$, 结合 $D E / / A B$ 得 $D E \perp A P$.所以 $E$ 为 $\triangle A D P$ 的垂心, 故 $A D \perp E P$.

评注 本题是一个比较简单的问题, 注意到 $A E \perp D P$, 容易转化为证明 $E$为垂心。
题 3 已知 $c$ 为非负整数, 求所有无穷正整数数列 $\left\{a_{n}\right\}$, 使得对任意正整数 $n$, 恰有 $a_{n}$ 个正整数 $i$ 满足 $a_{i} \leq a_{n+1}+c$.

解 先证 $\left\{a_{n}\right\}$ 无上界. 否则必存在某个 $a_{l}$ 的值在数列中出现无穷多次, 从而使得 $a_{i} \leq a_{l}+c$ 的下标 $i$ 有无穷多个, 矛盾.

其次证明 $\left\{a_{n}\right\}$ 单调不减.

反设存在正整数 $k$ 使 $a_{k}>a_{k+1}$, 由题设知恰有 $a_{k}$ 个 $i$ 使 $a_{i} \leq a_{k+1}+c$, 也恰有 $a_{k+1}$ 个 $i$ 使 $a_{i} \leq a_{k+2}+c$, 所以 $a_{k+1}>a_{k+2}$. 这样从 $a_{k}$ 开始数列严格递减, 这与 $\left\{a_{n}\right\}$ 是无穷正整数数列矛盾.

若存在正整数 $k$ 使 $a_{k}=a_{k+1}$, 由题设知恰有 $a_{k-1}$ 个 $i$ 使 $a_{i} \leq a_{k}+c$, 也恰有 $a_{k}$ 个 $i$ 使 $a_{i} \leq a_{k+1}+c$, 所以 $a_{k-1}=a_{k}$. 于是有 $a_{1}=a_{2}=\cdots=a_{k+1}$. 又数列 $\left\{a_{n}\right\}$ 无上界, 所以存在正整数 $N$, 使得 $a_{1}=a_{2}=\cdots=a_{N}$, 之后数列严格递增. 当 $\left\{a_{n}\right\}$ 严格递增时, 上式中 $N=1$. 故对任意 $n \geq N$, 不超过 $a_{n+1}+c$ 的项只可能为

$$
a_{1}, a_{2}, \cdots, a_{n}, a_{n+1}, a_{n+1}+1, \cdots, a_{n+1}+c
$$

共 $n+c+1$ 个, 所以 $a_{n} \leq n+c+1$.

这表明当 $n \geq N$ 时, $\left\{a_{n}-n\right\}$ 单调不减且有上界 $c+1$, 所以存在整数 $M \geq N$, 使得对任意 $n \geq M$, 数列 $\left\{a_{n}-n\right\}$ 为常数列. 于是对任意 $n \geq M$, 均有 $a_{n+1}=a_{n}+1$, 于是有 $a_{n+1}+1=a_{n+2}, \cdots, a_{n+1}+c=a_{n+1+c}$. 从而对任意 $n \geq M$, 不超过 $a_{n+1}+c$ 的项恰为

$$
a_{1}, a_{2}, \cdots, a_{n}, a_{n+1}, \cdots, a_{n+c+1},
$$

共 $n+c+1$ 个, 所以 $a_{n}=n+c+1$.

最后我们证明, 对任意正整数 $n$, 均有 $a_{n}=n+c+1$. 只需证明, 对任意 $t=0,1, \cdots, M-1$, 均有

$$
a_{M-t}=a_{M}-t=(M-t)+c+1 .
$$

我们对 $t$ 归纳证明. 当 $t=0$ 时, 结论显然成立. 设结论对 $\leq t$ 的非负整数均成立, 则有

$$
a_{M-t}+c=(M-t)+c+1+c=(M-t+c)+c+1=a_{M-t+c} .
$$

又由题设, 恰有 $a_{M-(t+1)}$ 个 $i$ 使得

$$
a_{i} \leq a_{M-(t+1)+1}+c=a_{M-t}+c=a_{M-t+c},
$$

故必有 $a_{M-(t+1)}=M-t+c=M-(t+1)+c+1$, 也即结论对 $t+1$ 也成立.
由数学归纳法知, (1) 对任意 $t=0,1, \cdots, M-1$ 均成立.

综上, 对任意正整数 $n$, 均有 $a_{n}=n+c+1$, 容易验证知该数列满足题设要求.

评注 由题设不难发现数列 $\left\{a_{n}\right\}$ 是单调递增的, 进而得到 $a_{n}=n+c+1$.但是本题如何能够将证明过程书写清楚, 是不容易的. 这里我们从 $n$ 充分大的情况开始, 得出 $a_{n}$ 表达式, 进而向下归纳出结果.

题 4 求所有的正整数 $n$, 使得 $\frac{\varphi(n)^{d(n)}+1}{n}$ 是一个整数且 $\frac{n^{\varphi(n)}-1}{d(n)^{5}}$ 不是整数.

这里, $\varphi(n)$ 表示 $1,2, \cdots, n$ 中与 $n$ 互素的整数的个数, $d(n)$ 表示 $n$ 的正约数的个数.

解 显然 $n \neq 1$. 当 $n=2$ 时,

$$
\frac{\varphi(2)^{d(2)}+1}{2}=\frac{1^{2}+1}{2}=1, \frac{2^{\varphi(2)}-1}{d(2)^{5}}=\frac{2^{1}-1}{2^{5}}=\frac{1}{32},
$$

满足题设要求.

下设 $n \geq 3$, 设 $n=p_{1}^{r_{1}} p_{2}^{r_{2}} \cdots p_{k}^{r_{k}}$ 为 $n$ 的素因子分解式. 则有

$$
\varphi(n)=\left(p_{1}-1\right) p_{1}^{r_{1}-1}\left(p_{2}-1\right) p_{2}^{r_{2}-1} \cdots\left(p_{k}-1\right) p_{k}^{r_{k}-1}
$$

由 $n \mid \varphi(n)^{d(n)}+1$ 知 $(n, \varphi(n))=1$, 从而对任意 $1 \leq i \leq k$, 均有 $r_{i}=1$. 所以

$$
\begin{aligned}
n & =p_{1} p_{2} \cdots p_{k} \\
\varphi(n) & =\left(p_{1}-1\right)\left(p_{2}-1\right) \cdots\left(p_{k}-1\right) \\
d(n) & =(1+1)^{k}=2^{k}
\end{aligned}
$$

由 $\varphi(n)$ 为偶数知 $n$ 必为奇数.

由 $n \mid \varphi(n)^{d(n)}+1$ 知, 对每个 $p_{i}$ 均有 $\varphi(n)^{2^{k}} \equiv-1\left(\bmod p_{i}\right)$, 于是有 $\varphi(n)^{2^{k+1}} \equiv 1\left(\bmod p_{i}\right)$. 设 $t$ 是使得 $\varphi(n)^{t} \equiv 1\left(\bmod p_{i}\right)$ 成立的最小正整数, 则 $t \mid 2^{k+1}$, 且 $t \nmid 2^{k}$, 从而必有 $t=2^{k+1}$. 又由费马小定理知 $\varphi(n)^{p_{\mathrm{i}}-1} \equiv 1\left(\bmod p_{i}\right)$,所以 $2^{k+1} \mid p_{i}-1$. 则

$$
n-1=\prod_{i=1}^{k} p_{i}-1 \equiv \prod_{i=1}^{k} 1-1 \equiv 0 \quad\left(\bmod 2^{k+1}\right)
$$

于是有 $\operatorname{ord}_{2}(n-1) \geq k+1$, 且 $\operatorname{ord}_{2}(\varphi(n)) \geq k(k+1)$.

引理 若 $x(\geq 3)$ 为正奇数, $y$ 为正整数, 则

$$
\operatorname{ord}_{2}\left(x^{y}-1\right) \geq \operatorname{ord}_{2}(x-1)+\operatorname{ord}_{2} y .
$$

证明 设 $y=2^{v} \cdot s$, 其中 $v$ 为非负整数, $s$ 为正奇数, 则有

$$
\begin{aligned}
x^{y}-1 & =\left(x^{s}-1\right) \prod_{i=0}^{v-1}\left(x^{2^{i} \cdot s}+1\right) \\
& =(x-1)\left(x^{s-1}+\cdots+x+1\right) \prod_{i=0}^{v-1}\left(x^{2^{i} \cdot s}+1\right) .
\end{aligned}
$$

注意到 $x$ 为奇数, 对任意 $i$, 均有 $\operatorname{ord}_{2}\left(x^{2^{i} \cdot s}+1\right) \geq 1$, 所以

$$
\operatorname{ord}_{2}\left(x^{y}-1\right) \geq \operatorname{ord}_{2}(x-1)+v=\operatorname{ord}_{2}(x-1)+\operatorname{ord}_{2} y
$$

引理得证.

回到原题，由题设及引理知

$$
5 k>\operatorname{ord}_{2}\left(n^{\varphi(n)}-1\right) \geq \operatorname{ord}_{2}(n-1)+\operatorname{ord}_{2}(\varphi(n)) \geq(k+1)+k(k+1),
$$

结合 $k$ 为正整数, 得 $k=1$ 或 2 .

若 $k=1$, 则 $\varphi(n)=n-1, d(n)=2$, 则

$$
\frac{\varphi(n)^{d(n)}+1}{n}=\frac{(n-1)^{2}+1}{n}=n-2+\frac{2}{n},
$$

不为整数.

若 $k=2,(k+1)+k(k+1)=9,5 k=10$, 故必有 $\operatorname{ord}_{2}(n-1)=3$, $\operatorname{ord}_{2}(\varphi(n))=6$. 于是

$$
\operatorname{ord}_{2}\left(p_{1}-1\right)=\operatorname{ord}_{2}\left(p_{2}-1\right)=3=\operatorname{ord}_{2}(n-1) \text {. }
$$

故必有 $p_{1} \equiv p_{2} \equiv 9(\bmod 16)$, 但是, 此时有 $n-1=p_{1} p_{2}-1 \equiv 0(\bmod 16)$, 矛盾. 从而 $n \geq 3$ 时, 不存在满足要求的 $n$.

综上, 满足题设要求的 $n=2$.

评注 本题是用 LTE 引理的一个典型问题. 这里我们给出了引理的证明. 阶和 LTE 引理, 再加上不等式控制, 是解决这一类整除性的问题的基本方法.

题 $\mathbf{5}$ 设 $S=\{1,2, \cdots, 3000\}$, 求最大的整数 $X$, 满足对任意双射 $f: S \rightarrow S$,存在双射 $g: S \rightarrow S$, 使得

$$
\begin{aligned}
& \sum_{k=1}^{3000}(\max \{f(f(k)), f(g(k)), g(f(k)), g(g(k))\} \\
& \quad-\min \{f(f(k)), f(g(k)), g(f(k)), g(g(k))\}) \geq X
\end{aligned}
$$

## 解 我们记

$$
X_{\max }(f, g)=\sum_{k=1}^{3000} \max \{f(f(k)), f(g(k)), g(f(k)), g(g(k))\}
$$

$$
X_{\min }(f, g)=\sum_{k=1}^{3000} \min \{f(f(k)), f(g(k)), g(f(k)), g(g(k))\}
$$

并记 $X(f, g)=X_{\max }(f, g)-X_{\min }(f, g)$.

首先, 我们证明 $X \leq 6000000$.

注意到定义在 $S$ 上且在 $S$ 上取值的双射的复合仍为双射. 我们考虑 $S$ 上的双射 $f: S \rightarrow S$, 使得对任意 $x \in S$, 均有 $f(x)=x$.

因为 $f \circ g=g \circ f$, 且三个映射 $f \circ f, f \circ g, g \circ g$ 均为双射, 则对任意 $a \in S$,使得 $f(f(x))=a, f(g(x))=a$ 和 $g(g(x))=a$ 的 $x$ 都恰有一个. 因此, 最多有 3 个 $x$, 使得

$$
\max \{f(f(x)), f(g(x)), g(f(x)), g(g(x))\}=a
$$

也最多有 3 个 $x$, 使得

$$
\min \{f(f(x)), f(g(x)), g(f(x)), g(g(x))\}=a .
$$

所以

于是

$$
\begin{aligned}
& X_{\max }(f, g) \leq 3 \times 3000+3 \times 2999+\cdots+3 \times 2001=\sum_{k=2001}^{3000} 3 k, \\
& X_{\min }(f, g) \geq 3 \times 1+3 \times 2+\cdots+3 \times 1000=\sum_{k=1}^{1000} 3 k
\end{aligned}
$$

$$
X(f, g) \leq \sum_{k=2001}^{3000} 3 k-\sum_{k=1}^{1000} 3 k=6000000
$$

因此, 所求 $X \leq 6000000$.

其次, 我们证明 $X=6000000$ 满足题设要求.

我们定义集合

$S_{1}=\{1,2, \cdots, 1000\}, S_{2}=\{1001,1002, \cdots, 2000\}, S_{3}=\{2001,2002, \cdots, 3000\}$.

且对 $a, b \in\{1,2,3\}$, 定义 $S_{a, b}=\left\{x \in S_{a} \mid f(x) \in S_{b}\right\}$, 并记 $n_{a, b}=\left|S_{a, b}\right|$. 那么,对任意 $x \in S$, 恰有一个 $a, b \in\{1,2,3\}$ 组, 使得 $x \in S_{a, b}$, 我们称 $S_{a, b}$ 为 $x$ 所属的块.

引理 对 $S$ 上的任意双射 $f$, 可以将 $S$ 中的元素划分成 1000 个三元组, 满足以下要求:

- $S$ 中的每个元素都恰属于一个组;
- 设 $a_{1}, a_{2}, a_{3}$ 为同一组中从小到大的三个元素, 则 $a_{1} \in S_{1}, a_{2} \in S_{2}, a_{3} \in S_{3}$,且 $f\left(a_{1}\right), f\left(a_{2}\right), f\left(a_{3}\right)$ 中各有一个属于集合 $S_{1}, S_{2}, S_{3}$.
证明 在满足引理要求的划分中, 每个三元组中元素所属块的组合只有以下六种:

$$
\begin{array}{lll}
\left\{S_{1,1}, S_{2,2}, S_{3,3}\right\}, & \left\{S_{1,1}, S_{2,3}, S_{3,2}\right\}, & \left\{S_{1,2}, S_{2,3}, S_{3,1}\right\}, \\
\left\{S_{1,2}, S_{2,1}, S_{3,3}\right\}, & \left\{S_{1,3}, S_{2,1}, S_{3,2}\right\}, & \left\{S_{1,3}, S_{2,2}, S_{3,1}\right\}
\end{array}
$$

设划分后这六种组合的个数分别为 $A_{1}, B_{1}, A_{2}, B_{2}, A_{3}, B_{3}$.

我们只需证明存在非负整数组 $\left(A_{1}, B_{1}, A_{2}, B_{2}, A_{3}, B_{3}\right)$ 满足

$$
\begin{array}{lll}
A_{1}+B_{1}=n_{1,1}, & A_{2}+B_{2}=n_{1,2}, & A_{3}+B_{3}=n_{1,3}, \\
A_{3}+B_{2}=n_{2,1}, & A_{1}+B_{3}=n_{2,2}, & A_{2}+B_{1}=n_{2,3}, \\
A_{2}+B_{3}=n_{3,1}, & A_{3}+B_{1}=n_{3,2}, & A_{1}+B_{2}=n_{3,3} .
\end{array}
$$

即可知引理成立.

由对称性, 不妨设 9 个整数 $n_{a, b}(a, b \in\{1,2,3\})$ 中, $n_{1,1}$ 最小. 取

$$
\left(A_{1}, B_{1}, A_{2}, B_{2}, A_{3}, B_{3}\right)=\left(n_{1,1}, 0, n_{2,3}, n_{3,3}-n_{1,1}, n_{3,2}, n_{2,2}-n_{1,1}\right) .
$$

由 $n_{1,1}$ 的最小性知上式中各数均为非负整数, 且显然满足 (2) 中的第 $1,5,6,8,9$式.

注意到, 对任意 $a \in\{1,2,3\}$, 均有

$$
\begin{aligned}
& n_{a, 1}+n_{a, 2}+n_{a, 3}=\left|S_{a}\right|=1000, \\
& n_{1, a}+n_{2, a}+n_{3, a}=\left|\left\{x \in S \mid f(x) \in S_{a}\right\}\right|=1000 .
\end{aligned}
$$

则可得

$$
\begin{aligned}
A_{2}+B_{2} & =n_{2,3}+n_{3,3}-n_{1,1} \\
& =\left(n_{1,3}+n_{2,3}+n_{3,3}\right)-\left(n_{1,1}+n_{1,2}+n_{1,3}\right)+n_{1,2}=n_{1,2}, \\
A_{3}+B_{3} & =n_{3,2}+n_{2,2}-n_{1,1} \\
& =\left(n_{1,2}+n_{2,2}+n_{3,2}\right)-\left(n_{1,1}+n_{1,2}+n_{1,3}\right)+n_{1,3}=n_{1,3}, \\
A_{3}+B_{2} & =n_{3,2}+n_{3,3}-n_{1,1} \\
& =\left(n_{3,1}+n_{3,2}+n_{3,3}\right)-\left(n_{1,1}+n_{2,1}+n_{3,1}\right)+n_{2,1}=n_{2,1}, \\
A_{2}+B_{3} & =n_{2,3}+n_{2,2}-n_{1,1} \\
& =\left(n_{2,1}+n_{2,2}+n_{2,3}\right)-\left(n_{1,1}+n_{2,1}+n_{3,1}\right)+n_{3,1}=n_{3,1} .
\end{aligned}
$$

从而也满足 (2) 中的第 $2,3,4,7$ 式. 引理得证.

在满足引理的划分下, 定义 $S$ 上的双射 $h$, 使得对每个三元组中从小到大的三个元素 $a_{1}, a_{2}, a_{3}$, 均有

$$
h\left(a_{1}\right)=a_{2}, h\left(a_{2}\right)=a_{3}, h\left(a_{3}\right)=a_{1} .
$$

令 $g=h \circ f$, 下证: $X(f, g) \geq 6000000$.

由 $h$ 的定义知, 若 $x \in S_{1}$, 则 $h(x) \in S_{2}$, 若 $x \in S_{2}$, 则 $h(x) \in S_{3}$, 若 $x \in S_{3}$, 则 $h(x) \in S_{1}$. 考虑同一三元组中三个数 $a_{1} \in S_{1}, a_{2} \in S_{2}, a_{3} \in S_{3}$. 对 $i \in\{1,2,3\}$, 记 $k_{i}=f^{-1}\left(a_{i}\right)$, 则有

$$
g\left(k_{i}\right)=h\left(f\left(k_{i}\right)\right)=h\left(a_{i}\right)=a_{i+1} .
$$

其中 $a_{4}=a_{1}$. 从而有

$$
\begin{aligned}
& \max \left\{f\left(f\left(k_{i}\right)\right), f\left(g\left(k_{i}\right)\right), g\left(f\left(k_{i}\right)\right), g\left(g\left(k_{i}\right)\right)\right\} \\
& =\max \left\{f\left(a_{i}\right), f\left(a_{i+1}\right), g\left(a_{i}\right), g\left(a_{i+1}\right)\right\} .
\end{aligned}
$$

设 $f\left(a_{1}\right), f\left(a_{2}\right), f\left(a_{3}\right)$ 按从小到大的顺序分别等于 $F_{1}, F_{2}, F_{3}$, 由引理知 $F_{1} \in S_{1}, F_{2} \in S_{2}, F_{3} \in S_{3}$. 又由 $g=h \circ f$ 得 $h\left(F_{1}\right) \in S_{2}, h\left(F_{2}\right) \in S_{3}$, $h\left(F_{3}\right) \in S_{1}$. 故有

$$
\begin{aligned}
& \sum_{i=1}^{3} \max \left\{f\left(f\left(k_{i}\right)\right), f\left(g\left(k_{i}\right)\right), g\left(f\left(k_{i}\right)\right), g\left(g\left(k_{i}\right)\right)\right\} \\
&= \max \left\{F_{1}, F_{2}, h\left(F_{1}\right), h\left(F_{2}\right)\right\}+\max \left\{F_{2}, F_{3}, h\left(F_{2}\right), h\left(F_{3}\right)\right\} \\
&+\max \left\{F_{3}, F_{1}, h\left(F_{3}\right), h\left(F_{1}\right)\right\} \\
&= h\left(F_{2}\right)+\max \left\{F_{3}, h\left(F_{2}\right)\right\}+F_{3} \\
& \geq h\left(F_{2}\right)+\frac{1}{2}\left(F_{3}+h\left(F_{2}\right)\right)+F_{3}=\frac{3}{2} F_{3}+\frac{3}{2} h\left(F_{2}\right) .
\end{aligned}
$$

考虑所有的 1000 个三元组, 在 $a_{1}, a_{2}, a_{3}$ 中, $S$ 中的每个元素恰出现一次, 在 $k_{1}, k_{2}, k_{3}$ 中, $S$ 中的每个元素也恰出现一次. 注意到, $f$ 和 $h$ 是双射, 则 $S_{3}$ 中每个元素在 $F_{3}$ 和 $h\left(F_{2}\right)$ 中都各出现一次. 将 1000 个三元组对应的式子 (3) 求和得

$$
X_{\max }(f, g) \geq \frac{3}{2} \sum_{k=2001}^{3000} k+\frac{3}{2} \sum_{k=2001}^{3000} k=\sum_{k=2001}^{3000} 3 k .
$$

同理可得 $X_{\min }(f, g) \leq \sum_{k=1}^{1000} 3 k$. 从而有

$$
X(f, g) \geq \sum_{k=2001}^{3000} 3 k-\sum_{k=1}^{1000} 3 k=6000000
$$

综上, 所求的 $X$ 的最大值为 6000000 .

评注 本题取 $f(x)=x$, 得出最大值 6000000 , 这一半不难得到的. 但是另一半的证明是相当困难的. 我们采用划分的想法，将集合 $S$ 划分成 1000 个三元组, 以保证每一个三元组对应的 $X_{\max }(f, g)$ 尽可能的大, 而其对应的 $X_{\min }(f, g)$尽可能的小.

