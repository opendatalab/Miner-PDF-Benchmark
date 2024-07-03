数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2019 美国 HMMT 2 月赛部分试题评析 

杨铮<br>(上海市上海中学, 200231)<br>指导教师: 王广廷

2019 年美国哈佛一麻省理工大学数学锦标赛 (HMMT) 二月场于今年 2 月如期举行. 下面是其中部分试题的解与评析, 供读者参考. 其中部分解答参考了官方答案.

## I、个人赛: 代数和数论

题 1. 已知函数 $f: \mathbb{N} \rightarrow \mathbb{R}$ 满足 $f(1)>0$ 且对任意自然数 $n$ 均有:

$$
\sum_{d \mid n} f(d) f\left(\frac{n}{d}\right)=1
$$

求 $f\left(2018^{2019}\right)$.

解 首先对所有素数 $p$ 和非负整数 $\alpha$, 求 $f\left(p^{\alpha}\right)$.

由题可知, 取 $n=1$ 时, $f(1)^{2}=1$. 结合 $f(1)>0$ 知 $f(1)=1$.

对每个素数 $p$, 记 $a_{t}=f\left(p^{t}\right), t \in \mathbb{N}$, 则 $a_{0}=1$ 且对任意 $t \in \mathbb{N}$, 有

$$
1=\sum_{d \mid p^{t}} f(d) f\left(\frac{p^{t}}{d}\right)=\sum_{u=0}^{t} f\left(p^{u}\right) f\left(\frac{p^{t}}{p^{u}}\right)=\sum_{u=0}^{t} a_{u} a_{t-u}
$$

因此考虑母函数

$$
g(x)=\sum_{t=0}^{+\infty} a_{t} x^{t}
$$

则

$$
(g(x))^{2}=\left(\sum_{t=0}^{+\infty} a_{t} x^{t}\right)^{2}=\sum_{t=0}^{+\infty}\left(\sum_{u=0}^{t} a_{u} a_{t-u}\right) x^{t}=\sum_{t=0}^{+\infty} 1 \cdot x^{t}=(1-x)^{-1}
$$

由 $a_{0}=1$ 并结合广义的二项式定理知

修订日期: 2019-05-19.

$$
\begin{aligned}
g(x) & =(1-x)^{-\frac{1}{2}}=\sum_{t=0}^{+\infty}\left(\begin{array}{c}
-\frac{1}{2} \\
t
\end{array}\right)(-1)^{t} x^{t} \\
& =\sum_{t=0}^{+\infty}\left(\frac{\prod_{i=1}^{t}\left(-\frac{1}{2}-i\right)}{t !}\right)(-1)^{t} x^{t} \\
& =\sum_{t=0}^{+\infty}\left(\frac{(2 t-1) !}{2^{t} t !}\right) \cdot \frac{\prod_{i=1}^{t}(2 i)}{t ! \cdot 2^{t}} \cdot x^{t} .
\end{aligned}
$$

故对 $t \in \mathbb{N}$, 有 $a_{t}=\frac{1}{2^{2 t}}\left(\begin{array}{c}2 t \\ t\end{array}\right)$. 故

$$
f\left(p^{t}\right)=\frac{1}{2^{2 t}}\left(\begin{array}{c}
2 t \\
t
\end{array}\right) .
$$

再对 $n$ 进行归纳证明: 若 $n$ 的标准分解为 $n=\prod_{i=1}^{l} p_{i}^{\alpha_{i}}$, 则

$$
f(n)=\prod_{i=1}^{l} f\left(p_{i}^{\alpha_{i}}\right) .
$$

$n=1$ 时 (2) 成立. 若 $n \leq n^{\prime}-1\left(n^{\prime} \in \mathbb{N}^{*}, n^{\prime} \geq 2\right)$ 时成立, 则 $n=n^{\prime}$ 时, 由归纳假设 (此处 $n=\prod_{i=1}^{l} p_{i}^{\alpha_{i}}$ 为 $n$ 的标准分解) 及 $f(1)=1$,

$$
\begin{aligned}
1 & =\sum_{d \mid n} f(d) f\left(\frac{n}{d}\right)=\prod_{i=1}^{l}\left(\sum_{d \mid p^{\alpha_{i}}} f(d) f\left(\frac{n}{d}\right)\right)=\prod_{i=1}^{l}\left(\sum_{t_{i}=0}^{\alpha_{i}} f\left(p_{i}^{t_{i}}\right) f\left(p_{i}^{\alpha_{i}-t_{i}}\right)\right) \\
& =\sum_{\substack{0 \leq t_{1} \leq \alpha_{1}, 0 \leq t_{2} \leq \alpha_{2}, \cdots, 0 \leq t_{l} \leq \alpha_{l}}}\left(\prod_{i=1}^{l} f\left(p_{i}^{t_{i}}\right) \prod_{i=1}^{l} f\left(p_{i}^{\alpha_{i}-t_{i}}\right)\right) \\
& =\sum_{\substack{0 \leq t_{1} \leq \alpha_{1}, 0 \leq t_{2} \leq \alpha_{2}, \cdots, 0 \leq t_{l} \leq \alpha_{l},\left(t_{1}, t_{2}, \cdots, t_{l}\right) \neq(0,0, \cdots, 0) \\
\left(t_{1}, t_{2}, \cdots, t_{l}\right) \neq\left(\alpha_{1}, \alpha_{2}, \cdots, \alpha_{l}\right)}} f\left(\prod_{i=1}^{l} p_{i}^{t_{i}}\right) f\left(\prod_{i=1}^{l} p_{i}^{\alpha_{i}-t_{i}}\right)+2 \prod_{i=1}^{l} f\left(p_{i}^{\alpha_{i}}\right) \prod_{i=1}^{l} f(1) \\
& =\left(\sum_{\substack{l \mid n, d \neq 1, d \neq n \\
d i=1}} f(d) f\left(\frac{n}{d}\right)\right)+2\left(\prod_{i=1}^{l} f\left(p_{i}^{\alpha_{i}}\right)\right) f(1) .
\end{aligned}
$$

故有

$$
2 f(n) f(1)=2 \prod_{i=1}^{l} f\left(p_{i}^{\alpha_{i}}\right) f(1)
$$

因此

$$
f(n)=\prod_{i=1}^{l} f\left(p_{i}^{\alpha_{i}}\right)
$$

$n=n^{\prime}$ 时 (2) 成立. 故 (2) 证毕!
故由 (1), (2) 知:

$$
f\left(2018^{2019}\right)=f\left(2^{2019} \cdot 1009^{2019}\right)=f\left(2^{2019}\right) f\left(1009^{2019}\right)=\frac{1}{2^{8076}}\left(\begin{array}{l}
4038 \\
2019
\end{array}\right)^{2} .
$$

故

$$
f\left(2018^{2019}\right)=\frac{1}{2^{8076}}\left(\begin{array}{c}
4038 \\
2019
\end{array}\right)^{2}
$$

评析 先代几个 $n$ 的值进行尝试或从递推式本身进行观察, 可以猜到或者看出 $f(n)$ 在 $\mathbb{N}^{*}$ 上的积性, 从而只需对素数 $p$ 或和非负整数 $\alpha$ 来求 $f\left(p^{\alpha}\right)$. 而记 $a_{t}=f\left(p^{t}\right)$ 则有 $\sum_{t=0}^{m} a_{t} a_{m-t}=1$, 对 $m \in \mathbb{N}$ 成立, 这让我们想到母函数. 如果一时想不到母函数, 也可以先算几个 $a_{t}$ 再去猜通项, 最后化为去证对 $n \in \mathbb{N}$, 有

$$
\sum_{t=0}^{n}\left(\begin{array}{c}
2 t \\
t
\end{array}\right)\left(\begin{array}{c}
2(n-t) \\
n-t
\end{array}\right)=4^{n}
$$

这个组合恒等式应该是熟悉的, 证明方法中较为普遍的是用母函数, 读者有兴趣的可以尝试寻找它的不用母函数的证明.

题 2. 数列 $\left\{a_{n}\right\}_{n=0}^{\infty}$ 满足 $a_{0}=3, a_{1}=4$, 且有

$$
a_{n+2}=a_{n+1} a_{n}+\left\lceil\sqrt{a_{n+1}^{2}-1} \sqrt{a_{n}^{2}-1}\right\rceil
$$

对 $n \geq 0$ 成立, 求

$$
\sum_{n=0}^{\infty}\left(\frac{a_{n+3}}{a_{n+2}}-\frac{a_{n+2}}{a_{n}}+\frac{a_{n+1}}{a_{n+3}}-\frac{a_{n}}{a_{n+1}}\right) .
$$

