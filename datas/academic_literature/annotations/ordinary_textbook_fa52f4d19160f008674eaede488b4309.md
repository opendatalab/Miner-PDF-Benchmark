数学新星网 莫学生专栏

www.nsmath.cn/xszl

# 第 37 届 CMO 试题解答与评析 

廖昱博<br>(中国人民大学附属中学, 100080)<br>指导教师: 张端阳

本届 $\mathrm{CMO}$ 较往年难度偏低, 全体考生的平均分达到了 66.6 分. 其中第 1 题与第 4 题是容易题, 第 2 题与第 5 题是中档题, 第 3 题与第 6 题是较难的中档题. 第 2 题主要考察学生代数变形的基本功; 第 5 题题目新颖, 再现了三年前的尺规作图, 考察学生遇到新题的逻辑思维能力; 第 3 题把前一轮国家队选拔的热门考点母函数再次放入 $\mathrm{CMO}$, 考生们已经准备充分, 因此做出人数较多; 第 6 题是一个中规中矩的题目. 有趣的是本届 CMO 虽然有两道几何题, 但并没有一道难度适中的常规平面几何题.

笔者有幸获得了满分, 本文是根据考场上的作答整理而来的, 方法不一定最优, 但体现了一定的思考过程. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 给定正数 $a, b$ 和平面上的一条长度为 $a$ 的线段 $A B$. 设此平面上的两个动点 $C$ 和 $D$ 满足 $A B C D$ 是一个非退化的凸四边形, 且 $B C=C D=b, D A=a$.易知存在圆 $I$ 与四边形 $A B C D$ 的四边都相切. 求圆心 $I$ 的轨迹.
2. 求满足下述条件的最大实数 $\lambda$ : 对任意正实数 $p, q, r, s$, 都存在复数 $z=a+b \mathrm{i}(a, b \in \mathbb{R})$, 使得 $|b| \geq \lambda|a|$ 且

$$
\left(p z^{3}+2 q z^{2}+2 r z+s\right)\left(q z^{3}+2 p z^{2}+2 s z+r\right)=0 .
$$

3. 求所有整数 $a$, 使得存在 6 元整数集合 $X$ 满足下述条件: 对每个 $k=1$, $2, \cdots, 36$, 都存在 $x, y \in X$, 使得 $a x+y-k$ 可被 37 整除.
4. $n(n>3)$ 个科学家一同参加会议. 在会议上, 每个科学家都有一些朋友修订日期: 2022-01-04.

（朋友关系是相互的, 且每个人都不是自己的朋友).已知无论怎样将这些科学家分成两个非空的群体, 总存在两个来自同一群体的科学家是朋友, 也存在两个来自不同群体的科学家是朋友.

在会议的第一天提出了一项提案, 每个科学家对该提案的意见均用一个非负整数表示. 从第二天起, 每个科学家对该提案的意见改为前一天其所有朋友对该提案意见的平均值的整数部分.

证明: 经过一段时间, 所有科学家对该提案都有相同的意见.

5. 我们知道, 在尺规作图中, 出现的一维几何对象只有两种: 圆周和直线.设一张纸上仅标记了距离为 1 的两个点. 证明: 可以在这张纸上用尺规作出一条直线及该直线上距离为 $\sqrt{2021}$ 的两个点, 使得作图过程中出现的不同圆周和直线的总数不超过 10 个.

注: 解答中应用明确的作图步骤, 并对出现的圆周和直线依次编号. 如果你的作图过程中圆周和直线的总数超过 10 , 那么根据总数的大小可能有部分分数.

6. 对整数 $0 \leq a \leq n$, 设 $f(n, a)$ 为多项式 $(x+1)^{a}(x+2)^{n-a}$ 的展开式系数中 3 的倍数的个数. 例如: $(x+1)^{3}(x+2)^{1}=x^{4}+5 x^{3}+9 x^{2}+7 x+2$, 因此 $f(4,3)=1$. 对任意正整数 $n$, 设 $F(n)$ 为 $f(n, 0), f(n, 1), \cdots, f(n, n)$ 中的最小值.

(1) 证明: 存在无穷多个正整数 $n$, 使得 $F(n) \geq \frac{n-1}{3}$;

(2) 证明: 对任意正整数 $n, F(n) \leq \frac{n-1}{3}$.

## II. 解答与评注

