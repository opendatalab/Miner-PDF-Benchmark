# 第 19 届 CGMO 试题解答 

翟振华

(华东师范大学, 200241)

第 19 届中国女子数学奥林匹克 (CGMO) 于 2020 年 8 月 8 日至 11 日在江西省鹰潭一中举行. 下面介绍本次考试试题及解答.

## I. 试题

1. 如图, 在四边形 $A B C D$ 中, $A B=A D, C B=C D, \angle A B C=90^{\circ}$, 点 $E, F$ 分别在线段 $A B, A D$ 上, 点 $P, Q$ 在线段 $E F$ 上( $P$ 在 $E, Q$ 之间), 满足 $\frac{A E}{E P}=\frac{A F}{F Q}$. 点 $X, Y$ 分别在线段 $C P, C Q$ 上, 满足 $B X \perp C P, D Y \perp C Q$. 证明: $X, P, Q, Y$ 四点共圆.

(华东师范大学 何忆捷 供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_60abcbc9f7883cbf36deg-01.jpg?height=514&width=460&top_left_y=1493&top_left_x=798)

2. 给定整数 $n \geq 2$, 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是任意实数, 求

$$
2 \sum_{1 \leq i<j \leq n}\left[x_{i} x_{j}\right]-(n-1) \sum_{i=1}^{n}\left[x_{i}^{2}\right]
$$

的最大值, 其中 $[x]$ 表示不超过实数 $x$ 的最大整数.

(南方科技大学 付云皓 供题)

3. 设有三个班级, 每班恰有 $n$ 名同学, 这 $3 n$ 名同学的身高两两不同. 现将这些同学分成 $n$ 组, 每组 3 名同学分别来自不同的班级, 并将每组中身高最高
的同学称为 “高个子” . 已知无论如何分组, 每班都至少有 10 名同学是 “高个子” . 证明: $n$ 的最小可能值是 40 .

(南方科技大学 付云皓 供题)

4. 设 $p, q$ 是两个不同的素数, $p>q$. 证明: $p !-1$ 与 $q !-1$ 的最大公约数不超过 $p^{\frac{p}{3}}$.

(复旦大学 赖力 供题)

5. 求满足下面两个条件的所有实数序列 $\left\{b_{n}\right\}_{n \geq 1}$ 和 $\left\{c_{n}\right\}_{n \geq 1}$ :

(i) 对任意正整数 $n, b_{n} \leq c_{n}$;

(ii) 对任意正整数 $n, b_{n+1}$ 与 $c_{n+1}$ 是一元二次方程 $x^{2}+b_{n} x+c_{n}=0$ 的两根.

(华东师范大学 㫿振华 供题)

6. 设 $p, q$ 均是大于 1 的整数, 且 $p$ 与 $6 q$ 互素. 证明:

$$
\sum_{k=1}^{q-1}\left[\frac{p k}{q}\right]^{2} \equiv 2 p \sum_{k=1}^{q-1} k\left[\frac{p k}{q}\right] \quad(\bmod q-1)
$$

其中 $[x]$ 表示不超过实数 $x$ 的最大整数.

(南京师范大学 纪春岗 供题)

7. 如图, 在 $\triangle A B C$ 中, $A B<A C, \angle B A C=120^{\circ}$, 外接圆 $\odot O$ 在点 $A, B$ 处的切线相交于点 $P$, 在点 $A, C$ 处的切线相交于点 $Q$. 设 $H$ 和 $I$ 分别是 $\triangle P O Q$ 的垂心和内心, $M$ 是弧 $\widehat{B A C}$ 的中点, $N$ 是线段 $O I$ 的中点, $D$ 是直线 $M N$ 与 $\odot O$ 的另一个交点. 证明: $I H \perp A D$. (华东师范大学 林天齐 供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_60abcbc9f7883cbf36deg-02.jpg?height=631&width=508&top_left_y=1632&top_left_x=774)

