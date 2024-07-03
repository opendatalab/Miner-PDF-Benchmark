数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年 IMO 预选题及其解答 

沈子钧<br>(北京市十一学校, 100143)<br>指导教师: 吴凡迪

## I. 序

国际数学奥林匹克 (IMO) 一般于每年的七月举办, 邀请全球各国分别派最优秀的 6 名中学生组队参与并同场竞技. 每年 IMO 组委会在全世界范围内邀请资深专家组成试题委员会 (Problem Selection Committee, 简称 PSC), 而后 PSC 测试评估当年所收集的从世界各地提交的新命制数学竞赛问题, 最终确定其中 30 道左右新颖有趣且质量最高的问题组成当年 IMO 预选题 (shortlist), 其中每个版块 (代数, 几何, 组合, 数论) 各有约 7-8 个. 在 IMO 正式比赛前一周以内,各国的领队开会票选 IMO shortlist 中的 6 道题作为当年 IMO 的正式赛题.

由于 IMO shortlist 试题质量极高, 许多国家 (或地区) 希望使用第 $N$ 年未被选入正式比赛的问题作为第 $N+1$ 年代表队的选拔或训练题. 因此 IMO 组委会要求第 $N$ 年的 IMO shortlist 必须在第 $N+1$ 年的 IMO 比赛结束以前严格保密, 不能发生网络传播.

本套 2021 年 IMO shortlist 于 2022 年 7 月中旬公开. 笔者在接下来的一两个月里亲自尝试并解决了这些问题中的大多数. 对其中少数难度极大未解出的问题, 笔者广泛阅读了各大论坛的讨论以及官方解答. 本文的写作目的是整理记录 2021 年 IMO shortlist 中 32 个问题的解答、评注, 以及笔者心目中的难度评判. 直于水平, 难免出现纰漏与不当之处, 请读者指正.

本文沿用美国国家队教练 Evan Chen 引入的 MOHS 难度评判体系(详见 [3]), 简要解读如下:

- 10M 初赛常规的简单题, 因太简单免于决赛. 例如 2019 年初赛第 1 题, 2020 年初赛第 1 题.

修订日期: 2022-11-13.

- 20M 初赛偏易的中档题, 决赛常规的简单题. 例如 2019 年初赛第 2 题, 2018 年决赛第 1 题.
- 30M 初赛偏易的压轴题, 决赛常规的中档题. 例如 2020 年初赛第 4 题, 2019 年决赛第 5 题.
- 40M 初赛极难的压轴题, 决赛常规的压轴题. 例如 2021 年初赛第 4 题, 2019 年决赛第 6 题.
- $50 \mathrm{M}$ 因太困难免于初赛, 决赛极难的压轴题. 例如 2018 年决赛第 6 题, 2020 年决赛第 3 题.

特别地, “初赛” 是指全国中学生数学奥林匹克竞赛 (预赛, 暨全国高中数学联赛) 加试 A 卷, “决赛” 是指全国中学生数学奥林匹克竞赛 (决赛, 暨中国数学奥林匹克).

下面简要地谈谈笔者对本套 IMO 预选题的看法. 由于去年笔者参加北京省队培训时未经充分思考就见到了 IMO 真题 $(\mathrm{C} 2, \mathrm{~A} 4, \mathrm{G} 7 ; \mathrm{G} 2, \mathrm{C} 3, \mathrm{~A} 6)$ 的解答, 其中 A4, A6, C3 几道题的解法留下的印象太深很难重新思考, 难免有些遗憾.

在代数部分中, A1, A2, A3, A5 比较简单, 没有给人留下太多的印象. A4 相对于其位置却出乎意料的困难, 笔者曾尝试调整法与构造局部不等式的方法都没有进展, 随后查阅资料找到的先平移再归纳的证明使人眼前一亮, 而构造积分的证明让人大开眼界. A6 的解法比较巧妙, 通过组合的手法一瞬间破解了一个乍看上去无从下手的问题. A7 似乎比较难, 笔者未能独立解决, 其按照取等条件进行放缩或将下标进行分类的两种思路均值得反复玩味. A8 是一道十分复杂的函数方程问题, 融合了此类问题的各种常规方法, 在思考良久之后笔者成功解决了此题, 有几分得意.

在组合部分中, 这些题整体都很有趣. C2 虽然难度较低但问题与解答均小巧玲珑. C3 精妙的反证法令人难以忘怀. C4 所涉及的对应分析组合风味浓郁. C5 给人一种脑筋急转弯的感觉, 笔者曾被此题卡住不短的时间, 最终想到的解法也很神奇. C6 在笔者心中是这套题中最为优雅的一题, 问题的描述十分新颖,而从一维到二维过渡的思考方式又自然流畅. 许多人曾对这一题给出了形形色色的妙解, 令人印象最深的是 AoPS 论坛上仅用 8 种颜色确保猎人获胜的解法.此外, 笔者也很好奇 8 种颜色是否最优. $\mathrm{C} 7$ 的构造看似直接实则小有难度, 而证明却出人意料的简洁, 可以对方格分类并建立单射一举解决. C8 看上去抽象无从下手, 笔者未解出, 事实上此题的证明几乎是平凡的, 问题的核心在于让人
眼前一亮的归纳构造.

在几何部分中, G1, G2, G4 相对常规. G3 是一道新颖的好题, 组合味道很浓郁, 笔者在证明中采用的放缩看起来很松却始终严格服从取等条件. G5 理应是一道常规的问题, 但笔者自己找到的几何解法却十分有趣, 另一个长达三页的复数解法也使人惊叹. G6 是一道考查分析推理硬实力的组合几何好题, 其证明部分反复挖掘题目条件, 并用恰到好处的不等式估计导出矛盾. G8 特别困难, 笔者曾尝试多次均稌羽而归. 本文整理的三种解法中, 证明 2 对布里昂雄 (Brianchon) 定理的应用巧夺天工, 使人印象极深; 证明 1,3 也各自体现了独到的见解. 笔者认为在考场解题中证明 1 更有价值, 其朴素的消点思想最为自然合理.

在数论部分中, N1, N2, N3 中规中矩. N4 的解法中通过一步巧妙的取模分析规避了大量繁复讨论. N5 是繁琐的不定方程问题, 思路不难找但是需要处理大量估计细节. N6 是繁琐的组合数论问题, 笔者虽然对此类题的思路较熟悉,但还是不得不耐心地仔细讨论一番. N7 相对于其位置比较简单, 这主要是因为近年来先证明有界再证明 (最终) 周期这类手法已经逐渐论为套路. N8 在笔者心中是本套预选题中最难的一题, 需要在深入理解问题结构的基础上 (否则即使阅读答案也很可能是看不太懂的) 挖掘一个隐藏很深的量并对它做精细的大小估计导出相应的矛盾. 竞赛范围内如此困难的数论题实属罕见, 因此本题也给笔者留下了深刻的印象.

在序章的最后, 笔者感谢董子超老师对全文编辑校对的付出. 感谢陈晨老师于去年省队培训中分享 IMO 真题的解答, 感谢东紫昭学姐提供 G5 的复数解法, 感谢段柏延老师提供 G8 的消点解法, 感谢徐子健学长提供 C8 的构造思路.笔者也对在微信小程序数之谜上发表解答的罗方舟, 孙牧聪, 温元赫等同学, 以及在 AoPS 论坛上提供解答的网友们一并致谢.

## II. 问 题

## 一、代数

A1. 给定正整数 $n$. 设 $A$ 为 $\left\{0,1, \ldots, 5^{n}\right\}$ 的子集. 证明: 若 $A$ 的元素个数满足 $|A|=4 n+2$, 则存在 $a, b, c \in A$ 使得 $a<b<c$ 且 $c+2 a>3 b$.

A2. 求所有正整数 $n$, 使得

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\lfloor\frac{i j}{n+1}\right\rfloor=\frac{n^{2}(n-1)}{4}
$$

A3. 设 $n$ 为正整数. 当 $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$ 取遍 $\{1,2, \ldots, n\}$ 的所有排列时, 求代数式 $S=\sum_{k=1}^{n}\left\lfloor\frac{a_{k}}{k}\right\rfloor$ 的最小可能值.

A4. 设 $n$ 是正整数, $x_{1}, x_{2}, \ldots, x_{n}$ 是实数. 证明:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}-x_{j}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}+x_{j}\right|}
$$

A5. 已知正整数 $n \geq 2$, 且 $a_{1}, a_{2}, \ldots, a_{n}$ 是和为 1 的正实数. 证明:

$$
\sum_{k=1}^{n} \frac{a_{k}}{1-a_{k}}\left(a_{1}+a_{2}+\cdots+a_{k-1}\right)^{2}<\frac{1}{3}
$$

A6. 设整数 $m \geq 2$. 集合 $A$ 由有限个整数 (不一定为正) 构成, 且 $B_{1}, B_{2}$, $\cdots, B_{m}$ 是 $A$ 的子集. 已知对任意 $k=1,2, \ldots, m$, 均有 $B_{k}$ 中所有数之和为 $m^{k}$.证明: $|A| \geq \frac{m}{2}$.

A7. 设整数 $n \geq 1$, 非负实数 $x_{0}, x_{1}, \ldots, x_{n+1}$ 满足: $x_{i} x_{i+1}-x_{i-1}^{2} \geq 1$ 对 $i=1,2, \ldots, n$ 成立. 证明:

$$
x_{0}+x_{1}+\cdots+x_{n+1}>\left(\frac{2 n}{3}\right)^{3 / 2}
$$

A8. 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意实数 $a, b, c$, 均有 $(f(a)-f(b))(f(b)-f(c))(f(c)-f(a))=f\left(a b^{2}+b c^{2}+c a^{2}\right)-f\left(a^{2} b+b^{2} c+c^{2} a\right)$.

## 二、组合

C1. 设 $S$ 为正整数 $\mathbb{N}^{*}$ 的无穷子集, 且存在互不相同的 $a, b, c, d \in S$ 使得 $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(c, d)$. 证明: 存在互不相同的 $x, y, z \in S$ 使得

$$
\operatorname{gcd}(x, y)=\operatorname{gcd}(y, z) \neq \operatorname{gcd}(z, x)
$$

C2. 设正整数 $n \geq 3$. 一条环形项链上串有 $m \geq n+1$ 颗珠子. 小明希望将每颗珠子染为 $n$ 种不同颜色之一, 使得在任何连续 $n+1$ 颗珠子中每种颜色至少出现一次. 求使得小明不能实现愿望的不同正整数 $m$ 的个数.

C3. 两只松鼠 B 和 $\mathrm{J}$ 为过冬收集了 2021 枚核桃. $\mathrm{J}$ 将核桃依次编号为 1 到 2021, 并在它们最喜欢的树周围挖了一圈共 2021 个小坑. 第二天早上, $\mathrm{J}$ 发现 B 已经在每个小坑里放入了一枚核桃, 但并未注意编号. 不开心的 J 决定用 2021 次操作来改变这些核桃的位置. 在第 $k$ 次操作中, $\mathrm{J}$ 把与第 $k$ 号核桃相邻的两枚核桃交换位置. 证明: 存在某个 $k$, 使得在第 $k$ 次操作中, $\mathrm{J}$ 交换了两枚编号为 $a$ 和 $b$ 的核桃, 且 $a<k<b$.

C4. 设 $T$ 是完全有向简单图. 称若干条有向道路组成的集合为不交的,是指其中任何两条道路无公共边 (这里一条道路不能重复经过同一顶点). 设 $v, w$ 为 $T$ 的顶点. 记 $M$ 为从 $v$ 到 $w$ 的不交道路集所含元素个数的最大可能值;记 $N$ 为从 $w$ 到 $v$ 的不交道路集所含元素个数的最大可能值.

证明: $M=N$ 当且仅当 $v, w$ 在 $T$ 中的出度相同.

C5. 设正整数 $n>k \geq 1$. 有 $2 n+1$ 名学生围坐一个圆圈 (面向圆心). 每名学生有 $2 k$ 个邻居, 即左手边最近的 $k$ 名同学和右手边最近的 $k$ 名同学. 已知这些学生中有 $n+1$ 名女生和 $n$ 名男生.

证明: 存在一名女生, 其 $2 k$ 个邻居中至少有 $k$ 名女生.

C6. 一名猎人与一只隐形兔子在无穷大的方格表上做如下游戏:

(1) 猎人选取正整数 $N$, 并在每个小方格内放置整数根 (至少 1 根至多 $N$ 根) 胡萝卜. 在放置完毕后, 猎人不能再观察方格表中的胡萝卜.

(2) 兔子从某一小方格出发, 吃掉其中的所有胡萝卜, 并将其所吃胡萝卜的总数报告至猎人.

(3) 在每一轮中, 兔子移到某一相邻 (有公共边) 且有胡萝卜的小方格, 吃掉其中的所有胡萝卜, 并将其所吃胡萝卜的总数报告至猎人.

若兔子不能移动, 或猎人可以确定兔子的初始小方格, 则猎人获胜.

问: 猎人是否有必胜策略?

C7. 设正整数 $m>1$, 考虑一个 $3 m \times 3 m$ 的方格棋盘. 一只青蛙从位于左下角的方格 $S$ 出发去右上角的方格 $F$, 它每一步向右或向上跳一个方格. 有一些方格是陷阱, 一旦青蛙到达陷阱方格就会被困住. 称若干个方格组成的集合 $X$ 为障碍集, 如果当 $X$ 中的所有方格均为陷拼时青蛙无法从 $S$ 出发到达 $F$. 称一个障碍集为极小的, 是指它的任何非空真子集均不是障碍集.

(a) 证明: 存在一个由至少 $3 m^{2}-3 m$ 个方格组成的极小障碍集.

(b) 证明: 每个极小障碍集均由不超过 $3 m^{2}$ 个方格组成.

C8. 求最大的正整数 $N$, 使得存在 $N$ 行 100 列的正整数数表 $\left(t_{i, j}\right)_{N \times 100}$, 满足:

(1) 每行的 100 个数 $t_{i, 1}, t_{i, 2}, \ldots, t_{i, 100}(1 \leq i \leq N)$ 均为 $1,2, \ldots, 100$ 的排列.

(2) 对任意不同的两行 $r, s$, 均存在一列 $c$, 使得

$$
\left|t_{r, c}-t_{s, c}\right| \geq 2
$$

G1. 如图, 在平行四边形 $A B C D$ 中, $A C=B C, P$ 在线段 $A B$ 的延长线上. 已知 $\triangle A C D$ 的外接圆与线段 $P D$ 交于另一点 $Q$, 且 $\triangle A P Q$ 的外接圆与线段 $P C$ 交于另一点 $R$. 证明: $C D, A Q, B R$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-06.jpg?height=651&width=651&top_left_y=525&top_left_x=705)

G2. 如图, 圆 $\Gamma$ 的圆心为点 $I$. 凸四边形 $A B C D$ 满足: 线段 $A B, B C, C D$, $D A$ 都与 $\Gamma$ 相切. 设 $\Omega$ 是过 $A, I, C$ 三点的圆. 延长 $B A$ 交 $\Omega$ 于点 $X$, 延长 $B C$ 交 $\Omega$ 于点 $Z$, 延长 $A D$ 交 $\Omega$ 于点 $Y$, 延长 $C D$ 交 $\Omega$ 于点 $T$. 证明:

$$
A D+D T+T X+X A=C D+D Y+Y Z+Z C .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-06.jpg?height=683&width=910&top_left_y=1543&top_left_x=573)

G3. 考虑 $100 \times 100$ 的单位点阵 $\mathbf{L}$ (即 $|\mathbf{L}|=10000$ ). 设 $\mathcal{F}$ 是由若干多边形组成的集合, 满足:

(1) 每个 $\mathcal{F}$ 中多边形的所有顶点均落在 $\mathbf{L}$ 中;

(2) 每个 $\mathbf{L}$ 中的点恰作为一个 $\mathcal{F}$ 中多边形的顶点.

求 $\mathcal{F}$ 中所有多边形面积之和 $S$ 的最大可能值.

G4. 如图, 四边形 $A B C D$ 内接于圆 $\Omega$. 过点 $D$ 作 $\Omega$ 的切线分别与射线 $B A, B C$ 交于点 $E, F$. 已知 $\triangle A B C$ 内一点 $T$ 满足 $T E / / C D, T F / / A D$. 线段 $D F$ 内一点 $K$ 满足 $T D=T K$. 证明: $A C, D T, B K$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-07.jpg?height=468&width=811&top_left_y=451&top_left_x=634)

G5. 如图, 边长两两不等的四边形 $A B C D$ 内接于圆 $\Omega$ (圆心为 $O$ ), 角 $\angle A B C, \angle A D C$ 的平分线分别与对角线 $A C$ 交于 $B_{1}, D_{1}$ 两点. 圆 $\omega_{B}$ 过点 $B$ 且与 $A C$ 相切于点 $D_{1}$, 圆 $\omega_{D}$ 过点 $D$ 且与 $A C$ 相切于点 $B_{1}$. 设 $\omega_{B}, \omega_{D}$ 的圆心分别为 $O_{B}, O_{D}$. 证明: 若 $B D_{1} / / B_{1} D$, 则 $O_{B}, O, O_{D}$ 三点共线.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-07.jpg?height=622&width=665&top_left_y=1345&top_left_x=701)

G6. 求所有正整数 $n \geq 3$, 使得任一各边长均为 1 的凸 $n$ 边形均包含一边长为 1 的正三角形.

注: 本题涉及的多边形(三角形)同时包含边界与内部.

G7. 如图, 在锐角 $\triangle A B C$ 中, $A B>A C, D$ 是形内一点, 使得 $\angle D A B=$ $\angle C A D$. 线段 $A C$ 上一点 $E$ 满足 $\angle A D E=\angle B C D$, 线段 $A B$ 上一点 $F$ 满足 $\angle F D A=\angle D B C$, 且直线 $A C$ 上一点 $X$ 满足 $C X=B X$. 设 $O_{1}, O_{2}$ 分别为 $\triangle A D C, \triangle E X D$ 的外心. 证明: $B C, E F, O_{1} O_{2}$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-08.jpg?height=585&width=845&top_left_y=230&top_left_x=594)

G8. 如图, 在 $\triangle A B C$ 中, $\omega$ 是外接圆, $\Omega_{A}$ 是 $A$-旁切圆, 且圆 $\omega$ 与 $\Omega_{A}$ 交于 $X, Y$ 两点. 过 $X, Y$ 分别作 $\Omega_{A}$ 的切线, 设 $A$ 在这两条切线上的射影分别为 $P, Q$. 过 $P, Q$ 分别作圆 $(A P X),(A Q Y)$ 的切线交于点 $R$. 证明: $A R \perp B C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-08.jpg?height=907&width=506&top_left_y=1114&top_left_x=772)

## 四、数论

N1. 求所有正整数 $n \geq 1$, 使得存在一对正整数 $(a, b)$, 满足: 正整数 $a^{2}+b+3$ 无立方因子, 且

$$
n=\frac{a b+3 b+8}{a^{2}+b+3}
$$

N2. 设整数 $n>100$. 将数 $n, n+1, \ldots, 2 n$ 任意分为两组. 证明: 必定存在同组的两个数之和是一个完全平方数.

N3. 求所有正整数 $n$, 满足: 数 $n$ 全部的 $k$ 个不同正约数可以被排列为 $d_{1}, d_{2}, \ldots, d_{k}$, 使得对任意正整数 $i=1,2, \ldots, k$ 均有 $d_{1}+d_{2}+\cdots+d_{i}$ 是完全平方数.

N4. 设有理数 $r>1$. 小明在数轴上玩如下单人游戏: 一开始, 在 0 处有一颗红色珠子, 在 1 处有一颗蓝色珠子. 每一轮, 小明选取其中一颗珠子并选取整数 $k$. 如果被选中的珠子位于 $x$, 而未被选中的珠子位于 $y$, 则在该轮游戏中小明将选中的珠子移动到 $x^{\prime}$, 使得 $x^{\prime}-y=r^{k}(x-y)$.

求所有 $r$, 使得小明可以经过至多 2021 轮游戏将红色珠子移动到 1 .

N5. 证明: 只有有限多组正整数 $(a, b, c, n)$ 满足不定方程

$$
n !=a^{n-1}+b^{n-1}+c^{n-1} .
$$

N6. 求所有整数 $n \geq 2$, 满足: 对任意 $n$ 个不同正整数 $x_{1}, x_{2}, \ldots, x_{n}$, 若 $n \nmid x_{1}+x_{2}+\cdots+x_{n}$, 则存在它们的某个排列 $a_{1}, a_{2}, \ldots, a_{n}$, 使得

$$
n \mid 1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n} .
$$

N7. 正整数数列 $\left\{a_{n}\right\}$ 满足: 对任意正整数 $m, n$, 均有

$$
a_{m+2 n} \mid a_{m}+a_{m+n}
$$

证明： $\left\{a_{n}\right\}$ 是最终周期的数列.

N8. 求所有正整数 $n$, 使得存在整系数多项式 $P(x)$, 满足：对任意正整数 $m, P^{m}(1), \ldots, P^{m}(n)$ 在模 $n$ 的意义下恰取到 $\left\lceil\frac{n}{2^{m}}\right\rceil$ 个不同余数. 这里 $P^{m}$ 表示 $P$ 的 $m$ 次迭代.

## III. 解答与评注

## 一、代数

A1. 给定正整数 $n$. 设 $A$ 为 $\left\{0,1, \ldots, 5^{n}\right\}$ 的子集. 证明: 若 $A$ 的元素个数满足 $|A|=4 n+2$, 则存在 $a, b, c \in A$ 使得 $a<b<c$ 且 $c+2 a>3 b$.

证明 设 $A=\left\{x_{1}, x_{2}, \cdots, x_{4 n+2}\right\}$, 其中 $x_{1}<x_{2}<\cdots<x_{4 n+2}=M$.

假设原题结论不成立, 则对 $1 \leq i \leq 4 n$ 均有 $2 x_{i}+M \leq 3 x_{i+1}$, 即

$$
\left(\frac{3}{2}\right)^{i-1} \cdot x_{i} \leq\left(\frac{3}{2}\right)^{i} \cdot x_{i+1}-\frac{M}{2} \cdot\left(\frac{3}{2}\right)^{i-1} .
$$

将此式对 $1 \leq i \leq 4 n$ 求和, 得

$$
\begin{aligned}
x_{1} & \leq\left(\frac{3}{2}\right)^{4 n} \cdot x_{4 n+1}-\frac{M}{2} \cdot\left(\left(\frac{3}{2}\right)^{4 n-1}+\left(\frac{3}{2}\right)^{4 n-2}+\cdots+\left(\frac{3}{2}\right)^{0}\right) \\
& =\left(\frac{3}{2}\right)^{4 n} \cdot x_{4 n+1}-\left(\left(\frac{3}{2}\right)^{4 n}-1\right) \cdot M \\
& \leq\left(\frac{3}{2}\right)^{4 n} \cdot(M-1)-\left(\left(\frac{3}{2}\right)^{4 n}-1\right) \cdot M \\
& =M-\left(\frac{3}{2}\right)^{4 n} \leq 5^{n}-\left(\frac{3}{2}\right)^{4 n} .
\end{aligned}
$$

注意到 $3^{4}=81>80=5 \cdot 2^{4}$, 故 $\left(\frac{3}{2}\right)^{4}>5$, 从而 $x_{1}<0$, 矛盾! 假设错误, 结论成立.

评注 从反面考虑这个问题时, 容易发现即使我们贪心地从大往小将数加入 $A$, 所取数间隔也不得不越来越大, 最终导致 $A$ 的最小数为负数. 简单整理这个想法便可得到以上证明.

本题预计难度 $5 \mathrm{M}$.

A2. 求所有正整数 $n$, 使得

$$
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\lfloor\frac{i j}{n+1}\right\rfloor=\frac{n^{2}(n-1)}{4}
$$

解 所求 $n$ 为所有使得 $n+1$ 为素数的正整数.

在本题中, 对任意命题 $p$, 记

注意到

$$
[p]= \begin{cases}0, & \text { 若 } p \text { 是假命题, } \\ 1, & \text { 若 } p \text { 是真命题. }\end{cases}
$$

$\left\lfloor\frac{i j}{n+1}\right\rfloor+\left\lfloor\frac{i(n+1-j)}{n+1}\right\rfloor=i+\left\lfloor\frac{i j}{n+1}\right\rfloor+\left\lfloor-\frac{i j}{n+1}\right\rfloor=i-1+[n+1 \mid i j]$,

故

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\lfloor\frac{i j}{n+1}\right\rfloor & =\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\left\lfloor\frac{i j}{n+1}\right\rfloor+\left\lfloor\frac{i(n+1-j)}{n+1}\right\rfloor\right) \\
& =\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n}(i-1+\lfloor n+1 \mid i j]) \\
& \geq \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n}(i-1) \\
& =\frac{n^{2}(n-1)}{4} .
\end{aligned}
$$

