数学新星网 莫学生专栏

www.nsmath.cn/xszl

# 第四届国际大都市竞赛数学试题评析 

李逸凡 黄嘉俊

(上海市上海中学, 200231)

指导教师: 王广廷

第四届国际大都市竞赛 (IOM) 于 2019 年 9 月 1 日至 2019 年 9 月 6 日在莫斯科举行. 这次比赛共有来自全球 32 个国家、 45 座城市的 45 支队伍参赛.中国共有 5 支队伍受邀参赛, 分别来自北京、上海、成都、哈尔滨、香港. 比赛共分四个学科: 数学、物理、化学、计算机. 其中数学比赛采用标准 IMO 赛制,分两天, 每天四个半小时三道题, 每题 7 分. 虽然组委会声称难度接近 IMO, 但笔者认为这次考试的难度略低于 $\mathrm{CMO}$ 水平.

共有约 87 人参加了数学比赛, 金牌线为 28 分, 共有 10 人获得金牌. 银牌线为 21 分, 共有 20 人获得银牌. 铜牌线为 14 分, 共有 19 人获得铜牌. 我们有幸代表上海参加了本次比赛, 成绩是李逸凡 36 分, 黄嘉俊 31 分, 获得两枚金牌.

这次比赛受到了莫斯科市政府的高度关注, 参赛条件非常好, 试题质量高,命题风格和全俄罗斯数学奥林匹克比较接近, 可以作为高联、 $\mathrm{CMO}$ 训练的参考.

## I. 试 题

1. 设质数 $p, q$, 及正整数 $n$ 满足 $\frac{p+n}{q r}, \frac{q+n}{r p}$ 及 $\frac{r+n}{p q}$ 均为整数. 证明: $p=q=r$.
2. 在一个有固定有限个用户的社交网络里, 每一个用户拥有由其他用户组成的固定的追随者集合. 每一个用户拥有一个最初的正整数等级分(不一定所有的用户均相同). 每天午夜, 将每位用户的等级分加上在该时刻前他的所有追随者等级分之和作为他新的等级分. 设 $m$ 为正整数.一位不属于该网络的黑客, 希望使得所有用户的等级分均可被 $m$ 整除. 每一天, 他可以选择一位用户并将该用户的等级分加 1 , 或者什么也不做. 证明: 经过若干天后, 该黑客可以实现他的目标.

修订日期: 2019-11-04.

3. 非等边 $\triangle A B C$ 中, $I$ 为内心, $O$ 为外心. 过 $I$ 作直线 $s$ 垂直于 $I O$. 直线 $l$与直线 $B C$ 关于 $s$ 对称, 并与 $A B, A C$ 分别相交于点 $P, Q(P, Q$ 均不与 $A$ 重合).证明: $\triangle A P Q$ 的外心位于直线 $I O$ 上.
4. 有 100 个学生参加某个考试 (成绩只有“通过”或“不通过”两种). 由一个教授依次面试每一个学生, 且对每一个学生, 他只有一个问题: “在该考试结束时, 这 100 个学生中有多少人的成绩是“通过”?" 每个学生的答案必须是一个整数, 一旦该学生报出他的答案, 教授立即公开宣布该学生的成绩是“通过”或“不通过”。

在所有学生都得到自己的成绩后, 由监察员检查是否有学生虽然正确回答了考试成绩为“通过”的人数, 但他的成绩被教授宣布为“不通过”. 如果至少存在一个这样的学生, 则责令教授停职, 并且所有学生的成绩均改为“通过”: 如果不存在这样的学生, 则原成绩不作任何改动.

问这些学生能否想出一个策略, 确保每个人最后的成绩均为“通过”?

