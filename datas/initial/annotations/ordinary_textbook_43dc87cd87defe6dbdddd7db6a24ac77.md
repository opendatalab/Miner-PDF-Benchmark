# 最小解在一类整数问题中的应用 

## 曾卫国

(湖南省雅礼中学, 410007)

在某些与正整数解相关的问题中, 会存在无穷多组解的情况, 这个时候, 如果考虑所有解, 对解决实际问题没有太大的帮助. 由于是正整数解, 所以一定有一组最小的解. 此时, 这组最小的解往往成为解题的利刃.

本文将给出几道例题, 均是比较难的题目. 但是利用最小解, 精细地处理一下, 用初中的知识就能解决.

例 1. (Pell 方程) 已知 $d$ 是非完全平方数的正整数, 且方程 $x^{2}-d y^{2}=1$ 有一组正整数组 $\left(x_{0}, y_{0}\right)$ 使得 $x_{0}+\sqrt{d} y_{0}$ 最小. 证明: $x^{2}-d y^{2}=1$ 的任意一组正整数解 $(x, y)$, 均存在正整数 $n$, 使得 $x+\sqrt{d} y=\left(x_{0}+\sqrt{d} y_{0}\right)^{n}, x-\sqrt{d} y=\left(x_{0}-\sqrt{d} y_{0}\right)^{n}$.

证明 对于 $x^{2}-d y^{2}=1$ 的任意一组正整数解 $(x, y)$, 存在正整数 $n$, 使得

$$
\left(x_{0}+\sqrt{d} y_{0}\right)^{n} \leq x+\sqrt{d} y<\left(x_{0}+\sqrt{d} y_{0}\right)^{n+1} .
$$

令

$$
\begin{aligned}
& x^{\prime}+\sqrt{d} y^{\prime}=(x+\sqrt{d} y) /\left(x_{0}+\sqrt{d} y_{0}\right)^{n}=(x+\sqrt{d} y)\left(x_{0}-\sqrt{d} y_{0}\right)^{n}, \\
& x^{\prime}-\sqrt{d} y^{\prime}=(x-\sqrt{d} y) /\left(x_{0}-\sqrt{d} y_{0}\right)^{n}=(x-\sqrt{d} y)\left(x_{0}+\sqrt{d} y_{0}\right)^{n},
\end{aligned}
$$

得

$$
\begin{aligned}
x^{\prime} & =\frac{(x+\sqrt{d} y)\left(x_{0}-\sqrt{d} y_{0}\right)^{n}+(x-\sqrt{d} y)\left(x_{0}+\sqrt{d} y_{0}\right)^{n}}{2}, \\
y^{\prime} & =\frac{(x+\sqrt{d} y)\left(x_{0}-\sqrt{d} y_{0}\right)^{n}-(x-\sqrt{d} y)\left(x_{0}+\sqrt{d} y_{0}\right)^{n}}{2 \sqrt{d}} .
\end{aligned}
$$

易知 $x^{\prime 2}-d y^{\prime 2}=1$, 且 $x^{\prime}$ 是正整数, $y^{\prime}$ 为整数,

$$
1 \leq x^{\prime}+\sqrt{d} y^{\prime}<x_{0}+\sqrt{d} y_{0} .
$$

所以得到 $x^{\prime}-\sqrt{d} y^{\prime} \leq 1$, 所以 $y^{\prime} \geq 0$. 由 $x_{0}+\sqrt{d} y_{0}$ 的最小性知 $y^{\prime}$ 不能大于 0 .

收稿日期: 2017-04-07; 修订日期: 2017-09-28.
所以 $y^{\prime}=0, x^{\prime}=1$.

即 $x+\sqrt{d} y=\left(x_{0}+\sqrt{d} y_{0}\right)^{n}, x-\sqrt{d} y=\left(x_{0}-\sqrt{d} y_{0}\right)^{n}$. 证毕.

例 2. (第 29 届 IMO 试题) 已知 $x, y, \frac{x^{2}+y^{2}}{x y+1}$ 均为正整数. 证明: $\frac{x^{2}+y^{2}}{x y+1}$ 一定是完全平方数.

证明 设 $\frac{x^{2}+y^{2}}{x y+1}=n$ 是正整数. 从而关于 $x, y$ 的方程

$$
x^{2}+y^{2}-n x y-n=0 \text {, }
$$

有正整数解 $(x, y)$, 设 $\left(x_{0}, y_{0}\right)$ 是所有符合条件的 $(x, y)$ 中满足 $x_{0}+y_{0}$ 最小的解,不失一般性, 设 $x_{0} \leq y_{0}$. 我们接下来证明 $n=x_{0}^{2}$.

事实上, 关于 $y$ 的方程

$$
y^{2}-n x_{0} y+x_{0}^{2}-n=0
$$

