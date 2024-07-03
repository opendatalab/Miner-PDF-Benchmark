数学新星网 $*$ 解答展示

www.nsmath.cn/jdzs

# 第四十八期问题征解解答与点评 

张端阳

第一题 在 $\triangle A B C$ 中, $H$ 为垂心, $M$ 为 $B C$ 的中点. $X$ 为 $A$ 的对径点, $Y$ 为 $A$关于 $M$ 的对称点. 过 $H$ 作一个圆与 $\triangle A B C$ 的外接圆交于点 $E, F$, 与 $\triangle B H C$ 的外接圆交于另一点 $K$. 作平行四边形 $A E G F$, 证明: $G, K, X, Y$ 四点共圆.

(深圳中学学生 邓博文 供题)

证明 (根据供题者的解答整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_0a72b4bbd48a6e834b97g-01.jpg?height=794&width=577&top_left_y=1251&top_left_x=745)

对 $\triangle A B C$ 的外接圆、 $\triangle B H C$ 的外接圆、四边形 $H E K F$ 的外接圆用蒙日定理, 得 $B C, H K, E F$ 交于一点, 设为 $P$.

延长 $A P$ 交 $\triangle A B C$ 的外接圆于点 $Q$, 我们证明 $G, K, Q, X, Y$ 五点共圆.

一方面, 设 $A G, A Q, A X$ 的中点分别为 $N, R, O$, 则 $N$ 也是 $E F$ 的中点, $O$ 是 $\triangle A B C$ 的外心. 因为 $O N \perp E F, O R \perp A Q, O M \perp B C$, 所以 $N, R, M$ 都在以 $O P$ 为直径的圆上. 以 $A$ 为中心作 $2: 1$ 的位似得, $G, Q, X, Y$ 共圆.
另一方面, 因为

$$
A P \cdot P Q=B P \cdot P C=H P \cdot P K
$$

所以 $A, H, Q, K$ 共圆. 由垂心的性质, $H Y$ 是 $\triangle B H C$ 外接圆的直径. 延长 $A H$ 交 $\triangle A B C$ 的外接圆于点 $Z$, 则

$$
\begin{aligned}
\angle Q K Y & =\angle H K Y-\angle Q K H=90^{\circ}-\angle Q A H \\
& =90^{\circ}-\angle Q X Z=180^{\circ}-\angle Q X Y
\end{aligned}
$$

其中最后一步用到的 $\angle Z X Y=90^{\circ}$ 由 $X Y \perp B C, X Z / / B C$ 得到, 所以 $K, Q, X, Y$共圆.

故 $G, K, Q, X, Y$ 五点共圆.

评注 (1). 也可以取 $A K$ 的中点, 直接证明其与 $N, O, M$ 共圆.

(2). 华南师大附中戴子一、彭子晋, 长沙一中张浩鹏, 北大附中王子豪, 深圳高级中学丁立轩, 广州大学附属中学何金喜, 北京一零一中学牟思特, 浏阳市新翰高中吴高旺, 䨉州二中周厸帆, 上海市华育中学龚逸晨, 上海中学杨镇, 上海市大同中学卫达, 巴蜀中学王瑜, 西工大附中杨泽宇, 镇海中学卢一端等同学也给出了本题的正确解答.

第二题 设正实数 $x, y$ 满足 $x+y<1$. 数列 $\left\{a_{n}\right\}$ 满足 $a_{1}=1, a_{2}=a, a_{n+2}=$ $x a_{n+1}+y a_{n}$. 证明: 若 $a>-y$, 则对任意正整数 $n$, 均有

$$
a_{1}+a_{2}+\cdots+a_{n}<\frac{1-x+a}{1-x-y} .
$$

(温州育英中学学生 胡俊浦 供题)

## 证明 1 (根据供题者的整理):

对 $n$ 归纳.

当 $n=1$ 时,

$$
1<\frac{1-x+a}{1-x-y} \Leftrightarrow a>-y
$$

成立.

当 $n=2$ 时,

$$
1+a<\frac{1-x+a}{1-x-y} \Leftrightarrow a>-\frac{y}{x+y}
$$

