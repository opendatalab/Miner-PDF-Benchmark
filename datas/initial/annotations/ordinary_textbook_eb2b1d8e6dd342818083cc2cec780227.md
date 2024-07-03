数学新星网 莫学生专栏

www.nsmath.cn/xszl

# 2019 美国国家队选拔考试试题评析 

谢柏庭 韩新森<br>(浙江省乐清知临中学, 325600)<br>指导教师: 羊明亮

近年来, 美国国家队在 IMO 上取得了优异成绩, 其国家队选拔考试试题也备受关注. 今年的试题题目新颖, 解题方法和技巧值得品味. 下面我们整理了今年的试题及其解答, 并加以注记, 供读者参考. 其中部分解答参考了 Evan Chen 的资料.

## I. 试 题

1. $\triangle A B C$ 中, $M, N$ 分别为 $A B, A C$ 的中点. 过 $A$ 作 $\triangle A B C$ 外接圆的切线, 在切线上取一点 $X$. 设圆 $\omega_{B}$ 经过点 $M$ 与 $B$, 且与 $M X$ 相切; 圆 $\omega_{C}$ 经过点 $N$ 与 $C$, 且与 $N X$ 相切. 证明: 圆 $\omega_{B}$ 与 圆 $\omega_{C}$ 的一个交点在直线 $B C$ 上.
2. 设 $\mathbb{Z} / n \mathbb{Z}$ 表示在模 $n$ 意义下的整数集 (因此, $\mathbb{Z} / n \mathbb{Z}$ 有 $n$ 个元素). 求所有的正整数 $n$, 使得存在一个双射函数 $g: \mathbb{Z} / n \mathbb{Z} \rightarrow \mathbb{Z} / n \mathbb{Z}$, 满足 $g(x), g(x)+x$, $g(x)+2 x, \cdots, g(x)+100 x$ 均为 $\mathbb{Z} / n \mathbb{Z}$ 上的双射函数.
3. 在一个由单元格构成的 $n \times n$ 棋盘内, 定义一条长度为 $k$ 的“蛇”为由棋盘内 $k$ 个互不相同的单元格组成的有序序列 $\left(S_{1}, S_{2}, \cdots, S_{k}\right)$, 满足对 $i=1,2, \cdots, k-1$, 单元格 $S_{i}$ 与 $S_{i+1}$ 有一条公共边. 若在棋盘内的一条蛇现对应的单元格序列为 $\left(S_{1}, S_{2}, \cdots, S_{k}\right)$, 而 $S$ 为与 $S_{1}$ 有公共边的空单元格, 则该蛇可以“移动” 到 $\left(S, S_{1}, S_{2}, \cdots, S_{k-1}\right)$. 如果一条蛇最初的序列为 $\left(S_{1}, S_{2}, \cdots, S_{k}\right)$, 经过有限的一系列移动后, 其序列变为 $\left(S_{k}, S_{k-1}, \cdots, S_{1}\right)$, 则称该蛇进行了“转身”.问是否存在正整数 $n>1$, 使得可以在 $n \times n$ 棋盘内放置一条长度至少为 $0.9 n^{2}$,且可以进行转身的蛇?

修订日期: 2019-04-15.

4. 我们称函数 $f: \mathbb{Z}_{\geq 0} \times \mathbb{Z}_{\geq 0} \rightarrow \mathbb{Z}$ 为 “好”的, 如果对任意的非负整数 $m$ 和 $n$, 有

$$
f(m+1, n+1) f(m, n)-f(m+1, n) f(m, n+1)=1
$$

成立. 设 $A=\left(a_{0}, a_{1}, \cdots\right)$ 及 $B=\left(b_{0}, b_{1}, \cdots\right)$ 为两个整数序列, 如果存在一个 “好” 的函数 $f$ 使得 $f(n, 0)=a_{n}, f(0, n)=b_{n}$ 对所有非负整数 $n$ 成立 (特别地, $a_{0}=b_{0}$ ), 则记为 $A \sim B$. 证明: 如果四个整数序列 $A, B, C, D$ 满足 $A \sim B, B \sim C$及 $C \sim D$, 则有 $D \sim A$.

5. 设 $n$ 为正整数, 将 $3 n$ 块蓝宝石和 $3 n$ 块绿宝石串成一个环形项链, 且满足无位置连续的三块宝石为同一颜色. Tasty 和 Stacy 合作玩游戏, 他们轮流按如下的规则每次取走位置连续的三块宝石:

(i) 每当轮到 Tasty 取时, 他所取的三块宝石的颜色依位置顺序必须依次为绿, 蓝, 绿;

(ii) 每当轮到 Stacy 取时, 她所取的三块宝石的颜色依位置顺序必须依次为蓝, 绿, 蓝.

如果他们可经过 $2 n$ 轮取走全部的宝石, 则他们获胜. 证明: 如果他们可以在由 Tasty 先取时获胜, 则他们也可以在由 Stacy 先取时获胜.

6. 设 $\triangle A B C$ 的内心为 $I$, 点 $D$ 在直线 $B C$ 上, 满足 $\angle A I D=90^{\circ}$. 设 $\triangle A B C$中顶点 $A$ 对应的旁切圆切 $B C$ 于点 $A_{1}$. 类似定义点 $B_{1}, C_{1}$. 证明: 如果 $A B_{1} A_{1} C_{1}$为圆内接四边形, 则 $A D$ 与 $\triangle D B_{1} C_{1}$ 的外接圆相切.

## II . 解答与评注

题 1. $\triangle A B C$ 中, $M, N$ 分别为 $A B, A C$ 的中点. 过 $A$ 作 $\triangle A B C$ 外接圆的切线, 在切线上取一点 $X$. 设圆 $\omega_{B}$ 经过点 $M$ 与 $B$, 且与 $M X$ 相切; 圆 $\omega_{C}$ 经过点 $N$ 与 $C$, 且与 $N X$ 相切. 证明: 圆 $\omega_{B}$ 与圆 $\omega_{C}$ 的一个交点在直线 $B C$ 上.

证明 此题有多种解法, 我们取其中较有代表性的几种介绍一下.

