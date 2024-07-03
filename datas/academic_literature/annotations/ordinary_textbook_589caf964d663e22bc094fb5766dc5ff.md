数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 贝蒂一瑞利定理与一道数列问题的探究与思考 

刘家瑜<br>(长沙市中雅培粹学校, 410007)<br>指导教师: 申东

贝蒂-瑞利定理是有关正整数划分的著名定理, 形式和结构都十分漂亮, 在一些与数列相关的问题中可以有巧妙的应用. 本文将探讨一个经典的数列问题,当中蕴含着该定理的妙用.

## I. 预备知识

1. 正整数集上的互补数列定义.

正整数数列 $\left\{x_{n}\right\},\left\{y_{n}\right\}$ 如果满足:

(1) 对任意的 $i, j \in \mathbb{N}_{+}, i \neq j$, 均有 $x_{i} \neq x_{j}, y_{i} \neq y_{j}$;

(2) 对任意的 $i, j \in \mathbb{N}_{+}$, 均有 $x_{i} \neq y_{j}$;

(3) 集合 $\left\{x_{1}, x_{2}, \cdots\right\}$ 与 $\left\{y_{1}, y_{2}, \cdots\right\}$ 的并集为 $\mathbb{N}_{+}$.

则称数列 $\left\{x_{n}\right\}$ 与 $\left\{y_{n}\right\}$ 在正整数集上互为互补数列.

## 2. 贝蒂-瑞利定理

设 $\alpha, \beta$ 为正无理数, 且 $\frac{1}{\alpha}+\frac{1}{\beta}=1$, 则数列 $\left\{a_{n}\right\}$ 和 $\left\{b_{n}\right\}$ 为正整数集上的互补数列, 这里 $a_{n}=[\alpha n], b_{n}=[\beta n], n=1,2, \cdots$.

证明 由 $\alpha, \beta$ 为正无理数, 且 $\frac{1}{\alpha}+\frac{1}{\beta}=1 \Rightarrow \alpha, \beta>1$, 易知数列 $\left\{a_{n}\right\}$ 和 $\left\{b_{n}\right\}$ 为递增的正整数数列, 显然满足条件 (1).

若存在 $l \in \mathbb{N}_{+}$, 使得 $[\alpha i]=[\beta j]=l\left(i, j \in \mathbb{N}_{+}\right)$, 则有 $l \leq \alpha i<l+1, l \leq$ $\beta j<l+1$, 所以

$$
\frac{i}{l+1}<\frac{1}{\alpha} \leq \frac{i}{l}, \frac{j}{l+1}<\frac{1}{\beta} \leq \frac{j}{l}
$$

又 $\alpha, \beta$ 为正无理数, 故有

$$
\frac{i}{l+1}<\frac{1}{\alpha}<\frac{i}{l}, \frac{j}{l+1}<\frac{1}{\beta}<\frac{j}{l}
$$[^0]从而得到

$$
\frac{i+j}{l+1}<\frac{1}{\alpha}+\frac{1}{\beta}=1<\frac{i+j}{l} \Rightarrow l<i+j<l+1,
$$

但两个相邻的正整数 $l, l+1$ 之间不存在正整数, 矛盾. 所以数列 $\left\{a_{n}\right\}$ 和 $\left\{b_{n}\right\}$ 满足条件 (2).

若存在 $l \in \mathbb{N}_{+}$, 使得 $l \notin\left\{x_{1}, x_{2}, \cdots\right\} \bigcup\left\{y_{1}, y_{2}, \cdots\right\}$, 则存在 $i, j \in \mathbb{N}_{+}$, 使得 $[\alpha i] \leq l-1$, 且 $[\alpha(i+1)] \geq l+1,[\beta j] \leq l-1$, 且 $[\beta(j+1)] \geq l+1$, 类似上面的推理可得,

$$
\frac{i}{l}<\frac{1}{\alpha}<\frac{i+1}{l+1}, \frac{j}{l}<\frac{1}{\beta}<\frac{j+1}{l+1} .
$$

所以

