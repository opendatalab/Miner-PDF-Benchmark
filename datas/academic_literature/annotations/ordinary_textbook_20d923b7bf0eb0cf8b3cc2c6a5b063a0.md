数学新星网 当学生专栏

www.nsmath.cn/xszl

2022 年全国中学生数学奥林匹克竞赛试题解析

孙启傲

(上海市上海中学, 200231)

指导老师：王广廷

2022 年全国中学生数学奥林匹克竞赛 (决赛) 暨第 38 届全国中学生数学冬令营于 2022 年 12 月 29 、 30 日两天举行, 本次比赛分省线下举行. 这次比赛题目新颖、难度适中，充分考察了参赛选手的各方面能力. 本文尽可能还原作者在考场上的做法，可能并不是最优的解答，如有不当之处，敬请指正.

# I. 试题 

1. 设正实数序列 $\left\{a_{n}\right\},\left\{b_{n}\right\}$ 满足：对任意正整数 $n$ ，均有

$$
a_{n+1}=a_{n}-\frac{1}{1+\sum_{i=1}^{n} \frac{1}{a_{i}}}, b_{n+1}=b_{n}+\frac{1}{1+\sum_{i=1}^{n} \frac{1}{b_{i}}} .
$$

(1) 若 $a_{100} b_{100}=a_{101} b_{101}$, 求 $a_{1}-b_{1}$ 的值;

(2) 若 $a_{100}=b_{99}$, 比较 $a_{100}+b_{100}$ 与 $a_{101}+b_{101}$ 的大小.

2. 给定一个边长为 1 的正三角形 $A B C$, 称 $(\triangle D E F, \triangle X Y Z)$ 是一个好三角形对, 如果点 $D, E, F$ 分别在线段 $B C, C A, A B$ 内部, 点 $X, Y, Z$ 分别在直线 $B C, C A, A B$ 上, 满足

$$
\frac{D E}{20}=\frac{E F}{22}=\frac{F D}{38}
$$

且

$$
X Y \perp D E, Y Z \perp E F, Z X \perp F D \text {. }
$$

当 $(\triangle D E F, \triangle X Y Z)$ 取遍所有好三角形对时, 求 $\frac{1}{S_{\triangle D E F}}+\frac{1}{S_{\triangle X Y Z}}$ 的所有可能值.

3. 给定正整数 $m$ 和 $n$. 将正 $2 m+2 n$ 边形的 $2 m$ 个顶点染黑色, 其余 $2 n$个顶点染白色. 定义两个黑点 $B, C$ 的染色距离 $d(B, C)$ 为直线 $B C$ 两侧的白点数目的较小者; 定义两个白点 $W, X$ 的染色距离 $d(W, X)$ 为直线 $W X$ 两侧
的黑点数目的较小者.

一个黑点配对方案 $\mathcal{B}$ 是指将所有 $2 m$ 个黑点标记为 $B_{1}, \cdots, B_{m}, C_{1}, \cdots$, $C_{m}$, 使得 $m$ 条线段 $B_{i} C_{i}(1 \leq i \leq m)$ 两两不相交. 对任一黑点配对方案 $\mathcal{B}$, 记

$$
\mathcal{P}(\mathcal{B})=\sum_{i=1}^{m} d\left(B_{i}, C_{i}\right)
$$

一个白点配对方案 $\mathcal{W}$ 是指将所有 $2 n$ 个白点标记为 $W_{1}, \cdots, W_{m}, X_{1}, \cdots$, $X_{m}$, 使得 $n$ 条线段 $W_{i} X_{i}(1 \leq i \leq n)$ 两两不相交. 对任一白点配对方案 $\mathcal{W}$, 记

$$
\mathcal{P}(\mathcal{W})=\sum_{i=1}^{n} d\left(W_{i}, X_{i}\right)
$$

求证：无论顶点的染色方式如何，均有

$$
\max _{\mathcal{B}} \mathcal{P}(\mathcal{B})=\max _{\mathcal{W}} \mathcal{P}(\mathcal{W})
$$

其中等式两边的最大值分别在所有可能的黑点配对方案 $\mathcal{B}$ 和白点配对方案 $\mathcal{W}$中选取.

4. 求最小的整数 $n \geq 3$, 满足: 平面上存在 $n$ 个点 $A_{1}, A_{2}, \cdots, A_{n}$, 其中任意三点不共线, 且对任意 $1 \leq i \leq n$, 存在 $1 \leq j \leq n(j \neq i)$, 使得线段 $A_{j} A_{j+1}$经过线段 $A_{i} A_{i+1}$ 的中点, 这里 $A_{n+1}=A_{1}$.
5. 证明存在正数 $C$, 使得如下结论成立:

对任意一个无穷多项的正整数等差数列 $a_{1}, a_{2}, a_{3}, \cdots$, 若 $a_{1}$ 和 $a_{2}$ 的最大公约数无平方因子, 则存在正整数 $m \leq C a_{2}^{2}$, 使得 $a_{m}$ 无平方因子.

