$$
\text { 数学新星网 * 学生专栏 }
$$

www.nsmath.cn/xszl

# 浅谈数论型函数方程 

周世龙

(北京市第四中学，100034)

在数论问题中, 有一类较为特殊: 它会以函数方程的形式呈现. 此类问题通常难度较大, 既要求对数论知识掌握透彻, 同时也需要使用函数方程的处理手段. 不过在笔者看来, 此类问题较常见的离散型函数方程 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$ 的求解更有价值, 更能体现离散化的本质, 有相当一部分问题既具备极高的观赏性, 又有很大的研究价值.

本文中例题有较为详细的思路分析, 练习题则以答案为主. 望各位读者通过此文, 能感受到这类问题的美.

例 1. 求所有函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 使得对于所有的 $m, n \in \mathbb{N}^{*}$, 均有

(1) $f(m n)=f(m) f(n)$; (2) $m+n \mid f(m)+f(n)$.

分析与解 我们先来尝试猜出本题的答案.

代入 $m, n=1$, 有 $f(1)=f^{2}(1)$, 结合 $f(n) \in \mathbb{N}^{*}$ 得 $f(1)=1$.

代入 $n=1$, 有 $m+1 \mid f(m)+1$, 于是猜测 $f(m)=m^{k}, k$ 为奇数.

下面来证明我们的猜想是正确的.

由 $2 n+1 \mid f(2 n)+f(1)=f(2) f(n)+1$ 得 $(2 n+1, f(2) f(n))=1$, 有 $(2 n+1, f(2))=1, \forall n \in \mathbb{N}^{*}$, 这说明 $f(2)=2^{k}$.

由 $1+2 \mid f(1)+f(2)=f(2)+1$, 得到 $k$ 为奇数.

对任意 $m \in \mathbb{N}^{*}, f\left(2^{m}\right)=f^{m}(2)=2^{k m}$. 结合 $k$ 为奇数, 有 $2^{m}+n \mid 2^{m k}+n^{k}$, $\forall n \in \mathbb{N}^{*}$. 再由条件 $(2)$ 知 $2^{m}+n \mid f\left(2^{m}\right)+f(n)=2^{k m}+f(n)$, 从而 $2^{m}+n \mid$ $f(n)-n^{k}$.

由于 $m$ 的任意性, 必有 $f(n)-n^{k}=0$, 即 $f(n)=n^{k}\left(n \in \mathbb{N}^{*}\right)$.

反之, 通过验证, 易知其满足题目要求.

所以 $f(n)=n^{k}\left(n \in \mathbb{N}^{*}\right), k$ 为正奇数, 即为我们所求的 $f$.[^0]评注 本题不难, 是一道相当常规的题目. 可以说没有过多的技巧. 最好先猜出本题答案, 后往答案上靠拢, 上面解答中关于 $f(2)$ 的解法便是如此. 这也是处理这类问题的重要方式之一.

例 2. 求所有函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 使得对于任意正整数 $m, n, f(m)+f(n)-m n$不为 0, 且整除 $m f(m)+n f(n) .{ }^{[1]}$

分析与解 还是先尝试猜出答案. 注意到当 $f(n)=n^{2}$ 时, $m^{2}-m n+n^{2}$ 的确不为 0, 且整除 $m^{3}+n^{3}$. 除此之外似乎并不能试出其他答案.

来验证一下. 取 $m=n=1$, 有 $2 f(1)-1 \mid 2 f(1)$, 从而 $f(1)=1$.

对任意奇素数 $p$, 取另一个数为 1 , 得到 $f(p)+f(1)-p \mid p f(p)+1$. 于是

$$
f(p)+1-p \mid p f(p)+1-p(f(p)+1-p)=p^{2}+1-p
$$

若 $f(p)=p^{2}$, 明显成立; 下面考虑 $f(p)<p^{2}$ 的情况.

由于 $p^{2}+1-p$ 为奇数, 显然有 $p^{2}+1-p \geq 3(f(p)+1-p)$, 从而

$$
f(p) \leq \frac{1}{3}\left(p^{2}+2 p-2\right) .
$$

再代入 $m=n=p$, 有 $2 f(p)-p^{2} \mid 2 p f(p)$, 稍加变形得

$$
2 f(p)-p^{2} \mid p^{3} \text {. }
$$

然后进行一下估计, 得到

$$
-p^{2}<2 f(p)-p^{2} \leq \frac{2}{3}\left(p^{2}+2 p-2\right)-p^{2}<-p .
$$

上式最右端的小于号在 $p>6$ 时成立. 于是对不小于 7 的素数 $p$, 由式 (1) (2), 矛盾!

