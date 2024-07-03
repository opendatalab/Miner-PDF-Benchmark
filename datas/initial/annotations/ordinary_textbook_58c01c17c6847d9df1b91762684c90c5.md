# 第二十三期问题征解解答与点评 

牟晓生

第一题. 给定正整数 $n>1$. 考虑将 $n$ 分拆为若干正整数 $b_{1}, b_{2}, \ldots, b_{t}$ 的和.求所有分拆变化下

$$
S=2 \sum_{i=1}^{t} i b_{i}+\sum_{i=1}^{t} b_{i}^{2}
$$

的最小可能值.

(复旦附中 肖恩利 供题)

## 解 (根据武钢三中游阳, 李因立同学的解答整理):

首先注意到分拆只有有限个, 因此 $S$ 的最小值存在. 由排序不等式可以不妨设 $b_{1} \geq b_{2} \geq \cdots \geq b_{t}$. 记 $b_{1}=l$.

(1) 如果 $t \leq l-2$, 则可将 $\left(b_{1}, b_{2}, \ldots, b_{t}\right)$ 调整为 $\left(b_{1}-1, b_{2}, \ldots, b_{t}, 1\right), S$ 的值不增. 可以继续如此调整直到 $t=l-1$.

(2) 若 $t \leq l+1$, 则可将 $\left(b_{1}, b_{2}, \ldots, b_{t}\right)$ 调整为 $\left(b_{1}+b_{t}, b_{2}, \ldots, b_{t-1}\right), S$ 不增.

以下考虑 $t=l-1$ 或 $t=l$. 在所有使 $S$ 最小的数组中, 我们取 $b_{1}$ 为其最小可能值. 在固定 $b_{1}$ 的情况下取 $b_{2}$ 为其最小可能值. 以此类推.

再分几种情况讨论:

(3) 若存在 $i$ 使得 $b_{i}-b_{i+1} \geq 2$. 将 $b_{i}$ 减 $1, b_{i+1}$ 加 $1, S$ 的值不增. 这与前面的排序假设相矛盾!

(4) 若存在 $2 \leq i \leq t$ 使得 $b_{j} \geq l-j+3$. 将 $b_{1}$ 增加 $1, b_{j}$ 减一, $S$ 的值严格减少.

由 (4), 我们有 $b_{1}-b_{j} \geq j-2$. 而由 $(3), b_{i}-b_{i+1} \in\{0,1\}$. 因此最多存在一个 $i^{*}$ 使得 $b_{i^{*}}-b_{i^{*}+1}=0$, 而其他所有的 $i$ 满足 $b_{i}-b_{i+1}=1$. 这样结合 $\sum_{i=1}^{t} b_{i}=n$, $b_{1}=l$ 就能确定所有可能的数组 $\left(b_{1}, \ldots, b_{t}\right)$. 剩下的计算是平凡的, 我们在此略去.

评注 对于涉及整数的最值问题, 调整法是十分常用的思路.
第二题. 已知 $H$ 为锐角三角形 $A B C$ 的垂心. $D, E$ 分别是边 $A B, A C$ 上的点, 满足 $A D=A E$ 且 $D, H, E$ 共线. 延长 $D E$ 交 $\triangle A B C$ 的外接圆 $\omega$ 于 $K, L$两点. 过 $D$ 作 $A B$ 的垂线, 过 $E$ 作 $A C$ 的垂线，两条垂线交于 $N$. 延长 $H N$ 与圆 $\omega$ 上的 $B C$ 弧交于 $S$, 而 $K S, L S$ 分别与 $B C$ 交于 $X, Y$. 证明: $\triangle S X Y$ 的外接圆经过 $\triangle A B C$ 的外心.

(湖南雅礼中学学生 王子安 供题)

解 (根据杭州二中刘浩宇同学的解答整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_66166dc299c87086f0ebg-2.jpg?height=546&width=602&top_left_y=795&top_left_x=727)

如图, 过 $B, C$ 分别作 $A B, A C$ 的垂线交 $H N$ 于 $S_{1}, S_{2}$, 则

