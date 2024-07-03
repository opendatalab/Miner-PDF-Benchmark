数学新星网 * 教师专栏

www.nsmath.cn/jszl

2022 年第三届百年老校数学竞赛试题解答

王彬

(中国科学院数学与系统科学研究院, 100190)

第三届百年老校数学竞赛于 2022 年 8 月 1 日至 5 日在湖南省长沙市雅礼中学举行. 下面介绍本次考试试题及解答.

# I. 试题 

1. 设 $1,2, \ldots, 100$ 的排列 $a_{1}, a_{2}, \ldots, a_{100}$ 满足: 对任意 $1 \leq k<l \leq 100$,或者 $a_{k}$ 与 $a_{l}$ 都是 $l-k$ 的倍数, 或者 $a_{k}$ 与 $a_{l}$ 都不是 $l-k$ 的倍数.

证明: 或者 $a_{1}=1$, 或者 $a_{100}=1$.

(苏州中学 朱磊克 供题)

2. 如图, 在 $\triangle A B C$ 中, $A C>A B$, 点 $D, E$ 分别在边 $A B, A C$ 上, 满足 $D E$ 与 $B C$ 平行, 线段 $B E, C D$ 交于点 $R$. 设点 $A^{\prime}$ 为点 $A$ 关于直线 $B C$ 的对称点, 连接 $A^{\prime} R$ 与 $\triangle A D E$ 的外接圆交于点 $S$.

证明: $\triangle B C S$ 的外接圆与 $\triangle A D E$ 的外接圆相切.

(上海中学 周天佑 供题)



3. 给定实数 $r \in[-1,1]$. 已知实数 $x_{1}, x_{2}, \ldots, x_{100}$ 满足:

$$
\begin{gathered}
x_{1}^{2}+x_{2}^{2}+\cdots+x_{100}^{2}=1 \\
x_{1} x_{2}+x_{2} x_{3}+\cdots+x_{99} x_{100}+x_{100} x_{1}=r .
\end{gathered}
$$

记 $M=x_{1} x_{3}+x_{2} x_{4}+\cdots+x_{98} x_{100}+x_{99} x_{1}+x_{100} x_{2}$.

(1) 证明: $M \geq 2 r^{2}-1$;

(2) 求 $M$ 的最小可能值.

(中国科学院数学与系统科学研究院 王彬 供题)

4. 求最大的正整数 $m$, 使得存在集合 $\{1,2, \ldots, 100\}$ 的 $m$ 个子集 $A_{1}, A_{2}$, $\ldots, A_{m}$ 满足: 对任意 $1 \leq i<j \leq m$, 都有

$$
\left|A_{i} \bigcup A_{j}\right|-\left|A_{i} \bigcap A_{j}\right|=2
$$

(湖南师范大学 羊明亮 供题)

5. 已知 $n$ 次实系数多项式 $f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}$ 满足:对任意 $x \in[0,1] \cup[99,100]$, 都有 $-1 \leq f(x) \leq 1$.

(1) 当 $n=2$ 时, 求 $f(50)$ 的最大可能值;

(2) 当 $n=100$ 时, 求 $f(50)$ 的最大可能值.

(中国科学院数学与系统科学研究院 王彬 供题)

6. 已知正整数 $a, b, c$ 满足

$$
a !=b ! !+c ! !
$$

证明:

$$
a+b+c<2022
$$

注：当 $n$ 是奇数时, $n ! !=1 \times 3 \times 5 \times \cdots \times n$; 当 $n$ 是偶数时, $n ! !=$ $2 \times 4 \times 6 \times \cdots \times n$.

(南方科技大学 付云皓 供题)

## II. 解答

1. 设 $1,2, \ldots, 100$ 的排列 $a_{1}, a_{2}, \ldots, a_{100}$ 满足: 对任意 $1 \leq k<l \leq 100$, 或者 $a_{k}$ 与 $a_{l}$ 都是 $l-k$ 的倍数, 或者 $a_{k}$ 与 $a_{l}$ 都不是 $l-k$ 的倍数.

证明: 或者 $a_{1}=1$, 或者 $a_{100}=1$.
解. 由于 $1,2, \ldots, 100$ 的排列中只有一项是 51 的倍数, 设 $a_{k}=51$, 则 $a_{k+51}$与 $a_{k-51}$ (如果脚标不出界) 也是 51 的倍数, 因此一定有 $k+51>100$ 以及 $k-51<1$. 这样可得 $k=51$ 或 50 , 即 $a_{51}=51$ 或 $a_{50}=51$. 由于若排列 $a_{1}, a_{2}, \ldots, a_{100}$ 满足题意, 则其反序 $a_{100}, a_{99}, \ldots, a_{2}, a_{1}$ 亦满足条件. 故不妨设 $a_{51}=51$.

接下来考虑 $a_{1}$ 的取值. 设 $a_{1}=m$, 做带余除法, 设 $100=k m+r,(0 \leq$ $r \leq m-1)$. 若 $r \neq 0$ 则 $a_{1}, a_{1+m}, \ldots, a_{1+k m}$ 都是 $m$ 的倍数, 共有 $k+1$ 个. 但 $1,2, \ldots, 100$ 中只有 $k$ 个 $m$ 的倍数, 矛盾. 因此 $r=0$, 即 $a_{1}$ 是 100 的约数.

若 $a_{1}$ 是偶数, 则可依次推出 $a_{3}, a_{5}, a_{7}, \ldots, a_{51}$ 均为偶数, 与 $a_{51}=51$ 矛盾.

若 $a_{1}$ 是 5 的倍数, 则可依次推出 $a_{6}, a_{11}, a_{16}, \ldots, a_{51}$ 均为 5 的倍数，与 $a_{51}=51$ 矛盾.

