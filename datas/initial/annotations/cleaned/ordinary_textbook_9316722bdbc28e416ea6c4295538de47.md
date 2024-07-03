# 一道高中联赛试题的加强 

陈韫田 吴钒

(海亮高级中学, 311816)

指导教师: 赵斌

在 2022 年 11 月 27 日举行的高中数学联赛 A2 卷的二试第四题如下.

题 1 设 $k$ 是大于 2 的整数, 整数数列 $a_{0}, a_{1}, a_{2}, \cdots$ 满足 $a_{0}=0$, 且对任意非负整数 $i$, 均有 $a_{i+2}=k a_{i+1}-a_{i}$. 证明: 对任意正整数 $m$, 均有:

$$
(2 m) ! \mid a_{1} a_{2} a_{3} \cdots a_{3 m}
$$

现我们将证明更强的结论.

题 2 设 $k$ 是大于 2 的整数, 整数数列 $a_{0}, a_{1}, a_{2}, \cdots$ 满足 $a_{0}=0$, 且对任意非负整数 $i$, 均有 $a_{i+2}=k a_{i+1}-a_{i}$. 证明: 对任意正整数 $m \geq 3$, 均有:

$$
m ! \mid a_{1} a_{2} a_{3} \cdots a_{m} .
$$

证明 不妨设 $a_{1}=1$, 在证明中我们令,

$$
\alpha=\frac{k+\sqrt{k^{2}-4}}{2}, \beta=\frac{k-\sqrt{k^{2}-4}}{2},
$$

则 $\alpha+\beta=k, \alpha \beta=1, a_{n}=\frac{\alpha^{n}-\beta^{n}}{\alpha-\beta}$. 为叙述严谨, 首先我们先证明几个引理.

引理 1 设 $k^{\prime}$ 是大于 2 的整数, 令

$$
\alpha^{\prime}=\frac{k^{\prime}+\sqrt{k^{\prime 2}-4}}{2}, \beta^{\prime}=\frac{k^{\prime}-\sqrt{k^{2}-4}}{2}
$$

记 $s_{n}=\alpha^{\prime n}+\beta^{\prime n}$, 则对任意 $n \in \mathbb{N}$, 有 $s_{n} \in \mathbb{N}^{*}$.

证明 下面使用第二数学归纳法证明:

对于 $n=0$, 有 $s_{0}=2 ; n=1$, 有 $s_{1}=k^{\prime}$.

对于 $n \geq 2$, 由归纳假设易得,

$$
s_{n}=\left(\alpha^{\prime}+\beta^{\prime}\right) s_{n-1}-\alpha^{\prime} \beta^{\prime} s_{n-2}=k^{\prime} s_{n-1}-s_{n-2} \in \mathbb{Z}
$$[^0]且易得 $s_{n}>0$, 从而 $s_{n} \in \mathbb{N}^{*}$. 引理 1 证毕.

引理 2 设 $k^{\prime}$ 是大于 2 的整数, 若一个数列 $\left\{x_{n}\right\}_{n \geq 0}$ 满足: $x_{0}=0, x_{1}=1$, 且对任意 $n \in \mathbb{N}, x_{n+2}=k^{\prime} x_{n+1}-x_{n}$. 则对于 $i, j \in \mathbb{N}^{*}, i \mid j$, 有 $x_{i} \mid x_{j}$.

证明 令 $\alpha^{\prime}=\frac{k^{\prime}+\sqrt{k^{\prime 2}-4}}{2}, \beta^{\prime}=\frac{k^{\prime}-\sqrt{k^{\prime 2}-4}}{2}$. 则 $\alpha^{\prime} \beta^{\prime}=1$. 从而

$$
x_{n}=\frac{\alpha^{\prime n}-\beta^{\prime n}}{\alpha^{\prime}-\beta^{\prime}} \text {. }
$$

故 $x_{i} \left\lvert\, x_{j} \Longleftrightarrow \frac{x_{j}}{x_{i}} \in \mathbb{N}^{*}\right.$, 设 $j=m i, m \in \mathbb{N}^{*}$. 则

$$
\begin{aligned}
\frac{x_{j}}{x_{i}} & =\frac{\alpha^{\prime j}-\beta^{\prime j}}{\alpha^{\prime i}-\beta^{\prime i}} \\
& =\frac{\alpha^{\prime m i}-\beta^{\prime m i}}{\alpha^{\prime i}-\beta^{\prime i}}=\alpha^{\prime(m-1) i}+\alpha^{\prime(m-2) i} \beta^{\prime i}+\cdots+\beta^{\prime(m-1) i} \\
& =\left(\alpha^{\prime(m-1) i}+\beta^{\prime(m-1) i}\right)+\left(\alpha^{\prime(m-3) i}+\beta^{\prime(m-3) i}\right)+\cdots
\end{aligned}
$$

