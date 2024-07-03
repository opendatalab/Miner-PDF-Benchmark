# 第四届百年老校数学竞赛试题解析 

王彬

(中国科学院数学与系统科学研究院, 100190)

第四届百年老校数学竞赛于 2023 年 8 月 1 日至 5 日在江苏省苏州中学举行. 其中 8 月 2 日、 3 日的 8:00-12:30 进行了考试, 每场考试三道试题. 下面介绍本次考试的试题与解答, 不当之处敬请批评指正.

## I. 试 题

1. 已知正实数 $x, y, z$ 满足 $x y z=1$. 证明:

$$
\begin{aligned}
\frac{1}{1+x+y^{2}}+\frac{1}{1+y+z^{2}}+\frac{1}{1+z+x^{2}} & \leq 1 . \\
& (\text { 福州一中 卢伟 供题 })
\end{aligned}
$$

2. 平面上互不相同的七个点 $A, B, C, D, M, P, Q$ 满足下列条件:

(1) 四边形 $A B C D$ 是两组对边都不平行的凸四边形;

(2) $\triangle M A B \sim \triangle M D C$ 且为顺相似;

(3) $\triangle P A B \backsim \triangle P D C$ 且为逆相似, $\triangle Q A D \backsim \triangle Q B C$ 且为逆相似.

证明: 直线 $A P, B M, C Q$ 交于一点.

注：对于两个相似三角形, 如果沿周界按对应点顺序环绕的方向相同, 那么称这两个三角形互为顺相似, 否则称这两个三角形互为逆相似.

(深圳中学 金春来 供题)



修订日期: 2023-08-10.

3. 对正整数 $n$, 称两个 $n$ 元 $0-1$ 数组 $\alpha=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ 与 $\beta=$ $\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ 相邻, 如果 $\sum_{i=1}^{n}\left|x_{i}-y_{i}\right|=1$.

证明：对任意整数 $m>2^{2026}$, 均存在正整数 $k$, 以及由 $m$ 个两两不同的 $k$元 $0-1$ 数组构成的集合 $A$, 使得 $A$ 中每个数组都至少与 $A$ 中 2023 个数组相邻.

(南方科技大学 付云皓 供题)

4. 已知平面直角坐标系中的点集

$$
L=\{(x, y) \mid x, y \in\{1,2, \ldots, 100\}\} .
$$

设 $A$ 是由平面上若干个凸多边形组成的集合, 满足: $A$ 中每个凸多边形的所有顶点均属于 $L$, 并且 $L$ 中的每个点都恰好是 $A$ 中一个凸多边形的顶点.

求 $A$ 中所有凸多边形的面积之和的最小可能值.

(苏州中学 朱否克 供题)

5. 给定奇素数 $p$, 求满足下述条件的最大正整数 $k$ :

对任意非负整数 $a_{0}, a_{1}, \ldots, a_{k-1}$, 存在非负整数 $u, v$ 使得

$$
\mathrm{C}_{u}^{v+i} \equiv a_{i} \quad(\bmod p), \quad i=0,1, \ldots, k-1
$$

其中组合数 $\mathrm{C}_{n}^{m}(n, m$ 是非负整数 $)$ 定义如下:

如果 $m \leq n$, 则 $\mathrm{C}_{n}^{m}=\frac{n !}{m !(n-m) !}$, 否则 $\mathrm{C}_{n}^{m}=0$. 这里 $0 !=1$.

(南方科技大学 付云皓 供题)

6. 设 $n$ 是正整数, 记 $\lambda_{n}$ 是满足下述条件的最小实数 $\lambda$ :

对任意 $n$ 个复数 $z_{1}, z_{2}, \ldots, z_{n}$, 均存在 $\{1,2, \ldots, n\}$ 的非空子集 $B$ 使得

$$
\lambda \cdot\left|\sum_{k \in B} z_{k}\right| \geq \sum_{k=1}^{n}\left|z_{k}\right|
$$

(1) 求 $\lambda_{4}$;

(2) 求 $\lambda_{100}$.

(中国科学院数学与系统科学研究院 王彬供题)

## II . 解答与评注

题 1 已知正实数 $x, y, z$ 满足 $x y z=1$. 证明:

$$
\frac{1}{1+x+y^{2}}+\frac{1}{1+y+z^{2}}+\frac{1}{1+z+x^{2}} \leq 1 .
$$

证明 1 由柯西不等式, 我们做放缩

$$
\frac{1}{1+x+y^{2}} \leq \frac{z^{\frac{4}{3}}+x^{\frac{1}{3}}+y^{-\frac{2}{3}}}{\left(x^{\frac{2}{3}}+y^{\frac{2}{3}}+z^{\frac{2}{3}}\right)^{2}} .
$$

对上式轮换求和, 可知我们只需证

$$
\left(x^{\frac{4}{3}}+y^{\frac{4}{3}}+z^{\frac{4}{3}}\right)+\left(x^{\frac{1}{3}}+y^{\frac{1}{3}}+z^{\frac{1}{3}}\right)+\left(x^{-\frac{2}{3}}+y^{-\frac{2}{3}}+z^{-\frac{2}{3}}\right) \leq\left(x^{\frac{2}{3}}+y^{\frac{2}{3}}+z^{\frac{2}{3}}\right)^{2} .
$$

即只需证

$$
x^{\frac{1}{3}}+y^{\frac{1}{3}}+z^{\frac{1}{3}} \leq x^{-\frac{2}{3}}+y^{-\frac{2}{3}}+z^{-\frac{2}{3}} .
$$

由均值不等式

$$
\frac{x^{-\frac{2}{3}}+y^{-\frac{2}{3}}}{2} \geq x^{-\frac{1}{3}} y^{-\frac{1}{3}}=z^{\frac{1}{3}},
$$

轮换求和可得上式.

因此原式得证.

评注 1 一般的, 对 $0 \leq \alpha \leq \beta \leq \gamma \leq 2 \beta$, (本题是 $\alpha=0, \beta=1, \gamma=2$ 的特例), 我们可以证明:

$$
\frac{1}{x^{\alpha}+y^{\beta}+z^{\gamma}}+\frac{1}{y^{\alpha}+z^{\beta}+x^{\gamma}}+\frac{1}{z^{\alpha}+x^{\beta}+y^{\gamma}} \leq 1
$$

取参数 $k=\frac{1}{3} \gamma$, 考虑柯西放缩

$$
\frac{1}{x^{\alpha}+y^{\beta}+z^{\gamma}} \leq \frac{x^{2 k-\alpha}+y^{2 k-\beta}+z^{2 k-\gamma}}{\left(x^{k}+y^{k}+z^{k}\right)^{2}}
$$

轮换求和后只需证

$$
\sum_{c y c} x^{2 k-\alpha} \leq \sum_{c y c} x^{2 k} \text { 以及 } \sum_{c y c} x^{2 k-\beta} \leq \sum_{c y c} x^{-k} \text {. }
$$

考虑函数 $g(t)=x^{t}+y^{t}+z^{t}$ 在 $t \in[0,+\infty)$ 单调增, 在 $t \in(-\infty, 0]$ 单调减,并且 $g(-t) \leq g(2 t)$. 由于 $2 k-\beta \in\left[-k, \frac{k}{2}\right], 2 k-\alpha \in[-k, 2 k]$, 因此命题得证.

$g(t)$ 的单调性可以理解为: 对 $t_{1} \geq t_{2} \geq 0$ 有均值不等式 $\frac{t_{2}}{t_{1}} x^{t_{1}}+\frac{t_{1}-t_{2}}{t_{1}} \geq x^{t_{2}}$,轮换求和后可得 $g\left(t_{1}\right)-g\left(t_{2}\right) \geq \frac{t_{1}-t_{2}}{t_{1}}\left(g\left(t_{1}\right)-3\right) \geq 0$.

证明 2 用 $\sum_{c y c}$ 表示轮换求和, 我们考虑对左边式子通分:

$$
\begin{aligned}
\text { 分子 } & =\sum_{c y c}\left(1+x+y^{2}\right)\left(1+y+z^{2}\right) \\
& =\sum_{c y c}\left(1+x+y+y^{2}+z^{2}+x y+y^{2} z^{2}+x z^{2}+y^{3}\right) \\
& =3+2 \sum_{c y c} x+2 \sum_{c y c} x^{2}+\sum_{c y c} \frac{1}{x}+\sum_{c y c} \frac{1}{x^{2}}+\sum_{c y c} x^{3}+\sum_{c y c} x z^{2} .
\end{aligned}
$$

分母 $=\left(1+x+y^{2}\right)\left(1+y+z^{2}\right)\left(1+z+x^{2}\right)$

