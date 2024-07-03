# 第十九期问题征解解答与点评 

牟晓生

第一题. 给定正整数 $n \geq 4$, 设实数 $x_{1}, x_{2}, \ldots, x_{n} \in[0,1]$. 求 $\sum_{i=1}^{n} x_{i}\left|x_{i}-x_{i+1}\right|$的最大值, 约定 $x_{n+1}=x_{1}$.

(湖南雅礼中学学生 汤继尧 供题)

## 证明 (根据供题者的解答整理):

我们将证明当 $n$ 为偶数时, 最大值为 $\frac{n}{2}$; 而当 $n$ 为奇数时, 最大值为 $\frac{n}{2}-\frac{1}{4}$.不难给出取到最大值的例子:

当 $n$ 为偶数时, 令 $x_{1}=x_{3}=\cdots=x_{n-1}=1$, 而 $x_{2}=x_{4}=\cdots=x_{n}=0$;

当 $n$ 为奇数时, 令 $x_{1}=x_{3}=\cdots=x_{n-2}=1, x_{2}=x_{4}=\cdots=x_{n-1}=0$, $x_{n}=\frac{1}{2}$.

下面证明和式不可能更大. 我们对 $n$ 用归纳法, 以 $n=2$ 为归纳基础.

$n=2$ 时要证 $\left(x_{1}+x_{2}\right)\left|x_{1}-x_{2}\right| \leq 1$, 显然成立.

假设命题在 $n-1$ 时成立, 考虑 $n$ 的情况.

如果存在 $i$ 使得 $x_{i} \geq x_{i+1} \geq x_{i+2}$, 则

$$
\begin{aligned}
x_{i}\left|x_{i}-x_{i+1}\right|+x_{i+1}\left|x_{i+1}-x_{i+2}\right| & \leq x_{i}\left(\left|x_{i}-x_{i+1}\right|+\left|x_{i+1}-x_{i+2}\right|\right) \\
& =x_{i}\left|x_{i}-x_{i+2}\right| .
\end{aligned}
$$

此时去掉 $x_{i+1}$ 后应用归纳假设即可.

类似地, 如果 $x_{i} \leq x_{i+1} \leq x_{i+2}$, 则

$$
x_{i}\left|x_{i}-x_{i+1}\right|+x_{i+1}\left|x_{i+1}-x_{i+2}\right| \leq x_{i}\left|x_{i}-x_{i+2}\right|+\frac{1}{4} .
$$

应用归纳假设同样可得命题.

如果 $n$ 是奇数, 那么必定存在 $i$ 使得 $x_{i} \geq x_{i+1} \geq x_{i+2}$ 或者 $x_{i} \leq x_{i+1} \leq x_{i+2}$.这样我们就做完了. 因此只剩下 $n$ 是偶数且 $x_{2 i} \leq x_{2 i-1}, x_{2 i+1}, \forall i$ 的情况. 此时 $\sum_{i=1}^{n} x_{i}\left|x_{i}-x_{i+1}\right|=x_{1}\left(x_{1}-x_{2}\right)+x_{2}\left(x_{3}-x_{2}\right)+x_{3}\left(x_{3}-x_{4}\right)+\cdots+x_{n}\left(x_{1}-x_{n}\right)$.
等号右边是关于 $x_{1}$ 的二次式, 且首项系数为 1 , 因此其最大值在 $x_{1}=1$ 或者 $x_{1}=x_{2}$ 或者 $x_{1}=x_{n}$ 时取到. 后两种情况均可划归为之前的讨论, 所以不妨假设 $x_{1}=1$. 同样地, 我们可以假设 $x_{3}=x_{5}=\cdots=x_{n-1}=1$. 故

$$
\sum_{i=1}^{n} x_{i}\left|x_{i}-x_{i+1}\right|=\frac{n}{2}-x_{2}^{2}-x_{4}^{2}-\cdots-x_{n}^{2} \leq \frac{n}{2}
$$

命题得证!

评注 长沙市长郡中学彭永坚同学也给出了本题的正确解答.

第二题. 如图, 四边形 $A B C D$ 内接于圆 $\Gamma$. $I, I_{1}, I_{2}$ 分别是 $\triangle A B D, \triangle A B C, \triangle A D C$ 的内心.过 $C, I_{1}, I_{2}$ 的圆与圆 $\Gamma$ 交于除 $C$ 外的另一点 $E$, 过 $E$ 作 $E I$ 的垂线交直线 $B D$ 于 $F$. 证明: $I F \perp A I$.



(湖南师大附中 苏林 供题)

## 证明 (根据成都石室中学卢禹杰同学的解答整理):