方法一(等角线导角): 如图 1 , 作 $\odot(A M N)$, 并过 $X$ 作其另一条切线, 切点为 $Y$. 取 $A Y$ 中点 $L$. 下面我们证明 $Y$ 在 $\omega_{B}$ 上.

由 $M$ 为 $A B$ 的中点, $L$ 为 $A Y$ 的中点知 $M L / / B Y$. 又由 $A X, X Y$ 为 $\odot(A M Y)$切线可知, $M X$ 为 $\triangle A M Y$ 中的 $M-$ 陪位中线, 从而 $\angle X M B=\angle Y M L=$ $\angle M Y B$. 故 $X M$ 与 $\odot(B M Y)$ 相切, 即有 $Y$ 在 $\omega_{B}$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-03.jpg?height=563&width=916&top_left_y=204&top_left_x=570)

图 1

同理, $Y$ 在 $\omega_{C}$ 上. 那么作 $\omega_{B}$ 与 $B C$ 的另一交点 $Z$, 有

$$
\angle Y Z C=\angle Y M B=\angle Y N A
$$

故 $Z$ 也在 $\odot(Y N C)$ 上.

故 $\omega_{B}, \omega_{C}$ 与 $B C$ 交于一点, 原命题获证!

注 此法由供题者 Merlijn Staps 提供.

需要指出两点. 一是 $Y$ 为 $\triangle M Z N$ 对 $\triangle A B C$ 的 Miquel 点, 在考虑了 $\omega_{B}$ 与 $\omega_{C}$ 的情况下考虑 $Y$ 并不意外, 猜测 $Y$ 为另一切点, 有 $A X$ 的提示也是合理的选择; 二是此题导角的方法比较有趣, 利用了等角线来转化, 在涉及中线/陪位中线 / 内(旁)切圆切点/伪内(旁)切圆切点有关的角中可能有用.

方法二: 如图 2, 作 $\omega_{B}$ 与 $B C$ 的另一交点 $S$, 连结 $S M$ 并延长, 交 $C A$ 于 $Y$.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-03.jpg?height=671&width=717&top_left_y=1749&top_left_x=675)

图 2

下面我们证明: (1) $\triangle M X S \sim \triangle A X N$; (2) $S$ 在 $\omega_{C}$ 上.

(1) 的证明 由弦切角定理得

$$
\angle X M S=180^{\circ}-\angle A B C=\angle X A N, \angle X M B=\angle M S B, \angle X A B=\angle A C B,
$$

故结合正弦定理有

$$
\frac{A N}{M S}=\frac{A N}{M B} \cdot \frac{M B}{M S}=\frac{A C}{A B} \cdot \frac{\sin \angle M S B}{\sin \angle A B C}=\frac{\sin \angle M S B}{\sin \angle A C B}=\frac{\sin \angle M S B}{\sin \angle X A B}=\frac{A X}{M X},
$$

结合 $\angle X A N=\angle X M S$ 知 $\triangle X A N \sim \triangle X M S$. 故 (1) 证毕!

(2) 的证明 由

$$
\angle A X M=\angle X M B-\angle X A B=\angle M S B-\angle A C B=\angle M Y A
$$

知 $A, Y, X, M$ 四点共圆. 由 (1) 知 $\angle M S X=\angle A N X$, 故有 $Y, X, S, N$ 四点共圆.从而 $\angle A C B=\angle X A B=\angle X Y S=\angle X N S$, 故 $X N$ 与 $\odot(C N S)$ 相切, 即 $S$ 在 $\omega_{C}$ 上, (2) 证毕!

综合 $(1),(2)$, 原命题获证!

注 此法由 Jetze Zoethout 提供, 可谓一个常规手法, 需要注意的是, 中点条件只用到了 $\frac{A N}{A C}=\frac{B M}{B A}$, 可用于解决推广的问题.

方法三 (等角共轭点的转化): 如图 3, 取 $\triangle A M N$ 中 $X$ 的等角共轭点 $Y$, 作 $Y$ 关于 $M N$ 的对称点 $S$.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-04.jpg?height=477&width=939&top_left_y=1509&top_left_x=587)

图 3

因为 $\angle Y A N=\angle X A M=\angle A C B$, 故 $A Y / / B C$. 结合 $M$ 为 $\triangle A B C$ 中 $B C$边的中位线可知 $S$ 在 $B C$ 上.

下证 $\omega_{B}$ 过 $S$. 这是因为

$$
\angle X M B=\angle Y M N=\angle S M N=\angle M S B .
$$

同理 $\omega_{C}$ 过 $S$. 故 $\omega_{B}, \omega_{C}, B C$ 交于点 $S$. 原命题获证!

注 此法由 Anant Mudgal 提供. 事实上, 此题有如下的模型. 如图 4,

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-05.jpg?height=317&width=636&top_left_y=204&top_left_x=710)

图 4

当 $P, Q$ 为 $\triangle A B C$ 的等角共轭点时, 对 $Q$ 关于 $B C$ 的对称点 $R$, 有

$$
\angle R B C=\angle Q B C=\angle P B D, \quad \angle R C B=\angle Q C B=\angle P C A
$$

故 $A$ 与 $R$ 为 $\triangle P B C$ 的等角共轭点.

此题容易发现 $S$ 与 $A$ 为 $\triangle X M N$ 的等角共轭点, 用此模型一转即有此解法.

方法四 (投影法)：如图 5 , 作 $\omega_{B}, \omega_{C}$ 与 $B C$ 的另一交点 $S, S^{\prime}$, 过 $M, N$ 作 $B C$ 的垂线, 垂足为 $E, F$, 过 $X$ 作 $C A, B A$ 的垂线, 垂足为 $Y, Z$.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-05.jpg?height=594&width=782&top_left_y=1185&top_left_x=637)

图 5

下面我们证明 $S=S^{\prime}$. 为此我们只需证明 $E S+F S^{\prime}=E F$.注意到

