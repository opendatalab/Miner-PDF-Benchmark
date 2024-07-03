# 例说 “双标限定” 中求和顺序的交换 

冯跃峰

在 “组合求和” 中, 交换求和顺序, 是一种常见变形方式. 如果求和限定只涉及一个参数, 则我们称之为“单标限定”的求和形式.

对于 “单标限定” 的多层组合求和, 交换求和顺序是非常简单的, 直接交换求和符号的位置即可. 比如：

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i j}=\sum_{j=1}^{n} \sum_{i=1}^{n} x_{i j}
$$

如果求和限定涉及多个参数, 则我们称之为 “双标限定” 的求和形式.

“双标限定” 的求和形式中, 参数限定的一般描述为: $f(i, j)$ 具有性质 $p$, 比如: $i+j \leq n, i<j$ 等等.

值得指出的是, “双标限定”在单一求和中的意义是不明确的. 比如, 你能看出 “ $S=\sum_{i|k, j| k} 1$ ”表达的是什么意思吗?

如果是对 $i 、 j$ 求和, 则 $S$ 表示: $k$ 的约数对 $(i, j)$ 的个数; 如果是对数对 $k$求和, 则 $S$ 表示: $i 、 j$ 的公倍数的个数.

因此, 双标限定通常出现在多级求和的内层中, 其一般形式为

$$
\sum_{i \text { 具有性质 } p f(i, j) \text { 具有性质 } q} .
$$

因为外层的流动参数为 $i$ (对 $i$ 求和), 求和过程使内层的参数 $i$ 相对固定, 从而内层的流动参数为 $j$ (对 $j$ 求和).

比如, 多级求和“ $\sum_{\text {奇数 } k \leq n i|k, j| k} 1$ ” 中, 因为外层对 $k$ 求和, 当 $k$ 取定后, 假定 $k=3$, 则内层表达的意义是: 3 的约数对 $(i, j)$ 的个数. 即 $\sum_{i|3, j| 3} 1=4$, 这是因为约数对 $(i, j)=(1,1),(1,3),(3,1),(3,3)$.

对于含有双标限定的求和顺序的交换, 并非简单地交换求和符号的位置, 需遵循下述规则.

修订日期: 2022-02-22.
【交换顺序规则】对于多级求和 $\sum_{i \text { 具有性质 } p f(i, j) \text { 具有性质 } q}$, 将外层的流动参数 $i$ 移到内层时, 还必须同时受到内层求和对 $i$ 的限定, 所以需取两个限定的交集, 作为对 $i$ 的新限定. 将内层的流动参数 $j$ 移到外层时, 还必须同时考虑外层求和中 $j$ 的流动, 所以需取两个限定的并集, 作为对 $j$ 的新限定.

简言之: 内到外求并; 外到内求交.

下面以矩阵的“上三角”求和为例说明之.

对于矩阵 $\left(a_{i j}\right)_{n \times n}$, 其上三角求和为 $\sum_{i=1}^{n} \sum_{j=i}^{n} a_{i j}$, 它的内层求和含有双标限定.

如何交换其求和顺序? 有些同学对此很难准确把握, 其实很简单, 只需按照前述规则进行即可, 无需借助几何直观.

$$
\left(\begin{array}{ccccc}
a_{11} & a_{12} & \cdots & a_{1, n-1} & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2, n-1} & a_{2 n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
a_{n-1,1} & a_{n-1,2} & \cdots & a_{n-1, n-1} & a_{n-1, n} \\
a_{n, 1} & a_{n, 2} & \cdots & a_{n, n-1} & a_{n n}
\end{array}\right)
$$

为便于计算两个限定的交与并, 先将限定换成集合的“描述表示”形式：

$$
\sum_{i=1}^{n} \sum_{j=i}^{n} a_{i j}=\sum_{1 \leq i \leq n} \sum_{n \geq j \geq i} a_{i j}
$$

将内层的 $j$ 移到外层, 由 $1 \leq i \leq n, i \leq j \leq n$ 求并, 得 $j \in \bigcup_{i=1}^{n}[i, n]=[1, n]$,外层求和变成 $\sum_{1<j<n}$.

将外层的 $i$ 移到内层, 由 $1 \leq i \leq n, i \leq j \leq n$ 求交, 得 $i \in[1, n] \cap[1, i]=$ $[1, i]$, 内层求和变成 $\sum_{1 \leq i \leq j}$.

于是,

$$
\sum_{1 \leq i \leq n} \sum_{n \geq j \geq i} a_{i j}=\sum_{1 \leq j \leq n} \sum_{1 \leq i \leq j} a_{i j}
$$

