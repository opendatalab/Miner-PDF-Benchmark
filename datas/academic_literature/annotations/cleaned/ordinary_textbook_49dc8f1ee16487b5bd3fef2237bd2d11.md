# 对一道数列征解题的探究 

翟霄宇<br>(重庆市巴蜀中学校, 401121)<br>指导教师: 肖佳劼

2020 年 1 月的美国数学月刊上有这样一道征解题:

问题 1 给定正实数 $C$, 求所有的正实数列 $\left\{x_{n}\right\}_{n=1}^{+\infty}$, 使得级数 $\sum_{n=1}^{+\infty} x_{n}$ 收玫,且对任意正整数 $k$, 都有

$$
\sum_{n=1}^{+\infty} \frac{x_{n} x_{n+k}}{x_{k}}=C
$$

官方答案中有一些错误, 本文试给出一个完整的新证明以及对这个问题的推广.

分析与解 记

$$
D\left(z_{0}, r\right)=\left\{z \in \mathbb{C}:\left|z-z_{0}\right|<r\right\}, z_{0} \in \mathbb{C}, r>0
$$

以及

$$
\bar{D}\left(z_{0}, r\right)=\left\{z \in \mathbb{C}:\left|z-z_{0}\right| \leq r\right\}, z_{0} \in \mathbb{C}, r>0
$$

考虑如下函数:

$$
f(z)=\sum_{n=1}^{+\infty} x_{n} z^{n}, z \in \bar{D}(0,1)
$$

由绝对收玫的幂级数的性质, 这个函数在 $\bar{D}(0,1)$ 上连续, 在 $D(0,1)$ 上解析.

考虑单位圆上复数 $z$, 有

$$
\begin{aligned}
& f(z) \overline{f(z)}=f(z) f\left(z^{-1}\right)=\sum_{n=1}^{+\infty} x_{n} z^{n} \cdot \sum_{m=1}^{+\infty} x_{m} z^{-m} \\
= & \sum_{n, m \geq 1} x_{n} x_{m} z^{n} z^{-m}=\sum_{n=1}^{+\infty} x_{n}^{2}+\sum_{1 \leq n<m} x_{n} x_{m} z^{-(m-n)}+\sum_{1 \leq m<n} x_{n} x_{m} z^{n-m}
\end{aligned}
$$

修订日期: 2021-07-08.

$$
\begin{aligned}
& =A^{2}+\sum_{k=1}^{+\infty} \sum_{n=1}^{+\infty} x_{n} x_{n+k} z^{-k}+\sum_{k=1}^{+\infty} \sum_{m=1}^{+\infty} x_{m+k} x_{m} z^{k} \\
& =A^{2}+\sum_{k=1}^{+\infty}\left(z^{k}+z^{-k}\right) \sum_{n=1}^{+\infty} x_{n} x_{n+k}=A^{2}+\sum_{k=1}^{+\infty} C x_{k}\left(z^{k}+z^{-k}\right) \\
& =A^{2}+C f(z)+C f\left(z^{-1}\right)=A^{2}+C f(z)+C \overline{f(z)},
\end{aligned}
$$

其中

$$
A^{2}=\sum_{n=1}^{+\infty} x_{n}^{2}>0, A>0
$$

且所有的和式变换都可以由绝对收玫得到.

由此即得

$$
|f(z)-C|^{2}=A^{2}+C^{2}, \forall|z|=1,
$$

特别地, $f$ 在单位圆上无零点.

对 $f(z)-C$ 用最大模原理得

$$
|f(z)-C| \leq \sqrt{A^{2}+C^{2}}, \forall z \in \bar{D}(0,1) .
$$

若 $z \in \bar{D}(0,1)$ 使

$$
f(z)=-\frac{A^{2}}{C}
$$

则

$$
|f(z)-C|=\frac{A^{2}}{C}+C=\frac{A^{2}+C^{2}}{C}>\frac{A^{2}+C^{2}}{\sqrt{A^{2}+C^{2}}}=\sqrt{A^{2}+C^{2}}
$$