$$
\frac{H S_{1}}{N S_{1}}=\frac{H c B}{D B} ; \quad \frac{H S_{2}}{N S_{2}}=\frac{H b C}{E C}
$$

由于 $A D=A E, \angle C E H=\angle B D H$. 由此知 $\triangle C E H \sim \triangle B D H$, 得

$$
\frac{C E}{B D}=\frac{C H}{B H}
$$

而 $\triangle C H H_{b} \sim \triangle B H H_{c}$, 故我们又有

$$
\frac{C H}{B H}=\frac{H_{b} C}{H_{c} B}
$$

所以 $\frac{C E}{B D}=\frac{H_{b} C}{H_{c} B}$. 结合最初的两个等式得到

$$
\frac{H S_{1}}{N S_{1}}=\frac{H S_{2}}{N S_{2}}
$$

即 $S_{1}=S_{2}$. 由于 $S_{1} B \perp A B, S_{2} C$, 这个点就是 $A$ 在外界圆 $O$ 上的对径点, 结合 $S_{1}, S_{2}$ 在 $H N$ 上得到 $S_{1}=S_{2}=S$.

由于 $B H C S$ 是平行四边形, $H N$ 与 $B C$ 的交点 $T$ 一定是 $H S$ 的中点, 也是 $B C$ 的中点. 设 $U, V$ 分别是 $K S, L S$ 的中点, 则 $U, T, V$ 共线. 注意到 $U, T, V$ 分别是点 $O$ 在 $X S, X Y, Y S$ 上的投影, 所以由Simson定理的逆定理, $O$ 在 $\triangle X S Y$的外接圆上.
评注 华南师大附中胡苏麟, 西北师大附中杨鹏, 湖南长郡中学常杰, 浙江省镇海中学严君啸, 成都七中嘉祥外国语学校李林皓以及武钢三中游阳等同学也给出了本题的正确解答.

第三题. 设 $F(x)=\sum_{k=0}^{\infty} a_{k} \cdot x^{k}$ 是一个整系数的形式幂级数, 其中 $a_{0} \neq 0$. 而 $F^{\prime}(x)=\sum_{k=1}^{\infty} k a_{k} \cdot x^{k-1}$ 是它的导函数. 已知 $\frac{F^{\prime}(x)}{F(x)}$ 也是整系数的形式幂级数, 证明 $a_{0}$ 整除每个 $a_{k}$.

(哈佛大学 牟晓生 供题)

## 证明 (根据供题者的解答整理):

令 $b_{k}=\frac{a_{k}}{a_{0}}$. 我们有

$$
\frac{F^{\prime}(x)}{F(x)}=(\ln F(x))^{\prime}=\left(\ln \left(1+b_{1} x+b_{2} x^{2}+\cdots\right)\right)^{\prime} .
$$

设 $q(x)=-\left(b_{1} x+b_{2} x^{2}+\cdots\right)$, 则

$$
\ln F(x)=\ln (1-q(x))=-\left[\sum_{m=1}^{\infty} \frac{q(x)^{m}}{m}\right]
$$

我们将通过这些等式证明每个 $b_{k}$ 均为整数. 假设不然, 则存在某个 $k$ 以及素数 $p$ 使得 $v_{p}\left(b_{k}\right)<0$. 设

$$
w_{j}=v_{p}\left(b_{j}\right) / j, \quad \forall j
$$

并设 $\underline{w}=\min _{j} w_{j}$. 注意到最小值 $\min _{j} v_{p}\left(b_{j}\right) / j$ 是取到的. 这是因为 $v_{p}\left(b_{k}\right)<0$而每个 $v_{p}\left(b_{j}\right)$ 至少是 $-v_{p}\left(a_{0}\right)$, 所以当 $j$ 较大时必有 $v_{p}\left(b_{j}\right) / j>v_{p}\left(b_{k}\right) / k$.