$$
\frac{i+j}{l}<\frac{1}{\alpha}+\frac{1}{\beta}=1<\frac{i+j+2}{l+1} \Rightarrow i+j<l<l+1<i+j+2,
$$

这也是矛盾的. 所以数列 $\left\{a_{n}\right\}$ 和 $\left\{b_{n}\right\}$ 满足条件 (3).

综上, 定理得证.

## II. 问 题

在学兄的笔记本上我见到了如下问题:

问题 定义数列 $\left\{a_{n}\right\}$ 满足 $a_{1}=1, a_{n}$ 是满足 $n \mid a_{1}+a_{2}+\cdots+a_{n}$ 且 $a_{n} \neq a_{i}(i<n)$ 的最小正整数. 求证: $a_{a_{n}}=n$.

证法 1 考虑正整数数列 $1,2,3,4,5,6, \cdots$, 我们按如下方式操作:

1 固定不变, 第 1 次操作 2,3 交换位置(用 $\leftrightarrow$ 表示交换位置), 记为 $2 \leftrightarrow 3$,第 2 次操作 $4 \leftrightarrow 6, \cdots$, 第 $t$ 次操作 $k_{t} \leftrightarrow k_{t}+t$ ( $k_{t}$ 为前 $t-1$ 次操作后, 数列中没有参与过操作的最小数 (大于 1 )). 记操作后得到的新数列为 $\left\{b_{n}\right\}$, 显然每一项都是二阶不动点, 有 $b_{b_{n}}=n$.

记集合 $T=\left\{b_{1}, b_{2}, \cdots, b_{n}\right\}$ ，设集合 $T$ 与集合 $\bar{T}\left(\bar{T}=\mathbb{N}_{+} \backslash T\right)$ 之间恰进行了 $t(0 \leq t \leq n-1)$ 次上述的操作, 这些操作中比 $n$ 大的数交换到了前面(到集合 $T$ 内), 而不大于 $n$ 的数交换到了后面(到集合 $\bar{T}$ 内). 记集合 $T$ 中参与了这 $t$次操作的数分别为

$$
(n<) b_{n_{1}}<b_{n_{2}}<\cdots<b_{n_{t}}
$$

并设其中 $b_{n_{i}}$ 参与的是第 $c_{n_{i}}(1 \leq i \leq t)$ 次操作, 可知 $c_{n_{i}}(1 \leq i \leq t)$ 为连续的正整数且 $c_{n_{1}}<c_{n_{2}}<\cdots<c_{n_{t}}$ (这是因为, 若 $c_{n_{2}}<c_{n_{1}}$, 注意到第 $c_{n_{2}}$ 次操作为
$\left(b_{n_{2}}-c_{n_{2}}\right) \leftrightarrow b_{n_{2}}$. 但此时, 原数列中比 $\left(b_{n_{2}}-c_{n_{2}}\right)$ 小的数 $\left(b_{n_{1}}-c_{n_{1}}\right)$ 还没有被操作过 (它参与的是第 $c_{n_{1}}$ 次), 与操作要求相矛盾. 若 $c_{n_{2}}>c_{n_{1}}+1$, 设第 $c_{n_{1}}+1$ 次操作为 $x \leftrightarrow\left(x+c_{n_{1}}+1\right)$, 则类似可得,

$$
b_{n_{1}}-c_{n_{1}}<x<b_{n_{2}}-c_{n_{2}} \leq n
$$

因此

$$
x+c_{n_{1}}+1>b_{n_{1}}+1>n,
$$

这也属于集合 $T$ 与集合 $\bar{T}$ 之间的操作, 矛盾. 所以 $c_{n_{2}}=c_{n_{1}}+1$ 同理, $c_{n_{3}}=$ $c_{n_{2}}+1 \cdots$, 依此类推, 进一步有 $c_{n_{i}}(1 \leq i \leq t)$ 为依次连续的正整数).

下面首先证明: $n \mid b_{1}+b_{2}+\cdots+b_{n}$.

