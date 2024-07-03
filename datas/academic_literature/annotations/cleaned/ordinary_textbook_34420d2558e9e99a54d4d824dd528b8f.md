数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2020 年中国集训队测试 (单挑赛) 试题解析 

金晟治

(浙江省温州中学, 325014)

指导教师: 邵达

2020 年, 受新冠肺炎疫情影响, 中国国家集训队测试不能如期举行, 改为直接根据冬令营成绩确定国家队名单, 而冬令营中并列第六的两名选手则举行了一场线上测试. 本场考试的题目形式非常新颖漂亮, 值得研究与欣赏. 笔者认为,第 $1,4,5$ 题相对容易, 第 $2,3,6$ 题比较困难且很有意思. 本文给出这场考试的试题及解答, 其中第三题的证明 2 来自海亮高级中学赵斌老师的公众号 “历经数学竞赛”, 第六题的证明 2 来自陈晨老师的公众号 “陈晨讲数学”. 直于水平, 不当之处在所难免, 敬请读者不吝赐教.

## I. 试 题

1. 设 $\omega$ 是 $n$ 次本原单位根. 复数 $a_{1}, a_{2}, \cdots, a_{n}$ 中有 $p$ 个非零. 记

$$
b_{k}=\sum_{i=1}^{n} a_{i} \omega^{k i}, \quad k=1,2, \cdots, n
$$

证明: 若 $p>0$, 那么复数 $b_{1}, b_{2}, \cdots, b_{n}$ 中非零元素个数不小于 $\frac{n}{p}$.

2. 在 $\triangle A B C$ 中, $A B=A C$. 过 $B C$ 的中点 $M$ 作一直线, 分别与线段 $A B$ 和 $C A$ 的延长线交于点 $D$ 和 $E$. 点 $F$ 在线段 $M E$ 上, 满足 $E F=D M$, 点 $K$ 在线段 $M D$ 上. 过点 $B, D, K$ 作圆 $\Gamma_{1}$, 过点 $C, E, K$ 作圆 $\Gamma_{2}$. 设圆 $\Gamma_{1}$ 与圆 $\Gamma_{2}$ 相交于点 $K$ 及另一点 $L$. 记 $\omega_{1}, \omega_{2}$ 分别为 $\triangle L D E, \triangle L K M$ 的外接圆. 证明:若 $\omega_{1}, \omega_{2}$ 关于点 $L$ 对称, 则 $B F \perp B C$.
3. 对有限正整数集 $A$, 定义 $\operatorname{lcm}(A)$ 是 $A$ 中元素的最小公倍数, $d(A)$ 是 $\operatorname{lcm}(A)$ 的素因子个数(记重数). 给定有限正整数集 $S$, 以及

$$
f_{S}(x)=\sum_{\emptyset \neq A \subseteq S} \frac{(-1)^{|A|} x^{d(A)}}{\operatorname{lcm}(A)} .
$$

修订日期: 2021-01-30.



证明: 若 $0 \leq x \leq 2$, 则 $-1 \leq f_{S}(x) \leq 0$.

4. 证明如下方程只有有限组正整数解 $(t, A, x, y, z)$ :

$\sqrt{t\left(1-A^{-2}\right)\left(1-x^{-2}\right)\left(1-y^{-2}\right)\left(1-z^{-2}\right)}=\left(1+x^{-1}\right)\left(1+y^{-1}\right)\left(1+z^{-1}\right)$.

5. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是 $1,2, \cdots, n$ 的排列, 求下式的最小值:

$$
\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\}
$$

6. 一个 $n$ 个顶点的简单连通图有 $m$ 条边. 证明: 可以找到 $m$ 种方法把它的顶点集分成两部分, 使得每部分对应的诱导子图是连通的.

## II . 解答与评注

1. 设 $\omega$ 是 $n$ 次本原单位根. 复数 $a_{1}, a_{2}, \cdots, a_{n}$ 中有 $p$ 个非零. 记

