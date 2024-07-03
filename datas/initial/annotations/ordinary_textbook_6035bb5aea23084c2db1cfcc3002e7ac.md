# Descarts 定理与一类多圆相切问题 

## 王永喜

(山西大学附属中学, 030006)

我们先从一个非常经典的几何问题谈起:

引例. 如图 1(a), 已知圆心为 $A, B, C$ 的三个圆彼此外切, 且均与直线 $l$ 相切,设三个圆的半径分别为 $a, b, c(0<c<a<b)$. 求证:

$$
\frac{1}{\sqrt{c}}=\frac{1}{\sqrt{a}}+\frac{1}{\sqrt{b}}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-1.jpg?height=257&width=469&top_left_y=1205&top_left_x=448)

图 1(a)

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-1.jpg?height=297&width=511&top_left_y=1165&top_left_x=1092)

图 1(b)

此问题不难. 如图 1(b), 注意到

$$
A_{1} B_{1}=2 \sqrt{a b}, \quad B_{1} C_{1}=2 \sqrt{b c}, \quad A_{1} C_{1}=2 \sqrt{a c}
$$

且 $A_{1} C_{1}+B_{1} C_{1}=A_{1} B_{1}$, 故

$$
\frac{1}{\sqrt{c}}=\frac{1}{\sqrt{a}}+\frac{1}{\sqrt{b}} .
$$

事实上, 上述引例正是本文所要介绍的 Descartes 定理的特列. 我们先给出该定理的具体表述与证明, 该证明源自文献 [1].

定理 (Descartes). 若平面上四个半径为 $r_{1}, r_{2}, r_{3}, r_{4}$ 的圆两两相切于不同点, 则其半径满足以下结论:

(i) 若四圆两两外切, 则

$$
\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}+\frac{1}{r_{4}}\right)^{2}=2\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}+\frac{1}{r_{3}^{2}}+\frac{1}{r_{4}^{2}}\right) .
$$

(ii) 若半径为 $r_{1}, r_{2}, r_{3}$ 的圆内切于半径为 $r_{4}$ 的大圆中, 则

$$
\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}-\frac{1}{r_{4}}\right)^{2}=2\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}+\frac{1}{r_{3}^{2}}+\frac{1}{r_{4}^{2}}\right) .
$$

证明. 事实上, 平面上四圆满足两两相切, 要么四圆两两外切, 要么其中三个圆两两外切且同时内切于第四个圆中, 即有定理中 (i) 和 (ii) 两种情形. 下面分情况讨论.

(i) 若四圆两两外切. 如图 2, 令 $O_{1} O_{2}=r_{1}+$ $r_{2}=a, O_{1} O_{3}=r_{1}+r_{3}=b, O_{2} O_{3}=r_{2}+r_{3}=$ c, $O O_{3}=r_{3}+r_{4}=x, O O_{2}=r_{2}+r_{4}=y, O O_{1}=$ $r_{1}+r_{4}=z, \angle O_{1} O O_{2}=\alpha, \angle O_{3} O O_{1}=\beta, \angle O_{2} O O_{3}=$ $\gamma$. 则 $\alpha+\beta+\gamma=360^{\circ}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-2.jpg?height=352&width=428&top_left_y=475&top_left_x=1268)

图 2

由余弦定理, 有

$$
\cos \alpha=\frac{y^{2}+z^{2}-a^{2}}{2 y z}, \cos \beta=\frac{z^{2}+x^{2}-b^{2}}{2 z x}, \cos \gamma=\frac{x^{2}+y^{2}-c^{2}}{2 x y} .
$$

注意到

$$
\cos \gamma=\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sqrt{\left(1-\cos ^{2} a\right)\left(1-\cos ^{2} \beta\right)}
$$

将 (3) 式代入 (4) 式, 化简得,

