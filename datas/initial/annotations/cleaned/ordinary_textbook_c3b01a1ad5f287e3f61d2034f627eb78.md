# 第四十期问题征解解答与点评 

张端阳

第一题 在锐角 $\triangle A B C$ 中, $O$ 是外心, $M$ 是高 $A D$ 的中点, $\angle A$ 内的旁切圆 $\odot I_{a}$ 与 $B C$ 切于点 $E$, 与 $A B 、 A C$ 的延长线分别切于点 $P 、 Q$. 设 $O I_{a}$ 与 $M E$交于点 $T, T P 、 T Q$ 分别与 $\odot I_{a}$ 交于另一点 $X 、 Y$. 证明: 直线 $A T$ 是 $\triangle A B X$与 $\triangle A C Y$ 的外接圆的根轴.

(长沙一中学生 胡冬础 供题)

证明 (根据巴蜀中学罗智文同学的解答整理):



设 $\odot O$ 与 $\odot I_{a}$ 交于 $U, V$ 两点, 重新定义 $T$ 是 $\odot I_{a}$ 在 $U, V$ 处切线的交点, 则 $T$ 在 $O I_{a}$ 上. 下面证明 $T$ 在 $M E$ 上.

设直线 $P Q, B C$ 交于点 $S$, 则易知 $A E$ 是 $S$ 关于 $\odot I_{a}$ 的极线, 所以 $A E \perp S I_{a}$.又 $A D \perp S E, D E \perp E I_{a}$, 所以 $\triangle A D E \sim \triangle S E I_{a}$.

设直线 $U V, B C$ 交于点 $R$, 则

$$
R E^{2}=R U \cdot R V=R B \cdot R C .
$$

结合 $S, E ; B, C$ 是调和点列, 知 $R$ 是 $S E$ 的中点.

因为 $M$ 是 $A D$ 的中点, 所以 $M, R$ 是上述相似的对应点, 于是 $M E \perp R I_{a}$.
又易知 $T E$ 是 $R$ 关于 $\odot I_{a}$ 的极线, 故 $T$ 在 $M E$ 上.



此时 $U Y V Q$ 是调和四边形, 延长 $U V$ 交 $A Q$ 于点 $W$, 则 $W Y$ 是 $\odot I_{a}$ 的切线.

因为 $W Y^{2}=W U \cdot W V=W A \cdot W C$, 所以 $\triangle A C Y$ 的外接圆与 $W Y$ 相切,进而 $\triangle A C Y$ 的外接圆与 $\odot I_{a}$ 相切. 同理, $\triangle A B X$ 的外接圆与 $\odot I_{a}$ 相切.

设 $\odot I_{a}$ 在 $X, Y$ 处的切线交于点 $Z$, 则 $Z$ 在 $\triangle A B X$ 与 $\triangle A C Y$ 的外接圆的根轴上, 从而 $A Z$ 是这两个圆的根轴.

对退化的圆内接六边形 $P P X Q Q Y$ 用帕斯卡定理得, $A, T$ 及 $P Y$ 与 $Q X$ 的交点共线. 对退化的圆内接六边形 $P X X Q Y Y$ 用帕斯卡定理得, $T, Z$ 及 $P Y$ 与 $Q X$ 的交点共线. 故 $A, T, Z$ 共线.

综上, 命题得证.

评注 (1). 不少同学在证明中用到了熟知的结论 $E, I, M$ 共线. 有些同学发现了 $T$ 是 $\triangle P E Q$ 与 $\triangle I_{b} I_{c}$ 的位似中心, 其中 $I_{b}, I_{c}$ 是 $\triangle A B C$ 的另外两个旁心.

(2). 杭州学军中学叶梓、缪何尔、蒋昊、施敖, 武汉市武钢三中王迪, 石家庄二中王旭华, 上海中学刘胤辰, 南昌市第二中学李嘉睿、于沣林, 浙江温州中学金晟治, 华南师大附中戴子一, 湖南师大附中艾宇航, 巴蜀中学胡子渊, 深圳中学汪千桐等同学也给出了本题的正确解答.

