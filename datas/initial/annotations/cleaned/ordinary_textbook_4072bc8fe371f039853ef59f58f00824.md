# 数学新星问题征解第八期解答 

2015.09

第一题: 设正整数 $n>1$, 记 $A_{n}=\left\{k \in \mathbf{N}^{*} \mid(k, n)=1, k<n\right\}$. 问是否存在满射 $f: A_{n} \times A_{n} \rightarrow A_{n}$ 使得对任意 $a, b, c \in A_{n}$, 只要 $c \equiv a b(\bmod n)$ 就有

$$
\begin{aligned}
& f(a, k) \cdot f(b, k) \equiv f(c, k)(\bmod n), \\
& f(k, a) \cdot f(k, b) \equiv f(k, c)(\bmod n),
\end{aligned}
$$

对任意的 $k \in A_{n}$ 成立.

(湖北武钢三中学生 陈泽坤 供题)

## 解 (根据河北唐山一中兰添同学的解答整理):

首先我们证明: 对任意 $n=p^{\alpha}$ ( $\alpha \geq 1, p$ 为素数), 存在满足题意的映射 $f$.

设自然数数列 $g(k)$, 令 $f(a, k) \equiv a^{g(k)}(\bmod n)$, 则

$$
f(a, k) \cdot f(b, k) \equiv f(c, k)(\bmod n)
$$

成立. 故只需使其满足

$$
f(k, a) \cdot f(k, b) \equiv f(k, c)(\bmod n),
$$

即

$$
g(a)+g(b) \equiv g(c)(\bmod \varphi(n)),
$$

其中 $\varphi(n)$ 是 $n$ 的欧拉函数.

由于 $n=p^{\alpha}$, 则取 $n$ 的原根 $t \in\{1,2, \cdots, n-1\}$. 令 $a \equiv t^{g(a)}(\bmod n)$, 则

$$
t^{g(c)} \equiv c \equiv a b \equiv t^{g(a)+g(b)}(\bmod n),
$$

因此

$$
g(a)+g(b) \equiv g(c)(\bmod \varphi(n)),
$$

满足题意.

对任意 $a \neq b, t^{g(a)} \neq t^{g(b)}(\bmod n)$, 且 $\left(t^{g(a)}, n\right)=1$, 故每个 $a \in A_{n}$ 均可取到,且 $g(t)=1$. 所以 $f(a, t)=a$. 因此对任意的 $a \in A_{n}, f$ 均可取到, 即 $f$ 是满射.

最后, 我们证明: 对任意的 $(a, b)=1, a, b \in \mathbf{N}^{*}$, 若 $n=a, b$ 时, 存在满足题意的 $f$, 则 $n=a b$ 时, 也存在映射 $f$.
设 $n=a$ 时, $(m, k)$ 位置上的数为 $f_{1}(m, k) ; n=b$ 时, $(n, k)$ 位置上的数为 $f_{2}(n, k)$. 则当 $a \equiv a_{1}, b \equiv b_{1}(\bmod a)$ 时,

$$
f(a, b) \equiv f_{1}\left(a_{1}, b_{1}\right)(\bmod a)
$$

当 $a \equiv a_{2}, b \equiv b_{2}(\bmod b)$ 时,

$$
f(a, b) \equiv f_{2}\left(a_{2}, b_{2}\right)(\bmod b)
$$

因为 $(a, b)=1$, 则由中国剩余定理, 存在唯一正整数 $f(a, b) \in\{1,2, \cdots, n-1\}$ 满足条件, 且 $(f(a, b), a b)=1$.

下面只需证明, $f(a, b)$ 是满射.

对任意的 $x \equiv a_{0}(\bmod a), x \equiv b_{0}(\bmod b)$, 由 $f_{1}(a, b)$ 是满射, 存在 $x \equiv x_{1}, y \equiv$ $y_{1}(\bmod a), x \equiv x_{2}, y \equiv y_{2}(\bmod b)$, 使得 $f(x, y) \equiv f_{1}(x, y) \equiv a_{0}(\bmod a), f(x, y) \equiv$ $f_{2}(x, y) \equiv b_{0}(\bmod b)$ 恒成立.