$$
\begin{aligned}
&=1+\sum_{c y c}\left(x+y^{2}\right)+\sum_{c y c}\left(x y+y^{3}+x z^{2}+y^{2} z^{2}\right) \\
&+\left(x y z+x^{2} y^{2} z^{2}\right)+\sum_{c y c}\left(x^{3} y+x^{3} z^{2}\right) \\
&=3+\sum_{c y c} x+\sum_{c y c} x^{2}+\sum_{c y c} \frac{1}{x}+\sum_{c y c} x^{3}+\sum_{c y c} \frac{1}{x^{2}}+\sum_{c y c} x z^{2}+\sum_{c y c}\left(x^{3} y+x^{3} z^{2}\right) .
\end{aligned}
$$

原问题等价于证明

$$
x^{3} y+y^{3} z+z^{3} x+x^{3} z^{2}+y^{3} x^{2}+z^{3} y^{2} \geq(x+y+z)+\left(x^{2}+y^{2}+z^{2}\right) \text {. }
$$

由均值不等式

$$
0.5 x^{3} y+0.4 x^{3} z^{2}+0.1 y^{3} x^{2} \geq x^{2.9} y^{0.8} z^{0.8}=x^{2.1} \text {. }
$$

上式轮换求和可得:

$$
\frac{1}{2} \sum_{c y c}\left(x^{3} y+x^{3} z^{2}\right) \geq \sum_{c y c} x^{2.1} \geq \sum_{c y c} x^{2} \geq \sum_{c y c} x .
$$

因此原式得证.

评注 2 我们考虑用待定参数法做均值不等式的放缩, 由于 $\sum_{c y c}\left(x^{3} y+x^{3} z^{2}\right)$中含有 $x$ 的项有 $x^{3} y, z^{3} x, x^{3} z^{2}, y^{3} x^{2}$. 待定参数 $u, v \in\left[0, \frac{1}{2}\right]$,

$$
\begin{aligned}
& u x^{3} y+\left(\frac{1}{2}-u\right) z^{3} x+v x^{3} z^{2}+\left(\frac{1}{2}-v\right) y^{3} x^{2} \\
\geq & \left(x^{3} y\right)^{u} \times\left(z^{3} x\right)^{\frac{1}{2}-u} \times\left(x^{3} z^{2}\right)^{v} \times\left(y^{3} x^{2}\right)^{\frac{1}{2}-v} \\
= & x^{3 u+\frac{1}{2}-u+3 v+1-2 v} y^{u+\frac{3}{2}-3 v} z^{\frac{3}{2}-3 u+2 v} .
\end{aligned}
$$

要求 $y, z$ 的指数相等 $u+\frac{3}{2}-3 v=\frac{3}{2}-3 u+2 v$ 即 $4 u=5 v$. 记 $u=5 t, v=4 t$, $0 \leq t \leq 0.1$. 上式右边变成

$$
x^{3 u+\frac{1}{2}-u+3 v+1-2 v} y^{u+\frac{3}{2}-3 v} z^{\frac{3}{2}-3 u+2 v}=x^{\frac{3}{2}+14 t} y^{\frac{3}{2}-7 t} z^{\frac{3}{2}-7 t}=x^{21 t} .
$$

我们也可以取 $t=\frac{2}{21}$, 即 $u=\frac{10}{21}, v=\frac{8}{21}$ 得:

$$
\frac{20}{42} x^{3} y+\frac{1}{42} z^{3} x+\frac{16}{42} x^{3} z^{2}+\frac{5}{42} y^{3} x^{2} \geq x^{2} .
$$

轮换求和后可得

$$
\frac{1}{2} \sum_{c y c}\left(x^{3} y+x^{3} z^{2}\right) \geq \sum_{c y c} x^{2} \geq \sum_{c y c} x .
$$

题 2 平面上互不相同的七个点 $A, B, C, D, M, P, Q$ 满足下列条件:

(1) 四边形 $A B C D$ 是两组对边都不平行的凸四边形;

(2) $\triangle M A B \backsim \triangle M D C$ 且为顺相似;

(3) $\triangle P A B \backsim \triangle P D C$ 且为逆相似, $\triangle Q A D \backsim \triangle Q B C$ 且为逆相似.

证明: 直线 $A P, B M, C Q$ 交于一点.

证明 1 在平面上定义两个几何变换 $f$ 和 $g$, 其中变换 $f$ 是以点 $M$ 为反演中心, $\sqrt{M A \cdot M C}$ 为反演半径的反演变换, 变换 $g$ 是以 $\angle A M C$ 的平分线所在的直线为对称轴的轴对称变换. 设 $f$ 和 $g$ 的复合变换 $\varphi=g \circ f$. 根据变换 $\varphi$的定义, 易知 $\varphi \circ \varphi$ 是平面上的恒等变换, 即对于平面上任意两点 $X$ 和 $Y$, 若 $\varphi(X)=Y$, 则 $\varphi(Y)=X$. 由 $\varphi$ 的定义, 显然有 $\varphi(A)=C$.



因为 $\triangle M A B \sim \triangle M D C$, 所以 $\frac{M A}{M D}=\frac{M B}{M C}$ 且 $\angle A M B=\angle D M C$, 即 $M A$. $M C=M B \cdot M D$ 且 $\angle A M C$ 的平分线与 $\angle B M D$ 的平分线重合, 所以由变换 $\varphi$的定义有 $\varphi(B)=D$.

设 $\varphi(P)=P^{\prime}, \varphi(Q)=Q^{\prime}$, 设过 $M, C, P^{\prime}$ 三点的圆 $\omega_{1}$ 与直线 $C D$ 异于点 $C$ 的交点是 $S$, 过 $M, A, Q^{\prime}$ 三点的圆 $\omega_{2}$ 与直线 $A D$ 异于点 $A$ 的交点是 $T$. 连结 $A S, C T$.

根据变换 $\varphi$ 的定义, 由 $\varphi(A)=C$ 及 $\varphi(P)=P^{\prime}$ 得 $\triangle M A P^{\prime} \sim \triangle M P C$ 顺相似, 故 $\frac{P^{\prime} A}{C P}=\frac{M A}{M P}$. 同理, $\frac{P^{\prime} D}{B P}=\frac{M D}{M P}$. 由 $\triangle M A B \backsim \triangle M D C$ 得 $\frac{M A}{M D}=\frac{A B}{D C}$. 由
$\triangle P A B \backsim \triangle P D C$ 得 $\frac{B P}{C P}=\frac{A B}{D C}$. 故 $\frac{P^{\prime} A}{P^{\prime} D}=\frac{M A}{M D} \cdot \frac{C P}{B P}=1$, 即 $P^{\prime} A=P^{\prime} D$. 同理, $P^{\prime} B=P^{\prime} C$.

设直线 $A B$ 与直线 $C D$ 相交于点 $E$, 直线 $A D$ 与直线 $B C$ 相交于点 $F$. 由于 $\triangle M A B$ 与 $\triangle M D C$ 顺相似, 可知点 $M$ 是完全四边形 $A B C D E F$ 的密克点,即点 $M$ 在 $\triangle E A D, \triangle E B C, \triangle F A B, \triangle F C D$ 的外接圆上. 分别作 $\triangle E A D$ 和 $\triangle E B C$ 的外接圆 $\odot O_{1}$ 和 $\odot O_{2}$, 则 $\odot O_{1}$ 和 $\odot O_{2}$ 均经过点 $M$.

连结 $A O_{1}, D O_{1}, P^{\prime} M, P^{\prime} O_{1}, P^{\prime} O_{2}, M O_{1}, M O_{2}, E O_{2}$. 由 $O_{1} A=O_{1} D, P^{\prime} A=$ $P^{\prime} D$, 故 $O_{1} P^{\prime}$ 垂直平分线段 $A D, O_{1} P^{\prime} \perp A F$. 同理, $O_{2} P^{\prime} \perp B F$, 所以 $\angle O_{1} P^{\prime} O_{2}=\angle A F B$. 点 $M$ 同在 $\odot O_{1}$ 和 $\odot O_{2}$ 上, 故 $\angle O_{1} M E+\angle E A M=90^{\circ}$且 $\angle O_{2} M E+\angle E B M=90^{\circ}$. 所以,

$$
\angle O_{1} M O_{2}=\angle O_{2} M E-\angle O_{1} M E=\angle E A M-\angle E B M=\angle A M B .
$$