5. 给定一个顶点为 $O$, 底面为 $A B C D$ 的凸四棱雉, 且该四棱雉有内切球(即在其内部并与各面均相切的球). 沿棱 $O A, O B, O C, O D$ 将该四棱雉剪开, 并将侧面 $O A B, O B C, O C D, O D A$ 向外翻转至平面 $A B C D$ 内, 形成多边形 $A K B L C M D N$. 证明: $K, L, M, N$ 四点共圆.
6. 设 $p$ 为质数, $f(x)$ 为整系数 $d$ 次多项式. 已知当 $f(1), f(2), \cdots, f(p)$ 被 $p$ 除时, 恰有 $k$ 个互不相同的余数, 其中 $1<k<p$. 证明:

$$
\frac{p-1}{d} \leq k-1 \leq(p-1)\left(1-\frac{1}{d}\right)
$$

## II . 解答与评析

1. 设质数 $p, q$, 及正整数 $n$ 满足 $\frac{p+n}{q r}, \frac{q+n}{r p}$ 及 $\frac{r+n}{p q}$ 均为整数. 证明: $p=q=r$.

证明 不妨设 $p \leq q \leq r$. 由题知 $r|p+n, r| q+n$, 故 $r \mid q-p$. 而

$$
r \geq q>q-p \geq 0
$$

故 $p-q=0$, 即 $p=q$. 又由于 $p q|r+n, p r| q+n$, 得到 $p \mid r-q$.

考虑到 $p=q$, 有 $p \mid r$. 由于 $r$ 为素数, 因此 $p=r$.

综上得到 $p=q=r$.

评注 这是一道简单题, 只需对条件进行等价分析即可得证.

2. 在一个有固定有限个用户的社交网络里, 每一个用户拥有由其他用户组成的固定的追随者集合. 每一个用户拥有一个最初的正整数等级分(不一定所有的用户均相同). 每天午夜, 将每位用户的等级分加上在该时刻前他的所有追随者等级分之和作为他新的等级分. 设 $m$ 为正整数.一位不属于该网络的黑客, 希望使得所有用户的等级分均可被 $m$ 整除.每一天,他可以选择一位用户并将该用户的等级分加 1 , 或者什么也不做. 证明：经过若千天后,该黑客可以实现他的目标.

证明 将 $n$ 个人编号为 $1,2, \cdots, n$. 定义矩阵 $A_{n \times n}$, 其中元素 $a_{i j}$ 定义如下:

$$
a_{i j}= \begin{cases}1, & j \text { 为 } i \text { 的追随者或 } j=i, \\ 0, & j \text { 不为 } i \text { 的追随者. }\end{cases}
$$

令 $i$ 第 $m$ 天的等级分为 $h_{i}^{(m)}$ (初始状态视为第 0 天), 若不考虑黑客, 则

$$
h_{i}^{(m+1)}=\sum_{j=1}^{n} a_{i j} h_{j}^{(m)}
$$

从而

$$
\left(\begin{array}{cccc}
a_{11} & a_{12} & \ldots & a_{1 n} \\
a_{21} & a_{22} & \ldots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \ldots & a_{n n}
\end{array}\right)\left(\begin{array}{c}
h_{1}^{(m)} \\
h_{2}^{(m)} \\
\vdots \\
h_{n}^{(m)}
\end{array}\right)=\left(\begin{array}{c}
h_{1}^{(m+1)} \\
h_{2}^{(m+1)} \\
\vdots \\
h_{n}^{(m+1)}
\end{array}\right)
$$

将上式用矩阵表示, 记

$$
A=\left(\begin{array}{cccc}
a_{11} & a_{12} & \ldots & a_{1 n} \\
a_{21} & a_{22} & \ldots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \ldots & a_{n n}
\end{array}\right), X^{(m)}=\left(\begin{array}{c}
h_{1}^{(m)} \\
h_{2}^{(m)} \\
\vdots \\
h_{n}^{(m)}
\end{array}\right)
$$

有 $X^{(m+1)}=A X^{(m)}$.

