# 上海新星数学奥林匹克试题解答 

施柯杰

(上海大学数学系, 200444)

1. 在锐角 $\triangle A B C$ 中, $A B \neq A C, O, H$ 分别是其外心和垂心, $M$ 为 $B C$ 中点, $D$ 是 $M H$ 与 $\triangle A B C$ 外接圆的交点, 且 $H$ 在 $D, M$ 之间. 证明: $A D, B C, O H$共点当且仅当 $A B^{2}+A C^{2}=2 B C^{2}$.

(于翔宇 供题)

证明 设 $G$ 为 $\triangle A B C$ 的重心, 则由欧拉定理知 $O, G, H$ 共线.

设 $F$ 为直线 $A O$ 与 $M H$ 的交点, 由 $O M / / A H$且 $O M=\frac{1}{2} A H$ 知 $O$ 为 $A F$ 中点, 即 $F$ 为 $A$ 的对径点. 因此 $A F$ 为 $\odot O$ 直径, 故 $A D \perp F D$.



由题意, 不妨设 $A B>A C$. 则此时点 $H$ 与点 $C$ 在直线 $O M$ 同侧, 故点 $D$与点 $C$ 也在 $O M$ 同侧, 从而点 $A$ 与点 $D$ 在 $O M$ 同侧. 又因为 $A, B, C, D$ 均在圆 $O$ 上, 所以 $A D$ 与 $B C$ 不可能平行, 否则 $A, D$ 将在直线 $O M$ 的异侧.

故可设直线 $A D$ 与 $B C$ 交于点 $N$, 直线 $A H$ 与 $B C$ 交于点 $E$, 则 $A E \perp M N$, $M D \perp A N$. 从而 $H$ 为 $\triangle A M N$ 的垂心, 故 $N H \perp A M$. 因此

$$
\begin{aligned}
O H, A D, B C \text { 共点 } & \Leftrightarrow O, H, N \text { 共线 } \\
& \Leftrightarrow O, G, H, N \text { 共线 } \\
& \Leftrightarrow O G \perp A M \\
& \Leftrightarrow A O^{2}-O M^{2}=A G^{2}-G M^{2} .
\end{aligned}
$$

而由中线公式知

$$
\begin{aligned}
& A G^{2}-G M^{2}=\left(\frac{4}{9}-\frac{1}{9}\right) A M^{2}=\frac{1}{6}\left(A B^{2}+A C^{2}-\frac{B C^{2}}{2}\right), \\
& A O^{2}-O M^{2}=B O^{2}-O M^{2}=\frac{1}{4} B C^{2} .
\end{aligned}
$$

故

$$
\begin{aligned}
A O^{2}-O M^{2}=A G^{2}-G M^{2} & \Leftrightarrow \frac{1}{6}\left(A B^{2}+A C^{2}-\frac{B C^{2}}{2}\right)=\frac{1}{4} B C^{2} \\
& \Leftrightarrow A B^{2}+A C^{2}=2 B C^{2}
\end{aligned}
$$

结论得证, 且每一步都是充要的.

2. 设 $n, a_{1}, a_{2}, \cdots, a_{k}$ 均为大于 1 的整数, 使得 $n !$ 被 $a_{1} ! a_{2} ! \cdots a_{k} !$ 整除. 证明

$$
a_{1}+a_{2}+\cdots+a_{k}<\frac{5}{2} n
$$

(余红兵 供题)

证明 用反证法. 假设存在某个满足条件的整数组 $\left(a_{1}, \cdots, a_{k}\right)$, 使得

$$
S_{0}=a_{1}+a_{2}+\cdots+a_{k} \geq \frac{5}{2} n
$$

则在所有满足条件的和为 $S_{0}$ 的数组中取 $k$ 最大的一个, 仍记作 $\left(a_{1}, \cdots, a_{k}\right)$.

若存在 $i(1 \leq i \leq k)$, 使得 $a_{i} \geq 4$, 则考察整数组

$$
\left(a_{1}, \cdots, a_{i-1}, 2, a_{i}-2, a_{i+1}, \cdots, a_{k}\right),
$$