有根 $y=y_{0}$, 由韦达定理另一根 $y^{\prime}=n x_{0}-y_{0}$ 也是整数, 并且

$$
y^{\prime}=\frac{x_{0}^{2}-n}{y_{0}}<\frac{x_{0}^{2}}{y_{0}} \leq y_{0},
$$

由 $x_{0}+y_{0}$ 的最小性知 $y^{\prime}$ 一定不是正整数, 所以 $y^{\prime} \leq 0$, 从而 $x_{0}^{2}-n \leq 0$.

注意到 $(*)$ 的判别式

$$
\triangle=\left(n x_{0}\right)^{2}-4\left(x_{0}^{2}-n\right)=m^{2},
$$

$m$ 是非负整数, 因为

$$
\left(n x_{0}+2\right)^{2}-m^{2}=4\left(1+n x_{0}+x_{0}^{2}-n\right)>0,
$$

所以

$$
\left(n x_{0}\right)^{2} \leq m^{2}<\left(n x_{0}+2\right)^{2}, \quad n x_{0} \leq m<n x_{0}+2 .
$$

显然 $m$ 与 $n x_{0}$ 同奇偶, 所以 $m=n x_{0}$, 于是 $n=x_{0}^{2}$. 证毕.

注 利用同样的处理方式, 读者可以尝试解决下述题目:

(1). 求所有的正整数 $n$, 使得存在正整数 $x, y$, 满足 $\frac{x^{2}+y^{2}}{x y-1}=n$;

答案为 $n=5$.

(2). 求所有的正整数 $n$, 使得存在正整数 $x, y$, 满足 $\frac{x^{2}+y^{2}}{x y-2}=n$;

答案为 $n=4$ 和 10 .

(3). 一般地: 求所有的正整数 $n$, 使得存在正整数 $x, y$. 满足 $\frac{x^{2}+y^{2}}{x y+k}=n$, 其中 $k$ 为给定的整数.

例 3. 求所有正整数 $n$, 使得存在正整数 $x, y, z$ 满足 $\frac{(x+y+z)^{2}}{x y z}=n$.
解 $n$ 能够取到的值为 $1,2,3,4,5,6,8,9$.

首先, 注意到假如 $\frac{(x+y+z)^{2}}{x y z}=n$, 分别用 $k x, k y, k z$ ( $k$ 是正整数) 取代 $x, y, z$.则 $\frac{(k x+k y+k z)}{k^{3} x y z}=\frac{n}{k}$, 此式说明, 如果 $n$ 可以取到, 则 $n$ 的所有因子也能取到.

$(x, y, z)=(1,1,1)$ 时, $n=9$, 说明 $n$ 可以取到 $1,3,9$;

$(x, y, z)=(1,2,3)$ 时, $n=6$;

$(x, y, z)=(1,4,5)$ 时, $n=5$;

$(x, y, z)=(1,1,2)$ 时, $n=8 ; n$ 还可以取到 2,4 . 所以 $n$ 一定能够取到的值有 $1,2,3,4,5,6,8,9$.

其次, 我们来证明 $n=7$ 或者 $n \geq 10$ 时, 不存在 $x, y, z$ 满足 $\frac{(x+y+z)^{2}}{x y z}=n$.

假设存在 $x, y, z$ 符合. 固定 $n$, 则关于 $x, y, z$ 的方程

$$
(x+y+z)^{2}=n x y z,
$$

一定有正整数解 $(x, y, z)$. 假设 $\left(x_{0}, y_{0}, z_{0}\right)$ 是满足 $x_{0}+y_{0}+z_{0}$ 最小的一组, 不妨设 $x_{0} \leq y_{0} \leq z_{0}$. 接下来证明 $z_{0} \leq x_{0}+y_{0}$.

事实上, 考虑关于 $z$ 的方程 $\left(x_{0}+y_{0}+z\right)^{2}=n x_{0} y_{0} z$, 即

$$
z^{2}+\left(2\left(x_{0}+y_{0}\right)-n x_{0} y_{0}\right)+\left(x_{0}+y_{0}\right)^{2} \text {, }
$$

一定有根 $z=z_{0}$, 由韦达定理, 另一根 $z^{\prime}=n x_{0} y_{0}-2\left(x_{0}+y_{0}\right)$ 显然是整数, 且 $z^{\prime}=\frac{\left(x_{0}+y_{0}\right)^{2}}{z_{0}}$ 是正整数.

从而 $\left(x_{0}, y_{0}, z^{\prime}\right)$ 也是符合 $(x+y+z)^{2}=n x y z$ 的一组正整数解, 由 $x_{0}+y_{0}+z_{0}$的最小性, 知 $z^{\prime}=\frac{\left(x_{0}+y_{0}\right)^{2}}{z_{0}} \geq z_{0}$, 所以 $z_{0} \leq x_{0}+y_{0}$. 于是