我们不妨证明一个更强的命题: $n \mid b_{1}+b_{2}+\cdots+b_{n}$ 且 $c_{n_{1}}+c_{n_{t}}=n$. (后式在 $t \geq 1$ 时才需考虑)

(1) 写出数列 $\left\{b_{n}\right\}$ 的前几项: $1,3,2,6,8,4, \cdots . n=1$ 时, 命题显然成立. $n=2$ 时, $2 \mid b_{1}+b_{2}, b_{2}(=3)$ 与集合 $\left\{b_{1}, b_{2}\right\}$ 外的数交换位置, 此时 $t=1, c_{n_{1}}=c_{n_{t}}=1, c_{n_{1}}+c_{n_{1}}=2$, 命题也成立.

(2) 假设命题对 $n(n \geq 2)$ 成立, 考虑 $n+1$ 时的情形. 下面按 $b_{n+1}$ 分类讨论.

(I) 若 $b_{n+1}$ 与 $b_{1}, b_{2}, \cdots, b_{n}$ 中某个数交换了位置, 则显然是 $b_{n+1} \leftrightarrow b_{n_{1}}$.此时, $b_{1}, b_{2}, \cdots, b_{n}, b_{n+1}$ 与 $b_{n+2}, b_{n+3}, \cdots$ 之间的数恰进行了 $t-1$ 次上述的操作(考虑到 $b_{n+1} \leftrightarrow b_{n_{1}}$, 这里 $\left.t>0\right)$. 我们重新分别记 $c_{n_{i}}^{\prime}=c_{n_{i+1}}(1 \leq$ $\left.i \leq t^{\prime}, t^{\prime}=t-1\right)$, 由 $c_{n_{i}}(1 \leq i \leq t)$ 为依次连续的正整数及归纳假设, 可知, $c_{n_{1}}^{\prime}+c_{n_{t^{\prime}}}^{\prime}=c_{n_{2}}+c_{n_{t}}=c_{n_{1}}+1+c_{n_{t}}=n+1$. (若 $t=1, c_{n_{2}}, \cdots, c_{n_{t}}$ 都不存在,均视为 0, 也不影响后续计算和推理).

又考虑到 $b_{2}, \cdots, b_{n}, b_{n+1}$ 内部之间互换位置的数必为偶数个, 所以 $n \equiv t-1(\bmod 2)$.

从而

$$
\begin{aligned}
\sum_{i=1}^{n+1} b_{i} & =1+2+\cdots+(n+1)+\left(c_{n_{2}}+\cdots+c_{n_{t}}\right) \\
& =\frac{n+t+1}{2} \cdot(n+1) \\
& \equiv 0 \quad(\bmod n)+1 .
\end{aligned}
$$

(II) 若 $b_{n+1}$ 与其后某个数交换了位置, 重新分别记

$$
c_{n_{i}}^{\prime}=c_{n_{i}}(1 \leq i \leq t), c_{n_{t^{\prime}}}^{\prime}=c_{n_{t}}+1\left(t^{\prime}=t+1\right),
$$

由 $c_{n_{i}}(1 \leq i \leq t)$ 为依次连续的正整数及归纳假设, 可知, $c_{n_{1}}^{\prime}+c_{n_{t^{\prime}}}^{\prime}=c_{n_{1}}+c_{n_{t}}+$
$1=n+1$ (特别地, 若 $t=0, b_{2}, \cdots, b_{n}$ 都在内部之间互换位置, 共进行了 $\frac{n-1}{2}$次操作, 从而 $b_{n+1}$ 参与的是第 $\frac{n+1}{2}$ 次操作, 故 $c_{n_{1}}^{\prime}=c_{n_{t^{\prime}}}^{\prime}=\frac{n+1}{2}$, 仍然满足).

类似 (I) 可得 $2 \mid n+t+1$,

$$
\sum_{i=1}^{n+1} b_{i}=\left(1+\frac{n+t+1}{2}\right)(n+1) \equiv 0 \quad(\bmod n)+1
$$

故 $n+1$ 时命题成立.

由归纳原理. 对任意正整数 $n$, 命题成立.

再证明:数列 $\left\{b_{n}\right\}$ 即为数列 $\left\{a_{n}\right\}$.

