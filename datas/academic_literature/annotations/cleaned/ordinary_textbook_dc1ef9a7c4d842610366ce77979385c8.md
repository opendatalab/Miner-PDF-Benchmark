# 2015 年中国西部数学邀请赛 

王广廷

(上海中学, 200231)

1. 给定正整数 $n$, 实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{k=1}^{n} x_{k}$ 为整数. 记 $d_{k}=\min _{m \in \mathbb{Z}} \mid x_{k}-$ $m \mid, 1 \leq k \leq n$. 求 $\sum_{k=1}^{n} d_{k}$ 的最大值.

(冷岗松 供题)

解法一 不妨设 $x_{1}, x_{2}, \cdots, x_{n}$ 均属于 $(0,1]$, 否则对 $x_{i}$ 做一个整数的平移变换, 不影响问题的结论. 记 $\sum_{i=1}^{n} x_{i}=t$, 则 $0 \leq t \leq n, t \in N^{*}$.

不妨设 $x_{1}, x_{2}, \cdots, x_{k} \leq \frac{1}{2}, x_{k+1}, x_{k+2}, \cdots, x_{n}>\frac{1}{2}$. 则

$$
\begin{aligned}
\sum_{k=1}^{n} d_{k} & =x_{1}+x_{2}+\cdots+x_{k}+\left(1-x_{k+1}\right)+\cdots+\left(1-x_{n}\right) \\
& =2\left(x_{1}+x_{2}+\cdots+x_{k}\right)+n-k-t,
\end{aligned}
$$

注意到

$$
x_{1}+x_{2}+\cdots+x_{k} \leq \frac{k}{2}, x_{1}+x_{2}+\cdots+x_{k}=t-\left(x_{k+1}+\cdots+x_{n}\right) \leq t-\frac{n-k}{2}
$$

故

$$
\begin{aligned}
\sum_{k=1}^{n} d_{k} & \leq \min \{k, 2 t-n+k\}+n-k-t \\
& =\min \{n-t, t\} \leq\left[\frac{n}{2}\right]
\end{aligned}
$$

当 $n$ 为奇数时, 取 $x_{1}=x_{2}=\cdots=x_{n-1}=\frac{1}{2}, x_{n}=0$, 当 $n$ 为偶数时, 取 $x_{1}=x_{2}=\cdots=x_{n}=\frac{1}{2}$, 有 $\sum_{i=1}^{n} d_{i}=\left[\frac{n}{2}\right]$.

综上可知, 所求最大值为 $\left[\frac{n}{2}\right]$.

解法二 注意到 $d_{i}+\left|\frac{1}{2}-\left\{x_{i}\right\}\right|=\frac{1}{2}$, 故 $\sum_{i=1}^{n}\left|\frac{1}{2}-\left\{x_{i}\right\}\right|=\frac{n}{2}-\sum_{i=1}^{n} d_{i}$, 因此,

$$
\sum_{i=1}^{n} d_{i}=\frac{n}{2}-\sum_{i=1}^{n}\left|\frac{1}{2}-\left\{x_{i}\right\}\right|
$$

令 $f(x)=\sum_{i=1}^{n}\left|\frac{1}{2}-\left\{x_{i}\right\}\right|$, 考虑 $f(x)$ 的最小值. 由 $\sum_{i=1}^{n}\left\{x_{i}\right\}=\sum_{i=1}^{n} x_{i}-\sum_{i=1}^{n}\left[x_{i}\right] \in \mathbb{Z}$ 可

(1) 当 $n$ 为偶数时,

$$
f(x)=\sum_{i=1}^{n}\left|\frac{1}{2}-\left\{x_{i}\right\}\right| \geq\left|\frac{n}{2}-\sum_{i=1}^{n}\left\{x_{i}\right\}\right| \geq 0
$$

取 $x_{1}=x_{2}=\cdots=x_{n}=\frac{1}{2}$, 则 $f(x)=0$, 此时 $\sum_{i=1}^{n} d_{i}=\frac{n}{2}=\left[\frac{n}{2}\right]$.

(2) 当 $n$ 为奇数时,

$$
f(x)=\sum_{i=1}^{n}\left|\frac{1}{2}-\left\{x_{i}\right\}\right| \geq\left|\frac{n}{2}-\sum_{i=1}^{n}\left\{x_{i}\right\}\right|=\left|\frac{1}{2}+m\right| \geq \frac{1}{2}
$$

