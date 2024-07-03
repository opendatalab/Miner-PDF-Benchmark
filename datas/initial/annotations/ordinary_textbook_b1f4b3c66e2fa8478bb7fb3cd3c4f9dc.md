# 好题与妙解（三） 

## -2016 年新星五一班中的若干问题

## 冷岗松

本文将选择笔者为 2016 年数学新星五一班所编的讲义 “数学问题精选 30 例” 中的若干问题进行评析.

题 1 (圣彼得堡, 2001) 设 $x_{1}, x_{2}, \cdots, x_{10}$ 是 [0, $\left.\frac{\pi}{2}\right]$ 上的实数, 满足

$$
\sin ^{2} x_{1}+\sin ^{2} x_{2}+\cdots+\sin ^{2} x_{10}=1 .
$$

证明: $3\left(\sin x_{1}+\sin x_{2}+\cdots+\sin x_{10}\right) \leq \cos x_{1}+\cos x_{2}+\cdots+\cos x_{10}$.

分析 本题并不容易入手. 思考的关键点应是怎样才能产生常数 3 (相关连的是常数 9). 这诱发我们用 Cauchy 不等式, 导出局部不等式来达到目的.

证明 对任意的正整数 $i(1 \leq i \leq 10)$, 应用 Cauchy 不等式可得

$$
\cos x_{i}=\sqrt{1-\sin ^{2} x_{i}}=\sqrt{\sum_{j \neq i} \sin ^{2} x_{j}} \geq \frac{1}{3} \sum_{j \neq i} \sin x_{j}
$$

因此

$$
\sum_{i=1}^{10} \cos x_{i} \geq \frac{1}{3} \sum_{i=1}^{10} \sum_{j \neq i} \sin x_{j}=3\left(\sum_{i=1}^{10} \sin x_{i}\right)
$$

题 2 (白俄罗斯, 2003) 设 $Q_{1}$ 是不小于 1 的有理数的集合, 函数 $f: Q_{1} \rightarrow \mathbf{R}$满足对任意 $x, y \in Q_{1}$, 均有

$$
|f(x+y)-f(x)-f(y)|<a
$$

其中 $a$ 为某个正实数. 证明: 存在实数 $q$ 使得对所有 $x \in Q_{1}$, 均有

$$
\left|\frac{f(x)}{x}-q\right|<2 a .
$$[^0]分析 先考虑 $x$ 取正整数 $n$ 的情况, 这时猜测 $q$ 取第一个初始函数值 $f(1)$是自然的. 于是需要估计 $|f(n)-n f(1)|$, 这时应想到用差分方法, 把它用差分 $f((k+1) x)-f(k x)$ 来表示, 再联想到条件便可得到非常有用的差分估计式: $|f((k+1) x)-f(k x)-f(x)|<a$.

解 先证下面关键的引理.

引理 对任意正整数 $n$ 及所有的 $x \in Q_{1}$ 有

$$
|f(n x)-n f(x)|<(n-1) a .
$$

事实上, 由条件可得

$$
|f((k+1) x)-f(k x)-f(x)|<a,
$$

因此

$$
\begin{aligned}
|f(n x)-n f(x)| & =\left|\sum_{k=1}^{n-1}(f((k+1) x)-f(k x)-f(x))\right| \\
& <\sum_{k=1}^{n-1} a=(n-1) a .
\end{aligned}
$$

回到原题. 在 (1) 中令 $x=1$, 可得

$$
n f(1)-(n-1) a \leq f(n) \leq n f(1)+(n-1) a \text {. }
$$

再在 (1) 中令 $x=\frac{m}{n} \geq 1$, 可得

$$
n f\left(\frac{m}{n}\right)-(n-1) a \leq f(m) \leq n f\left(\frac{m}{n}\right)+(n-1) a .
$$

结合 $(2)$ 和 (3) 可得

$$
m f(1)-(m+n-2) a \leq n f\left(\frac{m}{n}\right) \leq m f(1)+(m+n-2) a
$$

将 (4)两边同除以 $m$, 并令 $x=\frac{m}{n}, q=f(1)$, 则有

$$
\left|\frac{f(x)}{x}-q\right| \leq\left(1+\frac{1}{x}-\frac{2}{m}\right) a<\left(1+\frac{1}{x}\right) a \leq 2 a .
$$

题 3 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是实数, 记 $m_{i j}=x_{j}-x_{i}, 1 \leq i<j \leq n$. 证明:

$$
\sum_{1 \leq i<j \leq n} m_{i j}\left(1-m_{i j}\right) \leq \frac{n^{2}-1}{12}
$$

这个问题是笔者提供给 2012 年国家集训队选拔考试的预选题.

分析 注意到不等式的左边以差的形式出现, 因此它是关于平移变换不变
的, 即将所有的 $x_{i}$ 用 $x_{i}+t$ ( $t$ 是某个实数) 来替代, 不等式不变. 故我们可设 $\sum_{i=1}^{n} x_{i}=0$. 这称作为 “归零” . 本题的一个关键技巧是主动用归零等式消去表达式中的二次混合项.

证明 注意到不等式是在变元的平移变换下不变的, 因此不妨设

$$
\sum_{i=1}^{n} x_{i}=0
$$

否则可将所有的 $x_{i}$ 用 $x_{i}-\frac{1}{n} \sum_{i=1}^{n} x_{i}$ 来替代. 这样, 由 (1) 可得

$$
\begin{aligned}
\sum_{1 \leq i<j \leq n} m_{i j}\left(1-m_{i j}\right) & =\sum_{1 \leq i<j \leq n} m_{i j}\left(1-m_{i j}\right)-\left(\sum_{i=1}^{n} x_{i}\right)^{2} \\
& =\sum_{i=1}^{n}(2 i-n-1) x_{i}-n \sum_{i=1}^{n} x_{i}^{2} \\
& =\sum_{i=1}^{n}\left(-n\left(x_{i}-\frac{2 i-n-1}{2 n}\right)^{2}+\frac{(2 i-n-1)^{2}}{4 n}\right) \\
& \leq \sum_{i=1}^{n} \frac{(2 i-n-1)^{2}}{4 n}=\frac{n^{2}-1}{12} .
\end{aligned}
$$

题 4 (Murray Klamkin, Crux Math.) 设 $x_{1}, x_{2}, \cdots, x_{n}(n \geq 3)$ 是非负实数, 满足 $x_{1}+x_{2}+\cdots+x_{n}=1$. 求

$$
F=x_{1}^{2} x_{2}+x_{2}^{2} x_{3}+\cdots+x_{n}^{2} x_{1}
$$

的最大值.

分析 首先我们来猜测可能的最大值点. 当 $n=3$ 时, 可能的最大值点应当是三个: $\left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right),(1,0,0),\left(\frac{2}{3}, \frac{1}{3}, 0\right)$. 通过尝试易发现在第三个处的值大, 应该是最大值点. 这样对一般的 $n$, 我们自然猜测 $F$ 的最大值点是 $\left(\frac{2}{3}, \frac{1}{3}, 0, \cdots, 0\right)$ 或它的任意一个轮换, 对应的最大值是 $\frac{4}{27}$.

