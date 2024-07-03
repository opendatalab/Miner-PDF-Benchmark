# 2020 越南数学奥林匹克试题与解析 

甘润知 ${ }^{1}$ 马飞雁 ${ }^{1}$ 陈昱达 ${ }^{2}$ 陈奕宸 $^{3}$

(1. 华东师范大学第二附属中学, 201203; 2. 天津市第四中学, 300210;

3. 天津市南开中学, 300100)

指导教师: 杨丕业 (北京质心教育科技有限公司)

2020 越南数学奥林匹克 (VMO) 于 2019 年 12 月 27 日和 28 日举行. 本次竞赛由 7 道题目组成, 分两天举行. 第一天考试有 4 道题, 每题 5 分, 第二天考试有 3 个题, 分值分别为 6 分, 6 分, 7 分. 满分 40 分.

下面我们给出试题的解答与评析, 解答人姓名随解答给出. 我们还在 AoPS 论坛上选取了第 $4,5,6$ 题的优质解答 ${ }^{[1]}$, 翻译后一并刊登于本文.

同时感谢来自北京质心教育科技有限公司的杨丕业老师, 对试题进行了翻译 ${ }^{[2]}$, 并在我们撰写解答时提供宝贵的建议.

## I. 试 题

1. 数列 $x_{n}$ 定义为 $x_{1}=1$, 且对任意 $n \geq 1$ 都有 $x_{n+1}=x_{n}+3 \sqrt{x_{n}}+\frac{n}{\sqrt{x_{n}}}$.

(1) 证明: $\lim _{n \rightarrow \infty} \frac{n}{x_{n}}=0$;

(2) 求极限 $\lim _{n \rightarrow \infty} \frac{n^{2}}{x_{n}}$.

2. (1) 三个实数 $a, b, c$ 满足 $a^{2}+b^{2}+c^{2}=1$, 证明:

$$
|a-b|+|b-c|+|c-a| \leq 2 \sqrt{2}
$$

(2) 2019 个实数 $a_{1}, a_{2}, \ldots, a_{2019}$ 满足 $a_{1}^{2}+a_{2}^{2}+\ldots+a_{2019}^{2}=1$. 求表达式

$$
S=\left|a_{1}-a_{2}\right|+\left|a_{2}-a_{3}\right|+\ldots+\left|a_{2018}-a_{2019}\right|+\left|a_{2019}-a_{1}\right| .
$$

的最大值.

3. 数列 $a_{n}$ 定义为 $a_{1}=5, a_{2}=13$, 且对任意 $n \geq 2$ 都有 $a_{n+1}=5 a_{n}-6 a_{n-1}$.

(1) 证明: 该数列任意两个相邻的项都互素;

修订日期: 2020-02-29.

(2) 证明: 对任意自然数 $k$, 若 $p$ 是 $a_{2^{k}}$ 的一个素因子, 则 $p-1$ 可被 $2^{k+1}$ 整除.

4. 不等腰的锐角 $\triangle A B C$ 内接于 $\odot O, H$ 是其垂心, $D, E, F$ 分别是 $O$ 关于三边 $B C, C A, A B$ 的对称点.

(1) 设 $H_{a}$ 是 $H$ 关于 $B C$ 的对称点, $A^{\prime}$ 是 $A$ 关于 $O$ 的对称点, $O_{a}$ 是 $\triangle B O C$的外心. 证明: $H_{a} D$ 和 $O_{a} A^{\prime}$ 的交点在 $\odot O$ 上;

(2) 取点 $X$ 满足 $A X D A^{\prime}$ 是一个平行四边形. 证明: $\triangle A H X, \triangle A B F$ 和 $\triangle A C E$ 的外接圆有除 $A$ 外的公共点.

5. 以 $a$ 为参数的方程组:

