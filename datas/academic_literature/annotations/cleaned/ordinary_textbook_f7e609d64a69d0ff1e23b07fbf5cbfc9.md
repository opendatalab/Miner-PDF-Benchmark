$$
\text { 数学新星网 * 教师专栏 }
$$

www.nsmath.cn/jszl

# 第五届国际大都市竞赛数学试题评析 

王广廷

(上海市上海中学, 200231)

每年 9 月份在俄罗斯莫斯科举办的国际大都市奥林匹克已经举办成功了四届. 这个比赛也成为了一项在全球有广泛影响力的赛事, 吸引着全球三十多个国家, 四十多座城市的参与, 比赛涉及四个学科: 数学、物理、化学、计算机, 其灵活的机制受到参赛者的好评.

今年由于受到疫情影响, 大都市竞赛没有组织线下比赛, 采用线上比赛的形式, 跟往年相比, 今年题目偏容易, 没有特别困难的问题. 本文给出这次比赛的试题评析.

## I. 试 题

1. $\triangle A B C$ 中, $\angle C$ 为直角, $\angle A$ 的平分线 $A L$ 交 $B C$ 于点 $L$, 交高 $C H$ 于点 $K . \angle B C H$ 的平分线与线段 $A B$ 交于点 $M$. 证明: $C K=M L$.
2. 是否存在十进制下的正整数 $n$, 使得它的各位数字都大于 5 , 但它的平方的各位数字都小于 5 ?
3. 给定正整数 $n>1$. 铸币需要一套 $n$ 种面值的硬币, 币值分别为 $a_{1}, \ldots, a_{n}$, $a_{i} \in \mathbb{N}^{*}$, 每种面值的硬币个数不限, 若币值 $\left\{a_{1}, \ldots, a_{n}\right\}$ 满足: $a_{1}+a_{2}+\cdots+a_{n}$只能通过唯一的一种方式给出 (记每种面额各一次), 就称这套币值是" 幸运”.

(1) 证明: 存在一组满足 $a_{1}+\cdots+a_{n}<n \cdot 2^{n}$ 的幸运币值 $\left\{a_{1}, \ldots, a_{n}\right\}$;

(2) 证明: 对所有幸运币值 $\left\{a_{1}, \ldots, a_{n}\right\}$, 必有 $a_{1}+\cdots+a_{n}>n \cdot 2^{n-1}$.

4. 正实数 $a, b, c$ 满足 $a^{2}=b^{2}+b c, b^{2}=c^{2}+a c$, 求证: $\frac{1}{c}=\frac{1}{a}+\frac{1}{b}$.
5. $A, B$ 两人在一个 $2^{100}$ 行、 100 列的网格表上玩游戏. 两人轮流在第一行的空单元格里填入符号由 $A$ 先开始, 在每个回合中, $A$ 任选一个第一行的空单元格在其中填入了一个 $X$. 随后 $B$ 任选一个第一行的空单元格. 在其中填入一

修订日期: 2021-03-31.
个 $O$. 当第一行的所有单元格都不空时, 两人开始对第二行的单元格填入符号并依次类推. 直到所有单元格都不空为止. $A$ 的目标是让网格表中出现尽可能的互不相同的行. $B$ 的目标是让网格表中互不相同的行尽可能少.如果两人都使用自己的最佳策略, 那么网格表中最终有多少个互不相同的行?

6. 如图, 凸五边形 $A B C D E$ 中, 对角线 $B D$ 与 $C E$ 交于点 $A_{1}, C E$ 与 $D A$交于点 $B_{1}, D A$ 与 $E B$ 交于点 $C_{1}, E B$ 与 $A C$ 交于点 $D_{1}, A C$ 与 $B D$ 交于点 $E_{1}$. 若五个凸四边形 $A B A_{1} B_{1}, B C B_{1} C_{1}, C D C_{1} D_{1}, D E D_{1} E_{1}, E A E_{1} A_{1}$ 有四个为圆内接四边形. 证明: 第五个也是圆内接四边形.



II . 解答与评注

题 $1 \triangle A B C$ 中, $\angle C$ 为直角, $\angle A$ 的平分线 $A L$ 交 $B C$ 于点 $L$, 交高 $C H$ 于点 $K . \angle B C H$ 的平分线与线段 $A B$ 交于点 $M$. 证明: $C K=M L$.



