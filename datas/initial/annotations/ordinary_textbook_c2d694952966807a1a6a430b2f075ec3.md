数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2019 年春季上海新星数学奥林匹克试题解析 

吴尉迟 1, 罗振华 ${ }^{2}$, 韩新栤 $^{3}$, 冷岗松 1

(1. 上海大学, 200444; 2. 华东师范大学, 200241; 3. 浙江省乐清市知临中学, 325600)

2019 年春季上海新星数学奥林匹克于 2019 年 4 月 24 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答.

## I. 试 题

1. 若正整数能被其最大素因子的平方整除, 则称其为 “好数”. 若 $x$ 与 $x+1$ 都是好数, 则称 $x$ 是 “超级好数”. 证明: 存在无穷多个超级好数.

(清华大学 孙孟越 供题)

2. 如图, 点 $O$ 是圆 $\Omega$ 的圆心, 圆 $\Omega$ 与圆 $\omega$ 内切于点 $T$. 圆 $\Gamma$ 过点 $O, T$ 且圆心在 $\omega$ 上. $\Gamma$ 分别与 $\Omega, \omega$ 交于不同于 $T$ 的两点 $A, B$, 过 $T$ 作 $\Gamma$ 的切线与 $\omega$ 交于不同于 $T$的点 $C$. 证明: $T B^{2}=T A \cdot T C$.

(中国人民大学附属中学 张端阳供题)

3. 设 $n \in \mathbb{N}^{*}$ 不为 2 的幂. 证明: $n^{n}$ 可以表示为

![](https://cdn.mathpix.com/cropped/2024_02_26_861c1c79cdef1d87bc1cg-01.jpg?height=486&width=374&top_left_y=1453&top_left_x=1366)

$$
n^{n}=a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}
$$

其中 $a_{i}$ 为正整数, 且 $n \nmid a_{i}, i=1,2, \cdots, n$.

(北京大学 饶家鼎 供题)

4. 设整数 $n \geq 2$. 不全为零的实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{i=1}^{n} x_{i}=0$, 且对任意正实数 $t$, 至多有 $\frac{1}{t}$ 对 $(i, j)$, 使得 $\left|x_{i}-x_{j}\right| \geq t$. 证明:

$$
\sum_{i=1}^{n} x_{i}^{2}<\frac{1}{n}\left(\max _{1 \leq i \leq n} x_{i}-\min _{1 \leq i \leq n} x_{i}\right) .
$$

修订日期: 2019-05-03.

5. 已知四边形 $A B C D$ 有内切圆, 圆心为 $I$, 直线 $A C, B D$ 交于 $K$, 直线 $A B, D C$ 交于 $E$, 直线 $A D, B C$ 交于 $F$, 设 $\triangle A B K$ 与 $\triangle C D K$ 的外接圆交于另一点 $Q, \triangle A D K$ 与 $\triangle B C K$ 的外接圆交于另一点 $P$. 若 $E, P, Q, F$ 四点共圆, 证明: 点 $I$ 也在此圆上.

(河南省郑州市一中 张甲 供题)

6. 设 $n$ 是给定的正整数,一个集族 $\Gamma$ 满足:

(1) $\left|\bigcup_{A \in \Gamma} A\right|=n$;

(2) 若 $A, B \in \Gamma$, 则存在 $C \in \Gamma$ 使得 $A \triangle B \subset C$, 其中 $A \triangle B=(A \backslash B) \bigcup(B \backslash A)$.

证明: $\max _{A \in \Gamma}|A|>\frac{n}{2}$.

(上海大学冷岗松 供题)

## II. 解 答

题 1 若正整数能被其最大素因子的平方整除, 则称其为 “好数”. 若 $x$ 与 $x+1$ 都是好数, 则称 $x$ 是 “超级好数”. 证明: 存在无穷多个超级好数.

证法一 对任意奇素数 $p$, 我们证明 $4 p^{2}(p-1)(p+1)$ 是超级好数.