$$
\begin{aligned}
E S & =M E \cdot \cot \angle M S E=(M B \cdot \sin \angle A B C) \cdot \cot \angle X M B \\
& =M B \cdot \sin \angle A B C \cdot \frac{A Z-A M}{X Z} \\
& =M B \cdot \sin \angle A B C \cdot \cot \angle A C B-A M^{2} \cdot \frac{\sin \angle A B C}{A X \cdot \sin \angle A C B} \\
& =\frac{1}{2} A C \cdot \cos \angle A C B-\frac{1}{4} \cdot \frac{1}{A X} \cdot A B \cdot A C,
\end{aligned}
$$

同理

$$
F S^{\prime}=\frac{1}{2} A B \cdot \cos \angle A B C+\frac{1}{4} \cdot \frac{1}{A X} \cdot A B \cdot A C,
$$

结合

$$
B C=A C \cdot \cos \angle A C B+A B \cdot \cos \angle A B C, \quad E F=M N=\frac{1}{2} B C
$$

知 $F S^{\prime}+E S=E F$. 故

$$
S=S^{\prime}
$$

即有 $\omega_{B}, \omega_{C}$ 与 $B C$ 交于一点 $S$. 原命题获证!

评析 投影法也可以解决一般的情形, 某种程度上其揭示了此题只是与角度相关. 实际上, 由于 $\angle X M S, \angle X N S^{\prime}$ 均为定值, $X \rightarrow S, X \rightarrow S^{\prime}$ 的角度均保持交比不变, 只需确定三个 $X$ 对应的 $S$ 与 $S^{\prime}$ 重合即可.

题 2. 设 $\mathbb{Z} / n \mathbb{Z}$ 表示在模 $n$ 意义下的整数集 (因此, $\mathbb{Z} / n \mathbb{Z}$ 有 $n$ 个元素). 求所有的正整数 $n$, 使得存在一个双射函数 $g: \mathbb{Z} / n \mathbb{Z} \rightarrow \mathbb{Z} / n \mathbb{Z}$ 满足 $g(x), g(x)+x$, $g(x)+2 x, \cdots, g(x)+100 x$ 均为 $\mathbb{Z} / n \mathbb{Z}$ 上的双射函数.

解 $n$ 为所求当且仅当 $n$ 无不超过 101 的素因子.

一方面, 当 $n$ 不含不超过 101 的素因子时, 取 $g: \mathbb{Z} / n \mathbb{Z} \rightarrow \mathbb{Z} / n \mathbb{Z}$ 为 $g(x)=x$,则 $\forall 0 \leq k \leq 100$, 有 $g(x)+k x=(k+1) x$. 注意到 $1 \leq k+1 \leq 101$, 故 $(k, n)=1$,从而 $k+1,2(k+1), \cdots, n(k+1)$ 构成一个 $\bmod n$ 的完系, 故 $g(x)+k x$ 为 $\mathbb{Z} / n \mathbb{Z}$到自身的双射.

另一方面, 我们先证明如下引理.

引理 设 $p$ 为素数, $\alpha \in \mathbb{N}^{*}$, 则有 $p^{\alpha} \nmid \sum_{r=1}^{p^{\alpha}} r^{p-1}$.

引理证明 当 $\alpha=1$ 时,

$$
\sum_{r=1}^{p} r^{p-1} \equiv p-1 \not \equiv 0(\bmod p)
$$

这里用到 $p^{p-1} \equiv 0(\bmod p)$ 及 $\forall 1 \leq r \leq p-1, r^{p-1} \equiv 1(\bmod p)$.

假设结论对 $\alpha$ 成立, 下面考虑 $\alpha+1$ 的情形.

注意到 $\forall 0 \leq u \leq p-1,1 \leq r \leq p^{2}$, 有

$$
\left(u p^{\alpha}+r\right)^{p-1} \equiv r^{p-1}+(p-1) \cdot r^{p-2} \cdot u p^{\alpha}\left(\bmod p^{\alpha+1}\right)
$$

(用到 $p^{\alpha+1} \mid p^{j \alpha}, 2 \leq j \leq p-1$ ), 故

