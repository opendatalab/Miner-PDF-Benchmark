# 好题与妙解 (一) 

## 一-2015年新星夏令营中的 8 个问题

## 冷岗松

在今年 7 月的上海新星数学夏令营上, 我提供了一份题为 “数学问题精选 50 题” 的讲义提纲, 其中的 50 题是我从近年来一些数学竞赛资料中精心挑选出来的, 问题的难度大多和全国联赛加试题的水平相当. 在选题过程中, 我力求选出的问题既要不偏不怪, 又要新颖和具有代表性.

在夏令营中, 不少学生贡献了他们的妙思和妙解, 使我如沐春风, 受益颇多.现在我把其中 8 个问题的讨论, 包括问题的来源, 学生的妙解及我的一些看法介绍出来, 供有兴趣者参考.

例 1 设 $a_{0}, a_{1}, \cdots, a_{n}$ 是实数, 满足 $a_{0}=a_{n}=0$, 且

$$
a_{i+1}-2 a_{i}+a_{i-1}=a_{i}^{2}, \quad i=1,2, \cdots, n-1 .
$$

证明: $a_{i} \leq 0, i=1,2, \cdots, n-1$.

解法一 设 $a_{k}=\max \left\{a_{0}, a_{1}, \cdots, a_{n}\right\}$, 要证结论, 只须证明 $a_{k}=0$.

事实上, 若 $k=0$ 或 $n$, 结论已经成立. 下面只须考虑 $1 \leq k \leq n-1$ 的情况,这时在条件等式中令 $i=k$ 便得

$$
0 \geq a_{k+1}-2 a_{k}+a_{k-1}=a_{k}^{2}
$$

故 $a_{k}=0$.

解法二 (根据武钢三中学生王逸轩的解法整理) 由条件知

$$
a_{i+1}-a_{i}=a_{i}-a_{i-1}+a_{i}^{2} \geq a_{i}-a_{i-1} .
$$

假设结论不成立, 则存在 $a_{i}>0(1 \leq i \leq n-1)$, 在所有这样的 $a_{i}$ 中, 取其中下标最小的一个, 记为 $a_{i_{0}}$, 则 $a_{i_{0}-1} \leq 0\left(i_{0}=1\right.$ 时亦成立 $)$, 因此 $a_{i_{0}}-a_{i_{0}-1}>0$. 故对任何 $j \geq i_{0}$ 有 $a_{j}-a_{j-1} \geq a_{i_{0}}-a_{i_{0}-1}>0$. 所以

$$
a_{n}=a_{i_{0}}+\sum_{j=i_{0}+1}^{n}\left(a_{j}-a_{j-1}\right)>0
$$

矛盾!

评注 解法一直接用最优化的思想, 直接考虑序列中的最大元来达到目的;而解法二主要是差分思想的应用, 利用差分的单调性说明序列中不能有正项.

例 2 设 $f(x), g(x)$ 是定义在 $\mathbf{R}$ 上的两个函数, 证明: 存在定义在 $\mathbf{R}$ 上的函数 $h(x)$ 使得

$$
(f(x)+h(x))^{2014}+(g(x)+h(x))^{2014}
$$

是 $\mathbf{R}$ 上的偶函数.

(N. Sedrakyan, Math. Refl. 2014)

解 对任意定义在 $\mathbf{R}$ 上的函数 $f(x)$, 令

$$
f_{e}(x)=\frac{1}{2}(f(x)+f(-x)), \quad f_{o}(x)=\frac{1}{2}(f(x)-f(-x))
$$

则 $f(x)=f_{e}(x)+f_{o}(x), \forall x \in \mathbf{R}$, 且 $f_{e}, f_{o}$ 分别是 $\mathbf{R}$ 上的偶函数和奇函数.

类似地, 对任意定义在 $\mathbf{R}$ 上的函数 $g(x)$ 有

$$
g(x)=g_{e}(x)+g_{o}(x),
$$

其中 $g_{e}(x)=\frac{1}{2}(g(x)+g(-x))$ 和 $g_{o}(x)=\frac{1}{2}(g(x)-g(-x))$ 分别是 $\mathbf{R}$ 上的偶函数和奇函数.

现令

$$
h(x)=-g_{e}(x)-f_{o}(x), \quad \forall x \in \mathbf{R} .
$$