故 $f(p)=p^{2}$. 对任意正整数 $n$, 取 $m=p$ 代入, 有 $p^{2}-p n+f(n) \mid p^{3}+n f(n)$,由此

$$
p^{2}-p n+f(n) \mid p^{3}+n f(n)-n\left(p^{2}-p n+f(n)\right)=p^{3}-n p^{2}+n^{2} p .
$$

取充分大的 $p(p \gg f(n))$, 此时有 $(p, f(n))=1$, 故 $p^{2}-p n+f(n) \mid p^{2}-p n+n^{2}$.稍加变形, 得到 $p^{2}-p n+f(n) \mid n^{2}-f(n)$. 由 $p$ 的性质, 必有 $n^{2}-f(n)=0$.

至此得到 $f(n)=n$, 证毕.

评注 对于这类问题, 有时在我们猜出答案后可能会尝试归纳 (见下一题).不过, 事实上, 大部分时候直接对整数情况进行归纳是行不通的, 主要是因为任意整数的情形过于复杂, 一般不是一步归纳就能轻易解决的. 此时我们不妨对特殊情况 (较常见的是奇素数时的命题) 进行讨论, 而此题提醒我们的是不要忘记不等式分析. 总体而言这是个很好的训练题.
例 3. 给定正整数 $k$ 和 $l$. 求所有函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 使得对任意 $m, n \in \mathbb{N}^{*}$,均有 $f(m)+f(n) \mid(m+n+l)^{k}$ 成立.

分析与解 首先, 当 $l$ 为奇数时, 取 $m=n$, 有 $2 f(m) \mid(2 m+l)^{k}$, 显然矛盾!故 $l$ 为奇数时不存在 $f$ 满足题意. 下面讨论 $l$ 为偶数的情况.

依然猜测 $f(n)=n+\frac{l}{2}$. 为往这个答案靠拢, 我们来证明如下引理:

引理 对任意 $m \in \mathbb{N}^{*}$, 有 $f(m+1)-f(m)= \pm 1$.

显然 $f$ 不为常值函数. 若 $|f(m+1)-f(m)| \neq 1$, 则存在素数 $p$, 使得 $p \mid f(m+1)-f(m)$.

取 $e$ 使得 $p^{e}>m+l$. 结合条件, 有

$$
f\left(p^{e}-m-l\right)+f(m) \mid\left(p^{e}-m-l+m+l\right)^{k}=p^{e k} .
$$

又 $f\left(p^{e}-m-l\right)+f(m) \geq 1+1=2$, 故 $p \mid f\left(p^{e}-m-1\right)+f(m)$.

再由假设可推得

$$
p \mid f\left(p^{e}-m-1\right)+f(m+1) .
$$

然而 $f\left(p^{e}-m-1\right)+f(m+1) \mid\left(p^{e}+1\right)^{k}$, 显然矛盾! 故引理证毕.

特别地, 由引理易得 $f(n) \leq f(n-1)+1 \leq \cdots \leq f(1)+(n-1)$.

接下来选取充分大的素数 $p, p>l+1, p^{2}>p+2 f(1)-l-2$. 注意到

$$
f(1)+f(p-l-1) \mid(p-l-1+l+1)^{k}=p^{k},
$$

且

$$
1<f(1)+f(p-l-1) \leq f(1)+(f(1)+p-l-2)<p^{2} .
$$

故 $f(1)+f(p-l-1)=p$, 即 $f(p-l-1)=p-f(1)$.

然后, 再取另一满足上式的素数 $q, p>q$. 则 $f(p-l-1)=p-f(1)$, 且 $f(q-l-1)=q-f(1)$. 因此

$$
\begin{aligned}
p-f(1) & =f(p-l-1) \leq f(p-l-2)+1 \leq \cdots \\
& \leq f(q-l+1)+(p-q)=q-f(1)+(p-q)=p-f(1)
\end{aligned}
$$

不等式中的等号均成立, 这说明当 $q \leq n \leq p$ 时, 有 $f(n-l-1)=n-f(1)$. 特别地, 对 $n \geq q-l-1$, 有 $f(n)=n+l+1-f(1)=n+c$, 其中 $c$ 为常数.

我们接下来固定 $n$, 选取 $q-l-1 \leq N \leq p-l-1$ 使得 $n+N+l$ 为素数.事实上, 由于 $p$ 充分大, 这是可以做到的. 于是由 $f(n)+f(N) \mid(n+N+l)^{k}$ 可得 $f(n)+f(N)=(n+N+l)^{e}$, 其中 $1 \leq e \leq k$.

