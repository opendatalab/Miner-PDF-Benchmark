# 柳智宇的两个妙解 

冷岗松

柳智宇是 2006 年中国国家队队员, 在第 31 届 IMO 中获得满分金牌. 作为该年国家队的副领队和教练, 柳智宇的数学才华给我留下了深刻印象.

他和人讨论几何题, 不画图不看图, 但是口中便能准确无误说出诸多点线的位置, 从不忘记和混乱, 真可谓 “心中有图” , 令人惊诧. 他的几何和组合都十分突出, 因此造就了一个少见的组合几何高手. 集训队选拔时的几个组合几何难题能解出者寥宍无几, 他提供的解却令人拍案叫绝! 碰巧当年 IMO 第 6 题是一个组合几何难题, 来自各国的所有参赛者仅 3 人做对, 其中就有柳智宇. 协调组专家们认为他的解法比标准答案还漂亮.

2006 年 9 月, 柳智宇进入北京大学数学系. 此后不断传来他的好消息: 成绩优异, 科研上也是崭露头角, 大学毕业前, 他成功申请到麻省理工学院 (MIT) 全额奖学金. 然而, 最后传来了一个准确但令人吃惊的消息: 大学毕业后, 柳来到北京龙泉寺, 成为一名修行居士, 之后出家为僧, 法号圣宇.

对于他的出家, 我无语也不妄评. 或许他的人生注定与佛有缘而最终于数学无缘.

本短文仅介绍柳智宇对于两个组合几何问题的妙解.

2006 年 6 月 15 日至 7 月 5 日中国国家队在清华附中集训. 集训期间, 我选用的训练题中包含了数学家 Granville 和 Roésler 的一个结果.

问题 1 (Granville-Roésler) 设 $A$ 是坐标平面上的一个有限点集. 对任意 $\alpha_{1}=\left(x_{1}, y_{1}\right), \alpha_{2}=\left(x_{2}, y_{2}\right) \in A$, 定义

$$
d\left(\alpha_{1}, \alpha_{2}\right)=\left(c_{1}, c_{2}\right)
$$

其中 $c_{1}=\max \left\{0, x_{1}-x_{2}\right\}, \quad c_{2}=\max \left\{0, y_{1}-y_{2}\right\}$. 记

$$
D(A)=\left\{d\left(\alpha_{1}, \alpha_{2}\right) \mid \alpha_{1} \in A, \quad \alpha_{2} \in A\right\}
$$

证明:

$$
|D(A)| \geq\left(\frac{1}{2}|A|\right)^{\frac{2}{3}}
$$

我们简称这个问题为 G-R 问题. G-R 问题的背景及相关讨论可见 [1].

这个问题有相当的难度, 笔者和几位国家队队员进行过多次讨论. 最后, 柳智宇提出了一个精妙的想法. 根据柳智宇的思路另一位来自天津耀华中学的国家队队员任庆春整理出如下优雅的解法:

解 将 $A$ 中各点的横坐标构成的集合记为 $X, A$ 中各点的纵坐标构成的集合记为 $Y$. 为证 (1) 式, 我们只须证明更强的结论

$$
|D(A)| \geq\left(\frac{|A|}{|X|+|Y|}\right)^{2}
$$

事实上, 若 $|X|,|Y|$ 中有一个大于等于 $\left(\frac{1}{2}|A|\right)^{\frac{2}{3}}$, 则由明显的不等式 $|D(A)| \geq$ $|X|,|D(A)| \geq|Y|$ 知 (1) 显然成立. 若 $|X|<\left(\frac{1}{2}|A|\right)^{\frac{2}{3}}$ 且 $|Y|<\left(\frac{1}{2}|A|\right)^{\frac{2}{3}}$, 这时由 (2)便知 (1) 成立.

下面证明 (2) 成立.

先证如下引理.

引理 设 $x_{0}>x_{1}>x_{2}>\cdots>x_{s}, y_{0}<y_{1}<y_{2}<\cdots<y_{t}, B=\left\{\left(x_{0}, y_{i}\right) \mid\right.$ $i=1,2, \cdots, t\} \cup\left\{\left(x_{i}, y_{0}\right) \mid i=1,2, \cdots, s\right\}$, 则 $|D(B)| \geq s t$.

