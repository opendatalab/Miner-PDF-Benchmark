# 2022 年 ELMO 试题解答与评析 

唐自远 李奕

(长沙市雅礼中学, 410007)

指导教师: 彭喜

2022 年 ELMO 于 6 月 11 日和 19 日举行. 本次赛题质量高, 整体难度与我国 CMO 基本相当, 其中 $1,4,5$ 题是简单题, 2,3 题是中等偏难的问题, 第 6 题则是困难的问题. 题目整体复杂, 要求选手具有清晰的思维和较强的计算能力,十分适合作为备战 CMO 的训练题. 直于水平, 本文如有不当之处, 还请各位读者批评指正.

## I. 试 题

1. 黑板上写有整数 $1,2, \cdots, n(n>1)$. 甲乙两人轮流每次在黑板上圈出一个未被圈出的数, 若某人圈出一个数后黑板上所有圈出的数的乘积被 $n$ 整除,此人输掉游戏. 问: 对哪些 $n$, 乙有必胜策略?
2. 求所有非常值的首一整系数多项式 $P$, 使得存在正整数 $a$ 和 $m$ 满足: 对所有正整数 $n \equiv a(\bmod m), P(n)$ 非零且

$$
2022 \cdot \frac{(n+1)^{n+1}-n^{n}}{P(n)}
$$

是一个整数.

3. 设 $\mathcal{P}$ 是面积为 1 的正 2022 边形. 求实数 $c$ 满足: 如果点 $A, B$ 是 $\mathcal{P}$ 边界上随机独立等分布选取的两个点, 那么 $A B \geq c$ 的概率是 $\frac{1}{2}$.
4. 设 $A B C D E$ 是凸五边形, $\triangle A B E, \triangle B E C$ 和 $\triangle E D B$ 都按对应顶点相似. 直线 $B E$ 和 $C D$ 交于点 $T$. 证明: 直线 $A T$ 和 $\triangle A C D$ 外接圆相切.
5. ELMO 社交平台上有 $n^{3}(n \geq 3)$ 个用户, 用户之间的好友是相互的. 大于等于 3 个相互为好友的用户的集合称为一个 ELMO 俱乐部. 已知任意 $n$ 个

修订日期: 2022-10-27.
用户中, 至少有三个用户构成的集合是一个 ELMO 俱乐部. 证明: 存在一个有五个成员的 ELMO 俱乐部.

6. 求所有函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$ 满足: 对所有整数 $m$ 和 $n$, 都有

$$
f(f(m)-n)+f(f(n)-m)=f(m+n) .
$$

## II. 解答与评注

题 1 黑板上写有整数 $1,2, \cdots, n(n>1)$. 甲乙两人轮流每次在黑板上圈出一个未被圈出的数, 若某人圈出一个数后黑板上所有圈出的数的乘积被 $n$ 整除, 此人输掉游戏。问: 对哪些 $n$, 乙有必胜策略?

解 所求 $n$ 为全体大于 1 的无平方因子的奇数.

(1) $n$ 有平方因子: 则存在素数 $p$ 使 $p^{2} \mid n$. 设 $n=p^{2} t, t \in \mathbb{N}^{*}$. 下面说明甲有必胜策略: 甲圈数 $p t$, 则下一个圈出 $p$ 的倍数的人输掉游戏, 而 1 到 $n$ 中不为 $p$ 的倍数的有 $p^{2} t-p t=p(p-1) t$ 个, 是偶数个. 由乙先圈, 故乙负.

(2) $n$ 为无平方因子的偶数: 设 $n=2 k, k \in \mathbb{N}^{*}$, 由 $n$ 无平方因子知 $2 \nmid k$.下面说明甲必胜: 甲圈数 $k$, 则接下来圈偶数者负. 而 1 到 $n$ 中有 $k$ 个奇数, 甲圈出后还剩 $k-1$ 个, 是偶数个, 故乙负.

