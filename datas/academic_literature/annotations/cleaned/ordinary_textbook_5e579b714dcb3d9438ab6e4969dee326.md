# 2019 年土耳其数学奥林匹克（决赛）试题解答与评析 

侯傑夫王琇 尹顺

(湖南师范大学附属中学, 410006)

指导教师: 汤礼达

2019 年土耳其数学奥林匹克 (决赛) 的六道试题最近出炉, 这是一套高质量的试题, 问题新颖且优雅. 其中, 题 1,2,4 是简单题, 题 3,5,6 是中等难度, 前 5 题是不错的联赛训练题. 本文给出这六道题的解答及一些评注, 不当之处敬请指正.

## I. 试 题

1. 设正实数 $a, b, c$ 满足

$$
(\sqrt{a b}-1)(\sqrt{b c}-1)(\sqrt{c a}-1)=1
$$

则六个数

$$
a-\frac{b}{c}, a-\frac{c}{b}, b-\frac{c}{a}, b-\frac{a}{c}, c-\frac{a}{b}, c-\frac{b}{a}
$$

中至多有几个数大于 1 ?

2. 对正整数 $m$, 用 $d(m)$ 表示 $m$ 的正约数个数. 给定奇数 $k$, 证明: 存在一个严格递增的正整数等差数列 $a_{1}, a_{2}, \cdots, a_{2019}$, 使得 $k$ 与 $d\left(a_{1}\right) d\left(a_{2}\right) \cdots d\left(a_{2019}\right)$互素.
3. 校园里有 2019 名学生, 每名学生加入了一个或多个社团, 每个社团恰有 12 名社团干部. 一群学生能够开展某个社团的活动, 当且仅当这些学生都来自该社团, 且这个社团的干部都在这些学生中.

现已知对任意一群至少 12 人的学生, 他们恰能开展唯一一个社团的活动,
这是否可能? 如果可能, 求恰有 27 人加入的社团的所有可能数目.

4. 在 $\triangle A B C$ 中, $A B=A C . M$ 为劣弧 $A C$ 上一点, $B M$ 与 $A C$ 相交于点 $E, \angle B M C$ 的平分线与 $B C$ 相交于点 $F$. 若 $\angle A F B=\angle C F E$, 证明: $\triangle A B C$ 是等边三角形.



5. 设函数 $f:\{1,2 \cdots 2019\} \rightarrow\{-1,1\}$ 满足对任意 $1 \leq k \leq 2019$, 都存在 $1 \leq l \leq 2019$ 使得

$$
\sum_{i:(i-k)(l-i) \geq 0} f(i) \leq 0 .
$$

求 $\sum_{i=1}^{2019} f(i)$ 的最大值.

6. 对于整数 $n \geq 3$, 整数 $a$ 称为 $n$-好的, 若存在正整数 $d$, 使得

$$
n \mid a^{d}-1, n \nmid a^{d-1}+a^{d-2}+\cdots+1 .
$$

设 $f(n)$ 是集合 $\{a \mid 0<a<n,(a, n)=1$, 但 $a$ 不是 $n-$ 好的 $\}$ 的元素个数. 求 $f(n)(n \geq 3)$ 的最小值, 并求出所有 $n(\geq 3)$ 使得 $f(n)$ 取到该最小值.

## II. 解答与评注

1. 设正实数 $a, b, c$ 满足

$$
(\sqrt{a b}-1)(\sqrt{b c}-1)(\sqrt{c a}-1)=1,
$$

则六个数

$$
a-\frac{b}{c}, a-\frac{c}{b}, b-\frac{c}{a}, b-\frac{a}{c}, c-\frac{a}{b}, c-\frac{b}{a}
$$

中至多有几个数大于 1 ?

解 至多 4 个数大于 1 .
一方面, 令 $a=b=\frac{5}{4}, c=\frac{36}{5}$ 满足条件, 所说六个数依次为

$$
\frac{155}{144},-\frac{451}{100},-\frac{451}{100}, \frac{155}{144}, \frac{31}{5}, \frac{31}{5}
$$

其中有 4 个数大于 1 .

另一方面, 假设所说的数中至少五个大于 1 , 则 $a, b, c>1$, 注意到

$$
\begin{aligned}
& \sqrt{a b}-1 \geq \sqrt{(a-1)(b-1)}, \\
& \sqrt{b c}-1 \geq \sqrt{(b-1)(c-1)}, \\
& \sqrt{c a}-1 \geq \sqrt{(c-1)(a-1)} .
\end{aligned}
$$

相乘得

$$
(\sqrt{a b}-1)(\sqrt{b c}-1)(\sqrt{c a}-1) \geq(a-1)(b-1)(c-1) .
$$