即 $\sum_{i=1}^{n} \sum_{j=i}^{n} a_{i j}=\sum_{j=1}^{n} \sum_{i=1}^{j} a_{i j}$.

下面介绍一个数论中涉及“双标限定”组合求和的例子.

【题目】设无穷实数列 $\left\{x_{n}\right\}$ 满足 $x_{1}=1$, 试证: 对任何整数 $n \geq 2$, 有

$$
\sum_{i \mid n} \sum_{j \mid n} \frac{x_{i} x_{j}}{[i, j]} \geq \prod_{\text {质数 } p \mid n}\left(1-\frac{1}{p}\right)
$$

其中 $\sum_{i \mid n}$ 表示对 $n$ 的所有正因子 $i$ 求和, $[i, j]$ 表示 $i 、 j$ 的最小公倍数， $\prod_{\text {质数 } p \mid n}$ 表
示对 $n$ 的所有质因子 $p$ 求积. (2018 中国女子数学奥林匹克)

【述评】本题非常优美, 其结论仅与 $x_{1}$ 相关(其它项可任意取值), 这几乎不可思议! 这也是造成一些人解题失败的重要原因.

虽然它的样子非常吓人, 但实际上是只 “纸老虎”. 比如, 官方给出的解答本身就很简短, 可谓寥覀数语, 一气呵成 ${ }^{[1]}$ :

【证明】注意到, 对 $n$ 的因子 $i 、 j$, 从 1 到 $n$ 的整数中能被 $[i, j]$ 整除的数的个数为 $\frac{n}{[i, j]}$, 即有

$$
\frac{n}{[i, j]}=\sum_{[i, j] \mid k, k \leq n} 1
$$

由此可得

$$
\begin{aligned}
\sum_{i|n, j| n} x_{i} x_{j} \frac{n}{[i, j]} & =\sum_{i|n, j| n} x_{i} x_{j} \sum_{[i, j] \mid k, k \leq n} 1=\sum_{i|n, j| n} x_{i} x_{j} \sum_{i|k, j| k, k \leq n} 1 \\
& =\sum_{k \leq n} \sum_{i \mid(n, k)} \sum_{j \mid(n, k)} x_{i} x_{j}=\sum_{k \leq n}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} \\
& \geq \sum_{k \leq n,(k, n)=1}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2}=\sum_{k \leq n,(k, n)=1} x_{1}^{2}=\varphi(n),
\end{aligned}
$$

其中 $\varphi(n)$ 是欧拉 (Euler) 函数, 即 $1,2, \cdots, n$ 中与 $n$ 互素的数的个数. 熟知

$$
\varphi(n)=n \prod_{\text {质数 } p \mid n}\left(1-\frac{1}{p}\right),
$$

这就完成了证明.

但过细一看, 其组合运算也有点吓人, 相关符号的含义比较抽象. 假设你读到这个解答, 你会怎样处理?

常言道, 他山之石, 可以攻玉. 但数学阅读, 也颇有讲究, 通常可分为 3 个层次 ${ }^{[2]}$ : 第一个层次是读懂. 如果读不懂, 则说明存在知识的缺陷, 需要完善.

对于本题, 如果你存在阅读困难, 则很有可能是没有了解如下一些相关的背景知识 (涉及多方面的知识, 内容较为丰富).

(1) 组合求和(积)的两种表达方式.

(i) 普通方式: 下标流动, 如 $\sum_{i=1}^{n} x_{i}, \sum_{i \in \mathrm{I}} x_{i}, \sum_{1 \leq i<j \leq n} a_{i j}$ 等;

(ii) 简略方式: 代表元流动, 一般可表示为 $\sum_{x \in A} f(x)$. 特别地, $f(x)=1$ 时, 求和变成 $\sum_{x \in A} 1=|A|$.
题中的求积 “ $\prod_{\text {质数 } p \mid n}\left(1-\frac{1}{p}\right)$ ”采用的就是“简略方式”, 它实际上就是 $\prod_{i=1}^{r}\left(1-\frac{1}{p_{i}}\right)$,其中 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{r}^{\alpha_{r}}$.

(2)“双标限定”交换求和顺序的规则(如前面所述)；

(3) 相关的数论知识:

欧拉函数定义: $\varphi(n)=\sum_{k \leq n,(k, n)=1} 1$;

欧拉函数计算公式:

$$
\begin{aligned}
\varphi(n) & =n \prod_{i=1}^{r}\left(1-\frac{1}{p_{i}}\right)\left(\text { 下标 } i \text { 流动, 其中 } n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{r}^{\alpha_{r}}\right) \\
& =n \prod_{\text {质数 } p \mid n}\left(1-\frac{1}{p}\right)(\text { 代表元 } p \text { 流动 }) ;
\end{aligned}
$$