8. 给定正整数 $n$. 一个有限项正整数列 $\left(a_{1}, \cdots, a_{m}\right)$ 称为 “ $n$-偶数列”:若 $n=a_{1}+\cdots+a_{m}$, 且共有偶数个整数对 $(i, j)$ 满足 $1 \leq i<j \leq m$ 而 $a_{i}>a_{j}$.求 $n$-偶数列的个数.

例如, 共有六个 4 -偶数列： $(4) 、(1,3) 、(2,2) 、(1,1,2) 、(2,1,1) 、(1,1,1,1)$. (华东师范大学 吴尉迟 供题)

## II. 解答

1. 如图, 在四边形 $A B C D$ 中, $A B=A D, C B=C D, \angle A B C=90^{\circ}$, 点 $E, F$ 分别在线段 $A B, A D$ 上, 点 $P, Q$ 在线段 $E F$ 上 ( $P$ 在 $E, Q$ 之间), 满足 $\frac{A E}{E P}=\frac{A F}{F Q}$. 点 $X, Y$ 分别在线段 $C P, C Q$ 上, 满足 $B X \perp C P, D Y \perp C Q$. 证明: $X, P, Q, Y$ 四点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_60abcbc9f7883cbf36deg-03.jpg?height=509&width=462&top_left_y=702&top_left_x=797)

证明. 由条件知 $\triangle A B C$ 与 $\triangle A D C$ 关于 $A C$ 对称, 且

$$
\angle A B C=\angle A D C=90^{\circ} \text {. }
$$

设 $A C$ 与 $E F$ 交于点 $K$, 由 $A K$ 平分 $\angle E A F$ 得 $\frac{A E}{A F}=\frac{K E}{K F}$, 又 $\frac{A E}{A F}=\frac{E P}{F Q}$,所以 $\frac{K E}{K F}=\frac{E P}{F Q}$, 即 $\frac{K E}{E P}=\frac{K F}{F Q}$.

延长 $C P$ 交 $A E$ 于点 $S$, 延长 $C Q$ 交 $A F$ 于点 $T$. 对 $\triangle K P C$ 与截线 $E S A$ 运用梅涅劳斯定理, 得

$$
\frac{K E}{E P} \cdot \frac{P S}{S C} \cdot \frac{C A}{A K}=1
$$

同理得

$$
\frac{K F}{F Q} \cdot \frac{Q T}{T C} \cdot \frac{C A}{A K}=1
$$

于是

$$
\frac{C S}{P S}=\frac{K E}{E P} \cdot \frac{C A}{A K}=\frac{K F}{F Q} \cdot \frac{C A}{A K}=\frac{C T}{Q T},
$$

故 $\frac{C S}{C P}=\frac{C T}{C Q}$, 即 $\frac{C P}{C Q}=\frac{C S}{C T}$.

注意到 $B X \perp C P, D Y \perp C Q$ 及 $\angle A B C=\angle A D C=90^{\circ}$, 得

$$
\frac{C X \cdot C P}{C Y \cdot C Q}=\frac{C X \cdot C S}{C Y \cdot C T}=\frac{C B^{2}}{C D^{2}}=1,
$$

所以 $X, P, Q, Y$ 四点共圆.

2. 给定整数 $n \geq 2$, 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是任意实数, 求

$$
2 \sum_{1 \leq i<j \leq n}\left[x_{i} x_{j}\right]-(n-1) \sum_{i=1}^{n}\left[x_{i}^{2}\right]
$$

的最大值, 其中 $[x]$ 表示不超过实数 $x$ 的最大整数.

因为

解. 注意到 $2 \sum_{1 \leq i<j \leq n}\left[x_{i} x_{j}\right]-(n-1) \sum_{i=1}^{n}\left[x_{i}^{2}\right]=\sum_{1 \leq i<j \leq n}\left(2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right]\right)$.

$$
2\left[x_{i} x_{j}\right] \leq 2 x_{i} x_{j} \leq x_{i}^{2}+x_{j}^{2}<\left[x_{i}^{2}\right]+\left[x_{j}^{2}\right]+2,
$$

且上式最左边和最右边都是整数, 故

