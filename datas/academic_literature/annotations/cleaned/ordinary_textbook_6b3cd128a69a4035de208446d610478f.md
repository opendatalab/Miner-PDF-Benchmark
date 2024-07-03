# 一类无穷正整数序列问题的新解 

## 廖悦辛

(华中师范大学第一附属中学, 430223)

数学竞赛中有一类无穷正整数序列的问题难度很大, 本文从一个多项式表为完全平方式的国外竞赛题出发, 运用构造多项式的方法给出这类问题的新解.

首先建立引理, 这是 2007 年保加利亚数学奥林匹克的一道试题.

引理 设 $P(x)$ 是关于 $x$ 的整系数多项式, $\operatorname{deg} P$ 为偶数, 且 $P$ 的首项为完全平方数. 若存在无穷多个 $x \in \mathbb{N}^{*}$ 使得 $P(x)$ 为完全平方数, 则必存在 $Q(x) \in \mathbb{Q}[x]$, 使 $P(x)=Q(x)^{2}$.

证明 设 $P(x)=a_{2 t}^{2} x^{2 t}+a_{2 t-1} x^{2 t-1}+\cdots+a_{0}$, 其中 $a_{2 t}, a_{2 t-1}, \cdots, a_{0} \in \mathbb{Z}$, $a_{2 t}>0$.

先证明存在 $S(x)=b_{t} x^{t}+\cdots+b_{0}, S \in \mathbb{Q}[x]$, 使得 $\operatorname{deg}\left(P-S^{2}\right) \leq t-1$ 或 $P=S^{2}$.

我们运用反向法归纳证明命题: 对任意不大于 $t$ 的非负整数 $k$, 存在 $b_{t}, b_{t-1}, \cdots, b_{k} \in \mathbb{Q}$, 使得

$$
\operatorname{deg}\left(P(x)-\left(b_{t} x^{t}+\cdots+b_{k} x^{k}\right)^{2}\right) \leq t+k-1
$$

当 $t=k$ 时, 取 $b_{t}=a_{2 t}$ 即可.

假设命题对 $k\left(k \in \mathbb{N}^{*}, k \leq t\right)$ 成立.

下面考虑 $k-1$ 的情况, 由归纳假设知存在 $b_{t}, b_{t-1}, \cdots, b_{k} \in \mathbb{Q}$, 使得 $P(x)-\left(b_{t} x^{t}+\ldots \ldots+b_{k} x^{k}\right)^{2}$ 为次数不大于 $t+k-1$ 的多项式.

那么对于任意 $b_{k-1} \in \mathbb{Q}, P(x)-\left(b_{t} x^{t}+\ldots \ldots+b_{k} x^{k}+b_{k-1} x^{k-1}\right)^{2}$ 也为次数不大于 $t+k-1$ 的多项式, 而它的 $t+k-1$ 项系数为

$$
a_{t+k-1}-2 b_{t} b_{k-1}-\sum_{i=0}^{t-k-1} b_{t-1-i} b_{k+i}
$$

修订日期: 2019-05-31.
取

$$
b_{k-1}=\frac{a_{t+k-1}-\sum_{i=0}^{t-k-1} b_{t-1-i} b_{k+i}}{2 b_{t}}
$$

则可得 $P(x)-\left(b_{t} x^{t}+\cdots+b_{k} x^{k}+b_{k-1} x^{k-1}\right)^{2}$ 为次数不大于 $t+k-2$ 的多项式,这就完成了归纳过渡.

从而 $(*)$ 得证.

在 $(*)$ 中取 $k=0$, 则知存在 $S(x), R(x) \in \mathbb{Q}[x]$, 其中 $\operatorname{deg} R \leq t-1$ 或 $R \equiv 0$且满足 $P(x)=S(x)^{2}+R(x)$.

下证此时必有 $R \equiv 0$.

用反证法. 假设 $R$ 不恒为 0 .

当 $R$ 的首项系数为正时, 存在 $M_{1}>0$, 使得 $x>M_{1}$ 时, $R(x)>0$.

记 $S$ 的所有系数的分母的最小公倍数为 $m$.

由于 $S$ 的首项系数 $a_{2 t}>0$ 且 $\operatorname{deg} R \leq t-1$, 则存在 $M_{2}>0$, 使得当 $x>M_{2}$时,

$$
\frac{2}{m} S(x)+\frac{1}{m^{2}}-R(x)>0
$$

取 $M=\max \left\{M_{1}, M_{2}\right\}$, 则当 $X>M$ 时,

$$
S(x)^{2}<S(x)^{2}+R(x)<\left(S(x)+\frac{1}{m}\right)^{2},
$$

即

$$
S(x)^{2}<P(x)<\left(S(x)+\frac{1}{m}\right)^{2} .
$$