由 $a>-y$ 及 $x+y<1$ 知成立.

假设 $n$ 和 $n+1$ 时命题成立, 来看 $n+2$ 时的情形.
由归纳假设,

$$
\begin{gathered}
a_{1}+a_{2}+\cdots+a_{n}<\frac{1-x+a}{1-x-y}, \\
a_{1}+a_{2}+\cdots+a_{n}+a_{n+1}<\frac{1-x+a}{1-x-y} .
\end{gathered}
$$

因为 $x, y>0$, 所以

$$
\begin{aligned}
& y\left(a_{1}+a_{2}+\cdots+a_{n}\right)+x\left(a_{1}+a_{2}+\cdots+a_{n}+a_{n+1}\right) \\
< & y \cdot \frac{1-x+a}{1-x-y}+x \cdot \frac{1-x+a}{1-x-y}
\end{aligned}
$$

结合递推公式得,

$$
x a_{1}+a_{3}+a_{4}+\cdots+a_{n+2}<(x+y) \cdot \frac{1-x+a}{1-x-y} .
$$

故

$$
\begin{aligned}
a_{1}+a_{2}+\cdots+a_{n+2} & <(x+y) \cdot \frac{1-x+a}{1-x-y}-x+1+a \\
& =\frac{1-x+a}{1-x-y}
\end{aligned}
$$

归纳得证.

## 证明 2 (根据北大附中王子豪同学的整理):

因为 $y>0$, 所以方程 $r^{2}-x r-y=0$ 有两个不等实根 $s, t$, 不妨设 $s>t$. 由 $x+y<1$ 知 $s<1$.

易知

$$
a_{n}=\frac{a-t}{s-t} \cdot s^{n-1}-\frac{a-s}{s-t} \cdot t^{n-1},
$$

所以

$$
\begin{aligned}
a_{1}+a_{2}+\cdots+a_{n} & =\frac{a-t}{s-t}\left(1+s+\cdots+s^{n-1}\right)-\frac{a-s}{s-t}\left(1+t+\cdots+t^{n-1}\right) \\
& =\frac{a-t}{(s-t)(s-1)}\left(s^{n}-1\right)-\frac{a-s}{(s-t)(t-1)}\left(t^{n}-1\right) \\
& =b_{n}-b_{0},
\end{aligned}
$$

其中

$$
b_{n}=\frac{a-t}{(s-t)(s-1)} s^{n}-\frac{a-s}{(s-t)(t-1)} t^{n} \text {. }
$$

因为

$$
\begin{aligned}
b_{0} & =\frac{a-t}{(s-t)(s-1)}-\frac{a-s}{(s-t)(t-1)} \\
& =\frac{s+t-a-1}{(s-1)(t-1)}=\frac{x-a-1}{1-x-y} \\
& <\frac{-y-a}{1-x-y}<0,
\end{aligned}
$$

$$
\begin{aligned}
b_{1} & =\frac{(a-t) s}{(s-t)(s-1)}-\frac{(a-s) t}{(s-t)(t-1)} \\
& =\frac{s t-a}{(s-1)(t-1)}=\frac{-y-a}{1-x-y}<0
\end{aligned}
$$

又有递推公式 $b_{n+1}=x b_{n+1}+y b_{n}$ 及 $x, y>0$, 所以对任意正整数 $n$ 都有 $b_{n}<0$.

这样,

$$
a_{1}+a_{2}+\cdots+a_{n}<-b_{0}=\frac{1-x+a}{1-x-y} .
$$

评注 (1). 也可以先将命题等价地转化为: 对任意正整数 $n$ 都有 $a_{n+1}+y a_{n}>0$,再归纳证明。

(2). 本题的提出源于如下事实的一种归纳证法:

对任意正整数 $n, 1+\frac{1}{2}+\frac{1}{4}+\cdots+\frac{1}{2^{n}}<2$.

证明: $n=1$ 时显然成立. 假设 $n$ 时成立, $n+1$ 时,

$$
\begin{aligned}
1+\frac{1}{2}+\frac{1}{4} \cdots+\frac{1}{2^{n+1}} & =1+\frac{1}{2}\left(1+\frac{1}{2}+\cdots+\frac{1}{2^{n}}\right) \\
& <1+\frac{1}{2} \cdot 2=2
\end{aligned}
$$

