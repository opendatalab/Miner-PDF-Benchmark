数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2021 年丝绸之路数学竞赛解答与评析 

邓晓

(武汉市武钢三中, 430080)

本文给出 2021 年丝绸之路数学竞赛的解答与评析, 总体而言今年的试题比去年简单, 第 1,2 题为联赛简单题, 第 3 题为冬令营中 1,4 难度的题, 第 4 题为联赛中等偏难的题. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 给定一个由 0,1 组成的字符小节 $s$. 对任意正整数 $k$, 定义 $v_{k}$ 为由 0,1 组成的长度为 $k$ 的字符串中, $s$ 出现次数的最大值 (例如, $s=0110$, 则 $v_{7}=v_{8}=2$,这是因为 0110 在 0110110 和 01101100 中各出现了两次, 但你无法构造 0110 出现三次的长度为 7 或 8 的字符串). 已知对给定字符小节 $s$, 存在正整数 $n$, 使得 $v_{n}<v_{n+1}<v_{n+2}$. 求证: $s$ 中所有字符相同.
2. 对任意正整数 $m$, 证明不等式

$$
\left|\{\sqrt{m}\}-\frac{1}{2}\right| \geq \frac{1}{8(\sqrt{m}+1)},
$$

其中 $[x]$ 表示不超过实数 $x$ 的最大整数, $\{x\}=x-[x]$ 表示 $x$ 的小数部分.



3. 如图所示, 在 $\triangle A B C$ 中, $M$ 为 $A B$ 中点. $A C$ 上一点 $B_{1}$ 满足 $C B=C B_{1}$.三角形 $A B C$ 的外接圆 $\omega$ 和过三点 $B, M, B_{1}$ 的圆 $\omega_{1}$ 再次相交于点 $K$. 设 $Q$ 为修订日期: 2021-07-07.
$\omega$ 上弧 $\widehat{A C B}$ 的中点. 直线 $B_{1} Q$ 与 $B C$ 相交于点 $E$. 求证: $K C$ 平分 $B_{1} E$.
4. 已知 $x, y, z, t$ 均为整数, 且满足 $x^{2}+y^{2}=z^{2}+t^{2}, x y=2 z t$. 求证: $x y z t=0$.

## II . 解答与评注

题 1 给定一个由 0,1 组成的字符小节 $s$. 对任意正整数 $k$, 定义 $v_{k}$ 为由 0,1 组成的长度为 $k$ 的字符串中, $s$ 出现次数的最大值 (例如, $s=0110$, 则 $v_{7}=v_{8}=2$, 这是因为 0110 在 0110110 和 01101100 中各出现了两次, 但你无法构造 0110 出现三次的长度为 7 或 8 的字符串). 已知对给定字符小节 $s$, 存在正整数 $n$, 使得 $v_{n}<v_{n+1}<v_{n+2}$. 求证: $s$ 中所有字符相同.

证明 考虑长为 $n+2$ 的字符串, 其中 $s$ 出现了 $v_{n+2}$ 次. 不妨设最后一位为 0 (不然将 0 与 1 对换), 则必有一个 $s$ 包含这个 0 , 否则去掉最后一位, $s$ 出现的次数不变, 则有 $v_{n+1}=v_{n+2}$, 矛盾. 考虑这个字符串的倒数第二位, 若没有一个 $s$ 以倒数第二位为终点, 则去掉末两位, $s$ 出现的次数减少 1 次, 则有 $v_{n} \geq v_{n+2}-1$,与 $v_{n}<v_{n+1}<v_{n+2}$ 矛盾. 则也有一个 $s$ 以倒数第二位为终点.

所以, 倒数第二位 $=$ 最后一位 $=0 \Rightarrow$ 倒数第三位 $=\cdots=0$, 即 $s$ 中所有字符均为 0 .

命题得证!

评注 本题较为简单, 经过尝试容易发现考虑从 $n+2$ 到 $n+1$ 到 $n$ 的变化是关键.

题 2 对任意正整数 $m$, 证明不等式

$$
\left|\{\sqrt{m}\}-\frac{1}{2}\right| \geq \frac{1}{8(\sqrt{m}+1)},
$$