解 记 $a_{-1}=1$, 下面对 $n$ 进行归纳证明: $n \geq 1$ 时,

$$
a_{n+1}=2 a_{n} a_{n-1}-a_{n-2} .
$$

$n=1$ 时, 由题得

$$
a_{2}=a_{0} a_{1}+\left\lceil\sqrt{a_{0}^{2}-1} \sqrt{a_{1}^{2}-1}\right\rceil=3 \times 4+\lceil\sqrt{120}\rceil=23=2 a_{1} a_{0}-a_{-1} .
$$

则 (1) 成立.

若 $n \leq n^{\prime}-1\left(n^{\prime} \in \mathbb{N}^{*}, n^{\prime} \geq 2\right)$ 时 (1) 成立, 则由归纳假设知

$$
a_{-1} \leq a_{0} \leq a_{1} \leq a_{2} \leq \cdots \leq a_{n^{\prime}}
$$

则

$$
\begin{aligned}
& 2 a_{n} a_{n-1} a_{n-2}+2-a_{n}^{2}-a_{n-1}^{2}-a_{n-2}^{2}=\left(2 a_{-1} a_{0} a_{1}+2-a_{-1}^{2}-a_{0}^{2}-a_{1}^{2}\right) \\
+ & \sum_{i=2}^{n}\left(\left(2 a_{i} a_{i-1} a_{i-2}+2-a_{i}^{2}-a_{i-1}^{2}-a_{i-2}^{2}\right)-\left(2 a_{i-1} a_{i-2} a_{i-3}+2-a_{i-1}^{2}-a_{i-2}^{2}-a_{i-3}^{2}\right)\right) \\
= & 2 \cdot 1 \cdot 3 \cdot 4+2-1^{2}-3^{2}-4^{2}+\sum_{i=2}^{n}\left(a_{i}-a_{i-3}\right)\left(2 a_{i-1} a_{i-2}-a_{i}-a_{i-3}\right)
\end{aligned}
$$

$=0+\sum_{i=2}^{n}\left(a_{i}-a_{i-3}\right) \cdot 0=0$.

因此 $-a_{n}^{2}-a_{n-1}^{2}=-2 a_{n} a_{n-1} a_{n-2}-2+a_{n-2}^{2}$. 故

$$
\begin{aligned}
\left(a_{n}^{2}-1\right)\left(a_{n-1}^{2}-1\right) & =a_{n}^{2} a_{n-1}^{2}-a_{n}^{2}-a_{n-1}^{2}+1 \\
& =a_{n}^{2} a_{n-1}^{2}-2 a_{n} a_{n-1} a_{n-2}-2+a_{n-2}^{2}+1 \\
& =\left(a_{n} a_{n-1}-a_{n-2}\right)^{2}-1 .
\end{aligned}
$$

易证 $a_{n} a_{n-1}-a_{n-2}>1$. 所以

$$
\begin{aligned}
a_{n+1} & =a_{n} a_{n-1}+\left\lceil\sqrt{a_{n}^{2}-1} \sqrt{a_{n-1}^{2}-1}\right\rceil \\
& =a_{n} a_{n-1}+\left(a_{n} a_{n-1}-a_{n-2}\right) \\
& =2 a_{n} a_{n-1}-a_{n-2} .
\end{aligned}
$$

(1) 在 $n=n^{\prime}$ 时成立. 因此 (1) 证毕!

因此由 (1) 可知

$$
\begin{aligned}
& \sum_{n=0}^{\infty}\left(\frac{a_{n+3}}{a_{n+2}}-\frac{a_{n+2}}{a_{n}}+\frac{a_{n+1}}{a_{n+3}}-\frac{a_{n}}{a_{n+1}}\right) \\
= & \sum_{n=0}^{\infty}\left(\frac{2 a_{n+1} a_{n+2}-a_{n}}{a_{n+2}}-\frac{2 a_{n+1} a_{n}-a n-1}{a_{n}}+\frac{n_{n+1}}{a_{n+3}}-\frac{a_{n}}{a_{n+1}}\right) \\
= & \sum_{n=0}^{\infty}\left(-\frac{a_{n}}{a_{n+2}}+2 a_{n+1}+\frac{a_{n-1}}{a_{n}}-2 a_{n+1}+\frac{a_{n+1}}{a_{n+3}}-\frac{a_{n}}{a_{n+1}}\right) \\
= & \sum_{n=0}^{\infty}\left(-\frac{a_{n}}{a_{n+2}}+\frac{a_{n-1}}{a_{n}}+\frac{a_{n+1}}{a_{n+3}}-\frac{a_{n}}{a_{n+1}}\right) \stackrel{\text { def }}{=} S .
\end{aligned}
$$

由 (1) 易知 $n \geq 2$ 时 $a_{n} \geq a_{n-1} a_{n-2} \geq 3 a_{n-1}$, 故 $n \geq 3$ 时,

$$
\frac{a_{n-1}}{a_{n}} \leq \frac{1}{a_{n-2}}=\frac{1}{a_{0}} \cdot \prod_{i=1}^{n-2} \frac{a_{i-1}}{a_{i}} \leq \frac{1}{a_{0}} \cdot \frac{3}{4} \cdot\left(\frac{1}{3}\right)^{n-3}=\left(\frac{1}{3}\right)^{n-2} \cdot \frac{3}{4} .
$$

因此

$$
\sum_{n=0}^{\infty}\left(-\frac{a_{n}}{a_{n+2}}\right)+\sum_{n=0}^{\infty} \frac{a_{n-1}}{a_{n}}+\sum_{n=0}^{\infty} \frac{a_{n+1}}{a_{n+3}}+\sum_{n=0}^{\infty}\left(-\frac{a_{n}}{a_{n+1}}\right)
$$

绝对收敛. 故

$$
S=\sum_{n=0}^{\infty}\left(-\frac{a_{n}}{a_{n+2}}+\frac{a_{n-1}}{a_{n}}\right)+\sum_{n=1}^{\infty}\left(\frac{a_{n}}{a_{n+2}}-\frac{a_{n-1}}{a_{n}}\right)=-\frac{a_{0}}{a_{2}}+\frac{a_{-1}}{a_{0}}=\frac{14}{69} .
$$

故所求和为 $\frac{14}{69}$.

评析 先去算一下 $\left\{a_{n}\right\}$ 的前几项并去猜测递推式就会发现 $\left(a_{n}^{2}-1\right)\left(a_{n+1}^{2}-\right.$ 1) +1 是完全平方数和 (1), 之后用韦达跳跃就能将各个猜测证出. 最后计算 $S$
的值时也要大胆地去想能否用一些简单的变形就能将 $S$ 进行裂项, 同时注意不要算错.

## II、个人赛: 组合

题 3. 对一个正整数 $N$, 我们将 $N$ 的正因子 (包括 1 和 $N$ ) 用四种颜色染色.一种染色方式称为“好的”, 若当 $a, b$ 和 $(a, b)$ 是 $N$ 的不同正因子时, 它们的颜色两两不同. 问: 对于一个不是素数幂的整数, 其好的染色方式至多有多少种?

解 若 $N$ 有三个或三个以上不同素因子, 记为 $p, q, r$.

下证对 $N$ 没有好的染色方式. 若有, 则由定义, $p, q, r, 1$ 颜色互不相同. 故考虑 $p q, r$, 和 $1=\operatorname{gcd}(p q, r)$ 的颜色知 $p q$, 和 $1, r$ 均不同色. 再考虑 $n$ 的正因子

$$
p q, r q, q=\operatorname{gcd}(p q, r q)
$$

和

$$
p q, r q, p=\operatorname{gcd}(p q, r p)
$$

知 $p q$ 和 $p, q$ 均不同色. 但 $p, q, r, 1$ 互不同色, 且一共只有四种颜色, 故矛盾!

故对 $N$ 没有好的染色方式.

下设 $N$ 有两个不同的素因子 $p, q$. 记 $N=p^{\alpha} q^{\beta}\left(\alpha, \beta \in \mathbb{N}^{*}\right)$, 并不妨设 $\alpha \geq \beta$.

对 $\alpha_{1}<\alpha_{2}\left(\alpha_{1}, \alpha_{2} \in \mathbb{N}, 0 \leq \alpha_{1}<\alpha_{2} \leq \alpha\right)$, 考虑 $N$ 的正因子

$$
p^{\alpha_{2}}, q p^{\alpha_{1}}, p^{\alpha_{1}}=\operatorname{gcd}\left(p^{\alpha_{2}}, q p^{\alpha_{1}}\right)
$$

知 $p^{\alpha_{1}}, p^{\alpha_{2}}, q p^{\alpha_{1}}$ 两两不同色.

