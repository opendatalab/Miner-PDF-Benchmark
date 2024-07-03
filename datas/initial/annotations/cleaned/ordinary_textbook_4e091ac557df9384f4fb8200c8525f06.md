# 2022 年 IMO 预选题及其解答 

王正陈晨

(学而思教育集团, 100080)

每年, 世界各国会有大量的命题寄送到国际数学奥林匹克组委会, 组委会会选出里面比较不错的题目组成 LongList, 然后进一步篮选组成 ShortList, 最终经过领队投票, 从 ShortList 里选出六道题目作为当年的 IMO 考题. 这里的 ShortList 我们一般简称为 IMOSL, 也叫“IMO 预选题”, 会发给各国领队参考可以用于下一年的训练及选拔等. IMOSL一般题目优美, 新颖, 难度从低到高, 是数学竞赛爱好者不可多得的好资料, 非常适合作为参加 CMO, TST 前的练习.

本届 IMOSL 题目非常新颖, 除没有收录的 2022 年考题之外, 本文中代数部分 A5, 6, 7 都是偏组合构造背景的问题; 组合部分的最后几题反而都有偏代数的简洁做法; 数论最后一道题在中国属于非常常规的问题. 总的来说, 有很多新颖的题目例如 A5, C7, G7, N5, N6 颇能启发思维.

我们之前每年都会以学生为主, 教师为辅写 IMOSL 的解析, 考虑到联赛的时间, 今年的编撰工作由两位老师完成, 对文章中的错误和疏漏, 欢迎读者指正.

## I. 问 题

## 一、代数 (Algebra)

A1. 设 $\left(a_{n}\right)_{n \geq 1}$ 是一列满足以下条件的正实数:

$$
\left(a_{n+1}\right)^{2}+a_{n} a_{n+2} \leq a_{n}+a_{n+2}
$$

对于所有正整数 $n$ 成立. 证明: $a_{2022} \leq 1$.

A2. 设 $k \geq 2$ 是一个整数. 找到最小的整数 $n \geq k+1$, 使得存在一个由 $n$ 个不同实数构成的集合, 其中集合中的每个元素都可以表示为该集合中另外 $k$ 个不同元素的和.

修订日期: 2023-11-16.

A4. 设 $n \geq 3$ 是一个整数, $x_{1}, x_{2}, \ldots, x_{n}$ 是区间 $[0,1]$ 中的实数. 令 $s=$ $x_{1}+x_{2}+\ldots+x_{n}$, 且假设 $s \geq 3$. 证明存在整数 $i$ 和 $j$, 满足 $1 \leq i<j \leq n$, 使得

$$
2^{j-i} x_{i} x_{j}>2^{s-3}
$$

A5. 求所有满足以下条件的正整数 $n \geq 2$ : 存在 $n$ 个实数 $a_{1}<\cdots<a_{n}$ 和一个正实数 $r>0$, 使得对于 $1 \leq i<j \leq n, \frac{1}{2} n(n-1)$ 个差值 $a_{j}-a_{i}$ 在某种次序下等于 $r^{1}, r^{2}, \ldots, r^{\frac{1}{2} n(n-1)}$.

A6. 设 $\mathbb{R}$ 为实数集合. 定义 $\mathcal{F}$ 为所有满足下式的函数集合：对于任意 $x, y \in \mathbb{R}$,

$$
f(x+f(y))=f(x)+f(y) \text {. }
$$

找到所有有理数 $q$, 使得对于任意 $f \in \mathcal{F}$, 存在某个 $z \in \mathbb{R}$ 满足 $f(z)=q z$.

A7. 对于正整数 $n$, 记 $s(n)$ 为 $n$ 的各位数字之和. 设

$$
P(x)=x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}
$$

为一个多项式, 其中 $n \geq 2$ 且对于所有 $0 \leq i \leq n-1, a_{i}$ 都是正整数. 是否可能对于所有正整数 $k, s(k)$ 和 $s(P(k))$ 的奇偶性相同?

## 二、组合 (Combinatorics)

C1. 一个 $\pm 1$ - 序列是一个由 2022 个数字 $a_{1}, \ldots, a_{2022}$ 组成的序列, 每个数字都是 +1 或 -1 . 找到最大的 $C$, 使得对于任何 $\pm 1-$ 序列, 都存在一个整数 $k$ 和索引 $1 \leq t_{1}<\ldots<t_{k} \leq 2022$, 使得对所有 $i, t_{i+1}-t_{i} \leq 2$ 且

$$
\left|\sum_{i=1}^{k} a_{t_{i}}\right| \geq C
$$

C3. 在一个类似 $2022 \times 2022$ 的花园的每个方格中, 最初都有一个高度为 0 的树. 园丁和伐木工交替进行以下游戏, 园丁首先开始: 园丁选择花园中的一个方格. 该方格上的每棵树以及周围至多八个方格中的所有树都会增长一单位. 伐木工随后选择板上的四个不同方格. 这些方格上正高的树都会减少一单位. 称一棵树为雄伟的, 如果其高度至少为 $10^{6}$. 确定园丁能够确保板上最终有 $K$ 棵雄伟的树, 无论伐木工如何操作, 求最大的 $K$.

C4. 给定正整数 $n>3$. 假设有 $n$ 个孩子环绕成一个圆圈, 同时有 $n$ 个硬币分发在他们之间 (某些孩子可能没有硬币). 在每一步中, 有至少 2 个硬币的孩子可以将一个硬币分别给他们相邻的左右两边的孩子. 确定所有可能的初始硬币分
布, 使得经过有限次步骤后, 每个孩子都恰好有一个硬币.

C5. 设 $m, n \geq 2$ 为整数, $X$ 是一个有 $n$ 个元素的集合, $X_{1}, X_{2}, \ldots, X_{m}$ 是非空且不一定互不相交的 $X$ 的子集, 且两两不相等. 一个函数 $f: X \rightarrow$ $\{1,2, \ldots, n+1\}$ 称为美好函数, 如果存在一个指标 $k$ 使得

$$
\sum_{x \in X_{k}} f(x)>\sum_{x \in X_{i}} f(x)
$$

对于所有 $i \neq k$ 成立. 证明: 美好函数的数量至少为 $n^{n}$.

C6. 对于正整数 $n$, 我们从 $n$ 堆石子开始, 每堆最初都有一个石子. 可以进行以下形式的移动: 选择两堆, 从每堆中取相同数量的石子, 然后将这些石子合并成一堆. 找到 (关于 $n$ 的函数形式), 通过一系列这样的移动, 可以得到最少数量的非空堆.

C7. 露西开始时在黑板上写下 $s$ 个整数值的 $2022-$ 元组. 然后, 她可以选择两个 (不一定不同的) 她已经写下的元组 $\mathbf{v}=\left(v_{1}, \ldots, v_{2022}\right)$ 和 $\mathbf{w}=$ $\left(w_{1}, \ldots, w_{2022}\right)$, 并将这两个元组应用到以下操作之一中以获得一个新的元组:

$$
\begin{aligned}
& \mathbf{v}+\mathbf{w}=\left(v_{1}+w_{1}, \ldots, v_{2022}+w_{2022}\right) \\
& \mathbf{v} \vee \mathbf{w}=\left(\max \left(v_{1}, w_{1}\right), \ldots, \max \left(v_{2022}, w_{2022}\right)\right)
\end{aligned}
$$

然后, 她将这个元组写在黑板上.

事实证明, 通过这种方法, 露西可以在有限次步骤后在黑板上写下任何整数值的 2022-元组. 求露西初始写下的元组的最小可能数量 $s$.

C9. 设 $\mathbb{Z}_{\geq 0}$ 为非负整数的集合, $f: \mathbb{Z}_{\geq 0} \times \mathbb{Z}_{\geq 0} \rightarrow \mathbb{Z}_{\geq 0}$ 是一个双射, 满足当 $f\left(x_{1}, y_{1}\right)>f\left(x_{2}, y_{2}\right)$ 时, 有

$$
f\left(x_{1}+1, y_{1}\right)>f\left(x_{2}+1, y_{2}\right) \text { 和 } f\left(x_{1}, y_{1}+1\right)>f\left(x_{2}, y_{2}+1\right) \text {. }
$$

令 $N$ 为满足 $0 \leq x, y<100$ 且 $f(x, y)$ 为奇数的整数对 $(x, y)$ 的数量. 求 $N$ 的最小和最大可能值.

## 三、几何 (Geometry)

G2. 在锐角三角形 $A B C$ 内部一点 $P$ 满足 $A P \perp B C$. 过 $P$ 作 $A C$ 和 $A B$ 的平行线分别与 $B C$ 相交于 $D$ 和 $E$. 点 $X \neq A$ 在 $\triangle A B D$ 的外接圆上, 满足 $D A=D X$; 点 $Y \neq A$ 在 $\triangle A C E$ 外接圆上, 满足 $E A=E Y$. 求证: $B, C, X, Y$ 共圆.

