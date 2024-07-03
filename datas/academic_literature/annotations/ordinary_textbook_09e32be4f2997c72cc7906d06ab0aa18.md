数学新星网 关教师专栏

www.nsmath.cn/jszl

# 2021 年哈佛一麻省数学竞赛春季赛试题解析 

石泽晖

(长春吉大附中实验学校, 130021)

本文给出 2021 年哈佛一麻省数学竞赛 (HMMT) 春季赛试题的解析和简评.该比赛时间为 2021 年 3 月 6 日, 试题新颖而有趣, 题目总体难度区分度高、梯度明显, 其中第 $1,2,3$ 题较为简单, 第 $5,6,7$ 题适合作为联赛训练题, 第 $4,8,9,10$题适合作为 $\mathrm{CMO}$ 训练题. 本文的不当之处还请读者批评指正.

## I. 试 题

1. 已知正整数 $a, b$ 满足 $a>b, \sqrt{\sqrt{a}+\sqrt{b}}+\sqrt{\sqrt{a}-\sqrt{b}}$ 为整数.

(1) $\sqrt{a}$ 是否一定为整数?

(2) $\sqrt{b}$ 是否一定为整数?

2. 直角 $\triangle A B C$ 中, $\angle A=90^{\circ}$, 圆 $\omega$ 的圆心在 $B C$ 上, 与 $A B$ 切于点 $D$, 与 $A C$ 切于点 $E$. 已知 $\omega$ 与 $B C$ 交于两点 $F, G$, 且 $F$ 在线段 $B G$ 上, 直线 $D G, E F$交于点 $X$. 求证: $A X=A D$.
3. 已知 $m$ 为正整数, 证明: 存在正整数 $n$, 使得 $2 m+1$ 个整数 $2^{n}-m$, $2^{n}-(m-1), \cdots, 2^{n}+(m-1), 2^{n}+m$ 均为正合数.
4. 已知 $n, k$ 为正整数, 设

$S=\left\{\left(a_{1}, a_{2}, \cdots, a_{k}\right) \in \mathbb{Z}^{k} \mid 0 \leq a_{k} \leq \cdots \leq a_{1} \leq n, a_{1}+\cdots+a_{k}=k\right\}$.

求值 (用 $n, k$ 表示):

$$
\sum_{\left(a_{1}, a_{2}, \cdots, a_{k}\right) \in S} \mathrm{C}_{n}^{a_{1}} \cdot \mathrm{C}_{a_{1}}^{a_{2}} \cdot \mathrm{C}_{a_{2}}^{a_{3}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}}
$$

5. 一个凸多面体的每个面都是全等的三角形, 且这个三角形的三个内角的度数为 $36^{\circ}, 72^{\circ}$ 和 $72^{\circ}$. 求这个多面体的面的个数的最大值.

修订日期: 2021-09-10.

6. 已知函数 $f(x)=x^{2}+x+1$. 求所有的正整数 $n$, 使得对 $n$ 的所有因数 $k$,均有 $f(k)$ 整除 $f(n)$.
7. 在 $\triangle A B C$ 中, $M$ 为 $B C$ 中点, $D$ 为线段 $A M$ 上一点. 在射线 $\overrightarrow{C A}$ 与 $\overrightarrow{B A}$上分别取点 $Y, Z$, 使得 $\angle D Y C=\angle D C B$ 且 $\angle D B C=\angle D Z B$. 求证: $\triangle D Y Z$的外接圆与 $\triangle D B C$ 的外接圆相切.
8. 对任意正实数 $\alpha$, 定义 $\lfloor\alpha \mathbb{N}\rfloor=\{\lfloor\alpha\rfloor \mid m \in \mathbb{N}\}$. 已知 $n$ 为正整数. 集合 $S \subseteq\{1,2, \cdots, n\}$ 满足: 对任意 $\beta>0$, 若 $S \subseteq\lfloor\beta \mathbb{N}\rfloor$, 则 $\{1,2, \cdots, n\} \subseteq\lfloor\beta \mathbb{N}\rfloor$.求 $|S|$ 的最小值.
9. 已知非等腰 $\triangle A B C$ 外心为 $O$, 内心为 $I$. 内切圆 $\omega$ 与边 $B C, C A, A B$分别切于点 $D, E, F$. 过 $D$ 作 $D P \perp E F$ 于 $P$, 直线 $D P$ 与 $\omega$ 交于点 $Q$. 过 $A$ 作 $B C$ 的垂线与直线 $O I$ 交于点 $T$. 若 $O T / / B C$, 证明: $P Q=P T$.
10. 已知 $n>1$ 为正整数, 将一个 $n \times n$ 的网格表的所有单元格染成黑色或白色, 并满足以下条件:

(1) 对任意两个黑色单元格, 可以从其中一个出发, 途经若干黑色单元格,到达另一个. (这里经过的每个单元格必须与上一个单元格有公共边)

(2) 对任意两个白色单元格, 可以从其中一个出发, 途经若干白色单元格,到达另一个. (同样的, 这里经过的每个单元格必须与上一个单元格有公共边)

(3) 任意一个 $2 \times 2$ 的小方块中, 至少有 1 个黑色单元格, 也至少有 1 个白色单元格.

