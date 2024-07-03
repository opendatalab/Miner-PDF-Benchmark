数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年美国 TSTST 试题解析 

马尧 孙牧聪 王衔邦

(中国人民大学附属中学, 100080)

指导教师: 陈晨(学而思教育集团)

下文为 2021 年美国 TSTST 的试题及解析. 在以前, TSTST 用于选拔 usamo 优胜者进入 mop(类似于我国冬令营进入集训队), 但受到疫情影响, 2021 年 TSTST 提高了难度, 并代替 TST 用于选拔国家队. 2021 年的美国 TSTST 分三天进行, 每天试题共三道, 考试时间 4 个半小时. 2021 TSTST 题目新颖,难度介于我国的冬令营到集训队之间. 很适合备战冬令营及以上考试的同学们训练和参考。

作为参考, 这里给出美国 mop 60 名队员的各题目平均分(满分 7 分):
4.72
$2.27 \quad 0.18$
3.77
4.92
0.30
4.63
3.38
0.60

原始解答来自各位同学和陈晨老师的课堂讲解, 我们已尽力把解答写的清晰易懂,但仍不免有瑕疵,欢迎批评指正.

## I. 试 题

1. $A B C D$ 内接于圆 $O$, 点 $X, Y$ 分别在 $A B, C D$ 上. $\triangle A D X$ 及 $\triangle B C Y$的外接圆分别交 $X Y$ 于 $P, Q$, 证明: $O P=O Q$.
2. 设 $a_{1}<a_{2}<a_{3}<\cdots$ 为在 $(0,1)$ 内的无穷数列. 证明: 存在一个数在以下序列中出现恰好一次:

$$
\frac{a_{1}}{1}, \frac{a_{2}}{2}, \frac{a_{3}}{3}, \cdots
$$

3. 求所有整数 $k \geq 2$, 使得存在正整数 $n$, 满足 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 为 $n$ 的倍数, 但对任意 $2 \leq m<k$ 均有 $\left(\begin{array}{l}n \\ m\end{array}\right)$ 不是 $n$ 的倍数.
4. 给定正整数 $a, b$. 已知存在无穷多对正整数 $(m, n)$ 使得 $m^{2}+a n+b$ 及 $n^{2}+a m+b$ 均为完全平方数, 证明: $2 b$ 被 $a$ 整除.

修订日期: 2022-03-14.

5. 设 $T$ 是一棵 $n$ 个点的树, 它恰有 $k$ 个点 $u$ 满足 $\operatorname{deg} u=1$. 若可以找到 $T$ 中的 $\frac{n+k-1}{2}$ 个点满足它们两两不相邻, 证明: $T$ 的最长路包含奇数个点.
6. $\triangle A B C, \triangle D E F$ 有公共外接圆 $\Omega$ 及公共内切圆 $\omega, A, F, B, D, C, E$ 顺次在 $\Omega$ 上. $\Delta_{A}$ 定义为 $A B, A C, E F$ 围出的三角形, 类似定义 $\Delta_{B}, \Delta_{C}, \cdots, \Delta_{F}$.定义 $\Omega_{A}$ 和 $\omega_{A}$ 分别为 $\Delta_{A}$ 的外接圆和内切圆, 类似定义 $\Omega_{B}, \omega_{B}, \cdots, \Omega_{F}, \omega_{F}$.

(a) 证明: $\Omega_{A}$ 和 $\Omega_{D}, \omega_{A}$ 和 $\omega_{D}$ 关于同一点位似;

(b) 设上述位似点为 $P_{A D}$, 类似定义 $P_{B E}$ 及 $P_{C F}$, 证明这三点共线.

7. 设 $M$ 是由有限个格点组成的集合, $n$ 是正整数. 一条“安全路”被定义为从 $(0,0)$ 开始, 经历若干格点到 $x+y=n$ 上一格点结束, 且不经过一切 $M$ 中的点的长度为 $n$ 的路. 证明: 若存在安全路, 则至少有 $2^{n-|M|}$ 条.
8. $\triangle A B C$ 为不等边三角形. $A_{1}, B_{1}, C_{1}$ 分别在线段 $B C, C A, A B$ 上, 满足 $\triangle A_{1} B_{1} C_{1}$ 与 $\triangle A B C$ 对应相似. $A_{2}$ 是在 $B_{1} C_{1}$ 上满足 $A A_{2}=A_{1} A_{2}$ 的唯一一点,类似定义 $B_{2}, C_{2}$. 证明: $\triangle A_{2} B_{2} C_{2}$ 与 $\triangle A B C$ 相似.
9. 令 $q=p^{r}$, 这里 $p$ 为质数且 $r$ 为正整数. 取 $\zeta=e^{\frac{2 \pi i}{q}}$. 求最小的正整数 $n$, 使得

$$
\sum_{1 \leq k \leq q, \operatorname{gcd}(k, p)=1} \frac{1}{\left(1-\zeta^{k}\right)^{n}}
$$

不是整数.

## II. 解答与评注

题 $1 A B C D$ 内接于圆 $O$, 点 $X, Y$ 分别在 $A B, C D$ 上. $\triangle A D X$ 及 $\triangle B C Y$的外接圆分别交 $X Y$ 于 $P, Q$, 证明: $O P=O Q$.


证明 设 $B Q$ 交圆 $O$ 于 $M, D P$ 交圆 $O$ 于 $N$. 由共圆, 我们有

$$
\angle X P D=\pi-\angle D A X=\pi-\angle D A B=\angle B N D,
$$

故 $X Y / / B N$. 同理有 $X Y / / D M$, 故 $B N / / D M$. 注意到 $P, Q$ 分别是 $N D, B M$与 $X, Y$ 的交点, 由对称性知 $O P=O Q$.

评注 经典的平行一等腰梯形结构.

题 2 设 $a_{1}<a_{2}<a_{3}<\cdots$ 为在 $(0,1)$ 内的无穷数列. 证明: 存在一个数在以下序列中出现恰好一次:

$$
\frac{a_{1}}{1}, \frac{a_{2}}{2}, \frac{a_{3}}{3}, \cdots
$$

证明 方便起见, 记 $\frac{a_{i}}{i}=f(i)$.

