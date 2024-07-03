# 第三十八期问题征解解答与点评 

张端阳

第一题 设 $\triangle A B C$ 为不等腰三角形, $O, H$ 分别为其外心与垂心, 直线 $O H$与 $A C, A B$ 分别交于点 $E, F$. 令 $\odot O$ 为 $\triangle A B C$ 的外接圆, 它与 $\triangle A E F$ 的外接圆 $\odot S$ 交于除 $A$ 外的另一点 $J$. 再设 $\triangle J S O$ 的外接圆与 $\odot O$ 交于 $J, K$ 两点,而与直线 $O H$ 交于 $O, D$ 两点. 直线 $D K$ 与 $\odot O$ 交于 $G, K$ 两点, 直线 $J K$ 与 $O H$ 交于 $M$. 求证: 过 $G, H, M$ 的圆与 $\odot O$ 相切.

(兰州一中学生 郝敏言 供题)

证明 (根据供题者的解答整理):



先证明 $H J \perp J D$.

延长 $O H 、 B C$ 交于点 $P$, 则 $J$ 是完全四边形 $A B C F E P$ 的密克点, 于是 $J, E, C, P$ 共圆. 延长 $A H$ 交 $\odot O$ 于点 $Q$, 则 $Q$ 与 $H$ 关于 $B C$ 对称. 因为

$$
\angle J P E=\angle J C E=\angle J Q A,
$$

所以 $J, P, Q, H$ 共圆. 这样,

$$
\angle J H D=\angle J Q P=\angle A Q P-\angle J Q A=\angle Q H P-\angle J P H .
$$

又

$$
\begin{aligned}
\angle J D H & =180^{\circ}-\angle O S J=90^{\circ}-\angle A J S=\angle A E J \\
& =\angle J C E+\angle E J C=\angle J P H+\angle E P C
\end{aligned}
$$

故

$$
\angle J H D+\angle J D H=\angle Q H P+\angle E P C=90^{\circ},
$$

即 $H J \perp J D$.



回到原题. 因为

$$
\angle J D G=180^{\circ}-\angle J O K=180^{\circ}-2 \angle J G D,
$$

所以 $D J=D G$. 又 $O J=O G$, 所以 $J$ 与 $G$ 关于直线 $O D$ 对称.

延长 $G M$ 交 $\odot O$ 于点 $X$, 则 $X$ 与 $K$ 关于直线 $O D$ 对称, 所以 $X K \perp O D$.

延长 $G H$ 交 $\odot O$ 于点 $Y$, 结合 $H J \perp J D$ 得,

$$
\angle Y X K=\angle Y G K=180^{\circ}-\angle H G D=180^{\circ}-\angle H J D=90^{\circ} \text {, }
$$

即 $X K \perp Y X$.

于是 $Y X / / O D$, 即 $Y X / / H M$, 故过 $G, H, M$ 的圆与 $\odot O$ 相切.

评注 (1). 北京大学刘云冲同学用的复数法, 他依次算出

$$
\begin{gathered}
E=\frac{A+C}{1+A C}, \quad F=\frac{A+B}{1+A B}, \quad S=\frac{A(1+A B+B C+C A)}{(1+A B)(1+A C)} \\
J=\frac{1+A B+B C+C A}{A+B+C+A B C}, \quad K=A B C, \quad G=\frac{A+B+C+A B C}{1+A B+B C+C A} .
\end{gathered}
$$

(2). 成都树德中学何雨航, 长沙市南雅中学石育锟, 杭州学军中学叶梓、
郑思源, 雅礼中学温玟杰, 温州育英国际实验学校林逸沿, 温州中学金晟治, 华东师大二附中王一川等同学也给出了本题的正确解答.

第二题 将一个 $n \times n$ 的白色方格表中的 $n$ 个格子染成黑色. 证明: 存在至少 $\left(\begin{array}{l}n \\ 2\end{array}\right)$ 个白格, 它们彼此之间通过公共边形成连通分支.

(重庆南开中学学生 伍样圳 供题)

