数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2019 年夏季上海新星数学奥林匹克试题解析 

罗振华 1, 吴尉迟 ${ }^{2}$, 金天 ${ }^{2}$, 冷岗松 2

(1. 华东师范大学, 200241; 2. 上海大学, 200444)

2019 年夏季上海新星数学奥林匹克于 2019 年 6 月 4 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答.

## I. 试 题

1. 设 $x_{1}, x_{2}, \cdots, x_{2019}$ 是实数, 且满足 $x_{1}+\cdots+x_{2019} \in \mathbb{Z}$. 求

$$
\sum_{1 \leq i<j \leq 2019}\left\{x_{i}+x_{j}\right\}
$$

的最大值.

(山西大学附属中学王永喜供题)

2. 如图, 锐角 $\triangle A B C$ 中, $H$ 为垂心, $E, F$ 在 $B C$上, $E H \perp H F$, 延长 $E H$ 与 $A C$ 交于 $M$, 延长 $F H$ 与 $A B$ 交于 $N . H_{1}, H_{2}$ 为 $\triangle B N F, \triangle C M E$ 的垂心. 证明: $H_{1}, H, H_{2}$ 共线.

(广西钦州 卢圣 供题)



3. 设 $n, r$ 为正整数, $n>r$. 将圆周上给定的 $2 n$ 个点染 $n$ 种颜色, 每色染 2 个点, 且任何两个同色点之间恰有 $r$ 个点.

(1) 试问: $n, r$ 能否同为奇数?

(2) 如果 $r+1$ 为质数, 求 $n$ 的所有可能取值.

(深圳高级中学 冯跃峰 供题)

4. 证明: 存在全体正整数的一个排列 $a_{1}, a_{2}, \cdots$, 使得对任意自然数 $i$, 均有

$$
\left(a_{i}, a_{i+1}\right) \geq \frac{i}{2}
$$

修订日期: 2019-06-25.

5. 设 $n$ 是正整数, $2 n$ 个实数 $x_{i}, y_{i}(1 \leq i \leq n)$ 满足

$$
\sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} y_{i}^{2}=1
$$

已知 $0<\lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{n}, 1 \in\left[\lambda_{1}, \lambda_{n}\right]$. 证明:

$$
\lambda_{1} \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}} \leq \lambda_{n}
$$

(北京大学王逸轩供题)

6. 对边互不平行的四边形 $A B C D$ 内接于 $\odot O$. 设对角线 $A C, B D$ 交于点 $P$, 直线 $A D, B C$ 交于点 $E, M$ 是 $O P$ 的中点. 已知 $\triangle A O B, \triangle C O D, \triangle A P B$, $\triangle C P D$ 的外心共圆, 证明: 该圆圆心是 $\triangle O M E$ 的垂心.

(中国人民大学附属中学 张端阳 供题)

## II. 解 答

题 1 设 $x_{1}, x_{2}, \cdots, x_{2019}$ 是实数, 且满足 $x_{1}+\cdots+x_{2019} \in \mathbb{Z}$. 求

$$
\sum_{1 \leq i<j \leq 2019}\left\{x_{i}+x_{j}\right\}
$$

的最大值.

解 我们用奇数 $n$ 代替 2019 解决更一般的问题:

设 $n$ 是奇数, $x_{1}, x_{2}, \cdots, x_{n}$ 是实数, 且满足 $x_{1}+\cdots+x_{n} \in \mathbb{Z}$. 求

$$
\sum_{1 \leq i<j \leq n}\left\{x_{i}+x_{j}\right\}
$$

的最大值.

引理 设 $[0,1)$ 上的实数 $a_{1}, a_{2}, \cdots, a_{k}$ 满足 $a_{1}+a_{2}+\cdots+a_{k} \in \mathbb{Z}$, 则

$$
\sum_{i=1}^{k} a_{k} \leq k-1 .
$$

引理证明事实上, 注意到

$$
\sum_{i=1}^{k} a_{k}<k
$$

结合 $a_{1}+a_{2}+\cdots+a_{k} \in \mathbb{Z}$ 可知

$$
\sum_{i=1}^{k} a_{k} \leq k-1
$$

故引理获证.

回到原题. 注意到

$$
\sum_{1 \leq i<j \leq n}\left\{x_{i}+x_{j}\right\}=\frac{1}{2} \sum_{k=1}^{n-1} \sum_{i=1}^{n}\left\{x_{i}+x_{i+k}\right\}
$$

而对每个正整数 $k(1 \leq k \leq n-1)$,

