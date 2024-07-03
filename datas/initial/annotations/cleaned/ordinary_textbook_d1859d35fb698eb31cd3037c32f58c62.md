数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2007 年美国数学奥林匹克第六题的简证 

金磊

(西安交通大学附属中学, 710048)

2007 年美国数学奥林匹克第六题为:

题目. 已知 $\triangle A B C$ 内切圆、外接圆为圆 $I$ 、圆 $O$, 设圆 $O$ 半径为 $R$. 过点 $A$ 作圆 $P_{A} 、 Q_{A}$ 均与圆 $O$ 内切于 $A$ 点, 且圆 $P_{A}$ 与圆 $I$ 外切, 圆 $Q_{A}$ 与圆 $I$ 内切. 类似定义 $P_{B}, Q_{B} 、 P_{C}, Q_{C}$. 求证: $8 P_{A} Q_{A} \cdot P_{B} Q_{B} \cdot P_{C} Q_{C} \leq R^{3}$, 等号成立当且仅当 $\triangle A B C$ 为正三角形 ${ }^{[1]}$.



本题是一个以非常困难而著称的题目. 官方提供的证明 [1] 要利用反演变换, 而且计算非常复杂, 其他书籍 $[2],[3],[4]$ 也给出了各种其他的证明, 但是都比较繁琐. 下面给出两种新的简洁的证明, 第一种是纯几何方法, 利用曼海姆定理和位似得到. 第二种是自然而简洁的三角计算方法. 当然最后都用到了简单的均值不等式和琴生不等式.

证法一 设圆 $I 、 Q_{A}$ 半径为 $r 、 x, \triangle A B C$ 边角依次为 $a, b, c, A, B, C$; 面积为 $S$.

由对称性不妨设 $C>B, R=1$. 设圆 $Q_{A} 、 P_{A}$ 分别交 $A B 、 A C$ 于 $B^{\prime}, C^{\prime}$及 $B^{\prime \prime}, C^{\prime \prime}$.

收稿日期: 2018-03-17； 修订日期: 2018-03-31.
圆 $I$ 与 $A B 、 A C$ 切于 $J 、 K, J K$ 交 $A I$ 于 $I^{\prime}, A D \perp B C$ 于 $D$. 则由曼海姆定理知 $I^{\prime}$ 为 $\triangle A B^{\prime} C^{\prime}$ 内心、 $\triangle A B^{\prime \prime} C^{\prime \prime}$ 的 $A$-旁心, 设此圆半径为 $r^{\prime}$.

显然 $\triangle A B^{\prime} C^{\prime}$ 及 $\triangle A B^{\prime \prime} C^{\prime \prime}$ 均与 $\triangle A B C$ 位似. 从而得到

$$
\begin{aligned}
x & =\frac{x}{R}=\frac{A I^{\prime}}{A I}=\cos ^{2} \frac{A}{2}, \\
\frac{P_{A} Q_{A}}{x} & =\frac{P_{A} Q_{A}}{A Q_{A}}=1-\frac{A P_{A}}{A Q_{A}}=1-\frac{A D^{\prime \prime}}{A D^{\prime}}=\frac{2 r^{\prime}}{A D^{\prime}} \\
& =\frac{2 r}{A D}=\frac{4 S}{a+b+c} \frac{a}{2 S}=\frac{2 a}{a+b+c} .
\end{aligned}
$$

则

$$
P_{A} Q_{A}=\frac{2 a x}{a+b+c}=\frac{2 a}{a+b+c} \cos ^{2} \frac{A}{2} .
$$

同理可以得到 $P_{B} Q_{B}, P_{C} Q_{C}$. 故

$$
\begin{aligned}
8 P_{A} Q_{A} \cdot P_{B} Q_{B} \cdot P_{C} Q_{C} & =8 \frac{8 a b c}{(a+b+c)^{3}}\left(\cos \frac{A}{2} \cos \frac{B}{2} \cos \frac{C}{2}\right)^{2} \\
& \leq \frac{64 a b c}{27 a b c}\left(\frac{\cos \frac{A}{2}+\cos \frac{B}{2}+\cos \frac{C}{2}}{3}\right)^{6} \\
& \leq \frac{64}{27}\left(\cos \frac{A+B+C}{6}\right)^{6}=1=R^{3} .
\end{aligned}
$$

即 $8 P_{A} Q_{A} \cdot P_{B} Q_{B} \cdot P_{C} Q_{C} \leq R^{3}$, 当且仅当 $\triangle A B C$ 为正三角形时取等号.

注 曼海姆 (Manheim) 定理一般叙述为: 如上图, 若圆 $I$ 与 $\triangle A B^{\prime} C^{\prime}$ 外接圆相内切, 且与 $A B 、 A C$ 切于 $J 、 K, J K$ 交 $A I$ 于 $I^{\prime}$, 则 $I^{\prime}$ 为 $\triangle A B^{\prime} C^{\prime}$ 内心;对旁心也有类似结论, 即圆 $I$ 与 $\triangle A B^{\prime \prime} C^{\prime \prime}$ 外接圆相外切, 且与 $A B 、 A C$ 切于 $J 、 K, J K$ 交 $A I$ 于 $I^{\prime}$, 则 $I^{\prime}$ 为 $\triangle A B^{\prime \prime} C^{\prime \prime}$ 的 $A$ 旁心. 且反之亦然.

曼海姆定理另一种等价叙述为: 定点 $A$ 在定圆 $O$ 外, $B 、 C$ 分别在圆 $O$ 切线 $A J 、 A K$ 上, 且 $B C$ 与圆 $O$ 切于 $D$, 则 $\triangle A B C$ 的外接圆与某定圆相切, 即点 $D$ 运动时, $\triangle A B C$ 的外接圆的包络为圆, 显然此时外心轨迹为双曲线.