$$
\left\{\begin{array}{l}
x-a y=y z \\
y-a z=z x \quad(x, y, z \in \mathbb{R}) . \\
z-a x=x y
\end{array}\right.
$$

(1) 当 $a=0$ 时, 解这个方程组;

(2) 证明: 当 $a>1$ 时该方程组有 5 组解.

6. 给定不等腰的锐角 $\triangle A B C$, 记 $D, E, F$ 分别为 $A, B, C$ 向对边所引高线的垂足. 以 $A D$ 为直径的圆交 $D E, D F$ 于点 $M, N$. 在 $A B, A C$ 上取点 $P, Q$ 满足 $N P \perp A B, M Q \perp A C$. 最后, 记 $\odot I$ 为 $\triangle A P Q$ 的外接圆.

(1) 证明: $\odot I$ 与 $E F$ 相切;

(2) 设 $T$ 为 $\odot I$ 在 $E F$ 上的切点, $D T$ 与 $M N$ 交于点 $K, L$ 是 $A$ 关于 $M N$的对称点. 证明: $\triangle D K L$ 的外接圆过 $E F$ 与 $M N$ 的交点.

7. 给定正整数 $n>1, T$ 是所有有序组 $(x, y, z)$ 组成的集合, 其中正整数 $x, y, z$ 互不相同, 且 $1 \leq x, y, z \leq 2 n$. 集合 $A$ 由一些有序对 $(u, v)$ 组成, 若对任意 $T$ 中的元素 $(x, y, z)$ 都有 $\{(x, y),(x, z),(y, z)\} \cap A \neq \varnothing$, 我们称 $A$ 与 $T$ 相连.

(1) 求 $T$ 中的元素个数;

(2) 证明: 存在一个与 $T$ 相连的集合, 且其恰有 $2 n(n-1)$ 个元素;

(3) 证明: 任意与 $T$ 相连的集合的元素个数都不少于 $2 n(n-1)$.

## II. 解答与评注

1. 数列 $x_{n}$ 定义为 $x_{1}=1$, 且对任意 $n \geq 1$ 都有 $x_{n+1}=x_{n}+3 \sqrt{x_{n}}+\frac{n}{\sqrt{x_{n}}}$.

(1) 证明: $\lim _{n \rightarrow \infty} \frac{n}{x_{n}}=0$;

(2) 求极限 $\lim _{n \rightarrow \infty} \frac{n^{2}}{x_{n}}$.

证明 (甘润知) (1) 我们证明 $x_{n} \geq n^{2}$.

注意到 $x_{1}=1, x_{2}=5$, 可以设当 $x_{n-1} \geq(n-1)^{2}$, 考虑 $n$ 的情况, 那么

$$
x_{n}=x_{n-1}+3 \sqrt{x_{n}}+\frac{n}{\sqrt{x_{n}}} \geq(n-1)^{2}+3(n-1) \geq n^{2}
$$

那么在 $n \rightarrow \infty$ 时,

$$
\lim _{n \rightarrow \infty} \frac{n}{x_{n}}=0
$$

(2) 我们的证明分两步:

(i) 证明: $x_{n}<\frac{9}{4} n^{2}+100 n$.

使用归纳假设, 显然此式对 $n=1,2$ 时是成立的, 设 (*) 在 $n-1$ 时成立,考虑 $n$ 时, 此时

$$
\begin{aligned}
x_{n} & =x_{n-1}+3 \sqrt{x_{n}}+\frac{n}{\sqrt{x_{n}}} \\
& <\frac{9}{4}(n-1)^{2}+100 n-100+3\left(\frac{3}{2}(n-1)+30\right)+1 \\
& <\frac{9}{4} n^{2}+100 n .
\end{aligned}
$$

(ii) 证明: $x_{n}>\frac{9}{4} n^{2}-100 n$.

使用归纳假设, 显然此式对 $n=1,2$ 是成立的, 设 (**) 在 $n-1$ 时成立, 考虑 $n$ 时, 此时

$$
\begin{aligned}
x_{n} & =x_{n-1}+3 \sqrt{x_{n}}+\frac{n}{\sqrt{x_{n}}} \\
& >\frac{9}{4}(n-1)^{2}-100 n+100+3\left(\frac{3}{2}(n-1)-30\right)+\frac{4}{9} \\
& >\frac{9}{4} n^{2}-100 n .
\end{aligned}
$$

因此

$$
\lim _{n \rightarrow \infty} \frac{n^{2}}{x_{n}}=\frac{4}{9}
$$

评注 十分基本的一个题, 很适合放在一试的第 9 题, 放在越南数学奥林匹克似乎有一些偏简单了. 第一问可以根据第二问的问题或者自己尝试写几个数猜出答案是 0 , 第二问的话笔者用了待定系数法: 先假设 $x_{n} \sim k n^{2}(n \rightarrow+\infty)$,
然后代入递推公式比较 $n$ 前的系数, 这样可以得到 $k$ 的值. 在写过程的时候要注意一个比较容易扣分的地方: 第二问别忘了要求上下界, 一部分学生可能就求完上界就开始写过程了, 这就可能会被扣掉第二问一半的分数了.

2. (1) 三个实数 $a, b, c$ 满足 $a^{2}+b^{2}+c^{2}=1$, 证明:

$$
|a-b|+|b-c|+|c-a| \leq 2 \sqrt{2}
$$

(2) 2019 个实数 $a_{1}, a_{2}, \ldots, a_{2019}$ 满足 $a_{1}^{2}+a_{2}^{2}+\ldots+a_{2019}^{2}=1$. 求表达式

$$
S=\left|a_{1}-a_{2}\right|+\left|a_{2}-a_{3}\right|+\ldots+\left|a_{2018}-a_{2019}\right|+\left|a_{2019}-a_{1}\right|
$$

的最大值.

证明（甘润知）(1) 设 $a \geq b \geq c$, 则

$$
|a-b|+|b-c|+|c-a| \leq 2|a|+2|c| \leq 2 \sqrt{2 a^{2}+2 c^{2}} \leq 2 \sqrt{2} \text {. }
$$

(2) 由于

$$
\prod_{i=1}^{2019}\left(a_{i}-a_{i+1}\right)\left(a_{i+1}-a_{i+2}\right) \geq 0
$$

所以存在 $1 \leq k \leq 2019$, 使 $\left(a_{k}-a_{k+1}\right)\left(a_{k+1}-a_{k+2}\right) \geq 0$. 即

$$
\left|a_{k}-a_{k+1}\right|+\left|a_{k+1}-a_{k+2}\right|=\left|a_{k}-a_{k+2}\right| .
$$

故原式左侧

$$
\begin{aligned}
S & =\left|a_{1}-a_{2}\right|+\cdots+\left|a_{k-1}-a_{k}\right|+\left|a_{k}-a_{k+2}\right|+\left|a_{k+2}-a_{k+3}\right|+\cdots+\left|a_{2019}-a_{1}\right| \\
& \leq 2\left|a_{1}\right|+2\left|a_{2}\right|+\cdots+2\left|a_{k}\right|+2\left|a_{k+2}\right|+\cdots+2\left|a_{2019}\right| \\
& \leq 2 \sqrt{\left(a_{1}^{2}+a_{2}^{2}+\cdots+a_{2019}^{2}\right) \cdot 2018} \\
& \leq 2 \sqrt{2018} .
\end{aligned}
$$

取等条件:

$$
a_{1}=\frac{1}{\sqrt{2018}}, a_{2}=-\frac{1}{\sqrt{2018}}, a_{3}=\frac{1}{\sqrt{2018}}, \cdots, a_{2018}=-\frac{1}{\sqrt{2018}}, a_{2019}=0 .
$$

评注 比较容易的一个不等式问题, 适合放在一试的第 10 题位置, 放在越南数学奥林匹克的第二题偏简单. 第一问因为式子轮换对称, 所以就可以设 $a \geq b \geq c$, 柯西或者均值不等式随便一做就做完了. 第二问在尝试 $\left|a_{1}-a_{2}\right|+\left|a_{2}-a_{1}\right|,\left|a_{1}-a_{2}\right|+\left|a_{2}-a_{3}\right|+\left|a_{3}-a_{4}\right|+\left|a_{4}-a_{1}\right|$ 的最大值的时候可以推出原式的最大值是 $2 \sqrt{2018}$, 注意到 2019 是一个奇数, 因此可以联想到一个常用结论: 对任意实数 $a_{1}, a_{2}, \cdots, a_{2 k+1}(k \geq 1)$ 排成一圈, 可以找到连续三个
数满足这三个数从小到大或者从大到小排列. 想到这个结论, 这道题便迎刃而解。书写时注意上下标, 不要把上下标弄混以至于一些不必要的扣分.

3. 数列 $a_{n}$ 定义为 $a_{1}=5, a_{2}=13$, 且对任意 $n \geq 2$ 都有 $a_{n+1}=5 a_{n}-6 a_{n-1}$.

(1) 证明: 该数列任意两个相邻的项都互素;

（2）证明: 对任意自然数 $k$, 若 $p$ 是 $a_{2^{k}}$ 的一个素因子, 则 $p-1$ 可被 $2^{k+1}$ 整除。

证明 (甘润知) (1) 由特征根方程可得 $a_{n}=2^{n}+3^{n}$. 由辗转相除法可得

$$
\left(2^{n}+3^{n}, 2^{n+1}+3^{n+1}\right)=\left(2^{n}+3^{n}, 3^{n}\right)=\left(2^{n}, 3^{n}\right)=1 .
$$

(2) 设素因子 $p \mid 2^{2^{k}}+3^{2^{k}}$. 由 $(2,3)=1$, 存在一个整数 $x$ 使得

$$
2 x \equiv 3 \quad(\bmod p),(x, p)=1
$$

则由 $p \mid(2 x)^{2^{k}}+(3 x)^{2^{k}}$, 那么 $p \mid x^{2^{k}}+1$.

设 $p$ 模 $x^{2^{k}}$ 的阶为 $\delta$, 则 $\delta \mid\left(p-1,2^{k+1}\right)$.

若 $(p-1)$ 中的 2 次幂小于 $k+1$ 次, 即 $v_{2}(\delta) \leq k$. 则

$$
-1 \equiv x^{2^{k}} \equiv\left(x^{\delta}\right)^{\frac{2^{k}}{\delta}} \equiv 1 \quad(\bmod p) .
$$

即 $p=2$, 矛盾!

故对每个素数 $p \mid 2^{2^{k}}+3^{2^{k}}$ 都有 $(p-1)$ 是 2 的 $k+1$ 次幕.

评注 这个题放在越南数学奥林匹克第三题偏简单, 应当是我国联赛二试的第一题难度 (可能都没有). 还是一个比较初级的考察“阶”的应用的考题. 第一问属于送分, 第二问的话结论既可以弱化又可以推广如下:

弱化的结论: 对素数 $p>2$, 若

$$
p \mid 2^{2^{k}}+1
$$

那么 $2^{k+1} \mid p-1$.

强化的结论: 对素数 $p>2$, 若

$$
p \mid x^{2^{k}}+y^{2^{k}}
$$

那么 $2^{k+1} \mid p-1$. 其中 $\operatorname{gcd}(x, y)=1$.

有兴趣的读者可以尝试:

弱化的结论的强化结论: 对素数 $p>2$, 整数 $k \geq 2$, 若 $p \mid 2^{2^{k}}+1$, 那么 $2^{k+2} \mid p-1$.
事实上, 能够联想到弱化结论, 题目也就做完了.

4. 不等腰的锐角 $\triangle A B C$ 内接于 $\odot O, H$ 是其垂心, $D, E, F$ 分别是 $O$ 关于三边 $B C, C A, A B$ 的对称点.

(1) 设 $H_{a}$ 是 $H$ 关于 $B C$ 的对称点, $A^{\prime}$ 是 $A$ 关于 $O$ 的对称点, $O_{a}$ 是 $\triangle B O C$的外心. 证明: $H_{a} D$ 和 $O_{a} A^{\prime}$ 的交点在 $\odot O$ 上;

(2) 取点 $X$ 满足 $A X D A^{\prime}$ 是一个平行四边形. 证明: $\triangle A H X, \triangle A B F$ 和 $\triangle A C E$ 的外接圆有除 $A$ 外的公共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_e3ec11798ed8a0a09fbeg-06.jpg?height=1033&width=988&top_left_y=800&top_left_x=543)