又由于点 $M$ 在 $\triangle A B F$ 的外接圆上, 故 $\angle A F B=\angle A M B$. 因此 $\angle O_{1} P^{\prime} O_{2}=$ $\angle O_{1} M O_{2}$, 故 $M, O_{1}, O_{2}, P^{\prime}$ 四点共圆, 因此 $\angle M P^{\prime} O_{1}=\angle M O_{2} O_{1}$. 由 $S, M, C, P^{\prime}$四点均在圆 $\omega_{1}$ 上, 且点 $S$ 在直线 $C E$ 上, 得 $\angle M P^{\prime} S=\angle M C S=\angle M C E$.注意线段 $E M$ 是 $\odot O_{1}$ 和 $\odot O_{2}$ 的公共弦, 故直线 $O_{1} O_{2}$ 垂直平分 $E M$, 故 $\angle M O_{2} O_{1}=\frac{1}{2} \angle M O_{2} E=\angle M C E$. 从而, $\angle M P^{\prime} O_{1}=\angle M P^{\prime} S$, 故 $P^{\prime}, S, O_{1}$ 三点共线. 又由于直线 $O_{1} P^{\prime}$ 垂直平分线段 $A D$, 故点 $S$ 在线段 $A D$ 的中垂线上, 因此 $\angle D A S=\angle A D S$.

注意 $\triangle M A B$ 与 $\triangle M D C$ 顺相似蕴含着 $\triangle M A D$ 与 $\triangle M B C$ 顺相似, 故同理可得 $\angle D C T=\angle C D T$. 因为 $\angle A D S=\angle C D T$, 所以 $\angle D A S=\angle D C T$, 故 $A, C, T, S$ 四点共圆, 记该圆为 $\omega$. 设圆 $\omega_{1}$ 与 $\omega_{2}$ 异于点 $M$ 的交点为 $X$. 对圆 $\omega, \omega_{1}, \omega_{2}$ 用根心定理得 $C S, A T, M X$ 三线共点, 即 $M, D, X$ 三点共线, 即圆 $\omega_{1}$,圆 $\omega_{2}$ 和直线 $M D$ 均经过点 $X$. 再由变换 $\varphi$ 的保圆性可知, $\varphi\left(\omega_{1}\right)=$ 直线 $A P$, $\varphi\left(\omega_{2}\right)=$ 直线 $C Q, \varphi($ 直线 $M D)=$ 直线 $M B$, 从而直线 $A P, B M, C Q$ 均经过点 $\varphi(X)$.

证明 2 设直线 $A B$ 与 $C D$ 交于点 $E$, 直线 $A D$ 与 $B C$ 交于点 $F$. 由 Apollonius 定理可知, 平面上到 $A, B$ 两点的距离之比为 $\frac{A D}{B C}$ 的点的轨迹为一圆周, 记该圆周为 $\odot O_{1}$. 类似地, 设平面上到 $B, C$ 两点的距离之比为 $\frac{A B}{C D}$ 的点的轨迹为 $\odot O_{2}$, 平面上到 $C, D$ 两点的距离之比为 $\frac{A D}{B C}$ 的点的轨迹为 $\odot O_{3}$, 平面上到 $A, D$ 两点的距离之比为 $\frac{A B}{C D}$ 的点的轨迹为 $\odot O_{4}$. (图中仅画出这些圆的圆心).



由 $\triangle M A D \backsim \triangle M B C$ 以及 $\triangle Q A D \backsim \triangle Q B C$ 得 $\frac{M A}{M B}=\frac{A D}{B C}=\frac{Q A}{Q B}$, 所以点 $M$ 和 $Q$ 均在 $\odot O_{1}$ 上, 同理点 $M$ 和 $Q$ 均在 $\odot O_{3}$ 上, 故点 $M$ 与 $Q$ 关于直线 $O_{1} O_{3}$轴对称. 同理点 $M$ 与点 $P$ 关于直线 $O_{2} O_{4}$ 轴对称.

由点 $M$ 在 $\odot O_{1}$ 上并根据 Apollonius 圆的性质, 有 $\triangle O_{1} M A \sim \triangle O_{1} B M$,从而 $\angle O_{1} M A=\angle A B M$. 同理 $\angle O_{3} M D=\angle D C M$. 再由 $\triangle M A B \backsim \triangle M D C$得 $\angle A B M=\angle D C M$ 且 $\angle E A M=\angle E D M$, 所以

$$
\angle E O_{1} M=\angle E A M+\angle O_{1} M A=\angle E D M+\angle O_{3} M D=\angle E O_{3} M
$$

所以 $E, M, O_{1}, O_{3}$ 四点共圆. 同理 $F, M, O_{2}, O_{4}$ 四点共圆.

过点 $M$ 分别作直线 $A B, B C, C D, D A, O_{1} O_{3}, O_{2} O_{4}$ 的垂线, 设垂足分别为 $H_{1}, H_{2}, H_{3}, H_{4}, U, V$, 注意到点 $M$ 在 $\triangle E A D, \triangle E O_{1} O_{3}, \triangle F C D, \triangle F O_{2} O_{4}$ 的外接圆上, 由 Simson 定理可知这 6 个垂足共线, 记该直线为 $l$. 且由点 $M$ 与点 $Q$关于直线 $O_{1} O_{3}$ 轴对称可知 $U$ 是线段 $M Q$ 的中点, 同理 $V$ 是线段 $M P$ 的中点.

设直线 $A B$ 与直线 $M P$ 相交于 $X$, 直线 $B C$ 与直线 $M Q$ 相交于 $Y$, 直线 $A C$ 与直线 $P Q$ 相交于 $Z$.

由 $E, M, O_{1}, O_{3}$ 四点共圆, 以及 $E, M, D, A$ 四点共圆得 $\angle O_{3} O_{1} M=\angle O_{3} E M$ $=\angle D A M$, 再由 $O_{1} O_{3} \perp M Q$ 以及 $\triangle O_{1} M A \backsim \triangle O_{1} B M$, 得

$$
\begin{aligned}
\angle Y M B & =\angle O_{1} M B-\angle O_{1} M Q=\angle M A O_{1}-90^{\circ}+\angle O_{3} O_{1} M \\
& =\angle M A O_{1}-90^{\circ}+\angle D A M=\angle D A E-90^{\circ} .
\end{aligned}
$$

同理 $\angle Y M C=\angle A D C-90^{\circ}$. 所以

$$
\frac{Y B}{Y C}=\frac{M B}{M C} \cdot \frac{\sin \angle Y M B}{\sin \angle Y M C}=\frac{M B}{M C} \cdot \frac{|\cos \angle B A D|}{|\cos \angle A D C|}
$$

同理

$$
\frac{X A}{X B}=\frac{M A}{M B} \cdot \frac{|\cos \angle A D C|}{|\cos \angle B C D|}
$$

注意 $C, M, H_{2}, H_{3}$ 四点共圆, $A, M, H_{1}, H_{4}$ 四点共圆, 所以

$$
\begin{aligned}
& \frac{d(C, l)}{d(M, l)}=\frac{C H_{2} \cdot C H_{3}}{M H_{2} \cdot M H_{3}}=\cot \angle M C F \cdot \cot \angle M C E . \\
& \frac{d(A, l)}{d(M, l)}=\frac{A H_{1} \cdot A H_{4}}{M H_{1} \cdot M H_{4}}=\cot \angle M A E \cdot \cot \angle M A F .
\end{aligned}
$$

其中 $d(C, l)$ 表示点 $C$ 到直线 $l$ 的距离, 依此类推. 所以

$$
\begin{aligned}
\frac{Z C}{Z A} & =\frac{d(C, P Q)}{d(A, P Q)}=\frac{d(M, l)-d(C, l)}{d(M, l)-d(A, l)}=\frac{1-\cot \angle M C F \cdot \cot \angle M C E}{1-\cot \angle M A E \cdot \cot \angle M A F} \\
& =\frac{\sin \angle M A E \cdot \sin \angle M A F}{\sin \angle M C E \cdot \sin \angle M C F} \cdot\left|\frac{\cos (\angle M C E+\angle M C F)}{\cos (\angle M A E+\angle M A F)}\right| \\
& =\frac{\sin \angle M F C}{\sin \angle M C F} \cdot \frac{\sin \angle M A F}{\sin \angle M F A} \cdot\left|\frac{\cos \angle B C D}{\cos \angle B A D}\right| \\
& =\frac{M C}{M F} \cdot \frac{M F}{M A} \cdot\left|\frac{\cos \angle B C D}{\cos \angle B A D}\right|=\frac{M C}{M A} \cdot\left|\frac{\cos \angle B C D}{\cos \angle B A D}\right| .
\end{aligned}
$$

所以 $\frac{X A}{X B} \cdot \frac{Y B}{Y C} \cdot \frac{Z C}{Z A}=1$, 所以 $X, Y, Z$ 三点共线, 即 $\triangle A B C$ 与 $\triangle P M Q$ 的三组对应边的交点三点共线, 故由 Desargues 定理可知 $A P, B M, C Q$ 三线共点.

评注 从证明 2 中可以看出直线 $P Q$ 是完全四边形 $A B C D E F$ 的垂心线.

