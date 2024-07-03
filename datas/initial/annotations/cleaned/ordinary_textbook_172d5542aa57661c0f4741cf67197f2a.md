数学新星网 $\%$ 冷岗松专栏

www.nsmath.cn/lgszl

# 2023 年上海新星夏季数学奥林匹克试题解析 

胡珏伟 吴尉迟冷岗松

2023 年上海新星春季数学奥林匹克于 2023 年 6 月 2 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 在 $\triangle A B C$ 中, $D, E, F$ 分别是三边 $B C, C A, A B$ 上的点满足 $A D, B E$, $C F$ 交于一点且 $A D$ 是 $\angle E D F$ 的角平分线. 证明: $A D \perp B C$.

(华东师范大学 罗振华 供题)

2. 设 $x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}^{+}$满足

$$
\sum_{i=1}^{n} x_{i}=1
$$

证明:

$$
\sum_{i=1}^{n} \frac{x_{i}^{2}}{1-x_{i}} \geq \frac{1}{n-1}+\frac{n}{(n-1)^{2}} \sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}
$$

(上海中学张甲供题)

3. 设正整数 $a, b, n$ 满足 $a<b \leq \frac{n}{2}$, 记 $d=\operatorname{gcd}\left(\left(\begin{array}{l}n \\ a\end{array}\right),\left(\begin{array}{l}n \\ b\end{array}\right)\right)$. 证明: $d \geq 2^{a}$.

(上海大学胡珏伟 冷岗松 供题)

4. 正实数数列 $\left\{a_{n}\right\}$ 满足: 对任意正整数 $n \geq 101$, 均有

$$
a_{n}=\max _{1 \leq i \leq 100} a_{n-i}-\min _{1 \leq i \leq 100} a_{n-i} .
$$

证明: 存在正整数 $k$, 使得对任意正整数 $n>k$, 均有 $a_{n}<1$.

(华威大学 吴茁 供题)

修订日期: 2023-07-03.

5. 给定 $n, k$ 是正整数满足 $n>4 k, X$ 是 $n$ 元集. 求最小的正整数 $m$, 使得 $X$的任意两两不同 $k$ 元子集 $X_{1}, X_{2}, \cdots, X_{m}$, 满足对任意 $a_{i} \in X_{i}, i=1,2, \cdots, m$,都存在 $1 \leq j \leq m$, 使得

$$
X_{j} \subset \bigcup_{i=1}^{m}\left\{a_{i}\right\}
$$

(华东师范大学 吴尉迟, 上海大学 胡珏伟 供题)

6. 在单位正方形 $A B C D$ 中, $X$ 是 $A B$ 的中点, $Y, Z$ 分别在边 $C D, D A$ 上.求最小的实数 $\lambda$, 使得 $\triangle X Y Z$ 的外接圆半径总不超过 $\lambda$.

(中国人民大学附属中学 张端阳 供题)

## II . 解答与评注

题 1 在 $\triangle A B C$ 中, $D, E, F$ 分别是三边 $B C, C A, A B$ 上的点满足 $A D, B E$, $C F$ 交于一点且 $A D$ 是 $\angle E D F$ 的角平分线. 证明: $A D \perp B C$.



证明 1 过点 $A$ 作直线 $B C$ 的平行线 $l$, 分别交 $D F, D E$ 于 $M, N$, 则

$$
\frac{A F}{F B}=\frac{A N}{B D}, \frac{A E}{E C}=\frac{A M}{C D}
$$

由塞瓦定理知

$$
\frac{A F}{F B} \cdot \frac{B D}{D C} \cdot \frac{C E}{E A}=1
$$

故 $A M=A N$. 因此 $A D \perp M N$, 即 $A D \perp B C$.


证明 2 若 $A C$ 不平行 $D F$. 延长 $C A, D F$ 交于点 $G$. 由塞瓦定理知

由梅涅劳斯定理知

