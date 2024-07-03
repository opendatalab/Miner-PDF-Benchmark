# “吃透” 目标是解题的关键 

—2021 年 IMO “压轴题” 思路分析

冯跃峰

今年 IMO 的“压轴题”有点特别, 难度并不算大, 但要找到解法却又很不容易. 也就是说, 它对思维层次的要求较高.

我们知道, 有些问题, 其条件看似非常熟悉, 表述也很简单, 但通常的“套路”在这里却派不上用场. 如何运用这些条件? 终是不明就里, 甚至造成解题失败.

这时, 我们需要跳过条件, 先透彻理解目标: 想象在怎样的情况下, 目标可以达到, 进而发现条件的实际意义.

今年 IMO 的 “压轴题” 就是这样的一个典型例子, 本文给出其解答的思路分析. 题目如下:

【原题】设整数 $m \geq 2$. 设集合 $A$ 由有限个整数 (不一定为正) 构成, 且 $B_{1}, B_{2}, B_{3}, \cdots, B_{m}$ 是 $A$ 的子集. 假设对任意 $k=1,2, \cdots, m, B_{k}$ 中所有元素之和为 $m^{k}$. 证明: $A$ 包含至少 $\frac{m}{2}$ 个元素.

【题感】从条件看, 涉及到有限集合 $A$ 的子集族及子集的 “元素和”,自然想到引入集合元素关系表 (相关性质及应用, 可在百度搜索“跃峰奥数代数组合 7-1”, 找到相关例子), 借以描述题给的关系, 实现问题的转化.

为此, 设 $A=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 构造 $n \times m$ 方格表 (见下页), 在第 $i$ 行第 $j$列填入数 $x_{i j}(1 \leq i \leq n, 1 \leq j \leq m)$, 其中 $x_{i j}= \begin{cases}1, & a_{i} \in B_{j}, \\ 0, & a_{i} \notin B_{j} .\end{cases}$

这样, 条件可表示为: $\sum_{i=1}^{n} x_{i j} a_{i}=S\left(B_{j}\right)=m^{j}(1 \leq j \leq m)$.

这是一种通性，最容易想到的是“叠合” (但其效果是否有作用并不得而知):

$$
\sum_{j=1}^{n} m^{j}=\sum_{j=1}^{m} \sum_{i=1}^{n} x_{i j} a_{i}=\sum_{i=1}^{n} a_{i} \sum_{j=1}^{m} x_{i j} .
$$[^0]

$$
\begin{aligned}
& \begin{array}{llll}
B_{1} & B_{2} & \cdots & B_{m}
\end{array} \\
& \begin{array}{c}
a_{1} \\
a_{2} \\
\vdots \\
a_{n}
\end{array}\left(\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 m} \\
x_{21} & x_{22} & \cdots & x_{2 m} \\
\vdots & \vdots & \vdots & \vdots \\
x_{n 1} & x_{n 2} & \cdots & x_{n m}
\end{array}\right)
\end{aligned}
$$

进一步, 原始条件还可用矩阵表示为:

$$
\left(a_{1}, a_{2}, \cdots, a_{n}\right)\left(\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 m} \\
x_{21} & x_{22} & \cdots & x_{2 m} \\
\vdots & \vdots & \vdots & \vdots \\
x_{n 1} & x_{n 2} & \cdots & x_{n m}
\end{array}\right)=\left(m^{1}, m^{2}, \cdots, m^{m}\right) .
$$

