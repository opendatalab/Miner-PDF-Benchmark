# 第一届 USEMO 试题解析 

## 邹明轩

(中国人民大学附属中学, 100080)

指导教师: 张端阳

USEMO (US Ersatz Math Olympiad) 是一项新的赛事, 它在 AoPS 网站上举行, 面向美国所有的中学生, 试题难度和 IMO 接近.

第一届比赛在 2020 年 5 月 23 日至 24 日进行, 有约 240 名学生参加. 第二届比赛将于 2020 年秋天进行.

本文给出第一届比赛试题的解析和简评. 总体而言, 题目新颖有趣, 难度得当. 其中第一题和第四题是高中联赛难度, 第二题、第五题和第六题是冬令营中档题难度, 第三题是冬令营难题难度. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 如图, $A B C D$ 是圆内接四边形. 过点 $B, D$ 作圆 $O$, 圆 $O$ 与直线 $B A, B C$分别交于不同于 $A, B, C$ 的点 $E, F$. 设 $H$ 是 $\triangle D E F$ 的垂心. 证明：如果 $A C, D O, E F$ 交于一点, 那么 $\triangle A B C \sim \triangle E H F$.



修订日期: 2020-07-06.

2. 设 $\mathbb{Z}[x]$ 是所有整系数多项式构成的集合. 求所有的映射 $\theta: \mathbb{Z}[x] \rightarrow \mathbb{Z}[x]$,使得

(1) 对任意 $p, q \in \mathbb{Z}[x], \theta(p+q)=\theta(p)+\theta(q)$ ；

(2) 对任意 $p \in \mathbb{Z}[x], p$ 有整数根当且仅当 $\theta(p)$ 有整数根.

3. 设 $G$ 是无限大的单位正方形网格. “棋盘多边形” 是指边沿着 $G$ 中网格线的不自交的多边形. 甲选择一个棋盘多边形 $F$, 乙的任务是将 $G$ 中某些方格染成绿色, 使得所有和 $F$ 全等的棋盘多边形中都至少有 1 个格、至多有 2020 个格是绿色的. 问:甲能否选择一个 $F$ 使乙无法完成任务?
4. 证明: 对任意素数 $p$, 存在正整数 $n$, 使得

$$
1^{n}+2^{n-1}+3^{n-2}+\cdots+n^{1} \equiv 2020 \quad(\bmod p)
$$

5. 设 $\mathcal{P}$ 是一个正多边形, $\mathcal{V}$ 是其顶点集. 将 $\mathcal{V}$ 中的每个点染成红、白、蓝三色之一. $\mathcal{V}$ 的一个子集称为 “爱国的”，如果它包含每种颜色的点的个数相同. $\mathcal{P}$ 的一条边称为 “耀眼的” , 如果它的两个端点的颜色不同. 已知 $\mathcal{V}$ 是爱国的且 $\mathcal{P}$ 有偶数条耀眼的边, 证明: 存在一条不经过 $\mathcal{V}$ 中点的直线, 将 $\mathcal{V}$ 划分成两个非空的爱国的子集.
6. 如图, 在不等边锐角 $\triangle A B C$ 中, $O$ 是外心, $A D, B E, C F$ 是高. $X, Y, Z$分别是 $A D, B E, C F$ 的中点, $A D$ 与 $Y Z$ 交于点 $P, B E$ 与 $Z X$ 交于点 $Q, C F$与 $X Y$ 交于点 $R$. 设 $Y Z$ 与 $B C$ 交于点 $A^{\prime}, Q R$ 与 $E F$ 交于点 $D^{\prime}$. 证明:过 $A, B, C, O$ 且分别垂直于 $Q R, R P, P Q, A^{\prime} D^{\prime}$ 的直线交于一点.



## II . 解答与评注

1. 如图, $A B C D$ 是圆内接四边形. 过点 $B, D$ 作圆 $O$, 圆 $O$ 与直线 $B A, B C$分别交于不同于 $A, B, C$ 的点 $E, F$. 设 $H$ 是 $\triangle D E F$ 的垂心. 证明: 如果
$A C, D O, E F$ 交于一点, 那么 $\triangle A B C \sim \triangle E H F$.



