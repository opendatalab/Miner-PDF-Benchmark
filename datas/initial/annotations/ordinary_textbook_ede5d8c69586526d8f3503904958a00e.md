$$
\text { 数学新星网 } \% \text { 教师专栏 }
$$

www.nsmath.cn/jszl

# 2020 年 USEMO 试题解析 

石泽晖 ${ }^{2}$ 董子超 $^{2}$

(1. 长春吉大附中实验学校, 130021；2. 卡内基梅隆大学, 15213)

USEMO 是美国数学奥林匹克 (USAMO) 的一个练习赛, 第 2 届 USEMO 于 2020 年 10 月 24 日、25 日两天进行. 本次比赛共 6 道题, 其中 $1,2,4,5$ 难度适中,较适合联赛训练; 3,6 较难, 适合国赛训练. 我们在下文中给出了这次 USEMO 的解答和评析, 请读者批评指正.

## I. 试 题

1. 求所有能被写成

$$
\frac{[x, y]+[y, z]}{[x, z]}
$$

形式的正整数, 其中 $x, y, z$ 是三个正整数, $[a, b]$ 是指正整数 $a, b$ 的最小公倍数.

2. 甲, 乙两人玩一个游戏. 首先, 乙选择集合 $\{1,2, \cdots, 2020\}$ 的一族子集 $\mathcal{F}$,并让甲知道这个子集族是什么. 然后, 甲和乙轮流从集合 $\{1,2, \cdots, 2020\}$ 中挑选数字, 已选过的数字不能再被挑选. 甲先挑选, 乙后挑选, 一直进行到所有数字都挑完为止 (即每人挑 1010 轮). 如果甲能挑完 $\mathcal{F}$ 中某个集合中的所有元素, 则甲赢, 否则乙赢. 试求所有能确保乙有必胜策略的 $\mathcal{F}$ 中, $|\mathcal{F}|$ 的最大可能值.
3. 在锐角 $\triangle A B C$ 中, $O, H$ 分别是外心和垂心. 记 $\Gamma$ 为 $\triangle A B C$ 的外接圆, $N$ 为 $O H$ 的中点. 考虑由 $\Gamma$ 在 $B, C$ 处的两条切线以及过点 $H$ 且垂直于 $A N$的直线组成的三角形, 并记该三角形的外接圆为 $\omega_{A}$, 类似定义 $\omega_{B}, \omega_{C}$. 证明: $\omega_{A}, \omega_{B}, \omega_{C}$ 的根心在 $O H$ 上.
4. 设函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$满足对任意 $x, y \in \mathbb{R}^{+}$, 都有

$$
f(x+f(y)+x y)=x f(y)+f(x+y) .
$$

证明: 对任意正实数 $x$, 均有 $f(x)=x$.

修订日期: 2021-02-07.

5. 凸 200 边形 $A_{1} A_{2} \cdots A_{200}$ 的所有边被相间地涂成了红蓝两色. 假设所有红边延长相交可以形成一个正 100 边形, 所有蓝边延长相交也可以形成一个正 100 边形. 证明: 凸 200 边形 $A_{1} A_{2} \cdots A_{200}$ 的 50 条对角线 $A_{1} A_{101}, A_{3} A_{103}, \cdots$, $A_{99} A_{199}$ 共点.
6. 证明: 对任意奇数 $n>1$, 均存在两个正整数 $a, b$, 使得多项式 $Q(x)=$ $(x+a)^{2}+b$ 同时满足如下三个条件:

(i) $(a, n)=(b, n)=1$;

(ii) $Q(0)$ 可以被 $n$ 整除;

(iii) $Q(1), Q(2), Q(3), \cdots$ 中每个数均有一个不能整除 $n$ 的素因子.

## II. 解 答

题 1 求所有能被写成

$$
\frac{[x, y]+[y, z]}{[x, z]}
$$

形式的正整数, 其中 $x, y, z$ 是三个正整数, $[a, b]$ 是指正整数 $a, b$ 的最小公倍数.

解 1 (沈月恒) 记 $d_{0}=(x, y, z), d_{1}=\frac{(y, z)}{d_{0}}, d_{2}=\frac{(x, z)}{d_{0}}, d_{3}=\frac{(x, y)}{d_{0}}$, 且

$$
x_{1}=\frac{x}{d_{0} d_{2} d_{3}}, y_{1}=\frac{y}{d_{0} d_{1} d_{3}}, z_{1}=\frac{z}{d_{0} d_{1} d_{2}},
$$

易知 $x_{1}, y_{1}, z_{1}$ 均为整数, 且两两互素. 这说明:

$$
[x, y]=x_{1} y_{1} d_{0} d_{1} d_{2} d_{3},[y, z]=y_{1} z_{1} d_{0} d_{1} d_{2} d_{3},[x, z]=x_{1} z_{1} d_{0} d_{1} d_{2} d_{3},
$$

