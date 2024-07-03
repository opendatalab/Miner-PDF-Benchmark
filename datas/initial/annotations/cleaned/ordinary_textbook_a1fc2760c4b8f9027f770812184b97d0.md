# 集合元素关系表在解组合题时的应用 

## 王乐达

(山西大学附属中学, 030006)

集合元素关系表是用一个矩阵 (数表) 描述元素与集合之间的从属关系, 最为常用的就是 $0-1$ 矩阵. 设全集 $S=\{1,2, \cdots, n\}$ 有若干子集 $A_{1}, A_{2}, \cdots, A_{m}$,构造矩阵如下:

$$
\left(\begin{array}{ccccc} 
& 1 & 2 & \cdots & n \\
A_{1} & \varepsilon_{11} & \varepsilon_{12} & \cdots & \varepsilon_{1 n} \\
A_{2} & \varepsilon_{21} & \varepsilon_{22} & \cdots & \varepsilon_{2 n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
A_{m} & \varepsilon_{m 1} & \varepsilon_{m 2} & \cdots & \varepsilon_{m n}
\end{array}\right),
$$

其中

$$
\varepsilon_{i j}= \begin{cases}1, & j \in A_{i} \\ 0, & j \notin A_{i}\end{cases}
$$

也可以类似地构造 $a-b$ 矩阵 $(a, b \in \mathbb{R})$, 分别表示对元素与集合间两种状态 (属于或不属于) 的赋值. 在解题时应对具体题目进行分析后, 确定 $a$ 与 $b$. 集合元素关系表的主要用途, 就是将集合的抽象特征具体过程化. 这样一方面从直观上对题目本质加深理解, 另一方面也提供了解题手段上的便捷, 譬如算两次与不等式放缩.

下面举例说明这一方法的应用.

例 1 (2018 年北大金秋营 $\left.{ }^{[1]}\right)$ 给定整数 $n>1$, 已知正整数 $m$ 和集合 $\{1,2, \cdots, n\}$ 的不同子集 $A_{1}, A_{2}, \cdots, A_{m}$ ，满足对任意 $1 \leq i<j \leq n, A_{1}, A_{2}, \cdots$, $A_{m}$ 中恰好有 $n-j+i$ 个集合同时含有 $i, j$. 求 $\sum_{k=1}^{m}\left|A_{k}\right|^{2}$ 的最小值.

分析与解 直观上可以感觉到, 直接放缩是行不通的: 将这个 “二次和”用常修订日期: 2019-06-14.
见手段放缩后, 其不等式无法继续处理且很难取到等号. 那么我们自然想到先用算两次的方法, 探求和式的实际意义. 为此, 可引入 $0-1$ 矩阵:

$$
\left(\begin{array}{ccccc} 
& 1 & 2 & \cdots & n \\
A_{1} & \varepsilon_{11} & \varepsilon_{12} & \cdots & \varepsilon_{1 n} \\
A_{2} & \varepsilon_{21} & \varepsilon_{22} & \cdots & \varepsilon_{2 n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
A_{m} & \varepsilon_{m 1} & \varepsilon_{m 2} & \cdots & \varepsilon_{m n}
\end{array}\right),
$$

其中

$$
\varepsilon_{i j}= \begin{cases}1, & j \in A_{i} \\ 0, & j \notin A_{i}\end{cases}
$$

从这里可以看出 $0-1$ 矩阵被经常使用的原因是: 一方面, 作为 Boolean 函数的两个取值, $0-1$ 可以最简便地描述集合与元素的某些普通属性; 另一方面, 0 与 1 是方程 $\varepsilon^{2}=\varepsilon$ 的全部解, 可达到降次的目的, 也就是说可将某些不易处理的“高次和”降至一次.

利用 $A_{k}$ 的意义, 有

$$
\begin{aligned}
\sum_{k=1}^{m}\left|A_{k}\right|^{2} & =\sum_{k=1}^{m}\left(\sum_{j=1}^{n} \varepsilon_{k j}\right)^{2} \\
& =\sum_{k=1}^{m}\left(\sum_{j=1}^{n} \varepsilon_{k j}^{2}+2 \sum_{1 \leq i<j \leq n} \varepsilon_{k i} \varepsilon_{k j}\right) \\
& =\sum_{k=1}^{m} \sum_{i=1}^{n} \varepsilon_{k i}+2 \sum_{k=1}^{m} \sum_{1 \leq i<j \leq n} \varepsilon_{k i} \varepsilon_{k j} \\
& =\sum_{i=1}^{n} \sum_{k=1}^{m} \varepsilon_{k i}+2 \sum_{1 \leq i<j \leq n} \sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j},
\end{aligned}
$$

其中利用了 $\varepsilon^{2}=\varepsilon$ 进行降次, 以及求和顺序的交换, 以方便在行与列两个维度间转换.

由 $0-1$ 矩阵的定义, $\varepsilon_{k i} \varepsilon_{k j} \in\{0,1\}$, 且

$$
\varepsilon_{k i} \varepsilon_{k j}=1 \Leftrightarrow \varepsilon_{k i}=\varepsilon_{k j}=1 \Leftrightarrow\{i, j\} \in A_{k} .
$$

故

$$
\varepsilon_{k i} \varepsilon_{k j}= \begin{cases}1, & \{i, j\} \in A_{k}, \\ 0, & \text { 其他情况. }\end{cases}
$$

所以 $\sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j}$ 就是同时含有 $\{i, j\}$ 的子集的个数, 由题意, 这个值就是 $n-j+i$.
进一步,