事实上, 对任意 $1 \leq i \leq s$ 和 $1 \leq j \leq t$ 有

$$
d\left(\left(x_{0}, y_{i}\right),\left(x_{i}, y_{0}\right)\right)=\left(x_{0}-x_{i}, y_{i}-y_{0}\right)
$$

因此

$$
|D(B)| \geq\left|\left\{\left(x_{0}-x_{i}, y_{i}-y_{0}\right) \mid 1 \leq i \leq s, 1 \leq j \leq t\right\}\right|=s t .
$$

回到原题.

因 $A$ 是有限集, 不妨设 $X=\left\{x_{1}, x_{2}, \cdots, x_{p}\right\}$ 且 $x_{1}>x_{2}>\cdots>x_{p}, Y=$ $\left\{y_{1}, y_{2}, \cdots, y_{q}\right\}$ 且 $y_{1}<y_{2}<\cdots<y_{q}$. 记 $k=\frac{|A|}{|X|+|Y|}=\frac{|A|}{p+q}$, 下面只须证明

$$
|D(A)| \geq k^{2}
$$

下面用归纳法证明 $(*)$ 成立.

当 $p=1$ 时, 此时所有点都在 $x=x_{1}$ 这条直线上, 因此 $|A| \leq q<p+q$, 这时 $k<1$, 而 $D(A)$ 中至少包含 $(0,0)$, 故 $(*)$ 显然成立. 同理当 $q=1$ 时, $(*)$ 也成立.

假设 $(*)$ 对 $(p-1, q)$ 和 $(q, p-1)$ 成立, 其中 $p, q \geq 2$. 下证 $(*)$ 对 $(p, q)$ 成立.设 $C_{1}=\left\{\left(x_{1}, y_{i}\right) \mid j=1,2, \cdots, q\right\}, C_{2}=\left\{\left(x_{i}, y_{1}\right) \mid j=1,2, \cdots, p\right\}$, 下面分两种情况讨论:

(1) 如果 $\left|C_{1}\right|>k$ 且 $\left|C_{2}\right|>k$, 令 $C=C_{1} \cup C_{2}$, 则由引理知 $|D(C)| \geq k^{2}$, 因此
更有 $|D(A)| \geq|D(C)| \geq k^{2}$.

(2) 如果 $\left|C_{1}\right| \leq k$ 或 $\left|C_{2}\right| \leq k$, 由对称性, 不妨设 $\left|C_{1}\right| \leq k$, 这时记 $A^{\prime}=A \backslash C_{1}$,则

$$
\left|A^{\prime}\right|=|A|-\left|C_{1}\right| \geq|A|-k .
$$

对 $A^{\prime}$ 用归纳假设可得

$$
\left|D\left(A^{\prime}\right)\right| \geq\left(\frac{|A|-k}{p-1+q}\right)^{2} \geq\left(\frac{k(p+q)-k}{p+q-1}\right)^{2}=k^{2}
$$

故

$$
|D(A)| \geq\left|D\left(A^{\prime}\right)\right| \geq k^{2}
$$

结论成立.

综上便知 $(*)$ 对 $(p, q)$ 成立, $(*)$ 得证.

另一个问题则是 2006 年 3 月在沈阳东北育才中学举行的国家集训队的选拔考试第 4 次小考中, 林常教授提供的如下问题:

问题 2 (林常) 给定正整数 $m, n$. 将 $m \times n$ 棋盘上的 $m n$ 个 $1 \times 1$ 方格交替地染成红蓝两色 (有公共边的任两个方格不同色, 左下角方格为红色). 此时从左下到右上的对角线被染成一些红、蓝线段 (每条线段与它所在的方格同色), 试求所有红色线段的长度之和.