由此可以得到:

$$
\frac{[x, y]+[y, z]}{[x, z]}=\frac{x_{1} y_{1}+y_{1} z_{1}}{x_{1} z_{1}}
$$

一方面, 若 $\frac{x_{1} y_{1}+y_{1} z_{1}}{x_{1} z_{1}}=m$ 为正整数, 则 $x_{1}\left|\left(x_{1} y_{1}+y_{1} z_{1}\right), z_{1}\right|\left(x_{1} y_{1}+y_{1} z_{1}\right)$,从而 $x_{1}\left|y_{1} z_{1}, z_{1}\right| x_{1} y_{1}$, 由 $x_{1}, y_{1}, z_{1}$ 两两互素可知: $x_{1}=z_{1}=1$, 从而

$$
\frac{[x, y]+[y, z]}{[x, z]}=m=2 y_{1}
$$

为偶数.

另一方面, 对任意的正偶数 $n=2 k$, 取 $x=1, y=k, z=1$, 则

$$
\frac{[x, y]+[y, z]}{[x, z]}=\frac{k+k}{1}=2 k=n
$$

这说明, 一切正偶数 $n$, 均能被写成 $\frac{[x, y]+[y, z]}{[x, z]}$ 形式.

结合以上两方面可知, 所有正偶数即为所求.
解 2 记 $v_{2}(x)=\alpha, v_{2}(y)=\beta, v_{3}(z)=\gamma$, 其中 $v_{2}(a)$ 为正整数 $a$ 的素因子 2 的个数.

首先, 我们证明: 若 $\frac{[x, y]+[y, z]}{[x, z]}$ 为正整数, 则其必为偶数.

由对称性, 不妨设 $\alpha \geq \gamma$. 分两种情况讨论:

(1) $\beta \geq \alpha$, 此时有 $\beta \geq \alpha \geq \gamma$. 易知

$$
v_{2}([x, y])=\max \left\{v_{2}(x), v_{2}(y)\right\}=\max \{\alpha, \beta\}=\beta
$$

同理

$$
v_{2}([y, z])=\max \left\{v_{2}(y), v_{2}(z)\right\}=\max \{\beta, \gamma\}=\beta .
$$

故

$$
v_{2}([x, y]+[y, z]) \geq \beta+1
$$

而 $v_{2}([x, z])=\max \left\{v_{2}(x), v_{2}(z)\right\}=\max \{\alpha, \gamma\} \leq \beta$, 因此

$$
v_{2}\left(\frac{[x, y]+[y, z]}{[x, z]}\right) \geq \beta+1-\beta=1,
$$

这说明 $\frac{[x, y]+[y, z]}{[x, z]}$ 为偶数.

(2) $\beta<\alpha$. 此时易知 $v_{2}([x, y])=\alpha, v_{2}([x, z])=\alpha$. 由 $\frac{[x, y]+[y, z]}{[x, z]}$ 为正整数, 可知 $v_{2}([y, z]) \geq \alpha$. 从而

$$
v_{2}([y, z])=\max \left\{v_{2}(y), v_{2}(z)\right\}=\max \{\beta, \gamma\} \geq \alpha
$$

注意到 $\alpha>\beta, \alpha \geq \gamma$, 故 $\alpha=\gamma$, 也即 $v_{2}([y, z])=\alpha$, 又 $v_{2}([x, y])=\alpha$, 故

$$
v_{2}([x, y]+[y, z]) \geq \alpha+1
$$

进而

$$
v_{2}\left(\frac{[x, y]+[y, z]}{[x, z]}\right) \geq \alpha+1-\alpha=1,
$$

这说明 $\frac{[x, y]+[y, z]}{[x, z]}$ 为偶数.

结合 $(1),(2)$ 可知, 若 $\frac{[x, y]+[y, z]}{[x, z]}$ 为正整数, 则其必为偶数.

其次, 对任意的正偶数 $n=2 k$, 取 $x=1, y=k, z=1$, 则

$$
\frac{[x, y]+[y, z]}{[x, z]}=\frac{k+k}{1}=2 k=n
$$

这说明一切正偶数 $n$ 均能被写成 $\frac{[x, y]+[y, z]}{[x, z]}$ 形式.

综上知, 所有正偶数即为所求.

评注 本题为简单题. 通过一些尝试探索不难猜到答案为全体正偶数并完成构造. 对于证明的部分, 一种较代数的想法是设出所有的最大公约数关系, 从而
代入化简表达式, 说明它只取偶数值; 另一种较组合的想法是对分子, 分母中素因子 2 的个数计数, 说明它只取偶数值. 在本题中, 两种解法皆奏效.

