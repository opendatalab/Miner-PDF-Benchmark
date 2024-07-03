数学新星网 $*$ 教师专栏

www.nsmath.cn/jszl

# 哈佛一麻省数学竞赛春季团体赛试题解析 

张甲<br>(郑州一中, 451152)

本文给出 2020 年哈佛一麻省春季团体赛的题目解析和简评. 该比赛时间为 2020 年 2 月 15 日. 试题新颖而有趣. 题目总体难度梯度明显, 其中第 $1,2,3$ 题较为简单, 第 $4,5,6,7$ 题是高中联赛难度, 第 8,9 题是 CMO 的第二, 五题难度,第 10 题是 CMO 的第三, 六题难度. 本文的不当之处请读者批评指正.

## I. 试 题

1. 设 $n$ 为正整数. 数列 $\left\{a_{n}\right\}$ 满足: $a_{0}=1, a_{2 i+1}=a_{i}, a_{2 i+2}=a_{i}+a_{i+1}, i \geq 0$,求 $a_{0}+a_{1}+a_{2}+\cdots+a_{2^{n}-1}$ 的值.
2. 设 $n$ 为给定的正整数. 一个 “ $n$ 级阶梯” 指由 $\frac{n(n+1)}{2}$ 个单元格按照阶梯的形状组成的任意大小的图形, 下图是两个 5 级阶梯的例子.


证明：任意一个 $n$ 级阶梯都可以被拆分为若干个比它小的 $n$ 级阶梯.

3. 如图 (见下页), $\triangle A B C$ 内接于圆 $\omega, l$ 为过点 $A$ 的 $\omega$ 的切线. 过点 $B$ 作 $A C$ 的平行线交 $l$ 于点 $P$, 过点 $C$ 作 $A B$ 的平行线交 $l$ 于点 $Q . \triangle A B P$ 与 $\triangle A C Q$的外接圆再次相交于点 $S$. 证明: $A S$ 平分 $B C$.
4. 叮当在平面上画了一个凸 2020 边形 $A=A_{1} A_{2} \cdots A_{2020}$, 每个顶点按顺时针排列, 随后他选择了 2020 个角 $\theta_{1}, \theta_{2}, \cdots, \theta_{2020} \in(0, \pi)$, 且其和为 $1010 \pi$. 然后他在凸 2020 边形 $A$ 的外侧构造了 2020 个点 $B_{1}, B_{2}, \cdots, B_{2020}$, 使得[^0]



$B_{i} A_{i}=B_{i} A_{i+1}, \angle A_{i} B_{i} A_{i+1}=\theta_{i},\left(A_{2021}=A_{1}\right)$. 接下来, 叮当擦除了这个凸 2020 边形 $A$ 以及点 $B_{1}$. 如果叮当告诉米多这 2020 个角 $\theta_{1}, \theta_{2}, \cdots, \theta_{2020}$ 分别是多少, 请证明米多一定能够根据其余 2019 个点的位置找出点 $B_{1}$ 的位置.

5. 已知 $a_{0}, b_{0}, c_{0}, a, b, c$ 为满足 $\operatorname{gcd}\left(a_{0}, b_{0}, c_{0}\right)=\operatorname{gcd}(a, b, c)=1$ 的整数. 证明: 存在正整数 $n$, 以及整数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}, c_{1}, c_{2}, \cdots, c_{n}$, 其中 $a_{n}=a, b_{n}=b, c_{n}=c$. 使得对任意的 $1 \leq i \leq n$, 均有 $a_{i-1} a_{i}+b_{i-1} b_{i}+c_{i-1} c_{i}=1$.
6. 设 $n$ 为正整数, $n>1, S$ 为 $\{1,2, \cdots, 2 n\}$ 的 $\frac{1}{2} \mathrm{C}_{2 n}^{n}$ 个 $n$ 元子集组成的集合. 证明: 存在 $A, B \in S$, 使得 $|A \cap B| \leq 1$.
7. 正实数 $x, y$ 满足

$$
|| \cdots|||x|-y|-x| \cdots-y|-x|=|| \cdots|||y|-x|-y| \cdots-x|-y|,
$$