其中 $m$ 是一个整数. 当取 $x_{1}=x_{2}=\cdots=x_{n-1}=\frac{1}{2}, x_{n}=0$ 时, $f(x)=\frac{1}{2}$. 此时 $\sum_{i=1}^{n} d_{i}=\frac{n}{2}-\frac{1}{2}=\left[\frac{n}{2}\right]$.

综上可知, 所求最大值为 $\left[\frac{n}{2}\right]$.

2. 如图, 圆 $\omega_{1}$ 与圆 $\omega_{2}$ 内切于点 $T . M, N$ 是圆 $\omega_{1}$ 上不同于 $T$ 的不同两点.圆 $\omega_{2}$ 的两条弦 $A B, C D$ 分别为过 $M, N$. 证明: 若线段 $A C, B D, M N$ 交于同一点 $K$. 求证: $T K$ 平分 $\angle M T N$.

(羊明亮 供题)


证明 分别延长 $T M, T N$ 交圆 $\omega_{2}$ 于点 $E$. 连接 $E F$, 从而 $M N / / E F$. 于是

$$
\frac{T M}{T N}=\frac{M E}{N F}
$$

故由相交弦定理,

$$
\frac{T M^{2}}{T N^{2}}=\frac{T M}{T N} \cdot \frac{M E}{N F}=\frac{A M \cdot M B}{D N \cdot N C}
$$

在 $\triangle A M K$ 和 $\triangle D N K$ 中, 由正弦定理知

$$
\frac{A M}{\sin \angle A K M}=\frac{M K}{\sin \angle M A K}, \quad \frac{D N}{\sin \angle D K N}=\frac{K N}{\sin \angle K D N}
$$

注意到 $\angle M A K=\angle B A C=\angle B D C=\angle K D N$, 于是

$$
\frac{A M}{D N}=\frac{M K \cdot \sin \angle A K M}{N K \cdot \sin \angle D K N}
$$

同理可知

$$
\frac{M B}{N C}=\frac{M K \cdot \sin \angle M K B}{N K \cdot \sin \angle N K C}
$$

从而

$$
\frac{A M \cdot M B}{D N \cdot N C}=\frac{M K^{2}}{N K^{2}}
$$

由(1),(2) 知

$$
\frac{T M^{2}}{T N^{2}}=\frac{M K^{2}}{N K^{2}}
$$

即

$$
\frac{T M}{T N}=\frac{M K}{N K}
$$

故 $T K$ 平分 $\angle M T N$.

3. 设整数 $n \geq 2$, 正实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{i=1}^{n} x_{i}=1$. 证明:

$$
\left(\sum_{i=1}^{n} \frac{1}{1-x_{i}}\right)\left(\sum_{1 \leq i<j \leq n} x_{i} x_{j}\right) \leq \frac{n}{2}
$$

(羊明亮, 牟晓生 供题)

解法一 不妨设 $0<x_{1} \leq x_{2} \leq \cdots \leq x_{n} \leq 1$. 注意到

$$
2 \sum_{1 \leq i<j \leq n} x_{i} x_{j}=\sum_{i=1}^{n} x_{i} \sum_{1 \leq i<j \leq n} x_{j}=\sum_{i=1}^{n} x_{i}\left(1-x_{i}\right)
$$

故原不等式等价于

$$
\left(\sum_{i=1}^{n} \frac{1}{1-x_{i}}\right)\left(\sum_{i=1}^{n} x_{i}\left(1-x_{i}\right)\right) \leq n
$$

因为对任意 $1 \leq i<j \leq n$, 有 $x_{i}+x_{j} \leq 1,0<x_{i}<x_{j} \leq 1$, 从而 $\left(x_{i}-x_{j}\right)\left(1-x_{i}-x_{j}\right) \leq 0$, 故 $x_{i}\left(1-x_{i}\right) \leq x_{j}\left(1-x_{j}\right)$. 于是

$$
x_{1}\left(1-x_{1}\right) \leq x_{2}\left(1-x_{2}\right) \leq \cdots \leq x_{n}\left(1-x_{n}\right) .
$$

又 $\frac{1}{1-x_{1}} \leq \frac{1}{1-x_{2}} \leq \cdots \leq \frac{1}{1-x_{n}}$, 由 Chebyshev 不等式得

