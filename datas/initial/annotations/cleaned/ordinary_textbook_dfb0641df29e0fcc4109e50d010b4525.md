# 第三十六期问题征解解答与点评 

张端阳

第一题 求所有的整数 $\alpha$, 使得对任意正整数 $n$ 以及任意乘积为 1 的正实数 $a_{1}, a_{2}, \ldots, a_{n}$ ，都有

$$
\sum_{i=1}^{n} \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{\alpha}} \leq n
$$

另外求所有的整数 $\alpha$ 使得上面不等式的反方向永远成立.

(山大附中学生 王子或 傅浩桐 供题)

## 解 (根据供题者的解答整理):

记 $f(\alpha)=\sum_{i=1}^{n} \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{2}}$. 注意到

$$
\sum_{i=1}^{n} \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{2}}=\sum_{i=1}^{n} \frac{\left(a_{i}^{-1}\right)^{2-\alpha}}{1-a_{i}^{-1}+\left(a_{i}^{-1}\right)^{2}}
$$

又当 $a_{1}, a_{2}, \cdots, a_{n}$ 是乘积为 1 的正实数时, $a_{1}^{-1}, a_{2}^{-1}, \cdots, a_{n}^{-1}$ 也是乘积为 1 的正实数, 所以 $f(\alpha)$ 与 $f(2-\alpha)$ 等价. 于是只需考虑 $\alpha$ 是正整数的情形.

下面分四种情形讨论.

情形 1 : 当 $\alpha=1$ 时, 由均值不等式,

$$
f(1)=\sum_{i=1}^{n} \frac{a_{i}}{1-a_{i}+a_{i}^{2}} \leq \sum_{i=1}^{n} \frac{a_{i}}{a_{i}}=n
$$

等号当且仅当 $a_{1}=a_{2}=\cdots=a_{n}=1$ 时取到.

情形 2 : 当 $\alpha=2$ 时, 若取 $a_{1}=2, a_{2}=\frac{1}{2}, a_{3}=\cdots=a_{n}=1$, 则

$$
f(2)=n-\frac{1}{3}<n \text {; }
$$

若取 $a_{1}=\cdots=a_{n-1}=2, a_{n}=\frac{1}{2^{n-1}}$, 则

$$
f(2) \geq \frac{4}{3}(n-1)>n
$$

在 $n \geq 5$ 时成立. 于是 $f(2)$ 既可以小于 $n$, 也可以大于 $n$.
情形 3: 当 $\alpha=3$ 时, 记函数

$$
g(x)=\frac{x^{3}}{1-x+x^{2}}-2 \ln x, x>0
$$

因为

$$
\begin{aligned}
g^{\prime}(x) & =\frac{x^{4}-2 x^{3}+3 x^{2}}{\left(1-x+x^{2}\right)^{2}}-\frac{2}{x} \\
& =\frac{x^{5}-4 x^{4}+7 x^{3}-6 x^{2}+4 x-2}{x\left(1-x+x^{2}\right)^{2}} \\
& =\frac{(x-1)\left(x^{2}\left(x-\frac{3}{2}\right)^{2}+(x-1)^{2}+1+\frac{3}{4} x^{2}\right)}{x\left(1-x+x^{2}\right)^{2}},
\end{aligned}
$$

所以 $g(x)$ 在 $(0,1)$ 上单调递减, 在 $(1,+\infty)$ 上单调递增, 于是 $g(x) \geq g(1)=1$.故

$$
f(3)=\sum_{i=1}^{n} g\left(a_{i}\right) \geq n \text {. }
$$

情形 $4:$ 当 $\alpha \geq 4$ 时, 记函数

$$
h(x)=\frac{x^{\alpha}}{1-x+x^{2}}, x>0
$$

则

$$
f^{\prime}(\alpha)=\sum_{i=1}^{n} \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{2}} \cdot \ln a_{i}=\sum_{i=1}^{n} h\left(a_{i}\right) \cdot \ln a_{i} .
$$

因为

$$
\begin{aligned}
h^{\prime}(x) & =\frac{\alpha x^{\alpha-1}\left(1-x+x^{2}\right)-x^{\alpha}(2 x-1)}{\left(1-x+x^{2}\right)^{2}} \\
& =\frac{x^{\alpha-1}\left((\alpha-2) x^{2}-(\alpha-1) x+\alpha\right)}{\left(1-x+x^{2}\right)^{2}}
\end{aligned}
$$