又 $f(N)=N+c$, 当 $N$ 趋于无穷时, 除非 $e=1$, 否则必然矛盾. 这时
$f(n)=n+l-c, \forall n \in \mathbb{N}^{*}$.

这时代入题目条件, 有 $m+n+2 l-2 c \mid(m+n+l)^{k}$. 则显然有

$$
m+n+2 l-2 c \mid(m+n+l-(m+n+2 l-2 c))^{k}=(2 c-l)^{k} .
$$

取 $m, n \rightarrow+\infty$, 右式为常值, 故必然为 0 , 即 $c=\frac{l}{2}$. 所以当 $l$ 为偶数时, $f(n)=n+\frac{l}{2}, \forall n \in \mathbb{N}^{*}$; 当 $l$ 为奇数时, 无满足题意的 $f$.

评注 本题在例 1 与例 2 的基础上变得更加不常规, 也更难处理了些. 大致想法仍然是往答案靠拢, 但此题进行下去时明显可以感受到阻碍, 整个过程也显得并不那么自然.

注意引理中的字母与后续证明中的相互独立, 未加区分, 请读者注意.

例 4. 对于每个 $n \in \mathbb{N}^{*}$, 记 $n$ 的所有正因子的数目为 $d(n)$. 求满足下列性质的所有函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$ :

(1) 对于所有的 $x \in \mathbb{N}^{*}, d(f(x))=x$;

(2) 对于所有的 $x, y \in \mathbb{N}^{*}$, 有 $f(x y) \mid(x-1) y^{x y-1} f(x)$.

分析与解 乍看此题, 感觉第一个条件较好下手, 于是来尝试一些较为简单的情况.

由 $d(f(1))=1$ 得 $f(1)=1$; 由 $d(f(2))=2$ 得 $f(2)=p, p$ 为素数; 由 $d(f(3))=3$ 知 $f(3)=q^{2}, q$ 为素数.

鉴于已设出 $f(2), f(3)$, 我们来考虑 $f(6)$.

由条件 (2) 可知, $f(6)=f(2 \cdot 3) \mid 3^{6-1} f(2)=3^{5} p$, 同时 $f(6)=f(3 \cdot 2) \mid$ $2 \cdot 2^{6-1} f(3)=2^{6} q^{2}$. 于是 $f(6) \mid\left(3^{5} p, 2^{6} q^{2}\right)$. 结合 $d(f(6))=6$, 易通过简单讨论知 $p=2, q=3, f(6)=3^{2} \cdot 2=18$.

经过上述讨论, 得到了 $f(2)=2=2^{2-1}, f(3)=3^{2}=3^{3-1}$.

于是我们猜测并证明如下引理:

引理 1. $f(p)=p^{p-1}, p$ 为素数.

由条件 (1) 知 $d(f(p))=p$, 结合 $p$ 为素数, 可知 $f(p)=q^{p-1}, q$ 为素数.

考虑 $f(2 p)=f(2 \cdot p)\left|p^{2 p-1} \cdot 2, f(2 p)=f(p \cdot 2)\right|(p-1) \cdot 2^{2 p-1} \cdot q^{p-1}$.

故 $f(2 p) \mid 2 \cdot\left(p^{2 p-1},(p-1) q^{p-1}\right)$, 易得 $\left(p^{2 q-1}, q^{p-1}\right) \neq 1$, 否则 $f(2 p) \mid 2$, 这显然是不成立的. 于是 $p=q$. 此时 $f(p)=p^{p-1}$, 引理 1 证毕.

继续进行尝试, 知 $f(4)=f(2 \cdot 2) \mid 2^{3} f(2)=2^{4}$, 结合 $d(f(4))=4$, 知 $f(4)=2^{3}$.

多进行几组尝试 (此处略去) 后, 可发现素数的幂也满足引理 1 的形式. 于
是我们证明:

引理 2. $f\left(p^{n}\right)=p^{p^{n}-1}, p$ 为素数.

对 $n$ 归纳.

$n=1$ 时, 即为引理 1.

假设命题对 $n-1$ 时成立, 考虑 $n$ 时的命题.

由条件 (2) 知

$$
f\left(p^{n}\right)=f\left(p \cdot p^{n-1}\right) \mid(p-1) \cdot\left(p^{n-1}\right)^{p^{n}-1} f(p)=(p-1) p^{(n-1)\left(p^{n}-1\right)+p-1}:=A,
$$

且

$$
f\left(p^{n}\right)=f\left(p^{n-1} \cdot p\right) \mid\left(p^{n-1}-1\right) p^{p^{n}-1} f\left(p^{n-1}\right)=\left(p^{n}-1\right) p^{p^{n}-1+p^{n-1}-1}:=B .
$$

