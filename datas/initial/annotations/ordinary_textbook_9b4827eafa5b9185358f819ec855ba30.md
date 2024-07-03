# 第 31 届 CMO 试题评析 

张盛桐 黄小雨

(上海市上海中学, 200231)

指导教师: 王广廷

第 31 届中国数学奥林匹克 (全国中学生数学冬令营) 于 2015 年 12 月 14 日至 18 日在江西省鹰潭市举行. 作为参赛者之一, 我们觉得此次冬令营试题难度很大, 极具挑战性. 下面我们给出各题的解答和评注, 供大家参考.

题 1. 设正整数 $a_{1}, a_{2}, \cdots, a_{31} ; b_{1}, b_{2}, \cdots, b_{31}$ 满足:

(i) $a_{1}<a_{2}<\cdots<a_{31} \leq 2015, b_{1}<b_{2}<\cdots<b_{31} \leq 2015$;

(ii) $a_{1}+a_{2}+\cdots+a_{31}=b_{1}+b_{2}+\cdots+b_{31}$.

求 $S=\left|a_{1}-b_{1}\right|+\left|a_{2}-b_{2}\right|+\cdots+\left|a_{31}-b_{31}\right|$ 的最大值.

解 令 $a_{i}^{\prime}=a_{i}-i+1, b_{i}^{\prime}=b_{i}-i+1$, 则由 $\mathbb{Z}$ 的离散性知

$$
\begin{aligned}
& 1 \leq a_{1}^{\prime} \leq a_{2}^{\prime} \leq \cdots \leq a_{31}^{\prime} \leq 1985 \\
& 1 \leq b_{1}^{\prime} \leq b_{2}^{\prime} \leq \cdots \leq b_{31}^{\prime} \leq 1985
\end{aligned}
$$

且

$$
\begin{gathered}
a_{1}^{\prime}+a_{2}^{\prime}+\cdots+a_{31}^{\prime}=b_{1}^{\prime}+b_{2}^{\prime}+\cdots+b_{31}^{\prime} \\
S^{\prime}=\sum_{i=1}^{31}\left|a_{i}^{\prime}-b_{i}^{\prime}\right|=\sum_{i=1}^{31}\left|a_{i}-b_{i}\right|=S
\end{gathered}
$$

故只需求 $S^{\prime}$ 的最大值. 记

$$
\begin{aligned}
& S_{1}=\left\{i \mid a_{i}^{\prime} \geq b_{i}^{\prime}, 1 \leq i \leq 31\right\} \\
& S_{2}=\left\{i \mid a_{i}^{\prime}<b_{i}^{\prime}, 1 \leq i \leq 31\right\}
\end{aligned}
$$

则

$$
\left|S_{1}\right|+\left|S_{2}\right|=31
$$

下证一个关键性的引理.

引理. 对任意的 $i \in S_{1}, j \in S_{2}$,

$$
\left|a_{i}^{\prime}-b_{i}^{\prime}\right|+\left|a_{j}^{\prime}-b_{j}^{\prime}\right| \leq 1984 .
$$

事实上, 对任意的 $i \in S_{1}, j \in S_{2}$,

$$
\begin{aligned}
\left|a_{i}^{\prime}-b_{i}^{\prime}\right|+\left|a_{j}^{\prime}-b_{j}^{\prime}\right| & =\left|a_{i}^{\prime}-b_{i}^{\prime}+b_{j}^{\prime}-a_{j}^{\prime}\right| \\
& =\left|\left(a_{i}^{\prime}-a_{j}^{\prime}\right)+\left(b_{j}^{\prime}-b_{i}^{\prime}\right)\right| .
\end{aligned}
$$

由 (1) 知 $a_{i}^{\prime}-a_{j}^{\prime}$ 与 $b_{j}^{\prime}-b_{i}^{\prime}$ 异号, 故

$$
\left|a_{i}^{\prime}-b_{i}^{\prime}\right|+\left|a_{j}^{\prime}-b_{j}^{\prime}\right| \leq \max \left(\left|a_{i}^{\prime}-a_{j}^{\prime}\right|,\left|b_{j}^{\prime}-b_{i}^{\prime}\right|\right) \leq 1984,
$$

引理得证.

回到原题. 由 $(2)$ 得,

$$
\sum_{i \in S_{1}}\left|a_{i}^{\prime}-b_{i}^{\prime}\right|=\sum_{i \in S_{2}}\left|a_{i}^{\prime}-b_{i}^{\prime}\right|
$$

由 $(3),(4)$ 及引理, 得

$$
\begin{aligned}
\sum_{i=1}^{31}\left|a_{i}^{\prime}-b_{i}^{\prime}\right| & =\sum_{i \in S_{1}}\left|a_{i}^{\prime}-b_{i}^{\prime}\right|+\sum_{i \in S_{2}}\left|a_{i}^{\prime}-b_{i}^{\prime}\right| \\
& =\frac{2}{31}\left(\left|S_{2}\right| \sum_{i \in S_{1}}\left|a_{i}^{\prime}-b_{i}^{\prime}\right|+\left|S_{1}\right| \sum_{i \in S_{2}}\left|a_{i}^{\prime}-b_{i}^{\prime}\right|\right) \\
& =\frac{2}{31} \sum_{i \in S_{1}, j \in S_{2}}\left(\left|a_{i}^{\prime}-b_{i}^{\prime}\right|+\left|a_{j}^{\prime}-b_{j}^{\prime}\right|\right) \\
& \leq \frac{2}{31} \sum_{i \in S_{1}, j \in S_{2}} 1984=\frac{2}{31} \cdot\left|S_{1}\right| \cdot\left|S_{2}\right| \cdot 1984 \\
& =128 \cdot\left|S_{1}\right| \cdot\left(31-\left|S_{1}\right|\right) \\
& \leq 128 \cdot 15 \cdot 16=30720 .
\end{aligned}
$$