注：称正整数 $N$ 无平方因子，若它不被任何大于 1 的平方数整除.

6. 有 $n(n \geq 8)$ 座机场, 某些机场之间有单向直达航线. 对任意两座机场 $a, b$, 从 $a$ 飞往 $b$ 的单向直达航线至多一条 (可能同时有从 $a$ 飞往 $b$ 的和从 $b$ 飞往 $a$ 的单向直达航线). 已知对任意由若干座机场构成的集合 $A(1 \leq|A| \leq n-1)$,都有至少 $4 \min \{|A|, n-|A|\}$ 条单向直达航线从 $A$ 中的机场飞往 $A$ 之外的机场.

求证：对任意一座机场 $x$, 都可以从 $x$ 出发, 经过不超过 $\sqrt{2 n}$ 条单向直达航线回到机场 $x$.

## II. 解答

1. 设正实数序列 $\left\{a_{n}\right\},\left\{b_{n}\right\}$ 满足：对任意正整数 $n$, 均有

$$
a_{n+1}=a_{n}-\frac{1}{1+\sum_{i=1}^{n} \frac{1}{a_{i}}}, b_{n+1}=b_{n}+\frac{1}{1+\sum_{i=1}^{n} \frac{1}{b_{i}}} .
$$

(1) 若 $a_{100} b_{100}=a_{101} b_{101}$, 求 $a_{1}-b_{1}$ 的值;

(2) 若 $a_{100}=b_{99}$, 比较 $a_{100}+b_{100}$ 与 $a_{101}+b_{101}$ 的大小.

证明：记 $a_{1}=a, b_{1}=b . a, b>0$. 下面对 $n$ 归纳证明：

$$
a_{n}=\frac{a^{n}}{(a+1)^{n-1}}, b_{n}=\frac{b(b+2) \cdots(b+2 n-2)}{(b+1)(b+3) \cdots(b+2 n-3)} .
$$

$n=1$ 时成立. 假设结论对小于等于 $n$ 时成立, 考虑 $n+1$ 时情形.

由归纳假设：

$$
a_{n+1}=a_{n}-\frac{1}{1+\sum_{i=1}^{n} \frac{1}{a_{i}}}=\frac{a^{n}}{(a+1)^{n-1}}-\frac{1}{\sum_{i=1}^{n} \frac{(a+1)^{i-1}}{a^{n}}}
$$

其中

$$
\sum_{i=1}^{n} \frac{(a+1)^{i-1}}{a^{n}}=\frac{1}{a} \frac{\frac{(a+1)^{n}}{a^{n}}-1}{\frac{1}{a}}=\frac{(a+1)^{n}}{a^{n}}-1
$$

于是

$$
a_{n+1}=\frac{a^{n}}{(a+1)^{n-1}}-\frac{a^{n}}{(a+1)^{n}}=\frac{a^{n+1}}{(a+1)^{n}} .
$$

成立!

由条件，

$$
\begin{aligned}
& \frac{1}{b_{n+1}-b_{n}}=1+\sum_{i=1}^{n} \frac{1}{b_{i}} \\
& \frac{1}{b_{n}-b_{n-1}}=1+\sum_{i=1}^{n-1} \frac{1}{b_{i}} .
\end{aligned}
$$

所以 (结合归纳假设)

$$
\frac{1}{b_{n+1}-b_{n}}=\frac{1}{b_{n}-b_{n-1}}+\frac{1}{b_{n}}=\frac{1}{\left(1-\frac{b+2 n-3}{b+2 n-2}\right) b_{n}}+\frac{1}{b_{n}}=\frac{b+2 n-1}{b_{n}} .
$$

有

$$
b_{n+1}=\frac{b+2 n}{b+2 n-1} b_{n}=\frac{b(b+2) \cdots(b+2 n)}{(b+1)(b+3) \cdots(b+2 n-1)}
$$

成立！于是证明了

$$
a_{n}=\frac{a^{n}}{(a+1)^{n-1}}, b_{n}=\frac{b(b+2) \cdots(b+2 n-2)}{(b+1)(b+3) \cdots(b+2 n-3)} .
$$

(1): $a_{100} b_{100}=a_{101} b_{101} \Rightarrow \frac{b+199}{b+200}=\frac{a}{a+1} \Rightarrow a_{1}-b_{1}=199$.

(2): 由条件, $a_{1}>a_{2}>\cdots>a_{100}=b_{99}>b_{98}>\cdots>b_{1}$.

得

$$
a_{100}+b_{100}-a_{99}-b_{99}=\frac{1}{\sum_{i=1}^{99} \frac{1}{b_{i}}}-\frac{1}{\sum_{i=1}^{99} \frac{1}{a_{i}}} .
$$

注意 $b_{i}<a_{i}$, 对任何 $1 \leq i \leq 99$ 成立. 故 $a_{100}+b_{100}-a_{99}-b_{99}<0$. 于是

$$
b_{100}<a_{99} \Rightarrow \sum_{i=1}^{100} \frac{1}{b_{i}}>\sum_{i=1}^{100} \frac{1}{a_{i}}
$$

