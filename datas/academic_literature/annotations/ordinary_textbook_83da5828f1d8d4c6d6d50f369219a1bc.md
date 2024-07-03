# 2019 年上海新星秋季数学奥林匹克试题解析 

吴尉迟 1, 罗振华 1, 胡珏伟 2 , 冷岗松 ${ }^{2}$

(1. 华东师范大学, 200241; 2. 上海大学, 200444)

2019 年上海新星秋季数学奥林匹克于 2019 年 12 月 9 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答.

## I. 试 题

1. 设整数 $n \geq 2$. 求最大的实数 $\lambda=\lambda(n)$ 使得

$$
\sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)\left(\frac{1}{i}+\frac{1}{j}\right) \geq \lambda \sum_{i=1}^{n} \frac{a_{i}}{i}
$$

对任意满足 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$ 的正实数 $a_{1}, \cdots, a_{n}$ 成立.

(上海中学王广廷供题)

2. 如图, 两圆 $\Gamma_{1}, \Gamma_{2}$ 相交于点 $P, Q$. 过点 $Q$ 的一条直线分别交圆 $\Gamma_{1}, \Gamma_{2}$ 于点 $A, B$, 过点 $Q$ 的另一条直线分别交圆 $\Gamma_{1}, \Gamma_{2}$ 于点 $C, D . \angle A P C$ 的角平分线交 $A C$ 于点 $E, \angle B P D$ 的角平分线交 $B D$ 于点 $F . \triangle A Q C, \triangle B Q D$ 的内心分别为 $I_{1}, I_{2}$, 直线 $E I_{1}$ 交 $F I_{2}$ 于点 $R$. 证明: $P R$ 平分 $\angle A P D$.

![](https://cdn.mathpix.com/cropped/2024_02_26_fa1e4040fddbc213fb50g-01.jpg?height=456&width=780&top_left_y=1945&top_left_x=638)

(浙江省乐清市知临中学 羊明亮 供题)

修订日期: 2019-12-25.

3. 设整数 $k \geq 2$. 若正整数 $n$ 能被所有小于 $\sqrt[k]{n}$ 的正整数整除. 证明: $n$ 的不同素因子的个数不超过 $2 k-1$.

(中国人民大学附属中学 张端阳供题)

4. 设整数 $n \geq 2$. 求最小的常数 $c=c(n)$ 使得不等式

$$
\sum_{k=1}^{n}\left(a_{k}-G_{n}\right)^{2} \leq c \sum_{k=1}^{n}\left(a_{k}-A_{n}\right)^{2}
$$

对任意非负实数 $a_{1}, \cdots, a_{n}$ 均成立, 其中 $G_{n}=\sqrt[n]{a_{1} a_{2} \cdots a_{n}}, A_{n}=\frac{a_{1}+\cdots+a_{n}}{n}$.

(华东师范大学 罗振华 供题)

5. 已知 $\triangle A B C$ 的外接圆为 $\odot O$, 点 $D, E$ 分别在边 $A B, A C$ 上. 过点 $B, C$的圆切线段 $D E$ 于点 $P$, 圆 $O$ 上一点 $Q$ 满足 $A Q, A P$ 互为关于 $\angle B A C$ 的等角线. 过点 $D, E$ 且与圆 $O$ 内切于点 $T$ 的圆, 分别交线段 $A D, A E$ 于点 $X, Y$. 证明: $X Y, B C, Q T$ 交于一点.

![](https://cdn.mathpix.com/cropped/2024_02_26_fa1e4040fddbc213fb50g-02.jpg?height=611&width=651&top_left_y=1299&top_left_x=702)

(吉林大学附属中学 石泽晖 供题)

6. 给定简单图 $G$ 和正整数 $n$. 证明: 图中存在两个(可以相同)顶点 $A, B$, 使得以 $A$ 为起点, $B$ 为终点的长度为 $n$ 的路径条数为偶数.

(华东师范大学 吴尉迟 供题)

## II. 解 答

题 1 设整数 $n \geq 2$. 求最大的实数 $\lambda=\lambda(n)$ 使得

$$
\sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)\left(\frac{1}{i}+\frac{1}{j}\right) \geq \lambda \sum_{i=1}^{n} \frac{a_{i}}{i}
$$

对任意满足 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$ 的正实数 $a_{1}, \cdots, a_{n}$ 成立.

解 $\lambda(n)$ 的最大值为 $2(n-1)$.

一方面, 取 $a_{1}=\cdots=a_{n}=1$, 有

$$
\lambda(n) \sum_{i=1}^{n} \frac{1}{i} \leq \sum_{1 \leq i<j \leq n} 2\left(\frac{1}{i}+\frac{1}{j}\right)=2(n-1) \sum_{i=1}^{n} \frac{1}{i}
$$

从而 $\lambda(n) \leq 2(n-1)$.

另一方面, 下证 $\lambda(n)=2(n-1)$ 不等式成立.

$$
\begin{aligned}
& \sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)\left(\frac{1}{i}+\frac{1}{j}\right) \geq 2(n-1) \sum_{i=1}^{n} \frac{a_{i}}{i} \\
\Leftrightarrow & 2 \sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)\left(\frac{1}{i}+\frac{1}{j}\right)+\sum_{i=1}^{n}\left(a_{i}+a_{i}\right)\left(\frac{1}{i}+\frac{1}{i}\right) \geq 4 n \sum_{i=1}^{n} \frac{a_{i}}{i} \\
\Leftrightarrow & 2 \sum_{i=1}^{n} a_{i}\left(\frac{n}{i}+\sum_{i=1}^{n} \frac{1}{i}\right) \geq 4 n \sum_{i=1}^{n} \frac{a_{i}}{i} \\
\Leftrightarrow & \left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{i}\right) \geq n \sum_{i=1}^{n} \frac{a_{i}}{i} .
\end{aligned}
$$