## 解法一 (甘润知、陈昱达)

(1) 设 $H_{a} D$ 交 $\odot O$ 于 $Z$. 只需证明 $Z, A^{\prime}, O_{a}$ 三点共线即可, 即需证 $\angle H_{a} Z A^{\prime}=\angle H_{a} Z O_{a}$.

由 $\angle O O_{a} C=2 \angle O B C=\angle O C D$ 可知 $\triangle O C D \sim \triangle C O_{a} O$, 则

$$
O C^{2}=O D \cdot O O_{a}=O H_{a}^{2}=O Z^{2}
$$

可知

$$
\angle Z O_{a} O=\angle O Z H_{a}=\angle O H_{a} Z=\angle O O_{a} H_{a},
$$

故 $Z, O, H_{a}, O_{a}$ 四点共圆. 又 $\angle A^{\prime} O O_{a}=\angle H_{a} O O_{a}$ 可得

$$
\angle H_{a} Z A^{\prime}=\frac{1}{2} \angle H O A^{\prime}=\angle A^{\prime} O O_{a}=\angle H_{a} O O_{a}=\angle H_{a} Z O_{a}
$$

（2）根据题目条件以及相关外心和垂心中角的性质可得

$$
\angle A E C=\angle A O C=2 \angle A B C=2(\pi-\angle A H C) .
$$