证明 设 $A C, D O, E F$ 交于点 $G$.

注意到 $D$ 是完全四边形 $A B C F G E$ 的密克点, 所以 $A, E, G, D$ 四点共圆.

这样,

$$
\angle G A E=\angle G D E=\angle O D E=90^{\circ}-\angle D B E
$$

即

$$
\angle C A B=90^{\circ}-\angle D B A,
$$

于是 $A C \perp B D$.

因此

$$
\angle H F E=90^{\circ}-\angle D E F=90^{\circ}-\angle D A G=90^{\circ}-\angle D B C=\angle B C A .
$$

同理, $\angle H E F=\angle B A C$. 故 $\triangle A B C \sim \triangle E H F$.

评注 本题一是要将条件中三线所共的点设出, 二是要注意到 $D$ 是完全四边形的密克点, 之后的导角是容易的.

2. 设 $\mathbb{Z}[x]$ 是所有整系数多项式构成的集合. 求所有的映射 $\theta: \mathbb{Z}[x] \rightarrow \mathbb{Z}[x]$,使得

(1) 对任意 $p, q \in \mathbb{Z}[x], \theta(p+q)=\theta(p)+\theta(q)$;

(2) 对任意 $p \in \mathbb{Z}[x], p$ 有整数根当且仅当 $\theta(p)$ 有整数根.

解 因为当 $P(x)=\sum_{i=0}^{n} a_{i} x^{i}$, 其中 $a_{0}, a_{1}, \cdots, a_{n} \in \mathbb{Z}$ 时, 由 (1),

$$
\theta(P)=\sum_{i=0}^{n} \theta\left(a_{i} x^{i}\right)=\sum_{i=0}^{n} a_{i} \theta\left(x^{i}\right)
$$

所以只需对每个正整数 $n$, 确定 $\theta\left(x^{n}\right)$.

先证明存在 $R_{n} \in \mathbb{Q}[x]$, 使得

$$
\theta\left(x^{n}\right)=\theta(1) R_{n}(x) .
$$

事实上, 对任意整数 $k$, 因为 $x^{n}-k^{n}$ 有整数根, 所以

$$
\theta\left(x^{n}-k^{n}\right)=\theta\left(x^{n}\right)-k^{n} \theta(1)
$$

有整数根, 设为 $z_{k}$. 由 $(2), \theta(1)$ 没有整数根, 于是 $[\theta(1)]\left(z_{k}\right) \neq 0$, 所以至多有两个 $k\left( \pm \sqrt[n]{\frac{\left[\theta\left(x^{n}\right)\right]\left(z_{k}\right)}{[\theta(1)]\left(z_{k}\right)}}\right)$ 对应同一个 $z_{k}$. 因此由 $k$ 有无穷多个, 知 $z_{k}$ 有无穷多个.

取正整数 $K$, 使得存在 $Q(x), R(x) \in \mathbb{Z}[x]$, 满足 $K \theta\left(x^{n}\right)=Q(x) \theta(1)+R(x)$且 $\operatorname{deg} R<\operatorname{deg} \theta(1)$.

由

$$
\left[\theta\left(x^{n}\right)\right]\left(z_{k}\right)-k^{n}[\theta(1)]\left(z_{k}\right)=0
$$

知

$$
[\theta(1)]\left(z_{k}\right) \mid K\left[\theta\left(x^{n}\right)\right]\left(z_{k}\right),
$$

于是

$$
[\theta(1)]\left(z_{k}\right) \mid R\left(z_{k}\right)
$$

因为 $\operatorname{deg} R<\operatorname{deg} \theta(1)$, 所以当 $\left|z_{k}\right|$ 充分大时, $\left|R\left(z_{k}\right)\right|<\left|[\theta(1)]\left(z_{k}\right)\right|$. 故 $R\left(z_{k}\right)=0$对无穷多个 $z_{k}$ 成立, 从而 $R(x)=0$, 命题得证.

这样, 由 $(*)$,

