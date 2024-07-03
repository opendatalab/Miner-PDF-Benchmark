# 第四十五期问题征解解答与点评 

张端阳

第一题 给定某个三角形的内切圆 $\odot I$ 与外接圆 $\odot O$. 在 $\odot O$ 上任取一条与 $\odot I$相切的弦 $A B$, 过 $A, B$ 作 $\odot P$ 与 $\odot I$ 相切. 求点 $P$ 的轨迹.

(长沙一中学生 尤溱 供题)

解 (根据供题者的解答整理):



设 $R, r$ 分别为 $\odot O, \odot I$ 的半径.

由彭赛列闭合定理, 在 $\odot O$ 上存在点 $C$, 使得 $\odot I$ 是 $\triangle A B C$ 的内切圆, 设 $\triangle A B C$ 角 $C$ 内的旁心为 $J$.

设 $\odot P$ 与 $\odot I$ 切于点 $T, \odot I$ 与 $A B$ 切于点 $D$. 设 $N$ 是 $\odot P$ 中弧 $A B$ 的中点, 由伪外接圆的性质 ${ }^{1}, T, D, N, J$ 共线, 且 $N$ 是 $D J$ 的中点.

设 $M$ 是 $\odot O$ 中弧 $A B$ 的中点, 则 $O, P, M, N$ 共线且 $M$ 是 $I J$ 的中点. 这样,

$$
O N=O M+M N=O M+\frac{1}{2} I D=R+\frac{1}{2} r
$$[^0]另一方面，

$$
O N=P O+P N=P O+P T=P O+P I+r
$$

所以

$$
P O+P I=R+\frac{1}{2} r-r=R-\frac{1}{2} r
$$

是定值.

故 $P$ 在以 $O, I$ 为焦点、长轴长为 $R-\frac{1}{2} r$ 的椭圆上运动.

因为切点 $D$ 可唯一确定弦 $A B$, 于是可以用 $D$ 在 $\odot I$ 上的运动代替 $A B$ 的运动. 当 $D$ 沿 $\odot I$ 运动一周时, $P$ 遍历粗圆上的所有点.

评注 马鞍山第二中学孙浩翔, 成都石室中学杨安洲, 大连市第二十四中学于丰硕、王浦丞, 华南师大附中戴子一, 北京师范大学海口附属学校列亭枫, 深圳中学邓博文, 东北师大附中鲁力源、吴竞航, 石坝镇八一中学伊峇戈, 南昌市第二中学于沣林, 西安市铁一中学张恩诰, 广西师范大学附属外国语学校铁山校区叶骐铭, 清华大学严君啸, 长郡中学姜梓涵等同学也给出了本题的正确解答.

第二题 设 $n$ 是正整数. 将一个 $2 n \times 2 n$ 方格表的格相间地染为黑白两色之一.从中任选 $n^{2}$ 个黑格, 证明: 恰含一个选出黑格的 $2 \times 2$ 正方形的个数不少于 $2 n-1$.

(人大附中学生 马天佑 供题)

## 证明 (根据供题者的解答整理):

当 $n=1$ 时显然成立, 下设 $n \geq 2$.

作出每个黑格的中心点, 在每个 $2 \times 2$ 正方形中两个黑格的中心点之间连一条线段. 下面将黑格等同于其中心点, $2 \times 2$ 正方形等同于其内的线段. 则只需证明任选 $n^{2}$ 个点时, 恰有一个端点被选出的线段的条数不少于 $2 n-1$.

可以将所有线段分成 $n$ 组, 第一组在一条直线上 (含 $2 n-1$ 条线段和 $2 n$ 个点), 其余 $n-1$ 组构成一个矩形 (含 $4 n-2$ 条线段和 $4 n-2$ 个点). 下页中的图是 $n=6$ 时的例子.

对于第一组, 如果其 $2 n$ 个点中有被选出的, 但没有全被选出, 则至少含一条满足要求的线段. 对于其余 $n-1$ 组, 如果其 $4 n-2$ 个点中有被选出的, 但没有全被选出, 则至少含两条满足要求的线段. 因此若每组中都有点被选出, 且没有全被选出, 则至少有 $1+2(n-1)=2 n-1$ 条满足要求的线段, 结论成立.

下设存在一组或者没有点被选出, 或者所有点全被选出. 因为恰选出所有 $2 n^{2}$
个点的一半, 所以由对称性 (取补集不影响恰有一个端点被选出的线段的条数),可不妨设存在一组所有点全被选出.


