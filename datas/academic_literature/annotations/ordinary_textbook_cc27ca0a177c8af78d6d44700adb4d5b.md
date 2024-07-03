数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2020 年环球城市竞赛春季 O 水平试题解析 

$$
\text { 王广廷 }
$$

(上海市上海中学, 200231)

环球城市数学竞赛始于 1980 年的莫斯科-基辅-里加三市邀请赛, 现已成为一个有上百个城市参加的国际性比赛. 从 1982 年开始. 每届举行两季比赛: 秋季赛和春季赛. 每季分为初级 ( $\mathrm{O}$ 水平)和高级 ( $\mathrm{A}$ 水平)两轮, 其中 $\mathrm{O}$ 水平的部分问题题目虽然相对容易, 但问题较为新颖. 我们选取了 2020 年春季 $\mathrm{O}$ 水平的 6 个问题给出了解答和评析.

## I. 试 题

1. 将 2020 个正整数排成一行, 其中任意相邻的三个数中, 第三个数都能被前两个数以及前两个数的和整除. 求最后一项的最小值.
2. 在锐角非等边三角形 $A B C$ 的三条高 $A D, B E, C F$ 上分别取点 $K, M, N$,使得 $A K=B M=C N=R$, 其中 $R$ 是 $\triangle A B C$ 的外接圆半径. 证明: $\triangle K M N$的圆心即为 $\triangle A B C$ 的内心.
3. 在一个无穷大的棋盘上, 有 40 个单元格被标记. 是否一定可以找出一个矩形, 使得其中被标记的单元格个数恰为 $20 ?$
4. 对无穷数列 $a_{1}, a_{2}, \cdots$, 设它的一阶差分为 $a_{n}^{\prime}=a_{n+1}-a_{n}$, 第 $k$ 阶差分为 $a_{n}^{(k)}=a_{n+1}^{(k-1)}-a_{n}^{(k-1)}$. 若一个数列本身及其所有的差分均为正数, 就称这个数列是 “好的”. 证明: 若数列 $a_{1}, a_{2}, \cdots ; b_{1}, b_{2}, \cdots$ 都是好的, 则数列 $a_{1} b_{1}, a_{2} b_{2}, \cdots$ 也是好的.
5. 在半径为 1 的球的球面上取一个球面三角形, 它的三条边均为球面上半径为 1 , 长度不超过 $\pi$ 的弧 (即这段弧所在的平面过球心), 其面积正好是球面积的 $\frac{1}{4}$. 证明: 将这个球面三角形复制 4 份, 可以覆盖整个球面.

修订日期: 2021-01-14.

6. 将 $N$ 个红色, 白色或蓝色的立方体放在圆圈上. 机器人从圆圈上的某个位置出发, 顺时针移动并执行如下操作, 直到只剩下一个立方体为止: 机器人摧毁自己前方最靠近自己的两个立方体, 并将一个立方体放置在自己身后, 该立方体的颜色由被摧毁的两个立方体决定：若这两个立方体暗色相同, 则被放置的立方体颜色与他们也相同, 若这两个立方体的颜色不同, 则被放置的立方体的颜色与它们均不同. 若放置好立方体后, 无论机器人从哪个位置出发, 最终得到的立方体颜色都不变, 就称这个放置法是“好的”. 若对整数 $N$, 所有的放置法都是“好的”, 就称 $N$ 是“成功的”. 求所有成功的 $N$.

## II. 解 答

题 1 将 2020 个正整数排成一行, 其中任意相邻的三个数中, 第三个数都能被前两个数以及前两个数的和整除. 求最后一项的最小值.

解 记这 2020 个正整数为 $a_{1}, a_{2}, \cdots, a_{2020}$, 则对任意的 $n \in\{3,4, \cdots, 2019\}$,记 $\frac{a_{n}}{a_{n-1}}=p_{n}$. 由题意得,

$$
a_{n}\left|a_{n+1}, a_{n}+a_{n-1}=\left(p_{n}+1\right) a_{n-1}\right| a_{n+1}
$$

所以,

$$
\left[a_{n},\left(p_{n}+1\right) a_{n-1}\right]=\left[a_{n-1} p_{n},\left(p_{n}+1\right) a_{n-1}\right]=a_{n-1} p_{n}\left(p_{n}+1\right)
$$