当

$$
a_{1}^{\prime}=\cdots=a_{16}^{\prime}=1, a_{17}^{\prime}=\cdots=a_{31}^{\prime}=1985, b_{1}^{\prime}=b_{2}^{\prime}=\cdots=b_{31}^{\prime}=961,
$$

即

$$
\begin{aligned}
& \left(a_{1}, a_{2}, \cdots, a_{16}, a_{17}, a_{18}, \cdots, a_{31}\right)=(1,2, \cdots, 16,2001,2002, \cdots, 2015) \\
& \left(b_{1}, b_{2}, \cdots, b_{31}\right)=(961,962, \cdots, 991)
\end{aligned}
$$

时，上式等号成立. 故 $S$ 的最大值为 30720 .

评注 这是一个离散最值问题, 是一个要有组合想法的代数问题. 为了看出什么时候取最大值, 我们需要对 $a_{i}$ 和 $b_{i}$ 作平移变换, 平移 $i-1$ 个单位, 分别得到 $a_{i}^{\prime}$和 $b_{i}^{\prime}$, 这时条件 (i) 中严格单调就变为上述 (1) 式. 因此可猜测最大值在一组变量 $a_{i}^{\prime}$ 有接近一半取 1 , 接近一半取 1985 , 而另一组变量 $b_{i}^{\prime}$ 均相等时取得. 证明的一个关键点是发现使得 $a_{i}^{\prime} \geq b_{i}^{\prime}$ 中的 $\left|a_{i}^{\prime}-b_{i}^{\prime}\right|$ 与使得 $a_{j}^{\prime}>b_{j}^{\prime}$ 中的 $\left|a_{j}^{\prime}-b_{j}^{\prime}\right|$ 的这两个
差的和不大于 1984 (即引理). 这个引理似乎是避不开的, 这也是此题思路较为单一, 从而导致难度较高的原因, 可以说这是 CMO 史上最难的第一题.

题 2. 如图, 凸四边形 $A B C D$ 中, $K, L, M, N$ 分别是边 $A B, B C, C D, D A$ 上的点, 满足

$$
\frac{A K}{K B}=\frac{D A}{B C}, \frac{B L}{L C}=\frac{A B}{C D}, \frac{C M}{M D}=\frac{B C}{D A}, \frac{D N}{N A}=\frac{C D}{A B}
$$