(1) $n=1,2,3$ 时, 逐一验证即可.

(2) 假设命题对 $n \leq l-1(l \geq 4)$ 均成立, 考虑 $n=l$ 时的情形.

由 $(*)$ 式知 $l \mid b_{1}+b_{2}+\cdots+b_{l}$, 由归纳假设可得 $l \mid a_{1}+\cdots+a_{l-1}+b_{l}$, 结合

$$
l\left|a_{1}+\cdots+a_{l-1}+a_{l} \Rightarrow l\right| a_{l}-b_{l} .
$$

若 $b_{l} \leq l$, 由 $a_{l}$ 的最小性知必有 $b_{l}=a_{l}$.

下设 $b_{l}=m>l$, 则 $l \leftrightarrow m$. 而 $b_{2}, \cdots, b_{l-1}$ 至多参与 $l-2$ 次操作, 由数列 $\left\{b_{n}\right\}$ 定义知,

$$
b_{l} \leq l+(l-1) \Rightarrow m<2 l \text {. }
$$

假设 $a_{l} \neq m$, 结合 (1), (2) $a_{l}$ 的最小性知必有 $a_{l}=m-l$. 这是矛盾的. 事实上, 我们只需证明 $b_{2}, \cdots, b_{l-1}$ (即 $a_{2}, \cdots, a_{l-1}$ ) 中某个数的值为 $m-l$.

设 $(m-l) \leftrightarrow(m-l+w)$, 则 $b_{m-l+w}=m-l$, 假设 $b_{m-l+w} \notin\left\{b_{2}, \cdots, b_{l-1}, b_{l}\right\}$,则

$$
m-l+w>l \text {. }
$$

记集合 $M=\{2,3, \cdots, m-l+w\}$. 注意到 $(m-l) \leftrightarrow(m-l+w)$ 为第 $w$次操作, 故前 $w$ 次操作中, 集合 $M$ 内参与操作的数为 $2 w$ 个 (由操作规则, 这些操作均在集合 $M$ 内部两数之间进行).

设第 $x(w+1 \leq x \leq m-l)$ 次操作为 $A \leftrightarrow B(A<B)$, 由 (3)得, $l \in M$, 且注意到 $l \leftrightarrow m$ 为第 $m-l$ 次操作, 由操作规则, 有

$$
m-l<A \leq l<m-l+w<A+w<B
$$

即 $A \in M$, 且 $B \notin M$. 这表明, 从第 $w+1$ 次操作开始, 到第 $(m-l)$ 次操作结束,集合 $M$ 中有 $m-l-w$ 个数参与操作(每次操作集合 $M$ 中恰有 1 个数参与).

综上, 集合 $M$ 中参与上述操作的数共计

$$
2 w+m-l-w=m-l+w(>|M|)
$$

个, 这不符合操作规则, 矛盾. 所以假设不成立, $a_{l}=m=b_{l}$.

由归纳原理, 对任意 $n \in \mathbb{N}_{+}, a_{n}=b_{n}$.

故 $a_{a_{n}}=n$. 证毕.

## III. 思 考

以上是我最初的证法. 在求解过程中, 注意到数列 $\left\{a_{n}\right\}$ 具有一些美好的性质, 便进行了一些探究. 不妨先观察数列 $\left\{a_{n}\right\}$ 前几项:

$$
1,3,2,6,8,4,11,5,14,16,7,19,21,9,24,10 \cdots \text {. }
$$

我们将 3 与 2 交换位置(记为 $3 \leftrightarrow 2$ ), $6 \leftrightarrow 4,8 \leftrightarrow 5,11 \leftrightarrow 7,14 \leftrightarrow 9,16 \leftrightarrow$ $10, \cdots$ 得到数列:

$$
1,2,3,4,5,6,7, \cdots
$$

这个数列显然代数上更容易刻画. 又注意到,

$$
3-2=1,6-4=2,8-5=3,11-7=4,14-9=5,16-10=6, \cdots
$$