注意到 $\left(2 p^{2}-1\right)^{2}$ 是平方数, 从而它一定是好数. 又

$$
\left(2 p^{2}-1\right)^{2}-1=2 p^{2}\left(2 p^{2}-2\right)=4 p^{2}(p-1)(p+1),
$$

由于 $p+1$ 与 $p-1$ 的最大素因子均小于 $p$, 故 $4 p^{2}(p-1)(p+1)$ 的最大素因子为 $p$, 且 $4 p^{2}(p-1)(p+1)$ 被 $p^{2}$ 整除, 故 $4 p^{2}(p-1)(p+1)$ 也是好数.

综上可知, 存在无穷多个超级好数.

证法二 考虑佩尔方程 $n^{2}-2 m^{2}=1$, 由熟知的结论知该方程有无穷多组正整数解, 取 $(n, m)$ 为其中一组解.

令 $x=2 m^{2}$, 注意到 $m>1$, 从而 $m$ 的最大素因子不小于 2 ,故 $x$ 被其最大素因子的平方整除, 这说明 $x$ 是好数. 注意到 $x+1=n^{2}$ 是完全平方数, 则 $x+1$也是好数, 所以 $x$ 是超级好数. 于是, 存在无穷多个超级好数.

证法三 易知 8 是超级好数. 下面用归纳法构造无穷多个超级好数.

我们证明: 对于超级好数 $k, 4 k(k+1)$ 也是超级好数.
事实上, 由于 $(k, k+1)=1$, 且 $k+1, k$ 均是好数, 故 $4 k(k+1)$ 是好数; 又

$$
4 k(k+1)+1=(2 k+1)^{2}
$$

是完全平方数, 一定是好数, 故 $4 k(k+1)$ 是超级好数.

这就证明了存在无穷多个超级好数.

评注 这是一道简单的数论题, 得分率约 $75 \%$. 本题可以采用直接构造、归纳构造和佩尔方程这三种方法来找到满足题意的数, 是一道训练构造思维的好题.

题 2 如图, 点 $O$ 是圆 $\Omega$ 的圆心, 圆 $\Omega$ 与圆 $\omega$ 内切于点 $T$. 圆 $\Gamma$ 过点 $O, T$ 且圆心在 $\omega$ 上. $\Gamma$ 分别与 $\Omega, \omega$ 交于不同于 $T$ 的两点 $A, B$, 过 $T$ 作 $\Gamma$ 的切线与 $\omega$ 交于不同于 $T$ 的点 $C$. 证明: $T B^{2}=T A \cdot T C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_861c1c79cdef1d87bc1cg-03.jpg?height=622&width=560&top_left_y=1091&top_left_x=748)

证明 设 $O_{1}$ 分别是 $\Gamma$ 的圆心. 由 $O_{1} T \perp T C$, 知 $O_{1} B \perp B C$, 所以 $C B$ 是 $\Gamma$的切线, 于是 $\angle T B C=\angle T A B$. 过 $T$ 作 $\Omega, \omega$ 的公切线 $X Y$. 延长 $T C$ 与 $\Omega$ 交于点 $D$. 因为

$$
\angle T B C=\angle Y T C=\angle Y T D=\angle T A D,
$$

所以 $\angle T A B=\angle T A D$, 从而 $A, B, D$ 三点共线.

我们证明 $T A=T D$. 事实上, 因为

$$
\begin{array}{r}
\angle X T A=\frac{1}{2} \angle T O A=\frac{1}{2} \angle T B A, \\
\angle X T B=180^{\circ}-\angle T O_{1} B=180^{\circ}-2 \angle T A B,
\end{array}
$$

又 $\angle X T A+\angle A T B=\angle X T B$, 所以

$$
\frac{1}{2} \angle T B A+\angle A T B=180^{\circ}-2 \angle T A B .
$$

因为