情形 1 : 第一组中的所有点全被选出.

第一组中的线段将其余 $n-1$ 组各分成两部分, 每部分含 $2 n-1$ 条线段和 $2 n$个点. 下图是第二组的例子:

如果一部分中的点没有全被选出, 则至少含两条满足要求的线段 (因为该部分两端的点都被选出). 设 $2 n-2$ 个部分中有 $x$ 个所有点全被选出, 则至少有 $2(2 n-2-x)$ 条满足要求的线段, 因此当 $x \leq n-2$ 时结论成立.

注意到每部分中位于 $2 n \times 2 n$ 方格表边界的两个点不出现在其他部分中, 有两个点出现在第一组中, 其余 $2 n-4$ 个点恰出现在另一个部分中. 因此共选出至少

$$
2 x+2 n+\frac{(2 n-4) \cdot x}{2}=2 n+n x
$$

个点. 由 $2 n+n x \leq n^{2}$ 知 $x \leq n-2$.

情形 2: 第二组中的所有点全被选出 (其余 $n-3$ 组同理).

可设第一组中的点没有全被选出 (否则归为情形 1 ), 则第一组中至少含一条满足要求的线段.

第二组中的线段将第 $3 \sim n$ 组各分成两部分, 每部分含 $2 n-1$ 条线段和 $2 n$ 个点. 下图是第三组的例子:


类似情形 1 中的讨论, 如果一部分中的点没有全被选出, 则至少含两条满足要求的线段. 设 $2 n-4$ 个部分中有 $x$ 个所有点全被选出, 则至少有 $1+2(2 n-4-x)$条满足要求的线段, 因此当 $x \leq n-3$ 时结论成立.

注意到每部分中有三个点不出现在其他部分中 (图中的红点), 有三个点出现在第二组中, 其余 $2 n-6$ 个点恰出现在另一个部分中. 因此共选出至少

$$
3 x+(4 n-2)+\frac{(2 n-6) \cdot x}{2}=4 n-2+n x
$$

个点. 由 $4 n-2+n x \leq n^{2}$ 知 $x \leq n-3$.

综上, 命题得证.

评注 (1). 广西师范大学附属外国语学校铁山校区叶骐铭同学给出了如下思路.

记 $f(i, i+1)$ 是位于第 $i, i+1$ 行中满足要求的 $2 \times 2$ 正方形的个数.
设第 $i$ 行有 $a_{i}$ 个黑格被选出, 且有 $b_{i}$ 个在第 1 或第 $2 n$ 列中. 则当 $a_{i} \neq a_{i+1}$ 时,

$$
f(i, i+1) \geq\left|\left(2 a_{i}-b_{i}\right)-\left(2 a_{i+1}-b_{i+1}\right)\right| ;
$$

当 $a_{i}=a_{i+1}$ 且不为 0 和 $n$ 时, $f(i, i+1) \geq 1$.

下面转化为代数问题, 即在 $\sum_{i=1}^{2 n} a_{i}=n^{2}$ 的前提下, 证明

$$
\sum_{i=1}^{2 n-1} f(i, i+1) \geq 2 n-1
$$

(2). 本题与 2021 年日本数学奥林匹克决赛第五题的叙述类似:

设 $n$ 是正整数. 求 $1,2, \cdots, 2 n^{2}$ 中所有满足如下条件的正整数 $k$ : 当将一个 $2 n \times 2 n$ 方格表的某 $k$ 个格染黑、其余格染白时，既有黑格也有白格的 $2 \times 2$ 正方形的个数的最小可能值为 $2 n-1$.

第三题 是否存在正实数 $C$, 使得对任意正整数 $n$ 和任意非负实数 $a_{1}, a_{2}, \cdots, a_{n}$, 都有

$$
\left(\sum_{k=1}^{n} 2^{-k} a_{k}^{2}\right)\left(\sum_{k=1}^{n} 2^{k} a_{k}^{2}\right) \geq C\left(\sum_{k=1}^{n} a_{k}\right)^{4} ?
$$

(湖南师范大学 羊明亮 供题)

## 解 (根据海亮外国语学校赵斌老师的解答整理):

存在, 取 $C=\frac{1}{81}$ 即可.

当 $\sum_{k=1}^{n} a_{k}=0$ 时显然成立.

当 $\sum_{k=1}^{n} a_{k}>0$ 时, 由齐次性, 可不妨设 $\sum_{k=1}^{n} a_{k}=1$, 此时只需证明