$$
\frac{1}{n}\left(\sum_{i=1}^{n} \frac{1}{1-x_{i}}\right)\left(\sum_{i=1}^{n} x_{i}\left(1-x_{i}\right)\right) \leq\left(\sum_{i=1}^{n}\left(\frac{1}{1-x_{i}}\right) x_{i}\left(1-x_{i}\right)\right)=1 .
$$

所以 $(*)$ 成立, 从而原不等式成立.

解法二 先证局部不等式: 对任意 $1 \leq k \leq n$, 有

$$
\left(2 \sum_{1 \leq i<j \leq n} x_{i} x_{j}\right)\left(\frac{1}{1-x_{k}}\right) \leq 2 x_{k}+\frac{n-2}{n-1} \sum_{i \neq k} x_{i}
$$

事实上, 由均值不等式 $\sum_{i \neq k} x_{i}^{2} \geq \frac{2}{n-2} \sum_{i, j \neq k} x_{i} x_{j}$, 可得

$$
2 \sum_{1 \leq i<j \leq n ; i, j \neq k} x_{i} x_{j} \leq \frac{n-2}{n-1}\left(\sum_{i \neq k} x_{i}\right)^{2} .
$$

从而

$$
\begin{aligned}
\left(2 \sum_{1 \leq i<j \leq n} x_{i} x_{j}\right)\left(\frac{1}{1-x_{k}}\right) & =\left(2 x_{k}\left(1-x_{k}\right)+2 \sum_{1 \leq i<j \leq n ; i, j \neq k} x_{i} x_{j}\right)\left(\frac{1}{1-x_{k}}\right) \\
& =2 x_{k}+\frac{2 \sum_{i \neq j \neq k} x_{i} x_{j}}{\sum_{i \neq k} x_{i}} \\
& \leq 2 x_{k}+\frac{n-2}{n-1} \sum_{i \neq k} x_{i} .
\end{aligned}
$$

所以 $(*)$ 式成立.

回到原题, 对 $(*)$ 式两边的 $k=1,2, \cdots, n$ 求和知原不等式成立.

4. 对平面上有 100 条直线. 用 $T$ 表示由这些直线中的某三条直线围成的直角三角形的集合. 求 $|T|$ 的最大值.

(邹瑾 供题)

解 $|T|_{\max }=62500$.

先证明直角三角形的个数不超过 62500 .

任取一条直线, 将所有与之平行的直线组成的集合记为 $A_{1}$ (包括这条直线本身), 所有与之垂直的直线组成的集合记为 $B_{1}$ (若不存在直线与之垂直, 则 $\left.B_{1}=\emptyset\right)$. 此时从剩下的直线中任取一条, 将所有与之平行的直线的集合记为 $A_{2}$, 所有与之垂直的直线组成的集合记为 $B_{2}$. 再考虑剩下的直线, 类似定义 $A_{3}, B_{3}, \cdots$. 于是这 100 条直线被分成彼此不交的集合 $A_{1}, B_{1}, A_{2}, B_{2}, \cdots, A_{k}, B_{k}$.

设 $\left|A_{i}\right|=a_{i},\left|B_{i}\right|=b_{i}(1 \leq i \leq k)$, 则 $\sum_{i=1}^{k}\left(a_{i}+b_{i}\right)=100$.

注意每个直角三角形的三边必为一组互相垂直的直线和另一条与前者不平行或垂直的直线, 故所有直角三角形的总个数不超过 $\sum_{i=1}^{k} a_{i} b_{i}\left(100-a_{i}-b_{i}\right)$. 而

$$
\begin{aligned}
\sum_{i=1}^{k} a_{i} b_{i}\left(100-a_{i}-b_{i}\right) & \leq \sum_{i=1}^{k} \frac{\left(a_{j}+b_{j}\right)^{2}}{4} \cdot\left(100-a_{i}-b_{i}\right) \\
& =\frac{1}{4} \sum_{i=1}^{k}\left(a_{i}+b_{i}\right) \cdot\left[\left(a_{i}+b_{i}\right)\left(100-a_{i}-b_{i}\right)\right] \\
& \leq \frac{1}{4} \sum_{i=1}^{k}\left(a_{i}+b_{i}\right) \cdot \frac{\left[\left(a_{i}+b_{i}\right)+\left(100-a_{i}-b_{i}\right)\right]^{2}}{4}
\end{aligned}
$$

$$
\begin{aligned}
& =625 \cdot \sum_{i=1}^{k}\left(a_{i}+b_{i}\right) \\
& =62500 .
\end{aligned}
$$

下面给出 62500 个直角三角形的具体构造.