注意到上面的不等号成立当且仅当不存在 $1 \leq i, j \leq n$ 使得 $n+1 \mid i j$, 即 $n+1$ 为素数.

综上, 所有满足要求的正整数 $n$ 即一切使得 $n+1$ 为素数的正整数.

评注 首尾配对的想法比较自然, 在配对之后处理起来也比较容易.

本题预计难度 $15 \mathrm{M}$.

A3. 设 $n$ 为正整数. 当 $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$ 取遍 $\{1,2, \ldots, n\}$ 的所有排列时, 求代数式 $S=\sum_{k=1}^{n}\left\lfloor\frac{a_{k}}{k}\right\rfloor$ 的最小可能值.

解 所求 $S$ 的最小可能值为 $\left\lfloor\log _{2} n\right\rfloor+1$.

一方面, 考虑排列

$$
a_{k}= \begin{cases}\min \{2 k-1, n\}, & \text { 若 } k \text { 是 } 2 \text { 的幂, } \\ k-1, & \text { 若 } k \text { 不是 } 2 \text { 的幂, }\end{cases}
$$

则 $\left\lfloor\frac{a_{k}}{k}\right\rfloor \in\{0,1\}$, 且 $\left\lfloor\frac{a_{k}}{k}\right\rfloor=1$ 当且仅当 $k$ 是 2 的幕. 易见此时 $S=\left\lfloor\log _{2} n\right\rfloor+1$.

另一方面, 将 $S$ 的最小值看作 $n$ 的函数 $f(n)$ (规定 $f(0)=0$ ). 我们说明 $f(n) \geq\left\lfloor\log _{2} n\right\rfloor+1$.

引理 对任意正整数 $n$, 均有

$$
f(n) \geq \min _{1 \leq i \leq n}\left\{f(i-1)+\left\lfloor\frac{n}{i}\right\rfloor\right\} .
$$

证明 对 $\{1,2, \ldots, n\}$ 的排列 $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$, 设 $a_{i}=n$. 若 $i=1$, 则

$$
S \geq\left\lfloor\frac{a_{1}}{1}\right\rfloor=f(0)+\left\lfloor\frac{n}{1}\right\rfloor .
$$

以下设 $i \geq 2$.

设 $\{1,2, \ldots, i-1\}$ 的排列 $\left(b_{1}, b_{2}, \ldots, b_{i-1}\right)$ 满足: 对 $k \in\{1,2, \ldots, i-1\}$ 均有 $a_{k}$ 是 $a_{1}, a_{2}, \ldots, a_{i-1}$ 中第 $b_{k}$ 小的数, 则

$$
\sum_{k=1}^{n}\left\lfloor\frac{a_{k}}{k}\right\rfloor \geq \sum_{k=1}^{i}\left\lfloor\frac{a_{k}}{k}\right\rfloor \geq\left\lfloor\frac{n}{i}\right\rfloor+\sum_{k=1}^{i-1}\left\lfloor\frac{a_{k}}{k}\right\rfloor \geq\left\lfloor\frac{n}{i}\right\rfloor+\sum_{k=1}^{i-1}\left\lfloor\frac{b_{k}}{k}\right\rfloor \geq f(i-1)+\left\lfloor\frac{n}{i}\right\rfloor
$$

综合以上讨论, 引理得证.

回到原题. 我们对正整数 $n$ 归纳证明 $f(n) \geq\left\lfloor\log _{2} n\right\rfloor+1$.

当 $n=1$ 时 $f(1)=1$, 结论成立.

假设 $1,2, \ldots, n-1(n \geq 2)$ 的结论已经证明, 考虑 $n$ 的情形.

根据引理, 只需证明

$$
\min _{1 \leq i \leq n}\left\{f(i-1)+\left\lfloor\frac{n}{i}\right\rfloor\right\} \geq\left\lfloor\log _{2} n\right\rfloor+1
$$

设 $\left\lfloor\frac{n}{i}\right\rfloor=t$, 则 $\frac{n}{i}<t+1$, 即 $i>\frac{n}{t+1}$, 从而 $i-1 \geq\left\lfloor\frac{n}{t+1}\right\rfloor$. 又因为 $f$ 单调不减, 所以

$$
f(i-1)+\left\lfloor\frac{n}{i}\right\rfloor \geq f\left(\left\lfloor\frac{n}{t+1}\right\rfloor+t\right) \geq f\left(\left\lfloor\frac{n}{2^{t}}\right\rfloor\right)+t
$$

若 $\left\lfloor\frac{n}{2 t}\right\rfloor=0$, 则

$$
f\left(\left\lfloor\frac{n}{2^{t}}\right\rfloor\right)+t=t \geq\left\lfloor\log _{2} n\right\rfloor+1
$$

若 $\left\lfloor\frac{n}{\left.2^{t}\right\rfloor} \geq 1\right.$, 则代入归纳假设即证明了 $(*)$.

综上所述, 表达式 $S$ 的最小可能值为 $\left\lfloor\log _{2} n\right\rfloor+1$.

评注 注意到 $\left\lfloor\frac{n}{k}\right\rfloor$ 容易比较大, 这启发我们设出 $a_{i}=n$. 之后进行一些推导就可以发现

$$
f(n)=\min _{1 \leq i \leq n}\left\{f(i-1)+\left\lfloor\frac{n}{i}\right\rfloor\right\}
$$

这一兼顾了构造与证明的结果 (证明的方法与引理的证明完全一样, 而构造部分则可以令 $a_{1}$ 至 $a_{i-1}$ 为 1 至 $i-1$ 的一个排列, 后面的项令 $a_{j}=j-1$ 即可), 此后用此式研究 $f(n)$ 的值便不难解决问题了 (发现 $f(n)=\min _{1 \leq i \leq n}\left\{f(i-1)+\left\lfloor\frac{n}{i}\right\rfloor\right\}$ 的过程实际上指出了构造的方式).

本题预计难度 $25 \mathrm{M}$.

A4. 设 $n$ 是正整数, $x_{1}, x_{2}, \ldots, x_{n}$ 是实数. 证明:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}-x_{j}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}+x_{j}\right|}
$$

证明 1 (官方解答) 我们对 $n$ 归纳证明此不等式.

当 $n=0,1$ 时不等式显然成立.

对于 $n \geq 2$, 假设 $0,1, \ldots, n-1$ 的情形均成立.

设 $x_{i}+x_{j}(1 \leq i, j \leq n)$ 这 $n^{2}$ 个数中最大的非正数为 $l$, 最小的非负数为 $r$.对任意 $l \leq d \leq r$, 设 $x_{i}^{\prime}=x_{i}-\frac{d}{2}(i=1,2, \ldots, n)$, 则

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}-x_{j}\right|}=\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}^{\prime}-x_{j}^{\prime}\right|}
$$

根据函数 $y=\sqrt{x}$ 的上凸性, 又注意到 $x_{i}+x_{j}$ 与 $x_{i}^{\prime}+x_{j}^{\prime}$ 同号, 那么

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}+x_{j}-d\right|}
$$

的最大值在端点处取到. 而无论 $d=l$ 还是 $d=r$, 均存在 $1 \leq i, j \leq n$ 使得 $x_{i}^{\prime}+x_{j}^{\prime}=0$.
若 $i=j$, 则 $x_{i}^{\prime}=0$. 消去左右两边含 $x_{i}^{\prime}$ 的项并使用 $n-1$ 时的归纳假设知

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}^{\prime}-x_{j}^{\prime}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}^{\prime}+x_{j}^{\prime}\right|}
$$

若 $i \neq j$, 则 $x_{j}^{\prime}=-x_{i}^{\prime}$. 消去左右两边含 $x_{i}^{\prime}, x_{j}^{\prime}$ 的项并使用 $n-2$ 时的归纳假设知

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}^{\prime}-x_{j}^{\prime}\right|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{\left|x_{i}^{\prime}+x_{j}^{\prime}\right|}
$$

这就完成了归纳证明, 原不等式得证.

评注 注意到不等式的平移不变性后, 经过大量尝试不同的调整方法, 可以找到以上归纳证明。

证明 2 (罗方舟) 对于正实数 $a$, 有

$$
\int \frac{1-\cos a x}{x \sqrt{x}} d x=4 \sqrt{a} \cdot S(\sqrt{a x})+\frac{2(\cos a x-1)}{\sqrt{x}}+C,
$$

其中

$$
S(x)=\int_{0}^{x} \sin t^{2} d t
$$

特别地, 有 $S(0)=0$ 且 $S(+\infty)=\sqrt{\frac{\pi}{8}}$, 故

$$
\begin{aligned}
\sqrt{|a+b|}-\sqrt{|a-b|} & =\frac{1}{\sqrt{2 \pi}} \int_{0}^{+\infty} \frac{\cos (a-b) x-\cos (a+b) x}{x \sqrt{x}} d x \\
& =\frac{1}{\sqrt{2 \pi}} \int_{0}^{+\infty} \frac{2 \sin a x \sin b x}{x \sqrt{x}} d x .
\end{aligned}
$$

回到原题,

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n}\left(\sqrt{\left|x_{i}+x_{j}\right|}-\sqrt{\left|x_{i}-x_{j}\right|}\right) & =\sum_{i=1}^{n} \sum_{j=1}^{n} \frac{1}{\sqrt{2 \pi}} \int_{0}^{+\infty} \frac{2 \sin x_{i} t \sin x_{j} t}{t \sqrt{t}} d t \\
& =\frac{1}{\sqrt{2 \pi}} \int_{0}^{+\infty} \sum_{i=1}^{n} \sum_{j=1}^{n} \frac{2 \sin x_{i} t \sin x_{j} t}{t \sqrt{t}} d t \\
& =\frac{1}{\sqrt{2 \pi}} \int_{0}^{+\infty} \frac{2\left(\sin x_{0} t+\cdots+\sin x_{n} t\right)^{2}}{t \sqrt{t}} d t \\
& \geq 0,
\end{aligned}
$$

这就证明了原不等式.

评注 如果将原题中所有的根号同时去掉, 则所得的不等式可以不难用积分方法证明，这启发我们尝试通过积分证明原不等式。当然, 这里使用的积分公式更高明．以上解答由原作者发表于微信小程序“数之谜”的讨论区.

本题预计难度 $45 \mathrm{M}$.

A5. 已知正整数 $n \geq 2$, 且 $a_{1}, a_{2}, \ldots, a_{n}$ 是和为 1 的正实数. 证明:

$$
\sum_{k=1}^{n} \frac{a_{k}}{1-a_{k}}\left(a_{1}+a_{2}+\cdots+a_{k-1}\right)^{2}<\frac{1}{3}
$$

证明 设 $S_{k}=\sum_{i=1}^{k} a_{k}(k=0,1, \ldots, n)$, 这里规定 $S_{0}=0$.

引理 对 $k=1,2, \ldots, n$ 均有

$$
\frac{S_{k}-S_{k-1}}{1-S_{k}+S_{k-1}} S_{k-1}^{2}<\frac{S_{k}^{3}-S_{k-1}^{3}}{3}
$$

证明 此不等式等价于 $\frac{S_{k-1}^{2}}{1-S_{k}+S_{k-1}}<\frac{S_{k}^{2}+S_{k} S_{k-1}+S_{k-1}^{2}}{3}$, 即

$$
\begin{aligned}
& \Longleftrightarrow 3 S_{k-1}^{2}<S_{k}^{2}+S_{k} S_{k-1}+S_{k-1}^{2}-\left(S_{k}-S_{k-1}\right)\left(S_{k}^{2}+S_{k} S_{k-1}+S_{k-1}^{2}\right) \\
& \Longleftrightarrow\left(S_{k}-S_{k-1}\right)\left(S_{k}^{2}+S_{k} S_{k-1}+S_{k-1}^{2}\right)<S_{k}^{2}+S_{k} S_{k-1}-2 S_{k-1}^{2} \\
& \Longleftrightarrow S_{k}^{2}+S_{k} S_{k-1}+S_{k-1}^{2}<S_{k}+2 S_{k-1} \\
& \Longleftrightarrow\left(S_{k}+S_{k-1}\right)\left(1-S_{k}\right)+S_{k-1}\left(1-S_{k-1}\right)>0 .
\end{aligned}
$$

注意到 $S_{k-1}=0$ 与 $S_{k}=1$ 不同时成立, 从而上式为真, 引理得证.

回到原题, 由引理得

$\sum_{k=1}^{n} \frac{a_{k}}{1-a_{k}}\left(a_{1}+a_{2}+\cdots+a_{k-1}\right)^{2}=\sum_{k=1}^{n} \frac{S_{k}-S_{k-1}}{1-S_{k}+S_{k-1}} S_{k-1}^{2}<\sum_{k=1}^{n} \frac{S_{k}^{3}-S_{k-1}^{3}}{3}=\frac{1}{3}$,这就证明了原不等式.

评注 不等式的形式使我们联想到裂项或积分等方法, 经过尝试不难发现引理中的局部不等式.

本题预计难度 $25 \mathrm{M}$.

A6. 设整数 $m \geq 2$. 集合 $A$ 由有限个整数 (不一定为正) 构成, 且 $B_{1}, B_{2}$, $\cdots, B_{m}$ 是 $A$ 的子集. 已知对任意 $k=1,2, \ldots, m$ ，均有 $B_{k}$ 中所有数之和为 $m^{k}$.证明: $|A| \geq \frac{m}{2}$.

证明 (陈晨) 设 $A=\left\{a_{1}, a_{2}, \ldots, a_{n}\right\}$. 将 $0,1, \ldots, m^{m}-1$ 中的每个数 $t$ 用 $m$ 进制表示, 即

$$
t=\sum_{k=1}^{m} x_{k-1} m^{k-1} \quad\left(0 \leq x_{i} \leq m-1\right)
$$

根据 $B_{k}$ 将每个 $m^{k}$ 写作 $A$ 中若干不同数之和, 展开并合并同类项得

$$
\sum_{k=1}^{m} x_{k-1} m^{k}=m t=\sum_{i=1}^{n} y_{i} a_{i} \quad\left(0 \leq y_{i} \leq m^{2}-m\right)
$$

注意到上式左边有 $m^{m}$ 个不同取值, 而右边有 $\left(m^{2}-m+1\right)^{n} \leq m^{2 n}$ 个不同取
值, 因此

$$
m^{2 n} \geq m^{m} \Longrightarrow|A|=n \geq \frac{m}{2}
$$

评注 由 $B_{1}, B_{2}, \ldots, B_{m}$ 是 $A$ 的子集可知: 若能将一个数表示成若干 $B_{k}$ 的元素和之和, 则能进一步地将其拆分为若干 $A$ 中的元素之和. 以上分析提供了一个可用的估计，从而解决了问题.

本题预计难度 $30 \mathrm{M}$.

A7. 设整数 $n \geq 1$, 非负实数 $x_{0}, x_{1}, \ldots, x_{n+1}$ 满足: $x_{i} x_{i+1}-x_{i-1}^{2} \geq 1$ 对 $i=1,2, \ldots, n$ 成立. 证明:

$$
x_{0}+x_{1}+\cdots+x_{n+1}>\left(\frac{2 n}{3}\right)^{3 / 2}
$$

证明 $\mathbf{1}$ (孙牧聪) 对 $i=1,2, \ldots, n+1$, 记 $y_{i}=2 x_{i-1}+x_{i}$, 则

$$
\begin{aligned}
y_{i+1}^{2}-y_{i}^{2} & =\left(2 x_{i}+x_{i+1}\right)^{2}-\left(2 x_{i-1}+x_{i}\right)^{2} \\
& \geq\left(2 x_{i}+x_{i+1}^{2}\right)-3\left(2 x_{i-1}^{2}+x_{i}\right)^{2} \\
& \geq 6 x_{i} x_{i+1}-6 x_{i-1}^{2} \geq 6 .
\end{aligned}
$$

因此 $y_{i} \geq \sqrt{6(i-1)}$ 对 $i=1, \ldots, n+1$ 均成立, 故

$$
\begin{aligned}
x_{0}+x_{1}+\cdots+x_{n+1} & \geq \frac{1}{3}\left(y_{2}+y_{3}+\cdots+y_{n+1}\right) \\
& \geq \frac{\sqrt{6}}{3}(\sqrt{1}+\sqrt{2}+\cdots+\sqrt{n}) \\
& >\frac{\sqrt{6}}{3} \int_{0}^{n} \sqrt{x} \mathrm{~d} x \\
& =\frac{\sqrt{6}}{3} \cdot \frac{2}{3} n^{3 / 2} \\
& =\left(\frac{2 n}{3}\right)^{3 / 2},
\end{aligned}
$$

这就证明了原不等式.

评注 (tastymath75025, AoPS) 注意到当 $x_{k}$ 约为 $\sqrt{\frac{2 k}{3}}$ 时不等式近似取等,故我们应当只采用在此条件下能够取等的放缩. 而条件诱导我们只考虑 $x_{i}$ 附近的项, 则对条件的不等式求和可得 $x_{1} x_{2}+\cdots+x_{k} x_{k+1} \geq k+x_{0}^{2}+x_{1}^{2}+\cdots+x_{k-1}^{2} \geq k+x_{1} x_{2}+\cdots+x_{k-2} x_{k-1}+0.5 x_{k-1}^{2}$.由此不难发现 $\frac{1}{3} x_{k+1}+\frac{2}{3} x_{k} \geq \sqrt{\frac{2 k}{3}}$, 从而整理得到以上略显玄幻的证明.

以上解答由原作者发表于微信小程序“数之谜”的讨论区.
证明 2(biomathematics, AoPS) 对下标 $k=0,1, \ldots, n, n+1$, 称 $k$ 是 “坏的”, 如果 $x_{k} \leq \sqrt{\frac{2 k}{3}}$; 称 $k$ 是 “好的”, 如果 $x_{k}>\sqrt{\frac{2 k}{3}}$. 注意 $k=0$ 是好的.

引理 不存在下标 $k \in\{0,1, \ldots, n\}$ 使得 $k, k+1$ 均是坏的, 且 $k$ 是坏的蕴含

$$
x_{k}+x_{k+1}>\sqrt{\frac{2 k}{3}}+\sqrt{\frac{2 k+1}{3}} .
$$

证明 用反证法. 假设 $k$ 是最小的使得 $k, k+1$ 均坏的下标, 则由 0 好知 $k-1$ 好, 从而

$x_{k+1}+x_{k} \geq \frac{x_{k-1}^{2}+1}{x_{k}}+x_{k} \geq \frac{2 k+1}{3 x_{k}}+x_{k}>\frac{2 k+1}{3 \sqrt{2 k / 3}}+\sqrt{\frac{2 k}{3}}>\sqrt{\frac{2 k}{3}}+\sqrt{\frac{2 k+1}{3}}$,即 $k+1$ 是好的, 矛盾! 假设错误. 以上推导一并证明了 $(*)$. 结论得证.

根据结论, 对任意 $1,2, \ldots, n$ 中坏的下标 $k$, 将其与好的下标 $k+1$ 配对, 则由 $(*)$ 得

$$
\begin{aligned}
x_{0}+x_{1}+\cdots+x_{n}+x_{n+1} & \geq x_{0}+x_{1}+\cdots+x_{n} \\
& \geq \sum_{k=1}^{n} \sqrt{\frac{2 k}{3}}>\left(\frac{2 n}{3}\right)^{3 / 2},
\end{aligned}
$$

这就证明了原不等式.

评注我们首先发现当 $x_{k}$ 约为 $\frac{2 k}{3}$ 时不等式近似取等, 于是自然地考虑 $x_{k}$ 与 $\frac{2 k}{3}$ 的大小关系. 条件提示我们局部来看 $x_{k}$ 是和 $x_{k-1}, x_{k+1}$ 相互关联的, 那么经过一些探索分析可以得到

$$
x_{k} \leq \sqrt{\frac{2 k}{3}} \Longrightarrow x_{k}+x_{k+1}>\sqrt{\frac{2 k}{3}}+\sqrt{\frac{2 k+1}{3}}
$$

这样就能配对放缩证明原不等式了.

本题预计难度 $35 \mathrm{M}$.

A8. 求所有函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意实数 $a, b, c$, 均有 $(f(a)-f(b))(f(b)-f(c))(f(c)-f(a))=f\left(a b^{2}+b c^{2}+c a^{2}\right)-f\left(a^{2} b+b^{2} c+c^{2} a\right)$.

解 所有满足要求的函数 $f$ 为 $f(x) \equiv c$ 或 $\pm x+c$ 或 $\pm x^{3}+c(c \in \mathbb{R})$.

注意到平移 $f$ 仍然满足条件, 故不妨设 $f(0)=0$. 记 $\operatorname{Plug}(a, b, c)$ 为将 $(a, b, c)$ 代入原方程.

情形 1 存在非零实数 $x$ 使得 $f(x)=0$.

此时 $\operatorname{Plug}(x, 0, c) \Rightarrow f\left(x^{2} c\right)=f\left(x c^{2}\right)$, 于是

$$
\operatorname{Plug}\left(x c^{2}, b, x^{2} c\right) \Rightarrow f\left(x c^{2} b^{2}+x^{4} c^{2} b+x^{4} c^{5}\right)=f\left(x^{2} c b^{2}+x^{2} c^{4} b+x^{5} c^{4}\right)
$$

关于 $u$ 的二次方程 $x^{2} c u^{2}+x^{2} c^{4} u+x^{5} c^{4}=0$ 在 $c$ 充分大时有实根, 取 $b$ 为其绝
对值较大的实根, 则

$$
\begin{aligned}
x c^{2} b^{2}+x^{4} c^{2} b+x^{4} c^{5} & =x^{4} c^{2} b+x c^{2}\left(b^{2}+x^{3} c^{3}\right)=x^{4} c^{2} b+x c^{2}\left(-c^{3} b\right) \\
& =\left(x^{4} c^{2}-x c^{5}\right) b \stackrel{\text { def }}{=} g(c) .
\end{aligned}
$$

容易看出 $\lim _{|c| \rightarrow+\infty}|g(c)|=+\infty$, 且 $g(c)$ 是 $c$ 的连续函数 ( $|c|$ 充分大). 又因为

$$
f\left(x c^{2} b^{2}+x^{4} c^{2} b+x^{4} c^{5}\right)=f\left(x^{2} c b^{2}+x^{2} c^{4} b+x^{5} c^{4}\right)=f(0)=0,
$$

所以存在充分大的 $M$ 使得 $\left.f\right|_{(-\infty,-M]} \equiv 0$ 或 $\left.f\right|_{[M,+\infty)} \equiv 0$. 注意以 $f(-x)$ 替换 $f(x)$ 不改变问题, 故不妨设 $\left.f\right|_{[M,+\infty)} \equiv 0$. 对任意正实数 $t$, 取充分小的实数 $c$ 使得 $\min \left\{t c^{-2}, t^{2} c^{-3}\right\}>M$, 则

$$
\begin{gathered}
\operatorname{Plug}\left(t c^{-2}, 0, c\right) \Rightarrow f(t)=f\left(t^{2} c^{-3}\right)=0 \\
\operatorname{Plug}\left(t^{1 / 3}, 0,-t^{1 / 3}\right) \Rightarrow f(-t)=f(t)=0
\end{gathered}
$$

因此由 $t$ 的任意性知在情形 1 下有 $f \equiv 0$, 显然 $f$ 是函数方程的解.

情形 2 不存在非零实数 $x$ 使得 $f(x)=0$.

以下分若干步确定 $f$.

结论 $1 f(1) f(-1)=-1$.

证明 注意到

$$
\operatorname{Plug}(1,0,-1) \Rightarrow f(-1)-f(1)=f(1) f(-1)(f(1)-f(-1))
$$

则 $f(1)=f(-1)$ 或 $f(1) f(-1)=-1$.

若 $f(1)=f(-1)$, 则由 $\operatorname{Plug}(a, 0,1), \operatorname{Plug}(a, 0,-1)$ 得

$f\left(a^{2}\right)-f(a)=f(a) f(1)(f(a)-f(1))=f(a) f(-1)(f(a)-f(-1))=f\left(-a^{2}\right)-f(a)$,

故 $f$ 是偶函数. 于是对任意非零实数 $a$, 取 $c=\frac{\sqrt{5}-1}{2} a$, 则

$$
\operatorname{Plug}(a,-a, c) \Rightarrow f\left(a^{2} c+a^{3}-a c^{2}\right)=f\left(a c^{2}-a^{3}+a^{2} c\right)=f(0)=0
$$

这与 $f(x)=0$ 蕴含 $x=0$ 矛盾! 因此 $f(1) \neq f(-1)$, 故 $f(1) f(-1)=-1$. 结论 1 得证.

结论 2 若 $t \notin\{0, \pm 1\}$, 则 $f(t) f\left(t^{-1}\right)=1$.

证明 注意到

