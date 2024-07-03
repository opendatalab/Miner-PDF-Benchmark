数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2017 年秋季上海新星数学奥林匹克试题解析 

吴尉迟 ${ }^{1}$ 叶思 ${ }^{1}$ 施柯杰 $^{2}$

(1. 上海大学数学系, 200444；2. 复旦大学附属中学, 200433)

2017 年秋季上海新星数学奥林匹克于 2017 年 11 月 22 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答.

## I. 试 题

1. 设 $A M$ 和 $C N$ 是一个锐角 $\triangle A B C$ 的两条高. $Y$ 是直线 $A C$ 和 $M N$的交点. 点 $X$ 位于 $\triangle A B C$ 内使得四边形 $M B N X$ 是一个平行四边形. 证明: $\angle M X N$ 的角平分线垂直于 $\angle M Y C$ 的角平分线.

(上海大学 叶思 供题)

2. 对给定的正整数 $n(n \geq 2)$, 求最小的正整数 $k$, 使得对任意 $k$ 个不同的整数中必存在两个不同的数, 其和或差为 $n$ 的倍数.

(复旦大学附属中学 施柯杰 供题)

3. 设 $p$ 是大于 5 的素数, 证明存在两个正整数 $m, n$, 使得 $m+n<p$ 且 $p \mid 2^{m} 3^{n}-1$.

(上海大学 吴尉迟 供题)

4. 给定正整数 $n \geq 2$, 求最小的实数 $c$, 使得对任意非负实数 $a_{1}, a_{2}, \cdots, a_{n}$,都存在 $i \in\{1,2, \cdots, n\}$, 满足 $a_{i-1}+a_{i+1} \leq c a_{i}$, 其中 $a_{0}=a_{n+1}=0$.

(中国人民大学附属中学 张端阳 供题)

5. 如图, 四边形 $A B C D$ 内接于圆 $O$, 且 $A B \cdot C D=$ $B C \cdot A D$. 直线 $A B, C D$ 交于 $K . A C, B D$ 交于 $J(O, J$不重合). 过 $K$ 作 $O J$ 的垂线, 分别与直线 $B D, A C$ 交于 $E, F$. 以 $E F$ 为直径的圆与线段 $O J$ 交于 $T$. 证明: $K T$ 平分 $\angle E T F$.

(广西卢圣 供题)



收稿日期: 2017-12-10； 修订日期: 2018-01-22.

6. 给定正整数 $m, n(1 \leq m \leq n)$, 在 $m \times n$ 棋盘 $M$ 的每个方格中填上 1 或 -1, 然后进行如下操作: 将同行 (或同列) 的每个数都同时加上 1 .

如果最初棋盘 $M$ 中恰有 $r$ 个 1 , 求所有的正整数 $r$, 使无论最初 $r$ 个 1 填在哪些方格中, 都不能通过有限次操作使各数变得相等.

(深圳高级中学 冯跃峰 供题)

## II. 解 答

题 1. 设 $A M$ 和 $C N$ 是一个锐角 $\triangle A B C$ 的两条高. $Y$ 是直线 $A C$ 和 $M N$的交点. 点 $X$ 位于 $\triangle A B C$ 内使得四边形 $M B N X$ 是一个平行四边形. 证明: $\angle M X N$ 的角平分线垂直于 $\angle M Y C$ 的角平分线.



证明 由 $\triangle A B M \backsim \triangle C B N$ 得

$$
\frac{B M}{B N}=\frac{A B}{B C}
$$

从而 $\triangle B M N \backsim \triangle B A C$, 故 $\angle B M N=\angle B A C$.

设 $\angle M X N$ 与 $\angle M Y C$ 的角平分线交于 $P$, 则