则 $f(x)+h(x)=f_{e}(x)-g_{e}(x)$ 是 $\mathbf{R}$ 上的偶函数, $g(x)+h(x)=g_{o}(x)-f_{o}(x)$ 是 $\mathbf{R}$ 上的奇函数. 因此对任何 $n \in \mathbf{N}^{*}$ 有

$$
(f(x)+h(x))^{2 n}+(g(x)+h(x))^{2 n}
$$

是 $\mathbf{R}$ 上的偶函数.

故上面构造的函数 $h(x)$ 满足要求.

评注 上面解法用到一个著名的事实: 任何定义在 $\mathbf{R}$ (或对称区间) 上的实函数都可表示成一个偶函数和一个奇函数的和. 一个自然的问题是: 是否任何一个定义在 $\mathbf{R}$ 上的实函数都可表示成两个单调函数的和 (或差)？回答这个问题却需要一些实变函数的知识, 因为全体单调函数形成的集合的基数是 $c$, 而一切实值函数之全体形成的几何的基数是 $2^{c}$, 因此答案是否定的. 当然, 任何有界变差函数可表示成两个单调增函数的差 (从而也是一个单调增函数和一个单调减函数
的和). 这方面的知识和问题可参见周民强的《实变函数论》一书 (北京大学出版社, 2010). 但下面的正面结论或许更能激发你的兴趣: 任何一个实多项式可表为两个单调增加的多项式之差.

例 3 设实数 $a, b, c, d$ 满足 $|a|>1,|b|>1,|c|>1,|d|>1$, 且

$$
a b(c+d)+d c(a+b)+a+b+c+d=0 .
$$

证明:

$$
\frac{1}{a-1}+\frac{1}{b-1}+\frac{1}{c-1}+\frac{1}{d-1}>0
$$

(2015，俄罗斯)

解法一 由 $|a|>1$ 知 $\frac{a+1}{a-1}>0$, 同理 $\frac{b+1}{b-1}>0, \frac{c+1}{c-1}>0, \frac{d+1}{d-1}>0$.

由条件等式知,

$$
\prod(a+1)-\prod(a-1)=2\left(\sum a b c+\sum a\right)=0
$$

因此 $\prod \frac{a+1}{a-1}=1$. 故由均值不等式可得

$$
\sum \frac{1}{a-1}=\frac{1}{2} \sum \frac{a+1}{a-1}-2 \geq 2 \sqrt[4]{\prod \frac{a+1}{a-1}}-2=0
$$

且上式等号成立当且仅当 $a=b=c=d$, 这时代入条件中的等式得 $|a|=1$, 矛盾!故上式等号不成立.

综上便得所证不等式成立.

## 解法二 (根据武钢三中学生林鸿的解法整理)

先证一个引理:

引理 设 $|x|>1,|y|>1, x, y \in \mathbf{R}$, 则

$$
\frac{1}{x-1}+\frac{1}{y-1}>\frac{x+y}{x y+1} .
$$

事实上, 由 $|x|>1,|y|>1$ 易知 $(x-1)(y+1)(x y+1)>0$. 这样,

$$
\frac{1}{x-1}-\frac{y}{x y+1}=\frac{y+1}{(x-1)(x y+1)}=\frac{(x-1)(y+1)(x y+1)}{(x-1)^{2}(x y+1)^{2}}>0,
$$

因此 $\frac{1}{x-1}>\frac{y}{x y+1}$.

同理, $\frac{1}{y-1}>\frac{x}{x y+1}$.

将上面两个不等式相加便得引理中的不等式, 引理证完.

回到原题. 由引理可得,

$$
\frac{1}{a-1}+\frac{1}{b-1}>\frac{a+b}{a b+1}, \frac{1}{c-1}+\frac{1}{d-1}>\frac{c+d}{c d+1} .
$$

因此

$$
\begin{aligned}
\frac{1}{a-1}+\frac{1}{b-1}+\frac{1}{c-1}+\frac{1}{d-1} & >\frac{a+b}{a b+1}+\frac{c+d}{c d+1} \\
& =\frac{(a+b)(c d+1)+(c+d)(a b+1)}{(a b+1)(c d+1)} \\
& =\frac{a b(c+d)+d c(a+b)+a+b+c+d}{(a b+1)(c d+1)}=0 .
\end{aligned}
$$

这就是要证的不等式.