题 3 对正整数 $n$, 称两个 $n$ 元 $0-1$ 数组 $\alpha=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ 与 $\beta=$ $\left(y_{1}, y_{2}, \ldots, y_{n}\right)$ 相邻, 如果 $\sum_{i=1}^{n}\left|x_{i}-y_{i}\right|=1$.

证明: 对任意整数 $m>2^{2026}$, 均存在正整数 $k$, 以及由 $m$ 个两两不同的 $k$元 $0-1$ 数组构成的集合 $A$, 使得 $A$ 中每个数组都至少与 $A$ 中 2023 个数组相邻.

证明 1 若正整数 $m$ 满足, 存在正整数 $n$ 及 $m$ 个两两不同的 $n$ 元 $0-1$数组 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{m}$, 使得任何一个数组都至少与 2023 个数组相邻, 则称 $m$为“好的”. 我们依次证明如下结论.

结论 1 若 $m_{1}, m_{2}$ 都是好的, 则 $m_{1}+m_{2}$ 也是 “好的”.

设 $m_{1}$ 个 $n_{1}$ 元 $0-1$ 数组 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{m_{1}}$, 使得任何一个数组都至少与 2023 个数组相邻, $m_{2}$ 个 $n_{2}$ 元 $0-1$ 数组 $\beta_{1}, \beta_{2}, \cdots, \beta_{m_{2}}$ 使得任何一个数组都至少与 2023 个数组相邻, 且不妨设 $n_{1} \leq n_{2}$. 现在, 在 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{m_{1}}$ 后面都添上
$n_{2}-n_{1}+1$ 个 0 , 在 $\beta_{1}, \beta_{2}, \cdots, \beta_{m_{2}}$ 后面都添上一个 1 , 就形成了 $m_{1}+m_{2}$ 个两两不同的 $n_{2}+1$ 元 $0-1$ 数组, 且任何一个数组都至少与 2023 个数组相邻, 即 $m_{1}+m_{2}$ 也是“好的”.

## 结论 $22^{2023}$ 是 “好的”.

选取所有 2023 元 $0-1$ 数组, 这样每个数组均与 2023 个数组相邻.

结论 $32^{2024}-2^{2022}$ 是“好的”.

选取所有 2024 元 $0-1$ 数组, 这样每个数组均与 2024 个数组相邻. 然后去掉其中前两位均为 0 的所有数组, 这样剩下的数组若要与被去掉的数组相邻,必须是前两位不同, 故易知剩下的每个数组最多与 1 个被去掉的数组相邻, 故在剩下的数组中, 每个数组均至少与 2023 个数组相邻.

结论 4 若整数 $d_{1}, d_{2}, \cdots, d_{l}$ 满足 $0 \leq d_{1}<d_{2}<\cdots<d_{l} \leq 2021$, 且对 $i=1,2, \ldots, k-1$ 均有 $d_{i+1}-d_{i} \geq 3$, 则 $2^{2024}-\left(2^{d_{1}}+2^{d_{2}}+\cdots+2^{d_{l}}\right)$ 是 “好的”.

选取所有 2024 元 $0-1$ 数组, 再去掉下面的数组:

前 $2024-d_{l}$ 位均为 0 的所有数组, 共 $2^{d_{l}}$ 个, 记这些数组的集合为 $T_{l}$;

前 $2024-d_{l}$ 位均为 1 , 接下来 $d_{l}-d_{l-1}$ 位均为 0 的所有数组, 共 $2^{d_{l-1}}$ 个,记这些数组的集合为 $T_{l-1}$;

前 $2024-d_{2}$ 位均为 1 , 接下来 $d_{2}-d_{1}$ 位均为 0 的所有数组, 共 $2^{d_{1}}$ 个, 记这些数组的集合为 $T_{1}$.

与结论 3 的证明类似, 在所有 2024 元 $0-1$ 数组中, 每个数组均与 2024 个数组相邻. 注意对于 $1 \leq i<j \leq l, T_{i}$ 中的数组的第 $2024-d_{j+1}+1,2024-$ $d_{j+1}+2, \cdots, 2024-d_{j}$ 位均为 1 (这里定义 $d_{l+1}=2024$ ), 而 $T_{j}$ 中的数组的第 $2024-d_{j+1}+1,2024-d_{j+1}+2, \cdots, 2024-d_{j}$ 位均为 0 , 故对于剩下的每个数组, 它不可能同时与 $T_{i}$ 中的数组和 $T_{j}$ 中的数组相邻. 使用结论 3 中的推理可知,剩下的每个数组最多与某个 $T_{i}$ 中的一个数组相邻, 因此在剩下的数组中, 每个数组均至少与 2023 个数组相邻. 剩下的数组恰为 $2^{2024}-\left(2^{d_{1}}+2^{d_{2}}+\cdots+2^{d_{l}}\right)$个, 故 $2^{2024}-\left(2^{d_{1}}+2^{d_{2}}+\cdots+2^{d_{l}}\right)$ 是“好的”.

现在, 对于 $m>2^{2026}$, 设 $m=2^{2026}-K+c \times 2^{2023}$, 其中 $0 \leq K<2^{2023}$.易知 $K$ 可以写成最多一个 $2^{2022}$ 和最多 3 个 $2^{d_{1}}+2^{d_{2}}+\cdots+2^{d_{l}}$ 之和, 其中 $d_{1}, d_{2}, \cdots, d_{l}$ 满足结论 4 的条件. 由结论 $1,2,3,4$ 可知 $2^{2026}-K$ 是 “好的”, 再结合结论 1,2 可知 $m$ 是“好的”, 证毕.

证明 2 对任意整数 $k \geq 2$, 我们选取所有 $k$ 元 $0-1$ 数组, 这样选取了 $2^{k}$
个数组, 且每个数组均与 $k$ 个数组相邻. 下面我们证明引理:

引理 对 $2^{k-1}<m \leq 2^{k}$, 可以将这些数组分为 $A, B$ 两个集合, 其中 $|A|=m$, 且 $A$ 中每个数组最多与 $B$ 中 4 个数组相邻.

如果 $m=2^{k}$, 那么取 $A$ 为所有 $k$ 元 $0-1$ 数组, 取 $B=\emptyset$ 即可. 下面假设 $m<2^{k}$, 设 $m=2^{k}-\left(2^{d_{1}}+2^{d_{2}}+\cdots+2^{d_{t}}\right)$, 这里整数 $d_{1}<d_{2}<\cdots<d_{t} \leq k-2$.

对 $i=1,2, \ldots, t$, 我们记前 $k-d_{i}-2$ 位均为 0 , 接下来两位即第 $k-d_{i}-1$位与第 $k-d_{i}$ 位均为 1 的所有 $k$ 元数组(共 $2^{d_{i}}$ 个)构成的集合为 $B_{i}$. 显然 $B_{1}, B_{2}, \ldots, B_{t}$ 两两不交. 我们取 $B=B_{1} \cup B_{2} \cup \cdots \cup B_{t}$, 取 $A$ 为 $B$ 的补集, 则有 $|A|=m$. 由证明 1 的结论 3 的证明类似可知：对 $A$ 中任意一个数组 $\alpha$ 与 $1 \leq i \leq t, \alpha$ 至多与 $B_{i}$ 中一个数组相邻. 因此, 为了证明 $(\star)$, 我们只需证明对 $A$ 中任意一个数组 $\alpha$, 最多存在四个不同的 $i$, 使得 $\alpha$ 与 $B_{i}$ 中某一个数组相邻.

假设不然, 设有五个这样的 $i$, 记为 $i_{1}<i_{2}<i_{3}<i_{4}<i_{5}$, 我们只考虑 $B_{i_{1}}, B_{i_{3}}, B_{i_{5}}$. 由于 $d_{i_{3}}-d_{i_{1}} \geq i_{3}-i_{1} \geq 2$, 故 $k-d_{i_{1}}-2 \geq k-d_{i_{3}}$, 因此 $B_{i_{1}}$ 中所有数组的第 $k-d_{i_{3}}-1, k-d_{i_{3}}$ 位都是 0 , 而 $B_{i_{3}}$ 中所有数组的第 $k-d_{i_{3}}-1, k-d_{i_{3}}$位都是 1 , 因此 $\alpha$ 的第 $k-d_{i_{3}}-1, k-d_{i_{3}}$ 位必须是一个 0 与一个 1 . 同理, $\alpha$ 的第 $k-d_{i_{5}}-1, k-d_{i_{5}}$ 位也必须是一个 0 与一个 1 , 但此时 $\alpha$ 与 $B_{i_{3}}$ 中的任何一个数组至少有两位不同, 不可能相邻, 矛盾!

