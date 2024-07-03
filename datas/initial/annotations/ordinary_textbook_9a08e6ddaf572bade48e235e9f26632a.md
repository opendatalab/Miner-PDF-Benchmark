# 第三十九期问题征解解答与点评 

## 张端阳

第一题 求所有的正整数 $n$, 使得对任意 $n$ 次首一实系数多项式 $P$, 只要 $P^{(2)}$ 有 $n^{2}$ 个不同的非正实根, 就有对每个正整数 $m, P^{(m)}$ 有 $n^{m}$ 个不同的实根.这里 $P^{(m)}$ 表示 $P$ 的 $m$ 次迭代.

(北京大学学生 杨泓暕 供题)

## 解 (根据供题者的解答整理):

所求为 1 及全体正偶数.

先证明对这些 $n$ 结论成立.

$n=1$ 时显然, 下设 $n$ 为正偶数.

因为 $P^{(2)}$ 有 $n^{2}$ 个不同的实根, 故 $P$ 有 $n$ 个不同的实根 $x_{1}<x_{2}<\cdots<x_{n}$,且 $P(x)=x_{k}(k=1,2, \cdots, n)$ 各有 $n$ 个不同的实根. 由 $P$ 首一知 $P$ 在 $\left(x_{n},+\infty\right)$上单调递增, 且 $P(x) \rightarrow+\infty(x \rightarrow+\infty)$.

若 $x_{n}>0$, 由介值定理, $P(x)=x_{n}$ 在 $\left(x_{n},+\infty\right)$ 上有一实根, 与 $P^{(2)}$ 的实根皆非正矛盾. 因此 $x_{n} \leq 0$, 进而 $P$ 的实根皆非正.

设 $P$ 在区间 $I_{k}=\left[x_{2 k-1}, x_{2 k}\right]$ 上的最小值为 $m_{k}<0\left(k=1,2, \cdots, \frac{n}{2}\right)$, 记 $M=\max \left\{m_{1}, m_{2}, \cdots, m_{\frac{n}{2}}\right\}$. 对 $y_{0} \in(M, 0]$, 由介值定理及函数单调性, 知 $P(x)=y_{0}$ 在每个 $I_{k}$ 上恰有两个不同的实根, 从而共有 $n$ 个不同的实根. 另一方面, 若 $P(x)=y_{0}$ 有 $n$ 个不同的实根, 则 $y_{0}>M$. 取 $y_{0}=x_{k}(k=1,2, \cdots, n)$, 知 $P$ 的实根皆在 $(M, 0]$ 中.

下面对 $m$ 归纳证明 $P^{(m)}$ 在 $(M, 0]$ 中有 $n^{m}$ 个不同的实根.

当 $m=1$ 时,上面已证. 假设 $m$ 时成立, 来看 $m+1$ 时的情形.

由归纳假设, $P^{(m)}(x)=0$ 有 $n^{m}$ 个实根 $M<y_{1}<y_{2}<\cdots<y_{n^{m}} \leq 0$. 由上述分析知 $P(x)=y_{k}\left(k=1,2, \cdots, n^{m}\right)$ 各有 $n$ 个不同的实根, 且这些根皆在 $\left(x_{1}, 0\right] \subseteq(M, 0]$ 中. 而对不同的 $k$, 这些实根显然互不相同, 故合并起来便给出 $(M, 0]$ 中 $n^{m+1}$ 个不同的实根.
归纳证毕.

下设 $n>1$ 为奇数, 来构造反例.

设 $P(x)=(x+t)(x+2 t) \cdots(x+n t)$, 我们说明可以选取 $t>0$ 符合要求.

设 $P$ 在区间 $[-2 k t,-(2 k-1) t]$ 上的最小值为 $m_{k}(t)<0\left(k=1,2, \cdots, \frac{n-1}{2}\right)$,记 $M(t)=\max \left\{m_{1}, m_{2}, \cdots, m_{\frac{n-1}{2}}\right\}$.

设 $g(t)=M(t)+n t$, 则由诸 $m_{k}$ 连续知 $g$ 亦连续.

因为对任意 $-1 \leq x \leq 0,\left(x+\frac{1}{n}\right)\left(x+\frac{2}{n}\right) \cdots(x+1)>-1$, 所以 $g\left(\frac{1}{n}\right)>0$.

另一方面, 对 $k=1,2, \cdots, \frac{n-1}{2}, P\left(-\left(2 k-\frac{1}{2}\right) t\right)$ 是关于 $t$ 的 $n>1$ 次多项式,且由 $n$ 是奇数知最高次项系数为负. 于是在 $t$ 充分大时, 对每个 $k$,