题 1 给定正数 $a, b$ 和平面上的一条长度为 $a$ 的线段 $A B$. 设此平面上的两个动点 $C$ 和 $D$ 满足 $A B C D$ 是一个非退化的凸四边形, 且 $B C=C D=b, D A=a$.易知存在圆 $I$ 与四边形 $A B C D$ 的四边都相切. 求圆心 $I$ 的轨迹.

解 建立复平面, 用一个点的字母表示该点对应的复数.

(一) 先证明 $I=\frac{b}{a+b} A+\frac{a}{a+b} C$.

事实上, 因为 $\odot I$ 与 $A B C D$ 四边均相切, 所以 $I$ 到四边距离相等且 $I$ 在内部, 于是 $A I$ 平分 $\angle B A D 、 B I$ 平分 $\angle A B C$. 由 $A B=A D, B C=D C$ 知 $\triangle A B C \cong \triangle A D C$, 所以 $A C$ 平分 $\angle B A D$, 故 $A, I, C$ 共线.

由角平分线定理, $\frac{A I}{C I}=\frac{A B}{C B}=\frac{a}{b}$, 再由定比分点公式,

$$
I=\frac{b}{a+b} A+\frac{a}{a+b} C .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_344c4c0d506ef620cc60g-03.jpg?height=497&width=506&top_left_y=200&top_left_x=775)

(二) 因为 $a, b$ 是定值, $A$ 是定点, 所以只需研究 $C$ 的轨迹.

首先, $C$ 在以 $B$ 为圆心、 $b$ 为半径的圆上, 记该圆为 $\Gamma$.

注意到当 $C$ 确定时, $D$ 可由 $B$ 关于 $A C$ 作对称所确定.

为保证 $A B C D$ 为非退化的凸四边形, 需要以下条件:

(1) $A, B, C$ 不共线;

(2) $2 \angle B A C=\angle B A D<180^{\circ}$, 即 $\angle B A C<90^{\circ}$;

(3) $2 \angle B C A=\angle B C D<180^{\circ}$, 即 $\angle B C A<90^{\circ}$.

下面按 $a, b$ 的大小关系讨论.

