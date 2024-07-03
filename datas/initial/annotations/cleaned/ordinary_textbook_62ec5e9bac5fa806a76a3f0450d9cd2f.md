# 2021 年 ELMO 试题解答与评析 

梁行健 刘翊哲 刘鹏远谢朋睿 张榕航<br>(湖南师范大学附属中学, 410006)<br>指导教师: 汤礼达

2021 年 ELMO 于 6 月 17, 18 日 $14: 00-18: 30$ 举行. 本次试题质量较高,其中 $1,3,4$ 较容易, 很适合联赛训练; $2,5,6$ 有一定难度, 是冬令营好的训练题.其中值得一提的是 6 , 观点独特, 内涵丰富, 很好地考察了学生的几何素养. 笔者水平有限, 不当之处还请指正.

## I. 试 题

1. 在 $\triangle A B C$ 中, 点 $P$ 和 $Q$ 分别在边 $A B$ 和 $A C$ 上, 使得 $\triangle A P Q$ 的外接圆与 $B C$ 相切于点 $D$. 边 $B C$ 上的点 $E$ 满足 $B D=E C$. 直线 $D P$ 再次交 $\triangle C D Q$的外接圆于 $X$, 直线 $D Q$ 再次交 $\triangle B D P$ 的外接圆于点 $Y$. 证明: $D 、 E 、 X 、 Y$四点共圆.



修订日期: 2021-08-01.

2. 给定整数 $n>1$ 和 $a_{1}, a_{2}, \cdots, a_{n}$, 且对 $1 \leq i \leq n$ 都有 $a_{i}$ 满足 $n \mid a_{i}-i$.证明: 存在无穷序列 $b_{1}, b_{2}, \cdots$ 满足:

(1) $b_{k} \in\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$ 对任意正整数 $k$ 成立;

(2) $\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}$ 是一个整数.

3. 在 $100 \times 100$ 的网格中, 每个格子都被涂成了 101 种颜色中的一种. 若一个格子满足, 在它所在的行和列的 199 个格子中, 每种颜色都至少出现了一次,那么我们称这个格子是多元化的. 求多元化的格子数目的最大可能值.
4. 将正整数集划分成 $n$ 个两两不交的无穷等差数列 $S_{1}, S_{2}, \cdots, S_{n}$, 它们的公差分别为 $d_{1}, d_{2}, \cdots, d_{n}$.

证明: 恰存在一个正整数 $i(1 \leq i \leq n)$ 使得 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \in S_{i}$.

5. 给定正整数 $n$ 和 $k$. 如果两个无穷数列 $\left\{s_{i}\right\}_{i \geq 1}$ 和 $\left\{t_{i}\right\}_{i \geq 1}$ 满足: 对任意正整数 $i$ 和 $j$ 有 $s_{i}=s_{j}$ 成立当且仅当 $t_{i}=t_{j}$ 成立, 那么我们称这两个数列是等价的. 若无穷数列 $\left\{r_{i}\right\}_{i \geq 1}$ 满足 $r_{1}, r_{2}, \cdots$ 和 $r_{k+1}, r_{k+2}, \cdots$ 等价, 那么我们称其具有等价周期 $k$. 假设有 $M$ 个具有等价周期 $k$ 的无穷数列, 每个数列的项都是集合 $\{1,2, \cdots, n\}$ 中的元素, 且它们两两都不是等价的, 求 $M$ 的最大可能值.
6. 在 $\triangle A B C$ 中, 点 $D 、 E 、 F$ 分别在边 $B C 、 C A 、 A B$ 上, 且满足四边形 $A F D E 、 B D E F 、 C E F D$ 都有内切圆. 证明: $\triangle A B C$ 的内切圆半径是 $\triangle D E F$内切圆半径的两倍.

## II . 解答与评注

1. 在 $\triangle A B C$ 中, 点 $P$ 和 $Q$ 分别在边 $A B$ 和 $A C$ 上,使得 $\triangle A P Q$ 的外接圆与 $B C$ 相切于点 $D$. 边 $B C$ 上的点 $E$ 满足 $B D=E C$. 直线 $D P$ 再次交 $\triangle C D Q$的外接圆于 $X$, 直线 $D Q$ 再次交 $\triangle B D P$ 的外接圆于点 $Y$. 证明: $D 、 E 、 X 、 Y$四点共圆。

证明 设 $B Y, C X$ 交于 $Z$. 则

$$
\angle D X C=\angle A Q D=\angle B P D \Rightarrow A B / / C Z .
$$

同理, $A C / / B Z$. 故 $A B Z C$ 为平行四边形.

$$
\begin{aligned}
& \text { 又 } \\
& \angle B D Y=\angle Q D C=\angle D A C, \angle D B Y=\angle A C D \Rightarrow \triangle D B Y \backsim \triangle A C D .
\end{aligned}
$$



故

$$
\begin{aligned}
\frac{D B}{A C}=\frac{B Y}{C D} & \Rightarrow D B \cdot D C=B Y \cdot A C \\
& \Rightarrow B E \cdot B D=B Y \cdot B Z \\
& \Rightarrow Y, Z, D, E \text { 共圆. }
\end{aligned}
$$

同理, $E, D, X, Z$ 共圆. 故 $E, D, X, Y$ 共圆.

评注 这是一道难度不大的几何题, 知识点非常基本.