为 $a_{n+1}$ 的约数. 因此

$$
\frac{a_{n+1}}{a_{n}}=\frac{a_{n+1}}{a_{n-1}} \cdot \frac{a_{n-1}}{a_{n}} \geq p_{n}\left(p_{n}+1\right) \cdot \frac{1}{p_{n}}=p_{n}+1
$$

于是, $p_{n+1} \geq p_{n}+1$.

因为 $a_{2} \mid a_{3}$, 且若 $a_{2}=a_{3}$, 则 $a_{1}+a_{2}>a_{3}, a_{1}+a_{2} \nmid a_{3}$, 矛盾. 故 $a_{3}>a_{2}$,于是 $p_{3} \geq 2$, 故对任意 $n \in\{3,4, \cdots, 2020\}$, 有 $p_{n} \geq n-1$, 所以,

$$
a_{2020}=a_{2} p_{3} p_{4} \cdots P_{2020} \geq 1 \cdot 2 \cdots 2019=2019 ! .
$$

对 2020 个正整数 1,1 !, 2!, 3!, 4!, 一, 2019!, 前三项显然满足要求, 且任一项被前两项整除, 对任意正整数 $n, n !+(n+1) !=n !(1+n+1)=(n+2) n !$ 为 $(n+2) !$ 的约数, 则此 2020 个正整数满足题意.

综上可得, 最后一项的最小值为 2019 !.

评注 对小的情况做一些探索可知前 $n$ 项为 $1,1,2,6$ 时最佳. 发现规律得到答案为 $n$ ! 后考虑有 $a_{k}\left|a_{k+1}, a_{k}+a_{k-1}\right| a_{k+1}$, 用归纳发后得到 $\frac{a_{k+1}}{a_{k}}$ 的下界即可.
题 2 在锐角非等边三角形 $A B C$ 的三条高 $A D, B E, C F$ 上分别取点 $K, M, N$, 使得 $A K=B M=C N=R$, 其中 $R$ 是 $\triangle A B C$ 的外接圆半径. 证明: $\triangle K M N$ 的圆心即为 $\triangle A B C$ 的内心.

