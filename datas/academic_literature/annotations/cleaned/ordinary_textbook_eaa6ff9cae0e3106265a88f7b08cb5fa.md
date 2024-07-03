# 第 32 届 $\mathrm{CMO}$ 试题解答与评析 

丁力煌

(江苏省南京外国语学校, 222008)

指导教师: 黄志军

第 32 届 CMO (中国数学奥林匹克) 于 2016 年 11 月 21 日至 25 日在湖南省长沙市雅礼中学举行. 作为参赛者的我, 在考试中发挥正常, 幸运地取得了满分的好成绩. 下面介绍各题我的解法, 并加以评注, 供大家参考.

题 1. 已知数列 $\left\{u_{n}\right\},\left\{v_{n}\right\}$ 满足

$$
\begin{gathered}
u_{0}=u_{1}=1, \quad u_{n}=2 u_{n-1}-3 u_{n-2}(n \geqslant 2) \\
v_{0}=a, \quad v_{1}=b, \quad v_{2}=c, \quad v_{n}=v_{n-1}-3 v_{n-2}+27 v_{n-3}(n \geqslant 3) .
\end{gathered}
$$

已知存在正整数 $N$, 使得当 $n \geqslant N$ 时, $v_{n}$ 均是整数且可被 $u_{n}$ 整除, 证明: $3 a=2 b+c$.

证明 利用特征方程易求得

$$
u_{n}=\frac{1}{2}\left(\alpha^{n}+\beta^{n}\right), \quad v_{n}=A \alpha^{2 n}+B \beta^{2 n}+C(\alpha \beta)^{n}
$$

其中 $\alpha=1+\sqrt{2} i, \beta=1-\sqrt{2} i$.

由于 $v_{n-3}=\frac{1}{27}\left(v_{n}-v_{n-1}+3 v_{n-2}\right)$, 所以由归纳法易知: $\forall n \in \mathbb{N}^{*}, v_{n} \in \mathbb{Q}$,特别地 $a, b, c \in \mathbb{Q}$.

由条件

