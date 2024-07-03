# 第三十二期问题征解解答与点评 

牟晓生

第一题 设 $A, B, C, D$ 内接于圆 $O, A C$ 与 $B D$ 相交于 $E . P, Q$ 是四边形 $A B C D$ 的一对等角共轭点. 证明: $\angle O P E=\angle O Q E$.

(浙江杭州高级中学 张晋源 供题)

证明 (根据浙江镇海中学袁昊喆同学的解答整理):

引理 1 完全四边形 $A B F C G D$ 中 $A B C D$ 共圆, 圆心为 $O, A C$ 交 $B D$ 于 $E$, 则完全四边形 $A B F C G D$ 的密克点为 $O E$ 和 $F G$ 的交点.



证明 取密克点 $M$,则 $G D C M$ 与 $C B F M$ 分别共圆. 所以

$$
\angle C M G=\angle A D C=180^{\circ}-\angle A B C=180^{\circ}-\angle C M F,
$$

所以 $G M F$ 共线. 因为 $F G$ 为 $E$ 极线, 所以 $O E \perp F G$. 而

$$
G M^{2}-F M^{2}=G M \cdot G F-F M \cdot F G=G C \cdot G B-F C \cdot F D=G O^{2}-F O^{2},
$$

所以 $O M \perp F G$, 所以 $O E M$ 共线, 引理得证!

引理 2 四边形的等角共轭点是反演反射变换的对应点.

证明 完全四边形 $A B F C G D$ 的密克点为 $M, P, Q\left(P_{1}\right)$ 为一对等角共轭点,考虑以 $M E \cdot M F$ 为幂, 以 $\angle E M F$ 为角平分线所在直线为轴的反演反射变换.



显然 $A V, B D, E F$ 分别为对应点.

设 $P$ 的对应点为 $P_{1}$. 因为

$$
\begin{aligned}
\angle A P_{1} B & =\angle A M B-\angle M A P_{1}-\angle M B P_{1} \\
& =\angle C M D-\angle M P C-\angle M P D \\
& =\angle F-\angle C P D \\
& =\angle F-180^{\circ}+\angle P C D+\angle P D C \\
& =\angle F-180^{\circ}+\angle Q C B+\angle Q D A \\
& =180^{\circ}-\angle C Q D \\
& =\angle A Q B,
\end{aligned}
$$

同理有

$$
\angle B Q C=\angle B P_{1} C, \angle C Q D=\angle C P_{1} D, \angle D Q A=\angle D P_{1} A
$$

所以 $P_{1}, Q$ 重合, 引理得证!

回到原题.



设 $A D$ 交 $B C$ 于 $G, A B$ 交 $D C$, 密克点为 $M$.
由布洛卡定理, $O$ 为 $\triangle E F G$ 的垂心; 由引理 $1, O E M \perp F G$. 所以

$$
M E \cdot M O=M F \cdot M G,
$$

所以 $O, E$ 为反演反射变换的对应点.

由引理 2 , 知

$$
\triangle Q M E \sim \triangle O M P, \triangle P M E \sim \triangle O M Q
$$

所以

$$
\angle Q E M=\angle O P M, \angle Q O M=\angle E P M \text {, }
$$

相减即得 $\angle O Q E=\angle O P E$.

评注 重庆巴蜀中学但流金, 山大附中王子或, 杭州二中刘浩宇, 北京十一学校崔云形, 华东师大二附中刘子宁, 河北省石家庄市第二中学贾镐铮等同学也给出了本题的正确解答.

第二题 给定正整数 $n$, 证明存在正整数 $m$ 满足以下条件: 对于任意 $\{1, \ldots, m\}$ 的子集 $G$, 若 $|G| \geq \frac{m}{2}$, 则存在 $n+1$ 个正整数 $x_{0}, x_{1}, \ldots, x_{n}$, 使得 $\left\{x_{1}, \ldots, x_{n}\right\}$ 中任意若干元素与 $x_{0}$ 的和都属于 $G$.

(上海大学 吴尉迟 供题)

## 证明 (根据供题者的解答整理):