令 $I^{(k)}=(\underbrace{0,0, \cdots, 0,1}_{k}, 0, \cdots, 0)^{T}$ 为第 $k$ 位为 1 其余均为零的矩阵, 则黑客的作用相当于在某一次给 $X^{(m)}$ 加上了某个 $I^{(k)}$. 从而只需证存在某一个 $M$, 及 $i_{1}, i_{2}, \cdots, i_{u}, k_{1}, k_{2}, \cdots k_{u}$ 使得

$$
A^{M} X^{(0)}+A^{M-i_{1}} I^{\left(k_{1}\right)}+A^{M-i_{2}} I^{\left(k_{2}\right)}+\cdots+A^{M-i_{u}} I^{\left(k_{u}\right)}
$$

的每一位均为 $m$ 的倍数.

定义两个矩阵 $A \equiv B(\bmod m)$ 为

$$
A \equiv B \quad(\bmod m) \Leftrightarrow A, B \text { 的每一位模 } m \text { 相同. }
$$

容易验证, 若 $A \equiv B(\bmod m), C \equiv D(\bmod m)$, 则

(i) $A+C \equiv B+D(\bmod m)$;

(ii) $A C \equiv B D(\bmod m)$.

于是先找 $k_{1}, k_{2}, \cdots, k_{u}$ 使得

$$
X^{(0)}+I^{\left(k_{1}\right)}+I^{\left(k_{2}\right)}+\cdots+I^{\left(k_{u}\right)} \equiv 0 \quad(\bmod m) .
$$

这显然可以办到, 下面只需让 $A^{M} \equiv A^{M-i_{1}} \equiv A^{M-i_{2}} \equiv \cdots \equiv A^{M-i_{u}}(\bmod m)$成立即可. 而 $A^{X}(X=1,2, \cdots)$ 在模 $m$ 意义下至多 $m^{n^{2}}$ 种取值. 因此必定存在无穷多个 $X$, 它们对应的 $A^{X}$ 模 $m$ 相同.

本题得证!

评注 笔者认为这道题较难, 难度比 3 要大. 关键之处在于矩阵的思想, 不熟悉矩阵的人做这道题会比较棘手. 本题的实质就是对“等级分矩阵”左乘一个“变换矩阵”, 将若干天后的状态用明确的表达式表述出来, 后面就变得比较简单了,解答也可以不用矩阵用变换来写. 而且本题还容易陷入对 $m$ 素因子分解或递推的方法中, 但可行性较低.

3. 非等边 $\triangle A B C$ 中, $I$ 为内心, $O$ 为外心. 过 $I$ 作直线 $s$ 垂直于 $I O$. 直线 $l$与直线 $B C$ 关于 $s$ 对称, 并与 $A B, A C$ 分别相交于点 $P, Q(P, Q$ 均不与 $A$ 重合).证明: $\triangle A P Q$ 的外心位于直线 $I O$ 上.

证明 不妨假设 $A B>A C$. 作 $I$ 关于 $B C$ 的对称点 $I^{\prime}, A$ 关于 $O I$ 的对称点 $A^{\prime}$, 记 $A I$ 交 $\odot O$ 于 $M, A M$ 与 $B C$ 交于 $U, P Q$ 与 $B C$ 交于 $K$.

由 $A, A^{\prime}$ 关于 $O I$ 对称, 故

$$
\angle O I A^{\prime}+\angle O I M=\angle O I A+\angle O I M=180^{\circ} .
$$

又 $O M=O A^{\prime}$, 故 $O, I, A^{\prime}, M$ 共圆. 由欧拉定理, 可知

$$
I A \cdot I M=2 O A \cdot r=O A \cdot I I^{\prime},
$$

其中 $r$ 为 $\triangle A B C$ 的内切圆半径. 又

$$
\begin{aligned}
\angle M I I^{\prime} & =90^{\circ}-\angle I U C=90^{\circ}-\angle A B C-\angle I A C \\
& =\angle O A C-\angle I A C=\angle O A I .
\end{aligned}
$$