所以

$$
a_{101}+b_{101}-a_{100}-b_{100}=\frac{1}{\sum_{i=1}^{100} \frac{1}{b_{i}}}-\frac{1}{\sum_{i=1}^{100} \frac{1}{a_{i}}}<0
$$

即 $a_{100}+b_{100}>a_{101}+b_{101}$.

评注: 本题是一道较为简单的数列题. 关键在于在考场上快速地发现 $\left\{a_{n}\right\}$, $\left\{b_{n}\right\}$ 的通项公式. 第二问这里给出的做法较难想到, 需要结合递推公式巧妙估计. 考场上也有不少同学直接使用通项公式放不等式解决第二问. 对于这样的解答有一个易错点：即在证明

$$
a+1<\frac{(b+197)(b+199)}{b+198}
$$

时，尝试去证明 $a<b+196$ 这一更强结果. 不过事实上，这在 $b$ 趋于无穷大的时候是不正确的. 这也说明某种意义上该不等式是较紧的, 也足以看出利用递推公式的妙处.

2. 给定一个边长为 1 的正三角形 $A B C$, 称 $(\triangle D E F, \triangle X Y Z)$ 是一个好三角形对, 如果点 $D, E, F$ 分别在线段 $B C, C A, A B$ 内部, 点 $X, Y, Z$ 分别在直线 $B C, C A, A B$ 上, 满足

$$
\frac{D E}{20}=\frac{E F}{22}=\frac{F D}{38}
$$

且

$$
X Y \perp D E, Y Z \perp E F, Z X \perp F D \text {. }
$$

当 $(\triangle D E F, \triangle X Y Z)$ 取遍所有好三角形对时, 求 $\frac{1}{S_{\triangle D E F}}+\frac{1}{S_{\triangle X Y Z}}$ 的所有可能值.

解：作出 $D, E, F$ 关于 $\triangle A B C$ 的 Miquel 点 $M$.

由条件, $\triangle X Y Z$ 与 $\triangle A B C$ 相似, 且是顺相似. 这说明 $X, Y, Z$ 关于 $\triangle A B C$的 Miquel 点也为 $M$. (该结论熟知，具体可参考《近代欧式几何学》第七章)由正弦定理：

$$
\frac{A M}{\sin \angle A F M}=\frac{E F}{\sin 60^{\circ}}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_731f1bd5cedeefb97053g-05.jpg?height=634&width=734&top_left_y=234&top_left_x=658)

以及对称的两个式子. 并结合 $\angle A F M=\angle B D M=\angle A E M$, 说明

$$
A M: B M: C M=22: 38: 20 \text {. }
$$

由于 $\triangle X Y Z$ 与 $\triangle A B C$ 对边垂直, 故两三角形旋转相似的旋转角为 $90^{\circ}$.故 $D M \perp X M$ 等.

作正三角形 $A M N$ 使得 $\triangle A B M \cong \triangle A C N$.

则有

$$
\begin{aligned}
\angle M N C & =\angle A N C-60^{\circ}=\angle A M B-60^{\circ} \\
& =\angle M B C-\angle M A C=\angle M F D-\angle M F E \\
& =\angle E F D \\
\angle N C M & =\angle N C A-\angle A C M=\angle M B A-\angle A C M \\
& =\angle M D F-\angle M D E=\angle E D F
\end{aligned}
$$

故 $\triangle M N C$ 与 $\triangle E F D$ 相似且是逆相似. 由于 $D, E, F$ 在三边内部, $C N$ 是绕 $N$ 顺时针旋转一个小于 $180^{\circ}$ 的角到达 $N M$.