又当 $\alpha \geq 3$ 时,

$$
\alpha-2>0, \quad \triangle=(\alpha-1)^{2}-4 \alpha(\alpha-2)=-3(\alpha-1)^{2}+4 \leq 0,
$$

所以 $h^{\prime}(x) \geq 0$, 于是 $h(x)$ 在 $(0,+\infty)$ 上单调不减.

不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 则

$$
\ln a_{1} \leq \ln a_{2} \leq \cdots \leq \ln a_{n}, \quad h\left(a_{1}\right) \leq h\left(a_{2}\right) \leq \cdots \leq h\left(a_{n}\right) .
$$

从而由 Chebyshev 不等式,

$$
f^{\prime}(\alpha) \geq \frac{1}{n}\left(\sum_{i=1}^{n} h\left(a_{i}\right)\right)\left(\sum_{i=1}^{n} \ln a_{i}\right)=0
$$

于是 $f(x)$ 在 $[3,+\infty)$ 上单调不减. 故 $f(\alpha) \geq f(3) \geq n$.

综上, 使得 $f(\alpha) \leq n$ 恒成立的整数 $\alpha$ 只有 1 , 使得 $f(\alpha) \geq n$ 恒成立的整数 $\alpha$ 为所有大于等于 3 或小于等于 -1 的整数.
评注 (1). 人大附中陈锐蹈同学对于 $\alpha \geq 4$ 时的情形给出了如下做法:

由 Hölder 不等式,

$$
\left(\sum_{i=1}^{n} \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{2}}\right)^{2}\left(\sum_{i=1}^{n} \frac{a_{i}}{1-a_{i}+a_{i}^{2}}\right)^{\alpha-3} \geq\left(\sum_{i=1}^{n} \frac{a_{i}^{3}}{1-a_{i}+a_{i}^{2}}\right)^{\alpha-1} .
$$

因此由 $f(1) \leq n, f(3) \geq n$ 即得 $f(\alpha) \geq n$.

山东省实验中学孙永喆同学对于 $\alpha \geq 4$ 时的情形给出了如下做法:

由均值不等式, 对 $1 \leq i \leq n$,

$$
2 \cdot \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{2}}+2\left(1-a_{i}+a_{i}^{2}\right)+\underbrace{1+1+\cdots+1}_{\alpha-4 \uparrow} \geq \alpha a_{i}^{2} .
$$

对 $i$ 从 1 到 $n$ 求和得,

$$
2 \sum_{i=1}^{n} \frac{a_{i}^{\alpha}}{1-a_{i}+a_{i}^{2}} \geq(\alpha-2) \sum_{i=1}^{n} a_{i}^{2}+2 \sum_{i=1}^{n} a_{i}-(\alpha-2) n .
$$

再由 $\sum_{i=1}^{n} a_{i}^{2} \geq n, \sum_{i=1}^{n} a_{i} \geq n$ 即得 $f(\alpha) \geq n$.

(2). 湖南省长沙市南雅中学黄叶, 桐乡高级中学冯屹霄, 武汉市新洲区第一中学罗云杰, 长郡中学刘楚才等同学也给出了本题的正确解答.

第二题 设 $\triangle A B C$ 的外心和内心分别为 $O$ 和 $I$. 外接圆上弧 $\widehat{B A C}$ 的中点为 $N_{1}, \angle B A C$ 所对的旁切圆在 $B C$ 上的切点为 $D_{1}$. 将 $\triangle A N_{1} D_{1}$ 的外接圆记为 $\Gamma_{1}$, 类似定义 $\Gamma_{2}, \Gamma_{3}$. 令 $P$ 为 $\Gamma_{1}, \Gamma_{2}, \Gamma_{3}$ 这三个圆的根心, 求证 $P$ 在直线 $O I$ 上.

(人大附中学生 董天诺 供题)

## 证明 (根据供题者的解答整理):

我们证明, $P$ 是 $\odot O$ 与 $\odot I$ 的外位似中心.



重新定义 $P$ 是 $\odot O$ 与 $\odot I$ 的外位似中心, 只需证明 $P$ 到 $\Gamma_{1}, \Gamma_{2}, \Gamma_{3}$ 的幂相
等.