其中 $[x]$ 表示不超过实数 $x$ 的最大整数, $\{x\}=x-[x]$ 表示 $x$ 的小数部分.

证明 1 设 $k=[\sqrt{m}]$, 结合 $\left|t-\frac{1}{4}\right| \geq \frac{1}{4}$ ( $t$ 为整数) 知

$$
\begin{aligned}
\left|\{\sqrt{m}\}-\frac{1}{2}\right|=\left|\sqrt{m}-k-\frac{1}{2}\right| & =\frac{\left|m-\left(k+\frac{1}{2}\right)^{2}\right|}{\sqrt{m}+k+\frac{1}{2}}=\frac{\left|m-k^{2}-k-\frac{1}{4}\right|}{\sqrt{m}+[\sqrt{m}]+\frac{1}{2}} \\
& \geq \frac{\frac{1}{4}}{2 \sqrt{m}+\frac{1}{2}} \geq \frac{1}{8(\sqrt{m}+1)} .
\end{aligned}
$$

证明 2 设 $[\sqrt{m}]=k, \sqrt{m}=k+\frac{1}{2}+t$. 假设存在 $m \in \mathbb{N}^{*}$, 使

$$
\left|\{\sqrt{m}\}-\frac{1}{2}\right|<\frac{1}{8(\sqrt{m}+1)},
$$

即

$$
|t|<\frac{1}{8(\sqrt{m}+1)}
$$

设 $s=m-k^{2}-k$, 则 $s \in \mathbb{Z}$, 且

$$
s=f(t)=-t^{2}+2 \sqrt{m} t+\frac{1}{4}
$$

由 $f(t)$ 在 $t \in\left(-\frac{1}{8(\sqrt{m}+1)}, \frac{1}{8(\sqrt{m}+1)}\right)$ 单调递增, 知

$$
0<f\left(-\frac{1}{8(\sqrt{m}+1)}\right)<s<f\left(\frac{1}{8(\sqrt{m}+1)}\right)<1
$$

与 $s \in \mathbb{Z}$ 矛盾. 所以原不等式成立.

评注 本题具有迷惑性, 充分利用 $m \in \mathbb{Z},[\sqrt{m}] \in \mathbb{Z}$ 即可解出本题, 法 1 通过有理化技巧和 $\left|t-\frac{1}{4}\right| \geq \frac{1}{4}(t \in \mathbb{Z})$ 可将目标式巧妙地放缩出来, 法 2 思路常规,将整数部分设出来, 消元处理, 利用反证法, 结合二次函数知识可得矛盾.

题 3 在 $\triangle A B C$ 中, $M$ 为 $A B$ 中点. $A C$ 上一点 $B_{1}$ 满足 $C B=C B_{1} . \triangle A B C$的外接圆 $\omega$ 和过三点 $B, M, B_{1}$ 的圆 $\omega_{1}$ 再次相交于点 $K$. 设 $Q$ 为 $\omega$ 上弧 $\widehat{A C B}$的中点. 直线 $B_{1} Q$ 与 $B C$ 相交于点 $E$. 求证: $K C$ 平分 $B_{1} E$.

证明 1 (文振宇) 延长 $B B_{1}$ 交 $C K$ 于 $T$. 延长 $K C$ 交圆 $\omega_{1}$ 于 $R$, 设直线 $B B_{1}$ 交圆 $\omega$ 于另一点 $P, M R$ 交 $B B_{1}$ 于 $H, K C$ 交 $B_{1} E$ 于 $D$.



因为 $\angle B M R=\angle B K R=\angle B K C=\angle B A C$, 所以 $M R / / A C$.

又 $A M=M B$ 可得 $B H=B_{1} H$. 因为

$$
T B_{1} \cdot T B=T K \cdot T R, T P \cdot T B=T K \cdot T C .
$$

所以 $\frac{T R}{T C}=\frac{T B_{1}}{T P}$.
又 $B_{1} C / / H R$, 得 $\frac{T R}{T C}=\frac{T H}{T B_{1}}$. 进而,

$$
T B_{1}^{2}=T P \cdot T H=\left(T B_{1}-B_{1} P\right)\left(T B_{1}+B_{1} H\right),
$$

