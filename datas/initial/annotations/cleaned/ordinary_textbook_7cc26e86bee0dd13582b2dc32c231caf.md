# 一个乘积不等式的注记 

冷岗松

美国数学月刊 (Amer. Math. Monthly) 的 11252 号问题是 2006 年由罗马尼亚的 Ovidiu Bagdasar 提出的一个乘积不等式 [1]:

问题 1 (AMM 11252). 设 $n \geq 2$ 是整数, $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数. 记 $S=\sum_{i=1}^{n} a_{i}, S^{\prime}=\sum_{i=1}^{n} b_{i}$, 其中 $b_{i}=S-a_{i}$, 则

$$
\frac{\prod_{i=1}^{n} a_{i}}{\prod_{i=1}^{n}\left(S-a_{i}\right)} \leq \frac{\prod_{i=1}^{n} b_{i}}{\prod_{i=1}^{n}\left(S^{\prime}-b_{i}\right)} .
$$

证明这个不等式的一个非常自然的想法是能否将问题转化为一个局部不等式. 通过尝试分析, 似乎最合理的局部不等式应当是:

$$
\frac{b_{i}}{S^{\prime}-b_{i}} \geq\left(\prod_{j \neq i} \frac{a_{j}}{S-a_{j}}\right)^{\frac{1}{n-1}}, \quad \forall i \in\{1,2, \cdots, n\}
$$

为了书写简便, 不失一般性, 我们仅须考虑 (1) 中 $i=n$ 的情况:

$$
\frac{b_{n}}{S^{\prime}-b_{n}} \geq\left(\prod_{j=1}^{n-1} \frac{a_{j}}{S-a_{j}}\right)^{\frac{1}{n-1}}
$$

为证 (3) 我们须用到下面乘积形式的 Minkowski 不等式: 设 $a_{1}, \cdots, a_{n}$, $b_{1}, b_{2}, \cdots, b_{n}$ 是非负实数, 则

$$
\left(\prod_{i=1}^{n}\left(a_{i}+b_{i}\right)\right)^{\frac{1}{n}} \geq\left(\prod_{i=1}^{n} a_{i}\right)^{\frac{1}{n}}+\left(\prod_{i=1}^{n} b_{i}\right)^{\frac{1}{n}} .
$$

下面是详细的解法.

解法一 先证下面引理.

引理 设 $x, x_{1}, x_{2}, \cdots, x_{m}$ 是正实数, $m$ 是正整数, 则

$$
\frac{\left(\prod_{i=1}^{m}\left(x+x_{i}\right)\right)^{\frac{1}{m}}}{m x+\sum_{i=1}^{m} x_{i}} \geq \frac{\left(\prod_{i=1}^{m} x_{i}\right)^{\frac{1}{m}}}{\sum_{i=1}^{m} x_{i}}
$$

事实上, 由 Minkowski 不等式和算术 - 几何平均值不等式可得

$$
\prod_{i=1}^{m}\left(1+\frac{x}{x_{i}}\right) \geq\left(1+\frac{x}{\left(\prod_{i=1}^{m} x_{i}\right)^{\frac{1}{m}}}\right)^{m} \geq\left(1+\frac{m x}{\sum_{i=1}^{m} x_{i}}\right)^{m}
$$

这就是 (5), 引理得证.

回到原问题.

在引理中令 $m=n-1, x=a_{n}, x_{i}=\sum_{j \in I_{i}} a_{j}$, 其中 $I_{i}=\{1,2, \cdots, n-1\} \backslash\{i\}$,并用算术-几何平均值不等式可得

$$
\begin{aligned}
\frac{\left(\prod_{i=1}^{n-1}\left(S-a_{i}\right)\right)^{\frac{1}{n-1}}}{S^{\prime}-b_{n}{ }^{\prime}} & =\frac{\left(\prod_{i=1}^{n-1}\left(a_{n}+\sum_{j \in I_{i}} a_{j}\right)\right)^{\frac{1}{n-1}}}{(n-1) a_{n}+\sum_{i=1}^{n-1}\left(\sum_{j \in I_{i}} a_{j}\right)} \\
& \geq \frac{\left(\prod_{i=1}^{n-1}\left(\sum_{j \in I_{i}} a_{j}\right)\right)^{\frac{1}{n-1}}}{\sum_{i=1}^{n-1} \sum_{j \in I_{i}} a_{j}}=\frac{\left(\prod_{i=1}^{n-1}\left(\sum_{j \in I_{i}} a_{j}\right)\right)^{\frac{1}{n-1}}}{(n-2) b_{n}} \\
& \geq \frac{\left(\prod_{i=1}^{n-1}(n-2)\left(\prod_{j \in I_{i}} a_{j}\right)^{\frac{1}{n-2}}\right)^{\frac{1}{n-1}}}{(n-2) b_{n}}=\frac{\left(\prod_{i=1}^{n-1} a_{i}\right)^{\frac{1}{n-1}}}{b_{n}}
\end{aligned}
$$

