# 几道集训队测试题的解与评析 

孔繁浩

(东北育才学校, 110179)

第 58 届 IMO 中国国家集训活动已于 2017 年 3 月 4 日至 28 日在复旦大学附属中学举行. 我有幸作为一名集训队员参加了全部集训过程. 本文就其中三个测试题进行讨论, 介绍自己的解法与体会, 以求抛砖引玉. 下面是本次集训活动中的部分试题以及笔者的解法和体会.

例 1 (集训队测试第 2 题). 求证对任意大于 1 的实数 $x$ 和正整数 $n$, 都有

$$
\sum_{k=1}^{n} \frac{\{k x\}}{[k x]}<\sum_{k=1}^{n} \frac{1}{2 k-1}
$$

评析 本题的标准答案采用了整体化处理的思想, 使用 Abel 求和公式进行变换以达到最终目的. 以下展示的解法则更偏重局部处理, 运用局部两两配对的思想, 最终获得证明. 本解法并不比标准答案的解法为简洁, 但其想法似更为纯朴, 或许能从另一个方向揭示试题的本质.

证明 由于

$$
\begin{aligned}
\sum_{k=1}^{n}\left(\frac{1}{2 k-1}-\frac{\{k x\}}{[k x]}\right) & =\sum_{k=1}^{n} \frac{[k x]-(2 k-1)(k x-[k x])}{(2 k-1)[k x]} \\
& =\sum_{k=1}^{n} \frac{2 k[k x]-(2 k-1) k x}{(2 k-1)[k x]} \\
& =\sum_{k=1}^{n} \frac{k(2[k x]-2 k x+x)}{(2 k-1)[k x]} \\
& =\sum_{k=1}^{n} \frac{k}{2 k-1} \frac{x-2\{k x\}}{[k x]},
\end{aligned}
$$

设 $a_{k}=\frac{k}{2 k-1} \frac{x-2\{k x\}}{[k x]}$, 则只需证明 $\sum_{k=1}^{n} a_{k}>0$.

若对任意 $1 \leq k \leq n$ 都有 $a_{k}>0$, 则显然 $\sum_{k=1}^{n} a_{k}>0$.

收稿日期: 2017-07-03; 修订日期: 2017-07-29.
现假设存在 $1 \leq k_{0} \leq n$ 使 $a_{k_{0}} \leq 0$, 则必有

$$
x-2\left\{k_{0} x\right\} \leq 0, \quad x \leq 2\left\{k_{0} x\right\}<2 .
$$

故 $1<x<2$.

这时可以取一个最小的整数 $0 \leq r_{1}<n$ 使 $a_{r_{1}+1} \leq 0$, 还可以取一个最大的整数 $r_{1} \leq s_{1} \leq n$, 使得对任意 $r_{1}<k \leq s_{1}$ 都有 $a_{k} \leq 0$. 若这时还存在 $s_{1}<k \leq n$ 使 $a_{k} \leq 0$, 那么可以取一个最小的整数 $s_{1} \leq r_{2}<n$ 使 $a_{r_{2}+1} \leq 0$, 还可以取一个最大的整数 $r_{2} \leq s_{2} \leq n$, 使得对任意 $r_{2}<k \leq s_{2}$ 都有 $a_{k} \leq 0$. 如此做下去, 直到取出 $r_{l}, s_{l}\left(l \in \mathbb{N}^{*}\right)$ 后, $s_{l}=n$ 或对任意 $s_{l}<k \leq n$ 都有 $a_{k}>0$.

这时由 $s_{m}(1 \leq m \leq l)$ 的最大性, 得对任意 $0<m<l$ 都有 $r_{m+1}>s_{m}$. 另一方面, 由于

$$
x-2\{x\}=x-2(x-1)=2-x>0 \text {, }
$$

故 $a_{1}>0$, 从而 $r_{1}>0$.

若令 $s_{0}=0$, 则 $r_{m+1}>s_{m}$ 对 $m=0$ 亦成立. 进一步地可知 $a_{k} \leq 0$ 当且仅当存在 $1 \leq m \leq l$ 使 $r_{m}<k \leq s_{m}$.

下证对任意 $1 \leq m \leq l$, 都有

$$
\sum_{k=s_{m-1}+1}^{s_{m}} a_{k}>0
$$

由于 $1<x<2$, 故对任意 $1 \leq k \leq n$, 有

$$
\{(k-1) x\}=\{k x\}+1-x \text { 或 }\{k x\}+2-x \text {. }
$$

而对 $r_{m}<k \leq s_{m}$, 都有 $x-2\{k x\} \leq 0$, 即 $\{k x\} \geq \frac{x}{2}$.

若 $\{(k-1) x\}=\{k x\}+2-x$, 则

$$
\begin{aligned}
\{(k-1) x\} & \geq \frac{x}{2}+2-x \\
& =2-\frac{x}{2}>2-1 \\
& =1, \text { 矛盾! }
\end{aligned}
$$

故必有 $\{(k-1) x\}=\{k x\}+1-x$, 因此 $[(k-1) x]=[k x]-1$.

这样若设 $\left[r_{m} x\right]=p,\left\{r_{m} x\right\}=\frac{x}{2}-\varepsilon$, 则

$$
r_{m} x=p+\frac{x}{2}-\varepsilon
$$

且对任意 $0<t \leq s_{m}-r_{m}$, 都有

$$
\left[\left(r_{m}+t\right) x\right]=p+t, \quad\left\{\left(r_{m}+t\right) x\right\}=\frac{x}{2}-\varepsilon+t(x-1),
$$

且 $0<\varepsilon \leq x-1$.
进一步地, 令 $t=s_{m}-r_{m}$, 则

$1>\left\{s_{m} x\right\}=\frac{x}{2}-\varepsilon+\left(s_{m}-r_{m}\right)(x-1),\left(s_{m}-r_{m}\right)(x-1)<1+\varepsilon-\frac{x}{2}$.

下分情况讨论.

(1). $0<\varepsilon \leq \frac{1}{2}(x-1)$. 这时对任意 $0 \leq t \leq s_{m}-r_{m}$,

