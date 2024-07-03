数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2017 年春季上海新星数学奥林匹克试题解析 

吴尉迟 ${ }^{1}$ 赵岩 $^{1}$ 施柯杰 $^{2}$

(1. 上海大学数学系, 200444；2. 复旦大学附属中学, 200433)

题 1. 令 $|S|=n$, 对固定的正整数 $k$, 求由 $S$ 的子集 $T_{i}$ 构成的序列 $\left(T_{1}, T_{2}, \cdots, T_{k}\right)$ 的个数, 其中要求 $T_{1} \subseteq T_{2} \subseteq \cdots \subseteq T_{k}$.

(上海大学 冷岗松 供题)

解 对一个满足要求的序列 $\left(T_{1}, T_{2}, \ldots, T_{k}\right)$, 约定 $T_{k+1}=S$, 则对 $\forall x \in S$, 可取出 $i_{x}$ 为最小的下标 $i$ 使得 $x \in T_{i}\left(1 \leq i_{x} \leq k+1\right)$. 而由 $T_{i_{x}} \subseteq T_{i_{x+1}} \subseteq \cdots \subseteq$ $T_{k} \subseteq T_{k+1}$ 知 $x \in T_{j}$, 这里 $i_{x} \leq j \leq k+1$. 由 $i_{x}$ 的最小性知对任何 $1 \leq j \leq i_{x}$ 均有 $x \notin T_{j}$.

也就说, $x$ 在 $T_{1}, T_{2}, \ldots, T_{k}$ 中的归属由 $i_{x}$ 唯一确定, 所以 $\left(T_{1}, T_{2}, \ldots, T_{k}\right)$ 与 $\left\{i_{x}\right\}_{x \in S}$ 一一对应. 而 $\left\{i_{x}\right\}_{x \in S}$ 的种数为 $(k+1)^{n}$, 这是因为 $i_{x}$ 有 $k+1$ 种可能的取法, 故满足要求的 $\left(T_{1}, T_{2}, \ldots, T_{k}\right)$ 有 $(k+1)^{n}$ 种.

评注 本题源于 “计数组合学” 一书. 该题的做法是考查各个元素的 “归属”。证明:

题 2. 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是实数, 对 $1 \leq k \leq n$, 记 $\sigma_{k}=\sum_{1 \leq i_{1}<i_{2}<\cdots<i_{k} \leq n} x_{i_{1}} x_{i_{2}} \cdots x_{i_{k}}$.

$$
\prod_{k=1}^{n}\left(x_{k}^{2}+1\right) \geq 2\left|\sum_{k=0}^{\left[\frac{n}{2}\right]}(-1)^{k} \sigma_{2 k}\right| \cdot\left|\sum_{k=0}^{\left[\frac{n-1}{2}\right]}(-1)^{k} \sigma_{2 k+1}\right|
$$

其中 $\sigma_{0}=1$.

(中国人民大学附属中学 张端阳 供题)

证明 记 $f(x)=\prod_{k=1}^{n}\left(x+x_{k}\right)$, 则由定义,

$$
f(x)=x^{n}+\sigma_{1} x^{n-1}+\sigma_{2} x^{n-2}+\cdots+\sigma_{n} .
$$

收稿日期: 2017-04-25; 修订日期: 2017-05-16.
设 $f(i)=A+B i$, 其中 $i$ 是虚数单位, $A, B$ 是实数. 则

$$
\begin{gathered}
\prod_{k=1}^{n}\left(x_{k}^{2}+1\right)=A^{2}+B^{2} \\
\left|\sum_{k=0}^{\left[\frac{n}{2}\right]}(-1)^{k} \sigma_{2 k}\right| \cdot\left|\sum_{k=0}^{\left[\frac{n-1}{2}\right]}(-1)^{k} \sigma_{2 k+1}\right|=|A B| .
\end{gathered}
$$

由 $(|A|-|B|)^{2} \geq 0$ 即知欲证不等式成立.

评注 本题实际上考查的下述恒等式:

$$
\prod_{k=1}^{n}\left(x_{k}^{2}+1\right)=\left(\sum_{k=0}^{\left[\frac{n}{2}\right]}(-1)^{k} \sigma_{2 k}\right)^{2}+\left(\sum_{k=0}^{\left[\frac{n-1}{2}\right]}(-1)^{k} \sigma_{2 k+1}\right)^{2}
$$

本题也可以用归纳法证明，借助多项式证明简洁且本质.

题 3. 设 $A_{1} A_{2} A_{3} A_{4}$ 为 $\odot O$ 的内接矩形, $B_{i}$ 是劣弧 $\overparen{A}_{i} A_{i+1}$ 上的一点, $i=$ $1,2,3,4$, 其中 $A_{5}=A_{1}$ 且 $B_{1} B_{3} / / A_{1} A_{4}, B_{2} B_{4} / / A_{1} A_{2}$, 并设 $\triangle A_{i} B_{i+1} B_{i+2}$ 的垂心为 $H_{i}, i=1,2,3,4$, 其中 $B_{5}=B_{1}, B_{6}=B_{2}$. 证明: $H_{1} H_{2} H_{3} H_{4}$ 为矩形.

(湖南雅礼中学 尹龙晖 供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_63b79507fd519bff97feg-2.jpg?height=488&width=491&top_left_y=1412&top_left_x=788)

证明 我们证明 $H_{1} H_{2} / / A_{1} A_{2}$. 记 $O$ 为该圆圆心, $O$ 到直线 $A_{1} B_{2}, A_{2} B_{4}$ 的距离分别为 $d_{1}, d_{2}$. 由垂外心定理得,

$$
B_{3} H_{1}=2 d_{1}, B_{3} H_{2}=2 d_{2} .
$$

由于 $B_{2} B_{4} / / A_{1} A_{2}$, 故 $d_{1}=d_{2}$, 从而 $B_{3} H_{1}=B_{3} H_{2}$.

由 $B_{3} H_{1} \perp A_{1} B_{2}$, 得

$$
\begin{aligned}
\angle H_{1} B_{3} B_{1} & =\angle B_{1} B_{3} B_{2}-\angle H_{1} B_{3} B_{2} \\
& =\angle B_{1} B_{3} B_{2}-\left(90^{\circ}-\angle A_{1} B_{2} B_{3}\right) \\
& =\angle B_{1} B_{3} B_{2}+\angle A_{1} B_{2} B_{3}-90^{\circ}
\end{aligned}
$$

又由于 $B_{4} B_{2} \perp B_{1} B_{3}$, 故 $\angle B_{1} B_{3} B_{2}+\angle B_{4} B_{2} B_{3}=90^{\circ}$, 故 $\angle H_{1} B_{3} B_{1}=\angle A_{1} B_{2} B_{4}$.同理 $\angle H_{2} B_{3} B_{1}=\angle A_{2} B_{4} B_{2}$.

而 $A_{1} A_{2} \perp B_{4} B_{2}$ 且内接于圆 $O$, 故 $\angle A_{1} B_{2} B_{4}=\angle A_{2} B_{4} B_{2}$, 故 $\angle H_{3} B_{3} B_{1}=$ $\angle H_{2} B_{3} B_{1}$, 结合 $B_{3} H_{1}=B_{3} H_{2}$ 知 $B_{1} B_{3}$ 为 $\triangle B_{3} H_{1} H_{2}$ 中 $\angle H_{1} B_{3} H_{2}$ 的平分线, 则 $B_{1} B_{3} \perp H_{1} H_{2}$, 故 $H_{1} H_{2} / / A_{1} A_{2}$.

同理得到其余三组平行, 故 $H_{1} H_{2} H_{3} H_{4}$ 为矩形.

评注通过垂外心定理和 “导角” 可以得出 $H_{1} H_{2} / / A_{1} A_{2}$, 进而得出了 $H_{1} H_{2} H_{3} H_{4}$ 为矩形. 此题也可以圆点为原点, 以 $B_{1} B_{3}$ 为正方向建系用复数方法解。

