# 数学新星问题征解第四期解答 

2014.9

第一题: 设 $k \geq 2$ 是一个整数, $a, b$ 是实数. 证明: 当且仅当 $a-b$ 是整数且 $k \mid a-b$ 时, 对任意的正整数 $n$ 有

$$
\lfloor a n\rfloor \equiv\lfloor b n\rfloor \quad(\bmod k) .
$$

(郑州外国语学校学生 朱书聪 供题)

## 证明 (根据饶正昊同学的解答整理):

先证充分性:

设 $a-b=k d(d \in \mathbf{Z})$, 则对任意的正整数 $n$ 有

$$
\lfloor a n\rfloor=\lfloor(b+k d) n\rfloor=\lfloor b n\rfloor+k d n \equiv\lfloor b n\rfloor \quad(\bmod k) .
$$

再证必要性:

设对任意的正整数 $n$ 有

$$
\lfloor a n\rfloor \equiv\lfloor b n\rfloor(\bmod k) .
$$

记 $\alpha=a-\lfloor a\rfloor, \beta=b-\lfloor b\rfloor$, 不妨设 $0 \leq \alpha \leq \beta<1$, 则对任意的正整数 $n$ 有

$$
\lfloor n a\rfloor=\lfloor n \alpha\rfloor+n\lfloor a\rfloor,\lfloor n b\rfloor=\lfloor n \beta\rfloor+n\lfloor b\rfloor .
$$

令 $n=1$ 可得

$$
\lfloor a\rfloor \equiv\lfloor b\rfloor \quad(\bmod k)
$$

由 (1), (2) 和 (3) 可得对任意的正整数 $n$ 有

$$
\lfloor n \alpha\rfloor \equiv\lfloor n \beta\rfloor \quad(\bmod k)
$$

若 $\alpha \neq \beta$, 不妨设 $\beta>\alpha$, 考虑函数 $f(n)=\lfloor n \beta\rfloor-\lfloor n \alpha\rfloor(n \in \mathbf{N})$. 因为

$$
\begin{aligned}
& 0 \leq\lfloor(n+1) \beta\rfloor-\lfloor n \beta\rfloor \leq\lfloor n \beta\rfloor+1=1, \\
& 0 \leq\lfloor(n+1) \alpha\rfloor-\lfloor n \alpha\rfloor \leq\lfloor n \alpha\rfloor+1=1,
\end{aligned}
$$

及

$$
\begin{aligned}
f(n+1)-f(n) & =(\lfloor(n+1) \beta\rfloor-\lfloor(n+1) \alpha\rfloor)-(\lfloor n \beta\rfloor-\lfloor n \alpha\rfloor) \\
& =(\lfloor(n+1) \beta\rfloor-\lfloor n \beta\rfloor)-(\lfloor(n+1) \alpha\rfloor-\lfloor n \alpha\rfloor),
\end{aligned}
$$

故

$$
f(n+1)-f(n) \in\{-1,0,1\}
$$

注意到 $f(0)=0$, 且当 $n>\frac{2}{\beta-\alpha}$ 时

$$
\begin{aligned}
f(n) & =\lfloor n \beta\rfloor-\lfloor n \alpha\rfloor \\
& >n \beta-n \alpha-1 \\
& >\frac{2}{\beta-\alpha} \cdot(\beta-\alpha)-1=1 .
\end{aligned}
$$

故由 (5) 和 (6) 便知必存在 $n_{0} \in \mathbf{N}^{*}$ 使得 $f\left(n_{0}\right)=1$.

在 (1) 中令 $n=n_{0}$ 可得

$$
0 \equiv\left\lfloor n_{0} \beta\right\rfloor-\left\lfloor n_{0} \alpha\right\rfloor=f\left(n_{0}\right)=1 \quad(\bmod k)
$$

这与 $k \geq 2$ 矛盾! 因此 $\alpha=\beta$. 故

$$
a-b=\lfloor a\rfloor-\lfloor b\rfloor \equiv 0 \quad(\bmod k),
$$

即 $a-b \in \mathbf{Z}$ 且 $k \mid a-b$.

必要性得证.

综上所述, 结论成立.