## 证明 (根据供题者的解答整理):

分两种情形讨论.

情形 1 : 有一行和一列 (记作 $L$ ) 中没有黑格.

设 $L$ 所在的连通分支为 $T$.

方格表除 $L$ 外被分为四个部分 $A_{1}, A_{2}, A_{3}, A_{4}$ (可能有的部分为空). 对 $1 \leq i \leq 4$, 设 $A_{i}$ 中有 $a_{i}$ 个黑格. 下面证明, $A_{i}$ 中不属于 $T$ 的白格至多有 $\left(\begin{array}{c}a_{i} \\ 2\end{array}\right)$ 个.

事实上, 对 $A_{i}$ 中不属于 $T$ 的一个白格 $B$, 设 $L$ 中与 $B$ 同行和同列的格分别为 $X, Y$, 则 $B, X$ 之间且与它们同行的格中必有黑格, $B, Y$ 之间且与它们同列的格中也必有黑格. 从而 $A_{i}$ 中不属于 $T$ 的一个白格对应了 $A_{i}$ 中的两个不同的黑格. 又不会有两个白格对应到同一对黑格 (否则这两个白格既同行也同列, 因而是同一个), 故 $A_{i}$ 中不属于 $T$ 的白格的个数不多于 $A_{i}$ 中黑格对的个数 $\left(\begin{array}{c}a_{i} \\ 2\end{array}\right)$.

从而 $T$ 中白格数不少于

$$
n^{2}-n-\sum_{i=1}^{4}\left(\begin{array}{c}
a_{i} \\
2
\end{array}\right) \geq n^{2}-n-\left(\begin{array}{l}
n \\
2
\end{array}\right)=\left(\begin{array}{l}
n \\
2
\end{array}\right)
$$

情形 2: (不妨) 每列中均有黑格.

因为黑格共有 $n$ 个, 所以每列中恰有一个黑格.

若存在相邻两列, 其中的黑格没有公共点, 则这两列中的 $2(n-1)$ 个白格属于同一个连通分支 $T$. 由每列中恰有一个黑格, 知当一列中有 $x$ 个白格属于 $T$时, 其相邻的列中至少有 $x-1$ 个白格属于 $T$. 从而 $T$ 中白格数不少于

$$
2(n-1)+(n-2)+(n-3)+\cdots+1>\left(\begin{array}{l}
n \\
2
\end{array}\right) \text {. }
$$

下设任意相邻两列的黑格都有公共点.

若第一行和最后一行中没有黑格, 则全部白格被分为上下两个连通分支, 必有一个中的白格数不少于 $\left(\begin{array}{l}n \\ 2\end{array}\right)$.

若 (不妨) 第一行中有黑格, 则其下方的 $n-1$ 个白格属于同一个连通分支 $T$. 同上面的论证, $T$ 中白格数不少于

$$
(n-1)+(n-2)+\cdots+1+0=\left(\begin{array}{l}
n \\
2
\end{array}\right) \text {. }
$$

综上, 命题得证.

评注 杭州学军中学黄行睿, 雅礼中学温斑杰, 麓山国际实验学校童吴阳,温州中学金晟治, 华东师大二附中王一川等同学也给出了本题的正确解答.

第三题 设 $a_{i}, b_{i}(1 \leq i \leq n)$ 为实数, 满足 $a_{i} \geq 0$ 且 $\sum_{i=1}^{n} a_{i}=1$. 证明:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{n} \sum_{l=1}^{n}\left|b_{i}+b_{j}+b_{k}+b_{l}\right| \cdot a_{i} a_{j} a_{k} a_{l} \geq \sum_{i=1}^{n}\left|b_{i}\right| \cdot a_{i}
$$

(北京大学学生 张江昊 供题)

## 证明 (根据供题者的解答整理):

先证明二维情形

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left|b_{i}+b_{j}\right| \cdot a_{i} a_{j} \geq \sum_{i=1}^{n}\left|b_{i}\right| \cdot a_{i}
$$

