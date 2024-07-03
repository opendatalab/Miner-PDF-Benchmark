# 第二期 一些有代数几何背景的初等数学问题 

## 韩京俊

(约翰$\cdot$霍普金斯大学, The Johns Hopkins University)

2018 年菲尔兹奖得主 Caucher Birkar 在几年前曾提出了如下代数几何方向的猜想.

猜想 1 ([Birkar]) For a fixed positive integer $n$ and a fixed positive real number $\epsilon \in(0,1]$, is there a positive integer $M$ depending only on $n$ and $\epsilon$, such that if $X_{a}$ is $\epsilon$-lc, then $a_{1} \leq M$, where $\boldsymbol{a}=\left(a_{1}, a_{2}, \ldots, a_{n}\right), a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, $a_{1}, a_{2}, \ldots, a_{n}$ are coprime, and $X_{\mathrm{a}}$ is the weighted blow up of the affine $n$-plane $\mathbb{A}^{n}$ at the origin with the weight $\mathbf{a}=\left(a_{1}, a_{2}, \ldots, a_{n}\right)$.

利用 toric geometry 中的一些知识, 不难将猜想 1 转化为如下与格点有关的初等数学问题, 可参见中国科学院系统科学研究所的陈亦飞教授的预印本论文 [5, Lemma 3.1].

猜想 2 固定正整数 $n$ 与正实数 $\epsilon \in(0,1]$. 求证, 存在正整数 $M$ 满足如下性质: 设 $C_{n}^{\epsilon}$ 是顶点为

$$
\left\{\mathbf{0}, \epsilon \boldsymbol{e}_{1}, \ldots, \epsilon \boldsymbol{e}_{n}, \epsilon \boldsymbol{a}\right\}
$$

的凸多面体，其中 $\boldsymbol{e}_{1}=(1,0,0, \ldots, 0), \boldsymbol{e}_{2}=(0,1,0, \ldots, 0), \cdots, \boldsymbol{e}_{n}=(0,0, \ldots, 1)$, $\boldsymbol{a}=\left(a_{1}, \ldots, a_{n}\right) \in \mathbb{R}^{n}, M \leq a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 则 $C_{n}^{\epsilon}$ 的内部存在整点.

陈亦飞教授同时还证明了 $n=2,3$ 时的猜想 $2, n=2$ 时即为:

定理 3 ([5, Theorem 1.6(Main Theorem) $]$ ) 固定正实数 $\epsilon \in(0,1]$. 则存在正整数 $M$ 满足如下性质. 设 $C_{2}^{\epsilon}$ 是顶点为

$$
\left\{(0,0),(\epsilon, 0),(0, \epsilon),\left(\epsilon a_{1}, \epsilon a_{2}\right)\right\}
$$

的凸多面体, 其中 $M \leq a_{1} \leq a_{2}$, 则 $C_{2}^{\epsilon}$ 的内部存在整点.
今年 2 月, Gregory Sankaran 与 Francisco Santos 声称证明了猜想 1, [7]. 他们的方法需要用一些较为高等的数学. 一个有趣的问题是, 是否存在较为初等的方法证明猜想 2 , 从而证明 Birkar 的猜想 (猜想 1 )?

当 $n=3$ 时, Birkar 的猜想与三维的极小模型纲领 (Minimal Model Program)相关 [6, Theorem 1]. Birkar 的猜想源自 Birkar 的的博士导师、美国约翰斯霍普金斯大学 Shokurov 教授提出的 Complement 理论. Birkar 的菲尔兹奖的主要获奖工作是证明了法诺簇的有界性, 也即所谓的 “Borisov-Alexeev-Borisov 猜想”. Birkar 的证明由两篇论文组成 $[2,1]$, 而第一篇接近 120 页长文的主要结果正是 Shokurov 的 Complement 猜想的一个特例 [2, Theorem 1.1, Theorem 1.7, Theorem 1.8]. 代数几何方向的专家们认为 Complement 理论是一个有深度又比较技术化的理论, 直到最近, 人们才逐渐将这一理论应用在代数几何中,除 “Borisov-Alexeev-Borisov 猜想” 外, 还解决了一些著名的猜想与公开问题, 可参见美国普林斯顿大学的许晨阳教授及其与合作者 Harold Blum、刘雨晨的论文 $[3,8]$.

Complement 理论在一维的情形, 还有一些问题有待解决, 我们可将其转化为初等数学的语言.