题 4. 设 $k, n$ 是正整数, $1 \leq k \leq n-2, n \geq 4, X(k, n)=\{k, k+1, k+2 \ldots, n\}$,对于 $X(k, n)$ 中的三元数组 $(a, b, c), k \leq a<b<c \leq n$, 如果 $a+b>c$, 则称之为 “好的” , 否则称为 “坏的” . 如果 $X(k, n)$ 中好的三元数组与坏的三元数组一样多,则称 $X(k, n)$ 是 “均衡集” 。问: 是否存在均衡集? 若存在, 求出所有均衡集; 若不存在, 请说明理由.

(上海大学 吴尉迟, 深圳高级中学 冯跃峰 供题)

解法一 不存在.

记 $B(n, k), A(n, k)$ 分别是 $X(n, k)$ 中所有坏三数组和好三数组组成的集合.

i) 对于给定的 $n$, 若 $k>\frac{n-1}{2}$, 则对于满足 $k \leq a<b<c \leq n$ 的三数组 $(a, b, c)$, 有 $a+b>\frac{n-1}{2}+\frac{n+1}{2}=n \geq c$, 此时 $X(k, n)$ 不存在坏三数组.

ii) 当 $k \leq\left[\frac{n-1}{2}\right]$ 时, 设 $(a, b, c)$ 是坏三数组. 我们先证明 $a \leq\left[\frac{n-1}{2}\right]$. 若不然,则有 $a>\frac{n-1}{2}$, 从而 $b \geq \frac{n-1}{2}+1=\frac{n+1}{2}$, 故我们有 $a+b>\frac{n-1}{2}+\frac{n+1}{2}=n \geq c$, 这与 $(a, b, c)$ 是坏三数组矛盾. 另一方面, 当 $a=i \leq\left[\frac{n-1}{2}\right]$ 时, $(a, b, c)$ 共有如下几种情形:

$$
\begin{array}{r}
(i, i+1,2 i+1)(i, i+1,2 i+2) \cdots(i, i+1, n) \\
(i, i+2,2 i+2) \cdots(i, i+2, n) \\
\vdots \\
(i, i+(n-2 i), n)
\end{array}
$$

一共有 $(n-2 i)+(n-2 i-1)+\cdots+1=\left(\begin{array}{c}n-2 i+1 \\ 2\end{array}\right)$ 种可能. 从而

$$
|B(n, k)|=\sum_{i=k}^{\left[\frac{n-1}{2}\right]}\left(\begin{array}{c}
n-2 i+1 \\
2
\end{array}\right)
$$

进而我们有

$$
\begin{aligned}
|B(n, k)|+|B(n+1, k)| & =\sum_{i=k}^{\left[\frac{n-1}{2}\right]}\left(\begin{array}{c}
n-2 i+1 \\
2
\end{array}\right)+\sum_{i=k}^{\left[\frac{n}{2}\right]}\left(\begin{array}{c}
n-2 i+2 \\
2
\end{array}\right) \\
& =\sum_{i=1}^{n-2 k+1}\left(\begin{array}{c}
i+1 \\
2
\end{array}\right) \\
& =\left(\begin{array}{c}
n+3-2 k \\
3
\end{array}\right) .
\end{aligned}
$$

注意到

$$
\begin{gathered}
|A(n+1, k)|+|B(n+1, k)|=\left(\begin{array}{c}
n+2-k \\
3
\end{array}\right) . \\
|A(n, k)|+|B(n, k)|=\left(\begin{array}{c}
n+1-k \\
3
\end{array}\right) .
\end{gathered}
$$

故我们有

$$
\begin{aligned}
& |A(n+1, k)|-|B(n, k)|=\left(\begin{array}{c}
n+2-k \\
3
\end{array}\right)-\left(\begin{array}{c}
n+3-2 k \\
3
\end{array}\right) . \\
& |A(n, k)|-|B(n+1, k)|=\left(\begin{array}{c}
n+1-k \\
3
\end{array}\right)-\left(\begin{array}{c}
n+3-2 k \\
3
\end{array}\right) .
\end{aligned}
$$

