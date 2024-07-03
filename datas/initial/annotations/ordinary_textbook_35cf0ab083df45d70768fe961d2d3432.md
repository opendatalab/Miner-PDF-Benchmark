# 张瑞祥的两个问题 

冷岗松

张瑞祥是 2008 年国家队队员. 他给人的印象是: 才华横溢, 激情四射. 如果你和他讨论数学问题, 一定会被他的热情感染, 被他的广阔视野和敏捷的反应折服. 他善于变换问题, 常常带给你正面的结果和意外的惊喜.

有一次, 我见到了罗马尼亚的一道试题(RomTST, 1998, Vasile Pop 供题):设 $n$ 是素数, 整数 $a_{1}<a_{2}<\cdots<a_{n}$. 证明: $a_{1}, a_{2}, \cdots, a_{n}$ 是等差数列当且仅当存在集合 $N=\{0,1,2, \cdots\}$ 的一个分划 $A_{1}, A_{2}, \cdots, A_{n}$ 使得 $a_{1}+A_{1}=a_{2}+A_{2}=$ $\cdots=a_{n}+A_{n}$. 其中 $a_{i}+A_{i}=\left\{a_{i}+x \mid x \in A_{i}\right\}$. 我非常喜欢这个问题, 于是交给张瑞祥, 希望他提供一个新解法. 令我吃惊的是, 几天后我收到了一篇题为 “终极归纳法” 的小论文, 手写的, 字迹整齐(但不漂亮), 篇幅大概有 $7-8$ 页. 显然, 这个问题诱发了他对归纳法运用模式的新思考.

张瑞祥是一个解题高手(每位国家队队员似乎都可配得上这样的称号), 但他似乎更专注、更热衷提出问题、研究问题. 2008 年, 他赠送过我他的一个笔记本 (复印件), 笔记本中全是他创作的问题和评注. 里面有不少漂亮的问题, 当然也有一些不成熟甚至幼稚的题, 从中可感受到思考的快乐, 研究的快乐!

张瑞祥应当是研究型学习的典范. 他的经验提醒那些整天埋头 “扫题” 的奥数选手, 或许你应做一些调整: 多欣赏, 多阅读, 多回味, 多去思考问题的关键、问题之间的联系、问题的拓广等.

张瑞祥现在在世界顶尖的普林斯顿大学数学系读博士, 他的导师是著名数学家 Peter Sarnak (沃尔夫奖获得者).

这篇短文的两个问题选自张瑞祥当年的笔记本. 作为一个高中生, 能创作出这样优雅的问题, 实属不易. 让我们欣赏之.

问题 1 设 $m, n$ 是正整数, $P(x)$ 是一个首 1 的 $n$ 次复系数多项式. 证明:

$$
\sum_{k=1}^{m}|P(k)| \geq \frac{n !}{2^{n-1}}(m-n)
$$

证明这个不等式的一个自然想法是对次数用归纳法, 并辅之差分多项式方法便可. 因为差分多项式方法可降低次数 (一个 $n$ 次多项式 $f(x)$ 的差分多项式 $\Delta f(x)=f(x+1)-f(x)$ 是一个 $n-1$ 次多项式), 方便用归纳假设. 张瑞祥本人的解答便源于这个想法.

解法一 显然只要考虑 $m>n$ 的情况. 我们用归纳法证明下面更一般的结论: 设 $m, n \in N^{*}, n$ 次多项式 $f(x) \in \mathbb{C}[x], f(x)$ 的首项系数为 $a_{n}$, 则

$$
\sum_{k=1}^{m}|f(k)| \geq \frac{n !}{2^{n-1}}(m-n)\left|a_{n}\right| .
$$

当 $n=1$ 时, 记 $f(x)=a_{1} x+a_{0}$, 这时

$$
\sum_{k=1}^{m}|f(k)| \geq|f(1)|+|f(m)| \geq|f(m)-f(1)|=(m-1)\left|a_{1}\right|
$$

结论成立.

假设 (1) 式对 $n$ 成立, 现考虑 $n+1$ 的情况. 设 $f(x)$ 是一个首项为 $a_{n+1}$ 的 $n+1$ 次多项式. 记 $f$ 的差分多项式 $\Delta f(x)=f(x+1)-f(x)$, 则 $\Delta f(x)$ 是一个首项系数是 $(n+1) a_{n+1}$ 的 $n$ 次多项式. 故