因此所有 $p^{i}(0 \leq i \leq \alpha)$ 互不同色, 且它们与 $q$ 的颜色也互不相同, 故 $\alpha+2 \leq 4$, 故 $\alpha \leq 2$.

若 $\beta \geq 2$, 则 $\alpha \geq \beta \geq 2$. 考虑 $N$ 的五个因子 $p^{2}, p, p q, q, q^{2}$, 则其中任两个不同色 (因为考虑 $p^{2}, p q, p=\operatorname{gcd}\left(p^{2}, p q\right)$ 和 $q^{2}, p q, q=\operatorname{gcd}\left(q^{2}, p q\right)$ 知 $p^{2}, p, p q ; p q, q, q^{2}$, 不同色, 而 $p, p^{2}$ 中任一个和 $q, q^{2}$ 中任一个的最大公约数都是 1 , 因此不同色. 故 $p^{2}, p, p q, q, q^{2}$, 互不同色). 但只有四种颜色, 故对 $N$ 不存在好的染色方式. 故下可设 $\beta=1$.

此时由 (1) 易证对 $N$ 的全体好的染色方式为: 使 $1, p, p^{2}, \cdots, p^{\alpha}$ 颜色互不相同, 且使对每个 $i(0 \leq i \leq \alpha-1)$ 都有 $p^{i} q$ 和 $p^{i}, p^{i+1}, \cdots, p^{\alpha}$ 颜色不同的染色方式.

故 $N=p q$ 时, 对 $N$ 共有 $4 \times 3 \times 2 \times 4=96$ 种好的染色方式;

$N=p^{2} q$ 时, 共有 $4 \times 3 \times 2 \times 1 \times 2 \times 4=192$ 种好的染色方式. 这里计数时
先考虑 $1, p, p^{2}, \cdots, p^{\alpha}$ 的颜色, 再考虑 $q, p q, \cdots, p^{\alpha} q$ 的颜色.

因此答案为 192 .

评析 本题可以先猜出当 $N$ 的素因子或者素因子幂次很大的时候, 没有好的染色方式. 而在讨论的过程中则需要大胆一些. 对于那些偏向于使用几何直观思考问题的人而言, 可以通过将 $N$ 的所有因数排成一个立方体来将问题看的更清晰 (此处易证 $N$ 有不超过 3 个不同素因子, 所以立方体也不超过三维). 本题如果将四种颜色更改为五种或更多的话, 思考的难度和讨论的复杂程度将会大大增加.

题 4. 一只羊在四维空间中行走. 它从原点出发, 每一分钟, 它从位置 $\left(a_{1}, a_{2}, a_{3}, a_{4}\right)$ 走到某个位置 $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ 均是整数, 且

$$
\begin{gathered}
\left(x_{1}-a_{1}\right)^{2}+\left(x_{2}-a_{2}\right)^{2}+\left(x_{3}-a_{3}\right)^{2}+\left(x_{4}-a_{4}\right)^{2}=4 \\
\left|\left(x_{1}+x_{2}+x_{3}+x_{4}\right)-\left(a_{1}+a_{2}+a_{3}+a_{4}\right)\right|=2 .
\end{gathered}
$$

若这只羊在 40 分钟后到达 $(10,10,10,10)$. 问: 共有多少种不同的路径?

解 归纳易证该羊每步移动后的位置的四个坐标都是整数. 因此易证它每一步移动过的向量为 $(2,0,0,0),(1,1,1,-1)$ 及其负向量和 (在四个维度的坐标上的) 置换.

考虑如下坐标变换: $\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \rightarrow$

$\left(\frac{1}{2}\left(x_{1}+x_{2}+x_{3}+x_{4}\right), \frac{1}{2}\left(x_{1}+x_{2}-x_{3}-x_{4}\right), \frac{1}{2}\left(x_{1}-x_{2}+x_{3}-x_{4}\right), \frac{1}{2}\left(x_{1}-x_{2}-x_{3}+x_{4}\right)\right)$.

则它是 $\mathbb{R}^{4} \rightarrow \mathbb{R}^{4}$ 的一一映射.

该变换将该羊每一步所走过的向量变为 $( \pm 1, \pm 1, \pm 1, \pm 1$ ) (四个正负号任取), 且将起点 $(0,0,0,0)$ 变为 $(0,0,0,0)$, 终点 $(10,10,10,10)$ 变为 $(20,0,0,0)$.

在进行这个坐标变换后, 该羊所在位置的第一, 二, 三, 四个坐标在 40 步内应该分别增加 $30,20,20,20$ 次而减少 $10,20,20,20$ 次, 并可在该前提下随意从 $\{-1,1\}$ 中选择四个坐标中每一个的变化量. 因此该羊共有 $\left(\begin{array}{l}40 \\ 10\end{array}\right)\left(\begin{array}{l}40 \\ 20\end{array}\right)^{3}$ 种走法.

评析 因为本题是在四维上讨论的, 所以一般的几何感觉不能用于处理这道题. 我们只能猜测这只羊移动的方式有一个很好的化简办法. 此时注意到这只羊每步有 16 种走法, 所以可以猜测这些走法是否经过变换后能够得到一个超立方体的 16 个顶点, 而除非观察出原先题目中给出的 16 个方向向量的端点本身构成一个超立方体 (从而找出上面答案中的全等变换), 否则很难找出所想要的
坐标变换. 因此本题实际难度很大.

## III、个人赛: 几何

题 5. 平面上, 六个单位圆盘 $C_{1}, C_{2}, C_{3}, C_{4}, C_{5}, C_{6}$ 两两不相交, 且 $C_{i}$ 与 $C_{i+1}$ 相切 $(1 \leq i \leq 6)$, 其中 $C_{7}=C_{1}$. 令 $C$ 表示包含这六个圆盘面积最小的圆盘, 设 $r$ 为 $C$ 可能的最小半径, $R$ 是 $C$ 可能的最大半径. 求 $R-r$.



解 先证 $r=3$.

若存在一个半径小于 3 的圆盘 $C$ 包含 $C_{1}, C_{2}, C_{3}, C_{4}, C_{5}, C_{6}$, 则记 $C$ 的圆心为 $O$ 并记 $C_{i}$ 的圆心为 $O_{i}(1 \leq i \leq 6)$. 以 $O$ 为中心, 作三条直线, 将平面分为六个区域, 其中任两条直线的夹角为 $\frac{\pi}{3}$ (六个区域均含其边界). 此时 $O_{1}, O_{2}, O_{3}, O_{4}, O_{5}, O_{6}$ 中必有两个在同一区域中, 记为 $O_{j_{1}}, O_{j_{2}}$, 则

$$
\left|O_{j_{1}} O_{j_{2}}\right| \geq 2,\left|O O_{j_{1}}\right|<2,\left|O O_{j_{2}}\right|<2
$$

且

$$
\angle O_{j_{1}} O O_{j_{2}} \leq \frac{\pi}{3}
$$

由大边对大角知 $\angle O_{j_{1}} O O_{j_{2}}$ 是 $\triangle O O_{j_{1}} O_{j_{2}}$ 唯一的最大内角, 故 $\angle O_{j_{1}} O O_{j_{2}}>\frac{\pi}{3}$,与 $\angle O_{j_{1}} O O_{j_{2}}<\frac{\pi}{3}$ 矛盾! 故 $r \geq 3$.

而当 $O_{1}, O_{2}, O_{3}, O_{4}, O_{5}, O_{6}$ 分别是一个边长为 2 的正六边形顺次的六个顶点时, 取 $O$ 为该六边形中心, 而 $C$ 的半径为 3 , 则 $C$ 包含 $C_{1}, C_{2}, C_{3}, C_{4}, C_{5}, C_{6}$.因此 $r \leq 3$, 故 $r=3$.

再证 $R=2+\sqrt{3}$. 仍记 $C_{i}$ 的圆心为 $O_{i}(1 \leq i \leq 6)$ 且 $C$ 的圆心为 $O$.

取 $O_{1}, O_{2}, O_{4}, O_{5}$ 分别为边长为 2 的正方形的顺次的四个顶点, 而 $O_{3}, O_{6}$在 $O_{1} O_{2} O_{4} O_{5}$ 外且使得 $\triangle O_{2} O_{3} O_{4}$ 和 $\triangle O_{5} O_{6} O_{1}$ 都是边长为 2 的正三角形, 则 $\left|O_{3} O_{6}\right|=2+2 \sqrt{3}$. 从而可以取出 $C_{3}, C_{6}$ 上各一个点 $A, B$, 使得

$$
|A B|=4+2 \sqrt{3}
$$

因此 $C$ 内 (或边界上) 两个点 $A, B$ 使得 $|A B|=4+2 \sqrt{3}$. 故

