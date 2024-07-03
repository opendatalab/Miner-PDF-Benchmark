数学新星网 $\%$ 冷岗松专栏

www.nsmath.cn/lgszl

# 2020 年上海新星冬季数学奥林匹克试题解析 

胡珏伟 吴尉迟 冷岗松

2021 年 2 月, 上海数学新星寒假营提供了一套网络自测题. 测试分为两天,一天四道题, 时间为每天晚上 6 点到 10 点. 本次测验第一天的题目较为常规, 第二天的题目较为困难. 下面就介绍这些试题及给出相应的解答. 不当之处, 敬请读者批评指正.

题 1 如图, 锐角 $\triangle A B C$ 内接于圆 $\Gamma, A B>A C, I$ 为内心, 直线 $A I, B C$ 交于 $J, L$ 为弧 $B A C$ 中点, $A I$ 为直径的圆与圆 $\Gamma$ 交于另一点 $P$. 证明: $\triangle A J P$ 的外心在 $L I$ 上.

(成都树德中学卢圣 供题)



证明 如图, 过 $I$ 作 $A B, A C, B C$ 的垂线, 垂足分别为 $D, E, H$, 则由 $A I$ 为直径知 $D, E$ 在 $\odot(A I P)$ 上. 首先证明 $P, H, M$ 共线且 $J, H, A, P$ 共圆. 事实上,

$$
\angle P B A=\angle P C A,
$$

修订日期: 2020-02-20.

$$
\angle B D P=180^{\circ}-\angle P D A=180^{\circ}-\angle P E A=\angle P E C .
$$

故 $\triangle P B D \sim \triangle P C E$, 于是

$$
\frac{P B}{P C}=\frac{B D}{C E}=\frac{B H}{C H}
$$

由角平分线定理 $H$ 在 $\angle B P C$ 的角平分线上. 又 $M$ 为 $\overparen{A B}$ 中点, 故 $P, H, M$ 共线. 由 $\angle M B J=\angle M A C=\angle M A B$ 知 $\triangle B M J \sim \triangle A M B$, 故

$$
B M^{2}=M J \cdot M A \text {. }
$$

由 $\triangle C M H \sim \triangle P M C$, 有

$$
C M^{2}=M H \cdot M P \text {. }
$$

故

$$
M J \cdot M A=M H \cdot M P,
$$

有 $J, H, A, P$ 共圆.

连结 $A L$, 延长 $H I$ 交 $A L$ 于 $Q$. 由

$$
\angle L A M=\angle J H Q=90^{\circ},
$$

知 $J, H, A, Q$ 共圆. 故有 $J, H, P, A, Q$ 共圆. 此时弦 $J Q$ 对应的圆心角为 $\angle J H Q=90^{\circ}$, 故 $\triangle A J P$ 的外接圆圆心在 $J Q$ 的中点. 因此只需证 $L I$ 平分 $J Q$.考虑到

$$
\frac{J I}{I Q}=\frac{I H}{I A}=\sin \frac{A}{2}
$$

同时

$$
\frac{\sin \angle L I Q}{\sin \angle J I L}=\frac{\sin \angle I L M}{\sin \angle M I L}=\frac{I M}{L M}=\frac{B M}{L M}=\sin \frac{A}{2},
$$

于是对 $\triangle Q S I$ 和 $\triangle S I J$ 分别应用正弦定理有

