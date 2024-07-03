# 2021 年伊朗 TST 试题解答与评析 

马晓博 马超航

(郑州市第一中学, 450006)

本次伊朗集训队测试题 (共 2 次 4 天 12 道) 总体难度中等偏难, 试题质量中等偏上. 这次考试题目亮眼之处在于将一些经典的证明方法巧妙地融入到题目中并加以很好的隐蔽性, 使题目的解答相当巧妙, 可以让读者反复玩味; 不足之处是题目之间难度差异过大, 一些试题如 $5 、 12$, 其难度不符合集训队测试题难度标准. 希望读者能够认真思考每一道题并继续探索.

## I. 试 题

1. 锐角非等腰 $\triangle A B C$ 中, $\angle B A C$ 的外角平分线与 $B C$ 交于 $X$, 过 $B, C$ 作 $\triangle A B C$ 外接圆切线交于点 $D$, 且二者分别与过 $X$ 的一条直线交于 $Y, Z$. 已知 $\triangle A Y B$ 的外接圆与 $\triangle A Z C$ 的外接圆交于 $N$, 求证: 直线 $N D$ 平分 $\angle Y N Z$.



2. 简单连通图 $G$ 中, 设度数为 $i$ 的顶点个数为 $x_{i}$. 设 $d>3$ 为 $G$ 中最大的度数. 求证: 若

$$
x_{d} \geq x_{d-1}+2 x_{d-2}+\cdots+(d-1) x_{1},
$$

修订日期: 2022-05-31.
则必然存在一个度数为 $d$ 的点, 使得移除这个点之后, $G$ 中剩下的点和线段仍组成一个连通图.

3. 四个正整数 $a, b, c, d$ 满足 $a b c d \neq 1$, 且它们两两互素. 完全积性函数 $f, g: \mathbb{N} \rightarrow\{0,1\}$ 满足对任意正整数 $n$, 均有

$$
f(a n+b)=g(c n+d) .
$$

证明以下命题中至少有一个成立:

(i) 对任意的正整数 $n, f(a n+b)=g(c n+d)=0$;

(ii) 存在正整数 $k$, 使得对任意满足 $(n, k)=1$ 的正整数 $n$, 均有 $g(n)=$ $f(n)=1$.

注: 若函数 $f(x)$ 满足对任意的正整数 $a, b$, 均有 $f(a b)=f(a) f(b)$, 就称 $f(x)$ 为完全积性函数.

4. 设 $\Omega(n), \omega(n)$ 分别为正整数 $n$ 的最大素因数和最小素因数. 阿里热扎和阿明玩一个游戏. 首先, 阿里热扎选定 1400 个整系数多项式, 阿明从中选择 700 个, 组成集合 $A$, 另外 700 个多项式组成集合 $B$. 若对于任意的 $n$, 都有下式成立,

$$
\max _{P \in A}(\Omega(P(n))) \geq \min _{P \in B}(\omega(P(n))),
$$

则阿明获胜. 若阿明无法选出这样的集合 $A$, 则阿里热扎获胜. 问谁有必胜策略?

5. 若三个实数中, 其中一个是另外两个数的平均数, 就称这是一个“好的”三元数组. 已知 $2 k+1$ 个互异的实数可以组成 $k^{2}$ 个 “好的”三元数组. 证明:可以把这 $2 k+1$ 个数划分为两个部分, 每部分都是等差数列, 且公差相同.
6. 在 $\triangle A B C$ 的欧拉线上取一点 $D$, 且 $D$ 在三角形内部. 直线 $B D, C D$ 分别和边 $A C, A B$ 交于 $E, F$. 在直线 $A D$ 上取点 $X$, 使得 $\angle E X F=180^{\circ}-\angle A$,且 $A, X$ 在直线 $E F$ 同侧. $\triangle C X F, \triangle B X E$ 的外接圆再次相交于点 $P$. 直线 $X P, E F$ 交于点 $K$. 求证: $A K \perp B C$.
7. 在一个无限大的网格表中放置若干正整数, 使得每个单元格中的数字等于它的相邻单元格中含有与其相同数字的单元格的个数. 这里的相邻指有公共顶点. 求这个网格表中互异的数字个数的最大值.
8. 求所有的函数 $f: \mathbb{N} \rightarrow \mathbb{N}$, 使得对任意的正整数 $m, n$, 均有

$$
f(n)+1400 m^{2} \mid n^{2}+f(f(m)) .
$$



9. 求证: 存在两个互素的整系数多项式 $P(x), Q(x)$ 以及一个实数 $u>0$,使得: 若正整数 $a, b, c, d$ 满足

则 $b P\left(\frac{a}{c}\right)=d Q\left(\frac{a}{c}\right)$.

$$
\left|\frac{a}{c}-1\right|^{2021} \leq \frac{u}{|d||c|^{1010}},\left|\left(\frac{a}{c}\right)^{2020}-\frac{b}{d}\right|<\frac{u}{|d||c|^{1010}}
$$

注：两个多项式互素，指这两个多项式没有相同的实根.

10. 求所有函数 $f: \mathbb{N} \rightarrow \mathbb{R}$, 使得对任意的正整数 $a, b, c$, 均有

$$
f(a c)+f(b c)-f(c) f(a b) \geq 1 .
$$

11. 在非等腰梯形的四边形 $A B C D$ 内部取一点 $X$, 使得 $\angle A X D+$ $\angle B X C=180^{\circ}$. 过 $D$ 作 $A X$ 垂线, 与 $\angle A B X$ 平分线交于点 $K$, 过 $A$ 作 $D X$ 垂线, 与 $\angle D C X$ 平分线交于点 $L$, 已知 $B K \perp C X, C L \perp B X, \triangle A D X$ 的外心在直线 $K L$ 上. 求证: $K L \perp A D$.



12. 对一个基数为 $3 n$ 的集合, 我们用八种颜色对其所有基数为 $n$ 的子集染色. 求证: 存在一种染色方法, 使得不存在 3 个同色的子集 $A, B, C$, 满足:

$$
|A \cap B| \leq 1,|A \cap C| \leq 1,|B \cap C| \leq 1
$$

## II. 解答与评注

题 1 锐角非等腰 $\triangle A B C$ 中, $\angle B A C$ 的外角平分线与 $B C$ 交于 $X$, 过 $B, C$作 $\triangle A B C$ 外接圆切线交于点 $D$, 且二者分别与过 $X$ 的一条直线交于 $Y, Z$. 已知 $\triangle A Y B$ 的外接圆与 $\triangle A Z C$ 的外接圆交于 $N$, 求证: 直线 $N D$ 平分 $\angle Y N Z$.



证明 (段毅果) 如图, 设 $B X$ 交圆 $A B Y$ 于 $P$, 交圆 $A C Z$ 于 $Q$, 连接 $N Q, N P, A N, A Y, A P$. 作 $\angle Y N Z$ 平分线交 $Y Z$ 于 $T$. 只需证明 $T, N, D$ 共线.由

$$
\angle A N Z=180^{\circ}-\angle A C B-\angle B C Z=\angle A B C=\angle A B P=\angle A N P
$$

故 $N, Z, P$ 共线, 同样 $N, Y, Q$ 共线.

根据 $\angle A Y B=\angle A P B$ 以及 $\angle A B Y=\angle A C P$ 可得 $\triangle A B Y \sim \triangle A C P$. 根据 $\angle Y B C=\angle Z C B$ 以及 $\angle N Q C=\angle N A C=\angle C Z P$ 可得 $\triangle B Q Y \sim \triangle C Z P$,则有

$$
\frac{B Q}{C Z}=\frac{B Y}{C P}, \frac{B Y}{C P}=\frac{A B}{A C}
$$

又 $A X$ 外平分 $\angle B A C$ 可得 $\frac{A B}{A C}=\frac{B X}{C X}$.