故 $\triangle I A O \sim \triangle I^{\prime} I M$, 所以

$$
\angle I M A^{\prime}=\angle A^{\prime} O I=\angle A O I=\angle A M I^{\prime} .
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_49878b8888620439ebb8g-05.jpg?height=594&width=645&top_left_y=206&top_left_x=708)

故 $M, I^{\prime}, A^{\prime}$ 三点共线. 由 $I, I^{\prime}$ 关于 $B C$ 对称, 得到 $\angle I K B=\angle I^{\prime} K B$. 故

$$
\begin{aligned}
\measuredangle\left(I K, I^{\prime} K\right) & =2 \measuredangle(I K, B C)=2\left(\measuredangle(O I, B C)-90^{\circ}\right) \\
& =2 \measuredangle(O I, O M)=2 \measuredangle\left(A^{\prime} I, A^{\prime} I^{\prime}\right) .
\end{aligned}
$$

因此 $K$ 为 $\triangle A^{\prime} I^{\prime} I$ 的外心. 故

$$
\begin{aligned}
& \measuredangle\left(P B, A^{\prime} B\right)-\measuredangle\left(P K, A^{\prime} K\right) \\
= & \measuredangle(A O, O I)-\measuredangle(I K, C K)+2 \measuredangle\left(M A^{\prime}, I I^{\prime}\right)-180^{\circ} \\
= & \measuredangle(A O, O I)-\measuredangle(I K, B C)-2 \measuredangle\left(B C, M A^{\prime}\right) \\
= & \measuredangle(A O, O I)+90^{\circ}-\measuredangle(O I, B C)-2 \measuredangle(B C, A I)+2 \measuredangle(O I, A O) \\
= & -\measuredangle(B C, A O)+90^{\circ}-2 \measuredangle(B C, A I) \\
= & -\measuredangle(A O, A I)+90^{\circ}-\measuredangle(B C, A I) \\
= & 0 .
\end{aligned}
$$

故 $\measuredangle\left(P B, A^{\prime} B\right)=\measuredangle\left(P K, A^{\prime} K\right)$. 因此 $P B K A^{\prime}$ 共圆. 考虑到 $A B A^{\prime} C$ 共圆, 由密克定理知 $A P A^{\prime} Q$ 共圆. 所以 $\triangle A P Q$ 的外心在 $A A^{\prime}$ 中垂线上, 即在 $O I$ 上.

评注 容易取出 $A$ 关于 $O I$ 对称点 $A^{\prime}$, 故只要证 $A P A^{\prime} C$ 共圆即可. 由密克定理, 只要证 $A^{\prime} B P K$ 共圆. 这等价于 $\angle A^{\prime} K P=\angle A^{\prime} B P$, 故只需确定 $A^{\prime} K$ 的方向即可. 笔者在这里取出了关于 $I$ 关于 $B C$ 的对称点 $I^{\prime}$, 通过证明 $K$ 为 $\triangle I I^{\prime} A$的圆心来确定 $I^{\prime} K$ 方向 (笔者之前证过 $M, I^{\prime}, A^{\prime}$ 三点共线, 故可以想出), 之后的过程只需导角即可.

4. 有 100 个学生参加某个考试 (成绩只有“通过”或“不通过”两种). 由一个教授依次面试每一个学生, 且对每一个学生, 他只有一个问题:“在该考试结束时, 这 100 个学生中有多少人的成绩是“通过”?”每个学生的答案必须是一个整
数,一旦该学生报出他的答案, 教授立即公开宣布该学生的成绩是“通过”或“不通过”。

在所有学生都得到自己的成绩后, 由监察员检查是否有学生虽然正确回答了考试成绩为“通过”的人数, 但他的成绩被教授宣布为“不通过”. 如果至少存在一个这样的学生, 则责令教授停职, 并且所有学生的成绩均改为“通过”: 如果不存在这样的学生, 则原成绩不作任何改动.