题 2 甲，乙两人玩一个游戏. 首先, 乙选择集合 $\{1,2, \cdots, 2020\}$ 的一族子集 $\mathcal{F}$, 并让甲知道这个子集族是什么. 然后, 甲和乙轮流从集合 $\{1,2, \cdots, 2020\}$ 中挑选数字, 已选过的数字不能再被挑选. 甲先挑选, 乙后挑选, 一直进行到所有数字都挑完为止 (即每人挑 1010 轮). 如果甲能挑完 $\mathcal{F}$ 中某个集合中的所有元素,则甲赢, 否则乙赢. 试求所有能确保乙有必胜策略的 $\mathcal{F}$ 中, $|\mathcal{F}|$ 的最大可能值.

解 (王孝文) 记集合 $S=\{1,2, \cdots, 2020\}$, 子集 $A_{i}=\{2 i-1,2 i\}(i=1,2$, $\cdots, 1010)$. 考虑子集族

$$
|\mathcal{F}|=\left\{A \mid A \subseteq S \text {, 且 } A_{1}, A_{2}, \cdots, A_{1010} \text { 中至少有一个是 } A \text { 的子集 }\right\} \text {. }
$$

首先, 我们计算 $|\mathcal{F}|$. 由 $\mathcal{F}$ 的定义可知: 对 $\mathcal{F}$ 中每个元素 $A$, 均存在最小的 $i$,使得 $A_{i}=\{2 i-1,2 i\} \subseteq A$. 而对每个最小的 $i$, 集合 $A_{j}=\{2 j-1,2 j\}(1 \leq j<i)$中的两个元素有 3 种满足 $i$ 为最小的取法: 均不取, 或任取其一. 而集合 $S$ 中每个大于 $2 i$ 的元素可取可不取, 共 2 种取法, 均能满足 $A$ 的定义. 故对每一个 $i(1 \leq i \leq 1010)$, 共对应了 $3^{i-1} \cdot 2^{2020-2 i}$ 个 $A$. 因此:

$$
|\mathcal{F}|=\sum_{i=1}^{1010} 3^{i-1} \cdot 2^{2020-2 i}=2^{2018} \cdot \sum_{i=0}^{1009}\left(\frac{3}{4}\right)^{i}=2^{2020}-3^{1010}
$$

其次, 给出此时乙的必胜策略: 当甲挑选 $2 i-1(1 \leq i \leq 1010)$ 时, 乙就挑选 $2 i(1 \leq i \leq 1010)$; 当甲挑选 $2 i(1 \leq i \leq 1010)$ 时, 乙就挑选 $2 i-1(1 \leq i \leq 1010)$.事实上, 由子集族 $\mathcal{F}$ 的定义可知, 对每个集合 $A \in \mathcal{F}$, 均存在一个 $i \leq i \leq$ 1010), 使得 $A_{i}=\{2 i-1,2 i\} \subseteq A$. 由乙的挑数策略可知, $A_{i}$ 中的两个元素中必有一个无法被甲取到, 故甲无法挑完 $\mathcal{F}$ 中任何一个集合的所有元素. 乙必胜.

最后, 我们证明所有满足条件的 $\mathcal{F}$, 均有 $|\mathcal{F}| \leq 2^{2020}-3^{1010}$.

考虑甲前 $k$ 次的挑选方式.

由于甲前 $k$ 次挑选共 $2020 \cdot(2020-2) \cdots(2020-2(k-1))$ 种选择. 而 $S$ 的任意 $k$ 元集合在以上选择中至多出现 $k$ ! 次 (全排列的种类数), 故甲至少能挑完

$$
\frac{2020 \cdot(2020-2) \cdots(2020-2(k-1))}{k !}=2^{k} \cdot \mathrm{C}_{1010}^{k}
$$

个 $k$ 元集合. 对 $k(1 \leq k \leq 1010)$ 如上考虑, 可得甲至少能挑出

$$
\sum_{k=0}^{1010} 2^{k} \mathrm{C}_{1010}^{k}=(2+1)^{1010}=3^{1010}
$$

个集合. 这说明 $|\mathcal{F}| \leq 2^{2020}-3^{1010}$.
综上, $|\mathcal{F}|$ 的最大值为 $2^{2020}-3^{1010}$.

评注 本题为中档题. 首先, 我们需要做较多的尝试探索猜出答案与构造, 一种可能的方式是将 2020 改成较小的数, 如 4,5,6,7,8 等等, 并试探乙选不同的子集族所得的结果. 在猜出答案后, 本题的证明也是不那么平凡的. 事实上, 我们计算了甲逐步所能控制的集合个数的下界, 进而估计了乙所选集合族的上界. 这个方法是自然的, 但是在思考问题的时候, 这样的贪心算法却容易被忽视. 本题的构造与证明浑然天成, 既出乎意料, 又合乎情理, 是一道难得的好题.