第二题: 设 $\Omega$ 为 $\triangle A B C$ 的外接圆, $I$ 为内心. $B I$ 交 $A C$ 于 $B_{1}, C I$ 交 $A B$ 于 $C_{1}, B_{1} C_{1}$ 的延长线交 $\Omega$ 于 $K . B I$ 的中点为 $B_{2}, C I$ 的中点为 $C_{2}$, $B_{2} C_{2}$ 的延长线交 $\Omega$ 于 $M$. 证明: $K, I, M$ 三点共线.

(上海中学学生 高继扬, 华东师大二附中学生 俞辰捷 供题)

## 证明一 (根据朱书聪同学的解答整理):

设 $C_{2} B_{2}, C_{1} B_{1}, B I, M I, C I, N I$ 的延长线分别交 $\Omega$ 于点 $N, L, B^{\prime}, K^{\prime}, C^{\prime}, L^{\prime}$, $X, Y$ 分别为 $I B$ 和 $I C$ 延长线上的点, 且使得 $I B^{\prime}=B X, I C^{\prime}=C Y$.
由 $I B^{\prime}=B X$ 知 $B_{2} B^{\prime}=B_{2} X$, 则由圆幂定理可得

$$
M B_{2} \cdot N B_{2}=B B_{2} \cdot B^{\prime} B_{2}=I B_{2} \cdot X B_{2},
$$

故 $M, I, N, X$ 四点共圆.

同理可得 $M, I, N, Y$ 四点共圆. 故 $M, I, N, X, Y$ 共圆.

因为

$$
\angle B^{\prime} A B_{1}=\angle B^{\prime} B C=\angle B^{\prime} B A,
$$

则

$$
\triangle B^{\prime} A B_{1} \sim \triangle B^{\prime} B A .
$$

又因为

$$
\angle B^{\prime} A I=\angle B^{\prime} A B_{1}+\angle C A I=\angle B^{\prime} B A+\angle B A I=\angle B^{\prime} I A,
$$

故

$$
B^{\prime} I=B^{\prime} A \text {. }
$$

因此

$$
B^{\prime} I^{2}=B^{\prime} A^{2}=B^{\prime} B_{1} \cdot B^{\prime} B .
$$

则由

$$
\frac{B^{\prime} I}{B^{\prime} B_{1}}=\frac{B^{\prime} B}{B^{\prime} I}=\frac{I X}{B X}
$$

可得

$$
\frac{B^{\prime} I}{I B_{1}}=\frac{I X}{I B}
$$

故

$$
I B_{1} \cdot I X=B^{\prime} I \cdot I B=K^{\prime} I \cdot I M
$$

从而 $K^{\prime}, M, X, B_{1}$ 四点共圆.

同理可得 $L^{\prime}, N, Y, C_{1}$ 四点共圆.

于是

$$
\angle M K^{\prime} B_{1}=\angle M X I=\angle M N I=\angle M K^{\prime} L^{\prime},
$$

故 $B_{1}$ 在 $K^{\prime} L^{\prime}$ 上. 同理可得 $C_{1}$ 也在 $K^{\prime} L^{\prime}$ 上. 即 $K^{\prime}, L^{\prime}$ 在 $B_{1}, C_{1}$ 上, 又 $K, L$也在 $B_{1}, C_{1}$ 上, 故 $K^{\prime}$ 与 $K$ 重合, $L^{\prime}$ 与 $L$ 重合. 因此, $K, I, M$ 三点共线.

## 证明二 (根据绕正昊同学的解答整理):

设 $O$ 为 $\Omega$ 的圆心. 延长 $C_{1} B_{1}$ 交 $\Omega$ 于 $L$, 连结 $K I, L I$ 并延长分别交 $\Omega$于 $M^{\prime}, N$, 延长 $A I, B I, C I$ 分别交 $\Omega$ 于 $D, E, F$.

对 $\Omega$ 上任意不同的两点 $X, Y$, 记 $\widehat{X Y}=\sin \frac{1}{2} \angle X O Y$.

由于 $A C, K L, B E$ 交于一点 $B_{1}$, 根据角元形式的塞瓦定理可得

