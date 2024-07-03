# 群论在组合中的一个应用 

傅影硕

(华中师范大学第一附属中学, 430223)

群 $G$ 在集合 $X$ 上的作用定义为映射

$$
\begin{aligned}
G \times X & \rightarrow X \\
(g, x) & \mapsto g_{*} x
\end{aligned}
$$

并且这样的映射满足

$$
e_{*} x=x
$$

以及

$$
(g h)_{*} x=g_{*}\left(h_{*} x\right)
$$

对任意的 $g, h \in G$ 都成立. 注意到对任意 $g \in G, x \mapsto g_{*} x$ 是双射 (因为 $\left.g_{*}^{-1}\left(g_{*} x\right)=x\right)$. 我们记 $X^{g}:=\left\{x: g_{*} x=x\right\}$ 为 $g \in G$ 作用在 $X$ 上的不动点集, $G_{*} x:=\left\{g_{*} x: g \in G\right\}$ 为点 $x \in X$ 在群 $G$ 作用下的轨道. 若两个轨道相交, 则这两个轨道是同一个轨道 (因为式 (2)). 不同的点 $x, y \in X$ 可能具有相同的轨道.记所有的轨道为 $X / G$.

例 1. 有限集合上 $X$ 的对称群 $S_{X}$ (有限集合上的所有重排构成的群) 或置换群 (对称群的子群) 在 $X$ 的作用为 $\sigma_{*} x=\sigma(x), \sigma \in S_{X} . X / S_{X}=\{X\}$, 即 $X / S_{X}$ 只含 $X$ 这一个元素.

例 2. 欧氏空间 $\mathbb{R}^{n}$ 上的所有的可逆线性变换构成一个群 $G L(n)$. 我们令 $G L(n)$ 在 $\mathbb{R}^{n}$ 上的作用为 $A_{*} x=A x, A \in G L(n), x \in \mathbb{R}^{n} . X / \mathbb{R}^{n}=$ $\left\{\mathbb{R}^{n} \backslash\{o\},\{o\}\right\}$. 这里 $o$ 表示 $\mathbb{R}^{n}$ 中的原点.

引理 (Burnside). 设群 $G$ 作用在集合 $X$ 上. 对 $g \in G$, 设 $f\left(X^{g}\right)$ 表示 $g$在 $X$ 上的不动点的个数, 则有

$$
|X / G|=\frac{1}{|G|} \sum_{g \in G} f\left(X^{g}\right)
$$

这里 $|\cdot|$ 表示集合中元素的个数.
用 Burnside 引理可以求解哈佛一麻省理工数学竞赛 (HMMT) 中的一道组合试题 (其他方法亦可见 [1]).

问题. 给定 $1,2, \cdots, 2013$ 的一个排列 $\sigma$, 记 $f(\sigma)$ 表示 $\sigma$ 的不动点的个数,试求

$$
\sum_{\sigma \in S} f(\sigma)^{4}
$$

其中 $S$ 为 $1,2, \cdots, 2013$ 的所有排列的集合.

解 取 Burnside 引理中的集合 $X=S_{n}^{4}$, 群 $G$ 为 $S_{n}$ 上的对换群 $S . S$ 在集合 $S_{n}^{4}$ 的作用为 $\sigma_{*}(a, b, c, d)=(\sigma(a), \sigma(b), \sigma(c), \sigma(d))$. 那么 $\sigma$ 在 $X$ 上的不动点的个数为 $f(\sigma)^{4}$. 由 Burnside 引理,

$$
\sum_{\sigma \in S} f(\sigma)^{4}=|X / S| \cdot|S|
$$

其中 $|S|=n$ !. 下面只需要算出 $|X / S|$.

由于无论 $1 \leq i \leq n$ 取何值, 都有 $\{\sigma(i): \sigma \in S\}=S_{n}$. 因此, 对 $n \geq 4$, 枚举可得 $X / G$ 中的元素为

$$
\begin{aligned}
& S_{*}(1,1,1,1), \quad S_{*}(1,1,1,2), \quad S_{*}(1,1,2,1), \quad S_{*}(1,2,1,1), \quad S_{*}(2,1,1,1), \\
& S_{*}(1,1,2,2), \quad S_{*}(1,2,1,2), \quad S_{*}(1,2,2,1), \\
& S_{*}(3,3,1,2), \quad S_{*}(3,1,3,2), \quad S_{*}(3,1,2,3), \quad S_{*}(1,3,3,2), \quad S_{*}(1,3,2,3), \quad S_{*}(1,2,3,3), \\
& S_{*}(1,2,3,4), \\
& \text { 因此 } \sum_{\sigma \in S} f(\sigma)^{4}=15 \cdot n !, n \geq 4 .
\end{aligned}
$$

## 参考文献

[1] 冷岗松, 施柯杰, 一道 HMMT 组合试题的证明 [J]. 数学新星网, 2016.