$$
\left(\sum_{k=1}^{n} 2^{-k} a_{k}^{2}\right)\left(\sum_{k=1}^{n} 2^{k} a_{k}^{2}\right) \geq \frac{1}{81}
$$

当存在 $1 \leq k \leq n$ 使得 $a_{k} \geq \frac{1}{3}$ 时,

$$
\text { LHS } \geq 2^{-k} a_{k}^{2} \cdot 2^{k} a_{k}^{2}=a_{k}^{4} \geq \frac{1}{81} \text {. }
$$

当对任意 $1 \leq k \leq n$ 均有 $a_{k} \leq \frac{1}{3}$ 时, 存在 $1 \leq m \leq n$ 使得

$$
S:=a_{1}+a_{2}+\cdots+a_{m} \in\left[\frac{1}{3}, \frac{2}{3}\right] \text {. }
$$

这样, 由柯西不等式,

$$
\mathrm{LHS} \geq\left(\sum_{k=1}^{m} 2^{-k} a_{k}^{2}\right)\left(\sum_{k=m+1}^{n} 2^{k} a_{k}^{2}\right)
$$

$$
\begin{aligned}
& \geq \frac{S^{2}}{\sum_{k=1}^{m} 2^{k}} \cdot \frac{(1-S)^{2}}{\sum_{k=m+1}^{n} 2^{-k}} \\
& \geq \frac{S^{2}}{2^{m+1}} \cdot \frac{(1-S)^{2}}{2^{-m}} \\
& =\frac{1}{2}(S(1-S))^{2} \geq \frac{1}{2}\left(\frac{1}{3} \cdot \frac{2}{3}\right)^{2}>\frac{1}{81} .
\end{aligned}
$$

综上, 命题得证.

评注 华南师大附中戴子一和长郡中学姜梓涵同学采用了证明 Carlson 不等式 ${ }^{2}$ 的方法.

记 $A=\sum_{k=1}^{n} 2^{k} a_{k}^{2}, B=\sum_{k=1}^{n} 2^{-k} a_{k}^{2}$. 对正实数 $x, y$, 由柯西不等式,

$$
x A+y B=\sum_{k=1}^{n}\left(2^{k} x+2^{-k} y\right) a_{k}^{2} \geq\left(\sum_{k=1}^{n} a_{k}\right)^{2}\left(\sum_{k=1}^{n} \frac{1}{2^{k} x+2^{-k} y}\right)^{-1} .
$$

如果可以证明 3

$$
\sum_{k=1}^{n} \frac{1}{2^{k} x+2^{-k} y} \leq \int_{-\infty}^{\infty} \frac{1}{2^{t} x+2^{-t} y} \mathrm{~d} t
$$

则由

$$
\int \frac{1}{2^{t} x+2^{-t} y} \mathrm{~d} t=\frac{1}{\ln 2} \cdot \frac{1}{\sqrt{x y}} \arctan \left(2^{t} \sqrt{\frac{x}{y}}\right)+C^{\prime},
$$

知

$$
\sum_{k=1}^{n} \frac{1}{2^{k} x+2^{-k} y} \leq \frac{1}{\ln 2} \cdot \frac{1}{\sqrt{x y}} \cdot \frac{\pi}{2}
$$

于是

$$
\sqrt{\frac{x}{y}} A+\sqrt{\frac{y}{x}} B \geq \frac{2 \ln 2}{\pi}\left(\sum_{k=1}^{n} a_{k}\right)^{2}
$$

从而取 $x=B, y=A$, 便有

$$
A B \geq\left(\frac{\ln 2}{\pi}\right)^{2}\left(\sum_{k=1}^{n} a_{k}\right)^{2}
$$

故取 $C=\left(\frac{\ln 2}{\pi}\right)^{2}$ 即可, 这比 $\frac{1}{81}$ 大.

${ }^{2}$ 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是实数, 则

$$
\left(\sum_{i=1}^{n} a_{i}\right)^{4} \leq \pi^{2}\left(\sum_{i=1}^{n} a_{i}^{2}\right)\left(\sum_{i=1}^{n} i^{2} a_{i}^{2}\right)
$$

3 戴子一同学给出一个证明, 但较复杂
第四题 设函数 $f: \mathbb{N} \rightarrow \mathbb{N}$, 满足:

(1) $f(0)=f(1)=0$ ，且对任意素数 $p, f(p)=1$ ；