$$
\frac{A F}{F B} \cdot \frac{B D}{D C} \cdot \frac{C E}{E A}=1
$$

$$
\frac{C G}{G A} \cdot \frac{A F}{F B} \cdot \frac{B D}{D C}=1
$$

故

$$
\frac{C E}{E A}=\frac{C G}{G A}
$$

即 $(G, E, A, C)$ 调和. 由 $A D$ 平分 $\angle E D F$ 知 $A D \perp B C$.

若 $A C / / D F, D E$ 不平行 $A B$, 可延长 $D E$ 与 $A B$, 同理得到证明.

若 $A C / / D F, D E / / A B$, 则 $A F D E$ 为菱形, 易证 $A D \perp B C$.

评注 此题是简单的几何题, 考试中约 $96 \%$ 做对此题. 证明 1 直接利用塞瓦定理得到证明; 证明 2 则是基于调和点列的性质转化角平分线和垂直的关系得到的。

题 2 设 $x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}^{+}$满足

证明:

$$
\sum_{i=1}^{n} x_{i}=1
$$

$$
\sum_{i=1}^{n} \frac{x_{i}^{2}}{1-x_{i}} \geq \frac{1}{n-1}+\frac{n}{(n-1)^{2}} \sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}
$$

证明 1 由

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{x_{i}^{2}}{1-x_{i}} & =\sum_{i=1}^{n} \frac{x_{i}^{2}-x_{i}+x_{i}}{1-x_{i}} \\
& =\sum_{i=1}^{n}\left(\frac{x_{i}}{1-x_{i}}-x_{i}\right) \\
& =\sum_{i=1}^{n} \frac{x_{i}}{1-x_{i}}-1
\end{aligned}
$$

可知等价于证明

$$
\sum_{i=1}^{n} \frac{x_{i}}{1-x_{i}} \geq \frac{n}{n-1}+\frac{n \sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}}{(n-1)^{2}}
$$

由 Cauchy 不等式知

$$
\sum_{i=1}^{n} \frac{x_{i}^{2}}{\left(1-x_{i}\right) x_{i}} \geq \frac{\left(\sum_{i=1}^{n} x_{i}\right)^{2}}{\sum_{i=1}^{n}\left(1-x_{i}\right) x_{i}}=\frac{1}{1-\sum_{i=1}^{n} x_{i}^{2}}
$$

结合

故只需证明

$$
\begin{aligned}
\frac{1}{1-\sum_{i=1}^{n} x_{i}^{2}}-\frac{n}{n-1} & =\frac{n \sum_{i=1}^{n} x_{i}^{2}-n+n-1}{(n-1)\left(1-\sum_{i=1}^{n} x_{i}^{2}\right)} \\
& =\frac{n \sum_{i=1}^{n} x_{i}^{2}-\left(\sum_{i=1}^{n} x_{i}\right)^{2}}{(n-1)\left(1-\sum_{i=1}^{n} x_{i}^{2}\right)} \\
& =\frac{\sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}}{(n-1)\left(1-\sum_{i=1}^{n} x_{i}^{2}\right)} .
\end{aligned}
$$

$$
1-\sum_{i=1}^{n} x_{i}^{2} \geq \frac{n-1}{n} \Leftrightarrow \sum_{i=1}^{n} x_{i}^{2} \geq \frac{1}{n}
$$

由 Cauchy 不等式知后者成立.

证明 2 (长沙市南雅中学 邓吴恩) 原不等式等价于