又知 $\left(\left(p^{n}-1\right), p\right)=1, p-1 \mid p^{n}-1$, 于是 $f\left(p^{n}\right) \mid(A, B)=(p-1) p^{p^{n}+p^{n-1}-2}$.

由条件 (1) 知 $d\left(f\left(p^{n}\right)\right)=p^{n}$, 若 $p-1$ 中含有 $f\left(p^{n}\right)$ 的素因子, 则其次数必 $\geq p-1$. 显然 $2^{p-1}>p-1$, 矛盾! 于是得到 $f\left(p^{n}\right)$ 只含素因子 $p$, 结合 $d\left(f\left(p^{n}\right)\right)=p^{n}$, 有 $f\left(p^{n}\right)=p^{p^{n}-1}$, 于是引理 2 证毕.

至此已完成了对素数的幂情况的证明. 稍加尝试后, 便可猜到此函数的一般形式. 但前面的证明只运用了条件和整除分析, 然而在证明一般情况时, 由于素因子数量的增多, 无法确定各种 $(p-1)$ 型因子与其他因子的最大公约数. 若仍只是用这些手段, 无疑将是极为复杂甚至走不下去的 (读者可自行尝试).

但我们可从上述证明过程中得到启发: $f\left(p^{n}\right)$ 只含素因子 $p$. 这引发了我们对如下引理的证明:

引理 3. 对于任意的正整数 $n$, 它的素因子与 $f(n)$ 的素因子完全相同.

设 $p=\min _{p_{i} \mid n} p_{i}$, 其中 $p_{i}$ 为素数.

则由条件 (2), 我们设 $m=\frac{n}{p}$, 有

$$
f(n)=f(p \cdot m) \mid(p-1) m^{n-1} f(p)=(p-1) m^{n-1} p^{p-1} .
$$

分离 $f(n)$ 的因子, 设 $f(n)=k N$, 其中 $(k, n)=1, p_{i} \mid N$. 下面只需说明 $k=1$即可.

由于 $k \mid(p-1) m^{n-1} f(p)$, 从而 $k \mid p-1$, 且 $d(k) \leq k<p$.

由条件 $(1), n=d(f(n))=d(k N)$, 且 $(k, N)=1$, 知 $n=d(k N)=d(k) d(N)$, $d(k) \mid n$.

上面已经说明了 $d(k)<p$, 于是 $d(k)=1$, 即 $k=1$, 引理 3 证毕.

自然地, 也可仿照引理 2 的证明完成此题. 不过此处给一个稍简单的方法.

设 $n=\prod_{i=1}^{k} p_{i}^{\alpha_{i}}$, 则由引理 $3, f(n)=\prod_{i=1}^{k} p_{i}^{\beta_{i}}$. 结合条件 $(2)$, 设 $x_{i}=\frac{n}{p_{i}^{\alpha_{i}}}$, 我们
有 $p_{i}^{\beta_{i}}|f(n)|\left(p_{i}^{\alpha_{i}}-1\right) x_{i}^{n-1} f\left(p_{i}^{\alpha_{i}}\right)$.

由于 $\left(p_{i}\left(p_{i}^{\alpha_{i}}-1\right) x_{i}^{n-1}\right)=1$, 有 $p_{i}^{\beta_{i}} \mid f\left(p_{i}^{\alpha_{i}}\right)=p_{i}^{p_{i}^{\alpha_{i}}-1}$, 从而 $\beta_{i} \leq p_{i}^{\alpha_{i}}-1$. 结合条件 (1), 等号必须取到, 此处不再赘述.答.

至此得到了 $f: f(n)=\prod_{i=1}^{k} p_{i}^{p_{i}^{\alpha_{i}-1}}$, 当 $n=\prod_{i=1}^{k} p_{i}^{\alpha_{i}}$ 时. 我们完成了对本题的解

评注 此题可以说是一个非常经典的题目, 用到的手段着实不多: 整除的性质, 算术基本定理, 似乎也就仅此而已了. 但看似过程一气呵成, 此题仍具有一定的难度, 自己做下来也并非一帆风顺.

此题之所以典型, 在于其思想的重要性: 从特殊到一般. 这对于大部分难题是不可或缺的.

例 5. 对于不小于 5 的素数 $p$ 和正整数 $n$, 求所有函数 $f: \mathbb{Z}^{*} \rightarrow \mathbb{N}$, 满足:

(1) 对所有满足 $a_{i} \notin\{0,1\}(1 \leq i \leq p-2)$ 且 $p \nmid a_{i}-1$ 的整数序列, 有 $\sum_{i=1}^{p-2} f\left(a_{i}\right)=f\left(\prod_{i=1}^{p-2} a_{i}\right)$.