$$
\begin{aligned}
\sum_{k=1}^{m}|f(k)| & \geq \frac{1}{2} \sum_{k=1}^{m-1}(|f(k)|+|f(k+1)|) \\
& \geq \frac{1}{2} \sum_{k=1}^{m-1}|f(k+1)-f(k)| \\
& =\frac{1}{2} \sum_{k=1}^{m-1}|\Delta f(k)| \\
& \geq \frac{n !}{2^{n}}(m-n-1)\left|(n+1) a_{n+1}\right| \\
& =\frac{(n+1) !}{2^{n}}(m-(n+1))\left|a_{n+1}\right|
\end{aligned}
$$

上面最后一个不等式是对 $\Delta f(x)$ 用归纳假设. 这证明了 (1) 式对 $n+1$ 成立.

下面我们考虑问题 1 的另外一种解法.

首先回忆著名的欧拉 (Euler) 恒等式 ([1]):

$$
\sum_{i=0}^{n}(-1)^{i}\left(\begin{array}{l}
n \\
i
\end{array}\right) i^{m}= \begin{cases}0, & \text { 若 } m<n ; \\
(-1)^{n} n !, & \text { 若 } m=n\end{cases}
$$

它有一个熟知的推广: 设 $f(x)$ 是 $m$ 次多项式, 首项系数为 $a_{m}$, 则

$$
\sum_{i=0}^{n}(-1)^{n-i}\left(\begin{array}{c}
n \\
i
\end{array}\right) f(x+i)= \begin{cases}0, & \text { 若 } m<n ; \\
m ! a_{m}, & \text { 若 } m=n .\end{cases}
$$

事实上, 取 $f(x)=x^{m}$, 并在上面等式 (3) 中取 $x=0$, 即得欧拉恒等式 (2).

如果我们把 $f(x+1)-f(x)$ 称为 $f(x)$ 的(一阶)差分, 并记为 $\Delta f(x) . \Delta f(x)$的差分我们记为 $\Delta^{2} f(x)$, 称为 $f(x)$ 的二阶差分. 一般可定义 $f(x)$ 的 $n$ 次差分 $\Delta^{n} f(x)=\Delta\left(\Delta^{n-1} f(x)\right)$. 通过计算不难得到 $\Delta^{n} f(x)=\sum_{k=0}^{n}(-1)^{n-k}\left(\begin{array}{l}n \\ k\end{array}\right) f(x+k)$. 利用它立得 (3).

现在我们从 (3) 出发来证明张瑞祥的不等式. 对首 1 的 $n$ 次多项式 $f(x),(3)$可写为

$$
\sum_{i=0}^{n}(-1)^{n-i}\left(\begin{array}{c}
n \\
i
\end{array}\right) f(x+i)=n !
$$

特别值得注意的是, (4) 式中的 $x$ 具有任意性, 因此 (4) 式具有某种意义上的平移不变性.

解法二 只须考虑 $m>n$ 的情况. 由 (4) 知, 对任意 $i \in\{1,2, \cdots, m-n\}$ 有

$$
\sum_{k=0}^{n}(-1)^{k}\left(\begin{array}{l}
n \\
k
\end{array}\right) P(n+i-k)=n !
$$

令 $i=1,2, \cdots, m-n$, 再将所得等式相加便得

$$
\begin{aligned}
(m-n) n ! & =\sum_{i=1}^{m-n} \sum_{k=0}^{n}(-1)^{k}\left(\begin{array}{l}
n \\
k
\end{array}\right) P(n+i-k) \\
& =\sum_{j=1-n}^{m-n}\left(\sum_{k=0}^{p}(-1)^{k}\left(\begin{array}{l}
n \\
k
\end{array}\right)\right) P(n+j),
\end{aligned}
$$

其中 $p=\min \{n, m-n-j\}$. 又

$$
\begin{aligned}
\sum_{k=0}^{p}(-1)^{k}\left(\begin{array}{l}
n \\
k
\end{array}\right) & =\sum_{k=0}^{p}(-1)^{k}\left(\left(\begin{array}{c}
n-1 \\
k
\end{array}\right)+\left(\begin{array}{l}
n-1 \\
k-1
\end{array}\right)\right) \\
& =-\sum_{k=1}^{p+1}(-1)^{k}\left(\begin{array}{l}
n-1 \\
k-1
\end{array}\right)+\sum_{k=0}^{p}(-1)^{k}\left(\begin{array}{c}
n-1 \\
k-1
\end{array}\right) \\
& =-(-1)^{p+1}\left(\begin{array}{c}
n-1 \\
p
\end{array}\right),
\end{aligned}
$$

故

$$
\left|\sum_{k=0}^{p}(-1)^{k}\left(\begin{array}{l}
n \\
k
\end{array}\right)\right|=\left(\begin{array}{c}
n-1 \\
p
\end{array}\right) \leq 2^{n-1}
$$

