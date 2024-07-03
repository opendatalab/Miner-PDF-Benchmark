数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2021 年亚洲太平洋地区数学奥林匹克试题评析 

张甲<br>(河南省郑州市第一中学, 450048)

本文给出 2021 年亚洲太平洋地区数学奥林匹克问题的评析. 一共 5 道题目,第 1 题较容易, 笔者认为 $2,3,4,5$ 题可以作为联赛加试模拟题. 不当之处还请批评指正.

## I. 试 题

1. 已知 $r$ 为大于 2 的实数. 求证: 恰存在 2 个或 3 个正实数 $x$ 满足 $x^{2}=$ $r\lfloor x\rfloor$.其中 $\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数.
2. 对于多项式 $P$ 和正整数 $n$, 记 $P_{n}$ 为使得 $|P(a)|-|P(b)|$ 能被 $n$ 整除的正整数数组 $(a, b)(a<b \leq n)$ 的个数. 求所有的整系数多项式 $P$, 使得对于任意正整数 $n$, 都有 $P_{n} \leq 2021$.
3. 凸四边形 $A B C D$ 内接于圆 $\Gamma$, 点 $E$ 为对角线 $A C, B D$ 的交点. 点 $L$ 为与边 $A B, B C, C D$ 均相切的圆的圆心, 点 $M$ 为 $\Gamma$ 的弧 $B C$ (不包含点 $A$ 和点 $D)$ 的中点. 证明: $\triangle B C E$ 的 $\angle E$ 内的旁心在直线 $L M$ 上.

注: $\triangle B C E$ 的 $\angle E$ 内的旁心指与线段 $B C$ 、射线 $E B$ 、射线 $E C$ 均相切的圆的圆心, 而非内切圆圆心.



修订日期: 2021-06-12.

4. 有一个 $32 \times 32$ 的正方形网格, 开始时, 一只老鼠位于左下方的方格中,且面朝正上方. 选定除左下方的方格以外的若干个方格, 在其中各放置一块奶酪. 接着老鼠重复以下动作, 直到爬出网格外: 一直沿直线前进到放有奶酪的方格中, 吃一口奶酪(并不吃光)后从前进方向开始右转 $90^{\circ}$. 如果老鼠在爬出网格时, 恰好品尝了所有奶酪, 则称这是一种好的放法.

证明: (1) 对于 888 块奶酪, 没有好的放法;

(2) 存在一种好的放法, 可放置 666 块及以上奶酪.

5. 求所有定义域和值域均为整数的函数 $f$, 使得: 对于任意的整数 $a, b$,

$$
f(f(a)-b)+b f(2 a)
$$

均为完全平方数.

## II . 解答与评注

题 1 已知 $r$ 为大于 2 的实数. 求证: 恰存在 2 个或 3 个正实数 $x$ 满足 $x^{2}=r\lfloor x\rfloor$. 其中 $\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数.

证明 设 $r>2, r \in \mathbb{R}, x$ 是满足 $x^{2}=r\lfloor x\rfloor$ 的正实数, 且 $\lfloor x\rfloor=k$.

由 $x>0, x^{2}=r k$ 知 $k>0$. 又 $k \leq x<k+1$, 故

$$
k^{2} \leq x^{2}=r k<k^{2}+2 k+1 \leq k^{2}+3 k .
$$

于是 $k \leq r<k+3$, 即 $r-3<k \leq r$. 至多有 3 个正整数在区间 $(r-3, r]$ 内.

因而 $k$ 至多有 3 个解. 所以原方程至多有 3 个正实根.

设 $k$ 是区间 $[r-2, r]$ 的一个正整数, 这样的 $k$ 至少有 2 个.

注意到

$$
k \leq \sqrt{r k} \leq \sqrt{(k+2) k}<k+1
$$

故

$$
r k=r\lfloor\sqrt{r k}\rfloor .
$$

所以原方程至少有两个正实根:

$$
x=\sqrt{r k}, k \in[r-2, r]
$$

综上所述，命题得证.