因此 $(\star)$ 成立. 对题述的 $m$, 选取 $k$ 使得 $2^{k-1}<m \leq 2^{k}$, 则 $k \geq 2027$,由 $(\star)$ 知可以选出由 $m$ 个两两不同的 $k$ 元 $0-1$ 数组构成的集合 $A$, 使得 $A$ 中每个数组都至少与 $A$ 中 $k-4 \geq 2023$ 个数组相邻, 证毕.

评注 事实上, $(\star)$ 可以加强到: $A$ 中每个数组最多与 $B$ 中 3 个数组相邻.为此我们在证明中假设 $A$ 中某一个数组 $\alpha$ 与 $B_{i_{1}}, B_{i_{2}}, B_{i_{3}}, B_{i_{4}}$ 中各一个数组相邻, 这里 $i_{1}<i_{2}<i_{3}<i_{4}$. 事实上, 上面证明类似可得 $\alpha$ 的第 $k-d_{i_{4}}-1, k-d_{i_{4}}$位也必须是一个 0 与一个 1 . 注意到 $B_{i_{2}}$ 中任意一个数组的第 $k-d_{i_{2}}-1$ 位为 1 , $B_{i_{1}}$ 中任意一个数组的第 $k-d_{i_{2}}-1$ 位为 0 , (因为 $k-d_{i_{2}}-1 \leq k-d_{i_{1}}-2$ ). 因此:

如果 $\alpha$ 的第 $k-d_{i_{2}}-1$ 位为 0 , 那么 $\alpha$ 与 $B_{i_{2}}$ 中的任何一个数组至少有两位不同, 不可能相邻, 矛盾;

如果 $\alpha$ 的第 $k-d_{i_{2}}-1$ 位为 1 , 那么 $\alpha$ 与 $B_{i_{1}}$ 中的任何一个数组至少有两位不同, 不可能相邻, 亦矛盾.

由此可知, 证明中的 $k$ 只需不小于 2026 即可, 因此题目中的 $m>2^{2026}$ 可以放宽为 $m>2^{2025}$.
题 4 已知平面直角坐标系中的点集

$$
L=\{(x, y) \mid x, y \in\{1,2, \ldots, 100\}\}
$$

设 $A$ 是由平面上若干个凸多边形组成的集合, 满足: $A$ 中每个凸多边形的所有顶点均属于 $L$, 并且 $L$ 中的每个点都恰好是 $A$ 中一个凸多边形的顶点.

求 $A$ 中所有凸多边形的面积之和的最小可能值.

解 假设 $A$ 中一共有 $m$ 个凸多边形, 分别有 $a_{1}, a_{2}, \ldots, a_{m}$ 个顶点. 由题意知

$$
a_{1}+a_{2}+\cdots+a_{m}=|L|=100 \times 100=10000 \text {. }
$$

根据皮克(Pick)定理知: 有 $a_{k}$ 个顶点的凸多边形的面积 $\geq \frac{a_{k}-2}{2} \geq \frac{1}{2} \times\left\lceil\frac{a_{k}}{3}\right\rceil$,因此总面积

$$
S \geq \sum_{k=1}^{m} \frac{a_{k}-2}{2} \geq \frac{1}{2} \times \sum_{k=1}^{m}\left\lceil\frac{a_{k}}{3}\right\rceil \geq \frac{1}{2} \times\left\lceil\frac{10000}{3}\right\rceil=\frac{1}{2} \times 3334=1667 .
$$

关于构造, 我们首先有一个 $4 \times 4$ 的点阵的构造



这个 $4 \times 4$ 可以放在左上角, 由于 $100-4$ 是 6 的倍数, $100 \times 100$ 点阵的其余区域可以分成若干个下图的 $2 \times 6$ 的区域(或着旋转 $90^{\circ}$ 后的 $6 \times 2$ 的区域).


这个构造恰好包含 3332 个面积为 $\frac{1}{2}$ 的三角形与 1 个单位正方形, 总面积为 1667.

评注 对于一般的 $n \times n$ 的点阵 ( $n \geq 2$ 是整数), 问题的结果即凸多边形的面积之和的最小可能值为

$$
S_{\min }=\frac{1}{2} \times\left\lceil\frac{n^{2}}{3}\right\rceil+\frac{1}{2} \times \mathbf{1}_{\{n=3,5\}}
$$

我们考虑点阵中横纵坐标均为奇数的点的个数, $3 \times 3$ 点阵中有 4 个这样的点, $5 \times 5$ 点阵中有 9 个这样的点, 因此一定有某个凸 $a_{k}$ 边形含有两个这样的点作为顶点, 该凸多边形中内部含有一个整点, 这时面积不等式无法取等.

因此 $n=3$ 时无法恰好有 3 个面积为 $\frac{1}{2}$ 的三角形, $n=5$ 时无法恰好有 7 个面积为 $\frac{1}{2}$ 的三角形与 1 个面积为 1 的四边形, 即 $n=3,5$ 时, $S \geq \frac{1}{2} \times\left\lceil\frac{n^{2}}{3}\right\rceil$无法取等, (取等要求每个 $a_{k}$ 边形的面积恰好是 $\frac{1}{2} \times\left\lceil\frac{a_{k}}{3}\right\rceil$, 只能 $a_{k}=3,4$; 并且 $\sum_{k}\left\lceil\frac{a_{k}}{3}\right\rceil \geq\left\lceil\frac{\sum_{k} a_{k}}{3}\right\rceil$ 取等时至多有一个四边形).

面积之和的最小值 $S_{\text {min }}=\frac{1}{2} \times\left\lceil\frac{n^{2}}{3}\right\rceil+\frac{1}{2} \times \mathbf{1}_{\{n=3,5\}}$ 是可以取到的, 有兴趣的同学可以尝试构造.

题 5 给定奇素数 $p$, 求满足下述条件的最大正整数 $k$ :

对任意非负整数 $a_{0}, a_{1}, \ldots, a_{k-1}$, 存在非负整数 $u, v$ 使得

$$
\mathrm{C}_{u}^{v+i} \equiv a_{i} \quad(\bmod p), \quad i=0,1, \ldots, k-1
$$

其中组合数 $\mathrm{C}_{n}^{m}(n, m$ 是非负整数) 定义如下:

如果 $m \leq n$, 则 $\mathrm{C}_{n}^{m}=\frac{n !}{m !(n-m) !}$, 否则 $\mathrm{C}_{n}^{m}=0$. 这里 $0 !=1$.

解 我们先证明 $k=2$ 符合题意. 不妨设 $0 \leq a_{0} \leq p-1,0 \leq a_{1} \leq p-1$.

如果 $a_{1}=0$, 我们取 $u=p \times a_{0}, v=p$, 由 Lucas 定理, $\mathrm{C}_{u}^{v} \equiv a_{0}(\bmod p)$, 而 $\mathrm{C}_{u}^{v+1}$ 是 $p$ 的倍数, 符合题意;

如果 $a_{1}>0, a_{0}=0$, 我们取 $u=p \times a_{1}, v=p-1$, 由 Lucas 定理, $\mathrm{C}_{u}^{v+1} \equiv a_{1}$ $(\bmod p)$, 而 $\mathrm{C}_{u}^{v}$ 是 $p$ 的倍数, 符合题意;

如果 $a_{1}>0, a_{0}>0$, 假设 $a_{1} \equiv m \times a_{0}(\bmod p)$, 其中 $m \in\{1,2, \ldots, p-1\}$ ，我们取 $u=p \times a_{0}+m, v=p$, 由 Lucas 定理, $\mathrm{C}_{u}^{v} \equiv a_{0}(\bmod p)$, 而 $\mathrm{C}_{u}^{v+1} \equiv$ $m \times a_{0} \equiv a_{1}(\bmod p)$, 符合题意.

下面我们证明 $k \geq 3$ 不合题意, 为此我们证明不存在非负整数 $u, v$ 使得 $\mathrm{C}_{u}^{v}, \mathrm{C}_{u}^{v+1}, \mathrm{C}_{u}^{v+2}$ 均模 $p$ 余 1.

假设它们均模 $p$ 余 1 , 在恒等式 $(u-v) \times \mathrm{C}_{u}^{v}=(v+1) \times \mathrm{C}_{u}^{v+1}$ 两边模 $p$ 得到 $v+1 \equiv u-v(\bmod p)$, 在恒等式 $(u-v-1) \times \mathrm{C}_{u}^{v+1}=(v+2) \times \mathrm{C}_{u}^{v+2}$ 两边模 $p$ 得到 $v+2 \equiv u-v-1(\bmod p)$, 两式相减得到 $-1 \equiv 1(\bmod p)$, 矛盾!

综上所述, 所求最大的 $k=2$.