$$
\left(r_{m}-t\right) x=p+\frac{x}{2}-\varepsilon-t x=(p-t)+\left(\frac{x}{2}-\varepsilon-t(x-1)\right) .
$$

另一方面，

$$
\begin{aligned}
\frac{x}{2}-\varepsilon-t(x-1) & \geq \frac{x}{2}-\varepsilon-\left(r_{m}-s_{m}\right)(x-1) \\
& >\frac{x}{2}-\varepsilon-\left(1+\varepsilon-\frac{x}{2}\right) \\
& =x-1-2 \varepsilon \\
& \geq 0 .
\end{aligned}
$$

且 $\frac{x}{2}-\varepsilon-t(x-1)<\frac{x}{2}<1$. 故有

$$
\left[\left(r_{m}-t\right) x\right]=p-t, \quad\left\{\left(r_{m}-t\right) x\right\}=\frac{x}{2}-\varepsilon-t(x-1),
$$

且 $x-2\left\{\left(r_{m}-t\right) x\right\}>0$, 故 $a_{r_{m}-t}>0$, 进而我们有 $s_{m-1} \leq 2 r_{m}-s_{m}-1$. 因此

$$
\begin{aligned}
\sum_{k=s_{m-1}+1}^{s_{m}} a_{k} & \geq \sum_{k=2 r_{m}-s_{m}}^{r_{m}-1} a_{k}+\sum_{k=r_{m}+1}^{s_{m}} a_{k}=\sum_{t=1}^{s_{m}-r_{m}}\left(a_{r_{m}-t}+a_{r_{m}+t}\right) \\
& =\sum_{t=1}^{s_{m}-r_{m}}\left(\frac{r_{m}-t}{2\left(r_{m}-t\right)-1} \frac{x-2\left(\frac{x}{2}-\varepsilon-t(x-1)\right)}{p-t}+\frac{r_{m}+t}{2\left(r_{m}+t\right)-1} \frac{x-2\left(\frac{x}{2}-\varepsilon+t(x-1)\right)}{p+t}\right) \\
& =\sum_{t=1}^{s_{m}-r_{m}}\left(\frac{r_{m}-t}{2\left(r_{m}-t\right)-1} \frac{2(t(x-1)+\varepsilon)}{p-t}-\frac{r_{m}+t}{2\left(r_{m}+t\right)-1} \frac{2(t(x-1)-\varepsilon)}{p+t}\right) .
\end{aligned}
$$

由于

$$
\begin{aligned}
\frac{r_{m}-t}{2\left(r_{m}-t\right)-1} & >\frac{r_{m}+t}{2\left(r_{m}+t\right)-1}>0, \\
\frac{1}{p-t} & >\frac{1}{p+t}>0 \\
t(x-1)+\varepsilon & >t(x-1)-\varepsilon>0,
\end{aligned}
$$

故有

$$
\frac{r_{m}-t}{2\left(r_{m}-t\right)-1} \frac{2(t(x-1)+\varepsilon)}{p-t}-\frac{r_{m}+t}{2\left(r_{m}+t\right)-1} \frac{2(t(x-1)-\varepsilon)}{p+t}>0
$$

进而 $\sum_{k=s_{m-1}+1}^{s_{m}} a_{k}>0$, 即 $(*)$ 式成立.

(2). $\frac{1}{2}(x-1)<\varepsilon \leq x-1$. 这时对任意 $0 \leq t \leq s_{m}-r_{m}-1$,

$$
\left(r_{m}-t\right) x=p+\frac{x}{2}-\varepsilon-t x=(p-t)+\left(\frac{x}{2}-\varepsilon-t(x-1)\right) .
$$

另一方面

$$
\begin{aligned}
\frac{x}{2}-\varepsilon-t(x-1) & \geq \frac{x}{2}-\varepsilon-\left(r_{m}-s_{m}-1\right)(x-1) \\
& >\frac{x}{2}-\varepsilon-\left(1+\varepsilon-\frac{x}{2}\right)+x-1 \\
& =2(x-1)-2 \varepsilon \geq 0
\end{aligned}
$$

且 $\frac{x}{2}-\varepsilon-t(x-1)<\frac{x}{2}<1$. 故有

$$
\left[\left(r_{m}-t\right) x\right]=p-t,\left\{\left(r_{m}-t\right) x\right\}=\frac{x}{2}-\varepsilon-t(x-1),
$$

且 $x-2\left\{\left(r_{m}-t\right) x\right\}>0$, 故 $a_{r_{m}-t}>0$. 进而我们有 $s_{m-1} \leq 2 r_{m}-s_{m}$. 因此

$$
\begin{aligned}
\sum_{k=s_{m-1}+1}^{s_{m}} a_{k} & \geq \sum_{k=2 r_{m}-s_{m}+1}^{r_{m}} a_{k}+\sum_{k=r_{m}+1}^{s_{m}} a_{k}=\sum_{t=1}^{s_{m}-r_{m}}\left(a_{r_{m}-t+1}+a_{r_{m}+t}\right) \\
& =\sum_{t=1}^{s_{m}-r_{m}}\left(\frac{r_{m}-t+1}{2\left(r_{m}-t+1\right)-1} \frac{x-2\left(\frac{x}{2}-\varepsilon-(t-1)(x-1)\right)}{p-t+1}+\frac{r_{m}+t}{2\left(r_{m}+t\right)-1} \frac{x-2\left(\frac{x}{2}-\varepsilon+t(x-1)\right)}{p+t}\right) \\
& =\sum_{t=1}^{s_{m}-r_{m}}\left(\frac{r_{m}-t+1}{2\left(r_{m}-t+1\right)-1} \frac{2((t-1)(x-1)+\varepsilon)}{p-t+1}-\frac{r_{m}+t}{2\left(r_{m}+t\right)-1} \frac{2(t(x-1)-\varepsilon)}{p+t}\right) .
\end{aligned}
$$

由于

$$
\begin{gathered}
\frac{r_{m}-t+1}{2\left(r_{m}-t+1\right)-1}>\frac{r_{m}+t}{2\left(r_{m}+t\right)-1}>0, \frac{1}{p-t}>\frac{1}{p+t}>0 \\
(t-1)(x-1)+\varepsilon>t(x-1)+\frac{1}{2}(x-1)-(x-1)>t(x-1)-\varepsilon>0
\end{gathered}
$$