现在尝试用归纳法证明. 有两点值得注意: 其一, 这里的表达式是轮换对称的, 因此不能将所有变元排序, 但可用优化假设, 即设定最大变元; 其二, 因为可能取最大值的点在边界上, 肯定要有 “调整” 的想法.

本题的真正难点是 $n=3$ 的证明, 既要又调整的想法,又要思考怎样 “弃项” 将问题简化.

解 我们仅须证明 $F \leq \frac{4}{27}$.

先考虑 $n=3$ 的情况. 为简单起见, 将这种情况用引理表述.
引理 设 $a, b, c$ 是非负实数,使得 $a+b+c=1$, 则

$$
a^{2} b+b^{2} c+c^{2} a \leq \frac{4}{27}
$$

事实上, 不妨设 $a=\max (a, b, c)$, 注意到 $\left(a+\frac{c}{2}\right)+\left(b+\frac{c}{2}\right)=1$, 我们希望证明下面的不等式

$$
a^{2} b+b^{2} c+c^{2} a \leq\left(a+\frac{c}{2}\right)^{2}\left(b+\frac{c}{2}\right) \text {. }
$$

事实上, (1) 可由两个明显的不等式 $a b c \geq b^{2} c$ 及 $\frac{a^{2} c}{2} \geq \frac{c^{2} a}{2}$ 立即推出.

又由算术一几何平均值不等式有

$$
\left(\frac{a+\frac{c}{2}}{2}\right)^{2}\left(b+\frac{c}{2}\right) \leq \frac{1}{27}\left(\frac{a+\frac{c}{2}}{2}+\frac{a+\frac{c}{2}}{2}+b+\frac{c}{2}\right)^{3}=\frac{1}{27} .
$$

结合(1) 和(2) 立得引理中要证的不等式.

## 回到原题.

对 $n$ 用归纳法. 由引理知 $n=3$ 结论成立. 假设结论对 $n-1$ 成立, 现考虑 $n$ 的情况. 不妨设 $x_{3}=\max \left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$, 则

$$
x_{1}^{2} x_{2}+x_{2}^{2} x_{3}+\cdots+x_{n}^{2} x_{1} \leq\left(x_{1}+x_{2}\right)^{2} x_{3}+x_{3}^{2} x_{4}+\cdots+x_{n}^{2}\left(x_{1}+x_{2}\right) .
$$

再对 $x_{1}+x_{2}, x_{3}, \cdots, x_{n}$ 用归纳假设有

$$
\left(x_{1}+x_{2}\right)^{2} x_{3}+x_{3}^{2} x_{4}+\cdots+x_{n}^{2}\left(x_{1}+x_{2}\right) \leq \frac{4}{27} .
$$

结合 (3) 和(4) 立得结论对 $n$ 成立.

另一方面, 取 $\left(x_{1}, x_{2}, x_{3}, \cdots, x_{n}\right)=\left(\frac{2}{3}, \frac{1}{3}, 0, \cdots, 0\right)$, 得 $F=\frac{4}{27}$. 故 $F$ 的最大值为 $\frac{4}{27}$.

题 5 (台湾 TST, 2005) 求所有正整数 $n \geq 3$ 使得对于任意 $n$ 个正数 $a_{1}, a_{2}, \cdots, a_{n}$, 存在一个正整数 $M_{n}$, 满足不等式

$$
\frac{a_{1}+a_{2}+\cdots+a_{n}}{\sqrt[n]{a_{1} a_{2} \cdots a_{n}}} \leq M_{n}\left(\frac{a_{2}}{a_{1}}+\frac{a_{3}}{a_{2}}+\cdots+\frac{a_{n}}{a_{n-1}}+\frac{a_{1}}{a_{n}}\right) .
$$

分析 取一个好的试验序列是解决本题的关键. 等比序列 $\left\{k, k^{2}, \cdots, k^{n}\right\}$ 是一个最佳的选择, 这是因为当 $n$ 较大时, 左边是变化是 “快速” 的 (即非线性的), 而右边几乎是线性的, 这样满足要求的正整数 $M_{n}$ 不可能存在.

解 先证明当 $n \geq 4$ 时, 满足要求的正整数 $M_{n}$ 不存在. 若不然, 在题中的不等式中, 取 $a_{1}=k, a_{2}=k^{2}, \cdots, a_{n}=k^{n}$ 可得

$$
\frac{k+k^{2}+\cdots+k^{n}}{\sqrt[n]{k k^{2} \cdots k^{n}}} \leq M_{n}\left((n-1) k+\frac{1}{k^{n-2}}\right) .
$$

而注意到

$$
\frac{k+k^{2}+\cdots+k^{n}}{\sqrt[n]{k k^{2} \cdots k^{n}}}>\frac{k^{n}}{k^{\frac{n+1}{2}}}=k^{\frac{n-1}{2}}
$$

这样由 (1) 可得

$$
k^{\frac{n-3}{2}} \leq M_{n}\left((n-1)+\frac{1}{k^{n-1}}\right)
$$

注意到 $n \geq 4$, 在 (2) 中令 $k \rightarrow+\infty$, 便知左边趋向于无穷大, 而右边趋向于 $M_{n}(n-1)$, 矛盾!

再证明当 $n=3$ 时, 满足要求的正整数 $M_{3}$ 存在, 如 $M_{3}=3$ 就满足要求.

对任意的正实数 $a_{1}, a_{2}, a_{3}$, 记

$$
M=\frac{a_{2}}{a_{1}}+\frac{a_{3}}{a_{2}}+\frac{a_{1}}{a_{3}}
$$

则由 $\frac{a_{2}}{a_{1}}, \frac{a_{3}}{a_{2}}, \frac{a_{1}}{a_{3}}$ 均小于 $M$, 可得

$$
a_{2}>\frac{1}{M} a_{3}, \quad a_{1}>\frac{1}{M} a_{2}>\frac{1}{M^{2}} a_{3} .
$$

不妨设 $a_{3}=\max \left(a_{1}, a_{2}, a_{3}\right)$, 则由 (3) 可得

$$
\frac{a_{1}+a_{2}+a_{3}}{\sqrt[3]{a_{1} a_{2} a_{3}}}<\frac{3 a_{3}}{\sqrt[3]{\frac{1}{M^{2}} a_{3} \cdot \frac{1}{M} a_{3} \cdot a_{3}}}=3 M
$$

这就是所要证明的.

综上, 所求的 $n=3$.

题 6 求最小的实数 $\lambda$, 使得对任意的三个复数 $z_{1}, z_{2}, z_{3} \in\{z \in \mathbb{C}|| z \mid<1\}$,若 $z_{1}+z_{2}+z_{3}=0$, 则

$$
\left|z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}\right|^{2}+\left|z_{1} z_{2} z_{3}\right|^{2}<\lambda
$$