G3. 设 $A B C D$ 是一个圆内接四边形. 假设点 $Q, A, B, P$ 在同一条直线上且按该顺序排列, 使得直线 $A C$ 与圆 $A D Q$ 相切, 直线 $B D$ 与圆 $B C P$ 相切. 设 $M$ 与 $N$ 分别为线段 $B C$ 和 $A D$ 的中点.

求证: 直线 $C D$, 过点 $A$ 的圆 $A N Q$ 的切线和过点 $B$ 的圆 $B M P$ 的切线共点.

G4. 设三角形 $A B C$ 是一个锐角三角形, 且 $A C>A B$. 设 $O$ 为其外心, 设 $D$ 为线段 $B C$ 上一点. 过 $D$ 且垂直于 $B C$ 的直线分别与直线 $A O, A C, A B$ 交于点 $W, X, Y$. 三角形 $A X Y$ 和 $A B C$ 的外接圆再次交于点 $Z \neq A$.

求证: 如果 $W \neq D$ 且 $O W=O D$, 则 $D Z$ 与圆 $A X Y$ 相切.

G5. 已知三角形 $A B C$ 和两平行线 $l_{1}, l_{2}$. 对 $i=1,2$, 直线 $l_{i}$ 分别交直线 $B C, C A, A B$ 于 $X_{i}, Y_{i}, Z_{i}$. 过 $X_{i}$ 作 $B C$ 的垂线, 过 $Y_{i}$ 作 $C A$ 的垂线, 过 $Z_{i}$ 作 $A B$ 的垂线交出 $\triangle_{i}$.

求证: 三角形 $\triangle_{1}$ 的外接圆和三角形 $\triangle_{2}$ 的外接圆相切

G6. 设三角形 $A B C$ 是一个锐角三角形. $A H$ 为三角形的高. 设 $P$ 是一个动点, 使得 $\angle P B C$ 和 $\angle P C B$ 的角平分线 $k$ 和 $l$ 交点在 $A H$ 上. 设 $k$ 与 $A C$ 交于 $E$, $l$ 与 $A B$ 交于 $F, E F$ 与 $A H$ 交于 $Q$.

求证: 当 $P$ 变化时, 直线 $P Q$ 经过一个定点.

G7. 两个三角形 $A B C, A^{\prime} B^{\prime} C^{\prime}$ 由同样的重心 $H$ 和同样的外接圆圆 $O$. 设由直线 $A A^{\prime}, B B^{\prime}, C C^{\prime}$ 构成的三角形为 $P Q R$.

求证: 三角形 $P Q R$ 的外接圆圆心在线段 $O H$ 上

G8. 设 $A A^{\prime} B B^{\prime} C C^{\prime}$ 是一个圆内接六边形, 其中 $A C$ 与三角形 $A^{\prime} B^{\prime} C^{\prime}$ 的内切圆相切. $A^{\prime} C^{\prime}$ 与三角形 $A B C$ 的内切圆相切. 设直线 $A B$ 与 $A^{\prime} B^{\prime}$ 交于 $X$, 直线 $B C$ 与 $B^{\prime} C^{\prime}$ 交于 $Y$.

求证: 若 $X B Y B^{\prime}$ 是凸四边形, 则它有内切圆.

## 四、数论 (Number Theory)

N1. 一个数被称为挪威数, 如果它有三个不同的正因子, 它们的和等于 2022 .确定最小的挪威数. (注意: 允许挪威数的正因子总数大于 3 .)

N2. 找出所有满足条件的正整数 $n>2$, 使得

$$
n ! \mid \prod_{p<q \leq n, p, q \text { 质数 }}(p+q) \text {. }
$$

N3. 设 $a>1$ 是一个正整数, $d>1$ 是一个与 $a$ 互质的正整数. 令 $x_{1}=1$, 对于 $k \geq 1$, 定义

$$
x_{k+1}= \begin{cases}x_{k}+d & \text { 如果 } a \text { 不能整除 } x_{k} \\ x_{k} / a & \text { 如果 } a \text { 能整除 } x_{k}\end{cases}
$$

以 $a$ 和 $d$ 为参数, 找出最大的正整数 $n$, 使得存在一个指数 $k$ 满足 $x_{k}$ 被 $a^{n}$ 整除.

N5. 对于每个 $1 \leq i \leq 9$ 和 $T \in \mathbb{N}$, 定义 $d_{i}(T)$ 为介于 1 和 $T$ 之间的所有 1829 的倍数在十进制下所有数字中数字 $i$ 出现的次数之和.

证明: 存在无穷多个 $T \in \mathbb{N}$, 使得 $d_{1}(T), d_{2}(T), \cdots, d_{9}(T)$ 中恰好有两个不同的值.

N6. $Q$ 是一组素数, 不一定有限. 对于正整数 $n$, 考虑它的素因子分解: 定义 $p(n)$ 为所有指数的和, $q(n)$ 为仅包含 $Q$ 中的素数对应的指数的和. 正整数 $n$ 被称为特殊数, 如果 $p(n)+p(n+1)$ 和 $q(n)+q(n+1)$ 都是偶数. 证明存在一个与集合 $Q$ 无关的常数 $c>0$, 使得对于任何大于 100 的正整数 $N$, 在区间 $[1, N]$ 内的特殊数至少有 $c N$ 个.

N8. 证明对于任何正整数 $n, 5^{n}-3^{n}$ 不能被 $2^{n}+65$ 整除.

## III. 解答与评注

## 一、代数 (Algebra)

A1. 设 $\left(a_{n}\right)_{n \geq 1}$ 是一列满足以下条件的正实数:

$$
\left(a_{n+1}\right)^{2}+a_{n} a_{n+2} \leq a_{n}+a_{n+2}
$$

对于所有正整数 $n$ 成立. 证明: $a_{2022} \leq 1$.

证明 记 $1-a_{n}=b_{n}$, 则有 $b_{n} \leq 1$, 而条件可以推出

$$
a_{n} a_{n+2}-a_{n}-a_{n+2}+1 \leq 1-a_{n+1}^{2},
$$

也即

$$
b_{n} b_{n+2} \leq b_{n+1}\left(2-b_{n+1}\right) \text {. }
$$

令 $n \rightarrow n+1$, 有

$$
b_{n+1} b_{n+3} \leq b_{n+2}\left(2-b_{n+2}\right) .
$$

由 $(*)(* *)$ 两式可得

$$
b_{n+1}\left(2-b_{n+1}-b_{n+3}\right)+b_{n+2}\left(2-b_{n}-b_{n+2}\right) \geq 0
$$

从而对任意正整数 $n, b_{n+1}, b_{n+2}$ 不同时小于 0 . 但由 $(*)$ 可以推出如果 $b_{n+1}<0$,那么 $b_{n}<0$ 或 $b_{n+2}<0$, 从而 $b_{n}$ 在第三项后都大于等于 0 , 也即 $a_{n} \geq 1$, 证毕.

评注 讨论与 1 的关系, 于是直接做差.

A2. 设 $k \geq 2$ 是一个整数. 找到最小的整数 $n \geq k+1$, 使得存在一个由 $n$ 个不同实数构成的集合, 其中集合中的每个元素都可以表示为该集合中另外 $k$ 个不同元素的和.

解 $n$ 的最小值是 $k+4$.

设这些数是 $a_{1}<a_{2}<\cdots<a_{n}, S=a_{1}+\cdots+a_{n}$.

一方面, $n=k+1$ 显然不成立. 若 $n=k+2$, 设 $a_{i}=S-a_{i}-a_{f(i)}$, 则

$$
2 a_{n}+a_{1} \leq 2 a_{n}+a_{f(n)}=S=2 a_{1}+a_{f(1)} \leq 2 a_{1}+a_{n}
$$

矛盾! 若 $n=k+3$, 设 $a_{i}=S-a_{f(i)}-a_{g(i)}$, 则

$$
2 a_{n}+2 a_{1} \leq 2 a_{n}+a_{f(n)}+a_{g(n)}=S=2 a_{1}+a_{f(1)}+a_{g(1)}<2 a_{n}+2 a_{1},
$$

矛盾!

另一方面, 容易验证当 $k=2 m$ 时,

$$
-m-2,-m-1,-m, \cdots,-1,1,2,3, \cdots, m
$$

满足要求; 当 $k=2 m+1$ 时,

$$
-m-2,-m-1,-m, \cdots,-1,0,1,2,3, \cdots, m
$$

满足要求. 证毕.

评注 典型的大小关系处理.

A4. 设 $n \geq 3$ 是一个整数, $x_{1}, x_{2}, \ldots, x_{n}$ 是区间 $[0,1]$ 中的实数. 令 $s=$ $x_{1}+x_{2}+\ldots+x_{n}$, 且假设 $s \geq 3$. 证明: 存在整数 $i$ 和 $j$, 满足 $1 \leq i<j \leq n$, 使得