$$
\left\{\begin{array}{l}
A+B+C=a \\
A \alpha^{2}+B \beta^{2}+C \alpha \beta=b \\
A \alpha^{4}+B \beta^{4}+C \alpha^{2} \beta^{2}=c
\end{array}\right.
$$

可得 $A, B, C \in \mathbb{Q}[\sqrt{-2}]$, 又因为可将 $v_{n}$ 乘上 $A, B, C$ 的公分母, 故可设 $A, B, C \in \mathbb{Z}[\sqrt{-2}]$.

收稿日期: 2016-12-14； 修订日期: 2017-01-06.
由于 $\alpha=\bar{\beta}$, 所以对 $v_{n}$ 取共轭知 $A=\bar{B}$, 故 $A \alpha^{n}+B \beta^{n} \in \mathbb{R}$, 又注意到 $A \alpha^{n}+B \beta^{n} \in \mathbb{Z}[\sqrt{-2}]$, 故

$$
A \alpha^{n}+B \beta^{n} \in \mathbb{Z}[\sqrt{-2}] \cap \mathbb{R}=\mathbb{Z}
$$

所以

$$
u_{n} \mid\left(\alpha^{n}+\beta^{n}\right)\left(A \alpha^{n}+B \beta^{n}\right)=v_{n}+3^{n} \cdot(C-A-B) .
$$

注意到 $\left(u_{n}, 3\right)=1$ 及 $n \geq N$ 时有 $u_{n} \mid v_{n}$, 所以当 $n \geq N$ 时, $u_{n} \mid C-A-B$.又由 $|\alpha|=\sqrt{3}>1$ 知 $\left|u_{n}\right|$ 无界. 所以 $C-A-B=0$, 即

$$
C=A+B .
$$

将 (1) 代入 $(*)$ 式可得

$$
a=2(A+B), \quad b=2(A \alpha+B \beta), \quad c=-2\left(A \alpha^{2}+B \beta^{2}\right) .
$$

故

$$
3 a-2 b-c=2\left(A\left(3-2 \alpha+\alpha^{2}\right)+B\left(3-2 \beta+\beta^{2}\right)\right)=0 .
$$

评注 作者不知道此题是否有纯递推的做法, 似乎应用特征方程写出通项公式是必须的. 在写出通项公式后, 我在考场上也想过很多方向, 感觉如果不联想到 $\mathbb{Q}[\sqrt{-2}]$ 或 $\mathbb{Z}[\sqrt{-2}]$ (虽然只是用到了最基本的性质, 完全可以用 $\mathbb{Q}$ 或 $\mathbb{Z}$代替) 的话做起来似乎还不太方便. 故作者认为本题是一道难度偏大的第一题.对熟悉 $\mathbb{Q}[\sqrt{-2}]$ 的选手, 这题却是一道不难的题.

题 2. 如图所示, 锐角 $\triangle A B C$ 中, $A B>A C, \odot O$ 和 $\odot I$ 分别是 $\triangle A B C$ 的外接圆和内切圆, $\odot I$ 与边 $B C$ 相切于点 $D$, 直线 $A O$ 与边 $B C$ 相交于点 $X$, $A Y$ 是边 $B C$ 上的高, $\odot O$ 在点 $B, C$ 处的切线相交于点 $L, P Q$ 是过点 $I$ 的 $\odot O$直径. 证明: $A, D, L$ 三点共线当且仅当 $P, X, Y, Q$ 四点共圆.

证明 设 $B C=a, C A=b, A B=c, p=\frac{1}{2}(a+b+c)$. 则

$$
B D=p-b, C D=p-c .
$$

由正弦定理知,

$$
\frac{A B}{\sin \angle A D B}=\frac{B D}{\sin \angle B A D}, \quad \frac{A C}{\sin \angle A D C}=\frac{C D}{\sin \angle C A D},
$$



对上面两式相除有

$$
\frac{\sin \angle B A D}{\sin \angle C A D}=\frac{B D \cdot A C}{A B \cdot C D}=\frac{b(p-b)}{c(p-c)}
$$

再由正弦定理知，

$$
\begin{gathered}
\frac{B L}{\sin \angle B A L}=\frac{A L}{\sin \angle A B L}, \quad \frac{C L}{\sin \angle C A L}=\frac{A L}{\sin \angle A C L}, \\
\angle A B L=180^{\circ}-\angle A C B, \quad \angle A C L=180^{\circ}-\angle A B C, \quad B L=C L .
\end{gathered}
$$

因此

$$
\frac{\sin \angle B A L}{\sin \angle C A L}=\frac{B L \sin \angle A B L}{C L \sin A C L}=\frac{\sin \angle A C B}{\sin \angle A B C}=\frac{c}{b} .
$$

从而

$$
\begin{aligned}
A, D, L \text { 共线 } & \Leftrightarrow \frac{\sin \angle B A D}{\sin \angle C A D}=\frac{\sin \angle B A L}{\sin \angle C A L} \\
& \Leftrightarrow \frac{b(p-b)}{c(p-c)}=\frac{c}{b} \\
& \Leftrightarrow b^{2}(p-b)=c^{2}(p-c) \\
& \Leftrightarrow(b-c)\left(p(b+c)-\left(b^{2}+b c+c^{2}\right)\right)=0 \\
& \Leftrightarrow(b-c) \cdot\left(a(b+c)-\left(b^{2}+c^{2}\right)\right)=0 \\
& \Leftrightarrow a(b+c)=b^{2}+c^{2}(\text { 由 } A B>A C) .
\end{aligned}
$$

设过 $A$ 的 $\odot O$ 切线交 $B C$ 于 $T, O I$ 交 $B C$ 于 $N, A I$ 交 $B C$ 于 $E$. 则

$$
\begin{aligned}
\angle T A Y & =\angle T A C+\angle C A Y \\
& =\angle T B A+90^{\circ}-\angle A C B \\
& =\angle T B A+\angle B A X=\angle T X A .
\end{aligned}
$$

所以 $\triangle T X A \sim \triangle T A Y$, 因此 $T A^{2}=T X \cdot T Y$. 又因为

$$
\angle T A E=\angle T A C+\angle C A E=\angle C B A+\angle B A E=\angle T E A,
$$

于是 $T A=T E$.

由割线定理知, $T A^{2}=T B \cdot T C$, 从而 $T X \cdot T Y=T B \cdot T C$. 又由割线定理, $N P \cdot N Q=N B \cdot N C$. 则

$$
\begin{aligned}
P, Q, X, Y \text { 共圆 } & \Leftrightarrow N P \cdot N Q=N X \cdot N Y \\
& \Leftrightarrow N B \cdot N C=N X \cdot N Y .
\end{aligned}
$$

设 $B X=u, X Y=v, C Y=w$, 则 $u \neq w$. 设 $C N=t$. 将其代入 (2) 中有

$$
t \cdot(t+u+v+w)=(t+w)(t+v+w),
$$

所以 $t \cdot(u-w)=w \cdot(v+w)$, 因此 $t$ 唯一. 故

$$
(2) \Leftrightarrow N=T \Leftrightarrow O, I, T \text { 共线. }
$$

由正弦定理知，

$$
\begin{aligned}
& \frac{\sin \angle A T I}{\sin \angle E T I}=\frac{\frac{A I}{A T} \cdot \sin \angle A I T}{\frac{I E}{E T} \cdot \sin \angle E I T}=\frac{A I}{I E}=\frac{b+c}{a} \\
& \frac{\sin \angle A T O}{\sin \angle E T O}=\frac{\frac{A O}{O T} \cdot \sin \angle O A T}{\frac{O E}{O T} \cdot \sin \angle O E T}=\frac{A O}{O E \cdot \sin \angle O E T} .
\end{aligned}
$$

又

$$
\sin \angle O E C=\frac{O C}{O E} \cdot \sin \angle O C B=\frac{O C}{O E} \cdot \cos A,
$$

所以

$$
\frac{\sin \angle A T O}{\sin \angle E T O}=\frac{A O}{O C \cdot \cos A}=\frac{2 b c}{b^{2}+c^{2}-a^{2}} .
$$

故

$$
\begin{aligned}
(3) & \Leftrightarrow \frac{\sin \angle A T I}{\sin \angle E T I}=\frac{\sin \angle A T O}{\sin \angle E T O} \\
& \Leftrightarrow \frac{b+c}{a}=\frac{2 b c}{b^{2}+c^{2}+a^{2}} \\
& \Leftrightarrow(b+c) a^{2}-2 b c a-(b+c)\left(b^{2}+c^{2}\right)=0 \\
& \Leftrightarrow(a+b+c)\left(a(b+c)-\left(b^{2}+c^{2}\right)\right)=0 \\
& \Leftrightarrow a(b+c)=\left(b^{2}+c^{2}\right) .
\end{aligned}
$$

由 (1), (4) 知 $A, D, L$ 共线 $\Leftrightarrow P, Q, X, Y$ 共圆.
评注 这题作者觉得纯几何方法并不容易想到, 或者说至少要求选手很熟悉极线或反演那一套理论, 这对于一般的冬令营选手 (包括作者) 是不可能的.但如果能结合一定量的几何推导并进行三角计算的话本题还是不太难的. 事实上从作者出考场听到的情况来看, 平时擅长纯几何题的人做出来的并不多, 而平时擅长计算的做出来的不少. 故作者认为这题是一个偏向计算的几何题, 计算难度不大, 几何难度不小.

题 3. 矩形 $R$ 被分割成 2016 个小矩形, 每个小矩形的边都平行于 $R$ 的边,小矩形的顶点称为结点. 一条在小矩形边上的线段, 若其两个端点都是结点, 并且其内部不含其它结点, 则称这条线段为基本线段. 考虑所有分割方式, 求基本线段条数的最大值和最小值.

解 以所有结点为顶点, 基本线段为边, 作一个图 $G$. 设 $G$ 的顶点数设为 $v$,边数为 $e$. 将矩形 $R$ 外部区域看作一个面 (区域), 则 $G$ 共有面数 $f=2017$.

由欧拉定理知 $v+f-e=2$, 因此

$$
e=v+2015 \text {. }
$$

因为 $G$ 的度数为 2 的点恰 4 个, 其余点度为 3 或 4 . 度 2 的点为 1 个矩形的顶点, 度 3 的点为 2 个矩形的顶点, 度 4 的点为 4 个矩形的顶点.

又每个小矩形的所有顶点数之和为 $4 \times 2016$.

而另一方面, 所有小矩形的顶点数之和 $\geq 2(v-4)+4=2 v-4$.

所以

$$
2 v-4 \leq 4 \times 2016 \text {. }
$$

因此 $v \leq 4034$.

故由 (1) 可得 $e \leq 6049$, 当将 $R$ 划分为 $1 \times 2016$ 个小矩形时取等号.

故所求的最大值 $e_{\text {max }}=6049$.

下再考虑 $e$ 的最小值.

设分割矩形 $R$ 共用了 $a$ 条横线和 $b$ 条坚线, 这里的横线和坚线均不算边界.因 $a$ 条横线, $b$ 条坚线至多分出 $(a+1)(b+1)$ 个区域, 所以

$$
(a+1)(b+1) \geq 2016 \text {. }
$$

设度 3 的点有 $x$ 个, 度 4 的点有 $y$ 个, 则

$$
v=4+x+y, \quad 4+2 x+4 y=4 \times 2016
$$

又注意到每条横线和坚线最两侧的点为两个矩形顶点, 因此都是度 3 的点,且这些点互不重复. 故

$$
x \geq 2 a+2 b \text {. }
$$

由 $(2),(4)$ 可得

$$
\begin{aligned}
x & \geq 2((a+1)+(b+1))-4 \\
& \geq 4 \sqrt{(a+1)(b+1)}-4 \\
& \geq 4 \sqrt{2016}-4>175.59
\end{aligned}
$$

因此

$$
x \geq 176
$$

这样由 (3), (5) 可得

$$
v=2019+\frac{1}{2} x \geq 2107
$$

这时再由 (1) 立得

$$
e \geq 4122
$$

其中等号在 $42 \times 48$ 的划分中取得.

故 $e_{\min }=4122$.

评注 这题作者觉得是一道质量很高的题目, 首先需要观察到转化成图论问题后, 这题边数不好表示, 但点数计算方便 (因为一个矩形一定是四个顶点, 但不知道会有几条边 $)$, 于是想到用点数来表示边数且已知区域数, 自然联想到欧拉公式, 想到这步的话最大值就是显然的. 关于最小值的话就相当于求点数的最小值, 也就是相当于让恰在两个矩形上的点数尽量少, 画一下矩形数较少的情况就可以发现这样的点出现在四周时候最少, 所以证明四周的点必定是恰好两个矩形的顶点, 构造可以从小的时候顺便得到. 作者认为此题难度不大, 应该是第一天最简单的题.

题 4. 设 $n \geqslant 2$. 对于 $1,2, \cdots, n$ 的任意两个排列 $\alpha=\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 和 $\beta=\left(b_{1}, b_{2}, \cdots, b_{n}\right)$, 若存在正整数 $k \leqslant n$ 使得

$$
b_{i}= \begin{cases}a_{k+1-i}, & 1 \leqslant i \leqslant k \\ a_{i}, & k+1 \leq i \leqslant n,\end{cases}
$$

则称 $\alpha$ 和 $\beta$ 互为翻转. 证明: 可以把 $1,2, \cdots, n$ 的所有排列适当记为 $P_{1}, P_{2}, \cdots, P_{m}$, 使得对每个 $i=1,2, \cdots, m, P_{i}$ 与 $P_{i+1}$ 互为翻转, 这里 $m=n !$且规定 $P_{m+1}=P_{1}$.

证明 用归纳法证明: 可将 $a_{1}, \cdots, a_{n}$ 的所有排列符合要求排好且第一个为 $\left(a_{1}, \cdots, a_{n}\right)$, 最后一个为 $\left(a_{n}, \cdots, a_{1}\right)$.

当 $n=1$ 时, 显然成立.

假设 $n-1$ 时成立, 现考虑 $n$ 的情况. 对 $\forall 1 \leq i \leq n$, 由归纳假设知, 存在 $a_{1}, \cdots, a_{i-1}, a_{i+1}, \cdots, a_{n}$ 的所有排列的满足要求的排法，且以 $\left(a_{i+1}, \cdots, a_{n}, a_{1}, \cdots, a_{i-1}\right)$ 为开头, 以 $\left(a_{i-1}, \cdots, a_{1}, a_{n}, \cdots, a_{i+1}\right)$ 为结尾. 现在每个这样的排列的最后添加一个 $a_{i}$ 得到 $a_{1}, \cdots, a_{n}$ 的 $(n-1)$ ! 个排列它们满足要求, 且以 $\left(a_{i+1}, \cdots, a_{n}, a_{1}, \cdots, a_{i-1}, a_{i}\right)$ 开头, $\left(a_{i-1}, \cdots, a_{1}, a_{n}, \cdots, a_{i+1}, a_{i}\right)$ 结尾, 且所有以 $a_{i}$ 结尾的排列均出现.

记这 $(n-1)$ ! 个排列的排列为 $Q_{i}$. 这样就把 $a_{1}, \cdots, a_{n}$ 所有排列分成了 $Q_{1}, Q_{2}, \cdots, Q_{n}$ 这 $n$ 组. 再将 $Q_{i-1}(2 \leq i \leq n)$ 的最后一个排列接上 $Q_{i}$ 的最初一个排列. 进行衔接时, 由于 $\left(a_{i-1}, \cdots, a_{1}, a_{n}, \cdots, a_{i}\right)$ 为 $\left(a_{i}, \cdots, a_{n}, a_{1}, \cdots, a_{i-1}\right)$的整体翻折, 因此衔接相邻的两个排列满足要求, 从而所有排列的这种排法满足要求, 且最后一个为 $\left(a_{n}, \cdots, a_{1}\right)$, 第一个为 $\left(a_{1}, \cdots, a_{n}\right)$.

评注 作者认为此题是全卷最简单的题, 观察一下 $n$ 小的情况就可以得到一个归纳的做法了.

题 5. 用 $D_{n}$ 表示正整数 $n$ 的所有正约数构成的集合. 求所有正整数 $n$, 使得 $D_{n}$ 可以写成两个不相交的子集 $A$ 和 $G$ 的并, 且满足: $A$ 和 $G$ 均含有至少三个元素, $A$ 中元素可以排列成一个等差数列, $G$ 中元素可以排列成一个等比数列。

解 答案是这样的 $n$ 不存在.

下面用反证法. 假设这样的 $n$ 存在. 设

$$
A=\left\{a_{1}<\cdots<a_{m}\right\}, \quad G=\left\{b_{1}<\cdots<b_{k}\right\} .
$$

(1) 若 $n \in A$, 则 $a_{m}=n$. 设 $a_{m-1}=\frac{n}{x}, x>1$, 因此

$$
a_{m-1} \leq \frac{n}{2}
$$

所以公差 $d \geq n-\frac{n}{2}=\frac{n}{2}$, 故

$$
a_{m-2}=n-2 d \leq 0 \text {, }
$$

矛盾!

这说明 $n \in G$, 现对 $n$ 进行如下讨论.

(2) 若 $n=p^{t}, p$ 为素数, $t \in \mathbb{N}^{*}$, 则

$$
a_{1}=p^{\alpha_{1}}, \quad a_{2}=p^{\alpha_{2}}, a_{3}=p^{\alpha_{3}}, \quad \alpha_{1}<\alpha_{2}<\alpha_{3}
$$

所以

$$
a_{3} \geq p a_{2} \geq 2 a_{2}=a_{1}+a_{3}
$$

矛盾!

(3) 故 $n$ 至少有 2 个素因子, 设 $n$ 最小的两个素因子为 $p<q$.

a) 若 $\frac{n}{p} \in G$. 因为 $n \in G$, 则 $G$ 公比为 $p$. 若 $1 \in G$, 则 $n=p^{\alpha}, \alpha \in \mathbb{N}^{*}$, 矛盾. 故 $1 \in A$. 同理 $p \in A$. 考虑到 $1, p$ 是 $n$ 的最小的两个因子. 故 $A$ 的公差为 $p-1$. 因为 $p, q$ 互素, 则 $\frac{n}{q} \in A$, 因此