因此 $a_{1}$ 与 2,5 互质, 且是 100 的约数, 只能 $a_{1}=1$. (若第一段中是 $a_{50}=$ 51, 则可类似推出 $a_{100}=1$.)

注 1. 若把题目中的 100 换成一般的正整数 $n$, 则本题结论在 $n$ 是 4 的倍数时成立, 并且命题人已证明 $n \leq 100$ 时本题结论均成立.

注 2. 若将排列 $1,2, \ldots, n-1, n$ 与排列 $n, n-1, \ldots, 2,1$ 视为平凡排列, 则对某些 $n$ 存在满足题目要求的非平凡排列. 例如 $n=5$ 时的排列 $1,4,3,2,5$, 或者在 $2^{k+1} \leq n<3 \times 2^{k}$ 时，将排列 $1,2, \ldots, n$ 中的 $2^{k}$ 与 $2^{k+1}$ 交换位置后得到的排列.

2. 如图, 在 $\triangle A B C$ 中, $A C>A B$, 点 $D, E$ 分别在边 $A B, A C$ 上, 满足 $D E$ 与 $B C$ 平行, 线段 $B E, C D$ 交于点 $R$. 设点 $A^{\prime}$ 为点 $A$ 关于直线 $B C$ 的对称点, 连接 $A^{\prime} R$ 与 $\triangle A D E$ 的外接圆交于点 $S$.

证明: $\triangle B C S$ 的外接圆与 $\triangle A D E$ 的外接圆相切.


解. 作 $A T \| D E$ 交 $\triangle A D E$ 的外接圆于点 $T$, 过 $A$ 作 $\triangle A B C$ 外接圆的切线与直线 $B C$ 交于点 $X$. 易知 $\triangle T D E \cong \triangle A E D \sim \triangle A C B \cong A^{\prime} C B$, 故 $\angle T D E=\angle A^{\prime} C B$. 由 $D E \| B C$ 知 $\angle E D R=\angle B C R$, 故

$$
\angle T D R=\angle T D E+\angle E D R=\angle A^{\prime} C B+\angle B C R=\angle A^{\prime} C R .
$$

因此 $D T \| A^{\prime} C$, 同理 $E T \| A^{\prime} B$. 因此 $\triangle T D E$ 与 $\triangle A^{\prime} C B$ 是以点 $R$ 为位似中心的位似形, 故 $T, R, A^{\prime}$ 共线, 即 $T, R, S, A^{\prime}$ 共线.

由对称性知 $X A=X A^{\prime}$. 由于

$\angle A S T=\angle A D T=\angle A D E-\angle T D E=\angle A B C-\angle A C B=\angle A B C-\angle X A B=\angle A X B$.

且 $\angle A X B=\frac{1}{2} \angle A X A^{\prime}$ 等于在以 $X$ 为圆心, $X A$ 为半径的圆上, 劣弧 $\widehat{A A^{\prime}}$ 所对的圆周角. 因此 $S$ 也在此圆上, 故 $X S=X A$. 注意 $X A$ 同时也是 $\triangle A D E$的外接圆切线, 因此 $X S$ 也是 $\triangle A D E$ 的外接圆切线.

由切割线定理知 $X B \cdot X C=X A^{2}=X S^{2}$, 故 $X S$ 也是 $\triangle B C S$ 的外接圆的切线, 即这两个圆在公共点 $S$ 处的切线是同一条直线, 因此它们相切.

3. 给定实数 $r \in[-1,1]$. 已知实数 $x_{1}, x_{2}, \ldots, x_{100}$ 满足:

$$
\begin{gathered}
x_{1}^{2}+x_{2}^{2}+\cdots+x_{100}^{2}=1 \\
x_{1} x_{2}+x_{2} x_{3}+\cdots+x_{99} x_{100}+x_{100} x_{1}=r .
\end{gathered}
$$

记 $M=x_{1} x_{3}+x_{2} x_{4}+\cdots+x_{98} x_{100}+x_{99} x_{1}+x_{100} x_{2}$.

(1) 证明: $M \geq 2 r^{2}-1$;

(2) 求 $M$ 的最小可能值.

解. (1) 记 $n=100$, 设角标模 $n$ 考虑 (即 $x_{n+k}=x_{k}$ ).

对 $k=0,1,2$, 记 $M_{k}=\sum_{i=0}^{n-1} x_{i} x_{i+k}$. 在 $M_{0}=1, M_{1}=r$ 的条件下考虑 $M_{2}$.

$$
\begin{aligned}
& \sum_{k=0}^{n-1}\left(x_{k-1}+x_{k+1}-2 r x_{k}\right)^{2} \\
&= \sum_{k=0}^{n-1}\left(x_{k-1}^{2}+x_{k+1}^{2}+4 r^{2} x_{k}^{2}-4 r x_{k-1} x_{k}-4 r x_{k} x_{k+1}+2 x_{k-1} x_{k+1}\right) \\
&=\left(4 r^{2}+2\right) M_{0}-8 r M_{1}+2 M_{2} \geq 0 \\
& \therefore M_{2} \geq 4 r \times M_{1}-\left(2 r^{2}+1\right) \times M_{0}=2 r^{2}-1 .
\end{aligned}
$$

(2) 记复数 $\omega=\cos \frac{2 \pi}{n}+i \sin \frac{2 \pi}{n}$ 满足 $\omega^{n}=1$, 记 $\omega_{j}=\omega^{j},\left(\omega_{j}^{k}=\omega_{k j}\right.$, 脚标模 $n)$.
考虑多项式 $F(z)=x_{0}+x_{1} z^{1}+x_{2} z^{2}+\cdots+x_{n-1} z^{n-1}$ 在 $\left\{1, \omega_{1}, \ldots, \omega_{n-1}\right\}$ (即所有 $n$ 次单位根) 处的取值, 记