(3) $n$ 为无平方因子的奇数: 设 $n=p_{1} p_{2} \cdots p_{l}$, 其中 $p_{i}(1 \leq i \leq l)$ 为互异的奇素数. 下面说明乙必胜: 设甲圈数 $a$, 若 $p_{i} \mid a$ 对 $1 \leq i \leq l$ 成立, 则 $n \mid a$, 甲负; 否则不妨设 $p_{1} \nmid a$. 若 $a=p_{2} \cdots p_{l}$, 则乙圈 $2 p_{2} \cdots p_{l}<n$; 否则乙圈 $p_{2} \cdots p_{l}$. 则甲、乙均未圈 $p_{1}$ 倍数, 且再圈 $p_{1}$ 倍数者负. 而未圈的数中仍有 $\left(p_{1} \cdots p_{l}-p_{2} \cdots p_{l}-2\right)$ 个数不为 $p_{1}$ 倍数, 是偶数个, 此时甲先取, 故乙胜.

评注 本题大致与全国高中联赛第二题难度相当, 属于较简单的双人操作问题. 稍加尝试后即可发现甲乙两人的最优策略均是取尽可能大的 $n$ 的因子, 让余下可取的数有限. 从而在情况 (1), (2) 下甲均可直接获胜, 而在 (3) 时乙只需根据甲的取数, 只保留一个素因子即可. 整体思路简单自然, 只用统计奇偶便能判定胜负.

题 2 求所有非常值的首一整系数多项式 $P$, 使得存在正整数 $a$ 和 $m$ 满足:对所有正整数 $n \equiv a(\bmod m), P(n)$ 非零且

$$
2022 \cdot \frac{(n+1)^{n+1}-n^{n}}{P(n)}
$$

是一个整数.

解 所求为 $P(x)=\left(x^{2}+x+1\right)^{\alpha}, \alpha=1,2$.

设 $n=k m+a, k \in \mathbb{N}^{*}$, 则 $P(n)=P(k m+a)$ 为关于 $k$ 的整系数多项式,由 Schur 引理, $P(k m+a)$ 的素因子集为无限集.

取充分大的素数 $p$ 使 $(p, 2022)=1$, 且存在正整数 $n \equiv a(\bmod m)$ 使得 $p \mid P(n)$, 则 $p \mid P(n+m p)$. 由条件知:

$$
p\left|(n+1)^{n+1}-n^{n}, p\right|(n+1)^{n+1+m p}-n^{n+m p} \Rightarrow p \mid n^{n}\left((n+1)^{m}-n^{m}\right) .
$$

又由 $p \mid(n+1)^{n+1}-n^{n}$ 知 $p \nmid n(n+1)$, 从而 $p \mid(n+1)^{m}-n^{m}$.

代入 $n=k m+a$, 有

$$
p\left|(n+1)^{k m} \cdot(n+1)^{a+1}-n^{k m} \cdot n^{a} \Rightarrow p\right|(n+1)^{a+1}-n^{a} .
$$

综合以上两式, 有

$$
n^{m(a+1)} \equiv(n+1)^{m(a+1)} \equiv n^{m a} \quad(\bmod p) \Rightarrow p \mid n^{m}-1
$$

设多项式 $f(x)=x^{m}-1, g(x)=(x+1)^{a+1}-x^{a}$, 记 $\operatorname{gcd}(f(x), g(x))=d(x)$.对于多项式 $d(x)$ 的根 $\omega$, 有 $|\omega|=1,|\omega+1|=1$, 从而 $\omega=\exp \left( \pm \frac{2}{3} \pi \mathbf{i}\right)$. 由实系数多项式的虚根成对定理, 结合 $f$ 首一, 可设 $d(x)=\left(x^{2}+x+1\right)^{\alpha}, \alpha \in \mathbb{N}$.

由 Bezout 定理, 存在 $N \in \mathbb{N}^{*}, r(x), s(x) \in \mathbb{Z}[x]$ 使

$$
f(x) r(x)+g(x) s(x)=N d(x) .
$$

结合以上知 $p \mid N \cdot d(n)$. 又 $p$ 充分大, 故 $d(x)$ 非常数, $\alpha \geq 1$. 取 $p>N$ 得 $p \mid n^{2}+n+1$.

若 $P(x)$ 有不同于 $x^{2}+x+1$ 的不可约因式 $S(x)$, 则 $\operatorname{gcd}\left(S(x), x^{2}+x+1\right)=$ 1. 由 Schur 引理, 有无穷多个素数 $p$ 是 $S(n)=S(k m+a)$ 的素因子. 取其中充分大的 $p$, 由 Bezout 定理, 存在 $M \in \mathbb{Z}, u(x), v(x) \in \mathbb{Z}[x]$ 使

$$
S(x) u(x)+\left(x^{2}+x+1\right) v(x)=M \text {. }
$$

