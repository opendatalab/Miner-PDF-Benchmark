数学新星网 学生专栏

www.nsmath.cn/xszl

# 2020 年伊朗 TST (第二轮) 试题解答与评析 

梁敬勋<br>(杭州学军中学, 310012)<br>指导教师: 边红平

伊朗数学奥林匹克国家队选拔一般有三轮共 18 个题. 伊朗的试题总体质量很高, 有些题目难度极大, 总是给我们的竞赛选手留下深刻的印象.

本文是 2020 年伊朗国家队选拔赛 (第二轮) 试题的解答. 由于能力有限, 难免有不当疏漏之处, 敬请读者批评指正.

## I. 试 题

1. 称首一多项式 $p(x) \in \mathbb{Z}[x]$ 为“模 $n$ 无平方因子的”, 若不存在多项式 $Q(x), R(x) \in \mathbb{Z}[x]$, 且 $Q$ 非常数, 使得 $P(x)=Q(x)^{2} R(x)(\bmod n)$. 给定素数 $p$及整数 $m \geq 2$, 求模 $p$ 无平方因子的 $m$ 次首一多项式 $P(x)$ 的个数, 其中 $p$ 的系数取自 $\{0,1, \cdots, p-1\}$.
2. 甲乙两人轮流对一个 $2020 \times 2020$ 的棋盘上的方格进行染色, 甲先开始每次操作可以选择一个未被着色的方格, 将它染黑并得到等同于此时它所在的行与列之并中黑格数目的分数. 当所有格均染黑时游戏结束, 得分高的人获胜.问: 甲乙谁有必胜策略? 他至多可保证比另一方多得多少分?
3. 给定 $\triangle A B C$ 及外接圆 $\Gamma$, 点 $E, F$ 分别为 $\angle B, \angle C$ 平分线与对边的交点, $I$ 为内心, $K$ 为 $A I$ 与 $E F$ 的交点. 设 $T$ 为 $\Gamma$ 中弧 $B A C$ 上的中点. 设 $\Gamma$ 与 $A$ - 中线和 $\odot(A E F)$ 的另一交点分别为 $X, S, S^{\prime}$ 为 $S$ 关于 $A I$ 的对称点. $J$ 为 $\odot\left(A S^{\prime} K\right)$ 与 $A X$ 的另一交点. 证明: $T, J, I, X$ 四点共圆.
4. 等腰 $\triangle A B C(A B=A C)$ 内心为 $I$. 圆 $\omega$ 过 $C$ 且与 $A I$ 切于 $I, \omega$ 与 $A C, \odot(A B C)$ 的另一交点分别为 $Q, D, M, N$ 分别为 $A B, C Q$ 的中点. 证明: $A D, B C, M N$ 三线共点.

修订日期: 2020-12-01.

5. 对每个 $k \in \mathbb{N}_{+}, k>1$, 证明: 存在 $x \in \mathbb{R}$, 使得对任一正整数 $n<1398$,有

$$
\left\{x^{n}\right\}>\left\{x^{n-1}\right\} \Leftrightarrow k \mid n .
$$

6. $p$ 为奇素数, 求所有 $\frac{p-1}{2}$ 元组 $\left(x_{1}, \cdots, x_{\frac{p-1}{2}}\right) \in \mathbb{Z}_{p}^{\frac{p-1}{2}}$, 使

$$
\sum_{i=1}^{\frac{p-1}{2}} x_{i} \equiv \sum_{i=1}^{\frac{p-1}{2}} x_{i}^{2} \equiv \cdots \equiv \sum_{i=1}^{\frac{p-1}{2}} x_{i}^{\frac{p-1}{2}} \quad(\bmod p)
$$

## II . 解答与评注

1. 称首一多项式 $p(x) \in \mathbb{Z}[x]$ 为“模 $n$ 无平方因子的”, 若不存在多项式 $Q(x), R(x) \in \mathbb{Z}[x]$, 且 $Q$ 非常数, 使得 $P(x)=Q(x)^{2} R(x)(\bmod n)$. 给定素数 $p$及整数 $m \geq 2$, 求模 $p$ 无平方因子的 $m$ 次首一多项式 $P(x)$ 的个数, 其中 $p$ 的系数取自 $\{0,1, \cdots, p-1\}$.

解 所求为 $p^{m}-p^{m-1}$.

固定素数 $p$, 用 $f(m)$ 表示满足条件的 $m$ 次首-多项式的个数. 补充约定 $f(0)=1, f(1)=p$, 在域 $\mathbb{Z}_{p}$ 上考察多项式.

对 $m \geq 2$, 每个 $m$ 次首一多项式 $P(x)$ 可以在 $\mathbb{Z}_{p}$ 中唯一分解为 $\mathbb{Z}_{p}[x]$ 上的首一不可约多项式的积:

$$
P(x)=P_{1}(x)^{\alpha_{1}} P_{2}(x)^{\alpha_{2}} \cdots P_{k}(x)^{\alpha_{k}} \quad(\bmod p)
$$

