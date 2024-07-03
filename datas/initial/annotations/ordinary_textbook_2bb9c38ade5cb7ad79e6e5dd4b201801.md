# 好题与妙解（四） 

## -2016 新星秋季精品班两次测试题

## 冷岗松叶思

2016 年上海数学新星秋季的精品班举行了两次测试 (小考). 每次测试四题, 时间 2 小时. 本文介绍这两次测试试题的解答. 我们将用题 $1 . x$ 表示第 1 次测试的第 $x$ 题, 题 $2 . y$ 的意义类似.

题 1.1 设 $k>n>1$ 是整数, $a_{1}, a_{2}, \cdots, a_{k} \in(0,1)$. 证明:

$$
\min \left\{a_{1}\left(1-a_{2}\right)^{n}, a_{2}\left(1-a_{3}\right)^{n}, \cdots, a_{k}\left(1-a_{1}\right)^{n}\right\} \leq \frac{n^{n}}{(n+1)^{n+1}}
$$

证法一 由算术-几何平均值不等式可得

$$
\begin{aligned}
x(1-x)^{n} & =\frac{1}{n} \cdot n x(1-x)^{n}=\frac{1}{n} \cdot n x \cdot \underbrace{(1-x) \cdots(1-x)}_{n \text { 个 }} \\
& \leq \frac{1}{n}\left(\frac{n x+n(1-x)}{n+1}\right)^{n+1}=\frac{n^{n}}{(n+1)^{n+1}}, \forall x \in(0,1) .
\end{aligned}
$$

因此

$$
\prod_{i=1}^{k} a_{i}\left(1-a_{i}\right)^{n} \leq\left(\frac{n^{n}}{(n+1)^{n+1}}\right)^{k}
$$

上式可写为

$$
\prod_{i=1}^{k} a_{i}\left(1-a_{i+1}\right)^{n} \leq\left(\frac{n^{n}}{(n+1)^{n+1}}\right)^{k}
$$

其中 $a_{k+1}=a_{1}$.

故由抽屉原理知一定存在 $1 \leq i \leq k$ 使得 $a_{i}\left(1-a_{i+1}\right)^{n} \leq \frac{n^{n}}{(n+1)^{n+1}}$.

证法二 设 $\max _{1 \leq i \leq n}\left(a_{i}\right)=a_{j}$, 则左边 $\leq a_{j-1}\left(1-a_{j}\right)^{n} \leq a_{j}\left(1-a_{j}\right)^{n}=\frac{1}{n} \cdot n a_{j}\left(1-a_{j}\right)^{n}$

$$
\leq \frac{1}{n}\left(\frac{n a_{j}+n\left(1-a_{j}\right)}{n+1}\right)^{n+1}=\frac{n^{n}}{(n+1)^{n+1}} .
$$

证法三 若存在 $1 \leq i \leq n$ 使得 $a_{i} \leq a_{i+1}$, 其中 $a_{n+1}=a_{1}$, 则

$$
\begin{aligned}
\text { 左边 } & \leq a_{i}\left(1-a_{i+1}\right)^{n} \leq a_{i+1}\left(1-a_{i+1}\right)^{n} \\
& \leq \frac{1}{n} \cdot n a_{i+1}\left(1-a_{i+1}\right)^{n} \\
& \leq \frac{1}{n}\left(\frac{n a_{i+1}+n\left(1-a_{i+1}\right)}{n+1}\right)^{n+1} \\
& =\frac{n^{n}}{(n+1)^{n+1}} .
\end{aligned}
$$

若对任意 $1 \leq i \leq n, a_{i} \leq a_{i+1}$ 都不成立, 则有 $a_{1}>a_{2}>\cdots>a_{n}>a_{1}$, 矛盾! 证毕.

题 1.2 设 $O$ 是 $\triangle A B C$ 的外心, $\triangle B O C$ 的外接圆的一条切线 $l$ 与边 $A B, A C$ 分别交于点 $D, E(D, E \neq A)$. 点 $A^{\prime}$ 是 $A$ 关于直线 $l$ 的对称点. 证明: $\triangle A^{\prime} D E$ 的外接圆与 $\triangle A B C$ 的外接圆相切.

