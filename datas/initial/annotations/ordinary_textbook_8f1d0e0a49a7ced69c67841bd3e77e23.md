# 数学新星网第十三期解答与点评 

## 牟晓生

第一题. 设 $n>3$ 为正奇数, 证明存在互不相等的奇数 $a, b, c$ 使得

$$
\frac{3}{n}=\frac{1}{a}+\frac{1}{b}+\frac{1}{c}
$$

(哈佛大学 牟晓生 供题)

## 解 (根据雅礼中学陈钦品同学的解答整理):

设 $n=2 k+1, k \geq 2$. 若 $k$ 为奇数, 取 $a=k, b=2 k+1, c=-k(2 k+1)$, 则

$$
\frac{1}{a}+\frac{1}{b}+\frac{1}{c}=\frac{1}{k}+\frac{1}{2 k+1}-\frac{1}{k(2 k+1)}=\frac{3}{2 k+1}=\frac{3}{n} .
$$

并且易见 $a, b, c$ 是互异的奇数 (注意 $c$ 是负的).

若 $k$ 为偶数, 取 $a=k+1, b=2 k+1, c=(k+1)(2 k+1)$. 则同样有 $\frac{1}{a}+\frac{1}{b}+\frac{1}{c}=\frac{3}{n}$, 且 $a, b, c$ 是互异奇数. 命题得证.

评注 (1). 如东高级中学张陈成同学, 长沙一中胡宇涵同学, 武汉外国语学校张睿桐同学, 湖南师大附中李颖杰, 刘奕然同学, 湖南省南雅中学戴轩宇同学,石家庄二中杨远同学以及雅礼中学团队等也给出了本题的正确解答.

(2). 本题结论可以加强为要求 $a, b, c$ 都是正的, 证明如下:

如果 $n \equiv 1(\bmod 4)$, 那么上面的证明依然有效.

下面假设 $n \equiv 3(\bmod 4)$. 如果 $n=3 m$, 则 $m \equiv 1(\bmod 4)$. 因此

$$
\frac{3}{n}-\frac{1}{m+2}=\frac{2}{m(m+2)}=\frac{m+1}{m(m+2) \frac{m+1}{2}}=\frac{1}{(m+2) \frac{m+1}{2}}+\frac{1}{m(m+2) \frac{m+1}{2}}
$$

取 $a=m+2, b=(m+2) \frac{m+1}{2}, c=m(m+2) \frac{m+1}{2}$, 命题成立.

如果 $n \equiv 1(\bmod 3)$, 令 $n=6 l+1$. 此时我们有

$$
\frac{3}{n}=\frac{3}{6 l+1}=\frac{1}{2 l+1}+\frac{1}{(2 l+1)(4 l+1)}+\frac{1}{(4 l+1)(6 l+1)}
$$

最后考虑 $n \equiv 2(\bmod 3)$. 设 $n+1=3^{r} \cdot s$, 其中 $r \geq 1$, 而 $3 \nmid s$. 先假设 $s \equiv 1$ $(\bmod 3)$, 则 $3^{r+1} \mid\left(3^{r}+1\right) n+1$. 因此存在奇数 $u$ 使得 $\left(3^{r}+1\right) n=3^{r+1} u-1$.令 $t=3^{r} u$, 那么

$$
\frac{3}{n}-\frac{1}{t n}=\frac{3 t-1}{t n}=\frac{3^{r}+1}{t}=\frac{1}{u}+\frac{1}{t} .
$$

取 $a=u, b=t, c=t n$ 即可.

假设 $s \equiv 2(\bmod 3)$, 则 $3^{r+1} \mid n+3^{r}+1$. 此时令奇数 $u$ 使得 $n+3^{r}+1=3^{r+1} u$以及 $t=3^{r} u$, 那么

$$
\frac{3}{n}-\frac{1}{t}=\frac{3 t-n}{n t}=\frac{3^{r}+1}{n t}=\frac{1}{n u}+\frac{1}{n t} .
$$

取 $a=n u, b=t, c=n t$ 即可 (注意 $n>3^{r}$, 因此 $b<a<c$ ).