2. 给定整数 $n>1$ 和 $a_{1}, a_{2}, \cdots, a_{n}$, 且对 $1 \leq i \leq n$ 都有 $a_{i}$ 满足 $n \mid a_{i}-i$.证明: 存在无穷序列 $b_{1}, b_{2}, \cdots$ 满足:

(1) $b_{k} \in\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$ 对任意正整数 $k$ 成立;

(2) $\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}$ 是一个整数.

证明 (刘翊哲) 我们证明: 对于任意给定的 $m \in \mathbb{Z}_{+}, m \geq 2$, 都一定存在序列 $b_{1}, b_{2}, \cdots \in\left\{a_{1}, \cdots, a_{n}\right\}$, 满足

$$
\left\|\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}\right\|<\frac{1}{n^{m-1}}
$$

其中, $\|x\|=\min \{x-\lfloor x\rfloor,\lceil x\rceil-x\}$ 为 $x$ 到与之最近的整数的距离.

我们在 $n$ 进制下看问题:

由题意, $a_{1}, \cdots, a_{n}$ 分别是末位为 $1,2, \cdots, n-1,0$ 的 $n$ 个整数 (把 $-1,-2, \cdots$ 的末位理解为 $n-1, n-2, \cdots)$, 设其中的位数最大者的位数为 $d$,先取 $b_{1}=b_{2}=\cdots=a_{n}$, 逐步调整:
由 $b_{m+d}=a_{n}$, 知此时 $\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}}$ 小数点后第 $(m+d)$ 位为 0 , 又设 $\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}}$ 小数点后第 $(m+d-1)$ 位为 $k_{m+d-1}$, 将 $b_{m+d-1}$ 调整为 $a_{n-k_{m+d-1}}$, 再设此时 $\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}}$小数点后第 $(m+d-2)$ 位为 $k_{m+d-2}$, 将 $b_{m+d-2}$ 调整为 $a_{n-k_{m+d-2}}$.

依此类推, 直至构造完 $b_{1}, b_{2}, \cdots, b_{m+d}$, 由构造方式知 $\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}}$ 的小数点后第 $(m+d),(m+d-1), \cdots, 1$ 位均为 0 .

又 $\left(\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}}\right) \cdot n^{m+d} \in \mathbb{Z}$, 故 $\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}}$ 的非 0 小数位只可能在小数点后前 $(m+d)$ 位, 故可得: $\sum_{k=1}^{m+d} \frac{b_{k}}{n^{k}} \in \mathbb{Z}$.

又因为

$$
\left|\sum_{k=m+d+1}^{\infty} \frac{b_{k}}{n^{k}}\right|<\sum_{k=m+d+1}^{\infty} \frac{n^{d+1}}{n^{k}}=\sum_{k=m}^{\infty} \frac{1}{n^{k}}=\frac{1}{n^{m-1}(n-1)} \leq \frac{1}{n^{m-1}}
$$

所以

$$
\left\|\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}\right\|=\left\|\sum_{k=m+d+1}^{\infty} \frac{1}{n^{k}}\right\|<\frac{1}{n^{m-1}}
$$

即知 $(*)$ 成立.

设对 $m \geq 2$, 前述构造得到的序列为 $B_{m}$.

由抽屉原理, 必有无穷多个 $B_{m}$ 的首项为 $a_{i_{1}}\left(i_{1} \in\{1,2, \cdots, n\}\right)$, 在首项为 $a_{i_{1}}$ 的所有 $B_{m}$ 中, 有无穷多个序列的第二项为 $a_{i_{2}}\left(i_{2} \in\{1,2, \cdots, n\}\right)$.

依此类推, 得到 $a_{i_{3}}, a_{i_{4}}, \cdots$, 满足对任意的正整数 $k$, 有无穷多个 $B_{m}$ 的前 $k$ 项为 $a_{i_{1}}, a_{i_{2}}, \cdots, a_{i_{k}}$, 又注意到, 若 $B_{m}$ 与 $B_{m}^{\prime}$ 的前 $k$ 项相同, 那么它们产生的 $\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}$ 之差的绝对值

$$
|\Delta|<\sum_{i=k+1}^{\infty} \frac{2 n^{d+1}}{n^{i}}=\frac{2}{n^{k-d-1}(n-1)} \leq \frac{2}{n^{k-d-1}}
$$

故 $B_{m}^{\prime}$ 产生的无穷级数 $\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}$ 到与其最近的整数的距离小于 $\frac{2}{n^{k-d-1}}+\frac{1}{n^{m-1}}$.

现取 $\left\{b_{n}\right\}: b_{t}=a_{i_{t}}\left(t \in \mathbb{Z}_{+}\right)$, 即知对任意固定的 $k \in \mathbb{Z}_{+}$, 存在无穷多个 $m \in \mathbb{Z}_{+}$满足:

$$
\left\|\sum_{i=1}^{\infty} \frac{b_{i}}{n^{i}}\right\|<\frac{2}{n^{k-d-1}}+\frac{1}{n^{m-1}}
$$

令 $k \rightarrow+\infty$, 结合 $m$ 的无限性, 即知 $\left\|\sum_{i=1}^{\infty} \frac{b_{i}}{n^{i}}\right\|=0$, 即 $\sum_{i=1}^{\infty} \frac{b_{i}}{n^{i}} \in \mathbb{Z}_{+}$, 证毕.