于是

$$
\frac{B Q}{C Z}=\frac{B Y}{C P}=\frac{A B}{A C}=\frac{B X}{C X}
$$

直线 $Y Z X$ 截取 $\triangle D B C$, 由梅涅劳斯定理得

$$
\frac{D Y}{Y B} \cdot \frac{B X}{X C} \cdot \frac{C Z}{Z D}=1
$$

结合 $\frac{B Q}{C Z}=\frac{B X}{C X}$, 得 $\frac{D Y}{D Z}=\frac{B Y}{B Q}$, 又

$$
\frac{D Y}{D Z}=\frac{\sin \angle D Z N}{\sin \angle Z Y D}, \frac{B Y}{B Q}=\frac{\sin \angle D Z N}{\sin \angle D Y N}
$$

于是 $\frac{\sin \angle Y Z D}{\sin \angle Z Y D}=\frac{\sin \angle D Z N}{\sin \angle D Y N}$. 结合 $N T$ 平分 $\angle Y N Z$ 可得 $\angle Y N T=\angle Z N T$, 故

$$
\frac{\sin \angle Y Z D}{\sin \angle D Z N} \cdot \frac{\sin \angle Z N T}{\sin \angle Y N T} \cdot \frac{\sin \angle D Y N}{\sin \angle Z Y D}=1 .
$$

由塞瓦定理逆定理得 $Z D, Y D, T N$ 共点, 即 $T, N, D$ 共线, 得证.

评注 本题难度易, 主要考察学生是否能发现题目图形中隐藏结论, 进而推证本题. 该题用一般的计算方法难以处理, 若无法发现共线则几何法亦不好下手, 但不失为一道好题。

题 2 简单连通图 $G$ 中, 设度数为 $i$ 的顶点个数为 $x_{i}$. 设 $d>3$ 为 $G$ 中最大的度数. 求证: 若

$$
x_{d} \geq x_{d-1}+2 x_{d-2}+\cdots+(d-1) x_{1}
$$

则必然存在一个度数为 $d$ 的点, 使得移除这个点之后, $G$ 中剩下的点和线段仍组成一个连通图。

注: 本题解答中, 小写字母均表示点, 大写字母均表示图.

证明 (谢晋宇 徐雪川) 反证法: 假设该结论不成立, 那么对给定的 $d$, 设使得存在一个简单连通图 $G_{t}$ (其中 $\left|G_{t}\right|=k$ ) 符合 $(*)$ 但不符合待证的最小的 $k$为 $k^{\prime}$.

设点 $a_{i}$ 为图 $G_{t}$ 中一个点度为 $d$ 的点, 满足去掉 $a_{i}$ 点后 $G_{t}$ 中分离出的部分中的某部分点数的最大值为 $G_{t}$ 中每一个点度为 $d$ 的点如此产生的值中的最大值, 并设 $B_{i}$ 为这个点数为最大值的部分, $C_{i}$ 为 $G_{t}$ 中除 $B_{i}$ 和点 $a_{i}$ 外的剩余部分. 则 $C_{i}$ 中任一点不与 $B_{i}$ 中任一点相连.

容易知道 $C_{i}$ 中不能再包含任意一个点度为 $d$ 的点; 否则, 设点 $t_{i} \in C_{i}$ 的度数为 $d$, 那么在原图 $G_{t}$ 中去掉点 $t_{i}$, 获得的部分中有一部分包含 $B_{i}$ 和点 $a_{i}$, 与 $a_{i}$ 的寻找条件矛盾.

考虑由 $B_{i}$, 点 $a_{i}$ 以及点 $a_{i}$ 与所有 $B_{i}$ 中的点原有的连线组成的新图集 $G_{s}$,并考虑由 $B_{i}$ 中所有原有连线组成的图集为 $G_{u}$. 下面计算 $G_{s}$ 和 $G_{u}$ 是否满足 $(*)$ 式.

由于 $B_{i}$ 中的点和 $C_{i}$ 中的点没有任何连线, 故 (*) 的变化仅限于去掉有关 $a_{i}$ 点的连线以及有关 $C_{i}$ 中的点的连线. 假设 $a_{i}$ 与 $C_{i}$ 中点共有 $m$ 条连线, 则去掉这些连线后, 由 $a_{i}$ 不再为点度为 $d$ 的点而为点度为 $d-m$ 的点, 即 $(*)$ 因此
左边减 1 , 右边加 $m$. 但是, 由于 $C_{i}$ 中每个点都不为点度为 $d$ 的点, 因此去掉 $C_{i}$ 中的点以及其和 $a_{i}$ 点的连线后, $C_{i}$ 中所有和 $a_{i}$ 连线的 $m$ 个点其点度均至多为 $d-1$.

若这些点度数并不均为 $d-1$, 则由于有 $m$ 个点, 每个点的去掉至少使得 (*) 右因此减 1 且至少存在一点去掉使得 (*) 右因此减 2 , 则总计会使得由此产生的 $(*)$ 右减少量 $\geq m+1$. 那么 $G_{s}$ 依然满足 $(*)$, 又由于 $G_{s}$ 包含于 $G$, 因此 $G_{s}$ 中任意一个点度为 $d$ 的点去掉后仍然会使 $G_{s}$ 不连通, 而 $\left|G_{s}\right|<|G|$, 与既设 ( $k$ 的最小性) 矛盾.

若 $C_{i}$ 中点个数 $\geq d$, 则全部去掉使得 $(*)$ 右边因此至少减去 $d$, 而 $m \leq d-1$,于是 $G_{s}$ 依然满足 $(*)$, 后续同上.

若 $C_{i}$ 中点个数 $\leq d-1$ 且 $C_{i}$ 中每个点度数均为 $d-1$, 则 $C_{i}$ 中的点与 $a_{i}$点构成一个 $d$ 阶完全图. 此时考虑 $G_{u}$, 去掉 $a_{i}$ 点以及 $C_{i}$ 后, 至多减少 2 个点度为 $d$ 的点而增加一个点度为 $d-1$ 的点, 即 $(*)$ 因此造成的右边增加和左边减少总计不超过 3 . 而由 $d$ 阶完全图中所有点均被去掉, 则 (*) 右至少因此减少 $d$,又 $d>3$, 故 $G_{u}$ 满足 $(*)$, 因 $G_{u}$ 也包含于 $G$, 故后续同上.

综上可知有矛盾, 则原命题成立.

评注 本题难度中等, 将部分化和极值思想很好地融入到图论问题中, 不等式条件看似随意而松散, 实际具有很强的迷惑性, 容易误导解题人向总线段等方向思考, 导致题目卡死. 解答中运用到的假设最小图以及推导矛盾的方式虽然常见，但仍然值得读者仔细思考.

题 3 四个正整数 $a, b, c, d$ 满足 $a b c d \neq 1$, 且它们两两互素. 完全积性函数 $f, g: \mathbb{N} \rightarrow\{0,1\}$ 满足对任意正整数 $n$, 均有

$$
f(a n+b)=g(c n+d) .
$$

证明以下命题中至少有一个成立:

(i) 对任意的正整数 $n, f(a n+b)=g(c n+d)=0$;

(ii) 存在正整数 $k$, 使得对任意满足 $(n, k)=1$ 的正整数 $n$, 均有 $g(n)=$ $f(n)=1$.

注: 若函数 $f(x)$ 满足对任意的正整数 $a, b$, 均有 $f(a b)=f(a) f(b)$, 就称 $f(x)$ 为完全积性函数.