$$
\operatorname{Plug}(a, 0,1) \Rightarrow f\left(a^{2}\right)-f(a)=f(a) f(1)(f(a)-f(1)),
$$

则对满足 $f(a)=f\left(a^{-1}\right)$ 的实数 $a$, 均有

$f\left(a^{2}\right)=f(a)+f(a) f(1)(f(a)-f(1))=f\left(a^{-1}\right)+f\left(a^{-1}\right) f(1)\left(f\left(a^{-1}\right)-f(1)\right)=f\left(a^{-2}\right)$.

不妨设 $|t|>1$. 若 $f(t)=f\left(t^{-1}\right)$, 则存在充分大的正整数 $k$ 使得 $T=t^{2^{k}}>10$,
从而

$$
\begin{gathered}
f(t)=f\left(t^{-1}\right) \Rightarrow f\left(t^{2}\right)=f\left(t^{-2}\right) \Rightarrow \cdots \Rightarrow f(T)=f\left(T^{-1}\right) \\
\operatorname{Plug}\left(x, T, T^{-1}\right) \Rightarrow f\left(x^{2} T+T+x T^{-2}\right)=f\left(x^{2} T^{-1}+T^{-1}+x T^{2}\right)
\end{gathered}
$$

又因为 $T>10$, 所以存在实数 $x$ 使得 $x^{2} T^{-1}+T^{-1}+x T^{2}=0$, 则 $f\left(x^{2} T^{-1}+T^{-1}+x T^{2}\right)=0 \Rightarrow f\left(x^{2} T+T+x T^{-2}\right)=0 \Rightarrow x^{2} T+T+x T^{-2}=0$.

但是两个关于 $x$ 的方程无公共零点, 这是不可能的. 因此 $f(t) \neq f\left(t^{-1}\right)$, 则

$$
\operatorname{Plug}\left(t, 0, t^{-1}\right) \Rightarrow f(t)-f\left(t^{-1}\right)=f(t) f\left(t^{-1}\right)\left(f(t)-f\left(t^{-1}\right)\right)
$$

故 $f(t) f\left(t^{-1}\right)=1$. 结论 2 得证.

结论 $3\{f(1), f(-1)\}=\{1,-1\}$.

证明 由结论 2 得 $f(1)^{2}=f(-1)^{2}=1$. 于是对任意 $a \notin\{0, \pm 1\}$, 均有

$$
\begin{aligned}
\operatorname{Plug}(a, 0,1) & \Rightarrow f\left(a^{2}\right)=f(a) f(1)(f(a)-f(-1)-f(1)), \\
\operatorname{Plug}(a, 0,-1) & \Rightarrow f\left(-a^{2}\right)=f(a) f(-1)(f(a)-f(-1)-f(1))
\end{aligned}
$$

又因为 $f\left(a^{2}\right) f\left(-a^{2}\right) \neq 0$, 所以 $f\left(a^{2}\right) f(-1)=f\left(-a^{2}\right) f(1)$.

设 $t \notin\{0, \pm 1\}$. 若 $f(t)=f\left(-t^{-1}\right)$, 则

$$
\begin{aligned}
f\left(t^{2}\right) & =f(t) f(1)(f(t)-f(-1)-f(1)) \\
& =f\left(-t^{-1}\right) f(1)\left(f\left(-t^{-1}\right)-f(-1)-f(1)\right) \\
& =f\left(t^{-2}\right)
\end{aligned}
$$

这与 $t^{2} \notin\{0, \pm 1\}$ 矛盾! 因此 $f(t) \neq f\left(-t^{-1}\right)$, 则由 $\operatorname{Plug}\left(a^{-2}, 0,-a^{2}\right)$, 得

$$
f\left(a^{-2}\right) f\left(-a^{2}\right)\left(f\left(a^{-2}\right)-f\left(-a^{2}\right)\right)=f\left(-a^{-2}\right)-f\left(a^{2}\right)=\frac{1}{f\left(-a^{2}\right)}-\frac{1}{f\left(a^{-2}\right)}
$$

又因为 $f\left(a^{2}\right) \neq f\left(a^{-2}\right)$, 所以 $f\left(a^{-2}\right) f\left(-a^{2}\right)=\left(f\left(a^{-2}\right) f\left(-a^{2}\right)\right)^{-1}$, 则由结论 2 得

$$
1=f\left(a^{-2}\right)^{2} f\left(-a^{2}\right)^{2}=f\left(a^{-2}\right)^{2}\left(\frac{f(-1)}{f(1)} f\left(a^{2}\right)\right)^{2}=\left(\frac{f(-1)}{f(1)}\right)^{2},
$$

于是由结论 1 得 $\{f(1), f(-1)\}=\{1,-1\}$. 结论 3 得证.

注意到以 $-f(x)$ 替换 $f(x)$ 仍然满足条件, 故不妨设 $f(1)=1, f(-1)=-1$.

结论 $4 f$ 是单射.

证明 假设实数 $a \neq b$ 使 $f(a)=f(b)$, 则 $a b \neq 0$, 由结论 2 , 结论 3 得 $f\left(a^{-1}\right)=f\left(b^{-1}\right)$. 于是

$$
\begin{aligned}
\operatorname{Plug}(a, 0, b) & \Rightarrow f\left(a b^{2}\right)=f\left(a^{2} b\right) \\
\operatorname{Plug}\left(a^{-1}, 0, b^{-1}\right) & \Rightarrow f\left(a^{-2} b^{-1}\right)=f\left(a^{-1} b^{-2}\right)
\end{aligned}
$$

注意到对任意 $x, y \in \mathbb{R}$, 均有

$$
\operatorname{Plug}(x, 0, y) \Rightarrow f(x) f(y)(f(x)-f(y))=f\left(x^{2} y\right)-f\left(x y^{2}\right),
$$

于是

$$
\prod_{c y c}(f(x)-f(y))=\sum_{c y c} f(x) f(y)(f(y)-f(x))=\sum_{c y c} f\left(x y^{2}\right)-f\left(x^{2} y\right) .
$$

在上式中取 $(x, y, z)=\left(a, b, a^{-1} b^{-1}\right)$, 得

$0=f\left(a b^{2}\right)-f\left(a^{2} b\right)+f\left(a^{-2} b^{-1}\right)-f\left(a^{-1} b\right)+f\left(a b^{-1}\right)-f\left(a^{-1} b^{-2}\right)=f\left(a b^{-1}\right)-f\left(a^{-1} b\right)$.

因为在结论 2 , 结论 3 的证明中得到了 $f(t)=f\left(t^{-1}\right)$ 当且仅当 $t \in\{ \pm 1\}$, 所以由 $a \neq b$ 知 $a=-b$. 但结论 3 的证明中又得到了对任意非零实数 $x$ 均有

$$
\frac{f\left(x^{2}\right)}{f\left(-x^{2}\right)}=\frac{f(1)}{f(-1)}=-1
$$

这与 $a=-b$ 矛盾! 因此假设错误, 故 $f$ 是单射. 结论 4 得证.

结论 $5 f(x) f(y)=f(x y)$ 对任意实数 $x, y$ 成立.

证明 根据结论 3 可得

$$
\operatorname{Plug}(a, 0,1) \Rightarrow f\left(a^{2}\right)=f(a)^{2}, \quad \operatorname{Plug}(a, 0,-1) \Rightarrow f\left(-a^{2}\right)=-f(a)^{2}
$$

即 $f$ 是奇函数. 取实数 $a, c$ 使得 $a c \neq 0$ 且 $|a| \neq|c|$, 则

$$
\begin{gathered}
\operatorname{Plug}(a, 0, c) \Rightarrow f(a) f(c)(f(a)-f(c))=f\left(a^{2} c\right)-f\left(a c^{2}\right) \\
\operatorname{Plug}\left(a^{2}, 0, c^{2}\right) \Rightarrow f\left(a^{2}\right) f\left(c^{2}\right)\left(f\left(a^{2}\right)-f\left(c^{2}\right)\right)=f\left(a^{4} c^{2}\right)-f\left(a^{2} c^{4}\right)
\end{gathered}
$$

又因为

$$
\begin{gathered}
f\left(a^{2}\right) f\left(c^{2}\right)\left(f\left(a^{2}\right)-f\left(c^{2}\right)\right)=f(a)^{2} f(c)^{2}(f(a)+f(c))(f(a)-f(c)) \\
f\left(a^{4} c^{2}\right)-f\left(a^{2} c^{4}\right)=f\left(a^{2} c\right)^{2}-f\left(a c^{2}\right)^{2}=\left(f\left(a^{2} c\right)+f\left(a c^{2}\right)\right)\left(f\left(a^{2} c\right)-f\left(a c^{2}\right)\right)
\end{gathered}
$$

所以

$$
\begin{aligned}
f(a) f(c)(f(a)+f(c)) & =\frac{f\left(a^{2}\right) f\left(c^{2}\right)\left(f\left(a^{2}\right)-f\left(c^{2}\right)\right)}{f(a) f(c)(f(a)-f(c))} \\
& =\frac{f\left(a^{4} c^{2}\right)-f\left(a^{2} c^{4}\right)}{f\left(a^{2} c\right)-f\left(a c^{2}\right)} \\
& =f\left(a^{2} c\right)+f\left(a c^{2}\right) .
\end{aligned}
$$

比较上式与

$$
f(a) f(c)(f(a)-f(c))=f\left(a^{2} c\right)-f\left(a c^{2}\right),
$$

得 $f(a)^{2} f(c)=f\left(a^{2} c\right)$, 故 $f\left(a^{2}\right) f(c)=f\left(a^{2} c\right)$. 再注意到 $f$ 是奇函数, 并对 $x, y \in\{0, \pm 1\}$ 作平凡的讨论, 可知 $f(x) f(y)=f(x y)$. 结论 5 得证.
结论 6 存在实数 $\alpha$ 使得 $f(x)=x^{\alpha}$.

证明 由结论 5 与柯西方程的性质, 只需证明当 $0<x<1$ 时 $0 \leq f(x) \leq 1$.显然当 $x>0$ 时 $f(x)=f(\sqrt{x})^{2}>0$.

若存在 $x \in(0,1)$ 使得 $f(x)>1$, 取充分大的正整数 $k$ 使得 $y=x^{k}<0.1$, 则 $f(y)=f(x)^{k}>1$, 且由 $\operatorname{Plug}(1, y,-y)$ 得

$$
f\left(y^{3}+y^{2}-y\right)-f\left(-y^{3}+y^{2}+y\right)=(1-f(y))(f(y)-f(-y))(f(-y)-1) \text {. }
$$

一方面, 由 $0<y<0.1$ 得 $\max \left\{y^{3}+y^{2}-y, y^{3}-y^{2}-y\right\}<0$, 故由 $f$ 是奇函数知

$$
f\left(y^{3}+y^{2}-y\right)-f\left(-y^{3}+y^{2}+y\right)=f\left(y^{3}+y^{2}-y\right)+f\left(y^{3}-y^{2}-y\right)<0 .
$$

另一方面, 由 $f$ 是奇函数以及 $f(y)>1$ 得

$$
(1-f(y))(f(y)-f(-y))(f(-y)-1)=-2 f(y)\left(1-f(y)^{2}\right)>0 \text {. }
$$

两方面相互矛盾, 从而 $x \in(0,1)$ 蕴含 $f(x) \in[0,1]$, 故存在实数 $\alpha$ 使得 $f(x)=$ $x^{\alpha}$. 结论 6 得证.

## 结论 $7 f(2) \in\{2,8\}$.

证明 设实数 $t$ 使得 $f(2)=t^{3}$, 则

$$
\operatorname{Plug}(2,1,-1) \Rightarrow f(-1)-f(5)=(f(2)-f(1))(f(1)-f(-1))(f(-1)-f(2))
$$

从而由结论 3 得 $f(5)=2 t^{6}-3$. 于是由结论 5 得

$$
\begin{aligned}
& \operatorname{Plug}(1, \sqrt[3]{2}, \sqrt[3]{4}) \\
& \Rightarrow f(4 \sqrt[3]{4})-f(5 \sqrt[3]{2})=(1-f(\sqrt[3]{2}))(f(\sqrt[3]{2})-f(\sqrt[3]{4}))(f(\sqrt[3]{4})-1) \\
& \Rightarrow t^{8}-t\left(2 t^{6}-3\right)=(1-t)\left(t-t^{2}\right)\left(t^{2}-1\right)
\end{aligned}
$$

解之得 $t=\sqrt[3]{2}$ 或 2 , 故 $f(2)=2$ 或 8 . 结论 7 得证.

根据结论 6 与结论 7 可知在情形 2 下有 $f(x)= \pm x$ 或 $\pm x^{3}$, 显然 $f$ 是函数方程的解.

综上所述, 满足要求的函数 $f$ 即 $f(x) \equiv c$ 或 $\pm x+c$ 或 $\pm x^{3}+c$, 其中 $c$ 为任意实数.

评注 解决这一题需要不断地将不同的 $(a, b, c)$ 取值代入条件等式以深入挖掘 $f$ 的各种性质. 由于 $f$ 的各种性质都不太直接, 解答就不可避免地像万里长征. 本题需要花费巨量的时间慢慢研究, 但是其实每一步的难度也不高, 逐步考虑 $f(0), f( \pm 1)$ 以及单射, 乘性都是函数方程的常规方法.

本题预计难度 $45 \mathrm{M}$.

C1. 设 $S$ 为正整数 $\mathbb{N}^{*}$ 的无穷子集, 且存在互不相同的 $a, b, c, d \in S$ 使得 $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(c, d)$. 证明: 存在互不相同的 $x, y, z \in S$ 使得

$$
\operatorname{gcd}(x, y)=\operatorname{gcd}(y, z) \neq \operatorname{gcd}(z, x)
$$

证明 用反证法. 假设原题结论不成立.

因为 $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(c, d)$, 所以或者 $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(a, c)$, 或者 $\operatorname{gcd}(a, c) \neq$ $\operatorname{gcd}(c, d)$. 我们不妨假设 $\operatorname{gcd}(a, b) \neq \operatorname{gcd}(a, c)$, 则对于一切 $s \in S \backslash\{a\}$, 数 $\operatorname{gcd}(a, s)$ 有至少两种取值. 又注意到 $\operatorname{gcd}(a, s)$ 有至多有限种取值, 故存在一个值 $x$ 使得存在无穷多个 $s \in S \backslash\{a\}$ 使得 $\operatorname{gcd}(a, s)=x$. 再取 $y \neq x$ 使得存在 $s \in S \backslash\{a\}$ 满足 $\operatorname{gcd}(a, s)=y$, 记

$$
\begin{aligned}
& X=\{s \in S \mid \operatorname{gcd}(a, s)=x\}, \\
& Y=\{s \in S \mid \operatorname{gcd}(a, s)=y\} .
\end{aligned}
$$

因为原题结论不成立, 所以

$$
\begin{array}{ll}
\operatorname{gcd}\left(s_{1}, s_{2}\right)=x & \left(\forall s_{1} \in X, s_{2} \in X, s_{1} \neq s_{2}\right), \\
\operatorname{gcd}\left(s_{1}, s_{2}\right) \neq x & \left(\forall s_{1} \in X, s_{2} \in Y\right) .
\end{array}
$$

于是对于任一固定的 $s \in Y$ 与任一 $s_{1} \in X$, 所有的 $\operatorname{gcd}\left(s, s_{1}\right)$ 两两不同. 然而 $s$为固定的正整数, 其约数只有有限多个, 这是不可能的! 故假设错误, 原命题成立.

评注 解决问题的关键在于观察到 $S$ 中任一数 $s$ 与其它数的最大公约数只有有限多个.

本题预计难度 $15 \mathrm{M}$.

C2. 设正整数 $n \geq 3$. 一条环形项链上串有 $m \geq n+1$ 颗珠子. 小明希望将每颗珠子染为 $n$ 种不同颜色之一, 使得在任何连续 $n+1$ 颗珠子中每种颜色至少出现一次. 求使得小明不能实现愿望的不同正整数 $m$ 的个数.

解 所求不同正整数 $m$ 的个数为 $\mathrm{C}_{n-1}^{2}$.

设 $m=n q+r$, 其中 $q$ 为正整数, 且整数 $r \in[0, n-1]$.

断言 小明的愿望不能实现当且仅当 $r>q$.

证明 一方面, 若 $r>q$, 则由抽庶原理知至少有一种颜色的珠子出现至多 $\left\lfloor\frac{m}{n}\right\rfloor=q$ 次. 若小明可以实现愿望, 则此种颜色的珠子在任意相邻的 $n+1$ 个珠
子中均出现, 其个数不少于

$$
\frac{m}{n+1}=\frac{n q+r}{n+1}>\frac{n q+q}{n+1}=q
$$

矛盾! 故当 $r>q$ 时小明的愿望不能实现. 另一方面, 若 $r \leq q$, 则有以下排法:

首尾相连

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-22.jpg?height=205&width=988&top_left_y=477&top_left_x=540)

容易验证每种颜色的珠子相邻间隔均不超过 $n$ 个其他颜色的珠子, 故此构造满足要求. 断言为真.

回到原题. 容易看出满足 $1 \leq q<r \leq n-1$ 的数组 $(q, r)$ 的个数为

$$
1+2+\cdots+(n-2)=\frac{(n-1)(n-2)}{2}
$$

而每组这样的 $(q, r)$ 恰对应一个 $m$, 故使得小明不能实现愿望的正整数 $m$ 恰有 $\mathrm{C}_{n-1}^{2}$ 个.

评注 我们希望找到一个方便计数的等价条件, 进行一些证明与构造的尝试后不难发现 $r>q$ 等价于小明的愿望不能实现, 于是借助这一刻画本质结构的中间结果问题就解决了.

本题预计难度 $20 \mathrm{M}$.

C3. 两只松鼠 B 和 $\mathrm{J}$ 为过冬收集了 2021 枚核桃. $\mathrm{J}$ 将核桃依次编号为 1 到 2021, 并在它们最喜欢的树周围挖了一圈共 2021 个小坑. 第二天早上, $J$ 发现 $\mathrm{B}$ 已经在每个小坑里放入了一枚核桃, 但并未注意编号. 不开心的 $\mathrm{J}$ 决定用 2021 次操作来改变这些核桃的位置. 在第 $k$ 次操作中, $\mathrm{J}$ 把与第 $k$ 号核桃相邻的两枚核桃交换位置. 证明: 存在某个 $k$, 使得在第 $k$ 次操作中, $\mathrm{J}$ 交换了两枚编号为 $a$ 和 $b$ 的核桃, 且 $a<k<b$.

证明 (陈晨) 假设结论不成立, 在第 $k$ 次操作时将编号为 $k$ 的核桃染色, 那么每次操作交换的两个核桃要么全都被染色, 要么全都没被染色.

考虑相邻且均被染色的核桃对数 $S$ : 在一次操作中, 若交换的核桃均被染色, 则 $S$ 加 2 , 否则 $S$ 不变, 从而 $S$ 的奇偶性始终不变. 然而 $S$ 初值为 0 , 最终变为 2021 , 矛盾! 故假设错误, 结论成立.

评注 以上证明的精髓在于考虑能用上反证假设的染色方式, 从而通过奇偶性导出矛盾.

以上解答是 2021 年中国数学奥林匹克 $(\mathrm{CMO})$ 北京队集训期间陈晨老师讲
授的.

本题预计难度 $30 \mathrm{M}$.

C4. 设 $T$ 是完全有向简单图. 称若干条有向道路组成的集合为不交的,是指其中任何两条道路无公共边 (这里一条道路不能重复经过同一顶点). 设 $v, w$ 为 $T$ 的顶点. 记 $M$ 为从 $v$ 到 $w$ 的不交道路集所含元素个数的最大可能值;记 $N$ 为从 $w$ 到 $v$ 的不交道路集所含元素个数的最大可能值.

证明: $M=N$ 当且仅当 $v, w$ 在 $T$ 中的出度相同.

证明 设 $T=(V, E)$. 对题中所述顶点 $v, w \in V$, 设

$$
\begin{aligned}
& A=\{x \in V \mid v \rightarrow x, w \rightarrow x\}, \\
& B=\{x \in V \mid x \rightarrow v, x \rightarrow w\}, \\
& C=\{x \in V \mid v \rightarrow x, x \rightarrow w\}, \\
& D=\{x \in V \mid x \rightarrow v, w \rightarrow x\} .
\end{aligned}
$$

不妨设 $v \rightarrow w$, 则 $v, w$ 在 $T$ 中的出度相同当且仅当 $|C|+1=|D|$.

设 $P, Q$ 分别为元素最多的从 $v$ 到 $w$, 从 $w$ 到 $v$ 的不交有向道路集, 则 $v \rightarrow w \in P$.

断言 可以不妨假设 $v \rightarrow c \rightarrow w \in P(\forall c \in C), w \rightarrow d \rightarrow v \in Q(\forall d \in D)$.

证明 按有向边 $v \rightarrow c, \rightarrow \rightarrow w$ 是否出现于 $P$ 中讨论:

若 $v \rightarrow c, c \rightarrow w$ 均不在 $P$ 中, 则 $P \cup\{v \rightarrow c \rightarrow w\}$ 仍是不交有向道路集,这与极大性矛盾!

若 $v \rightarrow c, c \rightarrow w$ 恰有一个在 $P$ 中, 不妨设 $v \rightarrow c \rightarrow \cdots \rightarrow w \in P$. 此时在 $P$ 中用 $v \rightarrow c \rightarrow w$ 替换 $v \rightarrow c \rightarrow w$ 所得新的 $P$ 仍满足要求.

若 $v \rightarrow c, c \rightarrow w$ 均在 $P$ 中, 则只需考虑 $v \rightarrow \cdots_{1} \rightarrow c \rightarrow w \in P, v \rightarrow c \rightarrow$ $\cdots_{2} \rightarrow w \in P$ 的情形: 在 $P$ 中用 $v \rightarrow c \rightarrow w$ 和 $v \rightarrow \cdots_{1} \rightarrow c \rightarrow \cdots_{2} \rightarrow w$ (若有重复顶点则删去其间的道路)替换以上两条有向道路所得新的 $P$ 仍满足要求.

综合以上讨论知断言为真.

设

$$
\begin{aligned}
& P^{\prime}=\{v \rightarrow a \rightarrow \cdots \rightarrow b \rightarrow w \in P \mid a \in A, b \in B\}, \\
& Q^{\prime}=\{w \rightarrow a \rightarrow \cdots \rightarrow b \rightarrow v \in Q \mid a \in A, b \in B\} .
\end{aligned}
$$