评注 前半部分论证利用 $n$ 进制从后往前的调整说明了 $\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}$ 可以任意接近一个整数; 后半部分则通过“找公共项”来构造 $\left\{b_{n}\right\}$, 使 $\sum_{k=1}^{\infty} \frac{b_{k}}{n^{k}}$ 等于 (无限接近于) 整数. 需要注意“任意小”和“无穷小”之间的区别.

3. 在 $100 \times 100$ 的网格中, 每个格子都被涂成了 101 种颜色中的一种. 若一个格子满足, 在它所在的行和列的 199 个格子中, 每种颜色都至少出现了一次,那么我们称这个格子是多元化的. 求多元化的格子数目的最大可能值.

解 (梁行健) 至多有 9996 个多元化的格子.

一方面, 在下图所示的染色方式中, 只有四个角上的格子不是多元化的, 故有 9996 个多元化的格子 (其中 $1,2, \cdots, 101$ 表示 101 种不同的颜色).



另一方面, 下证至多有 9996 个多元化的格子.

为了方便, 若一个格子不是多元化的, 我们称它为单一的, 只需证至少有 4 个单一的格子.

用反证法, 假设单一的格子至多 3 个, 则对于每种颜色, 这种颜色的格子不少于 99 个. 否则, 存在两行两列没有这种颜色的格子, 它们交出的 4 个方格都是单一的, 与反证假设矛盾.

又 $100^{2}=99 \times 101+1$, 故恰有一种颜色使得这种颜色的格子恰 100 个 ( 我们称这种颜色为大色), 对其余的 100 种颜色中的每种颜色, 恰有 99 个格子为这种颜色 (我们称另外 100 种颜色为小色 ).

注意到, 若对于一种小色 (不妨设为 1 色), 某行 $r$ 缺少 1 色的方格, 同时由 1 色为小色知, 存在一列 $c$ 缺少 1 色的方格, 故第 $r$ 行与第 $c$ 列相交的方格颜色是单一的, 则由单一的格子至多 3 个知, 至少有 97 行包含了全部 100 种小色的方格, 因而不包含大色的方格, 同理, 有 97 列不含大色的方格.
故至少有 $97^{2}=9409>3$ 个方格是单一的, 矛盾!

故单一的格子不少于 4 个, 即多元化的格子至多 9996 个.

综上所述, 答案为至多 9996 个.

评注 这是一道漂亮的方格表染色问题. 当 $n=1,2,3,4$ 时, 答案都是 $n^{2}-n$,因此最大值很容易被猜成 9900 , 而当 $n \geq 5$ 时, 答案却是 $n^{2}-4$. 只要正确地猜出答案, 就能较顺利的构造出最大值的例子, 剩下的证明部分也是自然的.

4. 将正整数集划分成 $n$ 个两两不交的无穷等差数列 $S_{1}, S_{2}, \cdots, S_{n}$, 它们的公差分别为 $d_{1}, d_{2}, \cdots, d_{n}$.

证明: 恰存在一个正整数 $i(1 \leq i \leq n)$ 使得 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \in S_{i}$.

证明 1 (张榕航) 首先, 我们来证明,

$$
\text { 对任意 } 1 \leq i \leq n \text {, 总有 } d_{i} \left\lvert\, \frac{1}{d_{i}} \cdot \prod_{j=1}^{n} d_{j}\right. \text {. }
$$

注意到, 对 $a_{s} \in S_{i}, b_{t} \in S_{j}(1 \leq i, j \leq n, i \neq j)$, 则

$$
\left(d_{i}, d_{j}\right) \nmid\left|a_{s}-b_{t}\right| .
$$

否则, 不妨设 $a_{s}>b_{t}$, 由 Bezout 定理, 存在 $x, y \in \mathbb{Z}_{+}$, 使 $y \cdot d_{j}-x \cdot d_{i}=\left|a_{s}-b_{t}\right|$,那么

$$
b_{t}+y \cdot d_{j}=b_{t}+x \cdot d_{i}+\left|a_{s}-b_{t}\right|=a_{s}+x \cdot d_{i}
$$

由于等式左边属于 $S_{j}$, 而等式右边属于 $S_{i}$, 故 $S_{i} \cap S_{j}=\varnothing$, 矛盾.

设 $d_{i}=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{r}^{\alpha_{r}}\left(p_{1}, p_{2}, \cdots, p_{r}\right.$ 为互异素数, $\left.\alpha_{1}, \alpha_{2}, \cdots, \alpha_{r} \in \mathbb{N}^{*}\right)$.设 $a$ 是数列 $S_{i}$ 中某项, 对任意的 $1 \leq u \leq r$, 我们有

$$
a<a+\frac{d_{i}}{p_{u}}<a+d_{i} \Rightarrow a+\frac{d_{i}}{p_{u}} \in S_{j}(j \neq i)
$$

于是

$$
\left.\left(d_{i}, d_{j}\right) \nmid \frac{d_{i}}{p_{u}} \Rightarrow p_{u}^{\alpha_{u}} \right\rvert\,\left(d_{i}, d_{j}\right) .
$$

即对任意的 $u, 1 \leq u \leq r$, 均存在 $j \neq i$ 使 $p_{u}^{\alpha_{u}} \mid d_{j}$, 故 $d_{i} \left\lvert\, \frac{1}{d_{i}} \cdot \prod_{j=1}^{n} d_{j}\right.$. 故 $(*)$ 得证.

