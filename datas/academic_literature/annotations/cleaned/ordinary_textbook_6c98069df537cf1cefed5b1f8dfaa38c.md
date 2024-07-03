数学新星网 实学生专栏

www.nsmath.cn/xszl

# 2020 年 USAMO 试题解答与评析 

王一川

(华东师范大学第二附属中学, 201203)

指导教师: 唐立华

2020 年 USAMO 于 6 月 19, 20 日 $13: 30-18: 00$ 在线上进行. 个人认为其中 $1,2,4,5$ 是简单题, 3,6 较难, 没有超级难题, 其中 3,6 均存在很简单 (巧妙)的做法, 但一般在考场上想到的解法都比较复杂. 本文给出 2020 年 USAMO 试题的解答. 直于水平, 不当之处在所难免, 敬请读者不吝赐教.

## I. 试 题

1. 给定锐角 $\triangle A B C, \omega$ 是其外接圆, $O$ 是 $\omega$ 的圆心, $X$ 是 $\omega$ 中劣弧 $A B$ 上的一个动点, $D$ 是线段 $C X$ 与 $A B$ 的交点, $O_{1}, O_{2}$ 分别是 $\triangle A D X, \triangle B D X$ 的外心. 求所有的点 $X$, 使 $\triangle O O_{1} O_{2}$ 的面积取到最小值.
2. 给定一个空心的 $2020 \times 2020 \times 2020$ 的大立方体, 在大立方体的 6 个面上各画一个 $2020 \times 2020$ 的方格表. 称 “棒” 是一个 $1 \times 1 \times 2020$ 的长方体, 在大立方体内放置若干 $(>0)$ 个棒, 满足下列条件:

(1) 每个棒中, 两个 $1 \times 1$ 的面分别是大立方体中两个相对的面上的小方格 (这样的棒一共有 $3 \cdot 2020^{2}$ 种可能的位置);

(2) 所有棒的内部区域 (不含面) 两两不相交;

(3) 每个棒中, 4 个 $1 \times 2020$ 的面 (不含棱) 均碰到大立方体的面或另一个棒的面 (不含棱).

求棒的个数的最小可能值.

3. 给定奇素数 $p$. 称一个整数 $x$ 是 “非平方剩余”, 如果对任意整数 $t, p$ 不整除 $x-t^{2} . A$ 是所有满足 $1 \leq a<p$ 且 $a, 4-a$ 均是非平方剩余的整数 $a$ 组成的集合, 求 $A$ 中所有元素的乘积模 $p$ 的余数.

修订日期: 2020-08-18.

4. 设 $\left(a_{1}, b_{1}\right),\left(a_{2}, b_{2}\right), \cdots,\left(a_{100}, b_{100}\right)$ 是两两不同的有序非负整数对, $N$ 是满足 $1 \leq i<j \leq 100$ 且 $\left|a_{i} b_{j}-a_{j} b_{i}\right|=1$ 的整数对 $(i, j)$ 的个数. 求 $N$ 的最大可能值.
5. 在平面直角坐标系 $x O y$ 中, 称一个有限点集 $S$ 是“超定的”,如果 $|S| \geq 2$且存在一个次数不超过 $|S|-2$ 的非零实系数多项式 $P(t)$, 满足对 $S$ 中的每个点 $(x, y)$, 均有 $P(x)=y$.

给定整数 $n \geq 2$, 求最大整数 $k=k(n)$, 使得存在一个 $n$ 元点集不是超定的,且这个点集有 $k$ 个超定的子集.

6. 设 $n \geq 2$ 是一个整数, $x_{1} \geq x_{2} \geq \cdots \geq x_{n}, y_{1} \geq y_{2} \geq \cdots \geq y_{n}$ 是 $2 n$ 个实数, 满足 $\sum_{i=1}^{n} x_{i}=\sum_{i=1}^{n} y_{i}=0$, 且 $\sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} y_{i}^{2}=1$. 证明:

$$
\sum_{i=1}^{n}\left(x_{i} y_{i}-x_{i} y_{n+1-i}\right) \geq \frac{2}{\sqrt{n-1}}
$$

## II . 解答与评注

1. 给定锐角 $\triangle A B C, \omega$ 是其外接圆, $O$ 是 $\omega$ 的圆心, $X$ 是 $\omega$ 中劣弧 $A B$ 上的一个动点, $D$ 是线段 $C X$ 与 $A B$ 的交点, $O_{1}, O_{2}$ 分别是 $\triangle A D X, \triangle B D X$ 的外心. 求所有的点 $X$, 使 $\triangle O O_{1} O_{2}$ 的面积取到最小值.



解 考虑 $\triangle A B C, \triangle A X D$, 其中 $O, O_{1}$ 分别是外心. 由 $A, B, C, X$ 共圆知 $\angle A B C=\angle A X D$, 进而 $\angle A O_{1} D=\angle A O C$, 故 $\triangle A O_{1} D \sim \triangle A O C$.于是

$$
A O \cdot A D=A O_{1} \cdot A C
$$

且.

$$
\angle O A O_{1}=\angle D A O_{1}+\angle O A D=\angle C A O+\angle O A D=\angle C A D .
$$

故

$$
\triangle O A O_{1} \sim \triangle C A D
$$

同理可知

$$
\triangle O B O_{2} \sim \triangle C B D .
$$

结合(1)(2)知:

$$
O O_{1}=C D \cdot \frac{A O}{A C}, O O_{2}=C D \cdot \frac{B O}{B C}
$$

且

$$
\begin{aligned}
\angle O_{1} O O_{2} & =\angle A O B-\angle A O O_{1}-\angle B O O_{2} \\
& =2 \angle A C B-\angle A C D-\angle B C D \\
& =\angle A C B .
\end{aligned}
$$

结合(3)(4)知:

$$
\begin{aligned}
S_{\triangle O O_{1} O_{2}} & =\frac{1}{2} \cdot O O_{1} \cdot O O_{2} \cdot \sin \angle O_{1} O O_{2} \\
& =\frac{1}{2} \cdot C D^{2} \cdot \frac{A O}{A C} \cdot \frac{B O}{B C} \cdot \sin \angle A C B .
\end{aligned}
$$

显然 $A, B, C, O$ 均为定点, 故 $\frac{A O}{A C} \cdot \frac{B O}{B C} \cdot \sin \angle A C B$ 是定值. 从而 $S_{\triangle O O_{1} O_{2}}$ 最小等价于 $C D^{2}$ 最小, 而 $C D^{2}$ 在 $C D \perp A B$ 时取到最小值. 相应地, 原题所求 $X$ 即为使 $C X \perp A B$ 的点.

评注 注意到 $\triangle O O_{1} O_{2}$ 各边长及角度均可以看得很清楚, 本题是送分题.

2. 给定一个空心的 $2020 \times 2020 \times 2020$ 的大立方体,在大立方体的 6 个面上各画一个 $2020 \times 2020$ 的方格表. 称 “棒” 是一个 $1 \times 1 \times 2020$ 的长方体, 在大立方体内放置若干 $(>0)$ 个棒, 满足下列条件:

(1) 每个棒中, 两个 $1 \times 1$ 的面分别是大立方体中两个相对的面上的小方格 (这样的棒一共有 $3 \cdot 2020^{2}$ 种可能的位置);

(2) 所有棒的内部区域 (不含面) 两两不相交;

(3) 每个棒中, 4 个 $1 \times 2020$ 的面 (不含棱) 均碰到大立方体的面或另一个棒的面 (不含棱).

求棒的个数的最小可能值.

解 (1) 约定一些记号:

将 $2020 \times 2020 \times 2020$ 的立方体看做一个 $2020 \times 2020 \times 2020$ 的立体表格，则“棒”即为 $1 \times 1 \times 2020$ 的子表格(可旋转).
我们用有序三元组 $(x, y, z)(1 \leq x, y, z \leq 2020)$ 标记表格中的每一个小立方体, 其中 $(x, y, z)$ 表示高度为 $z$ 的一层中第 $x$ 行第 $y$ 列的小立方体.

用三元组 $(x, y, \#)$ 表示包含小立方体

$$
(x, y, 1),(x, y, 2), \cdots,(x, y, 2020)
$$

的棒, 类似定义 $(x, \#, z),(\#, y, z)$.

我们称“截面”指一个 $1 \times 2020 \times 2020$ 的子表格(可旋转),显然“截面”有 3 . 2020 个. 用三元组 $(x, \#, \#)$ 或者 $(\#, y, \#)$ 或者 $(\#, \#, z)(1 \leq x, y, z \leq 2020)$来标记一个截面, 其中 “\#” 是一个符号, $(x, \#, \#)$ 表示由小立方体

$$
(x, i, j)(1 \leq i, j \leq 2020)
$$

组成的截面, 类似定义 $(\#, y, \#),(\#, \#, z)$.

记原题中的 3 个条件依次为 (1), (2), (3).

(2) 回到原题, 结论是: “棒” 个数最小值为 3030 . 先给出构造: 取出 3030 个棒: $(2 k-1,2 k, \#),(2 k, \#, 2 k-1),(\#, 2 k-1,2 k)(1 \leq k \leq 1010)$.

验证构造: 显然棒 $(2 k-1,2 k, \#)(1 \leq k \leq 1010)$ 两两不相交, 且对 $1 \leq$ $k, k^{\prime} \leq 1010$, 棒 $(2 k-1,2 k, \#),\left(2 k^{\prime}, \#, 2 k^{\prime}-1\right)$ 不交(考虑第一个分量即可).类似地, 可知 3030 个棒两两不相交, 符合条件 (2).

对 $1 \leq k \leq 1010$, 棒 $(2 k-1,2 k, \#)$ 四个面分别碰到棒 $(2 k-2, \#, 2 k-3),(2 k, \#, 2 k-1)$, (\#, $2 k+1,2 k+2)$, (\#, $2 k-1,2 k)$.其中, 约定 $(0, \#,-1),(\#, 2021,2022)$ 等表示表格边界. 类似地, 可知 3030 个棒均符合条件 (3).

条件 1显然满足, 故 3030 个“棒”可以达到.

(3) 再给出证明: 即证至少需要 3030 个“棒”.

任取一个棒, 不妨设为 $\left(x_{0}, y_{0}, \#\right)$ (否则适当旋转表格). 考虑 $\left(x_{0}, y_{0}, \#\right)$ 的与截面 $\left(x_{0}+1, \#, \#\right)$ 接触的面, 同样约定 $(0, \#, \#),(2021, \#, \#)$ 等表示表格边界.

由 (3) 知截面 $\left(x_{0}+1, \#, \#\right)$ 中至少包含一个棒. 同理, 截面 $\left(x_{0}-1, \#, \#\right)$, $\left(\#, y_{0}-1, \#\right),\left(\#, y_{0}+1, \#\right)$ 中也都至少包含一个棒.

由上述过程可知: 若截面 $(t, \#, \#),(1 \leq t \leq 2020)$ 至少包含一个棒, 则截面 $(t-1, \#, \#),(t+1, \#, \#)$ 均至少包含一个棒.

从 $\left(x_{0}, y_{0}, \#\right)$ 开始, 不断应用 $(*)$ 可知: 截面 $(1, \#, \#),(2, \#, \#), \cdots$, $(2020, \#, \#),(\#, 1, \#),(\#, 2, \#), \cdots,(\#, 2020, \#)$ 中均至少包含一个棒.
以下分两种情形:

情形 1: 存在形如 $(x, \#, z)$ 或 $(\#, y, z)$ 的棒.

由 $(*)$ 知所有 $3 \cdot 2020$ 个截面中均至少包含一个棒, 而另一方面, 显然每个棒恰包含在两个截面中, 故棒的个数 $\geq \frac{3 \times 2020}{2}=3030$.

情形 2: 不存在形如 $(x, \#, z)$ 或 $(\#, y, z)$ 的棒.

此时对 $1 \leq s, t \leq 2020$, 若存在棒 $(s, t, \#)$, 则由条件(3)知存在棒

$$
(s-1, t, \#),(s+1, t, \#),(s, t-1, \#),(s, t+1, \#)
$$

从 $\left(x_{0}, y_{0}, \#\right)$ 开始, 反复利用 $(* *)$ 知: 所有形如 $(x, y, \#)(1 \leq x, y \leq 2020)$ 的棒均存在,一共至少 $2020^{2}>3030$ 个棒.

综上, 总有至少 3030 个棒, 故“棒” 个数最小值为 3030 .

评注 本题是一个立方体表格问题, 本题的关键是需要理解清楚原题条件(3)到底是什么, 之后的证明就不难了, 本题的构造从几何直观上不太好理解,但从纯代数的角度反而更好理解.

3. 给定奇素数 $p$. 称一个整数 $x$ 是“非平方剩余”, 如果对任意整数 $t, p$ 不整除 $x-t^{2} . A$ 是所有满足 $1 \leq a<p$ 且 $a, 4-a$ 均是非平方剩余的整数 $a$ 组成的集合, 求 $A$ 中所有元素的乘积模 $p$ 的余数.

解 (1) 取 $p$ 的原根 $g$. 设 $X^{+}$是 $1,2, \cdots, p-1$ 中所有模 $p$ 的平方剩余组成的集合, $X^{-}$是 $1,2, \cdots, p-1$ 中所有模 $p$ 的非平方剩余组成的集合.

考虑如下 4 个同余方程组 (关于 $x, y$ )

$$
\begin{aligned}
& \Omega_{1}:\left\{\begin{array}{l}
x+y \equiv 4 \quad(\bmod p) \\
(x, y) \in X^{-} \times X^{-}
\end{array}, \quad \Omega_{2}:\left\{\begin{array}{l}
x+y \equiv 4 \quad(\bmod p) \\
(x, y) \in X^{+} \times X^{-}
\end{array}\right.\right. \\
& \Omega_{3}:\left\{\begin{array}{l}
g x^{2}+g y^{2} \equiv 4 \quad(\bmod p) \\
x, y \in\{1,2, \cdots, p-1\}
\end{array}, \quad \Omega_{4}:\left\{\begin{array}{l}
x^{2}+g y^{2} \equiv 4 \quad(\bmod p) \\
x, y \in\{1,2, \cdots, p-1\}
\end{array}\right.\right.
\end{aligned}
$$

显然, 由 $\Omega_{3}$ 的所有解 $(x, y)$ 得到的不同的 $\left(g x^{2}, g y^{2}\right)$ 即为 $\Omega_{1}$ 的所有不同解, 由 $\Omega_{4}$ 的所有解 $(x, y)$ 得到的不同的 $\left(x^{2}, g y^{2}\right)$ 即为 $\Omega_{2}$ 的所有不同解.

对 $i=1,2$, 记 $S_{i}$ 为 $\Omega_{i}$ 的所有不同解中 $y$ 的乘积. 显然 $S_{1} S_{2}=\prod_{j \in X^{-}} j$, 且原题所求即为 $S_{1}$ 模 $p$ 的余数. 其中

$$
S_{1} S_{2}=\prod_{j \in X^{-}} j \equiv \prod_{j=1}^{\frac{p-1}{2}} g^{2 j-1} \equiv g^{\left(\frac{p-1}{2}\right)^{2}} \quad(\bmod p)
$$

(2) 以下计算 $S_{2}$ : 设 $\Omega_{4}$ 的所有解中, $y$ 的所有不同值为 $y_{1}, y_{2}, \cdots, y_{m}$. 显然 $0 \notin\left\{y_{1}, y_{2}, \cdots, y_{m}\right\}$, 且

$$
\left\{-y_{1},-y_{2}, \cdots,-y_{m}\right\}=\left\{y_{1}, y_{2}, \cdots, y_{m}\right\}(\bmod p \text { 意义). }
$$

故 $2 \mid m$, 且可设

$$
\left\{y_{1}, y_{2}, \cdots, y_{m}\right\}=\left\{z_{1},-z_{1}, z_{2},-z_{2} \cdots z_{\frac{m}{2}},-z_{\frac{m}{2}}\right\}(\bmod p \text { 意义 }) \text {, }
$$

则

$$
S_{2} \equiv \prod_{j=1}^{\frac{m}{2}} g z_{j}^{2} \equiv \prod_{j=1}^{\frac{m}{2}}-g \cdot z_{j} \cdot\left(-z_{j}\right) \equiv(-g)^{\frac{m}{2}} \cdot y_{1} y_{2} \cdots y_{m} \quad(\bmod p)
$$

(3) 以下求 $m$ 及 $y_{1}, y_{2}, \cdots, y_{m}$. 注意到, $\Omega_{4}$ 可写为

$$
\left\{\begin{array}{l}
\left(x y^{-1}\right)^{2}+g \equiv\left(2 y^{-1}\right)^{2} \quad(\bmod p) \\
x, y \in\{1,2, \cdots, p-1\}
\end{array} .\right.
$$

其中, 用 $\alpha^{-1}$ 表示 $\alpha(p$ 不整除 $\alpha)$ 模 $p$ 的逆元. 且

$\left(x y^{-1}\right)^{2}+g \equiv\left(2 y^{-1}\right)^{2} \quad(\bmod p) \Leftrightarrow\left(2 y^{-1}+x y^{-1}\right)\left(2 y^{-1}-x y^{-1}\right) \equiv g \quad(\bmod p)$.为求出 $y$ 的所有不同可能值, 只需要考虑

$$
2 y^{-1}+x y^{-1} \equiv g^{k} \quad(\bmod p), 2 y^{-1}-x y^{-1} \equiv g^{p-k} \quad(\bmod p)
$$

的情形, 其中 $1 \leq k \leq \frac{p-1}{2}$. 由 $p$ 不整除 $2 y^{-1}, x y^{-1}$ 知

$$
g^{k} \neq \pm g^{p-k} \quad(\bmod p)
$$

即 $k \neq \frac{p+1}{4}$.

(4) 分 $p$ 模 4 余数讨论:

情形 $1 \quad p \equiv 1(\bmod 4)$. 此时 $m=\frac{p-1}{2}$ (因为 $\frac{p+1}{4} \notin \mathbb{Z}$ ), 且

$$
\begin{aligned}
y_{1} y_{2} \cdots y_{m} & \equiv\left(y_{1}^{-1} y_{2}^{-1} \cdots y_{m}^{-1}\right)^{-1} \\
& \equiv\left(\prod_{k=1}^{\frac{p-1}{2}}\left(\left(g^{k}+g^{p-k}\right) \cdot 4^{-1}\right)\right)^{-1}(\text { 由(3) }) \\
& \equiv 4^{\frac{p-1}{2}} \cdot \prod_{k=1}^{\frac{p-1}{2}}\left(g^{k}+g^{p-k}\right)^{-1} \\
& \equiv 4^{\frac{p-1}{2}} \cdot\left(\prod_{k=1}^{\frac{p-1}{2}}\left(g^{2 k-1}+1\right)^{-1}\right) \cdot\left(\prod_{k=1}^{\frac{p-1}{2}} g^{k-1}\right) \\
& \equiv\left(\prod_{k=1}^{\frac{p-1}{2}}\left(g^{2 k-1}+1\right)^{-1}\right) \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}}(\bmod p) .
\end{aligned}
$$

其中由费马小定理, 有

$$
4^{\frac{p-1}{2}}=2^{p-1} \equiv 1 \quad(\bmod p) .
$$

而 $g^{2 k-1}+1\left(1 \leq k \leq \frac{p-1}{2}\right)$ 恰为关于 $x$ 的多项式 $(x-1)^{\frac{p-1}{2}}+1$ 模 $p$ 意义下的所有不同根, 由韦达定理知乘积为 2 . 故由(4)知

$$
y_{1} y_{2} \cdots y_{m} \equiv 2^{-1} \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}} \quad(\bmod p) .
$$

再代入(2)知

$$
S_{2} \equiv(-g)^{\frac{p-1}{4}} \cdot 2^{-1} \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}} \quad(\bmod p)
$$

再代入(1)知

$$
\begin{aligned}
S_{1} & \equiv S_{1} S_{2} \cdot S_{2}^{-1} \\
& \equiv 2 \cdot(-1)^{\frac{p-1}{4}} \cdot g^{\left(\frac{p-1}{2}\right)^{2}-\frac{p-1}{4}-\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}} \\
& \equiv 2 \cdot g^{\left.\left(\left(\frac{p-1}{2}\right)^{2}-\frac{p-1}{4}-\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}\right)\right)+\frac{p-1}{4} \cdot \frac{p-1}{2}} \\
& \equiv 2 \cdot g^{\left(\frac{p-1}{2}\right)^{2}} \equiv 2 \quad(\bmod p) .
\end{aligned}
$$

其中最后一步是由于

$$
\left(\frac{p-1}{2}\right)^{2}=(p-1) \cdot \frac{p-1}{4} \equiv p-1 \quad(\bmod p-1)
$$

情形 $2 \quad p \equiv-1(\bmod 4)$. 此时 $\frac{p+1}{4} \in \mathbb{Z}$, 故 $m=\frac{p-3}{2}$ 且

$$
\begin{aligned}
y_{1} y_{2} \cdots y_{m} & \equiv\left(\prod_{\substack{1 \leq k \leq \frac{p-1}{2} \\
k \neq \frac{p+1}{4}}}\left(\left(g^{k}+g^{p-k}\right) \cdot 4^{-1}\right)\right)^{-1} \\
& \equiv 4^{\frac{p-3}{2}} \cdot\left(\prod_{\substack{1 \leq k \leq \frac{p-1}{2} \\
k \neq \frac{p+1}{4}}}\left(g^{2 k-1}+1\right)^{-1}\right) \cdot\left(\prod_{\substack{1 \leq k \leq \frac{p-1}{2} \\
k \neq \frac{p+1}{4}}} g^{k-1}\right) \\
& \equiv 4^{\frac{p-3}{2}} \cdot\left(\prod_{\substack{1 \leq k \leq \frac{p-1}{2} \\
k \neq \frac{p+1}{4}}}\left(g^{2 k-1}+1\right)^{-1}\right) \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}-\frac{p-3}{4}}(\bmod p) .
\end{aligned}
$$

其中 $g^{2 k-1}+1\left(1 \leq k \leq \frac{p-1}{2}, k \neq \frac{p+1}{4}\right)$ 恰为关于 $x$ 的多项式 $\frac{(x-1)^{\frac{p-1}{2}}+1}{x}$ 的所有不同根, 由韦达定理知乘积为 $\frac{p-1}{2}$. 代入(5)知

$$
\begin{aligned}
y_{1} y_{2} \cdots y_{m} & \equiv 4^{\frac{p-3}{2}} \cdot\left(\frac{p-1}{2}\right)^{-1} \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}-\frac{p-3}{4}} \\
& \equiv 2^{p-3} \cdot(-2) \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}-\frac{p-3}{4}} \\
& \equiv 2^{-1} \cdot(-1) \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}-\frac{p-3}{4}}(\bmod p) .
\end{aligned}
$$

上式同样用到费马小定理, 代入(2)有

$$
\begin{aligned}
& S_{2} \equiv(-g)^{\frac{p-3}{4}} \cdot 2^{-1} \cdot(-1) \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}-\frac{p-3}{4}} \\
& \equiv 2^{-1} \cdot(-1)^{\frac{p+1}{4}} \cdot g^{\left(\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}-\frac{p-3}{4}\right)+\frac{p-3}{4}} \\
& \equiv 2^{-1} \cdot(-1)^{\frac{p+1}{4}} \cdot g^{\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}} \quad(\bmod p) .
\end{aligned}
$$