$$
\sum_{i=1}^{n}\left\{x_{i}+x_{i+k}\right\}=2 \sum_{i=1}^{n} x_{i}-\sum_{i=1}^{n}\left\lfloor x_{i}+x_{i+k}\right\rfloor
$$

是一个整数, 由引理可知

$$
\sum_{i=1}^{n}\left\{x_{i}+x_{i+k}\right\} \leq n-1
$$

故

$$
\sum_{1 \leq i<j \leq n}\left\{x_{i}+x_{j}\right\} \leq \frac{(n-1)^{2}}{2}
$$

当 $x_{1}=x_{2}=\cdots=x_{n}=\frac{n-1}{2 n}$ 时等号成立. 事实上, 由 $n$ 是奇数, $\left\{x_{i}\right\}=\frac{n-1}{2 n}<\frac{1}{2}$,则

$$
\sum_{1 \leq i<j \leq n}\left\{x_{i}+x_{j}\right\}=\sum_{1 \leq i<j \leq n} \frac{n-1}{n}=\frac{(n-1)^{2}}{2} .
$$

故对一般的问题最大值为 $\frac{(n-1)^{2}}{2}$.

特别的, 当 $n=2019$ 时, 所求最大值为 2036162 .

评注 这是一道中等难度的代数题, 考场上有 $32 \%$ 的学生做对此题, 该题比我们预期的难度要大, 可能的原因是学生不大擅长处理带有组合意味的不等式.本题的关键在于按下标差整理和式, 对每一种下标差寻找一个局部不等式, 利用引理即可得出结论.

此题的背景是 2014 年北京大学挑战赛一道题:

$$
a_{1}+a_{2}+\cdots+a_{6}=2014 \text {, 求 } \sum_{1 \leq i<j \leq 6}\left\lfloor a_{i}+a_{j}\right\rfloor \text { 的最小值. }
$$

近几年也出现了不少与小数部分之和有关的竞赛题,例如 2018 年中国西部数学邀请赛第二题:

设整数 $n \geq 2$, 正整数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $x_{1} x_{2} \cdots x_{n}=1$, 证明:

$$
\left\{x_{1}\right\}+\left\{x_{2}\right\}+\cdots+\left\{x_{n}\right\}<\frac{2 n-1}{2} .
$$

题 2 如图, 锐角 $\triangle A B C$ 中, $H$ 为垂心, $E, F$ 在 $B C$ 上, $E H \perp H F$, 延长 $E H$ 与 $A C$ 交于 $M$, 延长 $F H$ 与 $A B$ 交于 $N . H_{1}, H_{2}$ 为 $\triangle B N F, \triangle C M E$ 的垂心.证明: $H_{1}, H, H_{2}$ 共线.


证明 1 (浙江乐清知临中学韩新竹) 延长 $B H_{1} 、 C H_{2}$ 分别与 $N F 、 E M$ 交于 $P 、 Q$. 由于 $B P, E M$ 都与 $F N$ 垂直, 则有 $B P / / E M$.

同理, $C Q / / N F, B H / / E H_{2}, C H / / F H_{1}$. 所以

$$
\triangle B P F \sim \triangle E Q C, \triangle B P H \sim \triangle E Q H_{2}, \triangle C Q H \sim \triangle F P H_{1} .
$$

故

$$
\frac{H_{1} P}{H Q}=\frac{P F}{Q C}=\frac{B P}{E Q}=\frac{P H}{Q H_{2}}
$$

从而 $\triangle H_{1} P H$ 与 $\triangle H Q H_{2}$ 相似.

注意到 $H_{1} P / / H Q, P H / / Q H_{2}$, 那么 $\triangle H_{1} P H$ 与 $\triangle H Q H_{2}$ 位似. 所以 $H_{1} H / / H H_{2}$. 故 $H_{1} 、 H 、 H_{2}$ 三点共线.

## 证明 2 (李先颖)


设直线 $B H$ 与 $A C$ 交于 $P$, 直线 $C H$ 与 $A B$ 交于 $Q$, 直线 $B H_{1}$ 与 $C H_{2}$ 交于 $S$, 直线 $P H_{2}$ 与 $Q H_{1}$ 交于 $T$. 注意到

$$
\begin{aligned}
\tan \angle C P H_{2} & =\frac{H_{2} X}{X P}=\frac{H_{2} X}{X M} \cdot \frac{X M}{X P}=\cot \angle C \cdot \frac{E M}{E H} \\
& =\cot \angle C \cdot \frac{E C \cdot \frac{\sin \angle C}{\sin \angle E M C}}{E C \cdot \frac{\cos \angle B}{\sin \angle E H C}}=\frac{\sin \angle E H C}{\sin \angle E M C},
\end{aligned}
$$