这是一个颇有难度的问题, 得满分者不多. 这个问题的背景分析可见 [2]. 柳智宇提供了一个精妙的解法, 它不仅简单, 而且很好地揭示了问题的本质: 对于 $a \times b$ 棋盘, 其中, $\operatorname{gcd}(a, b)=1$, 如果将对角线 $a b$ 等分, 则红线段长度比蓝线段长度恰好多一个等分单位.

解 考虑 $a \times b$ 棋盘, 其中, $\operatorname{gcd}(a, b)=1$, 且 $a, b$ 均为大于 1 的奇数.

将对角线 $a b$ 等分, 记第 $i$ 等分的线段为 $d_{i}(i=1,2, \cdots, a b), i$ 除以 $a, b$ 的最小正余数分别为 $p_{i}, q_{i}$. 容易证明, 当且仅当 $p_{i}+q_{i}$ 为偶数时, $d_{i}$ 为红色.

实际上, 当 $d_{i}$ 的右端点不在格线上时, $d_{i}$ 与 $d_{i+1}$ 同色. 此时, $p_{i+1}=$ $p_{i}+1, q_{i+1}=q_{i}+1$ 同时成立, 所以,

$$
p_{i}+q_{i} \equiv p_{i+1}+q_{i+1} \quad(\bmod 2)
$$

当 $d_{i}$ 的右端点在格线上时, $d_{i}$ 与 $d_{i+1}$ 异色. 此时, $p_{i+1}=p_{i}+1\left(p_{i}, p_{i+1}\right.$ 不同奇偶 $), q_{i+1}=1, q_{i}=b\left(q_{i}, q_{i+1}\right.$ 同为奇 $)$, 或者 $q_{i+1}=q_{i}+1\left(q_{i}, q_{i+1}\right.$ 不同奇偶 $)$,
$p_{i+1}=1, p_{i}=a\left(p_{i}, p_{i+1}\right.$ 同为奇 $)$, 于是,

$$
p_{i}+q_{i} \equiv 1+p_{i+1}+q_{i+1} \quad(\bmod 2) .
$$

所以, 当且仅当 $p_{i}+q_{i}$ 与 $p_{i+1}+q_{i+1}$ 同奇偶时, $d_{i}$ 与 $d_{i+1}$ 同色. 又 $d_{1}$ 为红色, $p_{1}+q_{1}=2$ 为偶数, 因此, 当且仅当 $p_{i}+q_{i}$ 为偶数时, $d_{i}$ 为红色.

对任何数对 $(s, t)$, 其中 $s \in\{1,2, \cdots, a\}, t \in\{1,2, \cdots, b\}$, 因为 $(a, b)=1$, 由中国剩余定理, 都有唯一的 $i \in\{1,2, \cdots, a b\}$, 使

$$
i \equiv s \quad(\bmod a) \quad \text { 且 } \quad i \equiv t \quad(\bmod b) .
$$

由于 $a, b$ 为奇数, 所以, $\{1,2, \cdots, a\}$ 中共有 $\frac{a+1}{2}$ 个奇数, $\frac{a-1}{2}$ 个偶数; $\{1,2, \cdots, b\}$ 中有 $\frac{b+1}{2}$ 个奇数, $\frac{b-1}{2}$ 个偶数. 因此, 使 $s, t$ 同奇偶的数对 $(s, t)$的个数为

$$
\frac{b+1}{2} \cdot \frac{a+1}{2}+\frac{b-1}{2} \cdot \frac{a-1}{2}=\frac{a b+1}{2} .
$$

于是, 有 $\frac{a b+1}{2}$ 条等分线段为红色.

而每条等分线段的长度为 $\frac{\sqrt{a^{2}+b^{2}}}{a b}$, 故

$$
S_{\text {红 }}=\frac{a b+1}{2} \cdot \frac{\sqrt{a^{2}+b^{2}}}{a b}=\frac{a b+1}{2 a b} \sqrt{a^{2}+b^{2}} \text {. }
$$

## 参考文献

[1] A. Gramville, F. Roesler, The Set of Diffierences of a Given Set, Amer. Math. Monthly. 106(1999),338-344.

[2] 冯跃峰, 2006 中国国家集训队测试题欣赏, 中等数学. 4(2007), 15-22.