$$
m \geq \frac{\frac{n}{q}-1}{p-1}+1>\frac{n}{p q}+1 .
$$

b) 若 $\frac{n}{p} \in A$, 则由于 $1, p, q$ 至少 2 个在 $A$ 中. 所以

$$
m \geq \frac{\frac{n}{p}-p}{q-p}+1 \text { 或 } m \geq \frac{\frac{n}{p}-1}{q-1}+1 \text {. }
$$

故

$$
m>\frac{\frac{n}{p}}{q}+1=\frac{n}{p q}+1
$$

结合 a), b) 可知

$$
m>\frac{n}{p q}+1 \Rightarrow m \geq \frac{n}{p q}+2
$$

设 $n=p_{1}^{\alpha_{1}} \cdots p_{t}^{\alpha_{t}}, p_{1}=p, p_{2}=q$. 由于 $G$ 含有至少 3 个元素, 故

$$
m \leq\left(\alpha_{1}+1\right) \cdots\left(\alpha_{t}+1\right)-3
$$

又由于

$$
m \geq 2+p^{\alpha_{1}-1} q^{\alpha_{2}-1} p_{3}^{\alpha_{3}} \cdots p_{t}^{\alpha_{t}}
$$

并注意到当 $k \geq 3$ 时 $p_{k} \geq 5$, 有 $p_{k}^{\alpha_{k}}>\left(\alpha_{k}+1\right)$. 所以