又因为 $E A=E C$, 因此 $E H=E A=E C$, 进而得到

$$
O A=O C=A E=E C=E H=H X .
$$

因此以 $H$ 为圆心, $H E$ 为半径作一个过 $X$ 的圆, 设这个圆还交 $\triangle A H X$ 的外接圆于 $Y$. 接下来证明 $Y$ 就是我们所要求的那个点.

注意到 $E C / / A O, E C=A O, E C=H X, A O H X$ 是平行四边形, 因此 $C H X E$ 也是平行四边形, 因此

$$
\angle C H O=\angle E X A \text {. }
$$

由 $H X=H Y=H E, A, H, X, Y$ 四点共圆以及垂心的角的性质进一步得到

$$
\begin{aligned}
\angle A Y E & =\angle A Y H-\angle H Y E=\angle H X A-\angle H E Y \\
& =\angle H X E-\angle A X E-\angle H E Y=\angle X E Y-\angle C H O \\
& =\frac{\pi}{2}-\angle X Y H-(\angle A H O-\angle A H C)=\frac{\pi}{2}-\angle A B C \\
& =\angle H A B=\angle O A C=\angle E C A .
\end{aligned}
$$

因此 $Y, A, C, E$ 四点共圆, 类似地, $Y, A, B, F$ 四点共圆, 因此命题获证.