其中左右两边各有 2019 个绝对值符号. 求 $\frac{x}{y}$ 所有可能的值.

8. 不等边 $\triangle A B C$ 中, $A D, B E, C F$ 分别为角平分线, 其中点 $D, E, F$ 分别在 $B C, C A, A B$ 上. $M, N$ 分别为 $B C$ 和 $E F$ 的中点. 过点 $M$ 作 $A D$ 的平行线, 交直线 $A N$ 于点 $P$. 证明: 点 $P$ 在 $\triangle A B C$ 外接圆上的充分必要条件是 $D E=D F$.



9. 设 $p$ 为素数, $p>5$. 证明: 存在整数 $n$, 以及素数 $q, q<p$, 使得 $p \mid n^{2}-q$.
10. 给定正整数 $n$, 对 $n$ 个正整数 $a_{1}, a_{2}, a_{3}, \cdots, a_{n}$. 设 $\pi$ 为前 $n$ 个正整数的一个排列, $S_{\pi}=\left\{i \left\lvert\, \frac{a_{i}}{\pi(i)} \in \mathbb{Z}\right.\right\}$. 设 $N$ 表示当 $\pi$ 遍历前 $n$ 个正整数的所有排列时, 得到的不同 $S_{\pi}$ 的个数. 那么, 当 $a_{1}, a_{2}, a_{3}, \cdots, a_{n}$ 变化时, 求 $N$ 的最大值 (用 $n$ 表示).

## II. 解 答

题 1 设 $n$ 为正整数. 数列 $\left\{a_{n}\right\}$ 满足: $a_{0}=1, a_{2 i+1}=a_{i}, a_{2 i+2}=a_{i}+a_{i+1}$, $i \geq 0$, 求 $a_{0}+a_{1}+a_{2}+\cdots+a_{2^{n}-1}$ 的值.

解 (全本然、冯正喜) 答案为: $\frac{3^{n}+1}{2}$.

引理 $n \geq 1$ 时, $\sum_{i=2^{n}}^{2^{n+1}-1} a_{i}=3^{n}$.

证明 由已知计算得 $a_{0}=1, a_{1}=1, a_{2}=2, a_{3}=1$, 故 $n=1$ 时结论成立.

假设 $n=k$ 时结论成立, 当 $n=k+1$ 时,

$$
\begin{aligned}
\sum_{i=2^{k+1}}^{2^{k+2}-1} a_{i} & =\sum_{\substack{2^{k+1} \leq i \leq 2^{k+2}-1 \\
i \text { 为奇数 }}} a_{i}+\sum_{\substack{2^{k+1} \leq i \leq 2^{k+2}-1 \\
i \text { 为偶数 }}} a_{i} \\
& =\sum_{i=2^{k}}^{2^{k+1}-1} a_{i}+2 \sum_{i=2^{k}}^{2^{k+1}-1} a_{i}+a_{2^{k}-1}-a_{2^{k+1}-1} \\
& =3 \sum_{i=2^{k}}^{2^{k+1}-1} a_{i} \\
& =3 \times 3^{k}=3^{k+1} .
\end{aligned}
$$

由数学归纳法知, 对一切 $n \geq 1$ 时, $\sum_{i=2^{n}}^{2^{n+1}-1} a_{i}=3^{n}$, 引理得证.

回到原题, 得

$$
\begin{aligned}
a_{0}+a_{1}+a_{2}+\cdots+a_{2^{n}-1} & =1+1+3+3^{2}+\cdots+3^{n-1} \\
& =1+\frac{3^{n}-1}{2}=\frac{3^{n}+1}{2} .
\end{aligned}
$$

评注 这是一道简单的递推数列问题, 由条件自然想到归纳法或者直接研究递推关系, 分奇偶讨论找到一般的递推关系分组求和即可得到解答.

题 2 设 $n$ 为给定的正整数. 一个 “ $n$ 级阶梯” 指由 $\frac{n(n+1)}{2}$ 个单元格按照阶梯的形状组成的任意大小的图形, 下图是两个 5 级阶梯的例子.


证明：任意一个 $n$ 级阶梯都可以被拆分为若干个比它小的 $n$ 级阶梯.

证明 (蒋明序) 首先证明:一个单元格可以被分拆为若干个 $n$ 级阶梯.

