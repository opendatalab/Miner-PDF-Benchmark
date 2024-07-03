# 第 39 届 CMO 试题解答与评析 

叶语行

(中国人民大学附属中学, 100080)

本次中国数学奥林匹克 (CMO) 试题第 1,4 题为简单题, 容易上手; 第 2,5 题为中档题, 有一定难度; 第 3,6 题非常困难, 其中第 3 题复杂度高, 第 6 题思维难度高.

本文是根据作者考场上的作答整理而来的, 方法不一定最优, 但体现了一定的思考过程. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 求最小的实数 $\lambda$, 使得对任意正整数 $n$, 存在正整数 $x_{1}, x_{2}, \cdots, x_{2023}$, 满足 $n=x_{1} x_{2} \cdots x_{2023}$, 且对任意 $i \in\{1,2, \cdots, 2023\}$, 均有 $x_{i}$ 为素数或 $x_{i} \leq n^{\lambda}$.
2. 求最大的实数 $C$, 使得对任意正整数 $n$ 和任意实数 $x_{1}, x_{2}, \cdots, x_{n}$, 均有

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}(n-|j-i|) x_{i} x_{j} \geq C \sum_{i=1}^{n} x_{i}^{2}
$$

3. 给定素数 $p \geq 5$, 记 $\Omega=\{1,2, \cdots, p\}$. 定义 $r(x, y)$ 如下:

$$
r(x, y)=\left\{\begin{array}{ll}
y-x, & y \geq x \\
y-x+p, & y<x
\end{array} .\right.
$$

对 $\Omega$ 的子集 $A$, 定义

$$
f(A)=\sum_{x \in A} \sum_{y \in A}(r(x, y))^{2}
$$

称集合 $A$ 为“好的”，如果 $0<|A|<p$, 且对任意 $B \subseteq \Omega,|B|=|A|$, 都有 $f(B) \geq f(A)$. 求最大的整数 $L$, 使得存在 $L$ 个不同的好子集 $A_{1}, A_{2}, \cdots, A_{L}$, 满足 $A_{1} \subseteq A_{2} \subseteq \cdots \subseteq A_{L}$.

修订日期: 2024-01-09.

4. 已知 $a_{1}, a_{2}, \cdots, a_{2023}$ 为非负实数, 满足 $a_{1}+a_{2}+\cdots+a_{2023}=100$. 设集合

$$
N=\left\{(i, j) \mid 1 \leq i \leq j \leq 2023, a_{i} a_{j} \geq 1\right\}
$$

证明: $|N| \leq 5050$, 并给出等号成立的充分必要条件.

5. 在锐角 $\triangle A B C$ 中, $K$ 是 $B C$ 延长线上的一点. 过 $K$ 分别作 $A B, A C$ 的平行线 $K P, K Q$, 满足 $B K=B P, C K=C Q$. 设 $\triangle K P Q$ 的外接圆与 $A K$ 交于点 $T$, 证明:

(1) $\angle B T C+\angle A P B=\angle C Q A$;

(2) $A P \cdot B T \cdot C Q=A Q \cdot C T \cdot B P$.

6. 称 $1,2, \cdots, 99$ 放置在正 99 边形的顶点使每个顶点恰有一个数的方式为一个状态. 称两个状态为等同的, 若它们在旋转之后重合. 称交换相邻两个顶点上的数为一次操作. 求最小的正整数 $N$, 使得对任意两个状态 $\alpha, \beta$, 都可对 $\alpha$ 进行不超过 $N$ 次操作变为与 $\beta$ 等同的状态.

## II. 解答与评注

题 1 求最小的实数 $\lambda$, 使得对任意正整数 $n$, 存在正整数 $x_{1}, x_{2}, \cdots, x_{2023}$,满足 $n=x_{1} x_{2} \cdots x_{2023}$, 且对任意 $i \in\{1,2, \cdots, 2023\}$, 均有 $x_{i}$ 为素数或 $x_{i} \leq n^{\lambda}$.

解 $\lambda$ 的最小值为 $\frac{1}{1012}$.

一方面, 取 $n=2^{2024}$, 则 $x_{1}, x_{2}, \cdots, x_{2023}$ 均为 2 的幂. 由抽屉原理, 存在 $1 \leq i \leq 2023$ 使 $x_{i} \geq 4$. 此时 $x_{i}$ 不为素数, 于是 $n^{\lambda} \geq x_{i} \geq 4$, 故 $\lambda \geq \frac{1}{1012}$.

另一方面, 我们证明 $\lambda=\frac{1}{1012}$ 符合要求.

一般地, 我们证明: 对任意正整数 $m, n$, 存在正整数 $x_{1}, x_{2}, \cdots, x_{m}$, 满足 $n=x_{1} x_{2} \cdots x_{m}$, 且对 $i \in\{1,2, \cdots, m\}$, 要么 $x_{i}$ 为素数、要么 $x_{i} \leq n^{\frac{2}{m+1}}$.

对 $m$ 归纳.

当 $m=1$ 时, 取 $x_{1}=n$ 即可. 假设命题对 $m-1$ 成立, 来看 $m$ 时的情形.

若存在 $m$ 的素因子 $p$ 使 $p \geq n^{\frac{1}{m+1}}$, 取 $x_{m}=p$. 由归纳假设, 存在正整数 $x_{1}, x_{2}, \cdots, x_{m-1}$, 满足 $\frac{n}{p}=x_{1} x_{2} \cdots x_{m-1}$, 且对 $i \in\{1,2, \cdots, m-1\}$, 要么 $x_{i}$ 为素数、要么 $x_{i} \leq\left(\frac{n}{p}\right)^{\frac{2}{m}}$. 因为 $n=x_{1} x_{2} \cdots x_{m}$ 且

$$
\left(\frac{n}{p}\right)^{\frac{2}{m}} \leq\left(n^{\frac{m}{m+1}}\right)^{\frac{2}{m}}=n^{\frac{2}{m+1}}
$$

所以满足要求.

若对 $m$ 的任意素因子 $p$, 都有 $p \leq n^{\frac{1}{m+1}}$, 取 $n$ 的最大的正因子 $n^{\prime}$, 使得 $n^{\prime}$可以写为 $y_{1} y_{2} \cdots y_{m}$, 其中 $y_{1}, y_{2}, \cdots, y_{m} \leq n^{\frac{2}{m+1}}$. (由 $1=1^{m}$ 知 $n^{\prime}$ 存在)

若 $n^{\prime}=n$, 取 $x_{i}=y_{i}$ 即可. 若 $n^{\prime} \neq n$, 则存在 $\frac{n}{n^{\prime}}$ 的素因子 $q$, 有 $q \leq n^{\frac{1}{m+1}}$. 对任意 $1 \leq i \leq m$, 因为 $n^{\prime} q=y_{1} \cdots\left(y_{i} q\right) \cdots y_{m}$, 所以由 $n^{\prime}$ 的最大性, $y_{i} q>n^{\frac{2}{m+1}}$,即 $y_{i}>\frac{1}{q} \cdot n^{\frac{2}{m+1}}$. 这样,

$$
n \geq y_{1} y_{2} \cdots y_{m} q>\left(\frac{1}{q} \cdot n^{\frac{2}{m+1}}\right)^{m} q \geq n^{\frac{2 m}{m+1}-\frac{m-1}{m+1}}=n
$$

矛盾!

归纳证毕.

综上, $\lambda$ 的最小值为 $\frac{1}{1012}$.

评注 本题为简单的数论背景的组合题, 以上做法本质上为贪心算法, 通过 $m=2$ 时的经典结论而启发.

题 2 求最大的实数 $C$, 使得对任意正整数 $n$ 和任意实数 $x_{1}, x_{2}, \cdots, x_{n}$, 均有

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}(n-|j-i|) x_{i} x_{j} \geq C \sum_{i=1}^{n} x_{i}^{2}
$$