同理,

$$
\tan \angle B Q H_{1}=\frac{\sin \angle F H B}{\sin \angle F N B}
$$

故

$$
\tan \angle C P H_{2} \cdot \tan \angle B Q H_{1}=\frac{\sin \angle E H C \cdot \sin \angle F H B}{\sin \angle E M C \cdot \sin \angle F N B}=1,
$$

最后一个等号用了 $\angle E H C=\pi-\angle F N B, \angle F H B=\pi-\angle E M C$.

所以 $\angle C P H_{2}+\angle B Q H_{1}=\frac{\pi}{2}$, 这说明点 $T$ 在以 $B C$ 为直径的圆上. 又注意到 $B H_{1} \perp F N, C H_{2} / / F N$, 则 $B H_{1} \perp C H_{2}, \angle B S C=\frac{\pi}{2}$. 那么 $P, Q, S, T$ 均在以 $B C$ 为直径的圆上, 对圆内接六边形 $B P T Q C S$ 使用 Pacal 定理知 $H, H_{1}, H_{2}$ 共线.

评注 这是一道简单的几何题, 考场上约 $70 \%$ 的学生做对. 上述两个解法均十分巧妙, 解法 1 通过找相似三角形和导比例来证明 $\triangle H_{1} P H$ 与 $\triangle H Q H_{2}$ 位似,从而证得结论; 解法 2 直接找到一个圆内接六边形, 使 $H, H_{1}, H_{2}$ 分别是这个六边形三组对边的交点, 由 Pascal 定理可以证得结论.

题 3 设 $n, r$ 为正整数, $n>r$. 将圆周上给定的 $2 n$ 个点染 $n$ 种颜色, 每色染 2 个点, 且任何两个同色点之间恰有 $r$ 个点.

(1) 试问: $n, r$ 能否同为奇数?

(2) 如果 $r+1$ 为质数, 求 $n$ 的所有可能取值.

解 (浙江乐清知临中学韩新秝) 我们证明: $n, r$ 满足的充要条件为

$$
v_{2}(n) \geq v_{2}(r+1) \text {. }
$$

其中 $v_{2}(m)$ 表示 $m$ 所含的 2 的幂次.

构造 $2 n$ 个顶点的有向图 $G$, 其顶点对应 $1,2, \cdots, 2 n$. 对顶点 $i, j$, 连边 $i \rightarrow j$当且仅当

$$
j-i \equiv r+1 \quad(\bmod 2 n)
$$

当 $r+1=n$ 时, 允许同时有边 $i \rightarrow j$ 和 $j \rightarrow i$.
题设中的条件等价于可在 $G$ 中找 $n$ 条有向边, 不重不漏地覆盖了 $G$ 的所有顶点. 注意到图 $G$ 由若干圈组成, 且对任意顶点 $i$, 含该点的有向圈长度 $l$ 即为满足 $l(r+1) \equiv 0(\bmod 2 n)$ 的最小正整数, 即 $\frac{2 n}{(2 n, r+1)}$. 于是图 $G$ 恰由 $(2 n, r+1)$个有向圈组成, 且每个有向圈长度为 $\frac{2 n}{(2 n, r+1)}$.

题设中的条件等价于 $G$ 所含的每个有向圈均为偶圈, 即 $\frac{2 n}{(2 n, r+1)}$ 为偶数, 这等价于 $v_{2}(2 n)>v_{2}(r+1)$, 即 $v_{2}(n) \geq v_{2}(r+1)$.

(1) 由 $(*)$ 知, $n, r$ 不能同时为奇数.

(2) 若 $r+1$ 为素数, 分两种情况.

当 $r+1=2$ 时, 由 $(*), n$ 为一切正偶数.

当 $r+1$ 为奇素数时, 由 $(*), n$ 为一切大于 $r$ 的整数.

评注 这是一道中等难度的组合题, 考场上约 $36 \%$ 的学生做对. 上述解法直接讨论了一般的情况, 再把问题转换成图论问题后观察到题设条件等价于图中每个有向圈均为偶圈, 从而得到了一般问题的充要条件为 $v_{2}(n) \geq v_{2}(r+1)$, 再去解决原题的两问就十分容易了.

题 4 证明: 存在全体正整数的一个排列 $a_{1}, a_{2}, \cdots$, 使得对任意自然数 $i$, 均有

$$
\left(a_{i}, a_{i+1}\right) \geq \frac{i}{2}
$$

证明 我们用归纳法构造满足条件的排列.

取 $a_{1}=1, a_{2}=2$, 成立.