问这些学生能否想出一个策略, 确保每个人最后的成绩均为“通过”?

解 可以得到一个确保每个人最后的成绩均为“通过”的策略.

给 100 个学生标号为 $1,2, \cdots, 100$, 设第 $i$ 个学生给出的答案为 $a_{i}$. 给定 $a_{1}=99$, 其余人答案按照如下规则给出

$$
a_{i+1}=\left\{\begin{array}{ll}
a_{i} & (i \text { 通过 }) \\
a_{i}-1 & (i \text { 未通过 })
\end{array} .\right.
$$

若教授给 100 个人通过, 则得证. 若不, 设教授最后一个给 $i$ “未通过”, 此时 $a_{i}$ 为 99 减去前 $i-1$ 位学生中未通过的人数, 即 100 减去前 $i$ 个学生中未通过的人数,也就是通过的人数. 因此该学生的回答正确, 由题意知此时教授停职, 并且所有学生的成绩均改为“通过”。

评注 本题是一道简单题, 易发现 $a_{1}$ 只能等于 99 , 否则教授给 1 不通过, 后 99 个人通过即可. 此后, 若教授给 1 不通过, 同理 $a_{2}$ 只能等于 98 , 若 1 通过, $a_{2}$只能等于 99. 类似的枚举几项后可找到规律.

5. 给定一个顶点为 $O$, 底面为 $A B C D$ 的凸四棱锥, 且该四棱锥有内切球(即在其内部并与各面均相切的球). 沿棱 $O A, O B, O C, O D$ 将该四棱锥剪开, 并将侧面 $O A B, O B C, O C D, O D A$ 向外翻转至平面 $A B C D$ 内, 形成多边形 $A K B L C M D N$. 证明: $K, L, M, N$ 四点共圆.

证明 记该四棱雉的内切球球心为 $O_{1}$, 内切球半径为 $d$. 作球 $O_{2}$, 使 $O, O_{1}, O_{2}$三点共线, 且 $\frac{O O_{1}}{O O_{2}}=\frac{d}{d^{\prime}}$, 其中 $d^{\prime}$ 为球 $O_{2}$ 的半径. 必存在 $O_{2}$, 使球 $O_{2}$ 与面 $A B C D$相切, 且 $O_{2} \neq O_{1}$, 此时球 $O_{2}$ 与面 $O A B$, 面 $O B C$, 面 $O C D$, 面 $O A D$ 也都相切.记 $O_{2}$ 在平面 $A B K$ 的投影为 $O_{2}^{\prime}, O_{2}$ 在平面 $O A B$ 的投影为 $O_{2}^{\prime \prime}$. 因为球 $O_{2}$ 与平面 $O A B$ 和平面 $A B K$ 均相切, 故有 $O_{2}$ 到平面 $O A B$ 与平面 $A B K$ 的距离相等,即 $\mathrm{O}_{2} \mathrm{O}_{2}^{\prime}=\mathrm{O}_{2} \mathrm{O}_{2}^{\prime \prime}$. 考虑到

$$
O_{2}^{\prime} A=\sqrt{O_{2} A^{2}-O_{2} O_{2}^{\prime 2}}=\sqrt{O_{2} A^{2}-O_{2} O_{2}^{\prime \prime 2}}=O_{2}^{\prime \prime} A
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_49878b8888620439ebb8g-07.jpg?height=528&width=759&top_left_y=204&top_left_x=654)

$$
O_{2}^{\prime} B=\sqrt{O_{2} B^{2}-O_{2} O_{2}^{\prime 2}}=\sqrt{O_{2} B^{2}-O_{2} O_{2}^{\prime \prime 2}}=O_{2}^{\prime \prime} B
$$

结合 $A B=A B$. 得到

$$
\triangle A B O_{2}^{\prime \prime} \cong \triangle A B O_{2}^{\prime}
$$