![](https://cdn.mathpix.com/cropped/2024_02_26_731f1bd5cedeefb97053g-05.jpg?height=582&width=706&top_left_y=2042&top_left_x=675)
设 $C M=20 a, C N=38 a, M N=22 a$.

由余弦定理：

$$
\cos \angle M N C=\frac{22^{2}+38^{2}-20^{2}}{2 \times 22 \times 38}=\frac{191}{209} \Rightarrow \sin \angle M N C=\frac{60 \sqrt{3}}{209} .
$$

故 $\cos \angle A N C=\cos \left(\angle M N C+60^{\circ}\right)=\frac{191-60 \sqrt{3}}{418}$.

再运用余弦定理：

$A N^{2}+N C^{2}-2 \cos \angle A N C * A N * N C=A C^{2}=1 \Rightarrow(1164+240 \sqrt{3}) a^{2}=1$.

$$
S_{\triangle C M N}=120 \sqrt{3} a^{2}
$$

于是

$$
\frac{1}{S_{\triangle D E F}}+\frac{1}{S_{\triangle X Y Z}}=\frac{1}{S_{\triangle C M N}}\left(\left(\frac{C M}{D E}\right)^{2}+\left(\frac{C M}{X Y}\right)^{2}\right)
$$

结合

$$
\frac{C M}{D E}=\frac{\sin \angle M D C}{\sin 60^{\circ}}, \frac{C M}{X Y}=\frac{\sin \angle M X D}{\sin 60^{\circ}}=\frac{\cos \angle M D C}{\sin 60^{\circ}},
$$

代人便得

$$
\frac{1}{S_{\triangle D E F}}+\frac{1}{S_{\triangle X Y Z}}=\frac{97 \sqrt{2}+40 \sqrt{3}}{15} .
$$

评注：本题是中等难度的几何题. 对于内接三角形的刻画使用 Miquel 点十分方便. (对于图形的进一步性质, 仍可参考《近代欧式几何学》第七章.) 上述证明中关于顺逆相似的判断以及导角使用有向角会更加清晰. 本题另一部分难度在于复杂的计算. 有不少使用直接计算方法的同学会得到两个答案： $\frac{97 \sqrt{2}+40 \sqrt{3}}{15}$和 $\frac{97 \sqrt{2}-40 \sqrt{3}}{15}$. 其舍根原因是条件 “点 $D, E, F$ 分别在线段 $B C, C A, A B$ 内部”.此方法利用构造的一个三角形和逆相似解决这一问题.

3. 给定正整数 $m$ 和 $n$. 将正 $2 m+2 n$ 边形的 $2 m$ 个顶点染黑色, 其余 $2 n$个顶点染白色. 定义两个黑点 $B, C$ 的染色距离 $d(B, C)$ 为直线 $B C$ 两侧的白点数目的较小者; 定义两个白点 $W, X$ 的染色距离 $d(W, X)$ 为直线 $W X$ 两侧的黑点数目的较小者.

一个黑点配对方案 $\mathcal{B}$ 是指将所有 $2 m$ 个黑点标记为 $B_{1}, \cdots, B_{m}, C_{1}, \cdots$, $C_{m}$, 使得 $m$ 条线段 $B_{i} C_{i}(1 \leq i \leq m)$ 两两不相交. 对任一黑点配对方案 $\mathcal{B}$, 记

$$
\mathcal{P}(\mathcal{B})=\sum_{i=1}^{m} d\left(B_{i}, C_{i}\right)
$$

一个白点配对方案 $\mathcal{W}$ 是指将所有 $2 n$ 个白点标记为 $W_{1}, \cdots, W_{m}, X_{1}, \cdots$,
$X_{m}$, 使得 $n$ 条线段 $W_{i} X_{i}(1 \leq i \leq n)$ 两两不相交. 对任一白点配对方案 $\mathcal{W}$, 记

$$
\mathcal{P}(\mathcal{W})=\sum_{i=1}^{n} d\left(W_{i}, X_{i}\right)
$$

求证：无论顶点的染色方式如何，均有

$$
\max _{\mathcal{B}} \mathcal{P}(\mathcal{B})=\max _{\mathcal{W}} \mathcal{P}(\mathcal{W})
$$

其中等式两边的最大值分别在所有可能的黑点配对方案 $\mathcal{B}$ 和白点配对方案 $\mathcal{W}$中选取。

解：对给定的配对方案 $\mathcal{B}, \mathcal{W}$. 记此时黑色线段 $B_{i} C_{i}$ 与所有白色线段 $W_{j} X_{j}$ $(j=1,2, \cdots, n)$ 的交点个数为 $x_{i}$. 显然 $d\left(B_{i}, C_{i}\right) \geq x_{i}$.

下面证明:对任意给定的 $\mathcal{B}$, 均存在 $\mathcal{W}$, 使得: $x_{i}=d\left(B_{i}, C_{i}\right)(i=1,2, \cdots, m)$.我们对 $m+n$ 归纳证明.

若 $m=1$ 或 $n=1$ 显然成立. 下设 $m \geq 2, n \geq 2$.

假设结论对于小于 $m+n$ 时成立, 考虑 $m, n$ 时情形.

若存在 $i$, 使得 $d\left(B_{i}, C_{i}\right)=0$, 即 $B_{i} C_{i}$ 一侧没有白点. 去掉 $B_{i}, C_{i}$ 两点,问题转化为 $m-1, n$ 时情形. 由归纳假设成立.

以下不妨假设 $d\left(B_{i}, C_{i}\right) \geq 1$.

若存在 $j, k, 1 \leq j<k \leq m$, 使得 $d\left(B_{k}, C_{k}\right)=d\left(B_{j}, C_{j}\right)=n$, 则线段 $B_{k} C_{k}$和 $B_{j} C_{j}$ 之间没有白色顶点. 去掉 $B_{k} C_{k}$, 则问题转化为 $m-1, n$ 情形. 由归纳假设成立.

若存在唯一的 $j$ 使得 $d\left(B_{j}, C_{j}\right)=n$, 分别延顺时针方向和逆时针方向取离 $B_{j}$ 最近的白点 $S, T, S T$ 一侧全是黑点且包含 $B_{j}$, 我们限定 $\mathcal{W}$ 中, 将 $S, T$ 配对, 其他白色顶点的配对连线一定与 $S T$ 不交, 故此时去掉 $S, T$ 两点, 不影响其他白色顶点. 又与 $S T$ 不相交的黑色线段距离不变, 与 $S T$ 相交 (删去 $S, T$后少了这个交点) 的黑色线段距离减 1 , 问题转化为 $n-1$ 时情况, 由归纳假设成立.

下设 $d\left(B_{i}, C_{i}\right)<n$ 对于所有 $i$ 成立. 令 $f\left(B_{i}, C_{i}\right)$ 为 $B_{i} C_{i}$ 含白点个数更多一侧黑色线段的个数, 不妨设 $B_{j}, C_{j}$ 满足 $f\left(B_{j}, C_{j}\right)$ 最小. 记 $B_{j} C_{j}$ 白点个数更多的一侧为左侧. 分别沿顺时针方向和逆时针方向取离 $B_{j}$ 最近的白点 $S, T$,去掉 $S, T$.

由 $f\left(B_{j}, C_{j}\right)$ 最小性, $B_{j} C_{j}$ 的左侧任一配对 $B_{u} C_{u}$ 右侧白点个数一定更多.其右侧白点个数至少 $n+1$.

类似地, $B_{j}, C_{j}$ 的右侧任一配对 $B_{t} C_{t}$ 左侧白点个数一定更多. 其左侧白点
个数 $\geq B_{j} C_{j}$ 左侧白点个数 $\geq n+1$.

因此, 去掉 $S, T$ 后, 对于与 $S T$ 不相交的黑色线段距离依然不变, 与 $S T$相交的黑色线段距离减 1 , 问题转化为 $n-1$ 的情形, 由归纳假设成立.

于是命题得证.

回到原题. 我们证明了存在 $\mathcal{W}$, 使得 $x_{i}=d\left(B_{i}, C_{i}\right)$ 对任意 $i$ 成立.

故 $\max _{\mathcal{B}} P(\mathcal{B})$ 为所有合法的配对方案中, 黑色线段与白色线段的交点个数最大值.

同理由对称性 $\max _{\mathcal{W}} \mathcal{P}(\mathcal{B})$ 也为此值. 故

$$
\max _{\mathcal{B}} \mathcal{P}(\mathcal{B})=\max _{\mathcal{W}} \mathcal{P}(\mathcal{W})
$$

得证.

评注：本题是一道中等难度的第三题. 这个证明中的引理基本上所有解答都需要. 而引理的证明虽然多样, 但是本质都要利用“最长边” 来构造一个配对. 这可以从下面一点看出：在引理中，如果有一对黑点平分白点（即两边各有 $n$ 个白点)，那么白点的配对方案事实上是唯一的, 即将左边 $n$ 个白点顺次配给右边白点. 这个特例暗示着我们考虑最长边, 然后后半部分的证明就不难了.