问题 4 设 $n$ 是一个正整数, $\epsilon \in[0,1]$. 我们称 $\left\{b_{i}^{+}\right\}_{i \in I}$ 是 $\left\{b_{i}\right\}_{i \in I}$ 的一个

![](https://cdn.mathpix.com/cropped/2024_02_26_8b382a14bebeb981c83ag-2.jpg?height=91&width=1197&top_left_y=1508&top_left_x=298)

$$
n b_{i}^{+} \geq\left\lfloor(n+1)\left\{b_{i}\right\}\right\rfloor+n\left\lfloor b_{i}\right\rfloor .
$$

(1) 求证, 对任意正整数 $p, \epsilon \in[0,1]$, 存在正整数 $N$ 满足下面的性质：对任意 $\left\{b_{i}\right\}_{i \in I}$, 若对任意 $i \in I, b_{i} \in[0,1-\epsilon]$, 且 $\sum_{i \in I} b_{i} \leq 2$, 则存在正整数 $n \leq N$, 使得 $p \mid n$ ，且 $\left\{b_{i}\right\}_{i \in I}$ 有一个 $(n, \epsilon)$-complement.

(2) 证明或否定, 对任意正整数 $p$, 对任意 $\left\{b_{i}\right\}_{i \in I}$, 若对任意 $i \in I, b_{i} \in[0,1]$,且 $\sum_{i \in I} b_{i} \leq 2$, 则存在正整数 $n \leq N:=p\left((p+1)^{2}+2\right)$, 使得 $p \mid n$, 且 $\left\{b_{i}\right\}_{i \in I}$ 有一个 $(n, 0)$-complement.

(3) 一般的, 对固定的 $\epsilon, p$, 是否能找到最佳的 $N$ ? 特别地, $\epsilon=0$ 时, $N$ 的最佳值是否为 $p\left((p+1)^{2}+2\right)$ ?

(4) 固定正整数 $p, \epsilon \in[0,1]$. 求元素个数最少的集合 $\left\{n_{i}\right\}$, 使得对任意 $\left\{b_{i}\right\}_{i \in I}$, 若对任意 $i \in I, b_{i} \in[0,1-\epsilon]$, 且 $\sum_{i \in I} b_{i} \leq 2$, 则存在正整数 $n \in\left\{n_{i}\right\}$, 使得 $p \mid n$, 且 $\left\{b_{i}\right\}_{i \in I}$ 有一个 $(n, \epsilon)$-complement. 特别地, 当 $\epsilon=0, p=1$ 时, 集合元素的最少个数是否为 5 ? 此时对应的集合为 $\{1,2,3,4,6\}$.

Birkar 在他的博士毕业论文中, 证明了问题 4(1) 的一个弱化版本, 也即当 $p=1$ 时, 存在一个只和 $\epsilon$ 相关的正实数 $\delta<\epsilon$, 使得 $\left\{b_{i}\right\}_{i \in I}$ 有一个 $(n, \delta)-$ complement. 今年年初, 我和北京大学的陈国度博士研究了二维的 Complement 理论, 顺便我们证明了问题 4(1), [4, Theorem 1.9]. 证明基于初等数论. 问题 4(2-4)目前均是未知的, 其中问题 4(2) 中 $N$ 的值 $p\left((p+1)^{2}+2\right)$ 是美国约翰斯霍普金斯大学的何阳博士通过编程计算之后提出的.

致谢 北京大学的陈国度博士仔细阅读了本文的初稿, 在此致谢.

## 参考文献

[1] Caucher Birkar, Singularities of linear systems and boundedness of Fano varieties. arXiv: 1609.05543v1, 2016.

[2] Caucher Birkar, Anti-pluricanonical systems on Fano varieties. Annals of Mathematics, 190(2):345-463, 2019.

[3] Harold Blum, Yuchen Liu, and Chenyang Xu. Openness of K-semistability for Fano varieties. arXiv:1907.02408, 2019.

[4] Guodu Chen and Jingjun Han, Boundedness of $(\epsilon, n)$-complements for surfaces. arXiv: 2002.02246v1, 2020.

[5] Yifei Chen, On singularities of threefold weighted blowups. arXiv: 1911.04726, 2019.

[6] Masayuki Kawakita, Divisorial contractions in dimension three which contract divisors to smooth points, Invent. Math. (145)2001: 105 - 119.

[7] Gregory Sankaran, and Francisco Santos. Blowups with log canonical singularities. arXiv: 1911.06435v3, 2020.

[8] Chenyang Xu. A minimizing valuation is quasi-monomial. Annals of Mathematics, 191, 1003-1030, 2020.