其中 $M$ 是常数, 但 $p \mid M$, 与 $p$ 充分大矛盾.

故 $P(x)$ 的不可约因式只有 $x^{2}+x+1$, 即 $P(x)=\left(x^{2}+x+1\right)^{\beta}$. 此时 $\omega$ 是 $f(x), g(x)$ 的公共根, 只能 $a \equiv 1(\bmod 6)$. 而 $\varphi(9)=6$, 故 $9 \nmid(n+1)^{n+1}-n^{n}$. 但 $3 \mid n^{2}+n+1$, 结合 2022 恰含一个 3 因子, 原式分子含 3 幂次不大于 2 , 故 $\beta \leq 2$.

最后只需验证: 对 $n \equiv 1(\bmod 6)$, 恒有

$$
\left(n^{2}+n+1\right)^{2} \mid 2022 \cdot\left((n+1)^{n+1}-n^{n}\right) .
$$

设 $n^{2}+n+1=c$, 则 $3 \mid c$, 有

$$
\begin{aligned}
3 n^{n+1}\left((n+1)^{n+1}-n^{n}\right) & \equiv 3\left((c-1)^{n+1}-(1+(n-1) c)^{\frac{2 n+1}{3}}\right) \\
& \equiv 3(1-(n+1) c)-3\left(1+(n-1) \cdot \frac{2 n+1}{3} \cdot c\right) \\
& \equiv-c(3 n+3+(n-1)(2 n+1)) \\
& \equiv 2 c^{2} \equiv 0 \quad\left(\bmod c^{2}\right),
\end{aligned}
$$

故是成立的.

评注 本题为较难的冬令营第 2,5 题. 初始时关于 $P(n)$ 的限制不够多, 自然选择对单个素因子分析, 利用多项式差分性质简化条件. 在分析幂次得出较为优美且较强性质后, 转向多项式上, 考虑具有共同素因子的多项式, 进一步分析得出 $\left(x^{2}+x+1\right)^{\alpha}$ 型结构。通过小情况试探可以发现 $P(x)=\left(x^{2}+x+1\right)^{2}$ 亦满足条件, 利用代数变形与二项式展开即证. 整个证明步骤较多, 细节繁琐, 但思路自然清晰.

题 3 设 $\mathcal{P}$ 是面积为 1 的正 2022 边形. 求实数 $c$ 满足：如果点 $A, B$ 是 $\mathcal{P}$边界上随机独立等分布选取的两个点, 那么 $A B \geq c$ 的概率是 $\frac{1}{2}$.

解 所求为 $c=\sqrt{\frac{2}{\pi}}$.



记 $n=2022=4 k+2$, 正 $n$ 边形 $\mathcal{P}$ 的各顶点按顺时针方向依次是 $A_{1} A_{2} \cdots A_{n}$, 中心为 $O$. 以 $O A_{k+1}$ 为 $x$ 轴正方向建立平面直角坐标系. 记 $A_{k} A_{k+1}, A_{k+1} A_{k+2}$ 分别交 $A_{1} A_{n}$ 与点 $U, V$. 记等腰 $\triangle A_{k+1} U V$ 的顶角为 $2 \theta$, 底角为 $\pi-\omega$. 对于平面上的点 $Z$, 用 $x(Z), y(Z)$ 分别表示其横纵坐标.

不妨设 $A$ 是边 $A_{1} A_{n}$ 上随机等分布选取的点, 首先有 $\left|A_{1} A_{k+1}\right|<c<$ $\left|A_{1} A_{k+2}\right|$, 这是因为若前一个不等号不成立, 则 $\mathbb{P}(A B \geq c)$ 恒大于 $\frac{1}{2}$; 若后一个
不等号不成立, 则 $\mathbb{P}(A B \geq c)$ 恒小于 $\frac{1}{2}$. 故存在 $W \in A_{n} A_{1}$ 使得 $W A_{k+1}=c$.

用 $T_{A}$ 表示 $\mathcal{P}$ 的边界上在顺时针方向上使 $A T_{A}=c$ 的点, 则当 $A \in A_{n} W$时三角形 $A T_{A} U$ 的外接圆半径 $R_{A}$ 恒为 $R=\frac{c}{2 \sin \omega}$.