$$
2^{j-i} x_{i} x_{j}>2^{s-3}
$$

证明 不妨设 $\max _{i<j}\left\{2^{j-i} x_{i} x_{j}\right\}=2^{b-a} x_{a} x_{b}(b>a)$. 则对任意 $i$, 有

$$
2^{b-i} x_{i} x_{b} \leq 2^{b-a} x_{a} x_{b}, \quad 2^{i-a} x_{i} x_{a} \leq 2^{b-a} x_{a} x_{b} .
$$

从而，

$$
\begin{aligned}
x_{a-1} & \leq \frac{x_{a}}{2}, x_{a-2} \leq \frac{x_{a}}{4}, \cdots, x_{a+1} \leq 2 x_{a}, x_{a+2} \leq 4 x_{a}, \cdots \\
x_{b+1} & \leq \frac{x_{b}}{2}, x_{b+2} \leq \frac{x_{b}}{4}, \cdots, x_{b-1} \leq 2 x_{b}, x_{b-2} \leq 4 x_{b}, \cdots
\end{aligned}
$$

设 $2^{\alpha} x_{a} \leq 1<2^{\alpha+1} x_{a}, 2^{\beta} x_{b} \leq 1<2^{\beta+1} x_{b}$, 若 $\alpha+\beta \geq b-a$, 则

$$
\begin{aligned}
S & \left.=\left(x_{1}+\cdots+x_{a+\alpha}\right)+\left(x_{a+\alpha+1}\right)+\cdots+x_{n}\right) \\
& <2^{\alpha} x_{a}\left(1+\frac{1}{2}+\cdots\right)+2^{\beta-1} x_{b}\left(1+\frac{1}{2}+\cdots\right) \\
& \leq 3
\end{aligned}
$$

矛盾！故 $\alpha+\beta \leq b-a-1$.

记 $A=2^{\alpha} x_{a}, B=2^{\beta} x_{b} \quad k=b-a-(\alpha+\beta)$, 则

$$
\begin{gathered}
x_{a+\alpha} \leq A, x_{a+\alpha-1} \leq \frac{A}{2}, \cdots ; \\
x_{b-\beta} \leq B, x_{b-\beta+1} \leq \frac{B}{2}, \cdots ; x_{i} \leq 1 .
\end{gathered}
$$

其中 $a+\alpha<i<b-\beta$. 进而,

$$
S<(k-1)+A\left(1+\frac{1}{2}+\cdots\right)+B\left(1+\frac{1}{2}+\cdots\right)=k+2 A+2 B-1 .
$$

而 $2^{b-a} x_{a} x_{b}=2^{k} A B$, 于是只要

$$
2^{k} A B \geq 2^{(k-1)+2 A+2 B-3} \Leftrightarrow A B \geq 4^{(A-1)+(B-1)}
$$

记 $f(A)=A-4^{A-1}$, 则 $f(1)=f\left(\frac{1}{2}\right)=0$, 且 $f$ 下凸, 故对于任意 $\frac{1}{2} \leq A, B \leq 1$, $A \geq 4^{A-1} \geq 0, B \geq 4^{B-1} \geq 0$, 即证.

评注 先假定最大值, 用最大值处理其他值化简式子, 注意到 $s \geq 3$ 意义即可.

A5. 求所有满足以下条件的正整数 $n \geq 2$ : 存在 $n$ 个实数 $a_{1}<\cdots<a_{n}$ 和一个正实数 $r>0$, 使得对于 $1 \leq i<j \leq n, \frac{1}{2} n(n-1)$ 个差值 $a_{j}-a_{i}$ 在某种次序下等于 $r^{1}, r^{2}, \ldots, r^{\frac{1}{2} n(n-1)}$.

解 所有 $n$ 为 $2,3,4$.

一方面, 当 $n=2$ 时, 取 0,1 ; 当 $n=3$ 时, 取 $0, r, r^{3}=r+r^{2}$, 其中 $r=\frac{\sqrt{5}+1}{2}$;当 $n=4$ 时, 取 $0, r, r^{4}=r+r^{3}, r^{6}=r^{4}+r^{3}=r^{5}+r$, 其中 $r$ 是 $r^{3}=r+1$ 的正根.

另一方面, 若 $n \geq 5$, 记 $m=\mathbf{C}_{n}^{2}$, 不妨设 $r>1$, 否则用 $\frac{a_{i}}{r^{m+1}}$ 代替 $a_{i}$. 记 $a_{j}-a_{i}=r^{t_{j, i}}$, 则存在 $j \geq i+2$ 使得 $t_{j, i} \leq n$, 此时

$$
r^{n} \geq r^{t_{j, i}}=a_{j}-a_{i}=\left(a_{j}-a_{i+1}\right)+\left(a_{i+1}-a_{i}\right) \geq r^{2}+r
$$

也即 $r^{n-1} \geq r+1$. 但 是, $r^{m}=a_{n}-a_{1}=\left(a_{n}-a_{2}\right)+\left(a_{2}-a_{1}\right)=\left(a_{n}-\right.$ $\left.a_{3}\right)+\left(a_{3}-a_{1}\right)=\cdots=\left(a_{n}-a_{n-1}\right)+\left(a_{n-1}-a_{1}\right)$, 这 $2 n-4$ 个差两两不同, 考察 $\max \left(t_{n, i}, t_{i, 1}\right)(1<i<n)$, 这 $n-2$ 个数中必有一个 $\leq m-(n-2)$, 从而
$r^{m} \leq r^{m-(n-2)}+r^{m-(n-1)}$, 也即 $r_{n-1} \leq r+1$.

从而, 上面不等式都取等并且 $r^{n-1}=r+1$. 此时, $t_{2,1}, t_{3,2}, \cdots, t_{n, n-1}$ 即为 $1,2,3, \cdots, n-1$, 于是

$$
\begin{aligned}
r^{m} & =r+r^{2}+\cdots+r^{n-1}=r^{3}+r^{4}+\cdots+r^{n} \\
& =r^{3}\left(r^{2}+r^{3}+\cdots+r^{n-1}\right) \\
& <r^{1+2}\left(r^{3}+r^{4}+\cdots+r^{n-1}\right) \\
& =r^{6}\left(r^{2}+r^{3}+\cdots+r^{n-1}\right) \\
& <r^{1+2+3}\left(r^{4}+r^{5}+\cdots+r^{n-1}\right) \\
& \quad \cdots \\
& <r^{1+2+\cdots+n}=r^{m} .
\end{aligned}
$$

矛盾!

评注 母函数不太有效; 分析大小就可以了.

A6. 设 $\mathbb{R}$ 为实数集合. 定义 $\mathcal{F}$ 为所有满足下式的函数集合：对于任意 $x, y \in \mathbb{R}$,

$$
f(x+f(y))=f(x)+f(y) .
$$

找到所有有理数 $q$, 使得对于任意 $f \in \mathcal{F}$, 存在某个 $z \in \mathbb{R}$ 满足 $f(z)=q z$.

证明 所有满足要求的有理数 $q$ 是 $1-\frac{1}{n}(n \in \mathbb{Z})$.

一方面, 取 $x=y=0$ 可以知道 $f(f(0))=2 f(0)$, 再取 $y=0$ 知 $f(x+f(0))=$ $f(x)+f(0)$, 进而 $f(k f(0))=(k+1) f(0), \forall k \in \mathbb{Z}$. 从而这样的 $q$ 满足要求.

另一方面, 对其他的 $q$, 我们来证明存在一个以 1 为周期, 取值为整数的 $f$ 不满足条件. 设 $q=\frac{b}{a}$, 若 $b=a$ 取 $f(x)=x+1$ 即可. 否则, 只需要对任意 $d \in[0,1)$ 构造 $f(d)$ 使得 $a f(d)-b d$ 不是 $b-a$ 的倍数 (这样就有 $f(c+d)=c+f(d) \neq \frac{b}{a}(c+d)$ ),因为 $b-a \neq 1,-1$, 这显然可以做到.

评注 构造需要一点想象力.

A7. 对于正整数 $n$, 记 $s(n)$ 为 $n$ 的各位数字之和. 设

$$
P(x)=x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}
$$

为一个多项式, 其中 $n \geq 2$ 且对于所有 $0 \leq i \leq n-1, a_{i}$ 都是正整数. 是否可能对于所有正整数 $k, s(k)$ 和 $s(P(k))$ 的奇偶性相同?
解 不可能.

假如存在, 则对于 $\forall x \in \mathbb{Z}$ 取 $B \in \mathbb{Z}^{+}$充分大, 有

$$
P\left(x+10^{B}\right)=P(x)+10^{B} P^{\prime}(x)+10^{2 B} \frac{P^{\prime \prime}(x)}{2 !}+\cdots .
$$