对有向道路 $v \rightarrow x \rightarrow \cdots \rightarrow y \rightarrow w \in P$ : 或者 $x=y \in C$, 或者 $x \in A, y \in B$,或者 $x=w, y=v$. 因此 $|P|=\left|P^{\prime}\right|+|C|+1$. 类似地可得 $|Q|=\left|Q^{\prime}\right|+|D|$. (注
意“ +1 ”来自 $v \rightarrow w$.

注意到 $(v \rightarrow a \rightarrow \cdots \rightarrow b \rightarrow w) \leftrightarrow(w \rightarrow a \rightarrow \cdots \rightarrow b \rightarrow v)$ 是集合 $P^{\prime}, Q^{\prime}$ 间的双射, 于是

$$
M=N \Leftrightarrow|P|=|Q| \Leftrightarrow\left|P^{\prime}\right|+|C|+1=\left|Q^{\prime}\right|+|D| \Leftrightarrow|C|+1=|D| \text {, }
$$

这等价于 $v$ 与 $w$ 在 $T$ 中的出度相同. 原命题得证.

评注 首先发现可以取出所有形如 $v \rightarrow w, v \rightarrow c \rightarrow w(c \in C)$ 或 $w \rightarrow v(d \in D)$ 的道路而保证能够取到最大值, 从而只要证明其余路径的个数的最大值总是相等的即可. 分类讨论从 $v$ 到 $w$, 从 $w$ 到 $v$ 的路后即可看出如上构造映射的论证方式.

本题预计难度 $30 \mathrm{M}$.

C5. 设正整数 $n>k \geq 1$. 有 $2 n+1$ 名学生围坐一个圆圈 (面向圆心). 每名学生有 $2 k$ 个邻居, 即左手边最近的 $k$ 名同学和右手边最近的 $k$ 名同学. 已知这些学生中有 $n+1$ 名女生和 $n$ 名男生.

证明: 存在一名女生, 其 $2 k$ 个邻居中至少有 $k$ 名女生.

证明 对圆周上的这些学生依次赋值 $a_{1}, \ldots, a_{2 n+1} \in\{ \pm 1\}$, 其中女生 +1 ,男生 -1 . 对任意正整数 $i$, 我们规定 $a_{2 n+1+i}=a_{i}$. 那么, 要证明的命题即: 存在下标 $i_{0}$, 使得 $a_{i_{0}}=1$ 且

$$
\sum_{j=1}^{k}\left(a_{i_{0}-j}+a_{i_{0}+(k+1-j)}\right) \geq 0
$$

对任意正整数 $i$, 设 $t_{i}=a_{i}+a_{i+k}, s_{i}=t_{i}-\frac{2}{2 n+1}$, 则

$$
\sum_{i=1}^{2 n+1} t_{i}=2 \sum_{i=1}^{2 n+1} a_{i}=2, \quad \sum_{i=1}^{2 n+1} s_{i}=\sum_{i=1}^{2 n+1}\left(t_{i}-\frac{2}{2 n+1}\right)=0 .
$$

取 $s_{1}, s_{1}+s_{2}, \cdots, s_{1}+\cdots+s_{n}$ 中最小的一个数, 设为 $s_{1}+\cdots+s_{p}$, 则对任意正整数 $i$, 均有

$$
s_{p+1}+\cdots+s_{p+i}=\left(s_{1}+\cdots+s_{p+i}\right)-\left(s_{1}+\cdots+s_{p}\right) \geq 0 .
$$

因此 $s_{p+1} \geq 0$ 且 $s_{p+1}+\cdots+s_{p+k+1} \geq 0$, 进而 $t_{p+1}>0$ 且 $t_{p+1}+\cdots+t_{p+k+1}>0$.于是

$$
a_{p+1}+a_{p+k+1}=t_{p+1}>0 \Rightarrow a_{p+k+1}=1 .
$$

又因为 $t_{p+1}+\cdots+t_{p+k+1}>0$, 所以

$$
0<t_{p+1}+\cdots+t_{p+k+1}=\sum_{i=1}^{k+1}\left(a_{p+i}+a_{p+i+k}\right)
$$

$$
=2 a_{p+k+1}+\sum_{i=1}^{k}\left(a_{p+i}+a_{p+i+k+1}\right) \equiv 0 \quad(\bmod 2),
$$

故

$$
\sum_{j=1}^{k}\left(a_{(p+k+1)-j}+a_{(p+k+1)+(k+1-j)}\right)=\sum_{i=1}^{k}\left(a_{p+i}+a_{p+i+k+1}\right) \geq 2-2 a_{p+k+1}=0
$$

综合 $(1)(2)$ 知下标 $i_{0}=p+k+1$ 满足要求. 原命题得证.

评注 我们先尝试将题目代数化, 然后尝试采用一些代换或不等式估计解决问题. 在此过程中可以发现题目能够化归到在卡塔兰(Catalan)数的讨论中一个相对熟知的结论，从而解决问题。

本题预计难度 $35 \mathrm{M}$.

C6. 一名猎人与一只隐形兔子在无穷大的方格表上做如下游戏:

(1) 猎人选取正整数 $N$, 并在每个小方格内放置整数根 (至少 1 根至多 $N$ 根) 胡萝卜. 在放置完毕后, 猎人不能再观察方格表中的胡萝卜.

（2）兔子从某一小方格出发，吃掉其中的所有胡萝卜, 并将其所吃胡萝卜的总数报告至猎人.

(3) 在每一轮中, 兔子移到某一相邻 (有公共边) 且有胡萝卜的小方格, 吃掉其中的所有胡萝卜, 并将其所吃胡萝卜的总数报告至猎人.

若兔子不能移动, 或猎人可以确定兔子的初始小方格, 则猎人获胜.

问: 猎人是否有必胜策略?

解 1 结论是肯定的. 我们说明 $N=144$ 满足要求.

以二元数组 $(x, y) \in \mathbb{Z}^{2}$ 表示所有所有方格, 以 $f(x, y)$ 表示 $(x, y)$ 处所放胡萝卜的数量. 构造

$$
f(x, y)=u(x, y)+9 v(x)+18 v(y)+36 w(x, y)+72 w(y, x) .
$$

这里选取 $g$ 为满足 $g(x)=\lceil\sqrt{x}\rceil^{2}-x+1(x \geq 0)$ 的偶函数(注意 $g$ 的值域为 $\left.\mathbb{N}_{+}\right)$, 并定义

$$
\begin{aligned}
& u(x, y)=3(x \bmod 3)+(y \bmod 3)+1 \\
& v(x)= \begin{cases}0, & \text { 若 } x \geq 0 \text { 且 } \sqrt{x} \in \mathbb{Z}, \text { 或 } x<0 \text { 且 } \sqrt{-x} \notin \mathbb{Z}, \\
1, & \text { 若 } x \geq 0 \text { 且 } \sqrt{x} \notin \mathbb{Z}, \text { 或 } x<0 \text { 且 } \sqrt{-x} \in \mathbb{Z},\end{cases} \\
& w(x, y)= \begin{cases}0, & \text { 若 } y \bmod 2 g(x) \in\{0,1, \ldots, g(x)-1\}, \\
1, & \text { 若 } y \bmod 2 g(x) \in\{g(x), g(x)+1, \ldots, 2 g(x)-1\} .\end{cases}
\end{aligned}
$$

容易看出 $u$ 的值域为 $\{1,2, \ldots, 9\}$ 且 $v, w$ 的值域均为 $\{0,1\}$, 从而 $f$ 的值域为 $\{1,2, \ldots, 144\}$.

不妨设兔子始终可以移动. 我们说明如上定义的 $f$ 使猎人总是可以确定兔子的初始位置.

显然猎人可以通过 $f(x, y)$ 的值反解得到其定义式中五个加项

$$
u(x, y), \quad 9 v(x), \quad 18 v(y), \quad 36 w(x, y), \quad 72 w(y, x)
$$

的值. 根据 $u(x, y)$ 的定义亦不难看出猎人总可以确定兔子各步的运动方向(上下左右之一).

不妨设兔子的运动轨迹在 $x$ 轴方向上的投影是无穷集, 则猎人可以根据使得 $v(x)=1$ 的相邻两步之间兔子在 $x$ 轴方向的位移反解得到兔子初始位置的 $x$ 坐标.

假设猎人仍不能唯一确定兔子的初始位置, 那么由于猎人确定了兔子的初始 $x$ 坐标 $x_{0}$, 则必然有两个不同的 $y$ 坐标 $y_{0}$ 与 $y^{\prime}+y_{0}$ ( $y^{\prime}$ 为正整数), 使得 $\left(x_{0}, y_{0}\right)$ 与 $\left(x_{0}, y_{0}+y^{\prime}\right)$ 均为可能的初始位置. 这表明对于无穷多个连续整数 $x$, 均存在 $y$ 使得 $f(x, y)=f\left(x, y+y^{\prime}\right)$, 从而 $w(x, y)=w\left(x, y+y^{\prime}\right)$. 又因为使得 $g(x)=y^{\prime}$ 的 $x$ 坐标两两之差有限, 所以兔子轨迹上的 $x$ 中必存在 $x_{1}$ 使得 $g\left(x_{1}\right)=y^{\prime}$, 故存在 $y$ 使得 $w\left(x_{1}, y\right)=w\left(x_{1}, y+y^{\prime}\right)$, 这与 $w$ 的定义矛盾! 因此猎人可以确定兔子的初始位置.

评注 本解法思路很清晰: 先确定兔子各步的行动方向, 为此构造了 $u$; 再确定兔子初始位置的一个坐标, 为此构造了 $v$; 最后确定兔子初始位置的另一个坐标, 为此构造了 $w$.

解 2(txc, AoPS $)$ 结论是肯定的. 我们说明 $N=8$ 满足要求. 将放置胡萝卜看作给方格染色.

记 8 种颜色分别为 $0 \mathrm{~W}, 0 \mathrm{R}, 0 \mathrm{~B}, 1 \mathrm{~W}, 1 \mathrm{R}, 1 \mathrm{~B}, 2,3$. 构造将分三步: 先对方格标数 $0,1,2,3$ 以初步确定兔子移动方向; 再将部分 0,1 方格染为红 (R) 白(W)蓝(B)色以形成一些“框”，从而将兔子的初始位置锁定在有限个方格内; 最后将其余 0,1 方格染为红蓝两色之一以确定兔子的初始位置.

第 1 步. 在方格 $(x, y)$ 内标数 $\left(x+y^{2}-y\right) \bmod 4$ (下图示意 $-8 \leq x \leq 9$, $-8 \leq y \leq 9$ 的部分), 则猎人可以由奇偶性确定兔子每次移动在水平方向或坚直方向. 猎人虽然不能确定首次坚直移动是向上或向下, 但他可以确定每次坚直移动的方向与上一次是否相同. 故兔子移动的轨迹的可能性只有两种(平移后认
为是同种轨迹), 且这两种轨迹关于水平方向轴对称.

| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |
| 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |

第 2 步. 定义 $B(x, y)$ 为 $(2 x, 2 y),(2 x, 2 y+1),(2 x+1,2 y),(2 x+1,2 y+1)$ 组成的 $2 \times 2$ 区域, 并定义大小为 $k$ 的“框” (称作 “框 $k$ ”) 为全体满足 $|x|+|y|=2 k$ 的 $B(x, y)$ 所成图形. 那么所有框均只含有颜色为 0,1 的格子, 且兔子需要经过框中的方格才能跨过框. 例如,

- 示意图中的黑色粗线即框 0 , 由 $B(0,0)$ 组成;
- 示意图中的粉色粗线即框 1 , 由 $B( \pm 1, \pm 1), B( \pm 2,0), B(0, \pm 2)$ 组成;
- 示意图中的紫色粗线即框 2 , 由满足 $|x|+|y|=4$ 的 16 个 $B(x, y)$ 组成.

对每个 $k \geq 2$, 我们分别将框 $2^{k}-1,2^{k}, 2^{k}+1$ 染为红，白，蓝色. 那么猎人总是知道兔子何时, 从什么方向 (从里向外还是从外向里)跨过了白色的框(若兔子先经过红色框再经过白色框, 则方向是从里向外, 其余情形类似). 当兔子跨出的框比跨入的框至少多两个时, 设兔子当前步数小于 $2^{k}$, 则兔子初始位置必定在框 $2^{k}$ 之内. 这就将兔子的初始位置锁定在了有限个方格之中.

第 3 步. 设兔子可能的初始位置已经被锁定在一个有限集合 $Q$ 中. 只需确保对任意 $q_{1}, q_{2} \in Q$, 在充分远处被染红白蓝色的框只有 $2^{k}, 2^{k} \pm 1$ 时, 可以将某些 0,1 方格适当染为红蓝二色之一, 使得

(a) 两只分别从 $q_{1}, q_{2}$ 出发的兔子保持各步方向相同的行动所经方格的颜色序列不同.

(b) 两只分别从 $q_{1}, q_{2}$ 出发的兔子各步方向水平翻转的行动所经方格的颜色序列不同.
注意处理一对 $q_{1}, q_{2}$ 之后要将所涉及最远框之内所有未染色的 0,1 方格染红继而处理下一对 $q_{1}, q_{2}$.

先解决(a). 固定 $q_{1}, q_{2} \in Q$, 定义向量 $v=q_{2}-q_{1}=(s, t)$, 记 $a=|s|+|t|$.取 $k>a$ 充分大且使框 $k-a, k-a+1, \ldots, k+a$ 均尚未被染色. 若方格 $q$ 在框 $k$ 中, 则方格 $q+v$ 或者标有 2 或 3 , 或者在框 $k-a, k-a+1, \ldots, k+a$ 中. 以上述 $2 a+1$ 个框中的全体小方格为顶点构作图 $G$, 并在其中所有形如 $q, q+v$ 的顶点对之间连边. 那么 $G_{1}$ 形如若干条无公共顶点道路之并, 于是可以适当对这些框中的方格染红蓝二色之一, 使得任何相差向量 $v$ 的两个方格颜色不同. 此时, 从 $q_{1}$ 出发的兔子到达框 $k$ 中的方格 $q$ 时, 从 $q_{2}$ 出发的兔子到达 $q+v$, 其颜色或标数与 $q$ 不同. 这就解决了(a).

再类似地解决 (b). 记 $u=(x, y)$ 的共轭 $\bar{u}=(x,-y)$. 固定 $q_{1}^{\prime}, q_{2}^{\prime} \in Q$, 记 $v^{\prime}=q_{2}^{\prime}-\overline{q_{1}^{\prime}}=\left(s^{\prime}, t^{\prime}\right)$, 记 $a^{\prime}=\left|s^{\prime}\right|+\left|t^{\prime}\right|$. 取 $k^{\prime}>a^{\prime}$ 充分大且使框 $k^{\prime}-a^{\prime}, k^{\prime}-a^{\prime}+$ $1, \ldots, k^{\prime}+a^{\prime}$ 均尚未被染色. 这样一来当从 $q_{1}^{\prime}$ 出发的兔子到达 $q^{\prime}$ 时, 从 $q_{2}^{\prime}$ 出发的兔子恰到达 $\overline{q^{\prime}}+q_{2}^{\prime}-\overline{q_{1}^{\prime}}=\overline{q^{\prime}}+v^{\prime}$. 若方格 $q^{\prime}$ 在框 $k$ 中, 则方格 $\overline{q^{\prime}}+v^{\prime}$ 或者标有 2 或 3 , 或者在框 $k^{\prime}-a^{\prime}, k^{\prime}-a^{\prime}+1, \ldots, k^{\prime}+a^{\prime}$ 中. 以上述 $2 a^{\prime}+1$ 个框中的全体小方格为顶点构作图 $G^{\prime}$, 并在其中所有形如 $q^{\prime}, \overline{q^{\prime}}+v^{\prime}$ 的顶点对之间连边. 则 $G^{\prime}$ 形如互不相交的若干条道路, 若干条二重边与若干个自环之并. 事实上, 如果 $q^{\prime}$ 处有一个自环, 那么 $q_{1}^{\prime}$ 与 $q_{2}^{\prime}$ 的横坐标相同, 且 $q^{\prime}$ 在 $q_{1}^{\prime}, q_{2}^{\prime}$ 的中垂线上. 此时 $q_{1} \rightarrow q^{\prime}$ 与 $q_{2} \rightarrow q^{\prime}$ 所经颜色序列一定不同(这由第 1 步保证, 从示意图上不难看出). 于是不妨删去 $G^{\prime}$ 中的所有自环, 从而可以对这些框中的方格染红蓝二色之一, 使得任意先取共轭再按 $v^{\prime}$ 平移的两个方格颜色不同. 这就解决了 (b).

评注 本解法的巧妙之处在于将兔子的初始位置控制在有限个方格内之后,充分利用此有界性, 不断膨胀向外地染色来确保能唯一定下兔子的初始位置.此外, 不难看出 $N=4$ 不满足要求. 笔者不知道 $N=5,6,7$ 是否存在构造, 而 $N=8$ 疑为目前所知使猎人能确保获胜的 $N$ 中最小的.

本题预计难度 $40 \mathrm{M}$.

C7. 设正整数 $m>1$, 考虑一个 $3 m \times 3 m$ 的方格棋盘.一只青蛙从位于左下角的方格 $S$ 出发去右上角的方格 $F$, 它每一步向右或向上跳一个方格. 有一些方格是陷阱, 一旦青蛙到达陷阱方格就会被困住. 称若干个方格组成的集合 $X$ 为障碍集, 如果当 $X$ 中的所有方格均为陷阱时青蛙无法从 $S$ 出发到达 $F$. 称一个障碍集为极小的, 是指它的任何非空真子集均不是障碍集.
(a) 证明: 存在一个由至少 $3 m^{2}-3 m$ 个方格组成的极小障碍集.

(b) 证明: 每个极小障碍集均由不超过 $3 m^{2}$ 个方格组成.

证明 将棋盘看作 $T=\left\{(x, y) \in \mathbb{Z}^{2} \mid 1 \leq x, y \leq 3 m\right\}$, 其中 $S=(1,1), F=$ $(3 m, 3 m)$.

(a) 考虑障碍集 $X=X_{1} \cup X_{2} \cup X_{3}$ ，其中

$$
\begin{aligned}
& X_{1}=\{(2, y) \in T \mid y \in\{3,6, \ldots, 3 m\}\}, \\
& X_{2}=\{(x, y) \in T \mid x \in\{3,4, \ldots, 3 m-2\}, y \in\{2,5, \ldots, 3 m-1\}\}, \\
& X_{3}=\{(3 m-1, y) \in T \mid y \in\{1,4, \ldots, 3 m-2\}\} .
\end{aligned}
$$

容易看出 $X$ 是极小障碍集, 且 $|X|=3 m^{2}-2 m \geq 3 m^{2}-3 m$. 当 $m=3$ 时 $X$ 如下图所示:

|  | $X_{1}$ |  |  |  |  |  |  | $F$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | $X_{2}$ | $X_{2}$ | $X_{2}$ | $X_{2}$ | $X_{2}$ |  |  |
|  |  |  |  |  |  |  | $X_{3}$ |  |
|  | $X_{1}$ |  |  |  |  |  |  |  |
|  |  | $X_{2}$ | $X_{2}$ | $X_{2}$ | $X_{2}$ | $X_{2}$ |  |  |
|  |  |  |  |  |  |  | $X_{3}$ |  |
|  | $X_{1}$ |  |  |  |  |  |  |  |
|  |  | $X_{2}$ | $X_{2}$ | $X_{2}$ | $X_{2}$ | $X_{2}$ |  |  |
| $S$ |  |  |  |  |  |  | $X_{3}$ |  |

(b) 称一列方格 $C=C_{1} C_{2} \cdots C_{6 m-1}$ 为路径, 若对诸下标 $i$ 均有 $C_{i+1}$ 为 $C_{i}$ 的右侧或上方邻格, 且 $C_{1}=S, C_{6 m-1}=F$. 任取一极小障碍集 $A$. 根据极小障碍集的定义, 对任意方格 $P \in A$ 均存在路径 $C_{P}$ 使得 $C_{P} \cap A=\{P\}$ (若存在多个路径则任取一个). 设从 $P$ 沿 $C_{P}$ 走到 $S$ 第一次下行所至格子为 $M_{P}$, 从 $P$ 沿 $C_{P}$ 走到 $F$ 第一次上行所至格子为 $N_{P}\left(M_{P}, N_{P}\right.$ 未必存在), 那么:

- $M_{P}, N_{P} \notin A$. 这是因为 $C_{P} \cap A=\{P\}$.
- $\left\{M_{P} \mid P \in A\right\} \cap\left\{N_{Q} \mid Q \in A\right\}=\varnothing$. 否则存在不经过 $A$ 的路径 $S \rightarrow M_{P}=N_{Q} \rightarrow F$.
- $P \mapsto M_{P}$ 与 $P \mapsto N_{P}$ 在定义域上均为单射. 这是因为 $P$ 是 $M_{P}$ 上一格向右所至首个 $A$ 中的格子, 从而由 $M_{P}$ 唯一确定. 因此 $P \mapsto M_{P}$ 在定义域上是单射. 对 $P \mapsto N_{P}$ 也是类似的.
- 使得 $M_{P}, N_{P}$ 不存在的 $P$ 分别至多有一个. 由 $A$ 的极小性知

$$
|A \cap\{(x, y) \in T \mid y=1\}| \leq 1
$$

从而使得 $M_{P}$ 不存在的 $P$ 至多有一个. 对 $N_{P}$ 也是类似的.

综合以上讨论, 根据 $A \cup\left\{M_{P} \mid P \in A\right\} \cup\left\{N_{Q} \mid Q \in A\right\} \subseteq T$ 考虑元素个数
即有 $|A| \leq 3 m^{2}$.

评注 先经过一段时间的探索尝试后可以找出可行的构造, 从而解决(a). 而后 (b) 的数字特征与 (a) 的极值结构启发我们将棋盘分成三个区, 进而通过构造单射完成证明.

本题预计难度 $35 \mathrm{M}$.

C8. 求最大的正整数 $N$, 使得存在 $N$ 行 100 列的正整数数表 $\left(t_{i, j}\right)_{N \times 100}$, 满足:

(1) 每行的 100 个数 $t_{i, 1}, t_{i, 2}, \ldots, t_{i, 100}(1 \leq i \leq N)$ 均为 $1,2, \ldots, 100$ 的排列.

(2) 对任意不同的两行 $r, s$, 均存在一列 $c$, 使得 $\left|t_{r, c}-t_{s, c}\right| \geq 2$.

解 (徐子健) 所求最大的正整数 $N=\frac{100 !}{2^{50} \text {. }}$

一方面, 我们说明 $N \leq \frac{100 !}{2^{50}}$.

对 $1,2, \ldots, 100$ 的排列 $\sigma_{1}, \sigma_{2}$, 记 $\sigma_{1} \sim \sigma_{2}$, 如果在 $(1,2),(3,4), \ldots,(99,100)$ 中可以选出若干对, 使得在 $\sigma_{1}$ 中分别对换这些数对后所得的排列即 $\sigma_{2}$. 容易看出 $\sim$ 是等价关系, 并将 $1,2, \ldots, 100$ 的所有排列划分为 $\frac{100 !}{2^{50}}$ 个等价类. 而条件(2)表明不存在 $r \neq s$ 使得行向量 $\boldsymbol{t}_{r} \sim \boldsymbol{t}_{s}$, 故 $N \leq \frac{100 !}{2^{50}}$.

另一方面, 我们对正整数 $k$ 与 $N_{k}=\frac{(2 k) !}{2^{k}}$ 归纳构造 $N_{k}$ 行 $2 k$ 列的数表 $\left(t_{i, j}\right)_{N_{k} \times 2 k}$, 满足:

(1') 每行的 100 个数 $t_{i, 1}, t_{i, 2}, \ldots, t_{i, 100}\left(1 \leq i \leq N_{k}\right)$ 均为 $1,2, \ldots, 2 k$ 的排列.

(2') 对任意不同的两行 $r, s$, 均存在一列 $c$, 使得 $\left|t_{r, c}-t_{s, c}\right| \geq 2$.

当 $k=1$ 时易见数表 $(1,2)$ 满足要求. 假设 $k$ 的情形已经构造, 考虑 $k+1$ 的情形:

考虑 $k$ 的情形下构造的数表 $T$, 其每一行均构成 $1,2, \ldots, 2 k$ 的排列. 我们对 $T$ 的每一行插入数 $2 k+1,2 k+2$, 使得它们与 $2 k$ 三个数的排列顺序为

$$
2 k, 2 k+1,2 k+2, \quad 2 k+1,2 k+2,2 k, \quad 2 k+2,2 k, 2 k+1
$$

三者之一. 这一插入的过程也可以看作在一行 $2 k+2$ 个位置中先制定 $2 k+1$, $2 k+2$ 的位置(但不指定顺序), 然后将原 $T$ 中的排列顺次放入其余 $2 k$ 个位置(这个排列唯一决定了 $2 k+1,2 k+2$ 的顺序). 因此, 在以上操作过程中 $T$ 的每一行对应 $\mathrm{C}_{2 k+2}^{2}$ 个 $1,2, \ldots, 2 k+2$ 的排列. 以这些排列构作新的数表 $T^{\prime}$, 则它的行数为 $T_{k} \cdot \mathrm{C}_{2 k+2}^{2}=T_{k+1}$, 且 $T^{\prime}$ 显然满足 $\left(1^{\prime}\right)$.

下面, 我们说明 $T^{\prime}$ 满足 $\left(2^{\prime}\right)$, 从而完成归纳构造.
用反证法. 假设 $T^{\prime}$ 中的 $\boldsymbol{t}_{r}^{\prime}, \boldsymbol{t}_{s}^{\prime}$ 两行不满足 $\left(2^{\prime}\right)$, 设 $t_{r, i_{1}}=t_{s, j_{1}}=2 k+1, t_{r, i_{2}}=$ $t_{s, j_{2}}=2 k+2$.

- 若 $\left\{i_{1}, i_{2}\right\}=\left\{j_{1}, j_{2}\right\}$, 则由归纳假设知存在 $c \in\{1,2, \cdots, 2 k+2\} \backslash\left\{i_{1}, i_{2}\right\}$ 满足 $\left(2^{\prime}\right)$, 矛盾!
- 若 $\left\{i_{1}, i_{2}\right\} \neq\left\{j_{1}, j_{2}\right\}$.

若 $i_{2}=j_{2}$, 则 $i_{1} \neq j_{1}$, 从而 $t_{r, j_{1}}=t_{s, i_{1}}=2 k$, 这与 $2 k, 2 k+1,2 k+2$ 的排列顺序矛盾!

若 $i_{2} \neq j_{2}$, 则 $i_{2} \neq j_{1}$ 或 $j_{2} \neq i_{1}$, 从而分别有 $c=i_{2}$ 或 $c=j_{2}$ 满足 $\left(2^{\prime}\right)$, 矛盾!

综上所述, 满足要求的最大正整数 $N=\frac{100 !}{2^{50} \text {. }}$

评注 本题的证明部分相对平凡, 主要难点在于大胆猜测这一平凡的上界可以取到并尝试构造. 经过对较小情形 (4 列, 6 列)的一些探索, 我们最终发现可以通过仅考虑插入 $2 k+1,2 k+2$ 并适当控制相对顺序生成新数表. 事实上, 这里插入的规则就是控制 $2 k, 2 k+1,2 k+2$ 的圆排列顺序, 从而使得当 $2 k+1,2 k+2$位置不同时只考虑 $2 k, 2 k+1,2 k+2$ 三个数就能验证条件 (2).

本题预计难度 $40 \mathrm{M}$.

## 三、几何

G1. 如图, 在平行四边形 $A B C D$ 中, $A C=B C, P$ 在线段 $A B$ 的延长线上. 已知 $\triangle A C D$ 的外接圆与线段 $P D$ 交于另一点 $Q$, 且 $\triangle A P Q$ 的外接圆与线段 $P C$ 交于另一点 $R$. 证明: $C D, A Q, B R$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-31.jpg?height=606&width=619&top_left_y=1793&top_left_x=707)

证明 延长 $R B$ 交 $\triangle A P Q$ 的外接圆于 $G$, 由于

$$
\angle A R C=\pi-\angle A R P=\pi-\angle A Q P=\angle A Q D=\angle A C D=\angle A B C
$$

故 $A, B, R, C$ 四点共圆. 因此 $\angle G A P=\angle G R P=\angle B A C$.

又注意到 $2 \angle B A C+\angle A B C=\pi$, 故 $G, A, D$ 三点共线.

于是有 $\angle A G R=\angle A P R=\pi-\angle D C P$, 故 $C, R, G, D$ 四点共圆.

对三圆 $(A D C Q),(A R P G),(C R G D)$ 由根心定理即知 $C D, A Q, G R$ 三线共点.

评注 直接从结论往回推需要的条件, 最终推到 $A, B, R, C$ 四点共圆, 通过导角证明即可.

本题预计难度 $10 \mathrm{M}$.

G2. 如图, 圆 $\Gamma$ 的圆心为点 $I$. 凸四边形 $A B C D$ 满足: 线段 $A B, B C, C D$, $D A$ 都与 $\Gamma$ 相切. 设 $\Omega$ 是过 $A, I, C$ 三点的圆. 延长 $B A$ 交 $\Omega$ 于点 $X$, 延长 $B C$ 交 $\Omega$ 于点 $Z$, 延长 $A D$ 交 $\Omega$ 于点 $Y$, 延长 $C D$ 交 $\Omega$ 于点 $T$. 证明:

$$
A D+D T+T X+X A=C D+D Y+Y Z+Z C .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-32.jpg?height=614&width=805&top_left_y=1212&top_left_x=614)

证明 设圆 $I$ 与 $A B, B C, C D, D A$ 分别相切于点 $E, F, G, H$, 则由 $\angle E X I=$ $\angle H Y I$ 可知 $\triangle E X I \cong \triangle H Y I$, 即 $E X=H Y$. 同理可得 $F Z=G T$. 注意到

$$
\begin{aligned}
E X+G T & =A X+A E+D R+D T \\
& =A X+D T+(A H+D H) \\
& =A X+D T+A D,
\end{aligned}
$$

同理 $H Y+F Z=C D+D Y+Z C$, 故

$$
A X+D T+A D=C D+D Y+Z C
$$

只需证明 $T X=Y Z$.
因为 $A I$ 平分 $\angle X A Y$ 的外角, 所以 $I$ 为弧 $(X A Y)$ 的中点. 同理 $I$ 为弧 $(Z A T)$ 的中点, 故 $T X=Y Z$.

评注 作出内切圆在四边形 $A B C D$ 上的四个切点后经观察发现 $\triangle E X I \cong$ $\triangle H Y I$, 转化线段长度后会注意到只需证明 $T X=Y Z$, 这比较容易.

本题预计难度 $20 \mathrm{M}$.

G3. 考虑 $100 \times 100$ 的单位点阵 $\mathbf{L}($ 即 $|\mathbf{L}|=10000$ ). 设 $\mathcal{F}$ 是由若干多边形组成的集合, 满足:

(1) 每个 $\mathcal{F}$ 中多边形的所有顶点均落在 $\mathbf{L}$ 中;

(2) 每个 $\mathbf{L}$ 中的点恰作为一个 $\mathcal{F}$ 中多边形的顶点.

求 $\mathcal{F}$ 中所有多边形面积之和 $S$ 的最大可能值.

解 所求 $S$ 的最大可能值为 8332500 .

设点阵 $\mathbf{L}=\{(i, j) \mid 1 \leq i, j \leq 100\}$. 定义点 $O=\left(\frac{101}{2}, \frac{101}{2}\right)$.

一方面, 考虑所有顶点在 $\mathbf{L}$ 中且关于点 $O$ 中心对称的正方形构成的集合 $\mathcal{F}$, 则

$$
\begin{aligned}
S & =\sum_{i=1}^{50} \sum_{j=0}^{2 i-2}\left(\sqrt{j^{2}+(2 i-1-j)^{2}}\right)^{2} \\
& =0^{2} \cdot 50+\sum_{j=1}^{99} j^{2}(100-j) \\
& =100 \sum_{j=1}^{99} j^{2}-\sum_{j=1}^{99} j^{3} \\
& =8332500 .
\end{aligned}
$$

另一方面, 对于 $\mathcal{F}$ 中任意一个多边形 $A_{1} A_{2} \cdots A_{k}$, 记 $A_{k+1}=A_{1}$, 则

$$
\begin{aligned}
S_{A_{1} A_{2} \cdots A_{k}} & \leq \sum_{i=1}^{k} S_{\triangle O A_{i} A_{i+1}} \leq \sum_{i=1}^{k} \frac{1}{2}\left|O A_{i}\right|\left|O A_{i+1}\right| \\
& \leq \sum_{i=1}^{k} \frac{\left|O A_{i}\right|^{2}+\left|O A_{i+1}\right|^{2}}{4}=\frac{1}{2} \sum_{i=1}^{k}\left|O A_{i}\right|^{2} .
\end{aligned}
$$

因此

$$
S \leq \frac{1}{2} \sum_{A \in \mathbf{L}}|O A|^{2}=100 \sum_{i=1}^{100}\left(i-\frac{101}{2}\right)^{2}=8332500 .
$$

综上, 所求 $\mathcal{F}$ 中所有多边形面积之和 $S$ 的最大可能值为 8332500 .

评注 进行一些探索后发现最大值应该在所有多边形均为关于点 $O$ 中心对
称的正方形时取到，这启发我们采取在此构造下能够取等的放缩方式. 经过一些尝试不难得到以上证明.

本题预计难度 $25 \mathrm{M}$.

G4. 如图, 四边形 $A B C D$ 内接于圆 $\Omega$. 过点 $D$ 作 $\Omega$ 的切线分别与射线 $B A, B C$ 交于点 $E, F$. 已知 $\triangle A B C$ 内一点 $T$ 满足 $T E / / C D, T F / / A D$. 线段 $D F$ 内一点 $K$ 满足 $T D=T K$. 证明: $A C, D T, B K$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-34.jpg?height=714&width=746&top_left_y=697&top_left_x=652)