$$
m_{k}(t)+n t \leq P\left(-\left(2 k-\frac{1}{2}\right) t\right)+n t<0
$$

故在 $t$ 充分大时 $g(t)<0$.

由介值定理, $g$ 存在正的零点. 我们可以取 $g$ 的零点中的最大者 (这是因为闭集 $\{0\}$ 的原像仍闭, 且 $g$ 的零点有上界), 记为 $t_{0}$, 那么当 $t>t_{0}$ 时便有 $g(t)<0$.

设 $Q(x)=P(x)-x$, 由于 $n>1$ 且 $n$ 是奇数, $Q$ 在 $(-\infty,-n t)$ 上恰有一个实根, 记为 $x_{0}=x_{0}(t)$. 设 $h(t)=M(t)-x_{0}(t)$, 则 $h$ 连续, 且

$$
h\left(t_{0}\right)=M\left(t_{0}\right)-x_{0}\left(t_{0}\right)=-n t_{0}-P\left(t_{0}\right)>0 .
$$

故存在 $t_{1}>t_{0}$ 使得 $h\left(t_{1}\right)>0$, 我们证明取 $t=t_{1}$ 即满足要求.

由函数的单调性及 $M\left(t_{1}\right)<-n t_{1}$, 模仿证明部分的分析知 $P(x)=-k t_{1}$ 有 $n$ 个不同的非正实根 $(k=1,2, \cdots, n)$, 故 $P^{(2)}$ 的确有 $n^{2}$ 个不同的非正实根.

另一方面, 我们归纳定义数列 $\left\{a_{m}\right\}$ 如下: $a_{1}=-n t_{1}$, 对 $m>1, a_{m}$ 定义为 $P(x)=a_{m-1}$ 的最小实根（特别地, $a_{m}$ 为 $P^{(m)}$ 的实根）.由 $n$ 是奇数知定义良好.

通过归纳法不难证明 $a_{m-1}>a_{m}>x_{0}\left(t_{1}\right)$, 因此 $\left\{a_{m}\right\}$ 为单调递减的有界数列, 故其极限存在, 设为 $L$. 在 $P\left(a_{m}\right)=a_{m-1}$ 两边同时取极限知 $P(L)=L$, 结合 $L<a_{1}=-n t_{1}$ 及 $x_{0}$ 的取法可知 $L=x_{0}\left(t_{1}\right)$. 由 $t_{1}$ 的取法知 $x_{0}\left(t_{1}\right)<M\left(t_{1}\right)<-n t_{1}$, 故存在正整数 $N$, 使得 $a_{N}<M\left(t_{1}\right)$. 再次模仿证明部分的分析知 $P(x)=a_{N}$ 没有 $n$ 个不同的实根, 因此 $P$ 的确是我们需要的反例.

评注 (1). 本题的过程很长, 但核心思想是简单的: 条件决定了 $P$ 的零点分布和单调性, 因而迭代中的根是否齐全只与根的分布范围相关, 由此不难猜到答案并给出证明. 另一方面, 构造部分有一定难度, 除构造的感觉外, 还要求较
高的定性分析功底.

(2). 人大附中郑云兮同学指出, 当 $n$ 是奇数时, 可以选取恰当的实数 $s, t$,使得对于

$$
P(x)=(x+s+t)(x+s+2 t) \cdots(x+s+n t),
$$

$P^{(2)}$ 有 $n^{2}$ 个不同的非正实根, 而 $P^{(3)}$ 的不同实根少于 $n^{3}$ 个.

第二题 设 $\triangle A B C$ 的外接圆为 $\Omega$, 内切圆为 $\omega, \omega$ 与 $B C, C A, A B$ 分别切于点 $D, E, F$. 延长 $E F$ 交 $\Omega$ 于点 $P$, 直线 $P D$ 分别与 $\omega, \Omega$ 交于点 $G, Q$. 设 $\Omega$ 在 $B, C$ 处的切线交于点 $T$. 证明: (1) $T G$ 是 $\omega$ 的切线; (2) $\frac{P Q}{D G}=\frac{R+r}{r}$, 其中 $R, r$ 分别是 $\Omega, \omega$ 的半径.

(法国再保险公司北京分公司 陈舜 华东师范大学 罗振华 供题)

## 证明 (根据南昌市第二中学李嘉睿、于沣林同学的解答整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_2094a9e20f8f810a556cg-3.jpg?height=954&width=556&top_left_y=1188&top_left_x=750)

(1) 设 $\omega$ 在 $G$ 处的切线与直线 $A B, A C$ 分别交于点 $J, H$.

