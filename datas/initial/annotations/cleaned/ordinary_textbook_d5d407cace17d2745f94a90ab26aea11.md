# 难题新解集锦 (一) 

张盛桐 ${ }^{1}$ 欧阳泽轩 ${ }^{2}$ 张江昊 $^{3}$ 虞家伟 ${ }^{4}$ 郭若一 5

(1. 上海中学, 200231；2. 温州中学, 325014；3. 西北师大附中, 730070 ;
4. 南昌二中, 330013 ;
5. 山西大学附属中学, 030006)

本期难题新解集锦介绍四个问题的新解.

## 1. 二项系数和的对数凹性

美国数学月刊 (Amer. Math. Monthly) 的第 11985 号问题 (2017. Vol. 124, No, 1) 可叙述为

题 1. 设 $s, t$ 是给定的自然数, $s \leq t$. 令

$$
a_{n}=\left(\begin{array}{c}
n \\
s
\end{array}\right)+\left(\begin{array}{c}
n \\
s+1
\end{array}\right)+\cdots+\left(\begin{array}{c}
n \\
t
\end{array}\right) \text {. }
$$

证明: 对 $\forall n \in \mathbb{N}^{*}$ 有 $a_{n}^{2} \geq a_{n-1} a_{n+1}$.

## 证法一 (张盛桐)

设 $F(n, s, t)=\sum_{i=s}^{t}\left(\begin{array}{c}n \\ i\end{array}\right)$, 则要证结果等价于

$$
F(n-1, s, t) \cdot F(n+1, s, t) \leq F^{2}(n, s, t) .
$$

仅需考虑 $n>1$ 的情况.

注意到

$$
\begin{aligned}
& F(n, s, t)=\sum_{i=s}^{t}\left(\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)+\left(\begin{array}{c}
n-1 \\
i-1
\end{array}\right)\right)=F(n-1, s, t)+F(n-1, s-1, t-1), \\
& F(n+1, s, t)=F(n, s, t)+F(n, s-1, t-1) \\
& \quad=F(n-1, s, t)+2 F(n-1, s-1, t-1)+F(n-1, s-2, t-2) .
\end{aligned}
$$

将它们分别代入 (1) 的两边便知 (1) 等价于

$$
F(n-1, s-2, t-2) \cdot F(n-1, s, t) \leq F^{2}(n-1, s-1, t-1) .
$$

收稿日期: 2017-11-27; 修订日期: 2017-12-14.
故我们只需证明: 对 $\forall s, t, n \in \mathbb{N}^{*}$ 有

$$
F(n, s-1, t-1) \cdot F(n, s+1, t+1) \leq F^{2}(n, s, t) .
$$

下用归纳法证明 (2).

$n=1$ 时, (2) 显然成立.

假设 (2) 对 $n$ 成立, 则对 $n+1$, 我们需要证明:

$$
F(n+1, s, t) \cdot F(n+1, s+2, t+2) \leq F^{2}(n+1, s+1, t+1) \text {. }
$$

下分两种情况:

1) 当 $s=t$ 时, (3) 可写为

$$
\left(\begin{array}{c}
n+1 \\
s
\end{array}\right)\left(\begin{array}{c}
n+1 \\
s+2
\end{array}\right) \leq\left(\begin{array}{c}
n+1 \\
s+1
\end{array}\right)^{2}
$$

这可直接计算验证其成立.

2) 当 $s<t$ 时, 由归纳假设知,

$$
F(n, s-1, t-1) \leq \frac{F^{2}(n, s, t)}{F(n, s+1, t+1)}, F(n, s+2, t+2) \leq \frac{F^{2}(n, s+1, t+1)}{F(n, s, t)}
$$

故

$$
\begin{aligned}
& F(n+1, s, t) \cdot F(n+1, s+2, t+2) \\
= & (F(n, s-1, t-1)+F(n, s, t)) \cdot(F(n, s+1, t+1)+F(n, s+2, t+2)) \\
\leq & \left(\frac{F^{2}(n, s, t)}{F(n, s+1, t+1)}+F(n, s, t)\right) \cdot\left(F(n, s+1, t+1)+\frac{F^{2}(n, s+1, t+1)}{F(n, s, t)}\right) \\
= & (F(n, s, t)+F(n, s+1, t+1))^{2}=F^{2}(n+1, s+1, t+1) .
\end{aligned}
$$

