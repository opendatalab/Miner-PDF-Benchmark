数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 第 41 届环球城市数学竞赛秋季赛试题解析 

$$
\text { 王广廷 }
$$

(上海市上海中学, 200231)

环球城市数学竞赛始于 1980 年的莫斯科-基辅-里加三市邀请赛, 现已成为一个有上百个城市参加的国际性比赛. 从 1982 年开始. 每届举行两季比赛: 秋季赛和春季赛. 每季分为初级 ( $\mathrm{O}$ 水平) 和高级 ( $\mathrm{A}$ 水平) 两轮, 其中 $A$ 水平的部分问题题目新颖, 值得研究和欣赏. 我们选取了 2019 秋季赛 $A$ 水平的 7 个问题给出了解答和评析.

## I. 试 题

1. 多项式 $P(x, y)$ 满足: 对任意非负整数 $n, P(n, y)$ 和 $P(x, n)$ 中的每一个要么为零, 要么为次数不超过 $n$ 的多项式. 问: 多项式 $P(x, x)$ 的次数是否可能为奇数?
2. 三角形 $A B C$ 是一个锐角三角形, 点 $A^{\prime}, B^{\prime}, C^{\prime}$ 分别在边 $B C, C A, A B$ 上,线段 $A A^{\prime}, B B^{\prime}, C C^{\prime}$ 交于三角形 $A B C$ 内部一点 $P$. 以 $A A^{\prime}, B B^{\prime}, C C^{\prime}$ 为直径作圆, 在每个圆内, 过点 $P$ 作垂直于直径的弦, 若所有的弦长相等. 求证： $P$ 为三角形 $A B C$ 的垂心.
3. 有 100 枚外观完全相同的硬币, 分为金银铜三种类型, 每种类型至少一枚. 每枚金币重 3 克, 每枚银币重 2 克,每枚铜币重 1 克. 现有一个无砝码的天平, 允许称重不超过101 次, 如何分辨出每一枚硬币的材质?
4. 考虑如下正数递增数列:

$$
\cdots<a_{-2}<a_{-1}<a_{0}<a_{1}<a_{2}<\cdots .
$$

其中两边都有无穷项. 对一个正整数 $k$, 该序列中任何连续 $k$ 项的和除以这 $k$ 项
中最大的一项的比值的最小上界记为整数 $b_{k}$. 证明: 序列 $b_{1}, b_{2}, b_{3}, \cdots$ 要么是正整数列 $1,2,3, \cdots$, 要么从某项开始是常数.

5. 已知凸四边形 $A B C D$ 内部有一点 $M$ 满足, 点 $M$ 到直线 $A B$ 和到直线 $C D$ 的距离相等, 点 $M$ 到直线 $B C$ 和直线 $A D$ 的距离也相等. 四边形 $A B C D$的面积等于 $M A \cdot M C+M B \cdot M D$. 求证:

(1) 四边形 $A B C D$ 存在内切圆;

(2) 四边形 $A B C D$ 存在外接圆.

6. 一个由 $(2 N)^{3}$ 个单位立方体组成的立方体被若干平行于它的边的针穿过(每根针恰好穿过 $2 N$ 个单位立方体). 每个单位立方体被至少一根针穿过. 称这些针的某个子集是”正则的”，如果这个这个集合中没有两根针穿过同一个单位立方体。

(1) 证明: 存在一个由 $2 N^{2}$ 根针组成的正则子集, 使得其中所有的针要么都是同一个方向, 要么有两个不同的方向;

(2) 求正则子集的元素个数最大值的最小可能值.

7. 将整数 $1,2,3, \cdots, n$ 中的一部分染为红色, 使得对每个红色数的三元组 $(a, b, c)$ (不必不同), 如果 $a(b-c)$ 是 $n$ 的倍数, 则 $b=c$. 证明:红色数的个数不超过 $\varphi(n)$. (注: 对正整数 $n, \varphi(n)$ 表示 $1,2, \cdots, n$ 中与 $n$ 互素的数的个数.)

## II. 解 答