$$
\begin{aligned}
\sum_{k=1}^{p^{\alpha+1}} k^{p-1} & =\sum_{u=0}^{p-1} \sum_{r=1}^{p^{\alpha}}\left(u p^{\alpha}+r\right)^{p-1} \\
& \equiv \sum_{u=0}^{p-1} \sum_{r=1}^{p^{\alpha}}\left(r^{p-1}+(p-1) \cdot r^{p-2} \cdot u p^{\alpha}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \equiv p \sum_{r=1}^{p^{\alpha}} r^{p-1}+p^{\alpha}(p-1) \sum_{r=1}^{p^{\alpha}} r^{p-2} \sum_{u=0}^{p-1} u \\
& \equiv p \sum_{r=1}^{p^{\alpha}} r^{p-1}+p^{\alpha}(p-1) \cdot \frac{p(p-1)}{2} \sum_{r=1}^{p^{\alpha}} r^{p-2} \\
& \equiv p \sum_{r=1}^{p^{\alpha}} r^{p-1} \quad\left(\text { 当 } p=2 \text { 时, } 2 \mid \sum_{r=1}^{p^{\alpha}} r^{p-2}, \text { 故此式也成立 }\right) \\
& \not \equiv 0\left(\bmod p^{\alpha+1}\right) \quad\left(\text { 用到 } p^{\alpha} \nmid \sum_{r=1}^{p^{\alpha}} r^{p-1}\right) .
\end{aligned}
$$

至此, 引理获证.

回到原题. 考虑下式的值

$$
S=\sum_{k=1}^{t} \sum_{m=1}^{n}(-1)^{k} C_{t}^{k}(g(m)+k m)^{t}
$$

其中, $1 \leq t \leq 100$.

由于 $g(m)+k m(m=1, \cdots, n)$ 构成 $\bmod n$ 的完系, 所以

$$
\begin{aligned}
S & =\sum_{k=0}^{t}(-1)^{k} C_{t}^{k} \sum_{m=1}^{n}(g(m)+k m)^{t} \\
& \equiv \sum_{k=0}^{t}(-1)^{k} C_{t}^{k} \sum_{m=1}^{n} m^{t} \\
& \equiv \sum_{m=1}^{n} m^{t} \cdot(1-1)^{t} \\
& \equiv 0(\bmod n)
\end{aligned}
$$

而记 $f_{m}(x)=(g(m)+m x)^{t}$, 则 $f_{m}(x)$ 为首项系数为 $m^{t}$ 的 $t$ 次整系数多项式, 于是

$$
\triangle^{(t)} f_{m}(x)=t ! \cdot m^{t}
$$

其中 $\triangle h(x)=h(x+1)-h(x)$. 因此

$$
\begin{aligned}
S & =\sum_{m=1}^{n} \sum_{k=0}^{t}(-1)^{k} C_{t}^{k}(g(m)+k m)^{t} \\
& =\sum_{m=1}^{n}(-1)^{t} \cdot \triangle^{(t)} f_{m}(0) \\
& =(-1)^{t} \cdot t ! \cdot \sum_{m=1}^{n} m^{t}
\end{aligned}
$$

假设 $n$ 有不超过 101 的素因子 $p$, 设 $n=l p^{\alpha}\left(\alpha \in \mathbb{N}^{*}, l \in \mathbb{N}^{*}, p \nmid l\right)$, 则

$$
\sum_{m=1}^{n} m^{t}=\sum_{u=0}^{l-1} \sum_{r=1}^{p^{\alpha}}\left(u p^{\alpha}+r\right)^{t}
$$

$$
\begin{aligned}
& \equiv \sum_{u=0}^{l-1} \sum_{r=1}^{p^{\alpha}} r^{t} \\
& \equiv l \sum_{r=1}^{p^{\alpha}} r^{t}\left(\bmod p^{\alpha}\right)
\end{aligned}
$$

取 $t=p-1,($ 则 $1 \leq t \leq 100)$, 由引理及 $p \nmid l, p \nmid t$ ! 即知

$$
S \equiv(-1)^{p-1} \cdot(p-1) ! \cdot l \sum_{r=1}^{p^{\alpha}} \not \equiv 0\left(\bmod p^{\alpha}\right)
$$

这与 $(*)$ 矛盾!

综上所述, $n$ 满足要求的充要条件为 $n$ 不含不超过 101 的素因子. 证毕!

评析 这道题的整体想法是算两次. 一方面固定 $g(m)+k m$ 的 $k$, 利用完系的整体上的性质去计算, 另一方面固定 $g(m)+k m$ 的 $m$, 化为关于 $k$ 的多项式,且利用差分直接让这个多项式成为常数多项式, 再进行求和. 总体来说是一道比较好的数论训练题, 涉及了比较多的东西.

题 3. 在一个由单元格构成的 $n \times n$ 棋盘内, 定义一条长度为 $k$ 的“蛇”为由棋盘内 $k$ 个互不相同的单元格组成的有序序列 $\left(S_{1}, S_{2}, \cdots, S_{k}\right)$, 满足对 $i=1,2, \cdots, k-1$, 单元格 $S_{i}$ 与 $S_{i+1}$ 有一条公共边. 若在棋盘内的一条蛇现对应的单元格序列为 $\left(S_{1}, S_{2}, \cdots, S_{k}\right)$, 而 $S$ 为与 $S_{1}$ 有公共边的空单元格, 则该蛇可以“移动”到 $\left(S, S_{1}, S_{2}, \cdots, S_{k-1}\right)$. 如果一条蛇最初的序列为 $\left(S_{1}, S_{2}, \cdots, S_{k}\right)$, 经过有限的一系列移动后, 其序列变为 $\left(S_{k}, S_{k-1}, \cdots, S_{1}\right)$, 则称该蛇进行了“转身”.问是否存在正整数 $n>1$, 使得可以在 $n \times n$ 棋盘内放置一条长度至少为 $0.9 n^{2}$,且可以进行转身的蛇?

## 解 下面给出两种解答方法.

方法一: 答案是肯定的, 我们给出一种构造方法: 取 $n$ 满足 $(n-4)(n-5)>$ $0.9 n^{2}$ 且 $2 \nmid n$. 设 $n=2 k+1 . k \in \mathbb{N}^{*}$.

下面我们在 $n \times n$ 棋盘中放入一条长为 $(n-4) \times(n-5)$ 的 “蛇,” 并使它可以“转身”. 如图 6 .

称蓝实线标注的区域为“主路”; 称蓝虚线标注的区域为“副路”; 称黑实线标注的区域为“ $A$-连接路”; 称黑虚线标注的区域为为“ $B$-连接路”.

下面我们将“蛇”尾放在 $A_{1}$ 格, 并让“蛇”按“主-副路”顺序延展, 此时“蛇”头应未到 $A_{k-1}$ 格 (否则共 $1+(n-4)(n-5)$ 格).

下面我们分步操作使“蛇”转身.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-09.jpg?height=751&width=910&top_left_y=207&top_left_x=573)

图 6

第一步: 让“蛇”沿“主-副路” (即 $A_{1} \rightarrow B_{1} \rightarrow A_{2} \rightarrow B_{2} \rightarrow \cdots \rightarrow A_{k} \rightarrow B_{k}$ )走到 $B_{k-1}$. 再沿着“ $B$-连接路”走到 $B_{k}$, 再沿“主-副路”走回 $A_{k}$, 再沿“ $A$-连接路”走向 $A_{1}$. 此时“蛇”尾已沿“主-副路”走过 $A_{1}$.

第 $m$ 步: 让“蛇”沿“主-副路”走到 $B_{k-m}, 2 \leq m \leq k$. 此时“蛇”尾已走过 $B_{k}$. (否则“主-副路”中, $A_{1}$ 到 $B_{k-m}$ 及 $A_{k-m+2}$ 到 $B_{k}$ 均为“蛇”一部分. (用到 (m-1)步定义) 此时蛇长不少于 $(n-4)(n-5)+1$, 这不可能!) 再让“蛇”沿“ $B$-连接路”走到 $B_{k}$, 再让“蛇”沿“主-副路”走到 $A_{k-m+1}$, 再让“蛇”沿“ $A$-连接路”走回 $A_{1}$. 此时“蛇”尾已走过 $A_{1}$.

