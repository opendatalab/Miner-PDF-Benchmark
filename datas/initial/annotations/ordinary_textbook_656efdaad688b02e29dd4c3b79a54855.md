数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年北京大学金秋营数学试题解答与评注 

曾彦翔<br>(湖南省长沙市雅礼中学, 410007)<br>指导教师: 彭熹

北京大学数学科学学院于 2021 年 10 月 23 日及 24 日举办北京大学优秀中学生数学学科探究拓展活动, 期间进行了两场考试, 考试分两天, 每天 4 道题,共 8 题. 试题第一天难度明显低于第二天, 其中第 $4,7,8$ 题难度较大, 且有一定背景, 其余问题均不超过 CMO 1,4 难度.

## I. 试 题

1. 在锐角三角形 $A B C$ 中, $A D$ 为 $B C$ 边上的高, $E$ 为 $A$ 关于 $\odot(A B C)$的对径点, $\angle B A C$ 的角平分线交 $B C$ 于 $F$, 交 $\odot(A B C)$ 于 $G$, 设 $E F$ 延长线交 $A D$ 于 $K$, 记 $A$ 关于 $G$ 的对称点为 $T$. 证明: $B, K, C, T$ 四点共圆.
2. 设 $p$ 为奇素数, $q$ 是大于 1 的奇数, $m, n$ 为正整数, 满足 $p^{m} \mid \prod_{i=1}^{n}\left(q^{i}-1\right)$.证明: $2 p^{m}<q^{n}$.
3. 已知 $p$ 为素数, $n \geq p$. 称 $n$ 阶置换为好的, 如果其 $p$ 次复合为单位置换. 证明: 好的置换数为 $p$ 的倍数.
4. 给定正整数 $n$, 求所有满足要求的非负整数 $t \leq n$ 使得存在多项式 $f(x)=x^{n}+\sum_{i=0}^{n-1} a_{i} x^{i}$ 同时满足:

(1) $a_{0}, a_{1}, \cdots, a_{n-1}$ 中存在 $t$ 个正数, $n-t$ 个负数;

(2) $f(x)$ 有 $t$ 个互异正根, $n-t$ 个互异负根.

5. 给定非负实数 $x, y, z$, 记 $a=x^{2}(y-z)^{4}, b=y^{2}(z-x)^{4}, c=z^{2}(x-y)^{4}$.证明:

$$
(a+b+c)^{3} \geq \frac{9}{2}(a \sqrt{b}+b \sqrt{c}+c \sqrt{a})^{2} .
$$

修订日期: 2022-02-03.

6. 设简单图 $G$ 有 95 个顶点, 2021 条边. 证明: 所有点度数平方和不超过 300000 .
7. 设 $p, q$ 是不同的奇素数. 证明: $p$ 是 $q$ 的原根, 当且仅当 $\frac{x^{q}-1}{x-1}$ 在模 $p$ 意义下是不可约的.
8. 设 $n$ 阶连通图 $G$ 围长为 $2 k$, 最小度数为 $\delta \geq 2$, 半径为 $r(G)=$ $\min _{v \in G} \max _{u \in G} \operatorname{dist}(u, v)$. 证明:

$$
r(G) \leq \frac{k n}{2(\delta-1)^{k-1}}+4 k
$$

## II. 解答与评注

题 1 在锐角三角形 $A B C$ 中, $A D$ 为 $B C$ 边上的高, $E$ 为 $A$ 关于 $\odot(A B C)$的对径点, $\angle B A C$ 的角平分线交 $B C$ 于 $F$, 交 $\odot(A B C)$ 于 $G$, 设 $E F$ 延长线交 $A D$ 于 $K$, 记 $A$ 关于 $G$ 的对称点为 $T$. 证明: $B, K, C, T$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_391abaa3a23ee1341f9fg-02.jpg?height=905&width=468&top_left_y=1221&top_left_x=794)

证明 延长 $T E$ 交 $B C$ 于 $S$, 设三角形 $A B C$ 外心为 $O$, 连接 $O G, K B, K C$, $T B, T C, C E$. 则 $O$ 为 $A E$ 中点. 而 $G$ 为 $A T$ 中点, 故