$$
\begin{aligned}
\angle Y P X & =\angle Y N X+\frac{1}{2} \angle M Y C-\frac{1}{2} \angle M X N \\
& =180^{\circ}-\angle X N M+\frac{1}{2}(\angle B M N-\angle B C A)-\frac{1}{2} \angle A B C \\
& =180^{\circ}-\angle B M N+\frac{1}{2}(\angle B M N-\angle B C A)-\frac{1}{2} \angle A B C \\
& =180^{\circ}-\angle B A C+\frac{1}{2}(\angle B A C-\angle B C A)-\frac{1}{2} \angle A B C \\
& =180^{\circ}-\frac{1}{2}(\angle B A C+\angle B C A+\angle A B C)=90^{\circ} .
\end{aligned}
$$

命题得证.

评注 这是简单题, 只需注意角之间的关系即可. 绝大多数的同学做对了此题.
题 2. 对给定的正整数 $n(n \geq 2)$, 求最小的正整数 $k$, 使得对任意 $k$ 个不同的整数中必存在两个不同的数, 其和或差为 $n$ 的倍数.

解 答案为: $k_{\min }=2+\left\lfloor\frac{n}{2}\right\rfloor$.

一方面, 考虑 $1+\left\lfloor\frac{n}{2}\right\rfloor$ 个数 $0,1, \ldots,\left\lfloor\frac{n}{2}\right\rfloor$. 显然它们中任意两个不同的数的差不为 $n$ 的倍数, 其中任意两个不同的数的和均小于 $n$, 因而也不为 $n$ 的倍数.这说明满足条件的 $k \geq 2+\left\lfloor\frac{n}{2}\right\rfloor$.

下证 $k=2+\left\lfloor\frac{n}{2}\right\rfloor$ 时结论成立.

对任意 $2+\left\lfloor\frac{n}{2}\right\rfloor$ 个不同的整数, 将其中模 $n$ 的余 $i$ 和 $n-i$ 的数分为一组 $\left(i=0, \ldots,\left\lfloor\frac{n}{2}\right\rfloor\right)$, 这样至多有 $1+\left\lfloor\frac{n}{2}\right\rfloor$ 组. 由抽屉原理知 $2+\left\lfloor\frac{n}{2}\right\rfloor$ 个数必有两个数属于同一组. 若这两个数模 $n$ 同余, 则其差为 $n$ 的倍数; 若它们模 $n$ 不同余, 则其和为 $n$ 的倍数. 这说明此时结论成立.

综上, $k_{\min }=2+\left\lfloor\frac{n}{2}\right\rfloor$.

评注此题为容易题, 约 $70 \%$ 的同学作对了此题. 由题设容易想到构造 $1+\left\lfloor\frac{n}{2}\right\rfloor$ 个抽屉 (即将和或差为 $n$ 的倍数的数放到一组).

题 3. 设 $p$ 是大于 5 的素数, 证明存在两个正整数 $m, n$, 使得 $m+n<p$ 且 $p \mid 2^{m} 3^{n}-1$.

证法一 考虑形如 $2^{i} 3^{j}$ 的数, 其中 $1 \leq i, j \leq p-1$. 则这样的数共有 $(p-1)^{2}$个. 注意到 $(p-1)^{2} \geq p+1$, 故由抽屉原理可知存在不同的正整数对 $\left(i_{1}, j_{1}\right)$, $\left(i_{2}, j_{2}\right)$ 使得

$$
2^{i_{1}} 3^{j_{1}} \equiv 2^{i_{2}} 3^{j_{2}} \quad(\bmod p), 1 \leq i_{1}, i_{2}, j_{1}, j_{2} \leq p-1
$$

由于 $i_{1} \neq i_{2}$ 或 $j_{1} \neq j_{2}$, 结合上式知 $i_{1} \neq i_{2}$ 且 $j_{2} \neq j_{2}$.

又由费马小定理知 $2^{p-1} \equiv 3^{p-1} \equiv 1(\bmod p)$, 从而

$$
2^{p-1} 2^{i_{1}} 3^{j_{1}} \equiv 2^{i_{2}} 3^{j_{2}} 3^{p-1} \quad(\bmod p),
$$

即

$$
2^{p-1+i_{1}-i_{2}} \equiv 3^{p-1+j_{2}-j_{1}} \quad(\bmod p)
$$

令

