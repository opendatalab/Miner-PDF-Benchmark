数学新星网 $*$ 教师专栏

www.nsmath.cn/jszl

# 类三角级数的最佳系数问题 

赵斌

(海亮高级中学, 311800)

本文主要解决以下两个关于三角级数的最佳系数问题.

问题 1 给定正整数 $n, k, n \geq k$, 已知 $A_{1}, A_{2}, \cdots, A_{n}$ 为实数, 对任意实数 $x$都有

$$
A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x \leq 1,
$$

求 $A_{k}$ 的最大值.

问题 2 给定正整数 $n, k, n \geq k$, 已知 $A_{1}, A_{2}, \cdots, A_{n}$ 为实数, 对任意实数 $x$都有

$$
\left|A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x\right| \leq 1,
$$

求 $A_{k}$ 的最大值.

虽然看似是只是是否加绝对值的区别, 但事实上区别蛮大的. 在解决该问题后我咨询了单元多项式方面的专家 Tamas Erdelyi 教授, 被告知此结论是已有结论. 在 Q.L.Rahman 和 G.Schmeisser 写的书《Analytic Theory of Polynomials》的第 16 章的定理 16.2.2、定理 16.2.4 以及推论 16.2.6 中已经出现过. 但我们这里的证明应该更容易被中学生理解.

## I. 主要结果及证明

定理 1 给定正整数 $n$, 已知 $A_{1}, A_{2}, \cdots, A_{n}$ 为实数, 且对任意实数 $x$ 都有

$$
A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x \leq 1,
$$

则 $A_{1}$ 的最大值为 $2 \cos \frac{\pi}{n+2}$.

修订日期: 2021-02-05.
证明 我们先来解决 $n$ 为奇数的情形, 设 $n=2 m-1, m \in \mathbb{N}^{*}$, 设 $\alpha=\frac{\pi}{2 m+1}$.我们先来证明一个引理:

引理 1 记