故有

$$
\frac{r_{m}-t+1}{2\left(r_{m}-t+1\right)-1} \frac{2((t-1)(x-1)+\varepsilon)}{p-t+1}-\frac{r_{m}+t}{2\left(r_{m}+t\right)-1} \frac{2(t(x-1)-\varepsilon)}{p+t}>0
$$

进而 $\sum_{k=s_{m-1}+1}^{s_{m}} a_{k}>0$. 即 $(*)$ 式成立.

从而 $(*)$ 式恒成立, 故

$$
\sum_{k=1}^{n} a_{k} \geq \sum_{m=1}^{l} \sum_{k=s_{m-1}+1}^{s_{m}} a_{k}>0
$$

即原式成立.

例 2 (集训队测试第 12 题). 数集 $M \subseteq \mathbb{R}$, 且满足如下性质:

1. 对任意 $x \in M, n \in \mathbb{N}$ 有 $x+n \in M$;
2. 对任意 $x \in M$ 有 $-x \in M$;
3. $M$ 和 $\mathbb{R} \backslash M$ 中各包含一段长度不为 0 的区间.

对任意 $x \in \mathbb{R}$, 记 $M(x)=\left\{n \in \mathbb{N}^{*} \mid n x \in M\right\}$. 若无理数 $a, b$ 满足

$$
M(a)=M(b),
$$

求证 $a+b, a-b$ 中至少有一个是有理数.

评析 本题是一道很有趣却不失难度的一道题目, 并掺杂了一些高等代数里线性无关的思想. 我们先看一下这道题目笔者的解答.

证明 由条件可知, 对任意 $n \in \mathbb{Z}, x \in \mathbb{R}$ 有 $M(x)=M(x+n)=M(-x)$.故可不妨设 $0 \leq a, b<1$. 进一步地有 $M(x)=M(\{x\})$, 且若 $M(x)=M(y)$,则对任意 $n \in \mathbb{N}^{*}$ 都有 $M(n x)=M(n y)$.

先证明两个引理:

引理 1. 对任意无理数 $\alpha_{1}, \cdots, \alpha_{t}$ 和 $\varepsilon>0$, 都存在 $n \in \mathbb{N}^{*}$ 使得对任意 $1 \leq i \leq t$ 都有 $\left\{n \alpha_{i}\right\} \in(0, \varepsilon) \cup(1-\varepsilon, 1)$.

证明 取 $k=\left[\frac{1}{\varepsilon}\right]+1$, 则 $\frac{1}{k}<\varepsilon$. 将集合 $[0,1) \times \cdots \times[0,1)$ 分为 $k_{t}$ 个不相交的集合 $\left[\frac{k_{1}}{k}, \frac{k_{1}+1}{k}\right) \times \cdots \times\left[\frac{k_{t}}{k}, \frac{k_{t}+1}{k}\right)\left(k_{1}, \cdots, k_{t} \in\{0,1, \cdots, k-1\}\right)$ ，由抽屉原理，存在 $1 \leq n_{1}<n_{2} \leq k^{t}+1$ 使 $\left(\left\{n_{1} \alpha_{1}\right\}, \cdots,\left\{n_{1} \alpha_{t}\right\}\right)$ 和 $\left(\left\{n_{2} \alpha_{1}\right\}, \cdots,\left\{n_{2} \alpha_{t}\right\}\right)$ 在同一个小集合中, 取 $n=n_{2}-n_{1}$ 即满足条件. 引理证毕.

引理 2. 对任意无理数 $\alpha$ 和 $\varepsilon>0,0<r<1$ 都存在 $n \in \mathbb{N}^{*}$ 使得 $|r-\{n \alpha\}|<\varepsilon$.

证明 不妨设 $\varepsilon \leq \min \{r, 1-r\}$. 由引理 1 知存在 $n_{1} \in \mathbb{N}^{*}$ 使得

$$
\left\{n_{1} \alpha\right\} \in(0, \varepsilon) \cup(1-\varepsilon, 1) \text {. }
$$

若 $\left\{n_{1} \alpha\right\} \in(0, \varepsilon)$, 设 $\left[n_{1} \alpha\right]=k,\left\{n_{1} \alpha\right\}=\delta$, 则存在 $n_{2} \in \mathbb{N}^{*}$ 使得 $n_{2} \delta \leq r<$ $\left(n_{2}+1\right) \delta$. 取 $n=n_{1} n_{2}$, 则 $n \alpha=n_{2} k+n_{2} \delta$, 又 $n_{2} k \in \mathbb{Z}, 0<n_{2} \delta \leq r<1$, 故 $\{n \alpha\}=n_{2} \delta$. 又 $0 \leq r-n_{2} \delta<\delta<\varepsilon$, 故 $|r-\{n \alpha\}|<\varepsilon$ 满足条件.

若 $\left\{n_{1} \alpha\right\} \in(1-\varepsilon, 1)$, 设 $\left[n_{1} \alpha\right]=k-1,\left\{n_{1} \alpha\right\}=1-\delta$, 则存在 $n_{2} \in \mathbb{N}^{*}$ 使得 $n_{2} \delta \leq 1-r<\left(n_{2}+1\right) \delta$. 取 $n=n_{1} n_{2}$, 则

$$
n \alpha=n_{2} k-n_{2} \delta=\left(n_{2} k-1\right)+\left(1-n_{2} \delta\right),
$$

又 $n_{2} k-1 \in \mathbb{Z}, 0<1-r \leq 1-n_{2} \delta<1$, 故 $\{n \alpha\}=1-n_{2} \delta$. 又 $0 \geq r-\left(1-n_{2} \delta\right)>$ $-\delta>-\varepsilon$, 故 $|r-\{n \alpha\}|<\varepsilon$, 满足条件. 引理得证.

推论 对任意无理数 $\alpha$ 和 $0 \leq r<s \leq 1$ 都存在 $n \in \mathbb{N}^{*}$ 使得 $\{n \alpha\} \in(r, s)$.