这个问题是 2016 年国家集训队的测试试题,系笔者提供.

解 1 不妨设 $\left|z_{1}\right|=\max \left\{\left|z_{1}\right|,\left|z_{2}\right|,\left|z_{3}\right|\right\}>0$. 记 $u=\frac{z_{2}}{z_{1}}, v=\frac{z_{3}}{z_{1}}$, 则

$$
|u| \leq 1, \quad|v| \leq 1, \quad u+v=-1
$$

由 (1) 知 $u, v$ 的实部均在区间 $[-1,0]$ 中, 且和为 -1 , 故不妨设 $u=-a+b i$,其中 $0 \leq a \leq \frac{1}{2}, b \in \mathbb{R}$, 则 $v=-1+a-b i$. 再由 $|v| \leq 1$ 知

$$
b^{2} \leq 2 a-a^{2}
$$

由计算易知

$$
u v=x+y i
$$

其中 $x=a(1-a)+b^{2}, y=b(2 a-1)$. 因此

$$
\begin{aligned}
& \left|z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}\right|^{2}+\left|z_{1} z_{2} z_{3}\right|^{2} \\
& =\left|z_{1}\right|^{4} \cdot|u+u v+v|^{2}+\left|z_{1}\right|^{6} \cdot|u v|^{2} \\
& <|u+u v+v|^{2}+|u v|^{2} \\
& =|-1+x+y i|^{2}+|x+y i|^{2}=2\left(x^{2}+y^{2}-x\right)+1 \\
& =2\left(\left(a(1-a)+b^{2}\right)^{2}-a(1-a)-b^{2}+b^{2}\left(2 a^{2}-1\right)^{2}\right)+1 \\
& =2\left(\left(b^{2}-a(1-a)\right)^{2}-a(1-a)\right)+1 .
\end{aligned}
$$

由 (2) 得, $-a \leq b^{2}-a(1-a) \leq a$, 并注意到 $0 \leq a \leq \frac{1}{2}$, 可知

$$
\left(b^{2}-a(1-a)\right)^{2} \leq a^{2} \leq a(1-a) .
$$

给合 (3) 和 (4) 可得

$$
\left|z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}\right|^{2}+\left|z_{1} z_{2} z_{3}\right|^{2}<1 .
$$

这表明 $\lambda$ 的最小值不超过 1 .

另一方面, 对任意 $r(0<r<1)$, 取 $\left(z_{1}, z_{2}, z_{3}\right)=(r,-r, 0)$, 可得 $\lambda>r^{2}$, 令 $r \rightarrow 1$, 可得 $\lambda \geq 1$.

故所求的最小正实数 $\lambda$ 为 1 .

解 2 设 $a=\left|z_{1}\right|^{2}, b=\left|z_{2}\right|^{2}, c=\left|z_{3}\right|^{2}$, 则

$$
\begin{aligned}
& \left|z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}\right|^{2}+\left|z_{1} z_{2} z_{3}\right|^{2} \\
& =\left(z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}\right)\left(\overline{z_{1} z_{2}}+\overline{z_{2} z_{3}}+\overline{z_{3} z_{1}}\right)+a b c \\
& =a b+b c+c a+\sum\left|z_{1}\right|^{2}\left(z_{2} \overline{z_{3}}+z_{3} \overline{z_{2}}\right)+a b c \\
& =a b+b c+c a+\sum\left|z_{1}\right|^{2}\left(\left|z_{2}+z_{3}\right|^{2}-\left|z_{2}\right|^{2}-\left|z_{3}\right|^{2}\right)+a b c \\
& =a b+b c+c a+\sum a(a-b-c)+a b c \\
& =a^{2}+b^{2}+c^{2}-a b-b c-a c+a b c \\
& =(a-1)(b-1)(c-1)+1<1
\end{aligned}
$$

由上面不等式的最后一步可看出,当 $a, b, c$ 中有一个趋于 1 时, 所研究的表达式趋于 1 , 这说明常数 1 是最佳的.

评注 解 1 的想法是先用最大模思想把三个变元问题转化成两个变元问题, 然后用条件设定好复变元的表达形式,从而将复变元问题转化成实变元问题进行计算. 解 2 是几位集训队队员的解法, 想法的关键是先研究所有变元
都是实数时, 应怎样来证明结论? 这样就可发现一个实数的恒等式, 复数情况本质上完全一样. 只是过程中要用上复数模的两个常用公式: $|z|^{2}=z \bar{z}$及 $\left|z_{1}+z_{2}\right|^{2}=\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}+z_{1} \overline{z_{2}}+z_{2} \overline{z_{1}}$.

题 7 (Titu Andreescu, Gabriel Dospinescu [1]) 设实数 $x_{1}, x_{2}, \cdots, x_{n} \in(0,1)$.对 $\{1,2, \cdots, n\}$ 的任意一个排列 $\sigma$, 证明:

$$
\sum_{i=1}^{n} \frac{1}{1-x_{i}} \geq\left(1+\frac{1}{n} \sum_{i=1}^{n} x_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{1-x_{i} x_{\sigma(i)}}\right)
$$

分析 注意到右边的第一个和式可写为 $\frac{1}{n} \sum_{i=1}^{n}\left(1+x_{i}\right)$, 自然联想到简单的关系式

$$
\frac{1}{1-x_{i}}=\left(1+x_{i}\right) \cdot \frac{1}{1-x_{i}^{2}}
$$

如果我们观察到 $\left\{1+x_{i}\right\}$ 和 $\left\{\frac{1}{1-x_{i}^{2}}\right\}$ 是两个同序的实数组, 便自然联想到切比雪夫不等式. 因此如果我们能证明

$$
\sum_{i=1}^{n} \frac{1}{1-x_{i} x_{\sigma(i)}} \leq \sum_{i=1}^{n} \frac{1}{1-x_{i}^{2}}
$$

便可用切比雪夫不等式直达目标.

解 设 $y_{1}, y_{2}, \cdots, y_{n}$ 是 $x_{1}, x_{2}, \cdots, x_{n}$ 的一个排列, 则由算术一几何平均值不等式并注意到一个十分常用的不等式 $\frac{1}{x+y} \leq \frac{1}{4 x}+\frac{1}{4 y}$, 我们有

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{1}{1-x_{i} y_{i}} & \leq \sum_{i=1}^{n} \frac{1}{1-\frac{x_{i}^{2}+y_{i}^{2}}{2}} \\
& =2 \sum_{i=1}^{n} \frac{1}{1-x_{i}^{2}+1-y_{i}^{2}} \\
& \leq \sum_{i=1}^{n}\left(\frac{1}{2\left(1-x_{i}^{2}\right)}+\frac{1}{2\left(1-y_{i}^{2}\right)}\right) \\
& =\sum_{i=1}^{n} \frac{1}{1-x_{i}^{2}} .
\end{aligned}
$$

因此, 要证本题的不等式, 我们仅须证明