$$
\begin{aligned}
& 2 z^{2}\left(x^{2}+y^{2}-c^{2}\right)+\left(y^{2}+z^{2}-a^{2}\right)\left(z^{2}+x^{2}-b^{2}\right) \\
& =\sqrt{\left(4 y^{2} z^{2}-\left(y^{2}+z^{2}-a^{2}\right)^{2}\right)\left(4 z^{2} x^{2}-\left(z^{2}+x^{2}-b^{2}\right)^{2}\right)}
\end{aligned}
$$

两边平方化简, 再将 $r_{1}, r_{2}, r_{3}, r_{4}$ 代入得

$$
r_{4}=\frac{r_{1} r_{2} r_{3}}{2 \sqrt{r_{1} r_{2} r_{3}\left(r_{1}+r_{2}+r_{3}\right)}+r_{1} r_{2}+r_{1} r_{3}+r_{2} r_{3}},
$$

从而

$$
\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}+\frac{1}{r_{4}}\right)^{2}=2\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}+\frac{1}{r_{3}^{2}}+\frac{1}{r_{4}^{2}}\right) .
$$

即 (1) 式成立.

(ii) 若其中三个圆内切于一个半径为 $r_{4}$ 的大圆中. 用同样的方法, 此时 $x=r_{4}-r_{3}, y=r_{4}-r_{2}, z=r_{4}-r_{1}, a, b, c$ 不变, 代入 (5) 式得:

$$
r_{4}=\frac{r_{1} r_{2} r_{3}}{2 \sqrt{r_{1} r_{2} r_{3}\left(r_{1}+r_{2}+r_{3}\right)}-\left(r_{1} r_{2}+r_{1} r_{3}+r_{2} r_{3}\right)},
$$

因此有

$$
\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}-\frac{1}{r_{4}}\right)^{2}=2\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}+\frac{1}{r_{3}^{2}}+\frac{1}{r_{4}^{2}}\right) .
$$

故 (2) 式成立.

现在我们解释引例为什么是 Descartes 定理的特列. 事实上, 由 (6) 式得

$$
\frac{1}{r_{4}}=2 \sqrt{\frac{1}{r_{2} r_{3}}+\frac{1}{r_{3} r_{1}}+\frac{1}{r_{1} r_{2}}}+\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}} .
$$

当 $r_{3} \rightarrow+\infty$ 时,有

$$
\frac{1}{r_{4}}=2 \sqrt{\frac{1}{r_{1} r_{2}}}+\frac{1}{r_{1}}+\frac{1}{r_{2}}=\left(\frac{1}{\sqrt{r_{1}}}+\frac{1}{\sqrt{r_{2}}}\right)^{2}
$$

于是

$$
\frac{1}{\sqrt{r_{4}}}=\frac{1}{\sqrt{r_{1}}}+\frac{1}{\sqrt{r_{2}}}
$$

这正是引例的结论. 同样的, 由 (7) 式得

$$
\frac{1}{r_{4}}=2 \sqrt{\frac{1}{r_{2} r_{3}}+\frac{1}{r_{3} r_{1}}+\frac{1}{r_{1} r_{2}}}-\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right) .
$$

此时令 $r_{4} \rightarrow+\infty$, 亦得引例结论.

下面给出 Descartes 定理的具体应用.

例 1 . 设在互相内切的两圆间隙中, 依次作四个内切圆. 若所作四圆除首末二者外各依次相外切, 则所作四圆的半径 $r_{1}, r_{2}, r_{3}, r_{4}$ 满足

$$
\frac{1}{r_{1}}-\frac{3}{r_{2}}+\frac{3}{r_{3}}-\frac{1}{r_{4}}=0
$$

例 1 被称作周达定理. 该定理最早出现在文献 [2] 中, 文献 [1] 和 [3] 都给出了详实的证明. 其中文献 [3] 用反演变换给出了该定理的简单证明, 并将结论推广到了 $n$ 个圆的情形. 本文我们用 Descartes 定理来证明.