$$
2 R \geq|A B|=4+2 \sqrt{3}
$$

即 $R \geq 2+\sqrt{3}$.

下证 $R \leq 2+\sqrt{3}$. 为此只需对每种 $C_{1}, C_{2}, C_{3}, C_{4}, C_{5}, C_{6}$ 可能的位置找一个半径为 $(2+\sqrt{3})$ 的圆盘 $C^{\prime}$ 包含 $C_{1}, C_{2}, C_{3}, C_{4}, C_{5}, C_{6}$. 直接取 $C^{\prime}$ 以 $C_{1} C_{4}$ 中点 $O^{\prime}$ 为圆心, $(2+\sqrt{3})$ 为半径. 则只需证明

$$
\left|O^{\prime} O_{i}\right| \leq 1+\sqrt{3}(i=1,2, \cdots, 6) .
$$

下只需证

$$
\left|O_{1} O^{\prime}\right| \leq 1+\sqrt{3},\left|O_{2} O^{\prime}\right| \leq 1+\sqrt{3} \text {. }
$$

其余类似可证.

取 $O_{1} O_{3}$ 中点 $D$. 由 $\left|O_{1} O_{2}\right|=\left|O_{2} O_{3}\right|=2$ 及 $\left|O_{1} O_{3}\right| \geq 2$ 知 $O_{2} D \perp O_{1} O_{3}$, 故

$$
\left|O_{2} D\right|=\sqrt{O_{1} O_{2}^{2}-O_{1} D^{2}} \leq \sqrt{2^{2}-1^{2}}=\sqrt{3}
$$

又可得 $O^{\prime} D$ 是 $\triangle O_{1} O_{3} O_{4}$ 平行于 $O_{3} O_{4}$ 的中位线, 从而

$$
\left|O^{\prime} D\right|=\frac{1}{2}\left|O_{3} O_{4}\right|=1
$$

故

$$
\left|O^{\prime} O_{2}\right| \leq\left|O^{\prime} D\right|+\left|D O_{2}\right| \leq 1+\sqrt{3} \text {. }
$$

又取 $O_{2} O_{5}$ 中点 $O^{\prime \prime}, O_{2} O_{6}$ 中点 $E, O_{3} O_{5}$ 的中点 $F$, 则同理

$$
\left|O_{1} E\right| \leq \sqrt{3},\left|O_{4} F\right| \leq \sqrt{3}, \quad\left|O^{\prime \prime} E\right|=\left|O^{\prime \prime} F\right|=1 .
$$

因此

$$
\left|O_{1} O^{\prime}\right|=\frac{1}{2}\left|O_{1} O_{4}\right| \leq \frac{1}{2}\left(\left|O_{1} E\right|+\left|E O^{\prime \prime}\right|+\left|O^{\prime \prime} F\right|+\left|F O_{4}\right|\right) \leq 1+\sqrt{3} .
$$

类似可证 $\left|O^{\prime} O_{i}\right| \leq 1+\sqrt{3}(i=1,2, \cdots, 6)$. 因此已得出 $R \leq 2+\sqrt{3}$. 故

$$
R=2+\sqrt{3} \text {. }
$$

故

$$
R-r=(2+\sqrt{3})-3=\sqrt{3}-1
$$

评析 本题最难的部分之一在于猜答案. 将 $R$ 与 $r$ 的值猜出后 $r=3$ 是容易证出的, 不用最大角也可以用余弦定理或几何直观得出 $\angle O_{j_{1}} O O_{j_{2}}$ 有关的矛盾.而 $2+\sqrt{3}$ 则要难一些. 在相信 $R=2+\sqrt{3}$ 并相信直接取 $O_{1} O_{4}$ 中点为 $C$ 的圆心就可以时, 是通过仔细分析题目条件 (具体是在确定 $\left|O_{1} O_{3}\right|$ 时让 $\left|O_{2} O^{\prime}\right|$ 最大)
后能放出答案中所述的三角不等式, 也可以通过投影 (而不是巧妙地放三角不等式) 得出 $\left|O_{1} O_{4}\right| \leq 2+2 \sqrt{3}$. 但是在没有对 $O$ 的位置和 $R$ 的大小有坚定的信念的情况下很难想到去放出这个三角不等式. 因此本题也很有难度.

## IV、团体赛

题 6. 已知 $0<\theta<\frac{\pi}{2}$. 证明:

$$
0<\sin \theta+\cos \theta+\tan \theta+\cot \theta-\sec \theta-\csc \theta<1 \text {. }
$$

证明一 记 $f(\theta)=\sin \theta+\cos \theta+\tan \theta+\cot \theta-\sec \theta-\csc \theta\left(0<\theta<\frac{\pi}{2}\right)$. 则

$$
\begin{aligned}
f^{\prime}(\theta) & =\cos \theta-\sin \theta+\frac{1}{\cos ^{2} \theta}-\frac{1}{\sin ^{2} \theta}-\frac{\sin \theta}{\cos ^{2} \theta}+\frac{\cos \theta}{\sin ^{2} \theta} \\
& =(\cos \theta-\sin \theta)\left(1-\frac{\cos \theta+\sin \theta}{\cos ^{2} \theta \sin ^{2} \theta}+\frac{\cos ^{2} \theta+\cos \theta \sin \theta+\sin ^{2} \theta}{\sin ^{2} \theta \cos ^{2} \theta}\right) \\
& =(\cos \theta-\sin \theta)\left(\frac{-(\cos \theta+\sin \theta)+\left(\frac{1}{2}+\frac{1}{2}(\cos \theta+\sin \theta)^{2}\right)}{\sin ^{2} \theta \cos ^{2} \theta}+1\right) \\
& =(\cos \theta-\sin \theta)\left(\frac{(\cos \theta+\sin \theta-1)^{2}}{2 \sin ^{2} \theta \cos ^{2} \theta}+1\right),
\end{aligned}
$$

故 $f^{\prime}(\theta)$ 与 $(\cos \theta-\sin \theta)$ 符号相同. 因此

$$
f^{\prime}(\theta)= \begin{cases}>0, & \left(0<\theta<\frac{\pi}{4}\right) \\ =0, & \left(\theta=\frac{\pi}{4}\right) \\ <0, & \left(\frac{\pi}{4}<\theta<\frac{\pi}{2}\right)\end{cases}
$$

故对 $\theta \in\left(0, \frac{\pi}{2}\right)$, 有

$$
f(\theta) \leq f\left(\frac{\pi}{4}\right)=\frac{\sqrt{2}}{2}+\frac{\sqrt{2}}{2}+1+1-\sqrt{2}-\sqrt{2}=2-\sqrt{2}<1 .
$$

证毕!

证明二 记 $X_{1}(\cos \theta, 0), Y_{1}(0, \sin \theta), O(0,0), X_{2}(\sec \theta, 0), Y_{2}(0, \csc \theta)$, 则

$$
\left|X_{1} Y_{1}\right|=1, \quad\left|X_{1} X_{2}\right|=\sec \theta-\cos \theta, \quad\left|Y_{1} Y_{2}\right|=\csc \theta-\sin \theta
$$

且

$$
\left|X_{2} Y_{2}\right|=\sqrt{\sec ^{2} \theta+\csc ^{2} \theta}=\frac{1}{\sin \theta \cos \theta}=\tan \theta+\cot \theta .
$$

因此

$$
\begin{aligned}
& \sin \theta+\cos \theta+\tan \theta+\cot \theta-\sec \theta-\csc \theta \\
= & -\left|Y_{1} Y_{2}\right|-\left|X_{1} X_{2}\right|+\left|X_{2} Y_{2}\right| \leq\left|X_{1} Y_{1}\right|=1 .
\end{aligned}
$$

因为 $X_{1}, Y_{1}, X_{2}, Y_{2}$ 不共线, 所以上式等号不成立. 证毕!
评析 证明一是常规的做法. 而证明二则是在标准答案 (记 $Z(\cos \theta, \sin \theta)$,并作 $Z$ 在 $x$ 轴, $y$ 轴上的投影 $X_{1}, Y_{1}$, 再过 $Z_{1}$ 作单位圆的切线交 $x$ 轴, $y$ 轴分别于 $X_{2}, Y_{2}$, 并按证法二使用三角不等式) 的基础上整理得到.

题 7. 不等边三角形 $A B C$ 满足 $\angle A=60^{\circ}$. 点 $O, H, I$ 分别是 $\triangle A B C$ 的外心, 垂心, 内心. 点 $D$ 是直线 $B C$ 与 $\angle A$ 的内角平分线的交点, 点 $X$ 在 $\triangle I H O$ 的外接圆上, $T$ 是直线 $B C$ 与 $\angle A$ 邻补角角平分线的交点, 且满足 $H X / / A I$. 证明: $O D \perp T X$.