$$
\sum_{i=1}^{n} \frac{1}{1-x_{i}} \geq \frac{1}{n}\left(\sum_{i=1}^{n}\left(1+x_{i}\right)\right)\left(\sum_{i=1}^{n} \frac{1}{1-x_{i}^{2}}\right)
$$

(1) 的证明是不难的. 事实上, 不妨设 $0 \leq x_{1} \leq x_{2} \leq \cdots \leq x_{n} \leq 1$ 则

$$
1+x_{1} \leq 1+x_{2} \leq \cdots \leq 1+x_{n}
$$

且

$$
\frac{1}{1-x_{1}^{2}} \leq \frac{1}{1-x_{2}^{2}} \leq \cdots \leq \frac{1}{1-x_{n}^{2}}
$$

这样直接应用切比雪夫不等式便立得 (1).

题 8 (M. Kurylo, World Math.) 设 $\left\{F_{n}\right\}$ 是一个 Fibonacci 数列: $F_{1}=$ $F_{2}=1, F_{n+2}=F_{n+1}+F_{n}$. 证明: 对任意 $x \in \mathbb{R}, n \geq 2$ 均有

$$
\sum_{k=1}^{n} F_{k}|x-k| \geq F_{n+2}+F_{n}-n-1 .
$$

首先, 我们有必要回忆一下分段线性函数 $f(x)=\sum_{i=1}^{n} k_{i}\left|x-a_{i}\right|$ 的基本性质,至少有两个结论是常用的:

1) 设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 函数 $f(x)=\sum_{i=1}^{n}\left|x-a_{i}\right|$, 则当 $n=2 k+1$ 时, $f(x)$的最小值点为 $a_{k+1}$, 其最小值为 $\sum_{i=k+2}^{n} a_{i}-\sum_{i=1}^{k} a_{i}$; 当 $n=2 k$ 时, 区间 $\left[a_{k}, a_{k+1}\right]$ 上的每一个点均为 $f(x)$ 的最小值点, 其最小值为 $\sum_{i=k+1}^{n} a_{i}-\sum_{i=1}^{k} a_{i}$.
2) 设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 而 $k_{1}, k_{2}, \cdots, k_{n}$ 都是正实数, 则函数 $f(x)=$ $\sum_{i=1}^{n} k_{i}\left|x-a_{i}\right|$ 的最小值在 $x=a_{i_{0}+1}$ 取到, 其中的 $i_{0}$ 是满足

$$
k_{1}+k_{2}+\cdots+k_{i} \leq k_{i+1}+k_{i+2}+\cdots+k_{n}
$$

的最大正整数 $i$.

证明 由 Fibonacci 数列 $\left\{F_{n}\right\}$ 的一个著名性质

$$
F_{1}+F_{2}+\cdots+F_{n}=F_{n+2}-1
$$

可得

$$
F_{1}+F_{2}+\cdots+F_{n-2}-F_{n-1}-F_{n}=-F_{n-1}-1<0
$$

因此

$$
F_{1}+F_{2}+\cdots+F_{n-2}<F_{n-1}+F_{n}
$$

但显然

$$
F_{1}+F_{2}+\cdots+F_{n-2}+F_{n-1}>F_{n}
$$

故函数 $f(x)=\sum_{k=1}^{n} F_{k}|x-k|$ 的最小值为

$$
f(n-1)=(n-2) F_{1}+\cdots+F_{n-2}+F_{n} .
$$

再用数学归纳法易证明

$$
(n-2) F_{1}+\cdots+F_{n-2}+F_{n}=F_{n+2}+F_{n}-n-1 .
$$

这样便得到了我们要证的不等式.

补注 上例用到了分段线性函数的基本性质 2). 这里再介绍基本性质 1)的一个应用.

例 设 $a_{1}, a_{2}, \cdots, a_{2 n+1}(n \geq 1)$ 是和为 0 的 $2 n+1$ 个实数, $y$ 是函数 $f(x)=$ $\sum_{i=1}^{2 n+1}\left|x-a_{i}\right|$ 的最小值点. 证明:

$$
y \leq \frac{1}{2(n+1)} \sum_{i=1}^{2 n+1}\left|a_{i}\right|
$$

证明 不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{2 n+1}$, 则 $y=a_{n+1}$. 因此, 我们仅须证明

$$
a_{n+1} \leq \frac{1}{2(n+1)} \sum_{i=1}^{2 n+1}\left|a_{i}\right|
$$

如果 $a_{n+1} \leq 0$, 则 (1) 显然成立. 因此不妨设

$$
a_{1} \leq \cdots \leq a_{k}<0 \leq a_{k+1} \leq \cdots \leq a_{n+1} \leq \cdots \leq a_{2 n+1}
$$

这时由条件 $a_{1}+a_{2}+\cdots+a_{2 n+1}=0$ 可得

$$
\begin{aligned}
\sum_{i=1}^{2 n+1}\left|a_{i}\right| & =-a_{1}-\cdots-a_{k}+a_{k+1} \cdots+a_{n+1}+\cdots+a_{2 n+1} \\
& =2\left(a_{k+1} \cdots+a_{n+1}+\cdots+a_{2 n+1}\right) \\
& \geq 2\left(a_{n+1}+\cdots+a_{2 n+1}\right) \geq 2(n+1) a_{n+1}
\end{aligned}
$$

这就是要证的不等式 (1).

题 9 (Gabriel Dospinescu [1]) 设 $n \geq 2$ 是整数, 求最大的正实数 $m_{n}$ 和最小的正实数 $M_{n}$ 使待对任何正实数 $x_{1}, x_{2}, \cdots, x_{n}$ 有

$$
m_{n} \leq \sum_{i=1}^{n} \frac{x_{i}}{x_{i-1}+2(n-1) x_{i}+x_{i+1}} \leq M_{n}
$$

其中 $x_{0}=x_{n}, x_{n+1}=x_{1}$.

分析 首先猜测 $m_{n}$ 和 $M_{n}$ 值及相应的可能极值点. 等变量的情况是优先考虑的: 当 $x_{1}=x_{2}=\cdots=x_{n}$ 时, 和式的值等于 $\frac{1}{2}$. 这是可能的最大值还是最小值呢? 再取 $n=3, x_{1}=x_{2}=1, x_{3}=0$. 这时和式的值是 $\frac{2}{5}<\frac{1}{2}$. 这说明等变量处可能取到最大值, 亦即猜测 $M_{n}=\frac{1}{2}$.
现在可能的最大下界自然应猜测在 $x_{1}=1, x_{2}=\varepsilon, \cdots, x_{n}=\varepsilon^{n-1}$ 当 $\varepsilon \rightarrow 0$时取得, 这是因为 $\left(1, \varepsilon, \cdots, \varepsilon^{n-1}\right) \rightarrow(1,0,0, \cdots, 0)$, 而后者是一个特殊的边界点一顶点. 这样 $m_{n}$ 的值就可能等于 $\frac{1}{2(n-1)}$.