$$
i=\left\{\begin{array}{ll}
i_{1}-i_{2} & \text { 若 } i_{1}>i_{2} \\
i_{1}-i_{2}+p-1 & \text { 若 } i_{1} \leq i_{2}
\end{array}, j=\left\{\begin{array}{ll}
j_{1}-j_{2} & \text { 若 } j_{1}>j_{2} \\
j_{1}-j_{2}+p-1 & \text { 若 } j_{1} \leq j_{2}
\end{array},\right.\right.
$$

则有

$$
2^{i} \equiv 3^{j} \quad(\bmod p)
$$

若 $i \leq j$, 令 $m=i, n=p-1-j$, 此时正整数 $m, n$ 满足 $m+n<p$ 且

$$
2^{m} 3^{n} \equiv 2^{i} 3^{p-1-j} \equiv 3^{j} 3^{p-1-j} \equiv 3^{p-1} \equiv 1 \quad(\bmod p)
$$

若 $i>j$, 令 $m=p-1-i, n=j$, 此时正整数 $m, n$ 满足 $m+n<p$ 且

$$
2^{m} 3^{n} \equiv 2^{p-1-i} 3^{j} \equiv 2^{p-1-i} 2^{i} \equiv 2^{p-1} \equiv 1 \quad(\bmod p) .
$$

命题得证.

证法二 设 2,3 模 $p$ 的阶分别为 $s, t$, 又由费马小定理知,

$$
2^{p-1} \equiv 3^{p-1} \equiv 1 \quad(\bmod p)
$$

从而 $s|p-1, t| p-1$. 下分两种情况证明结论.

1) 若 $s=p-1$ 或 $t=p-1$. 当 $s=p-1$ 时, 此时, $2, \cdots, 2^{p-1}$ 构成模 $p$ 的完系, 从而存在正整数 $0 \leq k \leq p-1$, 使得 $2^{k} 3 \equiv 1(\bmod p)$. 注意到 $k=0$ 或 $p-1$均不满足上式, 从而有 $0<k<p-1$. 此时, 令 $m=k, n=1$ 即可满足要求. 同理, 当 $t=p-1$ 时, 也存在满足要求的 $m, n$.
2) 若 $s \neq p-1$ 且 $t \neq p-1$. 结合 $s|p-1, t| p-1$ 知 $s, t \leq \frac{p-1}{2}$. 此时令 $m=s, n=t$, 则有 $m+n \leq p-1<p, 2^{m} 3^{n} \equiv 1(\bmod p)$.

由 1) 和 2) 知结论成立.

评注 (1). 此题为中等偏易的题,约有 $50 \%$ 的同学做对了此题. 证法一是基于费马小定理的一个朴素的想法, 即只需证明存在小于 $p-1$ 的正整数 $i, j$ 使得 $2^{i} \equiv 3^{j}(\bmod p)$, 而该结果用抽屈原理便可证明. 证法二给出了一个利用阶的简单证明, 相较于证法一, 其优点是可以利用该方法证明多元的情形：设 $p$ 是大于 7 的素数, 则存在两个正整数 $m, n, l$, 使得 $m+n+l<\frac{3 p}{2}$ 且 $p \mid 2^{m} 3^{n} 5^{l}-1$.

(2). 下面的证法给出了 $m+n$ 上界的一个更强的估计(这个上界当 $p=7$ 时可以取到, 此时 $m=n=2)$, 即证明如下命题:

设 $p$ 是大于 5 的素数, 证明存在两个正整数 $m, n$, 使得 $m+n \leq \frac{p+1}{2}$ 且 $p \mid 2^{m} 3^{n}-1$.

证明 设 2,3 模 $p$ 的阶分别为 $s, t$, 从而 $\max \{s, t\}=\frac{p-1}{k}, k \in \mathbb{N}^{*}$. 若 $\max \{s, t\} \leq \frac{p-1}{4}$, 则我们取 $n=s, m=t$ 即可满足要求. 故只需考虑 $k=1,2,3$的情形. 由对称性, 可不妨设 $s \geq t$. 则有 $\max \{s, t\}=s$.