从而

$$
\begin{aligned}
S(x)+1 & \equiv S\left(x+10^{B}\right) \equiv S\left(P\left(x+10^{B}\right)\right) \\
& \equiv S(P(x))+S\left(P^{\prime}(x)\right)+\cdots \quad(\bmod 2)
\end{aligned}
$$

类似地降次可以得到存在 $a \neq 0, b \in \mathbb{Z}$ 使得 $S(a x+b)$ 对任意 $x \in \mathbb{Z}$ 奇偶性恒不变. 此时取 $x=10^{C}\left(10^{2 D}-1\right), x=x=10^{C}\left(10^{2 D-1}-1\right)$ 其中 $C, D$ 充分大,可以发现这两个数数字和差 9, 矛盾!

解 2 不妨设 $b>0$, 否则让 $b$ 平移若干个 $a$, 再不妨设 $a=s 10^{T},(s, 10)=1$ (因为可以把 $a$ 扩倍), 此时由于 $(s, 10)=1$, 可以给 $a$ 再扩若干倍使 $a$ 的末 2 位非 0 项为 “ 19 ”, 容易知道可以取 $x=10^{u}+10^{v}, u, v$ 充分大, 使 $10^{u} a$ 的最后非 0 位恰好与 $10^{v} a$ 首位重合, 此时

$$
S(a x+b) \equiv S(a)+S(a)+S(b)-9 \quad(\bmod 2)
$$

而取 $x=10^{u+1}+10^{v}$ 时它 $\equiv S(a)+S(a)+S(b)(\bmod 2)$, 矛盾!

评注 典型的对付各位数字和的手段, 要特别注意对不同的差分项, 最终算出来的式子是统一的.

## 二、组合 (Combinatorics)

C1. 一个 $\pm 1$ - 序列是一个由 2022 个数字 $a_{1}, \ldots, a_{2022}$ 组成的序列, 每个数字都是 +1 或 -1 . 找到最大的 $C$, 使得对于任何 $\pm 1-$ 序列, 都存在一个整数 $k$ 和索引 $1 \leq t_{1}<\ldots<t_{k} \leq 2022$, 使得对所有 $i, t_{i+1}-t_{i} \leq 2$ 且

$$
\left|\sum_{i=1}^{k} a_{t_{i}}\right| \geq C
$$

解 $C_{\max }=506$.

一方面, 取 $+1,+1,-1,-1,+1,+1,-1,-1, \cdots$, 易知 $c \leq 506$.

另一方面, 不妨设序列总和大于等于 0 , 则至少有 1011 个 +1 . 设该数列分布如下: $\left(c_{0}\right.$ 个 -1$), b_{1}$ 个 $+1, c_{1}$ 个 $-1, \cdots, b_{m}$ 个 $+1,\left(c_{m}\right.$ 个 -1$)$. 则我们取出所有 +1 , 以及每段 -1 的第偶数项, 容易知道满足要求, 并且 -1 的个数不超过 $\left[\frac{c_{1}}{2}\right]+\cdots+\left[\frac{c_{m}}{2}\right] \leq 505$, 从而这些项之和大于等于 506 . 证毕.
评注 分析正负号数目, 连续 -1 至少取一半.

C3. 在一个类似 $2022 \times 2022$ 的花园的每个方格中, 最初都有一个高度为 0 的树. 园丁和伐木工交替进行以下游戏, 园丁首先开始: 园丁选择花园中的一个方格. 该方格上的每棵树以及周围至多八个方格中的所有树都会增长一单位. 伐木工随后选择板上的四个不同方格. 这些方格上正高的树都会减少一单位. 称一棵树为雄伟的, 如果其高度至少为 $10^{6}$. 确定园丁能够确保板上最终有 $K$ 棵雄伟的树, 无论伐木工如何操作, 求最大的 $K$.

解 $K_{\max }=5 \times 674^{2}=2271380$.

一方面, 将花园划分为 $674^{2}$ 个 $3 \times 3$ 的区域. 园丁每一轮选择这 $674^{2}$ 个区域的中心格, 各操作一次. 在园丁操作 $M$ 轮后, 伐木工共砍掉了高度为 $4 \times 674^{2} \times M$ 的树. 设此时有 $B$ 颗树高度小于 $10^{6}$, 则

$$
4 \times 674^{2} \times M \geq B\left(M-10^{6}\right)
$$

当 $M$ 充分大时, 由上式得到 $B>4 \times 674^{2}-1$, 故 $B \geq 4 \times 674^{2}$, 因此园丁可保证最终有 $5 \times 674^{2}$ 颗雄伟的树.

另一方面将所有位于第 $3 i \pm 1$ 行且位于第 $3 j \pm 1$ 列处的格中的树染红, 共 $4 \times 674^{2}$ 颗红树. 园丁每次操作至多让 4 颗红树变高, 接下来令伐木工选择园丁刚变高的红树将其高度减少 1 , 这样, 所有红树的高度永远为 0 或 1 , 故至多 $5 \times 674^{2}$ 颗雄伟的树. 因此 $5 \times 674^{2}$ 为 $K$ 的最大可能值.

评注 $从 3 * 3$ 做起.

C4. 给定正整数 $n>3$. 假设有 $n$ 个孩子环绕成一个圆圈, 同时有 $n$ 个硬币分发在他们之间 (某些孩子可能没有硬币). 在每一步中, 有至少 2 个硬币的孩子可以将一个硬币分别给他们相邻的左右两边的孩子. 确定所有可能的初始硬币分布, 使得经过有限次步骤后, 每个孩子都恰好有一个硬币.

解 不妨设这 $n$ 个小孩的硬币数分别为 $a_{1}, a_{2}, \cdots, a_{n}$ 则显然 $a_{1}+2 a_{2}+\cdots+$ $n a_{n}$ 在模 $n$ 意义下不变, 也即 $\sum_{i=1}^{n} i\left(a_{i}-1\right) \equiv 0(\bmod n)$.

下面证明这个要求是充分的, 容易知道存在 $x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{N}^{+}$使得 $a_{i}-2 x_{i}+x_{i+1}+x_{i-1}=1$ (将 $x_{i+1}-x_{i}$ 换元解方程即可), 从而只需要证明可以对第 $\mathrm{i}$个小孩做 $x_{i}$ 次操作. 否则, 一直做操作直到不能做为止, 设还剩下 $y_{1}, y_{2}, \cdots, y_{n}$ 次操作. 容易知道若 $y_{i}$ 不全相等 (此时所有小孩恰 1 硬币已经做完), 可以取某个 $y_{i}$ 使得 $y_{i}$ 最大, 并且 $y_{i-1}, y_{i+1}$ 不都等于 $y_{i}$. 此时 $b_{i}=2 y_{i}-y_{i-1}-y_{i+1}+1>1$, 与
不能操作矛盾！

评注 很有意思的问题, 只要造出一个明确的目标, 然后逐步在合法条件下完成操作.

C5. 设 $m, n \geq 2$ 为整数, $X$ 是一个有 $n$ 个元素的集合, $X_{1}, X_{2}, \ldots, X_{m}$ 是非空且不一定互不相交的 $X$ 的子集, 且两两不相等. 一个函数 $f: X \rightarrow$ $\{1,2, \ldots, n+1\}$ 称为美好函数, 如果存在一个指标 $k$ 使得

$$
\sum_{x \in X_{k}} f(x)>\sum_{x \in X_{i}} f(x)
$$

对于所有 $i \neq k$ 成立. 证明: 美好函数的数量至少为 $n^{n}$.

证明 不妨设 $X_{i}$ 互不包含, 否则去掉被包含的集合. 任意取 $\{1,2, \cdots, n\} \rightarrow$ $\{1,2, \cdots, n\}$ 的映射 $g$, 设 $S_{i}=\sum_{x \in X_{i}} g(x)$. 任取 $S_{i}$ 中最大的一个, 并将 $X_{i}$ 中函数的 $g$ 值全部增加 1. 这样构造出 $n^{n}$ 个 $g^{\prime}$, 容易验证它们都满足要求, 并且由修改后的 $g^{\prime}$ 可以唯一确定原来的 $g$ (把最大的 $S_{i}$ 对应的集合的函数值全部 -1), 从而他们互不相同, 故得证！

评注 答案给我们以启示 (笑).

C6. 对于正整数 $n$, 我们从 $n$ 堆石子开始, 每堆最初都有一个石子. 可以进行以下形式的移动: 选择两堆, 从每堆中取相同数量的石子, 然后将这些石子合并成一堆. 找到 (关于 $n$ 的函数形式), 通过一系列这样的移动, 可以得到最少数量的非空堆。

解 当 $n$ 是 2 的幂的时候至少 1 堆, 证明和构造都是显然的.

