# 一个椭圆型几何问题的解答 

羊明亮

(浙江省乐清市知临中学, 325600)

今年的北京大学 “中学生数学奖” 夏令营初赛的最后一题是一个具有一定难度的平面几何问题, 题目如下:

在 $\triangle A B C$ 中, $A B \neq A C$. 点 $A$ 所对应的旁切圆 $\odot J$ 分别与直线 $B C, C A, A B$ 相切于点 $D, E, F$. 点 $M$ 是线段 $B C$ 的中点, 点 $S$ 在线段 $S M$ 上,且满足 $A S+D S=A E$. 证明:



我们注意到 $A E=\frac{1}{2}(A B+B C+C A)=A B+D B=A C+D C$. 故

$$
A S+D S=A B+D B=A C+D C .
$$

在标准解答中, 由式 (1) 即推出折 (或凹) 四边形 $A B D S, A C D S$ 均为圆外切四边形. 考虑它们的旁切圆, 并在此基础上展开证明.

事实上, 由式 (1), 我们可能会更自然地想到点 $S$ 在以 $A, D$ 为焦点, $\triangle A B C$半周长为长轴长的椭圆上. 下面我们给出一种借助于椭圆的解答. 为此, 我们将

收稿日期: 2018-08-08.
用到如下有关粗圆的几何性质.

性质 $\mathbf{I}$ 在椭圆 $\Gamma$ 中, 设 $F_{1}, F_{2}$ 为其两焦点, 点 $O$ 为 $\Gamma$ 的中心, 直线 $l$ 是点 $F_{2}$ 对应 $\Gamma$ 的准线, 线段 $A B$ 是 $\Gamma$ 一条过 $F_{2}$ 的弦, 点 $J$ 为 $\triangle A F_{1} B$ 的 $F_{1}$-旁心.点 $M$ 是线段 $A B$ 的中点, 则 $J A, J B$ 是 $\Gamma$ 的切线且 $O, M, J$ 共线.



证明 由点 $J$ 为 $\triangle F_{1} A B$ 的 $F_{1} A B$ 的 $F_{1}$-旁心知 $J A$ 是 $\angle F_{1} A F_{2}$ 的外角平分线, 故由椭圆的光学性质可知 $J A$ 为 $\Gamma$ 的切线; 同理可证 $J B$ 也是 $\Gamma$ 的切线.

由椭圆第一定义知: $A F_{1}+A F_{2}=B F_{1}+B F_{2}$, 故

$$
A F_{2}=\frac{1}{2} \cdot\left(B F_{1}+B A-A F_{1}\right)
$$

从而点 $F_{2}$ 是旁切圆圆 $J$ 于边 $A B$ 的切点, 故 $J F_{2} \perp A B$.

设 $\odot(I)$ 是 $\triangle A F_{1} B$ 的内切圆且切边 $A B$ 于点 $D$, 则点 $M$ 是线段 $D F_{2}$ 的中点.

设点 $F_{2}$ 关于点 $J$ 的对称点为 $F_{2}^{\prime}$, 则 $F_{2}^{\prime}$ 在旁切圆圆 $J$ 上, 且 $\odot(J)$ 在点 $F_{2}^{\prime}$处的切线与 $\odot(I)$ 在点 $D$ 处的切线 $(\mathrm{AB})$ 平行, 而 $\odot(I), \odot(J)$ 关于点 $F_{1}$ 位似. 故 $D, F_{2}^{\prime}$ 是上述位似变换下的对应点. 从而 $F_{1}, D, F_{2}^{\prime}$ 共线.

又点 $O, M, J$ 分别是线段 $F_{2} F_{1}, F_{2} D, F_{2} F_{2}^{\prime}$ 的中点, 故 $O, M, J$ 共线.


性质 II 设点 $P$ 为椭圆 $\Gamma$ 所在平面上的一点, 且点 $P$ 在 $\Gamma$ 外. 过 $P$ 作 $\Gamma$ 的两条切线, 切点连线记为 $l$. 过点 $P$ 作割线分别交 $\Gamma$ 于点 $A, B$, 交 $l$ 于点 $C$. 则 $A, B ; C, P$ 是调和点列.



证明 以 $P$ 为原点, 割线 $P B A$ 为 $x$ 轴建立平面直角坐标系. 用 $x_{X}, y_{X}$ 分别表示平面上点 $X$ 的横纵坐标.

设椭圆的方程为:

$$
A x^{2}+B y^{2}+C x y+D x+E y+F=0, A, B \neq 0 .
$$