$$
f_{j}=F\left(\omega_{j}\right)=x_{0}+x_{1} \omega_{j}+x_{2} \omega_{2 j}+\cdots+x_{n-1} \omega_{(n-1) j}, \quad j=0,1,2, \ldots, n-1
$$

由于 $F(z)$ 是实系数多项式, 我们有 $f_{n-j}=F\left(\omega_{n-j}\right)=F\left(\overline{\omega_{j}}\right)=\overline{F\left(\omega_{j}\right)}=\overline{f_{j}}$,

即 $f_{j}, f_{n-j}$ 为共轭复数. 考虑 Lagrange 插值多项式, 尝试由 $F(z)$ 在 $\left\{1, \omega_{1}, \ldots, \omega_{n-1}\right\}$处的取值 $\left(f_{0}, f_{1}, \ldots, f_{n-1}\right)$ 反推 $F(z)$ 的各个系数. 即对 $k=0,1, \ldots, n-1$ 依次考虑多项式 $G_{k}(z)$ 在 $\omega_{k}$ 处取值为 1 , 其余 $\omega_{j}(j \neq k)$ 处取值为 0 .

$G_{k}(z)=\frac{\prod_{j \neq k}\left(z-\omega_{j}\right)}{\prod_{j \neq k}\left(\omega_{k}-\omega_{j}\right)}=\frac{1}{n \omega_{k}^{-1}} \frac{z^{n}-1}{z-\omega_{k}}=\frac{1}{n}\left(1+\omega_{-k} z+\omega_{-2 k} z^{2}+\cdots+\omega_{-(n-1) k} z^{n-1}\right)$.

因此由 Lagrange 插值多项式可知

$$
F(z)=f_{0} \times G_{0}(z)+f_{1} \times G_{1}(z)+\cdots+f_{n-1} \times G_{n-1}(z) .
$$

即

$$
x_{k}=\frac{1}{n} \sum_{j=0}^{n-1} f_{j} \times \omega_{-k j}, k=0,1, \ldots, n-1 .
$$

这样

$$
\begin{aligned}
& M_{0}=\sum_{k=0}^{n-1} x_{k}^{2}=\frac{1}{n^{2}} \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} f_{i} f_{j} \omega_{-i k} \omega_{-j k} \\
& =\frac{1}{n} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} f_{i} f_{j}\left(\frac{1}{n} \sum_{k=0}^{n-1} \omega_{-(i+j) k}\right) \\
& =\frac{1}{n} \sum_{i=0}^{n-1} f_{i} f_{n-i}=\frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \\
& M_{1}=\sum_{k=0}^{n-1} x_{k-1} x_{k}=\frac{1}{n^{2}} \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} f_{i} f_{j} \omega_{-i(k-1)} \omega_{-j k} \\
& =\frac{1}{n} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} f_{i} f_{j}\left(\frac{1}{n} \sum_{k=0}^{n-1} \omega_{-(i+j) k}\right) \omega_{i} \\
& =\frac{1}{n} \sum_{i=0}^{n-1} f_{i} f_{n-i} \omega_{i}=\frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \omega_{l}=\frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \cos \frac{2 l \pi}{n} \\
& M_{2}=\sum_{k=0}^{n-1} x_{k-2} x_{k}=\frac{1}{n^{2}} \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} f_{i} f_{j} \omega_{-i(k-2)} \omega_{-j k} \\
& =\frac{1}{n} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} f_{i} f_{j}\left(\frac{1}{n} \sum_{k=0}^{n-1} \omega_{-(i+j) k}\right) \omega_{2 i}
\end{aligned}
$$

$$
=\frac{1}{n} \sum_{i=0}^{n-1} f_{i} f_{n-i} \omega_{2 i}=\frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \omega_{2 l}=\frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \cos \frac{4 l \pi}{n} .
$$

上面的式子中用到 $\frac{1}{n} \sum_{k=0}^{n-1} \omega_{j k}=\mathbf{1}_{\{n \mid j\}}$.

对 $l=0,1, \ldots, n-1$, 记 $\lambda_{l}=\cos \frac{2 l \pi}{n}$, 则 $1=\lambda_{0}>\lambda_{1}>\cdots>\lambda_{\frac{n}{2}}=-1$, $\left(\lambda_{n-l}=\lambda_{l}\right)$.

设 $r=\cos \theta(\theta \in[0, \pi])$, 取 $m=\left\lfloor\frac{n \theta}{2 \pi}\right\rfloor=\left\lfloor\frac{n \arccos r}{2 \pi}\right\rfloor$ 使得

$$
\cos \frac{m \times 2 \pi}{n}=\lambda_{m} \geq r \geq \lambda_{m+1}=\cos \frac{(m+1) \times 2 \pi}{n}
$$

此时对每个 $\lambda_{l}$, 我们有 $\left(\lambda_{l}-\lambda_{m}\right)\left(\lambda_{l}-\lambda_{m+1}\right) \geq 0$, 即