$$
\left(\alpha_{1}+1\right)\left(\alpha_{2}+1\right) \geq 2^{\alpha_{1}-1} \cdot 3^{\alpha_{2}-1}+5
$$

i) 若 $\alpha_{2} \geq 3$, 则 $\alpha_{2}+1 \leq 3^{\alpha_{2}-1}-1$. 再由 $(*)$ 式可得

$$
\left(\alpha_{1}+1-2^{\alpha_{1}-1}\right) \cdot 3^{\alpha_{2}-1} \geq \alpha_{1}+1+5
$$

因此

$$
\alpha_{1}+1-2^{\alpha_{1}-1}>0
$$

故 $\alpha_{1} \leq 2$.

(1) 当 $\alpha_{1}=1$ 时, 由 $(*)$ 式得 $2 \cdot\left(\alpha_{2}+1\right) \geq 3^{\alpha_{2}-1}+5$, 从而

$$
3^{\alpha_{2}-1} \leq 2 \alpha_{2}-3=2\left(\alpha_{2}-1\right)-1 \text {, }
$$

矛盾!

(2) 当 $\alpha_{1}=2$ 时, 由 $(*)$ 式得 $3 \cdot\left(\alpha_{2}+1\right) \geq 2 \cdot 3^{\alpha_{2}-1}+5$, 从而