不妨设 $a-\frac{b}{c}, b-\frac{c}{a}, c-\frac{a}{b}$ 都大于 1 , 则

$$
a-1>\frac{b}{c}, b-1>\frac{c}{a}, c-1>\frac{a}{b} .
$$

相乘得

$$
(a-1)(b-1)(c-1)>1,
$$

(1) 与 (2) 矛盾! 因此至多 4 个数大于 1 .

评注 令 $a=b$ 代入条件以寻找例子, 对 Aczel 不等式熟悉的话容易导出 (1)式, 与结论相比对则可得到以上证明. 本题可以用分类讨论来做.

2. 对正整数 $m$, 用 $d(m)$ 表示 $m$ 的正约数个数. 给定奇数 $k$, 证明: 存在一个严格递增的正整数等差数列 $a_{1}, a_{2}, \cdots, a_{2019}$, 使得 $k$ 与 $d\left(a_{1}\right) d\left(a_{2}\right) \cdots d\left(a_{2019}\right)$互素.

证法 1 记 $d=2019$ !. 先证明 2019 个数 $1+d, 1+2 d, \cdots, 1+2019 d$ 两两互素.

假设存在素数 $p$ 以及 $1 \leq i<j \leq 2019$ 使得 $p|1+i d, p| 1+j d$, 则 $p$ 与 $d$互素, 且 $p \mid(1+j d)-(1+i d)=(j-i) d$, 故 $p \mid j-i$. 但 $0<j-i \leq 2019$, 故 $(j-i) \mid d$, 导致 $p \mid d$, 矛盾! 因此, $1+i d(1 \leq i \leq 2019)$ 两两互素.

设 $k$ 的全体素因子为 $q_{1}, q_{2}, \cdots, q_{t}$, 对任意素数

$$
p \mid(1+d)(1+2 d) \cdots(1+2019 d)
$$

由上述, 存在唯一的 $1 \leq i \leq 2019$ 使 $p \mid 1+i d$, 设 $p$ 在 $1+i d$ 中的幂次为 $e_{p}$. 因
为 $k$ 是奇数, 故 $q_{s} \geq 3$, 从而存在整数 $h_{p, s}$, 使得

$$
1+h_{p, s} \not \equiv 0\left(\bmod q_{s}\right), 1+h_{p, s}+e_{p} \not \equiv 0\left(\bmod q_{s}\right)(1 \leq s \leq t)
$$

因为 $q_{1}, q_{2}, \cdots, q_{t}$ 两两互素, 故由中国剩余定理, 存在正整数 $h_{p}$ 满足

$$
h_{p} \equiv h_{p, s}\left(\bmod q_{s}\right)(1 \leq s \leq t) .
$$

令

$$
A=\prod_{\text {素数 } p \mid(1+d) \cdots(1+2019 d)} p^{h_{p}}, a_{i}=A(1+i d)(1 \leq i \leq 2019),
$$

则对任意 $a_{i}(1 \leq i \leq 2019)$,

$$
d\left(a_{i}\right)=\prod_{\text {素数p } \mid a_{i}}\left(1+v_{p}\left(a_{i}\right)\right)\left(v_{p}(m) \text { 表示 } m \text { 中素数 } p \text { 的幂次 }\right) .
$$

若 $p \nmid 1+i d$, 则 $v_{p}\left(a_{i}\right)=v_{p}(A)=h_{p}$, 而 $1+h_{p}$ 与 $q_{s}(1 \leq s \leq t)$ 互素.

若 $p \mid 1+i d$, 则 $v_{p}\left(a_{i}\right)=v_{p}(A)+e_{p}=h_{p}+e_{p}$, 而 $1+h_{p}+e_{p}$ 与 $q_{s}(1 \leq s \leq t)$互素.

因此 $d\left(a_{i}\right)$ 与 $k$ 互素, $a_{1}, a_{2}, \cdots, a_{2019}$ 满足要求.

证法 2 我们证明更强的结论:

存在一个严格递增的正整数等差数列 $a_{1}, a_{2}, \cdots, a_{2019}$, 使得

$$
d\left(a_{1}\right) d\left(a_{2}\right) \cdots d\left(a_{2019}\right)
$$

是 2 的幂. 这等价于证明 $a_{1}, a_{2}, \cdots, a_{2019}$ 无平方因子.

为此, 考虑数列 $\{1+n d\}_{n \in \mathbb{N}}$, 其中 $d=2019$ !.

记 $f(N)$ 为 $1+d, 1+2 d, \cdots, 1+N d$ 中有平方因子的数的个数. 对素数 $p$, 记 $f_{p}(N)$ 为 $1+d, 1+2 d, \cdots, 1+N d$ 中 $p^{2}$ 倍数的个数, 同时考虑到对于 $p^{2} \mid 1+i d, i \leq N$, 有 $p^{2} \leq 1+N d$, 从而 $p \leq \sqrt{1+N d}$. 故