$\alpha_{1}, \alpha_{2}, \cdots, \alpha_{k} \in \mathbb{N}^{+}, p_{1}, p_{2}, \cdots, p_{k}$ 为互异的首一不可约多项式.

令

$$
\begin{gathered}
Q(x)=p_{1}(x)^{\left[\frac{\alpha_{1}}{2}\right]} p_{2}(x)^{\left[\frac{\alpha_{2}}{2}\right]} \cdots p_{k}(x)^{\left[\frac{\alpha_{k}}{2}\right]} \\
R(x)=p_{1}(x)^{\alpha_{1}-2\left[\frac{\alpha_{1}}{2}\right]} p_{2}(x)^{\alpha_{2}-2\left[\frac{\alpha_{2}}{2}\right]} \cdots p_{k}(x)^{\alpha_{k}-2\left[\frac{\alpha_{k}}{2}\right]}
\end{gathered}
$$

则

$$
P(x)=Q(x)^{2} R(x) \quad(\bmod p) .
$$

我们称在 $\mathbb{Z}_{p}$ 上 $p$ 对应于 $(Q, R)$.

易见 $R$ 为模 $p$ 无平方因子的多项式, 且对任一这样的 $R$ 及模 $p$ 首一多项式 Q. 若

$$
\operatorname{deg} R+2 \operatorname{deg} Q=m
$$

则 $\mathbb{Z}_{p}$ 上有唯一的 $p$ 对应于 $(Q, R)$. ( $\mathbb{Z}_{p}[x]$ 的唯一分解定理起了巨大作用 $)$

由于 $P$ 共有 $p^{m}$ 个, 对每个 $0 \leq R \leq \frac{m}{2}$, 使 $\operatorname{deg} Q=R$ 的 $(Q, R)$ 有 $p^{R} f(m-$ $2 k)$ 个. 由上述双射, 有

$$
p^{m}=\sum_{k=0}^{\left[\frac{m}{2}\right]} p^{k} f(m-2 k), \forall m \geq 2
$$

下归纳证明: $f(m)=p^{m}-p^{m-1}, m \geq 2$.

由 $p^{2}=f(2)+p f(0)$ 知 $f(2)=p^{2}-p$. 假设命题对小于 $m$ 的正整数均成立,等于 $m$ 时由 (1),

$$
\begin{aligned}
f(m) & =p^{m}-\sum_{k=1}^{\left[\frac{m}{2}\right]} p^{k} f(m-2 k) \\
& =p^{m}-\sum_{k=1}^{\left[\frac{m}{2}\right]-1} p^{m-k-1}(p-1)-p^{\left[\frac{m}{2}\right]} f\left(m-2\left[\frac{m}{2}\right]\right) \\
& =p^{m}-(p-1) p^{m-\left\lceil\frac{m}{2}\right]} \frac{1-p^{\left\lceil\frac{m}{2}\right]-1}}{1-p}-p^{\left\lceil\frac{m}{2}\right\rceil} \\
& =p^{m}+p^{\left\lceil\frac{m}{2}\right\rceil}-p^{m-1}-p^{\left\lceil\frac{m}{2}\right\rceil}=p^{m}-p^{m-1} .
\end{aligned}
$$

由归纳原理, 结论成立. 故所求 $m$ 次首一多项式有 $p^{m}-p^{m-1}$ 个.

评注 通常考虑多项式的重因式是要通过研究 $\left(f(x), f^{\prime}(x)\right)$ 来处理的. 但本题中 $\left(f^{\prime}(x), f(x)\right)=1$ 这一刻画使 $f(x)$ 比较孤立不利于计数, 因此要回到定义上. 本题的关键是 $\mathbb{Z}_{p}[x]$ 上的唯一分解定理. 因为 $\mathbb{Z}_{p}[x]$ 为域, 故 $\mathbb{Z}_{p}[x]$ 可建立带余除法, 从而有与 $Q[x], R[x]$ 类似的唯一分解定理. 本题较为简单.

2. 甲乙两人轮流对一个 $2020 \times 2020$ 的棋盘上的方格进行染色, 甲先开始每次操作可以选择一个未被着色的方格, 将它染黑并得到等同于此时它所在的行与列之并中黑格数目的分数. 当所有格均染黑时游戏结束, 得分高的人获胜.问：甲乙谁有必胜策略? 他至多可保证比另一方多得多少分?

解 乙必胜, 且至多可保证比甲多 $\frac{1}{2} \times 2020 \times 2020=2040200$ 分.

一方面, 乙采取如下策略可保证比甲多 2040200 分：易见从左到右第 1010 列的右边界 $l$ 为整个方格表的对称轴, 每个方格在关于 $l$ 的对称下有唯一的像.

甲每次染色后, 乙就染黑甲染的格在关于 $l$ 的对称下的像, 则:

- 只要甲可染, 则乙的操作就是可进行的.
- 乙每轮得分恰比甲多 1. 这是因为甲该轮染的格计入乙的得分.