解 记 $S=\sum_{i=1}^{n} \frac{x_{i}}{x_{i-1}+2(n-1) x_{i}+x_{i+1}}$. 整个解答过程分两部分:

1) 先证明 $S$ 的最优下界是 $\frac{1}{2(n-1)}$.

事实上,注意到下面显然的不等式

$$
x_{i-1}+2(n-1) x_{i}+x_{i+1} \leq 2(n-1)\left(\sum_{i=1}^{n} x_{i}\right), i=1,2, \cdots, n \text {. }
$$

我们有

$$
S \geq \sum_{i=1}^{n} \frac{x_{i}}{2(n-1)\left(\sum_{i=1}^{n} x_{i}\right)}=\frac{1}{2(n-1)}
$$

另一方面, 取 $x_{1}=1, x_{2}=\varepsilon, \cdots, x_{n}=\varepsilon^{n-1}$, 这时 $S$ 的值等于

$$
\frac{1}{\varepsilon^{n-1}+2(n-1)+\varepsilon}+\frac{(n-2) \varepsilon}{1+2(n-1) \varepsilon+\varepsilon^{2}}+\frac{\varepsilon^{n-1}}{\varepsilon^{n-2}+2(n-1) \varepsilon^{n-1}+1}
$$

再令 $\varepsilon \rightarrow 0$, 则 $S \rightarrow \frac{1}{2(n-1)}$.

这就说明了 $\frac{1}{2(n-1)}$ 是 $S$ 的最大下界, 即 $m_{n}=\frac{1}{2(n-1)}$.

2) 再证明 $S$ 的最大值是 $\frac{1}{2}$.

为此需要一个引理:

引理 (罗马尼亚TST, 1999) 设正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $a_{1} a_{2} \cdots a_{n}=1$, 则

$$
\frac{1}{n-1+a_{1}}+\frac{1}{n-1+a_{2}}+\cdots+\frac{1}{n-1+a_{n}} \leq 1 .
$$

引理证明 记 $r=1-\frac{1}{n}$. 由算术一几何平均值不等式和条件可得

$$
a_{1}^{r}+\cdots+a_{i-1}^{r}+a_{i+1}^{r}+\cdots+a_{n}^{r} \geq(n-1) a_{i}^{-\frac{1}{n}}
$$

因此

$$
\sum_{i=1}^{n} \frac{a_{i}}{n-1+a_{i}}=\sum_{i=1}^{n} \frac{a_{i}^{r}}{(n-1) a_{i}^{-\frac{1}{n}}+a_{i}^{r}} \geq \sum_{i=1}^{n} \frac{a_{i}^{r}}{a_{1}^{r}+a_{2}^{r}+\cdots+a_{n}^{r}}=1 .
$$

这等价于引理中要证的不等式.

回到原题. 记 $a_{i}=\frac{\sqrt{x_{i-1} \cdots x_{i+1}}}{x_{i}}$, 则 $a_{1} a_{2} \cdots a_{n}=1$.

这时由引理便得

$$
2 S \leq \sum_{i=1}^{n} \frac{2 x_{i}}{2 \sqrt{x_{i-1} \cdot x_{i+1}}+2(n-1) x_{i}}=\sum_{i=1}^{n} \frac{1}{n-1+a_{i}} \leq 1
$$

故 $S \leq \frac{1}{2}$. 又当 $x_{1}=x_{2}=\cdots=x_{n}$ 时, $S=\frac{1}{2}$. 所以 $M_{n}=\frac{1}{2}$.

题 10 (Kober 不等式) 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数, 证明:

$$
(n-1) \sum_{i=1}^{n} a_{i}^{2}+n\left(a_{1} a_{2} \cdots a_{n}\right)^{\frac{2}{n}} \geq\left(\sum_{i=1}^{n} a_{i}\right)^{2}
$$

分析 直觉告诉我们 $\left(a_{1} a_{2} \cdots a_{n}\right)^{\frac{2}{n}}$ 最不易处理, 于是我们就用齐次性把它 “隐” 去, 可设 $a_{1} a_{2} \cdots a_{n}=1$. 再注意到本问题取等号条件并不唯一, 如当 $a_{1}=a_{2}=\cdots=a_{n}$ 或其中有一个为 0 ,其余 $n-1$ 个均相等时等号成立. 这时宜用调整法. 一种非常合理的调整策略是：设定最小变元，把其它元都调为相等. 由于调整过程需要若干步, 因此结合用归纳法可使问题大大简化.

解 1 由齐次性,不妨设 $a_{1} a_{2} \cdots a_{n}=1$. 这时要证不等式转化为

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\left(\sum_{i=1}^{n} a_{i}\right)^{2}-(n-1) \sum_{i=1}^{n} a_{i}^{2}-n \leq 0
$$

现对 $n$ 用归纳法.

当 $n=1,2$ 时, 结论显然成立.

假设结论对 $n-1$ 成立, 下证结论对 $n$ 成立.

不妨设 $a_{1}=\min \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 并记 $G=\sqrt[n-1]{a_{2} \cdots a_{n}}$. 这时要证

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \leq 0 .
$$

我们只须证明

$$
f\left(a_{1}, a_{2}, \cdots, a_{n}\right) \leq f\left(a_{1}, G, \cdots, G\right),
$$

和

$$
f\left(a_{1}, G, \cdots, G\right) \leq 0 .
$$

先证 (1): 易知 (1) 可等价写为

$$
(n-1) \sum_{i=2}^{n} a_{i}^{2}-\left(\sum_{i=2}^{n} a_{i}\right)^{2} \geq 2 a_{1}\left(\sum_{i=2}^{n} a_{i}-(n-1) G\right)
$$

注意到

$$
a_{1} \leq G, \quad \sum_{i=2}^{n} a_{i} \geq(n-1) G
$$

要证 (3), 我们仅须证明

$$
(n-1) \sum_{i=2}^{n} a_{i}^{2}-\left(\sum_{i=2}^{n} a_{i}\right)^{2} \geq 2 G\left(\sum_{i=2}^{n} a_{i}-(n-1) G\right)
$$

由于 (4) 关于 $a_{2}, \cdots, a_{n}$ 是齐次的, 因此不妨设 $G=1$.

这时要证不等式 (4) 就等价于

$$
(n-2) \sum_{i=2}^{n} a_{i}^{2}-\left(\sum_{i=2}^{n} a_{i}\right)^{2}+(n-1) \geq 2 \sum_{i=2}^{n} a_{i}-\sum_{i=2}^{n} a_{i}^{2}-(n-1) .
$$

现对 $a_{2}, \cdots, a_{n}$ 用归纳假设知 (5) 的左边大于等于 0 , 故要证 (5), 我们只须证明

$$
2 \sum_{i=2}^{n} a_{i}-\sum_{i=2}^{n} a_{i}^{2}-(n-1) \leq 0 .
$$

这等价于

$$
\sum_{i=2}^{n}\left(a_{i}-1\right)^{2} \geq 0
$$

它是显然成立的,故 (1) 得证.

再证 (2):