在坐标平面上取 100 条直线分别为 $x=1, x=2, \cdots, x=25 ; y=1, y=$ $2, \cdots, y=25 ; y=x+26, y=x+27, \cdots, y=x+50 ; y=-x+101, y=$ $-x+102, \cdots, y=-x+125$. 此时, 这 100 条直线分为 4 组, 每组 25 条相互平行, 倾斜角分别为 $0^{\circ}, 45^{\circ}, 90^{\circ}, 135^{\circ}$. 易知前两组直线相互垂直, 后两组直线也相互垂直, 且任意三线不共点. 故此时直角三角形的总个数等于 $25 \times 25 \times 50+25 \times 25 \times 50=62500$.

综上, 所求最大值为 62500 .

5. 设凸四边形 $A B C D$ 的面积为 $S, A B=a, B C=b, C D=c, D A=d$. 证明: 对 $a, b, c, d$ 的任意一个排列 $x, y, z, w$, 有

$$
S \leq \frac{1}{2}(x y+z w)
$$

(冯志刚 供题)

证明 凸四边形 $A B C D$ 的边长 $a, b, c, d$ 的排列有 $4 !=24$ 种, 事实上由边长 $x, y$ 是否相邻, 我们只须考虑如下两种情况:

(1) 若 $x, y$ 是凸四边形 $A B C D$ 的相邻的两边长, 不失一般性, 只须证明 $S \leq \frac{1}{2}(a b+c d)$. 注意到

$S_{\triangle A B C}=\frac{1}{2} A B \cdot B C \sin \angle A B C \leq \frac{1}{2} a b, \quad S_{\triangle C D A}=\frac{1}{2} C D \cdot D A \sin \angle C D A \leq \frac{1}{2} c d$,故 $S=S_{\triangle A B C}+S_{\triangle C D A} \leq \frac{1}{2}(a b+c d)$.

(2) 若 $x, y$ 是凸四边形 $A B C D$ 的两相对边的长, 只须证明 $S \leq \frac{1}{2}(a c+b d)$.设点 $A$ 关于 $B D$ 的中垂线的对称点为 $A^{\prime}$. 则

$$
\begin{aligned}
S_{A B C D}=S_{A^{\prime} B C D} & =S_{A^{\prime} B C}+S_{C D A^{\prime}} \\
& \leq \frac{1}{2} A^{\prime} B \cdot B C+\frac{1}{2} C D \cdot D A^{\prime} \\
& =\frac{1}{2} A D \cdot B C+\frac{1}{2} C D \cdot A B \\
& =\frac{1}{2}(a c+b d) .
\end{aligned}
$$

由 (1),(2) 可知原问题成立.
注 当 $x, y$ 是凸四边形 $A B C D$ 的两相对边的长时, 可以用 Ptolmey 不等式证明结论成立, 事实上

$S=S_{A B C D}=\frac{1}{2} A C \cdot B D \sin \theta \leq \frac{1}{2} A C \cdot B D \leq \frac{1}{2}(A B \cdot C D+B C \cdot D A)=\frac{1}{2}(a c+b d)$.

6. 对数列 $a_{1}, a_{2}, \cdots, a_{m}$, 定义集合 $A=\left\{a_{i} \mid 1 \leq i \leq m\right\}, B=\left\{a_{i}+2 a_{j} \mid\right.$ $1 \leq i, j \leq m, i \neq j\}$. 设 $n$ 为给定的大于 2 的整数, 对所有由正整数组成的严格递增的等差数列 $a_{1}, a_{2}, \cdots, a_{n}$, 求集合 $A \triangle B$ 的元素个数的最小值. 其中 $A \triangle B=(A \cup B) \backslash(A \cap B)$.

(王广廷 供题)

解 当 $n=3$ 时, 所求最小值为 5 ; 当 $n \geq 4$ 时, 所求最小值为 $2 n$.

引理 当 $n \geq 4$ 时, 对公差为 $d$ 的等差数列 $a_{1}, a_{2}, \cdots, a_{n}$, 有 $B=\left\{3 a_{1}+k d \mid\right.$ $1 \leq k \leq 3 n-4, k \in \mathbb{Z}\}$.

事实上, 对任意 $1 \leq i, j \leq n, i \neq j$, 有

$$
a_{i}+2 a_{j}=3 a_{1}+(i-1) d+2(j-1) d=3 a_{1}+(i+2 j-3) d,
$$