(2) 对任意的互质整数 $a, b$, 当 $a \equiv b(\bmod p)$ 时, $f(a)=f(b)$.

(3) 对任意正整数 $n$, 存在 $l \in \mathbb{Z}^{*}$, 使得 $f(l)=n$. ${ }^{[3]}$

分析与解 题目不允许我们取 $a_{i}=1$, 不妨取 $a_{i}=-1$, 这时 $(p-2) f(-1)=$ $f(-1)$, 则 $f(-1)=0$.

取 $a_{i}=i+1$, 据 Wilson 定理, 结合条件 $(2)$, 必有 $\sum_{i=2}^{p-1} f(i)=f\left(\prod_{i=2}^{p-1} i\right)=$ $f(-1)=0$. 由题意, 函数的值域为非负整数, 所以 $f(i)=0,2 \leq i \leq p-1$.

再取 $a_{1}=4$, 其余 $a_{i}=2$, 由 Fermat 小定理, $\sum_{i=1}^{p-2} f\left(a_{i}\right)=f\left(2^{p-1}\right)=f(1)=0$.

当 $(a, p)=1$ 时, $(a, a+k p)=1$. 结合条件 $(2)$, 得 $f(n)=0$, 当 $p \nmid n$ 时.

至此我们已将与 $p$ 互素的正整数讨论完全. 下面来说明 $p \mid n$ 时的情况.

取 $a_{1}=x, a_{2}=y($ 其中 $x y \equiv-1(\bmod p)), a_{3}=a_{4}=p$, 其余 $a_{i}=-1$, 可知 $2 f(p)=f\left(p^{2}\right)$, 经过简单的归纳, 可得 $f\left(p^{k}\right)=k f(p), \forall k \in \mathbb{N}$.

对任意与 $p$ 互素的整数 $r$, 若 $p \nmid r-1$, 取 $a_{1}=r, a_{2}=p^{k-1}, a_{3}=p$, 其余 $a_{i}=-1$, 有 $f\left(r p^{k}\right)=\sum_{i=1}^{p-2} a_{i}=k f(p)$. 若 $p \mid r-1$, 不妨设 $r=m p+1$, 我们不能直接代入 $r$, 但在证明了上述情况后, 可进行一些处理. 取 $a_{1}=(m p+1) p^{k}$, $a_{2}=(m p-1) p^{k}, a_{3}=x, a_{4}=y($ 仍有 $x y \equiv-1(\bmod p))$, 其余 $a_{i}=-1$, 则

$$
f\left((m p+1) p^{k}\right)=f\left(\left(m^{2} p^{2}-1\right) p^{2 k}\right)-f\left((m p-1) p^{k}\right)=k f(p) .
$$

整理一下, 我们有 $f(n)=\alpha \nu_{p}(n)$, 其中 $\alpha=f(p)$.

再结合条件 3, 知 $f(p) \mid f(l)=n$, 故最终得到 $f(n)=\alpha \nu_{p}(n)$, 其中 $\alpha$ 为 $n$
的因子.

评注 一道相当精彩的题目, 这几步赋值其实都相当关键且漂亮, 不失为一道好的习题. 原题目的题设是 “证明 $f$ 的个数与 $n$ 的因子个数相同”. 应该说命题者的目的在于给选手提示, 但在实际过程中这反而可能会让人想多 (笔者便是如此).

这题相对于以上几道还是 “数论的” . 其实对于这类问题, 何时该使用代数手段处理, 何时该利用数论知识构造或分析, 是难点, 同时也是魅力所在.

例 6. 求所有 $f: \mathbb{Q} \rightarrow \mathbb{Z}$, 使得对任意 $x \in \mathbb{Q}, a \in \mathbb{Z}, b \in \mathbb{Z}_{+}$, 有

$$
f\left(\frac{f(x)+a}{b}\right)=f\left(\frac{x+a}{b}\right) .
$$

分析与解 我们可先取 $a=0, b=1$, 得到 $f(f(x))=f(x)$, 这说明 $f$ 或为常函数, 或为在整数上的恒等映射, 结合原式比较容易猜到天花板和地板两种高斯函数. 故猜测 $f(x) \equiv c, c \in \mathbb{Z} ; f(x)=\lfloor x\rfloor ; f(x)=\lceil x\rceil$ (注意不要算上 $f(x)=x$,因为是 $\mathbb{Q} \rightarrow \mathbb{Z}$ ). 在以上三种中常函数较特殊, 故先来处理它, 为方便书写, 以引理的形式呈现.

