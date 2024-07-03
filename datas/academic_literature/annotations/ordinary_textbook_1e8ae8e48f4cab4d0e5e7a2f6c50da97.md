# 数学新星问题征解第七期解答 

2015.07

第一题: 圆内接四边形 $A B C D$ 中存在一点 $P$, 使得 $\angle P A B=\angle P B C=$ $\angle P C D=\angle P D A$, 证明: $A B \cdot C D=B C \cdot D A$.

(郑州外国语学校学生 朱书聪 供题)

## 解法一 (根据浙江省象山县第三中学黄子宸同学的解答整理):

如图, 作 $\triangle A P B$ 外接圆 $\odot A P B$ 交 $B D$于 $Q$, 连接 $Q P, Q A, Q C, A C$.

由 $\angle P A B=\angle P B C$ 知, $\odot A P B$ 与 $B C$ 相切于 $B$ 点, 于是

$$
\angle Q A B=\angle Q B C=\angle D B C=\angle D A C \text {, }
$$

且

$$
\angle P Q D=\angle P A B=\angle P C D .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_abcaf3e94be94f8a45dag-1.jpg?height=537&width=517&top_left_y=988&top_left_x=1272)

因此 $P, Q, C, D$ 四点共圆, 且由 $\angle P D A=\angle P C D$ 知 $\odot P Q C D$

与 $A D$ 相切于 $D$ 点. 所以

$$
\angle Q C D=\angle Q D A=\angle B D A=\angle B C A,
$$

从而

$$
\angle B C Q=\angle A C D=\angle A B D=\angle A B Q
$$

故

$$
\triangle A D C \backsim \triangle A Q B \backsim \triangle B Q C,
$$

因而有

$$
\triangle D Q C \backsim \triangle A Q D \backsim \triangle A B C .
$$

于是

$$
\frac{A Q}{Q D}=\frac{D Q}{Q C}, \frac{A Q}{Q B}=\frac{B Q}{Q C},
$$

从而得 $Q D=Q B$, 故

$$
\frac{A D}{D C}=\frac{A Q}{Q B}=\frac{A Q}{Q D}=\frac{A B}{B C},
$$

因此 $A B \cdot C D=B C \cdot D A$.

## 解法二 (根据江苏省无锡市第一中学高诚同学的解答整理):

先证明下面引理:

引理: 已知 $\triangle A B C$ 与 $\triangle A^{\prime} B^{\prime} C^{\prime}$, 其中 $\angle B=\angle B^{\prime}, \angle A+\angle A^{\prime}=180^{\circ}$, 则

$$
B C \cdot B^{\prime} C^{\prime}=A C \cdot A^{\prime} C^{\prime}+A B \cdot A^{\prime} B^{\prime} .
$$

证明 过点 $C$ 作 $A B$ 的平行线, 在 $A$ 关于 $B C$ 的另一侧取点 $D$, 使得 $\angle B D C+\angle B A C=180^{\circ}$, 连结 $A D$. 于是 $\angle B C D=\angle A B C=\angle B^{\prime}, \angle B D C=$ $\angle A^{\prime}$, 从而 $\triangle A^{\prime} B^{\prime} C^{\prime} \sim \triangle D C B$. 因此 $\frac{D C}{A^{\prime} B^{\prime}}=\frac{D B}{A^{\prime} C^{\prime}}=\frac{C B}{B^{\prime} C^{\prime}}$, 从而所证即为

$$
B C^{2}=A C \cdot B D+A B \cdot D C .
$$

由 $\angle B D C+\angle B A C=180^{\circ}$ 得 $A, B, C, D$ 四点共圆, 则由托勒密定理, 得

$$
A B \cdot C D+B D \cdot A C=A D \cdot B C .
$$

故只须证 $A D=B C$. 因为 $\angle B C D=\angle A B C$, 所以弧 $\widehat{B D}=\widehat{A C}$, 从而 $A C=B D$.因此四边形 $A B C D$ 为等腰梯形, 故 $A D=B C$. 引理得证.

回到原题, 易知

$$
\begin{aligned}
& \angle A P B=180^{\circ}-\angle P A B-\angle P B A=180^{\circ}-\angle A B C=\angle A D C . \\
& \angle C P D=180^{\circ}-\angle P C D-\angle P D C=180^{\circ}-\angle C D A=\angle A B C .
\end{aligned}
$$

因此 $\angle A P B+\angle C P D=\angle A D C+\angle A B C=180^{\circ}$. 又 $\angle P A B=\angle P C D$, 从而由引理, 在 $\triangle A B P$ 与 $\triangle C D P$ 中,