证明 (徐雪川谢晋宇) 设 $f(a s+b)=1$, 下面说明, 对 $p>\max \left\{(a s+b)^{1+\varphi(a)}\right.$, $\left.(c s+d)^{1+\varphi(c)}, a d-b c, a, c\right\}$ 的时候, 有 $f(p)=g(p)=1$.
注意到由 $f(x)$ 为完全积性函数, 故若 $f(a b)=1$, 则 $f(a)=1$ 且 $f(b)=1$.

记

$$
A=\{a x+b \mid f(a x+b)=1\}, B=\{c x+d \mid g(c x+d)=1\}
$$

注意到对任意的正整数 $k$, 若 $m \in A$ 则 $m^{1+k \varphi(a)} \in A$; 若 $m \in B$ 则 $m^{1+k \varphi(c)} \in B$.

将 $A, B$ 中元素在 $\bmod p$ 理解下为 $A^{\prime}=\left\{x_{1}, x_{2}, \cdots, x_{t}\right\}, B^{\prime}=\left\{y_{1}, y_{2}, \cdots, y_{s}\right\}$.

设 $g$ 为 $\bmod p$ 的原根 (由原根存在性定理可知存在这样的 $g$ ), 因 $p>a s+b$,不妨设 $x_{1}=a s+b$.

设 $g^{l_{i}} \equiv \frac{x_{i}}{x_{1}}(\bmod p)(2 \leq i \leq t)$, 不妨设 $l_{2}<l_{3}<\cdots<l_{t}$, 令 $C=$ $\left\{l_{2}, l_{3}, \cdots, l_{t}\right\}$.

由于 $f(x)$ 完全积性, 注意 $\bmod p$ 意义下存在 $f\left(x_{i}\right)=1$, 存在 $f\left(x_{1}\right)=1$, 因此存在 $f\left(\frac{x_{i}}{x_{1}}\right)=1$, 同理可知, 存在 $f\left(\frac{x_{i} x_{j}}{x_{1}^{2}}\right)=1$. 又

$$
g^{l_{i}+l_{j}} \equiv \frac{x_{i} x_{j}}{x_{1}^{2}} \quad(\bmod p)
$$

于是 $l_{i}+l_{j} \in C$, 同理 $l_{i}-l_{j} \in C$, 即 $C$ 加减封闭.

因 $p>(a s+b)^{1+\varphi(a)}$, 故 $(a s+b)^{1+\varphi(a)}$ 与 $a s+b$ 模 $p$ 不同余.

于是, 由 $C$ 加减封闭, 故 $l_{i}=(i-2) l_{2}(2 \leq i \leq t)$, 记 $x_{1} \equiv g^{x}(\bmod p), l_{2}=$ $L$, 那么 $A^{\prime}=\left\{g^{x}, g^{x+L}, g^{x+2 L}, \cdots, g^{x+(t-1) L}\right\}$ (注意: $p \mid g^{t L}$ ), 则 $A^{\prime}$ 中所有元素之和 $\bmod p$ 余 0 . 同理 $B^{\prime}$ 元素之和 $\bmod p$ 余 0 .

对于 $m \in A^{\prime}, m \equiv a k+b(\bmod p)$, 则 $c k+d=\frac{c}{a} m+\frac{a d-b c}{a}$. 由 $a, b, c, d$ 两两互素, 故 $a d-b c \neq 0$. 又 $p>a d-b c, p>c$, 记

$$
U \equiv \frac{c}{a}(\bmod p), V \equiv \frac{a d-b c}{a} \quad(\bmod p)
$$

则 $U m+V \in B^{\prime}$, 于是 $A^{\prime}$ 有一个到 $B^{\prime}$ 的映射, 同样的 $B^{\prime}$ 有一个到 $A^{\prime}$ 的映射,即 $\left|A^{\prime}\right|=\left|B^{\prime}\right|$.

由于 $B^{\prime}$ 中元素和 $\equiv U \cdot \sum_{i \in A^{\prime}} i+t V \equiv 0(\bmod p)$, 又 $V$ 模 $p$ 不为 0 , 故 $p \mid t$,即 $t=p$. 于是 $A$ 中有 $p$ 的倍数, 同样 $B$ 中也有 $p$ 倍数.

从而, 此时 $f(p)=g(p)=1$.

也就是说, 要么对任意的 $n$ 均有 $f(a n+b)=g(c n+d)=0$, 要么, 当 $p$ 充分大时, $f(p)=g(p)=1$, 于是对于和 $R=\prod_{\substack{s<p \\ s \text { s数数 }}} s$ 互质的所有正整数 $n$, 均有 $f(n)=g(n)=1$, 命题得证.

评注 本题难度难, 不仅考察学生对原根的应用, 同时加减封闭性和总体考虑思想也完美地融入到了题目中，解答可以说是十分精妙而有趣，是很值得用来仔细思考和品味的一道题。
题 4 设 $\Omega(n), \omega(n)$ 分别为正整数 $n$ 的最大素因数和最小素因数. 阿里热扎和阿明玩一个游戏. 首先, 阿里热扎选定 1400 个整系数多项式, 阿明从中选择 700 个, 组成集合 $A$, 另外 700 个多项式组成集合 $B$. 若对于任意的 $n$, 都有下式成立,

$$
\max _{P \in A}(\Omega(P(n))) \geq \min _{P \in B}(\omega(P(n)))
$$

则阿明获胜. 若阿明无法选出这样的集合 $A$, 则阿里热扎获胜. 问谁有必胜策略?

解 (徐雪川) 设阿里热扎选取的多项式为 $f_{1}(x), f_{2}(x), \cdots, f_{1400}(x)$, 对于 1400 个多项式中任取 700 个构成的集合 $A_{1}, A_{2}, \cdots, A_{\mathrm{C}_{1400}^{700}}$, 令

$$
f_{i}(x)=\sum_{\left\{j \mid f_{i}(x) \in A_{j}\right\}} \frac{\left(p_{j}-2\right) \prod_{k \neq j}\left(x-a_{k}\right)}{\prod_{k \neq j}\left(a_{j}-a_{k}\right)}+2,
$$

其中 $p_{i}$ 为素数且大于 $2, a_{i}\left(1 \leq i \leq \mathrm{C}_{1400}^{700}\right)$ 满足 $\prod_{k \neq i}\left(a_{j}-a_{k}\right) \mid\left(p_{i}+1\right)$.

由拉格朗日差值公式，