证明. 如图 3, 设已知两圆圆心为 $O, O^{\prime}$, 半径分别为 $a, b$. 所作的四圆圆心分别为 $O_{1}, O_{2}, O_{3}, O_{4}$.则对圆 $O, O^{\prime}, O_{1}, O_{2}$ 利用 Descartes 定理 (2) 式, 得 $\left(-\frac{1}{a}+\frac{1}{b}+\frac{1}{r_{1}}+\frac{1}{r_{2}}\right)^{2}=2\left(\frac{1}{a^{2}}+\frac{1}{b^{2}}+\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}\right)$.同理对圆 $O, O^{\prime}, O_{2}, O_{3}$ 利用 Descartes 定理, 我们有

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-3.jpg?height=414&width=437&top_left_y=1552&top_left_x=1255)

$$
\left(-\frac{1}{a}+\frac{1}{b}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right)^{2}=2\left(\frac{1}{a^{2}}+\frac{1}{b^{2}}+\frac{1}{r_{2}^{2}}+\frac{1}{r_{3}^{2}}\right) .
$$

图 3

两式相减得

$$
\left(\frac{1}{r_{1}}-\frac{1}{r_{3}}\right)\left(-\frac{2}{a}+\frac{2}{b}+\frac{2}{r_{2}}+\frac{1}{r_{1}}+\frac{1}{r_{3}}\right)=2\left(\frac{1}{r_{1}}-\frac{1}{r_{3}}\right)\left(\frac{1}{r_{1}}+\frac{1}{r_{3}}\right),
$$

即

$$
\frac{1}{r_{1}}+\frac{1}{r_{3}}-\frac{2}{r_{2}}=-\frac{2}{a}+\frac{2}{b}
$$

同理, 有

$$
\frac{1}{r_{2}}+\frac{1}{r_{4}}-\frac{2}{r_{3}}=-\frac{2}{a}+\frac{2}{b}
$$

由以上两式联立即可.
下一例题选自 2007 年国家队培训试题 (见文献 [4]). 原解答长达 4 页篇幅,显得略为繁杂. 用上 Descartes 定理, 便会简便很多.

例 2. 设 $a, b, c \in \mathbb{R}^{+}$, 试求以下方程的正根 $x$,

$$
\sqrt{a b x(a+b+x)}+\sqrt{b c x(b+c+x)}+\sqrt{c a x(c+a+x)}=\sqrt{a b c(a+b+c)} .
$$

解. 如图 4, 以 $a+b, b+c, a+c$ 为边构成 $\triangle A B C$,以 $A, B, C$ 为心, $a, b, c$ 为半径分别作圆, 设圆 $O$ 与上述三个圆相外切, 其半径为 $x_{0}$. 由于

$$
S_{O A B}+S_{O B C}+S_{O A C}=S_{A B C},
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-4.jpg?height=337&width=371&top_left_y=642&top_left_x=1325)

则根据海伦公式有

$\sqrt{a b x_{0}\left(a+b+x_{0}\right)}+\sqrt{b c x_{0}\left(b+c+x_{0}\right)}+\sqrt{c a x_{0}\left(c+a+x_{0}\right)}=\sqrt{a b c(a+b+c)}$,

因此 $x_{0}$ 便是所求的正根. 易知已知条件正是 Descartes 定理中四圆两两外切的情形, 故由 (6) 式, 得

$$
x_{0}=\frac{a b c}{a b+b c+c a+2 \sqrt{a b c(a+b+c)}} .
$$

即得所求正根.

例 3. 如图 5, 设最大半圆半径为 1 , 绿色半圆半径为 $\frac{1}{2}$, 求第 $k$ 个灰色圆的半径.

解. 假设第 $k$ 个灰色圆的半径为 $r_{k}$, 则由 Descartes 定理有

$$
\left(2-1+\frac{1}{r_{k}}+\frac{1}{r_{k+1}}\right)^{2}=2\left(1+4+\frac{1}{r_{k}^{2}}+\frac{1}{r_{k+1}^{2}}\right) \text {. }
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-4.jpg?height=249&width=503&top_left_y=1703&top_left_x=1256)

同理有