$$
\frac{\widehat{A E}}{\widehat{E L}} \cdot \frac{\widehat{L C}}{\widehat{C B}} \cdot \frac{\widehat{B K}}{\widehat{K A}}=1
$$

由于 $A D, B E, M^{\prime} K$ 交于一点 $I$, 故

$$
\frac{\widehat{A K}}{\widehat{K B}} \cdot \frac{\widehat{B D}}{\widehat{D M^{\prime}}} \cdot \frac{\widehat{M^{\prime} E}}{\widehat{E A}}=1
$$

$(1) \times(2)$ 可得

$$
\frac{\widehat{L C}}{\widehat{E L}} \cdot \frac{\widehat{M^{\prime} E}}{\widehat{D M^{\prime}}} \cdot \frac{\widehat{B D}}{\widehat{B C}}=1
$$

又因为 $C F, B E, L N$ 交于一点 $I$, 故

$$
\frac{\widehat{L E}}{\widehat{E F}} \cdot \frac{\widehat{F N}}{\widehat{N B}} \cdot \frac{\widehat{B C}}{\widehat{C L}}=1
$$

$(3) \times(4)$ 可得

$$
\frac{\widehat{B D}}{\widehat{D M^{\prime}}} \cdot \frac{\widehat{M^{\prime} E}}{\widehat{E F}} \cdot \frac{\widehat{F N}}{\widehat{N B}}=1
$$

由 (5) 及角元形式的塞瓦定理的逆定理可知 $B E, M^{\prime} N, D F$ 交于一点.

因为 $D, F$ 分别为弧 $B C$ 和弧 $B A$ 的中点, 故

$$
D I=D B, F I=F B .
$$

因此, $D F$ 与 $B E$ 交于点 $B_{2}$, 故 $M^{\prime}, B_{2}, N$ 三点共线.

同理可得 $M^{\prime}, C_{2}, N$ 三点共线.

从而 $M^{\prime}, B_{2}, C_{2}, N$ 四点共线. 故 $M, M^{\prime}$ 重合. 再由 $K, I, M^{\prime}$ 三点共线便知 $K, I, M$ 三点共线.
第三题: 设 $n$ 是一个正整数, 证明: 存在无穷整数数列

$$
\cdots, t_{-1}, t_{0}, t_{1}, t_{2}, \cdots, t_{n}, \cdots
$$

使得其中只有 $2^{n}-n$ 项不为 0 , 且对任意连续 $n+2$ 项 $t_{i}, t_{i+1}, t_{i+2}, \cdots, t_{i+n+1}(i \in$ Z) 存在一个次数不超过 $n$ 的多项式 $f(x)$ 使得对 $j=i, i+1, \cdots, i+n+1$有

$$
\left|f(j)-t_{j}\right| \leq \frac{1}{2^{n}}
$$

(上海中学学生 陆一平 供题)

## 证明 (根据陆一平同学的解答整理):

引理 1: 对任意的实数序列 $t_{1}, t_{2}, \cdots, t_{n+2}$, 如果

$$
\sum_{i=1}^{n+2}(-1)^{n+2-i} C_{n+1}^{i-1} t_{i}=0
$$

则存在一个次数不超过 $n$ 的多项式 $f(x)$ 使得对任意的 $i=1,2, \cdots, n+2$都有 $f(i)=t_{i}$.

事实上, 由拉格朗日插值公式可以构造多项式 $f(x)$ 使得对任意的 $i=1,2, \cdots, n+1$ 都有 $f(i)=t_{i}$, 且 $f(x)$ 的次数不超过 $n$. 定义

$$
\Delta f(x)=f(x+1)-f(x), \Delta^{k} f=\Delta\left(\Delta^{k-1} f\right) .
$$

则由 $\Delta^{n+1} f=0$, 可得

$$
\sum_{i=1}^{n+2}(-1)^{n+2-i} C_{n+1}^{i-1} f(i)=0
$$

故

$$
f(n+2)=\sum_{i=1}^{n+1}(-1)^{n+2-i} C_{n+1}^{i-1} f(i)
$$

再由 $f(i)=t_{i}(i=1,2, \cdots, n+1)$ 及