从而当 $k=1$ 时, $|A(n+1, k)|=|B(n, k)|$; 当 $k \geq 2$ 时, $|A(n, k)| \geq|B(n+1, k)|$.

又由于当 $k \leq\left[\frac{n-1}{2}\right]$ 时, $A(n, k), B(n, k)$ 关于 $n$ 严格递增, 故当 $k=1$ 时,

$$
|A(n, k)|<|A(n+1, k)|=|B(n, k)|
$$

当 $k \geq 2$ 时,

$$
|A(n, k)| \geq|B(n+1, k)|>|B(n, k)| .
$$

结合 i) 和 ii) 两种情形可知, 不存在均衡集.

解法二 不存在. 以下分三种情况说明:

I）当 $k=1$ 时, 我们证明坏数组比好数组多.

对于一个好集中的三元数组 $(a, b, c)$, 即有 $a+b>c$, 我们定义从好数组到坏数组的映射:

$$
f((a, b, c))=(c-b, c-a, c),
$$

由 $a+b>c$ 知: $(c-b)+(c-a)<c$, 故 $(c-b, c-a, c)$ 是坏三元数组. 由于映射 $f$ 是一一映射, 故好集与坏集的一个真子集一一对应(因为满足 $a+b=c$ 的坏三元数组 $(a, b, c)$ 没有与之对应的好三原数组), 从而坏数组比好数组多.

II) 当 $k>\frac{n-1}{2}$, 则对于满足 $k \leq a<b<c \leq n$ 的三数组 $(a, b, c)$, 有 $a+b>\frac{n-1}{2}+\frac{n+1}{2}=n \geq c$, 此时不存在坏三数组. 此时好数组比坏数组多.

III）当 $1<k \leq\left[\frac{n-1}{2}\right]$ 时, 对于一个坏数组 $(a, b, c)$, 即有 $k \leq a<b<c \leq$ $n, a+b \leq c$. 我们定义从坏数组到好数组的映射:

$$
g((a, b, c))=(c-b+1, c-a+1, c) .
$$

由 $k \leq a<b<c \leq n, a+b \leq c$ 知

$$
c-b+1>a \geq k,(c-b+1)+(c-a+1)>c .
$$

所以 $(c-b+1, c-a+1, c)$ 是好三元数组. 注意到

$$
g((k, n-k+1, n))=(k, n-k+1, n)
$$

故好三元组 $(k, n-k+1, n)$ 没有坏三元组与之对应, 又由于 $g$ 是一一映射, 故此时, 好数组比坏数组多. 结合 I), II) 和 III) 三种情形可知, 不存在均衡集.

评注 此题可以从两方面思考这个题, 一是通过计数来做, 这样做难点在于计算量大, 解法一通过观察 $|B(n, k)|+|B(n+1, k)|=\left(\begin{array}{c}n+3-2 k \\ 3\end{array}\right)$ 这一关键等式简化了运算. 此题也可以直接算坏数组的个数, 事实上当 $k \leq\left[\frac{n-1}{2}\right]$ 时坏集的个数有如下公式:

$$
B(n, k)= \begin{cases}\frac{(n-2 k+1)(n-2 k+3)(2 n-4 k+1)}{24}, & n \text { 为奇数 } \\ \frac{(n-2 k)(n-2 k+2)(2 n-4 k+5)}{24}, & n \text { 为偶数 }\end{cases}
$$

然后与好数组和坏数组总数的一半 $\frac{1}{2}\left(\begin{array}{c}n-k+1 \\ 3\end{array}\right)$ 比较也可以得出结论.

二是通过构造一一映射来规避复杂的运算, 当然构造映射的方法并不唯一,这样做的难点在于要分情况讨论构造两个映射。

题 5. 求所有满射 $f: \mathbf{N}^{*} \rightarrow \mathbf{N}^{*}$, 满足: 对任意的正整数 $i, j, i \neq j$, 有