$$
A B \cdot C D=P A \cdot P C+P B \cdot P D \text {. }
$$

同理, 在 $\triangle B C P$ 与 $\triangle A P D$ 中, 有 $\angle P D A=\angle P B C, \angle A P D+\angle B P C=180^{\circ}$, 从而由引理, 有

$$
B C \cdot A D=P A \cdot P C+P B \cdot P D \text {. }
$$

故而 $A B \cdot C D=B C \cdot D A$.

## 解法三 (根据东北师大附中孙伟舰、河北唐山一中兰添等同学的解答整理):

延长 $A P$ 交 $B C$ (延长线) 于 $T$, 连结 $D T$.

由已知条件 $\angle P A B=\angle P B C=\angle P C D=\angle P D A$, 易得

$$
\angle A P B=\angle A D C, \quad \angle C P D=\angle A B C, \angle A P D=\angle B C D, \quad \angle B P C=\angle B A D .
$$

从而 $\angle A P D+\angle B P C=180^{\circ}, \angle A P B+\angle C P D=180^{\circ}$. 由正弦定理,

$$
\frac{A P}{A D}=\frac{\sin \angle A D P}{\sin \angle A P D}=\frac{\sin \angle C B P}{\sin \angle B P C}=\frac{C P}{B C} .
$$

故 $B C=\frac{A D \cdot C P}{A P}$.

又 $\angle A B T=\angle C P D, \angle B A T=\angle P C D$, 因此 $\triangle A B T \sim \triangle C P D$. 从而

$$
\frac{A B}{A T}=\frac{C P}{C D}, \quad \angle A T B=\angle C D P .
$$

若 $T$ 在线段 $B C$ 上, 有 $\angle P T C+\angle C D P=180^{\circ}$; 若 $T$ 在线段 $B C$ 的延长线上, 则有 $\angle A T C=\angle C D P$. 因此 $C, T, P, D$ 四点共圆. 于是 $\angle D T P=\angle D C P=\angle A D P$.从而 $\triangle A D P \backsim \triangle A T D$. 所以 $A D^{2}=A P \cdot A T$. 故

$$
A B \cdot C D=C P \cdot A T=C P \cdot \frac{A D^{2}}{A P}=A D \cdot \frac{A D \cdot C P}{A P}=A D \cdot B C .
$$

## 解法四 (根据北师大二附中李泽宇同学的解答整理):

我们首先证明如下引理:

引理: 以 $\odot O$ 为单位圆建立复平面, 已知单位圆上一点 $A$ 以及非圆上一点 $B$,直线 $A B$ 交圆另一点为 $A^{\prime}$. 记点 $A, B, A^{\prime}$ 的坐标为 $\mathbf{a}, \mathbf{b}, \mathbf{a}^{\prime}$, 则

$$
\mathbf{a}^{\prime}=\frac{\mathbf{a}-\mathbf{b}}{\mathbf{a} \bar{b}-1}
$$

这是因为

$$
\frac{\mathbf{a}-\mathbf{b}}{\mathbf{a}^{\prime}-\mathbf{a}}=\frac{\overline{\mathbf{a}}-\overline{\mathbf{b}}}{\overline{\mathbf{a}^{\prime}}-\overline{\mathbf{a}}}
$$

所以有 $\mathbf{a}-\mathbf{b}+\mathbf{a} \mathbf{a}^{\prime}(\overline{\mathbf{a}}-\overline{\mathbf{b}})=\mathbf{0}$. 从而引理得证.

回到原题, 设四边形 $A B C D$ 是单位圆 $\odot O$ 的内接四边形. 以 $\odot O$ 为单位圆建立复平面, 设点 $P$ 落在实轴上. 则由引理, 知

$$
\mathbf{a}^{\prime}=\frac{\mathrm{a}-\mathbf{p}}{\mathrm{ap}-1}, \quad \mathrm{~b}^{\prime}=\frac{\mathrm{b}-\mathbf{p}}{\mathrm{bp}-\mathbf{1}}, \quad \mathbf{c}^{\prime}=\frac{\mathbf{c}-\mathbf{p}}{\mathbf{c p}-\mathbf{1}}, \quad \mathrm{d}^{\prime}=\frac{\mathbf{d}-\mathbf{p}}{\mathrm{dp}-\mathbf{1}} .
$$

由 $\angle P A B=\angle P B C=\angle P C D=\angle P D A$ 知,

$$
\left|A^{\prime} B\right|=\left|B^{\prime} C\right|=\left|C^{\prime} D\right|=\left|D^{\prime} A\right|,
$$

即