$$
\begin{aligned}
& \lambda_{l}^{2} \geq\left(\lambda_{m}+\lambda_{m+1}\right) \lambda_{l}-\lambda_{m} \lambda_{m+1}, l=0,1, \ldots, n-1 \\
& \lambda_{2 l}=2 \lambda_{l}^{2}-1 \geq 2\left(\lambda_{m}+\lambda_{m+1}\right) \lambda_{l}-2 \lambda_{m} \lambda_{m+1}-1 \\
& M_{2}=\frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \lambda_{2 l} \geq \frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2}\left[2\left(\lambda_{m}+\lambda_{m+1}\right) \lambda_{l}-2 \lambda_{m} \lambda_{m+1}-1\right] \\
&= 2\left(\lambda_{m}+\lambda_{m+1}\right) \times \frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \lambda_{l}-\left(2 \lambda_{m} \lambda_{m+1}+1\right) \times \frac{1}{n} \sum_{l=0}^{n-1}\left|f_{l}\right|^{2} \\
&= 2\left(\lambda_{m}+\lambda_{m+1}\right) M_{1}-\left(2 \lambda_{m} \lambda_{m+1}+1\right) M_{0}
\end{aligned}
$$

因此 $M=M_{2}$ 的最小值是 $M^{\star}=2\left(\lambda_{m}+\lambda_{m+1}\right) r-\left(2 \lambda_{m} \lambda_{m+1}+1\right)$, 即 $M^{\star}=2\left(\cos \frac{2 m \pi}{n}+\cos \frac{2(m+1) \pi}{n}\right) r-\left(2 \cos \frac{2 m \pi}{n} \cos \frac{2(m+1) \pi}{n}+1\right), m=\left\lfloor\frac{n \arccos r}{2 \pi}\right\rfloor$.

构造最小值点: 对 $k=0,1, \ldots, \frac{n}{2}$, 考虑向量

$$
\begin{aligned}
\alpha_{k} & =\left(1, \cos \frac{2 k \pi}{n}, \cos \frac{4 k \pi}{n}, \cos \frac{6 k \pi}{n}, \ldots, \cos \frac{2(n-1) k \pi}{n}\right), \\
\beta_{k} & =\left(0, \sin \frac{2 k \pi}{n}, \sin \frac{4 k \pi}{n}, \sin \frac{6 k \pi}{n}, \ldots, \sin \frac{2(n-1) k \pi}{n}\right) .
\end{aligned}
$$

(在 Lagrange 插值计算中, 取 $f_{k}=f_{n-k}=1$ 其余 $f_{j}=0$, 可得向量 $\alpha_{k}$;取 $f_{k}=i, f_{n-k}=-i$, 其余 $f_{j}=0$, 可得向量 $\beta_{k}$.)

容易验证向量 $\alpha_{0}, \alpha_{1}, \ldots, \alpha_{\frac{n}{2}}, \beta_{1}, \beta_{2}, \ldots, \beta_{\frac{n}{2}-1}$ 两两正交. 并且 $\alpha_{k}$ 经过移位之后的 $\alpha_{k}^{\prime}=\left(\cos \frac{2 k \pi}{n}, \cos \frac{4 k \pi}{n}, \ldots, \cos \frac{(n-1) k \pi}{n}, 1\right)=\cos \frac{2 k \pi}{n} \alpha_{k}-\sin \frac{2 k \pi}{n} \beta_{k}$ 满足内积 $\left(\alpha_{k}, \alpha_{k}^{\prime}\right)=\lambda_{k}\left|\alpha_{k}\right|^{2}$; 再次移位之后的 $\alpha_{k}^{\prime \prime}=\left(\cos \frac{4 k \pi}{n}, \ldots, \cos \frac{(n-1) k \pi}{n}, 1, \cos \frac{2 k \pi}{n}\right)=$ $\cos \frac{4 k \pi}{n} \alpha_{k}-\sin \frac{4 k \pi}{n} \beta_{k}$ 满足内积 $\left(\alpha_{k}, \alpha_{k}^{\prime \prime}\right)=\lambda_{2 k}\left|\alpha_{k}\right|^{2}$.

最后取

$$
\mathbf{X}=\left(x_{0}, x_{1}, \ldots, x_{n-1}\right)=\sqrt{\frac{r-\lambda_{m+1}}{\lambda_{m}-\lambda_{m+1}}} \times \frac{\alpha_{m}}{\left|\alpha_{m}\right|}+\sqrt{\frac{\lambda_{m}-r}{\lambda_{m}-\lambda_{m+1}}} \times \frac{\alpha_{m+1}}{\left|\alpha_{m+1}\right|}
$$

即可满足 $M_{0}=1$, 以及

$$
\begin{gathered}
M_{1}=\frac{r-\lambda_{m+1}}{\lambda_{m}-\lambda_{m+1}} \times \lambda_{m}+\frac{\lambda_{m}-r}{\lambda_{m}-\lambda_{m+1}} \times \lambda_{m+1}=r \\
M_{2}=\frac{r-\lambda_{m+1}}{\lambda_{m}-\lambda_{m+1}} \times\left(2 \lambda_{m}^{2}-1\right)+\frac{\lambda_{m}-r}{\lambda_{m}-\lambda_{m+1}} \times\left(2 \lambda_{m+1}^{2}-1\right)=M^{\star} .
\end{gathered}
$$

注 1. 第一问也可用柯西不等式证明:

$\left(2 M_{2}+2 M_{0}\right) M_{0}=\sum_{k=0}^{n-1}\left(x_{k-1}+x_{k+1}\right)^{2} \times \sum_{k=0}^{n-1} x_{k}^{2} \geq\left(\sum_{k=0}^{n-1}\left(x_{k-1}+x_{k+1}\right) x_{k}\right)^{2}=\left(2 M_{1}\right)^{2}$.