显然, 这些条件及其变异形式如何运用, 暂时都不得而知. 此外, 题中还有一个不起眼的条件 $(m \geq 2$ ", 它的意义也一时难以明白, 统统先跳过. 从目标看,用 $|A|$ 表示 $A$ 中元素个数, 目标为: $n=|A| \geq \frac{m}{2}$, 即 $m \leq 2 n$.

如何证明? 这是一个“参数” 不等式, 常用的方法之一是建立单射. 回顾前面的 “矩阵运算”, 发现它恰好具有映射功能: 一个 $n$ 维向量 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 与矩阵 $X=\left(x_{i j}\right)_{1<i \leq n, 1<j \leq m}$ 相乘之后, 得到一个 $m$ 维向量 $\left(m^{1}, m^{2}, \cdots, m^{m}\right)$.

由此想到, 要证明“ $m \leq 2 n$ ”, 只需利用这一“功能”, 建立 $m$ 维向量集合 $P$到 $n$ 维向量集合 $Q$ 的单射, 这样便有 $|P| \leq|Q|$. 它用参数 $m, n$ 表示即为: $p(m, n) \leq q(m, n)$. 期望解不等式, 能得到 $m \leq 2 n$.

但这个矩阵运算方向相反, 这交换乘法顺序即可. 下面将这些想法具体化.

【表格模型】设 $A=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 构造 $n \times m$ 方格表, 在第 $i$ 行第 $j$列填入数 $x_{i j}(1 \leq i \leq n, 1 \leq j \leq m)$, 其中 $x_{i j}= \begin{cases}1, & a_{i} \in B_{j}, \\ 0, & a_{i} \notin B_{j} .\end{cases}$

$$
\begin{aligned}
& \begin{array}{cccc}
B_{1} & B_{2} & \cdots & B_{m}
\end{array} \\
& \begin{array}{c}
a_{1} \\
a_{2} \\
\vdots \\
a_{n}
\end{array}\left(\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 m} \\
x_{21} & x_{22} & \cdots & x_{2 m} \\
\vdots & \vdots & \vdots & \vdots \\
x_{n 1} & x_{n 2} & \cdots & x_{n m}
\end{array}\right)
\end{aligned}
$$

依题意, 有

$$
\sum_{i=1}^{n} x_{i j} a_{i}=S\left(B_{j}\right)=m^{j}(1 \leq j \leq m)
$$

用矩阵运算表示为:

$$
\left(a_{1}, a_{2}, \cdots, a_{n}\right)\left(\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 m} \\
x_{21} & x_{22} & \cdots & x_{2 m} \\
\vdots & \vdots & \vdots & \vdots \\
x_{n 1} & x_{n 2} & \cdots & x_{n m}
\end{array}\right)=\left(m^{1}, m^{2}, \cdots, m^{m}\right)
$$

亦可简记为 $a X=b$, 其中

$$
X=\left(x_{i j}\right)_{1<i \leq n, 1<j \leq m}, a=\left(a_{1}, a_{2}, \cdots, a_{n}\right), b=\left(m^{1}, m^{1}, \cdots, m^{m}\right) .
$$

【建立映射】取集合

$P=\left\{\left(p_{1}, p_{2}, \cdots, p_{m}\right) \mid p_{i}\right.$ 具有性质 $\left.p\right\}, Q=\left\{\left(q_{1}, q_{2}, \cdots, q_{n}\right) \mid q_{j}\right.$ 具有性质 $\left.q\right\}$,