记长度 $L(A)=U T_{A}$, 角度 $\alpha=\angle T_{A} A U, \beta=A T_{A} U$, 在 $A \in A_{n} W$ 时 $\beta$ 的最大值和最小值分别是 $\beta_{1}, \beta_{0}$, 则它们分别是 $A=W$ 时对应的 $\alpha, \beta$ 的值. 考察积分

$$
\begin{aligned}
I_{1} & =\int_{x\left(A_{n}\right)}^{x(W)} L(A) \mathrm{d}(x(A))=\int_{\beta_{0}}^{\beta_{1}} 2 R \sin \alpha \mathrm{d}(2 R \sin \beta) \\
& =\int_{\beta_{0}}^{\beta_{1}} 2 R \sin \alpha \cdot 2 R \cos \beta \mathrm{d} \beta \\
& =2 R^{2} \int_{\beta_{0}}^{\beta_{1}}(\sin (\alpha+\beta)-\sin (\beta-\alpha)) \mathrm{d} \beta \\
& =2 R^{2} \sin \omega \cdot\left(\beta_{1}-\beta_{0}\right)=2 R^{2} \sin \omega \cdot\left(\pi-\omega-2 \beta_{0}\right) .
\end{aligned}
$$

完全类似地, 当 $A \in W A_{1}$ 时, 记长度 $M(A)=V T_{A}$, 可得

$$
I_{2}=\int_{x(W)}^{x\left(A_{1}\right)} M(A) \mathrm{d}(x(A))=2 R^{2} \sin \omega \cdot\left(2 \beta_{0}+4 \theta-\omega\right)
$$

记 $\mathcal{P}$ 的边长为 $2 a$, 由于 $\mathbb{P}(A B \geq c)=\frac{1}{2}$, 结合 $\omega=\theta+\frac{\pi}{2}$, 应有

$$
4 R^{2} \cos \theta \cdot \theta=I_{1}+I_{2}=A_{1} A_{n} \cdot U A_{k+1}=\frac{2 a^{2}}{\sin \theta}
$$

由于 $\mathcal{P}$ 面积为 1 , 其中 $a^{2}=\frac{\tan \theta}{n}$. 故

$$
c^{2}=\frac{2}{n \theta}=\frac{2}{\pi} \Rightarrow c=\sqrt{\frac{2}{\pi}}
$$

评注 本题有一定难度. 看到条件会想到积分, 但直接对长度积分会十分繁琐。上述解答中将折线的长度转化为等腰三角形边上的长度, 极大地简化了计算过程. 值得一提的是, 题目中 $n$ 模 4 余 2 是必要的, 否则 $A_{k+1} U \neq A_{k+1} V$, 不具有对称性.

题 4 设 $A B C D E$ 是凸五边形, $\triangle A B E, \triangle B E C$ 和 $\triangle E D B$ 都按对应顶点相似. 直线 $B E$ 和 $C D$ 交于点 $T$. 证明: 直线 $A T$ 和 $\triangle A C D$ 外接圆相切.

证明 记 $B D$ 与 $E C$ 交于点 $P$. 过 $D$ 作平行于 $B E$ 的直线交 $B C$ 于点 $Q$,过 $C$ 作平行于 $B E$ 的直线交 $E D$ 的延长线于点 $R$. 作 $A$ 关于 $B E$ 的对称点 $S$.

记 $B E$ 的中垂线为 $\ell$. 由相似关系,

$$
\angle A E B=\angle E B D, \angle B E C=\angle A B E,
$$

故 $A B / / E C, A E / / B D, A B P E$ 为平行四边形, $S, P$ 关于 $\ell$ 对称.



因

$$
\angle C B E=\angle B A E=\angle B E D,
$$

故 $(B, E),(Q, D),(C, R)$ 为三组关于 $\ell$ 的对称点.

由

$$
\angle B D Q=\angle D B E=\angle A E B=\angle B C E \text {, }
$$

有 $P, D, C, Q$ 共圆, 同理 $R, D, P, C$ 共圆. 结合对称性, 有 $S, P, D, R, C, Q$六点共圆. 又 $B, P, D$ 共线, 故 $Q, S, E$ 共线; $E, P, C$ 共线, 故 $B, S, R$ 共线.

对圆内接六边形 $S S Q C D R$ 使用 Pascal 定理, 记 $S S \cap C D=T^{\prime}$, 则 $T^{\prime}, E, B$共线, 因此 $T^{\prime}=T$, 并且 $T S$ 为 $\odot(D C S)$ 的切线. 故