$$
2 \cdot 3^{\alpha_{2}-1} \leq 3\left(\alpha_{2}-1\right)+1
$$

矛盾!

ii) 若 $\alpha_{2} \leq 2$, 则

(1) 当 $\alpha_{2}=1$ 时, 由 $(*)$ 式得 $2\left(\alpha_{1}+1\right) \geq 2^{\alpha_{1}-1}+5$, 于是

$$
2^{\alpha_{1}-1} \leq 2\left(\alpha_{1}-1\right)-1
$$

矛盾!

(2) 当 $\alpha_{2}=2$ 时, 由 $(*)$ 式得,

$$
\begin{aligned}
& 3\left(\alpha_{1}+1\right) \geq 3 \cdot 2^{\alpha_{1}-1}+5, \\
\Rightarrow & 3\left(\alpha_{1}+1\right) \geq 3 \cdot 2^{\alpha_{1}-1}+6 . \\
\Rightarrow & 2^{\alpha_{1}-1} \leq \alpha_{1}-1,
\end{aligned}
$$

矛盾!

综上所述, $n$ 无解.

评注 作者认为此题不算一道难题, 直接暴力讨论即可, 但较为耗时, 想到思路不困难, 写完整过程需要比较长的时间.

题 6. 给定整数 $n \geqslant 2$, 以及正数 $a<b$. 设实数 $x_{1}, x_{2}, \ldots, x_{n} \in[a, b]$. 求