其中性质 $p, q$ 待定. 如何建立单射 $f: P \rightarrow Q$ ?一自然想到前面矩阵乘法的“映射功能”: $(a \rightarrow a X$ ” 是由 $n$ 维向量映射到 $m$ 维向量. 更换矩阵运算顺序, 则“ $p \rightarrow X p$ ” 是由 $m$ 维向量映射到 $n$ 维向量, 由此即可沟通 “条件”与 “子目标”之间的联系.

【沟通联系】对 $p=\left(p_{1}, p_{2}, \cdots, p_{m}\right), q=\left(q_{1}, q_{2}, \cdots, q_{n}\right), X=\left(x_{i j}\right)(1<$ $i \leq n, 1<j \leq m)$, 令 $p \rightarrow q=X p$, 即

$$
\left(\begin{array}{c}
p_{1} \\
p_{2} \\
\vdots \\
p_{m}
\end{array}\right) \rightarrow\left(\begin{array}{c}
q_{1} \\
q_{2} \\
\vdots \\
q_{n}
\end{array}\right)=\left(\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 m} \\
x_{21} & x_{22} & \cdots & x_{2 m} \\
\vdots & \vdots & \vdots & \vdots \\
x_{n 1} & x_{n 2} & \cdots & x_{n m}
\end{array}\right)\left(\begin{array}{c}
p_{1} \\
p_{2} \\
\vdots \\
p_{m}
\end{array}\right)=\left(\begin{array}{c}
\sum_{j=1}^{m} x_{1 j} p_{j} \\
\sum_{j=1}^{m} x_{2 j} p_{j} \\
\vdots \\
\sum_{j=1}^{m} x_{n j} p_{j}
\end{array}\right)
$$

略去 “矩阵” 运算, 则映射为

$$
\left(p_{1}, p_{2}, \cdots, p_{m}\right) \rightarrow\left(q_{1}, q_{2}, \cdots, q_{n}\right)=\left(\sum_{j=1}^{m} x_{1 j} p_{j}, \sum_{j=1}^{m} x_{2 j} p_{j}, \cdots, \sum_{j=1}^{m} x_{n j} p_{j}\right)
$$

下面计算像与原像的个数, 这需先确定 $p_{j}$ 的取值范围. 为简单起见, 想到使每个 $p_{j}$ 的取值范围相同: 都取特定的 $r$ 个值 ( $r$ 待定). 特别地, 可取 $1,2, \cdots, r$.

【待定参数】对 $1 \leq j \leq m$, 令 $p_{j} \in\{1,2, \cdots, r\}$, 即

$$
P=\left\{\left(p_{1}, p_{2}, \cdots, p_{m}\right) \mid 1 \leq p_{j} \leq r, 1 \leq j \leq m\right\}
$$

则由乘法原理, $|P|=r^{m}$.

再注意到 $x_{i j}=0,1$, 对 $1 \leq i \leq n$, 有

$$
0 \leq \sum_{j=1}^{m} x_{i j} p_{j} \leq \sum_{j=1}^{m} p_{j} \leq \sum_{j=1}^{m} r=r m .
$$

于是, 限定 $q_{j} \in\{0,1,2, \cdots, r m\}$, 则

$$
Q=\left\{\left(q_{1}, q_{2}, \cdots, q_{n}\right) \mid 0 \leq q_{j} \leq m r, 1 \leq j \leq n\right\},
$$

此时 $|Q|=(r m+1) n$,

如果 $f$ 是单射, 便有 $r^{m} \leq(r m+1) n$. 与目标 $m \leq 2 n$ 比较, 可尝试取 $r=n$, 便有 $m^{m} \leq\left(m^{2}+1\right) n$.