如图, 两个 $n$ 级阶梯可以拼成一个 $n \times(n+1)$ 的矩形. 将这样的矩形摆 $(n+1)$ 行 $n$ 列即可拼成一个边长为 $n \times(n+1)$的单元格.



于是, 一个由 $\frac{n \times(n+1)}{2}$ 个单元格组成的 $n$ 级阶梯自然可以被拆分为若干个小的 $n$ 级阶梯.

评注 此题简单有趣, 用转化思想, 像拼积木一样把小单元格拼好, 那拼大单元格就容易了.

题 $3 \triangle A B C$ 内接于圆 $\omega, l$ 为过点 $A$ 的 $\omega$ 的切线. 过点 $B$ 作 $A C$ 的平行线交 $l$ 于点 $P$, 过点 $C$ 作 $A B$ 的平行线交 $l$ 于点 $Q . \triangle A B P$ 与 $\triangle A C Q$ 的外接圆再次相交于点 $S$. 证明: $A S$ 平分 $B C$.



证明 (蒋明序) 由 $l$ 为 $\omega$ 的切线知 $\angle B C A=\angle P A B$, 又 $P B / / A C$, 故 $\angle B A C=\angle P B A$, 于是 $\triangle B A C \sim \triangle P B A$, 所以 $\angle A P B=\angle A B C$, 可得 $B C$ 为 $\triangle A P B$ 外接圆的切线. 同理 $B C$ 为 $\triangle A Q C$ 外接圆的切线.

设 $A S$ 交 $B C$ 于点 $M$,则

$$
M B^{2}=M S \cdot M A=M C^{2}
$$

于是 $M B=M C$, 从而 $A S$ 平分 $B C$.

评注 这是一道简单题, 直接用相似和圆的基本知识即可完成证明.
题 4 叮当在平面上画了一个凸 2020 边形 $A=A_{1} A_{2} \cdots A_{2020}$, 每个顶点按顺时针排列, 随后他选择了 2020 个角 $\theta_{1}, \theta_{2}, \cdots, \theta_{2020} \in(0, \pi)$ ，且其和为 $1010 \pi$. 然后他在凸 2020 边形 $A$ 的外侧构造了 2020 个点 $B_{1}, B_{2}, \cdots, B_{2020}$, 使得 $B_{i} A_{i}=B_{i} A_{i+1}, \angle A_{i} B_{i} A_{i+1}=\theta_{i},\left(A_{2021}=A_{1}\right)$. 接下来, 叮当擦除了这个凸 2020 边形 $A$ 以及点 $B_{1}$. 如果叮当告诉米多这 2020 个角 $\theta_{1}, \theta_{2}, \cdots, \theta_{2020}$ 分别是多少, 请证明米多一定能够根据其余 2019 个点的位置找出点 $B_{1}$ 的位置.

证明 (郭恒恺) 任意建立一复平面, 并用每个点的字母表示它的位置.

因为 $\triangle A_{1} B_{1} A_{2}$ 是顶角为 $\theta_{1}$ 的等腰三角形, 所以 $\frac{B_{1}-A_{1}}{B_{1}-A_{2}}=e^{-i \theta_{1}}$. 于是

$$
A_{2} e^{-i \theta_{1}}=B_{1}\left(e^{-i \theta_{1}}-1\right)+A_{1} \text {. }
$$

同理可得:

$$
A_{k+1} e^{-i \theta_{k}}=B_{k}\left(e^{-i \theta_{k}}-1\right)+A_{k}, \quad k=2,3, \cdots, 2020
$$

所以

$$
\begin{aligned}
& \sum_{k=1}^{2020} A_{k+1} e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{k}\right)}=\sum_{k=1}^{2020}\left[B_{k}\left(e^{-i \theta_{k}}-1\right)+A_{k}\right] e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{k-1}\right)} \\
& \quad=\sum_{k=1}^{2020} B_{k}\left(e^{-i \theta_{k}}-1\right) e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{k-1}\right)}+\sum_{k=1}^{2020} A_{k} e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{k-1}\right)}
\end{aligned}
$$

可得

