# 第三十七期问题征解解答与点评 

张端阳

第一题 在锐角三角形 $A B C$ 中, $B C>A B>A C$. 设 $I$ 为内心, $D, E, F$分别为内切圆在 $B C, A C, A B$ 上的切点. $G$ 为三角形的葛尔刚点, $J$ 是 $I$ 关于 $\triangle G B C$ 的等角共轭点, 直线 $I J$ 与 $A D$ 交于点 $X$. 证明: $A X=2 X D$.

(青岛二中学生 陈晓琨 供题)

解 (根据供题者的解答整理):

先证明一个引理.

引理 在非等腰锐角 $\triangle A B C$ 中, $O, H$ 分别是外心和垂心, $X$ 是 $B C$ 的中点, $E$ 是 $B$ 在 $A C$ 上的投影, $F$ 是 $C$ 在 $A B$ 上的投影. 设 $E X$ 与 $A B$ 交于点 $P, F X$与 $A C$ 交于点 $Q$. 过 $P, Q$ 分别作 $A B, A C$ 的垂线交于点 $K$, 则 $O, H, K$ 三点共线.
![](https://cdn.mathpix.com/cropped/2024_02_26_8bef08ebac85b1aafb3cg-1.jpg?height=770&width=1072&top_left_y=1620&top_left_x=500)

证明 设 $Y, Z$ 分别是 $A C, A B$ 的中点, 则只需证明 $\frac{Q E}{E Y}=\frac{P F}{F Z}$.

设 $\triangle A B C$ 的三边分别为 $a, b, c$, 不妨设 $b>c>a$.
由梅涅劳斯定理得,

$$
C Q=\frac{b\left(a^{2}-b^{2}+c^{2}\right)}{2\left(b^{2}-a^{2}\right)} .
$$

又 $C E=\frac{a^{2}+b^{2}-c^{2}}{2 b}, C Y=\frac{b}{2}$, 所以

$$
\frac{Q E}{E Y}=\frac{\frac{b\left(a^{2}-b^{2}+c^{2}\right)}{2\left(b^{2}-a^{2}\right)}+\frac{a^{2}+b^{2}-c^{2}}{2 b}}{\frac{b}{2}-\frac{a^{2}+b^{2}-c^{2}}{2 b}}=\frac{a^{2}\left(b^{2}+c^{2}-a^{2}\right)}{\left(b^{2}-a^{2}\right)\left(c^{2}-a^{2}\right)}
$$

这关于 $b, c$ 对称, 故 $\frac{Q E}{E Y}=\frac{P F}{F Z}$.

引理证毕.

![](https://cdn.mathpix.com/cropped/2024_02_26_8bef08ebac85b1aafb3cg-2.jpg?height=457&width=828&top_left_y=794&top_left_x=634)

回到原题. 设 $A I$ 的中点为 $N$, 由梅涅劳斯定理, 只需证明 $I J$ 平分线段 $N D$.

设 $P, Q$ 分别为 $I$ 在 $B G, C G$ 上的投影, 因为 $D$ 为 $I$ 在 $B C$ 上的投影, 所以由等角共轭点的性质, $\triangle D P Q$ 的外心为 $I J$ 的中点. 于是只需证明 $\triangle D P Q$ 的外心、 $I 、 N D$ 的中点三点共线.

设 $M, D$ 为 $\odot I$ 的对径点, $L$ 为 $\triangle D P Q$ 的外接圆与 $\odot I$ 的另一个交点. 因为 $M L$ 经过 $D$ 在 $\triangle D P Q$ 外接圆的对径点, 于是只需证明 $M, N, L$ 三点共线.

设 $D F$ 与 $A C$ 交于点 $U, D E$ 与 $A B$ 交于点 $V$. 因为 $D F, A C$ 分别为点 $B, E$关于 $\odot I$ 的极线, 所以 $U, P$ 关于 $\odot I$ 互为反演点. 同理, $V, Q$ 关于 $\odot I$ 互为反演点. 因为 $D, L$ 在反演下不动, 所以由 $D, L, Q, P$ 共圆知 $D, L, V, U$ 共圆.

过 $U, V$ 分别作 $U D, V D$ 的垂线交于点 $K$, 则 $D, L, V, U, K$ 都在以 $D K$ 为直径的圆上, 所以 $D L \perp L K$. 因为 $D L \perp L M$, 所以 $K, M, L$ 共线.

设 $E M$ 与 $D F$ 交于点 $S, F M$ 与 $D E$ 交于点 $T$, 则 $M$ 为 $\triangle D S T$ 的垂心, 于是 $S T / / B C$. 因为 $A$ 为 $E F$ 关于 $\odot I$ 的极点, 所以 $S, A, T$ 共线, 进而 $A$ 为 $S T$的中点. 因为 $N$ 为 $\triangle A E F$ 的外心, 所以 $N$ 为 $\triangle D S T$ 九点圆的圆心. 从而对 $\triangle D S T$ 用引理得, $K, M, N$ 共线.

故 $M, N, L$ 共线, 命题得证.

![](https://cdn.mathpix.com/cropped/2024_02_26_8bef08ebac85b1aafb3cg-3.jpg?height=922&width=811&top_left_y=207&top_left_x=614)

评注 南昌市第二中学魏业勋同学也给出了本题的正确解答, 他通过三角计算证明了 $I J$ 经过 $A$ 关于 $M$ 的对称点. 山东省实验中学孙永喆同学也给出了本题的正确解答, 他通过复数计算证明了 $I J / / M N$.

第二题 给定正整数 $n \geq 2$. 平面上有 $n$ 个圆, 圆心分别为 $O_{1}, \ldots, O_{n}$. 对平面上任意一点 $P$, 令 $\rho_{i}(P)$ 为点 $P$ 到圆 $O_{i}$ 的幂. 称一个 1 到 $n$ 的排列 $\tau_{1}, \ldots, \tau_{n}$为合法排列, 若存在点 $P$ 使得

$$
\rho_{\tau_{1}}(P)>\cdots>\rho_{\tau_{n}}(P)
$$

若 $n$ 个圆可以任意选取, 求合法排列个数的最大值.

(人大附中学生 卢远 供题)

## 解 (根据供题者的解答整理):

这 $n$ 个圆两两的根轴将平面分成了若干个区域. 对每块区域中的任意一点 $P$, 对任意 $1 \leq i<j \leq n, \rho_{i}(P)$ 和 $\rho_{j}(P)$ 有明确的大小关系. 又显然每个不在任意一条根轴上的点都对应一个合法排列, 故合法排列的个数等于根轴分平面形成的区域数.

当分成的区域数最多时, 显然这 $\mathrm{C}_{n}^{2}$ 条根轴两两不平行. 此时由蒙日定理,对每三个圆, 它们的根轴交于一点, 因此至少存在 $\mathrm{C}_{n}^{3}$ 组根轴三线共点.

当有三条直线交于一点时, 区域总数会减少 1 . 熟知 $\mathrm{C}_{n}^{2}$ 条直线至多将平面
分为 $\frac{\left(\mathrm{C}_{n}^{2}\right)^{2}+\mathrm{C}_{n}^{2}+2}{2}$ 个区域, 再减去至少存在的 $\mathrm{C}_{n}^{3}$ 组三线共点, 故这 $\mathrm{C}_{n}^{2}$ 条根轴至多将平面分为

$$
\frac{\left(\mathrm{C}_{n}^{2}\right)^{2}+\mathrm{C}_{n}^{2}+2}{2}-\mathrm{C}_{n}^{3}=\frac{3 n^{4}-10 n^{3}+21 n^{2}-14 n+24}{24}
$$

个区域。

当这 $n$ 个圆的根轴两两相交, 且无四条交于一点时可以取到最大值.

综上, 合法排列个数的最大值为 $\frac{3 n^{4}-10 n^{3}+21 n^{2}-14 n+24}{24}$.

评注 (1). 本题与 2002 年女子数学奥林匹克第八题类似:

设 $A_{1}, A_{2}, \cdots, A_{8}$ 是平面上任意取定的 8 个点, 对平面上任意取定的一条有向直线 $l$, 设 $A_{1}, A_{2}, \cdots, A_{8}$ 在该直线上的射影分别是 $P_{1}, P_{2}, \cdots, P_{8}$. 如果这 8 个射影两两不重合, 依直线 $l$ 的方向依次排列为 $P_{i_{1}}, P_{i_{2}}, \cdots, P_{i_{8}}$, 这样就得到了 $1,2, \cdots, 8$ 的一个排列 $i_{1}, i_{2}, \cdots, i_{8}$. 设这 8 个点对平面上所有有向直线作射影后, 得到的不同排列的个数为 $N_{8}=N\left(A_{1}, A_{2}, \cdots, A_{8}\right)$, 求 $N_{8}$ 的最大值.

(2). 成都七中唐旅凯, 安师大附中胡越洋, 武汉市新洲区第一中学罗云杰,武汉市武珞路实验初级中学黄俊文等同学也给出了本题的正确解答.

第三题 对正整数 $n$, 定义 $f(n)=2^{n}+1$, 而 $f^{(k)}(n)$ 为 $f(n)$ 的 $k$ 次迭代.是否存在无穷多个正整数 $n$, 使得 $n$ 整除 $f^{(2020)}(n)$, 但对任意 $1 \leq k<2020, n$不整除 $f^{(k)}(n)$ ?

(湖南师大附中学生 刘宇东 供题)

## 解 (根据成都七中唐施凯同学的解答整理):

存在.

由 Zsigmondy 定理, 对任意正整数 $t$, 存在大于 3 的素数 $p_{t}$, 使得 2 关于模 $p_{t}$ 的半阶为 $3^{t+2019}$, 即 $p_{t} \mid 2^{3^{t+2019}}+1$, 且对任意 $0<x<3^{t+2019}, p_{t} \nmid 2^{x}+1$.

下面证明, $n=3^{t} p_{t}$ 满足要求.

先证明对 $0 \leq k \leq 2020, \nu_{3}\left(f^{(k)}\left(3^{t} p_{t}\right)\right)=k+t$.

对 $k$ 归纳.

当 $k=0$ 时, $\nu_{3}\left(3^{t} p_{t}\right)=t$, 结论成立.

假设 $k-1$ 时成立, 来看 $k$ 时的情形.

因为 $f^{(k-1)}\left(3^{t} p_{t}\right)$ 是奇数, 所以由指数提升引理和归纳假设,

$$
\nu_{3}\left(f^{(k)}\left(3^{t} p_{t}\right)\right)=\nu_{3}\left(2^{f^{(k-1)}\left(3^{t} p_{t}\right)}+1\right)=\nu_{3}(2+1)+\nu_{3}\left(f^{(k-1)}\left(3^{t} p_{t}\right)\right)=k+t
$$

归纳证毕.
由 2 关于模 $p_{t}$ 的半阶为 $3^{t+2019}$, 知

$$
p_{t}\left|f^{(k)}\left(3^{t} p_{t}\right) \Longleftrightarrow 3^{t+2019}\right| f^{(k-1)}\left(3^{t} p_{t}\right) .
$$

由 $(*)$, 这对 $k=2020$ 成立, 而对 $1 \leq k<2020$ 不成立.

又由 $(*), 3^{t} \mid f^{(2020)}\left(3^{t} p_{t}\right)$, 所以 $3^{t} p_{t} \mid f^{(2020)}\left(3^{t} p_{t}\right)$. 而由上面的证明, 对 $1 \leq k<2020,3^{t} p_{t} \nmid f^{(k)}\left(3^{t} p_{t}\right)$, 故 $3^{t} p_{t}$ 满足要求.

综上, 存在无穷多个满足要求的正整数 $n$.

评注 (1). 本题是对 2012 年罗马尼亚大师杯第四题的推广:

证明: 存在无穷多个正整数 $n$, 使得 $n \mid 2^{2^{n}+1}+1$, 但 $n \nmid 2^{n}+1$.

(2). 本题也可以通过归纳构造证明: 若 $n$ 满足要求, 则 $2^{n}+1$ 也满足要求.

(3). 安师大附中胡越洋, 武汉市武珞路实验初级中学黄俊文, 重庆市巴蜀中学郭泓辰等同学也给出了本题的正确解答.

第四题 设 $a, b, c, d$ 为模长不超过 1 的复数, 且满足 $a+b+c+d=0$. 求 $\left|a^{3}+b^{3}+c^{3}+d^{3}\right|$ 的最大值.

(湖南师大附中学生 陈茁卓 供题)

## 解 1 (根据人大附中依嘉的解答整理):

当 $a=0, b=1, c=\omega, d=\omega^{2}$, 其中 $\omega=e^{\frac{2 \pi \mathrm{i}}{3}}$ 是三次单位根时, $a+b+c+d=$ 0 , 且 $\left|a^{3}+b^{3}+c^{3}+d^{3}\right|=3$.

下面证明, 总有 $\left|a^{3}+b^{3}+c^{3}+d^{3}\right| \leq 3$.

注意到

$$
\begin{aligned}
& \left|a^{3}+b^{3}+c^{3}+d^{3}\right| \\
= & \left|(a+b)\left(a^{2}-a b+b^{2}\right)+(c+d)\left(c^{2}-c d+d^{2}\right)\right| \\
= & \left|(a+b)\left(a^{2}-a b+b^{2}-c^{2}+c d-d^{2}\right)\right| \\
= & |a+b| \cdot\left|(a+b)^{2}-(c+d)^{2}-3 a b+3 c d\right| \\
= & 3|a+b| \cdot|a b-c d|,
\end{aligned}
$$

于是只需证明 $|a+b| \cdot|a b-c d| \leq 1$.

记 $a+b=r$, 通过将 $a, b, c, d$ 同时旋转可不妨设 $r \geq 0$. 当 $r=0$ 时结论显然成立, 当 $r>0$ 时, 只需证明 $|a b-c d| \leq \frac{1}{r}$.

先证明一个引理.

引理 $\left|a b-1+\frac{1}{2 r}\right| \leq \frac{1}{2 r}$.
证明 当 $0<r<\frac{1}{2}$ 时, 由三角不等式,

$$
\left|a b-1+\frac{1}{2 r}\right| \leq|a b|+\left(\frac{1}{2 r}-1\right) \leq 1+\left(\frac{1}{2 r}-1\right)=\frac{1}{2 r} .
$$

当 $r \geq \frac{1}{2}$ 时, 设 $a=x_{1}+y \mathrm{i}, b=x_{2}-y \mathrm{i}$, 其中 $x_{1}, x_{2}, y \in \mathbb{R}$. 则 $x_{1}+x_{2}=$ $r, x_{1}^{2}+y^{2} \leq 1, x_{2}^{2}+y^{2} \leq 1$. 此时

$$
a b-1+\frac{1}{2 r}=\left(x_{1} x_{2}+y^{2}-1+\frac{1}{2 r}\right)+y\left(x_{2}-x_{1}\right) \mathrm{i},
$$

所以只需证明

$$
\left(x_{1} x_{2}+y^{2}-1+\frac{1}{2 r}\right)^{2}+y^{2}\left(x_{2}-x_{1}\right)^{2} \leq \frac{1}{4 r^{2}},
$$

即

$$
y^{4}+\left(-2+\frac{1}{r}+x_{1}^{2}+x_{2}^{2}\right) y^{2}+\left(x_{1} x_{2}-1\right)\left(x_{1} x_{2}-1+\frac{1}{r}\right) \leq 0 .
$$

不妨设 $x_{1} \geq x_{2}$, 则 $y^{2} \in\left[0,1-x_{1}^{2}\right]$, 由二次函数的凸性, 只需证明当 $y^{2}=0$和 $y^{2}=1-x_{1}^{2}$ 的情形.

当 $y^{2}=0$ 时, 因为 $x_{1} \leq|a| \leq 1, x_{1}+x_{2}=r$, 所以

$$
x_{1} x_{2}-1+\frac{1}{r} \geq 1 \cdot(r-1)-1+\frac{1}{r}=r+\frac{1}{r}-2 \geq 0 \text {. }
$$

又 $x_{1} x_{2} \leq\left|x_{1} x_{2}\right| \leq|a b| \leq 1$, 所以

$$
\left(x_{1} x_{2}-1\right)\left(x_{1} x_{2}-1+\frac{1}{r}\right) \leq 0 .
$$

当 $y^{2}=1-x_{1}^{2}$ 时,

$$
\begin{aligned}
& y^{4}+\left(-2+\frac{1}{r}+x_{1}^{2}+x_{2}^{2}\right) y^{2}+\left(x_{1} x_{2}-1\right)\left(x_{1} x_{2}-1+\frac{1}{r}\right) \\
= & \left(1-x_{1}^{2}\right)\left(-1+\frac{1}{r}+x_{2}^{2}\right)+\left(x_{1} x_{2}-1\right)\left(x_{1} x_{2}-1+\frac{1}{r}\right) \\
= & -1+x_{1}^{2}+\frac{1}{r}-\frac{x_{1}^{2}}{r}+x_{2}^{2}-x_{1}^{2} x_{2}^{2}+x_{1}^{2} x_{2}^{2}-2 x_{1} x_{2}+1+\frac{1}{r} x_{1} x_{2}-\frac{1}{r} \\
= & \left(x_{1}-x_{2}\right)^{2}-\frac{1}{r} x_{1}\left(x_{1}-x_{2}\right) \\
= & \left(x_{1}-x_{2}\right)\left(\left(1-\frac{1}{r}\right) x_{1}-x_{2}\right) .
\end{aligned}
$$

因为 $r \geq \frac{1}{2}$, 所以

$$
\left(1-\frac{1}{r}\right) x_{1}-x_{2}=\left(2-\frac{1}{r}\right) x_{1}-r \leq 2-\frac{1}{r}-r \leq 0 \text {. }
$$

引理证毕.

回到原题. 因为 $(-c)+(-d)=a+b=r$, 所以由引理,

$$
\left|c d-1+\frac{1}{2 r}\right|=\left|(-c)(-d)-1+\frac{1}{2 r}\right| \leq \frac{1}{2 r} .
$$

故由三角不等式，

$$
|a b-c d| \leq\left|a b-1+\frac{1}{2 r}\right|+\left|c d-1+\frac{1}{2 r}\right| \leq \frac{1}{2 r}+\frac{1}{2 r}=\frac{1}{r} .
$$

综上, 所求最大值为 3 .

## 解 2 (根据成都七中唐施凯同学的解答整理):

只证 $\left|a^{3}+b^{3}+c^{3}+d^{3}\right| \leq 3$.

固定 $c, d$, 将 $a^{3}+b^{3}+c^{3}+d^{3}=a^{3}-(a+c+d)^{3}+c^{3}+d^{3}$ 视为关于 $a$的函数, 其中 $|a| \leq 1,|a+c+d| \leq 1$. 显然这不是常值函数, 所以由最大模原理, $\left|a^{3}+b^{3}+c^{3}+d^{3}\right|$ 的最大值必在边界处取得, 即要么 $|a|=1$, 要么 $|b|=|a+c+d|=1$.

于是当 $\left|a^{3}+b^{3}+c^{3}+d^{3}\right|$ 取得最大值时, $a, b, c, d$ 任两个中至少有一个的模为 1 , 故 $a, b, c, d$ 中至少有 3 个的模为 1 .

不妨设 $|a|=|b|=|c|=1$, 设 $a, b, c$ 在复平面内对应的点分别为 $A, B, C$, 则 $A, B, C$ 在单位圆上. 由 $|a+b+c|=|d| \leq 1$, 知 $\triangle A B C$ 的垂心在单位圆内或单位圆上, 从而 $\triangle A B C$ 是锐角或直角三角形.

设 $A B, B C, C A$ 的中点分别为 $C_{1}, A_{1}, B_{1}$, 则

$$
\begin{aligned}
& \left|\frac{a+b}{2}\right|=O C_{1}=\cos C, \\
& \left|\frac{b+c}{2}\right|=O A_{1}=\cos A, \\
& \left|\frac{c+a}{2}\right|=O B_{1}=\cos B .
\end{aligned}
$$

注意到

$$
\begin{aligned}
& \left|a^{3}+b^{3}+c^{3}+d^{3}\right| \\
= & \left|a^{3}+b^{3}+c^{3}-(a+b+c)^{3}\right|=3|(a+b)(b+c)(c+a)| \\
= & 24\left|\frac{a+b}{2}\right|\left|\frac{b+c}{2}\right|\left|\frac{c+a}{2}\right|=24 \cos A \cos B \cos C,
\end{aligned}
$$

所以只需证明 $\cos A \cos B \cos C \leq \frac{1}{8}$, 而这是熟知的.

评注 武汉市武珞路实验初级中学黄俊文, 学军中学施敖、周箴言, 人大附中罗方舟, 清华大学周海刚等同学也给出了本题的正确解答.