假设对 $k \in \mathbb{N}^{*}$,已经选取了 $a_{1}, a_{2}, \cdots, a_{2 k}$ 满足题目条件.

取 $a_{2 k+2}$ 为不在 $a_{1}, a_{2}, \cdots, a_{2 k}$ 中出现的最小正整数, 再取 $a_{2 k+1}$ 为不在 $a_{1}, a_{2}, \cdots, a_{2 k}, a_{2 k+2}$ 中出现的某个 $a_{2 k}, a_{2 k+2}$ 的公倍数.

下面说明这样的构造满足要求.

由构造的方法知, 每个正整数恰在 $\left\{a_{i}\right\}_{i \in \mathbb{N}^{*}}$ 中出现一次, 故是全体正整数的一个排列. 另外, 对任意 $s \in \mathbb{N}^{*}$, 有

$$
a_{2 s}>a_{2 s-2}>\cdots>a_{2}=2,
$$

故 $a_{2 s} \geq s+1$. 于是对任意 $j \in \mathbb{N}^{*}$, 均有

$$
\begin{gathered}
\left(a_{2 j}, a_{2 j+1}\right)=a_{2 j} \geq j+1 \geq \frac{2 j}{2} \\
\left(a_{2 j+1}, a_{2 j+2}\right)=a_{2 j+2} \geq j+2 \geq \frac{2 j+1}{2} .
\end{gathered}
$$

从而它满足要求. 故结论成立.

评注 这是一道中等难度的数论构造题, 考场上约 $42 \%$ 的学生做对. 用归纳法来构造是比较自然的想法, 为了满足题目条件在归纳过渡可取一项为前面没有出现的最小正整数, 再取一项使得它是前项和后项的公倍数, 故只需分奇数位和偶数位构造即可满足要求.

本题是 2011 年中国国家集训队选拔考试第五题的逆向讨论, 原题如下:

设 $a_{1}, a_{2}, \cdots$ 为全体正整数的一个排列. 证明: 存在无穷多个正整数 $i$, 使得

$$
\left(a_{i}, a_{i+1}\right) \leqslant \frac{3}{4} i
$$

题 5. 设 $n$ 是正整数, $2 n$ 个实数 $x_{i}, y_{i}(1 \leq i \leq n)$ 满足

$$
\sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} y_{i}^{2}=1
$$

已知 $0<\lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{n}, 1 \in\left[\lambda_{1}, \lambda_{n}\right]$. 证明:

$$
\lambda_{1} \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}} \leq \lambda_{n}
$$

证明 1 (湖北武钢三中袁祉祯) 由于 $0<\lambda_{1} \leq \cdots \leq \lambda_{n}$, 那么

$$
\lambda_{1} \sum_{i=1}^{n} x_{i}^{2} \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2} \leq \lambda_{n} \sum_{i=1}^{n} x_{i}^{2}
$$

要证原不等式只需证

$$
\lambda_{1}\left(1-\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}\right) \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}} \leq \lambda_{n}\left(1-\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}\right)
$$

将条件 $\sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} y_{i}^{2}=1$ 代入其中, 上式等价于

$\lambda_{1}\left(\sum_{i=1}^{n} x_{i}^{2}-\frac{\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} y_{i}^{2}}\right) \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}} \leq \lambda_{n}\left(\sum_{i=1}^{n} x_{i}^{2}-\frac{\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} y_{i}^{2}}\right)$,

将上式同乘 $\sum_{i=1}^{n} y_{i}^{2}$, 利用拉格朗日恒等式可知上式等价于

$$
\lambda_{1} \sum_{i=1}^{n} \lambda_{i} y_{i}^{2} \sum_{1 \leq j<k \leq n}\left(x_{j} y_{k}-x_{k} y_{j}\right)^{2} \leq \sum_{i=1}^{n} y_{i}^{2} \sum_{1 \leq j<k \leq n}\left(x_{j} y_{k}-x_{k} y_{j}\right)^{2} \lambda_{j} \lambda_{k}
$$

$$
\leq \lambda_{n} \sum_{i=1}^{n} \lambda_{i} y_{i}^{2} \sum_{1 \leq j<k \leq n}\left(x_{j} y_{k}-x_{k} y_{j}\right)^{2}
$$

下证上式对实数 $x_{1}, \cdots, x_{n}, y_{1}, \cdots, y_{n}$ 和 $0 \leq \lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{n}$ 成立.

$n=1$ 时, 上式成立. 若 $y_{1}, y_{2}, \cdots, y_{n}$ 中有一项为 0 , 设 $y_{j_{0}}=0$, 则由