![](https://cdn.mathpix.com/cropped/2024_02_26_e3ec11798ed8a0a09fbeg-07.jpg?height=885&width=948&top_left_y=1608&top_left_x=560)

解法二 (AoPS) (1) 略.

(2) 首先注意到 $X A A^{\prime} D, X A O H, H O A^{\prime} D$ 均为平行四边形. 因此

$$
\angle X H A=\angle H A O=\angle D O A^{\prime}=\angle D K A^{\prime} .
$$

设 $\odot(A B F) \cap \odot(A C E)=M$. 下证 $M$ 与 $K$ 关于 $\triangle A B C$ 的 $N_{9}$ (译者注: $N_{9}$ 为九点圆圆心) 对称. $\left(K=H_{A} D \cap O_{A} A^{\prime}\right)$.

由广义 Reim 定理的逆定理 (译者注: 广义 Reim 定理及其逆定理与证明见评析) 可知, 如果 $\mathcal{C}$ 是一个经过 $A, F, B, D, C, E$ 的圆雉曲线, 则

$$
B F / / C E \Longrightarrow M \in \mathcal{C} .
$$

又注意到 $K \in H_{A} D$, 因此

$$
\angle D K C=90^{\circ}-\angle C=\angle D E C \Longrightarrow D, E, K, C
$$

共圆. 注意到由于 $D$ 与 $E$ 关于 $C H$ 对称, 故

$$
\angle D E C=90^{\circ}-\angle C \text {. }
$$

同理可证 $A, F, E, K$ 共圆.

又由于广义 Reim 定理的逆定理, 有 $K \in \mathcal{C}$. 故

$$
\angle B M A=\angle E K D \text {. }
$$

又由于对称性, 故有 $M$ 与 $K$ 关于 $N_{9}$ 对称. 再注意到

$$
\angle X H A=\angle D K A^{\prime}=\angle X M A .
$$

因此, $\odot(A H X)$ 经过 $M$.

评注 有一点我国联赛二试的味道了 (放在越南数学奥林匹克第一天的压轴题还算比较合适), 笔者此题想了 1 个小时, 本题第一问是一个比较“陈”的结论了, 通过一些相似, 导角的常用手法可以轻松搞定. 第二问有一些困难, 我看到的一些解答有的是写了用调和, 有的是用向量法, 但这些解答的辅助线实在是让人看得眼花缭乱, 此处笔者采用了一个比较巧妙的手法: 注意到这个共的点事实上在一个以垂心为圆心，外接圆长为半径的一个圆上! 这个是需要一定的时间发现的，如果发现这个结论，那么这个题也就可以通过我们比较熟悉的导角做完了. 我认为单单展现此题的第二问, 虽然解答很短, 但是也在某一程度上达到了二试第 3 题的难度了。

附:

广义 Reim 定理 设 $\mathcal{C}$ 是一个过 $A, B$ 的圆锥曲线. 若过 $A, B$ 的圆 $\omega_{1}$ 和圆 $\omega_{2}$ 与 $\mathcal{C}$ 分别再次交于 $C, D$ 和 $E, F$. 则 $C D / / E F$.
证明设 $I, J$ 为复射影平面上两点, 齐次坐标分别为 $(1: i: 0)$ 和 $(1:-i: 0)$.考虑将 $A, B$ 分别变成 $I, J$ 的射影变换. 对每个点 $P$, 用 $P^{\prime}$ 表示射影变换后的点.则 $\mathcal{C}^{\prime}, \omega_{1}^{\prime}, \omega_{2}^{\prime}$ 均为圆. 此外, 由于 $\omega_{1}, \omega_{2}$ 交于 $A, B, I, J$, 可以得到 $\omega_{1}^{\prime}, \omega_{2}^{\prime}$ 的另外两个交点为 $I^{\prime}, J^{\prime}$. 由根心定理, $C^{\prime} D^{\prime}, E^{\prime} F^{\prime}, I^{\prime} J^{\prime}$ 三线共点. 再做一次反向的射影变换, 就证明了这个定理.

![](https://cdn.mathpix.com/cropped/2024_02_26_e3ec11798ed8a0a09fbeg-09.jpg?height=788&width=808&top_left_y=603&top_left_x=630)

广义 $\operatorname{Reim}$ 定理的逆定理 设 $\mathcal{C}$ 为一圆锥曲线, $A \in \mathcal{C}$. 设 $C, D, E, F \in \mathcal{C}$,使得 $C D / / E F$. 则 $\odot(A C D) \cap \odot(A E F) \in \mathcal{C}$.

证明 设 $T=\odot A E F \cap \odot A C D$. 这可以说明

$$
(T C, T D, T E, T F)=(A C, A D, A E, A F),
$$

故 $T \in \mathcal{C}$.

设

$$
\begin{aligned}
& M=A D \cap \odot A E F, \\
& N=A C \cap \odot A E F, \\
& K=T C \cap \odot A E F, \\
& L=T D \cap \odot A E F .
\end{aligned}
$$

由 Reim 定理 (译者注: 即广义 Reim 定理中, 圆锥曲线是圆的情况) 可得

$$
N L / / C D / / E F / / K M \text {. }
$$

因此有 $N M E F$ 和 $L K F E$ 关于 $E F$ 的垂直平分线对称. 特别地, 有 $[N, M ; E, F]=$
$[K, L ; E, F]$. 因此由交比的性质有

$$
[A C, A D ; A E, A F]=[N, M ; E, F]=[K, L ; E, F]=[T C, T D ; T E, T F]
$$

所以可以得出结论 $T \in \mathcal{C}$.

5. 以 $a$ 为参数的方程组:

$$
\left\{\begin{array}{l}
x-a y=y z \\
y-a z=z x \quad(x, y, z \in \mathbb{R}) . \\
z-a x=x y
\end{array}\right.
$$

(1) 当 $a=0$ 时, 解这个方程组;

(2) 证明: 当 $a>1$ 时该方程组有 5 组解.

## 解法一 (陈昱达)

(1) 当 $x=y=z$ 时, 可得到第一组和第二组解:

$$
(x, y, z)=(0,0,0),(1,1,1)
$$

下面考虑 $x, y, z$ 不全相等的情况. 消元可得 $y=x^{2} y$, 即 $\left(1-x^{2}\right) y=0$, 显然 $y \neq 0$, 则 $x= \pm 1$. 同理 $y= \pm 1, z= \pm 1$. 由原式的正负性可知 $x, y, z$ 必全为正数或两负一正, 则至多有以下三组解:

$$
(x, y, z)=(1,-1,-1),(-1,1,-1),(-1,-1,1) \text {. }
$$

经检验, 以上三组解均成立.

综上, 当 $a=0$ 时, 该方程组共有 5 组解:

$$
(x, y, z)=(0,0,0),(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) .
$$

(2) 首先可以求得两组解:

$$
(x, y, z)=(0,0,0),(1-a, 1-a, 1-a) .
$$

下面考虑 $x, y, z$ 不全相等的情况. 将原式消元可得

$$
\left\{\begin{array}{l}
x-a y=y(a x+x y) \\
y-a(a x+x y)=(a x+x y) x
\end{array},\right.
$$

得到

$$
y=\frac{a^{2} x+a x^{2}}{1+a x-x^{2}}
$$

再次消元可得

$$
x-\frac{a^{3} x}{1-a x-x^{2}}-\frac{a^{2} x^{2}}{1-a x-x^{2}}-\frac{a^{3} x^{2}+a^{2} x^{3}}{\left(1-a x-x^{2}\right)^{2}}=0 .
$$

再将此式除去 0 和 $1-a$ 的根 (即除以 $x(x-1+a)$ ), 整理可得

$$
x^{3}+\left(a^{2}+a+1\right) x^{2}+\left(a^{3}-1\right) x-a^{2}-a-1=0 .
$$

将 $f(x)=x^{3}+\left(a^{2}+a+1\right) x^{2}+\left(a^{3}-1\right) x-a^{2}-a-1$ 求导可得

$$
f^{\prime}(x)=3 x^{2}+2\left(a^{2}+a+1\right) x+a^{3}-1 \text {. }
$$

由

$$
\begin{gathered}
\Delta_{f^{\prime}(x)}=4\left(a^{4}-a^{3}+3 a^{2}+2 a+4\right)>4\left(3 a^{2}+2 a+4\right)>0(a>1), \\
\Delta_{f^{\prime}(x)}<4\left(a^{2}+a+1\right)^{2},
\end{gathered}
$$

可知 $f(x)$ 有两个极值点 $x_{f 1}, x_{f 2}$ :

$$
\begin{gathered}
x_{f 1}=-\frac{\left(\sqrt{a^{4}-a^{3}+3 a^{2}+2 a+4}+a^{2}+a+1\right)}{3}, \\
x_{f 2}=\frac{\left(\sqrt{a^{4}-a^{3}+3 a^{2}+2 a+4}-a^{2}-a-1\right)}{3} .
\end{gathered}
$$

由

$$
f\left(x_{f 1}\right)=x_{f 1}^{3}+\left(a^{2}+a+1\right) x_{f 1}^{2}+\left(a^{3}-1\right) x_{f 1}-a^{2}-a-1>0
$$

和

$$
f\left(x_{f 2}\right)=x_{f 2}^{3}+\left(a^{2}+a+1\right) x_{f 2}^{2}+\left(a^{3}-1\right) x_{f 2}-a^{2}-a-1<0
$$

可知该三次方程有三个不等实根 $x_{1}, x_{2}, x_{3}$.

下证明 $x, y, z$ 必两两不等.

若 $x=y \neq z$, 则由原式得

$$
x=(a+z) x \Rightarrow a+z=1 \Rightarrow z=1-a .
$$

此时 $x=y=z=1-a$, 与假设矛盾. 故 $x, y, z$ 两两不等. 由 $x, y, z$ 轮换且两两不等可知, 该方程组还有三组解:

$$
(x, y, z)=\left(x_{1}, x_{2}, x_{3}\right),\left(x_{2}, x_{3}, x_{1}\right),\left(x_{3}, x_{1}, x_{2}\right) .
$$

综上, 当 $a>1$ 时该方程组共有 5 组解:

$$
(x, y, z)=(0,0,0),(1-a, 1-a, 1-a),\left(x_{1}, x_{2}, x_{3}\right),\left(x_{2}, x_{3}, x_{1}\right),\left(x_{3}, x_{1}, x_{2}\right) .
$$

解法二 (AoPS) (1) 当 $a=0$ 时, 将三个方程相乘, 得到 $x y z(x y z-1)=0$.假设 $x y z=0$, 那么 $x=0$, 故 $y z=0, y=0$. 代入到第三个方程得到 $z=0$. 如果 $x y z-1=0$, 则分别用 $\frac{1}{x}, \frac{1}{y}, \frac{1}{z}$ 来代换 $y z, z x, x y$. 得到 $x=y=z= \pm 1$ (译者注:即 $(x, y, z)=(1,1,1)$ 或 $(1,-1,-1)$ 或 $(-1,1,-1)$ 或 $(-1,-1,1)$.

(2) 如果 $z=0$, 则 $x=y=0$.

如果 $z \neq 0$, 则

$$
x=a y+y z, y-a z=z, a y+y z, z-a=a y+y z .
$$

故

$$
x=a y+y z, y=\frac{a z}{1-a z-z^{2}} z-(a y+y z)=y(a y+y z) .
$$

由第二和第三个方程可以得到

$$
z-a^{2}+a z \cdot \frac{a z}{1-a z-z^{2}}=a+z\left(\frac{a z}{1-a z-z^{2}}\right)^{2} .
$$

即

$$
z^{5}+a^{2}+2 a z^{4}+2 a^{3}-2 z^{3}+a^{4}-a^{3}-a^{2}-2 a z^{2}+1-a^{3} z=0 .
$$

下证该方程有 5 组解. 容易看出该方程的两组解,即 0 和 $1-a$. 原方程化为

$$
(z)(z-1+a)\left(z^{3}+\left(a^{2}+a+1\right) z^{2}+\left(a^{3}-1\right) z-a^{2}-a-1\right)=0 .
$$

设 $f(z)=z^{3}+\left(a^{2}+a+1\right) z^{2}+\left(a^{3}-1\right) z-a^{2}-a-1$, 由

$$
f(-\infty)<0, f(-2 a)>0, f(0)<0, f(+\infty)>0
$$

可知该方程还有三组解, 故方程组共有五组解.

评注 本题难度上来说作为第二天的第一题还是比较合适的, 难度大约在二试第 1 题和第 2 题之间. 本题从方法上来说着实不太难, 核心就在于算. 看出 0 和 $1-a$ 的根后, 原题就化为了一个证明该三次方程有三个实根的问题 (此处也可以使用三次方程的实根判别式). 笔者认为 AoPS 上的解答构造的四个函数值比较巧妙, 比笔者的解答更为简洁。此外, 还要注意在由方程组化为一元五次方程的时候一定要仔细, 稍不注意便有可能计算出错, 功亏一策.

6. 给定不等腰的锐角 $\triangle A B C$, 记 $D, E, F$ 分别为 $A, B, C$ 向对边所引高线的垂足. 以 $A D$ 为直径的圆交 $D E, D F$ 于点 $M, N$. 在 $A B, A C$ 上取点 $P, Q$ 满足 $N P \perp A B, M Q \perp A C$. 最后, 记 $\odot I$ 为 $\triangle A P Q$ 的外接圆.

(1) 证明: $\odot I$ 与 $E F$ 相切;

(2) 设 $T$ 为 $\odot I$ 在 $E F$ 上的切点, $D T$ 与 $M N$ 交于点 $K, L$ 是 $A$ 关于 $M N$的对称点. 证明: $\triangle D K L$ 的外接圆过 $E F$ 与 $M N$ 的交点.

## 解法一 (马飞雁、陈奕宸)

(1) 过 $A$ 作 $A T \perp E F$ 于 $T$. 显然有 $A, F, N, T$ 与 $A, E, M, T$ 两组四点共

![](https://cdn.mathpix.com/cropped/2024_02_26_e3ec11798ed8a0a09fbeg-13.jpg?height=985&width=1034&top_left_y=193&top_left_x=517)

圆. 由于

$$
\begin{gathered}
\angle F N T=\angle F A T=90^{\circ}-\angle A C B, \\
\angle F N P=90^{\circ}-\angle N F P=90^{\circ}-\angle B P D=90^{\circ}-\angle A C B .
\end{gathered}
$$

故 $N, P, T$ 共线. 同理 $M, Q, T$ 共线, 则 $\angle A P T=\angle A Q T=90^{\circ}$, 故 $A, P, Q, T$ 四点共圆且 $A T$ 为直径.

又 $A T \perp E F$, 故 $\odot I$ 与 $E F$ 相切.

(2) 记以 $A D$ 为直径的圆为 $\odot O_{1}$, 记 $\odot O_{1}$ 和 $A C$ 交于 $Y$, 和 $A B$ 交于 $X$. 故

$$
\angle F N T=\angle F A T=\angle F T N=\angle D A C=\angle D A Y .
$$

则 $N, T, Y$ 三点共线, 同理 $M, T, X$ 共线. 由于 $\angle F T N=\angle D A C=\angle N M T$, 故 $F T$ 为 $\triangle M N T$ 外接圆的一条切线.

记 $M N, E F$ 交于点 $Z$, 取 $W$ 为 $D T$ 和 $\triangle A P Q$ 外接圆的交点.

由于 $A T$ 为 $\triangle A P Q$ 外接圆的直径, 故 $\angle A W T=\angle A W D=90^{\circ}$, 则 $W$ 在 $\odot O_{1}$ 上.

由根心定理得 $\odot O_{1}, \triangle A P Q$ 外接圆, $\triangle M N T$ 外接圆两两的根轴 $A W, Z T, M N$交于一点, 即为 $Z$. 故 $Z, W, A$ 共线, 则

$$
\angle L Z K=\angle A Z K=90^{\circ}-\angle W K Z=\angle K D L .
$$

故 $K, L, D, Z$ 共圆, 即 $\triangle D K L$ 外接圆过 $E F, M N$ 的交点.

## 解法二 (AoPS) (1) 略.

(2) 设 $U$ 为 $M N$ 的中点, $Z$ 为 $E F$ 与 $M N$ 的交点.

由于 $[M, N ; K, Z]=[E, F ; T, Z]=-1$, 又因为 $U$ 是 $M N$ 的中点, 结合调和点列的性质, 则有:

$$
\overrightarrow{U K} \cdot \overrightarrow{U Z}=U N^{2}=U M^{2}=-\overrightarrow{U A} \cdot \overrightarrow{U D}=\overrightarrow{U L} \cdot \overrightarrow{U D} .
$$

即 $D, L, K, Z$ 四点共圆.

评注 这道几何题是一道中等难度的题, 或许将此题与第 4 题交换位置更为合适. 第一问证明相切, 一个不错的方法就是先找到切点, 再证明这一条直线垂直于经过该点的半径. 第二问难度稍高, 要求证明共圆的点较难刻画, 如果从纯几何的角度分析, 但若找到本题隐藏的圆, 想到根心定理, 找到本题的关键点 $W$点, 再加上一些角度的推导, 问题就迎刃而解了. 当然, 利用射影几何的观点, 也能洞察到此题的本质。事实上, 虽然这道题构图复杂, 但是模型较为常见, 解题方法也较为常规. 本题还有一些很多有意思的结论, 譬如, $L$ 点 $\triangle D M N$ 的垂心, $M N$ 与 $A C$ 的交点在过 $A N F T$ 的圆上等等,证明也不困难, 在此不做赘述.

7. 给定正整数 $n>1, T$ 是所有有序组 $(x, y, z)$ 组成的集合, 其中正整数 $x, y, z$ 互不相同, 且 $1 \leq x, y, z \leq 2 n$. 集合 $A$ 由一些有序对 $(u, v)$ 组成, 若对任意 $T$ 中的元素 $(x, y, z)$ 都有 $\{(x, y),(x, z),(y, z)\} \cap A \neq \varnothing$, 我们称 $A$ 与 $T$ 相连.

(1) 求 $T$ 中的元素个数;

(2) 证明: 存在一个与 $T$ 相连的集合, 且其恰有 $2 n(n-1)$ 个元素;

(3) 证明: 任意与 $T$ 相连的集合的元素个数都不少于 $2 n(n-1)$.

## 解 (马飞雁)

(1) 可知 $|T|=2 n(2 n-1)(2 n-2)=8 n^{3}-12 n^{2}+4 n$.

(2) 取 $A=\{(x, y) \mid 1 \leq x, y \leq n$ 或 $n+1 \leq x, y \leq 2 n, x \neq y\}$ 即满足题意.

(3) 取 $S=\{(u, v) \mid 1 \leq u \neq v \leq 2 n\}$, 则 $|S|=2 n(n-1)=4 n^{2}-2 n$.

利用反证法: 设存在一个元素个数少于 $2 n^{2}-2 n$ 的 $A$ 与 $T$. 则

$$
|A| \leq 2 n^{2}-2 n-1
$$

故 $\left|\complement_{S} A\right| \geq 2 n^{2}+1$. 下证此时 $\complement_{S} A$ 必有一个三元子集 $\{(x, y),(x, z),(y, z)\}$.

命题转化为在有 $2 n$ 个点 $\left(n \geq 2, n \in \mathbb{N}^{*}\right)$ 的有向图 $K$ 中, 若其中有不少于 $2 n^{2}+1$ 条有向边, 则一定存在一个如下图所示不循环的三阶完全图 $K_{3}$ (我们规定给定的两点之间只能连接至多一条同一方向的边).

![](https://cdn.mathpix.com/cropped/2024_02_26_e3ec11798ed8a0a09fbeg-15.jpg?height=329&width=305&top_left_y=201&top_left_x=881)

当 $n=2$ 时, 4 个点之间连有不少于 9 条有向边, 必有两点间连有双向有向边. 记为 $A \rightarrow B, B \rightarrow A$. 则 $A, B$ 两点和 $C, D$ 两点之间连有不少于 5 条边, $C, D$ 之中必有一个点向 $A$ 和 $B$ 共连出 3 条边, 不妨记为 $C$. 故 $C$ 向 $A, B$ 中一点连出两条边, 记为 $B \rightarrow C, C \rightarrow B$. 无论 $C A$ 方向如何, $A, B, C$ 均能组成满足要求的 $K_{3}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_e3ec11798ed8a0a09fbeg-15.jpg?height=349&width=300&top_left_y=999&top_left_x=884)

归纳假设 $n \leq k$ 时, $(*)$ 成立.

当 $n=k+1$ 时, 在 $2(k+1)$ 个点的有向图中连有 $2\left(k^{2}+1\right)^{2}+1$ 条有向边,则必有两点 (记为 $a, b)$ 之间连有双向边, 即 $a \rightarrow b, b \rightarrow a$. 在其余 $2 k$ 个点之间若连有不少于 $2 k^{2}+1$ 条有向边, 由归纳假设 $(*)$ 对 $n=k+1$ 也成立.

否则, 若这 $2 k$ 个点之间连有不多于 $2 k^{2}$ 条有向边, $a, b$ 两点和其余 $2 k$ 个点之间连有不少于 $\left(2(k+1)^{2}+1\right)-2-2 k^{2}=4 k+1$ 条边, 即其余 $2 k$ 个点中至少有一个点 $u$ 向 $a, b$ 连出了 3 条边. 易知 $(u, a, b)$ 为满足条件的 $K_{3},(*)$ 成立.

故 $\complement_{S} A$ 中必有一个三元子集 $\{(x, y),(x, z),(y, z)\}$, 即存在一个 $(x, y, z) \in T$使

$$
\{(x, y),(x, z),(y, z)\} \cap A=\varnothing .
$$

故 $A$ 与 $T$ 不相连, 矛盾!

则任意与 $T$ 相连的集合元素个数不少于 $2 n(n-1)$.

评注 利用反证法转化命题后容易看出, 题目中对于“相连”的描述中出现了子集族 $\{(x, y),(x, z),(y, z)\}$, 具有明显的方向性特征, 故考虑利用图论中的有向图描述和解决问题. 在讨论 $n=2$ 的情况中, 我们发现如果有一个外部点向目标
点连出 3 边即可迅速解决问题, 故在归纳证明中采用了类似的想法. 整体思路比较自然流畅。

## 参考文献

[1] Art of Problem Solving. 2020 Vietnam National Olympiad.[Z/OL]. https:// artof problemsolving.com/community/c1036575_2020_vietnam_national_olympiad. 2019.12.27

[2] 杨丕业. 第十一期. 2019 年越南 MO [Z/OL]. 微信公众号 “伪同文算學”. 2019.12.31.

