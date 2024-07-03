数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2020 年保加利亚 TST 试题解答与评析 

饶睿<br>(华南师范大学附属中学, 510630 )<br>指导教师: 陈嘉华

本次赛事的六道题里面, 第一题相对较简单, 而第二、四、五、六题属于中档题, 第三题则是较为困难的题目, 主要难在不容易表达.

## I. 试 题

1. 在锐角 $\triangle A B C$ 中, $B C>A C, \Gamma$ 是外接圆, $D$ 是 $A C$ 上一点, $E$ 是以 $C D$为直径的圆与 $\Gamma$ 的另一个交点. $M$ 是 $A B$ 的中点, $C M$ 交 $\Gamma$ 于另一点 $Q$. 与 $\Gamma$ 相切于 $A, B$ 两点的两条直线交于点 $P$, 而 $H$ 是 $P$ 在 $B Q$ 上的垂足. 点 $K$ 是 $H Q$上的一点, 满足 $Q$ 在 $H, K$ 之间. 证明: $\angle H K P=\angle A C E$ 当且仅当 $\frac{K Q}{Q H}=\frac{C D}{D A}$.
2. 设 $a, b$ 是两个正奇数. 证明: 对任意 $n \in \mathbb{N}$, 存在一个 $m \in \mathbb{N}$, 使得 $2^{n}$ 至少整除 $a^{m} b^{2}-1$ 和 $b^{m} a^{2}-1$ 中的一个数.
3. $\Omega$ 是一个由 $A=\{1,2, \cdots, 100\}$ 的一些子集组成的集族, 满足

(1) 任何一个 $A$ 的 99-元子集都在 $\Omega$ 中;

(2) 对任意一个非空集合 $C \in \Omega$, 都存在一个元素 $c \in C$ 使得 $C \backslash\{c\} \in \Omega$.

求 $|\Omega|$ 可能满足的最小值.

4. 甲在一张 $n \times n$ 的棋盘上依次摆放一些棋子, 规则如下：若一个格子是空的, 并且同行同列的剩下 $2 n-2$ 个格子中棋子的个数为偶数, 那么甲可以在这个格子中放一颗棋子. 在放了 $M$ 颗棋子之后, 甲发现他无法再放入任何棋子了,请问 $M$ 的最小可能值是多少?
5. 设函数 $f: \mathbb{R} \rightarrow \mathbb{R}$ 满足对任意 $x, y \in \mathbb{R}$ 都有

$$
|f(x+y)-f(x)-f(y)| \leq 1
$$

证明: 存在一个唯一的函数 $g: \mathbb{R} \rightarrow \mathbb{R}$ 满足对任意 $x$ 都有

$$
|g(x)-f(x)| \leq 1
$$

且对任意 $x, y \in \mathbb{R}$ 都有

$$
g(x+y)=g(x)+g(y) .
$$

6. 在 $\triangle A B C$ 中, $B C>A C, I_{B}$ 是 $B$-旁心, 过 $C$ 且平行于 $A B$ 的直线交 $B I_{B}$ 于 $F$. 点 $M$ 是 $A I_{B}$ 的中点, 而 $A$-旁切圆与直线 $A B$ 切于点 $D$. 点 $E$ 与点 $C$ 在同一侧, 且满足 $\angle B A C=\angle B D E, D E=B C$. 设 $Q$ 是 $E C, F M$ 的交点, $P$为 $E C, A B$ 的交点. 证明: $P, A, M, Q$ 共圆.

## II . 解答与评注

1. 在锐角 $\triangle A B C$ 中, $B C>A C, \Gamma$ 是外接圆, $D$ 是 $A C$ 上一点, $E$ 是以 $C D$为直径的圆与 $\Gamma$ 的另一个交点. $M$ 是 $A B$ 的中点, $C M$ 交 $\Gamma$ 于另一点 $Q$. 与 $\Gamma$ 相切于 $A, B$ 两点的两条直线交于点 $P$, 而 $H$ 是 $P$ 在 $B Q$ 上的垂足. 点 $K$ 是 $H Q$上的一点, 满足 $Q$ 在 $H, K$ 之间. 证明: $\angle H K P=\angle A C E$ 当且仅当 $\frac{K Q}{Q H}=\frac{C D}{D A}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_aad50db12aecd5b3e8a6g-02.jpg?height=685&width=514&top_left_y=1422&top_left_x=771)