评注 本题难度不高, 熟悉函数 $\lfloor x\rfloor$ 的性质进行分类讨论即可得到证明, 用数形结合的方法也可以完成证明。
题 2 对于多项式 $P$ 和正整数 $n$, 记 $P_{n}$ 为使得 $|P(a)|-|P(b)|$ 能被 $n$ 整除的正整数数组 $(a, b)(a<b \leq n)$ 的个数. 求所有的整系数多项式 $P$, 使得对于任意正整数 $n$, 都有 $P_{n} \leq 2021$.

解 假设对于某个整数 $p$, 存在 $a, b \in \mathbb{N}, 0<a<b \leq p$, 使得 $p \mid P(a)-P(b)$,设 $x \geq M, M \in \mathbb{N}$ 时 $P(x)$ 不变号.

任取一个素数 $q>\max \{p, M\}$, 令 $n=p q$, 考虑 $a+i p, b+i p(M \leq i \leq q-1)$这 $2(q-M)$ 个数.

设这些数中满足 $P(x) \equiv l(\bmod q)$ 的元素有 $a_{l}$ 个 $(l=1,2, \cdots, q)$, 则

$$
a_{1}+a_{2}+\cdots+a_{q}=2(q-M) .
$$

于是可以选出 $S=\mathrm{C}_{a_{1}}^{2}+\mathrm{C}_{a_{2}}^{2}+\cdots+\mathrm{C}_{a_{p}}^{2}$ 个数对 $(x, y)$ 使得

$$
P(x) \equiv P(y) \quad(\bmod q) .
$$

注意到 $a_{i} \in \mathbb{N}_{+}, i=1,2, \cdots, q$, 则

$$
\left(a_{i}-1\right)\left(a_{i}-2\right) \geq 0 \Rightarrow a_{i}^{2}-a_{i} \geq 2 a_{i}-2
$$

从而

$$
S=\sum_{i=1}^{q} C_{a_{i}}^{2}=\frac{1}{2} \sum_{i=1}^{q}\left(a_{i}^{2}-a_{i}\right) \geq \frac{1}{2} \sum_{i=1}^{q}\left(2 a_{i}-2\right)=2(q-M)-q=q-2 M \text {. }
$$

考虑到这 $S$ 个数对 $\left(x_{k}, y_{k}\right), x_{k}, y_{k} \geq M, p>M$, 由 $a, b$ 取法知

$$
P\left(x_{k}\right) \equiv P\left(y_{k}\right) \quad(\bmod p)
$$

又

$$
P\left(x_{k}\right) \equiv P\left(y_{k}\right) \quad(\bmod q),
$$

所以

$$
n \mid P\left(x_{k}\right)-P\left(y_{k}\right),
$$

即

$$
n|| P\left(x_{k}\right)|-| P\left(y_{k}\right) \mid,
$$

于是对于充分大的 $q$, 有

$$
S \geq q-2 M>2021
$$

矛盾.

所以假设不成立, 从而对于任意正整数 $p, P(1), P(2), \cdots, P(p)$ 历遍模 $p$的完系.
若存在 $i \in \mathbb{N}_{+}$, 使得

$$
|P(i+1)-P(i)|=m>1
$$

成立.

令 $p=x m$, 设

$$
i \equiv r \quad(\bmod m), 1<r \leq m,\left(m, x, r \in \mathbb{N}_{+}\right)
$$

则

$$
P(i) \equiv P(r) \equiv P(r+m) \equiv \cdots \equiv P(r+(x-1) m) \equiv P(i+1) \quad(\bmod m)
$$

故在 $P(1) \sim P(p)$ 之间必至少有 $x+1$ 个不同的数模 $m$ 同余, 这与 $P(1) \sim P(p)$构成模 $p$ 的完系矛盾.

因此必有

$$
|P(i+1)-P(i)|=1, \forall i \in \mathbb{N}_{+}
$$

当 $x$ 充分大时 $P(x)$ 单调, 必存在常数 $c$ 使得 $P(x)=x+c$ 或 $P(x)=-x+c$对无穷多个 $x$ 都成立.

因而 $P(x)=x+c,(c \geq-2022)$ 或 $P(x)=-x+c,(c \leq 2022)$.