$$
\begin{aligned}
\frac{Q S}{S J} & =\frac{Q I \cdot \frac{\sin \angle S I Q}{\sin \angle Q S I}}{I J \cdot \frac{\sin \angle S I J}{\sin \angle I S J}} \\
& =\frac{Q I}{I J} \cdot \frac{\sin \angle L I Q}{\sin \angle J I L} \\
& =\frac{1}{\sin \frac{A}{2}} \cdot \sin \frac{A}{2} \quad \text { (用到(1), (2) } \\
& =1 .
\end{aligned}
$$

即 $L I$ 平分 $J Q$.
评注 首先发现 $A, J, P$ 与内心 $I$ 在边 $B C$ 上的垂足 $H$ 共圆. 上述做法的关键在于添出直径 $J Q$, 于是 $\triangle A J P$ 的外心即为 $J Q$ 中点. 从而转化为证明 $L I$ 平分线段 $J Q$, 利用正弦定理导比例便可证明这一点.

题 2 证明存在无穷多组正整数对 $(a, b)$, 使得集合

$$
\left\{\left.\left\lfloor\frac{a^{n}}{n}\right\rfloor \right\rvert\, n \in \mathbb{N}^{+}\right\} \text {和 }\left\{\left.\left\lfloor\frac{b^{n}}{n}\right\rfloor \right\rvert\, n \in \mathbb{N}^{+}\right\}
$$

均包含模 3 的完系, 且 $a-b=2021$.

(湖南师范大学附属中学 刘伟才 供题)

证明 任取奇素数 $p>a(p>3)$, 则由费马小定理,

$$
a^{p} \equiv a \quad(\bmod p)
$$

故

$$
\left\lfloor\frac{a^{p}}{p}\right\rfloor=\frac{a^{p}-a}{p},
$$

又由 $a\left(a^{2}-1\right) \mid a\left(a^{p-1}-1\right)$, 知 $3 \mid a^{p}-a$, 从而 $3 \left\lvert\,\left\lfloor\frac{a^{p}}{p}\right\rfloor\right.$.

若 $a \equiv 2(\bmod 3)$, 则对任意 $m \in \mathbb{Z}^{+}$有



若 $a \equiv 1(\bmod 3)$, 且存在 $3 k+2$ 型素数 $p$ 使得 $p \mid a$, 则

$$
\begin{gathered}
\left\lfloor\frac{a^{a}}{a}\right\rfloor=a^{a-1} \equiv 1 \quad(\bmod 3), \\
\left\lfloor\frac{a^{p a}}{p a}\right\rfloor=\frac{a^{p a-1}}{p} \equiv \frac{1}{2} \equiv 2 \quad(\bmod 3) .
\end{gathered}
$$

若 $3 \mid a, 2 \nmid a$, 则

$$
\begin{aligned}
& \left\lfloor\frac{a^{2}}{2}\right\rfloor=\frac{a^{2}-1}{2} \equiv \frac{-1}{2} \equiv 1 \quad(\bmod 3), \\
& \left\lfloor\frac{a^{4}}{4}\right\rfloor=\frac{a^{4}-1}{4} \equiv \frac{-1}{4} \equiv 2 \quad(\bmod 3) .
\end{aligned}
$$

若 $3|a, 2| a$, 则

$$
\begin{gathered}
\left\lfloor\frac{a^{a-1}}{a-1}\right\rfloor=\frac{a^{a-1}-1}{a-1} \equiv \frac{-1}{-1} \equiv 1 \quad(\bmod 3), \\
\left\lfloor\frac{a^{2(a+1)}}{2(a+1)}\right\rfloor=\frac{a^{2(a+1)}-a-2}{2(a+1)} \equiv \frac{-2}{2} \equiv 2 \quad(\bmod 3) .
\end{gathered}
$$

其中 $\left\lfloor\frac{a^{2(a+1)}}{2(a+1)}\right\rfloor=\frac{a^{2(a+1)}-a-2}{2(a+1)}$ 是由于 $a^{2(a+1)}+a$ 能被 $2(a+1)$ 整除.

综上, 任意被 3 整除或有 $3 k+2$ 型素因子的整数 $a$, 都有 $\left\{\left.\left\lfloor\frac{a^{n}}{n}\right\rfloor \right\rvert\, n \in \mathbb{N}^{+}\right\}$包含模 3 的完系. 注意到 $2021 \equiv 2(\bmod 3)$, 故取

$$
a=b+2021, b=3 k, \quad k \in \mathbb{N}^{+},
$$

即可满足条件.

评注 本题需要对正整数 $a$ 按模 3 的余数分类讨论, 证明 $3 k$ 型和 $3 k+2$ 型正整数均满足 $\left\{\left.\left\lfloor\frac{a^{n}}{n}\right\rfloor \right\rvert\, n \in \mathbb{N}^{+}\right\}$包含模 3 的完系. 再注意到 2021 模 3 余 2 便可完成证明。

题 3 给定整数 $n \geq 4$, 求最小的 $\lambda(n)$, 使得对于任意 $a_{1}, a_{2}, \cdots, a_{n} \geq 0$, 满足

$$
\sum_{i=1}^{n} a_{i}=n
$$

就有

$$
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1} \leq \lambda(n)
$$

恒成立, 其中, $a_{n+1}=a_{1},\{x\}=x-\lfloor x\rfloor,\lfloor x\rfloor$ 表示不超过实数 $x$ 的最大整数.

(长沙一中宋青山供题)

解 先证明如下引理.

引理 设 $n \geq 4$, 若 $r_{1}, r_{2}, \cdots, r_{n} \in[0,1]$ 且

$$
\sum_{i=1}^{n} r_{i}=r
$$

其中 $r \in \mathbb{N}^{+}, r \leq n-1$, 则

$$
\sum_{i=1}^{n} r_{i} r_{i+1} \leq r-\frac{3}{4}
$$

证明 设