$$
\angle T B A+\angle A T B+\angle T A B=180^{\circ},
$$

所以 $\angle T B A=2 \angle T A B$. 这样,

$$
\angle D=\angle T B A-\angle B T D=2 \angle T A B-\angle T A B=\angle T A B
$$

所以 $T A=T D$. 此时, $\angle T B C=\angle T A B=\angle D$, 所以 $\triangle T B C \sim \triangle T D B$, 故

$$
T B^{2}=T D \cdot T C=T A \cdot T C .
$$

评注 这是一道简单的几何题. 得分率约 $90 \%$. 上述解法主要是通过导角寻找相似三角形最后证得结论.

题 3 设 $n \in \mathbb{N}^{*}$ 不为 2 的幂. 证明: $n^{n}$ 可以表示为

$$
n^{n}=a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}
$$

其中 $a_{i}$ 为正整数, 且 $n \nmid a_{i}, i=1,2, \cdots, n$.

证法一 因为 $n$ 不是 2 的幂, 故可取 $p$ 为 $n$ 的一个奇素因子.

我们证明如下的加强命题:

对任意正整数 $\alpha, n^{\alpha}$ 能表示成 $n$ 个不被 $p$ 整除的整数的平方和.

对 $\alpha$ 用数学归纳法.

当 $\alpha=1$ 时, $n^{\alpha}=\underbrace{1^{2}+1^{2}+\cdots+1^{2}}_{n \text { 个 }}$, 结论成立.

当 $\alpha=2$ 时, $n^{\alpha}=n^{2}=(n-2)^{2}+(n-1) \cdot 2^{2}$, 注意到 $p$ 为奇素数及 $p \mid n$, 则 $p \nmid n-2$ 且 $p \nmid 2$, 结论成立.

假设结论对 $\alpha=k\left(k \in \mathbb{N}^{*}\right)$ 成立.

当 $\alpha=k+2$ 时, 由归纳假设, 存在 $a_{1}, \cdots, a_{n} \in \mathbb{Z}, p \nmid a_{1}, \cdots, a_{n}$, 使得

$$
n^{k}=a_{1}^{2}+\cdots+a_{n}^{2}
$$

下面我们选取 $b_{1}, \cdots, b_{n} \in \mathbb{Z}, p \nmid b_{1}, \cdots, b_{n}$, 使得

$$
\left(n a_{1}\right)^{2}+\left(n a_{2}\right)^{2}+\cdots+\left(n a_{n}\right)^{2}=\left(n a_{1}-b_{1}\right)^{2}+\left(n a_{2}-b_{2}\right)^{2}+\cdots+\left(n a_{n}-b_{n}\right)^{2} .
$$

事实上,

$$
(*) \Leftrightarrow b_{1}^{2}+b_{2}^{2}++\cdots+b_{n}^{2}=2 n\left(a_{1} b_{1}+a_{2} b_{2}+\cdots+a_{n} b_{n}\right) .
$$

经验证,

$$
b_{1}=b_{2}=\cdots=b_{n}=2\left(a_{1}+a_{2}+\cdots+a_{n}\right)
$$

$$
-b_{1}=b_{2}=\cdots=b_{n}=2\left(-a_{1}+a_{2}+\cdots+a_{n}\right)
$$

皆满足上式.

而 $p \mid 2\left(a_{1}+a_{2}+\cdots+a_{n}\right)$ 与 $p \mid 2\left(-a_{1}+a_{2}+\cdots+a_{n}\right)$ 不能同时成立. 否则,两式相加可得 $p \mid 4 a_{1}$, 由于 $p$ 是奇素数则 $p \mid a_{1}$, 这与归纳假设矛盾!

这样上面两组解中一定有一组满足条件, 取出满足条件的解 $b_{1}, \cdots, b_{n}$.

那么由 $(*)$ 及归纳假设立得