评注 如果素数 $p=2$, 则本题的结果为 $k=3$. 事实上不存在 $u, v$ 使得

$$
\mathrm{C}_{u}^{v} \equiv 1, \quad \mathrm{C}_{u}^{v+1} \equiv 1, \quad \mathrm{C}_{u}^{v+2} \equiv 0, \mathrm{C}_{u}^{v+3} \equiv 1 \quad(\bmod 2)
$$

若不然, 则二进制加法 $v+(u-v)$ 不进位, $(v+1)+(u-v-1)$ 也不进位,若 $u$ 是偶数则其中有一个式子是两个奇数相加一定会进位. 因此 $u$ 是奇数, 这时对任意偶数 $x$, 二进制加法 $x+(u-x)$ 不进位等价于 $(x+1)+(u-x-1)$ 不进位, 若 $v$ 是偶数则取 $x=v+2$, 若 $v$ 是奇数则取 $x=v+1$, 将会产生进位情况不一致的矛盾。

题 6 设 $n$ 是正整数, 记 $\lambda_{n}$ 是满足下述条件的最小实数 $\lambda$ :

对任意 $n$ 个复数 $z_{1}, z_{2}, \ldots, z_{n}$ ，均存在 $\{1,2, \ldots, n\}$ 的非空子集 $B$ 使得

$$
\lambda \cdot\left|\sum_{k \in B} z_{k}\right| \geq \sum_{k=1}^{n}\left|z_{k}\right|
$$

(1) 求 $\lambda_{4}$;

(2) 求 $\lambda_{100}$.

解 对复数集合(可重集) $Z=\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$, 定义其所有部分和的最大模长 $H(Z)=\max _{B \subseteq\{1,2, \ldots, n\}}\left|\sum_{k \in B} z_{k}\right|$. 问题等价于考虑 $Z$ 中元素的模长总和至多是 $H(Z)$ 的多少倍.

如果 $z_{1}+z_{2}+\cdots+z_{n} \neq 0$, 不妨设 $z_{1}+z_{2}+\cdots+z_{n}=1$, 由 $n \geq 3$ 知存在某个数的实部 $\Re\left(z_{k}\right)<\frac{1}{2}$, 这样 $\left|z_{k}-1\right|>\left|z_{k}\right|$. 我们在 $Z=\left\{z_{1}, \ldots, z_{n}\right\}$ 中将 $z_{k}$替换为 $z_{k}-1$, 得到集合 $Z^{\prime}$, 由于 $Z^{\prime}$ 的部分和都是 $\left\{z_{1}, \ldots, z_{n},-1\right\}$ 的部分和,并且 $\left\{z_{1}, \ldots, z_{n},-1\right\}$ (总和为 0$)$ 的部分和均为 $Z$ 的部分和或部分和的相反数,因此 $H\left(Z^{\prime}\right) \leq H\left(\left\{z_{1}, \ldots, z_{n},-1\right\}\right)=H(Z)$, 同时 $Z^{\prime}$ 的模长总和大于 $Z$ 的模长总和。

我们假设 $z_{1}+z_{2}+\cdots+z_{n}=0$, 并且 $z_{1}, z_{2}, \ldots, z_{n}$ 的幅角主值从小到大排列. 我们考虑顺次求和:

$A_{1}=z_{1}, A_{2}=z_{1}+z_{2}, \ldots, A_{k}=z_{1}+z_{2}+\cdots+z_{k}, \ldots, A_{n}=z_{1}+z_{2}+\cdots+z_{n}=0$.

在复平面上, $A_{1}, A_{2}, \ldots, A_{n}$ 构成某个凸 $n$ 边形 $\Omega$ 的按逆时针排列 $n$ 个顶点. 由于 $Z$ 的任何部分和 $S$ 的模长 $|S|$ 不超过 $Z$ 中与 $S$ 夹角 $<90^{\circ}$ 的复数到 $S$方向的投影长度之和, 因此 $|S|$ 不超过 $z_{1}, z_{2}, \ldots, z_{n}$ 中幅角在某个半平面内(即其中连续若干项)的部分和的模长, 即 $|S|$ 不超过某个 $A_{i}-A_{j}$ 的模长, 也就是 $|S|$ 不超过 $\Omega$ 的某条对角线长或某条边长. 另一方面 $A_{1}, A_{2}, \ldots, A_{n}$ 中任意两数之差均为 $Z$ 的部分和. 因此 $H(Z)$ 等于凸 $n$ 边形 $\Omega$ 的所有对角线长的最大值.为方便叙述, 我们将凸多边形的边也视为对角线.

这样我们的问题转化为: 已知凸 $n$ 边形的所有对角线长均不超过 1 , 求该凸
$n$ 边形的周长 $L$ 的最大可能值 $\lambda_{n}$.

(1) 当 $n=4$ 时, 考虑凸四边形 $A_{1} A_{2} A_{3} A_{4}$, 如果某条边的长度 $=1$, 不妨设 $\left|A_{1} A_{2}\right|=1$, 此时 $A_{3}, A_{4}$ 在左图中的区域内 (即分别以 $A_{1}, A_{2}$ 为中心的 $60^{\circ}$ 圆弧与线段 $A_{1} A_{2}$ 围成的区域).


为使周长最大化, 首先 $A_{3}, A_{4}$ 需在区域边界上, 不然取直线 $A_{3} A_{4}$ 与区域边界的交点, (易知区域边界上任意两点的距离不超过 1), 四边形周长变大.

Case 1: 如果 $A_{3}, A_{4}$ 同一侧边界上, 不妨设均在左边界弧 $\widehat{M A_{1}}$ 上, 记 $\alpha=\angle A_{1} A_{2} A_{4}, \beta=\angle A_{4} A_{2} A_{3}$, 满足 $\alpha+\beta \leq 60^{\circ}$, 则周长

$L=2+2 \sin \frac{\alpha}{2}+2 \sin \frac{\beta}{2} \leq 2+4 \sin \frac{\alpha+\beta}{4} \leq 2+4 \sin 15^{\circ}=2+\sqrt{6}-\sqrt{2}:=L^{\star}$.

当 $A_{3}$ 取 $M$ 点, $A_{4}$ 取弧 $\widehat{M A_{1}}$ 的中点时, $L$ 达到最大值 $L^{\star}$.

Case 2: 如果 $A_{4}$ 在左边界, $A_{3}$ 在右边界, 不妨设 $A_{3}$ 相比 $A_{4}$ 到直线 $A_{1} A_{2}$的距离更大. 我们断言将 $A_{3}$ 移动至点 $M$ 时, 四边形周长变大, 即

$$
\left|A_{3} A_{2}\right|+\left|A_{3} A_{4}\right|<\left|M A_{2}\right|+\left|M A_{4}\right| .
$$

这等价于证明 $\left|A_{2} M\right|-\left|A_{2} A_{3}\right|>\left|A_{4} A_{3}\right|-\left|A_{4} M\right|$, 考虑点 $A_{2}$ 关于 $A_{3} M$ 的中垂线的对称点 $A_{2}^{\prime}$, 即 $A_{3}$ 绕 $A_{1}$ 拟时针旋转 $60^{\circ}$ 到达 $A_{2}^{\prime}$, 此时 $\left|A_{2} M\right|-\left|A_{2} A_{3}\right|=$ $\left|A_{2}^{\prime} A_{3}\right|-\left|A_{2}^{\prime} M\right|$. 证明断言转化为证明 $\left|A_{2}^{\prime} A_{3}\right|-\left|A_{2}^{\prime} M\right|>\left|A_{4} A_{3}\right|-\left|A_{4} M\right|$, 即

$$
\left|A_{2}^{\prime} A_{3}\right|+\left|A_{4} M\right|>\left|A_{4} A_{3}\right|+\left|A_{2}^{\prime} M\right| \text {. }
$$

由于点 $A_{4}, A_{2}^{\prime}$ 在直线 $A_{3} M$ 的下方, 且点 $A_{4}, A_{3}, M, A_{2}^{\prime}$ 到直线 $A_{1} A_{2}$ 的距离依次增大, 这样射线 $A_{4} A_{3}$ 与射线 $A_{2}^{\prime} M$ 交于直线 $A_{3} M$ 上方的某点. 因此 $A_{4} A_{3} M A_{2}^{\prime}$ 构成凸四边形的四个顶点, 其两条对角线 $A_{2}^{\prime} A_{3}, A_{4} M$ 长度之和大于两条对边 $A_{4} A_{3}, A_{2}^{\prime} M$ 的长度之和, 即上式成立, 从而断言得证.

这样, 四边形 $A_{1} A_{2} A_{3} A_{4}$ 的周长, 不超过四边形 $A_{1} A_{2} M A_{4}$ 的周长, 即不超过 Case 1 中的上界 $L^{\star}=2+\sqrt{6}-\sqrt{2}$.



