# 数学新星问题征解第十一期解答 

2016.03

第一题. 对于 $n, k \in \mathbb{N}^{*}$, 若 $n$ 个实数 $x_{1}, x_{2}, \cdots, x_{n}$ 的和为整数, 求

$$
\min _{1 \leq i \leq n}\left(\left\{x_{i}+x_{i+1}+\cdots+x_{i+k-1}\right\}\right)
$$

的最大值. 其中 $\{x\}$ 表示 $x$ 的小数部分, $x_{n+i}=x_{i}, i=1,2, \cdots$.

(四川省绵阳中学学生 刘俊松 供题)

## 解 (根据人大附中欧阳明晖同学和长沙一中胡冬础同学的解答整理):

所求最大值为 $1-\frac{(n, k)}{n}$.

设 $(n, k)=d$, 并记 $k=k_{1} d, n=n_{1} d,\left(k_{1}, n_{1}\right)=1$, 由于 $x_{1}+x_{2}+\cdots+x_{n}$ 是整数, 则

$$
\begin{aligned}
& \left(x_{1}+x_{2}+\cdots+x_{k}\right)+\left(x_{k+1}+\cdots+x_{2 k}\right)+\cdots+\left(x_{k_{1} n-k+1}+\cdots+x_{k_{1} n}\right) \\
= & \left(x_{1}+x_{2}+\cdots+x_{n}\right)+\left(x_{n+1}+\cdots+x_{2 n}\right)+\cdots+\left(x_{k_{1} n-n+1}+\cdots+x_{k_{1} n}\right) \\
= & k_{1}\left(x_{1}+x_{2}+\cdots+x_{n}\right)
\end{aligned}
$$

也是整数. 令

$$
S=\left\{x_{1}+\cdots+x_{k}\right\}+\left\{x_{k+1}+\cdots+x_{2 k}\right\}+\cdots+\left\{x_{k_{1} n-k+1}+\cdots+x_{k_{1} n}\right\},
$$

(1) 与 (2) 作差, 得

$$
\left[x_{1}+\cdots+x_{k}\right]+\left[x_{k+1}+\cdots+x_{2 k}\right]+\cdots+\left[x_{k_{1} n-k+1}+\cdots+x_{k_{1} n}\right]
$$

这是一个整数, 则 $S$ 为整数. 由于 (2) 中共有 $\frac{k_{1} n}{k}=\frac{k_{1} n_{1} d}{k_{1} d}=n_{1}$ 个小数, 则 $S \leq n_{1}-1$. 从而存在 $0 \leq i \leq n_{1}-1$, 使得

$$
x_{i k+1}+x_{i k+2}+\cdots+x_{(i+1) k} \leq \frac{S}{n_{1}} \leq \frac{n_{1}-1}{n_{1}} .
$$

因此

$$
\min _{1 \leq i \leq n}\left(\left\{x_{i}+x_{i+1}+\cdots+x_{i+k-1}\right\}\right) \leq \frac{n_{1}-1}{n_{1}}
$$

下面说明 $\frac{n_{1}-1}{n_{1}}$ 可达.

取 $x_{i}=\frac{m}{k_{1} n}(i=1,2, \cdots, n)$, 其中 $m$ 满足:

$$
m \equiv-1 \quad\left(\bmod n_{1}\right), \quad m \equiv 0 \quad\left(\bmod k_{1}\right)
$$

则 $x_{1}+x_{2}+\cdots+x_{n}=\frac{m n}{k_{1} n}=\frac{m}{k_{1}} \in \mathbf{Z}$, 且对任意 $1 \leq i \leq n$,

$$
x_{i}+x_{i+1}+\cdots+x_{i+k-1}=\frac{m k}{k_{1} n}=\frac{m k_{1} d}{k_{1} n_{1} d}=\frac{m}{n_{1}}
$$

因此

$$
\left\{x_{i}+x_{i+1}+\cdots+x_{i+k-1}\right\}=\left\{\frac{m}{n_{1}}\right\}=\frac{n_{1}-1}{n_{1}} .
$$

综上, 所求最大值为 $\frac{n_{1}-1}{n_{1}}=1-\frac{d}{n}=1-\frac{(n, k)}{n}$.

评注 东北师大附中孙伟舰同学、湖南师大附中刘奕然、李颖杰同学、湖南省雅礼中学江朗、尹龙晖、谢天乐、肖尧、王文瑞、刘恺睿、段剑儒、陈钦品、邱添、刘哲成等同学也给出了本题的正确解答.