$$
T A^{2}=T S^{2}=T D \cdot T C
$$

即 $A T$ 与 $\triangle A C D$ 的外接圆相切.

评注 本题是难度中等的几何题. 解答中展示了一种纯几何的证明, 其关键在于通过相似关系得到大量角度关系，从而注意到图形的“对称性”，构选一些对称点以发掘更多的相关性质. 最后一步对退化六边形使用 Pascal 定理是一种很好的刻画切线的方式, 绕开了很多涉及切线本身的过程.

题 5 ELMO 社交平台上有 $n^{3}(n \geq 3)$ 个用户，用户之间的好友是相互的.大于等于 3 个相互为好友的用户的集合称为一个 ELMO 俱乐部. 已知任意 $n$ 个用户中，至少有三个用户构成的集合是一个 ELMO 俱乐部. 证明: 存在一个有五个成员的 ELMO 俱乐部。

证明 1 将题目转化为图论语言叙述: 已知简单图 $G(V, E)$ 满足 $|V|=n^{3}$,
且 $G$ 的任意 $n$ 个顶点诱导的子图中存在一个 $K_{3}$ 子图, 则 $G$ 中存在一个 $K_{5}$ 子图.

对 $n$ 归纳, $n=3$ 时显然成立. 假设命题在 $n-1$ 时成立, 考虑 $n$ 时情形.

不妨设存在 $n-1$ 个点, 它们在 $G$ 中任意三点间至少有两点不连边,记为 $v_{1}, v_{2}, \cdots, v_{n-1}$, 否则直接满足归纳假设的条件. 由 Turan 定理, 由 $v_{1}, v_{2}, \cdots, v_{n-1}$ 诱导的子图 $H$ 的边数满足 $|E(H)| \leq\left\lfloor\frac{(n-1)^{2}}{4}\right\rfloor$. 在余下的 $n^{3}-n+1$ 个点中任取点 $v$, 则存在 $1 \leq i<j \leq n-1$ 使 $v, v_{i}, v_{j}$ 之间两两连边, 任取其中一对 $(i, j)$ 并记为 $f(v)=(i, j)$. 从而存在一对 $(i, j)$ 至少被

$$
\left(n^{3}-n+1\right) \cdot\left\lfloor\frac{(n-1)^{2}}{4}\right\rfloor^{-1}>n
$$

个点 $v$ 对应. 而这 $n$ 个点中存在 $K_{3}$ 子图, 它并入 $v_{i}, v_{j}$ 后将生成 $K_{5}$ 子图, 故结论成立.

证明 2 转化为图论语言同证明 1 . 先证一个引理:

引理 已知简单图 $G\left(V, F_{2}\right)$ 满足 $|V|=n^{2}$, 且 $G$ 的任意 $n$ 个顶点诱导的子图中存在一个 $K_{3}$ 子图, 则 $G$ 中存在一个 $K_{4}$ 子图.

证明 对 $n$ 归纳, $n=3$ 时显然成立. 假设命题在 $n-1$ 时成立, 考虑 $n$ 时情形: 取某个 $v_{0} \in V$, 记 $N\left(v_{0}\right)$ 为 $v_{0}$ 在 $G$ 中的邻域. 若 $\left|N\left(v_{0}\right)\right| \geq n$, 则 $K_{4}$ 子图已经存在. 否则 $\left|N\left(v_{0}\right)\right| \leq n-1$, 则

$$
\left|V \backslash\left(N\left(v_{0}\right) \cup\left\{v_{0}\right\}\right)\right| \geq n^{2}-n \geq(n-1)^{2} .
$$

对于 $G$ 中包含 $v_{0}$ 但与 $N\left(v_{0}\right)$ 交为空的 $n$ 个点, $K_{3}$ 子图必产生于除 $v_{0}$ 外的 $n-1$ 个点诱导的子图. 由归纳假设可知 $G$ 中存在 $K_{4}$ 子图, 引理获证.

回到原题, 归纳证明原命题. $n=3$ 时显然成立. 假设命题在 $n-1$ 时成立,考虑 $n$ 时情形: 取某个 $v_{0} \in V$, 若 $\left|N\left(v_{0}\right)\right| \geq n^{2}$, 则由引理知 $G$ 中已经存在 $K_{5}$子图. 否则 $\left|N\left(v_{0}\right)\right| \leq n^{2}-1$, 则