再代入(1)有

$$
\begin{aligned}
S_{1} & \equiv S_{1} S_{2} \cdot S_{2}^{-1} \\
& \equiv g^{\left(\frac{p-1}{2}\right)^{2}-\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}} \cdot(-1)^{\frac{p+1}{4}} \cdot 2 \\
& \equiv g^{\left(\frac{p-1}{2}\right)^{2}-\frac{1}{2} \cdot \frac{p-1}{2} \cdot \frac{p-3}{2}+\frac{p+1}{4} \cdot \frac{p-1}{2}} \cdot 2 \\
& \equiv g^{\frac{p^{2}-1}{4}} \cdot 2 \\
& \equiv g^{(p-1) \cdot \frac{p+1}{4}} \cdot 2 \equiv 2 \quad(\bmod p) .
\end{aligned}
$$

综上, 两种情形中, 均有所求 $S_{1} \equiv 2(\bmod p)$.

评注 一个经典的问题是: 求 $|A|$ 的值 (该经典问题的解法中, 关键部分的配平方差, 即原题解答中式(3)的那一步), 利用这个方法容易将原题所求乘积化为计算 $\prod_{1 \leq k \leq \frac{p-1}{2}, k \neq \frac{p+1}{4}}\left(g^{k}+g^{p-k}\right)$. 在处理这个乘积的时候, 我们类比了处理复数单位根问题中的手法: 复数中的经典问题是求表达式 $\sin 1^{\circ} \cdot \sin 2^{\circ} \cdots \cdot \sin 89^{\circ}$ 的值, 解法是化为单位根, 并构造多项式, 应用韦达定理(复数单位根与素数原根有很多相似之处).