由 (5), (6), 我们可得

$$
\begin{aligned}
(m-n) n ! & \leq \sum_{j=1-n}^{m-n}\left|\sum_{k=0}^{p}(-1)^{k}\left(\begin{array}{l}
n \\
k
\end{array}\right)\right| \cdot|P(n+j)| \\
& \leq \sum_{j=1-n}^{m-n} 2^{n-1}|P(n+j)| \\
& =\sum_{k=1}^{m} 2^{n-1}|P(k)| .
\end{aligned}
$$

这就是所要证的结果.

注 张瑞祥在这个问题的后面加了一个注, 其中有几句话对理解这个问题或许有帮助, 抄录如下: 本题在 $m$ 很大时很弱. 韦东奕在 $m=2 n-1$ 时用步长为 2 的差分可估计到 $n !$ 级别. 另一方面, $m=n+1$ 时, 用插值公式可看出结论很强.

问题 2 对数集 $A$, 定义 $d(A)=\{|x-y| \mid x, y \in A, x \neq y\}$. 试问能否将正整数集 $N^{*}$ 分拆为有限个集合 $M_{1}, M_{2}, \cdots, M_{n}(n>1)$, 使得 $n$ 个非空集合 $d\left(M_{1}\right), d\left(M_{2}\right), \cdots, d\left(M_{n}\right)$ 两两不交?

这是张瑞祥本人比较满意的问题. 笔者也认为这是一个自然的问题: $N^{*}$ 能分拆为有限个两两不交的集合, 它们的 “距离集” 能否仍然保持两两不交呢? 这是值得探讨的. 当然, 这也是一个难度适中的问题, 相当于 CMO 第 2,5 题的水平.

这个问题的答案是否定的, 即不存在这样的分拆. 笔者个人不太喜欢 “不存在” 的答案, 因此, 觉得张瑞祥的问题 2 改写为下面的等价形式可能更好.

问题 $2^{\prime}$ 对数集 $A$, 定义 $d(A)=\{|x-y| \mid x, y \in A, x \neq y\}$. 对正整数集 $N^{*}$ 的有限分拆 $M_{1}, M_{2}, \cdots, M_{n}(n>1)$, 如果满足对任意 $1 \leq i \leq n$ 均有 $\left|M_{i}\right| \geq 2$, 则存在 $1 \leq i<j \leq n$ 使得

$$
d\left(M_{i}\right) \cap d\left(M_{j}\right) \neq \emptyset
$$

现在讨论一下问题 2 的解答.

下面的解法一属于张瑞祥自己.
解法一 答案是不能.

用反证法. 假设有 $M_{1}, M_{2}, \cdots, M_{n}$ 满足要求. 对任意 $i \in N^{*}$, 设 $i \in$ $M_{f(i)}, f(i) \in\{1,2, \cdots, n\}$.

若有无穷多个 $i \in N^{*}$ 使得 $f(i) \neq f(i+1)$, 则由于数对 $(f(i), f(i+1))$ 在 $f(i) \neq f(i+1)$ 时仅有 $n(n-1)$ 种可能. 故存在 $i<i^{\prime}, i, i^{\prime} \in N^{*}$ 使得

$$
(f(i), f(i+1))=\left(f\left(i^{\prime}\right), f\left(i^{\prime}+1\right)\right)
$$

且

$$
f(i) \neq f(i+1), f\left(i^{\prime}\right) \neq f\left(i^{\prime}+1\right) .
$$

这样就有 $i^{\prime}-i \in d\left(M_{f(i)}\right) \cap d\left(M_{f(i+1)}\right)$, 矛盾!

因此, 当 $i \in N^{*}$ 充分大时, $f(i)$ 均等于 $f(i+1)$, 即当 $i$ 充分大时, $f(i)$ 为某一固定值. 不妨设存在正整数 $N$ 使对任何 $i>N$ 均有 $i \in M_{1}$, 则任取 $d\left(M_{2}\right)$ 的一个元 $r$, 有

$$
r=|(N+1)-(N+r+1)| \in d\left(M_{1}\right),
$$

矛盾!

这个证明是漂亮的, 但技巧性稍强, 下面的解法更直白一些.

解法二 答案是不能.

用反证法, 假设 $N^{*}$ 能分拆成 $n$ 个集合 $M_{1}, M_{2}, \cdots, M_{n}(n>1)$ 满足要求. 因 $N^{*}$ 是无限集, 故 $M_{i}$ 中必存在一个为无限集. 不妨设 $M_{1}$ 为无限集.

现在在 $M_{1}$ 中取 $n$ 个不同的元 $a_{1}, a_{2}, \cdots, a_{n}$. 由于 $d\left(M_{2}\right)$ 非空, 设 $x \in d\left(M_{2}\right)$,则

