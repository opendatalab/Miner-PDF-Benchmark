# 第56届国际数学奥林匹克 

㫿振华

泰国 清迈<br>第一天<br>7月10日 9:00-13:30

1. 我们称平面上一个有限点集 $\mathcal{S}$ 是平衡的, 如果对 $\mathcal{S}$ 中任意两个不同的点 $A, B$, 都存在 $\mathcal{S}$ 中一点 $C$, 满足 $A C=B C$. 我们称 $\mathcal{S}$ 是无中心的, 如果对 $\mathcal{S}$ 中任意三个不同的点 $A, B, C$, 都不存在 $\mathcal{S}$ 中一点 $P$, 满足 $P A=P B=P C$.

(a) 证明: 对每个整数 $n \geqslant 3$, 均存在一个由 $n$ 个点构成的平衡点集.

(b) 确定所有的整数 $n \geqslant 3$, 使得存在一个由 $n$ 个点构成的平衡且无中心的点集.

(荷兰供题)

证明: (a) 对于奇数 $n \geqslant 3$, 考虑正 $n$ 边形的 $n$ 个顶点构成的点集 $\mathcal{S}$, 我们说明 $\mathcal{S}$ 是平衡的. 事实上, $\mathcal{S}$ 中所有点在一圆周 $\omega$ 上. 对于 $\mathcal{S}$ 中任意两个不同点 $A, B$, 点 $A, B$ 分 $\omega$ 为两段圆弧, 其中一段圆弧内部有奇数个 $S$ 中点, 其中一点 $C$ 是这段圆弧的中点, 它满足 $A C=B C$.

对于偶数 $n \geqslant 4$, 考虑如下构图: 设圆 $\omega$ 的圆心为 $O$, 在 $\omega$ 上取非常靠近的 $k=\frac{n}{2}-1$ 个点 $A_{1}, \cdots, A_{k}$, 使得这些点都落在圆心角为 $30^{\circ}$ 的一段圆弧上, 将这 $k$ 个点绕圆心 $O$ 顺时针旋转 $60^{\circ}$, 又得到 $k$ 个点, $B_{1}, \cdots, B_{k}$, 将 $A_{1}$ 绕 $O$ 逆时针旋转 $60^{\circ}$, 得到点 $A^{\prime}$. 令

$$
\mathcal{S}=\left\{O, A_{1}, \cdots, A_{k}, B_{1}, \cdots, B_{k}, A^{\prime}\right\},
$$

则 $\mathcal{S}$ 含有 $n$ 个不同的点. 我们说明 $\mathcal{S}$ 是平衡的. 事实上, 对 $\mathcal{S}$ 中任意两个不同点 $A, B$,若 $A, B$ 都在 $\omega$ 上, 则 $O$ 到 $A, B$ 的距离相等. 若 $A, B$ 之一是 $O$, 则由上述构造方法知, 总存在另一点 $C \in \mathcal{S}$, 使得三角形 $A B C$ 是正三角形, 因此 $C$ 到 $A, B$ 的距离也相等.

(b) 所求 $n$ 为所有大于等于 3 的奇数.

当 $n$ 是大于等于 3 的奇数时, 取 $\mathcal{S}$ 为一个正 $n$ 边形的 $n$ 个顶点所构成的点集, (a)中已经说明 $\mathcal{S}$ 是平衡的. 由于 $\mathcal{S}$ 中任意三个不同点的外心为这个正 $n$ 边形的中心, 它不在 $\mathcal{S}$ 中,因此 $S$ 也是无中心的.

