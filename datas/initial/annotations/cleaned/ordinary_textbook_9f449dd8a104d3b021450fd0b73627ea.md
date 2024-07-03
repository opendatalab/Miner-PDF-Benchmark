# 第十五期问题征解解答与点评 

牟晓生

第一题. 设 $z_{1}, z_{2}, z_{3}$ 是单位复数. 证明存在单位复数 $z$ 使得

$$
\frac{1}{\left|z-z_{1}\right|^{2}}+\frac{1}{\left|z-z_{2}\right|^{2}}+\frac{1}{\left|z-z_{3}\right|^{2}} \leq \frac{9}{4}
$$

(湖北武钢三中学生 王逸轩, 上海大学 冷岗松 供题)

## 证明 (根据人大附中陈炤华同学的解答整理):

设单位圆上 $z_{1}, z_{2}, z_{3}$ 对应的点分别为 $A, B, C$. 不妨设它们是逆时针排列的, 且 $B C$ 是最长边. 取 $D$ 为弧 $B C$ (不含 $A$ 那段) 的中点, 我们证明点 $D$ 对应的复数 $z$ 满足条件. 令 $\triangle A B C$ 的三个内角分别是 $\alpha, \beta, \gamma$, 分两种情况讨论:

1) $\alpha>\frac{\pi}{2}$. 此时 $|D A|,|D B|,|D C|$ 均大于 $\sqrt{2}$, 于是

$$
\sum_{i=1}^{3} \frac{1}{\left|z-z_{i}\right|^{2}}=\frac{1}{|D A|^{2}}+\frac{1}{|D B|^{2}}+\frac{1}{|D C|^{2}}<\frac{3}{2}<\frac{9}{4}
$$

2) $\alpha \leq \frac{\pi}{2}$. 此时有

$$
\sum_{i=1}^{3} \frac{1}{\left|z-z_{i}\right|^{2}}=\frac{1}{4 \sin ^{2} \frac{\alpha}{2}}+\frac{1}{4 \sin ^{2} \frac{\alpha}{2}}+\frac{1}{4 \sin ^{2}\left(\beta+\frac{\alpha}{2}\right)}
$$

为证等式右边 $\leq \frac{9}{4}$, 等价于要证

$$
\sin ^{2}\left(\beta+\frac{\alpha}{2}\right) \geq \frac{\sin ^{2} \frac{\alpha}{2}}{9 \sin ^{2} \frac{\alpha}{2}-2}
$$

也就是

$$
1-\cos (2 \beta+\alpha) \geq \frac{2-2 \cos \alpha}{5-9 \cos \alpha} \text {. }
$$

由假设 $\alpha \geq \beta, \gamma$, 因此 $\pi-2 \alpha \leq \beta \leq \alpha$. 于是 $\frac{\pi}{2} \leq 2 \pi-3 \alpha \leq 2 \beta+\alpha \leq 3 \alpha \leq \frac{3 \pi}{2}$.由此可知 $\cos (2 \beta+\alpha) \leq \cos (3 \alpha)$. 将它代入到要证的 (1) 式, 化归为

$$
1-\cos (3 \alpha)=3 \cos \alpha+1-4 \cos ^{3} \alpha \geq \frac{2-2 \cos \alpha}{5-9 \cos \alpha} .
$$

整理后即 $(1-\cos \alpha)(1-2 \cos \alpha)\left(3+17 \cos \alpha+18 \cos ^{2} \alpha\right) \geq 0$. 这对 $\cos \alpha \in\left[0, \frac{1}{2}\right]$显然成立, 命题得证!
评注 (1). 浙江省富阳中学黄昊中同学, 西工大附中吴庆肜同学, 巴蜀中学叶安宁, 崔郝好同学, 长沙市一中方浩同学, 雅礼中学陈钦品, 邱添, 谢添乐, 黄磊等同学也给出了本题的正确解答.