再证明:

$$
\text { 存在唯一的 } 1 \leq i \leq n \text {, 使 } S_{i}=\left\{k d_{i} \mid k \in \mathbb{N}^{*}\right\} \text {. }
$$

由条件知存在唯一的 $i(1 \leq i \leq n)$ 使 $\prod_{j=1}^{n} d_{j} \in S_{i}$, 又因为 $d_{i} \mid \prod_{j=1}^{n} d_{j}$, 有 $S_{i} \subseteq\left\{k d_{i} \mid k \in \mathbb{N}^{*}\right\}$.

假设 $S_{i}$ 的首项不为 $d_{i}$, 不妨设其首项为 $k d_{i}\left(k \in \mathbb{N}^{*}, k>1\right)$, 则存在 $j \neq i$
使 $(k-1) d_{i} \in S_{j}$, 推出

$$
\left(d_{i}, d_{j}\right) \nmid\left|k d_{i}-(k-1) d_{i}\right|=d_{i},
$$

矛盾.

故假设不成立, 必有 $S_{i}=\left\{k d_{i} \mid k \in \mathbb{N}^{*}\right\}$.

故 $(* *)$ 得证.

结合 $(*)$ 及 $(* *)$, 知恰存在一个正整数 $i,(1 \leq i \leq n)$, 使 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \in S_{i}$, 原命题得证.

证明 2 (刘翊哲) 若 $a \notin S_{k}$, 则对任意正整数 $t$, 有 $a-t d_{k} \notin S_{k}$.

不妨设 $\prod_{j=1}^{n} d_{j} \in S_{1}$, 那么对 $i \in\{2,3, \cdots, n\}$, 有

$$
\prod_{j=1}^{n} d_{j}+\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \in S_{1}
$$

所以

$$
\prod_{j=1}^{n} d_{j}+\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \notin S_{i}
$$

从而

$$
\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \notin S_{i}
$$

由于 $\prod_{j=1}^{n} d_{j} \in S_{1}$, 所以

$$
\prod_{j=1}^{n} d_{j} \notin S_{i}(i \in\{2,3, \cdots, n\})
$$

进一步得到 $\frac{1}{d_{1}} \prod_{j=1}^{n} d_{j} \notin S_{i}$, 从而有 $\frac{1}{d_{1}} \prod_{j=1}^{n} d_{j} \in S_{1}$,

即知 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \in S_{i}$ 当且仅当 $\prod_{j=1}^{n} d_{j} \in S_{i}, i \in\{1,2, \cdots, n\}$, 故命题得证.

评注 在法一中注意到 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j}$ 是 $n-1$ 个公差的积, 再结合条件去刻画 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j}$ 的性质, 即 $(*)$ 式, 接着再证明 $(* *)$ 便顺利完成证明. 在法二中只需利用等差数列最基本的性质, 便可证明 $\frac{1}{d_{i}} \prod_{j=1}^{n} d_{j} \in S_{i} \Leftrightarrow \prod_{j=1}^{n} d_{j} \in S_{i}$, 即可完成证明.

5. 给定正整数 $n$ 和 $k$. 如果两个无穷数列 $\left\{s_{i}\right\}_{i \geq 1}$ 和 $\left\{t_{i}\right\}_{i \geq 1}$ 满足: 对任意正整数 $i$ 和 $j$ 有 $s_{i}=s_{j}$ 成立当且仅当 $t_{i}=t_{j}$ 成立, 那么我们称这两个数列是等价的. 若无穷数列 $\left\{r_{i}\right\}_{i \geq 1}$ 满足 $r_{1}, r_{2}, \cdots$ 和 $r_{k+1}, r_{k+2}, \cdots$ 等价, 那么我们称其具有等价周期 $k$. 假设有 $M$ 个具有等价周期 $k$ 的无穷数列, 每个数列的项都是集合 $\{1,2, \cdots, n\}$ 中的元素, 且它们两两都不是等价的, 求 $M$ 的最大可能值.
解 1 (刘鹏远) 答案: $M_{\max }=n^{k}$.

(1) 令 $f\left(a_{1}, a_{2}, \cdots, a_{k}\right)=\left\{s_{i}\right\}_{i=1}^{+\infty}$, 其中 $a_{1}, a_{2}, \cdots, a_{k} \in\{1,2, \cdots, n\}$,且满足: $\left\{s_{i}\right\}_{i=1}^{+\infty}$ 具有等价周期 $k$. 令 $C_{0}=0$, 对 $i=1,2, \cdots, k$, 进行以下操作:

(1) 当 $a_{i} \leq n-C_{i-1}$ 时, 令

$$
\begin{aligned}
s_{\left(t a_{i}+j-1\right) k+i} & =C_{i-1}+j\left(t \in \mathbb{N}, j \in\left\{1,2, \cdots, a_{i}\right\}\right), \\
C_{i} & =C_{i-1}+a_{i} .
\end{aligned}
$$

当 $i=1$ 时, 由 $a_{i} \leq n-C_{0}=n$, 故 $C_{1}=C_{0}+a_{1}=a_{1}$, 此时 $s_{t k+i}(t \in \mathbb{N})$ 取遍 $1,2, \cdots, C_{1}$.