4. 求最小的整数 $n \geq 3$, 满足: 平面上存在 $n$ 个点 $A_{1}, A_{2}, \cdots, A_{n}$, 其中任意三点不共线, 且对任意 $1 \leq i \leq n$, 存在 $1 \leq j \leq n(j \neq i)$, 使得线段 $A_{j} A_{j+1}$经过线段 $A_{i} A_{i+1}$ 的中点, 这里 $A_{n+1}=A_{1}$.

证明: 一方面, 取 $A_{1}, \cdots, A_{6}$ 为 $(-1,-10),(0,1),(1,-10),(-1,0),(0,-9),(1,0)$则六个点满足 $A_{1} A_{2}, A_{4} A_{5} ; A_{2} A_{3}, A_{5} A_{6} ; A_{3} A_{4}, A_{6} A_{1}$ 互相平分，且图中没有三点共线. 满足要求.

另一方面, 来证明 $n \leq 6$. 易知 $A_{i} A_{i+1}$ 的中点一定不在 $A_{i-1} A_{i}$ 及 $A_{i+1} A_{i+2}$上, 因此我们有以下结论:

$n=3$ 时, $A_{1} A_{2}$ 的中点无法在其他直线上出现，矛盾。

$n=4$ 时, $A_{i} A_{i+1}$ 的中点一定在 $A_{i+2} A_{i+3}$ 上, 所以 $A_{1} A_{3} A_{2} A_{4}$ 为平行四边形, 此时 $A_{2} A_{3}$ 的中点不在 $A_{4} A_{1}$ 上出现, 矛盾.

$n=5$ 时, 若存在 $i \neq j$ 使得 $A_{i} A_{i+1}$ 的中点在 $A_{j} A_{j+1}$ 上且 $A_{j} A_{j+1}$ 的中点在 $A_{i} A_{i+1}$ 上, 即图中出现平行四边形 $A_{i} A_{j} A_{i+1} A_{j+1}$, 不妨设为线段 $A_{1} A_{2}$线段 $A_{3} A_{4}$ 互相平分. 此时 $A_{2} A_{3}$ 的中点在 $A_{4} A_{5}$ 或 $A_{5} A_{1}$ 上, 由对称性不妨设在 $A_{4} A_{5}$ 上.
此时若 $A_{4} A_{5}$ 的中点在 $A_{2} A_{3}$ 上, 则有 $A_{3} A_{5} \| A_{2} A_{4}$, 又由于 $A_{1} A_{3} \| A_{2} A_{4}$,因此 $A_{1}, A_{3}, A_{5}$ 三点共线, 矛盾.