题 3 在锐角 $\triangle A B C$ 中, $O, H$ 分别是外心和垂心. 记 $\Gamma$ 为 $\triangle A B C$ 的外接圆, $N$ 为 $O H$ 的中点. 考虑由 $\Gamma$ 在 $B, C$ 处的两条切线以及过点 $H$ 且垂直于 $A N$的直线组成的三角形, 并记该三角形的外接圆为 $\omega_{A}$, 类似定义 $\omega_{B}, \omega_{C}$. 证明: $\omega_{A}, \omega_{B}, \omega_{C}$ 的根心在 $O H$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_f455f696a807f4908203g-05.jpg?height=831&width=853&top_left_y=1115&top_left_x=590)

证明 (邹听雨) 如图所示, 过 $H$ 作 $A N, B N, C N$ 的垂线, 分别交 $D E, D F, E F$于 $A_{2}, B_{1}, A_{1}, C_{2}, B_{2}, C_{1}$. 记 $\triangle A B C$ 的三边长分别为 $a, b, c$, 外接圆半径为 $R$.

记 $B C$ 中点 $M, A H$ 中点 $L$, 则由九点圆的性质可知 $L M$ 为 $\triangle A B C$ 九点圆的直径, 由九点圆与外接圆的位似比为 $1: 2$, 可知 $L M=R$. 由卡诺定理可知, $L M / / O A$. 所以 $L M \perp A B_{2}, M C \perp A H, N C \perp B_{2} H$, 从而有 $\triangle A H B_{2} \sim$ $\triangle M C N$. 同理有 $\triangle A H C_{1} \sim \triangle M B N$.

于是有 $\frac{A B_{2}}{A H}=\frac{N M}{M C}=\frac{R}{a}$, 注意到 $A H=2 O M=2 R \cos A$, 可知:

$$
A B_{2}=\frac{2 R^{2} \cos A}{a}=\frac{R \cos A}{\sin A}=R \cot A
$$

同理

$$
A C_{1}=R \cot A=A B_{2},
$$

以及

$$
B A_{1}=B C_{2}=R \cot B, C B_{1}=C A_{2}=R \cot C .
$$

设 $A H$ 交 $B C$ 于点 $U$, 下证 $A_{1}, U, E$ 三点共线. 容易知道

$$
\begin{gathered}
A_{1} D=B D-B A_{1}=R \tan A-R \cot B \\
D E=D C+C E=R \tan A+R \tan B \\
C U=b \cos C=2 R \sin B \cos C, B U=2 R \sin C \cos B
\end{gathered}
$$

故

$$
\begin{aligned}
\frac{B A_{1}}{A_{1} D} \cdot \frac{D E}{E C} \cdot \frac{C U}{U B} & =\frac{R \cot B}{R(\tan A-\cot B)} \cdot \frac{R(\tan A+\tan B)}{R \tan B} \cdot \frac{2 R \sin B \cos C}{2 R \sin C \cos B} \\
& =\frac{(\tan A+\tan B) \cot B \cot C}{(\tan A-\cot B) \tan B \cot B} \\
& =\frac{\tan A+\tan B}{\tan A \tan B-1} \cdot \cot C=1,
\end{aligned}
$$

在 $\triangle B C D$ 中应用 Menelaus 定理的逆定理, 可得 $A_{1}, U, E$ 三点共线. 同理, $A_{2}, U, F$ 三点共线.

又易知 $\angle F B U=\angle E C U$, 且

$$
\frac{F B}{B U}=\frac{R \tan C}{2 R \sin C \cos B}=\frac{1}{2 \cos B \cos C},
$$

同理

$$
\frac{E C}{C U}=\frac{1}{2 \cos B \cos C},
$$

故 $\triangle F B U \sim \triangle E C U$, 从而 $\angle D F U=\angle D E U$, 故 $E, F, A_{1}, A_{2}$ 四点共圆, 于是

$$
D A_{1} \cdot D F=D A_{2} \cdot D E
$$

这说明 $D$ 在 $\omega_{B}, \omega_{C}$ 的根轴上.

设 $D U$ 交 $E F$ 于 $X$, 则

$$
\begin{aligned}
\frac{F X}{X E} & =\frac{D F \sin \angle X D F}{D E \sin \angle X D E}=\frac{R(\tan A+\tan C)}{R(\tan A+\tan B)} \cdot \frac{B U}{U C} \\
& =\frac{(\tan A+\tan C) \cot B}{(\tan A+\tan B) \cot C}=\frac{\tan A \tan C-1}{\tan A \tan B-1} \\
& =\frac{\tan C-\cot A}{\tan B-\cot A}=\frac{R(\tan C-\cot A)}{R(\tan B-\cot A)}=\frac{F C_{1}}{E B_{2}} .
\end{aligned}
$$

