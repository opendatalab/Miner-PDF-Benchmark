# 2020首届百年老校数学竞赛试题解答 

王彬

(中国科学院数学与系统科学研究院, 100190)

首届百年老校数学竞赛于 2020 年 8 月 1 日至 5 日在浙江省宁波中学举行.下面介绍本次考试试题及解答.

## I. 试题

1. 已知 $\triangle A B C$ 满足 $A B+B C=2 A C$ 且 $A B \neq B C$. 设点 $O, I$ 分别是 $\triangle A B C$ 的外心与内心, 直线 $O I$ 交边 $B C$ 于点 $D$, 点 $E$ 在边 $A B$ 上使得 $B E=B D$. 设点 $M, N$ 分别为 $\odot O$ 的弧 $\overparen{A B}$ (不含 $C)$ 与弧 $\overparen{B C}$ (不含 $A)$ 的中点, 直线 $M E$ 和 $N D$ 交于点 $P$. 证明: 点 $P$ 在 $\triangle A B C$ 的外接圆上.

(北京四中 贾祥雪 供题)



2. 对实数 $\alpha$, 若 $\cos \alpha$ 和 $\sin \alpha$ 均为有理数, 则称 $\alpha$ 为 “好角”. 求同时满足下列两个条件的整数 $m$ 的个数:

(i) 存在好角 $\alpha$ 使得 $\cos \alpha=\frac{m}{100^{2020}}$;

(ii) 对整数 $n \geq 2$, 不存在好角 $\beta$ 使得 $\cos (n \beta)=\frac{m}{100^{2020}}$.

(福州一中 滒继崟、孙谌劼 供题)

3. 将 $100 \times 100 \times 100$ 的正方体分割成 $100^{3}$ 个单位正方体. 我们称这些单位正方体的棱为 “ $\mathrm{E}$ 棱” , 称这些单位正方体的面为 “ $\mathrm{F}$ 面” . 设 $\Omega$ 是由 2020 条两两不同的 “ $\mathrm{E}$ 棱” $e_{1}, e_{2}, \ldots, e_{2020}$ 构成的集合, 满足对其中任意两条 “E棱” $e_{i}$ 与 $e_{j}(1 \leq i<j \leq 2020)$, 它们有公共端点当且仅当 $j-i=1$ 或 2019 .

求证：可以将若干个 “ $\mathrm{F}$ 面” 染为蓝色, 使得属于 $\Omega$ 的每条 “ $\mathrm{E}$ 棱” 都恰好在奇数个蓝色的 “ $\mathrm{F}$ 面” 上, 同时不属于 $\Omega$ 的每条 “ $\mathrm{E}$ 棱” 都恰好在偶数个蓝色的 “ $F$ 面”上.

(上海中学 周天佑 供题)

4. 求最大的实数 $C$, 使得不等式

$$
\sum_{k=1}^{100} \frac{1}{x_{k}} \cdot \sum_{k=1}^{100}\left(x_{k}^{3}+2 x_{k}\right)-\left(\sum_{k=1}^{100} \sqrt{x_{k}^{2}+1}\right)^{2} \geq C
$$

对任意 100 个两两不同的正整数 $x_{1}, x_{2}, \ldots, x_{100}$ 成立.

(温州中学 邵达 供题)

5. 圆 $\Gamma_{1}$ 和圆 $\Gamma_{2}$ 相交于 $P, Q$ 两点, 圆 $\Gamma_{1}$ 的弦 $A B$ (异于 $P Q$ )与圆 $\Gamma_{2}$ 的弦 $C D$ (异于 $P Q$ ) 均经过 $P Q$ 的中点 $M$. 线段 $B D$ 与圆 $\Gamma_{1}$ 交于点 $G$ (异于 $B$ ), 与圆 $\Gamma_{2}$ 交于点 $H$ (异于 $D$ ). 点 $E, F$ 分别在线段 $B M$ 与 $D M$ 上, 满足 $E M=A M, F M=C M$. 直线 $E H$ 与 $F G$ 相交于点 $N$. 求证: $M, E, N, F$ 四点共圆.

(南方科技大学 付云皓 供题)



6. 是否存在正整数集的 100 个两两不交的子集 $A_{1}, A_{2}, \ldots, A_{100}$ 满足：对任意无穷多个质数组成的集合 $S$, 存在正整数 $m$ 以及

$$
a_{1} \in A_{1}, a_{2} \in A_{2}, \ldots, a_{100} \in A_{100}
$$

使得 $a_{1}, a_{2}, \ldots, a_{100}$ 都可以表示为 $S$ 中的 $m$ 个不同质数的乘积.

(镇海中学 沈虎跃供题)

## II. 解答

1. 已知 $\triangle A B C$ 满足 $A B+B C=2 A C$ 且 $A B \neq B C$. 设点 $O, I$ 分别是 $\triangle A B C$ 的外心与内心, 直线 $O I$ 交边 $B C$ 于点 $D$, 点 $E$ 在边 $A B$ 上使得 $B E=B D$. 设点 $M, N$ 分别为 $\odot O$ 的弧 $\widehat{A B}$ (不含 $C)$ 与弧 $\widehat{B C}$ (不含 $A$ ) 的中点, 直线 $M E$ 和 $N D$ 交于点 $P$. 证明: 点 $P$ 在 $\triangle A B C$ 的外接圆上.