此时必有 $A_{4} A_{5}$ 的中点在 $A_{1} A_{2}$ 上, 设 $A_{1} A_{2}, A_{2} A_{3}, A_{4} A_{5}$ 的中点分别为 $L, M, N, A_{5} A_{1}$ 与 $A_{3} A_{4}$ 和 $A_{2} A_{3}$ 的交点分别为 $P, Q$, 我们有

$$
\frac{A_{5} P}{A_{1} P}=\frac{A_{3} A_{5}}{A_{1} L}=\frac{A_{3} A_{5}}{L A_{2}}<\frac{A_{3} A_{5}}{N A_{2}}=1,
$$

所以 $P$ 不为 $A_{5} A_{1}$ 的中点, 同理点 $Q$ 不为 $A_{5} A_{1}$ 的中点, 矛盾.

若不存在 $i \neq j$ 使得 $A_{i} A_{i+1}$ 的中点在 $A_{j} A_{j+1}$ 上且 $A_{j} A_{j+1}$ 的中点在 $A_{i} A_{i+1}$ 上, 即图中不出现平行四边形 $A_{i} A_{j} A_{i+1} A_{j+1}$, 由对称性, 不妨设 $A_{1} A_{2}$的中点在 $A_{3} A_{4}$ 上, 则 $A_{3} A_{4}$ 的中点一定在 $A_{5} A_{1}$ 上, $\cdots$

所以对所有直线 $A_{i} A_{i+1}$ 均经过某条其它题设直线的中点. 考虑这五个点的凸包.

若为三角形或四边形, 则必存在线段 $A_{i} A_{i+1}$ 为凸包的边, 其它 3 个点均在直线同侧，则线段 $A_{i} A_{i+1}$ 不会经过其他题设直线的中点，矛盾.

凸包为五边形时, 则不存在线段 $A_{i} A_{i+1}$ 为凸包的边. 则凸包上必为五个点顺次排列为 $A_{1} A_{3} A_{5} A_{2} A_{4}$. 如下图, 有

$$
\begin{aligned}
& S_{\triangle A_{1} A_{3} A_{4}}=S_{\triangle A_{2} A_{3} A_{4}}, \\
& S_{\triangle A_{1} A_{2} A_{4}}<S_{\triangle A_{1} A_{2} A_{3}}
\end{aligned}
$$

故有

$$
S_{\triangle A_{1} A_{2} A_{4}}<S_{\triangle A_{1} A_{4} A_{3}} .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_731f1bd5cedeefb97053g-09.jpg?height=492&width=557&top_left_y=1847&top_left_x=772)

对称地，

$$
S_{\triangle A_{1} A_{2} A_{4}}<S_{\triangle A_{1} A_{4} A_{3}}<S_{\triangle A_{5} A_{4} A_{3}}<\cdots<S_{\triangle A_{1} A_{2} A_{4}}
$$

矛盾.

综上所述, $n$ 的最小值为 6 .

评注：本题是一道简单的组合几何题. $n=6$ 的构造可以容易想到, 而证明部分需要讨论，其中最难的部分是利用三角形面积的大小关系导出矛盾. 换句话说, 本题也可以直接取面积最小的三角形来解决这一部分. 不过笔者认为对凸包进行讨论的方法更加稳妥且自然.

5. 证明存在正数 $C$, 使得如下结论成立:

对任意一个无穷多项的正整数等差数列 $a_{1}, a_{2}, a_{3}, \cdots$, 若 $a_{1}$ 和 $a_{2}$ 的最大公约数无平方因子，则存在正整数 $m \leq C a_{2}^{2}$ ，使得 $a_{m}$ 无平方因子.

注：称正整数 $N$ 无平方因子，若它不被任何大于 1 的平方数整除.

证明：设 $\left(a_{1}, a_{2}\right)=d$, 则根据条件, $d$ 不含平方因子. 设整数 $x, y$ 满足 $a_{n}=d(x+n y)$. 若 $x y=0$, 则显然存在满足条件的 $a_{m}$. 故不妨设 $x, y$ 非零,这时有 $(x, y)=1$. 记 $m_{0}=c a_{2}^{2}=c d^{2}(x+2 y)^{2}$. 下用反证法证明 $a_{1}, a_{2}, \cdots, a_{m_{0}}$中存在某一项没有平方因子.

若对于任意 $m<m_{0}, a_{m}$ 均有平方因子，即存在素数 $p$ 使得 $p^{2} \mid a_{m}$. 我们将所有能够整除 $a_{1}, a_{2}, \cdots, a_{m_{0}}$ 中至少一项的素数构成的集合记为 $M$ ，并根据能否整除 $d$ 将 $M$ 划分为 $P$ (能整除 $d$ ) 和 $Q$ (不能整除 $d$ ).

情形 $1: P, Q$ 均非空.

