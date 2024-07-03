# 函数方程问题的一些方法 

施奕成

(华中师范大学第一附属中学，430223)

函数方程是一类比较有趣的代数问题, 也是近几年 IMO 的常考题型 (2015 年第 5 题, 2017 年第 2 题). 本文介绍一些函数方程问题的解题方法.

笔者认为, 对于一般的函数方程问题, 有以下几种思考方向:

(1) 考虑一些特殊值. 比如 $f(0), f(1), f(-1)$ 之类. 可先将其求出, 再代入到原函数方程中, 可以得到一些有用的结论.

（2）考虑函数的一些特殊性质. 比如考虑 $f$ 是否为单射, 满射. $f$ 是否为奇函数等性质.

(3) 考虑所给函数方程的形式. 通过式子形式来选择用什么方法去做, 比如,若所给式子形式为柯西方程的形式, 那么应尽可能地去凑出柯西方程的条件(单调性, 连续性).

下面介绍几种函数方程问题的方法.

## I. 合理代入特殊值

题 1. 求函数 $f: \mathbb{R} \rightarrow \mathbb{R}$ 使得对任意 $x, y \in \mathbb{R}$,

$$
f(f(x)+y)=f\left(x^{2}-y\right)+4 f(x) y .
$$

解 固定 $x$, 取 $y$ 使得

$$
f(x)+y=x^{2}-y
$$

即 $y=\frac{x^{2}-f(x)}{2}$, 则此时

$$
f(f(x)+y)=f\left(x^{2}-y\right)
$$

故对任意 $x \in \mathbb{R}$,

$$
2 f(x)\left(x^{2}-f(x)\right)=0 .
$$

则对任意 $x \in \mathbb{R}, f(x)=0$, 或 $f(x)=x^{2}$. 于是 $f(0)=0$.

收稿日期: 2018-01-17； 修订日期: 2018-02-21.
若有 $a \neq 0, f(a)=0$, 在 (1) 中令 $x=0, x=a$, 可分别得出

$$
f(y)=f(-y) \text { 及 } f(y)=f\left(a^{2}-y\right) .
$$

故

$$
f(y)=f(-y)=f\left(a^{2}+y\right),
$$

即 $a^{2}$ 为 $f$ 的周期.

由 (1), 对任意 $x, y \in \mathbb{R}$, 有

$$
f\left(f(x)+y+a^{2}\right)=f\left(x^{2}-y-a^{2}\right)+4 f(x)\left(y+a^{2}\right) .
$$

又

$$
f\left(f(x)+y+a^{2}\right)=f(f(x)+y), f\left(x^{2}-y-a^{2}\right)=f\left(x^{2}-y\right),
$$

故

$$
4 f(x)\left(y+a^{2}\right)=4 f(x) y \text {. }
$$

故 $a^{2} f(x)=0$. 又 $a \neq 0$, 因此 $f(x)=0 . \forall x \in \mathbb{R}$.

故综上可知 $f(x)=x^{2}, \forall x \in \mathbb{R}$ 或 $f(x)=0, \forall x \in \mathbb{R}$.

经检验, 上述两解符合题意.

注 本题最重要的地方就是观察 (1) 后, 发现代入特殊的 $y$ 可使得两个麻烦的式子 $f(f(x)+y)$ 及 $f\left(x^{2}-y\right)$ 都被消掉, 后面就简单了.

题 2. 求所有的函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对于任意实数 $x, y$, 有

$$
f(f(x) f(y))+f(x+y)=f(x y) .
$$

解 令 $x=y=0$, 则 $f\left(f^{2}(0)\right)=0$.

考虑 $z \in \mathbb{R}, f(z)=0$. (由上式, 这样的 $z$ 存在)

若 $z=0$, 在 (1) 中令 $y=0$, 则

$$
f(x)=0, \forall x \in \mathbb{R}
$$

若 $z \neq 0,1$, 在 (1) 中令 $x=z, y=\frac{z}{z-1}$, 这样有 $x+y=x y$. 故

$$
f\left(f(z) f\left(\frac{z}{z-1}\right)\right)=0 .
$$

