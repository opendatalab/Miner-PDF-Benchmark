$$
\text { 数学新星网 } \% \text { 学生专栏 }
$$

www.nsmath.cn/xszl

# 2019 年罗马尼亚大师杯 $(\mathrm{RMM})$代数部分预选题 

依嘉<br>(中国人民大学附属中学, 100080)<br>指导教师: 张端阳

罗马尼亚大师杯 (RMM) 是由罗马尼亚数学会主办的一场国际邀请赛, 中国、美国、俄罗斯和一些罗马尼亚周边的国家会受邀参加, 是一个在国际上十分重要的比赛. 2019 年的 RMM 于 2 月 20 日 2 月 25 日举行, 由上海市组队参加.

这篇文章为 2019 年 RMM 代数部分的预选题, 共 3 道题, 其中第三题为 RMM 的第五题. 本人认为预选题中第一题相对简单, 后两道题较难, 整体难度略高于 CMO. 此外, 第一题和第三题均为函数方程.

直于本人水平, 文中若有不当之处或新颖解法, 敬请指教.

## I. 试 题

1. 求映射 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对 $\forall a, b \in \mathbb{R}$, 均有

$$
f\left(a^{2}+a b+f\left(b^{2}\right)\right)=a f(b)+b^{2}+f\left(a^{2}\right) .
$$

2. 给定 $n \in \mathbb{N}^{*}$. 将 $\{1,2, \cdots, 2 n\}$ 划分为两个 $n$ 元子集 $A, B$. 若存在常数 $c_{n}$, 使得我们无论怎么划分, 一定存在 $A$ 中元素的排列 $a_{1} \sim a_{n}$ 和 $B$ 中元素的排列 $b_{1} \sim b_{n}$, 使得

$$
\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2} \geq c_{n}
$$

求 $c_{n}$ 的最大值.

3. 求函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对 $\forall x, y \in \mathbb{R}$, 均有

$$
f(x+y f(x))+f(x y)=f(x)+f(2019 y) .
$$

修订日期: 2020-07-06.

## II . 解答与评注

1. 求映射 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对 $\forall a, b \in \mathbb{R}$, 均有

$$
f\left(a^{2}+a b+f\left(b^{2}\right)\right)=a f(b)+b^{2}+f\left(a^{2}\right) .
$$

解 1 (1) 令 $a=0$, 有

$$
f\left(f\left(b^{2}\right)\right)=b^{2}+f(0) \text {. }
$$

令 $a=-1, b=1$, 有

$$
f(f(1))=-f(1)+1+f(1)=1 \text {. }
$$

由(1)知 $f(f(1))=1+f(0)$. 因此

$$
f(0)=0
$$

由(1), (3)知

$$
f\left(f\left(b^{2}\right)\right)=b^{2} .
$$

(2) 在 $b \neq 0$ 时. 取 $a=-\frac{f\left(b^{2}\right)}{b}$, 则 $a b+f\left(b^{2}\right)=0$. 因此

$$
f\left(a^{2}+a b+f\left(b^{2}\right)\right)=f\left(a^{2}\right) .
$$

此时

$$
-\frac{f\left(b^{2}\right)}{b} f(b)+b^{2}=0 \Rightarrow f(b) f\left(b^{2}\right)=b^{3}
$$

又 $b=0$ 时(5)仍成立. 因此 $f(b) f\left(b^{2}\right)=b^{3}$ 恒成立.

令 $a+b=0$, 有

$$
f\left(f\left(b^{2}\right)\right)=b^{2}-b f(b)+f\left(b^{2}\right) .
$$

将(4)带入(6), 知 $f\left(b^{2}\right)=b f(b)$. 结合(5)知 $f(b)= \pm b$.

(3) 若 $f(a)=a, f(b)=-b$, 且 $a, b \neq 0$, 则由(5)知 $f\left(a^{2}\right)=a^{2}, f\left(b^{2}\right)=-b^{2}$.代回原式, 有

$$
f\left(a^{2}+a b-b^{2}\right)=-a b+b^{2}+a^{2} .
$$

(i). 若 $f\left(a^{2}+a b-b^{2}\right)=a^{2}+b^{2}-a b$, 则 $b=0$ 或 $a=b$ 矛盾.

(ii). 若 $f\left(a^{2}+a b-b^{2}\right)=b^{2}-a b-a^{2}$, 则 $a=0$ 矛盾.

所以 $f(x)=x$ 对 $\forall x$ 成立或 $f(x)=-x$ 对 $\forall x$ 成立.

经检验 $f(x) \equiv x$ 和 $f(x) \equiv-x$ 均为原方程的解.

解 2 用 $P(a, b)$ 表示原方程.
考虑方程 $P(a, b)$ 和 $P(-a-b, b)$, 作差得到

$$
f\left((a+b)^{2}\right)-f\left(a^{2}\right)=(2 a+b) f(b) .
$$