它们和仍为 $S$ 且注意到 $\frac{a_{i} !}{2 !\left(a_{i}-2\right) !}=\mathrm{C}_{a_{i}}^{2}$ 是整数, 从而

$$
a_{1} ! \cdots a_{i-1} ! 2 !\left(a_{i}-2\right) ! a_{i+1} ! \cdots a_{k} ! \quad \mid \quad a_{1} ! \cdots a_{k} !
$$

故新得到数组 $(*)$ 仍符合条件且此时 $k$ 更大, 矛盾!

因此对每个 $i(1 \leq i \leq k)$, 有 $a_{i} \in\{2,3\}$.

设有 $a$ 个 $2, b$ 个 3 , 则

$$
\prod_{i=1}^{k} a_{i} !=2^{n+b} 3^{b} .
$$

所以由条件可知 $2^{a+b}\left|n !, 3^{b}\right| n !$.

记 $\nu_{2}(n !), \nu_{3}(n !)$ 分别表示 $n !$ 中 2 的幂次和 3 的幂次, 则

$$
\begin{aligned}
& \nu_{2}(n !)=\sum_{j=1}^{\infty}\left[\frac{n}{2^{j}}\right]<\sum_{j=1}^{\infty} \frac{n}{2^{j}}=n \\
& \nu_{3}(n !)=\sum_{j=1}^{\infty}\left[\frac{n}{3^{j}}\right]<\sum_{j=1}^{\infty} \frac{n}{3^{j}}=\frac{n}{2} .
\end{aligned}
$$

所以 $a+b<n, b<\frac{n}{2}$. 从而

$$
S_{0}=2 a+3 b<\frac{5}{2} n
$$

矛盾!

3. 正整数序列 $a_{1}, a_{2}, \cdots$ 满足

$$
\min \left(a_{i}, a_{j}\right)=a_{\operatorname{gcd}(i, j)}, \quad \max \left(a_{i}, a_{j}\right)=a_{\operatorname{lcm}(i, j)}
$$

对所有 $i, j \geq 1$ 都成立, 其中 $\operatorname{gcd}(i, j), \operatorname{lcm}(i, j)$ 分别表示 $i, j$ 的最大公约数和最小公倍数. 求 $a_{1}, a_{2}, \cdots, a_{2016}$ 中不同整数个数的最大可能值.

(施柯杰 供题)

解 所求不同整数个数的最大可能值为 11 .

事实上, 我们可以证明任一个满足条件的正整数序列 $a_{1}, a_{2}, \cdots, a_{n}$ 中最多有 $1+\left[\log _{2} n\right]$ 个不同正整数.

为方便计, 记 $a_{1}, a_{2}, \cdots, a_{n}$ 中不同整数的个数为 $S_{n}$.

一方面, 取 $a_{k}=2^{\nu_{2}(k)}(k=1,2, \cdots, n)$, 其中 $\nu_{2}(k)$ 表示 $k$ 的因子中 2 的幂次. 此时对所有 $i, j \geq 1$, 满足

$$
\begin{aligned}
& \min \left(a_{i}, a_{j}\right)=2^{\min \left(\nu_{2}(i), \nu_{2}(j)\right)}=2^{\nu_{2}(\operatorname{gcd}(i, j))}=a_{\operatorname{gcd}(i, j)} \\
& \max \left(a_{i}, a_{j}\right)=2^{\max \left(\nu_{2}(i), \nu_{2}(j)\right)}=2^{\nu_{2}(\operatorname{lcm}(i, j))}=a_{\operatorname{lcm}(i, j)}
\end{aligned}
$$

即序列 $a_{1}, a_{2}, \cdots, a_{n}$ 符合要求, 且此时 $S_{n}=1+\left[\log _{2} n\right]$.

另一方面, 我们用数学归纳法证明 $(*)$, 即 $S_{n} \leq 1+\left[\log _{2} n\right]$.

当 $n=1$ 时, 结论显然成立.

假设结论对所有 $k \leq n-1(n \geq 2)$ 都成立, 考虑 $n$ 时的情形.

对任意 $d>1$, 由于 $\min \left(a_{1}, a_{d}\right)=a_{1}, \max \left(a_{1}, a_{d}\right)=a_{d}$, 从而 $a_{1}=\min _{1 \leq i \leq n} a_{i}$.