由比例性质可知

$$
\frac{F X}{X E}=\frac{F C_{1}}{E B_{2}}=\frac{C_{1} X}{B_{2} X}
$$

于是

$$
F X \cdot B_{2} X=E X \cdot C_{1} X
$$

这说明 $X$ 在 $\omega_{B}, \omega_{C}$ 的根轴上. 故 $D U$ 为 $\omega_{B}, \omega_{C}$ 的根轴. 同理: $E V$ 为 $\omega_{A}, \omega_{C}$的根轴, $F W$ 为 $\omega_{A}, \omega_{B}$ 的根轴. 由蒙日定理可得: $D U, E V, F W$ 三线共点于 $\omega_{A}, \omega_{B}, \omega_{C}$ 的根心, 亦为 $\triangle D E F$ 与 $\triangle U V W$ 的位似中心. 再注意到 $O$ 为 $\triangle D E F$的内心, $H$ 为 $\triangle U V W$ 的内心, 由位似可知: $\omega_{A}, \omega_{B}, \omega_{C}$ 的根心在 $O H$ 上.

评注 本题为难题. 首先图中有很多垂直, 可以考虑用垂直导出相似, 进而通过计算确定 $A_{1}$ 等点的具体位置; 其次由精确图发现两组共线, 并可以通过计算证明, 从而确定根轴上的一个点 $D$; 再次由精确图可知 $U$ 也在根轴上, 但不好直接证明, 于是考虑作出 $D U$ 上另一点 $X$, 转而证明 $X$ 在根轴上, 从而刻画出根轴; 最后我们通过熟知的位似完成证明。

题 4. 设函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$满足对任意 $x, y \in \mathbb{R}^{+}$, 都有

$$
f(x+f(y)+x y)=x f(y)+f(x+y) .
$$

证明: 对任意正实数 $x$, 均有 $f(x)=x$.

证明 1 (沈月恒) 我们分几步完成证明:

若存在某个 $y_{0}>0$ 使得 $f\left(y_{0}\right)<y_{0}$, 取 $x=1-\frac{f\left(y_{0}\right)}{y_{0}}, y=y_{0}$ 得 $x f(y)=0$, 这与 $x>0, f(y)>0$ 矛盾! 因此, 我们得到

结论 1 对任意正实数 $y$, 均有 $f(y) \geq y$.

定义 $g(x)=f(x)-x$, 则由结论 1 知 $g(x)$ 的值域为 $[0,+\infty)$. 此时 (1) 式可化为

$$
g(x+y+x y+g(y))=(x-1) g(y)+g(x+y) .
$$

由 $x, y$ 的任意性, 交换 $x, y$ 得

$$
g(x+y+x y+g(x))=(y-1) g(x)+g(x+y) .
$$

将 (2),(3)式作差得

$$
g(x+y+x y+g(y))-(x-1) g(y)=g(x+y+x y+g(x))-(y-1) g(x)
$$

对任意正实数 $x, y$ 均成立.
因此, 若 $g(x)=g(y)$, 则有

$$
(x-1) g(y)=(y-1) g(x) \text {. }
$$

这说明

结论 2 若互异的正实数 $a, b$, 使得 $g(a)=g(b)$, 则 $g(a)=g(b)=0$.

在 (2) 式中, 代入 $x=1$ 得

$$
g(g(y)+2 y+1)=g(y+1)
$$

对任意正实数 $y$ 均成立. 由于 $g(y) \geq 0$, 我们发现 $g(y)+2 y+1>y+1$. 从而由结论 2 得 $g(y+1)=0$ 对任意正实数 $y$ 均成立. 因此, 我们得到

结论 3 对任意实数 $y>1$, 均有 $g(y)=0$.

在 (2) 式中, 代入任意 $x=x_{0}>1$, 则 $x_{0}+y+x_{0} y+g(y)>1$, 由结论 2 知

$$
0=g\left(x_{0} y+x_{0}+y+g(y)\right)=\left(x_{0}-1\right) g(y)+g\left(x_{0}+y\right)
$$

对任意正实数 $y$ 均成立. 因为 $g$ 非负, 且 $x_{0}>1$, 所以 $g(y)=g\left(x_{0}+y\right)=0$ 对任意正实数 $y$ 均成立, 这就完成了证明.

证明 2 同法一, 我们得到结论 1, 及 (2) 式. 接下来我们采用反证法证明.

若存在正实数 $y_{0}$, 使得 $g\left(y_{0}\right)>0$, 在 $(2)$ 式中, 令 $y=y_{0}$, 则