由于共进行 $\frac{1}{2} \times 2020 \times 2020$ 轮, 故乙至少可比甲多 2040200 分.
另一方面, 甲采取如下策略可使乙至多比甲多 2040200 分.

每次轮到甲染色时, 甲染黑格 $a$, 使得在剩下的可染色的格中, 染黑格 $a$ 得分最高. 这时, 无论乙如何染色, 其除格 $a$ 之外的得分不超过 $a$, 连同格 $a$ 至多比甲多一分. 从而每轮乙至多比甲多一分, 共多至多 2040200 分.

综上, 乙至多可保证比甲多 2040200 分.

评注 通常“中心对称”型配对可立刻说明乙不败, 从而乙必然是必胜一方.由于总共操作次数为偶数, 从而可看成若干个“甲，乙”的轮. 每一轮中甲先乙后，甲先手可以抢占有利位置, 乙后手可以借助甲新染的格, 在这样的分析下可以很容易构造两者的策略。

3. 给定 $\triangle A B C$ 及外接圆 $\Gamma$, 点 $E, F$ 分别为 $\angle B, \angle C$ 平分线与对边的交点, $I$ 为内心, $K$ 为 $A I$ 与 $E F$ 的交点. 设 $T$ 为 $\Gamma$ 中弧 $B A C$ 上的中点. 设 $\Gamma$ 与 $A-$ 中线和 $\odot(A E F)$ 的另一交点分别为 $X, S, S^{\prime}$ 为 $S$ 关于 $A I$ 的对称点. $J$ 为 $\odot\left(A S^{\prime} K\right)$ 与 $A X$ 的另一交点. 证明: $T, J, I, X$ 四点共圆.



证明 设 $B C$ 中点为 $M, T$ 在 $\Gamma$ 中对径点为 $N$. 设 $A T \cap B C=D$, 则由角平分线及外角平分线定理知

$$
\frac{A F}{F B} \cdot \frac{B D}{D C} \cdot \frac{C E}{E A}=\frac{A C}{C B} \frac{A B}{A C} \cdot \frac{B C}{A B}=1 .
$$

由梅氏定理之逆即有 $D, E, F$ 共线.

设 $A X$ 关于 $\angle B A C$ 的等角线 (共轭中线) 与 $E F$ 交于 $U$, 与 $\Gamma$ 交于另一点 $V$. 熟知四边形 $A B V C$ 为调和四边形.
断言 $1 A, S, U, K$ 共圆.

证明 设 $A I \cap B C=L$, 则

$$
\frac{B L}{L C}=\frac{B A}{A C}=\frac{B D}{D C} \Rightarrow N(B C ; L D)=-1=N(B C ; A V)
$$

又 $N, L, A$ 共线, 故 $N, V, D$ 共线. 而

$$
\begin{aligned}
& \varangle(S F, F D)=\varangle(S A, A E)=\varangle(S B, B C) \Rightarrow B, F, S, D \text { 共圆, } \\
& \varangle(S V, V A)=\varangle(S V, V D)=\varangle(S A, A K) \leftrightarrow S, U, V, D \text { 共圆, }
\end{aligned}
$$

从而

$$
\varangle(S U, U D)=\varangle(S V, V D)=\varangle(S A, A K) \Rightarrow S, A, K, U \text { 共圆. }
$$

由断言 $1, \odot(A K S)$ 与 $\odot\left(A K S^{\prime}\right)$ 关于 $A N$ 对称, $A U$ 与 $A X$ 关于 $A N$ 对称,故 $J$ 与 $U$ 关于 $A N$ 对称.

断言 $2 M, I, U$ 共线.

证明 设 $B I, C I$ 为 $\Gamma$ 另一交点为 $P, Q \cdot P Q$ 与过 $A$ 的 $\Gamma$ 切线交于 $R$. 对圆内接六边形 $A A C Q P B$, 用 Pascal 定理:

$$
A A \cap Q P=R, A C \cap P B=E, C Q \cap B A=F \text {, }
$$

故 $F, E, R$ 共线.

又熟知 $P A=P I, Q A=Q I$, 故 $P Q$ 为 $A I$ 中垂线. 故 $R A=R I$. 从而

$$
\begin{aligned}
\varangle(A I, I R)=\varangle(A R, A I) & =\varangle(A R, A C)+\varangle(A C, A I) \\
& =\varangle(A B, B C)+\varangle(A I, A B) \\
& =\varangle(A I, B C) .
\end{aligned}
$$

故 $I R / / B C$. 从而

$$
I(C B ; M R)=-1=A(B C ; V A)=(F E ; U R)=I(F E ; U R)
$$

又 $I, F, C$ 共线; $I, B, E$ 共线; $I, R, R$ 共线, 故 $I, M, U$ 共线. 现在, 由

$$
\begin{aligned}
N M \cdot N T=N B^{2}=N I^{2} & \Rightarrow \triangle N I M \sim \triangle N T I \\
& \Rightarrow \varangle(I N, I T)=\varangle(I M, M N) .
\end{aligned}
$$