$$
u_{j}=\left\{\begin{aligned}
1+\cos \alpha, & j=0, \\
2 \cos (2 j \alpha)+2 \cos \alpha, & 1 \leq j \leq m-1 .
\end{aligned}\right.
$$

则我们有

$$
\sum_{j=0}^{m-1} u_{j} \cos (2 k j \alpha)=\left\{\begin{array}{c}
(2 m+1) \cos \alpha, \quad k=0 \\
m+\frac{1}{2}, \quad k=1 \\
0, \quad 2 \leq k \leq m
\end{array}\right.
$$

引理的证明是简单的, 只是一些计算, 关键是发现这些等式.

证明 对于 $2 \leq k \leq m$ ，

$$
\sum_{j=0}^{m-1} u_{j} \cos (2 k j \alpha)
$$

$$
\begin{aligned}
= & 1+\cos \alpha+2 \sum_{j=1}^{m-1} \cos (2 k j \alpha) \cos (2 j \alpha)+2 \cos \alpha \sum_{j=1}^{m-1} \cos (2 k j \alpha) \\
= & 1+\cos \alpha+\sum_{j=1}^{m-1} \cos (2(k+1) j \alpha)+\sum_{j=1}^{m-1} \cos (2(k-1) j \alpha)+2 \cos \alpha \sum_{j=1}^{m-1} \cos (2 k j \alpha) \\
= & +\cos \alpha+\frac{(-1)^{k} \sin 2(k+1) \alpha-\sin (k+1) \alpha}{2 \sin (k+1) \alpha} \\
& +\frac{(-1)^{k} \sin 2(k-1) \alpha-\sin (k-1) \alpha}{2 \sin (k-1) \alpha}+\cos \alpha \cdot \frac{(-1)^{k-1} \sin 2 k \alpha-\sin k \alpha}{\sin k \alpha} \\
= & 1+\cos \alpha+(-1)^{k} \cos (k+1) \alpha-\frac{1}{2}+(-1)^{k} \cos (k-1) \alpha-\frac{1}{2}
\end{aligned}
$$

$+(-1)^{k-1} 2 \cos \alpha \cos k \alpha-\cos \alpha$

$=(-1)^{k}(\cos (k+1) \alpha+\cos (k-1) \alpha-2 \cos \alpha \cos k \alpha)=0$.

对于 $k=0,1$ 的时候也可以类似计算.

回到原题.一方面, 记

$$
f(x)=A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{2 m-1} \cos (2 m-1) x,
$$

由于对任意 $j, 0 \leq j \leq m-1, u_{j} \geq 0$, 故我们有,

$$
\sum_{j=0}^{m-1} u_{j} \cdot f(2 j \alpha) \leq \sum_{j=0}^{m-1} u_{j}
$$

令 $B_{1}=A_{1} ; B_{k}=A_{k}+A_{2 m+1-k}, 2 \leq k \leq m$, 由引理得,

$$
\sum_{j=0}^{m-1} u_{j} f(2 j \alpha)=\sum_{j=0}^{m-1} u_{j} \sum_{k=1}^{m} B_{k} \cos (2 k j \alpha)=\sum_{j=0}^{m-1} \sum_{k=1}^{m} u_{j} B_{k} \cos (2 k j \alpha)
$$

$$
=\sum_{k=1}^{m} B_{k} \sum_{j=0}^{m-1} u_{j} \cos (2 k j \alpha)=B_{1} \cdot\left(m+\frac{1}{2}\right),
$$

而又

$$
\sum_{j=0}^{m-1} u_{j}=(2 m+1) \cos \alpha
$$

故我们有

$$
A_{1}=B_{1} \leq 2 \cos \alpha
$$

另一方面, 我们来构造一个例子符合条件且 $A_{1}=2 \cos \alpha$. 记

$$
g(x)=(1-\cos x) \prod_{k=1}^{m-1}(\cos x-\cos (2 k \alpha))^{2}
$$

容易知道, $g(x)$ 还可以写成如下形式:

$$
g(x)=a_{0}+a_{1} \cos x+a_{2} \cos 2 x+\cdots+a_{2 m-1} \cos (2 m-1) x,
$$

故由于 $g(2 j \alpha)=0,0 \leq j \leq m-1$, 故我们有

$$
\sum_{j=0}^{m-1} u_{j} g(2 j \alpha)=0
$$

从而我们有

$$
(2 m+1) \cos \alpha \cdot a_{0}+\left(m+\frac{1}{2}\right) \cdot a_{1}=0,
$$

即

$$
a_{1}=-2 \cos \alpha \cdot a_{0},
$$

且易知,

$$
a_{0}=\frac{\sum_{k=0}^{2 m} g(2 k \alpha)}{2 m+1}=\frac{2 g(2 m \alpha)}{2 m+1}>0,
$$

故我们可取，

$$
g(x)=-\frac{a_{1}}{a_{0}} \cos x-\frac{a_{2}}{a_{0}} \cos 2 x-\cdots-\frac{a_{2 m-1}}{a_{0}} \cos (2 m-1) x,
$$

即符合条件.

对于 $n$ 为偶数的情形, 设 $n=2 m, m \in \mathbb{N}^{*}$, 设 $\alpha=\frac{\pi}{2 m+2}$. 我们先来证明一个引理:

引理 2 记 $u_{j}=\cos \alpha+\cos (2 j-1) \alpha, 1 \leq j \leq m$. 则我们有,

$$
\sum_{j=1}^{m} u_{j} \cos (k(2 j-1) \alpha)=\left\{\begin{array}{c}
(m+2) \cos \alpha, \quad k=0, \\
\frac{m}{2}+1, \quad k=1, \\
0, \quad 2 \leq k \leq m .
\end{array}\right.
$$

引理的证明以及应用引理证明原问题的方法与 $n=2 m-1$ 时完全一样. 故我们完成了证明.

一个更一般的结果.

定理 2 给定正整数 $n$, 已知 $A_{1}, A_{2}, \cdots, A_{n}$ 为实数, 对任意实数 $x$ 都有:

$$
A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x \leq 1,
$$

则 $A_{k}$ 的最大值为 $2 \cos \frac{\pi}{p+2}$, 其中 $p=\left\lfloor\frac{n}{k}\right\rfloor$.

证明 记

$$
f(x)=A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x
$$

则对于任意 $x$,

$$
\begin{aligned}
g(x) & =\frac{f(x)+f\left(x+\frac{2 \pi}{k}\right)+\cdots+f\left(x+\frac{2(k-1) \pi}{k}\right)}{k} \\
& =A_{k} \cos y+A_{2 k} \cos 2 y+\cdots+A_{p k} \cos p y \leq 1,
\end{aligned}
$$

其中 $y=p x$, 利用上个定理的结论, 可得 $A_{k}$ 的最大值为 $2 \cos \frac{\pi}{p+2}$.

定理 3 给定正整数 $n$, 已知 $A_{1}, A_{2}, \cdots, A_{n}$ 为实数, 对任意实数 $x$ 都有:

$$
\left|A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x\right| \leq 1,
$$

则 $A_{1}$ 的最大值为

$$
\frac{2 \cot \frac{\pi}{2\left\lfloor\frac{n+1}{2}\right\rfloor+2}}{\left\lfloor\frac{n+1}{2}\right\rfloor+1} .
$$

证明 事实上我们只要解决 $n$ 为奇数的情形, $n$ 为偶数的情形是一样的.

我们先来证明 $n=4 m-1, m \in \mathbb{N}^{*}$ 的情形, 记 $\alpha=\frac{\pi}{4 m+2}$. 令,

$$
f(x)=A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{4 m-1} \cos (4 m-1) x,
$$

故我们有,

$$
\begin{aligned}
g(x) & =A_{1} \cos x+A_{3} \cos 3 x+\cdots+A_{4 m-1} \cos (4 m-1) x \\
& =\frac{f(x)-f(x+\pi)}{2} \leq 1
\end{aligned}
$$

因此

$$
g((2 j-1) \alpha) \leq 1,1 \leq j \leq m .
$$

故

$$
\sum_{j=1}^{m} \cos (2 j-1) \alpha \cdot g((2 j-1) \alpha) \leq \sum_{j=1}^{m} \cos (2 j-1) \alpha .
$$

而

$$
\sum_{j=1}^{m} \cos (2 j-1) \alpha=\frac{\sin 2 m \alpha}{2 \sin \alpha}=\frac{\cot \alpha}{2}
$$

且

$$
\begin{aligned}
& \sum_{j=1}^{m} \cos (2 j-1) \alpha \cdot g((2 j-1) \alpha) \\
= & \sum_{j=1}^{m} \cos (2 j-1) \alpha \cdot\left(\sum_{k=1}^{2 m} A_{2 k-1} \cos ((2 j-1)(2 k-1) \alpha)\right) \\
= & \sum_{k=1}^{2 m} A_{2 k-1} \sum_{j=1}^{m} \cos (2 j-1) \alpha \cdot \cos ((2 j-1)(2 k-1) \alpha) \\
= & A_{1} \sum_{j=1}^{m} \cos ^{2}(2 j-1) \alpha \\
= & A_{1} \cdot \frac{2 m+1}{4} .
\end{aligned}
$$

故

$$
A_{1} \leq \frac{2 \cot \frac{\pi}{4 m+2}}{2 m+1}
$$

对于 $n=4 m-3, m \in \mathbb{N}^{*}$ 的情形, 证明完全是一样的, 只需要取点为 $\frac{0 \cdot \pi}{2 m}, \frac{1 \cdot \pi}{2 m}, \cdots$, $\frac{(m-1) \cdot \pi}{2 m}$. 并考虑,

$$
\frac{1}{2} g(0)+\sum_{j=1}^{m-1} \cos 2 j \alpha g(2 j \alpha), \alpha=\frac{\pi}{4 m} .
$$

下面我们来构造例子, 我们来给出统一的构造. 记 $m=\left\lfloor\frac{n+1}{2}\right\rfloor$, 从而我们有 $n=2 m$ 或 $2 m-1$, 在这里令 $\alpha=\frac{\pi}{2 m+2}$. 并记 $f(x)=\frac{1}{(m+1)^{2}} \sum_{j=1}^{m}(-1)^{j-1}\{(2 m-2 j+3) \cot (2 j-1) \alpha+\cot \alpha\} \cdot \cos (2 j-1) x$,那么 $f(x)$ 满足其首项系数

$$
A_{1}=\frac{2 \cot \frac{\pi}{2 m+2}}{m+1}
$$

故我们只需证明对任意 $x \in \mathbb{R}$, 都有 $-1 \leq f(x) \leq 1$ 即可.

$$
\begin{aligned}
\text { 令 } \theta_{\nu} & =\frac{\nu \pi}{m+1}, 1 \leq|\nu| \leq m, \text { 记 } \\
S(x) & =f\left(x-\frac{\pi}{2}\right) \\
& =\frac{1}{(m+1)^{2}} \sum_{j=1}^{m}\{(2 m-2 j+3) \cot (2 j-1) \alpha+\cot \alpha\} \cdot \sin (2 j-1) x \\
& =\frac{1}{(m+1)^{2}} \sum_{j=1}^{m+1}\{(2 m-2 j+3) \cot (2 j-1) \alpha+\cot \alpha\} \cdot \sin (2 j-1) x
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{(m+1)^{2}} \sum_{j=1}^{m+1}(2 m-2 j+3) \cot (2 j-1) \alpha \cdot \sin (2 j-1) x \\
& +\frac{1}{(m+1)^{2}} \sum_{j=1}^{m+1} \cot \alpha \cdot \sin (2 j-1) x
\end{aligned}
$$

并注意到

$$
\begin{aligned}
\frac{\sin ^{2}(m+1) x}{\sin x} & =\sin x\left\{(m+1)+2 \sum_{k=1}^{m}(m+1-k) \cos 2 k x\right\} \\
& =\sum_{j=1}^{m+1} \sin (2 j-1) x,
\end{aligned}
$$

记

$$
h_{\nu}(x)=\frac{1}{(2 m+2)^{2}} \frac{\sin ^{2}(m+1) x}{\sin ^{2}\left(x-\theta_{\nu}\right) / 2}, \quad 1 \leq|\nu| \leq m
$$

我们有

$$
\begin{aligned}
h_{\nu}(x)-h_{-\nu}(x) & =\frac{2}{(2 m+2)^{2}} \sum_{k=1}^{2 m+1}(2 m+2-k)\left(\cos k\left(x-\theta_{\nu}\right)-\cos k\left(x+\theta_{\nu}\right)\right) \\
& =\frac{1}{(m+1)^{2}} \sum_{k=1}^{2 m+1}(2 m+2-k) \sin k \theta_{\nu} \sin k x
\end{aligned}
$$

再根据,

$$
\sum_{\nu=1}^{m} \sin \frac{\nu k \pi}{m+1}= \begin{cases}0, & \text { 若 } k \text { 偶数, } 1 \leq k \leq 2 m ， \\ \cot \frac{k \pi}{2 m+2}, & \text { 若 } k \text { 奇数, } 1 \leq k \leq 2 m ，\end{cases}
$$

我们有

$$
\sum_{\nu=1}^{m}\left(h_{\nu}(x)-h_{-\nu}(x)\right)=\sum_{j=1}^{m+1}\left\{(2 m-2 j+3) \cot \frac{(2 j-1) \pi}{2(m+1)}\right\} \frac{\sin (2 j-1) x}{(m+1)^{2}}
$$

从而

$$
S(x)=\sum_{\nu=1}^{m}\left(h_{\nu}(x)-h_{-\nu}(x)\right)+\frac{\cot \alpha \cdot \sin ^{2}(m+1) x}{(m+1)^{2} \sin x},
$$

而 $\frac{\cot \alpha \cdot \sin ^{2}(m+1) x}{(m+1)^{2} \sin x}$ 在 $\theta_{\nu}, 1 \leq|u| \leq m$ 处的值与导数均为 0 , 且

$$
h_{\nu}\left(\theta_{\mu}\right)=0 \text { 若 } \mu \neq \nu, h_{\nu}\left(\theta_{\nu}\right)=1 \text {, 且 } h_{\nu}^{\prime}\left(\theta_{\mu}\right)=0 \text { 其中 } 1 \leq|\nu|,|\mu| \leq m \text {, }
$$

故我们有 $S(x)$ 在 $\theta_{1}, \theta_{2}, \cdots, \theta_{m}$ 处的取值为 1 , 导数均为 0 , 由 Rolle 定理, $S^{\prime}(x)$ 在 $\left(\theta_{1}, \theta_{2}\right),\left(\theta_{2}, \theta_{3}\right), \cdots,\left(\theta_{m-1}, \theta_{m}\right)$ 处至少有 $m-1$ 个零点, 再加上 $S^{\prime}(x)$ $\theta_{1}, \theta_{2}, \cdots, \theta_{m}$ 处为 0 , 故 $S^{\prime}(x)$ 至少在 $(0, \pi)$ 上的 $2 m-1$ 点处取值为 0 , 再由 $S^{\prime}(x)$ 是偶函数, 从而在 $(-\pi, \pi)$ 上至少有 $4 m-2$ 个零点, 且由于这是个次数为 $2 m-1$ 次的三角多项式, 故在 $[-\pi, \pi)$ 上至多有 $4 m-2$ 个零点, 故 $S^{\prime \prime}(x)$ 的零点与 $S^{\prime}(x)$ 的零点不同.
故所有的这 $4 m-2$ 个零点处都为局部的极大值或极小值, 且 $S(0)=S(\pi)=$ 0 , 故我们得到在 $S(x)$ 在 $\theta_{1}, \theta_{2}, \cdots, \theta_{m}$ 处均取到极大值 1 , 从而 $S(x)$ 在 $(0, \pi)$ 上没有其他极大值点, 故我们有 $S(x) \leq 1, x \in(0, \pi)$. 另一方面我们易得，

$$
S(x)=\sum_{\nu=1}^{m}\left(h_{\nu}(x)-h_{-\nu}(x)\right)+\frac{\cot \alpha \cdot \sin ^{2}(m+1) x}{(m+1)^{2} \sin x} \geq 0, x \in(0, \pi),
$$

结合 $S(x)$ 奇函数, 我们有对任意 $x \in \mathbb{R},-1 \leq S(x) \leq 1$. 故我们完成了构造.

注 这里的构造部分我们参考了文献 [1]. 构造的最后一部分用了结论: 一个非零的 $n$ 次三角函数在一个周期内根的个数至多只有 $2 n$ 个. 这个是容易的, 可转为 $z=e^{i x}$ 的根个数.

一般地, 根据定理 1 到定理 2 的相同做法,我们有如下结果:

定理 4 给定正整数 $n, k, n \geq k$, 已知 $A_{1}, A_{2}, \cdots, A_{n}$ 为实数, 对任意实数 $x$都有

$$
\left|A_{1} \cos x+A_{2} \cos 2 x+\cdots+A_{n} \cos n x\right| \leq 1,
$$

则 $A_{k}$ 的最大值为

$$
\frac{2 \cot \frac{\pi}{2 m+2}}{m+1}
$$

其中 $m=\left\lfloor\frac{n+k}{2 k}\right\rfloor$.

## II. 相关问题

注 (1) 本结论推广了 1977 年 IMO 试题.

题 1 已知 $a, b, A, B$ 都是实数, 若对于一切实数 $x$, 都有

$$
f(x)=1-a \cos x-b \sin x-A \cos 2 x-B \sin 2 x \geq 0
$$

求证: $a^{2}+b^{2} \leq 2, A^{2}+B^{2} \leq 1$.

事实上, 我们有如下结果:

题 2 已知 $A_{k}, B_{k}, 1 \leq k \leq n$ 都是实数,若对于一切实数 $x$, 都有,

$$
f(x)=1-\sum_{k=1}^{n}\left(A_{k} \cos k x+B_{k} \sin k x\right) \geq 0
$$

求证: $A_{1}^{2}+B_{1}^{2} \leq 4 \cos ^{2} \frac{\pi}{n+2}, A_{n}^{2}+B_{n}^{2} \leq 1, A_{k}^{2}+B_{k}^{2} \leq 4 \cos ^{2} \frac{\pi}{p+2}, p=\left\lfloor\frac{n}{k}\right\rfloor$.

简证 只解决 $A_{1}^{2}+B_{1}^{2} \leq 4 \cos ^{2} \frac{\pi}{n+2}$, 首先由辅助角公式, 设 $y=x+\phi$,

$$
g(y)=1-\sqrt{A_{1}^{2}+B_{1}^{2}} \cos (y)-\sum_{k=1}^{n}\left(A_{k}^{\prime} \cos k y+B_{k}^{\prime} \sin k x\right) \geq 0,
$$

然后再考虑

$$
g(y)+g(-y) \geq 0
$$

即可用第 1 题结论.

注 (2) 事实上我们可以命制如下有意思的问题:

题 3 记 $n$ 为正整数, $A_{2}, A_{3}, \cdots, A_{n}$ 为实数, 则一定存在 $x \in \mathbb{R}$ 使得

$$
\cos x+A_{2} \cos 2 x+A_{3} \cos 3 x+\cdots+A_{n} \cos n x>\frac{1}{2} .
$$

注 (3) 同样地利用定理 3 的结论我们也可以命制如下有意思的问题:

题 4 记 $n$ 为正整数, $A_{2}, A_{3}, \cdots, A_{n}$ 为实数,则一定存在 $x \in \mathbb{R}$ 使得

$$
\left|\cos x+A_{2} \cos 2 x+A_{3} \cos 3 x+\cdots+A_{n} \cos n x\right|>\frac{\pi}{4}
$$

值得注意的是该问题不仅可以用题 3 的结论, 还有个直接的做法.

证明 记

$$
M=\max _{x \in \mathbb{R}}\left|\cos x+A_{2} \cos 2 x+A_{3} \cos 3 x+\cdots+A_{n} \cos n x\right|,
$$

且

$$
f(x)=\cos x+A_{2} \cos 2 x+A_{3} \cos 3 x+\cdots+A_{n} \cos n x,
$$

则我们有

$$
4 M=M \cdot \int_{0}^{2 \pi}|\cos x| d x \geq \int_{0}^{2 \pi} f(x) \cos x d x=\int_{0}^{2 \pi} \cos ^{2} x d x=\pi,
$$

从而 $M \geq \frac{\pi}{4}$, 并且我们容易知道等号是取不到的, 故

$$
M>\frac{\pi}{4}
$$

即证明了原问题.

致谢 感谢在写作过程中张端阳老师提供了绝对值情形的特例. 感谢在写作中冷岗松教授的鼓励. 感谢赖力博士在查阅相关资料上的帮助. 感谢龙崎岗老师在计算 $u_{j}$ 时提供的一些特殊数据上的计算.

## 参考文献

[1] Q.L.Rahman,G.Schmeisser. Analytic Theory of Polynomials. London Mathematical Society.