$$
T E / / O G, T E S \perp B C .
$$

故 $\angle A D C, \angle C S E, \angle A C E$ 均为直角,

$$
\triangle A D C \sim \triangle C S E
$$

$$
D C \times S C=A D \times S E
$$

利用平行线 $A D, S T$ 分线段成比例:

$$
A D \times S E=D K \times S T .
$$

联立上式并注意到 $\angle K D C, \angle C S T$ 均为直角,

$$
\triangle K D C \sim \triangle C S T .
$$

于是 $\angle K C T$ 为直角. 同理, $\angle K B T$ 也为直角, 即四点 $B, K, C, T$ 均在以 $K T$ 为直径的圆上.

评注 作出标准图容易发现 $\angle K B T, \angle K C T$ 都是直角, 而 $G$ 是 $A T$ 中点提示 $T E$ 垂直于 $B C$, 随之发现两组三垂直形式的相似, 问题便得证. 本题较易,是全卷最简单的题目。

题 2 设 $p$ 为奇素数, $q$ 是大于 1 的奇数, $m, n$ 为正整数, 满足 $p^{m} \mid \prod_{i=1}^{n}\left(q^{i}-1\right)$.证明: $2 p^{m}<q^{n}$.

证明 显然 $p, q$ 互素. 设 $q$ 模 $p$ 的阶为 $d$, 则只有 $i$ 为 $d$ 的倍数的项贡献 $p$ 因子, 可用 $q^{d}$ 代替 $q$ 进行讨论, 故下不妨设 $d=1$, 即 $q$ 模 $p$ 余 1 . 并记 $q=k p^{s}+1\left(k, s \in \mathbb{N}^{*}, p \nmid k\right)$.

用 $\nu_{p}(x)$ 表示正整数 $x$ 在标准分解下含素数 $p$ 的幕次, 由升幕定理(LTE 引理),

$$
m \leq \sum_{i=1}^{n}\left(\nu_{p}(q-1)+\nu_{p}(i)\right)=n s+\sum_{j=1}^{\infty}\left\lfloor\frac{n}{p^{j}}\right\rfloor<n s+\frac{n}{p-1},
$$

解得 $n \geq\left\lfloor\frac{(p-1) m}{(p-1) s+1}\right\rfloor+1>\frac{(p-1) m}{(p-1) s+1}$. 注意到 $p, q$ 为奇数, 故 $k \neq 1, q>2 p^{s}$.

不妨设 $s<m$, 否则命题直接成立. 此时若 $s \geq \frac{m}{2}$, 有 $n \geq 2$. 故

$$
q^{n} \geq\left(2 p^{s}\right)^{n} \geq\left(2 p^{\frac{m}{2}}\right)^{2}>2 p^{m}
$$

而若 $s \leq \frac{m-1}{2}$ 且 $p \geq 7$, 则

$$
q^{n}>\left(2 p^{s}\right)^{\frac{(p-1) m}{(p-1) s+1}}=p^{m} \cdot\left(\frac{2}{\sqrt[p-1]{p}}\right)^{\frac{(p-1) m}{(p-1) s+1}}>p^{m} \cdot\left(\frac{2}{\sqrt[p-1]{p}}\right)^{2}>2 p^{m} .
$$

特别地, $p=3$ 时, 利用 $s, m$ 都是整数:

- 若 $s \geq \frac{m-1}{2}$, 则 $n=2, q^{n}>\left(2 p^{\frac{m-1}{2}}\right)^{2}=4 p^{m-1}>2 p^{m}$.
- 若 $\frac{m-1}{3} \leq s \leq \frac{m-2}{2}$, 则 $n=3, q^{n}>\left(2 p^{\frac{m-1}{3}}\right)^{3}=8 p^{m-1}>2 p^{m}$.
- 若 $\frac{m-1}{4} \leq s \leq \frac{m-2}{3}$, 则 $n=4, q^{n}>\left(2 p^{\frac{m-1}{4}}\right)^{4}=16 p^{m-1}>2 p^{m}$.
- 若 $\frac{m-2}{5} \leq s \leq \frac{m-2}{4}$, 则 $n=5, q^{n}>\left(2 p^{\frac{m-2}{5}}\right)^{5}=32 p^{m-2}>2 p^{m}$.
- 若 $s \leq \frac{m-3}{5}$, 则