我们将结论加强, 证明对任意给定的 $\delta \in(0,1)$, 只要 $m$ 足够大且 $|G| \geq \delta m$,则可以找到满足条件的 $x_{0}, \ldots, x_{n}$. 对 $n$ 进行归纳: 当 $n=1$ 时只需 $m>\frac{1}{\delta}$ 即可保证 $G$ 有两个不同元素 $a, b$. 则 $x_{0}=\min \{a, b\}, x_{1}=|b-a|$ 满足条件.

假设命题对 $n-1$ 成立. 具体地, 令 $q$ 为满足以下条件的一个正整数: 只要 $m \geq q$ 且 $G \subset\{1, \ldots, m-1\}$ 满足 $|G| \geq \frac{\delta}{2} \cdot m$, 则能在 $G$ 中找到满足条件的 $x_{0}, \ldots, x_{n-1}$. 下面考虑任意正整数 $M$ 使得 $M>\left(1+\frac{4}{\delta^{2}}\right) q$, 以及 $M>\frac{2}{\delta} q^{n}+q$.将 $M$ 写成

$$
M=q \cdot r+t, \quad 0 \leq t \leq q-1
$$

则 $r>\frac{4}{\delta^{2}}, \frac{\delta}{2} r>q^{n-1}$.

设 $G \subset\{1, \ldots, M-1\}$, 且 $|G| \geq \delta M$. 令 $G_{i}=G \cap((i-1) q, i q), \forall 1 \leq i \leq r$,则简单的计数可知至少有 $R=\frac{\delta}{2} r$ 个下标 $i$ 使得 $\left|G_{i}\right| \geq \frac{\delta}{2} q$. 于是由归纳假设, 对每个这样的 $G_{i}$, 存在满足条件的正整数 $x_{i, 0}, x_{i, 1}, \ldots, x_{i, n-1}$. 由于 $x_{i, 0}$ 和 $x_{i, 0}+\cdots+x_{i, n-1}$ 都属于 $G_{i}$, 它们都大于 $(i-1) q$ 而小于 $i q$. 因此
$x_{i, 1}, x_{i, 2}, \ldots, x_{i, n-1}$ 每个都至多为 $q$.

由于我们有 $R>q^{n-1}$ 个不同的下标 $i$, 由抽庹原理知存在 $i<j$, 使得 $x_{i, k}=x_{j, k}$ 对每个 $1 \leq k \leq n-1$ 成立. 于是令

$$
x_{k}=x_{i, k}, \forall 0 \leq k \leq n-1, \quad x_{n}=x_{j, 0}-x_{i, 0}
$$

即能满足题目要求. 这样就完成了归纳证明.

评注 (1). 杭州二中刘浩宇同学给出了本题的正确解答.

(2). 这道题的形式和范德瓦尔登定理以及拉多定理相近, 因此归纳法是比较自然的. 关键是要敢于加强命题.

第三题 给定正整数 $n$, 求最大的正常数 $c_{n}$ 满足以下条件: 对于任意 $n$ 次实系数多项式 $f(x)=\sum_{k=0}^{n} b_{k} x^{k}$, 若 $f(x)$ 的复根全在单位圆上, 则有

$$
\left|\sum_{k=0}^{n} \sum_{j=0}^{k}\left(\begin{array}{l}
n-j \\
k-j
\end{array}\right) b_{j}\right| \geq c_{n} \cdot\left|\sum_{j=0}^{n} b_{j}\right|
$$

(浙江杭州二中学生 包恺成 供题)

## 解 (根据成都七中嘉祥外国语学校唐龙天同学的解答整理):

答案是 $\left(\frac{3}{2}\right)^{n}$. 注意到

$$
\sum_{k=0}^{n} \sum_{j=0}^{k}\left(\begin{array}{l}
n-j \\
k-j
\end{array}\right) b_{j}=\sum_{j=0}^{n} b_{j} \cdot \sum_{k=j}^{n}\left(\begin{array}{l}
n-j \\
k-j
\end{array}\right)=\sum_{j=0}^{n} b_{j} 2^{n-j}=2^{n} f\left(\frac{1}{2}\right) .
$$

于是只要证明对每个满足条件的多项式 $f,\left|f\left(\frac{1}{2}\right)\right| \geq\left(\frac{3}{4}\right)^{n} \cdot|f(1)|$, 且这个常数无法改进. 因此也就只要证明当 $z$ 是单位复数时,

