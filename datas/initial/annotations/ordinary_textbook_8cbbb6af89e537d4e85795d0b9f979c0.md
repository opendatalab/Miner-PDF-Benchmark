# 特征和相关背景的赛题一谈谈整体求和 

吴宇培<br>(天元公学・杭州二中未来科技城学校, 311121)

如果我们做题的时候知道背景, 会比较好做. 解尧平同学曾写过整体求和相关的思想 (见[2]), 本文我们谈一些以特征和为背景的整体求和的题目.

题 1 (2017 清华金秋营) 给定奇素数 $p$ 和正整数 $a$, 试求方程 $x^{2}+y^{2} \equiv a$ $(\bmod p)$ 在模 $p$ 意义下的解的个数.

思路分析 设所求解的个数是 $f_{p}(a)$, 本题有些许背景, 所以我们一边寻找策略, 一边给出解答. 本题与 Gauss 和相关, 这里给出两种策略, 第一种, 我们可以用 Legendre 符号求和来表示所求解的个数:

$$
f_{p}(a)=\sum_{x=0}^{p-1}\left(1+\left(\frac{a-x^{2}}{p}\right)\right)
$$

这是因为, 固定 $x$, 当 $a-x^{2}$ 是平方剩余的时候, 在 $\mathbb{F}_{p}$ 上贡献了两个解 $\pm \sqrt{a-x^{2}}$;当 $p \mid a-x^{2}$ 时, 贡献一个解 0 ; 当 $a-x^{2}$ 不是平方剩余的时候贡献了 0 个解, 所以可以用 $1+\left(\frac{a-x^{2}}{p}\right)$ 求和得到解的个数, 然后我们将 Legendre 符号二项式展开后交换求和号, 本题目前大多数解答都类似这样处理; 第二种, 我们还可以拿单位根轮一圈, 来生成解的个数:

$$
f_{p}(a)=\frac{1}{p} \sum_{0 \leq x, y \leq p-1} \sum_{j=0}^{p-1} \omega^{j\left(x^{2}+y^{2}-a\right)}
$$

其中, $\omega=e^{\frac{2 \pi i}{p}}$ 是 $p$ 次单位根. 该策略是基于

$$
\sum_{j=0}^{p-1} \omega^{j k}= \begin{cases}p, & p \mid k \\ 0, & p \nmid k\end{cases}
$$

因此就算我们不知道 Gauss 和, 也有机会想到这一操作.

修订日期: 2020-06-14.
我们先用第二种策略进行证明.

解 1 我们已经得到

$$
f_{p}(a)=\frac{1}{p} \sum_{0 \leq x, y \leq p-1} \sum_{j=0}^{p-1} \omega^{j\left(x^{2}+y^{2}-a\right)}
$$

考虑

$$
\begin{aligned}
\sum_{0 \leq x, y \leq p-1} \sum_{j=0}^{p-1} \omega^{j\left(x^{2}+y^{2}-a\right)} & =\sum_{j=0}^{p-1} \sum_{0 \leq x, y \leq p-1} \omega^{j\left(x^{2}+y^{2}\right)} \omega^{-a j} \\
& =\sum_{j=0}^{p-1} \omega^{-a j}\left(\sum_{0 \leq x \leq p-1} \omega^{j x^{2}}\right)^{2} \\
& =\sum_{j=1}^{p-1} \omega^{-a j}\left(\sum_{0 \leq x \leq p-1} \omega^{j x^{2}}\right)^{2}+p^{2}
\end{aligned}
$$

设 $g_{p}(j)=\left(\sum_{0 \leq x \leq p-1} \omega^{j x^{2}}\right)^{2}$, 下面我们证明:对于 $1 \leq j \leq p-1$, 我们有 $g_{p}(j)$的值不依赖于 $j$.

当 $\left(\frac{j}{p}\right)=1$ 时, $\left(\frac{j x^{2}}{p}\right)=1(1 \leq x \leq p-1)$, 所以 $\left\{j x^{2}\right\}_{0 \leq x \leq p-1}$ 遍历所有非零的平方剩余两次并取到一次零, 所以

$$
\sum_{0 \leq x \leq p-1} \omega^{j x^{2}}=\sum_{0 \leq x \leq p-1} \omega^{x^{2}}
$$

进而

$$
g_{p}(j)=\left(\sum_{0 \leq x \leq p-1} \omega^{x^{2}}\right)^{2}
$$