$$
2\left[x_{i} x_{j}\right] \leq\left[x_{i}^{2}\right]+\left[x_{j}^{2}\right]+1
$$

等号必须在 $\left[x_{i}^{2}\right]$ 和 $\left[x_{j}^{2}\right]$ 奇偶性不同时才可能成立 (因为左边是偶数). 因此,当 $\left[x_{i}^{2}\right]$ 和 $\left[x_{j}^{2}\right]$ 奇偶性不同时,

$$
2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right] \leq 1
$$

当 $\left[x_{i}^{2}\right]$ 和 $\left[x_{j}^{2}\right]$ 奇偶性相同时,

$$
2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right] \leq 0
$$

设 $\left[x_{1}^{2}\right],\left[x_{2}^{2}\right], \cdots,\left[x_{n}^{2}\right]$ 中有 $k$ 个奇数, $n-k$ 个偶数, 则

$$
\sum_{1 \leq i<j \leq n}\left(2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right]\right) \leq k(n-k) \leq\left[\frac{n^{2}}{4}\right]
$$

另一方面, 设 $m=\left[\frac{n}{2}\right]$. 如果

$$
x_{1}=x_{2}=\cdots=x_{m}=1.4, x_{m+1}=x_{m+2}=\cdots=x_{n}=1.5
$$

那么当 $1 \leq i<j \leq m$ 或 $m+1 \leq i<j \leq n$ 时,

$$
2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right]=0
$$

而当 $1 \leq i \leq m$ 且 $m+1 \leq j \leq n$ 时,

$$
2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right]=1
$$

此时

$$
\sum_{1 \leq i<j \leq n}\left(2\left[x_{i} x_{j}\right]-\left[x_{i}^{2}\right]-\left[x_{j}^{2}\right]\right)=m(n-m)=\left[\frac{n^{2}}{4}\right]
$$

综上所述, 所求的最大值为 $\left[\frac{n^{2}}{4}\right]$.

3. 设有三个班级, 每班恰有 $n$ 名同学, 这 $3 n$ 名同学的身高两两不同. 现将这些同学分成 $n$ 组, 每组 3 名同学分别来自不同的班级, 并将每组中身高最高的同学称为 “高个子”. 已知无论如何分组, 每班都至少有 10 名同学是 “高个子”. 证明： $n$ 的最小可能值是 40 .

证法一. 首先对 $n=40$ 给出一种构造. 设三个班分别为 $A$ 班, $B$ 班和 $C$ 班. 所有学生由高到低分别为 $1,2, \cdots, 120$ 号, 其中 $1,2, \cdots, 10$ 号和 $71,72, \cdots, 100$ 号在 $A$ 班; $11,12, \cdots, 30$ 号和 $101,102, \cdots, 120$ 号在 $B$ 班; $31,32, \cdots, 70$ 号在 $C$ 班。

从而 $A$ 班的 $1,2, \cdots, 10$ 号必然是 “高个子” ; $B$ 班的 $11,12, \cdots, 30$ 号中最多有 10 名同学与 $1,2, \cdots, 10$ 号之一同组, 剩下至少有 10 名同学是 “高个子”; $C$ 班的 $31,32, \cdots, 70$ 号中最多有 30 名同学与 $1,2, \cdots, 30$ 号至少之一同组, 剩下至少有 10 名同学是 “高个子”。因此这个构造满足题目要求.

下面证明 40 是最小的. 将 $3 n$ 名同学按身高由高到低顺次编号为 $1,2, \cdots, 3 n$, 我们先证明一个引理.

引理. 设三个班的学生满足题目中的条件, 则对于每个班, 都存在一个 $k$,使得编号为 $1,2, \cdots, k$ 的学生中, 该班所占的人数比其它两个班所占的人数之和至少多 10 人.

引理的证明。考虑一个班（不妨设为 $A$ 班）, 设该班的所有同学的编号由小到大排列为 $a_{1}<a_{2}<\cdots<a_{n}$, 其余两个班的所有同学编号由小到大排列为 $x_{1}<x_{2}<\cdots<x_{2 n}$.