评注 本题有一定难度, 利用反证法结合整系数多项式的性质证明任意正整数 $p, P(1), P(2), \cdots, P(p)$ 历遍模 $p$ 的完系是一个不错的思路, 另外需要注意结果中 $c$ 是有范围的.

题 3 凸四边形 $A B C D$ 内接于圆 $\Gamma$, 点 $E$ 为对角线 $A C, B D$ 的交点. 点 $L$为与边 $A B, B C, C D$ 均相切的圆的圆心, 点 $M$ 为 $\Gamma$ 的弧 $B C$ (不包含点 $A$ 和点 $D)$ 的中点. 证明: $\triangle B C E$ 的 $\angle E$ 内的旁心在直线 $L M$ 上.

注: $\triangle B C E$ 的 $\angle E$ 内的旁心指与线段 $B C$, 射线 $E B$, 射线 $E C$ 均相切的圆的圆心, 而非内切圆圆心.

证明 取 $\triangle A B C$ 的内心 $I_{1}, \triangle D B C$ 的内心 $I_{2}$, 则 $B, I_{1}, L ; C, I_{2}, L$ 分别三点共线.

由内心性质知 $B, I_{1}, I_{2}, C$ 四点共圆且圆心为 $M$.

过 $B, C$ 分别做圆 $M$ 的直径 $B P, C Q$. 连 $L B, L C, I_{1} C, I_{1} P, I_{2} B, I_{2} Q, B I_{E}$, $C I_{E}, L M, L I_{E}$, 则 $\angle I_{2} B I_{E}=\angle I_{1} C I_{E}=90^{\circ}$. 则 $L, M, I_{E}$ 三点共线等价于

$$
\frac{S_{\triangle M B L}}{S_{\triangle M C L}}=\frac{S_{\triangle L B I_{E}}}{S_{\triangle L C I_{E}}}
$$



即证:

$$
\frac{\frac{1}{2} B L \cdot B M \cdot \sin \angle L B M}{\frac{1}{2} C L \cdot C M \cdot \sin \angle L C M}=\frac{\frac{1}{2} B L \cdot B I_{E} \cdot \sin \angle L B I_{E}}{\frac{1}{2} C L \cdot C I_{E} \cdot \sin \angle L C I_{E}}
$$

即证:

$$
\frac{\sin \angle L B M}{\sin \angle L C M}=\frac{B I_{E} \cdot \sin \angle L B I_{E}}{C I_{E} \cdot \sin \angle L C I_{E}}
$$

注意到:

$$
\frac{\sin \angle L B M}{\sin \angle L C M}=\frac{\cos \angle B P I_{1}}{\cos \angle C Q I_{2}}=\frac{\cos \angle B C I_{1}}{\cos \angle C B I_{2}}=\frac{\sin \angle B C I_{E}}{\sin \angle C B I_{E}}=\frac{B I_{E}}{C I_{E}},
$$

且

$$
\frac{\sin \angle L B I_{E}}{\sin \angle L C I_{E}}=\frac{\cos \angle L B I_{2}}{\cos \angle L C I_{1}}=1
$$

故 (1) 成立, 从而 $L, M, I_{E}$ 三点共线得证.

评注 本题是一道难度不高的几何题, 利用同一法证明三点共线的思路很自然.

也可以使用变相同一法, 证明 $\frac{\sin \angle B I_{E} M}{\sin \angle C I_{E} M}=\frac{\sin \angle B I_{E} I}{\sin \angle B I_{E} I}$, 即可得到 $I, M, I_{E}$ 三点共线.

题 4 有一个 $32 \times 32$ 的正方形网格, 开始时,一只老鼠位于左下方的方格中, 且面朝正上方. 选定除左下方的方格以外的若干个方格, 在其中各放置一块奶酪. 接着老鼠重复以下动作, 直到爬出网格外: 一直沿直线前进到放有奶酪的方格中, 吃一口奶酪(并不吃光)后从前进方向开始右转 $90^{\circ}$. 如果老鼠在爬出网格时, 恰好品尝了所有奶酪, 则称这是一种好的放法.

证明: (1) 对于 888 块奶酪, 没有好的放法;

