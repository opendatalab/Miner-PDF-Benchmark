# 三个问题的命题过程 

胡俊浦<br>(温州育英国际实验学校, 325014)<br>指导教师: 孙涛

我的同学林逸沿最近在数学新星网发表了两个问题和两篇文章. 受林逸沿工作的激励, 我也开始命题尝试. 本文介绍三个问题的命制过程. 难度相当于联赛 1,2 题难度.

问题 1 在等腰 $\triangle A B C$ 中, $D, E$ 分别在 $A B, A C$ 上且 $D E / / B C$. 设等腰梯形 $D E C B$ 的外接圆为 $\Gamma, F$ 为弧 $\overparen{D E}$ 上的点, $F E$ 与 $B C$ 延长交于 $G . K$ 为圆 $\Gamma$在 $F, C$ 处切线的交点. 证明: $A K$ 平分 $C G$.

![](https://cdn.mathpix.com/cropped/2024_02_26_b79dd26e3917b1f1ae83g-1.jpg?height=491&width=580&top_left_y=1439&top_left_x=744)

该问题来源于偶然想到一个常见的模型.

模型 1 设 $B, C$ 为 $\odot O$ 内点满足 $B C$ 过圆心 $O$ 且被 $O$ 平分, $A$ 为圆上一点, 延长 $A B, A C$ 交圆于 $D, E$. 过 $D, E$ 作切线交于点 $K, J$ 为 $A K$ 的中点, 则 $J O \perp B C$.

证明思路 如图, 作 $A F / / B C$ 交圆于 $F$, 则 $A F, A B, A O, A C$ 成调和线束.延长 $A O$ 交圆于 $G$, 则 $F D G E$ 为调和四边形, 根据调和四边形的性质有 $K G F$共线.

修订日期: 2021-08-08.

![](https://cdn.mathpix.com/cropped/2024_02_26_b79dd26e3917b1f1ae83g-2.jpg?height=563&width=514&top_left_y=204&top_left_x=774)

命题过程 受模型 1 的启发, 我试图用这种平行线结合中点得共线的方法命一道题, 过程较为顺利, 把构型中的一个点 $C$ 置于圆上, 另一点 $B$ 置于圆内,同上作图可知有如下图的共线结论, 其中 $M$ 即为 $B C$ 中点.
![](https://cdn.mathpix.com/cropped/2024_02_26_b79dd26e3917b1f1ae83g-2.jpg?height=626&width=972&top_left_y=1086&top_left_x=544)

为了进一步隐藏点 $G$, 考虑利用帕斯卡定理转化结论. 上面的核心结论即 $K=F G \cap C C$. 再设 $C B$ 延长交圆于 $E$, 有 $M=A G \cap C E$. 进而最后的点为 $P=E F \cap A C$, 可以把结论转化为 $K P$ 平分 $B C$. 根据等腰梯形 $F A C E$ 进一步润饰条件和图形的相对位置可得问题 1.

![](https://cdn.mathpix.com/cropped/2024_02_26_b79dd26e3917b1f1ae83g-2.jpg?height=500&width=636&top_left_y=2120&top_left_x=710)
证明 设 $M$ 为 $C G$ 的中点, $E M$ 交圆 $\Gamma$ 于 $L$. 由 $E D / / C G$ 知 $E D, E C, E L$, $E G$ 呈调和线束. 从而 $F L C D$ 为调和四边形, 故 $D, L, K$ 共线. 在圆内接六边形 $C C B D L E$ 中用帕斯卡定理知 $A, K, M$ 共线, 故 $A K$ 平分 $C G$.

评注 此题过程照这样写十分简略, 同时也可用三角计算的方法解决, 难度不大, 图形简洁, 正常来讲大约 15-30 分钟能解决.

问题 2 已知非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{i=1}^{n} x_{i}=1$, 求

$$
\sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j}
$$

的最大值.

此题的灵感来源于增刊一上的一道题.

模型 2 已知 $x_{i} \geq 0$ 满足 $\sum_{i=1}^{n} x_{i}=1$, 求 $n=4,5$ 时

$$
\sum_{i=1}^{n} i x_{i}\left(1-x_{i}\right)
$$

的最大值.

命题过程 一个自然的想法是将 $n=4,5$ 拓展到任意整数, 但显然对 $n=4,5$ 的方法在大于 5 时并不适用 (要不然为什么出这题的人不要求直接对任意 $n$ 证明). 于是转而进行另一种思路: 将 $1-x_{i}$ 替换为 $\sum_{j \neq i} x_{j}$, 原式转化为

$$
\sum_{1 \leq i<j \leq n}(i+j) x_{i} x_{j}
$$

进行了齐次化同时也成了命制此题的契机, 联想到下面两个恒等式

$$
\begin{aligned}
\sum_{1 \leq i, j \leq n}^{n} \min \{i, j\} x_{i} x_{j}= & \sum_{i=1}^{n} i x_{i}^{2}+2 \sum_{i=1}^{n} i x_{i} x_{j} \\
= & x_{n}^{2}+\left(x_{n}+x_{n-1}\right)^{2}+\cdots+\left(x_{n}+x_{n-1}+\cdots+x_{1}\right)^{2} ; \text { (1) } \\
\sum_{1 \leq i, j \leq n}^{n} \max \{i, j\} x_{i} x_{j}= & \sum_{i=1}^{n} i x_{i}^{2}+2 \sum_{i=1}^{n} j x_{i} x_{j} \\
= & (n+1)\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2} \\
& -\left[x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}+\cdots+\left(x_{1}+x_{2}+\cdots+x_{n}\right)^{2}\right]
\end{aligned}
$$

将两式相加后得到的唯一成果就是 $x_{1} \geq x_{2} \geq \cdots \geq x_{n}$ 时有

$$
\sum_{1 \leq i, j \leq n}(i+j) x_{i} x_{j}
$$

的最大值为 $n+1$, 实际上由

$$
\sum_{1 \leq i, j \leq n}(i+j) x_{i} x_{j}=2\left(\sum_{i=1}^{n} x_{i}\right)\left(\sum_{i=1}^{n} i x_{i}\right)
$$

易证.

脱离本题将两式相减发现

$$
2 \sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j}=(n-1) S^{2}-\sum_{i=1}^{n-1}\left(S_{i}^{2}+\left(S-S_{i}\right)^{2}\right),
$$