这种交换呈现出一定的规律, 我们把每次交换过程中的较小数与较大数分开写成两个数列.

$$
\begin{aligned}
& \left\{x_{n}\right\}: 2,4,5,7,9,10,12,13,15, \cdots \\
& \left\{y_{n}\right\}: 3,6,8,11,14,16,19,21,24, \cdots
\end{aligned}
$$

(事实上, 也可以认为 1 与自身对换)

再将两个数列中每一项都减去 1 , 得到

$$
\begin{aligned}
& \left\{x_{n}^{\prime}\right\}: 1,3,4,6,8,9,11,12,14, \cdots \\
& \left\{y_{n}^{\prime}\right\}: 2,5,7,10,13,15,18,20,23, \cdots
\end{aligned}
$$

满足对任意正整数 $n$, 均有 $y_{n}^{\prime}-x_{n}^{\prime}=n$. 发现 $\left\{x_{n}^{\prime}\right\}$ 与 $\left\{y_{n}^{\prime}\right\}$ 为正整数集上的互补数列, 自然猜想其与贝蒂-瑞利定理有关联.

设 $y_{n}^{\prime}=[\beta n], x_{n}^{\prime}=[\alpha n], y_{n}^{\prime}-x_{n}^{\prime}=n$, 则 $\beta-\alpha=1$, 联立 $\frac{1}{\alpha}+\frac{1}{\beta}=1$ 解得,

$$
\alpha=\frac{1+\sqrt{5}}{2}, \beta=\frac{3+\sqrt{5}}{2} \text {. }
$$

进一步猜测:

$$
\left[\frac{1+\sqrt{5}}{2} n\right]+1 \leftrightarrow\left[\frac{3+\sqrt{5}}{2} n\right]+1(n \in \mathbb{N})
$$

得到数列 $\left\{a_{n}\right\}$ (可以定义 1 与本身交换).
藉此, 我们得到下面的证明.

证法 2 考虑正整数数列 $1,2,3,4,5,6, \cdots$, 我们按如下方式操作:

1 固定不变, 第 $n(n \geq 1)$ 次操作 $\left\lceil\frac{1+\sqrt{5}}{2} n\right\rceil,\left\lceil\frac{3+\sqrt{5}}{2} n\right\rceil$ 交换位置(用 $\leftrightarrow$ 表示交换位置), 记为

$$
\left\lceil\frac{1+\sqrt{5}}{2} n\right\rceil \leftrightarrow\left\lceil\frac{3+\sqrt{5}}{2} n\right\rceil .
$$

设操作后得到的新数列为 $\left\{b_{n}\right\}$.

由贝蒂-瑞利定理知, 1 以外的每个正整数都参与了唯一一次操作, 有 $b_{b_{n}}=n$.

记 $M=\left\{b_{1}, b_{2}, \cdots, b_{n}\right\}$, 若 $b_{l} \in M, b_{l}$ 与集合 $M$ 外的数交换位置. 则有:

$$
l=\left\lceil\frac{1+\sqrt{5}}{2} k\right\rceil \leq n, b_{l}=\left\lceil\frac{3+\sqrt{5}}{2} k\right\rceil \geq n+1 .
$$

因此

$$
\left\lceil\frac{3-\sqrt{5}}{2} n\right\rceil \leq k \leq\left[\frac{\sqrt{5}-1}{2} n\right] .
$$

故

$$
\begin{aligned}
\sum_{i=1}^{n} b_{i} & =\sum_{i=1}^{n} i+\sum_{k=\left\lceil\frac{3-\sqrt{5}}{2} n\right\rceil}^{\left[\frac{\sqrt{5}-1}{2} n\right]} \\
& =\frac{n(n+1)}{2}+\frac{\left(\left\lceil\frac{3-\sqrt{5}}{2} n\right\rceil+\left[\frac{\sqrt{5}-1}{2} n\right]\right)\left(\left[\frac{\sqrt{5}-1}{2} n\right]-\left\lceil\frac{3-\sqrt{5}}{2} n\right\rceil+1\right)}{2} \\
& =\frac{n(n+1)}{2}+\frac{n\left(2\left[\frac{\sqrt{5}-1}{2} n\right]-n+1\right)}{2} \\
& =n\left(\left[\frac{\sqrt{5}-1}{2} n\right]+1\right) \\
& \equiv 0 \quad(\bmod n)
\end{aligned}
$$