再结合 $\triangle A B K \cong \triangle O A B$, 知四边形 $K A B O_{2}^{\prime}$ 与四边形 $O B A O_{2}^{\prime \prime}$ 全等, 故

$$
O_{2}^{\prime \prime} O=O_{2}^{\prime} K
$$

结合 $O_{2} O_{2}^{\prime}=O_{2} O_{2}^{\prime \prime}$, 及 $O_{2} O_{2} \perp$ 平面 $A B K, O_{2} O_{2}^{\prime \prime} \perp$ 平面 $O A B$ 得到

$$
O_{2} K=\sqrt{O_{2}^{\prime} K^{2}+O_{2} O_{2}^{\prime 2}}=\sqrt{O_{2}^{\prime \prime} O^{2}+O_{2} O_{2}^{\prime \prime 2}}=O O_{2}
$$

同理可得

$$
O_{2} L=O O_{2}, O_{2} M=O O_{2}, O_{2} N=O O_{2}
$$

故

$$
O_{2}^{\prime} K=\sqrt{O_{2} K^{2}-O_{2} O_{2}^{\prime 2}}=\sqrt{O_{2} L^{2}-O_{2} O_{2}^{\prime 2}}=O_{2}^{\prime} L .
$$

同理可知

$$
O_{2}^{\prime} K=O_{2}^{\prime} L=O_{2}^{\prime} M=O_{2}^{\prime} N
$$

即 $K, L, M, N$ 四点共圆.

评注 笔者最初的想法是直接找出 $K, L, M, N$ 外接圆圆心, 从而证明四点共圆. 但是该方法难以运用题中条件, 于是便放弃. 后来笔者发现到 $K$ 与 $O$ 距离相同的点所构成的平面较容易刻画, 进而想到是否可以做出 $O, K, L, M, N$ 的球心从而证明共圆(容易发现 $K, L, M, N$ 共圆与 $O, K, L, M, N$ 共球等价).因此只要证明存在点 $T$, 使平面 $T A B$ 与 $O_{1} A B$ 垂直, 平面 $T B C$ 与 $O_{1} B C$ 垂直,平面 $T D C$ 与 $O_{1} D C$ 垂直, 平面 $T D A$ 与 $O_{1} D A$ 垂直. 笔者一开始想到了一个代数的证明, 但后来发现 $O, K, L, M, N$ 的旁切球球心直接符合这些条件, 于是
只要证明旁切球存在, 而这是显然的.

6. 设 $p$ 为质数, $f(x)$ 为整系数 $d$ 次多项式. 已知当 $f(1), f(2), \cdots, f(p)$ 被 $p$ 除时, 恰有 $k$ 个互不相同的余数, 其中 $1<k<p$. 证明:

$$
\frac{p-1}{d} \leq k-1 \leq(p-1)\left(1-\frac{1}{d}\right)
$$

证明 我们需要如下的引理.

引理 若 $1 \leq n \leq p-2$, 则 $p \mid 1^{n}+\cdots+(p-1)^{n}+p^{n}$.

引理的证明 取模 $p$ 的原根 $a$. 由 $(a, p)=1$ 可得 $a, 2 a, \cdots, p a$ 构成模 $p$ 完系. 故

$$
1^{n}+\cdots+p^{n} \equiv a^{n}+\cdots+(p a)^{n}(\bmod p)
$$

即

$$
\left(a^{n}-1\right)\left(1^{n}+\cdots+p^{n}\right) \equiv 0 \quad(\bmod p) .
$$

因此 $\left(a^{n}-1\right)\left(1^{n}+\cdots+p^{n}\right) \equiv 0(\bmod p)$, 引理得证.

回到原题. $f(x)$ 的次数为 $d, f(x)$ 模 $p$ 有 $k$ 个值, 其中 $2 \leq k \leq p-1$. 设 $f(x)$ $\bmod p$ 的 $k$ 个值构成的集合为 $\left\{S_{1}, S_{2}, \cdots, S_{k}\right\}$.