评注 (1) 用解法一的方法, 可立得本题的一个自然推广:

设 $a_{1}, a_{2}, \cdots, a_{n} \in \mathbf{R}$ 满足 $\left|a_{i}\right|>1, i=1,2, \cdots, n$. 且

$$
\prod_{i=1}^{n}\left(a_{i}+1\right)=\prod_{i=1}^{n}\left(a_{i}-1\right)
$$

则

$$
\sum_{i=1}^{n} \frac{1}{a_{i}-1}>0
$$

(2) 湖南雅礼中学学生尹龙晖给出了该问题的一个新的有趣的推广:

设 $f(x)=\prod_{i=1}^{n}\left(x-a_{i}\right), a_{i} \in \mathbf{R}, i=1,2, \cdots, n$. 实数 $\alpha, \beta$ 满足

(i) $f(\alpha)=f(\beta)$;

(ii) $[\alpha, \beta] \cap\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}=\emptyset$.

则

$$
\sum_{i=1}^{n}\left(\frac{1}{\alpha-a_{i}}-\frac{1}{\beta-a_{i}}\right)>0 .
$$

尹龙晖的推广详见他发表在数学新星网上学生专栏第五期的文章.

例 4 设 $n \geq 3, x_{1}, x_{2}, \cdots, x_{n}$ 是非负实数. 记

$$
A=\sum_{i=1}^{n} x_{i}, \quad B=\sum_{i=1}^{n} x_{i}^{2}, \quad A=\sum_{i=1}^{n} x_{i}^{3}
$$

证明:

$$
(n+1) A^{2} B+(n-2) B^{2} \geq A^{4}+(2 n-2) A C \text {. }
$$

(2013, ICM)

## 证明 (根据上海中学学生高继扬和武钢三中学生王逸轩的解法整理)

记 $D=\sum_{i=1}^{n} x_{i}^{4}$. 注意到

$$
A^{2}-B=\sum_{1 \leq i \neq j \leq n} x_{i} x_{j}=\sum_{i=1}^{n} x_{i}\left(A-x_{i}\right)
$$

由 Cauchy 不等式有

$$
\begin{aligned}
\left(A^{2}-B\right)^{2} & =\left(\sum_{1 \leq i \neq j \leq n} x_{i} x_{j}\right)^{2}=n(n-1) \sum_{1 \leq i \neq j \leq n} x_{i}^{2} x_{j}^{2} \\
& =n(n-1)\left(B^{2}-D\right),
\end{aligned}
$$

再由 Cauchy 不等式有

$$
\begin{aligned}
\left(A^{2}-B\right)^{2} & =\left(\sum_{i=1}^{n} x_{i}\left(A-x_{i}\right)\right)^{2}=n\left(\sum_{i=1}^{n} x_{i}^{2}\left(A-x_{i}\right)^{2}\right) \\
& =n\left(A^{2}-2 A C+D\right) .
\end{aligned}
$$

将 $(1)$ 式除以 $n(n-1)$ 及 $(2)$ 式除以 $n$ 后相加得

$$
\frac{1}{n-1}\left(A^{2}-B\right)^{2} \leq A^{2} B-2 A C+B^{2}
$$

整理便得所证结果.

评注 吉林大学附属中学的王晨旭同学敏锐的发现本题中的不等式是著名的 Newton 不等式的一个特例. 一般的 Newton 不等式可叙述为: 设 $a_{1}, a_{2}, \cdots, a_{n}$为非负实数, 记 $P_{0}=1$,

$$
P_{r}=\frac{\sum_{1 \leq i_{1}<i_{2}<\cdots<i_{r} \leq n} a_{i_{1}} a_{i_{2}} \cdots a_{i_{r}}}{\left(\begin{array}{l}
n \\
r
\end{array}\right)}, \quad 1 \leq r<n
$$

则 $P_{r}^{2} \geq P_{r-1} P_{r+1}$.

王晨旭同学的推导如下:

$$
\begin{array}{r}
\text { 记 } Q=\sum_{1 \leq i<j \leq n} x_{i} x_{j}, R=\sum_{1 \leq i<j<k \leq n} x_{i} x_{j} x_{k} . \text { 注意到 } \\
C=A^{3}-3 A Q+3 R, \quad B=A^{2}-2 Q .
\end{array}
$$