第二题 证明: 存在无穷多个正整数 $n$, 使得 $n$ 不是幂, 且 $\sigma(\sigma(n))$ 与 $\tau(n)$ 互素, 其中 $\sigma$ 与 $\tau$ 分别表示因数和与因数个数.

注: 在本题中, 幂指形如 $a^{b}$ 的数, 其中 $a, b$ 是大于 1 的整数.

(湖南师大附中学生 刘宇东 供题)

## 证明 1 (根据浙江温州中学金晟治同学的解答整理):

取 $p$ 为任意大于 100 的素数, 我们证明 $n=2^{p-1} 3^{p-1}$ 满足要求.

记

$$
m=\frac{\left(2^{p}-1\right)\left(3^{p}-1\right)}{2}
$$

则 $\sigma(\sigma(n))=\sigma(m), \tau(n)=p^{2}$.

设 $q$ 是 $m$ 的任意一个素因子. 由 $p$ 是奇素数知 $q$ 是奇素数, 结合阶的性质，由 $q \mid 2^{p}-1$ 或 $q \mid 3^{p}-1$ 均能得到 $q \equiv 1(\bmod p)$, 特别有 $q>p$.

因为 $m$ 的所有素因子均模 $p$ 余 1 , 所以

$$
\sigma(m) \equiv \tau(m) \quad(\bmod p)
$$

设 $q^{\alpha} \| m$, 若 $p \mid \tau\left(q^{\alpha}\right)=\alpha+1$, 则 $\alpha \geq p-1$. 但这导致

$$
6^{p}>m \geq q^{\alpha}>p^{p-1},
$$

与 $p>100$ 矛盾!

从而 $p \nmid \tau\left(q^{\alpha}\right)$, 进而 $p \nmid \tau(m)$, 即 $p \nmid \sigma(m)$, 故 $(\sigma(\sigma(n)), \tau(n))=1$.

综上, 命题得证.

## 证明 2 (根据湖南师大附中陈思遇同学的解答整理)：

只需证明对任意正整数 $N$, 存在整数 $n>N$ 满足要求.

将素数从小到大排列为 $p_{1}, p_{2}, \cdots$. 取定正整数 $k$, 使得 $p_{k}>N$, 并待定充分大的正整数 $M$. 设 $\left(p_{k}+1\right)\left(p_{k+1}+1\right) \cdots\left(p_{M}+1\right)$ 的所有奇素因子为 $q_{1}<q_{2}<\cdots<q_{t}$, 则 $q_{t} \leq \frac{p_{M}+1}{2}$.

对 $\{k, k+1, \cdots, M\}$ 的任意非空子集 $I$, 记在 $\prod_{i \in I}\left(p_{i}+1\right)$ 的奇数部分的素因数分解中, 指数为奇数的素数的下标集为 $T_{I}$, 则 $T_{I}$ 是 $\{1,2, \cdots, t\}$ 的子集.

由素数定理, 可取 $M$ 充分大, 使得区间 $\left(\frac{p_{M}+1}{2}, p_{M}\right)$ 中素数的个数超过 $k$. 结合 $q_{t} \leq \frac{p_{M}+1}{2}$ 知 $M \geq k+t$, 于是 $2^{M-k+1}-1>2^{t}$.

此时 $\{k, k+1, \cdots, M\}$ 的非空子集的个数多于 $\{1,2, \cdots, t\}$ 的子集的个数,所以由抽屉原理, 存在 $\{k, k+1, \cdots, M\}$ 的不同的非空子集 $I, J$, 使得 $T_{I}=T_{J}$.

令

$$
n=\prod_{i \in I \triangle J} p_{i}
$$

其中 “ $\triangle$ ” 表示对称差, 则 $n$ 不是幂, $n \geq p_{k}>N$, 且

$$
\sigma(n)=\prod_{i \in I \triangle J}\left(p_{i}+1\right)
$$

由 $T_{I}=T_{J}$ 知 $\sigma(n)$ 的奇数部分为完全平方数, 于是 $\sigma(\sigma(n))$ 为奇数. 而 $\tau(n)$为 2 的幂, 故 $(\sigma(\sigma(n)), \tau(n))=1$.

综上, 命题得证.