$$
\theta(P)=\sum_{i=0}^{n} a_{i} \theta(1) R_{n}(x)=\theta(1) \sum_{i=0}^{n} a_{i} R_{n}(x)=\theta(1) R_{P}(x)
$$

其中 $R_{P} \in \mathbb{Q}[x]$.

下用 $\{P(n)\}$ 表示 $\{P(n) \mid n \in \mathbb{Z}\}$.

因为 $\theta(P-k)$ 有整数根当且仅当 $P-k$ 有整数根, 又 $\theta(P-k)=\theta(1)\left(R_{P}-k\right)$且 $\theta(1)$ 没有整数根, 所以 $P-k$ 有整数根当且仅当 $R_{P}-k$ 有整数根. 这说明 $k \in\{P(n)\}$ 当且仅当 $k \in\left\{R_{P}(n)\right\}$, 故 $\{P(n)\}=\left\{R_{P}(n)\right\}$.

我们需要一个引理.

引理 设 $p, q \in \mathbb{Q}[x]$, 且 $\operatorname{deg} q$ 是奇数. 若 $\{p(n)\}=\{q(n)\}$, 则存在 $\varepsilon \in$ $\{-1,1\}, k \in \mathbb{Z}$, 使得 $p(x)=q(\varepsilon x+k)$.

引理的证明由 $\operatorname{deg} q$ 是奇数, 知 $\{q(n)\}$ 无上界和下界, 所以 $\{p(n)\}$ 无上界和下界, 于是 $\operatorname{deg} p$ 也是奇数.

不妨设当 $x \rightarrow+\infty$ 时, $p(x), q(x) \rightarrow+\infty$, 否则考虑 $p(-x), q(-x)$. 于是存
在实数 $M$, 使得当 $x<M$ 时, $p(x)<p(M), q(x)<q(M)$, 且 $p, q$ 都在 $[M,+\infty)$上单调递增.

记 $X=\max \{p(M), q(M)\}$, 则存在整数 $a, b \geq M$, 使得

$$
\begin{aligned}
& \{p(n)\} \cap[X,+\infty)=\{p(a), p(a+1), \cdots\} \\
& \{q(n)\} \cap[X,+\infty)=\{q(b), q(b+1), \cdots\} .
\end{aligned}
$$

由 $\{p(n)\}=\{q(n)\}$, 知

$$
\{p(n)\} \cap[X,+\infty)=\{q(n)\} \cap[X,+\infty) .
$$

又

$$
p(a)<p(a+1)<\cdots, \quad q(b)<q(b+1)<\cdots,
$$

所以

$$
p(a)=q(b), p(a+1)=q(b+1), \cdots,
$$

故 $p(x)=q(x+b-a)$.

引理证毕.

回到原题. 当 $\operatorname{deg} P$ 是奇数时, 由 $\{P(n)\}=\left\{R_{P}(n)\right\}$ 和引理, 知 $R_{P}(x)=$ $P(\varepsilon x+k)$, 所以

$$
\theta(P)=\theta(1) P(\varepsilon x+k) .
$$

注意这里的 $\varepsilon$ 和 $k$ 依赖于 $P$.

设 $\theta(x)=\theta(1)(r x+s)$, 其中 $r \in\{-1,1\}, s \in \mathbb{Z}$. 下面证明, 对任意正整数 $n$,均有

$$
\theta\left(x^{n}\right)=\theta(1)(r x+s)^{n} .
$$

事实上, 对奇数 $n \geq 3$, 设 $\theta\left(x^{n}\right)=\theta(1)(t x+u)^{n}$, 其中 $t \in\{-1,1\}, u \in \mathbb{Z}$. 考虑 $\theta\left(x^{n}+x\right)$. 一方面, 由 $(* *)$,

$$
\theta\left(x^{n}+x\right)=\theta(1)\left((v x+w)^{n}+(v x+w)\right),
$$

其中 $v \in\{-1,1\}, w \in \mathbb{Z}$. 另一方面,