回到原题. 由性质 1 和 2 , 不妨设 $0<A<B<1$ 满足 $(A, B) \subset M, 0<$ $C<D<1,(C, D) \subset \mathbb{R} \backslash M$, 令

$$
\varepsilon=\frac{\min \{B-A, D-C\}}{2}
$$

由引理 1 , 存在 $n_{0} \in \mathbb{N}^{*}$ 使

$$
\left\{n_{0} a\right\},\left\{n_{0} b\right\} \in\left(0, \frac{\varepsilon}{10}\right) \cup\left(1-\frac{\varepsilon}{10}, 1\right) .
$$

若 $\left\{n_{0} a\right\} \in\left(1-\frac{\varepsilon}{10}, 1\right)$, 那么令 $a^{\prime}=1-a$, 则

$$
\left\{n_{0} a^{\prime}\right\} \in\left(0, \frac{\varepsilon}{10}\right)
$$

而 $M\left(a^{\prime}\right)=M(a)=M(b)$, 且 $a^{\prime}+b, a^{\prime}-b$ 中至少有一个是有理数当且仅当 $a+b, a-b$ 中至少有一个是有理数. 故可不妨设 $\left\{n_{0} a\right\},\left\{n_{0} b\right\} \in\left(0, \frac{\varepsilon}{10}\right)$. 这时分三种情况:

(1) $\frac{\left\{n_{0} a\right\}}{\left\{n_{0} b\right\}}=1$. 则存在 $u, v \in \mathbb{N}^{*}$ 使得

$$
n_{0} a-u=n_{0} b-v, \quad a-b=\frac{u-v}{n_{0}} \in \mathbb{Q}
$$

原命题成立.

(2) $\frac{\left\{n_{0} a\right\}}{\left\{n_{0} b\right\}} \in \mathbb{Q}$ 但不为 1. 设 $\left\{n_{0} a\right\}=p s,\left\{n_{0} b\right\}=q s\left(p, q \in \mathbb{N}^{*}\right)$ 并不妨设 $p>q$, 取 $t \in \mathbb{N}^{*}$ 使

$$
\left(\frac{p}{q}\right)^{t}>\frac{10}{\varepsilon}
$$

由引理 2 知存在 $n_{1} \in \mathbb{N}^{*}$ 使

$$
\left\{n_{1} s\right\} \in\left(0, \frac{\varepsilon}{10 p^{t} q^{t}}\right)
$$

则有 $\left\{n_{1}\left\{n_{0} a\right\}\right\}=\left\{n_{1} p s\right\}=p\left\{n_{1} s\right\}$.

同理 $\left\{n_{1}\left\{n_{0} b\right\}\right\}=q\left\{n_{1} s\right\}$, 由条件得 $M\left(\left\{n_{1}\left\{n_{0} a\right\}\right\}\right)=M\left(\left\{n_{1}\left\{n_{0} b\right\}\right\}\right)$,故 $M\left(p\left\{n_{1} s\right\}\right)=M\left(q\left\{n_{1} s\right\}\right)$. 从而有

$$
M\left(p^{t}\left\{n_{1} s\right\}\right)=M\left(p^{t-1} q\left\{n_{1} s\right\}\right)=\cdots=M\left(q^{t}\left\{n_{1} s\right\}\right) .
$$

设 $a_{1}=p^{t}\left\{n_{1} s\right\}, b_{1}=q^{t}\left\{n_{1} s\right\}$, 则 $0<a_{1}, b_{1}<\frac{\varepsilon}{10}$ 且 $M\left(a_{1}\right)=M\left(b_{1}\right)$.

由于 $\left(\frac{p}{q}\right)^{t}>\frac{10}{\varepsilon}$, 故

$$
\frac{p^{t}}{q^{t}}(B-A)>\frac{10}{\varepsilon} \cdot 2 \varepsilon=20
$$

从而存在 $n_{2} \in \mathbb{N}^{*}$ 使得

$$
\frac{p^{t}}{q^{t}} A<n_{2}+C<n_{2}+D<\frac{p^{t}}{q^{t}} B
$$

又 $a_{1}<\frac{\varepsilon}{10} \leq\left(n_{2}+D\right)-\left(n_{2}+C\right)$, 故 $\exists n_{3} \in \mathbb{N}^{*}$ 使得

$$
n_{3} a_{1} \in\left(n_{2}+C, n_{2}+D\right) \text {, }
$$

故 $n_{3} \notin M\left(a_{1}\right)$; 又

$$
A<\frac{p^{t}}{q^{t}}\left(n_{2}+C\right)<\frac{p^{t}}{q^{t}}\left(n_{3} a_{1}\right)=n_{3} b_{1}<\frac{p^{t}}{q^{t}}\left(n_{2}+D\right)<B,
$$

故 $n_{3} \in M\left(b_{1}\right)$,与 $M\left(a_{1}\right)=M\left(b_{1}\right)$ 矛盾!

(3) $\frac{\left\{n_{0} a\right\}}{\left\{n_{0} b\right\}} \notin \mathbb{Q}$. 令 $a_{0}=\left\{n_{0} a\right\}, b_{0}=\left\{n_{0} b\right\}, c=\frac{A+B}{2}, d=\frac{C+D}{2}, z_{0}=\frac{a_{0}}{b_{0}}$, 由条件知 $M\left(a_{0}\right)=M\left(b_{0}\right)$, 由引理 2 知存在 $n_{2} \in \mathbb{N}^{*}$ 使得

$$
\left|\left\{n_{2} z_{0}\right\}-\left\{c-d z_{0}\right\}\right|<\frac{\varepsilon \sqrt{a_{0}^{2}+b_{0}^{2}}}{10 b_{0}}
$$

令 $n_{1}=\left[n_{2} z_{0}\right]-\left[c-d z_{0}\right]$, 则 $n_{1} \in \mathbb{N}^{*}$, 且

$$
\left|n_{1}-n_{2} z_{0}+\left(c-d z_{0}\right)\right|=\left|-\left\{n_{2} z_{0}\right\}+\left\{c-d z_{0}\right\}\right|<\frac{\varepsilon \sqrt{a_{0}^{2}+b_{0}^{2}}}{10 b_{0}}
$$