本题还有另一个巧妙的解法: 记

$$
\begin{aligned}
& V^{+}=\left\{x \mid x, 4-x \in X^{+} \quad(\bmod p)\right\} \\
& V^{-}=\left\{x \mid x, 4-x \in X^{-} \quad(\bmod p)\right\}
\end{aligned}
$$

其中, $X^{+}, X^{-}$与原解答中定义相同. 则

$$
\begin{aligned}
& \prod_{x \in V^{+}} x=\prod_{x \in V^{+}}(4-x)=\prod_{\substack{4-x^{2} \in X^{+} \\
x \neq 0,2 \\
1 \leq x \leq \frac{p-1}{2}}}\left(4-x^{2}\right) \\
& =\prod_{\substack{4-x^{2} \in X^{+} \\
x \neq 0,2 \\
1 \leq x \leq \frac{p-1}{2}}}(2+x)(2-x)=\prod_{\substack{4-x^{2} \in X^{+} \\
x \neq 2,-2 \\
1 \leq x \leq p-1}}(2+x) \\
& =\prod_{\substack{x(4-x) \in X^{+} \\
x \neq 0,4 \\
3 \leq x \leq p+1}} x=\prod_{\substack{x \in V^{+} \cup V^{-} \\
x \neq 0,2,4 \\
1 \leq x \leq p-1}} x
\end{aligned}
$$

$$
=\frac{1}{2} \cdot \prod_{x \in V^{+}} x \cdot \prod_{x \in V^{-}} x
$$

故有

$$
\prod_{x \in V^{-}} x \equiv 2 \quad(\bmod p)
$$

4. 设 $\left(a_{1}, b_{1}\right),\left(a_{2}, b_{2}\right), \cdots,\left(a_{100}, b_{100}\right)$ 是两两不同的有序非负整数对, $N$ 是满足 $1 \leq i<j \leq 100$ 且 $\left|a_{i} b_{j}-a_{j} b_{i}\right|=1$ 的整数对 $(i, j)$ 的个数. 求 $N$ 的最大可能值

解 结论: $N$ 最大值为 197 .

(1) 先给出构造: 令

$$
\left(a_{i}, b_{i}\right)=(i-1, i)(1 \leq i \leq 99),\left(a_{100}, b_{100}\right)=(1,1) .
$$

此时对 $1 \leq i \leq 98$, 有

$$
\left|a_{i} b_{i+1}-a_{i+1} b_{i}\right|=\left|(i-1)(i+1)-i^{2}\right|=1 .
$$

对 $1 \leq i \leq 99$, 有

$$
\left|a_{i} b_{100}-a_{100} b_{i}\right|=|(i-1)-i|=1 \text {. }
$$

故 $N \geq 98+99=197$, 得到了一个使 $N \geq 197$ 的构造.

(2) 再证明总有 $N \leq 197$.

不妨设对 $i=1,2, \cdots, 100, a_{i}, b_{i}$ 全为 0 或全不为 0 , 否则用 $\left(a_{i}+b_{i}, a_{i}+2 b_{i}\right)$替换 $\left(a_{i}, b_{i}\right)(1 \leq i \leq 100)$. 此时对 $1 \leq i \leq j \leq 100$,

$$
\left(a_{i}+b_{i}\right)\left(a_{j}+2 b_{j}\right)-\left(a_{j}+b_{j}\right)\left(a_{i}+2 b_{i}\right)=a_{i} b_{j}-a_{j} b_{i},
$$

结论不变. 显然此时 $\left(a_{i}+b_{i}, a_{i}+2 b_{i}\right)$ 仍两两不同.

不妨设 $b_{1} \leq b_{2} \leq \cdots \leq b_{100}$, 否则重新排列. 称符合原题条件的 $(i, j)$ 为 “好对”。

下证对取定的 $j \in\{3,4, \cdots 100\}$, 至多存在 2 个 $i$ 使 $(i, j)$ 是“好对”. (1)

用反证法, 假设(1)不成立, 即存在正整数 $i_{1}, i_{2}, i_{3}, j$, 其中 $i_{1}, i_{2}, i_{3}$ 是区间 $[1, j)$ 中的不同正整数, 且 $\left(i_{1}, j\right),\left(i_{2}, j\right),\left(i_{3}, j\right)$ 均是好对, 即对 $k=1,2,3$, 有

$$
a_{i_{k}} b_{j}-a_{j} b_{i_{k}} \in\{-1,1\},
$$

由抽屉原理, 存在 $1 \leq u<v \leq 3$, 使得

$$
a_{i_{u}} b_{j}-a_{j} b_{i_{u}}=a_{i_{v}} b_{j}-a_{j} b_{i_{v}} \in\{-1,1\} .
$$

不妨设 $u=1, v=2$. 显然, 最大公约数

$$
\left(a_{j}, b_{j}\right)=\left(b_{i_{1}}, b_{j}\right)=\left(b_{i_{2}}, b_{j}\right)=1,
$$

且

$$
a_{i_{1}} b_{j}-a_{j} b_{i_{1}}=a_{i_{2}} b_{j}-a_{j} b_{i_{2}} \Rightarrow b_{j}\left(a_{i_{1}}-a_{i_{2}}\right)=a_{j}\left(b_{i_{1}}-b_{i_{2}}\right) .
$$

由于 $\left(a_{j}, b_{j}\right)=1$, 故由(3)知可设

$$
a_{i_{1}}-a_{i_{2}}=h a_{j}, b_{i_{1}}-b_{i_{2}}=h b_{j}, \quad(h \in \mathbb{Z}),
$$