公倍数的性质: “ $a 、 b$ 的最小公倍数” 整除 “ $a 、 b$ 的公倍数” (利用质因数标准分解式即可看出), 由此便有

$$
a|k, b| k \Leftrightarrow k \text { 是 } a 、 b \text { 的公倍数 } \Leftrightarrow[a, b] \mid k \text {. }
$$

公约数的性质: “ $a 、 b$ 的公约数” 整除 “ $a 、 b$ 的最大公约数” (利用质因数标准分解式即可看出), 由此便有

$$
k|a, k| b \Leftrightarrow k \text { 是 } a 、 b \text { 的公倍数 } \Leftrightarrow k \mid(a, b) \text {. }
$$

(4) 计数公式

$x \geq 1 、 a \in \mathbb{N}^{*}$ 时, $\left[\frac{x}{a}\right]$ 是 $[1, x]$ 中被 $a$ 整除的数的个数:

$$
\left[\frac{x}{a}\right]=\sum_{1 \leq k \leq x, a \mid k} 1
$$

它的详细表示为 $\sum_{1 \leq k \leq x, k \in \mathbb{N}} f(k)$, 其中 $f(k)=\left\{\begin{array}{l}1(a \mid k), \\ 0(a \nmid k) .\end{array}\right.$

特别地, $x \geq 1$ 时, $[x]$ 是 $[1, x]$ 中格点(整数)的个数: $[x]=\sum_{1 \leq k \leq x, k \in \mathbb{N}} 1$.

(5) 多项式乘法规则

$$
\sum_{i \in A} \sum_{j \in A} x_{i} x_{i}=\sum_{i \in A} x_{i} \sum_{j \in A} x_{j}=\left(\sum_{i \in A} x_{i}\right)^{2}
$$

比如: $\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i} x_{j}=\left(\sum_{i=1}^{n} x_{i}\right)^{2}$.

如果熟悉上述一些知识, 读懂解答就是轻而易举的了. 当然, 原文排版有一处笔误: 漏掉一个“平方”符号(见文[1]).

阅读的第二层次是, 弄清其解答究竟是怎样想出来的. 下面, 我们着重剖析
上述解答的发现过程.

【题感】从条件看, 它过于简单, 先略去.

从目标看, 局部结构是我们非常熟悉的. 比如, 不等式右边就是我们的老朋友:

$$
\prod_{\text {质数 } p \mid n}\left(1-\frac{1}{p}\right)=\varphi(\mathrm{n}) / n \text {. }
$$

由此想到先“去分母”, 将不等式化简.

【结构联想】不等式等价于 $\sum_{i \mid n} \sum_{j \mid n} \frac{n}{[i, j]} x_{i} x_{j} \geq \varphi(n)$.

再看不等式的左边, 此时也出现了熟悉结构: $\frac{n}{[i, j]}$ 的意义为 $[1, n]$ 中被 $[i, j]$整除的数的个数(其中注意 $i|n, j| n \Leftrightarrow[i, j] \left\lvert\, n \Leftrightarrow \frac{n}{[i, j]}\right.$ 为整数).

$\frac{n}{[i, j]}=\sum_{1 \leq k \leq n,[i, j] k} 1(1$ 到 $n$ 中被 $[i, j]$ 整除的数 $k$ 的个数).

【参数转换】不等式可变成 $\sum_{i \mid n} \sum_{j \mid n}\left(\sum_{1 \leq k \leq n,[i, j] k} 1\right) x_{i} x_{j} \geq \varphi(n)$.

至此, 自然想到交换求和顺序, 将内外层求和对 $i 、 j$ 的限定融合在一起, 分离参数以便利用多项式乘法法则.

此外, 为使其限定与外层求和的限定一致, 需要将对 $i 、 j$ 限定的“捆绑形式” $[i, j] \mid k$, 转换为 “独立形式”: $i|k 、 j| k$ (由公倍数的性质, 这两个对 $i 、 j$ 的限定是等价的). 再将其与外层求和中 “ $i|n, j| n$ ”求交, 变成 $i|(n, k), j|(n, k)$.

于是,

$$
\begin{aligned}
\sum_{i \mid n} \sum_{j \mid n}\left(\sum_{1 \leq k \leq n,[i, j] \mid k} 1\right) x_{i} x_{j} & =\sum_{i \mid n} \sum_{j \mid n} \sum_{1 \leq k \leq n, i|k, j| k} x_{i} x_{j} \\
& =\sum_{1 \leq k \leq n} \sum_{i \mid(n, k)} \sum_{j \mid(n, k)} x_{i} x_{j}
\end{aligned}
$$

