# 数学新星问题征解第六期解答 

2015.06

第一题: 设 $a, b$ 是正整数且 $a<b$. 证明: 存在正整数 $n$ 及整数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $1 \leq\left|x_{1}\right|<\left|x_{2}\right|<\cdots<\left|x_{n}\right|<b^{2}$, 使得

$$
\frac{a}{b}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}} .
$$

(湖北武钢三中学生 陈泽坤 供题)

## 证法一 (根据陈坤同学的解答整理):

根据题意, 我们不妨假设 $a, b$ 互素, 设 $\frac{a}{b}$ 的连分数表示为

$$
\frac{a}{b}=\left\langle 0, a_{1}, \cdots, a_{n}\right\rangle=0+\frac{1}{a_{1}+\frac{1}{a_{2}+\frac{1}{\ddots \cdot+\frac{1}{a_{n}}}}}
$$

其中 $a_{1}, \cdots, a_{n} \in \mathbb{N}^{+}$. 记 $\frac{P_{k}}{Q_{k}}$ 是 $\left\langle 0, a_{1}, \cdots, a_{k}\right\rangle(k=1,2, \cdots, n)$ 的既约分数表示,约定 $P_{0}=0, Q_{0}=1$. 下面证明

$$
1 \leq Q_{1}<Q_{2}<\cdots<Q_{n}=b
$$

且

$$
P_{k+1} Q_{k}-P_{k} Q_{k+1}=(-1)^{k} .
$$

为此, 我们先对 $k$ 归纳证明

$$
P_{k+1}=a_{k+1} P_{k}+P_{k-1}, \quad Q_{k+1}=a_{k+1} Q_{k}+Q_{k-1}
$$

当 $k=1$ 时, 易知 $P_{2}=a_{2}, Q_{2}=a_{2} a_{1}+1$, 而 $P_{1}=1, Q_{1}=a_{1}, P_{0}=0, Q_{0}=1$,因此 $P_{2}=a_{2} P_{1}+P_{0}, Q_{2}=a_{2} Q_{1}+Q_{0}$ 成立.

假设对于 $k-1(k \geq 2)$ 时成立, 即

$$
P_{k}=a_{k} P_{k-1}+P_{k-2}, \quad Q_{k}=a_{k} Q_{k-1}+Q_{k-2}
$$

则由归纳假设，

$$
\frac{P_{k+1}}{Q_{k+1}}=\left\langle 0, a_{1}, \cdots, a_{k-1}, a_{k}+\frac{1}{a_{k+1}}\right\rangle=\frac{\left(a_{k}+\frac{1}{a_{k+1}}\right) P_{k-1}+P_{k-2}}{\left(a_{k}+\frac{1}{a_{k+1}}\right) Q_{k-1}+Q_{k-2}}=\frac{a_{k+1} P_{k}+P_{k-1}}{a_{k+1} Q_{k}+Q_{k-1}}
$$

故 $P_{k+1}=a_{k+1} P_{k}+P_{k-1}, Q_{k+1}=a_{k+1} Q_{k}+Q_{k-1}$ 对于 $k=1,2, \cdots, n-1$ 均成立.

由上述结果, 可得

$$
Q_{k+1}=a_{k+1} Q_{k}+Q_{k-1}>a_{k+1} Q_{k} \geq Q_{k}, k=1,2, \cdots, n-1
$$

即 (1) 式成立. 并且

$$
\begin{aligned}
P_{k+1} Q_{k}-P_{k} Q_{k+1} & =\left(a_{k+1} P_{k}+P_{k-1}\right) Q_{k}-\left(a_{k+1} Q_{k}+Q_{k-1}\right) P_{k} \\
& =(-1)\left(P_{k} Q_{k-1}-P_{k-1} Q_{k}\right. \\
& =\cdots \\
& =(-1)^{k}\left(P_{1} Q_{0}-P_{0} Q_{1}\right)=(-1)^{k}
\end{aligned}
$$

因此 (2) 式成立.

从而

$$
\frac{a}{b}=\frac{P_{n}}{Q_{n}}=\sum_{k=0}^{n-1}\left(\frac{P_{k+1}}{Q_{k+1}}-\frac{P_{k}}{Q_{k}}\right)=\sum_{k=0}^{n-1} \frac{(-1)^{k}}{Q_{k} Q_{k+1}}
$$

令 $x_{k+1}=(-1)^{k} Q_{k} Q_{k+1}, k=0,1, \cdots, n-1$, 则 $\left|x_{k+1}\right|=Q_{k} Q_{k+1}$, 且由 (1) 式得,

$$
1 \leq\left|x_{1}\right|<\left|x_{2}\right|<\cdots<\left|x_{n}\right|<Q_{n}^{2}=b^{2}
$$

且

$$
\frac{a}{b}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}}
$$

