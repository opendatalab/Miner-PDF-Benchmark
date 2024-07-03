# 一道 HMMT 组合试题的证明 

冷岗松 施柯杰

设 $S_{n}=\{1,2, \cdots, n\}$, 则 $S_{n}$ 的一个排列 $\sigma$ 是 $S_{n} \rightarrow S_{n}$ 的一个一一映射. 对于这样的一个排列 $\sigma$, 若存在 $k \in\{1,2, \cdots, n\}$ 使得 $\sigma(k)=k$, 则称 $k$ 是 $\sigma$ 的一个不动点. 若 $\sigma$ 的不动点个数恰为 $r$ 个, 即 $|\{i: \sigma(i)=i, 1 \leq i \leq n\}|=r(0 \leq$ $r \leq n)$, 则称此排列 $\sigma$ 为 $S_{n}$ 的一个 $r$ 保位排列.

一个自然的问题是：在 $S_{n}$ 的所有排列中， $r$ 保位排列的个数是多少? 事实上, 设 $S_{n}$ 的所有 $r$ 保位排列的个数记为 $E_{r}(0 \leq r \leq n)$, 则下面的公式是著名的:

$$
E_{r}=\frac{n !}{r !} \sum_{k=1}^{n-1} \frac{(-1)^{k}}{k !}
$$

当 $r=0$ 时, (*) 式就是熟知的错位排列公式, 这是上世纪 80 年代组合学习中的经典题目.

同学们, 你们能给出 $(*)$ 式的证明吗? 给一个 Hint: 用容斥原理.

关于 $\sigma$ 的不动点的另一自然的问题是求 $S_{n}$ 的所有不动点个数的总量. 这类问题中一个有趣且难度不太高的问题是计算

$$
\sum_{\sigma} f(\sigma)^{k}, \quad k \in \mathbb{N}^{*}
$$

其中 $f(\sigma)$ 表示排列 $\sigma$ 的不动点个数, 求和号跑遍 $S_{n}$ 的所有排列.

2013 年, 哈佛一麻省理工数学竞赛 (简称 HMMT) 中有这样一道试题:

问题. 给定 $1,2, \cdots, 2013$ 的一个排列 $\sigma$, 记 $f(\sigma)$ 表示 $\sigma$ 的不动点的个数,试求

$$
\sum_{\sigma \in S} f(\sigma)^{4}
$$

其中 $S$ 为 $1,2, \cdots, 2013$ 的所有排列的集合.

下面介绍 2015 年三位国家队队员贺嘉帆、谢昌志、高继扬的解法.

## 解法一 (根据贺嘉帆解答整理)

记 $n=2013$, 令

