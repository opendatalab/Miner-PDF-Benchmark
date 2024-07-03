# 一类常见多项式数论结构的研究 

侯宇轩<br>(北京一零一中学, 100091)<br>指导教师: 李佳

在数学竞赛中相当多的数论问题涉及到形如 $\frac{x^{2 r+1}+1}{x+1}$ 的结构, 比如下面这个经典的问题:

问题 证明: 关于 $(x, y)$ 的方程 $y^{5}+1=2 x^{2}$ 除了 $(1,1)$ 外的正整数解 $\left(x_{0}, y_{0}\right)$ 满足 $5 \mid x_{0}$.

其核心难点是证明 $x>1$ 时 $\frac{x^{5}+1}{x+1}$ 不是完全平方数. 通常采用的方法是将 $4\left(\frac{x^{5}+1}{x+1}\right)$ 夹在两相邻完全平方数之内. 但这种方法当 $\frac{x^{5}+1}{x+1}$ 式分子中的 $x$ 幕次变为较大的奇数时很难证明它不是完全平方数.

笔者经过一定的研究证明了 $\frac{x^{2 r+1}+1}{x+1}$ 不是完全平方数在 $r$ 较大时依然成立,即为下面的定理.

定理 $x>1, x, r$ 为正整数, 则 $\frac{x^{2 r+1}+1}{x+1}$ 不是完全平方数.

我们为了证明该定理先证明几个引理.

引理 1 方程 $(a+1) x^{2}-a y^{2}=1$ 的所有解具有如下形式:

$$
\left\{\begin{array}{l}
x=\frac{(\sqrt{a+1}+\sqrt{a})^{2 n+1}+(\sqrt{a+1}-\sqrt{a})^{2 n+1}}{2 \sqrt{a+1}} \\
y=\frac{(\sqrt{a+1}+\sqrt{a})^{2 n+1}-(\sqrt{a+1}-\sqrt{a})^{2 n+1}}{2 \sqrt{a}}
\end{array},\right.
$$

其中 $n \in \mathbb{N}, a \geq 1, a \in \mathbb{Z}$.

证明 考虑方程 $(a+1) x^{2}-a y^{2}=1$, 易知该方程的解满足 $y \geq x$.

设:

$$
\left\{\begin{array}{l}
x+y=u \\
y-x=v
\end{array}, \quad u, v \in \mathbb{Z}_{\geq 0}, \quad\left\{\begin{array}{l}
x=\frac{u-v}{2} \\
y=\frac{u+v}{2}
\end{array}\right.\right.
$$[^0]所以,

$$
\begin{aligned}
& (a+1)\left(\frac{u+v}{2}\right)^{2}-a\left(\frac{u-v}{2}\right)^{2}=1 \\
& \Leftrightarrow u^{2}+v^{2}-(4 a+2) \cdot u \cdot v=4,(u, v \in \mathbb{N})
\end{aligned}
$$

我们证明 $u, v$ 是数列 $\left\{a_{n}\right\}$ 相邻两项.

$a_{n}$ 这样定义:

$$
a_{0}=0, a_{1}=2, a_{2}=8 a+4, \cdots, a_{n+2}=(4 a+2) \cdot a_{n+1}-a_{n} .
$$

先从 $(*)$ 式推导引理 1 : 易知 $a_{n}$ 的通项公式为

$$
a_{n}=\frac{\left(2 a+1+\sqrt{4 a^{2}+4 a}\right)^{n}-\left(2 a+1-\sqrt{4 a^{2}+4 a}\right)^{n}}{\sqrt{4 a^{2}+4 a}},
$$

而 $a_{n}$ 相邻两项之差的一半具有 $\frac{(\sqrt{a+1}+\sqrt{a})^{2 n+1}+(\sqrt{a+1}-\sqrt{a})^{2 n+1}}{2 \sqrt{a+1}}$ 的形式, $a_{n}$ 相邻两项之和的一半具有 $\frac{(\sqrt{a+1}+\sqrt{a})^{2 n+1}-(\sqrt{a+1}-\sqrt{a})^{2 n+1}}{2 \sqrt{a}}$ 的形式. 于是证明了 $(*)$ 式也就证明了引理 1.

下面开始证明 $(*)$ 式:

对于方程 $u^{2}+v^{2}-(4 a+2) \cdot u \cdot v=4$, 我们先证 $(1, t)$ 不是解. 代入得 $t^{2}-(4 a+2) \cdot t-3=0$, 其判别式 $\Delta=(4 a+2)^{2}+12$.

由于 $a \geq 1,(4 a+2)^{2}<(4 a+2)^{2}+12<(4 a+3)^{2}$, 所以 $t$ 无整数解, 证毕.

再证原来的 $(*)$, 易知每组解 $(s, r)$ 中 $s \neq r$. 我们对 $(u, v)$ 中较大的一项归纳证明.

我们对 $n$ 归纳证明命题: 若存在解 $(u, v)$ 使得 $u, v \leq n$, 则 $u, v$ 为数列 $a_{n}$中相邻两项.

使用第二数学归纳法, 下面开始归纳:

$n=2$ 是平凡的.

考虑对于任意 $u, v$ 均小于等于 $k_{0}\left(k_{0} \geq 2\right)$ 时成立: $u, v$ 为 $\left\{a_{n}\right\}$ 中相邻项,那么, 考虑对于 $u, v \leq k_{0}+1$ 时, 不妨设 $u>v($ 显然 $u \neq v)$.

若 $u=k_{0}+1$, 考虑关于 $x$ 的二次方程

$$
x^{2}-(4 a+2) \cdot v \cdot x+v^{2}-4=0,
$$

其有一根为 $u$, 另一根为 $u^{\prime}$, 由韦达定理, $u^{\prime}$ 满足 $u^{\prime}=(4 a+2) \cdot v-u$, 所以 $u^{\prime} \in \mathbb{Z}, u^{\prime}=\frac{v^{2}-4}{u} \geq 0(v \neq 0, v \neq 1$, 注: $v \neq 0$, 因为 $v=0$ 时 $u=2$, 而之前规定了 $\left.u=k_{0}+1 \geq 3\right)$.

所以, $u^{\prime} \in \mathbb{Z}_{\geq 0}$, 且 $u^{\prime}=\frac{v^{2}-4}{u}<v$.
由于 $v, u^{\prime} \leq k_{0}$, 由归纳假设知存在 $r$, 使得 $v=a_{r}, u^{\prime}=a_{r-1}, u=$ $(4 a+2) \cdot a_{r}-a_{r-1}=a_{r+1}$.

若 $u \neq k_{0}+1$, 由归纳假设成立.

综上, 引理 1 证毕.

回到待证明的定理, 考虑方程

$$
\frac{x^{2 r+1}+1}{x+1}=u^{2} \Rightarrow(x+1) \cdot u^{2}-(x) \cdot\left(x^{r}\right)^{2}=1 \text {. }
$$

所以由引理 1 我们知道存在 $n \in \mathbb{N}$,

$$
x^{r}=\frac{(\sqrt{x+1}+\sqrt{x})^{2 n+1}+(\sqrt{x+1}-\sqrt{x})^{2 n+1}}{2 \sqrt{x}} .
$$

我们需要证明 $(\triangle)$ 不可能有 $x=1$ 以外的解 $(x, r, n)(r \geq 1, n \geq 1)$, 这也就证明了该定理.

先证一个小结论: $\frac{(\sqrt{x+1}+\sqrt{x})^{2 n+1}-(\sqrt{x+1}-\sqrt{x})^{2 n+1}}{2 \sqrt{x}}$ 为奇数.

考虑:

$$
b_{k}=\frac{(\sqrt{x+1}+\sqrt{x})^{2 k+1}-(\sqrt{x+1}-\sqrt{x})^{2 k+1}}{2 \sqrt{x}}, b_{0}=1, b_{1}=4 x+3
$$

易知有递推公式: $b_{n+2}=(4 a+2) b_{n+1}-b_{n}$. 两边 $\bmod 2$, 知 $b_{i+2} \equiv b_{i}(\bmod 2)$, 又 $2 \nmid b_{2}, 2 \nmid b_{1}$, 证毕.

从而, 如果 $(\triangle)$ 有非平凡解 $(x, r, n)$, 那么 $x$ 为奇数. 我们仅考虑 $x$ 为奇数的情况.

我们再证明几个引理, 内容如下:

引理 $\mathbf{2}$ 对于奇质数 $p$, 且 $p \mid x$, 则有

$$
p\left|\frac{(\sqrt{x+1}+\sqrt{x})^{2 n+1}-(\sqrt{x+1}-\sqrt{x})^{2 n+1}}{2 \sqrt{x}} \Leftrightarrow p\right| 2 n+1 .
$$

证明 用二项式定理展开得到

$$
\begin{aligned}
& \frac{(\sqrt{x+1}+\sqrt{x})^{2 n+1}-(\sqrt{x+1}-\sqrt{x})^{2 n+1}}{2 \sqrt{x}} \\
& \quad=x^{n}+x^{n-1} \cdot \mathrm{C}_{2 n+1}^{2}(x+1)+\cdots+\mathrm{C}_{2 n+1}^{2 n}(x+1)^{n} .
\end{aligned}
$$

又 $p \mid x$, 所以

$$
\begin{aligned}
p \left\lvert\, \frac{(\sqrt{x+1}+\sqrt{x})^{2 n+1}-(\sqrt{x+1}-\sqrt{x})^{2 n+1}}{2 \sqrt{x}}\right. & \Leftrightarrow p \mid \mathrm{C}_{2 n+1}^{2 n}(x+1)^{n} \\
& \Leftrightarrow p \mid 2 n+1 .
\end{aligned}
$$

综上, 引理 2 证毕.
引理 3 (扩环 LTE 引理) 记 $\alpha=\sqrt{x+1}+\sqrt{x}, \beta=\sqrt{x+1}-\sqrt{x}, 2 \nmid p$, $2 \nmid t, p$ 是素数, $p \mid x$, 则 $V_{p}\left(\frac{\alpha^{p t}-\beta^{p t}}{\alpha^{p}-\beta^{p}}\right)=V_{p}(t)$.

证明 我们先证一个小结论: $\alpha^{2 m}+\beta^{2 m}$ 不是 $p$ 的倍数 $(p \mid x)$.

这是因为

$$
\left(\alpha^{2 m}+\beta^{2 m}\right)^{2}-\left(\frac{\alpha^{2 m}-\beta^{2 m}}{\sqrt{x(x+1)}}\right)^{2} \cdot x \cdot(x+1)=4
$$

又 $\frac{\alpha^{2 m}-\beta^{2 m}}{\sqrt{x(x+1)}} \in \mathbb{Z}$, 所以两边 $\bmod p$, 知小结论成立.

回到引理 3 的证明, 先考虑 $p \nmid t:$

设 $\alpha^{p}=2 \sqrt{x} \cdot K \cdot p+\beta^{p}$, 则

$$
\frac{\alpha^{p t}-\beta^{p t}}{\alpha^{p}-\beta^{p}}=\frac{\left(2 \sqrt{x} \cdot K \cdot p+\beta^{p}\right)^{t}-\beta^{p t}}{2 \sqrt{x \cdot K \cdot p}},
$$

设其为 $t \cdot \beta^{p(t-1)}+p \cdot m$, 则 $m$ 可写成 $a+b \sqrt{x}+c \sqrt{x+1}+d \sqrt{x(x+1)}$, 其中 $a, b, c, d \in \mathbb{Z}, \beta^{p(t-1)}$ 可写成 $e+f \sqrt{x(x+1)}$ 的形式, 其中 $e, f \in \mathbb{Z}$.

由 $(o)$ 式知 $p \nmid e$, 所以 $\frac{\alpha^{p t}-\beta^{p t}}{\alpha^{p}-\beta^{p}}$ 可写成

$$
p a+t e+p b \sqrt{x}+p c \sqrt{x+1}+(p d+t f) \sqrt{x(x+1)} .
$$

考虑其整数部分得

$$
\frac{\alpha^{p t}-\beta^{p t}}{\alpha^{p}-\beta^{p}} \equiv t e \quad(\bmod p) .
$$

由于 $2 \mid(t-1)$, 结合 (o) 式知 $p \nmid e$, 进而由于 $p \nmid t$, 本情况证毕.

有了上面的过程, 下面证明对于一般的 $p^{s}(s \geq 1)$, 且 $p \nmid t$, 有 $\frac{\alpha^{\left(p^{s}\right) t}-\beta^{\left(p^{s}\right) t}}{\alpha^{\left(p^{s}\right)}-\beta^{\left(p^{s}\right)}}$ 不能被 $p$ 整除.

设 $\alpha^{\left(p^{s}\right)}-\beta^{\left(p^{s}\right)}=2 \sqrt{x} \cdot k \cdot p, k \in \mathbb{Z}$, 则

$$
\frac{\alpha^{\left(p^{s}\right) t}-\beta^{\left(p^{s}\right) t}}{\alpha^{\left(p^{s}\right)}-\beta^{\left(p^{s}\right)}}=\frac{\left(2 \sqrt{x} \cdot k \cdot p+\beta^{\left(p^{s}\right)}\right)^{t}-\beta^{\left(p^{s}\right) t}}{2 \sqrt{x} \cdot k \cdot p}
$$

设其为 $t \cdot \beta^{\left(p^{s}\right)(t-1)}+p \cdot m$, 则 $m$ 可写成

$$
a+b \sqrt{x}+c \sqrt{x+1}+d \sqrt{x(x+1)}
$$

的形式, $\beta^{\left(p^{s}\right)(t-1)}$ 可写成 $e+f \sqrt{x(x+1)}$ 的形式 $(a, b, c, d, e, f \in \mathbb{Z})$.

而 $\frac{\alpha^{\left(p^{s}\right) t}-\beta^{\left(p^{s}\right) t}}{\alpha^{\left(p^{s}\right)}-\beta^{\left(p^{s}\right)}}$ 可写成

$$
p a+t e+p b \sqrt{x}+p c \sqrt{x+1}+(p d+t f) \sqrt{x(x+1)},
$$

考虑其整数部分得

$$
\frac{\alpha^{\left(p^{s}\right) t}-\beta^{\left(p^{s}\right) t}}{\alpha^{\left(p^{s}\right)}-\beta^{\left(p^{s}\right)}} \equiv t e \quad(\bmod p) .
$$

由于 $2 \mid(t-1)$, 结合 (o) 式知 $p \nmid e$, 进而由于 $p \nmid t$, 本情况证毕.

为证明引理 3 , 我们只需证: $\frac{\alpha^{\left(p^{q+1}\right)}-\beta^{\left(p^{q+1}\right)}}{\alpha^{\left(p^{q}\right)}-\beta^{\left(p^{q}\right)}}$ 所含 $p$ 幂次为 1 .

设 $\alpha^{\left(p^{q}\right)}-\beta^{\left(p^{q}\right)}=2 \sqrt{x} \cdot k \cdot p$, 同理, 由于 $p \mid \mathrm{C}_{p}^{i},(1 \leq i \leq p-1)$, 则

$$
\frac{\alpha^{\left(p^{q+1}\right)}-\beta^{\left(p^{q+1}\right)}}{\alpha^{\left(p^{q}\right)}-\beta^{\left(p^{q}\right)}}=\frac{\left(2 \sqrt{x} \cdot k \cdot p+\beta^{\left(p^{q}\right)}\right)^{p}-\beta^{\left(p^{q+1}\right)}}{2 \sqrt{x} \cdot k \cdot p} .
$$

设其为 $p \cdot \beta^{p^{q}(p-1)}+p^{2} \cdot t$, 则 $t$ 可写成

$$
a+b \sqrt{x}+c \sqrt{x+1}+d \sqrt{x(x+1)},
$$

$\beta^{p^{q}(p-1)}$ 可写成 $e+f \sqrt{x(x+1)}$, 其中 $a, b, c, d, e, f \in \mathbb{Z}$.

由 (o) 式知 $p \nmid e$, 所以 $\frac{\alpha^{\left(p^{q+1}\right)}-\beta^{\left(p^{q+1}\right)}}{\alpha^{\left(p^{q}\right)}-\beta^{(p q)}}$ 可写成

$$
p^{2} a+p e+p^{2} b \sqrt{x}+p^{2} c \sqrt{x+1}+\left(p^{2} d+p f\right) \sqrt{x(x+1)} .
$$

考虑其整数部分得

$$
\frac{\alpha^{\left(p^{q+1}\right)}-\beta^{\left(p^{q+1}\right)}}{\alpha^{\left(p^{q}\right)}-\beta^{(p q)}} \equiv p e \quad\left(\bmod p^{2}\right) .
$$

由于 $2 \mid(p-1)$, 结合 (o) 式知 $p \nmid e$, 本情况证毕.

综上, 引理 3 证毕.

引理 4 对于奇素数 $p, p \nmid x, p \neq 3$, 有 $V_{p}\left(\frac{\alpha^{p}-\beta^{p}}{\alpha-\beta}\right)=1$.

证明 可以用二项式定理展开,

$$
\begin{aligned}
\frac{\alpha^{p}-\beta^{p}}{\alpha-\beta} & =\frac{(\sqrt{x+1}+\sqrt{x})^{p}-(\sqrt{x+1}-\sqrt{x})^{p}}{2 \sqrt{x}} \\
& =\mathrm{C}_{p}^{1}(x+1)^{\frac{p-1}{2}}+\mathrm{C}_{p}^{3}(x+1)^{\frac{p-3}{2}} \cdot x+\cdots+\mathrm{C}_{p}^{p} x^{\frac{p-1}{2}}
\end{aligned}
$$

易知从第二项开始每项均是 $p^{2}$ 倍数, 证毕.

于是, 我们对 $x$ 除了 3 以外的质因子 $p$ 证明了

$$
V_{p}\left(\frac{\alpha^{t}-\beta^{t}}{\alpha-\beta}\right)=V_{P}(t)
$$

而对于 3 (如果 $3 \mid x)$, 有

$$
V_{p}\left(\frac{\alpha^{t}-\beta^{t}}{\alpha-\beta}\right)=\left\{\begin{array}{ll}
V_{p}(t)+V_{p}(4 x+3)-1, & p \mid t \\
0, & p \nmid t
\end{array} .\right.
$$

引理 $5(\sqrt{x+1}+\sqrt{x})^{2 n+1}-(\sqrt{x+1}-\sqrt{x})^{2 n+1}>(2 \sqrt{x})^{2 n+1}$.

对于该引理, 我们有更一般的结论: 对于 $a, b>0$ 有 $(a+b)^{n}>a^{n}+b^{n}$. 而这个结论是显然的. 而在一般结论中令 $a=\sqrt{x+1}-\sqrt{x}, b=2 \sqrt{x}$ 就得到了引
理 5.

引理 6 设 $a$ 是不小于 3 的整数, $r$ 是正整数, 则 $a^{r} \geq 2 r+1$.

证明 对 $r$ 归纳证明: 采取第一数学归纳法.

$r=1$ 时是平凡的.

设 $r=m$ 时结论成立, $r=m+1$ 时,

$$
a^{m+1} \geq 2 a^{m} \geq 4 m+2 \geq 2 m+3
$$

也成立.

综上, 引理 6 成立.

我们现在开始证明 $(\triangle)$ 不存在正整数解 $(x, r, n)$, 其中 $x>1$. 由于我们只考虑 $x$ 为奇数的情况, 所以有 $x$ 不小于 3 .

对以下 4 种情况分别进行证明:

第一种情况: 若 $3 \nmid x$ 对于 $p \mid x$, 有 $V_{p}(2 n+1)=V_{p}\left(x^{r}\right)$, 所以 $2 n+1 \geq x^{r}$. $(\triangle)$ 式的右边由于引理 5 大于 $(2 \sqrt{x})^{x^{r}-1}$, 由于引理 6 大于等于 $2^{2 r} x^{r}$, 大于 $(\triangle)$式的左边. 矛盾!

第二种情况: 若 $9 \mid x$, 同上有对于 $p \mid x, V_{p}(2 n+1)=V_{p}\left(x^{r}\right)$, 于是 $2 n+1 \geq$ $x^{r}$. $\left.\triangle\right)$ 式的右边由于引理 5 大于 $(2 \sqrt{x})^{x^{r}-1}$, 由于引理 6 大于等于 $2^{2 r} x^{r}$ 大于 $(\triangle)$ 式的左边, 矛盾!

第三种情况: 若 $3 \mid x$ 但是 $9 \nmid x, 9 \nmid 4 x+3$, 同上有对于 $p \mid x, V_{p}(2 n+1)=$ $V_{p}\left(x^{r}\right)$, 于是 $2 n+1 \geq x^{r} .(\triangle)$ 式的右边由于引理 5 大于 $(2 \sqrt{x})^{x^{r}-1}$, 由于引理 6 大于等于 $2^{2 r} x^{r}$, 大于 $(\triangle)$ 式的左边, 矛盾!

第四种情况: 若 $9 \nmid x, 3|x, 9| 4 x+3$, 有 $x>9$. 对于 $p \mid x, p \neq 3, V_{p}(2 n+1)=$ $V_{p}\left(x^{r}\right)$, 于是 $2 n+1 \geq(x / 3)^{r}$. $(\triangle)$ 式的右边由于与引理 5 大于 $(2 \sqrt{x})^{(x / 3)^{r}-1}$, 由于引理 6 大于等于 $2^{2 r} x^{r}$ 大于 $(\triangle)$ 式的左边, 矛盾!

综上, 待证明的定理成立, 即当 $x>1, x, r$ 为正整数, $\frac{x^{2 r+1}+1}{x+1}$ 不是完全平方数.


[^0]:    修订日期: 2022-02-16.