从而结论成立.

证法二 (根据吴东晓同学的解答整理): 对 $b$ 用归纳法.

当 $b=2$ 时, $a=1$. 此时令 $n=1, x_{1}=2$ 即可.

假设结论对一切 $2 \leq b^{\prime}<b$ 成立, 下证结论对 $b$ 成立.

(i) 若 $(a, b)=d>1$, 设 $a=a_{1} d, b=b_{1} d$, 其中 $a_{1}, b_{1}$ 是正整数且 $\left(a_{1}, b_{1}\right)=1$.

由归纳假设知, 存在正整数 $n$ 及整数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $1 \leq\left|x_{1}\right|<\left|x_{2}\right|<\cdots<$ $\left|x_{n}\right|<b_{1}^{2}$, 使得

$$
\frac{a_{1}}{b_{1}}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}},
$$

则

$$
\frac{a}{b}=\frac{a_{1}}{b_{1}}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}}
$$

且

$$
1 \leq\left|x_{1}\right|<\left|x_{2}\right|<\cdots<\left|x_{n}\right|<b_{1}^{2}<b^{2} .
$$

结论成立.

(ii) 若 $(a, b)=1$, 则存在 $k \in\{1,2, \cdots, b-1\}$, 使得 $a k \equiv 1(\bmod b)$. 设存在正整数 $l$, 满足 $a_{k}=b l+1$, 则 $l<k$, 且有

$$
\frac{a}{b}=\frac{a k}{b k}=\frac{b l+1}{b k}=\frac{l}{k}+\frac{1}{b k}
$$

由归纳假设知, 存在正整数 $n$ 及整数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $1 \leq\left|x_{1}\right|<\left|x_{2}\right|<\cdots<$ $\left|x_{n}\right|<k^{2}$, 使得

$$
\frac{l}{k}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}}
$$

令 $x_{n+1}=b k$, 则有 $1 \leq\left|x_{1}\right|<\left|x_{2}\right|<\cdots<\left|x_{n}\right|<k^{2}<b k=\left|x_{n+1}\right|<b^{2}$, 且

$$
\frac{a}{b}=\frac{l}{k}+\frac{1}{b k}=\frac{1}{x_{1}}+\frac{1}{x_{2}}+\cdots+\frac{1}{x_{n}}+\frac{1}{x_{n+1}} .
$$

因此对一切正整数 $b \geq 2$ 结论成立.

第二题: 在空间直角坐标系中, 以原点为起点作三条两两垂直的单位向量, 从这三个向量的三个终点向 $X O Y$ 平面作射影 $A, B, C$. 证明: $A, B, C$ 的横坐标的平方和为 1 .

(湖南雅礼中学学生 何通木 供题)

## 证明 (根据何通木同学的解答整理):

设两两垂直的单位向量的坐标分别为 $\left(x_{A}, y_{A}, z_{A}\right),\left(x_{B}, y_{B}, z_{B}\right),\left(x_{C}, y_{C}, z_{C}\right)$,则这三个实数对满足下列关系式:

$$
\begin{gathered}
x_{A}^{2}+y_{A}^{2}+z_{A}^{2}=1, x_{B}^{2}+y_{B}^{2}+z_{B}^{2}=1, x_{C}^{2}+y_{C}^{2}+z_{C}^{2}=1, \\
x_{A} x_{B}+y_{A} y_{B}+z_{A} z_{B}=0, x_{B} x_{C}+y_{B} y_{C}+z_{B} z_{C}=0, x_{C} x_{A}+y_{C} y_{A}+z_{C} z_{A}=0,
\end{gathered}
$$

我们要证明 $x_{A}^{2}+x_{B}^{2}+x_{C}^{2}=1$.

