# 一个问题的两个推广 

胡俊浦

(温州育英国际学校, 325005)

本文问题来源于 2021 年上半年做的一套一试模拟试题第 9 题. 原题如下:

原题 已知 $a, b, c$ 为互不相同的实数, 证明:

$$
\left|\frac{a+b}{a-b}\right|+\left|\frac{b+c}{b-c}\right|+\left|\frac{c+a}{c-a}\right| \geq 2
$$

此问题看似简单, 实则作为一试题不太容易. 若试图通过讨论 $a, b, c$ 打开绝对值, 那么将十分复杂. 答案采取了一个常规又巧妙的方法.

证明 设

$$
x=\frac{a+b}{a-b}, y=\frac{b+c}{b-c}, z=\frac{c+a}{c-a},
$$

则

$$
(x+1)(y+1)(z+1)=\frac{8 a b c}{(a-b)(b-c)(c-a)}=(x-1)(y-1)(z-1),
$$

即

$$
x y+y z+z x=-1 .
$$

不难发现 $x, y, z$ 中必有两数同号, 另一数与它们异号. 不妨设 $x, y \geq 0, z<0$,则

$$
|x|+|y|+|z|=x+y-z=x+y+\frac{x y+1}{x+y} \geq 2 \sqrt{x y+1} \geq 2
$$

成立. 等号在 $x=1, y=0, z=-1$ 时可取得.

答案的证明简洁而有技巧, 最关键且值得深思的一步就是将条件转化为

$$
x y+y z+z x=-1 .
$$

实际上原式根据齐次性实际上是一个 2 元的式子, 换元之后变成 3 元式子, 转化而来的条件可以消去一个元. 由此可以看出条件的转化是充要的, 可以根据满足
这个式子的 $x, y, z$ 唯一确定出 $a, b, c$ 之间的比例关系, 那么这种巧妙的思路能否推广便是我想研究的.

对于上面的问题联想到两个 $n$ 元形式的问题如下:

问题 给定正整数 $n$, 设 $x_{1}, \ldots, x_{n}$ 为 $n$ 个互不相同的实数

(1) 求 $\lambda_{\max }=\lambda(n)$, 使得

$$
\sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right| \geq \lambda(n)
$$

恒成立。

(2) 求 $\lambda_{\max }=\lambda(n)$, 使得

$$
\sum_{i=1}^{n}\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right| \geq \lambda(n)
$$

恒成立。

这种类型的推广命题的一开始自然是以原解答切入. 尝试可以发现其中 (1)的换元所得到的的条件式并非充分条件, 并不能进行类似转化. (2) 的换元满足充分的要求, 可化为下面的问题:

已知 $a_{1}, \ldots, a_{n}$ 满足

$$
\prod_{i=1}^{n}\left(a_{i}+1\right)=\prod_{i=1}^{n}\left(a_{i}-1\right)
$$

求 $\sum_{i=1}^{n}\left|a_{i}\right|$ 的最小值.

上面的转化并不能带来很干净的条件式, 完全相同的路走不通. 根据上面的尝试, 基本可以放弃用原本的思路进行推广, 转而开始重新审视这两个问题. 其中问题 1 在结构上更具有对称性, 可以用归纳的思路; 问题 2 较为容易, 在我们猜出取等条件后可以很轻松地通过调整法讨论而得.

下面首先解决问题 1. 尽管处理 $n$ 元不等式的方法并不多, 用常规的单个 $x_{i}$的调整尤为复杂, 因此归纳也没有什么把 $n$ 化小的思路, 直到 2021 年 IMO 的第二题激发了我的灵感:

设 $x_{1}, \ldots, x_{n}$ 为实数, 证明:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}-x_{j}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}+x_{j}\right|}
$$

它的解答思路是利用 $\left|x_{i}-x_{j}\right|$ 的平移不变性, 并保持 $x_{i}+x_{j}$ 不变号. 通过抽象化处理进行调整, 使得存在 $x_{i}+x_{j}=0$, 从而达到从 $n$ 到更小的正整数的归
纳效果. 种种契合给了问题 1 一个很好的解决方案如下:

问题 1 给定正整数 $n$, 设 $x_{1}, \ldots, x_{n}$ 为 $n$ 个互不相同的实数. 求 $\lambda_{\text {max }}=$ $\lambda(n)$, 使得

$$
\sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right| \geq \lambda(n)
$$

