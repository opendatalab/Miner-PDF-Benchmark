# 一道不等式问题的探究 

刘浩宇

(杭州市第二中学，310052)

2017 年秋季新星数学奥林匹克第 4 题是如下一道不等式:

题 1. 给定正整数 $n \geq 2$, 求最小的实数 $c$, 使得对任意非负实数 $a_{1}, a_{2}, \cdots$, $a_{n}$, 都存在 $i \in\{1,2, \cdots, n\}$, 满足 $a_{i-1}+a_{i+1} \leq c a_{i}$, 其中 $a_{0}=a_{n+1}=0$.

冷岗松教授指出, 这道题是由 2013 年罗马尼亚国家队选拔考试的一道题改编而成, 是一类 Ky Fan 型不等式.

题 2. 已知 $n$ 为正整数, $x_{1}, x_{2}, \cdots, x_{n}$ 为正实数, 证明:

$$
\begin{aligned}
& \min \left\{x_{1}, \frac{1}{x_{1}}+x_{2}, \cdots, \frac{1}{x_{n-1}}+x_{n}, \frac{1}{x_{n}}\right\} \leq 2 \cos \frac{\pi}{n+2} \\
\leq & \max \left\{x_{1}, \frac{1}{x_{1}}+x_{2}, \cdots, \frac{1}{x_{n-1}}+x_{n}, \frac{1}{x_{n}}\right\} .
\end{aligned}
$$

事实上, 可将题 1 中地条件改为 $\frac{a_{i-1}}{a_{i}}+\frac{a_{i+1}}{a_{i}} \leq c$, 再令 $x_{i}=\frac{a_{i+1}}{a_{i}} 1 \leq i \leq n$,就变成了与题 2 相同的结构, 此时题 2 的下标 $n$ 应改为 $n-1$, 从而题 1 的最佳常数 $c=2 \cos \frac{\pi}{n+1}$.

吴尉迟博士在讲评试卷时利用归纳法证明了题 1 , 而题 2 的官方解答中先是构造了一个数列, 使得 $x_{1}=\frac{1}{x_{1}}+x_{2}=\cdots=\frac{1}{x_{n-1}}+x_{n}=\frac{1}{x_{n}}$, 再用反证法证明了两边的不等式, 而我的证明方法有所不同.

设最佳常数 $c=c(n)$, 对较小的 $n$, 考虑一组使不等式的等号均成立的 $\left(a_{1}, \cdots, a_{n}\right)$, 可得 $c(2)=1, c(3)=\sqrt{2}, c(4)=\frac{\sqrt{5}+1}{2}, c(5)=\sqrt{3}$. 由此我猜测 $c(n)=2 \cos \frac{\pi}{n+1}$. 看到这个结果之后, 我联想到了一道以前在学校里做过的不等式问题:

题 3. 已知 $a_{1}, a_{2}, \cdots, a_{n}$ 为不全为 0 的实数, 求

$$
\frac{a_{1} a_{2}+a_{2} a_{3}+\cdots+a_{n-1} a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}}
$$

收稿日期: 2017-12-04； 修订日期: 2017-12-27.
的最大值.

这道题的想法是利用均值不等式平衡系数, 即利用如下 $n-1$ 个不等式.

$$
\begin{aligned}
2 a_{1} a_{2} & \leq \lambda_{1} a_{1}^{2}+\frac{1}{\lambda_{1}} a_{2}^{2}, \\
2 a_{2} a_{3} & \leq \lambda_{2} a_{2}^{2}+\frac{1}{\lambda_{2}} a_{3}^{2}, \\
& \vdots \\
2 a_{n-1} a_{n} & \leq \lambda_{n-1} a_{n-1}^{2}+\frac{1}{\lambda_{n-1}} a_{n}^{2} .
\end{aligned}
$$

相加后, 为使右边 $a_{1}^{2}, a_{2}^{2}, \cdots, a_{n}^{2}$ 的系数相同, 考虑找出 $\lambda_{1}, \cdots, \lambda_{n-1} \in \mathbb{R}$, 使得