如此便知第 $k$ 步时, “蛇”已转身. 故 $(*)$ 成立.

特别地, 因 $0.9 n^{2}<(n-4)(n-5)$, 故 $n$ 满足条件!

综上, 存在满足条件的 $n$, 原题答案是肯定的.

方法二: 取 $n=10^{10}$, 并令 $m=n-3$, 下面用大正方形表示整个方格表, 小正方形表示方格表第 2 至第 $m+1$ 行及列构成的子方格表.

首先, 将长度为 $0.9 n^{2}$ 的蛇按图 7-1 方式放置, 其中箭头表示蛇首的位置, 实线表示蛇身的位置 (蛇身长度之外的部分无蛇身).

将图 7-1 中的蛇沿图 7-2 中虚线及实线运动, 得到图 7-2 (从箭头所在处沿虚线出发,一直走, 再沿实线, 按图 7-2 中所示路径到达图 7-2 所示位置) (图 7-2 中小正方形左部空出 3 列).

我们说明在上述运动过程中蛇不会碰到身体 (之后蛇运动过程中不会碰到自己的证明方法完全类似).

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=337&width=265&top_left_y=208&top_left_x=707)

图 7-1

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=334&width=257&top_left_y=210&top_left_x=1136)

图 7-2

设在图 7-2 中小正方形内实线最末端方格为 $A$, 最前端 (即箭头所在处) 方格为 $B$. 假设蛇在上述运动过程中在方格 5 处碰到身体.

则沿着图 7-1 中实线, 从 $S$ 到 $B$ 的这段方格此时均被蛇占住, 沿图 7-2 中实线, 从 $A$ 到 $S$ 这段方格均被蛇占住.

又沿图 7-1 中实线, 从 $S$ 到 $B$ 的这段方格包含了沿图 7-2 中实线, 从 $S$ 到 $B$的这段方格.

故此时沿图 7-2 中实线, 从 $A$ 到 $B$ 的这整段方格均被蛇占住. 故

$$
0.9 n^{2}>m^{2}-3 m=(n-3)^{2}-3(n-3)
$$

这与 $n=10^{10}$ 矛盾!

类似地, 可让蛇从图 7-2 运动到图 7-3, 图 7-4, 图 7-5, , , 一直到图 7-6. 至此, 我们让蛇逆时针旋转了 $90^{\circ}$, 再进行一轮类似的操作, 则可变为图 7-7, 即完成了转身.

因此, 这样的 $n$ 存在.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=323&width=388&top_left_y=1683&top_left_x=614)

图 7-3

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=302&width=414&top_left_y=1688&top_left_x=1067)

图 7-4

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=317&width=377&top_left_y=2057&top_left_x=408)

图 7-5

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=315&width=399&top_left_y=2058&top_left_x=857)

图 7-6

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-10.jpg?height=320&width=394&top_left_y=2053&top_left_x=1322)

图 7-7

评析 (1). 此题的第一步是猜答案, 答案是肯定还是否定对应了哲学中的两个东西: 量变和质变. 站在肯定这边, 就希望通过量变的积累来促进质变; 站在
否定这边, 就希望找一个变化过程中不变的“质”, 即不变量.

(2). 对于构造, 此题关键在于问自己这两个问题并予以解答:

(i) “蛇”如何转身?

(ii) $0.9 n^{2}$ (可猜测为 $c n^{2}, c<1$ ) 意味着什么?

(ii) 是容易回答的. “蛇”几乎占据了整个盘. 其可缓冲的空间就只有 (应是) $n$-次级别. 因此若可转身, 转身过程中必有一大部分仍在原来“蛇”的位置上. 想要不撞上这些部分, 就要尽可能地“头咬尾”, 而对于 (i) 的回答则导致了两种解法的产生。

法一据 Nikolai Beluhov (供题者) 解答整理. 据原解答, 其先将图简化为了平面图, 显著简化了原命题, 从而也使全过程很有条理. 法二有一点有趣, 为了转身他没有选择“反向”, 而是选择了“旋转”, 相当于分两步完成了“转身”, 这需要一点前瞻的眼光.

题 4. 我们称函数 $f: \mathbb{Z}_{\geq 0} \times \mathbb{Z}_{\geq 0} \rightarrow \mathbb{Z}$ 为 “好”的, 如果对任意的非负整数 $m$和 $n$, 有

$$
f(m+1, n+1) f(m, n)-f(m+1, n) f(m, n+1)=1
$$

成立. 设 $A=\left(a_{0}, a_{1}, \cdots\right)$ 及 $B=\left(b_{0}, b_{1}, \cdots\right)$ 为两个整数序列, 如果存在一个“好” 的函数 $f$ 使得 $f(n, 0)=a_{n}, f(0, n)=b_{n}$ 对所有非负整数 $n$ 成立 (特别地, $a_{0}=b_{0}$ ), 则记为 $A \sim B$. 证明: 如果四个整数序列 $A, B, C, D$ 满足 $A \sim B, B \sim C$及 $C \sim D$, 则有 $D \sim A$.

证明 下面给出两种证明方法.

方法一: 由 $A \sim B, B \sim C, C \sim D$ 知 $a_{0}=b_{0}=c_{0}=d_{0}$. 记其为 $k$. 设 $f, g, h$ 分别为 $(A, B),(B, C),(C, D)$ 对应的函数, 并构造如下无限阵列

$$
\left[\begin{array}{ccccccccc}
\ddots & & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
& \ddots & \cdots & \cdots & b_{3} & \cdots & \cdots & \cdots & \cdots \\
\cdots & \cdots & g(2,2) & g(2,1) & b_{2} & f(1,2) & f(2,2) & \cdots & \cdots \\
\cdots & \cdots & g(1,2) & g(1,1) & b_{1} & f(1,1) & f(2,1) & \cdots & \cdots \\
\cdots & c_{3} & c_{2} & c_{1} & k & a_{1} & a_{2} & a_{3} & \cdots \\
\cdots & \cdots & h(2,1) & h(1,1) & d_{1} & & & & \\
\cdots & \cdots & h(2,2) & h(1,2) & d_{2} & & & & \\
& & & & d_{3} & & & & \\
& & & & \vdots & & & &
\end{array}\right]
$$