$$
f(N) \leq \sum_{\text {素数p: } p \leq \sqrt{1+N d}} f_{p}(N) .
$$

明显地, 由于 $(1+n d, 2019 !)=1$, 从而对素数 $p \leq 2019$ 有 $f_{p}(N)=0$. 对素数 $p>2019,(p, d)=1$, 由于 $1+i d \equiv 0\left(\bmod p^{2}\right)$ 对 $i \in\left\{1,2, \cdots, p^{2}\right\}$ 恰有一解.从而有

$$
f_{p}(N) \leq\left[\frac{N-1}{p^{2}}\right]+1<\frac{N}{p^{2}}+1
$$

故



$$
\begin{aligned}
& \leq \sum_{\text {素数 } p: 2019<p \leq \sqrt{1+N d}}\left(\frac{N}{p^{2}}+1\right) \\
& <N\left(\sum_{\text {素数 } p: 2019<p} \frac{1}{p^{2}}\right)+\sqrt{1+N d} \\
& <N \sum_{p>2020} \frac{1}{p(p-1)}+\sqrt{1+N d}(2020 \text { 不是素数 }) \\
& \leq \frac{N}{2020}+\sqrt{1+N d} .
\end{aligned}
$$

假设对 $i=1,2, \cdots, N-2018,1+i d, 1+(i+1) d, \cdots, 1+(i+2018) d$ 中至少一个有平方因子, 那么

$$
f(N) \geq\left[\frac{N}{2019}\right]>\frac{N}{2019}-1
$$

于是

$$
\frac{N}{2019}-1<\frac{N}{2020}+\sqrt{1+N d}
$$

在 $N$ 充分大时上式不成立. 于是存在 $i \in \mathbb{N}_{+}, 1+i d, 1+(i+1) d, \cdots 1+(i+2018) d$均无平方因子, 从而加强命题得证.

原命题成立.

评注 本题一开始可能想归纳法, 但过渡时若改变公差则难以应用归纳假设。

法 1 直接构造时意识到等差数列的标准分解难以刻画，会促使我们对预先给的数列乘上适当倍数, 以调整各项的素因数幂次.

如果了解 Green-Tao 定理, 即存在任意长的素数等差数列, 法 2 加强命题是自然的. 我们需要证明每一项无平方因子, 这可以化归为经典的数论计数问题.

3. 校园里有 2019 名学生, 每名学生加入了一个或多个社团, 每个社团恰有 12 名社团千部.一群学生能够开展某个社团的活动, 当且仅当这些学生都来自该社团,且这个社团的干部都在这些学生中.

现已知对任意一群至少 12 人的学生, 他们恰能开展唯一一个社团的活动,这是否可能? 如果可能, 求恰有 27 人加入的社团的所有可能数目.

解 用集合语言描述问题:

设 $A_{1}, A_{2}, \cdots, A_{n}, B_{1}, B_{2}, \cdots, B_{n}$ 是集合 $S=\{1,2, \cdots 2019\}$ 的子集， $B_{i} \subseteq A_{i},\left|B_{i}\right|=12(1 \leq i \leq n)$. 已知对任意 $C \subseteq S$, 存在唯一的 $i(1 \leq i \leq n)$,使得 $B_{i} \subseteq C \subseteq A_{i}$. 问这是否可能, 如果可能, 求满足 $\left|A_{i}\right|=27$ 的 $i(1 \leq i \leq n)$
的所有可能数目.

这可能发生, 令 $B_{i}\left(1 \leq i \leq n, n=\left(\begin{array}{c}2019 \\ 12\end{array}\right)\right)$ 为 $S$ 的全体 12 元子集, 设 $B_{i}$ 中最大元素为 $b_{i}$, 令 $A_{i}=B_{i} \bigcup\left\{b_{i}+1, b_{i}+2, \cdots, 2019\right\}$.

此时对任意 $C \subseteq S$, 设 $C$ 的 12 个较小的元素组成集合 $C^{\prime}$, 则存在 $B_{i}=C^{\prime}$,进而 $A_{i} \backslash B_{i}=\left\{b_{i}+1, b_{i}+2, \cdots, 2019\right\} \supseteq\left(C \backslash C^{\prime}\right)$, 故 $B_{i}=C^{\prime} \subseteq C \subseteq A_{i}$. 若有 $j$ 使得 $B_{j} \subseteq C \subseteq A_{j}$, 由 $B_{j} \subseteq C$ 知 $B_{j}$ 中第 12 小的元素 $b_{j}$ 不小于 $C$ 中第 12 小的元素 $c$, 由 $C \subseteq A_{j}$ 知 $A_{j}$ 中第 12 小的元素 $b_{j}$ 不大于 $C$ 中第 12 小的元素 $c$,故只能 $c=b_{j}$, 导致 $B_{j}=C^{\prime} . j$ 唯一性得证.