i) 若 $k=1$, 即 $s=p-1$, 从而存在 $1<l<p$ 使得 $2^{l} \equiv 3(\bmod p)$. 设 $p-1=l q+r$, 其中 $r \leq l, q, r \in \mathbb{N}^{*}$.

现在我们取 $n=r, m=q$, 则我们有 $2^{n} 3^{m} \equiv 2^{r} 2^{l q} \equiv 1(\bmod p)$. 注意到 $q+r \leq \frac{p-1}{l}+l-1$, 故若 $l \leq \frac{p-1}{2}$, 则由 $2 \leq l \leq \frac{p-1}{2}$ 知 $m, n$ 满足条件. 若 $l>\frac{p-1}{2}$,
则 $q=1$, 从而由 $p-1=l q+r$ 知 $n+m=p-l$, 此时 $m, n$ 也满足要求.

ii) 当 $k=2,3$ 时, 令 $I_{s}=\left\{2^{i}(\bmod p) \mid 1 \leq i \leq s\right\}$. 我们证明存在正整数 $j \leq k$,满足 $3^{j} \in I_{s}$. 事实上, 若 $3, \ldots, 3^{k-1} \notin I_{s}$, 设 $3^{q} \times I_{s}=\left\{3^{q} 2^{i}(\bmod p) \mid 1 \leq i \leq s\right\}$,则此时, $3^{q} \times I_{s}, q=0, \ldots, k-1$ 互不相交, 又注意到 $s=\frac{p-1}{k}$, 从而

$$
\{1,2, \ldots, p-1\}=\bigcup_{q=0}^{k-1} 3^{q} \times I_{s}
$$

这时, $3^{k} \in I_{s}$. 从而存在正整数 $1 \leq l \leq s$, 使得 $2^{l} \equiv 3^{j}(\bmod p)$. 取 $n=s-l, m=$ $j$, 则有 $m+n \leq \frac{p-1}{k}+k-1 \leq \frac{p+1}{2}$ 且 $2^{m} 3^{n} \equiv 2^{s-l} 2^{l} \equiv 1(\bmod p)$.

结合 i), ii) 知结论成立.

题 4. 给定正整数 $n \geq 2$, 求最小的实数 $c$, 使得对任意非负实数 $a_{1}, a_{2}, \cdots, a_{n}$,都存在 $i \in\{1,2, \cdots, n\}$, 满足 $a_{i-1}+a_{i+1} \leq c a_{i}$, 其中 $a_{0}=a_{n+1}=0$.

解 当 $c<2 \cos \frac{\pi}{n+1}$ 时, 对 $0 \leq k \leq n+1$, 取 $a_{k}=\sin \frac{k \pi}{n+1}$. 此时对任意 $i \in\{1,2, \cdots, n\}$,

$a_{i-1}+a_{i+1}=\sin \frac{(i-1) \pi}{n+1}+\sin \frac{(i+1) \pi}{n+1}=2 \cos \frac{\pi}{n+1} \sin \frac{i \pi}{n+1}>c a_{i}$,

不满足要求.

下证当 $c=2 \cos \frac{\pi}{n+1}$ 时满足要求. 否则, 对任意 $i \in\{1,2, \cdots, n\}$, 都有

$$
a_{i-1}+a_{i+1}>2 a_{i} \cos \frac{\pi}{n+1} .
$$

我们归纳证明, 对 $1 \leq k \leq n-1$, 满足

$$
a_{k+1}>\frac{\sin \frac{(k+1) \pi}{n+1}}{\sin \frac{k \pi}{n+1}} a_{k}
$$

当 $k=1$ 时, 在 $(*)$ 中取 $i=1$ 得, $a_{2}>2 a_{1} \cos \frac{\pi}{n+1}=\frac{\sin \frac{2 \pi}{n+1}}{\sin \frac{\pi}{n+1}}$ 成立.

假设 $k-1$ 时成立, 来看 $k$ 时的情形.