评注 华南师大附中戴子一, 上海中学刘胤辰, 石家庄二中王旭华, 武汉市武钢三中王迪, 杭州学军中学缪何泉、叶梓等同学都给出了类似证明二的解答.这种证法基于如下经典的命题: 存在无穷多个正整数 $n$, 使得 $\sigma(n)$ 是完全平方数.

第三题 设正整数 $k \leq n$. $T$ 是有 $n$ 个顶点的树, 且有 $k$ 个树叶. 证明: 可以用 $1,2, \cdots, n$ 将 $T$ 的顶点编号, 使得任意一边的两个顶点编号之差的绝对值不超过 $\left\lceil\frac{k}{2}\right\rceil$.

(上海大学 冷岗松 供题)

## 证明 (根据浙江温州中学金晟治同学的解答整理):

先说明只需在每个顶点上标不同的整数, 使得任意相邻两个顶点的标数之差的绝对值不超过 $\left\lceil\frac{k}{2}\right\rceil$.

事实上, 将所标的 $n$ 个数从小到大排列为 $a_{1}<a_{2}<\cdots<a_{n}$. 由 $\left|a_{i}-a_{j}\right| \geq|i-j|$, 知将标为 $a_{i}$ 的顶点编号为 $i$ 即可.

对 $k$ 归纳.

当 $k=2$ 时, $T$ 是一条链, 将 $1,2, \cdots, n$ 顺次标在链的每个顶点上即可.

当 $k=3$ 时, 恰有一个顶点 $x$ 的度为 3 , 且 $T$ 是以 $x$ 为起点的三条链之并. 在 $x$ 上标 0 , 在第一条链上顺次标 $-1,-3,-5, \cdots$, 在第二条链上顺次标 $-2,-4,-6, \cdots$, 在第三条链上顺次标 $0,1,2, \cdots$ 即可.

假设 $k \geq 4$ 且命题对 $k-2$ 成立, 来看 $k$ 时的情形.

存在一个顶点 $x$ 的度不小于 3 .

若 $\operatorname{deg} x \geq 4$, 则任取两个树叶 $u, v$, 使得从 $u$ 到 $v$ 的链经过 $x$.

若 $\operatorname{deg} x=3$, 则存在一个树叶 $u$, 使得从 $u$ 到 $x$ 的链上有另一个度不小于 3 的顶点 $y$ (否则 $T$ 为以 $x$ 为起点的三条链之并, 只有 3 个树叶, 矛盾!) 再任取一个不同于 $u$ 的树叶 $v$, 使得从 $u$ 到 $v$ 的链经过 $x$. 此时从 $u$ 到 $v$ 的链上有两个不同的顶点 $x, y$, 度均不小于 3 .

设从 $u$ 到 $v$ 的链为

$$
u=v_{0}-v_{1}-\cdots-v_{m}=v
$$

再设

$$
\begin{aligned}
& s=\min \left\{1 \leq i \leq m-1 \mid \operatorname{deg} v_{i} \geq 3\right\} \\
& t=\max \left\{1 \leq i \leq m-1 \mid \operatorname{deg} v_{i} \geq 3\right\}
\end{aligned}
$$

由上面的讨论, $s, t$ 定义良好, 且或者 $s<t$ 或者 $s=t, \operatorname{deg} s \geq 4$.

设从 $T$ 中去掉顶点 $v_{0}, v_{1}, \cdots, v_{s-1}, v_{t+1}, \cdots, v_{m}$ 后得到 $T^{\prime}$. 则 $T^{\prime}$ 仍为树,且 $T^{\prime}$ 的所有树叶为 $T$ 的所有树叶去掉 $u, v$, 共 $k-2$ 个.

记 $\left\lceil\frac{k}{2}\right\rceil=c$. 由归纳假设, 可将 $T^{\prime}$ 的顶点标为不同的整数, 使得任意相邻两个顶点的标数之差的绝对值不超过 $c-1$.

对 $T^{\prime}$ 中的任意一个顶点 $A$, 设 $A$ 的标数为 $f(A)=q(c-1)+r$, 其中 $q, r \in \mathbb{Z}, 1 \leq r \leq c-1$, 现将其重新标数为 $g(A)=q c+r$.