令 $f(x)=\left(n_{1}+c-a_{0} x\right)^{2}+\left(n_{2}+d-b_{0} x\right)^{2}$, 则

$$
\begin{aligned}
f(x)= & \left(a_{0}^{2}+b_{0}^{2}\right) x^{2}-2\left(a_{0}\left(n_{1}+c\right)+b_{0}\left(n_{2}+d\right)\right) x+\left(n_{1}+c\right)^{2}+\left(n_{2}+d\right)^{2} \\
= & \left(a_{0}^{2}+b_{0}^{2}\right)\left(x-\frac{a_{0}\left(n_{1}+c\right)+b_{0}\left(n_{2}+d\right)}{a_{0}^{2}+b_{0}^{2}}\right)^{2} \\
& \quad+\left(n_{1}+c\right)^{2}+\left(n_{2}+d\right)^{2}-\frac{\left(a_{0}\left(n_{1}+c\right)+b_{0}\left(n_{2}+d\right)\right)^{2}}{a_{0}^{2}+b_{0}^{2}} \\
= & \left(a_{0}^{2}+b_{0}^{2}\right)\left(x-\frac{a_{0}\left(n_{1}+c\right)+b_{0}\left(n_{2}+d\right)}{a_{0}^{2}+b_{0}^{2}}\right)^{2}+\frac{\left(b_{0}\left(n_{1}+c\right)-a_{0}\left(n_{2}+d\right)\right)^{2}}{a_{0}^{2}+b_{0}^{2}} .
\end{aligned}
$$

设 $x_{0}=\frac{a_{0}\left(n_{1}+c\right)+b_{0}\left(n_{2}+d\right)}{a_{0}^{2}+b_{0}^{2}}$, 则

$$
f\left(x_{0}\right)=\frac{\left(b_{0}\left(n_{1}+c\right)-a_{0}\left(n_{2}+d\right)\right)^{2}}{a_{0}^{2}+b_{0}^{2}}=\frac{b_{0}^{2}\left(n_{1}-n_{2} z_{0}+\left(c-d z_{0}\right)\right)^{2}}{a_{0}^{2}+b_{0}^{2}}<\frac{\varepsilon^{2}}{100},
$$

故 $\left|n_{1}+c-a_{0} x_{0}\right|,\left|n_{2}+d-b_{0} x_{0}\right|<\frac{\varepsilon}{10}$. 令 $n_{3}=\left[x_{0}\right]$, 则

$$
\begin{aligned}
& \left|n_{1}+c-a_{0} n_{3}\right|<\left|n_{1}+c-a_{0} x_{0}\right|+\left|a_{0}\right|<\frac{\varepsilon}{5} \\
& \left|n_{2}+d-b_{0} n_{3}\right|<\left|n_{2}+d-b_{0} x_{0}\right|+\left|b_{0}\right|<\frac{\varepsilon}{5}
\end{aligned}
$$

故 $n_{3} a_{0} \in\left(n_{1}+A, n_{1}+B\right), n_{3} b_{0} \in\left(n_{2}+C, n_{2}+D\right)$, 进而

$$
n_{3} \in M\left(a_{0}\right), \quad n_{3} \notin M\left(b_{0}\right)
$$

与 $M\left(a_{0}\right)=M\left(b_{0}\right)$ 矛盾!

综上,只有情况 1 成立, 故有原命题成立.

仔细分析这道题目的解法，可以看出线性相关和稠密性的思想贯穿了整个证明过程 (尤其是在两个引理的证明以及情况 3 的处理中), 这两个思想也是较为常见的数学竞赛题目的背景之一. 笔者也认为适当的了解高等数学的一些思想更有助于理解题目的本质, 有助于对解题思路的启发.

上述证明过程中的引理 2 就是著名的 Kronecker 定理, 运用本证明过程中的处理方法, 还可将此结果推广如下:

命题 无理数 $a_{1}, \cdots, a_{t}$ 满足对任意不全为 0 的有理数 $k_{1}, \cdots, k_{t}$ 都有 $k_{1} a_{1}+\cdots+k_{t} a_{t}$ 为无理数, 则对任意 $x_{1}, \cdots, x_{t} \in \mathbb{R}$ 和 $\varepsilon>0$, 都存在
$n, m_{1}, \cdots, m_{t} \in \mathbb{N}^{*}$, 使得

$$
\max _{1 \leq i \leq t}\left\{\left|m_{i}+x_{i}-n a_{i}\right|\right\}<\varepsilon
$$

证明 对 $t$ 归纳. $t=1$ 时即为上题中引理 2 的结果.

现假设命题对某个正整数 $t-1$ 成立, 我们证明命题对 $t$ 也成立.

由上题中引理 1 的结果, 存在 $n_{0} \in \mathbb{N}^{*}$ 使

$$
\left\{n_{0} a_{1}\right\}, \cdots,\left\{n_{0} a_{t}\right\} \in\left(0, \frac{\varepsilon}{10}\right) \cup\left(1-\frac{\varepsilon}{10}, 1\right) .
$$

若某个 $\left\{n_{0} a_{i}\right\} \in\left(1-\frac{\varepsilon}{10}, 1\right)$, 则可设 $a_{i}{ }^{\prime}=-a_{i}, x_{i}^{\prime}=-x_{i}, m_{i}{ }^{\prime}=-m_{i}$, 此时有

$$
\left|m_{i}{ }^{\prime}+x_{i}{ }^{\prime}-n a_{i}{ }^{\prime}\right|=\left|m_{i}+x_{i}-n a_{i}\right|,
$$

而 $\left\{n_{0} a_{i}{ }^{\prime}\right\} \in\left(0, \frac{\varepsilon}{10}\right)$, 故可不妨设 $\left\{n_{0} a_{1}\right\}, \cdots,\left\{n_{0} a_{t}\right\} \in\left(0, \frac{\varepsilon}{10}\right)$.

设 $\left\{n_{0} a_{i}\right\}=b_{i},\left[n_{0} a_{i}\right]=c_{i}(i=1, \cdots, t)$.