下面, 我们令 $j^{*}$ 是使得 $w_{j}=\underline{w}$ 的最小下标 $j$. 取充分大的正整数 $r$,令 $N=j^{*} \cdot p^{r}$. 我们将考虑 (2) 式右边展开后 $x^{N}$ 的系数, 并求出这个系数含 $p$的幂次. 首先, 当 $m=p^{r}$ 时 $\frac{q(x)^{m}}{m}$ 的展开中有一项 $\frac{\left(b_{\left.j^{*} \cdot x^{j^{*}}\right)^{m}}^{m}\right.}{m}=\frac{\left(b_{j^{*}}\right)^{m} \cdot x^{N}}{m}$. 这一项含 $p$ 的幂次为 $v_{p}\left(b_{j^{*}}\right) \cdot m-v_{p}(m)=\underline{w} \cdot N-r$.

接下来我们证明其余所有 $x^{N}$ 的系数含 $p$ 的幂次都大于 $\underline{w} \cdot N-r$. 为此, 注意到 (2) 式右边展开后每个 $x^{N}$ 的单项式均可写为

$$
\frac{\left(b_{1} x\right)^{t_{1}} \cdot\left(b_{2} x^{2}\right)^{t_{2}} \cdots}{m} \cdot\left(\begin{array}{c}
m \\
t_{1}, t_{2}, \ldots
\end{array}\right),
$$

其中 $\sum_{j} j \cdot t_{j}=N$, 而 $\sum_{j} t_{j}=m$. 以上系数含 $p$ 的幂次为

$$
V=\sum_{j} v_{p}\left(b_{j}\right) \cdot t_{j}+v_{p}\left(\left(\begin{array}{c}
m \\
t_{1}, t_{2}, \ldots
\end{array}\right) / m\right)
$$

由假设, $v_{p}\left(b_{j}\right) \geq \underline{w} \cdot j$ 对每个 $j$ 成立. 所以当 $\sum_{j} j \cdot t_{j}=N$ 时必有 $\sum_{j} v_{p}\left(b_{j}\right) \cdot t_{j} \geq$
$\underline{w} \cdot N$. 因此, $V \leq \underline{w} \cdot N-r$ 只可能是 $v_{p}\left(\left(\begin{array}{c}m \\ t_{1}, t_{2}, \ldots\end{array}\right) / m\right) \leq-r$. 注意到

$$
\left(\begin{array}{c}
m \\
t_{1}, t_{2}, \ldots
\end{array}\right) / m=\left(\begin{array}{c}
m-1 \\
t_{1}-1, t_{2}, \ldots
\end{array}\right) / t_{1}
$$

故我们只需考虑 $p^{r} \mid t_{1}$ 的情况. 类似地我们可以假设 $p^{r}$ 整除每个 $t_{j}$. 由于 $\sum_{j} j \cdot t_{j}=N=p^{r} \cdot j^{*}$, 只有两种可能: 要么 $t_{j^{*}}=p^{r}, t_{j}=0, \forall j \neq j^{*}$, 要么 $t_{j}=$ $0, \forall j \geq j^{*}$. 前一种可能就是我们之前考虑过的那一项, 那时 $V=\underline{w} \cdot N-r$. 如果是后一种, 则由 $j^{*}$ 的最小性可知存在 $\epsilon>0$, 满足

$$
v_{p}\left(b_{j}\right) \geq(\underline{w}+\epsilon) \cdot j, \forall 1 \leq j<j^{*} .
$$

因此当 $\sum_{j=1}^{j^{*}-1} j \cdot t_{j}=N$ 时必有 $\sum_{j=1}^{j^{*}-1} v_{p}\left(b_{j}\right) \cdot t_{j} \geq(\underline{w}+\epsilon) \cdot N$. 这样由 (3) 得到

$$
V \geq(\underline{w}+\epsilon) \cdot N-v_{p}(m) \geq(\underline{w}+\epsilon) \cdot N-\log _{p}(N)
$$

对充分大的 $r$ (及 $N$ ), $V$ 严格大于 $\underline{w} \cdot N-r$.

这样我们就证明了 $\ln (F(x))$ 的展开中 $x^{N}$ 的系数含 $p$ 的幂次恰为 $\underline{w} \cdot N-r$.于是 $\frac{F^{\prime}(x)}{F(x)}$ 中 $x^{N-1}$ 的系数含 $p$ 的幕次恰为