![](https://cdn.mathpix.com/cropped/2024_02_26_344c4c0d506ef620cc60g-03.jpg?height=514&width=651&top_left_y=1382&top_left_x=705)

情形 1: 若 $a>b$, 则由 $\angle B C A>\angle B A C$ 知 (2) 已成立. 为保证 (3, 需要 $C$ 在 $\odot(A B)$ 的外部. 由 $a>b$, 可设 $\Gamma$ 与 $\odot(A B)$ 交于点 $E, F$, 与 $A B$ 延长线交于点 $G$, 则 $C$ 的轨迹为弧 $\overparen{E G F}$ (不含点 $E, F)$ 去掉点 $G$.

作 $\angle A B E$ 的平分线交 $A E$ 于点 $E^{\prime}, \angle A B F$ 的平分线交 $A F$ 于点 $F^{\prime}$, 则

$$
\begin{array}{ll}
\frac{b}{a+b} A+\frac{a}{a+b} E=E^{\prime}, & \frac{b}{a+b} A+\frac{a}{a+b} F=F^{\prime} \\
\frac{b}{a+b} A+\frac{a}{a+b} G=B, & \frac{b}{a+b} A+\frac{a}{a+b} C=I .
\end{array}
$$

注意到对任意一点 $P, \frac{b}{a+b} A+\frac{a}{a+b} P$ 是一个关于 $A$ 的位似变换, 所以 $I$ 的轨迹为 $\odot\left(E^{\prime} B F^{\prime}\right)$ 上弧 $\widehat{E^{\prime} B F^{\prime}}$ (不含点 $\left.E^{\prime}, F^{\prime}\right)$ 去掉点 $B$.

![](https://cdn.mathpix.com/cropped/2024_02_26_344c4c0d506ef620cc60g-04.jpg?height=480&width=534&top_left_y=197&top_left_x=767)

情形 2: 若 $a=b$, 则由 $\angle B C A=\angle B A C$ 知 (2)、(3) 已成立.

此时 $\Gamma=\odot(B, B A)$, 设 $A B$ 延长线与 $\Gamma$ 交于点 $G$, 则 $C$ 的轨迹为 $\Gamma$ 去掉点 $A, G$. 因为 $I$ 为 $A C$ 中点, 所以 $I$ 的轨迹为 $\odot(A B)$ 去掉点 $A, B$.

![](https://cdn.mathpix.com/cropped/2024_02_26_344c4c0d506ef620cc60g-04.jpg?height=485&width=514&top_left_y=977&top_left_x=774)

情形 3: 若 $a<b$, 则由 $\angle B A C>\angle B C A$ 知 (3) 已成立. 为保证 (2), 需要 $C$ 与 $B$ 在过 $A$ 且垂直于 $A B$ 的直线 (记为 $l$ ) 的同侧. 设 $\Gamma$ 与 $l$ 交于点 $E, F$, 与 $A B$ 延长线交于点 $G$, 则 $C$ 的轨迹为弧 $\widehat{E G F}$ (不含点 $E, F)$ 去掉点 $G$. 后同情形 $1, I$的轨迹为 $\odot\left(E^{\prime} B F^{\prime}\right)$ 上弧 $\widehat{E^{\prime} B F^{\prime}}$ (不含点 $\left.E^{\prime}, F^{\prime}\right)$ 去掉点 $B$.

综上, 得到了 $I$ 的轨迹.

评注 这是一道极为简单的几何题, 容易发现 $I$ 的轨迹是圆的一部分, 不要漏掉对弧的端点的讨论即可.

题 2 求满足下述条件的最大实数 $\lambda$ : 对任意正实数 $p, q, r, s$, 都存在复数 $z=a+b \mathrm{i}(a, b \in \mathbb{R})$, 使得 $|b| \geq \lambda|a|$ 且

$$
\left(p z^{3}+2 q z^{2}+2 r z+s\right)\left(q z^{3}+2 p z^{2}+2 s z+r\right)=0 .
$$

解 令 $p=q=r=s=1$, 知 $z^{3}+2 z^{2}+2 z+1=0$, 解得 $z=-1$ 或 $-\frac{1}{2} \pm \frac{\sqrt{3}}{2} \mathrm{i}$,故 $\left|\frac{\sqrt{3}}{2}\right| \geq \lambda\left|-\frac{1}{2}\right|$, 即 $\lambda \leq \sqrt{3}$.

下面证明当 $\lambda=\sqrt{3}$ 时成立.
不妨设 $p s \geq q r$, 否则交换 $p$ 与 $q 、 r$ 与 $s$.

我们证明 $p z^{3}+2 q z^{2}+2 r z+s=0$ 有一个根 $z=a+b \mathrm{i}$, 满足 $|b| \geq \sqrt{3}|a|$.

设 $x$ 为一实根, $z_{1}, z_{2}$ 为另外两根, 其中 $z_{1}, z_{2}$ 均为实数或互为共轭. 记 $u=z_{1}+z_{2}, v=z_{1} z_{2}$, 则 $u, v \in \mathbb{R}$. 由 $p, q, r, s>0$ 知方程没有非负实根, 故 $x<0$.

由韦达定理，

$$
x+z_{1}+z_{2}=-\frac{2 q}{p}, \quad x z_{1}+x z_{2}+z_{1} z_{2}=\frac{2 r}{p}, \quad x z_{1} z_{2}=-\frac{s}{p},
$$

于是

$$
x+u=-\frac{2 q}{p} \text { (1) }, \quad x u+v=\frac{2 r}{p}(2), \quad x v=-\frac{s}{p} \text { (3) . }
$$

将 $x=-\frac{2 q}{p}-u$ 代入 (2)、(3), 知

$$
-\frac{2 q}{p} u-u^{2}+v=\frac{2 r}{p} \text { (4), }-\frac{2 q}{p} v-u v=-\frac{s}{p} \text { (5). }
$$

将 (4) 乘以 $s$ 、(5) 乘以 $2 r$ 并相加得,

$$
-\frac{2 q s}{p} u-s u^{2}+s v-\frac{4 q r}{p} v-2 r u v=0,
$$

即

$$
\left(-\frac{2 q s}{p}-s u\right) u=\left(\frac{4 q r}{p}+2 r u-s\right) v .
$$

显然 $v \neq 0$, 记 $\frac{u^{2}}{v}=t$, 来证 $t \leq 1$.

假设 $t>1$, 将 $v=\frac{u^{2}}{t}$ 代入上式得,

$$
\left(-\frac{2 q s}{p}-s u\right) u=\left(\frac{4 q r}{p}+2 r u-s\right) \frac{u^{2}}{t}
$$

所以

$$
\left(\frac{4 q r}{p}+2 r u-s\right) u=\left(-\frac{2 q s}{p}-s u\right) t<-\frac{2 q s}{p}-s u,
$$

其中最后一步是因为 $s>0,-\frac{2 q}{p}-u=x<0, t>1$. 化简得,

$$
r p u^{2}+2 q r u+q s<0,
$$

即

$$
r p\left(u+\frac{q}{p}\right)^{2}+\frac{q}{p}(p s-q r)<0 .
$$

这与 $p s \geq q r$ 矛盾!

所以 $t \leq 1$, 即 $\frac{u^{2}}{v} \leq 1$.

若 $z_{1}, z_{2} \in \mathbb{R}$, 则 $z_{1}, z_{2}<0$, 于是 $v>0$. 此时 $u^{2} \leq v$, 即 $\left(z_{1}+z_{2}\right)^{2} \leq z_{1} z_{2}$.但 $\left(z_{1}+z_{2}\right)^{2} \geq 4 z_{1} z_{2}$, 所以 $z_{1} z_{2} \leq 0$, 矛盾!
所以 $z_{1}, z_{2}$ 互为共轭, 设 $z_{1}=a+b \mathrm{i}, z_{2}=a-b \mathrm{i}$, 其中 $a, b \in \mathbb{R}$, 则 $u=2 a, v=$ $a^{2}+b^{2}>0$. 此时 $u^{2} \leq v$, 即 $4 a^{2} \leq a^{2}+b^{2}$, 故 $|b| \geq \sqrt{3}|a|$. 从而取 $z=z_{1}$ 即可.

综上, 所求最大值为 $\sqrt{3}$.

评注 本题的方法很多, 主要思路是用韦达定理给出根与系数的关系, 经过一些变形后按实根个数讨论, 属于中档题. 值得一提的是题目中的系数 1221 刚好是考试当天的日期.

题 3 求所有整数 $a$, 使得存在 6 元整数集合 $X$ 满足下述条件: 对每个 $k=1,2, \cdots, 36$, 都存在 $x, y \in X$, 使得 $a x+y-k$ 可被 37 整除.

解 条件等价于可重集 $a X+X$ 为模 37 的缩系.

注意到 37 是素数, 以下都在模 37 的意义下讨论.

先证明当 $a= \pm 6$ 时满足要求.

取 $X=\{16,17,18,19,20,21\}$, 则 $6 X=\{22,28,34,3,9,15\}$, 容易验证 $6 X+$ $X$ 为模 37 的缩系, 故当 $a=6$ 时满足要求. 同理, 当 $a=-6$ 时也满足要求.

再证明若 $a$ 满足要求, 则 $a^{2} X=X$.

设 $X=\left\{x_{1}, x_{2}, \cdots, x_{6}\right\}$, 显然 $X$ 中不含 0 且元素互不相同.

令 $f(t)=t^{x_{1}}+t^{x_{2}}+\cdots+t^{x_{6}}$, 则由题意,

$$
f\left(t^{a}\right) f(t) \equiv t+t^{2}+\cdots+t^{36} \quad\left(\bmod t^{37}-1\right)
$$

记 $\omega=e^{\frac{2 \pi i}{37}}$, 则对任意与 37 互质的正整数 $k$, 都有

$$
f\left(\omega^{a k}\right) f\left(\omega^{k}\right)=-1 \text { 且 } f\left(\omega^{a^{2} k}\right) f\left(\omega^{a k}\right)=-1 \text {, }
$$

所以 $f\left(\omega^{a^{2} k}\right)=f\left(\omega^{k}\right)$. 由此知对任意 37 次单位根 $t$, 都有 $f\left(t^{a^{2}}\right)=f(t)$, 于是 $t^{37}-1 \mid f\left(t^{a^{2}}\right)-f(t)$, 故 $a^{2} X=X$.

以 $1,2, \cdots, 36$ 为顶点构造有向图 $G$, 其中 $k \mapsto a^{2} k$, 则 $G$ 是若干个圈的并.设 $a^{2}$ 模 37 的阶为 $l$, 则每个圈的长度均为 $l$. 由 $a^{2} X=X$ 知 $X$ 为若干个完整的圈的并, 于是 $l \mid 6$.

(1) 若 $l=1$, 则 $a^{2}=1$.

若 $a=1$, 则 $x_{1}+x_{2}=x_{2}+x_{1}$ 在 $a X+X$ 中出现两次, 矛盾!

若 $a=-1$, 则 $0=\left(-x_{1}\right)+x_{1}$ 在 $a X+X$ 中出现, 矛盾!

(2) 若 $l=2$, 则 $a^{2}=-1$, 此时 $a= \pm 6$, 已验证满足要求.

(3) 若 $l=3$, 则 $a^{6}=1$.

若 $a^{3}=-1$, 设 $x_{1} \in X$, 则由 $a^{2} x_{1} \in X$ 知 $a^{3} x_{1} \in a X$, 即 $-x_{1} \in a X$, 所以
$0=\left(-x_{1}\right)+x_{1}$ 在 $a X+X$ 中出现, 矛盾!

若 $a^{3}=1$, 设 $x_{1} \in X$, 则由 $a^{2} x_{1} \in X$ 知 $a^{4} x_{1} \in a^{2} X$, 即 $a x_{1} \in X$. 此时 $a \cdot x_{1}+a^{2} x_{1}=a \cdot a x_{1}+a x_{1}$ 在 $a X+X$ 中出现两次, 矛盾!

(4) 若 $l=6$, 容易验证 2 是模 37 的原根, 于是 $a^{2}=2^{6}$ 或 $2^{30}$, 故 $a=2^{3}$ 或 $2^{21}$或 $2^{15}$ 或 $2^{33}$.

不妨设 $1 \in X$, 则

$$
X=\left\{1,2^{6}, 2^{12}, 2^{18}, 2^{24}, 2^{30}\right\}=\{1,27,26,36,10,11\}
$$

所以

$$
a X=\left\{2^{3}, 2^{9}, 2^{15}, 2^{21}, 2^{27}, 2^{33}\right\}=\{8,31,23,29,6,14\} .
$$

此时 $6+1=8+36$ 在 $a X+X$ 中出现两次, 矛盾!

综上, $a \equiv \pm 6(\bmod 37)$.

评注 本题根据题目的形式联想到母函数是自然的, 从而得到 $a^{2} X=X$, 故 $a^{12}=1$, 之后的工作只要时间充足应该是容易完成的。本题是一个较容易的第三题. 事实上, 题目中的 6 和 37 可以推广为一般的 $2 p$ 和 $4 p^{2}+1$, 其中 $p$ 和 $4 p^{2}+1$ 都是素数, 但是证明需要稍作改动.

题 $4 n(n>3)$ 个科学家一同参加会议. 在会议上, 每个科学家都有一些朋友（朋友关系是相互的，且每个人都不是自己的朋友）。已知无论怎样将这些科学家分成两个非空的群体, 总存在两个来自同一群体的科学家是朋友, 也存在两个来自不同群体的科学家是朋友.

在会议的第一天提出了一项提案, 每个科学家对该提案的意见均用一个非负整数表示. 从第二天起, 每个科学家对该提案的意见改为前一天其所有朋友对该提案意见的平均值的整数部分.

证明：经过一段时间, 所有科学家对该提案都有相同的意见.

证明 将科学家作为顶点, 如果两个科学家是朋友, 则在对应的顶点之间连边, 由此得到图 $G$.

(一) 先证明图 $G$ 有奇圈且连通.

若无奇圈, 则图 $G$ 是二部图. 设两部分为 $A, B$, 则 $A$ 内部、 $B$ 内部均无边,与条件矛盾! (若 $A, B$ 中有空集, 则 $G$ 为空图, 更加矛盾)

若不连通, 设图 $G$ 的一个连通分支为 $A$ 、其余点构成 $B$, 则 $A, B$ 均非空.此时 $A, B$ 之间没有边, 与条件矛盾!

（二）再证明对任意顶点 $u$, 存在正整数 $k$, 使得从 $u$ 出发恰 $k$ 步可到达所有顶点, 即对任意顶点 $v$, 存在顶点 $u=u_{0}, u_{1}, \cdots, u_{k}=v$ (允许相同), 使得对 $0 \leq i \leq k-1, u_{i}$ 与 $u_{i+1}$ 连边.

设 $C$ 是一个奇圈, 其上有 $t$ 个顶点. 任取其中一个顶点 $w$, 由图 $G$ 连通, 可得到路径 $u \rightarrow \cdots \rightarrow w \rightarrow \cdots \rightarrow v$. 设对所有顶点 $v$, 这样的路径长度的最大值为 $M$.

下面证明 $k=M+t$ 符合要求.

对任意顶点 $v$, 找路径 $u \rightarrow \cdots \rightarrow w \rightarrow \cdots \rightarrow v$, 设该路径长为 $l$, 则 $l \leq M$.

设 $v_{1}$ 是与 $v$ 相邻的一个顶点.

若 $l$ 与 $k$ 同奇偶, 则在到达 $v$ 之后, $v \rightarrow v_{1} \rightarrow v \rightarrow v_{1} \rightarrow \cdots \rightarrow v$ 即可.

若 $l$ 与 $k$ 不同奇偶, 则在到达 $w$ 之后, 先绕着 $C$ 走一圈, 回到 $w$, 再走到 $v$.此时路径长度为 $l+t \leq M+t=k$, 且 $l+t$ 与 $k$ 同奇偶, 再 $v \rightarrow v_{1} \rightarrow v \rightarrow v_{1} \rightarrow$ $\cdots \rightarrow v$ 即可.

回到原题. 将对提案的意见视为对点赋值, 考虑赋值的最大值 $S$.

注意到 $S$ 不增且赋值是非负整数, 故只有有限多种状态, 因此充分多次后必然周期. 考虑一个周期的所有状态 $\cdots, \alpha_{1}, \alpha_{2}, \cdots$, 其中下标按模 $T$ 理解. 由于 $S$ 不增, 所以周期内 $S$ 不变, 设为 $S_{0}$.

注意到若 $\alpha_{i}$ 中 $v$ 的赋值为 $S_{0}$, 则 $\alpha_{i-1}$ 中 $v$ 的邻居的赋值均为 $S_{0}$. 设 $\alpha_{0}$ 中 $u$ 的赋值为 $S_{0}$, 则 $\alpha_{-1}$ 中从 $u$ 出发恰 1 步能到达的所有点的赋值均为 $S_{0}, \alpha_{-2}$中从 $u$ 出发恰 2 步能到达的所有点的赋值均为 $S_{0}, \cdots, \alpha_{-k}$ 中从 $u$ 出发恰 $k$ 步能到达的所有点的赋值均为 $S_{0}$. 故由（二）, $\alpha_{-k}$ 中所有点的赋值均为 $S_{0}$.

故周期内所有点的赋值均相同, 而有限步后必然周期, 因此命题得证.

评注 这是一道中等偏易的漂亮的图论问题, 只需抓住最大值这一个半不变量, 后面的过程就顺理成章了.

题 5 我们知道, 在尺规作图中, 出现的一维几何对象只有两种：圆周和直线. 设一张纸上仅标记了距离为 1 的两个点. 证明: 可以在这张纸上用尺规作出一条直线及该直线上距离为 $\sqrt{2021}$ 的两个点, 使得作图过程中出现的不同圆周和直线的总数不超过 10 个.

注: 解答中应用明确的作图步骤, 并对出现的圆周和直线依次编号. 如果你的作图过程中圆周和直线的总数超过 10 , 那么根据总数的大小可能有部分分数.

证明 按以下十步作图.

![](https://cdn.mathpix.com/cropped/2024_02_26_344c4c0d506ef620cc60g-09.jpg?height=731&width=791&top_left_y=200&top_left_x=632)

第一步, 作直线 $A B$, 记为 $l$, 建立数轴 $A(0), B(1)$.

第二步, 作 $\odot(B, B A)$ 交 $l$ 于 $C(2)$.

第三步, 作 $\odot(C, C B)$ 交 $l$ 于 $D(3)$.

第四步, 作过第二步、第三步中的圆的两个交点的直线交 $l$ 于 $E(1.5)$.

第五步, 作 $\odot(D, D A)$ 交 $l$ 于 $F(6)$.

第六步, 作 $\odot(F, F A)$ 交 $l$ 于 $G(12)$.

第七步, 作 $\odot(G, G E)$ 交 $l$ 于 $H(22.5)$.

第八步, 作 $\odot(H, H A)$ 交 $l$ 于 $I(45)$.

第九步, 作 $\odot(A, A C)$ 交第八步中的圆于 $J, K$.

第十步, 作直线 $J I$.

来证 $J I=\sqrt{2021}$.

事实上, 注意到第八步中的圆以 $A I$ 为直径, 所以 $\angle A J I=90^{\circ}$. 又 $A J=$ $A C=2, A I=45$, 所以 $J I=\sqrt{A I^{2}-A J^{2}}=\sqrt{2021}$.

评注 本题是一个不太常规的几何题, 难度不大. 第一步要发现 $2021=$ $45^{2}-2^{2}$, 接下来需要构造一条长为 45 的线段和一个直角, 这里的办法很多, 基本都能做出来. 需要指出的是, 允许以已知的一点为圆心, 已知的两点之间的距离为半径作圆。事实上, 题目中的 10 步可以改进为 9 步, 但是最佳常数目前还不知道是多少.

题 6 对整数 $0 \leq a \leq n$, 设 $f(n, a)$ 为多项式 $(x+1)^{a}(x+2)^{n-a}$ 的展开式系数中, 3 的倍数的个数. 例如: $(x+1)^{3}(x+2)^{1}=x^{4}+5 x^{3}+9 x^{2}+7 x+2$, 因此 $f(4,3)=1$. 对任意正整数 $n$, 设 $F(n)$ 为 $f(n, 0), f(n, 1), \cdots, f(n, n)$ 中的最小
值.

(1) 证明: 存在无穷多个正整数 $n$, 使得 $F(n) \geq \frac{n-1}{3}$;

(2) 证明: 对任意正整数 $n, F(n) \leq \frac{n-1}{3}$.

证明 先给出 $f(n, a)$ 的递推公式.

(1) 对任意 $0 \leq a \leq k-1, f(3 k+1,3 a+2)=3 f(k-1, a)+2$.

事实上,

$$
\begin{aligned}
(x+1)^{3 a+2}(x+2)^{3 k-3 a-1} & =(x+1)^{2}(x+2)^{2}\left((x+1)^{3}\right)^{a}\left((x+2)^{3}\right)^{k-a-1} \\
& \equiv\left(x^{2}+2\right)^{2}\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k-a-1} \\
& \equiv\left(x^{4}+x^{2}+1\right)\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k-a-1} \quad(\bmod 3) .
\end{aligned}
$$

所以对 $0 \leq t \leq k-1, x^{3 t}, x^{3 t+2}, x^{3 t+4}$ 的系数均为 $\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k-a-1}$ 中 $x^{3 t}$的系数, 即 $(x+1)^{a}(x+2)^{k-a-1}$ 中 $x^{t}$ 的系数, 等于 $f(k-1, a)$. 又还有 $x$ 和 $x^{3 k}$的系数为 0 , 故共有 $3 f(k-1, a)+2$ 个系数是 3 的倍数.

(2) 对任意 $0 \leq a \leq k, f(3 k+2,3 a+2)=3 f(k, a)$.

事实上，

$$
\begin{aligned}
(x+1)^{3 a+2}(x+2)^{3 k-3 a} & =(x+1)^{2}\left((x+1)^{3}\right)^{a}\left((x+2)^{3}\right)^{k-a} \\
& \equiv\left(x^{2}+2 x+1\right)\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k-a} \quad(\bmod 3),
\end{aligned}
$$

后同 (1).

(3) 对任意 $0 \leq a \leq k, f(3 k+3,3 a+2)=2 f(k, a)+f(k+1, a)$.

事实上,

$$
\begin{aligned}
& (x+1)^{3 a+2}(x+2)^{3 k-3 a+1} \\
= & (x+1)^{2}(x+2)\left((x+1)^{3}\right)^{a}\left((x+2)^{3}\right)^{k-a} \\
\equiv & \left(x^{3}+x^{2}+2 x+2\right)\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k-a} \\
\equiv & \left(x^{2}+2 x\right)\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k-a}+\left(x^{3}+1\right)^{a}\left(x^{3}+2\right)^{k+1-a}(\bmod 3),
\end{aligned}
$$