题 1 多项式 $P(x, y)$ 满足: 对任意非负整数 $n, P(n, y)$ 和 $P(x, n)$ 中的每一个要么为零, 要么为次数不超过 $n$ 的多项式. 问: 多项式 $P(x, x)$ 的次数是否可能为奇数?

解 $P(x, x)$ 的次数不可能为奇数.

事实上, 我们可以归纳证明: 对每个非负整数 $t, P(x, y)$ 可写成如下形式:

$$
\begin{aligned}
P(x, y)= & x y(x-1) \cdots(x-t)(y-1) \cdots(y-t) T(x, y) \\
& +\sum_{i=1}^{t} a_{i} x y(x-1) \cdots(x-i+1)(y-1) \cdots(y-i+1)+a_{0}
\end{aligned}
$$

其中 $a_{i}(0 \leq i \leq t)$ 是复数, $T(x, y)$ 是复系数多项式.

对 $t$ 进行归纳.

当 $t=0$ 时, 在 $P(x, y)$ 中取 $n=0$, 结合条件知, $P(0, x)$ 和 $P(x, 0)$ 均为常
数, 且该常数为 $P(0,0)=a_{0}$, 于是 $x y \mid\left(P(x, y)-a_{0}\right)$, 故存在多项式 $T(x, y)$, 使得

$$
P(x, y)=x y T(x, y)+a_{0}
$$

假设 $t-1$ 时结论成立, 下面考虑 $t$ 的情况. 由归纳假设知, $t-1$ 时

$$
\begin{aligned}
P(x, y)= & x y(x-1) \cdots(x-t+1)(y-1) \cdots(y-t+1) T(x, y) \\
& +\sum_{i=1}^{t-1} a_{i} x y(x-1) \cdots(x-i+1)(y-1) \cdots(y-i+1)+a_{0} .
\end{aligned}
$$

上式结合条件: 多项式 $P(t, y)$ 和 $P(y, t)$ 为常数 0 或者次数不超过 $t$, 则 $T(t, y)$和 $T(y, t)$ 均为常数且该常数等于 $P(t, t)=a_{t}$, 于是

$$
T(x, y)=a_{t}+(x-t)(y-t) T^{\prime}(x, y)
$$

所以

$$
\begin{aligned}
P(x, y)= & x y(x-1) \cdots(x-t)(y-1) \cdots(y-t) T(x, y) \\
& +\sum_{i=1}^{t} a_{i} x y(x-1) \cdots(x-i+1)(y-1) \cdots(y-i+1)+a_{0} .
\end{aligned}
$$

故 $t$ 时命题成立, 由归纳法知 $P(x, y)$ 可写成形如 $(*)$ 的形式.

由于 $P(x, y)$ 次数有限. 设 $\operatorname{deg} P(x, y)=N$, 则取 $u=\left\lceil\frac{1}{2} N\right\rceil$, 则根据前面的证明, 有

$$
\begin{aligned}
P(x, y)= & x y(x-1) \cdots(x-u)(y-1) \cdots(y-u) T(x, y) \\
& +\sum_{i=1}^{u} a_{i} x y(x-1) \cdots(x-i+1)(y-1) \cdots(y-i+1)+a_{0} .
\end{aligned}
$$

则 $T(x, y)=0$, 否则 $\operatorname{deg} P>N$. 从而

$$
P(x, y)=\sum_{i=1}^{u} a_{i} x y(x-1) \cdots(x-i+1)(y-1) \cdots(y-i+1)+a_{0} .
$$

取最大的 $m \leq u$, 使得 $a_{m} \neq 0$, 则 $P(x, x)$ 的次数为 $2 m$ 是偶数.

所以, $P(x, x)$ 的次数不可能为奇数.

评注 这个问题的关键是先猜想 $P(x, y)$ 的表达式. 从特殊情况出发, 通过 $t=0$ 和 $t=1$ 的情况就能猜出 $P(x, y)$ 的表达式, 然后再用归纳法证明即可.