![](https://cdn.mathpix.com/cropped/2024_02_26_bfc80a05684a9f9e6686g-3.jpg?height=403&width=485&top_left_y=455&top_left_x=791)

证明 设点 $I$ 是三角形 $A B C$ 的内心, 因为 $\angle B A D=90^{\circ}-\angle A B C=\angle O A C$, $A K=O A=R$, 又 $\angle B A I=\angle C A I$, 所以 $\angle K A I=\angle O A I$, 于是点 $O, K$ 关于 $A I$ 对称, 所以 $O I=I K$.

同理可得, $I O=I M, I O=I N$.

所以, $I K=I N=I M$, 即点 $I$ 为 $\odot K M N$ 的圆心. 原问题得证.

评注 利用顶点与垂心、外心的等角线关系及题中边长等于 $R$ 的条件联想到对称. 作图发现点 $O$ 也在 $\odot K M N$ 上即得证.

题 3 在一个无穷大的棋盘上, 有 40 个单元格被标记. 是否一定可以找出一个矩形, 使得其中被标记的单元格个数恰为 20 ?

解 考虑如图标记的方格.

![](https://cdn.mathpix.com/cropped/2024_02_26_bfc80a05684a9f9e6686g-3.jpg?height=294&width=257&top_left_y=1829&top_left_x=905)

假设可以找出一个矩形, 在方阵中的子矩形为 $a$ 行 $b$ 列, 则 $20 \leq a b \leq 22$.下面分情况讨论:

(1) 若 $a b=20$, 由于行列均小于 10 , 因此, $\{a, b\}\{4,5\}$, 但任取 4 行 5 列或者 4 列 5 行均取到未标记的格, 不成立.

(2) 若 $a b=21$, 由于行列数均小于等于 7 , 于是 $\{a, b\}=\{3,7\}$, 而 $a \leq 7, b \leq$ 6 , 则 $a=7, b=3$, 如此取出子矩形中恰 1 个未取方格. 若取第 3 列, 则取 2 个.
若不取第三列, 则取不到, 矛盾.

(3) 若 $a b=22$, 但是 $a, b \leq 7$, 于是 11 不整除 $a b$, 矛盾.

综上可知, 假设不成立, 故不一定可以取出.

评注 本题的关键在于猜出可构造的例子, 将标记格限定在尽量小的区域 $(6 \times 7)$ 后只需考虑 $4 \times 5,3 \times 7$ 的情况, 稍作尝试即可.

题 4 对无穷数列 $a_{1}, a_{2}, \cdots$, 设它的一阶差分为 $a_{n}^{\prime}=a_{n+1}-a_{n}$, 第 $k$ 阶差分为 $a_{n}^{(k)}=a_{n+1}^{(k-1)}-a_{n}^{(k-1)}$. 若一个数列本身及其所有的差分均为正数,就称这个数列是 “好的”. 证明: 若数列 $a_{1}, a_{2}, \cdots ; b_{1}, b_{2}, \cdots$ 都是好的, 则数列 $a_{1} b_{1}, a_{2} b_{2}, \cdots$ 也是好的.

证明 因为 $a_{1}, a_{2}, \cdots ; b_{1}, b_{2}, \cdots$ 的零阶差分为正, 则 $a_{1}, a_{2}, \cdots ; b_{1}, b_{2}, \cdots$ 均为正数, 于是 $a_{1} b_{1}, a_{2} b_{2}, \cdots$ 也都为正数.

下面归纳证明: 对任意正整数 $k$, 对于一切好的 $a_{1}, a_{2}, \cdots ; b_{1}, b_{2}, \cdots$ 均有 $a_{1} b_{1}, a_{2} b_{2}, \cdots$ 的 $k$ 阶差分是正的.

当 $k=1$ 时, 对任意正整数 $i$, 由于 $a_{i+1}-a_{i}>0, b_{i+1}-b_{i}>0$, 因此, $a_{i+1} b_{i+1}>a_{i} b_{i}$, 即 $k=1$ 时成立.

假设数列 $a_{1} b_{1}, a_{2} b_{2}, \cdots$, 的小于 $k$ 阶差分为正. 下面考虑 $k$ 阶差分的情况.

由于对任意正整数 $i$, 有

$a_{i+1} b_{i+1}-a_{i} b_{i}=\frac{1}{2} b_{i}\left(a_{i+1}-a_{i}\right)+\frac{1}{2} b_{i+1}\left(a_{i+1}-a_{i}\right)+\frac{1}{2} a_{i}\left(b_{i+1}-b_{i}\right)+\frac{1}{2} a_{i+1}\left(b_{i+1}-b_{i}\right)$.

由于 $a_{1}, a_{2}, \cdots ; b_{1}, b_{2}, \cdots$ 是好的, 则数列 $\left\{a_{i+1}-a_{i}\right\},\left\{b_{i+1}-b_{i}\right\}$ 也是好的.由归纳假设 $\frac{1}{2} b_{1}, \frac{1}{2} b_{2}, \cdots ; a_{2}-a_{1}, a_{3}-a_{2} \cdots$ 均为好的, 则 $\frac{1}{2} b_{i}\left(a_{i+1}-a_{i}\right)$ 的 $k-1$阶差分为正. 对 $\frac{1}{2} b_{2}, \frac{1}{2} b_{3}, \cdots ; a_{2}-a_{1}, a_{3}-a_{2}, \cdots$ 用归纳假设, 知 $\frac{1}{2} b_{i+1}\left(a_{i+1}-a_{i}\right)$的 $k-1$ 阶差分为正. 同理可得 $\frac{1}{2} a_{i}\left(b_{i+1}-b_{i}\right), \frac{1}{2} a_{i+1}\left(b_{i+1}-b_{i}\right)$ 的 $k-1$ 阶差分也为正.

所以(注意到 $k$ 阶差分是可加的)

$$
\begin{aligned}
\left(a_{n} b_{n}\right)^{(k)}= & \left(\left(a_{n+1} b_{n+1}\right)^{(k-1)}-\left(a_{n} b_{n}\right)^{(k-1)}\right) \\
= & \left(\frac{1}{2} b_{n}\left(a_{n+1}-a_{n}\right)\right)^{(k-1)}+\left(\frac{1}{2} b_{n+1}\left(a_{n+1}-a_{n}\right)\right)^{(k-1)} \\
& \left(\frac{1}{2} a_{n}\left(a_{n+1}-b_{n}\right)\right)^{(k-1)}+\left(\frac{1}{2} a_{n+1}\left(b_{n+1}-b_{n}\right)\right)^{(k-1)} \\
> & 0 .
\end{aligned}
$$

即 $k$ 时, 命题成立.

综上可知, 对一切正整数 $k, a_{1} b_{1}, a_{2} b_{2}, \cdots$ 的 $k$ 阶差分是正的，从而 $a_{1} b_{1}, a_{2} b_{2}, \cdots$ 是好的.

评注 为了利用题目中的条件, 容易注意到只需将 $\left\{a_{i} b_{i}\right\}$ 的差分分拆为数列 $a_{i}, b_{i}$ 的差分之积的正项和之后利用归纳假设完成证明.

题 5. 在半径为 1 的球的球面上取一个球面三角形, 它的三条边均为球面上半径为 1 , 长度不超过 $\pi$ 的弧(即这段弧所在的平面过球心), 其面积正好是球面积的 $\frac{1}{4}$. 证明: 将这个球面三角形复制 4 份, 可以覆盖整个球面.

证明 (张贻然) 对球面上的任意三点 $A, B, C$, 记 $S(\widehat{A B}, \overparen{B C}, \overparen{C A})$ 表示 $\overparen{A B}, \overparen{B C}, \overparen{C A}$ 三条圆心为球心的弧在球面上围出的三角形的面积. 该题中的三角形均为球面三角形. 球心为 $O$.

设题中球面三角形为 $A B C$. 若 $A, A_{0}$ 为对径点, 对球面上的点 $X, Y$, 记 $S\left(\widehat{A X A_{0}}, \widehat{A Y A_{0}}, T\right)$ 表示两段弧在球面上围成的经过点 $T$ 的图形的面积. 由题意 $S(\overparen{A B}, \overparen{B C}, \overparen{C A})=\frac{1}{4}$. 不妨设点 $C$ 在平面 $A O B$ 的上方, 取 $\triangle A B C$ 内一点 $I$.

定义包含点 $W$ 的弧 $\widehat{X Y}, \overparen{X Z}$ 的夹角为其在过点 $X$ 的切平面上的投影向量为 $\overrightarrow{X Y}, \overrightarrow{X Z}$, 将 $\overrightarrow{X Y}$ 经过 $W$ 绕点 $X$ 转到 $\overrightarrow{X Z}$ 经过(所在平面包含球心 $O$ )的角度, 则夹角为 $\theta$ 的两段半圆弧围成的图形面积为球面的 $\frac{\theta}{2 \pi}(0<\theta<2 \pi)$ 倍.

首先证明:包含点 $I$ 的弧的夹角满足 $\angle A C B+\angle C B A+\angle B A C=360^{\circ}$.

事实上, 取 $A, B, C$ 的对径点 $A_{0}, B_{0}, C_{0}$, 则过点 $A$ 的每段以球心为圆心的弧过点 $A_{0}$, 对点 $B, C$ 有同样的结论.

![](https://cdn.mathpix.com/cropped/2024_02_26_bfc80a05684a9f9e6686g-5.jpg?height=480&width=456&top_left_y=1890&top_left_x=800)

由于 $A_{0}, B_{0}, C_{0}$ 为对径点, 所以 $\triangle A B C \cong \triangle A_{0} B_{0} C_{0}$, 于是 $S\left(\widehat{B A B_{0}}, \widehat{B C B_{0}}, I\right)+S\left(\widehat{C A C_{0}}, \widehat{C B C_{0}}, I\right)+S\left(\widehat{A B A_{0}}, \widehat{A C A_{0}}, I\right)$

$$
\begin{aligned}
= & 3 S(\widehat{A B}, \overparen{B C}, \overparen{C A})+S\left(\widehat{A B_{0}}, \overparen{B_{0} C}, \overparen{C A}\right)+S\left(\widehat{B C}, \overparen{C A_{0}}, \widehat{A_{0}} B\right)+S\left(\widehat{A B}, \widehat{B C_{0}}, \overparen{A C_{0}}\right) \\
= & 2 S(\widehat{A B}, \overparen{B C}, \overparen{C A})+S\left(\widehat{A B_{0}}, \overparen{B_{0} C}, \overparen{C A}\right)+S(\widehat{A B}, \overparen{B C}, \overparen{C A})+S\left(\widehat{B C}, \widehat{C A_{0}}, \widehat{A_{0} B}\right) \\
& +S\left(\widehat{A_{0} B_{0}}, \widehat{B_{0} C_{0}}, \widehat{A_{0} C_{0}}\right) \\
= & 2 S(\overparen{A B}, \overparen{B C}, \overparen{C A})+S=\frac{1}{2} S_{\text {球 }}+\frac{1}{2} S_{\text {球 }}=S_{\text {球. }} .
\end{aligned}
$$

所以, $\angle A C B+\angle C B A+\angle B A C=360^{\circ}$.

取弧 $\overparen{A B}$ 的中点 $M$, 以 $M O$ 为轴将球旋转 $180^{\circ}$, 此时, 点 $C$ 旋转至点 $C^{\prime}$, 于是 $C, O, C^{\prime}, M$ 四点共面, 由于 $\left(C, C^{\prime}\right),(A, B)$ 分别关于 $O M$ 对称, 所以 $\widehat{C^{\prime} A}=\overparen{C B}, \widehat{C^{\prime} B}=\widehat{C A}, \triangle A B C \cong \triangle B A C^{\prime}$. 取点 $M$ 的对径点 $M_{0}$, 则弧夹角 $\angle C A B+\angle C^{\prime} A B=\angle C A B+\angle C B A=360^{\circ}-\angle A C B$. 由弧 $\widehat{C C^{\prime}}$ 过点 $M_{0}$, 弧夹角 $\angle C A C^{\prime}\left(M_{0}\right.$ 在角内 $)=\angle A C B$, 且 $\overparen{A C}=\overparen{A C}, \overparen{A C^{\prime}}=\overparen{B C}$, 所以, $\triangle C A C^{\prime} \cong \triangle A C B$. 同理可得, $\triangle A C B \cong \triangle C B C^{\prime}$. 所以, 球面三角形复制 4 份,可覆盖整个球面.

原问题得证.

评注 注意到球面上三弧长固定的球面三角形形状固定. 不难想到覆盖只能利用球面上类似平移或者对称的操作完成, 然后再利用顶点三角形的全等来严谨的证明即可. 需注意曲边(弧)的夹角, 球面上的几何变换的表述要足够谨慎.

题 6. 将 $N$ 个红色, 白色或蓝色的立方体放在圆圈上. 机器人从圆圈上的某个位置出发, 顺时针移动并执行如下操作, 直到只剩下一个立方体为止: 机器人摧毁自己前方最靠近自己的两个立方体, 并将一个立方体放置在自己身后,该立方体的颜色由被摧毁的两个立方体决定：若这两个立方体暗色相同，则被放置的立方体颜色与他们也相同, 若这两个立方体的颜色不同, 则被放置的立方体的颜色与它们均不同. 若放置好立方体后, 无论机器人从哪个位置出发, 最终得到的立方体颜色都不变, 就称这个放置法是“好的”. 若对整数 $N$, 所有的放置法都是“好的”, 就称 $N$ 是“成功的”。求所有成功的 $N$.

解 (张贻然) 首先证明: 若 $N$ 为 2 的幂, 则 $N$ 是成功的.

事实上, 记 $N=2^{n}, n \in \mathbb{N}$. 当 $n=0$ 时, 显然成立, 下设 $n>0$, 若场上剩余 $2^{k}$ 个立方体, 记颜色为红、白、蓝的立方体各 $a_{k}, b_{k}, c_{k}, k \in \mathbb{N}^{*}$ 个. 机器人行动 $2^{k-1}$ 次, 每次将相邻的两个立方体变为一个立方体, 由于每次将前面两个立方体变为身后一个立方体, 则机器人行动 $2^{k-1}$ 次后每个原立方体均被摧毁, 每个新立方体均留存, 此时, 场上剩余 $2^{k-1}$ 个立方体. 记红、白、蓝各有
$a_{k-1}, b_{k-1}, c_{k-1}$ 个. 考虑这 $2^{k}+2^{k-1}$ 个立方体(包括新的以及原来的立方体), 若摧毁两个同色的立方体, 则又生成一个该颜色的立方体, 于是此颜色共被计数 3 次, 被 3 整除. 若摧毁两个异色的立方体, 则生成一个第三种颜色的立方体, 此时, 三种颜色均被计数 1 次. 所以,

$$
a_{k}+a_{k-1} \equiv b_{k}+b_{k-1} \equiv c_{k}+c_{k-1}(\bmod 3)
$$

由于若 $a_{k} \equiv b_{k}(\bmod 3)$, 则 $a_{k-1} \equiv b_{k-1}(\bmod 3)$, 最后可得 $a_{0} \equiv b_{0}(\bmod 3)$,于是 $a_{0}=b_{0}=0$, 则余下的立方体均为蓝色, 同理可得其余情形.

若初始时, 有 2 种颜色的立方体的个数模 3 相同, 则放置为好的, 而若 $a_{n}, b_{n}, c_{n}$ 两两模 3 不同余, $2^{n}=a_{n}+b_{n}+c_{n} \equiv 0+1+2 \equiv 0(\bmod 3)$, 矛盾.

所以, 一切放法都为好的, 即 $N$ 是成功的.

再证：对一切不为 2 的幂的 $N, N$ 不是成功的.

将 $N-1$ 个白色立方体和一个红色立方体放在圆上.

因为 $N$ 为正整数, 于是 $\left[\left\lceil\frac{N}{2}\right\rceil, N\right]$ 中有 2 的幂, 而 $N$ 不为 2 的幂, 因此, $\left[\left\lceil\frac{N}{2}\right\rceil, N-1\right]$ 中有 2 的幂, 不妨记为 $2^{\alpha}$, 则机器人由一处开始, 经过 $N-2^{\alpha}$ 次操作, 使得场上剩余 $2^{\alpha}$ 个立方体, 且起始位置前的一个立方体未被操作(这是由于 $\frac{N}{2} \neq 2^{\alpha}$, 则 $2^{\alpha}>\frac{N}{2}$ ). 因此, 由红立方体前放机器人, 仅第一次摧毁一个红立方体和一个立方体, 得到一个蓝立方体, 后面都是摧白毁两个白立方体得到一个白立方体. 所以, 剩余 $2^{\alpha}$ 个立方体时, 剩余 1 个蓝立方体及 $2^{\alpha}-1$ 个白立方体. 而由红立方体后放机器人, 每次摧毁两个白立方体放一个白立方体, 剩余一个红立方体及 $2^{\alpha}-1$ 个白立方体. 由于 $2^{\alpha}$ 个立方体不随机器人初始位置的改变最终立方体的颜色, 且对偶数 $\alpha, 2^{\alpha}-1 \equiv 0(\bmod 3)$. 两种情形初始 $\left(2^{\alpha}\right.$ 个立方体)时分别为 $a_{\alpha} \equiv b_{\alpha}(\bmod 3)$ 或者 $b_{\alpha} \equiv c_{\alpha}(\bmod 3)$, 最后为蓝、红立方体各一个. 对奇数 $\alpha, 2^{\alpha}-1 \equiv 1(\bmod 3)$, 两种情形初始 $\left(2^{\alpha}\right.$ 个立方体)时分别为 $c_{\alpha} \equiv b_{\alpha}(\bmod 3)$或者 $b_{\alpha} \equiv a_{\alpha}(\bmod 3)$, 最后为蓝、红立方体各一个. 故总有 $N$ 不是成功的.

综上可知, 一切成功的 $N=2^{n}, n \in \mathbb{N}$.

评注 此类操作问题需要寻找一个不变量. 将三种颜色编号为 $0,1,2$, 则容易注意到题中操作及模 3 意义下的加法再取负，也即场上有 $2^{k}$ 个立方体一轮操作后编号的和取相反数模 3. 试验较小的情况时, 可发现非 $2^{k}$ 的值是不行的. 利用对操作控制化归到 $2^{k}$ 例子容易给出反例.