因为 $a_{1} a_{2} \cdots a_{n}=1$, 所以 $a_{1}=\frac{1}{G^{n-1}}$. 这时易知 (2) 等价于

$$
\frac{n-2}{G^{2 n-2}}+n \geq \frac{2 n-2}{G^{n-2}}
$$

事实上, 由算术一几何平均值不等式, 我们有

$$
\begin{aligned}
\frac{n-2}{G^{2 n-2}}+n & =\underbrace{\frac{1}{G^{2 n-2}}+\cdots+\frac{1}{G^{2 n-2}}}_{n-2}+\underbrace{1+\cdots+1}_{n} \\
& \geq(2 n-2) \sqrt[2 n-2]{\left(\frac{1}{G^{2 n-2}}\right)^{n-2} \cdot 1^{n}}=\frac{2 n-2}{G^{n-2}}
\end{aligned}
$$

(6) 得证, 从而 (2) 得证.

解 2 (饶家鼎) 由齐次性, 不妨设 $a_{1} a_{2} \cdots a_{n}=1$. 这时要证不等式转化为

$$
g\left(a_{1}, a_{2}, \cdots, a_{n}\right)=(n-1) \sum_{i=1}^{n} a_{i}^{2}+n-\left(\sum_{i=1}^{n} a_{i}\right)^{2} \geq 0
$$

现对 $n$ 用归纳法.

当 $n=1,2$ 时, 结论显然成立.

假设结论对 $n-1$ 成立, 下证结论对 $n$ 成立. 不妨设 $a_{1} \geq a_{2} \geq \cdots \geq a_{n}$.

若 $a_{n} \geq 1$, 则必有 $a_{1}=a_{2}=\cdots=a_{n}=1$. 此时结论显然成立. 下面只须考虑 $a_{n}<1$ 的情况.

a) 若 $a_{n-1} \geq 1$, 则 $a_{i} \geq 1, i=1,2, \cdots, n-1$.

由 Cauchy 不等式可得

$$
(n-1)\left(a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}\right) \geq\left(a_{1}+a_{2}+\cdots+a_{n-1}\right)^{2} .
$$

这时要证结论对 $n$ 成立, 只须证明:

$$
\frac{n-2}{2} a_{n}^{2}+\frac{n}{2} \geq a_{n}\left(a_{1}+a_{2}+\cdots+a_{n-1}\right) .
$$

事实上, 由广义贝努里不等式有

$$
a_{1}+a_{2}+\cdots+a_{n-1} \leq a_{1} a_{2} \cdots a_{n-1}+n-2=\frac{1}{a_{n}}+n-2
$$

故

$$
\begin{aligned}
a_{n}\left(a_{1}+a_{2}+\cdots+a_{n-1}\right) & \leq 1+(n-2) a_{n} \\
& \leq 1+\frac{n-2}{2}\left(a_{n}^{2}+1\right) \\
& =\frac{n-2}{2} a_{n}^{2}+\frac{n}{2},
\end{aligned}
$$

(6) 得证.

b) 若 $a_{n-1}<1$, 我们断言下面两个不等式 (7) 和 (8) 至少有一个成立.

$$
\begin{aligned}
& g\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq g\left(a_{1} a_{n}, a_{2}, \cdots, a_{n-1}, 1\right) \\
& g\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq g\left(a_{1}, a_{2}, \cdots, a_{n-1} a_{n}, 1\right)
\end{aligned}
$$

事实上, (7) 等价于

$$
(n-1)\left(1-a_{1}^{2}\right)\left(1-a_{n}^{2}\right) \leq\left(1-a_{1}\right)\left(1-a_{n}\right)\left\{\left(1+a_{1}\right)\left(1+a_{n}\right)+2\left(S-a_{1}-a_{n}\right)\right\},
$$

其中 $S=\sum_{i=1}^{n} a_{i}$.

注意到 $a_{1} \geq 1 \geq a_{n}$, 化简 (9) 知 (7) 等价于

$$
\frac{n-2}{2}\left(1+a_{1}\right)\left(1+a_{n}\right)+a_{1}+a_{n} \geq S
$$

同理 (8) 等价于

$$
\frac{n-2}{2}\left(1+a_{n-1}\right)\left(1+a_{n}\right)+a_{n-1}+a_{n} \leq S .
$$

因 (10) 式左边显然不小于 (11) 式左边, 故 (10) 和 (11) 中至少有一个成立,这也证明了 (7) 和 (8) 中至少有一个成立.

由 (7) 和 (8) 中至少有一个成立, 说明存在乘积为 1 的 $n-1$ 个正实数 $b_{1}, b_{2}, \cdots, b_{n-1}$ 使得

$$
g\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq g\left(b_{1}, b_{2}, \cdots, b_{n-1}, 1\right)
$$

现在我们只须证明 $g\left(b_{1}, b_{2}, \cdots, b_{n-1}, 1\right) \geq 0$, 亦即

$$
(n-1) \sum_{i=1}^{n-1} b_{i}^{2}+2 n-1 \geq\left(\sum_{i=1}^{n-1} b_{i}+1\right)^{2}
$$

而由归纳假设, 我们有

$$
(n-2) \sum_{i=1}^{n-1} b_{i}^{2}+n-1 \geq\left(\sum_{i=1}^{n-1} b_{i}\right)^{2}
$$

这样要证 (12), 只须证明

$$
\sum_{i=1}^{n-1} b_{i}^{2}+n-1 \geq 2 \sum_{i=1}^{n-1} b_{i}
$$

这等价于 $\sum_{i=1}^{n-1}\left(b_{i}-1\right)^{2} \geq 0$, 显然成立. 故 (12) 成立.

综上, 说明结论对 $n$ 成立.

补注 本题中的不等式有些文献上又叫 Turkevici 不等式. 我们这里之所以叫它 Kober 不等式, 一方面是沿用《解析不等式》(D.S. 密特利诺维奇著, 中译本, 科学出版社, 1987) 一书的叫法, 另一方面是注意到 Kober 在他的那篇文章 (刊于 Proc. Amer. Math. Soc. 9, 1958) 中提出了算术一几何平均值不等式的一个加强形式 (本题的等价形式), 近期被应用到高维几何不等式的稳定性研究中.

Kober 不等式的一个推广是下面的 Surányi 不等式:

设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数, 则

$$
(n-1) \sum_{i=1}^{n} a_{i}^{n}+n \prod_{i=1}^{n} a_{i} \geq\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} a_{i}^{n-1}\right) .
$$

最近, M.Bencze 进一步把 Surányi 不等式不等式推广到了凸函数, 他的结果可表述为:

设 $a_{1}, a_{2}, \cdots, a_{n}$ 是区间 $I$ 上的正实数, $f$ 和 $f^{\prime}$ 都是 $I$ 上的凸函数, 则

$$
(n-1) \sum_{i=1}^{n} f\left(a_{i}\right)+n f\left(\frac{1}{n} \sum_{i=1}^{n} a_{i}\right) \geq \sum_{1 \leq i, j \leq n} f\left(\frac{(n-1) a_{i}+a_{j}}{n}\right) .
$$