若不存在 $d>1$, 使得 $a_{d}>a_{1}$, 则 $S_{n}=1,(*)$ 成立.

反之, 取 $d$ 是满足 $a_{d}>a_{1}$ 最小的数, 即对任意 $d^{\prime}<d$, 均有 $a_{d^{\prime}}=a_{1}$.

对任意 $x>1$, 若 $d \nmid x$, 由于 $\min \left(a_{d}, a_{x}\right)=a_{\operatorname{gcd}(d, x)}$, 而 $\operatorname{gcd}(d, x)<d$, 则由 $d$的最小性, 可知 $\min \left(a_{d}, a_{x}\right)=a_{1}$, 因此 $a_{x}=a_{1}$.

故 $a_{1}, a_{2}, \cdots, a_{n}$ 中不同的整数至多是在 $a_{1}, a_{d}, a_{2 d}, \cdots, a_{\left[\frac{n}{d}\right] d}$ 这 $\left[\frac{n}{d}\right]+1$ 个数中取. 记 $b_{k}=a_{k d}\left(k=1,2, \cdots,\left[\frac{n}{d}\right]\right)$, 则

$$
\begin{aligned}
& \min \left(b_{i}, b_{j}\right)=\min \left(a_{i d}, a_{j d}\right)=a_{\operatorname{gcd}(i, j) d}=b_{\operatorname{gcd}(i, j)}, \\
& \max \left(b_{i}, b_{j}\right)=\max \left(a_{i d}, a_{j d}\right)=a_{\operatorname{lcm}(i, j) d}=b_{\operatorname{lcm}(i, j)} .
\end{aligned}
$$

故序列 $b_{1}, \cdots, b_{\left[\frac{n}{d}\right]}$ 满足题设条件, 由归纳假设, 序列 $b_{1}, \cdots, b_{\left[\frac{n}{d}\right]}$ 中至多有 $\left[\log _{2}\left[\frac{n}{d}\right]\right]+1$ 不同的整数, 从而 $a_{1}, a_{2}, \cdots, a_{n}$ 中不同的整数个数 $S_{n}$ 满足

$$
S_{n} \leq 1+\left[\log _{2}\left[\frac{n}{d}\right]\right]+1 \leq 1+\left[\log _{2} n\right]
$$

故 $(*)$ 得证.

4. 已知 $n$ 为给定的正整数, $S$ 是 $\{1,2, \cdots, n\}$ 的一个子集. 求最小的正整数 $k$, 使得对任意满足 $|S| \geq k$ 的子集 $S$, 都可以找到 $S$ 中若干个元素 (不一定不同) 其和为 2 的幂.

(饶家鼎供题)

解 所求 $k$ 的最小值为 $\left[\frac{n}{3}\right]+1$.

我们先证明如下引理.

引理 设 $a, b$ 是两个互质的正整数, 则存在 $k, l \in \mathbb{N}$, 使得 $k a+l b$ 为 2 的幂.

事实上, 选取 $s \in \mathbb{N}^{*}$, 满足 $2^{s}>a b$.

由于 $(a, b)=1$, 则存在 $k_{0} \in\{0,1, \cdots, b-1\}$, 使得 $k_{0} a \equiv 2^{s}(\bmod b)$. 因此取 $l_{0}=\frac{2^{s}-k_{0} a}{b} \in \mathbb{Z}$, 又

$$
l_{0}=\frac{2^{s}-k_{0} a}{b}>\frac{a b-a b}{b}=0,
$$

故 $l_{0}$ 为正整数. 此时, $k_{0} a+l_{0} b=2^{s}$ 即为所求. 引理得证.

回到原题.

首先考虑 $\{1,2, \cdots, n\}$ 的子集 $\bar{S}=\left\{3 i \mid i=1,2, \cdots,\left[\frac{n}{3}\right]\right\}$, 其中若干个元素之和一定是 3 的倍数, 不为 2 的幂. 这表明 $k>|\bar{S}|=\left[\frac{n}{3}\right]$, 即 $k \geq\left[\frac{n}{3}\right]+1$.