对 $1 \leq i \leq n-9$, 将编号为 $a_{i+9}$ 的 $A$ 班同学和编号为 $x_{i}$ 的 $B$ 或 $C$ 班同学分为一组, 然后将有 $A$ 班和 $C$ 班同学的组中添入一个未被分组的 $B$ 班同学,将有 $A$ 班和 $B$ 班同学的组中添入一个未被分组的 $C$ 班同学, 剩下同学按照每组 $A, B, C$ 班各一人分组, 此时除编号为 $a_{1}, a_{2}, \cdots, a_{9}$ 的同学外, $A$ 班还至少有一名同学是 “高个子”, 设其编号为 $a_{m}$, 那么 $a_{m}<x_{m-9}$, 这说明在编号为 $1,2, \cdots, a_{m}$ 的同学中, $A$ 班有 $m$ 人, $B, C$ 两班加在一起最多 $m-10$ 人, 因此引理得证.

回到原问题, 设 $A, B, C$ 班对应的引理中的 $k$ 分别为 $k_{1}, k_{2}, k_{3}$, 且不妨设 $k_{1} \leq k_{2} \leq k_{3}$, 那么在 $1,2, \cdots, k_{1}$ 号中, $A$ 班至少有 10 人; 在 $1,2, \cdots, k_{2}$ 号中, $B$班至少有 $10+10=20$ 人; 在 $1,2, \cdots, k_{3}$ 号中, $C$ 班至少有 $10+20+10=40$ 人.因此 40 是最小可能值.
证法二. 对学生的编号和构造同证法一, 下面仅证明 40 是最小的, 即证明 $n<40$ 时不可能满足题目中的条件.

假设可以满足条件, 由于每个班都至少有 10 名高个子, 故 $n \geq 30$. 考虑 $a_{n-19}, b_{n-19}, c_{n-19}$, 不妨设 $a_{n-19}$ 是三个数中最小的, 故编号为 $a_{1}, a_{2}, \cdots, a_{n-19}$ 的学生都高于编号为 $b_{20}, b_{21}, \cdots, b_{n}, c_{20}, c_{21}, \cdots, c_{n}$ 的学生.

现在对 $1 \leq i \leq n-19$, 将 $a_{i}, b_{i+1}, c_{i+19}$ 分为一组, 这些组中的高个子都是 $A$ 班的, 剩下的学生按照每班一人分组, 则 $B, C$ 班一共不超过 19 名高个子, 矛盾！因此 40 是最小可能值.

4. 设 $p, q$ 是两个不同的素数, $p>q$. 证明: $p !-1$ 与 $q !-1$ 的最大公约数不超过 $p^{\frac{p}{3}}$ 。

证明. 记 $D=\operatorname{gcd}(p !-1, q !-1)$. 易验证 $2 !-1,3 !-1,5 !-1,7 !-1$ 两两互素, 故 $p \leq 7$ 时命题成立.

以下设 $p \geq 11$. 注意到 $p !-q$ ! 被 $D$ 整除, 而 $q !$ 与 $D$ 互素, 故 $D$ 整除 $\frac{p !}{q !}-1$. 于是 $D \leq \frac{p !}{q !} \leq p^{p-q}$. 如果 $q \geq \frac{2}{3} p$, 则前式推出 $D \leq p^{\frac{p}{3}}$, 已得证. 故以下设 $p>\frac{3}{2} q$.

注意到 $D \mid\left(p !-q !^{2}\right.$ ), 并且 $p !-q !^{2} \neq 0$ （因为 $p !-q !^{2}$ 不被素数 $p$ 整除）.

如果 $p>2 q$, 则 $p !$ 与 $q !^{2}$ 有公因子 $q !^{2}$, 它与 $D$ 互素, 从而 $D$ 整除 $\frac{p !-q !^{2}}{q !^{2}}=$ $\frac{p !}{q !^{2}}-1$, 这推出 $D \leq \frac{p !}{q !^{2}}$. 又 $D \mid(q !-1)$ 推出 $D \leq q !$, 于是