则 $l$ 的方程为:

$$
D x+E y+2 F=0 .
$$

由于 $l$ 与 $x$ 轴有交点 $C$, 故 $D \neq 0$, 且 $C$ 的坐标为 $\left(-\frac{2 F}{D}, 0\right)$.

由 $y_{A}=y_{B}=0$, 点 $A, B$ 在 $\Gamma$ 上知: $x_{A}, x_{B}$ 是方程 $A x^{2}+D x+F=0$ 的两根. 由 Viete 定理:

$$
x_{A}+x_{B}=-\frac{D}{A}, \quad x_{A} \cdot x_{B}=\frac{F}{A}
$$

于是,

$$
\begin{aligned}
\left(x_{A}-x_{C}\right) \cdot x_{B}+\left(x_{B}-x_{C}\right) \cdot x_{A} & =2 x_{A} \cdot x_{B}-\left(x_{A}+x_{B}\right) \cdot x_{C} \\
& =\frac{2 F}{A}-\left(-\frac{D}{A}\right)\left(-\frac{2 F}{D}\right) \\
& =0 .
\end{aligned}
$$

这说明

$$
\frac{\overline{C A}}{\overline{C B}}=-\frac{\overline{P A}}{\overline{P B}}
$$

故 $A, B ; C, P$ 是调和点列.

注 性质 II 也可以用仿射变换处理. 由于仿射变换保交比, 调和点列在仿射变换之后仍是调和点列,将椭圆 $\Gamma$ 作仿射变换变成圆,故只需考虑 $\Gamma$ 为圆的情形.



设点 $S, T$ 是直线 $l$ 与 $\Gamma$ 的两个交点, 则有

$$
\triangle P S B \sim \triangle P A S ; \triangle P T B \sim \triangle P A T \text {. }
$$

于是,

$$
\frac{\overline{C A}}{\overline{C B}}=-\frac{\left|S_{\triangle S A T}\right|}{\left|S_{\triangle S B T}\right|}=-\frac{|A S| \cdot|A T|}{|B S| \cdot|B T|}=-\frac{|A P|}{|P S|} \cdot \frac{|P T|}{|P B|}=-\frac{\overline{P A}}{\overline{P B}}
$$

这里, $S_{\triangle S A T}, S_{\triangle S B T}$, 分别指 $\triangle S A T, \triangle S B T$ 的面积.

故 $A, B ; C, P$ 是调和点列.

现在列举原题的一些解法, 提供解法的均是我任教班级的学生.

## 解法 1 (王琛, 郑立瑜)

设点 $O$ 是线段 $A D$ 的中点, $\Gamma$ 为以 $A, D$ 为焦点, 过 $B, C, S$ 的粗圆.

由点 $J$ 是 $\triangle A B C$ 的 $A$-旁心及性质 $\mathrm{I}$ 知 $J B, J C$ 是 $\Gamma$ 的切线, 且 $O, M, J$共线.

设直线 $O M$ 与 $\Gamma$ 的另一交点为 $T$. 由性质 II 知: $T, S ; M, J$ 是调和点列.

又点 $O$ 是线段 $S T$ 的中点, 由调和点列性质有

$$
O M \cdot O J=O S^{2}
$$

于是,

$$
\frac{M S}{S J}=\frac{O S-O M}{O J-O S}=\frac{\sqrt{O M \cdot O J}-O M}{O J-\sqrt{O M \cdot O J}}=\sqrt{\frac{O M}{O J}} .
$$

设 $\triangle A B C$ 的内心为点 $I$, 内切圆 $\odot(I)$ 切边 $B C$ 于点 $K$; 点 $I$ 关于点 $M$ 的对称点为 $I^{\prime}$, 则 $I^{\prime}, J, D$ 共线.

下证: $I^{\prime} M / / O D$.

设点 $K$ 关于点 $I$ 的对称点为 $K^{\prime}$, 同性质 I 证明得 $A, K^{\prime}, D$ 共线.

而点 $M, I$ 分别是线段 $D K, K K^{\prime}$ 的中点, 故 $M I / / D K^{\prime}$, 即 $I^{\prime} M / / O D$.

又注意到, $\angle B I^{\prime} D=\angle C I K=\angle J C D$, 故 Rt $\triangle B I^{\prime} D \sim$ Rt $\triangle J C D$.



于是,

$$
\frac{B D}{D I^{\prime}}=\frac{J D}{D C} \Rightarrow D I^{\prime}=\frac{B D \cdot D C}{J D}
$$

