# 正方形区域中点构成的三角形的探究 

朱磊克<br>(江苏省苏州中学, 215000)

单墫老师在《奥数教程》 ${ }^{22]}$ 中有一道例题, 要求证明 9 个点在边长为 2 的正方形中, 必然存在三个点面积不超过 $\frac{1}{2}$; 田廷彦老师在《组合几何》[1] 中明确指出 6 个点在单位正方形中, 必有三个点构成的三角形面积不超过 $\frac{1}{8}$, 由下面两种结构差异较大的使等号成立的情况可知, 此问题较为困难. 本文给出了此问题的一种证明, 为证明此问题给出了四个引理的证明. 其中, 引理 2 与引理 4 的证明具有一定的巧妙之处, 也可以独立成题.


问题 单位正方形中有 6 个点, 无三点共线, 则必存在 3 个点构成的三角形面积不超过 $\frac{1}{8}$, 且 $\frac{1}{8}$ 是最优的界.

结合一个事实: 线性变化前后, 部分与整体的比值不发生改变. 我们可以知道单位正方形可以改成任意面积为 1 的平行四边形.

用 $S_{\min }(T)$ 表示集合 $T$ 中任意三点构成的三角形面积的最小值.

引理 13 个点任意放在一个平行四边形中, 包括边界, 这个点的面积不超过平行四边形的 $\frac{1}{2}$.

证明 $A, B, C$ 在平行四边形 $G H I J$ 中, 考虑坚直方向, 不妨设 $C$ 在 $A$,修订日期: 2023-12-21.



$B$ 之间, 过 $C$ 作 $H I$ 的平行线与平行四边形 $G H I J$ 交于点 $E, F$, 与 $A B$ 交于点 $D$. 则有

$$
S_{\triangle A B C}=S_{\triangle D B C}+S_{\triangle A D C} \leq \frac{1}{2} S_{E H I F}+\frac{1}{2} S_{E G J F}=\frac{1}{2} S_{H I J G}
$$

引理 1 证毕!

引理 2 凸包为四边形的 6 个点, 任意三点组成的三角形中面积最大值记作 $S_{1}$, 面积最小值记作 $S_{2}$, 则 $\frac{S_{1}}{S_{2}} \leq \frac{1}{4}$.


证明 设 $E F$ 在四边形 $A B C D$ 内部.

(1) 直线 $E F$ 与四边形 $A B C D$ 的交点必然在邻边上, 不妨设在 $\triangle A C D$ 内部, 则 $\triangle A C D$ 可以三角剖分成 5 个三角形, 从而 $\frac{S_{1}}{S_{2}} \leq \frac{1}{5}$.

(2) 直线 $E F$ 与四边形 $A B C D$ 的交点必然在对边上. 设 $F E$ 与 $B C$ 交于点 $G$, 与 $A D$ 交于点 $H$. 同时假设 $H F \geq E G$, 则

$$
\begin{aligned}
S_{1} & \geq S_{\triangle B C H} \\
& =S_{\triangle B C E}+S_{\triangle B E F}+S_{\triangle C E F}+S_{B F C H} \\
& \geq 2 S_{\triangle B C E}+S_{\triangle B E F}+S_{\triangle C E F} \\
& \geq 4 S_{2}
\end{aligned}
$$

从而, $\frac{S_{1}}{S_{2}} \leq \frac{1}{4}$.

引理 3 面积为 $\frac{1}{2}$ 的三角形中, 内部以及边界上有四个点, 且这四个点构成的凸包为凸四边形, 则其中必有三个点构成的三角形面积不超过 $\frac{1}{8}$.


证明 不难看出, 若 $A^{\prime}$ 在 $C A$ 延长线上, 则

$$
S(\{A, B, C, D\}) \leq S\left(\left\{A^{\prime}, B, C, D\right\}\right),
$$

因此不妨设 $A, B, C, D$ 四个点均在 $\triangle X Y Z$ 的边界上. 若存在一边不含任何给定点, 则如上图所示, 我们可以考虑 $A, B, C, D$ 所构成三角形在 $\triangle X C Y$ 的占比.

因此, 可以不妨设 $A, B$ 从左往右分布在边 $Y Z$ 上, $D$ 在边 $X Y$ 上, $C$ 在边 $X Z$ 上, 且设 $a=\frac{X D}{X Y}$, 则 $a \geq \frac{X C}{X Z}$.

过 $D$ 作 $X Z$ 的平行线, 与 $Y Z$ 交于点 $F$, 则

$$
S_{\triangle D Z F}=S_{\triangle D C F}=\frac{1}{2} a(1-a) \leq \frac{1}{8}
$$

若 $A$ 在线段 $Y F$ 上, 则 $S_{\triangle D C A} \leq S_{\triangle D C F} \leq \frac{1}{8}$.