$$
D \cdot D^{2} \leq \frac{p !}{q !^{2}} \cdot q !^{2}=p ! \leq p^{p}
$$

故 $D \leq p^{\frac{p}{3}}$, 命题得证.

剩下的情况是 $\frac{3}{2} q<p \leq 2 q$, 此时 $p !$ 与 $q !^{2}$ 有公因子 $q !(p-q)$ !, 它与 $D$ 互素,故 $D$ 整除 $\frac{p !-q !^{2}}{q !(p-q) !} \neq 0$, 这推出

$$
D \leq\left|\frac{p !}{q !(p-q) !}-\frac{q !}{(p-q) !}\right| \leq \max \left\{\frac{p !}{q !(p-q) !}, \frac{q !}{(p-q) !}\right\} .
$$

由于

$$
\frac{p !}{q !(p-q) !} \leq 2^{p} \leq 11^{\frac{p}{3}} \leq p^{\frac{p}{3}}
$$

而 $\frac{q !}{(p-q) !}$ 可以写成 $2 q-p$ 个不超过 $p$ 的连续正整数的乘积, 故

$$
\frac{q !}{(p-q) !} \leq p^{2 q-p} \leq p^{\frac{p}{3}}
$$

其中最后一个不等式是因为 $\frac{3}{2} q<p$. 于是 $D \leq p^{\frac{p}{3}}$, 得证.

5. 求满足下面两个条件的所有实数序列 $\left\{b_{n}\right\}_{n \geq 1}$ 和 $\left\{c_{n}\right\}_{n \geq 1}$ :

(i) 对任意正整数 $n, b_{n} \leq c_{n}$;

(ii) 对任意正整数 $n, b_{n+1}$ 与 $c_{n+1}$ 是一元二次方程 $x^{2}+b_{n} x+c_{n}=0$ 的两根.

解. 由条件(i),(ii)可知, $b_{n+1}$ 与 $c_{n+1}$ 由 $b_{n}, c_{n}$ 唯一确定, 且由韦达定理, 有

$$
\begin{aligned}
& b_{n}=-\left(b_{n+1}+c_{n+1}\right) \\
& c_{n}=b_{n+1} c_{n+1}
\end{aligned}
$$

若 $b_{1}=c_{1}=0$, 易知对所有 $n \geq 1$, 均有 $b_{n}=c_{n}=0$, 我们得到满足题目条件的序列 $\left\{b_{n}\right\}_{n \geq 1}$ 和 $\left\{c_{n}\right\}_{n \geq 1}$, 对任意正整数 $n, b_{n}=c_{n}=0$.

下面证明其他序列均不满足条件.

假设 $b_{1}, c_{1}$ 中恰有一个为零. 若 $b_{1}=0$, 则 $c_{1}>0$, 方程 $x^{2}+b_{1} x+c_{1}=0$ 无实根, 不满足条件. 若 $c_{1}=0$, 则 $b_{1}<0$, 方程 $x^{2}+b_{1} x+c_{1}=0$ 的两根为 $b_{2}=0$, $c_{2}=-b_{1}>0$, 方程 $x^{2}+b_{2} x+c_{2}=0$ 无实根, 不满足条件.

假设 $b_{1}, c_{1}$ 均不为零. 若 $b_{n}>0, c_{n}>0$, 则由等式 (1),(2) 可知 $b_{n+1}<$ $0, c_{n+1}<0$. 若 $b_{n}<0, c_{n}<0$, 则由等式 (1),(2) 可知 $b_{n+1}<0, c_{n+1}>0$. 若 $b_{n}<0, c_{n}>0$, 则由等式 (1),(2) 可知 $b_{n+1}>0, c_{n+1}>0$. 从而 $\left(b_{n}, c_{n}\right)$ 的符号以 3 为周期： $\cdots$ 、正正、负负、负正、 $\cdots$.