下面证明: 对任意 $S \subseteq\{1,2, \cdots, n\}$ 满足 $|S| \geq\left[\frac{n}{3}\right]+1$, 都可以找到 $S$ 中的若干个元素 (不一定不同), 其和为 2 的幂.

用反证法. 假设不能找到 $S$ 中的若干元素 (这些元素可以相同), 使得其和为 2 幂, 则易知 $1 \notin S, 2 \notin S$.

考虑如下 $\left[\frac{n}{3}\right]$ 个集合

$$
S_{i}=\{n-3 i, n-3 i-1, n-3 i-2\}, i=0,1,2, \cdots,\left[\frac{n}{3}\right]-1 .
$$

这样的 $S_{i}$ 将集合 $\{3,4, \cdots, n\}$ 分成了 $\left[\frac{n}{3}\right]$ 组, 又 $1,2 \notin S$, 则

$$
S \subseteq S_{0} \cup S_{1} \cup \cdots \cup S_{\left[\frac{n}{3}\right]-1}
$$

因为 $|S|>\left[\frac{n}{3}\right]$, 由抽屉原理, 必存在正整数 $m$, 使得

$$
|S \cap\{m, m+1, m+2\}| \geq 2 \text {. }
$$

由于 $(m, m+1)=(m+1, m+2)=1,(m, m+2)=1$ 或 2 , 故必存在 $a, b \in S$,使得 $(a, b)=1$ 或 $(a, b)=2$.

若 $(a, b)=1$, 则由引理知存在 $k, l \in \mathbb{N}$, 使得 $k a+l b$ 为 2 的幂, 矛盾!

若 $(a, b)=2$, 则 $\left(\frac{a}{2}, \frac{b}{2}\right)=1$, 再由引理知存在 $k, l \in \mathbb{N}$, 使得 $k \frac{a}{2}+l \frac{b}{2}$ 为 2 的幂. 此时 $k a+l b$ 也为 2 的幂, 矛盾!

故 $(*)$ 得证.

5. 设 $O$ 为锐角 $\triangle A B C$ 的外心, 点 $P$ 是 $\triangle A B C$ 的内点, $P$ 关于边 $B C$ 的中点的对称点为 $P_{a}, P_{a}$ 关于边 $B C$ 的对称点为 $Q_{a}, A Q_{a}$ 的中点记为 $R_{a}$. 同样可定义 $R_{b}, R_{c}$. 证明:

$$
\frac{S_{\triangle R_{a} R_{b} R_{c}}}{S_{\triangle A B C}}=\frac{1}{4}\left(1-\frac{O P^{2}}{O A^{2}}\right)
$$

(王逸轩熊昱滔 供题)

证明 设 $M, N$ 分别为 $P_{c} P, P_{c} Q_{c}$ 与 $A B$的交点, 则 $M N$ 为 $\triangle P P_{c} Q_{c}$ 中位线.

从而 $P Q_{c} / / A B$ 且 $P Q_{c}=2 M N$, 即 $P Q_{c}$关于 $A B$ 中垂线 $O M$ 对称. 所以 $O P=O Q_{c}$.同样 $O P=O Q_{a}=O Q_{b}$. 故 $P, Q_{a}, Q_{b}, Q_{c}$ 共圆.



由于 $P Q_{c} / / A B, P Q_{a} / / B C$, 因此 $\angle Q_{c} P Q_{a}=\angle A B C$. 而由 $P, Q_{a}, Q_{b}, Q_{c}$ 共圆可得 $\angle Q_{a} Q_{b} Q_{c}=\angle Q_{c} P Q_{a}$, 故 $\angle Q_{a} Q_{b} Q_{c}=\angle A B C$. 同理可得 $\angle Q_{c} Q_{a} Q_{b}=$ $\angle C A B, \angle Q_{a} Q_{b} Q_{c}=\angle A C B$. 故 $\triangle Q_{a} Q_{b} Q_{c} \backsim \triangle A B C$.

又 $O$ 为 $\triangle Q_{a} Q_{b} Q_{c}$ 与 $\triangle A B C$ 的公共外心, 从而 $\triangle O Q_{a} Q_{c} \sim \triangle O A C$ (逆向相似). 因此