用反证法. 若不然, 取最大的正整数 $x_{1}$ 使 $f(1)=f\left(1+x_{1}\right)$, 再取最小的正整数 $y_{1}$ 满足存在 $t \geq 1$ 使 $f\left(1+x_{1}+y_{1}\right)=f\left(1+x_{1}+y_{1}+t\right)$. 记这样最小的 $t$ 为 $x_{2}$,再取最小的 $y_{2}$ 满足存在 $t \geq 1$ 使 $f\left(1+x_{1}+y_{1}+x_{2}+y_{2}\right)=f\left(1+x_{1}+y_{1}+x_{2}+y_{2}+t\right)$,以此类推.

事实上, 一定可以找到满足条件的 $\left\{x_{n}\right\},\left\{y_{n}\right\}$. 我们需要证明如下引理:

引理 对任意 $0<k<1$, 仅存在有限多个 $i$ 满足 $f(i)=k$.

证明 取 $N>\frac{1}{k}$, 则对任意正整数 $n \geq N, f(n)=\frac{a_{n}}{n}<\frac{1}{n}<k$. 故这样的 $i$至多 $N-1$ 个, 得证.

回到原题. 由引理, $x_{i}$ 一定存在. 同时, 对于任意正整数 $N$, 都存在 $x \neq y>N$ 满足 $f(x)=f(y)$. 这就证明了 $y_{i}$ 一定存在.

此时, 我们考虑 $f\left(1+x_{1}+1\right), \cdots, f\left(1+x_{1}+y_{1}-1\right)$, 由 $y_{1}$ 的最小性, 这些项互不相同, 且不与 $f\left(1+x_{1}+y_{1}\right)$ 及之后的项相等. 故它们必与前面的某项相同. 注意到它们不能与 $f(1)$ 相等(否则与 $x_{1}$ 的最大性矛盾), 且 $f(2), \cdots, f\left(1+x_{1}-1\right)$至多 $x_{1}-1$ 种不同的值, 故 $y_{1}-1 \leq x_{1}-1$, 即 $y_{1} \leq x_{1}$.

更进一步, 记 $A_{k+1}$ 为 $f\left(1+\left(x_{1}+y_{1}\right)+\cdots+\left(x_{k}+y_{k}\right)+x_{k+1}+1\right), \cdots$, $f\left(1+\left(x_{1}+y_{1}\right)+\cdots+\left(x_{k}+y_{k}\right)+x_{k+1}+y_{k+1}-1\right)$ 组成的集合, $B_{k+1}$ 为 $f\left(1+\left(x_{1}+y_{1}\right)+\cdots+\left(x_{k}+y_{k}\right)\right), \cdots, f\left(1+\left(x_{1}+y_{1}\right)+\cdots+\left(x_{k}+y_{k}\right)+x_{k+1}-1\right)$组成的集合, 则 $A_{1}, \cdots, A_{k}$ 中的数互不相同且均在 $B_{1}, \cdots, B_{k}$ 中出现, 故

$$
\begin{aligned}
y_{1}+\cdots+y_{k} & =\left|A_{1}\right|+\cdots+\left|A_{k}\right|+k \\
& \leq\left|B_{1}\right|+\cdots+\left|B_{k}\right|+k
\end{aligned}
$$

$$
\leq x_{1}+\cdots+x_{k}
$$

记 $A=a_{1+\left(x_{1}+y_{1}\right)+\cdots+\left(x_{n-1}+y_{n-1}\right)+x_{n}}$. 由 $f(1)=f\left(1+x_{1}\right)$ 得 $a_{1}=\frac{1}{1+x_{1}} a_{1+x_{1}}$,再由 $f\left(1+x_{1}+y_{1}\right)=f\left(1+x_{1}+y_{1}+x_{2}\right)$ 得

$$
\begin{aligned}
a_{1} & =\frac{1}{1+x_{1}} a_{1+x_{1}} \\
& <\frac{1}{1+x_{1}} a_{1+x_{1}+y_{1}} \\
& =\frac{1}{1+x_{1}} \cdot \frac{1+x_{1}+y_{1}}{1+x_{1}+y_{1}+x_{2}} a_{1+x_{1}+y_{1}+x_{2}} .
\end{aligned}
$$

以此类推,得到

$$
A>a_{1} \cdot \frac{1+x_{1}}{1} \cdot \frac{1+x_{1}+y_{1}+x_{2}}{1+x_{1}+y_{1}} \cdot \cdots \cdot \frac{1+x_{1}+y_{1}+\cdots+x_{n-1}+y_{n-1}+x_{n}}{1+x_{1}+y_{1}+\cdots+x_{n-1}+y_{n-1}}
$$

由 $y_{1}+\cdots+y_{k}<x_{1}+\cdots+x_{k}$, 有

$$
A>a_{1} \cdot \frac{S_{0}+S_{1}}{2 S_{0}} \cdot \frac{S_{1}+S_{2}}{2 S_{1}} \cdot \ldots \cdot \frac{S_{n-1}+S_{n}}{2 S_{n-1}}
$$

其中, 令 $S_{i}=\frac{1}{2}+x_{1}+\cdots+x_{i}$. 易得 $S_{n} \geq n$, 对上式用均值不等式得

$$
\begin{aligned}
A & >a_{1} \cdot \frac{2^{n} \cdot \sqrt{\left(S_{0} S_{1}\right)\left(S_{1} S_{2}\right) \cdots\left(S_{n-1} S_{n}\right)}}{2^{n} S_{0} S_{1} \cdots S_{n-1}} \\
& =a_{1} \cdot \sqrt{\frac{S_{n}}{S_{0}}} \\
& \geq a_{1} \sqrt{2 n}
\end{aligned}
$$

而 $A<1$, 故 $a_{1}<\frac{1}{\sqrt{2 n}}$ 对任意正整数 $n$ 成立. 矛盾!

评注 本题最自然的思路是希望存在一串 $\frac{a_{i}}{i}$ 全都相等, 但因为有 $a_{i}<1$ 的界易知是不行的. 这里是退而求其次, 让第一个与第二个相等, 第三个与第四个相等, 再对两组间的差距进行估计, 估计的方法有很多种, 这里选用了一种较为简洁的。

题 3 求所有整数 $k \geq 2$, 使得存在正整数 $n$, 满足 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 为 $n$ 的倍数, 但对任意 $2 \leq m<k$ 均有 $\left(\begin{array}{c}n \\ m\end{array}\right)$ 不是 $n$ 的倍数.

解 所求为全体正整数 $k \geq 2$.

我们只需要对所有 $k \geq 2$ 都找到一个 $n$ 满足题目条件. 设 $k=p_{1}^{\alpha_{1}} \cdot p_{2}^{\alpha_{2}}$. $\cdots \cdot p_{m}^{\alpha_{m}}$, 并设 1 至 $k$ 中除 $p_{i}(1 \leq i \leq m)$ 以外的质数为 $q_{1}, \cdots, q_{s}$.