$$
b_{k}=\sum_{i=1}^{n} a_{i} \omega^{k i}, \quad k=1,2, \cdots, n
$$

证明: 若 $p>0$, 那么复数 $b_{1}, b_{2}, \cdots, b_{n}$ 中非零元素个数不小于 $\frac{n}{p}$.

证明 我们只需证明: 对于任意下标连续的 $p$ 个数 $b_{t+1}, b_{t+1}, \cdots, b_{t+p}$, 其中必有非零数. (下标 $\bmod n$ 理解)

假设存在 $t$, 使得 $b_{t+1}=b_{t+2}=\cdots=b_{t+p}=0$. 设 $a_{j_{1}}, a_{j_{2}}, \cdots, a_{j_{p}}$ 为 $a_{1}, a_{2}, \cdots, a_{n}$ 中的 $p$ 个非零数. 待定一组系数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{p}$, 有

$$
0=\sum_{k=1}^{p} \lambda_{k} b_{t+k}=\sum_{k=1}^{p} \lambda_{k} \cdot\left(\sum_{i=1}^{p} a_{j_{i}} \omega^{(t+k) j_{i}}\right)=\sum_{i=1}^{p} a_{j_{i}} \cdot\left(\sum_{k=1}^{p} \lambda_{k} \cdot\left(\omega^{j_{i}}\right)^{t+k}\right) .
$$

令

$$
f(x)=\sum_{k=1}^{p} \lambda_{k} x^{k-1}=\left(x-\omega^{j_{1}}\right)\left(x-\omega^{j_{2}}\right) \cdots\left(x-\omega^{j_{p-1}}\right)
$$

即取 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{p}$ 为上述 $f(x)$ 展开式中对应项的系数, 则

$$
f\left(\omega^{j_{i}}\right)=0,1 \leq i \leq p-1, f\left(\omega^{j_{p}}\right) \neq 0 .
$$

故

$$
0=\sum_{i=1}^{p} a_{j_{i}}\left(w^{j_{i}}\right)^{t+1} \cdot f\left(\omega^{j_{i}}\right)=a_{j_{p}}\left(\omega^{j_{p}}\right)^{t+1} \cdot f\left(\omega^{j_{p}}\right) \neq 0
$$

矛盾.

评注 本题想法比较简单, 要证明等于零的数不能太多, 矛盾可能与次数有关, 考虑下标连续的 $p$ 项就可能会得到与次数有关的限制. 这里我们将反证法得到的条件进行整体的处理, 和式重新整理后即可发现多项式的结构, 容易得到矛盾.

2. 在 $\triangle A B C$ 中, $A B=A C$. 过 $B C$ 的中点 $M$ 作一直线, 分别与线段 $A B$ 和 $C A$ 的延长线交于点 $D$ 和 $E$. 点 $F$ 在线段 $M E$ 上, 满足 $E F=D M$, 点 $K$ 在线段 $M D$ 上. 过点 $B, D, K$ 作圆 $\Gamma_{1}$, 过点 $C, E, K$ 作圆 $\Gamma_{2}$. 设圆 $\Gamma_{1}$ 与圆 $\Gamma_{2}$ 相交于点 $K$ 及另一点 $L$. 记 $\omega_{1}, \omega_{2}$ 分别为 $\triangle L D E, \triangle L K M$ 的外接圆. 证明:若 $\omega_{1}, \omega_{2}$ 关于点 $L$ 对称, 则 $B F \perp B C$.



证明 设 $B M$ 交圆 $\Gamma_{1}$ 于另一点 $Q, L M$ 交圆 $\Gamma_{1}$ 于另一点 $P, C K$ 交 $A M$ 于 $S, C K$ 交圆 $\Gamma_{1}$ 于 $T$.

我们依次证明如下结论:

$1^{\circ} B, P, S$ 共线; $2^{\circ} T, L, A$ 共线; $3^{\circ} E, L, Q$ 共线; $4^{\circ} T Q / / A C, T D / / B Q$.
$1^{\circ}$ 由 $\omega_{1}, \omega_{2}$ 关于 $L$ 对称及 $L$ 为两圆交点, 知 $\omega_{1}, \omega_{2}$ 相切于点 $L \Rightarrow \angle D L K=$ $\angle L E D+\angle L M K=\pi-\angle E L M \Rightarrow \angle D L K+\angle E L M=\pi \Rightarrow \angle E L K+\angle D L M=$ $\pi \Rightarrow \angle D B P=\angle D L M=\pi-\angle E L K=\angle A C K=\angle A C S=\angle A B S$, 即 $\angle A B P=\angle A B S$, 故 $B, P, S$ 共线.

$2^{\circ}$ 对圆内接六边形 $T L P B D K$, 由 Pascal 定理, 知 $T L$ 与 $B D$ 的交点与 $M, S$ 共线, 即 $T, L, A$ 共线.

$3^{\circ}$ 对圆内接六边形 $Q L T K D B$, 由 Pascal 定理, 知 $Q L$ 与 $D K$ 的交点与 $A, C$ 共线, 即 $E, L, Q$ 共线.

$4^{\circ} \angle Q T C=\angle Q L K=\angle E C T \Rightarrow T Q \| / A C \Rightarrow \angle T Q B=\angle A C B=$ $\angle D B Q \Rightarrow T D / / B Q$.

最后证明: $B F \perp B C$. 这等价于:

$$
M F=\frac{B M}{\cos \angle B M D} \Leftrightarrow D E=\frac{B M}{\sin \angle A M E}
$$

由 $\omega_{1}, \omega_{2}$ 半径相等及正弦定理, 知

$$
\frac{D E}{\sin \angle D L E}=\frac{L M}{\sin \angle L B D} .
$$

故只需证:

$$
\frac{B M}{\sin \angle A M E}=\frac{L M \cdot \sin \angle D L E}{\sin \angle L B D} \Leftrightarrow \frac{B M}{\sin \angle A M D}=\frac{L M \cdot \sin \angle A B C}{\sin \angle A T D} .
$$

结合

$$
\frac{\sin \angle A M D}{\sin \angle A T D}=\frac{\sin \angle B A M}{D M} \cdot \frac{A T}{\sin \angle A B C}, \quad B M=A B \cdot \sin \angle B A M,
$$

故只需证:

$$
\frac{A B}{L M}=\frac{A T}{D M} .
$$

而注意到

$$
\begin{aligned}
\frac{A T}{A B} & =\frac{A T}{A C}=\frac{\sin \angle A B S}{\sin \angle A T K}=\frac{D P}{L K} \\
\frac{D M}{L M} & =\frac{\sin \angle D L M}{\sin \angle L D M}=\frac{D P}{L K} \Rightarrow \frac{A T}{A B}=\frac{D M}{L M}
\end{aligned}
$$

故所证结论成立.

评注 本题有相当大的难度. 两圆关于某一个公共点对称的条件可以等价的拆分为相切与半径相等两个条件. 要证明的结论用 $M F=\frac{B M}{\cos \angle B M D}$ 来刻画, 于是想到可用简单的三角计算来解决, 半径相等的条件恰好可以通过正弦定理在三角计算中得到运用。而相切的条件则用角度来刻画，难点在于图形复杂，角度条件很难得到变化. 该解法的关键在于从角度关系出发, 发现第一组共线后, 以
这组共线为动机, 不断配 Pascal 定理的六个点, 每次将新得到的共线作为条件继续构造共线. 应当注意的是, Pascal 定理是一个很强的结果, 在得到足够多的共线条件后, 我们可以相信角度的条件应该已经得到较为充分的刻画, 足以使之后的三角计算完成。

3. 对有限正整数集 $A$, 定义 $\operatorname{lcm}(A)$ 是 $A$ 中元素的最小公倍数, $d(A)$ 是 $\operatorname{lcm}(A)$ 的素因子个数(记重数). 给定有限正整数集 $S$, 以及