而 $1 \leq i+2 j-3 \leq 3 n-4$, 因此有 $B \subseteq\left\{3 a_{1}+k d \mid 1 \leq k \leq 3 n-4, k \in \mathbb{Z}\right\}$.

另一方面, 对 $1 \leq k \leq 3 n-4$, 可以证明存在 $1 \leq i, j \leq n, i \neq j$, 使得 $i+2 j-3=k$.

(1) 当 $k \geq 2 n-2$ 时, 取 $i=k+3-2 n, j=n$, 有 $1 \leq i \leq n-1<j=n$, 且 $i+2 j-3=k ;$

(2) 当 $k \leq 2 n-3$ 时, 且 $k$ 为偶数时, 取 $i=1, j=\frac{k+2}{2}$, 有 $1=i<j<n$, 且 $i+2 j-3=k$;

(3) 当 $5 \leq k \leq 2 n-3$, 且 $k$ 为奇数时, 取 $i=2, j=\frac{k+1}{2}$, 有 $1<i<j<n$, 且 $i+2 j-3=k ;$

(4) 当 $k=1$ 时, 取 $i=2, j=1$; 当 $k=3$ 时, 取 $i=4, j=1$.

由上面的讨论, 可知总存在 $1 \leq i, j \leq n, i \neq j$ 使得 $i+2 j-3=k$. 于是有 $\left\{3 a_{1}+k d \mid 1 \leq k \leq 3 n-4, k \in \mathbb{Z}\right\} \subseteq B$.

引理得证.

回到原题, 先讨论 $n \geq 4$ 的情形.

设由正整数组成的等差数列 $a_{1}, a_{2}, \cdots, a_{n}$ 严格递增, 即公差 $d>0$. 显然有 $|A|=n$. 由引理可知 $B=\left\{3 a_{1}+k d \mid 1 \leq k \leq 3 n-4, k \in \mathbb{Z}\right\}$, 于是 $|B|=3 n-4$.又由 $a_{2}=a_{1}+d<3 a_{1}+d$ 可知 $a_{1}, a_{2}$ 不属于 $B$, 于是 $|A \cap B| \leq n-2$. 因此有
$|A \triangle B|=|A|+|B|-2|A \cap B| \geq n+(3 n-4)-2(n-2)=2 n$.

另一方面, 当等差数列为 $1,3,5 \cdots, 2 n-1$ 时, 有 $A=\{1,3,5, \cdots, 2 n-1\}$,而由引理可得 $B=\{5,7, \cdots, 6 n-5\}$, 此时有 $|A \triangle B|=2 n$.

当 $n=3$ 时, 设 $a_{1}, a_{2}, a_{3}$ 为正整数组成的严格递增等差数列, 则 $|A|=3$.由 $2 a_{1}+a_{2}<2 a_{1}+a_{3}<2 a_{3}+a_{1}<2 a_{3}+a_{2}$ 可知 $|B| \geq 4$, 又由 $a_{1}, a_{2}$ 不属于 $B$ 可知 $|A \cap B| \leq 1$, 因此 $|A \triangle B| \geq 5$. 另一方面, 当 $a_{1}=1, a_{2}=3, a_{3}=5$ 时, $A=\{1,3,5\}, B=\{5,7,11,13\},|A \triangle B|=5$. 由此即得 $|A \triangle B|$ 的最小值为 5 .

综上所述, 当 $n=3$ 时, 所求最小值为 5 ; 当 $n \geq 4$ 时, 所求最小值为 $2 n$.

7. 设 $a \in(0,1), f(z)=z^{2}-z+a, z \in \mathbb{C}$. 证明: 对任意满足 $|z| \geq 1$ 的复数 $z$, 存在满足 $\left|z_{0}\right|=1$ 的复数 $z_{0}$, 使得 $\left|f\left(z_{0}\right)\right| \leq f(z)$.

( 张新泽 供题)

证明 先我们证明如下引理:

引理 若复数 $z$ 在单位圆外, 则存在模为 1 的复数 $z_{0}$, 对单位圆内的任意复数 $\omega$ 有 $\left|z_{0}-\omega\right|<|z-\omega|$.

事实上, 令 $z_{0}=\frac{z}{|z|}$, 则 $Z_{0}$ 是 $Z$ 与圆心 $O$ 的连线段与圆的交点. 注意到 $\omega$ 在圆的内部, 则 $|\omega|<1=\left|z_{0}\right|$, 故 $\angle O Z_{0} W<90^{\circ}, \angle W Z_{0} Z>90^{\circ}$. 这里 $Z_{0}, W, Z$ 是以 $O$ 为原点的复平面上复数 $z_{0}, w, z$ 对应的点. 因此, $\left|z_{0}-\omega\right|<|z-\omega|$.