在这个例子中恰有 $\left(\begin{array}{c}2019-15-1 \\ 11\end{array}\right)=\left(\begin{array}{c}2003 \\ 11\end{array}\right)$ 个 $i$ 使得 $\left|A_{i}\right|=27$, 下证这样的数目只能是 $\left(\begin{array}{c}2003 \\ 11\end{array}\right)$.

用 $x_{k}(12 \leq k \leq 2019)$ 表示使得 $\left|A_{i}\right|=k$ 的 $i$ 的数目. 对 $12 \leq k \leq 2019, S$的每个 $k$ 元子集 $C$ 都存在唯一的 $i$ 使 $B_{i} \subseteq C \subseteq A_{i}$; 而对每个 $i$, 设 $\left|A_{i}\right|=t$, 则恰有 $\left(\begin{array}{l}t-12 \\ k-12\end{array}\right)$ 个 $k$ 元子集 $C$ 使得 $B_{i} \subseteq C \subseteq A_{i}$ (约定 $u<v$ 时 $\left(\begin{array}{l}u \\ v\end{array}\right)=0$ ), 故

$$
\left(\begin{array}{c}
2019 \\
k
\end{array}\right)=\sum_{t=12}^{2019} x_{t}\left(\begin{array}{l}
t-12 \\
k-12
\end{array}\right)
$$

依次令 $k=2019,2018,2017 \cdots 12$, 得到

$$
\begin{aligned}
x_{2019} & =\left(\begin{array}{c}
2019 \\
2019
\end{array}\right), \\
x_{2018} & =\left(\begin{array}{c}
2019 \\
2018
\end{array}\right)-\left(\begin{array}{c}
2007 \\
2006
\end{array}\right) x_{2019}, \\
x_{2017} & =\left(\begin{array}{c}
2019 \\
2017
\end{array}\right)-\left(\begin{array}{c}
2007 \\
2005
\end{array}\right) x_{2019}-\left(\begin{array}{c}
2007 \\
2006
\end{array}\right) x_{2018}, \\
\vdots & \\
x_{12} & =\left(\begin{array}{c}
2019 \\
12
\end{array}\right)-\left(\begin{array}{c}
2007 \\
0
\end{array}\right) x_{2019}-\left(\begin{array}{c}
2007 \\
1
\end{array}\right) x_{2018}-\cdots-\left(\begin{array}{c}
2007 \\
2006
\end{array}\right) x_{13} .
\end{aligned}
$$

因此可依次解出 $x_{2019}, x_{2018}, \cdots, x_{12}$, 我们证明 $x_{k}=\left(\begin{array}{c}2030-k \\ 11\end{array}\right)(12 \leq k \leq 2019)$,这只要验证等式

$$
\left(\begin{array}{c}
2019 \\
k
\end{array}\right)=\sum_{t=12}^{2019}\left(\begin{array}{c}
2030-t \\
11
\end{array}\right)\left(\begin{array}{l}
t-12 \\
k-12
\end{array}\right)
$$

事实上, $\left(\begin{array}{c}2030-t \\ 11\end{array}\right)$ 等于方程

$$
y_{1}+y_{2}+\cdots+y_{12}=2031-t
$$

的正整数解解数, $\left(\begin{array}{c}t-12 \\ k-12\end{array}\right)$ 等于方程

$$
z_{1}+z_{2}+\cdots+z_{k-11}=t-11
$$

的正整数解解数, 故 $\sum_{t=12}^{2019}\left(\begin{array}{c}2030-t \\ 11\end{array}\right)\left(\begin{array}{l}t-12 \\ k-12\end{array}\right)$ 等于方程

$$
y_{1}+y_{2}+\cdots+y_{12}+z_{1}+\cdots+z_{k-11}=2020
$$

的正整数解解数, 即 $\left(\begin{array}{c}2019 \\ k\end{array}\right)$.

综上, 所说情况可能发生, 且使得 $\left|A_{i}\right|=27$ 成立的 $i$ 的数目只能为 $x_{27}=$ $\left(\begin{array}{c}2003 \\ 11\end{array}\right)$.