$$
A_{1} e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{2020}\right)}=\sum_{k=1}^{2020} B_{k}\left(e^{i \theta_{k}}-1\right) e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{k-1}\right)}+A_{1} .
$$

又由于

$$
\theta_{1}+\theta_{2}+\cdots+\theta_{2020}=1010 \pi
$$

所以

$$
\sum_{k=1}^{2020} B_{k}\left(e^{-i \theta_{k}}-1\right) e^{-i\left(\theta_{1}+\theta_{2}+\cdots+\theta_{k-1}\right)}=0
$$

此式子表明: $B_{1}$ 的位置由 $B_{2}, B_{3}, \cdots, B_{2020}, \theta_{1}, \theta_{2}, \cdots, \theta_{2020}$ 给定.

命题得证.

评注 刻画平面上点的位置, 尤其与旋转或夹角有关的问题, 复数是一个不错的选择。

题 5. 已知 $a_{0}, b_{0}, c_{0}, a, b, c$ 为满足 $\operatorname{gcd}\left(a_{0}, b_{0}, c_{0}\right)=\operatorname{gcd}(a, b, c)=1$ 的整数. 证明: 存在正整数 $n$, 以及整数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}, c_{1}, c_{2}, \cdots, c_{n}$, 其中 $a_{n}=a, b_{n}=b, c_{n}=c$. 使得对任意的 $1 \leq i \leq n$, 均有 $a_{i-1} a_{i}+b_{i-1} b_{i}+c_{i-1} c_{i}=1$.
证明 (郭语涵) 先证明如下引理:

引理 若 $x, y, z \in \mathbb{Z}, \operatorname{gcd}(x, y, z)=1, x, y, z$ 均不为零, 则存在 $x^{\prime}, y^{\prime}, z^{\prime} \in$ $\mathbb{Z}$, 满足 $x x^{\prime}+y y^{\prime}+z z^{\prime}=1$ (这也蕴含 $\left.\operatorname{gcd}\left(x^{\prime}, y^{\prime}, z^{\prime}\right)=1\right)$, 且

$$
\min \left\{\left|x^{\prime}\right|,\left|y^{\prime}\right|,\left|z^{\prime}\right|\right\}<\min \{|x|,|y|,|z|\}
$$

证明 由 Bezout 定理, 存在 $x_{0}, y_{0}, z_{0} \in \mathbb{Z}$, 满足 $x x_{0}+y y_{0}+z z_{0}=1$.

不妨设 $\min \{|x|,|y|,|z|\}=|z|$, 则对任意的 $k \in \mathbb{Z}$, 有

$$
x x_{0}+y\left(y_{0}+k z\right)+z\left(z_{0}-k y\right)=1 .
$$

因为 $|z| \geq 1$, 所以存在整数 $k$ 使

$$
-(|z|-1)-y_{0} \leq k z \leq|z|-1-y_{0}, \quad(2|z|-1 \geq|z|)
$$

即:

$$
\left|y_{0}+k z\right| \leq|z|-1<|z|
$$

故令 $x^{\prime}=x_{0}, y^{\prime}=y_{0}+k z, z^{\prime}=z_{0}-k y$ 即可, 引理得证.

回到原题. 对 $a_{0}, b_{0}, c_{0}$ 使用引理, 存在整数 $x_{1}, y_{1}, z_{1}$, 满足 $a_{0} x_{1}+b_{0} y_{1}+$ $c_{0} z_{1}=1$, 且 $\min \left\{\left|x_{1}\right|,\left|y_{1}\right|,\left|z_{1}\right|\right\}<\min \left\{\left|a_{0}\right|,\left|b_{0}\right|,\left|c_{0}\right|\right\}$. 若 $x_{1}, y_{1}, z_{1}$ 均不为 0 ,再对 $x_{1}, y_{1}, z_{1}$ 使用引理, 得到 $x_{2}, y_{2}, z_{2}$, 依此类推.

注意每个三数组的三项的绝对值的最小值严格减小, 故必然在有限步后变为 0 . 即存在 $k \in \mathbb{N}_{+}, x_{i}, y_{i}, z_{i} \in \mathbb{Z}(i=1,2, \cdots, k)$, 满足