$$
\frac{1}{2}(i, j)<(f(i), f(j))<2(i, j)
$$

其中 $(a, b)$ 表示 $a, b$ 的最大公约数.

(北京大学 吴茁 供题)

解 解为 $f(n)=n$,

I) 先给出两个性质:

性质 1. 分别令 $(i, j)=1$ 和 $(f(i), f(j))=1$, 可得 $(i, j)=1$ 与 $(f(i), f(j))=$ 1 等价.

若 $f(1) \neq 1$, 则令 $f(j)=2 f(1)$, 此时 $(f(1), f(j)) \neq 1$ 但 $(1, j)=1$, 与性质 1 矛盾, 故 $f(1)=1$.

性质 2. 令 $i=1$, 有 $\frac{i}{2}<f(i)<2 i$.

II) 我们证明 $f(2)=2, f(3)=3, f(5)=5, f(7)=7$.

若 $f(2) \neq 2$, 则由性质 2 知 $f(2)=3, f(3)=2$, 设 $f(k)=4$, 则由性质 1,2 知 $k<8,2 \nmid k, 3 \mid k$, 矛盾, 故 $f(2)=2$.

若 $f(3) \neq 3$, 由 $f(2)=2$ 和性质 1,2 知 $f(3)=5$, 进而 $f(5)=3$. 设 $f(k)=9$,则由性质 1,2 知 $k<18,2 \nmid k, 3 \nmid k, 5 \mid k$, 矛盾, 故 $f(3)=3$.

若 $f(5) \neq 5$, 则由性质 1,2 知 $f(7)=5$. 设 $f(k)=25$, 则由性质 1,2 知 $k<50,2 \nmid k, 3 \nmid k, 5 \nmid k$, 从而 $k=49$. 设 $f(m)=125$, 则由性质 1,2 知 $49 \mid m, 2 \nmid m, 3 \nmid m, 5 \nmid m$, 从而 $m \geq 49 \times 7>250$, 矛盾, 所以 $f(5)=5$.

若 $f(7) \neq 7$, 设 $f(r)=49$, 则由性质 1,2 知 $2 \nmid r, 3 \nmid r, 5 \nmid r, 7 \nmid r$. 所以 $r \geq 121$, 矛盾! 故 $f(7)=7$.

III) 证明 $f(p)=p, p$ 为任意正素数.

设素数从小到大为 $p_{1}<\cdots<p_{n}<\cdots$, 对 $n$ 归纳. $n \leq 4$ 已经在 II) 证明.设 $n \leq k$ 时成立. 当 $n=k+1$, 设 $f\left(p_{k+1}\right)=r$.

(1) 若 $r$ 为合数, 它有小于 $p_{k+1}$ 的素因子 $d$, 则由 $p_{k+1}$ 是素数知 $\left(d, p_{k+1}\right)=1$但 $\left(f(d), f\left(p_{k+1}\right)\right) \neq 1$, 矛盾.

(2) 若 $r$ 为素数, 对 $m$ 归纳证明: $f\left(p_{k+1}^{m}\right)=r^{m}$.

当 $m=1$ 成立. 设 $m \leq l$ 时成立.

则当 $m=l+1$ 时, 取 $d$ 使得 $f(d)=r^{l+1}$. 若 $d$ 有素因子 $k_{0} \neq p_{k+1}$, 则 $\left(k_{0}, p_{k+1}\right)=1$. 故 $\left(f\left(k_{0}\right), f\left(p_{k+1}\right)\right)=1$, 进而 $\left(f\left(k_{0}\right), r\right)=1,\left(f\left(k_{0}\right), r^{l+1}\right)=1$, 于是 $\left(f\left(k_{0}\right), f(d)\right)=1$, 矛盾. 故 $d$ 为 $p_{k+1}$ 的幂次. 由于 $p_{k+1}^{l}>\frac{1}{2} r^{l}$, 所以