当 $n$ 不是 2 的幂的时候我们断言最少两堆.

一方面, 设 $n=2^{x_{1}}+\cdots+2^{x_{k}}\left(x_{1}>x_{2}>\cdots>x_{k}\right)$, 则容易先把他变成 $\left(2^{x_{1}}, 2^{x_{2}}, \cdots, 2^{x_{k}}\right)$, 然后变成 $\left(2^{x_{1}}-2^{x_{k}}, 2^{x_{2}}, \cdots, 2^{x_{k}+1}\right)$, 之后每次对最后一堆 $2^{r}$ 个石子操作, 如果有另一堆 $2^{r}$ 个石子则取出变成一堆 $2^{r+1}$ 个, 否则在第一堆中取出 $2^{r}$ 个和他合成 $2^{r+1}$ 个. 容易知道这样操作最后得到两堆石子, 最后一堆 $2^{x_{2}+1}$ 个,以及第一堆 (显然第一堆不会用完).

另一方面, 来证明至少有两堆, 这是因为否则任取 $n$ 的一个奇质因子 $p$, 考虑第一次所有堆石子数都是 $p$ 的倍数的时刻, 注意到操作把 $(a, b) \rightarrow(a-c, b-c, 2 c)$,从而容易知道若 $p$ 整除后三个数, 则整除前两个数, 矛盾!

评注 从较小数开始猜答案.

C7. 露西开始时在黑板上写下 $s$ 个整数值的 $2022-$ 元组. 然后, 她可以选择两个 (不一定不同的) 她已经写下的元组 $\mathbf{v}=\left(v_{1}, \ldots, v_{2022}\right)$ 和 $\mathbf{w}=$ $\left(w_{1}, \ldots, w_{2022}\right)$, 并将这两个元组应用到以下操作之一中以获得一个新的元组:

$$
\begin{aligned}
& \mathbf{v}+\mathbf{w}=\left(v_{1}+w_{1}, \ldots, v_{2022}+w_{2022}\right) \\
& \mathbf{v} \vee \mathbf{w}=\left(\max \left(v_{1}, w_{1}\right), \ldots, \max \left(v_{2022}, w_{2022}\right)\right)
\end{aligned}
$$

然后，她将这个元组写在黑板上.

事实证明, 通过这种方法, 露西可以在有限次步骤后在黑板上写下任何整数值的 2022 -元组. 求露西初始写下的元组的最小可能数量 $s$.

## 解 答案是 3 .

先证明初始有 2 个元组时不行. 反正, 如果有初始元组符合提议, 设为

$$
\alpha=\left(a_{1}, a_{2}, \ldots, a_{2022}\right), \quad \beta=\left(b_{1}, b_{2}, \ldots, b_{2022}\right) \text {. }
$$

如果有 $i$ 使 $a_{i}, b_{i} \leq 0$, 则无论相加还是取最大值, 得到的值永远小于等于 0 ; 如果有 $i$ 使 $a_{i}, b_{i} \geq 0$, 相加或取最大值得到的值永远大于等于 0 . 故 $a_{i}$ 和 $b_{i}$ 异号且均非 0.

由抽屉原理, 存在 $a_{i}, a_{j}$ 同号, 易知可找到正实数 $k$ 使得