证明 $\because C=90^{\circ}, C H \perp A B, \therefore \angle H C B=\angle C A H . \because C M$ 平分 $\angle H C B, A L$平分 $\angle C A B, \therefore \angle L C M=\angle C A L, C M \perp K L$. 又 $\because A L$ 平分 $\angle C A M, \therefore A C=$ $A M, \triangle C A L \cong \triangle M A L, M L=C L$. 又 $\because \angle C L K=\angle B+\angle L A B, \angle C K L=$ $\angle C A L+\angle A C K, \angle C A L=\angle B A L, \angle A C H=\angle B, \therefore \angle C K L=\angle C L A, C L=$ $C K, C K=M L$.

评注 本题是一道极为简单的几何题, 只需使用最为基本的角关系与三线合一即可.
题 2 是否存在十进制下的正整数 $n$, 使得它的各位数字都大于 5 , 但它的平方的各位数字都小于 5 ?

解 (石镕诚) 事实上, 不存在这样的正整数 $n$.

用反证法. 假设存在这样的 $n$, 设 $n=\overline{a_{1} a_{2} \cdots a_{n}}$, 其中 $n$ 的各位数字均大于 5. 对 $1 \leq i \leq n$, 归纳证明 $a_{1}=\cdots=a_{i-1}=6, a_{i}=6$ 或 7 .

当 $i=1$ 时,因 $a_{1}>5$, 故 $a_{1}=6,7,8,9$. 若 $a_{1}=8$, 则 $n^{2}$ 首位为 6,7 , 或 8 ;若 $a_{1}=9, n^{2}$ 首位为 8 或 9 . 两者皆矛盾, 故 $a_{1}=6$ 或 7 成立.

下证对于 $i \geq 2$ 时, 若 $a_{1}=\cdots=a_{i-2}=6$, 且 $a_{i-1}=6$ 或 7 , 则 $a_{i-1}=6$, $a_{i}=6$ 或 7.

(i) 当 $a_{i-1}=6$ 时, 设 $M=\overline{a_{i+1} \cdots a_{m}}$ 并记 $k=m-i$. 我们有 $0 \leq M<10^{k}$.

假设 $a_{i}=8, n=\underbrace{6 \cdots 6}_{(i-1) \text { 个 }} 8 \times 10^{k}+M$, 则

$$
n^{2}=\underbrace{4 \cdots 4}_{(i-1) \uparrow} 6 \underbrace{2 \cdots 2}_{(i-1) \uparrow} 4 \times 10^{2 k}+1 \underbrace{3 \cdots 3}_{(i-1) \uparrow} 6 \times 10^{k} \times M+M^{2} .
$$

下式成立 (利用 $0 \leq M<10^{k}$ )

$$
\underbrace{4 \cdots 4}_{(i-1) \uparrow} 6 \underbrace{2 \cdots 2}_{(i-1) \uparrow} 4 \times 10^{2 k} \leq n^{2}<\underbrace{4 \cdots 4}_{(i-1) \uparrow} 7 \underbrace{5 \cdots 5}_{(i-2) \uparrow} 61 \times 10^{2 k}
$$

故 $n^{2}$ 第 $i$ 位为 6 或 7 , 矛盾, 假设错误.

假设 $a_{i}=9, n=\underbrace{6 \cdots 6}_{(i-1) \text { 个 }} 9 \times 10^{k}+M$ 同理有

$$
\underbrace{4 \cdots 4}_{(i-1) \uparrow} 7 \underbrace{5 \cdots 5}_{(i-2) \uparrow} 61 \times 10^{2 k} \leq n^{2}<\underbrace{4 \cdots 4}_{(i-1) \uparrow} \underbrace{8 \cdots 8}_{(i-2) \uparrow} 900 \times 10^{2 k},
$$

故 $n^{2}$ 第 $i$ 位为 7 或 8 或 9 , 矛盾, 假设错误. 故 $a_{i}=6$ 或 7 成立.

(ii) $a_{i-1}=7$ 时, $n=\underbrace{6 \cdots 6}_{(i-2) \uparrow} 7 a_{i} \times 10^{k}+M$, 其中 $M, k$ 定义与 (i) 中相同, $a_{i}=6,7,8,9$.