$$
f_{S}(x)=\sum_{\emptyset \neq A \subseteq S} \frac{(-1)^{|A|} x^{d(A)}}{\operatorname{lcm}(A)} .
$$

证明: 若 $0 \leq x \leq 2$, 则 $-1 \leq f_{S}(x) \leq 0$.

证明 1 设 $\operatorname{lcm}(S)$ 所有素因子为 $p_{1}, p_{2}, \cdots, p_{t}, S=\left\{a_{1}, a_{2}, \cdots, a_{m}\right\}, a_{k}=$ $\prod_{i=1}^{t} p_{i}^{\alpha_{i}(k)}$. 设 $\frac{x}{p_{i}}=y_{i} \in[0,1](x \in[0,2]), z_{i}(k)=y_{i}^{\alpha_{i}(k)} \in[0,1], 1 \leq i \leq t, 1 \leq k \leq$ $m$,用 $[n]$ 表示集合 $\{1,2, \cdots, n\}$ ，则

$$
\begin{aligned}
f_{S}(x) & =\sum_{\emptyset \neq I \subseteq[m]}(-1)^{|I|} \cdot \prod_{i=1}^{t} y_{i}^{\max \left\{\alpha_{i}(k) \mid k \in I\right\}} \\
& =\sum_{\emptyset \neq I \subseteq[m]}(-1)^{|I|} \cdot \prod_{i=1}^{t} \min \left\{z_{i}(k) \mid k \in I\right\} .
\end{aligned}
$$

下面对 $m+t$ 归纳证明: $\forall z_{i}(k) \in[0,1], 1 \leq i \leq t, 1 \leq k \leq m$, 有

$$
X=\sum_{\emptyset \neq I \subseteq[m]}(-1)^{|I|} \cdot \prod_{i=1}^{t} \min \left\{z_{i}(k) \mid k \in I\right\} \in[-1,0]
$$

$t=1$ 或 $m=1$ 时命题显然.

下考虑 $m, t \geq 2$, 假设命题对 $<m+t$ 时成立.

考虑第 $t$ 维 $z_{t}(1), z_{t}(2), \cdots, z_{t}(m)$, 分别记为 $z_{1}, z_{2}, \cdots, z_{m}$. 不妨设 $1 \geq z_{1} \geq$ $z_{2} \geq \cdots \geq z_{m} \geq 0$. 在 $X$ 的求和式中, 对 $I$ 中的最大元 $l$ 分类, 有

$$
X=\sum_{l=1}^{m} z_{l} \cdot\left(-\sum_{\emptyset \subseteq I \subseteq[l-1]}(-1)^{|I|} \cdot \prod_{i=1}^{t-1} \min \left\{z_{i}(k) \mid k \in I \cup\{l\}\right\}\right)
$$

记上式中 $z_{l}$ 的系数为 $-C_{l}$, 记

$$
\mu_{l}=\prod_{i=1}^{t-1} z_{i}(l) \in[0,1]
$$

则

$$
C_{1}=\mu_{1}
$$

对 $l \geq 2$, 记

$$
z_{i}^{\prime}(k)=\min \left\{z_{i}(k), z_{i}(l)\right\} \in\left[0, z_{i}(l)\right] \quad(1 \leq k \leq l-1)
$$

则

$$
\begin{aligned}
C_{l} & =\sum_{\emptyset \subseteq I \subseteq[l-1]}(-1)^{|I|} \cdot \prod_{i=1}^{t-1} \min \left\{z_{i}^{\prime}(k) \mid k \in I\right\} \\
& =\mu_{l} \cdot\left(\sum_{\emptyset \subseteq I \subseteq[l-1]}(-1)^{|I|} \cdot \prod_{i=1}^{t-1} \min \left\{\left.\frac{z_{i}^{\prime}(k)}{z_{i}(l)} \right\rvert\, k \in I\right\}\right) .
\end{aligned}
$$