证明. 延长 $B I$ 交外接圆 $\odot O$ 于点 $Q$, 由鸡爪定理可知 $A Q=Q I=Q C$. 在圆内接四边形 $A B C Q$ 中由托勒密定理可得:

$$
A Q \times B C+Q C \times A B=A C \times Q B=A C \times(Q I+I B)
$$

由 $A B+B C=2 A C$ 可知 $2 A Q=Q I+I B$ 进而 $Q I=I B$, 由垂径定理可得 $I O \perp I B$. 连接 $I E$, 由 $I$ 是 $\triangle A B C$ 的内心可知 $\triangle B I D \cong \triangle B I E$, 进而 $I E \perp I B$. 即 $D, I, E$ 三点共线.

设 $N D$ 交 $\odot O$ 于点 $P^{\prime}, M P^{\prime}$ 交 $A B$ 于点 $E^{\prime}$. 对六边形 $A B C M P^{\prime} N$ 使用帕斯卡定理, 因为 $C M$ 交 $A N$ 于点 $I$, 故 $D, I, E^{\prime}$ 三点共线.

又 $D, I, E$ 共线. 点 $E$ 和点 $E^{\prime}$ 都在 $A B$ 上, 故点 $E$ 和 $E^{\prime}$ 重合.

故 $N D$ 和 $M E$ 交于点 $P^{\prime}$, 从而点 $P$ 与点 $P^{\prime}$ 重合, 即点 $P$ 在外接圆 $\odot O$上.
注. 解答的后半部分也可以采用帕斯卡定理的逆定理, 即六边形 $A B C M P N$ 满足相应的三组交点共线后,可知其六个顶点一定在同一个圆锥曲线(二次曲线)上, 而其中五个点顶点 $A, B, C, M, N$ 共圆, 可知第六个顶点 $P$也在该圆上(因为两个不同的非退化二次曲线至多只有四个交点).

2. 对实数 $\alpha$, 若 $\cos \alpha$ 和 $\sin \alpha$ 均为有理数, 则称 $\alpha$ 为 “好角”. 求同时满足下列两个条件的整数 $m$ 的个数:

(i) 存在好角 $\alpha$ 使得 $\cos \alpha=\frac{m}{100^{2020}}$;

(ii) 对整数 $n \geq 2$, 不存在好角 $\beta$ 使得 $\cos (n \beta)=\frac{m}{100^{2020}}$.

解. 设所有好角构成集合 $M$, 容易验证集合 $M$ 对加减法封闭. 记 $\theta=$ $\arccos \frac{4}{5}$, 我们有 $\theta \in M, \frac{\pi}{2} \in M$, 对正整数 $n$, 集合

$$
A_{n}=\left\{n \theta+r \times \frac{\pi}{2}: r=0,1,2,3\right\}
$$

中四个数都是好角.

对正整数 $n$, 称 $\cos n \alpha$ ( $\alpha$ 是好角) 形式的数为 “可被 $n$ 阶表示” . 题目考虑所有 $\frac{m}{100^{2020}}$ 形式的有理数, 它可被 1 阶表示但不可被高阶 $(n \geq 2$ 阶)表示.

对好角 $\alpha$, 设有理数 $\cos \alpha, \sin \alpha$ 约分后分别为 $\frac{x}{z}, \frac{y}{z^{\prime}}$ (整数 $x, z$ 互质, $y, z^{\prime}$ 互质, 且 $z, z^{\prime}$ 是正整数),

$$
\cos ^{2} \alpha+\sin ^{2} \alpha=\frac{x^{2}}{z^{2}}+\frac{y^{2}}{z^{\prime 2}}=1 \Rightarrow \frac{y^{2}}{z^{\prime 2}}=\frac{z^{2}-x^{2}}{z^{2}}
$$

两个最简分数相等可知其分子分母分别相等, 即: $z=z^{\prime}, x^{2}+y^{2}=z^{2}$, 这时只能 $x, y$ 一奇一偶, 分母 $z$ 是奇数. 因此题目中的 $\frac{m}{100^{2020}}$ 约分后一定是 $\frac{x}{5^{t}}$ 的形式(分子 $x$ 与 5 互质), 其中 $t \in\{0,1, \ldots, 4040\}$, 称这样的数为 $t$ 型好数, 设所有 $t$ 型好数构成集合 $B_{t}$. 例如 $B_{1}=\left\{ \pm \frac{3}{5}, \pm \frac{4}{5}\right\}$, 它们是

$$
A_{1}=\left\{\theta+r \times \frac{\pi}{2}: r=0,1,2,3\right\}
$$

中四个好角的 $\cos$ 值.

我们关注 $\cos n \alpha$ 与 $\cos \alpha$ 的关系, 考虑切比雪夫多项式 $\left\{T_{n}\right\}_{n=1}^{\infty}$ :

$$
\begin{aligned}
& T_{1}(X)=X \\
& T_{2}(X)=2 X^{2}-1, \\
& T_{3}(X)=4 X^{3}-3 X, \\
& T_{n+2}(X)=2 X T_{n+1}(X)-T_{n}(X), n=1,2, \ldots
\end{aligned}
$$

由归纳法易知: $T_{n}(X)$ 是首项系数为 $2^{n-1}$ 的 $n$ 次整系数多项式, 且满足
$T_{n}(\cos \alpha)=\cos n \alpha$. 如果有理数 $\cos \alpha=\frac{x}{z}$, 则