且由数对 $\left(a_{i_{1}}, b_{i_{1}}\right) \neq\left(a_{i_{2}}, b_{i_{2}}\right)$ 知 $h \neq 0$ 且 $a_{j}, b_{j}$ 不全为 0 . 由 $h \neq 0$ 知

$$
\left|b_{i_{1}}-b_{i_{2}}\right|=\left|h b_{j}\right| \geq\left|b_{j}\right|
$$

而由 $i_{1}, i_{2} \in[1, j)$ 知 $b_{i_{1}}, b_{i_{2}} \in\left[0, b_{j}\right]$, 故只能 $\left\{b_{i_{1}}, b_{i_{2}}\right\}=\left\{0, b_{j}\right\}$. 特别地, 若 $b_{j}$ $=0$, 则 $b_{i_{1}}=b_{i_{2}}=0$. 再结合(2)即知最大公约数

$$
\left(0, b_{j}\right)=\left(b_{j}, b_{j}\right)=1
$$

只能 $b_{j}=1$. 进而不妨设 $b_{i_{1}}=0, b_{i_{2}}=1$. 由 “不妨设对 $i=1,2, \cdots, 100, a_{i}, b_{i}$全为 0 或全不为 0 "知: $a_{i_{1}}=0$. 于是

$$
a_{i_{1}} b_{j}-a_{j} b_{i_{1}}=0 \notin\{-1,1\},
$$

矛盾!故反证不成立, 结论11得证!

显然 $j=2$ 时至多存在 1 个 $i$ 使 $(i, j)$ 是 “好对”, 结合(1)即知:

$$
N \leq 1+2 \cdot 98=197
$$

综上, 所求 $N$ 最大值为 197 .

评注 本题的构造可通过下列经典问题想到:

设 $a, b, c, d \in \mathbb{Z}^{+}$, 若

$$
\left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right|=1
$$

则

$$
\frac{a}{c}>\frac{a+b}{c+d}>\frac{b}{d}
$$

且

$$
\left|\begin{array}{ll}
a & a+b \\
c & c+d
\end{array}\right|=\left|\begin{array}{ll}
a+b & b \\
c+d & d
\end{array}\right|=1
$$

证明部分也不难.

5. 在平面直角坐标系 $x O y$ 中, 称一个有限点集 $S$ 是“超定的”,如果 $|S| \geq 2$且存在一个次数不超过 $|S|-2$ 的非零实系数多项式 $P(t)$, 满足对 $S$ 中的每个点 $(x, y)$, 均有 $P(x)=y$.

给定整数 $n \geq 2$, 求最大整数 $k=k(n)$, 使得存在一个 $n$ 元点集不是超定的,且这个点集有 $k$ 个超定的子集.

解 结论是: $k$ 最大值为 $2^{n-1}-n$. 设 $n$ 元点集为 $T$.

(1) 先给出构造: 令 $T=T^{\prime} \cup\{(0,0)\}$, 其中 $T^{\prime}=\{(i, 1) \mid i=0,1, \cdots, n-2\}$.

一方面, 由于对任意多项式 $P, P(0)=0$ 与 $P(0)=1$ 不同时成立, 显然 $T$不是“超定的”. 另一方面, 令 $P(t)=1$ 即得 $T^{\prime}$ 的任意 $\geq 2$ 元子集均是“超定的”.故

$$
k \geq \sum_{j=2}^{n-1}\left(\begin{array}{c}
n-1 \\
j
\end{array}\right)=\left(\sum_{j=0}^{n-1}\left(\begin{array}{c}
n-1 \\
j
\end{array}\right)\right)-\left(\begin{array}{c}
n-1 \\
1
\end{array}\right)-\left(\begin{array}{c}
n-1 \\
0
\end{array}\right)=2^{n-1}-n .
$$

其中, 约定 $\sum_{j=2}^{1}$ 表示空求和. 从而 $k \geq 2^{n-1}-n$ 可以取到.

(2) 证明总有 $\left.k \leq 2^{n-1}-n\right)$.

设 $T$ 的所有”超定的”子集组成集族 $F$. 记 $F_{2}, F_{3}, \cdots, F_{n}$ 分别是 $F$ 中 $2,3, \cdots, n$ 元集合组成的集族. 显然

$$
|F|=\left|F_{2}\right|+\left|F_{3}\right|+\cdots+\left|F_{n}\right|,
$$

且 $\left|F_{n}\right|=0$.

我们证明一个引理

引理 $\quad$ 对 $I \subseteq T$, 及 $\beta, \beta^{\prime} \in T \backslash I\left(I \neq \varnothing, \beta \neq \beta^{\prime}\right)$. 若

$$
I \cup\{\beta\}, I \cup\left\{\beta^{\prime}\right\} \in F,
$$

则

$$
I \cup\left\{\beta, \beta^{\prime}\right\} \in F
$$

证明 由 $F$ 的定义知, 存在实系数多项式 $P, Q$, 满足

$$
\operatorname{deg} P, \operatorname{deg} Q \leq|I|-1,
$$

且对任意 $(x, y) \in I \cup\{\beta\}$, 有 $P(x)=y$. 对任意 $(x, y) \in I \cup\left\{\beta^{\prime}\right\}$, 有 $Q(x)=y$.于是对任意 $(x, y) \in I$, 有 $P(x)=Q(x)=y$. 显然 $I$ 中点的横坐标两两不同, 否则 $P, Q$ 不存在. 故结合 $\operatorname{deg} P, \operatorname{deg} Q \leq|I|-1$ 及拉格朗日插值公式知：只能 $P=Q$. 进而对任意 $(x, y) \in I \cup\left\{\beta, \beta^{\prime}\right\}$, 有 $P(x)=y$, 故 $I \cup\left\{\beta, \beta^{\prime}\right\} \in F$, 引理得证!
回到原题, 对 $i=n, n-1, \cdots 2$, 归纳证明:

$$
\left|F_{i}\right| \leq\left(\begin{array}{c}
n-1 \\
i
\end{array}\right)
$$

$i=n$ 时, 由于 $T$ 不是 “超定的”, 故

$$
\left|F_{n}\right|=0=\left(\begin{array}{c}
n-1 \\
n
\end{array}\right)
$$

(1)成立.

$i \in[2, n-1]$ 时, 假设(1)在 $i$ 更大时均成立, 则 $\left|F_{i+1}\right| \leq\left(\begin{array}{c}n-1 \\ i+1\end{array}\right)$. 记 $\left(\begin{array}{c}T \\ i+1\end{array}\right)$ 表示 $T$ 的所有 $(i+1)$ 元子集组成的集族. 构造一个二部图 $G=\left(V_{1}, V_{2}, E\right)$, 其中

$$
V_{1}=F_{i}, V_{2}=\left(\begin{array}{c}
T \\
i+1
\end{array}\right), E=\left\{(I, J) \mid I \in V_{1}, J \in V_{2}, I \subseteq J\right\}
$$

显然, $V_{1}$ 中每个点度数恰为 $n-i, V_{2} \cap F_{i+1}$ 中每个度数 $\leq i+1$, 且由引理知:

$$
V_{2} \backslash F_{i+1} \text { 中每个度数 } \leq 1
$$

若不然, 则存在 $J, J^{\prime} \in F_{i}\left(J \neq J^{\prime}\right), L \in V_{2} \backslash F_{i+1}$, 且 $J, J^{\prime} \subseteq L$, 在引理中令

$$
I=J \cap J^{\prime},\{\beta\}=J \backslash J^{\prime},\left\{\beta^{\prime}\right\}=J^{\prime} \backslash J
$$

即知

$$
L=J \cup J^{\prime} \in F_{i+1},
$$

矛盾! 故