若 $b_{n}>0, c_{n}>0$, 一元二次方程 $x^{2}+b_{n} x+c_{n}=0$ 有实根, 判别式 $b_{n}^{2}-4 c_{n} \geq 0$, 即 $b_{n}^{2} \geq 4 c_{n} \geq 4 b_{n}$, 故 $c_{n} \geq b_{n} \geq 4$.

若 $b_{n}>0, c_{n}>0$, 且 $n>3$. 由等式(1)(2), 并结合 $c_{n} \geq b_{n} \geq 4$, 我们有

$$
\begin{aligned}
& b_{n-1}=-\left(b_{n}+c_{n}\right)<0, \quad c_{n-1}=b_{n} c_{n}>0, \\
& b_{n-2}=-\left(b_{n-1}+c_{n-1}\right)=b_{n}+c_{n}-b_{n} c_{n}<0, \\
& c_{n-2}=b_{n-1} c_{n-1}=-\left(b_{n}+c_{n}\right) b_{n} c_{n}<0, \\
& b_{n-3}=-\left(b_{n-2}+c_{n-2}\right) \geq-c_{n-2}=\left(b_{n}+c_{n}\right) b_{n} c_{n} \geq 4 b_{n},
\end{aligned}
$$

设 $i \in\{1,2,3\}$, 使得 $b_{i}>0, c_{i}>0$. 于是对任意正整数 $k, b_{i+3 k}>0, c_{i+3 k}>0$.反复利用上述不等式可得

$$
b_{i} \geq 4^{k} b_{i+3 k} \geq 4^{k+1}
$$

而 $k$ 是任意的, 这不可能.

综上所述, 所有满足条件的序列 $\left\{b_{n}\right\}_{n \geq 1}$ 和 $\left\{c_{n}\right\}_{n \geq 0}$ 只有恒为零的常数列.

6. 设 $p, q$ 均是大于 1 的整数, 且 $p$ 与 $6 q$ 互素. 证明:

$$
\sum_{k=1}^{q-1}\left[\frac{p k}{q}\right]^{2} \equiv 2 p \sum_{k=1}^{q-1} k\left[\frac{p k}{q}\right] \quad(\bmod q-1)
$$

其中 $[x]$ 表示不超过实数 $x$ 的最大整数.

证明. 对 $\alpha \in \mathbb{R}$, 记 $\{\alpha\}=\alpha-[\alpha]$.

$$
\begin{aligned}
2 p \sum_{k=1}^{q-1} k\left[\frac{p k}{q}\right] & =2 q \sum_{k=1}^{q-1} \frac{p k}{q}\left[\frac{p k}{q}\right]=q \sum_{k=1}^{q-1}\left(\left(\frac{p k}{q}\right)^{2}+\left[\frac{p k}{q}\right]^{2}-\left(\frac{p k}{q}-\left[\frac{p k}{q}\right]\right)^{2}\right) \\
& =q \sum_{k=1}^{q-1}\left(\frac{p k}{q}\right)^{2}+q \sum_{k=1}^{q-1}\left[\frac{p k}{q}\right]^{2}-q \sum_{k=1}^{q-1}\left\{\frac{p k}{q}\right\}^{2} .
\end{aligned}
$$

由于 $(p, q)=1, p \cdot 1, p \cdot 2, \cdots, p \cdot(q-1)$ 除以 $q$ 的余数取遍 $1,2, \cdots, q-1$. 从而,

$$
\sum_{k=1}^{q-1}\left\{\frac{p k}{q}\right\}^{2}=\sum_{k=1}^{q-1}\left(\frac{k}{q}\right)^{2}
$$

代入 (1) 式, 得

$$
\begin{aligned}
2 p \sum_{k=1}^{q-1} k\left[\frac{p k}{q}\right] & =\frac{p^{2}-1}{q} \sum_{k=1}^{q-1} k^{2}+q \sum_{k=1}^{q-1}\left[\frac{p k}{q}\right]^{2} \\
& =\frac{\left(p^{2}-1\right)(q-1)(2 q-1)}{6}+q \sum_{k=1}^{q-1}\left[\frac{p k}{q}\right]^{2} .
\end{aligned}
$$