这时不等式 (*) 等价于

$$
(n+1) A^{2}\left(A^{2}-2 Q\right)+(n-2)\left(A^{2}-2 Q\right)^{2} \geq A^{4}+(2 n-2) A\left(A^{3}-3 A Q+3 R\right),
$$

整理就是

$$
\left(\frac{Q}{\left(\begin{array}{c}
n \\
2
\end{array}\right)}\right)^{2} \geq \frac{A}{\left(\begin{array}{c}
n \\
1
\end{array}\right)} \cdot \frac{R}{\left(\begin{array}{c}
n \\
3
\end{array}\right)}
$$

也就是 $P_{2}^{2} \geq P_{1} \cdot P_{3}$.

这正是 Newton 不等式 $r=2$ 的情形.
例 5 设 $a, b, c, d>0$. 证明:

$$
\frac{1}{(a+b)^{2}}+\frac{1}{(b+c)^{2}}+\frac{1}{(c+d)^{2}}+\frac{1}{(d+a)^{2}} \geq \frac{2}{a c+b d}
$$

(2013, Kolmogorov Olympiad)

解法一 不妨设 $b d \geq a c$. 由 Cauchy 不等式, 可得

$$
\frac{1}{(a+b)^{2}}+\frac{1}{(b+c)^{2}} \geq \frac{1}{\left(a c+b^{2}\right)\left(\frac{a}{c}+1\right)}+\frac{1}{\left(b^{2}+a c\right)\left(1+\frac{c}{a}\right)}=\frac{1}{a c+b^{2}} .
$$

同理,

$$
\frac{1}{(c+d)^{2}}+\frac{1}{(d+a)^{2}} \geq \frac{1}{a c+d^{2}}
$$

因此我们仅须证明

$$
\frac{1}{a c+b^{2}}+\frac{1}{a c+d^{2}} \geq \frac{2}{a c+b d}
$$

事实上,

$$
\begin{aligned}
\frac{1}{a c+b^{2}}+\frac{1}{a c+d^{2}}-\frac{2}{a c+b d} & =\frac{2 a c+b^{2}+d^{2}}{\left(a c+b^{2}\right)\left(a c+d^{2}\right)}-\frac{2}{a c+b d} \\
& =\frac{(b d-a c)(b-d)^{2}}{\left(a c+b^{2}\right)\left(a c+d^{2}\right)(a c+b d)} \geq 0 .
\end{aligned}
$$

故 (2) 式成立, 故所证不等式成立.

当 $a=b=c=d$ 时, (2) 式中等号成立.

评注 此题难度容易被我们低估. 开始我们认为: 只要熟悉一个常用的不等式: $\frac{1}{1+x^{2}}+\frac{1}{1+y^{2}} \geq \frac{1}{1+x y}(x, y>0)$, 此题便可迅速证得. 事实上并不然. 一些同学尽管知道上述不等式, 仍然解得十分繁复. 这是因为怎样用上述小不等式需作对称分析, 即便化归为 (2) 后, 证明仍不简单.

王逸轩发现, (2) 式实际上可抽象为下面的引理: 设 $x y \geq 1$, 则 $\frac{1}{1+x^{2}}+\frac{1}{1+y^{2}} \geq$ $\frac{2}{x y+1}$. 事实上, 只要在这个引理中取 $x=\sqrt{\frac{b^{2}}{a c}}, y=\sqrt{\frac{d^{2}}{a c}}$, 便得 (2) 式.

下面的解法非常优雅.

## 解法二 (根据湖南省长郡中学学生谭华为的解法整理)

由 Cauchy 不等式可得

$$
\frac{a c+b d}{(a+b)^{2}}=\frac{(a c+b d)\left(\frac{a}{c}+\frac{b}{d}\right)}{(a+b)^{2}} \cdot \frac{c d}{a d+b c} \geq \frac{c d}{a d+b c} .
$$

同理

$$
\frac{a c+b d}{(c+d)^{2}} \geq \frac{a b}{a d+b c}
$$

故

$$
\frac{a c+b d}{(a+b)^{2}}+\frac{a c+b d}{(c+d)^{2}} \geq \frac{a b+c d}{a d+b c}
$$

同理

$$
\frac{a c+b d}{(b+c)^{2}}+\frac{a c+b d}{(d+a)^{2}} \geq \frac{a d+b c}{a b+c d}
$$