$$
f(z)=\sum_{i=1}^{t}\left(n_{i}+x_{i}-z b_{i}\right)^{2}, \quad z_{0}=\frac{\sum_{i=1}^{t}\left(n_{i}+x_{i}\right) b_{i}}{\sum_{i=1}^{t} b_{i}^{2}}
$$

则可得

$$
\begin{aligned}
f\left(z_{0}\right) & =\sum_{i=1}^{t}\left(n_{i}+x_{i}\right)^{2}-\frac{\left(\sum_{i=1}^{t}\left(n_{i}+x_{i}\right) b_{i}\right)^{2}}{\sum_{i=1}^{t} b_{i}^{2}} \\
& =\frac{1}{\sum_{i=1}^{t} b_{i}^{2}}\left(\sum_{i=1}^{t}\left(n_{i}+x_{i}\right)^{2} \sum_{i=1}^{t} b_{i}^{2}-\left(\sum_{i=1}^{t}\left(n_{i}+x_{i}\right) b_{i}\right)^{2}\right) \\
& =\frac{1}{\sum_{i=1}^{t} b_{i}^{2}}\left(\sum_{1 \leq i<j \leq t}\left(b_{i}\left(n_{j}+x_{j}\right)-b_{j}\left(n_{i}+x_{i}\right)\right)^{2}\right) .
\end{aligned}
$$

对于 $i=1, \cdots, t-1$, 设 $\frac{b_{t}}{b_{i}}=d_{i}$, 则由条件知 $d_{i}$ 为无理数. 进一步地,

$$
\begin{aligned}
f\left(z_{0}\right) & =\frac{b_{t}^{2}\left(\sum_{1 \leq i<j \leq t-1}\left(d_{i}^{-1}\left(n_{j}+x_{j}\right)-d_{j}^{-1}\left(n_{i}+x_{i}\right)\right)^{2}+\sum_{i=1}^{t-1}\left(d_{i}^{-1}\left(n_{t}+x_{t}\right)-\left(n_{i}+x_{i}\right)\right)^{2}\right)}{\sum_{i=1}^{t} b_{i}^{2}} \\
& =\frac{b_{t}^{2}\left(\sum_{1 \leq i<j \leq t-1} \frac{\left(d_{j}\left(n_{j}+x_{j}\right)-d_{i}\left(n_{i}+x_{i}\right)\right)^{2}}{d_{i}^{2} d_{j}^{2}}+\sum_{i=1}^{t-1} \frac{\left(\left(n_{t}+x_{t}\right)-d_{i}\left(n_{i}+x_{i}\right)\right)^{2}}{d_{i}^{2}}\right)}{\sum_{i=1}^{t} b_{i}^{2}}
\end{aligned}
$$

记 $\max \left\{d_{1}^{-1}, \cdots, d_{t-1}^{-1}, 1\right\}=r$, 由归纳假设知存在 $n_{1}, \cdots, n_{t} \in \mathbb{N}^{*}$ 使

$$
\max _{1 \leq i \leq t-1}\left\{\left|n_{i}+\left(x_{i}+x_{t} d_{i}^{-1}\right)-n_{t} d_{i}^{-1}\right|\right\}<\frac{\varepsilon \min \left\{d_{1}^{-1}, \cdots, d_{t-1}^{-1}\right\}}{10 r^{2} t}
$$

故

$$
\max _{1 \leq i \leq t-1}\left\{\left|\left(n_{t}+x_{t}\right)-d_{i}\left(n_{i}+x_{i}\right)\right|\right\}<\frac{\varepsilon}{10 r^{2} t}
$$

从而对任意 $i, j \in\{1, \cdots, t-1\}$, 有

$$
\begin{aligned}
& \left|d_{j}\left(n_{j}+x_{j}\right)-d_{i}\left(n_{i}+x_{i}\right)\right| \\
= & \left|\left(\left(n_{t}+x_{t}\right)-d_{i}\left(n_{i}+x_{i}\right)\right)-\left(\left(n_{t}+x_{t}\right)-d_{j}\left(n_{j}+x_{i}\right)\right)\right| \\
\leq & \left|\left(n_{t}+x_{t}\right)-d_{i}\left(n_{i}+x_{i}\right)\right|+\left|\left(n_{t}+x_{t}\right)-d_{j}\left(n_{j}+x_{i}\right)\right| \\
< & \frac{\varepsilon}{5 r^{2} t} .
\end{aligned}
$$

故有

$$
\begin{aligned}
f\left(z_{0}\right) & <\frac{b_{t}^{2}\left(\sum_{1 \leq i<j \leq t-1} \frac{\left(\frac{\varepsilon}{5 r^{2} t}\right)^{2}}{r^{-4}}+\sum_{i=1}^{t-1} \frac{\left(\frac{\varepsilon}{10 r^{2} t}\right)^{2}}{r^{-4}}\right)}{\sum_{i=1}^{t} b_{i}^{2}} \\
& <\sum_{1 \leq i<j \leq t-1} \frac{\left(\frac{\varepsilon}{5 r^{2} t}\right)^{2}}{r^{-4}}+\sum_{i=1}^{t-1} \frac{\left(\frac{\varepsilon}{10 r^{2} t}\right)^{2}}{r^{-4}} \\
& <t^{2} r^{4}\left(\frac{\varepsilon}{5 r^{2} t}\right)^{2} \\
& =\left(\frac{\varepsilon}{5}\right)^{2} .
\end{aligned}
$$

由 $f(z)$ 的定义知 $\max _{1 \leq i \leq t}\left\{\left|n_{i}+x_{i}-z_{0} b_{i}\right|\right\}<\frac{\varepsilon}{5}$.

令 $n=\left[z_{0}\right] n_{0}, m_{i}=n_{i}+\left[z_{0}\right] c_{i}(1 \leq i \leq t)$, 由 $b_{i}+c_{i}=n_{0} a_{i}$, 知

$$
m_{i}+x_{i}-n a_{i}=n_{i}+x_{i}-\left[z_{0}\right] b_{i} .
$$

因此