$$
\sum_{i=1}^{n+2}(-1)^{n+2-i} C_{n+1}^{i-1} t_{i}=0
$$

可得 $f(n+2)=t_{n+2}$. 引理 1 得证.
引理 2: 存在恰有 $2^{n}-n$ 个非零项的整数数列 $\cdots, t_{-2}, t_{-1}, t_{0}, t_{1}, t_{2}, \cdots$使得

$$
\left|\sum_{k=0}^{n+1}(-1)^{k} C_{n+1}^{k} t_{i-k}\right| \leq 2 \quad\left(i=0,1, \cdots, 2^{n}\right)
$$

下面证明一个更强的形式: 若整数数列 $\cdots, t_{-1}, t_{0}, t_{1}, t_{2}, \cdots, t_{n}, \cdots$ 中的 $2^{n}-n$ 个非零正整数为 $t_{0}, t_{1}, \cdots, t_{2^{n}-n-1}$, 设

$$
a_{i}=\sum_{k=0}^{n+1}(-1)^{k} C_{n+1}^{k} t_{i-k}(i \in \mathbf{Z})
$$

则当 $i \leq-1$ 或 $i \geq 2^{n}+1$ 时有 $a_{i}=0$, 且数组 $\left(a_{0}, a_{1}, \cdots, a_{2^{n}}\right)$ 具有 $( \pm 1,0, \cdots, 0, \pm 2,0, \cdots, 0, \pm 2, \cdots, \pm 1)$ (除了绝对值为 1 的首末项外其余非零项的绝对值均为 2) 的形式.

对 $n$ 用归纳法.

当 $n=1$ 时, 取 $t_{0}=1$, 其余项全为 0 便可; 当 $n=2$ 时, 取 $t_{0}=t_{1}=1$,其余项全为 0 便可.

假设结论对 $n$ 时成立, 下面考虑 $n+1$ 的情况.

假设 $n$ 时整数数列 $\cdots, t_{-1}, t_{0}, t_{1}, t_{2}, \cdots, t_{n}, \cdots$ 中满足条件的非零正整数项为 $t_{0}, t_{1}, \cdots, t_{2^{n}-n-1}$, 则当 $i \leq-1$ 或 $i \geq 2^{n}+1$ 时有 $a_{i}=0$, 且 $2^{n}+1$元数组 $\left(a_{0}, a_{1}, \cdots, a_{2^{n}}\right)$ 具有 $( \pm 1,0, \cdots, 0, \pm 2,0, \cdots, 0, \pm 2, \cdots, \pm 1)$ (除了绝对值为 1 的首末项外其余非零项的绝对值均为 2) 的形式. 下构造恰有 $2^{n+1}-n-1$ 个非零项的数列 $\left\{t_{j}^{\prime}\right\}$ 使得其对应的满足要求的 $2^{n+1}+1$ 元数组为 $\left(a_{0}, a_{1}, \cdots, a_{2^{n}-1}, a_{2^{n}}-a_{0},-a_{1}, \cdots,-a_{2^{n}}\right)$.

令

$$
t_{i}^{\prime}=\sum_{j=i-\left(2^{n}-1\right)}^{i} t_{j}, a_{i}^{\prime}=\sum_{k=0}^{n+2}(-1)^{k} C_{n+2}^{k} t_{i-k}^{\prime}
$$

则 $\left\{t_{j}^{\prime}\right\}$ 中有 $2^{n+1}-n-1$ 个非零项 $t_{0}^{\prime}, t_{1}^{\prime}, \cdots, t_{2^{n+1}-n-2}^{\prime}$, 且当 $i \leq-1$ 或 $i \geq 2^{n}+1$时, $a_{i}^{\prime}=0$. 又由

$$
\begin{aligned}
a_{i}^{\prime} & =\sum_{k=0}^{n+2}(-1)^{k} C_{n+2}^{k} t_{i-k}^{\prime}=\sum_{k=0}^{n+2}(-1)^{k}\left(C_{n+1}^{k}+C_{n+1}^{k-1}\right) t_{i-k}^{\prime} \\
& =a_{i}-a_{i-1}+a_{i-1}-a_{i-2}+\cdots+a_{i-2^{n}+1}-a_{i-2^{n}} \\
& =a_{i}-a_{i-2^{n}}
\end{aligned}
$$