该证法有意思的地方在于, 虽然不等式左边关于 $n$ 单调递增, 但并没有使用加强归纳.

本题将等比数列推广为二阶线性递推 (两个等比数列之和), 得到类似的结果.

(3). 北京一零一中学牟思特, 华南师大附中戴子一、彭子晋, 浏阳市新翰高中吴高旺, 嘚州二中石芷润, 上海中学杨镇, 深圳中学伍知行, 巴蜀中学王瑜, 西工大附中杨泽宇, 浙江省淳安中学徐海天等同学也给出了本题的正确解答.

第三题 对 $i \in \mathbb{N}, j \in \mathbb{Z},|j| \leq i$, 定义 $a_{i, j}$ 为 $\left(x+1+\frac{1}{x}\right)^{i}$ 的 $j$ 次项系数模 2 的最小非负剩余. 将 $a_{i, j}$ 标记在平面直角坐标系的点 $(j,-i)$ 处. 将距离为 1 的两个标 0 的点连一条边, 则 $y$ 轴右侧所有标 0 的点构成一个无限图 $G$. 证明: $G$ 是连通图.

(湖南师大附中学生 刘子昂 供题)

## 证明 (根据西工大附中杨泽宇同学的解答整理):

以下都在模 2 的意义下进行. 先证明几个结论.

(1) 对任意正整数 $k$,

$$
\left(x+1+\frac{1}{x}\right)^{2^{k}}=x^{2^{k}}+1+\frac{1}{x^{2^{k}}} \text {. }
$$

这由

$$
\left(x+1+\frac{1}{x}\right)^{2}=x^{2}+2 x+3+\frac{2}{x}+\frac{1}{x^{2}}=x^{2}+1+\frac{1}{x^{2}}
$$

及归纳法即证.

(2) $a_{i, j}=a_{i-1, j-1}+a_{i-1, j}+a_{i-1, j+1}$, 其中当 $|j|>i$ 时, 约定 $a_{i, j}=0$.

这由

$$
\left(x+1+\frac{1}{x}\right)^{i}=\left(x+1+\frac{1}{x}\right)^{i-1}\left(x+1+\frac{1}{x}\right)
$$

展开并比较系数即证.

(3) $a_{i, 0}=1$.

由对称性, $a_{i, j}=a_{i,-j}$, 所以 $a_{i, 0}=a_{i-1,-1}+a_{i-1,0}+a_{i-1,1}=a_{i-1,0}$, 再由 $a_{0,0}=1$及归纳法即证.

(4) $a_{i, i}=1$.

这由 $\left(x+1+\frac{1}{x}\right)^{i}$ 的展开式中 $x^{i}$ 为最高次项即证.

(5) 当 $i$ 是偶数, $j$ 是奇数时, $a_{i, j}=0$.

因为

$$
\left(x+1+\frac{1}{x}\right)^{i}=\sum_{k=0}^{i} \mathrm{C}_{i}^{k}\left(x+\frac{1}{x}\right)^{k}
$$

且当 $k$ 是偶数时, $\left(x+\frac{1}{x}\right)^{k}$ 的展开式中 $x$ 的指数都是偶数; 当 $k$ 是奇数时, $\mathrm{C}_{i}^{k}$ 是偶数, 由此即证.

回到原题. 若对 $j \geq 0$, 有

$$
a_{i, j}=1, a_{i, j+1}=a_{i, j+2}=\cdots=a_{i, j+k}=0, a_{i, j+k+1}=1
$$

则称其为第 $i$ 行的一个 $k-$ 连通组. 进一步, 若存在 $1 \leq h \leq k$, 使得 $a_{i+1, j+h}=0$,则称上述 $k$-连通组可以向下延伸.

由 (3),(4), 若某行中有 0 , 则必有连通组.

我们证明每个连通组必然向下延伸.

设 $a_{i, j+1}, a_{i, j+2}, \cdots, a_{i, j+k}$ 是第 $i$ 行的一个 $k-$ 连通组.