设 $A I, B I, C I$ 与圆 $\Gamma$ 交于 $L, M, N . M L \cap B N=R, N L \cap D M=S$.

通过角度易知 $\triangle E I_{1} M \sim \triangle E I_{2} N$. 故 $\frac{M E}{N E}=\frac{M I_{1}}{N I_{2}}=\frac{M A}{N A}$.

又 $\frac{M A}{N A}=\frac{M I}{N I}=\frac{M R}{N S}$, 所以 $\frac{M E}{N E}=\frac{M R}{N S}$. 导出 $\triangle E R M \sim \triangle E S N$.

从而 $\angle L R E=\angle L S E$, 故 $E, L, R, S$ 共圆, 并且这个圆经过点 $I$.

于是 $\triangle I E L=\frac{\pi}{2}$, 推出 $F$ 在 $L E$ 的延长线上.

接下来注意到圆 $\Gamma$ 与圆 $E L R I S$ 交于 $L, E$, 圆 $\Gamma$ 与圆 $B I D$ 交于 $B, D$, 因此 $F$ 作为 $L E$ 与 $B D$ 的交点一定是三个圆的根心. 而圆 $E L R I S$ 与圆 $B I D$ (后者圆心为 $L)$ 相切于点 $I$, 所以 $I F \perp A I$.

评注 乐清寄宿中学黄硕董, 如东高级中学张陈成, 象山县第三中学黄子宸,
东北育才学校何雨桐, 长沙市长郡中学曾科荣、彭永坚以及杭州二中包恺成、刘浩宇等同学也给出了本题的正确解答.

第三题. 考虑数列 $x_{1}=1, x_{n+1}=1+\frac{n}{x_{n}}, \forall n \geq 1$. 证明这个数列中只有前三项是整数.

(哈佛大学 牟晓生 供题)

## 证明 (根据杭州二中刘浩宇同学的解答整理):

我们用归纳法证明当 $n \geq 4$ 时有

$$
\frac{1+\sqrt{4 n-3}}{2}<x_{n}<\frac{1+\sqrt{4 n+1}}{2} .
$$

由于 $x_{4}=\frac{5}{2}$, 归纳假设成立.

假设结论对 $n$ 成立, 那么在 $n+1$ 时,

$$
x_{n+1}=1+\frac{n}{x_{n}}>1+\frac{2 n}{1+\sqrt{4 n+1}}=\frac{1+\sqrt{4 n+1}}{2} .
$$

这就是我们所寻求的下界. 另一方面我们有

$$
x_{n+1}<1+\frac{2 n}{1+\sqrt{4 n-3}} .
$$

因此只要证明 $\frac{2 n}{1+\sqrt{4 n-3}}<\frac{\sqrt{4 n+5}-1}{2}$.

令 $t=\sqrt{4 k-3}$, 则只要证 $t^{2}+t+4<(t+1) \sqrt{t^{2}+8}$. 平方展开后等价于 $t>1$, 即 $k>1$, 显然成立. 于是上面的结论成立.

这样我们有 $n-\frac{3}{4}<\left(x_{n}-\frac{1}{2}\right)^{2}<n+\frac{1}{4}$, 即 $n-1<x_{n}^{2}-x_{n}<n$. 因此 $x_{n}$在 $n \geq 4$ 时不可能是整数.

评注 (1). 如东高级中学张陈成以及长沙市长郡中学曾科荣、彭永坚等同学也给出了本题的正确解答.

(2). 这道题看似是数论题, 但上面的解答却几乎只用了代数. 那么是否有偏数论一些的解答呢? 答案是肯定的. 首先令 $x_{n}=\frac{a_{n}}{a_{n-1}}$, 则有递推式

$$
a_{n+1}=a_{n}+n a_{n-1}, a_{0}=a_{1}=1
$$

考虑指数型母函数 $f(x)=\sum_{n \geq 0} \frac{a_{n}}{n !} x^{n}$. 则由这个递推式得到 $f^{\prime}(x)=(1+x) f(x)$.结合 $f(0)=1$ 得到 $f(x)=\exp \left\{x+\frac{x^{2}}{2}\right\}$. 展开后得到

$$
a_{n}=\sum_{k=0}^{\lfloor n / 2\rfloor}\left(\begin{array}{c}
n \\
2 k
\end{array}\right)(2 k) ! !
$$

我们来证明 $a_{n}$ 与 $a_{n+1}$ 的最大公约数只能是 2 的幂次.