$$
\theta\left(x^{n}+x\right)=\theta\left(x^{n}\right)+\theta(x)=\theta(1)\left((t x+u)^{n}+(r x+s)\right) .
$$

所以

$$
(v x+w)^{n}+(v x+w)=(t x+u)^{n}+(r x+s) .
$$

比较 $x^{n}$ 的系数, 知 $v^{n}=t^{n}$, 因为 $n$ 是奇数, 所以 $v=t$. 比较 $x^{n-1}$ 的系数, 知
$n v^{n-1} w=n t^{n-1} u$, 所以 $w=u$. 再比较 $x$ 的系数和常数项, 知 $v=r, w=s$, 所以 $t=r, u=s$, 故

$$
\theta\left(x^{n}\right)=\theta(1)(r x+s)^{n} \text {. }
$$

对偶数 $n$, 取正奇数 $d$, 则由上面的论证,

$$
\theta\left(x^{n+d}\right)=\theta(1)(r x+s)^{n+d} \text {. }
$$

考虑 $\theta\left(x^{n+d}+x^{n}\right)$.一方面, 由 $(* *)$,

$$
\theta\left(x^{n+d}+x^{n}\right)=\theta(1)\left((v x+w)^{n+d}+(v x+w)^{n}\right),
$$

其中 $v \in\{-1,1\}, w \in \mathbb{Z}$. 另一方面，

$$
\theta\left(x^{n+d}+x^{n}\right)=\theta\left(x^{n+d}\right)+\theta\left(x^{n}\right)=\theta(1)\left((r x+s)^{n+d}+R_{n}(x)\right) .
$$

所以

$$
(v x+w)^{n+d}+(v x+w)^{n}=(r x+s)^{n+d}+R_{n}(x) .
$$

取 $d$ 使得 $n+d-1>\operatorname{deg} R_{n}$. 比较 $x^{n+d}$ 的系数, 知 $v^{n+d}=r^{n+d}$, 因为 $n+d$是奇数, 所以 $v=r$. 比较 $x^{n+d-1}$ 的系数, 知 $(n+d) v^{n+d-1} w=(n+d) r^{n+d-1} s$, 所以 $w=s$. 于是 $R_{n}(x)=(r x+s)^{n}$, 故

$$
\theta\left(x^{n}\right)=\theta(1)(r x+s)^{n} .
$$

这样, 由 $(*)$,

$$
\theta(P)=\sum_{i=0}^{n} a_{i} \theta(1)(r x+s)^{i}=\theta(1) P(r x+s) .
$$

综上, 对任意 $P \in \mathbb{Z}[x], \theta(P)=f(x) P(r x+s)$, 其中 $f(x) \in \mathbb{Z}[x]$ 无整数根, $r \in\{-1,1\}, s \in \mathbb{Z}$.

评注 本题过程较长, 但思路比较清晰. 先由条件 (1), 将问题锁定在多项式空间的一组基上. 再由条件 (2), 将整数根之间的关系转化为两个多项式的值域相同,由此自然想到引理. 最后是一些细节上的讨论.

3. 设 $G$ 是无限大的单位正方形网格. “棋盘多边形” 是指边沿着 $G$ 中网格线的不自交的多边形. 甲选择一个棋盘多边形 $F$, 乙的任务是将 $G$ 中某些方格染成绿色, 使得所有和 $F$ 全等的棋盘多边形中都至少有 1 个格、至多有 2020 个格是绿色的. 问:甲能否选择一个 $F$ 使乙无法完成任务?

解 结果是肯定的. 事实上, 我们可以证明更强的结论, 甲能选择一个棋盘多边形 $F$, 使得存在一个由 $F$ 平移得到的棋盘多边形, 其中有多于 2020 个绿格.
对正整数 $d$, 设集合

$A=\left\{x \mid x\right.$ 为小于 $4000^{d}$ 的正整数且 $x$ 的 4000 进制表示中无 3999$\}$.

先证明一个引理.

引理 对任意由介于 $\frac{1}{4} \cdot 4000^{d}$ 和 $\frac{1}{2} \cdot 4000^{d}$ 之间的 3999 个正整数构成的集合 $S$, 存在整数 $x$, 使得 $S+x \subseteq A$, 其中 $S+x=\{s+x \mid s \in S\}$.