(3). 上面的结论由 T. Hagedorn 发表于 2000 年的美国数学月刊. 武汉外国语学校张睿桐以及石家庄二中杨远同学通过考虑 $n+1$ 含 2 的幂 (并对它分奇偶讨论) 也得到了这个结果. 与之相关的一个问题是著名的 Erdös-Straus 猜想: 对任意的 $n>1$, 存在正整数 $a, b, c$ 使得

$$
\frac{4}{n}=\frac{1}{a}+\frac{1}{b}+\frac{1}{c}
$$

第二题. 考虑多项式 $f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}$, 如果对所有 $x \in[-1,1]$ 恒有 $|f(x)| \leq 1$, 证明

$$
\left|a_{n}\right|+\left|a_{n-1}\right| \leq 2^{n-1}
$$

(山西大学附属中学 王永喜 供题)

## 解法一 (根据供题者的解答整理):

首先不妨假设 $a_{n}, a_{n-1}$ 都是非负实数, 否则可以用 $\pm f( \pm x)$ 代替 $f(x)$.

用反证法, 假设存在 $\varepsilon>0$ 使得 $a_{n}+a_{n-1}>(1+\varepsilon) 2^{n-1}$.

令 $T_{n}(x)=\cos (n \arccos x)$ 为 $n$ 阶的 Chebyshev 多项式, 则熟知 $T_{n}(x)$ 是 $n$次首项系数为 $2^{n-1}$ 的多项式. 考虑

$$
g(x)=(1+\varepsilon) T_{n}(x)-f(x)=\left((1+\varepsilon) 2^{n-1}-a_{n}\right) x^{n}-a_{n-1} x^{n-1}-\ldots
$$

由韦达定理, $g(x)$ 所有根的和等于 $\frac{a_{n-1}}{(1+\varepsilon) 2^{n-1}-a_{n}}>1$ (注意 $a_{n} \leq 2^{n-1}$ 是熟知的结论, 因此分母是正的).

另一方面, $T_{n}\left(\cos \left(\frac{k \pi}{n}\right)\right)=\cos (k \pi)=(-1)^{k}, 0 \leq k \leq n$. 根据条件 $|f(x)| \leq$ $1, \forall|x| \leq 1$. 因此 $g\left(\cos \left(\frac{k \pi}{n}\right)\right)$ 和 $(-1)^{k}$ 同号. 由介值定理, $g(x)$ 在 $n$ 个区间 $\left(\cos \left(\frac{(k+1) \pi}{n}\right), \cos \left(\frac{k \pi}{n}\right)\right)_{0 \leq k \leq n-1}$ 上各有一个根. 而 $g(x)$ 次数为 $n$, 因此这 $n$个根就是 $g(x)$ 的全部根. 也就是说 $g(x)$ 所有根的和至多是

$$
\sum_{0 \leq k \leq n-1} \cos \left(\frac{k \pi}{n}\right)=1
$$

这与之前得到的结论矛盾, 因此命题得证!

## 解法二 (根据石家庄二中杨远同学的解答整理):

令

$$
g(x)=\sum_{0 \leq k \leq \frac{n}{2}} a_{n-2 k} x^{n-2 k}, \quad h(x)=\sum_{0 \leq k \leq \frac{n-1}{2}} a_{n-2 k-1} x^{n-2 k-1} .
$$

我们有 $f(x)=g(x)+h(x)$ 以及 $f(-x)=(-1)^{n}(g(x)-h(x))$.

考虑 $F(x)=g(x)+x h(x)$, 则在 $x \in[-1,1]$ 时有

$$
|F(x)| \leq|g(x)|+|x h(x)| \leq|g(x)|+|h(x)|=|f(x)| \text { 或者 }|f(-x)| \text {. }
$$

$|F(x)|$ 在区间 $[-1,1]$ 上不超过 1, 说明 $F(x)$ 的首项系数不超过 $2^{n-1}$. 因此 $a_{n}+a_{n-1} \leq 2^{n-1}$. 同解法一不妨假设 $a_{n}, a_{n-1} \geq 0$, 故命题得证.

评注 (1). 雅礼中学邱添同学给出此题一个不同的解法. 他的思路基于长沙一中龙博同学在本刊学生专栏 2016-01-15 期上的文章 “关于有界多项式的最高次系数的界的问题”, 利用插值公式将 $a_{n}, a_{n-1}$ 表示为 $f$在 $n+1$ 个点 $\cos \left(\frac{k \pi}{n}\right)_{0 \leq k \leq n}$ 处的值的线性和. 然后用三角形不等式直接证明 $\left|a_{n} \pm a_{n-1}\right| \leq 2^{n-1}$. 由此可得 $\left|a_{n}\right|+\left|a_{n-1}\right| \leq 2^{n-1}$.