引理 若存在 $n \in \mathbb{N}^{*}$, 使得 $f(n) \neq n$, 则必有 $f(n) \equiv c, c \in \mathbb{Z}$.

不妨设 $m=f(n) \neq n$, 代入 $x=n, a=k b-m(\forall k \in \mathbb{Z}), b=|m-n|$, 有 $f(k)=f(k \pm 1), \forall k \in \mathbb{Z}$. 不论加减, 必然会得到 $f(n) \equiv c, n \in \mathbb{Z}$.

上面提到了 $f(f(x))=f(x)$, 结合 $f(x) \in \mathbb{Z} \Rightarrow f(f(x))=c \Rightarrow f(x) \equiv c$, $x \in \mathbb{Q}, c \in \mathbb{Z}$.

至此引理证毕.

接下来讨论非常函数的情况. 据引理可知 $f(n)=n, \forall n \in \mathbb{Z}$. 我们还有一个简单的小结论: $f(x+a)=f(f(x)+a)=f(x)+a, x \in \mathbb{Q}, a \in \mathbb{Z}$. 这是易于证明的。

下面的证明分步给出.

(1) $f\left(\frac{1}{2}\right) \in\{0,1\}$.

讨论需先从特殊情况开始. 取 $x=\frac{1}{2}, b=2 a+1$, 有

$$
f\left(\frac{f\left(\frac{1}{2}\right)+a}{2 a+1}\right)=f\left(\frac{\frac{1}{2}+a}{2 a+1}\right)=f\left(\frac{1}{2}\right) .
$$

欲证 $f\left(\frac{1}{2}\right) \in\{0,1\}$, 我们进行一下分段:

i) 若 $f\left(\frac{1}{2}\right) \geq 1$, 取 $a=f\left(\frac{1}{2}\right)-1$, 会得到 $f\left(\frac{2 f\left(\frac{1}{2}\right)-1}{2 f\left(\frac{1}{2}\right)-1}\right)=f(1)=1=f\left(\frac{1}{2}\right)$;

ii) 若 $f\left(\frac{1}{2}\right) \leq 0$, 取 $a=-f\left(\frac{1}{2}\right)$, 得到 $f(0)=0=f\left(\frac{1}{2}\right)$ (为什么可以这样分段留给读者思考). 故 (1) 证毕.

(2) 当 $f\left(\frac{1}{2}\right)=0$ 时, $f(x)=\lfloor x\rfloor$.

结合上面的小结论, 其实只需证明: 对任意的 $0<k<n, f\left(\frac{k}{n}\right)=0$.

先来证明: $n=2^{k}$ 时命题成立.

对 $k$ 归纳. $k=1$ 已给出, 假设 $k-1$ 时成立, 讨论 $k$ 时的命题.

易知 $f\left(\frac{1}{2^{k}}\right)=f\left(\frac{\frac{l}{2^{k-1}}}{2}\right)=f\left(\frac{f\left(\frac{1}{2^{k-1}}\right)}{2}\right)$, 结合 $0<l<2^{k} \Rightarrow f\left(\frac{l}{2^{k-1}}\right)=0$ 或 1 . 而 $f(0)=f\left(\frac{1}{2}\right)=0$, 故 $k$ 时命题成立.

回到原题, 对 $n$ 归纳. $n=2$ 已给出. 假设 $n-1$ 时成立, 讨论 $n$ 时的命题.

$$
f\left(\frac{1}{n}\right)=f\left(\frac{f\left(\frac{1}{n-1}\right)+1}{n}\right)=f\left(\frac{\frac{1}{n-1}+1}{n}\right)=f\left(\frac{1}{n-1}\right)=0,
$$

直至 $f\left(\frac{n-2}{n}\right)$ 均类似操作即可.

注意到 $f\left(\frac{n-1}{n}\right)=f\left(-\frac{1}{n}+1\right)=f\left(\frac{f\left(\frac{1}{2 \varphi(n)}\right)-1}{n}+1\right)=f\left(\frac{\frac{1-2^{\varphi(n)}}{n}}{2^{\varphi(n)}}+1\right)$, 这里 $\varphi(n)$为 Euler 函数. 由于 $2^{\varphi(n)}>\frac{2^{\varphi(n)}-1}{n} \in \mathbb{Z}$, 由前面 $2^{k}$ 的结论不难得出 $f\left(\frac{n-1}{n}\right)=0$.于是 (2) 证毕.

(3) 当 $f\left(\frac{1}{2}\right)=1, f(x)=\lceil x\rceil$.

证明与 (2) 几乎完全相同, 读者可自行探究, 此处不再赘述.