这就是 (3), 证毕.

## 证法二 (欧阳泽轩)

当 $n \leq s$ 时, 结论显然成立.

下设 $n \geq s+1$. 注意到 $\left(\begin{array}{c}n \\ i\end{array}\right)=\left(\begin{array}{c}n-1 \\ i-1\end{array}\right)+\left(\begin{array}{c}n-1 \\ i\end{array}\right), \forall 1 \leq i \leq n-1$. 故要证结论等价于

$$
\begin{aligned}
\frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \geq \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n+1 \\
i
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i
\end{array}\right)} & \Leftrightarrow \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)+\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i-1
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \geq \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i
\end{array}\right)+\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i-1
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i
\end{array}\right)} \\
& \Leftrightarrow \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i-1
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \geq \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i-1
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i
\end{array}\right)}
\end{aligned}
$$

$$
\Leftrightarrow \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \geq \frac{\sum_{i=s}^{t}\left(\begin{array}{c}
n \\
i-1
\end{array}\right)}{\sum_{i=s}^{t}\left(\begin{array}{c}
n-1 \\
i-1
\end{array}\right)}
$$

注意到

$$
\frac{\left(\begin{array}{c}
n \\
i
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \geq \frac{\left(\begin{array}{c}
n \\
i-1
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
i-1
\end{array}\right)}, \forall 1 \leq i \leq n-1
$$

由分式性质: 若 $0<\frac{a_{1}}{b_{1}} \leq \cdots \leq \frac{a_{k}}{b_{k}}$, 则 $\frac{a_{1}}{b_{1}} \leq \frac{a_{1}+\cdots+a_{k}}{b_{1}+\cdots+b_{k}} \leq \frac{a_{k}}{b_{k}}$. 可得

$$
\frac{\left(\begin{array}{c}
n \\
s-1
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
s-1
\end{array}\right)} \leq \frac{\left(\begin{array}{c}
n \\
s
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
s
\end{array}\right)} \leq \frac{\sum_{i=s}^{t-1}\left(\begin{array}{c}
n \\
i
\end{array}\right)}{\sum_{i=s}^{t-1}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \leq \frac{\left(\begin{array}{c}
n \\
t-1
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
t-1
\end{array}\right)} \leq \frac{\left(\begin{array}{c}
n \\
t
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
t
\end{array}\right)}
$$

再用上面的分式性质可得:

$$
\frac{\left(\begin{array}{c}
n \\
s-1
\end{array}\right)+\sum_{i=s}^{t-1}\left(\begin{array}{c}
n \\
i
\end{array}\right)}{\left(\begin{array}{c}
n-1 \\
s-1
\end{array}\right)+\sum_{i=s}^{t-1}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \leq \frac{\sum_{i=s}^{t-1}\left(\begin{array}{c}
n \\
i
\end{array}\right)}{\sum_{i=s}^{t-1}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)} \leq \frac{\sum_{i=s}^{t-1}\left(\begin{array}{c}
n \\
i
\end{array}\right)+\left(\begin{array}{c}
n \\
t
\end{array}\right)}{\sum_{i=s}^{t-1}\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)+\left(\begin{array}{c}
n-1 \\
t
\end{array}\right)}
$$

这就是 (4). 证毕.

## 2. $\left(\begin{array}{c}p^{n} \\ q^{n}\end{array}\right)$ 的素因子

2017 年北京大学金秋营 [1] 的第八题是一个数论难题, 可叙述为:

题 2. 给定正整数 $p, q$, 满足 $1<q<p$. 证明: 对任意素数 $r>p$, 存在正整数 $n$ 满足

$$
r \left\lvert\,\left(\begin{array}{l}
p^{n} \\
q^{n}
\end{array}\right)\right.
$$

## 证明 (张江昊)

由卢卡斯定理, 仅需证明: 存在正整数 $n$ 使得 $q^{n}$ 在 $r$ 进制下某一位的数码比 $p^{n}$ 在 $r$ 进制下相应位的数码大. 进而, 只需证明: 存在 $n$ 使得 $q^{n}$ 模 $r^{k}$ 的最小非负剩余大于 $p^{n}$ 模 $r^{k}$ 的最小非负剩余, 这里 $k$ 是一个待定的正整数.

现在需要如下引理:

引理 设正整数 $p, q, r$ 满足 $1<q<p<r$ 且 $r$ 为素数, 当 $\alpha \in \mathbb{N}^{*}$ 足够大时,存在 $l \in \mathbb{N}^{*}$ 满足 $r^{l} \not \equiv 1\left(\bmod p^{\alpha}\right), r^{l} \equiv 1\left(\bmod q^{\alpha}\right), r^{l} \equiv 1\left(\bmod p^{\alpha-1}\right)$.

引理证明 由升幂定理知, 当 $\alpha$ 足够大时, 若设 $r$ 模 $p^{\alpha-1}$ 的阶为 $l$, 则对 $\forall p_{i} \mid p$ 有

$$
v_{p_{i}}\left(r^{l_{1}}-1\right)=v_{p_{i}}\left(p^{\alpha-1}\right),
$$

从而, 若设 $r$ 模 $p^{\alpha-1}, q^{\alpha}$ 的阶分别为 $l_{1}, l_{2}$, 则取 $l_{0}=\left[l_{1}, l_{2}\right]$, 便有 $r^{l_{0}} \equiv 1$
$\left(\bmod p^{\alpha-1}\right), r^{l_{0}} \equiv 1\left(\bmod q^{\alpha}\right)$.

对任意素数 $s \mid\left[q^{\alpha}, p^{\alpha-1}\right]$, 现考虑 $v_{s}\left(r^{l_{0}}-1\right)$, 由于

$$
v_{s}\left(l_{0}\right)=\max \left\{v_{s}\left(l_{1}\right), v_{s}\left(l_{2}\right)\right\}
$$

由升幂定理知

$$
v_{s}\left(r^{l_{0}}-1\right)=v_{s}\left(r^{l_{1}}-1\right) \text { 或 } v_{s}\left(r^{l_{2}}-1\right) \text {. }
$$

由于 $p>q$, 因此 $p$ 的素因子分解中有一个素数 $s_{0}$ 满足 $s_{0}$ 在 $p$ 中的幕次大于它在 $q$ 中的, 对于这个 $s_{0}$, 注意到

$$
v_{s_{0}}\left(r^{l_{0}}-1\right)=v_{s_{0}}\left(r^{l_{1}}-1\right) \text { 或 } v_{s_{0}}\left(r^{l_{2}}-1\right) \text {, }
$$

这两种情况都有

$$
v_{s_{0}}\left(r^{l_{0}}-1\right)<v_{s_{0}}\left(p^{\alpha}\right) .
$$

这里用到了 (1).

因此这个 $l_{0}$ 符合条件, 引理得证.

回到原题. 取一个足够大的 $b \in \mathbb{N}^{*}$ 使得 $b$ 满足 (1) 且 $q^{b}>p$. 由引理知存在 $n \in \mathbb{N}^{*}$ 满足 $r^{n} \equiv 1\left(\bmod q^{b}\right), r^{n} \equiv 1\left(\bmod p^{b-1}\right), r^{n} \not \equiv 1\left(\bmod p^{b}\right)$. 又易见存在 $c \in \mathbb{N}^{*}$ 且 $c>b$ 使得 $p^{c} \equiv 1\left(\bmod r^{n}\right), q^{c} \equiv 1\left(\bmod r^{n}\right)$. 现取 $n_{0}=c-b$, 下证 $n_{0}$ 满足题意.

设 $q^{c-b}$ 模 $r^{n}$ 的最小非负剩余为 $Q$, 则

$$
Q \cdot q^{b} \equiv q^{c} \quad\left(\bmod r^{n}\right)
$$

即

$$
Q \cdot q^{b} \equiv m r^{n}+1 \text {. }
$$

又由 $Q<r^{n}$ 可得 $m<q^{b}$.

现在 (2) 的两边模 $q^{b}$, 则有

$$
m \equiv 1 \quad\left(\bmod q^{b}\right) .
$$

因此 $m=q^{b}-1$, 即 $Q=\left(1-\frac{1}{q^{b}}\right) r^{n}+\frac{1}{q^{b}}$.

类似地, 设 $P$ 为 $p^{c-b}$ 模 $r^{n}$ 的最小非负剩余, 则

$$
P \cdot p^{b}=g \cdot r^{n}+1, g<p^{b} .
$$

上式两边模 $p^{b-1}$ 可得 $g \equiv-1\left(\bmod p^{b-1}\right)$, 而两边 $\bmod p^{b}$ 可得 $g \neq p^{b}-1$, 故
$g \leq p^{b}-1-p^{b-1}$, 因此

$$
p \leq\left(1-\frac{1}{p}-\frac{1}{p^{b}}\right) r^{n}+\frac{1}{p^{b}}
$$

于是 $p<Q$. 这说明 $q^{n_{0}}$ 模 $r^{n}$ 的最小非负剩余大于 $p^{n_{0}}$ 模 $r^{n}$ 的最小非负剩余,故在 $q^{n_{0}}, p^{n_{0}}$ 的 $r$ 进制后 $n$ 位数必有一位上 $q^{n_{0}}$ 的数码更大, 故命题成立.

## 3. 连通的几何图

2017 年罗马尼亚的国家队选拔考试中有如下的几何图问题:

题 3. 一个国家有奇数个城市, 它们之间的距离两两不同. 有些城市之间有双向直飞航班连接。对每一个城市, 它恰和两个距离它最远的城市有直飞航班.证明: 我们可以从任意一个城市飞到另一个.

## 证明 (虞家伟)

首先构造图 $G$ : 其中的顶点表示城市; 若两个城市间有直飞航班, 则在对应的两点之间连边, 这里的边是有长度的, 即为其对应两城市间的距离. 由条件知,若 $G$ 中的三个点 $X, Y, Z$ 满足 $X Y$ 是边, $X$ 和 $Z$ 没有连边, 则 $|X Y|>|X Z|$.

现来证明 $G$ 是连通的.

用反证法. 假设 $G$ 不连通, 则 $G$ 至少有两个连通分支.

由于 $G$ 中每个点的度为 2 , 因此 $G$ 的每个连通分支均是一个圈. 又 $G$ 的总顶点数为奇数. 故 $G$ 的某个连通分支必是奇圈 (奇数个顶点的圈).

设 $C_{1}$ 是 $G$ 的一个奇圈, 这时再取 $G$ 的异于 $C_{1}$ 的另一连通分支中的一条边 $A B$, 注意到 $C_{1}$ 的点均与 $A$ 和 $B$ 没有边相连. 任取顶点 $P \in C_{1}$, 则 $|P A|<|A B|,|P B|<|A B|$.

现分边以 $A, B$ 为圆心, $|A B|$ 为半径作图, 两圆交于 $X, Y$ (如右图), 则 $P$ 既在 $\odot A$ 内, 又在 $\odot B$ 内.

现定义区域 $\alpha: \overparen{A X}, \overparen{X B}, A B$ 围成的区域; 区域 $\beta$ : $\overparen{A Y}, \overparen{Y B}, A B$ 围成的区域, 则点 $P$ 在 $\alpha \cup B$ 内.



记 $C_{1}$ 在 $\alpha$ 内的点的集合为 $C_{1}^{(1)}$, 在 $\beta$ 内的点的集合记为 $C_{1}^{(2)}$. 由于 $C_{1}$ 是奇圈, 但二部图不含奇圈, 故 $C_{1}$ 不是二部图, 于是 $C_{1}^{(1)}$ 中有一对相连的点或 $C_{1}^{(2)}$ 中有一对相连的点.

不妨设 $Q, R \in C_{1}^{(1)}$, 且 $Q, R$ 相连. 不妨设 $Q$ 到 $A B$ 的距离不小于 $R$ 到 $A B$的距离, 且 $Q$ 在 $A B$ 中垂线右侧 (靠近 $B$ ), 如右下图.

作 $R H \perp A B$. 由于 $\angle Q R H \geq 90^{\circ}>\angle Q H R$, 所以 $Q R<Q H$.
又 $\angle Q H A \geq \angle Q B A \geq \angle Q A B$, 因此 $Q H \leq Q A$, 故 $Q R<Q A$.

注意到 $Q R$ 是边, 这说明 $Q, A$ 有边相连, 这与它们分别位于不同连通分支上矛盾!

综上, $G$ 是连通的, 亦即我们可从任意一个城市飞到另一个.



## 4. 一个离散 Northcott 不等式

K. Fan, O. Taussky 和 J.Todd 在 1955 年建立了一个离散的 Northcott不等式 [2]. 它可改述为下面的极值问题:

题 4. 给定整数 $n \geq 2$, 实数 $x_{1}, \cdots, x_{n}$ 满足

(1) $\sum_{i=1}^{n} x_{i}=0 ; \quad$ (2) $\max _{1 \leq i \leq n}\left|x_{i}\right|=1$.

求 $\max _{1 \leq i \leq n}\left|x_{i}-x_{i+1}\right|$ 的最小值, 其中 $x_{n+1}=x_{1}$.

## 解答 (郭若一)

记 $M=\max _{1 \leq i \leq n}\left|x_{i}-x_{i+1}\right|$.

注意到问题是轮换对称的, 不妨设 $x_{1}=1$.

1) 当 $n$ 是偶数时, 设 $n=2 k, k \in \mathbb{N}^{*}$.

由于 $\left|x_{1}-x_{2}\right| \leq M$, 所以 $x_{2} \geq x_{1}-\left|x_{1}-x_{2}\right| \geq 1-M$. 进而有

$$
x_{3} \geq x_{2}-\left|x_{3}-x_{2}\right| \geq 1-2 M
$$

一般地, 对任意 $r \in\{2, \cdots, k+1\}$ 有

$$
x_{r} \geq 1-(r-1) M \text {. }
$$

又 $\left|x_{1}-x_{2 k}\right| \leq M$, 所以 $x_{2 k} \geq x_{1}-\left|x_{1}-x_{2 k}\right| \geq 1-M$. 进而有

$$
x_{2 k-1} \geq x_{2 k}-\left|x_{2 k+1}-x_{2 k}\right| \geq 1-2 M
$$

一般地, 对任意 $r \in\{k+2, \cdots, 2 k\}$ 有

$$
x_{r} \geq 1-(2 k+1-r) M \text {. }
$$

结合 (1), (2) 及条件知

$$
0=x_{1}+\sum_{r=2}^{k+1} x_{r}+\sum_{r=k+2}^{2 k} x_{r}=2 k-k^{2} M
$$

故 $M \geq \frac{2}{k}$.
当 $x_{1}=1, x_{r}=1-\frac{2}{n}(r-1), r=2,3, \cdots, k, x_{k+1}=-1, x_{n+1+r}=-1+\frac{2}{k} r$, $r=1,2, \cdots, k-1$ 时, 满足条件且此时 $M=\frac{2}{k}$. 故 $M$ 的最小值为 $\frac{2}{k}$.

2) 当 $n$ 为奇数时, 设 $n=2 k+1, k \in \mathbb{N}^{*}$.