求黑色单元格与白色单元格的个数之差的最大值 (用 $n$ 表示).

## II. 解答与评注

题 1 已知正整数 $a, b$ 满足 $a>b, \sqrt{\sqrt{a}+\sqrt{b}}+\sqrt{\sqrt{a}-\sqrt{b}}$ 为整数.

(1) $\sqrt{a}$ 是否一定为整数?

(2) $\sqrt{b}$ 是否一定为整数?

解 (1) 先证明下面的引理.

引理 设 $x, y \in \mathbb{Z}^{+}, \sqrt{x}+\sqrt{y} \in \mathbb{Z}$, 则 $\sqrt{x}, \sqrt{y} \in \mathbb{Z}$.

证明 假设 $\sqrt{x} \notin \mathbb{Z}$, 设 $\sqrt{x}+\sqrt{y}=n\left(n \in \mathbb{Z}^{+}\right)$, 则 $y=(n-\sqrt{x})^{2}=$ $n^{2}+x-2 n \sqrt{x} \notin \mathbb{Z}$, 矛盾! 故 $\sqrt{x} \in \mathbb{Z}$, 同理 $\sqrt{y} \in \mathbb{Z}$, 引理得证.

回到原题.
将原式平方, 有 $2 \sqrt{a}+2 \sqrt{a-b} \in \mathbb{Z}$, 由引理知: $\sqrt{4 a}, \sqrt{4(a-b)} \in \mathbb{Z}$. 由 $a \in Z^{+}, \sqrt{a} \in \mathbf{Q}$, 知 $\sqrt{a} \in \mathbb{Z}$.

(2) 取 $a=256, b=252$, 则

原式 $=\sqrt{16+6 \sqrt{7}}+\sqrt{16-6 \sqrt{7}}=3+\sqrt{7}+3-\sqrt{7}=6 \in \mathbb{Z}$,

此时 $\sqrt{b} \notin \mathbb{Z}$.

综上, $\sqrt{a}$ 一定为整数, $\sqrt{b}$ 不一定为整数.

评注 这是一道简单的代数题, 不难发现解析中的引理, 是解决该题 (1) 的关键. 而 $\sqrt{b} \notin \mathbb{Z}$ 的反例在分析过程中容易得出，另外 $a=36, b=32$ 也是反例之一.

题 2 直角 $\triangle A B C$ 中, $\angle A=90^{\circ}$, 圆 $\omega$ 的圆心在 $B C$ 上, 与 $A B$ 切于点 $D$, 与 $A C$ 切于点 $E$. 已知 $\omega$ 与 $B C$ 交于两点 $F, G$, 且 $F$ 在线段 $B G$ 上, 直线 $D G, E F$ 交于点 $X$. 求证: $A X=A D$.

证明 (卢典) 设 $\omega$ 圆心为 $O$, 由 $D, E$ 为切点得 $O D \perp A B, O E \perp A C$, 故四边形 $A D O E$ 为正方形. 因此: $\angle D X E=\angle F X G=180^{\circ}-\angle E F G-\angle D G F$ $=180^{\circ}-\frac{1}{2}(\angle E O G+\angle D O F)=180^{\circ}-\frac{1}{2}\left(180^{\circ}-\angle D O E\right)=135^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_dd25aabe4ca9932b3f52g-03.jpg?height=357&width=623&top_left_y=1506&top_left_x=722)

在 $D G$ 上, 取点 $X^{\prime} \neq D$, 使 $A X^{\prime}=A D$, 则 $A X^{\prime}=A D=A E$, 有:

$$
\begin{aligned}
\angle D X^{\prime} E & =\angle D X^{\prime} A+\angle E X^{\prime} A=\angle X^{\prime} D A+\angle X^{\prime} E A \\
& =\frac{1}{2}\left(\angle D X^{\prime} E+\angle X^{\prime} D A+\angle X^{\prime} E A\right) \\
& =\frac{1}{2}\left(360^{\circ}-\angle B A C\right)=135^{\circ},
\end{aligned}
$$

故 $X^{\prime}=X, A X=A D$.

评注 这是一道简单的几何题, 图形中存在直角与切线的特殊构形, 故处理方式较多, 另外一个方法是取弧 $F D E G$ 的中点 $M$, 容易证明 $D X E M$ 为平行四边形, 进而证明 $\triangle A X D \cong \triangle O M E$.
题 3 已知 $m$ 为正整数, 证明: 存在正整数 $n$, 使得 $2 m+1$ 个整数 $2^{n}-m$, $2^{n}-(m-1), \cdots, 2^{n}+(m-1), 2^{n}+m$ 均为正合数.

证明 只需考虑 $2^{n}+c_{i}(i=1,2, \cdots, l)$, 其中 $c_{i}$ 为 $-m,-(m-1), \cdots, m$中的奇数, $l=2\left\lceil\frac{\mathrm{m}}{2}\right\rceil$.

先取 $n_{0}$ 使 $2^{n_{0}}+c_{i}>1$, 则存在素数 $p_{i} \mid 2^{n_{0}}+c_{i}, i=1,2, \cdots, l\left(p_{i} \neq 2\right)$.

再取

$$
n=n_{0}+\prod_{i=1}^{l}\left(p_{i}-1\right)
$$