$$
\begin{aligned}
7 \leq n & =\frac{\left(x_{0}+y_{0}+z_{0}\right)^{2}}{x_{0} y_{0} z_{0}} \\
& =\frac{1}{x_{0} y_{0}}\left(\frac{\left(x_{0}+y_{0}\right)^{2}}{z_{0}}+2\left(x_{0}+y_{0}\right)+z_{0}\right) \\
& \leq \frac{1}{x_{0} y_{0}}\left(2\left(x_{0}+y_{0}\right)+2\left(x_{0}+y_{0}\right)+\left(x_{0}+y_{0}\right)\right) \\
& \leq \frac{10}{x_{0}} .
\end{aligned}
$$

而

$$
x_{0} \leq y_{0} \leq z_{0} \leq x_{0}+y_{0},
$$

所以 $x_{0}=1, z_{0} \leq 1+y_{0}, z_{0}=y_{0}$ 或者 $1+y_{0}$.

当 $z_{0}=y_{0}$ 时, $n=\frac{\left(1+2 y_{0}\right)^{2}}{y_{0}^{2}}=\left(\frac{1}{y_{0}}+2\right)^{2}$ 是正整数, 所以 $y_{0}=1$, 此时 $n=9$.

当 $z_{0}=y_{0}+1$ 时, $n=\frac{4\left(1+y_{0}\right)}{y_{0}}=4+\frac{4}{y_{0}}, y_{0}=1,2,4, n=5,6,8$, 也不等于 7 .

综上: $n=1,2,3,4,5,6,8,9$.
例 4. $n$ 是给定大于 1 的正整数, 求最大的正整数 $k$, 使得存在正整数 $x_{1}, \cdots, x_{n}$, 满足 $x_{1}^{2}+\cdots+x_{n}^{2}=k x_{1} \cdots x_{n}$.

解 $k$ 的最大值为 $n$.

显然 $x_{1}, \cdots, x_{n}$ 均取 1 时, $k=n$.

当 $n=2$ 时, 设 $\left(x_{1}, x_{2}\right)=d, x_{1}=a d, x_{2}=b d,(a, b)=1$, 进而得到 $a=b=1$. 所以 $k=2$.

接下来证明 $k>n>2$ 时, $x_{1}^{2}+\cdots+x_{n}^{2}=k x_{1} \cdots x_{n}$ 无正整数解.

事实上, 固定 $k$, 假如 $x_{1}^{2}+\cdots+x_{n}^{2}=k x_{1} \cdots x_{n}$ 有正整数解 $\left(x_{1}, \cdots, x_{n}\right)$, 那么在所有的解中, 一定有一组 $\left(y_{1}, \cdots, y_{n}\right)$, 使得 $y_{1}+\cdots+y_{n}$ 最小.

不妨设 $y_{1} \geq \cdots \geq y_{n}$. 考虑关于 $y$ 的方程

$$
y^{2}-k y y_{2} \cdots y_{n}+y_{2}^{2}+\cdots+y_{n}^{2}=0
$$

一定有解 $y=y_{1}$. 由韦达定理另外一个根 $y^{\prime}$ 满足

$$
y^{\prime}=k y_{2} \cdots y_{n}-y_{1}, \quad y^{\prime}=\frac{y_{2}^{2}+\cdots+y_{n}^{2}}{y_{1}}>0
$$

所以 $y^{\prime}$ 也是正整数, 由于 $y_{1}+\cdots+y_{n}$ 的最小性, 知

$$
y^{\prime}=\frac{y_{2}^{2}+\cdots+y_{n}^{2}}{y_{1}} \geq y_{1}
$$

于是

$$
y_{1}^{2} \leq y_{2}^{2}+\cdots+y_{n}^{2} \leq(n-1) y_{2}^{2}
$$

从而

$$
n y_{1} y_{2} \cdots y_{n}<k y_{1} y_{2} \cdots y_{n}=y_{1}^{2}+y_{2}^{2}+\cdots+y_{n}^{2} \leq 2(n-1) y_{2}^{2}<2 n y_{2}^{2}
$$

因为 $n>2$, 则 $y_{3} \cdots y_{n}<2$, 说明 $y_{3}=\cdots=y_{n}=1$, 从而

$$
y^{2}-k y y_{2}+y_{2}^{2}+n-2=0 .
$$

当 $y=y_{2}$ 时, 有 $k=2+\frac{n-2}{y^{2}} \leq n$, 与 $k>n$ 矛盾.

当 $y \neq y_{2}$ 时, 因为 $y_{1} \geq y_{2}$, 所以 $y_{1}>y_{2}$, 进而

$$
\left(y_{2}+1\right)^{2} \leq y_{1}^{2} \leq y_{2}^{2}+n-2 .
$$