注意到 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}, 1>\frac{1}{2}>\cdots>\frac{1}{n}$, 由切比雪夫不等式知上式成立.

评注 这是一道简单的代数题. 约 $85 \%$ 的学生做对此题. 注意到变量全相等时取等, 再作适当的代数变形结合切比雪夫不等式即可证得结论.

题 2 如图, 两圆 $\Gamma_{1}, \Gamma_{2}$ 相交于点 $P, Q$. 过点 $Q$ 的一条直线分别交圆 $\Gamma_{1}, \Gamma_{2}$于点 $A, B$, 过点 $Q$ 的另一条直线分别交圆 $\Gamma_{1}, \Gamma_{2}$ 于点 $C, D . \angle A P C$ 的角平分线交 $A C$ 于点 $E, \angle B P D$ 的角平分线交 $B D$ 于点 $F . \triangle A Q C, \triangle B Q D$ 的内心分别为 $I_{1}, I_{2}$, 直线 $E I_{1}$ 交 $F I_{2}$ 于点 $R$. 证明: $P R$ 平分 $\angle A P D$..

![](https://cdn.mathpix.com/cropped/2024_02_26_fa1e4040fddbc213fb50g-03.jpg?height=425&width=691&top_left_y=2203&top_left_x=680)
证明设 $\overparen{A C}, \widehat{B D}$ 的中点为 $U, V$. 由于 $P E$ 平分 $\angle A P C$, 故 $P, E, U$ 三点共线. 类似可知 $P, F, V$ 三点共线, 又注意到 $\angle A Q C$ 与 $\angle B Q D$ 是对顶角, 则 $U, I_{1}, Q, I_{2}, V$ 四点共线.

由于 $\angle P A B=\angle P C D, \angle P B A=\angle P D C$, 故 $\triangle P A B \sim \triangle P C D$, 那么 $\triangle P C A \sim \triangle P D B$, 则有

$$
\frac{E A}{E C}=\frac{P A}{P C}=\frac{P B}{P D}=\frac{F B}{F D}, \frac{P E}{P U}=\frac{P F}{P V}
$$

从而 $\triangle P E F \sim \triangle P A B \sim \triangle P C D, E F / / U V$.

对 $\triangle P E F$ 及点 $R$, 由第一角元 Ceva 定理, 知

$$
\frac{\sin \angle E P R}{\sin \angle R P F} \cdot \frac{\sin \angle P F R}{\sin \angle R F E} \cdot \frac{\sin \angle F E R}{\sin \angle R E P}=1 .
$$

由 $E F / / U V$ 知 $\angle R E F=\angle E I_{1} U$, 所以

$$
\frac{\sin \angle F E R}{\sin \angle R E P}=\frac{\sin \angle E I_{1} U}{\sin \angle I_{1} E U}=\frac{E U}{I_{1} U}=\frac{E U}{A U}=\frac{E C}{P C}=\frac{A C}{P C+P A} .
$$

同理,

$$
\frac{\sin \angle P F R}{\sin \angle R F E}=\frac{P D+P B}{B D} .
$$

结合 $\triangle P C A \sim \triangle P D B$ 知 $\frac{A C}{B D}=\frac{P A}{P B}=\frac{P C}{P D}=\frac{P A+P C}{P B+P D}$, 从而

$$
\frac{\sin \angle F E R}{\sin \angle R E P} \cdot \frac{\sin \angle P F R}{\sin \angle R F E}=1,
$$

代入 $(*)$, 故 $\sin \angle E P R=\sin \angle F P R$. 故 $\angle E P R=\angle F P R$.

评注 这是一道中等难度的几何题, 约 $62 \%$ 的学生做对此题. 利用鸡爪定理的几何结构, 与内心和外接圆有关的问题的延长角平分线与圆相交是自然的, 从而首先找 $\widehat{A C}, \widehat{B D}$ 的中点 $U, V$. 之后立即可以发现若干组相似三角形, 最后用角元 Ceva 定理计算这两个角的正弦比值就可以证得结论.

题 3 设整数 $k \geq 2$. 若正整数 $n$ 能被所有小于 $\sqrt[k]{n}$ 的正整数整除. 证明: $n$的不同素因子的个数不超过 $2 k-1$.

证明 设 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{l}^{\alpha_{l}}$, 其中 $p_{1}, p_{2}, \cdots, p_{l}$ 是不同的素数, $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{l}$是正整数.

若 $l=1$, 则 $l \leq 2 k-1$, 命题成立.

若 $l \geq 2$. 对 $1 \leq i \leq l$, 因为 $p_{i}^{\alpha_{i}+1}$ 不能整除 $n$, 所以由题意, $p_{i}^{\alpha_{i}+1} \geq \sqrt[k]{n}$. 由 $\alpha_{i}$ 是正整数, 知 $2 \alpha_{i} \geq \alpha_{i}+1$, 所以

$$
p_{i}^{2 \alpha_{i}} \geq \sqrt[k]{n}
$$

对 $i$ 从 1 到 $l$ 求积, 得到

$$
n^{2}=p_{1}^{2 \alpha_{1}} p_{2}^{2 \alpha_{2}} \cdots p_{l}^{2 \alpha_{l}} \geq(\sqrt[k]{n})^{l}=n^{\frac{l}{k}}
$$

并注意到 $p_{i}^{2 \alpha_{i}}(i=1, \cdots, l)$ 不能同时等于 $\sqrt[k]{n}$, 故

$$
n^{2}>n^{\frac{l}{k}}
$$

从而 $2>\frac{l}{k}$, 即 $l<2 k$, 故 $l \leq 2 k-1$, 命题得证.

评注 此题是有一定难度的数论题, 约 $30 \%$ 的学生做对此题. 此题的关键将 $n$ 质因数分解, 探究每个素因子的幂次与 $\sqrt[k]{n}$ 的大小关系, 再对指数放缩得到结论.

本题当 $k=2$ 时是经典的问题, 我们可以求出所有满足要求的 $n$. 对于一般的 $k$, 本题给出了 $n$ 的素因子个数的上界, 其处理手段与具体的 $k$ 时是不同的.

题 4 设整数 $n \geq 2$. 求最小的常数 $c=c(n)$ 使得不等式

$$
\sum_{k=1}^{n}\left(a_{k}-G_{n}\right)^{2} \leq c \sum_{k=1}^{n}\left(a_{k}-A_{n}\right)^{2}
$$

对任意非负实数 $a_{1}, \cdots, a_{n}$ 均成立, 其中 $G_{n}=\sqrt[n]{a_{1} a_{2} \cdots a_{n}}, A_{n}=\frac{a_{1}+\cdots+a_{n}}{n}$.

解 一方面, 令 $a_{1}=\cdots=a_{n-1}=1, a_{n}=0$. 则 $A_{n}=\frac{n-1}{n}, G_{n}=0$.

$$
\begin{aligned}
\sum_{k=1}^{n}\left(a_{k}-G_{n}\right)^{2} & =\sum_{k=1}^{n} a_{k}^{2}=n-1 \\
\sum_{k=1}^{n}\left(a_{k}-A_{n}\right)^{2} & =(n-1) \frac{1}{n^{2}}+\frac{(n-1)^{2}}{n^{2}}=\frac{n-1}{n}
\end{aligned}
$$

可得 $n-1 \leq c \frac{n-1}{n}$. 即 $c \geq n$.

另一方面, 当 $c=n$ 时, 我们证明不等式成立. 即证

$$
\sum_{k=1}^{n}\left(a_{k}-G_{n}\right)^{2} \leq n \sum_{k=1}^{n}\left(a_{k}-A_{n}\right)^{2}
$$

$$
\begin{aligned}
\text { (*) 右 } & =n \sum_{k=1}^{n}\left(a_{k}^{2}-2 a_{k} A_{n}+A_{n}^{2}\right)=n\left(\sum_{k=1}^{n} a_{k}^{2}-2 A_{n} \sum_{k=1}^{n} a_{k}+n A_{n}^{2}\right) \\
& =n\left(\sum_{k=1}^{n} a_{k}^{2}-n A_{n}^{2}\right)=n \sum_{k=1}^{n} a_{k}^{2}-\left(\sum_{k=1}^{n} a_{k}\right)^{2} \\
& =\sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2} .
\end{aligned}
$$