故

$$
\begin{aligned}
\varangle(J I, I T) & =\varangle(J I, A I)+\varangle(A I, I T) \\
& =\varangle(A I, U I)+\varangle(I M, M N) \\
& =\varangle(A I, M N)=\varangle(A X, X T)
\end{aligned}
$$

$$
\Rightarrow J, I, X, T \text { 共圆. }
$$

故得证!

评注 本题点的复杂度都比较高, $J$ 处理起来非常困难. 点 $J$ 用 $\angle A J K=$ $\angle A S K$ 来定义显然是不好的, 需要消去 $J$ 或改造 $J$ 的定义. 在进行一系列的尝试性导角后, 如果作出了共轭中线, 则容易猜想 $A, K, U, S$ 共圆, 但本题的困难之处在于 $U, K$ 在图上很接近, (纸笔做图) 很难从图形中得到一些证据来确认 $A, S, U, K$ 共圆; 而这一点又不容易证, $U$ 的定义比较复杂, 使人对这一结论缺乏信心，做到这很容易卡住。幸好 $U, J, M$ 共线是好证的（与一个出现过的题： $Q E, P F, I M$ 共点做法完全相同), 从而只要 $U$ 在 $\odot(A S K)$ 上, 这确信了这一结论.

总的来说, 本题点的定义较复杂, 能做的推理不多, 依赖于对结论的观察 (个人感觉 $J$ 关于 $A I$ 对称点为 $U$ 这种清楚但不简单的点是很难事先预测的),因此需要较多时间探索. 另外, 本题也可用反演法 (以 $A$ 为中心的反演反射),(本质上区别不大), 这使 $A, S, U, K$ 共圆的对应结论更清楚一点.

4. 等腰 $\triangle A B C(A B=A C)$ 内心为 $I$. 圆 $\omega$ 过 $C$ 且与 $A I$ 切于 $I, \omega$ 与 $A C, \odot(A B C)$ 的另一交点分别为 $Q, D, M, N$ 分别为 $A B, C Q$ 的中点. 证明: $A D, B C, M N$ 三线共点.



证明 设 $\omega$ 圆心为 $N^{\prime}$, 则由 $\omega$ 与 $A I$ 相切知 $N^{\prime} I \perp A I$, 即 $N^{\prime} I / / B C$. 故

$$
\begin{gathered}
\varangle\left(N^{\prime} C, C I\right)=\varangle\left(C I, I N^{\prime}\right)=\varangle(C I, B C)=\varangle(A C, C I) \\
\Rightarrow A, N^{\prime}, C \text { 共线. }
\end{gathered}
$$

即 $C Q$ 过 $N^{\prime}$, 故 $N \equiv N^{\prime}$.

设 $\omega$ 与 $B C, A D$ 分别交于另一点 $U, V$, 则由直径 $C Q$ 有 $Q U \perp U C$. 从而

$$
\begin{aligned}
& \varangle\left(N^{\prime} C, C I\right)=\varangle(D C, C U)=\varangle(D A, A B) \Rightarrow A B / / U V . \\
& \varangle(V D, D U)=\varangle(V D, D C)+\varangle(D C, D U) \\
&=\varangle(A B, B C)+\varangle(Q C, Q U) \\
&=\varangle(B C, A C)+\varangle(Q C, Q U) \\
&=\varangle(B C, Q U)=\frac{\pi}{2}
\end{aligned}
$$

即 $U V$ 为 $\omega$ 直径, 故 $N$ 为 $U V$ 中点.

令 $A B / / U V, M, N$ 分别为 $A B, U V$ 中点, 故 $A V, M N, B U$ 共点, 即 $A D, M N$, $B C$ 共点. 故得证.

评注 本题没有特别复杂的点, 只要作图时发现 $N$ 为圆心, 各点的相关性质就很容易描述出来。但证明三线共点是通过“线段位似”来证的, 不太常规, 需要对对图形进行一些探索. 本题较为简单.

5. 对每个 $k \in \mathbb{N}_{+}, k>1$, 证明: 存在 $x \in \mathbb{R}$, 使得对任一正整数 $n<1398$,有

$$
\left\{x^{n}\right\}>\left\{x^{n-1}\right\} \Leftrightarrow k \mid n .
$$

证明 1 记 $m=1397$.

引理 任取 $a_{n}, b_{n}$ 使 $0<a_{n}<b_{n}<1(1 \leq n \leq m)$, 存在 $M_{1}, M_{2}, \cdots, M_{m} \in$ $\mathbb{N}_{+}$, 使得

$$
\begin{gathered}
\left(\left(M_{1}+a_{1}\right)^{\frac{1}{1}},\left(M_{1}+b_{1}\right)^{\frac{1}{1}}\right) \supseteq\left(\left(M_{2}+a_{2}\right)^{\frac{1}{2}},\left(M_{2}+b_{2}\right)^{\frac{1}{2}}\right) \supseteq \cdots \\
\supseteq\left(\left(M_{m}+a_{m}\right)^{\frac{1}{m}},\left(M_{m}+b_{m}\right)^{\frac{1}{m}}\right)
\end{gathered}
$$