$$
\begin{aligned}
& \sum_{i=1}^{n} \frac{x_{i}^{2}}{1-x_{i}}+\sum_{i=1}^{n} x_{i}-1 \geq \frac{1}{n-1}+\frac{n}{(n-1)^{2}} \sum_{1 \leq i<j \leq n}\left(x_{i}^{2}+x_{j}^{2}-2 x_{i} x_{j}\right) \\
& \Leftrightarrow \sum_{i=1}^{n} \frac{x_{i}}{1-x_{i}}-1 \geq \frac{1}{n-1}+\frac{n}{(n-1)^{2}}\left((n-1) \sum_{i=1}^{n} x_{i}^{2}-\sum_{1 \leq i<j \leq n} 2 x_{i} x_{j}\right) \\
& \Leftrightarrow \sum_{i=1}^{n} \frac{x_{i}}{1-x_{i}} \geq \frac{n}{n-1}+\frac{n}{(n-1)^{2}}\left(n \sum_{i=1}^{n} x_{i}^{2}-\left(\sum_{i=1}^{n} x_{i}\right)^{2}\right) \\
& \Leftrightarrow \sum_{i=1}^{n} \frac{x_{i}}{1-x_{i}} \geq \frac{n}{n-1}+\frac{n^{2}}{(n-1)^{2}} \sum_{i=1}^{n} x_{i}^{2}-\frac{n}{(n-1)^{2}} \\
& \Leftrightarrow \sum_{i=1}^{n} \frac{x_{i}}{1-x_{i}}+\frac{n^{2}}{(n-1)^{2}} \sum_{i=1}^{n} x_{i}\left(1-x_{i}\right) \\
& \quad \geq \frac{n}{n-1}+\frac{n^{2}}{(n-1)^{2}} \sum_{i=1}^{n} x_{i}-\frac{n}{(n-1)^{2}}=\frac{2 n}{n-1} .
\end{aligned}
$$

最后一步不等式成立是由于

$$
\sum_{i=1}^{n}\left(\frac{x_{i}}{1-x_{i}}+\frac{n^{2}}{(n-1)^{2}} x_{i}\left(1-x_{i}\right)\right) \geq \sum_{i=1}^{n} \frac{2 n}{n-1} x_{i}=\frac{2 n}{n-1}
$$

等号成立当且仅当

$$
x_{1}=x_{2}=\cdots=x_{n}=\frac{1}{n} \text {. }
$$

证毕.

评注 此题是简单的代数题, 考试中约 $54 \%$ 做对此题. 问题的关键是如何处
理 $\left(x_{i}-x_{j}\right)^{2}$ 项, 再结合 Cauchy 不等式就可以得到证明. 证明 2 是利用均值不等式给出的证明.

题 3 设正整数 $a, b, n$ 满足 $a<b \leq \frac{n}{2}$, 记 $d=\operatorname{gcd}\left(\left(\begin{array}{l}n \\ a\end{array}\right),\left(\begin{array}{l}n \\ b\end{array}\right)\right)$. 证明: $d \geq 2^{a}$.

证明 由

$$
\left(\begin{array}{l}
n \\
a
\end{array}\right)\left(\begin{array}{l}
n-a \\
b-a
\end{array}\right)=\left(\begin{array}{l}
n \\
b
\end{array}\right)\left(\begin{array}{l}
b \\
a
\end{array}\right)
$$

知

$$
\frac{\left(\begin{array}{c}
n \\
a
\end{array}\right)}{d}\left(\begin{array}{c}
n-a \\
b-a
\end{array}\right)=\frac{\left(\begin{array}{c}
n \\
b
\end{array}\right)}{d}\left(\begin{array}{l}
b \\
a
\end{array}\right)
$$

故 $\frac{\left(\begin{array}{l}n \\ a\end{array}\right)}{d}$ 整除 $\left(\begin{array}{l}b \\ a\end{array}\right)$, 即

$$
\frac{\left(\begin{array}{l}
n \\
a
\end{array}\right)}{d} \leq\left(\begin{array}{l}
b \\
a
\end{array}\right)
$$

因此

$$
\begin{aligned}
d \geq \frac{\left(\begin{array}{l}
n \\
a
\end{array}\right)}{\left(\begin{array}{l}
b \\
a
\end{array}\right)} & =\frac{n(n-1) \cdots(n-a+1)}{b(b-1) \cdots(b-a+1)} \\
& =\frac{n}{b} \frac{n-1}{b-1} \cdots \frac{n-a+1}{b-a+1} \geq 2^{a} .
\end{aligned}
$$