$$
\lambda_{1}=\frac{1}{\lambda_{1}}+\lambda_{2}=\frac{1}{\lambda_{2}}+\lambda_{3}=\cdots=\frac{1}{\lambda_{n-2}}+\lambda_{n-1}=\frac{1}{\lambda_{n-1}}+\lambda_{n}
$$

这里 $\lambda_{n}=0$, 我们要求的最大值即为 $\frac{\lambda_{1}}{2}$.

这是一个递推数列, 满足 $\lambda_{k+1}=\lambda_{1}-\frac{1}{\lambda_{k}}(1 \leq k \leq n-1)$. 容易知道 $0<\frac{\lambda_{1}}{2} \leq 1$ (因为最小值为 $\lambda_{1}$, 显然不超过 2 ), 我们可设 $\lambda_{1}=2 \cos \alpha, \alpha \in\left(0, \frac{\pi}{2}\right.$ ].则有

$$
\begin{aligned}
& \lambda_{2}=2 \cos \alpha-\frac{1}{2 \cos \alpha}=\frac{3-4 \sin ^{2} \alpha}{2 \cos \alpha}=\frac{\sin 3 \alpha}{\sin 2 \alpha} \\
& \lambda_{3}=2 \cos \alpha-\frac{\sin 2 \alpha}{\sin 3 \alpha}=\frac{2 \sin 3 \alpha \cos \alpha-\sin 2 \alpha}{\sin 3 \alpha}=\frac{\sin 4 \alpha}{\sin 3 \alpha}
\end{aligned}
$$

一般地, 由归纳法可知 $\lambda_{k}=\frac{\sin (k+1) \alpha}{\sin k \alpha}$. 这里我们需多次利用和差化积公式

$$
\sin (k-1) \alpha+\sin (k+1) \alpha=2 \sin k \alpha \cos \alpha
$$

又要求 $\lambda_{n}=0$, 故 $\sin (n+1) \alpha=0$. 因此可取 $\alpha=\frac{\pi}{n+1}$, 此时最大值为 $\frac{\lambda_{1}}{2}=\cos \frac{\pi}{n+1}$. 等号成立时, 有 $\lambda_{k} a_{k}^{2}=\frac{1}{\lambda_{k}} a_{k+1}^{2}, 1 \leq k \leq n-1$. 即

$$
\frac{a_{k+1}}{a_{k}}=\lambda_{k}=\frac{\sin (k+1) \alpha}{\sin k \alpha}, 1 \leq k \leq n-1
$$

也即

$$
a_{k}=c \cdot \sin \frac{k \pi}{n+1}, 1 \leq k \leq n \text {, 这里 } c \text { 为不等于 } 0 \text { 的常数. }
$$

这道题的答案与题 1 的答案如此相似, 是否可以类似地完成? 经过尝试, 我发现是可以的.

由于 $a_{1}, \cdots, a_{n} \geq 0$, 故我们只需证明如下不等式:

$$
\begin{aligned}
a_{2}^{2}+\left(a_{1}+a_{3}\right)^{2}+ & \left(a_{2}+a_{4}\right)^{2}+\cdots+\left(a_{n-2}+a_{n}\right)^{2}+a_{n-1}^{2} \\
& \leq 4 \cos ^{2} \frac{\pi}{n+1}\left(a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}\right) .
\end{aligned}
$$

这样必存在一个 $i \in\{1,2, \cdots, n\}$ 使得 $a_{i-1}+a_{i+1} \leq c a_{i}$, 其中 $a_{0}=a_{n+1}=0$.
为证明式 (2), 我们考虑 $n-2$ 个局部的 Cauchy 不等式:

$$
\left(a_{k-1}+a_{k+1}\right)^{2} \leq\left(\frac{1}{\lambda_{k-1}}+\lambda_{k}\right)\left(\lambda_{k-1} a_{k-1}^{2}+\frac{1}{\lambda_{k}} a_{k+1}^{2}\right), \quad k=2,3, \cdots, n-1 .
$$