证明 1 延长 $B D$ 交 $\triangle B E F$ 的外接圆于 $S$. 由

$$
\angle E F S=\angle E B S=\angle A D E=\angle T F E, \quad \angle F E S=\angle F B S=\angle C D F=\angle T E F
$$

可知 $S$ 为 $T$ 关于 $E F$ 的对称点, 四边形 $T D S K$ 为菱形.

设 $A C$ 与 $B K$ 交于 $P$. 考虑以 $B$ 为中心, 以 $\frac{B D}{B S}$ 为位似比的位似变换 $\varphi$.

设 $\varphi(A)=X, \varphi(C)=Y, X Y$ 交 $E F$ 于 $K^{\prime}$. 则 $B, X, S, Y$ 四点共圆. 于是

$$
\angle X Y S=\angle X B S=\angle E F S
$$

故 $K^{\prime}, Y, F, S$ 四点共圆. 同理有 $K^{\prime}, X, E, S$ 四点共圆. 故

$$
\angle X K^{\prime} S+\angle Y K^{\prime} S=\angle X E S+\pi-\angle Y E S=\pi,
$$

从而 $X, K^{\prime}, Y$ 三点共线. 于是

$$
\angle S D K^{\prime}=\angle B D E=\angle B C D=\angle B Y G=\angle S K^{\prime} D,
$$

因此 $S D=S K^{\prime}$, 则 $K=K^{\prime}, \varphi(P)=K$, 即 $\angle B D P=\angle B S K=\angle B D T$, 故 $B, P, T$ 三点共线.

评注 本解法的关键在于注意到 $T$ 关于 $E F$ 的对称点恰是 $B D$ 与 $\triangle B E F$ 外接圆的交点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-35.jpg?height=465&width=1311&top_left_y=207&top_left_x=384)

证明 2 (陳誼廷) 连 $B D$. 在圆 $\Omega$ 取一点 $W \neq B$ 使得 $B W / / E F$. 设 $A C$ 与 $D W$ 交于点 $X$.

对圆 $\Omega$ 内接六点形 $A B W D D C$, 由帕斯卡 (Pascal) 定理得 $E X, B W, C D$ 三线共点(设为 $Y$ ).

对圆 $\Omega$ 内接六点形 $C B W D D A$, 由帕斯卡 (Pascal) 定理得 $F X, B W, A D \equiv$线共点(设为 $Z$ ).

因为 $E T / / D Y, F T / / D Z, E F / / Y Z$, 所以 $\triangle D Y Z$ 与 $\triangle T E F$ 关于中心 $E Y \cap F Z=X$ 位似, 故 $D, X, T$ 三点共线, 从而 $D, X, T, W$ 四点共线. 注意到 $D B=D W, T K=T D$, 于是在上述位似变换下 $B, K$ 为对应点, 故 $B, X, K$ 三点共线, 原命题得证.

评注 (陳谊廷) 观察图形发现将 $D T$ 延长到 $\Omega$ 上后得到的交点 $W$ 似乎满足 $B W / / D D$, 之后自然地尝试使用帕斯卡(Pascal)定理得到点 $Y, Z$, 这就不难完成证明了。

以上解答由原作者发表于 AoPS 线上论坛的讨论区.

本题预计难度 $25 \mathrm{M}$.

G5. 如图, 边长两两不等的四边形 $A B C D$ 内接于圆 $\Omega$ (圆心为 $O$ ), 角 $\angle A B C, \angle A D C$ 的平分线分别与对角线 $A C$ 交于 $B_{1}, D_{1}$ 两点. 圆 $\omega_{B}$ 过点 $B$ 且与 $A C$ 相切于点 $D_{1}$, 圆 $\omega_{D}$ 过点 $D$ 且与 $A C$ 相切于点 $B_{1}$. 设 $\omega_{B}, \omega_{D}$ 的圆心分别为 $O_{B}, O_{D}$. 证明: 若 $B D_{1} / / B_{1} D$, 则 $O_{B}, O, O_{D}$ 三点共线.

证明 1 设 $\omega_{B}, \omega_{D}$ 分别再交 $\Omega$ 于 $P, Q$ 两点. 延长 $B B_{1}, D D_{1}, B D_{1}, P D_{1}$, $D B_{1}, Q B_{1}$ 分别交 $\Omega$ 于 $M, N, I, J, L, R$ 六点. 设 $M N$ 交 $A C$ 于 $K$, 则 $K$ 是线段 $A C$ 的中点.

由 $\angle R L B_{1}=\angle D Q B_{1}=\angle D B_{1} C$ 可知 $R L / / A C$, 同理有 $I J / / A C$. 对圆内接六边形 $M N D L I B$ 由帕斯卡(Pascal) 定理知 $B_{1}, D_{1}, M N \cap L I$ 三点共线, 即
$M N, L I, B_{1} D_{1}$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-36.jpg?height=748&width=834&top_left_y=303&top_left_x=605)

又注意到 $M N, B_{1} D_{1}$ 交于 $K$, 故 $L, I, K$ 三点共线. 结合 $B_{1} L / / D_{1} I$ 即有 $\triangle L B_{1} K \sim \triangle I D_{1} K$. 又因为 $\triangle L R K \sim \triangle I J K$, 故四边形 $L R K B_{1} \sim$ 四边形 $I J K D_{1}$. 因此 $\triangle L R B 1 \sim \triangle I J D_{1}$, 且

$$
\angle P B D_{1}=\angle I J D_{1}=\angle L R B_{1}=\angle Q D B_{1} .
$$

而 $B D_{1} / / D B_{1}$, 故 $B P / / D Q$. 注意到 $O O_{B} \perp B P, O O_{D} \perp D Q$, 故 $O_{B}, O, O_{D}$ 三点共线.

评注 我们想证明 $B P / / D Q$, 而这进一步地需要 $\triangle D Q B_{1} \sim \triangle B P D_{1}$. 注意到 $I J / / A C / / L R$, 故 $\triangle R L B_{1}$ 与 $\triangle J I D_{1}$ 的这组旋转 $180^{\circ}$ 的相似是相对容易证明的. 通过帕斯卡 (Pascal) 定理我们最终证明了这组相似, 从而证明了原命题.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-36.jpg?height=645&width=651&top_left_y=1862&top_left_x=705)

证明 2(东紫昭) 用复数法. 这里用同一字母表示点与该点其对应的复数.
引理 若单位圆上的两条弦 $A B$ 与 $C D$ 交于点 $X$, 则

$$
X=\frac{A B(C+D)-C D(A+B)}{A B-C D} .
$$

证明 参见 [2, Theorem 6.17]. (单位圆上两弦的交点公式在复平面解析法中经常用到.)

设弧 $(A D C)$ 的中点为 $M$, 弧 $(A B C)$ 的中点为 $N$. 以 $O$ 为圆心, 以 $\Omega$ 为单位圆建立复平面. 设 $N=1$, 则 $M=-1, C=\bar{A}$. 由引理得

$$
\begin{aligned}
& B_{1}=A C \cap B M=\frac{B-1+B(A+\bar{A})}{1+B}, \\
& \overline{B_{1}}=\frac{\frac{1}{B}-1+\frac{1}{B}(A+\bar{A})}{1+\frac{1}{B}}=\frac{1-B+(A+\bar{A})}{B+1}, \\
& D_{1}=A C \cap D N=\frac{D+1-D(A+\bar{A})}{1-D} \\
& \overline{D_{1}}=\frac{\frac{1}{D}+1+\frac{1}{D}(A+\bar{A})}{1-\frac{1}{D}}=\frac{1+D-(A+\bar{A})}{D-1} .
\end{aligned}
$$

下面计算 $O_{D}$. 设 $D B_{1}$ 的中点为 $K$. 由于 $O_{D} B_{1} \perp A C$, 故

$$
O_{D}-B_{1} \in \mathbb{R}, \quad O_{D}-B_{1}=\overline{O_{D}-B_{1}}
$$

又由于 $O_{D} K \perp B_{1} D$, 故 $\frac{O_{D}-K}{B_{1}-D}$ 为纯虚数, $\frac{O_{D}-K}{B_{1}-D}=-\frac{\overline{O_{D}-K}}{\overline{B_{1}-D}}$. 代入 $K=\frac{B_{1}+D}{2}$ 并化简得

$$
O_{D} \overline{\left(B_{1}-D\right)}+\overline{O_{D}}\left(B_{1}-D\right)=\frac{1}{2}\left(B_{1}+D\right) \overline{\left(B_{1}-D\right)}+\frac{1}{2} \overline{\left(B_{1}+D\right)}\left(B_{1}-D\right)
$$

联立

$$
\left\{\begin{array}{l}
O_{D}-\overline{O_{D}}=B_{1}-\overline{B_{1}} \\
O_{D} \cdot \overline{\frac{B_{1}-D}{B_{1}-D}}+\overline{O_{D}}=\frac{1}{2} \frac{\left(B_{1}+D\right) \overline{\left(B_{1}-D\right)}}{B_{1}-D}+\frac{1}{2} \overline{\left(B_{1}+D\right)}
\end{array}\right.
$$

并消去 $\overline{O_{D}}$ 得

$$
O_{D} \cdot \frac{B_{1}-D+\overline{B_{1}-D}}{B_{1}-D}=B_{1}-\overline{B_{1}}+\frac{1}{2} \frac{\left(B_{1}+D\right) \overline{\left(B_{1}-D\right)}}{B_{1}-D}+\frac{1}{2} \overline{\left(B_{1}+D\right)},
$$

即

$$
\begin{aligned}
O_{D} & =\frac{\left(\left(B_{1}-\overline{B_{1}}\right)\left(B_{1}-D\right)+\frac{1}{2}\left(B_{1} \overline{B_{1}}+D \overline{B_{1}}-\overline{D B_{1}}-D \bar{D}+B_{1} \overline{B_{1}}-D \overline{B_{1}}+\bar{D} B_{1}-D \bar{D}\right)\right)}{B_{1}-D+\overline{B_{1}-D}}\left(B_{1}^{2}-B_{1} D+D \overline{B_{1}}-D \bar{D}\right) \\
& =\frac{1}{B_{1}+\overline{B_{1}}-D-\bar{D}}\left(\left(B_{1}+1\right)\left(B_{1}-1\right)+D\left(\overline{B_{1}}-B_{1}\right)\right) \\
& \left.=\frac{1}{A+\bar{A}-D-\bar{D}}\right) \\
& =\frac{1}{A+\bar{A}-D-\bar{D}}\left(\frac{B(A+\bar{A}+2)}{B+1} \cdot \frac{B(A+\bar{A})-2}{B+1}+D \cdot \frac{(1-B)(2+A+\bar{A})}{B+1}\right) \\
& =\frac{A D}{(A-D)(A D-1)} \cdot \frac{2+A+\bar{A}}{B+1} \cdot\left(\frac{B(B(A+\bar{A})-2)}{B+1}+D(1-B)\right) .
\end{aligned}
$$

类似地, 可算出

$$
O_{B}=\frac{A B}{(A-B)(A B-1)} \cdot \frac{A+\bar{A}-2}{D-1} \cdot\left(\frac{D(D(A+\bar{A})-2)}{D-1}-B(D+1)\right) .
$$

记

$$
\begin{array}{ll}
d_{1}=\frac{A D}{(A-D)(A D-1)}, & d_{2}=\frac{2+A+\bar{A}}{B+1}, \quad d_{3}=\left(\frac{B(B(A+\bar{A})-2)}{B+1}+D(1-B)\right), \\
b_{1}=\frac{A B}{(A-B)(A B-1)}, \quad b_{2}=\frac{A+\bar{A}-2}{D-1}, \quad b_{3}=\left(\frac{D(D(A+\bar{A})-2)}{D-1}-B(D+1)\right) .
\end{array}
$$

往证 $O_{B}, O_{D}, O$ 共线, 只需证 $\frac{O_{D}}{O_{B}} \in \mathbb{R}$, 即 $\frac{O_{D}}{\overline{O_{D}}}=\frac{O_{B}}{\overline{O_{B}}}$.

注意到

$$
d_{1}=\overline{d_{1}}, \overline{d_{2}}=\frac{2+A+\bar{A}}{\frac{1}{B}(B+1)}=B d_{2}
$$

故 $\frac{O_{D}}{O_{D}}=\frac{d_{1} d_{2} d_{3}}{d_{1} d_{2} d_{3}}=\frac{1}{B} \cdot \frac{d_{3}}{d_{3}}$, 同理 $\frac{O_{B}}{\overline{O_{B}}}=-\frac{1}{D} \cdot \frac{b_{3}}{\overline{b_{3}}}$.

记 $a=A+\bar{A}$, 则 $a=\bar{a}$, 且

$$
\begin{gathered}
d_{3}=\frac{B(a B+2)}{B+1}+D(1-B)=\frac{a B^{2}-2 B+D-D B^{2}}{B+1}, \\
\overline{d_{3}}=\frac{\frac{1}{B^{2} D}\left(a D-2 B D+B^{2}-1\right)}{\frac{1}{B}(B+1)}=\frac{a D-2 B D+B^{2}-1}{B D(B+1)}, \\
\frac{O_{D}}{\overline{O_{D}}}=D \cdot \frac{a B^{2}-2 B+D-D B^{2}}{a D-2 B D+B^{2}-1} .
\end{gathered}
$$

类似地,

$$
\frac{O_{B}}{\overline{O_{B}}}=B \cdot \frac{a D^{2}-2 D+B-B D^{2}}{a B-2 B D+D^{2}-1} .
$$

题设条件 $B D_{1} / / B_{1} D$ 即 $\frac{D_{1}-B}{B_{1}-D} \in \mathbb{R}$.

记

$$
u=\frac{D_{1}-B}{B_{1}-D}=\frac{\frac{1}{1-D}(D+1-D a)-B}{\frac{1}{B+1}(B a+B-1)-D}=\frac{D+1-D a+B D-B}{B a+B-1-B D-D} \cdot \frac{B+1}{1-D} .
$$

再记

$$
u_{1}=\frac{D+1-D a+B D-B}{B a+B-1-B D-D}, u_{2}=\frac{B+1}{1-D},
$$

则 $u=u_{1} u_{2}$, 且

$$
\overline{u_{1}}=\frac{B+B D-B a+1-D}{D a+D-B D-1-B}, \quad \overline{u_{2}}=\frac{\frac{1}{B}(B+1)}{\frac{1}{D}(D-1)}=-\frac{D}{B} \overline{u_{2}}
$$

于是

$u \in \mathbb{R} \Leftrightarrow u_{1} u_{2}=\overline{u_{1} u_{2}} \Leftrightarrow u_{1}=-\frac{D}{B} \overline{u_{1}}$

$$
\begin{aligned}
& \Leftrightarrow \frac{D+1-D a+B D-B}{B a+B-1-B D-D}=-\frac{D}{B} \frac{B+B D-B a+1-D}{D a+D-B D-1-B} \\
& \Leftrightarrow \frac{(D a-B D+1)+(B-D)}{(B a-B D-1)+(B-D)}=-\frac{D}{B} \cdot \frac{(B a-B D-1)+(D-B)}{(D a-B D-1)+(D-B)} \\
& \Leftrightarrow B(D a-B D-1)^{2}+D(B a-B D-1)^{2}-(B+D)(B-D)^{2}=0 \\
& \Leftrightarrow B D(B+D) a^{2}-4 B D(B D+1) a+(B+D)(B D+1)^{2}-(B+D)(B-D)^{2}=0 \\
& \Leftrightarrow B D(B+D) a^{2}-4 B D(B D+1) a+(B+D)\left(B^{2} D^{2}+2 B D+1-B^{2}+2 B D-D^{2}\right)=0 \\
& \Leftrightarrow B D(B+D) a^{2}-4 B D(B D+1) a+(B+D)\left(\left(B^{2}-1\right)\left(D^{2}-1\right)+4 B D\right)=0 .
\end{aligned}
$$

而

$$
\begin{aligned}
& \frac{O_{D}}{\overline{O_{D}}}=\frac{O_{B}}{\overline{O_{B}}} \Leftrightarrow D\left(a B^{2}-2 B+D\left(1-B^{2}\right)\right)\left(a B-2 B D+\left(D^{2}-1\right)\right) \\
& =B\left(a D^{2}-2 D+B\left(1-D^{2}\right)\right)\left(a D-2 B D+\left(B^{2}-1\right)\right) \\
\Leftrightarrow & a^{2}\left(B^{3} D-D^{3} B\right)+a\left(B^{2} D\left(D^{2}-1-2 B D\right)+B D\left(D\left(1-B^{2}\right)-2 B\right)\right. \\
& \left.-B D^{2}\left(B^{2}-1-2 B D\right)-B D\left(B\left(1-D^{2}\right)-2 D\right)\right) \\
& +D\left(D\left(1-B^{2}\right)-2 B\right)\left(D^{2}-1-2 B D\right)-B\left(B\left(1-D^{2}\right)-2 D\right)\left(B^{2}-1-2 B D\right)=0 \\
\Leftrightarrow & a^{2} \cdot B D(B-D)(B+D)+a \cdot B D\left(B D^{2}-B-2 B^{2} D+D-B^{2} D-2 B\right. \\
& \left.-B^{2} D+D+2 B D^{2}-B+B D^{2}+2 D\right)+D^{2}\left(1-B^{2}\right)\left(D^{2}-1\right)-2 B D\left(D^{2}-1\right) \\
& -2 B D^{3}\left(1-B^{2}\right)+4 B^{2} D^{2}-B^{2}\left(1-D^{2}\right)\left(B^{2}-1\right) \\
& +2 B D\left(B^{2}-1\right)+2 B^{3} D\left(1-D^{2}\right)-4 B^{2} D^{2}=0 \\
\Leftrightarrow & a^{2} \cdot B D(B-D)(B+D)+a \cdot 4 B D\left(B D^{2}-B+D-B^{2} D\right) \\
& +\left(D^{2}-B^{2}\right)\left(1-B^{2}\right)\left(D^{2}-1\right)-2 B D\left(D^{2}-1\right)-2 B D^{3}\left(1-B^{2}\right) \\
& +2 B D\left(B^{2}-1\right)+2 B^{3} D\left(1-D^{2}\right)=0 \\
\Leftrightarrow & a^{2} \cdot B D(B-D)(B+D)+a \cdot 4 B D(D-B)(B D+1) \\
& +(B+D)(B-D)\left(B^{2}-1\right)\left(D^{2}-1\right)+4 B D(B-D)(B+D)=0 \\
\Leftrightarrow & B D(B+D) a^{2}-4 B D(B D+1) a+(B+D)\left(\left(B^{2}-1\right)\left(D^{2}-1\right)+4 B D\right)=0,
\end{aligned}
$$