$$
\frac{\frac{x_{1}^{2}}{x_{2}}+\frac{x_{2}^{2}}{x_{3}}+\cdots+\frac{x_{n-1}^{2}}{x_{n}}+\frac{x_{n}^{2}}{x_{1}}}{x_{1}+x_{2}+\cdots+x_{n-1}+x_{n}}
$$

的最大值.
解 设 $f\left(x_{1}, \cdots, x_{n}\right)=\frac{\frac{x_{1}^{2}}{x_{2}}+\cdots+\frac{x_{n}^{2}}{x_{1}}}{x_{1}+\cdots+x_{n}}$. 固定 $x_{2}, \cdots, x_{n}$, 设

$$
g(x)=f\left(x, x_{2}, \cdots, x_{n}\right)=\frac{\frac{x^{2}}{c}+\frac{d^{2}}{x}+T}{x+S}, x \in[a, b]
$$

其中 $S=x_{2}+\cdots+x_{n}, T=\frac{x_{2}^{2}}{x_{3}}+\cdots+\frac{x_{n-1}^{2}}{x_{n}}, c=x_{2}, \quad d=x_{n}$. 则

$$
\begin{aligned}
g^{\prime}(x)= & \frac{1}{(S+x)^{2}}\left[-\frac{S d^{2}}{x^{2}}-\frac{2 d^{2}}{x}-T+\frac{2 S x}{c}+\frac{x^{2}}{c}\right], \\
g^{\prime \prime}(x)= & \frac{1}{(S+x)^{3}}\left\{\left[\frac{2 S d^{2}}{x^{3}}+\frac{2 d^{2}}{x^{2}}+\frac{2 S}{c}+\frac{2 x}{c}\right](S+x)\right. \\
& \left.+2\left[\frac{S d^{2}}{x^{2}}+\frac{2 d^{2}}{x^{2}}+T\right]-2\left[\frac{2 S x}{c}+\frac{x^{2}}{c}\right]\right\} .
\end{aligned}
$$