注 2. 本题的另一种思路是: 考虑第一问取等 $M_{2}=2 r^{2}-1$ 的情况, 发现只有在 $r=\cos \frac{2 k \pi}{n}$ 时才可能取等. 取等时 $x_{i+1}+x_{i-1}=2 r x_{i}$ 意味着 $\mathbf{X}=$ $\left(x_{0}, x_{1}, \ldots, x_{n-1}\right)$ 是 $\alpha_{k}$ 与 $\beta_{k}$ 的线性组合. 接下来看出 $\left\{\alpha_{0}, \ldots, \alpha_{\frac{n}{2}}, \beta_{1}, \ldots, \beta_{\frac{n}{2}-1}\right\}$两两正交, 构成 $\mathbb{R}^{n}$ 的一组正交基, 故可以对向量 $\mathbf{X}$ 考虑正交分解.

另一方面, 我们考虑矩阵 (以 $n=8$ 为例) 及二次型.

$$
A=\frac{1}{2} \times\left(\begin{array}{cccccccc}
0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{array}\right), B=2 A^{2}-I=\frac{1}{2} \times\left(\begin{array}{cccccccc}
0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 1 & 0 & 0
\end{array}\right) .
$$

我们在已知 $X X^{T}=1$ 与 $X A X^{T}=r$ 时最小化 $X B X^{T}$, 可以理解为诸特征值 $\lambda$ 的加权平均为 $r$ 时 (权即为各特征方向所占比重), 考虑 $2 \lambda^{2}-1$ 的加权平均最小化. 由凸性即可知平均值 $\geq 2 r^{2}-1$, 由 $\lambda$ 取值的离散性可得稍大的下界. 该下界与 $2 r^{2}-1$ 的差恰好是 $r$ 与其左右最近可能 $\lambda$ 值距离的乘积的两倍.

这一结果也可以理解为: 点集 $\left\{\left(\lambda, 2 \lambda^{2}-1\right): \lambda=\cos \frac{2 k \pi}{n}, k=0,1, \ldots, \frac{n}{2}\right\}$ 的凸包即为 $\left(M_{1}, M_{2}\right)$ 的取值范围. 点集凸包在直线 $x=r$ 上所截的区间即为：固定 $M_{0}=1, M_{1}=r$ 时 $M_{2}$ 的取值范围. $M_{2}$ 的最小可能值 (视为 $r$ 的函数) 是分段线性函数 (一条折线).

注 3. 本题有离散傅里叶变换 (Discrete Fourier Transform) 的背景, 即把一个周期序列表示为若干个正弦、余弦序列之和（也类似于傅里叶级数的离散点取值)。对时域周期序列 $\left(x_{0}, x_{1}, \ldots, x_{n-1}\right)$, 二次式 $M_{0}, M_{1}, M_{2}, \ldots$ 的值与该序
列的自相关函数有关，因而与其频域的能量分布 $\left(f_{0}, f_{1}, \ldots, f_{n-1}\right.$ 的值) 有关.

解答中用母函数 (多项式模 $x^{n}-1$ 的余式) 来理解围成一圈的 $n$ 个数, 也是一种比较自然的联系到离散傅里叶变换的方法.

注 4. 当 $r=M_{1} \geq \frac{1}{2}$ 时, 也可以用配方法得到 $M_{3} \geq 4 r^{3}-3 r$.

$$
\begin{aligned}
& \sum_{k=0}^{n-1}(2 r+1)\left[x_{k+3}+x_{k}-(2 r-1)\left(x_{k+2}+x_{k+1}\right)\right]^{2} \\
&+ \sum_{k=0}^{n-1}(2 r-1)\left[x_{k+3}-x_{k}-(2 r+1)\left(x_{k+2}-x_{k+1}\right)\right]^{2} \\
&=(2 r+1)\left[\left(8 r^{2}-8 r+4\right) M_{0}+2(2 r-1)(2 r-3) M_{1}-4(2 r-1) M_{2}+2 M_{3}\right] \\
&+(2 r-1)\left[\left(8 r^{2}+8 r+4\right) M_{0}-2(2 r+1)(2 r+3) M_{1}+4(2 r+1) M_{2}-2 M_{3}\right] \geq 0 \\
& \therefore M_{3} \geq\left[\left(4 r^{2}-1\right) \times 12 M_{1}-32 r^{3} \times M_{0}\right] / 4=4 r^{3}-3 r .
\end{aligned}
$$

进一步的, 用类似的方法可知: 点集 $\left\{\left(\lambda, 4 \lambda^{3}-3 \lambda\right): \lambda=\cos \frac{2 k \pi}{n}, k=\right.$ $\left.0,1, \ldots, \frac{n}{2}\right\}$ 的凸包即为 $\left(M_{1}, M_{3}\right)$ 的取值范围.

4. 求最大的正整数 $m$, 使得存在集合 $\{1,2, \ldots, 100\}$ 的 $m$ 个子集 $A_{1}, A_{2}$, $\ldots, A_{m}$ 满足: 对任意 $1 \leq i<j \leq m$ ，都有

$$
\left|A_{i} \bigcup A_{j}\right|-\left|A_{i} \bigcap A_{j}\right|=2 .
$$

解. 当 $m=100$ 时, 可取 $A_{k}=\{k\}, k=1,2, \ldots, 100$ 满足条件.

下证 $m \geq 101$ 不满足题目条件. 假设不然, 则对任意 $1 \leq i<j \leq 101$, 都有 $\left|A_{i} \cup A_{j}\right|-\left|A_{i} \cap A_{j}\right|=2$.

对任意 $n \in\{1,2,3, \ldots, 100\}$, 我们可以把 $A_{1}, A_{2}, \ldots, A_{101}$ 里所有含 $n$ 的集合中的 $n$ 去掉, 同时在 $A_{1}, A_{2}, \ldots, A_{101}$ 里所有不含 $n$ 的集合中加上一个元素 $n$, 这样的操作不改变任何 $\left|A_{i} \cup A_{j}\right|-\left|A_{i} \cap A_{j}\right|$ 的值. 对 $A_{101}$ 中的元素不断进行这个操作, 最终可以把 $A_{101}$ 变为空集. 故我们可以假设 $A_{101}$ 是空集.