$$
\left(n a_{1}-b_{1}\right)^{2}+\left(n a_{2}-b_{2}\right)^{2}+\cdots+\left(n a_{n}-b_{n}\right)^{2}=n^{k+2} .
$$

故当 $\alpha=k+2$ 时, 结论成立.

由此, 可知 (1) 对所有正整数 $\alpha$ 均成立.

特别地, 在 (1) 式中取 $\alpha=n$ 可知原题结论成立.

证法二 (东北育才中学谢子辰) 设 $p$ 是 $n$ 的奇素因子.

我们证明更强的命题: 对任意整数 $k \geq 2, n^{k}$ 有如下表示:

$$
n^{k}=a^{2}+(n-1) b^{2},
$$

其中 $p \nmid a, p \nmid b$.

对 $k$ 归纳.

当 $k=2$ 时, $n^{2}=(n-2)^{2}+(n-1) 2^{2}$. 由 $n$ 不是 2 的幂, $p \nmid n-2, p \nmid 2$, 此时 $(*)$ 成立.

假设结论对 $k$ 成立. 即有 $n^{k}=a^{2}+(n-1) b^{2}$, 且 $p \nmid a, p \nmid b$. 于是

$$
\begin{aligned}
n^{k+1} & =n\left[a^{2}+(n-1) b^{2}\right] \\
& =[(n-1) b+a]^{2}+(n-1)(b-a)^{2} \\
& =[(n-1) b-a]^{2}+(n-1)(b+a)^{2} .
\end{aligned}
$$

因为 $p \nmid a, p \nmid b$, 结合 $p \mid n$ 知, $p$ 不能同时整除 $(n-1) b-a$ 与 $(n-1) b+a$.

若 $p \nmid(n-1) b-a$, 则 $n^{k+1}=n\left[a^{2}+(n-1) b^{2}\right]=[(n-1) b-a]^{2}+(n-1)(b+a)^{2}$,满足要求.

若 $p \nmid(n-1) b+a$, 则 $n^{k+1}=n\left[a^{2}+(n-1) b^{2}\right]=[(n-1) b+a]^{2}+(n-1)(b-a)^{2}$,满足要求.

这说明 $k+1$ 时, $(*)$ 仍然成立. 故 $(*)$ 得证.

在 $(*)$ 中取 $k=n$ 便知原命题成立.
评注 这是一道十分困难的数论题, 得分率仅为 $2 \%$. 两种方法都是用归纳法证明加强命题, 法一是在归纳过渡中进行调整使得每一项均不被 $n$ 整除, 法二主要利用了形如 $x^{2}+(n-1) y^{2}$ 的数具有的乘积不变性来寻找合适的项. 我们在选题时低估了此题的难度。

题 4 设整数 $n \geq 2$. 不全为零的实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{i=1}^{n} x_{i}=0$, 且对任意正实数 $t$, 至多有 $\frac{1}{t}$ 对 $(i, j)$, 使得 $\left|x_{i}-x_{j}\right| \geq t$. 证明:

$$
\sum_{i=1}^{n} x_{i}^{2}<\frac{1}{n}\left(\max _{1 \leq i \leq n} x_{i}-\min _{1 \leq i \leq n} x_{i}\right) .
$$

证明 由拉格朗日恒等式,

$$
n \sum_{i=1}^{n} x_{i}^{2}=\left(\sum_{i=1}^{n} x_{i}\right)^{2}+\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}
$$

所以只需证明

$$
\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}<\max _{1 \leq i \leq n} x_{i}-\min _{1 \leq i \leq n} x_{i}
$$

设集合

$$
\left\{\left|x_{i}-x_{j}\right| \mid 1 \leq i<j \leq n\right\}=\left\{y_{1}, y_{2}, \cdots, y_{m}\right\} \text {, }
$$

其中 $y_{1}<y_{2}<\cdots<y_{m}$. 再对 $1 \leq k \leq m$, 设有 $a_{k}$ 对 $(i, j)$, 使得 $\left|x_{i}-x_{j}\right|=y_{k}$.