证毕!

评注 此题是中等难度的数论题, 考试中约 $30 \%$ 做对此题. 问题的关键是得到如下组合恒等式

$$
\left(\begin{array}{l}
n \\
a
\end{array}\right)\left(\begin{array}{l}
n-a \\
b-a
\end{array}\right)=\left(\begin{array}{l}
n \\
b
\end{array}\right)\left(\begin{array}{l}
b \\
a
\end{array}\right)
$$

若使用库默尔定理等反而会使得问题复杂化.

题 4 正实数数列 $\left\{a_{n}\right\}$ 满足: 对任意正整数 $n \geq 101$, 均有

$$
a_{n}=\max _{1 \leq i \leq 100} a_{n-i}-\min _{1 \leq i \leq 100} a_{n-i} .
$$

证明: 存在正整数 $k$, 使得对任意正整数 $n>k$, 均有 $a_{n}<1$.

证明 我们分几步完成证明.

结论 1 对任意实数 $\varepsilon>0$, 均存在无穷多个正整数 $k$, 使得 $a_{k}<\varepsilon$.

若不然, 则存在正整数 $M$, 使得对任意正整数 $n \geq M$ 时均有 $a_{n} \geq \varepsilon$. 定义

$$
M_{k}=\max _{0 \leq i \leq 99} a_{M+100 k-i} \quad(k=1,2, \cdots)
$$

则由 $\left\{a_{n}\right\}$ 的递推关系易见 $M_{k}-M_{k+1} \geq \varepsilon$, 这与 $\left\{M_{k}\right\}$ 为正项数列矛盾! 结论 1
获证.

结论 2 存在正整数 $p, q(100 \leq p<q \leq p+99)$ 使得 $\max \left(a_{p}, a_{q}\right)<\frac{1}{2}$.

若不然, 根据结论 1 知, 存在 $r>100$ 使得 $a_{r}=\delta<\frac{1}{2}$, 且

$$
a_{r \pm 1}, a_{r \pm 2}, \cdots, a_{r \pm 99} \geq \frac{1}{2}
$$

设

$$
S=\max _{1 \leq i \leq 100} a_{r-i}=a_{r-s}
$$

则由 $\left\{a_{n}\right\}$ 的定义得 $a_{r+1}=S-\delta$, 且

$$
a_{r+2}, a_{r+3}, \cdots, a_{r+99} \in\left[a_{r+1}-a_{r}, a_{r-s}-a_{r}\right]=[S-2 \delta, S-\delta]
$$

于是,

$$
a_{r+100}=a_{r+1}-a_{r}=S-2 \delta,
$$

且

$$
a_{r+101}=a_{r+1}-a_{r+100}=\delta,
$$

由假设知 $S-2 \delta \geq \frac{1}{2}$. 因此, 重复以上过程我们便得到了数列 $\left\{a_{r+101 k}\right\}$ 中的各项均为常数 $\delta$, 进而由假设可得对任意正整数 $r^{\prime} \geq r$, 均有 $a_{r^{\prime}} \geq \delta$. 但这与结论 1 相悖, 矛盾! 结论 2 获证.

结论 3 若正整数 $p, q(100 \leq p<q \leq p+99)$ 使得 $\max \left(a_{p}, a_{q}\right)<\frac{1}{2}$, 则 $a_{n}<1(n \geq q)$.

因为

$$
\frac{1}{2}>a_{q}=\max _{1 \leq i \leq 100} a_{q-i}-\min _{1 \leq i \leq 100} a_{q-i} \geq \max _{1 \leq i \leq 100} a_{q-i}-a_{p}>\max _{1 \leq i \leq 100} a_{q-i}-\frac{1}{2}
$$