注意到

$$
\left(\frac{2 S}{c}+\frac{2 x}{c}\right)(S+x)-2\left(\frac{2 S x}{c}+\frac{x^{2}}{c}\right)=\frac{2 S^{2}}{c}>0 .
$$

因此 $g^{\prime \prime}(x)>0$. 这说明 $g(x)$ 是凸函数, 因此它在 $[a, b]$ 的最大值在 $x=a$ 或 $x=b$ 处取得.

再依次对其它变元 $x_{2}, \cdots, x_{n}$ 作上述讨论知当 $\left\{x_{i}\right\}$ 取端点, 即 $x_{1}, x_{2}, \cdots, x_{n}$ $\in\{a, b\}, f\left(x_{1}, \cdots, x_{n}\right)$ 取得最大值.

设 $\left(x_{i}, x_{i+1}\right)(i=1,2, \cdots, n)$ 中有 $u$ 个 $(a, a), v$ 个 $(a, b), w$ 个 $(b, b), z$ 个 $(b, a)$. 则 $v=z, x_{i}(i=1,2, \cdots, n)$ 中共有 $u+v$ 个 $a, v+w$ 个 $b$, 则 $u+w+2 v=n$, $v \leq \frac{n}{2}$.

所以

$$
\begin{aligned}
f\left(x_{1}, \cdots, x_{n}\right) & \leq \frac{u \cdot a+w \cdot b+v \cdot\left(\frac{a^{2}}{b}+\frac{b^{2}}{a}\right)}{a \cdot(u+v)+b \cdot(v+w)} \\
& =1+\frac{v\left(\frac{a^{2}}{b}+\frac{b^{2}}{a}-a-b\right)}{a u+b w+(a+b) v} \\
& =1+\frac{\frac{a^{2}}{b}+\frac{b^{2}}{a}-(a+b)}{\frac{a u+b w}{v}+(a+b)} .
\end{aligned}
$$