记 $f(t)=\sum_{k=1}^{n}\left(a_{k}-t\right)^{2} . f$ 是关于 $t$ 的二次函数, 开口向上.

不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 由 $a_{1} \leq G_{n} \leq a_{n}$, 则 $f\left(G_{n}\right) \leq \max \left\{f\left(a_{1}\right), f\left(a_{n}\right)\right\}$.
而

$$
f\left(a_{1}\right)=\sum_{k=2}^{n}\left(a_{k}-a_{1}\right)^{2}, f\left(a_{n}\right)=\sum_{k=1}^{n-1}\left(a_{k}-a_{n}\right)^{2}
$$

有

$$
f\left(a_{1}\right) \leq \sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2}, f\left(a_{n}\right) \leq \sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2}
$$

则

$$
\max \left\{f\left(a_{1}\right), f\left(a_{n}\right)\right\} \leq \sum_{1 \leq i<j \leq n}\left(a_{i}-a_{j}\right)^{2}
$$

综上可知, (*) 成立.

评注 这是一道有一定难度的代数题, 约 $27 \%$ 的学生做对此题. 此题来源于 Figalli 不等式, 探讨了 $n$ 个非负实数减去几何平均的平方和的上界估计. 取等条件是常见的两点分布, 上述解法把 $G_{n}$ 看作变量 $t$, 利用二次函数的性质得到了结论.