所以

$$
\max _{1 \leq j \leq 100} a_{q-j}<1
$$

据此及 $\left\{a_{n}\right\}$ 的定义递推易见 $a_{n}<1(n \geq q)$. 结论 3 获证.

注意到结论 2 , 结论 3 蕴含了原命题, 这就完成了证明.

评注 此题是困难的代数题, 考试中约 $4 \%$ 做对此题. 要证明对任意的 $n>k$均有 $a_{n}<1$, 只需证明存在 $a_{q}$ 使得 $a_{q}$ 的前 100 项均小于 1 . 结合 $a_{n}$ 的递推关系,这又可以转化为 $a_{q}$ 与 $a_{q}$ 的前 100 项最小值之和. 因此只需找到下标差不超过 100 的两项均小于 $\frac{1}{2}$, 即结论 2. 难点在于利用反证假设仔细分析相邻 99 项的最大值和最小值关系得到连续 100 项最小值为常数, 这与结论 1 矛盾.

值得指出的是: 结论中的 1 可以替换为任意正常数, 因此 $a_{n}$ 的极限为零.
题 5 给定 $n, k$ 是正整数满足 $n>4 k, X$ 是 $n$ 元集. 求最小的正整数 $m$, 使得 $X$ 的任意两两不同 $k$ 元子集 $X_{1}, X_{2}, \cdots, X_{m}$, 满足对任意 $a_{i} \in X_{i}, i=1,2, \cdots$, $m$, 都存在 $1 \leq j \leq m$, 使得

$$
X_{j} \subset \bigcup_{i=1}^{m}\left\{a_{i}\right\}
$$

解 所求 $m$ 的最小值为

$$
\left(\begin{array}{l}
n \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lfloor\frac{n}{2}\right\rfloor \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lceil\frac{n}{2}\right\rceil \\
k
\end{array}\right)+1 .
$$

先证:

$$
m=\left(\begin{array}{l}
n \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lfloor\frac{n}{2}\right\rfloor \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lceil\frac{n}{2}\right\rceil \\
k
\end{array}\right)+1
$$

时, 命题成立.

任取 $a_{i} \in X_{i}, i=1,2, \cdots, m$, 记

$$
Y=\bigcup_{i=1}^{m}\left\{a_{i}\right\}
$$

设 $|Y|=t$. 考虑包含于 $Y$ 或包含于 $X \backslash Y$ 的 $k$ 元集个数,

$$
\left(\begin{array}{l}
t \\
k
\end{array}\right)+\left(\begin{array}{c}
n-t \\
k
\end{array}\right) \geq\left(\begin{array}{c}
\left\lfloor\frac{n}{2}\right\rfloor \\
k
\end{array}\right)+\left(\begin{array}{c}
\left\lceil\frac{n}{2}\right\rceil \\
k
\end{array}\right)
$$

故不包含于 $Y$ 且不包含于 $X \backslash Y$ 的 $k$ 元集个数不超过

$$
\left(\begin{array}{l}
n \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lfloor\frac{n}{2}\right\rfloor \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lceil\frac{n}{2}\right\rceil \\
k
\end{array}\right) .
$$

由抽屉原理, $X_{1}, X_{2}, \cdots, X_{m}$ 至少有一个包含于 $Y$ 或包含于 $X \backslash Y$, 不妨设为 $X_{j}$, 注意到 $X_{j} \cap Y \neq \varnothing$, 故 $X_{j} \subset Y$.

下证:

$$
m \geq\left(\begin{array}{l}
n \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lfloor\frac{n}{2}\right\rfloor \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lceil\frac{n}{2}\right\rceil \\
k
\end{array}\right)+1
$$