此时, 由 Fermat 小定理, $2^{p_{i}-1} \equiv 1\left(\bmod p_{i}\right)$, 从而 $2^{n} \equiv 2^{n_{0}}\left(\bmod p_{i}\right)$, 因此 $p_{i} \mid 2^{n}+c_{i}$, 且 $2^{n}+c_{i}>2^{n_{0}}+c_{i} \geq p_{i}, 2^{n}+c_{i}$ 为合数. 命题得证.

评注 这是一道简单的数论问题, 由于出现 2 的幂, 容易想到利用 Fermat 小定理或 Euler 定理来对幕次进行合理构造。

题 4 已知 $n, k$ 为正整数, 设

$$
S=\left\{\left(a_{1}, a_{2}, \cdots, a_{k}\right) \in \mathbb{Z}^{k} \mid 0 \leq a_{k} \leq \cdots \leq a_{1} \leq n, a_{1}+\cdots+a_{k}=k\right\}
$$

求值(用 $n, k$ 表示):

$$
\sum_{\left(a_{1}, a_{2}, \cdots, a_{k}\right) \in S} \mathrm{C}_{n}^{a_{1}} \cdot \mathrm{C}_{a_{1}}^{a_{2}} \cdot \mathrm{C}_{a_{2}}^{a_{3}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}}
$$

解 1 (王孝文) 由组合数定义, 得

$$
\begin{aligned}
\mathrm{C}_{n}^{a_{1}} \cdot \mathrm{C}_{a_{1}}^{a_{2}} \cdot \mathrm{C}_{a_{2}}^{a_{3}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}} & =\frac{n !}{\left(n-a_{1}\right) ! a_{1} !} \cdot \frac{a_{1} !}{\left(a_{1}-a_{2}\right) ! a_{2} !} \cdots \frac{a_{k-1} !}{\left(a_{k-1}-a_{k}\right) ! a_{k} !} \\
& =\frac{n !}{\left(n-a_{1}\right) !\left(a_{1}-a_{2}\right) ! \cdots\left(a_{k-1}-a_{k}\right) ! a_{k} !}
\end{aligned}
$$

设

$$
b_{0}=n-a_{1}, b_{i}=a_{i}-a_{i+1}(i=1,2, \cdots, k-1), b_{k}=a_{k}
$$

则要求 $b_{i} \geq 0, i=0,1, \cdots, k$, 满足

$$
\sum_{i=0}^{k} b_{i}=n, \sum_{i=0}^{k} i b_{i}=\sum_{i=1}^{k-1} i\left(a_{i}-a_{i+1}\right)+k a_{k}=\sum_{i=1}^{k} a_{i}=k
$$

注意到 $\sum_{\substack{\sum b_{i}=n, \sum i b_{i}=k}} \frac{1}{\prod b_{i} !}$ 即为 $f(x, y)=\prod_{i=0}^{k} \sum_{j=0}^{\infty} \frac{\left(x y^{i}\right)^{j}}{j !}$ 中 $x^{n} y^{k}$ 的系数, 利用泰勒展开公式可知:

$$
f(x, y)=\prod_{i=0}^{k} e^{x y^{i}}=e^{x\left(1+y+\cdots+y^{k}\right)}
$$

$$
=\frac{1}{0 !}+\frac{x\left(1+y+\cdots+y^{k}\right)}{1 !}+\cdots+\frac{x^{n}\left(1+y+\cdots+y^{k}\right)^{n}}{n !}+o\left(x^{n}\right),
$$

$\left(1+y+\cdots+y^{k}\right)^{n}$ 中 $y^{k}$ 的系数即 $\left(\frac{1}{1-y}\right)^{n}=\left(\sum_{i=0}^{\infty} y^{i}\right)^{n}$ 中 $y^{k}$ 的系数, $(n-1) !\left(\frac{1}{1-y}\right)^{n}$为 $\frac{1}{1-y}=1+y+y^{2}+\cdots$ 的 $n-1$ 阶导数, 从而 $\left(\frac{1}{1-y}\right)^{n}$ 中 $y^{k}$ 系数为 $\frac{1}{(n-1) !} \cdot \frac{(k+n-1) !}{k !}=$ $\mathrm{C}_{k+n+1}^{n-1}$, 这说明 $f(x, y)$ 中 $x^{n} y^{k}$ 的系数为 $\frac{\mathrm{C}_{k+n+1}^{n-1}}{n !}$, 故:

$$
\sum_{\left(a_{1}, a_{2}, \cdots, a_{k}\right) \in S} \mathrm{C}_{n}^{a_{1}} \cdot \mathrm{C}_{a_{1}}^{a_{2}} \cdot \mathrm{C}_{a_{2}}^{a_{3}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}}=n ! \sum_{\substack{\sum_{i} b_{i}=n \\ \sum i b_{i}=k}} \frac{1}{\prod b_{i} !}=\mathrm{C}_{k+n-1}^{n-1}
$$

解 2 我们从两方面考虑方程 $x_{1}+x_{2}+\cdots+x_{n}=k$ 在 $\mathbb{N}^{n}$ 上的解的个数 $F(n, k)$.