$$
\left(2-1+\frac{1}{r_{k}}+\frac{1}{r_{k-1}}\right)^{2}=2\left(1+4+\frac{1}{r_{k}^{2}}+\frac{1}{r_{k-1}^{2}}\right) \text {. }
$$

两式相减得

$$
2\left(\frac{1}{r_{k+1}}-\frac{1}{r_{k-1}}\right)\left(\frac{1}{r_{k+1}}+\frac{1}{r_{k-1}}\right)=\left(\frac{1}{r_{k+1}}-\frac{1}{r_{k-1}}\right)\left(2+\frac{2}{r_{k}}+\frac{1}{r_{k-1}}+\frac{1}{r_{k+1}}\right),
$$

即

$$
\frac{1}{r_{k+1}}+\frac{1}{r_{k-1}}-\frac{2}{r_{k}}=2
$$

从而

$$
\left(\frac{1}{r_{k+1}}-\frac{1}{r_{k}}\right)-\left(\frac{1}{r_{k}}-\frac{1}{r_{k-1}}\right)=2
$$

累加有

$$
\frac{1}{r_{k}}=k^{2}-k+C .
$$

其中 $C$ 为待定系数. 因此 $\frac{1}{r_{1}}=C, \frac{1}{r_{2}}=2+C$. 由于大圆, 绿色圆和第一个灰色圆, 第二个灰色圆相切, 则有

$$
(-1+2+C+2+C)^{2}=2\left(1+4+C^{2}+(C+2)^{2}\right)
$$

即得 $C=\frac{9}{4}$. 所以

$$
r_{k}=\frac{4}{4 k^{2}-4 k+9}
$$

下一例题选自 2003 年第 44 届 IMO 预选试题(见文献 [5]).

例 4. 设 $\triangle A B C$ 的半周长为 $p$, 内切圆半径为 $r$, 分别以 $B C, C A, A B$ 为直径在 $\triangle A B C$ 的外侧作半圆, 设与这三个半圆均相切的圆 $T$ 的半径为 $t$. 证明:

$$
\frac{p}{2}<t \leq \frac{p}{2}+\left(1-\frac{\sqrt{3}}{2}\right) r
$$

证明. 如图 6, 设圆 $T$ 的圆心为 $O$, 点 $D, E, F$ 分别为边 $B C, C A, A B$ 的中点, 圆 $T$ 与三个半圆的切点分别为 $D^{\prime}, E^{\prime}, F^{\prime}$, 又设这三个半圆的半径分别为 $d^{\prime}, e^{\prime}, f^{\prime}$. 则 $D D^{\prime}, E E^{\prime}, F F^{\prime}$均过点 $O$, 且 $p=d^{\prime}+e^{\prime}+f^{\prime}$. 设

$$
\begin{aligned}
& d=\frac{p}{2}-d^{\prime}=\frac{-d^{\prime}+e^{\prime}+f^{\prime}}{2}, \\
& e=\frac{p}{2}-e^{\prime}=\frac{d^{\prime}-e^{\prime}+f^{\prime}}{2}, f=\frac{p}{2}-f^{\prime}=\frac{d^{\prime}+e^{\prime}-f^{\prime}}{2} .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-5.jpg?height=517&width=514&top_left_y=1392&top_left_x=1182)

图 6 则 $d+e+f=\frac{p}{2}$.

在三角形 $A B C$ 内部, 分别以 $D, E, F$ 为圆心, $d, e, f$ 为半径作三个较小的半圆, 因为 $d+e=f^{\prime}=\frac{1}{2} A B=D E, e+f=d^{\prime}=\frac{1}{2} B C=E F, f+d=e^{\prime}=$ $\frac{1}{2} A C=F D$, 所以这三个较小的半圆两两相切, 且这些切点分别为 $\triangle D E F$ 的内切圆与其三边的切点.

设 $D D^{\prime}, E E^{\prime}, F F^{\prime}$ 与较小的半圆分别交于点 $D^{\prime \prime}, E^{\prime \prime}, F^{\prime \prime}$. 因为这些半圆不互相重叠, 且 $O$ 为这些半圆外部的点, 所以 $D^{\prime} O>D^{\prime} D^{\prime \prime}$, 即 $t>\frac{p}{2}$. 因此 (8) 式左边得证. 设 $g=t-\frac{p}{2}$, 则有

