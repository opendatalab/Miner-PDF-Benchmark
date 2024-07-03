# 与 $\{x\}$ 相关的一些数论性质 

张晚治

(河北省石家庄第二中学 ,051430)

近年来, 国内外出现一些关于小数部分的不等式. 本文选取了几个有意思的结果, 并归纳总结 供有兴趣的读者参考. 在本文中, $\{x\}$ 均表示 $x$ 的小数部分. 我们先看一道经典试题.

题 1 求最大的正数 $\lambda$, 使得对任意 $n \in \mathbb{N}^{*}$ 均有: $\{\sqrt{2} n\}>\frac{\lambda}{n}$.

解 $\lambda_{\max }=\frac{1}{2 \sqrt{2}}$.

先证 $\{\sqrt{2} n\}>\frac{1}{2 \sqrt{2} n}$. 令 $t=[\sqrt{2} n]$, 则

$$
\{\sqrt{2} n\}=\sqrt{2} n-t=\frac{2 n^{2}-t^{2}}{\sqrt{2} n+t}
$$

由于 $2 n, t$ 均为整数, 故 $2 n^{2}-t^{2} \geq 1$, 结合 $t<\sqrt{2} n$ 知

$$
\{\sqrt{2} n\} \geq \frac{1}{\sqrt{2} n+t}>\frac{1}{2 \sqrt{2} n}
$$

再证 $\lambda \leq \frac{1}{2 \sqrt{2}}$. 只需证: 对任意 $\varepsilon>0$, 总存在 $n \in \mathbb{N}^{*}$, 使得

$$
\{\sqrt{2} n\}<\frac{1+\varepsilon}{2 \sqrt{2} n}
$$

考虑佩尔方程 $x^{2}-2 y^{2}=-1$, 由于 $x=y=1$ 是一组解, 故方程有无穷组解. 取一组解 $(m, n)$, 满足 $n>\frac{1}{2 \sqrt{2}}\left(1+\frac{1}{\varepsilon}\right)$. 变形得

$$
\frac{1+\varepsilon}{2 \sqrt{2} n}>\frac{1}{2 \sqrt{2} n-1}
$$

由 $m^{2}-2 n^{2}=-1$ 知, $m^{2}<2 n^{2}<(1+m)^{2}$, 故 $m=[\sqrt{2} n]$. 从而由 (1) 知,

$$
\{\sqrt{2} n\}=\frac{2 n^{2}-m^{2}}{\sqrt{2} n+m}=\frac{1}{\sqrt{2} n+m} .
$$

又 $m>\sqrt{2} n-1$, 故

$$
\{\sqrt{2} n\}<\frac{1}{2 \sqrt{2} n-1} .
$$

修订日期: 2019-07-04.
结合上式与 $(2)$ 便知 $(*)$ 成立.

评注 $\{\sqrt{2} n\}$ 难以化简, 用定义化为 $\sqrt{2} n-[\sqrt{2} n]$, 分子有理化后, 利用整数的离散性和 Pell 方程进行离散估计得到结论.

题 2 (1) 设 $p$ 是整数, $q$ 是正整数, 证明: $\left|\sqrt{2}-\frac{p}{q}\right|>\frac{1}{3 q^{2}}$.

(2) 设正整数 $p, q$ 满足 $\frac{p}{q}<\sqrt{11}$, 证明: $\sqrt{11}-\frac{p}{q}>\frac{1}{2 p q}$.

(2018 年波罗的海数学奥林匹克)

证明 (1) 注意到 $\frac{p}{q}$ 为有理数, 由于原结论对某些距离 $\sqrt{2}$ 较远的 $\frac{p}{q}$ 比较显然, 而另一些并不显然. 考虑对 $\frac{p}{q}$ 分三种情况讨论.

当 $\frac{p}{q}<\sqrt{2}$ 时, 即有 $p<\sqrt{2} q$, 故