进一步, 我们可以将问题转变成: 一个 $3 \times 3$ 的实矩阵 $H=\left(\begin{array}{lll}x_{A} & y_{A} & z_{A} \\ x_{B} & y_{B} & z_{B} \\ x_{C} & y_{C}\end{array}\right)$, 如果它的三个行向量是两两垂直的单位向量, 那么它的三个列向量也是两两垂直的单位向量.
事实上, 由已知得, $H H^{T}=E$, 这里 $H^{T}$ 表示矩阵 $H$ 的转置, $E$ 表示单位矩阵, 我们需证 $H^{T} H=E$. 由行列式的运算性质, $|H| \cdot\left|H^{T}\right|=|E|=1$,所以 $|H| \neq 0,\left|H^{T}\right| \neq 0$. 则由克莱姆法则, 逆 $H^{-1},\left(H^{T}\right)^{-1}$ 均存在. 于是对 $H H^{T}=E$ 两边前后分别乘 $H^{T}$ 和 $\left(H^{T}\right)^{-1}$, 得 $H^{T}\left(H H^{T}\right)\left(H^{T}\right)^{-1}=H^{T} E\left(H^{T}\right)^{-1}$,即 $H^{T} H E=E$, 故 $H^{T} H=E$. 因此 $x_{A}^{2}+x_{B}^{2}+x_{C}^{2}=1$, 结论成立.

评注: 本题的问题来源是 2014 年北京大学 “百年数学” 科学体验营的一道试题:已知 $a_{i}, b_{i}, c_{i}$ 是实数, $i=1,2,3,4$, 且

$$
\begin{aligned}
& \sum_{i=1}^{4} a_{i}^{2}=1, \quad \sum_{i=1}^{4} b_{i}^{2}=1, \quad \sum_{i=1}^{4} c_{i}^{2}=1, \\
& \sum_{i=1}^{4} a_{i} b_{i}=0, \quad \sum_{i=1}^{4} b_{i} c_{i}=0, \quad \sum_{i=1}^{4} c_{i} a_{i}=0 .
\end{aligned}
$$

证明: $a_{1}^{2}+b_{1}^{2}+c_{1}^{2} \leq 1$.

原问题中的求和上标 $n=4$ 不是本质的, 实际上, 对任意 $n \geq 3$ 的情形都成立. 结论可以由初等证法得到, 证明过程极富技巧性. 当 $n=3$ 时, 我们需证明 $a_{1}^{2}+b_{1}^{2}+c_{1}^{2} \geq 1$, 继而完成第二题的解答.

第三题: 设四边形 $A B C D$ 是圆外切四边形, $O_{A}, O_{B}, O_{C}, O_{D}$ 分别是 $\triangle B C D, \triangle C D A$, $\triangle D A B, \triangle A B C$ 的外心. 证明: $O_{A} O_{B} O_{C} O_{D}$ 也是圆外切四边形.

(北京人大附中 张端阳 供题)

## 证明 (根据窦泽皓同学的解答整理):

先证明 $O_{A} O_{B} O_{C} O_{D}$ 是凸四边形. 事实上, 由于 $O_{A} O_{D} \perp B C, O_{A} O_{B} \perp C D$, 所以 $\angle O_{D} O_{A} O_{B}=180^{\circ}-\angle B C D$. 同理, $\angle O_{A} O_{B} O_{C}=180^{\circ}-\angle A D C, \angle O_{B} O_{C} O_{D}=$ $180^{\circ}-\angle D A B, \angle O_{C} O_{D} O_{A}=180^{\circ}-\angle A B C$. 假设 $O_{A} O_{B} O_{C} O_{D}$ 是凹四边形, 不妨设 $\angle O_{D} O_{A} O_{B}$ 最大, 则

$$
\angle O_{D} O_{A} O_{B}=\angle O_{A} O_{B} O_{C}+\angle O_{B} O_{C} O_{D}+\angle O_{C} O_{D} O_{A},
$$

从而

$$
\angle B C D+360^{\circ}=\angle A D C+\angle D A B+\angle A B C .
$$

但

$$
\angle B C D+\angle A D C+\angle D A B+\angle A B C=360^{\circ},
$$

故 $\angle B C D=0^{\circ}$, 矛盾! 故 $O_{A} O_{B} O_{C} O_{D}$ 是凸四边形.

要证 $O_{A} O_{B} O_{C} O_{D}$ 是圆外切四边形, 我们需证

$$
O_{A} O_{D}+O_{B} O_{C}=O_{A} O_{B}+O_{C} O_{D}
$$

记 $\triangle B C D, \triangle C D A, \triangle D A B, \triangle A B C$ 的外接圆半径分别为 $R_{A}, R_{B}, R_{C}, R_{D}$, 则由 $O_{A} O_{D} \perp B C$ 知,

$$
O_{A} O_{D}=R_{A} \cos \angle B D C-R_{D} \cos \angle B A C .
$$