$$
O D^{\prime \prime}=O E^{\prime \prime}=O F^{\prime \prime}=g .
$$

因此, 以 $O$ 为圆心, $g$ 为半径的圆与这三个互切的半圆均相切. 故由 Descartes 定理, 得

$$
2\left(\frac{1}{d^{2}}+\frac{1}{e^{2}}+\frac{1}{f^{2}}+\frac{1}{g^{2}}\right)=\left(\frac{1}{d}+\frac{1}{e}+\frac{1}{f}+\frac{1}{g}\right)^{2} .
$$

于是

$$
\frac{1}{g}=\frac{1}{d}+\frac{1}{e}+\frac{1}{f}+2 \sqrt{\frac{d+e+f}{d e f}}
$$

又因为

$$
S_{D E F}=\frac{1}{4} S_{A B C}=\frac{p r}{4}=\sqrt{(d+e+f) d e f}
$$

所以

$$
\frac{r}{2}=\frac{2}{p} \sqrt{(d+e+f) d e f}=\sqrt{\frac{d e f}{d+e+f}}
$$

故要证明 (8) 式右边, 即等价证明

$$
\frac{r}{2 g} \geq \frac{1}{2-\sqrt{3}}=2+\sqrt{3}
$$

由于

$$
\frac{r}{2 g}=\sqrt{\frac{d e f}{d+e+f}}\left(\frac{1}{d}+\frac{1}{e}+\frac{1}{f}+2 \sqrt{\frac{d+e+f}{d e f}}\right)=\frac{x+y+z}{\sqrt{x y+y z+x z}}+2,
$$

其中 $x d=1, y e=1, z f=1$. 故而只需证明

$$
(x+y+z)^{2} \geq 3(x y+y z+x z) .
$$

而上式显然成立，因为

$$
(x+y+z)^{2}-3(x y+y z+x z)=\frac{1}{2}\left((x-y)^{2}+(y-z)^{2}+(z-x)^{2}\right) \geq 0 \text {. }
$$

因此 (8) 式右边也成立.

Descartes 定理在三维空间中仍有类似的结论: 若 5 个球的半径为 $r_{i}, i=$ $1,2,3,4,5$, 满足任意一个球与其他四个球外切. 则

$$
\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}+\frac{1}{r_{4}}+\frac{1}{r_{5}}\right)^{2}=3\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}+\frac{1}{r_{3}^{2}}+\frac{1}{r_{4}^{2}}+\frac{1}{r_{5}^{2}}\right) .
$$

利用三维的 Descartes 定理, 我们就可以解决 1995 年的 CMO 试题 (见文献 $[6])$.

例 5. 空间有四个球, 它们的半径分别为 $2,2,3,3$. 每个球都与其余 3 个球外切, 另有一个小球与这四个球都外切. 求该小球的半径.

解法一. 如图 7, 设四个球的球心分别为 $A, B, C, D$, 则四个球心组成四面
体 $A B C D$, 其中 $A B=4, C D=6, A C=B C=A D=B D=5$. 设 $E, F$ 分别为 $A B, C D$ 中点, 小球球心为 $O$, 半径为 $r$. 则

$$
\begin{aligned}
& A E=D E=\sqrt{A C^{2}-C E^{2}}=\sqrt{5^{2}-2^{2}}=\sqrt{21}, \\
& E F=\sqrt{A E^{2}-A F^{2}}=\sqrt{5^{2}-2^{2}-3^{2}}=2 \sqrt{3}
\end{aligned}
$$

易知四面体 $A B C D$ 关于平面 $A B F, C D E$ 对称, 四个球也有此性质. 故由对称性, $O$ 在 $E F$ 上, 且