若 $A$ 在线段 $F Z$ 上, 则 $B$ 也在线段 $F Z$ 上, $S_{\triangle A B D} \leq S_{\triangle F Z D} \leq \frac{1}{8}$. 从而,引理 3 成立.

引理 4 单位正方形 $A X Y Z$ 中分布着六个点, 其中 $B, C, D, E$ 分别在正方形的四条边处, 其不在顶点处, $F$ 在五边形 $A B C D E$ 内部, 求证: $A, B, C, D$, $E, F$ 这 6 个点中, 存在三个点构成的三角形面积不超过 $\frac{1}{8}$.


证明 以 $A$ 为原点, $A Z$ 为 $x$ 轴, $A X$ 为 $y$ 轴建立直角坐标系. 假设结论不成立, 存在合适的分布, 使得 $S_{\text {min }}(\{A, B, C, D, E, F\})>\frac{1}{8}$. 值得注意的是, 由
于仿射变换不改变部分占整体的比值, 因此, 单位正方形可以改成任意面积为 1 的平行四边形.

(1) $F(a, b)$ 在 $\triangle A E B$ 内部, 但是在 $\triangle A C B, \triangle A E D$ 外部时,

$$
S_{\triangle A E F}=S_{\triangle A I E}+S_{\triangle A F I}+S_{\triangle A E I}>\frac{3}{4}
$$

因此, $A E>\frac{3}{4} ; A F>\frac{3}{4}$. 又,

$$
\frac{1}{4}<2 S_{\triangle E B F} \leq 2 S_{\triangle X F Z}=1-a-b
$$

即

$$
a+b<\frac{3}{4} .
$$

故

$$
2 S_{\triangle A B C}>\frac{1}{4} \Rightarrow C Z>\frac{1}{4} .
$$

同理 $D X>\frac{1}{4}$.

取 $Y Z, A Z$ 边靠近 $Z$ 点的四等分点分别为 $J, K, Y Z$ 靠近 $Z$ 点的三等分点为 $L$, 则有

$$
b-\frac{a}{4}=2 S_{A F J}>2 S_{A F C}>\frac{1}{4} .
$$

同理,

$$
a-\frac{b}{4}>\frac{1}{4}
$$

于是,

$$
\frac{3}{4} \min \{a, b\} \geq \min \{a, b\}-\frac{\max \{a, b\}}{4}>\frac{1}{4} \Rightarrow \min \{a, b\}>\frac{1}{3} .
$$

若 $\min \{C Z, D X\}<\frac{1}{3}$, 不妨设 $C Z<\frac{1}{3}$. 注意到,

$$
0 \leq 2 S_{\triangle F J K}=\left|\begin{array}{ccc}
a & 0.75 & 1 \\
b & 0 & \frac{1}{3} \\
1 & 1 & 1
\end{array}\right|=\frac{1}{4}+\frac{b}{4}-\frac{a}{3}<\frac{1}{4}
$$

从而 $S_{\triangle F B C}<S_{\triangle F K L}<\frac{1}{4}$. 矛盾. 这是因为 (1) $\times\left(-\frac{1}{3}\right)+$ (2)得:

$$
\frac{2}{3} a-\frac{7}{12} b>0 \Rightarrow \frac{a}{3}>\frac{7}{24} b>\frac{b}{4} .
$$

若 $\min \{C Z, D X\} \geq \frac{1}{3}$, 有

$$
b-\frac{a}{3}=2 S_{A F J}>2 S_{A F C}>\frac{1}{4} .
$$

同理 $a-\frac{b}{3}>\frac{1}{4}$, 结合 1 , 有

$$
2=2(1-a-b)+3\left(a-\frac{b}{3}\right)+3\left(b-\frac{a}{3}\right)>\frac{8}{4}=2,
$$

矛盾.

(2) $F(a, b)$ 在 $\triangle A E B$ 内部, 也在 $\triangle A C B, \triangle A E D$ 之一内部时, 设其在 $\triangle A B C$ 内部, 延长 $A F$ 交 $Y Z$ 与 $L$, 延长 $B F$ 交 $A X$ 与点 $M$.


注意到, $\frac{B F}{B M}<1-a ; \frac{A F}{A L}=a$. 从而,

$$
\frac{S_{\triangle A F C}+S_{\triangle A F B}}{S_{\triangle A C Z}}+\frac{S_{\triangle B F E}+S_{\triangle A F B}}{S_{\triangle A E B}}<\frac{A F}{A L}+\frac{B F}{B M}<1 .
$$

结合引理 1 可知, $S_{\triangle A C Z}<\frac{1}{2}, S_{\triangle B E A}<\frac{1}{2}$, 从而,

$$
\min \left\{S_{\triangle A F C}, S_{\triangle A F B}, S_{\triangle B F E}, S_{\triangle A F B}\right\}<\frac{1}{8}
$$