记 $P=\left\{p_{1}<p_{2}<\cdots<p_{k}\right\}, Q=\left\{q_{1}<q_{2}<\cdots<q_{t}\right\}$. 注意到

$$
p_{i}^{2}\left|a_{n} \Leftrightarrow p_{i}^{2}\right| d(x+n y) \Leftrightarrow p_{i} \mid x+n y .
$$

所以 $a_{1}, a_{2}, \cdots, a_{m_{0}}$ 中至少有 $\frac{m_{0}}{p_{1} p_{2} \cdots p_{k}}$ 个不为 $p_{i}^{2}(i=1,2, \cdots, k)$ 的倍数.

记 $A=\frac{1}{p_{1} p_{2} \cdots p_{k}}$, 易知 $A \geq \frac{1}{d}$.

注意对任何整数 $s, v, a_{s+v p_{1} p_{2} \cdots p_{k}} \equiv a_{s}\left(\bmod p_{1}^{2} p_{2}^{2} \cdots p_{k}^{2}\right)$.

故我们可以从 $a_{1}, a_{2}, \cdots, a_{m_{0}}$ 中选出下标公差为 $p_{1} p_{2} \cdots p_{k}$ 且不被任何 $p_{i}^{2}$整除的 $A m_{0}$ 个数.

在这些数中, 若存在某个 $q_{j}(1 \leq j \leq t)$ 使得 $q_{j}^{2} \mid a_{n}$, 则有 $q_{j}^{2} \mid x+n y$. 注意到 $\left(p_{1} p_{2} \cdots p_{k}, q_{j}^{2}\right)=1(j=1,2, \cdots, t)$, 所以这 $A m_{0}$ 个数中至多有 $\left\lfloor\frac{A m_{0}}{q_{j}^{2}}\right\rfloor+1$ 个为 $q_{j}^{2}$ 的倍数.

于是选出的数中不被任何 $q_{j}^{2}$ 整除的数的个数不少于

$$
A m_{0}-\sum_{j=1}^{t}\left(A m_{0} \frac{1}{q_{j}^{2}}+1\right)=A m_{0}\left(1-\sum_{j=1}^{t} \frac{1}{q_{j}^{2}}\right)-t
$$

其中，

$$
1-\sum_{j=1}^{t} \frac{1}{q_{j}^{2}} \geq 1-\frac{1}{4}-\frac{1}{2 \times 3}-\frac{1}{3 \times 4}-\cdots \geq \frac{1}{4}
$$

另一方面，根据 $q_{1}, \cdots, q_{t}$ 的定义，有

$$
q_{t}^{2} \leq \frac{a_{m_{0}}}{d} \Rightarrow t^{2} \leq x+c d^{2}(x+2 y)^{2} y \leq d^{2}(x+2 y)^{2}(c+1) y
$$

所以取 $c=24$ 时,

$$
\begin{aligned}
A m_{0}\left(1-\sum_{j=1}^{t} \frac{1}{q_{j}^{2}}\right)-t & \geq \frac{m_{0}}{4 d}-t \\
& \geq \frac{c d(x+2 y)^{2}}{4}-d(x+2 y) \sqrt{(c+1) y} \\
& \geq d(x+2 y) \sqrt{y}\left(\frac{c}{4}-\sqrt{c+1}\right) \\
& \geq \frac{c}{4}-\sqrt{c+1}>0
\end{aligned}
$$

故 $a_{1}, \cdots, a_{m_{0}}$ 中至少存在一项不被任何 $p_{i}^{2}(i=1,2, \cdots, k)$ 或 $q_{j}^{2}(j=1,2, \cdots, t)$整除，矛盾.

情形 2: $Q$ 为空集.

$p_{1}, \cdots, p_{k}$ 同情形 1 中的定义. 根据情形 1 中的分析, $a_{1}, a_{2}, \cdots, a_{m_{0}}$ 中至少有 $\frac{m_{0}}{p_{1} p_{2} \cdots p_{k}}$ 个不为 $p_{i}^{2}(i=1,2, \cdots, k)$ 的倍数. 而显然 $\frac{m_{0}}{p_{1} p_{2} \cdots p_{k}} \geq 1$, 成立.

情形 3: $P$ 为空集而 $Q$ 不是.

$q_{1}, q_{2}, \cdots, q_{t}$ 同情形 1 中的定义. 则由情形 1 中的分析, $a_{1}, a_{2}, \cdots, a_{m_{0}}$ 中不被任何 $q_{j}^{2}$ 整除的数的个数不少于

$$
m_{0}-\sum_{j=1}^{t}\left(m_{0} \frac{1}{q_{j}^{2}}+1\right)>A m_{0}\left(1-\sum_{j=1}^{t} \frac{1}{q_{j}^{2}}\right)>0 .
$$

成立.

综上得证.

评注：本题是一道中等难度的数论估计题. 其估计想法是熟知的, 即计算密度. 不过具体的细节需要分析. 这里我们采用只看数列中除以 $d$ 后与 $d$ 互素的那些项。(事实上，其他项都必有平方因子，因此不必考虑. ) 注意证明的严谨性，有不少考生在此题扣分.