$$
f\left(r_{1}, r_{2}, \cdots, r_{n}\right)=\sum_{r=1}^{n} r_{i} r_{i+1}, \quad r_{1}, r_{2}, \cdots, r_{n} \in[0,1]
$$

此时函数 $f$ 为定义在有界闭集上的连续函数, 故存在最大值, 不妨假设最大值在 $\left(r_{1}, r_{2}, \cdots, r_{n}\right)$ 取到. 下证其中不存在 3 个数属于 $(0,1)$.

若不然, 必有两个数的下标之差大于 $1\left(\bmod n\right.$ 意义下). 不妨设为 $r_{i}, r_{j}$, 即 $i, j$ 满足

$$
|i-j| \quad(\bmod n) \geq 2
$$

固定 $r_{i}+r_{j}=t$, 则 $f$ 是关于 $r_{i}$ 的线性函数, 最大值在 $r_{i}=0$ 或 1 时取到, 矛盾!故至多有两个数属于 $(0,1)$ 且两个数(若存在)的下标必定相邻, 即

$$
|i-j| \quad(\bmod n)=1 .
$$

(1) 所有 $r_{i}$ 均为 0 或 1 , 则恰有 $r$ 个 1 . 此时

$$
\sum_{i=1}^{n} r_{i} r_{i+1} \leq r-1 .
$$

(2) 当恰由 2 个 $r_{i}$ 属于 $(0,1)$. 不妨设为 $r_{1}, r_{2}$, 则 $r_{1}+r_{2}=1$ 且剩余 $r-1$个 1. 此时有

$$
r_{n} r_{1}+r_{1} r_{2}+r_{2} r_{3} \leq r_{1}+r_{1} r_{2}+r_{2}
$$

故

$$
\begin{aligned}
\sum_{i=1}^{n} r_{i} r_{i+1} & \leq r_{1}+r_{1} r_{2}+r_{2}+r-2 \\
& =r-1+r_{1} r_{2} \\
& \leq r-1+\left(\frac{r_{1}+r_{2}}{2}\right)^{2} \\
& =r-\frac{3}{4}
\end{aligned}
$$

引理得证!

回到原题. 设 $a_{i}=b_{i}+r_{i}$, 其中 $b_{i}=\left\lfloor a_{i}\right\rfloor, r_{i}=\left\{a_{i}\right\}$. 设 $\sum_{i=1}^{n} r_{i}=r$, 则

$$
r+\sum_{i=1}^{n} b_{i}=n
$$

故 $r \in \mathbb{N}^{+}$且 $r \leq n-1$. 由引理有

$$
\begin{aligned}
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1} & =\sum_{i=1}^{n} r_{i}\left(b_{i+1}+r_{i+1}\right) \\
& =\sum_{i=1}^{n} r_{i} r_{i+1}+\sum_{i=1}^{n} r_{i} b_{i+1} \\
& \leq r-\frac{3}{4}+\sum_{i=1}^{n} b_{i+1} \\
& =n-\frac{3}{4} .
\end{aligned}
$$

另一方面, 令 $a_{1}=\frac{3}{2}+(n-2) \epsilon, a_{2}=\frac{1}{2}$ (对应有两个 $r_{i}$ 为 $\frac{1}{2}$ ), $a_{3}=a_{4}=$ $\cdots=a_{n}=1-\epsilon$. 这时, 令 $\epsilon \rightarrow 0^{+}$, 有

$$
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1} \rightarrow n-\frac{3}{4}
$$

综上, $\lambda(n)_{\min }=n-\frac{3}{4}$.
评注 本题想法是将 $a_{i}$ 拆为整数部分 $b_{i}$ 和小数部分 $r_{i}$. 对 $\sum_{i=1}^{n} r_{i} r_{i+1}$ 用调整法证明该部分极大值时除两个小数部分外, 其余 $r_{i}$ 需足够接近 0 或 1 . 此时, $\sum_{i=1}^{n} r_{i} b_{i+1}$ 中的 $r_{i}$ 均可直接放缩为 1 . 这样得到的最优值是渐进最优的.

题 4 设 $n$ 是正整数, $A_{1}, A_{2}, \cdots, A_{n}$ 是 $n$ 个不同的非空有限集, 满足对任意 $1 \leq i, j, k \leq n$, 若 $A_{i} \cap A_{j}=\varnothing$, 则存在整数 $l(1 \leq l \leq n)$ 使得

$$
\left(A_{i} \cup A_{k}\right) \backslash A_{j}=A_{l} .
$$

求最大的实常数 $c$, 使对任意正整数 $n$ 和任意满足上述性质的集合 $A_{1}, A_{2}, \cdots, A_{n}$,存在集合 $I \subseteq\{1,2, \cdots, n\}$, 使得