事实上, 假设奇素数 $p \mid a_{n}, a_{n+1}$ 且 $p \nmid a_{n-1}$, 则由递推公式知 $p \mid n$. 然而在上面 $a_{n}$ 的直接表达式中若 $p \mid n$, 则 $\left(\begin{array}{l}n \\ 2 k\end{array}\right)$ 在 $p \nmid k$ 时是 $p$ 的倍数, 而 $(2 k) !$ ! 在 $p \mid k$且 $k>0$ 时是 $p$ 的倍数. 因此当 $p \mid n$ 时 $a_{n} \equiv 1(\bmod p)$, 导出矛盾!

接下来我们注意到由归纳法, $a_{n}$ 与 $a_{n+1}$ 的最大公约数整除 $n !$. 由于这个最大公约数是 2 的幂次, 即得 $\left(a_{n}, a_{n+1}\right) \mid 2^{n-1}, \forall n \geq 1$. 然而 $a_{n} \geq(2\lfloor n / 2\rfloor) !$ ! 远远比 $2^{n-1}$ 大, 这样我们就证明了对较大的 $n, a_{n} \nmid a_{n+1}$, 即 $x_{n+1}$ 不是整数.

事实上我们证明了强得多的结论, 即 $x_{n+1}$ 的最简分母 $\frac{a_{n}}{\left(a_{n}, a_{n+1}\right)}$ 随着 $n$ 趋于无穷, 且其增长速度比指数还快. 这些更强的结论是无法用原来巧妙的代数估计得出的.

第四题. 令 $F\left(n ; a_{1}, a_{2}, \ldots, a_{k}\right)$ 为 $1 \sim n$ 中能被某个 $a_{i}$ 整除或能整除某个 $a_{i}$ 的数的个数. 证明若 $1<a_{1}, \ldots, a_{k} \leq n$, 则

$$
F\left(n ; a_{1}, \ldots, a_{k}\right) \leq F\left(n ; p_{1}, \ldots, p_{k}\right)
$$

其中 $p_{1}, p_{2}, \ldots, p_{k}$ 是前 $k$ 个素数.

(哈佛大学 牟晓生 供题)

## 证明 (根据供题者的解答整理):

令 $M\left(n ; a_{1}, \ldots, a_{k}\right)$ 表示 $1 \sim n$ 中能被某个 $a_{i}$ 整除或能整除某个 $a_{i}$ 的数的集合. 我们取 $1<a_{1}, \ldots, a_{k} \leq n$ 使得 $|M|$ 最大, 且在 $|M|$ 相等的情况下使得 $a_{1} \cdots a_{k}$ 的素因子个数(计重数)最小. 我们将证明在这种情况下每个 $a_{i}$ 都是素数. 显然, 我们可以假设 $a_{1}, \ldots, a_{k}$ 互不相等. 先证明以下事实:

1. 假设 $a_{i}=p^{\alpha}, p$ 是素数, 则 $\alpha=1$. 这是因为可以将 $a_{i}$ 调整为 $p$, 使得 $M$中元素不减, 且总的素因子个数变少.
2. 假设 $a_{i}=p$ 为素数, 则 $p \nmid a_{j}, \forall j \neq i$. 事实上, 如果 $a_{j}=p^{\alpha} a_{j}^{\prime}, \alpha>0, p \nmid a_{j}^{\prime}$.那么首先由上一步知道 $a_{j}^{\prime}>1$. 此时把 $a_{j}$ 调整为 $a_{j}^{\prime}$ 可以保证原来 $M$ 中的元素仍在 $M$ 中, 与最优性矛盾 (如果 $x \mid a_{j}, x \nmid a_{j}^{\prime}$, 则 $d$ 是 $p$ 的倍数. 此时 $\left.a_{i} \mid x \Longrightarrow x \in M\right)$.
3. 假设 $a_{i}=p^{\alpha} d, \alpha \geq 1, d>1, p \nmid d$, 则 $d \nmid a_{j}, \forall j \neq i$. 否则设 $d \mid a_{j}$, 则可将 $a_{i}$ 调整为 $p$ 而保证 $M$ 中元素不减.

现在设 $a_{1}, \ldots, a_{r}$ 为合数, $a_{r+1}, \ldots, a_{k}$ 为素数. 由上面的第二点, 我们知道 $\left(a_{\mu}, a_{\nu}\right)=1, \forall \mu \leq r<\nu$. 取不同素数 $q_{1}, q_{2}, \ldots, q_{k}$ 使得: (1) $q_{1}$ 是 $a_{1} \cdots a_{r}$ 的
最小素因子; (2) 每个 $a_{i}$ 均被某个 $q_{j}$ 整除; (3) $q_{v}=a_{v}, \forall r<\nu$.

我们只要证明:

$$
\left|M^{\prime}\right|=\left|M\left(n ; q_{1}, \ldots, q_{k}\right)\right| \geq\left|M\left(n ; a_{1}, \ldots, a_{k}\right)\right|=|M|
$$