$$
\lambda_{1} x_{j_{0}}^{2} \sum_{j=1}^{n} \lambda_{j} y_{j}^{2} \sum_{i=1}^{n} y_{i}^{2} \leq \sum_{i=1}^{n} y_{i}^{2} \sum_{j=1}^{n} \lambda_{j} \lambda_{j_{0}} x_{j_{0}}^{2} y_{j}^{2} \leq \lambda_{n} x_{j_{0}}^{2} \sum_{j=1}^{n} \lambda_{j} y_{j}^{2} \sum_{i=1}^{n} y_{i}^{2}
$$

知, 只需证明除去 $x_{j_{0}}, l_{j_{0}}$ 后 $n-1$ 时不等式的情形, 这样不断进行下去故可不妨设 $\prod_{j=1}^{n} y_{j} \neq 0$.

记 $a_{i}=y_{i}^{2}, b_{i}=\lambda_{i} y_{i}^{2}, u_{i}=\frac{x_{i}}{y_{i}}(i=1,2, \cdots, n)$. 即证:

$$
\begin{aligned}
\min _{1 \leq l \leq n}\left\{\frac{b_{l}}{a_{l}}\right\} \sum_{i=1}^{n} b_{i} \sum_{1 \leq j<k \leq n} a_{j} a_{k}\left(u_{j}-u_{k}\right)^{2} & \leq \sum_{i=1}^{n} a_{i} \sum_{1 \leq j<k \leq n} b_{j} b_{k}\left(u_{j}-u_{k}\right)^{2} \\
& \leq \max _{1 \leq l \leq n}\left\{\frac{b_{l}}{a_{l}}\right\} \sum_{i=1}^{n} b_{i} \sum_{1 \leq j<k \leq n} a_{j} a_{k}\left(u_{j}-u_{k}\right)^{2}
\end{aligned}
$$

下面在一般意义下证明上述不等式(而不是题目限制条件下). 由对称性, 只需证右边不等式即可.

由于不等式关于所有的 $a_{i}$ 或 $b_{i}$ 是齐次的, 不妨设 $\max \left\{\frac{b_{i}}{a_{i}}\right\}=1$, 则 $a_{i} \geq b_{i}>0(i=1,2, \cdots, n)$.

作增量代换 $x_{i}=a_{i}-b_{i}(i=1,2, \cdots, n)$, 则 $x_{i} \geq 0$. 将 $a_{i}=b_{i}+x_{i}$ 代入可得

$$
\begin{aligned}
& \sum_{i=1}^{n} b_{i} \sum_{1 \leq j<k \leq n} a_{j} a_{k}\left(u_{j}-u_{k}\right)^{2}-\sum_{i=1}^{n} a_{i} \sum_{1 \leq j<k \leq n} b_{j} b_{k}\left(u_{j}-u_{k}\right)^{2} \\
= & \sum_{i=1}^{n} b_{i} \sum_{1 \leq j<k \leq n}\left(b_{j} x_{k}+b_{k} x_{j}+x_{j} x_{k}\right)\left(u_{j}-u_{k}\right)^{2}-\sum_{i=1}^{n} x_{i} \sum_{1 \leq j<k \leq n} b_{j} b_{k}\left(u_{j}-u_{k}\right)^{2} \\
\geq & \sum_{i=1}^{n} b_{i} \sum_{1 \leq j<k \leq n}\left(b_{j} x_{k}+b_{k} x_{j}\right)\left(u_{j}-u_{k}\right)^{2}-\sum_{i=1}^{n} x_{i} \sum_{1 \leq j<k \leq n} b_{j} b_{k}\left(u_{j}-u_{k}\right)^{2} \\
= & \sum_{i=1}^{n} x_{i}\left(\sum_{k=1}^{n} b_{k} \sum_{j=1}^{n} b_{j}\left(u_{i}-u_{j}\right)^{2}-\sum_{1 \leq j<k \leq n} b_{j} b_{k}\left(u_{j}-u_{k}\right)^{2}\right) \\
= & \sum_{i=1}^{n} x_{i}\left(\sum_{k=1}^{n} b_{k}\left(u_{i}-u_{k}\right)\right)^{2} \geq 0,
\end{aligned}
$$

得证.

证明 2 (山西大学附属中学王永喜) 设

$$
f\left(\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}\right)=\sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}}
$$

对任意 $1 \leq k \leq n$, 有