先证明一个引理.

引理 设 $T_{A}$ 是 $A$-伪内切圆与 $\odot O$ 的切点, 类似定义点 $T_{B}, T_{C}$, 则 $A T_{A}, B T_{B}, C T_{C}$ 共点于 $P$.

证明 由 Monge 定理, $\odot O, \odot I$ 及 $A$-伪内切圆两两的外位似中心 $A, P, T_{A}$共线, 即 $A T_{A}$ 过 $P$. 同理, $B T_{B}, C T_{C}$ 均过 $P$. 引理证毕.

回到原题. 由伪内切圆的熟知结论, $N_{1}, I, T_{A}$ 共线, 设该直线与 $B C$ 交于点 $R$.



下面证明, $R$ 在 $\Gamma_{1}$ 上, 即 $A, N_{1}, D_{1}, R$ 共圆.

事实上, 设直线 $N_{1} O$ 与 $B C$ 交于点 $M_{A}$ 、与 $\widehat{B C}$ 交于点 $M_{1}$, 则 $A, I, M_{1}$ 共线. 由内心的性质及射影定理,

$$
M_{1} I^{2}=M_{1} C^{2}=M_{1} M_{A} \cdot M_{1} N_{1} \text {, }
$$

所以 $\triangle M_{1} M_{A} I \sim \triangle M_{1} I N_{1}$, 于是

$$
\angle I N_{1} A=\angle M_{1} I N_{1}-90^{\circ}=\angle M_{1} M_{A} I-90^{\circ}=\angle I M_{A} C .
$$

又熟知 $I M_{A} / / A D_{1}$, 所以

$$
\angle A N_{1} R=\angle I M_{A} R=\angle A D_{1} R,
$$

故 $A, N_{1}, D_{1}, R$ 共圆.

设 $A T_{A}$ 与 $\odot I$ 靠近 $T_{A}$ 的交点为 $K_{A}$.

下面证明, $K_{A}$ 在 $\Gamma_{1}$ 上, 即 $A, K_{A}, R, N_{1}$ 共圆.

熟知 $T_{A} D, T_{A} A$ 是 $\angle B T_{A} C$ 的等角线, 结合 $N_{1} T_{A}$ 平分 $\angle B T_{A} C$, 知 $N_{1} T_{A}$ 平



分 $\angle D T_{A} K_{A}$. 又因为 $I D=I K_{A}$, 所以 $I T_{A}$ 是线段 $D K_{A}$ 的垂直平分线. 于是

$$
\angle A N_{1} R=\angle A B T_{A}=\angle R D T_{A}=\angle R K_{A} T_{A},
$$

故 $A, K_{A}, R, N_{1}$ 共圆.



根据之前的推导, $P$ 到 $\Gamma_{1}$ 的幂为 $-P A \cdot P K_{A}$. 同理, $P$ 到 $\Gamma_{3}$ 的幂为 $-P C \cdot P K_{C}$. 因此只需证明 $P A \cdot P K_{A}=P C \cdot P K_{C}$, 即 $A, K_{C}, K_{A}, C$ 共圆.

如图, 记

$$
\angle 1=\angle C K_{A} T_{A}, \quad \angle 2=\angle K_{A} C T_{A}, \quad \angle 3=\angle A K_{C} T_{C}, \quad \angle 4=\angle K_{C} A T_{C}
$$

由 $\triangle C T_{A} A \sim \triangle D T_{A} B$, 知

$$
\frac{\sin \angle 1}{\sin \angle 2}=\frac{T_{A} C}{T_{A} K_{A}}=\frac{T_{A} C}{T_{A} D}=\frac{C A}{B D}
$$

类似地,

$$
\frac{\sin \angle 3}{\sin \angle 4}=\frac{T_{C} A}{T_{C} K_{C}}=\frac{T_{C} A}{T_{C} F}=\frac{C A}{B F}
$$

所以

$$
\frac{\sin \angle 1}{\sin \angle 2}=\frac{\sin \angle 3}{\sin \angle 4}
$$

又因为

$$
\angle 1+\angle 2=180^{\circ}-\angle K_{A} T_{A} C=180^{\circ}-\angle K_{C} T_{C} A=\angle 3+\angle 4<180^{\circ} \text {, }
$$