又注意到

$$
\frac{a u+b w}{v} \geq \frac{a(u+w)}{v}=\frac{a(n-2 v)}{v}, \quad\left(\frac{a^{2}}{b}+\frac{b^{2}}{a}\right) \geq \frac{(a+b)^{2}}{a+b}=a+b .
$$

我们有

1) 当 $n$ 为偶数时, 注意到 $\frac{a(n-2 v)}{v} \geq 0$, 故

$$
f\left(x_{1}, \cdots, x_{n}\right) \leq \frac{\frac{a^{2}}{b}+\frac{b^{2}}{a}}{a+b}=\frac{a^{2}-a b+b^{2}}{a b} .
$$

此时取 $x_{1}=x_{3}=\cdots=x_{n-1}=a, x_{2}=x_{4}=\cdots=x_{n}=b$ 时等号成立. 因此当 $n$ 为偶数时, $f_{\text {max }}=\frac{a^{2}-a b+b^{2}}{a b}$.

2) 当 $n$ 为奇数时, 注意到 $\frac{a(n-2 v)}{v} \geq \frac{a}{\frac{n-1}{2}}=\frac{2 a}{n-1}$, 故

$$
\begin{aligned}
f\left(x_{1}, \cdots, x_{n}\right) & \leq 1+\frac{\frac{a^{2}}{b}+\frac{b^{2}}{a}-(a+b)}{\frac{2 a}{n-1}+a+b} \\
& =\frac{(n-1)\left(a^{3}+b^{3}\right)+2 a^{3} b}{a b((n+1) a+(n-1) b)} .
\end{aligned}
$$

此时取 $x_{1}=x_{3}=\cdots=x_{n}=a, x_{2}=x_{4}=\cdots=x_{n-1}=b$ 时等号成立. 因此当 $n$ 为奇数时, $f_{\text {max }}=\frac{(n-1)\left(a^{3}+b^{3}\right)+2 a^{3} b}{a b((n+1) a+(n-1) b)}$.

评注 这题作者认为是一道调整法的好题, 通过计算验证目标函数关于任一个变元 (其它元固定) 是凸函数, 可把每个变元调整到端点 $a$ 或 $b$ 取最大值, 然后直接按连续两个数来分类计算即可. 应该难度比第 5 题略大, 但所需时间不多, 作者认为是第二天的难度适中的一题.

对于整个试卷, 我认为: 这整套卷子难度适中. 第一天偏向想法, 第二天偏向写过程. 如果能把第 1 题和第 4 题交换一下位置, 第 2 题和第 6 题交换位置就更好了。