$$
a_{\sigma_{j}}=\left\{\begin{array}{ll}
1, & \text { 当 } \sigma(j)=j \\
0, & \text { 当 } \sigma(j) \neq j
\end{array},\right.
$$

则 $a_{\sigma_{j}}^{2}=a_{\sigma_{j}}, f(\sigma)=\sum_{i=1}^{n} a_{\sigma_{i}}$. 故

$$
\begin{aligned}
\sum_{\sigma \in S} f(\sigma)^{4}= & \sum_{\sigma \in S}\left(\sum_{i=1}^{n} a_{\sigma_{i}}\right)^{4} \\
= & \sum_{\sigma \in S}\left(\sum_{i=1}^{n} a_{\sigma_{i}}^{4}+\sum_{1 \leq i<j \leq n}\left(4 a_{\sigma_{i}}^{3} a_{\sigma_{j}}+6 a_{\sigma_{i}}^{2} a_{\sigma_{j}}^{2}+4 a_{\sigma_{i}} a_{\sigma_{j}}^{3}\right)\right. \\
& +12 \sum_{1 \leq i<j<k \leq n}\left(a_{\sigma_{i}}^{2} a_{\sigma_{j}} a_{\sigma_{k}}+a_{\sigma_{i}} a_{\sigma_{j}}^{2} a_{\sigma_{k}}+a_{\sigma_{i}} a_{\sigma_{j}} a_{\sigma_{k}}^{2}\right) \\
& \left.+24 \sum_{1 \leq i<j<k<l \leq n} a_{\sigma_{i}} a_{\sigma_{j}} a_{\sigma_{k}} a_{\sigma_{l}}\right) \\
= & \sum_{\sigma \in S}\left(\sum_{i=1}^{n} a_{\sigma_{i}}+14 \sum_{1 \leq i<j \leq n} a_{\sigma_{i}} a_{\sigma_{j}}+36 \sum_{1 \leq i<j<k \leq n} a_{\sigma_{i}} a_{\sigma_{j}} a_{\sigma_{k}}\right. \\
& \left.+24 \sum_{1 \leq i<j<k<l \leq n} a_{\sigma_{i}} a_{\sigma_{j}} a_{\sigma_{k}} a_{\sigma_{l}}\right) .
\end{aligned}
$$

注意到对任一个 $i \in\{1,2, \cdots, n\}$, 存在 2012 ! 个 $\sigma$ 使得 $\sigma(i)=i$, 因此

$$
\sum_{\sigma \in S}\left(\sum_{i=1}^{n} a_{\sigma_{i}}\right)=\sum_{i=1}^{n} \sum_{\sigma \in S} a_{\sigma_{i}}=\sum_{i=1}^{n} 2012 !=n \cdot 2012 !=2013 !
$$

又对任一对 $1 \leq i<j \leq n$, 存在 2011! 个 $\sigma$ 使得 $\sigma(i)=i, \sigma(j)=j$, 故

$$
\sum_{\sigma \in S}\left(\sum_{1 \leq i<j \leq n} a_{\sigma_{i}} a_{\sigma_{j}}\right)=\sum_{1 \leq i<j \leq n} \sum_{\sigma \in S} a_{\sigma_{i}} a_{\sigma_{j}}=\sum_{1 \leq i<j \leq n} 2011 !=2011 ! \cdot \mathrm{C}_{2013}^{2} .
$$

同理,

$$
\begin{gathered}
\sum_{\sigma \in S}\left(\sum_{1 \leq i<j<k \leq n} a_{\sigma_{i}} a_{\sigma_{j}} a_{\sigma_{k}}\right)=2010 ! \cdot \mathrm{C}_{2013}^{3} \cdot \\
\sum_{\sigma \in S}\left(\sum_{1 \leq i<j<k<l \leq n} a_{\sigma_{i}} a_{\sigma_{j}} a_{\sigma_{k}} a_{\sigma_{l}}\right)=2009 ! \cdot \mathrm{C}_{2013}^{4} \cdot
\end{gathered}
$$

将 (2),(3),(4) 和 (5) 代入 (1) 右边, 便得

$$
\begin{aligned}
\sum_{\sigma \in S} f(\sigma)^{4} & =2013 !+14 \cdot \mathrm{C}_{2013}^{2} \times 2011 !+36 \cdot \mathrm{C}_{2013}^{3} \times 2010 !+24 \cdot \mathrm{C}_{2013}^{4} \times 2009 ! \\
& =15 \cdot 2013 !
\end{aligned}
$$

因此所求 $\sum_{\sigma \in S} f(\sigma)^{4}=15 \cdot 2013$ !.

贺嘉帆的解法利用不动点的特征函数, 将所要求的计数问题转化为特征函数的运算, 拙中藏巧, 颇具 “通法” 意味.

## 解法二 (根据谢昌志解答整理)

令 $n=2013$, 先证下面的引理.

引理。

$$
\sum_{\sigma \in S} \mathrm{C}_{f(\sigma)}^{k}=(n-k) ! \cdot \mathrm{C}_{n}^{k}, \quad k=1,2,3,4
$$

事实上, 只需对 $k=4$ 证明上式成立便可, $k=1,2,3$ 的情况类似.

记 $S$ 中同时以 $a, b, c, d(a<b<c<d)$ 为不动点的排列个数为 $g(a, b, c, d)=$ $(n-4)$ !, 则

$$
\sum_{1 \leq a<b<c<d \leq n} g(a, b, c, d)=(n-4) ! \cdot \mathrm{C}_{n}^{4} \text {. }
$$

考虑上式中每个排列 $\sigma$ 的贡献. 由于每个有 $m$ 个不动点的排列可产生 $\mathrm{C}_{m}^{4}$个四元不动点组, 故每个排列 $\sigma$ 在 (7) 式中的贡献为 $\mathrm{C}_{f(\sigma)}^{4}$, 故

$$
\sum_{1 \leq a<b<c<d \leq n} g(a, b, c, d)=\sum_{\sigma \in S} \mathrm{C}_{f(\sigma)}^{4}
$$

由 (7),(8) 便知 (6) 对 $k=4$ 成立, 引理得证.

回到原题. 注意到恒等式

$$
m^{4}=24 \mathrm{C}_{m}^{4}+36 \mathrm{C}_{m}^{3}+14 \mathrm{C}_{m}^{2}+m, \quad m \in \mathbb{N}^{*}
$$

则由引理知

$$
\begin{aligned}
\sum_{\sigma \in S} f(\sigma)^{4} & =24 \sum_{\sigma \in S} \mathrm{C}_{f(\sigma)}^{4}+36 \sum_{\sigma \in S} \mathrm{C}_{f(\sigma)}^{3}+14 \sum_{\sigma \in S} \mathrm{C}_{f(\sigma)}^{2}+\sum_{\sigma \in S} f(\sigma) \\
& =24(n-4) ! \mathrm{C}_{n}^{4}+36(n-3) ! \mathrm{C}_{n}^{3}+14(n-2) ! \mathrm{C}_{n}^{2}+(n-1) ! \mathrm{C}_{n}^{1} \\
& =15 n !=15 \cdot 2013 !
\end{aligned}
$$

因此所求 $\sum_{\sigma \in S} f(\sigma)^{4}=15 \cdot 2013$ !.

谢昌志的解法中的引理本质上等价于贺嘉帆解法中的 (2),(3),(4),(5), 或许由于左边写法的特点, 使他想到了一个恒等式 (9), 从而快速得到了问题的结果.恒等式 (9) 是下面一般形式的组合恒等式的特列 (见 $[1, P 16]$ ):

$$
m^{n}=\sum_{r=0}^{m} \mathrm{C}_{m}^{r} \sum_{t_{1}+t_{2}+\cdots+t_{r}=n, t_{i} \geq 1} \frac{n !}{t_{1} ! t_{2} ! \cdots t_{r} !}
$$

## 解法三 (根据高继扬解答整理)

考虑 5 元有序对 $(\sigma, a, b, c, d)$ 的个数 $T$, 其中 $\sigma \in S, a, b, c, d \in\{1,2, \cdots, 2013\}$,且 $\sigma(a)=a, \sigma(b)=b, \sigma(c)=c, \sigma(d)=d$.

一方面, 对固定的 $\sigma$, 由乘法原理知, 这样的五元有序对的个数为 $f(\sigma)^{4}$, 故

$$
T=\sum_{\sigma \in S} f(\sigma)^{4}
$$

另一方面, 先对 $(a, b, c, d)$ 计数来计算 $T$, 分下面四种情况:

(i) 当 $a=b=c=d$ 时, 此时四元数组 $(a, b, c, d)$ 的选择有 2013 个, 其排列有 1 个, 而 $\sigma$ 的选取有 $(2013-1) !=2012$ ! 个, 则此时满足条件的五元有序对共有 $T_{1}=2013 \times 2012 !=2013$ ! 个.

(ii) 当 $a, b, c, d$ 中有两个不同的数, 此时四元数组 $(a, b, c, d)$ 的选择有 $\mathrm{C}_{2013}^{2}$个, 其排列有 $2 \times \mathrm{C}_{4}^{1}+\mathrm{C}_{4}^{2}=14$ 个, 而 $\sigma$ 有 $(2013-2) !=2011$ ! 个. 故此时满足条件的五元有序对的个数 $T_{2}=\mathrm{C}_{2013}^{2} \times 14 \times 2011 !=7 \times 2013$ !.

(iii) 当 $a, b, c, d$ 中有三个不同的数, 此时四元数组 $(a, b, c, d)$ 有 $\mathrm{C}_{2013}^{3}$ 个, 其排列有 $3 \times 4 \times 3=36$ 个, 而 $\sigma$ 有 $(2013-3) !=2010 !$ 个. 故此时满足条件的五元有序对的个数 $T_{3}=\mathrm{C}_{2013}^{3} \times 36 \times 2010 !=6 \times 2013$ !.

(iv) 当 $a, b, c, d$ 两两不同时, 此时四元数组 $(a, b, c, d)$ 有 $\mathrm{C}_{2013}^{4}$ 个, 其排列有 $4 !=24$ 个, 而 $\sigma$ 有 $(2013-4) !=2009 !$ 个. 故此时满足条件的五元有序对的个数 $T_{4}=\mathrm{C}_{2013}^{4} \times 4 ! \times 2009 !=2013$ !

综上, $T=T_{1}+T_{2}+T_{3}+T_{4}=15 \times 2013 !$.

高继扬的解法非常质朴, 特别简明. 其中一个关键是将问题转化为五元有序对的计数问题, 将置换 $\sigma$ 也看作一个元, 这是一种高观点, 有应用群 $S \otimes S_{n}$的思想

## 参考文献

[1] 叶思源编译. 俄罗斯组合分析问题集 [M]. 哈尔滨工业大学出版社, 2011.