对于每个 $p_{i}$, 我们设 $t_{i} \cdot p_{i}^{\beta_{i}}<k \leq\left(t_{i}+1\right) \cdot p_{i}^{\beta_{i}}$, 其中 $1 \leq t_{i} \leq p_{i}-1$. 我们希望选取 $n$ 满足 $v_{p_{i}}\left(n-t_{i} \cdot p_{i}^{\beta_{i}}\right)=\alpha_{i}+\beta_{i}$ 对任意 $1 \leq i \leq m$ 成立; 同时, 我们取充分大的 $M$, 令 $v_{q_{i}}(n)=M(1 \leq i \leq s)$. 由中国剩余定理, 一定存在满足上述所有
条件的 $n$. 我们来证这个 $n$ 满足要求.

事实上, $n \left\lvert\,\left(\begin{array}{l}n \\ l\end{array}\right)\right.$ 等价于 $l \left\lvert\,\left(\begin{array}{l}n-1 \\ l-1\end{array}\right)\right.$. 我们先证明如下三个结论.

结论 1 对任意满足 $l<k$ 且 $q_{i} \mid l$ 的正整数 $l$, 有 $l \nmid\left(\begin{array}{l}n-1 \\ l-1\end{array}\right)$.

证明 由 $q_{i}^{M} \mid n$, 故 $n-1$ 在 $q_{i}$ 进制下后 $M$ 位均为 $q_{i}-1$, 因为 $M$ 充分大,故由 Lucas 定理知 $q_{i} \nmid\left(\begin{array}{c}n-1 \\ l-1\end{array}\right)$. 得证!

结论 2 对任意满足 $l \leq t_{i} \cdot p_{i}^{\beta_{i}}$ 且 $p_{i} \mid l$ 的正整数 $l$, 有 $l \nmid\left(\begin{array}{l}n-1 \\ l-1\end{array}\right)$.

证明 由 $l$ 的大小限制, 对任意 $1 \leq j \leq l-1$ 都有 $v_{p_{i}}((n-j))=v_{p_{i}}(j)$, 故

$$
\begin{aligned}
v_{p_{i}}\left(\left(\begin{array}{c}
n-1 \\
l-1
\end{array}\right)\right) & =v_{p_{i}}\left(\frac{(n-1)(n-2) \cdots(n-l+1)}{(l-1) !}\right) \\
& =v_{p_{i}}\left(\frac{1 \cdot 2 \cdot \cdots \cdot(j-1)}{(j-1) !}\right)=0
\end{aligned}
$$

得证!

结论 3 对 $l>t_{i} \cdot p_{i}^{\beta_{i}}$ 且 $p_{i} \mid l$, 有 $v_{p_{i}}\left(\left(\begin{array}{c}n-1 \\ l-1\end{array}\right)\right)=\alpha_{i}$.

证明 存在唯一的 $A$, 使得 $n-l+1 \leq A \cdot p_{i}^{\alpha_{i}+\beta_{i}} \leq n-1$, 有

$$
\begin{aligned}
v_{p_{i}}\left(\left(\begin{array}{l}
n-1 \\
l-1
\end{array}\right)\right) & =v_{p_{i}}\left(\frac{(n-1)(n-2) \cdots(n-l+1)}{(l-1) !}\right) \\
& =v_{p_{i}}\left(\frac{(n-1) \cdots\left(A p_{i}^{\alpha_{i}+\beta_{i}}+1\right) \cdot A p_{i}^{\alpha_{i}+\beta_{i}} \cdot\left(A p_{i}^{\alpha_{i}+\beta_{i}}-1\right) \cdots(n-l+1)}{\left(t_{i} p_{i}^{\beta_{i}}-1\right) ! \cdot t_{i} p_{i}^{\beta_{i}} \cdot\left(t_{i} p_{i}^{\beta_{i}}+1\right) \cdots(l-1)}\right) \\
& =v_{p_{i}}\left(\frac{A p_{i}^{\alpha_{i}+\beta_{i}}}{t_{i} p_{i}^{\beta_{i}}} \cdot 1\right) \\
& =\alpha_{i} .
\end{aligned}
$$

得证!

由结论 3 , 可知 $k \left\lvert\,\left(\begin{array}{c}n-1 \\ k-1\end{array}\right)\right.$, 即 $n \left\lvert\,\left(\begin{array}{l}n \\ k\end{array}\right)\right.$.

而对 $2 \leq l<k$, 我们进行如下讨论:

1) 若 $l$ 含有质因子 $q_{1}, \cdots, q_{s}$ 中至少一个, 由结论 $1, n \nmid\left(\begin{array}{l}n \\ l\end{array}\right)$;
2) 若 $l$ 仅含 $p_{i}$, 设 $l=p_{1}^{r_{1}} \cdots \cdots p_{m}^{r_{m}}$. 如果 $r_{i} \leq \alpha_{i}$ 均成立, 则 $2 l \leq k$. 不妨 $r_{1}>0$, 则有 $l \leq t_{1} p_{1}^{\beta_{1}}$, 由结论 2 知也成立. 否则, 不妨 $r_{1}>\alpha_{1}$, 且 $l>t_{1} p_{1}^{\beta_{1}}$. 但是, 由结论 3 ,

$$
v_{p_{1}}\left(\left(\begin{array}{l}
n-1 \\
l-1
\end{array}\right)\right)=\alpha_{1}<r_{1}=v_{p_{1}}(l)
$$

故 $l \nmid\left(\begin{array}{c}n-1 \\ l-1\end{array}\right)$, 也成立.

综上, 这个 $n$ 是满足要求的.

评注 在思考时, 试验较小的 $k$, 想到对于 $(k, q)=1$ 的质数 $q$ 取 $q^{M} \mid n$ 是自然的. 但在解决解答中 $p_{i} \mid l$ 特别是 $r_{i}>\alpha_{i}$ 的情形还需对 $n$ 的含 $p_{i}$ 量做细致的
处理. 总体上此题较难, 花费时间也较长, 顺带提一句第九题也需要精确的计算组合数含质数幂次.

题 4 给定正整数 $a, b$. 已知存在无穷多对正整数 $(m, n)$ 使得 $m^{2}+a n+b$及 $n^{2}+a m+b$ 均为完全平方数, 证明: $2 b$ 被 $a$ 整除.