证明 下只说明 $\triangle A B C$ 为锐角三角形的情况. 其余情况类似可证.由题易证

$$
\begin{gathered}
\angle B H C=\pi-\angle B A C=\frac{2 \pi}{3}, \\
\angle B I C=\frac{\pi}{2}+\frac{1}{2} \angle B A C=\frac{2 \pi}{3}, \\
\angle B O C=2 \angle B A C=\frac{2 \pi}{3},
\end{gathered}
$$

故 $B, H, I, O, C$ 共圆.

由熟知的结论知 $I B$ 平分 $\angle O B H$, 故 $H I=I O$. 又易知 $A I$ 与 $\odot(A B C)$ 的另一交点为 $\odot(B I C)$ 的圆心. 结合 $H I=I O$ 及垂径定理知 $A I \perp O H$. 故由 $A I / / H X$ 知 $H X \perp O H$. 故 $O X$ 是 $\odot(B H I O C)$ 的直径. 故由 $B O=O C$ 知

$$
O X \perp B C \text {. }
$$

记 $O X$ 交 $B C$ 于 $E$, 则 $E$ 为 $B C$ 的中点, 由 $A B, A C, A D, A T$ 构成调和线束知 $B, C, D, T$ 构成调和点列. 因此由调和点列的性质知

$$
E D \cdot E T=E B^{2}=E B \cdot E C=E O \cdot E X .
$$

故 $\frac{E D}{E O}=\frac{E X}{E T}$. 结合 $\angle O E D=\angle T E X=\frac{\pi}{2}$ 知

$$
\triangle D E O \sim \triangle X E T .
$$

故

$$
\angle D O X+\angle O X T=\angle D O E+\angle E X T=\angle D O E+\angle E D O=\frac{\pi}{2}
$$

故 $O D \perp T X$. 证毕!

评析 熟知 (当 $\angle B A C=\frac{\pi}{3}$ ), $B, H, I, O, C$ 共圆, 且 $A I \perp O H$, 且画图可猜到 $X, O$ 是 $\odot(B O C)$ 的一对对径点, 因此题中结论 $O D \perp T X$ 可以转化为相对容易处理的对象 (如直线 $B C$, 点 $D, T$ 在 $B C$ 的位置关系) 更接近的命题 “ $D$ 是 $\triangle O T X$ ”的垂心, 此时它又能转化为 $E O \cdot E X=E D \cdot E T$. 即 $E B^{2}=E D \cdot E T$,而这是 $B, C, D, T$ 构成调和点列的推论.

题 8. 令 $\mathbb{N}^{*}=\{1,2,3, \cdots\}$ 表示正整数集, $f$ 是 $\mathbb{N}^{*}$ 到 $\mathbb{N}^{*}$ 的双射, 是否存在正整数 $n$, 使得 $(f(1), f(2), \cdots, f(n))$ 是 $(1,2,3, \cdots, n)$ 的一个排列?

解 不一定存在.

取 $T=\left\{2^{2^{i}} \mid i \in \mathbb{N}^{*}\right\}, U=\mathbb{N}^{*} \backslash T$. 对 $i \in \mathbb{N}^{*}$, 记 $a_{i}$ 为 $U$ 中第 $i$ 小的数. 取 $f$如下:

$$
f\left(a_{i}\right)=2^{2^{i}}, f\left(2^{2^{i}}\right)=a_{i}, i \in \mathbb{N}^{*}
$$

则由 $T=\left\{2^{2^{i}} \mid i \in \mathbb{N}^{*}\right\}, U=\left\{a_{i} \mid i \in \mathbb{N}^{*}\right\}$ 是 $\mathbb{N}^{*}$ 的一个划分知 $f$ 是 $\mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$ 的一个双射, 且

$$
\{f(u) \mid u \in U\}=T,\{f(t) \mid t \in T\}=U
$$

故若存在 $n \in \mathbb{N}^{*}$ 使 $(f(1), f(2), \cdots, f(n))$ 是 $(1,2,3, \cdots, n)$ 的一个排列, 则记 $[n]=\{1,2,3, \cdots, n\}$, 则

$$
\{f(u) \mid u \in U \cap[n]\}=T \cap[n], \quad\{f(t) \mid t \in T \cap[n]\}=U \cap[n] .
$$

因此 $|T \cap[n]|=|U \cap[n]|$. 所以

$$
|T \cap[n]|=\frac{n}{2}
$$

故

$$
2^{2^{\frac{n}{2}}}=\max _{t \in T \cap[n]}\{t\} \leq n .
$$

这不可能. 故不一定存在这样的 $n$.

评析上述做法应该来说已经成为一种套路了. 对处理这种看似苛刻的限制时, 利用无限集可以充分向外延伸这一特点, 构造映射往往有神奇的效果. 通常的处理方式是对每个 $n$, 在充分远处找一个数 $m$, 使得 $f(n)=m$, 再从的“更
远”的地方找一个数 $m_{2}$, 使得 $f\left(m_{2}\right)=n$. 因为对无穷集合, 在每个“更远”之外还有更远的地方, 所以不会产生矛盾. 类似的题有今年中国 TST二阶段第一天的第 3 题和“找出一个集合 $A \subset \mathbb{Z}$ 使每个 $m \in \mathbb{Z}$ 都有唯一一对 $a_{m}, b_{m} \in A$ 使 $m=2 a_{m}+3 b_{m}$ ”. 另外, 官方答案中给出的映射 $f$ 是:

$$
f(n)= \begin{cases}2 n, & n=1,2 \\ n+3, & n \geq 3,2 \nmid n \\ n-3, & n \leq 4,2 \mid n\end{cases}
$$

题 9. 一个平面上的凸多边形叫做宽的, 如果它在任意直线上的投影的长度均不小于 1. 证明: 任一宽的凸多边形都包含一个半径为 $\frac{1}{3}$ 的圆.

证明一 对每个宽的多边形 $A$. 考虑该多边形内含的圆中最大的一个, 记为 $\omega$ (容易证明所有 $A$ 内含的圆的半径构成的集合是闭集, 因此它有最大元). $\omega$ 必与 $T$ 的三条边相切.

记 $T$ 的所有与 $\omega$ 相切的边与 $\omega$ 的切点的集合为 $B$. 若 $B$ 中任三点构成钝角三角形, 则任取 $B$ 中一点 $b$ 并作 $\omega$ 的过 $b$ 的直径, 对 $B$ 在该直径两侧的点中到 $b$的距离最远的点 (共 2 个) 讨论可知必有一条直径 $l$ 使 $b$ 和这两个点在 $l$ 的同侧 (且不在 $l$ 上). 此时可知 $B$ 中所有点都在 $l$ 的该侧 (且不在 $l$ 上).

因此将 $\omega$ 的圆心向 $l$ 的另一侧稍作移动 (移动方向与 $l$ 垂直) 则可将 $\omega$ 的半径稍作增加, 而保证 $\omega$ 内含于 $A$, 与 $\omega$ 半径最大性矛盾!

故 $B$ 中有三点 $a, b, c$ 构成非针角三角形.

记 $T$ 与 $\omega$ 切于 $a, b, c$ 的边分别为 $l_{a}, l_{b}, l_{c}$, 则若 $a, b, c$ 中有两个点是 $\omega$ 的对径点, 则记为 $x, y$, 则 $A$ 包含于 $l_{x}, l_{y}$ 所在直线之间的带状区域中 (此处 $l_{x} / / l_{y}$ ).

因此 $A$ 在垂直于 $l_{x}$ 的直线上投影的长度为 $\omega$ 的半径的两倍, 故 $\omega$ 的半径不小于 $\frac{1}{2}$. 若 $a, b, c$ 没有两个点是 $\omega$ 的对径点, 则 $l_{a}, l_{b}, l_{c}$ 围成三角形 $C$, 且 $\omega$ 是 $C$的内切圆, 且 $T$ 内含于 $C$. 而记 $\omega$ 的半径为 $r, C$ 的三边长分别为 $a, b, c$, 面积为 $S$, 则 $T$ 在垂直于 $C$ 三边的直线上的投影的长度分别不大于 $\frac{2 S}{a}, \frac{2 S}{b}, \frac{2 S}{c}$. 故

$$
\frac{2 S}{a} \geq 1, \frac{2 S}{b} \geq 1, \frac{2 S}{c} \geq 1
$$

而注意到 $2 S=r(a+b+c)$, 因此

$$
\begin{aligned}
r & =\frac{1}{\frac{1}{r}\left(\frac{a}{a+b+c}+\frac{b}{a+b+c}+\frac{c}{a+b+c}\right)} \\
& =\frac{1}{\frac{a}{2 S}+\frac{b}{2 S}+\frac{c}{2 S}} \geq \frac{1}{\frac{1}{1}+\frac{1}{1}+\frac{1}{1}}=\frac{1}{3} .
\end{aligned}
$$