故 $f(0)=0 \Rightarrow f(x)=0, \forall x \in \mathbb{R}$.

下面假设满足 $f(z)=0$ 的实数 $z$ 仅 $z=1$, 那么

$$
f^{2}(0)=1 \Rightarrow f(0)= \pm 1
$$

$f(0)=-1$ 时, 在 (1) 中令 $y=1$, 则对任意 $x \in \mathbb{R}$ 有

$$
f(x+1)=f(x)+1 \text {. }
$$

下证 $f$ 为单射, 若存在 $x_{1}, x_{2} \in \mathbb{R}, x_{1} \neq x_{2}, f\left(x_{1}\right)=f\left(x_{2}\right)$.

首先, 有结论 $f(x)=-1$ 的解为

$$
x=0 .
$$

这是因为由 (1) 可知 $f(x+1)=0 \Rightarrow x+1=1 \Rightarrow x=0$.

取 $N \in \mathbb{N}_{+}$, 使 $\left(x_{1}+N+1\right)^{2}>4\left(x_{1}+N\right)$. 则必有 $x \in \mathbb{R}, y \in \mathbb{R}$,

$$
x+y=x_{1}+N+1, x y=x_{2}+N .
$$

于是取这样的 $(x, y)$ 代入 (1) 有

$$
f(f(x) f(y))+f\left(x_{1}+N+1\right)=f\left(x_{2}+N\right) .
$$

由 (2) 易知

$$
f\left(x_{1}+N+1\right)=N+1+f\left(x_{1}\right), f\left(x_{2}+N\right)=f\left(x_{2}\right)+N \text {. }
$$

结合 $f\left(x_{1}\right)=f\left(x_{2}\right)$, 有 $f(f(x) f(y))=-1$. 由 (3) 知 $f(x) f(y)=0$.

不妨设 $f(x)=0 \Rightarrow x=1$. 故 $y=x_{1}+N$, 因此 $x_{1}+N=x_{2}+N \Rightarrow x_{1}=x_{2}$,矛盾. 故 $f$ 为单射.

此时在 (1) 中令 $y=0$, 有

$$
f(-f(x))+f(x)=-1 .
$$

在 (4) 中令 $x=-f(x)$, 有

$$
f(-f(x))+f(-f(-f(x)))=-1 .
$$

(4) $-(5)$ 有 $f(x)=f(-f(-f(x)))$. 故

$$
x=-f(-f(x)) \text {, (由单射) }
$$

结合 (4) 有 $f(x)=x-1, \forall x \in \mathbb{R}$.

$f(0)=1$ 时, 令 $g(x)=-f(x)$, 则

$$
g(g(x) g(y))+g(x+y)=g(x y) \text { 且 } g(0)=-1, g(1)=0 \text {. }
$$

同理可知 $g(x)=x-1$. 故 $f(x)=1-x$.

综上知对任意 $x \in \mathbb{R}$, 有

$$
f(x) \equiv 0 \text { 或 } f(x)=x-1 \text { 或 } f(x)=1-x \text {. }
$$

经检验, 上述三解均合题.
注 本题的关键即为证明 $f$ 为单射. 而证明单射的方法也是用取特殊值得方法消去一些东西, 从而将式子化到最简.

## II. 算二次

题 3. 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使对任意 $x, y \in \mathbb{R}$, 有

$$
f\left(x^{2}+y+f(y)\right)=2 y+f^{2}(x) .
$$

解 在 (1) 中令 $x=0$, 得

$$
f(y+f(y))=2 y+f^{2}(0) .
$$

故 $f$ 为满射.

在 (1) 中将 $x$ 换为 $-x$, 有

$$
f\left(x^{2}+y+f(y)\right)=f^{2}(-x)+2 y,
$$

可得 $f^{2}(-x)=f^{2}(x)$. 故 $f(-a)=0$.

在 (1) 中令 $x=0, y=a$, 则

$$
2 a+f^{2}(0)=f(a+f(a))=f(a)=0 .
$$

在 (1) 中令 $x=0, y=-a$, 则

$$
-2 a+f^{2}(0)=f(-a+f(-a))=f(-a)=0 \text {. }
$$

故