评注 在说明了 $x_{2019}, x_{2018}, \cdots, x_{12}$ 唯一确定后, 由我们的例子便已经可说明 $x_{27}=\left(\begin{array}{c}2003 \\ 11\end{array}\right)$. 但本题先研究 $x_{k}$ 可能会比构造例子容易, 即例子是我们试算出 $x_{k}=\left(\begin{array}{c}2030-k \\ 11\end{array}\right)$ 后受数字启发而造. 写解答时把例子写在前面更合逻辑.

4. 在 $\triangle A B C$ 中, $A B=A C . M$ 为劣弧 $A C$ 上一点, $B M$ 与 $A C$ 相交于点 $E, \angle B M C$ 的平分线与 $B C$ 相交于点 $F$. 若 $\angle A F B=\angle C F E$, 证明: $\triangle A B C$ 是等边三角形.



证明 由 $A B=A C$ 知 $\angle A B F=\angle E C F$, 又 $\angle A F B=\angle C F E$, 故 $\triangle A B F \sim$ $\triangle E C F$. 因此

$$
\frac{B F}{C F}=\frac{A B}{C E}
$$

由 $M F$ 平分 $\angle B M C$ 可知

$$
\frac{B F}{C F}=\frac{B M}{C M}
$$

故 $\frac{A B}{C E}=\frac{B M}{C M}$, 即有

$$
\frac{A B}{B M}=\frac{C E}{C M}=\frac{B E}{B A} .
$$

结合 $\angle A B E=\angle M B A$ 知 $\triangle A B E \sim \triangle M B A$, 故

$$
\angle B A C=\angle A M B=\angle A C B .
$$

即 $\triangle A B C$ 是等边三角形.
评注利用 $\triangle A B F \sim \triangle E C F$ 得到比例式后消去 $A F$ 和 $B F$, 简化了问题.本题是简单题.

5. 设函数 $f:\{1,2 \cdots 2019\} \rightarrow\{-1,1\}$ 满足对任意 $1 \leq k \leq 2019$, 都存在 $1 \leq l \leq 2019$ 使得

$$
\sum_{i:(i-k)(l-i) \geq 0} f(i) \leq 0
$$

求 $\sum_{i=1}^{2019} f(i)$ 的最大值.

## 解 令