$$
\frac{(p-1) m}{(p-1) s+1}>5, q^{n}>p^{m} \cdot\left(\frac{2}{\sqrt[p-1]{p}}\right)^{\frac{(p-1) m}{(p-1) s+1}}>p^{m} \cdot\left(\frac{2}{\sqrt{3}}\right)^{5}>2 p^{m}
$$

特别地, $p=5$ 时, 利用 $s, m$ 都是整数:

- 若 $s \geq \frac{m}{2}$, 则 $n=2, q^{n}>\left(2 p^{\frac{m}{2}}\right)^{2}=4 p^{m}>2 p^{m}$.
- 若 $\frac{m}{3} \leq s \leq \frac{m-1}{2}$, 则 $n=3, q^{n}>\left(2 p^{\frac{m}{3}}\right)^{3}=8 p^{m}>2 p^{m}$.
- 若 $s \leq \frac{m-1}{3}$, 则

$$
\frac{(p-1) m}{(p-1) s+1}>3, q^{n}>p^{m} \cdot\left(\frac{2}{\sqrt[p-1]{p}}\right)^{\frac{(p-1) m}{(p-1) s+1}}>p^{m} \cdot\left(\frac{2}{\sqrt[4]{5}}\right)^{3}>2 p^{m}
$$

无论何种情形, 命题均成立.

评注 由于升幂定理是熟知的, 本题难度不大, 后半部分完全是精细的代数处理。

题 3 已知 $p$ 为素数, $n \geq p$. 称 $n$ 阶置换为好的, 如果其 $p$ 次复合为单位置换. 证明: 好的置换数为 $p$ 的倍数.

证明 设 $A$ 是全体 $n$ 阶置换构成的集合, 由乘法原理, $|A|=n !$. 记 $i d$ 是恒等置换, 定义

$$
B=\left\{\left(g_{1}, g_{2}, \cdots, g_{p}\right) \mid g_{1} \circ g_{2} \circ \cdots \circ g_{p}=i d, g_{1}, g_{2}, \cdots, g_{p} \in A\right\}
$$

则 $g_{p}$ 由 $g_{1}, g_{2}, \cdots, g_{p-1}$ 唯一确定, $|B|=|A|^{p-1}$, 且好的置换数等于 $B$ 中使得 $g_{1}=g_{2}=\cdots=g_{p}$ 的元素个数. 对于 $B$ 中其它的元素, 记它们构成集合 $C$,可以将它们每 $p$ 个归入同一等价类, 具体地, 如下 $p$ 个属于同一等价类:

$$
\left(g_{1}, g_{2}, \cdots, g_{p}\right), \quad\left(g_{2}, g_{3}, \cdots, g_{p}, g_{1}\right), \cdots, \quad\left(g_{p}, g_{1}, g_{2}, \cdots, g_{p-1}\right)
$$

事实上, 由于 $p$ 是素数且 $g_{1}, g_{2}, \cdots, g_{p}$ 不全相同, 如上 $p$ 者互异. 故 $|C|$ 是 $p$ 的倍数. 好置换个数 $m$ 满足

$$
m=|B|-|C|=(n !)^{p-1}-|C| \equiv 0-0=0 \quad(\bmod p) .
$$

评注 利用等价类进行配对是组合计数中很巧妙的想法, 它往往能避免复杂
的计算. 本题也可以直接计算, 即利用好置换对应的映射轨道是若干长度为 1 或 $p$ 的圈之并进行计数.

题 4 给定正整数 $n$, 求所有满足要求的非负整数 $t \leq n$ 使得存在多项式 $f(x)=x^{n}+\sum_{i=0}^{n-1} a_{i} x^{i}$ 同时满足:

(1) $a_{0}, a_{1}, \cdots, a_{n-1}$ 中存在 $t$ 个正数, $n-t$ 个负数;

(2) $f(x)$ 有 $t$ 个互异正根, $n-t$ 个互异负根.