题 2 三角形 $A B C$ 是一个锐角三角形, 点 $A^{\prime}, B^{\prime}, C^{\prime}$ 分别在边 $B C, C A, A B$上, 线段 $A A^{\prime}, B B^{\prime}, C C^{\prime}$ 交于三角形 $A B C$ 内部一点 $P$. 以 $A A^{\prime}, B B^{\prime}, C C^{\prime}$ 为直径作圆, 在每个圆内, 过点 $P$ 作垂直于直径的弦, 若所有的弦长相等. 求证: $P$
为三角形 $A B C$ 的垂心.

![](https://cdn.mathpix.com/cropped/2024_02_26_bc9b884f6abfc99f06c0g-04.jpg?height=588&width=780&top_left_y=291&top_left_x=638)

证明 由条件知

$$
P A \cdot P A^{\prime}=P B \cdot P B^{\prime}=P C \cdot P C^{\prime},
$$

因此由相交弦定理得 $A, B, A^{\prime}, B^{\prime} ; A, C, A^{\prime}, C^{\prime} ; B, C, B^{\prime}, C^{\prime}$ 分别四点共圆. 所以

$$
\angle A A^{\prime} C=\angle A C^{\prime} C=\angle A B^{\prime} B=\angle A A^{\prime} B
$$

所以

$$
\angle A A^{\prime} C=\angle A A^{\prime} B=90^{\circ},
$$

即 $A A^{\prime} \perp B C$.

同理可得 $B B^{\prime} \perp A C, C C^{\prime} \perp A B$. 故点 $P$ 是三角形 $A B C$ 的垂心.

评注 这是个简单题, 只需注意到由相交弦定理得到四点共圆即可.

题 3 有 100 枚外观完全相同的硬币, 分为金银铜三种类型, 每种类型至少一枚. 每枚金币重 3 克, 每枚银币重 2 克, 每枚铜币重 1 克. 现有一个无砝码的天平, 允许称重不超过101 次, 如何分辨出每一枚硬币的材质?

解 (黄凤麟) 首先任取两枚硬币, 不妨设硬币重量为 $a, b$, 若 $a=b$, 则丢掉其中一枚硬币, 再任取一枚硬币与前面留下的硬币比较重量, 重复该操作, 直至得到两枚质量分别为 $a<b$ 的硬币为止.

(1) 若此时只剩一枚重量为 $c$ 硬币, 其中 $c \neq a, c \neq b$. 将 $\{c, a\},\{c, b\}$ 各称重一次, 即可分辨出所有硬币, 此时共称重 100 次.

(2) 若此时剩下至少两枚硬币. 对剩下的这些硬币也进行上述操作, 可得到重量为 $c<d$ 的两枚硬币. 下面对 $a+b$ 和 $c+d$ 称重,

(i) 若 $a+b=c+d$, 则有 $a=c, b=d$, 丢掉 $c, d$, 继续重复上述操作;
(ii) 若 $a+b<c+d$, 则 $a=1, d=3$. 继续比较 $b, d$ 的大小, 若 $b=d$, 则 $a<c<d$. 若 $b<d$, 则 $a<b<d$.

此时, 我们都找到了重为 2 克的硬币. 将剩下的硬币与 2 克的硬币比较重量即可分辨出所有的硬币, 且操作次数不超过 101.

综合 (1),(2) 可知, 原问题成立.

评注 这是一个比较常规的问题, 容易看出 100 和 101 可以用 $n$ 和 $n+1$ 代替, 问题的关键在于确定重量为 2 克的硬币, 然后再将剩下的硬币与之比较即可. 在寻找重量为 2 克的硬币的过程中，遇到重量相同的硬币是可以直接忽略的 (因为用一次称量确定一枚硬币是恰好的), 因而只剩下有限的情况, 一一枚举即可.

题 4 考虑如下正数递增数列:

$$
\cdots<a_{-2}<a_{-1}<a_{0}<a_{1}<a_{2}<\cdots .
$$

其中两边都有无穷项. 对一个正整数 $k$, 该序列中任何连续 $k$ 项的和除以这 $k$ 项中最大的一项的比值的最小上界记为整数 $b_{k}$. 证明: 序列 $b_{1}, b_{2}, b_{3}, \cdots$ 要么是正整数列 $1,2,3, \cdots$, 要么从某项开始是常数.

证明 由条件得序列 $\left\{b_{k}\right\}$ 满足: $b_{1} \leq b_{2} \leq \cdots$ 以及 $b_{k} \leq k$.

若对任意整数 $k$, 都有 $b_{k}=k$, 则问题得证.

若存在正整数 $k$, 使得 $b_{k} \neq k$, 则 $b_{k} \leq k-1$. 下面说明序列 $\left\{b_{k}\right\}$ 有上界, 结合 $\left\{b_{k}\right\}$ 单调不减且 $\left\{b_{k}\right\}$ 均为整数, 知序列 $\left\{b_{k}\right\}$ 从某项开始是常数.

对任意正整数 $t$, 记 $S=\sum_{i \leq t} a_{i}$, 而每 $k$ 个连续项的和不超过最大数的 $k-1$倍, 则

$$
\begin{aligned}
S & \leq \sum_{i \leq t, i \equiv t(\bmod k)}(k-1) a_{i} \\
& =(k-1) a_{t}+\sum_{i<t, i \equiv t(\bmod k)}(k-1) a_{i} \\
& <(k-1) a_{t}+\sum_{i<t, i \equiv t(\bmod k)} \frac{k-1}{k}\left(a_{i}+\cdots+a_{i+k-1}\right) \\
& =(k-1) a_{t}+\frac{k-1}{k}\left(S-a_{t}\right) .
\end{aligned}
$$

则

$$
\frac{1}{k} S<\frac{(k-1)^{2}}{k} a_{t}
$$

即

$$
S<(k-1)^{2} a_{t}
$$

由 $t$ 的任意性可知, 对任意的正整数 $i$, 有 $b_{i}<(k-1)^{2}$, 即序列 $b_{i}$ 有上界. 原问题得证.

评注 容易想到用反证法证明该问题. 注意到数列 $\left\{b_{n}\right\}$ 单调不减, 要证明 $\left\{b_{n}\right\}$ 最终为常数列, 只需证明 $\left\{b_{n}\right\}$ 有上界即可. 由 $n$ 的任意性, 只需证明 $\frac{\sum_{i \leq t} a_{i}}{a_{t}}$有界即可. 剩下的任务就是不等式的放缩.

题 5. 已知凸四边形 $A B C D$ 内部有一点 $M$ 满足, 点 $M$ 到直线 $A B$ 和到直线 $C D$ 的距离相等, 点 $M$ 到直线 $B C$ 和直线 $A D$ 的距离也相等. 四边形 $A B C D$的面积等于 $M A \cdot M C+M B \cdot M D$. 求证:

(1) 四边形 $A B C D$ 存在内切圆;

(2) 四边形 $A B C D$ 存在外接圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_bc9b884f6abfc99f06c0g-06.jpg?height=548&width=691&top_left_y=1251&top_left_x=685)