设 $b_{i}=c_{i} d_{i}$, 其中 $d_{i}=\left|b_{i}\right|, c_{i}= \pm 1$, 则只需证明

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left|c_{i} d_{i}+c_{j} d_{j}\right| \cdot a_{i} a_{j} \geq \sum_{i=1}^{n} d_{i} a_{i}
$$

先证明局部不等式

$$
\left|c_{i} d_{i}+c_{j} d_{j}\right| \geq \frac{1}{2}\left(d_{i}+d_{j}\right)+c_{i} c_{j} \sqrt{d_{i} d_{j}}
$$

事实上, 当 $c_{i}, c_{j}$ 同号时, 即证 $\frac{1}{2}\left(d_{i}+d_{j}\right) \geq \sqrt{d_{i} d_{j}}$, 显然成立.

当 $c_{i}, c_{j}$ 异号时, 不妨设 $d_{i} \geq d_{j}$, 则即证 $d_{i}-d_{j} \geq \frac{1}{2}\left(\sqrt{d_{i}}-\sqrt{d_{j}}\right)^{2}$, 这等价于 $2\left(\sqrt{d_{i}}+\sqrt{d_{j}}\right) \geq \sqrt{d_{i}}-\sqrt{d_{j}}$, 也成立.

这样,

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n}\left|c_{i} d_{i}+c_{j} d_{j}\right| \cdot a_{i} a_{j} & \geq \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\frac{1}{2}\left(d_{i}+d_{j}\right)+c_{i} c_{j} \sqrt{d_{i} d_{j}}\right) a_{i} a_{j} \\
& =\left(\sum_{i=1}^{n} d_{i} a_{i}\right)\left(\sum_{j=1}^{n} a_{j}\right)+\left(\sum_{i=1}^{n} c_{i} \sqrt{d_{i}} a_{i}\right)^{2} \\
& \geq \sum_{i=1}^{n} d_{i} a_{i} .
\end{aligned}
$$

回到原题. 因为

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i} a_{j}=\left(\sum_{i=1}^{n} a_{i}\right)^{2}=1
$$

所以先对 $n^{2}$ 个变量 $a_{i} a_{j}$ 与 $b_{i}+b_{j}(1 \leq i, j \leq n)$ 用二维情形, 再直接用二维情形
得,

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{n} \sum_{l=1}^{n}\left|\left(b_{i}+b_{j}\right)+\left(b_{k}+b_{l}\right)\right| \cdot\left(a_{i} a_{j}\right)\left(a_{k} a_{l}\right) \\
\geq & \sum_{i=1}^{n} \sum_{j=1}^{n}\left|b_{i}+b_{j}\right| \cdot a_{i} a_{j} \geq \sum_{i=1}^{n}\left|b_{i}\right| \cdot a_{i} .
\end{aligned}
$$

综上, 命题得证.

评注 (1). 在二维情形中取 $a_{1}=a_{2}=\cdots=a_{n}=\frac{1}{n}$, 即得到 2006 年伊朗国家队选拔考试第四题.

(2). 二维情形也可以通过对 $b_{1}, b_{2}, \cdots, b_{n}$ 正负分离来证明.

(3). 南开大学唐梓洲教授指出, 二维情形对复数 $b_{1}, b_{2}, \cdots, b_{n}$ 也成立. 证明思想同原证明相近, 事实上, 设 $b_{i}=c_{i} d_{i}$, 其中 $d_{i}=\left|b_{i}\right|,\left|c_{i}\right|=1$, 关键的一步是证明局部不等式

$$
\left|c_{i} d_{i}+c_{j} d_{j}\right| \geq \frac{1}{2}\left(d_{i}+d_{j}\right)+\frac{1}{2}\left(c_{i} \overline{c_{j}}+\overline{c_{i}} c_{j}\right) \sqrt{d_{i} d_{j}}
$$

之后同原证明.