设 $K$ 是 $D F$ 与 $E G$ 的交点, 则 $H, P, B$ 都在 $K$ 关于 $\omega$ 的极线上, 因此它们共线.

同理, $J, P, C$ 共线.

对圆内接六边形 $B B P C C A$ 用帕斯卡定理得, $H, J, T$ 共线, 从而 $T G$ 是 $\omega$的切线.

(2) 记 $\angle P D B=\theta$, 则

$$
\angle D P E=\angle P D B+\angle F B D-\angle B F P=\theta+B-\left(90^{\circ}-\frac{A}{2}\right)=\theta+\frac{B-C}{2} .
$$

在 $\triangle P D E$ 中,

$$
P D=D E \cdot \frac{\sin \angle P E D}{\sin \angle D P E}=2 r \cos \frac{C}{2} \cdot \frac{\sin \left(90^{\circ}-\frac{B}{2}\right)}{\sin \left(\theta+\frac{B-C}{2}\right)}=\frac{2 r \cos \frac{B}{2} \cos \frac{C}{2}}{\sin \left(\theta+\frac{B-C}{2}\right)} .
$$

于是

$$
\begin{aligned}
& D Q=\frac{B D \cdot D C}{P D}=\frac{r \cot \frac{B}{2} \cdot r \cot \frac{C}{2}}{\frac{2 r \cos \frac{B}{2} \cos \frac{C}{2}}{\sin \left(\theta+\frac{B-C}{2}\right)}}=\frac{r \sin \left(\theta+\frac{B-C}{2}\right)}{2 \sin \frac{B}{2} \sin \frac{C}{2}} \\
& =2 R \sin \frac{A}{2} \sin \left(\theta+\frac{B-C}{2}\right) .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_2094a9e20f8f810a556cg-4.jpg?height=583&width=580&top_left_y=1002&top_left_x=744)

设 $I$ 是 $\triangle A B C$ 的内心, 延长 $A I$ 交 $\Omega$ 于点 $M$, 过 $M$ 作 $P Q$ 的平行线交 $\Omega$于点 $X$, 作 $I Y \perp X M$ 于 $Y$.

因为

$$
\begin{aligned}
Y M & =I M \cos \angle A M X=2 R \sin \frac{A}{2} \cos \left(C+\frac{A}{2}-\theta\right) \\
& =2 R \sin \frac{A}{2} \sin \left(\theta+\frac{B-C}{2}\right)=D Q
\end{aligned}
$$

所以四边形 $D Y M Q$ 是平行四边形, 于是 $D Y=Q M$. 又 $P X=Q M$, 且由 $I Y$垂直平分线段 $G D$, 知 $G Y=D Y$, 所以 $P X=G Y$. 于是四边形 $P X Y G$ 是平行四边形, 从而 $P G=X Y$.

这样,

$$
P G+D Q=X Y+Y M=X M=2 R \sin \theta
$$

又 $D G=2 r \sin \theta$, 所以

$$
\frac{P Q}{D G}=\frac{P G+D G+D Q}{D G}=\frac{2 R \sin \theta+2 r \sin \theta}{2 r \sin \theta}=\frac{R+r}{r}
$$

评注 (1). 北京师范大学附属实验中学张晟宁等同学也给出了本题的正确解答.

(2). 点 $P$ 的其他性质在第八期征解第三题和第 60 届 IMO 预选题 G6 中有所涉及.

第三题 求最大的实数 $\lambda$, 使得对任意正整数 $n$ 和正实数 $x_{1}, x_{2}, \cdots, x_{n}$, 都有

$$
\left(\sum_{i=1}^{n} x_{i}^{2}\right)\left(\sum_{i=1}^{n} \sum_{j=1}^{n} \max \{i, j\} x_{i} x_{j}\right) \geq \lambda\left(\sum_{i=1}^{n} x_{i}\right)^{4}
$$

(人大附中学生 邹明轩 供题)

## 证明 (根据供题者的解答整理):

由齐次性, 不妨设 $\sum_{i=1}^{n} x_{i}=1$. 注意到

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n} \max \{i, j\} x_{i} x_{j} & =\sum_{i=1}^{n} i x_{i}^{2}+2 \sum_{1 \leq j<i \leq n} i x_{i} x_{j} \\
& =n\left(\sum_{i=1}^{n} x_{i}\right)^{2}-\sum_{i=1}^{n}\left(\sum_{j=1}^{i-1} x_{j}\right)^{2} \\
& =\sum_{i=1}^{n}\left(1-\left(x_{1}+x_{2}+\cdots+x_{i-1}\right)^{2}\right) .
\end{aligned}
$$