(2). 更一般地可以考虑对 $n$ 个单位复数的相应问题. Ambrus, Ball 以及 Erdelyi 在 2013 年发表的论文 “Chebyshev constants for the unit circle” 证明了最佳常数是 $\frac{n^{2}}{4}$.

第二题. 如图, $D$ 是正三角形 $A B C$ 的边 $B C$ 上一点, $B D>C D$. 记 $O_{1}, I_{1}$为 $\triangle A B D$ 的外心与内心, $O_{2}, I_{2}$ 为 $\triangle A C D$ 的外心与内心. 圆 $I_{1}$ 与圆 $I_{2}$ 除 $B C$外的另一条外公切线交 $A B, A C$ 于 $P, Q$. 设直线 $P I_{1}$ 与 $Q I_{2}$ 交于 $R$, 而直线 $O_{1} I_{1}$ 与 $O_{2} I_{2}$ 交于 $T$. 证明: $A T^{2}=A R^{2}+A D \cdot B C$.

(广西钦州 卢圣 供题)


## 证明 (根据长沙市一中胡冬础同学的解答整理):

如图标点. 首先注意到 $R$ 是 $\triangle A P Q$ 的对应顶点 $A$ 的旁心. 因此 $\angle R A B=$ $30^{\circ}$, 并且有

$$
\begin{aligned}
A R^{2} & =\frac{4}{3}\left(\frac{1}{2}(A P+P Q+Q A)\right)^{2}=\frac{1}{3}(A E+M L+A H)^{2} \\
& =\frac{1}{3}(A E+F G+A H)^{2}=\frac{1}{3}(3 A B-2 B E-2 C H)^{2} \\
& =\frac{1}{3}(3 A B-(A B+B D-A D)-(A C+C D-A D))^{2} \\
& =\frac{4}{3} A D^{2} .
\end{aligned}
$$

接下来我们有

$$
A O_{1}=D O_{1}=A O_{2}=D O_{2}=\frac{\sqrt{3}}{3} A D
$$

而 $\angle O_{1} A O_{2}=60^{\circ}$, 因此 $A O_{1} D O_{2}$ 是两个正三角形拼成的菱形. 另外由 $\angle A O_{1} D=\angle A I_{1} D=120^{\circ}$ 知 $A O_{1} I_{1} D$ 四点公圆, $A O_{2} I_{2} D$ 同理. 利用这些我们有如下计算:

$$
\begin{aligned}
\angle O_{1} T O_{2} & =180^{\circ}-\angle I_{1} O_{1} O_{2}-\angle I_{2} O_{2} O_{1} \\
& =60^{\circ}-\angle I_{1} O_{1} D-\angle I_{2} O_{2} D \\
& =60^{\circ}-\angle I_{1} A D-\angle I_{2} A D=30^{\circ} .
\end{aligned}
$$

而 $D O_{1}=D O_{2}$ 且 $\angle O_{1} D O_{2}=60^{\circ}$, 故 $D$ 是 $\triangle O_{1} T O_{2}$ 的外心.

令 $S$ 为 $O_{1} I_{1}$ 与 $B C$ 的交点, 那么

$$
\begin{aligned}
\angle D S O_{1} & =360^{\circ}-\angle A D B-\angle D A O_{1}-\angle A O_{1} I_{1} \\
& =360^{\circ}-\left(120^{\circ}-2 \angle I_{1} A D\right)-30^{\circ}-\left(120^{\circ}+I_{1} O_{1} D\right) \\
& =90^{\circ}+2 \angle I_{1} A D-\angle I_{1} O_{1} D \\
& =90^{\circ}+\angle I_{1} O_{1} D .
\end{aligned}
$$

于是 $\angle T S D=90^{\circ}-\angle I_{1} O_{1} D=90^{\circ}-\angle I_{1} T D$, 即 $D T \perp B C$. 由余弦定理知