(2) 存在一种好的放法, 可放置 666 块及以上奶酪.
证明 (1) 注意到小老鼠的路径中, 每 4 个右转会出现一个自交, 而每个自交都需要一个空格与之对应, 于是奶酪总数不会超过总格子数的 $\frac{4}{5}$, 而 $32 \times 32 \times \frac{4}{5}=819.2$, 最初的左下角不放奶酪, 所以奶酪总数不会超过 818 块.于是对于 888 块奶酪没有好的放法.

(2) 对于 $2^{n} \times 2^{n},(n$ 为正整数) 的正方形网格中的好放法, 我们对可放置的奶酪数 (记为 $a_{n}$ 进行归纳构造.)

当 $n=1$ 时, $2 \times 2$ 的网格放法如图所示, $a_{1}=3$.



当 $n=2$ 时, 我们将 $4 \times 4$ 的网格分成四个 $2 \times 2$ 的块, 路线图可以视为 4 个 $2 \times 2$ 的网格放法中心对称(当然左下角是小老鼠,没有奶酪).于是 $a_{2}=4 a_{1}-1=11$.


当 $n=3$ 时, 可以给出 $a_{3}=4 a_{2}-1=43$. (见右上图)

类似的, 当 $n=4$ 时, 可以给出 $a_{4}=4 a_{3}-1=171$. 当 $n=5$ 时, 可以给出 $a_{5}=4 a_{4}-1=683>666$

于是 (2) 得证.

评注 本题是一道有趣的组合题, 利用递推的构造想法清晰明了. 值得一提的是, 最初的翻译有一处错误, 将“吃一口”改为了“吃掉”, 这会导致曾经放奶酪的位置可以重复穿过, 奶酪总数会增加一些, 有学生给出了 700 多块的构造(含有不少重复穿过的结构), 有兴趣的读者可以研究一下.
题 5 求所有定义域和值域均为整数的函数 $f$, 使得: 对于任意的整数 $a, b$,

$$
f(f(a)-b)+b f(2 a)
$$

均为完全平方数.

解 我们先给出一个引理.

引理 对一个给定的整数 $T$, 若存在一个充分大的整数 $M$ 使得 $M$ 与 $T+M$均为完全平方数, 则 $T=0$.

证明 假设 $T \neq 0$, 设 $M=k^{2}, k \in \mathbb{Z}$, 则 $M+T \geq(k+1)^{2}$ 和 $M+T \leq(k-1)^{2}$必有一个成立. 即

$$
T \geq 2 \sqrt{M}+1 \text { 或 } T \leq 1-2 \sqrt{M} \text {. }
$$

这在 $M$ 充分大时均不可能成立. 故引理得证.

回到原题. 记 $S$ 为所有完全平方数构成的集合.

在 $f(f(a)-b)+b f(2 a)$ 中作代换 $b \rightarrow f(a)-b$. 得

$$
f(b)+(f(a)-b) f(2 a) \in S
$$

在 $(*)$ 式中令 $a=b=0$ 得

$$
f^{2}(0)+f(0) \in S \Rightarrow f(0)=0 \text { 或 }-1
$$

若 $f(0)=-1$, 记 $x=f(-1), y=f(-2)$, 在 $(*)$ 式中令

$$
a=0, b=-1 \Rightarrow x \in S
$$

令

$$
a=0, b=-2 \Rightarrow y-1 \in S
$$

令

$$
a=-1, b=-1 \Rightarrow x y+x+y \in S
$$

令

$$
a=-1, b=-2 \Rightarrow(x+3) y \in S
$$

令

$$
a=-1, b=0 \Rightarrow x y-1 \in S
$$

由 (1) (2) 知

$$
x \equiv 0,1 \quad(\bmod 4), y \equiv 1,2 \quad(\bmod 4)
$$

结合 (3) (5) 知仅可能为

$$
x \equiv 1 \quad(\bmod 4), y \equiv 2 \quad(\bmod 4)
$$

在 (4) 中由于 $x \in S, x \equiv 1(\bmod 8) \Rightarrow 2^{2}\|x+3,2\| y$, 矛盾.

故 $f(0)=0$.