利用类似的方法, 我们可求得 $\lambda_{k}=\frac{\sin (k+1) \alpha}{\sin k \alpha}, k=1,2, \cdots, n-1$. 这里 $\alpha=\frac{\pi}{n+1}$.

这时, 注意到

$$
\frac{1}{\lambda_{k-1}}+\lambda_{k}=\frac{\sin (k-1) \alpha}{\sin k \alpha}+\frac{\sin (k+1) \alpha}{\sin k \alpha}=2 \cos \alpha,
$$

将 (3) 对 $k=2,3, \cdots, n-1$ 求和得

$$
\begin{aligned}
& \left(a_{1}+a_{3}\right)^{2}+\left(a_{2}+a_{4}\right)^{2}+\cdots+\left(a_{n-2}+a_{n}\right)^{2} \\
\leq & 2 \cos \alpha\left(\left(\frac{\sin 2 \alpha}{\sin \alpha} a_{1}^{2}+\frac{\sin 2 \alpha}{\sin 3 \alpha} a_{3}^{2}\right)+\left(\frac{\sin 3 \alpha}{\sin 2 \alpha} a_{2}^{2}+\frac{\sin 3 \alpha}{\sin 4 \alpha} a_{4}^{2}\right)\right. \\
& \left.+\cdots+\left(\frac{\sin (n-1) \alpha}{\sin (n-2) \alpha} a_{n-2}^{2}+\frac{\sin (n-1) \alpha}{\sin n \alpha} a_{n}^{2}\right)\right),
\end{aligned}
$$

两边加上 $a_{2}^{2}+a_{n-1}^{2}$, 此时, (4) 的左边即为 (2) 的左边, 而右边 $a_{1}^{2}$ 的系数为 $2 \cos \alpha \cdot \frac{\sin 2 \alpha}{\sin \alpha}=4 \cos ^{2} \alpha, a_{n}^{2}$ 的系数为 $2 \cos \alpha \cdot \frac{\sin (n-1) \alpha}{\sin n \alpha}=4 \cos ^{2} \alpha, a_{2}^{2}$ 的系数为 $2 \cos \alpha \cdot \frac{\sin 3 \alpha}{\sin 2 \alpha}+1=\frac{\sin 3 \alpha}{\sin \alpha}+1=2 \cos \alpha, a_{n-1}^{2}$ 的系数为 $2 \cos \alpha \cdot \frac{\sin (n-2) \alpha}{\sin (n-1) \alpha}+1=2 \cos \alpha$,对 $3 \leq k \leq n-2, a_{k}^{2}$ 的系数为 $2 \cos \alpha \cdot\left(\frac{\sin (k+1) \alpha}{\sin k \alpha}+\frac{\sin (k-1) \alpha}{\sin k \alpha}\right)=4 \cos ^{2} \alpha$. 从而有

$$
\begin{gathered}
a_{2}^{2}+\left(a_{1}+a_{3}\right)^{2}+\left(a_{2}+a_{4}\right)^{2}+\cdots+\left(a_{n-2}+a_{n}\right)^{2}+a_{n-1}^{2} \\
\leq 4 \cos ^{2} \alpha\left(a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}\right) .
\end{gathered}
$$

这就是 (2) 式.

由柯西不等式的取等条件, 应有 $\frac{a_{k+1}}{a_{k-1}}=\frac{\sin (k+1) \alpha}{\sin (k-1) \alpha}$, 取 $a_{k}=\sin k \alpha, 1 \leq k \leq n$,可得到 $c$ 的最大值就是 $2 \cos \frac{\pi}{n+1}$, 这就解决了题 1 .

冷岗松教授同时还指出一道类似的问题:

题 4. (第二期新星征解第 4 题) 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是实数, 证明:

$$
\sum_{k=1}^{n+1}\left(a_{k}-a_{k-1}\right)^{2} \leq 2\left(1+\cos \frac{\pi}{n+1}\right) \sum_{k=1}^{n} a_{k}^{2}
$$

其中 $a_{0}=a_{n+1}=0$.

事实上, 题 4 等价于

$$
2 \cos \frac{\pi}{n+1} \sum_{k=1}^{n} a_{k}^{2}+2 \sum_{k=2}^{n} a_{k-1} a_{k} \geq 0 .
$$

当 $a_{1}, a_{2}, \cdots, a_{n}$ 不全为 0 时 (否则显然), 即为

$$
\frac{a_{1} a_{2}+a_{2} a_{3}+\cdots+a_{n-1} a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}} \geq-\cos \frac{\pi}{n+1}
$$

左边就是题 3 中的左边表达式, 其证明也是类似的. 只需将题 3 证明中的均值不等式改为

$$
-2 a_{k} a_{k+1} \leq \frac{\sin \frac{k+1}{n+1} \pi}{\sin \frac{k}{n+1} \pi} a_{k}^{2}+\frac{\sin \frac{k}{n+1} \pi}{\sin \frac{k+1}{n+1} \pi} a_{k+1}^{2}, \quad 1 \leq k \leq n-1 .
$$

再对 $k=1,2, \cdots, n-1$ 求和即可. 不等式的取等条件为 $a_{k}=(-1)^{k} \cdot c \cdot \sin \frac{k \pi}{n+1}$,这里 $c$ 为不等于 0 的常数或 $a_{k}=0,0 \leq k \leq n+1$ (这是平凡的).

所以, 我们有以下结论:

对不全为 0 的实数 $a_{1}, a_{2}, \cdots, a_{n}$ 有

$$
-\cos \frac{\pi}{n+1} \leq \frac{a_{1} a_{2}+a_{2} a_{3}+\cdots+a_{n-1} a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}} \leq \cos \frac{\pi}{n+1} .
$$

这个表达式

$$
\frac{a_{1} a_{2}+a_{2} a_{3}+\cdots+a_{n-1} a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}}
$$

的上下界互为相反数, 这也是从它的形式中可以预见到的.

通过以上几个问题, 我们发现在一些利用二元均值, 柯西不等式证明的不等式中, 等式 $\sin (k-1) \alpha+\sin (k+1) \alpha=2 \sin k \alpha \cos \alpha$ 起着关键作用.

我们再来研究一些形式类似的问题. 以下两题均出自《不等式的秘密》一书.

题 5. 对任意实数 $x_{1}, x_{2}, \cdots, x_{n}$,

$$
x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+\cdots+\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2} \leq t\left(x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}\right)
$$

均成立, 求 $t$ 的最小值.

解 待定 $c_{1}, c_{2}, \cdots, c_{n}$ 为正实数, 由 Cauchy 不等式,

$$
\left(x_{1}+x_{2}+\cdots+x_{k}\right)^{2} \leq\left(c_{1}+c_{2}+\cdots+c_{n}\right)\left(\frac{x_{1}^{2}}{c_{1}}+\frac{x_{2}^{2}}{c_{2}}+\cdots+\frac{x_{k}^{2}}{c_{k}}\right) .
$$

将 (5) 对 $k=1,2, \cdots, n$ 求和, 可得

$$
\begin{aligned}
& x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+\cdots+\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2} \\
& \quad \leq \frac{s_{1}+s_{2}+\cdots+s_{n}}{c_{1}} x_{1}^{2}+\frac{s_{2}+\cdots+s_{n}}{c_{2}} x_{2}^{2}+\cdots+\frac{s_{n}}{c_{n}} x_{n}^{2},
\end{aligned}
$$

这里 $s_{k}=c_{1}+c_{2}+\cdots+c_{k}, k=1,2, \cdots, n$.