证明 因为 $m, n$ 是对称的, 故我们可以只关心 $m \leq n$ 的解.

设 $m^{2}+a n+b=(m+s)^{2}, n^{2}+a m+b=(n+t)^{2}$. 即有

$$
\left\{\begin{array}{l}
2 s m+s^{2}=a n+b \\
2 t n+t^{2}=a m+b
\end{array}\right.
$$

则 $2 t n+t^{2}=a m+b \leq a n+b$, 取 $n$ 充分大得到 $t \leq \frac{a}{2}$, 这说明 $t$ 的取值有上界.由于解有无限组, 故存在 $t_{0}$, 使得满足 $t=t_{0}$ 的解有无穷多组. 那么

$$
\begin{aligned}
2 s m+s^{2} & =a n+b \\
& =a \cdot \frac{a m+b-t_{0}^{2}}{2 t_{0}}+b \\
& =\frac{a^{2}}{2 t_{0}} \cdot m+C,
\end{aligned}
$$

其中, $C$ 为常数. 取 $m$ 充分大, 得到 $s \leq \frac{a^{2}}{4 t_{0}}$, 这说明 $s$ 的取值有上界. 由于解有无限组, 故存在 $s_{0}$, 使得满足 $s=s_{0}, t=t_{0}$ 的解有无穷多组. 此时

$$
\left\{\begin{array}{l}
2 s_{0} m+s_{0}^{2}=a n+b \\
2 t_{0} n+t_{0}^{2}=a m+b
\end{array}\right.
$$

两式联立得

$$
\left(a^{2}-4 s_{0} t_{0}\right) n=2 s_{0} t_{0}^{2}-2 s_{0} b+a s_{0}^{2}-a b .
$$

由于有无限组解, 故 $a^{2}=4 s_{0} t_{0}$, 且 $a b-a s_{0}^{2}=2 s_{0} t_{0}^{2}-2 s_{0} b$. 即 $s_{0} t_{0}$ 是完全平方数, 可设 $s_{0}=A^{2} d, t_{0}=B^{2} d$, 则 $a=2 A B d$, 代入后式得

$$
b=\left(A^{2}-A B+B^{2}\right) \cdot A B d^{2},
$$

故 $a \mid 2 b$ 成立!

评注 本题是简单题, 第一步的代换是自然的, 而后可以发现在 $m \leq n$ 时 $t$有上界, 这样就可以把变化的方程改为固定参数的方程,接下来的过程如顺水推舟.

题 5 设 $T$ 是一棵 $n$ 个点的树, 它恰有 $k$ 个点 $u$ 满足 $\operatorname{deg} u=1$. 若可以找
到 $T$ 中的 $\frac{n+k-1}{2}$ 个点满足它们两两不相邻, 证明: $T$ 的最长路包含奇数个点.

证明 取 $T$ 的最长路, 记为 $C_{1}$, 两端点为 $A, B$. 则 $\operatorname{deg} A=\operatorname{deg} B=1$, 其余 $k-2$ 个一度点 $A_{1}, \cdots, A_{k-2}$ 都不在 $C_{1}$ 上, 且它们两两之间不连边.

$A_{1}$ 通过一段路连接到 $C_{1}$ 上, 设路为 $C_{2}$, 其上共 $x_{2}$ 个点(不计 $C_{1}$ 上的点); $A_{2}$ 通过一段路连接到 $C_{1} \cup C_{2}$ 上, 设路为 $C_{3}$, 其上共 $x_{3}$ 个点(不计 $C_{1}, C_{2}$ 上的点); 以此类推.

容易得到除此之外没有其它的点和边. 注意到 $C_{1}, C_{2}, \cdots, C_{k-1}$ 中均至多取一半的点, 则总取出的点数应不超过

$$
\sum_{i=1}^{k-1}\left\lceil\frac{x_{i}}{2}\right\rceil \leq \frac{k-1}{2}+\frac{x_{1}+\cdots+x_{k-1}}{2}=\frac{n+k-1}{2}
$$

取等时, $C_{i}$ 为奇数. 即证!

评注 对于本题, 可以首先考虑 $k=2$ 的情况, 随即想到是否可以将树拆成 $k-1$ 条链, 这样就说明了 $\frac{n+k-1}{2}$ 是上界, 且所有链的长度都是奇数.

题 $6 \triangle A B C, \triangle D E F$ 有公共外接圆 $\Omega$ 及公共内切圆 $\omega, A, F, B, D, C, E$ 顺次在 $\Omega$ 上. $\Delta_{A}$ 定义为 $A B, A C, E F$ 围出的三角形, 类似定义 $\Delta_{B}, \Delta_{C}, \cdots, \Delta_{F}$.定义 $\Omega_{A}$ 和 $\omega_{A}$ 分别为 $\Delta_{A}$ 的外接圆和内切圆, 类似定义 $\Omega_{B}, \omega_{B}, \cdots, \Omega_{F}, \omega_{F}$.

(a) 证明: $\Omega_{A}$ 和 $\Omega_{D}, \omega_{A}$ 和 $\omega_{D}$ 关于同一点位似;

(b) 设上述位似点为 $P_{A D}$, 类似定义 $P_{B E}$ 及 $P_{C F}$, 证明这三点共线.

证明 设 $\Omega, \omega$ 的圆心分别为 $O, I$, 半径分别为 $R, r$. 设 $\Delta_{A}$ 的内心为 $I_{A}$,外心为 $O_{A}, \Omega_{A}, \omega_{A}$ 的半径分别为 $R_{A}, r_{A}$. 同理定义 $I_{B}, O_{B}, R_{B}, r_{B}, \cdots, I_{F}, O_{F}$, $R_{F}, r_{F}$.

作 $\Omega$ 的内接三角形 $\Delta_{A^{\prime}}, \Delta_{D^{\prime}}$ 分别与 $\Delta_{A}, \Delta_{D}$ 的三边平行. 同时, 以 $O$ 为原点作弧 $(A F B)$ 的中点 $M_{A B}$, 同理作出 $M_{A C}, M_{B C}, M_{D E}, M_{E F}, M_{D F}$. 我们记 $M_{B C}^{\prime}, M_{E F}^{\prime}$ 为 $M_{B C}, M_{E F}$ 的对径点.

由 $\Delta_{A^{\prime}}$ 与 $\Delta_{A}$ 的平行关系, $\Delta_{A^{\prime}}$ 三边作为 $\Omega$ 的弦所对弧中点恰为 $M_{A B}, M_{A C}, M_{E F}^{\prime}$. 若将 $\Omega$ 视为单位圆, 则 $\Delta_{A^{\prime}}$ 的内心 $I_{A^{\prime}}$ 所对应复数为

$$
M_{A B}+M_{A C}+M_{E F}^{\prime}=M_{A B}+M_{A C}-M_{E F}
$$

同理, $I_{D^{\prime}}$ 所对应复数为 $M_{D F}+M_{D E}-M_{B C}$. 又因为 $\triangle A B C$ 与 $\triangle D E F$ 的内心相同, 则

$$
M_{A B}+M_{B C}+M_{A C}=M_{D E}+M_{E F}+M_{D F} .
$$



故 $I_{A^{\prime}}=I_{D^{\prime}}$. 由公式 $O I^{2}=R^{2}-2 R r$, 知 $r_{A^{\prime}}=r_{D^{\prime}}$, 故 $\Delta_{A^{\prime}}, \Delta_{D^{\prime}}$ 共内接圆 $\omega^{\prime}$.于是, $\Omega_{A}, \omega_{A} ; \Omega_{D}, \omega_{D}$ 均与 $\Omega, \omega^{\prime}$ 位似. (a) 证毕!

我们接下来证明: $P_{A D}$ 在 $\Omega$ 和点圆 $I$ 的根轴上. 在图中,

$$
\frac{I A}{A I_{A}}=\frac{r}{r_{A}}, \frac{D I}{I I_{D}}=\frac{r}{r_{D}}, \frac{I_{A} P_{A D}}{P_{A D} I_{D}}=\frac{r_{A}}{r_{D}}
$$

对 $\triangle I I_{A} I_{D}$ 及割线 $A D P_{A D}$ 用梅涅劳斯逆定理, 得到 $A, D, P_{A D}$ 共线. 再对 $\triangle I A D$ 及割线 $I_{A} I_{D} P_{A D}$ 用梅涅劳斯定理, 有

$$
\frac{P_{A D} D}{P_{A D} A}=\frac{I_{A} I}{I_{A} A} \cdot \frac{I_{D} D}{I_{D} I}
$$

设 $A B, A C$ 与 $E F$ 交于 $J, K$, 过 $I, I_{A}$ 作 $A C$ 垂线, 垂足为 $M, L$. 我们有

$$
L M=J K=2 R_{A} \cdot \sin A .
$$

于是

$$
\begin{aligned}
\frac{I I_{A}}{A I_{A}} & =\frac{L M / \cos \frac{A}{2}}{r_{A} / \sin \frac{A}{2}} \\
& =\frac{2 R_{A} \sin A / \cos \frac{A}{2}}{r_{A} / \sin \frac{A}{2}} \\
& =\frac{4 R_{A} \sin ^{2} \frac{A}{2}}{r_{A}}=\frac{4 R_{A} \cdot r^{2}}{r_{A} \cdot A I^{2}} .
\end{aligned}
$$

故由 (1) 式,

$$
\frac{P_{A D} D}{P_{A D} A}=\left(\frac{D I}{A I}\right)^{2}
$$

由相似三角形结论, $P_{A D} I^{2}=P_{A D} A \cdot P_{A D} D$. 即 $P_{A D}$ 在 $\Omega$ 和 $I$ 的根轴上. 从而 (b) 证毕!

评注 本题很难, 第一问首先要精确作图猜到两组圆位似, 然后如果熟知内心可以理解为圆外切三角形的垂心从而写出内心对应复数坐标, 用它处理平行问题就变得非常简单. 第二问相对简单一些, 共线的结论是熟知的, 有非常非常多的证法, 我们选择了比较好写的一种. 本题体现了内心复数坐标在处理平移问题时的优越性。

题 7 设 $M$ 是由有限个格点组成的集合, $n$ 是正整数. 一条“安全路”被定义为从 $(0,0)$ 开始, 经历若干格点到 $x+y=n$ 上一格点结束, 且不经过一切 $M$ 中的点的长度为 $n$ 的路. 证明: 若存在安全路, 则至少有 $2^{n-|M|}$ 条.

证明 对 $n$ 归纳证明这一命题.

$n=1$ 时的结论平凡. 若 $n-1$ 成立, 来证 $n$ 时也成立. 由路的长度为 $n$, 则每次只能向上或向右. 我们进行如下讨论:

$1)$ 若第一步走到 $(0,1),(1,0)$ 时均存在安全路. 则由归纳假设, 两种的安全路条数不小于 $2^{n-1-|M|}$, 故总数不少于 $2^{n-|M|}$, 成立!

$2)$ 若仅有第一步走到 $(1,0)$ 时存在安全路. (若为 $(0,1)$ 则同理, 这里不再讨论 $)$ 由 $(0,1) \rightarrow(0,2) \rightarrow \cdots \rightarrow(0, n)$ 不是安全路, 则存在 $i$ 使得 $(0, i) \in M$.那么, 除去所有的 $(0, j)$ 后, 至多还剩下 $|M|-1$ 个在 $M$ 中的点. 由归纳假设,路径条数不少于 $2^{n-1-(|M|-1)}=2^{n-|M|}$. 也成立!