对 $1 \leq k \leq m$, 在条件中取 $t=y_{k}$ 得, 至多有 $\frac{1}{y_{k}}$ 对 $(i, j)$, 使得 $\left|x_{i}-x_{j}\right| \geq t$,所以

$$
a_{k}+a_{k+1}+\cdots+a_{m} \leq \frac{1}{y_{k}} .
$$

记 $S_{k}=a_{k}+a_{k+1}+\cdots+a_{m}$, 则 $S_{k} \leq \frac{1}{y_{k}}$.

由阿贝尔变换,

$$
\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}=\frac{1}{2} \sum_{k=1}^{m} a_{k} y_{k}^{2}=\frac{1}{2} \sum_{k=1}^{m} S_{k}\left(y_{k}^{2}-y_{k-1}^{2}\right) \leq \frac{1}{2} \sum_{k=1}^{m} \frac{y_{k}^{2}-y_{k-1}^{2}}{y_{k}}
$$

其中 $y_{0}=0$. 因为 $y_{k-1}<y_{k}$, 所以

$$
\frac{y_{k}^{2}-y_{k-1}^{2}}{y_{k}}=\frac{\left(y_{k}+y_{k-1}\right)\left(y_{k}-y_{k-1}\right)}{y_{k}}<2\left(y_{k}-y_{k-1}\right) .
$$

故

$$
\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}<\sum_{k=1}^{m}\left(y_{k}-y_{k-1}\right)=y_{m}=\max _{1 \leq i \leq n} x_{i}-\min _{1 \leq i \leq n} x_{i}
$$

评注 这是一道颇有难度的代数题, 得分率约 $8 \%$. 本题所用的方法不大常
规, 首先用拉格朗日恒等式做初步的化简, 然后考虑所有两两的差构成的集合,最后利用题设条件使用阿贝尔变换进行放缩就可以证得结论.

值得注意的是, 题目中的 $(i, j)$ 应理解为有序对. 若理解为无序对, 则结论未必成立. 例如, $n=3$ 时, $a_{1}=\frac{7}{18}, a_{2}=\frac{1}{18}, a_{3}=-\frac{4}{9}$ 便是一个反例.

本题改编自 Andreescu T. 与 Dospinescu G. 所著的书 《Problems from the book》第十九章习题 19 , 原题是

设 $x_{1}, x_{2}, \cdots, x_{n}, y_{1}, y_{2}, \cdots, y_{n}$ 是正实数, 满足对任意正实数 $t$, 至多有 $\frac{1}{t}$ 对 $(i, j)$, 使得 $x_{i}+y_{j} \geq t$. 证明:

$$
\left(\sum_{i=1}^{n} x_{i}\right)\left(\sum_{i=1}^{n} y_{i}\right) \leq \max _{1 \leq i, j \leq n}\left(x_{i}+y_{j}\right)
$$

本题采用了不同于原解答 (积分) 的方法, 且得到了更强的结论.

题 5. 已知四边形 $A B C D$ 有内切圆, 圆心为 $I$, 直线 $A C, B D$ 交于 $K$, 直线 $A B, D C$ 交于 $E$, 直线 $A D, B C$ 交于 $F$, 设 $\triangle A B K$ 与 $\triangle C D K$ 的外接圆交于另一点 $Q, \triangle A D K$ 与 $\triangle B C K$ 的外接圆交于另一点 $P$. 若 $E, P, Q, F$ 四点共圆, 证明: 点 $I$ 也在此圆上.

证明 依题意得 $P$ 为完全四边形 $F D A K B C$ 的密克点, $Q$ 为完全四边形 $A B E C D K$ 的密克点.