$$
f\left(a_{i}\right)=\left\{\begin{array}{cc}
p_{i}, & f_{j}(x) \in A_{i} \\
2, & f_{j}(x) \notin A_{i}
\end{array}\right.
$$

由此, 阿里热扎必胜.

评注 本题难度中等偏易, 题目条件容易误导解题人认为阿明必胜, 但只要经过简单的枚举尝试就可以知道事实上阿里热扎似乎是必胜的, 从而根据拉格朗日差值公式构造多项式即可.

题 5 若三个实数中, 其中一个是另外两个数的平均数, 就称这是一个“好的"三元数组. 已知 $2 k+1$ 个互异的实数可以组成 $k^{2}$ 个“好的”三元数组. 证明:可以把这 $2 k+1$ 个数划分为两个部分, 每部分都是等差数列, 且公差相同.

证明（李春阳）假设 $2 k+1$ 个数依次为 $a_{1}<a_{2}<\cdots<a_{2 k+1}$, 不妨设 $a_{k+1}=0$. 于是以 $a_{i}$ 为中间数的三元等差数组至多为 $\min \{i-1,2 k+1-i\}$ 个,即总和至多 $k^{2}$ 个. 故必须全部取等. 则这些数必定关于 $a_{k+1}$ 对称, 否则以 $a_{k+1}$为中间数将少于 $k$ 个.

下面归纳证明: 对于 $2 k-1$ 个数, 只能为形如 $\{-2 s b,-2 s(b-1), \cdots, 2 s b\}$以及形如 $\{-(2 a-1) s,-(2 a-3) s, \cdots,(2 a-1) s\}$ 的等差数列拼接而成(对于 $k=1,2$, 这是平凡的).

若对 $2 k-1$ 成立, 当 $2 k+1$ 个数时, 包含首、尾两项中至少一项的三元等差数组最多为 $2 k-1$ 个(以任何一个正数项作中间项不可能包含首项, 否则其
第三项将大于末项; 负数项同理). 于是只从中间 $2 k-1$ 个数找三元数组需要找出至少 $(k-1)^{2}$ 对, 由归纳, 则 $2 k-1$ 个数为 $\{-2 s b,-2 s(b-1), \cdots, 2 s b\}$ 及 $\{-(2 a-1) s,-(2 a-3) s, \cdots,(2 a-1) s\}$. 考虑首末两项, 它们互为相反数. 易知它们必须为 $s$ 的倍数. 否则, 它们不可能和任何中间项形成三元等差数组.

由于对每个正数项为中间项必须与末项和某项构成等差数列, 因此容易知道末项必须为 $\max \{2(b+1) s,(2 a+1) s\}$, 因此归纳成立.

评注 本题难度易, 事实上很容易看出题目的条件正好是可以取到的最大值, 从而围绕达到最大值时的情况考虑, 则较容易给出证明.

题 6 在 $\triangle A B C$ 的欧拉线上取一点 $D$, 且 $D$ 在三角形内部. 直线 $B D, C D$分别和边 $A C, A B$ 交于 $E, F$. 在直线 $A D$ 上取点 $X$, 使得 $\angle E X F=180^{\circ}-\angle A$,且 $A, X$ 在直线 $E F$ 同侧. $\triangle C X F, \triangle B X E$ 的外接圆再次相交于点 $P$. 直线 $X P, E F$ 交于点 $K$. 求证: $A K \perp B C$.

证明 (谢晋宇) 先证明如下引理:

引理 如图, $\triangle A B C$ 中, $A B$ 的中垂线与 $A C$ 交于点 $Q, A C$ 的中垂线与 $A B$交于点 $R$, 则 $B Q, C R$ 的交点 $S$ 在其欧拉线上.



证明 以 $\triangle A B C$ 的外接圆 $O$ 为单位圆建立复平面, 以每个点的字母表示该点对应复数. 则 $Q$ 满足 $A, Q, C$ 共线以及 $A B \perp O Q$, 于是

$$
Q(\bar{A}-\bar{C})+A(\bar{C}-\bar{Q})+C(\bar{Q}-\bar{A})=0, \quad \frac{Q}{\bar{Q}}=-\frac{A-B}{\bar{A}-\bar{B}},
$$

解得 $Q=\frac{B(A+C)}{B+C}$, 同理 $R=\frac{C(A+B)}{B+C}$.

$S$ 满足 $B, Q, S$ 共线, 则 $S(\bar{B}-\bar{Q})+B(\bar{Q}-\bar{S})+Q(\bar{S}-\bar{B})=0$, 化简可得

$$
C S+\frac{A B^{2}}{C} \bar{S}=\frac{B(A+C)}{C} .
$$

同理, $C, R, S$ 共线, 则

$$
S+\frac{A C^{2}}{B} \bar{S}=\frac{C(A+B)}{B}
$$

联立, 消去 $\bar{S}$, 解出

$$
S=\frac{B C(A+B+C)}{B^{2}+B C+C^{2}}, \bar{S}=\frac{A B+B C+C A}{A\left(B^{2}+B C+C^{2}\right)}
$$

则

$$
\frac{S}{\bar{S}}=\frac{A B C(A+B+C)}{A B+B C+C A}=\frac{A+B+C}{\frac{A B+B C+C A}{A B C}}=\frac{H}{\bar{H}} .
$$

故 $S, O, H$ 共线, 也即 $S$ 在 $\triangle A B C$ 的欧拉线上, 引理得证.



回到原题. 注意到

$$
\begin{aligned}
& \angle A-\angle A C D=180^{\circ}-\angle D C S, \\
& \angle A-\angle A B D=\angle D B S(A B<A C),
\end{aligned}
$$

则

$$
\frac{\cos B}{\cos C}=\frac{\sin \angle B A H}{\sin \angle C A H}=\frac{\frac{A H \sin \angle A B H}{B H}}{\frac{A H \sin \angle A C H}{C H}}=\frac{C H}{B H} .
$$

又

$$
\begin{aligned}
\angle H B S & =\angle A B Q-\angle H B A=\angle A-\angle H B A \\
& =\angle A C R-\angle H C A=\angle H C R,
\end{aligned}
$$

因此

$$
\begin{aligned}
\frac{C H}{B H} & =\frac{C H \sin \angle H C S}{B H \sin \angle H B S}=\frac{H S \sin \angle H S C}{H S \sin \angle H S B} \\
& =\frac{B D \sin (\angle A-\angle A B D)}{C D \sin (\angle A-\angle A C D)}
\end{aligned}
$$

于是我们得到

$$
\frac{\cos B}{\cos C}=\frac{B D \sin (\angle A-\angle A B D)}{C D \sin (\angle A-\angle A C D)}
$$

如图, 设 $\triangle B X E$ 的外接圆交 $A B, E F$ 于 $L, U, \triangle C X F$ 的外接圆交 $A C, E F$ 于 $M, V, A H$ 交 $E F$ 于 $J, A D$ 交 $B C$ 于 $G$, 则

$$
\begin{gathered}
\angle M X E=\angle M X F-\angle E X F=180^{\circ}-\angle A C D-\left(180^{\circ}-\angle A\right) \\
=\angle A-\angle A C D \\
\frac{E M}{E X}=\frac{\sin \angle M X E}{\sin \angle X K E}=\frac{\sin (\angle A-\angle A C D)}{\sin \angle X F C} .
\end{gathered}
$$

类似地,

$$
\frac{F L}{F X}=\frac{\sin (\angle A-\angle A B D)}{\sin \angle X E B}
$$

由圆幂，

$$
F U \cdot F E=F L \cdot F B, E V \cdot E F=E M \cdot E C .
$$

由塞瓦定理 $(\triangle A B C-D)$,

$$
\frac{A F}{F B} \cdot \frac{B G}{G C} \cdot \frac{C E}{E A}=1,
$$

联立可得：

$$
\frac{A F}{A E} \cdot \frac{B G}{C G} \cdot \frac{E V}{F U}=\frac{E M}{F L} .
$$

又

$$
\begin{aligned}
\frac{E M}{F L} & =\frac{E X \sin \angle X E B \sin (\angle A-\angle A C D)}{F X \sin \angle X F C \sin (\angle A-\angle A B D)} \\
& =\frac{\sin \angle E D A \sin (\angle A-\angle A C D)}{\sin \angle F D A \sin (\angle A-\angle A B D)}
\end{aligned}
$$

再结合 $(*)$ 式可得

由此,

$$
\begin{aligned}
\frac{\sin \angle E D A \sin (\angle A-\angle A C D)}{\sin \angle F D A \sin (\angle A-\angle A B D)} & =\frac{B G \cdot C D \cdot \sin (\angle A-\angle A C D)}{C G \cdot B D \cdot \sin (\angle A-\angle A B D)} \\
& =\frac{B G \cos C}{C G \cos B} .
\end{aligned}
$$

$$
\frac{E V}{F U}=\frac{A E \cos C}{A F \cos B}=\frac{J E}{J F}=\frac{J E+E V}{J F+F U}=\frac{J V}{J U},
$$

故 $J V \cdot J F=J E \cdot J U, J$ 在两圆根轴上, 即 $J=K$, 因此, $A K \perp B C$.

评注 本题难度难, 需要学生熟知解答中的欧拉线有关结论, 并且本题并没有一个较完美的纯几何证法, 从而解答最终采用了三角法, 有兴趣的读者可以继续探索本题的几何法.
题 7 在一个无限大的网格表中放置若干正整数, 使得每个单元格中的数字等于它的相邻单元格中含有与其相同数字的单元格的个数. 这里的相邻指有公共顶点. 求这个网格表中互异的数字个数的最大值.

解 (徐雪川) 首先, 若存在 8 , 则方格表全为 8 ; 若存在 7 , 则方格表只能为 7 和空格, 否则设有一个 $t(t \neq 7)$ 与 7 相邻, 则 $t$ 周围必然全都是 $7, t$ 周围不存在 $t$, 与题目条件不符合.

定义一个数字为全封闭的: 如果该数字能填入表格, 并且仅存在于一个有限的区域内.

定义一个数字为半封闭的: 如果该数字能填入表格, 且在该表格中存在一行或一列的子方格表, 其中不存在该数字.

下面证明: 数字 6 将不能半封闭, 数字 5 将不能全封闭.

若数字 6 半封闭, 假设第 $k$ 行为存在数字 6 的最大的一行, 则第 $i$ 行 $(i>k)$将不能存在数字 6 , 则对于第 $k$ 行的任一个数字 6 而言, 显然其周围 8 格中位于第 $k+1$ 行的三格将不存在 6 , 即其周围最多有 5 个 6 , 矛盾. 对于列则同理.

若数字 5 全封闭, 则封闭处必然有拐角, 于是拐角处至少有 4 个不为 5 的数字, 则为 5 的数字个数 $\leq 4$, 矛盾.

于是数字 5 不能全封闭, 而数字 6 不能半封闭, 则必然存在 5 和 6 相邻.

若 5,6 紧挨着, 则 5 以及 5 周围有 5 个 5 , 也就是说, 至少有 3 个 5 会在 6 周围, 则 6 周围的 6 小于等于 5 个, 矛盾.

若 5,6 相邻但不紧挨着, 由于 6 周围要有 6 个 6 , 则必然存在一个 6 与 5 紧挨着, 下面同上. 于是矛盾.

故 5 和 6 不能同时存在. 又存在 7,8 时 $n$ 必然为 1 , 故可得 $n \leq 5$.

给出 $n=5$ 的构造:

第 $t(t \equiv 1(\bmod 8))$ 行均为 2 ;

第 $t(t \equiv 2(\bmod 8))$ 行均为 4 ;

第 $t(t \equiv 3(\bmod 8))$ 行第 $s(s \equiv 1(\bmod 3))$ 列为 3 , 其余均为 4 ;

第 $t(t \equiv 4(\bmod 8))$ 行均为 3 ;

第 $t(t \equiv 5,6(\bmod 8))$ 行均为 5 ;

第 $t(t \equiv 7,0(\bmod 8))$ 行第 $s(s \equiv 1(\bmod 3))$ 列为 1 , 其余均为 3 .

评注 本题难度易, 只需要考虑到最大的 6 和 5 的情况, 就容易得出矛盾的结论. 原题目中没有提到是否可以使用空格, 为了严谨, 上述构造中没有留空格.
题 8 求所有的函数 $f: \mathbb{N} \rightarrow \mathbb{N}$, 使得对任意的正整数 $m, n$, 均有

$$
f(n)+1400 m^{2} \mid n^{2}+f(f(m)) .
$$

解 (马超航 谢晋宇) 易知 $f(x), f(f(x))$ 无界; 否则, 由 (*),

$$
f(n)+1400 m^{2} \leq n^{2}+f(f(m)),
$$

令 $n$ 固定, $m$ 取足够大即知矛盾.

由 $(*)$ 可知:

$f(n)+1400 a^{2} \mid\left(n^{2}+f(f(a))\right)\left(f(n)+1400 b^{2}\right)-\left(n^{2}+f(f(b))\right)\left(f(n)+1400 a^{2}\right)$,同样

$f(n)+1400 b^{2} \mid\left(n^{2}+f(f(a))\right)\left(f(n)+1400 b^{2}\right)-\left(n^{2}+f(f(b))\right)\left(f(n)+1400 a^{2}\right)$,于是 $\left[f(n)+1400 a^{2}, f(n)+1400 b^{2}\right]$ 整除

$$
\left(n^{2}+f(f(a))\right)\left(f(n)+1400 b^{2}\right)-\left(n^{2}+f(f(b))\right)\left(f(n)+1400 a^{2}\right) .
$$

由辗转相除法得

$$
\left(f(n)+1400 a^{2}, f(n)+1400 b^{2}\right) \mid 1400\left(b^{2}-a^{2}\right),
$$

于是 $\left(f(n)+1400 a^{2}\right)\left(f(n)+1400 b^{2}\right)$ 整除

$1400\left(b^{2}-a^{2}\right)\left(n^{2}+f(f(a))\right)\left(f(n)+1400 b^{2}\right)-\left(n^{2}+f(f(b))\right)\left(f(n)+1400 a^{2}\right)$.

(*) 中取 $n=f(m)$ 可得

$$
f(f(m))+1400 m^{2} \mid f^{2}(m)+f(f(m)),
$$

可得 $f(m) \geq 1400 m^{2}$, 于是 $f(m)>30 m$.

从而在 $(* *)$ 中令 $a, b$ 固定, 当足够 $n$ 大时,

$$
\begin{aligned}
\left(f(n)+1400 a^{2}\right)\left(f(n)+1400 b^{2}\right) & >1400\left(b^{2}-a^{2}\right)\left(n^{2}+f(f(a))\right)\left(f(n)+1400 b^{2}\right) \\
& -\left(n^{2}+f(f(b))\right)\left(f(n)+1400 a^{2}\right) .
\end{aligned}
$$

因此, 当 $n$ 足够大时,

$1400\left(b^{2}-a^{2}\right)\left(n^{2}+f(f(a))\right)\left(f(n)+1400 b^{2}\right)-\left(n^{2}+f(f(b))\right)\left(f(n)+1400 a^{2}\right)=0$,

即

$1400 n^{2}\left(a^{2}-b^{2}\right)+f(n)(f(f(b))-f(f(a)))+1400\left(a^{2} f(f(b))-b^{2} f(f(a))\right)=0$,

解得当 $n$ 足够大时,

$$
f(n)=\frac{1400\left(a^{2} f(f(b))-b^{2} f(f(a))\right)+1400 n^{2}\left(a^{2}-b^{2}\right)}{f(f(b))-f(f(a))}
$$

对任意的 $n, a, b$ 均成立.
从而可以得到当 $a, b$ 固定时, $f(n)=p n^{2}+q$, 其中 $p$ 为正有理数, $q$ 为有理数, $p, q$ 均为定值. (当 $n$ 足够大时)

注意到 $f(n)$ 为自然数, 故 $p, q$ 必均为整数. 将其代回到 $(*)$ 中, 可得

$$
1400 m^{2}+p n^{2}+q \mid n^{2}+p^{2} m^{4}+2 p q m^{2}+q^{2} \text { ( } m, n \text { 足够大). }
$$

若 $p \geq 2$, 对固定的足够大的 $m$, 取 $n$ 足够大时, RHS $<\mathrm{LHS}$, 矛盾;

若 $p=1$, 对固定足够大的 $m$, 取 $n>n_{0}$ 为足够大的数, 则只能 RHS $=\mathrm{LHS}$,即 $1400 m^{2}+q=m^{4}+2 q m^{2}+q^{2}$, 当 $m$ 足够大时该式显然矛盾.

综上, 不存在符合题目的 $f$.

评注 本题难度中等偏难, 核心思路是运用轮换思想, 将整除项的量级翻倍,从而通过量级差推导矛盾. 轮换思想是函数方程 (尤其是整除类函数方程) 的一种基本思想, 读者可以通过本题品味这种思想的应用.

题 9 求证: 存在两个互素的整系数多项式 $P(x), Q(x)$ 以及一个实数 $u>0$,使得: 若正整数 $a, b, c, d$ 满足

则 $b P\left(\frac{a}{c}\right)=d Q\left(\frac{a}{c}\right)$.

$$
\left|\frac{a}{c}-1\right|^{2021} \leq \frac{u}{|d \| c|^{1010}}, \quad\left|\left(\frac{a}{c}\right)^{2020}-\frac{b}{d}\right|<\frac{u}{|d \| c|^{1010}}
$$

注：两个多项式互素，指这两个多项式没有相同的实根.

解 (马超航) 首先, 对于整系数多项式

$$
P(x)=x^{2020}-(x-1)^{2021}, Q(x)=1 \text {, }
$$

易知 $P(x)$ 与 $Q(x)$ 互素, 且若 $\frac{c}{a}, \frac{d}{b}$ 满足 $P\left(\frac{c}{a}\right)=\frac{d}{b} Q\left(\frac{c}{a}\right)$, 则

$$
\frac{d}{b}=\left(\frac{c}{a}\right)^{2020}-\left(\frac{c}{a}-1\right)^{2021} .
$$

代入 (**) 可知, (**) 等价于 $(*)$, 从而对任意的 $a, b, c, d$, 只要 $a, b, c, d$ 满足 $P\left(\frac{c}{a}\right)=\frac{d}{b} Q\left(\frac{c}{a}\right)$ 以及 $(*)$, 就有 $(* *)$ 成立.

下面说明, 存在一个 $u$, 使得对于任意的 $a, c$, 最多存在一组成比例的 $b, d$,使得 $(*)$ 与 $(* *)$ 均成立, 进而即可完成本题证明.

设 $r=a-c$, 注意到由于 $c, d$ 均为正整数, 只要 $u<1$, 则 $|r|<c^{\frac{1}{2}}$, 否则 $(*)$必然不可能成立.

下面先证明 $r=1$ 的情况, 化简 $(*)$ 与 $(* *)$ 可得:

$$
\begin{gathered}
d \leq u c^{1011} \\
\left|d(c+1)^{2020}-b c^{2020}\right| \leq u c^{1010}
\end{gathered}
$$

分解 $(c+1)^{2020}$ 可得:

$$
(c+1)^{2020}=c^{2020}+\mathrm{C}_{2020}^{2019} c^{2019}+\mathrm{C}_{2020}^{2018} c^{2018}+\cdots+\mathrm{C}_{2020}^{1} c+1 .
$$

对于任意一个 $c$ 以及 $x$, 我们将 $x$ 在 $c$ 进制下分解, 即

$$
x=s_{k} c^{k}+s_{k-1} c^{k-1}+\ldots s_{1} c+s_{0}
$$

其中 $0 \leq s_{i} \leq c-1(1 \leq i \leq k)$ 且 $s_{k} \neq 0$. 注意由于 $x<u c^{1011}$, 当 $u<1$ 时, 则 $k \leq 1010$.

对每一个 $x$, 必然有且只有一个最高次项为 $k$ 的非零整系数多项式 $f_{x}(c)$,满足 $f_{x}(c) \cdot(c+1)^{2020}$ 的 $c^{2020+k}$ 项到 $c^{2020}$ 项均与 $x c^{2020}$ 的这些项相等.

下面说明, 对于任何 $f_{x}(c)$, 当 $f_{x}(c)$ 的次数小于 1010 次时, $f_{x}(c)(c+1)^{2020}-$ $x c^{2020}$ 中 $, c^{2019}, c^{2018}, \cdots, c^{1010}$ 这些项中至少有一项非 0 .

设 $f_{x}(c)$ 中 $c^{k}$ 的系数为 $t_{k}$. 从而若希望 $c^{2019}, c^{2018}, \cdots, c^{1010}$ 这些项的系数全部为 0 , 则需要以下方程组成立:

$$
\begin{gathered}
\mathrm{C}_{2020}^{2019-k} t_{k}+\mathrm{C}_{2020}^{2020-k} t_{k-1}+\cdots+\mathrm{C}_{2020}^{2019} t_{0}=0 \\
\mathrm{C}_{2020}^{2018-k} t_{k}+\mathrm{C}_{2020}^{2019-k} t_{k-1}+\cdots+\mathrm{C}_{2020}^{2018} t_{0}=0 \\
\cdots \cdots \\
\mathrm{C}_{2020}^{1010-k} t_{k}+\mathrm{C}_{2020}^{1009-k} t_{k-1}+\cdots+\mathrm{C}_{2020}^{1010} t_{0}=0
\end{gathered}
$$

这里一共有 1010 个不同方程式, 而仅有 $k+1$ 个末知数, 因 $k+1 \leq 1010$, 又该方程组显然有解 $(0,0, \cdots, 0)$, 故该方程组只有一个解即全 0 , 与既设矛盾.

对一个次数等于 1010 的 $f_{x}(c)$ 而言, 若希望 $f_{x}(c)(c+1)^{2020}-x c^{2020}$ 中 $c^{2019}, c^{2018}, \cdots, c^{1010}$ 这些项的系数全部为 0 , 则需要求解方程组

$$
\begin{gathered}
\mathrm{C}_{2020}^{1009} t_{1010}+\mathrm{C}_{2020}^{1010} t_{1009}+\cdots+\mathrm{C}_{2020}^{2019} t_{0}=0 \\
\mathrm{C}_{2020}^{1008} t_{1010}+\mathrm{C}_{2020}^{1009} t_{1009}+\cdots+\mathrm{C}_{2020}^{2018} t_{0}=0 \\
\cdots \cdots \\
\mathrm{C}_{2020}^{0} t_{1010}+\mathrm{C}_{2020}^{1} t_{1009}+\cdots+\mathrm{C}_{2020}^{1010} t_{0}=0
\end{gathered}
$$

这里共 1010 个不同方程式以及 1011 个未知数, 于是解出的未知数 $\left(t_{1010}, t_{1009}\right.$, $\left.\cdots, t_{0}\right)$ 一定为某一组解 $\left(t_{1010}^{\prime}, t_{1009}^{\prime}, \cdots, t_{0}^{\prime}\right)$ 的倍数. 从而由

$$
\begin{aligned}
& s_{1010}=\mathrm{C}_{2020}^{0} t_{1010}, \\
& s_{1009}=\mathrm{C}_{2020}^{1} t_{1010}+\mathrm{C}_{2020}^{0} t_{1009}, \\
& \ldots \ldots \\
& s_{0}=\mathrm{C}_{2020}^{1010} t_{1010}+\mathrm{C}_{2020}^{1009} t_{1009}+\cdots+\mathrm{C}_{2020}^{0} t_{0},
\end{aligned}
$$

可得 $\left(s_{0}, s_{1}, \cdots, s_{1010}\right)$ 也为某一个固定的 $\left(s_{0}^{\prime}, s_{1}^{\prime}, \cdots, s_{1010}^{\prime}\right)$ 的若干倍数.
从而 $x$ 必然为某个定值 $x_{0}$ 的倍数. 对应的 $f_{x}(c)$ 也为 $f_{x_{0}}(c)$ 的倍数, 因此,若 $b, d$ 的取值希望 $f_{x}(c)(c+1)^{2020}-x c^{2020}$ 中 $c$ 的最高次系数小于等于 1009 ,则 $b$ 和 $d$ 的比值确定, 即 $\frac{d}{b}$ 为定值.

对 $r$ 不等于 1 , 当 $r$ 为正数时, 将 $c$ 视为 $r c^{\prime}$ (此时允许不为整数, 注意到因 $|r|<c^{\frac{1}{2}}$, 故此时 $c^{\prime}$ 最多会减小至 $\left.c^{\frac{1}{2}}\right)$, 因此时 $d \leq u c^{1011} r^{-2021}$, 因此 $(* *)$ 中左、右各乘 $r^{1010}$ 后, 可以化归为 $r=1$ 的情形(事实上, $r=1$ 中的任意正整数 $d$ 对应到这里会变为 $d r^{-2021}$, 有可能会不再为整数, 所以该情形会比 $r=1$ 的情形更便于解决); 当 $r$ 为负数时, 只需要将 $b, d$ 进行调换即可(不改变结果).

最后, 令 $u$ 满足: $u<1$;

对于任意的 $c$, 要么 $c^{\frac{1}{2}}$ 足够大, 满足对任意的 $x, f_{x}\left(c^{\frac{1}{2}}\right)$ 需要满足 $x c^{1010}-$ $\left(f_{x}\left(c^{\frac{1}{2}}\right)-1\right)\left(c^{\frac{1}{2}}+1\right)^{2020}$ 必然大于 $c^{505}$ (由于 $f_{x}(c) \cdot(c+1)^{2020}$ 与 $x c^{2020}$ 中 $c$的 $2020,2021, \cdots, 2020+k$ 项系数均一致, 因此 $\left(f_{x}(c) \cdot-1\right)(c+1)^{2020}$ 中必然有一个 $c^{i}(i \geq 2020)$ 系数比 $x c^{2020}$ 中该项系数要小, 由于二者均为整系数, 故该系数至少要小 1 , 因此只要 $c^{\frac{1}{2}}$ 足够大, 必然可以做到这一点);

要么 $u c^{1010}<1$, 从而, 对于任意的两个正整数 $b, d$, 当 $b c^{2020}>d(c+s)^{2020}$时, $(* *)$ 无解; 当 $b c^{2020}<d(c+s)^{2020}$ 时, $(* *)$ 至多有一组成比例的解 $b, d$, 即对于已知的 $a, c, d$, 只有一个确定的 $\frac{d}{b}$, 从而题目得证.

评注 本题难度中等偏难, 考察对正整数的利用. 实际上 $\frac{d}{b}$ 的取值是必须根据 $\frac{c}{a}$ 唯一确定的, 根据这一点, 结合已知条件中右项 $c$ 的系数和左项 $c$ 的系数的对比, 就可以比较顺利地想到通过量级寻求矛盾.

题 10 求所有函数 $f: \mathbb{N} \rightarrow \mathbb{R}$, 使得对任意的正整数 $a, b, c$, 均有

$$
f(a c)+f(b c)-f(c) f(a b) \geq 1
$$

解 (徐雪川) 取 $a=b=c=1$ 知 $(f(1)-1)^{2} \leq 0$, 即 $f(1)=1$.

取 $b=c=1$ 可知 $f(a) \geq 1$.

取 $a=b=c$ 有 $2 f\left(a^{2}\right)-f(a) f\left(a^{2}\right) \geq 1$, 即 $f\left(a^{2}\right)(2-f(a)) \geq 1$, 即

$$
f\left(a^{2}\right) \leq 2-\frac{1}{f\left(a^{2}\right)}
$$

结合 $f(a) \geq 1$ 知 $f(a)<2$.

假设数列 $\left\{b_{n}\right\}: b_{1}=f(a), b_{n+1}=\frac{1}{2-b_{n}}$, 则 $b_{n}=f\left(a \cdot 2^{n}\right)$.

又 $1 \leq f(a)<2$, 设 $f(a)=k$, 下归纳证明

$$
b_{n}=\frac{(n-1)-k(n-2)}{n-k(n-1)}(n \geq 2) .
$$

对 $n=2$ 平凡, 设 $n=s$ 成立, $n=s+1$ 时, $b_{s+1}=\frac{1}{2-b_{s}}=\frac{s-k(s-1)}{(s+1)-s k}$, 于是归纳成立.

又根据 $f(a)<2$ 即 $b_{n}<2$, 可得 $k<\frac{n+2}{n+1}$. 令 $n \rightarrow+\infty$ 时, 可得 $k=1$. 于是对任意的 $a, f(a)$ 均为 1 , 故 $f(x)=1$.

评注 本题难度易, 考察简单的递推思想. 容易发现函数的一个解 $f(x)=1$,且通过试验可以发现当 $x$ 增大时, $f(x)$ 从两端逼近 1 , 从而就可以确定大致思路.

题 11 在非等腰梯形的四边形 $A B C D$ 内部取一点 $X$, 使得 $\angle A X D+$ $\angle B X C=180^{\circ}$. 过 $D$ 作 $A X$ 垂线, 与 $\angle A B X$ 平分线交于点 $K$, 过 $A$ 作 $D X$ 垂线, 与 $\angle D C X$ 平分线交于点 $L$, 已知 $B K \perp C X, C L \perp B X, \triangle A D X$ 的外心在直线 $K L$ 上. 求证: $K L \perp A D$.



证明 (马超航) 如图, 设 $C X$ 交 $A B$ 于 $E, B X$ 交 $C D$ 于 $F, A L$ 交 $D K$ 于 $H$ ( $H$ 为 $\triangle A X D$ 的垂心), 则 $B K$ 为 $X E$ 的中垂线, $C L$ 为 $X F$ 的中垂线. 记 $R$为 $\triangle A X D$ 外接圆半径.

由此,

$$
\angle E X F=180^{\circ}-\angle A X D, \angle B E X=\angle B X E=\angle C X F=\angle X F C \text {, }
$$

故

$$
\angle A E X=180^{\circ}-\angle X E B=180^{\circ}-\angle E X B=\angle C X B=180^{\circ}-\angle A X D .
$$

在直线 $A L$ 上取点 $M$ 使得 $M O \perp A X, D K$ 上取点 $N$ 使得 $N O \perp D X$. 于是 $O N H M$ 为平行四边形. $\angle M A X=90^{\circ}-\angle A X D=\angle A E X-90^{\circ}$, 故

$$
\angle A M X=180^{\circ}-2 \angle M A X=360^{\circ}-2 \angle A E X,
$$

结合 $M$ 在 $A X$ 中垂线上可知 $M$ 为 $\triangle A E X$ 外心, 同理 $N$ 为 $\triangle D F X$ 外心.
故 B,K,M 与 $C, L, N$ 均共线. $K M$ 与 $N L$ 的夹角即为 $B K$ 与 $C L$ 的夹角大小, 也即 $D K$ 与 $A L$ 夹角大小, 即 $\angle A H K$, 也即 $\angle A X D$.

以下, 不妨令 $\angle D A X, \angle A X D, \angle A D X$ 分别为 $p, q, r$, 并设 $p \geq q \geq r$, 令 $s=p-q, t=q-r$, 则

$$
\begin{aligned}
& \angle K D O=\angle H D X-\angle O D X=\left(90^{\circ}-q\right)-\left(90^{\circ}-p\right)=p-q=s, \\
& \angle L A O=\angle O A X-\angle L A X=\left(90^{\circ}-r\right)-\left(90^{\circ}-q\right)=q-r=t .
\end{aligned}
$$

下由 $M O / / H N, M H / / O N$, 可得 $\triangle L M O \sim \triangle N K O$, 则

$$
M L \cdot N K=M O \cdot N O \text {. }
$$

令 $\angle H M K=b$ 并令 $a=b+q, c=b-q$, 则

$$
\begin{aligned}
& \angle L N O=\angle H L N=b-\angle\langle\overrightarrow{M K}, \overrightarrow{L N}\rangle, \\
& \angle K M O=180^{\circ}-\angle A M O-\angle H M K=180^{\circ}-q-b=180^{\circ}-a .
\end{aligned}
$$

(符号 $\angle\langle\overrightarrow{M K}, \overrightarrow{L N}\rangle$ 表示有向角, 即向量 $\overrightarrow{M K}$ 与 $\overrightarrow{L N}$ 的夹角, 后面同理)

同时，

$$
\angle L N K=\angle L H N+\angle H L N=c+x=b,
$$

于是

$$
\begin{aligned}
M L & =H L-H M=H N \frac{\sin \angle H N L}{\sin \angle H L N}-O N \\
& =O M \frac{\sin \angle H N L}{\sin \angle H L N}-O D \frac{\sin \angle O D N}{\sin \angle O N D} \\
& =O A \frac{\sin \angle M A O}{\sin \angle A M O} \frac{\sin \angle H N L}{\sin \angle H L N}-O D \frac{\sin \angle O D N}{\sin \angle O N D} \\
& =R \frac{\sin t}{\sin q} \frac{\sin b}{\sin c}-R \frac{\sin s}{\sin q} \\
& =\frac{R}{\sin q}\left(\frac{\sin t \cdot \sin b}{\sin c}-\sin s\right) .
\end{aligned}
$$

同理, $N K=\frac{R}{\sin q}\left(\frac{\sin s \cdot \sin b}{\sin a}-\sin t\right)$, 代入 $M L \cdot N K=M O \cdot N O$ 有

$$
\frac{R^{2}}{\sin ^{2} q}\left(\frac{\sin t \cdot \sin b}{\sin c}-\sin s\right)\left(\frac{\sin s \cdot \sin b}{\sin a}-\sin t\right)=\frac{R \sin s \cdot R \sin t}{\sin ^{2} q},
$$

即

$(\sin b \cdot \sin t-\sin c \cdot \sin s)(\sin b \cdot \sin s-\sin a \cdot \sin t)=\sin a \cdot \sin c \cdot \sin s \cdot \sin t$,展开并相消可得

$$
\sin b \cdot \sin s \cdot \sin t=\sin ^{2} s \cdot \sin c+\sin ^{2} t \cdot \sin a
$$

由 $\sin a+\sin c=\sin (b+q)+\sin (b-q)=2 \sin b \cdot \cos q$ 可得

$$
\left(\frac{\sin s \cdot \sin t}{2 \cos q}\right)(\sin a+\sin c)=\sin ^{2} s \cdot \sin c+\sin ^{2} t \cdot \sin a
$$

注意到, 由 $p+q+r=\pi$,

$$
\begin{aligned}
\sin p \cdot \sin s+\sin r \cdot \sin t & =\sin p \cdot \sin (p-q)+\sin r \cdot \sin (q-r) \\
& =2 \sin (p+2 r) \cdot \sin r+\sin (r+2 p) \cdot \sin p
\end{aligned}
$$

由积化和差，

$$
\begin{aligned}
& 2 \cos (p+r) \sin p=\sin (2 p+r)-\sin r, \\
& 2 \cos (p+r) \sin r=\sin (2 r+p)-\sin p .
\end{aligned}
$$

于是

$$
\begin{aligned}
\sin (2 p+r) \sin (2 r+p) & =\sin (2 p+r)(\sin p+2 \cos (p+r) \sin r) \\
& =\sin p \cdot \sin (2 p+r)+2 \cos (p+r) \cdot \sin r \cdot \sin (2 p+r)
\end{aligned}
$$

以及

$$
\begin{aligned}
\sin (2 p+r) \sin (2 r+p) & =\sin (2 p+r)(\sin r+2 \cos (p+r) \sin p) \\
& =\sin r \cdot \sin (2 r+p)+2 \cos (p+r) \cdot \sin p \cdot \sin (2 r+p)
\end{aligned}
$$

于是

$$
\begin{aligned}
& \sin r \cdot \sin (2 r+p)+2 \cos (p+r) \cdot \sin p \cdot \sin (2 r+p) \\
& =\sin p \cdot \sin (2 p+r)+2 \cos (p+r) \cdot \sin r \cdot \sin (2 p+r),
\end{aligned}
$$

即

$$
\sin p \cdot \sin s+\sin r \cdot \sin t=2 \cos q(\sin p \cdot \sin t+\sin r \cdot \sin s) .
$$

结合 (*), (**), 将 $\sin a$ 与 $\sin c$ 的比视作未知数, 可以解出

$$
\frac{\sin a}{\sin c}=\frac{\sin p \cdot \sin s}{\sin r \cdot \sin t}
$$

注意

$$
H M=O N=O D \frac{\sin \angle K D O}{\sin \angle D N O}=R \frac{\sin s}{\sin q},
$$

同样 $H N=R \frac{\sin t}{\sin q}$, 则

$$
\begin{aligned}
\frac{\sin a}{\sin c} & =\frac{\sin p \cdot \sin s}{\sin r \cdot \sin t}=\frac{H M \sin p}{H N \sin r} \\
& =\frac{H K \cdot \frac{\sin \angle H K M}{\sin \angle H M K} \sin p}{H L \cdot \frac{\sin \angle H L N}{\sin \angle H N L} \sin r} \\
& =\frac{H K \cdot \frac{\sin a}{\sin b} \sin p}{H L \cdot \frac{\sin c}{\sin b} \sin r} \\
& =\frac{H K \cdot \sin a \cdot \sin p}{H L \cdot \sin c \cdot \sin r} .
\end{aligned}
$$

于是 $\frac{H K}{H L}=\frac{\sin r}{\sin p}$, 又 $\frac{H K}{H L}=\frac{\sin \angle H K L}{\sin \angle H L K}$, 设有向角 $\angle\langle\overrightarrow{L K}, \overrightarrow{A D}\rangle=\alpha$, 有

$$
\frac{\sin r}{\sin p}=\frac{\sin \left(\frac{\pi}{2}+r-a\right)}{\sin \left(p+\alpha-\frac{\pi}{2}\right)}
$$

可得 $\alpha=\frac{\pi}{2}$, 即 $L K \perp A D$.

评注 本题难度难, 难点在于图形的构造非常紧凑, 不容易画出一个标准图,也就不容易观察到其中的几何学奥秘. 本题的解答采用了三角的方法, 利用点 $A$ 和 $D$ 的对称性、 $L$ 和 $K$ 的对称性, 考虑出 $M$ 和 $N$ 这两个关于 $A, D$ 以及 $L, K$ 均对称的点, 从而利用三角计算出最终希望得到的结论. 本题还可以采用反演的方法, 取出点 $X$ 关于 $K D, A L$ 以及 $K L$ 的对称点, 利用如此构造出的多组四点共圆, 关于 $X$ 点进行反演, 有兴趣的读者可以自行尝试.

题 12 对一个基数为 $3 n$ 的集合, 我们用八种颜色对其所有基数为 $n$ 的子集染色. 求证: 存在一种染色方法, 使得不存在 3 个同色的子集 $A, B, C$, 满足:

$$
|A \cap B| \leq 1,|A \cap C| \leq 1,|B \cap C| \leq 1
$$

证明 (谢晋宇) 由题意, 不妨设该集合中含有元素 $1,2,3,4$, 构造一种染色方法:
(I) $1 \in A, 2,3,4 \notin A$;
(II) $2 \in A, 1,3,4 \notin A$;
(III) $3 \in A, 1,2,4 \notin A$;
(IV) $4 \in A, 1,2,3 \notin A$;
(V) $1,2 \in A$ 或 $3,4 \in A$;
(VI) $1,3 \in A$ 或 $2,4 \in A$;
(VII) $2,3 \in A$ 或 $1,4 \in A$;
(VIII) $1,2,3,4 \notin A$.

注: 一个集合若染多种颜色, 则默认为标号最小.

评注 本题难度易, 只要从前几个元素开始着手思考, 很容易就能得到构造.