当 $k \geq 3$ 时, $a_{i, j+1}=a_{i, j+2}=a_{i, j+3}=0$, 由 $(2)$,

$$
a_{i+1, j+2}=a_{i, j+1}+a_{i, j+2}+a_{i, j+3}=0
$$

当 $k=2$ 时, $a_{i, j}=1, a_{i, j+1}=a_{i, j+2}=0, a_{i, j+3}=1$. 由 (5), $i$ 是奇数, 于是 $a_{i+1, j+1}$ 和 $a_{i+1, j+2}$ 中必有 0 . (事实上再由 (2) 可知这种情形不存在)

当 $k=1$ 时, $a_{i, j}=1, a_{i, j+1}=0, a_{i, j+2}=1$, 由 (2),

$$
a_{i+1, j+2}=a_{i, j+1}+a_{i, j+2}+a_{i, j+3}=0 .
$$

由 (1), 对任意正整数 $n, a_{2^{n}, 1}, a_{2^{n}, 2}, \cdots, a_{2^{n}, 2^{n}-1}$ 是第 $2^{n}$ 行的 $\left(2^{n}-1\right)$ - 连通组,所以 $1 \sim 2^{n}-1$ 行中的连通组都可以向下延伸至第 $2^{n}$ 行. 由此即知 $G$ 是连通图.

综上, 命题得证.

评注 (1). $y$ 轴右侧的前 16 行如下图所示:

$$
\begin{aligned}
& 1
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_0a72b4bbd48a6e834b97g-06.jpg?height=46&width=92&top_left_y=662&top_left_x=548)

$$
\begin{aligned}
& \begin{array}{lll}
0 & 1 & 1
\end{array} \\
& \begin{array}{llll}
0 & 0 & 0 & 1
\end{array} \\
& \begin{array}{lllll}
1 & 0 & 1 & 1 & 1
\end{array} \\
& \begin{array}{llllll}
0 & 0 & 0 & 1 & 0 & 1
\end{array} \\
& \begin{array}{lllllll}
1 & 0 & 1 & 1 & 0 & 1 & 1
\end{array} \\
& \begin{array}{llllllllll}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & &
\end{array} \\
& \left.\begin{array}{ccccccccc}
1 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1
\end{array}\right) \\
& \begin{array}{llllllllll}
0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 1
\end{array} \\
& \begin{array}{lllllllllll}
0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 1
\end{array} \\
& \begin{array}{llllllllllll}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1
\end{array} \\
& \begin{array}{lllllllllllll}
1 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 1 & 1 & 1
\end{array} \\
& \begin{array}{llllllllllllll}
0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1
\end{array} \\
& \begin{array}{lllllllllllllll}
0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1
\end{array} \\
& \begin{array}{llllllllllllllll}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{array}
\end{aligned}
$$

(2). 可以证明, 每个连通组的长度都是奇数.

(3). 本题的想法源自下题:

证明 $\left(x^{2}+x+1\right)^{n}$ 的展开式中至少有一项系数为偶数.

本题讨论 $\left(x+1+\frac{1}{x}\right)^{n}$ 的展开式系数模 2 构成的三角阵的几何性质, 自然联想到 $(x+1)^{n}$ 的展开式系数构成的三角阵, 即杨辉三角. 我们知道, 杨辉三角模 2 得到的数阵有很强的自相似性, 因此猜测题中的数阵也有自相似性, 这由 $a_{2^{k}+i, 2^{k}+j}=a_{i, j}\left(1 \leq i<2^{k}, j \geq 0\right)$ 可以看出.

(4). 上海中学杨镇, 华南师大附中戴子一、彭子晋, 北京一零一中学牟思特,雗州二中石芷润, 巴蜀中学王瑜等同学也给出了本题的正确解答.
第四题 设 $A_{1}, A_{2}, \cdots, A_{2022}$ 是集合 $\{1,2, \cdots, 2022\}$ 的不同子集, 满足其中任意 100 个的并集的元素个数严格大于 2001. 证明: 其中必有 21 个两两交集非空.

(长郡中学学生 李瑾波 供题)

## 证明 1 (根据华南师大附中彭子晋同学的解答整理):