$$
\begin{aligned}
\cos n \alpha & =T_{n}\left(\frac{x}{z}\right)=\frac{2^{n-1} x^{n}}{z^{n}}+\square \frac{x^{n-1}}{z^{n-1}}+\square \frac{x^{n-2}}{z^{n-2}}+\cdots \\
& =\frac{2^{n-1} x^{n}+\square x^{n-1} z+\square x^{n-2} z^{2}+\cdots}{z^{n}}
\end{aligned}
$$

其中分子与 $z$ 互质, 因此 $\cos n \alpha$ 的分母等于 $z^{n}$, 即恰好是 $\cos \alpha$ 分母的 $n$ 次方.

对 $\cos \theta=\frac{4}{5}$, 由上述推理可知: $\cos n \alpha=\frac{x_{n}}{5^{n}}, \sin n \theta=\frac{y_{n}}{5^{n}}$ 且分子 $x_{n}, y_{n}$ 均为与 5 互质的整数, 这样可得到 $\left\{ \pm \frac{x_{n}}{5^{n}}, \pm \frac{y_{n}}{5^{n}}\right\}$ 这四个 $n$ 型好数. 我们断言除此之外没有别的 $n$ 型好数, 这是因为不定方程 $x^{2}+y^{2}=5^{2 n}$ 只有一组正整数解 $(x, y)$满足 $x>y>0$ 且 $(x, 5)=1$. 若不然, 设

$$
5^{2 n}=x^{2}+y^{2}=u^{2}+v^{2}(x>y>0, u>v>0),
$$

则

$$
5^{2 n} \mid\left(5^{2 n}-y^{2}\right)\left(5^{2 n}-v^{2}\right)-y^{2} v^{2}=x^{2} u^{2}-y^{2} v^{2}=(x u+y v)(x u-y v) .
$$

由于 $x, y, u, v$ 均与 5 互质, 这样 $(x u+y v)$ 与 $(x u-y v)$ 不能都被 5 整除, 因此有 $5^{2 n} \mid x u+y v$ 或 $5^{2 n} \mid x u-y v$, 由于

$$
0<x u-y v<\max \left\{x^{2}, u^{2}\right\}<5^{2 n}
$$

所以只能 $5^{2 n} \mid x u+y v$ 即 $x u+y v \geq 5^{2 n}$, 这样可推得: $x=u, y=v$, 矛盾. 因此恰有四个 $n$ 型好数, 即:

$$
B_{n}=\left\{ \pm \frac{x_{n}}{5^{n}}, \pm \frac{y_{n}}{5^{n}}\right\}=\left\{\cos \alpha: \alpha \in A_{n}\right\}=\left\{\cos \left(n \theta+r \times \frac{\pi}{2}\right): r=0,1,2,3\right\} .
$$

注意一个细节是 $A_{n}=\left\{n \theta+r \times \frac{\pi}{2}: r=0,1,2,3\right\}$ 中的四个好角的 $\cos$ 值是互不相同的, (否则会出现 $2 n \theta$ 是 $\frac{\pi}{2}$ 的整数倍的情况, 导致 $\cos (2 n \theta)=0, \pm 1$ 矛盾.)

由切比雪夫多项式的分析可知: 若某个 $t$ 型好数可被 $n$ 阶表示, 即 $\frac{x}{5^{t}}=$ $\cos n \beta$, 则此时 $\cos \beta$ 一定是分母为 $5^{\frac{t}{n}}$ 的有理数, 即 $\cos \beta \in B_{\frac{t}{n}}$. 接下来我们考虑原问题, 即考虑每个 $B_{t}$ 中分别有几个数满足"不能被高阶表示” 的条件:

若 $t=0$, 则 $B_{0}=\{-1,0,1\}$ 中的数均可被高阶表示, 都不满足条件;

若 $t=1$, 则 $B_{1}=\left\{ \pm \frac{3}{5}, \pm \frac{4}{5}\right\}$ 中的 4 个好数均不能被高阶表示, 即都满足条件;

若 $t>1$ 不是 2 的方幂, 即存在奇数 $L \geq 3$ 整除 $t$, 设 $t=L k$. 此时 $A_{k}=\left\{k \theta+r \times \frac{\pi}{2}, r=0,1,2,3\right\}$ 中的四个好角的 $L$ 倍变成 $\left\{k L \theta+L r \times \frac{\pi}{2}: r=0,1,2,3\right\} \equiv\left\{k L \theta+r \times \frac{\pi}{2}: r=0,1,2,3\right\}=A_{k L}(\bmod 2 \pi)$,即 $B_{t}=B_{k L}$ 中的数均可被 $L$ 阶表示, 即都不满足条件;
若 $t=2^{k},(k \geq 1)$ 是 2 的方幂, 如果 $B_{t}=B_{2^{k}}=\left\{\cos \alpha: \alpha \in A_{2^{k}}\right\}$ 中某个数可被 $n \geq 2$ 阶表示, 则 $n \mid 2^{k}$ 可知 $n$ 也是 2 的方幕, 因此该数 $\cos n \beta=\cos 2 \beta^{*}$可被 2 阶表示(其中 $\beta^{*}=\frac{n}{2} \beta$ 也是好角), 这时

$$
\beta^{*} \in A_{2^{k-1}}=\left\{2^{k-1} \theta+\tilde{r} \times \frac{\pi}{2}: \tilde{r}=0,1,2,3\right\}
$$

