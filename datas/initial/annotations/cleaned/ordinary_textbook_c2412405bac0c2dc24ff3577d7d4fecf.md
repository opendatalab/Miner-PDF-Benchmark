# 一类多项式问题的简捷解法 

罗文林

(湖南师范大学附属中学, 410008)

指导老师: 羊明亮

对给定的一个复系数多项式, 如何用多项式的系数来估计其在单位圆盘内的最大模, 即估计 $\max _{\|z\| \leq 1}|f(z)|$ 的问题, 近年来在数学竞赛中经常出现. 本文通过实例介绍这一类问题的新的简捷方法.

题 A. 已知 $f(z)=c_{n} \cdot z^{n}+c_{n-1} \cdot z^{n-1}+\cdots+c_{1} \cdot z+c_{0}$ 是一个 $n$ 次复系数多项式. 求证: 一定存在一个复数 $z_{0},\left|z_{0}\right| \leq 1$, 且 $\left|f\left(z_{0}\right)\right| \geq\left|c_{n}\right|+\left|c_{0}\right|$.

(CMO, 1994)

解法一 设 $w=e^{\frac{2 \pi i}{n}}$, 则对 $k \in\{1,2, \cdots, n-1\}$ 有

$$
w^{k}+w^{2 k}+\cdots+w^{(n-1) k}+w^{n k}=0 .
$$

再设 $u=\left(\frac{c_{0} \cdot\left|c_{n}\right|}{c_{n} \cdot\left|c_{0}\right|}\right)^{\frac{1}{n}}$, 则

$$
\begin{aligned}
\sum_{k=1}^{n}\left|f\left(u w^{k}\right)\right| & \geq\left|\sum_{k=1}^{n} f\left(u w^{k}\right)\right| \\
& =\left|n \cdot \frac{c_{0} \cdot\left|c_{n}\right|}{\left|c_{0}\right|}+n \cdot c_{0}\right| \\
& =n \cdot\left|c_{n}\right|+n \cdot\left|c_{0}\right| .
\end{aligned}
$$

故

$$
\max _{1 \leq k \leq n}\left\{\left|f\left(u w^{k}\right)\right|\right\} \geq\left|c_{n}\right|+\left|c_{0}\right|
$$

亦即存在 $1 \leq j \leq n$ 使得

$$
\left|f\left(u w^{j}\right)\right| \geq\left|c_{n}\right|+\left|c_{0}\right| .
$$

因此取 $z_{0}=u w^{j}$, 注意到 $\left|z_{0}\right|=1$ 便知结论成立.

这是笔者在第一次做题 $\mathrm{A}$ 时的解法. 这个解法源于下面自然的想法: 既然
要证明结果的右边只留下了最高次项系数 $c_{n}$ 及常数项 $c_{0}$, 那么我们就可利用单位根的性质, 消去 $c_{1}, \cdots, c_{n-1}$.

题 B. 已知复系数多项式 $P(z)=a_{n} \cdot z^{n}+a_{n-1} \cdot z^{n-1}+\cdots+a_{1} \cdot z+a_{0}$, 求证: 存在一个复数 $z$, 满足 $|z| \leq 1$, 且 $|P(z)| \geq\left|a_{0}\right|+\frac{\left|a_{1}\right|}{n}$.

(中国国家队培训, 2003)

这一问题不能用题 A 的解中的方法解决; 虽然右边有一项系数相对于题 A 来说变小了, 但由单位根的性质却不能直接将之消去的. 不过可以构造另外的多项式, 再将它的根按模长大小排序, 并说明模长最小的根一定满足要求.

解 令

$$
f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x-\frac{a_{0}\left|a_{1}\right|}{n\left|a_{0}\right|}
$$

若 $a_{0}=0$, 取 $f(x)$ 常数项为 $\frac{a_{1}}{n}$. 设 $f(x)$ 的所有根为 $z_{1}, z_{2}, \cdots, z_{n}$, 不妨设

$$
\left|z_{1}\right| \leq\left|z_{2}\right| \leq \cdots \leq\left|z_{n}\right|,
$$

则由韦达定理, 得