故 $u \in \mathbb{R}$ 当且仅当 $\frac{O_{D}}{\overline{O_{D}}}=\frac{O_{B}}{\overline{O_{B}}}$, 即等价于 $O_{B}, O, O_{D}$ 三点共线.

评注 本题的复平面解析法思路相对简单, 即分别算出 $O_{B}, O, O_{D}$ 共线与 $B D_{1} / / B_{1} D$ 的条件, 然后经过代数变形验证它们相互等价. 然而具体实施得过程中对计算能力要求较高.

本题预计难度 $30 \mathrm{M}$.

G6. 求所有正整数 $n \geq 3$, 使得任一各边长均为 1 的凸 $n$ 边形均包含一边长为 1 的正三角形.

注: 本题涉及的多边形(三角形)同时包含边界与内部.

解 所求正整数 $n$ 为不小于 3 的所有奇数.

为叙述方便, 我们总是称边长为 1 的等边三角形为单位三角形.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-40.jpg?height=100&width=854&top_left_y=635&top_left_x=607)

图 1. 当 $n=10$ 时一个可能的所取多边形.

一方面, 当 $n$ 为偶数时, 取多边形的内角顺次为 $\left(\frac{n}{2}-1\right) \varepsilon$, 连续 $\frac{n}{2}-1$ 个 $\pi-\varepsilon$, 及 $\left(\frac{n}{2}-1\right) \varepsilon$, 连续 $\frac{n}{2}-1$ 个 $\pi-\varepsilon$, 其中 $\varepsilon$ 为充分小的正实数(如图 1 所示).那么存在一个方向使该多边形在这一方向上的宽度小于 0.1. 于是该多边形不包含单位三角形的内切圆, 从而不包含单位三角形.

另一方面, 当 $n$ 为奇数时, 我们用反证法证明题述等边凸 $n$ 边形必定包含一个单位三角形.

假设存在某个等边凸 $n$ 边形反例, 则 $n \geq 5$. 设此凸 $n$ 边形为 $P=$ $A_{1} A_{2} \cdots A_{n}$ (其中 $A_{1}, \ldots, A_{n}$ 顺时针排列). 不妨设 $P$ 的最长对角线(或边)为 $A_{1} A_{t}$, 其中 $t \geq \frac{n+3}{2}$, 即多边形 $P^{\prime}=A_{1} A_{2} \cdots A_{t}$ 在 $P$ 上顶点个数较多. 在 $A_{1} A_{t}$ 以 $A_{1}$ 为中心逆时针旋转 $\frac{\pi}{3}$ 所得线段上取一点 $X$ 使得 $\left|A_{1} X\right|=1$, 在 $A_{1} A_{t}$ 以 $A_{t}$ 为中心顺时针旋转 $\frac{\pi}{3}$ 所得线段上取一点 $Y$ 使得 $\left|A_{t} Y\right|=1$.

断言 多边形 $P^{\prime}=A_{1} A_{2} \cdots A_{t}$ 包含于等腰梯形 $A_{1} X Y A_{t}$, 且与线段 $X Y$无交.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-40.jpg?height=586&width=651&top_left_y=1806&top_left_x=705)

证明 以 $A_{t}$ 为圆心, 以 $A_{1} A_{t}$ 为半径作圆 $\omega_{1}$; 以 $A_{1}$ 为圆心, 以 $A_{1} A_{t}$ 为半径作圆 $\omega_{2}$. 设 $\omega_{1}, \omega_{2}$ 交于点 $C$ 使得 $C$ 与 $X Y$ 位于直线 $A_{1} A_{t}$ 同侧. 设直线 $A_{1} X$ 与 $\omega_{t}$ 交于另一点 $B_{t}$, 直线 $A_{t} X$ 与 $\omega_{1}$ 交于另一点 $B_{1}$. 记以 $B_{1}, X, Y, B_{t}, C$ 为顶点
的曲边五边形为 $\mathcal{S}$, 以 $A_{1}, B_{1}, X$ 和 $A_{t}, B_{t}, Y$ 为顶点的曲边三角形分别为 $\mathcal{S}_{1}, \mathcal{S}_{t}$.由 $A_{1} A_{t}$ 的最长性可知 $P^{\prime}$ 包含于曲边三角形 $A_{1} A_{t} C$. 如图 2 所示.

注: $\mathcal{S}$ 包含全部边界, 而 $\mathcal{S}_{1}, \mathcal{S}_{t}$ 不包含线段 $A_{1} X, A_{t} Y$ (含端点)并包含其余的全部边界.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-41.jpg?height=234&width=776&top_left_y=503&top_left_x=640)

图 3. 用反证法说明 $P^{\prime} \cap \mathcal{S}=\varnothing$ 的图示.

先说明 $P^{\prime} \cap \mathcal{S}=\varnothing$. 根据 $P^{\prime}$ 的凸性, 只需说明 $P^{\prime} \cap \overline{X Y}=\varnothing$. 这里 $\overline{A B}$ 指 $A, B$ 两点所成线段(含端点). 若不然, 设 $K \in P^{\prime} \cap \overline{X Y}$. 过点 $K$ 作与直线 $A_{1} A_{t}$ 的夹角为 $\frac{\pi}{3}$ 的两条直线与 $A_{1} A_{t}$ 分别交于 $M, N$ 两点, 则单位三角形 $\triangle K M N \subset P^{\prime} \subset P$ (如图 3 所示), 矛盾! 因此 $P^{\prime} \cap \mathcal{S}=\varnothing$.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-41.jpg?height=208&width=776&top_left_y=1164&top_left_x=640)

图 4. 用反证法说明 $P^{\prime} \cap \mathcal{S}_{1}=\varnothing$ 的图示(未体现 $\left|A_{1} A_{2}\right|=\left|A_{1} X\right|=1$ ).

再说明 $P^{\prime} \cap\left(\mathcal{S}_{1} \cup \mathcal{S}_{t}\right)=\varnothing$. 若不然, 不妨设 $P^{\prime} \cap \mathcal{S}_{1} \neq \varnothing$, 则 $A_{2} \in \mathcal{S}_{1}$. 作单位三角形 $A_{1} A_{2} Z$ 使点 $Z$ 与 $A_{t}$ 位于直线 $A_{1} A_{2}$ 同侧. 因为 $\left|A_{1} A_{t}\right| \geq\left|A_{2} A_{t}\right|$, 所以 $\angle A_{1} A_{2} A_{t} \geq \angle A_{2} A_{1} A_{t}>\frac{\pi}{3}$, 于是单位三角形 $\triangle A_{1} A_{2} Z \subset \triangle A_{1} A_{2} A_{t} \subset P$ (如图 4 所示), 矛盾! 因此 $P^{\prime} \cap\left(\mathcal{S}_{1} \cup \mathcal{S}_{t}\right)=\varnothing$, 断言为真.

回到原题. 设 $A_{1} A_{2}, \ldots, A_{t-1} A_{t}$ 在 $A_{1} A_{t}$ 上的投影长分别为 $x_{1}, \ldots, x_{t-1}$, 在垂直于 $A_{1} A_{t}$ 方向上的投影长分别为 $y_{1}, \ldots, y_{t-1}$. 设 $A_{m}$ 为 $A_{1}, \ldots, A_{t}$ 中距 $A_{1} A_{t}$ 最远的点, 距离为 $h$. 由断言可知

$$
\begin{gathered}
\frac{1}{2} \leq x_{i} \leq 1 \Rightarrow\left(1-x_{i}\right)\left(x_{i}-\frac{1}{2}\right) \geq 0 \Rightarrow x_{i}^{2} \leq \frac{3}{2} x_{i}-\frac{1}{2} . \\
\sum_{i=1}^{t-1} x_{i}^{2} \leq \sum_{i=1}^{t-1}\left(\frac{3}{2} x_{i}-\frac{1}{2}\right)=\frac{3}{2}\left|A_{1} A_{t}\right|-\frac{t-1}{2} \\
\sum_{i=1}^{t-1} y_{i}^{2} \leq\left(\sum_{i=1}^{m-1} y_{i}\right)^{2}+\left(\sum_{i=m}^{t-1} y_{i}\right)^{2}=2 h^{2} .
\end{gathered}
$$

注意到

$$
\left|A_{1} A_{t}\right| \leq\left|A_{t} A_{t+1}\right|+\left|A_{t+1} A_{t+2}\right|+\cdots+\left|A_{n} A_{1}\right|=n-t+1,
$$

且 $h<\frac{\sqrt{3}}{2}$, 故由 $t \geq \frac{n+3}{2}$ 得

$$
t-1=\sum_{i=1}^{t-1}\left|A_{i} A_{i+1}\right|=\sum_{i=1}^{t-1}\left(x_{i}^{2}+y_{i}^{2}\right)<\frac{3}{2}(n-t+1)-\frac{t-1}{2}+2 h^{2}<t-1,
$$

矛盾! 因此当 $n$ 为奇数时每个各边长均为 1 的等边凸 $n$ 边形都包含一个单位三角形.

综上所述, 满足要求的正整数 $n$ 即不小于 3 的全体奇数.

评注 不难发现偶数 $n$ 不满足要求然后猜测答案是奇数. 经过一些尝试可以发现当 $n$ 为奇数时极端的 $n$ 边形即证明中的等腰梯形 $Q=A_{1} X Y A_{t}$, 其中 $t=\frac{n+3}{2}$ 时 ( $Q$ 有多个退化的平角内角). 在此基础上做进一步的探索分析发现在反证假设下 $P$ 在 $Q$ 之外似乎是不能有点. 事实上, 将 $A_{1} A_{t}$ 定义为最长对角线则确实不能有点, 进而通过不等式估计就不难导出矛盾了。

本题预计难度 $35 \mathrm{M}$.

G7. 如图, 在锐角 $\triangle A B C$ 中, $A B>A C, D$ 是形内一点, 使得 $\angle D A B=$ $\angle C A D$. 线段 $A C$ 上一点 $E$ 满足 $\angle A D E=\angle B C D$, 线段 $A B$ 上一点 $F$ 满足 $\angle F D A=\angle D B C$, 且直线 $A C$ 上一点 $X$ 满足 $C X=B X$. 设 $O_{1}, O_{2}$ 分别为 $\triangle A D C, \triangle E X D$ 的外心. 证明: $B C, E F, O_{1} O_{2}$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-42.jpg?height=870&width=1173&top_left_y=1501&top_left_x=447)

证明 (温元赫) 作 $D$ 关于 $\triangle A B C$ 的等角共轭点 $Q$, 则 $A, D, Q$ 三点共线.连 $B Q, C Q$.

由 $\angle A B Q=\angle D B C=\angle A D F$ 知 $B, F, D, Q$ 四点共圆. 同理有 $C, E, D, Q$ 四
点共圆, 则

$$
A B \cdot A F=A D \cdot A Q=A C \cdot A E,
$$

故 $B, C, E, F$ 四点共圆.

设 $T=B C \cap E F$, 以 $T$ 为圆心, 以 $T D$ 为半径的圆为 $\delta$, 则只需证明圆 $\delta$,圆 $O_{1}$, 圆 $O_{2}$ 共轴.

注意到

$$
\begin{aligned}
\angle E D F+\angle B D C & =\angle A D F+\angle A D E+\angle B D C \\
& =\angle D B C+\angle D C B+\angle B D C=\pi
\end{aligned}
$$

则 $D$ 关于四边形 $B C E F$ 存在等角共轭点. 又因为 $B D, B Q$ 与 $C D, C Q$ 分别为 $\angle A B C, \angle A C B$ 的等角线, 所以 $D$ 关于四边形 $B C E F$ 的等角共轭点即 $Q$, 从而

$$
\angle D F E+\angle D B C=\angle B F Q+\angle F B Q=\pi-\angle B Q F=\angle E Q C=\angle E D C,
$$

故圆 $(D E F)$ 与 $(D B C)$ 相切. 由 $T E \cdot T F=T B \cdot T C$ 知 $T D$ 为公切线. 同理有 $T Q$ 为圆 $(Q E F)$ 与圆 $(Q B C)$ 的公切线. 故 $Q$ 在圆 $\delta$ 上.

引理 到两个定圆 $\Gamma_{1}, \Gamma_{2}$ 的圆幂之比为定值 $\lambda \neq 1$ 的点的轨迹为一个与此两圆共轴的圆.

这个结论有时被称为开世(Casey)引理, 在根轴的刻画中很好用却并不常见, 下面给出证明.

证明 建立平面直角坐标系 $x O y$. 设 $\Gamma_{i}: x^{2}+y^{2}+a_{i} x+b_{i} y+c_{i}=0(i=1,2)$.记

$$
p(x, y)=x^{2}+y^{2}+a_{i} x+b_{i} y+c_{i},
$$

则平面上一点 $\left(x_{0}, y_{0}\right)$ 到 $\Gamma_{i}$ 的圆幂分别为 $p_{i}\left(x_{0}, y_{0}\right)$, 故所求轨迹为

$$
\left\{(x, y) \mid p_{1}(x, y)=\lambda p_{2}(x, y)\right\}
$$

即一个圆 $\Gamma$. 根据圆系的性质可知 $\Gamma_{1}$ 与 $\Gamma$ 的根轴为

$$
p_{1}(x, y)-\frac{1}{\lambda-1}\left(\lambda p_{2}(x, y)-p_{1}(x, y)\right)=0
$$

容易看出这与 $\Gamma_{1}, \Gamma_{2}$ 的根轴 $p_{1}(x, y)-p_{2}(x, y)=0$ 为同一直线, 故 $\Gamma_{1}, \Gamma_{2}, \Gamma$ 三圆共轴. 引理得证.

回到原题. 根据引理可知只需证明 $A, C$ 两点到圆 $\delta$ 与圆 $O_{2}$ 的幂的比值相等. 注意到

$$
\begin{aligned}
& \operatorname{Pow}(A, \delta)=A D \cdot A Q=A E \cdot A C \\
& \operatorname{Pow}(C, \delta)=C T^{2}-T D^{2}=C T^{2}-C T \cdot C B=-C B \cdot C T .
\end{aligned}
$$

则只需证明

$$
\frac{A X \cdot A E}{A C \cdot A E}=\frac{C X \cdot C E}{C T \cdot C B}
$$

即证明 $\frac{A X}{A C}=\frac{C E}{C T} \cdot \frac{C X}{C B}$.

由 $\angle F T C=\angle C-\angle B, \angle C E T=\angle B$ 得 $\frac{C E}{C T}=\frac{\sin (C-B)}{\sin B}$. 又因为 $\frac{C X}{C B}=\frac{1}{2 \cos C}$,所以

$\frac{A X}{A C}=\frac{C X}{A C}-1=\frac{B C}{A C \cdot 2 \cos C}-1=\frac{\sin A}{2 \cos C \sin B}-1=\frac{\sin (C-B)}{2 \cos C \sin B}=\frac{C E}{C T} \cdot \frac{C X}{C B}$.

因此三圆 $\delta, O_{1}, O_{2}$ 共轴, 故 $T, O_{1}, O_{2}$ 三点共线, 即 $B C, E F, O_{1} O_{2}$ 三线共点于 $T$.

评注 题中的角度关系是不自然的, 故我们优先考虑通过转化进一步理解图形. 经过探索可以发现 $D$ 的等角共轭点 $Q$ 关联 $B, D, F, Q$ 与 $C, D, Q, E$ 两组四点共圆. 进一步, 不难推出 $B, C, E, F$ 四点共圆且 $D, Q$ 关于四边形 $B C E F$ 等角共轭. 至此我们认为对 $D, Q$ 两点的刻画已经很好, 但是距离最终要证明的结论似乎还有一定距离. 事实上, 再次倒角则不难发现 $T D, T Q$ 分别为两组圆的公切线, 而后在圆幂的观点下利用开世(Casey)引理辅以少量计算就不难解决问题了.

本题预计难度 $45 \mathrm{M}$.

G8. 如图,在 $\triangle A B C$ 中, $\omega$ 是外接圆, $\Omega_{A}$ 是 $A$ - 旁切圆, 且圆 $\omega$ 与 $\Omega_{A}$ 交于 $X, Y$ 两点. 过 $X, Y$ 分别作 $\Omega_{A}$ 的切线, 设 $A$ 在这两条切线上的射影分别为 $P, Q$. 过 $P, Q$ 分别作圆 $(A P X),(A Q Y)$ 的切线交于点 $R$. 证明: $A R \perp B C$.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-44.jpg?height=840&width=445&top_left_y=1770&top_left_x=811)
证明 1(段柏延) 作过 $A$ 且垂直于 $B C$ 的直线 $l$. 设 $P R \cap l=R_{1}, Q R \cap l=R_{2}$.设圆 $\Omega_{A}$ 的圆心为 $I_{a}$. 连 $A I_{a}, A X, A Y, I_{a} X, I_{a} Y, X Y$. 只需证明 $A R_{1}=A R_{2}$.

第 1 步: 消去点 $P, Q, R_{(1,2)}$. 不难得到角度关系

$$
\begin{aligned}
\angle A R_{2} Q & =\pi-\angle R_{2} A Q-\angle A Q R_{2}=\angle A Y Q-\angle Y I_{a} D=\angle A Y I_{a}-\frac{\pi}{2}-\angle Y I_{a} D \\
& =\left(\angle A Y I_{a}+\angle A I_{a} Y\right)-\frac{\pi}{2}+\left(\angle A I_{a} Y-\angle D I_{a} Y\right)-2 \angle A I_{a} Y \\
& =\frac{\pi}{2}-\angle I_{a} A Y+\angle A I_{a} D-2 \angle A I_{a} Y \\
& =\frac{\pi}{2}-\frac{1}{2} \angle B A C+\angle C A Y+\frac{1}{2}(\angle A C B-\angle A B C)-2 \angle A I_{a} Y \\
& =\angle C A Y+\angle B A C-2 \angle A I_{a} Y=\angle A X Y-2 \angle A I_{a} Y .
\end{aligned}
$$

同理有 $\angle A R_{1} P=\angle A Y X-2 \angle A I_{a} X$. 根据正弦定理得

$$
\begin{aligned}
A R_{2}=A R_{1} & \Leftrightarrow \frac{A Q \cdot \sin \angle A Q R_{2}}{\sin \angle A R_{2} Q}=\frac{A P \cdot \sin \angle A P R_{1}}{\sin \angle A R_{1} P} \\
& \Leftrightarrow \frac{A Y \cdot \sin \angle A Y Q \cdot \sin \angle A Y Q}{\sin \left(\angle A X Y-2 \angle A I_{a} Y\right)}=\frac{A X \cdot \sin \angle A X P \cdot \sin \angle A X P}{\sin \left(\angle A Y X-2 \angle A I_{a} X\right)} \\
& \Leftrightarrow \frac{\sin \left(\angle A X Y-2 \angle A I_{a} Y\right)}{\sin \left(\angle A Y X-2 \angle A I_{a} X\right)}=\frac{A Y}{A X} \cdot\left(\frac{\cos \angle A Y I_{a}}{\cos \angle A X I_{a}}\right)^{2}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-45.jpg?height=708&width=925&top_left_y=1348&top_left_x=568)

第 2 步: 刻画点 $X, Y$. 分别延长 $I_{a} X, I_{a} Y$ 交 $\omega$ 于两点 $U, V$. 设圆 $\omega, \Omega_{A}$ 的半径分别为 $R, r_{a}$. 设 $\omega$ 的圆心是 $O$, 连 $I_{a} O$, 则由欧拉 (Euler) 公式得

$$
I_{a} U \cdot I_{a} X=O I_{a}^{2}-R^{2}=2 R r_{a} \Rightarrow I_{a} U=2 R=I_{a} V
$$

设圆 $(A B C)$ 上 $A$ 的对径点为 $A^{\prime}$. 设直线 $U V$ 与 $\omega$ 在 $A^{\prime}$ 处的切线交于点 $W$, 则

$$
W I_{a}^{2}=W U \cdot W V+\left(I_{a} U\right)^{2}=W A^{\prime 2}+A A^{\prime 2}=W A^{2} \Rightarrow W A=W I_{a}
$$

第 3 步: 验证 $(*)$ 式. 因为 $W A^{\prime}$ 与圆 $\left(A^{\prime} U V\right)$ 相切, 所以由熟知的相似与正弦定理可得

$$
\frac{U W}{W V}=\left(\frac{A^{\prime} U}{A^{\prime} V}\right)^{2}=\left(\frac{\sin \angle A^{\prime} A V}{\sin \angle A^{\prime} A U}\right)^{2}=\left(\frac{\cos \angle A Y I_{a}}{\cos \angle A X I_{a}}\right)^{2}
$$

设 $A I_{a}$ 的中垂线与 $I_{a} U, I_{a} V$ 分别交于两点 $S, T$, 则 $S, T, W$ 三点共线, 从而 $\angle V A T=\angle A T I_{a}-\angle A V I_{a}=\left(\pi-2 \angle A I_{a} T\right)-(\pi-\angle A X Y)=\angle A X Y-2 \angle A I_{a} Y$.同理有 $\angle U A S=\angle A Y X-2 \angle A I_{a} X$. 连 $A U, A V$, 则

$$
\begin{aligned}
\frac{V T}{T I_{a}} \cdot \frac{I_{a} S}{S U} & =\frac{A V \cdot \sin \angle V A T}{A I_{a} \cdot \sin \angle T A I_{a}} \cdot \frac{A I_{a} \cdot \sin \angle S A I_{a}}{A U \cdot \sin \angle U A S}=\frac{\sin \angle V A T}{\sin \angle U A S} \cdot \frac{A V}{A U} \cdot \frac{\sin \angle S I_{a} A}{\sin \angle T I_{a} A} \\
& =\frac{\sin \left(\angle A X Y-2 \angle A I_{a} Y\right)}{\sin \left(\angle A Y X-2 \angle A I_{a} X\right)} \cdot \frac{\sin \angle A Y V}{\sin \angle A X U} \cdot \frac{\sin \angle A I_{a} X}{\sin \angle A I_{a} Y} \\
& =\frac{\sin \left(\angle A X Y-2 \angle A I_{a} Y\right)}{\sin \left(\angle A Y X-2 \angle A I_{a} X\right)} \cdot \frac{A X}{A Y} .
\end{aligned}
$$

对 $\triangle V I_{a} U$ 与截线 $T S W$ 由梅涅劳斯(Menelaus)定理得

$$
\frac{V T}{T I_{a}} \cdot \frac{I_{a} S}{S U} \cdot \frac{U W}{W V}=1
$$

故 $(*)$ 成立.

评注 以上证明从消点的角度出发, 通过重新定义 $R$ 的方式与正弦定理的转化成功消掉图形中最后生成的三点 $P, Q, R$ 将结论等价转化为三角函数等式 $(*)$. 然而, 要证明 $(*)$ 也不算容易, 尤其是 $\sin (\angle ?-2 \angle ?)$ 项让人望而生畏. 于是我们进一步研究 $X, Y$ 两点的性质, 通过欧拉(Euler) 公式与角度转化将 $(*)$ 变形为更简洁的等式, 最终用梅涅劳斯(Menelaus)定理顺利完成证明.

证明 2 (官方解答) 设 $A$-旁切圆 $\Omega_{A}$ 切 $B C$ 于 $D$, 且 $E$ 为 $D$ 在 $\Omega_{A}$ 上的对径点.

重新定义 $R$ 为圆 $\Omega_{A}$ 在 $E$ 处的切线与 $A$ 关于 $B C$ 的垂线的交点. 只要证明 $R P$ 与圆 $(A P X)$ 相切, 则由对称性可知 $R Q$ 亦与圆 $(A Q Y)$ 相切, 这就证明了原命题.

设 $L=X X \cap A B, T=E E \cap X X, V=A T \cap C L$, 其中 $X X, E E$ 分别为 $\Omega_{A}$ 过 $X, E$ 的切线.

断言 $V L / / B C / / E E$.

证明 对广义圆外切六边形 $C A L X T \infty_{B C}$ 应用布里昂雄(Brianchon)定理即证.

断言 $A, V, L, X$ 四点共圆.