当 $\left(\frac{j}{p}\right)=-1$ 时, $\left(\frac{j x^{2}}{p}\right)=-1(1 \leq x \leq p-1),\left\{j x^{2}\right\}_{0 \leq x \leq p-1}$ 遍历所有非平方剩余两次并取到一次零, 所以

$$
\begin{aligned}
\sum_{0 \leq x \leq p-1} \omega^{j x^{2}} & =1+\sum_{1 \leq x \leq p-1} \omega^{j x^{2}} \\
& =1+2 \sum_{1 \leq x \leq p-1} \omega^{x}-\sum_{1 \leq x \leq p-1} \omega^{x^{2}} \\
& =-\sum_{0 \leq x \leq p-1} \omega^{x^{2}}
\end{aligned}
$$

进而

$$
g_{p}(j)=\left(\sum_{0 \leq x \leq p-1} \omega^{x^{2}}\right)^{2}
$$

所以 $g_{p}(j)$ 的值不依赖于 $j(1 \leq j \leq p-1)$, 我们可以设 $g_{p}(j) \equiv g_{p}(1 \leq j \leq p-1)$是只依赖于 $p$ 的量.
于是,

$$
p f_{p}(a)=g_{p} \sum_{j=1}^{p-1} \omega^{-a j}+p^{2}
$$

所以当 $p \nmid a$ 时, $f_{p}(a)=p-\frac{g_{p}}{p}$, 于是 $f_{p}(a)$ 不依赖于 $a$ 、只依赖于 $p$, 所以

$$
f_{p}(a)=\frac{p^{2}-f_{p}(0)}{p-1}
$$

现在我们只要计算 $f_{p}(0)$ 即可(根本不需要处理 $g_{p}$ 的表达式), 显然,

$$
f_{p}(0)= \begin{cases}1, & \left(\frac{-1}{p}\right)=-1 \\ 2 p-1, & \left(\frac{-1}{p}\right)=1\end{cases}
$$

这是因为, 当 $\left(\frac{-1}{p}\right)=1$ 时, $(x-i y)(x+i y) \equiv 0(\bmod p)$ 的非零解可以按 $x+i y \equiv 0(\bmod p)$ 或 $x-i y \equiv 0(\bmod p)$ 唯一确定, 其中, $i$ 按 $i^{2} \equiv-1(\bmod p)$理解.

熟知 -1 是模 $p$ 的平方剩余当且仅当 $p \equiv 1(\bmod 4)$, 所以我们得到:

当 $p \mid a$ 时,

$$
f_{p}(a)= \begin{cases}1, & p \equiv-1 \quad(\bmod 4) \\ 2 p-1, & p \equiv 1 \quad(\bmod 4)\end{cases}
$$

当 $p \nmid a$ 时,

$$
f_{p}(a)= \begin{cases}p+1, & p \equiv-1 \quad(\bmod 4) \\ p-1, & p \equiv 1 \quad(\bmod 4)\end{cases}
$$

允许笔者再唠四一下, $g_{p}$ 是可以直接求的. 首先, 我们已经证明: 若 $p \nmid j$, 则

$$
\sum_{0 \leq x \leq p-1} \omega^{j x^{2}}=\left(\frac{j}{p}\right) \sum_{0 \leq x \leq p-1} \omega^{x^{2}}
$$

那么, 我们这样处理

$$
\begin{aligned}
g_{p} & =\left(\frac{-1}{p}\right) \sum_{0 \leq x \leq p-1} \omega^{x^{2}} \sum_{0 \leq y \leq p-1} \omega^{-y^{2}} \\
& =\left(\frac{-1}{p}\right) \sum_{0 \leq x, y \leq p-1} \omega^{x^{2}-y^{2}} \\
& =\left(\frac{-1}{p}\right) \sum_{0 \leq u, v \leq p-1} \omega^{u v}=\left(\frac{-1}{p}\right) p .
\end{aligned}
$$

现在, 我们换第一种策略解决此题.
解 2 我们已经得到

$$
f_{p}(a)=\sum_{x=0}^{p-1}\left(1+\left(\frac{a-x^{2}}{p}\right)\right)
$$

设 $s_{p}=\sum_{0 \leq x \leq p-1}\left(\frac{a-x^{2}}{p}\right)$, 熟知:

$$
\sum_{x=1}^{p-1} x^{i} \equiv \sum_{j=1}^{p-1}\left(g^{j}\right)^{i}=\frac{g^{i}\left(g^{i(p-1)}-1\right)}{g^{i}-1} \equiv\left\{\begin{array}{ll}
0 \quad(\bmod p), & \text { 若 } p-1 \nmid i \\
-1 \quad(\bmod p), & \text { 若 } p-1 \mid i
\end{array},\right.
$$

则当 $p \nmid a$ 时,

$$
\begin{aligned}
\sum_{0 \leq x \leq p-1}\left(\frac{a-x^{2}}{p}\right) & \equiv \sum_{0 \leq x \leq p-1}\left(a-x^{2}\right)^{\frac{p-1}{2}}(\bmod p) \\
& =a^{\frac{p-1}{2}}+\sum_{1 \leq x \leq p-1} \sum_{k=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{k} x^{2 k}(-1)^{k} a^{\frac{p-1}{2}-k} \\
& =a^{\frac{p-1}{2}}+\sum_{k=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{k}(-1)^{k} a^{\frac{p-1}{2}-k} \sum_{1 \leq x \leq p-1} x^{2 k} \\
& \equiv a^{\frac{p-1}{2}}-\sum_{0 \leq k \leq \frac{p-1}{2}} C_{\frac{p-1}{2}}^{k}(-1)^{k} a^{\frac{p-1}{2}-k} \\
& =a^{\frac{p-1}{2}}-\left(a^{\frac{p-1}{2}}+(-1)^{\frac{p-1}{2}}\right) \\
& =(-1)^{\frac{p+1}{2}}(\bmod p)
\end{aligned}
$$

由于 $\left|s_{p}\right| \leq p$, 所以 $s_{p}=1,-1, p-1,1-p$. 若 $\left|s_{p}\right|=p-1 \equiv 0(\bmod 2)$, 但是 $\left|s_{p}\right| \equiv s_{p} \equiv p \equiv 1(\bmod 2)$, 矛盾, 所以, $s_{p}=(-1)^{\frac{p+1}{2}}$.

故当 $p \nmid a$ 时,

$$
f_{p}(a)=\sum_{x=0}^{p-1}\left(1+\left(\frac{a-x^{2}}{p}\right)\right)=p+(-1)^{\frac{p+1}{2}}
$$

当 $p \mid a$ 时,

$$
f_{p}(a)=1+\sum_{x=1}^{p-1}\left(1+\left(\frac{-x^{2}}{p}\right)\right)=p+\sum_{x=1}^{p-1}\left(\frac{-1}{p}\right)=p+(p-1)(-1)^{\frac{p-1}{2}} .
$$

本题显然与代数数论相关, 学过的同学很容易处理, 同年国家集训队测试中也考到了类似的:

题 2 (2017 中国国家集训队测试四) 试求同时满足下列三个条件的有序数组 $\left(x_{1}, x_{2}, \cdots, x_{100}\right)$ 的个数:

(1) $x_{1}, x_{2}, \cdots, x_{100} \in\{1,2, \cdots, 2017\}$;

(2) $2017 \mid x_{1}+x_{2}+\cdots+x_{100}$;

(3) $2017 \mid x_{1}^{2}+x_{2}^{2}+\cdots+x_{100}^{2}$.

解 设 $p=2017$ 是素数, 所求数组的个数设为 $f(p)$, 令

$$
\omega=e^{\frac{2 \pi i}{p}}, g_{p}(j)=\left(\sum_{0 \leq x \leq p-1} \omega^{j x^{2}}\right)^{2}
$$

以下 $\omega$ 的上标皆按模 $p$ 理解, 分数按模 $p$ 的逆元(数论倒数)理解. 于是

$$
\begin{aligned}
p^{2} f(p) & =\sum_{0 \leq x_{1}, x_{2}, \cdots, x_{100} \leq p-1} \sum_{0 \leq a, b \leq p-1} \omega^{a\left(x_{1}^{2}+x_{2}^{2}+\cdots+x_{100}^{2}\right)+b\left(x_{1}+x_{2}+\cdots+x_{100}\right)} \\
& =\sum_{0 \leq a, b \leq p-1} \omega^{a\left(x_{1}^{2}+x_{2}^{2}+\cdots+x_{100}^{2}\right)+b\left(x_{1}+x_{2}+\cdots+x_{100}, \cdots, x_{100} \leq p-1\right.} \\
& =\sum_{0 \leq a, b \leq p-1}\left(\sum_{0 \leq x \leq p-1} \omega^{a x^{2}+b x}\right)^{100} \\
& =\sum_{0 \leq b \leq p-1}\left(\sum_{0 \leq x \leq p-1} \omega^{b x}\right)^{100}+\sum_{0 \leq b \leq p-1} \sum_{1 \leq a \leq p-1} \omega^{\frac{-25 b^{2}}{a}}\left(\sum_{0 \leq x \leq p-1} \omega^{a\left(x+\frac{b}{2 a}\right)^{2}}\right)^{100}
\end{aligned}
$$

由于上标按照模 $p$ 理解, 分数按数论倒数理解, 根据题 1 的第二种策略: 对于 $1 \leq j \leq p-1$, 有

$$
g_{p}(j)=\left(\sum_{0 \leq x \leq p-1} \omega^{x^{2}}\right)^{2}=g_{p}=(-1)^{\frac{p-1}{2}} p
$$

是只依赖 $p$ 不依赖 $j$ 的量, 所以

$$
\begin{aligned}
p^{2} f(p) & =p^{100}+\sum_{0 \leq b \leq p-1} \sum_{1 \leq a \leq p-1} \omega^{\frac{-25 b^{2}}{a}}\left(\sum_{0 \leq x \leq p-1} \omega^{a x^{2}}\right)^{100} \\
& =p^{100}+g_{p}^{50} \sum_{0 \leq b \leq p-1} \sum_{1 \leq a \leq p-1} \omega^{\frac{-25 b^{2}}{a}} .
\end{aligned}
$$

当 $a$ 遍历模 $p$ 缩系时, $a^{-1}$ 也是如此的, 由于当 $1 \leq b \leq p-1$ 时, $p \nmid 25 b^{2}$, 所以,

$$
\begin{aligned}
\sum_{0 \leq b \leq p-1} \sum_{1 \leq a \leq p-1} \omega^{\frac{-25 b^{2}}{a}} & =p-1+\sum_{1 \leq b \leq p-1} \sum_{1 \leq a \leq p-1} \omega^{-25 b^{2} a} \\
& =p-1+\sum_{1 \leq b \leq p-1}-1 \\
& =0,
\end{aligned}
$$

故 $f(p)=p^{98}=2017^{98}$.

本题和 2017 清华金秋营的那道数论题可以说几乎约等于是同一题, 都有明
显的特征和相关的背景, 本题也可以配方之后对 Legendre 符号整体求和, 这想法略有点让人望而生畏.

用单位根进行计数的想法非常值得尝试.

题 3 (2007 IMO Shortlists C3) 试求所有正整数 $n$, 使得 $S=\{1,2, \ldots, n\}$中的元素可以被染红蓝两种颜色, $S \times S \times S$ 恰好包含 2007 个三元数组 $(x, y, z)$,满足下面两个条件:

(i) $x, y, z$ 同色, (ii) $n \mid x+y+z$.

解 设红色的数构成集合 $R$, 蓝色的数构成集合 $B, \omega=e^{\frac{2 \pi i}{n}}$,于是,

$$
\begin{aligned}
2007 n & =\sum_{j=0}^{n-1} \sum_{x, y, z \in R} \omega^{j(x+y+z)}+\sum_{j=0}^{n-1} \sum_{x, y, z \in B} \omega^{j(x+y+z)} \\
& =\sum_{j=0}^{n-1}\left[\left(\sum_{x \in R} \omega^{j x}\right)^{3}+\left(\sum_{x \in B} \omega^{j x}\right)^{3}\right] \\
& =|R|^{3}+|B|^{3}+\sum_{j=1}^{n-1}\left(\sum_{x=1}^{n} \omega^{j x}\right) f_{j}(R, B) \\
& =|R|^{3}+|B|^{3},
\end{aligned}
$$

其中，

$$
f_{j}(R, B)=\left(\sum_{x \in R} \omega^{j x}\right)^{2}-\left(\sum_{x \in R} \omega^{j x}\right)\left(\sum_{x \in B} \omega^{j x}\right)+\left(\sum_{x \in B} \omega^{j x}\right)^{2} .
$$

由于 $|R|+|B|=n$, 所以 $2007=r^{2}-r b+b^{2}$, 其中 $r=|R|, b=|B|$. 易证 $3 \mid r, b$, 设 $r=3 x, b=3 y$, 解得 $(x, y)=(17,11),(11,17),(17,6),(6,17)$, 所以 $n=84,69$.

我们处理题 2 和题 3 的思想是一样的, 用单位根轮一圈写出计数函数的想法值得考虑, 当然有的情况并不好用, 比如说:固定正整数 $k, r, n$, 让我们计算 $x_{1} x_{2} \cdots x_{k} \equiv r(\bmod n)$ 在模 $n$ 意义下的解的个数 $(2020$ 土耳其 TST 的最后一题), 我们很难描述 $x_{1} \cdots x_{k-1}$ 什么时候被 $n$ 整除, 给我们用单位根整体求和带来了很大的难度(有可能可行, 只是笔者不会算).

对于数论中按某种性质整体求和的问题我们再举两例:

题 4 (2012 IMO Shortlists N8 ${ }^{[4]}$ ) 证明:对每个素数 $p>100$ 和每个整数 $r$, 存在整数 $a, b$, 使得 $p \mid a^{2}+b^{5}-r$.

本题显然是以Jacobi和为背景的. 下面给出两种求解方法.
解 $15 \nmid p-1$ 时, $b^{5}$ 遍历模 $p$ 完系(上标跑遍模 $p-1$ 完系). 于是, 我们处理素数 $p=10 k+1$ 的情形. 若结论不成立, 存在 $r$, 使得对任意整数 $a, b$, 都有 $p \nmid a^{2}+b^{5}-r$, 则

$$
\left(\begin{array}{c}
r \\
p
\end{array}\right)=\left(\frac{r-b^{5}}{p}\right)=-1,
$$

其中, $\left(\frac{a}{p}\right)$ 是 Legendre 符号. 注意到 $b$ 的任意性, 我们对 $\left(\frac{r-b^{5}}{p}\right)=-1$ 按 $b$ 求和:设 $g$ 是模 $p$ 原根, 我们熟知

![](https://cdn.mathpix.com/cropped/2024_02_26_59d31c64028603108496g-07.jpg?height=198&width=966&top_left_y=689&top_left_x=545)

一方面

$$
\begin{aligned}
\sum_{b=0}^{p-1}\left(r-b^{5}\right)^{\frac{p-1}{2}} & =-1+\sum_{b=1}^{p-1} \sum_{l=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{l}(-1)^{l} b^{5 l} r^{\frac{p-1}{2}-l} \\
& =-1+\sum_{l=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{l}(-1)^{l} r^{\frac{p-1}{2}-l} \sum_{b=1}^{p-1} b^{5 l} \\
& \equiv-\sum_{\substack{\left.0 \leq l \leq \frac{p-1}{2} \\
p-1 \right\rvert\, 5 l}} C_{\frac{p-1}{2}}^{l}(-1)^{l} r^{\frac{p-1}{2}-l}(\bmod p) \\
& =-\left(C_{5 k}^{2 k} r^{3 k}+C_{5 k}^{4 k} r^{k}\right)
\end{aligned}
$$

另一方面, 由于 $\left(\frac{r-b^{5}}{p}\right)=-1$ 对 $0 \leq b \leq p-1$ 都成立, 所以

$$
\sum_{b=0}^{p-1}\left(r-b^{5}\right)^{\frac{p-1}{2}} \equiv 0 \quad(\bmod p)
$$

我们得到 $C_{5 k}^{2 k} r^{2 k}+C_{5 k}^{4 k} \equiv 0(\bmod p)$. 此时, 表达式中有个 $r$ 不太好处理, 我们要再找一个方程, 考虑对 $b^{5}\left(r-b^{5}\right)^{\frac{p-1}{2}} \equiv-b^{5}(\bmod p)$ 按 $b$ 求和.

一方面

$$
\begin{aligned}
\sum_{b=0}^{p-1} b^{5}\left(r-b^{5}\right)^{\frac{p-1}{2}} & =\sum_{b=1}^{p-1} \sum_{l=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{l}(-1)^{l} b^{5(l+1)} r^{\frac{p-1}{2}-l} \\
& =-1+\sum_{l=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{l}(-1)^{l} r^{\frac{p-1}{2}-l} \sum_{b=1}^{p-1} b^{5(l+1)} \\
& \equiv-\sum_{\substack{\left.0 \leq l \leq \frac{p-1}{2} \\
p-1 \right\rvert\, 5(l+1)}} C_{\frac{p-1}{2}}^{l}(-1)^{l} r^{\frac{p-1}{2}-l}(\bmod p) \\
& =C_{5 k}^{2 k-1} r^{3 k+1}+C_{5 k}^{4 k-1} r^{k+1}
\end{aligned}
$$

另一方面, 由于

$$
\sum_{b=0}^{p-1} b^{5}\left(r-b^{5}\right)^{\frac{p-1}{2}} \equiv-\sum_{b=0}^{p-1} b^{5} \equiv 0 \quad(\bmod p)
$$

所以 $C_{5 k}^{2 k-1} r^{2 k}+C_{5 k}^{4 k-1} \equiv 0(\bmod p)$.

现在我们可以消去 $r$, 得到:

$$
C_{5 k}^{4 k-1}\left(C_{5 k}^{2 k-1}\right)^{-1} \equiv C_{5 k}^{k}\left(C_{5 k}^{2 k}\right)^{-1} \quad(\bmod p)
$$

化简得 $p \mid 2 k(5 k+1)$, 所以 $10 k+1 \mid 2 k$ 或 $10 k+1 \mid 5 k+1$,矛盾.

若不曾学过代数数论, 解法 2 可能不是朝夕之间可以搞懂的, 所以一时不明白也不必在意. 读者可以参考川大的数论讲义下册 $\mathbb{F}_{p}$ 上的不定方程和 Jacobi 和中的内容. 我们先介绍一些相关知识, 读者也可以直接翻阅川大的数论讲义 (见 [1]).

定义 1 对于素数 $p, \mathbb{F}_{p}=\{0,1,2, \cdots, p-1\}$, 定义一个映射 $\chi: \mathbb{F}_{p}^{*} \rightarrow \mathbb{C}$,对于任意的 $x, y \in \mathbb{F}_{p}^{*}$, 都有 $\chi(x y)=\chi(x) \chi(y), \chi(1) \neq 0$. 我们称 $\chi$ 是 $\mathbb{F}_{p}$ 上的一个特征. 定义一个平凡的特征 $\chi_{0}: \chi_{0}(x)=1\left(a \in \mathbb{F}_{p}^{*}\right)$. ( $\mathbb{F}_{p}$ 的所有特征构成的集合 $T$ 是 $p-1$ 阶乘法循环群, 定义 $T$ 中的乘法如下: $\lambda \chi(a)=\lambda(a) \chi(a), a \in \mathbb{F}_{p}^{*}$. $)$

注 可求得 $\chi(1)=1$, 对于任意的 $a \in \mathbb{F}_{p}^{*}, \chi^{p-1}(a)=\chi\left(a^{p-1}\right)=1$, 所以 $\chi(a)$是 $p-1$ 次单位根.

定义 2 用 $|\chi|$ 表示最小的正整数 $k$, 使得 $\chi^{k}=\chi_{0}$, 即为 $\chi$ 在群 $T$ 中的阶, $\chi$ 是一个 $k$ 阶特征.

定义 3 用 $N(f(x, y)=0)$ 表示不定方程 $f(x, y)=0$ 在 $\mathbb{F}_{p}$ 上的解的个数.

定义 4 设 $\chi, \lambda$ 是 $\mathbb{F}_{p}$ 上的两个特征, 令

$$
J(\chi, \lambda)=\sum_{\substack{a+b=1 \\ a, b \in \mathbb{F}_{p}}} \chi(a) \lambda(b)
$$

$J(\chi, \lambda)$ 称作 $\mathbb{F}_{p}$ 上的 Jacobi 和.

例 1 给定素数 $p$ 和正整数 $a$ 及 $k \mid p-1$, 我们用 $N\left(x^{k}=a\right)$ 表示 $x^{k}=a$在 $\mathbb{F}_{p}$ 上的解的个数, 设 $\chi$ 是 $\mathbb{F}_{p}$ 上的 $k$ 阶特征, 那么,

$$
N\left(x^{k}=a\right)=\sum_{\lambda \text { 是 } k \text { 阶特征 }} \lambda(a)=\sum_{j=0}^{k-1} \chi^{j}(a) \text {. }
$$

例 $2 N\left(u^{2}+v^{5}=1\right)$ 与 Jacobi 和的关系: 设 $\chi$ 是 $\mathbb{F}_{p}$ 上的 2 阶特征, $\lambda$ 是一
个 5 阶特征, 则

$$
\begin{aligned}
N\left(u^{2}+v^{5}=1\right) & =\sum_{\substack{x+y=1 \\
x, y \in \mathbb{F}_{p}}} N\left(u^{2}=x\right) N\left(v^{5}=y\right)=\sum_{\substack{x+y=1 \\
x, y \in \mathbb{F}_{p}}} \sum_{i=0}^{1} \sum_{j=0}^{4} \chi^{i}(x) \lambda^{j}(y) \\
& =\sum_{i=0}^{1} \sum_{j=0}^{4} \sum_{\substack{x+y=1 \\
x, y \in \mathbb{F}_{p}}} \chi^{i}(x) \lambda^{j}(y)=\sum_{i=0}^{1} \sum_{j=0}^{4} J\left(\chi^{i}, \lambda^{j}\right) .
\end{aligned}
$$

性质 设 $\chi, \lambda$ 是 $\mathbb{F}_{p}$ 上的两个特征, 且 $\chi, \lambda \neq \chi_{0}$, 则

(1). $J\left(\chi_{0}, \chi_{0}\right)=p$;

(2). $J\left(\chi_{0}, \chi\right)=0$;

(3). 若 $\chi, \lambda, \chi \lambda \neq \chi_{0}$, 则 $|J(\chi, \lambda)|=\sqrt{p}$.

下面开始解决这一问题.

解 2 本题只要做 $5 \mid p-1$ 的情况, 这是因为 $\operatorname{gcd}(5, p-1)=1$ 时, $b^{5}$ 可以遍历模 $p$ 完系(上标可以跑遍 $p-1$ 的完系). 设 $\chi$ 是 $\mathbb{F}_{p}$ 上的 2 阶特征, $\lambda$ 是一个 5 阶特征, 则

$$
\begin{aligned}
N\left(u^{2}+v^{5}=r\right) & =\sum_{\substack{x+y=r \\
x, y \in \mathbb{F}_{p}}} N\left(u^{2}=x\right) N\left(v^{5}=y\right) \\
& =\sum_{\substack{x+y=r \\
x, y \in \mathbb{F}_{p}}} \sum_{i=0}^{1} \sum_{j=0}^{4} \chi^{i}(x) \lambda^{j}(y) \\
& =\sum_{i=0}^{1} \sum_{j=0}^{4} \sum_{\substack{x+y=1 \\
x, y \in \mathbb{F}_{p}}} \chi^{i}(r) \lambda^{j}(r) \chi^{i}(x) \lambda^{j}(y) \\
& =\sum_{i=0}^{1} \sum_{j=0}^{4} \chi^{i}(r) \lambda^{j}(r) J\left(\chi^{i}, \lambda^{j}\right) \\
& =J\left(\chi_{0}, \chi_{0}\right)+\sum_{j=1}^{4} \chi(r) \lambda^{j}(r) J\left(\chi, \lambda^{j}\right) \\
& \geq p-\sum_{j=1}^{4}\left|\chi \lambda^{j}(r)\right| \cdot\left|J\left(\chi, \lambda^{j}\right)\right| \\
& =p-4 \sqrt{p}>0 .
\end{aligned}
$$

结论成立.

题 $5(2015$ 清华金秋营) 设素数 $p \equiv 1(\bmod 4), p>5$. 我们称 $a$ 是模 $p$ 的平方剩余, 若存在正整数 $x$, 使得 $x^{2} \equiv a(\bmod p)$. 证明: 对于给定的正整数 $a$, 都存在整数 $b, c$, 使得 $a=b+c$ 且 $b, c$ 都不是平方剩余.
解 1 本题其实非常容易, 只要说明存在 $b, c$, 使得 $a \equiv b+c(\bmod p)$ 且 $\left(\frac{b}{p}\right)=\left(\frac{c}{p}\right)=-1$. 我们补充Legendre符号的定义, 约定 $\left(\frac{0}{p}\right)=1$. 现在, 我们用反证法并整体求和(类似题 1 的第一种策略): 假设对任意的 $1 \leq b \leq p-1$, $\left(\frac{b}{p}\right)=-1$, 都有 $\left(\frac{a-b}{p}\right)=1$, 我们对 $(a-b)^{\frac{p-1}{2}}$ 整体求和, 设 $g$ 是模 $p$ 原根, $n$ 是偶数, 我们熟知:

$$
\sum_{j=1}^{\frac{p-1}{2}}\left(g^{n}\right)^{j} \equiv\left\{\begin{array}{ll}
0 \quad(\bmod p), & \text { 若 } p-1 \nmid n \\
-\frac{1}{2} \quad(\bmod p), & \text { 若 } p-1 \mid n
\end{array} ，\right.
$$

则

$$
\begin{aligned}
\sum_{\left(\frac{b}{p}\right)=-1}(a-b)^{\frac{p-1}{2}} & \equiv \sum_{j=1}^{\frac{p-1}{2}}\left(a-g^{2 j-1}\right)^{\frac{p-1}{2}} \quad(\bmod p) \\
& =\sum_{j=1}^{\frac{p-1}{2}} \sum_{k=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{k}\left(g^{2 j-1}\right)^{k}(-1)^{k} a^{\frac{p-1}{2}-k} \\
& =\sum_{k=0}^{\frac{p-1}{2}} C_{\frac{p-1}{2}}^{k} g^{-k}(-1)^{k} a^{\frac{p-1}{2}-k} \sum_{j=1}^{\frac{p-1}{2}}\left(g^{2 k}\right)^{j} \\
& \equiv-\frac{1}{2} \sum_{0 \leq k \leq \frac{p-1}{2}} C_{\frac{p-1}{2}}^{k} g^{-k}(-1)^{k} a^{\frac{p-1}{2}-k} \quad(\bmod p) \\
& =\frac{1}{2}\left(1-a^{\frac{p-1}{2}}\right)
\end{aligned}
$$

我们要注意 $a$ 是非平方剩余时, $b$ 在遍历非平方剩余时候会取到 $a$,但我们约定了 $\left(\frac{0}{p}\right)=1$, 所以我们分两种情况说明:

(1) 若 $a$ 是平方剩余或零, 我们有

$$
\frac{p-1}{2} \equiv \sum_{\left(\frac{b}{p}\right)=-1}(a-b)^{\frac{p-1}{2}} \equiv \frac{1}{2}\left(1-a^{\frac{p-1}{2}}\right) \equiv 0, \frac{1}{2} \quad(\bmod p)
$$

所以, $-1 \equiv 1,0(\bmod p)$, 进而 $p \mid 2,1$, 矛盾.

(2) 若 $a$ 是非平方剩余, 则 $\left(\frac{a}{p}\right)=-1$, 我们有

$$
\frac{p-1}{2}-1 \equiv \sum_{\left(\frac{b}{p}\right)=-1}(a-b)^{\frac{p-1}{2}} \equiv \frac{1}{2}\left(1-a^{\frac{p-1}{2}}\right) \equiv 1 \quad(\bmod p),
$$

所以 $\frac{-3}{2} \equiv 1(\bmod p)$, 进而 $p \mid 5$, 矛盾 $(p>5)$.

所以假设错误, 一定存在两个非平方剩余 $b, c$, 使得 $b+c \equiv a(\bmod p)$.

笔者认为这个方法是套路的, 值得学会的.

解 2 本题可以直接构造, 相比直接整体求和而言这样考虑可能比较烧脑.
当 $a$ 不是模 $p(>5)$ 的平方剩余时, 在 $\mathbb{F}_{p}$ 上有

$$
a=\left(\frac{3}{5}\right)^{2} a+\left(\frac{4}{5}\right)^{2} a
$$

结论成立.

当 $a$ 是平方剩余且 $p \nmid a$ 时, 考虑这样的 $x: x$ 是非平方剩余, 但 $1,2, \cdots, x-$ 1 都是平方剩余即可. 设 $x-1 \equiv y^{2}(\bmod p), a \equiv(k x)^{2}(\bmod p)$, 注意到

$$
a \equiv(k x)^{2}=x k^{2}\left(y^{2}+1\right)=x(k y)^{2}+x k^{2},
$$

取 $b \equiv x(k y)^{2}(\bmod p), c \equiv x k^{2}(\bmod p)$ 即可.

当 $p \mid a$ 时, 由于 $p \equiv 1(\bmod 4),\left(\frac{-1}{p}\right)=1$, 设 $x^{2} \equiv-1(\bmod 4)$, 取 $y$ 是非平方剩余, 则

$$
0 \equiv y+y x^{2} \quad(\bmod p)
$$

所以结论成立.

这一做法看似简单, 但思考难度上并没有整体求和简单.

学科营有时候会出现一些有背景的题, 2017 年北大夏令营考过: 设 $p$ 是素数, 证明:对任意的正数 $a$, 同余方程 $x^{2}+y^{3}-a \equiv 0(\bmod p)$ 都有解. Erdös 与朋友有一个非常漂亮的结果 (EGZ 定理): 任意 $2 n-1$ 个整数中一定能找到 $n$ 个数的和被 $n$ 整除. 用整体求和的思想进行证明相信不再困难.

读者可以学习一下文献 [2].

致谢 感谢华东师范大学敟振华教授和罗振华老师仔细审阅本文并提出宝贵的修改建议.

## 参考文献

[1] 柯召, 孙琦, 数论讲义下册(第二版) [M], 高等教育出版社.

[2] 解尧平, 数论问题中的整合思想 $[\mathrm{J}]$, 数学新星网, 学生专栏, 2018.08.26.

[3] https://artofproblemsolving. com/community/c6h1408832p7904039.

[4] https://artofproblemsolving. com/community/c6h545767p3156853.