解 所求 $t$ 为满足 $1 \leq t \leq \frac{2 n}{3}$ 的全体整数.

考虑命题 $P(s, t, n)$ : 存在一个 $n$ 次首项系数为正的实系数多项式 $f$, 使 $f$除首项外恰有 $s$ 个正系数, $n-s$ 个负系数, 且 $f$ 恰有 $t$ 个互异正根, $n-t$ 个互异负根. 只需考虑 $0 \leq s, t \leq n$ 的命题 $P$.

断言 命题 $P(s, t, n)$ 为真的充要条件是:

1. $t$ 为偶数时, $P(s-1, t-1, n-1)$ 与 $P(s-1, t, n-1)$ 中至少一者为真;
2. $t$ 为奇数时, $P(s, t-1, n-1)$ 与 $P(s, t, n-1)$ 中至少一者为真.

证明 充分性. 假设 $f(x)=x^{n}+\sum_{i=0}^{n-1} a_{i} x^{i}$ 满足 $P(s, t, n)$, 记 $f$ 的所有根为

$$
z_{1}<z_{2}<\cdots<z_{n-t}<0<z_{n-t+1}<\cdots<z_{n} .
$$

由罗尔 (Rolle) 定理, $f^{\prime}$ 在 $\left(z_{i}, z_{i+1}\right)(i=1,2, \cdots, n-1)$ 上有根. 又 $f^{\prime}(0)=$ $a_{1} \neq 0$, 故 $f^{\prime}$ 恰有 $t$ 个正根, $n-t-1$ 个负根或 $t-1$ 个正根, $n-t$ 个负根.

由韦达 (Vieta) 定理, $a_{0}$ 和 $(-1)^{t}$ 同号, 而 $f^{\prime}$ 的 $x^{k}$ 项系数与 $f$ 的 $x^{k+1}$ 项系数同号, 故 $f^{\prime}$ 相较于 $f$, 在 $t$ 为偶数时, 少了一个正系数; $t$ 为奇数时少了一个负系数, 充分性得证.

必要性. 假设 $n-1$ 次多项式 $g$ 系数非零且有 $n-1$ 个互异实根,令 $f(x)=x g(x)+\varepsilon$, 其中 $|\varepsilon|$ 充分小, 则 $f$ 的 $n$ 个根均为实数, 其中一个根接近于 0 , 其余 $n-1$ 个根充分接近 $g$ 的 $n-1$ 个根. 根据 $\varepsilon$ 正负的选取, $f$ 接近于 0 的根分别为负、正根. 同时显然, $f$ 和 $g$ 的正负系数个数仅差异在 $\varepsilon$, 必要性得证, 断言成立.

利用断言, 所有使 $P(s, t, n)$ 为真的 $(s, t, n)$ 可由 $(1,0,1),(0,1,1)$ 开始 (也可以视作从 $(0,0,0)$ 开始), 按如下规则递推得:

$$
P(s, t, n)=\text { true } \Rightarrow\left\{\begin{array}{l}
P(s, t, n+1)=P(s+1, t+1, n+1)=\text { true, } t \text { odd } \\
P(s, t+1, n+1)=P(s+1, t, n+1)=\text { true, } t \text { even }
\end{array}\right.
$$

容易归纳说明, 使 $P(t, t, n)$ 为真的充要条件是 $1 \leq t \leq \frac{2 n}{3}$.
评注 考虑到系数正负性要得到控制, 可以利用求导进行反向递推; 递推构造时, 可以乘上 $x$ 再进行微扰, 以控制系数符号. 本题结论精妙, 但做起来并不容易。

利用笛卡尔符号法则 (Descartes' rule of signs) 同样可以建立起根与系数的关系. 法则表明, 多项式的正根的个数不大于相邻系数符号的变化次数, 而符合要求的 $f$ 有 $t$ 个正根, 变号次数不大于 $2(n-t)$, 解得 $t \leq \frac{2 n}{3}$.

题 5 给定非负实数 $x, y, z$, 记 $a=x^{2}(y-z)^{4}, b=y^{2}(z-x)^{4}, c=z^{2}(x-y)^{4}$.证明:

$$
(a+b+c)^{3} \geq \frac{9}{2}(a \sqrt{b}+b \sqrt{c}+c \sqrt{a})^{2} .
$$

证明 利用柯西 (Cauchy) 不等式,

$$
9\left(\sum_{c y c} a \sqrt{b}\right)^{2}=\left(\sum_{c y c} \sqrt{a}(2 \sqrt{a b}+c)\right)^{2} \leq(a+b+c)\left(\sum_{c y c}(2 \sqrt{a b}+c)^{2}\right) .
$$

不等式两边约去 $a+b+c$ 并展开, 化简, 只需证明

$$
a^{2}+b^{2}+c^{2} \geq 4 \sqrt{a b c}(\sqrt{a}+\sqrt{b}+\sqrt{c}) .
$$

不妨设 $x \geq y \geq z$, 则 $\sqrt[4]{a}=\sqrt{x}(y-z), \sqrt[4]{b}=\sqrt{y}(x-z), \sqrt[4]{c}=\sqrt{z}(x-y)$.

将

$$
(\sqrt{x}-\sqrt{y})(\sqrt{x}-\sqrt{z})(\sqrt{y}-\sqrt{z}) \geq 0
$$

展开, 化简得 $\sqrt[4]{b} \geq \sqrt[4]{a}+\sqrt[4]{c}$. 平方,

$$
\sqrt{b} \geq \sqrt{a}+2 \sqrt[4]{a c}+\sqrt{c} \geq 4 \sqrt[4]{a c}
$$

于是 $\sqrt{a}+\sqrt{c} \leq \sqrt{b}, \sqrt{a c} \leq \frac{1}{16} b$. 代入得

$4 \sqrt{a b c}(\sqrt{a}+\sqrt{b}+\sqrt{c}) \leq 4 \sqrt{b} \cdot \frac{1}{16} \sqrt{b} \cdot 2 \sqrt{b}=\frac{1}{2} b^{2} \leq b^{2} \leq a^{2}+b^{2}+c^{2}$.

评注 考虑对右式配柯西不等式是自然的想法. 又注意到右边比左边关于 $a, b, c$ 的项多一些, 故必须利用 $a, b, c$ 的表达式将若干项放成一个项, 这一步更需观察力.

题 6 设简单图 $G$ 有 95 个顶点, 2021 条边. 证明: 所有点度数平方和不超过 300000 。

证明 设每个顶点的度依次为 $d_{1} \leq d_{2} \leq \cdots \leq d_{95}$, 则 $0 \leq d_{j} \leq 94$且 $\sum_{j=1}^{95} d_{j}=4042$.
记 $k=43, n=95, e=2021$, 考察度最大的 $k$ 个点的导出子图 $G[S]$,记 $p=|E(G[S])| \leq\left(\begin{array}{l}k \\ 2\end{array}\right)$, 除去这些边后, 剩下的每条边都至少与剩下 $n-k$ 个顶点之一连边, 从而

$$
e-p \leq \sum_{j=1}^{n-k} d_{j} \Rightarrow \sum_{j=n-k+1}^{n} d_{j} \leq e+p
$$

故 $d_{n-k+1} \leq \frac{e+p}{k}$. 利用函数 $f(x)=x^{2}$ 的单调性和凸性, 有

$$
\begin{aligned}
\sum_{j=1}^{n} d_{j}^{2} & =\sum_{j=1}^{n-k} d_{j}^{2}+\sum_{j=n-k+1}^{n} d_{j}^{2} \\
& \leq d_{n-k}^{2} \times \frac{e-p}{d_{n-k}}+\left(d_{n-k+1}^{2} \times \frac{(n-1) k-e-p}{n-1-d_{n-k+1}}+(n-1)^{2} \times \frac{e+p-k d_{n-k+1}}{n-1-d_{n-k+1}}\right) \\
& =(e-p) d_{n-k}+(n-1)(e+p)-((n-1) k-e-p) d_{n-k+1} \\
& \leq(e-p) d_{n-k+1}+(n-1)(e+p)-((n-1) k-e-p) d_{n-k+1} \\
& =(n-1)(e+p)+(2 e-(n-1) k) d_{n-k+1},
\end{aligned}
$$

其中由 $k$ 的选取知 $2 e=(n-1) k$, 故上式不大于

$$
(n-1)(e+p) \leq(n-1)\left(e+\left(\begin{array}{l}
k \\
2
\end{array}\right)\right)=94 \times(2021+903)=274856<300000 .
$$

评注 直接将 $d_{j}$ 放成 94 会接近 400000, 这是由于总有度稍小些的点, 该放缩无法取等. 于是将顶点集划分为两部分分别进行放缩即可.

题 7 设 $p, q$ 是不同的奇素数. 证明: $p$ 是 $q$ 的原根, 当且仅当 $\frac{x^{q}-1}{x-1}$ 在模 $p$意义下是不可约的.

证明 以下均在域 $\mathbb{F}_{p}$ 上的多项式中考虑.

引理 1 设 $g$ 是 $d$ 次不可约多项式, 则 $g \mid x^{p^{d}-1}-1$.

任何一个多项式对 $g$ 作带余除法得到次数小于 $d$ 的多项式, 非零余数共有 $p^{d}-1$ 个, 称它们构成模 $g$ 的一个缩系, 记它们是 $f_{1}, f_{2}, \cdots, f_{p^{d}-1}$. 容易验证 $x f_{1}, x f_{2}, \cdots, x f_{p^{d}-1}$ 也是模 $g$ 的一个缩系, 它们的积模 $g$ 相同, 约去全部 $f_{i}$即得证.

引理 2 设 $g$ 是 $d$ 次不可约多项式, $T$ 是 $k$ 次多项式, 方程 $T(h) \equiv 0$ $(\bmod g)$ 至多有 $k$ 个解.

对 $k$ 归纳. $k=1$ 时, 命题显然. 下设命题对所有次数小于 $k$ 的 $T$ 都成立,考虑次数为 $k$ 的情形. 若存在一个 $T$ 使之有 $k+1$ 个不同解 $h_{0}, h_{1}, h_{2}, \cdots, h_{k}$,记 $T(h)-T\left(h_{0}\right)=\left(h-h_{0}\right) L(h)$, 其中 $L$ 是模 $g$ 意义下的 $k-1$ 次多项式,
但 $h_{1}, h_{2}, \cdots, h_{k}$ 都是它的解, 矛盾.

引理 $3 R(x)=x^{p^{k}}-x$ 是所有次数整除 $k$ 的不可约多项式之积.

一方面, 若 $d \mid k$ 且 $g$ 是 $d$ 次不可约多项式, 由引理 $1, g$ 是 $x^{p^{d}}-x$ 的因式,从而是 $R$ 的因式. 而 $R$ 与其导函数无公共根, 从而 $R$ 无重根, 即全体次数整除 $k$ 的不可约多项式之积整除 $R$.

另一方面, 若 $g$ 是 $d$ 次不可约多项式, 且整除 $R$, 我们说明 $d \mid k$. 不妨设 $d>1$, 则 $g$ 整除 $x^{p^{k}-1}-1$. 由费马小定理, $g$ 整除 $x^{p^{d}-1}-1$. 由欧几里得 (Euclidean) 算法, $g \mid x^{p^{r}-1}-1$, 其中 $r$ 是 $k, d$ 的最大公因数. 对于任一 $r$ 次多项式 $h$,

$$
h(x)^{p^{r}} \equiv h\left(x^{p^{r}}\right) \equiv h(x) \quad(\bmod g(x))
$$

这样的 $h$ 共有 $p^{d}$ 个. 由引理 2 , 方程 $h^{r^{r}} \equiv h(\bmod g)$ 至多 $p^{r}$ 个解, 故 $d \leq r$,这即 $d=r, d \mid k$. 即 $x^{p^{k}}-x$ 整除全体次数整除 $k$ 的不可约多项式之积.

回到原题. 必要性. 记 $f(x)=1+x+\cdots+x^{q-1}, p$ 模 $q$ 的阶为 $k$,则 $f \mid x^{p^{k}}-x$. 引理 3 实质上表明 $f$ 的所有不可约因子的次数都整除 $k$, 故 $f$不可约时, $p-1 \mid k, p$ 是模 $q$ 的原根.

充分性. 若 $p$ 是 $q$ 的原根且 $f$ 可约, 设 $g \mid f, \operatorname{deg} g<q-1, g$ 不可约. 由引理 $1, g \mid x^{p^{\operatorname{deg} g}}-1$. 而 $g \mid x^{q}-1$, 由欧几里得算法, 并注意到 $\operatorname{gcd}\left(p^{\operatorname{deg} g}, q\right)=1$,故 $g \mid x-1$, 这表明 $g=x-1, p=q$, 矛盾.

评注 题目有一定有限域的背景, 了解相关知识做起来会容易很多, 核心是仿照初等数论中利用带余除法、欧几里得算法建立体系的方式在模 $p$ 的多项式环上类似地操作即可. 证明过程中用到的引理 1 即费马小定理, 引理 2 即拉格朗日定理。

题 8 设 $n$ 阶连通图 $G$ 围长为 $2 k$, 最小度数为 $\delta \geq 2$, 半径为 $r(G)=$ $\min _{v \in G} \max _{u \in G} \operatorname{dist}(u, v)$. 证明:

$$
r(G) \leq \frac{k n}{2(\delta-1)^{k-1}}+4 k
$$

证明 ${ }^{[1]}$ 先证明下面的引理.

引理 若 $V(G)$ 的子集 $T$ 满足其中任意两点或者在 $G$ 中相邻, 或者在 $G$中 dist 不小于 $2 k-1$, 则 $n \geq|T|(\delta-1)^{k-1}$.

证明 对于 $v \in T$, 定义 $S(v)=\{u \in V(G): \operatorname{dist}(u, v)=k-1\}$, 则对不同的 $u, v \in T$, 总有 $S(u) \cap S(v)=\varnothing$. 因为若存在 $w \in S(u) \cap S(v)$,
在 $u, v$ 相邻时最短路径 $(u, w),(v, w)$ 的对称差加上边 $(u, v)$ 构成了长度不大于 $2 k-1$ 的圈, 与围长为 $2 k$ 矛盾; 在 $u, v$ 不相邻时, 由三角不等式得 $\operatorname{dist}(u, v) \leq \operatorname{dist}(u, w)+\operatorname{dist}(w, v) \leq 2 k-2$, 矛盾.

再说明 $|S(v)| \geq(\delta-1)^{k-1}$ 对任意 $v \in T$ 成立. 反证法, 取 $2 \leq i \leq k$ 为最小的使 $S_{i}(v)=\{u \in V(G): \operatorname{dist}(u, v)=i-1\}$ 满足 $\left|S_{i}(v)\right|<(\delta-1)^{i-1}$ 的整数.显然 $i \geq 3, i=2$ 时是最小度数 $\delta$ 的定义. 考察不同的 $a, b \in S_{i-1}(v)$, 有如下事实:

1. 所有与 $a, b$ 中至少一者相邻的点都在 $S_{i-2}(v), S_{i-1}(v), S_{i}(v)$ 中.
2. $a, b$ 不相邻, 否则有长度小于 $2 k$ 的圈.
3. $a, b$ 均至多与 $S_{i-2}$ 中一者相邻, 否则有长度小于 $2 k$ 的圈.
4. $a, b$ 在 $S_{i}$ 中没有公共邻点, 否则有长度小于 $2 k$ 的圈.

以上表明 $\left|S_{i}(v)\right| \geq(\delta-1)\left|S_{i-1}(v)\right| \geq(\delta-1)^{i-1}$, 反证假设不成立. 故

$$
n=|V(G)| \geq\left|\bigcup_{v \in T} S(v)\right|=\sum_{v \in T}|S(v)| \geq|T|(\delta-1)^{k-1}
$$

引理得证. 回到原题, 只需找到满足引理条件的较大的 $T$.

为此, 任意取定属于 $G$ 中心的一点 $v_{0}$, 并取定 $G$ 的一条半径路径 $v_{0}, v_{1}, \cdots, v_{r}$, 这里 $r=r(G)$. 待定 $m \in\{1,2, \cdots, r-1\}$, 并令 $v^{\prime}$ 是某个使得 $\operatorname{dist}\left(v_{m}, v^{\prime}\right) \geq r$ 的点, 记 $\operatorname{dist}\left(v_{0}, v^{\prime}\right)=r-t$, 从 $v_{0}$ 到 $v^{\prime}$ 的一条最短路径是 $v_{0}=v_{0}^{\prime}, v_{1}^{\prime}, v_{2}^{\prime}, \cdots, v_{r-t}^{\prime}=v^{\prime}$, 取定 $m=2 k$, 有如下事实:

1. $t \leq m$. 这是因为三角不等式,

$$
r-t+m=\operatorname{dist}\left(v_{0}, v^{\prime}\right)+\operatorname{dist}\left(v_{0}, v_{m}\right) \geq \operatorname{dist}\left(v^{\prime}, v_{m}\right) \geq r .
$$

2. $\operatorname{dist}\left(v_{i}, v_{j}^{\prime}\right) \geq|i-j|$. 这是因为三角不等式,

$$
\operatorname{dist}\left(v_{i}, v_{j}^{\prime}\right) \geq\left|\operatorname{dist}\left(v_{i}, v_{0}\right)-\operatorname{dist}\left(v_{0}, v_{j}^{\prime}\right)\right|=|i-j| .
$$

3. $\operatorname{dist}\left(v_{2 k j+\varepsilon_{1}}, v_{2 k j+\varepsilon_{2}}^{\prime}\right) \geq 2 k-1$, 其中 $\varepsilon_{1}, \varepsilon_{2} \in\{0,1\}$. 这是因为三角不等式,

$$
\begin{aligned}
\operatorname{dist}\left(v_{2 k j+\varepsilon_{1}}, v_{2 k j+\varepsilon_{2}}^{\prime}\right) & \geq\left|\operatorname{dist}\left(v_{m}, v_{2 k j+\varepsilon_{2}}\right)-\operatorname{dist}\left(v_{2 k j+\varepsilon_{1}}, v_{m}\right)\right| \\
& \geq\left(t+2 k j+\varepsilon_{2}\right)-\left(2 k j+\varepsilon_{1}-m\right) \\
& \geq m+\varepsilon_{2}-\varepsilon_{1} \geq 2 k-1 .
\end{aligned}
$$

于是, 在 $r \leq 2 k$ 时命题直接成立; 在 $r>2 k$ 时若令 $x=\left\lfloor\frac{r}{2 k}\right\rfloor$, 并选取 $T$ 为

$$
\begin{gathered}
T=\left\{v_{2 k j+\varepsilon}: 0 \leq j \leq x-1, \varepsilon \in\{0,1\}\right\} \cup\left\{v_{2 k j+\varepsilon}^{\prime}: 1 \leq j \leq x-2, \varepsilon \in\{0,1\}\right\} \\
\cup\left\{v_{2 k(x-1)}^{\prime}\right\} \cup\left\{v_{2 k x}\right\},
\end{gathered}
$$

则 $T$ 中含有 $4 x-2$ 个互异元素, 且它们或者相邻, 或者相距至少为 $2 k-1$. 利
用引理,

$$
\begin{aligned}
& n \geq(4 x-2)(\delta-1)^{k-1} \geq\left(\frac{2 r}{k}-6\right)(\delta-1)^{k-1} \\
& \Rightarrow \quad r \leq \frac{n k}{2(\delta-1)^{k-1}}+3 k<\frac{n k}{2(\delta-1)^{k-1}}+4 k .
\end{aligned}
$$

评注 利用围长为 $2 k$ 的条件可以探索出若干小结论, 证明过程在这些小结论的基础上是自然的. 本题是 Dvorak 等在 2020 证明的结论, 在引理部分 $S_{2}(v)$的界可以改进为 $\delta$, 从而他们论文中的结论是

$$
r(G) \leq \frac{k n}{2 \delta(\delta-1)^{k-2}}+3 k
$$

## 参考文献

[1] Dvořák, V., van Hintum, P., Shaw, A., \& Tiba, M.(2020). Radius, Girth and Minimum Degree. https://arxiv.org/pdf/2009.00741.pdf