当 $i \geq 3$ 时,我们有

$$
\underbrace{4 \cdots 4}_{(i-2) \uparrow} 56 \underbrace{8 \cdots 8}_{(i-3) \text { 个 }} 976 \times 10^{2 k} \leq n^{2}<\underbrace{4 \cdots 4}_{(i-2) \uparrow} 6 \underbrace{2 \cdots 2}_{(i-2) \uparrow} 400 \times 10^{2 k} \text {, }
$$

故 $n^{2}$ 第 $i-1$ 位为 5 或 6 , 矛盾.

当 $i=2$ 时, 我们有

$$
5776 \times 10^{2 k} \leq n^{2}<6400 \times 10^{2 k}
$$

故 $n^{2}$ 首位为 5 或 6 , 矛盾.

从而 $a_{i-1} \neq 7$ 情形不成立.
综上所述, 对于 $i \geq 2$ 时, 若 $a_{1}=\cdots=a_{i-2}=6$, 且 $a_{i-1}=6$ 或 7 , 则 $a_{i-1}=6, a_{i}=6$ 或 7 . 因此, 对于 $1 \leq i \leq m$, 我们有 $a_{1}=\cdots=a_{i-1}=6, a_{i}=6$或 7 . 取 $i=m, n^{2}$ 末位为 6 或 9 , 矛盾.

命题得证.

评注 本题为中等难度问题. 容易发现 $n$ 不存在, 证明过程中可从前若干位估值入手, 证明 $n$ 各位数字具有特定的形式. 中间讨论过程较为繁琐, 需要多次利用所给条件.

题 3 给定正整数 $n>1$. 铸币需要一套 $n$ 种面值的硬币, 币值分别为 $a_{1}, \ldots, a_{n}, a_{i} \in \mathbb{N}^{*}$, 每种面值的硬币个数不限, 若币值 $\left\{a_{1}, \ldots, a_{n}\right\}$ 满足: $a_{1}+$ $a_{2}+\cdots+a_{n}$ 只能通过唯一的一种方式给出 (记每种面额各一次), 就称这套币值是”幸运”。

(1) 证明: 存在一组满足 $a_{1}+\cdots+a_{n}<n \cdot 2^{n}$ 的幸运币值 $\left\{a_{1}, \ldots, a_{n}\right\}$;

(2) 证明: 对所有幸运币值 $\left\{a_{1}, \ldots, a_{n}\right\}$ ，必有 $a_{1}+\cdots+a_{n}>n \cdot 2^{n-1}$.

证明 (王元鸿) (1) 令 $a_{1}=2^{n}-2^{0}, a_{2}=2^{n}-2^{1}, \ldots, a_{n}=2^{n}-2^{n-1}$, 则 $a_{1}>a_{2}>\cdots>a_{n}$, 则 $a_{1}+a_{2}+\cdots+a_{n}=(n-1) \cdot 2^{n}+1$.

设 $b_{1}, b_{2}, \ldots, b_{n} \in \mathbb{N}$ 满足

$$
\sum_{i=1}^{n} a_{i} \cdot b_{i}=(n-1) \cdot 2^{n}+1
$$

则

$$
\sum_{i=1}^{n}\left(2^{n}-a_{i}\right) \cdot b_{i}=\left(\sum_{i=1}^{n} b_{i}\right) \cdot 2^{n}-(n-1) \cdot 2^{n}-1 .
$$

设 $\sum_{i=1}^{n} b_{i}=m$, 则

$$
\sum_{i=1}^{n} 2^{i-1} \cdot b_{i}=(m-n+1) \cdot 2^{n}-1
$$

引理 $\quad$ 若 $\sum_{i=1}^{k} 2^{i-1} \cdot S_{i} \equiv-1\left(\bmod 2^{k}\right), k, S_{1}, S_{2}, \ldots, S_{k} \in \mathbb{N}$, 则 $\sum_{i=1}^{k} S_{i} \geq k$.