当 $i \geq 2$ 时, 若 $s_{t k+j}(t \in \mathbb{N}, 1 \leq j \leq i-1)$ 取遍 $1,2, \cdots, C_{i-1}$, 由 $(*)$ 知 $s_{t k+i}(t \in \mathbb{N})$ 取遍 $C_{i-1}+1, C_{i-1}+2, \cdots, C_{i-1}+a_{i}=C_{i}$.

故 $s_{t k+j}(t \in \mathbb{N}, 1 \leq j \leq i)$ 取遍 $1,2, \cdots, C_{i}$.

(2) 当 $a_{i}>n-C_{i-1}$ 时, 令 $s_{i}=n+1-a_{i} \leq C_{i-1}, C_{i}=C_{i-1}$, 若 $s_{t k+j}(t \in$ $\mathbb{N}, 1 \leq j \leq i)\left(i \geq 2\right.$ 时) 取遍 $1,2, \cdots, C_{i-1}$, 则 $s_{i}$ 在 $s_{t k+j}(t \in \mathbb{N})(1 \leq j \leq$ $i-1)(i \geq 2$ 时) 中出现过.

不妨设 $s_{i}=s_{j}$, 则由 $\left\{s_{i}\right\}_{i=1}^{+\infty}$ 具有等价周期 $k$, 知

$$
s_{i}=s_{j} \Rightarrow s_{t k+i}=s_{t k+j}, t \in\left\{1,2, \cdots, C_{i}\right\}(t \in \mathbb{N})
$$

故 $s_{t k+j}(t \in \mathbb{N}, 1 \leq j \leq i)(i \geq 2$ 时 $)$ 取遍 $1,2, \cdots, C_{i}$.

(2) 此时 $f^{-1}\left(\left\{s_{i}\right\}_{i=1}^{+\infty}\right)=\left(a_{1}, a_{2}, \cdots, a_{k}\right)$ 满足对 $\left\{s_{i}\right\}_{i=1}^{+\infty}$ 具有等价周期 $k$,则有 $C_{0}=0$, 对 $i=1,2, \cdots, k$ :

(1) 若对任意的 $t \in \mathbb{N}, s_{t k+i}>C_{i-1}$, 令 $a_{i}$ 为 $\left\{s_{t k+i}\right\}_{t=0}^{+\infty}$ 的周期, $C_{i}=C_{i-1}+a_{i}$.

事实上, 由于对任意 $t \in \mathbb{N}, s_{t k+i} \in\{1,2, \cdots, n\}$, 且由抽屉原理知 $\left\{s_{t k+i}\right\}_{t=0}^{+\infty}$ 中必有两数相等.

故

$$
\begin{aligned}
s_{t_{1} k+i} & =s_{t_{2} k+i}\left(t_{1}, t_{2} \in \mathbb{N}, t_{1}<t_{2}\right) \\
\Rightarrow s_{t k+i} & =s_{\left(\left(t_{2}-t_{1}\right)+t\right) k+i}(t \in \mathbb{N})
\end{aligned}
$$

因此 $\left\{s_{t k+i}\right\}_{t=0}^{+\infty}$ 有周期.

由等价性, 不妨设 $s_{\left(t a_{i}+j\right) k+i}=C_{i-1+j}\left(t \in \mathbb{N}, j \in\left\{1,2, \cdots, a_{i}\right\}\right)$.

当 $i=1$ 时, $C_{1}=C_{0}+a_{1}=a_{1}, s_{t k+1}(t \in \mathbb{N})$ 取遍 $1,2, \cdots, a_{i}$, 即 $1,2, \cdots, C_{1}$.

对 $i \geq 2$, 若 $s_{t k+j}(1 \leq j \leq i-1, t \in \mathbb{N})$ 取遍 $1,2, \cdots, C_{i-1}$, 则由于 $s_{t k+i}$取遍 $C_{i-1}+1, \cdots, C_{i}$, 故 $s_{t k+j}(1 \leq j \leq i, t \in \mathbb{N})$ 取遍 $1,2, \cdots, C_{i}$.

(2) 若存在 $s_{i}, s_{k+i}, s_{2 k+i}, \cdots$ 中的数不大于 $C_{i-1}(i \geq 2), s_{t k+j}(t \in \mathbb{N}, 1 \leq$ $j \leq i-1)$ 取遍 $1,2, \cdots, C_{i}$.

设 $s_{t_{1} k+i}=s_{j}\left(t_{1} \in \mathbb{N}\right)$, 则由于 $\left\{s_{m}\right\}_{m=j(\bmod k)}^{m \geq 1}$ 为周期数列, 故数列中存在一项 $s_{j^{\prime}}$ 满足 $j^{\prime}>t_{1} k$, 且 $s_{t_{1} k+i}=s_{j^{\prime}}$, 故

$$
s_{i}=s_{j^{\prime}-t_{1} k}, s_{t k+i}=s_{j+\left(t-t_{1}\right) k}(t \in \mathbb{N}) .
$$

故 $s_{i}, s_{k+i}, s_{2 k+i}, \cdots$ 已被确定且为周期数列.

令 $a_{i}=n+1-s_{i}, C_{i}=C_{i-1}$, 则 $s_{t k+j}(t \in \mathbb{N})(1 \leq j \leq i)$ 取遍 $1,2, \cdots, C_{i}$.