$$
\left|V_{1}\right| \cdot(n-i)=|E| \leq(i+1) \cdot\left|V_{2} \cap F_{i+1}\right|+\left|V_{2} \backslash F_{i+1}\right|,
$$

即

$$
\left|F_{i}\right| \cdot(n-i) \leq(i+1) \cdot\left|F_{i+1}\right|+\left(\begin{array}{c}
n \\
i+1
\end{array}\right)-\left|F_{i+1}\right| .
$$

从而

$$
\begin{aligned}
\left|F_{i}\right| & \leq \frac{i \cdot\left|F_{i+1}\right|+\left(\begin{array}{c}
n \\
i+1
\end{array}\right)}{n-i} \leq \frac{i \cdot\left(\begin{array}{c}
n-1 \\
i+1
\end{array}\right)+\left(\begin{array}{c}
n \\
i+1
\end{array}\right)}{n-i}(\text { 由归假 }) \\
& =\frac{i \cdot\left(\begin{array}{c}
n-1 \\
i
\end{array}\right) \cdot \frac{n-1-i}{i+1}+\left(\begin{array}{c}
n-1 \\
i
\end{array}\right) \cdot \frac{n}{i+1}}{n-i} \\
& =\left(\begin{array}{c}
n-1 \\
i
\end{array}\right) \cdot \frac{i \cdot \frac{n-1-i}{i+1}+\frac{n}{i+1}}{n-i}=\left(\begin{array}{c}
n-1 \\
i
\end{array}\right) .
\end{aligned}
$$

故(1)对 $i$ 成立, 由归纳法知结论(1)得证!

由(1)知:

$$
k=|F|=\sum_{j=2}^{n}\left|F_{j}\right| \leq \sum_{j=2}^{n-1}\left(\begin{array}{c}
n-1 \\
j
\end{array}\right)
$$

$$
\begin{aligned}
& =\left(\sum_{j=0}^{n-1}\left(\begin{array}{c}
n-1 \\
j
\end{array}\right)\right)-\left(\begin{array}{c}
n-1 \\
1
\end{array}\right)-\left(\begin{array}{c}
n-1 \\
0
\end{array}\right) \\
& =2^{n-1}-n .
\end{aligned}
$$

综上, 所求 $k$ 最大值为 $2^{n-1}-n$.

评注 可以先研究较小的找找感觉, 然后不难想到引理, 这个引理的好处是可以将问题转化为一个纯组合问题(而且运气好的是: 这样的转化足够做出原题,但并不一定的充要的), 后面的组合部分也不难, 归纳十算两次就可以了.

6. 设 $n \geq 2$ 是一个整数, $x_{1} \geq x_{2} \geq \cdots \geq x_{n}, y_{1} \geq y_{2} \geq \cdots \geq y_{n}$ 是 $2 n$ 个实数, 满足 $\sum_{i=1}^{n} x_{i}=\sum_{i=1}^{n} y_{i}=0$, 且 $\sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} y_{i}^{2}=1$. 证明:

$$
\sum_{i=1}^{n}\left(x_{i} y_{i}-x_{i} y_{n+1-i}\right) \geq \frac{2}{\sqrt{n-1}}
$$

证明 记

$$
F=\sum_{i=1}^{n}\left(x_{i} y_{i}-x_{i} y_{n+1-i}\right) \text {. }
$$

由条件知

$$
n=n \cdot \sum_{i=1}^{n} x_{i}^{2}-\left(\sum_{i=1}^{n} x_{i}\right)^{2}=\sum_{1 \leq i \leq j \leq n}\left(x_{i}-x_{j}\right)^{2}
$$

同理

$$
n=\sum_{1 \leq i \leq j \leq n}\left(y_{i}-y_{j}\right)^{2}
$$

下面分 $n$ 奇偶讨论.

情形 $1 \quad n$ 是偶数. 此时,

$$
\begin{aligned}
F & =\sum_{i=1}^{\frac{n}{2}}\left(x_{i} y_{i}+x_{n+1-i} y_{n+1-i}-x_{n+1-i} y_{i}-x_{i} y_{n+1-i}\right) \\
& =\sum_{i=1}^{\frac{n}{2}}\left(x_{i}-x_{n+1-i}\right)\left(y_{i}-y_{n+1-i}\right) .
\end{aligned}
$$

记

$$
l_{i}=x_{i}-x_{n+1-i}, l_{i}^{\prime}=y_{i}-y_{n+1-i}\left(1 \leq i \leq \frac{n}{2}\right)
$$

注意到, 由 (1) 知:

$$
n=\sum_{1 \leq i \leq j \leq n}\left(x_{i}-x_{j}\right)^{2}
$$

$$
\begin{aligned}
= & \sum_{1 \leq i \leq \frac{n}{2}}\left(x_{i}-x_{n+1-i}\right)^{2}+\sum_{1 \leq i<j \leq \frac{n}{2}}\left(\left(x_{i}-x_{j}\right)^{2}+\left(x_{i}-x_{n+1-j}\right)^{2}\right. \\
& \left.+\left(x_{n+1-i}-x_{j}\right)^{2}+\left(x_{n+1-i}-x_{n+1-j}\right)^{2}\right) .
\end{aligned}
$$

其中对 $1 \leq i \leq j \leq n$,

$$
\begin{aligned}
& \left(x_{i}-x_{j}\right)^{2}+\left(x_{i}-x_{n+1-j}\right)^{2}+\left(x_{n+1-i}-x_{j}\right)^{2}+\left(x_{n+1-i}-x_{n+1-j}\right)^{2} \\
= & \left(x_{i}-x_{j}\right)^{2}+\left(x_{i}-x_{j}+l_{j}\right)^{2}+\left(x_{i}-l_{i}-x_{j}\right)^{2}+\left(x_{i}-l_{i}-x_{j}+l_{j}\right)^{2} \\
= & 4 \cdot\left(x_{i}-x_{j}-\frac{l_{i}-l_{j}}{2}\right)^{2}+l_{i}^{2}+l_{j}^{2} \leq\left(l_{i}-l_{j}\right)^{2}+l_{i}^{2}+l_{j}^{2} .
\end{aligned}
$$

其中, 最后的不等号是由 $x_{i} \geq x_{j}, x_{n+1-j} \geq x_{n+1-i}$ 有

$$
0 \leq x_{i}-x_{j}=l_{i}+x_{n+1-i}-l_{j}-x_{n+1-j} \leq l_{i}-l_{j}
$$

进而

$$
\left(x_{i}-x_{j}-\frac{l_{i}-l_{j}}{2}\right)^{2} \leq\left(\frac{l_{i}-l_{j}}{2}\right)^{2}
$$

将 (3) 代入 $(2)$ 得

$$
\begin{aligned}
n & \leq \sum_{1 \leq i \leq \frac{n}{2}} l_{i}^{2}+\sum_{1 \leq i \leq j \leq \frac{n}{2}}\left(\left(l_{i}^{2}+l_{j}^{2}\right)+\left(l_{i}-l_{j}\right)^{2}\right) \\
& =n \cdot \sum_{1 \leq i \leq \frac{n}{2}} l_{i}^{2}-\left(\sum_{1 \leq i \leq \frac{n}{2}} l_{i}\right)^{2} .
\end{aligned}
$$

于是可设 $l_{1}: l_{2}: \cdots: l_{\frac{n}{2}}=t_{1}: t_{2}: \cdots: t_{\frac{n}{2}}$ 且

$$
n=n \cdot \sum_{1 \leq i \leq \frac{n}{2}} t_{i}^{2}-\left(\sum_{1 \leq i \leq \frac{n}{2}} t_{i}\right)^{2}
$$