(2). 有界多项式系数的最大值是逼近理论中一个重要的研究问题. Chebyshev 在 1854 年证明 $\left|a_{n}\right| \leq 2^{n-1}$. 之后 V.A. Markov 在 1892 年证明对所有 $k \equiv n(\bmod 2),\left|a_{k}\right|$ 的最大值在 $f=T_{n}(x)$ 时取到; 而当 $k \equiv n+1(\bmod 2)$时 $\left|a_{k}\right|$ 的最大值在 $f=T_{n-1}(x)$ 时取到. 本题的结论来源于 Szego, 他证明当 $k \equiv n(\bmod 2)$ 时 $\left|a_{k}\right|+\left|a_{k-1}\right|$ 的最大值在 $f=T_{n}(x)$ 时取到, 加强了 Markov 的结果一实际上用杨远同学的方法可知两者是等价的. 当 $k \equiv n+1(\bmod 2)$时的相应结果在 2014 年由 H.J. Rack 得到. 另外 Rack 还证明对 $n \geq 10$, $\left|a_{n}+a_{n-1}+a_{n-2}\right|$ 与 $\left|a_{n}+a_{n-1}+a_{n-2}+a_{n-3}\right|$ 的最大值都在 $f=T_{n}(x)$ 时取到.有兴趣的同学可以参考这些文献, 并思考相关的推广与未解决问题.

第三题. 考虑一个有限简单图 $G=(V, E)$, 证明 $G$ 有奇数个支配子集.

注: 称 $A \subset V$ 是 $G$ 的 “支配子集”，如果对所有 $v \in V$ ，要么 $v \in A$, 要么 $v$ 与 $A$ 中某个顶点相邻.

(湖北 边红平 供题)

## 解法一 (根据雅礼中学刘哲成同学的解答整理):

我们对顶点个数 $|V|$ 进行归纳, 归纳基础 $|V|=0,1$ 显然成立. 假设 $|V|>1$,任取 $v \in V$. 令 $S$ 为 $v$ 的领域, 而 $T=V-S-\{v\}$. 考虑 $G$ 的支配子集 $A$, 分三
种情况讨论:

(i) 如果 $v \notin A$, 令 $G^{\prime}$ 为 $G$ 在 $V-\{v\}=S \cup T$ 上的导出子图, 则 $A$ 是 $G^{\prime}$的支配子集并且 $A$ 包含 $S$ 中至少一个点. 反过来, 如果 $A$ 是 $G^{\prime}$ 的支配子集且 $A \cap S \neq \emptyset$, 则 $A$ 也是 $G$ 的支配子集. 设 $G^{\prime}$ 有 $t_{1}$ 个支配子集, 而其中 $m$ 个包含于 $T$ 中, 则这样的 $A$ 恰有 $t_{1}-m$ 个. 由归纳假设, $t_{1}$ 是奇数.

(ii) 如果 $v \in A$, 并且 $A$ 不包含 $S$ 中任意点. 令 $G^{\prime \prime}$ 为 $G$ 在 $T$ 上的导出子图,那么 $A-\{v\}$ 一定是 $G^{\prime \prime}$ 的支配子集. 这样的 $A$ 有 $t_{2}$ 个, 其中 $t_{2}$ 是奇数.