我们考虑 $2 \beta^{*}$ 能 $(\bmod 2 \pi)$ 意义下取到 $\left.A_{2^{k}}=\left\{2^{k} \theta+r \times \frac{\pi}{2}\right): r=0,1,2,3\right\}$ 中的哪些角, 由于 $2 \beta^{*}$ 是 $2^{k} \theta+2 \tilde{r} \times \frac{\pi}{2}$ 的形式, 可以取到 $r=0,2$ 的情况, 不能取到 $r=1,3$ 的情况, 因此 $B_{t}=B_{2^{k}}$ 中恰有两个数满足条件.

综上 $B_{1}$ 中有四个数, $B_{2}, B_{4}, \ldots, B_{2^{11}}$ 中各有两个数, 共 26 个数满足条件.

3. 将 $100 \times 100 \times 100$ 的正方体分割成 $100^{3}$ 个单位正方体. 我们称这些单位正方体的棱为 “ $\mathrm{E}$ 棱” ，称这些单位正方体的面为 “ $\mathrm{F}$ 面” 。设 $\Omega$ 是由 2020 条两两不同的 “ $\mathrm{E}$ 棱” $e_{1}, e_{2}, \ldots, e_{2020}$ 构成的集合, 满足对其中任意两条 “E棱” $e_{i}$ 与 $e_{j}(1 \leq i<j \leq 2020)$, 它们有公共端点当且仅当 $j-i=1$ 或 2019 .

求证：可以将若干个 “ $\mathrm{F}$ 面” 染为蓝色, 使得属于 $\Omega$ 的每条 “ $\mathrm{E}$ 棱” 都恰好在奇数个蓝色的 “ $\mathrm{F}$ 面” 上, 同时不属于 $\Omega$ 的每条 “ $\mathrm{E}$ 棱” 都恰好在偶数个蓝色的 “ $\mathrm{F}$ 面” 上.

证明. 记 $m=1010$ 即 $2 m=2020$. 设棱 $e_{i}$ 与 $e_{i+1}$ 的公共端点为

$$
P_{i},\left(i=1,2, \ldots, 2 m, e_{2 m+1}=e_{1}\right)
$$

这样得到点 $P_{1}, P_{2}, \ldots, P_{2 m}$ (它们两两不同, 也是单位正方体的顶点), 以及棱 $e_{i}$的两个端点是 $P_{i-1}, P_{i},\left(P_{0}=P_{2 m}\right)$. 直观的看, $\Omega$ 中的 $2 m$ 条棱构成一条不自交的闭曲线 (一个圈).

记所有的”F面”构成集合 $A$, 所有的” $\mathrm{E}$ 棱”构成集合 $B$. 我们考虑一个 $A$的子集族到 $B$ 的子集族的映射 $\Phi: 2^{A} \mapsto 2^{B}$ ，对任意由若干个 “ $\mathrm{F}$ 面” 构成的集合 $S \subseteq A$, 定义 $\Phi(S)$ 是由所有恰好在 $S$ 中的奇数个面上的” $\mathrm{E}$ 棱”构成的集合. 例如若 $S$ 是某个” $F$ 面”构成的单元集, 则 $\Phi(S)$ 恰好是它的 4 条” E棱”构成的集合, 如果 $S$ 是某个单位立方体的六个面构成集合, 则 $\Phi(S)$ 是空集.

注意 $\Phi$ 有一个重要的性质, 它是模 2 意义下的线性函数. 即对 $\Phi\left(S_{1}\right)=T_{1}$与 $\Phi\left(S_{2}\right)=T_{2}$ 我们有 $\Phi\left(S_{1} \triangle S_{2}\right)=T_{1} \triangle T_{2}$, 这里 $\triangle$ 表示集合的对称差运算, 也可以理解为(把集合看成示性函数意义下的) 模 2 加法运算.
题目的要求是对任意长为 $2 m$ 的封闭曲线 $\Omega$, 存在它在 $\Phi$ 映射下的原像. 我们对 $m$ 归纳来证明该命题.

归纳奠基 $m=2$ 即恰好 4 条” E棱” 时,它们一定是某个”F面”的 4 条” $\mathrm{E}$棱”, 结论成立. 一般情况下, 我们考虑把 $\Omega$ 这个大圈分解成两个圈 “相加” $\Omega=\Omega_{1} \triangle \Omega_{2}$, 其中 $\Omega_{1}, \Omega_{2}$ 是长度更小的圈或者容易找到原像的圈.

具体的, 对于闭曲线 $\Omega=\left(P_{1}-P_{2}-\cdots-P_{2 m}-P_{1}\right)$ 的 $2 m$ 条棱, 如果有某两个不相邻的点 $P_{i}, P_{j}$ 的距离为 $1,(1 \leq i<i+1<j \leq 2 m)$ 即有一条不属于 $\Omega$ 的棱 $e *$ 以 $P_{i} P_{j}$ 为端点. 此时我们作出

$\Omega_{1}=\left(P_{i}-P_{i+1}-\cdots-P_{j}-P_{i}\right), \Omega_{2}=\left(P_{j}-P_{j+1}-\cdots-P_{2 m}-P_{1}-\cdots-P_{i}-P_{j}\right)$

是两条长度均小于 $2 m$ 的闭曲线, 由归纳假设存在 $S_{1}, S_{2} \subset A$ 使得