第二题. 如图 $1, \odot I$ 是 $\triangle A B C$ 的内切圆, 过 $B, C$的圆 $\odot u$ 与 $\odot I$ 相切, 且分别交 $A B, A C$ 于 $S, T$. 点 $M, N$ 是 $\overparen{B C}, \overparen{C T}$ (均不含点 $S$ ) 的中点, $I_{1}$ 是 $\triangle S T C$ 的内心, $Q$ 在 $\odot u$ 上且 $\odot(Q A C)$ 与 $\odot I$ 相切, $M N$ 交 $C Q$于 $G$. 求证: $I_{1} G / / A C$.

(浙江省象山县第三中学学生 黄子宸 供题)

## 证明 (根据供题者解答整理):



图 1

我们首先证明两个引理.

引理 1. 已知 $\triangle A B C$ 内切圆 $\odot I$ 切 $B C$ 于 $D, \odot u$ 过 $B, C$ 切 $\odot I$ 于 $K, R$ 是 $\triangle A B C$ 的 $A$-旁心, 则 $K, D, R$ 共线.

引理 1 证明 如图 2 , 连接 $K C$ 交 $D E, \odot I$ 于 $T, H$,连接 $K B$ 交 $D F, \odot I$ 于 $S, G$.

由于 $K$ 是 $\odot I, \odot u$ 的位似中心, $G, B, H, C$ 位似对应点, 故 $G H / / B C$, 因此

$$
\frac{B K}{B G}=\frac{C K}{C H}
$$

而 $B D, B F$ 是切线, 故 $D K F G$ 是调和四边形, 即 $B, G, S, K$ 是调和点列. 所以

$$
\frac{B K}{B G}=\frac{S K}{S G}
$$

同理,

$$
\frac{C K}{C H}=\frac{T K}{T H}
$$



图 2
由 (1), (2), (3) 得 $\frac{S K}{S G}=\frac{T K}{T H}$, 即 $S T / / G H / / B C$.

而 $\angle F D B=90^{\circ}-\angle I B C=\angle R B C$, 从而 $D S / / B R$, 同理 $D T / / C R$.

因此 $\triangle D S T, \triangle R B C$ 位似, 则 $B S, R D, C T$ 共点. 故 $K, D, R$ 共线. 引理 1 得证.

引理 2. $\odot I$ 是 $\triangle A B C$ 内切圆, $\odot(B K C), \odot(A J C)$ 均与 $\odot I$ 相切且交于 $Q$,则 $C Q$ 过 $\triangle A B C$ 内切圆切点三角形和 $\triangle A B C$ 旁心三角形的位似中心 $X$.



图 3

引理 2 证明 如图 3, 设 $A, B, C$ 所对内切圆切点为 $D, E, F, A, B, C$ 所对旁心为 $I_{1}, I_{2}, I_{3}$. 过 $K$ 作 $\odot I$ 切线交 $A C$ 于 $M$, 过 $J$ 作 $\odot I$ 切线交 $B C, M K$ 于 $N, S$.

由于 $M K$ 是 $\odot I, \odot u$ 的根轴, $N J$ 是 $\odot I, \odot v$ 的根轴, $C Q$ 是 $\odot u, \odot v$ 的根轴, 根据根心定理知, $M K, N J, C Q$ 共点于 $S$, 即 $S, Q, C$ 共线.

此时, 对于圆外切四边形 $M S N C$ 应用牛顿定理 (圆的外切四边形的对角线的交点和以切点为顶点的四边形对角线交点重合), 得 $K D, J E, C S, M N$ 共点.结合引理 1, 即得 $I_{1} D K, I_{2} E J, C Q S$ 共点. 而由熟知结论, $I_{1} D, I_{2} E, I_{3} F$ 共点于 $\triangle D E F, \triangle I_{1} I_{2} I_{3}$ 的位似中心 $X$. 因此, $X$ 在直线 $C Q S$ 上. 引理 2 得证.

回到原题. 取 $\triangle A B C$ 的三个旁心 $I_{A}, I_{B}, I_{C}$, 取 $\triangle B C T$ 的内心 $L$, 过 $I_{1}$ 作 $A C$ 的平行线交 $D E$ 于 $X$. 其他辅助线连接如图 4 所示.

由曼海姆定理得 $D, L, E$ 共线, 且 $L$ 为 $D E$ 的中点. 又由沢山定理知, $\triangle C S T$ 的内心在 $E F$ 上. 显然 $B, L, N$ 共线, $S, I_{1}, N$ 共线, 由鸡爪定理, $N T=$ $N I_{1}=N C=N L$. 所以 $T, I_{1}, L, C$ 共圆, 圆心是 $N$. 从而

$$
\angle E L I_{1}=180^{\circ}-\angle E L C-\angle I_{1} T E=90^{\circ}-\frac{1}{2} \angle S T C
$$