证明 待定 $M_{1}$ (充分大), 递归地选取 $M_{k}$ : 设 $M_{1}, \cdots, M_{k}$ 已取好, 要取 $M_{k+1}$ 使

$$
\left(\left(M_{k}+a_{k}\right)^{\frac{1}{k}},\left(M_{k}+b_{k}\right)^{\frac{1}{k}}\right) \supseteq\left(\left(M_{k+1}+a_{k+1}\right)^{\frac{1}{k+1}},\left(M_{k+1}+b_{k+1}\right)^{\frac{1}{k+1}}\right) .
$$

即

$$
\left(M_{k}+a_{k}\right)^{\frac{k+1}{k}}-b_{k+1}>M_{k+1}>\left(M_{k}+a_{k}\right)^{\frac{k+1}{k}}-a_{k+1}
$$

欲满足的 $M_{k+1} \in N_{+}$存在, 仅需

$$
\left(M_{k}+a_{k}\right)^{\frac{k+1}{k}}-\left(M_{k}+a_{k}\right)^{\frac{k+1}{k}}>2
$$

由取法,

$$
\left(M_{k}+a_{k}\right)^{\frac{1}{k}}>M_{1}+a_{1} \Rightarrow M_{k}>M_{1}^{k}-1>\frac{1}{2} M_{1}^{k}
$$

从而

$$
\begin{aligned}
& \left(M_{k}+b_{k}\right)^{\frac{k+1}{k}}-\left(M_{k}+a_{k}\right)^{\frac{k+1}{k}} \\
= & \left(M_{k}+a_{k}\right)^{\frac{k+1}{k}}\left(1+\frac{b_{k}-a_{k}}{M_{k}+a_{k}}\right)^{\frac{k+1}{k}} \geq M_{k}^{\frac{k+1}{k}}\left(1+\frac{k+1}{k} \frac{b_{k}-a_{k}}{M_{k}+a_{k}}\right)
\end{aligned}
$$

(伯努利不等式)

$$
\leq \frac{k+1}{2 k}\left(b_{k}-a_{k}\right) M_{k}^{\frac{1}{k}}>\frac{k+1}{2 k}\left(b_{k}-a_{k}\right) \frac{1}{2} M_{1} .
$$

仅需

$$
M_{1}>8 k \frac{1}{(k+1)\left(b_{k}-a_{k}\right)} .
$$

上式右边仅与 $k, a_{k}, b_{k}$ 有关, 在 $M_{1}$ 充分大时, 上式成立, 故 (2) 符合.

由归纳原理, 结论成立.

我们可以证明更强结论:

任取 $\{1,2, \cdots, m\}$ 的排列 $\sigma, \exists x \in \mathbb{R}$, 使

$$
\left\{x^{\sigma(1)}\right\}<\left\{x^{\sigma(2)}\right\}<\cdots<\left\{x^{\sigma(m)}\right\} .
$$

事实上, 记 $\tau \circ \sigma=i d$, 则令 $\left\{x^{i}\right\} \in\left(\frac{\tau(i)-1}{m}, \frac{\tau(i)}{m}\right)$ 即可.

由断言, 存在 $M_{1}, \cdots, M_{m}$, 使得

$$
\begin{aligned}
& \left(\left(M_{i}+\frac{\tau(i)-1}{m}\right)^{\frac{1}{i}},\left(M_{i}+\frac{\tau(i)}{m}\right)^{\frac{1}{i}}\right) \\
& \quad \supseteq\left(\left(M_{i+1} \frac{\tau(i+1)-1}{m}\right)^{\frac{1}{i+1}},\left(M_{i+1} \frac{\tau(i+1)}{m}\right)^{\frac{1}{i+1}}\right)
\end{aligned}
$$

这里 $1 \leq i \leq m-1$.

取 $x \in\left(\left(M_{m}+\frac{\tau(m)-1}{m}\right)^{\frac{1}{m}},\left(M_{m}+\frac{\tau(m)}{m}\right)^{\frac{1}{m}}\right)$, 则由取法

$$
\begin{aligned}
& \left(M_{n}+\frac{\tau(n)-1}{m}\right)^{\frac{1}{n}}<x<\left(M_{n}+\frac{\tau(n)}{m}\right)^{\frac{1}{n}} \quad 1 \leq n \leq m \\
\Rightarrow & \{x\}^{\frac{1}{n}} \in\left(\frac{\tau(n)-1}{m}, \frac{\tau(n)}{m},\right),
\end{aligned}
$$

符合, 这个 $x$ 即为所求.

评注 本题的主要难点在于变量太少, 仅有一个 $x$. 虽然 $x \in \mathbb{R}$ 可连续变化,蕴含无限的可能, 但实际操作中如果先取好 $x$, 则很难控制 $\left\{x^{n}\right\}$.