$$
\left\{\begin{array} { l } 
{ a _ { i } \geq k a _ { j } } \\
{ b _ { i } \geq k b _ { j } }
\end{array} \text { 或 } \left\{\begin{array}{l}
a_{j} \geq k a_{i} \\
b_{j} \geq k b_{i}
\end{array}\right.\right. \text {. }
$$

不妨是第一种情况, 则无论如何操作, 得到的数 $\left(c_{1}, c_{2}, \ldots, c_{2022}\right)$ 永远满足 $c_{i} \geq k c_{j}$, 故无法得到全体 2022 元整数组.

下面给出初始时 3 个元组的构造: 取

$$
\begin{aligned}
& \alpha=(-1,-1, \ldots,-1), \\
& \beta=(1,2, \ldots, n), \\
& \gamma=\left(-1^{2},-2^{2}, \ldots,-n^{2}\right) .
\end{aligned}
$$

易知对于正整数 $a, b, c$, 可通过求和操作得到

$$
(f(1), f(2), \ldots, f(n))
$$

其中 $f(n)=-a x^{2}+b x-c$.

对于 $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$, 取 $f_{i}(x)=-N_{i}(x-i)^{2}+a_{i}$, 其中 $N_{i}$ 足够大, 使得 $-N_{i} i^{2}+a_{i}<0$ 且 $N_{i}>\max _{i, j}\left|a_{i}-a_{j}\right|$, 易知

$$
f_{i}(i)=a_{i}, f_{i}(j)<a_{j}(i \neq j) .
$$

记 $v_{i}=\left(f_{i}(1), f_{i}(2), \ldots, f_{i}(n)\right)$, 对这些 $v_{i}$ 求有限次最大值可以得到

$$
v_{1} \vee v_{2} \vee \ldots \vee v_{n}=\left(a_{1}, a_{2}, \ldots, a_{n}\right)
$$

评注 构造中的 $\beta 、 \alpha$ 的分量实际上可换成任何单增、单减, 且非负的上凸函数在 $1,2, \ldots, n$ 处的取值.

C9. 设 $\mathbb{Z}_{\geq 0}$ 为非负整数的集合, $f: \mathbb{Z}_{\geq 0} \times \mathbb{Z}_{\geq 0} \rightarrow \mathbb{Z}_{\geq 0}$ 是一个双射, 满足当 $f\left(x_{1}, y_{1}\right)>f\left(x_{2}, y_{2}\right)$ 时, 有

$$
f\left(x_{1}+1, y_{1}\right)>f\left(x_{2}+1, y_{2}\right) \text { 和 } f\left(x_{1}, y_{1}+1\right)>f\left(x_{2}, y_{2}+1\right) \text {. }
$$

令 $N$ 为满足 $0 \leq x, y<100$ 且 $f(x, y)$ 为奇数的整数对 $(x, y)$ 的数量. 求 $N$ 的最小和最大可能值.

解 $N$ 的最小、最大值分别为 $2500 、 7500$.

显然当 $i, j \geq 0$ 时, $f(x+i, y+j)>f(x, y)$.

设 $a_{i}$ 为使得 $f\left(a_{i}, 0\right)<f(0, i)$ 的最大整数. 我们有 $j \leq a_{i}$ 时, $f(x+j, y)<$ $f(x, y+i)$; 当 $j \geq a_{i}+1$ 时, $f(x+j, y)>f(x, y+i)$.

设 $b_{i}$ 为使得 $f(i, 0)<f\left(0, b_{i}\right)$ 的最大整数. 我们有 $j \leq b_{i}$ 时, $f(x+i, y)<$ $f(x, y+j)$; 当 $j \geq b_{i}+1$ 时, $f(x+i, y)>f(x, y+j)$.

由此, 函数值小于等于 $f(x, y)$ 的点共有

$$
(x+1)(y+1)+\sum_{i=1}^{y} a_{i}+\sum_{j=1}^{x} b_{j}
$$

个, 故

$$
f(x, y)=(x+1)(y+1)+\sum_{i=1}^{y} a_{i}+\sum_{j=1}^{x} b_{j}-1
$$

考察 $f(x, y), f(x, y+1), f(x+1, y), f(x+1, y+1)$, 由于

$$
\begin{aligned}
& f(x, y)+f(x, y+1)+f(x+1, y)+f(x+1, y+1) \\
= & (2 x+3)(2 y+3)+2 \sum_{i=1}^{y} a_{i}+2 \sum_{j=1}^{x} b_{j}+2 a_{y+1}+2 b_{x+1}-4
\end{aligned}
$$

为奇数, 所以这 4 个数中至少一个奇数, 最多三个奇数. 故 $2500 \leq N \leq 7500$.

构造: 设 $\alpha$ 为无理数, 设 $x+y \alpha$ 为集合 $\{x+y \alpha \mid x, y \in \mathbb{N}\}$ 中第 $n_{x, y}$ 小的数,令 $f(x, y)=n_{x, y}-1$. 易知 $f$ 满足题目条件.

取 $\alpha=1000000+0.0000001 \sqrt{2}$, 易知当 $i \leq 100$ 时, $a_{i}=1000000 i$ 为偶数, $b_{i}=0$. 因此 $f(x, y) \equiv(x+1)(y+1)-1(\bmod 2)$, 所以此时 $N=7500$.

取 $\alpha=1000000-0.0000001 \sqrt{2}$, 与上面类似可知此时 $N=2500$.
评注 实际上可以证明, 当 $\alpha$ 取遍正无理数时, 上述构造中的 $f(x, y)=$ $n_{x, y}-1$ 覆盖了 $0 \leq x, y<100$ 时 $f(x, y)$ 所有可能的情况.

## 三、几何 (Geometry)

G2. 在锐角三角形 $A B C$ 内部一点 $P$ 满足 $A P \perp B C$. 过 $P$ 作 $A C$ 和 $A B$ 的平行线分别与 $B C$ 相交于 $D$ 和 $E$. 点 $X \neq A$ 在 $\triangle A B D$ 的外接圆上, 满足 $D A=D X$; 点 $Y \neq A$ 在 $\triangle A C E$ 外接圆上, 满足 $E A=E Y$. 求证: $B, C, X, Y$ 共圆.



证明 设 $\triangle A B D$ 和 $\triangle A C E$ 的外接圆分别为 $\Gamma_{1}, \Gamma_{2}$. 作 $A^{\prime}$ 为 $B X$ 和 $C Y$ 的交点, 则由 $\angle A^{\prime} B C=\overparen{X D}=\overparen{A X}=\angle A B D$.

同理, $\angle A C B=\angle A^{\prime} C B$, 所以 $A^{\prime}$ 是 $A$ 关于 $B C$ 的对称点,故 $A, P, A^{\prime}$ 三点共线.

设 $F=A A^{\prime} \cap B C$, 则

$$
\frac{B F}{E F}=\frac{A F}{P F}=\frac{C F}{D F}
$$

故 $B F \cdot F D=E F \cdot F C$.

所以 $A$ 和 $F$ 都在 $\Gamma 1$ 和 $\Gamma 2$ 的根轴上.

所以 $A F$ 为 $\Gamma 1$ 和 $\Gamma 2$ 的根轴, 故 $A^{\prime} F$ 在 $\Gamma 1$ 和 $\Gamma 2$ 的根轴上, 故

$$
A^{\prime} B \cdot A^{\prime} X=A^{\prime} C \cdot A^{\prime} Y
$$

综上, $B, X, C, Y$ 共圆, 证毕.

评注 $入$ 手点是 $D A=D X$ 等价于 $B D$ 平分 $\angle A B X$.

G3.设 $A B C D$ 是一个圆内接四边形. 假设点 $Q, A, B, P$ 在同一条直线上且按该顺序排列, 使得直线 $A C$ 与圆 $A D Q$ 相切, 直线 $B D$ 与圆 $B C P$ 相切. 设 $M$ 与 $N$ 分别为线段 $B C$ 和 $A D$ 的中点.

求证: 直线 $C D$, 过点 $A$ 的圆 $A N Q$ 的切线和过点 $B$ 的圆 $B M P$ 的切线共点.



证明 设 $X$ 是圆 $A N Q$ 在点 $A$ 处的切线和圆 $B M P$ 在点 $B$ 处的切线的交点.取 $B C$ 中点 $L$, 首先来证: $L A B X$ 四点共圆.

注意到 $\angle D Q A=\angle D A C=\angle D B C$, 且 $\angle D Q A=\angle D C B$. 所以 $\triangle A Q D \sim$ $\triangle C B D$, 同理 $\triangle B P C \sim \triangle D A C$

结合 $L$ 是 $B C$ 中点, $M$ 是 $B C$ 中点, $N$ 是 $A D$ 中点, 有

$$
\triangle A D L \sim \triangle P B M, \triangle B C L \sim \triangle Q A N .
$$

所以

$$
\begin{aligned}
\angle L A X & =\angle D A X-\angle D A L \\
& =\angle N Q A-\angle M P B \\
& =\angle C B L-\angle C B X \\
& =\angle X B L,
\end{aligned}
$$

即证 $L A B X$ 四点共圆.

接下来来证 $X$ 在 $C D$ 上.

由上述证明，

$$
\angle A L X=\angle X B P=\angle X B C+\angle C B P=\angle D A L+\angle A D C=\angle A L C \text {, }
$$

所以 $L, X, C$ 三点共线.

综上所述, $X$ 在 $C D$ 上. 证毕.

评注 思路是作出 $C D$ 中点后证明共圆, 该点可由做相似想到.

G4. 设三角形 $A B C$ 是一个锐角三角形, 且 $A C>A B$. 设 $O$ 为其外心, 设 $D$ 为线段 $B C$ 上一点. 过 $D$ 且垂直于 $B C$ 的直线分别与直线 $A O, A C, A B$ 交于点 $W, X, Y$. 三角形 $A X Y$ 和 $A B C$ 的外接圆再次交于点 $Z \neq A$.

求证: 如果 $W \neq D$ 且 $O W=O D$, 则 $D Z$ 与圆 $A X Y$ 相切.



证明 先证: $D O Z$ 三点共线.

由题意, 取 $H$ 为三角形 $A B C$ 的垂心, 那么 $A H=2 \cdot \operatorname{dis}(O, B C)=D W$, 又 $A H / / W D$, 所以平行四边形 $A W D H$,

$$
\angle D W O=\angle D O W=\angle H A O=\angle B-\angle C
$$

另外, $\angle D B Z=\angle Z A C=\angle Z A X=\angle Z Y D$, 所以 $B D Y Z$ 共圆, 所以,

$$
\angle A B Z=\angle B-\angle C .
$$

所以,

$$
\angle A O Z=2 \cdot(\angle B-\angle C)=2 \cdot \widehat{A Z}=\angle A O Z=\angle O D W+\angle O W D
$$

故 $D, O, Z$ 共线. 最后, $\angle B A O=\frac{\pi}{2}-\angle C=\angle C X D=\angle A X Y$, 所以 $O A$ 与圆 $A X Y$ 相切, 又因为 $O A=O Z$, 所以 $O Z$ 也和圆 $A X Y$ 相切, 证毕.
评注 实际上 $D$ 与 $A$ 关于 $B C$ 中垂线对称.

G5. 已知三角形 $A B C$ 和两平行线 $l_{1}, l_{2}$. 对 $i=1,2$, 直线 $l_{i}$ 分别交直线 $B C, C A, A B$ 于 $X_{i}, Y_{i}, Z_{i}$. 过 $X_{i}$ 作 $B C$ 的垂线, 过 $Y_{i}$ 作 $C A$ 的垂线, 过 $Z_{i}$ 作 $A B$ 的垂线交出 $\triangle_{i}$.

求证: 三角形 $\triangle_{1}$ 的外接圆和三角形 $\triangle_{2}$ 的外接圆相切



证明 如图所示, 设三角形 $\triangle_{1}$ 为 $\triangle D E F$, 三角形 $\triangle_{2}$ 为 $\triangle G H I$.

设 $A E$ 和 $G Z_{2}$ 交于 $H^{\prime}$, 则

$$
\frac{A E}{A H^{\prime}}=\frac{A Z_{1}}{A Z_{2}}=\frac{A Y_{1}}{A Y_{2}}
$$

所以 $E Y_{1} / / E Y_{2}$, 故 $H^{\prime}$ 与 $H$ 重合, 即 $A E H$ 三点共线, 同理 $B G F, C D I$ 分别三点共线.

设 $F G$ 与 $E H$ 交于点 $J$, 那么由于 $E F / / G H, I H / / D E, I G / / F D$, 同理知 $D I J$ 也共线.

另外, $\angle G H I=180^{\circ}-\angle Y_{2} H Z_{2}$, 同样对其他 $\triangle_{1}, \triangle_{2}$ 中的角导角, 知 $\triangle D E F \sim \triangle G I J \sim \triangle A B C$. 所以

$$
\angle I J H=180^{\circ}-\angle A J C=180^{\circ}-\angle A B C=\angle X_{2} B Z_{2}=180^{\circ}-\angle I G H,
$$

故 $J$ 在三角形 $G I H$ 的外接圆上, 同理也在 $D E F$ 的外接圆上.

最后来证 $J$ 是 $\triangle_{1}, \triangle_{2}$ 公共切点. 只用 $\overparen{J H}=\overparen{J E}$, 这由 $H G / / E F$ 知成立. 证毕.

评注用特殊点法可以找到位似中心, 即 $\triangle A B C$ 外接圆上到该三角形的西姆松线平行于 $l_{1}$ 的点.

G6. 设三角形 $A B C$ 是一个锐角三角形. $A H$ 为三角形的高. 设 $P$ 是一个动点, 使得 $\angle P B C$ 和 $\angle P C B$ 的角平分线 $k$ 和 $l$ 交点在 $A H$ 上. 设 $k$ 与 $A C$ 交于 $E$, $l$ 与 $A B$ 交于 $F, E F$ 与 $A H$ 交于 $Q$.

求证：当 $P$ 变化时, 直线 $P Q$ 经过一个定点.



证明 取点 $S$ 为使 $\angle A B S=180^{\circ}-2 \cdot \angle B, \angle A C S=180^{\circ}-2 \cdot \angle C$ 且 $S$ 与 $A$ 在 $B C$ 异侧. 那么 $A$ 为 $\triangle S B C$ 的旁心, 记 $\triangle S B C$ 旁切圆为 $\Gamma 1$.

由于 $H$ 为 $\triangle B P C$ 的 $B C$ 边上的内切圆切点, 所以

$$
B P-P C=B H-H C=B S-S C,
$$

故存在圆 $\Gamma 2$ 与 $B P, P C, C S, S B$ 均相切 (且切点不在线段上), 记 $\Gamma 3$ 为 $B P C$ 的内切圆圆 $D$ ( $D$ 是 $C F$ 与 $B E$ 的交点).

那么 $\Gamma 1, \Gamma 2, \Gamma 3$ 三个圆两两的外位似中心共线.

即 $P Q S$ 共线. 证毕.

评注 核心是猜到定点 $S$, 该点可通过特殊点法猜到: 设 $A^{\prime}$ 为 $A$ 关于 $B C$ 的对称点, 取 $D=A$ 和 $D=A^{\prime}$ 即可.

G7. 两个三角形 $A B C, A^{\prime} B^{\prime} C^{\prime}$ 由同样的重心 $H$ 和同样的外接圆圆 $O$. 设由直线 $A A^{\prime}, B B^{\prime}, C C^{\prime}$ 构成的三角形为 $P Q R$.

求证: 三角形 $P Q R$ 的外接圆圆心在线段 $O H$ 上.



证明 设

$$
\begin{gathered}
A H \cap B C=D, A H \cap B^{\prime} C^{\prime}=S, B C \cap A A^{\prime}=X, \\
A^{\prime} H \cap B^{\prime} C^{\prime}=D^{\prime}, A^{\prime} H \cap B C=S^{\prime}, B^{\prime} C^{\prime} \cap A A^{\prime}=Y .
\end{gathered}
$$

不难注意到 $\angle S D S^{\prime}=\angle S D^{\prime} S^{\prime}=90^{\circ} \Rightarrow D D^{\prime} S S^{\prime}$ 共圆,

$A H \cdot H D=A^{\prime} H \cdot H D^{\prime}=\frac{1}{2} \cdot \operatorname{Pow}(H$, 圆 $O) \Rightarrow A A^{\prime} D D^{\prime}$ 共圆.

综合以上两式知 $S S^{\prime} / / A A^{\prime}$, 所以 $S S^{\prime} / / X Y$ 且 $S S^{\prime} D D^{\prime}$ 共圆. 故 $D D^{\prime} X Y$ 共圆.

另外, 设 $D D^{\prime} \cap A A^{\prime}=K_{A}$, 那么

$$
K_{A} X \cdot K_{A} Y=K_{A} D \cdot K_{A} D^{\prime}=K_{A} A \cdot K_{A} A^{\prime}
$$

对于 $\Gamma 1=$ 圆 $O, \Gamma 2=B^{\prime} C^{\prime} \cup B C, \Gamma 3=B B^{\prime} \cup C C^{\prime}$. 使用笛沙格对合定理, 存在对合中心点 $K_{A}^{\prime}$.

由上述知必有 $K_{A}=K_{A}^{\prime}$, 同理定义的 $K_{B}, K_{C}$ 也到三圆等幂.

故三圆 $C_{1}=$ 圆 $O, C_{2}=$ 九点圆圆 $K$ (由于九点圆是外接圆关于垂心以 $\frac{1}{2}$ 位似得到, 故三角形 $A B C$ 与三角形 $A^{\prime} B^{\prime} C^{\prime}$ 有相同的九点圆), $C_{3}=P Q R$ 外接圆圆 $M$ 共轴.

综上, $O X M$ 共线, 即 $O H M$ 共线.证毕.

评注 此题的难度很大, 证明共轴的方法不唯一, 其中用笛沙格对合是比较简洁的一种方法。

G8. 设 $A A^{\prime} B B^{\prime} C C^{\prime}$ 是一个圆内接六边形, 其中 $A C$ 与三角形 $A^{\prime} B^{\prime} C^{\prime}$ 的内切圆相切. $A^{\prime} C^{\prime}$ 与三角形 $A B C$ 的内切圆相切. 设直线 $A B$ 与 $A^{\prime} B^{\prime}$ 交于 $X$, 直线 $B C$ 与 $B^{\prime} C^{\prime}$ 交于 $Y$.

求证: 若 $X B Y B^{\prime}$ 是凸四边形, 则它有内切圆.



证明 设 $M, N$ 分别是 $\widehat{A^{\prime} C^{\prime}}, \widehat{A C}$ 的中点.

先证 $M N / / I J$, 显然 $M J B^{\prime}, N I B$ 分别共线, 只用证 $I J B^{\prime} B$ 四点共圆.事实上, $B I$ 和 $I J$ 的夹角为

$$
\begin{aligned}
& 360^{\circ}-\frac{1}{2} \angle A B C-\frac{1}{2}\left\langle A^{\prime} C^{\prime}, A C\right\rangle-\left\langle A^{\prime} C^{\prime}, A B\right\rangle \\
= & 360^{\circ}-\frac{1}{2} \overparen{A C}-\frac{1}{2}\left(\widehat{A^{\prime} C}+\overparen{A C^{\prime}}\right)-\left(\widehat{A^{\prime} A}+\widehat{B C^{\prime}}\right) \\
= & 180^{\circ}-\frac{1}{2}\left(\widehat{B C^{\prime}}+\widehat{A^{\prime} B}\right)=180^{\circ}-\angle B B^{\prime} J .
\end{aligned}
$$

所以 $B I J B^{\prime}$ 共圆, $M N / / I J$, 设 $K=B^{\prime} M \cap B N, K$ 到 $A B, B Y$ 的距离记为 $x=r_{I} \cdot \frac{B K}{B I}, K$ 到 $A^{\prime} B^{\prime}, B^{\prime} Y$ 的距离记为 $y=r_{J} \cdot \frac{B^{\prime} K}{B^{\prime} J}$.

那么

$$
\frac{x}{y}=\frac{r_{I}}{r_{J}} \cdot \frac{B K}{B^{\prime} K} \cdot \frac{B^{\prime} J}{B I}=\frac{r_{I}}{r_{J}} \cdot \frac{M K}{N K} \cdot \frac{B^{\prime} J}{B I}=\frac{r_{I}}{r_{J}} \cdot \frac{M J}{N I} \cdot \frac{B^{\prime} J}{B I}=\frac{r_{I}}{r_{J}} \cdot \frac{2 R \cdot r_{J}}{2 R \cdot r_{I}}=1
$$

其中第三个等号用到了 $M N / / I J$, 第四个等号用到了欧拉公式的推导结论： $I$ 到圆 $O$ 的幂为 $2 R \cdot r_{I}$.

所以 $x=y$, 综上, 以 $K$ 为圆心, $x$ 为半径的圆是 $X B Y B^{\prime}$ 的内切圆. 证毕.

评注 此题也可作出 $\odot I$ 和 $\odot J$ 的外位似中心 $T$, 可以证明 $T, B, B^{\prime}$ 共线.

## 四、数论 (Number Theory)

N1. 一个数被称为挪威数, 如果它有三个不同的正因子, 它们的和等于 2022 .确定最小的挪威数。(注意: 允许挪威数的正因子总数大于 3.)

解 最小的挪威数为 1344 .

一方面, $1344+672+6=2022$, 故 1344 满足要求.

另一方面, 设好数为 $n$, 因数为 $\frac{n}{a}, \frac{n}{b}, \frac{n}{c}(a<b<c)$.
若 $a \geq 2$, 则 $b \geq 3, c \geq 4$, 从而

$$
2022 \geq \frac{n}{2}+\frac{n}{3}+\frac{n}{4} \Rightarrow n \geq \frac{12}{13} \cdot 2022>1344
$$

若 $a=1, b \geq 4$, 则 $c \geq 5$, 类似地, $n>\frac{3}{2} \cdot 2022>1344$.

若 $a=1, b=3$, 当 $c=4,5$ 时可以知道无解, 从而 $c \geq 6$, 同样的, $n>$ $\frac{3}{2} \cdot 2022>1344$.

若 $a=1, b=2$, 则 $n=\frac{2022}{\frac{1}{1}+\frac{1}{2}+\frac{1}{c}}=\frac{4044 c}{3 c+2}$, 而 $(3 c+2, c)=1$, 故 $3 c+2 \mid 4044$, 进而 $3 c+2=674$, 此时可以得到 $n=1344$.

综上, $n_{\min }=1344$.

评注 常规的大小估计问题, 讨论清楚即可.

N2. 找出所有满足条件的正整数 $n>2$, 使得

$$
n ! \mid \prod_{p<q \leq n, p, q \text { 质数 }}(p+q) \text {. }
$$

解 计算易知当 $n<17$ 时只有 1,7 满足要求.

当 $n \geq 17$, 设 $p_{0}$ 是不超过 $n$ 的最大质数.

(1) 若 $p_{0}-2$ 不是质数, 则 $\forall p<q \leq n, p+q \neq p_{0}$ 且 $p+q<2 p_{0}$, 从而 $\left(p+q, p_{0}\right)=1$, 矛盾!

(2) 若 $p_{0}-2$ 是质数, 则 $p_{0}-4$ 不是质数, 从而 $\forall p<q \leq n$ 若 $p, q$ 中有 $p_{0}-2$, 则 $\left(p+q, p_{0}-2\right)=1$, 若没有, 则 $p+q \neq p_{0}-2$ 且 $p+q<2\left(p_{0}-2\right)$, 从而 $\left(p+q, p_{0}-2\right)=1$ 也成立. 所以, $\left(\prod(p+q), p_{0}-2\right)=1$, 矛盾!

评注 核心是发现需要 $p \mid \prod_{p<q \leq n, p, q \text { 质数 }}(p+q)$.

N3. 设 $a>1$ 是一个正整数, $d>1$ 是一个与 $a$ 互质的正整数. 令 $x_{1}=1$, 对于 $k \geq 1$, 定义

$$
x_{k+1}= \begin{cases}x_{k}+d, & \text { 如果 } a \text { 不能整除 } x_{k} \\ x_{k} / a, & \text { 如果 } a \text { 能整除 } x_{k}\end{cases}
$$

以 $a$ 和 $d$ 为参数, 找出最大的正整数 $n$, 使得存在一个指数 $k$ 满足 $x_{k}$ 被 $a^{n}$ 整除.

解 首先证明 $x_{k}<a d$ 对任意 $k$ 成立. 用归纳, 奠基显然, 若 $x_{k}<a d(k<m)$,则设 $t$ 为 1 到 $k-1$ 中最大的使 $x_{t}=\frac{x_{t-1}}{a}$ 的数 (若没有, 定义 $t=1$ ), 则由归纳假设易知 $x_{t}<d$, 而注意到 $x_{t}, x_{t}+d, \cdots, x_{t}+(a-1) d$ 中必有 $a$ 的倍数, 所以 $k \leq t+(a-1)$, 也即 $x_{k} \leq x_{t}+(a-1) d<a d$.
从而, $n \leq\left\lceil\log _{a} d\right\rceil$. 但是注意到该数列可以逆推, 也即 $x_{k}$ 可推出 $x_{k-1}$ (若 $x_{k}<d$, 则 $x_{k-1}=a x_{k}$, 否则 $\left.x_{k-1}=x_{k}-d\right)$, 从而该数列是纯周期的. 从而, 从 1 开始逆推可以知道 $a^{\left\lceil\log _{a} d\right\rceil}$ 在数列中, 故 $n$ 的最大值是 $\left\lceil\log _{a} d\right\rceil$.

评注 入手时可以先尝试较小的例子, 找到规律.

N5. 对于每个 $1 \leq i \leq 9$ 和 $T \in \mathbb{N}$, 定义 $d_{i}(T)$ 为介于 1 和 $T$ 之间的所有 1829 的倍数在十进制下所有数字中数字 $i$ 出现的次数之和.

证明: 存在无穷多个 $T \in \mathbb{N}$, 使得 $d_{1}(T), d_{2}(T), \cdots, d_{9}(T)$ 中恰好有两个不同的值.

证明 设 $m=k \varphi(1829)\left(k \in \mathbb{Z}^{+}\right)$, 我们来证明 $10^{m}-1$ 满足要求.

首先, 断言 1 到 9 的每个数码在 1 到 $\mathrm{T}$ 间 1829 的倍数中每位出现的次数都一样, 这是因为

$1829\left|\overline{a_{m} a_{m-1} \cdots a_{1}} \Leftrightarrow 1829\right| \overline{a_{m} a_{m-1} \cdots a_{2} a_{1} 0} \Leftrightarrow 1829 \mid \overline{a_{m-1} a_{m-2} \cdots a_{1} a_{m}}$.

从而由 $(*)$, 我们只需要证明每个数在末位出现的次数恰有两种, 注意到 1829 的倍数的末位以 10 为周期循环且每个数码恰好在循环中各出现一次, 从而这是显然的 (1829 和 $10^{m}-1$ 末位都为 9 , 所以不会每个数码出现次数全都一样), 证毕!

评注 核心是发现 $(*)$ 式 (可以从 1829 的整除规律中得到思路, 因为必然要涉及到怎么刻画一个很大的数被 1829 整除, 而经典的方法就是 $\varphi(1829)$ 位一段,然后求和), 后面的证明中考虑首位或者末位均可, 最后要记得说明不可能 $d_{1}(T)$, $d_{2}(T), \cdots, d_{9}(T)$ 全相等.

N6. $Q$ 是一组素数, 不一定有限. 对于正整数 $n$, 考虑它的素因子分解: 定义 $p(n)$ 为所有指数的和, $q(n)$ 为仅包含 $Q$ 中的素数对应的指数的和. 正整数 $n$ 被称为特殊数, 如果 $p(n)+p(n+1)$ 和 $q(n)+q(n+1)$ 都是偶数. 证明存在一个与集合 $Q$ 无关的常数 $c>0$, 使得对于任何大于 100 的正整数 $N$, 在区间 $[1, N]$ 内的特殊数至少有 $c N$ 个.

证明 考虑 $72 k, 72 k+6,72 k+8,72 k+9,72 k+12$ 这 5 个数, 由抽屉原理, 其中必有两个数的 $p, q$ 值奇偶性都相同, 但注意到其中任意两个数形如 $r m,(r+1) m$,从而这两个数 $p, q$ 值奇偶性相同意味着 $p(r)+p(r+1), q(r)+q(r+1)$ 都是偶数,也即 $r$ 是好数.

从而, 我们发现对任意正整数 $k, 12 k, 9 k, 8 k, 6 k, 36 k+3.24 k+2,12 k+1,72 k+$
$8,18 k+2,24 k+3$ 中至少有一个好数.

取 $k=1$ 可以知道 1 到 100 内至少有一个好数, 取 $k=1,2, \cdots,\left[\frac{N}{100}\right]$, 可以构造出 $\left[\frac{N}{100}\right]$ 个不超过 $N$ 的好数, 且每一个数至多重复出现 10 次, 所以不超过 $N$ 的好数至少有 $\left[\frac{N}{1000}\right]$ 个. 结合 1 到 100 内至少有一个好数, 容易知道取 $c=\frac{1}{2000}$ 满足要求.

评注 通过仅考虑 $p(n)+p(n+1)$ 为偶数的简单情况, 可以发现本题的核心是构造两两之比为 $r: r+1$ 的数利用抽屉原理. 这样的数的构造用归纳构造的思路是熟知的. 但是在本题中如果使用归纳构造, 会得到 $360 k, 360 k+8,360 k+9,360 k+10,360 k+12$ 的构造, 则对 $N$ 较小的情况还需要进行处理. (可以手动构造小于 100 的好数, 但是若 $p$ 也类似于 $q$ 的构造, 仅对某个集合计算, 手动构造会更为复杂).

N8. 证明对于任何正整数 $n, 5^{n}-3^{n}$ 不能被 $2^{n}+65$ 整除.

证明 反证法. 假如结论不成立, 设有某个 $n$ 使 $2^{n}+65 \mid 5^{n}-3^{n}$, 则 $n$ 是奇数 (否则 $2^{n}+65$ 为 3 的倍数但 $5^{n}-3^{n}$ 不是). 任取 $2^{n}+65$ 的质因子 $p$ (易知 $p \neq 2,3,5$ ), 可以知道 $p \mid 5^{n}-3^{n}$, 故 $\frac{5}{3}$ 是模 $p$ 的二次剩余 (因为 $\frac{5}{3}$ 模 $p$ 的阶是一个奇数), 也即 $\left(\frac{5}{p}\right)=\left(\frac{3}{p}\right)$, 由二次互反律, 这等价于 $\left(\frac{p}{5}\right)\left(\frac{p}{3}\right)(-1)^{\frac{p-1}{2}}=1$, 计算可知 $p \equiv \pm 1, \pm 7, \pm 11, \pm 17(\bmod 60)$, 注意到模 60 余 $\pm 1, \pm 7, \pm 11, \pm 17$ 的数相乘模 60 还余 $\pm 1, \pm 7, \pm 11, \pm 17$, 所以 $2^{n}+65$ 模 60 也余 $\pm 1, \pm 7, \pm 11, \pm 17$, 但容易知道 $2^{n}+65 \equiv 13,37(\bmod 60)(n \geq 3)$. 从而 $n=1$ 或 2, 验算知矛盾!

评注 常见的利用二次剩余分析质因子性质的方法, 做法较唯一. 类似的题还有证明 $2^{n}-1$ 不整除 $3^{n}-1(n>1)$.