故而对任意 $n \in \mathbf{N}^{*}$, 存在满足条件的映射 $f$.

第二题: 设 $n(n \geq 2)$ 是正整数. 用 $1 \times 2$ 的方格覆盖 $n \times n$ 方格表, 要求任意两个 $1 \times 2$ 方格不重叠. 设放了 $k$ 个 $1 \times 2$ 方格后，无法再放入一个这样的方格. 证明: $k \geq\left\lfloor\frac{n^{2}}{3}\right\rfloor$. 进一步, 当 $n=3 m\left(m \in \mathbf{N}^{*}\right)$ 时, 求 $k$ 的最小值.

(辽宁省实验中学初三学生 毕梦达 供题)

## 证明 (根据海南中学林道哲同学的解答整理):

当 $n=2$ 时, $k=2>1=\left\lfloor\frac{4}{3}\right\rfloor$ 成立.

当 $n \geq 3$ 时, 将每个 $1 \times 2$ 的方格内部染成黑色, 边染成红色, 并将 $n \times n$ 方框的外边也染成红色, 则由题设, 每一个未染色的空格子, 其 4 条边均为红色, 否则有一个空格子与其相邻, 矛盾! 对于每个 $1 \times 2$ 方格, 其 6 条长度为 1 的边至多为空格子贡献 4 条红边, 否则其有一条长度为 2 的边均为空格子贡献红边, 从而导致有两个空格子相邻, 矛盾! 下面考虑在 $n \times n$ 方框最外围一圈的格子. 对于 $n \times n$方框的一条边上的格子, 由于不存在两个连续的空格子, 则两个空格子之间必至少存在一个黑格. 无论该黑格所属的 $1 \times 2$ 方格中长为 2 的边是平行于或是垂直于该边, 该黑格所属的 $1 \times 2$ 方格都至多贡献 3 条红边. 与该黑格相邻的空格的其中一条红边由 $n \times n$ 的边框提供, 我们将其计入该黑格所属的 $1 \times 2$ 方格所提供的红边中, 从而该黑格所属的 $1 \times 2$ 方格也至多贡献 4 条边. 此外, $n \times n$ 方框的每一条边
至多再贡献一条红边.

记空格子个数为 $l$, 则根据前面的讨论可得, 空格子的边数不超过 $1 \times 2$ 方格与 $n \times n$ 方框的边所提供的红边数, 即 $4 l \leq 4 k+4$. 又 $l+2 k=n^{2}$, 于是

$$
k \geq\left\lceil\frac{n^{2}-1}{3}\right\rceil=\left\lfloor\frac{n^{2}}{3}\right\rfloor .
$$

当 $n=3 m$ 时, 我们证明 $k=3 m^{2}$ 取到最小值. 容易构造奇数行类似 “黑格,空格, 黑格, 空格, ”. 排列, 偶数行类似 “空格, 黑格, 空格, 黑格, ”. 排列, 显然这种构造不能再加入 $1 \times 2$ 方格. 在这种构造下, 每 $3 \times 3$ 方框内有 3 个 $1 \times 2$ 方格和 3 个空格. 故 $k=\frac{n^{2}}{3}=3 m^{2}$ 成立.

评注: 河北唐山一中兰添同学也给出了本题的正确解答.

第三题: 设 $I$ 为 $\triangle A B C$ 的内心, $D, E, F$ 为内切圆在三边上的切点, $E F$交 $\triangle A B C$ 的外接圆于点 $X, Y$ ( $X$ 在 $\overparen{A B}$ 内.) 证明:

$$
\angle I X D-\frac{1}{2} \angle B=\angle I Y D-\frac{1}{2} \angle C
$$

(湖南省雅礼中学学生 谢昌志 供题)

## 证明 (根据浙江省象山县第三中学黄子宸同学的解答整理):

