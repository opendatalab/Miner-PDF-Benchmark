# 第四十四期问题征解解答与点评 

张端阳

第一题 在锐角非等腰 $\triangle A B C$ 中, $A D, B E, C F$ 是高, $H$ 是垂心. $D^{\prime}$ 是 $D$ 关于 $E F$ 的对称点, $O_{1}$ 是 $\triangle A D^{\prime} H$ 的外心, 类似定义点 $O_{2}, O_{3} . \Gamma_{1}$ 是过 $O_{2}, O_{3}$ 且圆心在直线 $A D$ 上的圆, 类似定义圆 $\Gamma_{2}, \Gamma_{3}$. 证明: $\Gamma_{1}, \Gamma_{2}, \Gamma_{3}$ 交于一点.

(人大附中学生 方大容 占扬 孙家瑞 供题)

证明 (根据深圳中学邓博文同学的解答整理):



设 $\triangle A B C$ 的九点圆圆心为 $V$, 我们证明 $V$ 是 $\Gamma_{1}, \Gamma_{2}, \Gamma_{3}$ 的公共点.

设 $V$ 关于 $A D, B E, C F$ 的对称点分别为 $V_{1}, V_{2}, V_{3}$. 下面依次证明 (1) $V_{1}$ 在 $\odot O_{1}$ 上; (2) $V_{2}, V_{3}, O_{1}$ 共线; (3) $V, V_{1}, O_{2}, O_{3}$ 共圆.

(1) 因为 $V$ 是 $\triangle D E F$ 的外心, 且由 $H D$ 平分 $\angle E D F$ 知 $V_{1} D$ 和 $V D$ 是 $\angle E F D$的等角线, 所以 $V_{1} D \perp E F$, 于是 $D, V_{1}, D^{\prime}$ 共线.



易知 $\triangle D V F \sim \triangle D E D^{\prime}, \triangle D H F \sim \triangle D E A$, 所以

$$
D V_{1} \cdot D D^{\prime}=D V \cdot D D^{\prime}=D E \cdot D F=D H \cdot D A \text {. }
$$

从而 $V_{1}, D^{\prime}, A, H$ 共圆, 即 $V_{1}$ 在 $\odot O_{1}$ 上.

同理, $V_{2}$ 在 $\odot O_{2}$ 上, $V_{3}$ 在 $\odot O_{3}$ 上.

为了证明 $(2),(3)$, 我们需要一个引理.

引理 在 $\triangle A B C$ 中, $O, V, H$ 分别是外心、九点圆圆心、垂心, $R$ 是外接圆半径. 设 $A O$ 的垂直平分线与直线 $B C$ 交于点 $D$, 则 $\angle A D O=2 \angle V A H$, 且

$$
C D \sin \angle O A H=2 R \sin ^{2} B-\frac{R}{2} .
$$



证明 设 $O$ 关于 $B C$ 的对称点是 $O^{\prime}$, 则 $O O^{\prime}$ 与 $A H$ 平行且相等, 于是 $A, V, O^{\prime}$共线. 由 $D A=D O=D O^{\prime}$, 知 $\angle A D O=2 \angle A O^{\prime} O=2 \angle V A H$.

设 $A O$ 的垂直平分线与 $A C, A O$ 分别交于点 $P, Q$. 由 $A O \perp D P, A H \perp D C$ 知 $\angle O A H=\angle P D C$, 所以

$$
\begin{aligned}
C D \sin \angle O A H & =C D \sin \angle P D C=P C \sin \angle C P D \\
& =(A C-A P) \sin \angle A P Q \\
& =2 R \sin B \cdot \sin B-A Q
\end{aligned}
$$

$$
=2 R \sin ^{2} B-\frac{R}{2}
$$

引理证毕.



(2) 由 $H V=H V_{1}=H V_{2}=H V_{3}$ 知 $V, V_{1}, V_{2}, V_{3}$ 共圆且 $H$ 是圆心, 所以