综上, 归纳得证.

评注 直接算也能做, 但归纳最好写.

题 $8 \triangle A B C$ 为不等边三角形. $A_{1}, B_{1}, C_{1}$ 分别在线段 $B C, C A, A B$ 上, 满足 $\triangle A_{1} B_{1} C_{1}$ 与 $\triangle A B C$ 对应相似. $A_{2}$ 是在 $B_{1} C_{1}$ 上满足 $A A_{2}=A_{1} A_{2}$ 的唯一一点, 类似定义 $B_{2}, C_{2}$. 证明: $\triangle A_{2} B_{2} C_{2}$ 与 $\triangle A B C$ 相似.

证明 1 设 $D, E, F$ 分别为 $B C, C A, A B$ 中点, $O$ 为 $\triangle A B C$ 外心. 我们先证明: $\triangle D E F(O)$ 与 $\triangle A_{1} B_{1} C_{1}(O)$ 相似. 显然 $\triangle D E F$ 与 $\triangle A_{1} B_{1} C_{1}$ 相似, 即需证 $O$ 在两个三角形内的相对位置相同.

设 $A_{1} B_{1}, B_{1} C_{1}$ 分别交 $D E$ 于 $U, V, B_{1} C_{1}, C_{1} A_{1}$ 交 $E F$ 于 $W, X, C_{1} A_{1}, A_{1} B_{1}$分别交 $F D$ 于 $Y, Z$. 由 $\angle F D E=\angle A=\angle A_{1}$, 故 $A_{1}, D, U, Y$ 共圆, 记此圆为 $\Gamma_{1}$;