所以

$$
\begin{aligned}
& \left(\frac{1}{(a+b)^{2}}+\frac{1}{(b+c)^{2}}+\frac{1}{(c+d)^{2}}+\frac{1}{(d+a)^{2}}\right) \cdot(a c+b d) \\
& \geq \frac{a b+c d}{a d+b c}+\frac{a d+b c}{a b+c d} \geq 2
\end{aligned}
$$

故

$$
\frac{1}{(a+b)^{2}}+\frac{1}{(b+c)^{2}}+\frac{1}{(c+d)^{2}}+\frac{1}{(d+a)^{2}} \geq \frac{2}{a c+b d}
$$

例 6 集合 $A_{1}, A_{2}, \cdots, A_{m}$ 的元素个数均为 $a, B_{1}, B_{2}, \cdots, B_{m}$ 的元素个数均为 $b$, 且满足 $A_{i} \cap B_{j}=\emptyset$ 当且仅当 $i=j$. 试求 $m$ 的最大值.

这是著名的 Bollobás 定理的一个特例, 这个特例也早已出现在上世纪 70 年代的组合学教材中. 它被选作 2013 年哈佛一麻省的数学竞赛试题. Bollobás 定理可叙述为:

设 $A_{1}, A_{2}, \cdots, A_{n}$ 和 $B_{1}, B_{2}, \cdots, B_{n}$ 是 $2 n$ 个不同的正整数的集合, 满足 $A_{i} \cap B_{j}=\emptyset$ 当且仅当 $i=j$. 则

$$
\sum_{i=1}^{n} \frac{1}{\left(\begin{array}{c}
\left|A_{i}\right|+\left|B_{i}\right| \\
\left|A_{i}\right|
\end{array}\right)} \leq 1
$$

有兴趣者可研究一下 Bollobás 定理的证明及它和著名的 Sperner 定理的关系.

下面介绍王逸轩给出的例 6 的解法.

解 所求 $m$ 的最大值为 $\left(\begin{array}{c}a+b \\ a\end{array}\right)$.

不妨设 $A_{1} \cup \cdots \cup A_{m} \cup B_{1} \cup \cdots \cup B_{m}=\{1,2, \cdots, n\}$.

下面考虑 $\{1,2, \cdots, n\}$ 的排列. 我们把满足 $A_{i}$ 中的数全在 $B_{i}$ 之前的排列叫做具有性质 $P_{i}$ 的排列, 则对 $\{1,2, \cdots, n\}$ 的任一个排列, 性质 $P_{1}, P_{2}, \cdots, P_{m}$ 至多有一个成立. 否则, 不妨设某一排列同时具有性质 $P_{1}, P_{2}$. 由于 $A_{1} \cap B_{2} \neq \emptyset$, 取 $x \in A_{1} \cap B_{2}$, 则由该排列满足性质 $P_{1}$ 知 $B_{1}$ 中的数全在 $x$ 之后, 由该排列具有性质 $P_{2}$ 知 $A_{2}$ 中的数全在 $x$ 之前, 即 $A_{1} \cap B_{2}=\emptyset$, 矛盾!
因此, $1,2, \cdots, n$ 的总排列数不少于 $\sum_{i=1}^{n}\left|P_{i}\right|$, 其中 $\left|P_{i}\right|$ 表示具有性质 $P_{i}$ 的所有排列的个数. 故

$$
n ! \geq m \cdot\left(\begin{array}{c}
n \\
a+b
\end{array}\right) \cdot a ! b !(n-a-b) !
$$

即

$$
m \leq \frac{(a+b) !}{a ! b !}=\left(\begin{array}{c}
a+b \\
a
\end{array}\right) .
$$

另一方面, 设 $A=\{1,2, \cdots, a+b\}$. 令 $A_{i}$ 表示 $A$ 的所有 $a$ 元素, $B_{i}=A-A_{i}$,则 $A_{i} \cap B_{i}=\emptyset$ 且 $A_{i} \cap B_{j} \neq \emptyset(\forall i \neq j)$, 此时 $m=\left(\begin{array}{c}a+b \\ a\end{array}\right)$.

综上所述, $m_{\text {max }}=\left(\begin{array}{c}a+b \\ a\end{array}\right)$.