$$
\begin{aligned}
\angle V_{2} V_{1} V_{3} & =\frac{1}{2} \angle V_{2} H V_{3}=\frac{1}{2}\left(\angle V H V_{2}+\angle V H V_{3}\right) \\
& =\angle V H B+\angle V H F=\angle B H F=\angle B A C .
\end{aligned}
$$

同理 $\angle V_{1} V_{2} V_{3}=\angle A B C$, 所以 $\triangle V_{1} V_{2} V_{3} \sim \triangle A B C$.

设 $X, Y$ 分别是 $\triangle V_{1} V_{2} V_{3}$ 的九点圆圆心和垂心(图中未标出), 则由相似, $\angle V A H=\angle X V_{1} Y$. 这样,

$$
\angle V_{1} O_{1} H=2 \angle V_{1} A H=2 \angle V A H=2 \angle X V_{1} Y \text {. }
$$

又 $O_{1}$ 在 $V_{1} H$ 的垂直平分线上, 所以对 $\triangle V_{1} V_{2} V_{3}$ 用引理得, $V_{2}, V_{3}, O_{1}$ 共线.

同理, $V_{3}, V_{1}, O_{2}$ 和 $V_{1}, V_{2}, O_{3}$ 分别共线.



(3) 由三弦定理逆定理, 只需证明

$$
V V_{1} \sin \angle O_{2} V_{1} O_{3}+O_{3} V_{1} \sin \angle O_{2} V_{1} V=O_{2} V_{1} \sin \angle O_{3} V_{1} V
$$

即

$$
V V_{1} \sin \angle V_{3} V_{1} V_{2}+O_{3} V_{1} \sin \angle V_{3} V_{1} V=O_{2} V_{1} \sin \angle V_{2} V_{1} V
$$

设 $R_{1}, R_{2}$ 分别是 $\triangle A B C, \triangle V_{1} V_{2} V_{3}$ 的外接圆半径, 则 $R_{2}=V H=\frac{1}{2} O H$.

由 $\angle V_{3} V_{1} V=\frac{1}{2} \angle V_{3} H V=\angle F H O$ 知

$$
\sin \angle V_{3} V_{1} V=\sin \angle O C H \cdot \frac{O C}{O H}=\sin \angle H V_{3} Y \cdot \frac{R_{1}}{2 R_{2}} .
$$

又对 $\triangle V_{1} V_{2} V_{3}$ 用引理得

$$
O_{3} V_{1} \sin \angle H V_{3} Y=2 R_{2} \sin ^{2} \angle V_{1} V_{2} V_{3}-\frac{R_{2}}{2}=2 R_{2} \sin ^{2} B-\frac{R_{2}}{2},
$$

所以

$$
O_{3} V_{1} \sin \angle V_{3} V_{1} V=\frac{R_{1}}{2 R_{2}}\left(2 R_{2} \sin ^{2} B-\frac{R_{2}}{2}\right)=R_{1}\left(\sin ^{2} B-\frac{1}{4}\right) .
$$

同理,

$$
O_{2} V_{1} \sin \angle V_{2} V_{1} V=R_{1}\left(\sin ^{2} C-\frac{1}{4}\right)
$$

又

$$
V V_{1}=2 d(V, A H)=d(O, A H)=R_{1} \sin \angle O A H=R_{1} \sin (C-B)
$$

所以

$$
V V_{1} \sin \angle V_{3} V_{1} V_{2}=R_{1} \sin (C-B) \sin A=R_{1}\left(\sin ^{2} C-\sin ^{2} B\right)
$$

于是只需证明

这显然成立.

$$
R_{1}\left(\sin ^{2} C-\sin ^{2} B\right)+R_{1}\left(\sin ^{2} B-\frac{1}{4}\right)=R_{1}\left(\sin ^{2} C-\frac{1}{4}\right),
$$

最后, 因为 $V, V_{1}, O_{2}, O_{3}$ 所共圆的圆心在 $V V_{1}$ 的垂直平分线 $A H$ 上, 所以该圆即为 $\Gamma_{1}$, 从而 $V$ 在 $\Gamma_{1}$ 上.

