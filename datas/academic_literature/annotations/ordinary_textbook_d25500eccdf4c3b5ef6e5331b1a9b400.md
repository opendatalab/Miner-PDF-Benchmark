数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 预给径向半径的凸多边形的最大内径问题 

李先颖

本文主要讨论和解决冷岗松教授提出的如下关于平面凸集的问题:

命题 1 如果一个平面上的凸多边形 $P$ 内存在一点 $K$, 过 $K$ 的任意直线与 $P$ 相交形成的截线段的长度均不小于 1 , 则 $P$ 包含一个半径为 $\frac{\sqrt{3}}{4}$ 的圆.

事实上, 对于满足命题 1 的平面凸多边形 $P$, 取 $P$ 所包含的一个极大的圆 $\Omega$, 则 $\Omega$ 至少与 $P$ 的至少三条边（或者两条平行的边）相切.

(i) 若 $\Omega$ 与 $P$ 的两条平行的边相切, 由凸性可知 $P$ 一定位于这两条平行线之间. 注意到过 $K$ 作垂直于这两条平行线方向的截线段长度不小于 1 , 因此这两条平行线之间的距离至少为 1 , 从而 $\Omega$ 的半径至少为 $\frac{1}{2}>\frac{\sqrt{3}}{4}$, 命题成立.

(ii) 若 $\Omega$ 与 $P$ 的至少三条边相切, 由凸性可知 $P$ 一定包含在这三条边所在直线围成的三角形内部. 注意到该三角形也满足命题 1 所描述的条件, 并且 $\Omega$ 作为该三角形的内切圆就是它所包含的最大的圆, 所以只需要证明命题对于三角形成立即可.

至此, 我们将平面任意凸多边形的问题转化成了平面三角形的问题, 换句话说, 命题 1 等价于:

命题 2 如果 $\triangle A B C$ 内存在一点 $K$, 过 $K$ 的任意直线与 $\triangle A B C$ 相交形成的截线段的长度均不小于 1 , 则 $\triangle A B C$ 的内切圆半径 $r \geq \frac{\sqrt{3}}{4}$.

我们证明一个更强的结论：

命题 3 如果 $\triangle A B C$ 内存在一点 $K$, 过 $K$ 作三条分别垂直于 $A I, B I, C I$ 的直线 ( $I$ 为 $\triangle A B C$ 内心), 与 $\triangle A B C$ 相交形成的截线段的长度均不小于 1 , 则 $\triangle A B C$ 的内切圆半径 $r \geq \frac{\sqrt{3}}{4}$.

事实上, 设过 $K$ 作垂直于 $A I$ 的直线交直线 $A I$ 于 $A_{0}$, 且该直线与射线 $A B, A C$ 相交形成的截线段长度为 $l_{A}$. 类似定义 $B_{0}, l_{B} ; C_{0}, l_{C}$.

修订日期: 2019-12-14.
根据位似, 我们有

$$
l_{A}=\frac{2 r}{\cos (A / 2)} \cdot \frac{A A_{0}}{A I}
$$

由条件, $l_{A} \geq 1$, 所以

$$
\frac{A A_{0}}{A I} \geq \frac{\cos (A / 2)}{2 r}
$$

设 $\triangle A B C$ 的旁心分别为 $I_{A}, I_{B}, I_{C}$, 注意到 $A A_{0}, B B_{0}, C C_{0}$ 分别为点 $K$ 到 $\triangle I_{A} I_{B} I_{C}$ 三边的距离, 根据面积, 我们有

$$
\sum_{c y c} \frac{A A_{0}}{A I_{A}}=1
$$

由 (1), (2), 以及 $A I=A I_{A} \tan \frac{B}{2} \tan \frac{C}{2}$, 有

$$
r \geq \frac{1}{2} \sum_{c y c} \cos \frac{A}{2} \tan \frac{B}{2} \tan \frac{C}{2}
$$

所以, 要证明 $r \geq \frac{\sqrt{3}}{4}$, 只需要证明如下不等式:

命题 4 对任意 $\triangle A B C$, 有

$$
\sum_{c y c} \cos \frac{A}{2} \tan \frac{B}{2} \tan \frac{C}{2} \geq \frac{\sqrt{3}}{2} .
$$

我们给出命题 4 的两个证明:

证明 1 设 $\triangle A B C$ 的三边长分别为 $B C=y+z, C A=z+x, A B=x+y$,则 (3) 等价于

$$
\sum_{c y c} \sqrt{x^{3}(y+z)} \geq \frac{\sqrt{3}}{2} \sqrt{(x+y+z) \prod_{c y c}(y+z)}
$$

将 (4) 左右两边平方, 等价于

$$
\begin{aligned}
& \sum_{c y c} x^{3}(y+z)+2 \sum_{c y c} \sqrt{y^{3} z^{3}} \sqrt{(x+y)(x+z)} \\
& \quad \geq \frac{3}{4}\left(\sum_{c y c} x^{3}(y+z)+2 \sum_{c y c} y^{2} z^{2}+4 x y z \sum_{c y c} x\right) .
\end{aligned}
$$

将 (5) 中的根式项利用 Cauchy 不等式 (用两次) 放缩