延长 $A B, D C$ 交于点 $E$, 延长 $A D, B C$ 交于点 $F$. 设 $\triangle A E F$ 的内切圆在边 $A E, A F$ 上的切点分别为 $S, T ; \triangle C E F$ 的内切圆在边 $C E, C F$ 上的切点分别为 $U, V$. 证明: 若 $K, L, M, N$ 四点共圆, 则 $S, T, U, V$ 四点共圆.
![](https://cdn.mathpix.com/cropped/2024_02_26_4e87afb549d1562e69ccg-03.jpg?height=366&width=1168&top_left_y=936&top_left_x=450)

证明 由 $\frac{A K}{K B}=\frac{D A}{B C}, \frac{D N}{N A}=\frac{C D}{A B}$, 得

$$
A K=\frac{A B \cdot A D}{A D+B C}, \quad A N=\frac{A B \cdot A D}{A B+C D}
$$

当 $A B+C D>A D+B C$ 时, $A N<A K$. 同理 $B L<B K, C L<C M, D N<D M$.故 $\angle A K N<\angle A N K, \angle B K L<\angle B L K, \angle C M L<\angle C L M, \angle D M N<\angle D N M$.从而

$$
\begin{aligned}
& \angle A K N<\frac{\pi-\angle D A B}{2}, \angle B K L<\frac{\pi-\angle A B C}{2}, \\
& \angle C M L<\frac{\pi-\angle B C D}{2}, \angle D M N<\frac{\pi-\angle A D C}{2},
\end{aligned}
$$

因此

$$
\angle A K N+\angle B K L+\angle C M L+\angle D M N<\pi,
$$

故 $\angle N K L+\angle N M L>\pi$, 这与 $K, L, M, N$ 共圆矛盾.

因此 $A B+C D>A D+B C$ 不成立, 同理 $A B+C D<A D+B C$ 也不可能. 所以 $A B+C D=A D+B C$, 故 $A B C D$ 有内切圆 $\omega$, 设其分别切 $A B, B C, C D, D A$于 $W, X, Y, Z$ 点.

因为 $\omega$ 为 $\triangle A D E$ 的内切圆, $\triangle F C D$ 的外切圆, 所以

$$
E Y=\frac{E D+E C-D C}{2}, C Y=\frac{C D+F D-F C}{2},
$$

于是 $2 C E+C D+F D-F C=A E+E D-A D$, 消项整理得 $A F-C F=A E-C E$.

因为 $S, U$ 分别为 $\triangle A E F$ 和 $\triangle C E F$ 与其内切圆的切点, 故

$$
E S=\frac{A E+E F-A F}{2}, E U=\frac{C E+E F-C F}{2}
$$

从而 $E S=E U$.

同理 $F V=F T, A T=A S, C U=C V$. 因此

$$
\begin{aligned}
\angle S U V=\angle S U C+\angle C U V & =\frac{\pi}{2}+\frac{\angle A E C}{2}+\frac{\angle B C E}{2} \\
& =\frac{\pi}{2}+\frac{\angle A B C}{2},
\end{aligned}
$$

同样, 我们可以得到

$$
\begin{aligned}
\angle S T V & =\angle S T F-\angle V T F \\
& =\pi-\frac{\pi-\angle D A B}{2}-\frac{\pi-\angle A F B}{2} \\
& =\frac{1}{2}(\angle D A B+\angle A F B)=\frac{1}{2} \angle F B E .
\end{aligned}
$$

故

$$
\angle S U V+\angle S T V=\frac{\pi}{2}+\frac{\angle A B C}{2}+\frac{\angle F B E}{2}=\pi .
$$

所以 $S, T, U, V$ 四点共圆. 证毕.

评注 本题可分解为两道几何题, 中间用 $A B C D$ 有内切圆这一结论来过渡.这一题的前半部分不是很难, 结合四边形有内切圆判定条件, 用反证法即可得证,属于一个熟知的结论. 后半部分略有难度, 关键是发现四个角上的小三角形为等腰三角形, 而这一点要结合切线的性质, 严谨推导. 值得一提的是, 有些同学在得出两组对边和相同后, 直接写了图中四个点为内切圆切点, 然而仔细思考后会发现这四个点不一定为切点. 总的来说, 今年第二题是一道中等难度的几何题.

题 3. 设 $p$ 是奇素数, $a_{1}, a_{2}, \cdots, a_{p}$ 是整数, 证明以下两个命题等价:

(I) 存在一个次数不超过 $\frac{p-1}{2}$ 的整系数多项式 $f(x)$, 使得对每个不超过 $p$ 的正整数 $i$, 都有 $f(i) \equiv a_{i}(\bmod p)$.

(II) 对每个不超过 $\frac{p-1}{2}$ 的正整数 $d$, 都有

$$
\sum_{i=1}^{p}\left(a_{i+d}-a_{i}\right)^{2} \equiv 0 \quad(\bmod p)
$$

这里下标按模 $p$ 理解, 即 $a_{p+n}=a_{n}$.

证明 我们首先证明下面的引理.
引理. 对素数 $p \geq 3,0 \leq n<p-1, n \in \mathbb{N}^{+}$, 有 $p \mid \sum_{i=1}^{p} i^{n}$.

引理证明 当 $n=0$ 时, $\sum_{i=1}^{p} i^{n} \equiv p \equiv 0(\bmod p)$, 结论成立.

下面考虑 $1 \leq n<p-1$ 的情况. 由于 $p \mid p^{n}$, 因此只要证 $p \mid \sum_{i=1}^{p-1} i^{n}$. 由模素数的原根存在性, 设 $g$ 为模 $p$ 的原根 $\left(g \in \mathbb{N}^{*}\right)$, 则在模 $p$ 意义下,

$$
g^{0}, g^{1}, \cdots, g^{p-2} \text { 为 } 1,2, \cdots, p-1 \text { 的排列. }
$$

故只要证明 $p \mid \sum_{i=0}^{p-2} g^{i n}$.

设 $d=(n, p-1)$, 由 $n<p-1$ 知, $d<p-1$. 又 $g^{p-1} \equiv 1(\bmod p)$, 对任意 $0 \leq i \leq p-2, i n$ 模 $p-1$ 的余数中, $0, d, 2 d, \cdots,(p-1) d$ 各出现 $d$ 次. 所以只需证明

$$
p \left\lvert\, d \cdot \sum_{i=0}^{\frac{p-1}{d}-1} g^{i d}\right.
$$

由 $(*)$ 且 $p \left\lvert\, 1+2+\cdots+(p-1)=\frac{p(p-1)}{2}\right.$, 得

$$
p \left\lvert\, \sum_{i=0}^{p-2} g^{i}=\left(\sum_{i=0}^{d-1} g^{i}\right) \cdot\left(\sum_{i=0}^{\frac{p-1}{d}-1} g^{i d}\right)=\frac{g^{d}-1}{g-1} \cdot \sum_{i=0}^{\frac{p-1}{d}-1} g^{i d}\right.
$$

由于 $g$ 为原根, 而 $d<p-1$, 因此 $p \nmid g^{d}-1$, 故

$$
p \left\lvert\, \sum_{i=0}^{\frac{p-1}{d}-1} g^{i d}\right.
$$

从而 (1) 成立, 引理得证.

回到原题.

先证 (I) $\Rightarrow$ (II).

设 $f(x)=c_{k} x^{k}+c_{k-1} x^{k-1}+\cdots+c_{0}$, 其中 $c_{i} \in \mathbb{Z}, 0 \leq i \leq k, c_{k} \neq 0, k \leq \frac{p-1}{2}$,则对 $1 \leq d \leq \frac{p-1}{2}$,

$$
a_{i+d}-a_{i} \equiv f(i+d)-f(i) \quad(\bmod p) .
$$

而

$$
\begin{aligned}
f(x+d)-f(x) & =\sum_{i=1}^{k} c_{i}\left((x+d)^{i}-x^{i}\right) \\
& =d \cdot\left(\sum_{i=1}^{k} c_{i}\left((x+d)^{i-1}+(x+d)^{i-2} x+\cdots+x^{i-1}\right)\right)
\end{aligned}
$$

所以 $f(x+d)-f(x)$ 为关于 $x$ 的不大于 $\frac{p-3}{2}$ 次整系数多项式, 从而 $(f(x+d)-f(x))^{2}$为关于 $x$ 的不大于 $p-3$ 次整系数多项式. 设其为 $g(x)=b_{l} x^{l}+\cdots+b_{0}\left(b_{i} \in\right.$ $\left.\mathbb{Z}, 0 \leq i \leq l, b_{l} \neq 0, l \leq p-3\right)$, 从而由引理, 得

$$
\sum_{i=1}^{p}\left(a_{i+d}-a_{i}\right)^{2} \equiv \sum_{i=1}^{p} g(i)=\sum_{i=1}^{p} \sum_{j=0}^{l} b_{j} i^{j}=\sum_{j=0}^{l} b_{j} \sum_{i=1}^{p} i^{j} \equiv \sum_{j=0}^{l} 0 \equiv 0 \quad(\bmod p) .
$$

故 $(\mathrm{I}) \Rightarrow(\mathrm{II})$ 证毕.

下证 (II) $\Rightarrow$ (I).

记 $F$ 是次数不大于 $p-1$, 且每项系数都属于 $\{0,1,2, \cdots, p-1\}$ 的整系数多项式 $f(x)$ 的集合, $G=\left\{\left(n_{1}, n_{2}, \cdots, n_{p}\right) \mid\right.$ 对于 $\left.1 \leq i \leq p, n_{i} \in\{0,1,2, \cdots, p-1\}\right\}$.由于将 $f(x)$ 的系数及 $a_{i}$ 在模 $p$ 同余下任意替换不影响命题, 因此只考虑 $f(x) \in F,\left(a_{1}, a_{2}, \cdots, a_{p}\right) \in G$ 的情况.

构造映射 $\Delta: F \rightarrow G$ 如下: 对 $f \in F$,

$$
\Delta(f)=\left(n_{1}, n_{2}, \cdots, n_{p}\right)
$$

且对 $1 \leq i \leq p, f(i) \equiv n_{i}(\bmod p)$.

若存在 $f \neq g \in F$ 使得 $\Delta(f)=\Delta(g)$. 则在模 $p$ 下, $1,2, \cdots, p$ 均为 $f(x)-g(x)$的根. 又 $f(x)-g(x)$ 不会是零多项式, 由 Lagrange 定理得 $\operatorname{deg}(f-g) \geq p$, 而 $\operatorname{deg} f, \operatorname{deg} g \leq p-1$, 则 $\operatorname{deg}(f-g) \leq p-1$, 矛盾. 所以 $\Delta$ 为单射, 又 $|F|=p^{p}=|G|$,因而 $\Delta$ 为双射.

由 $(\mathrm{I}) \Rightarrow(\mathrm{II})$ 知, 要证 $(\mathrm{II}) \Rightarrow(\mathrm{I})$, 只要证明: 对 $F$ 中大于 $\frac{p-1}{2}$ 次的 $f, \Delta(f)=$ $\left(n_{1}, n_{2}, \cdots, n_{p}\right)$, 存在 $1 \leq d \leq \frac{p-1}{2}$, 使得

$$
\sum_{i=1}^{p}\left(n_{i+d}-n_{i}\right)^{2} \not \equiv 0 \quad(\bmod p)
$$

即存在 $1 \leq d \leq \frac{p-1}{2}$ 使得

$$
\sum_{i=1}^{p}(f(i+d)-f(i))^{2} \not \equiv 0 \quad(\bmod p)
$$

设 $f(x)=d_{k} x^{k}+\cdots+d_{0}$, 其中 $d_{i} \in \mathbb{Z}, 0 \leq i \leq k, d_{k} \neq 0, \frac{p+1}{2} \leq k \leq p-1$,则

$$
\begin{aligned}
(f(x+d)-f(x))^{2} & =d^{2} \cdot\left(\sum_{i=0}^{k} d_{i}\left((x+d)^{i-1}+(x+d)^{i-2} x+\cdots+x^{i-1}\right)\right)^{2} \\
& =d^{2} \cdot\left(\sum_{i=0}^{k} d_{i}\left(c_{i}^{1} x^{i-1}+c_{i}^{2} x^{i-2} d+c_{i}^{3} x^{i-3} d^{2}+\cdots+c_{i}^{i} d^{i-1}\right)\right)^{2}
\end{aligned}
$$

展开式为关于 $x$ 的 $2 k-2$ 次式, 其中每项的系数均为关于 $d$ 的整系数多项式.

设 $x^{p-1}$ 的系数为 $h(d), h(d) \in \mathbb{Z}[x]$, 由引理, 对 $0 \leq n<p-1$, 有 $p \mid \sum_{i=1}^{p} i^{n}$.
而由 Fermat 小定理, 当 $n=p-1$ 时,

当 $p-1<n<2(p-1)$ 时,

$$
\sum_{i=1}^{p} i^{n} \equiv p-1 \quad(\bmod p)
$$

$$
\sum_{i=1}^{p} i^{n} \equiv \sum_{i=1}^{p} i^{n-(p-1)} \equiv 0 \quad(\bmod p)
$$

又 $p-1 \leq 2 k-2 \leq 2 p-4$, 故

$$
\sum_{i=1}^{p}\left(n_{i+d}-n_{i}\right)^{2} \equiv \sum_{i=1}^{p}(f(i+d)-f(i))^{2} \equiv h(d)(p-1) \quad(\bmod p) .
$$

注意到 (2) 式与 $d_{i}$ 相乘的括号内, 每一项 $d$ 与 $x$ 次数和固定为 $i-1$. 因此 $h(d)$ 最高次项为由 $d_{k}$ 对应括号内项的积产生, 故 $h(d)$ 最高次项系数为

$$
d^{2} d_{k}^{2}\left(c_{k}^{1} c_{k}^{2 k-p}+c_{k}^{2} c_{k}^{2 k-p-1}+\cdots+c_{k}^{2 k-p} c_{k}^{1}\right)=d^{2} d_{k}^{2}\left(c_{2 k}^{2 k-p+1}-2 c_{k}^{2 k-p+1}\right)
$$

最高次项为 $2 k-p-1$ 次.

由 $\frac{p+1}{2} \leq k \leq p-1$, 得 $p \nmid 2 k-p+1, p \nmid c_{k}^{2 k-p+1}$. 故在 $p$ 进制下 $2 k-p+1$与 $p-1$ 相加会进位, 由 Kummer 定理, $p \nmid c_{2 k}^{2 k-p+1}$, 则

$$
p \nmid d^{2} d_{k}^{2}\left(c_{2 k}^{2 k-p+1}-2 c_{k}^{2 k-p+1}\right),
$$

即 $h(d)$ 在模 $p$ 下次数为 $2 k-p-1$ 次且不为零多项式. 而 $0 \leq 2 k-p-1 \leq p-3$,从而存在 $1 \leq d \leq p-1$, 使得 $h(d) \not \equiv 0(\bmod p)$, 不然, 由 Lagrange 定理, $2 k-p-1 \geq p-1$, 矛盾. 故由 (3) 得

$$
\sum_{i=1}^{p}\left(n_{i+d}-n_{i}\right)^{2} \not \equiv 0 \quad(\bmod p)
$$

若 $1 \leq d \leq \frac{p-1}{2},(* *)$ 已得证.

若 $\frac{p-1}{2} \leq d \leq p-1$, 考虑 $d^{\prime}=p-d$, 则 $1 \leq d^{\prime} \leq \frac{p-1}{2}$,

$$
\begin{aligned}
\sum_{i=1}^{p}\left(n_{i+d^{\prime}}-n_{i}\right)^{2} & \equiv \sum_{i=1}^{p}\left(n_{i}-n_{i+d^{\prime}}\right)^{2} \equiv \sum_{i=1}^{p}\left(n_{i+p}-n_{i+d^{\prime}}\right)^{2} \\
& \equiv \sum_{i=1}^{p}\left(n_{i+d^{\prime}+\left(p-d^{\prime}\right)}-n_{i+d^{\prime}}\right)^{2} \\
& \equiv \sum_{i=1}^{p}\left(n_{i+d}-n_{i}\right)^{2} \neq 0 \quad(\bmod p)
\end{aligned}
$$

所以 $p \nmid \sum_{i=1}^{p}\left(n_{i+d^{\prime}}-n_{i}\right)^{2},(* *)$ 也得证.

综上, (II) $\Rightarrow$ (I) 成立. 故 (I) $\Leftrightarrow$ (II).

评注 作为冬令营第三题, 本题难度非常大, 直逼集训队考试的难度. (I) 推

(II) 难度不大, 只要用到多项式差分后, 再用一个素数的小结论, 熟悉数论的同学可以很快做出这一部分. 而 (II) 推 (I) 的难度相当的大. 首先注意到模 $p$ 意义下不大于 $p-1$ 的多项式在 $1,2, \cdots, p$ 上取值模 $p$ 的余数两两不同, 其中要用到拉格朗日定理; 然后发现所构造集合元素个数各 $p^{p}$ 个, 可形成双射, 从而将其转化为大于 $\frac{p-1}{2}$ 次的多项式不满足 (II), 之后只要将多项式的差分式的平方展开后分析 $x^{p-1}$ 次项的系数, 将其看作一个 $d$ 的多项式并要证明可取一个使之不为 $p$ 的倍数, 然后用 (I) 推 (II) 用到的数论结论即可. 这道题的过程可谓是极其繁琐, 难度也很大, 在写的时候也要极其小心, 注意多项式与同余中的各项细节.

题 4. 设整数 $n \geq 3$, 不超过 $n$ 的素数共有 $k$ 个, 且 $A$ 是集合 $\{2,3, \cdots, n\}$ 的子集, $A$ 的元素个数小于 $k$, 且 $A$ 中任意一个数不是另一个数的倍数. 证明: 存在集合 $\{2,3, \cdots, n\}$ 的 $k$ 元子集 $B$, 使得 $B$ 中任意一个数也不是另一个数的倍数,且 $B$ 包含 $A$.

证明 将集合 $\{2,3, \cdots, n\}$ 中的素数记为 $p_{1}, p_{2}, \cdots, p_{k}$, 令 $z_{i}=\left[\log _{p_{i}} n\right]$, 则 $p_{i}^{z_{i}} \leq n<p_{i}^{z_{i}+1}, i=1,2, \cdots, k$.

设 $|A|=s, s<k$. 对于任意 $a \in A$, 称 $a$ 占领 $p_{i}$, 若 $a$ 与 $p_{i}^{z_{i}}$ 有倍数关系, 即满足 (i) $a \mid p_{i}^{z_{i}}$, 或者 (ii) $p_{i}^{z_{i}} \mid a$.

若对任意 $a \in A$, 存在 $p_{i}$ 满足条件 (i), 则 $a$ 为 $p_{i}$ 的方幂, 从而 $a$ 只占领 $p_{i}$.

另一方面, 若 $a$ 由条件 (ii) 占领了两个素数 $p<q$, 则 $q\left|a, p^{\alpha}\right| a, \alpha=\left[\log _{p} n\right]$.从而 $a \geq p^{\alpha} q \geq p^{\alpha+1}>n$, 矛盾. 因此 $a$ 只占领一个素数 $p$.

故对任意 $a \in A, a$ 至多只占领一个素数, 从而 $A$ 至多占领素数 $p_{1}, p_{2}, \cdots, p_{k}$中的 $s$ 个. 所以至少有 $k-s$ 个素数未被占领, 设其为 $q_{1}, q_{2}, \cdots, q_{k-s}$, 记 $\alpha_{i}=$ $\left[\log _{q_{i}} n\right], i=1,2, \cdots, k$. 令

$$
B=A \cup\left\{q_{1}^{\alpha_{1}}, q_{2}^{\alpha_{2}}, \cdots, q_{k-s}^{\alpha_{k-s}}\right\}
$$

由占领定义知 $B$ 中元素两两之间无倍数关系, 且 $|B|=k$, 故 $B$ 满足要求.

评注 这是一个难度适中的第 4 题, 这题在题干中就已经指明了解题方向. 设出了素数有 $k$ 个就提示要从素数考虑, 而 “非倍数” 则提示我们添加最 “难以”满足倍数关系的数, 结合两点就不难想到取素数最高幂, 这就解决了问题.

题 5. 在平面中, 对任意给定的凸四边形 $A B C D$, 证明: 存在正方形 $A^{\prime} B^{\prime} C^{\prime} D^{\prime}$ (其顶点可以按顺时针或逆时针标记), 使得 $A^{\prime} \neq A, B^{\prime} \neq B, C^{\prime} \neq C, D^{\prime} \neq D$, 且直线 $A A^{\prime}, B B^{\prime}, C C^{\prime}, D D^{\prime}$ 经过同一个圆.
证明 (i) $A B C D$ 为矩形, 按逆时针标记. 以 $A$ 为顶点, 以 $B A, D A$ 延长线为边向外任作正方形 $A^{\prime} B^{\prime} C^{\prime} D^{\prime}$, 令 $C^{\prime}=A$, 按顺时针标记. 从而 $A A^{\prime}, B B^{\prime}, C C^{\prime}, D D^{\prime}$过 $A$, 且 $A^{\prime} \neq A, B^{\prime} \neq B, C^{\prime} \neq C, D^{\prime} \neq D$.

(ii) $A B C D$ 不为矩形. 因为内角和为 $360^{\circ}$, 所以四个内角中至少有一个锐角,不妨设 $\angle B A D<90^{\circ}$. 任取 $A C$ 上一点 $C^{\prime}$, 以 $C^{\prime}$ 为顶点作直角, 保证其两边分别与 $A B, C D$ 交于点 $B^{\prime}, D^{\prime}$.

将直角 $\angle B^{\prime} C^{\prime} D^{\prime}$ 以 $C^{\prime}$ 为中心旋转, 当接近 $C^{\prime} D^{\prime} / / A D$ 时, $C^{\prime} D^{\prime} \rightarrow+\infty$, 而此时 $\angle A C^{\prime} B^{\prime}=90^{\circ}+\angle D A C<180^{\circ}-\angle C A B$. 所以另一边 $C^{\prime} B^{\prime}$ 始终与 $A B$ 相交, 则此时 $C^{\prime} B^{\prime}$ 趋向一个有限值, 所以 $C^{\prime} D^{\prime}-C^{\prime} B^{\prime} \rightarrow+\infty$.

同理, 当接近 $C^{\prime} B^{\prime} / / A B$ 时, $C^{\prime} D^{\prime}-C^{\prime} B^{\prime} \rightarrow-\infty$. 因此由介值原理, 存在直角 $\angle B_{0} C^{\prime} D_{0}$, 使 $B_{0} C^{\prime}-D_{0} C^{\prime}=0$. 从而以 $B_{0} C^{\prime}, D_{0} C^{\prime}$ 为边可作正方形 $A^{\prime} B_{0} C^{\prime} D_{0}$,且 $A A^{\prime}, B_{0} B, C C^{\prime}, D_{0} D$ 均过 $A$.

通过以 $A$ 为中心的位似, 易使 $B_{0} \neq B, C \neq C^{\prime}, D_{0} \neq D$ (因为至多三个 $C^{\prime}$ 使这个不成立). 而 $\angle B_{0} A^{\prime} D_{0}=90^{\circ}, \angle B_{0} A D_{0}=\angle B A D<90^{\circ}$, 所以 $A^{\prime} \neq A$. 故肯定存在符合要求的 $A_{0} B^{\prime} C_{0} D^{\prime}$.

评注 第五题实质上是一个几何作图问题. 入手点是清晰的: 先找出公共的那个点, 再在连线上找出 $A^{\prime}, B^{\prime}, C^{\prime}, D^{\prime}$. 关于这个点有两种取法: 一种在边 (或对角线上), 另一种是直接利用顶点 $A$. 相比较而言, 后一种比较简便.

在做此题时需要灵活运用条件, 避开限制. 这题允许在正方形定住的情况下通过更改顶点标号来避免重合. 很多同学没有意识到这一点, 导致在解题中困难重重. 需要注意的是很多人尝试用位似、射影来解此题, 利用这种方法解题的人往往没有意识到位似、射影中的共点包括平行, 这在此题中是不允许的, 事实上,这正是难点所在.

题 6. 一项赛事共有 100 位选手参加. 对于任意两位选手 $x, y$, 他们之间恰比赛一次且分出胜负, 以 $x \rightarrow y$ 表示 $x$ 战胜 $y$. 如果对任意两位选手 $x, y$, 均能找到关于选手序列 $u_{1}, u_{2}, \cdots, u_{k}(k \geq 2)$, 使得 $x=u_{1} \rightarrow u_{2} \rightarrow \cdots \rightarrow u_{k}=y$, 那么称该赛事结果是 “友好” 的.

(i) 证明: 对任意一个友好的赛事结果, 存在正整数 $m$ 满足如下条件:

对任意两位选手 $x, y$, 均能找到某个长度为 $m$ 的选手序列 $z_{1}, z_{2}, \cdots, z_{m}$ (这里 $z_{1}, z_{2}, \cdots, z_{m}$ 可以有重复), 使得 $x=z_{1} \rightarrow z_{2} \rightarrow \cdots \rightarrow z_{m}=y$.

(ii) 对任意一个友好的赛事结果 $T$, 将符合 (i) 中条件的最小正整数 $m$ 记为
$m(T)$, 求 $m(T)$ 的最小值.

证明 (i) 对于两位选手 $x, y$, 按如下方式构造 $a(x, y) \in \mathbb{N}^{*}$ 与 $b(x, y) \in \mathbb{N}^{*}$, 满足若 $m=a(x, y) k+b(x, y)(k \in \mathbb{N})$, 则存在 $v_{1}, v_{2}, \cdots, v_{m}$, 使得

$$
x \rightarrow v_{1} \rightarrow v_{2} \rightarrow \cdots \rightarrow v_{m}=y
$$

对第一对 $(x, y)$, 由 “友好” 的定义, 存在 $r_{1}, r_{2}, \cdots, r_{l}$, 使得

$$
x \rightarrow r_{1} \rightarrow r_{2} \rightarrow \cdots \rightarrow r_{l}=y
$$

取 $z \neq x, y$, 则由定义, 存在 $v_{1}, v_{2}, \cdots, v_{t}, u_{1}, \cdots, u_{s}$, 使得

$$
x \rightarrow v_{1} \rightarrow v_{2} \rightarrow \cdots \rightarrow v_{t}=z \rightarrow u_{1} \rightarrow u_{2} \rightarrow \cdots \rightarrow u_{s}=x
$$

令 $a(x, y)=t+s \geq 2, b(x, y)=l$, 对 $m=a(x, y) k+b(x, y)$, 重复 $k$ 次 $(2)$, 再接一次 (1) 即可.

下设已构造完一些 $a(x, y), b(x, y)$, 并记 $\pi$ 为所有这些 $a(x, y)$ 之积, 则 $\pi \geq 2$.考虑 $\left(x_{0}, y_{0}\right)$, 类似的, 令 $b\left(x_{0}, y_{0}\right)=l_{0}$, 除去 $x_{0}, y_{0}$, 剩 98 人, 其中至少有一个人胜两局. 不妨设 $a \rightarrow b, a \rightarrow c$, 再不妨设 $b \rightarrow c$, 这里 $a, b, c$ 与之前构造的 $x, y$ 均不相等. 有定义, 设

$$
x_{0} \rightarrow v_{1} \rightarrow \cdots \rightarrow v_{t_{0}}=a \rightarrow c=u_{1} \rightarrow \cdots \rightarrow u_{s_{0}}=x_{0}
$$

重复 $\pi-1$ 次 (3), 再进行一次

$$
x_{0} \rightarrow v_{1} \rightarrow \cdots \rightarrow v_{t_{0}}=a \rightarrow b \rightarrow c=u_{1} \rightarrow \cdots \rightarrow u_{s_{0}}=x_{0}
$$

得 $x_{0} \rightarrow \cdots \rightarrow x_{0}$ 且长为 $\pi\left(t_{0}+s_{0}\right)+1$ 的圈. 令 $a\left(x_{0}, y_{0}\right)=\pi\left(t_{0}+s_{0}\right)+1$, 则其满足 $(*)$ 且与之前 $a(x, y)$ 均互素 (因为与 $\pi$ 互素).

所以可对所有的二人对 $(x, y)$ 构造两两互素的 $a(x, y)$ 与 $b(x, y)$ 使 $(*)$ 成立.同余方程组 $m \equiv b(x, y)(\bmod a(x, y))$ 有正整数解 $m$. 由 $(*)$ 知对任意的 $x, y$, 存在 $v_{1}, v_{2}, \cdots, v_{m}$ 使 $x \rightarrow v_{1} \rightarrow v_{2} \rightarrow \cdots \rightarrow v_{m}=y$.

(ii) 记 $m(T, n)$ 为 $n$ 个选手时 $m(T)$ 的最小值. 显然 $m(T, n) \geq 3$.

首先, 我们证明: $m(T, 9)=m(T, 12)=3$.

当 $n=9$ 时, 把选手编号为 $1,2, \cdots, 9$, 以下均在模 9 时讨论. 令选手 $i$ 胜 $i+2, i+3, i+4, i+8$, 则有 $i$ 负 $i+7, i+6, i+5, i+1$, 故所有胜负关系已确定.此时

$$
i \rightarrow(i+2) \rightarrow(i+2+8)=i+1, \quad i \rightarrow(i+3) \rightarrow(i+3+8)=i+2
$$

其余关系类似可得.
$n=12$ 时, 令 $i$ 胜 $i+2, i+3, i+4, i+7, i+11, i$ 与 $i+6$ 间胜负关系可任意确定. 类似与 $n=9$ 的情形可验证所有胜负关系都已确定.

接下来, 我们证明: 若 $m(T, a)=m(T, b)=3=m(T, c), a, b, c \geq 3$, 则

$$
m(T, a+b+1)=3, m(T, a+b+c)=3 .
$$

对 $n=a+b+c$, 把选手分为 $V_{1}, V_{2}, V_{3}$ 三组, 分别有 $a, b, c$ 人. 在 $V_{1}$ 内确定胜负使得在 $V_{1}$ 中 $m(T)=3$, 同样使 $V_{2}, V_{3}$ 中 $m(T)=3$.

令 $V_{1}$ 中人胜 $V_{2}$ 中人, $V_{2}$ 中人胜 $V_{3}$ 中人, $V_{3}$ 中人胜 $V_{1}$ 中人.

对任一选手 $x \in V_{1}$, 考虑选手 $y$ :

(A) 若 $y \in V_{1}$, 由于在 $V_{1}$ 中 $m(T)=3$, 存在另一人 $z \in V_{1}$, 使得 $x \rightarrow z \rightarrow y$;

(B) 若 $y \in V_{2}$, 由于 $V_{1}$ 胜 $V_{2}$, 则存在 $z \in V_{1}$, 且 $x \rightarrow z$, 使得 $x \rightarrow z \rightarrow y$;

(C) $y \in V_{3}$ ，则对任意 $z \in V_{2}$ ，都有 $x \rightarrow z \rightarrow y$.

对于 $x \in V_{2}, V_{3}$ 的情形可以类似讨论, 因此 $m(T, a+b+c)=3 . n=a+b+1$的情形也可以类似得到. 从而 $(* *)$ 得证.

故由 $m(T, 9)=m(T, 12)=3$, 得 $m(T, 9+12+9)=m(T, 30)=3$, 再由 $(* *)$得

$$
m(T, 30+9+1)=m(T, 40)=3, m(T, 30+40+30)=3
$$

即 $m(T, 100)=3$.

评注 本题放在第六题的位置似乎比较简单, 也许算是对第一天的难度的补偿吧! 第一小问的方法比较多, 既可以直接拿出两个人来仔细地分类讨论做分析,也可以直接证明对所有充分大的 $m$, 这样的结论都是成立的. 虽说方法很多, 归根结底还是要找到过一个人的两个长度互质的圈. 然后反复地在这些圈上操作,用数论的方法得到所需要的 $m$, 所有方法的本质都在于此.

第二问是一个构造题, 需要大胆的猜想与小心的构造, $T(m) \neq 2$ 是一个很好证的结论, 简单到以至于让人不敢猜测答案是 $T(m)=3$. 而很多人在试 3,6 到 8 个人, 发现 $T(m) \neq 3$ 后便抛弃了这一结论, 这是十分可惜的. 实际上, 9 个人的时候 $T(m)=3$, 接下来结合三组 $T(m)=3$ 的人可合并为一组, 从而构造 100 时, $T(m)=3$ 的情况.