而 $\left(S(x), S(x)+\frac{1}{m}\right)$ 一定包含在某个区间 $(j, j+1)$, 其中 $j \in \mathbb{Z}$, 则 $P(x)$ 一定不是平方数, 这与存在无穷多个 $x \in \mathbb{N}^{*}$ 使 $P(x)$ 为完全平方数矛盾.

当 $R$ 的首项系数为负时, 同理可导出矛盾.

故假设不成立, 则 $R \equiv 0$.

这就说明 $P(x)=S(x)^{2}$. 取 $Q=S$, 则引理获证.

下面我们应用引理, 解决两道颇有难度的竞赛题.

例 1 是否存在一个由无穷多个正整数构成的集合 $S$, 使得任意 $a, b, c \in S$ ( $a, b, c$ 互异), 均有 $a b c+1$ 为完全平方数?

## 解 不存在.

假设存在这样的无穷集 $S$, 不妨设其中最小的 4 个元为 $x_{1}, x_{2}, x_{3}, x_{4}\left(x_{1}<\right.$ $\left.x_{2}<x_{3}<x_{4}\right)$, 构造多项式

$$
f(x)=\left(x_{1} x_{2} x+1\right)\left(x_{2} x_{3} x+1\right)\left(x_{3} x_{4} x+1\right)\left(x_{4} x_{1} x+1\right),
$$

则有 $\operatorname{deg} f=4, f$ 的首项系数为 $\left(x_{1} x_{2} x_{3} x_{4}\right)^{2}$, 且对任意 $x \in S, f(x)$ 均为完全平方数. 由引理, 存在 $g(x) \in \mathbb{Q}[x]$, 使得 $f(x)=(g(x))^{2}$, 从而 $f$ 的每个根均为二重或者四重.

注意到 $f$ 的四个根为 $-\frac{1}{x_{1} x_{2}},-\frac{1}{x_{2} x_{3}},-\frac{1}{x_{3} x_{4}},-\frac{1}{x_{4} x_{1}}$, 由序条件知 $-\frac{1}{x_{1} x_{2}}$ 是最小的根, 它与其他根都不相同, 矛盾.

综上可知, 假设不成立, 命题获证.

例 2 设 $a_{1}<a_{2}<\cdots$ 是一个无穷正整数序列, 证明存在无穷多个素数 $p$,使得存在正整数 $i, j, k\left(i, j, k\right.$ 两两不同) 满足 $p \mid a_{i} a_{j} a_{k}-1$.

(2018 年伊朗国家队选拔考试试题)

证明 用反证法, 假设结论不成立, 则存在有限多个素数 $p_{1}, p_{2}, \cdots, p_{s}$, 使得对所有两两不同的 $i, j, k$, 都有 $a_{i} a_{j} a_{k}-1$ 的素因子在 $p_{1}, p_{2}, \cdots, p_{s}$ 中.

考虑多项式 $g_{1}(x)=\left(a_{1} a_{2} x-1\right)\left(a_{1} a_{4} x-1\right)\left(a_{2} a_{3} x-1\right)\left(a_{3} a_{4} x-1\right)$.

取 $x=a_{k}(k \geq 5)$, 则 $g_{1}(x)$ 的素因子都在 $p_{1}, p_{2}, \cdots, p_{s}$ 中, 设 $g_{1}(x)$ 的标准分解为 $g_{1}(x)=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{s}^{\alpha_{s}}$, 其中 $\alpha_{i}$ 是非负整数, 在模 2 意义下考虑 $\left(\alpha_{1}, \alpha_{2}, \cdots, \alpha_{s}\right)$, 共有 $2^{s}$ 种可能取值,而 $x$ 有无穷多个取值, 这说明存在 $\left\{a_{5}, a_{6}, \cdots\right\}$ 下的无限子集 $A_{1}$, 当 $a \in A_{1}$ 时, $g_{1}(a)$ 的标准分解中 $p_{i}$ 的幕次在模 2 意义下是定值 $(1 \leq i \leq s)$, 设这 $s$ 个幂次在模 2 意义下为 $\left(k_{11}, k_{12}, \cdots, k_{1 s}\right)$, 其中 $k_{1 i} \in\{0,1\}(i=0,1, \cdots, s)$.

由于 $A_{1}$ 是无限集, 将数列 $a_{1}, a_{2}, \cdots$ 中不在 $A_{1} \cup\left\{a_{1}, a_{2}, a_{3}, a_{4}\right\}$ 中的去掉,不影响讨论, 不妨设 $A_{1}=\left\{a_{5}, a_{6}, \cdots\right\}$.

类似地, 考虑多项式 $g_{2}(x)=\left(a_{5} a_{6} x-1\right)\left(a_{5} a_{8} x-1\right)\left(a_{6} a_{7} x-1\right)\left(a_{7} a_{8} x-1\right)$.