同理, $V$ 也在 $\Gamma_{2}$ 和 $\Gamma_{3}$ 上.

综上, 命题得证.

评注 (1). 可以证明 $O_{1}, O_{2}, O_{3}$ 共线, $V$ 是完全四边形 $V_{1} V_{2} V_{3} O_{1} O_{2} O_{3}$ 的密克点.

(2). 东北育才学校朱家庆、湖南雅礼中学曾午午等同学也给出了本题的正确解答.
第二题 设 $A$ 是 $n$ 元正整数集合. 证明: 存在 $A$ 的子集 $B$, 使得 $|B|>\frac{n}{2022}$, 且对任意 $x_{1}, x_{2}, \cdots, x_{32} \in B$, 都有 $x_{1}^{2}+2 x_{2}^{2}+\cdots+31 x_{31}^{2} \neq x_{32}^{2}$.

(湖南师大附中学生 刘祚旭 供题)

## 证明 (根据深圳中学姜志诚同学的解答整理):

取素数 $p$, 使得 $p$ 大于 $10^{9}$ 以及 $A$ 中所有元素.

设 $A=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, 对 $1 \leq i \leq p-1$, 记 $A_{i}=\left\{i a_{1}^{2}, i a_{2}^{2}, \cdots, i a_{n}^{2}\right\}$.

称一个正整数是好的, 如果它除以 $p$ 的余数属于区间 $\left(\frac{p}{(31 \times 16)^{2}}, \frac{p}{31 \times 16}\right)$.

对固定的 $1 \leq j \leq n$, 由 $p>a_{j}$ 知 $a_{j}^{2}, 2 a_{j}^{2}, \cdots,(p-1) a_{j}^{2}$ 构成模 $p$ 的缩系, 于是其中有

$$
\left[\frac{p}{31 \times 16}\right]-\left\lceil\frac{p}{(31 \times 16)^{2}}\right\rceil+1>\frac{p}{500}
$$

个好数, 这里用到了 $p>10^{9}$.

这样 $A_{1}, A_{2}, \cdots, A_{p-1}$ 中至少有 $n \cdot \frac{p}{500}$ 个好数. 由平均值原理, 存在 $1 \leq i \leq$ $p-1$, 使得 $A_{i}$ 中至少有 $\frac{n}{500}$ 个好数, 不妨设为 $i a_{1}^{2}, i a_{2}^{2}, \cdots, i a_{s}^{2}$, 其中 $s>\frac{n}{500}$.

此时令 $B=\left\{a_{1}, a_{2}, \cdots, a_{s}\right\}$, 下面验证其满足要求.

若存在 $x_{1}, x_{2}, \cdots, x_{32} \in B$, 使得 $x_{1}^{2}+2 x_{2}^{2}+\cdots+31 x_{31}^{2}=x_{32}^{2}$, 则

$$
\left(i x_{1}^{2}\right)+2\left(i x_{2}^{2}\right)+\cdots+31\left(i x_{31}^{2}\right)=i x_{32}^{2} .
$$

模 $p$ 后, 上式左边的余数介于

$$
\frac{p}{(31 \times 16)^{2}} \times(1+2+\cdots+31)=\frac{p}{31 \times 16}
$$

与

$$
\frac{p}{31 \times 16} \times(1+2+\cdots+31)=p
$$

之间, 即属于 $\left(\frac{p}{31 \times 16}, p\right)$. 但右边的余数属于 $\left(\frac{p}{(31 \times 16)^{2}}, \frac{p}{31 \times 16}\right)$, 两者交集是空集, 矛盾!

又 $|B|>\frac{n}{500}>\frac{n}{2022}$, 所以命题得证.

评注 (1). 本题与如下经典问题的证明方法相同:

设 $A$ 是由 $n$ 个非零整数构成的集合, 则存在 $A$ 的子集 $B$, 使得 $|B| \geq \frac{n}{3}$, 且不存在 $x, y, z \in B$, 满足 $x+y=z$.

用同样的方法可以证明 2022 年保加利亚春季十一年级第四题:

设整数 $n \geq 2 . M$ 是由 $2 n^{2}-3 n+2$ 个有理数构成的集合. 则存在 $M$ 的 $n$ 元子集 $A$, 满足对任意 $2 \leq k \leq n, A$ 中任意 $k$ 个元素(允许相同)的和都不属于 $A$.

(2). 湖南雅礼中学李奕同学也给出了本题的正确解答.

第三题 设数列 $\left\{a_{n}\right\}$ 满足 $a_{1}=1, a_{k}=\max _{i+j=k}\left\{a_{i} a_{j}\right\}+1, k \geq 2$. 证明: 对任意正整数 $n, a_{2^{n}}=a_{2^{n-1}}^{2}+1$.

(北京二中学生 钱泽暄 供题)

## 证明 (根据供题者的解答整理):

我们归纳证明更强的结论: 对任意正整数 $n, k$, 若 $2^{n-1} \leq k \leq 2^{n+1}$, 则

(1) $a_{2^{n}+k}=a_{2^{n}} a_{k}+1$;

(2) $a_{2^{n}+k-1}+a_{2^{n}+k+1} \geq 2 a_{2^{n}+k}$.

按 $2^{n}+k$ 从小到大的顺序归纳, 注意到 $\left\{a_{n}\right\}$ 单调递增.

由 $a_{1}=1, a_{2}=2, a_{3}=3, a_{4}=5, a_{5}=7, a_{6}=11, a_{7}=16$, 容易验证 $n=1$ 时结论成立.

假设 $n \geq 2$, 且 $(n, k)$ 之前结论成立, 来看 $(n, k)$ 时的情形.

先证明 (1).

由定义, 只需证明对任意 $1 \leq i \leq 2^{n}+k-1$, 都有

$$
a_{2^{n}} a_{k} \geq a_{i} a_{2^{n}+k-i}
$$

(I) $2^{n-1} \leq k \leq 2^{n}$.

不妨设 $i \leq \frac{2^{n}+k}{2}$, 则 $i \leq 2^{n}$.

(i) $i \leq k$.

若 $k-i<2^{n-1}$, 则

$$
a_{2^{n}+k-i}=a_{2^{n-1}} a_{2^{n-1}+k-i}+1 .
$$

又 $a_{2^{n}}=a_{2^{n-1}}^{2}+1$, 所以只需证明

$$
\left(a_{2^{n-1}}^{2}+1\right) a_{k} \geq a_{i}\left(a_{2^{n-1}} a_{2^{n-1}+k-i}+1\right) .
$$

这由 $a_{k} \geq a_{i}$ 且

$$
a_{2^{n-1}} a_{k} \geq a_{i} a_{2^{n-1}+k-i}
$$

即证.

若 $k-i \geq 2^{n-1}$, 则

$$
a_{2^{n}+k-i}=a_{2^{n}} a_{k-i} .
$$

所以只需证明

$$
a_{2^{n}}\left(a_{k}-1+1\right) \geq a_{i}\left(a_{2^{n}} a_{k-i}+1\right) .
$$

这由 $a_{2^{n}} \geq a_{i}$ 且

$$
a_{k}-1 \geq a_{i} a_{k-i}
$$

即证.

(ii) $i>k$.

由 (2), $a_{2^{n}}+a_{k} \geq a_{i}+a_{2^{n}+k-i}$, 所以只需证明

$$
\left(a_{2^{n}}-1\right)\left(a_{k}-1\right) \geq\left(a_{i}-1\right)\left(a_{2^{n}+k-i}-1\right) .
$$

由 $i-k \leq \frac{2^{n}-k}{2} \leq 2^{n-2}$ 知

$$
a_{2^{n}+k-i}-1=a_{2^{n-1}} a_{2^{n-1}+k-i},
$$

又 $a_{2^{n}}-1=a_{2^{n-1}}^{2}$, 所以只需证明

$$
a_{2^{n-1}}\left(a_{k}-1\right) \geq\left(a_{i}-1\right) a_{2^{n-1}+k-i}
$$