$$
\Phi\left(S_{1}\right)=\Omega_{1}, \Phi\left(S_{2}\right)=\Omega_{2}
$$

此时

$$
\Phi\left(S_{1} \triangle S_{2}\right)=\Omega_{1} \triangle \Omega_{2}=\Omega
$$

满足条件.

如果任意不相邻顶点的距离都大于 1 , 则考虑顶点 $P_{k}$ 的坐标

$$
\left(x_{k}, y_{k}, z_{k}\right), k=1,2, \ldots, 2 m \text {. }
$$

不妨设 $x_{1}, x_{2}, \ldots, x_{2 m}$ 的取值不为常数, 设它们的取值最大为 $b$, 且不全为 $b$, 即其中有一些 $=b$, 有一些 $\leq b-1$. 由于角标模 $2 m$ 循环, 不妨设 $x_{0}=x_{2 m} \leq b-1$且有某个 $l$ 使得 $x_{l}=b$, 此时依此考虑 $x_{l+1}, x_{l+2}, \ldots$ 的取值, 其中会首次出现 $x_{k}=b-1$ 的情况, 不妨设为 $x_{v+1}$, 即存在 $v$ 使得:

$$
x_{l}=x_{l+1}=\cdots=x_{v}=b, x_{v+1}=b-1 .
$$

同理存在 $u$ 使得

$$
x_{l}=x_{l-1}=\cdots=x_{u}=b, x_{u-1}=b-1 .
$$

我们有 $1 \leq u \leq k \leq v \leq 2 m-1$, 且由于 $P_{l-1} \neq P_{l+1}$ 可知 $u, v$ 不能都等于 $l$, 即 $v-u \geq 1$. 这样我们有 $x_{u}=x_{u+1}=\cdots=x_{v}=b, x_{u-1}=x_{v+1}=b-1$.

对 $k=u, u+1, \ldots, v$, 我们取点 $Q_{k}=\left(x_{k}-1, y_{k}, z_{k}\right)$ 即把点 $P_{k}=\left(x_{k}, y_{k}, z_{k}\right)$平移一格使 $x$ 坐标减小 1 , 由任意不相邻顶点的距离都大于 1 的假设可知 $Q_{u+1}, Q_{u+2}, \ldots, Q_{v-1}$ 与点 $P_{1}, P_{2}, \ldots, P_{2 m}$ 互不相同, 且 $Q_{u}=P_{u-1}, Q_{v}=P_{v+1}$.
我们设计 $\Omega_{1}=\left(P_{u}-P_{u+1}-\cdots-P_{v}-Q_{v}-Q_{v-1}-\cdots-Q_{u}-P_{u}\right)$ 以及

$$
\begin{gathered}
\Omega_{2}=\left(P_{1}-P_{2}-\cdots-P_{u-1}\left(=Q_{u}\right)-Q_{u+1}-Q_{u+2}-\cdots\right. \\
\left.-Q_{v-1}\left(=P_{v}\right)-P_{v+1}-\cdots-P_{2 m}-P_{1}\right)
\end{gathered}
$$

取 $S_{1}$ 是由 $v-u$ 个“ $\mathrm{F}$ 面” $\left\{\left(P_{k} P_{k+1} Q_{k+1} Q_{k}\right) \mid k=u, u+1, \ldots, v-1\right\}$ 构成的集合. 此时 $\Phi\left(S_{1}\right)=\Omega_{1}$, 另一方面 $\Omega_{2}$ 是长度为 $2 m-2$ 的闭曲线, 由归纳假设知存在 $S_{2} \subset A$ 使得 $\Phi\left(S_{2}\right)=\Omega_{2}$, 这样 $\Phi\left(S_{1} \triangle S_{2}\right)=\Omega_{1} \triangle \Omega_{2}=\Omega$ 满足条件.

由归纳法可知命题对所有 $m \geq 2$ 成立, 特别的对原题中的 $m=1010$ 即 2020 条”E棱”时成立.

注. 本题的背景与拓扑、同调论有关, 即 $\mathbb{R}^{3}$ 的 1 阶同调群 $H_{1}\left(\mathbb{R}^{3}\right)=0$ 是平凡的. 结论直观来看就是: 三维空间中的一条封闭曲线总是某一片曲面的边缘(边界), 本题是该结论的离散版本。

解答中的 $\Phi$ 映射类似于求二维图形的边缘的运算, 结论也可以理解为: $\mathbb{R}^{3}$中的某个一维图形如果没有边缘, 则它一定是某个二维图形的边缘.

4. 求最大的实数 $C$, 使得不等式

$$
\sum_{k=1}^{100} \frac{1}{x_{k}} \cdot \sum_{k=1}^{100}\left(x_{k}^{3}+2 x_{k}\right)-\left(\sum_{k=1}^{100} \sqrt{x_{k}^{2}+1}\right)^{2} \geq C
$$

对任意 100 个两两不同的正整数 $x_{1}, x_{2}, \ldots, x_{100}$ 成立.

解. 记 $m=100$. 看到 $\left(\sum_{k=1}^{m} \sqrt{x_{k}^{2}+1}\right)^{2}$, 想到柯西不等式与拉格朗日恒等式, 考虑把式子左边变形成为 $S+T$, 其中 $S=\left(\sum_{k=1}^{m} \frac{1}{x_{k}}\right) \cdot\left(\sum_{k=1}^{m} x_{k}\right)$,