又由引理 1 知其为正整数. 引理 2 证毕.

引理 3 令 $k^{\prime}=\alpha^{s}+\beta^{s}, s \in \mathbb{N}^{*}$. 若数列 $\left\{x_{n}\right\}_{n \geq 0}$ 满足: $x_{0}=0, x_{1}=1$, 且对任意 $n \in \mathbb{N}, x_{n+2}=k^{\prime} x_{n+1}-x_{n}$. 则对于 $\forall n \in \mathbb{N}, x_{n}=\frac{a_{n s}}{a_{s}}$.

证明 下面使用第二数学归纳法:

对于 $n=0, x_{0}=0=\frac{a_{0}}{a_{s}}$; 对于 $n=1, x_{1}=1=\frac{a_{s}}{a_{s}}$.

对于 $n \geq 2$, 则由归纳假设知,

$$
\begin{aligned}
x_{n} & =k^{\prime} x_{n-1}-x_{n-2} \\
& =\frac{\left(\alpha^{s}+\beta^{s}\right)\left(\alpha^{(n-1) s}-\beta^{(n-1) s}\right)}{\alpha^{s}-\beta^{s}}-\frac{\alpha^{(n-2) s}-\beta^{(n-2) s}}{\alpha^{s}-\beta^{s}} \\
& =\frac{\alpha^{n s}-\beta^{n s}}{\alpha^{s}-\beta^{s}}=\frac{a_{n s}}{a_{s}} .
\end{aligned}
$$

引理 3 证毕.

引理 4 设 $k^{\prime}$ 是大于 2 的整数, 若一个数列 $\left\{x_{n}\right\}_{n \geq 0}$ 满足: $x_{0}=0, x_{1}=1$,且对任意 $n \in \mathbb{N}, x_{n+2}=k^{\prime} x_{n+1}-x_{n}$. 则对于任意非负整数 $t$ 及任意奇素数 $p$, $x_{1}, x_{2}, \cdots, x_{p^{t}}$ 中至少有一项为 $p^{t}$ 的倍数.

证明 下面使用数学归纳法:

对于 $t=0$ 显然成立; 对于 $t=1$, 令 $\alpha^{\prime}=\frac{k^{\prime}+\sqrt{k^{\prime 2}-4}}{2}, \beta^{\prime}=\frac{k^{\prime}-\sqrt{k^{\prime 2}-4}}{2}$, 则

$$
\begin{aligned}
x_{p} & =\frac{\alpha^{\prime p}-\beta^{\prime p}}{\alpha^{\prime}-\beta^{\prime}} \\
& =\frac{\mathrm{C}_{p}^{1} k^{\prime p-1}+\mathrm{C}_{p}^{3} k^{\prime p-3}\left(k^{\prime 2}-4\right)+\cdots+\mathrm{C}_{p}^{p}\left(k^{\prime 2}-4\right)^{\frac{p-1}{2}}}{2^{p-1}} \\
& \equiv\left(k^{\prime 2}-4\right)^{\frac{p-1}{2}} \cdot(\bmod p)
\end{aligned}
$$

而由费尔马小定理, $\left(k^{\prime 2}-4\right)^{p-1} \equiv 1$ 或 $0(\bmod p)$, 从而 $p \mid x_{p}\left(x_{p}-1\right)\left(x_{p}+1\right)$.

若 $p \mid x_{p}$, 则证毕.

若 $p \mid\left(x_{p}+1\right)$, 则

$$
\begin{aligned}
0 & \equiv x_{p}+x_{1}=\frac{\alpha^{\prime p}+\alpha^{\prime}-\beta^{\prime p}-\beta^{\prime}}{\alpha^{\prime}-\beta^{\prime}} \\
& =\frac{\left(\alpha^{\prime \frac{p+1}{2}}-\beta^{\prime \frac{p+1}{2}}\right)\left(\alpha^{\prime \frac{p-1}{2}}+\beta^{\prime \frac{p-1}{2}}\right)}{\alpha^{\prime}-\beta^{\prime}} \\
& =\frac{x_{\frac{p+1}{2}} x_{p-1}}{x_{\frac{p-1}{2}}}(\bmod p)
\end{aligned}
$$

故有 $p \left\lvert\, x_{\frac{p+1}{2}}\right.$ 或 $p \mid x_{p-1}$. 则证毕.

若 $p \mid\left(x_{p}-1\right)$, 则 $\left(k^{\prime 2}-4\right)^{\frac{p-1}{2}} \equiv 1(\bmod p)$. 则