一种常见的方法是用递推数列保证 $x^{n}+\alpha^{n}+\beta^{n} \in \mathbb{Z}, \forall n \in \mathbb{N}_{+}$, 其中
$\{\alpha\},\{\beta\}<1$. 再用 $\left\{x^{n}\right\}=\left\{-\alpha^{n}-\beta^{n}\right\}$ 来打开小数部分, 但这很难实现本题中分咐按递增的分布。

本题的处理方法是扩充参数：将 $\left\{x^{n}\right\}$ 的大小关系转化为具体的

$$
M_{k}+a_{K}<x_{k}<M_{k}+b_{k} .
$$

引入一个待取的参数 $M_{k}$, 降低单次选取的困难, 从而区间 $\left(\left(M_{k}+a_{k}\right)^{\frac{1}{k}},\left(M_{k}+b_{k}\right)^{\frac{1}{k}}\right)$长度不断变短实现目的。

证明 2 我们证明更强的结论: 对于 $1,2, \cdots, n$ 的任意排列 $\sigma(1), \sigma(2), \cdots, \sigma(n)$,我们都能找到一个 $x$ 使得 $\alpha_{1} \sim \alpha_{n}, \beta_{1} \sim \beta_{n}$.

(i). 取一个足够大的 $M$, 令

$$
\alpha_{1}=M+(\gamma(1)-1) \cdot \frac{1}{n}, \beta_{1}=M+\gamma(1) \cdot \frac{1}{n}\left(\alpha_{1}, \beta_{1} \in[m, m+1]\right),
$$

则有

$$
\beta_{1}-\alpha_{1}=\frac{1}{n}>2\left(\sqrt{m^{2}+1}-1\right) .
$$

(ii). 设 $\alpha_{k}, \beta_{k}$ 满足:

$$
\beta_{k}-\alpha_{k}>2\left(\sqrt[k+1]{m^{k+1}}-1\right), \alpha_{k-1} \leq \alpha_{k}<\beta_{k} \leq \beta_{k-1} .\left(\alpha_{0}=M, \beta_{0}=M+1\right)
$$

则必定存在一个 $m_{k}$, 满足 $\sqrt[k]{m_{k}}, \sqrt[k]{m^{k}+1}$ 均在区间 $\left(\alpha_{k}, \beta_{k}\right)$ 中. $\left(m_{k} \in \mathbb{N}_{+}\right)$(这是因为当 $m>M^{k}$ 时, $\sqrt[k]{m_{k}+1}-\sqrt[k]{m_{k}}<\sqrt[k]{M_{k}+1}-M<\frac{1}{2}\left(\beta_{k}-\alpha_{k}\right)$, 由区间的长度可知, 上面的结论成立).

我们令

$$
\alpha_{k+1}=\sqrt[k+1]{m_{k}+(\gamma(k+1)-1) \cdot \frac{1}{n}}, \beta_{k+1}=\sqrt[k+1]{M_{k}+\gamma(k+1) \cdot \frac{1}{n}},
$$

则

$$
\begin{aligned}
\beta_{k+1}-\alpha_{k+1} & >(M+1)-\sqrt[k+1]{(M+1)^{k+1}-\frac{1}{n}} \\
& =\frac{1}{n} \frac{1}{(M+1)^{k} \cdots\left[(M+1)^{k+1}-\frac{1}{n}\right]^{\frac{k}{k+1}}} .
\end{aligned}
$$

而

$$
2\left(\sqrt[k+2]{M^{k+2}+1}-M\right)=2 \cdot \frac{1}{M^{k+1} \cdots\left(M^{k+2}+1\right)^{\frac{k+1}{k+2}}}
$$

$M$ 充分大时下式 $<$ 上式, 故

$$
\beta_{k+1}-\alpha_{k+1}>2\left(\sqrt[k+2]{M^{k+2}+1}-M\right), \alpha_{k} \leq \alpha_{k+1}<\beta_{k+1} \leq \beta_{k}
$$

成立.

依次类推可得到 $\alpha_{1} \sim \alpha_{n}, \beta_{1} \sim \beta_{n}$, 则我们考虑在 $\left(\alpha_{t}, \beta_{t}\right)$ 中取一个数
$x,\left\{x^{t}\right\} \in\left((\gamma(t)-1) \cdot \frac{1}{n}, \gamma(t) \cdot \frac{1}{n}\right)$.

故我们在 $\left(\alpha_{n}, \beta_{n}\right)$ 中取 $x_{0}$. (同样地, $\left.x_{0} \in\left(\alpha_{i}, \beta_{i}\right), i=1,2, \cdots, n-1\right)$.

$$
\Rightarrow\left\{x_{0}^{i}\right\} \in\left((\gamma(t)-1) \cdot \frac{1}{n}, \gamma(t) \cdot \frac{1}{n}\right) \text { 成立, } \forall \in[1, n] \text {. }
$$

所以 $\left\{x^{\sigma(1)}\right\}<\left\{x^{\sigma(2)}\right\}<\cdots<\left\{x^{\sigma(n)}\right\}$ 成立.