此时 $T^{\prime}$ 中所有顶点的新标数不被 $c$ 整除且互不相同, 并且任意相邻两个顶点的标数之差的绝对值不超过 $c$.

不妨设 $g\left(v_{s}\right) \leq g\left(v_{t}\right)$, 记 $\left[\frac{g\left(v_{s}\right)}{c}\right]=a,\left\lceil\frac{g\left(v_{t}\right)}{c}\right\rceil=b$, 则 $a<b$.

对 $0 \leq i \leq s-1$, 令

$$
g\left(v_{i}\right)=a c-(s-1-i) c
$$

对 $t+1 \leq i \leq m$, 令

$$
g\left(v_{i}\right)=b c+(i-t-1) c .
$$

现将 $T$ 的所有顶点按 $g$ 标数, 则 $n$ 个顶点的标数互不相同, 且相邻两个顶点的标数之差的绝对值不超过 $c$.

归纳证毕.

综上, 命题得证.

评注 (1). 本题是论文 The bandwidth of a tree with $k$ leaves is at most $\left\lceil\frac{k}{2}\right\rceil$中的结果, 其弱化版本曾作为 2021 年新星春季数学奥林匹克的第二题.

(2). 武汉市武钢三中王迪, 上海中学刘胤辰, 湖南师大附中艾宇航等同学也给出了本题的正确解答.

第四题 给定正整数 $k, n$. 求最大的实数 $\lambda$, 使得对任意满足 $\sum_{i=1}^{n} x_{i}=k n$ 的正实数 $x_{1}, x_{2}, \cdots, x_{n}$, 都有 $\sum_{i=1}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}} \geq \lambda$.

(温州育英国际实验学校学生 林逸沿 供题)

## 解 (根据人大附中陈锐韬同学的解答整理):

当 $n \leq k$ 时, 我们证明 $\lambda$ 的最大值为 $\frac{(k n-n+1)^{2}}{k n}$.

一方面, 取

$$
\begin{gathered}
x_{1}=x_{2}=\cdots=x_{n-1}=\frac{(k-1) k n}{k n-n+1}=k-1+\frac{(k-1)(n-1)}{k n-n+1}, \\
x_{n}=\frac{k^{2} n}{k n-n+1}=k+\frac{k(n-1)}{k n-n+1} .
\end{gathered}
$$

容易验证 $\sum_{i=1}^{n} x_{i}=k n$, 且由 $n \leq k$ 知

$$
0 \leq \frac{(k-1)(n-1)}{k n-n+1} \leq \frac{k(n-1)}{k n-n+1}<1 .
$$

所以

$$
\sum_{i=1}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}}=(n-1) \cdot \frac{(k-1)^{2}}{\frac{(k-1) k n}{k n-n+1}}+\frac{k^{2}}{\frac{k^{2} n}{k n-n+1}}=\frac{(k n-n+1)^{2}}{k n}
$$

另一方面, 由

$$
\sum_{i=1}^{n}\left[x_{i}\right]=\sum_{i=1}^{n} x_{i}-\sum_{i=1}^{n}\left\{x_{i}\right\}>k n-n
$$

知

$$
\sum_{i=1}^{n}\left[x_{i}\right] \geq k n-n+1
$$

所以由柯西不等式,

$$
\sum_{i=1}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}} \geq \frac{\left(\sum_{i=1}^{n}\left[x_{i}\right]\right)^{2}}{\sum_{i=1}^{n} x_{i}} \geq \frac{(k n-n+1)^{2}}{k n}
$$

当 $n \geq k+1$ 时, 我们证明 $\lambda$ 的最大值为

$$
\frac{(n-1)^{2}(k-1)^{2}}{k n-k-1}+\frac{k^{2}}{k+1}
$$

其中当 $k=1, n=2$ 时为 $\frac{1}{2}$.

一方面, 对充分小的正实数 $\delta$, 取

$$
\begin{gathered}
x_{1}=x_{2}=\cdots=x_{n-1}=\frac{k n-k-1}{n-1}+\delta=k-1+\frac{n-2}{n-1}+\delta, \\
x_{n}=k+1-(n-1) \delta .
\end{gathered}
$$