$$
\begin{aligned}
\frac{\partial f}{\partial \lambda_{k}} & =x_{k}^{2}-\frac{2\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)\left(x_{k} y_{k}\right)\left(\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}\right)-\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right)^{2} \cdot y_{k}^{2}}{\left(\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}\right)^{2}} \\
& =\frac{\left(x_{k}\left(\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}\right)-\left(\sum_{i=1}^{n} \lambda_{i} x_{i} y_{i}\right) \cdot y_{k}\right)^{2}}{\left(\sum_{i=1}^{n} \lambda_{i} y_{i}^{2}\right)^{2}}
\end{aligned}
$$

$\geq 0$,

故 $f$ 关于每个 $\lambda_{k}$ 都是单调递增的, 从而当所有 $\lambda_{k}$ 取 $\lambda_{1}$ 时 $f$ 取最小值, 当所有 $\lambda_{k}$ 取 $\lambda_{n}$ 时 $f$ 取最大值.

当所有 $\lambda_{k}$ 取 $\lambda_{1}$ 时,

$$
f=\sum_{i=1}^{n} \lambda_{1} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}-\lambda_{1}\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}=\lambda_{1}+\left(1-\lambda_{1}\right)\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2} \geq \lambda_{1},
$$

当所有 $\lambda_{k}$ 取 $\lambda_{n}$ 时,

$$
f=\sum_{i=1}^{n} \lambda_{n} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}-\lambda_{n}\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2}=\lambda_{n}+\left(1-\lambda_{n}\right)\left(\sum_{i=1}^{n} x_{i} y_{i}\right)^{2} \leq \lambda_{n} .
$$

综上可知, 结论成立.

证明 3 (北京大学 王逸轩) 我们证明比原题更强的结论:

$$
\begin{aligned}
\lambda_{1} & \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} l_{i}\right)^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} l_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} l_{i}^{2}} \\
& \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} l_{i}\right)^{2}+\left(\sum_{i=1}^{n} \lambda_{i} l_{i}\right)^{2}-2\left(\sum_{i=1}^{n} \lambda_{i} x_{i} l_{i}\right)\left(\sum_{i=1}^{n} x_{i} l_{i}\right) \\
& \leq \lambda_{n}
\end{aligned}
$$

对于 $(*)$ 中间的不等式, 由均值不等式

$$
\left(\sum_{i=1}^{n} \lambda_{i} l_{i}^{2}\right)\left(\sum_{i=1}^{n} x_{i} l_{i}\right)^{2}+\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} l_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} l_{i}^{2}} \geq 2\left(\sum_{i=1}^{n} \lambda_{i} x_{i} l_{i}\right)\left(\sum_{i=1}^{n} x_{i} l_{i}\right) .
$$

故不等式成立.
对于 $(*)$ 最左边的不等式, 令 $u_{i}=\lambda_{i}-\lambda_{1}$, 那么 $u_{i} \geq 0$. 记 $b=\sum_{i=1}^{n} x_{i} l_{i}$, 则

$$
\begin{aligned}
& \lambda_{1} \leq \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} k_{i}\right)^{2}-\frac{\left(\sum_{i=1}^{n} \lambda_{i} x_{i} l_{i}\right)^{2}}{\sum_{i=1}^{n} \lambda_{i} l_{i}^{2}} \\
\Leftrightarrow & 0 \leq \sum_{i=1}^{n}\left(\lambda_{i}-\lambda_{1}\right) x_{i}^{2}+b^{2}-\frac{\left[\sum_{i=1}^{n}\left(\lambda_{1}+u_{i}\right) x_{i} l_{i}\right]^{2}}{\sum_{i=1}^{n}\left(\lambda_{1}+u_{i}\right) l_{i}^{2}} \\
\Leftrightarrow & 0 \leq \sum_{i=1}^{n} u_{i} x_{i}^{2}+b^{2}-\frac{\left(\sum_{i=1}^{n} u_{i} x_{i} l_{i}+\lambda_{1} b\right)^{2}}{\sum_{i=1}^{n} u_{i} l_{i}^{2}+\lambda_{1}} \\
\Leftrightarrow & \left(\sum_{i=1}^{n} u_{i} x_{i}^{2}+b^{2}\right)\left(\sum_{i=1}^{n} u_{i} l_{i}^{2}+\lambda_{1}\right) \geq\left(\sum_{i=1}^{n} u_{i} x_{i} l_{i}+\lambda_{1} b\right)^{2} .
\end{aligned}
$$

由于 $0<\lambda_{1} \leq 1$, 那么 $\lambda_{1} \geq \lambda_{1}^{2}$, 再结合柯西不等式知