$$
\left(a_{0}^{\prime}, a_{1}^{\prime}, \cdots, a_{2^{n+1}+1}^{\prime}\right)=\left(a_{0}, a_{1}, \cdots, a_{2^{n}-1}, a_{2^{n}}-a_{0},-a_{1}, \cdots,-a_{2^{n}}\right)
$$

也具有满足要求的形式. 即结论对于 $n+1$ 也成立.

故引理 2 得证.

回到原题. 首先说明引理 2 中归纳构造的 $\left\{t_{j}^{\prime}\right\}$ 满足要求.

对任意的正整数 $k$, 设

$$
\begin{gathered}
a_{k}=\sum_{i=0}^{n+1}(-1)^{n+1-i} C_{n+1}^{i} t_{i+k} \\
t_{k+i}^{\prime}=t_{k+i}-\frac{(-1)^{n+1-i}}{2^{n+1}} a_{k}(i=0,1,2, \cdots, n+1) .
\end{gathered}
$$

由引理 2 知

$$
\left|a_{k}\right|=\left|\sum_{i=0}^{n+1}(-1)^{n+1-i} C_{n+1}^{i} t_{i+k}\right| \leq 2,
$$

故

$$
\left|t_{k+i}^{\prime}-t_{k+i}\right|=\left|\frac{a_{k}}{2^{n+1}}\right| \leq \frac{2}{2^{n+1}}=\frac{1}{2^{n}}
$$

并且

$$
\begin{aligned}
& \sum_{i=0}^{n+1}(-1)^{n+1-i} C_{n+1}^{i} t_{i+k}^{\prime}=\sum_{i=0}^{n+1}(-1)^{n+1-i} C_{n+1}^{i}\left(t_{k+i}-\frac{(-1)^{n+1-i}}{2^{n+1}} a_{k}\right) \\
& =a_{k}-\frac{a_{k}}{2^{n+1}}\left(\sum_{i=0}^{n+1}(-1)^{n+1-i} C_{n+1}^{i}\right)=a_{k}-a_{k}=0 .
\end{aligned}
$$

再由引理 1 可知存在多项式 $f_{k}(x)$ 使得 $f_{k}(i)=t_{i}^{\prime}(i=k, k+1, \cdots, k+n+1)$,且对任意的 $i=k, k+1, \cdots, k+n+1$ 有

$$
\left|f_{k}(i)-t_{i}\right|=\left|t_{i}^{\prime}-t_{i}\right| \leq \frac{1}{2^{n}} .
$$

综上所述, 结论得证.
第四题: 设 $p$ 是一个素数, $4 \mid p-1, a$ 是一个正整数使得 $a<\frac{p}{2}, p \mid a^{2}+1$. 定义数列如下: $x_{0}=p, x_{1}=a$, 对 $n \geq 2$,

$$
x_{n}=\min \left\{m \geq 0 \mid m \equiv x_{n-2} \quad\left(\bmod x_{n-1}\right)\right\}
$$

证明: 存在正整数 $k$ 使得 $p=x_{k}^{2}+x_{k+1}^{2}$.

(湖北武钢三中学生 黄一山 供题)

## 证明 (根据吴东晓同学的解答整理):

对任意的 $\alpha \in \mathbf{Q}^{*}$, 设

$$
\alpha=\left[a_{0}, a_{1}, \cdots, a_{n}\right]=a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\cdots+\frac{1}{a_{n}}}}
$$

为 $\alpha$ 的连分数表示, 其中 $a_{0}, a_{1}, \cdots, a_{n} \in \mathbf{Z}^{*}$. 记 $\frac{P_{k}}{Q_{k}}=\left[a_{0}, a_{1}, \cdots, a_{k}\right](k=$ $0,1, \cdots, n)$, 则 $P_{k}, Q_{k}$ 是关于 $a_{0}, a_{1}, \cdots, a_{k}$ 的整系数多项式.

下面证明

$$
\begin{gathered}
P_{k+1}=P_{k} a_{k+1}+P_{k-1}, Q_{k+1}=Q_{k} a_{k+1}+Q_{k-1} \\
P_{k} Q_{k+1}-P_{k+1} Q_{k}=(-1)^{k+1}
\end{gathered}
$$