$$
\left|\sqrt{2}-\frac{p}{q}\right|=\sqrt{2}-\frac{p}{q}=\frac{2 q^{2}-p^{2}}{q(\sqrt{2} q+p)} \geq \frac{1}{q(\sqrt{2} q+p)} \geq \frac{1}{2 \sqrt{2} q^{2}}>\frac{1}{3 q^{2}} .
$$

当 $\sqrt{2}<\frac{p}{q}<3-\sqrt{2}$ 时, 有

$$
\left|\sqrt{2}-\frac{p}{q}\right|=\frac{p}{q}-\sqrt{2}=\frac{p^{2}-2 q^{2}}{q(p+\sqrt{2} q)} \geq \frac{1}{q(p+\sqrt{2} q)}>\frac{1}{3 q^{2}} .
$$

当 $\frac{p}{q}>3-\sqrt{2}$ 时, 若 $q=1$, 则 $p>3-\sqrt{2}$, 从而由 $p$ 是整数知 $p \geq 2$,

$$
p-\sqrt{2} \geq 2-\sqrt{2}>\frac{1}{3}=\frac{1}{3 q^{2}}
$$

命题成立. 若 $q \geq 2$, 则

$$
\frac{p}{q}-\sqrt{2}>3-2 \sqrt{2}>\frac{1}{12} \geq \frac{1}{3 q^{2}}
$$

命题亦成立.

(2) 当 $\frac{p}{q} \leq 3$ 时, 若 $p q=1$, 则

$$
\sqrt{11}-\frac{p}{q}=\sqrt{11}-1>\frac{1}{2}=\frac{1}{2 p q} \text {. }
$$

若 $p q \geq 2$, 则

$$
\sqrt{11}-\frac{p}{q}=\sqrt{11}-3>\frac{1}{4} \geq \frac{1}{2 p q} \text {. }
$$

当 $\frac{p}{q}>3$ 时, 即证 $q \sqrt{11}-p>\frac{1}{2 p}$, 这等价于

$$
\frac{11 q^{2}-p^{2}}{\sqrt{11} q+p}>\frac{1}{2 p}
$$

注意到 $p^{2} \equiv-1(\bmod 11)$ 无解, 故 $11 q^{2}-p^{2} \geq 2$. 故要证 $(*)$ 只需证

$$
\frac{2}{\sqrt{11} q+p}>\frac{1}{2 p}
$$

即证 $3 p>\sqrt{11} q$, 由 $\frac{p}{q}>3$ 知成立. 故 $(*)$ 成立, 从而命题成立.

评注 (i). 题 1 中, 不等式右边是关于 $n$ 的式子, 因此只需对分子有理化后的分子应用 Pell 方程的结论. 在分母放缩时, 由于 $\{x\}$ 可趋于 0 , 放缩几乎是“无损的”. 由于题 2 右边涉及有理数的分子与分母, 因此需对有理数大小进行估计,再用 Pell 方程的结论.

(ii). 上面两道题无一例外是对二次代数数进行逼近, 所以绕不开对 Pell 方程是否有解的试探. 更一般地, 下面的 Hwrwitz 不等式是对无理数更精确的逼近: 设 $a \in \mathbb{R}$, 则存在整数 $p, q$, 使得 $\left|a-\frac{p}{q}\right|<\frac{1}{\sqrt{5} q^{2}}$.

值得指出的是, $\sqrt{5}$ 是最佳常数, 证明见文献 [1].

对 $n$ 次代数数而言, 有如下的结果:

刘维尔定理 设 $\theta$ 为 $n$ 次代数数, 存在 $c>0$, 使得对任意 $a, b \in \mathbb{Z}, b>0$, 均有 $\left|\theta-\frac{a}{b}\right|>\frac{c}{b^{n}}$.

证明见文献 [1]. 由刘维尔定理知, 对于一个 $n$ 次代数数, 不可能存在一个高于 $n$ 阶的逼近(在题 2 中体现为 $p q, q^{2}$ ), 该定理也从侧面给出了一个判定超越数的条件。