恒成立。

证明 设

$$
X=\left\{x_{i}+x_{j} \mid 1 \leq i<j \leq n\right\}
$$

为可重集. 用 $X_{1}, X_{2}$ 分别表示 $X$ 中大于等于 0 和小于 0 的部分. 记

$$
m_{1}=\min X_{1}, m_{2}=\max X_{2}
$$

考察 $m_{1}, m_{2} \neq 0$ 的情形, 则对于 $t \in\left[-\frac{m_{1}}{2},-\frac{m_{2}}{2}\right]$. 令

$$
y_{i}=x_{i}+t, f(i, j)=x_{i}+x_{j}, g(i, j)=\left|x_{i}-x_{j}\right| \text {, }
$$

则 $y_{i}+y_{j}$ 与 $x_{i}+x_{j}$ 同号, 从而

$$
\sum_{1 \leq i<j \leq n}\left|\frac{y_{i}+y_{j}}{y_{i}-y_{j}}\right|=\sum_{f(i, j) \in X_{1}} \frac{f(i, j)+2 t}{g(i, j)}-\sum_{f(i, j) \in X_{2}} \frac{f(i, j)+2 t}{g(i, j)} .
$$

将上式视为关于 $t$ 的函数 $h(t)$, 有

$$
h(0)=\sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right| .
$$

由一次函数的性质对于 $-\frac{m_{1}}{2}<0<-\frac{m_{2}}{2}$, 必存在 $t=-\frac{m_{1}}{2}$ 或 $-\frac{m_{2}}{2}$, 使得 $h(t) \leq h(0)$.

对于这样的 $t$, 满足

$$
\sum_{1 \leq i<j \leq n}\left|\frac{y_{i}+y_{j}}{y_{i}-y_{j}}\right| \leq \sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|
$$

且存在 $1 \leq i<j \leq n$ 使得 $y_{i}+y_{j}=0$. 至此我们将原式转化为了

$$
\min _{1 \leq i<j \leq n}\left|x_{i}+x_{j}\right|=0
$$

的情况.

不妨设 $x_{n-1}+x_{n}=0$, 则

$$
\begin{aligned}
\sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right| & =\sum_{1 \leq i<j \leq n-2}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|+\sum_{i=1}^{n-2}\left(\left|\frac{x_{i}+x_{n-1}}{x_{i}-x_{n-1}}\right|+\left|\frac{x_{i}+x_{n}}{x_{i}-x_{n}}\right|\right) \\
& =\sum_{1 \leq i<j \leq n-2}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|+\sum_{i=1}^{n-2}\left(\left|\frac{x_{i}+x_{n-1}}{x_{i}-x_{n-1}}\right|+\left|\frac{x_{i}-x_{n-1}}{x_{i}+x_{n-1}}\right|\right)
\end{aligned}
$$

$$
\geq \sum_{1 \leq i<j \leq n-2}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|+2(n-2) .
$$

通过上面的处理, 成功将 $n$ 与 $n-2$ 建立了联系. 不难得到 $\lambda(2)=0, \lambda(3)=$ 2. 利用 $\lambda(n) \geq \lambda(n-2)+2(n-2)$ 建立递推关系可得:

$$
\begin{cases}\lambda(n) \geq \frac{n(n-2)}{2}, & n \text { 为偶数 } \\ \lambda(n) \geq \frac{(n-1)^{2}}{2}, & n \text { 为奇数 }\end{cases}
$$

反过来考虑取等条件, 从归纳及其中的放缩可以看出 $x_{n-1}=-x_{n}$ 需满足

$$
\frac{x_{n-1}}{x_{i}} \rightarrow 0 \text { 或 } \frac{x_{i}}{x_{n-1}} \rightarrow 0, \quad i<n-1 \text {. }
$$

同时继续向下归纳知类似的 $x_{n-3}=-x_{n-2}$ 需满足

$$
\frac{x_{n-3}}{x_{i}} \rightarrow 0 \text { 或 } \frac{x_{i}}{x_{n-3}} \rightarrow 0, \quad i<n-3 \text {. }
$$

我们不难想到, 在 $n$ 为偶数时取

$$
x_{2 i-1}=\varepsilon^{i-1}, x_{2 i}=-\varepsilon^{i-1}\left(1 \leq i \leq \frac{n}{2}\right)
$$