综上所述, $f$ 为双射, 故 $M_{\text {max }}=n^{k}$.

解 2 (梁行健) $M_{\text {max }}=n^{k}$.

因为数列之间的等价是等价关系, 所以只需计算所有具有等价周期 $k$, 且所有项均取自集合 $\{1,2, \cdots, n\}$ 的无穷序列的等价类的个数.

注意到两个序列 $\left\{s_{n}\right\},\left\{t_{n}\right\}$ 等价当且仅当存在双射 $\sigma: \mathbb{R} \rightarrow \mathbb{R}$ 满足

$$
\sigma\left(s_{i}\right)=t_{i}, i \in \mathbb{Z}_{+}
$$

因此, 对于等价周期为 $k$ 的序列 $\left\{x_{n}\right\}$, 存在双射 $\sigma:\{1,2, \cdots, n\} \rightarrow\{1,2, \cdots, n\}$满足

$$
\sigma\left(x_{i}\right)=x_{k+i}, i \in \mathbb{Z}_{+}
$$

故对任意 $i \in \mathbb{Z}_{+}$, 我们有

$$
x_{k n+i}=\sigma^{(n)}\left(x_{i}\right)\left(i=1,2, \cdots, k, n \in \mathbb{Z}_{+}\right) \text {, }
$$

故序列 $\left\{x_{k}\right\}$ 由它的前 $k$ 项 $x_{1}, x_{2}, \cdots, x_{k}$ 和双射 $\sigma$ 唯一确定, 我们把 $\left\{x_{k}\right\}$ 称为由 $x_{1}, x_{2}, \cdots, x_{k}$ 和 $\sigma$ 生成的序列.

考虑任意一个具有等价周期 $k$ 的序列 $\left\{x_{n}\right\}$, 固定其前 $k$ 项 $x_{1}, x_{2}, \cdots, x_{k}$,设它们一共取到 $t$ 个不同的值. 由等价性, 不妨设它们是 $1,2, \cdots, t$, 且对于任意 $i=1,2, \cdots, t-1, i$ 第一次出现的位置在 $i+1$ 第一次出现的位置之前.

下面我们确定置换 $\sigma$ 的个数, 使得由前 $k$ 项 $x_{1}, x_{2}, \cdots, x_{k}$ 和 $\sigma$ 生成的这些序列 $\left\{x_{n}\right\}$ 互不等价.

设 $I=\{0,1, \cdots, t\}$, 定义映射 $\sigma_{I}: I \rightarrow I$, 对于任意 $i \in I$, 设 $n_{\sigma}(i)$ 是满足 $\sigma^{(j)}(i) \in I$ 的最小正整数 $j$. 令 $\sigma_{I}(i)=\sigma^{(j)}(i)$, 其中 $j=n_{\sigma}(i)$.

下证 $\sigma_{I}$ 为单射.

假设存在 $n_{\sigma^{\prime}}\left(x_{i}\right)=n_{\sigma}\left(x_{i}\right), i_{1}, i_{2} \in I, i_{1} \neq i_{2}$ 满足 $\sigma_{I}\left(i_{1}\right)=\sigma_{I}\left(i_{2}\right) \stackrel{\text { def }}{=} s$.

设 $j_{1}$ 和 $j_{2}$ 分别为满足 $\sigma^{\left(j_{1}\right)}\left(i_{1}\right) \in I$ 和 $\sigma^{\left(j_{2}\right)}\left(i_{2}\right) \in I$ 的最小正整数, 则
$\sigma^{\left(j_{1}\right)}\left(i_{1}\right)=\sigma^{\left(j_{2}\right)}\left(i_{2}\right)=s$, 故 $j_{1} \neq j_{2}$.

不妨设 $j_{1}<j_{2}$, 则有

$$
\sigma^{\left(j_{2}-j_{1}\right)}\left(i_{2}\right)=\left(\sigma^{-1}\right)^{\left(j_{1}\right)}\left(\sigma^{\left(j_{2}\right)}\left(i_{2}\right)\right)=\left(\sigma^{-1}\right)^{\left(j_{1}\right)} s=i_{1} \in I
$$

这与 $j_{2}$ 的最小性矛盾. 因此 $\sigma_{I}$ 为单射.

从而, 由 $I$ 为有限集知, $\sigma_{I}$ 为满射, 因此 $\sigma_{I}$ 为 $I$ 上的置换.

引理 设 $\sigma$ 和 $\sigma^{\prime}$ 为 $\{1,2, \cdots, n\}$ 上的两个置换, 则由 $x_{1}, x_{2}, \cdots, x_{k}$ 和 $\sigma$生成的序列 $\left\{x_{n}\right\}$ 与由 $x_{1}, \cdots, x_{k}$ 和 $\sigma^{\prime}$ 生成的序列 $\left\{x_{n}^{\prime}\right\}$ 等价当且仅当

(1) $\sigma_{I}=\sigma_{I}^{\prime}$

(2) 对于每个 $i \in I$ 均有 $n_{\sigma}(i)=n_{\sigma^{\prime}}(i)$.

证明 必要性. 设 $\{1,2, \cdots, n\}$ 上的置换 $\pi$ 满足: $\pi\left(x_{i}\right)=x_{i}^{\prime}$ 对任意正整数 $i$ 成立, 则对所有 $i \in I$, 有 $\pi(i)=i$, 故对所有 $i \notin I, \pi(i) \notin I$.