![](https://cdn.mathpix.com/cropped/2024_02_26_861c1c79cdef1d87bc1cg-07.jpg?height=669&width=596&top_left_y=1553&top_left_x=730)

第一种情况: 若 $B, E, F, D$ 四点共圆, 则 $\angle A B C=\angle A D C$, 于是 $E, B, P, Q$, $D, F$ 六点共圆, 所以

$$
\begin{aligned}
\angle B I D & =\angle B A D+\angle A B I+\angle A D I \\
& =\angle B A D+\frac{1}{2} \angle A B C+\frac{1}{2} \angle A D C
\end{aligned}
$$

$$
\begin{aligned}
& =\angle B A D+\angle A B C \\
& =180^{\circ}-\angle A F B \\
& =\angle B P D
\end{aligned}
$$

故 $B, P, I, D$ 四点共圆, 即 $E, B, P, I, Q, D, F$ 七点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_861c1c79cdef1d87bc1cg-08.jpg?height=665&width=665&top_left_y=587&top_left_x=701)

第二种情况: 若 $B, E, F, D$ 四点不共圆.

对圆 $P Q F E$, 圆 $B E D Q$, 圆 $B P D F$ 用蒙日定理知, 直线 $B D, P F, E Q$ 三线共点. 对圆 $P Q F E$, 圆 $A E C Q$, 圆 $A P C F$ 用蒙日定理知, 直线 $A C, P F, E Q$ 三线共点.于是直线 $Q E, P F$ 都过点 $K$.

又 $B, P, D, F$ 四点共圆, 所以 $B K \cdot K D=K P \cdot K F=K C \cdot K A$. 于是可得 $A, B, C, D$ 四点共圆, 从而四边形 $A B C D$ 是双心四边形. 于是

$$
\begin{aligned}
\angle E I F & =180^{\circ}-\angle I E F-\angle I F E \\
& =180^{\circ}-\angle I E C-\angle I F C-\angle B C E \\
& =180^{\circ}-\frac{1}{2}(\angle B E C+\angle D F C+2 \angle B C E) \\
& =180^{\circ}-\frac{1}{2}(\angle A B C+\angle A D C)=90^{\circ} .
\end{aligned}
$$

在完全四边形 $A D F C B K$ 中, $P E, P C, P F, P D$ 为调和线束. 结合

$$
\angle C P K=\angle C B K=\angle D A K=\angle D P K
$$

可知 $P K \perp P E$, 故 $\angle E P F=\angle E I F=90^{\circ}$, 所以 $E, P, I, F$ 四点共圆, 即 $E, P, I, Q, F$ 五点共圆.

评注 本题是有一定难度的几何题. 得分率为 $14 \%$. 解答中的第一种情况是特殊情形, 第二种情况是一般情形. 本题综合运用了蒙日定理、双心四边形、完
全四边形和调和点列的性质, 考察了学生几何方面的综合能力. 有趣的是, 两种情况下都有 (1) $I K \perp E F ;$ (2) $E P, F Q, K I$ 三线共点.

题 6. 设 $n$ 是给定的正整数, 一个集族 $\Gamma$ 满足:

(1) $\left|\bigcup_{A \in \Gamma} A\right|=n$;

(2) 若 $A, B \in \Gamma$, 则存在 $C \in \Gamma$ 使得 $A \triangle B \subset C$, 其中 $A \triangle B=(A \backslash B) \bigcup(B \backslash A)$.证明: $\max _{A \in \Gamma}|A|>\frac{n}{2}$.

证法一 (长郡中学胡再午) 对 $n$ 用归纳法.

$n=1$ 时, 命题显然成立.

假设命题对小于等于 $n-1$ 时成立, 下面考虑 $n$ 时的情形.

取 $\Gamma$ 中元素个数最多的集合, 设为 $A_{1}$, 且 $\left|A_{1}\right|=M$. 下证:

$$
\left|B \backslash A_{1}\right| \leq \frac{1}{2} M, \forall B \in \Gamma
$$

事实上, 由条件知, 存在集合 $C$, 使得 $A_{1} \triangle B \subset C$, 结合 $A_{1}$ 的最大性知,