取 $x=a_{k}(k \geq 9)$, 则 $g_{2}(x)$ 的素因子都在 $p_{1}, p_{2}, \cdots, p_{s}$ 中, 故存在 $\left\{a_{9}, a_{10}, \cdots\right\}$的无穷子集 $A_{2}$, 当 $a \in A_{2}$ 时, $g_{2}(a)$ 的标准分解中 $p_{i}$ 的幂次在模 2 意义下是定值 $(1 \leq i \leq s)$, 设这 $s$ 个幂次在模 2 意义下为 $\left(k_{21}, k_{22}, \cdots, k_{2 s}\right)$, 其中 $k_{2 i} \in\{0,1\}(i=1,2, \cdots, s)$.

重复上面的步骤, 可以继续找到多项式 $g_{j}(x)$ 和 $s$ 维数组 $\left(k_{j 1}, k_{j 2}, \cdots, k_{j s}\right)$,满足当 $x \in A_{j}\left(A_{j}\right.$ 为无穷集 $)$ 时, $g_{j}(x)$ 的标准分解中 $p_{1}, \cdots, p_{s}$ 的幕次模 2 意义下为 $\left(k_{j 1}, \cdots, k_{j s}\right)$, 其中 $j=3,4, \cdots, 2^{s}$. 注意到 $s$ 维 0,1 数组只有 $2^{s}$ 种取值, 由抽屉原理, 存在 $1 \leq j<j^{\prime} \leq 2^{s}+1$, 使得 $\left(k_{j 1}, k_{j 2}, \cdots, k_{j s}\right)=\left(k_{j^{\prime} 1}, k_{j^{\prime} 2}, \cdots, k_{j^{\prime} s}\right)$.
记 $b_{1}=a_{4 j-3}, b_{2}=a_{4 j-2}, b_{3}=a_{4 j-1}, b_{4}=a_{4 j}, b_{5}=a_{4 j^{\prime}-3}, b_{6}=a_{4 j^{\prime}-2}, b_{7}=$ $a_{4 j^{\prime}-1}, b_{8}=a_{4 j^{\prime}}$

由于 $A_{1} \supseteq A_{2} \supseteq \cdots \supseteq A_{j^{\prime}}$, 则对任意 $x \in A_{j^{\prime}}, g_{j}(x)$ 与 $g_{j^{\prime}}(x)$ 中 $p_{1}, p_{2}, \cdots, p_{s}$的幂次的奇偶性相同, 这说明 $g_{j}(x)$ 与 $g_{j^{\prime}}(x)$ 的乘积为完全平方数.

构造多项式

$$
\begin{aligned}
f(x)= & \left(b_{1} b_{2} x-1\right)\left(b_{2} b_{3} x-1\right)\left(b_{3} b_{4} x-1\right)\left(b_{4} b_{1} x-1\right) \\
& \cdot\left(b_{5} b_{6} x-1\right)\left(b_{6} b_{7} x-1\right)\left(b_{7} b_{8} x-1\right)\left(b_{8} b_{5} x-1\right) .
\end{aligned}
$$

则对任意 $x \in A_{j^{\prime}}\left(A_{j^{\prime}}\right.$ 为无穷集), $f(x)$ 为完全平方数. 又 $\operatorname{deg} f=8, f$ 的首项系数为 $\left(\prod_{i=1}^{8} b_{i}\right)^{2}$, 由引理知存在有理系数多项式 $h(x)$, 使 $f(x)=h(x)^{2}$, 那么 $f$ 的每个根均是偶数重的.

而 $f$ 的 8 个根依次为 $\frac{1}{b_{1} b_{2}}, \frac{1}{b_{2} b_{3}}, \frac{1}{b_{3} b_{4}}, \frac{1}{b_{4} b_{1}}, \frac{1}{b_{5} b_{6}}, \frac{1}{b_{6} b_{7}}, \frac{1}{b_{7} b_{8}}, \frac{1}{b_{8} b_{5}}$, 由前述定义可知 $b_{1}<b_{2}<\cdots<b_{8}$, 这说明 $\frac{1}{b_{1} b_{2}}$ 大于其余 7 个根, 则其为单根, 矛盾.

综上可知,假设不成立,命题得证.

应用引理解决此类问题时, 核心在于构造一个多项式满足引理中的条件. 例 1 中的多项式是显而易见得到的, 例 2 中的多项式则找起来要花一番功夫, 需要使用多次抽屉原理找到指数之间的对偶关系, 从而构造对应的多项式. 关于无穷正整数序列的问题很多都比较困难, 本文另辟蹊径探究这一类问题, 希望对读者有所帮助.

致谢 感谢华中师大一附中李建国老师和华东师范大学罗振华老师仔细审阅了本文并提出的宝贵修改意见.