$$
\frac{O Q_{a}}{O Q_{c}}=\frac{O A}{O C}, \angle Q_{c} O Q_{a}=\angle C O A,
$$

从而

$$
O Q_{a} \cdot O C=O A \cdot O Q_{c}, \angle C O Q_{a}=\angle A O Q_{c}
$$

以下三角形面积均为有向面积 (即顺时针为正, 逆时针为负), 则

$$
S_{A O Q_{c}}=S_{C O Q_{a}}=-S_{Q_{a} O C}
$$

因为 $R_{a}, R_{c}$ 为 $A Q_{a}, C Q_{c}$ 的中点, 故

$$
\begin{aligned}
S_{R_{a} O R_{c}} & =\frac{1}{2}\left(S_{A O R_{c}}+S_{Q_{a} O R_{c}}\right) \\
& =\frac{1}{4}\left(S_{A O Q_{c}}+S_{A O C}+S_{Q_{a} O C}+S_{Q_{a} O Q_{c}}\right) \\
& =\frac{1}{4}\left(S_{A O C}+S_{Q_{a} O Q_{c}}\right) .
\end{aligned}
$$

同理,

$$
S_{R_{a} O R_{b}}=\frac{1}{4}\left(S_{A O B}+S_{Q_{a} O Q_{b}}\right), \quad S_{R_{b} O R_{c}}=\frac{1}{4}\left(S_{B O C}+S_{Q_{b} O Q_{c}}\right) .
$$

故

$$
S_{R_{a} R_{b} R_{c}}=S_{R_{a} O R_{b}}+S_{R_{c} O R_{a}}+S_{R_{b} O R_{c}}
$$

$$
=\frac{1}{4}\left(S_{A B C}+S_{Q_{a} Q_{b} Q_{c}}\right) .
$$

另一方面, 由逆向相似得

$$
S_{Q_{a} Q_{b} Q_{c}}=-\frac{O P^{2}}{O A^{2}} \cdot S_{A B C}
$$

因此

$$
S_{\triangle R_{a} R_{b} R_{c}}=\frac{1}{4}\left(1-\frac{O P^{2}}{O A^{2}}\right) S_{\triangle A B C}
$$

6. 设 $z \in \mathbb{C}, n \in \mathbb{N}(n \geq 2)$, 证明:

$$
\left|1+z+z^{2}+\cdots+z^{n-1}\right|^{2} \leq\left(1+|z|^{2}+\frac{2}{n-1} \operatorname{Re} z\right)^{n-1} .
$$

(冷岗松 供题)

证明 注意到

$$
\begin{aligned}
1+z+z^{2}+\cdots+z^{n-1} & =\frac{z^{n}-1}{z-1}=\frac{\prod_{k=1}^{n}\left(z-e^{\frac{2 \pi i k}{n}}\right)}{z-1} \\
& =\prod_{k=1}^{n-1}\left(z-e^{\frac{2 \pi i k}{n}}\right),
\end{aligned}
$$

又因为

$$
\sum_{k=1}^{n} e^{\frac{2 \pi i k}{n}}=0 \Longleftrightarrow \sum_{k=1}^{n-1} e^{\frac{2 \pi i k}{n}}=-1
$$

因此

$$
\begin{aligned}
& \left|1+z+z^{2}+\cdots+z^{n-1}\right|^{\frac{2}{n-1}}=\prod_{k=1}^{n-1}\left|z-e^{\frac{2 \pi i k}{n}}\right|^{\frac{2}{n-1}} \\
& =\prod_{k=1}^{n-1}\left(1-z \cdot e^{\frac{-2 \pi i k}{n}}-\bar{z} \cdot e^{\frac{2 \pi i k}{n}}+|z|^{2}\right)^{\frac{1}{n-1}} \\
& \leq \sum_{k=1}^{n-1} \frac{1-z \cdot e^{\frac{-2 \pi i k}{n}}-\bar{z} \cdot e^{\frac{2 \pi i k}{n}}+|z|^{2}}{n-1}=1+|z|^{2}+\frac{z+\bar{z}}{n-1} \\
& =1+|z|^{2}+\frac{2}{n-1} \operatorname{Re}(z) .
\end{aligned}
$$