对 $1 \leq i \leq 2022$, 设 $A_{1}, A_{2}, \cdots, A_{2022}$ 中有 $x_{i}$ 个含元素 $i$.

假设命题不成立, 则 $x_{i} \leq 20$,于是

$$
\left|A_{1}\right|+\left|A_{2}\right|+\cdots+\left|A_{2022}\right|=x_{1}+x_{2}+\cdots+x_{2022} \leq 20 \times 2022 \text {. }
$$

不妨设 $\left|A_{1}\right| \leq\left|A_{2}\right| \leq \cdots \leq\left|A_{2022}\right|$, 则

$$
\begin{aligned}
\left|A_{1} \cup A_{2} \cup \cdots \cup A_{100}\right| & \leq\left|A_{1}\right|+\left|A_{2}\right|+\cdots+\left|A_{100}\right| \\
& \leq \frac{100}{2022}\left(\left|A_{1}\right|+\left|A_{2}\right|+\cdots+\left|A_{2022}\right|\right) \\
& \leq \frac{100}{2022} \times 20 \times 2022=2000,
\end{aligned}
$$

与条件矛盾！

综上, 命题得证.

## 证明 2 (根据巴蜀中学王瑜同学的解答整理):

我们证明更强的结论,必有 92 个子集两两交集非空.

对 $i=1,2, \cdots, 2022$, 依次检查 $A_{i}$ 中的元素. 对于 $a \in A_{i}$, 若对其他任意 99 个子集 $A_{j_{1}}, A_{j_{2}}, \cdots, A_{j_{99}}$, 有

$$
\left|A_{j_{1}} \cup A_{j_{2}} \cup \cdots \cup A_{j_{99}} \cup\left(A_{i} \backslash\{a\}\right)\right|>2001,
$$

则令 $A_{i}^{\prime}=A_{i} \backslash\{a\}, A_{j}^{\prime}=A_{j}(j \neq i)$. 若 $A_{1}^{\prime}, A_{2}^{\prime}, \cdots, A_{2022}^{\prime}$ 中有 92 个两两交集非空,则 $A_{1}, A_{2}, \cdots, A_{2022}$ 中对应的 92 个两两交集非空.

设将 $A_{1}, A_{2}, \cdots, A_{2022}$ 中的所有元素检查完毕后, $A_{i}$ 剩余的元素组成 $B_{i}$. 任取 $B_{1} \cup B_{2} \cup \cdots \cup B_{2022}$ 中的一个元素 $b$, 设 $b \in B_{s}$. 因为 $b$ 不可删除, 所以存在不含 $b$ 的 99 个集合 $B_{t_{1}}, B_{t_{2}}, \cdots, B_{t_{99}}$, 使得

$$
\left|B_{t_{1}} \cup B_{t_{2}} \cup \cdots \cup B_{t_{99}} \cup B_{s}\right|=2002,
$$

这表明

$$
k:=\left|B_{t_{1}} \cup B_{t_{2}} \cup \cdots \cup B_{t_{99}}\right| \leq 2001
$$

为了记号上的简便, 不妨设 $t_{1}=1, t_{2}=2, \cdots, t_{99}=99$.

记

$$
S=\{1,2, \cdots, 2022\} \backslash\left(B_{1} \cup B_{2} \cup \cdots \cup B_{99}\right)
$$

则 $|S|=2022-k$.

对 $100 \leq i \leq 2022$, 因为

$$
\left|B_{1} \cup B_{2} \cup \cdots \cup B_{99} \cup B_{i}\right| \geq 2002
$$

所以 $\left|B_{i} \cap S\right| \geq 2002-k$.

下面证明, 存在 $S$ 中的一个元素至少属于 $B_{100}, B_{101}, \cdots, B_{2022}$ 中的 92 个. 假设不成立, 则

$$
\sum_{i=100}^{2022}\left|B_{i}\right| \leq 91|S|=91(2022-k)
$$

又

$$
\sum_{i=100}^{2022}\left|B_{i} \cap S\right| \geq 1923(2002-k)
$$

所以 $1923(2002-k) \leq 91(2022-k)$. 解得 $k>2001$, 矛盾!

综上, 命题得证.