所以 $\angle 1=\angle 3$, 故 $A, K_{C}, K_{A}, C$ 共圆.

综上, 命题得证.

评注 成都实验外国语学校黄楚锋, 杭州学军中学郑思源、叶梓, 湖南省长沙市南雅中学石育锟、欧阳仁鼎, 南昌市第二中学魏业勋, 南宁三中高曼书, 山大附中肖行健、朱鹤延, 石家庄二中赵柳烨, 长郡中学刘楚才、刘尧瑞、王子晗、周祖毅, 人大附中陈锐蹈, 重庆市巴蜀中学陈冠霖等同学也给出了本题的正确解答.

第三题 给定正整数 $n \geq 4$. 考虑所有和为 $n$ 的非整数的正实数 $x_{1}, x_{2}, \ldots, x_{n}$. 求最优的常数 $C_{1}(n)$ 以及 $C_{2}(n)$, 使得下面不等式恒成立:

其中 $\left\{x_{i}\right\}$ 为 $x_{i}$ 的小数部分.

$$
C_{1}(n) \leq \sum_{i=1}^{n} \frac{x_{i} \cdot\left\{x_{i}\right\}}{x_{i}+1} \leq C_{2}(n)
$$

(湖南师大附中学生 夏阳 供题)

## 解 (根据供题者的解答整理):

记 $S=\sum_{i=1}^{n} \frac{x_{i} \cdot\left\{x_{i}\right\}}{x_{i}+1}$.

先求 $S$ 的下界.

对 $0<\varepsilon<1$, 取 $x_{1}=x_{2}=\cdots=x_{n-1}=\frac{1-\varepsilon}{n-1}, x_{n}=n-1+\varepsilon$. 则

$$
S=(n-1) \cdot \frac{\frac{(1-\varepsilon)^{2}}{(n-1)^{2}}}{\frac{1-\varepsilon}{n-1}+1}+\frac{(n-1+\varepsilon) \varepsilon}{n+\varepsilon} \rightarrow \frac{1}{n}(\varepsilon \rightarrow 0),
$$

所以 $C_{1}(n) \leq \frac{1}{n}$.

下面证明 $C_{1}(n)=\frac{1}{n}$ 时不等式成立.

不妨设 $x_{1} \leq x_{2} \leq \cdots \leq x_{n}$. 因为当 $x \geq 0$ 时, $x \geq\{x\}$, 又函数 $y=\frac{x}{x+1}$在 $(0,+\infty)$ 上单调递增, 所以

$$
S \geq \sum_{i=1}^{n-1} \frac{\left\{x_{i}\right\}^{2}}{\left\{x_{i}\right\}+1}+\frac{x_{n}\left\{x_{n}\right\}}{x_{n}+1} \geq \frac{\left(\sum_{i=1}^{n-1}\left\{x_{i}\right\}\right)^{2}}{\sum_{i=1}^{n-1}\left\{x_{i}\right\}+n-1}+\frac{x_{n}\left\{x_{n}\right\}}{x_{n}+1}
$$

其中最后一步用到了柯西不等式.

记 $\sum_{i=1}^{n}\left\{x_{i}\right\}=k$. 因为 $\sum_{i=1}^{n} x_{i}=n$ 是整数, 所以 $k$ 是整数, 又 $x_{i}$ 均不是整数,所以 $k$ 是正整数.

当 $k \geq 2$ 时, 由 $\left\{x_{n}\right\}<1$ 知 $\sum_{i=1}^{n-1}\left\{x_{i}\right\}>1$, 所以

$$
\frac{\left(\sum_{i=1}^{n-1}\left\{x_{i}\right\}\right)^{2}}{\sum_{i=1}^{n-1}\left\{x_{i}\right\}+n-1} \geq \frac{1}{n} \Leftrightarrow\left(n \sum_{i=1}^{n-1}\left\{x_{i}\right\}+n-1\right)\left(\sum_{i=1}^{n-1}\left\{x_{i}\right\}-1\right) \geq 0
$$

成立. 故由 $(*)$,

$$
S \geq \frac{\left(\sum_{i=1}^{n-1}\left\{x_{i}\right\}\right)^{2}}{\sum_{i=1}^{n-1}\left\{x_{i}\right\}+n-1} \geq \frac{1}{n}
$$