下面只需在第四象限中填入满足要求的数即可.

注意到, 要求为: 对任一 $2 \times 2$ 子矩阵

$$
\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]
$$

有

$$
\left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right|=\left\{\begin{array}{ll}
1, & \text { 若其在二, 四象限 } \\
-1, & \text { 若其在一,三象限 }
\end{array},\right.
$$

故只需证明如下结论: 若我们已有一个 $3 \times 3$ 子阵列

$$
\left[\begin{array}{lll}
a & b & c \\
x & y & z \\
p & q &
\end{array}\right]
$$

其完整的 $2 \times 2$ 子矩阵均满足 $(*)$, 则可在右下角填一个数, 并保持该性质不变.

事实上, 只需考虑其完全在第四象限中的情况 (否则可适当更改 $a, b, c, x, p$的正负号, 右下角方格满足条件不变), 那么可在其中填入数

$$
r= \begin{cases}\frac{q z+1}{y}, & \text { 若 } y \neq 0 ; \\ 1, & \text { 若 } y=0,\end{cases}
$$

对于 (1), 有

$$
\left|\begin{array}{ll}
y & z \\
q & r
\end{array}\right|=1
$$

且因 $b z \equiv x q \equiv-b x \equiv 1(\bmod y)$, 故

$$
z q \equiv-1(\bmod y)
$$

有 $r \in \mathbb{Z}$.

对于 (2), 因 $-b x=b z=x q=1$, 故 $z q=1$, 有

$$
\left|\begin{array}{ll}
y & z \\
q & r
\end{array}\right|=1
$$

故均满足要求!

因此, 可在第四象限中填入满足要求的数, 即有 $A \sim D$, 证毕!

方法二: 我们先证明一个引理.

引理 对数列 $A=\left\{a_{0}, a_{1}, \cdots\right\}$ 及 $B=\left\{b_{0}, b_{1}, \cdots\right\}, A \sim B$ 当且仅当 $a_{0}=b_{0}, a_{0} \mid a_{1} b_{1}+1$, 且 $a_{n}\left|a_{n-1}+a_{n+1}, b_{n}\right| b_{n-1}+b_{n+1}\left(n \in \mathbb{N}^{+}\right)$(上述式子中,当 0 作除数时, “整除” 意为被除数为 0 ).
引理证明 首先证必要性. 显然

$$
a_{0}=b_{0},
$$

由 $a_{0} f(1,1)-a_{1} b_{1}=1$ 知

$$
a_{0} \mid a_{1} b_{1}+1
$$

而对 $n \in \mathbb{N}^{+}$, 由于

$$
f(n, 1) a_{n-1}-f(n-1,1) a_{n}=1, \quad f(n+1,1) a_{n}-f(n, 1) a_{n+1}=1,
$$

故

$$
a_{n}\left|f(n, 1) a_{n-1}-1, \quad a_{n}\right| f(n, 1) a_{n+1}+1 .
$$

因此

$$
a_{n} \mid f(n, 1)\left(a_{n-1}+a_{n+1}\right) \text {. }
$$

当 $a_{n}=0$ 时, $f(n, 1) a_{n-1}=1, f(n, 1) a_{n+1}=-1$. 故

$$
\left(a_{n-1}+a_{n+1}\right) \cdot f(n, 1)=0 \text {, 且 } f(n, 1) \neq 0 \text {, }
$$

因此 $a_{n-1}+a_{n+1}=0$, 有

$$
a_{n} \mid a_{n-1}+a_{n+1} \text {. }
$$

当 $a_{n} \neq 0$ 时, $\left(f(n, 1), a_{n}\right)=1, a_{n} \mid a_{n-1}+a_{n+1}$. 故总有

$$
a_{n} \mid a_{n-1}+a_{n+1} \text {. }
$$

同理

$$
b_{n} \mid b_{n-1}+b_{n+1} \text {. }
$$

综合 $(1),(2),(3),(4)$, 必要性得证.

下证充分性.

我们先证明: 可以先填入 $f(1,1), f(2,1), \cdots$, 使之满足要求, 同时满足数列 $\left(b_{1}, b_{2}, \cdots\right)$ 与 $\left(b_{1}, f(1,1), f(2,1), \cdots\right)$ 满足条件 $(1),(2),(3),(4)$.

我们先用归纳法填入 $f(1,1), f(2,1), \cdots$, 选取 $f(1,1) \in \mathbb{Z}$, 使得

$$
f(1,1) a_{0}=a_{1} b_{1}+1
$$

由 (2) 可知此可行.

当 $f(1,1), f(2,1), \cdots, f(n, 1)$ 已取定时, 取

$$
f(n+1,1)= \begin{cases}1, & \text { 当 } a_{n}=0 \\ \frac{f(n, 1) a_{n+1}+1}{a_{n}}, & \text { 当 } a_{n} \neq 0\end{cases}
$$

对于前者, 有 $f(n, 1) a_{n-1}=1$, 及 $a_{n-1}+a_{n+1}=0$, 故 $f(n, 1) a_{n+1}=-1$, 有

$$
f(n+1,1) a_{n}-f(n, 1) a_{n+1}=1 .
$$

对于后者, 因

$$
f(n, 1) a_{n+1}-f(n-1,1) a_{n}=1, \quad f(n+1,1) a_{n}-f(n, 1) a_{n+1}=1,
$$

结合 $a_{n} \mid a_{n-1}+a_{n+1}$ 知

$$
f(n+1,1)+f(n-1,1) \in \mathbb{Z}
$$

故

$$
f(n+1,1) \in \mathbb{Z}
$$

如此我们得到了满足要求的 $f(1,1), f(2,1), \cdots$, 记为 $P_{1}, P_{2}, \cdots$, 并记 $P_{0}=b_{1}$,则对 $P=\left(P_{0}, P_{1}, \cdots\right)$ 及 $A$ 类似于必要性证明知：因

$$
a_{n-1} P_{n}-a_{n} P_{n-1}=1, \quad a_{n} P_{n+1}-a_{n+1} P_{n}=1,
$$

故

$$
P_{n} \mid P_{n-1}+P_{n+1} \text {. }
$$

类似地,

$$
b_{1} \mid b_{2} P_{1}+1
$$

故 $P$ 与 $B^{*}=\left(b_{1}, b_{2}, \cdots\right)$ 满足 $(1),(2),(3),(4)$.

如此反复即可一行一行地填满第一象限, 充分性得证!

综上所述, 引理获证!

回到原题. 由 $A \sim B, B \sim C, C \sim D$ 知 $a_{0}=b_{0}=c_{0}=d_{0}$, 记为 $k$. 且

$$
k\left|a_{0} b_{0}+1, \quad k\right| b_{0} c_{0}+1, \quad k \mid c_{0} d_{0}+1,
$$

故

$$
k \mid a_{0} d_{0}+1
$$

又由 $A \sim B, C \sim D$ 知

$$
a_{n}\left|a_{n-1}+a_{n+1}, \quad d_{n}\right| d_{n-1}+d_{n+1} .
$$

故 $A, D$ 满足 $(1),(2),(3),(4)$, 有 $A \sim D$. 证毕!

评析 此题要特别小心“ “0”.

两种做法体现对证明两个事物 $A$ 与 $B$ 之间关系的问题的两种看法. 一是为 $A \sim B$. 我们只需要考虑 $A$ 与 $B$ 之间的关系. 例如为证 $A=B$, 证 $A-B=0$. 法
一采取了这种观点, 此法由 Nikolai Beluhov 提供, 颇具巧思; 二是为 $A \sim B$. 我们挖掘 $A$ 与 $B$ 自身的性质, 发现它们具有某个性质 $P$, 从而得到 $A \sim B$. 例如为证 $A=B$, 分别算出 $A$ 和 $B$. 法二采取了这种观点, 更为自然. 需要指出这两种看法也可用于利用这类条件, 并且它们并没有优劣之分, 甚至也没有自然或不自然的说法, 只是两种不同的审视问题的眼光而已. 最好都要意识到, 并分别进行试探, 选择更能充分利用条件,更能突破的路.

题 5. 设 $n$ 为正整数, 将 $3 n$ 块蓝宝石和 $3 n$ 块绿宝石串成一个环形项链, 且满足无位置连续的三块宝石为同一颜色. Tasty 和 Stacy 合作玩游戏, 他们轮流按如下的规则每次取走位置连续的三块宝石:

(i) 每当轮到 Tasty 取时, 他所取的三块宝石的颜色依位置顺序必须依次为绿, 蓝, 绿;

(ii) 每当轮到 Stacy 取时, 她所取的三块宝石的颜色依位置顺序必须依次为蓝, 绿, 蓝.

如果他们可经过 $2 n$ 轮取走全部的宝石, 则他们获胜. 证明: 如果他们可以在由 Tasty 先取时获胜, 则他们也可以在由 Stacy 先取时获胜.

证明 用 $B$ 代表蓝宝石, $G$ 代表绿宝石.

因为无位置连续的三块宝石同色, 所以可将圆圈上的宝石按颜色分为长为 1,2 的若干段. 注意到蓝的段数与绿的段数相同, 且蓝, 绿宝石总数相同, 故蓝, 绿的长为 1 的段数相同, 设为 $a$, 蓝, 绿的长为 2 的段数相同, 设为 $b$.

下证：可在 Tasty 先取时获胜当且仅当 $a \geq b$ (也即 $b \leq n$ ).

先证必要性.

假设 $b>n$. 下考虑圆周上各长度不小于 2 的蓝段长度减 1 之和 (即 $\left.\sum_{l>2}(l-1)\right)$, 记为 $S$.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-15.jpg?height=286&width=300&top_left_y=1993&top_left_x=884)