$T=\sum_{k=1}^{m} \frac{1}{x_{k}} \cdot \sum_{k=1}^{m} x_{k}\left(x_{k}^{2}+1\right)-\left(\sum_{k=1}^{m} \sqrt{x_{k}^{2}+1}\right)^{2}=\sum_{1 \leq i<j \leq m}\left[\sqrt{\frac{x_{j}\left(x_{j}^{2}+1\right)}{x_{i}}}-\sqrt{\frac{x_{i}\left(x_{i}^{2}+1\right)}{x_{j}}}\right]^{2}$.

我们分别考虑 $S, T$ 的取值下界, 易知 $S \geq m^{2}$,且当

$$
\left\{x_{1}, x_{2}, \ldots, x_{m}\right\}=\{N+1, N+2, \ldots, N+m\}
$$

同时正整数 $N$ 充分大时, $S$ 的值充分接近 $m^{2}$.

我们对 $T$ 的求和式中的每一项进行化简, 记 $x=x_{i}, y=x_{j}$ 不妨设 $y>x$,

$$
A(y, x)=\sqrt{\frac{y\left(y^{2}+1\right)}{x}}-\sqrt{\frac{x\left(x^{2}+1\right)}{x}}=\frac{y \sqrt{y^{2}+1}-x \sqrt{x^{2}+1}}{\sqrt{x y}}
$$

容易看出 $x \sqrt{x^{2}+1}$ 比较接近于 $x^{2}+\frac{1}{2}$, 并且后者略大于前者:

$$
g(x)=x^{2}+\frac{1}{2}-x \sqrt{x^{2}+1}=\frac{1}{4} \times \frac{1}{x^{2}+\frac{1}{2}+x \sqrt{x^{2}+1}}<\frac{1}{8 x^{2}}
$$

显然 $g(x)$ 是减函数, 且当 $x$ 较大时, $g(x)$ 取值很小,因此:

$$
\begin{gathered}
A(y, x)=\frac{\left[y^{2}+\frac{1}{2}-f(y)\right]-\left[x^{2}+\frac{1}{2}-f(x)\right]}{\sqrt{x y}}=\frac{y^{2}-x^{2}}{\sqrt{x y}}+\frac{g(x)-g(y)}{\sqrt{x y}} \\
>\frac{(y+x)(y-x)}{\sqrt{x y}}>2(y-x) \\
A(y, x)=\frac{y^{2}-x^{2}}{\sqrt{x y}}+\frac{g(x)-g(y)}{\sqrt{x y}}<2(y-x) \frac{y}{\sqrt{x y}}+\frac{1}{8 x^{2} \sqrt{x y}}
\end{gathered}
$$

我们对 $x_{1}, x_{2}, \ldots, x_{m}$ 排序, 设 $x_{1}<x_{2}<\cdots<x_{m}$, 此时对 $j>i$ 有 $x_{j}-x_{i} \geq j-i$.

$$
\begin{aligned}
T & =\sum_{1 \leq i<j \leq m}\left[A\left(x_{j}, x_{i}\right)\right]^{2}>\sum_{1 \leq i<j \leq m} 4\left(x_{j}-x_{i}\right)^{2} \\
& \geq \sum_{1 \leq i<j \leq m} 4(j-i)^{2}=2 \sum_{i=1}^{m} \sum_{j=1}^{m}(j-i)^{2} \\
& =4 m\left(\sum_{i=1}^{m} i^{2}\right)-4\left(\sum_{i=1}^{m} i\right)^{2}=\frac{4 m^{2}(m+1)(2 m+1)}{6}-m^{2}(m+1)^{2} \\
& =\frac{m^{4}-m^{2}}{3}
\end{aligned}
$$

我们有 $T>\frac{1}{3}\left(m^{4}-m^{2}\right)$, 且当

$$
\left(x_{1}, x_{2}, \ldots, x_{m}\right)=(N+1, N+2, \ldots, N+m)
$$

同时正整数 $N$ 充分大时, 由 $A\left(x_{j}, x_{i}\right)<2(j-i) \frac{N+m}{N}+\frac{1}{N^{3}}$ 可知此时

$$
\begin{aligned}
T & =\sum_{1 \leq i<j \leq m}\left[A\left(x_{j}, x_{i}\right)\right]^{2}<\frac{m^{2}}{N^{3}}+\frac{N+m}{N} \sum_{1 \leq i<j \leq m} 4(j-i)^{2} \\
& =\frac{m^{4}-m^{2}}{3}+\left(\frac{m^{4}-m^{2}}{3} \times \frac{m}{N}+\frac{m^{2}}{N^{3}}\right)
\end{aligned}
$$

可以充分接近其最小值 $\frac{1}{3}\left(m^{4}-m^{2}\right)$.

综上

$$
S+T>m^{2}+\frac{1}{3}\left(m^{4}-m^{2}\right)=\frac{1}{3} m^{2}\left(m^{2}+2\right),
$$

当

$$
\left(x_{1}, x_{2}, \ldots, x_{m}\right)=(N+1, N+2, \ldots, N+m)
$$

同时正整数 $N$ 充分大时, $S+T$ 充分接近其最小值. 因此题目所求的结果为 $\frac{1}{3} m^{2}\left(m^{2}+2\right)=33340000$.