对于大于等于 4 的偶数 $n$, 不存在平衡且无中心的点集. 假设一个 $n$ 个点的集合 $\mathcal{S}$ 是平衡的. 对于 $\mathcal{S}$ 中的任意一个二元子集 $\{A, B\}$, 存在 $\mathcal{S}$ 中一点到 $A, B$ 距离相等, 取定这样一个点, 称为 $\{A, B\}$ 的关联点. $\mathcal{S}$ 的二元子集共有 $C_{n}^{2}$ 个, 每个二元子集均确定一个关联点, 根据抽屉原理, $\mathcal{S}$ 中有一个点 $P$, 它至少是 $\frac{1}{n} C_{n}^{2}=\frac{1}{2}(n-1)$ 个二元子集的关联点.由于 $n$ 是偶数, 故 $P$ 至少是 $\mathcal{S}$ 的 $\frac{n}{2}$ 个二元子集的关联点. 以 $P$ 为关联点的二元子集中的两点均不为 $P$, 这 $\frac{n}{2}$ 个二元子集中的点都是 $\mathcal{S} \backslash\{P\}$ 中的点. 由于 $\frac{n}{2} \times 2=n>n-1$, 其中有两个二元子集有共同元素, 记为 $\{A, B\}$ 和 $\{A, C\}$, 则 $P A=P B=P C$, 从而 $\mathcal{S}$ 不是无中心的.

2. 确定所有三元正整数组 $(a, b, c)$, 使得

$$
a b-c, \quad b c-a, \quad c a-b
$$

中的每个数都是 2 的方幂.

$\left(2\right.$ 的方幂是指形如 $2^{n}$ 的整数, 其中 $n$ 是非负整数)

(塞尔维亚供题)

解: 如果 $a=1$, 那么 $b-c$ 与 $c-b$ 都是 2 的方幕, 这不可能. 于是 $a \geq 2$, 同理 $b \geq 2, c \geq 2$.下面分两种情形.

情形 $1: a, b, c$ 中有两个数相等.

不妨设 $a=b$, 于是 $a c-b=a(c-1)$ 是 2 的方幂, 这表明 $a$ 和 $c-1$ 都是 2 的方幂.设 $a=2^{s}, c=1+2^{t}, s \geq 1, t \geq 0 . a b-c=2^{2 s}-2^{t}-1$ 是 2 的方幂. 若 $t>0$,则 $2^{2 s}-2^{t}-1$ 是奇数, 只可能 $2^{2 s}-2^{t}-1=1$, 模 4 得 $2^{t} \equiv 2(\bmod 4)$, 故 $t=1$, 从而 $s=1$,此时 $a=b=2, c=3$. 若 $t=0$, 则 $2^{2 s}-2$ 是 2 的方幂, 只可能 $s=1$, 此时 $a=b=c=2$.容易验证 $(2,2,2)$ 和 $(2,2,3)$ 都满足要求.

情形 $2: a, b, c$ 互不相同.

不妨设 $2 \leq a<b<c$. 由题意, 存在非负整数 $\alpha, \beta, \gamma$, 使得

$$
\begin{aligned}
& b c-a=2^{\alpha} \\
& a c-b=2^{\beta} \\
& a b-c=2^{\gamma}
\end{aligned}
$$

显然 $\alpha>\beta>\gamma \geq 0$. 对 $a$ 的大小再分两种情形讨论.

情形2.1: $a=2$.

我们先证明 $\gamma=0$. 假如 $\gamma>0$, 由(3)式可知 $c$ 是偶数, 由(2)式可知 $b$ 也是偶数, 这样 $(1)$ 式左边 $b c-a \equiv 2(\bmod 4)$, 但是 $2^{\alpha} \equiv 0(\bmod 4)$, 矛盾.

从而 $\gamma=0,(3)$ 式成为 $c=2 b-1$, 由 (2) 式得到 $3 b-2=2^{\beta}$, 模 3 可知 $\beta$ 是偶数. 若 $\beta=2$,则 $b=2=a$, 不成立. 若 $\beta=4$, 则 $b=6, c=11$, 容易验证 $(a, b, c)=(2,6,11)$ 满足要求.若 $\beta \geq 6$, 则有

$$
b=\frac{1}{3}\left(2^{\beta}+2\right) \text {. }
$$

代入(1)式，

$$
9 \cdot 2^{\alpha}=9(b c-a)=9 b(2 b-1)-18=(3 b-2)(6 b+1)-16=2^{\beta}\left(2^{\beta+1}+5\right)-16 .
$$

由于 $\alpha>\beta \geq 6$, 故 $2^{7} \mid 9 \cdot 2^{\alpha}$, 但是上式右边仅被 $2^{4}$ 整除, 不被 $2^{5}$ 整除, 矛盾.