如果凸四边形 $A_{1} A_{2} A_{3} A_{4}$ 的四条边长均小于 1 , 记 $A_{1}, A_{3}$ 所在直线为 $l$, 我们固定 $A_{2} A_{4}$ 两点, 让 $A_{1}, A_{3}$ 在直线 $l$ 上活动, 向右移动 $t$ 距离到达 $U_{t}, V_{t}$ 的位置 $\left(t<0\right.$ 时即为向左移动 $-t$ 的距离). 考虑四边形 $U_{t} A_{2} V_{t} A_{4}$ 的周长

$$
L(t)=\left|U_{t} A_{2}\right|+\left|U_{t} A_{4}\right|+\left|V_{t} A_{2}\right|+\left|V_{t} A_{4}\right|
$$

是关于 $t$ 的下凸函数, 因为每一项均为 $\sqrt{(t-\square)^{2}+\square^{2}}$ 的形式, 均为下凸函数.

考虑每条边长 $\leq 1$ 对 $t$ 的约束, 对应 $t$ 的范围是一个包含 0 的闭区间. 四个闭区间的交集仍为某个闭区间 $\left[t_{1}, t_{2}\right]$, 其中 $t_{1}<0<t_{2}$. 对 $t=t_{1}$ 或 $t=t_{2}$ 的情形, 四边形至少有一条边长为 1 , 此时周长 $L\left(t_{1}\right) \leq L^{\star}, L\left(t_{2}\right) \leq L^{\star}$. 由函数 $L(t)$的下凸性质可知

$$
L(0) \leq \max \left\{L\left(t_{1}\right), L\left(t_{2}\right)\right\} \leq L^{\star}=2+\sqrt{6}-\sqrt{2}
$$

因此 $\lambda_{4}=2+\sqrt{6}-\sqrt{2}$. 对应的四个复数是

$$
\left\{z_{1}, z_{2}, z_{3}, z_{4}\right\}=\left\{-\frac{1}{2}+\frac{\sqrt{3}}{2} \mathbf{i},-\frac{1}{2}-\frac{\sqrt{3}}{2} \mathbf{i}, \frac{1}{2}+\left(1-\frac{\sqrt{3}}{2}\right) \mathbf{i}, \frac{1}{2}-\left(1-\frac{\sqrt{3}}{2}\right) \mathbf{i}\right\} .
$$

(2) 对一般的 $n$, 我们证明: 如果复平面上的凸 $n$ 边形 $\Omega=A_{1} A_{2} \ldots A_{n}$ 的每条对角线长(包括边长)均 $\leq 1$, 则其周长 $L \leq 2 n \sin \frac{\pi}{2 n}$.

我们考虑多边形向各方向投影长度的平均值来估计周长.

对倾角为 $\alpha$ 的直线 $l_{\alpha}$, 考虑凸多边形 $\Omega$ 向 $l_{\alpha}$ 的投影长度 $J_{\alpha}(\Omega)$. 同时考虑每条边 $A_{k} A_{k+1}$ 到直线 $l_{\alpha}$ 的投影长度 $J_{\alpha}\left(A_{k} A_{k+1}\right)$, 由于是凸多边形, 总投影区间里面的每个小段恰好被两条边的投影覆盖, 因此

$$
\sum_{k=1}^{n} J_{\alpha}\left(A_{k} A_{k+1}\right)=2 J_{\alpha}(\Omega)
$$

将倾角 $\alpha$ 看作时间, 即直线 $l_{\alpha}$ 的倾角 $\alpha$ 逐渐变化, 注意任意图形(多边形 $\Omega$或是某条线段)的投影长度 $J_{\alpha}=J_{\alpha+\pi}$, 即投影长度的变化以时间 $\pi$ 为周期.

我们考虑在一个 $\pi$ 周期内, 各边投影长度的平均值(或累积值). 对某个倾角为 $\beta$ 的边 $A_{k} A_{k+1}$, 投影长度为 $J_{\alpha}\left(A_{k} A_{k+1}\right)=\left|A_{k} A_{k+1}\right| \cdot|\cos (\alpha-\beta)|$, (函数
$|\cos x|$ 以 $\pi$ 为周期), 因此

$$
\begin{aligned}
\int_{0}^{\pi} J_{\alpha}\left(A_{k} A_{k+1}\right) \mathrm{d} \alpha & =\int_{0}^{\pi}\left|A_{k} A_{k+1}\right| \cdot|\cos (\alpha-\beta)| \mathrm{d} \alpha \\
& =\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left|A_{k} A_{k+1}\right| \cdot|\cos x| \mathrm{d} x=2 \cdot\left|A_{k} A_{k+1}\right| .
\end{aligned}
$$

所以

$$
\int_{0}^{\pi} J_{\alpha}(\Omega) \mathrm{d} \alpha=\frac{1}{2} \sum_{k=1}^{n} \int_{0}^{\pi} J_{\alpha}\left(A_{k} A_{k+1}\right) \mathrm{d} \alpha=\sum_{k=1}^{n}\left|A_{k} A_{k+1}\right|=L .
$$

我们估计周长 $L=\int_{0}^{\pi} J_{\alpha}(\Omega) \mathrm{d} \alpha$ 的上界. 对每个时刻 $\alpha$, 多边形 $\Omega$ 有某条对角线到 $l_{\alpha}$ 的投影长度恰好为 $J_{\alpha}(\Omega)$, 称该对角线为此时的“支撑对角线”, 并称执行过一段时间支撑任务的对角线为“好对角线”. 当 $\alpha$ 缓缓增加时，只有直线 $l_{\alpha}$ 恰好与某条边 $A_{k} A_{k+1}$ 垂直时, 支撑对角线会发生变化(称之为换班), 即此时将“对角线二点组”里面的 $A_{k}$ 换为 $A_{k+1}$. 在一个 $\pi$ 周期内, 所有好对角线恰好各出场一次, 但周期内换班不超过 $n$ 次, 因此好对角线不超过 $n$ 条.

考虑某条好对角线 $A_{i} A_{j}$, 设其倾角为 $\beta$, 长度 $\left|A_{i} A_{j}\right| \leq 1$. 在某个周期内执行支撑任务的时间区间为 $\left[\alpha_{1}, \alpha_{2}\right]$, (其中 $\beta-\frac{\pi}{2} \leq \alpha_{1} \leq \beta \leq \alpha_{2} \leq \beta+\frac{\pi}{2}$ ), 该对角线对 $\int_{0}^{\pi} J_{\alpha}(\Omega) \mathrm{d} \alpha$ 的贡献为

$$
\begin{aligned}
\int_{\alpha_{1}}^{\alpha_{2}} J_{\alpha}(\Omega) \mathrm{d} \alpha & =\left|A_{i} A_{j}\right| \cdot \int_{\alpha_{1}}^{\alpha_{2}} \cos (\alpha-\beta) \mathrm{d} \alpha=\left|A_{i} A_{j}\right| \cdot\left(\sin \left(\alpha_{2}-\beta\right)-\sin \left(\alpha_{1}-\beta\right)\right) \\
& =\left|A_{i} A_{j}\right| \cdot 2 \sin \frac{\alpha_{2}-\alpha_{1}}{2} \cdot \cos \left(\frac{\alpha_{2}+\alpha_{1}}{2}-\beta\right) \leq 2 \sin \frac{\alpha_{2}-\alpha_{1}}{2} .
\end{aligned}
$$

假设所有 $n_{1} \leq n$ 条好对角线在 $\pi$ 周期内的执行支撑任务的时长分别为 $\theta_{1}, \theta_{2}, \ldots, \theta_{n_{1}}$, 总和为 $\pi$. 由 $\sin$ 函数在 $[0, \pi]$ 的凸性可知

$$
L=\int_{0}^{\pi} J_{\alpha}(\Omega) \mathrm{d} \alpha \leq \sum_{k=1}^{n_{1}} 2 \sin \frac{\theta_{k}}{2} \leq 2 n_{1} \sin \frac{\pi}{2 n_{1}} \leq 2 n \sin \frac{\pi}{2 n}
$$

关于构造, 我们希望恰有 $n$ 个对角线各执行 $\frac{\pi}{n}$ 时间的支撑任务.