$$
=\frac{1}{2} \angle A T S=\frac{1}{2} \angle A B C=90^{\circ}-\angle D E F,
$$

即 $L I_{1} \perp E F$.

取 $\triangle D E F, \triangle I_{A} I_{B} I_{C}$ 的位似中心 $W$, 由引理 2 知, $W$ 在 $C Q$ 上. 又 $F, I_{C}, J, C$ 为 $\triangle D E F, \triangle I_{A} I_{B} I_{C}$ 的位似对应点, 所以 $F J / / C I_{C}$, 而 $C I_{C} \perp D E$,因此 $F J / / C I_{C}, F J \perp D E$. 从而 $\triangle E I_{1} L \sim \triangle E J F$, 因此 $E I_{1} \cdot E F=E J \cdot E L$.

又 $\angle X I_{1} E=\angle A E F=\angle E D F$, 得 $\triangle E I_{1} X \sim \triangle E D F$, 故 $E I_{1} \cdot E F=$ $E X \cdot E D$.

因此 $E J \cdot E L=E X \cdot E D$. 而 $E D=2 E L$, 因此 $E J=2 E X$, 即 $X$ 是 $E J$的中点.

注意到 $B, L, N ; T, L, M$ 分别共线, 由鸡爪定理, $N C=N L=N T, M C=$ $M L=M B$. 所以 $M N$ 是 $C L$ 的中垂线, 结合 $C L$ 是 $D E$ 的中垂线, 得 $M N$ 是 $\triangle C D E$ 的中位线. 因此 $G$ 是 $C J$ 的中点.

故 $X G / / A C$,而 $I_{1} X / / A C$, 所以 $I_{1}, X, G$ 共线且 $I_{1} X G / / A C$.



图 4

评注 东北师大附中孙伟舰同学也给出了本题的正确解答.
第三题. 已知 $0<a_{1} \leq a_{2} \leq \cdots \leq a_{n}, b_{1} \geq b_{2} \geq \cdots \geq b_{n}>0$ 且 $\frac{a_{i+1}}{a_{i}} \leq \frac{b_{i}}{b_{i+1}}$.证明

$$
\frac{A_{n}(a)}{G_{n}(a)} \leq\left(\frac{A_{n}(b)}{G_{n}(b)}\right)^{n-1} .
$$

其中 $A_{n}(a), G_{n}(a)$ 分别表示 $a_{1}, \cdots, a_{n}$ 的算术平均值和几何平均值, $A_{n}(b), G_{n}(b)$分别表示 $b_{1}, b_{2}, \cdots, b_{n}$ 的算术平均值和几何平均值.

(辽宁省实验中学 赵斌 供题)

## 证明 (根据吉大附中于翔宇同学的解答整理):

事实上, 我们可以由 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}, \quad a_{1} b_{1} \geq a_{2} b_{2} \geq \cdots \geq a_{n} b_{n}$ 推得

$$
\frac{A_{n}(a)}{G_{n}(a)} \leq \frac{A_{n}(c)}{G_{n}(c)}
$$

其中 $A_{n}(c), G_{n}(c)$ 分别表示 $c_{i}=\frac{1}{b_{i}}, i=1,2, \cdots, n$ 的算术平均值和几何平均值.

对 $n \geq 2$ 归纳证明. 当 $n=2$ 时, (1) 式为

$$
\frac{a_{1}+a_{2}}{2 \sqrt{a_{1} a_{2}}} \leq \frac{b_{1}+b_{2}}{2 \sqrt{b_{1} b_{2}}}
$$

即需证

$$
\frac{a_{2}}{a_{1}}+\frac{a_{1}}{a_{2}} \leq \frac{b_{2}}{b_{1}}+\frac{b_{1}}{b_{2}}
$$

而这由 $1 \leq \frac{a_{2}}{a_{1}} \leq \frac{b_{1}}{b_{2}}$ 及函数 $f(x)=x+\frac{1}{x}$ 在 $(1, \infty)$ 上单调递增即得.

假设 $n$ 时结论成立, 记 $u_{n}=n A_{n}, v_{n}=G_{n}^{n}$, 则

$$
\frac{u_{n}^{n}}{v_{n}} \leq \frac{\left(c_{1}+\cdots+c_{n}\right)^{n}}{c_{1} \cdots c_{n}}
$$

当 $n+1$ 时, 需证

$$
\frac{u_{n+1}^{n+1}}{v_{n+1}} \leq \frac{\left(c_{1}+\cdots+c_{n+1}\right)^{n+1}}{c_{1} \cdots c_{n+1}}
$$

而由归纳假设，