记这个方程为 $Q(a, b)$. 考虑 $Q(a, b)$ 和 $Q(a,-2 a-b)$, 作差知

$$
(2 a+b) f(b)=-b f(-2 a-b) .
$$

即

$$
\frac{f(b)}{b}=\frac{f(-2 a-b)}{-2 a-b}
$$

对 $\forall a, b$ 成立.

因此 $\exists c$ 使 $f(x) \equiv c x$, 代回原题检验, 知 $c= \pm 1$.

所以方程的解为 $f(x)=x$ 或者 $f(x)=-x$.

评注 这是一个相对比较简单的函数方程, 方法相对比较常规. 证法是一个常规做法, 第一步得到 $f(0)=0$, 第二步得到 $f(x)= \pm x$, 最后解出原方程的解.证法二则相对巧妙, 直接通过代换解出 $f(x)=c x$, 过程相对比较短, 但却并不容易想到其中的代换.

2. 给定 $n \in \mathbb{N}^{*}$. 将 $\{1,2, \cdots, 2 n\}$ 划分为两个 $n$ 元子集 $A, B$. 若存在常数 $c_{n}$, 使得我们无论怎么划分, 一定存在 $A$ 中元素的排列 $a_{1} \sim a_{n}$ 和 $B$ 中元素的排列 $b_{1} \sim b_{n}$, 使得

$$
\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2} \geq c_{n}
$$

求 $c_{n}$ 的最大值.

解 记

$$
C_{n}=\left\{\begin{array}{ll}
\frac{13}{12} n^{3}-\frac{1}{3} n, & n \text { 是偶数 } \\
\frac{13}{12} n^{3}-\frac{1}{12} n, \quad n \text { 是奇数 }
\end{array} .\right.
$$

对 $\{1,2, \cdots, 2 n\}$ 的任意一个划分 $(A, B)$, 设 $A$ 中元素满足

$$
a_{1}<a_{2}<\cdots<a_{s} \leq n<a_{s+1}<\cdots<a_{n}
$$

$B$ 中元素满足

$$
b_{1}>b_{2}>\cdots>b_{s}>n \geq b_{s+1}>\cdots>b_{n}
$$

下证:

$$
\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2} \geq C_{n}
$$

对 $1 \leq i \leq n$, 记 $x_{i}=\left|a_{i}-b_{i}\right|$. 注意到

$$
\begin{gathered}
x_{1} \geq x_{2}+2 \geq \cdots \geq x_{s}+2(s-1), \\
x_{n} \geq x_{n-1}+2 \geq \cdots \geq x_{s+1}+2(n-s-1) .
\end{gathered}
$$

所以由拉格朗日恒等式,

$$
\begin{aligned}
\sum_{i=1}^{s} x_{i}^{2} & =\frac{1}{s}\left(\sum_{i=1}^{s} x_{i}\right)^{2}+\frac{1}{s} \sum_{1 \leq i<j \leq s}\left(x_{i}-x_{j}\right)^{2} \\
& \geq \frac{1}{s}\left(\sum_{i=1}^{s} x_{i}\right)^{2}+\frac{4}{s} \sum_{1 \leq i<j \leq s}(i-j)^{2} \\
& =\frac{1}{s}\left(\sum_{i=1}^{s} x_{i}\right)^{2}+\frac{s^{3}-s}{3} .
\end{aligned}
$$

同理,

$$
\sum_{i=s+1}^{n} x_{i}^{2} \geq \frac{1}{n-s}\left(\sum_{i=s+1}^{n} x_{i}\right)^{2}+\frac{(n-s)^{3}-(n-s)}{3} .
$$

相加得,

$$
\sum_{i=1}^{n} x_{i}^{2} \geq \frac{1}{s}\left(\sum_{i=1}^{s} x_{i}\right)^{2}+\frac{1}{n-s}\left(\sum_{i=s+1}^{n} x_{i}\right)^{2}+\frac{s^{3}+(n-s)^{3}-n}{3}
$$

又注意到

$$
\begin{aligned}
\sum_{i=1}^{n} x_{i} & =\left(b_{1}-a_{1}\right)+\cdots+\left(b_{s}-a_{s}\right)+\left(a_{s+1}-b_{s+1}\right)+\cdots+\left(a_{n}-b_{n}\right) \\
& =[(n+1)+(n+2)+\cdots+2 n]-(1+2+\cdots+n)=n^{2},
\end{aligned}
$$

所以由柯西不等式,

$$
\frac{1}{s}\left(\sum_{i=1}^{s} x_{i}\right)^{2}+\frac{1}{n-s}\left(\sum_{i=s+1}^{n} x_{i}\right)^{2} \geq \frac{\left(\sum_{i=1}^{s} x_{i}+\sum_{i=s+1}^{n} x_{i}\right)^{2}}{s+(n-s)}=n^{3} .
$$