所以 $n \geq 2 y_{2}+3$. 方程 $y^{2}-k y y_{2}+y_{2}^{2}+n-2=0$ 的判别式为 $\left(k y_{2}\right)^{2}-$ $4\left(y_{2}^{2}+n-2\right)=m^{2}$ 是完全平方数, 且 $m<k y_{2}$, 且 $m$ 与 $k y_{2}$ 同奇偶, 所以

$$
\left(k y_{2}\right)^{2}-4\left(y_{2}^{2}+n-2\right)=m^{2} \leq\left(k y_{2}-2\right)^{2}
$$

从而 $n y_{2}<k y_{2} \leq y_{2}^{2}+n-1$, 因此 $n\left(y_{2}-1\right)<\left(y_{2}-1\right)\left(y_{2}+1\right)$, 进而有 $n<y_{2}+1$,且 $y_{2} \neq 1$, 与 $n \geq 2 y_{2}+3$ 矛盾.
综上, $k$ 的最大值为 $n$.

注 读者可以尝试解决下面问题: 已知 $k$ 是给定大于 3 的正整数, 求最小的 $n(n>k)$, 使得存在正整数 $x_{1}, \cdots, x_{n}$, 满足 $x_{1}^{2}+\cdots+x_{n}^{2}=k x_{1} \cdots x_{n}$.

例 5. (第 48 届 IMO 试题) $m, n$ 是正整数, 证明: 如果 $4 m n-1 \mid\left(4 m^{2}-1\right)^{2}$,则 $m=n$.

证明 因为 $4 m n-1 \mid\left(4 m^{2}-1\right)^{2}$, 所以 $4 m n-1 \mid\left(16(m n)^{2}-4 m^{2}\right)^{2}$. 于是 $4 m n-1 \mid\left(4 n^{2}-1\right)^{2}$.

所以 $(4 m n-1)^{2} \mid\left(4 n^{2}-1\right)^{2}\left(4 m^{2}-1\right)^{2}$, 从而 $4 m n-1 \mid\left(4 n^{2}-1\right)\left(4 m^{2}-1\right)$. 即 $4 m n-1\left|(4 n m-1)^{2}-4(m-n)^{2}, 4 m n-1\right| 4(m-n)^{2}$, 所以 $4 m n-1 \mid(m-n)^{2}$.

设 $(m-n)^{2}=k(4 m n-1)$, 当 $k=0$ 时, 结论已经成立. 接下来证明 $k>0$时不可能. 用反证法.

对于固定的正整数 $k$, 假如存在正整数组 $(m, n)$, 使得 $(m-n)^{2}=k(4 m n-1)$.设 $\left(m_{0}, n_{0}\right)$ 是其中满足 $m_{0}+n_{0}$ 最小的一组. 不妨设 $m_{0}<n_{0}$.

于是考虑关于 $n$ 的方程 $\left(m_{0}-n\right)^{2}=k\left(4 m_{0} n-1\right)$, 即

$$
n^{2}-(4 k+2) m_{0} n+m_{0}^{2}+k=0
$$

有一个正整数根 $n=n_{0}$, 另一个根 $n^{\prime}=(4 k+2) m_{0}-n_{0}$ 是整数, $n^{\prime}=\frac{m_{0}^{2}+k}{n_{0}}>0$,所以 $\left(m_{0}, n^{\prime}\right)$ 也是符合的一组正整数根. 由 $m_{0}+n_{0}$ 最小知 $n^{\prime}=\frac{m_{0}^{2}+k}{n_{0}} \geq n_{0}$, 所以 $k \geq n_{0}^{2}-m_{0}^{2} \geq 2 m_{0}+1$, 而方程 $n^{2}-(4 k+2) m_{0} n+m_{0}^{2}+k=0$ 的判别式

$$
\Delta=4(2 k+1)^{2} m_{0}^{2}-4\left(m_{0}^{2}+k\right)
$$

是完全平方, 所以 $(2 k+1)^{2} m_{0}^{2}-\left(m_{0}^{2}+k\right)$ 是完全平方, 且小于 $(2 k+1)^{2} m_{0}^{2}$, 所以

$$
(2 k+1)^{2} m_{0}^{2}-\left(m_{0}^{2}+k\right) \leq\left((2 k+1) m_{0}-1\right)^{2}
$$

从而得到

$$
\left(m_{0}-1\right)^{2} \geq k\left(4 m_{0}-1\right) \geq\left(4 m_{0}-1\right)\left(2 m_{0}+1\right)
$$

整理得到 $7 m_{0}^{2}+4 m_{0}-2 \leq 0$, 这与 $m_{0}$ 是正整数矛盾.

所以假设不成立, 即 $k$ 只能是 0 , 从而 $m=n$.