对 $1 \leq i \leq k$, 我们有 $x_{p k+i}=\sigma^{(p)}\left(x_{i}\right)$.

因此, 对 $p=1,2, \cdots, n_{\sigma}\left(x_{i}\right)-1$, 有

$$
x_{p k+i} \notin I \Rightarrow x_{p k+i}^{\prime}=\pi\left(x_{p k+i}\right) \notin I
$$

并且

$$
x_{k n_{\sigma}\left(x_{i}\right)+i} \in I \Rightarrow x_{k n_{\sigma}\left(x_{i}\right)+i}^{\prime}=\pi\left(x_{k n_{\sigma}\left(x_{i}\right)+i}\right) \in I \text {. }
$$

故由 $n_{\sigma}(i)$ 的定义知,

$$
n_{\sigma^{\prime}}\left(x_{i}\right)=n_{\sigma}\left(x_{i}\right) \stackrel{\text { def }}{=} j,
$$

而且

$$
\sigma_{I}^{\prime}\left(x_{i}\right)=\sigma^{\prime(j)}\left(x_{i}^{\prime}\right)=x_{k j+i}^{\prime}=\pi\left(x_{k j+i}\right)=\pi\left(\sigma^{(j)}\left(x_{i}\right)\right)=\pi\left(\sigma_{I}\left(x_{i}\right)\right)=\sigma_{I}\left(x_{i}\right) .
$$

故由 $i$ 的任意性知必要性得证.

充分性. 设 $\{1,2, \cdots, n\}$ 上的置换 $\pi$ 满足如下条件:

(1) $\pi(i)=i, i \in I$

(2) 对任意的 $i \in I$ 及 $1 \leq j<n_{\sigma}(i)$, 均有 $\pi\left(\sigma^{(j)}(i)\right)=\sigma^{\prime(j)}(i)$;

下证置换 $\pi$ 满足 $\pi\left(x_{i}\right)=x_{i}, i=1,2, \cdots$.

对 $i$ 归纳. $i=1,2, \cdots, k$ 时,显然成立.

假设小于 $i$ 时, 结论成立, 其中 $i \geq k+1$.

$1^{\circ}$ 若 $x_{i} \in I$, 分别取最小的正整数 $j_{1}, j_{2}<i$ 满足 $x_{i-k \cdot j_{1}}, x_{i-k \cdot j_{1}}^{\prime} \in I$, 注意到 $\pi(i) \in I$ 当且仅当 $i \in I$, 故 $j_{1}=j_{2}$, 因此由归纳假设知,

$$
\pi\left(x_{i-k \cdot j_{1}}\right)=x_{i-k \cdot j_{1}}^{\prime},
$$

故由 $x_{i-k \cdot j_{1}} \in I$ 知,

$$
x_{i-k \cdot j_{1}}=x_{i-k \cdot j_{1}}^{\prime}
$$

故

$$
n_{\sigma}\left(x_{i-k \cdot j_{1}}\right)=n_{\sigma}\left(x_{i-k \cdot j_{1}}^{\prime}\right),
$$

因此

$$
\pi\left(x_{i}\right)=x_{i}=\sigma_{I}\left(x_{i-k \cdot j_{1}}\right)=\sigma_{I}^{\prime}\left(x_{i-k \cdot j_{1}}^{\prime}\right)=x_{i}^{\prime} .
$$

$2^{\circ}$ 若 $x_{i} \notin I$, 同情形 1 知, 存在正整数 $j$, 满足 $x_{i-k \cdot j_{1}}=x_{i-k \cdot j_{1}}^{\prime} \in I$, 且对任意的 $1 \leq j_{1}<j$ 都有 $x_{i-k \cdot j_{1}}, x_{i-k \cdot j_{2}}^{\prime} \notin I$, 此时有

$$
j>n_{\sigma}\left(x_{i-k \cdot j_{1}}\right)=n_{\sigma^{\prime}}\left(x_{i-k \cdot j_{1}}^{\prime}\right) .
$$

故

$$
\pi\left(x_{i}\right)=\pi\left(\sigma^{(j)}\left(x_{i-k \cdot j_{1}}\right)\right)=\sigma^{\prime(j)}\left(x_{i-k \cdot j_{1}}^{\prime}\right)=x_{i}^{\prime}
$$

结论成立.

由归纳基本原理, 充分性得证, 故引理得证.

回到原题. 对于固定的 $x_{1}, \cdots, x_{k}$, 确定置换 $\sigma_{I}$ 的方法数为 $t !$, 确定 $n_{\sigma}(i)(i=1,2, \cdots, t)$ 的方法数为 $\left(\begin{array}{c}n \\ t\end{array}\right)$ ( 这里的方法数等于方程 $a_{1}+\cdots+$ $a_{t} \leq n-t$ 的非负整数解的个数), 设 $F(k, t)$ 是从集合 $\{1,2, \cdots, k\}$ 到集合 $\{1,2, \cdots, t\}$ 的满射个数, 则由引理知, 所求等价类个数为

$$
\sum_{t=1}^{k} \frac{F(k, t)}{t !} \cdot t !\left(\begin{array}{c}
n \\
t
\end{array}\right)=\sum_{t=1}^{k} F(k, t)\left(\begin{array}{c}
n \\
t
\end{array}\right)
$$