故我们证明了上述猜想为真, 证毕.

评注 初看此题, 若不是官方标注它是数论题, 笔者可能会在代数的道路上一路走到黑. 官方的答案似乎讨论得有些麻烦, 上述解法可能稍方便些. 其实总体上来说我们的目的便是证明有且仅有那三个函数满足题意, 故总体而言, 在确定方向后, 思路还算清晰, 剩下的便是慢慢摸索完成证明了.

例 7. 已知函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$ 同时满足:

(1) 对任意正整数 $m, n$, 有 $(f(m), f(n)) \leq(m, n)^{2014}$.

(2) 对任意正整数 $n$, 有 $n \leq f(n) \leq n+2014$.

证明：存在正整数 $N$, 使得对每个整数 $n \geq N$, 均有 $f(n)=n$.

分析与解 考察 (1) 的特殊情况: 当 $(m, n)=1$ 时, $(f(m), f(n)) \leq(m, n)^{2014}=$ 1 , 得 $(f(m), f(n))=1$.

而 (2) 是一个限定 $f(n)$ 范围的条件. 故欲证在一定条件下 $f(n)=n$, 我们可考虑如下命题:

引理 对素数 $p$, 若 $p \mid f(n)$, 则 $p \mid n$.

由 (1) 知: 当 $(f(m), f(n))>1$ 时, 有 $(m, n)>1$.

假设存在 $p \mid m+l=f(m)$, 其中 $p \nmid m$. 我们取 $2015^{2}-1$ 个不同于 $p$ 且大于 2014 的互异素数 $p_{i, j}(i, j=0,1,2, \cdots, 2014)\left(p_{0,0}=1\right)$. 此时有 $\left(p_{i, j}, p m\right)=1$.
由中国剩余定理, 存在 $n_{0}$ 使得 $p \nmid n_{0}$, 且 $\prod_{k=0}^{2014} p_{i, k} \mid n_{0}+i, \forall 0 \leq i \leq 2014$.

再由中国剩余定理, 取 $n_{1}$ 使得 $p \mid n_{1},\left(n_{0}, n_{1}\right)=1,\left(n_{1}, m\right)=1$, 且 $\prod_{i=0}^{2014} p_{i, j} \mid n_{1}+j, \forall 0 \leq j \leq 2014$. 此时若 $f\left(n_{1}\right) \neq n_{1}$, 显然 $\left(n_{0}+i, n_{1}+j\right)>$ $1, \forall 0 \leq i, j \leq 2014, j \neq 0$, 但 $\left(n_{0}, n_{1}\right)=1$, 与 (1) 矛盾. 于是 $f\left(n_{1}\right)=n_{1}$. 但 $\left(n_{1}, m\right)=1,\left(f\left(n_{1}\right), f(m)\right)=\left(n_{1}, f(m)\right) \geq p$, 矛盾! 这说明假设不成立.

接下来的一个想法是 “平移” : 若存在 $d>n$, 使得 $f(d+i)=d+i(i=$ $1,2, \cdots, 2014)$, 由 (2) 可知 $d \leq f(d) \leq d+2013$, 我们只需导出 $f(d)=d$, 那么以此类推, 就有对 $n \in[N, d], f(n)=n$. 而欲得到 $f(d)=d$, 自然想到证 $f$ 在 $[N,+\infty)$ 为单射, 大概确定一下 $N$ 的范围.

若存在 $a>b>N$, 使得 $f(a)=f(b)$. 由 (1), 有 $(f(a), f(b)) \leq(a, b)^{2014} \leq$ $|a-b|^{2014}$.

由 (2), 易知 $|a-b| \leq 2014$. 而事实上 $(f(a), f(b))=f(a) \geq a>N$, 为推得矛盾, 可取 $N \geq 2014^{2014}+1$. 此时满足了 $f(n)=n$ 的单射性.

最后我们来确定 $d$ 的存在性与无穷性, 以及 $N$ 的取值.

取互异的素数 $p_{j}>2014(j=1,2, \cdots, 4028)$, 取 $d \equiv-j\left(\bmod p_{j}\right)$. 由中国剩余定理知 $d$ 有无穷多个解, 记其中最小的正整数解为 $d_{0}, d_{1}=d_{0}+\prod_{j=1}^{4028} p_{j}$.

易知 $d_{1}>N, p_{j} \mid d_{1}+j$, 且 $p_{j} \nmid d_{1}+i$, 当 $i \neq j$ 时, $1 \leq i \leq 2014$.

由 $(2)$ 知 $d_{1}+i \leq f\left(d_{1}+i\right) \leq 2014+d_{1}+i$, 结合 $p_{j}>2014$, 且