注意到 Tasty 操作时, $S$ 不减, 且 Stacy 操作时, $S$ 至多减 1. 而一开始 $S=b>n$, 最终 $S=0$, 且 Stacy 共操作了 $n$ 次. 故矛盾!

必要性获证.

再证充分性.
我们采用数学归纳法进行证明.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-16.jpg?height=263&width=174&top_left_y=274&top_left_x=952)

当 $n=1$ 时, 此时圆周上只有两种情况, 容易验证结论成立.

假设结论对 $n-1$ 成立. 下面考虑 $n$ 的情形.

若 $b=0$, 此时结论显然成立. (每两轮两人连续地去掉 $B G B G B G$ 即可)下设 $b \geq 1$.

‥ G B BGB G ...

... $G B-B-G-B B \quad G$...

注意到长为 1 的蓝, 绿段一样多及 $b \geq 1$, 所以必存在一个长为 1 的绿段与一个长为 2 的蓝段相邻. Tasty 在该步去掉以该绿宝石为中间者的连续三块宝石, 则删去后仍不会出现连续三块宝石同色, 且长为 2 的蓝段个数必减 1 , 长为 2 的绿段个数不变.

类似地, 下一步 Stacy 可以操作, 使得仍不出现连续三块宝石同色, 且长为 2 的绿段个数减 1 , 长为 2 的蓝段个数不变 (这只需用到长为 1 的蓝段个数不少于长为 1 的绿段个数).

于是, 这样操作两轮以后, 立即变为 $n-1$ 时的情形 (因此此时 $b^{\prime}=b-1 \leq$ $n-1)$. 由归纳假设立证.

充分性得证.

同理, 有可在 Stacy 先取时获胜当且仅当 $a \geq b$.

由此立得所证结论.

评析 此题再次体现了题 4 注中体现的两种眼光, 让人颇为惊讶的是, 似乎求出充要条件本应是困难的, 但在此题中考虑两种操作方式的互化是极为困难的. 原解答注中特别提及以下三点:

(1) “无位置连续的三块宝石同色”是必要的. 如 G G B G G B G G B B 即为反例。

（2）通常归纳法无法保证上述条件的传递性.