再证明: 数列 $\left\{b_{n}\right\}$ 即为数列 $\left\{a_{n}\right\}$.

(1) $n=1,2,3$ 时, 逐一验证可证.

(2) 假设不大于 $n-1(n \geq 4)$ 时, 命题成立, 考虑 $n$ 时的情形.

若 $n=\left[\frac{3+\sqrt{5}}{2} l\right]+1, l \in \mathbb{N}_{+}$, 可得

$$
b_{n}=\left[\frac{1+\sqrt{5}}{2} l\right]+1<n
$$

由操作规则及归纳假设, 此时 $b_{n}$ 满足最小性, 所以 $a_{n}=b_{n}$.
若 $n=\left[\frac{1+\sqrt{5}}{2} l\right]+1, l \in \mathbb{N}_{+}, l \geq 2$, 有

假设 $a_{n} \neq b_{n}$, 则必有

$$
b_{n}=\left[\frac{3+\sqrt{5}}{2} l\right]+1
$$

$$
a_{n}=\left[\frac{3+\sqrt{5}}{2} l\right]+1-\left[\frac{1+\sqrt{5}}{2} l\right]-1=l .
$$

下面我们证明这是不可能的.

当 $l=\left[\frac{1+\sqrt{5}}{2} m\right]+1, m \in \mathbb{N}_{+}$, 可得 $m \leq \frac{\sqrt{5}-1}{2} l$, 因此

$$
\frac{3+\sqrt{5}}{2} m \leq \frac{1+\sqrt{5}}{2} l \Rightarrow\left[\frac{3+\sqrt{5}}{2} m\right] \leq\left[\frac{1+\sqrt{5}}{2} l\right]
$$

由贝蒂-瑞利定理, 等号不成立. 进一步, 有

$$
1+\left[\frac{3+\sqrt{5}}{2} m\right] \leq\left[\frac{1+\sqrt{5}}{2} l\right]<n
$$

故

$$
a_{\left[\frac{3+\sqrt{5}}{2} m\right]+1}=b_{\left[\frac{3+\sqrt{5}}{2} m\right]+1}=l .
$$

矛盾.

当 $l=\left[\frac{3+\sqrt{5}}{2} m\right]+1, m \in \mathbb{N}_{+}$, 可得

$$
b_{\left[\frac{1+\sqrt{5}}{2} m\right]+1}=\left[\frac{3+\sqrt{5}}{2} m\right]+1,
$$

且 $\left[\frac{1+\sqrt{5}}{2} m\right]+1<l<n$. 此时

$$
a_{\left[\frac{1+\sqrt{5}}{2} m\right]+1}=b_{\left[\frac{1+\sqrt{5}}{2} m\right]+1}=l .
$$

矛盾。

从而假设不成立, 即 $a_{n}=b_{n}$.

由归纳原理, 对任意 $n \in \mathbb{N}_{+}$, 命题成立.

故 $a_{a_{n}}=n$. 证毕.

## IV. 小 结

至此, 对于数列 $\left\{a_{n}\right\}: 1,3,2,6,8,4,11,5,14,16,7,19,21,9,24,10 \cdots$.我们可以得到其有如下性质:

(1) 通项公式: $a_{n}=n\left\lceil\frac{2 n}{\sqrt{5}+1}\right\rceil-(n-1)\left\lceil\frac{2(n-1)}{\sqrt{5}+1}\right\rceil$;

(2) 前 $n$ 项的和: $\sum_{i=1}^{n} a_{i}=\left\lceil\frac{2 n}{\sqrt{5}+1}\right\rceil n$;

(3) $a_{\left[\frac{1+\sqrt{5}}{2} n\right]+1}=\left[\frac{3+\sqrt{5}}{2} n\right]+1, a_{\left[\frac{3+\sqrt{5}}{2} n\right]+1}=\left[\frac{1+\sqrt{5}}{2} n\right]+1(n \in \mathbb{N})$;