于是由柯西不等式,

$$
\begin{aligned}
& \left(\sum_{i=1}^{n} x_{i}^{2}\right)\left(\sum_{i=1}^{n} \sum_{j=1}^{n} \max \{i, j\} x_{i} x_{j}\right) \\
= & \left(\sum_{i=1}^{n} x_{i}^{2}\right)\left(\sum_{i=1}^{n}\left(1-\left(x_{1}+x_{2}+\cdots+x_{i-1}\right)^{2}\right)\right) \\
\geq & \left(\sum_{i=1}^{n} x_{i} \sqrt{1-\left(x_{1}+x_{2}+\cdots+x_{i-1}\right)^{2}}\right)^{2} .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_2094a9e20f8f810a556cg-5.jpg?height=456&width=440&top_left_y=2162&top_left_x=814)
如图, 构造半径为 1 的四分之一圆以及 $n$ 个矩形. 其中对 $1 \leq i \leq n$, 第 $i$ 个矩形的宽为 $x_{i}$, 高为 $\sqrt{1-\left(x_{1}+x_{2}+\cdots+x_{i-1}\right)^{2}}$, 则

$$
\sum_{i=1}^{n} x_{i} \sqrt{1-\left(x_{1}+x_{2}+\cdots+x_{i-1}\right)^{2}}
$$

即为 $n$ 个矩形的面积之和. 由图知, $n$ 个矩形的面积之和不小于四分之一圆的面积 $\frac{\pi}{4}$, 故

$$
\left(\sum_{i=1}^{n} x_{i}^{2}\right)\left(\sum_{i=1}^{n} \sum_{j=1}^{n} \max \{i, j\} x_{i} x_{j}\right) \geq\left(\frac{\pi}{4}\right)^{2}=\frac{\pi^{2}}{16}
$$

即当 $\lambda=\frac{\pi^{2}}{16}$ 时不等式成立.

另一方面, 对 $1 \leq i \leq n$, 取 $x_{i}=\cos \frac{i \pi}{2 n}$. (可将 $x_{n}$ 加上一个充分小的正实数以使之为正实数, 为了叙述方便, 统一写成余弦的形式, 不影响结果)

当 $n \rightarrow \infty$ 时,

$$
\begin{aligned}
\frac{1}{n} \sum_{i=1}^{n} x_{i} & =\frac{1}{n} \sum_{i=1}^{n} \cos \frac{i \pi}{2 n} \rightarrow \frac{2}{\pi} \int_{0}^{\frac{\pi}{2}} \cos x \mathrm{~d} x=\frac{2}{\pi}, \\
\frac{1}{n} \sum_{i=1}^{n} x_{i}^{2} & =\frac{1}{n} \sum_{i=1}^{n} \cos ^{2} \frac{i \pi}{2 n}=\frac{1}{2 n}\left(n+\sum_{i=1}^{n} \cos \frac{i \pi}{n}\right) \\
& \rightarrow \frac{1}{2}+\frac{1}{2 \pi} \int_{0}^{\pi} \cos x \mathrm{~d} x=\frac{1}{2} .
\end{aligned}
$$

又

$$
\sum_{j=1}^{i-1} x_{j}=\sum_{j=1}^{i-1} \cos \frac{j \pi}{2 n}=\frac{1}{2}\left(\frac{\sin \frac{(2 i-1) \pi}{4 n}}{\sin \frac{\pi}{4 n}}-1\right)
$$

所以

$$
\begin{aligned}
\sum_{i=1}^{n}\left(\sum_{j=1}^{i-1} x_{j}\right)^{2} & =\frac{1}{4}\left(\frac{1}{\sin ^{2} \frac{\pi}{4 n}} \sum_{i=1}^{n} \sin ^{2} \frac{(2 i-1) \pi}{4 n}-\frac{2}{\sin \frac{\pi}{4 n}} \sum_{i=1}^{n} \sin \frac{(2 i-1) \pi}{4 n}+n\right) \\
& =\frac{1}{4}\left(\frac{n}{2 \sin ^{2} \frac{\pi}{4 n}}-\frac{1}{\sin ^{2} \frac{\pi}{4 n}}+n\right) .
\end{aligned}
$$

于是当 $n \rightarrow \infty$ 时,