## 证明 3 (根据供题者的解答整理):

构造图 $G: A_{1}, A_{2}, \cdots, A_{2022}$ 是顶点, 若 $A_{i} \cap A_{j} \neq \emptyset$, 则在 $A_{i}, A_{j}$ 之间连边. 本题即证图中存在 21-团.

先证明一个引理.

引理 设整数 $n \geq k \geq 3$, 若一个 $n$ 阶图中无 $k-$ 团, 则图中至少有 $\left\lceil\frac{1}{k-1} n\right\rceil+r-1$个顶点的度不超过 $\left[\frac{k-2}{k-1} n\right]$, 这里 $r$ 是 $n$ 模 $k-1$ 的最小正余数.

证明 设 $n=q(k-1)+r_{0}\left(0 \leq r_{0} \leq k-2, q \in \mathbb{N}_{+}\right)$.

(1) 若 $k-1 \mid n$, 则

$$
r_{0}=0, r=k-1,\left\lceil\frac{1}{k-1} n\right\rceil+r-1=q+k-2,\left[\frac{k-2}{k-1} n\right]=q(k-2)
$$

假设结论不成立, 则至少有 $n-(q+k-2)+1=q(k-2)-k+3$ 个顶点的度不小于 $q(k-2)+1$, 记它们构成集合 $S$.

下面对 $t$ 归纳证明, 对任意 $1 \leq t \leq k-2$, 存在 $v_{1}, v_{2}, \cdots, v_{t} \in S$, 它们两两相邻, 且

$$
\left|\left(\bigcap_{i=1}^{t} N\left(v_{i}\right)\right) \cap S\right| \geq q(k-t-2)-k+t+3
$$

当 $t=1$ 时, 任取 $v_{1} \in S$, 则

$$
\begin{aligned}
\left|N\left(v_{1}\right) \cap S\right| & =\left|N\left(v_{1}\right)\right|+|S|-\left|N\left(v_{1}\right) \cup S\right| \\
& \geq(q(k-2)+1)+(q(k-2)-k+3)-q(k-1) \\
& =q(k-3)-k+4
\end{aligned}
$$

结论成立.

假设 $t$ 时成立, 其中 $1 \leq t \leq k-3$, 设已选定 $v_{1}, v_{2}, \cdots, v_{t}$. 则 $t+1$ 时, 由

$$
\left|\bigcap_{i=1}^{t} N\left(v_{i}\right) \cap S\right| \geq q(k-t-2)-k+t+3 \geq(k-t-2)-k+t+3=1,
$$

知可选出 $v_{t+1} \in \bigcap_{i=1}^{t} N\left(v_{i}\right) \cap S$. 此时 $v_{1}, \cdots, v_{t}, v_{t+1}$ 两两相邻, 因此只需证明

$$
\left|\bigcap_{i=1}^{t+1} N\left(v_{i}\right) \cap S\right| \geq q(k-t-3)-k+t+4
$$

事实上,

$$
\begin{aligned}
\left|\bigcap_{i=1}^{t+1} N\left(v_{i}\right) \cap S\right| & \geq\left|\bigcap_{i=1}^{t} N\left(v_{i}\right) \cap S\right|+\left|N\left(v_{t+1}\right)\right|-|V| \\
& \geq(q(k-t-2)-k+t+3)+(q(k-2)+1)-q(k-1) \\
& =q(k-t-3)-k+t+4
\end{aligned}
$$

归纳证毕.

取 $t=k-2$ 知, 存在 $k-2$ 个顶点 $v_{1}, \cdots, v_{k-2} \in S$, 它们两两相邻. 因为此时 $q(k-t-2)-k+t+3=1$, 所以可取 $v_{k-1} \in \bigcap_{i=1}^{k} N\left(v_{i}\right) \cap S$, 则

$$
\begin{aligned}
\left|\bigcap_{i=1}^{k-1} N\left(v_{i}\right)\right| & \geq(k-1)\left|N\left(v_{i}\right)\right|-(k-2)|V| \\
& \geq(k-1)(q(k-2)+1)-(k-2) q(k-1) \\
& =k-1
\end{aligned}
$$