$$
2 \sum_{1 \leq i<j \leq n} \sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j}=2 \sum_{1 \leq i<j \leq n}(n-j+i)=\frac{1}{3}(n-1) n(2 n-1) .
$$

另一方面 (算两次),

$$
\sum_{k=1}^{m} \varepsilon_{k i} \geq \sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k(i+1)}=n-(i+1)+i=n-1
$$

对 $i=1,2, \cdots, n-1$ 均成立, 且

$$
\sum_{k=1}^{m} \varepsilon_{k n} \geq \sum_{k=1}^{m} \varepsilon_{k n} \varepsilon_{k(n-1)}=n-1
$$

我们现在考虑 $i=2,3, \cdots, n-1$ 时, $\sum_{k=1}^{m} \varepsilon_{k i}=n-1$ 的情况. 这时,

$$
\sum_{k=1}^{m} \varepsilon_{k i}=n-1=\sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k(i-1)}=\sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k(i+1)} .
$$

由于等号成立, 故在 $\varepsilon_{k i}=1$ 时, 必有 $\varepsilon_{k(i-1)}=\varepsilon_{k(i+1)}=1$. 但这说明

$$
\sum_{k=1}^{m} \varepsilon_{k(i-1)} \varepsilon_{k(i+1)} \geq \sum_{k=1}^{m} \varepsilon_{k i}=n-1
$$

与

$$
\sum_{k=1}^{m} \varepsilon_{k(i-1)} \varepsilon_{k(i+1)}=n-(i+1)+i-1=n-2
$$

矛盾! 所以

$$
\sum_{k=1}^{m} \varepsilon_{k i}>n-1 \Rightarrow \sum_{k=1}^{m} \varepsilon_{k i} \geq n, i=2,3, \cdots, n-1
$$

所以

$$
\begin{aligned}
\sum_{k=1}^{m}\left|A_{k}\right|^{2} & =\sum_{i=1}^{n} \sum_{k=1}^{m} \varepsilon_{k i}+2 \sum_{1 \leq i \leq j \leq n} \sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j} \\
& \geq 2(n-1)+n(n-2)+\frac{1}{3}(n-1) n(2 n-1) \\
& =\frac{1}{3}\left(2 n^{3}+n-6\right)
\end{aligned}
$$

最后给出极值构造, 这个不难: 设 $A_{1}=\{1,2\}, A_{2}=\{1,2,3\}, \cdots, A_{n-1}=$ $\{1,2, \cdots, n\}, A_{n}=\{2,3, \cdots, n\}, A_{n+1}=\{3,4, \cdots, n\}, \cdots, A_{2 n-1}=\{n-1, n\}$,这说明

$$
\left(\sum_{k=1}^{m}\left|A_{k}\right|^{2}\right)_{\min }=\frac{1}{3}\left(2 n^{3}+n-6\right)
$$

评注 本题初步介绍了集合元素关系表的应用, 读者已经可以感受到 $0-1$矩阵在算两次与放缩估计中的重要作用。
例 2 (2018 年中国国家集训队选拔第一阶段 $\left.{ }^{[2]}\right)$ 设 $m, n$ 为正整数, $A_{1}, A_{2}, \cdots, A_{m}$ 是某个 $n$ 元集合的 $m$ 元子集. 证明:

$$
\sum_{i=1}^{m} \sum_{j=1}^{m}\left|A_{i}\right| \cdot\left|A_{i} \cap A_{j}\right| \geq \frac{1}{m n}\left(\sum_{i=1}^{m}\left|A_{i}\right|\right)^{3}
$$

分析与解 文献 [2] 《走向 IMO》一书中给出的解答, 是构造二部图结合“算两次”方法求解, 但不易想到. 用 $0-1$ 矩阵解题, 可以让这个解答更易于理解. 不妨设全集 $X=\{1,2, \cdots, n\}$,引入 $0-1$ 矩阵:

$$
\left(\begin{array}{ccccc} 
& 1 & 2 & \cdots & n \\
A_{1} & \varepsilon_{11} & \varepsilon_{12} & \cdots & \varepsilon_{1 n} \\
A_{2} & \varepsilon_{21} & \varepsilon_{22} & \cdots & \varepsilon_{2 n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
A_{m} & \varepsilon_{m 1} & \varepsilon_{m 2} & \cdots & \varepsilon_{m n}
\end{array}\right)
$$

其中

$$
\varepsilon_{i j}= \begin{cases}1, & j \in A_{i} \\ 0, & j \notin A_{i}\end{cases}
$$

考虑局部结构 $\begin{array}{lllll}A_{i} & \varepsilon_{i 1} & \varepsilon_{i 2} & \cdots & \varepsilon_{i n}\end{array}$, 注意到 $k \in A_{i} \cap A_{j} \Leftrightarrow k \in A_{i}$ 且 $\begin{array}{lllll}A_{j} & \varepsilon_{j 1} & \varepsilon_{j 2} & \cdots & \varepsilon_{j n}\end{array}$

$k \in A_{j}$, 可知 $A_{i} \cap A_{j}$ 对应的行为 $\varepsilon_{i 1} \varepsilon_{j 1} \quad \varepsilon_{i 2} \varepsilon_{j 2} \quad \cdots \quad \varepsilon_{i n} \varepsilon_{j n}$. 所以

$$
\begin{aligned}
& \sum_{i=1}^{m} \sum_{j=1}^{m}\left|A_{i}\right| \cdot\left|A_{i} \cap A_{j}\right| \\
= & \sum_{i=1}^{m}\left|A_{i}\right| \cdot \sum_{j=1}^{m}\left(\sum_{k=1}^{n} \varepsilon_{i k} \varepsilon_{j k}\right) \\
= & \sum_{i=1}^{m}\left|A_{i}\right| \cdot \sum_{k=1}^{n}\left(\sum_{j=1}^{m} \varepsilon_{i k} \varepsilon_{j k}\right) \\
= & \sum_{i=1}^{m}\left|A_{i}\right| \cdot \sum_{j=1}^{n} \varepsilon_{i j}\left(\sum_{k=1}^{m} \varepsilon_{k j}\right) .
\end{aligned}
$$

为简便起见, 记每列的和 $\sum_{k=1}^{m} \varepsilon_{k j}=l_{j}$, 则

$$
\sum_{i=1}^{m}\left|A_{i}\right| \cdot \sum_{j=1}^{n} \varepsilon_{i j}\left(\sum_{k=1}^{m} \varepsilon_{k j}\right)=\sum_{i=1}^{m} \sum_{j=1}^{n}\left|A_{i}\right| l_{j} \varepsilon_{i j}
$$

且

$$
\sum_{i=1}^{m}\left|A_{i}\right|=\sum_{i=1}^{n} l_{j}=\sum_{i=1}^{m} \sum_{j=1}^{n} \varepsilon_{i j}
$$

所以要证的不等式等同于

$$
m n \sum_{i=1}^{m} \sum_{j=1}^{n}\left|A_{i}\right| l_{j} \varepsilon_{i j} \geq\left(\sum_{i=1}^{m} \sum_{j=1}^{n} \varepsilon_{i j}\right)^{3}
$$

不妨设 $\left|A_{i}\right| l_{j} \neq 0$, 否则可将某行 (或列) 从这一矩阵中删去, 右侧不变而左侧减小. 注意到 (1) 的结构, 自然地想到 Hölder 不等式, 这仅需用相关式子表示 $m, n$ :

$$
\begin{gathered}
m=\sum_{i=1}^{m} 1=\sum_{i=1}^{m} \frac{\sum_{j=1}^{n} \varepsilon_{i j}}{\left|A_{i}\right|}=\sum_{i=1}^{m} \sum_{j=1}^{n} \frac{\varepsilon_{i j}}{\left|A_{i}\right|}, \\
n=\sum_{j=1}^{n} 1=\sum_{j=1}^{n} \frac{\sum_{i=1}^{m} \varepsilon_{i j}}{l_{j}}=\sum_{i=1}^{m} \sum_{j=1}^{n} \frac{\varepsilon_{i j}}{l_{j}} .
\end{gathered}
$$

代入 (1) 后我们发现, 待证不等式恰为 $m n$ 元 Hölder 不等式, 这自然成立!

评注 利用 $0-1$ 矩阵将题目转化, 为算两次创造了时机, 大大降低了本题的难度.

例 $3\left(2013\right.$ 年罗马尼亚国家队选拔 $\left.{ }^{[3]}\right)$ 求最大的正整数 $r$ 满足: 在任意五个 $\{1,2, \cdots, 1000\}$ 的 500 元子集中, 存在两个子集, 它们交得的元素个数至少是 $r$.

分析与解 直观上, 本题要求出某两个子集之交集的元素个数的下界, 可利用集合元素关系表, 结合平均值原理进行处理. 先将结论一般化, 证明如下引理:

引理 正整数 $n>1, S_{1}, S_{2}, \cdots, S_{n}$ 为有限集 $S$ 的子集, 且 $\sum_{i=1}^{n}\left|S_{i}\right| \geq S$. 记 $N$为最接近 $\sigma$ 的整数之一, 其中 $\sigma=\frac{\sum_{i=1}^{n}\left|S_{i}\right|}{|S|}-\frac{1}{2}$, 则存在 $i<j$, 使得

$$
\left|S_{i} \cap S_{j}\right| \geq \frac{N(2 \sigma-N)}{n(n-1)}|S|
$$

证明 不妨设 $S=\{1,2, \cdots, m\}$, 引入 $0-1$ 矩阵

$$
\left(\begin{array}{ccccc} 
& 1 & 2 & \cdots & n \\
A_{1} & \varepsilon_{11} & \varepsilon_{12} & \cdots & \varepsilon_{1 n} \\
A_{2} & \varepsilon_{21} & \varepsilon_{22} & \cdots & \varepsilon_{2 n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
A_{m} & \varepsilon_{m 1} & \varepsilon_{m 2} & \cdots & \varepsilon_{m n}
\end{array}\right),
$$

其中

$$
\varepsilon_{i j}= \begin{cases}1, & j \in A_{i}, \\ 0, & j \notin A_{i} .\end{cases}
$$

设 $\sum_{k=1}^{n} \varepsilon_{k j}=l_{j}$, 类似于上一题的局部分析, 我们可以得到: $S_{i} \cap S_{j}$ 对应的行为 $\varepsilon_{i 1} \varepsilon_{j 1} \quad \varepsilon_{i 2} \varepsilon_{j 2} \cdots \varepsilon_{i m} \varepsilon_{j m}$.于是

$$
\sum_{1 \leq i<j \leq n}\left|S_{i} \cap S_{j}\right|=\sum_{1 \leq i<j \leq n} \sum_{k=1}^{m} \varepsilon_{i k} \varepsilon_{j k}=\sum_{k=1}^{m} \sum_{1 \leq i<j \leq n} \varepsilon_{i k} \varepsilon_{j k}
$$

在交换求和号后, 交叉积求和的形式可以想到 $l_{k}^{2}$ 的展开式中类似的项. 考虑

$$
l_{k}^{2}=\left(\sum_{l=1}^{n} \varepsilon_{l k}\right)^{2}=\sum_{l=1}^{n} \varepsilon_{l k}^{2}+2 \sum_{1 \leq i<j \leq n} \varepsilon_{i k} \varepsilon_{j k}
$$

所以

$$
\sum_{1 \leq i<j \leq n} \varepsilon_{i k} \varepsilon_{j k}=\frac{1}{2}\left(l_{k}^{2}-\sum_{l=1}^{n} \varepsilon_{l k}^{2}\right)=\frac{1}{2}\left(l_{k}^{2}-l_{k}\right)
$$

其中再次用到了 $0-1$ 矩阵中 $\varepsilon^{2}=\varepsilon$ 这一性质降次. 因此,

$$
\begin{aligned}
\sum_{k=1}^{m} \sum_{1 \leq i<j \leq n} \varepsilon_{i k} \varepsilon_{j k} & =\sum_{k=1}^{m} \frac{1}{2}\left(l_{k}^{2}-l_{k}\right) \\
& =\sum_{k=1}^{m}\left[\frac{1}{2}\left(l_{i}-k\right)\left(l_{i}-k-1\right)+k\left(l_{i}-\frac{k+1}{2}\right)\right] \\
& \geq \sum_{i=1}^{m} k\left(l_{i}-\frac{k+1}{2}\right) \\
& =k\left(\sum_{i=1}^{m} l_{i}-\frac{k+1}{2} m\right) \\
& =k m \cdot\left(\frac{\sum_{i=1}^{n}\left|S_{i}\right|}{m}-\frac{(k+1)}{2}\right) \\
& =k\left(\sigma-\frac{k}{2}\right)|S| .
\end{aligned}
$$

取 $k=N$, 上式取到最大值, 从而必然存在 $i<j$, 使得

$$
\left|S_{i} \cap S_{j}\right| \geq \frac{2}{n(n-1)} \cdot N\left(\sigma-\frac{N}{2}\right)|S|
$$

回到原题. 取 $n=5, \sigma=\frac{5 \times 500}{1000}-\frac{1}{2}=2$, 所以 $\left|S_{i} \cap S_{j}\right| \geq 200$.

构造也不难: 对 $\{1,2, \cdots, 10\}$ 的 5 个 5 元子集, $A_{1}=\{1,2,3,6,8\}, A_{2}=$ $\{1,2,5,7,10\}, A_{3}=\{1,4,5,7,9\}, A_{4}=\{2,3,4,7,9\}, A_{5}=\{3,4,5,8,10\}$, 令 $S_{i}=\bigcup_{k=0}^{99}\left(10 k+A_{i}\right)$ 即可, $i=1,2,3,4,5$.
下面再看一道经典的 IMO 试题.

例 4 (1992 年 IMO) 在空间直解坐标系中, $S$ 为有限整点集. $S_{x}$ 为 $S$ 在 $y O z$ 平面上的投影集, 证明:

$$
|S|^{2} \leq\left|S_{x}\right| \cdot\left|S_{y}\right| \cdot\left|S_{z}\right|
$$

分析与解 为了很好地刻画 $|S|$ 与 $\left|S_{x}\right|,\left|S_{y}\right|,\left|S_{z}\right|$ 的关系, 可考虑用集合元素关系表的思想解题. 本质上, $a-b$ 矩阵就是对元素与集合间的从属关系赋值. 我们对三个投影平面构造对应的三个 $0-1$ 矩阵, 进而, 这三个 $0-1$ 矩阵唯一确定了 $S$, 因为 $S$ 可看作三个投影平面经某种方式还原后的交集.

为便于理解, 笔者选择用赋值的语言书写解题过程, 但其本质与 $0-1$ 矩阵没有大的区别.

$$
\text { 令 } a_{x y}=\left\{\begin{array}{c}
1, \quad(x, y, 0) \in S_{z} \\
0, \quad(x, y, 0) \notin S_{z}
\end{array}, \text { 类似定义 } \beta_{y z} \text { 和 } \gamma_{z x}\right. \text {, 则 }
$$

故原式等同于

$$
\left(\sum_{x, y, z} a_{x y} \beta_{y z} \gamma_{z x}\right)^{2} \leq\left(\sum_{x, y} a_{x y}\right)\left(\sum_{y, z} \beta_{y z}\right)\left(\sum_{z, x} \gamma_{z x}\right)
$$

注意到 $\varepsilon^{2}=\varepsilon, \varepsilon \in\{0,1\}$ 的好性质, 由 Cauchy 不等式,

$$
\begin{aligned}
\left(\sum_{x, y, z} \alpha_{x y} \beta_{y z} \gamma_{z x}\right)^{2} & =\left(\sum_{x, y} \alpha_{x y} \sum_{z} \beta_{y z} \gamma_{z x}\right)^{2} \\
& \leq\left(\sum_{x, y} \alpha_{x y}^{2}\right)\left(\sum_{x, y}\left(\sum_{z} \beta_{y z} \gamma_{z x}\right)^{2}\right) \\
& \leq\left(\sum_{x, y}^{2}\right)\left(\sum_{x, y}\left(\sum_{z} \beta_{y z}^{2}\right)\left(\sum_{z} \gamma_{z x}^{2}\right)\right) \\
& =\left(\sum_{x, y} \alpha_{x y}\right)\left(\sum_{y}\left(\sum_{z} \beta_{y z}\right) \sum_{x}\left(\sum_{z} \gamma_{z x}\right)\right) \\
& =\left(\sum_{x, y} \alpha_{x y}\right)\left(\sum_{y, z} \beta_{y z}\right)\left(\sum_{z, x} \gamma_{z x}\right) .
\end{aligned}
$$

评注 本题的维度可以推广到任意正整数, 有兴趣的读者可以用类似的解法尝试更一般的情况. $0-1$ 矩阵很好地刻画了集合与元素的从属关系, 但它并非
万能的, 更不能僵化地套用“模板”. 实际上, 集合元素关系表, 还有不同的赋值方式, 我们举一个例子.

例 $5\left(2018\right.$ 年中国国家集训队选拔第二阶段 $\left.{ }^{[3]}\right)$ 某班有 32 名学生, 班上有 10 个兴趣小组, 每小组恰 16 人. 对任两名学生, 将他们两人恰有一人参加的兴趣小组的个数的平方称为他们的兴趣差, 设 $S$ 为所有兴趣差之和, 求 $S$ 的最小值.

我们先将题目用数学语言重新描述.

例 5 , 已知 $A_{1}, A_{2}, \cdots, A_{10} \in\{1,2, \cdots, 32\}$, 且 $\left|A_{i}\right|=16, i=1,2, \cdots, 10$.记 $D_{i}=\left\{A_{j} \mid i \in A_{j}\right\}$, 求下式

$$
\sum_{1 \leq i<j \leq 32}\left|D_{i} \Delta D_{j}\right|^{2}
$$

的最小值.

分析与解 我们先从刻画 $\left|D_{i} \Delta D_{j}\right|$ 中入手.如果使用 $0-1$ 矩阵, $\left|D_{i} \Delta D_{j}\right|$ 很难被描述清楚, 因为对 $0-1$ 矩阵中的行相乘操作仅能得到 $D_{i} \cap D_{j}$, 而相加后新的赋值有 $0,1,2$ 三种可能, 几乎不能进行进一步的推导. 再思考对称差运算的特征: 它取出恰在一个集合中的元素, 将它们与同时在两个集合中或同时不在两个集合中的元素分为两类, 这与乘法运算中的变号规则非常相似. 于是考虑引入 $1-(-1)$ 矩阵, 结合条件, 便可发现该矩阵的特征: 行和均为 0 .

注意到问题仅与 $\left|D_{i} \Delta D_{j}\right|$ 有关, 与 $D_{i}$ 中的元素性质无关, 故不妨设 $D_{i}=$ $\left\{j \mid i \in A_{j}\right\}$, 而不影响题意.

记 $n=32, m=10$, 考虑更一般的结论, 引入 $1-(-1)$ 矩阵:

$$
\left(\begin{array}{ccccc} 
& 1 & 2 & \cdots & n \\
A_{1} & \varepsilon_{11} & \varepsilon_{12} & \cdots & \varepsilon_{1 n} \\
A_{2} & \varepsilon_{21} & \varepsilon_{22} & \cdots & \varepsilon_{2 n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
A_{m} & \varepsilon_{m 1} & \varepsilon_{m 2} & \cdots & \varepsilon_{m n}
\end{array}\right)
$$

其中

$$
\varepsilon_{i j}= \begin{cases}1, & j \in A_{i} \\ -1, & j \notin A_{i}\end{cases}
$$

由条件, $\left|A_{i}\right|=\frac{n}{2}$, 我们有

$$
\sum_{j=1}^{n} \varepsilon_{i j}=\frac{n}{2} \cdot 1+\left(n-\frac{n}{2}\right) \cdot(-1)=0
$$

设两行 (对应的行向量) 的内积为 $h_{k l}$, 两列 (对应的列向量) 的内积为 $l_{i j}$, 则

$$
h_{k l}=\sum_{i=1}^{n} \varepsilon_{k i} \varepsilon_{l i}, l_{i j}=\sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j}
$$

由 $D_{i}$ 的定义, $D_{i}$ 对应的生成向量恰为第 $i$ 列, 且 $l_{i j}$ 的求和式中有 $\left|D_{i} \Delta D_{j}\right|$个 $-1, m-\left|D_{i} \Delta D_{j}\right|$ 个 1 , 从而 $l_{i j}=m-2 \cdot\left|D_{i} \Delta D_{j}\right|$, 所以

$$
\begin{aligned}
\sum_{1 \leq i<j \leq n}\left|D_{i} \Delta D_{j}\right|^{2} & =\sum_{i=1}^{n} \sum_{j=1}^{n}\left|D_{i} \Delta D_{j}\right|^{2} \\
& =\frac{1}{4} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(m-l_{i j}\right)^{2} \\
& =\frac{m^{2} n^{2}}{4}+\frac{1}{4} \sum_{i=1}^{n} \sum_{j=1}^{n} l_{i j}^{2}-\frac{m}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} l_{i j}
\end{aligned}
$$

注意到

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n} l_{i j} & =\sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j} \\
& =\sum_{k=1}^{m}\left(\sum_{i=1}^{n} \sum_{j=1}^{n} \varepsilon_{k i} \varepsilon_{k j}\right) \\
& =\sum_{k=1}^{m}\left(\sum_{i=1}^{n} \varepsilon_{k i}\right) \cdot\left(\sum_{j=1}^{n} \varepsilon_{k j}\right)=0,
\end{aligned}
$$