题 3 给定正奇数 $a$ 和有理数 $b$, 其既约分数表示形式的分母为奇数. 对任意 $m, n \in \mathbb{N}^{*}$, 定义 $M(n, m)=\left|n \sqrt{n^{2}+a}-b m\right|$. 证明:

(1) 至多只有有限对正整数 $(n, m)$, 使得 $M(n, m)=0$;

(2) 存在正常数 $c$, 使得对任意 $n, m \in \mathbb{N}^{*}$, 若 $M(n, m) \neq 0$, 则 $M(n, m) \geq c$.

(2018 年白俄罗斯数学奥林匹克 11 年级第 7 题)

证明 (1) 若 $M(n, m)=0$, 则有 $n \sqrt{n^{2}+a}=b m$, 即有

$$
n^{2}+a=\left(\frac{b m}{n}\right)^{2}
$$

于是 $\frac{b m}{n}$ 为整数. 从而 $a$ 可以表示成两个整数的平方差, 又 $a$ 表示成两个整数的平方差只有有限种方法, 故满足 $M(n, m)=0$ 的 $(n, m)$ 只有有限多对.

(2) 先证: $\lim _{n \rightarrow \infty}\left\{n \sqrt{n^{2}+a}\right\}=\frac{1}{2}$.

事实上,

$$
\begin{aligned}
\lim _{n \rightarrow \infty} & \left(\sqrt{\left(n^{2}+\frac{a}{2}\right)^{2}}-\sqrt{\left(n^{2}+\frac{a}{2}\right)^{2}-\frac{a^{2}}{4}}\right) \\
& =\lim _{n \rightarrow \infty} \frac{\frac{a^{2}}{4}}{\sqrt{\left(n^{2}+\frac{a}{2}\right)^{2}+\sqrt{\left(n^{2}+\frac{a}{2}\right)^{2}-\frac{a^{2}}{4}}}}=0,
\end{aligned}
$$

又 $\lim _{n \rightarrow \infty}\left\{\sqrt{\left(n^{2}+\frac{a}{2}\right)^{2}}\right\}=\frac{1}{2}$ (因 $a$ 是奇数), 故

$$
\lim _{n \rightarrow \infty}\left\{n \sqrt{n^{2}+a}\right\}=\lim _{n \rightarrow \infty} \sqrt{\left(n^{2}+\frac{a}{2}\right)^{2}-\frac{a^{2}}{4}}=\frac{1}{2}
$$

设 $b$ 表示成既约分数时的分母为奇素数 $p$. 则由 $(*)$ 知, 存在 $N$, 当 $n>N$时, 有

$$
\frac{1}{2}-\frac{1}{4 p} \leq\left\{n \sqrt{n^{2}+a}\right\} \leq \frac{1}{2}+\frac{1}{4 p}
$$

分母为 $p$ 且与 $\frac{1}{2}$ 最接近的两个分数为 $\frac{\frac{p+1}{2}}{p} 、 \frac{\frac{p-1}{2}}{p}$, 这两个数与 $\frac{1}{2}$ 的差的绝对值均为 $\frac{1}{4 p}$, 故

$$
\left|\{b m\}-\frac{1}{2}\right| \geq \frac{1}{4 p}
$$

于是, 当 $n>N$ 时,

$$
M(n, m)=\left|n \sqrt{n^{2}+a}-b m\right| \geq\left|\left\{n \sqrt{n^{2}+a}\right\}-\{b m\}\right| \geq \frac{1}{4 p}
$$

对于每个 $1 \leq n \leq N,\left|n \sqrt{n^{2}+a}-b m\right|$ 为关于 $m$ 的函数, 设其非零最小值为 $f(n)$. 取

$$
c=\min \left\{f(1), f(2), \cdots, f(N), \frac{1}{4 p}\right\}
$$

结合 $(* *)$ 便知 $c$ 满足要求.

评注 此题对 $n$ 较大时, 进行间距估计, 得到一个下界估计. 在 $n$ 较小时, 只有有限种情况, 必存在非零最小值.