$$
2 a+f^{2}(0)=-2 a+f^{2}(0)
$$

由此可得 $a=0$. 因此 $f(0)=0$.

在 (1) 中令 $y=0$ 有 $f\left(x^{2}\right)=f^{2}(x)$. 故 $x \geq 0$ 时,

$$
f(x)=f^{2}(\sqrt{x}) \geq 0 .
$$

故

$$
f\left(x^{2}+y+f(y)\right)=2 y+f\left(x^{2}\right) .
$$

将 $x^{2}$ 换为 $x$ 知, $x \geq 0$ 时,

$$
f(x+y+f(y))=f(x)+2 y \text {. }
$$

取 $x \geq 0, y \geq 0, z \geq 0$, 则

$$
f(x) \geq 0, f(y) \geq 0, f(z) \geq 0 .
$$

考虑 $f(z+x+y+f(y)+f(x+y+f(y)))$. 一方面，

$$
f(z+x+y+f(y)+f(x+y+f(y)))=f(z)+2(x+y+f(y)),
$$

另一方面，

$$
\begin{aligned}
& f(z+x+y+f(y)+f(x+y+f(y))) \\
= & f(z+x+y+f(y)+f(x)+2 y) \\
= & f(z+3 y+f(y+x+f(x))) \\
= & 2 x+f(z+3 y+f(y)) \\
= & 2 x+2 y+f(z+2 y) .
\end{aligned}
$$

比较上两式知

$$
f(x)+2 f(y)=f(z+2 y)(y \geq 0, z \geq 0)
$$

令 $z=0$, 有 $f(2 y)=2 f(y)$, 故

$$
f(z+2 y)=f(z)+f(2 y) \quad(z \geq 0, y \geq 0)
$$

故对任意 $x \geq 0, y \geq 0$,

$$
f(x+y)=f(x)+f(y) .
$$

又 $x \geq 0$ 时, $f(x) \geq 0$, 故

$$
f(x+y) \geq f(y) .
$$

故 $f$ 在 $[0, \infty)$ 上单调不减. 则 $f(x)=c x \quad(x \geq 0, c=f(1))$. (由柯西方程)

而在 (3) 中令 $x \geq 0, y \geq 0$, 有

$$
c(x+y+c y)=c x+2 y .
$$

故 $c^{2} y=y \Rightarrow c= \pm 1$, 由 $c \geq 0 \Rightarrow c=1$. 故 $x \geq 0$ 时, $f(x)=x$.

若存在 $x_{0}>0, f\left(x_{0}\right)=f\left(-x_{0}\right)$ 则

$$
f\left(-x_{0}\right)=x_{0} .
$$

在 (1) 中令 $x=0, y=-x_{0}$, 则

$$
f\left(-x_{0}+f\left(-x_{0}\right)\right)=-2 x_{0} .
$$

故 $f(0)=-2 x_{0}$ 可得 $-2 x_{0}=0 \Rightarrow x_{0}=0$ 矛盾.

则由 $f^{2}(x)=f\left(x^{2}\right)$, 知

$$
f^{2}(x)=f^{2}(-x),
$$

故 $f(x)=-f(-x)$. 因此对任意 $x \in \mathbb{R}, f(x)=x$.

经检验 $f(x)=x(x \in \mathbb{R})$ 合题.

注 本题困难之处在于 (1) 中 $f\left(x^{2}+y+f(y)\right)$ 并不能好处理. 而添加一个
变量算二次后则可将一个很复杂的式子变为两个不同形式的简单式子, 从而得到关键讨论.

题 4. 求所有的 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使对任意 $x, y \in \mathbb{R}$,

$$
f(x+y)=f(x) f(y) f(x y) .
$$

解 对任意 $x, y, z \in \mathbb{R}$,

$$
\begin{aligned}
f(x+y+z) & =f(x+y) f(z) f((x+y) z) \\
& =f(z) f(x) f(y) f(x y) f(x z+y z) \\
& =f(x) f(y) f(z) f(x y) f(y z) f(z x) f\left(x y z^{2}\right), \\
f(x+y+z) & =f(x+z) f(y) f(x y+z y) \\
& =f(y) f(x) f(z) f(x z) f(x y) f(z y) f\left(x y^{2} z\right) .
\end{aligned}
$$