$$
\begin{aligned}
a_{0} x_{1}+b_{0} y_{1}+c_{0} z_{1} & =x_{1} x_{2}+y_{1} y_{2}+z_{1} z_{2}=x_{2} x_{3}+y_{2} y_{3}+z_{2} z_{3} \\
& =\cdots=x_{k-1} x_{k}+y_{k-1} y_{k}+z_{k-1} z_{k}=1
\end{aligned}
$$

且 $x_{k}, y_{k}, z_{k}$ 中有一个数为 0 , 不妨设 $z_{k}=0$. 于是 $\left(x_{k}, y_{k}\right)=1$, 由 Bezout 定理,存在 $p, q \in \mathbb{Z}$, 使得 $p x_{k}+q y_{k}=1$. 从而

$$
x_{k} p+y_{k} q+z_{k} \cdot 1=1, p \cdot 0+q \cdot 0+1 \cdot 1=1,
$$

故

$$
\begin{aligned}
a_{0} x_{1}+b_{0} y_{1}+c_{0} z_{1} & =x_{1} x_{2}+y_{1} y_{2}+z_{1} z_{2}=x_{2} x_{3}+y_{2} y_{3}+z_{2} z_{3} \\
& =\cdots=x_{k+1} x_{k+2}+y_{k+1} y_{k+2}+z_{k+1} z_{k+2}=1
\end{aligned}
$$

且

$$
x_{k+2}=y_{k+2}=0, z_{k+2}=1,\left(x_{k+1}=p, y_{k+1}=q, z_{k+1}=1\right) .
$$

同理, 从 $a, b, c$ 开始, 也可以找到类似的一串数, 且以两个 0, 一个 1 的三数组结
尾 $\left(\right.$ 记为 $\left.d_{i}, e_{i}, f_{i}(i=1,2, \cdots, l+2)\right)$. 注意

$$
0 \times 0+0 \times 1+1 \times 1=0 \times 0+1 \times 1+1 \times 0=1
$$

故若 $f_{l+2}=1$, 可直接将两串数以 $(0,0,1)$ 对接. 若 $e_{l+2}=1$, 在 $(0,0,1)$ 与 $(0,1,0)$ 之间加入 $(0,1,1)$ 后对接. 若 $d_{l+2}=1$, 同理.

综上所述, 命题得证.

评注 这是一道中等难度的数论题, 由条件自然想到 Bezout 定理, 利用操作调整的方法将其中一个变量降为 0 即可得到证明.

题 6. 设 $n$ 为正整数, $n>1, S$ 为 $\{1,2, \cdots, 2 n\}$ 的 $\frac{1}{2} \mathrm{C}_{2 n}^{n}$ 个 $n$ 元子集组成的集合. 证明: 存在 $A, B \in S$, 使得 $|A \cap B| \leq 1$.

证明 (郭恒恺、全本然) 反证法.

假设对任意 $A, B \in S$, 有 $|A \cap B|>1$, 即 $|A \cap B| \neq 0$ 或 1 , 记

$$
U=\{1,2, \cdots, 2 n\}
$$

将 $U$ 的 $\mathrm{C}_{2 n}^{n}$ 个 $n$ 元子集分为 $\frac{1}{2} \mathrm{C}_{2 n}^{n}$ 组, 每一组为 $\left\{A, \complement_{U} A\right\}$. 由于 $A \cap \complement_{U} A=\varnothing$,故每一组恰有一个集合属于 $S$, 即 $A \in S$ 等价于 $\complement_{U} A \notin S$.

不妨设 $\{1,2, \cdots, n\} \in S$, 则 $\{2,3, \cdots, n+1\} \in S$, 否则

$$
\{1, n+2, n+3, \cdots, 2 n\} \in S
$$

而它与 $\{1,2, \cdots, n\}$ 的交集为 $\{1\}$, 矛盾.

由上述方法可以依此类推得到 $\{n+1, n+2, \cdots, 2 n\} \in S$, 但是

$$
\{1,2, \cdots, n\} \cap\{n+1, n+2, \cdots, 2 n\}=\varnothing,
$$

矛盾。

故假设不成立, 存在 $A, B \in S$ 满足 $|A \cap B| \leq 1$.