整理得

$$
\frac{b_{n}}{S^{\prime}-b_{n}} \geq\left(\prod_{j=1}^{n-1} \frac{a_{j}}{S-a_{j}}\right)^{\frac{1}{n-1}}
$$

这就是(3). 所以对任意的 $1 \leq i \leq n,(2)$ 成立. 将 (2) 中的 $n$ 个不等式相乘便得 $(1)$.

饶家鼎 (2013 年中国国家队队员) 给出了 (1) 的一个另证.

解法二 注意到 (1) 是关于 $a_{1}, \cdots, a_{n}$ 的齐次不等式, 故不妨设 $S=1$, 这时 $S^{\prime}=\sum_{i=1}^{n}\left(1-a_{i}\right)=n-1$. 要证的 (1)等价于

$$
\prod_{i=1}^{n}\left(\frac{1}{a_{i}}-1\right) \geq \prod_{i=1}^{n}\left(\frac{n-1}{\sum_{j \neq i} a_{j}}-1\right)
$$

要证 (6), 只需证局部不等式

$$
\prod_{j=1}^{n-1}\left(\frac{1}{a_{j}}-1\right) \geq\left(\frac{n-1}{\sum_{j=1}^{n-1} a_{j}}-1\right)^{n-1}
$$

便可, 而对 (7) 存在稍一般的如下不等式, 仍用引理表述.
引理 设 $x_{1}, x_{2}, \cdots, x_{k}$ 是正实数, 且 $x_{1}+\cdots+x_{k} \leq 1, k$ 是正整数, 则

$$
\prod_{i=1}^{k}\left(\frac{1}{x_{i}}-1\right) \geq\left(\frac{k}{\sum_{i=1}^{n} x_{i}}-1\right)^{k}
$$

事实上, 令 $f(x)=\ln \left(\frac{1}{x}-1\right), x \in(0,1)$, 则

$$
f^{\prime \prime}(x)=\frac{1-2 x}{x^{2}(1-x)^{2}} \geq 0, \quad \forall x \in\left(0, \frac{1}{2}\right] .
$$

这说明 $f(x)$ 在 $\left(0, \frac{1}{2}\right]$ 上是凸函数.

(i) 当 $x_{1}, x_{2}, \cdots, x_{k}$ 均属于 $\left(0, \frac{1}{2}\right]$ 时, 这时对 $f(x)$ 用 Jensen 不等式立得所证不等式 (8).

(ii) 当 $x_{1}, x_{2}, \cdots, x_{k}$ 中有数不属于 $\left(0, \frac{1}{2}\right]$ 时, 由条件, 这样的数仅有一个, 不妨设为 $x_{1}$, 这时由 $x_{1}+x_{2} \leq 1$ 便知

$$
\left(\frac{1}{x_{1}}-1\right)\left(\frac{1}{x_{2}}-1\right)-\left(\frac{2}{x_{1}+x_{2}}-1\right)^{2}=\frac{\left(x_{1}-x_{2}\right)^{2}\left(1-x_{1}-x_{2}\right)}{\left(x_{1}+x_{2}\right)^{2} x_{1} x_{2}} \geq 0
$$

亦即

$$
\left(\frac{1}{x_{1}}-1\right)\left(\frac{1}{x_{2}}-1\right) \geq\left(\frac{2}{x_{1}+x_{2}}-1\right)^{2}
$$

这样要证 (8), 仅须证明

$$
\left(\frac{1}{\frac{x_{1}+x_{2}}{2}}-1\right)^{2} \prod_{i=3}^{k}\left(\frac{1}{x_{i}}-1\right) \geq\left(\frac{k}{\sum_{i=1}^{k} x_{i}}-1\right)^{k}
$$

故只要对变元 $\frac{x_{1}+x_{2}}{2}, \frac{x_{1}+x_{2}}{2}, x_{3}, \cdots, x_{n}$ 用 Jensen 不等式便得 (9). 引理得证.

最近, 福建晋江养正中学的王明璋同学在求证 (1) 时, 证明了如下结果:

问题 2. 设 $c, x_{1}, x_{2}, \ldots, x_{n}$ 是正数 $(n \geq 2)$ 且满足

$$
c \geq \sum_{i=1}^{n} x_{i}
$$

则

$$
\prod_{i=1}^{n} \frac{x_{i}}{c-x_{i}} \leq\left(\frac{\sum_{i=1}^{n} x_{i}}{n c-\sum_{i=1}^{n} x_{i}}\right)^{n}
$$