若分别将 $\angle D A B, \angle A B C, \angle B C D, \angle C D A$ 简记为 $\angle A, \angle B, \angle C, \angle D$, 则由正弦定理及余弦定理，

$$
\begin{aligned}
R_{A} \cos \angle B D C & =\frac{B D}{2 \sin C} \cdot \frac{B D^{2}+C D^{2}-B C^{2}}{2 B D \cdot C D} \\
& =\frac{\left(C D^{2}+B C^{2}-2 C D \cdot B C \cdot \cos C\right)+C D^{2}-B C^{2}}{4 C D \sin C} \\
& =\frac{C D-B C \cos C}{2 \sin C} \\
& =\frac{1}{2}\left(\frac{C D}{\sin C}-B C \cot C\right) .
\end{aligned}
$$

同理,

$$
R_{D} \cos \angle B A C=\frac{1}{2}\left(\frac{A B}{\sin B}-B C \cot B\right) .
$$

这样,

$$
2 O_{A} O_{D}=\frac{C D}{\sin C}-\frac{A B}{\sin B}+B C(\cot B-\cot C)
$$

同理,

$$
\begin{aligned}
2 O_{A} O_{B} & =\frac{B C}{\sin C}-\frac{A D}{\sin D}+C D(\cot D-\cot C), \\
2 O_{B} O_{C} & =\frac{A B}{\sin A}-\frac{C D}{\sin D}+A D(\cot D-\cot A), \\
2 O_{C} O_{D} & =\frac{A D}{\sin A}-\frac{B C}{\sin B}+A B(\cot B-\cot A) .
\end{aligned}
$$

于是, 若记 $S=2\left(O_{B} O_{C}+O_{A} O_{D}-O_{A} O_{B}-O_{C} O_{D}\right)$, 则

$$
\begin{aligned}
S & =A B\left(\frac{1}{\sin A}-\frac{1}{\sin B}+\cot A-\cot B\right)+B C\left(\frac{1}{\sin B}-\frac{1}{\sin C}+\cot B-\cot C\right) \\
& +C D\left(\frac{1}{\sin C}-\frac{1}{\sin D}+\cot C-\cot D\right)+D A\left(\frac{1}{\sin D}-\frac{1}{\sin A}+\cot D-\cot A\right)
\end{aligned}
$$

若记 $\angle A=2 \alpha, \angle B=2 \beta, \angle C=2 \gamma, \angle D=2 \delta$, 且设四边形 $A B C D$ 的内切圆半径为 1 , 则 $A B=\cot \alpha+\cot \beta$. 又注意到

$$
\frac{1}{\sin \theta}+\cot \theta=\frac{1+\cos \theta}{\sin \theta}=\frac{2 \cos ^{2} \frac{\theta}{2}}{2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}=\cot \frac{\theta}{2}
$$

故

$A B\left(\frac{1}{\sin A}-\frac{1}{\sin B}+\cot A-\cot B\right)=(\cot \alpha+\cot \beta)(\cot \alpha-\cot \beta)=\cot ^{2} \alpha-\cot ^{2} \beta$.

同理,

$$
\begin{aligned}
& B C\left(\frac{1}{\sin B}-\frac{1}{\sin C}+\cot B-\cot C\right)=\cot ^{2} \beta-\cot ^{2} \gamma, \\
& C D\left(\frac{1}{\sin C}-\frac{1}{\sin D}+\cot C-\cot D\right)=\cot ^{2} \gamma-\cot ^{2} \delta, \\
& D A\left(\frac{1}{\sin D}-\frac{1}{\sin A}+\cot D-\cot A\right)=\cot ^{2} \delta-\cot ^{2} \alpha .
\end{aligned}
$$

由此可知 $S=0$, 即 $O_{A} O_{D}+O_{B} O_{C}=O_{A} O_{B}+O_{C} O_{D}$. 故四边形 $O_{A} O_{B} O_{C} O_{D}$ 是圆外切四边形.

第四题: 已知 $n$ 阶完全图可拆分为 $n$ 个两两无公共边的完全图 $G_{1}, \cdots, G_{n}$ 的并,其中 $G_{1}, \cdots, G_{n}$ 均至少有两个顶点. 设 $G_{1}, \cdots, G_{n}$ 的顶点集为 $V_{1}, \cdots, V_{n}$. 证明:要么 $\left\{\left|V_{1}\right|, \cdots,\left|V_{n}\right|\right\}=\{\underbrace{2, \cdots, 2}_{n-1 \text { 个 } 2}, n-1\}$, 要么 $\left|V_{1}\right|=\cdots=\left|V_{n}\right|=a$ 且 $n=a^{2}-a+1$.