$$
\frac{a-p}{(a p-1) b}=\frac{b-p}{(b p-1) c}=\frac{c-p}{(c p-1) d}=\frac{d-p}{(d p-1) a} .
$$

我们要证 $A B \cdot C D=B C \cdot D A$, 则证 $|\mathbf{a}-\mathbf{b}| \cdot|\mathbf{c}-\mathbf{d}|=|\mathbf{b}-\mathbf{c}| \cdot|\mathbf{d}-\mathbf{a}|$, 即

$$
(\mathbf{a}-\mathbf{b})(\mathbf{c}-\mathbf{d})= \pm(\mathbf{b}-\mathbf{c})(\mathbf{d}-\mathbf{a}) .
$$

而

$$
\mathbf{a d}+\mathbf{b c}-\mathbf{a b}-\mathbf{c d}=(\mathbf{c}-\mathbf{a})(\mathbf{b}-\mathbf{d}) \neq \mathbf{0}
$$

故只需证

$$
2(\mathrm{ac}+\mathrm{bd})=(\mathrm{a}+\mathbf{c})(\mathrm{b}+\mathbf{d})
$$

由 (1) 式可得

$$
\begin{aligned}
& \frac{(\mathbf{a}-\mathbf{b}) \mathrm{d}}{\mathrm{bd}(\mathbf{a}-\mathbf{c}) \mathrm{p}-(\mathbf{b}-\mathbf{c}) \mathrm{d}}=\frac{(\mathrm{b}-\mathbf{c}) \mathbf{a}}{\mathrm{ac}(\mathbf{b}-\mathbf{d}) \mathrm{p}-(\mathbf{c}-\mathbf{d}) \mathrm{a}} \\
= & \frac{(\mathbf{c}-\mathbf{d}) \mathbf{b}}{\mathrm{bd}(\mathbf{c}-\mathbf{a}) \mathrm{p}-(\mathbf{d}-\mathbf{a}) \mathrm{b}}=\frac{(\mathbf{d}-\mathbf{a}) \mathbf{c}}{\mathrm{ac}(\mathbf{d}-\mathbf{b}) \mathbf{p}-(\mathbf{a}-\mathbf{b}) \mathbf{c}}
\end{aligned}
$$

因此

$$
\frac{(\mathbf{a}-\mathbf{b}) \mathbf{d}+(\mathbf{c}-\mathbf{d}) \mathbf{b}}{(\mathbf{b}-\mathbf{c}) \mathbf{d}+(\mathbf{d}-\mathbf{a}) \mathbf{b}}=\frac{(\mathbf{b}-\mathbf{c}) \mathbf{a}+(\mathbf{d}-\mathbf{a}) \mathbf{c}}{(\mathbf{c}-\mathbf{d}) \mathbf{a}+(\mathbf{a}-\mathbf{b}) \mathbf{c}}
$$

从而

$$
\frac{(\mathbf{a}-\mathrm{c})(\mathrm{d}-\mathrm{b})}{2 \mathrm{bd}-\mathrm{ab}-\mathrm{cd}}=\frac{(\mathrm{a}-\mathrm{c})(\mathrm{b}-\mathrm{d})}{2 \mathrm{ac}-\mathrm{ad}-\mathrm{bc}}
$$

故 (2) 式成立.

评注: 本题的问题来源是 R.A. 约翰逊著, 单墫译的《近代欧氏几何学》 $\S 504$中的一个定理: 若圆内接四边形 $A B C D$ 满足 $A B \cdot C D=B C \cdot D A$, 则存在一点 $P$与一点 $Q$, 使得

$$
\begin{aligned}
& \angle P A B=\angle P B C=\angle P C D=\angle P D A, \\
& \angle Q B A=\angle Q C B=\angle Q D C=\angle Q A D .
\end{aligned}
$$

第一题是该命题的逆命题.

第二题: 设正实数 $x, y, z, w$ 满足 $\max \{x, y, z, w\} \leq \sqrt{5} \min \{x, y, z, w\}$. 证明:

$$
\frac{x y}{5 x^{2}-y^{2}}+\frac{y z}{5 y^{2}-z^{2}}+\frac{z w}{5 z^{2}-w^{2}}+\frac{w x}{5 w^{2}-x^{2}} \geq 1
$$

(浙江省富阳中学学生 黄昊中 供题)

## 证明 (根据河北唐山一中兰添同学的解答整理):

我们先证明如下引理:

引理: 设函数 $f(x)=\frac{1}{5 x-\frac{1}{x}}$, 则当 $x, y>\frac{1}{\sqrt{5}}$ 时, 有

$$
f(x)+f(y) \geq 2 f(\sqrt{x y}) .
$$

将函数 $f(x)$ 代入上式, 即证