$$
\begin{aligned}
0 & \equiv x_{p}-x_{1}=\frac{\alpha^{\prime p}-\alpha^{\prime}-\beta^{\prime p}+\beta^{\prime}}{\alpha^{\prime}-\beta^{\prime}} \\
& =\frac{\left(\alpha^{\prime \frac{p+1}{2}}+\beta^{\prime \frac{p+1}{2}}\right)\left(\alpha^{\prime \frac{p-1}{2}}-\beta^{\prime \frac{p-1}{2}}\right)}{\alpha^{\prime}-\beta^{\prime}} \\
& =\frac{x_{\frac{p-1}{2}} x_{p+1}}{x_{\frac{p+1}{2}}}(\bmod p)
\end{aligned}
$$

若 $p \left\lvert\, x_{\frac{p-1}{2}}\right.$, 则证毕.

若 $p \nmid x_{\frac{p-1}{2}}$, 则 $p \mid x_{p+1}$. 又

$$
\begin{aligned}
0 \equiv x_{p+1} & =\frac{\mathrm{C}_{p+1}^{1} k^{\prime p}+\mathrm{C}_{p+1}^{3} k^{\prime p-2}\left(k^{\prime 2}-4\right)+\cdots+\mathrm{C}_{p+1}^{p} k^{\prime}\left(k^{\prime 2}-4\right)^{\frac{p-1}{2}}}{2^{p}} \\
& \equiv \frac{p+1}{2}\left(k^{\prime p-1}+\left(k^{\prime 2}-4\right)^{\frac{p-1}{2}}\right) \cdot k^{\prime} \equiv k^{\prime} \quad(\bmod p) .
\end{aligned}
$$

则 $p \mid x_{2}=k^{\prime}$, 证毕.

对于 $t \geq 2$, 若对 $t \leq l-1$ 时成立.

下证 $t=l$ 时成立. 设 $p^{l-1} \mid x_{q}, 1 \leq q \leq p^{l-1}$.

构造数列 $\left\{y_{n}\right\}: y_{0}=0, y_{1}=1, y_{n+2}=k_{0} y_{n+1}-y_{n}, k_{0}=\alpha^{\prime q}+\beta^{\prime q}$. 则由引理 3 知 $\forall n \in \mathbb{N}^{*}, y_{n}=\frac{x_{n q}}{x_{q}}$, 故仅需证明 $y_{1}, y_{2}, \cdots, y_{p}$ 中有一项为 $p$ 的倍数即可.

又 $k_{0}=\alpha^{\prime q}+\beta^{\prime q}$ 由引理 1 知其为正整数. 即转化为了 $t=1$ 的情形. 故 $x_{q}, x_{2 q}, \cdots, x_{p q}$ 中有项是 $p^{l}$ 的倍数. 又 $p q \leq p^{l}$, 故我们完成里归纳假设. 引理 4 证毕.

回到原题. 对 $\forall t \in \mathbb{N}^{*}$, 由引理 4 设 $\left\{a_{n}\right\}_{n \geq 1}$ 中第一个为 $p^{t}$ 的倍数的项记为 $a_{s}$, 则 $s \leq p^{t}, p$ 为奇素数. 又由引理 $2, \forall r \in \mathbb{N}^{*}, a_{r} \mid a_{r s}$, 故有 $\forall r \in \mathbb{N}^{*}, p^{t} \mid a_{r s}$.

故对 $\forall m, t \in \mathbb{N}^{*}, a_{1}, a_{2}, \cdots, a_{m}$ 中 $a_{s}, a_{2 s}, \cdots, a_{s \cdot\left\lfloor\frac{m}{s}\right\rfloor}$ 都为 $p^{t}$ 的倍数, 故至少有 $\left\lfloor\frac{m}{s}\right\rfloor$ 个 $p^{t}$ 的倍数.

但 $1,2, \cdots, m$ 中 $p^{t}$ 的倍数共有 $\left\lfloor\frac{m}{p^{t}}\right\rfloor$ 个, 而 $\left\lfloor\frac{m}{p^{t}}\right\rfloor \leq\left\lfloor\frac{m}{s}\right\rfloor$. 故对于 $\forall t \in \mathbb{N}^{*}$ 及
奇素数 $p, a_{1}, a_{2}, \cdots, a_{m}$ 中 $p^{t}$ 的倍数的个数不少于 $1,2, \cdots, m$ 中 $p^{t}$ 的倍数的个数. 从而对任意奇素数 $p$ 有,

$$
v_{p}\left(\prod_{i=1}^{m} a_{i}\right) \geq v_{p}(m !)
$$