题 4 对任意 $n \in \mathbb{N}$, 证明:

$$
|\{\sqrt{2} n\}-\{\sqrt{3} n\}|>\frac{1}{20 n^{3}} .
$$

证明 要证原命题只需证(将两个小数部分合并)

$$
1-\frac{1}{20 n^{3}}>\{(\sqrt{3}-\sqrt{2}) n\}>\frac{1}{20 n^{3}} .
$$

令 $x=(\sqrt{3}-\sqrt{2}) n$, 则 $x<n, x^{2}=(5-2 \sqrt{6}) n^{2}$, 进一步,

$$
x^{4}-10 n^{2} x^{2}=-n^{4} .
$$

于是, 由二次函数的单调性知,

$$
\left[x^{2}\right]^{2}-10 n^{2}\left[x^{2}\right]+n^{4}>0, \quad\left\lceil x^{2}\right\rceil^{2}-10 n^{2}\left\lceil x^{2}\right\rceil+n^{4}<0
$$

其中 $\lceil y\rceil$ 表示大于 $y$ 的最小整数.
a) 证明: $\left\{x^{2}\right\} \geq \frac{1}{10 n^{2}},\left\{-x^{2}\right\}=\left\lceil x^{2}\right\rceil-x^{2}>\frac{1}{10 n^{2}}$.

由 (1) 知,

$$
\left(\left[x^{2}\right]+\left\{x^{2}\right\}\right)^{2}-10 n^{2}\left(\left[x^{2}\right]+\left\{x^{2}\right\}\right)+n^{4}=0 .
$$

结合 (2) 知,

$$
\left(10 n^{2}-2\left[x^{2}\right]\right)\left\{x^{2}\right\}-\left(x^{2}\right)^{2}=\left[x^{2}\right]^{2}-10 n^{2}\left[x^{2}\right]+n^{4}>0
$$

于是, $10 n^{2}\left\{x^{2}\right\} \geq 1$, 即 $\left\{x^{2}\right\} \geq \frac{1}{10 n^{2}}$.

令 $a=\left\lceil x^{2}\right\rceil, b=\left\lceil x^{2}\right\rceil-x^{2}$. 则由 (1), (2) 知,

$$
b\left(10 n^{2}-2 a+b\right)=10 n^{2} a-a^{2}-n^{4}>0,
$$

故

$$
b \geq \frac{1}{10 n^{2}-2 a+b}>\frac{1}{10 n^{2}} .
$$

b) 再证: $1-\frac{1}{20 n^{3}}>\{x\}>\frac{1}{20 n^{3}}$.

一方面, 由 $x=[x]+\{x\}$ 知,

$$
\left\{x^{2}\right\}=\left\{(\{x\}+[x])^{2}\right\}=\left\{\{x\}^{2}+2[x]\{x\}\right\}=\left\{2 x\{x\}-\{x\}^{2}\right\}
$$

又 $\left\{x^{2}\right\} \geq \frac{1}{10 n^{2}}$, 故 $\left\{2 x\{x\}-\{x\}^{2}\right\}>\frac{1}{10 n^{2}}$. 于是

$$
2 x\{x\}-\{x\}^{2} \geq \frac{1}{10 n^{2}}
$$

从而 $2 x\{x\} \geq \frac{1}{10 n^{2}}$, 故

$$
\{x\}>\frac{1}{20 n^{2} x}>\frac{1}{20 n^{3}} .
$$

$(*)$ 右式得证.

另一方面, 由 $x=\lceil x\rceil-\{-x\}$ 知,

$$
\left\{-x^{2}\right\}=\left\{-(\lceil x\rceil-\{-x\})^{2}\right\}=\left\{-\{-x\}^{2}+2\lceil x\rceil\{-x\}\right\}=\left\{2 x\{-x\}+\{-x\}^{2}\right\}
$$