$$
\begin{gathered}
\left|z_{1} z_{2} \cdots z_{n}\right|=\left|\frac{a_{1}}{n a_{n}}\right| \\
\left|z_{1} z_{2} \cdots z_{n}\right| \cdot\left|\frac{1}{z_{1}}+\frac{1}{z_{2}}+\cdots+\frac{1}{z_{n}}\right|=\sum_{i=1}^{n} \prod_{j \neq i}\left|z_{j}\right|=\left|\frac{a_{1}}{a_{n}}\right| .
\end{gathered}
$$

两式相除, 得

$$
\left|\frac{1}{z_{1}}+\frac{1}{z_{2}}+\cdots+\frac{1}{z_{n}}\right|=n \text {. }
$$

又注意到

$$
n \cdot\left|\frac{1}{z_{1}}\right|=\left|\frac{1}{z_{1}}+\frac{1}{z_{1}}+\cdots+\frac{1}{z_{1}}\right| \geq\left|\frac{1}{z_{1}}+\frac{1}{z_{2}}+\cdots+\frac{1}{z_{n}}\right|=n,
$$

故 $\left|z_{1}\right| \leq 1$. 从而

$$
|P(z)|=\left|\frac{a_{0}\left|a_{1}\right|}{n\left|a_{0}\right|}+a_{0}\right|=\frac{\left|a_{1}\right|}{n}+\left|a_{0}\right| .
$$

故结论成立.

题 B 的处理方法对题 A 也是适用的. 事实上, 我们有

题 A 的解法二 设

$$
P(x)=c_{n} x^{n}+c_{n-1} x^{n-1}+\cdots+c_{1} x-\frac{c_{n}\left|c_{0}\right|}{\left|c_{0}\right|},
$$

若 $c_{0}=0$, 则取 $p(x)$ 常数项为 $c_{0}$. 设 $p(x)$ 的所有根为 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$, 由韦达定
理得

$$
\left|\alpha_{1}\right| \cdots\left|\alpha_{n}\right|=1
$$

则存在 $i \in\{1,2, \cdots, n\}$, 使得 $\left|\alpha_{i}\right| \leq 1$, 不妨设为 $\alpha_{1}$, 则

$$
\left|f\left(\alpha_{1}\right)\right|=\left|\frac{c_{n}\left|c_{0}\right|}{\left|c_{0}\right|}+c_{0}\right|=\left|c_{0}\right|+\left|c_{n}\right|
$$

故结论成立.

当然, 这种构造多项式的方法也有一定的局限性, 有时需要同时利用单位根的性质来构造.

题 C. 设 $n$ 为正整数, 复系数多项式 $P(z)=\sum_{i=0}^{n} a_{i} \cdot z^{i}$, 求证: 存在一个复数 $z$, 满足 $|z| \leq 1$, 且

$$
|P(z)| \geq\left|a_{0}\right|+\max _{1 \leq k \leq n} \frac{\left|a_{k}\right|}{\left[\frac{n}{k}\right]}
$$

(AMM, 10779 号问题)

证明 只须证对任意 $k \in\{1,2, \cdots, n\}$, 存在 $|z| \leq 1$, 使得

$$
|P(z)| \geq\left|a_{0}\right|+\frac{\left|a_{k}\right|}{\left[\frac{n}{k}\right]}
$$

首先, 先证 $k=1$ 的情形, 这即题 $\mathrm{B}$, 构造多项式即证.

再证 $1<k \leq n$ 的情形. 令 $\varepsilon=e^{\frac{2 \pi i}{k}}(k$ 次单位根), 考虑多项式

$$
Q(z)=\frac{1}{k} \cdot \sum_{j=0}^{k-1} P\left(\varepsilon^{j} \cdot z\right)=a_{0}+a_{k} \cdot z^{k}+a_{2 k} \cdot z^{2 k}+\cdots
$$

则 $Q(z)$ 为关于 $z^{k}$ 的 $\left[\frac{n}{k}\right]$ 次多项式.

由 $k=1$ 的结论可知, 存在 $\left|z_{0}\right| \leq 1$, 使得

$$
|Q(z)| \geq\left|a_{0}\right|+\frac{\left|a_{k}\right|}{\left[\frac{n}{k}\right]}
$$

故存在 $1 \leq j \leq n$, 使得

$$
\left|P\left(\varepsilon^{j} \cdot z_{0}\right)\right| \geq\left|a_{0}\right|+\frac{\left|a_{k}\right|}{\left[\frac{n}{k}\right]} .
$$

证毕.