容易验证 $\sum_{i=1}^{n} x_{i}=k n$, 且当 $\delta \rightarrow 0$ 时,

$$
\sum_{i=1}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}} \rightarrow \frac{(n-1)^{2}(k-1)^{2}}{k n-k-1}+\frac{k^{2}}{k+1}
$$

另一方面, 我们证明

$$
\sum_{i=1}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}} \geq \frac{(n-1)^{2}(k-1)^{2}}{k n-k-1}+\frac{k^{2}}{k+1}
$$

第一步, 记 $S=\sum_{i=1}^{n}\left[x_{i}\right]$, 上面已证 $S \geq k n-n+1$.

若 $S \geq k n-n+2$, 则 $\sum_{i=1}^{n}\left\{x_{i}\right\} \leq n-2$. 不妨设 $\left[x_{1}\right]=a>0$, 并记 $\left\{x_{1}\right\}=\varepsilon$.

由

$$
\varepsilon<1 \leq \frac{2 a^{2}-a}{(a-1)^{2}}
$$

知

$$
\frac{a^{2}}{a+\varepsilon}>\frac{(a-1)^{2}}{a}
$$

所以存在充分小的正实数 $\eta$, 使得

$$
\frac{a^{2}}{a+\varepsilon}>\frac{(a-1)^{2}}{a-\eta} .
$$

因为 $\sum_{i=2}^{n}\left\{x_{i}\right\} \leq n-2-\varepsilon$, 所以可适当增大 $x_{2}, \cdots, x_{n}$, 使得 $\left[x_{2}\right], \cdots,\left[x_{n}\right]$ 不变, 且总共增加 $\varepsilon+\eta$, 得到 $x_{2}^{\prime}, \cdots, x_{n}^{\prime}$. 再令 $x_{1}^{\prime}=a-\eta$, 则 $\sum_{i=1}^{n} x_{i}^{\prime}=k n$,

$$
\frac{\left[x_{1}\right]^{2}}{x_{1}}=\frac{a^{2}}{a+\varepsilon}>\frac{(a-1)^{2}}{a-\eta}=\frac{\left[x_{1}^{\prime}\right]^{2}}{x_{1}^{\prime}}, \quad \sum_{i=2}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}}>\sum_{i=2}^{n} \frac{\left[x_{i}^{\prime}\right]^{2}}{x_{i}^{\prime}}
$$

且

$$
\sum_{i=1}^{n}\left[x_{i}^{\prime}\right]=\sum_{i=1}^{n}\left[x_{i}\right]-1
$$

因此可不断调整使得 $S=k n-n+1$.