对 $\nu=1, \cdots, k$, 令 $m_{\nu}$ 为 $a_{\nu}$ 的约数中与 $q_{1} \cdots q_{k}$ 互素的最大的那个. 例如在 $\nu>r$ 时 $m_{\nu}$ 必然为 1 . 注意到每个在 $M$ 中且不在 $M^{\prime}$ 中的数必定是某个 $a_{\nu}$的因子, 且不被任何 $q_{j}$ 整除, 因此

$$
M-M^{\prime} \subset\left\{d>1: \exists \nu \leq r, d \mid m_{\nu}\right\} .
$$

接下来, 我们将对每个这样的 $d$ 构造一个在 $M^{\prime}$ 中且不在 $M$ 中的数. 只要这些数互不相同就证明了 $\left|M^{\prime}\right| \geq|M|$.

首先考虑 $d \mid m_{\nu}$ 且 $1<d<m_{\nu}$. 令 $\alpha$ 为最大的正整数使得 $A(d)=q_{1}^{\alpha} d \leq n$.由于 $q_{1} d \leq m_{\nu} \leq n, \alpha$ 是存在的, 并且显然有 $A(d) \in M^{\prime}$. 让我们证明 $A(d) \notin M$.事实上, 如果 $A(d) \mid a_{j}$ 则 $A(d)=a_{j}$, 否则 $j \leq r$ 而 $\alpha$ 可以更大. 所以假设 $a_{j} \mid A(d)$, 即 $a_{j}=q_{1}^{\beta} d_{1}$, 其中 $d_{1}|d| a_{\nu}$. 由上面证明的第三点, 要么 $d_{1}=1$,要么 $\beta=0$. 前者导致 $a_{j}=q_{1}^{\beta}=q_{1}$, 与假设 $a_{1} \sim a_{r}$ 为合数矛盾. 后者导致 $a_{j}=d_{1} \mid m_{\nu}$, 与假设 $a_{j}$ 被某个 $q_{\mu}$ 整除而 $m_{\nu}$ 与每个 $q_{\mu}$ 互素矛盾. 这样我们就验证了 $A(d)=q_{1}^{\alpha} d \in M^{\prime}-M$.

其次考虑 $d=m_{\nu}>1$, 故 $\nu \leq r$. 设 $S$ 为这样的 $\nu$ 的个数. 对 $1 \leq i \leq r$,令 $\gamma_{i}$ 为最大的整数使得 $A_{i}=q_{1}^{\gamma_{i}} q_{i} \leq n$. 显然, 这 $r$ 个 $A_{i}$ 互不相同, 且均不同于上面定义的 $A(d)$. 它们都属于 $M^{\prime}$, 而我们将要证明它们中至多有 $r-S$ 个属于 $M$. 事实上, 如果 $A_{i} \mid a_{j}$ 则 $A_{i}=a_{j}$. 所以我们只需考虑 $a_{j} \mid A_{i}, j \leq r$ 的情况. 这时由于 $m_{j} \mid a_{j}$ 而 $m_{j}$ 与 $q_{1} \cdots q_{k}$ 互素, 我们知道 $m_{j}=1$. 这样的不同的 $j$恰有 $r-S$ 个, 所以只要证明同一个 $a_{j}$ 不能整除两个 $A_{i}$ 就行了. 由 $A_{i}$ 的定义,那样会导致 $a_{j}$ 为 $q_{1}$ 的幂, 故而 $a_{j}=q_{1}$, 与假设 $a_{j}$ 为合数矛盾.

因此, $r$ 个 $A_{i}$ 中至少有 $S$ 个属于 $M^{\prime}-M$, 故我们证明了 $\left|M^{\prime}-M\right| \geq$ $\left|M-M^{\prime}\right|$ 也即 $\left|M^{\prime}\right| \geq|M|$. 于是我们也就证明了最初的论断：当 $|M|$ 最大且 $a_{1} \cdots a_{k}$ 的素因子个数最少时每个 $a_{i}$ 都是素数. 显然, 在这种情况下 $|M|$ 的最大值在 $a_{i}=p_{i}$ 时取到, 所以命题得证!

评注 这是 Erdös 在 1949 年向美国数学月刊提供的问题, 而以上漂亮的解答由 George Szekeres 给出. 值得一提的是, George Szekeres 和他的夫人 Esther Klein 证明了平面上一般位置的五个点中必有四个点构成凸四边形, 并且将结
论推广为足够多的点中必有凸 $n$ 边形, 开启了欧式拉姆塞问题的研究. 由于这个问题促成了 Szekeres 和 Klein 的婚姻, Erdös 将其称为 “The Happy Ending Problem” .