故原命题随之成立.
6. $p$ 为奇素数, 求所有 $\frac{p-1}{2}$ 元组 $\left(x_{1}, \cdots, x_{\frac{p-1}{2}}\right) \in \mathbb{Z}_{p}^{\frac{p-1}{2}}$, 使

$$
\sum_{i=1}^{\frac{p-1}{2}} x_{i} \equiv \sum_{i=1}^{\frac{p-1}{2}} x_{i}^{2} \equiv \cdots \equiv \sum_{i=1}^{\frac{p-1}{2}} x_{i}^{\frac{p-1}{2}}(\bmod p)
$$

解法 $1 p>3$ 时, 所求为全体 $\left(x_{1}, \cdots, x_{\frac{p-1}{2}}\right) \in\{0,1\}^{\frac{p-1}{2}}(\bmod p) ; p=3$ 时所求为 0,1 或 2 .

一方面, 显然所给的 $x_{1}, \cdots, x_{\frac{p-1}{2}}$ 符合.

另一方面, 下设 $r=\frac{p-1}{2} ; x_{1}, \cdots, x_{n}$ 满足:

$$
\left\{\begin{array}{cc}
x_{1}+x_{2}+\cdots+x_{r} \equiv a & (\bmod p) \\
x_{1}^{2}+x_{2}^{2}+\cdots+x_{r}^{2} \equiv a & (\bmod p) \\
\vdots \\
x_{1}^{r}+x_{2}^{r}+\cdots+x_{r}^{r} \equiv a & (\bmod p),
\end{array}\right.
$$

下证 $\left(x_{1}, \cdots, x_{r}\right)$ 一定具有上述形式. 我们仅需考虑 $p>3$ 的情况. 事实上, 任取 $t \in\{2,3, \cdots, p-1\}$, 令 $\lambda \in\{1, \cdots, p-1\}$, 使得 $1+\lambda \equiv t^{2}(\bmod p)$, 则

$$
\begin{aligned}
\sum_{i=1}^{r}\left(\lambda x_{i}+1\right)^{r} & =\sum_{i=1}^{r} \sum_{k=0}^{r}\left(\begin{array}{l}
r \\
k
\end{array}\right) x_{i}^{k} \lambda^{k} \\
& =r+\sum_{k=1}^{r} \sum_{i=1}^{r}\left(\begin{array}{l}
r \\
k
\end{array}\right) x_{i}^{k} \lambda^{k} \\
& =r+\sum_{k=1}^{r} a\left(\begin{array}{l}
r \\
k
\end{array}\right) \lambda^{k} \\
& =r+a\left((\lambda+1)^{r}-1\right) \quad(\bmod p)
\end{aligned}
$$

而

$$
\left.1=\left(\frac{1+\lambda}{p}\right) \equiv(1+\lambda)^{r} \quad(\bmod p) \Rightarrow p \right\rvert\,(\lambda+1)^{r}-1
$$

这里 $\left(\frac{a}{p}\right)$ 为勒让德符号. 故

$$
\sum_{i=1}^{r}\left(\lambda x_{i}+1\right)^{r} \equiv r \quad(\bmod p)
$$

即

$$
\sum_{i=1}^{r}\left(\frac{\lambda x_{i}+1}{p}\right)^{r} \equiv r \quad(\bmod p)
$$

即

$$
\sum_{i=1}^{r}\left(\frac{x_{i} \cdot \lambda+1}{p}\right) \equiv r \quad(\bmod p)
$$

又

$$
-p+r<-r \leq \sum_{i=1}^{r}\left(\frac{x_{i} \lambda+1}{p}\right) \leq r
$$

故必须

$$
\left(\frac{x_{i} \lambda+1}{p}\right)=1 \quad(1 \leq i \leq r)
$$

即

$$
\left(\frac{x_{i}\left(t^{2}-1\right)+1}{p}\right)=1, \forall t \in\{2,3, \cdots, p-1\} \quad(1 \leq i \leq r)
$$

又由于

$$
\sum_{t=1}^{p-1} t^{k} \equiv\left\{\begin{array}{ll}
0, & p-1 \nmid k \\
-1, & p-1 \mid k
\end{array} \quad(\bmod p)\right.
$$

故

$$
\begin{aligned}
p-1+\left(\frac{1-x_{i}}{p}\right) & =\sum_{t=0}^{p-1}\left(\frac{x_{i}\left(t^{2}-1\right)+1}{p}\right) \\
& \equiv \sum_{t=1}^{p}\left(x_{i} t^{2}+\left(1-x_{i}\right)\right)^{r} \\
& \equiv \sum_{t=1}^{p} \sum_{l=0}^{r}\left(\begin{array}{l}
r \\
l
\end{array}\right)\left(x_{i} t^{2}\right)^{l}\left(1-x_{i}\right)^{r-l} \\
& =\sum_{t=1}^{p}\left(1-x_{i}\right)^{r}+\sum_{l=1}^{r-1}\left(\begin{array}{l}
r \\
l
\end{array}\right)\left(1-x_{i}\right)^{r-l} x_{i}^{l} \sum_{t=1}^{p} t^{2 l}+\sum_{t=1}^{p} x_{i}^{r} t^{p-1} \\
& \equiv-x_{i}^{r} \equiv-\left(\frac{x_{i}}{p}\right)^{(\bmod p) .}
\end{aligned}
$$

即

$$
-1+\left(\frac{1-x_{i}}{p}\right)+\left(\frac{x_{i}}{p}\right) \equiv 0 \quad(\bmod p), \quad(1 \leq i \leq r)
$$

又 $p>3$, 故必须

$$
-1+\left(\frac{1-x_{i}}{p}\right)+\left(\frac{x_{i}}{p}\right)=0, \quad(1 \leq i \leq r)
$$

这表明 $\left(\frac{1-x_{i}}{p}\right)=0$ 与 $\left(\frac{x_{i}}{p}\right)=0$ 至少有一个成立, 否则上式左边为奇数, 矛盾!
从而

$$
x_{i} \equiv 0 \text { 或 } 1 \quad(\bmod p),(1 \leq i \leq r)
$$

故得证! 从而所求数组即为开头所列的.

评注 本题很容易想到计算 $\sigma_{k}$, 由此导出 $x_{1}, \cdots, x_{\frac{p-1}{2}}$ 为 $\sum_{k=0}^{r}\left(\begin{array}{l}a \\ k\end{array}\right) x^{r-k}(-1)^{k}$的 $r$ 个根, 说明每个 $a$ 在轮换意义下仅一组 $\left(x_{1}, \cdots, x_{r}\right)$. 但用这种方法对 “有 $r$个根”体现较弱, 不容易对 $r<a<p$ 的情况进行排除.

另一角度是不等式: $x^{r} \equiv 0, \pm 1(\bmod p)$, 其对根的个数体现很强. 但可惜 (1) 中 $\sum_{i=1}^{r} x_{i}^{r} \equiv a(\bmod p)$ 夹不出等号, 并且一般情况其算出余 $\pm n$ 的概率很低,本题中 (2) 的出现不得不说是一个奇迹. 发现 (2) 基于考察平移变换 $y_{i}=x_{i}+\lambda$下方程 (1) 的变化, 但主要是巧合性居多, 本题也需要广大的尝试.

解法 $2 p=3$ 同解法一. 下面仅考虑 $p>3$ 的情形.

此时, $\left(x_{1}, x_{2}, \cdots, x_{\frac{p-1}{2}}\right) \in\{0,1\}^{\frac{p-1}{2}}$. 即每项非 0 即 1 .

一方面, 上述的 $2^{\frac{p-1}{2}}$ 个数组显然符合条件.

另一方面, 下证仅有这些数组符合条件.

设 $M \in\{0,1, \cdots, p-1\}$ 且

$$
M \equiv \sum_{i=1}^{\frac{p-1}{2}} x_{i}^{t} \quad(\bmod p), t=1,2, \cdots, \frac{p-1}{2}
$$

则对于 $\bmod p$ 的一个新余类 $a$ ，

$$
\begin{aligned}
& \sum_{i=1}^{\frac{p-1}{2}}\left(1-a x_{i}\right)^{\frac{p-1}{2}} \equiv \frac{p-1}{2}+M \cdot\left[(1-a)^{\frac{p-1}{2}}-1\right] \quad(\bmod p) . \\
& \text { 若 }\left(\frac{1-a}{p}\right)=1 \text {, 则 } \\
& \sum_{i=1}^{\frac{p-1}{2}}\left(1-a x_{i}\right)^{\frac{p-1}{2}} \equiv \frac{p-1}{2} \quad(\bmod p) \Rightarrow\left(\frac{1-a x_{i}}{p}\right)=1\left(i=1,2, \cdots, \frac{p-1}{2}\right) .
\end{aligned}
$$

也就是说, 如果 $1-a$ 是 $\bmod p$ 的平方剩余, $1-a x_{i}$ 也是. $\left(i=1,2, \cdots, \frac{p-1}{2}\right)$.

所以记 $1-a=a^{\prime}$, 则 $1-a x_{i}=1-\left(1-a^{\prime}\right) x_{i}=1-x_{i}+x_{i} a^{\prime}$. 所以

$$
\sum_{\left(\frac{a^{\prime}}{p}\right)=1} a^{\prime}=\sum_{\left(\frac{a^{\prime}}{p}\right)=1} 1-x_{i}+x_{i} a^{\prime}
$$

记左边 $=A$, 则

$$
A=\frac{p-1}{2} \cdot\left(1-x_{i}\right)+x_{i} \cdot A \Rightarrow\left(\frac{p-1}{2}-A\right) \cdot\left(1-x_{i}\right)=0 \quad(\bmod p \text { 意义 }) \text {. }
$$

又因为 $A \equiv 0(\bmod p)$, 故必有 $x_{i}=1$.

所以每个 $x_{i}$ 非 0 即 1 , 则原来的断言成立.