后同 (1).

再证明 $f(n, a)=f(n, n-a) .(*)$

事实上,

$$
\begin{aligned}
&(x+1)^{a}(x+2)^{n-a} \equiv(x+1)^{a}(x-1)^{n-a} \quad(\bmod 3), \\
&(x+1)^{n-a}(x+2)^{a} \equiv(x+1)^{n-a}(x-1)^{a} \\
&=(-1)^{n}(-x+1)^{a}(-x-1)^{n-a} \quad(\bmod 3) .
\end{aligned}
$$

两式经 $x \mapsto-x$ 及乘 $(-1)^{n}$ 即可变为对方, 于是每项系数模 3 均相同或互为相
反数, 因此要么同时被 3 整除、要么同时不被 3 整除.

(1) 我们证明对正整数 $\alpha, n=3^{\alpha}-2$ 符合要求, 即 $F\left(3^{\alpha}-2\right) \geq 3^{\alpha-1}-1$.

对 $\alpha$ 归纳. 当 $\alpha=1$ 时显然成立, 假设 $\alpha$ 时成立, 来看 $\alpha+1$ 时的情形.

只需证对任意 $0 \leq b \leq 3^{\alpha+1}-2$, 都有 $f\left(3^{\alpha+1}-2, b\right) \geq 3^{\alpha}-1$.