评注 这是一道中等偏易的组合题, 利用反证法, 把 $U$ 的 $n$ 元子集利用补集配对分组推出矛盾即可.

题 7. 正实数 $x, y$ 满足

$$
|| \cdots|||x|-y|-x| \cdots-y|-x|=|| \cdots|||y|-x|-y| \cdots-x|-y|,
$$

其中左右两边各有 2019 个绝对值符号. 求 $\frac{x}{y}$ 所有可能的值.

## 解 (郭恒恺、蒋明序)

1) 当 $x=y$ 时, 左边 $=x=y=$ 右边, 成立.
2) 当 $x>y$ 时,

$$
|||| x|-y|-x|-y|=|| x-y-x|-y|=|y-y|=0 \text {, }
$$

故左边 $=|||x|-y|-x|=y$.

若 $x>2 y$, 则

$$
|||||y|-x|-y|-x|-y|=y
$$

又 $2019 \equiv 3(\bmod 4)$, 故可连续使用此式得到原式右边 $=|||y|-x|-y|=x-2 y$,所以 $x-2 y=y$, 即 $\frac{x}{y}=3$.

若 $x \leq 2 y$, 由于 $|a-b|<\max \{a, b\},(a, b>0)$, 所以

$$
|| y|-x|<x,|||y|-x|-y|<x
$$

依此类推可知

$$
\begin{aligned}
& |\cdots||| y|-x|-y|\cdots-x|<x, \quad \text { (左边含有 } 2018 \text { 个绝对值) } \\
& || \cdots|||y|-x|-y| \cdots-x|-y|<x, \quad \text { (左边含有 } 2017 \text { 个绝对值) }
\end{aligned}
$$

由 (a) 知

$$
|\cdots||| y|-x|-y|\cdots-x|-y<x-y \leq y
$$

而原等式右边 $=y$, 故

$$
|\cdots||| y|-x|-y|\cdots-x|-y=-y
$$

即

$$
|\cdots||| y|-x|-y|\cdots-x|=0, \quad \text { (左边含有 } 2018 \text { 个绝对值) }
$$

从而

$$
|| \cdots|||y|-x|-y| \cdots-x|-y|=x, \quad \text { (左边含有 } 2017 \text { 个绝对值) }
$$

但这与 (b) 矛盾, 此时无解.

3) 当 $x<y$ 时, 同理可得 $\frac{x}{y}=\frac{1}{3}$.

综上所述: $\frac{x}{y}$ 可以为 $1,3, \frac{1}{3}$.

评注 本题左右两边各含有 2019 个绝对值符号, 容易想到化简的时候有可能会有类似周期性或函数迭代的特点, 通过分类讨论, 不断利用 5 个绝对值时候的式子即可.
题 8. 不等边 $\triangle A B C$ 中, $A D, B E, C F$ 分别为角平分线, 其中点 $D, E, F$分别在 $B C, C A, A B$ 上. $M, N$ 分别为 $B C$ 和 $E F$ 的中点. 过点 $M$ 作 $A D$ 的平行线, 交直线 $A N$ 于点 $P$. 证明: 点 $P$ 在 $\triangle A B C$ 外接圆上的充分必要条件是 $D E=D F$.



证明 (郭恒恺) 设 $\triangle A B C$ 点 $A$ 处的外角平分线交直线 $B C$ 于点 $S$.

1) 若 $D E=D F$, 有 $B, D, C, S$ 为调和点列. 设 $A D, B E, C F$ 交于内心 $I$,于是完全四边形 $A F B I C E$ 中, $F E$ 的延长线过点 $S$. 又 $\angle D N S=\angle D A S=$ $90^{\circ}$, 于是 $A, N, D, S$ 四点共圆. 延长 $A N$ 交 $\triangle A B C$ 外接圆于点 $P^{\prime}$, 连接 $P^{\prime} B, P^{\prime} M, P^{\prime} C$.

设直线 $A N$ 与 $\triangle A F E$ 的外接圆的不同于 $A$ 的另一个交点为 $T$, 则

$$
\angle T F E=\angle T A E=\angle P^{\prime} B C,
$$