因此 $\omega$ 的半径不小于 $\frac{1}{3}$, 证毕!
证明二 对每个宽的多边形 $A$, 取 $A$ 的重心 $G_{A}$. 下证以 $G_{A}$ 为圆心的, $\frac{1}{3}$ 为半径的圆包含于 $A$.

若否, 则存在 $A$ 的边界上一点 $P$ 使得 $\left|G_{A} P\right| \leq \frac{1}{3}$. 过 $P$ 作直线 $l_{1}$, 使 $A$ 在 $l_{1}$的某侧. 再过 $G_{A}$ 作 $l_{2} / / l_{1}$ 交 $A$ 于两点 $B, C$. 再作另一条平行于 $l_{1}$ 的与 $A$ 的边界接触的直线 $l_{3}$, 使 $A$ 在 $l_{3}$ 的某侧 (其中 $l_{3} \neq l_{1}$ ).

记 $l_{3}$ 与 $A$ 的边界的一个公共点为 $D, D B$ 与 $D C$ 分别交 $l$ 于 $E, F$, 则 $\triangle D E F$ 比 $A$ 多了 $l_{1}, l_{2}$ 间的几块区域, 且比 $A$ 少了 $l_{2}, l_{3}$ 间的几块区域.

因此 $\triangle D E F$ 的重心 $G$ 比 $G_{A}$ 到 $l_{1}$ 的距离更短, 故 $G_{A}$ 到 $l_{1}$ 的距离小于 $\frac{1}{3}$,而 $D$ 到 $l_{1}$ (即 $E F$ ) 的距离为 $G$ 到 $l_{1}$ 的距离的三倍.

因此 $l_{3}$ 到 $l_{1}$ (即 $D$ 到 $l_{1}$ ) 的距离小于 1 . 故 $A$ 在垂直于 $l_{1}$ 的直线上的投影长度小于 1, 与 $A$ 是宽的矛盾!

故以 $G_{A}$ 为圆心的, $\frac{1}{3}$ 为半径的圆包含于 $A$. 证毕!

评析 这两个证明都整理自标准答案. 它们一个是去证明有一点 $P$ 到 $C$ 的所有边距离不大于 $\frac{1}{3}$. 另一个是稍稍加强了一些, 去证有一点在每条夹住多边形的“带子”中间 $\frac{1}{3}$ 的地方. (其中“带子”指两条直线之间的带状区域). 而这两件事情都可以用海莱定理进行证明, 有兴趣的读者可以自己进行尝试, 而标准答案比用海莱定理的叙述简单.

本题供题人是 2015 年 CMO 第一名, 2016 年 IMO 金牌张盛桐.

题 10. 证明: 对任意正整数 $n$, 多项式 $P(x)=(2 n) x^{2 n}+(2 n-1) x^{2 n-1}+$ $\cdots+(n+1) x^{n+1}+n x^{n}+(n+1) x^{n-1}+\cdots+(2 n-1) x+(2 n)$ 的所有复根的模长为 1 .

证明 易证 0 和 1 都不是 $P(x)$ 的根, 故

$$
\begin{aligned}
P(x) & =(2 n+1)\left(\sum_{i=0}^{2 n} x^{i}\right)-\left(\sum_{i=0}^{n}(i+1) x^{i}+\sum_{i=n+1}^{2 n}(2 n+1-i) x^{i}\right) \\
& =(2 n+1) \frac{x^{2 n+1}-1}{x-1}-\left(\sum_{i=0}^{n} x^{i}\right)^{2} \\
& =(2 n+1) \frac{x^{2 n+1}-1}{x-1}-\left(\frac{x^{n+1}-1}{x-1}\right)^{2} .
\end{aligned}
$$

因此

$$
\begin{gathered}
P(x)=0 \Leftrightarrow(2 n+1)\left(\frac{x^{2 n+1}-1}{x-1}\right) \\
\Leftrightarrow(2 n+1)\left(x^{2 n+1}-1\right)(x-1)=\left(x^{n+1}-1\right)^{2} .
\end{gathered}
$$

下证 $P(x)$ 有 $(2 n)$ 个根在单位圆上 (这样 $P(x)$ 的根都在单位圆上). 则只需在单位圆上找出 $(2 n)$ 个不为 1 的满足

$$
(2 n+1)\left(x^{2 n+1}-1\right)(x-1)=\left(x^{n+1}-1\right)^{2}
$$

的满足 $(2 n)$ 个复数.

注意到 $x$ 在单位圆上且 $x \neq 1$ 时: 记 $x=\cos \theta+i \sin \theta$, 则

$$
\begin{gathered}
x-1=2 \sin \frac{\theta}{2}\left(-\sin \frac{\theta}{2}+i \cos \frac{\theta}{2}\right), \\
x^{n+1}-1=2 \sin \frac{(n+1) \theta}{2}\left(-\sin \frac{(n+1) \theta}{2}+i \cos \frac{(n+1) \theta}{2}\right), \\
x^{2 n+1}-1=2 \sin \frac{(2 n+1) \theta}{2}\left(-\sin \frac{(2 n+1) \theta}{2}+i \cos \frac{(2 n+1) \theta}{2}\right) .
\end{gathered}
$$

因此

$$
\begin{aligned}
(x-1)\left(x^{2 n+1}-1\right) & =2 \sin \frac{\theta}{2} \cdot e^{i\left(\frac{\theta}{2}+\frac{\pi}{2}\right)} \cdot 2 \sin \frac{(2 n+i) \theta}{2} e^{i\left(\frac{(2 n+i) \theta}{2}+\frac{\pi}{2}\right)} \\
& =4 \sin \frac{\theta}{2} 2 \sin \frac{(2 n+i) \theta}{2} e^{i((n+1) \theta+\pi)}, \\
\left(x^{n+1}-1\right)^{2} & =\left(2 \sin \frac{(n+1) \theta}{2} e^{i\left(\frac{(n+1) \theta}{2}+\frac{\pi}{2}\right)}\right)^{2} \\
& =4 \sin ^{2} \frac{(n+1) \theta}{2} e^{i((n+1) \theta+\pi)} .
\end{aligned}
$$

故

$$
\begin{aligned}
& (2 n+1)(x-1)\left(x^{2 n+1}-1\right)=\left(x^{n+1}-1\right)^{2} \\
\Leftrightarrow & (2 n+1) \sin \frac{\theta}{2} \sin \frac{(2 n+1) \theta}{2}=\sin ^{2} \frac{(n+1) \theta}{2} \\
\Leftrightarrow & (2 n+1)\left(\frac{1}{2}(\cos (n \theta)-\cos (n+1) \theta)\right)=\frac{1}{2}(1-\cos (n+1) \theta) \\
\Leftrightarrow & 2 n \cos (n+1) \theta+1-(2 n+1) \cos n \theta=0 .
\end{aligned}
$$

记

$$
f(\theta)=2 n \cos (n+1) \theta+1-(2 n+1) \cos n \theta, \theta \in[0,2 \pi]
$$

则只需证明 $f(\theta)=0$ 在 $(0,2 \pi)$ 中有不少于 $(2 n)$ 个根 $\theta$. 注意到 $f(\theta)$ 是 $[0,2 \pi]$ 上的连续函数, 而对奇数 $i(1 \leq i \leq 2 n-1)$, 有

$$
f\left(\frac{i \pi}{n}\right)=2 n \cos \frac{i(n+1) \pi}{n}+1+(2 n+1)>0
$$

对偶数 $i(2 \leq i \leq 2 n-2)$, 有

$$
f\left(\frac{i \pi}{n}\right)=2 n \cos \frac{i(n+1) \pi}{n}+1-(2 n+1)<0 .
$$

(若 $f\left(\frac{i \pi}{n}\right)=0$, 则 $\cos \frac{i(n+1) \pi}{n}=1$. 故 $2 n \mid i(n+1)$. 故 $n \mid i$. 结合 $2 \leq i \leq 2 n-2$ 知 $i=n$. 故 $2 \mid n+1$, 这与 $2 \mid i$ 矛盾!) 且

$$
\cos \frac{\pi}{2(n+1)}=1-(2 n+1) \cos \frac{n \pi}{2(n+1)}=1-(2 n+1) \sin \frac{\pi}{2(n+1)}<0
$$

这是因为记

$$
g(x)=\frac{2}{\pi} x-\sin x,\left(0 \leq x \leq \frac{\pi}{2}\right)
$$

则 $g^{\prime}(x)=\frac{2}{\pi}-\cos x$, 故