证明 我们先证

$$
\angle H K P=\angle A C E \Rightarrow \frac{K Q}{Q H}=\frac{C D}{D A} .
$$

若已知 $\angle H K P=\angle A C E$. 作 $Q Z \perp P K$ 于 $Z$, 过 $P$ 作 $P Y / / A B$ 交 $C Q$ 于 $Y$, 则 $C, Q, M, Y$ 调和. 由 $P M \perp P Y$ 可得

$$
\angle C P M=\angle Q P M \Rightarrow \angle A P C=\angle B P Q
$$

因为 $\angle P B Q=\angle B C Q=\angle A C P$, 所以 $\triangle P A C \sim \triangle P Q B$. 故

$\angle A E C=\pi-\angle C B A=\angle C A P=\angle P Q B=\pi-\angle H Q P=\pi-\angle H Z P=\angle H Z K$,

因此 $\triangle H Z K \sim \triangle A E C$. 因为 $D E \perp E C, Q Z \perp Z K$, 所以 $Q$ 与 $D$ 为相似对称点.即

$$
\frac{K Q}{Q H}=\frac{C D}{D A}
$$

下面我们证明

$$
\frac{K Q}{Q H}=\frac{C D}{D A} \Rightarrow \angle H K P=\angle A C E
$$

若已知 $\frac{K Q}{Q H}=\frac{C D}{D A}$, 由于

$$
\angle P Q H=\angle A B C>\angle A C E \text {, }
$$

则 $H Q$ 的延长线上必存在点 $K^{\prime}$ 满足 $\angle H K^{\prime} P=\angle A C E$, 由前面的证明可得

$$
\frac{K^{\prime} Q}{Q H}=\frac{C D}{D A}
$$

即 $K^{\prime}$ 与 $K$ 为同一点.

评注 $\angle H K P=\angle A C E \Rightarrow \frac{K Q}{Q H}=\frac{C D}{D A}$ 的证明中, 比较容易找到相似三角形,而 $\frac{K Q}{Q H}=\frac{C D}{D A} \Rightarrow \angle H K P=\angle A C E$ 的证明则比较自然能够想到同一法.

2. 设 $a, b$ 是两个正奇数. 证明: 对任意 $n \in \mathbb{N}$, 存在一个 $m \in \mathbb{N}$, 使得 $2^{n}$ 至少整除 $a^{m} b^{2}-1$ 和 $b^{m} a^{2}-1$ 中的一个数.

证明 设 $\nu_{2}\left(a^{2}-1\right)=x, \nu_{2}\left(b^{2}-1\right)=y$, 不妨设 $x \leq y$. 下面证明: 对任意 $n \in \mathbb{N}$, 存在一个 $m \in \mathbb{N}$, 使得 $2^{n} \mid a^{2 m} b^{2}-1$.

因为

$$
a^{2^{n-x+1}}-1=\left(a^{2}-1\right)\left(a^{2}+1\right)\left(a^{4}+1\right)\left(a^{8}+1\right) \cdots\left(a^{2^{n-x}}+1\right),
$$

而当 $i \geq 1$ 时, $\nu_{2}\left(a^{2^{i}}+1\right)=1$, 且 $\nu_{2}\left(a^{2}-1\right)=x$. 所以有

$$
2^{n} \| a^{2^{n-x+1}}-1 .
$$

若正整数 $t$ 满足 $2^{n-x+1} \mid t$, 则有 $2^{n} \mid a^{t}-1$. 而若正整数 $t$ 满足 $2^{n} \mid a^{t}-1$. 假设 $u=\nu_{2}(t) \leq n-x$, 则

$$
2^{n} \mid a^{\left(2^{n-x+1}, t\right)}-1
$$

即 $2^{n} \mid a^{2^{u}}-1$, 这与 $2^{u+x-1}|| a^{2^{u}}-1$ 矛盾. 因此 $2^{n-x+1} \mid t$, 即

$$
2^{n}\left|a^{t}-1 \Leftrightarrow 2^{n-x+1}\right| t .
$$

所以 $a^{2}, a^{4}, a^{6}, \cdots, a^{2^{n-x+1}}$ 这 $2^{n-x}$ 个数模 $2^{n}$ 互不同余. 而