$$
\frac{1}{5 x-\frac{1}{x}}+\frac{1}{5 y-\frac{1}{y}} \geq 2 \frac{1}{5 \sqrt{x y}-\frac{1}{\sqrt{x y}}} .
$$

由均值不等式, 得

$$
\text { 上式左边 } \geq 2 \frac{1}{\sqrt{\left(5 x-\frac{1}{x}\right)\left(5 y-\frac{1}{y}\right)}},
$$

故只需证明

$$
\frac{1}{\sqrt{\left(5 x-\frac{1}{x}\right)\left(5 y-\frac{1}{y}\right)}} \geq \frac{1}{5 \sqrt{x y}-\frac{1}{\sqrt{x y}}}
$$

化简, 得 $\frac{y}{x}+\frac{x}{y} \geq 2$. 由均值不等式, 上式显然成立. 于是引理得证.

回到原题. 令 $a=\frac{x}{y}, b=\frac{y}{z}, c=\frac{z}{w}, d=\frac{w}{x}$, 则 $a b c d=1$, 且 $a, b, c, d>\frac{1}{\sqrt{5}}$. 因此所证不等式等价于

$$
f(a)+f(b)+f(c)+f(d) \geq 1
$$

由引理, 得

$$
\begin{aligned}
& f(a)+f(b)+f(c)+f(d) \\
& \geq 2(f(\sqrt{a b})+f(\sqrt{c d})) \\
& \geq 2 \cdot 2 f(\sqrt[4]{a b c d}) \\
& =4 f(1)=1
\end{aligned}
$$

评注: 人大附中杨泓梀同学、东北师大附中孙伟舰和李政铎同学也给出了本题的正确解答.

第三题: 在一个连通二部图中, 点 $A_{1}, A_{2}, \cdots, A_{n}$ 与点 $B_{1}, B_{2}, \cdots, B_{m}$ 相连.设点 $A_{1}, A_{2}, \cdots, A_{n}$ 的度数分别为 $a_{1}, a_{2}, \cdots, a_{n}$, 点 $B_{1}, B_{2}, \cdots, B_{m}$ 的度数分别为 $b_{1}, b_{2}, \cdots, b_{m}$, 且每个点都放有一定数量的糖果. 每次操作, 若某点的糖果数大于等于其度数, 则将该点的糖果分给与它相邻的点各一个. 证明: 若糖果总数为 $\left(a_{1}+a_{2}+\cdots+a_{n}-1\right)$ 个, 则不论初始状态如何, 只能进行有限次操作.

(辽宁实验中学学生 苏海舰 供题)

## 证明 (根据湖南省雅礼中学贺嘉帆同学的解答整理):

首先证明 $A_{1}, A_{2}, \cdots, A_{n}$ 与 $B_{1}, B_{2}, \cdots, B_{m}$ 不能都进行过操作.
反之, 若 $A_{1}, A_{2}, \cdots, A_{n}$ 与 $B_{1}, B_{2}, \cdots, B_{m}$ 均进行过操作, 则考虑这 $n+m$ 个点最后进行操作的时刻, 从最早到最晚的时刻依次记为 $t_{1}, t_{2}, \cdots, t_{m+n}$.

对于 $A_{i}$ 或 $B_{i}$, 若有 $s$ 个与其相邻的点在其进行最后一次操作后进行了操作,则其至少有 $s$ 颗糖果.

记 $C=\left\{A_{1}, \cdots, A_{n}, B_{1}, \cdots, B_{m}\right\}, E$ 为边集. 故糖果总数 $=\sum_{x \in C} x$ 最后糖果数

$$
\begin{aligned}
& \geq \sum_{x \in C} \sum_{y \in \tau} 1=\sum_{(x, y) \in \tau^{\prime}} 1 \\
& =\sum_{z \in E, \text { 且 } z \text { 连接 } x, y} 1=|E| .
\end{aligned}
$$

其中 $\tau=\{y: y$ 与 $x$ 相邻, 且 $y$ 最后一次操作在 $x$ 最后一次操作之后 $\}, \tau^{\prime}=$ $\{(x, y):(x, y)$ 相邻, 且 $y$ 最后一次操作在 $x$ 最后一次操作之后 $\}$.

事实上, 任何一条边连接了两点 $x_{1}, x_{2}, x_{1}, x_{2}$ 中必恰有一点最后一次操作比另一点晚一些. 则对于一条边, 上面和式中考虑了两次, 一次为 $\left(x_{1}, x_{2}\right)$, 一次为 $\left(x_{2}, x_{1}\right)$, 其中恰有一种被算入.