(2) 对任意 $m, n \in \mathbb{N}, f(m n)=f(m) n+m f(n)$.

求所有的奇自然数 $n$, 使得 $n f(f(f(n)))=f(n) f(f(n))$.

(清华大学学生 尹龙晖 供题)

## 解 (根据供题者的解答整理):

由归纳法容易证明, 对素数 $p$ 和非负整数 $\alpha$, 有

$$
f\left(p^{\alpha}\right)=\alpha p^{\alpha-1} ;
$$

且对任意 $k$ 个非负整数 $n_{1}, n_{2}, \cdots, n_{k}$, 有

$$
f\left(\prod_{i=1}^{k} n_{i}\right)=\sum_{i=1}^{k} f\left(n_{i}\right) \prod_{j \neq i} n_{j}
$$

先证明一个引理.

引理 设 $n=\prod_{i=1}^{k} p_{i}^{\alpha_{i}}, m=\prod_{i=1}^{k} p_{i}^{\beta_{i}}$, 其中 $\alpha_{i}, \beta_{i}$ 为非负整数, $p_{i}$ 为素数, 则

$$
\frac{f(n)}{n}=\frac{f(m)}{m}
$$

当且仅当 $\alpha_{i} \equiv \beta_{i}\left(\bmod p_{i}\right)(1 \leq i \leq k)$ 且

$$
\sum_{i=1}^{k}\left[\frac{\alpha_{i}}{p_{i}}\right]=\sum_{i=1}^{k}\left[\frac{\beta_{i}}{p_{i}}\right]
$$

证明 注意到

$$
f(n)=\sum_{i=1}^{k} f\left(p_{i}^{\alpha_{i}}\right) \prod_{j \neq i} p_{j}^{\alpha_{j}}=\prod_{i=1}^{k} p_{i}^{\alpha_{i}-1} \cdot \sum_{i=1}^{k} \alpha_{i} \prod_{j \neq i} p_{j}
$$

故 $\frac{f(n)}{n}=\sum_{i=1}^{k} \frac{\alpha_{i}}{p_{i}}$.

同理, $\frac{f(m)}{m}=\sum_{i=1}^{k} \frac{\beta_{i}}{p_{i}}$.

令 $\alpha_{i}=a_{i} p_{i}+c_{i}, a_{i} \in \mathbb{N}, 0 \leq c_{i}<p_{i}, \beta_{i}=b_{i} p_{i}+d_{i}, b_{i} \in \mathbb{N}, 0 \leq d_{i}<p_{i}$. 因此 $\frac{f(n)}{n}=\frac{f(m)}{m}$ 等价于

$$
\sum_{i=1}^{k} \frac{\alpha_{i}}{p_{i}}=\sum_{i=1}^{k} \frac{\beta_{i}}{p_{i}}
$$

即

$$
\left(\sum_{i=1}^{k} a_{i}-\sum_{i=1}^{k} b_{i}\right)+\sum_{i=1}^{k} \frac{c_{i}-d_{i}}{p_{i}}=0
$$

对每个 $i$, 将上式两边乘以 $\prod_{j \neq i} p_{j}$, 则除了 $\frac{c_{i}-d_{i}}{p_{i}}$ 一项以外, 剩下的项均为整数,
因此 $p_{i} \mid c_{i}-d_{i}$. 又因为 $\left|c_{i}-d_{i}\right|<p_{i}$, 所以 $c_{i}=d_{i}$. 于是 $\alpha_{i} \equiv \beta_{i}\left(\bmod p_{i}\right)$, 且 $\sum_{i=1}^{k} a_{i}=\sum_{i=1}^{k} b_{i}$, 即 $\sum_{i=1}^{k}\left[\frac{\alpha_{i}}{p_{i}}\right]=\sum_{i=1}^{k}\left[\frac{\beta_{i}}{p_{i}}\right]$.

以

反之, 当 $\alpha_{i} \equiv \beta_{i}\left(\bmod p_{i}\right)$ 且 $\sum_{i=1}^{k}\left[\frac{\alpha_{i}}{p_{i}}\right]=\sum_{i=1}^{k}\left[\frac{\beta_{i}}{p_{i}}\right]$ 时, $c_{i}=d_{i}$ 且 $\sum_{i=1}^{k} a_{i}=\sum_{i=1}^{k} b_{i}$, 所

$$
\left(\sum_{i=1}^{k} a_{i}-\sum_{i=1}^{k} b_{i}\right)+\sum_{i=1}^{k} \frac{c_{i}-d_{i}}{p_{i}}=0
$$