引理的证明 我们证明可将 $S$ 中的元素表示成

$$
a_{0}+a_{1} \cdot 4000+\cdots+a_{d-1} \cdot 4000^{d-1}
$$

的形式, 其中 $-3999 \leq a_{i} \leq 3999, i=0,1, \cdots, d-1$.

首先确定 $a_{0}$. 因为 $|S|=3999$, 所以存在 $m(1 \leq m \leq 4000)$ 不与 $S$ 中任意一个元素模 4000 同余. 对 $s \in S$, 若 $s$ 模 4000 的余数小于 $m$, 则取 $a_{0}$ 为 $s$ 模 4000 的余数; 若 $s$ 模 4000 的余数大于 $m$, 则取 $a_{0}$ 为 $s$ 模 4000 的余数减 4000 .

将 $S$ 中的所有元素减 $a_{0}$ 再除以 4000 , 对得到的数重复上述过程, 可依次确定 $a_{1}, \cdots, a_{d-2}$. 因为

$$
3999+3999 \cdot 4000+\cdots+3999 \cdot 4000^{d-2}<4000^{d-1}
$$

所以此时所有数介于 $0.24 \cdot 4000$ 和 $0.51 \cdot 4000$ 之间, 取 $a_{d-1}$ 为现在的数即可.

对 $0 \leq i \leq d-1$, 设 $b_{i}$ 是所有 3999 个 $a_{i}$ 中最小的一个. 由构造的方式, $m-3999 \leq a_{i} \leq m-1$, 所以令

$$
y=\sum_{i=0}^{d-1} b_{i} \cdot 4000^{i}
$$

则 $S-y \subseteq A$. 引理得证.

回到原题.

甲取棋盘多边形 $F$ 为区域

$$
\left(\bigcup_{a \in A}[a, a+1]\right) \times\left[0,4000^{d}\right] \cup\left[1,4000^{d}\right] \times[0,1]
$$

的边界, $F$ 的形状近似于下图.



由 $|A|=3999^{d}-1$ 知 $F$ 的面积

$$
[F]=\left(3999^{d}-1\right) \cdot 4000^{d}+\left(4000^{d}-3999^{d}\right) .
$$

当 $d$ 充分大时, $[F]<\frac{1}{10^{20}} \cdot 4000^{2 d}$.

假设乙能完成任务, 则对每个 $F$ 平移后的像 $F^{\prime}, F^{\prime}$ 中都至少有 1 个绿格, 至多有 2020 个绿格.

当 $F^{\prime}$ 左下角的小方格取遍区域 $\left[0,4000^{d}\right] \times\left[0,4000^{d}\right]$ 中的所有小方格时,设这 $4000^{2 d}$ 个 $F^{\prime}$ 所围成的区域的并为 $H$. 因为每个 $F^{\prime}$ 中都至少有 1 个绿格, 且每个绿格至多在 $[F]$ 个 $F^{\prime}$ 中, 所以 $H$ 中至少有

$$
\frac{4000^{2 d}}{[F]}>10^{20}
$$

个绿格.

$H$ 包含于正方形 $\left[0,2 \cdot 4000^{d}\right] \times\left[0,2 \cdot 4000^{d}\right]$ 中. 将该正方形横向平均分成 8 排、纵向平均分成 8 列, 得到 64 个小正方形, 每个小正方形的边长均为 $\frac{1}{4} \cdot 4000^{d}$. 由平均值原理, 存在一个小正方形中至少有

$$
\frac{10^{20}}{64}>2020
$$

个绿格. 由引理, 可找到 $F$ 平移后的像 $F_{0}$ 覆盖这些绿格, 这与 $F_{0}$ 中的绿格至多有 2020 个矛盾!

综上, 命题得证.