下面考虑选取 $c_{1}, c_{2}, \cdots, c_{n}$ 使得 (6) 中各 $x_{i}^{2}$ 的系数相等. 即

$$
\frac{s_{1}+s_{2}+\cdots+s_{n}}{c_{1}}=\frac{s_{2}+\cdots+s_{n}}{c_{2}}=\cdots=\frac{s_{n}}{c_{n}}=t
$$

也即 $\frac{s_{1}}{c_{1}-c_{2}}=\frac{s_{2}}{c_{2}-c_{3}}=\cdots=\frac{s_{n-1}}{c_{n-1}-c_{n}}=\frac{s_{n}}{c_{n}-c_{n+1}}$, 这里 $c_{n+1}=0$.
利用 $c_{k}=s_{k}-s_{k-1}, k=1,2, \cdots, n$, 这里 $s_{0}=0$. 上面的等式可化为

$$
\frac{s_{2}}{s_{1}}=\frac{s_{1}+s_{3}}{s_{2}}=\cdots=\frac{s_{n-2}+s_{n}}{s_{n-1}}=\frac{s_{n-1}+s_{n+1}}{s_{n}} .
$$

这里补充定义 $s_{n+1}=c_{1}+\cdots+c_{n}+c_{n+1}$.

注意到这个式子本质与题 3 的求解系数的等式是一致的，只不过有 $s_{n+1}=s_{n}$, 考虑 (1) 中的 $\lambda_{n}=\frac{\sin (n+1) \alpha}{\sin n \alpha}=1$, 知 (7) 就是 (1) 在 $2 n+1$ 下的情形.故可取 $s_{k}=\sin k \alpha$, 这里 $\alpha=\frac{\pi}{2 n+1}$, 此时 $c_{k}=\sin k \alpha-\sin (k-1) \alpha$. 则

$$
\begin{aligned}
s_{k}+s_{k+1}+\cdots+s_{n} & =\sin k \alpha+\sin (k+1) \alpha+\cdots+\sin n \alpha \\
& =\frac{\cos \left(k-\frac{1}{2}\right) \alpha-\cos \left(n+\frac{1}{2}\right) \alpha}{2 \sin \frac{\alpha}{2}} \\
& =\frac{\cos \left(k-\frac{1}{2}\right) \alpha}{2 \sin \frac{\alpha}{2}} .
\end{aligned}
$$

从而

$$
t=\frac{s_{k}+s_{k+1}+\cdots+s_{n}}{c_{k}}=\frac{\cos \left(k-\frac{1}{2}\right) \alpha}{2 \sin \frac{\alpha}{2}(\sin k \alpha-\sin (k-1) \alpha)}=\frac{1}{4 \sin ^{2} \frac{\alpha}{2}} .
$$

利用 (4) 取等条件可知, 等号成立时, 应有

$$
\frac{x_{1}}{c_{1}}=\frac{x_{2}}{c_{2}}=\cdots=\frac{x_{n}}{c_{n}} \text {, }
$$

即

$$
\frac{x_{1}}{\sin \alpha}=\frac{x_{2}}{\sin 2 \alpha-\sin \alpha}=\cdots=\frac{x_{n}}{\sin n \alpha-\sin (n-1) \alpha}
$$

将这一组数代入不等式, 可得 $t \geq \frac{1}{4 \sin ^{2} \frac{\pi}{2(2 n+1)}}$. 故最佳常数为 $t=\frac{1}{4 \sin ^{2} \frac{\pi}{2(2 n+1)}}$.

与题 3 , 题 4 的紧密联系相同, 题 5 的不等式也有一个反向不等式.

题 6. 对任意实数 $x_{1}, x_{2}, \cdots, x_{n}$,

$$
x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+\cdots+\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2} \geq t\left(x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}\right)
$$

恒成立, 求 $t$ 的最大值.

解 待定 $c_{1}, c_{2}, \cdots, c_{n-1}$ 为正实数, 作换元 $y_{k}=x_{1}+x_{2}+\cdots+x_{k}$, 由均值不等式,