$$
a^{2 k} \equiv\left(a^{2}\right)^{k} \equiv 1\left[2^{x}\right]
$$

故它们必为

$$
1,2^{x}+1,2 \cdot 2^{x}+1,3 \cdot 2^{x}+1, \cdots,\left(2^{n-x}-1\right) 2^{x}+1
$$

的一个排列. 而由 $b^{2} \equiv 1\left[2^{x}\right]$ 可知 $\left(b^{2}\right)^{-1} \equiv 1\left[2^{x}\right]$, 这里 $\left(b^{2}\right)^{-1}$ 是 $b^{2}$ 模 $2^{n}$ 意义下的倒数. 所以存在 $k$, 使

$$
a^{2 k} \equiv\left(b^{2}\right)^{-1}\left[2^{n}\right]
$$

即

$$
2^{n} \mid a^{2 k} b^{2}-1
$$

评注 本题考察原根在 $p=2$ 时的推广, 了解原根这一个知识点的可以比较轻松地完成证明。
3. $\Omega$ 是一个由 $A=\{1,2, \cdots, 100\}$ 的一些子集组成的集族, 满足

(1) 任何一个 $A$ 的 99-元子集都在 $\Omega$ 中;

(2) 对任意一个非空集合 $C \in \Omega$, 都存在一个元素 $c \in C$ 使得 $C \backslash\{c\} \in \Omega$.

求 $|\Omega|$ 可能满足的最小值.

解 $|\Omega|$ 的最小值为 673 .

对每个符合条件的 $\Omega$, 构造一个对应的 $\Phi$, 满足对集合 $A$ 的任意子集 $S$, 都有 $S \in \Phi$ 当且仅当 $A \backslash S \in \Omega$, 此时 $\Phi$ 满足的性质为:

(1) $\{1\},\{2\}, \cdots,\{100\} \in \Phi$;

(2) 对任意 $S \in \Phi(S \neq A)$, 存在 $c \notin S(c \in A)$, 使 $\{c\} \cup S \in \Phi$.

此时等价于求 $|\Phi|$ 的最小值.

我们用 $f(x)$ 表示由 $\{1,2, \cdots, x\}$ 的一些子集组成且满足条件(1), (2)的集族的元素个数的最小值, 即求 $f(100)$.

我们先证明