由于 $(p, 6)=1$, 故 $6 \mid p^{2}-1$. 因此, 由 $(2)$ 得

$$
2 p \sum_{k=1}^{q-1} k\left[\frac{p k}{q}\right] \equiv \sum_{k=1}^{q-1}\left[\frac{p k}{q}\right]^{2} \quad(\bmod q-1)
$$

7. 如图, $\odot O$ 是 $\triangle A B C$ 的外接圆, $A B<A C, \angle B A C=120^{\circ}$. 设 $M$ 是弧 $\widehat{B A C}$ 的中点, 点 $P, Q$ 使得 $P A, P B, Q A, Q C$ 均与 $\odot O$ 相切, $H, I$ 分别是 $\triangle P O Q$ 的垂心和内心, $N$ 是线段 $O I$ 的中点, $D$ 是直线 $M N$ 与 $\odot O$ 的另一个交点. 证明: $I H \perp A D$.

证明. 延长 $B P, C Q$ 相交于点 $L$.

由已知条件可设 $\angle A B C=30^{\circ}+\theta, \angle A C B=30^{\circ}-\theta$. 不难得到

$$
\angle O P A=90^{\circ}-\angle P O A=90^{\circ}-\angle A C B=60^{\circ}+\theta \text {, }
$$

同理 $\angle O Q A=60^{\circ}-\theta$, 因此 $\angle P O Q=60^{\circ}$, 进而

$$
\angle P I Q=\angle P H Q=120^{\circ} \text {. }
$$

又 $O$ 是 $\triangle L P Q$ 的旁心, 所以 $\angle P L Q=2\left(90^{\circ}-\angle P O Q\right)=60^{\circ}$, 故 $L, P, H, I, Q$ 五点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_60abcbc9f7883cbf36deg-09.jpg?height=897&width=717&top_left_y=248&top_left_x=675)

由于 $O I$ 平分 $\angle P O Q$, 并且

$$
\begin{aligned}
& \angle A O I=\angle P O I-\angle P O A=30^{\circ}-\left(30^{\circ}-\theta\right)=\theta \\
& \angle A O M=\angle B O M-\angle B O A=60^{\circ}-2\left(30^{\circ}-\theta\right)=2 \theta
\end{aligned}
$$

所以 $O I$ 平分 $\angle A O M$, 于是

$$
\angle A O N=\angle A O I=\frac{1}{2} \angle A O M=\angle A D M=\angle A D N
$$

进而 $A, N, O, D$ 四点共圆. 设外接圆圆心是 $T$.

延长 $P H$ 到点 $X$. 由内心与垂心的性质可知

$\angle O H I=\angle I H X+\angle O H X=\angle P Q I+\angle O Q P=\frac{3}{2} \angle O Q P=\frac{3}{2}\left(60^{\circ}-\theta\right)=90^{\circ}-\frac{3}{2} \theta$.

注意到在直角 $\triangle L O B$ 中, $\angle B L O=30^{\circ}$, 故 $L O=2 O B=2 O M$, 故 $M N \| L I$.

由于

$$
\begin{aligned}
\angle L I O & =\angle L I Q+\angle Q I O=\angle L P Q+90^{\circ}+\frac{1}{2} \angle O P Q=270^{\circ}-\frac{3}{2} \angle O P Q \\
& =270^{\circ}-\frac{3}{2}\left(60^{\circ}+\theta\right)=180^{\circ}-\frac{3}{2} \theta .
\end{aligned}
$$

因此 $\angle M N I=\angle A N I=\frac{3}{2} \theta, \angle A O D=\angle A N D=180^{\circ}-3 \theta$. 注意到 $O A=O D$,故 $O T$ 平分 $\angle A O D$ 且 $A D \perp O T$, 故

$$
\angle A O T=\frac{1}{2} \angle A O D=90^{\circ}-\frac{3}{2} \theta
$$