$$
\begin{aligned}
c_{1} y_{1}^{2}+\frac{1}{c_{1}} y_{2}^{2} & \geq-2 y_{1} y_{2}, \\
c_{2} y_{2}^{2}+\frac{1}{c_{2}} y_{3}^{2} & \geq-2 y_{2} y_{3}, \\
& \vdots \\
c_{n-1} y_{n-1}^{2}+\frac{1}{c_{n-1}} y_{n}^{2} & \geq-2 y_{n-1} y_{n} .
\end{aligned}
$$

相加得

$$
c_{1} y_{1}^{2}+\left(\frac{1}{c_{1}}+c_{2}\right) y_{2}^{2}+\cdots+\left(\frac{1}{c_{n-2}}+c_{n-1}\right) y_{n-1}^{2}+\frac{1}{c_{n-1}} y_{n}^{2}+2 \sum_{i=1}^{n-1} y_{i} y_{i+1} \geq 0 .
$$

而题中的不等式等价于

$$
y_{1}^{2}+y_{2}^{2}+\cdots+y_{n}^{2} \geq t\left(y_{1}^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(y_{n}-y_{n-1}\right)^{2}\right),
$$

即

$$
2\left(y_{1} y_{2}+y_{2} y_{3}+\cdots+y_{n-1} y_{n}\right) \geq \frac{2 t-1}{t}\left(y_{1}^{2}+y_{2}^{2}+\cdots+y_{n-1}^{2}\right)+\frac{t-1}{t} y_{n}^{2}
$$

对比 (8), (9), 可知应令 $c_{1}, \cdots, c_{n-1}$ 满足

$$
c_{1}=\frac{1}{c_{1}}+c_{2}=\cdots=\frac{1}{c_{n-2}}+c_{n-1}=\frac{1}{c_{n-1}}-1=\frac{1-2 t}{t} .
$$

这个等式的形式与题 3 的求解系数的等式类似. 利用相同的方法. 可以得到 $c_{k}=\frac{\sin (k+1) \alpha}{\sin k \alpha}$, 其中 $\alpha=\frac{2 \pi}{2 n+1}$. 此时 $\frac{1-2 t}{t}=2 \cos \alpha$, 则

$$
t=\frac{1}{2(\cos \alpha+1)}=\frac{1}{4 \cos ^{2} \frac{\alpha}{2}}=\frac{1}{4 \cos ^{2} \frac{\pi}{2 n+1}},
$$

等号成立时, 由均值不等式成立条件, 知

$$
\frac{y_{k}}{y_{k+1}}=-\frac{1}{c_{k}}=-\frac{\sin k \alpha}{\sin (k+1) \alpha}, \quad k=1,2, \cdots, n-1
$$

即 $y_{k}=(-1)^{k} \cdot c \cdot \sin k \alpha$, 这里 $c$ 为不等于 0 的常数. 从而

$$
x_{k}=y_{k}-y_{k-1}=(-1)^{k} \cdot c \cdot(\sin k \alpha+\sin (k-1) \alpha) \text {, }
$$

即

$$
x_{k}=(-1)^{k} \cdot c \cdot\left(\sin \frac{2 k \pi}{2 n+1}+\sin \frac{2(k-1) \pi}{n+1}\right), \quad k=1,2, \cdots, n \text {. }
$$

将这一组数代入不等式, 可得 $t \leq \frac{1}{4 \cos ^{2} \frac{\pi}{2 n+1}}$, 故最佳常数为 $t=\frac{1}{4 \cos ^{2} \frac{\pi}{2 n+1}}$.

由题 5 和题 6 , 我们得到一个有趣的结果:

对不全为 0 的实数 $x_{1}, x_{2}, \cdots, x_{n}$ 有

$$
\frac{1}{4 \cos ^{2} \frac{\pi}{2 n+1}} \leq \frac{x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+\cdots+\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2}}{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}} \leq \frac{1}{4 \sin ^{2} \frac{\pi}{2(2 n+1)}}
$$