第二步, 不妨设 $\left[x_{1}\right\rceil \geq\left\lceil\frac{k n-n+1}{n}\right\rceil=k$. 由柯西不等式,

$$
\sum_{i=1}^{n} \frac{\left[x_{i}\right]^{2}}{x_{i}} \geq \frac{\left[x_{1}\right]^{2}}{x_{1}}+\frac{\left(S-\left[x_{1}\right]\right)^{2}}{k n-x_{1}}
$$

情形 1 : 当 $\left[x_{1}\right]=k$ 时,

$$
\frac{\left[x_{1}\right]^{2}}{x_{1}}+\frac{\left(S-\left[x_{1}\right]\right)^{2}}{k n-x_{1}}=\frac{k^{2}}{x_{1}}+\frac{(S-k)^{2}}{k n-x_{1}} .
$$

记

$$
f(x)=\frac{k^{2}}{x}+\frac{(S-k)^{2}}{k n-x}
$$

解

$$
f^{\prime}(x)=-\frac{k^{2}}{x^{2}}+\frac{(S-k)^{2}}{(k n-x)^{2}} \geq 0,
$$

得

$$
x \geq \frac{k^{2} n}{S}=\frac{k^{2} n}{k n-n+1} \geq k+1
$$

因为 $x_{1} \leq k+1$, 所以

$$
f\left(x_{1}\right) \geq f(k+1)=\frac{k^{2}}{k+1}+\frac{(n-1)^{2}(k-1)^{2}}{k n-k+1}
$$

情形 2 : 当 $\left[x_{1}\right] \geq k+1$ 时, 记 $a=\left[x_{1}\right]$, 则

$$
\begin{aligned}
\frac{\left[x_{1}\right]^{2}}{x_{1}}+\frac{\left(S-\left[x_{1}\right]\right)^{2}}{k n-x_{1}} & =\frac{a^{2}}{x_{1}}+\frac{(S-a)^{2}}{k n-x_{1}} \\
& =\left(\frac{1}{x_{1}}+\frac{1}{k n-x_{1}}\right) a^{2}-\frac{2 S}{k n-x_{1}} a+\frac{S^{2}}{k n-x_{1}} .
\end{aligned}
$$

这是关于 $a$ 的二次函数, 开口向上, 对称轴

$$
\frac{\frac{S}{k n-x_{1}}}{\frac{1}{x_{1}}+\frac{1}{k n-x_{1}}}=\frac{S x_{1}}{k n}=\frac{(k n-n+1) x_{1}}{k n} \leq x_{1}-1,
$$

其中最后一步用到了 $x_{1} \geq k+1, n \geq k+1$. 于是当 $a=x_{1}-1$ 时取到最小值.

记 $b=x_{1}-1 \geq k$, 则

$$
\frac{a^{2}}{x_{1}}+\frac{(S-a)^{2}}{k n-x_{1}} \geq \frac{b^{2}}{b+1}+\frac{(S-b)^{2}}{k n-b-1} .
$$

最后证明当 $b \geq k$ 时,

$$
\frac{b^{2}}{b+1}+\frac{(S-b)^{2}}{k n-b-1} \geq \frac{k^{2}}{k+1}+\frac{(S-k)^{2}}{k n-k-1} .
$$

事实上，

$$
\begin{aligned}
(*) & \Leftrightarrow \frac{b^{2}}{b+1}-\frac{k^{2}}{k+1} \geq \frac{(S-k)^{2}}{k n-k-1}-\frac{(S-b)^{2}}{k n-b-1} \\
& \Leftrightarrow \frac{b^{2} k-b k^{2}+b^{2}-k^{2}}{(b+1)(k+1)} \geq \frac{(k n-1)\left((S-k)^{2}-(S-b)^{2}\right)+k(S-b)^{2}-b(S-k)^{2}}{(k n-k-1)(k n-b-1)} \\
& \Leftrightarrow \frac{(b k+b+k)(b-k)}{(b+1)(k+1)} \geq \frac{(k n-1)(2 S-k-b)(b-k)+\left(b k-S^{2}\right)(b-k)}{(k n-k-1)(k n-b-1)} \\
& \Leftrightarrow \frac{b k+b+k}{(b+1)(k+1)} \geq \frac{(k n-1)(2 S-k-b)+\left(b k-S^{2}\right)}{(k n-k-1)(k n-b-1)} \\
& \Leftrightarrow 1-\frac{1}{(b+1)(k+1)} \geq 1-\frac{(k n-1-S)^{2}}{(k n-k-1)(k n-b-1)} \\
& \Leftrightarrow(b+1)(k+1)(n-2)^{2}-(k n-k-1)(k n-b-1) \geq 0 .
\end{aligned}
$$

上式左边是关于 $b$ 的一次函数, 系数

$$
(k+1)(n-2)^{2}+(k n-k-1) \geq 0,
$$

因此只需证明当 $b=k$ 时成立. 而这等价于

$$
(k+1)(n-2)-(k n-k-1) \geq 0 \Leftrightarrow n \geq k+1 \text {, }
$$

成立.

综上, 所求最大值为

$$
\left\{\begin{array}{ll}
\frac{(k n-n+1)^{2}}{k n}, & n \leq k \\
\frac{(n-1)^{2}(k-1)^{2}}{k n-k-1}+\frac{k^{2}}{k+1}, & n \geq k+1
\end{array} .\right.
$$

评注 长沙麓山国际实验学校童吴阳, 杭州学军中学叶梓、周箴言, 武汉市武钢三中王迪, 石家庄二中王旭华, 华南师大附中戴子一, 巴蜀中学杨皓瑜, 广西师大附外叶骐铭, 湖南师大附中学生艾宇航等同学也给出了本题的正确解答.