问题 2 本质上和饶家鼎证明的引理一样, 但形式上更一般化. 由于参数 $c$的引进, 使得我们的证明更多样化, 特别是下面由湖南省雅礼中学江朗同学, 上海中学黄小雨同学等人的证明颇为有趣, 也可算是 (1) 的一个新证明.

解法一 注意到 (10) 等价于

$$
\frac{\left(n c-\left(x_{1}+\ldots+x_{n}\right)\right)^{n}}{\prod_{i=1}^{n}\left(c-x_{i}\right)} \leq \frac{\left(x_{1}+\ldots+x_{n}\right)^{n}}{\prod_{i=1}^{n} x_{i}}
$$

固定 $x_{1}, x_{2}, \ldots, x_{n}$, 引进函数

$$
f(c)=\frac{\left(n c-\left(x_{1}+\ldots+x_{n}\right)\right)^{n}}{\prod_{i=1}^{n}\left(c-x_{i}\right)}, \quad c \geq \max \left\{x_{1}, \ldots, x_{n}\right\}
$$

注意到由 Cauchy 不等式可得

$$
\left(n c-\left(x_{1}+\ldots+x_{n}\right)\right) \cdot \sum_{i=1}^{n} \frac{1}{c-x_{i}} \geq n^{2} .
$$

这样便知

$$
f^{\prime}(c)=\frac{\left(n c-\left(x_{1}+\ldots+x_{n}\right)\right)^{n-1}\left(n^{2}-\left(n c-\left(x_{1}+\ldots+x_{n}\right)\right) \sum_{i=1}^{n} \frac{1}{c-x_{i}}\right)}{\prod_{i=1}^{n}\left(c-x_{i}\right)} \leq 0
$$

故 $f(c)$ 在其定义域 $\left[\max \left\{x_{1}, \ldots, x_{n}\right\},+\infty\right)$ 上是减函数. 这样由

$$
c \geq x_{1}+\ldots+x_{n} \geq \max \left\{x_{1}, \ldots, x_{n}\right\}
$$

便知 $f(c) \leq f\left(x_{1}+\ldots+x_{n}\right)$, 这就是 (11), 证毕.

问题 2 的另一简洁独特证法由湖南长郡中学的谭华为同学给出.

解法二 令 $c=k\left(x_{1}+\ldots+x_{n}\right)$, 则 $k \geq 1$. 这时由加权的算术-几何平均不等式便得

$$
\begin{aligned}
\frac{c-x_{i}}{n k-1} & =\sum_{j \neq i} \frac{k x_{j}}{n k-1}+\frac{k-1}{n k-1} x_{i} \\
& \geq\left(\prod_{j \neq i} x_{j}^{\frac{k}{n-1}}\right) \cdot x_{i}^{\frac{k-1}{n k-1}}, \quad \forall i=1,2, \cdots, n .
\end{aligned}
$$

将上面 $n$ 个不等式相乘便得

$$
\prod_{i=1}^{n} \frac{c-x_{i}}{n k-1} \geq \prod_{i=1}^{n}\left(\prod_{j \neq i} x_{j}^{\frac{k}{n k-1}}\right) \cdot x_{i}^{\frac{k-1}{n k-1}}=\prod_{i=1}^{n} x_{i},
$$

将 $k=\frac{x_{1}+\cdots+x_{n}}{c}$ 代入, 这就是要证的不等式 (10).

对问题 2 的下面的观察是有趣的 (这实质上也是对问题 1 的观察). $a_{k}=\frac{x_{k}}{c}, k=1,2, \cdots, n$, 这时 (10) 可等价变为:

设 $a_{1}, a_{2}, \ldots, a_{n}$ 是正数且满足 $a_{1}+\ldots+a_{n} \leq 1$. 则

$$
\frac{\prod_{k=1}^{n} a_{k}}{\left(\sum_{k=1}^{n} a_{k}\right)^{n}} \leq \frac{\prod_{k=1}^{n}\left(1-a_{k}\right)}{\left(\sum_{i=1}^{n}\left(1-a_{k}\right)\right)^{n}}
$$

对比著名的 Fan Ky 不等式: 设 $0<a_{k} \leq \frac{1}{2}, k=1,2, \cdots, n$.

$$
\frac{\prod_{k=1}^{n} a_{k}}{\left(\sum_{k=1}^{n} a_{k}\right)^{n}} \leq \frac{\prod_{k=1}^{n}\left(1-a_{k}\right)}{\left(\sum_{k=1}^{n}\left(1-a_{k}\right)\right)^{n}}
$$

便知 (10) 是一个 Fan Ky 型的不等式, 只是条件稍有变化. 这样, 不等式 (1) 也是 Fan Ky 不等式的一个变形结果. 这算是一种 “探源” 吧!

## 参考文献

[1] Ovidiu Bagdasar, etc. A Productive Inequality (Problem 11252), Amer Math.

Monthly, 115 (2008), 268-269.