(1) $|I| \geq c n$,

(2) 对任意 $i, j \in I, A_{i} \cap A_{j} \neq \varnothing$.

(华东师范大学第二附属中学 王一川供题))

解 $c$ 的最大值为 $\frac{1}{2}$.

首先证明 $c=\frac{1}{2}$ 时结论成立. 称符合条件的集族 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 是 “好的”. 由若 $A_{i} \cap A_{j}=\varnothing$, 则存在整数 $l(1 \leq l \leq n)$ 满足

$$
A_{l}=\left(A_{i} \cup A_{k}\right) \backslash A_{j} \supseteq A_{i},
$$

易知对任意 $X \in\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$, 若 $X$ 的真子集均不在 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$中, 则 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\} \backslash X$ 仍是“好的”. 证明如下引理.

引理 若对“好的”集族 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$, 其中有两个集合不交, 则存在集合 $T \in\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$, 使得 $T$ 恰好与 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 中一个集合不交.

证明 取 $T$ 为与 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 中至少一个集合不交的集合中元素最多的一个. 用反证法, 若存在 $l_{1} \neq l_{2}$ 使

$$
T \cap A_{l_{1}}=T \cap A_{l_{2}}=\varnothing .
$$

由于 $A_{l_{1}}, A_{l_{2}}$ 是不同集合, 故不妨设 $A_{l_{1}} \backslash A_{l_{2}} \neq \varnothing$. 由题设条件有

$$
T^{\prime}=T \cup\left(A_{l_{1}} \backslash A_{l_{2}}\right)=\left(T \cup A_{l_{1}}\right) \backslash A_{l_{2}} \in\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}
$$

注意到

$$
\left|T^{\prime}\right|=|T|+\left|A_{l_{1}} \backslash A_{l_{2}}\right|>|T|
$$

且 $T^{\prime} \cap A_{l_{2}}=\varnothing$, 这与 $T$ 的最大性矛盾!
引理得证.

回到原题. 若 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 两两相交, 则 $c=\frac{1}{2}$ 满足题目要求. 若不然,则可以归纳地在 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 中取出两两不同的集合

$$
P_{1}, P_{2}, \cdots, P_{t}, Q_{1}, Q_{2}, \cdots, Q_{t}(t \geq 1 \text { 待定 }) \text {. }
$$

取法如下: 对 $i \geq 1$, 记

$$
\mathcal{F}_{i-1}=\left\{A_{1}, A_{2}, \cdots, A_{n}\right\} \backslash\left\{P_{1}, P_{2}, \cdots, P_{i-1}\right\}
$$

若 $\mathcal{F}_{i-1}$ 中集合两两相交, 则停止.

若 $\mathcal{F}_{i-1}$ 中存在两个集合不交, 则取 $Q_{i} \in \mathcal{F}_{i-1}$ 恰与一个集合不交, 记为 $P_{i}$.此时 $P_{i}$ 的真子集一定不在 $\mathcal{F}_{i-1}$ 中, 故若 $\mathcal{F}_{i-1}$ 是 “好的”, 则 $\mathcal{F}_{i}$ 也是“好的”. 而 $\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 是“好的”, 结合引理, 这保证了若 $\mathcal{F}_{i}$ 中存在两个集合不交, 取法中的 $Q_{i+1}$ 必定存在.

下面说明 $P_{i}$ 与 $Q_{j}(j=1,2, \cdots, i-1)$ 必定不相同. 若不然, 则由取法知 $Q_{j}$ 只与 $P_{j}$ 不交, 与 $Q_{i} \in \mathcal{F}_{i-1} \subset \mathcal{F}_{j-1}$ 相交, 而由 $Q_{i}$ 取法知 $Q_{i}$ 只与 $P_{i}\left(\right.$ 即 $\left.Q_{j}\right)$不交, 产生矛盾. 因此

$$
P_{i} \notin\left\{A_{1}, A_{2}, \cdots, A_{n}\right\} \backslash\left\{P_{1}, P_{2}, \cdots, P_{i-1}, Q_{1}, Q_{2}, \cdots, Q_{i-1}\right\}
$$

类似讨论可得

$$
Q_{i} \notin\left\{A_{1}, A_{2}, \cdots, A_{n}\right\} \backslash\left\{P_{1}, P_{2}, \cdots, P_{i-1}, Q_{1}, Q_{2}, \cdots, Q_{i-1}\right\}
$$

故

$$
P_{1}, P_{2}, \cdots, P_{t}, Q_{1}, Q_{2}, \cdots, Q_{t}
$$