解 $C$ 的最大值为 $\frac{1}{2}$.

先证明

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n}(n-|j-i|) x_{i} x_{j} \\
= & \sum_{s=1}^{n}\left(x_{1}+\cdots+x_{s}\right)^{2}+\sum_{t=2}^{n}\left(x_{t}+x_{t+1}+\cdots+x_{n}\right)^{2} .
\end{aligned}
$$

对 $1 \leq i \leq j \leq n$, 比较 $(*)$ 两边 $x_{i} x_{j}$ 的系数.

当 $i=j$ 时, 左边为 $n$, 右边为 $(n+1-i)+(i-1)=n$.

当 $i<j$ 时, 左边为 $2(n-j+i)$, 右边为 $2(n+1-j)+2(i-1)=2(n-j+i)$.

故 $(*)$ 恒成立.

再证明当 $C=\frac{1}{2}$ 时原不等式成立.

当 $n=1$ 时, 即为 $x_{1}^{2} \geq \frac{1}{2} x_{1}^{2}$, 成立.

当 $n=2$ 时, 即为

$$
x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+x_{2}^{2} \geq \frac{1}{2}\left(x_{1}^{2}+x_{2}^{2}\right) \text {, }
$$

成立.
当 $n \geq 3$ 时, 若 $n$ 为奇数, 设 $n=2 k+1$. 由 $(*)$ 及均值不等式,

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n}(n-|j-i|) x_{i} x_{j} \\
= & x_{1}^{2}+\sum_{s=1}^{k}\left(\left(x_{1}+\cdots+x_{2 s}\right)^{2}+\left(x_{1}+\cdots+x_{2 s+1}\right)^{2}\right) \\
& +\sum_{t=1}^{k}\left(\left(x_{2 t}+\cdots+x_{n}\right)^{2}+\left(x_{2 t+1}+\cdots+x_{n}\right)^{2}\right) \\
\geq & \frac{1}{2} x_{1}^{2}+\frac{1}{2} \sum_{s=1}^{k} x_{2 s+1}^{2}+\frac{1}{2} \sum_{t=1}^{k} x_{2 t}^{2}=\frac{1}{2} \sum_{i=1}^{n} x_{i}^{2} .
\end{aligned}
$$