解得 $T B_{1}=\frac{B_{1} P \cdot B H}{B_{1} H-B_{1} P}$.

又

$$
\angle Q C E=\angle Q A B=\frac{180^{\circ}-\angle A Q B}{2}=\frac{180^{\circ}-\angle A C B}{2}=\angle C B B_{1} \text {, }
$$

所以 $C Q / / B B_{1}$, 且 $\triangle B C B_{1}$ 与 $\triangle B Q A$ 相似 $\Rightarrow \triangle B A B_{1}$ 与 $\triangle B Q C$ 相似, 所以有

$$
\frac{C Q}{B_{1} A}=\frac{B C}{B B_{1}}=\frac{B_{1} C}{B_{1} B} \Rightarrow C Q \cdot B_{1} B=B_{1} C \cdot B_{1} A
$$

由圆幕定理有 $B_{1} A \cdot B_{1} C=B_{1} B \cdot P B_{1}$, 两式比较得 $P B_{1}=C Q$.

通过计算，

$$
\begin{aligned}
\frac{B T}{B_{1} T} & =1+\frac{B B_{1}}{B_{1} T}=1+B B_{1} \cdot \frac{B_{1} H-B_{1} P}{B_{1} P \cdot B H} \\
& =1+\frac{2\left(B_{1} H-B_{1} P\right)}{B_{1} P}=\frac{B B_{1}}{B_{1} P}-1=\frac{B B_{1}}{C Q}-1,
\end{aligned}
$$

可得

$$
\frac{B T}{B_{1} T}=\frac{B E}{C E}-1=\frac{B C}{C E} .
$$

对 $\triangle B_{1} B E$ 和截线 $T D C$, 由梅涅劳斯定理知 $\frac{E C}{C B} \cdot \frac{B T}{T B_{1}} \cdot \frac{B_{1} D}{D E}=1$, 所以 $B_{1} D=D E$.命题得证!

证明 2 (杨梓豪) 设 $K C$ 交 $B_{1} E$ 于 $D$.

$$
\frac{B_{1} D}{D E}=\frac{B_{1} C \sin \angle B_{1} C D}{C E \sin \angle D C E}=\frac{B_{1} C \sin \angle A C K}{C E \sin \angle K A B}=\frac{B_{1} C \cdot A K}{C E \cdot K B} .
$$

所以, 要证 $B_{1} D=D E$, 只需证: $\frac{B_{1} C}{C E}=\frac{B K}{A K}$.



因为 $Q$ 为弧 $\widehat{A C B}$ 的中点, 所以 $Q A=Q B$. 结合 $\angle A Q B=\angle B_{1} C B$, 知
$\triangle B C B_{1}$ 与 $\triangle B Q A$ 相似 $\Rightarrow \triangle B A B_{1}$ 与 $\triangle B Q C$ 相似.

又

$$
\angle Q C E=\angle Q A B=\frac{180^{\circ}-\angle A C B}{2}=\angle C B B_{1},
$$

所以 $C Q / / B B_{1}$. 故

$$
\frac{B_{1} C}{C E}=\frac{B C}{C E}=\frac{B B_{1}-C Q}{C Q}=\frac{B B_{1}}{C Q}-1 .
$$

因为 $\triangle B A B_{1}$ 与 $\triangle B Q C$ 相似, 所以

$$
\frac{C Q}{A B_{1}}=\frac{B C}{B B_{1}}=\frac{\cos \frac{\angle A C B}{2}}{\sin \angle A C B}
$$

所以

$$
\frac{B B_{1}}{C Q}-1=\frac{B B_{1} \sin \angle A C B}{A B_{1} \cos \frac{\angle A C B}{2}}-1
$$

设 $\angle M K B=\alpha$, 则

$$
1=\frac{A M}{B M}=\frac{A K \sin \angle A K M}{B K \sin \angle B K M}=\frac{A K \sin (\angle A C B-\alpha)}{B K \sin \alpha},
$$

所以

$$
\frac{B K}{A K}=\sin \angle A C B \cdot \frac{\cos \alpha}{\sin \alpha}-\cos \angle A C B .
$$