如图, 作以 $\odot I$ 为反演基圆的反演变换, 则 $A, B, C$ 的反演点为 $E F, D F, D E$的中点, 即 $\triangle A B C$ 外接圆的反演图形为 $\triangle D E F$ 的九点圆. 设该九点圆交 $I X, I Y$于 $X^{\prime}, Y^{\prime}$, 则 $\angle I X D=\angle I D X^{\prime}, \angle I Y D=$ $\angle I D Y^{\prime}$,而 $\angle C B I=\angle I D F, \angle B C I=\angle I D E$,因此 $\angle C B I-\angle I X D=\angle I D F-\angle I D X^{\prime}=$ $\angle F D X^{\prime}$. 同理, $\angle B C I-\angle I Y D=\angle E D Y^{\prime}$.


于是问题转化为证明: $\angle F D X^{\prime}=\angle E D Y^{\prime}$.

此时, 以 $D$ 为反演中心, $\frac{1}{2} D E \cdot D F$ 为反演幕作反演变换, 再以 $\angle E D F$ 的角平分线为对称轴作轴反射. 则易知在上述合变换下有 $K \rightarrow E, L \rightarrow F$.

取 $\triangle D E F$ 的垂心 $H$, 连接 $D H$ 交 $\odot(J K L)$ 于 $M$, 延长 $D I$ 交 $\odot(A E F)$于 $N$.

下面证明 $M \rightarrow N$. 由 $H, I$ 的等角共轭性可知 $D M, D N$ 关于 $\angle E D F$ 的角
平分线对称. 同样由等角共轭性可知, $\angle H D F=\angle I D E=\angle N D E, \angle H F D=$ $\angle I F E=\angle I N E=\angle D N E$, 故 $\triangle D H F \sim \triangle D E N$. 因此 $\frac{D F}{D N}=\frac{D H}{D E}$. 于是 $D M$. $D N=\frac{1}{2} D H \cdot D N=\frac{1}{2} D E \cdot D F$. 所以有 $K \rightarrow E, L \rightarrow F, M \rightarrow N$. 故 $\odot(K L M) \rightarrow$ $\odot(E F N)$, 即 $\odot(J K L) \rightarrow \odot(I E F)$. 同理 $\odot(I E F) \rightarrow \odot(J K L)$. 它们有两个交点 $X^{\prime}, Y^{\prime}$, 显然该变换下它们不会变为自身. 因此 $X^{\prime}$ 在该变换下变为 $Y^{\prime}$, 即 $X^{\prime} Y^{\prime}$关于 $\angle E D F$ 的角平分线对称, 即 $\angle F D X^{\prime}=\angle E D Y^{\prime}$.

第四题: 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是 $n(n \geq 3)$ 个正实数, 使得 $\sum_{i=1}^{n} x_{i}=n$. 证明:若 $k>t>1$, 则

$$
\frac{\sum_{i=1}^{n} x_{i}^{k}-n}{k-1} \geq \frac{\sum_{i=1}^{n} x_{i}^{t}-n}{t-1}
$$

(上海中学学生 李嘉昊 供题)

## 解法一 (根据长沙一中胡冬础同学的解答整理):

设 $k=t+m, m>0$, 则原不等式等价于

我们证明局部不等式:

$$
(t-1) \sum_{i=1}^{n} x_{i}^{k}+m \sum_{i=1}^{n} x_{i} \geq(t+m-1) \sum_{i=1}^{n} x_{i}^{t}
$$

$$
(t-1) x_{i}^{k}+m x_{i} \geq(t+m-1) x_{i}^{t}(i=1,2, \cdots, n)
$$

即证

$$
\frac{t-1}{t+m-1} x_{i}^{t+m}+\frac{m}{t+m-1} x_{i} \geq x_{i}^{t}
$$

事实上, 利用加权的平均值不等式:

$$
a x+b y \geq x^{a} y^{b} \quad(a+b=1, \quad a, b \geq 0, x, y>0)
$$

得到