两两不同, 上述过程必定会终止, 且 $t \leq \frac{n}{2}$.

对于 $1 \leq i \leq t, Q_{i}$ 与 $P_{1}, P_{2}, \cdots, P_{i}, Q_{1}, Q_{2}, \cdots, Q_{i-1}$ 外集合均相交, 且

$$
\left\{A_{1}, A_{2}, \cdots, A_{n}\right\} \backslash\left\{P_{1}, P_{2}, \cdots, P_{t}, Q_{1}, Q_{2}, \cdots, Q_{t}\right\}
$$

中集合两两相交, 故

$$
\left\{A_{1}, A_{2}, \cdots, A_{n}\right\} \backslash\left\{P_{1}, P_{2}, \cdots, P_{t}\right\}
$$

中的集合两两相交, 从而存在 $I \subseteq\{1,2, \cdots, n\},|I|=n-t \geq \frac{n}{2}$ 且 $A_{i}(i \in I)$两两相交.

另一方面, 可以证明 $c>\frac{1}{2}$ 不成立. 当 $n=2$ 时, $A_{1}=\{1\}, A_{2}=\{2\}$ 满足题设条件, 但 $A_{1} \cap A_{2}=\varnothing$, 于是 $c \leq \frac{1}{2}$.

综上, $c$ 的最大值为 $\frac{1}{2}$.
评注 本题的最优值可以在尝试较小的 $n$ 时得到. 在论证部分, 我们通过不断寻找剩余集族中的“极小集族”，该最小元满足存在一个集族，该集族只与“极小集族”不交, 这样的过程可以保证我们的题设条件不变. 从而, 取出的集族不超过一半,并且剩余的集族两两相交.

题 5 设 $n$ 是正整数, $\overrightarrow{v_{1}}, \overrightarrow{v_{2}}, \cdots, \overrightarrow{v_{n}}$ 是平面中的单位向量, $a_{1}, a_{2}, \cdots, a_{n}$是正数. 证明: 可以选取 $\epsilon_{i} \in\{-1,1\}, i=1,2, \cdots, n$, 使

$$
\vec{x}=\sum_{i=1}^{n} \epsilon_{i} a_{i} \vec{v}_{i}
$$

满足

$$
\left|\vec{x} \cdot \overrightarrow{v_{k}}\right| \geq a_{k}
$$

对 $k=1,2, \cdots, n$ 均成立.

(华东师范大学 吴尉迟 供题)

证明 取 $\epsilon_{i} \in\{-1,1\}$, 使

$$
\vec{x}=\sum_{i=1}^{n} \epsilon_{i} a_{i} \vec{v}_{i}
$$

模长最大. 设 $k \in\{1,2, \cdots, n\}$, 对

$$
\vec{y}=\sum_{i \neq k} \epsilon_{i} a_{i} \vec{v}_{i}
$$

由于 $\vec{x}$ 模长的最大性, 知

$$
\left|\vec{y}+\epsilon_{k} a_{k} \overrightarrow{v_{k}}\right|=|\vec{x}| \geq\left|\vec{y}-\epsilon_{k} a_{k} \overrightarrow{v_{k}}\right|,
$$

从而

$$
\vec{y} \cdot\left(\epsilon_{k} a_{k} \overrightarrow{v_{k}}\right) \geq 0
$$

即

$$
\epsilon_{k} \vec{y} \cdot \overrightarrow{v_{k}} \geq 0
$$

故

$$
\begin{aligned}
\left|\vec{x} \cdot \overrightarrow{v_{k}}\right| & =\left|\vec{y} \cdot \overrightarrow{v_{k}}+\epsilon_{k} a_{k} \overrightarrow{v_{k}} \cdot \overrightarrow{v_{k}}\right| \\
& =\left|\epsilon_{k} \cdot\left(\epsilon_{k} \vec{y} \cdot \overrightarrow{v_{k}}+a_{k}\right)\right| \\
& \geq \epsilon_{k} \cdot \vec{y} \cdot \overrightarrow{v_{k}}+a_{k} \\
& \geq a_{k} .
\end{aligned}
$$

命题得证.

评注 本题的想法应是极端原理, 即取 $\epsilon_{i}$ 使得 $\vec{x}=\sum_{i=1}^{n} \epsilon_{i} a_{i} \vec{v}_{i}$ 模长最大, 再验证不等式即可.

题 6 对任意整数 $n \geq 3$, 试找出一个 $\mathbb{Q}$ 上不可约的 $n$ 次多项式 $f(x)$, 使得对任意 $g(x) \in \mathbb{Q}[x](1<\operatorname{deg} g<n)$, 均有 $f(x) \nmid f(g(x))$.