情形 $2.2: a \geq 3$.

将 $(1),(2)$ 两式相加, 得

$$
(a+b)(c-1)=2^{\alpha}+2^{\beta} \text {. }
$$

将(1), (2)两式相减, 得

$$
(b-a)(c+1)=2^{\alpha}-2^{\beta} \text {. }
$$

由于 $c-1$ 与 $c+1$ 中有一个不是 4 的倍数, 故 $2^{\beta-1} \mid a+b$, 或者 $2^{\beta-1} \mid b-a$. 由

$$
2^{\beta}=a c-b \geq 3 c-b>2 c
$$

可得, $b<c<2^{\beta-1}$, 因此 $0<b-a<2^{\beta-1}$, 故 $2^{\beta-1} \mid b-a$ 不成立, 于是 $2^{\beta-1} \mid a+b$, 且由于 $a+b<2 b<2^{\beta}$, 只能 $a+b=2^{\beta-1}$. 代入 (2)式,

$$
a c-b=2^{\beta}=2(a+b),
$$

即 $a(c-2)=3 b$. 若 $a \geq 4$, 则 $b \geq 5$,

$$
a(c-2) \geq 4(c-2) \geq 4(b-1)>3 b,
$$

矛盾. 故 $a=3, c-2=b$. 因此 $b=2^{\beta-1}-3, c=2^{\beta-1}-1$. 代入(3)式,

$$
2^{\gamma}=a b-c=3\left(2^{\beta-1}-3\right)-\left(2^{\beta-1}-1\right)=2^{\beta}-8,
$$

从而 $\beta=4, b=5, c=7$. 容易验证 $(3,5,7)$ 也满足条件.

综上所述, 满足条件的三元正整数组共有 16 个, 为 $(2,2,2),(2,2,3)$ 的 3 种排列, $(2,6,11)$ 的 6 种排列, 和 $(3,5,7)$ 的 6 种排列.

3. 在锐角三角形 $A B C$ 中, $A B>A C$. 设 $\Gamma$ 是它的外接圆, $H$ 是它的垂心, $F$ 是由顶点 $A$ 处所引高的垂足. $M$ 是边 $B C$ 的中点. $Q$ 是 $\Gamma$ 上一点, 使得 $\angle H Q A=90^{\circ}, K$ 是 $\Gamma$ 上一点, 使得 $\angle H K Q=90^{\circ}$. 已知点 $A, B, C, K, Q$ 互不相同, 且按此顺序排列在 $\Gamma$ 上.

证明: 三角形 $K Q H$ 的外接圆和三角形 $F K M$ 的外接圆相切.

(乌克兰供题)

证明: 如图所示.



延长 $Q H$ 交 $\Gamma$ 于点 $A^{\prime}$, 由于 $\angle A Q H=90^{\circ}$, 从而 $A A^{\prime}$ 是 $\Gamma$ 的直径. 由于 $A^{\prime} B \perp A B$,故 $A^{\prime} B \| C H$, 同理可知 $A^{\prime} C \| B H$, 故 $B A^{\prime} C H$ 是平行四边形, 从而 $M$ 是 $A^{\prime} H$ 的中点. 延长 $A F$ 交 $\Gamma$ 于点 $E$, 由于 $A^{\prime} E \perp A E$, 故 $A^{\prime} E \| B C$, 从而 $M F$ 是三角形 $H A^{\prime} E$ 的中位线, $F$ 是 $H E$ 的中点.
设直线 $A^{\prime} E$ 与 $Q K$ 交于点 $R$. 根据圆幂定理,

$$
R K \cdot R Q=R E \cdot R A^{\prime} .
$$

三角形 $H K Q$ 的外接圆 $\omega_{1}$ 和三角形 $H E A^{\prime}$ 的外接圆 $\omega_{2}$ 分别是以 $H Q$ 和 $H A^{\prime}$ 为直径的圆,这两个圆外切于点 $H$, 而 $R$ 是这两个圆的等幕点, 从而 $R$ 在这两个圆的根轴上, 即 $R H$ 是这两圆的公切线, $R H \perp A^{\prime} Q$.