(4) 二阶不动点的性质: $a_{a_{n}}=n$;

(5) 数论性质: $a_{1}=1, a_{n}$ 是满足 $n \mid a_{1}+a_{2}+\cdots+a_{n}$ 且 $a_{n} \neq a_{i}(i<n)$ 的最小正整数;

(6) 设 $x_{n}^{\prime}=\left[\frac{1+\sqrt{5}}{2} n\right], y_{n}^{\prime}=\left[\frac{3+\sqrt{5}}{2} n\right]$, 则数列 $\left\{x_{n}^{\prime}\right\},\left\{y_{n}^{\prime}\right\}\left(n \in \mathbb{N}_{+}\right)$为正整数集上的互补数列.

## V. 展望与联想

我们已经发现了数列 $\left\{a_{n}\right\}$ 的一些代数和数论的性质. 比较有趣的是, 这个数列还具备很有意思的组合背景. 历届的 IMO 试题中也不乏该数列的身影. 下面几个问题均与之相关.

问题 1 (Wythoff 游戏) 甲、乙两人轮流从两堆棋子中取棋子. 满足下列要求:或者从一堆中取若干枚(至少一枚)棋子, 或者从两堆中取出同样数目(至少一枚)棋子. 将两堆取完并取到最后一枚棋子者获胜.

问:在什么情况下,甲(先取者)有必胜策略?

问题 2(20 届 IMO T3) 全体正整数集合可以分成两个互不相交的正整数子集

$$
\{f(1), f(2), \cdots, f(n), \cdots\},\{g(1), g(2), \cdots, g(n), \cdots\} .
$$

其中

$$
f(1)<f(2)<\cdots<f(n)<\cdots, g(1)<g(2)<\cdots<g(n) \cdots,
$$

且有 $g(n)=f(f(n))+1, n \geq 1$. 求 $f(240)$.

问题 2 (34 届 IMO T5) 设 $\mathbb{N}_{+}$是全体正整数集合, 是否存在一个定义在集合 $\mathbb{N}_{+}$上的函数 $f(n)$, 具有如下性质:

(1) 对于一切 $n \in \mathbb{N}_{+}, f(n) \in \mathbb{N}_{+}$;

(2) 对于一切 $n \in \mathbb{N}_{+}, f(n)<f(n+1)$;

(3) $f(1)=2$;

(4) 对于一切 $n \in \mathbb{N}_{+}, f(f(n))=f(n)+n$.

事实上, 问题 1 的解是两堆棋子数目为所有的非 $\left(x^{\prime}{ }_{n}, y^{\prime}{ }_{n}\right)$ (无序对), 即两堆
棋子的数目不能表示为 $\left(\left[\frac{1+\sqrt{5}}{2} n\right],\left[\frac{3+\sqrt{5}}{2} n\right]\right)$ 的时候甲有必胜策略. 读者可以尝试证明或者参阅文 $[1]$.

问题 2 中的 $f(n)=x_{n}^{\prime}=\left[\frac{1+\sqrt{5}}{2} n\right], g(n)=y_{n}^{\prime}=\left[\frac{3+\sqrt{5}}{2} n\right]$. 这里还可以发现数列的另一个性质, $y_{n}^{\prime}=x_{x_{n}^{\prime}}^{\prime}+1$. 问题 2 和问题 3 的解答均可以参阅文 [2].

另外, 注意到特征数字 $\frac{1+\sqrt{5}}{2}$, 也容易联想到该数列与斐波那契数列可能具有一定的关系, 这里就不再展开讨论了.

## 参考文献

[1] 张圭, 沈文选, 冷岗松. 奥林匹克数学中的组合问题 $[\mathrm{M}]$ 湖南师范大学出版社. 2015.1

[2] 刘培杰. 历届IMO试题集 [M]. 哈尔滨工业大学出版社. 2006. 5.


[^0]:    修订日期: 2020-05-09.