$$
\begin{gathered}
\text { 记 } f(x)=\sum_{j=0}^{d} a_{j} x^{j},(f(x))^{n}=\sum_{j=0}^{n d} a_{n, j} x^{j} \text {. 当 } n d \leq p-2 \text { 时, 有 } \\
\sum_{i=1}^{p}(f(i))^{n} \equiv \sum_{i=1}^{p} \sum_{j=0}^{n d} a_{n, j} i^{j} \equiv \sum_{j=0}^{n d} a_{n, j} \sum_{i=1}^{p} i^{j} \equiv 0 \quad(\bmod p) .
\end{gathered}
$$

若 $(k-1) d \leq p-2$, 则

$$
\begin{aligned}
& \sum_{i=1}^{p}\left(f(i)-S_{1}\right) \cdots\left(f(i)-S_{k-1}\right) \\
= & \sum_{i=1}^{p} \sum_{l=0}^{k-1}(-1)^{k-1-l} f(i)^{l} \sum_{1 \leq i_{1}<\cdots<i_{k-1-l} \leq k-1} S_{i_{1}} \cdots S_{i_{k-1-l}} \\
= & \sum_{l=0}^{k-1}(-1)^{k-1-l} \sum_{1 \leq i_{1}<\cdots<i_{k-1-l} \leq k-1} S_{i_{1}} \cdots S_{i_{k-1-l}} \sum_{i=1}^{p} f(i)^{l} \\
\equiv & 0 \quad(\bmod p) .
\end{aligned}
$$

记 $\alpha_{k}$ 为 $f(x) \equiv S_{k}$ 的个数, 有

$$
\sum_{i=1}^{p}\left(f(i)-s_{1}\right) \cdots\left(f(i)-s_{k-1}\right)=\alpha_{k}\left(S_{k}-S_{1}\right) \cdots\left(S_{k}-S_{k-1}\right) \not \equiv 0 \quad(\bmod p)
$$

矛盾.
故

$$
(k-1) d \geq p-1,(k-1) \geq \frac{p-1}{d}
$$

设 $f(x) \equiv S_{i}(\bmod p)$ 共有 $\alpha_{i}$ 个解. 取 $t_{1}^{\prime}, \cdots, t_{p-k}^{\prime}$, 使 $t_{1}^{\prime}, \cdots, t_{p-k}^{\prime}$ 中恰有 $\alpha_{i}-1$ 个 $S_{i}$. 取 $t_{1}, \cdots, t_{p-k}$, 使 $t_{1}, \cdots, t_{p-k}, S_{1}, \cdots, S_{k}$ 是模 $p$ 的完系.

由 $(*)$ 式, 当 $n d \leq p-2$ 时, 有

$$
\begin{aligned}
0 & \equiv \sum_{i=1}^{p}(f(i))^{n} \equiv \sum_{i=1}^{p}(f(i))^{n}-\left(1^{n}+\cdots+p^{n}\right) \\
& \equiv\left(t_{1}^{\prime}\right)^{n}+\cdots+\left(t_{p-k}^{\prime}\right)^{n}-\left(t_{1}^{n}+\cdots+t_{p-k}^{n}\right) \quad(\bmod p) .
\end{aligned}
$$

若 $(p-k) d \leq p-2$, 则对任意 $0 \leq n \leq p-k$ 都有

$$
\left(t_{1}^{\prime}\right)^{n}+\cdots+\left(t_{p-k}^{\prime}\right)^{n} \equiv t_{1}^{n}+\cdots+t_{p-k}^{n} \quad(\bmod p)
$$

成立.

记