(3) 哪怕加强归纳, 归纳过渡也并不容易. (并不一定对)

可见有些题无法用“第一印象” 来判断方向的, 更体现了两点都要尝试的重要性.
题 6. 设 $\triangle A B C$ 的内心为 $I$, 点 $D$ 在直线 $B C$ 上, 满足 $\angle A I D=90^{\circ}$. 设 $\triangle A B C$ 中顶点 $A$ 对应的旁切圆切 $B C$ 于点 $A_{1}$. 类似定义点 $B_{1}, C_{1}$. 证明: 如果 $A B_{1} A_{1} C_{1}$ 为圆内接四边形, 则 $A D$ 与 $\triangle D B_{1} C_{1}$ 的外接圆相切.

此题几何方法不唯一, 但无一例外地与下述证明中涉及的几何模型有关.

证明 设 $\triangle A B C$ 中 $\angle A, \angle B, \angle C$ 所对的旁心分别为 $I_{A}, I_{B}, I_{C}$, 内切圆 $\odot I$在 $A B, A C$ 上切点为 $X, Y$, 过 $I$ 作 $A D$ 的垂线, 垂足为 $E ; B_{1} C_{1}$ 交 $A D$ 于 $M$. 我们要证明:

(1) $A_{1}, C_{1}, I_{C}$ 三点共线;

(2) $I$ 在 $B_{1} C_{1}$ 上;

(3) $A D$ 为 $\odot\left(A C_{1} B_{1}\right)$ 的切线;

(4) $A D$ 为 $\odot\left(D C_{1} B_{1}\right)$ 的切线.

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-17.jpg?height=805&width=910&top_left_y=1105&top_left_x=573)

图 8

(1) 的证明:

我们注意到 $I_{C} C_{1}, I_{B} B_{1}, I_{A} A_{1}$ 三点共线于 $\triangle I_{A} I_{B} I_{C}$ 外心 $O$, 且

$$
\angle O C_{1} A=\angle O B_{1} A=90^{\circ} \text {, }
$$

有 $A, C_{1}, B, O$ 四点共圆. 由于 $O, A_{1}$ 均在 $A_{1} I_{A}$ 上, 且均在 $\odot\left(A B_{1} C_{1}\right)$ 上, 且在 $B_{1} C_{1}$ 同侧, 故

$$
O \equiv A_{1}
$$

即有 $I_{C}, C_{1}, A_{1}$ 三点共线. (1) 证毕!

(2) 的证明:

对直线 $I_{C} A I_{B}$ 及直线 $B A_{1} C$, 由 Pappus 定理, 结合 (1) 即证!

(3) 的证明:

由于

$$
\angle D I B=\frac{1}{2} \angle A C B=\angle I C B, \angle A I D=\angle I E D=90^{\circ} \text {, }
$$

故

$$
D B \cdot D C=D I^{2}=D E \cdot D A,
$$

有 $A, E, B, C$ 四点共圆. 又 $A, E, X, I, Y$ 五点共圆, 故

$$
\angle E B X=\angle E C Y, \angle E X B=\angle E Y C \text {, }
$$

则有 $\triangle E B X \sim \triangle E C Y$. 故

$$
\frac{E B}{E C}=\frac{B X}{C Y}=\frac{A C_{1}}{A B_{1}}
$$

又 $\angle B E C=\angle C_{1} A B_{1}$, 故

$$
\triangle B E C \sim \triangle C_{1} A B_{1} \text {. }
$$

因此 $\angle A B_{1} C_{1}=\angle E C B=\angle E A B$, 有 $A D$ 为 $\odot\left(A B_{1} C_{1}\right)$ 切线. (3) 证毕!

(4) 的证明:

由 (3) 知

$$
\angle M A I=\angle M A C_{1}+\frac{1}{2} \angle B_{1} A C_{1}=\angle A B_{1} C_{1}+\angle I A B_{1}=\angle A I M .
$$

又 $A I \perp D I$, 故 $A M=M I=D M$. 结合 $(3)$ 知

$$
D M^{2}=A M^{2}=M C \cdot M B,
$$

由切割线定理的逆知 (4) 证毕!

综上, 原命题获证.

评析 我们提取出那几个几何模型.

如图, $\triangle A B C$ 中, 内心为 $I, \angle A, \angle B, \angle C$ 所对的旁心分别为 $I_{A}, I_{B}, I_{C} ; D, E$, $F$ 分别为 $B C, C A, A B$ 的旁切圆切点, 过 $I$ 作 $A I$ 的垂线, 交 $B C$ 于 $R, M$ 为 $A R$中点, $K$ 为弧 $B C$ 中点, $L$ 为弧 $B A C$ 中点, $P$ 为 $L I$ 与 $\odot(A B C)$ 交点, 则有

(1) $I_{C} F, I_{B} E, I_{A} D$ 三点共线于 $\triangle I_{A} I_{B} I_{C}$ 外心 $V, V$ 也为 $\triangle D E F$ 关于 $\triangle A B C$ 的 Miquel 点;

(2) $A, L, F, E$ 四点共圆, 这意味着 $L$ 也为 Miquel 点;

(3) $K, P, R$ 三点共线, 这揭示了伪内切圆切点与此题关联, 且还有 $A D, A P$

![](https://cdn.mathpix.com/cropped/2024_02_26_38140020c34f016fdc73g-19.jpg?height=845&width=903&top_left_y=200&top_left_x=588)

图 9

为 $\angle B A C$ 的等角线;

(4) $A R$ 为 $\odot(A F E)$ 的切线. 由此立知 $F E / / I M$.

如果已知上述结论, 则很快猜出关键. 证明 $I$ 在 $F E$ 上, Pappus 定理稍生僻一些, 但若看出 $(2),(3)$ 后, 可用计算 $A I$ 与 $L I$ 分 $F E$ 的比相等来证明, 简单且自然.

总评 今年美国国家队选拔考试的六个问题, 难度适中, 较为平稳, 具有一定的区分度, 题目新颖, 并注重考查学生对解题策略 (而非知识套用) 的探索能力. 总的来说, 值得一做, 值得思考品味.