若存在 $x_{0} \in \mathbb{R}, f\left(x_{0}\right)=0$, 则对任意 $x \in \mathbb{R}$,

$$
f(x)=f\left(x-x_{0}\right) f\left(x_{0}\right) f\left(\left(x-x_{0}\right) x_{0}\right)=0 .
$$

若对任意 $x \in \mathbb{R}, f(x) \neq 0$, 则由 (2) (3) 知,

$$
f\left(x y z^{2}\right)=f\left(x y^{2} z\right) .
$$

取 $y \neq 0, z \neq 0, z=\frac{1}{y z}$, 则 $f(y)=f(z)$.

故对 $x \neq 0, f(x)=c$ ( $c$ 为常数), 由 (1) $c^{3}=c \Rightarrow c^{2}=1 \Rightarrow c= \pm 1$ (由于 $c \neq 0)$. 而

$$
f(0)=f(x) f(-x) f\left(-x^{2}\right)=c^{3}=c(x \neq 0) .
$$

综上对 $x \in \mathbb{R}$,

$$
f(x) \equiv 0 \text { 或 } f(x) \equiv 1 \text { 或 } f(x) \equiv-1 \text {. }
$$

经检验, 上述三解符合题.

注 本题的条件式并不算太复杂, 但若按一般方法去代入特值会讨论地有些麻烦. 这里添加一个变量 $z$ 算二次可以充分利用本题的对称性消去大部分式子从而得到 $f\left(x y z^{2}\right)=f\left(x y^{2} z\right)$.

题 5. 求所有的函数 $f: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$, 使得对任意 $x, y \in \mathbb{R}_{+}$,

$$
f(x+y+f(y))=4030 x-f(x)+f(2016 y) .
$$

解 记 $A=f(1)+1, B=f(2016)$.
在 (1) 中令 $y=1$ 有

$$
f(x+A)=4030 x-f(x)+B,
$$

下考虑 $f(x+A+y+f(y))$. 一方面

$$
\begin{aligned}
f(x+A+y+f(y)) & =4030(x+y+f(y))-f(x+y+f(y))+B \\
& =4030(x+y+f(y))-4030 x+f(x)-f(2016 y)+B \\
& =4030 y+4030 f(y)+f(x)-f(2016 y)+B .
\end{aligned}
$$

另一方面

$$
\begin{aligned}
f(x+A+y+f(y)) & =4030(x+A)-f(x+A)+f(2016 y) \\
& =4030(x+A)-4030 x+f(x)-B+f(2016 y) \\
& =4030 A+f(x)-B+f(2016 y) .
\end{aligned}
$$

综合上两式知

$$
f(2016 y)=2015(y+f(y))+B-2015 A \text {. }
$$

在 (1) 中令 $x=1$ 有

$$
\begin{aligned}
f(1+y+f(y)) & =4030-f(1)+f(2016 y) \\
& =2015(y+f(y)+1)+2015-f(1)+B-2015 A .
\end{aligned}
$$

故对任意 $x \in \mathbb{R}_{+}$,

$$
f(x+f(x)+1)=2015(x+f(x)+1)+c \text { (c 为常数). }
$$

又在 (1) 中令 $x=2016 y$, 知

$$
f(2017 y+f(y))=4030 \cdot 2016 y \text {. }
$$

故 $f$ 为 $\mathbb{R}_{+}$上满射.

而由 $(*)$ 知,

$$
1+\frac{f(2016 y)+2015 A-B}{2015}=y+f(y)+1 .
$$

又对任意 $y>0$, 存在 $y_{0}, f\left(2016 y_{0}\right)=y$.

故对任意 $x>1+\frac{2015 A-B}{2015}$ (即 $1+\frac{2015 A-B}{2015}=\lambda$ ), 即对任意 $x>\lambda$ ( $\lambda$ 为常数), 存在 $x_{0} \in \mathbb{R}$, 使 $x_{0}+f\left(x_{0}\right)+1=x$.

结合 (2) 知, 对 $x>\lambda, f(x)=2015 x+c$.