证明 考虑使 $\sum_{i=1}^{k} S_{i}$ 最小的一组 $\left(S_{1}, S_{2}, \ldots, S_{k}\right)$, 若存在 $1 \leq i \leq k, S_{i} \geq 2$,则令 $S_{i}^{\prime}=S_{i}-2, S_{i+1}^{\prime}=S_{i+1}+1, S_{j}^{\prime}=S_{j}(j \neq i+1)\left(\right.$ 若 $i=k$, 则只须令 $\left.S_{i}^{\prime}=S_{i}-2\right)$,

$$
\sum_{i=1}^{k} 2^{i-1} \cdot S_{i}^{\prime} \equiv \sum_{i=1}^{k} 2^{i-1} \cdot S_{i}-2 \cdot 2^{i-1}+2^{i} \equiv-1\left(\bmod 2^{k}\right)
$$

但 $\sum_{i=1}^{k} S_{i}^{\prime}=\sum_{i=1}^{k} S_{i}-1$ 与最小性矛盾! 故 $\forall 1 \leq i \leq k, S_{i} \leq 1$.
而

$$
2^{k}-1 \leq \sum_{i=1}^{k} 2^{i-1} \cdot S_{i} \leq \sum_{i=1}^{k} 2^{i-1}=2^{k}-1
$$

故 $S_{i}=1,1 \leq i \leq k$, 即 $\sum_{i=1}^{k} S_{i}$ 最小值为 $k$. 引理得证.

回到原题, 对任意 $k \leq n$, 有

$$
\sum_{i=1}^{k} 2^{i-1} \cdot b_{i} \equiv-1\left(\bmod 2^{k}\right)
$$

故 $\sum_{i=1}^{k} b_{i} \geq k$.

设 $S_{k}=\sum_{i=1}^{k} b_{i} \geq k, 1 \leq k \leq n$, 补充定义 $S_{0}=0$. 则

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} \cdot b_{i} & =\sum_{i=1}^{n} a_{i}\left(S_{i}-S_{i-1}\right) \\
& =\sum_{i=1}^{n-1} S_{i}\left(a_{i}-a_{i+1}\right)+S_{n} \cdot a_{n} \\
& \geq \sum_{i=1}^{n-1} i \cdot\left(a_{i}-a_{i+1}\right)+n \cdot a_{n} \\
& =\sum_{i=1}^{n} a_{i} .
\end{aligned}
$$

从而等号成立, 即 $b_{1}=\cdots=b_{n}=1$, 因此 $\left\{a_{1}, a_{2}, \ldots, a_{n}\right\}$ 为幸运的. 故

$$
a_{1}+a_{2}+\cdots+a_{n}=(n-1) \cdot 2^{n}+1<n \cdot 2^{n} .
$$

证毕!

(2) 因为 $n>1,\left\{a_{1}, a_{2}, \ldots, a_{n}\right\}$ 为幸运的, 故 $a_{1}, a_{2}, \ldots, a_{n}$ 互不相同.

不妨设 $a_{1}<a_{2}<\cdots<a_{n}$, 若 $\left\{a_{2}, \cdots, a_{n}\right\}$ 有两个不同的子集 $A, B$, 满足

$$
\sum_{i \in A} a_{i} \equiv \sum_{i \in B} a_{i} \quad\left(\bmod a_{1}\right)
$$

不妨设 $\sum_{i \in A} a_{i} \geq \sum_{i \in B} b_{i}$, 令

$$
A^{\prime}=A \backslash(A \cap B), B^{\prime}=B \backslash(A \cap B),
$$

则

$$
\sum_{i \in A^{\prime}} a_{i}-\sum_{i \in B^{\prime}} a_{i}=\sum_{i \in A} a_{i}-\sum_{i \in B} a_{i} \geq 0 .
$$

设

$$
\sum_{i \in A^{\prime}} a_{i}-\sum_{i \in B^{\prime}} a_{i}=k \cdot a_{1}
$$

令 $b_{1}=k+1$,