类似定义 $\Gamma_{2}, \Gamma_{3}$.

对这三个圆用密克定理, 得到它们交于一点, 记为 $O^{\prime}$. 由 $C_{1}, F, Y, W$ 共圆,有

$$
\angle A_{1}=\angle B F D=\angle C_{1} W Y \text {. }
$$

同理, $\angle C_{1} Y W=\angle B_{1}, \angle B_{1} U W=\angle C_{1}$, 故 $U, V, W$ 分别为 $\triangle A_{1} B_{1} C_{1}$ 在三边的垂足, 从而 $O^{\prime}$ 是 $\triangle A_{1} B_{1} C_{1}$ 的垂心. 我们证明 $\triangle D E F$ 的垂心也是 $O^{\prime}$, 由熟知结论, 只需证明 $O=O^{\prime}$. 事实上,

$$
\angle O^{\prime} F C_{1}=\pi-\angle O^{\prime} W C_{1}=\frac{\pi}{2}=\angle O F C_{1},
$$

故 $O O^{\prime} F$ 共线. 同理 $O O^{\prime} D, O O^{\prime} E$ 也共线, 这证明了 $O=O^{\prime}$.

下一步, 我们来研究 $A_{2}, B_{2}, C_{2}$. 在 $B_{1} C_{1}$ 上取点 $A_{2}^{\prime}$ 使 $\frac{B_{1} A_{2}^{\prime}}{C_{1} A_{2}^{\prime}}=\frac{B A_{1}}{C A_{1}}$. 设 $K$ 为 $B_{1} C_{1}$ 中点, $O_{1}$ 为 $\triangle A_{1} B_{1} C_{1}$ 的外心, $A^{\prime}$ 为 $A$ 关于 $B_{1} C_{1}$ 的对称点. 则有 $A^{\prime} C_{1} B_{1} A_{1}$ 共圆且圆心为 $O_{1}$.

设

$$
\angle A_{1} O D=\angle B_{1} O E=\angle C_{1} O F=\angle A_{2}^{\prime} O_{1} K=\theta,
$$

则

$$
\begin{aligned}
\angle A^{\prime} A_{1} B & =\angle B A_{1} C_{1}-\angle A^{\prime} A_{1} C_{1}=(C+\theta)-\angle A^{\prime} B_{1} C_{1} \\
& =(C+\theta)-(C-\theta)=2 \theta .
\end{aligned}
$$

且

$$
<O_{1} A_{2}^{\prime}, D O>=<O_{1} K, D O>+\angle K O_{1} A_{2}^{\prime}=2 \theta
$$

又 $A_{1} B$ 与 $O D$ 垂直, 故 $A_{1} A^{\prime} \perp O_{1} A_{2}^{\prime}$, 有

$$
A_{2}^{\prime} A_{1}=A_{2}^{\prime} A^{\prime}=A_{2}^{\prime} A
$$

故 $A_{2}=A_{2}^{\prime}$. 从而 $\triangle A B C\left(A_{1}\right)$ 与 $\triangle A_{1} B_{1} C_{1}\left(A_{2}\right)$ 相似, $B_{2}, C_{2}$ 同理. 这说明了 $\triangle A_{2} B_{2} C_{2}$ 相似于 $\triangle A B C$ !

证明 2 我们证明 $\frac{C_{1} A_{2}}{B_{1} A_{2}}=\frac{C A_{1}}{B A_{1}}$. 若此式成立, 则同理有轮换的式子也成立,这样图形 $\triangle A B C, \triangle A_{1} B_{1} C_{1}$ 与图形 $\triangle A_{1} B_{1} C_{1}, \triangle A_{2} B_{2} C_{2}$ 相似, 故结论得证.

由余弦定理,

$$
\begin{gathered}
A_{1} A_{2}^{2}=C_{1} A_{1}^{2}+C_{1} A_{2}^{2}-2 C_{1} A_{1} \cdot C_{1} A_{2} \cos \angle A_{1} C_{1} B_{1} \\
A A_{2}^{2}=A C_{1}^{2}+C_{1} A_{2}^{2}-2 A C_{1} \cdot C_{1} A_{2} \cos \angle A C_{1} B_{1}
\end{gathered}
$$

由 $A_{1} A_{2}=A A_{2}$, 解得

$$
C_{1} A_{2}=\frac{A_{1} C_{1}^{2}-A C_{1}^{2}}{2 A_{1} C_{1} \cos \angle A_{1} C_{1} B_{1}-2 A C_{1} \cos \angle A C_{1} B_{1}}
$$

那么

$$
B_{1} A_{2}=B_{1} C_{1}-C_{1} A_{2}=\frac{A B_{1}^{2}-A_{1} B_{1}^{2}}{2 A_{1} C_{1} \cos \angle A_{1} C_{1} B_{1}-2 A C_{1} \cos \angle A C_{1} B_{1}},
$$

进而

$$
\frac{C_{1} A_{2}}{B_{1} A_{2}}=\frac{A_{1} C_{1}^{2}-A C_{1}^{2}}{A B_{1}^{2}-A_{1} B_{1}^{2}}
$$

我们证明右式恰等于 $\frac{C A_{1}}{B A_{1}}$.

由 $\frac{C_{1} B_{1}}{\sin A}=\frac{C_{1} B_{1}}{\sin \angle C_{1} A_{1} B_{1}}$ 知 $\triangle A C_{1} B_{1}, \triangle A_{1} C_{1} B_{1}$ 的外接圆半径相等. 同理, 可得 $\triangle A C_{1} B_{1}, \triangle B A_{1} C_{1}, \triangle C B_{1} A_{1}$ 的外接圆半径均与 $\triangle A_{1} C_{1} B_{1}$ 相等. 所以

$$
\frac{C A_{1}}{B A_{1}}=\frac{\sin \angle A_{1} B_{1} C_{1}}{\sin \angle B C_{1} A_{1}}=\frac{\sin \angle A B_{1} A_{1}}{\sin \angle A C_{1} A_{1}}
$$

又