(*) 式证明如下: 当 $d_{i}$ 或 $d_{j}$ 等于 0 时显然成立, 下不妨设 $d_{i} \geq d_{j}>0$. 记 $d=\frac{d_{i}}{d_{j}}, \lambda=\overline{c_{i}} c_{j}$, 则 $d \geq 1,|\lambda|=1$, 且

$$
\left|c_{i} d_{i}+c_{j} d_{j}\right|=\left|d_{i}+\overline{c_{i}} c_{j} d_{j}\right|=d_{j}|d+\lambda|,
$$

于是只需证明

$$
|d+\lambda| \geq \frac{1}{2}(d+1)+\frac{1}{2}(\lambda+\bar{\lambda}) \sqrt{d}
$$

设 $\lambda=\cos \theta+i \sin \theta$, 则只需证明

$$
d+\cos \theta \geq \frac{1}{2}(d+1)+\cos \theta \sqrt{d}
$$

这等价于

$$
\sqrt{d}+1 \geq 2 \cos \theta
$$

由 $\sqrt{d}+1 \geq 2 \geq 2 \cos \theta$ 即证.

(4). 巴黎高等师范学院刘奔博士指出, 二维情形对 $b_{1}, b_{2}, \cdots, b_{n} \in \mathbb{R}^{d}$ 也成立, 其中 $d$ 是任意正整数.

先证明一个引理.

引理 设 $f: \mathbb{R}^{d} \rightarrow \mathbb{R}^{d}$, 满足

$$
f(x)= \begin{cases}0, & x=0 \\ \frac{x}{\sqrt{|x|}}, & x \neq 0\end{cases}
$$

则对任意 $a, b \in \mathbb{R}^{d}$,

$$
2|a+b| \geq|f(a)+f(b)|^{2}
$$

证明 设 $f(a)=x u, f(b)=y v$, 其中 $x=|f(a)|, y=|f(b)|, u, v$ 是单位向量,则 $a=x^{2} u, b=y^{2} v$. 记 $c=\langle u, v\rangle$ 为 $u, v$ 的内积, 则

$$
\begin{aligned}
& 4|a+b|^{2}-|f(a)+f(b)|^{4} \\
= & 4\left(x^{4}+y^{4}+2 x^{2} y^{2} c\right)-\left(x^{2}+y^{2}+2 x y c\right)^{2} \\
= & 3\left(x^{4}+y^{4}\right)-2 x^{2} y^{2}+\left(8 x^{2} y^{2}-4 x y\left(x^{2}+y^{2}\right)\right) c-4 x^{2} y^{2} c^{2} .
\end{aligned}
$$

上式是关于 $c$ 的二次函数, 开口向下, 因此最小值在端点 $\pm 1$ 处取到.

当 $c=1$ 时,

$$
4|a+b|^{2}-|f(a)+f(b)|^{4}=4\left(x^{2}+y^{2}\right)^{2}-(x+y)^{4} \geq 0
$$

当 $c=-1$ 时,

$4|a+b|^{2}-|f(a)+f(b)|^{4}=4\left(x^{2}-y^{2}\right)^{2}-(x-y)^{4}=(x-y)^{2}\left(4(x+y)^{2}-(x-y)^{2}\right) \geq 0$.

引理证毕.

回到原题. 由引理,

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n}\left|b_{i}+b_{j}\right| \cdot a_{i} a_{j} \\
\geq & \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n}\left|f\left(b_{i}\right)+f\left(b_{j}\right)\right|^{2} \cdot a_{i} a_{j} \\
= & \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\left|f\left(b_{i}\right)\right|^{2}+\left|f\left(b_{j}\right)\right|^{2}+2\left\langle f\left(b_{i}\right), f\left(b_{j}\right)\right\rangle\right) \cdot a_{i} a_{j} \\
= & \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\left|b_{i}\right|+\left|b_{j}\right|\right) \cdot a_{i} a_{j}+\sum_{i=1}^{n} \sum_{j=1}^{n}\left\langle f\left(b_{i}\right), f\left(b_{j}\right)\right\rangle \cdot a_{i} a_{j} \\
= & \left(\sum_{i=1}^{n}\left|b_{i}\right| \cdot a_{i}\right)\left(\sum_{j=1}^{n} a_{j}\right)+\left|\sum_{i=1}^{n} f\left(b_{i}\right) \cdot a_{i}\right|^{2} \\
\geq & \sum_{i=1}^{n}\left|b_{i}\right| \cdot a_{i} .
\end{aligned}
$$