矛盾。

(3) $F$ 不在 $\triangle A E B$ 中, 则 $F$ 在四边形 $E D C B$ 中, 则

$$
S_{B C D E}=S_{\triangle D E F}+S_{\triangle D C F}+S_{\triangle F B C}+S_{\triangle D E B}>\frac{1}{2} .
$$

用 $X E, Y C, D Y, B Z$ 表示四边形 $B C D E$, 代入可知,

$$
(X E-Y C) \cdot(D Y-B Z)>0
$$

不妨设 $X E>Y C, B Z>D Y$. 注意到, 此时 $S_{A E D C}<S_{\triangle A X C}=\frac{1}{2}$, 故 $F$ 点不在四边形 $A E D C$ 中, 从而 $F$ 在 $\triangle A B C$ 中.



延长 $B C$ 与直线 $X Y$ 交于点 $Q$, 过 $E$ 做 $B C$ 平行线, 与直线 $X Y, A Z$ 交于点 $P, O$, 此时, 平行四边形 $P Q B O$ 的面积小于 1 , 且 $F$ 在 $\triangle A B C$ 中, 由前面讨
论可知矛盾.

综上, 引理 4 得证.

下面回到原问题.

证明 记由 6 个点中的任意 3 个点构成的三角形中面积最小值为 $S$, 按 6 个点的构成的凸包分类.

(1) 凸包为三角形, 凸包可以被三角剖分成 7 个三角形, 由引理 1 可知,

$$
S \leq \frac{1}{7} \times \frac{1}{2}<\frac{1}{8}
$$

(2) 凸包为四边形, 结合引理 1 、引理 2 可知,

$$
S \leq \frac{1}{4} \times \frac{1}{2}=\frac{1}{8}
$$

断论 面积为 1 的平行四边形中的 6 个点构成的凸包边数不小于 5 时, 则一定可以找到一个面积不超过 1 的平行四边形, 包含这六个给定点, 且相对的两条边至少有一条边上包含两个给定点 (平行四边形的顶点也算在边上).

证明 事实上, 我们首先可以通过平移, 使得每条边上至少有一个点, 若一组对边上均恰有一个给定点. 设 $B, E$ 分别在边 $W X, Y Z$ 上, 如图所示, 可以不妨设 $X B \geq Y E$, 同时为方便计算, $X Y Z W$ 可以设为单位正方形.


此时, 所有点均在直线 $X W$ 与直线 $Y Z$ 之间. 过 $B, E$ 两点直线 $l_{1}, l_{2}$ 起始位置与 $X W, Y Z$ 重合, 然后顺时针旋转 $l_{1}, l_{2}$ (旋转过程中保持平行), 直到这两条直线首次有除 $B E$ 之外的给定点落在 $l_{1}$ 或者 $l_{2}$ 上, 结束旋转.

设直线 $l_{1}, l_{2}$ 与直线 $X Y$ 交于点 $S, V$, 与直线 $W Z$ 交于点 $R, U$. 此时

$$
U Z=E Z \cdot \tan \angle U E Z \geq B W \cdot \tan \angle R B W=R W
$$

从而, $R U \leq W Z, S_{R Z V S} \leq S_{X Y Z W}=1$. 显然平行四边形 $S R U V$ 包含给定的六个点 $A, B, C, D, E, F$. 而线段 $S R$ 与线段 $U V$ 至少有一条含至少两个给定点.对另一组对边类似考虑, 可知断论成立.

(3) 凸包为五边形, 结合断论可知, 存在两条邻边, 均恰含有两个给定点. 此时, 6 个点的分布只有两种可能,



图a



图 b

(I) 对于图 a, 由引理 4 可知此时结论成立;

(II) 对于图 $\mathrm{b}$, 由引理 3 可知 $A C D E$ 这 4 个点中有 3 个点构成的三角形面积不超过 $\frac{1}{8}$.

(4) 凸包为六边形.



(I) 存在给定点在顶点处, 连结 $A Y$, 由抽革原理可知, $\triangle A X Y$ 与 $\triangle A Y Z$ 中必有一个三角形含另外 5 个点中的至少 3 个点, 这 3 个点再加上 $A$ 点, 由引理 3 可知结论成立.

(II) 不存在给定点在顶点处, 则由断论可知, 必有两条邻边含两个给定点.由引理 3 可知结论成立.

致谢 感谢冷岗松教授, 刘炜老师, 沈浩老师对于本文给予的批评与指导.

## 参考文献

[1] 田廷彦著, 单墫编. 数学奥林匹克命题人讲座一组合几何 $[M]$, 上海: 科技教育出版社. 2010,7: 134.

$[2]$ 单墫主编. 奥数教程一初一年级 $[M]$, 上海: 华东师范大学出版社. 2002,1 : 227 .