评注 本题难度较大, 从一维情形入手是几乎必然的, 由此可以想到 $F$ 的形状类似 “梳子”. 主要难点在于如何排布梳子的缝隙, 使得一方面 $F$ 的面积比较小, 另一方面梳子的 “齿” 可以囊括一定范围内的方格在一维上的所有分布可能. 其中去掉进制中含某个数字的所有数的手段让人想到下面的经典问题:

“证明: 所有十进制表示中不含数字 9 的正整数的倒数之和小于 28.”

4. 证明: 对任意素数 $p$, 存在正整数 $n$, 使得

$$
1^{n}+2^{n-1}+3^{n-2}+\cdots+n^{1} \equiv 2020 \quad(\bmod p)
$$

证明 先证明一个引理.

引理 $\sum_{k=1}^{p(p-1)} k^{p(p-1)+1-k} \equiv-1(\bmod p)$.

引理的证明 注意到

$$
\begin{aligned}
\sum_{k=1}^{p(p-1)} k^{p(p-1)+1-k} & =\sum_{i=0}^{p-2} \sum_{r=1}^{p}(i p+r)^{p(p-1)+1-i p-r} \\
& \equiv \sum_{i=0}^{p-2} \sum_{r=1}^{p} r^{p(p-1)+1-i p-r}
\end{aligned}
$$

$$
=\sum_{r=1}^{p} \sum_{i=0}^{p-2} r^{p(p-1)+1-i p-r} \quad(\bmod p)
$$

对固定的 $r(2 \leq r \leq p-1)$, 由 $(p, p-1)=1$ 知, 当 $i$ 遍历 $0 \sim p-2$ 时, $p(p-1)+1-i p-r$ 遍历模 $p-1$ 的完全剩余系. 于是由费马小定理,

$$
\sum_{i=0}^{p-2} r^{p(p-1)+1-i p-r} \equiv \sum_{i=0}^{p-2} r^{i}=\frac{r^{p-1}-1}{r-1} \equiv 0 \quad(\bmod p)
$$

又当 $r=1$ 时,

$$
\sum_{i=0}^{p-2} r^{p(p-1)+1-i p-r}=\sum_{i=0}^{p-2} 1=p-1 \equiv-1 \quad(\bmod p)
$$

当 $r=p$ 时,

$$
\sum_{i=0}^{p-2} r^{p(p-1)+1-i p-r} \equiv \sum_{i=0}^{p-2} 0=0 \quad(\bmod p)
$$

所以

$$
\sum_{r=1}^{p} \sum_{i=0}^{p-2} r^{p(p-1)+1-i p-r} \equiv-1 \quad(\bmod p)
$$

引理证毕.

回到原题. 令 $n=t p(p-1)$. 由费马小定理, 当 $a_{1} \equiv a_{2}(\bmod p), b_{1} \equiv b_{2}$ $(\bmod p-1)$ 时, $a_{1}^{b_{1}} \equiv a_{2}^{b_{2}}(\bmod p)$. 从而结合引理得,

$$
\sum_{k=1}^{n} k^{n+1-k} \equiv t \sum_{k=1}^{p(p-1)} k^{p(p-1)+1-k} \equiv-t \quad(\bmod p) .
$$

因此取正整数 $t$ 满足 $t \equiv-2020(\bmod p)$ 即可.

综上, 命题得证.

评注本题是费马小定理的常规运用. 当考虑幂模素数 $p$ 的余数时, 常让底数模 $p$ 、指数模 $p-1$, 由此自然地想到引理. 之后利用模 $p$ 余数的周期性即可找到合适的 $n$.

5. 设 $\mathcal{P}$ 是一个正多边形, $\mathcal{V}$ 是其顶点集. 将 $\mathcal{V}$ 中的每个点染成红、白、蓝三色之一. $\mathcal{V}$ 的一个子集称为 “爱国的”，如果它包含每种颜色的点的个数相同. $\mathcal{P}$ 的一条边称为 “耀眼的”，如果它的两个端点的颜色不同. 已知 $\mathcal{V}$ 是爱国的且 $\mathcal{P}$ 有偶数条耀眼的边, 证明:存在一条不经过 $\mathcal{V}$ 中点的直线, 将 $\mathcal{V}$ 划分成两个非空的爱国的子集.