$$
\begin{aligned}
\left(\sum_{i=1}^{n} u_{i} x_{i}^{2}+b^{2}\right)\left(\sum_{i=1}^{n} u_{i} l_{i}^{2}+\lambda_{1}\right) & \geq\left(\sum_{i=1}^{n} u_{i} x_{i}^{2}+b^{2}\right)\left(\sum_{i=1}^{n} u_{i} l_{i}^{2}+\lambda_{1}^{2}\right) \\
& \geq\left(\sum_{i=1}^{n} u_{i} x_{i} l_{i}+\lambda_{1} b\right)^{2} .
\end{aligned}
$$

故不等式成立.

对于 $(*)$ 最右边的不等式, 令 $v_{i}=\lambda_{n}-\lambda_{i}$, 则 $v_{i} \geq 0 . b$ 的记号与之前一样, 则

$$
\begin{aligned}
& \sum_{i=1}^{n} \lambda_{i} x_{i}^{2}+\left(\sum_{i=1}^{n} x_{i} l_{i}\right)^{2}+\left(\sum_{i=1}^{n} \lambda_{i} l_{i}^{2}\right)\left(\sum_{i=1}^{n} x_{i} l_{i}\right)^{2}-2\left(\sum_{i=1}^{n} \lambda_{i} x_{i} l_{i}\right)\left(\sum_{i=1}^{n} x_{i} l_{i}\right) \leq \lambda_{n} \\
\Leftrightarrow & b^{2}+\left(\sum_{i=1}^{n}\left(\lambda_{n}-v_{i}\right) l_{i}^{2}\right) b^{2}-2\left(\sum_{i=1}^{n}\left(\lambda_{n}-v_{i}\right) x_{i} \lambda_{i}\right) b \leq \sum_{i=1}^{n}\left(\lambda_{n}-\lambda_{i}\right) x_{i}^{2} \\
\Leftrightarrow & b^{2}+\lambda_{n} b^{2}-\sum_{i=1}^{n} v_{i} l_{i}^{2} b^{2}-2 \lambda_{n} b^{2}+2 \sum_{i=1}^{n} v_{i} x_{i} l_{i} b \leq \sum_{i=1}^{n} v_{i} x_{i}^{2} \\
\Leftrightarrow & b^{2} \leq \lambda_{n} b^{2}+\sum_{i=1}^{n} v_{i} x_{i}^{2}+\sum_{i=1}^{n} v_{i} l_{i}^{2} b^{2}-2 \sum_{i=1}^{n} v_{i} x_{i} l_{i} b \\
\Leftrightarrow & b^{2} \leq \lambda_{n} b^{2}+\sum_{i=1}^{n} v_{i}\left(x_{i}-l_{i} b\right)^{2} .
\end{aligned}
$$

由于 $v_{i} \geq 0, \lambda_{n} \geq 1$, 故不等式成立.

综上可知, (*)成立, 从而原不等式获证.

评注 这是一道非常困难的不等式问题,考场上约 $1 \%$ 的学生做对. 法 1 先用
题设条件对原不等式作齐次化处理, 再作变量代换后在一般意义下证明转化之后的不等式; 法 2 通过研究代数式关于 $\lambda_{k}$ 的单调性,把原不等式化简为 $\lambda_{k}$ 都取 $\lambda_{1}$ 或 $\lambda_{n}$ 的情形,最后把只需证明关于 $\lambda_{1}$ 或 $\lambda_{n}$ 的不等式即可; 法 3 非常巧妙,只需作适当的和式变形并结合柯西不等式和均值不等式就证明了结论.

题 6. 对边互不平行的四边形 $A B C D$ 内接于 $\odot O$. 设对角线 $A C, B D$ 交于点 $P$, 直线 $A D, B C$ 交于点 $E, M$ 是 $O P$ 的中点. 已知 $\triangle A O B, \triangle C O D, \triangle A P B$, $\triangle C P D$ 的外心共圆, 证明: 该圆圆心是 $\triangle O M E$ 的垂心.

证明 设 $O_{1}, O_{2}, O_{3}, O_{4}$ 分别是 $\triangle A O B, \triangle C O D, \triangle A P B, \triangle C P D$ 的外心, 设直线 $A B, D C$ 交于点 $F$, 设 $O_{1}, O_{2}, O_{3}, O_{4}$ 所共圆的圆心为 $O^{*}$.

第一步, 证明 $A C \perp B D$.



设 $\odot O_{1}$ 与 $\odot O_{2}$ 交于点 $O, Q$, 则由蒙日定理, $O, Q, F$ 三点共线. 因为 $O_{1} O_{2} \perp$ $O Q, O_{1} O_{3} \perp A B$, 所以 $\angle O_{2} O_{1} O_{3}=\angle O F A$.