矛盾! 从而

$$
A^{2}+C f(z) \neq 0, \forall z \in \bar{D}(0,1) .
$$

考虑函数

$$
g(z)=\frac{\sqrt{A^{2}+C^{2}} f(z)}{A^{2}+C f(z)}, z \in \bar{D}(0,1) .
$$

则 $g$ 在 $\bar{D}(0,1)$ 上连续, 在 $D(0,1)$ 上解析, 且

$$
g(0)=\frac{\sqrt{A^{2}+C^{2}} f(0)}{A^{2}+C f(0)}=0 .
$$

对 $|z|=1$, 有

$$
\begin{aligned}
|g(z)| & =\frac{\sqrt{A^{2}+C^{2}}|f(z)|}{\left|A^{2}+C f(z)\right|}=\frac{\sqrt{A^{2}+C^{2}}|f(z)|}{|f(z) \overline{f(z)}-C \overline{f(z)}|} \\
& =\frac{\sqrt{A^{2}+C^{2}}|f(z)|}{|f(z)||f(z)-C|}=\frac{\sqrt{A^{2}+C^{2}}}{|f(z)-C|}=1 .
\end{aligned}
$$

在这一步之后, 官方答案给出了如下的步骤:

函数 $g(z)$ 将 0 映射到 0 , 将单位圆映射到单位圆, 由 Schwarz 引理, 我们得到 $g$ 是一个旋转变换:

$$
g(z)=c z
$$

其中 $|c|=1$.

紧接着, 官方答案解出了 $f$, 并由此求出了数列的通项. 但是这是有问题的,因为 Schwarz 引理说的是:

连续函数 $f: \bar{D}(0,1) \rightarrow \mathbb{C}$ 在 $D(0,1)$ 上解析, 且将 0 映射到 0 , 将单位圆上的点映射到闭圆盘 $\bar{D}(0,1)$ 中，则有