同理 $\angle T E F=\angle P^{\prime} C B$. 所以 $\triangle B P^{\prime} C \sim \triangle F T E$, 且 $M, N$ 为相似对应点, 故 $P^{\prime} M$ 与 $T N$ 的夹角等于 $F E$ 与 $B C$ 的夹角. 于是

$$
\angle M P^{\prime} A=\angle M S N=\angle N A D
$$

可得 $M P^{\prime} / / A D$, 从而 $P^{\prime}$ 与 $P$ 重合, 即点 $P$ 在 $\triangle A B C$ 外接圆上.



2) 若点 $P$ 在 $\triangle A B C$ 外接圆上, 在 $A N$ 上取点 $Q$, 满足 $Q N=N A$, 则四边形 $A F Q E$ 为平行四边形, 可得

$$
\angle P B C=\angle P A C=\angle Q A E, \angle P C B=\angle P A B=\angle A Q E
$$

从而 $\triangle A Q E \sim \triangle B C P$, 且 $N, M$ 为相似对应点. 所以 $\triangle A N E \sim \triangle B M P$, 可得

$$
\angle A N E=\angle B M P=\angle A D C .
$$

于是 $A, N, D, S$ 四点共圆, 可得 $\angle D N E=90^{\circ} . N$ 为 $E F$ 中点, 所以 $D E=D F$.



综上所述, 点 $P$ 在 $\triangle A B C$ 外接圆上的充分必要条件是 $D E=D F$.

评注 此题是一道设计巧妙的几何题, 命题有射影几何的背景, 利用相似对应关系和同一法可以得到解答. 此题也可以用三角计算或者交比性质完成证明.

题 9. 设 $p>5$ 为素数, 证明: 存在整数 $n$, 以及素数 $q, q<p$, 使得 $p \mid n^{2}-q$.

证明 (李蔚林) 用反证法, 假设对任意的素数 $q<p$, 均不满足 $p \mid n^{2}-q$, 则勒让德符号 $\left(\frac{2}{p}\right)=-1$, 于是 $p \equiv \pm 3(\bmod 8)$.

(1) 若 $p \equiv-3(\bmod 8)$, 由高斯二次互反律知 $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right)=1$, 则 $\left(\frac{p}{q}\right)=-1$,我们取 $q$ 为 $p-1$ 的奇素因子, (因为 $p-1 \equiv-4(\bmod 8)$, 所以当 $p \geq 13$ 时, $p-1$必有奇素因子, 而 $p<13$ 时, 有 $p=5$, 矛盾.)则 $-1=\left(\frac{p}{q}\right)=\left(\frac{1}{q}\right)=1$, 矛盾.

(2) 若 $p \equiv 3(\bmod 8)$, 我们取 $q$ 为 $(p+1)$ 的奇素因子(类似上述证明知 $q$存在).

a) 如果 $q \equiv 1(\bmod 4)$, 由高斯二次互反律知: $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right)=1$, 于是

$$
-1=\left(\frac{p}{q}\right)=\left(\frac{-1}{q}\right)=(-1)^{\frac{q-1}{2}}=1,
$$

矛盾.

b) 如果 $q \equiv 3(\bmod 4)$, 由高斯二次互反律知: $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right)=-1$, 于是

$$
1=\left(\frac{p}{q}\right)=\left(\frac{-1}{q}\right)=(-1)^{\frac{q-1}{2}}=-1 \text {, }
$$

矛盾.

综上所述, 存在整数 $n$, 以及素数 $q, q<p$, 使得 $p \mid n^{2}-q$.

评注 本题的证明需要对二次剩余, 高斯二次互反律较为熟悉, 考虑奇素因
子也是经典手段.

题 10. 给定正整数 $n$, 对 $n$ 个正整数 $a_{1}, a_{2}, a_{3}, \cdots, a_{n}$. 设 $\pi$ 为前 $n$ 个正整数的一个排列, $S_{\pi}=\left\{i \left\lvert\, \frac{a_{i}}{\pi(i)} \in \mathbb{Z}\right.\right\}$. 设 $N$ 表示当 $\pi$ 遍历前 $n$ 个正整数的所有排列时, 得到的不同 $S_{\pi}$ 的个数. 那么, 当 $a_{1}, a_{2}, a_{3}, \cdots, a_{n}$ 变化时, 求 $N$ 的最大值 (用 $n$ 表示).