$$
\begin{aligned}
& \frac{1}{n^{3}} \sum_{i=1}^{n} \sum_{j=1}^{n} \max \{i, j\} x_{i} x_{j} \\
= & \left(\frac{1}{n} \sum_{i=1}^{n} x_{i}\right)^{2}-\frac{1}{n^{3}} \sum_{i=1}^{n}\left(\sum_{j=1}^{i-1} x_{j}\right)^{2} \\
\rightarrow & \left(\frac{2}{\pi}\right)^{2}-\frac{1}{4} \cdot \frac{1}{2\left(\frac{\pi}{4}\right)^{2}}=\frac{2}{\pi^{2}} .
\end{aligned}
$$

故在

$$
\left(\frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}\right)\left(\frac{1}{n^{3}} \sum_{i=1}^{n} \sum_{j=1}^{n} \max \{i, j\} x_{i} x_{j}\right) \geq \lambda\left(\frac{1}{n} \sum_{i=1}^{n} x_{i}\right)^{4}
$$

两边同时令 $n \rightarrow \infty$ 得，

$$
\frac{1}{2} \cdot \frac{2}{\pi^{2}} \geq \lambda\left(\frac{2}{\pi}\right)^{4}
$$

解得 $\lambda \leq \frac{\pi^{2}}{16}$.

综上, 所求最大值为 $\frac{\pi^{2}}{16}$.

评注 杭州学军中学周箴言、北京师范大学附属实验中学张茂宁等同学给出了本题正确的证明, 但构造不正确.

第四题 对正整数集的非空有限子集 $I$, 用 $l(I)$ 表示 $I$ 中所有元素的最小公倍数. 设 $n$ 是大于 1 的整数, $k$ 是不超过 $n$ 的素数的个数. 设 $A$ 是 $\{2,3, \cdots, n\}$的非空子集, 记 $B=\left\{l(I) \mid I \subseteq A, I \neq \emptyset, l(I) \leq n^{2}\right\}$. 求证：存在 $C \subseteq B$, 使得 $|C| \geq \frac{2}{k+1}|B|$, 且 $C$ 中元素两两不互素.

(华东师范大学第二附属中学学生 王一川 供题)

## 证明 (根据人大附中陈锐軞同学的解答整理):

设不超过 $n$ 的 $k$ 个素数为 $p_{1}, p_{2}, \cdots, p_{k}$.

对 $1 \leq i \leq k$, 定义集合

$$
C_{i}=\left\{b \in B\left|p_{i}\right| b\right\}, \quad D_{i}=\left\{b \in B \mid b \text { 是 } p_{i} \text { 的幂 }\right\} .
$$

显然 $C_{i}$ 中元素两两不互素, 记 $\left|D_{i}\right|=d_{i}$.

一方面, 证明 $\max _{1 \leq i \leq k}\left|C_{i}\right| \geq d_{1}+d_{2}+\cdots+d_{k}$.

若 $d_{1}=d_{2}=\cdots=d_{k}=0$, 结论显然成立.

若存在 $i$ 使 $d_{i} \neq 0$, 不妨 $d_{1} \neq 0$, 我们证明 $\left|C_{1}\right| \geq d_{1}+d_{2}+\cdots+d_{k}$.

事实上, 此时 $A$ 中存在 $p_{1}$ 的幂, 设为 $p_{1}^{\alpha}$.

对任意 $d \in D_{i}, i>1$, 设 $l(I)=d$, 则 $d \in I$, 进而 $d \in A$, 特别地 $d \leq n$. 因为

$$
l\left(\left\{d, p_{1}^{\alpha}\right\}\right)=p_{1}^{\alpha} d \leq n^{2},
$$

所以 $p_{1}^{\alpha} d \in C_{1}$, 故

$$
\left\{p_{1}^{\alpha} d \mid d \in D_{i}, i>1\right\} \subseteq C_{1} .
$$

又显然 $D_{1} \subseteq C_{1}$, 所以 $\left|C_{1}\right| \geq d_{1}+d_{2}+\cdots+d_{k}$.
另一方面, 考虑 $\left|C_{1}\right|+\left|C_{2}\right|+\cdots+\left|C_{k}\right|$.

计算每个 $b \in B$ 的贡献, 即 $b$ 属于多少个 $C_{i}$, 这恰为 $b$ 的素因子个数. 因此当 $b \in D_{1} \cup D_{2} \cup \cdots \cup D_{k}$ 时贡献为 1 , 否则贡献至少为 2 . 故

$$
k \max _{1 \leq i \leq k}\left|C_{i}\right| \geq\left|C_{1}\right|+\left|C_{2}\right|+\cdots+\left|C_{k}\right| \geq 2|B|-\left(d_{1}+d_{2}+\cdots+d_{k}\right) .
$$

综合两方面, $\max _{1 \leq i \leq k}\left|C_{i}\right| \geq \frac{2}{k+1}|B|$, 命题得证.