此时由 $\left|A_{i} \cup A_{101}\right|-\left|A_{i} \cap A_{101}\right|=2$ 可知 $\left|A_{i}\right|=2, i=1,2, \ldots, 100$. 进一步的,

$2=\left|A_{i} \cup A_{j}\right|-\left|A_{i} \cap A_{j}\right|=\left|A_{i}\right|+\left|A_{j}\right|-2\left|A_{i} \cap A_{j}\right| \Rightarrow\left|A_{i} \cap A_{j}\right|=1, \forall 1 \leq i<j \leq 100$.

由对称性, 不妨设 $A_{1}=\{1,2\}, A_{2}=\{1,3\}$. 注意 $A_{1}, A_{2}, \ldots, A_{100}$ 两两不同, 但 $\{1,2, \ldots, 100\}$ 的含 1 的二元子集仅有 99 个，故不妨设 $1 \notin A_{3}$. 由 $\left|A_{3} \cap A_{1}\right|=\left|A_{3} \cap A_{2}\right|=1$ 知 $A_{3}=\{2,3\}$. 但这样无论如何选取 $A_{4}$ 都不可能使 $\left|A_{4} \cap A_{1}\right|=\left|A_{4} \cap A_{2}\right|=\left|A_{4} \cap A_{3}\right|=1$, 矛盾. 因此 $m \leq 100$.
综上所述, 所求最大的 $m=100$.

注. 如果把题目条件松驰为 $\left|A_{i} \cup A_{j}\right|-\left|A_{i} \cap A_{j}\right|=2 t, \forall 1 \leq i<j \leq m$, 我们也可以用线性代数的方法证明 $m \leq 100$.

用反证法, 假设 $m \geq 101$, 由类似解法一的分析知: 我们可假设 $A_{101}$ 是空集. 进而 $\left|A_{i}\right|=2 t, i=1,2, \ldots, 100$, 以及 $\left|A_{i} \cap A_{j}\right|=t, \forall 1 \leq i<j \leq 100$.

接下来, 记 $x_{k, u}=\left\{\begin{array}{l}0 \text { 若 } u \notin A_{k} \\ 1 \text { 若 } u \in A_{k}\end{array}\right.$, 我们考虑矩阵 $M=\left(x_{k, u}\right)_{100 \times 100}$, 以及行向量 $\alpha_{k}=\left(x_{k, 1}, x_{k, 2}, \ldots, x_{k, 100}\right), k=1,2, \ldots, 100$. 行向量之间的内积为: $\left(\alpha_{k}, \alpha_{k}\right)=2 t,\left(\alpha_{k}, \alpha_{l}\right)=t, k \neq l$, 因此:

$$
M M^{T}=\left(\begin{array}{cccccc}
2 t & t & t & \cdots & \cdots & t \\
t & 2 t & t & \cdots & \cdots & t \\
t & t & 2 t & \ldots & \ldots & t \\
\ldots & \ldots & \ldots & \ldots & \\
\ldots & \ldots & \ldots & & \ldots & \\
t & t & t & \cdots & \cdots & 2 t
\end{array}\right) \Rightarrow \operatorname{det}\left(M M^{T}\right)=(n+1) t^{n}=101 t^{100} .
$$

上式与 $\operatorname{det}\left(M M^{T}\right)=\operatorname{det}(M) \times \operatorname{det}\left(M^{T}\right)=(\operatorname{det}(M))^{2}$ 是整数的平方矛盾.因此 $m \leq 100$.

5. 已知 $n$ 次实系数多项式 $f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}$ 满足:对任意 $x \in[0,1] \cup[99,100]$, 都有 $-1 \leq f(x) \leq 1$.

(1) 当 $n=2$ 时, 求 $f(50)$ 的最大可能值;

(2) 当 $n=100$ 时, 求 $f(50)$ 的最大可能值.

解. 由于 $n$ 是偶数, 记 $n=2 m$. 考虑多项式 $f_{1}(x)=\frac{1}{2}[f(50+x)+f(50-x)]$满足 $f_{1}(x)=f_{1}(-x)$ 是偶函数, 即只含偶数次项, 因此存在 $m$ 次多项式 $g(\cdot)$ (首项系数为 $\left.a_{n} \neq 0\right)$ 满足 $g\left(x^{2}\right)=f_{1}(x)$. 这样多项式 $g(y)$ 满足

$$
-1 \leq g(y) \leq 1, \quad \forall y \in\left[49^{2}, 50^{2}\right]=[2401,2500]
$$

我们关注 $g(0)=f(50)$ 的最大值, 考虑将区间 $[2401,2500]$ 变换到 $[-1,1]$, 即考虑多项式 $h(x)=g\left(\frac{4901-99 x}{2}\right)$ 满足

$$
-1 \leq h(x) \leq 1, \quad \forall x \in[-1,1]
$$

记 $x^{\star}=\frac{4901}{99}=\frac{1}{2}\left(99+\frac{1}{99}\right)$, 我们关注 $h\left(x^{\star}\right)=g(0)=f(50)$ 的最大可能值.

为此我们考虑切比雪夫多项式 (族)

$$
T_{0}(x)=1, T_{1}(x)=x, T_{2}(x)=2 x^{2}-1, T_{3}(x)=4 x^{3}-3 x, \ldots
$$

$$
T_{k+1}(x)=2 x T_{k}(x)-T_{k-1}(x), \quad k=1,2, \ldots
$$