若 $b \equiv 0(\bmod 3)$, 设 $b=3 a$. 因为

$$
(x+1)^{3 a}(x+2)^{n-3 a} \equiv\left(x^{3}+1\right)^{a}(x+2)\left(x^{3}+2\right)^{\frac{n-1}{3}-a} \quad(\bmod 3),
$$

所以 $x^{3 t+2}\left(0 \leq t \leq \frac{n-4}{3}\right)$ 的系数均为 0 , 故至少有 $\frac{n-1}{3}$ 个系数被 3 整除.

若 $b \equiv 1(\bmod 3)$, 由 $(*)$, 考虑 $3^{\alpha+1}-2-b$ 即化为上述情形.

若 $b \equiv 2(\bmod 3)$, 设 $b=3 a+2$. 由 (1) 及归纳假设,

$$
f\left(3^{\alpha+1}-2,3 a+2\right)=3 f\left(3^{\alpha}-2, a\right)+2 \geq 3\left(3^{\alpha-1}-1\right)+2=3^{\alpha}-1 .
$$

故 $\alpha+1$ 时也成立, 归纳得证.

(2) 称 $(n, a)$ 为好对, 当且仅当 $f(n, a) \leq \frac{n-1}{3}$.

由 (1), 若 $(k-1, a)$ 是好对, 则 $(3 k+1,3 a+2)$ 是好对.