![](https://cdn.mathpix.com/cropped/2024_02_26_5914f6d5d66c4fa8b44bg-7.jpg?height=317&width=363&top_left_y=401&top_left_x=1326)

图 7

$$
O E=\sqrt{O C^{2}-C E^{2}}=\sqrt{(r+2)^{2}-2^{2}}, O F=\sqrt{O A^{2}-A F^{2}}=\sqrt{(r+3)^{2}-3^{2}} .
$$

故由 $O E+O F=E F$ 得

$$
\sqrt{(r+2)^{2}-2^{2}}+\sqrt{(r+3)^{2}-3^{2}}=2 \sqrt{3} .
$$

从而解得 $r=\frac{6}{11}$.

解法二. 利用 Descartes 定理解决该题. 设所求的球的半径为 $r=\frac{1}{x}$, 则由 Descartes 定理, 得

即

$$
\left(\frac{1}{2}+\frac{1}{2}+\frac{1}{3}+\frac{1}{3}+x\right)^{2}=3\left(\frac{1}{2^{2}}+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\frac{1}{3^{2}}+x^{2}\right)
$$

$$
\left(\frac{5}{3}+x\right)^{2}=3\left(\frac{13}{18}+x^{2}\right)
$$

解得 $x=\frac{11}{6}$, 从而 $r=\frac{6}{11}$.

本文最后, 作为练习, 请读者给出下面两个问题的解答.

习题 1. 设已知三个圆彼此外切, 且半径分别为 $a, b, c$, 若还有两个圆分别与这三个圆外切和内切, 且在这两圆中记小圆的半径为 $x$, 大圆的半径为 $y$, 求 $\frac{1}{x}-\frac{1}{y}$.

提示. 由

$$
\left(\frac{1}{x}+\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\right)^{2}=2\left(\frac{1}{x^{2}}+\frac{1}{a^{2}}+\frac{1}{b^{2}}+\frac{1}{c^{2}}\right)
$$

以及

$$
\left(-\frac{1}{y}+\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\right)^{2}=2\left(\frac{1}{y^{2}}+\frac{1}{a^{2}}+\frac{1}{b^{2}}+\frac{1}{c^{2}}\right),
$$

两式联立即可.

习题 2. (2013 OMOP) 设多项式 $P(t)=t^{3}+27 t^{2}+199 t+432$. 假设 $a, b, c, x$是不同的正实数满足 $P(-a)=P(-b)=P(-c)=0$, 且

$$
\sqrt{\frac{a+b+c}{x}}=\sqrt{\frac{b+c+x}{a}}+\sqrt{\frac{c+a+x}{b}}+\sqrt{\frac{a+b+x}{c}} .
$$

若 $x=\frac{m}{n}, \operatorname{gcd}(m, n)=1, m, n \in \mathbb{N}^{+}$, 求 $m+n$ 的值.

提示. 利用例 3 的结论易得.

致谢. 特别感谢萧振纲教授对本文细心审稿和指正文章的错误并修改.

## 参考文献

[1] 沈文选, 杨清桃. 几何瑰宝: 平面几何 500 名题暨 1000 条定理 (上) [M]. 哈尔滨: 哈尔滨工业大学出版社, 2010.

[2] 梁绍鸿. 初等数学复习及研究 (平面几何) [M]. 北京: 人民教育出版社, 1958.

[3] 萧振纲. 几何变换与几何证题 $[\mathrm{M}]$. 哈尔滨: 哈尔滨工业大学出版社, 2010.

[4] 中国国家集训队教练组编. 走向 IMO: 数学奥林匹克试题集锦 (2007) [M]. 上海: 华东师范大学出版社, 2007.

[5] D. Djukić, V. Janković, I. Matić, N. Petrović. The IMO Compendium (19592009) [M]. 2nd, Springer, 2011.

[6] 刘培杰. 历届 CMO 中国数学奥林匹克试题集 (1986-2009) [M]. 哈尔滨: 哈尔滨工业大学出版社, 2008.

编者注: 本文初稿由湖南理工学院萧振纲教授审阅. 作者修改后, 由上海大学博士生施柯杰对修改稿进行审核校对。