并令 $\varepsilon \rightarrow 0$. 不难验证 $\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|$ 除了对 $(i, j)=(2 k-1,2 k)$ 为 0 , 其余均为 1 . 故

$$
\sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|=\mathrm{C}_{n}^{2}-\frac{n}{2}=\frac{n(n-2)}{2}
$$

成立.

$n$ 为奇数时, 在前 $n-1$ 个数按偶数的取法的基础上取 $x_{n}=0$. 类似可以得到

$$
\sum_{1 \leq i<j \leq n}\left|\frac{x_{i}+x_{j}}{x_{i}-x_{j}}\right|=\mathrm{C}_{n-1}^{2}-\frac{n-1}{2}+n-1=\frac{(n-1)^{2}}{2}
$$

成立.

故问题 1 所求 $\lambda_{\min }=\lambda(n)=\left[\frac{(n-1)^{2}}{2}\right]$.

回顾总结问题 1 , 该问题的提出并不困难, 有趣的是它可以巧妙化用 IMO 第二题的解答思路, 这种手法并不常见, 通过尝试用此方法命制一些其它题目的方式可以加深我们对这种技巧的熟练程度.

下面解决问题 2.

问题 2 给定正整数 $n$, 设 $x_{1}, \ldots, x_{n}$ 为 $n$ 个互不相同的实数. 求 $\lambda_{\max }=$ $\lambda(n)$, 使得

$$
\sum_{i=1}^{n}\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right| \geq \lambda(n)
$$

恒成立。
利用换元可以得到更直观的形式如问题 $2^{\prime}$.

问题 $2^{\prime}$ 已知 $a_{1}, \ldots, a_{n}$ 满足

$$
\prod_{i=1}^{n}\left(a_{i}+1\right)=\prod_{i=1}^{n}\left(a_{i}-1\right)
$$

求 $\sum_{i=1}^{n}\left|a_{i}\right|$ 的最小值.

当 $n$ 为偶数时, 取 $a_{1}=\ldots=a_{n}=0$ 即为 $\sum_{i=1}^{n}\left|a_{i}\right|$ 的最小值. $n$ 为奇数时, 也可只取 $a_{1}=-1, a_{2}=1$ 其余为 0 . 这样 $n$ 为偶数时命题平凡, $n$ 为奇数时猜想

$$
\sum_{i=1}^{n}\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right| \geq 2
$$

证明 $n$ 为偶数时, 取

$$
x_{1}=-x_{2}=x_{3}=-x_{4}=\cdots=x_{n-1}=-x_{n},
$$

有

$$
\sum_{i=1}^{n}\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right|=0
$$

故 $\lambda_{\max }=0$.

$n$ 为奇数时,我们证明

$$
\sum_{i=1}^{n}\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right| \geq 2
$$

注意到若 $x_{i}, x_{i+1}$ 同号, 即有

$$
\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right| \geq 1
$$

由奇数的条件又必有一组 $x_{i}, x_{i+1}$ 同号. 因此问题就可归为恰有一组 $x_{i}, x_{i+1}$ 同号的情形.

不妨设 $x_{2 i-1}>0, x_{2 i}<0$ (若有等于 0 的可以进行小范围微调, 只要不影响绝对值内数值的符号即可). 此时只有 $x_{1}, x_{n}$ 同号, 不妨设 $x_{n}>x_{1}$. 记 $d_{i}=\left|\frac{x_{i}}{x_{i+1}}\right|$, 则 $\prod_{i=1}^{n} d_{i}=1$ 且对 $1 \leq i \leq n-1$,

$$
\left|\frac{x_{i}+x_{i+1}}{x_{i}-x_{i+1}}\right|=\left|\frac{\left|x_{i}\right|-\left|x_{i+1}\right|}{\left|x_{i}\right|+\left|x_{i+1}\right|}\right|=\frac{\left|d_{i}-1\right|}{d_{i}+1} .
$$

设

$$
f\left(d_{1}, d_{2}, \ldots, d_{n}\right)=\sum_{i=1}^{n-1} \frac{\left|d_{i}-1\right|}{d_{i}+1}+\frac{d_{n}+1}{d_{n}-1}
$$

下面将在 $\prod_{i=1}^{n} d_{i}=1$ 条件下进行调整.

(1) 若存在 $d_{k}>1, k \leq n-1$. 令