$$
\begin{aligned}
A T^{2} & =\frac{4}{3} A D^{2}+D T^{2}+2 \sin \angle A D B \cdot A D \cdot D T \\
& =A D^{2}+D O_{1}^{2}+2 \frac{\frac{\sqrt{3}}{2} B C}{A D} \cdot A D \cdot D O_{1} \\
& =A D^{2}+\frac{1}{3} A D^{2}+\sqrt{3} B C \cdot \frac{A D}{\sqrt{3}} \\
& =\frac{4}{3} A D^{2}+B C \cdot A D .
\end{aligned}
$$

比较 (2), (3)两式, 命题得证!

评注 象山第三中学黄子宸同学, 如东高级张陈成同学, 人大附中陈炤华同学, 巴蜀中学叶安宁, 崔郝好同学, 雅礼中学陈钦品, 刘麟轩, 李师铨同学, 长沙市一中胡宇涵, 李疆来等同学也给出了本题的正确解答.

第三题. 给定正整数 $m, n$, 考虑在 $m \times n$ 白棋盘上先将一些格染成黑色. 在之后的每一时刻, 若存在一个白格至少与两个黑格相邻, 则可将它也染成黑色.求最初至少要染多少个黑色格才能在某一时刻染黑整个棋盘?

(哈佛大学牟晓生 供题)

## 证明 (根据雅礼中学刘舰徽同学的解答整理):

答案是 $\left\lceil\frac{m+n}{2}\right\rceil$.

一方面, 我们注意到黑色区域的周长在题设的操作下单调不增. 这里一条线段被算作周长当且仅当它恰是一个 (而不是两个) 黑格的某条边. 周长单调不增是因为当一个格被染黑时, 它的四条边里至少有两条从周长的一部分消失了.由于要染黑全部棋盘, 最终黑色区域的周长是 $2(m+n)$, 因此最初的周长至少也是 $2(m+n)$. 而每个黑格至多贡献 4 条边, 因此前面说的答案是一个下界.

接下来我们进行构造. 不妨假设 $m \leq n$. 将 $m \times n$ 棋盘划分为左边 $m \times m$以及右边 $m \times(n-m)$ 两部分. 在左边的正方形部分, 我们将对角线上的 $m$ 个格子染黑, 这样可以保证左边部分沿着一条一条对角线最终全部成为黑色. 在右边部分, 如果 $n-m$ 是偶数 (奇数), 则将这部分第一行所有偶数 (奇数) 列格子染黑, 恰好是 $\left\lceil\frac{n-m}{2}\right\rceil=\left\lceil\frac{m+n}{2}\right\rceil-m$ 个. 在左边部分全部染黑以后, 右边第一行也按条件全部染黑, 之后一行一行直到棋盘全部变黑. 于是构造成立!

评注 (1). 人大附中陈炤桦, 张峰玮同学, 西工大附中吴庆胿同学, 巴蜀中学叶安宁, 崔郝好同学, 长沙市一中胡宇涵同学, 雅礼中学刘哲成, 肖尧, 邱添等同学也给出了本题的正确解答.

(2). 这个问题被收录在 Bollobas 的书《The Art of Mathematics: Coffee Time in Memphis》中. 那本书里有几百个精彩的问题与证明, 非常值得一读.

第四题. $A B C$ 是一个三角形, 而 $P, Q, R$ 分别是 $B C, C A, A B$ 上的点. 证明 $\triangle P Q R$ 的周长不小于 $\triangle A Q R, \triangle B R P, \triangle C P Q$ 周长的最小值.

(哈佛大学牟晓生 供题)

## 证明 (根据供题者的解答整理):

我们用反证法. 假设命题不成立, 则有:

$$
\begin{aligned}
& P Q+P R<A Q+A R \\
& Q P+Q R<B P+B R \\
& R P+Q R<C P+C Q .
\end{aligned}
$$

自然地, 我们希望将三条内部的边 $P Q, Q R, R P$ 用外面的 $A Q, A R, B P, B R$ 以及 $C P, C Q$ 表示出来. 最直接的方法是用余弦定理, 比如