成立.

引理证毕.

回到原题. $n=1$ 显然是方程的解. 当 $n$ 是奇素数时, $f(f(n))=0$, 方程也成立.

下设 $n$ 是奇合数, 记 $n=\prod_{i=1}^{k} p_{i}^{\alpha_{i}}$, 其中 $\alpha_{i}$ 为正整数, $p_{i}$ 为素数.

记 $P=\prod_{i=1}^{k} p_{i}, P_{i}=\frac{P}{p_{i}}, B=\sum_{i=1}^{k} \alpha_{i} P_{i}, C=\sum_{i=1}^{k}\left(\alpha_{i}-1\right) P_{i}$. 由引理中的计算方法可得, $f(n)=B \prod_{i=1}^{k} p_{i}^{\alpha_{i}-1}$. 因此

$$
\begin{aligned}
f(f(n)) & =f(B) \prod_{i=1}^{k} p_{i}^{\alpha_{i}-1}+B f\left(\prod_{i=1}^{k} p_{i}^{\alpha_{i}-1}\right) \\
& =f(B) \prod_{i=1}^{k} p_{i}^{\alpha_{i}-1}+B \prod_{i=1}^{k} p_{i}^{\alpha_{i}-2} \cdot \sum_{i=1}^{k}\left(\alpha_{i}-1\right) P_{i} \\
& =\prod_{i=1}^{k} p_{i}^{\alpha_{i}-2}(f(B) P+B C) .
\end{aligned}
$$

由 $n$ 是奇合数, 知 $f(n)>1$, 所以 $f(f(n)) \neq 0$. 因此方程等价于

$$
\frac{f(n)}{n}=\frac{f(f(f(n)))}{f(f(n))}
$$

设

$$
f(B) P+B C=\prod_{i=1}^{k} p_{i}^{\beta_{i}} \cdot \prod_{j=1}^{l} q_{j}^{\gamma_{j}}
$$

其中 $l$ 为非负整数, $q_{j}$ 为素数, $\beta_{i}$ 为非负整数, $\gamma_{j}$ 为正整数. 则

$$
f(f(n))=\prod_{i=1}^{k} p_{i}^{\alpha_{i}+\beta_{i}-2} \prod_{j=1}^{l} q_{j}^{\gamma_{j}}
$$

注意到方程等价于

$$
\frac{f(n)}{n}=\frac{f(f(f(n)))}{f(f(n))}
$$

于是由引理得, $\alpha_{i}+\beta_{i}-2 \equiv \alpha_{i}\left(\bmod p_{i}\right)$ 即 $\beta_{i} \equiv 2\left(\bmod p_{i}\right), \gamma_{j} \equiv 0\left(\bmod q_{j}\right)$, 且

$$
\sum_{i=1}^{k}\left[\frac{\alpha_{i}}{p_{i}}\right]=\sum_{i=1}^{k}\left[\frac{\alpha_{i}+\beta_{i}-2}{p_{i}}\right]+\sum_{j=1}^{l}\left[\frac{\gamma_{j}}{q_{j}}\right]
$$

由 $n$ 为奇数知 $p_{i}>2$, 进而 $\beta_{i} \geq 2$. 又 $\gamma_{j} \geq q_{j}$, 所以

$$
\sum_{i=1}^{k}\left[\frac{\alpha_{i}+\beta_{i}-2}{p_{i}}\right]+\sum_{j=1}^{l}\left[\frac{\gamma_{j}}{q_{j}}\right] \geq \sum_{i=1}^{k}\left[\frac{\alpha_{i}}{p_{i}}\right]+\sum_{j=1}^{l} 1 \geq \sum_{i=1}^{k}\left[\frac{\alpha_{i}}{p_{i}}\right]
$$

于是所有的不等式都取等, 即 $\beta_{i}=2, l=0$, 故

$$
f(f(n))=\prod_{i=1}^{k} p_{i}^{\alpha_{i}}=n
$$

且

$$
f(B) P+B C=\prod_{i=1}^{k} p_{i}^{2}=P^{2}
$$

(*) 中 $f(B) P$ 与 $P^{2}$ 均为 $p_{i}$ 的倍数, 故 $p_{i} \mid B C$. 因为

$$
\begin{gathered}
B=\alpha_{i} P_{i}+\sum_{j \neq i} \alpha_{j} P_{j}, \\
C=\left(\alpha_{i}-1\right) P_{i}+\sum_{j \neq i}\left(\alpha_{j}-1\right) P_{j}
\end{gathered}
$$