证明 我们在正三角形网格中按如下方式画出一条路径:

(1) 在 $\mathcal{V}$ 中任取一点 $A$, 将其任意对应到正三角形网格的一个格点 $A^{\prime}$;

(2) 按顺时针方向, 如果 $A$ 的下一个顶点是红色的, 则将 $A^{\prime}$ 向右移到下一个格点; 如果 $A$ 的下一个顶点是白色的, 则将 $A^{\prime}$ 沿左上方向移到下一个格点;如果 $A$ 的下一个顶点是蓝色的, 则将 $A^{\prime}$ 沿左下方向移到下一个格点;

(3) 依此类推.

由于 $\mathcal{V}$ 是爱国的, 所以上述路径是闭的, 记为 $\mathcal{Q}$. 下图是 $\mathcal{V}$ 中有 18 个点的例子:


注意到若 $\mathcal{V}$ 中的点不能被直线划分成两个非空的爱国的子集, 则 $\mathcal{Q}$ 是不自交的多边形, 我们证明此时 $\mathcal{P}$ 中耀眼的边的个数是奇数, 从而矛盾.

事实上, $\mathcal{P}$ 中每条耀眼的边对应 $\mathcal{Q}$ 的一个顶点. $\mathcal{Q}$ 的每个内角等于 $60^{\circ}$ 或 $300^{\circ}$, 设有 $x$ 个等于 $60^{\circ} 、 y$ 个等于 $300^{\circ}$. 考虑内角和得,

$$
60^{\circ} x+300^{\circ} y=180^{\circ}(x+y-2),
$$

即 $x-y=3$. 所以 $\mathcal{Q}$ 的顶点的个数为 $x+y$, 是奇数, 故 $\mathcal{P}$ 中耀眼的边的个数是奇数.

综上, 命题得证.

评注 本题将描述状态的数组与坐标中的点一一对应, 有点像物理中的相空间. 类似的思想也出现在经典的项链分赃问题 (stolen necklace problem) 中, 那里是应用拓扑学中的 Borsuk-Ulam 定理予以解决的.

6. 如图, 在不等边锐角 $\triangle A B C$ 中, $O$ 是外心, $A D, B E, C F$ 是高. $X, Y, Z$分别是 $A D, B E, C F$ 的中点, $A D$ 与 $Y Z$ 交于点 $P, B E$ 与 $Z X$ 交于点 $Q, C F$与 $X Y$ 交于点 $R$. 设 $Y Z$ 与 $B C$ 交于点 $A^{\prime}, Q R$ 与 $E F$ 交于点 $D^{\prime}$. 证明:过 $A, B, C, O$ 且分别垂直于 $Q R, R P, P Q, A^{\prime} D^{\prime}$ 的直线交于一点.

证明 1 先证明 $A^{\prime} D^{\prime}$ 是 $\triangle D E F$ 和 $\triangle X Y Z$ 的外接圆的根轴.

设 $H$ 是 $\triangle A B C$ 的垂心, $M$ 是 $B C$ 的中点. 因为 $M B=M E$ 且 $Y$ 是 $B E$ 的



中点, 所以 $M Y \perp B E$. 同理, $M Z \perp C F$. 又 $H D \perp B C$, 所以 $Y, Z, D$ 都在以 $H M$为直径的圆上. 这样,

$$
A^{\prime} D \cdot A^{\prime} M=A^{\prime} Y \cdot A^{\prime} Z
$$

又 $M$ 在 $\triangle D E F$ 的外接圆上, 所以 $A^{\prime}$ 到 $\triangle D E F$ 和 $\triangle X Y Z$ 的外接圆的幂相等.

同理可知, $H, X, E, Z$ 和 $H, X, F, Y$ 分别四点共圆, 所以

$$
Q H \cdot Q E=Q X \cdot Q Z, \quad R H \cdot R F=R X \cdot R Y
$$