$$
P Q=\sqrt{A Q^{2}+A R^{2}-2 A Q \cdot A R \cdot \cos A} .
$$

然而这样的话上面式子的左边会有两个根号, 计算非常不易. 为了简化问题, 我们试图将 $P Q$ 进行放缩, 而一种方法就是将 $P Q$ 放为它在直线 $A B$ 上的投影.由此我们得到

$$
\begin{aligned}
& P Q \geq A B-A Q \cdot \cos A-B P \cdot \cos B ; \\
& P R \geq A C-A R \cdot \cos A-C P \cdot \cos C ; \\
& Q R \geq B C-B R \cdot \cos B-C Q \cdot \cos C .
\end{aligned}
$$

在我们进行接下来的计算之前, 注意到原命题在 $P, Q, R$ 为三条边中点时取等号. 而此时 $P Q$ 平行于 $A B$, 因此上面的放缩并没有放过头. 这一点给我们继续下去提供了信心.

令 $B C=a, C A=b, A B=c$, 另外设 $B P=\frac{a}{2}+\alpha, C Q=\frac{b}{2}+\beta, A R=\frac{c}{2}+\gamma$,其中 $\alpha, \beta, \gamma$ 不一定是正的. 将 (7) 代入到 (4) 式中, 我们得到

$b+c-\left(\frac{b}{2}-\beta+\frac{c}{2}+\gamma\right) \cdot \cos A-\left(\frac{a}{2}+\alpha\right) \cos B-\left(\frac{a}{2}-\alpha\right) \cos C<\frac{b}{2}-\beta+\frac{c}{2}+\gamma$.

经过整理也就是

$$
\frac{(b+c)(1-\cos A)-a(\cos B+\cos C)}{2}<\alpha(\cos B-\cos C)-(\beta-\gamma)(1+\cos A)
$$

由于 $b \cos A+a \cos B=c, c \cos A+a \cos C=b$, 上面左边是零(也对应了 $\alpha=\beta=\gamma=0$ 时等号成立). 于是我们简化为:

$$
\alpha(\cos B-\cos C)>(\beta-\gamma)(1+\cos A) .
$$

利用和差化积公式约去 $\cos \frac{A}{2}=\sin \frac{B+C}{2}$, 我们进一步得到

$$
\alpha \sin \frac{C-B}{2}>(\beta-\gamma) \cos \frac{A}{2}
$$

类似地, 我们由 (5), (6) 结合 (7) 可以得到

$$
\begin{aligned}
& \beta \sin \frac{A-C}{2}>(\gamma-\alpha) \cos \frac{B}{2} . \\
& \gamma \sin \frac{B-A}{2}>(\alpha-\beta) \cos \frac{C}{2} .
\end{aligned}
$$

我们将要从 (8)-(10) 导出矛盾. 为此我们将 (8) 式乘上 $\sin \frac{A}{2},(9)$ 式乘上 $\sin \frac{B}{2}$, (10) 式乘上 $\sin \frac{C}{2}$, 然后相加.

我们来证明最后得出的不等式左右相等. 为此考虑 $\alpha$ 的系数. 在左边它只出现在 (8) 式中, 因此系数是

$$
\sin \frac{C-B}{2} \sin \frac{A}{2}=\sin \frac{C-B}{2} \cos \frac{B+C}{2}=\frac{\sin C-\sin B}{2} .
$$

而在右边 $\alpha$ 的系数来自 $(9),(10)$ 二式, 一共也是

$$
-\cos \frac{B}{2} \sin \frac{B}{2}+\cos \frac{C}{2} \sin \frac{C}{2}=\frac{\sin C-\sin B}{2}
$$

由此我们导出了矛盾, 命题得证!

评注 我记得是在熊斌老师的《奥数教程》上看到这个问题的. 关于面积的结论也成立, 被称作 Erdös-Debrunner 不等式.