$$
\begin{aligned}
\max _{1 \leq i \leq t}\left\{\left|m_{i}+x_{i}-n a_{i}\right|\right\} & =\max _{1 \leq i \leq t}\left\{\left|n_{i}+x_{i}-\left[z_{0}\right] b_{i}\right|\right\} \\
& <\max _{1 \leq i \leq t}\left\{\left|n_{i}+x_{i}-z_{0} b_{i}\right|+\left|b_{i}\right|\right\} \\
& <\frac{3 \varepsilon}{10} \\
& <\varepsilon
\end{aligned}
$$

即命题对 $t$ 也成立.

故由归纳法知此命题成立.

例 3 (集训队测试第 23 题). 求证对任意 $m \in \mathbb{N}^{*}, m \geq 2$, 及 $x_{1}, x_{2}, \cdots, x_{m} \geq$ 0 ,

$$
(m-1)^{m-1}\left(\sum_{k=1}^{m} x_{k}^{m}-m \prod_{k=1}^{m} x_{k}\right) \geq\left(\sum_{k=1}^{m} x_{k}\right)^{m}-m^{m} \prod_{k=1}^{m} x_{k},
$$

并确定取等条件.

评析 本题是一个非常有趣的题目, 从这道题目的各种解法中可以领略到调
整法巧妙的应用.

通过观察 $m$ 较小的情况, 可以观察到这个不等式是相当强的(事实上, $m=2$ 时此式为恒等式, $m=3$ 时此式为舒尔不等式当 $r=1$ 的情形), 且取等条件不只有所有数都相等这一种情况, 通常的放缩方法, 如使用均值不等式, 柯西不等式以至于各种其他不等式似都难以奏效. 而本题的本质是两组算数平均值和几何平均值的差之间的比较, 而在历史上均值不等式的第一个证明也是用调整法给出的. 这时一个较为自然的想法就是使用调整法对本题中的式子进行放缩. (笔者至今也没能成功找到不使用调整或导数即可证出此题的方法)

调整法的具体表现有多种形式. 笔者在考试结束之后对本题进行了较为深入的思考, 成功找到了若干种适用于本题的调整法, 其中有固定 $\prod_{k=1}^{m} x_{k}$ 的方法,有固定 $\sum_{k=1}^{m} x_{k}$ 的方法, 有固定 $x_{i}-x_{j}(1 \leq i<j \leq m)$ 的方法. 以下展示的解法则是在从集训队的试题讲评中获得的思路从而完成的解答. 这个解答并不显简洁, 但采用了一般题目很少使用的一个调整思路:固定 $x_{1}+x_{2}+x_{3}$ 和 $x_{1} x_{2} x_{3}$. 我们先来看一下这个证明过程.

证明 先证明一个引理.

引理 给定 $p, r>0, r \leq \frac{1}{27} p^{3}$, 正整数 $n \geq 3$, 实数 $a_{1}, a_{2}, a_{3}>0, a_{1}+a_{2}+$ $a_{3}=p, a_{1} a_{2} a_{3}=r$. 则仅当 $a_{1}, a_{2}, a_{3}$ 中有两个相等,另一个不大于这两个时, $a_{1}^{n}+a_{2}^{n}+a_{3}^{n}$ 取得最小值.

证明 由条件知这样的 $a_{1}, a_{2}, a_{3}$ 存在, 若 $r=\frac{1}{27} p^{3}$, 则 $a_{1}=a_{2}=a_{3}=\frac{p}{3}$, 命题成立. 下设 $r<\frac{1}{27} p^{3}$. 不妨设 $a_{1} \leq a_{2} \leq a_{3}$, 则必有 $a_{1}<a_{3}$, 记 $S=a_{1}^{n}+a_{2}^{n}+a_{3}^{n}$,只需证明

$$
\frac{d S}{d a_{2}} \leq 0
$$

对条件中二式对 $a_{2}$ 求导得

$$
\frac{d a_{1}}{d a_{2}}+1+\frac{d a_{3}}{d a_{2}}=0, \frac{d a_{1}}{d a_{2}} a_{2} a_{3}+a_{1} a_{3}+\frac{d a_{3}}{d a_{2}} a_{1} a_{2}=0,
$$

解得

$$
\frac{d a_{1}}{d a_{2}}=\frac{a_{1} a_{3}-a_{1} a_{2}}{a_{1} a_{2}-a_{2} a_{3}}, \frac{d a_{3}}{d a_{2}}=\frac{a_{2} a_{3}-a_{1} a_{3}}{a_{1} a_{2}-a_{2} a_{3}} .
$$

故有

$$
\begin{aligned}
\frac{d S}{d a_{2}} & =n a_{1}^{n-1} \frac{a_{1} a_{3}-a_{1} a_{2}}{a_{1} a_{2}-a_{2} a_{3}}+n a_{2}^{n-1}+n a_{3}^{n-1} \frac{a_{2} a_{3}-a_{1} a_{3}}{a_{1} a_{2}-a_{2} a_{3}} \\
& =\frac{n\left(a_{1}^{n}\left(a_{3}-a_{2}\right)+a_{2}^{n}\left(a_{1}-a_{3}\right)+a_{3}^{n}\left(a_{2}-a_{1}\right)\right)}{a_{2}\left(a_{1}-a_{3}\right)} .
\end{aligned}
$$

另一方面，

$$
\begin{aligned}
& a_{1}^{n}\left(a_{3}-a_{2}\right)+a_{2}^{n}\left(a_{1}-a_{3}\right)+a_{3}^{n}\left(a_{2}-a_{1}\right) \\
= & \left(a_{2}-a_{1}\right)\left(a_{3}^{n}-a_{2}^{n}\right)+\left(a_{3}-a_{2}\right)\left(a_{1}^{n}-a_{2}^{n}\right) \\
= & \left(a_{2}-a_{1}\right)\left(a_{3}-a_{2}\right)\left(\sum_{m=0}^{n-1} a_{2}^{m} a_{3}^{n-1-m}-\sum_{m=0}^{n-1} a_{2}^{m} a_{1}^{n-1-m}\right) \\
\geq & 0 .
\end{aligned}
$$

故有

$$
\frac{d S}{d a_{2}} \leq 0
$$

从而引理成立.