如果 $n$ 不是 2 的方幕, 则可以分解为 $n=m \times r$, 其中 $m=2 h+1 \geq 3$ 是奇数. 我们取正 $m$ 边形 $B_{1} B_{2} \ldots B_{m}$, 其中最长对角线 $B_{k} B_{k+h}=B_{k} B_{k+h+1}=1$,对 $k=1,2, \ldots, m$, 依次以 $B_{k}$ 为心, 1 为半径画劣弧 $\widehat{B_{k+h} B_{k+h+1}}$, 然后将该劣弧 $r$ 等分, 取出 $r-1$ 个等分点, 这样得到的 $m(r-1)$ 个等分点以及原来的 $B_{1}, \ldots, B_{m}$ 一共 $m r=n$ 个点构成多边形 $\Omega$ 的 $n$ 个顶点, 易知 $\Omega$ 的最长对角线为 1 且每条边长均为 $2 \sin \frac{\pi}{2 m r}=2 \sin \frac{\pi}{2 n}$, 周长 $L=2 n \sin \frac{\pi}{2 n}$ 达到最大.

多边形 $\Omega$ 以 $\frac{1}{2 \sin \frac{\pi}{2 n}}$ 的比例位似放大后, 其 $n$ 条边的向量(复数)可以是

$$
\left\{\mathbf{e}^{(u \times 2 r+v) \times \frac{2 \pi \mathbf{i}}{2 n}}, \quad u=0,1, \ldots, m-1, v=0,1, \ldots, r-1 .\right\} .
$$

这是达到极值的 $\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$. 这个构造可以理解为把所有 $2 n=2 m r$ 次单位根分成 $2 m$ 组, 每组是连续 $r$ 个单位根, 然后取一组, 空一组, 取一组, 空一组, $\ldots$, 一共取出 $n=m r$ 个单位根.

因此当 $n$ 不是 2 的方幂时, $\lambda_{n}=2 n \sin \frac{\pi}{2 n}$. 特别的, $\lambda_{100}=200 \sin \frac{\pi}{200}$. 下右图是 $n=100(m=5)$ 时的多边形 $\Omega$ 的示意图(该图的构造是受到等宽曲线的启发). 下左图是 $n=100(m=5)$ 时的复数 $\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$ 的分布的示意图.


（2）解 2 构造同解法一. 证明部分, 我们假设 $\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$ 的任意部分和的模长均 $\leq 1$. (可以不假设总和为 0 ).

将总和为 0 的 $2 n$ 个复数 $\left\{z_{1}, z_{2}, \ldots, z_{n},-z_{1},-z_{2}, \ldots,-z_{n}\right\}$ 按照幅角主值从小到大的顺序排列, 并顺次组成某个凸 $2 n$ 边形(可能不严格凸) $\Omega=$ $P_{1} P_{2} \ldots P_{n} P_{n+1} \ldots P_{2 n}$ 的 $2 n$ 个边向量, (这相当于把 $2 n$ 个复数对应的向量围成一圈). 此时 $\Omega$ 是中心对称图形, 设其对称中心为 $O$.

在复平面上, $\Omega$ 的两个顶点的差是 $\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$ 的某两个部分和之差, 即两个顶点的距离等于

$$
\left|\sum_{k \in B_{1}} z_{k}-\sum_{l \in B_{2}} z_{l}\right| \leq\left|\sum_{k \in B_{1}} z_{k}\right|+\left|\sum_{l \in B_{2}} z_{l}\right| \leq 2
$$

特别的 $\left|P_{k} P_{n+k}\right|=2\left|O P_{k}\right| \leq 2$, 因此 $\Omega$ 的所有顶点均在以 $O$ 为中心半径为 1 的圆盘内. 对 $k=1,2, \ldots, 2 n$, 延长 $O P_{k}$ 交圆周于点 $Q_{k}$, 这时凸多边形 $\Omega$ 被凸 $2 n$边形 $\Omega^{\prime}=Q_{1} Q_{2} \ldots Q_{2 n}$ 覆盖.

我们每次沿着 $\Omega$ 的某条边所在直线切一刀, 把 $\Omega^{\prime}$ 的在直线另一侧的部分切掉, 这样使得剩下的图形周长变小, 经过若干次操作后 $\Omega^{\prime}$ 最终变成 $\Omega$, 且周长不断变小. 因此周长 $L(\Omega) \leq L\left(\Omega^{\prime}\right)$.
设单位圆内接 $2 n$ 边形 $\Omega^{\prime}$ 各边对应的圆周角分别为 $\theta_{1}, \theta_{2}, \ldots, \theta_{2 n}$ (总和为 $\pi$, 且 $\left.\theta_{k}=\theta_{k+n}\right)$, 则其周长

$$
L\left(\Omega^{\prime}\right)=\sum_{k=1}^{2 n} 2 \sin \theta_{k} \leq 2 \times 2 n \sin \frac{\theta_{1}+\theta_{2}+\cdots+\theta_{2 n}}{2 n}=4 n \sin \frac{\pi}{2 n}
$$

因此

$$
\left|z_{1}\right|+\left|z_{2}\right|+\cdots+\left|z_{n}\right|=\frac{1}{2} L(\Omega) \leq \frac{1}{2} L\left(\Omega^{\prime}\right) \leq 2 n \sin \frac{\pi}{2 n} .
$$

评注 1 我们考虑 $\lambda_{n}=2 n \sin \frac{\pi}{2 n}$ 的可能构造, 由证法一的思路可知此时恰有 $n$ 条好对角线, 满足长度相等 (设长度均为 1 ) 且两两夹角均为 $\frac{\pi}{n}$ 的整数倍.此时任意两条好对角线均相交(不然会有两个顶点的距离大于 1 ). 考虑 $n$ 个顶点与 $n$ 个好对角线(看作图的边)构成的图, 由顶点数等于边数知图中有圈, 若是长度为偶数的圈 $X_{1} X_{2} \ldots X_{2 h}$, 则 $X_{k} X_{k+1}$ 与 $X_{1} X_{2}$ 相交, 即点 $X_{k}, X_{k+1}$ 在直线 $X_{1} X_{2}$ 两侧 $(k=3,4, \ldots, 2 h-1)$, 这样可推得 $X_{3}$ 与 $X_{2 h}$ 在直线 $X_{1} X_{2}$ 两侧, 这会使得 $X_{2 h} X_{1}$ 与 $X_{2} X_{3}$ 不交导致矛盾, 因此图中一定有长度为奇数的圈 $X_{1} X_{2} \ldots X_{2 h+1}$, 即一个 $m=2 h+1$ 角星的形状的骨架. 这个 $m$ 角星的 $m$ 个角均为 $\frac{\pi}{n}$ 的整数倍, 且 $m$ 个角之和等于 $\pi$.

当 $n$ 有奇数因子 $m=2 h+1$ 时, 我们容易想到正 $m$ 角星的例子, 这也是解答中的构造. 记 $\omega=\mathbf{e}^{\frac{\pi i}{n}}$ 是 $2 n$ 次单位根, 一般的满足要求的 $m$ 角星对应多项式 $f(x)=x^{i_{1}}+x^{i_{2}}+\cdots+x^{i_{m}}$ 使得 $f(\omega)=0$.

当 $n=2^{r}$ 是 2 的方幂时, $\omega=\mathbf{e}^{\frac{\pi \mathrm{i}}{n}}$ 的极小多项式是分圆多项式 $\Phi_{2 n}(x)=$ $x^{n}+1$, 若存在上述多项式 $f(x)=x^{i_{1}}+\cdots+x^{i_{m}}$ 使得 $f(\omega)=0$, 则整系数多项式 $\Phi_{2 n}(x)=x^{n}+1$ 整除 $f(x)$, 此时代入 $x=1$ 可得 2 整除奇数 $m$, 导致矛盾.

因此当 $n$ 是 2 的方幂时有 $\lambda_{n}<2 n \sin \frac{\pi}{2 n}$.

评注 2 从证法二的角度来看 $\lambda_{n}=2 n \sin \frac{\pi}{2 n}$ 的构造, 由于 $\left\{z_{1}, z_{2}, \ldots, z_{n},-z_{1}\right.$ ， $\left.-z_{2}, \ldots,-z_{n}\right\}$ 恰好是所有的 $2 n$ 次单位根 $\left\{\omega^{0}, \omega^{1}, \ldots, \omega^{2 n-1}\right\}$ ，且 $\left\{z_{1}, z_{2}, \ldots, z_{n}\right\}$是其中每对相反数 $\left\{\omega^{k}, \omega^{k+n}\right\}$ 中恰好取出一个, 所以 $z_{1}+z_{2}+\cdots+z_{n}=0$ 可以表示为某个 $\pm \omega^{0} \pm \omega^{1} \pm \omega^{2} \pm \cdots \pm \omega^{n-1}$ 的形式.

当 $n=2^{r}$ 是 2 的方幂时, 由于 $\omega$ 的极小多项式是分圆多项式 $\Phi_{2 n}(x)=$ $x^{n}+1$, 可知上式无法成立. 即 $n$ 是 2 的方幂时有 $\lambda_{n}<2 n \sin \frac{\pi}{2 n}$.