其中, $I=\emptyset$ 时, 定义 $\min \left\{z_{i}^{\prime}(k) \mid k \in I\right\}=z_{i}(l), \min \left\{\left.\frac{z_{i}^{\prime}(k)}{z_{i}(l)} \right\rvert\, k \in I\right\}=1$.

对 $l-1(\leq m), t-1$ 及 $\frac{z_{i}^{\prime}(k)}{z_{i}(l)} \in[0,1](1 \leq i \leq t-1,1 \leq k \leq l-1)$ 用归纳假设, 知

$$
\sum_{\emptyset \neq I \subseteq[l-1]}(-1)^{|I|} \cdot \prod_{i=1}^{t-1} \min \left\{\left.\frac{z_{i}^{\prime}(k)}{z_{i}(l)} \right\rvert\, k \in I\right\} \in[-1,0]
$$

故

$$
C_{l} \in\left[0, \mu_{l}\right]
$$

故

$$
\begin{aligned}
X & =-\sum_{l=1}^{m} C_{l} \cdot z_{l} \leq 0 \\
X & =-\sum_{l=1}^{m} C_{l} \cdot z_{l} \geq-\sum_{l=1}^{m} C_{l} \\
& =\sum_{l=1}^{m}\left(-\sum_{\emptyset \subseteq I \subseteq[l-1]}(-1)^{|I|} \cdot \prod_{i=1}^{t-1} \min \left\{z_{i}(k) \mid k \in I \cup\{l\}\right\}\right) \\
& =\sum_{\emptyset \neq I \subseteq[m]}(-1)^{|I|} \cdot \prod_{i=1}^{t-1} \min \left\{z_{i}(k) \mid k \in I\right\} \geq-1 .
\end{aligned}
$$

最后一个不等号用到了归纳假设. 故 $X \in[-1,0]$, 完成归纳过渡.

证明 2 设 $\operatorname{lcm}(S)$ 所有素因子为 $p_{1}, p_{2}, \cdots, p_{m}, S=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 则 $\frac{x}{p_{i}} \in[0,1]$. 定义事件 $B_{i, 1}, B_{i, 2}, \cdots B_{i, N_{i}}$, 其中 $N_{i}=v_{p_{i}}(\operatorname{lcm}(S)), 1 \leq i \leq m$. 要求这些事件两两独立, 且 $B_{i, j}$ 发生的概率为 $\frac{x}{p_{i}}, 1 \leq i \leq m, 1 \leq j \leq N_{i}$.

对 $A \subseteq S$, 设 $\operatorname{lcm}(A)=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{m}^{\alpha_{m}}, \alpha_{i} \in \mathbb{Z}_{\geqslant 0}$. 定义事件 $X_{A}$ 为所有事件 $B_{i, j}\left(1 \leq i \leq m, 1 \leq j \leq \alpha_{i}\right)$ 同时发生 (其余事件随意, 若 $\alpha_{i}=0$, 相当于对 $B_{i, j}$ 无要求). 则

$$
P\left(X_{A}\right)=\frac{x^{d(A)}}{\operatorname{lcm}(A)}
$$

对 $1 \leq i \leq n$, 记 $X_{i}=X_{a_{i}}$, 则当 $A=\left\{a_{i_{1}}, a_{i_{2}}, \cdots, a_{i_{s}}\right\}$ 时, $X_{A}=X_{i_{1}} \cap X_{i_{2}} \cap$ $\cdots \cap X_{i_{s}}$. 由容斥原理,

$P\left(X_{1} \cup X_{2} \cup \cdots \cup X_{n}\right)=\sum_{\emptyset \neq A \subseteq S}(-1)^{|A|-1} \cdot P\left(X_{A}\right)=\sum_{\emptyset \neq A \subseteq S} \frac{(-1)^{|A|-1} \cdot x^{d(A)}}{\operatorname{lcm}(A)}=-f_{S}(x)$.
即有

$$
f_{S}(x)=-P\left(X_{1} \cup X_{2} \cup \cdots \cup X_{n}\right) \in[-1,0] .
$$