回到原题. 令

$$
s=(m-1)^{m-1} \sum_{k=1}^{m} x_{k}^{m}+\left(m^{m}-m(m-1)^{m-1}\right) \prod_{k=1}^{m} x_{k}-\left(\sum_{k=1}^{m} x_{k}\right)^{m},
$$

需证明 $s \geq 0$.

当 $m=2$ 时,

$$
s=x_{1}^{2}+x_{2}^{2}+2 x_{1} x_{2}-\left(x_{1}+x_{2}\right)^{2}=0
$$

命题成立, 且对 $\forall x_{1}, x_{2} \geq 0$ 取等, 下设 $m \geq 3$.

若某个 $x_{i}=0$, 不妨设 $x_{m}=0$, 则由幕平均不等式,

$$
s=(m-1)^{m-1} \sum_{k=1}^{m-1} x_{k}^{m}-\left(\sum_{k=1}^{m-1} x_{k}\right)^{m} \geq 0
$$

当且仅当 $x_{1}=x_{2}=\cdots=x_{m-1}$ 时取等.

下设所有的 $x_{i}>0$, 这时对任意 $p, r>0, r \leq \frac{1}{m^{m}} p^{m}$, 记

$$
D=\left\{\left(x_{1}, \cdots, x_{m}\right) \mid \sum_{k=1}^{m} x_{k}=p, \prod_{k=1}^{m} x_{k}=r\right\}
$$

根据初等函数的性质, $\sum_{k=1}^{m} x_{k}^{m}$ 在 $D$ 上连续. 又由 $D$ 的定义知 $D$ 是闭集, 且显见 $D$ 有界, 故 $\sum_{k=1}^{m} x_{k}^{m}$ 在 $D$ 上有最小值. 设这个最小值点为 $\left(x_{10}, \cdots, x_{m 0}\right)$, 则由引理有 $x_{10}, \cdots, x_{m 0}$ 中任意三个都有两个相等, 另一个不大于这两个. 故必有其中 $m-1$ 个相等, 另一个不大于这 $m-1$ 个.

不妨设 $x_{10}=\cdots=x_{(m-1) 0}=x, x_{m 0}=y$, 则

$$
\begin{aligned}
s=( & m-1)^{m} x^{m}+(m-1)^{m-1} y^{m} \\
& +\left(m^{m}-m(m-1)^{m-1}\right) x^{m-1} y-((m-1) x+y)^{m} .
\end{aligned}
$$

只需证明对任意 $0 \leq y \leq x, s \geq 0$, 当且仅当 $y=0$ 或 $y=x$ 时取等. 而

$$
\begin{aligned}
\frac{d s}{d y} & =m(m-1)^{m-1} y^{m-1}+\left(m^{m}-m(m-1)^{m-1}\right) x^{m-1}-m((m-1) x+y)^{m-1}, \\
\frac{d^{2} s}{d y^{2}} & =m(m-1)^{m} y^{m-2}-m(m-1)((m-1) x+y)^{m-2} \\
& =m(m-1)\left(\left((m-1)^{\frac{m-1}{m-2}} y\right)^{m-2}-((m-1) x+y)^{m-2}\right),
\end{aligned}
$$

则 $\frac{d^{2} s}{d y^{2}}$ 在 $0 \leq y<\frac{m-1}{(m-1)^{\frac{m-1}{m-2}}-1} x$ 时为负, 在 $\frac{m-1}{(m-1)^{\frac{m-1}{m-2}}-1} x<y \leq x$ 时为正 (由 Bernoulli 不等式, $\left.\frac{m-1}{(m-1)^{\frac{m-1}{m-2}}-1}<1\right)$. 记

$$
t=\frac{m-1}{(m-1)^{\frac{m-1}{m-2}}-1} x
$$

则关于 $y$ 的函数 $\frac{d s}{d y}$ 在 $[0, t]$ 上递减, 在 $[t, x]$ 上递增. 又

$$
\left.\frac{d s}{d y}\right|_{y=0}=m\left(m^{m-1}-2(m-1)^{m-1}\right) x^{m-1}
$$

且

$$
m^{m-1}-2(m-1)^{m-1}>(m-1)^{m-1}+C_{m-1}^{1}(m-1)^{m-2}-2(m-1)^{m-1}=0
$$

故

$$
\left.\frac{d s}{d y}\right|_{y=0}>0,\left.\frac{d s}{d y}\right|_{y=x}=0
$$

由上述单调性知存在 $0<t_{1}<t$ 使得关于 $y$ 的函数 $\frac{d s}{d y}$ 在 $\left[0, t_{1}\right)$ 为正，在 $\left(t_{1}, x\right)$为负, 故关于 $y$ 的函数 $s$ 在 $\left[0, t_{1}\right]$ 递增, 在 $\left[t_{1}, x\right]$ 递减. 又

$$
\left.s\right|_{y=0}=\left.s\right|_{y=x}=0
$$

故有任意 $0 \leq y \leq x, s \geq 0$, 当且仅当 $y=0$ 或 $y=x$ 时取等.

综上所述，原不等式成立，取等条件为

$$
\left\{\begin{array}{l}
\forall x_{1}, x_{2} \geq 0(m=2) \\
m \text { 个数都相等或 } m-1 \text { 个相等另一个为 } 0(m \geq 3) .
\end{array}\right.
$$

评析 这个解法展示了如何通过固定多个对称式的结果进行调整, 其主要思想是将其中若干个变元视为一些独立变元的隐函数 (最好只有一个独立变元),再对待求的式子对独立变元求导, 从而达到最终目的. 这一方法可以扩展到很多齐次对称不等式的证明, 尤其是其他方法难以奏效时, 运用这个方法很可能有意想不到的效果.

另外, 本解答中避免无限调整的方法 (如果直接对这 $m$ 个变量使用引理势
必会造成无限调整) 也很值得思考, 这里采用了数学分析中有界闭集上的连续函数必有最值这一结果. 这一方法也可用于其他不等式的证明, 例如均值不等式, 以及一些竞赛题目.

致谢 本文最后笔者要感谢张雷老师和缠祥瑞老师的指导和帮助.