$$
g^{\prime}(x)\left\{\begin{array}{l}
>0, \quad \arccos \frac{2}{\pi}<x \leq \frac{\pi}{2} \\
=0, \quad x=\arccos \frac{2}{\pi} \\
<0, \quad 0 \leq x<\arccos \frac{2}{\pi}
\end{array}\right.
$$

结合 $g\left(\frac{2}{\pi}\right)=g(0)=0$ 知

$$
g(x) \leq 0\left(0 \leq x \leq \frac{\pi}{2}\right) .
$$

故由 $g\left(\frac{\pi}{2(n+1)}\right) \leq 0$ 知

$$
\sin \frac{\pi}{2(n+1)} \geq \frac{1}{n+1}>\frac{1}{2 n+1}
$$

故

$$
1-(2 n+1) \sin \frac{\pi}{2 n+1}<0
$$

及

$$
f\left(\frac{(4 n+1) \pi}{2(n+1)}\right)=f\left(\frac{\pi}{2(n+1)}\right)<0
$$

结合

$$
\frac{\pi}{2 n+1}<\frac{\pi}{n}<\frac{2 \pi}{n}<\cdots<\frac{(2 n-1) \pi}{n}<\frac{(4 n+1) \pi}{2(n+1)}
$$

和连续函数的介值原理知 $f(\theta)=0$ 在 $\left(\frac{\pi}{2 n+1}, \frac{\pi}{n}\right),\left(\frac{\pi}{n}, \frac{2 \pi}{n}\right), \cdots,\left(\frac{(2 n-1) \pi}{n}, \frac{(4 n+1) \pi}{2(n+1)}\right)$中的每个区间中都有根.

因此 $f(\theta)=0$ 有不少于 $(2 n)$ 个在 $(0,2 \pi)$ 上的根 $\theta$.

故原题证毕!

评析 在对 $P$ 进行代数变形后不容易直接证出原题结论, 此时需要有灵活的思维 (即“脑洞大开”), 想到直接找出 $P$ 的 $(2 n)$ 个根, 这是利用单位圆的几何性质将问题转化为找出一个 $\mathbb{R} \rightarrow \mathbb{R}$ 的函数

$$
f(\theta)=2 n \cos (n+1) \theta+1-(2 n+1) \cos n \theta
$$

的一些零点, 考虑图像知此时使用介值原理会更为方便. 官方答案是先证明

$$
Q(x)=\frac{P(x)}{x^{n}}=\frac{2 n}{x^{n}} \cdot \frac{x^{2 n+1}-1}{x-1}-\frac{x}{x^{n}}\left(\frac{x^{n}-1}{x-1}\right)^{2}
$$

在单位圆上值为实数, 再证明 $Q(x)$ 在 $(2 n)$ 个 $(2 n)$ 次单位根上取值正负交替, 巧妙地避开了对 $f(\theta)$ 在 $\theta=0$ 附近取值的讨论, 并叙述得更简洁.

## V、附加赛

题 11. 鲍勃将 $\{(x, y) \mid 1 \leq x, y \leq 5\}$ 中的五个点染成蓝色. 求可能染色方式的数目, 使得任两个蓝色点间的距离不是整数.

解 注意到这样的染色法中任两个不同蓝点不能再同一行或着同一列中. 因此下面考虑所有使每行每列各有一个蓝点的染色方法. 记所有这样的染色方法构成的集合为 $A$. 则 $|A|=120$. 记 $T=\{(1,1),(1,5),(5,1),(5,5)\}$. 对 $t \in T$, 恰有两个其它 $\{(x, y) \mid 1 \leq x, y \leq 5\}$ 中的格点到它的距离为 5 , 记为 $t_{1}, t_{2}$.

对 $t \in T, i \in\{1,2\}$, 记 $A_{t, i}=\left\{a \mid a \in A\right.$, 在 $a$ 中 $t$ 和 $t_{i}$ 都是蓝色的 $\}$. 容易证明全体符合原题条件的染法构成的集合为

$$
B:=A \backslash\left(\bigcup_{t \in T, i \in\{1,2\}} A_{t, i}\right), i \in\{1,2\} \text {. }
$$

且对 $t \in T$, 有 $\left|A_{t, i}\right|=3 !=6,\left|A_{t, 1} \cap A_{t, 2}\right|=2 !=2$.

对 $t_{1}, t_{2} \in T, i_{1}, i_{2} \in\{1,2\}$. 若 $t_{1} \neq t_{2}$, 则 $A_{t_{1}, i_{1}} \cap A_{t_{2}, i_{2}}=\emptyset$.

故由容斥原理, 记 $S=\left\{A_{t, i} \mid t \in T, i \in 1,2\right\}$, 则

$$
\begin{aligned}
|B| & =|A|+\sum_{c \subseteq S, C \neq \emptyset}(-1)^{|C|}\left|\cap_{A^{\prime} \in c} A^{\prime}\right| \\
& =|A|+(-1) \cdot \sum_{t \in T, i \in\{1,2\}}\left|A_{t, i}\right|+1 \cdot \sum_{t \in T}\left|A_{t, 1} \cap A_{t, 2}\right| \\
& =120-8 \cdot 6+4 \cdot 2=80 .
\end{aligned}
$$

故所求答案为 80 .

评析 本题需要注意的主要有: 讨论时不要漏情况和计算时不要算错.

题 12 . 求最小的正整数 $n$, 使得

$$
\underbrace{2^{2^{.{ }^{2}}}}_{n \text { 个 } 2}>\underbrace{((\cdots((100 !) !) ! \cdots) !) !}_{100 \text { 个阶乘 }} .
$$

解 所求最小的正整数 $n$ 为 104 .
对 $n \in \mathbb{N}$, 记 $a_{n}=\underbrace{2^{2 \cdot}{ }^{\cdot 2}}_{n \text { 个 } 2}, b_{n}=\underbrace{((\cdots((100 !) !) ! \cdots) !) !}_{n \text { 个阶乘 }}$, 则 $a_{0}=1, b_{0}=100$, 且对 $n \in \mathbb{N}$, 有

$$
a_{n+1}=2^{a_{n}}, b_{n+1}=b_{n} !
$$

则易证 $n \geq 2$ 时,

$$
a_{n} \geq 4, a_{n}=2^{a_{n-1}} \geq a_{n-1}^{2}, b_{n} \geq 100
$$

下面对 $n$ 归纳证明

$$
a_{n+3}<b_{n}<\frac{a_{n+4}}{a_{n+3}} .
$$

$n=0$ 时成立.

若 $n \leq n^{\prime}$ 成立 $\left(n^{\prime} \in \mathbb{N}\right)$, 则 $n=n^{\prime}+1$ 时, 由归纳假设,

$$
\begin{gathered}
a_{n+3}=2^{a_{n+2}}=\prod_{i=1}^{a_{n+2}} 2 \leq \prod_{i=1}^{a_{n+2}} i<\prod_{i=1}^{b_{n-1}} i=b_{n-1} !=b_{n} . \\
b_{n}=b_{n-1} !<\left(\frac{a_{n+3}}{a_{n+2}}\right) !<\left(\frac{a_{n+3}}{a_{n+2}}\right)^{\frac{a_{n+3}}{a_{n+2}}} \\
=\left(2^{a_{n+2}-a_{n+1}}\right)^{\frac{a_{n+3}}{a_{n+2}}}=2^{a_{n+3}-\frac{a_{n+1} a_{n+3}}{a_{n+2}}} \\
<2^{a_{n+3}-\frac{a_{n+2}^{2}}{a_{n+2}}}=\frac{a_{n+4}}{a_{n+3}} .
\end{gathered}
$$

故 $n=n^{\prime}+1$ 时也成立. 因此由数学归纳法知对 $n \in \mathbb{N}$ 均有

$$
a_{n+3}<b_{n}<\frac{a_{n+4}}{a_{n+3}}<a_{n+4} .
$$

因此所求最小的正整数 $n$ 为 104 . 因为

$$
a_{103}=\underbrace{2^{2 \cdot{ }^{2}}}_{103 \text { 个 } 2}<\underbrace{((\cdots((100 !) !) ! \cdots) !) !}_{100 \text { 个阶乘 }}=b_{100}<\underbrace{2^{2 \cdot{ }^{.2}}}_{104 \text { 个 } 2} .
$$

评析 可以猜测 $a_{n+3}<b_{n}<a_{n+4}(n \in \mathbb{N})$, 且也可以感觉出用归纳法从 $n$ 证到 $n+1$ 时, 将 $b_{n+1}$ 的下界放成 $2^{b_{n}}$, 上界放成 $b_{n}^{b_{n}}$. 这时就可以考虑加强 $b_{n}$ 的上界, 因此只要通过稍微加强就能通过用 $b_{n}^{b_{n}}$ 这一归纳步骤将对 $b_{n+1}$ 的上界加强很多, 就能顺利的完成归纳的步骤. 官方的步骤是直接归纳证明 $a_{n+3}<b_{n}<\sqrt{a_{n+4}}$.

题 13. 复数 $a, b, c$ 构成复平面上一个边长为 18 的等边三角形, 若 $|a+b+c|=$ 36. 求 $|b c+c a+a b|$.

解 记

$$
\frac{a+b+c}{3}=\alpha, \omega=-\frac{1}{2}+\frac{\sqrt{3}}{2}
$$

为三次单位根, 则由题

$$
|\alpha|=\frac{1}{3}|a+b+c|=12
$$

且可不妨设存在模长为 $6 \sqrt{3}$ 的复数 $\beta$ 使得

$$
a=\alpha+\beta \omega, b=\alpha+\beta \omega^{2}, c=\alpha+\beta .
$$

因此

$$
\begin{aligned}
& |b c+c a+a b|=\left|\left(\alpha+\beta \omega^{2}\right)(\alpha+\beta)+(\alpha+\beta)(\alpha+\beta \omega)+(\alpha+\beta \omega)\left(\alpha+\beta \omega^{2}\right)\right| \\
= & \left|\left(\alpha^{2}+\alpha \beta\left(1+\omega^{2}\right)+\beta^{2} \omega^{2}\right)+\left(\alpha^{2}+\alpha \beta(\omega+1)+\beta^{2} \omega\right)+\alpha^{2}+\alpha \beta\left(\omega^{2}+\omega\right)+\beta^{2}\right| \\
= & \left|3 \alpha^{2}\right|=3|\alpha|^{2}=3 \cdot 12^{2}=432 .
\end{aligned}
$$

评析 $|b c+c a+a b|$ 其实和等边三角形的边长没有关系. 本题的关键在于不要算错.

题 14. 对两个互素的正整数 $a, b$, 令 $\operatorname{ord}_{b}(a)$ 表示最小的正整数 $k$, 使得 $b \mid a^{k}-1$. 令 $\varphi(a)$ 表示小于或等于 $a$ 的正整数中与 $a$ 互素的个数. 求最小的正整数 $n$, 使得 $\operatorname{ord}_{n}(m)<\frac{\varphi(m)}{10}$ 对所有与 $n$ 互素的正整数 $m$ 成立.

解 对素数 $p$ 和正整数 $\alpha$, 定义

$$
\lambda\left(p^{\alpha}\right)= \begin{cases}p^{\alpha-1}(p-1)=\varphi\left(p^{\alpha}\right), & p \neq 2, \\ 2^{\alpha-1}=\varphi\left(2^{\alpha}\right), & p=2 \text { 且 } \alpha \leq 2, \\ 2^{\alpha-2}=\frac{1}{2} \varphi\left(2^{\alpha}\right), & p=2 \text { 且 } \alpha \geq 3 .\end{cases}
$$

则由欧拉定理及原根的性质可知

(1) 对 $m \in \mathbb{Z}(p \nmid m)$, 有 $m^{\lambda\left(p^{\alpha}\right)} \equiv 1\left(\bmod p^{\alpha}\right)$;

(2) 存在 $g_{p} \in \mathbb{N}^{*}$, 使得 $\operatorname{ord}_{p^{\alpha}}\left(g_{p}\right)=\lambda\left(p^{\alpha}\right)$.

再定义

$$
\lambda(n)=\operatorname{lcm}\left(\lambda\left(p_{1}^{\alpha_{1}}\right), \lambda\left(p_{2}^{\alpha_{2}}\right), \cdots, \lambda\left(p_{t}^{\alpha_{t}}\right)\right),
$$

其中 $n=\prod_{i=1}^{t} \lambda\left(p_{i}^{\alpha_{i}}\right)$ 是 $n$ 的标准分解, 则考虑数 $g_{n} \in \mathbb{N}^{*}$ (对 $1 \leq i \leq t$ 有 $\left.g_{n} \equiv g_{p_{i}^{\alpha_{i}}}\left(\bmod p_{i}^{\alpha_{i}}\right)\right)$, 可知 $\operatorname{ord}_{n}\left(g_{n}\right)=\lambda(n)$. 因此易证

$$
\max _{\substack{m \in \mathbb{N}^{*} \\ \operatorname{gcd}(m, n)=1}}\left\{\operatorname{ord}_{n}(m)\right\}=\lambda(n)
$$

故即求最小的正整数 $n$, 使 $\lambda(n)<\frac{\varphi(n)}{10}$. 易证 $\lambda(n) \mid \varphi(n)$, 且

$$
\lambda(240)=4<\frac{64}{10}=\frac{\varphi(240)}{10} .
$$

下证若 $\lambda(n)<\frac{\varphi(n)}{10}$, 则 $n \geq 240$.

(i) 存在素数 $p \neq 2$, 使 $p \left\lvert\, \frac{\varphi(n)}{\lambda(n)}\right.$, 则必存在 $p_{1}^{\alpha_{1}}, \cdots, p_{t}^{\alpha_{t}}$ 中的两个 (记为 $n_{1}, n_{2}$ ),使得 $\varphi\left(n_{1}\right), \varphi\left(n_{2}\right)$ 必被 $p$ 整除 (此处 $n=\prod_{i=1}^{t} \lambda\left(p_{i}^{\alpha_{i}}\right)$ 是 $n$ 的标准分解). 此时 $n_{1}, n_{2}$要么被 $p^{2}$ 整除, 要么被模 $p$ 与 1 同余的素数整除, 且 $\operatorname{gcd}\left(n_{1}, n_{2}\right)=1, n_{1} n_{2} \mid n$. 因此

$$
n \geq \min \left(p^{2}(2 p+1),(2 p+1)(4 p+1)\right)
$$

因为模 $p$ 与 1 同余的最小的两个素数至少为 $(2 p+1)$ 和 $(4 p+1)$.

若 $p \geq 5$, 则易证 $n$ 必须大于 240 , 故 $p=3$. 这意味着 $7,9,13,19,31,37$ 中的两个数被 $n$ 整除. 由 $7 \times 37>240$ 知我们可以前述序列中去掉大于 31 的素数.在剩下的可能性中, 由 $\lambda(9)=\lambda(7)=6, \lambda(19)=18, \lambda(31)=30$ 易证, 若 $n$ 为 $9,7,13,19,31$ 中两个数的乘积, 则

$$
\frac{\varphi(n)}{\lambda(n)} \leq 6 \text {. }
$$

又因为 $2 \nmid n$ 时,

$$
\varphi(2 n)=\varphi(n), \lambda(2 n)=\lambda(n)
$$

所以由 $\frac{\varphi(n)}{\lambda(n)}>10$ 知 $n$ 为一个不小于 3 的数乘以 $9,7,13,19,31$ 中其中两个数.

当 $n<240$ 时, $n$ 只能为 $3 \times 9 \times 7=189$, 但容易验证 $\frac{\varphi(189)}{\lambda(189)}=4<10$. 矛盾!

(ii) $\frac{\varphi(n)}{\lambda(n)}$ 为 2 的幂.

易证 $n \nmid 24$ 时, $\lambda(n) \geq 4$, 而 $n \mid 24$ 时, $\varphi(n) \leq 8$. 因此当 $n \mid 24$ 时,

$$
\frac{\varphi(n)}{\lambda(n)}<10
$$

故 $n \nmid 24$, 此时 $\lambda(n) \geq 4$, 当 $\lambda(n)=4$ 时 $\varphi(n) \geq 4 \cdot 2^{4}=64$ 且 $32 \nmid n$ (否则 $\lambda(n) \geq \lambda(32)=8)$. 这样的唯一正整数 $n$ 为 $2^{4} \cdot 3 \cdot 5=240$.

不难证明 $\lambda(n) \geq 5$ 时为使

$$
\frac{\varphi(n)}{\lambda(n)} \geq 2^{4}
$$

$n$ 不可能不大于 240 (否则 $\lambda(n) \leq 15$, 由此 $n$ 不被任何不小于 17 且不为 32 的素数或素数幂整除, 故 $n$ 是 $2,4,8,16,32,3,9,5,7,11,13$ 中一些数的乘积, 此时容易验证 $n \geq 240$ ).

综上所求的最小正整数 $n$ 为 240 .

评析 上述解答选自官方解答, 对 $\frac{\varphi(n)}{\lambda(n)}$ 的值的讨论在该解答中较为简洁和巧妙. 若 10 改为更大的数, 恐怕就没有那么简洁的做法了.