其中 $S_{i}=\sum_{j=1}^{i} x_{j}, S=\sum_{i=1}^{n} x_{i}$, 后面的式子恰好可由柯西放缩为 $\frac{n-1}{2} S^{2}$. 故有

$$
\sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j} \leq \frac{n-1}{4}
$$

等号在 $x_{1}=x_{n}=\frac{1}{2}, x_{2}=\cdots=x_{n-1}=0$ 时取到.

后来发现了另一个妙解如证法 2 .

解 取 $x_{1}=x_{n}=\frac{1}{2}, x_{2}=\cdots=x_{n}=0$ 知

$$
\sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j}=\frac{n-1}{4}
$$

下证

$$
\sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j} \leq \frac{n-1}{4}
$$

法 1 注意到式(1), (2). 设 $S_{i}=\sum_{j=1}^{i} x_{j}, S=\sum_{i=1}^{n} x_{i}$, 两式相减由柯西不等式知

$$
\begin{aligned}
2 \sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j} & =(n-1) S^{2}-\sum_{i=1}^{n-1}\left(S_{i}^{2}+\left(S-S_{i}\right)^{2}\right) \\
& \leq(n-1) S^{2}-(n-1) \frac{S^{2}}{2} \\
& =\frac{n-1}{2} .
\end{aligned}
$$

得证.

法 2 注意到

$$
\sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j}=\sum_{i=1}^{n-1} S_{i}\left(S-S_{i}\right) \leq \frac{n-1}{4} S^{2}=\frac{n-1}{4}
$$

即证.

综上所述, $\sum_{1 \leq i<j \leq n}(j-i) x_{i} x_{j}$ 的最大值为 $\frac{n-1}{4}$.

评注 此题解法二虽然简单但也并不容易看出, 给同学测试的时候大约要花 30 分钟左右写出, 可见思路的重要性远大于过程.
问题 $3(1)$ 已知正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $\sum_{i=1}^{n} a_{i}=n^{3}-1$, 求 $\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}$ 的最小值;

(2) 给定正整数 $n, k$, 正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $\sum_{i=1}^{n} a_{i}=k n$, 求 $\sum_{i=1}^{n}\left[a_{i}\right]^{2}$ 的最小值.

命题过程 注意到林逸沿研究 $\sum_{i=1}^{n} \frac{\left[a_{i}\right]^{2}}{a_{i}}$ 有了一定的成果, 也激励我去研究这种 $\sum_{i=1}^{n} a_{i}$ 且含有取整的式子, 我开始选择入手探究 $\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}$. 与林逸沿的式子不同, 此式在 $a_{i}$ 为整数照样不能去取等. 故先不妨 $a_{i}$ 为实数. 设 $\sum_{i=1}^{n} a_{i}=k, k<n$时平凡, 故不妨 $k \geq n$. 最简单的思路是设 $b_{i}^{2} \leq a_{i}<\left(b_{i}+1\right)^{2}$, 则 $\left[\sqrt{a_{i}}\right]=b_{i}$ 且有 $b_{i} \geq \max \left\{\sqrt{a_{i}}-1,0\right\}$. 设

$$
a_{1}, \cdots, a_{t} \geq 1, a_{t+1}, \cdots, a_{n}<1
$$

由柯西不等式