且

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n} l_{i j}^{2} & =\sum_{i=1}^{n} \sum_{j=1}^{n}\left(\sum_{k=1}^{m} \varepsilon_{k i} \varepsilon_{k j}\right)^{2} \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{m} \sum_{l=1}^{m} \varepsilon_{k i} \varepsilon_{k j} \varepsilon_{l i} \varepsilon_{l j} \\
& =\sum_{k=1}^{m} \sum_{l=1}^{m}\left(\sum_{i=1}^{n} \sum_{j=1}^{n} \varepsilon_{k i} \varepsilon_{l i} \varepsilon_{k j} \varepsilon_{l j}\right) \\
& =\sum_{k=1}^{m} \sum_{l=1}^{m}\left(\sum_{i=1}^{n} \varepsilon_{k i} \varepsilon_{l i}\right)^{2} \\
& =\sum_{k=1}^{m} \sum_{l=1}^{m} h_{k l}^{2} \\
& \geq \sum_{k=1}^{m} h_{k k}^{2}=m n^{2},
\end{aligned}
$$

所以

$$
\sum_{1 \leq i<j \leq n}\left|D_{i} \Delta D_{j}\right|^{2} \geq \frac{1}{4} n^{2} m(m+1)
$$

特别地将 $n=32, m=10$ 代入, 可得

$$
\sum_{1 \leq i<j \leq n}\left|D_{i} \Delta D_{j}\right|^{2} \geq 14080
$$

等号成立时我们需要 $h_{i j}=0, i \neq j$. 所以构造一个 $32 \times 32$ 的 Hadamard 矩阵,从中取 10 行 (每行不全为 +1 ) 即可.

评注 本题是集合元素关系表 $1-(-1)$ 矩阵的应用. 先用显性的代数形式表示原来的对称差个数, 之后多次算两次, 由于主体上都是恒等变形, 从而保证了放缩的适度。

本题颇有难度, 从中可以看出“集合元素关系表”解题的威力.

致谢 感谢冯跃峰老师对本文的修改提出建议和指导.

## 参考文献

[1] 孙孟越等, 2018 年北大清华金秋营试题简析 [J]. 数学新星网. 学生专栏, 2018-10-21 期.

[2] 2018 年 IMO 中国国家集训队教练组, 走向 IMO: 数学奥林匹克试题集锦 (2018) [M]. 上海华东师范大学出版社, 2018.9.

[3] 《中等数学》编辑部, 国内外数学奥林匹克试题及精解 (2012-2013) [M]. 2014.6.