(5). 杭州学军中学叶梓、郑思源, 雅礼中学温玟杰, 温州中学金茂治, 华东师大二附中王一川等同学也给出了本题的正确解答.

第四题 对简单图 $G(V, E)$ 以及任意边子集 $E_{1} \subset E$, 称顶点子集 $V_{1} \subset V$ 覆盖 $E_{1}$, 若 $E_{1}$ 中的每条边至少有一个端点在 $V_{1}$ 中. 求最小的正整数 $N$, 使得对
任意简单图 $G$, 只要 $G$ 的任意 $N$ 条边可以被不超过 20 个顶点覆盖, 则 $G$ 的全部边可以被不超过 20 个顶点覆盖.

(北京大学学生 刘浩宇 供题)

## 解 (根据华东师大二附中王一川同学的解答整理)：

$N$ 的最小值为 231 .

一方面, 取 $G$ 为 22 阶完全图, 则 $G$ 的全部边不能被 20 个顶点覆盖. 而去掉 $G$ 中任意一条边 $v_{1} v_{2}$ 后, 余下的边可用 $V \backslash\left\{v_{1}, v_{2}\right\}$ 覆盖. 故 $N \leq \mathrm{C}_{22}^{2}-1=230$,不符合要求.

另一方面, 我们证明 $N=231$ 符合要求.

只需证明在简单图 $G(V, E)$ 中, 若 $|E| \geq 232$, 且去掉 $G$ 中任意一条边后余下的边可用 20 个顶点覆盖, 则 $G$ 的所有边也可用 20 个顶点覆盖.

设 $G$ 的边数为 $r(r \geq 232), G$ 的边为 $e_{1}, e_{2}, \cdots, e_{r}$.

对 $1 \leq i \leq r$, 设 $e_{i}$ 的两端点构成二元集 $A_{i}, 20$ 元集 $B_{i} \subseteq V$ 覆盖除 $e_{i}$ 外的所有边。

假设 $G$ 的所有边不能用 20 个顶点覆盖, 则 $B_{1}, B_{2}, \cdots, B_{r}$ 两两不同, 且对 $1 \leq i \leq r, A_{i} \cap B_{i}=\emptyset\left(\right.$ 否则 $B_{i}$ 覆盖 $\left.e_{i}\right) ;$ 对 $1 \leq i, j \leq r, i \neq j, A_{i} \cap B_{j} \neq \emptyset($ 因为 $B_{j}$ 覆盖 $\left.e_{i}\right)$.

因为 $\left|A_{i}\right|=2,\left|B_{i}\right|=20$, 所以由 Bollobás 定理, $r \leq \mathrm{C}_{2+20}^{2}=231$, 矛盾!

综上, 所求最小值为 231 .

评注 (1). Bollobás 定理叙述为:

设 $A_{1}, A_{2}, \cdots, A_{k}, B_{1}, B_{2}, \cdots, B_{k}$ 是集合 $\{1,2, \cdots, n\}$ 的不同子集，满足对 $1 \leq i, j \leq k, A_{i} \cap B_{j}=\emptyset$ 当且仅当 $i=j$, 则

$$
\sum_{i=1}^{k} \frac{1}{\mathrm{C}_{\left|A_{i}\right|+\left|B_{i}\right|}^{\left|A_{i}\right|}} \leq 1
$$

特别当 $\left|A_{1}\right|=\cdots=\left|A_{k}\right|=a,\left|B_{1}\right|=\cdots=\left|B_{k}\right|=b$ 时, $k \leq \mathrm{C}_{a+b}^{a}$.

(2). 杭州学军中学郑思源同学也给出了本题的正确解答.