$$
\begin{aligned}
\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}=\sum_{i=1}^{n} b_{i}^{2} & \geq \sum_{i=1}^{t}\left(\sqrt{a_{i}}-1\right)^{2} \\
& =\sum_{i=1}^{t} a_{i}-2 \sum_{i=1}^{t} \sqrt{a_{i}}+t \\
& \geq S-2 \sqrt{t S}+t=(\sqrt{S}-\sqrt{t})^{2}
\end{aligned}
$$

其中 $S=\sum_{i=1}^{t} a_{i}>k-(n-t)>t$, 故

$$
\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}>(\sqrt{k-n+t}-\sqrt{t})^{2} \geq(\sqrt{k}-\sqrt{n})^{2}
$$

获得一个初步估计最小值约为 $\left[(\sqrt{k}-\sqrt{n})^{2}\right]$. 经尝试发现取特定 $k$ 可使等号成立, 即题 (1).

这次探索的过程就比较曲折了, 不管怎样等号成立都是一个坎, 过不去了我也就只能多换几个式子(这正是我所说的提出做不出困境), 怎么说试了五六个类似的式子, 就不一一赘述了, 最后能看的结论就是上述题 (2).

同时再将根号改成 $m$ 次根发现结论类似有

$$
\sum_{i=1}^{n}\left[\sqrt[m]{a_{i}}\right]^{m} \geq(\sqrt[m]{k}-\sqrt[m]{n})^{m}
$$

此时的证明要用琴生但没什么意义就保留了 2 次的情况.

解 (1) 取 $a_{1}=a_{2}=\cdots=a_{n}=n^{2}-\frac{1}{n}$ 则

$$
\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}=n(n-1)^{2}
$$

下证

$$
\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2} \geq n(n-1)^{2}
$$

设 $\left[\sqrt{a_{i}}\right]=b_{i}$, 则 $b_{i}^{2} \leq a_{i}<\left(b_{i}+1\right)^{2}$. 不妨设 $a_{1}, \cdots, a_{t} \geq 1, a_{t+1}, \cdots, a_{n}<1$,设

$$
S=\sum_{i=1}^{t} a_{i}=n^{3}-1-\sum_{i=t+1}^{n} a_{i} \geq n^{3}-1-n+t>t
$$

则

$$
\begin{aligned}
\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}=\sum_{i=1}^{n} b_{i}^{2} & \geq \sum_{i=1}^{t}\left(\sqrt{a_{i}}-1\right)^{2} \\
& =\sum_{i=1}^{t} a_{i}-2 \sum_{i=1}^{t} \sqrt{a_{i}}+t \\
& \geq S-2 \sqrt{t S}+t=(\sqrt{S}-\sqrt{t})^{2} \\
& >\left(\sqrt{n^{3}-1-n+t}-\sqrt{t}\right)^{2} \\
& =\frac{\left(n^{3}-1-n\right)^{2}}{\left(\sqrt{n^{3}-1-n+t}+\sqrt{t}\right)^{2}} \geq\left(\sqrt{n^{3}-1}-\sqrt{n}\right)^{2}
\end{aligned}
$$

又

$$
\left(\sqrt{n^{3}-1}-\sqrt{n}\right)^{2}>n(n-1)^{2}-1 \Leftrightarrow 2 n^{2}>2 \sqrt{n^{4}-n}
$$

成立且 $\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}$ 为整数. 故 $\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2} \geq n(n-1)^{2}$ 得证.

综上 $\sum_{i=1}^{n}\left[\sqrt{a_{i}}\right]^{2}$ 的最小值为 $n(n-1)^{2}$.

(2) 取 $a_{1}=\cdots=a_{n-1}=k-\frac{1}{n}, a_{n}=k+\frac{n-1}{n}$, 则

$$
\sum_{i=1}^{n}\left[a_{i}\right]^{2}=(n-1)(k-1)^{2}+k^{2}
$$

又由题意

$$
\sum_{i=1}^{n}\left[a_{i}\right]>\sum_{i=1}^{n}\left(a_{i}-1\right)=k n-n
$$

且 $\sum_{i=1}^{n}\left[a_{i}\right]$ 为整数. 故由 $\sum_{i=1}^{n}\left[a_{i}\right] \geq k n-n+1$ 可知

$$
\sum_{i=1}^{n}\left[a_{i}\right]^{2} \geq \frac{1}{n}\left(\sum_{i=1}^{n}\left[a_{i}\right]\right)^{2} \geq \frac{(n k-n+1)^{2}}{n}=n(k-1)^{2}+2(k-1)+\frac{1}{n}
$$

再由 $\sum_{i=1}^{n}\left[a_{i}\right]^{2}$ 为整数知

$$
\sum_{i=1}^{n}\left[a_{i}\right]^{2} \geq n(k-1)^{2}+2 k-1=(n-1)(k-1)^{2}+k^{2}
$$

综上所述, $\sum_{i=1}^{n}\left[a_{i}\right]^{2}$ 的最小值为 $(n-1)(k-1)^{2}+k^{2}$.