若 $i \geq 2^{n-1}+2^{n-2}$, 则

$$
a_{i}-1=a_{2^{n-1}} a_{i-2^{n-1}},
$$

于是只需证明

$$
a_{k}-1 \geq a_{i-2^{n-1}} a_{2^{n-1}+k-i},
$$

这由定义即证.

若 $i<2^{n-1}+2^{n-2}$, 则

$$
\begin{aligned}
& a_{i}-1=a_{2^{n-2}} a_{i-2^{n-2}} \\
& a_{k}-1=a_{2^{n-2}} a_{k-2^{n-2}}
\end{aligned}
$$

于是只需证明

$$
a_{2^{n-1}} a_{k-2^{n-2}} \geq a_{i-2^{n-2}} a_{2^{n-1}+k-i},
$$

这由归纳假设即证.

(II) $2^{n}<k \leq 2^{n+1}$

不妨设 $i \geq \frac{2^{n}+k}{2}$, 则 $i>2^{n}$.

(i) $i>k$.

若 $i \leq 2^{n}+2^{n-1}$, 则

$$
\begin{aligned}
& a_{i}=a_{2^{n-1}} a_{i-2^{n-1}}+1 \\
& a_{k}=a_{2^{n-1}} a_{k-2^{n-1}}+1
\end{aligned}
$$

于是只需证明

$$
a_{2^{n}}\left(a_{2^{n-1}} a_{k-2^{n-1}}+1\right) \geq\left(a_{2^{n-1}} a_{i-2^{n-1}}+1\right) a_{2^{n}+k-i}
$$

这由 $a_{2^{n}} \geq a_{2^{n}+k-i}$ 且

$$
a_{2^{n}} a_{k-2^{n-1}} \geq a_{i-2^{n-1}} a_{2^{n}+k-i}
$$

即证.

若 $i>2^{n}+2^{n-1}$, 则

$$
a_{i}=a_{2^{n}} a_{i-2^{n}}+1,
$$

于是只需证明

$$
a_{2^{n}}\left(a_{k}-1+1\right) \geq\left(a_{2^{n}} a_{i-2^{n}}+1\right) a_{2^{n}+k-i} .
$$

这由 $a_{2^{n}} \geq a_{2^{n}+k-i}$ 且

$$
a_{k}-1 \geq a_{i-2^{n}} a_{2^{n}+k-i}
$$

即证.

(ii) $i \leq k$.

由 (2), $a_{2^{n}}+a_{k} \geq a_{i}+a_{2^{n}+k-i}$, 所以只需证明

$$
\left(a_{2^{n}}-1\right)\left(a_{k}-1\right) \geq\left(a_{i}-1\right)\left(a_{2^{n}+k-i}-1\right) .
$$

由 $k-i \leq \frac{k-2^{n}}{2} \leq 2^{n-1}$ 知

$$
a_{2^{n}+k-i}-1=a_{2^{n-1}} a_{2^{n-1}+k-i},
$$

又 $a_{2^{n}}-1=a_{2^{n-1}}^{2}$, 所以只需证明

$$
a_{2^{n-1}}\left(a_{k}-1\right) \geq\left(a_{i}-1\right) a_{2^{n-1}+k-i} \text {. }
$$

若 $i \geq 2^{n}+2^{n-1}$, 则

$$
\begin{gathered}
a_{i}-1=a_{2^{n}} a_{i-2^{n}} \\
a_{k}-1=a_{2^{n}} a_{k-2^{n}}
\end{gathered}
$$

于是只需证明

$$
a_{2^{n-1}} a_{k-2^{n}} \geq a_{i-2^{n}} a_{2^{n-1}+k-i},
$$

这由归纳假设即证.

若 $i<2^{n}+2^{n-1}$, 则

$$
a_{i}-1=a_{2^{n-1}} a_{i-2^{n-1}},
$$

于是只需证明

$$
a_{k}-1 \geq a_{i-2^{n-1}} a_{2^{n-1}+k-i}
$$

这由定义即证.