$$
\left|\frac{1}{2}-z\right| \geq \frac{3}{4}|1-z|
$$

等号在 $z=-1$ (也就是 $\left.f(z)=(1+z)^{n}\right)$ 时取到. 令 $z=\cos \theta+i \sin \theta$, 则以上不等式转化为

$$
5 / 4-\cos \theta \geq \frac{9}{16}(2-2 \cos \theta)
$$

也就是

$$
\frac{1}{8}+\frac{1}{8} \cos \theta \geq 0 \text {. }
$$

显然成立.

评注 济南历城二中欧瑜, 浙江省镇海中学袁昊喆, 广西师大附外马康哲, 山大附中王子或, 石家庄市第二中学贾镐铮以及杭州二中刘浩宇等同学也给出了本题的正确解答.
第四题 设 $p \equiv 3(\bmod 8)$ 是素数, 且 $p>3$. 证明存在正整数 $a, b, c<\sqrt{p}$,使得 $p=a^{2}+b c$.

(耶鲁大学 牟晓生 供题)

## 证明 (根据供题者的解答整理):

我们将证明一个更强的结论: 设 $p$ 不是完全平方数, 且存在正整数 $x \neq y$ 使得 $p=x^{2}+2 y^{2}$, 则可以找到 $0<a, b, c<\sqrt{p}$ 使得 $p=a^{2}+b c$. 因此 $p$ 为素数这一条件可以削弱.

首先假设 $x>y$. 注意到如果 $y<\frac{\sqrt{p}}{2}$ 则命题得证. 否则假设 $y>\frac{\sqrt{p}}{2}$, 则我们有

$$
p=x^{2}+2 y^{2}=(3 y-x)^{2}-y \cdot(7 y-6 x) \text {. }
$$

由于 $y>\frac{\sqrt{p}}{2}$ 且 $p=x^{2}+2 y^{2}$, 我们有 $6 x-7 y<\sqrt{p}$. 所以如果 $6 x-7 y>0$, 则上面的等式给出满足条件的 $a, b, c$. 不然 $7 y>6 x$, 由 $p=x^{2}+2 y^{2}$ 导出 $y>\frac{6}{11} \sqrt{p}$ 以及 $x<\frac{7}{11} \sqrt{p}$. 接下来我们将 $p$ 写为

$$
p=x^{2}+2 y^{2}=(5 x-4 y)^{2}+2(2 x-y)(7 y-6 x) .
$$

由于 $0<2 x-y<\sqrt{p}$, 只要 $7 y-6 x<\frac{\sqrt{p}}{2}$ 则命题得证. 否则可以继续考虑

$$
p=x^{2}+2 y^{2}=(25 y-23 x)^{2}-(7 y-6 x)(89 y-88 x) .
$$

由 $7 y-6 x>\frac{\sqrt{p}}{2}$ 可知 $88 x-99 y<\sqrt{p}$. 于是如果 $88 x>89 y$, 则上面的等式又给出满足条件的 $a, b, c$. 于是只需考虑 $89 y>88 x$ 的情况.

注意到我们通过 $x>y$ 这个假设逐步缩小范围至 $7 y>6 x$, 以至现在这个更严格的不等式 $89 y>88 x$. 如果这个过程能够一直延续下去, 最终能导出与 $x>y$ 矛盾. 下面我们就来推广这个过程. 为此定义两个递归数列:

$$
\begin{aligned}
u_{0}=0, u_{1}=6, u_{2}=88, \ldots, & \left(u_{n+1}=4 v_{n}+2-u_{n}\right) ; \\
v_{-1}=-1, v_{0}=1, v_{1}=23, v_{2}=329, \ldots, & \left(v_{n+1}=4 u_{n}-v_{n}\right) .
\end{aligned}
$$

可以验证对每个 $n \geq 0,\left(u_{n}, v_{n-1}\right)$ 以及 $\left(u_{n}, v_{n}\right)$ 这两个数组都满足方程

$$
(u-v)^{2}=2 u v+2 u+1
$$

如果 $x>y$, 则对任意 $n \geq 0$, 我们有如下等式

$$
p=x^{2}+2 y^{2}=\left[\left(v_{n}+2\right) y-v_{n} x\right]^{2}-\left[\left(u_{n}+1\right) y-u_{n} x\right] \cdot\left[\left(u_{n+1}+1\right) y-u_{n+1} x\right] .
$$