评注 本题中, 素数的条件只提供了 $p \geq 2 \geq x$, 容易看出其本质是一个代数问题. 证明 1 的想法比较朴素, 考虑直接归纳. 在写出 $X=\sum_{l=1}^{m} z_{l} \cdot\left(-C_{l}\right)$ 后, 容易看出当 $z_{l}$ 都等于 1 时就是 $t-1$ 时的归纳假设, 注意到 $X$ 是关于 $z_{l}$ 的线性式,接下来的目标就自然转化为分析 $z_{l}$ 的系数 $C_{l}$ 的正负性. 之后的操作就是通过换元的方式构造出归纳假设的结构与条件, 运用归纳假设即可. 证明 2 技巧性很强, 需要对容斥原理写成对子集求和的形式及其加权形式与概率形式有很深刻的理解. 从 $f_{S}$ 表达式中的求和下标 $A \subseteq S$ 及 $(-1)^{|A|}$ 中可以看出容斥原理的特征, 事件 $B_{i, j}$ 及其对应概率的构造是从 $f_{S}$ 的具体表达式出发, 对应容斥原理的形式反推得到的.

感兴趣的读者还可以尝试用容斥原理解决 2020 年北大金秋营第 7 题, 笔者认为在理解了容斥原理的基础上, 通过表达式的形式结合容斥原理的式子, 反推构造出其对应的组合意义, 可以更加自然的得到解法中的母函数.

4. 证明如下方程只有有限组正整数解 $(t, A, x, y, z)$ :

$$
\sqrt{t\left(1-A^{-2}\right)\left(1-x^{-2}\right)\left(1-y^{-2}\right)\left(1-z^{-2}\right)}=\left(1+x^{-1}\right)\left(1+y^{-1}\right)\left(1+z^{-1}\right) \text {. }
$$

证明 不妨设 $x \leq y \leq z$. 原方程即

$$
t\left(1-\frac{1}{A^{2}}\right)=\frac{(x+1)^{2}(y+1)^{2}(z+1)^{2}}{\left(x^{2}-1\right)\left(y^{2}-1\right)\left(z^{2}-1\right)}
$$

显然 $t, A, x, y, z \geq 2$. 故由 $(*)$ 可知

$$
\frac{3}{4} t \leq t\left(1-\frac{1}{A^{2}}\right)=\frac{(x+1)^{2}(y+1)^{2}(z+1)^{2}}{\left(x^{2}-1\right)\left(y^{2}-1\right)\left(z^{2}-1\right)} \leq 3^{3}=27,
$$

即 $t \leq 36$, 故 $t$ 只有有限个取值.

又由 $(*)$ 可知

$$
\frac{(x+1)^{2}(y+1)^{2}(z+1)^{2}}{\left(x^{2}-1\right)\left(y^{2}-1\right)\left(z^{2}-1\right)}=t\left(1-\frac{1}{A^{2}}\right) \geq \frac{3}{2}
$$

当 $x \rightarrow+\infty$ 时, $\frac{(x+1)^{2}}{x^{2}-1} \rightarrow 1$. 故存在 $N>0$, 当 $x>N$ 时, $\frac{(x+1)^{2}}{x^{2}-1}<\sqrt[3]{\frac{3}{2}}$. 故 $x \leq N$, 即 $x$ 只有有限个取值.

下面证明: 对固定的 $x, t \geq 2$, 方程 (*) 关于 $A, y, z$ 只有有限组正整数解, 即对固定的正整数 $p, q$, 方程

$$
\frac{p}{q}=\frac{A^{2}}{A^{2}-1} \cdot \frac{(y+1)^{2}}{y^{2}-1} \cdot \frac{(z+1)^{2}}{z^{2}-1}
$$

只有有限组正整数解 $A, y, z$.