(iii) 如果 $v \in A$, 并且 $A$ 包含 $S$ 中至少一个点. 此时考虑图 $G^{\prime \prime \prime}$, 它与 $G^{\prime}$在其他地方一致, 只是 $S$ 中每两个顶点都在 $G^{\prime \prime \prime}$ 中连了边. 我们证明 $A-\{v\}$是 $G^{\prime \prime \prime}$ 的支配子集. 注意到 $A-\{v\}$ 包含 $S$ 中至少一个点, 因此它在 $G^{\prime \prime \prime}$ 支配 $S$中每个点. 另外由于 $v$ 与 $T$ 中任意点都不相邻, 而 $A$ 在 $G$ 中支配 $T$ 中每个点,因此 $A-\{v\}$ 在 $G$ 中支配 $T$ 中每个点, 从而它在 $G^{\prime \prime \prime}$ 中也支配 $T$ 中每个点. 这样我们就证明了对每个 $G$ 的支配子集 $A$, 如果 $v \in A$ 且 $A \cap S \neq \emptyset$, 则 $A-\{v\}$是 $G^{\prime \prime \prime}$ 的支配子集, 且 $A-\{v\} \cap S \neq \emptyset$. 这个结论的反面也成立, 故我们只要计算 $G^{\prime \prime \prime}$ 的支配子集中与 $S$ 相交的个数. 现在考虑 $G^{\prime \prime \prime}$ 的包含于 $T$ 的支配子集,它一定也是 $G^{\prime}$ 的包含于 $T$ 的支配子集, 反之亦然. 因此这部分的 $A$ 共有 $t_{3}-m$个, 其中 $t_{3}$ 是 $G^{\prime \prime \prime}$ 的所有支配子集总数, 是一个奇数.

综合上面的讨论, $G$ 中支配子集的总数是 $t_{1}-m+t_{2}+t_{3}-m$ 是一个奇数,归纳成立!

## 解法二 (根据雅礼中学刘恺睿同学的解答整理):

对 $u, v \in V$, 如果 $u \neq v$ 且 $u, v$ 不相邻, 则令 $f(u, v)=1$, 否则令 $f(u, v)=0$.对任意的 $A \subset V, A$ 支配顶点 $y$ 当且仅当存在 $x \in A$ 使得 $f(x, y)=0$, 也即当且仅当 $\prod_{x \in A} f(x, y)=0$. 因此 $A$ 支配任意 $y \in V$ 当且仅当

$$
\prod_{y \in V}\left(1-\prod_{x \in A} f(x, y)\right)=1
$$

而当 $A$ 不是支配子集时等号右边是零. 因此 $V$ 的所有支配子集的个数等于

$$
\begin{aligned}
& \sum_{A \subset V} \prod_{y \in V}\left(1-\prod_{x \in A} f(x, y)\right) \\
\equiv & \sum_{A \subset V} \prod_{y \in V}\left(1+\prod_{x \in A} f(x, y)\right) \quad(\bmod 2) \\
= & \sum_{A \subset V} \sum_{B \subset V} \prod_{y \in B} \prod_{x \in A} f(x, y) .
\end{aligned}
$$

由于 $f(x, y)=f(y, x)$, 我们可以将 $(A, B)$ 与 $(B, A)$ 配对求和, 因此上面的和在
模二意义下化简为

$$
\sum_{A \subset V} \prod_{x \in A} \prod_{y \in A} f(x, y)
$$

由于 $f(x, x)=0$, 当 $A$ 非空时 $\prod_{x \in A} \prod_{y \in A} f(x, y)=0$. 因此

$$
\sum_{A \subset V} \prod_{x \in A} \prod_{y \in A} f(x, y)=1
$$

为奇数, 命题得证!

评注 (1). 湖南省南雅中学戴轩宇同学, 雅礼中学段剑儒, 肖尧, 尹龙晖, 丘添等同学也给出了本题的正确解答. 他们中的一些考虑集合 $(A, B)$ 的对数, 满足 $A, B \subset V$ 不交, 且 $A$ 中任意点与 $B$ 中任意点不相邻. 这实际上就是解法二中的和 $\sum_{A \subset V} \sum_{B \subset V} \prod_{y \in B} \prod_{x \in A} f(x, y)$.

(2). 这个结论是 A.E. Brouwer 等人在 2009 年得到的, 随后出现在 2010 年美国国家队的选拔考试中. 最初看到这个问题让我想到华校课本上的一个习题,要求证明每一个完全有向图都有奇数条 Hamilton 链. 有兴趣的同学可以尝试做一下.

第四题. 给定正整数 $n, k$, 设有 $n k$ 个小球, 每个小球上写有编号 $1,2, \ldots, n$,而每种编号的球恰有 $k$ 个. 另外有 $m$ 个盒子, 每个盒子 $j$ 配有一个容量 $c_{j}$ 以及一个编号集合 $S_{j} \subset\{1,2, \ldots, n\}$. 现在我们要将所有小球放入这些盒子里, 满足以下两个条件:

(i) 每个盒子 $j$ 中至多放 $c_{j}$ 个小球;

(ii) 每个盒子 $j$ 中小球的编号都属于 $S_{j}$, 且互不相同.

证明存在这样一种放法当且仅当以下条件成立:

$$
\sum_{j=1}^{m} \min \left\{c_{j},\left|S_{j} \cap A\right|\right\} \geq k|A|, \quad \forall A \subset\{1,2, \ldots, n\}
$$

(普林斯顿大学 张瑞祥, 哈佛大学 牟晓生 供题)

## 解法一(根据供题者的解答整理):

必要性只需注意到编号在 $A$ 中的球共有 $k|A|$ 个, 而这些球在盒子 $j$ 中至多放下 $\min \left\{c_{j},\left|S_{j} \cap A\right|\right\}$ 个. 记 $[n]=\{1,2, \cdots, n\}$. 为证充分性, 我们先列一个关键的引理.

引理 假设 $(*)$ 式对所有 $A \subset[n]$ 成立. 如果 $A$ 与 $B$ 分别使得 $(*)$ 式取等号,那么 $A \cup B, A \cap B$ 也是如此.
引理的证明 对固定的 $j(1 \leq j \leq m)$, 函数 $\min \left\{c_{j}, x\right\}$ 是关于 $x$ 的凹函数.注意到 $\left|S_{j} \cap(A \cap B)\right| \leq\left|S_{j} \cap A\right|,\left|S_{j} \cap B\right| \leq\left|S_{j} \cap(A \cup B)\right|$, 而且

$$
\left|S_{j} \cap(A \cap B)\right|+\left|S_{j} \cap(A \cup B)\right|=\left|S_{j} \cap A\right|+\left|S_{j} \cap B\right| .
$$

因此由凹函数的性质我们有

$\min \left\{c_{j},\left|S_{j} \cap(A \cap B)\right|\right\}+\min \left\{c_{j},\left|S_{j} \cap(A \cup B)\right|\right\} \leq \min \left\{c_{j},\left|S_{j} \cap A\right|\right\}+\min \left\{c_{j},\left|S_{j} \cap B\right|\right\}$.

对 $j$ 求和即得

$$
\begin{aligned}
& \sum_{j} \min \left\{c_{j},\left|S_{j} \cap(A \cap B)\right|\right\}+\sum_{j} \min \left\{c_{j},\left|S_{j} \cap(A \cup B)\right|\right\} \\
\leq & \sum_{j} \min \left\{c_{j},\left|S_{j} \cap A\right|\right\}+\sum_{j} \min \left\{c_{j},\left|S_{j} \cap B\right|\right\}
\end{aligned}
$$

由于 (*) 式对 $A \cap B, A \cup B$ 成立, 上面 (2) 式的左边至少是

$$
k|A \cap B|+k|A \cup B|=k|A|+k|B| .
$$

而由假设 (*) 式对 $A, B$ 取等号, 因此 (2) 式右边恰好也等于 $k|A|+k|B|$. 故之前所有不等式均取等号, 引理得证!

回到原题. 我们对 $\sum_{j}\left(c_{j}+\left|S_{j}\right|\right)$ 归纳证明 $(*)$ 式的充分性. 我们可以假设 (*) 式对某个非空的 $A$ 取等号, 否则将某个 $c_{j}$ 减 1 不影响 (*) 式与结论. 在所有使 $(*)$ 式取等号的非空集合中, 取 $A^{*}$ 为包含关系下极小的一个(可能有多个).那么由引理, 如果 $A$ 使 $(*)$ 式取等号则 $A \cap A^{*}$ 亦然, 因而由 $A^{*}$ 的最小性可知要么 $A$ 包含 $A^{*}$, 要么 $A$ 与 $A^{*}$ 不交. 分两种情况讨论:

(i) 如果对每个 $j$ 都有 $c_{j} \geq\left|S_{j} \cap A^{*}\right|$, 那么由 $(*)$ 式知 $\sum_{j}\left|S_{j} \cap A^{*}\right|=k\left|A^{*}\right|$,而对每个 $i \in A^{*}$ 有 $\sum_{j}\left|S_{j} \cap\{i\}\right| \geq k$. 对 $i$ 求和得到这些不等式均取等号, 因此 $(*)$ 式对 $\{i\}$ 取等号, $\forall i \in A^{*}$. 由 $A^{*}$ 的最小性, $A^{*}=\{i\}$. 不妨设 $i=n$,因而 $S_{1}, S_{2}, \ldots, S_{m}$ 中恰有 $k$ 个包含元素 $n$. 自然地, 我们将 $k$ 个 $n$ 号球放到这 $k$ 个盒子里. 然后将这些盒子的容量减 1 , 而在对应的 $S_{j}$ 中去掉元素 $n$, 并用 $n-1$ 代替 $n$ 使用归纳假设即可将剩下的球放好. 容易验证在新的问题下, (*) 式对 $A \subset[n-1]$ 成立当且仅当在原有问题下 $(*)$ 式对 $A \cup\{n\}$ 成立, 因此这种情况下命题得证.

(ii) 如果存在 $j$ 使得 $c_{j}<\left|S_{j} \cap A^{*}\right|$, 此时任取 $S_{j}$ 的元素 $i$, 然后将 $S_{j}$ 变为 $S_{j}-\{i\}$. 我们验证 $(*)$ 式仍然对每个 $A$ 成立. 由于在这个变化下 $(*)$ 式的左边至多减去了 1 , 我们可以假设原来的 (*) 式恰取等号(否则变化后不等式必
然成立). 由前面的分析, 我们知道 $A \supset A^{*}$ 或者 $A \cap A^{*}=\emptyset$. 如果 $A$ 包含 $A^{*}$,则 $c_{j}<\left|S_{j} \cap A^{*}\right| \leq\left|S_{j} \cap A\right|$, 因而

$$
\min \left\{c_{j},\left|S_{j} \cap A\right|\right\}=c_{j}=\min \left\{c_{j},\left|S_{j} \cap A-\{i\}\right|\right\} .
$$

而其他的盒子对 $(*)$ 式左边的贡献没有变化, 因此 $(*)$ 式成立. 如果 $A$ 与 $A^{*}$ 不交, 那么回到引理的证明我们知道 (1) 式必须取等号 $\left(B=A^{*}\right)$. 也就是说

$$
\min \left\{c_{j},\left|S_{j} \cap\left(A \cup A^{*}\right)\right|\right\}=\min \left\{c_{j},\left|S_{j} \cap A\right|\right\}+\min \left\{c_{j},\left|S_{j} \cap A^{*}\right|\right\}
$$

利用假设 $c_{j}<\left|S_{j} \cap A^{*}\right|$ 我们得到 $\min \left\{c_{j},\left|S_{j} \cap A\right|\right\}=0$. 因此当 $S_{j}$ 变为 $S_{j}-\{i\}$时盒子 $j$ 对 (*) 式左边的贡献不变, (*) 式仍然成立. 无论如何我们都可以用归纳假设完成证明!

## 解法二 (根据雅礼中学尹龙晖的解答整理):

必要性同上易证, 这里只证充分性. 考虑一个有向图 $G$, 它的顶点集为 $s, t, a_{1}, \ldots, a_{n}, b_{1}, \ldots, b_{m}$, 其中 $a_{i}$ 表示编号为 $i$ 的球, 而 $b_{j}$ 表示第 $j$ 个盒子. $G$ 中的边有三类:

1) $s$ 向每个 $a_{i}$ 均连边, 记这些边为 $D$;
2) $a_{i}$ 向 $b_{j}$ 连边当且仅当 $i \in S_{j}$, 记这些边为 $E$;
3) 每个 $b_{j}$ 向 $t$ 连边, 记这些边为 $F$.

另外我们对每条有向边 $e$ 赋上一个 “流量” $c(e)$ : $D$ 中每条边的流量为 $k$,代表每个编号的球恰有 $k$ 个; $E$ 中每条边的流量为 1 , 代表每个盒子中所放的球编号互不相同; $F$ 中的边 $b_{j} t$ 的流量是 $c_{j}$, 代表盒子 $j$ 的容量.

图 $G$ 的一个 “流” $f$ 是定义在 $G$ 边集上的一个整值函数, 满足 $0 \leq f(e) \leq$ $c(e), \forall e$, 并且