注意到在 $n=0$ 时 $u_{n} x=0<\left(u_{n}+1\right) y$, 但由于 $x>y$, 当 $n$ 足够大时一定有 $u_{n} x>\left(u_{n}+1\right) y$. 于是存在最小的非负整数 $n$, 使得 $u_{n+1} x>\left(u_{n+1}+1\right) y$. 此时
取

$$
a=\left|\left(v_{n}+2\right) y-v_{n} x\right|, \quad b=\left(u_{n}+1\right) y-u_{n} x, \quad c=\left(u_{n+1}+1\right) y-u_{n+1} x .
$$

则 $p=a^{2}+b c$ 且 $a, b, c \geq 0$. 注意到 $b<y<\sqrt{p}$, 故只要 $c<\sqrt{p}$ 即可.

为此考虑另一个等式

$p=x^{2}+2 y^{2}=\left[\left(u_{n}-v_{n-1}\right) x-\left(u_{n}-v_{n-1}-1\right) y\right]^{2}+2 \cdot\left[\left(u_{n}+1\right) y-u_{n} x\right] \cdot\left[\left(v_{n-1}+1\right) x-v_{n-1} y\right]$.

注意到 $2\left[\left(u_{n}+1\right) y-u_{n} x\right]=2 b$ 和 $\left(v_{n-1}+1\right) x-v_{n-1} y$ 都是正整数. 并且由 $\left(u_{n}+1\right) y-u_{n} x>0$ 以及 $x^{2}+2 y^{2}=p$ 可以导出

$$
y>\frac{u_{n} \sqrt{p}}{2 u_{n}-v_{n-1}}, \quad x<\frac{\left(u_{n}+1\right) \sqrt{p}}{2 u_{n}-v_{n-1}} .
$$

所以

$$
\left(v_{n-1}+1\right) x-v_{n-1} y<\frac{u_{n}+v_{n-1}+1}{2 u_{n}-v_{n-1}} \sqrt{p}<\sqrt{p} .
$$

因此如果 $2 b=\left(u_{n}+1\right) y-u_{n} x<\sqrt{p}$, 则上面的等式给出了满足条件的表示.

然而如果 $b=\left(u_{n}+1\right) y-u_{n} x>\frac{\sqrt{p}}{2}$, 则由 $x^{2}+2 y^{2}=p$ 以及 $u_{n+1}<16 u_{n}$ 容易证明

$$
c=u_{n+1} x-\left(u_{n+1}+1\right) y<\sqrt{p} \text {. }
$$

于是无论何种情况我们都找到了满足条件的 $a, b, c$.

对于 $x<y$ 的情况, 证明是类似的. 我们用下面两个等式:

$p=x^{2}+2 y^{2}=\left[\left(u_{n+1}+1\right) x-\left(u_{n+1}-1\right) y\right]^{2}-\left[\left(v_{n}+1\right) x-v_{n} y\right] \cdot\left[\left(v_{n+1}+1\right) x-v_{n+1} y\right]$,例如 $x^{2}+2 y^{2}=(x+y)^{2}-y \cdot(2 x-y)=(7 x-5 y)^{2}-(2 x-y)(24 x-23 y)$. 以及 $p=x^{2}+2 y^{2}=\left[\left(v_{n}+1-u_{n}\right) y-\left(v_{n}-u_{n}\right) x\right]^{2}+2 \cdot\left[\left(v_{n}+1\right) x-v_{n} y\right] \cdot\left[\left(u_{n}+1\right) y-u_{n} x\right]$,例如 $x^{2}+2 y^{2}=(2 y-x)^{2}+2(2 x-y) y=(18 y-17 x)^{2}+2(24 x-23 y)(7 y-6 x)$.最终需要证明 $\left(v_{n}+1\right) x-v_{n} y>\sqrt{p}$, 则 $v_{n+1} y-\left(v_{n+1}+1\right) x<\sqrt{p}$. 具体细节这里略去.

评注 由上面的证明可以看出 $x \neq y$ 这个假设是十分重要的. 事实上, $75=5^{2}+2 \times 5^{2}$ 但不存在 $a, b, c<\sqrt{75}$ 使得 $75=a^{2}+b c$.