显然, 如果去掉上式右边括号中的 $\left(+1 "\right.$, 则有 $m^{m} \leq m^{2 n}$.

又 $m \geq 2$ (此时才发现题中条件 $(m \geq 2$ ” 的意义, 但这个条件并非必要:分类讨论即可: $m=1$ 时, $|A| \geq 1>\frac{1}{2}=\frac{m}{2}$ ), 所以 $m \leq 2 n$.

如何去掉上式右边括号中的 “ +1 ” ? 一一只需不等式 “ $0 \leq \sum_{j=1}^{m} x_{i j} p_{j} \leq m$ ” 左边改为严格不等式 (舍弃取值为 “ 0 ” 的情形), 即限定 $x_{i_{1}}, x_{i_{2}}, \cdots, x_{i_{m}}$ 不全为 0 ,也就是 $A$ 中每个元素 $a_{i}$ 至少在 $B_{1}, B_{2}, \cdots, B_{m}$ 之一中出现一次, 这优化假设即可.

【优化假设】不妨设 $A=B_{1} \cup B_{2} \cup \cdots \cup B_{m}$, 否则, 令 $B=B_{1} \cup B_{2} \cup \cdots \cup B_{m}$,若能证得 $|B| \geq \frac{m}{2}$, 则由 $B \subseteq A$, 当然有 $|A| \geq|B| \geq \frac{m}{2}$.

以下只需证明 $f$ 是单射, 采用反面思考.

【反面思考】假设存在两个不同向量 $\left(p_{1}, p_{2}, \cdots, p_{m}\right),\left(p_{1}^{\prime}, p_{2}^{\prime}, \cdots, p_{m}^{\prime}\right)$, 对应同一个像, 即

$$
\left(\sum_{j=1}^{m} x_{1 j} p_{j}, \sum_{j=1}^{m} x_{2 j} p_{j}, \cdots, \sum_{j=1}^{m} x_{n j} p_{j}\right)=\left(\sum_{j=1}^{m} x_{1 j} p_{j}^{\prime}, \sum_{j=1}^{m} x_{2 j} p_{j}^{\prime}, \cdots \sum_{j=1}^{m} x_{n j} p_{j}^{\prime}\right),
$$

那么,

$$
\sum_{j=1}^{m} x_{1 j}\left(p_{j}-p_{j}^{\prime}\right)=\sum_{j=1}^{m} x_{2 j}\left(p_{j}-p_{j}^{\prime}\right)=\cdots=\sum_{j=1}^{m} x_{n j}\left(p_{j}-p_{j}^{\prime}\right)=0
$$

令 $p_{j}-p_{j}^{\prime}=u_{j}$, 则 $u_{1}, u_{2}, \cdots, u_{m}$ 不全为 0 , 且

$$
\sum_{j=1}^{m} x_{1 j} u_{j}=\sum_{j=1}^{m} x_{2 j} u_{j}=\ldots=\sum_{j=1}^{m} x_{n j} u_{j}=0
$$

即对 $1 \leq i \leq n$, 都有 $\sum_{j=1}^{m} x_{i j} u_{j}=0 .(*)$

如何由 $(*)$ 导出矛盾? 这自然想到, 还有一个关键条件没有用到:

$$
\sum_{i=1}^{n} x_{i j} a_{i}=m_{j}((1 \leq j \leq m)
$$

发现它恰好具有消参功能 (捆绑消去 “ $x_{i j} a_{i}$ ”). 至此终于明白: 原来题中的关键条件就是为“单射”服务的.

为了捆绑 “ $x_{i j} a_{i}$ ”, 需对 $(*)$ 式进行“加权叠合” (先配上因子 $a_{i}$, 然后相加).
【加权】由 $(*)$, 有 (对 $j$ 求和, 与 $i$ 无关)

$$
0=a \sum_{j=1}^{m} x_{i j} u_{j}=\sum_{j=1}^{m} x_{i j} u_{j} a_{i}
$$

## 【叠合】

$$
0=\sum_{i=1}^{n} \sum_{j=1}^{m} x_{i j} u_{j} a_{i}=\sum_{j=1}^{m} \sum_{i=1}^{n} x_{i j} u_{j} a_{i}=\sum_{j=1}^{m} u_{j} \sum_{i=1}^{n} x_{i j} a_{i}=\sum_{j=1}^{m} u_{j}
$$

如何进一步消去“ $u_{j}$ ”一自然想到等式运用的“三板斧” (因数分析、模分析、不等式控制), 这里当然是用不等式控制放缩消元.

但这里 $u_{j}$ 有正有负, 想到使用绝对值不等式, 其“控制工具”为

$$
\left|u_{j}\right|=\left|p_{j}-p_{j}^{\prime}\right| \leq m-1\left(p_{j}, p_{j}^{\prime} \in\{1,2, \cdots, m\}\right) .
$$

## 【尝试错误】

$$
\begin{aligned}
0=\left|\sum_{j=1}^{m} u_{j} m^{j}\right| & \leq \sum_{j=1}^{m}\left|u_{j}\right| m^{j} \\
& \leq \sum_{j=1}^{m}(m-1) m^{j} \\
& =(m-1) \sum_{j=1}^{m} m^{j}=m^{m+1}-m .
\end{aligned}
$$

尽管这显然无法产生矛盾, 但却启发我们应在 “控制”前, 将等式中的绝对值最大的项移至左边, 期望 “大数 $\leq 小$ 数”产生矛盾.

“ $\sum_{j=1}^{m} u_{j} m^{j}$ ” 中哪个项的绝对值最大? 似乎是 “ $u_{m} m^{m}$ ”. 但一细想, 又发现 $u_{m}$可能为 0 ,于是, 想到考察极端: 取系数下标最大的非 0 项.

【考察极端】注意到 $u_{1}, u_{2}, \cdots, u_{m}$ 不全为 0 , 取最大下标 $g$, 满足 $u_{g} \neq 0$,但 $u_{h}=0(h>g)$, 则上式变成 $\sum_{j=1}^{g} u_{j} m^{j}=0$, 进而 $u_{g} m^{g}=\sum_{j=1}^{g-1} u_{j} m^{j}$.

以下再利用不等式控制, 即可产生矛盾.

## 【不等式控制】

$$
\begin{aligned}
\left|u_{g} m^{g}\right|=\left|\sum_{j=1}^{g-1} u_{j} m^{j}\right| & \leq \sum_{j=1}^{g-1}\left|u_{j}\right| m^{j} \\
& \leq \sum_{j=1}^{g-1}(m-1) m^{j} \\
& =(m-1) \sum_{j=1}^{g-1} m^{j} \\
& =m^{g}-m .
\end{aligned}
$$

但 $\left|u_{g} m^{g}\right|=\left|u_{g}\right| m^{g} \geq m^{g}$, 所以 $m^{g} \leq m^{g}-m$, 矛盾. 所以 $f$ 为单射, 命题获证.
【新写】设 $B=B_{1} \cup B_{2} \cup \cdots \cup B_{m}=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 则 $B \subseteq A$. 构造 $n \times m$ 方格表, 在第 $i$ 行第 $j$ 列填入数 $x_{i j}$, 其中 $x_{i j}=\left\{\begin{array}{l}1\left(a_{i} \in B_{j}\right), \\ 0\left(a_{i} \notin B_{j}\right) .\end{array}\right.$

依题意, 数表的每行、每列都不全为 0, 且

$$
\sum_{i=1}^{n} x_{i j} a_{i}=S\left(B_{j}\right)=m^{i}(1 \leq j \leq m)
$$

记 $P=\left\{\left(p_{1}, p_{2}, \cdots, p_{m}\right) \mid 1 \leq p_{j} \leq m, 1 \leq j \leq m\right\}, Q=\left\{\left(q_{1}, q_{2}, \cdots, q_{n}\right)\right.$ $\left.\mid 1 \leq q_{j} \leq m^{2}, 1 \leq j \leq n\right\}$, 则由乘法原理, $|P|=m^{m},|Q|=\left(m^{2}\right)^{n}=m^{2 n}$.

构造映射

$f:\left(p_{1}, p_{2}, \cdots, p_{m}\right) \rightarrow\left(q_{1}, q_{2}, \cdots, q_{n}\right)=\left(\sum_{j=1}^{m} x_{1 j} p_{j}, \sum_{j=1}^{m} x_{2 j} p_{j}, \cdots,, \sum_{j=1}^{m} x_{n j} p_{j}\right)$.

注意到 $x_{i j}=0,1$, 对 $1 \leq i \leq n$, 有

$$
0<\sum_{j=1}^{m} x_{i j} p_{j} \leq \sum_{j=1}^{m} p_{j} \leq \sum_{j=1}^{m} m=m^{2}
$$

所以 $\left(q_{1}, q_{2}, \cdots, q_{n}\right) \in Q, f$ 是 $P$ 到 $Q$ 的映射.

下面证明 $f$ 是单射.

假设 $P$ 中存在两个不同数组 $\left(p_{1}, p_{2}, \cdots, p_{m}\right),\left(p_{1}^{\prime}, p_{2}^{\prime}, \cdots, p_{m}^{\prime}\right)$, 对应 $Q$ 中同一个像, 即

$$
\left(\sum_{j=1}^{m} x_{1 j} p_{j}, \sum_{j=1}^{m} x_{2 j} p_{j}, \cdots, \sum_{j=1}^{m} x_{n j} p_{j}\right)=\left(\sum_{j=1}^{m} x_{1 j} p_{j}^{\prime}, \sum_{j=1}^{m} x_{2 j} p_{j}^{\prime}, \cdots \sum_{j=1}^{m} x_{n j} p_{j}^{\prime}\right),
$$

那么,

$$
\sum_{j=1}^{m} x_{1 j}\left(p_{j}-p_{j}^{\prime}\right)=\sum_{j=1}^{m} x_{2 j}\left(p_{j}-p_{j}^{\prime}\right)=\cdots=\sum_{j=1}^{m} x_{n j}\left(p_{j}-p_{j}^{\prime}\right)=0 .
$$

令 $p_{j}-p_{j}^{\prime}=u_{j}$, 则 $u_{1}, u_{2}, \cdots, u_{m}$ 不全为 0 , 且对 $1 \leq i \leq n$, 都有 $\sum_{j=1}^{m} x_{i j} u_{j}=0$.所以

$$
\sum_{j=1}^{m} x_{i j} u_{j} a_{i}=a_{i} \sum_{j=1}^{m} x_{i j} u_{j}=0(1 \leq i \leq n)
$$

进而

$$
0=\sum_{i=1}^{n} \sum_{j=1}^{m} x_{i j} u_{j} a_{i}=\sum_{j=1}^{m} \sum_{i=1}^{n} x_{i j} u_{j} a_{i}=\sum_{j=1}^{m} u_{j} \sum_{i=1}^{n} x_{i j} a_{i}=\sum_{j=1}^{m} u_{j} m^{j} .
$$

注意到 $u_{1}, u_{2}, \cdots, u_{m}$ 不全为 0 , 取最大下标 $g$, 满足 $u_{g} \neq 0$, 但 $u_{h}=0(h>$ $g)$, 则上式变成 $-u_{g} m^{g}=\sum_{j=1}^{g-1} u_{j} m^{j}$. 于是,

$$
\left|u_{g} m^{g}\right|=\left|\sum_{j=1}^{g-1} u_{j} m^{j}\right| \leq \sum_{j=1}^{g-1}\left|u_{j}\right| m^{j} \leq \sum_{j=1}^{g-1}(m-1) m^{j}=(m-1) \sum_{j=1}^{g-1} m^{j}=m^{g}-m .
$$

但 $\left|u_{g} m^{g}\right|=\left|u_{g}\right| m^{g} \geq m^{g}$, 所以 $m^{g} \leq m^{g}-m$, 矛盾.

所以 $f$ 为单射, 从而 $m^{m}=|P| \leq|Q|=m^{2 n}$. 又 $m \geq 2$, 得 $m \leq 2 n$.

因为 $B \subseteq A$, 所以 $|A| \geq|B|=n \geq \frac{m}{2}$, 命题获证.

【注】题中条件 $\left(m \geq 2\right.$ " 是多余的, 因为 $m=1$ 时, 由 $S\left(B_{1}\right)=1$ 可知, $A$ 非空, 从而 $|A| \geq 1>\frac{1}{2}=\frac{m}{2}$, 结论显然成立.


[^0]:    修订日期: 2021-08-16.