设 $\odot O_{3}$ 与 $\odot O_{4}$ 交于点 $P, R$, 则由蒙日定理, $P, R, F$ 三点共线. 因为 $O_{3} O_{4} \perp$ $P R, O_{2} O_{4} \perp C D$, 所以 $\angle O_{2} O_{4} O_{3}=\angle P F D$.

因为 $O_{1}, O_{2}, O_{3}, O_{4}$ 四点共圆, 所以 $\angle O_{2} O_{1} O_{3}=\angle O_{2} O_{4} O_{3}$, 从而 $\angle O F A=$ $\angle P F D$.

设 $P$ 在 $\triangle A D F$ 中的等角共轭点是 $P^{\prime}$, 则 $\angle P^{\prime} F A=\angle P F D$, 所以 $P^{\prime}$ 在直线 $O F$ 上. 又

$$
\angle P^{\prime} A D=\angle P A B=\angle P D C=\angle P^{\prime} D A,
$$

所以 $P^{\prime}$ 在 $A D$ 的垂直平分线上. 于是 $P^{\prime}$ 是直线 $O F$ 与 $A D$ 的垂直平分线的交点, 所以 $P^{\prime}$ 与 $O$ 重合 (直线 $A D$ 与 $B C$ 不平行保证了 $O F$ 与 $A D$ 不垂直).

这样,

$$
\angle P D A+\angle P A D=\angle O D C+\angle P A D=90^{\circ} \text {, }
$$

所以 $A C \perp B D$. 此时 $O_{3}, O_{4}$ 分别是 $A B, C D$ 的中点.

第二步, 证明 $O^{*} E \perp O M$.



由 Brocard 定理, $O P \perp E F$, 所以只需证明 $O^{*}$ 在直线 $E F$ 上.

设 $O_{1} O_{3}$ 的垂直平分线与直线 $E F$ 交于点 $O^{\prime}, O_{2} O_{4}$ 的垂直平分线线与直线 $E F$ 交于点 $O^{\prime \prime}$. 只需证明 $O^{\prime}$ 与 $O^{\prime \prime}$ 重合, 这只需证明 $F O^{\prime}=F O^{\prime \prime}$.

事实上, 因为

$$
\begin{aligned}
F O^{\prime} & =\frac{O_{1} O_{3}}{2 \sin \angle E F A}, \quad F O^{\prime \prime}=\frac{O_{2} O_{4}}{2 \sin \angle E F D}, \\
O_{1} O_{3} & =\frac{A B}{2 \cot \angle O_{1} A B}=\frac{1}{2} \cdot A B \cdot|\cot \angle A O B| \\
O_{2} O_{4} & =\frac{C D}{2 \cot \angle O_{2} D C}=\frac{1}{2} \cdot C D \cdot|\cot \angle C O D|
\end{aligned}
$$

又 $\angle A O B+\angle C O D=180$, 所以

$$
\frac{F O^{\prime}}{F O^{\prime \prime}}=\frac{A B}{C D} \cdot \frac{\sin \angle E F D}{\sin \angle E F A}
$$

由正弦定理及 $\triangle E C D \sim \triangle E A B$,

$$
\frac{\sin \angle E F D}{\sin \angle E F A}=\frac{E C \cdot \frac{\sin \angle E C F}{E F}}{E A \cdot \frac{\sin \angle E A F}{E F}}=\frac{E C}{E A}=\frac{C D}{A B}
$$

所以

$$
\frac{F O^{\prime}}{F O^{\prime \prime}}=\frac{A B}{C D} \cdot \frac{C D}{A B}=1
$$

第三步, 证明 $O^{*} M \perp O E$.

熟知 $O O_{3} P_{4}$ 是平行四边形, 所以 $M$ 是 $O_{3} O_{4}$ 的中点. 这样, $O^{*} M \perp O_{3} O_{4}$,所以只需证明 $O_{3} O_{4} / / O E$.

事实上, 设 $\odot O_{3}$ 与 $\odot O_{4}$ 交于点 $P ; R$, 则熟知 $R$ 在 $O E$ 上, 且 $O R \perp P R$. 因为 $O_{3} O_{4} \perp P R$, 所以 $O_{3} O_{4} / / O R$.

综上, $O^{*}$ 是 $\triangle O M E$ 的垂心.



评注 这是一道有相当难度的几何问题, 考场上约 $5 \%$ 的学生做对. 本题的入手点是发现 $A C \perp B D$, 再逐步证明所述圆心 $O^{*}$ 是 $\triangle O M E$ 的垂心. 本题考察了圆的性质、Brocard 定理和三角计算等几何方法和技巧, 对学生的几何综合能力要求较高.