对 $k$ 数学归纳.

当 $k=1$ 时, 易验证 (1) 和 (2) 成立.

假设 $k-1(k \geq 2)$ 时, (1) 和 (2) 成立, 则

$$
\begin{aligned}
\frac{P_{k+1}}{Q_{k+1}} & =\left[a_{0}, a_{1}, \cdots, a_{k+1}\right]=\left[a_{0}, \cdots, a_{k-1}, a_{k}+\frac{1}{a_{k+1}}\right] \\
& =\frac{\left(a_{k}+\frac{1}{a_{k+1}}\right) P_{k-1}+P_{k-2}}{\left(a_{k}+\frac{1}{a_{k+1}}\right) Q_{k-1}+Q_{k-2}}=\frac{a_{k+1} P_{k}+P_{k-1}}{a_{k+1} Q_{k}+Q_{k-1}} .
\end{aligned}
$$

故

$$
\begin{gathered}
P_{k+1}=P_{k} a_{k+1}+P_{k-1}, Q_{k+1}=Q_{k} a_{k+1}+Q_{k-1} \\
P_{k} Q_{k+1}-P_{k+1} Q_{k}=P_{k}\left(a_{k+1} Q_{k}+a_{k-1}\right)-\left(a_{k+1} P_{k}+P_{k-1}\right) Q_{k} \\
=-\left(P_{k-1} Q_{k}-P_{k} Q_{k-1}\right)=(-1)^{k+1}
\end{gathered}
$$

即当 $k$ 时, (1) 和 (2) 也成立.
故 (1) 和 (2) 得证.

对任意的 $k=1,2, \cdots, n$, 由 (1) 和 (2) 可得

$$
\begin{gathered}
a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\cdots+\frac{1}{a_{k}+\frac{1}{x}}}}=\frac{P_{k} x+P_{k-1}}{Q_{k} x+Q_{k-1}} \\
\frac{P_{k}}{P_{k-1}}=a_{k}+\frac{P_{k-2}}{P_{k-1}}=a_{k}+\frac{1}{a_{k-1}+\frac{P_{k-3}}{P_{k-2}}}=\cdots=\left[a_{k}, a_{k-1}, \cdots, a_{0}\right] .
\end{gathered}
$$

令 $\frac{p}{a}=\left[a_{0}, a_{1}, \cdots, a_{n}\right]$, 则 $\frac{P_{n}}{Q_{n}}=\frac{p}{a}=\left[a_{0}, a_{1}, \cdots, a_{n}\right]$. 再由 (2) 可得

$$
P_{n-1} a-p Q_{n-1}=(-1)^{n}
$$

故

$$
P_{n-1} a \equiv(-1)^{n} \quad(\bmod p) .
$$

又因为 $a<\frac{p}{2}, p \mid a^{2}+1$, 故

$$
P_{n-1} \equiv a \text { 或 }-a(\bmod p) .
$$

取 $p=P_{n}$, 则由 (4) 可得

$$
\frac{p}{P_{n-1}}=\frac{P_{n}}{P_{n-1}}=\left[a_{n}, a_{n-1}, \cdots, a_{0}\right]>a_{n} \geq 2
$$

故 $2 \leq P_{n-1} \leq \frac{p-1}{2}$, 则必有 $P_{n-1}=a$. 因此 $\frac{p}{a}=\frac{P_{n}}{P_{n-1}}=\left[a_{n}, a_{n-1}, \cdots, a_{0}\right]$, 从而

$$
\frac{p}{a}=\left[a_{n}, a_{n-1}, \cdots, a_{0}\right]=\left[a_{0}, a_{1}, \cdots, a_{n}\right]
$$

故

$$
a_{i}=a_{n-i}, i=0,1, \cdots, n
$$

下用归纳法证明当 $n=2 k+1\left(k \in \mathbf{N}^{*}\right)$ 且 $a_{i}=a_{n-i}(i=0,1, \cdots, n)$ 时,

有