一方面, $F(n, k)$ 亦为 $y_{1}+y_{2}+\cdots+y_{n}=n+k$ 在 $\mathbb{Z}_{+}^{n}$ 上的解的个数. 注意到 $1 \leq y_{1}<y_{1}+y_{2}<\cdots<y_{1}+\cdots+y_{n-1}<y_{1}+\cdots+y_{n}=n+k$, 故我们可通过在 $1 \sim n+k-1$ 中选取 $y_{1}, y_{1}+y_{2}, \cdots, y_{1}+\cdots+y_{n-1}$ 后, 来唯一确定 $y_{1}, y_{2}, \cdots, y_{n}$ （构成一一映射）, 这说明解的个数为 $\mathrm{C}_{n+k-1}^{n-1}$.

另一方面:

$$
k=\sum_{i=1}^{n} x_{n}=\sum_{i=1}^{n} \sum_{j=1}^{x_{i}} 1=\sum_{j=1}^{k} \sum_{x_{i} \geq j}^{x_{i}} 1=\sum_{j=1}^{k}\left|A_{j}\right|
$$

其中 $A_{j}=\left\{i \mid x_{i} \geq j, i=1,2, \cdots, n\right\}$. 记 $a_{j}=\left|A_{j}\right|$, 则有

$$
0 \leq a_{k} \leq \cdots \leq a_{1} \leq n, a_{1}+a_{2}+\cdots+a_{k}=k .
$$

这说明当 $a_{1}, a_{2}, \cdots, a_{k}$ 确定时, 集合 $A_{1}, A_{2}, \cdots, A_{k}$ 的选取可能共有 $\mathrm{C}_{n}^{a_{1}}$. $\mathrm{C}_{a_{1}}^{a_{2}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}}$ 种. 因为 $A_{k} \subseteq A_{k-1} \subseteq \cdots \subseteq A_{1} \subseteq\{1,2, \cdots, n\}$, 此时 $x_{i}$ 唯一确定为 $i$ 在 $A_{j}$ 中出现的总次数, 故解的个数即为 $\sum_{\left(a_{1}, a_{2}, \cdots, a_{k} \in S\right)} \mathrm{C}_{n}^{a_{1}} \cdot \mathrm{C}_{a_{1}}^{a_{2}} \cdot \mathrm{C}_{a_{2}}^{a_{3}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}}$.结合这两方面, 可知

$$
\sum_{\left(a_{1}, a_{2}, \cdots, a_{k}\right) \in S} \mathrm{C}_{n}^{a_{1}} \cdot \mathrm{C}_{a_{1}}^{a_{2}} \cdot \mathrm{C}_{a_{2}}^{a_{3}} \cdots \mathrm{C}_{a_{k-1}}^{a_{k}}=\mathrm{C}_{n+k-1}^{n-1}
$$

评注 这是一道中档难度的组合计数问题, 利用母函数或经典组合模型的传统方法均可解决.

题 5 一个凸多面体的每个面都是全等的三角形, 且这个三角形的三个内角的度数为 $36^{\circ}, 72^{\circ}$ 和 $72^{\circ}$. 求这个多面体的面的个数的最大值.

解 (沈月恒) 设多面体的顶点数, 边数, 面数分别为 $v, e, f$. 我们考虑所有
角度之和 $S$. 一方面, 从每个顶点出发, 由于以任一点为顶点的角度之和为 $36^{\circ}$的倍数, 且小于 $360^{\circ}$, 故至多 $324^{\circ}$; 另一方面, 从每个面出发, 每个面上的三个角度之和为 $180^{\circ}$. 因此

$$
324^{\circ} v \geq S=180^{\circ} f \Rightarrow v \geq \frac{5}{9} f
$$

而每边恰出现于 2 个面上, 每个面上有 3 条边, 故有 $e=\frac{3}{2} f$. 由 Euler 公式可知:

$$
2=v-e+f \geq \frac{5}{9} f-\frac{3}{2} f+f \Rightarrow f \leq 36 .
$$

构造几何体如下: 考虑圆柱与两个圆雉构成的几何体, 其中圆柱的上下底面与圆雉重合. 在上下两个圆雉底面上取正九边形, 并使上下两组点关于圆柱中心成中心对称, 先调节圆雉高使圆雉顶点与底面相邻两点所成三角形各角为 $36^{\circ}, 72^{\circ}, 72^{\circ}$; 再调节圆柱高使一个底面上相邻两点与另一底面上面与这两点等距的点构成 $36^{\circ}, 72^{\circ}, 72^{\circ}$ 的三角形.

此时圆雉上产生 9 个面, 圆柱上产生 18 个面, 得到 36 个面.

评注 这是一道中档偏易的组合几何问题. 由于出现角度, 容易想到利用算两次得到顶点、边数关于面数的关系, 再结合 Euler 公式完成对面数的估计, 本题的构造需要一定表述能力。

题 6 已知函数 $f(x)=x^{2}+x+1$. 求所有的正整数 $n$, 使得对 $n$ 的所有因数 $k$, 均有 $f(k)$ 整除 $f(n)$.

解 (王孝文) 设 $n=p_{1}^{\alpha_{1}} \cdots p_{l}^{\alpha_{l}}$, 若 $\alpha_{1}+\alpha_{2}+\cdots+\alpha_{l} \geq 3$, 不妨设 $p_{1}$ 为 $n$ 最小素因子, 故有 $\left.f\left(\frac{n}{p_{1}}\right) \right\rvert\, f(n)$. 由 $f(x)=x^{2}+x+1$ 可知:

$$
f(n)=n^{2}+n+1<n^{2}+n p_{1}+p_{1}^{2}=f\left(\frac{n}{p_{1}}\right) p_{1}^{2} .
$$

而另一方面:

$$
\begin{aligned}
f\left(\frac{n}{p_{1}}\right)\left(p_{1}^{2}-1\right)-f(n) & <-\frac{n^{2}}{p_{1}^{2}}+\left(p_{1}-1\right) n+p_{1}^{2} \\
& \leq-p_{1} n+\left(p_{1}-1\right) n+p_{1}^{2} \\
& =p_{1}^{2}-n<0 \quad\left(n \geq p_{1}^{3}\right)
\end{aligned}
$$

因此有 $p_{1}^{2}-1<\frac{f(n)}{f\left(\frac{n}{p_{1}}\right)}<p_{1}^{2}$, 这与 $\frac{f(n)}{f\left(\frac{n}{p_{1}}\right)} \in \mathbb{Z}$ 矛盾! 这说明 $\alpha_{1}+\alpha_{2}+\cdots+\alpha_{l} \leq 2$.若 $n=1$, 符合要求;

若 $n=p$, 则 $f(1)=3 \mid f(p)=p^{2}+p+1, p \equiv 1(\bmod 3)$;
若 $n=p^{2}$, 同理可得 $p^{2} \equiv 1(\bmod 3)$. 此时, $f(1)=3 \mid f\left(p^{2}\right)$, 且

$$
\begin{aligned}
f\left(p^{2}\right) & =p^{4}+p^{2}+1 \\
& =p\left(1+(p-1)\left(p^{2}+p+1\right)\right)+p^{2}+1 \\
& \equiv p+p^{2}+1 \equiv 0 \quad(\bmod f(p)),
\end{aligned}
$$

符合要求;

若 $n=p q$, 此时

$$
\begin{aligned}
f(p q) & =p^{2} q^{2}+p q+1 \\
& \equiv p^{2}(-q-1)+p q+1 \\
& =(1-p)(p q+p+1) \quad\left(\bmod q^{2}+q+1\right)
\end{aligned}
$$

若 $f(q)\left|f(p q), q^{2}+q+1\right|(1-p)(q-p)$, 则 $q^{2}+q+1 \mid(1-p)(p q+q+1)$, 从而有 $q^{2}+q+1 \mid(1-p)\left(p q-q^{2}\right)$,

注意到 $\left(q^{2}+q+1, q\right)=1$, 故 $q^{2}+q+1 \mid(1-p)(p-q)$. 而

$$
0<(p-1)(q-p)=p q-q-p^{2}+p<q^{2}+q+1
$$

矛盾!

综上可知: $n=1, n=p, p \equiv 1(\bmod 3)$ 或 $n=p^{2}, p \neq 3, p$ 为素数.

评注 这是一道中档难度的数论问题, 利用常规的模分析与大小估计可知 $\Omega(n) \leq 2$, 再对其逐一讨论即可.

题 7 在 $\triangle A B C$ 中, $M$ 为 $B C$ 中点, $D$ 为线段 $A M$ 上一点. 在射线 $\overrightarrow{C A}$与 $\overrightarrow{B A}$ 上分别取点 $Y, Z$, 使得 $\angle D Y C=\angle D C B$ 且 $\angle D B C=\angle D Z B$. 求证: $\triangle D Y Z$ 的外接圆与 $\triangle D B C$ 的外接圆相切.