由 (2), 若 $(k, a)$ 是好对, 则 $(3 k+2,3 a+2)$ 是好对.

由 (3), 若 $(k, a),(k+1, a)$ 均是好对, 则 $(3 k+3,3 a+2)$ 是好对.

对 $n$ 归纳证明, 存在 $0 \leq a \leq n$ 使得 $(n, a),(n+1, a)$ 均是好对.

因为 $f(1,0)=f(2,0)=0$, 所以当 $n=1$ 时可取 $a=0$.

因为 $f(2,2)=f(3,2)=0$, 所以当 $n=2$ 时可取 $a=2$.

因为 $f(3,1)=0, f(4,1)=1$, 所以当 $n=3$ 时可取 $a=1$.

因为 $f(4,0)=1, f(5,0)=0$, 所以当 $n=4$ 时可取 $a=0$.

因此 $n=1,2,3,4$ 时结论都成立.

假设 $n \geq 5$ 且对小于 $n$ 的正整数结论都成立, 来看 $n$ 时的情形.

若 $n=3 k+1(k \geq 2)$, 对 $k-1$ 用归纳假设, 得到 $a^{\prime}$ 使得 $\left(k-1, a^{\prime}\right),\left(k, a^{\prime}\right)$均是好对, 所以 $\left(3 k+1,3 a^{\prime}+2\right),\left(3 k+2,3 a^{\prime}+2\right)$ 均是好对.