(华东师范大学 罗振华供题)

解 取 $f(x)=x^{n}-2$, 则 $f(x)$ 在 $\mathbb{Q}$ 上不可约, 且所有根为

$$
\sqrt[n]{2} \xi^{k}, k=1,2, \cdots, n
$$

其中

$$
\xi=e^{\frac{2 \pi}{n} i}
$$

下面证明 $f(x)$ 即为所求.

若存在 $g \in \mathbb{Q}[x]$ 且 $1<\operatorname{deg} g<n$ 使得 $f(x) \mid f(g(x))$, 则 $g\left(\sqrt[n]{2} \xi^{k}\right)$ 也是 $f(x)$的根. 考虑到 $g(\sqrt[n]{2})$ 为实数故

$$
g(\sqrt[n]{2})=\sqrt[n]{2} \text { 或 } g(\sqrt[n]{2})=-\sqrt[n]{2} \text {. }
$$

若 $g(\sqrt[n]{2})=\sqrt[n]{2}$, 则 $g(x)-x$ 与 $f(x)$ 有公共根 $\sqrt[n]{2}$. 又 $f$ 在 $\mathbb{Q}$ 上不可约, 故

$$
f(x) \mid g(x)-x .
$$

于是

$$
\operatorname{deg} g(x)=\operatorname{deg}(g(x)-x) \geq \operatorname{deg} f(x) \geq n
$$

矛盾! 同理, $g(\sqrt[n]{2})=-\sqrt[n]{2}$ 也会导出矛盾.

综上, 命题得证.

评注 上述的构造的想法是构造 $f$ 满足其根均不是有理数, 且恰有一根为实根. 在反证假设下, 利用 $g$ 是有理系数多项式知 $f(x)$ 与 $g(x)-x$ 有公共实根且根不为有理数. 结合 $f$ 不可约性便得矛盾.

题 $7 \triangle A B C$ 内心为 $I, D$ 为 $B C$ 边上一点, $A D$ 再次交 $\triangle B D I$ 外接圆于点 $E$. 过 $B$ 作 $A D$ 平行线再次交 $\triangle B D I$ 外接圆于点 $F, F E$ 交 $A C$ 于点 $G, K$ 在 $\triangle A B C$ 外接圆上满足 $\angle B A D=\angle C A K$. 证明: $C, G, I, K$ 共圆.

(温州中学 金晟治 供题)



证明 下面利用同一法.

设 $D$ 在 $B C$ 上, $K$ 在 $\odot A B C$ 满足 $\angle B A D=\angle C A K . \odot C I K$ 交 $A C$ 于 $G$,点 $E$ 在 $A D$ 上, 使 $\angle G E D=\angle C D E$. 设 $C K \cap A D=L, A I \cap \odot C I K=\{I, J\}$.下面只需证: $B, D, I, E$ 共圆.

由

$$
\begin{aligned}
\angle G E D & =\angle C D E=\angle D B A+\angle B A D \\
& =\angle A K C+\angle C A K=180^{\circ}-\angle A C K,
\end{aligned}
$$

知 $L, C, G, E$ 共圆. 由

$$
A I \cdot A J=A G \cdot A C=A E \cdot A L
$$

知 $E, I, J, L$ 共圆. 考虑到

$$
\begin{aligned}
\angle E I B & =\angle E I J-\angle B I J=180^{\circ}-\angle E L J-\left(90^{\circ}-\frac{\angle C}{2}\right) \\
& =180^{\circ}-\angle A L C-\angle J L C-90^{\circ}+\frac{\angle C}{2} \\
& =\angle L D C+\angle L C D+\frac{\angle C}{2}+\angle J L C-90^{\circ} \\
& =\angle B D E+\angle L C I+\angle J L C-90^{\circ} .
\end{aligned}
$$

故只需证明

$$
\angle L C I+\angle J L C=90^{\circ},
$$

由

$$
\angle L C I=180^{\circ}-\angle A J K
$$

只需证

$$
\angle A J K=90^{\circ}+\angle J L C .
$$

故需证: $J$ 为 $\triangle A L K$ 的内心. 结合 $A J$ 平分 $\angle L A K$ 知, 只需证 $K J$ 平分 $\angle A K L$.而

$$
\angle L K J=\angle J I C=90^{\circ}-\frac{\angle B}{2}=90^{\circ}-\frac{\angle A K C}{2} .
$$

故 $K J$ 平分 $\angle A K L$.

综上, 命题得证.