证明 注意到 $\measuredangle L V X=\measuredangle L V C=\measuredangle B C X=\measuredangle B A X=\measuredangle L A X$ 即证.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-47.jpg?height=951&width=939&top_left_y=233&top_left_x=564)

回到原题. 因为 $\measuredangle R T A=\measuredangle L V A=\measuredangle L X A=\measuredangle P X A$, 所以

$$
\text { Rt } \triangle A T R \stackrel{+}{\sim} \operatorname{Rt} \triangle A X P \Longrightarrow \triangle A X T \stackrel{+}{\sim} \triangle A P R
$$

故 $\measuredangle A P R=\measuredangle A X T=\measuredangle A X P$, 即 $R P$ 是圆 $(A P X)$ 的切线. 原命题得证.

评注 以上证明中布里昂雄(Brianchon)定理的应用是神来之笔.

证明 3(官方解答) 连 $A X$. 设 $I_{a}$ 为 $\Omega_{A}$ 的圆心. 设 $P X$ 与圆 $\omega$ 交于另一点 $S$.在直线 $P X$ 上取一点 $T$, 使得 $\measuredangle T A I_{a}=\measuredangle I_{a} A S$. 我们断言: $\triangle A S I_{a} \stackrel{+}{\sim} \triangle A I_{a} T$.

设 $I_{a} X$ 与 $\omega$ 交于另一点 $K$, 连 $K A, K S$. 设 $\omega, \Omega_{A}$ 的半径分别为 $R, r_{a}$, 则由欧拉(Euler)公式得 $I_{a} X \cdot I_{a} K=2 R r_{a}$, 即 $I_{a} K=2 R$. 而 $P X$ 是圆 $\Omega_{A}$ 的切线,则 $K X \perp X S$, 因此 $K S=2 R=I_{a} K$. 取 $I_{a} S$ 的中点 $M$, 则 $\measuredangle K M S=90^{\circ}=$ $\measuredangle K X S$, 故 $M$ 在 $\omega$ 上. 设 $A^{\prime}$ 为 $A$ 关于 $M$ 的对称点, 则

$$
\measuredangle I_{a} A^{\prime} A=\measuredangle S A M=\measuredangle S K M=\measuredangle M K I_{a}=\measuredangle M K X=\measuredangle M S X=\measuredangle I_{a} S X,
$$

从而直线 $S X$ 上存在一点 $T^{\prime}$ 使得 $\triangle I_{a} A A^{\prime} \stackrel{ }{\sim} \triangle I_{a} T^{\prime} S$. 于是 $\frac{S A}{S I_{a}}=\frac{I_{a} A^{\prime}}{I_{a} S}=\frac{I_{a} A}{I_{a} T^{\prime}}$且

$$
\measuredangle A S I_{a}=\measuredangle A^{\prime} I_{a} S=\measuredangle A^{\prime} I_{a} A-\measuredangle S I_{a} A=\measuredangle S I_{a} T^{\prime}-\measuredangle S I_{a} A=\measuredangle A I_{a} T^{\prime}
$$

这表明 $\triangle A S I_{a} \stackrel{+}{\sim} \triangle A I_{a} T^{\prime}$, 故 $\measuredangle S A I_{a}=\measuredangle I_{a} A T^{\prime}$, 即 $T=T^{\prime}, \triangle A S I_{a} \stackrel{+}{\sim} \triangle A I_{a} T$.

作 $\Omega_{A}$ 平行于 $B C$ 的切线 $l$, 分别延长 $A B, A C$ 交 $l$ 于 $B^{\prime}, C^{\prime}$ 两点. 考虑以
$A$ 为中心, 以 $A I_{a}$ 为反演半径的反演变换与关于 $A I_{a}$ 的对称变换复合所得的 $\varphi$,则 $B \xrightarrow{\varphi} C^{\prime}, C \xrightarrow{\varphi} B^{\prime},(A B C) \xrightarrow{\varphi} l$. 又因为 $\triangle A S I_{a} \stackrel{+}{\sim} \triangle A I_{a} T$ 表明 $S \xrightarrow{\varphi} T$, 所以 $T$ 在 $l$ 上.

![](https://cdn.mathpix.com/cropped/2024_02_26_22480dd36c139316040bg-48.jpg?height=957&width=1239&top_left_y=424&top_left_x=403)

作 $A$ 在 $l$ 上的投影点 $R^{\prime}$, 则 $A, P, R^{\prime}, T$ 四点共圆. 设 $\triangle A B C$ 的外心为 $O$,连 $A O$, 则 $K, O, S$ 三点共线, 且 $\varphi(R)$ 在射线 $A O$ 上. 又因为 $\varphi(T)=S$, 所以

$$
\measuredangle R^{\prime} P T=\measuredangle R^{\prime} A T=\measuredangle S A O=\measuredangle K S A=\measuredangle K X A=\measuredangle P A X
$$

故 $R^{\prime} P$ 与圆 $(A P X)$ 相切. 由对称性可知 $R^{\prime} Q$ 与圆 $(A Q Y)$ 相切, 故 $R=R^{\prime}$, 即 $A R \perp B C$.

评注 以上证明深度挖掘了 $T$ 点关联的两组相似, 然后用同一法证明了命题.

本题预计难度 $50 \mathrm{M}$.

## 四、数论

N1. 求所有正整数 $n \geq 1$, 使得存在一对正整数 $(a, b)$, 满足: 正整数 $a^{2}+b+3$ 无立方因子, 且

$$
n=\frac{a b+3 b+8}{a^{2}+b+3} \text {. }
$$

解 所求正整数 $n=2$.
由 $n=\frac{a b+3 b+8}{a^{2}+b+3}$ 得

$$
n a^{2}+n b+3 n=a b+3 b+8,
$$

故 $b=\frac{n a^{2}+3 n-8}{a+3-n}($ 显然 $a+3-n>0)$, 从而

$$
a^{2}+b+3=\frac{n a^{2}+3 n-8+(a+3-n)\left(a^{2}+3\right)}{a+3-n}=\frac{(a+1)^{3}}{a+3-n} .
$$

由于 $a^{2}+b+3$ 无立方因子, 故 $a+1 \mid a+3-n$. 这在 $n \neq 2$ 时不成立.

当 $n=2$ 时, 取 $a=b=2$, 则 $2=\frac{a b+3 b+8}{a^{2}+b+3}$ 合题意.

综上可知只有 $n=2$ 满足要求.

评注 只要大胆地解出 $b$ 并代入, 就可以用上无三次方因子的条件从而顺利解决问题。

本题预计难度 $15 \mathrm{M}$.

N2. 设整数 $n>100$. 将数 $n, n+1, \ldots, 2 n$ 任意分为两组. 证明：必定存在同组的两个数之和是一个完全平方数.

证明 注意到形如 $2 k^{2}-4 k, 2 k^{2}+1,2 k^{2}+4 k$ ( $k$ 为正整数)的三个数中任意两个之和均为完全平方数, 故只要它们同时属于 $[n, 2 n]$ 即证明了原题结论.

设 $k$ 为最小的正整数, 使得 $2 k^{2}-4 k \geq n$, 我们断言: $2 k^{2}+4 k \leq 2 n$.

若 $2 k^{2}+4 k>2 n$, 则 $2 k^{2}+4 k>200, k \geq 10$, 从而

$$
n<k^{2}+2 k \leq 2(k-1)^{2}-4(k-1)+1 \text {, }
$$

其中最后一个不等号当 $k \geq 10$ 时成立, 而这与 $k$ 的最小性矛盾! 故有

$$
n \leq 2 k^{2}-4 k<2 k^{2}+4 k \leq 2 n \text {. }
$$

至此, 断言获证, 从而原命题为真.

评注 题目的设问提示我们构造三个两两和为完全平方数的数. 为了让它们落入既定的范围内, 我们让这三个数离得尽量近, 即选取 $2 k^{2}-4 k, 2 k^{2}+1$, $2 k^{2}+4 k$. 此后做一些代数的估计即可.

本题预计难度 $20 \mathrm{M}$.

N3. 求所有正整数 $n$, 满足: 数 $n$ 全部的 $k$ 个不同正约数可以被排列为 $d_{1}, d_{2}, \ldots, d_{k}$, 使得对任意正整数 $i=1,2, \ldots, k$ 均有 $d_{1}+d_{2}+\cdots+d_{i}$ 是完全平方数.
解 所有满足要求的正整数 $n$ 为 1,3 .

容易验证 $n=1,3$ 满足要求, 下面我们证明满足要求的正整数只有 1,3 .

设 $n$ 以及其所有正因数的一个排列 $d_{1}, d_{2}, \ldots, d_{k}$ 满足要求. 令 $\sqrt{\sum_{j=1}^{i} d_{j}}=a_{i}$.

断言 $d_{i}=2 i-1$ 对 $i=1,2, \ldots, k$ 均成立.

证明 对 $i$ 归纳证明此结论.

当 $i=1$ 时, 注意到 $1 \in\left\{d_{1}, d_{2}, \ldots, d_{k}\right\}$, 且对于 $2 \leq j \leq k$, 均有

$$
d_{j}=a_{j}^{2}-a_{j-1}^{2} \geq\left(a_{j-1}+1\right)^{2}-a_{j-1}^{2}>1,
$$

故 $d_{1}=1$.

假设结论对于 $1,2, \ldots, i-1(i \geq 2)$ 均成立, 那么 $a_{i-1}=i-1$. 若 $a_{i} \neq i$, 即 $a_{i} \geq i+1$, 则

$$
d_{i}=a_{i}^{2}-a_{i-1}^{2}=a_{i}^{2}-(i-1)^{2}=\left(a_{i}+i-1\right)\left(a_{i}-i+1\right),
$$

故 $a_{i}+i-1\left|d_{i}\right| n, a_{i}+i-1 \in\left\{d_{1}, d_{2}, \ldots, d_{k}\right\}$. 设 $a_{i}+i-1=d_{j}$.

注意到 $a_{i}+i-1>2 i-1$, 故由归纳假设有 $a_{i}+i-1 \notin\left\{d_{1}, d_{2}, \ldots, d_{i-1}\right\}$.

又 $d_{i}=\left(a_{i}+i-1\right)\left(a_{i}-i+1\right)>a_{i}+i-1$, 故 $j \geq i+1$. 然而

$d_{j}=a_{j}^{2}-a_{j-1}^{2} \geq\left(a_{j-1}+1\right)^{2}-a_{j-1}^{2}=2 a_{j-1}+1 \geq 2 a_{i}+1>a_{i}+i-1$,

矛盾! 故 $a_{i}=i$, 即 $d_{i}=a_{i}^{2}-a_{i-1}^{2}=2 i-1$. 归纳证毕, 断言成立.

回到原题, 由断言可知 $n$ 的所有正因数为 $1,3, \ldots, n$, 从而 $n$ 为奇数. 若 $n>1$, 则由 $n-2 \mid n$ 可知 $n-2 \mid 2$, 因此 $n=1$ 或 $n=3$.

综上所述, 满足要求的所有正整数 $n$ 为 1,3 .

评注试着依次写出 $d_{1}, d_{2}, \ldots$ 时会自然地猜到 $d_{i}=2 i-1$. 该结论的归纳证明很自然, 而有了这一结论后原题也就迎刃而解了.

本题预计难度 $20 \mathrm{M}$.

N4. 设有理数 $r>1$. 小明在数轴上玩如下单人游戏: 一开始, 在 0 处有一颗红色珠子, 在 1 处有一颗蓝色珠子. 每一轮, 小明选取其中一颗珠子并选取整数 $k$. 如果被选中的珠子位于 $x$, 而未被选中的珠子位于 $y$, 则在该轮游戏中小明将选中的珠子移动到 $x^{\prime}$, 使得 $x^{\prime}-y=r^{k}(x-y)$.

求所有 $r$, 使得小明可以经过至多 2021 轮游戏将红色珠子移动到 1 .

解 所有满足要求的有理数 $r$ 即全体形如 $\frac{t+1}{t}(t=1,2, \ldots, 1010)$ 的有理数.

一方面, 我们证明这些 $r=\frac{t+1}{t}$ 均满足要求.
以一个数对表示红色与蓝色在数轴上的位置, 则可以进行如下移动:

$$
\begin{aligned}
(0,1) & \rightarrow\left(\frac{1}{t+1}, 1\right) \rightarrow\left(\frac{1}{t+1}, 1+\frac{1}{t+1}\right) \\
& \rightarrow\left(\frac{2}{t+1}, 1+\frac{1}{t+1}\right) \rightarrow \cdots \rightarrow\left(1,1+\frac{t}{t+1}\right)
\end{aligned}
$$

这样所用的步数 $2 t+1 \leq 2021$, 满足要求.

另一方面, 我们证明其它 $r$ 不满足要求.

设 $r=\frac{a}{b}$, 其中 $a, b$ 互素且 $a>b$. 若 $a-b$ 有素因子 $p$, 则每个珠子任何一次移动的距离 $d$ 均满足 $v_{p}(d) \geq 1$, 而红色珠子移动的总距离为 1 , 即有 $v_{p}(1)=0$,矛盾! 故 $a-b=1$, 即 $r$ 形如 $\frac{t+1}{t}$.

下面说明 $t \leq 1010$. 注意到 $\frac{t+1}{t} \equiv-1(\bmod 2 t+1)$, 则

$$
x^{\prime}-y \equiv \pm(x-y) \quad(\bmod 2 t+1)
$$

因此 $(x, y)$ 在模 $2 t+1$ 的意义下能到达位置的同余类是确定的(只有 $(x, y),(2 y-x, y)$ 两个). 因此, 在模 $2 t+1$ 的意义下初始状态 $(x, y)=(0,1)$ 能到达的位置即

$$
\cdots \leftrightarrow(-2,-3) \leftrightarrow(-2,-1) \leftrightarrow(0,-1) \leftrightarrow \underbrace{(0,1)}_{\text {起点 }} \leftrightarrow(2,1) \leftrightarrow(2,3) \leftrightarrow(4,3) \leftrightarrow \cdots .
$$

当红色珠子到达 1 时, 游戏的轮数不小于在模 $2 t+1$ 的意义下 $x$ 从 0 沿 $(*)$ 所示轨迹运动到 $-2 t$ 或 $2 t+2$ 所需的步数, 即 $2 t$. 这表明 $2 t \leq 2021$, 故 $t \leq 1010$.

综上所述, 一切满足要求的有理数 $r$ 构成集合 $\left\{\left.\frac{t+1}{t} \right\rvert\, t=1,2, \ldots, 1010\right\}$.

评注 经过一些尝试不难猜出答案. 在证明的过程中, 分析素因子容易得到 $r=\frac{t+1}{t}$, 而随后说明 $t \leq 1010$ 的部分有难度. 这里我们通过分析模 $2 t+1$ 规避复杂的讨论, 巧妙地解决了问题.

本题预计难度 $30 \mathrm{M}$.

N5. 证明: 只有有限多组正整数 $(a, b, c, n)$ 满足不定方程

$$
n !=a^{n-1}+b^{n-1}+c^{n-1} .
$$

证明 若 $n \leq 4$, 则容易验证原方程的正整数解 $(a, b, c, n)$ 只有

$$
(1,1,2,3), \quad(1,2,1,3), \quad(2,1,1,3)
$$

四组. 下面我们证明当 $n \geq 5$ 时原方程无正整数解.

(a) 若 $n$ 为奇数, 则考虑模 4 不难看出 $a, b, c$ 均为偶数, 从而 $2^{n-1} \mid a^{n-1}+$
$b^{n-1}+c^{n-1}$. 但是

$$
v_{2}(n !)=v_{2}((n-1) !)=\sum_{i=0}^{\infty}\left\lfloor\frac{n-1}{2^{i}}\right\rfloor<n-1,
$$

矛盾! 故在情形(a)中原方程无正整数解.

(b) 若 $n$ 为偶数, 则 $a, b, c$ 两奇一偶或全偶.

(b1) 若 $a, b, c$ 两奇一偶, 不妨设 $2 \mid a$, 则由 $v_{2}(n !) \leq n-1$ 可得

$$
v_{2}(b+c)=v_{2}\left(b^{n-1}+c^{n-1}\right) \geq v_{2}(n !) \geq n-\log _{2} n
$$

于是 $b+c \geq \frac{2^{n}}{n}$, 则由 $n \geq 6$ 得

$$
b^{n-1}+c^{n-1} \geq 2 \cdot\left(\frac{2^{n-1}}{n}\right)^{n-1} \geq n !
$$

矛盾! 故在情形(b1) 中原方程无正整数解.

(b2) 若 $a, b, c$ 全偶, 则 $v_{2}(n !) \geq n-1$, 即 $n$ 是 2 的幂, 故 $n \geq 8$. 枚举可知 $n \neq 8$, 从而 $n \geq 16$.

引理 对任意正整数 $n \geq 16$ 均有 $2\left(\frac{n}{2}\right)^{n-1}>n$ !.

证明 对 $n$ 归纳. 当 $n=16$ 时, 由于 $15 \times 14 \times 2<8^{3}$, 且

$16 \times(3 \times 13) \times(4 \times 12) \times \cdots \times(7 \times 9) \times 8<16 \times 64^{5} \times 8=2 \times 8^{12}$,

故 $16 !<2 \times 8^{15}$. 假设 $n-1$ 的情形已经证明成立, 考虑 $n$ 的情形: 注意到

$$
\frac{2\left(\frac{n}{2}\right)^{n-1}}{2\left(\frac{n-1}{2}\right)^{n-2}}=\frac{n}{2} \cdot\left(\frac{n}{n-1}\right)^{n} \cdot\left(\frac{n-1}{n}\right)^{2}>\frac{n}{2} \cdot \mathrm{e} \cdot\left(\frac{16}{17}\right)^{2}>n
$$

故

$$
2\left(\frac{n}{2}\right)^{n-1}>n \cdot 2\left(\frac{n-1}{2}\right)^{n-2}>n \cdot(n-1) !=n !,
$$

归纳证明完成.引理得证.

回到原题, 不妨设 $a \leq b \leq c$. 注意到

$$
n !>b^{n-1}+c^{n-1} \geq 2\left(\frac{b+c}{2}\right)^{n-1},
$$

则由引理得 $b+c<n$, 故 $b<\frac{n}{2}$. 同理可得 $a<\frac{n}{2}$.

断言 $b+c, a+c$ 两数中至少有一个存在奇素因子.

证明 用反证法. 假设不然, 设 $a=2 a_{0}, b=2 b_{0}, c=2 c_{0}$, 则 $a_{0}+c_{0}, b_{0}+c_{0}$ 两数均为 2 的幂. 因为 $v_{2}(n !) \leq n-1$, 所以 $a_{0}^{n-1}+b_{0}^{n-1}+c_{0}^{n-1}=\frac{n !}{2^{n-1}}$ 为奇数, 而 $a_{0}+c_{0}, b_{0}+c_{0}$ 是偶数, 故 $a_{0}, b_{0}, c_{0}$ 均为奇数. 设 $a_{0}+c_{0}=2^{k}, b_{0}+c_{0}=2^{l}$, 则由 $a_{0} \leq b_{0} \leq c_{0}$ 可知 $k \leq l$ 且 $c_{0} \geq 2^{l-1}$,于是由

$$
1 \leq a_{0}=2^{k}-c_{0} \leq 2^{k}-2^{l-1}
$$

得 $k=l$, 即 $a_{0}=b_{0}$. 此时若有奇素数 $q \mid c_{0} \leq n$, 则 $q \nmid 2^{k}-c_{0}=a_{0}=b_{0}$, 从而

$$
q \nmid a_{0}^{n-1}+b_{0}^{n-1}+c_{0}^{n-1}=\frac{n !}{2^{n-1}},
$$

这是不可能的. 因此 $c_{0}=1$, 即 $a_{0}=b_{0}=c_{0}=1$, 故 $n !=3 \times 2^{n-1}$, 矛盾! 断言为真.

以下不再用到 $a \leq b$, 由断言不妨设 $b+c$ 有奇素因子 $p$. 由 $b+c<n$ 得 $p<n$, 从而 $p \mid n$ !, 故

$$
p \mid n !-\left(b^{n-1}+c^{n-1}\right)=a^{n-1},
$$

因此 $p \mid a$. 又因为 $a<\frac{n}{2}$, 所以 $p \leq \frac{n}{2}-1$. 若 $p \mid b$ 或 $p \mid c$, 则 $p$ 同时整除 $a, b, c$,从而

$$
v_{p}(n !)=v_{p}\left(a^{n-1}+b^{n-1}+c^{n-1}\right) \geq n-1
$$

这与 $p \geq 3$ 矛盾! 因此 $p \nmid b c$, 则由升幂(LTE)定理得

$v_{p}(b+c)=v_{p}\left(b^{n-1}+c^{n-1}\right)-v_{p}(n-1)=v_{p}(n !)-v_{p}(n-1) \geq v_{p}((n-2) !) \geq\left\lfloor\frac{n-2}{p}\right\rfloor$.

设 $t=\left\lfloor\frac{n-2}{p}\right\rfloor$, 则由 $\frac{n-2}{p}<t+1$ 得 $p>\frac{n-2}{t+1}$, 从而

$$
b+c \geq p^{\left\lfloor\frac{n-2}{p}\right\rfloor}>\left(\frac{n-2}{t+1}\right)^{t} .
$$

记 $f(t)=\left(\frac{n-2}{t+1}\right)^{t}$, 则 $\ln f(t)=t \ln \frac{n-2}{t+1}$, 对 $t$ 求导得 $\frac{f^{\prime}(t)}{f(t)}=\ln \frac{n-2}{t+1}+t \cdot\left(-\frac{1}{t+1}\right)$.

故

$$
\begin{aligned}
f^{\prime}(t) \geq 0 & \Leftrightarrow \ln \frac{n-2}{t+1}+t \cdot\left(-\frac{1}{t+1}\right) \geq 0 \\
& \Leftrightarrow \ln (n-2)-1>\ln (t+1)-\frac{1}{t+1} .
\end{aligned}
$$

注意到右式关于 $t$ 单增, 则 $f(t)$ 在 $(0,+\infty)$ 上先增后降. 由 $3 \leq p \leq \frac{n}{2}-1$ 得 $2 \leq t \leq\left\lfloor\frac{n-2}{3}\right\rfloor$, 即

$$
f(t) \geq \min \left\{f(2), f\left(\frac{n-3}{2}\right)\right\}=\min \left\{\left(\frac{n-2}{3}\right)^{2}, 2^{\frac{n-3}{2}}\right\}>n .
$$

这导致 $b+c>f(t)>n$, 矛盾! 故在情形 (b2)中原方程无正整数解.

综合以上讨论, 我们便证明了原不定方程的正整数解有且仅有四组.

评注 本解法思路相对自然, 就是通过LTE定理等手段卡住某个质数的幂次后从大小关系上推出矛盾. 难点在于最后一种情况需要大量讨论分析与计算,势必要消耗大量时间. 值得一提的是, 如果只说明不定方程正整数解的个数有限而不具体确定只有四组, 那么(b1)的讨论可以简化.

本题预计难度 $35 \mathrm{M}$.

N6. 求所有整数 $n \geq 2$, 满足: 对任意 $n$ 个不同正整数 $x_{1}, x_{2}, \ldots, x_{n}$, 若 $n \nmid x_{1}+x_{2}+\cdots+x_{n}$, 则存在它们的某个排列 $a_{1}, a_{2}, \ldots, a_{n}$, 使得

$$
n \mid 1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n} .
$$

解 所有满足要求的正整数 $n$ 为全体 2 的正整数幂和全体不小于 3 的正奇数.

一方面, 当 $n$ 同时含有奇偶素因子时, 取 $x_{1} \equiv \cdots \equiv x_{n-1} \equiv 1(\bmod n), x_{n}=$ $1+2^{n}$. 此时对于其任意一个排列 $a_{1}, \ldots, a_{n}$, 设 $a_{k}=1+2^{n}$, 则

$$
1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n} \equiv 1+2+\cdots+n+2^{n} k \equiv \frac{n}{2}+2^{n} k \quad(\bmod n) .
$$

注意到 $v_{2}\left(\frac{n}{2}+2^{n} k\right)=v_{2}\left(\frac{n}{2}\right)<v_{2}(n)$, 则 $n \nmid 1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n}$, 故这样的 $n$ 不满足要求.

另一方面, 我们说明一切 2 的正整数幂和奇数均满足要求.

引理 若 $\operatorname{gcd}\left(n, x_{1}+\cdots+x_{n}\right)=d$, 且存在 $x_{1}, \ldots, x_{n}$ 的某个排列 $b_{1}, \ldots, b_{n}$ 使得

$$
d \mid 1 \cdot b_{1}+2 \cdot b_{2}+\cdots+n \cdot b_{n}
$$

那么 $x_{1}, \ldots, x_{n}$ 存在排列 $a_{1}, \ldots, a_{n}$ 使得 $n \mid 1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n}$.

证明 对 $i=1, \ldots, n$, 记