又

$$
1=\frac{A M}{B M}=\frac{A B_{1} \sin \angle A B_{1} M}{B B_{1} \sin \angle M B_{1} B}=\frac{A B_{1} \sin \left(90^{\circ}+\frac{\angle A C B}{2}-\alpha\right)}{B B_{1} \sin \alpha},
$$

所以,

$$
\frac{B B_{1}}{A B_{1}}=\cos \frac{\angle A C B}{2} \cdot \frac{\cos \alpha}{\sin \alpha}+\sin \frac{\angle A C B}{2} .
$$

(3) $\times 2 \sin \frac{\angle A C B}{2}$ 代入

(2) 得 $\frac{B K}{A K}=2 \sin \frac{\angle A C B}{2} \cdot \frac{B B_{1}}{A B_{1}}-1$. 而由 (1) 知

$$
\frac{B B_{1}}{C Q}-1=2 \sin \frac{\angle A C B}{2} \cdot \frac{B B_{1}}{A B_{1}}-1,
$$

所以

$$
\frac{B_{1} C}{C E}=\frac{B K}{A K} .
$$

命题得证!

证明 3 (王玮杰) 作 $Q F / / B C$ 交 $B B_{1}$ 于点 $F$, 设 $K C$ 交 $B_{1} E$ 于 $D, Q B$ 的中点为 $N$, 延长 $K M$ 交圆 $\omega$ 于点 $T$.

因为 $Q$ 为弧 $\widehat{A C B}$ 的中点, 所以 $Q A=Q B$. 结合 $\angle A Q B=\angle B_{1} C B$ 知 $\triangle B C B_{1}$ 与 $\triangle B Q A$ 相似 $\Rightarrow \triangle B A B_{1}$ 与 $\triangle B Q C$ 相似, 且 $M, N$ 是一对相似对应点.



又

$$
\angle Q C E=\angle Q A B=\frac{180^{\circ}-\angle A C B}{2}=\angle C B B_{1}
$$

所以 $C Q / / B B_{1}$.

又 $Q F / / B C$, 得四边形 $Q F B C$ 为平行四边形, 进而 $F, N, C$ 三点共线.

因为

$$
\angle B_{1} F Q=\angle B_{1} B C=\angle A B Q=\angle A C Q=\angle B_{1} C Q,
$$

所以 $B_{1}, F, C, Q$ 四点共圆.

进一步,

$$
\angle C B_{1} Q=\angle C F Q=\angle N C B=\angle M B_{1} B=\angle M K B=\angle T K B=\angle T A B .
$$

又

$$
\angle B_{1} C E=180^{\circ}-\angle A C B=\angle A T B, \quad \angle A T M=\angle A C K=\angle B_{1} C D,
$$

所以 $\triangle A T B$ 与 $\triangle B_{1} C E$ 相似, 且 $M, D$ 是一对相似对应点, 所以 $D$ 为 $B_{1} E$ 的中点. 命题得证.

评注 本题有一定的难度, 纯几何的角度似乎还是要发现构造 $\triangle A T B$ 与 $\triangle B_{1} C E$ 的相似对应点, 以中点证中点, 从计算的角度好做一些, 但也要发现 $\triangle B A B_{1}$ 与 $\triangle B Q C$ 相似, $C Q / / B B_{1}$ 等几何性质. 法一结合要证的是中点, 利用梅氏定理, 将目标式转化证一组比值式相等, 而取出点 $T$ 后要导比例, 需熟悉两圆相交有平行的结构. 法二, 多次把线段边上的点分线段的比值, 通过三角形的面积转化为三角函数的比值, 利用几何性质将目标集中, 结合三角运算导出想要的结果, 比较典型的三角法. 法三, 若能想到构造相似对应点, 剩余的部分也还比较自然, 比较巧妙.
题 4 已知 $x, y, z, t$ 均为整数, 且满足 $x^{2}+y^{2}=z^{2}+t^{2}, x y=2 z t$. 求证: $x y z t=0$.