若 $n=3 k+2(k \geq 1)$, 对 $k$ 用归纳假设, 得到 $a^{\prime}$ 使得 $\left(k, a^{\prime}\right),\left(k+1, a^{\prime}\right)$ 均是好对, 所以 $\left(3 k+2,3 a^{\prime}+2\right),\left(3 k+3,3 a^{\prime}+2\right)$ 均是好对.

若 $n=3 k+3(k \geq 1)$, 对 $k$ 用归纳假设, 得到 $a^{\prime}$ 使得 $\left(k, a^{\prime}\right),\left(k+1, a^{\prime}\right)$ 均是好对, 所以 $\left(3 k+3,3 a^{\prime}+2\right),\left(3 k+4,3 a^{\prime}+2\right)$ 均是好对.

故 $n$ 时也成立, 归纳得证.

从而对任意正整数 $n$, 存在 $0 \leq a \leq n$ 使得 $f(n, a) \leq \frac{n-1}{3}$, 故

$$
F(n) \leq f(n, a) \leq \frac{n-1}{3}
$$

评注 本题的第一个关键点是发现 $(x+1)^{3} \equiv x^{3}+1(\bmod 3)$, 于是把次数按模 3 分开, 从而可以得到递推式，做到这里可以解决第 (1) 问。在做第 (2) 问时先尝试直接归纳, 发现 $3 \mid n$ 时需要同时用到 $\frac{n}{3}$ 和 $\frac{n}{3}+1$, 故第二个关键点是进行加强归纳, 接下来就容易解决了. 本题是一个较容易的第 6 题.