又因为 $G$ 是二部图, 则有 $a_{1}+\cdots+a_{n}=b_{1}+\cdots+b_{m}$. 故

$$
\begin{aligned}
|E| & =\frac{1}{2}\left(a_{1}+\cdots+a_{n}+b_{1}+\cdots+b_{m}\right) \\
& =a_{1}+\cdots+a_{n} .
\end{aligned}
$$

矛盾! 故 $A_{1}, A_{2}, \cdots, A_{n}$ 与 $B_{1}, B_{2}, \cdots, B_{m}$ 不能都进行过操作.

下面证明只能进行有限次操作.

反之, 假设可以无限进行下去, 则事实上, 糖果只有有限种分布情形, 故由抽屉原理, 必存在两种情形使其糖果分布相同, 即经过有限次操作之后, 糖果分布不变, 则此时不可能有点未操作. 这是因为若点 $x$ 未操作, 又 $x$ 处糖果不变, 则 $x$ 邻点处都未操作, 又由连通性, 此时 $G$ 中所有点都未操作, 矛盾! 而这根据前面的讨论, 得到矛盾!

评注: 武钢三中陈泽坤同学、东北师大附中张湛唯同学也给出了本题的解答.

第四题: 设 $\pi_{1}, \pi_{2}, \cdots, \pi_{n !}$ 为 $\{1,2, \cdots, n\}$ 的全体排列, 并且 $\pi_{1}=(1,2, \cdots, n)$, $\pi_{n !}=(n, n-1, \cdots, 1)$. 对于图 $G(V, E): V=\left\{v_{1}, v_{2}, \cdots, v_{n !}\right\}, v_{i}$ 和 $v_{j}$ 相邻当且仅
当 $\pi_{i}, \pi_{j}$ 两个排列仅有两位不同. 试问: 至少删去多少个 $G$ 的顶点, 才能使得 $v_{1}, v_{n}$ !在图 $G$ 中不连通.

(上海中学学生 陆一平, 武钢三中学生 陈泽坤 供题)

## 解 (根据河北唐山一中兰添同学的解答整理):

至少删去 $\mathrm{C}_{n}^{2}$ 个 $G$ 的顶点, 才能使得 $v_{1}, v_{n !}$ 在图 $G$ 中不连通.

一方面, $v_{1}$ 与 $\mathrm{C}_{n}^{2}$ 个顶点相邻, 删去这些邻点, 可使 $v_{1}, v_{n}$ 在图 $G$ 中不连通;另一方面, 只需构造 $\mathrm{C}_{n}^{2}$ 条不相交的从 $v_{1}$ 到 $v_{n}$ 的链即可.

记 $v_{1}$ 与其邻点对应的排列不同的两项为 $a, b(a<b, a, b \in\{1,2, \cdots, n\})$. 下面我们来构造链.

(1) 当 $a+b=n+1$ 时,

依次交换排列 $\pi_{1}$ 中的 $(a, b),(a+1, b-1), \cdots,(m, n+1-m),(1, n),(2, n-$ $1), \cdots,(a-1, b+1)$. 每次交换两项, 直到得到 $\pi_{n !}$. 这样就形成一条从 $v_{1}$ 到 $v_{n !}$ 的链. 其中

$$
m= \begin{cases}\frac{n-1}{2}, & \text { 当 } n \text { 为奇数, } \\ \frac{n}{2}, & \text { 当 } n \text { 为偶数. }\end{cases}
$$

取遍 $a<b \in\{1,2, \cdots, n\}$, 即得到 $\mathrm{C}_{n}^{2}$ 条链. 每一条链都由位置 $a, b$ 唯一确定, 故而这 $\mathrm{C}_{n}^{2}$ 条链两两不交.

(2) 当 $a+b \neq n+1$ 时,

先交换 $(a, b)$, 得排列 $\pi_{1^{\prime}}$, 然后依次交换排列 $\pi_{1^{\prime}}$ 中的 $(1, n),(2, n-$ $1), \cdots,(m, n+1-m)$, 最后再交换 $(a, b)$, 即得到一条从 $v_{1}$ 到 $v_{n}$ ! 的链. 其中 $m$ 同情形 (1) 中定义. 每一条链对应的 $a, b$ 的位置都不同, 故每条链中都不存在公共边, 因此这 $\mathrm{C}_{n}^{2}$ 条链两两不交.

综上, 必须从每条链上删去一个点才能使得 $v_{1}, v_{n}$ 分离, 因此至少删去 $\mathrm{C}_{n}^{2}$个 $G$ 的顶点, 才能使得 $v_{1}, v_{n !}$ 在图 $G$ 中不连通.