$$
\sum_{e \text { 为 } v \text { 引出的边 }} f(e)=\sum_{e^{\prime} \text { 为指向 } v \text { 的边 }} f\left(e^{\prime}\right), \forall v \neq s, t .
$$

定义流 $f$ 的值:

$$
\operatorname{Val}(f)=\sum_{e \text { 为 } s \text { 引出的边 }} f(e) .
$$

由于 $f\left(s a_{i}\right) \leq c\left(s a_{i}\right)=k$, 我们有 $\operatorname{Val}(f) \leq k n$. 反过来, 如果 $f$ 是一个使得 $\operatorname{Val}(f)=k n$ 的流, 那么我们可以由 $f$ 得到 $k n$ 个小球的放法. 具体来说, 如果 $f\left(a_{i} b_{j}\right)=1$, 那么就将 $i$ 号球放到 $j$ 号盒子中. 由于 $\operatorname{Val}(f)=k n$, 我们知道 $f\left(s a_{i}\right)=k, \forall i$, 因此将(3)式应用到 $v=a_{i}$ 我们得到 $\sum_{j} f\left(a_{i} b_{j}\right)=k$, 也就是说 $k$ 个 $i$ 号球被放到了 $k$ 个不同的盒子里. 另一方面, 由图 $G$ 的构造知盒子 $j$ 中
所放入球的编号一定在 $S_{j}$ 中. 并且, 盒子 $j$ 中的总球数等于 $\sum_{i} f\left(a_{i} b_{j}\right)$. 由(3)式应用到 $v=b_{j}$, 这等于 $f\left(b_{j} t\right) \leq c\left(b_{j} t\right)=c_{j}$. 因此每个盒子的容量足够.

接下来我们只需证明 $G$ 存在一个值为 $k n$ 的流. 为此我们引入一个新的概念： $G$ 的一个 “割” 是其边集的一个子集 $U$, 使得从 $s$ 到 $t$ 的任意有向通路都包含 $U$ 中至少一条边. 对割集 $U$, 定义 $U$ 的流量为

$$
\operatorname{Cap}(U)=\sum_{e \in U} c(e) .
$$

根据著名的最大流最小割定理, 图 $G$ 中最大的流值等于其最小割流量. 因此为证 $G$ 存在一个值为 $k n$ 的流, 我们只需证明 $G$ 的每个割集的流量不小于 $k n$. 假设 $U$ 是 $G$ 的割集, 令 $I=\left\{i: 1 \leq i \leq n, s a_{i} \in U\right\}, J=\left\{j: 1 \leq j \leq m, b_{j} t \in U\right\}$.对任意的 $i \in[n]-I, j \in[m]-J, i \in S_{j}$, 考虑从 $s$ 到 $t$ 的通路 $s a_{i} b_{j} t$, 由 $U$ 是割集我们得到 $a_{i} b_{j} \in U$. 所以

$$
\begin{aligned}
\operatorname{Cap}(U) & \geq \sum_{i \in I} f\left(s a_{i}\right)+\sum_{j \in J} f\left(t b_{j}\right)+\sum_{j \in[m]-J, i \in[n]-I, i \in S_{j}} 1 \\
& =k|I|+\sum_{j \in J} c_{j}+\sum_{j \in[m]-J}\left|S_{j} \cap([n]-I)\right| \\
& \geq k|I|+\sum_{j} \min \left\{c_{j},\left|S_{j} \cap([n]-I)\right|\right\} \\
& \geq k|I|+k|([n]-I)| \\
& =k n .
\end{aligned}
$$

证毕!

评注 武钢三中王逸轩, 雅礼中学汤继尧, 肖尧, 刘恺睿, 邱添等同学也给出了本题正确的解答. 注意到 $k=1$ 时本题结论化归为 Hall 定理, 因此归纳法是比较自然的, 大部分解答也都类似于上面的解法一. 其中关键性的引理受到 06 IMO 预选题 C6 的启发. 而尹龙晖同学的解法二非常巧妙, 并且更容易推广. 比如可以假设不同编号的球个数不尽相同, 或者对每对 $i, j$ 要求 $j$ 号盒子中至多放 $x_{i j}$ 个 $i$ 号球. 最大流最小割定理有一个非常漂亮的算法证明, 建议有兴趣的同学学习一下.