$$
\left|V \backslash\left(N\left(v_{0}\right) \cup\left\{v_{0}\right\}\right)\right| \geq n^{3}-n^{2} \geq(n-1)^{3} .
$$

对于 $G$ 中包含 $v_{0}$ 但与 $N\left(v_{0}\right)$ 交为空的 $n$ 个点, $K_{3}$ 子图必产生于除 $v_{0}$ 外的 $n-1$ 个点诱导的子图. 由归纳假设, $G$ 中存在 $K_{5}$ 子图, 结论成立.

评注本题是较为简单的图论问题. 证明 1 直接用平均值原理取出 $K_{5}$; 证明 2 中想到引理则较为关键, 而引理可以通过 $n$ 个点时存在 $K_{3}, n^{3}$ 个点时存在 $K_{5}$自然想到 $n^{2}$ 个点时存在 $K_{4}$, 此后分两步归纳即可.
题 6 求所有函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$ 满足: 对所有整数 $m$ 和 $n$, 都有

$$
f(f(m)-n)+f(f(n)-m)=f(m+n) .
$$

解 (AOPS) 所求函数为 $f(n)=2 n$ 或 $f(n) \equiv 0$, 容易验证它们符合要求.以下用 $P(m, n)$ 简记在条件中代入 $m, n$. 先证明一个引理:

引理 $\quad$ 对于 $n \in \mathbb{Z}$ 及 $k \in \mathbb{N}$, 若 $2^{k} \mid n$, 则 $2^{k} \mid f(n)$.

证明 对 $k$ 归纳, $k=0$ 时显然成立. 下设 $k>0$ 且 $k-1$ 时命题成立. 考虑 $k$ 时情形: $P\left(\frac{n}{2}, \frac{n}{2}\right)$ 得

$$
f(n)=f\left(\frac{n}{2}+\frac{n}{2}\right)=2 f\left(f\left(\frac{n}{2}\right)-\frac{n}{2}\right) .
$$

其中 $2^{k-1} \left\lvert\, \frac{n}{2}\right.$, 故由归纳假设,

$$
2^{k-1}\left|f\left(\frac{n}{2}\right)-\frac{n}{2}, \quad 2^{k-1}\right| f\left(f\left(\frac{n}{2}\right)-\frac{n}{2}\right),
$$

故 $2^{k} \mid f(n)$, 归纳成立. 引理获证.

回到原题, 由引理立即可以推出 $f(0)=0 . P(n, n)$ 得 $f(2 n)=2 f(f(n)-n)$,即 $f(2 n)-(f(f(n)-n)-n)=(f(f(n)-n)-n)+2 n$, 故 $P(f(f(n)-n)-n, 2 n)$得

$$
f(f(f(f(n)-n)-n)-2 n)=0 .
$$

再令 $P(m, f(m)-m)$ 得

$$
f(m)+f(f(f(m)-m)-m)=f(f(m)),
$$

$P(m, 0)$ 得

$$
f(f(m))+f(-m)=f(m),
$$

故有

$$
f(-m)+f(f(f(m)-m)-m)=0
$$

对一切 $m \in \mathbb{Z}$ 成立.

以下对 $f$ 的零点进行讨论.

(1) $f(n)$ 仅有 0 为零点. 在以上两个结果中令 $n=m$ 直接得到 $f(-m)=$ $-2 m$ 对一切 $m \in \mathbb{Z}$ 成立, 即此时解得 $f(n)=2 n$ 对一切 $n \in \mathbb{Z}$ 成立.

(2) $f(n)$ 存在多于一个零点.

令 $S=\{x \mid f(x)=0\}$, 则 $|S| \geq 2$. 由 $P(m, 0)$ 知 $m \in S$ 可得 $-m \in S$.由 $P(m, n)$ 知 $m, n \in S$ 可得 $m+n \in S$. 故由Bezout 定理, 存在 $t \in \mathbb{N}^{*}$ 使 $S=\{t n \mid n \in \mathbb{Z}\}$.
若 $t$ 为偶数, $P\left(\frac{t}{2}, \frac{t}{2}\right)$ 得

$P\left(-t, \frac{t}{2}\right)$ 得

$$
f\left(f\left(\frac{t}{2}\right)-\frac{t}{2}\right)=0 \Rightarrow f\left(\frac{t}{2}\right) \equiv \frac{t}{2} \quad(\bmod t) .
$$