又 $\left\{-x^{2}\right\} \geq \frac{1}{10 n^{2}}$, 故 $\left\{2 x\{-x\}+\{-x\}^{2}\right\}>\frac{1}{10 n^{2}}$. 于是

$$
\{-x\}>\frac{1}{20 n^{2} x}>\frac{1}{20 n^{3}},
$$

这等价于 $\{x\}<1-\frac{1}{20 n^{3}},(*)$ 左式得证.

评注 (i). 注意到 $\sqrt{3}-\sqrt{2}$ 是方程 $x^{4}-10 x^{2}+1$ 的根, 但 $\frac{1}{20 n^{3}}$ 的阶为 -3 ,故考虑先对 $\left\{(\sqrt{3}-\sqrt{2})^{2} n^{2}\right\}$ 放缩, 再放缩 $\{(\sqrt{3}-\sqrt{2}) n\}$.

(ii). 一般地, 该命题有如下推广版本: 若 $a, b \in \mathbb{N}^{*}$ 为非完全平方数,则

$$
|\{\sqrt{a} n\}-\{\sqrt{b} n\}|>\frac{1}{4(a+b) n^{3}} .
$$

(iii). 更一般地, 若 $k$ 个整数 $a_{1}, \cdots, a_{k}$ 均为非完全平方数,则

$$
\left|\sum_{i=1}^{k}\left\{n \sqrt{a_{i}}\right\}\right|>\frac{c}{n^{2^{k}-1}},
$$

其中 $c=\left(2 \sum_{i=1}^{k} \sqrt{a_{i}}\right)^{1-2^{k}}$.

下面的题目难度较大, 需要较强的代数变形能力, 对恒等式的离散估计, 以及对小数部分的精确放缩.

题 5 求最大的正实数 $c$, 使得对于任意满足 $a+b \in \mathbb{N}^{*}$ 的正实数 $a, b$, 均有

$$
\left\{a^{2}\right\}+\left\{b^{2}\right\} \leq 2-\frac{c}{(a+b)^{2}}
$$

(2018 年北京大学数学营试题)

解 所求最大的正实数 $c=\frac{3}{4}$.

引理 1 不存在整数 $x, y, z$ 使得

$$
2 x y+2 y z+2 z x-x^{2}-y^{2}-z^{2}=1 \text { 或 } 2 \text {. }
$$

事实上, 假设存在, 则有

$$
(2-x-y)^{2}=4 x y-1 \text { 或 } 4 x y-2 \text {. }
$$

左边模 4 余 0,1 右边模 4 余 2,3 , 矛盾! 引理成立.

引理 2 存在无穷个正整数 $d$, 使得方程 $x^{2}-4 d y^{2}=-3$ 有无穷多对正整数解.

事实上, 取 $4 d=k^{2}+3$, 其中 $k$ 为奇数, 易知 $4 d$ 不为完全平方数. 注意到 Pell 方程 $x^{2}-4 d y^{2}=-3$ 有解 $(k, 1)$, 故有无穷多组解. 引理得证.

(i) 先证 $c=\frac{3}{4}$ 时, 原命题成立.

设 $a+b=k, a^{2}=m-\frac{x}{k^{2}}, b^{2}=n-\frac{y}{k^{2}}$, 其中 $k, m, n \in \mathbb{N}^{*}, 0<x, y<k^{2}$. 于是, $\left\{a^{2}\right\}=1-\frac{x}{k^{2}},\left\{b^{2}\right\}=1-\frac{y}{k^{2}}$, 且

$$
\sqrt{m-\frac{x}{k^{2}}}+\sqrt{n-\frac{y}{k^{2}}}=k=a+b<\sqrt{m}+\sqrt{n} .
$$

下证 $\left\{a^{2}\right\}+\left\{b^{2}\right\} \leq 2-\frac{\frac{3}{4}}{(a+b)^{2}}$. 即证 $x+y \geq \frac{3}{4}$.

反证法. 假设 $x+y<\frac{3}{4}$, 则