于是 $\angle O H I=\angle A O T$. 而 $A, O, H$ 共线, 故 $I H \| O T$. 又 $A D \perp O T$, 所以 $I H \perp A D$.

8. 给定正整数 $n$. 一个有限项正整数列 $\left(a_{1}, \cdots, a_{m}\right)$ 称为 “ $n$-偶数列”:若 $n=a_{1}+\cdots+a_{m}$, 且共有偶数个整数对 $(i, j)$ 满足 $1 \leq i<j \leq m$ 而 $a_{i}>a_{j}$.求 $n$-偶数列的个数.

例如, 共有六个4-偶数列：(4)、(1,3)、(2,2)、(1,1,2)、 $(2,1,1) 、(1,1,1,1)$.

解. 一个有限项正整数列 $\left(a_{1}, \cdots, a_{m}\right)$ 称为 “ $n$-数列”, 若 $n=a_{1}+\cdots+a_{m}$.若 $n$-数列不是 $n-$ 偶数列, 则称为 “ $n$-奇数列”. 记 $S(n)$ 为 $n$-偶数列与 $n$-奇数列的个数之差, 并定义 $S(0)=1$. 下面证明: 对 $n \geq 1$,

$$
S(n)=1+\sum_{k=1}^{\left[\frac{n}{2}\right]} S(n-2 k)
$$

事实上, 我们可以将 $n$-数列分为下面几类（当 $n=1$ 时, 仅有第(i)类; 当 $n=2$ 时, 仅有第(i)(iii)两类）:

(i) $\left(a_{1}\right)=(n)$. 此类 $n$-偶数列与 $n$-奇数列个数之差为 1 ;

(ii) 满足 $a_{1} \neq a_{2}$ 的 $n$-数列. 注意到 $n$-数列 $\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ 与 $\left(a_{2}, a_{1}, \cdots, a_{m}\right)$的奇偶性不同, 从而在满足 $a_{1} \neq a_{2}$ 的 $n$-数列中, $n$-奇数列与 $n$-偶数列的个数相同.

(iii) 满足 $a_{1}=a_{2}$ 的 $n$-数列. 在满足 $a_{1}=a_{2}=k\left(1 \leq k \leq\left[\frac{n}{2}\right]\right)$ 的 $n$-数列中,由于 $\left(a_{1}, \cdots, a_{m}\right)$ 与 $\left(a_{3}, \cdots, a_{m}\right)$ 的奇偶性相同, 故 $n-$ 偶数列与 $n$-奇数列的个数之差恰好是 $S(n-2 k)$ （注意, $n=2 k$ 时, $S(0)=1$ 对应 $(k, k)$ ).综合(i),(ii),(iii)便知 $(*)$ 式成立.

由 $(*)$ 知, 当 $n \geq 3$ 时,

$$
S(n)-S(n-2)=\sum_{k=1}^{\left[\frac{n}{2}\right]} S(n-2 k)-\sum_{k=1}^{\left[\frac{n}{2}-1\right]} S(n-2 k)=S(n-2) .
$$

即 $S(n)=2 S(n-2)$. 当 $n=2$ 时, 亦有 $S(2)=2=2 S(0)$. 因此, 当 $n$ 为奇数时,

$$
S(n)=1+S(1)+S(3)+\cdots+S(n-2)=2^{\frac{n-1}{2}} .
$$

当 $n$ 为偶数时,

$$
S(n)=1+S(0)+S(2)+\cdots+S(n-2)=2^{\frac{n}{2}} .
$$

注意到 $n$-数列 $\left(a_{1}, \cdots, a_{m}\right)$ 与有序数组 $\left(a_{1}, a_{1}+a_{2}, \cdots, a_{1}+a_{2}+\cdots+a_{m}\right)$ 一一对应, 而后者的个数等于 $\{1,2, \cdots, n\}$ 含 $n$ 的子集个数, 故 $n$-数列的总数为 $2^{n-1}$. 从而 $n$-偶数列个数为 $\frac{2^{n-1}+S(n)}{2}=2^{n-2}+2^{\left[\frac{n}{2}\right]-1}$.