$$
d_{1}+1 \leq f\left(d_{1}+i\right) \leq d_{1}+2014+2014=d_{1}+4028
$$

由引理，必有 $f\left(d_{1}+i\right)=d_{1}+i, 1 \leq i \leq 2014$. 结合上面的 “平移” 思想知 $f(n)=n, n \in\left[N, d_{1}+2014\right]$, 而对于 $\forall n \geq N$, 取合适的 $k$ 使得 $d=$ $d_{0}+k \prod_{i=0}^{4028} p_{i}>n+2014$, 则同上, 必有 $f(n)=n$.

上述讨论对 $N$ 没有额外要求, 故 $N=2014^{2014}+1$ 满足题意. 我们完成了本题的证明.

评注 难度不小. 首先几步中国剩余定理就需要反复地卙酌, 而解题的方向也着实不太好确立.

注意在确定 $f(d+i), 1 \leq i \leq 2014$ 时, 因为有 4028 个可能的取值, 所以不能只取 2014 个素数. 还有, 过程前后的 $p_{i}$ 与 $p_{i, j}$ 无关, 请勿混淆.

其实本题的引理也是一道试题. 笔者对引理的证明可能有些繁琐, 若读者有较为简洁的方法, 可与笔者交流, 谢谢!

后注 上面的例题中有一部分解答是笔者完成的, 由于水平不足和疏忽难免
可能出现纰漏. 若读者发现解答有误, 或有更好的方法, 还请不吝指出. 笔者的邮箱为 m13121806586@163.com.

## 练习题:

1. 试求满足下列条件的函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 对任意的 $m, n \in \mathbb{N}^{*}$, 有 $n+f(m) \mid f(n)+n f(m)$.

提示通过两种变形, 分别为

(1) $n+f(m) \mid f(n)-n^{2}$; (2) $n+f(m) \mid f(n)-f^{2}(m)$.

我们分 $f(n)$ 是否有界进行讨论, 简单讨论可得 (1) $f(n)=n^{2} ;(2) f(n) \equiv 1$,此即为我们所求的所有 $f$.

2. 求所有满射函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 使得对任意的 $m, n \in \mathbb{N}^{*}$ 和任意的素数 $p$, $p \mid m+n$ 当且仅当 $p \mid f(m)+f(n)$.

提示 需先猜测 $f(n)=n$ (这是由于任意素数整除的条件相当强).

我们来分几步完成对此题的证明. 对任意素数 $p$, 找出最小的 $m \in \mathbb{N}^{*}$, 使得 $p \mid f(m)$.

先证 $p|f(x) \Leftrightarrow m| x$, 再证 $f(x) \equiv f(y)(\bmod p) \Leftrightarrow x \equiv y(\bmod m)$. 观察可得 $p=m$ (同样易证). 上述结论有一推论: 若 $x=y+1$, 则 $f(x)=f(y) \pm 1$.后面利用上述推论, 归纳即可证 $f(x)=x$.

3. 是否存在一个函数 $f: \mathbb{N}^{*} \rightarrow \mathbb{N}^{*}$, 满足: (1) 存在 $n \in \mathbb{N}^{*}$, 使得 $f(n) \neq n$; (2) $d(m)=f(n)$ 当且仅当 $d(f(m))=n$, 其中 $d(n)$ 表示 $n$ 的因子个数.

提示存在. 我们如下定义 $f: f(1)=1, f(2)=2, f(3)=5, f(5)=3$.

然后进行递归定义: 假设 $f(k)(1 \leq k \leq n-1)$ 均已被定义，由于 $d(n)<n$,设 $j=f(d(n))$, 则 $j$ 已被定义.

设 $D_{k}=\left\{n \in \mathbb{N}^{*} \mid d(n)=k\right\}$, 而对任意的素数 $p, p^{k-1} \in D_{k}$, 故 $k>1$ 时 $D_{k}$为无穷集.

设 $t$ 为 $D_{j}$ 中未被定义的最小元素, 定义 $f(t)=n, f(n)=t$. 经过验证, 知此函数满足题意.

## 参考文献

[1] Shortlisted Problems with Solutions (2016).http://imoofficial.org/problems /IMO2016SL.pdf.

[2] Function Equation(March 23, 2016). [Online] Available: https:// artofproblemsolving.com/community/c6h1212550.

[3] Proofathon Spring Contest-Problem8(May 1, 2015). [Online] Available: https://artofproblemsolving.com/community/c587h1083995.


[^0]:    收稿日期: 2017-11-12； 修订日期: 2017-12-14.