显然 $p>q$ 时方程才有解. 当 $x \rightarrow+\infty$ 时, $\frac{x^{2}}{x^{2}-1} \rightarrow 1$ 且 $\frac{(x+1)^{2}}{x^{2}-1} \rightarrow 1$. 故存在 $M>0$, 当 $x>M$ 时, $\frac{x^{2}}{x^{2}-1}<\sqrt[3]{\frac{p}{q}}$ 且 $\frac{(x+1)^{2}}{x^{2}-1}<\sqrt[3]{\frac{p}{q}}$. 故 $\min \{A, y, z\} \leq M$.

(i) 若 $A \leq M$, 则 $A$ 的取值有限. 对固定的 $A$, 考虑

$$
\frac{s}{t}=\frac{(y+1)^{2}}{y^{2}-1} \cdot \frac{(z+1)^{2}}{z^{2}-1}
$$

其中 $s, t$ 为固定正整数, 且应有 $\frac{s}{t}>1$, 类似分析可知 $y$ 取值有限 $(y \leq z), z$ 随 $y$ 确定, 故该情形下解数有限.

(ii) 若 $y \leq M$, 则 $y$ 的取值有限. 类似可知该情形下解数有限. 综上, 方程 (**) 解数有限, 即对固定的 $x, t$, 原方程 $(*)$ 解数有限. 结合 $x, t$ 取值有限, 即知 (*) 解数有限.

评注 本题是一道常规的数论问题, 要证明解数有限, 基本的想法就是证明变量有界。无法直接证明所有变量都有界时，可以逐个解决，当某一个变量限定在某个范围内后就可以将其视为常数.

5. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是 $1,2, \cdots, n$ 的排列, 求下式的最小值:

$$
\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\}
$$

解 最小值为 $\left\lfloor\frac{n^{2}+n+1}{3}\right\rfloor$, 在 $a_{i}=n+1-i$ 时取到.

设 $\left\lfloor\frac{n}{3}\right\rfloor=k$, 则由题设, 对于任意 $1 \leq j \leq k, 2 j-1$ 与 $2 j$ 均在 $a_{i}$ 中恰出现一次, 故在求和式 $\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\}$ 的 $n$ 个项中, 每个 $2 j-1$ 至多出现两次,每个 $2 j$ 至多出现一次.

(i) $n=3 k$ 时，

$$
\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\} \geq \sum_{i=1}^{k}(2 \cdot(2 i-1)+2 i)=\frac{n(n+1)}{3}
$$

(ii) $n=3 k+1$ 时，

$$
\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\} \geq \sum_{i=1}^{k}(2 \cdot(2 i-1)+2 i)+(2 k+1)=\frac{n(n+1)+1}{3} .
$$

(iii) $n=3 k+2$ 时,

$$
\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\} \geq \sum_{i=1}^{k}(2 \cdot(2 i-1)+2 i)+2 \cdot(2 k+1)=\frac{n(n+1)}{3}
$$

结合三种情形, 即得

$$
\sum_{i=1}^{n} \min \left\{a_{i}, 2 i-1\right\} \geq\left\lfloor\frac{n^{2}+n+1}{3}\right\rfloor .
$$

评注 本题直接的想法就是让求和式中的项都尽量小, 题目所给的排列的条件诱导我们去尝试寻找整体的性质, 得到一个简单的整体估计, 简单尝试后即可发现的确能够取到该最小值.

6. 一个 $n$ 个顶点的简单连通图有 $m$ 条边. 证明: 可以找到 $m$ 种方法把它的顶点集分成两部分, 使得每部分对应的诱导子图是连通的.

证明 1 对 $n$ 归纳. 设图为 $G$.

$n=1,2,3$ 时是平凡的, 下设 $n \geq 4$, 假设命题对 $<n$ 时成立. 称满足题意的划分为好划分.

考虑 $G$ 的任一生成树中的任一叶节点 $v$, 则图 $G^{\prime}=G-v$ 为连通图. 显然 $\{v\} \cup V\left(G^{\prime}\right)$ 是一个好划分.

设 $G$ 中 $v$ 的邻点有 $d$ 个, $d \geq 1$, 设为 $u_{0}, u_{1}, \cdots u_{d-1}$.