$k=1$ 时结论成立. $k \geq 2$ 时, 不妨设 $X=\{1,2, \cdots, n\}$. 记 $A_{1}, A_{2}, \cdots, A_{l}$中所有不包含于 $\left\{1,2, \cdots,\left\lfloor\frac{n}{2}\right\rfloor\right\}$ 且不包含于 $\left\{\left\lfloor\frac{n}{2}\right\rfloor+1, \cdots, n\right\}$ 的所有 $k$ 元集,则

$$
l=\left(\begin{array}{l}
n \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lfloor\frac{n}{2}\right\rfloor \\
k
\end{array}\right)-\left(\begin{array}{c}
\left\lceil\frac{n}{2}\right\rceil \\
k
\end{array}\right) .
$$

下证: $l \geq\left\lfloor\frac{n}{2}\right\rfloor$.

$n$ 是偶数时,

$$
\begin{aligned}
& \left(\begin{array}{l}
n \\
k
\end{array}\right)-\left(\begin{array}{l}
\frac{n}{2} \\
k
\end{array}\right)-\left(\begin{array}{c}
\frac{n}{2} \\
k
\end{array}\right) \geq \frac{n}{2} \\
\Leftrightarrow & n(n-1) \cdots(n-k+1)-2 \frac{n}{2}\left(\frac{n}{2}-1\right) \cdots\left(\frac{n}{2}-k+1\right) \geq \frac{n}{2} k !
\end{aligned}
$$

$$
\Leftrightarrow 2(n-1) \cdots(n-k+1)-2\left(\frac{n}{2}-1\right) \cdots\left(\frac{n}{2}-k+1\right) \geq k !
$$

上式在 $k \geq 2$ 时成立.

同理可证 $n$ 为奇数时, $l \geq\left\lfloor\frac{n}{2}\right\rfloor$ 成立.

由

$$
A_{i} \cap\left\{1,2, \cdots,\left\lfloor\frac{n}{2}\right\rfloor\right\} \neq \varnothing
$$

且

$$
\left\{1,2, \cdots,\left\lfloor\frac{n}{2}\right\rfloor\right\} \subset \bigcup_{i=1}^{l} A_{i}
$$

故可取 $a_{i} \in A_{i}$, 使得

$$
\bigcup_{i=1}^{l}\left\{a_{i}\right\}=\left\{1,2, \cdots,\left\lfloor\frac{n}{2}\right\rfloor\right\}
$$

又由 $A_{i} \not \subset\left\{1,2, \cdots,\left\lfloor\frac{n}{2}\right\rfloor\right\}$, 知满足要求的 $m \geq l+1$.

评注 此题是困难的组合题, 考试中约 $4 \%$ 做对此题. 题目所求的 $m$ 最小值不容易直接猜测, 事实上是在集合“平分”的情形下取得. 对 $m=\left(\begin{array}{l}n \\ k\end{array}\right)-\left(\begin{array}{c}\left\lfloor\frac{n}{2}\right\rfloor \\ k\end{array}\right)-$ $\left(\begin{array}{c}\left\lceil\frac{n}{2}\right\rceil \\ k\end{array}\right)+1$ 的情形通过计数结合抽屉原理得到证明. 证明 $m \geq\left(\begin{array}{l}n \\ k\end{array}\right)-\left(\begin{array}{c}\left\lfloor\frac{n}{2}\right\rfloor \\ k\end{array}\right)-\left(\begin{array}{c}\left\lceil\frac{n}{2}\right\rceil \\ k\end{array}\right)+1$时需要比较 $\left(\begin{array}{l}n \\ k\end{array}\right)-\left(\begin{array}{c}\left\lfloor\frac{n}{2}\right\rfloor \\ k\end{array}\right)-\left(\begin{array}{c}\left\lceil\frac{n}{2}\right\rceil \\ k\end{array}\right)$ 与 $\left\lfloor\frac{n}{2}\right\rfloor$ 的大小关系, 事实上这个大小关系是较为宽松的, 直接展开即可验证.