【换维思考】交换求和顺序, 不等式变成 $\sum_{1 \leq k \leq n} \sum_{i \mid(n, k)} \sum_{j \mid(n, k)} x_{i} x_{j} \geq \varphi(n)$.至此, 已成功分离参数, 可直接利用多项式乘法法则.

【结构联想】不等式变成 $\sum_{1 \leq k \leq n} \sum_{i \mid(n, k)} x_{i} \sum_{j \mid(n, k)} x_{j} \geq \varphi(n)$, 即

$$
\sum_{1 \leq k \leq n}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} \geq \varphi(n)
$$

至此, 不等式已是最简形式. 现在设法代入已知条件: $x_{1}=1$, 这只需将 $x_{1}$ 从求和中分离出来即可. 但此处有一个陷阱: 不能在内层求和中分拆, 而要在外层
求和中分拆. 这是因为 $x_{i}(i>1)$ 为实数, 未必为正, 无法进行 “舍项放缩”.

比如, 下述推理是错误的: $\sum_{1 \leq k \leq n}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} \geq \sum_{1 \leq k \leq n}\left(x_{1}\right)^{2}$.

如果瞄准目标, 就可避免跌入上述陷阱.

由欧拉函数定义: $\varphi(n)=\sum_{k \leq n,(k, n)=1} 1$, 不等式变为

$$
\sum_{1 \leq k \leq n}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} \geq \sum_{k \leq n,(k, n)=1} 1 .
$$

考察左边与右边的差异, 只需将左边的外层求和中分离出满足 $(k, n)=1$的 $k$ 对应的项即可, 其余的项舍弃.

## 【舍项放缩】

$$
\begin{aligned}
\sum_{1 \leq k \leq n}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} & =\sum_{1 \leq k \leq n,(k, n)=1}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2}+\sum_{1 \leq k \leq n,(k, n) \neq 1}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} \\
& \geq \sum_{1 \leq k \leq n,(k, n)=1}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2}=\sum_{1 \leq k \leq n,(k, n)=1}\left(x_{1}\right)^{2} \\
& =\sum_{k \leq n,(k, n)=1} 1=\varphi(n) .
\end{aligned}
$$

证毕.

## 【新写】

$$
\begin{aligned}
n \sum_{i \mid n} \sum_{j \mid n} \frac{x_{i} x_{j}}{[i, j]} & =\sum_{i \mid n} \sum_{j \mid n} \frac{n}{[i, j]} x_{i} x_{j}=\sum_{i \mid n} \sum_{j \mid n}\left(\sum_{1 \leq k \leq n,[i, j] \mid k} 1\right) x_{i} x_{j} \\
& =\sum_{i \mid n} \sum_{j \mid n} \sum_{1 \leq k \leq n, i|k, j| k} x_{i} x_{j}=\sum_{1 \leq k \leq n} \sum_{i \mid(n, k)} \sum_{j \mid(n, k)} x_{i} x_{j} \\
& =\sum_{1 \leq k \leq n} \sum_{i \mid(n, k)} \sum_{j \mid(n, k)} x_{i} x_{j}=\sum_{1 \leq k \leq n}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2} \\
& \geq \sum_{1 \leq k \leq n,(k, n)=1}\left(\sum_{i \mid(n, k)} x_{i}\right)^{2}=\sum_{1 \leq k \leq n,(k, n)=1}\left(x_{1}\right)^{2} \\
& =\sum_{k \leq n,(k, n)=1} 1=\varphi(n)=n \prod_{\text {质数 } p \mid n}\left(1-\frac{1}{p}\right),
\end{aligned}
$$

证毕.

阅读的第三层次是创新. 比如: 上述解答能否简化? 有没有思想相同、但表现方式不一样的新解答? 能不能用这一方法解决其它问题? 比如, 2021 年中国女
子数学竞赛中的一个组合求和问题, 这些都留给读者思考.

## 参考文献

[1] 2019 年 IMO 中国国家集训队教练组, 走向 IMO: 数学奥林匹克试题集锦 (2019)[M]. 上海: 华东师范大学出版社, 2019 年 10 月.

$[2]$ 冯跃峰, 数学阅读的三个层次 $[\mathrm{A}]$. 冷岗松主编, 数学竞赛问题与感悟, 第二卷: 研究文集(上) [C], 华东师范大学出版社, 2019 年 5 月.