由归纳假设, $a_{k}>\frac{\sin \frac{k \pi}{n+1}}{\sin \frac{(k-1) \pi}{n+1}} a_{k-1}$; 在 (*) 中取 $i=k$ 得, $a_{k-1}+a_{k+1}>$ $2 a_{k} \cos \frac{\pi}{n+1}$. 所以

归纳证毕.

$$
a_{k+1}>\left(2 \cos \frac{\pi}{n+1}-\frac{\sin \frac{(k-1) \pi}{n+1}}{\sin \frac{k \pi}{n+1}}\right) a_{k}=\frac{\sin \frac{(k+1) \pi}{n+1}}{\sin \frac{\sin k \pi}{n+1}} a_{k}
$$

取 $k=n-1$ 得, $a_{n}>\frac{\sin \frac{n \pi}{n+1}}{\sin \frac{(n-1) \pi}{n+1}}=\frac{1}{2 \cos \frac{\pi}{n+1}} a_{n-1}$. 但在 (*) 中取 $i=n$ 得, $a_{n-1}>2 a_{n} \cos \frac{\pi}{n+1}$, 这与上式矛盾!

综上, 所求实数的最小值为 $2 \cos \frac{\pi}{n+1}$.

评注 (1). 此题是本次考试得分率最低的一道题,约有 $10 \%$ 做对了此题. 此
题是由 2013 年罗马尼亚国家队选拔试题改编而来:

已知 $n$ 为正整数, $x_{1}, x_{2}, \cdots, x_{n}$ 为正实数, 证明:

$$
\begin{aligned}
& \min \left\{x_{1}, \frac{1}{x_{1}}+x_{2}, \cdots, \frac{1}{x_{n-1}}+x_{n}, \frac{1}{x_{n}}\right\} \leq 2 \cos \frac{\pi}{n+2} \\
\leq & \max \left\{x_{1}, \frac{1}{x_{1}}+x_{2}, \cdots, \frac{1}{x_{n-1}}+x_{n}, \frac{1}{x_{n}}\right\} .
\end{aligned}
$$

(2). 本题的难点在于如何求出常数 $c$. 也可以通过设最佳常数为 $c=c(n)$,考虑使所有题中所有不等式均成立的 $\left(a_{1}, \cdots, a_{n}\right)$, 可得 $c(2)=1, c(3)=$ $\sqrt{2}, c(4)=\frac{\sqrt{5}+1}{2}, c(5)=\sqrt{3}$, 从而猜测 $c(n)=2 \cos \frac{\pi}{n+1}$. 也可以利用构造数列计算常数 $c$ :

## 解 (雅礼中学 覃俊卓)

构造数列 $\left\{a_{n}\right\}: a_{0}=a_{1}=1, a_{n+1}=c a_{k}-a_{k-1}(k=1,2, \ldots, n)$, 且 $a_{n+1}=0$ ( $c$ 为待定的正常数).

解特征方程 $x^{2}-c x+1=0$ 得两复数根 $\alpha=\frac{c+\sqrt{c^{2}-4}}{2}, \beta=\frac{c-\sqrt{c^{2}-4}}{2}$. 故可设 $a_{k}=A \alpha^{n}+B \beta^{n}$. 令 $n=0, n=1$ 可得