题 6 在单位正方形 $A B C D$ 中, $X$ 是 $A B$ 的中点, $Y, Z$ 分别在边 $C D, D A$上. 求最小的实数 $\lambda$, 使得 $\triangle X Y Z$ 的外接圆半径总不超过 $\lambda$.

解 记 $R$ 为 $\triangle X Y Z$ 的外接圆半径.

固定点 $Z$ 时, $X Z$ 的长固定, 此时只需求 $\sin \angle X Y Z$ 的最小值.



当 $Z=D$ 时, 因为

$$
\angle X C D \leq \angle X Y D<180^{\circ}-\angle X D C,
$$

所以 $\sin \angle X Y D \geq \sin \angle X C D=\frac{2}{\sqrt{5}}$, 从而

$$
R=\frac{1}{2} \cdot \frac{X Z}{\sin \angle X Y D} \leq \frac{1}{2} \cdot \frac{\sqrt{5} / 2}{2 / \sqrt{5}}=\frac{5}{8}<\frac{5}{4} .
$$

当 $Z \neq D$ 时, 设点 $Y_{0}$ 使 $\sin \angle X Y Z$ 达到最小值. 此时 $\angle X Y_{0} Z$ 达到最小或最大, 所以 $Y_{0}=C$ 或 $Y_{0}=D$ 或 $\triangle X Y_{0} Z$ 的外接圆与 $C D$ 相切.



当 $Y_{0}=C$ 时, 一方面, $\angle X Z C \geq \min \{\angle X A C, \angle X D C\}=45^{\circ}$. 另一方面, 取 $X C$ 的中点 $M$, 则

$$
M Z \geq \frac{3}{4}>\frac{\sqrt{5}}{4}=M X=M C
$$

所以 $\angle X Z C<90^{\circ}$.于是 $\sin \angle X Z C \geq \frac{\sqrt{2}}{2}$, 从而

$$
R=\frac{1}{2} \cdot \frac{X C}{\sin \angle X Z C} \leq \frac{1}{2} \cdot \frac{\sqrt{5} / 2}{\sqrt{2} / 2}=\frac{\sqrt{10}}{4}<\frac{5}{4} .
$$



当 $Y_{0}=D$ 时, $\angle X D A<\angle X Z A \leq 90^{\circ}$, 所以

$$
\sin \angle X Z D>\sin \angle X D A=\frac{1}{\sqrt{5}}
$$

从而

$$
R=\frac{1}{2} \cdot \frac{X D}{\sin \angle X Z A}<\frac{1}{2} \cdot \frac{\sqrt{5} / 2}{1 / \sqrt{5}}=\frac{5}{4} .
$$



当 $\angle X Y_{0} Z$ 最大时, $\angle X Y_{0} Z>\angle X D Z$, 又

$$
\angle X Y_{0} Z \leq \angle X Y_{0} D<180^{\circ}-\angle X D C
$$

所以 $\sin \angle X Y_{0} Z>\min \{\sin \angle X D Z, \sin \angle X D C\}=\frac{1}{\sqrt{5}}$, 从而

$$
R=\frac{1}{2} \cdot \frac{X Z}{\sin \angle X Y_{0} Z}<\frac{1}{2} \cdot \frac{\sqrt{5} / 2}{1 / \sqrt{5}}=\frac{5}{4} .
$$

故总有 $R<\frac{5}{4}$, 于是当 $\lambda=\frac{5}{4}$ 时满足要求.

由上述证明可知, 当 $Y=D, Z \rightarrow D$ 时, $R \rightarrow \frac{5}{4}$.

综上, 所求最小值为 $\frac{5}{4}$.

评注 此题是中等偏难的几何题, 考试中约 $21 \%$ 做对此题. 讨论 $\triangle X Y Z$ 外接圆半径的上确界即讨论 $\sin \angle X Y Z$ 的最小值. 本题源于对 Funar 猜想的讨论.

单位正方形内接三角形内切圆半径的最大值为 $\frac{\sqrt{5}-1}{4}$.