又在 $\{1,2, \cdots, k\}$ 到 $\{1,2, \cdots, n\}$ 的所有映射中, 值域为 $t$ 元集的映射恰有 $F(n, t)\left(\begin{array}{l}n \\ t\end{array}\right)$ 个, 故所求即为 $\{1,2, \cdots, k\}$ 到 $\{1,2, \cdots, n\}$ 的所有映射的个数, 而这显然为 $n^{k}$.

因此, 所求最大值为 $n^{k}$.

评注 本题是一道中等偏难的组合计数题, 关键在于真正理解并转化序列“等价”的定义, 利用双射重新叙述定义之后的想法是自然的, 在书写时对表述的要求较高.

6. 在 $\triangle A B C$ 中, 点 $D 、 E 、 F$ 分别在边 $B C 、 C A 、 A B$ 上, 且满足四边形 $A F D E 、 B D E F 、 C E F D$ 都有内切圆. 证明: $\triangle A B C$ 的内切圆半径是 $\triangle D E F$内切圆半径的两倍.
证明 (谢朋睿) 先证明一个引理.



引理 (蒙日定理) 平面上三个圆 $C_{1}, C_{2}, C_{3}$, 设 $C_{1}, C_{2} ; C_{2}, C_{3} ; C_{3}, C_{1}$ 的外位似中心分别是 $A, B, C$. 则 $A, B, C$ 三点共线.

证明 设圆 $C_{1}, C_{2}, C_{3}$ 的圆心为 $O_{1}, O_{2}, O_{3}$, 半径为 $r_{1}, r_{2}, r_{3}$, 由两圆位似的性质, 知 $O_{1}, O_{2}, A ; O_{2}, O_{3}, B ; O_{3}, O_{1}, C$ 分别三点共线, 且

$$
\frac{O_{1} A}{O_{2} A}=\frac{r_{1}}{r_{2}}, \frac{O_{2} B}{O_{3} B}=\frac{r_{2}}{r_{3}}, \frac{O_{3} C}{O_{1} C}=\frac{r_{3}}{r_{1}} \Rightarrow \frac{O_{1} A}{O_{2} A} \cdot \frac{O_{2} B}{O_{3} B} \cdot \frac{O_{3} C}{O_{1} C}=1
$$

对 $\triangle O_{1} O_{2} O_{3}$ 使用 Menelaus 定理的逆定理, 得 $A, B, C$ 三点共线, 引理获证.



回到原题.

作 $\triangle D^{\prime} E^{\prime} F^{\prime}$, 使得 $D, E, F$ 分别是 $E^{\prime} F^{\prime}, F^{\prime} D^{\prime}, D^{\prime} E^{\prime}$ 的中点.

由 $\triangle D E F \sim \triangle D^{\prime} E^{\prime} F^{\prime}$, 相似比为 $1: 2$, 知 $\triangle D^{\prime} E^{\prime} F^{\prime}$ 的内切圆半径是 $\triangle D E F$ 内切圆半径的 2 倍.

我们证明: $\triangle A B C$ 和 $\triangle D^{\prime} E^{\prime} F^{\prime}$ 有相同的内切圆.

因为四边形 $A F D E$ 有内切圆, 所以

$$
A F+D E=A E+D F
$$

$$
D^{\prime} F=D E, D F=D^{\prime} E
$$

故

$$
A F+D^{\prime} F=A E+D^{\prime} E
$$

进而四边形 $A E D^{\prime} F$ 有 $A$-旁切圆, 记为 $\omega_{a}$.

同理, 四边形 $B D E^{\prime} F, C E F^{\prime} D$ 分别有 $B-$ 旁切圆, $C-$ 旁切圆, 分别记为 $\omega_{b}, \omega_{c}$.

假设 $\triangle A B C$ 与 $\triangle D^{\prime} E^{\prime} F^{\prime}$ 的内切圆不同, 那么 $\omega_{a}, \omega_{b}, \omega_{c}$ 互不相同. 因为 $\omega_{b}, \omega_{c}$ 都与 $B C, E^{\prime} F^{\prime}$ 相切, 所以 $\omega_{b}, \omega_{c}$ 的外位似中心为 $B C \cap E^{\prime} F^{\prime}=D$.

同理, $\omega_{a}, \omega_{c} ; \omega_{a}, \omega_{b}$ 的外位似中心分别为 $A C \cap D^{\prime} F^{\prime}=E, A B \cap D^{\prime} E^{\prime}=F$.对 $\omega_{a}, \omega_{b}, \omega_{c}$ 使用引理, 得到 $D, E, F$ 三点共线, 矛盾!

因此 $\triangle A B C$ 和 $\triangle D^{\prime} E^{\prime} F^{\prime}$ 有相同的内切圆.

故 $r_{\triangle A B C}=r_{\triangle D^{\prime} E^{\prime} F^{\prime}}=2 r_{\triangle D E F}$ (这里 $r$ 表示内切圆半径), 原命题得证.

评注 这是一道难度较大的几何题, 计算方法基本行不通, 作图困难, 从而难以发现题目的关键: $\triangle A B C$ 和 $\triangle D^{\prime} E^{\prime} F^{\prime}$ 有相同的内切圆. 后面的反证与戴维斯定理的证明有异曲同工之妙.