$$
2 \sqrt{(x+y)(x+z)} \geq(x+\sqrt{y z})+(\sqrt{x y}+\sqrt{x z}) .
$$

将 (5) 加强为

$$
\begin{aligned}
& \sum_{c y c} x^{3}(y+z)+4 x y z \sum_{c y c} \sqrt{y z}+4 \sum_{c y c} x^{2}\left(\sqrt{y^{3} z}+\sqrt{y z^{3}}\right) \\
& \quad \geq 2 \sum_{c y c} y^{2} z^{2}+12 x y z \sum_{c y c} x .
\end{aligned}
$$

等价于

$$
\sum_{c y c}(\sqrt{y}-\sqrt{z})^{2}\left(y z(\sqrt{y}+\sqrt{z})^{2}+4 x^{2} \sqrt{y z}-2 x y z\right) \geq 0 .
$$

最后, 因为

$$
y z(\sqrt{y}+\sqrt{z})^{2}+4 x^{2} \sqrt{y z}-2 x y z \geq 4 \sqrt{y^{3} z^{3}}+4 x^{2} \sqrt{y z}-2 x y z \geq 6 x y z>0,
$$

故 (6) 成立, 命题得证.

## 证明 2 (该方法属于上海中学黄嘉俊同学)

由

$$
\sum_{c y c} \tan \frac{B}{2} \tan \frac{C}{2}=1,
$$

可知 (3) 等价于

$$
\sum_{c y c} \frac{\cos \frac{A}{2}-\frac{\sqrt{3}}{2}}{\tan \frac{B}{2}} \geq 0
$$

令

$$
f(x)=\frac{\cos x-\sqrt{3} / 2}{\tan x}, x \in(0, \pi / 2)
$$

则

$$
\begin{aligned}
f^{\prime \prime}(x) & =\frac{1}{\sin ^{3} x}\left(2 \sin ^{4} x+\sin ^{2} x \cos ^{2} x+2 \cos ^{2} x-\sqrt{3} \cos x\right) \\
& =\frac{1}{\sin ^{3} x}\left(\cos ^{4} x-\cos ^{2} x-\sqrt{3} \cos x+2\right) \\
& >\frac{1}{\sin ^{3} x}(-1 / 4-\sqrt{3}+2) \\
& >0 .
\end{aligned}
$$

故 $f(x)$ 为 $(0, \pi / 2)$ 上的凸函数, 由 Jensen 不等式

$$
\sum_{c y c} f(A / 2) \geq 3 f(\pi / 6)=0
$$

故 (7) 成立, 命题得证.

杨路教授用他自己创作的软件 bottema 给出了命题 4 的机器证明, 我们将其作为附录.

$$
\begin{aligned}
& \text { read bottema2015; } \\
& \text { sgm }(\cos (\mathrm{A} / 2) * \tan (B / 2) * \tan (\mathrm{C} / 2) \text { ) } \\
& \qquad \cos \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right)+\cos \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right)+\cos \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right) \\
& \text { prove (\%)=sqrt (3)/2); } \\
& {\left[\frac{\sqrt{3}}{2} \leq \cos \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right)+\cos \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right)+\cos \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right)\right]} \\
& \left.\frac{\sqrt{3}}{2} \leq \cos \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right)+\cos \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right)+\cos \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right)\right] \\
& \frac{\sqrt{3}}{2} \leq \cos \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right)+\cos \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right)+\cos \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right)
\end{aligned}
$$

Start to solve the left polynomial , 0.171

Start to solve the right polynomial, 0.187

$$
\begin{aligned}
& \cos \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right)+\cos \left(\frac{B}{2}\right) \tan \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right)+\cos \left(\frac{C}{2}\right) \tan \left(\frac{A}{2}\right) \tan \left(\frac{B}{2}\right)-T \\
& \frac{\sqrt{\frac{x(x+y+z)}{(x+y)(z+x)}}}{y z}+\frac{\sqrt{\frac{y(x+y+z)}{(x+y)(y+z)}}}{z x}+\frac{\sqrt{\frac{z(x+y+z)}{(y+z)(z+x)}}}{x y}-T \\
& \text { LpolypqT: length }=, 2, T \text { degree }:=, 2 \\
& \text { RpolypqT: length }=, 19, T \text { degree }:=, 8 \\
& \text { Start to eliminate } T \\
& \text { finding the border curve(s) }, 0.328 \\
& O K \\
& \text { all right } \\
& \text { all right }
\end{aligned}
$$

found the border curve(s) finding the intersection point( $(s) \quad, 0.328$

$$
\begin{gathered}
\text { 1,2, Good } \\
\text { OK } \\
\text { all right }
\end{gathered}
$$

$$
\text { finding the critical point }(s), 0.343
$$

OK

$O K$

OK

all right

output one-dimension test point(s):

$[4,16,33,44]$
setting the test point(s) and doing test , 0.343

$[[4,3],[16,35],[16,74],[33,139],[33,291],[44,207],[44,469],[44,525]]$

The test result follows ---

Either always 1 or always - 1 means the inequality holds accordingly

the number of test point(s) is, 8

$$
\begin{gathered}
-1 \\
-1 \\
-1 \\
-1 \\
-1 \\
-1 \\
-1 \\
-1 \\
\text { less }
\end{gathered}
$$

The inequality holds, 0.687