设直线 $M F$ 交 $H R$ 于点 $S$, 则 $S$ 是 $H R$ 的中点. 由于三角形 $R H K$ 是直角三角形, $S$ 是斜边 $R H$ 的中点, 故 $S H=S K$. 再由 $S H$ 是 $\omega_{1}$ 的切线知, $S K$ 也是 $\omega_{1}$ 的切线. 在直角三角形 $S H M$ 中, $H F$ 是斜边上的高, 从而

$$
S F \cdot S M=S H^{2}=S K^{2},
$$

故 $S K$ 也是三角形 $K M F$ 的外接圆的切线. 于是 $S K$ 与三角形 $K Q H$ 的外接圆和三角形 $F K M$ 的外接圆均相切于点 $K$ 处, 因此这两个圆也在点 $K$ 处相切.

$$
\text { 第二天 }
$$

7月11日 9:00-13:30

4. 在三角形 $A B C$ 中, $\Omega$ 是其外接圆, $O$ 是其外心. 以 $A$ 为圆心的一个圆 $\Gamma$ 与线段 $B C$ 交于两点 $D$ 和 $E$, 使得点 $B, D, E, C$ 互不相同, 并且按此顺序排列在直线 $B C$ 上. 设 $F$ 和 $G$ 是圆 $\Gamma$ 和 $\Omega$ 的两个交点, 并且使得点 $A, F, B, C, G$ 按此顺序排列在 $\Omega$ 上. 设 $K$ 是三角形 $B D F$ 的外接圆和线段 $A B$ 的另一个交点. 设 $L$ 是三角形 $C G E$ 的外接圆和线段 $C A$ 的另一个交点.

假设直线 $F K$ 和 $G L$ 不相同, 且相交于点 $X$. 证明: $X$ 在直线 $A O$ 上.

(希腊供题)

证明: 如图所示.



由于 $A F=A G$, 而 $A O$ 是 $\angle F A G$ 的内角平分线, 故 $F, G$ 关于直线 $A O$ 对称. 要证明点 $X$ 在直线 $A O$ 上, 只需证明

$$
\angle A F K=\angle A G L
$$

首先

$$
\angle A F K=\angle D F G+\angle G F A-\angle D F K .
$$

由 $D, F, G, E$ 共圆, 有 $\angle D F G=\angle C E G$. 由 $A, F, B, G$ 共圆, 有 $\angle G F A=\angle G B A$. 由 $D$, $B, F, K$ 共圆, 有 $\angle D F K=\angle D B K$. 从而

$$
\angle A F K=\angle C E G+\angle G B A-\angle D B K=\angle C E G-\angle C B G .
$$

再由 $C, E, L, G$ 共圆, 得 $\angle C E G=\angle C L G$. 由 $C, B, A, G$ 共圆, 有 $\angle C B G=\angle C A G$. 故

$$
\angle A F K=\angle C L G-\angle C A G=\angle A G L .
$$

结论获证.

5. 设 $\mathbb{R}$ 是全体实数的集合. 求所有的函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 满足对任意实数 $x, y$, 都有

$$
f(x+f(x+y))+f(x y)=x+f(x+y)+y f(x) .
$$

(阿尔巴尼亚供题)

解: 将题中等式记为 $P(x, y)$. 设 $f$ 是满足条件的一个函数. 考察 $P(x, 1)$, 有

$$
f(x+f(x+1))=x+f(x+1)
$$

于是对任意实数 $x, x+f(x+1)$ 都是 $f$ 的不动点. 下面分两种情况讨论.

情形 $1: f(0) \neq 0$.

考察 $P(0, y)$, 有

$$
f(f(y))+f(0)=f(y)+y f(0) .
$$

若 $y_{0}$ 是 $f$ 的不动点, 在上式中令 $y=y_{0}$, 可得 $y_{0}=1$. 于是,

$$
x+f(x+1)=1 \text {, }
$$

从而 $f(x)=2-x$ 对所有实数 $x$ 成立. 容易验证 $f(x)=2-x$ 是满足条件的函数.