$$
\begin{aligned}
& g(x)=\left(x-t_{1}\right) \cdots\left(x-t_{p-k}\right)=\sum_{i=0}^{p-k} \epsilon_{i} x^{p-k-i} \\
& g^{\prime}(x)=\left(x-t_{1}^{\prime}\right) \cdots\left(x-t_{p-k}^{\prime}\right)=\sum_{i=0}^{p-k} \epsilon_{i}^{\prime} x^{p-k-i} .
\end{aligned}
$$

下面归纳证明 $\epsilon_{i} \equiv \epsilon_{i}^{\prime}(\bmod p)$.

$$
i=0 \text { 时, } \epsilon_{i}=\epsilon_{i}^{\prime}=1 \text {. }
$$

$i=1$ 时, 等价于 $(* *)$ 式中 $n=1$ 的情况.

归纳假设小于 $i$ 时结论成立. 由牛顿幂和公式

$$
\begin{aligned}
t_{1}^{i}+\cdots+t_{p-k}^{i}= & -\left(t_{1}+\cdots+t_{p-k}\right) \epsilon_{i-1}-\left(t_{1}^{2}+\cdots+t_{p-k}^{2}\right) \epsilon_{i-2}-\cdots \\
& -\left(t_{1}^{i-1}+\cdots+t_{p-k}^{i-1}\right) \epsilon_{1}-i \epsilon_{i} \\
\left(t_{1}^{\prime}\right)^{i}+\cdots+\left(t_{p-k}^{\prime}\right)^{i}= & -\left(t_{1}^{\prime}+\cdots+t_{p-k}^{\prime}\right) \epsilon_{i-1}^{\prime}-\left(\left(t_{1}^{\prime}\right)^{2}+\cdots+\left(t_{p-k}^{\prime}\right)^{2}\right) \epsilon_{i-2}^{\prime}-\cdots \\
& -\left(\left(t_{1}^{\prime}\right)^{i-1}+\cdots+\left(t_{p-k}^{\prime}\right)^{i-1}\right) \epsilon_{1}^{\prime}-i \epsilon_{i}^{\prime} .
\end{aligned}
$$

两式相减, 再结合 $(* *)$ 式及归纳假设知: $i \epsilon_{i} \equiv i \epsilon_{i}^{\prime}(\bmod p)$. 又 $i \leq p-k$, 故 $\epsilon_{i} \equiv \epsilon_{i}^{\prime}$ $(\bmod p)$, 结论成立.

由此得 $g(x) \equiv g^{\prime}(x)(\bmod p)$, 而

$$
0 \equiv g\left(t_{1}\right) \equiv g^{\prime}\left(t_{1}\right) \not \equiv 0 \quad(\bmod p)
$$

矛盾. 因此 $(p-k) d \geq p-1$, 变形即得到

$$
k-1 \leq(p-1)\left(1-\frac{1}{d}\right)
$$

命题得证!

评注 看到左式容易想到拉格朗日定理, 但无法放出左边的结果. 之后笔者又想到了利用 $p \mid 1^{k}+\cdots+p^{k}$ 可得 $p \mid f(1)^{k}+\cdots+f(p)^{k}$, 进一步可得

$$
p \left\lvert\, \sum_{i=1}^{p} g(f(i)) \quad\left(\operatorname{deg} g \leq \frac{p-2}{d}\right)\right.
$$

这样左式基本就解决了. 右式稍有些难度, 若直接考虑 $S=\{f(x) \bmod p\}$ 不太方便, 故可考虑 $\bar{S}$ 较为容易 (估计这一步转化会比较困难). 之后的操作都十分自然, 对一些能力较高的同学应该没有问题.

## III. 总评

本次考试第一题, 第四题相对容易, 应为联赛第一题难度. 第二题的做法中要用到矩阵, 对矩阵不熟悉可能会造成困难. 第五题以立体几何为载体, 在国内竞赛中不常见. 作为压轴题的三、六两题真正难度并没有那么高. 整体而言, 这是一套难度略低于冬令营的题.