证明 (1) 如图, 作 $M A_{1} \perp A B, M B_{1} \perp B C, M C_{1} \perp C D, M D_{1} \perp D A$, 只需证明 $M A_{1}=M B_{1}=M C_{1}=M D_{1}$.

设 $\angle A M A_{1}=\alpha_{1}, \angle B M A_{1}=\alpha_{2}, \angle B M B_{1}=\beta_{1}, \angle B_{1} M C=\beta_{2}, \angle C M C_{1}=$ $\theta_{1}, \angle D M C_{1}=\theta_{2}, \angle D M D_{1}=\gamma_{1}, \angle D_{1} M A=\gamma_{2}$.

注意到 $M A_{1}=M C_{1}$, 我们有

$$
\begin{aligned}
S_{\triangle C M C_{1}}+S_{\triangle A M A_{1}} & =\frac{1}{2} M C \cdot M C_{1} \sin \theta_{1}+\frac{1}{2} M A \cdot M A_{1} \sin \alpha_{1} \\
& =\frac{1}{2} M C \cdot M A_{1} \sin \theta_{1}+\frac{1}{2} M A \cdot M C_{1} \sin \alpha_{1} \\
& =\frac{1}{2} M C \cdot M A \cos \alpha_{1} \sin \theta_{1}+\frac{1}{2} M A \cdot M C \cos \theta_{1} \sin \alpha_{1} \\
& =\frac{1}{2} M A \cdot M C\left(\cos \alpha_{1} \sin \theta_{1}+\cos \theta_{1} \sin \alpha_{1}\right)
\end{aligned}
$$