当 $k=1$ 时, 记 $\sum_{i=1}^{n-1}\left\{x_{i}\right\}=m$, 则 $0<m<1$ 且 $\left\{x_{n}\right\}=1-m$. 又由 $x_{n}$ 最大知 $x_{n} \geq 1$, 所以 $\left[x_{n}\right] \geq 1$, 故

$$
x_{n}=\left[x_{n}\right]+\left\{x_{n}\right\} \geq 2-m
$$

从而由 $(*)$,

$$
S \geq \frac{m^{2}}{m+n-1}+\frac{(2-m)(1-m)}{3-m}
$$

而

$$
\begin{aligned}
& \frac{m^{2}}{m+n-1}+\frac{(2-m)(1-m)}{3-m} \geq \frac{1}{n} \\
\Leftrightarrow & m^{2}(3-m) n+(m+n-1)\left(m^{2}-3 m+2\right) n \geq(m+n-1)(3-m) \\
\Leftrightarrow & \left(n^{2}-n+1\right) m^{2}-\left(3 n^{2}-6 n+4\right) m+\left(2 n^{2}-5 n+3\right) \geq 0 .
\end{aligned}
$$

记函数

$$
g(x)=\left(n^{2}-n+1\right) x^{2}-\left(3 n^{2}-6 n+4\right) x+\left(2 n^{2}-5 n+3\right),
$$

由 $n \geq 4$, 知其对称轴

$$
\frac{3 n^{2}-6 n+4}{2\left(n^{2}-n+1\right)} \geq 1
$$

所以 $g(x)$ 在 $[0,1]$ 上单调递减, 于是

$$
g(m) \geq g(1)=\left(n^{2}-n+1\right)-\left(3 n^{2}-6 n+4\right)+\left(2 n^{2}-5 n+3\right)=0
$$

成立.

综上, $C_{1}(n)$ 的最优值为 $\frac{1}{n}$.
再求 $S$ 的上界.

对 $0<\varepsilon<\frac{1}{n-1}$, 取 $x_{1}=(n-1) \varepsilon, x_{2}=\cdots=x_{n-1}=1-\varepsilon, x_{n}=2-\varepsilon$. 则

$S=\frac{(n-1)^{2} \varepsilon^{2}}{(n-1) \varepsilon+1}+\frac{(n-2)(1-\varepsilon)^{2}}{2-\varepsilon}+\frac{(2-\varepsilon)(1-\varepsilon)}{3-\varepsilon} \rightarrow \frac{3 n-2}{6}(\varepsilon \rightarrow 0)$,

所以 $C_{2}(n) \geq \frac{3 n-2}{6}$.

下面证明 $C_{2}(n)=\frac{3 n-2}{6}$ 时不等式成立.

不妨设 $x_{1} \leq x_{2} \leq \cdots \leq x_{t}<1 \leq x_{t+1} \leq \cdots \leq x_{n}$. 注意到当 $x \in[a, a+1)$,其中 $a \in \mathbb{N}$ 时，

$$
\frac{\{x\}}{x+1}=\frac{x-a}{x+1}<\frac{1}{a+2}
$$

所以

$$
\begin{aligned}
S & =\sum_{i=1}^{t} \frac{x_{i}\left\{x_{i}\right\}}{x_{i}+1}+\sum_{j=t+1}^{n} \frac{x_{j}\left\{x_{j}\right\}}{x_{j}+1}<\frac{1}{2} \sum_{i=1}^{t} x_{i}+\frac{1}{3} \sum_{j=t+1}^{n} x_{j} \\
& =\frac{1}{2} \sum_{i=1}^{t} x_{i}+\frac{1}{3}\left(n-\sum_{i=1}^{t} x_{i}\right)=\frac{n}{3}+\frac{1}{6} \sum_{i=1}^{t} x_{i} .
\end{aligned}
$$

当 $\sum_{i=1}^{t} x_{i} \leq n-2$ 时,

$$
S<\frac{n}{3}+\frac{1}{6}(n-2)=\frac{3 n-2}{6} .
$$

当 $\sum_{i=1}^{t} x_{i}>n-2$ 时, $t=n-1$, 所以 $x_{n} \in(1,2)$, 此时

$$
S=\sum_{i=1}^{n-1} \frac{x_{i}^{2}}{x_{i}+1}+\frac{x_{n}\left(x_{n}-1\right)}{x_{n}+1}
$$