(广东深圳第三中学学生 吴东晓 供题)

## 证明 (根据吴东晓同学的解答整理):

记 $G_{1}, \cdots, G_{n}$ 的边集为 $\left\{E_{1}, \cdots, E_{n}\right\}$, 记 $G$ 的顶点集 $V=\left\{X_{1}, \cdots, X_{n}\right\}$, 并设 $V_{1}, \cdots, V_{n}$ 中有 $x_{i}$ 个点集包含 $X_{i}(i=1, \cdots, n)$, 则对不在 $V_{i}$ 中的一点 $X_{j}$, 有

$$
x_{j} \geq\left|V_{i}\right|, \quad i=1, \cdots, n
$$

这是因为对 $V_{i}$ 中每点 $X_{t}$, 边 $X_{t} X_{j}$ 包含于 $E_{1}, \cdots, E_{n}$ 中不同于 $E_{i}$ 的一个, 设为 $E_{k_{t}}$, 则 $E_{k_{t}}$ 两两不同. 不然假设存在 $t_{1} \neq t_{2}$, 使得 $E_{k_{t_{1}}}=E_{k_{2}}$, 由 $X_{t_{1}}, X_{t_{2}} \in V_{i}$且 $X_{t_{1}}, X_{t_{2}} \in V_{k_{t_{1}}}$ 知边 $X_{t_{1}} X_{t_{2}}$ 属于 2 个边集 $E_{k_{t_{1}}}$ 与 $E_{i}$, 矛盾. 故 $X_{j}$ 至少包含于 $\left|V_{i}\right|$ 个不同点集 $V_{k_{t}}\left(X_{t} \in V_{i}\right)$, 因此 $x_{j} \geq\left|V_{i}\right|$, 从而 (1) 式得证.

设 $x_{1}=\min \left(x_{1}, \cdots, x_{n}\right)$, 并设 $X_{1}$ 包含于 $V_{1}, \cdots, V_{x_{1}}$, 因为 $\left|V_{i}\right| \geq 2, i=$ $1, \cdots, x_{1}$, 故 $V_{i}$ 中至少还有一个不同于 $X_{1}$ 的点. 同时注意到 $V_{i} \backslash\left\{X_{1}\right\} \cap V_{j} \backslash\left\{X_{1}\right\}=$
$\emptyset, 1 \leq i<j \leq x_{1}$. 故不妨假设 $X_{2} \in V_{1}, X_{3} \in V_{2}, \cdots, X_{x_{1}+1} \in V_{x_{1}}$, 且 $X_{i+1} \notin$ $V_{j}, 1 \leq j \leq x_{1}, j \neq i, i=1, \cdots, x_{1}$, 则利用 (1), 可得

$$
x_{i+1} \geq\left|V_{j}\right|, 1 \leq j \leq x_{1}, j \neq i, i=1, \cdots, x_{1} .
$$

将这些式子全部累加, 得

$$
\left(x_{1}-1\right) \sum_{i=1}^{x_{1}} x_{i+1} \geq\left(x_{1}-1\right) \sum_{j=1}^{x_{1}}\left|V_{j}\right|
$$

再由 $X_{1} \notin V_{j}, j=x_{1}+1, \cdots, n$, 以及 (1) 式知

$$
x_{1} \geq\left|V_{j}\right|, j=x_{1}+1, \cdots, n
$$

结合 (3),(4) 两式, 得

$$
\begin{aligned}
\sum_{i=1}^{n} x_{i} & \geq\left(n-x_{1}\right) x_{1}+\sum_{i=1}^{x_{1}} x_{i+1} \\
& \geq \sum_{j=x_{1}+1}^{n}\left|V_{j}\right|+\sum_{i=1}^{x_{1}}\left|V_{i}\right| \\
& =\sum_{i=1}^{n}\left|V_{i}\right|=\sum_{i=1}^{n} x_{i}
\end{aligned}
$$

这表明, (2) 式与 (4) 式中的不等式等号均成立.

故由等号成立条件, 当 $x_{1}>2$ 时, 有