$$
f\left(f\left(\frac{t}{2}\right)-t\right)=0 \Rightarrow f\left(\frac{t}{2}\right) \equiv 0 \quad(\bmod t)
$$

矛盾! 故 $t$ 为奇数.

在最初两个结果中令 $n=m$, 我们有

$$
\begin{aligned}
f(-n) & \equiv-f(f(f(n)-n)-n) \\
& \equiv-2 n \quad(\bmod t)
\end{aligned}
$$

故 $f(n) \equiv 2 n(\bmod t)$ 对一切 $n \in \mathbb{Z}$ 成立.

对于 $m \in \mathbb{Z}, t \nmid m, k \in \mathbb{Z}, P(k t, m)$ 得

$$
f(-m)+f(f(m)-k t)=f(m+k t)
$$

此即为: 对于 $x \equiv m(\bmod t)$, 均有

$$
f(x)-f(m+f(m)-x)=f(-m) .
$$

(a) 若存在 $m, n \in \mathbb{Z}$ 使 $m \equiv n(\bmod t)$, 但 $f(m)+m \neq f(n)+n$.

对于 $x \equiv m(\bmod t)$, 在上式中分别代入 $m, n$ 作差得

$$
f(m+f(m)-x)-f(n+f(n)-x)=f(-n)-f(-m) .
$$

其中 $m+f(m)-x \equiv 2 m(\bmod t)$, 故对一切 $y \equiv 2 m(\bmod t)$ 均有

$$
f(y)-f((n+f(n)-m-f(m))+y)=f(-n)-f(-m) \text {. }
$$

记其中 $E=f(-n)-f(-m),-D=n+f(n)-m-f(m)$, 则 $D$ 是 $t$ 的某个非零倍数. 因此对 $y \equiv 2 m(\bmod t), f(y)-f(y-D)=E$, 故 $f(y)-f(y-k D)=k E$.

在 $(\star)$ 中令 $x=m+D$ 得 $f(m+D)-f(f(m)-D)=f(-m)$, 类似可知对一切 $y \equiv m(\bmod t)$ 均有 $f(y)-f(y-D)=-E$.

由 $P(m, m)$ 与 $P\left(m+D^{2}, m\right)$ 作差可知

$$
\begin{aligned}
f\left(m+D^{2}-m\right)-f(m+m)= & f\left(f\left(m+D^{2}\right)-m\right)-f(f(m)-m) \\
& +f\left(f(m)-m-D^{2}\right)-f(f(m)-m),
\end{aligned}
$$

此即

$$
E D=f(f(m)+E D-m)-f(f(m)-m)+E D,
$$

故 $f(f(m)-m)=f(f(m)+E D-m)$. 而

$$
f(f(m)+E D-m)=f(f(m)-m)-E^{2},
$$

故 $-E^{2}=0, E=0$, 故 $f(m), f(m+t), \cdots$ 为周期序列.

令 $M$ 为所有 $f(m+k t)$ 中的最大者, 假设 $t \geq 2$, 则存在 $\alpha \equiv m(\bmod t)$ 且 $2^{M} \mid \alpha$. 由引理, 有 $f(\alpha)=0$ 或 $|f(\alpha)|>M$, 故只能 $f(\alpha)=0$. 但 $t \nmid \alpha$, 矛盾! 故只能 $t=1$, 此时 $f(n) \equiv 0$ 对一切 $n \in \mathbb{Z}$ 成立.

(b) 若对一切 $m, n \in \mathbb{Z}, m \equiv n(\bmod t)$ 均有 $f(m)+m=f(n)+n$.

则 $f(n)-f(n-t)=t$, 则可类似 (a) 中证明得出矛盾.

综合以上, $f(n)=2 n$ 或 $f(n) \equiv 0$.

评注 这是一道非常困难的函数方程问题, 需要进行大量的计算与推导. 在证明的主要部分之前, 不妨先通过条件式本身推出一些基本的小结论, 其中 $f(0)=0$ 的证明是有趣的, 通过证明 2 的任意幂次整除 $f(0)$ 证出. 此后自然会想到根据零点情况分类讨论. 在第 (2) 部分中我们可以注意到 $f(n)$ 在每个模 $t$的剩余类中具有一些类似一次函数的性质, 从而推出 $f$ 所具有的周期性, 再结合引理即可通过大小关系推出矛盾.