$$
\lim _{x \rightarrow+\infty} g(x)=\lim _{x \rightarrow+\infty} g\left(x\left(1+y_{0}\right)+\left(g\left(y_{0}\right)+y_{0}\right)\right) \geq \lim _{x \rightarrow+\infty}(x-1) g\left(y_{0}\right),
$$

故

$$
\lim _{x \rightarrow+\infty} g(x)=+\infty
$$

在 $(2)$ 式中, 令 $x=1$, 可得

$$
g(g(y)+2 y+1)=g(y+1) \text {. }
$$

在 (3) 式中, 令 $y=x-1$, 得

$$
g(g(x-1)+2 x-1)=g(x) .
$$

取如下序列 $\left\{x_{n}\right\}_{n=1}^{+\infty}$ :

$$
x_{1}=2, x_{n+1}=g\left(x_{n}-1\right)+2 x_{n}-1(n \geq 1) \text {. }
$$

反复利用 (4) 式可得: $g\left(x_{1}\right)=g\left(x_{1}\right)=g\left(x_{3}\right)=\cdots$ 为定值, 不妨记该定值为 $c$.

注意到 $g(x) \geq 0$, 故 $x_{n+1} \geq 2 x_{n}-1(n \geq 1)$, 而 $x_{1}=2$, 故序列 $\left\{x_{n}\right\}_{n=1}^{+\infty}$ 单调递增, 且 $\lim _{n \rightarrow+\infty} x_{n}=+\infty$.

由 $\lim _{x \rightarrow+\infty} g(x)=+\infty$ 可知, 存在 $M$, 使得 $\forall x \geq M$, 均有 $g(x)>c$; 由于
$\lim _{n \rightarrow+\infty} x_{n}=+\infty$, 故存在 $x_{n}>M$, 因此 $g\left(x_{n}\right)>c$. 这与 $g\left(x_{n}\right)$ 为定值 $c$ 矛盾.

综上, 对任意正实数 $x$, 都有 $f(x)=x$.

评注 本题为中档题. 一方面, 我们从条件出发. 函数的定义域中没有 0 , 考虑 $x=1, y=1, x=y$ 等等较特殊的取值看起来也不太能较好地化简条件得到信息. 注意到条件式两边的每一项都有 $f$, 所以我们尝试能否消掉其中的一些项.在这个尝试的过程中, 我们便不难得到结论 1 . 另一方面, 我们从结论出发, 作代换 $g(x)=f(x)-x$ 是自然的, 而代入条件式后发现 $g$ 的关系中关于 $x, y$ 的对称性较高, 所以我们尝试交换 $x, y$ 作差, 消掉大部分项, 我们便得到了结论 2 . 事实上, 结论 2 很好用, 因为有了它, 我们配凑 $g(a)=g(b)$ 就能得到大量信息, 于是完成证明就不难了. 法二我们尝试用分析语言说明问题。一方面易知 $g(x)$ 无上界, 另一方面在得到 $g(x)$ 不是单射后, 通过迭代得到一个单调递增无上界, 且 $g(x)$ 在其上为定值的子序列 $\left\{x_{n}\right\}_{n=1}^{+\infty}$, 从而产生矛盾.

题 5. 凸 200 边形 $A_{1} A_{2} \cdots A_{200}$ 的所有边被相间地涂成了红蓝两色. 假设所有红边延长相交可以形成一个正 100 边形, 所有蓝边延长相交也可以形成一个正 100 边形. 证明: 凸 200 边形 $A_{1} A_{2} \cdots A_{200}$ 的 50 条对角线 $A_{1} A_{101}, A_{3} A_{103}, \cdots$, $A_{99} A_{199}$ 共点.

证明 不妨记所有红边延长相交构成的正 100 边形为 $X_{1} X_{2} \cdots X_{100}$, 所有蓝边延长相交构成的正 100 边形为 $Y_{1} Y_{2} \cdots Y_{100}$, 且

$$
X_{i} X_{i+1} \cap Y_{i} Y_{i+1}=A_{2 i-1}=B_{i}, i=1,2, \cdots, 100
$$

这里下标 $\bmod 100$ 处理. (为简单化, 我们以 10 替代 100 作如下示意图)