5. 圆 $\Gamma_{1}$ 和圆 $\Gamma_{2}$ 相交于 $P, Q$ 两点, 圆 $\Gamma_{1}$ 的弦 $A B$ (异于 $P Q$ )与圆 $\Gamma_{2}$的弦 $C D$ (异于 $P Q$ ) 均经过 $P Q$ 的中点 $M$. 线段 $B D$ 与圆 $\Gamma_{1}$ 交于点 $G$ (异于 $B$ ), 与圆 $\Gamma_{2}$ 交于点 $H$ (异于 $D$ ). 点 $E, F$ 分别在线段 $B M$ 与 $D M$ 上, 满足
$E M=A M, F M=C M$. 直线 $E H$ 与 $F G$ 相交于点 $N$. 求证: $M, E, N, F$ 四点共圆.

证法一. 如图, 作 $\triangle D F G$ 的外接圆 $\Gamma_{3}$. 设直线 $M G$ 与圆 $\Gamma_{3}$ 交于 $J$ (异于 $G)$, 则

$$
M G \cdot M J=M F \cdot M D=M C \cdot M D=M P \cdot M Q=M A \cdot M B=M E \cdot M B .
$$



所以 $B, E, G, J$ 四点共圆, 记该圆为圆 $\Gamma_{4}$.

由 $A M=E M$ 及 $C M=F M$ 知四边形 $A P E Q$ 是平行四边形, 故 $\angle P A Q=\angle P E Q$. 再由 $M G \cdot M J=M P \cdot M Q=M P^{2}=M Q^{2}$ 可得 $\triangle M P G \sim \triangle M J P$ 且 $\triangle M Q G \sim \triangle M J Q$, 故

$$
\begin{aligned}
\angle P J Q & =\angle P J M+\angle Q J M=\angle G P M+\angle G Q M \\
& =\pi-\angle P G Q=\pi-\angle P A Q=\pi-\angle P E Q
\end{aligned}
$$

故 $E, P, Q, J$ 四点共圆.

考虑三圆: $\Gamma_{1}, \Gamma_{4}$ 与 $\odot(E P J Q)$, 由根心定理可知 $P Q, B G, E J$ 三线交于一点, 记该点为 $K$.

由相交弦定理得 $E K \cdot J K=P K \cdot Q K=D K \cdot H K$, 故 $E, H, J, D$ 四点共圆, 故

$$
\angle M F N=\angle M J D=\angle E J D-\angle E J M=\angle E H D-\angle E B G=\angle B E H .
$$

故 $M, E, N, F$ 四点共圆.

证法二. 如图, 设直线 $P Q, B D$ 相交于点 $K$. 则 $E M \cdot B M=M P^{2}$ 且 $H K \cdot D K=P K \cdot Q K$. 由 $M$ 是 $P Q$ 的中点可得 $M P^{2}-P K \cdot Q K=M K^{2}$, 故



$B E \cdot B M-B H \cdot D K=(B M-E M) \cdot B M-(B K-H K) \cdot D K$

$$
\begin{aligned}
& =B M^{2}-(E M \cdot B M-H K \cdot D K)-B K \cdot D K \\
& =B M^{2}-\left(M P^{2}-P K \cdot Q K\right)-B K \cdot D K \\
& =B M^{2}-M K^{2}-B K \cdot D K \\
& =B K \cdot(B K-2 M K \cdot \cos \angle B K M-D K)
\end{aligned}
$$

同理 $D F \cdot D M-D G \cdot B K=D K \cdot(D K-2 M K \cdot \cos \angle D K M-B K)$, 所以

$$
\frac{B E \cdot B M-B H \cdot D K}{D F \cdot D M-D G \cdot B K}=-\frac{B K}{D K} .
$$

注意 $B K \cdot G K=P K \cdot Q K=D K \cdot H K$, 故 $\frac{B K}{D K}=\frac{H K}{G K}=\frac{B H}{D G}$, 故

$$
\begin{aligned}
& \frac{B E \cdot B M-B H \cdot D K}{D F \cdot D M-D G \cdot B K}=-\frac{B H}{D G} \\
\Rightarrow & \frac{B E \cdot B M-B H \cdot D K}{B H}=-\frac{D F \cdot D M-D G \cdot B K}{D G} .
\end{aligned}
$$

即 $\frac{B E \cdot B M}{B H}+\frac{D F \cdot D M}{D G}=B D$.

现于 $B D$ 上取一点 $L$ 使得 $B L=\frac{B E \cdot B M}{B H}$, 则 $D L=\frac{D F \cdot D M}{D G}$, 而这意味 $M, E, H, L$ 四点共圆, 且 $M, F, G, L$ 四点共圆, 故 $\angle B E N-\angle M L B=\angle M F N$,故 $M, E, N, F$ 四点共圆.

6. 是否存在正整数集的 100 个两两不交的子集 $A_{1}, A_{2}, \ldots, A_{100}$ 满足：对任意无穷多个质数组成的集合 $S$, 存在正整数 $m$ 以及

$$
a_{1} \in A_{1}, a_{2} \in A_{2}, \ldots, a_{100} \in A_{100}
$$

使得 $a_{1}, a_{2}, \ldots, a_{100}$ 都可以表示为 $S$ 中的 $m$ 个不同质数的乘积.

解. 存在, 下面给出一种构造方法. 记全体质数为 $p_{1}<p_{2}<p_{3}<\ldots$, 对任
意正整数 $m$, 记所有无平方因子且恰有 $m$ 个质因数的正整数构成集合 $H_{m}$.