不妨设 $\lambda>0$ (若 $\lambda \leq 0$ 本题已解决), 取 $y>10^{10} \lambda+10^{10} k, x>\lambda$.

$$
f(x+y+2015 y+c)=4030 x-f(x)+2015(2016 y)+c .
$$

故

$$
2015(x+y+2015 y+c)+c=4030 x-2015 x-c+2015 \cdot 2016 y+c .
$$

故 $2016 c=0$, 因此 $c=0$.

在 (1) 中取 $y>10^{10} \lambda+10^{10} k$, 对 $x \leq \lambda$, 有

$$
2015(x+y+2015 y)=4030 x-f(x)+2015 \cdot 2016 y .
$$

从而 $f(x)=2015 x$. 故对任意 $x \in \mathbb{R}_{+}, f(x)=2015 x$.

经检验, 此解合题.

## III. 利用极限解决函数方程

在某些函数方程题中, 其条件全给一些不等式关系. 此时可以考虑重复某一估计步骤并用极限得出函数方程的解.

题 6. 求所有函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{R}$, 使得对任意 $k, m, n \in \mathbb{N}^{*}$, 有

$$
f(k m)+f(k n)-f(k) f(m n) \geq 1 .
$$

解 令 $k=m=n=1$ 得

$$
2 f(1) \geq 1+f^{2}(1)
$$

可得 $f(1)=1$.

令 $m=n=1$ 得

$$
f(k)+f(k)-f(k) \geq 1
$$

故对任意 $k \in \mathbb{N}_{+}, f(k) \geq 1$.

令 $k=m=n$ 得

$$
2 f\left(k^{2}\right)-f(k) f\left(k^{2}\right) \geq 1, f\left(k^{2}\right)(2-f(k)) \geq 1 .
$$

结合对任意 $x \in \mathbb{N}_{+}, f(x) \geq 1$ 知 $f(k)<2$. 故

$$
f\left(k^{2}\right) \geq \frac{1}{2-f(k)}
$$

下归纳证明: 对任意 $k \in \mathbb{N}_{+}, \frac{n+1}{n}>f(k) \geq 1$ ( $n$ 为任意正整数).

$n=1$ 时, $2>f(k) \geq 1$ 成立.

设对 $n$ 时已成立 $(n \geq 1)$, 考虑 $n+1$ 时, 此时由 (*) 有

$$
\frac{n+1}{n}>f\left(k^{2}\right) \geq \frac{1}{2-f(k)} .
$$

故

$$
\frac{2 n+2}{n}-\frac{n+1}{n} f(k)>1 .
$$

因此

$$
f(k)<\frac{n+2}{n+1}
$$

从而对 $n+1$ 时结论也成立.

故对任意 $k \in \mathbb{N}_{+}, n \in \mathbb{N}_{+}$,

$$
\frac{n+1}{n}>f(k) \geq 1 \text {. }
$$

此时取 $n \rightarrow+\infty$, 由于 $\lim _{n \rightarrow \infty} \frac{n+1}{n}=1$, 故 $f(k)=1\left(k \in \mathbb{N}_{+}\right)$.

因此 $f(x) \equiv 1\left(\forall x \in \mathbb{N}_{+}\right)$, 经检验合题.

注 本题所能用的等式条件并不多, 只有一些不等关系. 而在较粗略的估计 $2>f(k) \geq 1$ 后, 便可以发现 $f(k)$ 的范围可不断精确, 由此便可以求极限.

题 7. 求满足以下条件的所有函数 $f:[1,+\infty) \rightarrow[1,+\infty)$
(1) $f(x) \leq 2(x+1)$;
(2) $f(x+1)=\frac{1}{x}\left[f^{2}(x)-1\right]$.

解 令 $g(x)=f(x)-x-1$, 则 $-x \leq g(x) \leq x+1$, 且 $g(x+1)=$ $\frac{1}{x} g(x)(g(x)+2 x+2)$. 故由

$$
\frac{1}{x} g(x)(g(x)+2 x+2)=g(x+1) \leq x+2
$$

知

$$
(g(x)+x+1)^{2} \leq x(x+2)+(x+1)^{2}<2(x+1)^{2} .
$$

