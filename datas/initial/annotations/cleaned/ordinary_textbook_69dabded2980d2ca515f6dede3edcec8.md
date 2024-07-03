# 2019 APMO 试题简析 

马康哲 ${ }^{1}$ 印展宽 ${ }^{2}$

(1. 广西师范大学附属外国语学校, 541004; 2. 浙江省杭州第十四中学, 310006)

第 31 届亚太地区数学奥林匹克于 2019 年 3 月 12 日举行. 考试时间为 4 个小时, 共 5 道题,每题 7 分.

本文给出这些题目的解答及简评. 其中第 2,5 题由马康哲整理, 第 1,3 题由印展宽整理. 第 4 题参考了 APMO 官网 [1] 的解答. 不当之处, 敬请读者批评指正.

## I. 试 题

1. $f$ 是定义在正整数上且取值为正整数的函数, 试求所有的 $f$, 满足: 对任意的正整数 $a$ 和 $b$, 使 $a^{2}+f(a) f(b)$ 能被 $f(a)+b$ 整除.
2. $m$ 是正整数, 数列 $a_{n}$ 定义如下

$$
a_{n+1}=\left\{\begin{array}{ll}
a_{n}^{2}+2^{m} & \text { 当 } a_{n}<2^{m} \\
\frac{a_{n}}{2} & \text { 当 } a_{n} \geq 2^{m}
\end{array},\right.
$$

其中 $a_{1}$ 是正整数. 试求所有的 $a_{1}$, 使得数列 $a_{n}$ 的所有项都是整数.

3. 三条边各不相等的 $\triangle A B C$ 内接于圆 $\Gamma . B C$ 的中点为 $M, P$ 点 (动点)在线段 $A M$ 上. $\odot(B P M)$ 与 $\odot(C P M)$ 分别再次与圆 $\Gamma$ 交于点 $D$ 和点 $E$. 直线 $D P$ 再次交 $\odot(C P M)$ 于 $X$, 直线 $E P$ 再次交 $\odot(B P M)$ 于 $Y$. 证明: 不依赖于 $P$ 的选取, $\triangle A X Y$ 的外接圆经过异于点 $A$ 的一定点 $T$.
4. 对于 $2018 \times 2019$ 的方格, 每个格子里写着一个整数, 对于每个格子, 与它有公共边的别的格子称之邻居, 考虑下面的操作: 任意选择几个格子, 计算出格子的邻居的数的平均值, 然后将这些值替换进格子. 能否做到: 不管最初的情况如何, 总能在有限次操作后, 使得所有格子里的数都相等?

修订日期: 2019-10-13.
5. $f$ 是定义在实数上且取值为实数的函数, 求所有的 $f$, 使得: 对任意实数 $x$ 和 $y$, 满足

$$
f\left(x^{2}+f(y)\right)=f(f(x))+f\left(y^{2}\right)+2 f(x y) .
$$

## II . 解答与评注

1. $f$ 是定义在正整数上且取值为正整数的函数, 试求所有的 $f$, 满足: 对任意的正整数 $a$ 和 $b$, 使 $a^{2}+f(a) f(b)$ 能被 $f(a)+b$ 整除.

证法一 首先我们令 $a=1, b=1$, 有 $f(1)+1 \mid 1+f(1)^{2}$, 故只能有 $f(1)=1$.

我们再令 $a=1$, 有

$$
f(1)+b|1+f(1) f(b) \Rightarrow 1+b| 1+f(b)
$$

故 $1+f(b) \geq 1+b$, 即 $f(b) \geq b$.

我们再令 $b=1$, 有

$$
f(a)+1\left|a^{2}+f(a) f(1) \Rightarrow f(a)+1\right| a^{2}+f(a) \Rightarrow f(a)+1 \mid a^{2}-1,
$$

故 $f(a)+1 \leq a^{2}-1$ 即 $f(a) \leq a^{2}-2(a \geq 2)$.

我们再令 $p$ 为任意奇质数, 令 $a=p, b=f(p)$, 则有 $2 f(p) \mid p^{2}+f(p) f(f(p))$,故必须有 $f(p) \mid p^{2}$,所以只可能为 1 或 $p$ 或 $p^{2}$, 又 $p \leq f(p) \leq p^{2}-2$, 故 $f(p)=p$.

再令 $a=p$, 有

$$
f(p)+b\left|p^{2}+f(p) f(b) \Rightarrow p+b\right| p^{2}+p f(b) \Rightarrow p+b \mid p(f(b)-b) .
$$

因为要对任意 $b$ 成立, 我们取 $(b, p)=1$, 则必须有 $p+b \mid f(b)-b$, 我们可以取充分大的 $p$, 故 $f(b)-b=0$, 即 $f(b)=b$.

证法二 我们发现 $f(x)=x$ 是一个解, 下面证明这是唯一解. 先令 $a=b=1$,则有

$$
f(1)+1\left|f(1)^{2}+1 \Leftrightarrow f(1)+1\right| f(1)^{2}+1-(f(1)+1)(f(1)-1)=2,
$$

又知 $f: \mathbb{N}^{+} \rightarrow \mathbb{N}^{+}$, 故 $f(1)+1 \geq 2$, 又 $f(1)+1 \leq 2$, 故 $f(1)=1$.

若结论对于 $x$ 成立, 则令 $(a, b)=(x, x+1)$, 有

$$
f(x)+x+1\left|f(x) f(x+1)+x^{2} \Leftrightarrow 2 x+1\right| x f(x+1)+x^{2} .
$$

易知 $(x, 2 x+1)=1$, 从而有

$$
2 x+1 \mid f(x+1)+x .
$$

再令 $(a, b)=(x+1, x)$, 有

$$
f(x+1)+x\left|f(x+1) f(x)+(x+1)^{2} \Leftrightarrow f(x+1)+x\right| x f(x+1)+(x+1)^{2} .
$$

从而有 $f(x+1)+x \mid x f(x+1)+(x+1)^{2}-x(f(x+1)+x)=2 x+1$. 即

$$
f(x+1)+x \mid 2 x+1 .
$$

由(1)(2)两式可见 $f(x+1)=x+1$, 故结论对于 $x+1$ 也成立, 故结论对于所有正整数成立.

评注 作为第一题, 这道题很常规也很简单. 证法一主要是先规定出的上下界, 从而用整除关系得到结论. 证法二也是自然的归纳法, 在对 $a, b$ 分别进行代换后便不难得到结论。
2. $m$ 是正整数, 数列 $a_{n}$ 定义如下

$$
a_{n+1}=\left\{\begin{array}{ll}
a_{n}^{2}+2^{m} & \text { 当 } a_{n}<2^{m} \\
\frac{a_{n}}{2} & \text { 当 } a_{n} \geq 2^{m}
\end{array},\right.
$$

其中 $a_{1}$ 是正整数. 试求所有的 $a_{1}$, 使得数列 $a_{n}$ 的所有项都是整数.

解法一 我们来证明 $m=2$ 是使满足题意的唯一值, 此时 $a_{1}=2^{l}(l \geq 1)$ 是唯一解.

对于整数 $m$ 与 $a_{1}$, 设数列的每一项皆为整数. 记 $a_{i}=b_{i} 2^{c_{i}}$, 其中 $b_{i}$ 为 $a_{i}$ 的最大奇因子, $c_{i}$ 为非负整数.

引理 $12^{m}$ 是数列 $b_{1}, b_{2}, \cdots$ 的上界.

证明 假设不存在上界, 取使 $c_{i}$ 最小且 $b_{i}>2^{m}$ 的下标, 由于 $a_{i} \geq b_{i}>2^{m}$,我们有 $a_{i+1}=\frac{a_{i}}{2}$, 因此 $b_{i+1}=b_{i}>2^{m}$ 且 $c_{i+1}=c_{i}-1<c_{i}$, 与 $c_{i}$ 最小矛盾.

引理 $2 b_{1}, b_{2}, \cdots$ 为非递减数列.

证明 若 $a_{i} \geq 2^{m}$, 我们有 $a_{i+1}=\frac{a_{i}}{2}$, 因此 $b_{i+1}=b_{i}$.

若 $a_{i}<2^{m}$,

$$
a_{i+1}=a_{i}^{2}+2^{m}=b_{i}^{2} 2^{2 c_{i}}+2^{m},
$$

则有以下三种情况:

(1) 若 $2 c_{i}>m$ 则 $a_{i+1}=2^{m}\left(b_{i}^{2} 2^{2 c_{i}-m}+1\right)$, 因此 $b_{i+1}=b_{i}^{2} 2^{2 c_{i}-m}+1>b_{i}$.

(2) 若 $2 c_{i}<m$, 则 $a_{i+1}=2^{2 c_{i}}\left(b_{i}^{2}+2^{m-2 c_{i}}\right)$, 因此 $b_{i+1}=b_{i}^{2}+2^{m-2 c_{i}}>b_{i}$.

(3) 若 $2 c_{i}=m$, 则 $a_{i+1}=2^{m+1} \cdot \frac{b_{i}^{2}+1}{2}$, 又因为 $b_{i}^{2}+1 \equiv 2(\bmod 4)$, 因此 $b_{i+1}=\frac{b_{i}^{2}+1}{2} \geq b_{i}$.

结合两个引理, 可得 $b_{1}, b_{2}, \cdots$ 在剔除前若干个有限项后为一常数数列. 固
定下标 $j$ 满足对于所有 $k \geq j$ 有 $b_{k}=b_{j}$, 由于 $a_{n} \geq 2^{m}$ 时 $a_{n}$ 递减为 $\frac{a_{n}}{2}$, 则数列中存在无穷多项小于 $2^{m}$. 因此, 我们可选一个下标 $i>j$ 满足 $a_{i}<2^{m}$. 由引理 2 的证明, $a_{i}<2^{m}$ 且 $b_{i+1}=b_{i}$ 同时成立当且仅当 $2 c_{i}=m$ 且 $b_{i+1}=b_{i}=1$. 根据引理 $2, b_{1}, b_{2}, \cdots$ 每一项均为 1 且 $a_{1}, a_{2}, \cdots$ 均为 2 的次幂. 以 $a_{i}=2^{c_{i}}=2^{\frac{m}{2}}<2^{m}$起始陆续写下之后的项,

$$
2^{\frac{m}{2}} \rightarrow 2^{m+1} \rightarrow 2^{m} \rightarrow 2^{m-1} \rightarrow 2^{2 m-2}+2^{m}
$$

注意到最后一项为 2 的幂当且仅当 $2 m-2=m$, 即 $m$ 只能等于 2 . 当 $m=2$ 且 $a_{1}=2^{l}(l \geq 1)$, 数列的项以 $2,8,4,2, \cdots$ 循环; 当 $m=2$ 且 $a_{1}=1$, 数列的前几项为 $1,5, \frac{5}{2}$, 不满足题意.

解法二 $m=2$ 时, $a_{1}$ 可以取 $2^{s}, \forall s \in \mathbb{N}^{+}$;

$m \neq 2$ 时, 不存在符合要求的. 理由如下:

假设对 $n$ 存在这样的 $a_{1}$, 则我们取该符合条件的序列 $\left\{a_{n}\right\}$, 有: 对 $\forall n \in \mathbb{N}^{+}$,定义函数 $\alpha(n)$ 为二进制表示的最低数位, 为 $\beta(n)$ 二进制表示的最高数位(事实上, $\alpha(n)=v_{2}(n), \beta(n)$ 为满足 $2^{t} \leq n<2^{t+1}$ 的唯一整数 $\left.t\right)$.

定义 $\theta(n)=\beta(n)-\alpha(n)$. 我们先证明如下 4 个引理:

引理 $1\left\{a_{n}\right\}$ 中无奇数项.

证明 若存在 $n \in \mathbb{N}^{+}$, 使 $a_{n} \equiv 1(\bmod 2)$. 若 $a_{n} \geq 2^{m} \Rightarrow a_{n+1}=\frac{a_{n}}{2} \notin \mathbb{N}^{+}$,矛盾!

若 $a_{n}<2^{m} \Rightarrow a_{n+1}=a_{n}^{2}+2^{m} \equiv 1(\bmod 2) \Rightarrow a_{n+2}=\frac{a_{n}}{2} \notin \mathbb{N}^{+}$, 矛盾!

从而引理 1 成立.

引理 2 对 $\forall n \in \mathbb{N}^{+}, \alpha\left(n^{2}\right)=2 \alpha(n), \beta\left(n^{2}\right)=2 \beta(n)+1$ 或 $2 \beta(n)$.

证明 $\alpha\left(n^{2}\right)=v_{2}\left(n^{2}\right)=2 v_{2}(n)=2 \alpha(n)$.

设 $\beta(n)=t$, 则 $2^{t} \leq n<2^{t+1} . \Rightarrow 2^{2 t} \leq n^{2}<2^{2 t+2} \Rightarrow 2^{2 t} \leq n^{2}<2^{2 t+1}$ 或 $2^{2 t+1} \leq n^{2}<2^{2 t+2} \Rightarrow \beta\left(n^{2}\right)=2 t$ 或 $2 t+1$. 故引理 2 得证.

引理 3 对 $\forall n \in \mathbb{N}^{+}, \theta(n)=\theta(2 n)$.

证明 有

$$
\alpha(2 n)=v_{2}(2 n)=v_{2}(n)+1=\alpha(n)+1 .
$$

设 $\beta(n)=t \Rightarrow 2^{t} \leq n<2^{t+1} \Rightarrow 2^{t+1} \leq 2 n<2^{t+2}$. 则

$$
\beta(2 n)=t+1=\beta(n)+1 .
$$

(1)(2)两式相减, 可知: $\theta(2 n)=\beta(2 n)-\alpha(2 n)=\beta(n)-\alpha(n)=\theta(n)$. 故引理 3 得证.
引理 $4 \forall m, n \in \mathbb{N}^{+}, n<2^{m}, \theta\left(n^{2}+2^{m}\right) \geq 2 \theta(n)-1$.

证明 若 $n^{2}, 2^{m}$ 的二进制加法下不产生进位(即 $n^{2}$ 第 $m$ 位为 0 ).

$\Rightarrow \theta\left(n^{2}+2^{m}\right) \geq \theta\left(n^{2}\right)=\beta\left(n^{2}\right)-\alpha\left(n^{2}\right) \geq 2 \beta(n)-2 \alpha(n)=2 \theta(n)>2 \theta(n)-1$.

结论成立.

若 $n^{2}, 2^{m}$ 的二进制加法产生进位, 此时必有 $\alpha\left(n^{2}\right) \leq m$.

(I) $\alpha\left(n^{2}\right)<m \Rightarrow \alpha\left(n^{2}+2^{m}\right)=v_{2}\left(n^{2}+2^{m}\right)=\min \left\{v_{2}\left(n^{2}\right), v_{2}\left(2^{m}\right)\right\}=$ $v_{2}\left(n^{2}\right)=\alpha\left(n^{2}\right)$.

$\beta\left(n^{2}+2^{m}\right) \geq \beta\left(n^{2}\right) \Rightarrow \theta\left(n^{2}+2^{m}\right)=\beta\left(n^{2}+2^{m}\right)-\alpha\left(n^{2}+2^{m}\right) \geq \beta\left(n^{2}\right)-$ $\alpha\left(n^{2}\right) \geq 2 \beta(n)-2 \alpha(n)=2 \theta(n)>2 \theta(n)-1$. 故结论成立.

(II) $\alpha\left(n^{2}\right)=m$. 我们来证明: $n^{2}, 2^{m}$ 的加法最多进一次位.

设 $\alpha(n)=s$, 则 $m=2 \alpha(n)=2 s$. 取 $n^{\prime}=\frac{n}{2^{s}}$.

$$
\Rightarrow \alpha\left(n^{\prime 2}\right)=\alpha\left(\frac{n^{2}}{2^{2 s}}\right)=\alpha\left(n^{2}\right)-2 s=0 .
$$

其中 $n^{\prime 2}$ 是 $n^{2}$ 去掉末尾若干个 0 形成的数.

若 $n^{2}+2^{m}$ 的二进制加法进了两次位,则 $n^{\prime 2}+1$ 也进了两次位. $\Rightarrow n^{\prime 2}$第 0 位、第 1 位均为 $1 \Rightarrow n^{2} \equiv 1+2 \equiv-1(\bmod 4)$, 矛盾(由对 $\forall n \in \mathbb{N}^{+}$, $\left.n^{2} \equiv 0,1(\bmod 4)\right)$ ! 从而 $n^{2}+2^{m}$ 的二进制加法最多进一次位 $\Rightarrow \alpha\left(n^{2}+2^{m}\right) \leq$ $\alpha\left(n^{2}\right)+1 . \Rightarrow \theta\left(n^{2}+2^{m}\right)=\beta\left(n^{2}+2^{m}\right)-\alpha\left(n^{2}+2^{m}\right) \geq \beta\left(n^{2}\right)-\alpha\left(n^{2}\right)-1=$ $2 \theta(n)-1$.

故结论成立. 引理 4 得证.

回到原题. 由引理 1 , 对 $\forall n \in \mathbb{N}^{+}, \alpha\left(a_{n}\right) \geq 1$. 将数列 $\left\{a_{n}\right\}$ 中所有满足 $a_{n}<2^{m}$ 的项顺次取出组成数列 $\left\{b_{n}\right\}_{n=1}^{+\infty}$. 则对 $\forall n \in \mathbb{N}^{+}$,

$$
\theta\left(b_{n}\right)=\beta\left(b_{n}\right)-\alpha\left(b_{n}\right)<m-1 .
$$

设 $b_{n}$ 对应原序列 $\left\{a_{n}\right\}$ 中的项为 $a_{n^{\prime}}$. 则对 $\forall n_{0}{ }^{\prime}+1 \leq n \leq\left(n_{0}+1\right)^{\prime}$, $\theta\left(a_{n}\right)=\theta\left(a_{n+1}\right)\left(\right.$ 因为 $a_{n+1}=2 a_{n}$, 由引理 3 可得). $\Rightarrow \theta\left(b_{n+1}\right)=\theta\left(a_{(n+1)^{\prime}}\right)=$ $\theta\left(a_{n^{\prime}+1}\right)=\theta\left(a_{n^{\prime}}^{2}+2^{m}\right) \geq 2 \theta\left(a_{n^{\prime}}\right)-1=2 \theta\left(b_{n}\right)-1$ (由引理 4$)$.

若 $\exists N \in \mathbb{N}^{+}$, 使 $\theta\left(b_{N}\right)>1 \Rightarrow \theta\left(b_{N+1}\right) \geq 2 \theta\left(b_{N}\right)-1>\theta\left(b_{N}\right)>1$.

归纳易知:对 $\forall n \geq N$ 均有: $\theta\left(b_{n+1}\right)>\theta\left(b_{n}\right)$.

由整数的离散性知: $\theta\left(b_{N+m-1}\right)>m$, 与(3)矛盾! 故对 $\forall n \in \mathbb{N}^{+}, \theta\left(b_{n}\right) \leq$ $1 \Rightarrow$ 对 $\forall n \in \mathbb{N}^{+}, \theta\left(a_{n}\right) \leq 1$.

若存在一个项 $b_{n}$ 使: $\theta\left(b_{n}\right)=1 \Rightarrow \theta\left(a_{n^{\prime}}\right)=1$.
设 $a_{n^{\prime}}=2^{t-1}+2^{t}, t \in \mathbb{N}^{+}$.

$$
\Rightarrow a_{n^{\prime}+1}=\left(2^{t-1}+2^{t}\right)^{2}+2^{m}=2^{2 t+1}+2^{2 t-2}+2^{m} .
$$

若 $m=2 t-2$, 则: $\theta\left(a_{n^{\prime}+1}\right)=\theta\left(2^{2 t-1}+2^{2 t+1}\right)=2$. 若 $m \neq 2 m-2$, 则: $\theta\left(a_{n^{\prime}+1}\right) \geq$ $(2 t+1)-(2 t-2)=3$. 均与 $(*)$ 矛盾!

故对 $\forall n \in \mathbb{N}^{+}, \theta\left(b_{n}\right)=0 \Rightarrow \forall n \in \mathbb{N}^{+}, \theta\left(a_{n}\right)=0$.

设 $b_{n}=2^{s}, s<m \Rightarrow a_{n^{\prime}}=2^{s} \Rightarrow a_{n^{\prime}+1}=2^{2 s}+2^{m}$. 由 $\theta\left(a_{n^{\prime}+1}\right)=0 \Rightarrow 2 s=$ $m \Rightarrow a_{n^{\prime}+1}=2^{m+1} \geq 2^{m} \Rightarrow a_{n^{\prime}+2}=2^{m} \geq 2^{m} \Rightarrow a_{n^{\prime}+3}=2^{m-1}<2^{m} \Rightarrow a_{n^{\prime}+4}=$ $2^{2 m-2}+2^{m}$.

由 $\theta\left(a_{n^{\prime}+4}\right)=0 \Rightarrow 2 m-2=m \Rightarrow m=2$.

这表明, 若 $m \neq 2$, 则不存在满足要求的数列 $\left\{a_{n}\right\}$, 更不存在符合要求的 $a_{1}$.

若 $m=2$, 由上述, $a_{1}$ 只能取 $2^{s}, \forall s \in \mathbb{N}^{+}$. 同时当 $a_{1}=2^{s}, \forall s \in \mathbb{N}^{+}$时, 可以得到: $a_{n}=2^{s+1-n}, \forall 1 \leq n \leq s$,而 $n \geq s+1$ 时, $\left\{a_{n}\right\}$ 形成 2,4 的循环序列.

综上, $m=2$ 时, $a_{1}$ 可以取 $2^{s}, \forall s \in \mathbb{N}^{+} ; m \neq 2$ 时,不存在符合要求的 $a_{1}$.

评注 这题的解答虽然很长, 但是难度并不高, 证法一是官网的解答, 证法二考察 $a_{n}$ 的二进制表示, 注意到 $\alpha(n), \beta(n), \theta(n)$ 与 $a_{n}$ 递推变化联系的规律性, 则很容易给出解答.

3. 三条边各不相等的 $\triangle A B C$ 内接于圆 $\Gamma . B C$ 的中点为 $M, P$ 点 (动点)在线段 $A M$ 上. $\odot(B P M)$ 与 $\odot(C P M)$ 分别再次与圆 $\Gamma$ 交于点 $D$ 和点 $E$. 直线 $D P$ 再次交 $\odot(C P M)$ 于 $X$, 直线 $E P$ 再次交 $\odot(B P M)$ 于 $Y$. 证明: 不依赖于 $P$ 的选取, $\triangle A X Y$ 的外接圆经过异于点 $A$ 的一定点 $T$.

## 证法一 (印展宽)

延长 $D P$ 和 $E P$ 交 $\Gamma$ 于 $F$ 和 $G$, 设 $G F$ 与 $B C$ 交于 $Q$. 设 $\odot(A X Y)$ 与 $\Gamma$交于点 $T$, 下面我们证明 $T$ 是定点.

首先有 $\angle C F D=\angle C B D=\angle D P M$, 故 $P M / / C F$. 同理, $B G / / P M$. 由 $\angle X C B=\angle D P M=\angle D F C$, 故 $Q F$ 与 $\odot(B Y G)$ 相切. 同理, $Q F$ 与 $\odot(B Y G)$相切. 又由 $\angle Q G B=\angle Q C F=\angle Q B G$, 故 $Q F$ 与 $\odot(B Y G)$ 相切. 同理, $Q F$ 与 $\odot(C F X)$ 相切.

故 $Q$ 为 $\odot(B Y G)$ 与 $\odot(C F X)$ 的外位似中心. 易知 $\odot(B Y G)$ 与 $\odot(C F X)$为定圆, 故 $Q$ 为定点. 因为 $B G / / P M / / C F, B M=C M$, 所以 $A M$ 为 $\odot(B Y G)$与 $\odot(C F X)$ 的根轴. 于是有 $P Y \cdot P G=P X \cdot P F$, 故 $F G Y X$ 四点共圆.



因为 $A M$ 也是 $\odot(B P M)$ 与 $\odot(C P M)$ 的根轴, 故对 $\odot(B Y G), \odot(B P M)$, $\odot(C F X)$ 和 $\odot(B P M), \odot(C P M), \odot(C F X)$ 分别使用蒙日定理知 $B Y, P M, C X$共点.

设该点为 $H$. 故有 $H Y \cdot H B=H P \cdot H M=H X \cdot H C$, 于是 $B C X Y$ 四点共圆. 再对 $\odot(G F X), \odot(B C Y), \Gamma$ 用蒙日定理知 $G F, B C, X Y$ 共点.

故 $Q, X, Y$ 共线. 再对 $\odot(A X Y), \odot(B C X)$, $\Gamma$ 用蒙日定理知 $A T, X Y, B C$ 共点. 故 $A T$ 经过定点 $Q$, 故 $T$ 是一个定点.

## 证法二 (马康哲)

首先有 $\angle B D P=\angle P M C=\angle C X P$, 故 $B D / / C X$. 同理, $B Y / / C E$.

延长 $B D$ 交 $C E$ 于 $P_{1}, C X$ 交 $B Y$ 于 $P_{2}$, 由蒙日定理知 $P_{1}$ 在 $A M$ 上,同时易知四边形 $P_{1} B P_{2} C$ 为平行四边形. 从而可得 $P_{1}, M, P_{2}$ 三点共线, 亦即 $P_{1}, M, P_{2}, A, P$ 五点共线.

于是有 $P_{2} X \cdot P_{2} C=P_{2} M \cdot P_{2} P=P_{2} Y \cdot P_{2} B$, 故 $B, C, X, Y$ 四点共圆. 于是又由蒙日定理, 知 $A T, X Y, B C$ 交于一点, 设该点为 $S$. 故只需证 $S$ 是定点,也就是证明 $X Y$ 交 $B C$ 于一定点 $S$.

再设 $E P$ 交 $\Gamma$ 于 $K$, 则根据证法一中的结论有 $B K / / A M$. 同理, 对 $C$ 也作出这样的点 $N$. 注意到 $K N$ 和 $B C$ 的交点显然是定点, 故由蒙日定理知只需证 $K Y N X$ 共圆.



延长 $B Y$ 交 $\Gamma$ 于 $S_{1}, C X$ 交 $\Gamma$ 于 $S_{2}$. 有

$$
\angle C S_{2} S_{1}=180^{\circ}-\angle Y B M=180^{\circ}-\angle Y X S_{2}
$$

故 $S_{1} S_{2} / / X Y$. 由前述知弧 $D S_{1}$ 等于弧 $E S_{2}$, 于是 $S_{1} S_{2} / / D E$, 故 $D E / / X Y$.

所以有 $\angle K N D=\angle K E D=\angle E Y X$, 故有 $\angle Y K N=\angle Y X N$, 故 $K Y N X$共圆. 所以 $K N, B C, A T$ 交于一定点 $S$, 故 $A T$ 过定点 $S$, 故 $T$ 为定点.

评注 笔者认为该题是一道较难的几何题, 第一步的难点在于画图, 图中的 $D$与 $E$ 如果 $P$ 点位置选取不当则很难在图上作出. 定点较为容易找到,找与已知定点 $A$ 相关的点往往是做这类题的常见套路,接下来涉及对于 $T$ 的刻画, 这一步的蒙日定理不难想到,然后命题就转化为证明 $B C X Y$ 共圆.根据画图不难发现 $D X$ 和 $E Y$ 与 $\Gamma$ 的交点 $F, G$ 都是定点, 故想到用这两个点对根心 $Q$ 进行刻画. 取出 $\odot(B Y G)$ 与 $\odot(C F X)$ 的这一步又是一个难点, 但取出后可以将中点的条件转化为根轴, 并且可以发现 $Q$ 为这两个圆的外位似中心, 这样就完成了对于 $Q$ 的刻画,接下来的步骤对于熟悉圆幂的同学不难完成。

证法二中先想到用易知的两组平行从而将中点的条件转化为平行四边形, 再由根心的性质就可以证明 $B C X Y$ 共圆, 进而也选择了蒙日定理对 $T$ 进行刻画. 后面也需要发现 $D X$ 和 $E Y$ 与 $\Gamma$ 的交点都是定点,然后选择用证明共圆.

另外, 西北工大附中的杜俊辰同学在纯几何吧里提出了另一种关于根心 $Q(S)$ 的刻画, 需要用到如下引理, 有兴趣的读者不妨一试:



设 $\odot O_{1}$ 与 $\odot O_{2}$ 的外位似中心为 $P$, 一条外公切线为 $A B, C \neq A$ 在 $\odot O_{1}$上, $D \neq B$ 在 $\odot O_{2}$ 上, $A C$ 交 $B D$ 于 $Q$, 则以下三个结论等价:

(1) $Q$ 在根轴上;(2) $C, D$ 为逆对应点;(3) $\triangle Q C D$ 的外接圆与 $\odot O_{1}, \odot O_{2}$ 均相切.

4. 对于 $2018 \times 2019$ 的方格, 每个格子里写着一个整数, 对于每个格子, 与它有公共边的别的格子称之邻居,考虑下面的操作: 任意选择几个格子,计算出格子的邻居的数的平均值, 然后将这些值替换进格子. 能否做到: 不管最初的情况如何, 总能在有限次操作后, 使得所有格子里的数都相等?

解 在构造方格表之前, 我们先来定义分数 $\frac{a}{b}$, 其中 $b$ 不能被 5 整除, $(a, b)=1$.

由于 $b$ 不能被 5 整除, 故 $b$ 在 $\bmod 5$ 意义下必有数论倒数 $b^{\prime}$. 我们定义 $\frac{a}{b} \equiv a \cdot b^{\prime}(\bmod 5)$. 我们给出如下构造:

由于 $2|2018,3| 2019$, 故我们可以将这个方格表划分为 $\frac{2018}{2} \times \frac{2019}{3}$ 个方格表, 记第 $i$ 行第 $j$ 列的方格表为表 $(i, j)$.

我们在表 $(2 k, j), k \in\left[1, \frac{2018}{4}\right], j \in\left[1, \frac{2019}{3}\right], k \in \mathbb{N}, j \in \mathbb{N}$ 内填入 $\left[\begin{array}{l}020 \\ 313\end{array}\right]$,在表 $(2 k-1, j), k \in\left[1, \frac{2020}{4}\right], j \in\left[1, \frac{2019}{3}\right], k \in \mathbb{N}, j \in \mathbb{N}$ 内填入 $\left[\begin{array}{l}313 \\ 020\end{array}\right]$.

下面我们证明, 这个方格表内的每个数在 $\bmod 5$ 意义下保持不变. 设 $i$ 经操作过后的数为 $M_{i}$.

(I) 方格表内的 0 .

按照方格表的定义,其邻居只可能为: $\{0,0,2,3\},\{0,2,3\},\{2,3\}$.
对于第一种情形, 操作后的数:

$$
M_{0} \equiv \frac{0+0+2+3}{4} \equiv 5 \cdot 4^{-1} \equiv 0(\bmod 5)
$$

对于第二种情形, 操作后的数:

$$
M_{0} \equiv \frac{0+2+3}{3} \equiv 5 \cdot 3^{-1} \equiv 0(\bmod 5) .
$$

对于第三种情形, 操作后的数:

$$
M_{0} \equiv \frac{2+3}{2} \equiv 5 \cdot 2^{-1} \equiv 0(\bmod 5) .
$$

从而经过操作之后 0 在意义下的数仍是 0 保持不变.

(II) 方格表内的 1 .

按照方格表的定义, 其邻居只可能为: $\{1,2,3,3\},\{2,3,3\}$.

对于第一种情形, 操作后的数:

$$
M_{0} \equiv \frac{1+2+3+3}{4} \equiv 9 \cdot 4^{-1} \equiv 1(\bmod 5) .
$$

对于第二种情形,操作后的数:

$$
M_{0} \equiv \frac{2+3+3}{3} \equiv 8 \cdot 3^{-1} \equiv 1(\bmod 5) .
$$

从而经过操作之后 1 在 $\bmod 5$ 意义下保持不变.

(III) 方格表内的 3 .

按照方格表的定义,其邻居只可能为: $\{3,3,1,0\},\{0,1,3\},\{0,1\}$.

对于第一种情形, 操作后的数:

$$
M_{0} \equiv \frac{3+3+1+0}{4} \equiv 7 \cdot 4^{-1} \equiv 3(\bmod 5) .
$$

对于第二种情形, 操作后的数:

$$
M_{0}=\frac{3+1+0}{3} \equiv 4 \cdot 3^{-1} \equiv 3(\bmod 5) .
$$

对于第三种情形, 操作后的数:

$$
M_{0} \equiv \frac{0+1}{2} \equiv 1 \cdot 2^{-1} \equiv 3(\bmod 5) .
$$

从而经过操作之后 3 在 $\bmod 5$ 意义下保持不变.

(IV) 方格表内的 2.

按照方格表的定义,其邻居只可能为: $\{0,0,1,2\},\{0,0,1\}$.

对于第一种情形, 操作后的数:

$$
M_{0} \equiv \frac{0+0+1+2}{4} \equiv 3 \cdot 4^{-1} \equiv 2(\bmod 5) .
$$

对于第二种情形, 操作后的数:

$$
M_{0}=\frac{0+0+1}{3} \equiv 1 \cdot 3^{-1} \equiv 2(\bmod 5) .
$$

从而经过操作之后 2 在 $\bmod 5$ 意义下保持不变.

综合上述 4 种情况, 方格表内的每个数均在 $\bmod 5$ 意义下保持不变. 由于 $a \neq \equiv b(\bmod 5) \Rightarrow a \neq b$, 故该方格表不可能在有限步操作之后每个数均变为相同的数,故答案是否定的.

评注 本题是五道题内最困难的一道题, 全场无人做出 (全场仅有一个人得分, 且为 1 分）.由于方格表的操作过程中会出现分数, 所以很容易让人否决数论的方法, 而考虑一些代数分析的方法, 而这样的方法在这个地方使用显得过于苛刻, 因为条件没有提供相应的信息. 若要在考场上做出此题, 就需要马上意识到要用数论的方法处理此题, 并关注到可能出现的系数数论上的特征(分母的素因子只可能为 2,3$)$, 及时想到构造意义下的方格表构造 $(p \geq 2,3)$. 而这个想法又显得非常大胆, 有此胆识不是件容易的事情.
5. $f$ 是定义在实数上且取值为实数的函数, 求所有的 $f$, 使得: 对任意实数 $x$ 和 $y$, 满足

$$
f\left(x^{2}+f(y)\right)=f(f(x))+f\left(y^{2}\right)+2 f(x y) .
$$

## 解 (马康哲)

令 $x=y=0$, 有 $f(f(0))=f(f(0))+f(0)+2 f(0)$ 可知 $f(0)=0$.

令 $x=0$, 有

$$
f(f(y))=f\left(y^{2}\right)
$$

故原方程可化为:

$$
f\left(x^{2}+f(y)\right)=f\left(x^{2}\right)+f\left(y^{2}\right)+2 f(x y) .
$$

设(2)式为 $P(x, y)$, 考虑 $P(y, x)$ 还可以得到: $f\left(y^{2}+f(x)\right)=f\left(x^{2}+f(y)\right)$. 将 $x$ 换为 $-x$ 容易得到这个函数为偶函数. 下面我们分两种情况讨论:

情形 $1 . f$ 存在除 0 以外的零点, 设为 $t$, 则令 $y=t$, 有:

$$
f\left(x^{2}\right)=f\left(x^{2}+f(t)\right)=f(f(x))+f\left(t^{2}\right)+2 f(x t) .
$$

故有 $f\left(t^{2}\right)+2 f(x t)=0$. 此时令 $x=0$ 容易得到 $f\left(t^{2}\right)=0$, 代回上式可知 $f(x t)=0$. 由于 $t \neq 0$, 故 $x t$ 遍历 $\mathbb{R}$, 故此时 $f(x)=0$.

情形 $2 . f$ 仅有 0 一个零点. 我们先证明几个结论:

结论 1: $f(x f(1))=f(x)$.
在(1)式中令 $y=1$ 有:

$$
f(f(1))=f(1)
$$

令 $y=f(1)$ 有

$$
f\left(f(1)^{2}\right)=f(f(f(1)))=f(f(1))=f(1) .
$$

考虑 $P(x, 1)$, 有:

$$
f\left(x^{2}+f(1)\right)=f\left(x^{2}\right)+f(1)+2 f(x) .
$$

考虑 $P(x, f(1))$, 有:

$$
f\left(x^{2}+f(f(1))\right)=f\left(x^{2}\right)+f\left(f(1)^{2}\right)+2 f(x f(1)) .
$$

由(3), (4)两式, 该式可化为:

$$
f\left(x^{2}+f(1)\right)=f\left(x^{2}\right)+f(1)+2 f(x f(1)) .
$$

(5), (6)两式对比可得: $f(x f(1))=f(x)$.

结论 2: $f\left(x^{2}+f(1)\right)=f\left(x^{2} f(1)+1\right)$

考虑 $P(x, 1)$, 有:

$$
f\left(x^{2}+f(1)\right)=f\left(x^{2}\right)+f(1)+2 f(x) .
$$

考虑 $P(x f(1), 1)$, 有:

$$
\begin{aligned}
f\left(x^{2} f(1)^{2}+f(1)\right) & =f\left(x^{2} f(1)^{2}\right)+f(1)+2 f(x f(1)) \\
& \left.=f\left(x^{2}\right)+f(1)+2 f(x)=f\left(x^{2}+f(1)\right)\right)
\end{aligned}
$$

同时由结论 $1, f\left(x^{2} f(1)^{2}+f(1)\right)=f\left(x^{2} f(1)+1\right)$, 从而结论 2 成立.

结论 3: 对任意 $x \neq 0, f(x)>0$.

先证明 $f(1)>0$. 反证法: 假设 $f(1)<0$, 在 $(* 2)$ 式中令 $x=\sqrt{-f(1)}$, 则有

$$
f\left(-f(1)^{2}+1\right)=f(-f(1)+f(1))=0 .
$$

由于 0 为 $f$ 的唯一零点, 故 $-f(1)^{2}+1=0$, 结合 $f(1)<0$ 有 $f(1)=-1$.

考虑 $P(1,1)$ 有

$$
f(1+f(1))=4 f(1) .
$$

将 $f(1)=-1$ 代入上式的 $f(1)=0$, 矛盾. 从而 $f(1)>0$.

由偶函数性质我们不妨设存在 $s>0$, 使 $f(s)<0$. 同理, 我们考虑 $P(f(1) \sqrt{-f(s)}, s), P(\sqrt{-f(s)}, s)$ 即得到

$$
-f(1)^{2} f(s)+f(s)=0,
$$

可知 $f(1)=1$. 下面我们来证明 $f$ 在 $\mathbb{R}^{+}$上是单射.

反证法: 假设存在 $u>v>0$, 使得 $f(u)=f(v)$, 那么由于

$4 f\left(u^{2}\right)=f\left(u^{2}+f(u)\right)=f\left(u^{2}+f(v)\right)=f\left(v^{2}+f(u)\right)=f\left(v^{2}+f(v)\right)=4 f\left(v^{2}\right)$,可推知 $f\left(u^{2}\right)=f\left(v^{2}\right)$.

考虑 $P(x, u), P(x, v)$, 容易得到: $f(x u)=f(x v)$.

令 $a=\frac{u}{v}>1$, 则上述条件表明 $f(x)=f(a x)$.

不妨设 $a>\sqrt{2}$, 因为若 $a<\sqrt{2}$, 可以取充分大的 $k$ 使 $a^{k}>\sqrt{2}$, 并用 $a^{k}$ 取代 $a$.

令 $x=1$ 有 $f(a)=f(1)=1$, 令 $x=a$ 有 $f\left(a^{2}\right)=f(a)=1$.

考虑 $P(x, 1), P(a x, 1)$ 容易得到 $f\left(x^{2}+1\right)=f\left(a^{2} x^{2}+1\right)=f\left(x^{2}+\frac{1}{a^{2}}\right)$. 令 $x=\sqrt{a^{2}-2}$ 有:

$$
f\left(a^{2}-1\right)=f\left(a^{2}-2+\frac{1}{a^{2}}\right)=f\left(a^{4}-2 a^{2}+1\right)=f\left(\left(a^{2}-1\right)^{2}\right)
$$

考虑 $P(x, 1), P\left(\frac{x}{a}, 1\right)$ 容易得到

$$
f\left(x^{2}+1\right)=f\left(\frac{x^{2}}{a^{2}}+1\right)=f\left(x^{2}+a^{2}\right) .
$$

令 $x=a^{2}-1$ 有: $f\left((a-1)^{2}+1\right)=f\left(\left(a^{2}-1\right)^{2}+a^{2}\right)=f\left(a^{4}-a^{2}+1\right)$. 令 $x=\sqrt{a^{4}-a^{2}}$ 有:

$$
f\left(a^{4}-a^{2}+1\right)=f\left(a^{4}-a^{2}+a^{2}\right)=f\left(a^{4}\right)=f\left(a^{3}\right)=f\left(a^{2}\right)=f(a)=1 .
$$

从而 $f\left((a-1)^{2}+1\right)=1$.

再考虑 $P\left(a^{2}-1,1\right)$, 有:

$$
1=f\left((a-1)^{2}+1\right)=f\left(\left(a^{2}-1\right)^{2}\right)+f(1)+2 f\left(a^{2}-1\right),
$$

故 $f\left((a-1)^{2}\right)+2 f\left(a^{2}-1\right)=0$.

将(8)式代入得: $f\left(a^{2}-1\right)=0$, 从而 $a^{2}-1=0, a=-1$ 或 1 , 与 $a>1$ 矛盾!故 $f$ 在 $\mathbb{R}^{+}$上是单射.

结合 $f(f(x))=f\left(x^{2}\right)$, 有 $f(-f(s))=f(f(s))=f(s)$. 由于 $f(s)<0$, 有 $-f(s)>0$, 由于 $s^{2}>0$, 结合上述单射结论有 $f(s)=-s^{2}$. 考虑 $P(s, s)$ 有: $0=f\left(s^{2}-s^{2}\right)=4 f\left(s^{2}\right)$, 从而 $f\left(s^{2}\right)=0$, 故 $s=0$, 矛盾 ! 综上结论 3 得证 $!$

回到原题, 我们再来证明 $f$ 在 $\mathbb{R}^{+}$上是单射.

由结论 $3, x \neq 0$ 时

$$
f\left(x^{2}+f(y)\right)=f\left(x^{2}\right)+f\left(y^{2}\right)+2 f(x y)>f\left(y^{2}\right)=f(f(y)) .
$$

假设存在 $u>v>0, f(u)=f(v)$, 与结论 3 中的证明同理, 可知 $f(x u)=f(x v)$,
任取 $s>0$, 则 $f(s)>0$, 取 $x=\frac{f(s)}{v}$, 得到

$$
f\left(\frac{u f(s)}{v}\right)=f(f(s)) .
$$

然而在(9)式中令 $x=\sqrt{\left(\left(\frac{u}{v}-1\right) f(s)\right)}, y=s$, 可得到 $f\left(\frac{u f(s)}{v}\right)>f(f(s))$, 这与(10 式矛盾!

从而 $f$ 在 $\mathbb{R}^{+}$上是单射, 由于 $x>0$ 时,

$$
f(f(x))=f\left(x^{2}\right), f(x)>0, x^{2}>0
$$

从而 $f(x)=x^{2}$, 由偶函数性质和 $f(0)=0$, 不难验证 $x \leq 0$ 时也有 $f(x)=x^{2}$. 从而该情形下的解为 $f(x)=x^{2}$.

综上所述, 满足条件的 $f$ 有两个: $f(x)=0$ 和 $f(x)=x^{2}$.

评注 本题是一道比较常规(中偏难)的函数方程题, 在通过一些简单的赋值之后容易猜出答案，再用一些常见的函方技巧一一尝试(比如这里在得到 $f(f(x))=f\left(x^{2}\right)$ 之后可以猜测这里需要利用单射的结论), 思维链条比较长, 但整体还是较自然的.

致谢 感谢江苏王浩杰老师给出的题目翻译. 感谢曲靖市第一中学的林斌同学和安庆一中的严仲谨同学, 他们认真审阅了本稿并提出了宝贵的修改意见.

## 参考文献

[1] APMO 官网: http://www.apmo-official.org/problems.

[2] 纯几何吧: http://tieba.baidu.com/p/6086618605?share=9105\&fr=share\&unique $=5$ C4F3AA741F0F5CA89C84AD31706B960\&st=1565421299\&clienttype $=1 \&$ client_version $=10.2 .6 \& s f c=$ copy