考虑 $A_{1}, A_{2}, \ldots, A_{100}$ 的构造, 即对所有无平方因子的数 $H=\bigcup_{m=1}^{\infty} H_{m}$ 进行 100 划分. 我们分别对每个 $H_{m}$ 考虑划分, 对 $a=p_{i_{1}} p_{i_{2}} \cdots p_{i_{m}} \in H_{m}$, 我们考虑让 $a$ 的分类结果 $F(a)$ 只取决于 $a$ 的最小素因子 $p_{i_{1}}$ 的情况. 这样我们只需对每个正整数 $m$, 给出一个素数集 $P=\left\{p_{1}, p_{2}, p_{3}, \ldots\right\}$ 的分类函数(分类方案) $f_{m}: P \mapsto\{1,2, \ldots, 100\}$, 即可诱导出 $H_{m}$ 的分类方案:

$$
F(a)=f_{m}\left(p_{i_{1}}\right) \in\{1,2, \ldots, 100\}, \quad a=p_{i_{1}} p_{i_{2}} \cdots p_{i_{m}} \in H_{m}, \quad i_{1}<i_{2}<\cdots<i_{m}
$$

设计 $P$ 的分类方案 $f_{m}$ 时, 我们考虑简单的按照大小分段的方式, 即设定好 99 个分点(写成有序数组的形式) $\beta=\left(x_{1}, x_{2}, \ldots, x_{99}\right)$, (默认 $x_{0}=0, x_{100}=+\infty$ , 且递增排列 $\left.0<x_{1}<x_{2}<\cdots<x_{99}<+\infty\right)$, 我们把满足 $x_{k-1}<p \leq x_{k}$ 的质数 $p$ 归为第 $k$ 类, $k=1,2, \ldots, 100$, 即定义

$$
f_{m}(p)=\min \left\{k=1,2, \ldots, 100: x_{k} \geq p\right\}, \forall p \in P
$$

我们为每个 $m$ 选择分点数组 $\beta_{m}$, 并得到相应的分类函数 $f_{m}$. 要求对于任意无穷素数集 $S$, 都存在某个 $m$ 使得 $\left\{f_{m}(p): p \in S\right\}$ 的取值遍历 $\{1,2, \ldots, 100\}$.

一个自然的想法是选择互不相同的, 尽可能多的 $\beta_{m}$, 或者尝试考虑所有可能的分点数组 $\beta=\left(x_{1}, x_{2}, \ldots, x_{99}\right)$, 事实上这些分点 $x_{k}$ 都可以取成质数, 因此我们考虑质数集 $P$ 的所有 99 元子集(记作数组的形式)构成的集合:

$$
C=\left\{\beta=\left(p_{l_{1}}, p_{l_{2}}, \ldots, p_{l_{99}}\right) \mid l_{1}<l_{2}<\cdots<l_{99} \in Z_{+}\right\}
$$

幸运的是集合 $C$ 是可数集, 即可以把 $C$ 的所有元素排成一排(例如按照元素和从小到大排序, 固定 99 个元素之和后, 99 元子集的选择只有有限个), 并依次被命名为 $\beta_{1}, \beta_{2}, \beta_{3}, \ldots$ 接下来对每个 $m$, 我们根据分点数组 $\beta_{m}=\left(x_{m, 1}, x_{m, 2}, \ldots, x_{m, 99}\right)$ ( 默认 $\left.x_{m, 0}=0, x_{m, 100}=+\infty\right)$, 给出素数集 $P$ 的分类方案 $f_{m}$, 然后由 $f_{m}$ 诱导出 $H_{m}$ 的分类方案以及最终的 $H=\bigcup_{m=1}^{\infty} H_{m}$ 的分类方案. 即对 $k=1,2, \ldots, 100$, 定义:

$$
A_{k}=\bigcup_{m=1}^{\infty}\left\{a=p_{i_{1}} p_{i_{2}} \ldots p_{i_{m}} \in H_{m}: x_{m, k-1}<p_{i_{1}} \leq x_{m, k}, p_{i_{1}}<p_{i_{2}}<\cdots<p_{i_{m}}\right\}
$$

这个方案满足题意. 对素数集 $P$ 的无穷子集 $S=\left\{q_{1}, q_{2}, q_{3} \ldots\right\}$ (元素从小到大排列), 考虑其中最小的 99 个素数构成的数组 $\left(q_{1}, q_{2}, \ldots, q_{99}\right)$, 它是集合 $C$ 的元素, 因此存在某个正整数 $m$,使得 $\beta_{m}=\left(q_{1}, q_{2}, \ldots, q_{99}\right)$. 这时对 $k=1,2, \ldots, 100$, 我们有 $f_{m}\left(q_{k}\right)=k$, 即分类方案 $f_{m}$ 将素数 $q_{k}$ 被分在第 $k$ 类，
同时我们取

$$
a_{k}=q_{k} q_{(k+1)} q_{(k+2)} \cdots q_{(k+m-1)} \in H_{m}
$$

是 $S$ 中的 $m$ 个不同素数的乘积, 满足 $a_{k}$ 的最小质因数为 $q_{k}$, 因而被分在第 $k$类, 即 $a_{k} \in A_{k},(k=1,2, \ldots, 100)$ 满足题意.