故

$$
g(x)<\left(2^{\frac{1}{2}}-1\right)(x+1) .
$$

下设 $g(x)<\left(2^{\frac{1}{2^{k}}}-1\right)(x+1)\left(k \in \mathbb{N}_{+}\right)$已成立, 则

$$
g(x+1)=\frac{1}{x} g(x)(g(x)+2 x+2)<\left(2^{\frac{1}{2^{k}}}-1\right)(x+2) .
$$

故

$$
(g(x)+x+1)^{2} \leq(x+1)^{2}+\left(2^{\frac{1}{2^{k}}}-1\right)(x+2) x \leq 2^{\frac{1}{2^{k}}}(x+1)^{2} .
$$

故

$$
g(x)<\left(2^{\frac{1}{2^{k+1}}}-1\right)(x+1) .
$$

故对任意 $k \in \mathbb{N}_{+}$,

$$
g(x)<\left(2^{\frac{1}{2^{k}}}-1\right)(x+1) \text {. }
$$

取 $k \rightarrow+\infty$ 知 $g(x) \leq 0, x \in[1,+\infty)$.
又

$$
g(x+1)=\frac{1}{x} g(x)(g(x)+2 x+2) \geq-x-1,
$$

故

$$
(g(x)+x+1)^{2} \geq x+1
$$

故

$$
g(x) 2-x-1+\sqrt{x+1} \geq-x-1+x^{\frac{1}{2}}
$$

(由于 $g(x) \geq-x$ 故 $g(x) \leq-x-1-\sqrt{x+1}$ 不成立.) 故

$$
\frac{1}{x} g(x)(g(x)+2 x+2)=g(x+1) \geq-x-2+\sqrt{x+1},
$$

故

$$
(g(x)+x+1)^{2} \geq 1+x \sqrt{x+1}
$$

故

$$
g(x) \geq-x-1+\sqrt{1+x \sqrt{x+1}} \geq-x-1+x^{1-\frac{1}{2^{k}}} .
$$

设已有 $g(x) \geq-x-1+x^{1-\frac{1}{2^{k}}}$ 成立, 则

$$
g(x+1)=\frac{1}{x} g(x)(g(x)+2 x+2) \geq-(x+2)+(x+1)^{1-\frac{1}{2^{k}}} .
$$

故

$$
(g(x)+x+1)^{2} \geq 1+x(x+1)^{1-\frac{1}{2^{k}}}>x^{2-\frac{1}{2^{k}}},
$$

故

$$
g(x) \geq-x-1+x^{1-\frac{1}{2^{k+1}}}
$$

对 $k+1$ 也成立. 故任意 $k \in \mathbb{N}_{+}$,

$$
g(x) \geq-x-1+x^{1-\frac{1}{2^{k}}}
$$

取 $k \rightarrow+\infty$ 知 $g(x) \geq-1(\forall x \in[1,+\infty))$,

$$
\frac{1}{x} g(x)(g(x)+2 x+2)=g(x+1) \geq-1,
$$

故

$$
(g(x)+x+1)^{2} \geq x^{2}+x+1>\left(x+\frac{1}{2}\right)^{2} .
$$

故 $g(x) \geq-\frac{1}{2}$.

设已有 $g(x) \geq-\frac{1}{2^{k}}\left(k \in \mathbb{N}_{+}\right)$, 则

$$
\frac{1}{x} g(x)(g(x)+2 x+2)=g(x+1) \geq-\frac{1}{2^{k}},
$$

故

$$
(g(x)+x+1)^{2} \geq(x+1)^{2}-\frac{1}{2^{k}} x>\left(x+1-\frac{1}{2^{k+1}}\right)^{2} .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_d7ccb34fe004ec8e66cdg-11.jpg?height=65&width=1420&top_left_y=390&top_left_x=318)
$0(\forall x \in[1,+\infty))$.

综上 $g(x) \leq 0(x \in[1,+\infty))$ 得 $g(x) \equiv 0(x \in[1,+\infty))$.

故 $f(x)=x+1(x \in[1,+\infty))$.

经检验合题.