因为

$$
\left(x_{n-1}, x_{n-2}, \cdots, x_{2}, x_{1}\right) \prec(\underbrace{1,1, \cdots, 1}_{n-2 \text { 个 }}, 2-x_{n}),
$$

且易知 $y=\frac{x^{2}}{x+1}$ 在 $(0,+\infty)$ 上是下凸函数, 所以由 Karamata 不等式,

$$
\sum_{i=1}^{n-1} \frac{x_{i}^{2}}{x_{i}+1} \leq \frac{n-2}{2}+\frac{\left(2-x_{n}\right)^{2}}{3-x_{n}}
$$

于是只需证明

$$
\frac{\left(2-x_{n}\right)^{2}}{3-x_{n}}+\frac{x_{n}\left(x_{n}-1\right)}{x_{n}+1} \leq \frac{2}{3}
$$

化简知, 这等价于

$$
5 x_{n}^{2}-13 x_{n}+6 \leq 0
$$

即 $\frac{3}{5} \leq x_{n} \leq 2$, 由 $1<x_{n}<2$ 即证.

综上, $C_{2}(n)$ 的最优值为 $\frac{3 n-2}{6}$.
评注 安师大附中胡越洋, 人大附中陈锐韫, 武汉市新洲区第一中学罗云杰,长郡中学刘楚才等同学也给出了本题的正确解答.

第四题 正整数 $x_{1} \leq x_{2} \leq \cdots \leq x_{27}$ 满足这些数没有大于 1 的公因子, 且每个 $x_{i}$ 均整除它们的和. 若 $x_{27}$ 是一个素数, 求这个素数的所有可能值.

(吉林大学 苏㖓航 供题)

## 解 (根据供题者的解答整理):

先注意到对任意的素数 $p \leq 26$, 都有一组满足题意的正整数, 使得 $x_{27}=p$.事实上, 令

