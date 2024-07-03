# 数学新星网 $\%$ 学生专栏 

www.nsmath.cn/xszl

## 一次完整多项式

任建宇

(合肥市第一中学, 230601)

在 2018 年上海新星数学夏令营中, 冯跃峰老师提出了如下“完整多项式” 问题:

问题 设 $f(x)$ 为多项式, 如果对给定的正整数 $n$, 存在 $x_{0} \in \mathbb{N}$ 使

$$
f\left(x_{0}\right), f^{(2)}\left(x_{0}\right), \cdots, f^{(n)}\left(x_{0}\right)
$$

构成模 $n$ 的完系,则称 $f(x)$ 为模 $n$ 的完整多项式. 试问: 对给定的正整数 $n$, 哪些多项式 $f(x)$ 是模 $n$ 的完整多项式?

这是一个容量很大的问题. 本文解决了一次完整多项式的情形, 得到如下定理:

定理 对给定正整数 $n \geq 4$, 设 $n$ 的标准分解式为 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{r}^{\alpha_{r}}$, 则 $f(x)=a x+b\left(a, b \in \mathbb{N}^{*}\right)$ 是模 $n$ 的完整多项式当且仅当 $(b, n)=1$, 且

$$
\left\{\begin{array}{l}
a \equiv 1\left(\bmod p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \nmid n \\
a \equiv 1\left(\bmod 2 p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \mid n
\end{array} .\right.
$$

证明 原题等价于: 对给定的正整数 $n \geq 4$, 求所有正整数对 $(a, b)$, 使存在 $m \in \mathbb{N}$, 数列 $\left\{x_{k} \mid x_{1}=m, x_{l}=a x_{l-1}+b, l \geq 2\right\}$ 的前 $n$ 项构成模 $n$ 的完系.

当 $a=1$ 时, 问题等价于存在 $m \in\{1,2, \cdots, n\}$, 使 $m+b, m+2 b, \cdots, m+n b$构成模 $n$ 的完系, 这又等价于 $(b, n)=1$, 所以结论成立.

当 $a \geq 2$ 时, 易知若正整数对 $(a, b)$ 满足上述条件, 则必有 $(a, n)=1$ (否则, $(a, n)=d>1$, 则 $\left\{x_{k}\right\}$ 中除第一项外都在模 $d$ 余 $b$ 的剩余类中, 不可能构成模 $n$的完系), 故以下证明中均假设 $(a, n)=1$.

我们熟知 $(a, n)=1$ 时, $\left\{x_{k}\right\}$ 关于 $n$ 的模数列是纯周期数列, 故存在 $m \in \mathbb{N}$,[^0]数列 $\left\{x_{k} \mid x_{1}=m, x_{n}=a x_{n-1}+b\right\}$ 的前 $n$ 项构成模 $n$ 的完系等价于数列 $\left\{x_{k} \mid x_{1}=1, x_{l}=a x_{l-1}+b, l \geq 2\right\}$ 的前 $n$ 项构成模 $n$ 的完系.

下面先考虑 $b=1$ 的情形, 此时问题转化为求所有正整数 $a$,使得

$$
\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \ldots, \frac{a^{n}-1}{a-1}
$$

模 $n$ 互不同余.

(1) $n=p, p$ 为素数.

此时若正整数 $a$ 满足上述条件, 则有

$$
p \nmid \frac{a^{j}-1}{a-1}-\frac{a^{i}-1}{a-1}, \forall 1 \leq i<j \leq p,
$$

结合 $(a, p)=(a, n)=1$, 有

$$
p \nmid \frac{a^{j-i}-1}{a-1}, \forall 1 \leq i<j \leq p .
$$

又 $\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \ldots, \frac{a^{p}-1}{a-1}$ 模 $n$ 互不同余, 则只能有 $p \left\lvert\, \frac{a^{p}-1}{a-1}\right.$.

若 $a \neq \equiv 1(\bmod p)$, 则 $p \mid a^{p}-1, a \equiv a^{p} \equiv 1(\bmod p)$, 矛盾!

若 $a \equiv 1(\bmod p)$, 则易验证其满足要求.

综上, 此时正整数 $a$ 满足条件当且仅当 $a \equiv 1(\bmod p)$.

(2) $n=p^{\alpha}, p$ 为素数, $\alpha \geq 2$.

对素数 $p$, 正整数 $m$, 若 $p^{k} \mid m, p^{k+1} \nmid m$, 则记为 $v_{p}(m)=k$. 由定义易知 $m_{2} \mid m_{1}$ 时,

$$
v_{p}\left(\frac{m_{1}}{m_{2}}\right)=v_{p}\left(m_{1}\right)-v_{p}\left(m_{2}\right) .
$$

(1) $p$ 为奇素数时.

若 $a \not \equiv 1(\bmod p)$, 则由 (1) 知 $\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \ldots, \frac{a^{p}-1}{a-1}$ 无法构成模 $p$ 的完系, 更不可能构成模 $p^{\alpha}$ 的完系.

若 $a \equiv 1(\bmod p)$, 由著名的升幂定理 (即 LTE 引理), 知

$$
\begin{aligned}
v_{p}\left(\frac{a^{k}-1}{a-1}\right) & =v_{p}\left(a^{k}-1\right)-v_{p}(a-1) \\
& =v_{p}(a-1)+v_{p}(k)-v_{p}(a-1) \\
& =v_{p}(k),
\end{aligned}
$$

也即 $p^{\alpha} \left\lvert\, \frac{a^{k}-1}{a-1}\right.$ 当且仅当 $p^{\alpha} \mid k$.

故若存在 $1 \leq i<j \leq p^{\alpha}, p^{\alpha} \left\lvert\, \frac{a^{j}-1}{a-1}-\frac{a^{i}-1}{a-1}\right.$, 则 $p^{\alpha} \left\lvert\, \frac{a^{j-i}-1}{a-1}\right.$, 于是 $p^{\alpha} \mid j-i$, 与 $j-i \leq p^{\alpha}-1$ 矛盾! 从而

$$
\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \ldots, \frac{a^{p^{\alpha}}-1}{a-1}
$$

模 $p^{\alpha}$ 互不同余.

(2) $p=2$ 时.

由 $\left(a, 2^{\alpha}\right)=1$ 知 $a$ 为奇数.

若 $a \equiv 3(\bmod 4)$, 则

$$
v_{2}\left(\frac{a^{2^{\alpha-1}}-1}{a-1}\right)=v_{2}\left(a^{2^{\alpha-1}}-1\right)-v_{2}(a-1)=\sum_{i=0}^{\alpha-2} v_{2}\left(a^{2^{i}}+1\right) \geq \alpha .
$$

于是 $2^{\alpha} \left\lvert\, \frac{a^{2^{\alpha-1}-1}}{a-1}\right.$, 则 $2^{\alpha} \left\lvert\, \frac{a^{2^{\alpha-1}+1}-1}{a-1}-\frac{a-1}{a-1}\right.$,

$$
\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \cdots, \frac{a^{2^{\alpha}}-1}{a-1}
$$

中有模 $2^{\alpha}$ 同余的两项, 不符题意.

若 $a \equiv 1(\bmod 4)$, 则 $k$ 为奇数时,

$$
v_{2}\left(a^{k}-1\right)=v_{2}(a-1)+v_{2}\left(1+a+\cdots+a^{k-1}\right) .
$$

而 $1+a+\cdots+a^{k-1}$ 是奇数个奇数相加, 是一个奇数, 故

$$
v_{2}\left(1+a+\cdots+a^{k-1}\right)=0,
$$

即 $v_{2}\left(a^{k}-1\right)=v_{2}(a-1)$. 又

$$
v_{2}\left(a^{2}-1\right)=v_{2}(a-1)+v_{2}(a+1)=v_{2}(a-1)+1,
$$

由数学归纳法可知

$$
v_{2}\left(a^{m}-1\right)=v_{2}(a-1)+v_{2}(m), \forall m \in \mathbb{N}^{+}
$$

于是同 $p$ 为奇素数的情况可知, 此时

$$
\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \ldots, \frac{a^{2^{\alpha}}-1}{a-1}
$$

模 $2^{\alpha}$ 互不同余.

综上, 此时 $a$ 满足要求当且仅当

$$
\left\{\begin{array}{ll}
a \equiv 1 & (\bmod p), p \text { 为奇素数 } \\
a \equiv 1 \quad(\bmod 4), p=2
\end{array} .\right.
$$

(3) $n$ 的标准分解式为 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{r}^{\alpha_{r}}$.

由(1)(2)可知若 $a$ 不满足

$$
\left\{\begin{array}{ll}
a \equiv 1 & \left(\bmod p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \nmid n \\
a \equiv 1 & \left(\bmod 2 p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \mid n
\end{array} .\right.
$$

且存在 $1 \leq i<j \leq n, n \left\lvert\, \frac{a^{j}-1}{a-1}-\frac{a^{i}-1}{a-1}\right.$, 则

$$
\forall p_{i} \in\left\{p_{1}, p_{2}, \cdots, p_{r}\right\}, p_{i}^{\alpha_{i}} \left\lvert\, \frac{a^{j-i}-1}{a-1}\right.,
$$

又可知此时

$$
\left\{\begin{array}{ll}
a \equiv 1 & \left(\bmod p_{i}\right), p_{i} \text { 为奇素数 } \\
a \equiv 1 & (\bmod 4), p_{i}=2
\end{array} .\right.
$$

有 $p_{i}^{\alpha_{i}} \mid j-i$. 从而 $n \mid j-i$, 与 $1 \leq j-i \leq n-1$ 矛盾!

故此时

$$
\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \cdots, \frac{a^{n}-1}{a-1}
$$

模 $n$ 互不同余, 满足条件.

下面考虑一般情形. 易知数列 $\left\{x_{k} \mid x_{1}=1, x_{l}=a x_{l-1}+b, l \geq 2\right\}$ 的前 $n$ 项即为

$$
1, a+b, \cdots, a^{n-1}+b \frac{a^{n-1}-1}{a-1} .
$$

由条件可知其中任意两项模 $n$ 不同余, 也即

$$
\forall 1 \leq i<j \leq n, a^{i-1}+b \frac{a^{i-1}-1}{a-1} \not \equiv a^{j-1}+b \frac{a^{j-1}-1}{a-1} \quad(\bmod n)
$$

即

$$
\forall 1 \leq i<j \leq n,(a-1+b) \frac{a^{j-i}-1}{a-1} \not \equiv 0 \quad(\bmod n) .
$$

这首先要求 $\forall 1 \leq i<j \leq n, \frac{a^{j-i}-1}{a-1} \not \equiv 0(\bmod n)$, 即

$$
\left\{\begin{array}{ll}
a \equiv 1 & \left(\bmod p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \nmid n \\
a \equiv 1 & \left(\bmod 2 p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \mid n
\end{array} .\right.
$$

且若 $(b, n)>1$, 设 $p_{k} \in\left\{p_{1}, p_{2}, \cdots, p_{r}\right\}, p_{k} \mid(b, n)$, 则 $p_{k} \mid a-1+b$. 又此时

$$
\frac{a-1}{a-1}, \frac{a^{2}-1}{a-1}, \cdots, \frac{a^{n}-1}{a-1}
$$

模 $n$ 互不同余, 故存在 $1 \leq s \leq n-1$, 使 $p_{k}^{\alpha_{k}-1} \left\lvert\, \frac{a^{s}-1}{a-1}\right.$. 取 $j-i=s$, 则有

$$
(a-1+b) \frac{a^{j-i}-1}{a-1} \equiv 0 \quad(\bmod n)
$$

不符合要求.

而若 $(b, n)=1$, 则此时 $(a-1+b, n)=1$, 且

$$
\forall 1 \leq i<j \leq n, \frac{a^{j-i}-1}{a-1} \not \equiv 0 \quad(\bmod n) .
$$

故

$$
\forall 1 \leq i<j \leq n,(a-1+b) \frac{a^{j-i}-1}{a-1} \not \equiv 0 \quad(\bmod n)
$$

符合要求.

综上, 对给定的正整数 $n \geq 4$, 记 $n$ 的标准分解式 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{r}^{\alpha_{r}}$, 则
$f(x)=a x+b\left(a, b \in \mathbb{N}^{*}\right)$ 是模 $n$ 的完整多项式当且仅当 $(b, n)=1$, 且

$$
\left\{\begin{array}{l}
a \equiv 1\left(\bmod p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \nmid n \\
a \equiv 1\left(\bmod 2 p_{1} p_{2} \cdots p_{r}\right), \text { 若 } 4 \mid n
\end{array} .\right.
$$

注 $n=2$ 时, $f(x)=a x+b\left(a, b \in \mathbb{N}^{*}\right)$ 是完整多项式当且仅当 $a \equiv 0$ $(\bmod 2)$ 或 $b \equiv 1(\bmod 2)$.

$n=3$ 时, $f(x)=a x+b\left(a, b \in \mathbb{N}^{*}\right)$ 是完整多项式当且仅当 $a \equiv 1(\bmod 3)$且 $b \not \equiv 0(\bmod 3)$.

致谢 本文得到了冯跃峰老师的支持与指导.


[^0]:    修订日期: 2019-05-09.