![](https://cdn.mathpix.com/cropped/2024_02_26_dd25aabe4ca9932b3f52g-07.jpg?height=574&width=428&top_left_y=1940&top_left_x=814)

证明 (沈月恒) 如图, 设 $U=A B \cap C D, V=A C \cap B D$, 由塞瓦定理, 有
$\frac{A U}{U B} \cdot \frac{B M}{M C} \cdot \frac{C V}{V A}=1$, 又 $B M=M C$, 则 $\frac{A U}{U B}=\frac{A V}{V C}$, 故 $U V / / B C$, 从而

$$
\angle D U V=\angle D C B=\angle D Y V
$$

这说明 $U, D, V, Y$ 四点共圆.

同理 $U, D, V, Z$ 共圆, 进而 $U, D, V, Z, Y$ 五点共圆,

$$
\angle C D V=\angle D C B+\angle D B C=\angle D C B+\angle D V U,
$$

这表明 $\triangle D U V$ 外接圆 (即 $\triangle D Y Z$ 的外接圆) 与 $\triangle D B C$ 外接圆相切.

评注 这是一道中档难度的几何问题, 在能做出较为标准的图形时, 可以发现延长 $B D, C D$ 与对边的交点有较多的性质, 然后通过简单的导角可得相切结论.

题 8 对任意正实数 $\alpha$, 定义 $\lfloor\alpha \mathbb{N}\rfloor=\{\lfloor\alpha m\rfloor \mid m \in \mathbb{N}\}$. 已知 $n$ 为正整数. 集合 $S \subseteq\{1,2, \cdots, n\}$ 满足: 对任意 $\beta>0$, 若 $S \subseteq\lfloor\beta \mathbb{N}\rfloor$, 则 $\{1,2, \cdots, n\} \subseteq$ $\lfloor\beta \mathbb{N}\rfloor$. 求 $|S|$ 的最小值.

解 (王孝文) $S$ 至少含 $\left\lfloor\frac{n}{2}\right\rfloor+1$ 个元素.

一方面, 取 $S=\left\{\left\lceil\frac{n}{2}\right\rceil,\left\lceil\frac{n}{2}\right\rceil+1, \cdots, n\right\}$. 若 $0<\beta \leq 1$, 显然成立. 不妨设 $\beta>1, n \geq 3$.

若存在 $1 \sim n$ 之间的整数 $i \notin\lfloor\beta \mathbb{N}\rfloor$, 则对任意整数 $a$, 必有 $a, a+1, \cdots, a+i$不同时在 $\lfloor\beta \mathbb{N}\rfloor$ 中. 事实上, 若不然, 则存在整数 $m$, 使得 $a=\lfloor m \beta\rfloor, a+1=$ $\lfloor(m+1) \beta\rfloor, \cdots, a+i=\lfloor(m+i) \beta\rfloor$, 此时 $i<i \beta<i+1,\lfloor i \beta\rfloor=i \in\lfloor\beta \mathbb{N}\rfloor$, 矛盾!

由 $S$ 的取法以及 $S \subseteq\lfloor\beta \mathbb{N}\rfloor$, 存在连续 $k\left(1 \leq k \leq\left\lfloor\frac{n}{2}\right\rfloor+1\right)$ 个整数同时在 $\lfloor\beta \mathbb{N}\rfloor$ 中, 这说明 $1,2, \cdots,\left\lfloor\frac{n}{2}\right\rfloor \in\lfloor\beta \mathbb{N}\rfloor$, 故 $\{1,2, \cdots, n\} \subseteq\lfloor\beta \mathbb{N}\rfloor$.

另一方面, 若 $|S| \leq \frac{n}{2}$, 则存在 $k \notin S, \frac{n}{2} \leq k \leq n$, 取 $\beta=\frac{k+1}{k}$, 则

$$
\lfloor\beta m\rfloor=\left\{\begin{array}{l}
m, m=1,2, \cdots, k-1 \\
m+1, m=k, k+1, \cdots, n-1
\end{array},\right.
$$

此时, $1 \sim n$ 中只有 $k$ 不在 $\lfloor\beta \mathbb{N}\rfloor$ 中, $S \subseteq\lfloor\beta \mathbb{N}\rfloor$ 但 $\{1,2, \cdots, n\} \not \subset\lfloor\beta \mathbb{N}\rfloor$, 矛盾!

结合两方面可知: $S$ 至少含 $\left\lfloor\frac{n}{2}\right\rfloor+1$ 个元素.

评注 这是一道中档难度的组合题, 由于 $\lfloor\beta \mathbb{N}\rfloor$ 结构并不直观, 可先通过对 $n$ 较小的情形猜到答案, 然后发现 $S$ 取较大数时为最优情况, 在此基础上再给出构造与证明是容易的.
题 9 已知非等腰 $\triangle A B C$ 外心为 $O$, 内心为 $I$. 内切圆 $\omega$ 与边 $B C, C A, A B$分别切于点 $D, E, F$. 过 $D$ 作 $D P \perp E F$ 于 $P$, 直线 $D P$ 与 $\omega$ 交于点 $Q$. 过 $A$ 作 $B C$ 的垂线与直线 $O I$ 交于点 $T$. 若 $O T / / B C$, 证明: $P Q=P T$.

![](https://cdn.mathpix.com/cropped/2024_02_26_dd25aabe4ca9932b3f52g-09.jpg?height=485&width=602&top_left_y=474&top_left_x=727)

证明 1 (王孝文) 首先证明 $\triangle D E F$ 的垂心 $H$ 在直线 $O I$ 上.

事实上, 以 $\odot I$ 为基圆作反演变换. 则 $A, B, C$ 分别变换为 $E F, D F, D E$ 中点 $A^{\prime}, B^{\prime}, C^{\prime}$, 所以 $\triangle D E F$ 的九点圆圆心在直线 $O I$ 上. 由欧拉线可知对 $\triangle D E F$而言, 其外心 $I$ 、垂心 $H$ 、九点圆圆心共线, 这说明 $H$ 也在直线 $O I$ 上.

其次证明 $A 、 Q 、 T$ 三点共线.

事实上, 设 $D$ 关于 $\odot I$ 对径点为 $K, \triangle A B C$ 的 $A$ 旁切圆与 $B C$ 切点为 $L$,过点 $Q$ 作 $\odot I$ 的切线, 分别交 $A B, A C$ 于点 $B_{1}, C_{1}$. 则由位似可知 $A, K, L$ 共线, 又 $K D \perp D L$, 故 $K L$ 的中点必在 $D K, D L$ 的中垂线上 ( $D L$ 中垂线即 $B C$中垂线), 这说明 $K L$ 的中点即为 $\triangle A B C$ 的外心 $O$, 从而 $A, O, L$ 共线. 注意到 $\triangle A B_{1} C_{1} \sim \triangle A C B$, 而 $Q, L$ 为对应点 (旁切圆切点), 故 $\angle C_{1} A Q=\angle B A L=$ $\angle C A T$, 从而 $A, Q, T$ 共线.

最后, 由 $\triangle D E F$ 的垂心 $H$ 在直线 $O I$ 上可知, $D Q$ 与 $O I$ 的交点即为 $H$,由垂心性质可知 $P$ 为 $Q H$ 中点; 而由 $A 、 Q 、 T$ 三点共线可知, $Q T \perp H T$. 故 $P H=P T=P Q$, 证毕.

证明 2 (沈月恒) 如图, 设 $Q D$ 与 $O T$ 交于点 $S$. 由条件

$$
O I / / B C \Leftrightarrow d(O, B C)=d(I, B C) \Leftrightarrow R \cos A=r,
$$

再结合三角恒等式:

$$
\frac{r}{R}=\cos A+\cos B+\cos C-1 \Rightarrow \cos B+\cos C=1 .
$$

由于 $A I=\frac{r}{\sin \frac{A}{2}}$, 且

$$
D Q=2 r \sin \angle D F Q=2 r \sin (\angle E F D+\angle E D Q)
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_dd25aabe4ca9932b3f52g-10.jpg?height=491&width=642&top_left_y=234&top_left_x=684)

$$
=2 r \sin \left(90^{\circ}-\frac{C}{2}+\frac{B}{2}\right)=2 r \cos \left(\frac{C}{2}-\frac{B}{2}\right),
$$

故

$$
\begin{aligned}
D Q=A I & \Leftrightarrow 2 \sin \frac{A}{2} \cos \left(\frac{C}{2}-\frac{B}{2}\right)=1 \\
& \Leftrightarrow 2 \cos \left(\frac{C}{2}+\frac{B}{2}\right) \cos \left(\frac{C}{2}-\frac{B}{2}\right)=1 \\
& \Leftrightarrow \cos B+\cos C=1
\end{aligned}
$$

成立. 由于 $D Q \perp E F, A I \perp E F$, 故 $D Q / / A I$, 因此 $A I D Q$ 为平行四边形, 从而 $I D / / A Q$. 又 $I D / / A T$, 故 $Q$ 在 $A T$ 上.

注意到 $Q T / / I D$, 有 $\frac{Q S}{S D}=\frac{Q T}{I D}$. 又

$$
\begin{aligned}
\angle Q I D & =2 \angle Q F D=2\left(\angle E F D+90^{\circ}-\angle F E D\right) \\
& =2\left(90^{\circ}-\frac{C}{2}+90^{\circ}-\left(90^{\circ}-\frac{B}{2}\right)\right) \\
& =180^{\circ}-(B-C),
\end{aligned}
$$

从而

$$
\begin{aligned}
Q S & =D Q \cdot \frac{Q T}{I D+Q T}=A I \cdot \frac{r \sin \angle Q I T}{r+r \sin \angle Q I T} \\
& =\frac{r}{\sin \frac{A}{2}} \cdot \frac{\cos \left(180^{\circ}-\angle Q I D\right)}{1+\cos \left(180^{\circ}-\angle Q I D\right)} \\
& =\frac{r}{\sin \frac{A}{2}} \cdot \frac{\cos (B-C)}{1+\cos (B-C)} .
\end{aligned}
$$

又 $\angle Q F E=90^{\circ}-\angle F E D=90^{\circ}-\left(90^{\circ}-\frac{B}{2}\right)=\frac{B}{2}$, 故

$$
\begin{aligned}
P Q & =F P \tan \frac{B}{2}=D F \sin \frac{C}{2} \tan \frac{B}{2} \\
& =2 r \cos \frac{B}{2} \sin \frac{C}{2} \tan \frac{B}{2}=2 r \sin \frac{C}{2} \sin \frac{B}{2},
\end{aligned}
$$

故

$$
\begin{aligned}
& 2 P Q=Q S \\
\Leftrightarrow & 4 \sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}=\frac{\cos (B-C)}{1+\cos (B-C)} \\
\Leftrightarrow & \cos A+\cos B+\cos C-1=\frac{\cos (B-C)}{1+\cos (B-C)} \\
\Leftrightarrow & \cos A(1+\cos (B-C))=\cos (B-C) \\
\Leftrightarrow & \cos (B-C)+\cos (B-C) \cos (B+C)+\cos (B+C)=0 \\
\Leftrightarrow & 2 \cos B \cos C+\cos ^{2} B \cos ^{2} C-\sin ^{2} B \sin ^{2} C=0 \\
\Leftrightarrow & 2 \cos B \cos C+\cos ^{2} B \cos ^{2} C-\left(1-\cos ^{2} B\right)\left(1-\cos ^{2} C\right)=0 \\
\Leftrightarrow & (\cos B+\cos C)^{2}=1 .
\end{aligned}
$$

上式显然成立. 这说明 $P$ 是 $S Q$ 中点, 结合上 $\triangle Q S T$ 为直角三角形可知: $P T=P Q$.

评注 这是一道中档偏难的几何问题. 法一采取纯几何方法, 其中反演与位似较为复杂, 但属于经典模型. 法二采取三角计算方法, 需熟悉图形中的基本线段的三角表示. 本题中存在常见的基本图形, 对积累较多, 观点较高的同学而言,本题可能并不困难.

题 10 已知 $n>1$ 为正整数, 将一个 $n \times n$ 的网格表的所有单元格染成黑色或白色, 并满足以下条件:

(1) 对任意两个黑色单元格，可以从其中一个出发，途经若干黑色单元格，到达另一个. (这里经过的每个单元格必须与上一个单元格有公共边)

(2) 对任意两个白色单元格，可以从其中一个出发，途经若干白色单元格，到达另一个. (同样的, 这里经过的每个单元格必须与上一个单元格有公共边)

(3) 任意一个 $2 \times 2$ 的小方块中，至少有 1 个黑色单元格，也至少有 1 个白色单元格.

求黑色单元格与白色单元格的个数之差的最大值 (用 $n$ 表示).

解 (王孝文) 所求最大值为 $\left\{\begin{array}{l}2 n+1,2 \nmid n \\ 2 n-2,2 \mid n\end{array}\right.$.

首先, 我们给出该上界的证明.

将网格表不在边界上的 $(n-1)^{2}$ 个格线交点进行标记, 考虑依次将一些方格染白, 要求新染的白格与一个已染的白格有公共边 (由条件 2 , 这可以做到).
第一个白格至多覆盖 4 个标记点, 之后加入的白格每个至多再覆盖 2 个未覆盖的标记点.

由条件 3 , 每个 $2 \times 2$ 的小方块的中心一定被白格覆盖, 故白格至少 $\frac{(n-1)^{2}-2}{2}$ 个. 同理黑格也至少 $\frac{(n-1)^{2}-2}{2}$ 个. 这说明黑格与白格数之差至多为 $n^{2}-2 \cdot \frac{(n-1)^{2}-2}{2}=2 n+1$.

注意到 $2 \mid n$ 时, 黑白格数之差必为偶数, 从而差至多 $2 n$, 此时的取等要求初始白格覆盖 4 个标记点, 其它白格中, 有一个覆盖 1 个标记点, 其余覆盖 2 个 (因为初始方格不能覆盖 3 个标记点).

我们考虑覆盖一个标记点的方格. 若该方格出现在 $n \times n$ 的网格表内部 (即去除边界的 $(n-2) \times(n-2)$ 的网格), 则它恰好与 2 个已染的连通的白格有公共边, 此时必存在一个全由白格构成的圈.

若圈内无黑格, 则圈内全为白格, 此时必有一个 $2 \times 2$ 的全为白格的小方块,与条件 3 矛盾; 若圈内有黑格, 由条件 1 可知圈外无黑格, 故圈外所有方格均为白格, 特别的, $n \times n$ 网格表 4 个角上的方格均为白格, 这些白格在上述染法中,未能新覆盖任何标记点, 矛盾. 若覆盖一个标记点的方格出现在 $n \times n$ 的网格表边界上, 则在边界上且与内部相邻的方格, 在染色时, 并未新覆盖任何标记点,矛盾. 这说明上述取等条件无法取到. 又黑白格数之差必为偶数, 故至多 $2 n-2$.

其次, 我们给出该上界的构造.

将 $n \times n$ 网格表中的 $n^{2}$ 个小方格, 标记坐标 $(x, y)(1 \leq x, y \leq n)$ :

若 $n=2$, 将坐标为 $(1,1)$ 的小方格染为黑色, 其余方格染为白色;

若 $n$ 为奇数, 将坐标为 $(i, 2)(i=2,3, \cdots, n-1) 、(2 k, j)\left(k=1,2, \cdots, \frac{n-1}{2}\right.$, $j=3,4, \cdots, n-1)$ 的小方格染为黑色, 其余方格染为白色;

若 $n$ 为大于 2 的偶数, 将坐标为 $(i, 2)(i=2,3, \cdots, n) 、(2 k, j)(k=$ $\left.1,2, \cdots, \frac{n}{2}-1, j=3,4, \cdots, n-1\right) 、(n, 3) 、(n-1,2 k+3)\left(k=1,2, \cdots, \frac{n}{2}-2\right)$的小方格染为黑色, 其余方格染为白色.

|  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ |  |
|  | $\mathrm{B}$ |  |  |  |  |  |
|  | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ |  |
|  | $\mathrm{B}$ |  |  |  |  |  |
|  | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ |  |
|  |  |  |  |  |  |  |


|  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ |  |
|  | $\mathrm{B}$ |  |  |  |  |  |  |
|  | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ |  |
|  | $\mathrm{B}$ |  |  |  |  |  |  |
|  | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ | $\mathrm{B}$ |  |
|  | $\mathrm{B}$ |  |  | $\mathrm{B}$ |  | $\mathrm{B}$ |  |
|  | $\mathrm{B}$ | $\mathrm{B}$ |  |  |  |  |  |

上图为 $n=7 、 n=8$ 时的染色情形, 标“ $\mathrm{B}$ ”表示染为黑色, 其余为白色.
评注 这是一道中档偏难的组合问题. 通过对 $n$ 的较小值进行尝试可推知答案与构造, 且奇偶是有差别的. 证明时可先考虑较易的奇数情形, 再对其取等条件进行精细处理, 即可得到偶数情形的证明. 该解答中的构造借鉴了官方解答的写法。