再证明 (2).

因为

$$
\begin{gathered}
a_{2^{n}+k-1} \geq a_{2^{n}} a_{k-1}+1, \\
a_{2^{n}+k+1} \geq a_{2^{n}} a_{k+1}+1, \\
a_{2^{n}+k}=a_{2^{n}} a_{k}+1,
\end{gathered}
$$

所以由归纳假设,

$$
\begin{aligned}
& a_{2^{n}+k-1}+a_{2^{n}+k+1}-2 a_{2^{n}+k} \\
\geq & a_{2^{n}}\left(a_{k-1}+a_{k+1}-2 a_{k}\right) \geq 0 .
\end{aligned}
$$

综上, 归纳得证.

评注 湖南雅礼中学曾午午、温州育英国际实验学校王泉皓、广西师范大学附属外国语学校铁山校区叶骐铭等同学也给出了本题的正确解答.

第四题 给定整数 $n \geq 2$. 设实数 $a_{1}, a_{2}, \cdots, a_{n} \in[0,1)$, 若对任意不超过 $k$ 的正整数 $i$, 在 $a_{1}, a_{2}, \cdots, a_{n}$ 中都存在若干项之和等于 $i$, 求正整数 $k$ 的最大可能值.

(人大附中 张端阳 供题)

## 解 1 (根据湖南雅礼中学曾午午同学的解答整理):

由 $a_{1}+a_{2}+\cdots+a_{n}<n$ 知 $k \leq n-1$.

当 $n \geq 3$ 时, 不妨设 $a_{1}+\cdots+a_{s}=1$, 其中 $2 \leq s \leq n$. 若 $s=n$, 则 $k=1$; 若 $s<n$, 则

$$
\begin{aligned}
& a_{1}+a_{2}+\cdots+a_{n} \\
= & \left(a_{1}+\cdots+a_{s}\right)+a_{s+1}+\cdots+a_{n} \\
< & 1+n-s \leq n-1,
\end{aligned}
$$

所以 $k \leq n-2$.

故当 $n=2$ 时 $k \leq 1$, 当 $n \geq 3$ 时 $k \leq n-2$.

下面给出构造.

当 $n=2$ 时, 取 $a_{1}=a_{2}=\frac{1}{2}$ 即可.
当 $n \geq 3$ 时, 记 $b_{i}=1-a_{i} \in(0,1]$, 那么若 $1 \leq i_{1}<i_{2}<\cdots<i_{t} \leq n$ 使 $b_{i_{1}}+b_{i_{2}}+\cdots+b_{i_{t}}=1$, 则 $a_{i_{1}}+a_{i_{2}}+\cdots+a_{i_{t}}=t-1$. 从而只需使得对任意 $2 \leq t \leq n-1$, 存在 $t$ 个 $b_{i}$ 的和为 1 .

记 $\alpha=\frac{\sqrt{5}-1}{2}$, 则 $\alpha^{2}+\alpha=1,0<\alpha<1$.

当 $n=2 m(m \geq 2)$ 时, 取 $b_{k}=\alpha^{k}(k=1,2, \cdots, 2 m-2), b_{2 m-1}=b_{2 m}=\frac{1}{2} \alpha^{2 m-3}$.

此时对 $1 \leq t \leq m-1$,

$$
\begin{aligned}
& b_{2 t}+b_{2 t-1}+b_{2 t-3}+b_{2 t-5}+\cdots+b_{1} \\
= & b_{2 t-2}+b_{2 t-3}+b_{2 t-5}+\cdots+b_{1} \\
= & \cdots \\
= & b_{2}+b_{1}=1,
\end{aligned}
$$

即存在 $t+1$ 个 $b_{i}$ 的和为 1 . 又由

$$
\begin{aligned}
& \alpha^{2 m-2}+\alpha^{2 m-3}+\cdots+\alpha^{2 t} \\
= & \frac{\alpha^{2 t}-\alpha^{2 m-1}}{1-\alpha}=\frac{\alpha^{2 t}-\alpha^{2 m-1}}{\alpha^{2}} \\
= & \alpha^{2 t-2}-\alpha^{2 m-3}
\end{aligned}
$$