$$
\begin{gathered}
x_{2}=\cdots=x_{x_{1}+1}=\left|V_{1}\right|=\cdots=\left|V_{x_{1}}\right|=p, \\
x_{1}=x_{x_{1}+2}=\cdots=x_{n}=\left|V_{x_{1}+1}\right|=\cdots=\left|V_{n}\right|=q,
\end{gathered}
$$

其中 $p, q$ 为正整数, 且由 $x_{1}$ 的最小性知 $p \geq q$. 若 $p>q$, 则

$$
\left|V_{i}\right|=p>q=x_{j}, i=1, \cdots, x_{1}, j=1, x_{1}+2, \cdots, n
$$

故由 (1) 式知, $X_{j} \in V_{i}$. 我们易知 $x_{1}=n-1$, 不然有 $X_{1}, X_{n} \in V_{1}, V_{2}$, 则边 $X_{1} X_{2}$ 属于 $E_{1}, E_{2}$, 矛盾. 因此 $x_{1}=n-1$, 又 $x_{2}=\cdots=x_{n}>x_{1}$, 于是 $x_{2}=\cdots=x_{n}=n$. 此时任一条边都属于 $E_{2}, \cdots, E_{n}$, 矛盾. 故而只能 $p=q$. 此时 $\left|V_{1}\right|=\left|V_{2}\right|=\cdots=\left|V_{n}\right|$,记它们的值为 $a$. 则由

$$
\mathrm{C}_{n}^{2}=|E(G)|=\left|E_{1}\right|+\cdots+\left|E_{n}\right|=n \mathrm{C}_{a}^{2}
$$

知 $n=a^{2}-a+1$.

当 $x_{1}=2$ 时, 仍由等号成立条件, 有

$$
x_{2}=\left|V_{1}\right|=p, x_{3}=\left|V_{2}\right|=q, x_{1}=x_{4}=\cdots=x_{n}=\left|V_{3}\right|=\cdots=\left|V_{n}\right|=2
$$

若 $p+q>n+1$, 即 $x_{2}+x_{3}>n+1$, 则存在 2 个点集 $V_{i}, V_{j}$ 包含 $X_{2}, X_{3}$, 于是边 $X_{2} X_{3}$ 属于边集 $E_{i}, E_{j}$, 矛盾. 故 $p+q \leq n+1$, 此外, $p=\left|V_{1}\right| \geq 2, q=\left|V_{2}\right| \geq 2$,又注意到

$$
\begin{aligned}
\mathrm{C}_{n}^{2} & =|E(G)|=\left|E_{1}\right|+\cdots+\left|E_{n}\right| \\
& =\mathrm{C}_{p}^{2}+\mathrm{C}_{q}^{2}+(n-2) \mathrm{C}_{2}^{2} \\
& =\frac{1}{2}\left(p^{2}+q^{2}-p-q\right)+n-2 \\
& \leq \frac{1}{2}\left((p+q-2)^{2}+2^{2}-p-q\right)+n-2 \\
& \leq \frac{1}{2}\left((n+1-2)^{2}+2^{2}-(n+1)\right)+n-2 \\
& =\frac{1}{2}\left(n^{2}-n\right)=\mathrm{C}_{n}^{2} .
\end{aligned}
$$

由等号成立条件知, $\{p, q\}=\{2, n-1\}$, 从而 $\left\{\left|V_{1}\right|, \cdots,\left|V_{n}\right|\right\}=\{\underbrace{2, \cdots, 2}_{n-1 \text { 个 } 2}, n-1\}$.

综上, $\left|V_{1}\right|, \cdots,\left|V_{n}\right|$ 满足

$$
\left\{\left|V_{1}\right|, \cdots,\left|V_{n}\right|\right\}=\{\underbrace{2, \cdots, 2}_{n-1 \text { 个 } 2}, n-1\}
$$

或者

$$
\left|V_{1}\right|=\left|V_{2}\right|=\cdots=\left|V_{n}\right|=a, \quad n=a^{2}-a+1
$$

结论得证.

评注: 第四题的问题来源是:

集合 $\{1,2, \cdots, n\}$ 的 $m$ 个子集 $A_{1}, \cdots, A_{m}$ ，满足对集合 $\{1,2, \cdots, n\}$ 中任两个不同元素 $i, j$, 恰有一个子集 $A_{k}$, 使得 $i, j$ 同时属于 $A_{k}$, 证明: $m \geq n$.

运用线性代数的知识容易得到上述不等式, 但难以从这种证法中得到等号成立条件. 通过细致的分析, 可以得到等号成立条件只有两种不复杂的情形, 转化成图论语言, 就产生了第四题.