$$
k \geq \sqrt{m-\frac{x}{k^{2}}}+\sqrt{1-\frac{y}{k^{2}}} \geq \sqrt{m-x}+\sqrt{1-y}>\sqrt{m}
$$

同理 $k>\sqrt{n}$. 故

$$
(\sqrt{m}+\sqrt{n}-k)(\sqrt{m}+\sqrt{n}+k)(k-\sqrt{m}+\sqrt{n})(k+\sqrt{m}-\sqrt{n})>0
$$

即

$$
2 m n+2 m k^{2}+2 n k^{2}-m^{2}-n^{2}-k^{4} \geq 0 \text {. }
$$

结合引理 1 知,

$$
2 m n+2 m k^{2}+2 n k^{2}-m^{2}-n^{2}-k^{4} \geq 3 .
$$

由 $(*)$ 和 $k^{2}>\max \{m, n\}>|m-n|$ 知,

$$
\begin{aligned}
2 m n+2 m k^{2}+2 n k^{2}-\left(m^{2}+n^{2}+k^{4}\right) & =2(x+y)+\frac{2}{k^{2}}(x-y)(n-m)+\frac{(x-y)^{4}}{k^{4}} \\
& <\frac{3}{2}+\frac{\{n-m\}+1}{k^{2}}<3,
\end{aligned}
$$

矛盾.

(ii) 证明 $c \leq \frac{3}{4}$.

取正整数 $d$ 使得引理 2 的方程有无穷多组整数解. 取 $(x, y)$ 为满足引理 2 的正整数解, 且 $x>2 d$. 取

$$
a=\sqrt{d-\frac{u}{y^{2}}}, b=\sqrt{y^{2}+d-x-\frac{v}{y^{2}}}
$$

且满足 $a+b=y \in \mathbb{N}^{*}$.

我们首先来看当 $v \rightarrow 0^{+}$时, $u$ 会接近于什么值, 即解 $u$ 的方程,

$$
\begin{aligned}
& \sqrt{d-\frac{u}{y^{2}}}+\sqrt{y^{2}+d-x}=y \\
\Leftrightarrow & 2 \sqrt{d-\frac{u}{y^{2}}} \sqrt{y^{2}+d-x}=x+\frac{u}{y^{2}}-2 d \\
\Leftrightarrow & 4\left(d-\frac{u}{y^{2}}\right)\left(y^{2}+d-x\right)=\left(x+\frac{u}{y^{2}}-2 d\right)^{2} \\
\Leftrightarrow & 4 y^{2} d-4 u+\frac{2 x u}{y^{2}}=x^{2}+\frac{u^{2}}{y^{4}} \\
\Leftrightarrow & 4 u=3+\frac{2 x u}{y^{2}}-\frac{u^{2}}{y^{4}},
\end{aligned}
$$

再令 $y \rightarrow+\infty$, 我们得到 $u \rightarrow \frac{3}{4}$, 即我们在

$$
1-\frac{u}{y^{2}}+1-\frac{v}{y^{2}} \leq 2-\frac{c}{y^{2}}
$$

中令 $v \rightarrow 0+y \rightarrow \infty$ 且满足引理 2 中的解, 可得 $u \rightarrow \frac{3}{4}$, 从而我们有 $c \leq \frac{3}{4}$.

评注 此题我先发现本质是数论题, 就去想用有理逼近来做, 但未做出. 后来换了一种代数化的思路, 将小数部分设出, 并用利用海伦公式中的恒等式与引理
得到结论. 最后可利用 Pell 方程给出构造.

致谢 作者感谢吴尉迟老师审阅了本文, 并给出了宝贵的意见!

## 参考文献

[1] 冯贝叶. 多项式与无理数 $[\mathrm{M}]$. 哈尔滨工业大学出版社, 2018 年 1 月.

[2] 2018 年 IMO 中国国家集训队教练组. 走向 IMO: 数学奥林匹克试题集锦 (2018) [M]. 上海华东师范大学出版社, 2018.9.