回到原题, 我们先证明 $f(z)$ 的两根在单位圆内.

下面分两种情况:

(1) 当 $0<a \leq \frac{1}{4}$ 时, 因为判别式 $\triangle=1-4 a \geq 0$, 所以 $z_{1}, z_{2}$ 均为实数, 于是由韦达定理知 $z_{1}, z_{2} \in(0,1)$.

(2) 当 $\frac{1}{4}<a<1$ 时, 因为 $\triangle=1-4 a<0$, 所以 $z_{1}, z_{2}$ 互为共轭复数, 于是由韦达定理 $\left|z_{1}\right|^{2}=\left|z_{2}\right|^{2}=z_{1} z_{2}=a \in(0,1)$.

由 (1),(2) 可知 $f(z)$ 的两根 $z_{1}, z_{2}$ 均在单位圆内.

又 $|f(z)|=\left|z^{2}-z+a\right|=\mid\left(z-z_{1}\right)\left(z-z_{2}|=| z-z_{1}|| z-z_{2} \mid\right.$.

当 $|z|=1$ 时, 取 $z_{0}=z$, 则 $|f(z)|=\left|f\left(z_{0}\right)\right|$;

当 $|z|>1$ 时, 由引理知存在 $z_{0}=\frac{z}{|z|}$ 有 $\left|z_{0}-z_{1}\right|<\left|z-z_{1}\right|, z_{0}-z_{2}|<| z-z_{2} \mid$,于是 $\left|f\left(z_{0}\right)\right|<|f(z)|$.

综上可知原题成立.

8. 设 $k$ 为正整数, $n=\left(2^{k}\right)$ !, 证明: $\sigma(n)$ 至少有一个大于 $2^{k}$ 的素因子. 其中 $\sigma(n)$ 为 $n$ 的所有正约数之和.
证明 因为

$$
\begin{aligned}
\nu_{2}(n) & =\left[\frac{2^{k}}{2}\right]+\left[\frac{2^{k}}{4}\right]+\cdots+\left[\frac{2^{k}}{2^{k}}\right] \\
& =2^{k-1}+2^{k-2}+\cdots+1 \\
& =2^{k}-1,
\end{aligned}
$$

所以, $2^{2^{k}-1} \| n$.

设 $n=2^{2^{k}-1} p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{t}^{\alpha_{t}}$, 其中 $t \in N^{*}, p_{1}, p_{2}, \cdots, p_{t}$ 为互不相同的奇素数, $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{t}$ 为正整数. 从而

$$
\begin{aligned}
\sigma(n) & =\sigma\left(2^{2^{k}-1}\right) \sigma\left(p_{1}^{\alpha_{1}}\right) \cdots \sigma\left(p_{t}^{\alpha_{t}}\right) \\
& =\left(2^{2^{k}}-1\right) \cdot M \\
& =\left(2^{2^{k-1}}+1\right)\left(2^{2^{k-1}}-1\right) \cdot M
\end{aligned}
$$

其中 $M$ 为正整数. 于是 $\left(2^{2^{k-1}}+1\right) \mid \sigma(n)$.

考虑 $2^{2^{k-1}}+1$ 的任意一个因子 $p$, 则 $p$ 为奇素数. 由 Fermat 小定理, $2^{p-1} \equiv$ $1(\bmod p)$, 由 $2^{2^{k-1}} \equiv-1(\bmod p)$ 知 $2^{2^{k}} \equiv 1(\bmod p)$, 故 $2^{\operatorname{gcd}\left(2^{k}, p-1\right)} \equiv 1(\bmod p)$.

若 $2^{k} \nmid(p-1)$, 则 $\operatorname{ccd}\left(2^{k}, p-1\right) \mid 2^{k-1}$, 从而 $2^{2^{k-1}} \equiv 1(\bmod p)$, 故 $2^{2^{k-1}} \equiv 1 \equiv$ $-1(\bmod p)$, 从而 $p=2$. 这与 $p$ 为奇素数矛盾.

故 $2^{k} \mid(p-1)$, 因此 $p \geq 2^{k}+1$. 即 $\sigma(n)$ 有一个大于 $2^{k}$ 的素因子.