$$
p_{k+1}^{l+2}>\frac{1}{2} r^{l} p_{k+1}^{2}>\frac{1}{4} r^{l+1} p_{k+1}>2 r^{l+1}
$$

故 $d$ 仅能为 $p_{k+1}^{l+1}$. 那么 $\frac{1}{2}<\left(\frac{p_{k+1}}{r}\right)^{m}<2$ 恒成立. 这就推得 $r=p_{k+1}$.

VI) 证明 $f\left(p^{n}\right)=p^{n}, p$ 为任意素数, $n \in \mathbf{N}_{+}$.

$p \neq 2,3,5,7$ 时, 由步骤三中证明立即可见.

$p=2,3,5,7$ 时, 前面仍正确, 即有 $f\left(p^{n}\right)$ 仍是 $p$ 的幂次. 此时由于 $f(p)=p$,由性质 2 知 $f\left(p^{n+l}\right)=p^{n+1}$ 仅能在 $l=1$ 时成立. 故也可推得 $f\left(p^{n}\right)=p^{n}$.

V) 证明 $f(x)=x, x \in \mathbf{N}_{+}$.

若 $x$ 为素数幂, 已证. 否则, 设 $x=\prod_{i=1}^{n} p_{i}^{\alpha_{i}},\left(f(x), f\left(p_{i}^{\alpha_{i}}\right)\right)>\frac{1}{2} p_{i}^{\alpha_{i}}$. 所以 $p_{i}^{\alpha_{i}} \mid f(x)$. 乘起来即 $x \mid f(x)$, 而 $f(x)<2 x$, 所以 $f(x)=x$.

评注 以下摘自出题人: 答案平凡. 步骤I) 易于发现. 但性质 1 无法保证原结果 (如 $x=2^{\alpha} 3^{\beta} p$, 则 $f(x)=3^{\alpha} 2^{\beta} p$ ), 故必须利用不等式. 从单射入手是一个
办法. 简单的放缩之后, 可以得到的仅有 $f(a x)=f(b x)((a, b) \in\{1,2,3\})$ 这三种情况. 这并不好使, 虽然研究 $f\left(2^{l}\right), f\left(3^{l}\right)$ 可以给出单射, 但是单射并不能给出太多用处. 利用归纳法, 可以化归为素数幕. 事实上, $x=p^{\alpha} q^{\beta} l, f(x)=q^{\alpha} p^{\beta} l,(p, q$互素, $(l, p)=(l, q)=1$.) 是一个解, 它满足性质 1 . 它促使我们考虑素数幂, 即 $f(p)=q$ 时, 考察 $f\left(p^{n}\right)$ 来放 $\left(\frac{p}{q}\right)^{n}$. 直接考察 $f\left(p^{n}\right)$ 和考察 $f(t)=p^{n}$ 应该都能做.上面的解答在放缩时, 先单独讨论了 $p \leq 7$, 这里面可能有更精确的估计, 但是 $p \leq 7$ 的情形讨论起来并不麻烦.

题 6. 设 $p$ 为素数, $S_{r}=1+2+\cdots+r(r=1,2, \cdots)$.

(1) 证明: 对任意正偶数 $c$, 不存在正整数对 $(m, n)$, 使得 $\frac{S_{m}}{S_{n}}=p^{c}$;

(2) 证明: 对任意正奇数 $c$, 存在无穷多个正整数对 $(m, n)$, 使得 $\frac{S_{m}}{S_{n}}=p^{c}$.

(华东师范大学 何忆捷 供题)

证明 (1) 设正偶数 $c=2 l$, 则 $\frac{S_{m}}{S_{n}}=p^{c} \Leftrightarrow m(m+1)=p^{2 l} n(n+1)$.

假设正整数对 $(m, n)$ 满足上述条件. 由于 $m, m+1$ 互素, 所以 $p^{2 l} \mid m$ 或 $p^{2 l} \mid m+1$.

若 $p^{2 l} \mid m$, 设 $m=p^{2 l} x$, 则 $p^{2 l} x \cdot\left(p^{2 l} x+1\right)=p^{2 l} n(n+1)$, 这等价于