证法二 设圆 $I 、 Q_{A} 、 P_{A}$ 半径为 $r 、 x 、 y, \triangle A B C$ 边角依次为 $a, b, c$, $A, B, C$; 面积为 $S$, 由对称性不妨设 $C>B, R=1$, 则

$$
\begin{aligned}
r & =\frac{2 S}{a+b+c}=\frac{b c \sin A}{2(\sin A+\sin B+\sin C)} \\
& =\frac{2 \sin A \sin B \sin C}{2 \sin \frac{A+B}{2} \cos \frac{A-B}{2}+2 \sin \frac{C}{2} \cos \frac{C}{2}} \\
& =\frac{\sin A \sin B \sin C}{2 \cos \frac{C}{2} \cos \frac{A}{2} \cos \frac{B}{2}} \\
& =4 \sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2} .
\end{aligned}
$$

显然 $P_{A} 、 Q_{A}$ 在 $O A$ 上, 则

$$
\begin{aligned}
\angle O A I & =\angle O A C-\angle C A I=90^{\circ}-\angle B-\frac{1}{2} \angle A \\
& =\frac{1}{2}(\angle C-\angle B) ; \\
A I & =\frac{r}{\sin \frac{A}{2}} .
\end{aligned}
$$

由圆 $Q_{A}$ 与圆 $O 、 I$ 内切及在 $\triangle A I Q_{A}$ 中, 由余弦定理得:

$$
\begin{aligned}
& x^{2}+\frac{r^{2}}{\sin ^{2} \frac{A}{2}}-2 x \frac{r}{\sin \frac{A}{2}} \cos \frac{C-B}{2}=(x-r)^{2}=x^{2}-2 x r+r^{2}, \\
& 2 x \frac{\cos \frac{C-B}{2}-\sin \frac{A}{2}}{\sin \frac{A}{2}}=r \cot ^{2} \frac{A}{2}, \\
& x=r \frac{\cos ^{2} \frac{A}{2}}{4 \sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}}=\cos ^{2} \frac{A}{2} .
\end{aligned}
$$

同理有

$$
\begin{gathered}
y^{2}+\frac{r^{2}}{\sin ^{2} \frac{A}{2}}-2 y \frac{r}{\sin \frac{A}{2}} \cos \frac{C-B}{2}=(y+r)^{2}=y^{2}+2 y r+r^{2}, \\
y=r \frac{\cos ^{2} \frac{A}{2}}{4 \sin \frac{A}{2} \cos \frac{B}{2} \cos \frac{C}{2}}=\cos ^{2} \frac{A}{2} \tan \frac{B}{2} \tan \frac{C}{2} .
\end{gathered}
$$

从而

$$
P_{A} Q_{A}=\cos ^{2} \frac{A}{2}-\cos ^{2} \frac{A}{2} \tan \frac{B}{2} \tan \frac{C}{2}=\frac{\sin \frac{A}{2} \cos ^{2} \frac{A}{2}}{\cos \frac{B}{2} \cos \frac{C}{2}}
$$

同理

$$
P_{B} Q_{B}=\frac{\sin \frac{B}{2} \cos ^{2} \frac{B}{2}}{\cos \frac{A}{2} \cos \frac{C}{2}}, \quad P_{C} Q_{C}=\frac{\sin \frac{C}{2} \cos ^{2} \frac{C}{2}}{\cos \frac{A}{2} \cos \frac{B}{2}} .
$$

从而

$$
\begin{aligned}
& 8 P_{A} Q_{A} \cdot P_{B} Q_{B} \cdot P_{C} Q_{C} \\
= & 8 \frac{\sin \frac{A}{2} \cos ^{2} \frac{A}{2} \sin \frac{B}{2} \cos ^{2} \frac{B}{2} \sin \frac{C}{2} \cos ^{2} \frac{C}{2}}{\cos \frac{B}{2} \cos \frac{C}{2} \cos \frac{A}{2} \cos \frac{C}{2} \cos \frac{A}{2} \cos \frac{B}{2}}
\end{aligned}
$$

$$
\begin{aligned}
& =8 \sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2} \leq 8\left(\frac{\sin \frac{A}{2}+\sin \frac{B}{2}+\sin \frac{C}{2}}{3}\right)^{3} \\
& \leq 8 \sin ^{3} \frac{A+B+C}{6}=1=R^{3} .
\end{aligned}
$$

即 $8 P_{A} Q_{A} \cdot P_{B} Q_{B} \cdot P_{C} Q_{C} \leq R^{3}$, 当且仅当 $\triangle A B C$ 为正三角形时取等号.

注 证法二中得到的恒等式 $P_{A} Q_{A} \cdot P_{B} Q_{B} \cdot P_{C} Q_{C}=\sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}$ 还是很漂亮的.

## 参考文献

[1] 2007年 IMO 中国国家集训队教练组. 走向 IMO: 数学奥林匹克试题集锦. $2007[\mathrm{M}]$. 华东师大出版社, 2007.

[2] 田廷彦. 数学奥林匹克命题人讲座, 圆 $[\mathrm{M}]$. 上海科技教育出版社, 2010 .

$[3]$ 单墫. 数学竞赛研究教程 $[\mathrm{M}]$. 江苏教育出版社, 2009 .

[4] 沈文选, 杨清桃. 高中数学竞赛解题策略. 几何分册 $[\mathrm{M}]$. 浙江大学出版社, 2012 .