$$
\underline{w} \cdot N-r+v_{p}(N)=\underline{w} \cdot N+v_{p}\left(j^{*}\right) .
$$

这在 $r$ (及 $N$ ) 充分大时是一个负数, 与假设 $\frac{F^{\prime}(x)}{F(x)}$ 为整系数矛盾!

于是命题得证.

第四题. $n$ 求最大的正常数 $C$, 使得对每个凸多边形 $P$ 及其任意顶点 $u$, 都能找到 $P$ 的另外两个顶点 $v, w$, 满足

$$
\operatorname{area}(\triangle u v w) \geq C \cdot \operatorname{area}(P) \text {. }
$$

(普林斯顿大学 张瑞祥 供题)

## 解 (根据供题者的解答整理):

答案是 $\frac{1}{\pi}$. 首先考虑 $P$ 是一个单位半圆, 而 $u$ 是其圆心. 此时 $\operatorname{area}(P)=\frac{\pi}{2}$,而任意包含顶点 $u$ 的三角形的面积至多是 $\frac{1}{2}$, 这说明 $C \leq \frac{1}{\pi}$. 当然, 严格来说这个例子并不符合条件, 因为单位半圆并不是多边形, 而其圆心也并不是一个顶点. 但我们可以用一系列多边形逼近 $P$, 这样仍可以证明 $C$ 至多是 $\frac{1}{\pi}$.

下面我们证明 $C=\frac{1}{\pi}$ 是可以达到的. 我们有下面的引理:

引理 设 $Q$ 是任意凸形, 而 $x$ 是其内部一点. 则存在 $Q$ 边界上的两个点 $y, z$,使得

$$
\operatorname{area}(\triangle x y z) \geq \frac{1}{2 \pi} \cdot \operatorname{area}(Q)
$$

引理的证明 由 Blaschke-Sas 定理知存在 $Q$ 内接的四边形 $a b c d$, 使得

$$
\operatorname{area}(a b c d) \geq \frac{2}{\pi} \cdot \operatorname{area}(Q) .
$$

于是 $x a b, x b c, x c d, x d a$ 这四个三角形中必有一个符合要求. Blaschke-Sas定理的陈述与证明详见下面的评注二.

回到原题. 设 $P$ 的顶点为 $u=u_{0}$ 以及 $u_{1}, \ldots, u_{n}$. 对 $0 \leq i \leq n$, 令 $v_{i}$为 $u_{i}$ 关于点 $u$ 的对称点. 则 $v_{0}, \ldots, v_{n}$ 构成一个凸多边形 $P^{\prime}$, 是 $P$ 关于点 $u$的中心对称图形. 由于 $u$ 是 $P$ 的顶点, $P^{\prime}$ 与 $P$ 只交于 $u$ 这一个点. 令 $Q$为 $u_{1}, \ldots, u_{n}, v_{1}, \ldots, v_{n}$ 的凸包, 就是 $P$ 与 $P^{\prime}$ 共同的凸包. 对 $Q$ 及其中心点 $u$应用引理, 得到两个点 $y, z \in\left\{u_{1}, \ldots, u_{n}, v_{1}, \ldots, v_{n}\right\}$ 使得

$$
\operatorname{area}(\triangle u y z) \geq \frac{1}{2 \pi} \cdot \operatorname{area}(Q) \geq \frac{1}{\pi} \cdot \operatorname{area}(P) \text {. }
$$

设 $y \in\left\{u_{i}, v_{i}\right\}, z \in\left\{u_{j}, v_{j}\right\}$, 则由对称性知

$$
\operatorname{area}\left(\triangle u u_{i} u_{j}\right)=\operatorname{area}(\triangle u y z) \geq \frac{1}{\pi} \cdot \operatorname{area}(P) \text {. }
$$

于是命题得证!

评注 (1). 解答后半部分考虑中心对称的方法是组合几何中的常用技巧. 非常困难的 IMO 2006 的最后一题也有一种解法是利用中心对称的. 有兴趣的同学还可以参考学习 Steiner 对称, 在几何不等式中的应用非常广泛.