$$
\left\{\begin{array}{l}
A+B=a_{0}=0, \\
A \cdot \frac{c+\sqrt{c^{2}-4}}{2}+B \cdot \frac{c-\sqrt{c^{2}-4}}{2}=1 .
\end{array}\right.
$$

从而有 $A=\frac{1}{\sqrt{c^{2}-4}}, B=-\frac{1}{\sqrt{c^{2}-4}}$. 又由 $a_{n+1}=0$ 知, $\alpha^{n+1}=\beta^{n+1}$, 注意到 $\alpha \beta=1$,故有 $\alpha^{2(n+1)}=1$. 这说明 $\alpha$ 是 $2(n+1)$ 次单位根, 所以有

$$
\alpha=\cos \frac{r \pi}{n+1}+i \sin \frac{r \pi}{n+1}, r=0,1, \cdots, 2 n-1
$$

为了使 $c$ 较大, 可取 $r=1$ (当 $r=0$ 时, $c=2$ 不满足要求), 有 $\frac{c}{2}+\frac{\sqrt{c^{2}-4}}{2}=$ $\cos \frac{\pi}{n+1}+i \sin \frac{\pi}{n+1}$, 故 $c=2 \cos \frac{\pi}{n+1}$.

题 5. 如图, 四边形 $A B C D$ 内接于圆 $O$, 且 $A B \cdot C D=B C \cdot A D$. 直线 $A B, C D$ 交于 $K . A C, B D$ 交于 $J(O, J$ 不重合). 过 $K$ 作 $O J$ 的垂线, 分别与直线 $B D, A C$ 交于 $E, F$. 以 $E F$ 为直径的圆与线段 $O J$ 交于 $T$. 证明: $K T$ 平分 $\angle E T F$.

证明 由于 $A B \cdot C D=B C \cdot A D$. 故 $A B C D$ 为调和四边形.

于是设 $B$ 关于 $\odot O$ 的切线与 $D$ 关于 $\odot O$ 的切线交于 $F^{\prime}$, 则 $F^{\prime}, C, A$ 共线.

设 $C$ 关于 $\odot O$ 的切线与 $A$ 关于 $\odot O$ 的切线交于 $E^{\prime}$. 则 $E^{\prime}, B, D$ 共线.

延长 $A D, B C$ 交于 $L$. 对退化的六边形 $A B C C D A$ 运用 Pascal 定理得 $K, F^{\prime}, L$ 共线, 同理有 $E^{\prime}, K, L$ 共线, 故 $E^{\prime}, F^{\prime}, K, L$ 共线.



由 Brocard 定理知 $O J \perp K L$, 从而有 $O J \perp E^{\prime} F^{\prime}$, 结合题设知 $E=E^{\prime}$, $F=F^{\prime}$.

连接 $E A, E C$, 则其为 $\odot O$ 切线. 同样地连接 $F B, F D$, 则 $F B, F D$ 为 $\odot O$切线. 延长 $O J$ 交 $E F$ 于 $P$. 则 $T P \perp E F$.

又 $T$ 在以 $E F$ 为直径的圆上, 所以 $\angle E T F=90^{\circ}$. 因此 $E T^{2}=E P \cdot E F$.

又 $\angle O B F=\angle O D F=90^{\circ}, \angle O P F=90^{\circ}$, 所以 $O, B, P, F, D$ 五点共圆, 即 $B, D, F, P$ 共圆, 从而 $E B \cdot E D=E P \cdot E F=E T^{2}$. 又 $E B \cdot E D=E A^{2}=E C^{2}$,所以 $E A=E C=E T$. 同理有 $F B=F D=F T$.

由梅涅劳斯定理, $\frac{E D}{D J} \cdot \frac{J C}{C F}=\frac{E K}{K F}$.

又 $F B, F D$ 为切线, 所以 $(F, C, J, A)$ 为调和点列. 故 $\frac{J C}{C F}=\frac{J A}{A F}$. 因此

$$
\begin{aligned}
\frac{E D}{D J} \cdot \frac{J C}{C F} & =\frac{E D}{D J} \cdot \frac{J A}{A F}=\frac{S_{\triangle A D E}}{S_{\triangle A D J}} \cdot \frac{S_{\triangle A D J}}{S_{\triangle A D F}} \\
& =\frac{S_{\triangle A D E}}{S_{\triangle A D F}}=\frac{A D \cdot A E \cdot \sin \angle D A E}{A D \cdot D F \cdot \sin \angle F D A} .
\end{aligned}
$$

注意到 $\angle D A E=\angle F D A$. 故

$$
\frac{E D}{D J} \cdot \frac{J C}{C F}=\frac{A E}{D F}=\frac{E T}{F T}
$$

所以 $\frac{E K}{F K}=\frac{E T}{F T}$, 故 $K T$ 为 $\angle E T F$ 平分线.

即原题证毕.

评注 此题是较难的几何题, 约有 $25 \%$ 的同学做对了此题. 此题的关键是要发现 $E A, E C, F B, F D$ 是圆的切线, 即 $E F$ 是 $J$ 关于圆的极线. 此题是合成题,需要对圆的一些基本图形和基本性质比较熟悉（Brocard 定理, 切线性质, 调和点列), 如果对这些性质比较熟悉, 这个题目是不难做出来的.
题 6. 给定正整数 $m, n(1 \leq m \leq n)$, 在 $m \times n$ 棋盘 $M$ 的每个方格中填上 1 或 -1 , 然后进行如下操作: 将同行 (或同列) 的每个数都同时加上 1 .