注 本题由条件得到 $g(x)$ 的范围后只用无脑重复估计过程即可得到最佳范围估计 $(0 \leq g(x) \leq 0)$.

## IV. 构造多项式

有时对于函数 $f$ 若可以证 $x \in \mathbb{Q}$ 时 $f(x) \geq x$, 但 $x \notin \mathbb{Q}$ 时无法证明, 可以构造多项式用代数基本定理证明.

题 8. 给定 $k \in \mathbb{N}_{+}, k \geq 2$. 求所有的函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使对任意 $x, y \in$ $\mathbb{R}, f(x+y)=f(x)+f(y)$ 且 $f\left(x^{k}\right)=(f(x))^{k}$.

解 $k$ 为偶数时, $x \geq 0$ 时, $f(x)=\left(f\left(x^{\frac{1}{k}}\right)\right)^{k} \geq 0$. 故 $x \geq 0, y \geq 0$ 时,

$$
f(x+y) \geq f(x),
$$

即 $f(x)$ 在 $[0,+\infty)$ 上单调不减. 故由柯西方程 $f(x)=c x(c \in \mathbb{R})$. 故 $c x^{k}=c^{k} x^{k}$,故 $c^{k}=c \Rightarrow c=0,1$, 因此 $f(x) \equiv 0(x \in \mathbb{R})$ 或 $f(x)=x(x \in \mathbb{R})$. 经检验合题.

$k$ 为奇数时, 由柯西方法易知对任意 $q_{0} \in \mathbb{Q}$,

$$
f\left(q_{0} x\right)=q_{0} f(x)(x \in \mathbb{R}) .
$$

取 $q_{0} \in \mathbb{Q}$, 则

$$
\begin{aligned}
\left(f\left(x+q_{0}\right)\right)^{k} & =\left(f(x)+f\left(q_{0}\right)\right)^{k} \\
& =f^{k}(x)+k f^{k-1}(x) f\left(q_{0}\right)+\cdots+f^{k}\left(q_{0}\right) \\
& =f^{k}(x)+k q_{0} f(1) f^{k-1}(x)+\cdots+\left(q_{0} f(1)\right)^{k}
\end{aligned}
$$

且

$$
\begin{aligned}
\left(f\left(x+q_{0}\right)\right)^{k} & =f\left(\left(x+q_{0}\right)^{k}\right) \\
& =f\left(x^{k}+k x^{k-1} q_{0}+\cdots+q_{0}^{k}\right) \\
& =f^{k}(x)+k f\left(x^{k-1} q_{0}\right)+\cdots+f^{k}\left(q_{0}\right) \\
& =f^{k}(x)+k q_{0} f\left(x^{k-1}\right)+\cdots+\left(q_{0} f(1)\right)^{k} .
\end{aligned}
$$

固定 $x$, 记

$$
g\left(q_{0}\right)=\left(f^{k}(x)+\cdots+\left(q_{0} f(1)\right)^{k}\right)-\left(f^{k}(x)+k q_{0} f(1) f^{k-1}(x)+\cdots+\left(q_{0} f(1)\right)^{k}\right) .
$$

对任意 $q_{0} \in \mathbb{Q}, g\left(q_{0}\right)=0$. 故 $g\left(q_{0}\right)$ 每项系数都为 0 . (由于 $g$ 为 $\leq k$ 次多项式, 而其有无穷多个根) 比较一次项系数有

$$
f^{k-1}(x) f(1)=f\left(x^{k-1}\right) .
$$

故对 $x \geq 0$,

$$
f(x)=\left(f\left(x^{\frac{1}{k-1}}\right)\right)^{k-1} f(1)
$$

恒非负或恒非正. 故可知 $f$ 在 $[0,+\infty)$ 上单调不减或单调不增, 由柯西方程 $f(x)=c x$ ( $c$ 为常数). 由 $f\left(x^{k}\right)=(f(x))^{k}$ 知 $c^{k}=c \Rightarrow c=0, \pm 1$.

故 $k$ 为奇数时, $f(x) \equiv 0(x \in \mathbb{R})$ 或 $f(x)=x(x \in \mathbb{R})$ 或 $f(x)=-x(x \in \mathbb{R})$.经检验上述三解合题.