$$
a_{1}+x, a_{2}+x, \cdots, a_{n}+x \notin M_{1}
$$

否则, 设 $a_{i}+x \in M$, 则 $\left(a_{i}+x\right)-a_{i}=x \in d\left(M_{1}\right)$, 这与 $d\left(M_{1}\right) \cap d\left(M_{2}\right)=\emptyset$ 矛盾!

这样 $a_{1}+x, a_{2}, \cdots, a_{n}+x$ 属于 $M_{2}, \cdots, M_{n}$ 这 $n-1$ 个集合中, 由抽庹原理知存在 $1 \leq i<j \leq n$ 使得 $a_{i}+k$ 和 $a_{j}+k$ 属于同一个 $M_{k}(2 \leq k \leq n)$ 中.

故

$$
\left|a_{j}-a_{i}\right|=\left|\left(a_{j}+x\right)-\left(a_{i}+x\right)\right| \in d\left(M_{k}\right) .
$$

又 $\left|a_{j}-a_{i}\right| \in d\left(M_{1}\right)$, 故 $d\left(M_{k}\right) \cap d\left(M_{1}\right) \neq \emptyset$. 矛盾!

关于问题 2,一个自然的问题是: 如果将正整数集 $N^{*}$ 分划为无限多个集合,又有什么结果呢? 人大附中的李秋生老师探讨了这个问题并得到下面美妙的结
果:

问题 3 对于数集 $A$, 定义 $d(A)=\{|x-y| \mid x, y \in A, x \neq y\}$. 问能否将正整数 $N^{*}$ 分拆为无限多个集合 $M_{1}, M_{2}, \cdots, M_{n}, \cdots$, 使得每个集合都有无限多个元素,且 $d\left(M_{1}\right), d\left(M_{2}\right), \cdots, d\left(M_{n}\right), \cdots$ 两两不交?

下面的解答也属于李秋生.

解 答案是肯定的.

记 $(k, i)$ 为集合 $M_{k}$ 的第 $i$ 个元素 (从小到大排列), 我们将所有集合的所有元素按如下顺序编号:

$$
(1,1) \rightarrow(1,2) \rightarrow(2,1) \rightarrow(1,3) \rightarrow(2,2) \rightarrow(3,1) \rightarrow(1,4) \rightarrow \cdots
$$

这就给出了一个从 $N^{*}$ 到 $\left\{(x, y) \mid x \in N^{*}, y \in N^{*}\right\}$ 的一一映射, 记为 $f$. 其中 $f(1)=(1,1), f(2)=(1,2), f(3)=(2,1), \cdots$, 依此类推.

下面给出具体的构造(只需同时兼顾遍历所有的位置和遍历所有的正整数):

i) 第 1 步: 将数字 1 放在第一个集合 $M_{1}$ 的第一个位置, 即 $(1,1)$;

ii) 假设在前 $k-1(k \geq 2)$ 步中, 位置 $f(1), f(2), \cdots, f(k-1)$ 上都已放置了正整数, 且 $1, \cdots, k-1$ 也都已放在某些恰当位置上(未必都在位置 $f(1), f(2), \cdots, f(k-1)$ 上). 则在第 $k$ 步中, 我们将把正整数 $k$ 放在某个恰当的位置, 并在位置 $f(k)$ 上放置一个恰当的数:

首先, 考察位置 $f(k)$. 如果已有正整数被放在这个位置上, 则接下来考察正整数 $k$; 如果还没有正整数被放在这个位置上, 则在这个位置上放置一个充分大的正整数, 使得它与这个集合中已有数的差都大于各个集合已有的差.

其次, 考察正整数 $k$. 如果它已经被放置在某个位置上, 则第 $k$ 步完成; 如果 $k$ 还没有被放置过, 则将它放在还没有任何元素的脚标最小的那个集合中.

由此可见, 在第 $k$ 步中, 我们没有放入重复的正整数, 也没有放置重复的位置.

按此方法, 正整数 $k$ 将在前 $k$ 步中被放入某个集合, 所以得到的是正整数集合 $N^{*}$ 的一个分拆; 位置 $f(k)$ 也在前 $k$ 步中被放入了某个正整数, 所以有无穷多个集合, 每个集合有无穷多个元素.

由上述构造知, $d\left(M_{1}\right), d\left(M_{2}\right), \cdots, d\left(M_{n}\right), \cdots$ 都是两两不交的.

## 参考文献

[1] 余红兵, 奥数教程(高三年级) $[M]$, 第四版, 华东师大出版社, 2008.