从而存在 $v_{k} \in \bigcap_{i=1}^{k-1} N\left(v_{i}\right)$, 于是 $v_{1}, v_{2}, \cdots, v_{k}$ 两两相邻, 构成 $k-$ 团, 矛盾!

(2) 若 $k-1 \nmid n$, 设 $n=q(k-1)+r$, 则

$$
\left\lceil\frac{1}{k-1} n\right\rceil+r-1=q+r,\left[\frac{k-2}{k-1} n\right]=q(k-2)+r-1 .
$$

同样地使用反证法, 并设出 $S$. 完全类似地, 可以归纳证明, 对任意 $1 \leq t \leq k-2$,存在 $v_{1}, v_{2}, \cdots, v_{t} \in S$, 它们两两相邻, 且

$$
\left|\left(\bigcap_{i=1}^{t} N\left(v_{i}\right)\right) \cap S\right| \geq q(k-t-2)+1
$$

取 $t=k-2$, 则 $\left|\left(\bigcap_{i=1}^{k-2} N\left(v_{i}\right)\right) \cap S\right| \geq 1$. 所以可取 $v_{k-1} \in \bigcap_{i=1}^{k-2} N\left(v_{i}\right) \cap S$, 则

$$
\left|\bigcap_{i=1}^{k-1} N\left(v_{i}\right)\right| \geq(k-1)\left|N\left(v_{i}\right)\right|-(k-2)|V|
$$

$$
\begin{aligned}
& \geq(k-1)(q(k-2)+r)-(k-2)(q(k-1)+r) \\
& =r>0 .
\end{aligned}
$$

从而存在 $v_{k} \in \bigcap_{i=1}^{k-1} N\left(v_{i}\right)$, 于是 $v_{1}, v_{2}, \cdots, v_{k}$ 两两相邻, 构成 $k-$ 团, 矛盾!

引理得证.

回到原题. 若 $G$ 中没有 $21-$ 才, 由引理, $G$ 中有 $\left\lceil\frac{1}{21-1} \cdot 2022\right\rceil+2-1=103$个顶点, 设为 $A_{1}, A_{2}, \cdots, A_{103}$, 它们的度不超过 $\left[\frac{21-2}{21-1} \cdot 2022\right]=1920$. 故对任意 $1 \leq i \leq 103$, 与 $A_{i}$ 不交的集合数不少于 $2022-1920-1=101$. 由条件, 这 101 个集合的并集元素个数大于 2001 , 故 $\left|A_{i}\right| \leq 2022-2002=20$. 在 $A_{1}, A_{2}, \cdots, A_{103}$ 中任选 100 个集合求并, 其元素个数不超过 2000 , 与条件矛盾!

综上, 命题得证.

评注 (1). 本题的命题背景是:

(i) (Zarankiewica 引理) 若一个 $n$ 阶图中无 $k-$ 团, 则必有一个顶点的度不超过 $\left[\frac{k-2}{k-1} n\right]$.

(ii)（2004 年罗马尼亚国家队选拔考试）设 $A_{1}, A_{2}, \cdots, A_{101}$ 是 $\{1,2, \cdots, n\}$的不同子集, 满足其中任意 50 个的并集的元素个数严格大于 $\frac{50}{51} n$. 证明: 其中必有 3 个子集两两交集非空.

在罗马尼亚的题中, 对 Zarankiewica 引理在 $k=3$ 的情形进行了加强, 改进了度不超过 $\left[\frac{n}{2}\right]$ 的顶点个数的下界. 这引发作者思考对一般的 $k$ 能否作此推广. 经过反复尝试, 确定了这个下界大约为 $\frac{n}{k-1}$, 常数项则是通过待定系数法得出.

在改进了一般情形下的 Zarankiewica 引理后, 作者把题目改编回集合的形式,并设计了相关数据, 使题面看起来较为巧合, 且为他人提供更多做法留下思考空间。

(2). 西工大附中杨泽宇, 上海中学杨镇, 浏阳市新翰高中吴高旺, 华南师大附中戴子一, 北京一零一中学牟思特, 北大附中王子豪, 徐州市第一中学黄羽翔等同学也给出了本题的正确解答.