若 $n$ 为偶数, 设 $n=2 k+2$. 由 $(*)$ 及均值不等式,

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n}(n-|j-i|) x_{i} x_{j} \\
= & x_{1}^{2}+\sum_{s=1}^{k}\left(\left(x_{1}+\cdots+x_{2 s}\right)^{2}+\left(x_{1}+\cdots+x_{2 s+1}\right)^{2}\right) \\
& +\sum_{t=1}^{k}\left(\left(x_{2 t}+\cdots+x_{n}\right)^{2}+\left(x_{2 t+1}+\cdots+x_{n}\right)^{2}\right) \\
& +x_{2 k+2}^{2}+\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2} \\
\geq & \frac{1}{2} x_{1}^{2}+\frac{1}{2} \sum_{s=1}^{k} x_{2 s+1}^{2}+\frac{1}{2} \sum_{t=1}^{k} x_{2 t}^{2}+\frac{1}{2} x_{2 k+2}^{2}=\frac{1}{2} \sum_{i=1}^{n} x_{i}^{2} .
\end{aligned}
$$

最后证明 $C \leq \frac{1}{2}$.

取 $n=2 k+1, x_{1}=k, x_{i+1}=(-1)^{i}(2 k+1-i)(i=1,2, \cdots, 2 k)$. 则

$$
\sum_{i=1}^{n} x_{i}^{2}=k^{2}+\frac{1}{3} k(2 k+1)(4 k+1)
$$

且结合 $(*)$,

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}(n-|j-i|) x_{i} x_{j}=4 \sum_{i=1}^{k} i^{2}=\frac{2}{3} k(k+1)(2 k+1) .
$$

故

$$
\frac{2}{3} k(k+1)(2 k+1) \geq C\left(k^{2}+\frac{1}{3} k(2 k+1)(4 k+1)\right),
$$

令 $k \rightarrow \infty$ 得 $C \leq \frac{1}{2}$.

综上, $C$ 的最大值为 $\frac{1}{2}$.

评注 本题为中等难度的代数问题, 与二次型不等式有关. 首先要发现 $(*)$式的配方, 再由此证明 $C=\frac{1}{2}$ 满足要求. 构造需要找到尽量满足不等式取等的一组变量, 此处仅为一种构造方式.
题 3 给定素数 $p \geq 5$, 记 $\Omega=\{1,2, \cdots, p\}$. 定义 $r(x, y)$ 如下:

$$
r(x, y)=\left\{\begin{array}{ll}
y-x, & y \geq x \\
y-x+p, & y<x
\end{array} .\right.
$$

对 $\Omega$ 的子集 $A$, 定义

$$
f(A)=\sum_{x \in A} \sum_{y \in A}(r(x, y))^{2}
$$

称集合 $A$ 为“好的”，如果 $0<|A|<p$, 且对任意 $B \subseteq \Omega,|B|=|A|$, 都有 $f(B) \geq f(A)$. 求最大的整数 $L$, 使得存在 $L$ 个不同的好子集 $A_{1}, A_{2}, \cdots, A_{L}$, 满足 $A_{1} \subseteq A_{2} \subseteq \cdots \subseteq A_{L}$.

解 $L$ 的最大值为 $2\left[\log _{2}(p+1)\right]$.

以下 $\Omega$ 中的运算均在模 $p$ 下进行.

先给出好子集的若干性质.

对一元子集 $A, f(A)=0$, 故 $A$ 为好子集. 下对 $2 \leq k \leq p-1$ 考虑 $k$ 元好子集.

性质 1 对 $k$ 元子集 $A$,

$$
f(A) \geq \sum_{d=1}^{k-1}\left(d p\left(2\left[\frac{d p}{k}\right]+1\right)-k\left[\frac{d p}{k}\right]\left(\left[\frac{d p}{k}\right]+1\right)\right) .
$$

证明 设 $A=\left\{x_{1}, x_{2}, \cdots, x_{k}\right\}$, 其中 $1 \leq x_{1}<x_{2}<\cdots<x_{k} \leq p$, 且下标按模 $k$ 理解. 因为对 $1 \leq d \leq k-1,1 \leq i \leq k$,

$$
\left(r\left(x_{i}, x_{i+d}\right)-\left[\frac{d p}{k}\right]\right)\left(r\left(x_{i}, x_{i+d}\right)-\left[\frac{d p}{k}\right]-1\right) \geq 0
$$

所以

$$
\begin{aligned}
f(A) & =\sum_{d=1}^{k-1} \sum_{i=1}^{k} r\left(x_{i}, x_{i+d}\right)^{2} \\
& \geq \sum_{d=1}^{k-1} \sum_{i=1}^{k}\left(r\left(x_{i}, x_{i+d}\right)\left(2\left[\frac{d p}{k}\right]+1\right)-\left[\frac{d p}{k}\right]\left(\left[\frac{d p}{k}\right]+1\right)\right) \\
& =\sum_{d=1}^{k-1}\left(d p\left(2\left[\frac{d p}{k}\right]+1\right)-k\left[\frac{d p}{k}\right]\left(\left[\frac{d p}{k}\right]+1\right)\right) .
\end{aligned}
$$

性质 $2 S_{k}=\left\{\left[\frac{p}{k}\right],\left[\frac{2 p}{k}\right], \cdots,\left[\frac{k p}{k}\right]\right\}$ 为好子集.

证明 $x_{i}$ 定义同上, 则对 $1 \leq d \leq k-1,1 \leq i \leq k$ ，

$$
r\left(x_{i}, x_{i+d}\right)=\left[\frac{(i+d) p}{k}\right]-\left[\frac{i p}{k}\right]=\left[\frac{d p}{k}\right] \text { 或 }\left[\frac{d p}{k}\right]+1 \text {, }
$$

因此 (1) 中不等式取等. 故对任意 $k$ 元子集 $A, f(A) \geq f\left(S_{k}\right)$, 从而 $S_{k}$ 为好子集.
性质 3 对任意 $k$ 元好子集 $A$, 存在整数 $c$ 使 $A=S_{k}+c$, 这里 $B+c=$ $\{b+c \mid b \in B\}$.

证明 $x_{i}$ 定义同上. 取 $1 \leq j \leq k$ 使 $x_{j}-\frac{j p}{k}$ 最大. 此时对 $1 \leq d \leq k-1$,

$$
r\left(x_{j}, x_{j+d}\right) \leq\left(x_{j}-\frac{j p}{k}+\frac{(j+d) p}{k}\right)-x_{j}=\frac{d p}{k} .
$$

由 $f(A) \leq f\left(S_{k}\right)$ 知 (1) 中不等式取等, 即

$$
r\left(x_{j}, x_{j+d}\right) \in\left\{\left[\frac{d p}{k}\right],\left[\frac{d p}{k}\right]+1\right\} .
$$

因此 $r\left(x_{j}, x_{j+d}\right)=\left[\frac{d p}{k}\right]$, 取 $c=x_{j}$ 即可.

性质 4 存在整数 $c_{k}$, 使得 $S_{k}+c_{k}$ 与 $S_{p-k}$ 为 $\Omega$ 的划分.

证明 取 $c_{k}$ 满足 $c_{k} \cdot k \equiv-1(\bmod p)$.

若 $x \in S_{k}+c_{k}$, 则 $x-c_{k} \in S_{k}$,

$$
\begin{gathered}
k\left(x-c_{k}\right) \equiv 0,-1, \cdots,-(k-1) \quad(\bmod p), \\
k x \equiv-1,-2, \cdots,-k \quad(\bmod p) .
\end{gathered}
$$

若 $x \in S_{p-k}$, 则

$$
\begin{aligned}
(p-k) x & \equiv 0,-1, \cdots,-(p-k-1) \quad(\bmod p) \\
k x & \equiv 0,1, \cdots, p-k-1 \quad(\bmod p) .
\end{aligned}
$$

故 $\left(S_{k}+c_{k}\right) \cap S_{p-k}=\emptyset$, 结合 $\left|S_{k}+c_{k}\right|+\left|S_{p-k}\right|=p$ 知其为 $\Omega$ 的划分.

以下记 $t_{k}=\left[\frac{p}{k}\right], 1 \leq k \leq p-1$.

性质 5 若 $1 \leq k<l \leq \frac{p-1}{2}, A$ 为 $k$ 元好子集, $B$ 为 $l$ 元好子集, 满足 $A \subseteq B$,则 $l \geq 2 k$ 或 $\left(t_{k}, t_{l}\right)=(3,2)$.

证明 在圆周上等距顺时针摆放 $1,2, \cdots, p$, 将 $A$ 中的元素染黑、 $B \backslash A$ 中的元素染红.

当 $k=1$ 时命题成立. 当 $k \geq 2$ 时, 由性质 2,3 知相邻两个黑点距离为 $t_{k}$ 或 $t_{k}+1$, 相邻两个染色点距离为 $t_{l}$ 或 $t_{l}+1$.

当 $l<2 k$ 时, 红点数 $l-k$ 小于黑点数 $k$, 所以存在两个黑点之间无红点, 故 $t_{k} \leq t_{l}+1$. 又存在两个黑点之间有红点, 故 $t_{k}+1 \geq 2 t_{l}$. 因此 $2 t_{l} \leq t_{k}+1 \leq t_{l}+2$,即 $t_{l} \leq 2$. 由 $l \leq \frac{p-1}{2}$ 知 $t_{l}=2$, 进而 $t_{k}=3$.

性质 6 若 $1 \leq k<l \leq \frac{p-1}{2}, A$ 为 $k$ 元好子集, $B$ 为 $l$ 元好子集, $A \subseteq B$ 且 $\left(t_{k}, t_{l}\right)=(3,2)$, 则 $p=4 k-1=2 l+1$.

证明 圆周定义同上, 则距离为 3 的黑点之间无红点, 距离为 4 的黑点之间有一个红点. 因此, 只需证明恰有一对距离为 3 的黑点.
对相邻两个染色点, 若距离为 3 , 则称它们之间为黑弧, 否则为红弧. 结合性质 3 , 通过旋转, 可不妨设 $B=S_{l}$.

对于染色点 $\left[\frac{i p}{l}\right]$, 它逆时针方向上一个点为 $\left[\frac{(i-1) p}{l}\right]$, 间距为

$$
\left[\frac{i p}{l}\right]-\left[\frac{(i-1) p}{l}\right]=t_{l} \text { 或 } t_{l}+1,
$$

即 2 或 3 , 当且仅当 $\left\{\frac{i p}{l}\right\} \leq\left\{\frac{p}{l}\right\}-\frac{1}{l}$ 时间距为 3 . 记 $m=l\left\{\frac{p}{l}\right\}$, 注意到

$$
\begin{aligned}
& \left\{\frac{i p}{l}\right\} \leq\left\{\frac{p}{l}\right\}-\frac{1}{l} \\
\Longleftrightarrow & i p \equiv 0,1, \cdots, l\left\{\frac{p}{l}\right\}-1 \quad(\bmod l) \\
\Longleftrightarrow & i m \equiv 0,1, \cdots, m-1 \quad(\bmod l) \\
\Longleftrightarrow & \text { 存在整数 } j \text { 使 } \frac{j l}{m} \leq i \leq \frac{j l}{m}+\frac{m-1}{m} \\
\Longleftrightarrow & \text { 存在整数 } j \text { 使 } i=\left\lceil\frac{j l}{m}\right\rceil .
\end{aligned}
$$

于是这样的 $i$ 相邻两个之差为 $\left[\frac{l}{m}\right]$ 或 $\left[\frac{l}{m}\right]+1$, 故相邻两段黑弧之间有 $\left[\frac{l}{m}\right]-1$或 $\left[\frac{l}{m}\right]$ 段红弧, 又它们之间有偶数段红弧, 故它们之间的红弧个数为定值 $u$.

设共有 $v$ 段黑弧, 则 $p=v(3+2 u)$, 由 $p$ 为素数知 $v=1$, 得证.

性质 7 若 $1 \leq k \leq \frac{p-1}{2}$, 则 $S_{k} \subseteq S_{p-k}+\left(1-c_{k}\right)$.

证明 结合性质 4 , 只需证明 $S_{k} \subseteq \Omega \backslash\left(S_{k}+1\right)$.

由 $t_{k} \geq 2$ 知对任意 $x \in S_{k}$, 有 $x-1 \notin S_{k}, x \notin S_{k}+1, x \in \Omega \backslash\left(S_{k}+1\right)$, 故 $S_{k} \subseteq \Omega \backslash\left(S_{k}+1\right)$, 得证.

回到原题. 先证明 $L \leq 2\left[\log _{2}(p+1)\right]$.

补充定义 $A_{0}=\emptyset, A_{L+1}=\Omega$. 取 $0 \leq M \leq L$ 使 $\left|A_{M}\right| \leq \frac{p-1}{2}<\left|A_{M+1}\right|$.

若对任意 $1 \leq i \leq M-1$, 都有 $\left|A_{i+1}\right| \geq 2\left|A_{i}\right|$, 则

$M \leq 1+\left[\log _{2}\left|A_{M}\right|\right] \leq 1+\left[\log _{2} \frac{p-1}{2}\right] \leq\left[\log _{2}(p-1)\right] \leq\left[\log _{2}(p+1)\right]$.

若存在 $1 \leq j \leq M-1$ 使 $\left|A_{j+1}\right|<2\left|A_{j}\right|$, 由性质 5,6 知 $\left|A_{j}\right|=\frac{p+1}{4},\left|A_{j+1}\right|=$ $\frac{p-1}{2}$. 故 $j+1=M$,

$$
M \leq 2+\left[\log _{2}\left|A_{M-1}\right|\right]=2+\left[\log _{2} \frac{p+1}{4}\right]=\left[\log _{2}(p+1)\right]
$$

因此总有 $M \leq\left[\log _{2}(p+1)\right]$.

由性质 $2,3,4$ 知 $\Omega \backslash A_{M+1}, \Omega \backslash A_{M+2}, \cdots, \Omega \backslash A_{L}$ 为好子集. 结合

$$
\Omega \backslash A_{L} \subseteq \Omega \backslash A_{L-1} \subseteq \cdots \subseteq \Omega \backslash A_{M+1}
$$

且 $\left|\Omega \backslash A_{M+1}\right|<\frac{p-1}{2}$, 同理有 $L-M \leq\left[\log _{2}(p+1)\right]$, 故 $L \leq 2\left[\log _{2}(p+1)\right]$.
再给出 $L=2\left[\log _{2}(p+1)\right]$ 的构造.

记 $\left[\log _{2}(p+1)\right]=\alpha$. 若 $p \neq 2^{\alpha}-1$, 则 $\frac{p-1}{2} \geq 2^{\alpha-1}$.

令

$$
A_{i}= \begin{cases}S_{2^{i-1}}, & 1 \leq i \leq \alpha, \\ \Omega \backslash\left(S_{2^{2 \alpha-i}}+1\right), & \alpha+1 \leq i \leq 2 \alpha .\end{cases}
$$

由性质 $2,3,4$ 知 $A_{i}$ 为好子集, 由 $S_{k}$ 的定义与性质 7 知 $A_{1} \subseteq A_{2} \subseteq \cdots \subseteq A_{L}$ 且互不相同, 故 $A_{1}, A_{2}, \cdots, A_{L}$ 符合题意.

若 $p=2^{\alpha}-1$, 则 $\alpha \geq 3$, 注意到 $S_{\frac{p+1}{4}} \subseteq S_{\frac{p-1}{2}}+3$.

令

$$
A_{i}= \begin{cases}S_{2^{i-1}}, & 1 \leq i \leq \alpha-1, \\ S_{\frac{p-1}{2}}+3, & i=\alpha \\ \Omega \backslash\left(S_{\frac{p-1}{2}}+4\right), & i=\alpha+1 \\ \Omega \backslash\left(S_{2^{i-1}}+1\right), & \alpha+2 \leq i \leq 2 \alpha\end{cases}
$$

由性质 $2,3,4$ 知 $A_{i}$ 为好子集, 由 $S_{k}$ 定义、性质 7 和 (2) 知 $A_{1} \subseteq A_{2} \subseteq \cdots \subseteq A_{L}$且互不相同, 故 $A_{1}, A_{2}, \cdots, A_{L}$ 符合题意.

综上, $L$ 的最大值为 $2\left[\log _{2}(p+1)\right]$.

评注 本题非常困难, 同时考查了代数、数论和组合. 首先要通过发现“均匀分布”, 借助高斯函数给出好子集的刻画。接下来发现较小一半相邻两个至少差几乎一倍, 且较大一半可通过取补集转化为较小的而完成. 具体细节还需要很多细致讨论。

题 4 已知 $a_{1}, a_{2}, \cdots, a_{2023}$ 为非负实数, 满足 $a_{1}+a_{2}+\cdots+a_{2023}=100$. 设集合

$$
N=\left\{(i, j) \mid 1 \leq i \leq j \leq 2023, a_{i} a_{j} \geq 1\right\}
$$

证明: $|N| \leq 5050$, 并给出等号成立的充分必要条件.

证明 对 $m$ 归纳证明: 对非负实数 $a_{1}, a_{2}, \cdots, a_{m}$, 记 $S=a_{1}+a_{2}+\cdots+a_{m}$,

$$
N=\left|\left\{(i, j) \mid 1 \leq i \leq j \leq m, a_{i} a_{j} \geq 1\right\}\right|
$$

则 $|N| \leq \frac{S(S+1)}{2}$, 且取等时 $a_{i} \in\{0,1\}$.

$$
\text { 当 } m=1 \text { 时, }|N|=\left\{\begin{array}{ll}
0, & a_{1}<1 \\
1, & a_{1} \geq 1
\end{array}\right. \text {, 命题成立. }
$$

假设命题对 $m$ 成立, 来看 $m+1$ 时的情形.

若对任意 $1 \leq i \leq m$, 都有 $a_{i} \geq 1$, 则 $|N|=\frac{m(m+1)}{2} \leq \frac{S(S+1)}{2}$. 取等时, $S=m, a_{1}=a_{2}=\cdots=a_{m}=1$, 命题成立.

若存在 $1 \leq i \leq m$ 使 $a_{i}<1$, 不妨 $i=1$.

若 $a_{1}=0$, 则 $N=\left\{(i, j) \mid 2 \leq i \leq j \leq m, a_{i} a_{j} \geq 1\right\}$. 由归纳假设, $|N| \leq \frac{S(S+1)}{2}$, 且取等时 $a_{2}, \cdots, a_{m} \in\{0,1\}$, 命题成立.

若 $a_{1}>0$, 则至多存在 $\frac{S-a_{1}}{\frac{1}{a_{1}}}=a_{1}\left(S-a_{1}\right)$ 个 $2 \leq j \leq m$, 使得 $a_{1} a_{j} \geq 1$. 又由归纳假设,

$$
\left|\left\{(i, j) \mid 2 \leq i \leq j \leq m, a_{i} a_{j} \geq 1\right\}\right| \leq \frac{\left(S-a_{1}\right)\left(S-a_{1}+1\right)}{2}
$$

故

$$
\begin{aligned}
|N| & \leq a_{1}\left(S-a_{1}\right)+\frac{\left(S-a_{1}\right)\left(S-a_{1}+1\right)}{2} \\
& =\frac{S(S+1)}{2}-\frac{a_{1}\left(a_{1}+1\right)}{2}<\frac{S(S+1)}{2}
\end{aligned}
$$

不能取等, 命题成立.

归纳得证.

回到原题. 取 $m=2023, S=100$ 知 $N \leq \frac{100 \cdot 101}{2}=5050$. 取等时, $a_{1}, a_{2}, \cdots$, $a_{2023} \in\{0,1\}$, 即 $a_{1}, a_{2}, \cdots, a_{2023}$ 中有 100 个 1 和 1923 个 0.

评注 本题为简单的代数题, 方法众多, 也可通过直接对条件平方证明.

题 5 在锐角 $\triangle A B C$ 中, $K$ 是 $B C$ 延长线上的一点. 过 $K$ 分别作 $A B, A C$的平行线 $K P, K Q$, 满足 $B K=B P, C K=C Q$. 设 $\triangle K P Q$ 的外接圆与 $A K$ 交于点 $T$, 证明:

(1) $\angle B T C+\angle A P B=\angle C Q A$;

(2) $A P \cdot B T \cdot C Q=A Q \cdot C T \cdot B P$.

证明 设 $A$ 在 $\triangle A B C$ 外接圆中的对径点为 $A^{\prime}$, 则 $B A^{\prime} \perp A B$, 进而 $B A^{\prime} \perp K P$.结合 $B K=B P$ 知 $A^{\prime} K=A^{\prime} P$. 同理 $A^{\prime} K=A^{\prime} Q$, 故 $A^{\prime}$ 为 $\triangle K P Q$ 外接圆的圆心.

设 $D$ 是 $A^{\prime}$ 在 $A K$ 上的投影, 则 $D$ 为 $T K$ 的中点, 且 $D$ 在 $\triangle A B C$ 的外接圆上.

取 $A K$ 的中点 $M$, 延长 $B M$ 至 $B^{\prime}$, 使得 $B^{\prime} M=B M$, 则 $A B$ 与 $B^{\prime} K$ 平行且相等, 所以 $B^{\prime}, K, P$ 共线. 又 $B K=P B$, 且

$$
\angle B^{\prime} K B=180^{\circ}-\angle B K P=180^{\circ}-\angle B P K=\angle A B P \text {, }
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_908e0489be5fd4b40ec8g-10.jpg?height=645&width=671&top_left_y=223&top_left_x=698)

所以 $\triangle B^{\prime} K B \cong \triangle A B P$.

由此, $\angle M B K=\angle A P B$, 且 $M B=\frac{1}{2} B B^{\prime}=\frac{1}{2} A P$.

同理, $\angle M C K=\angle C Q A$, 且 $M C=\frac{1}{2} A Q$.

注意到

$$
K T \cdot K M=2 K D \cdot \frac{1}{2} K A=K B \cdot K C
$$

故 $B, C, M, T$ 四点共圆.

(1) 有

$$
\angle C Q A-\angle A P B=\angle M C K-\angle M B K=\angle B M C=\angle B T C .
$$

(2) 有

$$
\begin{aligned}
\frac{A P \cdot B T}{A Q \cdot C T} & =\frac{2 M B \cdot B T}{2 M C \cdot C T}=\frac{M B \cdot B T \cdot \sin \angle M B T}{M C \cdot C T \cdot \sin \angle M C T} \\
& =\frac{S_{\triangle M B T}}{S_{\triangle M C T}}=\frac{B K}{C K}=\frac{B P}{C Q} .
\end{aligned}
$$

综上, 命题得证.

评注本题为比较简单的平面几何题. 首先要发现圆心为 $A$ 的对径点, 再引入 $M$ 点对角度进行转化. 发现 $B, C, M, T$ 共圆后, 两问都迎刃而解了.

题 6 称 1, 2, , , 99 放置在正 99 边形的顶点使每个顶点恰有一个数的方式为一个状态. 称两个状态为等同的, 若它们在旋转之后重合. 称交换相邻两个顶点上的数为一次操作. 求最小的正整数 $N$, 使得对任意两个状态 $\alpha, \beta$, 都可对 $\alpha$进行不超过 $N$ 次操作变为与 $\beta$ 等同的状态.

解 $N$ 的最小值为 2401 .
先证明 $N \geq 2401$.

设 $\alpha$ 为 $1,2, \cdots, 99$ 依次顺时针排列, $\beta$ 为 $1,2, \cdots, 99$ 依次逆时针排列. 对任意 $1 \leq i<j<k \leq 99, i, j, k$ 在 $\alpha, \beta$ 中的相对位置不同, 因此 $i, j, k$ 中有两个交换过, 即不存在 3 个数两两未被交换. 由 Turán 定理, 至多 $\left[\frac{99^{2}}{4}\right]$ 对数未被交换, 因此至少进行 $\mathrm{C}_{99}^{2}-\left[\frac{99^{2}}{4}\right]=2401$ 次交换.

再证明 $N=2401$ 满足要求.

对 $1 \leq i \leq 99$ 和状态 $\alpha, \beta$, 若 $i$ 在 $\alpha, \beta$ 中所在顶点重合, 则记 $d_{i}(\alpha, \beta)=0$;若不重合, 设这两个顶点之间边数较少一侧有 $l$ 条边, 则记 $d_{i}(\alpha, \beta)=l-\frac{1}{2}$. 再记 $d(\alpha, \beta)=\sum_{i=1}^{99} d_{i}(\alpha, \beta)$.

对 $2 d(\alpha, \beta)$ 归纳证明: 对状态 $\alpha, \beta$, 可用不超过 $d(\alpha, \beta)$ 次操作将 $\alpha$ 变为与 $\beta$ 等同的状态.

当 $2 d(\alpha, \beta)=0$ 时, $\alpha$ 与 $\beta$ 相同, 命题成立.

假设对正整数 $d$, 当 $2 d(\alpha, \beta) \leq d-1$ 时命题成立, 来看 $2 d(\alpha, \beta)=d$ 时的情形.

对 $1 \leq i \leq 99$, 若 $i$ 在 $\alpha, \beta$ 中的位置不同, 则从 $i$ 在 $\alpha$ 中顶点到 $i$ 在 $\beta$ 中顶点沿边数较少一侧作一条有向边. 若 $i$ 在 $\alpha, \beta$ 中的位置相同, 则称 $i$ 所在顶点为不动点.

情形 1 : 存在两个顶点 $u, v$, 使从 $u$ 顺时针到 $v$ 经过的顶点均为不动点, 且 $u$发出顺时针边, $v$ 发出逆时针边.

设 $u, v$ 之间的顶点依次为 $w_{1}, w_{2}, \cdots, w_{t}$, 依次操作

$$
u w_{1}, w_{1} w_{2}, \cdots, w_{t} v, w_{t-1} w_{t}, \cdots, w_{1} w_{2}, u w_{1}
$$

共 $2 t+1$ 次, 变为 $\alpha^{\prime}$. 则 $\alpha^{\prime}$ 与 $\alpha$ 仅将 $u, v$ 处的数交换.

设 $u, v$ 处的数初始为 $j_{1}, j_{2}$, 则对 $k \in\{1,2\}$,

$$
d_{j_{k}}(\alpha, \beta)-d_{j_{k}}\left(\alpha^{\prime}, \beta\right) \geq t+\frac{1}{2}
$$

且对 $i \notin\left\{j_{1}, j_{2}\right\}, d_{i}(\alpha, \beta)=d_{i}\left(\alpha^{\prime}, \beta\right)$. 对 $\alpha^{\prime}$ 与 $\beta$ 用归纳假设, 结合

$$
d(\alpha, \beta)-d\left(\alpha^{\prime}, \beta\right) \geq 2\left(t+\frac{1}{2}\right)=2 t+1
$$

即证

情形 2: 不存在 $u, v$ 满足 (1).

由 $d(\alpha, \beta)>0$ 知至少有一条有向边, 不妨设为顺时针的.

从这条有向边的起点沿顺时针走, 直到下一个有向边的起点, 则它也为顺时针的. 依此类推, 所有有向边均为顺时针的.
对每一段连续的不动点 $w_{1}, \cdots, w_{t}\left(w_{1}\right.$ 逆时针上一个顶点 $u 、 w_{t}$ 顺时针下一个顶点 $v$ 均不为不动点), 依次操作 $u w_{1}, w_{1} w_{2}, \cdots, w_{t-1} w_{t}$, 得到 $\alpha^{\prime}$, 再将 $\beta$ 逆时针旋转 $\frac{2 \pi}{99}$ 变为 $\beta^{\prime}$.

设所有不动点段的长度为 $t_{1}, t_{2}, \cdots, t_{k}$, 则共操作 $t_{1}+t_{2}+\cdots+t_{k}$ 次. 对 $1 \leq i \leq 99$, 若 $i$ 初始在 $\alpha$ 中位于某个 $u$, 则

$$
d_{i}(\alpha, \beta)-d_{i}\left(\alpha^{\prime}, \beta^{\prime}\right) \geq t_{j}+\frac{1}{2}
$$

这里 $t_{j}$ 为 $i$ 顺时针方向一段不动点的长度. 若 $i$ 初始在 $\alpha$ 中不位于任一个 $u$, 则 $d_{i}(\alpha, \beta) \geq d_{i}\left(\alpha^{\prime}, \beta^{\prime}\right)$. 故

$$
d(\alpha, \beta)-d\left(\alpha^{\prime}, \beta^{\prime}\right) \geq t_{1}+\cdots+t_{k}+\frac{k}{2} \geq t_{1}+\cdots+t_{k}
$$

对 $\alpha^{\prime}, \beta^{\prime}$ 用归纳假设即证.

归纳得证.

回到原题. 对 $1 \leq r \leq 99$, 记 $\beta_{r}$ 为 $\beta$ 顺时针旋转 $\frac{2 \pi r}{99}$ 的状态, 则

$$
\begin{aligned}
& \sum_{r=1}^{99} d\left(\alpha, \beta_{r}\right)=\sum_{r=1}^{99} \sum_{i=1}^{99} d_{i}\left(\alpha, \beta_{r}\right)=\sum_{i=1}^{99} \sum_{r=1}^{99} d_{i}\left(\alpha, \beta_{r}\right) \\
= & \sum_{i=1}^{99}\left(\frac{1}{2}+\frac{1}{2}+\frac{3}{2}+\frac{3}{2}+\cdots+\frac{97}{2}+\frac{97}{2}\right)=99 \cdot 49^{2} .
\end{aligned}
$$

故存在 $1 \leq r \leq 99$, 使得 $d\left(\alpha, \beta_{r}\right) \leq 49^{2}=2401$.

由已证, 可用不超过 $d\left(\alpha, \beta_{r}\right)$ 次操作将 $\alpha$ 变为与 $\beta_{r}$ 等同、即与 $\beta$ 等同的状态, 故 $N=2401$ 满足要求.

综上, $N$ 的最小值为 2401 .

评注 本题似易实难, 下界可通过猜测极端情形得到. 上界的半不变量构造可通过极端情形猜测出距离函数, 再微调而得到, 需要很多尝试. 上界也可通过将数分成四组来证明.