$$
\begin{aligned}
\frac{A_{1} C_{1}^{2}-A C_{1}^{2}}{A B_{1}^{2}-A_{1} B_{1}^{2}} & =\frac{\sin ^{2} \angle A_{1} B_{1} C_{1}-\sin ^{2} \angle A B_{1} C_{1}}{\sin ^{2} \angle A C_{1} B_{1}-\sin ^{2} \angle A_{1} C_{1} B_{1}} \\
& =\frac{\sin \angle A B_{1} A_{1} \sin \left(B-\angle A_{1} B_{1} C_{1}\right)}{\sin \angle A C_{1} A_{1} \sin \left(\angle A C_{1} B_{1}-C\right)}
\end{aligned}
$$

其中最后一步用了平方差公式. 故只需证明

$$
\sin \left(B-\angle A_{1} B_{1} C_{1}\right)=\sin \left(\angle A C_{1} B_{1}-C\right)
$$

这由 $\angle A_{1} B_{1} C_{1}+\angle A C_{1} B_{1}=B+C=\pi-A$ 得证!

评注 本题的关键是发现 $\frac{C_{1} A_{2}}{B_{1} A_{2}}=\frac{C A_{1}}{B A_{1}}$. 我们给出的两种方法的核心都是在证明这个式子成立, 其中第一种使用了同一法, 第二种是偏向计算的方法.
题 9 令 $q=p^{r}$, 这里 $p$ 为质数且 $r$ 为正整数. 取 $\zeta=e^{\frac{2 \pi i}{q}}$. 求最小的正整数 $n$, 使得

$$
\sum_{1 \leq k \leq q, \operatorname{gcd}(k, p)=1} \frac{1}{\left(1-\zeta^{k}\right)^{n}}
$$

不是整数.

解 当 $(k, p)=1$ 时, $\zeta^{k}$ 是多项式 $x^{(p-1) p^{r-1}}+x^{(p-2) p^{r-1}}+\cdots+1$ 的根. 令 $y_{k}=\frac{1}{1-\zeta^{k}}$, 则 $\zeta^{k}=\frac{y_{k}-1}{y_{k}}$, 进而 $y_{k}$ 是多项式

$$
(x-1)^{(p-1) p^{r-1}}+(x-1)^{(p-2) p^{r-1}} x^{p^{r-1}}+\cdots+x^{(p-1) p^{r-1}}
$$

的根. 由牛顿恒等式, 有

$$
S_{k}-\sigma_{1} S_{k-1}+\sigma_{2} S_{k-2}+\cdots+(-1)^{k} k \sigma_{k}=0
$$

其中,

$$
S_{k}=\sum_{1 \leq i \leq q, \operatorname{gcd}(i, p)=1} y_{i}^{k}=\sum_{\omega \in \mathbf{S}_{q}} \frac{1}{(1-\omega)^{k}}
$$

其中 $\mathbf{S}_{q}$ 为所有 $q$ 阶本原单位根构成的集合. $\sigma_{k}$ 为 $\frac{a_{(p-1) p^{r-1}-k}}{a_{(p-1) p^{r-1}}}$, 其中 $a_{i}$ 是 $x^{i}$ 项的系数, 易得

$$
\sigma_{k}=\frac{1}{p} \sum_{t=0}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right)
$$

这里我们指出, 该多项式实际上是分圆多项式.

因此, 当 $p^{r-1} \nmid k$ 时, $p \left\lvert\,\left(\begin{array}{c}t p^{r-1} \\ k\end{array}\right)\right.$ 对 $t=0,1, \cdots, p-1$ 成立, 此时 $\sigma_{k} \in \mathbb{Z}$. 否则, 我们有

$$
\begin{aligned}
\sum_{t=0}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right) & \equiv \sum_{t=0}^{p-1}\left(\begin{array}{c}
t \\
k / p^{r-1}
\end{array}\right) \\
& \equiv \sum_{t=0}^{p-1}\left(\left(\begin{array}{c}
t+1 \\
k / p^{r-1}+1
\end{array}\right)-\left(\begin{array}{c}
t \\
k / p^{r-1}+1
\end{array}\right)\right) \\
& \equiv\left(\begin{array}{c}
p \\
k / p^{r-1}+1
\end{array}\right)(\bmod p),
\end{aligned}
$$

它在 $k \neq(p-1) p^{r-1}$ 时是 $p$ 的倍数, 否则模 $p$ 余 1 . 故 $\sigma_{k} \in \mathbb{Z}$ 当且仅当 $k \neq$ $(p-1) p^{r-1}$. 若定义 $v_{p}(x / y)=v_{p}(x)-v_{p}(y), x, y \in \mathbb{Z}$ 则可知 $v_{p}\left(\sigma_{(p-1) p^{r-1}}\right)=-1$.设 $k_{i}$ 是最小的使得 $v_{p}\left(S_{k}\right)=i$ 的正整数 $k$, 其中 $i \in \mathbb{Z}$.

若 $k_{i}$ 存在, 且 $i \leq r-2$. 我们说明 $k_{i-1}=k_{i}+\varphi(q)$. 若 $v_{p}\left(S_{k_{i}+t}\right) \geq i$, 其中 $t$是正整数, 则 $t \leq \varphi(q)-1$ 时, 由 (2) 式,

$$
v_{p}\left(S_{k_{i}+t+1}\right)=v_{p}\left(\sigma_{1} S_{k_{i}+t-1}-\cdots+(-1)^{\varphi(q)+1} \sigma_{\varphi(q)} S_{k_{i}+\varphi(q)-t+1}\right.
$$

$$
\left.+\cdots+(-1)^{k_{i}+t}\left(k_{i}+t+1\right) \sigma_{k_{i}+t+1}\right)
$$

注意到, 对于正整数 $k$, 若 $v_{p}(k) \leq r-1$, 我们有

$$
v_{p}\left(\sigma_{k}\right)=v_{p}\left(\sum_{t=0}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right)\right) \geq r-v_{p}(k)-2
$$

故 $v_{p}(k \sigma k) \geq r-2$, 且若 $v_{p}(k) \geq r$, 同样有 $v_{p}(k \sigma k) \geq r-2$ 成立. 故

$$
v_{p}\left(\left(k_{i}+t+1\right) \sigma_{k_{i}+t+1}\right) \geq r-2 \text {, }
$$

逐项分析得