例 7 设 $A_{1}, A_{2}, \cdots, A_{n}(n \geq 2)$ 是一条直线上的线段, 满足

(1) $A_{i} \cap A_{i+1} \neq \emptyset, \quad \forall 1 \leq i \leq n-1$;

(2) 对 $\forall 1 \leq i<j \leq n$, 如果 $i-j$ 是偶数, 则 $A_{i} \cap A_{j} \neq \emptyset$.

求最大的 $k=k(n)$ 使得存在一点, 它属于至少 $k$ 个线段.

这是笔者从乌克兰一个中学数学杂志上看到的一个问题, 具体的出处已难再发现。

## 解 (根据上海中学学生高继扬的解法整理)

$$
k_{\max }=\left[\frac{n+3}{2}\right] .
$$

不妨设 $A_{1}, A_{2}, \cdots, A_{n}$ 分布在数轴上, $A_{i}$ 对应区间 $\left[x_{i}, y_{i}\right]$. 记

$$
S_{1}=\{i \mid 1 \leq i \leq n, i \text { 为奇数 }\}, S_{2}=\{i \mid 1 \leq i \leq n, i \text { 为偶数 }\} .
$$

由条件 (2) 和海莱定理知 $\bigcap_{i \in S_{1}} A_{i} \neq \emptyset, \bigcap_{i \in S_{2}} A_{i} \neq \emptyset$. 取 $a \in \bigcap_{i \in S_{1}} A_{i}, b \in \bigcap_{i \in S_{2}} A_{i}$, 不妨设 $a \leq b$.

设 $y_{k}=\min _{i \in S_{1}}\left\{y_{i}\right\}$, 那么对任意 $j \in S_{1}$, 因 $A_{k} \cap A_{j} \neq \emptyset$, 知 $x_{j} \leq a \leq y_{k} \leq y_{j}$, 因此 $\left[a, y_{k}\right] \subseteq A_{j}$. 这时 $k \pm 1 \in S_{2}, b \in A_{k \pm 1}$ 且 $A_{k \pm 1} \cap A_{k} \neq \emptyset$.

下分两种情况:

(i) 若 $b \leq y_{k}$, 则 $b \in\left[a, y_{k}\right]$, 这时对 $\forall 1 \leq i \leq n, b \in A_{i}$, 所以 $b$ 属于至少 $n \geq\left[\frac{n+3}{2}\right]$ 条线段 $(n \geq 2)$.

(ii) 若 $b \geq y_{k}$, 则 $y_{k \pm 1} \geq b>y_{k}$, 所以 $x_{k \pm 1} \leq y_{k}$, 进而有 $y_{k} \in A_{k \pm 1}$. 这里 $k \pm 1$取法为: 当 $k \neq n$ 时取 $k+1$, 当 $k=n$ 时取 $k-1$.

故 $y_{k}$ 属于至少 $\left|S_{1}\right|+1=\left[\frac{n+1}{2}\right]+1=\left[\frac{n+3}{2}\right]$ 条线段.

综上知 $k(n)=\left[\frac{n+3}{2}\right]$ 时命题成立.

下构造例子说明 $\left[\frac{n+3}{2}\right]$ 是最优的.
记 $t=\left[\frac{n}{2}\right]$, 令 $A_{2 k-1}=[0, k], A_{2 k}=[k, t+1], k=1,2, \cdots, t, A_{n}=[0, t+1]$ (若 $n$ 为奇数). 那么若 $i, j$ 同为奇数, 则 $0 \in A_{i} \cap A_{j}$; 若 $i, j$ 同为偶数, 则 $t+1 \in A_{i} \cap A_{j}$. 这说明上述构造的线段 $\left\{A_{i}\right\}$ 满足条件 (2). 又 $k \in A_{2 k-1} \cap$ $A_{2 k}, \quad[k, k+1] \subseteq A_{2 k} \cap A_{2 k+1}$. 这说明它们也满足条件 (1) 且 $[0, t+1]$ 上任意一点至多包含在 $\left[\frac{n+1}{2}\right]+1=\left[\frac{n+3}{2}\right]$ 个线段中. 这说明 $\left[\frac{n+3}{2}\right]$ 是最优的.