$$
\left\{\begin{array}{l}
f(2 x+1) \leq f(x)+f(x+1)+2 x \\
f(2 x) \leq 2 f(x)+2 x-1
\end{array} .\right.
$$

先考虑集合 $\{1,2, \cdots, 2 x+1\}$, 将其分成两个集合

$$
\{1,2, \cdots, x\},\{x+1, x+2, \cdots, 2 x+1\} \text {. }
$$

对于每个集合可得到一个符合题意且元素个数最少的集族, 取这两个集族的并集, 再加入

$$
\{1,2, \cdots, i\}(i>x) \text { 和 }\{i, i+1, i+2, \cdots, 2 x+1\}(2 \leq i \leq x)
$$

这 $2 x$ 个集合,则得到一个对于 $\{1,2, \cdots, 2 x+1\}$ 的符合条件的集族. 所以有

$$
f(2 x+1) \leq f(x)+f(x+1)+2 x .
$$

再考虑 $\{1,2, \cdots, 2 x\}$, 将其分成两个集合

$$
\{1,2, \cdots, x\},\{x+1, x+2, \cdots, 2 x\}
$$

对于每个集合可得到一个符合题意且元素个数最少的集族, 取这两个集族的并集, 再加入

$$
\{1,2, \cdots, i\}(i>x) \text { 和 }\{i, i+1, i+2, \cdots, 2 x\}(2 \leq i \leq x)
$$

这 $2 x-1$ 个集合,则得到一个对于 $\{1,2, \cdots, 2 x\}$ 的符合条件的集族. 所以有

$$
f(2 x) \leq 2 f(x)+2 x-1
$$

因为 $f(1)=1, f(2)=3, f(3)=6$, 所以

$$
\begin{aligned}
& f(4) \leq 9, f(6) \leq 17, f(7) \leq 21, f(12) \leq 45, \\
& f(13) \leq 50, f(25) \leq 119, f(50) \leq 287, f(100) \leq 673
\end{aligned}
$$

当 $|\Phi|$ 取最小值时, 若记 $\Phi$ 中拥有 $i$ 个元素的集合有 $x_{i}$ 个,

$$
a_{i}=x_{i}-x_{i+1}\left(i=1,2, \cdots, 100, x_{101}=0\right) \text {, }
$$

则 $x_{1} \geq x_{2} \geq \cdots \geq x_{100}$, 否则 $|\Phi|$ 必定不取最小值.

下面证明

$i \cdot a_{100}+i \cdot a_{99}+\cdots+i \cdot a_{2 i-1}+(i-1) \cdot a_{2 i-2}+(i-2) \cdot a_{2 i-3}+\cdots+a_{i} \geq 100$对任意 $i \leq 50$ 均成立.

首先我们知道, 对任意 $G \in \Phi$, 存在 $H \in \Phi, h \in A \backslash H$, 使得 $G=H \cup\{h\}$, 否则可以将 $G$ 删去, 仍满足题意, 但不符合最小性. 我们考虑 $M \in \Phi,|M|=i+k$,且存在 $S, T \in \Phi$ 和 $s, t \in A, s \notin S, t \notin T$, 满足

$$
M=S \cup\{s\}=T \cup\{t\}
$$

则存在集合 $X, Y \in \Phi,|X|=|Y|=i$, 满足 $X \subseteq S$ 和 $Y \subseteq T$. 即 $S$ 是从 $M$ 中删去 $k$ 个元素而成, $T$ 是从 $M$ 中删去 $k$ 个元素而成, 则最多删掉了 $2 k$ 个元素, 故

$$
|X \cap Y| \geq \max \{0, i-k\} .
$$

对于固定的 $i$, 我们考虑所有上述的集合 $M \in \Phi$, 若存在 $S, T \in \Phi$ 和 $s, t \in$ $A, s \notin S, t \notin T$, 满足

$$
M=S \cup\{s\}=T \cup\{t\}
$$

则我们称 $S$ 和 $T$ 合并为 $M$. 从 $\Phi$ 中所有 $(i+k-1)$ 元集合到所有 $(i+k)$ 元集合的过程中, 经过了 $a_{i+k-1}$ 次合并, 每次合并我们可知至少有 $(i-k)$ 个重复元素. 而 $i x_{i}-100$ 表示 $\Phi$ 中所有 $i$ 元集合的元素的重复总次数, 所以有

$$
i x_{i}-100 \geq(i-1) a_{i}+(i-2) a_{i+1}+\cdots+a_{2 i-2} \text {. }
$$

考虑到 $x_{i}=a_{i}+a_{i+1}+\cdots+a_{100}$, 所以化简可得:

$i \cdot a_{100}+i \cdot a_{99}+\cdots+i \cdot a_{2 i-1}+(i-1) \cdot a_{2 i-2}+(i-2) \cdot a_{2 i-3}+\cdots+a_{i} \geq 100$在上式中分别取 $i=1,2,4,8,16,32$, 有

$$
\left\{\begin{array}{l}
a_{100}+a_{99}+\cdots+a_{1}=100 \\
2 a_{100}+2 a_{99}+\cdots+2 a_{3}+a_{2} \geq 100 \\
4 a_{100}+4 a_{99}+\cdots+4 a_{7}+3 a_{6}+2 a_{5}+a_{4} \geq 100 \\
8 a_{100}+8 a_{99}+\cdots+8 a_{15}+7 a_{14}+6 a_{13}+\cdots+a_{8} \geq 100 \\
16 a_{100}+16 a_{99}+\cdots+16 a_{15}+15 a_{30}+14 a_{29}+\cdots+a_{16} \geq 100 \\
32 a_{100}+32 a_{99}+\cdots+32 a_{15}+31 a_{62}+30 a_{61}+\cdots+a_{32} \geq 100
\end{array}\right.
$$

相加可得

$$
63 a_{100}+63 a_{99}+\cdots+63 a_{63}+62 a_{62}+61 a_{61}+\cdots+a_{1} \geq 600 .
$$

而 $a_{100}=1$, 若 $a_{99}=0$, 则 $x_{99}=1$. 不妨设 $\Phi$ 中唯一的一个 99 元集合为 $\{1,2, \cdots, 99\}$, 则任意一个 $\Phi$ 中的 98 元集合均不包含元素 100 . 如此类推可得 $\Phi$中任意一个元素个数小于 100 的集合均不包含元素 100 , 这与 $\{100\} \in \Phi$ 矛盾,所以 $a_{99} \geq 1$. 故

$$
37 a_{100}+36 a_{99}+\cdots+a_{64} \geq 37 a_{100}+36 a_{99} \geq 73 .
$$

(3)(4)相加, 可得

$$
100 a_{100}+99 a_{99}+\cdots+a_{1} \geq 673,
$$

即

$$
f(100)=x_{100}+x_{99}+\cdots+x_{1}=100 a_{100}+99 a_{99}+\cdots+a_{1} \geq 673 .
$$

综上可得, $f(100)=673$, 即 $|\Omega|$ 的最小可能值为 673 .
评注 这题的构造与证明都比较困难, 证明过程的表达也有一定难度, 而且很难仅通过其中一项来猜出答案, 是一道需要频繁进行尝试的题目。

4. 甲在一张 $n \times n$ 的棋盘上依次摆放一些棋子, 规则如下：若一个格子是空的, 并且同行同列的剩下 $2 n-2$ 个格子中棋子的个数为偶数, 那么甲可以在这个格子中放一颗棋子. 在放了 $M$ 颗棋子之后, 甲发现他无法再放入任何棋子了,请问 $M$ 的最小可能值是多少?

解 当 $n$ 为奇数时, $M$ 的最小值为 $\frac{n^{2}+1}{2}$; 当 $n$ 为偶数时, $M$ 的最小值为 $\frac{n^{2}+2 n}{2}$.

首先, 对于任意一个 $m \times m$ 的正方形, 可将其划分为 $m$ 组, 每组 $m$ 个格子,且同一组的格子均两两不同行不同列. 此时只需要依次放完每一组的格子即可将 $m \times m$ 的正方形填满. 所以构造如下:

当 $n=2 k+1$ 时, 可以按照上述方式将位于左上角的 $k \times k$ 正方形和右下角的 $(k+1) \times(k+1)$ 正方形填满, 此时无法继续放入更多棋子了, 此时 $M=\frac{n^{2}+1}{2}$.

当 $n=2 k$ 时, 我们先按照下面的顺序将第一行, 第一列和从左上到右下的对角线填满:

$$
\begin{aligned}
& (1,1) \rightarrow(2,2) \rightarrow(1,2) \rightarrow(2,1) \rightarrow(1,3) \rightarrow \\
& (3,1) \rightarrow(3,3) \rightarrow(4,4) \rightarrow(4,1) \rightarrow(1,4) \rightarrow \cdots
\end{aligned}
$$

接下来可以对右下角的 $(2 k-1) \times(2 k-1)$ 进行奇数情况的操作 (这时左上到右下的对角线已经放入棋子, 可按照奇数情况的方式继续操作). 此时 $M=\frac{n^{2}+2 n}{2}$.

我们先证明: 经过 $i$ 次操作后, 若记 $a_{i}$ 为有奇数个棋子的行数, $b_{i}$ 为有奇数个棋子的列数, 则 $a_{i}=b_{i}$.

对 $i$ 归纳, 当 $i=0$ 时显然成立.

设命题对 $i-1$ 成立, 现考虑第 $i$ 次操作. 若这次操作的格子所在行和所在列的棋子数均为奇数, 则有 $a_{i}=a_{i-1}-1, b_{i}=b_{i-1}-1$, 由归纳假设可得 $a_{i}=b_{i}$. 若这次操作的格子所在行和所在列的棋子数均为偶数, 则有 $a_{i}=a_{i-1}+1, b_{i}=b_{i-1}+1$, 由归纳假设可得 $a_{i}=b_{i}$.

下面我们称有奇数个棋子的行为 “奇行”, 有奇数个棋子的列为 “奇列”. 若某次操作后不能再放棋, 此时记 “奇行”和 “奇列” 的个数均为 $a$, 则 “偶行” 和 “偶列” 的个数均为 $n-a$. 此时每个 “奇行” 与每个 “奇列” 的公共格子上必有棋子, 否则可以继续再放棋. 同理, 每个“偶行”与每个“偶列”的公共格子上也必有棋子,
所以当 $n=2 k+1$ 时, 至少有 $a^{2}+(n-a)^{2}$ 个棋子. 而

$$
a^{2}+(n-a)^{2}=n^{2}+2 a(n-a) \geq n^{2}+2 k(k+1)=\frac{n^{2}+1}{2}
$$

当 $n=2 k$ 时, 由于每个“奇行”与每个“奇列”的公共格子上必有棋子, 所以“奇行”和“奇列”都至少有 $a$ 个棋子. 同理“偶行”和“偶列”都至少有 $n-a$ 个棋子.

(1) 若 $a$ 为偶数, 对于任意一个 “奇行”, 它至少有 $a+1$ 个棋子, 也就是说除了这个“奇行”与所有 $a$ 个“奇列”的 $a$ 个公共格子里之外, 还至少有 1 个格子里有棋子, 这个棋子必定在“奇行”和“偶列”的公共格子上. 同理, 对于任意一个“奇列”, 它至少有 $a+1$ 个棋子, 也就是说除了这个“奇列”与所有 $a$ 个“奇行”的 $a$个公共格子里之外, 还至少有 1 个格子里有棋子, 这个棋子必定在 “奇列”和“偶行”的公共格子上. 所以总数至少为

$$
\begin{aligned}
(n-a)^{2}+a^{2}+2 a & =n^{2}-2 a(n-a-1) \\
& \geq n^{2}-2 k(k-1)=\frac{n^{2}+2 n}{2} .
\end{aligned}
$$

(2) 若 $a$ 为奇数, 对于任意一个“偶行”, 它至少有 $n-a+1$ 个棋子, 也就是说除了这个“偶行”与所有 $n-a$ 个“偶列”的 $n-a$ 个公共格子里之外, 还至少有 1 个格子里有棋子, 这个棋子必定在 “偶行” 和 “奇列”的公共格子上. 同理, 对于任意一个“偶列”, 它至少有 $n-a+1$ 个棋子, 也就是说除了这个 “偶列” 与所有 $n-a$ 个 “奇行” 的 $n-a$ 个公共格子里之外, 还至少有 1 个格子里有棋子, 这个棋子必定在 “偶列” 和 “奇行” 的公共格子上. 所以总数至少为

$$
\begin{aligned}
(n-a)^{2}+a^{2}+2(n-a) & =n^{2}+2 n-2 a(n-a+1) \\
& \geq n^{2}+2 n-2 k(k+1) \\
& =\frac{n^{2}+2 n}{2} .
\end{aligned}
$$

综上所述, 当 $n$ 为奇数时, $M$ 的最小值为 $\frac{n^{2}+1}{2}$, 当 $n$ 为偶数时, $M$ 的最小值为 $\frac{n^{2}+2 n}{2}$.

评注 本题虽然构造比较容易，但是突破口其实在证明，关键在于对于行列棋子奇偶性的分析.

5. 设函数 $f: \mathbb{R} \rightarrow \mathbb{R}$ 满足对任意 $x, y \in \mathbb{R}$ 都有

$$
|f(x+y)-f(x)-f(y)| \leq 1 .
$$

证明: 存在一个唯一的函数 $g: \mathbb{R} \rightarrow \mathbb{R}$ 满足对任意 $x$ 都有

$$
|g(x)-f(x)| \leq 1
$$

且对任意 $x, y \in \mathbb{R}$ 都有

$$
g(x+y)=g(x)+g(y) .
$$

证明 对任意正整数 $n_{1}, n_{2}$, 有

$$
\begin{aligned}
n_{2} f\left(n_{1} x\right) & \leq\left(n_{2}-2\right) f\left(n_{1} x\right)+f\left(2 n_{1} x\right)+1 \\
& \leq\left(n_{2}-3\right) f\left(n_{1} x\right)+f\left(3 n_{1} x\right)+2 \\
& \ldots \\
& \leq f\left(n_{2} n_{1} x\right)+n_{2}-1 \\
& \leq f\left(n_{2} x\right)+f\left[\left(n_{1}-1\right) n_{2} x\right]+n_{2} \\
& \leq n_{1} f\left(n_{2} x\right)+n_{2}+n_{1}-2 \\
& <n_{1} f\left(n_{2} x\right)+n_{2}+n_{1} .
\end{aligned}
$$

所以

$$
\frac{f\left(n_{1} x\right)-1}{n_{1}}<\frac{f\left(n_{2} x\right)+1}{n_{2}}
$$

对任意正整数 $n_{1}, n_{2}$ 和任意实数 $x$ 成立.

考虑数列 $\left\{a_{n}\right\},\left\{b_{n}\right\}$ ，

$$
a_{n}=\frac{f(n x)-1}{n}, b_{n}=\frac{f(n x)+1}{n} .
$$

则存在 $A, B \in \mathbb{R}$, 使得 $a_{n} \leq A \leq B \leq b_{n}$. 又因为

$$
\lim _{n \rightarrow+\infty}\left(b_{n}-a_{n}\right)=0
$$

所以对任意 $\varepsilon>0$, 存在 $n_{0} \in \mathbb{N}$, 使得对任意 $n \geq n_{0}$, 都有 $\left|b_{n}-a_{n}\right|<\varepsilon$, 即

$$
\left(b_{n}-B\right)+(B-A)+\left(A-a_{n}\right)<\varepsilon
$$

因为 $b_{n}-B \geq 0, B-A \geq 0, A-a_{n} \geq 0$, 所以 $A=B$, 且 $\left|b_{n}-B\right|<\varepsilon,\left|a_{n}-A\right|<$ $\varepsilon$, 即

$$
\lim _{n \rightarrow+\infty} a_{n}=\lim _{n \rightarrow+\infty} b_{n}=A .
$$

又因为

$$
a_{n}<\frac{f(n x)}{n}<b_{n},
$$

所以对于 $n \in \mathbb{N}^{*}, \lim _{n \rightarrow+\infty} \frac{f(n x)}{n}$ 存在.

设

$$
g(x)=\lim _{n \rightarrow+\infty} \frac{f(n x)}{n}
$$

下面证明 $g(x)$ 符合题意. 考虑到

$$
\begin{aligned}
& \left|\frac{f(n x)}{n}-f(x)\right| \\
& =\frac{1}{n}|f(n x)-n f(x)| \\
& \leq \frac{1}{n}(|f(n x)-f[(n-1) x]-f(x)|+|f[(n-1) x]-(n-1) f(x)|) \\
& \leq \frac{1}{n}(1+|f[(n-1) x]-(n-1) f(x)|) \\
& \cdots \\
& \leq \frac{1}{n} \times n \\
& =1 .
\end{aligned}
$$

所以 $|g(x)-f(x)| \leq 1$. 而

$$
0 \leq\left|\frac{f(n x+n y)}{n}-\frac{f(n x)}{n}-\frac{f(n y)}{n}\right| \leq \frac{1}{n},
$$

所以

$$
\lim _{n \rightarrow+\infty}\left[\frac{f(n x+n y)}{n}-\frac{f(n x)}{n}-\frac{f(n y)}{n}\right]=0
$$

即

$$
g(x+y)=g(x)+g(y) .
$$

所以 $g(x)$ 符合题意.

下面证明唯一性. 假设函数 $h(x)$ 符合题意, 且存在 $x_{0} \in \mathbb{R}$ 使得 $h\left(x_{0}\right) \neq$ $g\left(x_{0}\right)$, 则存在 $k \in \mathbb{Z}$ 使得

$$
\left|k g\left(x_{0}\right)-k h\left(x_{0}\right)\right|>2 .
$$

则

$$
f\left(k x_{0}\right) \in\left[g\left(k x_{0}\right)-1, g\left(k x_{0}\right)+1\right] .
$$

又因为 $g\left(k x_{0}\right)=k g\left(x_{0}\right)$, 所以

$$
f\left(k x_{0}\right) \in\left[k g\left(x_{0}\right)-1, k g\left(x_{0}\right)+1\right] .
$$

同理

$$
f\left(k x_{0}\right) \in\left[k h\left(x_{0}\right)-1, k h\left(x_{0}\right)+1\right] .
$$

而 $\left|k g\left(x_{0}\right)-k h\left(x_{0}\right)\right|>2$, 所以

$$
\left[k g\left(x_{0}\right)-1, k g\left(x_{0}\right)+1\right] \cup\left[k h\left(x_{0}\right)-1, k h\left(x_{0}\right)+1\right]=\varnothing
$$

所以不存在这样的函数 $h(x)$, 即唯一性得证.
评注一定不要去试图解出 $f$, 先对 $g$ 的形式进行一定分析, 然后去利用 $g$ 的结构构造出 $g$, 再验证这个 $g$ 符合条件且唯一.

6. 在 $\triangle A B C$ 中, $B C>A C, I_{B}$ 是 $B$-旁心, 过 $C$ 且平行于 $A B$ 的直线交 $B I_{B}$ 于 $F$. 点 $M$ 是 $A I_{B}$ 的中点, 而 $A$-旁切圆与直线 $A B$ 切于点 $D$. 点 $E$ 与点 $C$ 在同一侧, 且满足 $\angle B A C=\angle B D E, D E=B C$. 设 $Q$ 是 $E C, F M$ 的交点, $P$为 $E C, A B$ 的交点. 证明: $P, A, M, Q$ 共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_aad50db12aecd5b3e8a6g-11.jpg?height=556&width=928&top_left_y=710&top_left_x=564)

证明 设 $I_{C}$ 是 $C$-旁心, $N$ 为 $I_{C} I$ 中点, 在 $N B$ 的延长线上取一点 $X$, 使

$$
\angle X I_{C} A=\angle B A C
$$

因为 $\triangle I_{C} B A \sim \triangle C I_{B} A$, 而

$$
\angle X I_{C} A=\angle B A C=\angle F C A, \angle X B A=\pi-\angle A B N=\pi-\angle A I_{B} B=\angle F I_{B} A,
$$

则 $I_{C} B A X \sim C I_{B} A F$. 设 $A B$ 中点为 $L$, 则 $L, M$ 为相似对应点, 所以

$$
\angle X L B=\angle F M I_{B} .
$$

而

$$
P, A, M, Q \text { 共圆 } \Leftrightarrow \angle F M I_{B}=\angle C P A \Leftrightarrow \angle X L B=\angle C P A \Leftrightarrow E C / / X L \text {. }
$$

即只需证 $E C / / X L$ 即可.

作平行四边形 $C E D Y$, 由 $B C=D E$ 得 $\triangle C B Y$ 为等腰三角形. 所以有

$$
\angle Y B C=\frac{\pi}{2}-\frac{\angle B C Y}{2} .
$$

设 $A B$ 与 $C Y$ 交于点 $G$, 则

$$
\angle B C Y=\angle C G A-\angle A B C=\angle E D A-\angle A B C=\angle B A C-\angle A B C .
$$

所以

$$
\angle Y B C=\frac{\pi}{2}-\frac{\angle B A C}{2}+\frac{\angle C B A}{2}=\angle C B A+\frac{\angle A C B}{2}=\angle N B C,
$$

即 $Y, B, N$ 共线.

设 $I_{C} I$ 与 $A B$ 交于 $Z, O$ 是 $\triangle X B I_{C}$ 的外心, 则 $O N \perp B I_{C}$, 即 $O N / / B I$. 所以

$$
\angle O B X=\frac{\pi}{2}-\angle B I_{C} X=\frac{\pi}{2}-\angle I_{B} C F=\frac{\pi}{2}-\frac{\angle B C Y}{2}=\angle C B Y
$$

即 $O, B, C$ 共线. 所以 $\triangle B O X \sim \triangle B C Y$, 则

$$
\frac{X B}{X Y}=\frac{O B}{O C}=\frac{N I}{N C}
$$

而

$$
D L=D B+B L=\frac{C B+C A-A B}{2}+\frac{A B}{2}=\frac{C B+C A}{2},
$$

所以

$$
\frac{B L}{D L}=\frac{A B}{C B+C A}=\frac{A Z}{A C}=\frac{N B}{N C}=\frac{N I}{N C}
$$

即

$$
\frac{X B}{X Y}=\frac{B L}{D L}
$$

故 $X L / / D Y / / E C$, 因此 $P, A, M, Q$ 共圆.

评注 直接去证明共圆无疑是很困难的, 但经过一个旋转相似对应后就可以消去很多飘在空中的点, 接下来的处理基本就是盯着图猜结论了, 导角复导边,导边复导角即可.