$$
n-x=p^{2 l} x^{2}-n^{2}=\left(p^{l} x+n\right)\left(p^{l} x-n\right) .
$$

显然 $p^{l} x-n \neq 0$ (否则, 代入 (1) 又得 $n-x=0$, 从而 $p^{l} x=x$, 这不可能), 所以由 (1) 知,

$$
|n-x|=\left(p^{l} x+n\right)\left|p^{l} x-n\right| \geq\left(p^{l} x+n\right) \cdot 1>x+n>|n-x|,
$$

矛盾.

若 $p^{2 l} \mid m+1$, 设 $m+1=p^{2 l} x$, 则 $\left(p^{2 l} x-1\right) \cdot p^{2 l} x=p^{2 l} n(n+1)$, 这等价于

$$
n+x=\left(p^{l} x+n\right)\left(p^{l} x-n\right) .
$$

类似地, 易知 $n+x \geq\left(p^{l} x+n\right) \cdot 1>n+x$, 仍矛盾.

从而满足条件的正整数对 $(m, n)$ 不存在.

(2) 记 $k=p^{c}$. 由于

$$
\frac{S_{m}}{S_{n}}=p^{c} \Leftrightarrow m(m+1)=k n(n+1) \Leftrightarrow(2 m+1)^{2}-1=k\left((2 n+1)^{2}-1\right) .
$$

令 $a=2 m+1, b=2 n+1$. 则 $\frac{S_{m}}{S_{n}}=p^{c}$ 等价于

$$
a^{2}-k b^{2}=1-k,
$$

其中 $a, b$ 是大于 1 的奇数.

当 $c$ 为奇数时, $k$ 不是完全平方数. 我们证明此时方程 (2) 有无穷多组奇数
解 $(a, b)$.

熟知 Pell 方程

$$
u^{2}-k v^{2}=1
$$

存在无穷多组正整数解. 记 (3) 的任意一组解为 $(u, v)$, 并设

$$
\left(a_{0}, b_{0}\right)=(1,1),\left\{\begin{array}{l}
a_{t+1}=u a_{t}+k v b_{t}, \\
b_{t+1}=v a_{t}+u b_{t},
\end{array} \quad t=0,1,2, \cdots,\right.
$$

则易验证 $\left(a_{t}, b_{t}\right)(t=0,1, \cdots)$ 均为 (2) 的正整数解, 其中 $a_{0}<a_{1}<a_{2}<\cdots$, $b_{0}<b_{1}<b_{2}<\cdots$.

下证对一切正偶数 $t, a_{t}, b_{t}$ 均为大于 1 的奇数.

事实上, 反复利用 (4) 可得

$$
\left\{\begin{array}{l}
a_{t+2}=u a_{t+1}+k v b_{t+1}=\left(u^{2}+k v^{2}\right) a_{t}+2 k u v b_{t} \\
b_{t+2}=v a_{t+1}+u b_{t+1}=2 u v a_{t}+\left(u^{2}+k v^{2}\right) b_{t}
\end{array}\right.
$$

注意到 $u^{2}+k v^{2} \equiv u^{2}-k v^{2}=1(\bmod 2)$, 所以

$$
a_{t+2} \equiv a_{t} \quad(\bmod 2), \quad b_{t+1} \equiv b_{t} \quad(\bmod 2)
$$

又 $\left(a_{0}, b_{0}\right)=(1,1)$, 因此对一切正偶数 $t, a_{t}, b_{t}$ 均为大于 1 的奇数. 这表明, 方程 (2) 有无穷多组奇数解 $(a, b)$, 从而有无穷多个正整数对 $(m, n)=\left(\frac{a+1}{2}, \frac{b+1}{2}\right)$, 使得 $\frac{S_{m}}{S_{n}}=k=p^{c}$.

评注 第一问要分类讨论, 通过 “比大小” 来得出矛盾. 第二问需要发现 (2)式与 Pell 方程的联系。