显然 $l_{1}, l_{2}, \cdots, l_{\frac{n}{2}} \geq 0$, 故可令 $t_{1}, t_{2}, \cdots, t_{\frac{n}{2}} \geq 0$. 显然 $l_{i} \geq t_{i}\left(1 \leq i \leq \frac{n}{2}\right)$. 类似定义 $t_{1}^{\prime}, t_{2}^{\prime}, \cdots, t_{\frac{n}{2}}{ }^{\prime}$, 则

$$
F=\sum_{i=1}^{\frac{n}{2}} l_{i} l_{i}^{\prime} \geq \sum_{i=1}^{\frac{n}{2}} t_{i} t_{i}^{\prime}
$$

$$
n=2 \text { 时, 由 (5) 知只能 } t_{1}=t_{1}^{\prime}=\sqrt{2} \text {, 代入 (6) 知 } F \geq 2=\frac{2}{\sqrt{2-1}} \text {, 原不等式 }
$$

得证.

下设 $n \geq 4$, 记 $M=t_{1}, M^{\prime}=t_{1}^{\prime}, S=t_{1}+\cdots+t_{\frac{n}{2}}, S^{\prime}=t_{1}^{\prime}+\cdots+t_{\frac{n}{2}}{ }^{\prime}$. 由 (6) 及排序不等式知

$$
F \geq t_{1} t_{1}^{\prime}+\frac{1}{\frac{n}{2}-1} \cdot\left(\sum_{2 \leq i \leq \frac{n}{2}} t_{i}\right)\left(\sum_{2 \leq i \leq \frac{n}{2}} t_{i}^{\prime}\right)
$$

$$
\begin{aligned}
& =M M^{\prime}+\frac{2}{n-2} \cdot(S-M)\left(S^{\prime}-M^{\prime}\right) \\
& =\frac{n}{n-2} \cdot\left(M-\frac{2}{n} \cdot S\right)\left(M^{\prime}-\frac{2}{n} \cdot S^{\prime}\right)+\frac{2}{n} \cdot S S^{\prime} .
\end{aligned}
$$

由 (5) 知

$$
n \leq n \cdot S^{2}-S^{2} \Rightarrow S \geq \sqrt{\frac{n}{n-1}}, n \geq n \cdot \frac{S^{2}}{\frac{n}{2}}-S^{2} \Rightarrow S \leq \sqrt{n}
$$

且

$$
n \leq n \cdot \sum_{1 \leq i \leq \frac{n}{2}} M t_{i}-\left(\sum_{1 \leq i \leq \frac{n}{2}} t_{i}\right)^{2} \Rightarrow M \geq \frac{n+S^{2}}{n S} \geq \frac{2}{n} \cdot S
$$

其中对 $1 \leq i \leq \frac{n}{2}, 0 \leq t_{i} \leq M \Rightarrow t_{i}^{2} \leq M t_{i}$, 而 $\frac{n+S^{2}}{n S} \geq \frac{2}{n} \cdot S$ 是因为 $S \leq \sqrt{n}$. 类似有

$$
M \geq \frac{n+{S^{\prime}}^{2}}{n S^{\prime}} \geq \frac{2}{n} \cdot S^{\prime}
$$

将 (8) 代入 (7) 知

$$
\begin{aligned}
F & \geq \frac{n}{n-2} \cdot\left(\frac{n+S^{2}}{n S}-\frac{2}{n} \cdot S\right)\left(\frac{n+S^{\prime 2}}{n S^{\prime}}-\frac{2}{n} \cdot S^{\prime}\right)+S S^{\prime} \cdot \frac{2}{n} \\
& =\frac{n}{n-2} \cdot\left(\frac{1}{S}-\frac{S}{n}\right)\left(\frac{1}{S^{\prime}}-\frac{S^{\prime}}{n}\right)+S S^{\prime} \cdot \frac{2}{n} \\
& =\frac{1}{S S^{\prime}} \cdot \frac{n}{n-2}+S S^{\prime} \cdot \frac{2 n-3}{n(n-2)}-\frac{1}{n-2} \cdot\left(\frac{S}{S^{\prime}}+\frac{S^{\prime}}{S}\right) .
\end{aligned}
$$

从而只需证明: $S, S^{\prime} \in\left[\sqrt{\frac{n}{n-1}}, \sqrt{n}\right]$ 时,

$$
G=\frac{1}{S S^{\prime}} \cdot \frac{n}{n-2}+S S^{\prime} \cdot \frac{2 n-3}{n(n-2)}-\frac{1}{n-2} \cdot\left(\frac{S}{S^{\prime}}+\frac{S^{\prime}}{S}\right) \geq \frac{2}{\sqrt{n-1}}
$$

固定 $S S^{\prime}$, 此时 $\frac{S}{S^{\prime}}+\frac{S^{\prime}}{S}$ 在 $S \in\left\{\sqrt{\frac{n}{n-1}}, \sqrt{n}\right\}$ 或 $S^{\prime} \in\left\{\sqrt{\frac{n}{n-1}}, \sqrt{n}\right\}$ 时取最大值.故只需证明 $S \in\left\{\sqrt{\frac{n}{n-1}}, \sqrt{n}\right\}$ 时 (10) 成立.

当 $S=\sqrt{\frac{n}{n-1}}$ 时, 由均值不等式有

$$
G=\frac{1}{S^{\prime}} \cdot \frac{\sqrt{n}}{\sqrt{n-1}}+S^{\prime} \cdot \frac{1}{\sqrt{n-1} \cdot \sqrt{n}} \geq \frac{2}{\sqrt{n-1}}
$$

当 $S=\sqrt{n}$ 时, 由 $S^{\prime} \geq \sqrt{\frac{n}{n-1}}$ 有

$$
G=S^{\prime} \cdot \frac{2}{\sqrt{n}} \geq \frac{2}{\sqrt{n-1}}
$$

从而 (10) 成立, 代入 (9) 知 $F \geq \frac{2}{\sqrt{n-1}}$, 原不等式得证.

情形 $2 n$ 是奇数 (与情形 2 类似, 但略有不同).

记

$$
l_{i}=x_{i}-x_{n+1-i}, l_{i}^{\prime}=y_{i}-y_{n+1-i}\left(1 \leq i \leq \frac{n-1}{2}\right),
$$

则

$$
F=\sum_{i=1}^{\frac{n-1}{2}} l_{i} \cdot l_{i}^{\prime}
$$

由 (1),

$$
\begin{aligned}
n= & \sum_{1 \leq i \leq j \leq n}\left(x_{i}-x_{j}\right)^{2} \\
= & \sum_{1 \leq i \leq \frac{n-1}{2}} l_{i}^{2}+\sum_{1 \leq i \leq \frac{n-1}{2}}\left(\left(x_{i}-x_{\frac{n+1}{2}}\right)^{2}+\left(x_{n+1-i}-x_{\frac{n+1}{2}}\right)^{2}\right) \\
& +\sum_{1 \leq i \leq j \leq \frac{n-1}{2}}\left(\left(x_{i}-x_{j}\right)^{2}+\left(x_{i}-x_{n+1-j}\right)^{2}+\left(x_{n+1-i}-x_{j}\right)^{2}+\left(x_{n+1-i}-x_{n+1-j}\right)^{2}\right) \\
& \leq \sum_{1 \leq i \leq \frac{n-1}{2}} l_{i}^{2}+\sum_{1 \leq i \leq \frac{n-1}{2}} l_{i}^{2}+\sum_{1 \leq i \leq j \leq \frac{n-1}{2}}\left(l_{i}^{2}+l_{j}^{2}+\left(l_{i}-l_{j}\right)^{2}\right) \\
& =n \cdot \sum_{1 \leq i \leq \frac{n-1}{2}} l_{i}^{2}-\left(\sum_{1 \leq i \leq \frac{n-1}{2}} l_{i}\right)^{2} .
\end{aligned}
$$