$$
P_{n}=P_{k}^{2}+P_{k-1}^{2}, Q_{n}=P_{k} Q_{k}+P_{k-1} Q_{k-1}
$$

对 $k$ 数学归纳.

当 $k=1$ 时, 易知 (5) 成立.
假设当 $k$ 时, (5) 成立. 设 $\alpha=\left[a, a_{0}, a_{1}, \cdots, a_{2 k+1}, a\right]$, 并设 $\frac{P_{i}}{Q_{i}}=\left[a_{0}, a_{1}, \cdots, a_{i}\right](i=$ $0,1, \cdots, 2 k+1), \frac{P_{i}^{\prime}}{Q_{i}^{\prime}}=\left[a, a_{0}, a_{1}, \cdots, a_{i-1}\right](i=1, \cdots, 2 k+2)$, 且 $\frac{P_{0}^{\prime}}{Q_{0}^{\prime}}=[a], \frac{P_{2 k+3}^{\prime}}{Q_{2 k+3}^{\prime}}=$ $\left[a, a_{0}, a_{1}, \cdots, a_{2 k+1}, a\right]$, 则

$$
\frac{P_{i}^{\prime}}{Q_{i}^{\prime}}=a+\frac{1}{\left[a_{0}, a_{1}, \cdots, a_{i}\right]}=a+\frac{Q_{i-1}}{P_{i-1}}=\frac{a P_{i-1}+Q_{i-1}}{P_{i-1}}(i=1,2, \cdots, 2 k+2) .
$$

再由 (3) 及归纳假设可得

$$
\begin{aligned}
& \frac{P_{2 k+3}^{\prime}}{Q_{2 k+3}^{\prime}}=\frac{P_{2 k+2}^{\prime} a+P_{2 k+1}^{\prime}}{Q_{2 k+2}^{\prime} a+Q_{2 k+1}^{\prime}} \\
& =\frac{a^{2}\left(P_{k}^{2}+P_{k-1}^{2}\right)+a\left(P_{k-1} Q_{k-1}+P_{k} Q_{k}\right)+P_{k-1}^{\prime 2}+P_{k}^{\prime 2}}{a\left(P_{k}^{2}+P_{k-1}^{2}\right)+\left(P_{k-1}^{\prime} Q_{k-1}^{\prime}+P_{k}^{\prime} Q_{k}^{\prime}\right)} \\
& =\frac{P_{k+1}^{\prime 2}+P_{k}^{\prime 2}}{P_{k+1}^{\prime} Q_{k+1}^{\prime}+P_{k}^{\prime} Q_{k}^{\prime}} .
\end{aligned}
$$

从而

$$
P_{2 k+3}^{\prime}=P_{k+1}^{\prime 2}+P_{k}^{\prime 2}, Q_{2 k+3}^{\prime}=P_{k+1}^{\prime} Q_{k+1}^{\prime}+P_{k}^{\prime} Q_{k}^{\prime}
$$

即 (5) 对 $k+1$ 也成立.

故 (5) 得证.

回到原题. 利用 (5) 可得

$$
p=P_{n}=P_{k}^{2}+P_{k-1}^{2}
$$

并且

$$
\begin{gathered}
\frac{x_{0}}{x_{1}}=\frac{p}{a}=\left[a_{0}, a_{1}, \cdots, a_{n}\right] \\
\frac{x_{1}}{x_{2}}=\frac{1}{\frac{x_{0}}{x_{1}}-a_{0}}=\frac{1}{\frac{p}{a}-a_{0}}=\left[a_{1}, \cdots, a_{n}\right]=\left[a_{n-1}, \cdots, a_{1}, a_{0}\right]
\end{gathered}
$$

同理可得

$$
\frac{x_{i}}{x_{i+1}}=\left[a_{n-i}, a_{n-i-1}, \cdots, a_{0}\right]=\frac{P_{n-i}}{P_{n-i-1}}(i=0,1, \ldots, n),
$$

且 $x_{0}=P_{n}=p$, 从而 $x_{i}=P_{n-i}(i=0,1, \ldots, n)$. 故

$$
p=P_{k}^{2}+P_{k-1}^{2}=x_{n-k}^{2}+x_{n-k+1}^{2} .
$$

综上所述, 结论得证.