$$
v_{p}\left(S_{k_{i}+t+1}\right)\left\{\begin{array}{ll}
\geq i & t+1<\varphi(q) \\
=i-1 & t+1=\varphi(q)
\end{array},\right.
$$

这就证明了 $k_{i-1}=k_{i}+\varphi(q)$ !

若 $i=r-1$, 且 $k_{r-1}=1$. 我们先证明两个引理.

引理 1 设 $a, b \in N$ 满足 $a>0, a \geq b, v_{p}\left(\left(\begin{array}{c}a p \\ b p\end{array}\right)\right)=v$. 则

证明 此处注意到

$$
\left(\begin{array}{l}
a p \\
b p
\end{array}\right) \equiv\left(\begin{array}{l}
a \\
b
\end{array}\right) \quad\left(\bmod p^{v+1}\right)
$$

$$
\left(\begin{array}{l}
a p \\
b p
\end{array}\right)=\frac{a !}{b !(a-b) !} \prod_{k=1}^{a} T_{k}\left(\prod_{k=1}^{b} T_{k}\right)^{-1}\left(\prod_{k=1}^{a-b} T_{k}\right)^{-1}
$$

其中 $T_{k}=(k p-1) \cdots(k p-p+1) \equiv-1(\bmod p)$. 因此,

引理1 证毕!

$$
\left(\begin{array}{c}
a p \\
b p
\end{array}\right) \equiv\left(\begin{array}{l}
a \\
b
\end{array}\right) \frac{(-1)^{a}}{(-1)^{b}(-1)^{a-b}} \equiv\left(\begin{array}{l}
a \\
b
\end{array}\right) \quad(\bmod p) .
$$

引理 2 当 $k \leq(p-2) p^{r-1}$ 且 $p \nmid k$ 时,

$$
p^{r} \left\lvert\, \sum_{t=1}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right)\right.
$$

证明 设 $k-1=\left(K_{r-1} K_{r-2} \cdots K_{0}\right)_{p}$. 由卢卡斯定理,

$$
\begin{aligned}
\sum_{t=1}^{p-1} t\left(\begin{array}{c}
t p^{r-1}-1 \\
k-1
\end{array}\right) & \equiv \sum_{t=1}^{p-1} t\left(\begin{array}{c}
t-1 \\
K_{r-1}
\end{array}\right) \cdot\left(\begin{array}{c}
p-1 \\
K_{r-2}
\end{array}\right) \cdots\left(\begin{array}{c}
p-1 \\
K_{0}
\end{array}\right) \\
& \equiv K_{r-1} \cdot(-1)^{K_{0}+\cdots+K_{r-2}} \cdot \sum_{t=1}^{p-1}\left(\begin{array}{c}
t \\
K_{r-1}+1
\end{array}\right) \\
& \equiv K_{r-1} \cdot(-1)^{K_{0}+\cdots+K_{r-2}}\left(\begin{array}{c}
p \\
K_{r-1}+2
\end{array}\right),
\end{aligned}
$$

由条件知: 若 $r=1$, 则

$$
\sum_{t=1}^{p-1}\left(\begin{array}{l}
t \\
k
\end{array}\right)=\left(\begin{array}{c}
p \\
k+1
\end{array}\right) \equiv 0 \quad(\bmod p)
$$

若 $r \geq 2$, 则 $K_{r-1} \leq p-3$, 有

$$
\sum_{t=1}^{p-1} t\left(\begin{array}{c}
t p^{r-1}-1 \\
k-2
\end{array}\right) \equiv K_{r-1}(-1)^{K_{0}+\cdots+K_{r-2}}\left(\begin{array}{c}
p \\
K_{r-1}+2
\end{array}\right) \equiv 0 \quad(\bmod p) .
$$

故

$$
\sum_{t=1}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right)=\sum_{t=1}^{p-1} \frac{t p^{r-1}}{k}\left(\begin{array}{c}
t p^{r-1} \\
k-1
\end{array}\right) \equiv 0 \quad\left(\bmod p^{r}\right)
$$

引理 2 证毕!

回到原题. 由两个引理, 对于任意 $k \leq(p-2) p^{r-1}$, 设 $v_{p}(r)=s$, 则

$$
\sum_{t=1}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right) \equiv \sum_{t=1}^{p-1}\left(\begin{array}{c}
t p^{r-s-1} \\
k / p^{s}
\end{array}\right) \equiv 0 \quad\left(\bmod p^{r-s}\right)
$$

又 $p^{s} \mid r$, 故

$$
v_{p}\left(k \sigma_{k}\right)=v_{p}\left(k \cdot \frac{1}{p} \sum_{t=1}^{p-1}\left(\begin{array}{c}
t p^{r-1} \\
k
\end{array}\right)\right) \geq r-s+s-1=r-1,
$$

知当 $2 \leq k \leq(p-2) p^{r-1}+1$ 时

$$
S_{k}=\sigma_{1} S_{k-1}-\sigma_{2} S_{k-2}+\cdots+(-1)^{k-1} k \sigma_{k}
$$

又 $\sigma_{t} \in \mathbb{Z}$ 对任意 $t<(p-1) p^{r-1}$ 成立, 故 $v_{p}\left(S_{k}\right) \geq r-1$ 当且仅当 $v_{p}\left(k \sigma_{k}\right) \geq$ $r-1$. 当 $k=(p-2) p^{r-1}+1$ 时, 容易验证成立. 又由 (6), 知 $v_{p}\left(k \sigma_{k}\right)$ 仅当 $k=(p-2) p^{r-1}+1$ 时为 $r-2$ 其余均 $\geq r-1$, 故 $k_{r-2}=(p-2) p^{r-1}+1$.

又 $S_{1}=\sigma_{1}=\frac{1}{2} p^{r-1}(p-1)$, 故当 $p \geq 3$ 时 $k_{r-1}=1$, 在 $p=2$ 时 $k_{r-2}=1$. 所以,

$$
k_{-1}= \begin{cases}(r-1) 2^{r-1}+1 & p=2 \\ (r p-r-1) p^{r-1}+1 & p \geq 3\end{cases}
$$

两种情况可以合并为: $k_{-1}=(r p-p-1) p^{r-1}+1$. 又显然若 $S_{k} \notin \mathbb{Z}$ 则存在 $t \in \mathbb{N}^{+}$满足 $p^{t} S_{k} \in \mathbb{Z}$, 故最小的 $n$ 即为 $k_{-1}=(r p-r-1) p^{r-1}+1$.

评注 本题总体思路相对自然, 思考的难度不是很大. 不过细节较多, 尤其是大多数人计算方程系数时只会考虑是否是整数, 到最后才会发现需要研究具体的含质数幂次, 这样又得重新计算, 我们认为在考试时间限制的情况下并不容易做出. 作为参考, 考试时恰 4 位美国学生做出.