$$
f(i)=\left\{\begin{array}{l}
1, \quad i \equiv 0,1(\bmod 3) \\
-1, \quad i \equiv 2(\bmod 3)
\end{array}\right.
$$

符合要求, 此时 $\sum_{i=1}^{2019} f(i)=673$. 下证 $\sum_{i=1}^{2019} f(i) \leq 673$.

法 1 我们证明将 2019 换为一般的 $3 n\left(n \in \mathbb{Z}_{+}\right)$时, $\sum_{t=1}^{3 n} f(i) \leq n$.

对 $n$ 归纳, $n=1$ 时 $f(1), f(2), f(3)$ 不能全为 1 , 故 $f(1)+f(2)+f(3) \leq 1$,结论成立.

假设 $n-1$ 时结论成立, 考虑 $n$ 时的情形. 若存在 $1 \leq i<j \leq 3 n, i+1<j$,使得 $f(i)=f(j)=1$, 而对 $i<k<j$, 都有 $f(k)=-1$. 如下定义函数 $g$ :

$$
g(k)=\left\{\begin{array}{l}
f(k), \quad 1 \leq k \leq i-1 \\
f(k+2), \quad i \leq k \leq j-3, \\
f(k+3), \quad j-2 \leq k \leq 3 n-3 .
\end{array}\right.
$$

则 $g:\{1,2, \cdots, 3(n-1)\} \rightarrow\{-1,1\}$, 我们验证 $g$ 满足 $n-1$ 时的条件.

对 $1 \leq k \leq i-1$ 存在以 $k$ 为始末项的连续若干项的关于 $f$ 的函数值之和(设为 $S_{1}$ ) 非正, 即 $S_{1} \leq 0$. 它们对应的 $g$ 的函数值记为 $S_{2} . S_{2}$ 要么与 $S_{1}$中项相同, 要么比 $S_{1}$ 中少 $f(i)$, 要么比 $S_{1}$ 中少 $f(i), f(i+1)$, 要么比 $S_{1}$ 中少 $f(i), f(i+1), f(j)$, 均有 $S_{2} \leq S_{1} \leq 0$. 对 $j-2 \leq k \leq 3 n-3$ 可类似验证. 对 $i \leq k \leq j-3$ 有 $g(k)=f(k+2)<0$. 从而 $g$ 满足 $n-1$ 时条件.

故由归纳假设

$\sum_{i=1}^{3 n} f(i)=\sum_{i=1}^{3 n-3} g(i)+f(i)+f(i+1)+f(j)=\sum_{i=1}^{3 n-3} g(i)+1 \leq(n-1)+1=n$.

若不存在这样的 $i, j$, 由已知 $f$ 不能恒为 1 , 若此时 $\sum_{i=1}^{3 n} f(i) \geq 1$, 则存在
$1 \leq k \leq l \leq 3 n$ 使得 $f(k)=f(k+1)=\cdots=f(l)=1$, 对 $1 \leq i<k$ 与 $l<i \leq 3 n, f(i)=-1$ 且 $l-k+1 \geq \frac{3 n+1}{2}$. 则有 $k \leq 2 k-1<2 l-3 n+1$, 于是

$$
\sum_{i \in Z,(i-2 k+1)(j-i) \geq 0} f(i)>0
$$

对任意 $j$ 成立, 矛盾!

故 $\sum_{i=1}^{3 n} f(i) \leq 0$, 结论得证.

法 2 记

$$
S_{k}=f(1)+f(2)+\cdots+f(k)(1 \leq k \leq 2019),
$$

对 $k<k^{\prime}$, 有

$$
\left|S_{k^{\prime}}-S_{k}\right|=\left|f(k+1)+\cdots+f\left(k^{\prime}\right)\right| \leq k^{\prime}-k .
$$

由已知, 对任意 $1 \leq k \leq 2019$, 若 $S_{1}, S_{2}, \cdots, S_{k-1}<S_{k}$, 则存在 $l>k$ 使得

$$
S_{l} \leq S_{k-1}<S_{k}
$$

设全体这样的 $k$ 为 $1=k_{1}<k_{2}<\cdots<k_{n}$, 由离散介值定理

$$
0 \geq S_{k_{1}}-1=S_{k_{2}}-2=\cdots=S_{k_{n}}-n
$$

对任意 $1 \leq i \leq n$, 存在 $l_{i}>k_{i}$, 使 $S_{l_{i}}<S_{k_{i}}$, 而 $l_{i}$ 属于区间

$$
\left[k_{1}, k_{2}\right),\left[k_{2}, k_{3}\right), \cdots,\left[k_{n}, 2019\right]
$$

之一.

$1^{\circ}$ 若 $l_{i} \in\left[k_{j-1}, k_{j}\right)(2 \leq j \leq n)$. 由 $S_{l_{i}}<S_{k_{i}} \leq S_{k_{j-1}}=S_{k_{j}}-1$ 知

$$
\begin{aligned}
k_{j}-k_{i} & =\left(k_{j}-l_{i}\right)+\left(l_{i}-k_{j-1}\right)+\left(k_{j-1}-k_{i}\right) \\
& \geq\left(S_{k_{j}}-S_{l_{i}}\right)+\left(S_{k_{j-1}}-S_{l_{i}}\right)+\left(S_{k_{j-1}}-S_{k_{i}}\right) \\
& \geq\left(S_{k_{j}}-S_{k_{i}}+1\right)+\left(S_{k_{j-1}}-S_{k_{i}}+1\right)+\left(S_{k_{j-1}}-S_{k_{i}}\right) \\
& =3\left(S_{k_{j}}-S_{k_{i}}\right)=3(j-i) .
\end{aligned}
$$

$2^{\circ}$ 若 $l_{i} \in\left[k_{n}, 2019\right]$. 类似地, 由 $S_{l_{i}}<S_{k_{i}} \leq S_{k_{n}}, S_{k_{n}} \geq S_{2019}$ 知

$$
\begin{aligned}
2019-k_{i} & =\left(2019-l_{i}\right)+\left(l_{i}-k_{n}\right)+\left(k_{n}-k_{i}\right) \\
& \geq\left(S_{2019}-S_{l_{i}}\right)+\left(S_{k_{n}}-S_{l_{i}}\right)+\left(S_{k_{n}}-S_{k_{i}}\right) \\
& \geq\left(S_{2019}-S_{k_{i}}+1\right)+\left(S_{2019}-S_{k_{i}}+1\right)+\left(S_{2019}-S_{k_{i}}\right) \\
& =3\left(S_{2019}-S_{k_{i}}\right)+2 \geq 3\left(S_{2019}-i\right)+2 .
\end{aligned}
$$

现令 $i_{1}=1$, 假设已取好 $i_{t}$, 若 $l_{i_{t}} \in\left[k_{j-1}, k_{j}\right)$, 则令 $i_{t+1}=j$; 若 $l_{i_{t}} \in\left[k_{n}, 2019\right]$,
则停止选取. 设我们选出了 $i_{1}, i_{2}, \cdots, i_{t}$, 则由 $1^{\circ}, 2^{\circ}$,

$$
\begin{aligned}
2019 & =k_{i_{1}}+\left(k_{i_{2}}-k_{i_{1}}\right)+\cdots+\left(k_{i_{t}}-k_{i_{t-1}}\right)+\left(2019-k_{i_{t}}\right) \\
& \geq i_{1}+3\left(i_{2}-i_{1}\right)+\cdots+3\left(i_{t}-i_{t-1}\right)+3\left(S_{2019}-i_{t}\right)+2 \\
& =3 S_{2019} .
\end{aligned}
$$

评注 答案容易猜到, 解法一找到了一个普适的结构用于归纳, 但发现它需一定巧想. 解法二稍繁, 通过找适当的下标子列, 可以较清楚地刻画 $S_{k}$ 的变化.

6. 对于整数 $n \geq 3$, 整数 $a$ 称为 $n-$ 好的, 若存在正整数 $d$, 使得

$$
n \mid a^{d}-1, n \nmid a^{d-1}+a^{d-2}+\cdots+1 .
$$

设 $f(n)$ 是集合 $\{a \mid 0<a<n,(a, n)=1$, 但 $a$ 不是 $n-$ 好的 $\}$ 的元素个数. 求 $f(n)(n \geq 3)$ 的最小值, 并求出所有 $n(\geq 3)$ 使得 $f(n)$ 取到该最小值.

解 $f(n)$ 的最小值为 1 , 使 $f(n)=1$ 的全体 $n \geq 3$ 形如 $2^{\alpha}(\alpha \geq 2)$ 或 $3 \cdot 2^{\alpha}(\alpha \geq 0)$.

首先注意: 1 总是 $n$-好的, 对 $a>1$, 有 $a^{d-1}+a^{d-2}+\cdots+1=\frac{a^{d}-1}{a-1}$, 若 $a$ 是 $n$ - 好的, 显然 $(a, n)=1$.

断言 若 $a(>1)$ 为 $n-$ 好的, 则可不妨设 $a$ 对应的 $d$ 为 $a$ 模 $n$ 的阶.

证明 设 $a>1$ 为 $n$-好的, 即存在 $d>0$,

$$
n \mid a^{d}-1, n \nmid \frac{a^{d}-1}{a-1} .
$$

设 $d_{0}$ 为 $a$ 模 $n$ 的阶, 则 (1) 的前者推出 $d_{0} \mid d$, 从而由

$$
\left.\frac{a^{d_{0}}-1}{a-1} \right\rvert\, \frac{a^{d}-1}{a-1}
$$

及 (1) 的后者可见 $n \nmid \frac{a^{d_{0}-1}}{a-1}$. 因此存在满足 (1) 的 $d$ 当且仅当 $d=d_{0}$ 满足 (1),断言得证.

设 $n \geq 3$, 若 $n-1$ 是 $n$-好的, 由断言知不妨设 $d=2$, 推出

$$
n \nmid \frac{(n-1)^{2}-1}{(n-1)-1}=n,
$$

矛盾. 故 $n-1$ 总不是 $n-$ 好的, 从而 $f(n) \geq 1$, 又 $f(3)=1$, 故 $f(n)$ 的最小值是 1.

下面求所有的 $n \geq 3$ 使得 $f(n)=1$, 这即是说 $1,2, \cdots, n-2$ 中每个与 $n$互素的数 $a$ 均是 $n$-好的.
若 $n$ 是大于 3 的奇数, 则由

$$
n\left|2^{d}-1 \Leftrightarrow n\right| \frac{2^{d}-1}{2-1}
$$

可见 2 不是 $n-$ 好的, 与 $(*)$ 矛盾, 故 $n$ 是偶数. 可设 $n=2^{\alpha} r$, 其中 $\alpha \geq 1, r$ 是奇数. 分类讨论如下:

I. 如果 $r>3$, 设 $r$ 的最小素因子是 $p(>2)$, 模 $p$ 的最小正原根是 $g$, 则 $1<g \leq p-1$, 故 $(g, r)=1$. 我们取 $a \in\{1,2, \cdots, n\}$ 使得

$$
\left\{\begin{array}{l}
a \equiv g(\bmod r), \\
a \equiv-1\left(\bmod 2^{\alpha}\right)
\end{array}\right.
$$

由中国剩余定理 (注意 $(r, 2)=1)$ 知这样的 $a$ 存在, 且由 $(g, r)=1$ 易见 $1<a<n,(a, n)=1$.

设 $d>0$ 满足 $n \mid a^{d}-1$, 则特别地, $a \equiv g(\bmod p), p \mid a^{d}-1$. 故 $d$ 被 $a$ 模 $p$ 的阶 $p-1$ 整除, 从而 $2 \mid d$. 故

$$
a+1\left|\frac{a^{d}-1}{a-1} \Rightarrow 2^{\alpha}\right| \frac{a^{d}-1}{a-1} .
$$

此外, 注意到 $p$ 是 $r$ 的最小素因子, $1 \leq g-1<p$, 及 $a-1 \equiv g-1(\bmod p)$ 可知 $(a-1, r)=1$, 故

$$
r\left|a^{d}-1 \Rightarrow r\right| \frac{a^{d}-1}{a-1} .
$$

所以 $n=2^{\alpha} r$ 整除 $\frac{a^{d}-1}{a-1}$, 从而 $a$ 不是 $n-$ 好的.

若 $a=n-1$, 由 (2) 易见 $g=p-1, r=p$, 从而

$$
p-1=g \text { 模 } p \text { 的阶 }=p-1 \text { 模 } p \text { 的阶 }=2 \text {. }
$$

可得 $r=p=3$, 矛盾. 故 $2 \leq a \leq n-2,(a, n)=1$, 且 $a$ 不是 $n-$ 好的, 与 $(*)$ 矛盾. 从而在 $r>3$ 时 $n$ 不满足要求.

II. 如果 $r \in\{1,3\}$, 我们证明这样的 $n$ 满足要求, 即对 $a \in\{2,3, \cdots, n-1\}$, $(a, n)=1$, 设 $d$ 是 $a$ 模 $n$ 的阶, 则 $n \nmid \frac{a^{d}-1}{a-1}$. 为了确定奇数 $a$ 模 $2^{\alpha}$ 的阶, 我们需要下面熟知的引理:

引理 (1) 设 $a$ 是奇数, $a \equiv 1(\bmod 4), a \neq 1, k_{0}$ 满足 $2^{k_{0}} \| a-1$, 记 $l_{k}$ 是 $a$模 $2^{k}$ 的阶, 则有

$$
l_{k}=\left\{\begin{array}{l}
1, \text { 若 } k=1, \cdots, k_{0}, \\
2^{k-k_{0}}, \text { 若 } k>k_{0} .
\end{array}\right.
$$

(2) 设 $a$ 是奇数, $a \equiv-1(\bmod 4), a \neq-1, k_{0}$ 满足 $2^{k_{0}} \| a+1$, 记 $l_{k}$ 是 $a$ 模
$2^{k}$ 的阶, 则有

$$
l_{k}=\left\{\begin{array}{l}
1, \text { 若 } k=1, \\
2, \text { 若 } k=2, \cdots, k_{0}+1, \\
2^{k-k_{0}}, \text { 若 } k>k_{0}+1 .
\end{array}\right.
$$

引理的证明可对 $k$ 归纳进行, 这里不再赘述. 不过在归纳时容易发现对引理中

(1) 的 $k \geq k_{0}$ 的情形和 (2) 中 $k \geq k_{0}+1$ 的情形, 有 $2^{k} \| a^{l_{k}}-1$.

$\alpha=1$ 时, $n=3,6$, 易验证满足条件. $\alpha \geq 2$ 时, $a$ 模 $2^{\alpha}$ 的阶可设为 $2^{l}$ (注意欧拉定理), $l \geq 1$, 则 $a$ 模 $3 \cdot 2^{\alpha}$ 的阶也是 $2^{l}$. 在引理中取 $k=\alpha$, 对(1)(2)两种情况均有 $\alpha \geq k_{0}+1$, 故由前述知 $2^{\alpha} \| a^{d}-1$, 而 $a-1$ 是偶数, 故 $2^{\alpha} \nmid \frac{a^{d}-1}{a-1}$, 从而 $n \nmid \frac{a^{d}-1}{a-1}$. 证毕.

综上所述, $f(n)$ 的最小值为 1 , 使得 $f(n)=1$ 的全体 $n(\geq 3)$ 形如 $2^{\alpha}(\alpha \geq 2)$或 $3 \cdot 2^{\alpha}(\alpha \geq 0)$.

评注 出于确定 $d$ 的目的可以看出 “断言” 成立, 且容易发现 $f(n)$ 的最小值是 1 . 求使 $f(n)=1$ 成立的 $n$ 时, 首先考虑特殊值 $a=2$ 可排除奇数 $n$, 对偶数 $n$ 希望用对奇数类似的手段, 则可用中国剩余定理分成奇数部分 $r$ 和 $2^{\alpha}$ 分别构造 $a$ 的余数. 取原根的目的仅是让 $2 \mid d$, 而最小素因子的最小正原根保证了 $(a-1, r)=1$. 其实对奇数 $n$ 的处理也可取 $a \equiv g(\bmod n)$, 其中 $g$ 是 $r$ 的最小素因子的最小正原根。

本题要求对阶、升幂定理、中国剩余定理有一定理解, 综合性较强. 求满足取等条件的 $n$ 有两方面, 对答案没把握的话探索比较费时.