解 (郭语涵) 答案是: $2^{n}-n$.

设矩阵 $D=\left(d_{i j}\right)$, 其中

$$
d_{i j}=\left\{\begin{array}{cc}
1, & i \mid a_{j} \\
0, & i \nmid a_{j}
\end{array}\right.
$$

对 $\{1,2, \cdots, n\}$ 的一个子集 $S$, 令矩阵 $D_{S}$ 为在 $D$ 中把使 $j \notin S$ 的一切 $d_{i j}$ 的 0 与 1 互换, 即 $0 \rightarrow 1,1 \rightarrow 0$. 注意到 $S=S_{\pi}$ 当且仅当 $\left(D_{S}\right)_{\pi(i) i}=1$ 对 $i=$ $1,2, \cdots, n$ 均成立.

下证: $N \leq 2^{n}-n$, 考虑两种情况.

(1) 如果 $D$ 的所有行两两不同, 则存在 $n$ 个不同的 $S$ 使 $D_{S}$ 的某一行全为 0 . 这时, 显然不存在排列 $\pi$ 使 $S_{\pi}=S$, 从而至多只有 $2^{n}-n$ 个不同的 $S_{\pi}$.

(2) 如果存在 $D$ 的某两行相同, 我们取 $S_{0}$ 使 $D_{S_{0}}$ 有两行均全为 0 . 此时, 对满足与 $S_{0}$ 至多相差一个元素的 $n+1$ 个 $S$ 的取法, (即使 $\left|S \Delta S_{0}\right|=0$ 或 1 的 $n+1$ 个 $S), D_{S}$ 在这两行中至多只有 1 列可以出现 1 , 故不存在两个在这两行且不同列的 1 . 故对这些 $S$, 也不可能有 $S_{\pi}=S$.

从而 $N \leq 2^{n}-n-1$, 故 $N \leq 2^{n}-n$ 得证.

下面我们说明当 $a_{j}=j,(j=1,2, \cdots, n)$ 时, $N=2^{n}-n$. 根据霍尔婚配定理, 我们只需证明:

设 $D_{S}$ 没有一行全为 0 , 任给 $I=\left\{i_{1}, \cdots, i_{k}\right\}$, 均存在至少 $k$ 个 $j$ 的值使得存在 $i \in I$ 满足 $\left(D_{S}\right)_{i j}=1$.

我们称这种 $j$ 为 “可行的”. 不失一般性, 设 $i_{1}<i_{2}<\cdots<i_{k}$. 注意到若 $\left\{d_{i j} \mid i \in I\right\}=\{0,1\}$, 则 $j$ 是可行的. 因此 $i_{1}, \cdots, i_{k-1}$ 均是可行的. (因为对 $\alpha<k, i_{\alpha} \mid i_{\alpha}$, 但 $i_{k}$ 不整除 $i_{\alpha}$ ), 设 $i_{k}$ 不是可行的, 那么一定有对 $\forall \alpha<k, i_{\alpha} \mid i_{k}$.此时 $k=1$ 的情形是平凡的, 因为没有一行全为 0 (即每行均有至少一个 1 ).

若 $k=2,\left\{\left(D_{S}\right)_{i_{1} i_{1}},\left(D_{S}\right)_{i_{2} i_{1}}\right\}=\{0,1\}$, 那个 0 所在的那一行必然还有一个 1 , 即有两个可行的 $j$.

对 $k \geq 3$ 的情形, 注意到 $i_{1} \leq \frac{i_{k}}{3}$, 从而 $i_{k}-i_{1} \notin I$. 但 $i_{1} \mid i_{k}-i_{1}, i_{k}$ 不整除
$i_{k}-i_{1}$, 故又有一个可行的 $j$.

至此, 所有情况讨论完毕. 故 $a_{j}=j,(j=1,2, \cdots, n)$ 时, $N=2^{n}-n$.

综上所述, $N$ 的最大值为 $2^{n}-n$.

评注 本题有一定的难度, 利用矩阵的刻画方式以及根据霍尔婚配定理进行构造都有一定的技巧性。


[^0]:    修订日期: 2020-04-05.