$$
\begin{aligned}
\frac{u_{n+1}^{n+1}}{v_{n+1}} & =\frac{1}{v_{n}} \cdot \frac{\left(u_{n}+a_{n+1}\right)^{n+1}}{a_{n+1}} \\
& \leq \frac{\left(u_{n}+a_{n+1}\right)^{n+1}}{u_{n}^{n} a_{n+1}} \cdot \frac{\left(c_{1}+\cdots+c_{n}\right)^{n}}{c_{1} \cdots c_{n}} \\
& =\frac{\left(\frac{u_{n}}{a_{n+1}}+1\right)^{n+1}}{\left(\frac{u_{n}}{a_{n+1}}\right)^{n}} \cdot \frac{\left(c_{1}+\cdots+c_{n}\right)^{n}}{c_{1} \cdots c_{n}} .
\end{aligned}
$$

注意到 $\frac{u_{n}}{a_{n+1}} \leq n$ 且函数 $f(x)=\ln \frac{(x+1)^{n+1}}{x^{n}}$ 当 $0<x<n$ 时的导数

$$
f^{\prime}(x)=\frac{n+1}{x+1}-\frac{n}{x}=\frac{x-n}{x(x+1)} \leq 0,
$$

则函数 $g(x)=\frac{(x+1)^{n+1}}{x^{n}}$ 在 $0<x<n$ 上是减函数.
又注意到 $\frac{a_{i+1}}{a_{i}} \leq \frac{c_{i+1}}{c_{i}}, i=1,2, \cdots, n-1$, 则

$$
\frac{u_{n}}{a_{n+1}}=\frac{a_{1}+\cdots+a_{n}}{a_{n+1}} \geq \frac{c_{1}+\cdots+c_{n}}{c_{n+1}}
$$

由 (3) 式及函数 $g(x)$ 的单调性, 得

$$
\begin{aligned}
\frac{u_{n+1}^{n+1}}{v_{n+1}} & \leq \frac{\left(\frac{u_{n}}{a_{n+1}}+1\right)^{n+1}}{\left(\frac{u_{n}}{a_{n+1}}\right)^{n}} \cdot \frac{\left(c_{1}+\cdots+c_{n}\right)^{n}}{c_{1} \cdots c_{n}} \\
& \leq \frac{\left(\frac{c_{1}+\cdots+c_{n}}{c_{n+1}}+1\right)^{n+1}}{\left(\frac{c_{1}+\cdots+c_{n}}{c_{n+1}}\right)^{n}} \cdot \frac{\left(c_{1}+\cdots+c_{n}\right)^{n}}{c_{1} \cdots c_{n}} \\
& =\frac{\left(c_{1}+\cdots+c_{n+1}\right)^{n+1}}{c_{1} \cdots c_{n+1}} .
\end{aligned}
$$

故 (2) 式成立. 进而 (1) 式对所有 $n \geq 2$ 都成立.

最后由 $(2)$ 式及 Maclaurin 不等式, 得

$$
\begin{aligned}
\frac{A_{n}(a)}{G_{n}(a)} & =\frac{a_{1}+\cdots+a_{n}}{n\left(a_{1} \cdots a_{n}\right)^{\frac{1}{n}}} \leq \frac{\frac{1}{b_{1}}+\cdots+\frac{1}{b_{n}}}{n\left(\frac{1}{b_{1}} \cdots \frac{1}{b_{n}}\right)^{\frac{1}{n}}} \\
& =\frac{1}{n}\left(\sum_{i=1}^{n}\left(\prod_{j \neq i} b_{j}\right)\right)\left(\prod_{i=1}^{n} b_{i}\right)^{-\frac{n-1}{n}} \\
& \leq\left(\frac{1}{n} \sum_{i=1}^{n} b_{i}\right)^{n-1}\left(\prod_{i=1}^{n} b_{i}\right)^{-\frac{n-1}{n}} \\
& =\left(\frac{b_{1}+\cdots+b_{n}}{n\left(b_{1} \cdots b_{n}\right)^{\frac{1}{n}}}\right)^{n-1} \\
& =\left(\frac{A_{n}(b)}{G_{n}(b)}\right)^{n-1} .
\end{aligned}
$$

证毕.

评注 东北师大附中孙伟舰、湖南省雅礼中学江朗、湖南师大附中刘俊文同学也给出了本题的正确解答.

第四题. 设 $f(x)=x^{3}+a x+b$ 是一个首一整系数多项式, 且 $4 a^{3}+27 b^{2} \neq 0$.证明: 存在无穷多个正整数 $n$ 满足 $f(n)$ 没有平方因子.

(首都师范大学数学系 梁志斌 供题)

评注 本题无人提供解答. 供题人的解答, 由湖南雅礼中学江朗同学指出其中纰漏，目前暂未完整修正。