![](https://cdn.mathpix.com/cropped/2024_02_26_9fe99bc1230e55a444f9g-2.jpg?height=556&width=488&top_left_y=1361&top_left_x=790)

证法－记直线 $l$ 与 $\triangle B O C$ 的外接圆的切点为 $K$. 令 $\triangle B D K$ 与 $\triangle C E K$的外接圆的交点为 $X, X \neq K$. 因为

$$
\begin{aligned}
\angle B X C & =\angle B X K+\angle K X C \\
& =\angle A D K+\angle K E A \\
& =180^{\circ}-\angle C A B,
\end{aligned}
$$

所以点 $X$ 在 $\triangle A B C$ 外接圆 $\kappa$ 上.

另一方面，

$$
\angle D X E=\angle D X K+\angle K X E
$$

$$
\begin{aligned}
& =\angle D B K+\angle K C E \\
& =\angle C K B-\angle C A B \\
& =\angle C A B=\angle D A^{\prime} E
\end{aligned}
$$

所以 $X$ 也在 $\triangle A^{\prime} D E$ 的外接圆 $\kappa_{1}$ 上.

下面我们将证明圆 $\kappa, \kappa_{1}$ 切于点 $X$.

如果 $P$ 是直线 $C K$ 和 $X D$ 的交点, 则

$$
\begin{aligned}
\angle X P C & =\angle X D E-\angle C K E \\
& =\angle X B K-\angle C B K \\
& =\angle X B C,
\end{aligned}
$$

这说明点 $P$ 位于圆 $\kappa$ 上. 类似地, 直线 $B K$ 和 $X E$ 的交点 $Q$ 在圆 $\kappa$ 上.

又由 $\angle X P Q=\angle X B Q=\angle X D K$, 便知 $P Q / / D E$.

因此 $\triangle X D E$ 和 $\triangle X P Q$ 是关于位似中心 $X$ 位似, 所以它们的外接圆相切于点 $X$.

证法二 令直线 $B K$ 和 $C K$ 与 $\triangle A B C$ 的外接圆分别相交于点 $Q$ 和点 $P$.

因为 $\angle C P Q=\angle C B Q=\angle C K E$, 我们有 $P Q / / D E$.

令直线 $D P$ 和 $E Q$ 相交于点 $X$. 因为点 $D=P X \cap A B, K=P C \cap Q B$, $E=A C \cap Q X$ 三点共线, 由 Pascal 的逆定理得 $X$ 在由点 $A, B, C, P, Q$ 形成的同一个圆上.

由于 $\angle D K B=\angle K C B=\angle P Q X$, 则 $D E / / P Q$, 因此 $\triangle X D E \sim \triangle X P Q$,所以它们的外接圆彼此相切于位似中心 $X$.

最后, 注意到

$$
\begin{aligned}
\angle D X E & =\angle P X Q=\angle P C A+\angle A B Q \\
& =\angle B K C-\angle B A C \\
& =\angle B A C=\angle D A^{\prime} E,
\end{aligned}
$$

所以点 $A^{\prime}$ 在 $\triangle D E X$ 的外接圆上.

题 1.3 设 $2=p_{1}<p_{2}<\cdots$ 是全体素数. 证明: 对 $n>1, p_{1} p_{2} \cdots p_{n}-1$不是整数的完全方幂.

证明 设有 $n>1$, 使 $p_{1} \cdots p_{n}-1=a^{k}$ (1), 则 $a>1$, 从而 $a$ 有素因子, 设素数 $p \mid a$. 则 $p \geq p_{n+1}$ (若 $p \leq p_{n}$, 则 $p \mid p_{1} \cdots p_{n}$, 由 (1) 知 $p \mid 1$, 矛盾).
我们证明 $k<n$. 因为若 $k \geq n$, 则 (1) 的右边 $\geq p^{k} \geq p^{n} \geq p_{n+1}^{n}$. 而 (1) 的左边 $<p_{n}^{n}-1<p_{n+1}^{n}$, 矛盾. 故 $1<k<n$.

设 $q$ 是 $k$ 的一个素因子, 则由 $q<n<p_{n}$ 可知 $q$ 是某个 $p_{i}, i=1, \cdots, n-1$.

记 $x=a^{\frac{k}{q}}$, 则 (1) 化为

$$
p_{1} \cdots p_{n}-1=x^{q} .
$$

首先, $q$ 必是奇素数. 因为若 $q=2$, 则由于 $3 \nmid x$, 故 $x^{2} \equiv 1(\bmod 3)$, 但 (2)左边 $\equiv 0-1=2(\bmod 3)$, 矛盾. 故 $q$ 是奇素数. 由 (2) 推出 $x^{q} \equiv-1(\bmod q)$ (因 $q$ 是 $p_{1}, \cdots, p_{n}$ 之一).

结合费马小定理推出 $x \equiv-1(\bmod q)\left(\right.$ 因 $\left.x^{q} \equiv x(\bmod q)\right)$, 即 $x=$ $-1+q A$, 故

$$
\begin{aligned}
x^{q} & =(-1+q A)^{q}=-1+q A\left(\begin{array}{l}
q \\
1
\end{array}\right)+(q A)^{2}\left(\begin{array}{l}
q \\
2
\end{array}\right)+\cdots \\
& \equiv-1 \quad\left(\bmod q^{2}\right) .
\end{aligned}
$$

即 $q^{2} \mid x^{q}+1$, 由 (2) 知 $q^{2} \mid p_{1} \cdots p_{n}$, 这不可能 (因 $p_{1}, \cdots, p_{n-1}$ 互不相同).

题 1.4 一个古代部落用一种语言, 它的词仅由两个字母 $A, B$ 构成. 研究者发现长度相等的任何两个词至少有三个位置不同. 例如: 词 $A B B A A$ 和词 $A A A A B$ 在第 2, 第 3 和第 5 个位置不同.

设整数 $n \geq 3$. 证明: 在这种语言中, 长度为 $n$ 的词不能多于 $\left\lfloor\frac{2^{n}}{n+1}\right\rfloor$ 个.

证明 设 $C$ 表示长度为 $n$ 的所有由 $A, B$ 构成的字串, 则有 $|C|=2^{n}$. 如果对 $\forall x, y \in C$, 令 $d(x, y)$ 表示 $x$ 与 $y$ 对应位置字母不同的个数 (即定义距离). 显然地 $d(x, x)=0, d(x, y)=d(y, x)$. 对 $\forall x \in C$, 我们定义 $C_{x}=\{y \in C \mid d(x, y) \leq 1\}$.则 $\left|C_{x}\right|=n+1$.

如果 $a, b$ 是这种给定语言中的长度为 $n$ 的两个词, 则 $d(a, b) \geq 3$, 因此

$$
C_{a} \cap C_{b}=\emptyset .
$$

令 $D$ 是这种语言中长度为 $n$ 的所有词的集合, 则

$$
\bigcup_{a \in D} C_{a} \subset C
$$

注意到 $\left\{C_{a}\right\}_{a \in D}$ 是互不相交的, 则

$$
\left|\bigcup_{a \in D} C_{a}\right| \leq|C| \text {, 且 }\left|\bigcup_{a \in D} C_{a}\right|=(n+1) \cdot|D| \text {. }
$$

因此

$$
(n+1) \cdot|D| \leq 2^{n} \text {. }
$$

故

$$
|D| \leq \frac{2^{n}}{n+1}
$$

结论成立.

题 2.1 设 $P$ 是 $\triangle A B C$ 的边 $B C$ 内的一点 (不同于 $B$ 和 $C$ ), $I_{1}, I_{2}$ 分别是 $\triangle A B P$ 和 $\triangle A P C$ 的内心. $\triangle I_{1} P I_{2}$ 的外接圆与边 $B C$ 相交于 $P$ 和 $Q$. 证明: $A B+Q C=A C+Q B$.

证明 不失一般性, 不妨设 $Q$ 在线段 $P C$ 上,

令 $\omega_{1}$ 和 $\omega_{2}$ 分别表示 $\triangle A B P$ 和 $\triangle A P C$ 的内切圆. 令关于圆 $\omega_{1}$ 和 $\omega_{2}$ 的内部的切线 $l$ (不同于 $A P$ ) 与边 $B C$ 交于 $Q^{\prime}$. 我们证明 $I_{1}, P, Q^{\prime}$ 和 $I_{2}$ 是共圆的, 即有 $Q^{\prime} \equiv Q$. 令 $R$ 是直线 $l$ 和 $A P$ 的交点, 由于 $I_{1}$ 和 $I_{2}$ 分别位于 $\angle P Q^{\prime} R$

![](https://cdn.mathpix.com/cropped/2024_02_26_9fe99bc1230e55a444f9g-5.jpg?height=286&width=360&top_left_y=1022&top_left_x=1382)
的内角平分线和外角平分线上, 我们有 $\angle I_{1} Q^{\prime} I_{2}=90^{\circ}$.

类似地, 我们有 $\angle I_{1} P I_{2}=90^{\circ}$. 因此, 这个四边形 $I_{1} P Q^{\prime} I_{2}$ 在一个圆上, 所以 $Q^{\prime} \equiv Q$. 又注意到

$$
D P=\frac{P B+P A-A B}{2}, \quad P E=\frac{P C+P A-A C}{2},
$$

故

$$
D P=Q E=P E-P Q \text {. }
$$

于是

$$
P Q=P E-D P=\frac{A B+P C-A C-P B}{2} .
$$

因此

$$
\begin{aligned}
A C+Q B & =A C+B P+2 P Q-P Q \\
& =A B+P C-P Q=A B+Q C .
\end{aligned}
$$

题 2.2 求所有正整数 $n$ 使得存在 $n$ 的一个因子 $d$ 满足

$$
d n+1 \mid d^{2}+n^{2}
$$

解 设 $n=a d$, 则条件 $d n+1 \mid d^{2}+n^{2}$ 可重写为 $a d^{2}+1 \mid d^{2}+a^{2} d^{2}$. 因此

$$
a d^{2}+1 \mid d^{2}+a^{2} d^{2}-a \cdot\left(a d^{2}+1\right)=d^{2}-a
$$

(1) 若 $d^{2}-a>0$, 则由 $(*)$ 知

$$
d^{2}-a \geq a d^{2}+1
$$

注意到 $a$ 是正整数便有

$$
d^{2} \geq a d^{2}+a+1>d^{2}
$$

矛盾!

(2) 若 $d^{2}-a<0$, 则 $a-d^{2}>0$, 由 $(*)$ 可得

$$
a-d^{2} \geq a d^{2}+1
$$

又 $d$ 是正整数, 于是

$$
a \geq a d^{2}+1+d^{2}>a
$$

矛盾!

由 (1), (2) 立得 $d^{2}-a=0$, 即 $a=d^{2}$. 此时便有 $n=d^{3}$, 即 $n$ 为立方数.

另一方面, 设 $n$ 为立方数, $n=d^{3}$, 则有

$$
d^{4}+1 \mid d^{2}+d^{6}=d^{2}\left(d^{4}+1\right),
$$

满足要求.

故满足题意的 $n$ 是全体立方数.

题 2.3 设 $P(z)=a z^{3}+b z^{2}+c z+d$, 其中 $a, b, c, d$ 均为复数, 且满足 $|a|=|b|=|c|=|d|=1$. 证明: 存在一个模为 1 的复数 $z$ 使得 $|P(z)| \geq \sqrt{6}$.

证明 不妨设 $d=1$, 否则用 $\left(\frac{a}{d}, \frac{b}{d}, \frac{c}{d}, 1\right)$ 代替 $(a, b, c, d)$.

再不妨设 $a=1$, 否则用 $\varepsilon z$ 代替 $z$, 这里 $\varepsilon$ 是 $\varepsilon^{3} a=1$ 的某个复数. 此时

$$
P(z)=z^{3}+b z^{2}+c z+1 .
$$

再设 $w=e^{i \frac{2 \pi}{3}}$, 则

$$
\begin{aligned}
& |P(1)|^{2}+|P(w)|^{2}+\left|P\left(w^{2}\right)\right|^{2} \\
= & (2+b+c)(2+\bar{b}+\bar{c})+\left(2+w^{2} b+w c\right)\left(2+w \bar{b}+w^{2} \bar{c}\right) \\
& +\left(2+w b+w^{2} c\right)\left(2+w^{2} \bar{b}+w \bar{c}\right)=18
\end{aligned}
$$

因此 $|P(1)|,|P(w)|,\left|P\left(w^{2}\right)\right|$ 中至少有一个不小于 $\sqrt{6}$, 结论得证.
题 2.4 求同时满足下面条件的正整数集 $A=\left\{a_{1}, a_{2}, \cdots, a_{1000}\right\}$ 的个数:

(1) $a_{1}<a_{2}<\cdots<a_{1000} \leq 2014$;

(2) $\left\{a_{i}+a_{j} \mid 1 \leq i, j \leq 1000\right.$, 且 $\left.i+j \in A\right\} \subseteq A$.

解 如果 $A$ 一定具有 $B \cup C$ 的形式，其中 $C$ 是 $\{2001, \cdots, 2014\}$ 的子集, $B=\{1,2, \cdots, 1000-|C|\}$, 则我们称 $A$ 为 “好集” . 因 $\{2001, \cdots, 2014\}$ 共有 $2^{14}$ 个子集. 所以好集个数也是 $2^{14}$ 个.

下面我们证明满足要求的集合有 $2^{14}$ 个. 为此, 我们仅须证明:

(i) 每一个好集均满足要求;

(ii) 满足要求的集一定是好集.

为叙述方便, 记 $S=\left\{a_{i}+a_{j} \mid 1 \leq i, j \leq 1000\right.$ 且 $\left.i+j \in A\right\}$.

先证 (i). 设 $A$ 是一个好集,则 $|A|=1000$. 且不妨设

$$
A=\left\{a_{1}, \cdots, a_{1000}\right\}, \quad a_{1}<a_{2}<\cdots<a_{1000}<2014 .
$$

对 $\forall i, j \leq 1000, i+j \in A$ 知 $i+j \leq 2000$, 因此 $i+j \in B$.

因此存在一个 $k \leq 100-|C|$ 使得 $i+j=a_{k}=k$. 又因为 $a_{k} \leq 100-|C|$,于是也有 $i, j \leq 100-|C|$, 因此 $a_{i}=i, a_{j}=j$, 这意味着 $a_{i}+a_{j}=i+j=$ $a_{k} \in A$. 这说明 $S \subseteq A$, 即好集 $A$ 满足要求.

再证 (ii). 设 $A$ 是满足要求的集. 若存在整数 $1 \leq k \leq 1000$ 使得 $a_{k} \in$ $\{1001, \cdots, 2000\}$, 则我们有 $a_{k}=1000+i, i \in[1,1000]$. 因此 $a_{1000}+a_{i} \in S$,但 $a_{1000}+a_{i}>a_{1000}$, 矛盾!

这说明 $A$ 一定能写成两个不相交集合 $B, C$ 的并, 且具有形式 $B \cup C$. 其中 $C \subseteq\{2001, \cdots, 2014\}, B \subseteq\{1,2, \cdots, 1000\}$. 记 $b=|B|$, 因为 $C$ 至多有 14 个元, 故 $b \geq 986$.

为了证明 $A$ 是好的, 我们仅须证明 $B=\{1,2, \cdots, b\}$. 为此, 只须证明 $B$ 的最大元 $a_{b}$ 等于 $b$. 若不然, 设 $a_{b} \neq b$, 因为 $|B|=b$, 所以 $a_{b}>b$.

令 $i=a_{b}-b$, 则 $b+i=a_{b} \leq 1000$, 于是 $i \leq 1000-b \leq 14<b$. 因此 $a_{i} \leq 1000, a_{b}+a_{i} \leq 2000$. 又因为 $i+b=a_{b} \in A$, 所以 $a_{b}+a_{i} \in S \subset A$, 故 $a_{b}+a_{i} \in B$, 这与 $a_{b}$ 的最大性矛盾. 因此 $a_{b}=b$, 故 $A$ 是好的, 证毕.

注 两套试题的 8 个题目均非原创, 其中题 1.2 是 2016 年塞尔维亚 (SMO)试题, 题 1.4 是 2016 年罗马尼亚 (RMO) 试题, 题 2.4 是 2016 年荷兰国家队选拔 (DTST) 试题. 其它题目均难以追溯到它们的准确出处.