下面来看一些组合问题.

题 11 (环球城市联赛, 2015) 现有 15 个和为 0 的的整数, 其中至多有一个为 0 . 现在一张纸上写出这些数的所有 7 元子集的元素和, 另一张纸上写出所有 8 元子集的元素之和. 问两张纸上写出的和数整体是否可能完全相同,包括各数的出现次数?

分析和解 考虑一般的元素之和为 0 的 $2 n+1$ 元集合 $X$, 它的所有 $n$ 元子集构成的集族记为 $F_{1}$, 它的所有 $n+1$ 元子集构成的集族记为 $F_{2}$. 对任意一
个 $n$ 元子集 $A \in F_{1}, A$ 的补集 $X \backslash A \in F_{2}, A$ 的所有元素之和与补集 $X \backslash A$ 的元素之和为 0 .

因此我们取 $X$ 是关于原点对称的集合 (即 $X=-X$ ), 则 $-(X \backslash A)$ 仍然属于 $F_{2}$, 且 $A$ 和 $-(X \backslash A)$ 的元素之和相等. 这样映射 $A \rightarrow-(X \backslash A)$ 是 $F_{1}$ 和 $F_{2}$上的一个一一映射, 从而两组和数完全相同.

题 12 (匈牙利, 2011) 凸 2011 边形满足任意四点不共圆,过每三个顶点作一个圆。若多边形有在圆外的顶点, 则称此圆为 “瘦的” , 反之, 则称为 “胖的”. 问胖圆和瘦圆哪个多?

分析和解 对这 2011 个顶点中的任意四点 $A, B, C, D$. 不妨设

$$
\angle A+\angle C<180^{\circ} \text {. }
$$

这时, 点 $C$ 在 $\triangle A B D$ 的外接圆外, 而点 $A$ 在 $\triangle B C D$ 的外接圆外. 这说明由 $A, B, C, D$. 确定的 4 个圆中至少有 2 个瘦圆. 故瘦圆个数不小于胖圆个数.

下面进一步证明瘦圆个数不等于胖圆个数.

若瘦圆个数等于胖圆个数, 记为 $a$. 由于这 2011 个顶点可确定 $\mathrm{C}_{2011}^{4}$ 个四点组, 从而可确定 $4 \mathrm{C}_{2011}^{4}$ 个圆, 而任何一个三点组确定的圆出现在 $2011-3=2008$个四点组中, 故

$$
a=\frac{1}{2} \cdot \frac{4 \mathrm{C}_{2011}^{4}}{2008}
$$

但这不是整数, 矛盾!

综上便知瘦圆数大于胖圆数.

题 13 设整数 $n \geq 2, X=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 其中 $a_{i}$ 是正整数,且 $a_{i} \geq n, i=$ $1,2, \cdots, n+1$. 证明: 存在 $1 \leq i \neq j \leq n+1$ 使得 $\left[a_{i}, a_{j}\right]>n^{2}$.

分析 要证一个存在性的不等式, 想到用抽屈原理. 但 $a_{i}$ 是无界的, 因此取倒数, 这时 $\frac{1}{a_{i}}$ 变成有界量了, 从而方便构造抽屈.

证明 不妨设 $a_{1}>a_{2}>\cdots>a_{n+1} \geq n$, 则

$$
0<\frac{1}{a_{1}} \leq \frac{1}{a_{i}} \leq \frac{1}{n}, \quad i=1,2, \cdots, n+1 .
$$

现将区间 $\left[\frac{1}{a_{1}}, \frac{1}{n}\right]$ 等分成 $n$ 个小区间, 则每个小区间的长度小于 $\frac{1}{n^{2}}$.

如果存在 $a_{i}(2 \leq i \leq n+1)$ 使得 $\frac{1}{a_{i}}$ 落在第一个小区间内, 则有

$$
0<\frac{1}{a_{i}}-\frac{1}{a_{1}}<\frac{1}{n^{2}}
$$

如果所有 $a_{i}(2 \leq i \leq n+1)$ 使得 $\frac{1}{a_{i}}$ 均不落在第一个小区间内, 则由抽屉原理知存在 $2 \leq i<j \leq n+1$, 使得

$$
0<\frac{1}{a_{j}}-\frac{1}{a_{i}}<\frac{1}{n^{2}}
$$

这样, 不管是哪种情况, 总存在 $1 \leq i<j \leq n+1$, 使得

$$
0<\frac{1}{a_{j}}-\frac{1}{a_{i}}<\frac{1}{n^{2}}
$$

因为对任意正整数 $a, b$ 有 $a b=(a, b)[a, b]$, 故由 (1) 可得

$$
0<\frac{\frac{a_{i}-a_{j}}{\left(a_{i}, a_{j}\right)}}{\left[a_{i}, a_{j}\right]}<\frac{1}{n^{2}}
$$

又注意到 $\frac{a_{i}-a_{j}}{\left(a_{i}, a_{j}\right)}$ 是正整数, 故由 (2) 立得 $\left[a_{i}, a_{j}\right]>n^{2}$.

题 14 (全苏联冬令营, 1987) 设 $\left\{a_{n}\right\}$ 是递增的正整数序列, $a_{1}=1$, 且对任意正整数 $n$ 有 $a_{n+1} \leq 2 n$. 证明:任何不小于 2 的整数都可表示为 $a_{i}+a_{j}$ 的形式,其中 $i$ 可以等于 $j$.

分析 注意对递增 (这里均指严格递增) 的正整数序列 $\left\{a_{n}\right\}$, 若该序列中小于 $k$ 的项数至多为 $m$ 项,则 $a_{m+1} \geq k$. 这是整数离散性的一种表现.

证明 用反证法. 假设结论不成立, 则存在 $k>2$ 无法表为 $a_{i}+a_{j}$ 的形式.

1) 当 $k$ 为奇数时, 数对 $(1, k-1),(2, k-2), \cdots,\left(\frac{k-1}{2}, \frac{k+1}{2}\right)$ 的每一组数中,都至多有一个在序列 $\left\{a_{n}\right\}$ 中, 故序列 $\left\{a_{n}\right\}$ 中小于 $k$ 的至多有 $\frac{k-1}{2}$ 项.

$2)$ 当 $k$ 为偶数时, 数对 $(1, k-1),(2, k-2), \cdots,\left(\frac{k}{2}-1, \frac{k}{2}+1\right)$ 的每一组数中, 都至多有一个在序列 $\left\{a_{n}\right\}$ 中, 而 $\frac{k}{2}$ 也不能属于 $\left\{a_{n}\right\}$ 中. 故序列 $\left\{a_{n}\right\}$ 中小于 $k$ 的至多有 $\frac{k}{2}-1$ 项.

综上, 序列 $\left\{a_{n}\right\}$ 中小于 $k$ 的至多有 $\left\lfloor\frac{k-1}{2}\right\rfloor$ 项. 故