最后由 $y=x^{3}$ 在 $(0,+\infty)$ 上是下凸的知,

$$
s^{3}+(n-s)^{3} \geq\left[\frac{n}{2}\right]^{3}+\left(n-\left[\frac{n}{2}\right]\right)^{3}
$$

这样,

$$
\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2}=\sum_{i=1}^{n} x_{i}^{2} \geq n^{3}+\frac{\left[\frac{n}{2}\right]^{3}+\left(n-\left[\frac{n}{2}\right]\right)^{3}-n}{3}=C_{n}
$$

当取

$$
A=\left\{1,2, \cdots,\left[\frac{n}{2}\right], n+\left[\frac{n}{2}\right]+1, \cdots, 2 n\right\}
$$

$$
B=\left\{\left[\frac{n}{2}\right]+1,\left[\frac{n}{2}\right]+2, \cdots,\left[\frac{n}{2}\right]+n\right\}
$$

时, 因为

$$
\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2}=\sum_{i=1}^{n}\left(a_{i}^{2}+b_{i}^{2}\right)-2 \sum_{i=1}^{n} a_{i} b_{i}=\sum_{i=1}^{2 n} i^{2}-2 \sum_{i=1}^{n} a_{i} b_{i}
$$

所以由排序不等式知, 当 $a_{1}<a_{2}<\cdots<a_{n}, b_{1}>b_{2}>\cdots>b_{n}$ 时, $\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2}$最大, 经计算等于 $C_{n}$.

综上, 所求最大值为 $C_{n}$.

评注 由排序不等式, 注意到在 $A$ 中元素从小到大排列, $B$ 中元素从大到小排列时, $\sum_{i=1}^{n}\left(a_{i}-b_{i}\right)^{2}$ 取得最大值. 这个做法的关键在于设出 $\left|a_{i}-b_{i}\right|$, 之后利用 “ $x_{1} \geq x_{2}+2 \geq \cdots \geq x_{s}+2(s-1)$ ”等式子进行放缩. 在做这种类型的题目时,在放缩的过程中要根据取等条件来放缩. 同时, $\sum_{i=1}^{n}\left|a_{i}-b_{i}\right|=n^{2}$ 也是一个经典的结论.

3. 求函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对 $\forall x, y \in \mathbb{R}$, 均有

$$
f(x+y f(x))+f(x y)=f(x)+f(2019 y) .
$$

解 记原方程为 $P(x, y)$. 由 $P(2019, y)$ 知 $f(2019+y f(2019))=f(2019)$.

若 $f(2019) \neq 0$, 让 $y$ 取遍 $\mathbb{R}$, 知 $f$ 是常值函数, 检验知合题.

下考虑 $f(2019)=0$.

(1) 若 $\exists x_{0} \neq 2019$, 使 $f\left(x_{0}\right)=0$. 考虑 $P(x, 1)$, 知

$$
f(x+f(x))=0 .
$$

考虑 $P\left(x_{0}, y\right)$, 知

$$
f\left(x_{0} y\right)=f(2019 y)
$$

记 $c=\frac{x_{0}}{2019}$, 则

$$
P(y)=P(c y), \quad \forall y \text { 成立. }
$$

考虑 $P(x, y)$ 和 $P(c x, y)$ 知

$$
f(c x+y f(x))=f(x+y f(x))
$$

(1)若 $\forall x \neq 0, f(x)=0$. 经检验合题.

(2) 若 $\exists x \neq 0, f(x) \neq 0$, 取 $f(x) \neq 0$. 让 $y$ 取遍 $\mathbb{R}$, 则 $z=x+y f(x)$ 也可取
遍 $\mathbb{R}$. 此时, 有

$$
f((c-1) x+z)=f(z), \quad \forall z \in \mathbb{R} \text { 成立. }
$$

因此 $f(x)=f(x+T)$ 是周期函数.

考虑 $P(x+T, y)$ 和 $P(x, y)$, 作差知

$$
f(x y)=f(x y+y T), \quad \forall x, y \in \mathbb{R} \text { 成立. }
$$

因此 $f$ 是常值函数. 经检验合题.

(2) 若 $\forall x_{0} \neq 2019, f\left(x_{0}\right) \neq 0$.

由 $P(x, 1)$ 知 $f(x+f(x))=0$. 因此 $f(x)=2019-x$. 经检验合题.

综上所述, 原方程的解为:

(1) $f(x)=c$.

(2) $f(x)=2019-x$.

(3) $f(x)= \begin{cases}0, & x \neq 0 . \\ c, & x=0(c \neq 0) .\end{cases}$

评注 这是 2019 年罗马尼亚大师赛的第五题. 这是一个比较困难的问题, 虽然有一些不同的做法, 但思路都大致相同, 其中较重要的结论(包括 $f(2019)=0$和周期性的证明) 也都需要. 同时, 这道题也很容易产生漏解.