评注 上述解法采用同一法. 先取定 $D, K$, 再取定 $\triangle C K I$ 外接圆与 $A C$ 交点 $G$. 然后取点 $E$ 满足 $\angle G E D=\angle C D E$, 这样便消去了点 $F$, 此时只需证明 $B, D, I, E$ 共圆. 利用 $L, C, G, E$ 共圆, $E, I, J, L$ 共圆以及 $J$ 为 $\triangle A L K$ 内心这三个结论导角证明.

题 8 设 $n \geq 2$ 是给定的整数. 求所有的实数 $\alpha$, 使得存在函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 满足对任意实数 $x_{1}, x_{2}, \cdots, x_{n}$, 均有

$$
\frac{1}{n} \sum_{i=1}^{n} f\left(x_{i}\right) \geq f\left(\frac{1}{n} \sum_{i=1}^{n} x_{i}\right)+\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|^{\alpha} .
$$

(中国人民大学附属中学张端阳 供题)

解 当 $x_{i}=x_{j}$ 时, 由 $\left|x_{i}-x_{j}\right|^{\alpha}$ 存在知 $\alpha>0$.

首先证明, 当 $\alpha \geq 2$ 时, 取函数 $f(x)=2^{\alpha-1} n(n-1)|x|^{\alpha}$ 满足要求.

先证明: 对 $x_{1} \geq x_{2} \geq 0$,

$$
2^{\alpha-1}\left(x_{1}^{\alpha}+x_{2}^{\alpha}\right) \geq\left(x_{1}+x_{2}\right)^{\alpha}+\left(x_{1}-x_{2}\right)^{\alpha} .
$$

记

$$
g\left(x_{1}\right)=2^{\alpha-1}\left(x_{1}^{\alpha}+x_{2}^{\alpha}\right)-\left(x_{1}+x_{2}\right)^{\alpha}-\left(x_{1}-x_{2}\right)^{\alpha},
$$

则

$$
g^{\prime}\left(x_{1}\right)=\alpha\left(2^{\alpha-1} x_{1}^{\alpha-1}-\left(x_{1}+x_{2}\right)^{\alpha-1}-\left(x_{1}-x_{2}\right)^{\alpha-1}\right) .
$$

由 $\alpha-1 \geq 1$ 知

$$
\left(x_{1}+x_{2}\right)^{\alpha-1}+\left(x_{1}-x_{2}\right)^{\alpha-1} \leq\left(\left(x_{1}+x_{2}\right)+\left(x_{1}-x_{2}\right)\right)^{\alpha-1}=2^{\alpha-1} x_{1}^{\alpha-1},
$$

故 $g^{\prime}\left(x_{1}\right) \geq 0$, 结合 $g\left(x_{2}\right)=0$ 知 $g\left(x_{1}\right) \geq 0,(*)$ 式成立.

对 $x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}$, 有

$$
\begin{aligned}
\frac{1}{n} \sum_{i=1}^{n} f\left(x_{i}\right) & =2^{\alpha-1}(n-1) \sum_{i=1}^{n}\left|x_{i}\right|^{\alpha} \\
& =2^{\alpha-1} \sum_{1 \leq i<j \leq n}\left(\left|x_{i}\right|^{\alpha}+\left|x_{j}\right|^{\alpha}\right) \\
& \geq \sum_{1 \leq i<j \leq n}\left(\left.|| x_{i}|+| x_{j}\right|^{\alpha}+\left.|| x_{i}|-| x_{j}\right|^{\alpha}\right) \quad(\text { 用到 }(*) \text { 式) } \\
& =\sum_{1 \leq i<j \leq n}\left(\left|x_{i}+x_{j}\right|^{\alpha}+\left|x_{i}-x_{j}\right|^{\alpha}\right) \\
& \geq \frac{\left(\sum_{1 \leq i<j \leq n}\left|x_{i}+x_{j}\right|\right)^{\alpha}}{\left(\frac{n(n-1)}{2}\right)^{\alpha-1}}+\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|^{\alpha} \quad \text { (幂平均不等式) } \\
& \geq \frac{\left|\sum_{1 \leq i<j \leq n}\left(x_{i}+x_{j}\right)\right|^{\alpha}}{\left(\frac{n(n-1)}{2}\right)^{\alpha-1}}+\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|^{\alpha} \quad \text { (三角不等式) } \\
& =f\left(\frac{1}{n} \sum_{i=1}^{n} x_{i}\right)+\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|^{\alpha} .
\end{aligned}
$$

其次证明, 当 $\alpha<2$ 时, 不存在函数满足要求.

对任意实数 $x, y$, 当 $n$ 是偶数时, 取 $x_{1}=\cdots=x_{\frac{n}{2}}=x, x_{\frac{n}{2}+1}=\cdots=x_{n}=y$得,