从而

$$
\begin{aligned}
\frac{M S}{S T}=\sqrt{\frac{O M}{O J}} & =\sqrt{\frac{D I^{\prime}}{D J}}\left(I^{\prime} M \| O D\right) \\
& =\frac{\sqrt{B D \cdot C D}}{J D} .
\end{aligned}
$$

注 证出 $\frac{M S}{S J}=\sqrt{\frac{O M}{O J}}$ 后, 也可以借助简单的三角计算更快得证明出结论,这是因为

$$
\frac{O M}{O J}=\frac{h_{a}}{h_{a}+2 r_{a}}=\frac{\frac{2 S}{a}}{\frac{2 S}{a}+\frac{4 S}{b+c-a}}=\frac{b+c-a}{a+b+c}=\frac{B D \cdot C D}{J D^{2}}
$$

这里 $h_{a}, r_{a}$ 分别为 $\triangle A B C$ 中过 $A$ 的高的线段长与点 $A$ 所对应的旁切圆的半径.

若对椭圆的一些基本性质较为熟悉, 上述证明是自然的.

但借助椭圆的手法在较初级的平面几何证明中并不常见. 抛开粗圆性质不谈, 我们在作出标准的图形后, 容易猜测 $A S, D S$ 关于 $B C$ 的夹角是互补的.

延长 $A S$ 交线段 $J D$ 于一点 $W$, 则有 $S D=S W$. 于是,

$$
A W=A S+S W=A S+S D=A E
$$

我们考虑同一法.

## 解法 2 (郑立瑜)

记 $\triangle A B C$ 三边为 $a, b, c$, 且不妨设 $b<c$.

以 $A$ 为圆心, $A E\left(=\frac{a+b+c}{2}\right)$ 为半径作图交线段 $J D$ 于一点 $W$.

设 $A W$ 与 $J M, B C$ 分别交于点 $S^{\prime}, U$. 设点 $A$ 在边 $B C$ 上的投影为点 $H$.

另有

$$
\begin{gathered}
D M=\frac{1}{2} \cdot(c-b) ; M H=\frac{1}{2 a} \cdot\left(c^{2}-b^{2}\right) ; \\
J D=\frac{2 S_{\triangle A B C}}{b+c-a}=\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2(b+c-a)} ; \\
A H=\frac{2 S_{\triangle A B C}}{a}=\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2 a} .
\end{gathered}
$$

其中 $\prod$ 表示循环积.



而 $\sin \angle W A H=\frac{D H}{A W}=\frac{\frac{c-b}{2 a} \cdot(a+b+c)}{\frac{a+b+c}{2}}=\frac{c-b}{a}$, 故

$$
\begin{aligned}
U H & =A H \cdot \tan \angle W A H \\
& =\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2 a} \cdot \frac{c-b}{\sqrt{(a+b-c)(a+c-b)}} \\
& =\frac{c-b}{2 a} \cdot \sqrt{(b+c-a)(b+c+a)} ;
\end{aligned}
$$

$$
\begin{aligned}
D W & =A W \cdot \cos \angle W A H-A H \\
& =\frac{a+b+c}{2 a} \cdot \sqrt{(a+c-b)(a+b-c)}-\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2 a} .
\end{aligned}
$$

由Menelaus 定理, 有

$$
\begin{aligned}
\frac{W S^{\prime}}{S^{\prime} M}= & \frac{W J}{J D} \cdot \frac{D M}{M U} \\
= & \left(\frac{\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2(b+c-a)}-\frac{a+b+c}{2 a} \cdot \sqrt{(a+c-b) \cdot(a+b-c)}}{\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2(b+c-a)}}\right. \\
& \left.+\frac{\frac{1}{2 a} \cdot \sqrt{\prod(a+b-c) \cdot(a+b+c)}}{\frac{\sqrt{\prod(a+b-c) \cdot(a+b+c)}}{2(b+c-a)}}\right) \cdot \frac{\frac{c-b}{2}}{\frac{c^{2}-b^{2}}{2 a}-\frac{c-b}{2 a} \cdot \sqrt{(b+c-a)(b+c+a)}} \\
= & \frac{1-\frac{\sqrt{(b+c-a)(b+c+a)}}{a}+\frac{b+c-a}{a}}{\frac{c+b}{a}-\frac{\sqrt{(b+c-a)(b+c-a)}}{a}}=1 .
\end{aligned}
$$

于是 $S^{\prime} D=S^{\prime} U=S^{\prime} W$. 从而