例 8 设 $M=\{1,2, \cdots, 10\}$, 对于 $M$ 的一个分划 $A_{1}, A_{2}, A_{3}$ ( $A_{i}$ 均非空 $)$, 若存在 $A_{1}, A_{2}, A_{3}$ 的一个排列 $A_{i_{1}}, A_{i_{2}}, A_{i_{3}}$ 使得 $\max A_{i_{k}}>\min A_{i_{k+1}}, \quad k=1,2,3$,其中 $A_{i_{4}}=A_{i_{1}}$, 则称这是一个 “好的” 分划. 求 $M$ 的所有 “好的” 分划的个数.

(刘诗雄, 2015 全国命题研讨会)

## 解 (根据吉林大学附属中学于翔宇同学的解法整理)

先把一个基本的事实即 $M$ 的三分划的个数公式作为一个引理:

引理 设 $P=\left\{\left\{A_{1}, A_{2}, A_{3}\right\} \mid\right.$ 非空集 $A_{1}, A_{2}, A_{3}$ 是 $M$ 的一个分划 $\}$, 则 $|P|=\frac{1}{6}\left(3^{10}-3 \cdot 2^{10}+3\right)=9930$.

事实上, 先计算集合方程组

$$
\left\{\begin{array}{l}
M=A_{1} \cup A_{2} \cup A_{3} \\
A_{i} \cap A_{j}=\emptyset(1 \leq i \neq j \leq 3)
\end{array}\right.
$$

的非空有序解的个数.

由于 $M$ 中的每一个元 $x$ 恰好属于 $A_{1}, A_{2}, A_{3}$ 之一, 故 (*) 的有序解的个数为 $3^{10}$, 但其中包含了有一个集合是空集和有两个集合是空集的情况. 一个为空集的有 $3 \cdot 2^{10}$ 个, 两个为空集的有 3 个, 所以由容斥原理知 (*) 的非空有序解的个数为 $3^{10}-3 \cdot 2^{10}+3$ 个.

注意到 $P$ 的无序性, 知 $|P|=\frac{1}{6}\left(3^{10}-3 \cdot 2^{10}+3\right)$. 引理得证.

回到原题. 我们先说明, 对于非好的三个集合均非空的分划, 以下性质中至少一个成立:

(i) 1 所在的集合恰为 $\{1,2, \cdots, k\}, k \leq 8$;

(ii) 10 所在的集合恰为 $\{l, \cdots, 9,10\}, l \geq 3$.

事实上,一方面, 对满足 (i) 或 (ii) 的分划, 要么存在一个集合的最大元小于另外两个的最小元, 要么存在一个集合的最小元大于另外两个的最大元, 均不是好的分划.

另一方面, 对于一个不是好的分划 $M=A \cup B \cup C$, 其中 $A, B, C$ 互不相交且均非空. 不妨设 $1 \in A$.

(1) 若同时 $10 \in A$, 不妨设 $\max B>\max C$, 则 $\{A, B, C\}$ 这一循环排列满足好分划的定义, 矛盾!

(2) 若 $10 \notin A$, 不妨设 $10 \in B$. 假设 (i) 与 (ii) 均不成立, 那么存在 $i<k, i \notin$ $A, k \in A$, 也存在 $l<j, l \in B, j \notin B$. 若此时有 $\max A>\min B$, 则 $\{A, B, C\}$ 这一循环排列满足好分划的定义, 矛盾! 若此时 $\max A<\min B$, 则上述的 $i$ 与 $j$ 均在 $C$ 中, 这时 $\max A>\min C, \max C>\min B$. 这时循环排列 $\{A, C, B\}$ 满足好分划的定义, 矛盾! 这就证明了非好分划必定满足 (i),(ii) 中至少一个.

现在来计算非好分划的个数.

满足 (i) 的分划有 $\frac{1}{2} \sum_{k=1}^{8}\left(2^{10-k}-2\right)=2^{9}-10$ 个, 满足 (ii) 的分划有 $\frac{1}{2} \sum_{l=3}^{10}\left(2^{l-1}-\right.$ 2) $=2^{9}-10$ 个, 同时满足 (i),(ii) 的分划有 $\left(\begin{array}{l}9 \\ 2\end{array}\right)$ 个.

因此由容斥原理, 三个集合均非空的非好分划的个数为 $2\left(2^{9}-10\right)-\left(\begin{array}{l}9 \\ 2\end{array}\right)=968$,再应用引理知好分划的个数为 $|P|-968=9930-968=8362$ 个.