$$
\left\{\begin{array}{l}
\left|f^{\prime}(0)\right| \leq 1, \\
|f(z)| \leq|z|, \quad \forall z \in D(0,1) \backslash\{0\} .
\end{array}\right.
$$

并且如果上述这些不等式(无限个) 只要有一个取到等号, 则 $f$ 是旋转变换.

如果仅仅只有 $f$ 将单位圆映射到单位圆, 则旋转变换的结论不成立, 例如令 $f(z)=z^{2}$ 或者, 更一般地, $f$ 为一些单位圆盘到自身的分式线性变换的乘积(不是复合).

为了修复这一问题, 我们需要更深入地挖掘 $g$ 的性质.

我们有

$$
g(1)=\frac{\sqrt{A^{2}+C^{2}} f(1)}{A^{2}+C f(1)}>0 .
$$

则 $g(1)=1$. 若存在 $g(z)=1,|z|=1, z \neq 1$, 则可知

$$
f(1)=f(z) .
$$

但是我们有

$$
|f(z)|=\left|\sum_{n=1}^{+\infty} x_{n} z^{n}\right| \leq \sum_{n=1}^{+\infty}\left|x_{n} z^{n}\right|=\sum_{n=1}^{+\infty} x_{n}=f(1)
$$

其中的等号取不到, 因为

$$
\frac{\left(x_{2} z^{2}\right)}{\left(x_{1} z\right)}=\frac{x_{2}}{x_{1}} z \in \mathbb{C} \backslash[0,+\infty)
$$

这产生了一个矛盾! 从而

$$
g(z) \neq 1, \forall|z|=1, z \neq 1 .
$$

引理 若连续函数 $g: \bar{D}(0,1) \rightarrow \mathbb{C}$ 在 $D(0,1)$ 中解析, 且 $g(0)=0, g(1)=1$,

$$
|g(z)|=1, g(z) \neq 1, \forall|z|=1, z \neq 1,
$$

则

$$
g(z)=z, \forall z \in \bar{D}(0,1) .
$$

引理证明 若 $g(z)$ 在 $D(0,1)$ 上有无限个零点(计重数), 取这些零点的一个极限点 $z$, 则 $z$ 在边界上, 从而 $|z|=1$. 由连续性, $g(z)=0$, 这与 $|g(z)|=1$ 矛盾! 从而 $g$ 在 $D(0,1)$ 上只有有限个零点(计重数). 取实数 $0<r_{0}<1$ 使 $r_{0}$ 大于所有这些零点的模长.

注意到如果 $r_{0}<|z| \leq 1$, 则 $g(z) \neq 0$. 由此易知, 可以由对称延拓, 将 $g(z)$延拓成 $D\left(0, r_{0}^{-1}\right)$ 上的解析函数. 记 $N$ 是 $g$ 在 $D(0,1)$ 内的零点个数(计重数),则由辐角原理可知

$$
N=\frac{1}{2 \pi \mathrm{i}} \int_{\gamma} \frac{g^{\prime}(z)}{g(z)} \mathrm{d} z=\frac{1}{2 \pi} \operatorname{Im}\left(\int_{\gamma} \frac{g^{\prime}(z)}{g(z)} \mathrm{d} z\right),
$$

其中 $\gamma$ 是逆时针定向的单位圆. 由 $g(0)=0$ 有 $N \in \mathbb{Z}_{+}$. 作对数函数的分支

$$
\ell\left(r \mathrm{e}^{\mathrm{i} \theta}\right)=\log r+\mathrm{i} \theta, r>0, \theta \in(0,2 \pi) .
$$

固定 $0<\varepsilon<\pi$, 结合 $g(z)$ 连续性以及集合

$$
K=\left\{\mathrm{e}^{\mathrm{i} \theta}: \varepsilon \leq \theta \leq 2 \pi-\varepsilon\right\}
$$

的紧性, 并注意到

$$
g(z) \in\{w \in \mathbb{C}:|w|=1, w \neq 1\} \subset \mathbb{C} \backslash[0,+\infty), \forall z \in K
$$

可知存在 $0<\delta<1-r_{0}$ 使得开集

$$
K_{\delta}=\{w \in \mathbb{C}: \exists z \in K,|w-z|<\delta\}
$$

满足

$$
g\left(K_{\delta}\right) \subset \mathbb{C} \backslash[0,+\infty)
$$

从而 $\ell \circ g$ 在 $K_{\delta}$ 上为解析函数.

由此可得

$$
\begin{aligned}
& \frac{1}{2 \pi} \operatorname{Im}\left(\int_{z=\mathrm{e}^{\mathrm{i} \theta}, \varepsilon \leq \theta \leq 2 \pi-\varepsilon} \frac{g^{\prime}(z)}{g(z)} \mathrm{d} z\right)=\frac{1}{2 \pi} \operatorname{Im}\left(\int_{z=\mathrm{e}^{\mathrm{i} \theta}, \varepsilon \leq \theta \leq 2 \pi-\varepsilon}(\ell \circ g)^{\prime}(z) \mathrm{d} z\right) \\
= & \frac{1}{2 \pi} \operatorname{Im}\left(\ell\left(g\left(\mathrm{e}^{\mathrm{i}(2 \pi-\varepsilon)}\right)\right)-\ell\left(g\left(\mathrm{e}^{\mathrm{i} \varepsilon}\right)\right)\right)<1,
\end{aligned}
$$

其中积分中的圆弧由 $\theta$ 从小到大定向.

则

$$
N=\frac{1}{2 \pi} \operatorname{Im}\left(\int_{\gamma} \frac{g^{\prime}(z)}{g(z)} \mathrm{d} z\right)
$$

$$
\begin{aligned}
& =\frac{1}{2 \pi} \operatorname{Im}\left(\int_{z=\mathrm{e}^{\mathrm{i} \theta},-\varepsilon \leq \theta \leq \varepsilon} \frac{g^{\prime}(z)}{g(z)} \mathrm{d} z\right)+\frac{1}{2 \pi} \operatorname{Im}\left(\int_{z=\mathrm{e}^{\mathrm{i} \theta}, \varepsilon \leq \theta \leq 2 \pi-\varepsilon} \frac{g^{\prime}(z)}{g(z)} \mathrm{d} z\right) \\
& <\frac{M_{0} \varepsilon}{\pi}+1
\end{aligned}
$$

其中 $M_{0}$ 是 $\left|g^{\prime} / g\right|$ 在单位圆上的最大值, 且积分中的所有圆弧由 $\theta$ 从小到大定向.

这对所有 $0<\varepsilon<\pi$ 成立. 令 $\varepsilon \rightarrow 0^{+}$知 $N \leq 1$. 结合 $N \in \mathbb{Z}_{+}$知 $N=1$.

上面的讨论证明了 $N=1$. 从而 0 为 $g$ 的单重零点.

由 $g(0)=0$, 存在函数 $h(z)$ 在 $\bar{D}(0,1)$ 上连续, 在 $D(0,1)$ 上解析, 且

$$
g(z)=z h(z), \forall z \in \bar{D}(0,1) .
$$

则

$$
|h(z)|=1, \forall|z|=1
$$

由于 0 是 $g$ 的单重零点, 则 $h$ 没有零点. 如果 $h$ 不是常数, 可知 $h(D(0,1))$为开集. 取 $h$ 在 $\bar{D}(0,1)$ 上模长的最大值与最小值, 设它们分别是 $M, m$, 则

$$
M>m>0 \text {. }
$$

由此可见 $M \neq 1$ 或者 $m \neq 1$. 于是存在 $z \in D(0,1)$ 使得 $|h(z)|$ 为 $h$ 的模长的某个最值, 但由 $|h(z)| \geq m>0$ 可知任意的 $r>0$, 在 $D(h(z), r)$ 中都既有模长大于 $|h(z)|$ 的, 又有模长小于 $|h(z)|$ 的. 但是 $|h(z)|$ 取到了模长的最大值或者最小值. 这推出

$$
D(h(z), r) \not \subset h(D(0,1)) .
$$

这与 $h(D(0,1))$ 是开集矛盾! 由此可得 $h$ 是常数. 结合

$$
h(1)=g(1)=1
$$

可得

$$
h(z)=1, \forall z \in \bar{D}(0,1) .
$$

这推出

$$
g(z)=z, \forall z \in \bar{D}(0,1) .
$$

引理得证。

回到原题. 由引理, $g(z)=z$, 进一步,

$$
f(z)=\frac{A^{2} z}{\sqrt{A^{2}+C^{2}}-C z} .
$$

从而

$$
x_{n}=A^{2} C^{-1}\left(\frac{C^{2}}{A^{2}+C^{2}}\right)^{\frac{n}{2}}, \forall n \in \mathbb{Z}_{+}
$$

令

$$
\lambda=\sqrt{\frac{C^{2}}{A^{2}+C^{2}}} \in(0,1),
$$

得

$$
x_{n}=C\left(\lambda^{-2}-1\right) \lambda^{n} \text {. }
$$

经检验, 对任何 $\lambda \in(0,1)$, 数列

$$
x_{n}=C\left(\lambda^{-2}-1\right) \lambda^{n}
$$

均符合条件. 从而这就是所有的满足条件的数列. 解毕!

注意到, 这个证明中的关键点是引理中计算 $g(z)$ 在单位圆盘中的零点个数. 由辐角原理, 直观地来看, 由于 $g(z)$ 把单位圆周映射到自身, 则 $g(z)$ 的零点个数就是当 $z=\mathrm{e}^{2 \pi \mathrm{i} x}$ 中 $x$ 从 0 跑到 1 时, $g(z)$ 在单位圆周上逆时针绕的圈数. 题目条件中的正实数列保证了单位圆周上只有 $z=1$ 处 $g(z)=1$, 从而直观来看, $g(z)$ 在单位圆周上只能绕一圈. 这里的证明就是量化之后的表述.

这也自然而然地引出了一个新的问题: 如果将题目条件中的正实数列改为非负实数列, 会发生什么呢? 此时, 这个复变函数的做法就不再奏效了.

问题 2 给定正实数 $C$, 求所有的非负实数列 $\left\{x_{n}\right\}_{n=1}^{+\infty}$, 使得级数 $\sum_{n=1}^{+\infty} x_{n}$ 收玫, 且对任意正整数 $k$, 都有

$$
\sum_{n=1}^{+\infty} x_{n} x_{n+k}=C x_{k}
$$

解 为了解决这个问题, 我们尝试将其归结为上一个问题.

首先, 有一个平凡解 $x_{n} \equiv 0$. 下面设 $\left\{x_{n}\right\}$ 不是平凡解.

考察集合

$$
I=\left\{k \in \mathbb{Z}_{+}: x_{k}>0\right\} \neq \varnothing
$$

断言, 集合 $I$ 满足以下两个性质:

$$
\begin{aligned}
& \text { (1) } k \in I \Rightarrow \exists x, y \in I, x-y=k \\
& \text { (2) } x, y \in I, x>y \Rightarrow x-y \in I
\end{aligned}
$$

事实上, 对于 (1), 直接由原式即可得到; 对于 (2), 通过在原式中取 $k=x-y$ 即
可得到.

如果 $I$ 为有限集, 在 (1) 中取 $k=\max I$ 即得矛盾. 从而 $I$ 是无限集. 设 $I$中元素从小到大排列为

$$
t=k_{1}<k_{2}<\cdots .
$$

下面归纳证明:

$$
k_{i}=t i, \forall i \in \mathbb{Z}_{+}
$$

当 $i=1$ 时, 结论显然成立. 设只要 $1 \leq i<m$ 结论都成立, 下证 $k_{m}=m t$,其中 $m>1$.

由 $(2)$, 可设 $k_{m}-k_{1}=k_{j}, 1 \leq j<m$. 则 $k_{m}=k_{1}+k_{j}=(1+j) t$. 而

$$
k_{m}>k_{m-1}=(m-1) t, 1 \leq j \leq m-1 \text {, }
$$

因此

$$
j=m-1, k_{m}=m t .
$$

由以上讨论, $(*)$ 式得证. 亦即

$$
I=\left\{t m: m \in \mathbb{Z}_{+}\right\}
$$

考虑数列

$$
y_{m}=x_{t m}, m \in \mathbb{Z}_{+}
$$

容易验证 $\left\{y_{m}\right\}$ 满足问题 1 的条件, 从而存在正实数 $\lambda_{0} \in(0,1)$, 满足

$$
y_{m}=C\left(\lambda_{0}^{-2}-1\right) \lambda_{0}^{m} \text {. }
$$

记 $\lambda=\lambda_{0}^{1 / t}$, 则有

$$
x_{n}= \begin{cases}0, & t \nmid n, \\ C\left(\lambda^{-2 t}-1\right) \lambda^{n}, & t \mid n .\end{cases}
$$

经检验, 以上数列符合条件. 从而所有满足问题条件的数列 $\left\{x_{n}\right\}$ 为

$$
x_{n}=0, \forall n \in \mathbb{Z}_{+} \text {, }
$$

以及

$$
x_{n}= \begin{cases}0, & t \nmid n, \\ C\left(\lambda^{-2 t}-1\right) \lambda^{n}, & t \mid n,\end{cases}
$$

其中 $\lambda$ 为 $(0,1)$ 中的任意实数, 且 $t$ 为任意正整数. 解毕!
注记 问题 1 证明在引理之外的部分用到了分析学中级数的知识和一些复变函数论的基础知识(复变函数的解析以及最大模原理),引理的证明用到了基础的拓扑学知识以及复变函数论的一些较难的知识(辐角原理). 问题 2 仅仅用到了初等数学的知识以及问题 1 的结论.

致谢 作者感谢审稿人的细致反馈和冷岗松教授的热心关怀.