证明 (王迪) 假设 $x y z t \neq 0$, 可不妨设 $(x, y, z, t)$ 均为正整数 (否则用 $|x|,|y|,|z|,|t|$ 代替 $x, y, z, t)$. 进而可设 $x, y, z, t$ 为满足 $x^{2}+y^{2}=z^{2}+t^{2}$ (1), $x y=2 z t$ (2) 且使得 $x^{2}+y^{2}$ 最小的正整数解, 此时一定有 $(x, y, z, t)=1$.

由 (2) 知, $x, y$ 中必有一个数为偶数, 不妨设 $2 \mid x$, 若 $2 \mid y$, 则 $4|x y, 2| z t$,所以 $z, t$ 中有一个数为偶数, 再结合 (1) 知 $z, t$ 均为偶数, 矛盾! 所以 $y$ 为奇数.

由 (1) 知 $z, t$ 一奇一偶, 不妨设 $z$ 为偶数, $t$ 为奇数.

由 (2) 设

$$
\frac{x}{t}=\frac{2 z}{y}=\frac{2 q}{p},(p, 2 q)=1
$$

并设 $x=2 r q, t=r p, z=s q, y=s p$, 则 $s, p, r$ 为奇数, $q$ 为偶数, 且 $(s, r)=1$.代入 (1) 得,

$$
4 r^{2} q^{2}+s^{2} p^{2}=s^{2} q^{2}+r^{2} p^{2} \Rightarrow q^{2}\left(4 r^{2}-s^{2}\right)=p^{2}\left(r^{2}-s^{2}\right),
$$

结合 $\left(q^{2}, p^{2}\right)=1$ 知

$$
p^{2}\left|4 r^{2}-s^{2}, q^{2}\right| r^{2}-s^{2} \text {, 且 } \frac{4 r^{2}-s^{2}}{p^{2}}=\frac{r^{2}-s^{2}}{q^{2}}=m \text {. }
$$

又

$$
\left(4 r^{2}-s^{2}, r^{2}-s^{2}\right)=\left(3 r^{2}, r^{2}-s^{2}\right),\left(3 r^{2}, r^{2}-s^{2}\right) \mid 3\left(r^{2}, r^{2}-s^{2}\right)=3 .
$$

所以, $m \in\{-1,1,-3,3\}$.

$$
\begin{aligned}
& m=1 \text { 时, } 4 r^{2}-s^{2}=p^{2} \Rightarrow 0 \equiv s^{2}+p^{2} \equiv 2(\bmod 4), \text { 矛盾! } \\
& m=-1 \text { 时, } 4 r^{2}=s^{2}-p^{2} \equiv 0(\bmod 8) \Rightarrow 2 \mid r, \text { 矛盾! } \\
& m=-3 \text { 时, } 4 r^{2}-s^{2}=-3 p^{2} \Rightarrow 0 \equiv 1-3 \equiv-2(\bmod 4), \text { 矛盾! }
\end{aligned}
$$

对于 $m=3$ 的情形, 有 $4 r^{2}-s^{2}=3 p^{2}, r^{2}-s^{2}=3 q^{2}$, 所以

$$
p^{2}=q^{2}+r^{2}, p^{2}=4 q^{2}+s^{2},
$$

又 $(p, 2 q)=1$, 对两个式子分别利用本原勾股数定理, 知存在正整数 $m, n$,使得 $p=m^{2}+n^{2}, q=2 m n$. 同样存在正整数 $u, v$, 使得 $p=u^{2}+v^{2}, q=u v$.

所以

$$
m^{2}+n^{2}=u^{2}+v^{2}, 2 m n=u v \text {, 且 } u^{2}+v^{2}=p<4 q^{2} r^{2}+s^{2} p^{2}=x^{2}+y^{2} \text {, }
$$

与 $x^{2}+y^{2}$ 的最小性矛盾! 故原题结论成立. 命题得证!
评注 本题有一定的难度, 综合考查不定方程的知识, 由题目的形式可联想到无穷递降法导矛盾, 另外对于 $x y=2 z t$, 结合奇偶性分析可设 $\frac{x}{t}=\frac{2 z}{y}=\frac{2 q}{p}$, $(p, 2 q)=1$ 也是常见的技巧. 最后通过本原勾股数定理导出我们需要的结构.