知

$$
\begin{aligned}
& b_{2 m}+b_{2 m-1}+b_{2 m-2}+\cdots+b_{2 t}+b_{2 t-3}+b_{2 t-5}+\cdots+b_{1} \\
= & b_{2 t-2}+b_{2 t-3}+b_{2 t-5}+\cdots+b_{1}=1,
\end{aligned}
$$

即存在 $2 m-t$ 个 $b_{i}$ 的和为 1 . 于是对任意 $2 \leq t \leq 2 m-1$, 存在 $t$ 个 $b_{i}$ 的和为 1 ,满足条件.

当 $n=2 m-1(m \geq 2)$ 时, 取 $b_{k}=\alpha^{k}(k=1,2, \cdots, 2 m-2), b_{2 m-1}=\alpha^{2 m-3}$.同上一种情形知

$$
\begin{aligned}
& b_{2 t}+b_{2 t-1}+b_{2 t-3}+\cdots+b_{1} \\
= & b_{2 m-1}+b_{2 m-2}+\cdots+b_{2 t}+b_{2 t-3}+b_{2 t-5}+\cdots+b_{1}=1
\end{aligned}
$$

于是对任意 $2 \leq t \leq 2 m-2$, 存在 $t$ 个 $b_{i}$ 的和为 1 , 满足条件.

综上, 所求最大值当 $n=2$ 时为 1 , 当 $n \geq 3$ 时为 $n-2$.

## 解 2 (根据温州育英国际实验学校王胥皓同学的解答整理):

只给出当 $n \geq 3$ 时的构造.

当 $n=2 m(m \geq 2)$ 时, 取 $a_{2 i-1}=a_{2 i}=1-\frac{1}{2^{i}}(i=1,2, \cdots, m-1), a_{2 m-1}=$ $a_{2 m}=1-\frac{1}{2^{m-1}}$. 注意到总和为 $2 m-2$, 于是只需给出和为 $1,2, \cdots, m-1$ 的构造即可.(若能构造出 $t$, 则余下的数之和即为 $2 m-2-t$ )
事实上, 对 $1 \leq t \leq m-1$,

$$
a_{1}+a_{3}+a_{5}+\cdots+a_{2 t-1}+a_{2 t}=t .
$$

当 $n=2 m-1(m \geq 2)$ 时, 取 $a_{2 i-1}=a_{2 i}=1-\frac{1}{2^{i}}(i=1,2, \cdots, m-1), a_{2 m-1}=$ $1-\frac{1}{2^{m-2}}$. 验证同上一种情形.

## 解 3 (根据深圳中学姜志城同学的解答整理):

只给出当 $n \geq 3$ 时的构造.

对 $n=2 m+1$ 和 $2 m+2$, 记 $\varepsilon=\frac{1}{1+2+\cdots+m+1}$. 取前 $2 m$ 个数为

$$
m \varepsilon, \underbrace{1-\varepsilon, \cdots, 1-\varepsilon}_{m \uparrow}, 1-2 \varepsilon, 1-3 \varepsilon, \cdots, 1-m \varepsilon
$$

当 $n=2 m+1$ 时, 取最后一个数为 $(2+3+\cdots+m) \varepsilon$; 当 $n=2 m+2$ 时, 取最后两个数为 $(1+2+\cdots+m) \varepsilon$ 和 $1-\varepsilon$.

注意到总和为 $n-2$, 于是只需给出和为 $1,2, \cdots, m$ 的构造即可. (若能构造出 $t$, 则余下的数之和即为 $n-2-t)$

事实上, 对 $1 \leq t \leq m$,

$$
t=m \varepsilon+\underbrace{(1-\varepsilon)+\cdots+(1-\varepsilon)}_{t-1 \uparrow}+(1-(m-t+1) \varepsilon)
$$

满足要求.

评注 东北师大附中刘涛、人大附中孙牧聪等同学也给出了本题的正确解答.