$$
\frac{1}{2}(f(x)+f(y)) \geq f\left(\frac{x+y}{2}\right)+\frac{n^{2}}{2}|x-y|^{\alpha}
$$

当 $n$ 是奇数时, 取 $x_{1}=\cdots=x_{\frac{n-1}{2}}=x, x_{\frac{n+1}{2}}=\cdots=x_{n-1}=y, x_{n}=\frac{x+y}{2}$ 得,

$$
\begin{aligned}
& \frac{1}{n}\left(\frac{n-1}{2} f(x)+\frac{n-1}{2} f(y)+f\left(\frac{x+y}{2}\right)\right) \\
\geq & f\left(\frac{x+y}{2}\right)+\frac{(n-1)^{2}}{4}|x-y|^{\alpha}+(n-1) \cdot \frac{|x-y|^{\alpha}}{2^{\alpha}},
\end{aligned}
$$

即

$$
\frac{1}{2}(f(x)+f(y)) \geq f\left(\frac{x+y}{2}\right)+n\left(\frac{n-1}{4}+\frac{1}{2^{\alpha}}\right)|x-y|^{\alpha} .
$$

于是只需证明, 当 $\alpha<2$ 时, 不存在函数 $f(x)$ 和正实数 $C$, 使得对任意实数 $x, y$, 均有

$$
\frac{1}{2}(f(x)+f(y)) \geq f\left(\frac{x+y}{2}\right)+C|x-y|^{\alpha} .
$$

事实上, 假设存在, 则

$$
\frac{1}{2}\left(f(x)+f\left(\frac{x+y}{2}\right)\right) \geq f\left(\frac{3 x+y}{4}\right)+\frac{1}{2^{\alpha}} C|x-y|^{\alpha},
$$

$$
\begin{aligned}
\frac{1}{2}\left(f\left(\frac{x+y}{2}\right)+f(y)\right) & \geq f\left(\frac{x+3 y}{4}\right)+\frac{1}{2^{\alpha}} C|x-y|^{\alpha} \\
\frac{1}{2}\left(f\left(\frac{3 x+y}{4}\right)+f\left(\frac{x+3 y}{4}\right)\right) & \geq f\left(\frac{x+y}{2}\right)+\frac{1}{2^{\alpha}} C|x-y|^{\alpha}
\end{aligned}
$$

(1) + (2) $+2 \cdot$ (3) 得,

$$
\frac{1}{2}(f(x)+f(y)) \geq f\left(\frac{x+y}{2}\right)+\frac{4}{2^{\alpha}} C|x-y|^{\alpha} .
$$

重复上面的过程可知, 对任意正整数 $m$,

$$
\frac{1}{2}(f(x)+f(y)) \geq f\left(\frac{x+y}{2}\right)+\left(\frac{4}{2^{\alpha}}\right)^{m} C|x-y|^{\alpha}
$$

由 $\alpha<2$, 知 $\frac{4}{2^{\alpha}}>1$, 所以

$$
\lim _{m \rightarrow \infty}\left(\frac{4}{2^{\alpha}}\right)^{m}=+\infty
$$

矛盾!

综上, 所求为所有不小于 2 的实数.

评注 (1) 本题可以尝试 $\alpha=2$ 的情形. 当取 $f(x)=|n x|^{2}$, 要证不等式刚好取等. 我们知道当 $\alpha$ 越大, $f(x)=|n x|^{\alpha}$ 的凸性越强. 由此猜测 $\alpha \geq 2$ 结论成立.

对 $\alpha \geq 2$ 的情形, 取 $f(x)=|k x|^{\alpha}$ ( $k$ 为待定系数), 对于固定的 $x_{1}, x_{2}, \cdots, x_{n}$,系数 $k$ 越大,

$$
\frac{1}{n} \sum_{i=1}^{n} f\left(x_{i}\right)-f\left(\frac{1}{n} \sum_{i=1}^{n} x_{i}\right)
$$

也越大而

$$
\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|^{\alpha}
$$

不变. 因此取 $k$ 足够大时便满足题目条件.

对 $\alpha<2$ 的情形, 采用分析的想法. 在反证法的假设下, 取特定的 $x, y$, 使 $|x-y|^{\alpha}$ 前的系数不断增大并趋于无穷, 由此得到矛盾.

(2) 本题源于对 2000 年美国数学奥林匹克第一题的讨论:

称实值函数 $f$ 是“强凸的”, 如果对任意实数 $x, y$, 均有

$$
\frac{f(x)+f(y)}{2} \geq f\left(\frac{x+y}{2}\right)+|x-y| .
$$

证明: 不存在强凸的函数.