我们发现这个结果在证明中配凑系数的过程和最终得到的上下界均与题 3 ,题 4 类似. 赵斌老师指出, 这个不等式也可以直接利用 $(*)$ 证明.

以 $(* *)$ 右边的不等式为例.

$(*)$ 式不等式左边 $\Leftrightarrow a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}$

$$
\leq \frac{1}{2-2 \cos \frac{\pi}{n+1}}\left(a_{1}^{2}+\left(a_{1}-a_{2}\right)^{2}+\cdots+\left(a_{n-1}-a_{n}\right)^{2}+a_{n}^{2}\right)
$$

令 $n=2 k$, 并令 $a_{n+k}=a_{n+1-k}, k=1,2, \cdots, n$, 即得

$$
2\left(a_{1}^{2}+a_{2}^{2}+\cdots+a_{k}^{2}\right) \leq \frac{2}{2-2 \cos \frac{\pi}{2 k+1}}\left(a_{1}^{2}+\left(a_{1}-a_{2}\right)^{2}+\cdots+\left(a_{k-1}-a_{k}\right)^{2}\right) .
$$

再令 $a_{i}=x_{1}+\cdots+x_{i}, i=1,2, \cdots, k$, 得

$$
x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+\cdots+\left(x_{1}+\cdots+x_{k}\right)^{2} \leq \frac{1}{4 \sin ^{2} \frac{\pi}{2(2 k+1)}}\left(x_{1}^{2}+x_{2}^{2}+\cdots+x_{k}^{2}\right),
$$

这就是 $(* *)$ 的右边.

这个证明的想法是将前 $i$ 项和的形式转化为相邻两项之间的关系利用差分代换, 令 $y_{i}=x_{1}+\cdots+x_{i}, i=1,2, \cdots, k$. 则不等式转化为

$$
y_{1}^{2}+y_{2}^{2}+\cdots+y_{k}^{2} \leq \frac{1}{4 \sin ^{2} \frac{\pi}{2(2 k+1)}}\left(y_{1}^{2}+\left(y_{1}-y_{2}\right)^{2}+\cdots+\left(y_{k-1}-y_{k}\right)^{2}\right) .
$$

这个不等式的右边缺少了项 $y_{k}^{2}$, 我们考虑 $(*)$ 在 $n=2 k$ 时的情形, 若将 $y_{1}, \cdots, y_{k}$ 拓展为 $y_{1}, \cdots, y_{k}, y_{k}, \cdots, y_{1}$, 则中间项 $\left(y_{k}-y_{k}\right)^{2}=0$ 便消失了. 这就产生了上述的证明.

对 $(* *)$ 不等式作一些转化, 可以得到一个与题 2 形式相似的不等式.

题 7. 已知 $n$ 为正整数, $x_{1}, x_{2}, \cdots, x_{n}$ 为正实数, 证明:

$$
\begin{aligned}
& \min \left\{x_{1}, \frac{1}{x_{1}}+x_{2}, \cdots, \frac{1}{x_{n-1}}+x_{n}, \frac{1}{x_{n}}+1\right\} \leq 2 \cos \frac{\pi}{2 n+3} \\
\leq & \max \left\{x_{1}, \frac{1}{x_{1}}+x_{2}, \cdots, \frac{1}{x_{n-1}}+x_{n}, \frac{1}{x_{n}}+1\right\} .
\end{aligned}
$$

事实上, 在题 2 中令 $n=2 k+1$, 并令 $x_{k+1+i}=\frac{1}{x_{k+1-i}}, i=1,2, \cdots, k$, 并令 $x_{k+1}=1$ (这是可行的, 因为等号成立时恰有 $x_{k+1}=\frac{\sin (k+2) \cdot \frac{\pi}{2 k+3}}{\sin (k+1) \cdot \frac{\pi}{2 k+3}}=1$ ) 便得到了题 7 .