$S_{i}=i \cdot b_{1}+(i+1) \cdot b_{2}+\cdots+n \cdot b_{n-i+1}+1 \cdot b_{n-i+2}+2 \cdot b_{n-i+3}+\cdots+(i-1) \cdot b_{n}$.注意到 $S_{i}-S_{i-1} \equiv x_{1}+\cdots+x_{n}(\bmod n)$, 故 $S_{1}, \ldots, S_{n}$ 模 $n$ 后取遍 $d$ 的倍数 (含 0 ). 引理得证.

(a) 先对正奇数 $n$ 归纳证明其满足要求.

若 $n=1$, 则 $n \nmid x_{1}$ 不成立, 故 $n$ 满足要求. 以下假设 $n \geq 3$ 且小于 $n$ 的正奇数均满足要求.

设 $\operatorname{gcd}\left(n, x_{1}+\cdots+x_{n}\right)=d(1 \leq d<n)$. 根据引理, 只需说明存在 $x_{1}, \ldots, x_{n}$ 的排列 $b_{1}, \ldots, b_{n}$ 使得 $d \mid 1 \cdot b_{1}+2 \cdot b_{2}+\cdots+n \cdot b_{n}$. 以下假设 $d \geq 3$.

为此, 我们证明命题: 可以将 $x_{1}, \ldots, x_{n}$ 分成三组, 使每组依次含有 $d, d$, $n-2 d$ 个数, 且满足: 任何一组中的数均存在某一排列 (记为 $y_{1}, \ldots, y_{m}$ ), 使得 $d \mid 1 \cdot y_{1}+2 \cdot y_{2}+\cdots+m \cdot y_{m}$. 此时, 将这三组数依组内既定排列顺次写下得到的新排列 $b_{1}, \ldots, b_{n}$ 即满足 $d \mid 1 \cdot b_{1}+2 \cdot b_{2}+\cdots+n \cdot b_{n}$.

对任意奇数 $r$, 因为 $d \mid r$ 蕴含 $d \mid \mathrm{C}_{r+1}^{2}$, 所以任意模 $d$ 所得余数全相同的正整数 $x_{1}, \ldots, x_{r}$ 均满足 $d \mid 1 \cdot x_{1}+2 \cdot x_{2}+\cdots+r \cdot x_{r}$. 因此, 在分组时只需令每
组中或者所有数之和不被 $d$ 整除(由归纳假设)或者模 $d$ 所得余数全相同(因为 $n-2 d$ 是奇数), 即可证明命题. 分两种情形:

(a1) $x_{1}, \ldots, x_{n}$ 中存在 $d$ 个数模 $d$ 所得余数相同. 先将它们分成一组, 则其余 $n-d$ 个数之和仍被 $d$ 整除. 于是其余 $n-d$ 个数或者模 $d$ 所得余数全相同,或者可以被分成含有 $d, n-2 d$ 个数的两组, 使得每组中所有数之和均不被 $d$ 整除. 故此时存在满足要求的分组方式.

(a2) $x_{1}, \ldots, x_{n}$ 中不存在 $d$ 个数模 $d$ 所得余数相同. 因为 $n \geq 3 d$, 所以 $x_{1}, \ldots, x_{n}$ 中存在模 $d$ 所得余数互不相同的四个数, 不妨设为 $x_{1}, x_{2}, x_{3}, x_{4}$. 先将 $x_{5}, x_{6}, \ldots, x_{n}$ 任意分成三组, 使每组依次含有 $d-1, d-1, n-2 d-2$ 个数.然后从 $x_{1}, x_{2}, x_{3}, x_{4}$ 中适当选取 $1,1,2$ 个数分别放入这三个组, 使得它们依次含 $d, d, n-2 d$ 个和不被 $d$ 整除的数. 故此时存在满足要求的分组方式.

综合(a1)(a2)的讨论, 我们即证明了命题, 从而完成了归纳证明.

(b) 再对正整数 $k$ 归纳证明 $n=2^{k}$ 满足要求.

若 $k=1$, 则 $n=2$. 由 $n \nmid x_{1}+x_{2}$ 知 $x_{1}, x_{2}$ 奇偶性相异, 取其中之偶数置于 $a_{1}$, 取其中之奇数置于 $a_{2}$, 则 $n \mid 1 \cdot a_{1}+2 \cdot a_{2}$. 故 $k=1$ 满足要求. 以下假设 $k \geq 2$ 且小于 $k$ 的正整数均满足要求.

设 $\operatorname{gcd}\left(n, x_{1}+\cdots+x_{n}\right)=d$. 若 $d<2^{k-1}$, 则对 $x_{1}+x_{2^{k-1}+1}, x_{2}+x_{2^{k-1}+2}, \cdots$ ， $x_{2^{k-1}-1}+x_{2^{k}}$ 由归纳假设知存在其排列 $b_{1}, \ldots, b_{n}$ 使得 $2^{k-1} \mid 1 \cdot b_{1}+2 \cdot b_{2}+\cdots+n \cdot b_{n}$,从而引理表明其满足要求.

以下假设 $d=2^{k-1}$, 从而 $n=2 d$. 分两种情形:

(b1) $x_{1}, \ldots, x_{n}$ 模 $d$ 所得余数不全相同.

不妨设 $d \nmid x_{1}+\cdots+x_{d}$, 则 $d \nmid x_{d+1}+\cdots+x_{2 d}$. 根据归纳假设, 存在 $x_{1}, \ldots, x_{d}$ 的排列 $b_{1}, \ldots, b_{d}$ 使得 $d \mid 1 \cdot b_{1}+2 \cdot b_{2}+\cdots+d \cdot b_{d}$, 存在 $x_{d+1}, \ldots, x_{2 d}$ 的排列 $b_{d+1}, \ldots, b_{2 d}$ 使得 $d \mid 1 \cdot b_{d+1}+2 \cdot b_{d+2}+\cdots+d \cdot b_{2 d}$. 于是 $d \mid 1 \cdot b_{1}+2 \cdot b_{2}+\cdots+n \cdot b_{n}$.根据引理即可将 $b_{1}, \ldots, b_{n}$ 适当排列为 $a_{1}, \ldots, a_{n}$ 使得 $n \mid 1 \cdot a_{1}+2 \cdot a_{2}+\cdots+n \cdot a_{n}$.

(b2) $x_{1}, \ldots, x_{n}$ 模 $d$ 所得余数全相同.

设它们模 $n$ 所得不同余数构成集合 $R$, 则 $|R|=1$ 或 2 . 若 $|R|=1$, 则 $n \mid x_{1}+\cdots+x_{n}$, 矛盾! 因此 $|R|=2$. 不妨设 $x_{1} \not \equiv x_{2}(\bmod d)$, 则 $n \nmid x_{1}-x_{2}$.由

$$
\begin{aligned}
& d \mid 1 \cdot x_{1}+2 \cdot x_{2}+3 \cdot x_{3}+\cdots+n \cdot x_{n}=A, \\
& d \mid 1 \cdot x_{2}+2 \cdot x_{1}+3 \cdot x_{3}+\cdots+n \cdot x_{n}=B
\end{aligned}
$$

以及 $2 d=n \nmid x_{1}-x_{2}=B-A$ 得 $n \mid A$ 或 $n \mid B$, 从而该排列满足要求.
综上所述, 一切满足要求的正整数 $n$ 即全体 2 的正整数幂与全体不小于 3 的正奇数.

评注 由于笔者对引理较为熟悉, 故本题在思维上的难度并不是很大, 但是仍需要耐心搞清楚大量繁琐的细节. 如果不熟悉引理, 则本题是十分困难的. 据笔者所知, 有以下相关的问题:

(1) 2020 波兰数学奥林匹克第 5 题(见 [4]).

(2) 2021 百年老校数学竟赛第 6 题(见 [5]).

本题预计难度 $40 \mathrm{M}$.

N7. 正整数数列 $\left\{a_{n}\right\}$ 满足: 对任意正整数 $m, n$, 均有

$$
a_{m+2 n} \mid a_{m}+a_{m+n} \text {. }
$$

证明： $\left\{a_{n}\right\}$ 是最终周期的数列.

证明 先证明 $\left\{a_{n}\right\}$ 有界.

若正整数 $n^{*}>100$ 使得 $a_{n^{*}}>\max \left\{a_{1}, a_{2}, \ldots, a_{n^{*}-1}\right\}$, 则由条件知: 对任意 $m \leq \frac{n^{*}-1}{2}$ 均有

$$
a_{n^{*}} \mid a_{n^{*}-m}+a_{n^{*}-2 m}<2 a_{n^{*}} \Longrightarrow a_{n^{*}}=a_{n^{*}-m}+a_{n^{*}-2 m},
$$

从而

$$
a_{n^{*}-1}+a_{n^{*}-2}=a_{n^{*}-2}+a_{n^{*}-4}=a_{n^{*}-4}+a_{n^{*}-8},
$$

故 $a_{n^{*}-1}=a_{n^{*}-4}, a_{n^{*}-2}=a_{n^{*}-8}$. 由此递归易见

$$
a_{n^{*}-1}\left|a_{n^{*}-3 k-1}, \quad a_{n^{*}-2}\right| a_{n^{*}-6 k-2}
$$

对任意 $k \leq \frac{n-3}{6}$ 成立. 又因为

$$
\max \left\{a_{n^{*}-1}, a_{n^{*}-2}\right\} \geq \frac{1}{2}\left(a_{n^{*}-1}+a_{n^{*}-2}\right)=\frac{a_{n^{*}}}{2},
$$

所以 $a_{1}, a_{2}, \ldots, a_{6}$ 中存在被 $\max \left\{a_{n^{*}-1}, a_{n^{*}-2}\right\}$ 整除的数, 即

$$
\max \left\{a_{1}, a_{2}, \ldots, a_{6}\right\} \geq \frac{a_{n^{*}}}{2}
$$

这表明 $\left\{a_{n}\right\}$ 有界.

再证明 $\left\{a_{n}\right\}$ 是最终周期的.

因为 $\left\{a_{n}\right\}$ 有界, 所以

- 存在充分大的正整数 $N$, 使得 $\left\{a_{n}\right\}$ 自第 $N$ 项之后的每一项均在数列中出现无穷多次;
- 存在最大的正整数 $M$, 使得 $\left\{a_{n}\right\}$ 中有无穷多项取值为 $M$.

记 $X=\left\{n>N \mid a_{n}=M\right\}=\left\{n_{1}, n_{2}, \ldots\right\}$, 其中 $n_{1}<n_{2}<\cdots$.

断言 $\left\{n_{k}\right\}$ 是公差为奇数的等差数列.

证明 若正整数 $k$ 使得 $2 \mid n_{k+1}-n_{k}$, 令 $n^{\prime}=\frac{n_{k}+n_{k+1}}{2} \in \mathbb{N}_{+}$, 则由条件知

$$
a_{n_{k+1}}\left|a_{n_{k}}+a_{n^{\prime}} \Longrightarrow M\right| M+a_{n^{\prime}} \Longrightarrow a_{n^{\prime}}=M
$$

这与 $n^{\prime} \notin X$ 矛盾! 于是 $n_{k+1}-n_{k}$ 为奇数.

对任意正整数 $k$, 令 $n^{\prime \prime}=\frac{n_{k}+n_{k+2}}{2} \in \mathbb{N}_{+}$, 则由条件知

$$
a_{n_{k+2}}\left|a_{n_{k}}+a_{n^{\prime \prime}} \Longrightarrow M\right| M+a_{n^{\prime \prime}} \Longrightarrow a_{n^{\prime \prime}}=M,
$$

从而 $n^{\prime \prime}=n_{k+1}$. 这表明 $\left\{n_{k}\right\}$ 是以某奇数为公差的等差数列, 断言为真.

设 $\left\{n_{k}\right\}$ 的公差为 $d$. 对任意正整数 $m>n_{1}$, 由 $d$ 为奇数知方程 $2 x-m \equiv n_{1}$ $(\bmod d)$ 有解. 取充分大的正整数解 $x=k$, 则由条件知

$$
\left\{\begin{array}{l}
M=a_{2 k-m} \mid a_{k}+a_{m} \\
M=a_{2 k-m-d} \mid a_{k}+a_{m+d}
\end{array} \quad \Longrightarrow a_{m} \equiv a_{m+d} \quad(\bmod M) .\right.
$$

因此由 $M$ 的最大性知 $a_{m}=a_{m+d}$ 对任意正整数 $m>n_{1}$ 成立, 故 $\left\{a_{n}\right\}$ 是最终周期的数列.

评注 本题重点在证明 $\left\{a_{n}\right\}$ 有界. 设出比之前所有数都大的 $a_{n}$, 将条件用在所有 $a_{n}$ 附近的项就不难推导出大量结论, 第选出其中有用的即可得到断言，而后的证明就不困难了。

本题预计难度 $35 \mathrm{M}$.

N8. 求所有正整数 $n$, 使得存在整系数多项式 $P(x)$, 满足：对任意正整数 $m, P^{m}(1), \ldots, P^{m}(n)$ 在模 $n$ 的意义下恰取到 $\left\lceil\frac{n}{2^{m}}\right\rceil$ 个不同余数. 这里 $P^{m}$ 表示 $P$ 的 $m$ 次迭代。

解 (官方解答) 所求正整数 $n$ 为全体素数与全体 2 的非负整数幂.

一方面, 我们说明如上正整数 $n$ 均满足要求.

若 $n$ 为 2 的非负整数幂时, 则 $P(x)=2 x$ 满足要求.

若 $n$ 为奇素数, 则由拉格朗日(Lagrange)插值公式可知存在 $P(x)$ 使得 $P(x) \equiv\lfloor x / 2\rfloor(\bmod p)$ 对任意正整数 $x$ 成立, 满足要求.

另一方面, 我们说明其它正整数 $n$ 均不满足要求.

简记 $\mathbb{Z}_{l}=\mathbb{Z} / l \mathbb{Z}$. 令 $f_{m, l}=\left|P^{m}\left(\mathbb{Z}_{l}\right)\right|$, 则 $f_{m, n}=\left\lceil n / 2^{m}\right\rceil$.
情形 $1 . n$ 有两个不同素因子.

设 $n=a b$, 其中正整数 $a, b>1$ 且 $\operatorname{gcd}(a, b)=1$. 由中国剩余定理可知 $f_{m, n}=f_{m, a} f_{m, b}$. 对任意正整数 $m$ 与 $l \in\{a, b\}$, 注意到 $P^{m+1}\left(\mathbb{Z}_{l}\right) \subseteq$ $P^{m}\left(\mathbb{Z}_{l}\right)$, 从而 $f_{m+1, l}=f_{m, l}$ 蕴含 $P^{m+1}\left(\mathbb{Z}_{l}\right)=P^{m}\left(\mathbb{Z}_{l}\right)$. 取最小的正整数 $m$ 使得 $\min \left\{f_{m+1, a}, f_{m+1, b}\right\}=1$, 不妨设 $f_{m+1, a}=1$, 则

$$
f_{m+1, n}=f_{m+1, b}<f_{m, b}=\frac{f_{m, n}}{f_{m, a}} \leq \frac{f_{m, n}}{2} \leq f_{m+1, n}
$$

矛盾! 因此这样的 $n$ 不满足要求.

情形 $2 . n=p^{k}$, 其中 $p$ 为奇素数且正整数 $k \geq 2$.

引理 设 $f$ 为整系数多项式, $p$ 为素数, 且整数 $n \geq 2$. 若 $a$ 是方程 $f(x) \equiv 0$ $\left(\bmod p^{n-1}\right)$ 的解, 则同时满足 $y \equiv a\left(\bmod p^{n-1}\right)$ 与 $f(y) \equiv 0\left(\bmod p^{n}\right)$ 的模 $p$ 同余类 $y$ 的个数为

$$
\begin{cases}1, & \text { 若 } p \nmid f^{\prime}(a), \\ 0, & \text { 若 } p \mid f^{\prime}(a) \text { 且 } p^{n} \nmid f(a), \\ p, & \text { 若 } p \mid f^{\prime}(a) \text { 且 } p^{n} \mid f(a) .\end{cases}
$$

此即亨泽尔(Hensel)引理, 其证明见[1, Theorem 5.166].

以下记 $S_{r}$ 为 $\mathbb{Z}_{p^{k}}$ 中所有模 $p$ 余 $r$ 的数构成的集合.

推论 若 $p \mid P^{\prime}(r)$, 则 $\left|P\left(S_{r}\right)\right| \leq p^{k-2}$; 若 $p \nmid P^{\prime}(r)$, 则 $\left|P\left(S_{r}\right)\right|=p^{k-1}$.

证明 当 $p \mid P^{\prime}(r)$ 时, 考虑 $f(x)=P(x)-P(r)$. 令 $n=2$, 则根据引理可知:对 $y \equiv r(\bmod p)$ 均有 $P(y) \equiv P(r)\left(\bmod p^{2}\right)$. 因此 $P\left(S_{r}\right)$ 中所有数模 $p^{2}$ 同余,故 $\left|P\left(S_{r}\right)\right| \leq p^{k-2}$.

当 $p \nmid P^{\prime}(r)$ 时, 我们对正整数 $l$ 归纳证明: $P\left(S_{r}\right)$ 在模 $p^{l}$ 的意义下恰取到 $p^{l-1}$ 个剩余类.

当 $l=1$ 时结论显然成立. 假设 $l$ 的情形已经证明, 考虑 $l+1$ 的情形: 对每个 $P\left(S_{r}\right)$ 模 $p^{l-1}$ 的剩余类 $u \equiv P(t)\left(\bmod p^{l-1}\right)$, 考虑

$$
f_{i}(x)=P(x)-u-i p^{l-1} \quad(i=0,1, \ldots, p-1) .
$$

对这 $p$ 个多项式分别由引理得模 $p^{l}$ 意义下的剩余类

$$
u, u+p^{l-1}, \cdots, u+(p-1) p^{l-1}
$$

均在 $P\left(S_{r}\right)$ 中, 这就完成了归纳证明. 特别地, 取 $l=k$ 即证明了推论.

回到原题. 因为当 $m$ 充分大时 $f_{m, p^{k}}=1$, 所以由推论知存在最小的正整数 $m$, 满足:

- 存在 $r$ 使得 $\left|P^{m-1}\left(S_{r}\right)\right|=p^{k-1}$;
- 对任意 $q$ 均有 $\left|P^{m}\left(S_{q}\right)\right| \leq p^{k-2}$.

以下固定这组 $(m, r)$. 由于 $P^{m-1}\left(\mathbb{Z}_{p^{k}}\right) \backslash P^{m-1}\left(S_{r}\right)$ 在 $P$ 下的像包含 $P^{m}\left(\mathbb{Z}_{p^{k}}\right) \backslash P^{m}\left(S_{r}\right)$, 故

$$
\left|P^{m}\left(\mathbb{Z}_{p^{k}}\right) \backslash P^{m}\left(S_{r}\right)\right| \leq\left|P^{m-1}\left(\mathbb{Z}_{p^{k}}\right) \backslash P^{m-1}\left(S_{r}\right)\right|
$$

记 $a=\left|P^{m}\left(\mathbb{Z}_{p^{k}}\right) \backslash P^{m}\left(S_{r}\right)\right|$, 则

$$
a+p^{k-1} \leq f_{m-1, p^{k}} \leq 2 f_{m, p^{k}} \leq 2 p^{k-2}+2 a \Longrightarrow(p-2) p^{k-2} \leq a .
$$

因为对任意充分大的 $i$ 均有 $f_{i, p}=1$, 所以恰有一个 $t \in \mathbb{Z}_{p}$ 使得 $P(t) \equiv t$ $(\bmod p)$. 且 $t$ 满足: 集合 $\left\{s \in \mathbb{Z}_{p} \mid P^{i-1}(s) \equiv t(\bmod p)\right\}$ 的元素个数在达到 $p$ 之前关于 $i$ 严格单调递增. 因此

$$
\left|\left\{s \in \mathbb{Z}_{p} \mid P^{m-1}(s) \equiv t \quad(\bmod p)\right\}\right|=p
$$

或

$$
\left|\left\{s \in \mathbb{Z}_{p} \mid P^{m-1}(s) \equiv t \quad(\bmod p)\right\}\right| \geq m
$$

故或者 $f_{m-1, p}=1$, 或者 $X=\left\{s \in \mathbb{Z}_{p} \mid P^{m-1}(s) \equiv t(\bmod p)\right\}$ 满足 $|X| \geq m$.

若 $f_{m-1, p}=1$, 则 $\left|P^{m-1}\left(\mathbb{Z}_{p^{k}}\right)\right| \leq p^{k-1}=\left|P^{m-1}\left(S_{r}\right)\right|$, 即 $a=0$, 矛盾! 因此 $|X| \geq m$, 设

$$
Y=\left\{y \in \mathbb{Z}_{p^{k}} \mid \text { 存在 } x \in X \text { 使得 } y \equiv x \quad(\bmod p)\right\}, \quad Z=\mathbb{Z}_{p^{k}} \backslash Y \text {, }
$$

则 $P^{m-1}(Y) \subseteq S_{t}, P\left(S_{t}\right) \subsetneq S_{t}$, 且 $Z=\bigcup_{i \in \mathbb{Z}_{p} \backslash X} S_{i}$. 因此

$$
\left|P^{m}(Y)\right| \leq\left|P\left(S_{t}\right)\right| \leq p^{k-2}, \quad\left|P^{m}(Z)\right| \leq\left|\mathbb{Z}_{p} \backslash X\right| \cdot p^{k-2} \leq(p-m) p^{k-2},
$$

故

$(p-2) p^{k-2} \leq a<\left|P^{m}\left(\mathbb{Z}_{p^{k}}\right)\right|<\left|P^{m}(Y)\right|+\left|P^{m}(Z)\right| \leq(p-m+1) p^{k-2} \Rightarrow m<3$.

这表明对任意 $q \in \mathbb{Z}_{p}$ 均有 $\left|P^{2}\left(S_{q}\right)\right| \leq p^{k-2}$, 故 $\frac{p^{k}}{4} \leq\left|P^{2}\left(\mathbb{Z}_{p^{k}}\right)\right| \leq p^{k-1}$, 即 $p=3$.

设 $t \in \mathbb{Z}_{3}$ 使得 $P(t) \equiv t(\bmod 3)$. 若 $3 \nmid P^{\prime}(t)$, 则由推论可得 $P\left(S_{t}\right)=S_{t}$,从而 $f_{m, 3^{k}} \geq 3^{k-1}$ 对任意正整数 $m$ 成立, 这与 $f_{m, 3^{k}}=\left\lceil 3^{k} / 2^{m}\right\rceil$ 矛盾! 于是 $3 \mid P^{\prime}(t)$, 则由推论得

$$
P\left(t+3^{i} s\right) \equiv P(t) \quad\left(\bmod 3^{i+1}\right) \Rightarrow\left|P^{i}\left(S_{t}\right) \bmod 3^{i+1}\right|=1 \Rightarrow\left|P^{k-1}\left(S_{t}\right)\right|=1
$$

又因为 $f_{1,3} \leq 2, f_{2,3} \leq 1$, 所以 $P^{2}\left(\mathbb{Z}_{3^{k}}\right) \subseteq S_{t}$, 故 $\left|P^{k+1}\left(\mathbb{Z}_{3^{k}}\right)\right| \leq\left|P^{k-1}\left(S_{t}\right)\right|=1$,即 $3^{k} \leq 2^{k+1}$, 矛盾!

综上所述, 满足要求的正整数 $n$ 为全体素数与全体 2 的非负整数幂.
评注 本题的构造部分与证明部分的情形 1 均不太难, 但是证明 $n$ 为奇素数的幕时不存在满足要求的多项式(即情形 2) 却极为困难. 为了推导出矛盾, 需要对某个量进行两方面的放缩从而得到不等式估计. 这里所选的量 $a$ 很难被发现.经估计发现 $p=3$ 的情形需要单独解决, 而这相对容易. 值得一提的是, 本题在刻画结构的过程中多次使用亨泽尔(Hensel)引理, 这对知识面的要求较高.

本题预计难度 $55 \mathrm{M}$.

## 参考文献

[1] Titu Andreescu, Gabriel Dospinescu, and Oleg Mushkarov. Number Theory: Concepts and Problems. XYZ Press, LLC, 2017.

[2] Evan Chen. Euclidean Geometry in Mathematical Olympiads. The Mathematical Association of America, first edition, 2016.

[3] Evan Chen. Math Olympiad Hardness Scale (MOHS). 2022.

https://web.evanchen.cc/upload/MOHS-hardness.pdf

[4] 张世奇, 罗方舟. 2020 波兰数学奥林匹克(第二轮)试题解析. 数学新星网. 学生专栏, 2020-04-20 期.

[5] 王彬. 2021 年第二届百年老校数学竞赛试题解答. 数学新星网. 教师专栏, 2021-08-25 期.