$$
A S^{\prime}+S^{\prime} D=A S^{\prime}+S^{\prime} W=A W=A E=A S+S D .
$$

又点 $S^{\prime}$ 与 $S$ 均在线段 $J D$ 上, 故 $S^{\prime}$ 与 $S$ 重合. 则

$$
\begin{aligned}
\frac{M S}{S J} & =\frac{D M}{J D} \cdot \cot \angle J D S \\
& =\frac{\frac{c-b}{2} \cdot \frac{\sqrt{(a+b-c)(a+c-b)}}{c-b}}{J D} \\
& =\frac{\sqrt{\frac{a+b-c}{2} \cdot \frac{a+c-b}{2}}}{J D} \\
& =\frac{\sqrt{B D \cdot C D}}{J D} .
\end{aligned}
$$

注 这个解答的观赏性不如解法 1 , 但实用性更强.

此外, 我们观察待证的结论, 给我们了 $\frac{M S}{S J}$ 的比值, 由此准确的确定了点 $S$的位置, 因而有可以选择同一法及 Stewart 定理加以计算. 但实际上用 Stewart 定理表示出 $S D$ 的结果是根号下套根号的形式, 在不知道化简结果前不容易去根号. 下面介绍一种方法巧妙绕过了这一点.

## 解法 3 (吴承昫)

$a, b, c$ 同上定义, 并记 $\frac{M S}{S J}=\lambda\left(\lambda \in \mathbb{R}^{+}\right)$.

由 Stewart 定理, 有

$$
\begin{aligned}
D S^{2} & =\frac{\lambda}{\lambda+1} \cdot J D^{2}+\frac{1}{\lambda+1} \cdot D M^{2}-\frac{\lambda}{(\lambda+1)^{2}} \cdot J M^{2}, \\
A S^{2} & =\frac{\lambda}{\lambda+1} \cdot J A^{2}+\frac{1}{\lambda+1} A M^{2}-\frac{\lambda}{(\lambda+1)^{2}} \cdot J M^{2} .
\end{aligned}
$$



(2) - (1) 得

$$
\begin{aligned}
(A S-S D) \cdot A E & =A S^{2}-S D^{2} \\
& =\frac{\lambda}{\lambda+1} \cdot\left(J A^{2}-J D^{2}\right)+\frac{1}{\lambda+1} \cdot\left(A M^{2}-D M^{2}\right) \\
& =\frac{\lambda}{\lambda+1} \cdot A E^{2}+\frac{1}{\lambda+1} \cdot A E \cdot \frac{b+c-a}{2},
\end{aligned}
$$

即

$$
A S-S D=\frac{\lambda}{\lambda+1} \cdot \frac{b+c+a}{2}+\frac{1}{\lambda+1} \cdot \frac{b+c-a}{2} .
$$

又

$$
A S+S D=\frac{b+c+a}{2}
$$

故

$$
S D=\frac{a}{2(\lambda+1)}=\frac{B M}{\lambda+1}
$$

代回 (1) 整理得:

$$
B M^{2}=\lambda^{2} \cdot J D^{2}+D M^{2},
$$

从而

$$
\lambda^{2}=\frac{B M^{2}-D M^{2}}{J D^{2}}=\frac{(B M-D M)(M C+D M)}{J D^{2}}=\frac{B D \cdot D C}{J D^{2}}
$$

又 $\lambda>0$, 故 $\lambda=\frac{\sqrt{B D \cdot D C}}{J D}$.

注 上面解法中并没有对 (1), (2) 开根号相加来求解 $\lambda$. 而是通过平方作差,利用 $A S+S D$ 已知推得 $A S-S D$, 从而解得 $A S, S D$, 再求解 $\lambda$, 避免了大计算量和复杂的化简.
最后, 我们注意到性质 I, II 或其对偶的性质对一般的二次曲线均成立. 因此, 这个命题对于一般的二次曲线仍然成立. 我们看一下其在双曲线中的版本:

在 $\triangle A B C$ 中, $A B \neq A C$. 其内切圆圆 $I$ 切边 $B C, C A, A B$ 于点 $D, E, F$. 点 $M$ 是线段 $B C$ 的中点, 点 $S$ 在线段 $I M$ 上, 且满足 $A S-S D=A E$. 证明:

$$
\frac{M S}{S I}=\frac{\sqrt{B D \cdot D C}}{I D}
$$



证明是一致的, 留给读者作为练习.

致谢 感谢上海四季教育罗振华老师仔细审阅了本文并提出的宝贵修改意见.