情形 $2: f(0)=0$.

考察 $P(x+1,0)$, 有

$$
f(x+f(x+1)+1)=x+f(x+1)+1 .
$$

考察 $P(1, y)$, 有

$$
f(1+f(y+1))+f(y)=1+f(y+1)+y f(1) \text {. }
$$

在 $(1)$ 式中令 $x=-1$, 有 $f(-1)=-1$. 再在 $(3)$ 式中令 $y=-1$, 有 $f(1)=1$. 于是 $(3)$ 式可以改写为

$$
f(1+f(y+1))+f(y)=1+f(y+1)+y \text {. }
$$

如果 $y_{0}$ 和 $y_{0}+1$ 都是 $f$ 的不动点, 在 $(4)$ 式中令 $y=y_{0}$ 即知, $y_{0}+2$ 也是 $f$ 的不动点. 故由(1), (2)式可知, 对任意实数 $x, x+f(x+1)+2$ 都是 $f$ 的不动点, 即

$$
f(x+f(x+1)+2)=x+f(x+1)+2 .
$$

在上式中将 $x$ 用 $x-2$ 代替, 得

$$
f(x+f(x-1))=x+f(x-1) \text {. }
$$

考察 $P(x,-1)$, 有

$$
f(x+f(x-1))=x+f(x-1)-f(x)-f(-x) .
$$

从上面两式可知 $f(-x)=-f(x)$, 即 $f$ 是奇函数. 考察 $P(-1,-y)$, 并利用 $f(-1)=-1$,有

$$
f(-1+f(-y-1))+f(y)=-1+f(-y-1)+y
$$

再由 $f$ 是奇函数, 上式可改写为

$$
-f(1+f(y+1))+f(y)=-1-f(y+1)+y .
$$

将上式与 (4) 式相加, 可知 $f(y)=y$ 对所有实数 $y$ 成立. 容易验证 $f(x)=x$ 是满足条件的函数.

综上所述, 满足条件的函数一共两个, $f(x)=x$ 和 $f(x)=2-x$.

6. 整数序列 $a_{1}, a_{2}, \cdots$ 满足下列条件:

(i) 对每个整数 $j \geqslant 1$, 有 $1 \leqslant a_{j} \leqslant 2015$;

(ii) 对任意整数 $1 \leqslant k<\ell$, 有 $k+a_{k} \neq \ell+a_{\ell}$.

证明: 存在两个正整数 $b$ 和 $N$, 使得

$$
\left|\sum_{j=m+1}^{n}\left(a_{j}-b\right)\right| \leqslant 1007^{2}
$$

对所有满足 $n>m \geqslant N$ 的整数 $m$ 和 $n$ 均成立.

(澳大利亚供题)

证明: 设 $s_{n}=n+a_{n}$. 由条件可知, $n+1 \leqslant s_{n} \leqslant n+2015$, 且 $s_{1}, s_{2}, \cdots$ 互不相同.记 $S=\left\{s_{1}, s_{2}, \cdots\right\}$. 我们首先说明集合 $M=\mathbb{N}^{*} \backslash S$ 是有限集, 且 $1 \leqslant|M| \leqslant 2015$.

显然 $1 \in M$. 若 $M$ 中有多于 2015 个元素, 设 $m_{1}<m_{2}<\cdots<m_{2016}$ 都属于 $M$, 取一整数 $n>m_{2016}$. 那么

$$
\begin{gathered}
\left\{s_{1}, s_{2}, \cdots, s_{n}\right\} \subset\{1,2, \cdots, n+2015\}, \\
\left\{m_{1}, m_{2}, \cdots, m_{2016}\right\} \subset\{1,2, \cdots, n+2015\}
\end{gathered}
$$

由 $M$ 的定义, $\left\{s_{1}, s_{2}, \cdots, s_{n}\right\}$ 与 $\left\{m_{1}, m_{2}, \cdots, m_{2016}\right\}$ 不相交, 而 $n+2016>n+2015$, 矛盾. 因此 $M$ 是有限集, 且 $1 \leqslant|M| \leqslant 2015$.