在 $(*)$ 式中令 $a=0$ 得 $f(b) \in S, \forall b \in \mathbb{Z}$, 且 $f(b) \geq 0$.

如果 $\forall a \in \mathbb{Z}, f(2 a)=0$, 则可得

$$
f(x)=\left\{\begin{array}{ll}
0, & x \text { 是偶数 } \\
P_{x}^{2}, & x \text { 是奇数 }
\end{array}\left(P_{x} \in \mathbb{Z}\right)\right.
$$

下面假设存在 $u \in \mathbb{Z}$, 使得 $f(2 u) \neq 0$.

若还存在一个 $v \in \mathbb{Z}$ 满足 $v \neq 0, f(2 v)=0$.

在 $(*)$ 式中令 $a=u, b=2 v$ 得

$$
(f(u)-2 v) f(2 u) \in S
$$

又 $f(2 u) \in S$, 故

$$
f(u)-2 v \in S, \Rightarrow f(u)-2 v \geq 0 \Rightarrow v \leq \frac{1}{2} f(u)
$$

于是这样的 $v$ 是有上界的, 那么必存在充分大的 $w$ 使得 $f(2 w) \neq 0$.

把 $u$ 换为 $w$ 同理有 $f(w)-2 v \in S$.

在 $(*)$ 式中令 $a=u, b=w$ 得

$$
(f(u)-w) f(2 u)+f(w) \in S
$$

于是

$$
\begin{aligned}
& (f(u)-w) f(2 u)+f(w) \geq 0 \\
& \Rightarrow f(w) \geq f(2 u)(w-f(u)) \\
& \Rightarrow f(w) \text { 也充分大. }
\end{aligned}
$$

由引理知 $v=0$. 矛盾.

因此 $f(2 a) \neq 0$ 对任意 $a \neq 0$ 成立.

在 $(*)$ 式中令 $b=2 a$ 得

$$
(f(a)-2 a+1) f(2 a) \in S
$$

又 $f(2 a) \in S$, 取 $a \neq 0$, 则

$$
f(a)-2 a+1 \in S .(\forall a \neq 0)
$$

考虑奇素数 $p$, 设

$$
f\left(\frac{p+1}{2}\right)=m^{2} \in S, f\left(\frac{p+1}{2}\right)-2 \cdot \frac{p+1}{2}+1 \in S,
$$

即

$$
f\left(\frac{p+1}{2}\right)-p=n^{2} \in S,(m, n \in \mathbb{Z})
$$

于是

$$
p=m^{2}-n^{2}=(m+n)(m-n)
$$

则

$$
\begin{aligned}
m+n & =p, m-n=1 \\
\Rightarrow m=\frac{p+1}{2} \Rightarrow f\left(\frac{p+1}{2}\right) & =\left(\frac{p+1}{2}\right)^{2} \cdot(\text { 其中 } p \text { 为任意奇素数 })
\end{aligned}
$$

故存在充分大的 $x \in \mathbb{Z}$ 使得 $f(x)=x^{2}$.

在 $(*)$ 式中令 $b$ 为这样的一个 $x$, 得

$$
\begin{gathered}
(f(a)-x) f(2 a)+x^{2} \in S . \\
\Rightarrow(2 x-f(2 a))^{2}+4 f^{2}(a)-f^{2}(2 a) \in S
\end{gathered}
$$

由于 $x$ 充分大, 利用引理可知

$$
4 f^{2}(a)-f^{2}(2 a)=0,
$$

即

$$
f(2 a)=2 f(a), \forall a \in \mathbb{Z}
$$

在 $(*)$ 式中令 $a=x$ 得

$$
\begin{aligned}
& \left(x^{2}-b\right) \cdot 4 x^{2}+f(b) \in S . \\
\Rightarrow & \left(2 x^{2}-b\right)^{2}+f(b)-b^{2} \in S
\end{aligned}
$$

由于 $x$ 充分大, 利用引理可知 $f(b)-b^{2}=0$, 即

$$
f(b)=b^{2}, \forall b \in \mathbb{Z}
$$

评注 本题是一道中等难度的数论问题, 解决起来较为繁琐但是思维难度并不算高, 反复使用引理并将分类讨论细节处理到位即可完成解答.