6. 有 $n(n \geq 8)$ 座机场, 某些机场之间有单向直达航线. 对任意两座机场 $a, b$,从 $a$ 飞往 $b$ 的单向直达航线至多一条 (可能同时有从 $a$ 飞往 $b$ 的和从 $b$ 飞往 $a$ 的单向直达航线)。已知对任意由若干座机场构成的集合 $A(1 \leq|A| \leq n-1)$,都有至少 $4 \min \{|A|, n-|A|\}$ 条单向直达航线从 $A$ 中的机场飞往 $A$ 之外的机场.
求证：对任意一座机场 $x$, 都可以从 $x$ 出发, 经过不超过 $\sqrt{2 n}$ 条单向直达航线回到机场 $x$.

解：构造图 $G$, 原命题等价于 $n$ 阶有向图 $G$, 满足对任意两个顶点 $a, b, a$到 $b$ 的边至多一条 (可以同时存在 $a$ 到 $b$ 的边及 $b$ 到 $a$ 的边). 已知对任一顶点集 $A \subset V(G)(1 \leq|A| \leq n-1)$, 都有至少 $4 \min \{|A|, n-|A|\}$ 条不同的边，从 $A$ 中的某个顶点指向 $A$ 外的某个顶点. 即证对任意顶点 $x$, 都存在一条长度不超过 $\sqrt{2 n}$ 的圈包含 $x$.

显然有对任意顶点 $u, v$, 存在 $u$ 到 $v$ 的有向路径. (否则取 $A=\{y \in V(G) \mid$存在 $u$ 到 $y$ 的有向路径 $\}$ 即得到矛盾)

定义 $d(u, v)$ 为 $u$ 到 $v$ 的最短有向路径的长度,

$$
N_{d}(x)=\{y \in V(G) \mid d(x, y)=d\}, n_{d}(x)=\left|N_{d}(x)\right|, S_{k}=\sum_{d=0}^{k} n_{d}(x)
$$

取 $A=\bigcup_{d=0}^{k} N_{d}(x), B=\bigcup_{d>k+1} N_{d}(x)$, 则 $A$ 到 $B$ 的边均为从 $N_{k}(x)$ 中的点引向 $N_{k+1}(x)$, 这样的边至少 $4 \min \left\{S_{k}, n-S_{k}\right\}$ 条.

取 $k_{0}$ 满足 $S_{k_{0}} \leq n-S_{k_{0}}, S_{k_{0}+1}>n-S_{k_{0}+1}$,

则当 $k \leq k_{0}$ 时, $A$ 到 $B$ 的边至少有 $4 S_{k}$ 条，这样我们得到

$$
\begin{gathered}
n_{k}(x) n_{k+1}(x) \geq 4 S_{k},\left(S_{k+1}-S_{k}\right)\left(S_{k}-S_{k-1}\right) \geq 4 S_{k} \\
S_{k+1} \geq \frac{4 S_{k}}{S_{k}-S_{k-1}}+S_{k}=\frac{4 S_{k-1}}{S_{k}-S_{k-1}}+\left(S_{k}-S_{k-1}\right)+4+S_{k-1} \geq\left(\sqrt{S_{k-1}}+2\right)^{2}
\end{gathered}
$$

又由条件知 $S_{1} \geq 4$, 因此我们得到 $S_{k_{0}} \geq\left(2 k_{0}+1\right)^{2} \geq\left(k_{0}+1\right)^{2}$.

但 $S_{k_{0}} \leq \frac{n}{2} \Rightarrow k_{0} \leq \sqrt{\frac{n}{2}}-1$.

类似考虑 $N_{d}^{\prime}(x)=\{y \in V(G) \mid d(y, x)=d\}$,

则有 $k_{1}$ 使得 $S_{k_{1}}^{\prime} \leq \frac{n}{2}, S_{k_{1}+1}^{\prime}>\frac{n}{2}$,

对称地有 $k_{1} \leq \sqrt{\frac{n}{2}}-1$.

由于 $S_{k_{1}+1}^{\prime}+S_{k_{0}+1}>n$, 知 $\bigcup_{d=0}^{k_{0}+1} N_{d}(x)$ 与 $\bigcup_{d=0}^{k_{1}+1} N_{d}^{\prime}(x)$ 有公共点 $y$. 则存在 $x$到 $y$ 的有向路径长度至多 $\sqrt{\frac{n}{2}}$, 存在 $y$ 到 $x$ 的有向路径长度至多 $\sqrt{\frac{n}{2}}$,

故存在一条长度不超过 $\sqrt{2 n}$ 的圈包含 $x$. 得证.

评注：本题是较简单的冬令营第六题，考察图论. 主要想法在于使用有向图的 BFS，并对此结构使用条件. 这样便转化成一个不难的数列问题，就完成了证明. 也有同学仅使用了单向的 BFS 结构就解决了问题, 不过这种做法需要讨论前几层点数超过 $\frac{n}{2}$.