令 $b=|M|$, 任取整数 $N>\max M$, 下面证明这样选取的 $b$ 和 $N$ 满足要求.

显然 $b, N$ 都是正整数, 且前面证明了 $1 \leqslant b \leqslant 2015$. 对任意整数 $n \geqslant N$, 有如下分拆

$$
\{1,2, \cdots, n+2015\}=\left\{s_{1}, s_{2}, \cdots, s_{n}\right\} \cup M \cup C_{n} \text {, }
$$

前面已经说明 $\left\{s_{1}, s_{2}, \cdots, s_{n}\right\}$ 和 $M$ 是 $\{1,2, \cdots, n+2015\}$ 的两个不相交的子集, 设 $C_{n}$ 为剩余部分, $\left|C_{n}\right|=2015-b$. 对 $j \geqslant n+1, s_{j}=j+a_{j} \geqslant n+1+1=n+2$. 若 $C_{n}$ 不是空集, 一定有 $n+2 \leqslant \min C_{n}$, 否则 $\min C_{n}$ 不在 $S$ 中, 也不在 $M$ 中, 矛盾. 于是

$$
C_{n} \subseteq\{n+2, n+3, \cdots, n+2015\}
$$

这对 $C_{n}$ 是空集(即 $b=2015$ )自然也成立. 计算(1)式两边的所有元素之和, 用 $\sigma(X)$ 表示有限集合 $X$ 的所有元素之和, 有

$$
\sum_{i=1}^{n+2015} i=\sum_{j=1}^{n} s_{j}+\sigma(M)+\sigma\left(C_{n}\right)
$$

再将 $s_{j}=j+a_{j}$ 代入化简, 有

$$
\sum_{i=n+1}^{n+2015} i=\sum_{j=1}^{n} a_{j}+\sigma(M)+\sigma\left(C_{n}\right)
$$

对任意 $n>m \geqslant N$, 在上式中用 $m$ 代替 $n$, 并将两式作差, 得

$$
\sum_{i=n+1}^{n+2015} i-\sum_{i=m+1}^{m+2015} i=\sum_{j=m+1}^{n} a_{j}+\sigma\left(C_{n}\right)-\sigma\left(C_{m}\right)
$$

两边减去 $(n-m) b$, 并化简得

$$
\sum_{j=m+1}^{n}\left(a_{j}-b\right)=(2015-b)(n-m)+\sigma\left(C_{m}\right)-\sigma\left(C_{n}\right)
$$

由(2)以及 $\left|C_{n}\right|=2015-b$ 可知，

$$
\sum_{i=n+2}^{n+2016-b} i \leqslant \sigma\left(C_{n}\right) \leqslant \sum_{i=n+b+1}^{n+2015} i
$$

即

$$
\left(n+1009-\frac{b}{2}\right)(2015-b) \leqslant \sigma\left(C_{n}\right) \leqslant\left(n+1008+\frac{b}{2}\right)(2015-b) .
$$

上述不等式将 $n$ 换成 $m$ 也成立. 回到(3)式, 利用上面的不等式估计 $\sigma\left(C_{n}\right)$ 和 $\sigma\left(C_{m}\right)$ 的上下界, 有

$$
\begin{gathered}
\sum_{j=m+1}^{n}\left(a_{j}-b\right) \leqslant(2015-b)(n-m)+\left(m+1008+\frac{b}{2}\right)(2015-b) \\
-\left(n+1009-\frac{b}{2}\right)(2015-b)=(2015-b)(b-1) \leqslant 1007^{2}
\end{gathered}
$$

以及

$$
\begin{gathered}
\sum_{j=m+1}^{n}\left(a_{j}-b\right) \geqslant(2015-b)(n-m)+\left(m+1009-\frac{b}{2}\right)(2015-b) \\
-\left(n+1008+\frac{b}{2}\right)(2015-b)=-(2015-b)(b-1) \geqslant-1007^{2}
\end{gathered}
$$

结合这两个不等式, 就有

$$
\left|\sum_{j=m+1}^{n}\left(a_{j}-b\right)\right| \leqslant 1007^{2} .
$$

结论获证.