$$
b_{j}=\left\{\begin{array}{cc}
0 & j \in A^{\prime} \\
2 & j \in B^{\prime} \\
1 & j \notin A^{\prime}, j \notin B^{\prime}, j \neq 1
\end{array}\right.
$$

则

$$
\sum_{i=1}^{n} a_{i} b_{i}=\sum_{i=1}^{n} a_{i}+k \cdot a_{1}+\sum_{i \in B^{\prime}} a_{i}-\sum_{i \in A^{\prime}} a_{i}=\sum_{i=1}^{n} a_{i}
$$

因为 $A^{\prime}, B^{\prime}$ 不全为空, 则 $b_{i}$ 不全为 1 , 矛盾! 从而 $\left\{a_{2}, \cdots, a_{n}\right\}$ 的任两个不同的子集和模 $a_{1}$ 不同余. 又 $\left\{a_{2}, \cdots, a_{n}\right\}$ 有 $2^{n-1}$ 个不同子集, 故 $a_{1} \geq 2^{n-1}$. 从而

$$
a_{1}+\cdots+a_{n}>n \cdot a_{1} \geq n \cdot 2^{n-1}
$$

证毕!

评注 本题难度介于简单与中等之间, 第一小问主要运用代数、数论方法,第二小问涉及数论和组合的解题手段. 第一小问主要思路是先确定各项量级应在 $2^{n}$ 左右, 再适当进行尝试, 考虑与 $1,2, \ldots, 2^{n-1}$ 的常见形式进行结合. 第二小问则需抓住任两个子集和不同余这个关键点, 估计出每个 $a_{i}$ 的下界, 从而完成解答。

题 4 正实数 $a, b, c$ 满足 $a^{2}=b^{2}+b c, b^{2}=c^{2}+a c$, 求证: $\frac{1}{c}=\frac{1}{a}+\frac{1}{b}$.

证法 1 使用代数方法解一次方程.

因为 $a^{2}=b^{2}+b c$ 结合 $b>0$, 有

$$
c=\frac{a^{2}-b^{2}}{b}>0 \Rightarrow a^{2}-b^{2} \neq 0
$$

代入 $b^{2}=c^{2}+a c$, 有

$$
b^{2}=\frac{\left(a^{2}-b^{2}\right)^{2}}{b^{2}}+a \cdot \frac{a^{2}-b^{2}}{b} .
$$

即

$$
b^{4}=a^{4}-2 a^{2} b^{2}+b^{4}+a^{3} b-a b^{3} \Rightarrow a\left(a^{3}+a^{2} b-2 a b^{2}-b^{3}\right)=0 .
$$

结合 $a>0$,

$$
\Rightarrow a^{3}+a^{2} b-2 a b^{2}-b^{3}=0 .
$$

从而

$$
\frac{1}{c}=\frac{1}{a}+\frac{1}{b} \Leftrightarrow \frac{b}{a^{2}-b^{2}}=\frac{1}{a}+\frac{1}{b}
$$

$$
\begin{aligned}
& \Leftrightarrow a b^{2}=a^{2} b-b^{3}+a^{3}-a b^{2} \\
& \Leftrightarrow a^{3}+a^{2} b-2 a b^{2}-b^{3}=0 .
\end{aligned}
$$

即 (1) 成立.

证法 2 构造三角形,使用几何关系.

由

$$
\begin{gathered}
a^{2}=b^{2}+b c<(b+c)^{2}(a, b, c>0) \Rightarrow a<b+c, \\
b^{2}=c^{2}+a c<(a+c)^{2} \Rightarrow b<a+c, \\
c^{2}=b^{2}-a c<b^{2} \Rightarrow c<b<a+b,
\end{gathered}
$$

故可设 $a, b, c$ 构成 $\triangle A B C$ 三边长: $B C=a, C A=b, A B=c$.



作 $\angle B A C$ 平分线 $A D$ 交 $B C$ 于 $D$, 由角平分线定理

$$
\frac{C D}{B D}=\frac{C A}{B A}=\frac{b}{c}
$$

结合 $B C=a$, 有

$$
C D=\frac{a b}{b+c} .
$$

又由

$$
a^{2}=b^{2}+b c,
$$

即

$$
b+c=\frac{a^{2}}{b}
$$

有

$$
C D=\frac{a b}{\frac{a^{2}}{b}}=\frac{b^{2}}{a} \Rightarrow C D \cdot C B=C A^{2} .
$$

结合 $\angle A C D=\angle B C A$, 有 $\triangle C A D \sim \triangle C B A$. 故

$$
\angle B A C=2 \angle D A C=2 \angle A B C .
$$

同理 $\angle A B C=2 \angle A C B$.
结合 $\angle B C A+\angle A B C+\angle A C D=\pi$. 有

$$
\angle B A C=\frac{4}{7} \pi, \angle A B C=\frac{2}{7} \pi, \angle A C B=\frac{1}{7} \pi .
$$

故由正弦定理: $c: a: b=\sin \frac{\pi}{7}: \sin \frac{4}{7} \pi: \sin \frac{2}{7} \pi$, 要证 $\frac{1}{c}=\frac{1}{a}+\frac{1}{b}$. 只需

$$
\begin{aligned}
\frac{1}{\sin \frac{\pi}{7}}=\frac{1}{\sin \frac{4}{7} \pi}+\frac{1}{\sin \frac{2}{7} \pi} & \Leftrightarrow \frac{1}{\sin \frac{4}{7} \pi}=\frac{-1+2 \cos \frac{\pi}{7}}{\sin \frac{2}{7} \pi} \\
& \Leftrightarrow 2 \cos \frac{2}{7} \pi\left(-1+2 \cos \frac{\pi}{7}\right)=1 .
\end{aligned}
$$

记 $\cos \frac{\pi}{7}=t$, 有

$$
\begin{aligned}
& \cos \frac{2}{7} \pi=2 t^{2}-1 \\
& \cos \frac{4}{7} \pi=2\left(2 t^{2}-1\right)^{2}-1=8 t^{4}-8 t^{2}+1, \\
& \cos \frac{3}{7} \pi=4 t^{3}-3 t=-\cos \frac{4}{7} \pi,
\end{aligned}
$$

从而

$$
8 t^{4}+4 t^{3}-8 t^{2}-3 t+1=0
$$

即

$$
(t+1)\left(8 t^{3}-4 t^{2}-4 t+1\right)=0 .
$$

而 $t \neq-1$, 故

$$
8 t^{3}-4 t^{2}-4 t+1=0, \quad 2\left(2 t^{2}-1\right)(-1+2 t)=1
$$

即 $8 t^{3}-4 t^{2}-4 t+1=0$. 成立.

评注 本题较容易, 可以从多个角度入手. 推测出提着应该是从背后的以 $\frac{\pi}{7}$, $\frac{2}{7} \pi, \frac{4}{7} \pi$ 为内角的特殊三角形入手, 它的边长有许多比例性质, 本题即使用了其中三个。

题 $5 A, B$ 两人在一个 $2^{100}$ 行、 100 列的网格表上玩游戏. 两人轮流在第一行的空单元格里填入符号由 $A$ 先开始, 在每个回合中, $A$ 任选一个第一行的空单元格在其中填入了一个 $X$. 随后 $B$ 任选一个第一行的空单元格. 在其中填入一个 $O$. 当第一行的所有单元格都不空时, 两人开始对第二行的单元格填入符号并依次类推. 直到所有单元格都不空为止. $A$ 的目标是让网格表中出现尽可能的互不相同的行. $B$ 的目标是让网格表中互不相同的行尽可能少. 如果两人都使用自己的最佳策略, 那么网格表中最终有多少个互不相同的行?

证明 (刘胤辰) 答案为 $2^{50}$.

I. 先给出 $B$ 的策略使互不相同的行至多 $2^{50} . B$ 将每行的 $1 \times 100$ 网格, 划为 50 个 $1 \times 2$, 则 $B$ 可保证在自己填好后此行已填的 $O$ 和 $X$ 每个 $1 \times 2$ 要为空要么恰一个 $O$ 一个 $X$. 初始时, 没有 $O$ 和 $X$ 显然成立;

在某回合后 $B$ 保证在自己填好后此行已填的 $O$ 和 $X$, 每个 $1 \times 2$ 要么为空要么恰一个 $X$; 则 $A$ 必将 $X$ 填入某个还没有 $O$ 或 $X$ 的 $1 \times 2$, 则 $B$ 在该 $1 \times 2$另一个空格填上 $O$. 故因此 $B$ 可保证在自己填好后此行每个 $1 \times 2$ 要么为空要么恰一个 $O$ 一个 $X$, 最终行填满时每个 $1 \times 2$ 恰一个 $O$ 一个 $X$.

故可使不同行至多 $2^{50}$ 个.

II. 下面证明存在 $A$ 的策略使互不相同的行至少 $2^{50}$ 个.

采取以下策略:

(a) 初始: $A$ 与 $B$ 在第一行处各打 50 个 $X$ 和 $O$. 我们对 $A$ 的打法不作要求;

(b) 过渡: 假设 $\mathrm{A}$ 与 B 已经将第 $1,2, \ldots, n\left(n \leq 2^{100}-1\right)$ 行打完. 我们记 $S_{i}$表示第 $i$ 行的 100 个 $O, X$ 组成的有序符号组, $T_{i}$ 表示第 $i$ 列的前 $n$ 个 $O, X$ 组成的有序符号组, $S_{i} \cap T_{j}$ 表示交叉格 $(i, j)$ 上的格上的符号 $(1 \leq i \leq n)$.

现在 $A$ 与 $B$ 在第 $n+1$ 行进行游戏. 我们将这 100 次分为 50 轮 ( $A B$ 轮流):

(i) 初始: 记 $I_{0}=1,2, \ldots, n ; J_{0}=1,2, \ldots, 100$.

(ii) 过渡: $A$ 考察对每个 $j\left(j \in J_{l-1}\right), \bigcup_{i \in I_{l-1}}\left(S_{i} \cap T_{j}\right)$ 中 $O$ 和 $X$ 个数.

第 $l$ 轮时 $1 \leq l \leq 50$.

(1) 若存在 $j \in J_{l-1}$ 使 $\bigcup_{i \in I_{l-1}}\left(S_{i} \cap T_{j}\right)$ 中 $O$ 个数 $\geq X$ 个数, 则 $A$ 在第 $n+1$行第 $j$ 列位置打 $X$;

(2) 若不存在 $j \in J_{l-1}$ 使 $\bigcup_{i \in I_{l-1}}\left(S_{i} \cap T_{j}\right)$ 中 $O$ 个数 $\geq X$ 个数, 则 $A$ 随意在第 $n+1$ 行任何一个空着的位置位置打 $O$.

在 $A$ 操作后 $B$ 操作. $A, B$ 均操作完后:

若为情形 (1), 则定义新一轮的 $I_{l}=\left\{i \mid i \in I_{l-1}\right.$ 且 $S_{i} \cap T_{j}$ 为 $\left.X\right\}$ (其中 $j$ 为情形 (1) 中所定义的), $J_{l}=\left\{i \mid i \in J_{l-1}\right.$ 且在本轮中未被 $A / B$ 选中 $\}$;

若为情形 (2), 设 $A$ 操作第 $j$ 列, 则定义 $I_{l}=\left\{i \mid i \in I_{l-1}\right.$ 且 $S_{i} \cap T_{j}$ 为 $\left.O\right\}$, $J_{l}=\left\{i \mid i \in J_{l-1}\right.$ 且在本轮中未被 $A / B$ 选中 $\}$.

(iii) 终止. 若存在 $I_{l}=\emptyset(1 \leq l \leq 50)$, 则在此之后第 $l+1$ 轮 -50 轮 $A$ 随意选择即可; 若 $(i i)$ 运行至 $l=50$ 完成, 则我们就已完成 $n+1$ 行的策略.

(c) 终止: 当整个表格均已填完时终止.

下面验证策略符合且在 $n=1,2, \cdots, 2^{50}-1$ 时所得到 $2^{50}$ 行互不相同.

首先 $A$ 的操作位置永远为空格符合操作要求; 其次在 $n \leq 2^{50}-1$ 时由 (2)
的过渡.

在第 $l$ 轮时, 可能与第 $n+1$ 行一样的行仅可能是那些 $i \in I_{l}$ 的第 $i$ 行.

对于情形 (1), 在第 $j$ 列上有 $X$ 的且在 $I_{l-1}$ 中的行也就是在 $I_{l}$ 中的行, 又结合 $\bigcup_{i \in I_{l-1}}\left(S_{i} \cap T_{j}\right)$ 中 $O$ 个数 $\geq X$ 个数, 可得

$$
\left|I_{l}\right| \leq \frac{1}{2}\left|I_{l-1}\right|
$$

对于情形 (2), 在第 $j$ 列上有 $O$ 的且在 $I_{l-1}$ 中的行也就是在 $I_{l}$ 中的行, 又结合对每个 $S \in J_{l-1}, \bigcup_{i \in I_{l-1}}\left(S_{i} \cap T_{s}\right)$ 中 $O$ 个数 $<X$ 个数, 故特别地对第 $j$ 列有 $\left|I_{l}\right|<\frac{1}{2}\left|I_{l-1}\right|$. 从而由 $\left|I_{0}\right|=n$ 有

$$
\left|I_{50}\right| \leq \frac{1}{2^{50}} \times n<1 \Rightarrow I_{50}=\varnothing
$$

故操作终止时没有 $1 \sim n$ 中任意一行可能与策略所得第 $n+1$ 行相同. 即 $1,2,3, \cdots, 2^{50}$ 行互不相同.

由此存在 $A$ 策略使互不相同行至少 $2^{50}$ 个.

综上, 结合 I,II, $A, B$ 都使用最佳策略. 最终有 $2^{50}$ 个互不相同行.

评注 这是一道中等难度的组合题. 答案很容易猜出. 而本题中 $B$ 的策略容易给出. 对于 $A$ 的策略, 笔者原本意图使用概率方法解本题, 但逻辑出现部分漏洞. 最后 $A$ 的策略, 由一个直接的贪心算法给出. 贪心中每轮可能相同的行少一半. 故在前 $2^{50}$ 行中那些行互不相同. 有兴趣的读者可试试看如何用概率方法解本题.

题 6 如图, 凸五边形 $A B C D E$ 中, 对角线 $B D$ 与 $C E$ 交于点 $A_{1}, C E$ 与 $D A$交于点 $B_{1}, D A$ 与 $E B$ 交于点 $C_{1}, E B$ 与 $A C$ 交于点 $D_{1}, A C$ 与 $B D$ 交于点 $E_{1}$. 若五个凸四边形 $A B A_{1} B_{1}, B C B_{1} C_{1}, C D C_{1} D_{1}, D E D_{1} E_{1}, E A E_{1} A_{1}$ 有四个为圆内接四边形. 证明: 第五个也是圆内接四边形.


证明 (丁天巽) 不妨除 $E A E_{1} A_{1}$ 外的四个四边形为圆内接四边形, 则由 $A B A_{1} B_{1}$ 共圆有

$$
\begin{aligned}
\frac{A A_{1}}{\sin \angle A B_{1} A_{1}} & =\frac{B B_{1}}{\sin \angle B A_{1} B_{1}} \\
A A_{1} \cdot \sin \angle B A_{1} B_{1} & =B B_{1} \cdot \sin \angle A B_{1} A_{1} .
\end{aligned}
$$

同理有

$$
\begin{aligned}
& B B_{1} \cdot \sin \angle C B_{1} C_{1}=C C_{1} \cdot \sin \angle B C_{1} B_{1}, \\
& C C_{1} \cdot \sin \angle D C_{1} D_{1}=D D_{1} \cdot \sin \angle C D_{1} C_{1}, \\
& D D_{1} \cdot \sin \angle E D_{1} E_{1}=E E_{1} \cdot \sin \angle D E_{1} D_{1}
\end{aligned}
$$

从而

$$
\frac{A A_{1}}{\sin \angle A E_{1} A_{1}}=\frac{E E_{1}}{\sin \angle E A_{1} E_{1}} .
$$

故 $\triangle A E_{1} A_{1}$ 与 $\triangle E E_{1} A_{1}$ 外接圆半径相同.

而

$$
\begin{aligned}
\angle E_{1} A A_{1}+\angle E_{1} E A_{1} & <\angle C A D+\angle B E C \\
& =2 \pi-(\angle E B C+\angle B C E+\angle A C D+\angle A D C) \\
& <2 \pi-(\angle D B C+\angle D C B+\angle B D C) \\
& =\pi .
\end{aligned}
$$

故 $\angle E_{1} A A_{1}=\angle E_{1} E A_{1}$. 因此 $A E A_{1} E_{1}$ 共圆.

评注 本题是一道较不常规的几何题, 共圆的转化与证明不通过常规的几何关系, 而是利用圆中的正弦定理进行, 借助图形本身的高度对称性得出最后的结果. 而需注意到共圆与正弦定理成立并非相互等价, 故需进行分类讨论.