$$
\left|A_{1} \triangle B\right| \leq|C| \leq\left|A_{1}\right|,
$$

即有 $\left|B \backslash A_{1}\right| \leq\left|A_{1} \cap B\right|$, 注意到 $\left|B \backslash A_{1}\right|+\left|A_{1} \cap B\right|=|B|$, 从而有

$$
2\left|B \backslash A_{1}\right|=|B|-\left|A_{1} \cap B\right|+\left|B \backslash A_{1}\right| \leq|B| \leq M
$$

(*) 得证.

记 $\Gamma_{1}=\left\{A \backslash A_{1} \mid A \in \Gamma\right\}$, 则

$$
\left|\bigcup_{A_{1} \in \Gamma_{1}} A\right|=\left|\bigcup_{A \in \Gamma} A\right|-\left|A_{1}\right|=n-M
$$

对任意 $D, E \in \Gamma_{1}$, 有 $D \cup A_{1} \in \Gamma, E \cup A_{1} \in \Gamma$, 由条件知, 存在 $C \in \Gamma$, 使 $\left(D \cup A_{1}\right) \triangle\left(E \cup A_{1}\right) \subset C$, 即有

$$
D \triangle E \subset\left(C \backslash A_{1}\right) .
$$

又 $C \backslash A_{1} \in \Gamma_{1}$, 这说明 $\Gamma_{1}$ 仍满足题设条件 (2).

对 $\Gamma_{1}$ 用归纳假设, 结合 (1) 知

$$
\max _{A \in \Gamma_{1}}|A|>\frac{\left|\bigcup_{A_{1} \in \Gamma_{1}} A\right|}{2}=\frac{n-M}{2}
$$

由 $(*)$ 知, $\frac{M}{2} \geq \max _{A \in \Gamma_{1}}|A|$, 从而有 $M>\frac{n}{2}$, 这说明 $n$ 时命题仍成立.

证法二 (乐清市知临中学谢柏庭) 由于含于一个 $n$ 元集的子集至多 $2^{n}$ 个,
故 $\Gamma$ 为有限集.

因此, 可记 $M=\max _{A \in \Gamma}|A|$. 并可按如下方式确定集合列 $A_{1}, A_{2}, \cdots, A_{t}(t \in$ $\left.N^{*}\right), A_{1}$ 为 $\Gamma$ 中元素个数最多的集合; 当 $A_{1}, \cdots, A_{i-1}$ 已给定 $(i \geq 2)$ 时, 若 $A_{1} \cup \cdots \cup A_{i-1} \neq \bigcup_{A \in \Gamma} A$, 取 $A_{i}$ 为 $F$ 中去掉 $A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}$ 中元素后不为空集且剩余元素个数最多的集合. 否则, 即当 $A_{1} \cup \cdots \cup A_{i-1}=\bigcup_{A \in \Gamma} A$ 时, 则停止操作 (由 $\Gamma$ 为有限集知若干步后操作必停止, $t$ 必存在).

下面我们证明:

$$
\left|A_{i} \backslash\left(A_{1} \cup \cdots \cup A_{i-1}\right)\right| \leq \frac{1}{2^{i-1}}\left|A_{i}\right|, 1 \leq i \leq t
$$

$i=1$ 时即 $\left|A_{1}\right| \leq\left|A_{1}\right|$.

记 $B_{j}=\left(A_{i} \cap A_{j}\right) \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right), 1 \leq j \leq i\left(j=1\right.$ 时, 即 $\left.A_{i} \cap A_{1}\right)$, 则

$$
A_{i}=B_{1} \cup B_{2} \cup \cdots \cup B_{i},
$$

且 $B_{1}, \cdots, B_{i}$ 两两不相交.

所证结论即

$$
\left|B_{i}\right| \leq \frac{1}{2^{i-1}}\left|A_{i}\right| .
$$