$$
x_{i}=\left\{\begin{array}{l}
1, i \in\{1,2, \cdots, p\} \\
p, i \in\{p+1, p+2, \cdots, 27\}
\end{array}\right.
$$

即可.

下面证明一个引理.

引理 对于正整数 $a \leq b$, 区间 $\left[b,(b-a+2) \cdot 2^{a}-2\right]$ 中的每个正奇数 $c$ 都可以表示为 $\sum_{i=1}^{b} 2^{a_{i}}$ 的形式, 其中 $a_{1}, a_{2}, \cdots, a_{b}$ 是不超过 $a$ 的非负整数.

证明 首先, 归纳证明区间 $\left[b,(b-a+1) \cdot 2^{a}-1\right]$ 中的每个正整数 $c$ 都可以表示为引理中的形式.

当 $c=b$ 时, 可取所有的 $a_{i}$ 都是 0 .

假设 $c \leq(b-a+1) \cdot 2^{a}-2$ 且 $c$ 时结论成立, 设 $c=\sum_{i=1}^{b} 2^{a_{i}}$, 其中 $a_{1}, a_{2}, \cdots, a_{b}$是不超过 $a$ 的非负整数. 注意到至多有 $b-a$ 个 $a_{i}$ 等于 $a$, 所以至少有 $a$ 个 $a_{i}$ 小于 $a$. 若小于 $a$ 的 $a_{i}$ 互不相同, 则恰有 $a$ 个 $a_{i}$ 小于 $a$, 且 $0,1, \cdots, a-1$ 各一个.这样,

$$
\sum_{i=1}^{b} 2^{a_{i}}=(b-a) \cdot 2^{a}+\left(2^{0}+2^{1}+\cdots+2^{a-1}\right)=(b-a+1) \cdot 2^{a}-1,
$$

与 $c \leq(b-a+1) \cdot 2^{a}-2$ 矛盾! 因此存在下标 $i_{1}$ 和 $i_{2}$, 使得 $a_{i_{1}}=a_{i_{2}}=d$, 其中 $0 \leq d<a$. 记 $a_{i_{1}}^{\prime}=d+1, a_{i_{2}}^{\prime}=0$, 其余 $a_{i}^{\prime}=a_{i}$, 则所有 $a_{i}^{\prime}$ 都是不超过 $a$ 的非负整数, 且 $c+1=\sum_{i=1}^{b} 2^{a_{i}^{\prime}}$.

归纳证毕.

其次, 当 $(b-a+1) \cdot 2^{a} \leq c \leq(b-a+2) \cdot 2^{a}-2$ 时, 记

$$
c^{\prime}=c-(b-a+1) \cdot 2^{a}+1,
$$

则 $1 \leq c^{\prime} \leq 2^{a}-1$. 由 $c$ 是奇数, 知 $c^{\prime}$ 是偶数, 所以 $c^{\prime}$ 可以表示为 $\sum_{i=1}^{a-1} s_{i} \cdot 2^{i}$ 的形
式, 其中 $s_{i} \in\{0,1\}$. 此时, 取

$$
a_{i}= \begin{cases}0, & i=1 \\ i-1+s_{i-1}, & i \in\{2,3, \cdots, a\} \\ a, & i \in\{a+1, a+2, \cdots, b\}\end{cases}
$$

则所有 $a_{i}$ 都是不超过 $a$ 的非负整数. 又注意到总有

$$
s_{i} \cdot 2^{i}=2^{i+s_{i}}-2^{i}
$$

所以

$$
\begin{aligned}
\sum_{i=1}^{b} 2^{a_{i}} & =2^{0}+\sum_{i=1}^{a-1} 2^{i+s_{i}}+(b-a) \cdot 2^{a} \\
& =1+\sum_{i=1}^{a-1}\left(s_{i} \cdot 2^{i}+2^{i}\right)+(b-a) \cdot 2^{a} \\
& =1+\sum_{i=1}^{a-1} s_{i} \cdot 2^{i}+\left(2^{a}-2\right)+(b-a) \cdot 2^{a} \\
& =c^{\prime}+(b-a+1) \cdot 2^{a}-1=c
\end{aligned}
$$

引理证毕.

对素数 $27 \leq p \leq 157$, 对 $a=4, b=12$ 应用引理 1 , 因为 $(b-a+2) \cdot 2^{a}-2=$ 158 , 所以我们可以把 $p$ 写成 12 个不超过 2 的 4 次幂之和. 此时把这 12 项按照单调不减的顺序记为 $x_{1}$ 到 $x_{12}$, 再令 $x_{13}=x_{14}=\cdots=x_{27}=p$, 容易验证 $x_{1}, x_{2}, \cdots, x_{27}$ 满足题意.

接下来证明, 若素数 $p>183$, 则一定不存在满足题意的正整数组, 使得 $x_{27}=p$.

假设存在, 因为 $x_{27} \mid \sum_{i=1}^{27} x_{i}$, 所以可设 $\sum_{i=1}^{27} x_{i}=k p$, 其中 $k$ 是正整数. 因此对任意的 $1 \leq i \leq 27$, 都有 $x_{i} \mid k p$. 设 $i_{0}$ 是最小的使得 $x_{i}=p$ 的下标, 因为 $x_{1}, x_{2}, \cdots, x_{27}$ 没有大于 1 的公因子, 所以 $i_{0} \geq 2$. 因为

$$
\sum_{i=1}^{27} x_{i}>\sum_{i=i_{0}}^{27} x_{i}=\left(28-i_{0}\right) p
$$

所以 $k \geq 29-i_{0}$.

下面分两种情形讨论.

情形 $1: k=29-i_{0}$. 此时

$$
\sum_{i=1}^{i_{0}-1} x_{i}=\left(29-i_{0}\right) p-\left(28-i_{0}\right) p=p
$$

因为对 $1 \leq i \leq i_{0}-1, x_{i}<p$, 而 $x_{i} \mid k p$, 所以 $x_{i} \mid k$.

若 $x_{1}, x_{2}<k$, 则 $x_{1}, x_{2} \leq \frac{k}{2}$, 所以 $\sum_{i=1}^{i_{0}-1} x_{i} \leq\left(i_{0}-2\right) k$.

若对 $2 \leq i \leq i_{0}-1$, 都有 $x_{i}=k$, 则对这些 $i, x_{1} \mid x_{i}$. 又 $\sum_{i=1}^{i_{0}-1} x_{i}=p$, 所以 $x_{1} \mid p$. 于是 $x_{1}=1$, 进而 $\sum_{i=1}^{i_{0}-1} x_{i} \leq\left(i_{0}-2\right) k+1$.

从而总有

$$
p=\sum_{i=1}^{i_{0}-1} x_{i} \leq\left(i_{0}-2\right) k+1=(27-k) k+1 \leq 13 \times 14+1=183,
$$

矛盾!

情形 $2: k \geq 30-i_{0}$. 此时对 $1 \leq i \leq i_{0}-1$, 仍有 $x_{i} \leq k$. 因为

$$
\sum_{i=1}^{i_{0}-1} x_{i}=k p-\left(28-i_{0}\right) p=\left(k+i_{0}-28\right) p
$$

所以

$$
\left(k+i_{0}-28\right) p \leq\left(i_{0}-1\right) k .
$$

因此

$$
\begin{aligned}
p \leq \frac{\left(i_{0}-1\right) k}{k+i_{0}-28} & =i_{0}-1+\frac{\left(i_{0}-1\right)\left(28-i_{0}\right)}{k+i_{0}-28} \\
& \leq i_{0}-1+\frac{\left(i_{0}-1\right)\left(28-i_{0}\right)}{2} \\
& \leq 26+\frac{27^{2}}{8}<118,
\end{aligned}
$$

矛盾!

最后, 只需要再讨论 $p=163,167,173,179,181$ 的情形.

对 $p=163$, 令

$$
x_{i}= \begin{cases}1, & i=1 \\ 9, & i \in\{2,3, \cdots, 19\} \\ 163, & i \in\{20,21, \cdots, 27\}\end{cases}
$$

对 $p=167$, 令

$$
x_{i}=\left\{\begin{array}{ll}
2, & i=1 \\
5, & i=2 \\
10, & i \in\{3,4, \cdots, 18\} \\
167, & i \in\{19,20, \cdots, 27\}
\end{array} ;\right.
$$

对 $p=173$, 令

$$
x_{i}=\left\{\begin{array}{ll}
2, & i=1 \\
3, & i=2 \\
12, & i \in\{3,4, \cdots, 16\} \\
173, & i \in\{17,18, \cdots, 27\}
\end{array} ;\right.
$$

对 $p=181$, 令

$$
x_{i}= \begin{cases}1, & i=1 \\ 12, & i \in\{2,3, \cdots, 16\} \\ 181, & i \in\{17,18, \cdots, 27\}\end{cases}
$$

容易验证满足题意.

最后证明, 对 $p=179$, 不存在满足题意的正整数组.

事实上, 如果存在, 则由之前的讨论, 存在 $2 \leq i_{0} \leq 27$, 使得

$$
179\left(k+i_{0}-28\right) \leq\left(i_{0}-1\right) k .
$$

由 $(*)$, 当 $k \geq 30-i_{0}$ 时不存在这样的 $i_{0}$, 因此 $k=29-i_{0}$.

此时, $179 \leq\left(i_{0}-1\right)\left(29-i_{0}\right)$, 解得 $11 \leq i_{0} \leq 19$.

对给定的 $i_{0}$, 当且仅当有 $i_{0}-1$ 个 $29-i_{0}$ 的因子使得它们的和为 179 时有这样的正整数组. 然而当我们检验了 $11 \sim 19$ 后, 并没有发现满足上述要求的 $i_{0}$.

综上, 若将素数从小到大排列为 $p_{1}, p_{2}, \cdots$, 则本题的答案为 $p_{1}, p_{2}, \cdots, p_{40}$以及 $p_{42}$.

评注 (1). 对于 $27 \leq p \leq 173$ 及 $p=181$ 的情形, 湖南省长沙市南雅中学朱凯峰和石育锟同学采用了统一的构造方式: 令 $x_{1}, x_{2}, \cdots, x_{13}$ 中有 $a$ 个 $1 、 b$ 个 3、c个 $5 、 d$ 个 15 , 其中 $a, b, c, d$ 是非负整数, 且满足

$$
\left\{\begin{array}{l}
a+b+c+d=13 \\
a+3 b+5 c+15 d=p
\end{array}\right.
$$

再令 $x_{14}=x_{15}=\cdots=x_{27}=p$. 细节读者可自行补全.

(2). 巴蜀中学罗登尧、翟霄宇, 杭州学军中学郑思源, 人大附中陈锐㭏舀, 长郡中学刘楚才等同学也给出了本题的正确解答.