(2). Blaschke-Sas 定理是组合几何极值领域的一个经典结果. 它说的是单位面积的凸形必定包含面积至少是 $\frac{n}{2 \pi} \cdot \sin \left(\frac{2 \pi}{n}\right)$ 的凸 $n$ 边形, 且当原凸形为椭圆时常数最佳. Blaschke 最初用 Steiner 对称的方法证明了内接三角形的情况, 而 Sas 用下面的均值方法将结论推广到 $n$ 边形:

假设我们有凸形 $Q$. 取 $A B$ 为其直径, $O$ 为 $A B$ 中点. 由于放缩并不改变结论, 我们不妨假设 $O A=O B=1$. 进一步, 由 $A B$ 是直径我们可以将 $Q$ 的边界作如下的参数描述:

$$
z(\theta)=(\cos \theta, r(\theta) \sin \theta): 0 \leq \theta<2 \pi \text {. }
$$

其中 $\theta=0$ 对应点 $A$, 而 $\theta=\pi$ 对应点 $B$. 长度 $r(\theta) \geq 0$. 对任意的 $\theta$, 考虑由 $z(\theta), z(\theta+2 \pi / n), \cdots, z(\theta+2(n-1) \pi / n)$ 构成的凸 $n$ 边形. 其面积为

$$
\begin{gathered}
\frac{1}{2} \sum_{j=0}^{n-1} \cos \left(\theta+\frac{2 j \pi}{n}\right) \cdot r\left(\theta+\frac{2(j+1) \pi}{n}\right) \cdot \sin \left(\theta+\frac{2(j+1) \pi}{n}\right) \\
-\cos \left(\theta+\frac{2(j+1) \pi}{n}\right) \cdot r\left(\theta+\frac{2 j \pi}{n}\right) \cdot \sin \left(\theta+\frac{2 j \pi}{n}\right)
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{1}{2} \sum_{j=0}^{n-1} r\left(\theta+\frac{2 j \pi}{n}\right) \sin \left(\theta+\frac{2 j \pi}{n}\right) \cdot\left[\cos \left(\theta+\frac{2(j-1) \pi}{n}\right)-\cos \left(\theta+\frac{2(j+1) \pi}{n}\right)\right] \\
& =\sin \left(\frac{2 \pi}{n}\right) \cdot \sum_{j=0}^{n-1} r\left(\theta+\frac{2 j \pi}{n}\right) \sin ^{2}\left(\theta+\frac{2 j \pi}{n}\right) .
\end{aligned}
$$

所以当 $\theta$ 从 0 增加到 $\frac{2 \pi}{n}$ 时, 这样的凸 $n$ 边形的平均面积为

$$
\frac{n}{2 \pi} \cdot \sin \left(\frac{2 \pi}{n}\right) \cdot \int_{\theta=0}^{2 \pi} r(\theta) \sin ^{2}(\theta) d \theta
$$

另一方面, 如果我们在 (4) 中令 $n \rightarrow \infty$, 则整个凸形的面积为

$$
\lim _{n \rightarrow \infty} \sin \left(\frac{2 \pi}{n}\right) \cdot \sum_{j=0}^{n-1} r\left(\theta+\frac{2 j \pi}{n}\right) \sin ^{2}\left(\theta+\frac{2 j \pi}{n}\right)=\int_{\theta=0}^{2 \pi} r(\theta) \sin ^{2}(\theta) d \theta .
$$

于是由平均原理, 必有某个内接凸 $n$ 边形的面积是整个凸形面积的 $\frac{n}{2 \pi} \cdot \sin \left(\frac{2 \pi}{n}\right)$倍. 定理得证!

## 第二十三期新星妙解名单（排名不分先后）

1. 湖北武钢三中游阳
2. 湖北武钢三中李因立
3. 浙江杭州二中刘浩宇
4. 华南师大附中 胡苏麟
5. 西北师大附中 杨 鹏
6. 浙江镇海中学 严君啸
7. 湖南长郡中学常 杰
8. 成都七中嘉祥外国语学校 李林皓