由 $\left|A_{j} \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right)\right|$ 最大性知: 任给 $C \in \Gamma$,

$$
\left|C \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right)\right| \leq\left|A_{j} \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right)\right|, \forall 1 \leq j \leq i-1 .
$$

特别地, 由条件知: 存在 $C \in \Gamma$, 使得 $A_{j} \triangle A_{i} \subseteq C$. 故有

$$
\left|\left(A_{j} \triangle A_{i}\right) \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right)\right| \leq\left|A_{j} \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right)\right|
$$

而记 $A_{j} \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right)=C_{j}(1 \leq j \leq i-1)$ 有

$$
\begin{aligned}
& \left(A_{j} \triangle A_{i}\right) \backslash\left(A_{1} \cup \cdots \cup A_{j-1}\right) \\
= & \left(C_{j} \backslash A_{i}\right) \cup\left(A_{i} \backslash\left(A_{1} \cup \cdots \cup A_{j}\right)\right) \\
= & \left(C_{j} \backslash A_{i}\right) \cup\left(B_{j+1} \cup B_{j+2} \cdots \cup B_{i}\right) \\
= & \left(C_{j} \backslash\left(C_{j} \cap A_{i}\right)\right) \cup\left(B_{j+1} \cup B_{j+2} \cdots \cup B_{i}\right) \\
= & \left(C_{j} \backslash B_{j}\right) \cup B_{j+1} \cup B_{j+2} \cdots \cup B_{i},
\end{aligned}
$$

结合 $C_{j} \cap\left(B_{j+1} \cup B_{j+2} \cdots \cup B_{i}\right)=\emptyset$ 知

$$
\left|C_{j}\right|-\left|B_{j}\right|+\left|B_{j+1}\right|+\cdots+\left|B_{i}\right| \leq\left|C_{j}\right| .
$$

故

$$
\left|B_{j}\right| \geq\left|B_{j+1}\right|+\cdots+\left|B_{i}\right|, \forall 1 \leq j \leq i-1
$$

有

$$
\left|B_{j}\right| \geq 2^{i-1-j} \cdot\left|B_{i}\right|
$$

又 $A_{i}=B_{1} \cup B_{2} \cup \cdots \cup B_{i}$, 故知

$$
\left(1+1+2+2^{2}+\cdots+2^{i-2}\right)\left|B_{i}\right| \leq\left|A_{i}\right| .
$$

故 $(*)$ 得证, 从而

$$
\left|B_{i}\right| \leq \frac{1}{2^{i-1}}\left|A_{i}\right| \leq \frac{1}{2^{i-1}} M
$$

注意到

$$
\bigcup_{A \in \Gamma} A=\bigcup_{i=1}^{t} A_{i}=\bigcup_{i=1}^{t}\left(A_{i} \backslash\left(A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right)\right)
$$

故

$$
\begin{aligned}
n=\left|\bigcup_{A \in \Gamma} A\right| & =\left|\bigcup_{i=1}^{t} A_{i} \backslash\left(A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right)\right| \\
& \leq\left(\sum_{i=1}^{t} \frac{1}{2^{i-1}}\right) M \\
& <2 M,
\end{aligned}
$$

即 $M>\frac{n}{2}$, 原命题获证!

评注 这是一道中等难度的组合题, 得分率为 $8 \%$. 本题的做法关键是考虑抹去最大集合的元素后,其余集合的剩下的元素不超过抹去的最大集合的元素个数的一半. 在此基础上, 证法 2 , 采用贪心算法, 不断取剩余元素个数最多的子集,得到新取的元素的个数与最大子集的元素个数之间的不等关系. 由于所有元素会在有限步取完, 这样将全集进行分拆, 利用不等关系便得到了结果; 证法 1 则采用归纳法, 避免了繁琐的集合运算, 更清楚简洁。

值得指出的是, 在考试结束后, 付云皓和石泽晖等发现这道题和第三十期征解题的第二题第一问本质是一样的.