如果最初棋盘 $M$ 中恰有 $r$ 个 1 , 求所有的正整数 $r$, 使无论最初 $r$ 个 1 填在哪些方格中, 都不能通过有限次操作使各数变得相等.

解法一 记数表 $M=\left(a_{i j}\right)_{m \times n}$, 其中 $a_{i j}$ 表示 $M$ 的位于第 $i$ 行第 $j$ 列格上的数, $a_{i j}=1$ 或 $-1(1 \leq i \leq m, 1 \leq j \leq n)$.

若 $m \mid r$, 设 $r=m k$, 则可将 $M$ 的 $k$ 格列都填 1 , 其余列都填 -1 , 此时, 将填 -1 的列都操作 2 次, 各数都变成 1 , 矛盾.

所以 $m \nmid r$. 同理, $n \nmid r$.

反之, 当 $m \nmid r$, 且 $n \nmid r$ 时, 最初的棋盘 $M$ 必定有一行数不全同号, 也必有一列数不全同号 (否则与假设矛盾).

假定第 $i$ 行不全同号, 在该行中任取一个 1 , 设为 $a_{i j}=1$.

(1) 如果第 $i$ 行存在一个这样的 “ -1 ” : 它所在的列不全为 -1 , 则不妨设 $a_{i t}=-1(t \neq j), a_{s t}=1(s \neq i)$.

令 $A=\left\{a_{i j}, a_{s t}\right\}, B=\left\{a_{i t}, a_{s t}\right\}, S_{A}=a_{i j}+a_{s t}, S_{B}=a_{i t}+a_{s j}$, 定义 $f(M)=S_{A}-S_{B}$.

记考察任意一次操作, 它使 $S_{A} 、 S_{B}$ 同时增加 1 , 或都不变, 所以 $f(M)$ 在操作中保持不变.

假设通过有限次操作, 使数表 $M$ 中的每个数都变成 $c$, 则对最终的数表 $M_{2}$,有 $f\left(M_{2}\right)=(c+c)-(c+c)=0$.

但对最初的数表 $M_{1}, f\left(M_{1}\right)=(1+1)-\left(-1+a_{s j}\right)=3-a_{s j} \neq 0$, 故目标不能实现.

(2) 如果第 $i$ 行每个 “-1” 所在的列全为 -1 , 则第 $i$ 行必有一个这样的 “ 1 ” : 它所在的列不全为 1 , 不妨设 $a_{i r}=1, a_{p r}=-1(i \neq p)$.

在第 $i$ 行任取一个 -1 , 设 $a_{i q}=-1(q \neq r)$, 由于它所在的列全为 -1 , 有 $a_{p q}=-1$.

令 $A=\left\{a_{i r}, a_{p q}\right\}, B=\left\{a_{i q}, a_{p r}\right\}, S_{A}=a_{i r}+a_{p q}, S_{B}=a_{i q}+a_{p r}$, 定义 $f(M)=S_{A}-S_{B}$.

记考察任意一次操作, 它使 $S_{A} 、 S_{B}$ 同时增加 1 , 或都不变, 所以 $f(M)$ 在操作中保持不变.

假设通过有限次操作, 使数表 $M$ 中的每个数都变成 $c$, 则对最终的数表 $M_{2}$,有 $f\left(M_{2}\right)=(c+c)-(c+c)=0$.
但对最初的数表 $M_{1}, f\left(M_{1}\right)=(1-1)-(-1-1)=2 \neq 0$, 故目标不能实现.