$$
\frac{t-1}{t+m-1} x_{i}^{t+m}+\frac{m}{t+m-1} x_{i} \geq\left(x_{i}^{t+m}\right)^{\frac{t-1}{t+m-1}} x_{i}^{\frac{m}{t+m-1}}=\left(x_{i}\right)^{\frac{(t+m)(t-1)+m}{t+m-1}}=x_{i}^{t}
$$

即 (1) 式成立. 再对 (1) 式两边关于 $i=1,2, \cdots, n$ 求和, 即得所证结论.

## 解法二 (根据河北唐山一中兰添同学的解答整理):

由已知条件, 所证不等式等价于

$$
\frac{\sum_{i=1}^{n}\left(x_{i}^{k}-x_{i}\right)}{k-1} \geq \frac{\sum_{i=1}^{n}\left(x_{i}^{t}-x_{i}\right)}{t-1}
$$

我们证明局部不等式:

$$
\frac{x_{i}^{k}-x_{i}}{k-1} \geq \frac{x_{i}^{t}-x_{i}}{t-1}
$$

由于 $x_{i}>0$, 上式等价于

$$
\frac{x_{i}^{k-1}}{k-1} \geq \frac{x_{i}^{t-1}}{t-1}
$$

事实上, 令 $f(x)=\frac{x^{k-1}}{k-1}-\frac{x^{t-1}}{t-1}$, 则

$$
f^{\prime}(x)=x^{k-2}-x^{t-2}=x^{t-2}\left(x^{k-t}-1\right),
$$

由 $k>t>1, x>0$ 可得当 $x \geq 1$ 时, $f^{\prime}(x) \geq 0$, 当 $0<x \leq 1$ 时, $f^{\prime}(x) \leq 0$. 故

$$
f(x) \geq f(1)=0, \quad x>0 .
$$

即 (4) 式成立. 对 (3) 式两边对 $i=1,2, \cdots, n$ 求和, 即得所证结论.

## 解法三 (根据海南中学林道哲同学的解答整理):

由已知条件,所证不等式等价于

$$
\frac{\sum_{i=1}^{n} x_{i}^{k}}{k-1}-\frac{\sum_{i=1}^{n} x_{i}^{t}}{t-1} \geq n\left(\frac{1}{k-1}-\frac{1}{t-1}\right)
$$

先证明如下引理:

引理 已知 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数, $\sum_{i=1}^{n} a_{i} \geq n, r>1$, 则 $\sum_{i=1}^{n} a_{i}^{r} \geq \sum_{i=1}^{n} a_{i}$.

事实上, 由幕平均值单调性定理和引理已知条件, 有

$$
\frac{\sum_{i=1}^{n} a_{i}^{r}}{n} \geq\left(\frac{\sum_{i=1}^{n} a_{i}}{n}\right)^{r} \geq \frac{\sum_{i=1}^{n} a_{i}}{n}
$$

从而引理得证.

回到原题, 由 $t>1, \sum_{i=1}^{n} x_{i}=n$, 根据引理有

$$
\sum_{i=1}^{n} x_{i}^{t} \geq \sum_{i=1}^{n} x_{i}=n
$$

又 $k<t$, 设 $k=\mu t, \mu>1$, 则由 (6) 式,

$$
\sum_{i=1}^{n} x_{i}^{k}=\sum_{i=1}^{n} x_{i}^{\mu t} \geq \sum_{i=1}^{n} x_{i}^{t}
$$

因此

$$
\frac{\sum_{i=1}^{n} x_{i}^{k}}{k-1}-\frac{\sum_{i=1}^{n} x_{i}^{t}}{t-1} \geq \sum_{i=1}^{n} x_{i}^{t}\left(\frac{1}{k-1}-\frac{1}{t-1}\right) \geq n\left(\frac{1}{k-1}-\frac{1}{t-1}\right)
$$

即 (5) 式得证, 从而所证不等式成立.

评注 湖南省长沙市第一中学廖展锋同学也给出了本题的正确解答.