且 $\left(p_{i}, P_{i}\right)=1$ 而对任意 $j \neq i$ 有 $p_{i} \mid P_{j}$, 所以 $p_{i} \mid \alpha_{i}\left(\alpha_{i}-1\right)$. 于是要么 $p_{i} \mid \alpha_{i}$, 要么 $p_{i} \mid \alpha_{i}-1$.

若 $p_{i} \mid \alpha_{i}-1$, 则要么 $\alpha_{i}=1$ 、要么 $\alpha_{i} \geq p_{i}+1$. 如果为后者, 那么

$$
B C \geq \alpha_{i}\left(\alpha_{i}-1\right) P_{i}^{2}>p_{i}^{2} P_{i}^{2}=P^{2}
$$

与 $(*)$ 矛盾! 从而必有 $\alpha_{i}=1$.

因此对每个 $i$, 要么 $p_{i} \mid \alpha_{i}$, 要么 $\alpha_{i}=1$. 设满足前者的素数为 $x_{1}, x_{2}, \cdots, x_{t}$,满足后者的素数为 $y_{1}, y_{2}, \cdots, y_{s}$, 并设 $n$ 的素因子分解中 $x_{i}$ 的指数为 $\delta_{i} x_{i}$.

再记 $X=\prod_{i=1}^{t} x_{i}, X_{i}=\frac{X}{x_{i}}, D=\sum_{i=1}^{t} \delta_{i}, Y=\prod_{i=1}^{s} y_{i}, Y_{i}=\frac{Y}{y_{i}}$, 则 $P=X Y$, 且 $f(X)=\sum_{i=1}^{t} X_{i}$ 及 $f(Y)=\sum_{i=1}^{s} Y_{i}$. 于是

$$
\begin{gathered}
B=\sum_{i=1}^{t} \delta_{i} x_{i} X_{i} Y+\sum_{i=1}^{s} X Y_{i}=D X Y+X f(Y) \\
C=\sum_{i=1}^{t}\left(\delta_{i} x_{i}-1\right) X_{i} Y=D X Y-f(X) Y
\end{gathered}
$$

记 $Z=D Y+f(Y)$, 则 $B=X Z$, 故 $f(B)=f(X) Z+X f(Z)$. 代入 (*) 得,

$$
X^{2} Y^{2}=(f(X) Z+X f(Z)) X Y+X Z(D X Y-f(X) Y)
$$

化简得

$$
Y=f(Z)+D Z=f(Z)+D^{2} Y+D f(Y)
$$

当 $D>0$ 时, 由上式知 $f(Z)=f(Y)=0$ 且 $D=1$. 由 $f(Y)=0$ 得 $Y=1$, 故 $s=0$, 即 $n$ 没有指数为 1 的素因子. 而 $D=1$ 意味着 $t=1$ 且 $\delta_{1}=1$, 故 $n=x_{1}^{x_{1}}$.

当 $D=0$ 时, $n=y_{1} y_{2} \cdots y_{s}$ 是不同奇素数的乘积, 这种情形尚未解决.

综上, 目前解出的解为 $n=1$ 或 $p$ 或 $p^{p}$, 其中 $p$ 为奇素数.

评注 (1). 本题中的 $f$ 是一种数论导数.

(2). 北京师范大学海口附属学校列亭枫同学指出, 当 $n=p_{1} p_{2} \cdots p_{s}$ 是不同奇素数的乘积时, $f(n)=q_{1} q_{2} \cdots q_{r}$, 其中 $q_{1}, q_{2}, \cdots, q_{r}$ 是不同于 $p_{1}, p_{2}, \cdots, p_{s}$ 的不同的素数. 此时方程等价于

$$
\left(\sum_{i=1}^{s} \frac{1}{p_{i}}\right)\left(\sum_{j=1}^{r} \frac{1}{q_{j}}\right)=1
$$

这个在 Mathoverflow 论坛 4 上是一个公开的问题.

(3). 广西师范大学附属外国语学校铁山校区叶骐铭同学也讨论到了 $n$ 是不同奇素数的乘积的情形.[^1]


[^0]:    1可参见学生专栏 2016-03-03 期文章 《三角形的伪外接圆》中的性质 1 .

[^1]:    ${ }^{4}$ https://mathoverflow.net/questions/320838/product-of-sum-of-reciprocals-of-prime-numbers