其中, 最后一步类似 (3), 对 $1 \leq i \leq \frac{n-1}{2}, x_{i} \geq x_{\frac{n+1}{2}} \geq x_{n+1-i}$ 有

$$
\left(x_{i}-x_{\frac{n+1}{2}}\right)^{2}+\left(x_{n+1-i}-x_{\frac{n+1}{2}}\right)^{2} \leq\left(x_{i}-x_{n+1-i}\right)^{2}=l_{i}^{2} \text {. }
$$

类似 (5), 可设 $l_{1}: l_{2}: \cdots: l_{\frac{n-1}{2}}=t_{1}: t_{2}: \cdots: t_{\frac{n-1}{2}}, t_{1}, t_{2} \cdots, t_{\frac{n-1}{2}} \geq 0$, 且

$$
n=n \cdot \sum_{1 \leq i \leq \frac{n-1}{2}} t_{i}^{2}-\left(\sum_{1 \leq i \leq \frac{n-1}{2}} t_{i}\right)^{2}
$$

类似定义 $t_{1}^{\prime}, t_{2}^{\prime} \cdots, t_{\frac{n-1}{2}}{ }^{\prime}$, 则

$$
F \geq \sum_{1 \leq i \leq \frac{n-1}{2}} t_{i} t_{i}^{\prime}
$$

$n=3$ 时, 由 (12) 知 $t_{1}=t_{1}^{\prime}=\sqrt{\frac{3}{2}}, F \geq \frac{3}{2} \geq \frac{2}{\sqrt{3-1}}$, 下设 $n \geq 5$ : 记

$$
M=t_{1}, M^{\prime}=t_{1}^{\prime}, S=t_{1}+\cdots+t_{\frac{n-1}{2}}, S^{\prime}=t_{1}^{\prime}+\cdots+t_{\frac{n-1}{2}}{ }^{\prime} .
$$

由 (13) 及排序不等式, 类似 (7) 可得,

$$
\begin{aligned}
F & \geq M M^{\prime}+\frac{2}{n-3} \cdot(S-M)\left(S^{\prime}-M^{\prime}\right) \\
& =\frac{n-1}{n-3} \cdot\left(M-\frac{2}{n-1} \cdot S\right)\left(M^{\prime}-\frac{2}{n-1} \cdot S^{\prime}\right)+\frac{2}{n-1} \cdot S S^{\prime} .
\end{aligned}
$$

由 (12) 得

$$
n \leq n S^{2}-S^{2} \Rightarrow S \geq \sqrt{\frac{n}{n-1}}, n \geq n \cdot \frac{S^{2}}{\left(\frac{n-1}{2}\right)}-S^{2} \Rightarrow S \leq \sqrt{\frac{n(n-1)}{n+1}}
$$

且类似 $(8)$ 有

$$
n \leq n \cdot \sum_{1 \leq i \leq \frac{n-1}{2}} t_{i} M-\left(\sum_{1 \leq i \leq \frac{n-1}{2}} t_{i}\right)^{2} \Rightarrow M \geq \frac{n+S^{2}}{n S} \geq \frac{2}{n-1} \cdot S
$$

将 (15) 代入 (14) 得

$$
\begin{aligned}
F & \geq \frac{n-1}{n-3} \cdot\left(\frac{1}{S}-S \cdot \frac{n+1}{n(n-1)}\right)\left(\frac{1}{S^{\prime}}-S^{\prime} \cdot \frac{n+1}{n(n-1)}\right)+\frac{2}{n-1} \cdot S S^{\prime} \\
& =\frac{1}{S S^{\prime}} \cdot \frac{n-1}{n-3}+S S^{\prime} \cdot \frac{2 n^{2}-3 n-1}{n^{2}(n-3)}-\frac{(n+1)}{n(n-3)} \cdot\left(\frac{S}{S^{\prime}}+\frac{S^{\prime}}{S}\right) .
\end{aligned}
$$

类似 (10), 只需证明: $S \in\left\{\sqrt{\frac{n}{n-1}}, \sqrt{\frac{n(n-1)}{n+1}}\right\}$ 时, (16) 右边 $\geq \frac{2}{\sqrt{n-1}}$.

当 $S=\sqrt{\frac{n}{n-1}}$ 时, 由均值不等式有

$$
\text { (16) 右边 }=\frac{1}{S^{\prime}} \cdot \frac{\sqrt{n}}{\sqrt{n-1}}+S^{\prime} \cdot \frac{1}{\sqrt{n-1} \cdot \sqrt{n}} \geq \frac{2}{\sqrt{n-1}} \text {. }
$$

当 $S=\sqrt{\frac{n(n-1)}{n+1}}$ 时, 由 $S^{\prime} \geq \sqrt{\frac{n}{n-1}}$ 有

(16) 右边 $=S^{\prime} \cdot \frac{2 \sqrt{n}}{\sqrt{n+1} \cdot \sqrt{n-1}} \geq \frac{2 n}{\sqrt{n+1} \cdot(n-1)}>\frac{2}{\sqrt{n-1}}$.

故 $F \geq \frac{2}{\sqrt{n-1}}$, 原不等式得证.

综上两种情形中均有 $F \geq \frac{2}{\sqrt{n-1}}$, 原不等式得证!

评注 首先注意到结论是平移不变的, 这意味着条件“ $\sum x_{i}=0, \sum x_{i}{ }^{2}=$ 1 ”只需利用其中的 “ $\sum_{i<j}\left(x_{i}-x_{j}\right)^{2}=n$ ” (这一步其实不一定是好的, 反面例子的是: IMO 2003 第 5 题: $x_{1} \leq \cdots \leq x_{n}\left(n \in \mathbb{Z}^{+}\right)$, 证明:

$$
\left(\sum_{i . j=1}^{n}\left|x_{i}-x_{j}\right|\right)^{2} \leq \frac{2\left(n^{2}-1\right)}{3} \cdot \sum_{i . j=1}^{n}\left(x_{i}-x_{j}\right)^{2}
$$

反倒要加上 $\sum x_{i}=0$ 再利用柯西), 接下来容易将问题转化为式 (5), (6) (而且是充要的), 下一步的排序不等式直接放会放过头, 要单独取出最大值(优化), 最后的少元问题也不难.

若按此方法做, 步骤其实不算多, 而且排序优化的一步比较有意思, 但是要分奇偶讨论直接让解答长度翻倍。

本题的最优结果如下:

$n$ 是偶数时 $F_{\min }=\frac{2}{\sqrt{n-1}}$, 构造:

$n$ 是奇数时 $F_{\min }=\frac{2 n}{(n-1) \cdot \sqrt{n+1}}$, 构造:

$$
\left(l_{i}\right)=\left(\sqrt{\frac{n}{n-1}}, 0 \cdots, 0\right),\left(l_{i}^{\prime}\right)=\left(\frac{2}{\sqrt{n}}, \cdots \frac{2}{\sqrt{n}}\right) .
$$

$$
\left(l_{i}\right)=\left(\sqrt{\frac{n}{n-1}}, 0 \cdots, 0\right),\left(l_{i}^{\prime}\right)=\left(2 \cdot \sqrt{\frac{n}{n^{2}-1}}, \cdots, 2 \cdot \sqrt{\frac{n}{n^{2}-1}}\right) .
$$

$x_{1}=\cdots=x_{\left[\frac{n+1}{2}\right]}, y_{1}=\cdots=y_{\left[\frac{n+1}{2}\right]}$.

本题还有一个用概率的神奇做法: 随机取 $1,2, \cdots, n$ 的一个排列 $\sigma$, 记

$$
S(\sigma)=\sum x_{i} y_{\sigma(i)}
$$

计算 $S(\sigma)$ 的平均, 方差, 以及最大最小值之差即可(不需分奇偶).