综上所述, 所求 $r$ 是一切不为 $m$ 的倍数且不为 $n$ 的倍数的正整数.

解法二 (成都外国语中学 覃瀚林) 若存在一个 $m \times n$ 的棋盘 $M$ 中有 $r$个数为 1 , 且对 $i$ 行操作了 $a_{i}$, 第 $j$ 行操作了 $b_{j}$ 次后, 得到的棋盘中各数均为 $k$, $1 \leq i \leq m, 1 \leq j \leq n$. 从而有, $k-a_{i}-b_{j} \in\{-1,1\}, \forall 1 \leq i \leq m, 1 \leq j \leq n$. 设 $m_{i j}$ 为最初棋盘上第 $i$ 行第 $j$ 列的元素.

对于给定的 $a_{i}$, 则 $b_{j}$ 只有两种取值 $b, b+2$; 对于给定的 $b_{j}$, 则 $a_{i}$ 只有两种取值 $a, a+2$.

注意到对所有行或所有列各操作一次, 不影响结果. 故不妨设 $\min \left\{a_{i}\right\}=$ $\min \left\{b_{j}\right\}=0$; 注意到交换两行或者两列也不改变结果, 故可设 $a_{1}=\cdots=a_{s}=$ $2, a_{s+1}=\cdots=a_{m}=0 ; b_{1}=\cdots=b_{t}=2, b_{t+1}=\cdots=b_{n}=0$.

注意到 $m_{i j}(1 \leq i \leq s, 1 \leq j \leq t)$ 增加了 $4, m_{i j}(s+1 \leq i \leq m, t+1 \leq j \leq n)$保持不变, 且最初棋盘上的数为 1 或 -1 , 故若 $0<s<m$ 且 $0<t<n$, 则有 $m_{11}+4=m_{m n}$, 这与 $m_{i j} \in\{-1,1\}, \forall 1 \leq i \leq m, 1 \leq j \leq n$ 矛盾. 故 $s \in\{0, m\}$ 或 $t \in\{0, n\}$. 又 $\min \left\{a_{i}\right\}=\min \left\{b_{j}\right\}=0$, 故有 $s \neq m$ 或者 $t \neq n$, 从而 $s=0$ 或 $t=0$.

1) 当 $s=0$ 时, 此时有 $t m$ 个 $k-2,(n-t) m$ 个 $k$, 故 $r=(n-t) m$, 即 $m \mid r$.
2) 当 $t=0$ 时, 同理有 $n \mid r$.

上面说明了当 $n \nmid r$ 且 $m \nmid r$ 时,满足要求. 下面说明 $n \mid r$ 或 $m \mid r$ 均不满足要求.

若 $m \mid r$, 设 $r=m k$, 则可将 $M$ 的 $k$ 格列都填 1 , 其余列都填 -1 , 此时, 将填 -1 的列都操作 2 次, 各数都变成 1 , 矛盾.

所以 $m \nmid r$. 同理, $n \nmid r$.

综上所述, 所求 $r$ 是一切不为 $m$ 的倍数及 $n$ 的倍数的正整数.

评注 此题是较难的组合题, 约有 $15 \%$ 的同学做对了此题. 解 1 的难点在于,要发现一个 “矩形”，其 4 角方格不全同号, 且存在位于同一对角线的角上方格同号, 由此定义特征函数: $f(M)=\left(a_{i j}+a_{s t}\right)-\left(a_{i t}+a_{s j}\right)$.

解法二利用交换两行或两列不改变最后的结果这一性质, 将 -1 这一特殊的元素”移" 到了方阵的左上方, 再取 $a_{11}$ 和 $a_{m n}$ 这两个特殊元比较后得到结果.事实上, 此时 $a_{m 1}, a_{1 n}$ 相等, 故本质上也是利用了特征函数的想法.

致谢 感谢罗振华老师仔细审阅了此文, 并给出了宝贵的建议.