$$
=\frac{1}{2} M A \cdot M C \sin \left(\theta_{1}+\alpha_{1}\right)
$$

同理可得

$$
\begin{aligned}
& S_{\triangle D M C_{1}}+S_{\triangle B M A_{1}}=\frac{1}{2} M A \cdot M C \sin \left(\theta_{2}+\alpha_{2}\right), \\
& S_{\triangle D M D_{1}}+S_{\triangle B M B_{1}}=\frac{1}{2} M B \cdot M D \sin \left(\beta_{1}+\gamma_{1}\right), \\
& S_{\triangle A M D_{1}}+S_{\triangle C M B_{1}}=\frac{1}{2} M A \cdot M C \sin \left(\beta_{2}+\gamma_{2}\right) .
\end{aligned}
$$

将上述四式相加得

$S_{A B C D}=\frac{1}{2} M A \cdot M C\left(\sin \left(\theta_{1}+\alpha_{1}\right)+\sin \left(\theta_{2}+\alpha_{2}\right)\right)+\frac{1}{2} M B \cdot M D\left(\sin \left(\beta_{1}+\gamma_{1}\right)+\sin \left(\beta_{2}+\gamma_{2}\right)\right.$.

结合题目条件 $S_{A B C D}=M A \cdot M C+M B \cdot M D$ 以及三角函数的有界性知

$$
\sin \left(\theta_{1}+\alpha_{1}\right)=\sin \left(\theta_{2}+\alpha_{2}\right)=\sin \left(\beta_{1}+\gamma_{1}\right)=\sin \left(\beta_{2}+\gamma_{2}\right)=1
$$

于是,

$$
\theta_{1}+\alpha_{1}=\theta_{2}+\alpha_{2}=\beta_{1}+\gamma_{1}=\beta_{2}+\gamma_{2}=90^{\circ}
$$

所以

$$
\frac{M A_{1}}{M B_{1}}=\frac{\cos \alpha_{2}}{\cos \beta_{1}}=\frac{M C_{1}}{M D_{1}}=\frac{\cos \theta_{2}}{\cos \gamma_{1}}=\frac{\sin \alpha_{2}}{\sin \beta_{1}}
$$

故 $\tan \alpha_{2}=\tan \beta_{1}$, 于是 $\alpha_{2}=\beta_{1}$, 故 $M A_{1}=M B_{1}=M C_{1}=M D_{1}$, 即四边形 $A B C D$ 有内切圆.

(2) 注意到 $\angle A B C+\angle A D C=180^{\circ}-\angle A_{1} M B_{1}+180^{\circ}-\angle C_{1} M D_{1}=$ $360^{\circ}-\left(\alpha_{2}+\theta_{2}\right)-\left(\beta_{1}+\gamma_{1}\right)=180^{\circ}$, 故四边形 $A B C D$ 有外接圆.

评注 要证明四边形 $A B C D$ 有内切圆, 只需证明点 $M$ 到四条边的距离相等. 由于条件中已知四边形 $A B C D$ 的面积表达式, 我们要做的就是用另一种方式把 $A B C D$ 的面积表示出来, 因此想到把四边形 $A B C D$ 的面积表示为四组三角形的面积之和, 于是就得到了相应的角的关系，问题就很容易得到证明.

题 6. 一个由 $(2 N)^{3}$ 个单位立方体组成的立方体被若干平行于它的边的针穿过(每根针恰好穿过 $2 N$ 个单位立方体). 每个单位立方体被至少一根针穿过.称这些针的某个子集是”正则的”，如果这个这个集合中没有两根针穿过同一个单位立方体。

(1) 证明: 存在一个由 $2 N^{2}$ 根针组成的正则子集, 使得其中所有的针要么
都是同一个方向, 要么有两个不同的方向;

(2) 求正则子集的元素个数最大值的最小可能值.

## 证明 (李逸凡、颜川皓)

(1) 采用反证法, 假设结论不成立.

由于同一个方向的所有针显然构成一个正则子集, 故每个方向上的针数小于 $2 N^{2}$. 对两个方向, 比如 $x, y$ 方向, 则在每个 $z=k$ 的层上可取 $x$ 方向和 $y$ 方向上针数较多的一边的所有针.

记 $z=k$ 时, $x$ 方向上有 $x_{k}$ 根针, $y$ 方向上有 $y_{k}$ 根针. 则由反证法假设可知, $\sum_{k=1}^{2 N} \max \left\{x_{k}, y_{k}\right\}<2 N^{2}$, 从而由抽屉原理, 知存在某个正整数 $k$, 满足 $\max \left\{x_{k}, y_{k}\right\} \leq N-1$, 即 $x_{k} \leq N-1, y_{k} \leq N-1$. 此时, 这一层上其余的方块都必须由 $z$ 方向的针来覆盖, 因此 $z$ 方向上的所有针包含一个 $(N+1) \times(N+1)$的子阵.

由对称性, 知 $x$ 方向和 $y$ 方向上有同样的这样的子阵.

假设 $z$ 方向上已有 $(N+i) \times(N+i)$ 的子阵, 设为 $x=1,2, \cdots, N+i$ 与 $y=1,2, \cdots, N+i$, 则在 $x=1,2, \cdots, N+i$ 的层中每层可至少取出 $z$ 方向上的 $N+i$ 根针. 设此时 $x=k(N+i+1 \leq k \leq 2 N)$ 的层上 $y$ 方向的针有 $\widetilde{y_{k}}$ 根, $z$方向的针有 $\widetilde{z_{k}}$ 根, 则由反证法假设

$$
(N+i)^{2}+\sum_{k=N+i+1}^{2 N} \max \left\{\widetilde{y_{k}}, \widetilde{z_{k}}\right\}<2 N^{2}
$$

即

$$
\sum_{k=N+i+1}^{2 N} \max \left\{\widetilde{y_{k}}, \widetilde{z_{k}}\right\}<2 N^{2}-N^{2}-2 N i-i^{2}<(N-i)^{2}
$$

由抽屉原理, 知存在某个 $N+i+1 \leq k \leq 2 N$ 满足 $\widetilde{y_{k}} \leq N-i-1, \widetilde{z_{k}} \leq N-i-1$,故 $x$ 方向上的针存在 $(N+i+1) \times(N+i+1)$ 的子阵. 由对称性, $y, z$ 方向同理. 对 $i$ 归纳可得某个方向上的针包含 $\sqrt{2} N \times \sqrt{2} N$ 的子阵, 矛盾.

所以, 一定可以找出 $2 N^{2}$ 个元素的正则子集, 包含至多两个方向.

(2) 首先给出构造:

对 $x$ 方向, 取 $y, z$ 都在 $\{1,2, \cdots, N\}$ 中或都在 $\{N+1, N+2, \cdots, 2 N\}$ 中的共 $2 N^{2}$ 根针, 即下图阴影部分的所有针.

对 $y, z$ 方向的针取法类似.

此时, 可知每根针或与 $\{1,2, \cdots, N\}^{3}$ 的立方体相交(且恰穿过 $N$ 个方块),或与 $\{N+1, N+2, \cdots, 2 N\}^{3}$ 的立方体相交(且恰穿过 $N$ 个方块).

![](https://cdn.mathpix.com/cropped/2024_02_26_bc9b884f6abfc99f06c0g-09.jpg?height=451&width=585&top_left_y=234&top_left_x=724)

由于取出的任两根针穿过的方块不同, 且这两个立方体中共有 $2 N^{3}$ 个方块,故取出的针不能超过 $\frac{2 N^{3}}{N}=2 N^{2}$.

综上述所, 正则子集的元素个数的最大值的最小可能值为 $2 N^{2}$.

评注 这是一个有难度的问题, 题目的入手点在于运用反证法得到存在 $(N+1) \times(N+1)$ 的同方向的针阵. 整个题目的难点在于第二步, 需要注意到前面的做法具有推广的可能, 所以我们需要选择一个新的方向, 重复上述操作,直到不能继续操作下去为止, 这样就得到一个 $\sqrt{2} N \times \sqrt{2} N$ 的针阵, 从而导致矛盾. 在第一小问的提示下, 第二问就相对容易去处理, 按照最常规的构造就可以发现第一问的结果确实是最优的.

题 7. 将整数 $1,2,3, \cdots, n$ 中的一部分染为红色, 使得对每个红色数的三元组 $(a, b, c)$ (不必不同), 如果 $a(b-c)$ 是 $n$ 的倍数, 则 $b=c$. 证明: 红色数的个数不超过 $\varphi(n)$. (注: 对正整数 $n, \varphi(n)$ 表示 $1,2, \cdots, n$ 中与 $n$ 互素的数的个数.)

证明 (颜川皓) 对 $n$ 进行归纳.

当 $n=1$ 时, 显然成立.

当 $n$ 为素数时, $n$ 不能染为红色, 因为此时只需取 $a=n$ 就满足条件, $b, c$ 可任意取值, 可以不相等, 故 $n$ 为素数时也成立.

假设结论对小于 $n$ 时都成立, 下面考虑 $n$ 的情况.

设 $n=q^{\alpha} \cdot m$, 其中 $q$ 为 $n$ 的最大素因子, $m>1$.

若 $1,2,3, \cdots, n$ 中有一个 $q$ 的倍数为红色, 则模 $\frac{n}{q}$ 的剩余类中至多有一个为红色, 即红色数至多有

$$
\begin{aligned}
\frac{n}{q} & =n \cdot \frac{q-1}{q} \cdot \frac{q-2}{q-1} \cdots \frac{1}{2} \\
& =n \cdot\left(1-\frac{1}{q}\right)\left(1-\frac{1}{q-1}\right) \cdots\left(1-\frac{1}{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \leq n \cdot \prod_{p \text { 为素数,p|n }}\left(1-\frac{1}{p}\right) \\
& =\varphi(n) .
\end{aligned}
$$

结论成立.

下设没有 $q$ 的倍数为红色.

设 $A_{k}=\left\{x \equiv k\left(\bmod q^{\alpha}\right) \mid 1 \leq x \leq n\right\}, q$ 不整除 $k$, 则由

$$
n=q^{\alpha} \cdot m,(q, m)=1
$$

知 $A_{k}$ 的元素个数为 $m$, 且 $A_{k}$ 中的元素遍历模 $m$ 的完系, 由于对任意 $x, y \in A_{k}$,均有 $q^{\alpha} \mid(x-y)$. 而对任意 $x, y, z \in A_{k}$,

$$
n|z(x-y) \Leftrightarrow m| z(x-y) \text {, }
$$

且将 $A_{k}$ 中的数模 $m$ 即为 $1,2, \cdots, m$, 故可将 $A_{k}$ 中的数看做 $1,2, \cdots, m$. 则由归纳假设, 知 $A_{k}$ 中至多可取出 $\varphi(m)$ 个红色的数, 又 $q$ 不整除 $k$, 故共有 $\frac{q-1}{q} \cdot q^{\alpha} \cdot \varphi(m)=\varphi(n)$ 个数是红数. 故 $n$ 时命题成立.

综上可知, 原问题成立.

评注 本题要证的结论是 $\varphi(n)$ 这一数论函数, 在对应方法行不通之后, 考虑使用归纳法, 并利用 $\varphi(n)$ 是一个积性函数. 通过设出 $m$ 的形式, 只需去证明 $p$的倍数不是红色的数, 且每一个模 $m$ 的剩余类中至多有 $\varphi(n)$ 个数为红色. 后者由归纳假设可得, 若前者不成立, 又可导出至多有 $\varphi(n)$ 个红色数.