考虑 $G^{\prime}$ 的任一好划分 $U_{1} \cup U_{2}$. 若 $v$ 的 $d$ 个邻点均在同一部分中, 不妨设均在 $U_{1}$ 中, 则 $\left(U_{1} \cup\{v\}\right) \cup U_{2}$ 是 $G$ 的一个好划分;若 $v$ 在 $U_{1}$ 与 $U_{2}$ 中均有邻点,则 $\left(U_{1} \cup\{v\}\right) \cup U_{2}$ 与 $U_{1} \cup\left(U_{2} \cup\{v\}\right)$ 均是 $G$ 的好划分. 设 $G^{\prime}$ 的好划分中, 前者有 $a$ 个, 后者有 $b$ 个, 则由归纳假设知

$$
a+b \geq\left|E\left(G^{\prime}\right)\right|=m-d
$$

显然, 这样由 $G^{\prime}$ 的好划分生成的 $G$ 的好划分及 $\{v\} \cup V\left(G^{\prime}\right)$ 互不相同, 故 $G$ 的好划分数 $\geq a+2 b+1 \geq b+m-d+1$.

故只需证: $b \geq d-1$, 即 $G^{\prime}$ 至少有 $d-1$ 个好划分, 使得 $u_{0}, u_{1}, \cdots u_{d-1}$ 不全在同一部分中.

任取 $G^{\prime}$ 的一个以 $u_{0}$ 为根节点的有根生成树 $T$. 对于任意 $1 \leq i \leq d-1$, $T$ 中 $u_{i}$ 的子树与剩下的部分构成 $G^{\prime}$ 的一个好划分, 且 $u_{i}$ 与根节点 $u_{0}$ 不在同一部分中. 显然, 这样得到的 $d-1$ 个 $G^{\prime}$ 的好划分互不相同, 满足要求.

证明 2 设图为 $G$, 称满足题意的划分为好划分.

按如下方式取出图 $G$ 的广度优先生成树.

任取一点 $A$ 为根节点, 记 $S_{0}=\{A\}$.

假设 $S_{0}, S_{1}, \cdots, S_{k}$ 已取, 设 $S_{k}=\left\{v_{1}, v_{2}, \cdots, v_{t}\right\}$. 取 $v_{1}$ 的所有还未被取过的邻点及对应的边加入生成树中, 并将这些点放入 $S_{k+1}$ 中. 再依次对 $v_{2}, \cdots, v_{t}$ 进行相同的操作, 得到 $S_{k+1}$.

当所有点都被取完时操作终止. 这样得到了一个以 $A$ 为根的广度优先生成
树, 称 $S_{k}$ 中的点深度为 $k$.

下面对 $G$ 的每一条边构造一种好划分, 使这 $m$ 个好划分互不相同.

对生成树中的任一边 $u v$, 设 $u$ 为 $v$ 的父节点, 则考虑 $v$ 的子树与剩下的包含 $A$ 的部分的划分, 显然为好划分.

对非生成树中的任一边 $u v$, 则由生成树的取法知, $u, v$ 两点不为祖先关系,故两点对应的子树不交. 考虑 ( $u$ 的子树 $\cup v$ 的子树 ) 及剩下的包含 $A$ 的部分的划分,也为好划分.

这样对每一条边, 都得到了一个好划分. 考虑 $A$ 所在的部分, 知这 $m$ 个好划分互不相同, 满足要求.

评注 证明 1 的归纳法是图论问题中十分常见的手法, 直接暴力删点可能会导致连通性无法保证, 无法利用归纳假设, 因此需要删去一个特殊的点进行归纳. 在刻画图的连通性时, 生成树常有妙用, 因为只考虑生成树往往有比原来复杂的图更加清晰的结构。另外, 证明后半部分中的有根生成树在某些情况下能够更加清晰, 直观的反映出图的性质。证明 2 同样利用有根生成树来构造好划分, 但是当一条边对应的两点在生成树中不相邻且为祖先关系时, 可能会得到重复的好划分, 广度优先生成树恰好能避免这种边的出现.