$$
a_{\left\lfloor\frac{k-1}{2}\right\rfloor+1} \geq k .
$$

但

$$
a_{\left\lfloor\frac{k-1}{2}\right\rfloor+1} \leq 2\left\lfloor\frac{k-1}{2}\right\rfloor \leq k-1,
$$

矛盾! 这说明对任何大于 2 的整数可表为 $a_{i}+a_{j}$ 的形式, 又 $2=a_{1}+a_{1}$, 故对一切 $k \geq 2$ 的整数结论成立.

题 15 (伊朗, 2012) 求所有正整数序列 $\left\{a_{n}\right\}$, 使得对任意 $i \leq j$ 均有 $a_{i} \leq a_{j}$且对任意的正整数 $i, j, i+j$ 的正因数个数与 $a_{i}+a_{j}$ 的正因数的个数相等.
分析 很自然猜测自然数序列 $n$ 是满足条件的唯一的序列. 注意到 $a_{1}=1$,如果我们能证明 $\left\{a_{n}\right\}$ 严格递增且在一个无穷子序列上的每一个值等于下标的标号数, 则我们就证明了 $a_{n}=n$.

解 首先证明 $\left\{a_{n}\right\}$ 严格递增.

若不然, 假设存在正整数 $i$ 使得 $a_{i}=a_{i+1}$. 取 $j=p-i$, 其中 $p$ 是一个大于 $i+1$ 的素数. 这时由 $i+j$ 是素数知 $a_{i}+a_{j}$ 也是素数. 因为 $a_{i}=a_{i+1}$, 所以 $a_{i+1}+a_{j}$ 也是素数, 从而 $i+1+j$ 也是素数. 这样我们找到了相邻两整数 $i+j$和 $i+1+j$ 均是素数, 矛盾!

再证 $a_{n}=n$.

显然 $a_{1}=1$. 取 $i=j=2^{p-2}$, 其中 $p$ 是不小于 3 的素数, 则 $i+j=2 i=2^{p-1}$的正因数的个数为 $p$. 故 $a_{i}+a_{j}=2 a_{i}$ 的正因数的个数也为 $p$. 这样, $2 a_{i}$ 必须等于 $2^{p-1}$. 故 $a_{2^{p-2}}=2^{p-2}$. 这说明两个严格递增的正整数序列 $a_{n}$ 和 $\{n\}$ 的首项相等, 且在一个无穷子序列 $\left\{2^{p-2}\right\}$ 上的值对应相等. 故对所有正整数 $n$ 均有 $a_{n}=n$.

题 16 (全苏联国家队夏令营, 1985) 在无穷大方格纸上标出了 $n$ 个方格,称两个方格为 “相邻的” , 如果它们具有公共边或公共顶点. 证明: 可以从所标出的方格中挑选出 $k \geq \frac{n}{4}$ 个方格, 使得它们之中任何两个都不相邻.

证明 平面上的每个方格用整点 $(x, y) \in \mathbb{Z}^{2}$ 表示. 将平面上的整点分划成如下的四个集合:

$$
\begin{aligned}
& A_{00}=\{(x, y) \mid x, y \equiv 0, \quad(\bmod 2)\} \\
& A_{10}=\{(x, y) \mid x \equiv 1, y \equiv 0 \quad(\bmod 2)\} \\
& A_{01}=\{(x, y) \mid x \equiv 0, y \equiv 1 \quad(\bmod 2)\} \\
& A_{11}=\{(x, y) \mid x, y \equiv 1 \quad(\bmod 2)\},
\end{aligned}
$$

则这四个集合中的每个集合中整点对应的方格两两不相邻.

设标出的方格集为 $S$, 则

$$
\bigcup_{0 \leq i, j \leq 1}\left(A_{i j} \cap S\right)=S
$$

故必有一个 $A_{i j}(i, j \in\{0,1\}$ 使得

$$
\left|A_{i j} \cap S\right| \geq \frac{|S|}{4}=\frac{n}{4}
$$

因此取 $A_{i j} \cap S$ 中的方格满足要求.

题 17 (塞尔维亚, 2012) 设 $K$ 是平面直角坐标系上的整点集. 问: 是否存在双射 $f: \mathbb{N}^{*} \rightarrow K$ ，使得对任意的 $a, b, c \in \mathbb{N}^{*}$ ，若 $(a, b, c)>1$, 则 $f(a), f(b), f(c)$不共线?

本题要用整点集是一个可列集 (通俗地说,即可以用自然数来编号) 这一结论. 尽管它直观上是好理解的, 似乎还是有点超越中学生的知识范围. 幸好参加新星五一班的不少同学熟悉这个结论. 在这一结论的基础上, 我们通过归纳构造证明存在满足要求的双射.

分析和解 首先将平面上的整点編号, 记为 $K=\left\{A_{1}, A_{2}, \cdots\right\}$. 现要给出 $\mathbb{N}^{*}$到 $K$ 的一个满足要求的一一映射, 本质上是要我们重新给出 $K$ 的一个编号. 先摸索着前进. 当然取 $f(1)=A_{1}, f(2)=A_{2}, f(3)=A_{3}, f(4)=A_{4}, f(5)=A_{5}$.

但 $f(6)$ 呢? 因为 $(2,4,6)=2$, 因此 $f(6)$ 不能在直线 $A_{2} A_{4}$ 上, 这时我们取 $f(6)$ 为 $K$ 中除去 $A_{1} \sim A_{5}$ 且不在直线 $A_{2} A_{4}$ 上的下标最小的 $A_{j}$ (事实上,如果点 $A_{6}$ 在直线 $A_{2} A_{4}$ 上, 取 $f(6)=A_{7}$; 如果点 $A_{6}$ 不在直线 $A_{2} A_{4}$ 上, 仍取 $\left.f(6)=A_{6}\right)$.

再考虑 $f(7)$ 的值. 因 7 是素数, 这样我们取 $f(7)$ 为 $K$ 中除去 $f(1) \sim f(6)$对应点的具有最小下标 $j$ 的点 $A_{j}$.

现在一般的 $f(n)$ 的构造就不难了. 事实上, 假设 $f(1), f(2), \cdots, f(n-1)$己被选定对应点, 则取 $f(n)=A_{m}$, 其中下标 $m$ 为满足对任意 $i, j \leq n$有 $(i, j, n)>1$, 点 $A_{m}$ 不在直线 $f(i) f(j)$ 上 (因这样的直线的条数有限, $A_{m}$ 一定存在) 的所有下标中的最小者. 特别地, 对素数 $p, f(p)$ 对应着 $K$ 中没有被选取的具有最小下标的整点.

显然, 这样构造的 $f$ 确是 $\mathbb{N}^{*}$ 到 $K$ 的一个满足条件的一一映射.

## 参考文献

[1] T. Andreescu, V. Cirtoaje, G. Dospinescu and M. Lascu, Old and New inequalities, GIL Publishing House, 2004.


[^0]:    收稿日期: 2016-05-22.