题 5. 已知 $\triangle A B C$ 的外接圆为 $\odot O$, 点 $D, E$ 分别在边 $A B, A C$ 上. 过点 $B, C$ 的圆切线段 $D E$ 于点 $P$, 圆 $O$ 上一点 $Q$ 满足 $A Q, A P$ 互为关于 $\angle B A C$ 的等角线. 过点 $D, E$ 且与圆 $O$ 内切于点 $T$ 的圆, 分别交线段 $A D, A E$ 于点 $X, Y$.证明: $X Y, B C, Q T$ 交于一点.

证明 1 我们分三步完成题目证明.

![](https://cdn.mathpix.com/cropped/2024_02_26_fa1e4040fddbc213fb50g-06.jpg?height=609&width=966&top_left_y=1683&top_left_x=545)

(1) 先证明: $C, E, P, T$ 四点共圆.

设过 $C E P$ 的圆与 $\odot O$ 交于点 $T_{1}$ (异于点 $C$ ), 则

$$
\angle B T_{1} P=\angle B T_{1} C-\angle P T_{1} C=180^{\circ}-\angle B A C-\angle A E P=\angle A D P,
$$

故 $T_{1}, B, D, P$ 四点共圆.

由 $\angle C T_{1} E=\angle C P E=\angle C B P$ 可知, 直线 $T_{1} E$ 与直线 $B P$ 的交点 $R$ 在 $\odot O$上. 同理, 直线 $T_{1} D$ 与直线 $C P$ 的交点 $S$ 也在 $\odot O$ 上. 过 $T_{1}$ 作 $\odot O$ 的切线 $T_{1} L$,则

$$
\begin{aligned}
\angle L T_{1} E & =\angle L T_{1} R=\angle L T_{1} C+\angle C T_{1} R \\
& =\angle T_{1} S C+\angle C P E \\
& =\angle T_{1} S C+\angle S P D=\angle T_{1} D E
\end{aligned}
$$

由此可得: $T_{1} L$ 亦为 $\triangle T_{1} D E$ 外接圆的切线. 从而有 $T_{1}=T$. 故 $C, E, P, T$ 四点共圆.

同理可知, $B, D, P, T$ 四点共圆.

(2) 分别延长 $T X, T Y$ 交 $\odot O$ 于 $M, N$, 下证: $M C, N B, X Y, A Q$ 共点.

设 $M C, N B$ 交于点 $P^{\prime}$, 对圆内接六边形 $B A C M T N$ 应用帕斯卡定理可知: $X, P^{\prime}, Y$ 三点共线. 另一方面

$$
\angle T R C=\angle T A C, \angle T Y E=\angle T D E=\angle T B P=\angle T B R,
$$

从而有

$$
\angle T Y A=180^{\circ}-\angle T Y E=180^{\circ}-\angle T B R=\angle T C R,
$$

因此 $\angle A T Y=\angle C T R$, 故 $A N=C R$. 同理, $A M=B S$. 由此可知:

$$
\angle B C P=\angle A C P^{\prime}, \angle A B P^{\prime}=\angle C B P .
$$

这说明: $P, P^{\prime}$ 互为关于 $\triangle A B C$ 的等角共轭点, 从而点 $P^{\prime}$ 在直线 $A Q$ 上. 也即: $M C, N B, X Y, A Q$ 共点于 $P^{\prime}$.

(3) 最后证明 $X Y, B C, Q T$ 交于一点.

设 $B C, Q T$ 交于点 $Z$. 对圆内接六边形 $T Q A B C M$, 应用帕斯卡定理可知: $X, P^{\prime}, Z$ 三点共线. 又 $P^{\prime}$ 在直线 $X Y$ 上, 所以 $Z$ 在直线 $X Y$ 上, 从而 $X Y, B C, Q T$ 交于点 $Z$.

证明 2 延长 $T D, T E$ 与 $\odot O$ 交于另一点 $S, R$. 设 $B R \cap C S=P^{\prime}$.

则对圆内接六边形 $A B R T S C$, 由帕斯卡定理知 $D, P^{\prime}, E$ 共线,注意到 $T$ 为 $\odot O$ 与 $\odot(T D E)$ 的外位似中心, 所以 $S R / / D E$. 于是,

$$
\angle C P^{\prime} E=\angle D P^{\prime} S=\angle C S R=\angle C B P \text {. }
$$

故 $\odot\left(B C P^{\prime}\right)$ 与 $D E$ 相切与 $P^{\prime}$. 而 $\odot(B C P)$ 与 $D E$ 相切与 $P$, 所以 $P \equiv P^{\prime}$. 于

![](https://cdn.mathpix.com/cropped/2024_02_26_fa1e4040fddbc213fb50g-08.jpg?height=622&width=1062&top_left_y=206&top_left_x=500)

是, $B, P, R ; C, P, S$ 三点共线.

设 $X Y \cap B C=Z_{1}, Q T \cap B C=Z_{2}$.

对 $\triangle A B C$ 与截线 $X Y Z_{1}$, 由梅氏定理,有

$$
\frac{A X}{X B} \cdot \frac{B Z_{1}}{Z_{1} C} \cdot \frac{C Y}{Y A}=1
$$

又

$$
\frac{B Z_{2}}{Z_{2} C}=\frac{S_{\triangle B Q T}}{S_{\triangle C Q T}}=\frac{B Q \cdot B T}{C Q \cdot C T}
$$

所以要证 $X Y, B C, Q T$ 共点, 只需证: $\frac{B Z_{1}}{Z_{1} C}=\frac{B Z_{2}}{Z_{2} C}$, 即

$$
\frac{A X}{B X} \cdot \frac{C Y}{A Y} \cdot \frac{B Q}{C Q} \cdot \frac{B T}{C T}=1
$$

设 $B T, C T$ 与 $\odot(D E T)$ 另一交点分别为 $B_{1}, C_{1}$.

因为 $B, B_{1} ; C, C_{1} ; T, T$ 为 $\odot O$ 与 $\odot(D E T)$ 的三组外位似对应点, 所以

$$
\frac{B B_{1}}{B T}=\frac{C C_{1}}{C T}
$$

又 $B B_{1} \cdot B T=B D \cdot B X, C C_{1} \cdot C T=C E \cdot C Y$. 所以

$$
\frac{B D \cdot B X}{B T^{2}}=\frac{C E \cdot C Y}{C T^{2}}
$$

即

$$
\frac{B T \cdot C Y}{C T \cdot B X}=\frac{C T \cdot B D}{B T \cdot C E}
$$

又

$$
\frac{A X}{A Y} \cdot \frac{B Q}{C Q}=\frac{A E}{A D} \cdot \frac{\sin \angle E A P}{\sin \angle D A P}=\frac{E P}{D P}
$$

于是, $(*) \Leftrightarrow \frac{C T}{T B} \cdot \frac{B D}{D P} \cdot \frac{P E}{E C}=1$.
事实上,

$$
\begin{aligned}
\frac{C T}{T B} \cdot \frac{B D}{D P} \cdot \frac{P E}{E C} & =\frac{\sin \angle C B T}{\sin \angle B C T} \cdot \frac{\sin \angle B P D}{\sin \angle P B D} \cdot \frac{\sin \angle P C E}{\sin \angle C P E} \\
& =\frac{\sin \angle P S D}{\sin \angle B S D} \cdot \frac{\sin \angle B P D}{\sin \angle P B D} \cdot \frac{\sin \angle D B S}{\sin \angle D P S} \\
& =\frac{\sin \angle D S P}{\sin \angle D P S} \cdot \frac{\sin \angle D P B}{\sin \angle D B P} \cdot \frac{\sin \angle D B S}{\sin \angle D S B} \\
& =1
\end{aligned}
$$

证毕.

证明 3 同证明 1, 作出 $R, S$. 可知 $B, D, P, T ; C, E, P, T$ 四点共圆. 于是, $\angle X B T=\angle E P T$. 又 $\angle B X T=\angle P E T$. 故 $\triangle B T X \sim \triangle P T E$. 同理, $\triangle C T Y \sim$ $\triangle P T D$. 故

$$
\frac{B T}{B X}=\frac{P T}{P E}, \frac{C T}{C Y}=\frac{P T}{P D}
$$

同证明 2, 只需证:

$$
\frac{A X}{A Y} \cdot \frac{C Y}{B X} \cdot \frac{B Q}{C Q} \cdot \frac{B T}{C T}=1
$$

事实上,

$$
\frac{A X}{A Y} \cdot \frac{B Q}{C Q}=\frac{A E}{A D} \cdot \frac{\sin \angle E A P}{\sin \angle D A P}=\frac{E P}{D P}, \frac{B T}{B X} \cdot \frac{C Y}{C T}=\frac{P D}{P E},
$$

故结论成立.

评注 这是一道困难的几何题, 约 $6 \%$ 的学生做对此题. 此题是伪内切圆性质的推广, 如果熟悉相关几何性质和证法对解决问题是有一定帮助的. $C, E, P, T$和 $B, D, P, T$ 均四点共圆是基本的几何事实, 法一主要通过帕斯卡定理证得结论, 法二和法三通过计算比例证得结论.

题 6. 给定简单图 $G$ 和正整数 $n$. 证明: 图中存在两个(可以相同)顶点 $A, B$,使得以 $A$ 为起点, $B$ 为终点的长度为 $n$ 的路径条数为偶数.

证明 1 设 $G$ 的顶点集为 $V$, 边集为 $E$. 对 $v \in V$, 用 $d(v)$ 表示点 $v$ 的度数.

对 $u, v \in V$ 及 $m \in \mathbb{N}^{+}$, 用 $F_{m}(u, v)$ 表示以 $u$ 为起点, $v$ 为终点的长为 $m$ 的路径数目. 显然 $F_{m}(u, v)=F_{m}(v, u)$.

反证法, 假设结论不成立, 则对任意的 $u, v \in V$,

$$
F_{n}(u, v) \equiv 1 \quad(\bmod 2)
$$

成立. 对任意 $u, v \in V$.
考虑 $F_{n+1}(u, v)$. 有

$$
F_{n+1}(u, v)=\sum_{\substack{\omega \in V \\ u \omega \in E}} F_{n}(\omega, v) \equiv \sum_{\substack{\omega \in V \\ u \omega \in E}} 1 \equiv d(u) \quad(\bmod 2)
$$

同理

$$
F_{n+1}(u, v) \equiv d(v) \quad(\bmod 2)
$$

故

$$
d(u) \equiv d(v) \quad(\bmod 2)
$$

则 $G$ 中各顶点度的奇偶性相同.

设 $|v|=t, t \in \mathbb{N}^{+}$.

(1) $t$ 是奇数, 由于 $\sum_{u \in V} d(u) \equiv 0(\bmod 2)$, 从而 $G$ 中各顶点度为偶数. 我们归纳证明

$$
\sum_{\omega \in V} F_{i}(u, \omega) \equiv 0 \quad(\bmod 2)
$$

对任意 $u \in V, i \in \mathbb{N}^{+}$成立.

$i=1$ 时,

$$
\sum_{\omega \in V} F_{i}(u, \omega)=d(u) \equiv 0 \quad(\bmod 2)
$$

结论成立.

假设 $i$ 时成立, $i+1$ 时, 由归纳假设知,

$$
\sum_{\omega \in V} F_{i+1}(u, \omega)=\sum_{\substack{v \in V \\ u v \in E}} F_{i}(v, \omega)=\sum_{\substack{v \in V \\ u v \in E}} 0 \equiv 0 \quad(\bmod 2) .
$$

结论得证. 特别地,

$$
\sum_{\omega \in V} F_{n}(u, \omega) \equiv 0 \quad(\bmod 2) .
$$

但由假设

$$
\sum_{\omega \in V} F_{n}(u, \omega) \equiv \sum_{\omega \in V} 1 \equiv t \equiv 1 \quad(\bmod 2)
$$

矛盾!

(2) $t$ 是偶数.

(i) $G$ 中顶点度全为奇数.

与 (1) 类似归纳易证: 对任意 $u \in V, i \in \mathbb{N}^{+}$, 有

$$
\sum_{\omega \in V} F_{i}(u, \omega) \equiv 1 \quad(\bmod 2)
$$

特别地,

$$
\sum_{\omega \in V} F_{n}(u, \omega) \equiv 1 \quad(\bmod 2)
$$

这与

$$
\sum_{\omega \in V} F_{n}(u, \omega) \equiv \sum_{\omega \in V} 1 \equiv t \equiv 0 \quad(\bmod 2)
$$

矛盾.

(ii) $G$ 中顶点度全为偶数. 归纳证明: $F_{i}(u, u) \equiv 0(\bmod 2)$ 对任意 $u \in$ $V, i \in \mathbb{N}^{+}$成立.

$i=1$ 时, $F_{1}(u, u)=0$, 成立.

$i=2$ 时, $F_{2}(u, u)=\sum_{\substack{\omega \in V \\ u \omega \in E}} 1=d(u) \equiv 0(\bmod 2)$.

假设 $i$ 时结论成立, $i+2$ 时, 设 $u$ 与 $u_{1}, \cdots, u_{s}$ 相邻, 其中 $s$ 为非负偶数.

$s=0$ 时, $F_{i+2}(u, u)=0 \equiv 0(\bmod 2)$.

$s>0$ 时,

$$
\begin{aligned}
F_{i+2}(u, u) & =\sum_{k=1}^{s} \sum_{j=1}^{s} F_{i}\left(u_{k}, u_{j}\right) \\
& =\sum_{k=1}^{s} F_{i}\left(u_{k}, u_{k}\right)+2 \sum_{1 \leq k<j \leq s} F_{i}\left(u_{k}, u_{j}\right) \\
& \equiv \sum_{k=1}^{s} F_{i}\left(u_{k}, u_{k}\right) \\
& \equiv \sum_{k=1}^{s} 0(\text { 归纳假设 }) \\
& \equiv 0 \quad(\bmod 2) .
\end{aligned}
$$

结论成立. 特别地, $F_{n}(u, u) \equiv 0(\bmod 2)$ 与假设矛盾.

综上所述, 假设不成立, 故原命题得证.

证明 2 (根据华中师范大学第一附属中学廖悦辛同学解答整理) 记图 $G$的顶点为 $v_{1}, v_{2}, \cdots, v_{m}$, 考虑图 $G$ 的邻接矩阵 $A \in M_{m}(\mathbb{Z})$ : 若 $v_{i}$ 与 $v_{j}$ 相邻,则 $A$ 的 $(i, j)$ 元和 $(j, i)$ 元为 1 , 否则为 0 , 特别地, $A$ 的对角线上均为 0 (因为 $G$不含环边). 易知 $A$ 是对称矩阵. 设 $A^{k}$ 中的 $(i, j)$ 元为 $a_{i j}(k)$. 关于邻接矩阵, 有如下重要性质。

引理 1 对正整数 $k, A^{k}$ 中的 $(i, j)$ 元 $a_{i j}(k)$ 就是 $G$ 中 $v_{i}$ 到 $v_{j}$ 的长度为 $k$的路径个数.

引理 1 的证明 对 $k$ 归纳证明. $k=1$ 时结论显然成立. 假设 $k$ 时结论成立,
考虑 $k+1$ 时. 对从 $v_{i}$ 到 $v_{j}$ 的长度为 $k+1$ 的路径按其 $k$ 步之后所在顶点 $v_{l}$ 分类计算, 可知从 $v_{i}$ 到 $v_{j}$ 的长度为 $k+1$ 的路径个数为

$$
\sum_{l=1}^{m} a_{i l}(k) a_{l j}(1)
$$

而这正是矩阵乘法 $A^{k} \cdot A$ 的 $(i, j)$ 元, 即 $a_{i j}(k+1)$.

引理 2 设 $X \in M_{m}(K), K$ 是任意一个域, 若 $X$ 是对称矩阵, 则对任意正整数 $k, X^{k}$ 也是对称矩阵; 若 $X$ 是斜对称矩阵, 则对任意奇数 $k>0, X^{k}$ 也是斜对称矩阵.

引理 2 的证明 若 $X$ 是对称矩阵, $X^{T}=X$, 则对任意正整数 $k$, 由转置的性质可知 $\left(X^{k}\right)^{T}=\left(X^{T}\right)^{k}=X^{k}$, 因此 $X^{k}$ 也是对称矩阵. 若 $X$ 是斜对称矩阵, $X^{T}=-X$, 则对奇数 $k>0$, 由转置性质可知

$$
\left(X^{k}\right)^{T}=\left(X^{T}\right)^{k}=(-X)^{k}=(-1)^{k} X^{k}=-X^{k}
$$

因此 $X^{k}$ 也是斜对称矩阵.

下面回到原问题, 我们需要证明 $A^{n}$ 中有一个元素 $a_{i j}(n)$ 是偶数.

首先考虑 $n$ 是奇数的情形. 将 $A$ 的对角线下方的 1 全部改为 -1 , 所得矩阵记为 $B$, 则 $B$ 是斜对称矩阵, 且 $A \equiv B(\bmod 2)$. 将 $A, B$ 均看作实数域上矩阵, 由引理 $2, B^{n}$ 也是斜对称的, 而实数域上斜对称矩阵对角线元素均为 0 , 再由 $A^{n} \equiv B^{n}(\bmod 2)$ 可知, $A^{n}$ 的对角线元素均为偶数.

下面考虑 $n$ 是偶数的情形, 现将 $A$ 看作模 2 域 $\mathbb{F}_{2}$ 上的矩阵, $A \in M_{m}\left(\mathbb{F}_{2}\right)$, $A$ 是对角线上元素均为 0 的对称阵. 设 $n=2^{a} \cdot k, k$ 是奇数, 记 $C=A^{k}$, 上面已经证明了 $C$ 也是对角线上元素均为 0 的对称阵.

反证法, 假设 $C^{2^{a}}$ 的所有元素均为 1 , 记为矩阵 $J$, 则由于 $C^{2^{a}+1}=J C$ 的对角线元素为 0 , 可知 $C$ 的每一列均有偶数个 1 , 再由 $C$ 是对称阵, $C^{2}$ 的 $(i, i)$ 元为 $C$ 的 $i$ 行与 $i$ 列的对应数乘积之和, 等于 0 , 故 $C^{2}$ 是对角元素均为 0 的对称阵.设 $D=C^{2}$, 则 $D^{2^{a-1}}=J$, 重复上面的过程又可证明 $D^{2}$ 是对角元素均为 0 的对称阵, 继续这一过程, 对 $t=1,2, \cdots, a$, 依次可证明 $C^{2}$ 对角元素均为 0 的对称阵, 这与 $C^{2^{a}}=J$ 矛盾.

因此反证法假设不成立, $A^{n}$ 中总有元素是偶数.

评注 这是一道非常困难的组合题, 分类情形较多, 有相当的复杂度考场中并无学生做出此题. 解法一利用反证假设得到每点的度数均相同, 再对顶点数和度数分类讨论, 利用归纳法得到结论. 解法二运用图的邻接矩阵 $A$ 与路径个数
之间的联系, 采用矩阵的方法来证明 $A^{n}$ 中必有一个元素是偶数. 在 $n$ 是奇数时, 可将 $A$ 在模 2 下看作一个斜对称矩阵. 在 $n$ 是偶数时, 结合反证法, 先转化为 $n$ 是 2 的方幂的情形, 再归纳地证明 $C^{2^{t}}$ 上对角元素均为 0 .

致谢 感谢㫿振华老师对第六题的解法二做了精心的修改.