由 1) 的证明易知 $x_{2} \geq 1-M, x_{3} \geq 1-2 M, \cdots, x_{k+1} \geq 1-k M$, 且 $x_{2 k+1} \geq 1-M, x_{2 k} \geq 1-2 M, \cdots, x_{k+2} \geq 1-k M$.

将它们相加并用条件便知

$$
0=\sum_{i=1}^{n} x_{i}=2 k+1-k(k+1) M \text {. }
$$

故 $M \geq \frac{2 k+1}{k(k+1)}$.

当 $x_{1}=1, x_{r}=1-\frac{2 k+1}{k(k+1)}(r-1), r=2,3, \cdots, k+1$,

$$
x_{2 k+2-r}=1-\frac{2 k}{k(k+1)} r, r=1,2, \cdots, k
$$

注意到此时

$$
\min _{1 \leq i \leq n} x_{i}=1-\frac{(2 k+1) k}{k(k+1)}=-\frac{k}{k+1}>-1
$$

从而易验证它们满足条件. 故 $M$ 的最小值为 $\frac{2 k+1}{k(k+1)}$.

综上,

$$
M_{\text {min }}= \begin{cases}\frac{2}{k} & n=2 k\left(k \in \mathbb{N}^{*}\right) \\ \frac{2 k+1}{k(k+1)} & n=2 k+1\left(k \in \mathbb{N}^{*}\right) .\end{cases}
$$

致谢 特此致谢付云皓老师和施奕成同学审阅了部分稿件及提出了修改意见.

## 参考文献

[1] 孙孟越等. 2017 年北大清华金秋营试题简析 [J]. 数学新星网. 学生专栏, 2017-09-22 期.

[2] K. Fan, O. Taussky and J. Todd, Discrete analoges of inequalities of wirtinger, Moratsh. Math. 59(1955), 73-90.