这说明 $Q R$ 是以 $A H$ 为直径的圆和 $\triangle X Y Z$ 的外接圆的根轴. 又 $E F$ 是以 $A H$为直径的圆和 $\triangle D E F$ 的外接圆的根轴, 所以 $D^{\prime}$ 在 $\triangle D E F$ 和 $\triangle X Y Z$ 的外接圆的根轴上.

故 $A^{\prime} D^{\prime}$ 是 $\triangle D E F$ 和 $\triangle X Y Z$ 的外接圆的根轴.



设 $O^{\prime}$ 是 $\triangle X Y Z$ 的外心, $S$ 是 $H$ 关于 $O^{\prime}$ 的对称点.

再证明过 $A, B, C, O$ 且分别垂直于 $Q R, R P, P Q, A^{\prime} D^{\prime}$ 的直线交于点 $S$.

设 $N$ 是 $A H$ 的中点, 则 $N$ 是以 $A H$ 为直径的圆的圆心. 因为 $Q R$ 是以 $A H$为直径的圆和 $\triangle X Y Z$ 的外接圆的根轴, 所以 $N O^{\prime} \perp Q R$. 又因为 $N O^{\prime} / / A S$, 所以 $A S \perp Q R$. 同理, $B S \perp R P, C S \perp P Q$.
设 $V$ 是 $O H$ 的中点, 则 $V$ 是 $\triangle D E F$ 的外心. 因为 $A^{\prime} D^{\prime}$ 是 $\triangle D E F$ 和 $\triangle X Y Z$ 的外接圆的根轴, 所以 $V O^{\prime} \perp A^{\prime} D^{\prime}$. 又 $V O^{\prime} / / O S$, 所以 $O S \perp A^{\prime} D^{\prime}$.

综上, 命题得证.



证明 2 类似定义点 $B^{\prime}, C^{\prime}, E^{\prime}, F^{\prime}$.

对 $\triangle A B C$ 和 $\triangle X Y Z$ 用笛沙格定理得, $A^{\prime}, B^{\prime}, C^{\prime}$ 共线.

对 $\triangle D E F$ 和 $\triangle P Q R$ 用笛沙格定理得, $D^{\prime}, E^{\prime}, F^{\prime}$ 共线.

对 $\triangle A E F$ 和 $\triangle X Q R$ 用笛沙格定理得, $B^{\prime}, C^{\prime}, D^{\prime}$ 共线.

同理, $A^{\prime}, B^{\prime}, F^{\prime}$ 和 $A^{\prime}, C^{\prime}, E^{\prime}$ 分别共线, 所以 $A^{\prime}, B^{\prime}, C^{\prime}, D^{\prime}, E^{\prime}, F^{\prime}$ 六点共线.

因为过 $P, Q, R$ 且分别垂直于 $B C, C A, A B$ 的直线交于 $\triangle A B C$ 的垂心 $H$, 所以对 $\triangle A B C$ 和 $\triangle P Q R$ 用正交三角形定理得, 过 $A, B, C$ 且分别垂直于 $Q R, R P, P Q$ 的直线交于一点.

由 $F E \perp A O, D E \perp C O$, 知过 $D^{\prime}, F^{\prime}, Q$ 且分别垂直于 $A O, C O, A C$ 的直线交于点 $E$. 所以对 $\triangle D^{\prime} F^{\prime} Q$ 和 $\triangle C A O$ 用正交三角形定理得, 过 $C, A, O$ 且分别垂直于 $F^{\prime} Q, D^{\prime} Q, D^{\prime} F^{\prime}$ 的直线交于一点, 即过 $C, A, O$ 且分别垂直于 $P Q, Q R, A^{\prime} D^{\prime}$ 的直线交于一点.

故过 $A, B, C, O$ 且分别垂直于 $Q R, R P, P Q, A^{\prime} D^{\prime}$ 的直线交于一点.

评注 本题中前三条直线共点从正交三角形定理的观点看是显然的, 补出点 $B^{\prime}, C^{\prime}, E^{\prime}, F^{\prime}$ 后也不难证明六点共线, 有意思的是第四条直线共点也可以应用正交三角形定理. 相比之下证法一对根轴的观察是更有难度的, 但其提示了问题的本质.