$$
d_{k}{ }^{\prime}=1, d_{n}{ }^{\prime}=d_{n} d_{k}>d_{n}, d_{i}{ }^{\prime}=d_{i}(i \neq k, n),
$$

则

$$
f\left(d_{1}, d_{2}, \ldots, d_{n}\right)-f\left(d_{1}{ }^{\prime}, d_{2}{ }^{\prime}, \ldots, d_{n}{ }^{\prime}\right)=\frac{d_{k}-1}{d_{k}+1}+\frac{2 d_{n}\left(d_{k}-1\right)}{\left(d_{n}-1\right)\left(d_{n} d_{k}-1\right)}>0
$$

(2) 若存在 $d_{k}, d_{l}<1, k<l \leq n-1$. 令

$$
d_{k}^{\prime}=1, d_{l}^{\prime}=d_{k} d_{l}, d_{i}^{\prime}=d_{i}(i \neq k, l),
$$

则

$$
\begin{aligned}
& f\left(d_{1}, d_{2}, \ldots, d_{n}\right)-f\left(d_{1}{ }^{\prime}, d_{2}{ }^{\prime}, \ldots, d_{n}{ }^{\prime}\right)=\frac{1-d_{k}}{1+d_{k}}+\frac{1-d_{l}}{1+d_{l}}-\frac{1-d_{k} d_{l}}{1+d_{k} d_{l}}>0 \\
\Leftrightarrow & \left(1-d_{k}\right)\left(1-d_{l}\right)>0 .
\end{aligned}
$$

成立.

由上述讨论知, 经过有限次调整可得:对 $i \leq n-1$, 除至多一个 $d_{i} \neq 1$ (设为 $\left.d_{1}\right)$ 外, 其余 $d_{i}=1$. 因此就有 $d_{1}=\frac{1}{d_{n}}<1$. 故

$$
\begin{aligned}
\left(d_{1}, d_{2}, \ldots, d_{n}\right) & =\sum_{i=1}^{n-1} \frac{\left|d_{i}-1\right|}{d_{i}+1}+\frac{d_{n}+1}{d_{n}-1} \\
& \geq \frac{1-\frac{1}{d_{n}}}{1+\frac{1}{d_{n}}}+\frac{d_{n}+1}{d_{n}-1} \\
& =\frac{d_{n}-1}{d_{n}+1}+\frac{d_{n}+1}{d_{n}-1} \\
& \geq 2 .
\end{aligned}
$$

原不等式得证.

至此我们完成了问题 2 在奇数情况下的解答, 即所求 $\lambda_{\text {max }}=\lambda(n)=2$.

回顾总结问题 2 , 该问题是一个不太难的问题, 直接调整思路也很清晰. 但大家还可以尝试能否从

出发得到

$$
\prod_{i=1}^{n}\left(a_{i}+1\right)=\prod_{i=1}^{n}\left(a_{i}-1\right)
$$

$$
\sum_{i=1}^{n}\left|a_{i}\right| \geq 2
$$

的一个更加简单的证明.

在对原题拓展的过程中, 我也借鉴了很多外观类似的问题, 下面列举出来供大家参考.

1. 给定 $n \geq 2$, 求 $\lambda_{\text {min }}$ 使

$$
\sum_{i=1}^{n} \frac{a_{i}-b_{i}}{a_{i}+b_{i}} \leq \lambda
$$

对任意满足

$$
\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} b_{i}
$$

的正实数 $a_{1}, \ldots, a_{n}, b_{1}, \ldots, b_{n}$ 成立.

(新星小考试题)

2. 给定 $n \geq 3$, 求 $\lambda_{\text {max }}$, 使对任意两两不同的实数 $a_{1}, \ldots, a_{n}$, 都有

$$
\sum_{i=1}^{n} \frac{a_{i}}{\left|a_{i+1}-a_{i+2}\right|} \geq \lambda
$$

( 2019 哈萨克斯坦)

3. 已知 $a, b, c$ 为 3 个互不相等的正实数, 证明:

$$
\frac{a^{2}}{|b-c|}+\frac{b^{2}}{|c-a|}+\frac{c^{2}}{|c-a|} \geq a+b+c .
$$

其中 3 是一个尝试研究

$$
\sum_{i=1}^{n} \frac{a_{i}^{2}}{\left|a_{i+1}-a_{i+2}\right|}
$$

的一个半成品, 感觉不太好推广.