![](https://cdn.mathpix.com/cropped/2024_02_26_f455f696a807f4908203g-09.jpg?height=696&width=694&top_left_y=1905&top_left_x=681)
设这两个正 100 边形的旋转相似中心为 $O$, 我们断定 $B_{1} B_{51}, B_{2} B_{52}, \cdots$, $B_{50} B_{100}$ 必共点于 $O$. 为此, 我们证明更强结论:

对任意 $i=1,2, \cdots, 100$, 均有 $\angle B_{i} O B_{i+1}=\frac{\pi}{50}$, 这里 $B_{101}=B_{1}$.

事实上, 注意到 $O$ 为旋转相似中心, 故有

$$
\triangle X_{i} O X_{i+1} \sim \triangle Y_{i} X Y_{i+1}
$$

由此可知

$$
\angle X_{i+1} B_{i} Y_{i+1}=\angle X_{i+1} O Y_{i+1}
$$

这说明 $O, B_{i}, Y_{i+1}, X_{i+1}$ 共圆.

同理可知 $O, B_{i}, X_{i}, Y_{i}$ 共圆, 从而有 $O, B_{i}, Y_{i+1}, B_{i+1}, X_{i+1}$ 共圆, 因此

$$
\begin{aligned}
\angle B_{i} O B_{i+1} & =\pi-\angle B_{i} Y_{i+1} B_{i+1} \\
& =\pi-\angle Y_{i} Y_{i+1} Y_{i+1} \\
& =\pi-\frac{49}{50} \pi=\frac{\pi}{50}, i=1,2, \cdots, 100
\end{aligned}
$$

故 $B_{1} B_{51}, B_{2} B_{52}, \cdots, B_{50} B_{100}$ 共点于 $O$, 也即 $A_{1} A_{101}, A_{3} A_{103}, \cdots, A_{99} A_{199}$ 共点于 $O$. 证毕!

评注 本题为中档题. 首先题中的 100 边形是无法画图的, 这样的几何问题并不常见. 在解题过程中, 我们只好试着将 100 改成 $3,4,5$ 等较小的数作图, 并尝试在图形中发掘重要的巧合. 值得一提的是, 要证明 100 条直线共点, 所共的点很可能是某种巧合点, 如果观察图中的一个局部 $B_{10} B_{1} B_{2} X_{1} X_{2} Y_{1} Y_{2}$, 我们发现这是相交两圆的经典构型, 于是圆 $\left(B_{1} Y_{1} X_{1} B_{10}\right)$ 与圆 $\left(B_{1} X_{2} Y_{2} B_{2}\right)$ 的异于 $B_{1}$ 的交点 $O$ 便关联了丰富的旋转位似信息，它就是 “高度可疑”的共点处. 事实上，我们切换视角, 改变 $O$ 的定义方式, 即考虑两个 100 边形的旋转位似中心, 就可以一劳永逸的解决问题. 另外, 本题的共点证明部分, 也可以通过复数法计算.

题 6. 证明：对任意奇数 $n>1$, 均存在两个正整数 $a, b$, 使得多项式 $Q(x)=(x+a)^{2}+b$ 同时满足如下三个条件:

(i) $(a, n)=(b, n)=1$;

(ii) $Q(0)$ 可以被 $n$ 整除;

(iii) $Q(1), Q(2), Q(3), \cdots$ 中每个数均有一个不能整除 $n$ 的素因子.

证明 设 $n$ 的所有素因子从小到大依次为 $p_{1}, p_{2}, \cdots, p_{k}$, 我们分几步完成证明.
结论 1 存在素数 $q_{1}, q_{2}, \cdots, q_{k}$, 使得对任意 $1 \leq i \leq k$, 有

$$
\left(\frac{p_{j}}{q_{i}}\right)=\left\{\begin{array}{l}
1(j \neq i) \\
-1(j=i)
\end{array}\right.
$$

证明 任取一个 $\bmod p_{j}(1 \leq j \leq k)$ 的二次剩余 $d_{j}$, 和一个 $\bmod p_{j}$ 的非二次剩余 $e_{j}$. 由中国剩余定理及 Dirichlet 定理, 存在素数 $q_{i}$ 满足以下同余方程组

$$
\left\{\begin{array}{l}
q_{i}=1 \quad(\bmod 4), \\
q_{i}=e_{i} \quad\left(\bmod p_{i}\right), \\
q_{i}=d_{j} \quad\left(\bmod p_{j}\right)(j \neq i) .
\end{array}\right.
$$

结合二次互反律, 有

$$
\begin{gathered}
\left(\frac{p_{j}}{q_{i}}\right)=\left(\frac{q_{i}}{p_{j}}\right) \cdot(-1)^{\frac{\left(p_{j}-1\right)\left(q_{i}-1\right)}{4}}=\left(\frac{q_{i}}{p_{j}}\right)=\left(\frac{d_{j}}{p_{j}}\right)=1(j \neq i), \\
\left(\frac{p_{i}}{q_{i}}\right)=\left(\frac{q_{i}}{p_{i}}\right) \cdot(-1)^{\frac{\left(p_{i}-1\right)\left(q_{i}-1\right)}{4}}=\left(\frac{q_{i}}{p_{i}}\right)=\left(\frac{e_{i}}{p_{i}}\right)=-1 .
\end{gathered}
$$

证毕!

令 $b=m q_{1} q_{2} \cdots q_{k}$, 其中正整数 $m$ 满足同余方程组

$$
m \equiv-\frac{d_{i}}{q_{1} q_{2} \cdots q_{k}} \quad\left(\bmod p_{j}\right)(j=1,2, \cdots, k)
$$

结论 2 对上述 $b$, 只存在有限个正整数 $x$, 使得 $x^{2}+b$ 的素因子均在 $\left\{p_{1}, p_{2}, \cdots, p_{k}\right\}$ 中.

证明 设 $x^{2}+b=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}$,于是

$$
\left(\frac{p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}}{q_{1}}\right)=\left(\frac{p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}}{q_{2}}\right)=\cdots=\left(\frac{p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}}{q_{k}}\right)=1 .
$$