引理 5 设 $k^{\prime}$ 是大于 2 的偶数, 若数列 $\left\{x_{n}\right\}_{n \geq 0}$ 满足: $x_{0}=0, x_{1}=1$, 且对任意 $n \in \mathbb{N}, x_{n+2}=k^{\prime} x_{n+1}-x_{n}$. 则对任意 $m \in \mathbb{N}^{*}$, 有 $2^{m} \mid x_{2^{m}}$.

证明 下面使用数学归纳法:

对于 $m=1,2 \mid x_{2}=k^{\prime}$, 若对 $m=l-1$ 时成立. $l \geq 2$, 下证 $m=l$ 时成立.

事实上只需证明 $2 \left\lvert\, \frac{x_{2^{l}}}{x_{2^{l-1}}}\right.$ 即可. 令 $\alpha^{\prime}=\frac{k^{\prime}+\sqrt{k^{\prime 2}-4}}{2}, \beta^{\prime}=\frac{k^{\prime}-\sqrt{k^{\prime 2}-4}}{2}$, 并令 $s_{n}=\alpha^{\prime n}+\beta^{n}$, 则

$$
\frac{x_{2^{l}}}{x_{2^{l-1}}}=\alpha^{\prime 2^{l-1}}+\beta^{\prime 2^{l-1}}=s_{2^{l-1}} .
$$

又 $s_{0}=2, s_{1}=k^{\prime}$ 皆为偶数, 从而由归纳假设知道, 对任意 $n \geq 2$, 都有 $s_{n}=k^{\prime} s_{n-1}-s_{n-2}$ 为偶数, 故 $2 \mid s_{2^{l-1}}$. 故证毕.

回到原题. 若 $2 \mid k$, 则由引理 5 知对任意 $t \in \mathbb{N}^{*}, 2^{t} \mid a_{2^{t}}$, 又由引理 2 , $\forall s, t \in \mathbb{N}^{*}, 2^{t} \mid a_{2^{t} \cdot s}$. 故 $\forall t, m \in \mathbb{N}^{*}, a_{1}, a_{2}, \cdots, a_{m}$ 中 $2^{t}$ 的倍数的个数至少为 $\left\lfloor\frac{m}{2^{t}}\right\rfloor$ 个, 又 $1,2, \cdots, m$ 中 $2^{t}$ 的倍数的个数为 $\left\lfloor\frac{m}{2^{t}}\right\rfloor$ 个. 故有,

$$
v_{2}\left(\prod_{i=1}^{m} a_{i}\right) \geq v_{2}(m !)
$$

若 $2 \nmid k$, 知 $a_{3}=k^{2}-1$, 则 $8 \mid a_{3}$, 构造数列 $\left\{x_{n}\right\}, x_{0}=0, x_{1}=1, \forall n \in$ $\mathbb{N}, x_{n+2}=k^{\prime} x_{n+1}-x_{n}, k^{\prime}=\alpha^{3}+\beta^{3}=k\left(k^{2}-3\right)$, 则由引理 $3, \forall n \in \mathbb{N}^{*}, x_{n}=\frac{a_{3 n}}{a_{3}}$. 又 $2 \mid k^{\prime}=k\left(k^{2}-3\right)$. 由引理 5,

$$
v_{2}\left(\prod_{i=1}^{m} \frac{a_{3 i}}{a_{3}}\right) \geq v_{2}\left(\prod_{i=1}^{m} x_{i}\right) \geq v_{2}(m !)
$$

故,

$$
\begin{aligned}
v_{2}\left(\prod_{i=1}^{3 m} a_{i}\right) & \geq m v_{2}\left(a_{3}\right)+v_{2}(m !) \geq 3 m+v_{2}(m !) \\
& =2 m+v_{2}((2 m) !)=v_{2}((4 m) !)
\end{aligned}
$$

又，

$$
\begin{aligned}
& v_{2}\left(\prod_{i=1}^{3 m+1} a_{i}\right) \geq v_{2}((4 m) !) \geq v_{2}((3 m+1) !) \\
& v_{2}\left(\prod_{i=1}^{3 m+2} a_{i}\right) \geq v_{2}((4 m) !) \geq v_{2}((3 m+2) !)
\end{aligned}
$$

最后一个式子在 $m \geq 2$ 时是由于 $4 m \geq 3 m+2$, 而在 $m=1$ 也成立时由于 5 是
奇数.

综上我们有, 对 $\forall m \in \mathbb{N}, m \geq 3$, 有,

$$
m ! \mid a_{1} a_{2} a_{3} \cdots a_{m}
$$

故我们完成了证明.


[^0]:    修订日期: 2022-12-28.