其中 $T_{m}(x)$ 是 $m$ 次多项式, 满足 $T_{m}(\cos \theta)=\cos (m \theta)$, (进而对任意 $x \in$ $[-1,1]$ 均有 $\left.-1 \leq T_{m}(x) \leq 1\right)$. 记 $b_{k}=\cos \frac{k \pi}{m}, k=0,1,2, \ldots, m$, 我们有

$$
T_{m}\left(b_{k}\right)=T_{m}\left(\cos \frac{k \pi}{m}\right)=\cos k \pi=(-1)^{k}, k=0,1,2, \ldots, m
$$

对任意 $r>1$, 我们断言 $h(r) \leq T_{m}(r)$. 若不然, 可取 $\epsilon>0$ 使得 $h(r)>$ $(1+\epsilon) T_{m}(r)$, 此时 $m$ 次的多项式 $P(x)=h(x)-(1+\epsilon) T_{m}(x)$ (适当选取 $\epsilon$ 使 $P(x)$ 的 $x^{m}$ 项系数 $\neq 0$ ), 满足 $P(r)>0$ 以及

$$
P\left(b_{k}\right)=h\left(b_{k}\right)-(1+\epsilon)(-1)^{k}\left\{\begin{array}{l}
<0 \text { 若 } k \text { 是偶数 } \\
>0 \text { 若 } k \text { 是奇数 }
\end{array}, k=0,1, \ldots, m .\right.
$$

由连续函数介值定理可知 $P(x)$ 在开区间 $\left(b_{k+1}, b_{k}\right)$ 内 $(k=0,1, \ldots, m-1)$以及在开区间 $(1, r)$ 内各有至少一个实根, 共有至少 $m+1$ 个实根, 矛盾. 因此我们有 $h(r) \leq T_{m}(r)$, 特别的对 $r=x^{\star}=\frac{1}{2}\left(99+\frac{1}{99}\right)>1$, 我们有 $h\left(x^{\star}\right) \leq T_{m}\left(x^{\star}\right)$.

对 $x^{\star}=\frac{1}{2}\left(99+\frac{1}{99}\right)$ 易知 $T_{1}\left(x^{\star}\right)=\frac{1}{2}\left(99+\frac{1}{99}\right), T_{2}\left(x^{\star}\right)=\frac{1}{2}\left(99^{2}+\frac{1}{99^{2}}\right)$. 对 $k$归纳, 用递推式 $T_{k+1}(x)=2 x T_{k}(x)-T_{k-1}(x)$ 可得 $T_{k}\left(x^{\star}\right)=\frac{1}{2}\left(99^{k}+\frac{1}{99^{k}}\right)$. 因此

$$
f(50)=g(0)=h\left(x^{\star}\right) \leq T_{m}\left(x^{\star}\right)=\frac{1}{2}\left(99^{m}+\frac{1}{99^{m}}\right) .
$$

构造时取切比雪夫多项式 $T_{m}(x)$, 取 $h(x)=T_{m}(x)$, 取 $g(x)=h\left(\frac{4901-2 x}{99}\right)$,取

$$
f_{\star}(x)=g\left((x-50)^{2}\right)=T_{m}\left(\frac{4901-2(x-50)^{2}}{99}\right)
$$

满足题目条件, 且 $f_{\star}(50)=T_{m}\left(x^{\star}\right)=\frac{1}{2}\left(99^{m}+\frac{1}{99^{m}}\right)$.

例如 $n=2$ 时, $f_{\star}(x)=\frac{4901-2(x-50)^{2}}{99}=\frac{2}{99} x(100-x)-1$.

注 1. 可以用 Lagrange 插值多项式来证明 $h(r) \leq T_{m}(r)$. 取多项式

$$
g_{k}(x)=\prod_{j \neq k} \frac{x-b_{j}}{b_{k}-b_{j}}, k=0,1, \ldots, m
$$

我们有

$h(r)=\sum_{k=0}^{m} h\left(b_{k}\right) g_{k}(r) \leq \sum_{k=0}^{m}\left|g_{k}(r)\right|=\sum_{k=0}^{m}(-1)^{k} g_{k}(r)=\sum_{k=0}^{m} T_{m}\left(b_{k}\right) g_{k}\left(b_{k}\right)=T_{m}(r)$.

注 2. 对任意 $t \in[1,99]$, 我们可以证明: $f_{\star}(x)$ 也使得 $f(t)$ 最大化, 因为多项式 $f(x)$ 与 $f_{\star}(x)$ 在区间 $(0,1)$ 内相交 $\geq m$ 次, 在区间 $(99,100)$ 内相交 $\geq m$次. 因此无法在区间 $(1,99)$ 内相交, 即 $f(t) \leq f_{\star}(t), \forall t \in[1,99]$.
注 3. 切比雪夫多项式 $T_{m}(\cdot)$ 可以表示为

$$
T_{m}(x)=\frac{1}{2}\left(\left(x+\sqrt{x^{2}-1}\right)^{m}+\left(x-\sqrt{x^{2}-1}\right)^{m}\right), x \geq 1
$$

或者理解为

$$
T_{m}\left(\frac{1}{2}\left(t+\frac{1}{t}\right)\right)=\frac{1}{2}\left(t^{m}+\frac{1}{t^{m}}\right) .
$$

6. 已知正整数 $a, b, c$ 满足

$$
a !=b ! !+c ! !
$$

证明:

$$
a+b+c<2022 \text {. }
$$

证明. 不妨设 $b \leq c$. 如果 $b, c$ 不同奇偶, 那么 $a !=b ! !+c !$ ! 是奇数, 进而 $a=1$, 矛盾. 故 $b, c$ 奇偶性相同.

当 $c \leq 2$ 时, 逐一检验仅有 $a=2, b=c=1$ 符合题意, 此时 $a+b+c<2022$.

下设 $c \geq 3$. 由 $c ! ! \geq\left(\left\lceil\frac{c}{2}\right\rceil\right) !$ 知 $a>\left\lceil\frac{c}{2}\right\rceil$, 即 $a \geq\left\lceil\frac{c}{2}\right\rceil+1$.

先考虑 $b, c$ 都是偶数的情况. 如果 $c \geq b+6$, 那么 $\frac{c ! !}{b ! !}$ 是 $(b+2)(b+4)(b+6)$的倍数, 即是 3 的倍数, 故 $\nu_{3}(c ! !)>\nu_{3}(b ! !)$, 因此 $\nu_{3}(a !)=\nu_{3}(b ! !)=\nu_{3}\left(\left(\frac{b}{2}\right) !\right)$, 这说明 $a \leq \frac{b}{2}+2$, 但这与 $a \geq \frac{c}{2}+1$ 以及 $c \geq b+6$ 矛盾. 故 $c \in\{b, b+2, b+4\}$.

注意 $\nu_{2}(a !) \geq \nu_{2}(b ! !)=\nu_{2}(b !)$, 故 $a \geq b$, 这说明 $b ! \leq b ! !+(b+4) ! !$, 即 $(b-1) ! ! \leq 1+(b+2)(b+4)$. 当 $b \geq 10$ 时 $(b-1) ! ! \geq 5(b-3)(b-1)>(b+4)(b+2)+1$矛盾. 故只能是 $b \in\{2,4,6,8\}$, 经检验此时无解.

下面考虑 $b, c$ 都是奇数的情况. 如果 $\nu_{3}(b ! !)=\nu_{3}(c !$ ! , 那么 $c \leq b+4$, 且当 $c=b+4$ 时有 $3 \mid b$, 故

$$
\begin{aligned}
r & =\left\lfloor\frac{c+3}{4}\right\rfloor \leq\left\lfloor\frac{a}{2}\right\rfloor \leq \nu_{2}(a !)=\nu_{2}(b ! !+c ! !) \\
& =\nu_{2}\left(1+\frac{c ! !}{b ! !}\right) \leq \max \left\{\log _{2} \frac{(c-1)^{2}}{9}, \log _{2}(c+1)\right\}
\end{aligned}
$$

即 $2^{r} \leq \max \left\{\frac{(c-1)^{2}}{9}, c+1\right\}$, 可知 $r \leq 5$, 故 $c \leq 19$. 逐一检验得仅有 $(5,5,7)$.

下面假设 $\nu_{3}(b ! !)<\nu_{3}(c ! !)$, 此时 $\nu_{3}(a !)=\nu_{3}(b ! !)$. 注意

$$
\begin{aligned}
& b ! !=\frac{(b+1) !}{(b+1) ! !}=\frac{1}{2^{\frac{b+1}{2}}} \times\left(\frac{b+1}{2}\right) ! \times\left(\begin{array}{c}
b+1 \\
\frac{b+1}{2}
\end{array}\right) . \\
& \nu_{3}(a !)=\nu_{3}(b ! !)=\nu_{3}\left(\left(\frac{b+1}{2}\right) !\right)+\nu_{3}\left(\left(\begin{array}{c}
b+1 \\
\frac{b+1}{2}
\end{array}\right)\right) \leq \nu_{3}\left(\left(\frac{b+1}{2}\right) !\right)+\log _{3}(b+1) .
\end{aligned}
$$

这说明

$$
a \leq \frac{b+1}{2}+3 \log _{3}(b+1)+2 .
$$

又因为 $\nu_{2}\left(1+\frac{c ! !}{b ! !}\right)=\nu_{2}(a !) \geq a-\log _{2}(a+1)$, 故 $\frac{c ! !}{b !} \geq \frac{2^{a}}{a+1}-1$, 因此

$$
a !=b ! !+c ! ! \geq \frac{2^{a}}{a+1} \times b ! !, \quad \Rightarrow b ! ! \leq \frac{(a+1) !}{2^{a}}
$$

由于 $a \leq \frac{b+1}{2}+3 \log _{3}(b+1)+2$, 故 $a ! \leq\left(\frac{b+1}{2}\right) ! \times a^{3 \log _{3}(b+1)+2}$, 而

$$
b ! !=\frac{1}{2^{\frac{b+1}{2}}} \times\left(\frac{b+1}{2}\right) ! \times\left(\begin{array}{c}
b+1 \\
\frac{b+1}{2}
\end{array}\right)>\frac{2^{\frac{b+1}{2}}}{b+2} \times\left(\frac{b+1}{2}\right) ! .
$$

故

$$
\frac{2^{\frac{b+1}{2}}}{b+2} \leq \frac{a^{3 \log _{3}(b+1)+2}}{2^{a}} \Rightarrow \frac{b+1}{2}+a \leq \log _{2}(b+2)+\left(3 \log _{3}(b+1)+2\right) \log _{2} a
$$

注意 $c<2 a$, 故 $b \leq 2 a-3$. 因此 $a \leq \log _{2}(2 a)+3 \log _{3}(2 a) \log _{2} a+2 \log _{2} a$.

设 $d=\log _{2} a$, 则 $2^{d} \leq 3 \log _{3} 2 d^{2}+\left(3+\log _{3} 2\right) d+1<2 d^{2}+5 d+1$. 而当 $d \geq 8$ 时有 $2^{d}=2^{\frac{d}{2}} \times 2^{\frac{d}{2}} \geq\left(\frac{d}{2}\right)^{2} \times 16=4 d^{2}>2 d^{2}+5 d+1$, 矛盾.

故 $d \leq 8$, 因此 $a<256$, 由 $c<2 a$ 知 $b<c<512$, 故 $a+b+c<2022$.