由结论 1 可知

$$
\left(\frac{p_{1}^{\alpha_{1}}}{q_{1}}\right)=\left(\frac{p_{2}^{\alpha_{2}}}{q_{2}}\right)=\cdots=\left(\frac{p_{k}^{\alpha_{k}}}{q_{k}}\right)=1
$$

注意到 $\left(\frac{p_{i}}{q_{i}}\right)=-1(1 \leq i \leq k)$, 故

$$
(-1)^{\alpha_{1}}=(-1)^{\alpha_{2}}=\cdots=(-1)^{\alpha_{k}}=1
$$

这说明

$$
\alpha_{1} \equiv \alpha_{2} \equiv \cdots \equiv \alpha_{k} \equiv 0 \quad(\bmod 2),
$$

因此

$$
x^{2}+b=\left(p_{1}^{\frac{\alpha_{1}}{2}} p_{2}^{\frac{\alpha_{2}}{2}} \cdots p_{k}^{\frac{\alpha_{k}}{2}}\right)^{2} \geq(x+1)^{2},
$$

从而 $x \leq \frac{b-1}{2}$. 故只存在有限个正整数 $x$ 满足条件. 证毕!

由结论 2 可知, 对充分大的正整数 $x, x^{2}+b$ 均有不整除 $n$ 的素因子.
结论 3 存在正整数 $a$, 使得 $a^{2}+b \equiv 0(\bmod n)$.

证明 我们证明更强结论：

对任意的 $1 \leq i \leq k$, 以及正整数 $l$, 存在正整数 $a$, 使得 $a^{2}+b \equiv 0\left(\bmod p_{i}^{l}\right)$.

我们对 $l$ 采用数学归纳法进行证明.

$l=1$ 时, 由于 $\left(\frac{-b}{p_{i}}\right)=\left(\frac{-m q_{1} q_{2} \cdots q_{k}}{p_{i}}\right)=\left(\frac{d_{i}}{p_{i}}\right)=1$, 故存在 $a$, 使得 $a^{2}+b \equiv 0$ $\left(\bmod p_{i}^{l}\right)$.

若 $l$ 时结论成立, 设正整数 $a$ 满足 $a^{2}+b \equiv 0\left(\bmod p_{i}^{l}\right)$. 则 $l+1$ 时, 考虑如下 $p_{i}$ 个数:

$$
a^{2}+b,\left(a+p_{i}^{l}\right)^{2}+b, \cdots,\left(a+\left(p_{i}-1\right) p_{i}^{l}\right)^{2}+b
$$

它们均为 $p_{i}^{l}$ 的倍数, 且 $\bmod p_{i}^{l+1}$ 的余数互不相同, 故恰有 1 个是 $p_{i}^{l+1}$ 的倍数.故 $l+1$ 时结论也成立. 由数学归纳法可知结论对任意正整数 $l$ 均成立.

将 $n$ 标准分解, 对其每一个素因子的幕次, 应用更强结论, 即可知结论 3 成立. 证毕!

由结论 2 及结论 3 , 可知存在正整数 $a, b$, 使得 $a^{2}+b \equiv 0(\bmod n)$, 且对于 $x \geq a, x^{2}+b$ 均有不整除 $n$ 的素因子. 又由 $b$ 的定义及结论 3 , 显然有 $(a, n)=(b, n)=1$, 故存在符合题意的正整数 $a, b$. 证毕!

评注 本题为难题, 需要了解二次互反律并具备很强的数论综合分析能力.一种可能的思考方式为从结构简单的 $n$ 入手考虑, 如 $n=p, n=p^{2}, n=p q$ (这里 $p, q$ 均为素数). 这些思考启发我们找寻素数 $q_{1}, q_{2} \cdots, q_{k}$ 使得勒让德符号 $\left(\frac{n}{q_{i}}\right)$只与 $v_{p_{i}}(n)$ 有关, 进而导出关键的结论 2. 此后问题便不难解决了.

