# 如何知道刀塔游戏的内部积分 

聂子佩

设 $k$ 是正整数. 今有小明和另外一些玩家参与一种名为刀塔的游戏, 每人对应一个实数作为他的内部积分, 然而这个游戏的系统并不能直接让玩家查询他们的积分. 每次刀塔游戏由事先决定的 $k$ 名玩家合作完成,在这次游戏中系统会显示这 $k$ 名玩家积分的算术平均值, 我们假设积分不会因游戏的完成而改变. 问: 至少经过几场游戏, 我们可以推算出小明的内部积分? 由于这个问题似乎不太容易回答, 我们记这个问题的答案为 $f(k)$, 转而求 $f(k)$ 的合适的上下界.

例如, 当 $k=1$ 时, 小明一个人参加一次游戏即可知道他的积分: 而当 $k=2$ 时, 则至少经过三次游戏, 得到小明小红, 小明老王, 小红老王的积分之和分别为 $S_{1}, S_{2}, S_{3}$, 然后得出小明的积分 $\frac{S_{1}+S_{2}-S_{3}}{2}$. 因此, 我们有 $f(1)=1, f(2)=3$. 实际上, 当游戏允许几种不同的人数合作时, 要推算出小明的内部积分所需的最少游戏次数将会显著地减少, 如何利用好每场游戏的参与人数都相等这个条件将是给出适当下界的关键.

我们首先需要考虑的问题是, 究竟有哪些方法可以推算出小明的积分. 事实上, 若把每个人的内部积分作为一个未知数, 那么每次游戏后得到的信息是其中 $k$ 个数的和. 已知一些有理系数的线性方程, 能确定一个变元的值当且仅当这个变元可以写成这些方程的有理系数线性组合. 更确切地说, 我们有

$$
a_{1}=\sum_{i=1}^{f(k)} r_{i} S_{i}
$$

这里 $a_{1}$ 是对应于小明的变元, $r_{i}$ 是有理数, $S_{i}$ 是 $k$ 个变元的和. 由于 $f(k)$ 是最小的使得 1 )式有解的正整数, 我们知道 $a_{1}, S_{1}, \ldots, S_{f(k)}$ 中任意 $f(k)$ 个表达式线性无关, 于是给定 $S_{i}(1 \leqslant i \leqslant f(k))$ 后我们可以利用克莱姆法则解出 $r_{i}(1 \leqslant i \leqslant f(k))$. 特别地, 存在 $f(k) \times f(k)$ 的 $(0,1)$ 非奇异矩阵 $M$, 使得 $\operatorname{det}(M) r_{i}(1 \leqslant i \leqslant f(k))$ 是整数.另一方面, 将 (1)式中的所有变元赋值为 1 , 我们得到

$$
\frac{\operatorname{det}(M)}{k}=\sum_{i=1}^{f(k)} \operatorname{det}(M) r_{i} \in \mathbb{Z}
$$

由于 $\operatorname{det}(M) \neq 0$, 我们得到 $k \leqslant|\operatorname{det}(M)|$. 由归纳法可知, 任何 $n \times n$ 的 $(0,1)$ 矩阵的行列式的绝对值不超过 $n !$,故 $k \leqslant|\operatorname{det}(M)| \leqslant f(k)$ !. 于是以下定理成立.

定理1. 对正整数 $k \geqslant 7$, 我们有

$$
f(k)>\frac{\log k}{\log \log k}
$$

假设 $k \geqslant 2$. 接下来我们计算 $f(k)$ 的上界. 令 $a_{1}, a_{2}, \ldots$ 分别为对应于这些玩家的变元, 其中 $a_{1}$ 为对应于小明的变元. 令

$$
S_{1}=\sum_{i=1}^{k} a_{i}
$$

对于 $1 \leqslant j \leqslant\left\lfloor\log _{2} k\right\rfloor$, 令

$$
S_{3 j-1}=\sum_{i=1}^{\left\lfloor\frac{k}{2 j}\right\rfloor} a_{i}+\sum_{i=k+1}^{2 k-\left\lfloor\frac{k}{2 j}\right\rfloor} a_{i}
$$

公元2015年6月17日, 又没吃药, 感觉自己萌沙萌动哒劫

$$
\begin{gathered}
S_{3 j}=\sum_{i=\left\lfloor\frac{k}{2^{j}}\right\rfloor+1}^{2\left\lfloor\frac{k}{2 j}\right\rfloor} a_{i}+\sum_{i=k+1}^{2 k-\left\lfloor\frac{k}{2 j}\right\rfloor} a_{i}, \\
S_{3 j+1}=a_{\left\lfloor\frac{k}{2^{j-1}}\right\rfloor}+\sum_{i=k+1}^{2 k-1} a_{i} .
\end{gathered}
$$

则我们可以验证

$$
k a_{1}=S_{1}+\sum_{j=1}^{\left\lfloor\log _{2} k\right\rfloor} 2^{j-1}\left(S_{3 j-1}-S_{3 j}+\varepsilon_{j-1}\left(-S_{3 j+1}+S_{3\left\lfloor\log _{2} k\right\rfloor-1}\right)\right)
$$

这里 $\varepsilon_{j}=\left\lfloor\frac{k}{2^{j}}\right\rfloor-2\left\lfloor\frac{k}{2^{j+1}}\right\rfloor$ 是 $k$ 的二进制表达. 如此, 我们证明了以下定理.

定理 2 . 对正整数 $k \geqslant 5$, 我们有

$$
f(k)<5 \log k
$$

作者尚不知道 $f(k)$ 更接近定理1 中给出的下界还是定理 2 中给出的上界, 若得出更佳的对 $f(k)$ 的估计欢迎与他联系.

致谢. 感谢于乾同学告知作者如此有趣的题目.

聂子佩: Department of Mathematics, Princeton University, Princeton, NJ 08544, United States 电邮地址: znie@princeton.edu

