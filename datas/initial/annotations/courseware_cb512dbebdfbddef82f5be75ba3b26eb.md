# Ө 录 

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-001.jpg?height=243&width=406&top_left_y=320&top_left_x=1128)

## 上 册

第一章 函数 (第 $1-181$ 题) ..... 1
第二章 三角函数 (第 $182-247$ 题) ..... 128
第三章 向量 (第 $248-321$ 题) ..... 180
第四章 数列 (第 $322-418$ 题) ..... 234
第五章 不等式(第 419-514 题) ..... 317
下 册
第六章 解析几何 (第 515-697 题) ..... 399
第七章 计数与概率 (第 $698-727$ 题) ..... 554
第八章 平面几何(第 $728-735$ 题) ..... 573
第九章 立体几何(第 736-789 题) ..... 579
第十章 代数变形 (第 790-827 题) ..... 618
第十一章 微积分初步 (第 828-973 题) ..... 647
第十二章 其他好题(第 974-1001 题) ..... 782

## 第六章 解析几何

## 第 515 题 挖掘几何意义

已知 $a x+y=2 a+3$ ( $a$ 为正常数, $x \geqslant 0, y \geqslant 0$ ), 若 $x^{2}+y^{2}$ 的最大值为 $S$, 且 $S \in[49,121]$, 则 $a$ 的取值范围为

## 解析 $\left[\frac{1}{3}, \frac{3}{5}\right] \cup[2,4]$.

直线 $y=-a(x-2)+3$ 在第一象限以及 $x$ 轴、 $y$ 轴正半轴上的部分点 $(x, y)$ 到原点的距离最大值在 $[7$, $11]$ 上.

所以,

$$
7 \leqslant \max \left\{2+\frac{3}{a}, 2 a+3\right\} \leqslant 11
$$

由于 $\max \left\{2+\frac{3}{a}, 2 a+3\right\} \leqslant 11$ 即为

$$
\left\{\begin{array}{l}
2 a+3 \leqslant 11 \\
2+\frac{3}{a} \leqslant 11
\end{array}\right.
$$

所以 $\frac{1}{3} \leqslant a \leqslant 4$. 又 $\max \left\{2+\frac{3}{a}, 2 a+3\right\} \geqslant 7$ 即为

$$
2+\frac{3}{a} \geqslant 7 \text { 或 } 2 a+3 \geqslant 7 \text {. }
$$

所以 $a \leqslant \frac{3}{5}$ 或 $a \geqslant 2$.

综上, $a \in\left[\frac{1}{3}, \frac{3}{5}\right] \cup[2,4]$.

## 第 516 题 折线距离下的“轨迹”

设 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$ 是平面直角坐标系 $x O y$ 上的两点, 现定义由点 $A$ 到点 $B$ 的折线距离 $d(A$, $B)=\left|x_{2}-x_{1}\right|+\left|y_{2}-y_{1}\right|$. 对于平面 $x O y$ 上给定的不同两点 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$.

(1) 若点 $C(x, y)$ 是平面 $x O y$ 上的点, 试证明 $d(A, C)+d(C, B) \geqslant d(A, B)$.

(2) 在平面 $x O y$ 上是否存在点 $C(x, y)$ 同时满足:

(1) $d(A, C)+d(C, B)=d(A, B)$;

(2) $d(A, C)=d(C, B)$.

若存在, 请求出所有符合条件的点; 若不存在, 请说明理由.

## 解析 (1) 由题意知

$$
\begin{aligned}
d(A, C)+d(C, B) & =\left|x_{1}-x_{3}\right|+\left|y_{1}-y_{3}\right|+\left|x_{3}-x_{2}\right|+\left|y_{3}-y_{2}\right| \\
& \geqslant\left|\left(x_{1}-x_{3}\right)+\left(x_{3}-x_{2}\right)\right|+\left|\left(y_{1}-y_{3}\right)+\left(y_{3}-y_{2}\right)\right| \\
& \geqslant\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right|=d(A, B) .
\end{aligned}
$$

所以命题得证.

(2) 上述不等式中等号取得的条件是 $\left\{\begin{array}{l}\left(x_{1}-x_{3}\right)\left(x_{3}-x_{2}\right) \geqslant 0, \\ \left(y_{1}-y_{2}\right)\left(y_{3}-y_{2}\right) \geqslant 0,\end{array}\right.$ 也就是说

$$
\left\{\begin{array}{l}
\min \left(x_{1}, x_{2}\right) \leqslant x_{3} \leqslant \max \left(x_{1}, x_{2}\right) \\
\min \left(y_{1}, y_{2}\right) \leqslant y_{3} \leqslant \max \left(y_{1}, y_{2}\right)
\end{array}\right.
$$

不妨设 $x_{1} \leqslant x_{2}$, 则

(i) 当 $x_{1}=x_{2}$ 时, $C$ 为线段 $A B$ 的中点 $\left(x_{1}, \frac{y_{1}+y_{2}}{2}\right)$, 如图 1,

(ii) 当 $x_{1}>x_{2}$ 时,

(1) 当 $y_{1}=y_{2}$ 时, $C$ 为线段 $A B$ 的中点 $\left(\frac{x_{1}+x_{2}}{2}, y_{1}\right)$ 如图 2,

(2) 当 $y_{1}<y_{2}$ 时, $C$ 为过 $A B$ 中点, 斜率为 -1 的直线在以 $A B$ 为对角线的矩形内部的线段上的点, 如图 3,

(3) 当 $y_{1}>y_{2}$ 时, $C$ 为过 $A B$ 中点, 斜率为 1 的直线在以 $A B$ 为对角线的矩形内部的线段上的点, 如图 4 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-003.jpg?height=289&width=384&top_left_y=1045&top_left_x=215)

图1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-003.jpg?height=299&width=379&top_left_y=1037&top_left_x=632)

图2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-003.jpg?height=283&width=382&top_left_y=1051&top_left_x=1045)

图3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-003.jpg?height=288&width=365&top_left_y=1040&top_left_x=1463)

图4

思考与总结

其本质是考虑折线段、折线垂直平分线. 以下是折线椭圆、折线双曲线和折线抛物线.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-003.jpg?height=350&width=1210&top_left_y=1522&top_left_x=418)

## 第 517 题 逐步调整

已知点 $A(m, 0)$ 和双曲线 $x^{2}-y^{2}=1$ 右支上的两个动点 $B, C$, 在动点 $B, C$ 运动的过程中,若存在三个等边 $\triangle A B C$, 则实数 $m$ 的取值范围是 $\qquad$
解析 $(\sqrt{6},+\infty)$.

考虑以点 $A$ 为圆心, $r$ 为半径的圆与双曲线交于 4 个点 $M, N, P, Q$, 且 $M, N$ 位于 $x$ 轴上方, $P, Q$ 位于 $x$轴下方, 点 $M$ 与点 $Q$ 的横坐标相同, 点 $N$ 与点 $P$ 的横坐标相同, 点 $M$ 的横坐标大于点 $N$ 的横坐标. 线段 $M N$ 的中点为 $H$, 双曲线的右顶点为 $G$, 如图.

显然 $\triangle M A Q$ 和 $\triangle N A P$ 均可通过调整 $r$ 变为点 $A$ 所对的边与 $x$ 轴垂直的等边三角形, 且调整成的等边
三角形相同. 考虑到图形的对称性, 只需要研究 $\triangle M A N$ 与 $\triangle N A Q$ 是否能够通过调整变为等边三角形.

联立双曲线 $x^{2}-y^{2}=1$ 与圆 $(x-m)^{2}+y^{2}=r^{2}$, 有

$$
r^{2}=2\left(x-\frac{1}{2} m\right)^{2}+\frac{m^{2}}{2}-1
$$

因此点 $H$ 的横坐标为定值 $\frac{m}{2}$. 设双曲线上横坐标为 $\frac{m}{2}$ 的点为 $E$, 那么直线 $M N$ 的极限位置即双曲线在点 $E$ 处的切线. 记 $\angle E A G=\theta$, 当点 $N$ 与点 $G$ 重合时, $\angle M A N=\varphi$.

当点 $N$ 从点 $E$ 处运动到点 $G$ 处时, $\angle M A N$ 从 0 单调递增变化到 $\varphi$; 而 $\angle N A Q$ 满足

$$
\angle N A Q=2 \theta-\angle E A N+\angle E A M=2 \theta-2 \angle E A H
$$

由于 $H$ 点的纵坐标递减, 因此 $\angle E A H$ 单调递增, 因此 $\angle N A Q$ 从 $2 \theta$ 单调递减变化到 $\varphi$.

由于 $\angle M A N$ 与 $\angle N A Q$ 的变化区间无公共部分, 因此当 $\angle M A N$ 和 $\angle N A Q$ 变化的区间的并集 $(0,2 \theta)$ 中包含 $\frac{\pi}{3}$ 时符合题意, 也即问题等价于保证 $\theta>\frac{\pi}{6}$, 也即点 $E$ 处的切线斜率小于 $\sqrt{3}$.

由于 $y=\sqrt{x^{2}-1}$ 的导数 $y^{\prime}=\frac{x}{\sqrt{x^{2}-1}}$, 于是只需要

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-004.jpg?height=507&width=677&top_left_y=656&top_left_x=1119)

$$
\frac{\frac{m}{2}}{\sqrt{\left(\frac{m}{2}\right)^{2}-1}}<3
$$

解得 $m>\sqrt{6}$.

## 第 518 题 挖掘技术哪家强?

设点 $A(1,0), B(2,1)$, 如果直线 $a x+b y=1$ 与线段 $A B$ 有一个公共点, 那么 $a^{2}+b^{2}$ 的
A. 最小值为 $\frac{1}{5}$
B. 最小值为 $\frac{\sqrt{5}}{5}$
C. 最大值为 $\frac{1}{5}$
D. 最大值为 $\frac{\sqrt{5}}{5}$

## 解析 A.

解法一 题目中关键条件是直线 $a x+b y=1$ 与线段 $A B$ 有一个公共点, 这个条件可以转化成点 $A, B$ 在直线 $a x+b y=1$ 的两侧或 $A, B$ 中有一点在直线 $a x+b y=1$上 (同时, 直线不能与线段重合). 于是我们可以得到 $a, b$ 所满足的不等式, 从而得到它们的可行域, 再将所求代数式转化成可行域中的点 $(a, b)$ 到原点的距离的平方, 考虑距离的最值即可.

因为线段 $A B$ 与直线 $a x+b y=1$ 有一个公共点, 所以

$$
(a-1)(2 a+b-1) \leqslant 0 .
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-004.jpg?height=372&width=334&top_left_y=1860&top_left_x=1460)

图 1

建立平面直角坐标系 $a O b$, 则 $a, b$ 所满足的可行域如图 1 所示.

故原点到可行域中的点 $(a, b)$ 的距离 $\sqrt{a^{2}+b^{2}}$ 有最小值 $\frac{1}{\sqrt{5}}$, 从而 $a^{2}+b^{2}$ 有最小值 $\frac{1}{5}$.

解法二 记 $a x+b y=1$ 为直线 $l$, 则直线 $l$ 可以表示不经过原点的任意一条直线, 同时 $l$ 与线段 $A B$ 有且只有一个公共点, 直接考虑 $a^{2}+b^{2}$ 对于 $l$ 的几何意义.
因为原点到直线 $l$ 的距离为

$$
d=\frac{1}{\sqrt{a^{2}+b^{2}}}
$$

所以 $a^{2}+b^{2}=\frac{1}{d^{2}}$, 本题转化为思考原点到满足条件的直线 $l$ 的距离 $d$ 的最值情况. 显然 $d$ 没有最小值,即 $\sqrt{a^{2}+b^{2}}$ 没有最大值,下面考虑 $d$ 的最大值:

若 $P$ 是线段 $A B$ 与直线 $l$ 的公共点,则 $d \leqslant O P \leqslant O B$, 当 $l \perp O P$ 时第一个等号成

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-005.jpg?height=332&width=357&top_left_y=191&top_left_x=1511)

图 2 立, 当 $P$ 与 $B$ 重合时第二个等号成立, 如图 2.

故 $d$ 的最大值为 $\sqrt{5}$. 故 $a^{2}+b^{2}$ 有最小值 $\frac{1}{5}$.

## 第 519 题“四角星”区域

平面内定义 “区域 $X$ ”为满足条件 $P$ 的所有线段所在的区域. 如: 平面直角坐标系中, 若条件 $P$ 为 “线段的一端在原点, 另一端距离原点不超过 1 个单位长度”, 则其对应的“区域 $X$ ”为满足 $x^{2}+y^{2} \leqslant 1$ 的区域. 若平面内有夹角成 $60^{\circ}$ 的两条直线 $l_{O A}$ 与 $l_{O B}$, 且两直线交于点 $O$, 点 $C, D$ 分别为 $l_{C A}$ 与 $l_{O B}$ 上的点,并满足条件 $P:|O C| \cdot|O D|=4, E$ 为线段 $C D$ 的中点, 记所有线段 $C D$ 所在区域为“区域 $X$ ”. 试判断：

(1) $I$ 为 $\angle A O B$ 的角平分线上一点, 且 $|O I|=2$, 以 $I$ 为圆心, $2-\sqrt{3}$ 为半径作圆, 则该圆上的点均不在“区域 $X$ ”内;

(2) 点 $E$ 在“区域 $X$ ”内, 且 $|O E|_{\min }=\sqrt{3}$;

(3)过点 $E$ 作 $E M \perp O A$ 于点 $M, E N \perp O B$ 于点 $N$, 记 $\triangle M N E$ 的面积为 $S_{1}$, 过点 $E$ 作 $E F / / l_{O A}$ 交 $l_{O B}$于点 $F$, 作 $E G / / l_{O B}$ 交 $l_{C A}$ 于点 $G$, 记 $\triangle O F G$ 的面积为 $S_{2}$, 则 $S_{1} \leqslant S_{2}$ 恒成立;

(4)存在有限条直线 $l$,使得整条 $l$ 在“区域 $X$ ”内.

其中正确的有 $\qquad$ .

## 解析 (3).

我们知道, 如果 $C, D$ 在两条互相垂直的直线 (不妨设为 $x$ 轴与 $y$ 轴) 上运动, 且有 $|O C| \cdot|O D|=4$, 则它们的中点 $E$ 的轨迹为两对双曲线 $x y= \pm 1$. 而线段所在的区域为以这两对双曲线为边界的“四角星”区域, 但不包含原点, 如图 1.

现在两条互相垂直的直线变成了夹角为 $60^{\circ}$ 的两条直线, 我们猜测点 $E$ 的轨迹仍然为两条双曲线, 下面给出严格推导.

以 $l_{C A}, l_{O B}$ 的两条角平分线为坐标轴建立直角坐标系, 使得 $\angle x O A=$ $\angle x O B=30^{\circ}$, 先考虑点 $C, D$ 分别在第一、四象限时点 $E$ 的轨迹:

设 $|O C|=r$, 则 $|O D|=\frac{4}{r}$, 于是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-005.jpg?height=453&width=447&top_left_y=1666&top_left_x=1417)

图 1

$$
C\left(\frac{\sqrt{3}}{2} r, \frac{1}{2} r\right), D\left(\frac{\sqrt{3}}{2} \cdot \frac{4}{r},-\frac{1}{2} \cdot \frac{4}{r}\right)
$$

从而它们的中点 $E$ 的坐标为

$$
E\left(\sqrt{3}\left(\frac{r}{4}+\frac{1}{r}\right), \frac{r}{4}-\frac{1}{r}\right)
$$

于是 $E$ 点的坐标 $(x, y)$ 满足

$$
\left(\frac{x}{\sqrt{3}}\right)^{2}-y^{2}=1
$$

其实,当 $r$ 变成 $-r$ 时, $C, D$ 在第二、四象限,中点 $E$ 也满足上面的方程, 从而点 $E$ 的轨迹的一部分为双曲线

$$
\frac{x^{2}}{3}-y^{2}=1
$$

另外,当点 $C, D$ 分别在第一、二象限或第三、四象限时, 点 $E$ 的轨迹为另一组双曲线:

$$
\frac{x^{2}}{3}-y^{2}=-1
$$

如图 2.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-006.jpg?height=389&width=554&top_left_y=203&top_left_x=1224)

图 2

易知, “区域 $X$ ”为这两组双曲线所夹的“四角形”区域,除去原点. 下面我们来判断四个命题的真假:

对于(1), 点 $I$ 可能在 $x$ 轴上, 也可能在 $y$ 轴上, 当点 $I$ 在 $x$ 轴上时, 圆上恰有一个点 $(\sqrt{3}, 0)$ 在区域 $X$ 内, (1)错误;

对于(2), 当点 $E$ 的轨迹为焦点在 $y$ 轴上的双曲线时, 所以 $|O E|_{\min }=1$, (2)错误;

对于(3), 因为 $S_{1}=\frac{1}{2}|M E| \cdot|N E| \sin 120^{\circ}, S_{2}=S_{\triangle G F F}=\frac{1}{2}|G E| \cdot|E F| \sin 60^{\circ}$, 所以有 $S_{2}>S_{1}$, (3)正确, 如图 3 .

对于(4), 因为原点不在区域 $X$ 内,所以不存在这样的直线.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-006.jpg?height=310&width=312&top_left_y=716&top_left_x=1466)

图 3

事实上, 在这个问题中,直线 $C D$ 与 $E$ 点的轨迹形成的双曲线始终相切 (利用双曲线的“垂径定理”可以得到一个比较简单的证明), 切点为 $E$, 所以本题同时给出了双曲线的一条重要性质: 过双曲线上任意一点 $E$ 作双曲线在该点的切线, 这条切线与双曲线的渐近线相交于点 $C, D$, 则切点 $E$ 恰为线段 $C D$ 的中点,且双曲线的中心 $O$ 与这两个交点的距离乘积 $|O C| \cdot|O D|$ 为定值 (当双曲线为标准双曲线时, 此定值为 $\left.a^{2}+b^{2}\right)$.

## 第 520 题 殊途同归

点 $P$ 在曲线 $C: \frac{x^{2}}{4}+y^{2}=1$ 上, 若存在过点 $P$ 的直线交曲线 $C$ 于 $A$ 点, 交直线 $l: x=4$ 于 $B$ 点, 满足 $|P A|=|A B|$ 或 $|P A|=|P B|$, 则称点 $P$ 为“ $D$ 点”, 那么下列结论正确的是

A. 曲线 $C$ 上的所有点都是“ $D$ 点”

B. 曲线 $C$ 上仅有有限个点是“ $D$ 点”

C. 曲线 $C$ 上的所有点都不是 “ $D$ 点”

D. 曲线 $C$ 上有无穷多个点 (但不是所有点) 是“ $D$ 点”

解析 $\mathrm{D}$.

在这个问题中, $P, A, B$ 都是动点, 其中点 $P, A$ 在椭圆上运动, 点 $B$ 在直线上运动, 为了便于思考, 我们先固定一个点,看看其他两个点的变化情况,这有些类似于多参数问题中先固定一个参数.

思路一 先固定点 $A$, 考虑当点 $B$ 在直线 $l$ 上运动时, $P$ 点形成的轨迹(先不管“点 $P$ 在椭圆上”这个条件), 再让点 $A$ 在椭圆上运动起来, 考虑所有满足条件的点 $P$ 形成的轨迹, 看看这个轨迹与椭圆的关系.

记点集

$$
I_{1}=\{P|A \in C, B \in l,| P A|=| P B \mid\}
$$

点集

$$
I_{2}=\{P|A \in C, B \in l,| P A|=| A B \mid\}
$$

对于点集 $I_{1}$, 固定点 $A$, 让点 $B$ 在直线 $l$ 上运动时, 满足条件的点 $P$ 形成的集合即直线 $l$ 关于点 $A$ 缩放 $\frac{1}{2}$ 的直线 $l^{\prime}$. 因此, 当点 $A$ 在椭圆上移动时, 直线 $l^{\prime}$ 也会随之平行移动, 如图 1 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-007.jpg?height=318&width=343&top_left_y=378&top_left_x=388)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-007.jpg?height=323&width=394&top_left_y=354&top_left_x=1075)

图 2

$l^{\prime}$ 扫过的区域是如图 2 的带状区域:

对于点集 $I_{2}$, 当固定点 $A$, 让点 $B$ 在直线 $l$ 上运动时, $P$ 点形成的轨迹即直线 $l$ 关于点 $A$ 对称的直线 $l^{\prime}$.如图 3, 因此, 当点 $A$ 在椭圆上运动时, $l^{\prime}$ 扫过的区域为如图 4 的带状区域:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-007.jpg?height=241&width=405&top_left_y=899&top_left_x=458)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-007.jpg?height=270&width=466&top_left_y=896&top_left_x=1116)

图 4

接下来考虑 $U=\{P \mid P \in C\}$ 与 $I_{1} \cup I_{2}$ 的关系, 显然, 椭圆上有无穷多个 “ $D$ 点”, 但不是所有点都是“ $D$点”, 椭圆上不在两个带状区域内的点不是 “ $D$ 点”, 即横坐标在 $(0,1)$ 之间的椭圆上的点不是“ $D$ 点”, 故选 D.

思路二 在椭圆上任取一点 $P\left(x_{0}, y_{0}\right)$, 我们直接考查能否找到满足条件的 $A, B$ 点. 因为 $P, A, B$ 三点共线,所以只需要考虑横坐标即可.

若存在 $A, B$ 满足 $|P A|=|P B|$, 当点 $A$ 从 $P$ 开始运动时, 一开始有 $|P A|<|P B|$, 当点 $A$ 为椭圆的左顶点时, 若有 $|P A| \geqslant|P B|$, 则 $A, B$ 存在, 即

$$
x_{0}-(-2) \geqslant 4-x_{0}
$$

解得 $x_{0} \geqslant 1$.

同理, 若存在 $A, B$ 满足 $|P A|=|A B|$, 当点 $A$ 从 $P$ 开始运动时, 一开始有 $|P A|<|A B|$, 当点 $A$ 为椭圆的右顶点时, 若有 $|P A| \geqslant|A B|$, 则 $A, B$ 存在, 即

$$
2-x_{0} \geqslant 4-2
$$

解得 $x_{0} \leqslant 0$ ，故选 D.

综上知,当 $x_{0} \leqslant 0$ 或 $x_{0} \geqslant 1$ 时, $P$ 点为“ $D$ 点”.

思路三 本题也可以从纯代数角度考虑, 根据横坐标的关系得到“ $D$ 点”的横坐标范围.

设 $P\left(x_{0}, y_{0}\right)$, 因为 $P, A, B$ 三点共线, 所以条件 $|P A|=|P B|$ 当且仅当

$$
x_{A}=2 x_{0}-4,
$$

而 $x_{A} \in[-2,2]$, 解得

$$
x_{0} \in[1,3]
$$

同理条件 $|P A|=|A B|$ 当且仅当

$$
x_{A}=\frac{x_{0}+4}{2}
$$

由 $x_{A} \in[-2,2]$ 解得

$$
x_{0} \in[-8,0] \text {. }
$$

综上知, 当 $x_{0} \in[-2,0] \cup[1,2]$ 时, $P$ 点为 “ $D$ 点”, 故选 D.
思考与总结

本题的三个思路各有千秋,思路一与椭圆的形状无关,抓住了题目本质;思路二是动点存在性问题的常见思考方向,考虑变化中的边界;思路三在这个题目中最简洁, 但可推广性差. 不管是哪种方法,都没有直接考虑动直线的问题, 而是通过将距离相等转化成三个点的横坐标的关系, 去考虑对这三个点的转化与处理.

## 第 521 题 折线距离

在平面直角坐标系 $x O y$ 中, $O$ 为坐标原点. 定义 $P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$ 两点之间的“折线距离”为 $d(P, Q)=\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right|$.

(1) 若点 $A(-1,3)$, 则 $d(A, O)=$ $\qquad$ $;$

(2) 已知点 $B(1,0)$, 点 $M$ 是直线 $l: k x-y+k+3=0(k>0)$ 上的动点, $d(B, M)$ 的最小值为 ;

(3) 圆 $x^{2}+y^{2}=1$ 上一点与直线 $m: 2 x+y-2 \sqrt{5}=0$ 上一点的“折线距离”的最小值是 $\qquad$
解析 (1) ; (2) $\left\{\begin{array}{l}2 k+3,0<k \leqslant 1, \\ \frac{3}{k}+2, k>1 ;\end{array}\right.$ (3) $\frac{\sqrt{5}}{2}$.

用图形语言理解折线距离 $d(A, B)$, 其本质就是从 $A$ 到 $B$ 只能沿坚直方向和水平方向分别移动的折线的最小长度, 如图 1 两种颜色的折线路径都对应 $A, B$ 的折线距离.

(1) 根据折线距离的概念

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-008.jpg?height=241&width=244&top_left_y=1186&top_left_x=1532)

图 1

$$
d(A, O)=|-1|+|3|=4
$$

(2) 直线 $l$ 即

$$
y=k(x+1)+3
$$

是过定点 $C(-1,3)$ 的直线系. 先来确定点 $M$ 的位置.

过点 $B$ 作水平线与坚直线分别交直线 $l$ 于点

$$
S\left(-\frac{3}{k}-1,0\right), T(1,2 k+3)
$$

如图 2.

当点 $M$ 在点 $S$ 左下方时, 有

$$
d(B, M)>d(B, S)=|B S|
$$

当点 $M$ 在点 $T$ 右上方时, 有

$$
d(B, M)>d(B, T)=|B T|
$$

当点 $M$ 在线段 $S T$ 上 (包括端点) 时, 有

$$
d(B, M)=|B D|+|D M|=|B E|+|E M|,
$$

其中点 $D$ 为点 $M$ 在 $B S$ 上的投影, 点 $E$ 为点 $M$ 在 $B T$ 上的投影.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-008.jpg?height=375&width=465&top_left_y=1861&top_left_x=1312)

图 2

当 $0<k<1$ 时, 有 $|E M| \geqslant|E T|$, 从而

$$
d(B, M) \geqslant|B E|+|E T|=|B T|=d(B, T)
$$

当 $k \geqslant 1$ 时, 有 $|D M| \geqslant|D S|$, 从而

$$
d(B, M) \geqslant|B D|+|D S|=|B S|=d(B, S)
$$

因此 $d(B, M)$ 的最小值为

$$
\left\{\begin{array}{l}
d(B, T)=2 k+3,0<k<1 \\
d(B, S)=\frac{3}{k}+2, k \geqslant 1
\end{array}\right.
$$

(3) 在 (2) 中我们知道, 定点到直线上一点的折线距离的最小值等于该点到直线的水平距离或坚直距离中较小的一个.

因为直线 $m$ 的斜率为 -2 , 于是点 $M$ 到直线 $m$ 的折线距离的最小值即点 $M$ 到直线 $m$ 的水平距离,如图 3.

当点 $M$ 在单位圆上运动时, 点 $M$ 到直线 $m$ 的水平距离的最小值为 $\frac{\sqrt{5}}{2}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-009.jpg?height=398&width=308&top_left_y=196&top_left_x=1556)

图 3

## 第 522 题 运动中的规律探索

已知点 $A(-1,0), B(1,0), C(0,1)$, 直线 $y=a x+b(a>0)$ 将 $\triangle A B C$ 分割为面积相等的两部分, 则 $b$ 的取值范围是
A. $(0,1)$
B. $\left(1-\frac{\sqrt{2}}{2}, \frac{1}{2}\right)$
C. $\left(1-\frac{\sqrt{2}}{2}, \frac{1}{3}\right]$
D. $\left[\frac{1}{3}, \frac{1}{2}\right)$

## 解析 B.

解法一 动直线 $y=a x+b$ 的斜率为 $a$, 纵截距为 $b$, 且显然有 $b>0$.

注意到 $a>0$, 考虑 $a$ 的两个边界的情形:

当 $a=0$ 时, 可以通过直接计算面积得到

$$
b=1-\frac{\sqrt{2}}{2} \text {. }
$$

情形一 当 $b<1-\frac{\sqrt{2}}{2}$ 时, 结合图象易得右下方的面积始终比左上方的面积小.

情形二 当 $b>1-\frac{\sqrt{2}}{2}$ 时, $a$ 从 0 开始变化,右下方的面积开始时比左上方面积大, 之后右下方面积开始减小, 如果存在某个时候右下方的面积比左上方的面积小, 因为面积连续变化, 就能保证存在某个时刻两部分的面积相等.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-009.jpg?height=365&width=527&top_left_y=1580&top_left_x=1337)

图 1

我们去探索何时右下方的面积比左上方的面积小, 此时考虑另一个边界 $a \rightarrow+\infty$ 的情形, 如图 1.

右下方的面积大小取决于如图两块阴影面积的大小比较, 可以推测当 $b=\frac{1}{2}$ 时, 这两块面积接近相等.于是我们来分析 $b=\frac{1}{2}$ 的情形:

当 $b \geqslant \frac{1}{2}$ 时, 右下方的面积始终比左上方的面积大 ( $y$ 轴左边的阴影三角形面积始终比右边的阴影三角形的面积大).

而当 $b<\frac{1}{2}$ 时, 当 $a \rightarrow+\infty$ 时, 必然存在某个时候, 右下方的面积比左上方的面积小. 所以

$$
1-\frac{\sqrt{2}}{2}<b<\frac{1}{2}
$$

为所求的范围.

## 思考与总结

本题也可以从另外一个角度出发:

先探究将 $\triangle A B C$ 的面积平分的直线是什么样的.

考虑到 $a>0$, 该直线一定与线段 $B C$ 相交,于是我们从 $B C$ 上的一个动点 $M$ 出发去构造平分 $\triangle A B C$ 面积的直线.

根据动点 $M$ 在 $B C$ 中点的左上方还是右下方, 三角形被分成的两部分形状不同, 实际情况如图 2 所示：

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-010.jpg?height=369&width=506&top_left_y=704&top_left_x=343)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-010.jpg?height=396&width=576&top_left_y=677&top_left_x=953)

图 3

实际上 $b$ 的取值范围如图 3 中线段所示(不包含端点).

解法二 易知直线 $l: y=a x+b$ 与 $\triangle A B C$ 的交点不可能同时在边 $A C$ 和边 $A B$ 上,下面分两种情况来考虑.

情形一 直线 $l$ 与边 $A B$ 和 $B C$ 分别交于点 $M, N$, 交 $y$ 轴于 $F$ 点, 则 $b=O F$, 连结 $C M, O N$. 如图 4.

由 $l$ 平分 $\triangle A B C$ 的面积得 $S_{\triangle C N F}=S_{\triangle O F M}$, 从而有 $S_{\triangle O N C}=S_{\triangle O N M}$, 所以 $O N / / C M$. 于是有

$$
\frac{O F}{F C}=\frac{O N}{M C}=\frac{O B}{B M}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-010.jpg?height=353&width=528&top_left_y=1245&top_left_x=1261)

图 4

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-010.jpg?height=361&width=508&top_left_y=1662&top_left_x=1282)

图 5

$$
b=\frac{1}{1+B M}
$$

则 $b=O F$. 由 $a>0$ 得

显然 $1<B M \leqslant 2$, 所以 $\frac{1}{3} \leqslant b<\frac{1}{2}$.

情形二 直线 $l$ 与边 $A C$ 和 $B C$ 分别交于点 $D, E$, 交 $y$ 轴于 $F$ 点, 如

即 $\frac{b}{1-b}=\frac{1}{B M}$, 解得图 5.

$$
0<C E<C D \leqslant \sqrt{2}
$$

由

$$
S_{\triangle C D E}=\frac{1}{2} C D \cdot C E=\frac{1}{2}
$$

得 $1=C D \cdot C E<C D^{2}$, 所以

$$
1<C D \leqslant \sqrt{2}
$$

因为

$$
S_{\triangle C D E}=S_{\triangle C D F}+S_{\triangle C E F}=\frac{1}{2}(C D+C E) \cdot C F \cdot \sin 45^{\circ}=\frac{1}{2}
$$

故

$$
\frac{1}{C F \cdot \sin 45^{\circ}}=C D+C E=C D+\frac{1}{C D} \in\left(2, \frac{3 \sqrt{2}}{2}\right]
$$

所以 $\frac{2}{3} \leqslant C F<\frac{\sqrt{2}}{2}$, 从而得到

$$
1-\frac{\sqrt{2}}{2}<b \leqslant \frac{1}{3}
$$

综上所述, 实数 $b$ 的取值范围是 $\left(1-\frac{\sqrt{2}}{2}, \frac{1}{2}\right)$.

解法三 按直线 $y=a x+b$ 是否与斜边 $A B$ 相交分类讨论, 讨论的分界点为直线过点 $A$, 也即 $a=\frac{1}{3}$.

情形一 直线 $l$ 与边 $A C$ 和 $B C$ 分别交于点 $D, E$, 交 $y$ 轴于 $F$ 点, 如图 6. 此时 $a$ 的取值范围是 $\left(0, \frac{1}{3}\right)$.

设 $D\left(x_{1}, y_{1}\right), E\left(x_{2}, y_{2}\right)$, 则将直线 $y=a x+b$ 与相交直线 $A C \cup B C$ :

$$
(y-1)^{2}-x^{2}=0
$$

联立, 可得

$$
\left(a^{2}-1\right) x^{2}+2 a(b-1) x+(b-1)^{2}=0
$$

于是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-011.jpg?height=371&width=524&top_left_y=764&top_left_x=1341)

图 6

$$
\begin{aligned}
S_{\triangle C D E} & =\frac{1}{2} \cdot C D \cdot C E \\
& =\frac{1}{2} \cdot \sqrt{2}\left|x_{1}\right| \cdot \sqrt{2}\left|x_{2}\right| \\
& =\left|x_{1} x_{2}\right| \\
& =\frac{(1-b)^{2}}{1-a^{2}}
\end{aligned}
$$

从而

$$
(1-b)^{2}=\frac{1}{2}\left(1-a^{2}\right)
$$

因此 $b$ 的取值范围是 $\left(1-\frac{\sqrt{2}}{2}, \frac{1}{3}\right)$.

情形二 直线 $l$ 与边 $A B$ 和 $B C$ 分别交于 $D, E$, 交 $y$ 轴于 $F$ 点, 如图 7. 此时 $a$ 的取值范围是 $\left[\frac{1}{3},+\infty\right)$.

设 $D\left(x_{1}, y_{1}\right), E\left(x_{2}, y_{2}\right)$,则

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-011.jpg?height=365&width=527&top_left_y=1579&top_left_x=1336)

图 7

$$
x_{1}=-\frac{b}{a}, x_{2}=\frac{1-b}{a+1}
$$

于是

$$
\begin{aligned}
S_{\triangle B D E} & =\frac{\sqrt{2}}{4} \cdot B E \cdot B D \\
& =\frac{\sqrt{2}}{4} \cdot \sqrt{2}\left(1-x_{2}\right) \cdot\left(1-x_{1}\right) \\
& =\frac{1}{2} \cdot \frac{a+b}{a+1} \cdot \frac{a+b}{a} \\
& =\frac{(a+b)^{2}}{2 a(a+1)}
\end{aligned}
$$

从而

$$
(a+b)^{2}=a(a+1)
$$

即

$$
a=\frac{b^{2}}{1-2 b}
$$

因此 $b$ 的取值范围是 $\left[\frac{1}{3}, \frac{1}{2}\right)$.

综上所述, $b$ 的取值范围是 $\left(1-\frac{\sqrt{2}}{2}, \frac{1}{2}\right)$.

## 第 523 题 特征量与“T”型曲线

已知点 $A(-1,1)$, 若曲线 $G$ 上存在两点 $B, C$, 使得 $\triangle A B C$ 为正三角形, 则称 $G$ 为 $\mathrm{T}$ 型曲线. 给定下列三条曲线:

(1) $y=-x+3(0 \leqslant x \leqslant 3) ;$

(2) $y=\sqrt{2-x^{2}}(-\sqrt{2} \leqslant x \leqslant 0) ;$

(3) $y=-\frac{1}{x}(x>0)$.

则其中是 $\mathrm{T}$ 型曲线的为

## 解析 (3).

判定一个三角形为正三角形有很多种方式: 三边相等的三角形;有一个角为 $60^{\circ}$ 的等腰三角形; 底边上的高与底边的比值为 $\frac{\sqrt{3}}{2}$ 的等腰三角形等. 在动态问题中讨论正三角形的存在性问题时, 常常利用“顶角为 $60^{\circ}$ 的等腰三角形为正三角形”进行判定.

对于(1), 如图 1, 曲线 $G$ 为线段 $M N$, 以 $A$ 为圆心作圆与曲线 $G$ 交于两点构成等腰三角形. 由于顶角的最大值小于 $60^{\circ}$, 从而不存在满足要求的 $B, C$ 两点;

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-012.jpg?height=377&width=506&top_left_y=1738&top_left_x=217)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-012.jpg?height=377&width=380&top_left_y=1741&top_left_x=805)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-012.jpg?height=375&width=358&top_left_y=1739&top_left_x=1264)

图 3

对于(2), 如图 2, 曲线 $G$ 为一段圆弧, 以 $A$ 为圆心作圆与曲线 $G$ 交于两点构成等腰三角形. 由于顶角 $\angle M A N$ 的最小值大于 $60^{\circ}$, 从而不存在满足要求的 $B, C$ 两点;

对于 (3), 如图 3, 曲线 $G$ 为反比例曲线在第四象限的部分, 以 $A$ 为圆心作圆与曲线 $G$ 交于两点构成等腰三角形. 由于顶角 $\angle B A C$ 的范围为 $0^{\circ}<\angle B A C<90^{\circ}$, 且连续变化, 所以存在满足条件的 $B, C$ 两点.

## 第 524 题不变量与“完美点”

已知点 $A$ 在曲线 $P: y=x^{2}(x>0)$ 上, 圆 $A$ 过原点 $O$, 且与 $y$ 轴的另一个交点为 $M$. 若线段 $O M$, 圆 $A$ 和曲线 $P$ 上分别存在点 $B$, 点 $C$ 和点 $D$, 使得四边形 $A B C D$ (点 $A, B, C, D$ 按顺时针排列) 是正方形,则称点 $A$ 为曲线 $P$ 的“完美点”. 那么下列结论中正确的是

A. 曲线 $P$ 上不存在“完美点”

B. 曲线 $P$ 上只存在一个“完美点”,其横坐标大于 1

C. 曲线 $P$ 上只存在一个“完美点”, 其横坐标大于 $\frac{1}{2}$ 且小于 1

D. 曲线 $P$ 上存在两个“完美点”,其横坐标均大于 $\frac{1}{2}$

## 解析 B.

需要给这道题目配图. 当然, 除非先计算出 $A, B, C, D$ 四点的准确位置, 否则无法准确地画出这个正方形. 因此我们可以在曲线 $P$ 上挑一个点 $A$ 的位置, 然后在此基础上进行作图尝试. 虽然点 $A$ 的位置基本是错误的, 但如果我们使用尽量保证图形靠近正方形的作图法, 就可以通过调整 $A$ 点的位置, 将图形调整为正方形.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-013.jpg?height=381&width=333&top_left_y=1203&top_left_x=437)

图1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-013.jpg?height=373&width=332&top_left_y=1207&top_left_x=854)

图2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-013.jpg?height=373&width=315&top_left_y=1207&top_left_x=1269)

图3

如图 1, 连结 $O A$,则 $O A$ 的长度就是正方形的对角线长;

如图 2, 以点 $A$ 为圆心, $\frac{O A}{\sqrt{2}}$ 为半径作圆, 取该圆与 $y$ 轴交点中上方的一个为点 $B$, 取该圆与抛物线交点中上方的一个为点 $D$ (这是因为点 $A, B, C, D$ 按顺时针排列);

如图 3, 作 $\angle B A D$ 的平分线, 并截取 $A C=A O ;$

调整点 $A$ 的位置, 使得 $\angle B A D=90^{\circ}$ 即可.

接下来, 考虑这样的位置能否找到; 如果能找到, 有几个? 设点 $A$ 的坐标为 $A\left(m, m^{2}\right)$, 则 $m$ 至少为 1 , 否则无法找到点 $B$. 当 $m=1$ 时, 显然 $\angle B A D$ 为钝角; 而当 $m$ 逐渐增大时, 将 $\angle B A D$ 分割为两个部分 $\alpha$ 与 $\beta$, 如图 4.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-013.jpg?height=381&width=318&top_left_y=2108&top_left_x=650)

图4

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-013.jpg?height=384&width=334&top_left_y=2112&top_left_x=1051)

图5
很明显, 这两个部分都单调递减, 且趋于 0 . (想一想, 为什么?)于是满足条件的点 $A$ 的位置必然存在, 且唯一,选 B. 最后附上插画师的完成效果图, 如图 5.

'思考与总结

在处理复杂问题时,需要适当将问题拆解，用运动的观点看待问题. 这也是轨迹意识的重要体现.

## 第 525 题 交点直线系

如图, 在平面直角坐标系 $x O y$ 中, 设 $\triangle A B C$ 的顶点分别为 $A(0$, $a), B(b, 0), C(c, 0)$, 点 $P(0, p)$ 在线段 $A O$ 上(异于端点). 设 $a, b, c, p$为非零常数, 设直线 $B P, C P$ 分别与边 $A C, A B$ 交于点 $E, F$, 求直线 $O E$ 与直线 $O F$ 的方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-014.jpg?height=363&width=540&top_left_y=745&top_left_x=1198)

解析 用截距式方程容易求得直线 $A C$ 与 $B P$ 的方程为

$$
A C: \frac{x}{c}+\frac{y}{a}=1, B P: \frac{x}{b}+\frac{y}{p}=1 .
$$

所以过直线 $A C$ 与 $B P$ 的交点 $E$ 的直线系方程为

$$
\left(\frac{x}{c}+\frac{y}{a}-1\right)+\lambda\left(\frac{x}{b}+\frac{y}{p}-1\right)=0,
$$

其中 $\lambda$ 为参数. 该直线过原点 $O(0,0)$, 于是可得 $\lambda=-1$. 因此直线 $O E$ 的方程为

$$
\left(\frac{1}{c}-\frac{1}{b}\right) x+\left(\frac{1}{a}-\frac{1}{p}\right) y=0
$$

根据对称性可得直线 $O F$ 的方程为 $\left(\frac{1}{b}-\frac{1}{c}\right) x+\left(\frac{1}{a}-\frac{1}{p}\right) y=0$.

在图形中出现“三线共点”, 就可以考虑利用其中两条曲线的交点曲线系方程简化问题.

## 第 526 题 内心的轨迹

设 $P$ 为椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 上的动点, $F_{1}, F_{2}$ 为椭圆的两个焦点, $I$ 为 $\triangle P F_{1} F_{2}$ 的内心, 求点 $I$ 的轨迹方程.

## 解析 解法一

如图, 设内切圆 $I$ 与 $F_{1} F_{2}$ 的切点为 $H$, 半径为 $r$, 且 $F_{1} H=y, F_{2} H=z$, $P F_{1}=x+y, P F_{2}=x+z, c=\sqrt{a^{2}-b^{2}}$, 则

$$
\left\{\begin{array}{l}
y+z=2 c \\
2 x+y+z=2 a .
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-014.jpg?height=301&width=487&top_left_y=2285&top_left_x=1268)
直线 $I F_{1}$ 与 $I F_{2}$ 的斜率之积

$$
k_{I F_{1}} \cdot k_{I F_{2}}=-\frac{I H^{2}}{F_{1} H \cdot F_{2} H}=-\frac{r^{2}}{y z}
$$

而根据海伦公式, 有 $\triangle P F_{1} F_{2}$ 的面积为

$$
(x+y+z) r=\sqrt{x y z(x+y+z)},
$$

因此有

$$
k_{I F_{1}} \cdot k_{I F_{2}}=-\frac{x}{x+y+z}=-\frac{a-c}{a+c}
$$

再根据椭圆的斜率积定义, 可得 $I$ 点的轨迹是以 $F_{1} F_{2}$ 为长轴, 离心率 $e$ 满足

$$
e^{2}-1=-\frac{a-c}{a+c}
$$

的椭圆,其标准方程为

$$
\frac{x^{2}}{c^{2}}+\frac{y^{2}}{\frac{a-c}{a+c} \cdot c^{2}}=1, y \neq 0
$$

解法二 令 $P(a \cos \theta, b \sin \theta)$, 则 $\sin \theta \neq 0 . \triangle P F_{1} F_{2}$ 的面积

$$
S=\frac{1}{2} \cdot 2 c \cdot|b \sin \theta|=\frac{1}{2}(2 c+2 a) \cdot r
$$

其中 $r$ 为内切圆的半径, 解得

$$
r=\frac{b c \cdot|\sin \theta|}{a+c}=\left|y_{I}\right|
$$

另一方面, 由内切圆的性质及焦半径公式得

$$
\left(c-x_{I}\right)-\left(x_{I}+c\right)=\left|P F_{1}\right|-\left|P F_{2}\right|=(a-c \cos \theta)-(a+c \cos \theta),
$$

从而有 $x_{I}=c \cos \theta$. 消去 $\theta$ 得到点 $I$ 的轨迹方程为

$$
\frac{x^{2}}{c^{2}}+\frac{y^{2}}{\frac{a-c}{a+c} \cdot c^{2}}=1, y \neq 0
$$

## 第 527 题 三点共线

已知 $F_{1}, F_{2}$ 是椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ 的焦点, 直线 $P Q$ 过点 $F_{1}$ 且交椭圆于 $P, Q$ 两点. 若 $P F_{1}=F_{1} F_{2}$, 且 $2 P F_{1}=3 Q F_{1}$, 求椭圆的离心率.

解析 不妨设 $F_{1} F_{2}=2 c=6$, 则 $P F_{1}=F_{1} F_{2}=6, P F_{2}=2 a-P F_{1}=2 a-6, Q F_{1}=$ $\frac{2}{3} P F_{1}=4, Q F_{2}=2 a-Q F_{1}=2 a-4$.

由于 $\angle P F_{1} F_{2}$ 与 $\angle Q F_{1} F_{2}$ 互补,所以

$$
\cos \angle P F_{1} F_{2}+\cos \angle Q F_{1} F_{2}=0
$$

即

$$
\frac{36+36-(2 a-6)^{2}}{2 \times 6 \times 6}+\frac{16+36-(2 a-4)^{2}}{2 \times 4 \times 6}=0
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-015.jpg?height=340&width=345&top_left_y=1948&top_left_x=1524)

化简得

$$
5 a^{2}-24 a-45=0
$$

解得

$$
a=\frac{12+3 \sqrt{41}}{5}
$$

所以

$$
e=\frac{c}{a}=\frac{15}{12+3 \sqrt{41}}=\frac{\sqrt{41}-4}{5}
$$

思考与总结

本题的解题关键是如何处理条件“直线 $P Q$ 过点 $F_{1}$ ”, 即 $P, F_{1}, Q$ 三点共线. 因为本题已经用一个未知数表示出两个三角形的各条边的长度, 所以将表达三点共线转化成两个三角形中有一个内角互补, 从而利用余弦定理得到了等式.

## 第 528 题 圆中的解三角形

已知圆 $E:(x-2)^{2}+y^{2}=3$, 设直线 $l_{1}: x-m y-1=0$ 交圆 $E$ 于 $A, C$ 两点, 直线 $l_{2}: m x+y-m=0$交圆 $E$ 于 $B, D$ 两点. 线段 $A B, C D$ 分别位于 $x$ 轴的上方和下方. 当 $C D$ 的斜率为 -1 时, 求线段 $A B$ 的长.

解析 注意到直线 $l_{1}$ 与直线 $l_{2}$ 是过点 $F(1,0)$ 且互相垂直的两条直线. 在这样浓厚的几何色彩下, 我们选择利用三角知识解决问题.

如图, 取 $C D$ 的中点 $M$, 连结 $F M, E M, E C$. 由直线 $C D$ 的斜率为 -1 可得 $\angle F E M=45^{\circ}$, 在 $\triangle F E M$ 中应用余弦定理, 有

$$
F M^{2}=F E^{2}+E M^{2}-2 F E \cdot E M \cdot \cos 45^{\circ},
$$

又 $F M^{2}=E C^{2}-E M^{2}$, 代人数据可得

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-016.jpg?height=339&width=415&top_left_y=1225&top_left_x=1354)

$$
E M=\sqrt{2}, F M=1
$$

进而 $F M \perp F E$, 因此 $\angle F M D=45^{\circ}$, 于是 $\angle F C D=22.5^{\circ}$, 进而

$$
F C=2 \cos 22.5^{\circ}, F D=2 \sin 22.5^{\circ}
$$

根据圆幂定理, 有

$$
D F \cdot F B=C F \cdot F A=E C^{2}-E F^{2}=2,
$$

从而

$$
A B^{2}=A F^{2}+B F^{2}=\frac{1}{\cos ^{2} 22.5^{\circ}}+\frac{1}{\sin ^{2} 22.5^{\circ}}=\frac{4}{\sin ^{2} 45^{\circ}}=8
$$

因此线段 $A B$ 的长为 $2 \sqrt{2}$.

## 第 529 题 共焦点的椭圆与双曲线

已知 $F_{1}, F_{2}$ 是椭圆和双曲线的公共焦点, $P$ 是它们的一个公共点, 且 $\angle F_{1} P F_{2}=\frac{\pi}{3}$, 则椭圆和双曲线的离心率的倒数之和的最大值为

解析 $\frac{4 \sqrt{3}}{3}$.

解法一 不妨设椭圆与双曲线都是焦点在 $x$ 轴上的标准椭圆与标准双曲线, $P$ 为它们在第一象限内的
公共点, 并记椭圆的半长轴长、半短轴长、离心率分别为 $a_{1}, b_{1}, e_{1}$, 双曲线的半实轴长、半虚轴长、离心率分别为 $a_{2}, b_{2}, e_{2}$, 它们的半焦距长相等, 设为 $c$.

由题意知

$$
\left\{\begin{array}{l}
\left|P F_{1}\right|+\left|P F_{2}\right|=2 a_{1} \\
\left|P F_{1}\right|-\left|P F_{2}\right|=2 a_{2}
\end{array}\right.
$$

而题目中要求的是

$$
m=\frac{1}{e_{1}}+\frac{1}{e_{2}}=\frac{a_{1}}{c}+\frac{a_{2}}{c}=\frac{2\left|P F_{1}\right|}{\left|F_{1} F_{2}\right|}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-017.jpg?height=276&width=353&top_left_y=289&top_left_x=1510)

图 1

的最大值. 根据正弦定理, 可得

$$
\frac{a_{1}+a_{2}}{c}=\frac{2 \sin \angle P F_{2} F_{1}}{\sin \angle F_{1} P F_{2}}=\frac{4}{\sqrt{3}} \sin \angle P F_{2} F_{1} \leqslant \frac{4 \sqrt{3}}{3}
$$

当且仅当 $\angle P F_{2} F_{1}=\frac{\pi}{2}$ 时取到等号.

解法二 不妨设椭圆与双曲线都是焦点在 $x$ 轴上的标准椭圆与标准双曲线, $P$为它们在第一象限内的公共点, 并记椭圆的半长轴长、半短轴长、离心率分别为 $a_{1}$, $b_{1}, e_{1}$, 双曲线的半实轴长、半虚轴长、离心率分别为 $a_{2}, b_{2}, e_{2}$, 它们的半焦距长相等,设为 $c$.

由题意知

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-017.jpg?height=282&width=361&top_left_y=855&top_left_x=1503)

$$
\left\{\begin{array}{l}
\left|P F_{1}\right|+\left|P F_{2}\right|=2 a_{1} \\
\left|P F_{1}\right|-\left|P F_{2}\right|=2 a_{2}
\end{array}\right.
$$

解得

$$
\left\{\begin{array}{l}
\left|P F_{1}\right|=a_{1}+a_{2} \\
\left|P F_{2}\right|=a_{1}-a_{2}
\end{array}\right.
$$

在 $\triangle P F_{1} F_{2}$ 中应用余弦定理得

$$
\frac{1}{2}=\frac{\left(a_{1}+a_{2}\right)^{2}+\left(a_{1}-a_{2}\right)^{2}-4 c^{2}}{2\left(a_{1}+a_{2}\right)\left(a_{1}-a_{2}\right)}
$$

计算得

$$
a_{1}^{2}+3 a_{2}^{2}=4 c^{2}
$$

题目中要求的是 $\frac{1}{e_{1}}+\frac{1}{e_{2}}=\frac{a_{1}}{c}+\frac{a_{2}}{c}$ 的最大值.

设 $x=\frac{a_{1}}{c}, y=\frac{a_{2}}{c}$, 则本题转化为已知

$$
x^{2}+3 y^{2}=4, x>1,0<y<1
$$

求 $x+y$ 的最大值.

由柯西不等式得

$$
x+y=1 \cdot x+\frac{1}{\sqrt{3}} \cdot \sqrt{3} y \leqslant \sqrt{1+\frac{1}{3}} \cdot \sqrt{x^{2}+3 y^{2}}=\frac{4 \sqrt{3}}{3},
$$

当且仅当 $x=3 y=\sqrt{3}$ 时取到等号.

## 第 530 题 寻找“定值”

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-018.jpg?height=85&width=1553&top_left_y=455&top_left_x=172)
双曲线的左支交于 $A, B$ 两点, $A F_{2}, B F_{2}$ 分别交 $y$ 轴于 $P, Q$ 两点, 若 $\triangle P Q F_{2}$ 的周长为 12 , 求 $a b$ 取得最大值时双曲线的离心率 $e$.

解析 解法一 根据题意, $\triangle P Q F_{2}$ 的周长为 $\triangle A B F_{2}$ 的周长的一半, 因此 $\left|A F_{1}\right|+\left|A F_{2}\right|$ 为定值 12 ,也即

$$
\frac{2 b^{2}}{a}+2 a=12
$$

根据均值不等式, 有

$$
12=\frac{2 b^{2}}{a}+\frac{2 a}{3}+\frac{2 a}{3}+\frac{2 a}{3} \geqslant 4\left(\frac{16}{27} a^{2} b^{2}\right)^{\frac{1}{4}}
$$

等号当 $\frac{2 b^{2}}{a}=\frac{2 a}{3}$, 即 $a^{2}=3 b^{2}$ 时取得, 此时 $4 a^{2}=3 c^{2}$, 从而

$$
e^{2}=\frac{c^{2}}{a^{2}}=\frac{4}{3}
$$

因此 $e=\frac{2 \sqrt{3}}{3}$.

解法二 根据题意, $\triangle P Q F_{2}$ 的周长为 $\triangle A B F_{2}$ 的周长的一半, 因此 $\left|A F_{1}\right|+\left|A F_{2}\right|$ 为定值 12 , 也即

$$
\frac{b^{2}}{a}+a=6
$$

因为

$$
a^{2}-6 a+b^{2}=0,
$$

所以可以令 $a=3+3 \cos \theta, b=3 \sin \theta$, 得到

$$
\begin{aligned}
a b & =9(1+\cos \theta) \sin \theta \\
& =9 \sqrt{(1+\cos \theta)^{3} \cdot(3-3 \cos \theta) \cdot \frac{1}{3}} \\
& \leqslant 3 \sqrt{3} \cdot \sqrt{\left[\frac{3-3 \cos \theta+3(1+\cos \theta)}{4}\right]^{4}} \\
& =\frac{27}{4} \sqrt{3}
\end{aligned}
$$

当 $1+\cos \theta=3-3 \cos \theta$, 即 $\cos \theta=\frac{1}{2}$ 时取到等号, 此时 $a=\frac{9}{2}, b=\frac{3}{2} \sqrt{3}$, 所以 $e=\frac{2}{3} \sqrt{3}$.

## 第 531 题 内接三角形

已知抛物线 $y^{2}=4 x$ 的内接 $\triangle A B C$ 的重心恰好是抛物线的焦点,求 $\triangle A B C$ 面积的最大值.

解析 设 $A\left(a^{2}, 2 a\right), B\left(b^{2}, 2 b\right), C\left(c^{2}, 2 c\right)$, 则

$$
a^{2}+b^{2}+c^{2}=3, a+b+c=0
$$

于是

$$
a+b=-c, a b=c^{2}-\frac{3}{2},|a-b|=\sqrt{6-3 c^{2}}
$$

从而

$$
\begin{aligned}
S & =\left|\begin{array}{ccc}
1 & 1 & 1 \\
a^{2} & b^{2} & c^{2} \\
a & b & c
\end{array}\right| \\
& =\left|a^{2} b+b^{2} c+c^{2} a-a b^{2}-b c^{2}-c a^{2}\right| \\
& =\sqrt{6-3 c^{2}} \cdot\left|3 c^{2}-\frac{3}{2}\right| \\
& =\sqrt{\frac{1}{2}\left(12-6 c^{2}\right) \cdot\left(3 c^{2}-\frac{3}{2}\right) \cdot\left(3 c^{2}-\frac{3}{2}\right)} \\
& \leqslant \frac{3 \sqrt{6}}{2}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-019.jpg?height=304&width=321&top_left_y=347&top_left_x=1551)

等号当 $c^{2}=\frac{3}{2}$ 时取得, 因此 $\triangle A B C$ 面积的最大值为 $\frac{3 \sqrt{6}}{2}$.

## 第 532 题 几何极值的调整法

如图 1, 已知直线 $A B$ 过点 $M(2,1)$ 且与 $x$ 轴, $y$ 轴正半轴分别交于 $A, B$ 两点, $O$ 为坐标原点.

(1)求 $\triangle A O B$ 面积的最小值;

(2)求 $\triangle A O B$ 周长的最小值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-019.jpg?height=247&width=359&top_left_y=1204&top_left_x=1488)

图 1

解析 解法一 (1) 设 $\angle B A O=x$, 则

$$
\begin{aligned}
S_{\triangle A O B} & =\frac{1}{2} O A \cdot O B \\
& =\frac{1}{2}\left(2+\frac{1}{\tan x}\right)(1+2 \tan x) \\
& =2+2 \tan x+\frac{1}{2 \tan x} \\
& \geqslant 4
\end{aligned}
$$

等号当且仅当 $\tan x=\frac{1}{2}$ 时取得.

(2) 设 $\angle B A O=x$, 则

$$
c_{\triangle A O B}=3+\frac{1}{\sin x}+\frac{2}{\cos x}+\frac{1}{\tan x}+2 \tan x
$$

令 $\tan \frac{x}{2}=t, t \in(0,1)$, 则

$$
\begin{aligned}
c_{\triangle A O B} & =3+\frac{1+t^{2}}{2 t}+\frac{2\left(1+t^{2}\right)}{1-t^{2}}+\frac{1-t^{2}}{2 t}+\frac{4 t}{1-t^{2}} \\
& =1+\frac{1}{t}+\frac{4}{1-t} \\
& \geqslant 10
\end{aligned}
$$

这里用到了柯西不等式, 取得等号的条件是 $t=\frac{1}{3}$.

## 解法二

(1) 如图 2, 设直线 $A B$ 在第一象限内的线段被点 $M$ 平分时与 $x$ 轴, $y$ 轴的交点分别为 $P, Q$. 接下来证明此时 $\triangle A O B$ 的面积最小.

若不然, 假设 $A M<B M$, 则

$$
\begin{aligned}
S_{\triangle A O B} & =S_{\triangle P Q Q}-S_{\triangle M A P}+S_{\triangle M B Q} \\
& =S_{\triangle P Q Q}-\frac{1}{2} M P \cdot(A M-B M) \cdot \sin \angle A M P \\
& >S_{\triangle P Q Q},
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-020.jpg?height=277&width=355&top_left_y=198&top_left_x=1398)

图 2

当 $A M>B M$ 时类似.

因此当点 $M$ 平分 $A B$ 时, $\triangle A O B$ 的面积最小,最小值为 4 .

(2) 过点 $M$ 作圆 $E$ 与 $x$ 轴, $y$ 轴均相切, 作圆 $E$ 在点 $M$ 处的切线, 此时 $\triangle A O B$ 的周长最小, 为 $O P+$ $O Q$, 如图 3.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-020.jpg?height=312&width=358&top_left_y=829&top_left_x=417)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-020.jpg?height=312&width=352&top_left_y=829&top_left_x=1044)

图 4

若不然, $A B$ 为圆 $E$ 的割线, 此时可以作与该割线平行的切线, 则显然有 $\triangle A O B$ 的周长大于切线与两坐标轴围成的三角形的周长, 而切线与坐标轴围成的三角形周长为 $O P+O Q$, 故此时 $\triangle A O B$ 的周长大于 $O P+$ $O Q$, 如图 4.

经计算可得圆 $E:(x-5)^{2}+(y-5)^{2}=25, O P+O Q=10$, 于是 $\triangle A O B$ 周长的最小值为 10 .

解法三

(1) 设直线 $A B$ 的横截距和纵截距分别为 $\frac{1}{a}$ 和 $\frac{1}{b}$, 则 $2 a+b=1(a, b>0)$.

由于

$$
1=2 a+b \geqslant 2 \sqrt{2 a b}
$$

当 $a=\frac{1}{4}, b=\frac{1}{2}$ 时取到等号, 于是 $\triangle A O B$ 的面积 $\frac{1}{2 a b}$ 的最小值为 4 .

(2) $\triangle A O B$ 的周长为

$$
\frac{1}{a}+\frac{1}{b}+\sqrt{\frac{1}{a^{2}}+\frac{1}{b^{2}}}=\frac{a+b+\sqrt{a^{2}+b^{2}}}{a b}=\frac{2}{a+b-\sqrt{a^{2}+b^{2}}},
$$

而

$$
(3 a+4 b)^{2} \leqslant 25\left(a^{2}+b^{2}\right)
$$

于是

$$
\sqrt{a^{2}+b^{2}} \geqslant \frac{3}{5} a+\frac{4}{5} b
$$

因此

$$
a+b-\sqrt{a^{2}+b^{2}} \leqslant \frac{2 a+b}{5}=\frac{1}{5}
$$

从而 $\triangle A O B$ 的周长

$$
\frac{2}{a+b-\sqrt{a^{2}+b^{2}}} \geqslant 10
$$

等号当且仅当 $\frac{a}{b}=\frac{3}{4}$ 时取得.

## 第 533 题 雾里看花

已知 $P$ 为圆 $O_{1}:(x-a)^{2}+(y-b)^{2}=b^{2}+1$ 与圆 $O_{2}:(x-c)^{2}+(y-d)^{2}=d^{2}+1$ 的交点, 若 $a c=8$, $\frac{a}{b}=\frac{c}{d}$, 则点 $P$ 与直线 $l: 3 x-4 y-25=0$ 上的点 $Q$ 之间距离的最小值是

解析 2 .

设 $P(m, n), b=k a, d=k c$, 则

$$
P \in O_{1}:(m-a)^{2}+(n-k a)^{2}=k^{2} a^{2}+1
$$

即

$$
O_{1}: a^{2}-(2 m+2 k n) a+m^{2}+n^{2}-1=0
$$

类似地, 有

$$
P \in O_{2}: c^{2}-(2 m+2 k n) c+m^{2}+n^{2}-1=0,
$$

于是 $a, c$ 是关于 $t$ 的方程

$$
t^{2}-(2 m+2 k n) t+m^{2}+n^{2}-1=0
$$

的两个实根,于是

$$
c a=m^{2}+n^{2}-1
$$

从而点 $P$ 的轨迹方程为 $x^{2}+y^{2}=9$.

因此点 $P$ 到直线 $l: 3 x-4 y-25=0$ 的最小距离为 2 .

## 第 534 题 曲线间距离

设 $P$ 为曲线 $C_{1}$ 上的动点, $Q$ 为曲线 $C_{2}$ 上的动点, 则称 $|P Q|$ 的最小值为曲线 $C_{1}, C_{2}$ 之间的距离,记作 $d\left(C_{1}, C_{2}\right)$.

(1) 若

$$
C_{1}: x^{2}+y^{2}=2, C_{2}:(x-3)^{2}+(y-3)^{2}=2
$$

则 $d\left(C_{1}, C_{2}\right)=$ $\qquad$ ;

(2) 若

$$
C_{3}: \mathrm{e}^{x}-2 y=0, C_{4}: \ln x+\ln 2=y
$$

则 $d\left(C_{3}, C_{4}\right)=$ $\qquad$ .

解析 $\sqrt{2} ; \sqrt{2}-\sqrt{2} \ln 2$.

如图, 注意 $C_{3}$ 与 $C_{4}$ 的图象关于直线 $y=x$ 对称.

所以只需要求曲线 $C_{4}$ 上的点到直线 $y=x$ 的距离的最小值, $C_{4}$ 对应的函数为 $y=\ln x+\ln 2$, 所以斜率为 1 的切线方程对应的切点为 $(1, \ln 2)$, 从而切线为 $y=x-1+$ $\ln 2$, 它与 $y=x$ 的距离为

$$
d=\frac{1-\ln 2}{\sqrt{2}}
$$

从而

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-021.jpg?height=307&width=329&top_left_y=2145&top_left_x=1551)

$$
d\left(C_{3}, C_{4}\right)=2 \cdot \frac{1-\ln 2}{\sqrt{2}}=\sqrt{2}-\sqrt{2} \ln 2
$$

## 第 535 题 “ $L$ 距离”

在平面直角坐标系中,两点 $P_{1}\left(x_{1}, y_{1}\right), P_{2}\left(x_{2}, y_{2}\right)$ 间的“ $\mathrm{L}$ 一距离”定义为 ||$P_{1} P_{2}||=\left|x_{1}-x_{2}\right|+$ $\left|y_{1}-y_{2}\right|$,则平面内与 $x$ 轴上两个不同的定点 $F_{1}(-1,0), F_{2}(1,0)$ 的“L一距离”之和等于 5 的点的轨迹所围成的面积为 $\qquad$ .

解析 10 .

如图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-022.jpg?height=328&width=599&top_left_y=651&top_left_x=608)

可以看到, 题中轨迹的定义与椭圆的定义相仿, 得到的图形也与椭圆神似, 我们可以称之为 “ $L-$ 椭圆”.那么是否有“L一圆”,“L一双曲线”,“L一抛物线”等等其他“L一”图形呢?

答案是肯定的. “

L一圆”: 平面内到定点的“L一距离”为定值的点的轨迹.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-022.jpg?height=312&width=473&top_left_y=1285&top_left_x=671)

“ $L$-双曲线”: 平面内到两个定点的“ $L-$ 距离”之差的绝对值为定值 (小于 ||$F_{1} F_{2}||$ ) 的点的轨迹.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-022.jpg?height=317&width=547&top_left_y=1649&top_left_x=634)

“L-抛物线”: 平面内到定点的“ $L-$ 距离”与到定直线的“ $L-$ 距离”(即到直线上的点的“ $L-$ 距离”的最小值) 相等的点的轨迹.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-022.jpg?height=320&width=547&top_left_y=2060&top_left_x=634)
其实类似的还有“ $L-$ 线段”:平面内到两个定点的“ $L-$ 距离”之和为两个定点之间的“ $L-$ 距离”的点的轨迹.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-023.jpg?height=327&width=705&top_left_y=390&top_left_x=656)

“L一垂直平分线”: 平面内到两个定点的“L一距离”相等的点的轨迹.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-023.jpg?height=332&width=647&top_left_y=760&top_left_x=696)

## 第 536 题 反客为主

已知集合

$$
\begin{gathered}
A=\{(x, y) \mid x=n, y=n a+b, n \in \mathbf{Z}\} \\
B=\left\{(x, y) \mid x=m, y=3 m^{2}+12, m \in \mathbf{Z}\right\}
\end{gathered}
$$

若存在实数 $a, b$ 使得 $A \cap B \neq \varnothing$ 成立, 称点 $(a, b)$ 为 “ $\alpha$ ”点, 则 “ $\alpha$ ”点在平面区域

$$
C=\left\{(x, y) \mid x^{2}+y^{2} \leqslant 108\right\}
$$

内的个数是
A. 0
B. 1 个
C. 2 个
D. 无数个

解析 A.

解法一 根据题意, $A$ 与 $B$ 的交集即

$$
\left\{(x, y) \mid y=a x+b=3 x^{2}+12, x \in \mathbf{Z}\right\}
$$

于是 $A \cap B$ 是否为空集取决于关于 $x$ 的方程 $a x+b=3 x^{2}+12$ 是否存在整数解.

将 $x$ 看作参数, 需要考虑直线系 $x \cdot a+b-3 x^{2}-12=0$ 与圆 $a^{2}+b^{2}=108$ 的位置关系.

原点到直线的距离为

$$
\frac{3 x^{2}+12}{\sqrt{x^{2}+1}}=3 \sqrt{x^{2}+1}+\frac{9}{\sqrt{x^{2}+1}}>2 \sqrt{27}=\sqrt{108}
$$

其中考虑到 $x \in \mathbf{Z}$, 等号无法取到. 因此满足条件的点 $(a, b)$ 不存在.

解法二 本题也可以从代数角度考虑, 由方程 $a x+b=3 x^{2}+12$ 有解得到判别式 $\Delta \geqslant 0$, 即

$$
a^{2}+12 b-144 \geqslant 0,
$$

与不等式 $a^{2}+b^{2} \leqslant 108$ 结合可以得到

$$
a= \pm 6 \sqrt{2}, b=6 \text {. }
$$

此时方程 $a x+b=3 x^{2}+12$ 有唯一解, 但不是整数, 故 “ $\alpha$ ”点不存在.

## 第 537 题 数与形

如图 1, 在平面直角坐标系 $x O y$ 中, 圆 $C_{1}: x^{2}+y^{2}=4$, 圆 $C_{2}: x^{2}+y^{2}=16$, 点 $M(1,0)$, 动点 $P, Q$ 分别在圆 $C_{1}$ 和圆 $C_{2}$ 上, 满足 $M P \perp M Q$, 则线段 $P Q$ 的取值范围是 $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-024.jpg?height=320&width=331&top_left_y=448&top_left_x=1400)

图 1

解析 $[\sqrt{19}-1, \sqrt{19}+1]$.

解法一 注意到 $M P \perp M Q$, 于是可以利用直角三角形斜边上的中线等于斜边的一半来转移线段 $P Q$, 这样做的意义在于将两端都在动的线段 $P Q$ 转化成一端不动 $(M)$ 而另一端 $(E)$ 运动的线段 $M E$, 如图 2.

此时需要设法建立 $E$ 点与其他已知条件的联系. 连结 $O E, O P, O Q$, 我们可以发现共 $P Q$ 边的 $\triangle O P Q$ 和 $\triangle M P Q$, 而 $O E$ 和 $M E$ 分别是这两个三角形的中线, 如图 3.

此时根据中线长公式, 有

$$
O P^{2}+O Q^{2}=2 O E^{2}+\frac{1}{2} P Q^{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-024.jpg?height=320&width=312&top_left_y=894&top_left_x=1440)

图 2

也即

$$
2 O E^{2}+2 M E^{2}=20
$$

这样我们就得到了一个重要的不变量. 结合 $O M=1$, 由 $O E, M E, O M$ 的数量关系可得

$$
(M E-1)^{2} \leqslant O E^{2} \leqslant(M E+1)^{2},
$$

因此

$$
(M E-1)^{2}+M E^{2} \leqslant O E^{2}+M E^{2} \leqslant(M E+1)^{2}+M E^{2},
$$

即

$$
2 M E^{2}-2 M E+1 \leqslant 10 \leqslant 2 M E^{2}+2 M E+1,
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-024.jpg?height=405&width=400&top_left_y=1300&top_left_x=1352)

图 3

解得

$$
\frac{-1+\sqrt{19}}{2} \leqslant M E \leqslant \frac{1+\sqrt{19}}{2}
$$

从而 $P Q$ 也就是 $2 M E$ 的取值范围是 $[\sqrt{19}-1, \sqrt{19}+1]$.

事实上, 不变量可以再次利用中线长公式挖掘几何意义. 倍长 $M E$ 至点 $N$, 则

$$
O N^{2}+O M^{2}=2 O E^{2}+\frac{1}{2} M N^{2}=2 O E^{2}+2 M E^{2}=20
$$

于是 $O N$ 为定长 $\sqrt{19}$, 也就是说 $N$ 点的轨迹是以点 $O$ 为圆心的圆, 如图 4. 进而 $P Q$ 也就是 $M N$ 的取值范围是 $[\sqrt{19}-1, \sqrt{19}+1]$.

解法二 利用几何条件设参. 设 $M P=r_{1}, M Q=r_{2}, P\left(1+r_{1} \cos \theta, r_{1} \sin \theta\right)$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-024.jpg?height=392&width=392&top_left_y=1816&top_left_x=1359)

图 4 $Q\left(1+r_{2} \cos \left(\theta-\frac{\pi}{2}\right), r_{2} \sin \left(\theta-\frac{\pi}{2}\right)\right)$,

其中 $\theta \in \mathbf{R}$. 则

$$
P Q^{2}=r_{1}^{2}+r_{2}^{2}
$$

且

$$
\left\{\begin{array}{l}
\left(1+r_{1} \cos \theta\right)^{2}+\left(r_{1} \sin \theta\right)^{2}=4 \\
\left(1+r_{2} \sin \theta\right)^{2}+\left(-r_{2} \cos \theta\right)^{2}=16
\end{array}\right.
$$

化简条件组,得

$$
\left\{\begin{array}{l}
r_{1}^{2}+2 r_{1} \cos \theta-3=0 \\
r_{2}^{2}+2 r_{2} \sin \theta-15=0
\end{array}\right.
$$

观察式子的形状,两式相加得

$$
r_{1}^{2}+r_{2}^{2}+2 \sqrt{r_{1}^{2}+r_{2}^{2}} \sin (\theta+\varphi)-18=0
$$

其中 $\varphi$ 为辅助角. 因此

$$
\sin (\theta+\varphi)=\frac{18-P Q^{2}}{2 P Q} \in[-1,1]
$$

解得 $P Q$ 的取值范围是 $[\sqrt{19}-1, \sqrt{19}+1]$.

## 第 538 题 $\quad-$ 休两面

已知向量 $|\boldsymbol{a}|=|\boldsymbol{b}|=2,|\boldsymbol{c}|=1,(\boldsymbol{c}-\boldsymbol{a}) \cdot(\boldsymbol{c}-\boldsymbol{b})=0$, 则 $\boldsymbol{a} \cdot \boldsymbol{b}$ 的取值范围是

解析 $[-\sqrt{7}, \sqrt{7}]$.

解法一 设 $\boldsymbol{a}=\overrightarrow{O A}, \boldsymbol{b}=\overrightarrow{O B}, \boldsymbol{c}=\overrightarrow{O C}$, 于是条件 $(\boldsymbol{c}-\boldsymbol{a}) \cdot(\boldsymbol{c}-\boldsymbol{b})=0$ 即

$$
\overrightarrow{A C} \cdot \overrightarrow{B C}=0
$$

由题意知 $A, B$ 在以点 $O$ 为圆心, 2 为半径的圆上运动; $C$ 在以点 $O$ 为圆心, 1 为半径的圆上运动, 且有 $A C \perp B C$, 即点 $C$ 在以 $A B$ 为直径的圆上.

记 $A B$ 的中点为 $M$, 有

$$
\boldsymbol{a} \cdot \boldsymbol{b}=O M^{2}-\frac{1}{4} A B^{2}=4-\frac{1}{2} A B^{2}
$$

所以求 $\boldsymbol{a} \cdot \boldsymbol{b}$ 的范围, 只需要求出 $A B$ 的范围即可.

因为 $O M \perp A B$, 考虑点 $M$ 在大圆 $O$ (半径为 2 的圆) 的一条半径上运动, 过点 $M$ 作 $A B \perp O M$, 与大圆相交于 $A, B$ 两点, 再以点 $M$ 为圆心, $\frac{1}{2} A B$ 为半径作圆 $M$, 若圆 $M$ 与小圆 $O$ (半径为 1 的圆)有公共点, 则对应的 $A, B$ 满足要求.

于是得到两个临界情况, 图 1 是 $A B$ 取到最小值时的情况.

记 $r=\frac{1}{2} A B$, 在 $\triangle O A M$ 中, 有

$$
r^{2}+(r+1)^{2}=2^{2}
$$

解得

$$
r=\frac{\sqrt{7}-1}{2}
$$

图 2 是 $A B$ 取到最大值时的情况.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-025.jpg?height=310&width=307&top_left_y=1465&top_left_x=1554)

图1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-025.jpg?height=334&width=329&top_left_y=1858&top_left_x=1532)

图2

在 $\triangle O A M$ 中, 有

$$
r^{2}+(r-1)^{2}=2^{2}
$$

解得

$$
r=\frac{\sqrt{7}+1}{2}
$$

于是得到 $\boldsymbol{a} \cdot \boldsymbol{b}$ 的取值范围为 $[-\sqrt{7}, \sqrt{7}]$.

解法二 将条件 $(\boldsymbol{c}-\boldsymbol{a}) \cdot(\boldsymbol{c}-\boldsymbol{b})=0$ 整理得

$$
1-(\boldsymbol{a}+\boldsymbol{b}) \cdot \boldsymbol{c}+\boldsymbol{a} \cdot \boldsymbol{b}=0
$$

所以

$$
(\boldsymbol{a}+\boldsymbol{b}) \cdot \boldsymbol{c}=1+\boldsymbol{a} \cdot \boldsymbol{b}
$$

设 $\boldsymbol{a} \cdot \boldsymbol{b}=x, \theta=\langle\boldsymbol{a}+\boldsymbol{b}, \boldsymbol{c}\rangle$, 则

$$
|\boldsymbol{a}+\boldsymbol{b}|=\sqrt{(\boldsymbol{a}+\boldsymbol{b})^{2}}=\sqrt{8+2 x}
$$

所以

$$
\sqrt{8+2 x} \cdot 1 \cdot \cos \theta=1+x
$$

得到

$$
-1 \leqslant \frac{1+x}{\sqrt{8+2 x}} \leqslant 1
$$

即

$$
(1+x)^{2} \leqslant 8+2 x
$$

解得

$$
-\sqrt{7} \leqslant x \leqslant \sqrt{7}
$$

所以 $\boldsymbol{a} \cdot \boldsymbol{b}$ 的取值范围为 $[-\sqrt{7}, \sqrt{7}]$.

## 第 539 题 五仁月垪

已知植圆 $E: \frac{x^{2}}{2}+y^{2}=1$. 设 $A_{2}$ 为椭圆的右顶点.

(1) 如图 1, 过点 $A_{2}$ 且互相垂直的两条直线分别交椭圆 $E$ 于另两点 $A, B$, 直线 $A B$ 是否过定点? 请说明理由.

(2) 如图 2, 设直线 $l: x=2, F$ 为椭圆的右焦点, 过点 $F$ 的直线交椭圆 $E$ 于点 $P, Q$. 设 $G$ 为直线 $l$ 上的任意一点, 直线 $P G, F G, Q G$ 的斜率分别为 $k_{1}, k_{2}, k_{3}$, 求证: $k_{1}, k_{2}, k_{3}$ 成等差数列.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-026.jpg?height=221&width=287&top_left_y=1417&top_left_x=1417)

图1

(3) 如图 3, 设直线 $l: x=2, F$ 为椭圆的右焦点, 过点 $F$ 的直线交椭圆 $E$ 于点 $P, Q$. 设 $A_{1}$ 是椭圆的左顶点, 直线 $A_{1} P, A_{1} Q$ 分别与直线 $l$ 交于点 $M, N$, 求证: 直线 $F M$ 和直线 $F N$ 的斜率之积为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-026.jpg?height=236&width=312&top_left_y=1883&top_left_x=175)

图2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-026.jpg?height=260&width=312&top_left_y=1860&top_left_x=523)

图3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-026.jpg?height=323&width=312&top_left_y=1798&top_left_x=876)

图4

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-026.jpg?height=309&width=391&top_left_y=1811&top_left_x=1228)

图5

(4) 如图 4, 设直线 $l: x=2, F$ 为椭圆的右焦点, 过点 $F$ 的直线交椭圆 $E$ 于点 $P, Q$. 设 $H(2, \sqrt{7})$ 为直线 $l$ 上一点, 若向量 $\overrightarrow{H P}$ 与向量 $\overrightarrow{H Q}$ 的夹角为 $45^{\circ}$, 求直线 $P Q$ 的斜率.

(5) 如图 5, 设 $A_{3}$ 为椭圆的上顶点, 圆 $I:\left(x-\frac{2}{3}\right)^{2}+y^{2}=r^{2}$ 是椭圆 $E$ 的内接 $\triangle A_{1} B_{1} C_{1}$ 的内切圆,过 $A_{3}$ 作圆 $I$ 的两条切线分别交椭圆于点 $B_{3}, C_{3}$. 求 $r$ 的值并证明直线 $B_{3} C_{3}$ 与圆 $I$ 相切.

解析 (1) 设直线 $A_{2} A$ 的方程为 $x=m y+\sqrt{2}, A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 直线 $A B$ 交 $x$ 轴于点 $T(t, 0)$.联立直线 $A_{2} A$ 与椭圆 $E$ 的方程, 可得

$$
\left(m^{2}+2\right) y^{2}+2 \sqrt{2} m y=0
$$

于是

$$
y_{1}=\frac{-2 \sqrt{2} m}{m^{2}+2}
$$

类似地, 可得

$$
y_{2}=\frac{2 \sqrt{2} m}{2 m^{2}+1}
$$

于是由

$$
\frac{y_{1}-0}{x_{1}-t}=\frac{y_{2}-0}{x_{2}-t}
$$

可得

$$
\begin{aligned}
t & =\frac{x_{1} y_{2}-x_{2} y_{1}}{y_{2}-y_{1}} \\
& =\frac{\left(m y_{1}+\sqrt{2}\right) y_{2}-\left(-\frac{1}{m} y_{2}+\sqrt{2}\right) y_{1}}{y_{2}-y_{1}} \\
& =\frac{\left(m+\frac{1}{m}\right) \cdot y_{1} y_{2}}{y_{2}-y_{1}}+\sqrt{2} \\
& =\frac{\sqrt{2}}{3}
\end{aligned}
$$

为定值, 因此直线 $A B$ 恒过定点 $\left(\frac{\sqrt{2}}{3}, 0\right)$.

(2) 设直线 $P Q: x=m y+1, P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$, 则联立直线 $P Q$ 与椭圆 $E$ 的方程, 有

$$
\left(m^{2}+2\right) y^{2}+2 m y-1=0,
$$

于是

$$
y_{1}+y_{2}=-\frac{2 m}{m^{2}+2}, y_{1} y_{2}=-\frac{1}{m^{2}+2}
$$

设 $G(2, t)$, 则欲证明结论等价于

$$
\frac{t-y_{1}}{2-x_{1}}+\frac{t-y_{2}}{2-x_{2}}=2 t
$$

即

$$
\left(t-y_{1}\right)\left(1-m y_{2}\right)+\left(t-y_{2}\right)\left(1-m y_{1}\right)=2 t\left(1-m y_{1}\right)\left(1-m y_{2}\right)
$$

也即

$$
(t m-1)\left[\left(y_{1}+y_{2}\right)-2 m \cdot y_{1} y_{2}\right]=0
$$

事实上,由

$$
y_{1}+y_{2}=-\frac{2 m}{m^{2}+2}, y_{1} y_{2}=-\frac{1}{m^{2}+2}
$$

可得

$$
\left(y_{1}+y_{2}\right)-2 m \cdot y_{1} y_{2}=0
$$

因此原命题得证.

(3) 设直线 $P Q: x=m y+1, P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$, 则联立直线 $P Q$ 与椭圆 $E$ 的方程, 有

$$
\left(m^{2}+2\right) y^{2}+2 m y-1=0
$$

于是

$$
y_{1}+y_{2}=-\frac{2 m}{m^{2}+2}, y_{1} y_{2}=-\frac{1}{m^{2}+2}
$$

设点 $M, N$ 的纵坐标为 $y_{M}, y_{N}$,

则由

$$
\frac{y_{M}}{2+\sqrt{2}}=\frac{y_{1}}{x_{1}+\sqrt{2}}
$$

可得

$$
y_{M}=\frac{(2+\sqrt{2}) y_{1}}{x_{1}+\sqrt{2}}=\frac{(2+\sqrt{2}) y_{1}}{m y_{1}+1+\sqrt{2}} \text {, }
$$

类似地, 有

$$
y_{N}=\frac{(2+\sqrt{2}) y_{2}}{m y_{2}+1+\sqrt{2}}
$$

因此可得直线 $F M$ 与直线 $F N$ 的斜率之积

$$
\begin{aligned}
k_{F M} \cdot k_{F N} & =\frac{y_{M}-0}{2-1} \cdot \frac{y_{N}-0}{2-1} \\
& =\frac{(2+\sqrt{2})^{2} y_{1} y_{2}}{\left(m y_{1}+1+\sqrt{2}\right)\left(m y_{2}+1+\sqrt{2}\right)} \\
& =\frac{(2+\sqrt{2})^{2} \cdot y_{1} y_{2}}{m^{2} y_{1} y_{2}+(1+\sqrt{2}) m \cdot\left(y_{1}+y_{2}\right)+(1+\sqrt{2})^{2}} \\
& =-1
\end{aligned}
$$

为定值, 原命题得证.

(4) 设直线 $P Q: x=m y+1, P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$, 则联立直线 $P Q$ 与椭圆 $E$ 的方程,有

$$
\left(m^{2}+2\right) y^{2}+2 m y-1=0
$$

于是

$$
y_{1}+y_{2}=-\frac{2 m}{m^{2}+2}, y_{1} y_{2}=-\frac{1}{m^{2}+2}
$$

本题的背景为一般结论: 从准线上一点看椭圆的张角 $\theta$ 满足

$$
\tan \theta=\frac{2 e}{\left(1-e^{2}\right) \sqrt{1+m^{2}}}
$$

依此结论不难得到 $m$ 的值应该为 $-\sqrt{7}$.

利用到角公式直接计算

根据题意, 有

$$
\left|\frac{\frac{y_{1}-\sqrt{7}}{m y_{1}-1}-\frac{y_{2}-\sqrt{7}}{m y_{2}-1}}{1+\frac{y_{1}-\sqrt{7}}{m y_{1}-1} \cdot \frac{y_{2}-\sqrt{7}}{m y_{2}-1}}\right|=1
$$

即

$$
\left[\left(m y_{1}-1\right)\left(m y_{2}-1\right)+\left(y_{1}-\sqrt{7}\right)\left(y_{2}-\sqrt{7}\right)\right]^{2}=\left[\left(m y_{1}-1\right)\left(y_{2}-\sqrt{7}\right)-\left(m y_{2}-1\right)\left(y_{1}-\sqrt{7}\right)\right]^{2},
$$

整理得

$$
\left(9 m^{2}+2 \sqrt{7} m+15\right)^{2}=8\left(m^{2}+1\right)\left(7 m^{2}-2 \sqrt{7} m+1\right),
$$

令 $t=m+\sqrt{7}$, 则可整理得

$$
t^{2}\left(25 t^{2}-48 \sqrt{7} t+192\right)=0,
$$

因此 $m$ 的值为 $-\sqrt{7}$, 直线 $P Q$ 的斜率为 $-\frac{\sqrt{7}}{7}$.

利用到角公式结合第 (2) 小题结论计算

设直线 $H P, H Q$ 的斜率分别为 $k_{1}, k_{2}$, 则根据题意有

$$
\left|\frac{k_{1}-k_{2}}{1+k_{1} k_{2}}\right|=1
$$

即

$$
\left(k_{1}+k_{2}\right)^{2}-4 k_{1} k_{2}=\left(k_{1} k_{2}+1\right)^{2},
$$

根据第 $(2)$ 小题结论有

$$
k_{1}+k_{2}=2 \sqrt{7}
$$

由以上两个方程可得

$$
\left(k_{1} k_{2}\right)^{2}+6 \cdot k_{1} k_{2}-27=0,
$$

从而

$$
k_{1} k_{2}=3 \text { 或 } k_{1} k_{2}=-9 \text {, }
$$

显然 $k_{1}, k_{2}>0$, 因此 $k_{1} k_{2}=3$.

设过点 $H$ 的直线方程为

$$
y-\sqrt{7}=k(x-2),
$$

则根据等效判别式, 可得该直线与椭圆 $E$ 相切即

$$
2 k^{2}+1-(-2 k+\sqrt{7})^{2}=0
$$

即

$$
k^{2}-2 \sqrt{7} k+3=0
$$

因此 $k_{1}, k_{2}$ 是该方程的两个根, 也即直线 $H P, H Q$ 均为椭圆的切线, 而直线 $P Q$ 为点 $H$ 对应的极线

$$
x+\sqrt{7} y=1
$$

因此直线 $P Q$ 的斜率为 $-\frac{\sqrt{7}}{7}$.

(5) 设直线 $A_{1} C_{1}, B_{1} C_{1}$ 上的切点分别为 $J, K$, 连结 $I J$, 如图 6. 由对称性知 $B_{1} C_{1}$ 与 $x$ 轴垂直.设 $C_{1}(n+r, y)$, 其中 $n=\frac{2}{3}$, 则由

$$
\frac{I J}{A_{1} J}=\frac{C_{1} K}{A_{1} K}
$$

得

$$
\frac{r}{\sqrt{(\sqrt{2}+n)^{2}-r^{2}}}=\frac{y}{\sqrt{2}+n+r}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-029.jpg?height=303&width=369&top_left_y=1424&top_left_x=1487)

图 6

所以

$$
y=\frac{r \cdot \sqrt{(\sqrt{2}+n)+r}}{\sqrt{(\sqrt{2}+n)-r}}
$$

又由

$$
\frac{(n+r)^{2}}{2}+y^{2}=1
$$

得

$$
y=\frac{\sqrt{\sqrt{2}-(n+r)} \cdot \sqrt{\sqrt{2}+(n+r)}}{2}
$$

由以上两式得

$$
\frac{r}{\sqrt{(\sqrt{2}+n)-t}}=\frac{\sqrt{(\sqrt{2}-n)-r}}{\sqrt{2}}
$$

整理得

$$
r^{2}+2 \sqrt{2} r-2+n^{2}=0
$$

于是解得 $r=\frac{\sqrt{2}}{3}$.

如图 7, 设圆 $I$ 过点 $A_{3}$ 的切线为 $y=k x+1$, 即

$$
k x-y+1=0,
$$

则 $A_{3} B_{3}, A_{3} C_{3}$ 的斜率 $k_{1}, k_{2}$ 是方程

$$
\frac{\left|\frac{2}{3} k+1\right|}{\sqrt{1+k^{2}}}=\frac{\sqrt{2}}{3}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-030.jpg?height=307&width=359&top_left_y=193&top_left_x=1391)

图 7

即

$$
2 k^{2}+12 k+7=0
$$

的根, 于是

$$
k_{1}+k_{2}=-6, k_{1} k_{2}=\frac{7}{2}
$$

两切线方程为

$$
\left(y-k_{1} x-1\right)\left(y-k_{2} x-1\right)=0,
$$

即

$$
(y-1)^{2}-x(y-1)\left(k_{1}+k_{2}\right)+k_{1} k_{2} x^{2}=0,
$$

也即

$$
-\frac{7}{2} x^{2}=(y-1)(y-1+6 x)
$$

将椭圆方程变形为

$$
-\frac{x^{2}}{2}=(y-1)(y+1)
$$

将以上两式联立 (即相除) 得直线 $B_{3} C_{3}$ 的方程

$$
7=\frac{y-1+6 x}{y+1}
$$

即

$$
3 x-3 y-4=0,
$$

因此圆心 $I\left(\frac{2}{3}, 0\right)$ 到直线 $B_{3} C_{3}$ 的距离

$$
d=\frac{\left|3 \times \frac{2}{3}-4\right|}{\sqrt{3^{2}+(-3)^{2}}}=\frac{\sqrt{2}}{3}
$$

与半径 $r$ 相等, 因此直线 $B_{3} C_{3}$ 与圆 $I$ 相切, 命题得证.

这个连环解析几何试题是训练解析几何解题能力的绝佳练习材料. 解决这些问题无需花哨的技巧, 只需要潜心运算, 可以在提高解题能力的同时修身养性,达到一举两得的效果.

## 第 540 题 大胆推测小山求证

如图, 已知椭圆 $\frac{x^{2}}{4}+y^{2}=1$ 的上顶点为 $A$, 过点 $A$ 作圆 $M:(x+1)^{2}$ $+y^{2}=r^{2}(0<r<1)$ 的两条切线分别与椭圆 $C$ 相交于点 $B, D$ (不同于点 $A$ ). 当 $r$ 变化时, 试问直线 $B D$ 是否过某个定点? 若是, 求出该定点; 若不是, 请说明理由.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-031.jpg?height=351&width=485&top_left_y=432&top_left_x=1334)

解析 设直线 $A B: y=k x+1$, 则有

$$
\frac{|k-1|}{\sqrt{1+k^{2}}}=r
$$

于是

$$
\left(1-r^{2}\right) k^{2}-2 k+1-r^{2}=0,
$$

于是可得直线 $A D$ 的斜率为 $\frac{1}{k}$. 联立直线 $A B$ 与椭圆的方程, 可得

$$
\left(4 k^{2}+1\right) x^{2}+8 k x=0,
$$

于是可得

$$
B\left(\frac{-8 k}{4 k^{2}+1}, \frac{-4 k^{2}+1}{4 k^{2}+1}\right), D\left(\frac{-8 k}{4+k^{2}}, \frac{-4+k^{2}}{4+k^{2}}\right)
$$

考虑到当 $r \rightarrow 1$ 时, $D$ 趋于椭圆的下顶点, $B$ 趋于椭圆的上顶点, 因此猜想定点若存在, 则必然在 $y$ 轴上,因此计算直线 $B D$ 的纵截距, 为

$$
\frac{\frac{-4 k^{2}+1}{4 k^{2}+1} \cdot\left(\frac{-8 k}{4+k^{2}}\right)+\frac{8 k}{4 k^{2}+1} \cdot \frac{-4+k^{2}}{4+k^{2}}}{\frac{-8 k}{4+k^{2}}+\frac{8 k}{4 k^{2}+1}}=-\frac{5}{3}
$$

因此直线 $B D$ 过定点 $\left(0,-\frac{5}{3}\right)$.

## 第 541 题 兵分两路

如图 1, 已知直线 $l: x=t$ 与椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 相交于 $A$, $B$ 两点, $M$ 是椭圆 $C$ 上一点, 设直线 $M A, M B$ 分别与 $x$ 轴交于 $E, F$ 两点, $O$ 为坐标原点, 求证: $|O E| \cdot|O F|$ 为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-031.jpg?height=269&width=460&top_left_y=2028&top_left_x=1358)

图 1

## 解析 解法一

设 $A(t, s), B(t,-s), M(m, n)$, 则

$$
\frac{t^{2}}{a^{2}}+\frac{s^{2}}{b^{2}}=\frac{m^{2}}{a^{2}}+\frac{n^{2}}{b^{2}}=1
$$

且

$$
|O E| \cdot|O F|=\left|\frac{t n-m s}{n-s} \cdot \frac{t n-m(-s)}{n-(-s)}\right|=\left|\frac{t^{2} n^{2}-m^{2} s^{2}}{n^{2}-s^{2}}\right|
$$

将 $t^{2}=a^{2}-\frac{a^{2}}{b^{2}} s^{2}, m^{2}=a^{2}-\frac{a^{2}}{b^{2}}{ }^{2}$ 代人, 可得 $|O E| \cdot|O F|=a^{2}$ 为定值.

解法二 利用仿射变换 $x^{\prime}=x, y^{\prime}=\frac{a}{b} y$ 将椭圆 $C$ 变为圆 $C^{\prime}: x^{\prime 2}+y^{\prime 2}=$ $a^{2}$, 如图 2.

由于 $\angle O M B=\angle O B M=\angle O A F$, 于是 $O, M, F, A$ 四点共圆, 进而有

$$
\angle O M A=\angle A F O=\angle M F O
$$

因此 $\triangle O M E$ 与 $\triangle O F M$ 相似,进而

$$
|O E| \cdot|O F|=|O M|^{2}=a^{2}
$$

为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-032.jpg?height=385&width=460&top_left_y=423&top_left_x=1291)

图 2

特别的, 对 $\triangle M A B$ 应用梅涅劳斯定理, 可得 $\frac{M E}{E A}=\frac{M F}{F B}$.

## 第 542 题 相关直线处理

已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的右顶点为 $P$, 过点 $P$ 作互相垂直的两条直线, 分别与椭圆 $E$ 交于不同于 $P$ 点的 $A, B$ 两点,求证:直线 $A B$ 恒过定点.

解析 设过点 $P$ 且互相垂直的两条直线的方程分别为 $x=m y+a$ 和 $x=-\frac{1}{m} y+a, A\left(x_{1}, y_{1}\right), B\left(x_{2}\right.$, $\left.y_{2}\right)$. 联立直线 $x=m y+a$ 与椭圆 $E$ 的方程, 可得

$$
\left(\frac{m^{2}}{a^{2}}+\frac{1}{b^{2}}\right) y^{2}+\frac{2 m}{a} y=0
$$

于是

$$
y_{1}=-\frac{2 m}{a\left(\frac{m^{2}}{a^{2}}+\frac{1}{b^{2}}\right)},
$$

因此直线 $A B$ 的横截距为

$$
\begin{aligned}
\frac{x_{1} y_{2}-x_{2} y_{1}}{y_{2}-y_{1}} & =\frac{\left(m y_{1}+a\right) y_{2}-\left(-\frac{1}{m} y_{2}+a\right) y_{1}}{y_{2}-y_{1}} \\
& =\frac{\left(m+\frac{1}{m}\right) y_{1} y_{2}}{y_{2}-y_{1}}+a \\
& =\frac{\frac{1}{a}\left(m+\frac{1}{m}\right) \cdot(-2 m) \cdot \frac{2}{m}}{\frac{2}{m}\left(\frac{m^{2}}{a^{2}}+\frac{1}{b^{2}}\right)+2 m\left(\frac{1}{m^{2} a^{2}}+\frac{1}{b^{2}}\right)}+a \\
& =\frac{a^{2}-b^{2}}{a^{2}+b^{2}} \cdot a
\end{aligned}
$$

为定值, 因此直线 $A B$ 恒过定点 $\left(\frac{a^{2}-b^{2}}{a^{2}+b^{2}} \cdot a, 0\right)$.

## 第 543 题 各有千秋

已知 $P$ 是单位圆 $O$ 上一点, $A(1,0), B(0,1)$, 直线 $P A$ 与 $y$ 轴交于点 $M$, 直线 $P B$ 与 $x$ 轴交于点 $N$, 求证: $A N \cdot B M$ 为定值.

## 解析 解法一

设 $P(\cos \theta, \sin \theta)$, 则根据截距坐标公式, 可得点 $N$ 的横坐标 $x_{N}$ 和点 $M$ 的纵坐标 $y_{M}$ 分别为

$$
x_{N}=\frac{\cos \theta}{1-\sin \theta}, y_{M}=\frac{\sin \theta}{1-\cos \theta}
$$

因此

$$
A N \cdot B M=\left(1-\frac{\cos \theta}{1-\sin \theta}\right) \cdot\left(1-\frac{\sin \theta}{1-\cos \theta}\right)=2
$$

为定值.

解法二 以 $P$ 点在第三象限为例, 如图, 连结 $A B, M N$.

设 $\angle P B M=\theta$, 则

$$
\angle A M B=\angle A B N=45^{\circ}+\theta, \angle B A M=90^{\circ}-\theta=\angle A N B .
$$

于是

$$
\frac{A N}{\sin \angle A B N}=\frac{A B}{\sin \angle A N B}, \frac{B M}{\sin \angle B A M}=\frac{A B}{\sin \angle A M B},
$$

于是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-033.jpg?height=364&width=351&top_left_y=1115&top_left_x=1510)

$$
A N \cdot B M=A B^{2} \cdot \frac{\sin \angle A B N}{\sin \angle A N B} \cdot \frac{\sin \angle B A M}{\sin \angle A M B}=A B^{2}=2
$$

事实上,由于

$$
\angle A B N=\angle A M B, \angle N A B=\angle M B A
$$

所以 $\triangle A B N$ 与 $\triangle B M A$ 相似,故

$$
\frac{A N}{B A}=\frac{A B}{B M}
$$

从而 $A N \cdot B M=A B^{2}=2$, 为定值.

## 第 544 题 用解䉼办法解平几问题

已知矩形 $A B C D, A B=\sqrt{2} C D$, 以 $C D$ 为直径向矩形外作半圆, 设 $P$ 为半圆上任意一点, 直线 $P A, P B$ 分别与 $C D$ 相交于点 $M, N$, 求证: $C D^{2}=C M^{2}+D N^{2}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-033.jpg?height=293&width=271&top_left_y=2163&top_left_x=1550)

图 1
解析 如图 2, 以 $C D$ 的中点为原点, $D C$ 为 $x$ 轴方向建立平面直角坐标系, 不妨设 $A B=2$.

设 $P(\cos \theta, \sin \theta), A(-1,-\sqrt{2}), B(1,-\sqrt{2}), C(1,0), D(-1,0)$, 于是根据截距坐标公式, $M, N$ 的横坐标分别为

$$
\begin{aligned}
& x_{M}=\frac{\cos \theta \cdot(-\sqrt{2})-(-1) \cdot \sin \theta}{-\sqrt{2}-\sin \theta}=\frac{-\sin \theta+\sqrt{2} \cos \theta}{\sqrt{2}+\sin \theta} \\
& x_{N}=\frac{\cos \theta \cdot(-\sqrt{2})-1 \cdot \sin \theta}{-\sqrt{2}-\sin \theta}=\frac{\sin \theta+\sqrt{2} \cos \theta}{\sqrt{2}+\sin \theta}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-034.jpg?height=293&width=309&top_left_y=212&top_left_x=1422)

图 2

于是

$$
\begin{aligned}
C M^{2}+D N^{2} & =\left(1-x_{M}\right)^{2}+\left[x_{N}-(-1)\right]^{2} \\
& =\frac{(\sqrt{2}+2 \sin \theta-\sqrt{2} \cos \theta)^{2}+(\sqrt{2}+2 \sin \theta+\sqrt{2} \cos \theta)^{2}}{(\sqrt{2}+\sin \theta)^{2}} \\
& =4=C D^{2}, \quad
\end{aligned}
$$

因此原命题得证.

## 第 545 题 形影不离

已知过点 $P\left(1, \frac{1}{4}\right)$ 的直线 $l_{1}, l_{2}$ 分别与椭圆 $\frac{x^{2}}{4}+y^{2}=1$ 相交于点 $A, C$与点 $B, D$, 且 $\overrightarrow{A P}=2 \overrightarrow{P C}, \overrightarrow{B P}=2 \overrightarrow{P D}$, 求直线 $A B$ 的方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-034.jpg?height=318&width=438&top_left_y=1209&top_left_x=1289)

解析 设 $A\left(x_{1}, y_{1}\right), C\left(x_{2}, y_{2}\right)$, 则

$$
\left\{\begin{array}{l}
x_{2}=\frac{3 \cdot 1-x_{1}}{2} \\
y_{2}=\frac{3 \cdot \frac{1}{4}-y_{1}}{2}
\end{array}\right.
$$

于是

$$
\frac{\left(\frac{3-x_{1}}{2}\right)^{2}}{4}+\left(\frac{\frac{3}{4}-y_{1}}{2}\right)^{2}=1
$$

即

$$
\frac{x_{1}^{2}}{4}+y_{1}^{2}-\frac{3}{2} x_{1}-\frac{3}{2} y_{1}-\frac{19}{16}=0
$$

也即

$$
x_{1}+y_{1}+\frac{1}{8}=0
$$

类似的, 点 $B\left(x_{3}, y_{3}\right)$ 的坐标也满足

$$
x_{3}+y_{3}+\frac{1}{8}=0
$$

因此直线 $A B$ 的方程为

$$
x+y+\frac{1}{8}=0
$$

当然, 用同样的方法, 可以求出直线 $C D$ 的方程为

$$
x+y-\frac{31}{16}=0
$$

## 第 546 题 定性与定量

在平面直角坐标系中, 过点 $P(a, b)(a \neq 0, b \neq 0)$ 的直线 $l$ 与两坐标轴围成的三角形面积是定值 $M$,则这样的直线可能有条.

解析 $2,3,4$.

设直线 $l$ 的斜率为 $k, k \neq 0$ 且 $k \neq \frac{b}{a}$, 直线 $l$ 与两坐标轴围成的三角形面积为 $S(k)$.

定性分析 不妨设 $a, b>0$. 如图 1 所示, 当 $k \in(-\infty, 0)$ 时, $S(k)$ 先从正无穷大单调递减, 当 $P$ 为直线 $l$ 被两坐标轴所截得的线段的中点时取得最小值, 再单调递增到正无穷大; 当 $k \in\left(0, \frac{b}{a}\right)$ 时, $S(k)$ 从正无穷大单调递减到 0 ; 当 $k \in$ $\left(\frac{b}{a},+\infty\right)$ 时, $S(k)$ 从 0 单调递增到正无穷大. 因此不同的 $M(M>0)$ 所对应的 $k$的值可能为 $2,3,4$ 个, 进而这样的直线可能有 $2,3,4$ 条.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-035.jpg?height=320&width=400&top_left_y=1027&top_left_x=1463)

图 1

定量计算 直线 $l: y=k(x-a)+b$, 于是直线 $l$ 与两坐标轴围成的三角形面积

$$
\begin{aligned}
S(k) & =\frac{1}{2}\left|-\frac{b}{k}+a\right| \cdot|-a k+b| \\
& =\frac{1}{2}\left|a^{2} k+\frac{b^{2}}{k}-2 a b\right| \\
& =\frac{1}{2}\left[a^{2}|k|+\frac{b^{2}}{|k|}-2 a b \cdot \frac{k}{|k|}\right]
\end{aligned}
$$

因此 $S(k)$ 的函数图象如图 2 , 不同的 $M(M>0)$ 所对应的 $k$ 的值可能为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-035.jpg?height=300&width=468&top_left_y=1494&top_left_x=1396)

图 2 $2,3,4$ 个, 因此这样的直线可能有 $2,3,4$ 条.

## 第 547 题 等分点

过点 $M(2,1)$ 的直线交椭圆 $\frac{x^{2}}{16}+\frac{y^{2}}{4}=1$ 于 $A, B$ 两点, 使 $M$ 是弦 $A B$ 的一个三等分点,求此直线的斜率.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-035.jpg?height=271&width=427&top_left_y=2157&top_left_x=1414)

解析 容易验证当 $A B$ 的斜率不存在时, 不符合题意. 当直线 $A B$ 的斜率为 $k$ 时, 设直线 $A B$ 的方程为

$$
\left\{\begin{array}{l}
x=2+t \\
y=1+k t
\end{array}\right.
$$

其中 $t$ 为参数.

与椭圆方程联立得

$$
\frac{(2+t)^{2}}{16}+\frac{(1+k t)^{2}}{4}=1
$$

即

$$
\left(4 k^{2}+1\right) t^{2}+(8 k+4) t-8=0
$$

设此方程的两根为 $t_{1}, t_{2}$, 分别对应点 $A, B$, 有

$$
\frac{t_{1}}{t_{2}}=-2,
$$

因为 $t_{1}, t_{2}$ 为方程(1)的两根, 由两根比的公式有

$$
(8 k+4)^{2}=\left(-2-\frac{1}{2}+2\right)\left(4 k^{2}+1\right) \cdot(-8)
$$

化简得 $12 k^{2}+16 k+3=0$, 解得

$$
k=\frac{-4 \pm \sqrt{7}}{6}
$$

## 第 548 题 直线的参数方程

设 $P, Q$ 是抛物线 $C: y^{2}=2 p x(p>0)$ 上的不同两点,抛物线 $C$ 在点 $P$, $Q$ 处的切线交于点 $M$. 过点 $M$ 作直线 $l$ 与抛物线交于点 $A, B$, 与直线 $P Q$交于点 $K$, 求证: $\frac{M K}{M A}+\frac{M K}{M B}$ 为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-036.jpg?height=342&width=432&top_left_y=1376&top_left_x=1282)

解析 所求结论涉及的线段都位于同一条直线上,因此可以考虑利用直线的参数方程简化问题.

设 $M\left(x_{0}, y_{0}\right)$, 则直线 $P Q: y_{0} y=p\left(x+x_{0}\right)$. 设直线 $l$ 的方程为

$$
\left\{\begin{array}{l}
x=x_{0}+t \\
y=y_{0}+k t
\end{array}\right.
$$

点 $A, B, K$ 对应的参数分别为 $t_{1}, t_{2}, t_{0}$, 则

$$
\frac{M K}{M A}+\frac{M K}{M B}=\frac{t_{0}}{t_{1}}+\frac{t_{0}}{t_{2}}=t_{0} \cdot \frac{t_{1}+t_{2}}{t_{1} t_{2}}
$$

联立直线 $l$ 与抛物线 $y^{2}=2 p x$ 的方程, 整理得

$$
k^{2} t^{2}+\left(2 k y_{0}-2 p\right) t+y_{0}^{2}-2 p x_{0}=0,
$$

联立直线 $l$ 与直线 $P Q$ 的方程, 可得

$$
y_{0}^{2}+k y_{0} t=p\left(2 x_{0}+t\right),
$$

从而

$$
t_{0} \cdot \frac{t_{1}+t_{2}}{t_{1} t_{2}}=\frac{y_{0}^{2}-2 p x_{0}}{p-k y_{0}} \cdot \frac{2 p-2 k y_{0}}{y_{0}^{2}-2 p x_{0}}=2
$$

为定值. 因此原命题得证.

## 第 549 题 直线参数方程的应用

已知椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$, 过椭圆左顶点 $A(-a, 0)$ 的直线 $l$ 与椭圆交于点 $Q$, 与 $y$ 轴交于点 $R$, 过原点与 $l$ 平行的直线交椭圆于点 $P$. 求证: $A Q, \sqrt{2} O P, A R$ 成等比数列.

解析 如图, 设过原点与 $l$ 平行的直线为 $l^{\prime}, l$ 的斜率为 $k$,则取 $(1, k)$ 为直线 $l$ 与 $l^{\prime}$ 共同的方向向量, 则直线 $l$ 与 $l^{\prime}$ 的参数方程为

$$
\left\{\begin{array}{l}
x=-a+t \\
y=k t
\end{array}\right.
$$

与

$$
\left\{\begin{array}{l}
x=t \\
y=k t
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-037.jpg?height=309&width=359&top_left_y=651&top_left_x=1506)

欲证结论为 $\left(\sqrt{2} t_{P}\right)^{2}=t_{Q} \cdot t_{R}$, 即

$$
2 t_{P}^{2}=t_{R} t_{Q},
$$

因为点 $R$ 的横坐标为 0 , 于是 $t_{R}=a$; 联立直线 $l$ 的参数方程与椭圆方程, 有

$$
\frac{(t-a)^{2}}{a^{2}}+\frac{k^{2} t^{2}}{b^{2}}=1,
$$

解得

$$
t_{Q}=\frac{2}{\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}} \cdot \frac{1}{a}
$$

联立直线 $l^{\prime}$ 的参数方程与椭圆方程, 有

$$
\frac{t^{2}}{a^{2}}+\frac{k^{2} t^{2}}{b^{2}}=1
$$

于是

$$
t_{P}^{2}=\frac{1}{\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}}
$$

显然, $2 t_{P}^{2}=t_{Q} \cdot t_{R}$ 成立,于是命题得证.

## 第 550 题 三角形的欧拉线

已知 $\triangle A B C$ 的顶点 $A(-2,0), B(0,4)$, 欧拉线所在的直线方程为 $l: x+y-2=0$, 则顶点 $C$ 的坐标是 $\qquad$ .

解析 $(4,0)$.

如图, $A B$ 的中点记为 $M(-1,2)$, 于是线段 $A B$ 的垂直平分线方程

$$
O M: y=-\frac{1}{2} x+\frac{3}{2},
$$

与欧拉线 $l$ 的方程联立可得外心 $O(1,1)$.

设顶点 $C(m, n)$, 则由 $2 \overrightarrow{O G}=\overrightarrow{G H}$ 可得

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-037.jpg?height=339&width=447&top_left_y=2272&top_left_x=1415)

$$
\overrightarrow{C H}=2 \overrightarrow{O M}=(-4,2)
$$

于是垂心 $H(m-4, n+2)$. 垂心 $H$ 的坐标满足欧拉线 $l$ 的方程, 因此

$$
m+n=4
$$

同时 $A H \perp B C$, 于是

$$
(m-2, n+2) \cdot(m, n-4)=0
$$

即

$$
m^{2}-2 m+n^{2}-2 n-8=0 \text {. }
$$

由以上两个方程解得 $m=4$ 且 $n=0$, 于是顶点 $C$ 的坐标为 $(4,0)$.

在 $\triangle A B C$ 中, 若 $H$ 为垂心, $O$ 为外心, $M$ 为边 $A B$ 的中点, 那么有 $\overrightarrow{C H}=2 \overrightarrow{O M}$. 进一步, 作 $B A$ 的垂线 $A N$ 交 $\triangle A B C$ 的外接圆于点 $N$, 则 $\overrightarrow{C H}=\overrightarrow{N A}$.

## 第 551 题 射影的位置

已知实数 $a, b, c$ 成等差数列 $(a, b$ 不全为 0$)$, 点 $A(0,-3)$ 在直线 $a x+b y+c=0$ 上的射影为 $M$, 点 $N(2,3)$, 则 $|M N|$ 的最大值为

解析 $\frac{\sqrt{130}+\sqrt{2}}{2}$.

解法一 设 $M(x, y)$, 则

$$
\left\{\begin{array}{l}
\overrightarrow{A M} / /(a, b) \\
a x+b y+c=0
\end{array}\right.
$$

即

$$
\left\{\begin{array}{l}
b x-a y=3 a \\
a x+b y=a-2 b
\end{array}\right.
$$

解得

$$
\left\{\begin{array}{l}
x=\frac{a^{2}+a b}{a^{2}+b^{2}} \\
y=\frac{-3 a^{2}+a b-2 b^{2}}{a^{2}+b^{2}}
\end{array}\right.
$$

不妨设 $a=r \sin \theta, b=r \cos \theta$, 其中 $r \neq 0$, 则有

$$
\left\{\begin{array}{l}
x=\frac{1-\cos 2 \theta}{2}+\frac{1}{2} \sin 2 \theta \\
y=-\frac{3(1-\cos 2 \theta)}{2}-(1+\cos 2 \theta)+\frac{1}{2} \sin 2 \theta
\end{array}\right.
$$

整理得

$$
\left\{\begin{array}{l}
x-\frac{1}{2}=\frac{1}{2} \sin 2 \theta-\frac{1}{2} \cos 2 \theta \\
y+\frac{5}{2}=\frac{1}{2} \cos 2 \theta+\frac{1}{2} \sin 2 \theta
\end{array}\right.
$$

这样就有

$$
\left(x-\frac{1}{2}\right)^{2}+\left(y+\frac{5}{2}\right)^{2}=\frac{1}{2}
$$

进而可得 $|M N|$ 的最大值为

$$
\sqrt{\left(2-\frac{1}{2}\right)^{2}+\left(3+\frac{5}{2}\right)^{2}}+\sqrt{\frac{1}{2}}=\frac{\sqrt{130}+\sqrt{2}}{2}
$$

解法二 由于 $2 b=a+c$, 于是直线恒过点 $T(1,-2)$, 注意到 $A M \perp T M$, 于是点 $M$ 在以 $A T$ 为直径的圆上. 圆心坐标为 $B\left(\frac{1}{2},-\frac{5}{2}\right)$, 半径为 $r=\frac{1}{2}|A T|=\frac{\sqrt{2}}{2}$. 于是 $|M N|$ 的最大值为

$$
|B N|+r=\sqrt{\left(2-\frac{1}{2}\right)^{2}+\left(3+\frac{5}{2}\right)^{2}}+\sqrt{\frac{1}{2}}=\frac{\sqrt{130}+\sqrt{2}}{2}
$$

## 第 552 题 层层递进

在平面直角坐标系 $x O y$ 中, 点 $A, B, C$ 的坐标分别为 $(a, 0),(0, a),(3,4)$, 点 $P(x, y)$ 是平面内的任意一点, 记 $M(a)=\max \{|P A|,|P B|,|P C|\}$, 则 $M(a)$ 的最小值是

解析 $7-2 \sqrt{6}$.

当 $A, B, C$ 三点构成锐角三角形或直角三角形时, $M(a)$ 的最小值为 $\triangle A B C$ 的外接圆半径. 当 $A, B, C$ 三点构成针角三角形或共线时, $M(a)$ 的最小值为 $\frac{1}{2} \max \{|A B|,|B C|,|C A|\}$.

注意, 外接圆半径 $r \geqslant \frac{1}{2} \max \{|A B|,|B C|,|C A|\}$.

回到本题 因为 $\overrightarrow{B C} \cdot \overrightarrow{B A}=a^{2}-a$, 所以下面根据 $a$ 的大小进行分类:

情形一 $a \in[0,1]$. 此时角 $B$ 为针角或直角, 所以

$$
M(a) \geqslant \frac{1}{2}|A C| \geqslant \frac{1}{2} \sqrt{2^{2}+4^{2}}=\sqrt{5}
$$

情形二 $a \in(1,3]$. 此时设外心坐标 $D(m, m)$, 如图,则由线段 $A C$ 的垂直平分线方程

$$
y=\frac{a-3}{4}\left(x-\frac{a+3}{2}\right)+2
$$

可得

$$
m=\frac{25-a^{2}}{14-2 a}=7-\left(\frac{7-a}{2}+\frac{12}{7-a}\right) \leqslant 7-2 \sqrt{6}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-039.jpg?height=326&width=316&top_left_y=1493&top_left_x=1550)

等号当且仅当 $a=7-2 \sqrt{6}$ 时取得.

此时 $\triangle A B C$ 外接圆的半径最小, 为 $7-2 \sqrt{6}$.

情形三 $a \in(3,+\infty)$. 此时

$$
M(a) \geqslant \frac{1}{2}|A B|>\frac{3 \sqrt{2}}{2}>7-2 \sqrt{6}
$$

情形四 $a \in(-\infty, 0)$. 此时

$$
M(a) \geqslant \frac{1}{2}|A C|>\frac{5}{2}>7-2 \sqrt{6}
$$

因为 $\sqrt{5}>7-2 \sqrt{6}$, 所以 $M(a)$ 的最小值为 $7-2 \sqrt{6}$.

## 第 553 题 等张角线

已知侑圆 $\frac{x^{2}}{16}+\frac{y^{2}}{4}=1$ 的左右焦点分别为 $F_{1}, F_{2}$, 点 $P$ 在直线 $l: x-\sqrt{3} y+8+2 \sqrt{3}=0$ 上, 当 $\angle F_{1} P F_{2}$ 取最大值时, $\frac{P F_{1}}{P F_{2}}=$

解析 $\sqrt{3}-1$.

和物理中的电场线、磁场线类似,我们可以作出对线段 $F_{1} F_{2}$ 的“等张角线”, 如图所示:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-040.jpg?height=385&width=745&top_left_y=779&top_left_x=545)

由此可知, 取 $F_{1} F_{2}$ 的“等张角线” 中与直线 $l$ 相切的一条圆弧, 仜切点位置就是 $\angle F_{1} P F_{2}$ 取最大值的位置. 从而, 设该圆弧的圆心为 $M(0, m)$, 则

$$
\sqrt{12+m^{2}}=\frac{|\sqrt{3} m-8-2 \sqrt{3}|}{\sqrt{1^{2}+(\sqrt{3})^{2}}}
$$

解得 $m=2$, 或 $m=-2(7+8 \sqrt{3})$. 舍去负根, 可得 $m=2$, 进而圆弧的半径 $R=4$, 可计算得 $P(-2,2+$ $2 \sqrt{3})$. 因此可计算得

$$
\frac{P F_{1}}{P F_{2}}=\sqrt{3}-1
$$

利用“等张角线”处理张角问题是一种典型的轨迹思想,其本质是“分而治之”.

## 第 554 题 最大张角问题

如图 1, 已知 $F$ 是双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0, b>0)$ 的焦点, $A$ 是相应的顶点, $P$是 $y$ 轴上的点, 满足 $\angle F P A=\alpha$, 则双曲线的离心率的最小值为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-040.jpg?height=344&width=352&top_left_y=2069&top_left_x=1374)

图 1
解析 $\frac{1+\sin \alpha}{1-\sin \alpha}$.

我们先研究: 当 $F, A$ 固定时, 点 $P$ 在 $y$ 轴上运动, $\angle F P A$ 何时取到最大值,我们有以下结论: 当点 $P$ 位于过 $A, F$ 两点且与 $y$ 轴相切的圆上, 且为切点时, $\angle F P A$ 最大.

如图 2, 记 $\triangle F A P$ 的外接圆圆心为 $Q$, 记 $\angle F P A$ 为最大值作 $Q R \perp F A$ 于点 $R$, 则

$$
O P_{0}^{2}=O A \cdot O F=a c
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-041.jpg?height=350&width=397&top_left_y=197&top_left_x=1460)

图 2

所以

$$
Q R=O P_{0}=\sqrt{a c}
$$

所以

$$
\tan \angle F P_{0} A=\tan \angle F Q R=\frac{\frac{1}{2}(c-a)}{\sqrt{a c}} \geqslant \tan \alpha
$$

即

$$
\sqrt{e}-\sqrt{\frac{1}{e}} \geqslant 2 \tan \alpha>0
$$

两边平方化简得

$$
e+\frac{1}{e} \geqslant 4 \tan ^{2} \alpha+2=\frac{2+2 \sin ^{2} \alpha}{\cos ^{2} \alpha}=\frac{(1+\sin \alpha)^{2}+(1-\sin \alpha)^{2}}{1-\sin ^{2} \alpha}
$$

所以

$$
e_{\min }=\frac{1+\sin \alpha}{1-\sin \alpha}
$$

思考与总结

本题中用到的结论是一个重要的数学模型, 可以从正弦定理角度去推导, 因为

$$
\frac{F A}{\sin \angle F P A}=2 r
$$

故当 $\triangle F A P$ 的外接圆圆 $Q$ 的半径 $r$ 有最小值时, 对应的张角 $\angle F P A$ 有最大值. 而圆心 $Q$ 在线段 $F A$的中垂线上,故

$$
r=Q P \geqslant Q P_{0},
$$

当且仅当点 $P$ 为圆 $Q$ 与 $y$ 轴的切点时取到等号, 如图 3:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-041.jpg?height=304&width=307&top_left_y=1813&top_left_x=676)

图 3

也可以从等张角线角度去理解,过 $F A$ 的等张角线如图 4,每段圆弧对应的 $\angle F P A$ 相等, 随着曲线向外扩展, $\angle F P A$ 逐渐减小.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-041.jpg?height=518&width=353&top_left_y=1690&top_left_x=1504)

图 4

## 第 555 题 最大张角

## 在 $\triangle A B C$ 中,角 $A$ 是钝角, $A B=3, \overrightarrow{B C} \cdot \overrightarrow{B A}=12$, 当角 $C$ 最大时, $\triangle A B C$ 的面积等于

## 解析 3 .

记角 $A, B, C$ 所对的边长为 $a, b, c$, 由题意知

$$
c=3, a \cos B=4 .
$$

所以点 $C$ 在如图 1 的直线 $l$ 上 (也可以直接通过向量的数量积得到向量 $\overrightarrow{B C}$ 在向量 $\overrightarrow{B A}$ 上的射影长为 4 );

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-042.jpg?height=262&width=284&top_left_y=787&top_left_x=503)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-042.jpg?height=256&width=284&top_left_y=787&top_left_x=1024)

图 2

问题转化成当点 $C$ 在直线 $l$ 上运动时, 角 $C$ 何时有最大值?

如图 2 考虑过点 $A, B$ 的圆, 当圆与直线 $l$ 相切时,切点即为所求的点 $C$.

此时圆的半径为 $\frac{5}{2}$, 半弦长为 $\frac{3}{2}$, 所以圆心到弦 $A B$ 的距离为 2 , 这也是点 $C$ 到 $A B$ 的距离, 从而所求面积为 3 .

## 第 556 题 相对运动

如图 1, 在平面直角坐标系中, $P(6,8)$, 四边形 $A B C D$ 为矩形, $A B=16, A D=$ 9 ,点 $A, B$ 分别在射线 $O P$ 和 $O x$ 上,求 $O D$ 的最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-042.jpg?height=246&width=309&top_left_y=1568&top_left_x=1419)

图 1

解析 注意到在矩形 $A B C D$ 运动的过程中 $\angle A O B$ 始终不变,

因此可以看作矩形 $A B C D$ 不动, 而点 $O$ 在圆弧上运动, 如图 2.

在图中, 由于 $\tan \angle A O B=\frac{4}{3}$, 于是点 $Q$ 到弦 $A B$ 的距离为 6 , 圆 $Q$ 的半径为 10 . 因此 $O D$ 的最大值为

$$
C_{0} D=C_{0} Q+Q D=10+\sqrt{(6+9)^{2}+8^{2}}=27
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-042.jpg?height=290&width=230&top_left_y=1920&top_left_x=1521)

图 2

## 第 557 题 逃不开的轨迹

若实数 $a, b, c$ 成等差数列, 点 $P(-1,0)$ 在动直线 $a x+b y+c=0$ 上的投影为 $M$, 点 $N(3,3)$, 求线段 $M N$ 长度的取值范围.

解析 由于实数 $a, b, c$ 成等差数列, 因此动直线 $l: a x+b y+c=0$ 恒过点 $A(1,-2)$. 如图.

根据题意, $\angle P M A$ 恒为直角, 因此点 $M$ 的轨迹是以 $P A$ 为直径的圆

$$
(x+1)(x-1)+(y-0)(y+2)=0,
$$

即

$$
x^{2}+(y+1)^{2}=2
$$

因此线段 $M N$ 长度的取值范围是 $[5-\sqrt{2}, 5+\sqrt{2}]$.

## 第 558 题 阿波罗尼斯圆

如图 1, 圆 $C$ 与 $x$ 轴相切于点 $T(1,0)$, 与 $y$ 轴正半轴交于点 $A, B$ (点 $B$ 在点 $A$ 的上方), 且 $A B=2$.

(1) 圆 $C$ 的标准方程为 $\qquad$ $;$

(2) 过点 $A$ 任作一条直线与圆 $O: x^{2}+y^{2}=1$ 相交于 $M, N$ 两点,下列三个结论:

(1) $\frac{N A}{N B}=\frac{M A}{M B}$;

(2) $\frac{N B}{N A}-\frac{M A}{M B}=2$;

(3) $\frac{N B}{N A}+\frac{M A}{M B}=2 \sqrt{2}$.

其中正确结论的序号是 $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-043.jpg?height=386&width=339&top_left_y=1333&top_left_x=1480)

图 1 . (写出所有正确结论的序号)

解析 $(1)(x-1)^{2}+(y-\sqrt{2})^{2}=2$;

(2) (1)(2)(3).

(1) 由于圆 $C$ 与 $x$ 轴相切于点 $(1,0)$, 于是弦 $A B$ 与圆心的距离为 1 , 进而可得圆的半径为 $\sqrt{2}$, 于是圆 $C$的方程为

$$
(x-1)^{2}+(y-\sqrt{2})^{2}=2
$$

(2) 点 $A(0, \sqrt{2}-1)$, 点 $B(0, \sqrt{2}+1)$, 设圆 $O$ 与 $y$ 轴的交点分别为 $P, Q$, 如图 2 所示.

由于

$$
\overrightarrow{A P}=(\sqrt{2}-1) \overrightarrow{P B}, \overrightarrow{A Q}=-(\sqrt{2}-1) \overrightarrow{Q B}
$$

于是以 $P Q$ 为直径的圆 $O$ 上的点到点 $A$ 与到点 $B$ 的距离之比

$$
\frac{M A}{M B}=\frac{N A}{N B}=\sqrt{2}-1,
$$

因此命题(1)(2)(3)均正确.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-043.jpg?height=372&width=334&top_left_y=2079&top_left_x=1526)

图 2

## 第 559 题 向量的两面性

如图 1, 若点 $A$ 在圆 $C:(x-1)^{2}+(y+2)^{2}=4$ 上运动, 点 $B$ 在 $y$ 轴上运动,则对定点 $P(3,2)$ 而言, $|\overrightarrow{P A}+\overrightarrow{P B}|$ 的最小值为 $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-044.jpg?height=410&width=339&top_left_y=446&top_left_x=1375)

图 1

解析 3.

解法一 直角坐标 设 $A\left(x_{1}, y_{1}\right), B\left(0, y_{2}\right)$, 其中 $-1 \leqslant x_{1} \leqslant 3, y_{2} \in \mathbf{R}$, 则

$$
|\overrightarrow{P A}+\overrightarrow{P B}|=\sqrt{\left(x_{1}-6\right)^{2}+\left(y_{1}+y_{2}-4\right)^{2}} \geqslant \sqrt{\left(x_{1}-6\right)^{2}} \geqslant 3
$$

等号当 $x_{1}=3$ 且 $y_{2}=6$ 时取得, 因此所求最小值为 3 .

参数方程 设 $A(1+2 \cos \theta,-2+2 \sin \theta), B(0, t)$, 其中 $\theta, t \in \mathbf{R}$, 则

$$
|\overrightarrow{P A}+\overrightarrow{P B}|=\sqrt{(2 \cos \theta-5)^{2}+(t+2 \sin \theta-6)^{2}} \geqslant \sqrt{(2 \cos \theta-5)^{2}} \geqslant 3
$$

等号当 $t+2 \sin \theta-6=0$ 且 $\cos \theta=1$ 时, 即 $\theta=0$ 且 $t=6$ 时取得, 因此所求最小值为 3 .

解法二 解决问题的关键是将所求两个向量的和转化为一个向量, 以方便研究它的长度.

平行四边形法则 取线段 $A B$ 的中点 $M$, 则

$$
\overrightarrow{P A}+\overrightarrow{P B}=2 \overrightarrow{P M}
$$

于是问题转化为求向量 $\overrightarrow{P M}$ 长度最大值的两倍.

接下来的问题就是思考点 $M$ 的轨迹. 不妨先固定点 $B$, 这样 $M$ 的轨迹就是一个半径为 1 的圆, 然后再让 $B$ 点在 $y$ 轴上动起来, 这样点 $M$ 的轨迹就是在两条平行直线间的部分, 如图 2(也可以先固定 $A$ 点). 这样我们就得到了所求的最小值为 3.

三角形法则 如图 3 , 作 $B$ 点关于 $P$ 点的对称点 $B^{\prime}$, 则

$$
\overrightarrow{P A}+\overrightarrow{P B}=\overrightarrow{P A}-\overrightarrow{P B^{\prime}}=\overrightarrow{B^{\prime} A}
$$

于是问题转化为求向量 $\overrightarrow{B^{\prime} A}$ 长度的最小值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-044.jpg?height=347&width=361&top_left_y=1943&top_left_x=227)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-044.jpg?height=434&width=323&top_left_y=1905&top_left_x=864)

图 4

事实上, 点 $B^{\prime}$ 的轨迹是 $y$ 轴关于 $P$ 点对称的直线 $x=6$, 于是问题转化成圆 $C$ 上的点到直线 $x=6$ 的距离的最小值, 不难求得为 3 .

当然,也可以作 $A$ 点关于 $P$ 点的对称点,如图 4, 本质相同.

## 第 560 题 动中有静

如图 1, 已知圆 $O: x^{2}+y^{2}=4, F(0,2)$, 点 $A, B$ 是圆 $O$ 上的动点, 且 $|F A| \cdot|F B|$ $=4$, 是否存在与动直线 $A B$ 恒相切的定圆, 若存在, 求出该圆的方程; 若不存在, 请说明理由.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-045.jpg?height=301&width=274&top_left_y=455&top_left_x=1550)

图 1

解析 存在, 圆的方程为 $x^{2}+(y-2)^{2}=1$.

解法一 设 $A(2 \cos 2 \alpha, 2 \sin 2 \alpha), B(2 \cos 2 \beta, 2 \sin 2 \beta)$, 则

$$
\begin{aligned}
|F A| \cdot|F B| & =\sqrt{(2 \cos 2 \alpha)^{2}+(2 \sin 2 \alpha-2)^{2}} \cdot \sqrt{(2 \cos 2 \beta)^{2}+(2 \sin 2 \beta-2)^{2}} \\
& =\sqrt{8-8 \sin 2 \alpha} \cdot \sqrt{8-8 \sin 2 \beta} \\
& =8|(\sin \alpha-\cos \alpha)(\sin \beta-\cos \beta)| \\
& =8|\cos (\alpha-\beta)-\sin (\alpha+\beta)|
\end{aligned}
$$

另一方面, 直线 $A B$ 的方程为

$$
x \cos (\alpha+\beta)+y \sin (\alpha+\beta)-2 \cos (\alpha-\beta)=0
$$

因此点 $F(0,2)$ 到直线 $A B$ 的距离为

$$
\frac{2|\sin (\alpha+\beta)-\cos (\alpha-\beta)|}{\sqrt{\cos ^{2}(\alpha+\beta)+\sin ^{2}(\alpha+\beta)}}=\frac{1}{4}|F A| \cdot|F B|=1,
$$

为定值, 于是定圆 $F: x^{2}+(y-2)^{2}=1$ 与动直线 $A B$ 恒相切.

解法二 如图 2. 设 $\angle A F B=\theta$, 作 $F H \perp A B$ 于点 $H$, 则

$$
|A B|=2 r \sin \frac{\angle A O B}{2}=4 \sin \theta
$$

其中 $r=2$ 为圆 $O$ 的半径, 于是 $\triangle F A B$ 的面积

$$
S_{\triangle A F B}=\frac{1}{2} \cdot|A B| \cdot|F H|=2 \sin \theta \cdot|F H|
$$

同时亦有

$$
S_{\triangle A F B}=\frac{1}{2} \cdot \sin \theta \cdot|F A| \cdot|F B|=2 \sin \theta
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-045.jpg?height=345&width=271&top_left_y=1455&top_left_x=1593)

图 2

因此 $|F H|=1$ 为定值, 于是定圆 $F: x^{2}+(y-2)^{2}=1$ 与动直线 $A B$ 恒相切.

## 第 561 题 交点曲线系

如图 1, 函数 $y=x^{2}+a x+b$ 的图象与坐标轴交于三个不同的点 $A, B, C$, 已知 $\triangle A B C$ 的外心在直线 $y=x$ 上, 求 $a+b$ 的值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-045.jpg?height=337&width=337&top_left_y=2193&top_left_x=1508)

图 1

## 解析 解法一

作出 $\triangle A B C$ 的外接圆圆 $M$, 我们发现圆 $M$ 实际上是过抛物线与 $x$ 轴、 $y$ 轴的交点的曲线, 因此可以尝试用交点曲线系解决问题.

事实上,抛物线方程为

$$
F: x^{2}+a x+b-y=0,
$$

而 $x$ 轴、轴的方程为

$$
G: x y=0,
$$

此时我们发现利用常规的交点曲线系 $f(x, y)+\lambda g(x, y)=0$ 得到的方程

$$
\left(x^{2}+a x+b-y\right)+\lambda \cdot x y=0 .
$$

不可能形成圆.

那么问题出在哪里, 又该怎样解决呢?

由于圆的方程的特点,我们知道问题出在交叉项 $x y$ 上. 因此需要仔细思考交点 $C(0, b)$ 除了用 $x=0$ 描述, 是否还有其他方法.

到这里, 答案几乎是显然的, 应该采用 $y=b$ 描述, 如图 2 所示, 此时可以将交点曲线系写为

$$
\left(x^{2}+a x+b-y\right)+\lambda \cdot y(y-b)=0
$$

当方程表示圆时, $\lambda=1$, 于是再由圆心在直线 $y=x$ 上, 可得关于 $x, y$ 的一次项的

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-046.jpg?height=328&width=331&top_left_y=631&top_left_x=1420)

图 2 系数相同, 即

$$
a=-1-b
$$

从而 $a+b$ 的值为 -1 .

本题源自 2008 年高考江苏卷第 18 题:

在平面直角坐标系 $x O y$ 中, 记二次函数 $f(x)=x^{2}+2 x+b(x \in \mathbf{R})$ 与坐标轴有三个交点, 经过这三个交点的圆记为 $C$.

(1) 求实数 $b$ 的取值范围;

(2)求圆 $C$ 的方程;

(3) 问圆 $C$ 是否经过定点 (其坐标与 $b$ 无关)? 证明你的结论.

解法二 设 $A\left(x_{1}, 0\right), B\left(x_{2}, 0\right)$, 圆的方程为 $x^{2}+y^{2}+m x+m y+n=0$, 而 $C(0, b)$,于是

$$
\left\{\begin{array}{l}
x_{1}^{2}+m x_{1}+n=0 \\
x_{2}^{2}+m x_{2}+n=0 \\
b^{2}+m b+n=0
\end{array}\right.
$$

由于 $x_{1}, x_{2}$ 同时是方程

$$
x^{2}+a x+b=0
$$

和方程

$$
x^{2}+m x+n=0
$$

的两个根, 于是 $m=a$ 且 $n=b$, 因此

$$
b^{2}+a b+b=0
$$

即

$$
a+b=-1
$$

解法三 显然圆心的坐标为 $M\left(-\frac{a}{2},-\frac{a}{2}\right)$, 于是对原点 $O$ 应用圆幂定理有

$$
\overrightarrow{O A} \cdot \overrightarrow{O B}=O M^{2}-M C^{2}
$$

即

$$
b=\left(-\frac{a}{2}\right)^{2}+\left(-\frac{a}{2}\right)^{2}-\left[\left(-\frac{a}{2}\right)^{2}+\left(-\frac{a}{2}-b\right)^{2}\right]
$$

整理即得

$$
a+b=-1 \text {. }
$$

## 第 562 题 过三点的圆

已知 $\triangle A B C$ 是等轴双曲线 $H$ 的内接三角形, $P, Q, R$ 分别是边 $B C, A C, A B$ 上的中点, 求证: $\triangle P Q R$ 的外接圆恒过定点.

解析 根据双曲线的对称性, 若 $\triangle P Q R$ 的外接圆恒过定点, 则该定点一定为双曲线的中心. 下面给出证明.

如图, 不妨设等轴双曲线的方程为 $y=\frac{1}{x}$, 此时 $A\left(a, \frac{1}{a}\right), B\left(b, \frac{1}{b}\right), C\left(c, \frac{1}{c}\right)$, 其中 $a, b, c$ 互不相等. 这样就有

$$
P\left(\frac{b+c}{2}, \frac{b+c}{2 b c}\right), Q\left(\frac{c+a}{2}, \frac{c+a}{2 c a}\right), R\left(\frac{a+b}{2}, \frac{a+b}{2 a b}\right)
$$

当 $(a+b)(b+c)(c+a)=0$ 时, 命题显然成立. 当 $(a+b)(b+c)(c+a) \neq 0$ 时, 设 $\triangle P Q R$ 的外接圆方程为

$$
x^{2}+y^{2}+D x+E y+F=0,
$$

则

$$
\left(\frac{a+b}{2}\right)^{2}+\left(\frac{a+b}{2 a b}\right)^{2}+D \cdot \frac{a+b}{2}+E \cdot \frac{a+b}{2 a b}+F=0
$$

也即

$$
\frac{a+b}{2}+\frac{a+b}{2 a^{2} b^{2}}+D+E \cdot \frac{1}{a b}+F \cdot \frac{2}{a+b}=0
$$

类似的, 有

$$
\frac{b+c}{2}+\frac{b+c}{2 b^{2} c^{2}}+D+E \cdot \frac{1}{b c}+F \cdot \frac{2}{b+c}=0
$$

两式相减, 可得

$$
\frac{a-c}{2}+\frac{(c-a)(a b+b c+c a)}{2 a^{2} b^{2} c^{2}}+E \cdot \frac{c-a}{a b c}+F \cdot \frac{2(c-a)}{(a+b)(b+c)}=0
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-047.jpg?height=474&width=465&top_left_y=1071&top_left_x=1398)

也即

$$
-\frac{1}{2}+\frac{a b+b c+c a}{2 a^{2} b^{2} c^{2}}+E \cdot \frac{1}{a b c}+F \cdot \frac{2}{(a+b)(b+c)}=0
$$

类似的, 有

$$
-\frac{1}{2}+\frac{a b+b c+c a}{2 a^{2} b^{2} c^{2}}+E \cdot \frac{1}{a b c}+F \cdot \frac{2}{(b+c)(c+a)}=0
$$

两式相减,即得 $F=0$, 因此命题得证.

## 第 563 题 曲线系

已知圆 $M:(x+\cos \theta)^{2}+(y-\sin \theta)^{2}=1$, 直线 $l: y=k x$, 下面四个命题:

(1)对任意实数 $k$ 与 $\theta$, 直线 $l$ 和圆 $M$ 相切;

(2)对任意实数 $k$ 与 $\theta$, 直线 $l$ 和圆 $M$ 有公共点;

(3)对任意实数 $\theta$, 必存在实数 $k$, 使得直线 $l$ 和圆 $M$ 相切;

(4)对任意实数 $k$,必存在实数 $\theta$, 使得直线 $l$ 与圆 $M$ 相切.

其中真命题的代号是 . (写出所有真命题的代号)[^0]圆 $M$ 表示半径为 1 ,圆心为 $(-\cos \theta, \sin \theta)$ 的圆,随着参数 $\theta$ 的变化, 圆 $M$ 的圆心在单位圆上运动.

直线 $y=k x$ 表示过原点且斜率存在 (斜率为 $k$ ) 的直线. 因此对四个命题有以下判断:

(1)可能相切,也有可能相交;

(2)原点必然为公共点;

(3)由于直线系中缺失 $y$ 轴,于是当圆心为 $( \pm 1,0)$ 时，不存在形如 “ $y=k x$ ”的方程所表示的直线 $l$ 与圆 $M$ 相切

(4)对任何一条直线系中的直线, 只需要过原点作其垂线与单位圆相交,取圆系中以交点为圆心的圆即得.

因此不难得到正确答案为(2)(4).

## 第 564 题 划清界限得范围

已知圆 $C: x^{2}+y^{2}=2$, 直线 $l: x+2 y-4=0$, 点 $P\left(x_{0}, y_{0}\right)$ 在直线 $l$ 上. 若存在圆 $C$ 上的点 $Q$, 使得 $\angle O P Q=45^{\circ}\left(O\right.$ 为坐标原点), 则 $x_{0}$ 的取值范围是
A. $[0,1]$
B. $\left[0, \frac{8}{5}\right]$
C. $\left[-\frac{1}{2}, 1\right]$
D. $\left[-\frac{1}{2}, \frac{8}{5}\right]$

解析 B.

首先寻找对圆的视角等于 $90^{\circ}$ 的点的轨迹, 显然这是一个封闭曲线为圆 $x^{2}+y^{2}=$ 4. 那么在该圆内部的点对圆 $C$ 的视角均大于 $90^{\circ}$, 必然存在使 $\angle O P Q=45^{\circ}$ 的点; 同时在圆外部的点对圆的视角均小于 $90^{\circ}$, 一定不可能使得 $\angle O P Q=45^{\circ}$.

由此分析不难得出,所求点 $P$ 的取值集合为直线 $l: x+2 y-4=0$ 被圆 $x^{2}+y^{2}=4$所截得的线段 $P_{1} P_{2}$. 如图.

设 $P\left(x_{0}, \frac{1}{2}\left(4-x_{0}\right)\right)$, 则

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-048.jpg?height=347&width=311&top_left_y=1182&top_left_x=1440)

$$
x_{0}^{2}+\frac{1}{4}\left(4-x_{0}\right)^{2} \leqslant 4
$$

解得

$$
0 \leqslant x_{0} \leqslant \frac{8}{5}
$$

因此 $x_{0}$ 的取值范围是 $\left[0, \frac{8}{5}\right]$. 故选 B.

圆 $C$ 上的点对圆 $C$ 的视角可以认为是 $180^{\circ}$, 圆 $C$ 内部的点对圆 $C$ 的视角可以认为是 $360^{\circ}$. 用轨迹的方式思考问题实际上就是将原来的问题拆解为若干子问题,然后求交集的解题方式.

## 第 565 题 莫忘初衷

在平面直角坐标系 $x O y$ 中, 已知圆 $O_{1}$, 圆 $O_{2}$ 均与 $x$ 轴相切, 且圆心 $O_{1}$, 圆 $O_{2}$ 与原点 $O$ 共线, $O_{1}$, $O_{2}$ 两点的横坐标之积为 5 . 设圆 $O_{1}$ 与圆 $O_{2}$ 相交于 $P, Q$ 两点, 直线 $l: 2 x-y-8=0$, 则点 $P$ 到直线 $l$ 的距离的最小值为 $\qquad$ .
解析 $\frac{3 \sqrt{5}}{5}$.

如图, 不妨设圆 $O_{1}$ 的半径小于圆 $O_{2}$ 的半径, 圆 $O_{1}$, 圆 $O_{2}$ 与 $x$ 轴分别相切于点 $A, B, O P$ 与圆 $O_{1}$ 的交点为 $R$.

由于圆 $O_{1}$ 与圆 $O_{2}$ 以 $O$ 为中心位似, 因此弧 $R A$ 与弧 $P B$ 所对的圆周角相等, 从而

可得 $\triangle O A P$ 与 $\triangle O P B$ 相似, 于是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-049.jpg?height=388&width=530&top_left_y=197&top_left_x=1329)

$$
O P^{2}=O A \cdot O B=5
$$

为定值.

这就意味着 $P$ 点的轨迹是以 $O$ 为圆心, $\sqrt{5}$ 为半径的圆 (去掉 $x$ 轴上的两点), 不难得到 $P$ 点到直线 $l$ 的距离的最小值为

$$
\frac{|-8|}{\sqrt{2^{2}+(-1)^{2}}}-\sqrt{5}=\frac{3 \sqrt{5}}{5}
$$

思考与总结

在这个问题中,两个动圆在变化过程中 $O A \cdot O B$ 为定值, 因此设法将这个运动中的不变量转化到点 $P$上来就是解决问题的关键.

## 第 566 题 平面区域

在平面直角坐标系中, 点集 $A=\left\{(x, y) \mid x^{2}+y^{2} \leqslant 1\right\}, B=\{(x, y) \mid x \leqslant 4, y \geqslant 0,3 x-4 y \geqslant 0\}$, 则点集 $P=\left\{(x, y) \mid x=x_{1}+3, y=y_{1}+1,\left(x_{1}, y_{1}\right) \in A\right\}$ 所表示的平面区域的面积为 $\qquad$ ;点集 $Q=\{(x, y)$ $\left.\mid x=x_{1}+x_{2}, y=y_{1}+y_{2},\left(x_{1}, y_{1}\right) \in A,\left(x_{2}, y_{2}\right) \in B\right\}$ 所表示的平面区域的面积为 $\qquad$ .

解析 $\pi ; 18+\pi$.

从点 $M(x, y)$ 得到点 $M^{\prime}(x+3, y+1)$ 相当于将点 $M$ 向右平移 3 个单位长度, 再向上平移 1 个单位长度.

根据点集 $P$ 的定义知, 点集 $P$ 就是将点集 $A$ 中的任意一个点向右平移 3 个单位长度, 再向上平移 1 个单位长度得到的, 所以直接将点集 $A$ 表示的平面区域作这样的平移就能得到点集 $P$.

点集 $A$ 是以原点为圆心的单位圆, 所以点集 $P$ 就是以 $(3,1)$ 为圆心,半径为 1 的圆,面积为 $\pi$, 如图 1 所示.

在点集 $Q$ 中, 横坐标是由两个变化的数共同决定的, 纵坐标也是由两个变化的

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-049.jpg?height=232&width=358&top_left_y=1768&top_left_x=1503)

图 1 数共同决定的, 受第一空的启发, 可以先取定一点 $M\left(x_{2}, y_{2}\right) \in B$, 让 $\left(x_{1}, y_{1}\right) \in A$ 变化,由此得到的平面区域是点集 $Q$ 的一部分, 再让 $M\left(x_{2}, y_{2}\right)$ 在区域 $B$ 中运动起来, 就可以得到整个点集 $Q$ 表示的区域.

由第一空知, 取定点 $M\left(x_{2}, y_{2}\right) \in B$ 时, 得到的点集是以点 $M$ 为圆心, 以 1 为半径的圆. 当点 $M$ 在区域 $B$ 中运动起来, 这些单位圆 (及其内部) 运动扫过的区域就是所求的平面区域. 区域 $B$ 是 $\triangle O P Q$ 及其内部构成的区域, 其中 $P(4,3), Q(4,0)$, 只需考虑点 $M$ 在 $\triangle O P Q$ 边界上运动即可, 得到的边界及其内部就是点 $Q$ 表示的平面区域, 如

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-049.jpg?height=293&width=311&top_left_y=2063&top_left_x=1548)

图 2 图 2 所示.

容易计算得所求面积为 $18+\pi$.
在动态问题中, 先固定一个变元, 让另一个变元动起来, 得到一个中间状态, 再让固定的变元动起来,这是常见的处理思路.

## 第 567 题 最大张角

已知圆 $O: x^{2}+y^{2}=4$, 直线 $l: y=k x+5$.

(1) 若存在直线 $l$ 上一点 $A$ 以及圆 $O$ 上一点 $B$, 使得 $\angle O A B=\frac{\pi}{6}$, 求 $k$ 的取值范围;

(2) 若对直线 $l$ 上任意一点 $A$, 均存在圆 $O$ 上一点 $B$, 使得 $\angle O B A=\frac{\pi}{6}$, 求 $k$ 的取值范围.

解析 (1) 当点 $A$ 位于圆 $O$ 内 (包含边界)时, 显然存在 $\angle O A B=\frac{\pi}{6}$. 当点 $A$ 位于圆 $O$ 外部时, $\angle O A B$ 的取值范围是 $\left[0, \arcsin \frac{2}{O A}\right]$, 如图 1 所示.

因此当 $O A \leqslant 4$ 时, $\angle O A B$ 可以取得 $\frac{\pi}{6}$. 回到原问题, 即圆心 $O$ 到直线 $l$ 的距离不

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-050.jpg?height=215&width=327&top_left_y=983&top_left_x=1440)

图 1 大于 4, 也即

$$
\frac{5}{\sqrt{1+k^{2}}} \leqslant 4
$$

解得 $k$ 的取值范围是 $\left(-\infty,-\frac{3}{4}\right] \cup\left[\frac{3}{4},+\infty\right)$.

(2) 当点 $A$ 位于圆 $O$ 外 (包含边界) 时, 显然存在 $\angle O B A=\frac{\pi}{6}$. 当点 $A$ 位于圆 $O$ 内部时, $\angle O B A$ 的取值范围是 $\left[0, \arcsin \frac{O A}{2}\right]$, 如图 2 所示.

因此当 $O A \geqslant 1$ 时, $\angle O B A$ 可以取得 $\frac{\pi}{6}$. 回到原问题, 即圆心 $O$ 到直线 $l$ 的距离不小于

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-050.jpg?height=246&width=242&top_left_y=1524&top_left_x=1523)

图 2 1 , 也即

$$
\frac{5}{\sqrt{1+k^{2}}} \geqslant 1
$$

解得 $k$ 的取值范围是 $[-2 \sqrt{6}, 2 \sqrt{6}]$.

先不考虑“点 $A$ 在直线 $l$ 上” 这一条件, 将注意力都放在当 $A$ 点的位置确定时, 随着点 $B$ 的运动, $\angle O A B$ 或 $\angle O B A$ 的变化范围.

## 第 568 题 发现不变量

如图 1 所示, 圆 $O$ 的半径为 $r$, 直角 $\triangle A B C$ 的顶点 $A, B$ 在圆 $O$ 上, $\angle B$ 为直角, $\angle A$ 的大小为 $\theta$, 点 $C$ 在圆 $O$ 内部 (包括边界). 当点 $A$ 在圆 $O$ 上运动时, $O C$ 的最小值为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-051.jpg?height=287&width=274&top_left_y=453&top_left_x=1568)

图 1

解析 $\frac{1-\sin \theta}{\cos \theta} \cdot r$.

如图 2, 延长 $A C$ 交圆 $O$ 于点 $D$, 则由于 $\angle A$ 的大小为定值, 于是 $D$ 为定点, 且 $\angle D C B=\frac{\pi}{2}+\theta$ 为定值, 所以点 $C$ 的轨迹是圆弧.

设 $C$ 点的轨迹所在圆的圆心为 $I$, 半径为 $r^{\prime}$, 则由于

$$
\frac{1}{2} B D=r \sin \theta, \frac{1}{2} \angle B I D=\pi-\angle B C D=\frac{\pi}{2}-\theta
$$

因此

$$
r^{\prime}=r \tan \theta
$$

而

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-051.jpg?height=421&width=377&top_left_y=933&top_left_x=1486)

图 2

$$
O I=r \cos \theta+r^{\prime} \cos \left(\frac{\pi}{2}-\theta\right)=r \cos \theta+r^{\prime} \sin \theta
$$

于是 $O C$ 的最小值为

$$
r \cos \theta+r^{\prime} \sin \theta-r^{\prime}=\frac{1-\sin \theta}{\cos \theta} \cdot r
$$

## 第 569 题 圆环套圆环

如图, 已知点 $A$ 是抛物线 $y=\frac{1}{2} x^{2}$ 上的一个动点, 过点 $A$ 作圆 $D$ : $x^{2}+\left(y-\frac{1}{2}\right)^{2}=r^{2}(r>0)$ 的两条切线, 它们分别切圆 $D$ 于 $E, F$ 两点.

(1) 当 $r=\frac{3}{2}, A$ 点坐标为 $(2,2)$ 时, 求两条切线的方程;

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-051.jpg?height=306&width=512&top_left_y=1913&top_left_x=1331)

(2)若当点 $A$ 抛物线上 (总在圆 $D$ 外部)运动时, 直线 $E F$ 都不通过的点构成一个区域, 求这个区域的面积的取值范围.

解析 (1) 设直线 $k x-y-2 k+2=0$ 是过点 $A$ 的圆的切线, 则

$$
\frac{\left|-2 k+\frac{3}{2}\right|}{\sqrt{1+k^{2}}}=\frac{3}{2}
$$

解得

$$
k=0 \text { 或 } k=\frac{24}{7} .
$$

于是两条切线的方程为 $y-2=0$ 以及 $24 x-7 y-34=0$.

(2)联立抛物线与圆的方程, 可得

$$
2 y+\left(y-\frac{1}{2}\right)^{2}=r^{2}
$$

该方程无正根, 因此 $0<r<\frac{1}{2}$.

设 $A\left(m, \frac{1}{2} m^{2}\right)$, 则直线 $E F$ 的方程为

$$
m x+\left(\frac{1}{2} m^{2}-\frac{1}{2}\right)\left(y-\frac{1}{2}\right)=r^{2}
$$

整理得

$$
\left(\frac{1}{2} y-\frac{1}{4}\right) m^{2}+x m-\frac{1}{2} y+\frac{1}{4}-r^{2}=0
$$

无论 $m$ 取何值, 直线 $E F$ 都不通过点 $(x, y)$ 等价于这个关于 $m$ 的二次方程无解,即

$$
\Delta=x^{2}+\left(y-\frac{1}{2}\right)\left(y-\frac{1}{2}+2 r^{2}\right)<0
$$

也即

$$
x^{2}+\left(y+r^{2}-\frac{1}{2}\right)^{2}<r^{4}
$$

因此所求区域的面积为 $\pi r^{4}$, 取值范围是 $\left(0, \frac{\pi}{16}\right)$.

## 第 570 题 纵横交错

```
已知直线 \(a x+b y-1=0(a, b\) 不全为 0\()\) 与圆 \(x^{2}+y^{2}=50\) 有公共点, 且公共点横坐标和纵坐标均为
整数,那么这样的直线共有
条.
```


## 解析 72.

如图, 横纵坐标均为整数的点我们称为整点, 圆在第一象限有三个整点

$$
(1,7),(5,5),(7,1),
$$

从而知道圆上一共有 12 个整点.

再考虑 $a x+b y-1=0$ 可以表示什么样的直线, 只要一条直线不经过原点, 都可以化成这样的形式, 所以它可以表示所有不经过原点的直线.

最后考虑与圆的公共点为这些整点, 且不经过原点的直线有多少条.

如果公共点只有一个, 即为圆的切线, 共有 12 条, 都满足条件; 如果公共点有两个,共有

$$
\mathrm{C}_{12}^{2}=66
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-052.jpg?height=294&width=311&top_left_y=1991&top_left_x=1461)

条直线, 其中经过原点的有 6 条, 所以满足条件的有 60 条;

综上知, 这样的直线共有 $12+60=72$ 条.

## 第 571 题轨迹问题

已知直线 $l: y=k x$ 与圆 $C: x^{2}+(y-4)^{2}=4$ 相交于 $M, N$ 两点.

(1)求 $k$ 的取值范围;

(2) 若点 $Q$ 在线段 $M N$ 上, 且满足 $\frac{2}{|O Q|^{2}}=\frac{1}{|O M|^{2}}+\frac{1}{|O N|^{2}}$, 求点 $Q$ 的轨迹方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-053.jpg?height=290&width=181&top_left_y=456&top_left_x=1655)

解析 (1)根据题意, 有

$$
\frac{4}{\sqrt{1+k^{2}}}<2
$$

即

$$
k^{2}>3,
$$

于是 $k$ 的取值范围是 $(-\infty,-\sqrt{3}) \cup(\sqrt{3},+\infty)$.

(2) 根据题意, 由圆幂定理及垂径定理可得

$$
\left\{\begin{array}{l}
|O M| \cdot|O N|=12 \\
|O M|+|O N|=2 \cdot \frac{4|k|}{\sqrt{1+k^{2}}}
\end{array}\right.
$$

于是

$$
\frac{2}{|O Q|^{2}}=\frac{(|O M|+|O N|)^{2}-2 \cdot|O M| \cdot|O N|}{(|O M| \cdot|O N|)^{2}}=\frac{5 k^{2}-3}{18\left(1+k^{2}\right)}
$$

设 $Q(x, y)$, 则 $k=\frac{y}{x}(y>0)$, 代人得

$$
\frac{2}{x^{2}+y^{2}}=\frac{5 y^{2}-3 x^{2}}{18\left(x^{2}+y^{2}\right)}
$$

化简得

$$
5 y^{2}-3 x^{2}=36
$$

其中 $\frac{y^{2}}{x^{2}}>3$, 可得 $x^{2}<3$ 且 $x \neq 0$. 从而所求点 $Q$ 的轨迹方程为

$$
5 y^{2}-3 x^{2}=36\left(x^{2}<3, x \neq 0, y>0\right) .
$$

思考与总结

圆幂定理和垂径定理是直线与圆的位置关系问题中的重要定理, 合理的运用这两个定理可以避开复杂的联立运算.

## 第 572 题 “翻译”条件

如图, 已知点 $A(0,3), B(1,0), C(3, m)$, 以 $C$ 为圆心作半径为 $\frac{\sqrt{10}}{3}$ 的圆 $C$.

(1) 若对线段 $A B$ 上的任意一点 $P$,均存在过点 $P$ 的直线与圆 $C$ 相交于点 $M, N(|P M|<|P N|)$, 且 $|P M|=|M N|$, 求 $m$ 的取值范围;

(2) 若线段 $A B$ 上存在一点 $P$, 使过点 $P$ 的某条直线与圆 $C$ 相交于点 $M$, $N(|P M|<|P N|)$, 且 $|P M|=|M N|$, 求 $m$ 的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-054.jpg?height=346&width=398&top_left_y=444&top_left_x=1354)

解析 (1) “过点 $P$ 的某条直线与圆 $C$ 相交于点 $M, N(|P M|<|P N|)$, 且 $|P M|=|M N|$ ” 的充要条件是 “ $\frac{P C-r}{P C+r} \leqslant \frac{1}{2}(r$ 是圆 $C$ 的半径)”. 即 $|P C| \leqslant 3 r$.

题意即点 $C$ 到线段 $A B$ 上任意一点 $P$ 的距离不大于 $3 r$, 这当且仅当

$$
|C A| \leqslant 3 r,|C B| \leqslant 3 r
$$

解得 $2 \leqslant m \leqslant \sqrt{6}$.

(2)题意即在线段 $A B$ 上存在一点 $P$, 到点 $C$ 的距离不大于 $3 r$, 先探索充分条件: 若 $|C A| \leqslant 3 r$ 或 $|C B| \leqslant$ $3 r$, 此时的 $m$ 一定满足条件, 解得

$$
-\sqrt{6} \leqslant m \leqslant 4
$$

若 $m<-\sqrt{6}$, 此时 $C$ 到线段 $A B$ 上的点的距离的最小值为 $|C B|$, 显然不满足; 若 $m>4$, 此时 $C$ 到线段 $A B$ 上的点的距离的最小值为 $|C A|$, 也不满足,

综上知 $m \in[-\sqrt{6}, 4]$.

## 第 573 题 项圈与丝带

设集合

$$
\begin{gathered}
A=\left\{(x, y) \left\lvert\, \frac{m}{2} \leqslant(x-2)^{2}+y^{2} \leqslant m^{2}\right., x, y \in \mathbf{R}\right\}, \\
B=\{(x, y) \mid 2 m \leqslant x+y \leqslant 2 m+1, x, y \in \mathbf{R}\},
\end{gathered}
$$

若 $A \cap B \neq \varnothing$, 则实数 $m$ 的取值范围是 $\qquad$ .

解析 $\left[\frac{1}{2}, 2+\sqrt{2}\right]$.

考虑问题的反面, 若 $A \cap B=\varnothing$, 那么

情形一 集合 $A=\varnothing$. 此时 $\frac{m}{2}>m^{2}$, 即 $0<m<\frac{1}{2}$.

情形二 集合 $A \neq \varnothing$. 当 $m>\frac{1}{2}$ 时, $A$ 表示环形区域;

当 $m=\frac{1}{2}$ 时, $A$ 退化为一个圆圈;

当 $m=0$ 时, $A$ 表示一个点;

当 $m<0$ 时, $A$ 表示一个圆及其内部. $B$ 始终表示两条平行直线及之间的部分.

若 $A \cap B=\varnothing$, 无论 $A$ 表示何种形状, 皆与“圆心 $(2,0)$ 到直线 $x+y=2 m$ 及直线 $x+y=2 m+1$ 的距离均大于 $|m|$ "等价, 即

$$
\left\{\begin{array}{l}
\frac{|2-2 m|}{\sqrt{2}}>|m| \\
\frac{|1-2 m|}{\sqrt{2}}>|m|
\end{array}\right.
$$

解得 $m \leqslant 0$ 或 $m>2+\sqrt{2}$.

综上所述,若 $A \cap B=\varnothing$,那么 $m<\frac{1}{2}$ 或 $m>2+\sqrt{2}$.

因此所求实数 $m$ 的取值范围是 $\left[\frac{1}{2}, 2+\sqrt{2}\right]$.

## 第 574 题 抓住本质改头换面

如图, 已知点 $P$ 是圆 $O: x^{2}+y^{2}=1$ 上一动点, $O$ 为坐标原点.过点 $P$ 作圆 $O$ 的切线 $l$ 与圆 $O_{1}: x^{2}+y^{2}-2 x-8 y=19$ 相交于 $A$, $B$ 两点, 则 $\frac{A P}{B P}$ 的最大值为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-055.jpg?height=571&width=563&top_left_y=870&top_left_x=1262)

解析 $3+2 \sqrt{2}$.

不改变问题的本质,将问题拓展. 已知单位圆 $O: x^{2}+y^{2}=1$ 及其在点 $P(0,1)$ 处的切线 $l: y=1$, 圆 $O_{1}$ 的圆心到点 $O$ 的距离为 $d$, 半径为 $r$ 且与直线 $l$ 交于 $A, B$ 两点, 求 $A, B$ 两点横坐标绝对值的比的取值范围.

设 $O_{1}(d \cos \theta, d \sin \theta)$, 则圆 $O_{1}$ 的方程为

$$
(x-d \cos \theta)^{2}+(y-d \sin \theta)^{2}=r^{2},
$$

与直线 $l$ 的方程联立可得

$$
x^{2}-2 d \cos \theta \cdot x+d^{2}-r^{2}-2 d \sin \theta+1=0 .
$$

设 $A, B$ 两点横坐标的比为 $\lambda$, 则

$$
(-2 d \cos \theta)^{2}=\left(\lambda+\frac{1}{\lambda}+2\right)\left(d^{2}-r^{2}-2 d \sin \theta+1\right)
$$

整理得

$$
\lambda+\frac{1}{\lambda}=m+2 d \sin \theta+\frac{m^{2}-4 d^{2}}{m+2 d \sin \theta}-2 m-2
$$

其中 $m=r^{2}-d^{2}-1$.

当 $m^{2}-4 d^{2} \geqslant 0$ 时, $\lambda+\frac{1}{\lambda}$ 的取值范围是 $\left[2 \sqrt{m^{2}-4 d^{2}}-2 m-2,-2\right]$, 最小值当 $m+2 d \sin \theta=\sqrt{m^{2}-4 d^{2}}$时取得, 最大值当 $\sin \theta= \pm 1$ 时取得.

回到本题中, 有 $m=r^{2}-d^{2}-1=18$, 于是 $\lambda+\frac{1}{\lambda}$ 的最小值为 -6 , 进而可得 $\frac{A P}{B P}$ 的最大值为 $3+2 \sqrt{2}$.

## 第 575 题 平移齐次解张直角问题

已知圆 $x^{2}+y^{2}=4$ 的切线与 $x$ 轴正半轴、 $y$ 轴正半轴围成一个三角形. 当该三角形的面积最小时切点为 $P$. 双曲线 $C_{1}: \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ 过点 $P$ 且离心率为 $\sqrt{3}$.

(1) 求 $C_{1}$ 的方程;

(2) 椭圆 $C_{2}$ 过点 $P$ 且与 $C_{1}$ 有相同的焦点, 直线 $l$ 过 $C_{2}$ 的右焦点 $F$ 且与 $C_{2}$ 交于 $A, B$ 两点. 若以线段 $A B$ 为直径的圆过点 $P$, 求 $l$ 的方程.

解析 (1) 设圆 $x^{2}+y^{2}=4$ 的切线为 $x_{0} x+y_{0} y=4$, 切点为 $\left(x_{0}, y_{0}\right)$, 满足

$$
x_{0}^{2}+y_{0}^{2}=4, x_{0}>0, y_{0}>0
$$

则所围成的三角形面积为

$$
\frac{1}{2} \cdot \frac{4}{x_{0}} \cdot \frac{4}{y_{0}}=\frac{2\left(x_{0}^{2}+y_{0}^{2}\right)}{x_{0} y_{0}}=2\left(\frac{x_{0}}{y_{0}}+\frac{y_{0}}{x_{0}}\right)
$$

于是当 $x_{0}=y_{0}=\sqrt{2}$ 时, 该三角形的面积最小. 结合双曲线 $C_{1}$ 过点 $P(\sqrt{2}, \sqrt{2})$, 离心率为 $\sqrt{3}$, 可得其方程为 $x^{2}-\frac{y^{2}}{2}=1$.

(2) 根据题意, 陏圆 $C_{2}$ 的方程为 $\frac{x^{2}}{6}+\frac{y^{2}}{3}=1$. 以 $A B$ 为直径的圆过点 $P$, 因此直线 $A B$ 过点 $P$ 或者线段 $A B$ 对 $P$ 点的张角为直角.

如图 1, 以 $P$ 为原点, 以原来的坐标轴方向为新的坐标轴方向重新建立平面直角坐标系 $x^{\prime} P y^{\prime}$,则新坐标系下的椭圆方程为

$$
\frac{\left(x^{\prime}+\sqrt{2}\right)^{2}}{6}+\frac{\left(y^{\prime}+\sqrt{2}\right)^{2}}{3}=1
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-056.jpg?height=303&width=373&top_left_y=1223&top_left_x=1412)

图 1

整理得

$$
\frac{1}{6} x^{\prime 2}+\frac{1}{3} y^{\prime 2}+\frac{\sqrt{2}}{3} x^{\prime}+\frac{2 \sqrt{2}}{3} y^{\prime}=0
$$

设直线 $m x^{\prime}+n y^{\prime}=1$ 被椭圆截得的弦对 $P$ 点的张角为直角, 则化齐次联立, 有

$$
\frac{1}{6} x^{\prime 2}+\frac{1}{3} y^{\prime 2}+\left(\frac{\sqrt{2}}{3} x^{\prime}+\frac{2 \sqrt{2}}{3} y^{\prime}\right) \cdot\left(m x^{\prime}+n y^{\prime}\right)=0
$$

从而有

$$
\left(\frac{1}{3}+\frac{2 \sqrt{2}}{3} n\right) \cdot\left(\frac{y^{\prime}}{x^{\prime}}\right)^{2}+\left(\frac{\sqrt{2}}{3} n+\frac{2 \sqrt{2}}{3} m\right) \cdot\left(\frac{y^{\prime}}{x^{\prime}}\right)+\frac{1}{6}+\frac{\sqrt{2}}{3} m=0
$$

根据题意, $P A \perp P B$, 于是该方程的两根之积为 -1 , 即

$$
\frac{\frac{1}{6}+\frac{\sqrt{2}}{3} m}{\frac{1}{3}+\frac{2 \sqrt{2}}{3} n}=-1
$$

整理得

$$
-\frac{2 \sqrt{2}}{3} m-\frac{4 \sqrt{2}}{3} n=1
$$

因此该直线恒过新坐标系的点 $Q\left(-\frac{2 \sqrt{2}}{3},-\frac{4 \sqrt{2}}{3}\right)$, 也即旧坐标系下的点 $\left(\frac{\sqrt{2}}{3},-\frac{\sqrt{2}}{3}\right)$.
此时可知直线 $Q F$ 和直线 $P F$ 的方程为所求,结合 $F(\sqrt{3}, 0)$ 可得 $l$ 的方程为

$$
x-\left(\frac{3 \sqrt{6}}{2}-1\right) y-\sqrt{3}=0
$$

或

$$
x+\left(\frac{\sqrt{6}}{2}-1\right) y-\sqrt{3}=0
$$

'思考与总结

很容易遗漏直线 $P F$. 事实上, 只要出现圆锥曲线上的动弦对某定点张直角时,都可以考虑用此方法处理. 并且不难得到,若定点在圆锥曲线上,那么动弦恒过定点. 设 $P$ 为椭圆上一点, 对点 $P$ 的张角为直角的椭圆的弦过定点, 如图 2.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-057.jpg?height=304&width=383&top_left_y=608&top_left_x=1462)

图 2

## 第 576 题 乾忆大挪移

在平面直角坐标系中, 已知点 $F(3,0)$ 在圆 $C:(x-m)^{2}+(y-2)^{2}=40$ 内, 动直线 $A B$ 过点 $F$ 且交圆于 $A, B$ 两点, 若 $\triangle A B C$ 的面积的最大值为 20 , 则实数 $m$ 的取值范围是

解析 $(-3,-1] \cup[7,9)$.

注意到 $\triangle A B C$ 是以弦 $A B$ 为底, 圆 $C$ 的半径为腰的等腰三角形. 于是可得当 $\triangle A B C$ 的面积取得最大值 20 时, 其顶角 $\angle A C B$ 为直角, 进而将条件 “挪移” 为圆心 $C$ 到直线 $A B$ 的距离为半径的 $\frac{1}{\sqrt{2}}$, 也即直线 $A B$是圆

$$
(x-m)^{2}+(y-2)^{2}=20
$$

的切线, 如图.

因此题意即过点 $F$ 可以作圆

$$
(x-m)^{2}+(y-2)^{2}=20
$$

的切线, 即

$$
20 \leqslant(3-m)^{2}+(0-2)^{2}<40
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-057.jpg?height=347&width=356&top_left_y=1658&top_left_x=1503)

解得 $m$ 的取值范围是 $(-3,-1] \cup[7,9)$.

在解直线与圆的题目时, 以下几何量知其二就能推出其他几何量:

(1)半径 $r ;$ (2)弦所对的圆心角或圆周角 $\theta$; (3)弦长 $l$; (4)弦心距 $d$.

另一方面,弦的两个端点与圆心构成的三角形的面积可以由 (1) (2)计算, 也可以由 (3)(4)计算, 这些几何量之间的关系是需要在计算中熟练应用的.

## 第 577 题 美好的圆

在圆 $x^{2}+y^{2}=25$ 上有一点 $P(4,3)$, 点 $E, F$ 是 $y$ 轴上两点, 且满足 $|P E|=|P F|$, 直线 $P E, P F$ 与圆交于点 $C, D$, 则直线 $C D$ 的斜率是

## 解析 $\frac{4}{3}$.

当点 $E, F$ 在 $y$ 轴上运动时, 直线点 $C D$ 的斜率不变.

过点 $P$ 作 $x$ 轴的平行线, 交圆 $O$ 于 $Q$, 连结 $O Q, C Q, D Q$, 如图.

我们知道

$$
\angle C P Q=\angle D P Q \text {, }
$$

从而有

$$
C Q=D Q,
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-058.jpg?height=377&width=345&top_left_y=606&top_left_x=1433)

即 $Q$ 点平分弧 $C D$, 故有

$$
O Q \perp C D
$$

而 $Q(-4,3)$, 故

$$
k_{C D}=-\frac{1}{k_{C Q}}=\frac{4}{3}
$$

当点 $E, F$ 越来越靠近时, 点 $C, D$ 趋近于 $Q$ 点, 直线 $C D$ 的极限情况是圆 $O$ 在点 $Q$ 处的切线.

## 第 578 题 圆环套圆环

在平面直角坐标系 $x O y$ 中, 已知向量 $\boldsymbol{a}, \boldsymbol{b},|\boldsymbol{a}|=\boldsymbol{b}=1, \boldsymbol{a} \cdot \boldsymbol{b}=1, \boldsymbol{a} \cdot \boldsymbol{b}=0$, 点 $Q$ 满足 $\overrightarrow{O Q}=\sqrt{2}(\boldsymbol{a}+$ b). 曲线

$$
C=\{P \mid \overrightarrow{O P}=\boldsymbol{a} \cos \theta+\boldsymbol{b} \sin \theta, 0 \leqslant \theta<2 \pi\}
$$

区域

$$
\Omega=\{P|0<r \leqslant| \overrightarrow{P Q} \mid \leqslant R, r<R\}
$$

若 $C \cap \Omega$ 为两段分离的曲线, 则
A. $1<r<R<3$
B. $1<r<3 \leqslant R$
C. $r \leqslant 1<R<3$
D. $1<r<3<R$

## 解析 A.

整个问题的条件和结论都与相对位置有关, 和绝对位置无关, 因此可以忽略平面直角坐标系 $x \mathrm{O} y$ 这一束缚.

如图, 长度均为 1 的有向线段 $\overrightarrow{O A} \perp \overrightarrow{O B}$, 分别代表 $\boldsymbol{a}$ 和 $\boldsymbol{b}$. 易得 $\overrightarrow{O Q}$ 在 $\angle A O B$ 的平分线上, 与 $\overrightarrow{O A}$ 和 $\overrightarrow{O B}$ 的夹角均为 $45^{\circ}$, 且 $|O Q|=2$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-058.jpg?height=257&width=254&top_left_y=2023&top_left_x=1522)

对于曲线 $C$, 注意到 $\overrightarrow{O P}$ 在 $\boldsymbol{a}$ 和 $\boldsymbol{b}$ 上的有向投影分别为 $\cos \theta$ 和 $\sin \theta$, 因此曲线 $C$ (即 $P$ 点的轨迹) 是以 $O$为圆心, 1 为半径的圆 (且 $\theta$ 为以 $\overrightarrow{O A}$ 为始边, $\overrightarrow{O P}$ 为终边的角), 记为圆 $O$.

对于区域 $\Omega$, 容易得到它表示以 $Q$ 为圆心, 外圆半径为 $R$, 内圆半径为 $r$ 的圆环内部 (包括内外边界).

于是 $C \cap \Omega$ 表示圆 $O$ 被 $\Omega$ 表示的圆环所截的部分, 为了保证它为两段分离的曲线, 需要圆环的内圆和外圆均与圆 $O$ 相交, 因此 $1<r<R<3$.

## 第 579 题 团团圆圆

在平面直角坐标系中, 圆 $C_{1}:(x+1)^{2}+(y-6)^{2}=25$, 圆 $C_{2}:(x-17)^{2}+(y-30)^{2}=r^{2}$. 若 $C_{2}$ 上存在一点 $P$ 可作一条射线与 $C_{1}$ 依次交于点 $A, B$, 满足 $|P A|=2|A B|$, 则半径 $r$ 的取值范围是

解析 $[5,55]$.

对任意一点 $P$, 考虑条件的含义.

若点 $P$ 在圆 $C_{1}$ 的内部 (含圆上时), 一定无法作出满足条件的射线;

若点 $P$ 在圆外, 当射线与圆相切时, 一定有 $|P A|>2|A B|$, 所以只需要存在一条射线使得 $|P A| \leqslant 2|A B|$, 则点 $P$ 满足要求. 当射线过圆 $C_{1}$的圆心时, $|P A|$ 有最小值 $\left|P C_{1}\right|-r,|A B|$ 有最大值 $2 r$, 当 $\left|P C_{1}\right|-r \leqslant$ $4 r$, 即 $\left|P C_{1}\right| \leqslant 5 r=25$ 时满足条件.

所以 $P$ 点的轨迹是以圆 $C_{1}$ 的圆心为圆心, 内外半径分别为 5 (不含) 和 25 (含)的圆环. 而 $\left|C_{2} C_{1}\right|=30$, 所以 $r \in[5,55]$. 如图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-059.jpg?height=547&width=549&top_left_y=598&top_left_x=1332)

## 第 580 题 椭圆的光学性质

证明: 从椭圆焦点出发的光线, 经过椭圆反射后反射光线必经过另一个焦点.

解析 如图, 设反射点为 $T$, 反射面为 $M N$.

利用同一法, 命题等价于证明若 $\angle M T F_{1}=\angle N T F_{2}$, 那么 $M N$ 为切线.

显然 $M N$ 上存在椭圆上的点 (点 $T$ ), 因此 $M N$ 或者与椭圆相切, 或者与椭圆相交. 我们只需要证明直线 $M N$ 上不存在除 $T$ 以外栯圆上的其他点.

用反证法, 假设直线 $M N$ 上存在除 $T$ 以外椭圆上的点 $P$, 则 $P F_{1}+P F_{2}=2 a$ (椭

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-059.jpg?height=289&width=353&top_left_y=1435&top_left_x=1526)
圆定义). 作点 $F_{2}$ 关于 $M N$ 对称的点 $F_{2}{ }^{\prime}$, 则 $F_{1}, T, F_{2}{ }^{\prime}$ 共线, 于是

$$
F_{1} F^{\prime}{ }_{2}=F_{1} T+T F_{2}=2 a
$$

于是 $P F_{1}+P F^{\prime}{ }_{2}>F_{1} F^{\prime}{ }_{2}=2 a$ (三角形两边之和大于第三边), 矛盾. 因此直线 $M N$ 上不存在除 $T$ 以外椭圆上的点, 也即直线 $M N$ 与椭圆相切.

综上所述, 原命题得证.

圆锥曲线的光学性质以及它的证明过程在处理圆锥曲线的切线问题时往往可以起到“出奇制胜”的效果.

## 第 581 题 三角形的内切圆

如图, 已知 $P$ 为椭圆 $\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$ 上一点, $F_{1}, F_{2}$ 分别为植圆的两个焦点, 圆 $M$ 为 $\triangle F_{1} P F_{2}$ 的内切圆圆心, 直线 $P M$ 交 $x$ 轴于点 $N$, 求 $\frac{P M}{M N}$的值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-060.jpg?height=458&width=526&top_left_y=431&top_left_x=1242)

解析 2 .

设 $\triangle M F_{1} F_{2}, \triangle M F_{1} P, \triangle M P F_{2}$ 的面积分别为 $S_{\triangle M F_{1} F_{2}}, S_{\triangle M F_{1} P}, S_{\triangle M P F_{2}}$, 则

$$
\frac{|P M|}{|M N|}=\frac{S_{\triangle M F_{1} P}+S_{\triangle M P F_{2}}}{S_{\triangle M F_{1} F_{2}}}=\frac{\left|P F_{1}\right|+\left|P F_{2}\right|}{\left|F_{1} F_{2}\right|}=\frac{2 a}{2 c}=2,
$$

其中 $a, c$ 分别为椭圆的长半轴长和短半轴长.

遇到内切圆时, 往往利用面积进行数量关系的转化.

## 第 582 题 内心遇上重山

如图 1, 已知 $\triangle A B C$ 中, $B(-1,0), C(1,0)$. 设点 $G, I$ 分别为 $\triangle A B C$ 的重心和内心, 且 $G I / / B C$, 求 $A$ 点的轨迹方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-060.jpg?height=202&width=338&top_left_y=1524&top_left_x=1410)

图 1

解析 解法一 如图 2 , 延长 $A I$ 交 $B C$ 于点 $D$.

根据重心和内心的性质, 有

$$
\frac{A B}{B D}=\frac{A C}{C D}=\frac{A I}{D I}=\frac{A G}{G O}=\frac{2}{1},
$$

于是

$$
\frac{A B+A C}{B D+D C}=2
$$

即 $A B+A C=4$.

因此所求点 $A$ 的轨迹方程为 $\frac{x^{2}}{4}+\frac{y^{2}}{2}=1, y \neq 0$.

解法二 由于 $G I / / B C$, 于是

$$
S_{\triangle I B C}=S_{\triangle G B C}=\frac{1}{3} S_{\triangle A B C}
$$

进而

$$
\frac{S_{\triangle A B C}}{S_{\triangle B B C}}=\frac{A B+B C+C A}{B C}=3 .
$$

于是 $A B+A C=2 B C=4$.

根据椭圆的定义可知, $A$ 点的轨迹方程为

$$
\frac{x^{2}}{4}+\frac{y^{2}}{3}=1, y \neq 0
$$

## 第 583 题 挖掘长度关系

(1) 如图 1, 已知椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的右焦点为 $F$, 过点 $F$ 的直线交椭圆于 $A, B$ 两点, 点 $C$是点 $A$ 关于原点 $O$ 的对称点, 若 $C F \perp A B$ 且 $C F=A B$, 则椭圆的离心率为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-061.jpg?height=345&width=473&top_left_y=942&top_left_x=468)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-061.jpg?height=410&width=380&top_left_y=912&top_left_x=1329)

图 2

(2) 如图 2, 已知双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a, b>0)$ 的右焦点为 $F$, 过点 $F$ 的直线交椭圆于 $A, B$ 两点, 点 $C$是点 $A$ 关于原点 $O$ 的对称点, 若 $C F \perp A B$ 且 $C F=F B$, 则双曲线的离心率为 $\qquad$ .

解析 (1) $\sqrt{6}-\sqrt{3} \quad(2) \frac{\sqrt{10}}{2}$

(1) 如图 3, 设左焦点为 $F^{\prime}, A F=x$, 则直角 $\triangle F^{\prime} A B$ 的三边都可以用 $a$, $x$ 表示, 分别为

$$
2 a-x, 2 a-x, 2 x
$$

于是有

$$
2 x=\sqrt{2}(2 a-x),
$$

解得 $x=2 a(\sqrt{2}-1)$, 从而有

$$
4 c^{2}=x^{2}+(2 a-x)^{2}=4 a^{2} \cdot(9-6 \sqrt{2}),
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-061.jpg?height=347&width=486&top_left_y=1678&top_left_x=1374)

图 3

求得离心率 $e=\sqrt{6}-\sqrt{3}$.

(2) 如图 4, 在直角 $\triangle F^{\prime} A B$ 中,有

$$
(2 a+x)^{2}+(2 a+2 x)^{2}=(4 a+x)^{2},
$$

解得 $x=a$. 与(1) 同理可得 $e=\frac{\sqrt{10}}{2}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-061.jpg?height=402&width=385&top_left_y=2137&top_left_x=1479)

图 4

## 第 584 题 探寻几何意义

求函数 $f(x)=\cos x+\sqrt{\cos ^{2} x-4 \sqrt{2} \cos x+4 \sin x+9}$ 的最大值与最小值.

解析 首先对函数 $f(x)$ 进行代数变形,以期挖掘几何意义:

$$
f(x)=\cos x+\sqrt{(\sqrt{2} \cos x-2)^{2}+(\sin x+2)^{2}}
$$

根号下的部分的几何意义比较明显, 即椭圆 $\frac{m^{2}}{2}+n^{2}=1$ 上的点 $P(\sqrt{2} \cos x, \sin x)$ 到点 $A(2,-2)$ 的距离,如图,那么剩下的 $\cos x$ 的几何意义是什么呢?

注意到椭圆的左准线为 $x=-2$, 离心率 $e=\frac{\sqrt{2}}{2}$, 于是点 $P$ 到左焦点的距离为

$$
P F_{1}=\frac{\sqrt{2}}{2}(\sqrt{2} \cos x+2)=\cos x+\sqrt{2}
$$

因此我们有

$$
f(x)=P F_{1}+P A-\sqrt{2} \geqslant F_{1} A-\sqrt{2}=\sqrt{13}-\sqrt{2} .
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-062.jpg?height=331&width=423&top_left_y=828&top_left_x=1350)

另一方面, 由椭圆的定义,有

$$
f(x)=\left(2 \sqrt{2}-P F_{2}\right)+P A-\sqrt{2}=P A-P F_{2}+\sqrt{2} \leqslant A F_{2}+\sqrt{2}=\sqrt{5}+\sqrt{2},
$$

于是函数的最大值与最小值分别为 $\sqrt{5}+\sqrt{2}$ 和 $\sqrt{13}-\sqrt{2}$.

## 第 585 题

设椭圆的方程为 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$, 线段 $P Q$ 是过左焦点 $F$ 且不与 $x$ 轴垂直的焦点弦. 若在左准线上存在点 $R$, 使 $\triangle P Q R$ 为正三角形, 求椭圆的离心率 $e$ 的取值范围, 并用 $e$ 表示直线 $P Q$ 的斜率.

解析 如图, 设弦 $P Q$ 的中点为 $M$, 且 $P, Q, M$ 在左准线上的投影分别为 $P_{1}, Q_{1}, M_{1}$.

设 $\left|P P_{1}\right|=m,\left|Q Q_{1}\right|=n$, 则 $|P F|=e m,|Q F|=e n$, 根据题意, 有

$$
|R M|=\frac{\sqrt{3}}{2}|P Q|=\frac{\sqrt{3}}{2}(m+n) e,
$$

于是由 $|R M|>\left|M_{1} M\right|$ (因为 $P Q$ 不垂直于 $x$ 轴) 可得

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-062.jpg?height=298&width=398&top_left_y=1827&top_left_x=1373)

$$
\frac{\sqrt{3}}{2}(m+n) e>\frac{1}{2}(m+n)
$$

从而可得椭圆的离心率的取值范围是 $\left(\frac{\sqrt{3}}{3}, 1\right)$.

设直线 $P Q$ 的倾斜大小为 $\theta$, 则

$$
\sin \theta=\cos \angle R M M_{1}=\frac{\left|M_{1} M\right|}{|R M|}=\frac{1}{e \sqrt{3}}
$$

于是直线 $P Q$ 的斜率为

$$
\tan \theta= \pm \frac{1}{\sqrt{3 e^{2}-1}}
$$

## 第 586 题 共线时的长度转化

如图 1 所示, 已知 $A, B$ 两点在椭圆 $C: \frac{x^{2}}{m}+y^{2}=1(m>1)$ 上, 直线 $A B$ 上两个不同的点 $P, Q$ 满足 $|A P|:|P B|=|A Q|:|Q B|$, 且点 $P$ 坐标为 $(1,0)$.

(1) 若 $m=2$, 求证:点 $Q$ 在椭圆准线上;

(2)若 $m$ 为大于 1 的常数, 求点 $Q$ 的轨迹方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-063.jpg?height=303&width=385&top_left_y=565&top_left_x=1451)

图 1

解析 (1) 若 $m=2$, 则 $P$ 点为右焦点. 过点 $Q$ 作 $x$ 轴的垂线 $l$, 过点 $A, B$ 作 $l$ 的垂线, 垂足分别为 $M, N$, 如图 2 所示,

则

$$
\frac{A Q}{Q B}=\frac{A M}{B N}=\frac{A P}{P B}
$$

由同一法容易证明 $l$ 为准线.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-063.jpg?height=307&width=353&top_left_y=962&top_left_x=1508)

图 2

(2) 设直线 $l$ 为 $\left\{\begin{array}{l}x=1+t, \\ y=k t\end{array}\right.$, 其中 $A, B, Q$ 对应的参数分别为 $t_{1}, t_{2}, t_{0}$, 则

$$
\left|\frac{t_{1}}{t_{2}}\right|=\left|\frac{t_{0}-t_{1}}{t_{0}-t_{2}}\right|
$$

易知 $\frac{t_{1}}{t_{2}} \neq \frac{t_{0}-t_{1}}{t_{0}-t_{2}}$, 所以 $\frac{t_{1}}{t_{2}}=\frac{t_{0}-t_{1}}{t_{2}-t_{0}}$, 即

$$
t_{0}=\frac{2 t_{1} t_{2}}{t_{1}+t_{2}}
$$

联立直线与椭圆, 有

$$
\frac{1}{m}(t+1)^{2}+k^{2} t^{2}-1=0
$$

即

$$
\left(k^{2}+\frac{1}{m}\right) t^{2}+\frac{2}{m} t+\frac{1}{m}-1=0,
$$

所以

$$
t_{0}=\frac{2\left(\frac{1}{m}-1\right)}{-\frac{2}{m}}=m-1
$$

于是点 $Q$ 的轨迹方程为 $x=m$.

## 第 587 题 简洁明 3

如图 1, 已知椭圆 $\Gamma$ 的一个焦点为 $F$, 与其对应的准线为 $l$. 直线 $A B$ 交椭圆 $\Gamma$ 于 $A, B$ 两点, 交准线 $l$ 于点 $C$. 直线 $A F$ 交准线 $l$ 于点 $D$. 求证: $F C$平分 $\angle B F D$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-064.jpg?height=418&width=428&top_left_y=468&top_left_x=1304)

图 1

解析 如图 2 , 过点 $A$ 作 $A M$ 垂直准线 $l$ 于点 $M$, 过点 $B$ 作 $B N$ 垂直准线 $l$于点 $N$.

因为

$$
\frac{|F A|}{|F B|}=\frac{|M A|}{|N B|}=\frac{|C A|}{|C B|}
$$

故 $F C$ 是 $\triangle F A B$ 中 $\angle A F B$ 的外角平分线, 即 $F C$ 平分 $\angle B F D$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-064.jpg?height=424&width=434&top_left_y=984&top_left_x=1331)

图 2

## 第 588 题 滑动的线段

已知两条直线 $l_{1}, l_{2}$ 相交于点 $O$, 点 $A$ 在直线 $l_{1}$ 上运动, 点 $B$ 在直线 $l_{2}$ 上运动, 且线段 $A B$ 的长为定值 $2 m$, 求 $A B$ 的中点 $M$ 的轨迹.

解析 如图建系, 设 $l_{1}, l_{2}$ 的夹角为 $2 \theta, k=\tan \theta$, 直线 $O A$ 和直线 $O B$ 的方程分别为 $y=k x$ 和 $y=-k x$.

设 $A(a, k a), B(b,-k b), M(x, y)$, 则

$$
2 x=a+b, 2 y=k(a-b)
$$

代人

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-064.jpg?height=238&width=441&top_left_y=1921&top_left_x=1328)

$$
(a-b)^{2}+k^{2}(a+b)^{2}=(2 m)^{2}
$$

中, 可得

$$
\frac{4 y^{2}}{k^{2}}+4 k^{2} x^{2}=4 m^{2}
$$

即

$$
k^{2} x^{2}+\frac{y^{2}}{k^{2}}=m^{2}
$$

## 第 589 题 数形结合解不等式

解不等式: $\sqrt{x^{2}+4 x+8}+\sqrt{x^{2}-4 x+8} \leqslant 6$.

解析 $\quad$ 原不等式即

$$
\sqrt{(x+2)^{2}+(2-0)^{2}}+\sqrt{(x-2)^{2}+(2-0)^{2}} \leqslant 6
$$

联想棙圆的定义,构造以 $F_{1}(-2,0), F_{2}(2,0)$ 为焦点, 6 为长轴长的植圆 $\frac{x^{2}}{9}+$ $\frac{y^{2}}{5}=1$. 如图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-065.jpg?height=300&width=374&top_left_y=557&top_left_x=1503)

于是所求 $x$ 的范围即直线 $y=2$ 被椭圆截得的弦 $M N$ 上的点的横坐标的取值范围, 即 $\left[-\frac{3}{\sqrt{5}}, \frac{3}{\sqrt{5}}\right]$.

注意将两个根式的和与椭圆的定义联系起来, 积累利用几何图形解决代数问题的经验.

改编 解不等式: $\sqrt{x^{2}+4 x+8}-\sqrt{x^{2}-4 x+8} \geqslant 2$.

解答 $\left[\frac{\sqrt{21}}{3},+\infty\right)$. 提示: 考虑双曲线 $x^{2}-\frac{y^{2}}{3}=1$ 与直线 $y=2$.

## 第 590 题 $\quad$ 联立三次又何妨

已知植圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的长轴长为 4 , 过左焦点 $F_{1}$ 且垂直于 $x$ 轴的直线被椭圆 $C$ 截得的线段长为 1 .

(1) 求椭圆 $C$ 的方程;

(2) 设点 $A$ 为椭圆的右顶点, 过点 $B(1,0)$ 作不与 $x$ 轴垂直的直线与椭圆 $C$ 相交于 $E, F$ 两点, 若直线 $A E, A F$ 分别与直线 $x=3$ 交于不同的两点

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-065.jpg?height=314&width=429&top_left_y=1554&top_left_x=1415)
$M, N$. 求 $\overrightarrow{E M} \cdot \overrightarrow{F N}$ 的取值范围.

解析 (1) 通径长为 1 , 于是由 $2 a=4, \frac{2 b^{2}}{a}=1$, 解得 $a=2, b=1$, 于是所求椭圆方程为 $\frac{x^{2}}{4}+y^{2}=1$.

(2) 设 $E\left(x_{1}, y_{1}\right), F\left(x_{2}, y_{2}\right), M(3, m), N(3, n)$, 直线 $E F: y=k(x-1)$, 其中 $k \neq 0$.

由 $E, A, M$ 和 $F, A, N$ 分别共线, 可以解得 $m=\frac{y_{1}}{x_{1}-2}, n=\frac{y_{2}}{x_{2}-2}$, 于是

$$
\begin{aligned}
\overrightarrow{E M} \cdot \overrightarrow{F N} & =\left(3-x_{1}\right)\left(3-x_{2}\right)+\left(m-y_{1}\right)\left(n-y_{2}\right) \\
& =\left(3-x_{1}\right)\left(3-x_{2}\right)+y_{1} y_{2} \cdot \frac{\left(3-x_{1}\right)\left(3-x_{2}\right)}{\left(x_{1}-2\right)\left(x_{2}-2\right)} \\
& =\left(x_{1}-3\right)\left(x_{2}-3\right) \cdot\left[1+k^{2} \cdot \frac{\left(x_{1}-1\right)\left(x_{2}-1\right)}{\left(x_{1}-2\right)\left(x_{2}-2\right)}\right]
\end{aligned}
$$

联立直线 $E F$ 与椭圆方程, 有

$$
x^{2}+4 k^{2}(x-1)^{2}-4=0
$$

分别令 $u=x-1, v=x-2, w=x-3$, 得

$$
\left\{\begin{array}{l}
\left(4 k^{2}+1\right) u^{2}+2 u-3=0 \\
\left(4 k^{2}+1\right) v^{2}+\left(8 k^{2}+4\right) v+4 k^{2}=0 \\
\left(4 k^{2}+1\right) w^{2}+\left(16 k^{2}+6\right) w+16 k^{2}+5=0
\end{array}\right.
$$

从而

$$
\left\{\begin{array}{l}
\left(x_{1}-1\right)\left(x_{2}-1\right)=-\frac{3}{4 k^{2}+1} \\
\left(x_{1}-2\right)\left(x_{2}-2\right)=\frac{4 k^{2}}{4 k^{2}+1} \\
\left(x_{1}-3\right)\left(x_{2}-3\right)=\frac{16 k^{2}+5}{4 k^{2}+1}
\end{array}\right.
$$

代人可得 $\overrightarrow{E M} \cdot \overrightarrow{F N}=1+\frac{1}{16 k^{2}+4}$, 于是 $\overrightarrow{E M} \cdot \overrightarrow{F N}$ 的取值范围为 $\left(1, \frac{5}{4}\right)$.

这种联立方式在求解与数量积有关的问题时往往可以起到简化运算的作用.

## 第 591 题 椭圆化圆

如图 1, 已知椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的一个焦点为 $F(2,0)$, 离心率为 $\frac{\sqrt{6}}{3}$. 过焦点 $F$ 的直线 $l$ 与植圆 $C$ 交于 $A, B$ 两点, 线段 $A B$ 的中点为 $D$, $O$ 为坐标原点, 过 $O, D$ 两点的直线交椭圆于 $M, N$ 两点.

(1) 求椭圆 $C$ 的方程;

(2)求四边形 $A M B N$ 面积的最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-066.jpg?height=290&width=404&top_left_y=1323&top_left_x=1326)

图 1

解析 (1) 容易求得枉圆 $C: \frac{x^{2}}{6}+\frac{y^{2}}{2}=1$;

(2)根据题意可得四边形 $A M B N$ 的面积

$$
S_{A M B N}=\frac{1}{2} \cdot A B \cdot M N \cdot \sin \langle A B, M N\rangle
$$

其中 $A B, M N$ 及 $\langle A B, M N\rangle$ 均随着直线 $l$ 的运动而改变.

考虑用伸缩变换将其拉成圆, 只需要将每个点的纵坐标变成原来的 $\sqrt{3}$ 倍, 横坐标不变即可, 如图 2 所示.

此时 $M^{\prime} N^{\prime}$ 为圆 $x^{\prime 2}+y^{\prime 2}=6$ 的直径为定值 $2 \sqrt{6}$, 而由垂径定理 $\left\langle A^{\prime} B^{\prime}\right.$, $\left.M^{\prime} N^{\prime}\right\rangle=\frac{\pi}{2}$ 亦为定值, 此时可得

$$
S_{A^{\prime} M^{\prime} B^{\prime} N^{\prime}}=\sqrt{6} A^{\prime} B^{\prime} \leqslant \sqrt{6} \cdot 2 \sqrt{6}=12
$$

等号当且仅当 $A^{\prime} B^{\prime}$ 为直径, 也即直线 $l: y=0$ 时取得, 此时四边形 $A M B N$ 的面积取得最大值

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-066.jpg?height=461&width=420&top_left_y=1963&top_left_x=1351)

图 2

$$
\frac{S_{A^{\prime} M^{\prime} B^{\prime} N^{\prime}}}{\sqrt{3}}=4 \sqrt{3}
$$

## 第 592 题 参数方程与仿射交换

一种作图工具如图 1 所示. $O$ 是滑槽 $A B$ 的中点,短杆 $O N$ 可绕 $O$转动, 长杆 $M N$ 通过 $N$ 处较链与 $O N$ 连接, $M N$ 上的栓子可沿滑槽 $A B$ 滑动,且 $D N=O N=1, M N=3$. 当栓子 $D$ 在滑槽 $A B$ 内作往复运动时,带动 $N$ 绕 $O$ 转动一周 ( $D$ 不动时, $N$ 也不动), $M$ 处的笔尖画出的曲线记为 $C$. 以 $O$ 为原点, $A B$ 所在的直线为 $x$ 轴建立平面直角坐标系.

(1)求曲线 $C$ 的方程;

(2) 设动直线 $l$ 与两定直线: $l_{1}: x-2 y=0$ 和 $l_{2}: x+2 y=0$ 分别交于

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-067.jpg?height=312&width=503&top_left_y=453&top_left_x=1332)

图 1 $P, Q$ 两点. 若直线 $l$ 总与曲线 $C$ 有且只有一个公共点, 试探究: $\triangle O P Q$ 的面积是否存在最小值? 若存在, 求出该最小值; 若不存在, 说明理由.

解析 (1) 设 $N(\cos \theta, \sin \theta)$, 则 $D(2 \cos \theta, 0)$, 于是由

$$
\overrightarrow{N M}=-\frac{3}{2} \overrightarrow{M D}
$$

得

$$
M\left(\frac{x_{N}-\frac{3}{2} x_{D}}{1-\frac{3}{2}}, \frac{y_{N}-\frac{3}{2} y_{D}}{1-\frac{3}{2}}\right)=M(4 \cos \theta,-2 \sin \theta)
$$

于是可得曲线 $C$ 的方程为

$$
\frac{x^{2}}{16}+\frac{y^{2}}{4}=1
$$

(2)存在最小值,最小值为 8 . 证明如下:

在伸缩变换

$$
\left\{\begin{array}{l}
x^{\prime}=x \\
y^{\prime}=2 y
\end{array}\right.
$$

下, 椭圆 $C$ 变为圆 $x^{\prime 2}+y^{\prime 2}=16$. 而在变换后直线 $l^{\prime}{ }_{1}$ 和 $l_{2}^{\prime}{ }_{2}$ 则变为互相垂直的直线 $x^{\prime}-y^{\prime}=0$ 和 $x^{\prime}+y^{\prime}=0$, 如图 2 所示.

记切点 $T$ 变换后对应的点为 $T^{\prime}$, 则 $P^{\prime} Q^{\prime}$ 与圆相切于点 $T^{\prime}$, 从而变换后的 $\triangle O P^{\prime} Q^{\prime}$ 的面积

$$
\begin{aligned}
S_{\triangle\left(P^{\prime} Q^{\prime}\right.} & =\frac{1}{2} O T^{\prime} \cdot P^{\prime} Q^{\prime} \\
& =2\left(P^{\prime} T^{\prime}+Q^{\prime} T^{\prime}\right) \\
& \geqslant 4 \sqrt{P^{\prime} T^{\prime} \cdot Q^{\prime} T^{\prime}} \\
& =16
\end{aligned}
$$

等号当 $P^{\prime} T^{\prime}=Q^{\prime} T^{\prime}$ 时取得. 因此 $\triangle O P Q$ 的面积

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-067.jpg?height=459&width=462&top_left_y=1723&top_left_x=1418)

图 2

$$
S_{\triangle O P Q}=\frac{1}{2} S_{\triangle \triangle P^{\prime} Q^{\prime}} \geqslant 8
$$

于是其最小值存在, 且为 8.

## 第 593 题 化椭为圆

如图 1,在平面直角坐标系 $x O y$ 中, 已知椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b$ $>0)$ 的离心率为 $\frac{\sqrt{3}}{2}$, 左、右焦点分别是 $F_{1}, F_{2}$. 以 $F_{1}$ 为圆心, 以 3 为半径的圆与以 $F_{2}$ 为圆心, 以 1 为半径的圆相交, 且交点在椭圆 $C$ 上.

(1) 求椭圆 $C$ 的方程;

(2) 设椭圆 $E: \frac{x^{2}}{4 a^{2}}+\frac{y^{2}}{4 b^{2}}=1, P$ 为椭圆 $C$ 上任意一点, 过点 $P$ 的直

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-068.jpg?height=322&width=503&top_left_y=456&top_left_x=1245)

图 1 线 $y=k x+m$ 交椭圆 $E$ 于 $A, B$ 两点,射线 $P O$ 交椭圆 $E$ 于点 $Q$.

(1) 求 $\frac{|O Q|}{|O P|}$ 的值;

(2)求 $\triangle A B Q$ 面积的最大值.

解析 (1) 由椭圆的定义可得 $2 a=4$, 进而可以求得椭圆 $C$ 的方程为

$$
\frac{x^{2}}{4}+y^{2}=1
$$

(2) (1) 由 (1) 的结论, 可得椭圆 $E: \frac{x^{2}}{16}+\frac{y^{2}}{4}=1$.

设 $\overrightarrow{O Q}=\lambda \overrightarrow{O P}(\lambda<0), P\left(x_{0}, y_{0}\right)$, 则 $Q\left(\lambda x_{0}, \lambda y_{0}\right)$.

由于 $P, Q$ 两点分别在椭圆 $C, E$ 上, 因此

$$
\frac{x_{0}^{2}}{4}+y_{0}^{2}=1, \frac{\left(\lambda x_{0}\right)^{2}}{16}+\frac{\left(\lambda y_{0}\right)^{2}}{4}=1,
$$

两式相除, 解得 $\lambda=-2$, 因此

$$
\frac{|O Q|}{|O P|}=|\lambda|=2
$$

(2)注意到在运动过程中, $Q O$ 与 $O P$ 的比始终不变 (第(1)小问中的结论), 于是可以得到

$$
S_{\triangle A B Q}=3 S_{\triangle A B O},
$$

这样原来的动点 $Q$ 就转化成了现在的定点 $Q$, 如图 2 所示.

作保持横坐标不变, 纵坐标变为原来的 2 倍的伸缩变换 $\left\{\begin{array}{l}x^{\prime}=x, \\ y^{\prime}=2 y,\end{array}\right.$ 则椭圆 $E$ 变

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-068.jpg?height=240&width=357&top_left_y=1704&top_left_x=1416)

图 2 为圆 $E^{\prime}: x^{\prime 2}+y^{\prime 2}=16$, 椭圆 $C$ 变为圆 $C^{\prime}: x^{\prime 2}+y^{\prime 2}=4$, 与此同时, $\triangle A^{\prime} B^{\prime} O$ 的面积为 $\triangle A B O$ 面积的 2 倍, 如图 3 所示.

设原点 $O$ 到弦 $A^{\prime} B^{\prime}$ 的距离为 $d$, 则由弦 $A^{\prime} B^{\prime}$ 与圆 $C^{\prime}$ 有公共点可得 $d$ 的取值范围是 $(0,2]$, 于是在圆 $E^{\prime}$ 中应用垂径定理求弦长

$$
\left|A^{\prime} B^{\prime}\right|=2 \sqrt{4^{2}-d^{2}}
$$

进而

$$
S_{\triangle A^{\prime} B^{\prime} O}=\frac{1}{2} \cdot\left|A^{\prime} B^{\prime}\right| \cdot d=\sqrt{d^{2}\left(16-d^{2}\right)},
$$

结合 $d$ 的取值范围可得 $S_{\triangle A^{\prime} B^{\prime} O}$ 的最大值为 $4 \sqrt{3}$, 进而可得 $S_{\triangle A B O}$ 的最大值为 $2 \sqrt{3}$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-068.jpg?height=355&width=314&top_left_y=2138&top_left_x=1459)

图 3 于是 $S_{\triangle A B Q}$ 的最大值为 $6 \sqrt{3}$.

## 第 594 题 寻找定点

已知棙圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的离心率 $e=\frac{1}{2}$, 过焦点且垂直于 $x$ 轴的直线被栯圆截得的线段长为 3 .

(1)求椭圆的方程;

(2) 斜率为 $\frac{1}{2}$ 的动直线 $l$ 与椭圆交于 $A, B$ 两点, 在平面上是否存在定点 $P$, 使得当直线 $P A$ 与直线 $P B$ 的斜率均存在时, 斜率之和是与 $l$ 无关的常数? 若存在, 求出所有满足条件的定点 $P$ 的坐标; 若不存在, 请说明理由.

解析 解法一 (1)根据题意, 通径长 $\frac{2 b^{2}}{a}=3$, 于是椭圆的方程为 $\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$.

(2) 设定点 $P$ 的坐标为 $(m, n)$, 平移坐标系, 使 $P$ 点为坐标原点, 则椭圆方程变为

$$
\frac{\left(x^{\prime}+m\right)^{2}}{4}+\frac{\left(y^{\prime}+n\right)^{2}}{3}=1
$$

当 $l$ 不过点 $P^{\prime}$ 时, 设动直线的方程为 $t\left(x^{\prime}-2 y^{\prime}\right)=1$, 则联立直线与椭圆方程, 有

$$
\frac{1}{4} x^{\prime 2}+\frac{1}{3} y^{\prime 2}+\left(\frac{m}{2} x^{\prime}+\frac{2 n}{3} y^{\prime}\right) \cdot t\left(x^{\prime}-2 y^{\prime}\right)+\left(\frac{1}{4} m^{2}+\frac{1}{3} n^{2}-1\right) \cdot t^{2}\left(x^{\prime}-2 y^{\prime}\right)^{2}=0
$$

整理得 $y^{\prime 2}$ 的系数为

$$
\frac{1}{3}-\frac{4 n}{3} t+\left(\frac{1}{4} m^{2}+\frac{1}{3} n^{2}-1\right) \cdot 4 t^{2}
$$

而 $x^{\prime} y^{\prime}$ 的系数为

$$
\left(\frac{2 n}{3}-m\right) t-\left(\frac{1}{4} m^{2}+\frac{1}{3} n^{2}-1\right) \cdot 4 t^{2}
$$

根据题意, 直线 $P^{\prime} A^{\prime}$ 与直线 $P^{\prime} B^{\prime}$ 的斜率之和

$$
-\frac{\left(\frac{2 n}{3}-m\right) t-\left(\frac{1}{4} m^{2}+\frac{1}{3} n^{2}-1\right) \cdot 4 t^{2}}{\frac{1}{3}-\frac{4 n}{3} t+\left(\frac{1}{4} m^{2}+\frac{1}{3} n^{2}-1\right) \cdot 4 t^{2}}
$$

为定值. 于是

$$
\frac{2 n}{3}-m=\frac{1}{4} m^{2}+\frac{1}{3} n^{2}-1=0
$$

解得 $m=1, n=\frac{3}{2}$ 或 $m=-1, n=-\frac{3}{2}$. 对应的 $P$ 点在椭圆上, 于是不需要考虑 $l$ 过点 $P$ 的情形.

综上所述,所有满足条件的定点 $P$ 的坐标为 $\left(1, \frac{3}{2}\right)$ 或 $\left(-1,-\frac{3}{2}\right)$.

解法二 (1) 见解法一.

(2) 将椭圆仿射为圆, 则直线 $A^{\prime} B^{\prime}$ 的斜率为 $\frac{\sqrt{3}}{3}$, 于是点 $Q^{\prime}(-1, \sqrt{3})$ 始终平分弧 $A^{\prime} B^{\prime}$, 进而可取 $P^{\prime}(1$, $\sqrt{3})$, 此时 $\angle A^{\prime} P^{\prime} Q^{\prime}=\angle B^{\prime} P^{\prime} Q^{\prime}$, 因此直线 $P^{\prime} A^{\prime}$ 与直线 $P^{\prime} B^{\prime}$ 的斜率始终互为相反数, 符合题意.

解法三 (1) 见解法一.

(2) 设 $l: y=\frac{1}{2} x+t$, 与椭圆方程联立得

$$
x^{2}+t x+t^{2}-3=0
$$

设 $A\left(x_{1}, \frac{1}{2} x_{1}+t\right), B\left(x_{2}, \frac{1}{2} x_{2}+t\right)$, 则有

$$
x_{1}+x_{2}=-t, x_{1} x_{2}=t^{2}-3 .
$$

直线 $P A, P B$ 的斜率之和

$$
\begin{aligned}
k_{P A}+k_{P B} & =\frac{\left(m-\frac{1}{2} x_{1}-t\right)\left(m-x_{2}\right)+\left(n-\frac{1}{2} x_{2}-t\right)\left(m-x_{1}\right)}{\left(m-x_{1}\right)\left(m-x_{2}\right)} \\
& =\frac{\left(n-\frac{3}{2} m\right) t+2 m n-3}{t^{2}+m t+m^{2}-3}
\end{aligned}
$$

当 $n=\frac{3}{2} m, 2 m n=3$ 时斜率的和恒为 0 , 解得

$$
\left\{\begin{array} { l } 
{ m = 1 , } \\
{ n = \frac { 3 } { 2 } }
\end{array} \text { 或 } \left\{\begin{array}{l}
m=-1, \\
n=-\frac{3}{2} .
\end{array}\right.\right.
$$

综上所述, 所有满足条件的定点 $P$ 的坐标为 $\left(1, \frac{3}{2}\right)$ 或 $\left(-1,-\frac{3}{2}\right)$.

## 第 595 题 面积之比

已知椭圆 $C_{1}: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的离心率为 $\frac{\sqrt{2}}{2}$, 其短轴的下端点在抛物线 $x^{2}=4 y$ 的准线上. 设 $O$ 为坐标原点, $M$ 是直线 $l: x=2$ 上的动点, $F$ 为椭圆的右焦点, 过点 $F$ 作 $O M$ 的垂线与以 $O M$ 为直径的圆 $C_{2}$ 相交于 $P, Q$ 两点,与椭圆 $C_{1}$ 相交于 $A, B$ 两点, 如图 1 所示.

(1) 求椭圆 $C_{1}$ 的方程.

(2)若 $|P Q|=\sqrt{6}$, 求圆 $C_{2}$ 的方程;

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-070.jpg?height=338&width=461&top_left_y=1162&top_left_x=1286)

图 1

(3) 设 $C_{2}$ 与四边形 $O A M B$ 的面积分别为 $S_{1}, S_{2}$, 若 $S_{1}=\lambda S_{2}$, 求 $\lambda$ 的取值范围.

解析 解法一 (1) 由题意得

$$
\left\{\begin{array}{l}
\frac{c}{a}=\frac{\sqrt{2}}{2} \\
b=1
\end{array}\right.
$$

又 $a^{2}=b^{2}+c^{2}$, 所以解得 $a=\sqrt{2}, b=1$.

故椭圆方程为 $\frac{x^{2}}{2}+y^{2}=1$.

(2) 设 $O M$ 与 $P Q$ 交于 $E$ 点, $H(2,0)$. 如图 2 所示.

由于 $\triangle O E F$ 与 $\triangle O H M$ 相似,于是

$$
|O E| \cdot|O M|=|O F| \cdot|O H|=2
$$

又根据相交弦定理, 有

$$
|O E| \cdot|E M|=|P E| \cdot|E Q|=\frac{3}{2}
$$

于是有

$$
|O E| \cdot|O E|=\frac{1}{2}
$$

从而解得 $O M=2 \sqrt{2}$, 因此 $M(2, \pm 2)$, 进而可得圆 $C_{2}$ 的方程为

$$
(x-1)^{2}+(y \pm 1)^{2}=2
$$

(3)根据题意，有

$$
\lambda=\frac{S_{1}}{S_{2}}=\frac{\pi \cdot\left(\frac{1}{2}|O M|\right)^{2}}{\frac{1}{2} \cdot|A B| \cdot|O M|}=\frac{\pi}{2} \cdot \frac{|O M|}{|A B|}
$$

设直线 $P Q$ 的倾斜角为 $\theta$,则

$$
|A B|=\frac{2 a b^{2}}{b^{2}+c^{2} \sin ^{2} \theta}=\frac{2 \sqrt{2}}{1+\sin ^{2} \theta}
$$

而

$$
|O M|=\frac{|O H|}{\sin \theta}=\frac{2}{\sin \theta}
$$

这样就有

$$
\lambda=\frac{\pi}{2} \cdot \frac{1+\sin ^{2} \theta}{\sqrt{2} \cdot \sin \theta}=\frac{\pi}{2 \sqrt{2}}\left(\sin \theta+\frac{1}{\sin \theta}\right)
$$

从而其取值范围是 $\left[\frac{\sqrt{2}}{2} \pi,+\infty\right)$.

解法二 $(1)$ 见解法一.

(2) 设点 $M(2,2 m)$, 则直线 $P Q$ 的方程为 $x+m y-1=0$, 圆心 $(1, m)$ 到直线 $P Q$ 的距离

$$
d=\frac{\left|1+m^{2}-1\right|}{\sqrt{1+m^{2}}}=\frac{m^{2}}{\sqrt{1+m^{2}}}
$$

于是由弦心距、半弦长与半径得到的三角形三边关系满足

$$
\frac{m^{4}}{1+m^{2}}+\left(\frac{\sqrt{6}}{2}\right)^{2}=1+m^{2}
$$

解得 $m^{2}=1$, 所以 $m= \pm 1$, 从而圆 $C_{2}$ 的方程为

$$
(x-1)^{2}+(y \pm 1)^{2}=2
$$

(3) 因为

$$
S_{1}=\pi\left(1+m^{2}\right), S_{2}=\frac{1}{2} \cdot|O M| \cdot|A B|=\sqrt{1+m^{2}}|A B|
$$

联立直线 $P Q$ 与椭圆的方程消去 $x$ 得

$$
\left(m^{2}+2\right) y^{2}-2 m y-1=0,
$$

于是有

$$
|A B|=\sqrt{1+m^{2}} \cdot \frac{\sqrt{\Delta}}{m^{2}+2}=\frac{2 \sqrt{2}\left(m^{2}+1\right)}{m^{2}+2}
$$

于是

$$
\lambda=\frac{S_{1}}{S_{2}}=\frac{\sqrt{2}}{4} \pi \cdot \sqrt{\left(m^{2}+1\right)+\frac{1}{m^{2}+1}+2} \geqslant \frac{\sqrt{2}}{2} \pi
$$

当且仅当 $m=0$ 时等号成立.

因此 $\lambda$ 的取值范围是 $\left[\frac{\sqrt{2}}{2} \pi,+\infty\right)$.

## 第 596 题 合理表达条件

在直角坐标系中, 粗圆 $C_{1}: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的左、右焦点分别为 $F_{1}, F_{2}$, 其中 $F_{2}$ 也是抛物线 $C_{2}: y^{2}=4 x$ 的焦点, 点 $P$ 为 $C_{1}$ 与 $C_{2}$ 在第一象限的交点, 且 $\left|P F_{2}\right|=\frac{5}{3}$.

(1)求椭圆的方程;

(2) 过点 $F_{2}$ 且与坐标轴不垂直的直线交椭圆于 $M, N$ 两点, 线段 $O F_{2}$ 上存在点 $T(t, 0)$ 使得以 $T M, T N$ 为邻边的四边形是菱形, 求 $t$ 的取值范围.

解析 (1) 设 $P\left(x_{0}, y_{0}\right)$, 由题意得

$$
\left\{\begin{array}{l}
\frac{x_{0}^{2}}{a^{2}}+\frac{y_{0}^{2}}{b^{2}}=1 \\
y_{0}^{2}=4 x_{0} \\
\left(x_{0}-c\right)^{2}+y_{0}^{2}=\left(\frac{5}{3}\right)^{2} \\
c=1
\end{array}\right.
$$

又有 $a^{2}=b^{2}+c^{2}$, 解得 $a=2, b=\sqrt{3}$.

(2) 根据题意, $T$ 点横坐标 $t$ 为线段 $M N$ 的垂直平分线的横截距, 设直线 $M N$ 的中点为 $P(m, n)$, 则

$$
\left\{\begin{array}{l}
\frac{n}{m} \cdot \frac{n}{m-1}=-\frac{3}{4} \\
\frac{n}{m-t} \cdot \frac{n}{m-1}=-1
\end{array}\right.
$$

解得 $m=4 t, n^{2}=-12 t^{2}+3 t$, 于是

$$
\left\{\begin{array}{l}
n^{2}=-12 t^{2}+3 t>0 \\
\frac{m^{2}}{4}+\frac{n^{2}}{3}<1 \\
0 \leqslant t \leqslant 1
\end{array}\right.
$$

解得 $t$ 的取值范围是 $\left(0, \frac{1}{4}\right)$.

## 第 597 题 兵分三路证对称

已知椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的短轴长为 $2 \sqrt{3}$, 右焦点为 $F(1,0)$, 点 $M$ 是椭圆 $C$ 上异于左、右顶点 $A, B$ 的一点.

(1) 求栯圆 $C$ 的方程;

(2) 若直线 $A M$ 与直线 $x=2$ 交于点 $N$, 线段 $B N$ 的中点为 $E$. 证明: 点 $B$ 关于直线 $E F$ 的对称点在直线 $M F$ 上.

解析 解法一 (1) $\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$;

(2) 如图, 作椭圆 $C$ 的右准线 $x=4$, 作 $M H$ 垂直右准线 $x=4$ 于点 $H$. 设直线 $A M$ 交右准线 $x=4$ 于点 $G$, 设直线 $F G$ 交直线 $x=2$ 于点 $E_{1}$, 因为

$$
\frac{|F A|}{|F M|}=\frac{|D A|}{|H M|}=\frac{|G A|}{|G M|}
$$

所以 $F G$ 是 $\triangle F A M$ 中 $\angle A F M$ 的外角平分线, 即 $F G$ 平分 $\angle B F M$.注意到

$$
\frac{\left|E_{1} B\right|}{|G D|}=\frac{1}{3}, \frac{|N B|}{|G D|}=\frac{2}{3}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-073.jpg?height=364&width=465&top_left_y=198&top_left_x=1414)

故点 $E_{1}$ 与点 $E$ 重合, 所以 $F E$ 平分 $\angle B F M$, 进而点 $B$ 关于直线 $E F$ 的对称点在直线 $M F$ 上.

## 解法二 (1) 见解法一.

(2)根据椭圆的垂径定理的推论, 可设

$$
A M: x=\frac{1}{k} y-2, B M: x=-\frac{4 k}{3} y+2,
$$

于是可得

$$
M\left(\frac{6-8 k^{2}}{3+4 k^{2}}, \frac{12 k}{3+4 k^{2}}\right)
$$

因此直线 $M F$ 的斜率为

$$
\frac{\frac{12 k}{3+4 k^{2}}}{\frac{6-8 k^{2}}{3+4 k^{2}}-1}=\frac{4 k}{1-4 k^{2}}=\frac{2 \cdot(2 k)}{1-(2 k)^{2}}
$$

而直线 $E F$ 的斜率为 $2 k$, 因此命题得证.

解法三 (1) 见解法一.

(2)利用仿射变换不难证明直线 $M E$ 与椭圆相切. 设直线 $M E$ 与 $x$ 轴相交于点 $T$, 利用椭圆的极点极线性质可得 $M$ 点的横坐标 $x_{M}$ 与 $T$ 点的横坐标 $x_{T}$ 满足

$$
x_{M} \cdot x_{T}=4
$$

而

$$
\begin{aligned}
\angle M F E=\angle B F E & \Leftarrow \frac{M E}{E F}=\frac{F M}{F T} \\
& \Leftarrow \frac{2-x_{M}}{x_{T}-2}=\frac{2-\frac{1}{2} x_{M}}{x_{T}-1} \\
& \leftarrow x_{M} \cdot x_{T}=4
\end{aligned}
$$

因此原命题得证.

## 第 598 题 何以解忧? 唯有参方

已知椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的离心率为 $\frac{\sqrt{3}}{2}$, 直线 $y=\frac{1}{2} x+1$ 与椭圆交于 $A, B$ 两点, 点 $M$ 在椭圆上, $\overrightarrow{O M}=\frac{1}{2} \overrightarrow{O A}+\frac{\sqrt{3}}{2} \overrightarrow{O B}$, 求椭圆方程.

解析 由于离心率为 $\frac{\sqrt{3}}{2}$, 于是 $a^{2}=4 b^{2}$, 因此可设 $A(2 b \cos \alpha, b \sin \alpha), B(2 b \cos \beta, b \sin \beta)$.

于是由 $\overrightarrow{O M}=\frac{1}{2} \overrightarrow{O A}+\frac{\sqrt{3}}{2} \overrightarrow{O B}$ 可得

$$
M\left(b \cdot(\cos \alpha+\sqrt{3} \cos \beta), b\left(\frac{1}{2} \sin \alpha+\frac{\sqrt{3}}{2} \sin \beta\right)\right)
$$

又点 $M$ 在椭圆上,于是可得

$$
\frac{(\cos \alpha+\sqrt{3} \cos \beta)^{2}}{4}+\frac{(\sin \alpha+\sqrt{3} \sin \beta)^{2}}{4}=1,
$$

化简得

$$
\cos (\alpha-\beta)=0
$$

另一方面, 点 $A$ 在直线 $y=\frac{1}{2} x+1$ 上, 可得

$$
b \sin \alpha=\frac{1}{2} \cdot 2 b \cos \alpha+1
$$

即

$$
\frac{1}{b}=\sin \alpha-\cos \alpha
$$

类似的, 有 $\frac{1}{b}=\sin \beta-\cos \beta$. 因此有

$$
\begin{aligned}
\frac{1}{b^{2}} & =(\sin \alpha-\cos \alpha)(\sin \beta-\cos \beta) \\
& =\cos (\alpha-\beta)-\sin (\alpha+\beta) \\
& =-\sin (\alpha+\beta)
\end{aligned}
$$

而同时

$$
\sin \alpha-\sin \beta=\cos \alpha-\cos \beta
$$

由和差化积可得 $\tan \frac{\alpha+\beta}{2}=-1$, 代人上式可得 $b^{2}=1$,

于是所求的椭圆方程为 $\frac{x^{2}}{4}+y^{2}=1$.


#### Abstract

思考与总结 有时候可以利用参数方程转化问题后, 利用丰富的三角公式帮助我们进行推理计算. 另外, 本题也可以利用仿射变换求解.


# 第 599 题 椭圆与矩形 

设 $A, B, C$ 是椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 上的三个点, 判断四边形 $O A B C$ 能否为矩形.

解析 解法一 设 $A(a \cos \alpha, b \sin \alpha), C(a \cos \beta, b \sin \beta), B(a \cos \alpha+a \cos \beta, b \sin \alpha+b \sin \beta)$,则由点 $B$ 在椭圆上有

$$
\frac{(a \cos \alpha+a \cos \beta)^{2}}{a^{2}}+\frac{(b \sin \alpha+b \sin \beta)^{2}}{b^{2}}=1
$$

于是

$$
\cos \alpha \cos \beta+\sin \alpha \sin \beta=-\frac{1}{2}
$$

又 $O A \perp O C$, 于是

$$
a^{2} \cos \alpha \cos \beta+b^{2} \sin \alpha \sin \beta=0
$$

## 高考数学满分学霸的解题笔记(一千零一影)

于是

$$
\cos \alpha \cos \beta=\frac{b^{2}}{2\left(a^{2}-b^{2}\right)}, \sin \alpha \sin \beta=-\frac{a^{2}}{2\left(a^{2}-b^{2}\right)}
$$

从而

$$
\cos (\alpha+\beta)=\frac{b^{2}+a^{2}}{2\left(a^{2}-b^{2}\right)}
$$

因此当 $a, b$ 满足

$$
-1 \leqslant \frac{b^{2}+a^{2}}{2\left(a^{2}-b^{2}\right)} \leqslant 1
$$

即 $a^{2} \geqslant 3 b^{2}$ 时, 四边形 $O A B C$ 可以为矩形, 也即当椭圆的离心率不小于 $\frac{\sqrt{6}}{3}$ 时, 四边形 $O A B C$ 可能为矩形,如图 1 所示.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-075.jpg?height=223&width=336&top_left_y=478&top_left_x=1519)

图 1

当椭圆的离心率为 $\frac{\sqrt{6}}{3}$ 时, 矩形 $O A B C$ 恰好为正方形.

解法二 如图 2, 连结 $A C, O B$ 且 $A C$ 与 $O B$ 相交于点 $M$.

由于点 $M$ 平分 $O B$, 于是点 $M$ 的轨迹是以原点为中心, 对椭圆 $E$ 按 $2: 1$ 的比例缩小后得到的椭圆, 记为 $E^{\prime}$.

又由于点 $M$ 平分 $A C$, 于是直线 $A C$ 与椭圆 $E^{\prime}$ 相切于点 $M$.

接下来考虑 $\frac{O C}{O M}$, 由于当 $M$ 从 $x$ 轴正半轴向 $y$ 轴正半轴运动时, $O M$ 单调递减,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-075.jpg?height=232&width=333&top_left_y=965&top_left_x=1523)

图 2

$A C$ 单调递增, 因此 $\frac{A C}{2 \cdot O M}$ 的取值范围是 $\left[\frac{\sqrt{3} b}{a}, \frac{\sqrt{3} a}{b}\right]$.

因此当 $a \geqslant \sqrt{3} b$ 时, 存在符合题意的矩形.

当椭圆的离心率为 $\frac{\sqrt{6}}{3}$ 时, 矩形 $O A B C$ 恰好为正方形.

## 第 600 题 椭圆的参数方程

已知椭圆 $C: \frac{x^{2}}{4}+\frac{y^{2}}{3}=1$, 斜率为 1 的直线 $l$ 与椭圆交于 $A, B$ 两点, 点 $M(4,0)$, 直线 $A M$ 与椭圆 $C$ 交于点 $A_{1}$, 直线 $B M$ 与椭圆交于点 $B_{1}$, 求证:直线 $A_{1} B_{1}$ 恒过定点.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-075.jpg?height=303&width=448&top_left_y=1803&top_left_x=1389)

解析 设 $A(2 \cos 2 \alpha, \sqrt{3} \sin 2 \alpha), B(2 \cos 2 \beta, \sqrt{3} \sin 2 \beta), A_{1}\left(2 \cos 2 \alpha_{1}, \sqrt{3} \sin 2 \alpha_{1}\right), B_{1}\left(2 \cos 2 \beta_{1}, \sqrt{3} \sin 2 \beta_{1}\right)$,于是直线 $A B$ 的斜率为 1 等价于

$$
-\frac{\sqrt{3}}{2} \cdot \frac{1}{\tan (\alpha+\beta)}=1 \text {, 即 } \tan (\alpha+\beta)=-\frac{\sqrt{3}}{2} \text {. }
$$

而直线 $A A_{1}$ 和直线 $B B_{1}$ 均过点 $M(4,0)$, 因此

$$
\tan \alpha \cdot \tan \alpha_{1}=\tan \beta \cdot \tan \beta_{1}=\frac{1}{3}
$$

这样就有

$$
\tan (\alpha+\beta)=\frac{\frac{1}{3 \tan \alpha_{1}}+\frac{1}{3 \tan \beta_{1}}}{1-\frac{1}{3 \tan \alpha_{1}} \cdot \frac{1}{3 \tan \beta_{1}}}=-\frac{\sqrt{3}}{2}
$$

整理得

$$
6\left(\tan \alpha_{1}+\tan \beta_{1}\right)=-9 \sqrt{3} \tan \alpha_{1} \cdot \tan \beta_{1}+\sqrt{3}
$$

考虑到直线 $A_{1} B_{1}$ 的方程为

$$
\left(1-\tan \alpha_{1} \cdot \tan \beta_{1}\right) \cdot \frac{x}{2}+\left(\tan \alpha_{1}+\tan \beta_{1}\right) \cdot \frac{y}{\sqrt{3}}=1+\tan \alpha_{1} \cdot \tan \beta_{1}
$$

即

$$
\frac{y}{\sqrt{3}}\left(\tan \alpha_{1}+\tan \beta_{1}\right)=\left(1+\frac{x}{2}\right) \tan \alpha_{1} \cdot \tan \beta_{1}+1-\frac{x}{2}
$$

由

$$
\frac{y}{\sqrt{3}}: 6=\left(1+\frac{x}{2}\right):(-9 \sqrt{3})=\left(1-\frac{x}{2}\right): \sqrt{3},
$$

解得

$$
x=\frac{5}{2}, y=-\frac{3}{2}
$$

因此直线 $A_{1} B_{1}$ 恒过点 $\left(\frac{5}{2},-\frac{3}{2}\right)$.

## 第 601 题 多直线定点定值问题

已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1, x$ 轴上有不同于长轴端点的两点 $M(m, 0)$ 和 $N(n$, $0)$, 过点 $M$ 作直线 $A B$ 与椭圆 $E$ 交于点 $A, B$, 直线 $A N$ 和直线 $B N$ 分别交椭圆 $E$ 于点 $C, D$, 求证: 直线 $A B$ 与直线 $C D$ 的斜率之比为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-076.jpg?height=218&width=355&top_left_y=1342&top_left_x=1391)

解析 设 $A\left(a \cos 2 \theta_{1}, b \sin 2 \theta_{1}\right), B\left(a \cos 2 \theta_{2}, b \sin 2 \theta_{2}\right), C\left(a \cos 2 \theta_{3}, b \sin 2 \theta_{3}\right), D\left(a \cos 2 \theta_{4}, b \sin 2 \theta_{4}\right)$, 则由椭圆参数方程相关的结论知

$$
\tan \theta_{1} \cdot \tan \theta_{2}=\frac{m-a}{m+a}, \tan \theta_{1} \cdot \tan \theta_{3}=\tan \theta_{2} \cdot \tan \theta_{4}=\frac{n-a}{n+a}
$$

于是直线 $A B$ 与直线 $C D$ 的斜率之比

$$
\begin{aligned}
\frac{k_{A B}}{k_{C D}}= & \frac{-\frac{b}{a} \cdot \frac{1-\tan \theta_{1} \cdot \tan \theta_{2}}{\tan \theta_{1}+\tan \theta_{2}}}{-\frac{b}{a} \cdot \frac{1-\tan \theta_{3} \cdot \tan \theta_{4}}{\tan \theta_{3}+\tan \theta_{4}}} \\
= & \frac{\tan \theta_{3}+\tan \theta_{4}}{\tan \theta_{1}+\tan \theta_{2}} \cdot \frac{1-\tan \theta_{1} \cdot \tan \theta_{2}}{1-\tan \theta_{3} \cdot \tan \theta_{4}} \\
= & \frac{\frac{n-a}{n+a} \cdot \frac{\tan \theta_{1}+\tan \theta_{2}}{\tan \theta_{1} \cdot \tan \theta_{2}}}{\tan \theta_{1}+\tan \theta_{2}} \cdot \frac{1-\tan \theta_{1} \cdot \tan \theta_{2}}{1-\left(\frac{n-a}{n+a}\right)^{2} \cdot \frac{1}{\tan \theta_{1} \cdot \tan \theta_{2}}} \\
= & \frac{\frac{n-a}{n+a}}{\frac{m-a}{m+a}} \cdot \frac{1-\frac{m-a}{m+a}}{1-\left(\frac{n-a}{n+a}\right)^{2} \cdot \frac{m+a}{m-a}} \\
= & \frac{n^{2}-a^{2}}{2 m n-n^{2}-a^{2}},
\end{aligned}
$$

为定值.
椭圆的参数方程是处理这类多条直线的定点定值问题的有效手段.

## 第 602 题 双弦

如图, 已知 $P$ 为椭圆 $E: \frac{x^{2}}{4}+y^{2}=1$ 的下顶点, 过点 $P$ 作互相垂直的两条直线 $l_{1}, l_{2}$, 直线 $l_{1}$ 与圆 $x^{2}+y^{2}=4$ 相交于 $A, B$ 两点, 直线 $l_{2}$ 与椭圆 $E$ 交于另外一点 $Q$, 求 $\triangle Q A B$ 面积的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-077.jpg?height=333&width=317&top_left_y=620&top_left_x=1521)

解析 解法一 设 $Q(2 \cos \theta, \sin \theta)$, 则 $\overrightarrow{P Q}$ 为直线 $A B$ 的法向量, 于是

$$
A B: 2 \cos \theta \cdot x+(\sin \theta+1) \cdot y+\sin \theta+1=0
$$

进而可得

$$
\frac{1}{2}|A B|=\sqrt{4-\frac{(\sin \theta+1)^{2}}{(2 \cos \theta)^{2}+(\sin \theta+1)^{2}}}=\frac{\sqrt{19+6 \sin \theta-13 \sin ^{2} \theta}}{\sqrt{5+2 \sin \theta-3 \sin ^{2} \theta}},
$$

而

$$
|Q P|=\sqrt{(2 \cos \theta)^{2}+(\sin \theta+1)^{2}}=\sqrt{5+2 \sin \theta-3 \sin ^{2} \theta}
$$

于是 $\triangle Q A B$ 的面积

$$
S_{\triangle C A B}=\sqrt{19+6 \sin \theta-13 \sin ^{2} \theta}
$$

其取值范围是 $\left(0, \sqrt{\frac{256}{13}}\right]$.

解法二 当直线 $A B$ 的斜率不存在时, 点 $Q$ 不存在. 设直线 $A B$ 的方程为 $y=k x-1$, 于是点 $O$ 到直线 $A B$ 的距离 $d=\frac{1}{\sqrt{1+k^{2}}}$, 从而有

$$
|A B|=2 \sqrt{4-\frac{4}{1+k^{2}}}
$$

直线 $P Q$ 的方程为 $x+k y+k=0$, 与椭圆方程联立消去 $y$ 得 $x_{Q}=-\frac{8 k}{k^{2}+4}$, 于是

$$
|P Q|=\sqrt{1+\frac{1}{k^{2}}}\left|x_{Q}\right|=\frac{8 \sqrt{k^{2}+1}}{k^{2}+4}
$$

对 $k=0$ 也成立.

于是 $\triangle Q A B$ 的面积

$$
\begin{aligned}
S & =\frac{1}{2}|A B| \cdot|P Q| \\
& =\frac{8 \sqrt{4 k^{2}+3}}{k^{2}+4} \\
& =8 \sqrt{\frac{4\left(k^{2}+4\right)-13}{\left(k^{2}+4\right)^{2}}} \\
& =8 \sqrt{-13\left(\frac{1}{k^{2}+4}-\frac{2}{13}\right)^{2}+\frac{4}{13}} \\
& \in\left(0, \frac{16}{13} \sqrt{13}\right] .
\end{aligned}
$$

即 $\triangle Q A B$ 的面积的取值范围是 $\left(0, \frac{16}{13}, \sqrt{3}\right]$.

## 第 603 题 动点轨迹

已知椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 和直线 $l: A x+B y=1, P$ 是直线 $l$ 上一点, 射线 $O P$ 交椭圆于点 $R$. 又点 $Q$ 在射线 $O P$ 上且满足 $|O P| \cdot|O Q|=|O R|^{2}$, 当点 $P$ 在直线 $l$ 上移动时, 求点 $Q$ 的轨迹方程.

解析 解法一 设 $R(a \cos \theta, b \sin \theta), P(p a \cos \theta, p b \sin \theta)$, 其中 $p>0$, 则 $Q\left(\frac{a}{p} \cos \theta, \frac{b}{p} \sin \theta\right)$.

由点 $P$ 满足直线 $l$ 的方程, 可得

$$
A p a \cos \theta+B p b \sin \theta=1,
$$

而点 $Q$ 的参数方程为

$$
\left\{\begin{array}{l}
p x=a \cos \theta \\
p y=b \sin \theta
\end{array}\right.
$$

可得

$$
p^{2}\left(\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}\right)=1
$$

而

$$
A p^{2} x+B p^{2} y=1
$$

从而点 $Q$ 的轨迹方程为

$$
A x+B y=\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}
$$

即

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}-A x-B y=0
$$

其中 $x, y$ 不同时为 0 .

解法二 将椭圆 $C$ 仿射变换为

$$
C^{\prime}: x^{\prime 2}+y^{\prime 2}=a^{2},
$$

则点 $Q^{\prime}$ 的轨迹是直线 $l^{\prime}$ 以点 $O^{\prime}$ 为反演中心的圆, 其方程为

$$
\left(\frac{x^{\prime 2}}{a^{2}}+\frac{y^{\prime 2}}{a^{2}}-1\right)-\left(A x^{\prime}+B \cdot \frac{b}{a} y^{\prime}-1\right)=0\left(x^{2}+y^{2} \neq 0\right)
$$

回到原坐标系,其方程为

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}-A x-B y=0, x^{2}+y^{2} \neq 0
$$

事实上, 利用相似容易证明点 $Q^{\prime}$ 的轨迹是以 $O Q_{0}{ }^{\prime}$ 为直径的圆, 其中点 $Q_{0}{ }^{\prime}$ 是当 $O P^{\prime} \perp l^{\prime}$ 时对应的点 $Q^{\prime}$位置, 如图.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-079.jpg?height=368&width=820&top_left_y=398&top_left_x=610)

而 $Q_{0}{ }^{\prime}$ 的坐标容易计算,因此可以方便的推导反演圆方程.

## 第 604 题 交点曲线系

如图 1, 已知圆 $G:(x-2)^{2}+y^{2}=r^{2}$ 是椭圆 $\frac{x^{2}}{16}+y^{2}=1$的内接 $\triangle A B C$ 的内切圆, 其中 $A$ 为椭圆的左顶点.

(1) 求圆 $G$ 的半径 $r$;

(2) 过 $M(0,1)$ 作圆的两条切线交椭圆于 $E, F$ 两点, 证明:直线 $E F$ 与圆 $G$ 相切.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-079.jpg?height=277&width=662&top_left_y=1092&top_left_x=1176)

图 1

解析 (1) 如图 2, 设切点分别为点 $P, Q$.

由 $\triangle A P G$ 与 $\triangle A Q B$ 相似, 有

$$
\frac{P G}{A P}=\frac{B Q}{A Q}
$$

于是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-079.jpg?height=178&width=659&top_left_y=1437&top_left_x=1218)

图 2

$$
\frac{r}{\sqrt{36-r^{2}}}=\frac{B Q}{6+r}
$$

从而

$$
B Q=r \cdot \sqrt{\frac{6+r}{6-r}}
$$

将点 $B$ 的坐标代人椭圆方程有

$$
\frac{1}{16} \cdot(2+r)^{2}+\left(r \cdot \sqrt{\frac{6+r}{6-r}}\right)^{2}=1
$$

注意到 $r=-6$ 是该方程的一个解, 解得正根 $r=\frac{2}{3}$.

(2) 设过点 $M$ 的切线为 $y=k x+1$, 则由直线与圆的位置关系可得

$$
\frac{|2 k+1|}{\sqrt{1+k^{2}}}=\frac{2}{3}
$$

即

$$
32 k^{2}+36 k+5=0
$$

于是设直线 $M E, M F$ 的斜率分别为 $k_{1}, k_{2}$, 则

$$
k_{1}+k_{2}=-\frac{9}{8}, k_{1} \cdot k_{2}=\frac{5}{32} .
$$

将两条相交直线 $M E \cup M F$ 看作是一条曲线

$$
\left(y-k_{1} x-1\right) \cdot\left(y-k_{2} x-1\right)=0
$$

注意到这条曲线与椭圆的交点为 $M, E, F$, 因此需要设法联立变形为直线方程, 且在联立过程中去掉解 $x=0, y=1$. 于是将该曲线方程和椭圆方程分别变形为

$$
-k_{1} \cdot k_{2} x^{2}=(y-1)^{2}-\left(k_{1}+k_{2}\right) x(y-1)
$$

和

$$
-\frac{1}{16} x^{2}=y^{2}-1
$$

将 $k_{1}+k_{2}$ 和 $k_{1} \cdot k_{2}$ 代人,两式相比得

$$
\frac{5}{2}=\frac{y-1+\frac{9}{8} x}{y+1}
$$

化简得

$$
E F: 9 x-12 y-28=0 .
$$

从而圆心 $G(2,0)$ 到直线 $E F$ 的距离为

$$
\frac{10}{\sqrt{9^{2}+12^{2}}}=\frac{2}{3}=r
$$

原命题得证.

利用相交直线 $M E \cup M F$ 以及椭圆构成交点曲线系获得直线 $E F$ 的方程可以大大减少运算量.

## 第 605 题 “垂径定理”二三事

已知椭圆 $M: \frac{x^{2}}{4}+\frac{y^{2}}{3}=1$, 点 $F_{1}, C$ 分别是椭圆 $M$ 的左焦点、左顶点, 过点 $F_{1}$的直线 $l$ (不与 $x$ 轴重合) 交椭圆 $M$ 于 $A, B$ 两点.

(1) 求梄圆 $M$ 的离心率及短轴长;

(2) 是否存在直线 $l$, 使得点 $B$ 在以线段 $A C$ 为直径的圆上, 若存在, 求出直线 $l$ 的方程; 若不存在, 说明理由.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-080.jpg?height=316&width=348&top_left_y=1557&top_left_x=1394)

解析 (1) $e=\frac{1}{2}, 2 b=2 \sqrt{3}$.

(2) 不存在直线 $l$,使得点 $B$ 在以线段 $A C$ 为直径的圆上,证明如下.

原问题即 $\angle A B C$ 是否可能为直角, 我们接下来通过证明 $\angle A C B$ 恒为钝角来否定 $\angle A B C$ 为直角的可能性. 将坐标系平移至以 $C$ 为原点, 记新原点为 $C^{\prime}$, 则椭圆方程变为

$$
\frac{\left(x^{\prime}-2\right)^{2}}{4}+\frac{y^{\prime 2}}{3}=1
$$

即

$$
\frac{1}{4} x^{\prime 2}-x^{\prime}+\frac{1}{3} y^{\prime 2}=0
$$

此时 $F_{1}^{\prime}(1,0)$, 因此可设直线 $A^{\prime} B^{\prime}: x^{\prime}+n y^{\prime}=1$, 与椭圆方程化齐次联立, 有

$$
\frac{1}{4} x^{\prime 2}-x^{\prime}\left(x^{\prime}+n y^{\prime}\right)+\frac{1}{3} y^{\prime 2}=0,
$$

也即

$$
\frac{1}{3}\left(\frac{y^{\prime}}{x^{\prime}}\right)^{2}-n \cdot \frac{y^{\prime}}{x^{\prime}}-\frac{3}{4}=0
$$

于是

$$
k_{C_{A^{\prime}}} \cdot k_{C_{B^{\prime}}}=-\frac{9}{4}
$$

此时取与 $\overrightarrow{C A}$ 同向的向量 $\left(1, k_{C A^{\prime}}\right)$ 以及和 $\overrightarrow{C B}$ 同向的向量 $\left(1, k_{C B^{\prime}}\right)$, 它们的数量积

$$
\left(1, k_{C A^{\prime}}\right) \cdot\left(1, k_{C B^{\prime}}\right)=1+k_{C A^{\prime}} \cdot k_{C B^{\prime}}=-\frac{5}{4}<0
$$

因此 $\overrightarrow{C A}$ 与 $\overrightarrow{C B}$ 的夹角为针角, 也即 $\angle A C B$ 为针角, 欲证命题成立.

## 第 606 题 定比点差法

如图, 已知梄圆 $C: x^{2}+3 y^{2}=3$, 过点 $D(1,0)$ 且不过点 $E(2,1)$ 的直线与椭圆 $C$ 交于 $A, B$ 两点, 直线 $A E$ 与直线 $x=3$ 交于点 $M$.

(1) 求椭圆 $C$ 的离心率;

(2)若 $A B \perp x$ 轴,求直线 $B M$ 的斜率;

(3) 试判断直线 $B M$ 与直线 $D E$ 的位置关系,并说明理由.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-081.jpg?height=276&width=442&top_left_y=895&top_left_x=1394)

解析 (1) 椭圆 $C$ 的离心率 $e=\frac{c}{a}=\frac{\sqrt{6}}{3}$.

(2) 根据题意, 设 $A(1, t), B(1,-t), M(3, m)$, 则由 $A, E, M$ 三点共线有

$$
\frac{t-1}{1-2}=\frac{m-1}{3-2}
$$

即

$$
m+t=2 \text {. }
$$

从而直线 $B M$ 的斜率为

$$
\frac{m-(-t)}{3-1}=\frac{m+t}{2}=1
$$

(3) 直线 $B M$ 与 $D E$ 平行, 证明如下.

设 $\overrightarrow{A D}=\lambda \overrightarrow{D B}, A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 则

$$
D\left(\frac{x_{1}+\lambda x_{2}}{1+\lambda}, \frac{y_{1}+\lambda y_{2}}{1+\lambda}\right)=(1,0)
$$

于是

$$
x_{1}+\lambda x_{2}=1+\lambda, y_{1}+\lambda y_{2}=0
$$

由已知, 有

$$
x_{1}^{2}+3 y_{1}^{2}=3, \lambda^{2} x_{2}^{2}+3 \lambda^{2} y_{2}^{2}=3 \lambda^{2}
$$

两式相减得

$$
\left(x_{1}+\lambda x_{2}\right)\left(x_{1}-\lambda x_{2}\right)+3\left(y_{1}+\lambda y_{2}\right)\left(y_{1}-\lambda y_{2}\right)=3(1+\lambda)(1-\lambda),
$$

应用 $D$ 点坐标, 可得

$$
x_{1}-\lambda x_{2}=3-3 \lambda,
$$

进而

$$
x_{1}=2-\lambda \text {. }
$$

于是

$$
\frac{A E}{E M}=\frac{2-x_{1}}{3-2}=\lambda
$$

根据平行线截割定理的逆定理可知, 直线 $D E$ 与直线 $B M$ 平行.

## 第 607 题 定义 vs 方程

已知椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1, F_{1}, F_{2}$ 是椭圆的左、右焦点, $A, C$ 为椭圆上关于 $x$ 轴对称的两点, $B$ 点为短轴的端点, 线段 $A B$ 恰过右焦点, 如图 1 所示, 有 $A B \perp$ $C F_{1}$, 求椭圆的离心率.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-082.jpg?height=326&width=361&top_left_y=453&top_left_x=1371)

图 1

解析 连结 $B F_{1}, A F_{1}$, 易知图 2 中加“.”的角都相等, 设为 $\theta$,

易证

$$
\angle A F_{1} B=90^{\circ} .
$$

设 $A F_{2}=x$, 则

$$
A F_{1}=2 a-x
$$

在 Rt $\triangle A B F_{1}$ 中, 有

$$
(2 a-x)^{2}+a^{2}=(a+x)^{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-082.jpg?height=322&width=368&top_left_y=829&top_left_x=1398)

图 2

解得

$$
x=\frac{2 a}{3}
$$

于是

$$
\cos 2 \theta=\frac{a}{a+x}=\frac{3}{5}
$$

即

$$
1-2 \sin ^{2} \theta=\frac{3}{5}
$$

解得

$$
\sin \theta=\frac{\sqrt{5}}{5}
$$

从而椭圆的离心率

$$
e=\frac{c}{a}=\sin \theta=\frac{\sqrt{5}}{5}
$$

本题思路很多, 可以联立直线 $B F_{2}$ 与椭圆的方程求出 $A$ 点坐标, 通过垂直得到关于 $a, b, c$ 的方程, 求得离心率; 也可以设出点 $C$ 的坐标, 表示出点 $A$ 的坐标, 通过坐标满足椭圆方程, $A, B, F_{2}$ 三点共线以及垂直关系得到三个方程去求解.

## 第 608 题 合理选参简化计算

如图 1, 椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的左、右焦点分别为 $F_{1}$, 点 $F_{2}$, 过点 $F_{2}$ 的直线交椭圆于 $P, Q$ 两点, 且 $P Q \perp P F_{1}$. 若 $|P Q|=\lambda\left|P F_{1}\right|$, 且 $\frac{3}{4} \leqslant \lambda<\frac{4}{3}$, 试确定椭圆离心率 $e$ 的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-083.jpg?height=287&width=338&top_left_y=452&top_left_x=1502)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-083.jpg?height=273&width=330&top_left_y=803&top_left_x=1544)

图 2

$$
m+n=\sqrt{1+\lambda^{2}} m+(\lambda m-n)
$$

从而

$$
\frac{n}{m}=\frac{1}{2}\left(\lambda-1+\sqrt{1+\lambda^{2}}\right)
$$

当 $\lambda \in\left[\frac{3}{4}, \frac{4}{3}\right)$ 时, 由于 $\frac{n}{m}$ 随着 $\lambda$ 的增大而增大,于是 $\frac{n}{m}$ 的取值范围是 $\left[\frac{1}{2}, 1\right)$.

进而椭圆的离心率

$$
e=\frac{2 c}{2 a}=\frac{\left|F_{1} F_{2}\right|}{\left|P F_{1}\right|+\left|P F_{2}\right|}=\frac{\sqrt{m^{2}+n^{2}}}{m+n}=\sqrt{\frac{1}{1+\frac{2}{\frac{m}{n}+\frac{n}{m}}}}
$$

我们熟知函数 $y=x+\frac{1}{x}$ 在区间 $(0,1)$ 上单调递减, 因此当 $\frac{n}{m} \in\left[\frac{1}{2}, 1\right)$ 时, $\frac{m}{n}+\frac{n}{m}$ 随着 $\frac{n}{m}$ 的增大而减小,于是 $\frac{m}{n}+\frac{n}{m}$ 的取值范围是 $\left(2, \frac{5}{2}\right]$.

于是椭圆离心率 $e$ 的取值范围是 $\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{5}}{3}\right]$.

本题的关键是恰当地表达点 $Q$ 在椭圆上 (绕开方程用定义)以及利用几何条件解三角形, 同时对于多参数问题的化简与整理的方向也需要有一个明确的思路.

## 第 609 题 探索存在性

若椭圆或双曲线上存在点 $P$, 使得点 $P$ 到两个焦点的距离之比为 $2: 1$, 则称此椭圆或双曲线存在 “ $K$ 点”, 下列曲线中存在“ $K$ 点”的是
A. $\frac{x^{2}}{16}+\frac{y^{2}}{15}=1$
B. $\frac{x^{2}}{25}+\frac{y^{2}}{24}=1$
C. $x^{2}-\frac{y^{2}}{15}=1$
D. $x^{2}-y^{2}=1$

## 解析 $\mathrm{D}$.

我们需要将“点 $P$ 到两个焦点的距离之比为 $2: 1$ ”这一信息进行转化.

方案一 到两个定点的距离之比为 $2: 1$ 的点的轨迹为圆 (阿波罗尼斯圆), 因此原问题就是椭圆 (或双曲线)与两个圆是否存在公共点的问题. 每个选项对应不同的圆,还需要考虑是否存在交点,这并不简单,暂时舍弃这个方案.

方案二 考虑椭圆 (或双曲线)上的点到两个焦点的距离之比的取值范围. 为了方便起见,考虑“较大的”与“较小的”的比值.

对于椭圆来说, 这个比值的最小值为 1 , 因为椭圆上一点到两个焦点的距离之和为定值, 所以这个比值的最大值只需要考虑椭圆上一点到焦点的最大距离, 显然为 $a+c$, 于是比值的范围为

$$
\left[1, \frac{a+c}{a-c}\right] \text {. }
$$

对于双曲线来说, 设双曲线上的点到较近焦点的距离为 $m$, 则这个比值为 $\frac{2 a+m}{m}=\frac{2 a}{m}+1$, 因为 $m \in[c-$ $a,+\infty)$, 所以比值的取值范围为

$$
\left(1, \frac{c+a}{c-a}\right] \text {. }
$$

各个选项在这个比值上的取值范围分别为

$$
\left[1, \frac{5}{3}\right],\left[1, \frac{3}{2}\right],\left(1, \frac{5}{3}\right],\left(1, \frac{\sqrt{2}+1}{\sqrt{2}-1}\right]
$$

由此判断只有选项 D 满足要求.

方案三 由点 $P$ 到两个焦点的距离之比为 $2: 1$ 计算出点 $P$ 对应的焦半径, 再根据焦半径的范围去估计椭圆或双曲线的离心率.

对于椭圆, 由点 $P$ 到两个焦点的距离之比为 $2: 1$ 知焦半径分别为 $\frac{4 a}{3}$ 与 $\frac{2 a}{3}$. 而椭圆的焦半径的取值范围为 $[a-c, a+c]$, 所以有 $\frac{2}{3} a \geqslant a-c$, 解得 $e \geqslant \frac{1}{3}$. 类似地考虑双曲线, 可得 $e \leqslant 3$. 而各选项的离心率分别为

$$
\frac{1}{4}, \frac{1}{5}, 4, \sqrt{2},
$$

故只有选项 $\mathrm{D}$ 符合要求.

## 第 610 题 沟通的桥梁

已知有公共焦点的椭圆与双曲线中心, 原点为 $O$, 焦点在 $x$ 轴上, 左, 右焦点分别为 $F_{1}, F_{2}$, 且它们在第一象限的交点为 $P, \triangle P F_{1} F_{2}$ 是以 $P F_{1}$ 为底边的等腰三角形, 若双曲线的离心率的取值范围为 $(1$, $2)$, 则该椭圆的离心率的取值范围是

解析 $\left(\frac{1}{3}, \frac{2}{5}\right)$.

本题中椭圆与双曲线的半焦距长相等, 设为 $c$, 设椭圆的长半轴长为 $a_{1}$, 离心率为 $e_{1}$, 双曲线的实半轴长为 $a_{2}$, 离心率为 $e_{2}$.

因为点 $P$ 同时在椭圆与双曲线上, 所以根据椭圆与双曲线的定义, 我们就可以得到关于 $\triangle P F_{1} F_{2}$ 边长的多个关系式, 进而得到 $a_{1}, a_{2}, c$ 的联系, 导出离心率 $e_{1}, e_{2}$ 的大小关系, 得到结论. 如图 1 所示.

设 $\left|P F_{1}\right|=2 m,\left|P F_{2}\right|=2 n$, 由椭圆与双曲线的定义知

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-085.jpg?height=262&width=293&top_left_y=740&top_left_x=1590)

图 1

$$
2 m+2 n=2 a_{1}, 2 m-2 n=2 a_{2}, 2 n=2 c
$$

从而 $n=c, a_{1}=m+c, a_{2}=m-c$. 于是得到

$$
\dot{e}_{1}=\frac{c}{m+c}, e_{2}=\frac{c}{m-c} .
$$

从而得到 $\frac{1}{e_{1}}-\frac{1}{e_{2}}=2$, 由 $e_{2} \in(1,2)$ 得到 $e_{1}$ 的取值范围是 $\left(\frac{1}{3}, \frac{2}{5}\right)$.

若条件改为“ $\triangle P F_{1} F_{2}$ 是以 $P F_{2}$ 为定边的等腰三角形”, 则如图 2 , 由椭圆与双曲线的定义可以得到 $\frac{1}{e_{1}}+\frac{1}{e_{2}}=2$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-085.jpg?height=262&width=281&top_left_y=1412&top_left_x=1596)

图 2

## 第 611 题 椭圆中的等腰三角形

椭圆 $C: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的左、右焦点分别为 $F_{1}, F_{2}$, 若椭圆 $C$ 上恰好有 6 个不同的点 $P$, 使得 $\triangle F_{1} F_{2} P$ 为等腰三角形, 则椭圆 $C$ 的离心率的取值范围是

解析 $\left(\frac{1}{3}, \frac{1}{2}\right) \cup\left(\frac{1}{2}, 1\right)$.

$\triangle P F_{1} F_{2}$ 的一边长为 $2 c$, 另外两边为植圆的焦半径, 考虑三边中哪条边为等腰三角形的底边, 以此探究何时可以得到等腰三角形.

情形一 如果底边为 $F_{1} F_{2}$, 则点 $P$ 为短轴的两个顶点, 得到两个不同的点;

情形二 如果 $F_{1} F_{2}$ 不为底边, 不妨考虑以 $P F_{2}$ 为底边 (以 $P F_{1}$ 为底边的情况完全相同), 此时 $P F_{1}=$ $F_{1} F_{2}=2 c$. 故椭圆上能找到两点, 使得 $P F_{1}=2 c$, 由焦半径的取值范围知

$$
2 c \in[a-c, a+c]
$$

又 $P, F_{1}, F_{2}$ 三点不共线, 故 $2 c \neq a-c$, 解得 $e>\frac{1}{3}$.

最后,我们需要考虑,情形一与情形二中得到的点 $P$ 是否一定是不同的点?

事实上, 当等腰 $\triangle P F_{1} F_{2}$ 是等边三角形时, 上面的六个点会重合成两个点, 此时 $a=2 c$, 不满足题意,故 $e \neq \frac{1}{2}$.

综上知, $\frac{1}{3}<e<1$, 且 $e \neq \frac{1}{2}$.

## 第 612 题 代数与几何

如图 1, 已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ 的左、右焦点分别为 $F_{1}, F_{2} . P$ 是椭圆上一点,直线 $F_{2} M$ 垂直于 $O P$ 且交线段 $F_{1} P$ 于点 $M$, 若 $F_{1} M=2 M P$, 求椭圆 $E$ 的离心率 $e$ 的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-086.jpg?height=316&width=414&top_left_y=859&top_left_x=1309)

图 1

解析 解法一 设 $F_{1}(-c, 0), F_{2}(c, 0), P(x, y)$, 则 $M\left(\frac{2}{3} x-\frac{1}{3} c, \frac{2}{3} y\right)$.

由 $M F_{2} \perp O P$ 可得

$$
\frac{y}{x} \cdot \frac{\frac{2}{3} y}{\frac{2}{3} x-\frac{4}{3} c}=-1
$$

整理得

$$
x^{2}+y^{2}-2 c x=0,
$$

将 $y^{2}=b^{2} \cdot\left(1-\frac{x^{2}}{a^{2}}\right)$ 代人, 可得

$$
\frac{c^{2}}{a^{2}} x^{2}-2 c x+b^{2}=0
$$

该方程在 $[-a, a]$ 上有根, 又该方程的两根不等, 且同正, 两根之和大于 $2 a$, 故它在 $[-a, a]$ 上有且只有一根, 因此

$$
\frac{c^{2}}{a^{2}} \cdot a^{2}-2 c a+b^{2} \leqslant 0
$$

解得 $e \geqslant \frac{1}{2}$, 从而 $e$ 的取值范围是 $\left[\frac{1}{2}, 1\right)$.

解法二 延长 $O F_{2}$ 至点 $Q$, 使得 $F_{2} Q=F_{2} O$, 连结 $P Q$, 则有 $M F_{2} / / P Q$, 于是 $\angle O P Q$ 为直角, 从而 $P F_{2}=c$, 其中 $c$ 为椭圆 $E$ 的半焦距. 因此

$$
a-c \leqslant c \leqslant a+c
$$

解得 $e \geqslant \frac{1}{2}$, 进而 $e$ 的取值范围是 $\left[\frac{1}{2}, 1\right)$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-086.jpg?height=242&width=336&top_left_y=2224&top_left_x=1419)

图 2
利用平面向量知识, 可以由 $\overrightarrow{F_{2} M} \cdot \overrightarrow{O P}=0$ 得到

$$
\left(\overrightarrow{O M}-\overrightarrow{O F_{2}}\right) \cdot \overrightarrow{O P}=0
$$

即

$$
\left(\frac{2}{3} \overrightarrow{O P}+\frac{1}{3} \overrightarrow{O F_{1}}-\overrightarrow{O F_{2}}\right) \cdot \overrightarrow{O P}=0
$$

从而

$$
\left(\overrightarrow{O P}-2 \overrightarrow{O F_{2}}\right) \cdot \overrightarrow{O P}=0
$$

这就提示我们倍长 $O F_{2}$.

## 第 613 题 焦点三角形的内心

已知椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0), F_{1}, F_{2}$ 为其左右焦点, $P$ 为椭圆 $C$ 上任意一点, $I$ 为 $\triangle P F_{1} F_{2}$ 内切圆圆心, $\triangle P F_{1} F_{2}$ 的重心 $G$ 满足 $\overrightarrow{P F_{1}}+\overrightarrow{P F_{2}}=3 \overrightarrow{P G}$ 且存在非零实数 $\lambda$, 使得 $\overrightarrow{G I}=\lambda \overrightarrow{F_{1} F_{2}}$, 则椭圆的离心率是

解析 $\frac{1}{2}$.

如图. 因为 $\overrightarrow{G I}=\lambda \overrightarrow{F_{1} F_{2}}$, 所以 $y_{G}=y_{I}$, 而 $G$ 是重心, 所以

$$
y_{G}=\frac{1}{3} y_{P}=r
$$

而内切圆半径

$$
r=\frac{2 S_{\triangle P F_{1} F_{2}}}{P F_{1}+P F_{2}+F_{1} F_{2}}=\frac{2 \cdot \frac{1}{2} \cdot F_{1} F_{2} \cdot y_{P}}{2 a+2 c}=\frac{c}{a+c} \cdot y_{P}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-087.jpg?height=451&width=549&top_left_y=1392&top_left_x=1332)

因此 $\frac{1}{3} y_{P}=\frac{c}{a+c} \cdot y_{P}$, 所以 $\frac{c}{a}=\frac{1}{2}$.

题中关于重心 $G$ 的条件 $\overrightarrow{P F_{1}}+\overrightarrow{P F_{2}}=3 \overrightarrow{P G}$ 不必给出.

## 第 614 题 轨迹问题

已知椭圆 $G: \frac{x^{2}}{6}+\frac{y^{2}}{b^{2}}=1(0<b<\sqrt{6})$ 的两个焦点分别为 $F_{1}$ 和 $F_{2}$, 短轴的两个端点分别为 $B_{1}$ 和 $B_{2}$,点 $P$ 在椭圆 $G$ 上, 且满足 $\left|P B_{1}\right|+\left|P B_{2}\right|=\left|P F_{1}\right|+\left|P F_{2}\right|$. 当 $b$ 变化时, 给出下列三个命题:

(1) 点 $P$ 的轨迹关于 $y$ 轴对称;

(2) 存在 $b$ 使得椭圆 $G$ 上满足条件的点 $P$ 仅有两个;

(3) $|O P|$ 的最小值为 2,

其中,所有正确命题的序号是 $\qquad$

## 解析 (1)(3).

对于(1), 根据题意, $P(x, y)$ 满足

$$
\left\{\begin{array}{l}
\frac{x^{2}}{6}+\frac{y^{2}}{b^{2}}=1 \\
\frac{y^{2}}{6}+\frac{x^{2}}{6-b^{2}}=1
\end{array}\right.
$$

因此点 $P$ 的轨迹关于 $y$ 轴对称. 事实上, 点 $P$ 的轨迹还关于 $x$ 轴和原点 $O$ 对称;

对于(2), 由于 $P$ 点是两个椭圆的公共点, 因此若命题(2)成立, 则对应的点 $P$ 为椭圆 $G$ 的上下顶点或左右顶点, 容易验证这两种情形都不符合题意;

对于(3), 由于 $|O P|^{2}=x^{2}+y^{2}$, 因此

$$
\frac{x^{2}}{6}+\frac{|O P|^{2}-x^{2}}{b^{2}}=\frac{x^{2}}{6-b^{2}}+\frac{|O P|^{2}-x^{2}}{6}=1
$$

进而有

$$
x^{2}=\frac{1-\frac{|O P|^{2}}{b^{2}}}{\frac{1}{6}-\frac{1}{b^{2}}}=\frac{1-\frac{|O P|^{2}}{6}}{\frac{1}{6-b^{2}}-\frac{1}{6}}
$$

化简得

$$
|O P|^{2}=6-\frac{1}{\frac{1}{6-b^{2}}+\frac{1}{b^{2}}-\frac{1}{6}} \geqslant 6-\frac{1}{\frac{2}{3}-\frac{1}{6}}=4,
$$

因此 $|O P|$ 的最小值为 2 , 当 $b=\sqrt{3}$ 时取得.

## 第 615 题 焦半径立奇功

如图 1, 已知植圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$, 圆 $O$ 以椭圆 $E$ 的短轴为直径.设 $A B$ 是椭圆 $E$ 的弦且与圆 $O$ 相切, 椭圆的一个焦点 $F$ 与弦 $A B$ 在 $y$ 轴同侧,求证: $\triangle F A B$ 的周长为定值 $2 a$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-088.jpg?height=270&width=398&top_left_y=2176&top_left_x=1349)

图 1
解析 解法一 切点为 $M$, 我们可以证明一个更强的结论:

$$
F A+A M=F B+B M=a .
$$

如图 2 , 连结 $O A, O B, O M$. 设 $A\left(x_{1}, y_{1}\right)$, 则

$$
\begin{aligned}
F A+A M & =a-\frac{c}{a} \cdot x_{1}+\sqrt{O A^{2}-O M^{2}} \\
& =a-\frac{c}{a} \cdot x_{1}+\sqrt{x_{1}^{2}+y_{1}^{2}-b^{2}} \\
& =a-\frac{c}{a} \cdot x_{1}+\sqrt{x_{1}^{2}+b^{2}\left(1-\frac{x_{1}^{2}}{a^{2}}\right)-b^{2}} \\
& =a,
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-089.jpg?height=259&width=372&top_left_y=193&top_left_x=1486)

图 2

类似地, 有

$$
F B+B M=a,
$$

因此原命题得证.

解法二 当直线 $A B$ 的斜率存在时, 设直线 $A B$ 的方程为 $y=k x+m$, 不妨设 $k>0, m<0$.由 $A B$ 与圆 $x^{2}+y^{2}=b^{2}$ 相切可得

$$
\frac{|m|}{\sqrt{1+k^{2}}}=b
$$

即

$$
m=-b \sqrt{1+k^{2}} .
$$

联立直线 $A B$ 与椭圆 $E$ 的方程, 可得

$$
\left(b^{2}+a^{2} k^{2}\right) x^{2}+2 a^{2} k m x+a^{2} m^{2}-a^{2} b^{2}=0,
$$

将 $m$ 代人, 可得

$$
\left(b^{2}+a^{2} k^{2}\right) x^{2}-2 a^{2} k b \sqrt{1+k^{2}} x+a^{2} b^{2} k^{2}=0,
$$

设 $A, B$ 两点的横坐标分别为 $x_{1}, x_{2}$ 则

$$
x_{1}+x_{2}=\frac{2 a^{2} k b \sqrt{1+k^{2}}}{b^{2}+a^{2} k^{2}}
$$

且

$$
\left|x_{1}-x_{2}\right|=\frac{2 a b c k}{b^{2}+a^{2} k^{2}}
$$

其中 $c$ 为椭圆的半焦距.

因此 $\triangle F A B$ 的周长为

$$
F A+F B+A B=2 a-\frac{c}{a} \cdot\left(x_{1}+x_{2}\right)+\sqrt{1+k^{2}} \cdot\left|x_{1}-x_{2}\right|=2 a \text {. }
$$

容易验证, 当直线 $A B$ 的斜率不存在时, 命题依然成立.

因此原命题得证.

## 第 616 题 粗圆中的椭圆

如图, 已知 $A, B$ 是以 $F_{1}, F_{2}$ 为焦点的椭圆上 (不在长轴上) 两点, 且 $F_{1} A / /$ $F_{2} B . M$ 为 $F_{1} B$ 与 $F_{2} A$ 的交点, 求证: 点 $M$ 的轨迹也是以 $F_{1}, F_{2}$ 为焦点的椭圆.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-089.jpg?height=254&width=317&top_left_y=2256&top_left_x=1527)

解析 设 $A F_{1}=m, B F_{2}=n$, 则 $A F_{2}=2 a-m, B F_{1}=2 a-n$. 由题意得

$$
\frac{M F_{1}}{M B}=\frac{M A}{M F_{2}}=\frac{A F_{1}}{B F_{2}}=\frac{m}{n}
$$

于是

$$
M F_{1}=\frac{m}{m+n} \cdot(2 a-n), M F_{2}=\frac{n}{m+n} \cdot(2 a-m)
$$

因此

$$
M F_{1}+M F_{2}=2 a-\frac{2}{\frac{1}{m}+\frac{1}{n}} .
$$

我们熟知

$$
\frac{1}{m}+\frac{1}{n}=\frac{2}{e p}
$$

其中 $e$ 是植圆的离心率, $p$ 为椭圆的焦点到对应准线的距离,因此原命题得证.

进一步, 由于 $e p=\frac{b^{2}}{a}$ (即梗圆的半通径长), 新的椭圆的离心率为

$$
\frac{2 c}{2 a-\frac{b^{2}}{a}}=\frac{2 e}{1+e^{2}}
$$

思考与总结

椭圆的焦点弦被焦点分成的两条线段的长度的调和平均数为半通径长, 这是椭圆的焦点弦问题中的个常用性质.

## 第 617 题 用解析几何转化条件

如图, 已知扇形 $O A B$ 中, $\angle A O B$ 为直角, 圆 $C$ 与 $O A, O B$ 及圆 $O$ 相切, 圆 $D$与 $O A$, 圆 $O$, 圆 $C$ 相切. 作 $D E \perp O C$, 垂足为 $E$. 求证: $\triangle O D E$ 的三边成等差数列.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-090.jpg?height=452&width=316&top_left_y=1544&top_left_x=1429)

解析 不妨设 $O A=\sqrt{2}+1, O C=\sqrt{2}$, 则圆 $D$ 的半径

$$
r=\sqrt{2}+1-D O=D C-1
$$

于是 $D O+D C=\sqrt{2}+2$, 因此 $D$ 在以 $O, C$ 为焦点, $\sqrt{2}+2$ 为长轴长的椭圆上.

设 $\angle D O C=\theta$, 则

$$
O D=\frac{\left(\frac{\sqrt{2}+2}{2}\right)^{2}-\left(\frac{\sqrt{2}}{2}\right)^{2}}{\frac{\sqrt{2}+2}{2}-\frac{\sqrt{2}}{2} \cdot \cos \theta}=\frac{\sqrt{2}+2}{\sqrt{2}+1-\cos \theta}
$$

因此有

$$
r=O D \cdot \sin \left(\frac{\pi}{4}-\theta\right)=\sqrt{2}+1-O D
$$

即

$$
\frac{\sqrt{2}+2}{\sqrt{2}+1-\cos \theta} \cdot \frac{\sqrt{2}}{2}(\cos \theta-\sin \theta)=\sqrt{2}+1-\frac{\sqrt{2}+2}{\sqrt{2}+1-\cos \theta}
$$

整理可得

$$
2 \cos \theta-\sin \theta=1,
$$

于是 $\sin \theta=\frac{3}{5}$, 因此原命题得证.

## 第 618 题 托勒密定理

已知 $F$ 为椭圆 $\frac{x^{2}}{5}+y^{2}=1$ 的右焦点, 第一象限内的点 $M$ 在椭圆上, 若 $M F$ 与 $x$ 轴垂直, 直线 $M N$与圆 $x^{2}+y^{2}=1$ 相切于第四象限内的点 $N$, 则 $N F$ 的长度为

解析 $\frac{\sqrt{21}}{3}$.

如图, 半通径 $M F=\frac{b^{2}}{a}=\frac{1}{\sqrt{5}}, O F=2, O M=\sqrt{\frac{21}{5}}, O N=1, M N$ $=\frac{4}{\sqrt{5}}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-091.jpg?height=311&width=595&top_left_y=999&top_left_x=1264)

于是由托勒密定理得

$$
O M \cdot N F+O N \cdot M F=O F \cdot M N,
$$

代人数据计算可得

$$
N F=\frac{\sqrt{21}}{3}
$$

## 第 619 题 焦点弦长公式

已知椭圆 $E: \frac{x^{2}}{81}+\frac{y^{2}}{32}=1, F_{1}, F_{2}$ 是椭圆的左、右焦点, $A B$ 是过 $F_{1}$ 的焦点弦, 且 $\triangle A F_{2} B$ 的面积为 32 , 求 $|A B|$.

解析 设直线 $A B$ 的倾斜角为 $\theta$, 则

$$
|A B|=\frac{2 a b^{2}}{b^{2}+c^{2} \sin ^{2} \theta}
$$

其中 $a^{2}=81, b^{2}=32, c^{2}=49$, 因此 $\triangle A F_{2} B$ 的面积

$$
\begin{aligned}
S & =\frac{1}{2} \cdot \sin \theta \cdot\left|F_{1} F_{2}\right| \cdot|A B| \\
& =\frac{1}{2} \cdot \sin \theta \cdot 14 \cdot \frac{576}{32+49 \sin ^{2} \theta} \\
& =\frac{4032 \sin \theta}{32+49 \sin ^{2} \theta} \\
& =32
\end{aligned}
$$

解得 $\sin \theta=\frac{2}{7}$, 于是

$$
|A B|=\frac{576}{32+49 \sin ^{2} \theta}=16
$$

## 第 620 题 垂径定理与仿射变换

已知椭圆 $\frac{x^{2}}{2}+y^{2}=1$ 上有两个不同的点 $A, B$ 关于直线 $y=m x+\frac{1}{2}$ 对称.

(1) 求实数 $m$ 的取值范围;

(2)求 $\triangle O A B$ 面积的最大值 ( $O$ 为坐标原点).

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-092.jpg?height=267&width=316&top_left_y=619&top_left_x=1434)

图 1

解析 (1) 如图 2, 设线段 $A B$ 的中点为 $M\left(x_{0}, y_{0}\right)$,

则由椭圆的“垂径定理”可得

$$
\left\{\begin{array}{l}
\frac{y_{0}-\frac{1}{2}}{x_{0}}=m \\
-\frac{1}{m} \cdot \frac{y_{0}}{x_{0}}=-\frac{1}{2}
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-092.jpg?height=259&width=313&top_left_y=961&top_left_x=1479)

图 2

解得

$$
x_{0}=-\frac{1}{m}, y_{0}=-\frac{1}{2}
$$

结合条件 $\frac{x_{0}^{2}}{2}+y_{0}^{2}<1$ 可得对 $m$ 的约束

$$
\frac{1}{2 m^{2}}+\frac{1}{4}<1
$$

即

$$
m<-\frac{\sqrt{6}}{3} \text { 或 } m>\frac{\sqrt{6}}{3} \text {. }
$$

(2) 如图 3,作仿射变换

$$
\left\{\begin{array}{l}
x^{\prime}=x \\
y^{\prime}=\sqrt{2} y
\end{array}\right.
$$

将椭圆变成半径为 $\sqrt{2}$ 的圆.

此时 $\triangle O A^{\prime} B^{\prime}$ 的边 $A^{\prime} B^{\prime}$ 的中点 $M^{\prime}$ 在直线 $y^{\prime}=-\frac{\sqrt{2}}{2} x^{\prime}$ 上运动, 于是

$$
\begin{aligned}
S_{\triangle \alpha^{\prime} B^{\prime}} & =\frac{1}{2} \cdot 2 \sqrt{2-O M^{\prime 2}} \cdot O M^{\prime} \\
& =O M^{\prime} \cdot \sqrt{2-O M^{\prime 2}} \\
& =\sqrt{O M^{\prime 2}\left(2-O M^{\prime 2}\right)} \\
& \leqslant 1,
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-092.jpg?height=322&width=335&top_left_y=1796&top_left_x=1457)

图 3

等号当且仅当 $O M^{\prime}=1$ 时取得.

于是 $\triangle O A B$ 面积的最大值为 $\frac{\sqrt{2}}{2}$.

## 第 621 题垂径定理

设点 $O$ 为栯圆的中心, 点 $A$ 为椭圆上异于顶点的任意一点, 过点 $A$ 作长轴的垂线, 垂足为 $M$, 连结 $A O$ 并延长交椭圆于另一点 $B$, 连结 $B M$ 并延长交椭圆于点 $C$, 问是否存在椭圆, 使得 $B A \perp C A ?$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-093.jpg?height=289&width=404&top_left_y=451&top_left_x=1415)

解析 解法一 假设存在满足条件的椭圆, 设椭圆方程为 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$.

记 $A(m, n), B(-m,-n), M(m, 0)$, 则根据椭圆的“垂径定理”, 有

$$
k_{C A} \cdot k_{C B}=-\frac{b^{2}}{a^{2}}
$$

而

$$
k_{C A}=-\frac{1}{k_{A B}}=-\frac{m}{n}
$$

且

$$
k_{C B}=k_{B M}=\frac{n}{2 m}
$$

于是可得

$$
\left(-\frac{m}{n}\right) \cdot \frac{n}{2 m}=-\frac{b^{2}}{a^{2}}
$$

化简得

$$
a^{2}=2 b^{2}
$$

因此存在符合题意的椭圆使得 $B A \perp C A$, 只需椭圆的离心率为 $\frac{\sqrt{2}}{2}$ 即可.

解法二以椭圆的中心为坐标原点, 长轴为 $x$ 轴, 建立坐标系, 设椭圆方程为 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$, 若 $a^{2}=2 b^{2}$, 则必有 $B A \perp C A$.

设 $A\left(x_{0}, y_{0}\right), C\left(x_{1}, y_{1}\right)$, 则由题意知 $M\left(x_{0}, 0\right), B\left(-x_{0},-y_{0}\right)$, 且直线 $B C$ 的斜率一定存在, 设为 $k$, 则直线 $B C$ 的方程为

$$
y=k\left(x-x_{0}\right),
$$

代人椭圆方程并整理得

$$
\left(a^{2} k^{2}+b^{2}\right) x^{2}-2 a^{2} k^{2} x_{0} x+a^{2} k^{2} x_{0}^{2}-a^{2} b^{2}=0,
$$

由韦达定理得

$$
x_{1}-x_{0}=\frac{2 a^{2} k^{2} x_{0}}{a^{2} k^{2}+b^{2}}
$$

因此由直线 $B C$ 的方程为 $y=k\left(x-x_{0}\right)$ 得

$$
y_{1}=k\left(x_{1}-x_{0}\right)=k \frac{2 a^{2} k^{2} x_{0}}{a^{2} k^{2}+b^{2}}=\frac{2 a^{2} k^{3} x_{0}}{a^{2} k^{2}+b^{2}}
$$

由题意直线 $A B$ 的斜率为

$$
k_{A B}=\frac{y_{0}}{x_{0}},
$$

直线 $A C$ 的斜率为

$$
k_{A C}=\frac{y_{1}-y_{0}}{x_{1}-x_{0}}=\frac{\frac{2 a^{2} k^{3} x_{0}}{a^{2} k^{2}+b^{2}}-y_{0}}{\frac{2 a^{2} k^{2} x_{0}}{a^{2} k^{2}+b^{2}}}
$$

由 $B A \perp C A$ 得

$$
k_{A B} k_{A C}=-1
$$

注意到 $k=\frac{y_{0}}{2 x_{0}}$, 整理得 $a^{2}=2 b^{2}$.

## 第 622 题 椭圆的“垂径定理”

已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0), M$ 为椭圆内不在坐标轴上的一点. 过点 $M$ 作不过原点的直线交椭圆于 $A, B$ 两点, $M$ 恰为 $A B$ 的中点, 过点 $M$ 作 $A B$ 的垂线交椭圆于 $C, D$ 两点, $N$ 为弦 $C D$ 的中点. 记点 $O$ 到直线 $A B$ 的距离为 $d$, 求 $\frac{d}{|M N|}$ 的最大值.

解析 不妨设 $M(m, n), m, n>0$, 则根据植圆的“垂径定理”, 可得直线 $A B$ 的斜率为 $-\frac{b^{2} m}{a^{2} n}$, 于是

$$
A B: y=-\frac{b^{2} m}{a^{2} n}(x-m)+n
$$

进而由 $A B \perp C D$ 可得

$$
C D: y=\frac{a^{2} n}{b^{2} m}(x-m)+n
$$

设 $N(s, t)$, 则由椭圆的“垂径定理”, 有

$$
t=-\frac{b^{4} m}{a^{4} n} s
$$

又

$$
t=\frac{a^{2} n}{b^{2} m}(s-m)+n
$$

于是

$$
s=\frac{\frac{a^{2} n}{b^{2}}-n}{\frac{a^{2} n}{b^{2} m}+\frac{b^{4} m}{a^{4} n}}
$$

因此

$$
\begin{aligned}
\frac{d}{|M N|}= & \frac{\left|\frac{b^{2} m^{2}}{a^{2} n}+n\right|}{\sqrt{1+\frac{b^{4} m^{2}}{a^{4} n^{2}}} \cdot \frac{1}{\sqrt{1+\frac{a^{4} n^{2}}{b^{4} m^{2}}} \cdot|m-s|}} \\
& =\frac{\left(\frac{b^{2} m^{2}}{a^{2} n^{2}}+1\right)\left(\frac{a^{2} n}{b^{2} m}+\frac{b^{4} m}{a^{4} n}\right)}{\sqrt{\left(1+\frac{b^{4} m^{2}}{a^{4} n^{2}}\right)\left(1+\frac{a^{4} n^{2}}{b^{4} m^{2}}\right) \cdot\left(\frac{b^{4} m^{2}}{a^{4} n^{2}}+1\right)}} \\
& =\frac{\left(\frac{b^{2} m^{2} n^{2}}{a^{2} n^{2}}+1\right)\left(1+\frac{b^{6} m^{2}}{a^{6} n^{2}}\right)}{\left(\frac{b^{4} m^{2}}{a^{4} n^{2}}+1\right)^{2}},
\end{aligned}
$$

记 $\frac{b^{2} m}{a^{2} n}=u(u>0), \frac{a}{b}=\lambda$, 则

$$
\begin{aligned}
\frac{d}{|M N|} & =\frac{\left(\lambda^{2} u^{2}+1\right)\left(1+\frac{u^{2}}{\lambda^{2}}\right)}{\left(u^{2}+1\right)^{2}} \\
& =\frac{u^{4}+\lambda^{2} u^{2}+\frac{u^{2}}{\lambda^{2}}+1}{u^{4}+2 u^{2}+1} \\
& =1+\frac{\lambda^{2}+\frac{1}{\lambda^{2}}-2}{u^{2}+\frac{1}{u^{2}}+2} \\
& \leqslant 1+\frac{\lambda^{2}+\frac{1}{\lambda^{2}}-2}{4},
\end{aligned}
$$

等号当且仅当 $u=1$ 时取得. 因此所求的最大值为 $\frac{1}{4}\left(\frac{a}{b}+\frac{b}{a}\right)^{2}$.

## 第 623 题 $\quad$ 化复杂计算于无形

设动直线 $y=k x+m(k, m \in \mathbf{Z})$ 与椭圆 $\frac{x^{2}}{16}+\frac{y^{2}}{12}=1$ 交于不同的两点 $A, B$, 与双曲线 $\frac{x^{2}}{4}-\frac{y^{2}}{12}=1$ 交于不同的两点 $C, D$, 且 $\overrightarrow{A C}+\overrightarrow{B D}=\mathbf{0}$, 则符合条件的直线共有条.

## 解析 9.

由 $\overrightarrow{A C}+\overrightarrow{B D}=\mathbf{0}$ 知 $A B$ 的中点与 $C D$ 的中点重合, 记为 $M\left(x_{0}, y_{0}\right)$.

由椭圆与双曲线的垂径定理知, 当 $k \neq 0$ 且 $x_{0} \neq 0$ 时, 有

$$
k \cdot \frac{y_{0}}{x_{0}}=-\frac{12}{16}=\frac{12}{4}
$$

无解,所以只可能有 $k=0$ 或 $x_{0}=y_{0}=0$.

当 $k=0$ 时, 有 $m \in(-2 \sqrt{3}, 2 \sqrt{3})$, 所以 $m= \pm 3, \pm 2, \pm 1,0$;

当 $k \neq 0$ 时, 直线过原点, 所以 $m=0$, 结合双曲线的渐近线为 $y= \pm \sqrt{3} x$ 知, $k= \pm 1$.综上知, 存在 9 条直线满足要求.

## 第 624 题 曲线上的四点共圆

已知椭圆 $G: \frac{x^{2}}{2}+y^{2}=1$, 与 $x$ 轴不重合的直线 $l$ 经过左焦点 $F$, 且与椭圆 $G$ 相交于 $A, B$ 两点, 弦 $A B$ 的中点为 $M$, 直线 $O M$ 与椭圆 $G$ 相交于 $C, D$ 两点.

(1) 若直线 $l$ 的斜率为 1 , 求直线 $O M$ 的斜率;

(2) 是否存在直线 $l$, 使得 $|A M|^{2}=|C M| \cdot|D M|$ 成立? 若存在, 求出直线 $l$ 的方程;若不存在, 请说明理由.

解析 (1)根据楯圆的垂径定理,可得

$$
k_{\text {CM }} \cdot k_{A B}=-\frac{1}{2},
$$

于是直线 $O M$ 的斜率为 $-\frac{1}{2}$.

(2)若

$$
|A M|^{2}=|C M| \cdot|D M|,
$$

则 $A, B, C, D$ 四点共圆,因此

$$
k_{A B}+k_{C D}=0
$$

从而直线 $l$ 的斜率为 $\pm \frac{\sqrt{2}}{2}$, 进而其方程为

$$
y= \pm \frac{\sqrt{2}}{2}(x-1)
$$

## 第 625 题 切线一联结椭圆与圆的纽带

如图 1, 过椭圆外一点引椭圆的两条切线 $P A$ 与 $P B$. 椭圆上一点 $C$ 处的切线与 $P A, P B$ 分别交于 $M, N$ 两点, 即椭圆与 $\triangle P M N$ 旁切. 求证: $M N$对椭圆的焦点 $F$ 的张角大小与 $C$ 点的位置无关.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-096.jpg?height=283&width=420&top_left_y=777&top_left_x=1324)

图 1

解析 设栯圆的另一个焦点为 $E$, 以点 $F$ 为圆心, 长轴长为半径作圆, 则 $E$ 点关于 $P A, P B, M N$ 的对称点 $A_{1}, B_{1}, C_{1}$ 均在圆上, 如图 2 所示.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-096.jpg?height=589&width=558&top_left_y=1207&top_left_x=228)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-096.jpg?height=540&width=702&top_left_y=1223&top_left_x=935)

图 3

接下来想办法将 $\angle M F N$ 从难处理的椭圆中转移到容易处理的圆中. 如图 3 , 过 $A_{1}, B_{1}, C_{1}$ 分别作直线 $P^{\prime} A_{1}, P^{\prime} B_{1}, M^{\prime} N^{\prime}$ 与直线 $P A, P B, M N$ 平行, 这相当于以 $E$ 为中心, 将 $P M A, P N B$ 的长度放大到原来的两倍. 因此类似的将 $F$ 放大到 $F^{\prime}$ 的位置, 其中 $F^{\prime} E=2 F E$. 这样就有 $\angle M F N=\angle M^{\prime} F^{\prime} N^{\prime}$.

最后我们集中精力在圆中解决这个问题(如图 4 ).

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-096.jpg?height=526&width=703&top_left_y=2026&top_left_x=169)

图 4

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-096.jpg?height=524&width=712&top_left_y=2024&top_left_x=990)

图 5
设 $P^{\prime} A_{1}, P^{\prime} B_{1}, M^{\prime} N^{\prime}$ 分别与圆交于点 $X, Y, Z$, 连结 $F^{\prime} X, F^{\prime} Y, F^{\prime} Z, Z X, Z Y$.

由于 $F$ 平分 $F^{\prime} E$ 且为圆心, 于是 $F^{\prime} X \perp P^{\prime} A_{1}, F^{\prime} Y \perp P^{\prime} B_{1}, F^{\prime} Z \perp M^{\prime} N^{\prime}$, 进而 $Z, M^{\prime}, X, F^{\prime}$ 四点共圆, $Z$, $Y, N^{\prime}, F^{\prime}$ 四点共圆.

于是所求角

$$
\begin{aligned}
\angle M^{\prime} F^{\prime} N & =\angle M^{\prime} F^{\prime} Z+\angle N^{\prime} F^{\prime} Z \\
& =\angle M^{\prime} X Z+\left(\pi-\angle Z Y B_{1}\right) \\
& =\pi-\angle A_{1} X Z+\pi^{-} \angle Z Y B_{1}
\end{aligned}
$$

因此 $\angle M^{\prime} F^{\prime} N^{\prime}$ 的大小始终为弧 $A_{1} C_{1} B_{1}$ 所对的圆周角, 与 $C_{1}$ 的位置无关. 进而 $\angle M F N$ 的大小是固定的, 而与 $C$ 的位置无关, 原命题得证.

最后给出所有辅助线的“全家福”如图 5.

思考与总结

作椭圆的某个焦点关于切线的对称点,那么该点位于另一焦点与切点所在的直线上 (三点共线), 且该点到另一焦点的距离为椭圆的长轴长 (位于以另一焦点为圆心, 长轴长为半径的圆上).

## 第 626 题椭圆的光学性质

对于两条互相垂直的直线和一个椭圆, 已知椭圆无论如何滑动都与两条直线相切, 求椭圆中心的轨迹.

解析 如图, 由椭圆的几何性质,

$$
\left|F_{1}^{\prime} F_{2}\right|=\left|F_{1} F_{2}^{\prime}\right|=2 a \text {. }
$$

设 $O^{\prime}(x, y)$, 则 $F_{1}(x-c \cos \theta, y+c \sin \theta), F_{2}(x+c \cos \theta, y-c \sin \theta)$, $F_{1}^{\prime}(-x+c \cos \theta, y+c \sin \theta), F_{2}^{\prime}(x+c \cos \theta,-y+c \sin \theta)$,

所以

$$
\begin{aligned}
& \left|F_{1} F_{2}^{\prime}\right|^{2}=4 a^{2}=4 c^{2} \cos ^{2} \theta+4 y^{2}, \\
& \left|F_{2} F_{1}^{\prime}\right|^{2}=4 a^{2}=4 c^{2} \sin ^{2} \theta+4 x^{2}
\end{aligned}
$$

两式相加, 有

$$
x^{2}+y^{2}=2 a^{2}-c^{2}=a^{2}+b^{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-097.jpg?height=421&width=395&top_left_y=1306&top_left_x=1461)

所以 $P$ 点的轨迹是以两条互相垂直的直线的交点为圆心, $\sqrt{a^{2}+b^{2}}$ 为半径的圆. 即蒙日圆.

## 第 627 题 椭圆的几何性质

已知 $P$ 为椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ 上位于第一象限内的点, $F_{1}, F_{2}$ 为椭圆的左、右焦点, 则 $\angle F_{1} P F_{2}$ 的角平分线与 $y$ 轴交点的纵坐标 $t$ 的取值范围是

解析 $\left(-\frac{c^{2}}{b}, 0\right)$.

解法一 设 $P(m, n), m, n>0$, 则点 $P$ 处的切线斜率 $k=-\frac{b^{2} m}{a^{2} n}$, 根据植圆的光学性质, 可得角平分线的斜率为 $\frac{a^{2} n}{b^{2} m}$, 于是有

$$
\frac{n-t}{m-0}=\frac{a^{2} n}{b^{2} m}
$$

于是

$$
t=-\frac{c^{2}}{b^{2}} \cdot n
$$

其中 $c$ 为椭圆的半焦距. 考虑到 $n$ 的取值范围是 $(0, b)$, 于是 $t$ 的取值范围是 $\left(-\frac{c^{2}}{b}, 0\right)$.

解法二 如图, 设 $P(m, n), m, n>0$, 设 $\angle F_{1} P F_{2}$ 的角平分线与 $x$ 轴的交点为 $S(s, 0)$, 由角平分线定理及焦半径公式得

$$
\frac{s+c}{c-s}=\frac{a+e m}{a-e m}
$$

于是解得 $s=\frac{c^{2}}{a^{2}} m$, 由截距坐标公式得

$$
t=\frac{s \cdot n-m \cdot 0}{s-m}=\frac{\frac{c^{2}}{a^{2}} m \cdot n}{\frac{c^{2}}{a^{2}} m-m}=-\frac{c^{2}}{b^{2}} n
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-098.jpg?height=321&width=373&top_left_y=520&top_left_x=1387)

因此 $t$ 的取值范围是 $\left(-\frac{c^{2}}{b}, 0\right)$.

## 第 628 题 曲线系证共圆

已知 $A$ 是椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的右顶点, 弦 $P Q$ (不过点 $A$ ) 的斜率为定值 $k$, 求证: $\triangle A P Q$ 的外接圆恒过不同于点 $A$ 的另一点 $B$, 并求出 $B$ 点坐标.

解析 $\left(\frac{a^{2} k^{2}-b^{2}}{a^{2} k^{2}+b^{2}} \cdot a, \frac{2 a b k}{a^{2} k^{2}+b^{2}} \cdot b\right)$.

解法一 如图.

结论 已知 $E$ 是对称轴与坐标轴方向平行或垂直的非圆二次曲线, $A$, $B, C, D$ 是曲线 $E$ 上的四个不同点, 直线 $A C$ 与直线 $B D$ 相交且斜率均存在,求证: $A, B, C, D$ 四点共圆的充要条件是直线 $A C$ 与直线 $B D$ 的斜率互为相反数.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-098.jpg?height=349&width=485&top_left_y=1391&top_left_x=1277)

证明 设 $E$ 的方程为 $A x^{2}+B y^{2}+D x+E y+F=0$, 其中 $A^{2}+B^{2} \neq 0$ 且 $A \neq B$, 直线 $A C, B D$ 的方程分别为

$$
A C: k_{1} x-y+m_{1}=0, B D: k_{2} x-y+m_{2}=0,
$$

则曲线 $A C \cup B D$ 与曲线 $E$ 形成交点曲线系

$$
\left(k_{1} x-y+m_{1}\right)\left(k_{2} x-y+m_{2}\right)+\lambda\left(A x^{2}+B y^{2}+D x+E y+F\right)=0,
$$

因此 $A, B, C, D$ 四点共圆的充要条件是该方程不含交叉项 $x y$, 也即 $k_{1}$ 与 $k_{2}$ 互为相反数, 证毕.

这就意味着在本题中, 过点 $A$ 且斜率为 $-k$ 的直线与椭圆的交点 (不同于点 $A$ ) 恒在 $\triangle A P Q$ 的外接圆上, 也就是所要求的定点 $B$.

联立直线 $A B: x=-\frac{1}{k} y+a$ 与椭圆方程, 可得

$$
\left(\frac{1}{k^{2} a^{2}}+\frac{1}{b^{2}}\right) y^{2}-\frac{2}{k a} y=0
$$

因此 $B$ 点的纵坐标为

$$
\frac{2 a b^{2} k}{a^{2} k^{2}+b^{2}}
$$

进而可得其横坐标为

$$
\frac{a^{2} k^{2}-b^{2}}{a^{2} k^{2}+b^{2}} \cdot a
$$

因此所求的定点 $B$ 的坐标为

$$
\left(\frac{a^{2} k^{2}-b^{2}}{a^{2} k^{2}+b^{2}} \cdot a, \frac{2 a b k}{a^{2} k^{2}+b^{2}} \cdot b\right)
$$

解法二 设直线 $P Q$ 的方程为 $y=k x+m, \triangle A P Q$ 的外接圆方程为

$$
x^{2}+y^{2}+D x+E y-a^{2}-D a=0
$$

将直线 $P Q$ 的方程分别与圆的方程和棙圆的方程联立, 对比系数后可以将 $D$ 和 $E$ 用 $m$ 表示, 进而代人圆的方程整理为关于 $m$ 的代数式即可计算.

具体过程如下:

联立消元后分别得到

$$
\begin{gathered}
\left(\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}\right) x^{2}+\frac{2 k m}{b^{2}} x+\left(\frac{m^{2}}{b^{2}}-1\right)=0 \\
\left(1+k^{2}\right) x^{2}+(2 k m+k E+D) x+\left(m^{2}+E m-a^{2}-D a\right)=0
\end{gathered}
$$

于是得到

$$
\begin{aligned}
\left(\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}\right):\left(1+k^{2}\right) & =\frac{2 k m}{b^{2}}:(2 k m+k E+D) \\
& =\frac{m^{2}-b^{2}}{b^{2}}:\left(m^{2}+E m-a^{2}-D a\right),
\end{aligned}
$$

解得

$$
\left\{\begin{array}{l}
D=\frac{k\left(a^{2}-b^{2}\right)\left(m^{2}+b^{2}-1\right)}{(m+k a)\left(b^{2}+a^{2} k^{2}\right)} \\
E=\frac{\left(a^{2}-b^{2}\right)\left(m^{2}+2 m k a-b^{2}+1\right)}{(m+k a)\left(b^{2}+a^{2} k^{2}\right)}
\end{array}\right.
$$

代人外接圆的方程可以整理得到一个关于 $m$ 的形式上的一元二次方程, 于是 $m^{2}$ 与 $m$ 前面的系数均为零, 得到

$$
\left\{\begin{array}{l}
k x+y-k a=0, \\
\left(x^{2}+y^{2}-a^{2}\right)\left(b^{2}+a^{2} k^{2}\right)+2 k a y\left(a^{2}-b^{2}\right)=0,
\end{array}\right.
$$

将 $y=k(a-x)$ 代人得到

$$
x=\frac{a\left(k^{2} a^{2}-b^{2}\right)}{k^{2} a^{2}+b^{2}}, y=\frac{2 k a b^{2}}{k^{2} a^{2}+b^{2}}
$$

因此所求的定点 $B$ 的坐标为

$$
\left(\frac{a^{2} k^{2}-b^{2}}{a^{2} k^{2}+b^{2}} \cdot a, \frac{2 a b k}{a^{2} k^{2}+b^{2}} \cdot b\right)
$$

## 第 629 题 勘破玄机

已知椭圆 $\frac{x^{2}}{5}+y^{2}=1$, 过点 $P(0,2)$ 的直线 $l$ 交椭圆于 $M, N$ 两点, 若 $\overrightarrow{P M}=\lambda \overrightarrow{P N}$, 则 $\lambda$ 的取值范围是

解析 $\left(\frac{1}{3}, 3\right)$.

当点 $M$ 在 $P, N$ 之间时, 作点 $M, N$ 在 $y$ 轴上的投影点 $M_{1}, N_{1}$, 则 $\lambda=\frac{\left|P M_{1}\right|}{\left|P N_{1}\right|}$, 显然其取值范围是 $\left[\frac{1}{3}, 1\right)$.

因此当点 $N$ 在 $P, M$ 之间时, $\alpha$ 的取值范围是 $(1,3]$,

从而 $\lambda$ 的取值范围是 $\left[\frac{1}{3}, 1\right) \cup(1,3]$.
另法 设直线 $l$ 的方程为 $y=k x+2$, 与椭圆方程联立消元得

$$
\left(k^{2}+\frac{1}{5}\right) x^{2}+4 k x+3=0
$$

令点 $M, N$ 的横坐标分别为 $x_{1}, x_{2}$, 则有 $\lambda=\frac{x_{1}}{x_{2}}$,

则根据两根比公式得

$$
16 k^{2}-\left(\lambda+\frac{1}{\lambda}+2\right) \cdot 3\left(k^{2}+\frac{1}{5}\right)=0
$$

整理得

$$
\lambda+\frac{1}{\lambda}+2=\frac{16 k^{2}}{3 k^{2}+\frac{3}{5}}
$$

由联立方程的判别式为正得到 $k^{2}>\frac{3}{5}$, 从而得到

$$
\frac{16 k^{2}}{3 k^{2}+\frac{3}{5}} \in\left(4, \frac{16}{3}\right)
$$

即 $2<\lambda+\frac{1}{\lambda}<\frac{10}{3}$, 解得 $\frac{1}{3}<\lambda<3$.

## 第 630 题 构造双曲线

已知 $\triangle A B C$ 中, $A M$ 为 $B C$ 边上的中线 (点 $M$ 在 $B C$ 边上), 且满足 $A M=A B-A C, B C=4$. 求点 $A$到直线 $B C$ 距离的最大值.

## 解析 如图建系.

设 $A M=2 a$, 则 $A$ 点为双曲线 $E: \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ (其中 $a^{2}+b^{2}=4$ ) 和圆 $F: x^{2}+y^{2}$ $=4 a^{2}$ 的交点, 于是可得

$$
\frac{y^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=3
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-100.jpg?height=226&width=397&top_left_y=1449&top_left_x=1364)

进而

$$
y^{2}=\frac{3}{2} \cdot \frac{2}{\frac{1}{a^{2}}+\frac{1}{b^{2}}} \leqslant \frac{3}{2} \cdot \frac{a^{2}+b^{2}}{2}=3
$$

等号当且仅当 $a=b=\sqrt{2}$ 时取得.

因此所求点 $A$ 到直线 $B C$ 的最大距离为 $\sqrt{3}$.

恰当地将等式的两边拆解为两个轨迹的公共点, 利用双曲线的定义与方程简化运算.

## 第 631 题 拓展的定义和定理

如图 1, 动点 $M$ 与两定点 $A(-1,0), B(2,0)$ 构成 $\triangle M A B$, 且 $\angle M B A=$ $2 \angle M A B$, 设动点 $M$ 的轨迹为 $C$.

(1) 求轨迹 $C$ 的方程;

(2) 设直线 $y=-2 x+m$ 与 $y$ 轴相交于点 $P$, 与轨迹 $C$ 相交于点 $Q 、 R$, 且 $|P Q|<|P R|$, 求 $\frac{|P R|}{|P Q|}$ 的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-101.jpg?height=321&width=319&top_left_y=438&top_left_x=1517)

图 1

解析 (1) 注意到倍角条件, 可以作角平分线构造等腰三角形转化条件.

作 $\angle M B A$ 的角平分线交 $M A$ 于点 $D$, 过点 $D$ 作 $x$ 轴的垂线, 垂足为 $E$, 过点 $M$ 作 $D E$ 的垂线, 垂足为点 $H$, 如图 2.

根据已知条件可得 $\angle D A B=\angle D B A$, 于是 $D E$ 为线段 $A B$ 的垂直平分线, 为定直线 $x=\frac{1}{2}$. 由角平分线定理, 可得

$$
\frac{B M}{B A}=\frac{D M}{D A}
$$

再由 $\triangle D M H$ 与 $\triangle D A E$ 相似可得

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-101.jpg?height=346&width=332&top_left_y=853&top_left_x=1543)

图 2

$$
\frac{D M}{D A}=\frac{M H}{A E}
$$

于是

$$
\frac{B M}{B A}=\frac{M H}{A E}
$$

从而

$$
\frac{M B}{M H}=\frac{B A}{A E}=2
$$

为定值.

进而由双曲线的第二定义不难得到所求的轨迹方程为

$$
x^{2}-\frac{y^{2}}{3}=1, x>1
$$

(2) 设 $Q\left(x_{1}, y_{1}\right), R\left(x_{2}, y_{2}\right), \frac{x_{2}}{x_{1}}=\lambda, \lambda>1$. 联立直线与双曲线方程, 可得

$$
x^{2}-4 m x+m^{2}+3=0,
$$

该方程在 $(1,+\infty)$ 内有两个相异实根, 于是可得 $m>1$ 且 $m \neq 2$. 根据韦达定理, 有

$$
(4 m)^{2}=\left(2+\lambda+\frac{1}{\lambda}\right) \cdot\left(m^{2}+3\right)
$$

化简得

$$
\lambda+\frac{1}{\lambda}=\frac{16 m^{2}}{m^{2}+3}-2
$$

于是 $\lambda+\frac{1}{\lambda}$ 的取值范围是 $\left(2, \frac{50}{7}\right) \cup\left(\frac{50}{7}, 14\right)$, 进而不难得到 $\lambda$ 的取值范围是 $(1,7) \cup(7,7+4 \sqrt{3})$.

## 第 632 题 交轨定动点

在 $\triangle A B C$ 中, $M$ 是 $B C$ 的中点, $B M=2, A M=A B-A C$, 则 $\triangle A B C$ 的面积的最大值为 $\qquad$
解析 $2 \sqrt{3}$.

解法一 如图, 以 $B C$ 所在直线为 $x$ 轴, 以 $M$ 为坐标原点建立平面直角坐标系, $\triangle A B C$ 的面积只与 $A$ 点的纵坐标相关.

设 $A M$ 的长为 $2 a$, 则点 $A$ 既在以 $M$ 为圆心, $2 a$ 为半径的圆上, 也在以 $B, C$ 为焦点, 实轴长为 $2 a$ 的双曲线右支上, 联立圆与双曲线的方程有

$$
\left\{\begin{array}{l}
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{a^{2}}=4 \\
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{4-a^{2}}=1
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-102.jpg?height=351&width=348&top_left_y=592&top_left_x=1416)

两式相减得

$$
y^{2}=\frac{3}{4} a^{2}\left(4-a^{2}\right) \leqslant 3
$$

当且仅当 $a=\sqrt{2}$ 时取到等号, 所以

$$
\left(S_{\triangle A B C}\right)_{\max }=\frac{1}{2} \cdot 4 \cdot \sqrt{3}=2 \sqrt{3}
$$

解法二 由中线长定理可知

$$
A C^{2}+A B^{2}=2\left(A M^{2}+M B^{2}\right)
$$

整理可得

$$
b^{2}+c^{2}=4 b c-8
$$

又由余弦定理有

$$
16=a^{2}=b^{2}+c^{2}-2 b c \cos A=4 b c-8-2 b c \cos A,
$$

整理得

$$
b c=\frac{12}{2-\cos A}, 0<\angle A<\frac{\pi}{2}
$$

于是

$$
S_{\triangle A B C}=\frac{1}{2} b c \sin A=\frac{6 \sin A}{2-\cos A} \leqslant 2 \sqrt{3},
$$

当且仅当 $\angle A=\frac{\pi}{3}$ 时取得最大值.

## 第 633 题 双曲线的参数方程

给定双曲线 $C: \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0, b>0)$, 过它的一个焦点作直线 $l$, 交 $C$ 于点 $P$ 和 $Q, A_{1}, A_{2}$ 分别为 $C$ 的实轴端点, 求 $P A_{1}$ 与 $Q A_{2}$ 的交点的轨迹方程.

解析 设 $P(a \sec 2 \alpha, b \tan 2 \alpha), Q(a \sec 2 \beta, b \tan 2 \beta)$, 不妨设 $A_{1}(a, 0), A_{2}(-a, 0)$, 则根据双曲线的参数方程, 直线 $P A_{1}$ 与直线 $Q A_{2}$ 的方程分别为

$$
\left\{\begin{array}{l}
P A_{1}: \cos \alpha \cdot \frac{x}{a}-\sin \alpha \cdot \frac{y}{b}=\cos \alpha \\
Q A_{2}: \sin \beta \cdot \frac{x}{a}-\cos \beta \cdot \frac{y}{b}=-\sin \beta
\end{array}\right.
$$

联立可得

$$
x=\frac{1+\tan \alpha \cdot \tan \beta}{1-\tan \alpha \cdot \tan \beta} \cdot a
$$

从而有

$$
\tan \alpha \cdot \tan \beta=\frac{a-c}{a+c}
$$

或

$$
\tan \alpha \cdot \tan \beta=\frac{a+c}{a-c}
$$

于是直线 $P A_{1}$ 与 $Q A_{2}$ 的交点的轨迹方程为 $x= \pm \frac{a^{2}}{c}$.

若将条件“ $P Q$ 过焦点”修改为“直线 $P Q$ 过定点 $(m, 0)$ ”, 那么对应的轨迹方程为 $x=\frac{a^{2}}{m}$.

## 第 634 题 相似三角形

设双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a, b>0)$ 的右焦点为 $F$, 右顶点为 $A$, 过点 $F$ 作 $A F$ 的垂线与双曲线交于 $B, C$两点, 过点 $B, C$ 分别作 $A C, A B$ 的垂线, 两垂线交于点 $D$. 若点 $D$ 到直线 $B C$ 的距离小于 $a+\sqrt{a^{2}+b^{2}}$,则该双曲线的渐近线斜率的取值范围是
A. $(-1,0) \cup(0,1)$
B. $(-\infty,-1) \cup(1,+\infty)$
C. $(-\sqrt{2}, 0) \cup(0, \sqrt{2})$
D. $(-\infty,-\sqrt{2}) \cup(\sqrt{2},+\infty)$

## 解析 A.

如图, 根据已知条件 $\triangle B D F$ 与 $\triangle A B F$ 相似.

于是

$$
B F^{2}=A F \cdot D F,
$$

即

$$
D F=\left(\frac{b^{2}}{a}\right)^{2} \cdot \frac{1}{c-a}<a+\sqrt{a^{2}+b^{2}}=c+a
$$

整理得

$$
b^{2}<a^{2},
$$

于是该双曲线的渐近线的斜率的取值范围是 $(-1,0) \cup(0,1)$. 故选 A.

## 第 635 题 探索单调性

如图, 已知双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ 的左、右焦点分别为 $F_{1}, F_{2}$, 过点 $F_{2}$ 作直线与双曲线右支交于 $P, Q$ 两点, 且 $P F_{1} \perp P Q$. 记 $\lambda=\frac{|P Q|}{\left|P F_{1}\right|}$, 若 $\lambda \in$ $\left[\frac{5}{12}, \frac{4}{3}\right]$, 则双曲线离心率的取值范围是 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-104.jpg?height=425&width=422&top_left_y=436&top_left_x=1326)

解析 $\left[\frac{\sqrt{37}}{5}, \frac{\sqrt{10}}{2}\right]$.

不妨设 $a=1$, 则 $\left|F_{1} F_{2}\right|=2 e$, 其中 $e$ 为双曲线的离心率. 设 $\left|P F_{1}\right|=x$, 则 $|P Q|=\lambda x,\left|P F_{2}\right|=x-2$, $\left|Q F_{2}\right|=(\lambda-1) x+2,\left|Q F_{1}\right|=(\lambda-1) x+4$, 其中 $x>2$.

根据题意有

$$
\left\{\begin{array}{l}
x^{2}+(\lambda x)^{2}=[(\lambda-1) x+4]^{2}, \\
x^{2}+(x-2)^{2}=(2 e)^{2},
\end{array}\right.
$$

整理得

$$
\left\{\begin{array}{l}
\left(x^{2}-4 x\right) \cdot \lambda+4 x-8=0 \\
2 e^{2}=x^{2}-2 x+2
\end{array}\right.
$$

由第一个式子可得

$$
\frac{4}{\lambda}=\frac{4 x-x^{2}}{x-2}=2-x+\frac{4}{x-2},
$$

于是随着 $\lambda$ 的增大, $\frac{4}{\lambda}$ 减小, 而 $x$ 增大, 进而离心率 $e$ 增大, 因此 $e$ 是关于 $\lambda$ 的单调递增函数.

设 $t_{0}=x-2$, 则 $t_{0}$ 是关于 $t$ 的方程

$$
t^{2}+\frac{4}{\lambda} t-4=0
$$

的正根, 于是

$$
x=-\frac{2}{\lambda}+2 \sqrt{\frac{1}{\lambda^{2}}+1}+2
$$

因此 $x$ 的取值范围为 $\left[\frac{12}{5}, 3\right]$, 对应的离心率 $e$ 的取值范围是 $\left[\frac{\sqrt{37}}{5}, \frac{\sqrt{10}}{2}\right]$.

## 第 636 题 双曲线的焦半径公式

过双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0, b>0)$ 的一个焦点作平行于渐近线的两直线, 与双曲线分别交于 $A, B$ 两点, 若 $|A B|=2 a$, 双曲线的离心率为 $e$, 则 $\left[e^{2}\right]=$

## 解析 3.

解法一 设 $\angle A F O=\theta$, 则由双曲线的焦半径公式, 有

$$
|A F|=\frac{b^{2}}{a+c \cdot \cos \theta}=\frac{b^{2}}{2 a}
$$

因此

$$
\sin \theta=\frac{a}{|A F|}=\frac{b}{c}
$$

从而 $b^{3}=2 a^{2} c$, 不妨设 $a=1, c=e, b=\sqrt{e^{2}-1}$, 则

$$
\left(e^{2}-1\right)^{3}=4 e^{2}
$$

如图,可得 $3<e^{2}<4$,于是 $\left[e^{2}\right]=3$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-105.jpg?height=442&width=368&top_left_y=191&top_left_x=1508)

解法二 由双曲线的对称性知 $A B \perp x$ 轴, 不妨设点 $A$ 在 $x$ 轴上方, 则 $A$ 点的坐标为 $\left(-\frac{a c}{b}, a\right)$, 从而有

$$
k_{A F}=\frac{a}{-\frac{a c}{b}+c}=\frac{b}{a}
$$

整理得

$$
a^{2}=b c-a c=\sqrt{c^{2}-a^{2}} c-a c
$$

从而知双曲线的离心率 $e$ 满足

$$
e^{3}-e^{2}-e-1=0
$$

记 $f(x)=x^{3}-x^{2}-x-1$, 则

$$
f^{\prime}(x)=(x-1)(3 x+1)
$$

所以 $f(x)$ 在 $(1,+\infty)$ 上单调递增, 而

$$
f(\sqrt{3})<0, f(2)>0
$$

所以 $e \in(\sqrt{3}, 2)$, 从而有 $\left[e^{2}\right]=3$.

## 第 637 题 直线与双曲线

已知直线 $y=\frac{2 \sqrt{5}}{5} x$ 与双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a, b>0)$ 交于 $A, B$ 两点, 若在双曲线上存在点 $P$, 使得 $|P A|=|P B|=\frac{\sqrt{3}}{2}|A B|$, 则双曲线的离心率 $e$ 为

解析 $\sqrt{3}$.

不妨设 $|O A|=1$, 则 $|O P|=\sqrt{2}$. 进而可设 $A(\cos \theta, \sin \theta), P\left(\sqrt{2} \cos \left(\theta+\frac{\pi}{2}\right), \sqrt{2} \sin \left(\theta+\frac{\pi}{2}\right)\right)$, 其中 $\tan \theta=$ $\frac{2 \sqrt{5}}{5}$. 这样就有

$$
\left\{\begin{array}{l}
\frac{\cos ^{2} \theta}{a^{2}}-\frac{\sin ^{2} \theta}{b^{2}}=1 \\
\frac{\left[\sqrt{2} \cos \left(\theta+\frac{\pi}{2}\right)\right]^{2}}{a^{2}}-\frac{\left[\sqrt{2} \sin \left(\theta+\frac{\pi}{2}\right)\right]^{2}}{b^{2}}=1
\end{array}\right.
$$

即

$$
\left\{\begin{array}{l}
\frac{5}{9 a^{2}}-\frac{4}{9 b^{2}}=1 \\
\frac{4}{9 a^{2}}-\frac{5}{9 b^{2}}=\frac{1}{2}
\end{array}\right.
$$

解得

$$
a^{2}=\frac{1}{3}, b^{2}=\frac{2}{3}
$$

于是 $e^{2}=\frac{a^{2}+b^{2}}{a^{2}}=3$, 所求离心率 $e=\sqrt{3}$.

## 第 638 题 圆与双曲线

设 $F_{1}, F_{2}$ 为双曲线 $C: \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a, b>0)$ 的左、右焦点, 双曲线 $C$ 与圆 $x^{2}+y^{2}=r^{2}$ 的一个交点为 $P$, 若 $\frac{\left|P F_{1}\right|+\left|P F_{2}\right|}{r}$ 的最大值为 $4 \sqrt{2}$, 则双曲线的离心率 $e$ 为

解析 $2 \sqrt{2}$.

设 $P(r \cos \theta, r \sin \theta)$, 则由双曲线的焦半径公式, 有

$$
\frac{\left|P F_{1}\right|+\left|P F_{2}\right|}{r}=\frac{e \cdot r \cos \theta+a+e \cdot r \cos \theta-a}{r}=2 e \cos \theta
$$

显然当 $\theta=0$ 时该式取得最大值, 从而 $e=2 \sqrt{2}$.

## 第 639 题 焦半径公式的应用

如图, 设 $F$ 为双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ 的左焦点, 在 $x$ 轴上 $F$ 点的右侧有一点 $A$, 以 $F A$ 为直径的圆与双曲线左、右两支在 $x$ 轴上方的交点分别为 $M, N$, 则 $\frac{|F N|-|F M|}{|F A|}=$ $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-106.jpg?height=295&width=295&top_left_y=1330&top_left_x=1455)

解析 $\frac{a}{c}$.

解法一 设 $\angle M F A=\alpha, \angle N F A=\beta$, 则

$$
|F M|=\frac{b^{2}}{c \cos \alpha+a},|F N|=\frac{b^{2}}{c \cos \beta-a}
$$

两式相比可得

$$
\frac{|F M|}{|F N|}=\frac{c \cdot \frac{|F N|}{|F A|}-a}{c \cdot \frac{|F M|}{|F A|}+a}=\frac{c|F N|-a|F A|}{c|F M|+a|F A|}
$$

即

$$
c|F M|^{2}+a|F A| \cdot|F M|=c|F N|^{2}-a|F A| \cdot|F N|
$$

也即

$$
(|F M|+|F N|) \cdot(c|F M|-c|F N|+a|F A|)=0
$$

从而可得

$$
\frac{|F N|-|F M|}{|F A|}=\frac{a}{c}
$$

解法二 设 $A(m, 0)(m>-c)$, 由圆的直径式方程可得以 $F A$ 为直径的圆的方程为

$$
(x+c)(x-m)+y^{2}=0
$$

## 高考数学满分学霸的解题笔记(一千零一题)

设 $M, N$ 的横坐标分别为 $x_{1}, x_{2}$, 则由焦半径公式, 有

$$
|F M|=-\frac{c}{a} x_{1}-a,|F N|=\frac{c}{a} x_{2}+a,
$$

于是

$$
\frac{|F N|-|F M|}{|F A|}=\frac{\frac{c}{a}\left(x_{1}+x_{2}\right)+2 a}{m+c}
$$

联立圆的方程与双曲线方程, 有

$$
\frac{c^{2}}{a^{2}} x^{2}+(c-m) x-c m-b^{2}=0
$$

于是

$$
x_{1}+x_{2}=\frac{a^{2}(m-c)}{c^{2}}
$$

代人上式,可得

$$
\frac{|F N|-|F M|}{|F A|}=\frac{\frac{c}{a} \cdot \frac{a^{2}(m-c)}{c^{2}}+2 a}{m+c}=\frac{a}{c}
$$

## 第 640 题 利用边界条件解题

已知 $M\left(x_{0}, y_{0}\right)$ 是双曲线 $C: \frac{x^{2}}{2}-y^{2}=1$ 上的一点, $F_{1}, F_{2}$ 是 $C$ 的两个焦点, 若 $\overrightarrow{M F_{1}} \cdot \overrightarrow{M F_{2}}<0$, 则 $y_{0}$ 的取值范围是
A. $\left(-\frac{\sqrt{3}}{3}, \frac{\sqrt{3}}{3}\right)$
B. $\left(-\frac{\sqrt{3}}{6}, \frac{\sqrt{3}}{6}\right)$
C. $\left(-\frac{2 \sqrt{2}}{3}, \frac{2 \sqrt{2}}{3}\right)$
D. $\left(-\frac{2 \sqrt{3}}{3}, \frac{2 \sqrt{3}}{3}\right)$

## 解析 A.

解法一 考虑条件 $\overrightarrow{M F_{1}} \cdot \overrightarrow{M F_{2}}<0$ 的边界情形为 $\overrightarrow{M F_{1}} \cdot \overrightarrow{M F_{2}}=0$, 几何意义为点 $M$ 的轨迹是以 $F_{1}, F_{2}$为直径端点的圆. 进而可知符合题意的点 $M$ 均在圆内, 如图 1.

根据双曲线的焦点三角形面积公式, 有

$$
S_{\triangle M F_{1} F_{2}}=1^{2} \cdot \cot \frac{90^{\circ}}{2}=1
$$

另一方面, $\triangle M F_{1} F_{2}$ 的底 $F_{1} F_{2}$ 的长为 $2 \sqrt{3}$, 于是可得其边 $F_{1} F_{2}$ 上的高为 $\frac{\sqrt{3}}{3}$.

因此可得所求 $y_{0}$ 的取值范围是 $\left(-\frac{\sqrt{3}}{3}, \frac{\sqrt{3}}{3}\right)$. 故选 A.

解法二 考虑条件 $\overrightarrow{M F_{1}} \cdot \overrightarrow{M F_{2}}<0$ 的边界情形为 $\overrightarrow{M F_{1}} \cdot \overrightarrow{M F_{2}}=0$, 几何意义为点 $M$ 的轨迹是以 $F_{1}, F_{2}$ 为直径端点的圆. 进而可知符合题意的点 $M$ 均在圆内, 如图 2.

因此由

$$
\left\{\begin{array}{l}
x^{2}+y^{2}<3 \\
\frac{x^{2}}{2}-y^{2}=1
\end{array}\right.
$$

可得

$$
y^{2}<\frac{1}{3}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-107.jpg?height=372&width=380&top_left_y=1636&top_left_x=1479)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-107.jpg?height=391&width=385&top_left_y=2014&top_left_x=1476)

图 2

故选 A.

## 第 641 题 双曲线的垂径定理

如图, 双曲线 $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a, b>0)$ 的右顶点为 $A$, 左右焦点分别为 $F_{1}, F_{2}$, 点 $P$是双曲线右支上一点, $P F_{1}$ 交左支于点 $Q$, 交渐近线 $y=\frac{b}{a} x$ 于点 $R, M$ 是 $P Q$ 的中点, 若 $R F_{2} \perp P F_{1}$, 且 $A M \perp P F_{1}$, 则双曲线的离心率为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-108.jpg?height=308&width=314&top_left_y=446&top_left_x=1436)

## 解析 2.

题中条件为一个“中点”加两组“垂直”, 其中 $F_{2} R \perp R F_{1}$ 可以通过直角三角形的斜边中线转化为 $O R=$ $\frac{1}{2} F_{1} F_{2}=c$, 其中 $c$ 为双曲线的半焦距. 又由于点 $R$ 在渐近线上, 于是点 $R$ 的坐标为 $(a, b)$. 接下来的关键是如何恰当地表示中点,这就用到了双曲线的“垂径定理”.

直线 $P F_{1}$ 的斜率为 $\frac{b}{a+c}$, 设 $M(m, n)$, 则

$$
\left\{\begin{array}{l}
\frac{n}{m} \cdot \frac{b}{a+c}=\frac{b^{2}}{a^{2}} \\
\frac{n}{m-a} \cdot \frac{b}{a+c}=-1 \\
\frac{n}{m+c}=\frac{b}{a+c}
\end{array}\right.
$$

其中第一个方程来源于双曲线的“垂径定理”.

第一个式子与第二个式子相除, 可得

$$
\frac{m-a}{m}=-\frac{b^{2}}{a^{2}}
$$

即

$$
m=\frac{a^{3}}{c^{2}}
$$

第一个式子与第三个式子相除, 可得

$$
\frac{m+c}{m} \cdot \frac{b}{a+c}=\frac{b^{2}}{a^{2}} \cdot \frac{a+c}{b}
$$

将 $m=\frac{a^{3}}{c^{2}}$ 代人, 并整理可得

$$
e^{2}-e-2=0
$$

于是 $e=2$, 其中 $e=\frac{c}{a}$ 为双曲线的离心率.

## 第 642 题 焦点弦长

设 $t$ 是正实数, 双曲线 $x^{2}-y^{2}=t$ 的右焦点为 $F$, 过点 $F$ 任作一条直线交双曲线的右支于 $A, B$ 两点, 设线段 $A B$ 的垂直平分线交 $x$ 轴于点 $P$, 则 $\frac{F P \mid}{|A B|}$ 的值为 $\qquad$ .
解析 $\frac{\sqrt{2}}{2}$.

解法一 如图 1. 不妨设 $t=1$, 于是 $F(\sqrt{2}, 0)$. 设 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 线段 $A B$的中点 $M\left(x_{0}, y_{0}\right)$, 直线 $A B$ 的斜率为 $k$.

由双曲线的第二定义, 可得

$$
|A B|=\sqrt{2}\left(x_{1}-\frac{\sqrt{2}}{2}\right)+\sqrt{2}\left(x_{2}-\frac{\sqrt{2}}{2}\right)=\frac{\sqrt{2}}{2}\left(x_{1}+x_{2}-\sqrt{2}\right)
$$

直线 $P M: x-x_{0}=-k\left(y-y_{0}\right)$,于是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-109.jpg?height=374&width=338&top_left_y=195&top_left_x=1522)

图 1

$$
|F P|=x_{0}+k y_{0}-\sqrt{2}
$$

根据双曲线的“垂径定理”, 有 $\frac{y_{0}}{x_{0}} \cdot k=1$, 于是 $k y_{0}=x_{0}$, 进而

$$
|F P|=2 x_{0}-\sqrt{2}=x_{1}+x_{2}-\sqrt{2}
$$

因此所求的比值为 $\frac{\sqrt{2}}{2}$.

## 思考与总结

看到焦点与计算弦长,联想第二定义;看到中点,联想“垂径定理”. 本题条件中的双曲线可以修改为一般的双曲线, 设其离心率为 $e$, 则 $\frac{|F P|}{|A B|}$ 的值为 $\frac{e}{2}$.

解法二 如图 2 , 不妨设直线 $A B$ 的倾斜角为锐角 $\theta$,且 $|A F|>|B F|$.

根据双曲线的第二定义, 有

$$
\frac{|F P|}{|A B|}=\frac{|M F|}{|A B| \cos \theta}=\frac{|A F|-|B F|}{2\left(\left|A A_{1}\right|-\left|B B_{1}\right|\right)}=\frac{\sqrt{2}}{2}
$$

## 第 643 题 抛物线的光学性质

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-109.jpg?height=374&width=338&top_left_y=1193&top_left_x=1519)

图 2

在平面直角坐标系 $x O y$ 中, 动点 $E$ 到定点 $(1,0)$ 的距离与它到直线 $x=-1$ 的距离相等.

(1) 求动点 $E$ 的轨迹 $C$ 的方程;

(2) 设动直线 $l: y=k x+b$ 与曲线 $C$ 相切于点 $P$, 与直线 $x=-1$ 相交于点 $Q$. 证明: 以 $P Q$ 为直径的圆恒过 $x$ 轴上的某定点.

解析 (1) 根据抛物线的定义可知动点 $E$ 的轨迹为抛物线, 其方程为 $C: y^{2}$ $=4 x$.

(2) 以 $P Q$ 为直径的圆恒过抛物线 $C$ 的焦点 $F(1,0)$, 证明如下.

如图, 过点 $P$ 作准线 $x=-1$ 的垂线, 垂足为 $H$.

由抛物线的光学性质有

$$
\angle F P Q=\angle Q P H
$$

根据抛物线的定义有

$$
P F=P H,
$$

因此 $\triangle P Q F$ 与 $\triangle P Q H$ 全等, 于是 $\angle P F Q$ 恒为直角,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-109.jpg?height=428&width=398&top_left_y=1930&top_left_x=1459)

进而以 $P Q$ 为直径的圆恒过抛物线 $C$ 的焦点 $F(1,0)$.
圆锥曲线的光学性质是我们处理切线问题的一大利器, 往往可以起到出奇制胜的效果.

## 第 644 题 直线与抛物线

在平面直角坐标系 $x O y$ 中, 抛物线 $C$ 的顶点是原点, 以 $x$ 轴为对称轴, 且经过点 $P(1,2)$.

(1)求抛物线 $C$ 的方程;

(2) 设点 $A, B$ 在抛物线 $C$ 上, 直线 $P A, P B$ 分别与 $y$ 轴交于点 $M, N,|P M|=|P N|$, 求直线 $A B$ 的斜率.

解析 解法一 (1) $y^{2}=4 x$.

(2) 设 $M(0,2+m), N(0,2-m)$, 则直线 $P M: y=-m x+2+m$, 与抛物线的方程联立可得

$$
m y^{2}+4 y-8-4 m=0
$$

于是点 $A$ 的纵坐标

$$
y_{1}=\frac{1}{2} \cdot \frac{-8-4 m}{m}=-\frac{4}{m}-2
$$

同理,点 $B$ 的纵坐标

$$
y_{2}=\frac{4}{m}-2
$$

因此直线 $A B$ 的斜率

$$
k=\frac{4}{y_{1}+y_{2}}=-1
$$

解法二 $(1)$ 见解法一.

(2) 设 $A\left(4 a^{2}, 4 a\right), B\left(4 b^{2}, 4 b\right)$, 则直线 $A B$ 的斜率

$$
k=\frac{4 a-4 b}{4 a^{2}-4 b^{2}}=\frac{1}{a+b}
$$

根据截距坐标公式, 可得点 $M, N$ 的纵坐标分别为

$$
y_{1}=\frac{1 \cdot 4 a-4 a^{2} \cdot 2}{1-4 a^{2}}=\frac{4 a}{1+2 a}, y_{2}=\frac{4 b}{1+2 b},
$$

根据题意, 有

$$
y_{1}+y_{2}=4
$$

即

$$
\frac{4 a}{1+2 a}+\frac{4 b}{1+2 b}=4
$$

整理可得

$$
a+b=-1
$$

因此所求直线 $A B$ 的斜率为 -1 .

## 第 645 题 以点构图

设直线 $l$ 与抛物线 $y^{2}=4 x$ 相交于 $A, B$ 两点, 与圆 $(x-5)^{2}+y^{2}=r^{2}(r>0)$ 相切于点 $M$, 且 $M$ 为线段 $A B$ 的中点. 若这样的直线 $l$ 恰有 4 条,则 $r$ 的取值范围是
A. $(1,3)$
B. $(1,4)$
C. $(2,3)$
D. $(2,4)$

## 解析 $D$.

如图, 记圆心为 $C(5,0)$, 设 $A\left(4 a^{2}, 4 a\right), B\left(4 b^{2}, 4 b\right)$.

显然无论 $r$ 为何值, 都存在 $a+b=0$ 的两个平凡解 (垂直于 $x$ 轴的两条切线), 因此只需要考虑 $a+b \neq 0$ 的情形.

由于 $M\left(2\left(a^{2}+b^{2}\right), 2(a+b)\right)$, 于是根据 $A B$ 与圆 $C$ 相切于点 $M$, 可得

$$
\frac{2(a+b)-0}{2\left(a^{2}+b^{2}\right)-5} \cdot \frac{4 a-4 b}{4 a^{2}-4 b^{2}}=-1
$$

即

$$
a^{2}+b^{2}=\frac{3}{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-111.jpg?height=426&width=333&top_left_y=240&top_left_x=1524)

于是

$$
r^{2}=C M^{2}=\left[2\left(a^{2}+b^{2}\right)-5\right]^{2}+[2(a+b)-0]^{2}=4+4(a+b)^{2}
$$

由

$$
0<(a+b)^{2}<2\left(a^{2}+b^{2}\right)=3
$$

得

$$
4<r^{2}<16
$$

于是所求 $r$ 的取值范围是 $(2,4)$.

事实上, 由于 $a^{2}+b^{2}=\frac{3}{2}$ 可得点 $M$ 的横坐标为定值, 结合图形易得.

## 第 646 题 正三角形遇到抛物线

已知正 $\triangle A B C$ 的顶点 $A, B$ 在抛物线 $y^{2}=4 x$ 上, 另一个顶点 $C(4,0)$, 求符合题意的正 $\triangle A B C$ 的个数.

解析 情形一 当 $A B$ 与 $x$ 轴垂直时, 显然有 2 个符合题意的正三角形.

情形二 当 $A B$ 与 $x$ 轴不垂直时, 设 $A\left(4 a^{2}, 4 a\right), B\left(4 b^{2}, 4 b\right)$, 且 $a<b$, 则直线 $A B$ 的方程为

$$
x-(a+b) y+4 a b=0,
$$

线段 $A B$ 的垂直平分线为

$$
(a+b) x+y-2(a+b)\left(a^{2}+b^{2}+1\right)=0
$$

考虑到 $C(4,0)$, 因此

$$
a^{2}+b^{2}=1
$$

此时有

$$
|A B|=4|a-b| \cdot \sqrt{(a+b)^{2}+1}=4 \sqrt{2} \cdot|a-b| \cdot \sqrt{a b+1},
$$

而点 $C$ 到直线 $A B$ 的距离

$$
d=\frac{4|a b+1|}{\sqrt{(a+b)^{2}+1}}=2 \sqrt{2} \cdot \sqrt{a b+1}
$$

根据题意, 有 $d=\frac{\sqrt{3}}{2}|A B|$, 于是

$$
1=\sqrt{3} \cdot|a-b|
$$

两边平方, 将 $a^{2}+b^{2}=1$ 代人, 有 $a b=\frac{1}{3}$.

考虑到方程组

$$
\left\{\begin{array}{l}
a^{2}+b^{2}=1 \\
a b=\frac{1}{3}
\end{array}\right.
$$

有 2 组不同的解,对应 2 个符合题意的正三角形.

综上,共有 4 个不同的正三角形.

情形一的两组解为

$$
\left\{\begin{array} { l } 
{ A ( 1 0 - 2 \sqrt { 2 1 } , 2 \sqrt { 3 } - 2 \sqrt { 7 } ) , } \\
{ B ( 1 0 - 2 \sqrt { 2 1 } , 2 \sqrt { 7 } - 2 \sqrt { 3 } ) }
\end{array} \quad \text { 及 } \left\{\begin{array}{l}
A(10+2 \sqrt{21}, 2 \sqrt{3}+2 \sqrt{7}), \\
B(10+2 \sqrt{21},-2 \sqrt{3}-2 \sqrt{7}),
\end{array}\right.\right.
$$

情形二的两组解为

$$
\left\{\begin{array} { l } 
{ A ( \frac { 6 - 2 \sqrt { 5 } } { 3 } , \frac { 2 \sqrt { 1 5 } - 2 \sqrt { 3 } } { 3 } ) , } \\
{ B ( \frac { 6 + 2 \sqrt { 5 } } { 3 } , \frac { 2 \sqrt { 1 5 } + 2 \sqrt { 3 } } { 3 } ) , }
\end{array} \quad \text { 及 } \left\{\begin{array}{l}
A\left(\frac{6-2 \sqrt{5}}{3},-\frac{2 \sqrt{15}-2 \sqrt{3}}{3}\right) \\
B\left(\frac{6+2 \sqrt{5}}{3},-\frac{2 \sqrt{15}+2 \sqrt{3}}{3}\right)
\end{array}\right.\right.
$$

## 第 647 题 抛物线的光学性质

点 $P$ 到点 $A\left(\frac{1}{2}, 0\right), B(a, 2)$ 及到直线 $x=-\frac{1}{2}$ 的距离都相等, 如果这样的点恰好只有一个, 那么 $a$的值是 $\qquad$ .

解析 $\pm \frac{1}{2}$.

解法一 注意到 $P$ 点在以 $A$ 为焦点, 直线 $x=-\frac{1}{2}$ 为准线的抛物线 $E: y^{2}=2 x$ 上. 因此可设 $P\left(2 t^{2}, 2 t\right)$,于是由 $P$ 到焦点 $A$ 与到点 $B$ 的距离相等, 得

$$
2 t^{2}+\frac{1}{2}=\sqrt{\left(2 t^{2}-a\right)^{2}+(2 t-2)^{2}}
$$

整理得

$$
(2-4 a) t^{2}-8 t+a^{2}+\frac{15}{4}=0
$$

该方程的解集有且只有一个元素, 因此

$$
2-4 a=0 \text { 或 }\left\{\begin{array}{l}
2-4 a \neq 0, \\
\Delta=0,
\end{array}\right.
$$

解得 $a=\frac{1}{2}$ 或 $a=-\frac{1}{2}$.

直译条件的思路简单可行, 但其中涉及解一个三次方程, 运算量不小. 此时应当尝试几何解法.

解法二 点 $P$ 到 $A$ 与点 $P$ 到 $B$ 的距离相等, 于是问题可以转化为线段 $A B$ 的垂直平分线 $l$ 与抛物线只有一个公共点, 这包含两种情形.

情形一 直线 $l$ 与抛物线的对称轴平行. 如图 1, 此时 $l: y=$ 1 , 于是 $a=\frac{1}{2}$.

情形二 直线 $l$ 与抛物线相切. 如图 2 , 过点 $P$ 作射线 $P M$ $/ / x$ 轴. 根据拖物线的几何性质, $\angle 1=\angle 3$, 因此 $\angle 1=\angle 2=$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-112.jpg?height=298&width=229&top_left_y=2123&top_left_x=1109)

图 1 $\angle 3$, 于是 $P B / / x$ 轴. 因此 $P$ 点坐标为 $(2,2)$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-112.jpg?height=303&width=374&top_left_y=2115&top_left_x=1397)

图 2
进而

$$
P B=P A=2+\frac{1}{2}
$$

解得 $a=-\frac{1}{2}$.

综合以上两种情形, $a= \pm \frac{1}{2}$.

## 第 648 题 $\quad$ 转换, 妙联立

如图, 已知直线 $y=k(x+2)(k>0)$ 与抛物线 $C: y^{2}=8 x$ 相交于 $A, B$ 两点, $F$ 为 $C$ 的焦点. 若 $F A=2 F B$, 则 $k=$ $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-113.jpg?height=425&width=315&top_left_y=757&top_left_x=1530)

解析 $\frac{2 \sqrt{2}}{3}$.

设 $M(-2,0), A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 则根据题意由 $F A=2 F B$ 得

$$
x_{1}+2=2\left(x_{2}+2\right)
$$

接下来,如何处理 $M, A, B$ 三点共线变成了解决问题的关键.

利用中点公式处理共线 不难推知点 $B$ 平分线段 $A M$, 于是 $y_{1}=2 y_{2}$, 可得

$$
x_{1}=4 x_{2} \text {. }
$$

综合两式, 可解得 $x_{2}=1$, 进而 $y_{2}=2 \sqrt{2}$,

因此不难求得 $k=\frac{2 \sqrt{2}}{3}$.

利用直线与抛物线联立 联立直线与抛物线得

$$
k^{2}(x+2)^{2}=8 x,
$$

整理为

$$
k^{2}(x+2)^{2}-8(x+2)+16=0
$$

由于 $\frac{x_{1}+2}{x_{2}+2}=2$, 因此

$$
8^{2}-\left(2+\frac{1}{2}+2\right) \cdot k^{2} \cdot 16=0
$$

解得 $k=\frac{2 \sqrt{2}}{3}$.

## 第 649 题 截距的范围

已知抛物线 $x^{2}=4 y$ 的焦点为 $F$, 点 $A, B, C$ 为该抛物线上不同的三点, 且满足 $\overrightarrow{F A}+\overrightarrow{F B}+\overrightarrow{F C}=\mathbf{0}$,若直线 $A B$ 存在截距 $m$, 求 $m$ 的取值范围.
解析 设 $A\left(2 a, a^{2}\right), B\left(2 b, b^{2}\right), C\left(2 c, c^{2}\right)$, 则由题意可得

$$
\left\{\begin{array}{l}
a+b+c=0 \\
a^{2}+b^{2}+c^{2}=3
\end{array}\right.
$$

进而

$$
\left\{\begin{array}{l}
a+b=-c \\
a^{2}+b^{2}=3-c^{2}
\end{array}\right.
$$

另一方面, 有

$$
m=\frac{2 a \cdot b^{2}-2 b \cdot a^{2}}{2 a-2 b}=-a b
$$

且 $a \neq b$. 这样就有

$$
2 a b=(a+b)^{2}-\left(a^{2}+b^{2}\right)=2 c^{2}-3 \geqslant-3
$$

且

$$
6 a b<(a+b)^{2}+\left(a^{2}+b^{2}\right)=3
$$

于是

$$
-\frac{1}{2}<-a b \leqslant \frac{3}{2}
$$

且当 $a \rightarrow b$ 时,$-a b \rightarrow-\frac{1}{2} ;$ 当 $(a, b, c)=\left(\frac{\sqrt{6}}{2},-\frac{\sqrt{6}}{2}, 0\right)$ 时,$-a b=\frac{3}{2}$.

因此所求的取值范围是 $\left(-\frac{1}{2}, \frac{3}{2}\right]$.

## 第 650 题 任他东南西北风

已知抛物线 $y^{2}=2 p x(p>0)$ 的焦点为 $F$, 过点 $F$ 的直线交 $y$ 轴正半轴于点 $P$, 交抛物线于 $A, B$ 两点, 其中点 $A$ 在第一象限.

(1)求证:以线段 $F A$ 为直径的圆与 $y$ 轴相切;

(2) 若 $\overrightarrow{F A}=\lambda_{1} \overrightarrow{A P}, \overrightarrow{B F}=\lambda_{2} \overrightarrow{F A}, \frac{\lambda_{1}}{\lambda_{2}} \in\left[\frac{1}{4}, \frac{1}{2}\right]$, 求 $\lambda_{2}$ 的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-114.jpg?height=289&width=267&top_left_y=1428&top_left_x=1483)

解析 (1) 只需要证明

$$
\frac{x_{A}+x_{F}}{2}=\frac{1}{2}|A F|
$$

即可. 实际上,由抛物线的定义易得.

(2) 设 $A\left(2 p t_{1}^{2}, 2 p t_{1}\right), B\left(2 p t_{2}^{2}, 2 p t_{2}\right), P(0, m)$ ，则由直线 $A B$ 与直线 $P A$ 的斜率相等得

$$
\frac{m-2 p t_{1}}{0-2 p t_{1}^{2}}=\frac{2 p t_{1}-2 p t_{2}}{2 p t_{1}^{2}-2 p t_{2}^{2}}
$$

解得

$$
m=\frac{2 p t_{1} t_{2}}{t_{1}+t_{2}}
$$

这样我们有

$$
\lambda_{2}=-\frac{t_{2}}{t_{1}}
$$

其中 $\lambda_{2}>1$. 进而

$$
\lambda_{1}=\frac{2 p t_{1}}{\frac{2 p t_{1} t_{2}}{t_{1}+t_{2}}-2 p t_{1}}=-1-\frac{t_{2}}{t_{1}}=-1+\lambda_{2}
$$

因此根据题意有

$$
\frac{-1+\lambda_{2}}{\lambda_{2}} \in\left[\frac{1}{4}, \frac{1}{2}\right],
$$

解得 $\lambda_{2}$ 的取值范围是 $\left[\frac{4}{3}, 2\right]$.

第 (2)小题引人了两个参数 $\lambda_{1}$ 和 $\lambda_{2}$, 使得题目蕴含更多的“变数”.看似“东南西北”纷繁复杂, 实则是对多参数问题的代数处理能力的一次考量. 事实上,以 $A, B$ 两点的坐标为基本参数,注意齐次特性用 $\lambda_{2}$ 表示 $\lambda_{1}$ 即可.

根据抛物线的几何平均性质, 有

$$
2 p t_{1}^{2} \cdot 2 p t_{2}^{2}=\left(\frac{p}{2}\right)^{2}
$$

从而

$$
t_{1} t_{2}=-\frac{1}{4}
$$

但是对于本题而言, 直线 $A B$ 过点 $F$ 的条件是多余的.

## 第 651 题 有效转化

曲线 $C$ 是平面内到定点 $A(1,0)$ 的距离与到定直线 $x=-1$ 的距离之和为 3 的动点 $P$ 的轨迹, 则曲线 $C$ 与 $y$ 轴交点的横坐标是 $\qquad$ ; 又已知 $B(a, 1)(a$ 为参数), 那么 $|P A|+|P B|$ 的最小值 $d(a)=$

解析 $(0, \pm \sqrt{3}) ; \begin{cases}\sqrt{a^{2}-2 a+2}, & a<-\frac{7}{5}, \\ a+4, & -\frac{7}{5} \leqslant a \leqslant-1, \\ 2-a, & -1<a \leqslant 1, \\ \sqrt{a^{2}-2 a+2}, & a>1 .\end{cases}$

作与直线 $x=-1$ 的距离为 3 的两条直线 $x=2, x=-4$, 那么 “到定点 $A(1,0)$ 与到定直线 $x=-1$ 的距离之和为 3 ”, 就转化成了 “在直线 $x=-1$ 的左侧到定点 $A(1,0)$ 的距离与到直线 $x=-4$ 的距离相等”, 或 “在直线 $x=-1$ 的右侧到定点 $A(1,0)$ 的距离与到直线 $x=2$ 的距离相等”, 如图 2. 曲线 $C$ 由抛物线弧 $y^{2}=$ $-2\left(x-\frac{3}{2}\right), y \in[-\sqrt{5}, \sqrt{5}]$ 和抛物线弧 $y^{2}=10\left(x+\frac{3}{2}\right), y \in[-\sqrt{5}, \sqrt{5}]$ 共同组成.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-115.jpg?height=359&width=381&top_left_y=2099&top_left_x=565)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-115.jpg?height=359&width=452&top_left_y=2093&top_left_x=1023)

图 2

容易求出曲线 $C$ 与 $y$ 轴的交点坐标为 $(0, \pm \sqrt{3})$.
接下来研究对于 $B(a, 1),|P B|+|P A|$ 的最小值 $d(a)$. 如图 2, 设直线 $y=1$ 与直线 $x=-4$, 抛物线弧 $y^{2}=10\left(x+\frac{3}{2}\right), y \in[-\sqrt{5}, \sqrt{5}]$, 直线 $x=-1$, 抛物线弧 $y^{2}=-2\left(x-\frac{3}{2}\right), y \in[-\sqrt{5}, \sqrt{5}]$, 直线 $x=2$ 依次交于点 $B_{1}(-4,1), B_{2}\left(-\frac{7}{5}, 1\right), B_{3}(-1,1), B_{4}(1,1), B_{5}(2,1)$. 以 $B_{1}, B_{2}, B_{3}, B_{4}, B_{5}$ 为分界点分类讨论,可得

$$
d(a)= \begin{cases}\sqrt{a^{2}-2 a+2}, & a<-\frac{7}{5} \\ a+4, & -\frac{7}{5} \leqslant a \leqslant-1 \\ 2-a, & -1<a \leqslant 1 \\ \sqrt{a^{2}-2 a+2}, & a>1\end{cases}
$$

本题是抛物线描述“到定点与到定直线距离之差为定值”的升级版本, 需要补充辅助线. 解决问题的关键是利用抛物线的定义将到定点的距离转化为到定直线的距离.

## 第 652 题 双动点问题

已知抛物线 $y^{2}=4 x$ 的焦点为 $F$, 点 $M(m, 0)$ 在 $x$ 轴的正半轴上, 且不与点 $F$ 重合, 动点 $A$ 在抛物线上, 且不过点 $O$. 若 $\angle F A M$ 恒为锐角, 则 $m$ 的取值范围为

解析 $(0,1) \cup(1,9)$.

解法一 设 $A\left(\frac{a^{2}}{4}, a\right)(a>0), \angle F A M$ 恒为锐角只需要

$$
\overrightarrow{A F} \cdot \overrightarrow{A M}>0
$$

对 $x$ 轴正半轴上的点 $M$ 恒成立, 即

$$
\left(1-\frac{a^{2}}{4},-a\right) \cdot\left(m-\frac{a^{2}}{4},-a\right)>0
$$

对 $m>0$ 恒成立. 化简有

$$
a^{4}+4(3-m) a^{2}+16 m>0
$$

对 $a>0$ 恒成立,即函数 $f(x)=x^{2}+4(3-m) x+16 m$ 没有正零点, 注意到 $f(0)=16 m>0$, 所以

$$
-2(3-m) \leqslant 0
$$

且

$$
\left\{\begin{array}{l}
-2(3-m)>0 \\
\Delta<0
\end{array}\right.
$$

解得 $m<9$, 又 $m>0$ 且 $m \neq 1$, 所以

$$
0<m<1 \text { 或 } 1<m<9 .
$$

对一般的抛物线 $y^{2}=2 p x(p>0)$, 也有对应的结论, 当 $m$ 的取值范围为

$$
\left(0, \frac{p}{2}\right) \cup\left(\frac{p}{2}, \frac{9 p}{2}\right)
$$

时, 对于点 $M(m, 0)$ 与抛物线上任意一点 $A, \angle F A M$ 恒为锐角.
解法二 固定抛物线上一点 $A\left(\frac{a^{2}}{4}, a\right)(a>0)$, 考虑对于不同的 $a$, 满足 $\angle F A M$ 为锐角时 $m$ 的取值集合, 再求交集. 于是考虑边界情况 $\angle F A M=90^{\circ}$ 时点 $M$ 的位置, 如图 1:

对 $a$ 进行讨论, 当 $a=2$ 时, $\angle F A M$ 恒为锐角;

当 $a \neq 2$ 时, 过点 $A$, 且垂直于 $F A$ 的直线方程为

$$
y-a=-\frac{\frac{a^{2}}{4}-1}{a}\left(x-\frac{a^{2}}{4}\right)
$$

令 $y=0$ 得直线 $M A$ 的横截距

$$
x_{a}=\frac{4 a^{2}}{a^{2}-4}+\frac{a^{2}}{4}=5+\frac{16}{a^{2}-4}+\frac{a^{2}-4}{4},
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-117.jpg?height=268&width=303&top_left_y=344&top_left_x=1574)

图 1

当 $a<2$ 时, $a^{2}-4 \in(-4,0)$, 此时 $x_{a}<0$, 结合图 1 知, 此时对任意的 $m>0$, 都有 $\angle F A M$ 为锐角;

当 $a>2$ 时, $x_{a} \geqslant 9$, 当且仅当 $a^{2}=12$ 时取等号. 结合图 1 知, 对任意的 $a>2, m$ 在集合 $\left(0, x_{a}\right)$ 内, 且 $m \neq$ 1 , 故满足条件的 $m$ 的集合为 $(0,1) \cup(1,9)$.

综上知 $m \in(0,1) \cup(1,9)$.

解法三 让 $M$ 点先固定, 点 $A$ 在抛物线上运动, 且对线段 $F M$ 的张角为锐角, 这只需要点 $A$ 在以线段 $M F$ 为直径的圆外. 故原题条件转化成抛物线与以 $F M$ 为直径的圆没有公共点.

以 $M F$ 为直径的圆的方程为

$$
(x-m)(x-1)+y^{2}=0
$$

联立圆和抛物线的方程消去 $y$ 得

$$
x^{2}+(3-m) x+m=0,
$$

此方程没有正实根,即函数 $f(x)=x^{2}+(3-m) x+m$ 没有正零点, 注意到 $f(0)=m>$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-117.jpg?height=309&width=243&top_left_y=932&top_left_x=1637)

图 2 0 , 所以

$$
-\frac{(3-m)}{2} \leqslant 0
$$

且

$$
\left\{\begin{array}{l}
-\frac{(3-m)}{2}>0 \\
\Delta<0
\end{array}\right.
$$

解得 $m<9$, 又 $m>0$ 且 $m \neq 1$, 所以

$$
0<m<1 \text { 或 } 1<m<9 \text {. }
$$

## 第 653 题 抛物线的几何性质

已知抛物线 $C_{1}: x^{2}=2 p y(p>0)$ 与圆 $C_{2}: x^{2}+y^{2}=8$ 的两个交点之间的距离为 4 .

(1) 求 $p$ 的值;

(2) 若 $C_{1}$ 在点 $A, B$ 处切线垂直相交于点 $P$, 且点 $P$ 在圆 $C_{2}$ 内部, 直线 $A B$ 与 $C_{2}$ 相交于 $C, D$ 两点, 求 $|A B| \cdot|C D|$ 的最小值.

解析 $(1) p=1$.

(2) 设 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 对 $y=\frac{1}{2} x^{2}$ 求导得 $y^{\prime}=x$,

所以由题意知 $x_{1} x_{2}=-1$, 联立 $C_{1}$ 在点 $A, B$ 处的切线方程

$$
\left\{\begin{array}{l}
y=x_{1} x-\frac{1}{2} x_{1}^{2} \\
y=x_{2} x-\frac{1}{2} x_{2}^{2}
\end{array}\right.
$$

得到交点 $P\left(\frac{x_{1}+x_{2}}{2},-\frac{1}{2}\right)$. 由点 $P$ 在圆内得

$$
\left(x_{1}+x_{2}\right)^{2}<31
$$

又因为直线

$$
A B: \frac{1}{2}\left(x_{1}+x_{2}\right) x-y+\frac{1}{2}=0
$$

过抛物线的焦点,所以

$$
|A B| \cdot|C D|=\frac{1}{2}\left(x_{1}^{2}+x_{2}^{2}+2\right) \cdot 2 \sqrt{8-d^{2}}=\sqrt{(m+2)(8 m+15)}
$$

其中 $m=x_{1}^{2}+x_{2}^{2}<33$, 又由 $m=x_{1}^{2}+\frac{1}{x_{1}^{2}} \geqslant 2$, 所以 $m \in[2,33)$.

从而得到

$$
2 \sqrt{31} \leqslant|A B| \cdot|C D|<\sqrt{9765}
$$

## 第 654 题 最小距离

已知抛物线 $x^{2}=2 p y(p>0)$ 的弦 $A B$ 的中点为 $M$, 弦长为 $l$, 求点 $M$ 到 $x$ 轴的距离 $h$ 的最小值.

解析 设 $A\left(2 p a, 2 p a^{2}\right), B\left(2 p b, 2 p b^{2}\right)$,则

$$
(2 p a-2 p b)^{2}+\left(2 p a^{2}-2 p b^{2}\right)^{2}=l^{2}
$$

即

$$
m^{2}\left(1+n^{2}\right)=\frac{l^{2}}{4 p^{2}}
$$

其中 $m=|a-b|, n=|a+b|$. 而

$$
\begin{aligned}
h & =\frac{p}{2}\left(2 a^{2}+2 b^{2}\right) \\
& =\frac{p}{2}\left(m^{2}+n^{2}\right) \\
& =\frac{p}{2}\left(\frac{\frac{l^{2}}{4 p^{2}}}{1+n^{2}}+1+n^{2}\right)-\frac{p}{2},
\end{aligned}
$$

其中 $n \geqslant 0, n^{2}+1 \geqslant 1$.

于是当 $l \geqslant 2 p$ 时, $h$ 的最小值为 $\frac{l}{2}-\frac{p}{2}$, 当 $n=\sqrt{\frac{l}{2 p}-1}$ 时取得; 当 $0<l<2 p$ 时, $h$ 的最小值为 $\frac{l^{2}}{8 p}$, 当 $n=$ 0 时取得.

## 思考与总结

设抛物线的焦点为 $F$, 则

$$
h+\frac{1}{2} p=\frac{1}{2}(|F A|+|F B|) \geqslant \frac{1}{2}|A B|=\frac{1}{2} l,
$$

等号当 $F \in A B$ 时取得. 因此当 $l \geqslant 2 p$ 时, 所求的最小值为 $\frac{1}{2} l-\frac{1}{2} p$.

## 第 655 题 坐标系下的三角形面积

已知 $F$ 为抛物线 $y^{2}=x$ 的焦点, 点 $A, B$ 在该抛物线上且位于 $x$ 轴的两侧, $\overrightarrow{O A} \cdot \overrightarrow{O B}=2$ (其中 $O$ 为坐标原点), 则 $\triangle A B O$ 与 $\triangle A F O$ 面积之和的最小值是
A. 2
B. 3
C. $\frac{17 \sqrt{2}}{8}$
D. $\sqrt{10}$

解析 B.

画出示意图, 如图.

设 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 则由 $\overrightarrow{O A} \cdot \overrightarrow{O B}=2$ 得

$$
x_{1} x_{2}+y_{1} y_{2}=2,
$$

即

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-119.jpg?height=262&width=284&top_left_y=690&top_left_x=1590)

$$
x_{1} x_{2}-\sqrt{x_{1} x_{2}}-2=0
$$

从而 $x_{1} x_{2}=4$, 因此直线 $A B$ 恒过点 $(2,0)$,

因此 $\triangle A B O$ 与 $\triangle A F O$ 的面积之和为

$$
\frac{1}{2} \cdot 2 \cdot\left|y_{1}-y_{2}\right|+\frac{1}{2} \cdot \frac{1}{4} \cdot\left|y_{1}\right|=\left|\frac{9}{8} y_{1}-y_{2}\right|=\frac{9}{8} \sqrt{x_{1}}+\sqrt{x_{2}} \geqslant 2 \sqrt{\frac{9}{8} \sqrt{x_{1} x_{2}}}=3
$$

等号当且仅当 $\frac{x_{1}}{x_{2}}=\frac{64}{81}$ 时取得.

因此所求面积之和的最小值为 3.

## 第 656 题 抛物线的几何平均性质

如图, 过抛物线 $y^{2}=4 x$ 的焦点 $F$ 作抛物线的两条弦 $A B, C D$, 设直线 $A C$ 与 $B D$ 的交点为 $P$, 直线 $A C, B D$ 分别与 $y$ 轴交于点 $M, N$.

(1)求证: $P$ 点恒在抛物线的准线上;

(2) 求证:四边形 $P M F N$ 为平行四边形.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-119.jpg?height=403&width=332&top_left_y=1607&top_left_x=1525)

解析 (1) 设 $A\left(4 a^{2}, 4 a\right), D\left(4 b^{2}, 4 b\right)$.

由抛物线的几何平均性质, 可得 $B\left(\frac{1}{4 a^{2}},-\frac{1}{a}\right), C\left(\frac{1}{4 b^{2}},-\frac{1}{b}\right)$, 则可得直线

$$
A C: y=\frac{4 b}{4 a b-1} x-\frac{4 a}{4 a b-1}
$$

于是直线

$$
B D: y=\frac{4 a}{4 a b-1} x-\frac{4 b}{4 a b-1}
$$

且

$$
M\left(0,-\frac{4 a}{4 a b-1}\right), N\left(0,-\frac{4 b}{4 a b-1}\right)
$$

联立直线 $A C$ 与直线 $B D$ 的方程可得 $P$ 点的横坐标为定值 -1 ;

(2)易得直线 $A C$ 的斜率与直线 $F N$ 的斜率相等, 且直线 $B D$ 的斜率与直线 $F M$ 的斜率相等, 因此四边形 $P M F N$ 为平行四边形.

## 第 657 题 避其锋芒

已知抛物线 $C: y^{2}=4 x$ 的焦点为 $F$, 直线 $M N$ 过焦点 $F$ 且与抛物线 $C$ 交于 $M, N$ 两点, $P$ 为抛物线 $C$ 的准线 $l$ 上一点, 且 $P F \perp M N$. 连结 $P M$ 交 $y$ 轴于点 $Q$, 过点 $Q$ 作 $Q D \perp M F$ 于点 $D$, 若 $|M D|=$ $2|F N|$, 求 $|M F|$.

解析 如图.

设 $M\left(4 m^{2}, 4 m\right), N\left(4 n^{2}, 4 n\right)$, 则根据抛物线的平均性质, 有

$$
4 m^{2} \cdot 4 n^{2}=1
$$

根据题意, 有

$$
\begin{aligned}
\frac{|M D|}{|F N|} & =\frac{|M Q|}{|M P|} \cdot \frac{|M F|}{|F N|} \\
& =\frac{4 m^{2}}{4 m^{2}+1} \cdot \frac{4 m^{2}+1}{4 n^{2}+1} \\
& =\frac{4 m^{2}}{4 n^{2}+1}=2
\end{aligned}
$$

于是可得

$$
2 m^{2}=4 n^{2}+1,
$$

将 $4 n^{2}=\frac{1}{4 m^{2}}$ 代人, 可得

$$
2 m^{2}=\frac{1}{4 m^{2}}+1
$$

即

$$
8 m^{4}-4 m^{2}-1=0,
$$

解得 $m^{2}=\frac{1+\sqrt{3}}{4}$, 因此

$$
|M F|=4 m^{2}+1=2+\sqrt{3}
$$

## 第 658 题 抛物线的平均性质

已知过定点 $A(-1,0)$ 的直线与抛物线 $C: y^{2}=4 x$ 交于 $M, N$ 两点, $Q$ 是抛物线上不同于 $M, N$ 的点,若直线 $Q M$ 恒过点 $(1,-1)$, 求证: 直线 $Q N$ 也恒过定点并求出该定点的坐标.

解析 设 $M\left(x_{1}, y_{1}\right), N\left(x_{2}, y_{2}\right), Q\left(x_{3}, y_{3}\right)$, 则根据抛物线的平均性质, 有

$$
y_{1} y_{2}=4
$$

而

$$
\begin{aligned}
& Q M: 4 x=\left(y_{1}+y_{3}\right) y-y_{1} y_{3}, \\
& Q N: 4 x=\left(y_{2}+y_{3}\right) y-y_{2} y_{3}
\end{aligned}
$$

由于直线 $Q M$ 恒过点 $(1,-1)$, 于是

$$
y_{1}+y_{3}+y_{1} y_{3}+4=0 \text {. }
$$

将 $y_{2}=\frac{4}{y_{1}}$ 代人 $Q N$ 的方程, 得

$$
4 x=\left(\frac{4}{y_{1}}+y_{3}\right) y-\frac{4}{y_{1}} y_{3},
$$

可整理得

$$
x y_{1}+y_{3}-\frac{y}{4} y_{1} y_{3}-y=0
$$

因此直线 $Q N$ 恒过定点 $(1,-4)$.

## 第 659 题 二次曲线上的四点共圆

如图,已知抛物线 $y^{2}=2 p x(p>0), A B$ 为过抛物线焦点 $F$ 的弦, $A B$ 的中垂线交抛物线 $E$ 于点 $M, N$. 若 $A, M, B, N$ 四点共圆, 求直线 $A B$ 的方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-121.jpg?height=341&width=343&top_left_y=711&top_left_x=1515)

解析 设圆的两条弦所在直线的交点为 $P\left(x_{0}, y_{0}\right)$, 过点 $P$ 的直线 $l:\left\{\begin{array}{l}x=x_{0}+t, \\ y=y_{0}+k t\end{array}\right.$,则与抛物线联立可得

$$
\left(y_{0}+k t\right)^{2}=2 p\left(x_{0}+t\right)
$$

整理得

$$
k^{2} t^{2}+\left(2 y_{0} k-2 p\right) t+y_{0}^{2}-2 p x_{0}=0
$$

于是

$$
t_{1} t_{2}=\frac{y_{0}^{2}-2 p x_{0}}{k^{2}}
$$

当 $k$ 取 $k_{A B}$ 时, 设方程的两根为 $t_{A}, t_{B}$;

当 $k$ 取 $k_{M N}$ 时, 设方程的两根为 $t_{M}, t_{N}$, 根据圆幂定理, 有

$$
\sqrt{1+k_{A B}^{2}} \cdot t_{A} \cdot \sqrt{1+k_{A B}^{2}} \cdot t_{B}=\sqrt{1+k_{M N}^{2}} \cdot t_{M} \cdot \sqrt{1+k_{M N}^{2}} \cdot t_{N}
$$

进而可得 $\frac{1+k_{A B}^{2}}{k_{A B}^{2}}=\frac{1+k_{M N}^{2}}{k_{M N}^{2}}$, 因此 $k_{A B}=-k_{M N}$.

结合本题已知 $A B \perp M N$, 于是 $k_{A B}= \pm 1$, 进而直线 $A B$ 的方程为 $y= \pm x \mp \frac{p}{2}$.

思考与总结

事实上, 本题中 $k_{A B}=-k_{M N}$ 的结论可以推广到任意二次曲线.

## 第 660 题 切线三角形

已知抛物线 $C: y^{2}=4 x$ 和直线 $l: x-y+4=0, P$ 是直线 $l$ 上一点, 过 $P$ 作抛物线的两条切线, 切点分别为 $A, B$. 若 $P A, P B$ 分别交 $y$ 轴于点 $M, N$, 求 $\triangle P M N$ 外接圆半径的最小值.

解析 注意到 $\triangle P M N$ 的三边均为抛物线的切线, 而抛物线的切线三角形有一个优美性质: 抛物线的切线三角形的外接圆过焦点. 因此可以从这点人手, 结合图形的特殊性解题.
如图, 设 $A\left(4 a^{2}, 4 a\right)$, 则

$$
P A: 4 a y=2\left(x+4 a^{2}\right), \quad
$$

因此 $M$ 点的坐标为 $(0,2 a)$, 从而直线 $P A$ 与 $F M$ 的斜率之积为

$$
\frac{2}{4 a} \cdot \frac{2 a-0}{0-1}=-1
$$

因此 $P A \perp F M$. 类似的, 有 $P B \perp F N$. 因此 $P, M, F, N$ 四点共圆, 且圆的直径为 $P F$.

易知, 当 $P F \perp l$ 时, 所求外接圆的半径最小, 为

$$
\frac{1}{2} P F=\frac{5}{2 \sqrt{2}}=\frac{5 \sqrt{2}}{4}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-122.jpg?height=472&width=513&top_left_y=195&top_left_x=1258)

## 第 661 题 曲线内接三角形

已知函数 $f(x)=\mathrm{e}^{x}+x$, 对于曲线 $y=f(x)$ 上横坐标成等差数列的三个点 $A, B, C$, 给出以下判断:

(1) $\triangle A B C$ 一定是钝角三角形;

(2) $\triangle A B C$ 可能是直角三角形;

(3) $\triangle A B C$ 可能是等腰三角形;

(4) $\triangle A B C$ 不可能是等腰三角形.

其中, 正确的判断是
A. (1) (3)
B. (1)(4)
C. (2) (3)
D. (2)(4)

## 解析 B.

如图. 设直线 $A B, B C$ 的斜率分别为 $k_{A B}, k_{B C}$.

由于函数 $f(x)$ 单调递增, 于是 $k_{A B}>0, k_{B C}>0$, 因此直线 $A B$ 和直线 $B C$ 的倾斜角之差为锐角, 进而 $\angle A B C$ 为针角, 命题(1)正确, 命题(2)错误.

由于 $\triangle A B C$ 为钝角三角形, 因此如果它是等腰三角形, 那么一定有 $A B=B C$, 从而

$$
\sqrt{1+k_{A B}^{2}} \cdot\left|x_{A}-x_{B}\right|=\sqrt{1+k_{B C}^{2}} \cdot\left|x_{B}-x_{C}\right|
$$

结合 $k_{A B}, k_{B C}>0$, 有 $k_{A B}=k_{B C}$, 进而 $A, B, C$ 三点共线, 矛盾. 因此 $\triangle A B C$ 不可能为等腰三角形. 因此命题(3)错误, 命题(4)正确.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-122.jpg?height=445&width=296&top_left_y=1347&top_left_x=1476)

故选 B.

## 第 662 题 特殊三角形的极坐标表达

求抛物线 $y^{2}=2 p x(p>0)$ 的内接等腰直角三角形面积的最小值.

解析 解法一 如图 1, 设 $A\left(2 p a^{2}, 2 p a\right), B\left(2 p b^{2}, 2 p b\right), C\left(2 p c^{2}, 2 p c\right)$, 且 $A$ 为直角顶点.

注意到 $\triangle A B B^{\prime}$ 与 $\triangle A C C^{\prime}$ 全等, 因此 $A B^{\prime}=A C^{\prime}$, 等腰直角 $\triangle A B C$ 的面积

$$
S_{\triangle A B C}=\frac{1}{2} A B^{2}=2 p^{2}\left[(a-b)^{2}+(c-a)^{2}\right]=2 p^{2}\left[2 a^{2}-2 a(b+c)+b^{2}+c^{2}\right]
$$

又 $A C \perp A B$, 于是

$$
\left(2 p a^{2}-2 p b^{2}\right)\left(2 p a^{2}-2 p c^{2}\right)+(2 p a-2 p b)(2 p a-2 p c)=0,
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-122.jpg?height=262&width=204&top_left_y=2162&top_left_x=1563)

图 1

整理得

$$
(a+b)(a+c)+1=0,
$$

即

$$
a^{2}+b c+1=-a(b+c)
$$

代人面积的计算公式可得

$$
S_{\triangle A B C}=2 p^{2}\left[4 a^{2}+(b+c)^{2}+2\right] .
$$

于是抛物线的内接等腰直角三角形面积的最小值为 $4 p^{2}$, 当 $A(0,0), B(2 p, 2 p), C(2 p,-2 p)$ 时取得.

思考与总结

直角坐标下容易计算两点的距离和点到直线的距离, 关键是绕开两边相等表达等腰三角形的条件.

解法二 设抛物线的内接等腰直角三角形为 $\triangle A B C$, 直角顶点为 $A\left(2 p t^{2}, 2 p t\right)$, 平移坐标系, 使得原点为 $A$, 如图 2.

抛物线方程变为

$$
(y+2 p t)^{2}=2 p\left(x+2 p t^{2}\right),
$$

即 $y^{2}+4 p t y-2 p x=0$.

此时, 可设 $B(r \cos \theta, r \sin \theta), C(-r \sin \theta, r \cos \theta)$, 则

$$
r^{2} \sin ^{2} \theta+4 p t \cdot r \sin \theta-2 p \cdot r \cos \theta=0, r^{2} \cos ^{2} \theta+4 p t \cdot r \cos \theta+2 p \cdot r \sin \theta=0
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-123.jpg?height=287&width=287&top_left_y=714&top_left_x=1572)

图 2

于是

$$
4 t=\frac{2 p \cos \theta-r \sin ^{2} \theta}{p \sin \theta}=\frac{2 p \sin \theta+r \cos ^{2} \theta}{-p \cos \theta},
$$

从而解得

$$
r=\frac{2 p}{\sin \theta \cdot \cos \theta(\sin \theta-\cos \theta)}
$$

其中令 $s=\sin \theta \cdot \cos \theta$, 则由于 $\theta \in\left(-\frac{\pi}{2}, 0\right)$, 于是 $s \in\left[-\frac{1}{2}, 0\right)$.

此时

$$
S_{\triangle A B C}=\frac{1}{2} r^{2}=\frac{2 p^{2}}{s^{2}(1-2 s)}
$$

于是当 $s=-\frac{1}{2}$, 即 $\theta=-\frac{\pi}{4}$ 时, $\triangle A B C$ 的面积取得最小值为 $4 p^{2}$.

极坐标下容易表达“等腰”、“直角”等条件,难点在于坐标计算.

## 第 663 题 梅开三度

如图 1, 已知点 $F$ 是椭圆 $\frac{x^{2}}{25}+\frac{y^{2}}{9}=1$ 的左焦点, 直线 $A B$ 经过点 $F$ 且与椭圆交于 $A, B$ 两点. 若 $O$ 为坐标原点, $\triangle A O B$ 的面积是 $\frac{9}{2}$, 求直线 $A B$的斜率 $k$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-123.jpg?height=284&width=445&top_left_y=2049&top_left_x=1378)

图 1

解析 解法一 设 $A B: x=m y-4$, 则

$$
\frac{1}{25}(m y-4)^{2}+\frac{1}{9} y^{2}=1
$$

从而

$$
\left(\frac{m^{2}}{25}+\frac{1}{9}\right) y^{2}-\frac{8 m}{25} y-\frac{9}{25}=0
$$

从而

$$
S_{\triangle A O B}=\frac{1}{2} \cdot 4 \cdot \frac{1}{\frac{m^{2}}{25}+\frac{1}{9}} \cdot \sqrt{\left(\frac{8 m}{25}\right)^{2}-4\left(\frac{m^{2}}{25}+\frac{1}{9}\right) \cdot\left(-\frac{9}{25}\right)}=\frac{9}{2}
$$

整理得

$$
81 m^{4}-1150 m^{2}-975=0
$$

于是

$$
\left(m^{2}-15\right)\left(81 m^{2}+65\right)=0,
$$

因此直线 $A B$ 的斜率 $k= \pm \frac{\sqrt{15}}{15}$.

## 解法二 如图 2, 利用仿射交换

$$
x^{\prime}=x, y^{\prime}=\frac{5}{3} y
$$

将椭圆变成圆 $x^{\prime 2}+y^{\prime 2}=25$, 则

$$
S_{\triangle A^{\prime} O B^{\prime}}=\frac{9}{2} \cdot \frac{5}{3}=\frac{15}{2}
$$

设点 $O$ 到直线 $A^{\prime} B^{\prime}$ 的距离为 $O H$, 则

$$
\frac{1}{2} \cdot 2 \sqrt{25-O H^{2}} \cdot O H=\frac{15}{2}
$$

即

$$
O H^{2}\left(25-O H^{2}\right)=\frac{225}{4}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-124.jpg?height=450&width=423&top_left_y=834&top_left_x=1350)

图 2

于是 $O H^{2}=\frac{5}{2}$, 从而

$$
\sin \angle B^{\prime} F^{\prime} O=\sqrt{\frac{5}{32}}
$$

从而

$$
\tan \angle B^{\prime} F^{\prime} O= \pm \sqrt{\frac{5}{27}}
$$

因此所求直线的斜率 $k= \pm \frac{\sqrt{15}}{15}$.

解法三 设 $\angle B F O=\theta$, 则

$$
S_{\triangle A O B}=\frac{1}{2} \cdot 4 \cdot\left(\frac{9}{5-4 \cos \theta}+\frac{9}{5+4 \cos \theta}\right) \cdot \sin \theta=\frac{9}{2},
$$

整理得

$$
40 \sin \theta=25-16 \cos ^{2} \theta
$$

即

$$
(4 \sin \theta-1)(4 \sin \theta-9)=0,
$$

因此 $\sin \theta=\frac{1}{4}$, 从而直线 $A B$ 的斜率 $k= \pm \frac{\sqrt{15}}{15}$.

## 第 664 题 化椭为圆

如图 1, 过点 $T(2,3)$ 作直线 $l$ 交椭圆 $\frac{x^{2}}{4}+y^{2}=1$ 于两个不同的点 $P, Q$, 过点 $P, Q$ 作椭圆的切线, 两条切线交于点 $M, O$ 为原点, 已知四边形 $P O Q M$ 的面积为 4 , 求直线 $l$ 的方程.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-125.jpg?height=279&width=383&top_left_y=448&top_left_x=1441)

图 1

解析 如图 2, 考虑仿射变换 $x=x^{\prime}, y=\frac{1}{2} y^{\prime}$, 则椭圆变为 $x^{\prime 2}+y^{\prime 2}=4$, 点 $T(2$, 3) 变为 $T^{\prime}(2,6)$.

设 $P, Q, M$ 的对应点分别为 $P^{\prime}, Q^{\prime}, M^{\prime}$, 则四边形 $P^{\prime} O Q^{\prime} M^{\prime}$ 的面积为 8 .

设点 $O$ 到直线 $P^{\prime} Q^{\prime}$ 的距离为 $d$,

由射影定理 $d \cdot\left|O M^{\prime}\right|=\left|O P^{\prime}\right|^{2}$, 于是 $\left|O M^{\prime}\right|=\frac{4}{d}$,

从而四边形 $P^{\prime} O Q^{\prime} M^{\prime}$ 的面积

$$
S=\frac{1}{2} \cdot\left|P^{\prime} Q^{\prime}\right| \cdot\left|O M^{\prime}\right|=\sqrt{4-d^{2}} \cdot \frac{4}{d}=8
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-125.jpg?height=415&width=336&top_left_y=785&top_left_x=1527)

图 2

解得 $d^{2}=\frac{4}{5}$.

设直线 $P^{\prime} Q^{\prime}: y^{\prime}=k^{\prime}(x-2)+6$, 则有

$$
\frac{\left(2 k^{\prime}-6\right)^{2}}{1+k^{\prime 2}}=\frac{4}{5}
$$

解得 $k^{\prime}=2$ 或 $k^{\prime}=\frac{11}{2} ，$

于是直线 $l$ 的方程为 $y=x+1$ 或 $y=\frac{11}{4} x-\frac{5}{2}$.

## 第 665 题 两根之比

已知椭圆 $\frac{x^{2}}{4}+y^{2}=1, D$ 为其左顶点. 若存在直线 $l$ 过点 $M(t, 0)$ (其中 $-2<t<2$ ) 交椭圆于 $A, B$ 两点, 使 $S_{\triangle A O B}=\lambda S_{\triangle A O D}$, 则称 $M$ 为“ $\lambda$ 分点”.

(1)求证: $M(1,0)$ 是“ 1 分点”;

(2)求证: $M(1,0)$ 不是“ 2 分点”.

解析 $(1)$ 当点 $M(1,0)$ 时, 由于

$$
\frac{S_{\triangle A O D}}{S_{\triangle M O M}}=\frac{O D}{O M}=2
$$

于是

$$
S_{\triangle M O B}=\lambda S_{\triangle A O D}
$$

等价于

$$
\frac{B M}{A M}=2 \lambda-1
$$

因此只需要求出 $\frac{B M}{A M}$ 的取值范围就可以解决问题.

设直线 $A B: x=m y+1$, 与椭圆方程联立可得

$$
\left(m^{2}+4\right) y^{2}+2 m y-3=0
$$

记 $\frac{B M}{A M}=\mu, B\left(x_{1}, y_{1}\right), A\left(x_{2}, y_{2}\right)$, 其中 $\mu>0$, 则 $\frac{y_{1}}{y_{2}}=-\mu$, 于是

$$
-\mu+\frac{1}{-\mu}+2=\frac{4 m^{2}}{-3\left(m^{2}+4\right)}
$$

从而可得 $\mu+\frac{1}{\mu}$ 的取值范围是 $\left[2, \frac{10}{3}\right)$, 也即 $\mu$ 的取值范围是 $\left(\frac{1}{3}, 3\right)$, 对应的 $\lambda$ 的取值范围为 $\left(\frac{2}{3}, 2\right)$, 因此 $M(1,0)$ 是“ 1 分点”.

(2)根据第 (1) 小题的结果, $\lambda$ 的取值范围为 $\left(\frac{2}{3}, 2\right)$, 因此 $M(1,0)$ 不是“ 2 分点”.

## 第 666 题避重就轻

如图, 已知椭圆 $C: \frac{x^{2}}{9}+\frac{y^{2}}{8}=1$ 及圆 $M: x^{2}+2 x+y^{2}+m=0$. 过椭圆的左顶点 $A$ 且与圆 $M$ 相切于点 $B$ 的直线交椭圆 $C$ 于点 $P, P$ 与椭圆 $C$ 的右焦点 $F$ 的连线交椭圆于点 $Q$. 若 $B, M, Q$ 三点共线, 求实数 $m$ 的值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-126.jpg?height=450&width=442&top_left_y=1067&top_left_x=1327)

解析 设 $P A: y=k(x+3), Q B: y=-\frac{1}{k}(x+1), P\left(x_{1}, y_{1}\right)$.

联立直线 $P A$ 与椭圆方程, 可得

$$
\left(9 k^{2}+8\right) x^{2}+54 k^{2} x+8 k^{2}-72=0
$$

于是

$$
x_{1}=\frac{24-27 k^{2}}{9 k^{2}+8}, y_{1}=\frac{48 k}{9 k^{2}+8}
$$

即 $P$ 点坐标为

$$
P\left(\frac{24-27 k^{2}}{9 k^{2}+8}, \frac{48 k}{9 k^{2}+8}\right)
$$

而点 $F(1,0)$, 联立 $Q B$ 与 $P F$ 的方程

$$
\left\{\begin{array}{l}
y=-\frac{1}{k}(x+1) \\
y-0=\frac{48 k}{16-36 k^{2}}(x-1)
\end{array}\right.
$$

解得点 $Q$ 的坐标为

$$
Q\left(\frac{21 k^{2}-4}{3 k^{2}+4},-\frac{24 k}{3 k^{2}+4}\right)
$$

由 $Q$ 点在椭圆 $C$ 上可得

$$
8\left(\frac{21 k^{2}-4}{3 k^{2}+4}\right)^{2}+9\left(\frac{24 k}{3 k^{2}+4}\right)^{2}=72
$$

整理得

$$
\left(3 k^{2}-1\right)\left(15 k^{2}+16\right)=0
$$

于是 $k^{2}=\frac{1}{3}$, 进而可得圆 $M$ 的半径为 1 , 于是实数 $m$ 的值为 0 .

## 第 667 题 总有一款适合你

在椭圆 $\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$ 中, 直线 $l$ 与椭圆交于 $A, B$ 两点, 直线 $A B$ 不过点 $P(2,0)$, 且以 $A B$ 为直径的圆恒过点 $P(2,0)$, 求证: 直线 $A B$ 恒过定点, 并求该定点的坐标.

解析 $\left(\frac{2}{7}, 0\right)$.

解法一 设直线方程为 $x=m y+n, A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$. 联立直线 $A B$ 与椭圆方程可得

$$
\left(3 m^{2}+4\right) y^{2}+6 m n y+3 n^{2}-12=0,
$$

于是由 $\overrightarrow{P A} \cdot \overrightarrow{P B}=0$ 可得

$$
\left(m y_{1}+n-2\right)\left(m y_{2}+n-2\right)+y_{1} y_{2}=0
$$

即

$$
\left(3 m^{2}+4\right)(n-2)^{2}-6 m^{2} n(n-2)+\left(3 n^{2}-12\right) m^{2}+3 n^{2}-12=0,
$$

化简得 $7 n^{2}-16 n+4=0$, 解得 $n=\frac{2}{7}$ 或 $n=2$ (舍去).

于是直线 $A B$ 恒过定点 $\left(\frac{2}{7}, 0\right)$.

解法二 椭圆方程为 $3 x^{2}+4 y^{2}-12=0$, 设直线 $A P, B P$ 的方程分别为

$$
x+m y-2=0, m x-y-2 m=0,
$$

于是相交直线 $A P, B P$ 的方程为

$$
(x+m y-2)(m x-y-2 m)=0
$$

根据题意, 它们的交点曲线系为

$$
3 x^{2}+4 y^{2}-12+\lambda(x+m y-2)(m x-y-2 m)=0,
$$

即

$$
3 x^{2}+4 y^{2}-12+\lambda\left[-m y^{2}+m(x-2)^{2}+\left(m^{2}-1\right)(x-2) y\right]=0,
$$

我们想把 $P(2,0)$ 从方程中分离出来, 取 $\lambda=\frac{4}{m}$, 则有

$$
(x-2)\left[3(x+2)+4(x-2)+\frac{4\left(m^{2}-1\right)}{m} y\right]=0,
$$

于是可得直线 $A B$ 的方程为

$$
7 x+\frac{4\left(m^{2}-1\right)}{m} y-2=0
$$

于是直线 $A B$ 恒过定点 $\left(\frac{2}{7}, 0\right)$.

解法三 利用仿射变换, 使得 $P$ 点为新坐标系的原点, 则此时椭圆方程为

$$
\frac{\left(x^{\prime}+2\right)^{2}}{4}+\frac{y^{\prime 2}}{3}=1
$$

设直线方程为 $m x^{\prime}+n y^{\prime}=1$, 化齐次联立可得

## 整理得

$$
\frac{x^{\prime 2}}{4}+\frac{y^{\prime 2}}{3}+x^{\prime} \cdot\left(m x^{\prime}+n y^{\prime}\right)=0
$$

$$
\frac{1}{3}\left(\frac{y^{\prime}}{x}\right)^{2}+n \cdot \frac{y^{\prime}}{x^{\prime}}+m+\frac{1}{4}=0
$$

因为 $P A \perp P B$, 故关于 $y_{x^{\prime}}$ 的方程的两根之积为 -1 , 从而有

$$
\frac{1}{4}+\frac{1}{3}+m=0
$$

即

$$
\left(-\frac{12}{7}\right) m+0 \cdot n=1
$$

于是直线恒过点 $Q^{\prime}\left(-\frac{12}{7}, 0\right)$, 对应原坐标系的定点为 $Q\left(\frac{2}{7}, 0\right)$.

## 第 668 题 百花齐放

已知 $A, B$ 是椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 上的两点, $O$ 为坐标原点, 且 $O A \perp O B$, 求证: 点 $O$ 到直线 $A B$ 的距离为定值.

解析 解法一 直线消参.

当直线 $A B$ 的斜率存在时, 设其方程为 $y=k x+m, A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$. 根据题意, 有

$$
x_{1} x_{2}+y_{1} y_{2}=0,
$$

即

$$
\left(k^{2}+1\right) x_{1} x_{2}+k m\left(x_{1}+x_{2}\right)+m^{2}=0
$$

联立直线与椭圆方程, 可得

$$
\left(\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}\right) x^{2}+\frac{2 k m}{b^{2}} x+\frac{m^{2}}{b^{2}}-1=0
$$

这样就有

$$
\left(k^{2}+1\right)\left(\frac{m^{2}}{b^{2}}-1\right)+k m\left(-\frac{2 k m}{b^{2}}\right)+m^{2}\left(\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}\right)=0
$$

也即

$$
1+k^{2}=\left(\frac{1}{a^{2}}+\frac{1}{b^{2}}\right) m^{2}
$$

因此点 $O$ 到直线 $A B$ 的距离

$$
d=\frac{|m|}{\sqrt{1+k^{2}}}=\frac{a b}{\sqrt{a^{2}+b^{2}}}
$$

为定值.

经验证, 当直线 $A B$ 的斜率不存在时, 也有 $d=\frac{a b}{\sqrt{a^{2}+b^{2}}}$, 因此原命题得证.

解法二 化齐次联立.

设直线 $A B$ 的方程为 $m x+n y=1$, 与椭圆方程化齐次联立, 可得

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}-(m x+n y)^{2}=0
$$

从而由 $O A \perp O B$ 可得

$$
\frac{1}{a^{2}}+\frac{1}{b^{2}}-m^{2}-n^{2}=0
$$

因此点 $O$ 到直线 $A B$ 的距离

$$
d=\frac{1}{\sqrt{m^{2}+n^{2}}}=\frac{a b}{\sqrt{a^{2}+b^{2}}}
$$

为定值.
解法三 当直线 $O A$ 和直线 $O B$ 的斜率均存在时, 设 $O A: y=k x, O B: y=-\frac{1}{k} x$.联立直线 $O A$ 与椭圆的方程, 可得

$$
\left(\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}\right) x^{2}=1
$$

于是点 $O$ 到直线 $A B$ 的距离 $d$ 满足

$$
\begin{aligned}
\frac{1}{d^{2}} & =\frac{1}{|O A|^{2}}+\frac{1}{|O B|^{2}} \\
& =\frac{\frac{1}{a^{2}}+\frac{k^{2}}{b^{2}}}{1+k^{2}}+\frac{\frac{1}{a^{2}}+\frac{1}{b^{2} k^{2}}}{1+\frac{1}{k^{2}}} \\
& =\frac{1}{a^{2}}+\frac{1}{b^{2}}
\end{aligned}
$$

因此 $d$ 为定值 $\frac{a b}{\sqrt{a^{2}+b^{2}}}$.

经验证, 当直线 $O A$ 或 $O B$ 的斜率不存在时, 也有 $d=\frac{a b}{\sqrt{a^{2}+b^{2}}}$, 因此原命题得证.

解法四 设 $A(a \cos \alpha, b \sin \alpha), B(a \cos \beta, b \sin \beta)$, 则由 $O A \perp O B$ 有

$$
a^{2} \cos \alpha \cos \beta+b^{2} \sin \alpha \sin \beta=0,
$$

当 $\cos \alpha \cos \beta \neq 0$ 时, 有

$$
\tan ^{2} \alpha \cdot \tan ^{2} \beta=\frac{a^{4}}{b^{4}}
$$

此时点 $O$ 到直线 $A B$ 的距离 $d$ 满足

$$
\begin{aligned}
d^{2} & =\frac{1}{|O A|^{2}}+\frac{1}{|O B|^{2}} \\
& =\frac{1}{a^{2} \cos ^{2} \alpha+b^{2} \sin ^{2} \alpha}+\frac{1}{a^{2} \cos ^{2} \beta+b^{2} \sin ^{2} \beta} \\
& =\frac{\sin ^{2} \alpha+\cos ^{2} \alpha}{a^{2} \cos ^{2} \alpha+b^{2} \sin ^{2} \alpha}+\frac{\sin ^{2} \beta+\cos ^{2} \beta}{a^{2} \cos ^{2} \beta+b^{2} \sin ^{2} \beta} \\
& =\frac{\tan ^{2} \alpha+1}{a^{2}+b^{2} \tan ^{2} \alpha}+\frac{\tan ^{2} \beta+1}{a^{2}+b^{2} \tan ^{2} \beta} \\
& =\frac{\tan ^{2} \alpha+1}{a^{2}+b^{2} \tan ^{2} \alpha}+\frac{\left(\tan ^{2} \beta+1\right) \cdot \tan ^{2} \alpha}{\left(a^{2}+b^{2} \tan ^{2} \beta\right) \cdot \tan ^{2} \alpha} \\
& =\frac{\tan ^{2} \alpha+1}{a^{2}+b^{2} \tan ^{2} \alpha}+\frac{\frac{a^{4}}{b^{4}}+\tan ^{2} \alpha}{a^{2} \tan ^{2} \alpha+b^{2} \cdot \frac{a^{4}}{b^{4}}} \\
& =\frac{\tan ^{2} \alpha+1}{a^{2}+b^{2} \tan ^{2} \alpha}+\frac{a^{2}}{b^{2} \tan ^{2} \alpha+b^{2} \tan ^{2} \alpha} \\
& =\frac{1}{a^{2}}+\frac{1}{b^{2}},
\end{aligned}
$$

因此 $d$ 为定值 $\frac{a b}{\sqrt{a^{2}+b^{2}}}$.

经验证, 当 $\cos \alpha \cos \beta=0$ 时, $d=\frac{a b}{\sqrt{a^{2}+b^{2}}}$, 因此原命题得证.

解法五 设 $A\left(\theta, r_{1}\right), B\left(\theta+\frac{\pi}{2}, r_{2}\right)$, 则有

$$
\frac{r_{1}^{2} \cos ^{2} \theta}{a^{2}}+\frac{r_{1}^{2} \sin ^{2} \theta}{b^{2}}=1
$$

$$
\frac{r_{2}^{2} \cos ^{2}\left(\theta+\frac{\pi}{2}\right)}{a^{2}}+\frac{r_{2}^{2} \sin ^{2}\left(\theta+\frac{\pi}{2}\right)}{b^{2}}=1
$$

于是点 $O$ 到直线 $A B$ 的距离 $d$ 满足

$$
\frac{1}{d^{2}}=\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}=\frac{1}{a^{2}}+\frac{1}{b^{2}}
$$

为定值, 因此原命题得证.

## 第 669 题 曲线系与仿射变换

已知椭圆 $\frac{x^{2}}{a^{2}}+y^{2}=1$ 的离心率为 $\frac{\sqrt{3}}{2}, P(m, n)$ 为圆 $x^{2}+y^{2}=16$ 上任意一点, 过点 $P$ 作椭圆的两条切线 $P A, P B$. 设切点分别为 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$.

(1) 证明: 切线 $P A$ 的方程为 $\frac{x_{1} x}{4}+y_{1} y=1$;

(2) 设 $O$ 为坐标原点,求 $\triangle A B O$ 面积的最大值.

解析 (1) 椭圆的方程为 $\frac{x^{2}}{4}+y^{2}=1$. 设点 $A$ 的方程为

$$
\frac{\left(x-x_{1}\right)^{2}}{4}+\left(y-y_{1}\right)^{2}=0
$$

利用交点曲线系可得切线 $P A$ 的方程为

$$
\left(\frac{x^{2}}{4}+y^{2}-1\right)-\left[\frac{\left(x-x_{1}\right)^{2}}{4}+\left(y-y_{1}\right)^{2}\right]=0
$$

整理得

$$
\frac{2 x_{1} x}{4}+2 y_{1} y=\frac{x_{1}^{2}}{4}+y_{1}^{2}+1
$$

由于 $\frac{x_{1}^{2}}{4}+y_{1}^{2}=1$, 可得

$$
P A: \frac{x_{1} x}{4}+y_{1} y=1
$$

(2) 作仿射变换 $x^{\prime}=x, y^{\prime}=2 y$, 则问题等价于从椭圆 $x^{\prime 2}+\frac{y^{\prime 2}}{4}=16$ 上点 $P^{\prime}(m, 2 n)$ 引圆 $x^{\prime 2}+y^{\prime 2}=4$ 的两条切线, 切点分别为 $A^{\prime}, B^{\prime}$, 求 $\triangle A^{\prime} B^{\prime} O$ 面积的最大值的一半.

$\triangle A^{\prime} B^{\prime} O$ 的面积 $S$ 只与 $P^{\prime} O$ 有关, 设 $P^{\prime} O=x(x \in[4,8])$, 则

$$
S(x)=\frac{4}{x} \cdot \sqrt{2^{2}-\left(\frac{4}{x}\right)^{2}}=\sqrt{\left(\frac{4}{x}\right)^{2} \cdot\left[4-\left(\frac{4}{x}\right)^{2}\right]}
$$

由于 $\left(\frac{4}{x}\right)^{2}$ 的取值范围是 $\left[\frac{1}{4}, 1\right]$, 于是 $S(x)$ 的取值范围是 $\left[\frac{\sqrt{15}}{4}, \sqrt{3}\right]$, 其最大值为 $\sqrt{3}$. 回到原问题, 所求 $\triangle A B O$ 面积的最大值为 $\frac{\sqrt{3}}{2}$.

由曲线系得到的方程是过点 $P$ 的直线, 且椭圆上不存在另外一个点也在此直线上, 所以它是切线 $P A$的方程.

## 第 670 题 内接与外切

已知抛物线 $y^{2}=2 p x$ 的内接 $\triangle A B C$ 的三条边所在的直线均与抛物线 $x^{2}=2 p y$ 相切, 求证: $A, B, C$三点的纵坐标之和为 0.

解析 解法一 设三边所在的直线分别为 $l_{1}, l_{2}, l_{3}$, 切点分别为 $\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right),\left(x_{3}, y_{3}\right)$ 且 $l_{1}$ 与 $l_{2}$ 的交点为 $C, l_{2}$ 与 $l_{3}$ 的交点为 $A, l_{3}$ 与 $l_{1}$ 的交点为 $B$, 则

$$
\left\{\begin{array}{l}
l_{1}: 2 p y=2 x_{1} x-x_{1}^{2} \\
l_{2}: 2 p y=2 x_{2} x-x_{2}^{2} \\
l_{3}: 2 p y=2 x_{3} x-x_{3}^{2}
\end{array}\right.
$$

于是有

$$
A\left(\frac{x_{2}+x_{3}}{2}, \frac{x_{2} x_{3}}{2 p}\right), B\left(\frac{x_{3}+x_{1}}{2}, \frac{x_{3} x_{1}}{2 p}\right), C\left(\frac{x_{1}+x_{2}}{2}, \frac{x_{1} x_{2}}{2 p}\right)
$$

进而由 $A, B, C$ 三点均在抛物线上可得

$$
\left\{\begin{array}{l}
x_{1}^{2} x_{2}^{2}=4 p^{3}\left(x_{1}+x_{2}\right) \\
x_{2}^{2} x_{3}^{2}=4 p^{3}\left(x_{2}+x_{3}\right) \\
x_{3}^{2} x_{1}^{2}=4 p^{3}\left(x_{3}+x_{1}\right)
\end{array}\right.
$$

于是可得

$$
x_{1} x_{2}+x_{2} x_{3}+x_{3} x_{1}=8 p^{3}\left(\frac{1}{x_{1}}+\frac{1}{x_{2}}+\frac{1}{x_{3}}\right)
$$

即

$$
\left(x_{1} x_{2}+x_{2} x_{3}+x_{3} x_{1}\right)\left(1-\frac{8 p^{3}}{x_{1} x_{2} x_{3}}\right)=0
$$

若 $x_{1} x_{2} x_{3}=8 p^{3}$, 则将前面方程组中左右两边分别相乘可得

$$
x_{1}^{4} x_{2}^{4} x_{3}^{4}=64 p^{9}\left(x_{1}+x_{2}\right)\left(x_{2}+x_{3}\right)\left(x_{3}+x_{1}\right)=\left(8 p^{3}\right)^{3} x_{1} x_{2} x_{3},
$$

于是有

$$
8 x_{1} x_{2} x_{3}=\left(x_{1}+x_{2}\right)\left(x_{2}+x_{3}\right)\left(x_{3}+x_{1}\right) \geqslant 2 \sqrt{x_{1} x_{2}} \cdot 2 \sqrt{x_{2} x_{3}} \cdot 2 \sqrt{x_{3} x_{1}}=8 x_{1} x_{2} x_{3},
$$

所以 $x_{1}=x_{2}=x_{3}$, 矛盾;

所以有 $x_{1} x_{2}+x_{2} x_{3}+x_{3} x_{1}=0$, 进而原命题得证.

解法二 设 $A\left(2 p a^{2}, 2 p a\right), B\left(2 p b^{2}, 2 p b\right), C\left(2 p c^{2}, 2 p c\right)$, 有 $a^{2} \neq b^{2} \neq c^{2}$.

从而直线 $A B$ 的方程为

$$
y-2 p a=\frac{2 p b-2 p a}{2 p b^{2}-2 p a^{2}}\left(x-2 p a^{2}\right)=\frac{1}{a+b}\left(x-2 p a^{2}\right),
$$

联立 $A B$ 的方程与 $x^{2}=2 p y$ 消去 $y$ 得

$$
x^{2}-\frac{2 p}{a+b} x-\frac{4 p^{2} a b}{a+b}=0
$$

由直线 $A B$ 与曲线 $x^{2}=2 p y$ 相切得判别式

$$
\Delta_{1}=4 p^{2} \frac{1}{(a+b)^{2}}+\frac{16 p^{2} a b}{a+b}=0
$$

整理得 $1+4 a b(a+b)=0$.

同理有 $1+4 b c(b+c)=0$, 两式相减得

$$
4 b(a-c)(a+c+b)=0
$$

因为 $b \neq 0, a \neq c$, 所以 $a+b+c=0$, 命题得证.
也可以由 $a, c$ 是方程 $1+4 b x(b+x)=0$ 的两根得到 $a+c=-b$.

## 第 671 题 以不变应万变

在平面直角坐标系 $x O y$ 上, 给定拖物线 $L: y=\frac{1}{4} x^{2}$. 实数 $p, q$ 满足 $p^{2}-4 q \geqslant 0, x_{1}, x_{2}$ 是方程 $x^{2}-$ $p x+q=0$ 的两根, 记 $\varphi(p, q)=\max \left\{\left|x_{1}\right|,\left|x_{2}\right|\right\}$.

(1) 过点 $A\left(p_{0}, \frac{1}{4} p_{0}^{2}\right)\left(p_{0} \neq 0\right)$ 作 $L$ 的切线交 $y$ 轴于点 $B$. 证明: 对线段 $A B$ 上的任一点 $Q(p, q)$, 有 $\varphi(p, q)=\frac{1}{2}\left|p_{0}\right|$

(2) 设 $M(a, b)$ 是定点, 其中 $a, b$ 满足 $a^{2}-4 b>0, a \neq 0$. 过 $M(a, b)$ 作 $L$ 的两条切线 $l_{1}, l_{2}$, 切点分别为 $E\left(p_{1}, \frac{1}{4} p_{1}^{2}\right), E^{\prime}\left(p_{2}, \frac{1}{4} p_{2}^{2}\right), l_{1}, l_{2}$ 与 $y$ 轴分别交于 $F, F^{\prime}$ 两点, 线段 $E F$ 上异于两端点的点集记为 $X$,证明: $M(a, b) \in X \Leftrightarrow\left|p_{1}\right|>\left|p_{2}\right| \Leftrightarrow \varphi(a, b)=\frac{1}{2}\left|p_{1}\right|$;

(3) 记 $\left.D=\{x, y) \mid y \leqslant x-1, y \geqslant \frac{1}{4}(x+1)^{2}-\frac{5}{4}\right\}$, 当 $(p, q)$ 取遍 $D$ 时, 求 $\varphi(p, q)$ 的最小值 (记为 $\varphi_{\text {min }}$ ) 和最大值 $\left(\right.$ 记为 $\left.\varphi_{\text {max }}\right)$.

解析 解法一 (1) 显然 $A\left(p_{0}, \frac{1}{4} p_{0}^{2}\right)$ 在抛物线 $L$ 上,

于是过点 $A$ 的抛物线 $L$ 的切线方程为

$$
y=\frac{1}{2} p_{0} x-\frac{1}{4} p_{0}^{2}
$$

若 $p_{0}>0$, 则线段 $A B$ 的方程为

$$
y=\frac{1}{2} p_{0} x-\frac{1}{4} p_{0}^{2}, 0 \leqslant x \leqslant p_{0},
$$

若 $p_{0}<0$, 则线段 $A B$ 的方程为

$$
y=\frac{1}{2} p_{0} x-\frac{1}{4} p_{0}^{2}, p_{0} \leqslant x \leqslant 0
$$

又若 $p^{2}-4 q \geqslant 0$, 则方程 $x^{2}-p x+q=0$ 的两根为 $\frac{p \pm \sqrt{p^{2}-4 q}}{2}$,

若 $Q(p, q)$ 在线段 $A B$ 上,则

$$
q=\frac{1}{2} p_{0} p-\frac{1}{4} p_{0}^{2}
$$

从而 $p^{2}-4 q=\left(p-p_{0}\right)^{2}$, 从而两根为

$$
x_{1,2}=\frac{p \pm\left|p-p_{0}\right|}{2}
$$

当 $p_{0}>0$ 时, $0 \leqslant p \leqslant p_{0}$, 则

$$
\varphi(p, q)=\max \left\{\left|x_{1}\right|,\left|x_{2}\right|\right\}=\frac{p_{0}}{2}=\frac{\left|p_{0}\right|}{2} ;
$$

当 $p_{0}<0$ 时, $p_{0} \leqslant p \leqslant 0$, 则

$$
\varphi(p, q)=\max \left\{\left|x_{1}\right|,\left|x_{2}\right|\right\}=\frac{-p_{0}}{2}=\frac{\left|p_{0}\right|}{2} .
$$

因此原命题得证.

(2) 由题意知 $l_{1}, l_{2}$ 的方程分别为

$$
l_{1}: y=\frac{1}{2} p_{1} x-\frac{1}{4} p_{1}^{2}, l_{2}: y=\frac{1}{2} p_{2} x-\frac{1}{4} p_{2}^{2}
$$

联立解得点 $M$ 的坐标为 $(a, b)=\left(\frac{p_{1}+p_{2}}{2}, \frac{p_{1} p_{2}}{4}\right)$.

从而考虑方程

$$
x^{2}-\frac{p_{1}+p_{2}}{2} x+\frac{p_{1} p_{2}}{4}=0
$$

它的两根为 $\frac{1}{2} p_{1}, \frac{1}{2} p_{2}$, 所以 $\varphi(a, b)=\frac{1}{2} \max \left\{\left|p_{1}\right|,\left|p_{2}\right|\right\}$.

由此知 $\left|p_{1}\right|>\left|p_{2}\right|$ 等价于 $\varphi(a, b)=\frac{1}{2}\left|p_{1}\right|$.

下面证明当 $M(a, b) \in X$ 与它们等价.

由 (1) 知 $M(a, b) \in X$ 时, $\varphi(a, b)=\frac{1}{2}\left|p_{1}\right|$;

若 $\left|p_{1}\right|>\left|p_{2}\right|$, 有

$$
|a| \leqslant \frac{\left|p_{1}\right|+\left|p_{2}\right|}{2}<\frac{\left|p_{1}\right|+\left|p_{1}\right|}{2}=\left|p_{1}\right|
$$

从而有 $M(a, b) \in X$.

(3) 如图, $D$ 表示直线 $y=x-1$ 与抛物线 $y=\frac{1}{4}(x+1)^{2}-\frac{5}{4}$ 所围成的封闭区域 (包含边界), 其中 $A(0,-1), B(2,1)$ 是直线与抛物线的两个交点.

当点 $(p, q) \in D$ 时, 有

$$
\frac{1}{4}(p+1)^{2}-\frac{5}{4} \leqslant q \leqslant p-1
$$

从而

$$
(p-2)^{2} \leqslant p^{2}-4 q \leqslant 4-2 p
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-133.jpg?height=355&width=341&top_left_y=1265&top_left_x=1518)

其中 $0 \leqslant p \leqslant 2$. 于是有

$$
\frac{p+|p-2|}{2} \leqslant \varphi(p, q)=\frac{p+\sqrt{p^{2}-4 q}}{2} \leqslant \frac{p+\sqrt{4-2 p}}{2}
$$

从而

$$
\varphi(p, q) \geqslant \frac{p+2-p}{2}=1
$$

因此 $\varphi_{\text {min }}=1$.

设 $\sqrt{4-2 p}=t$, 其中 $t \in[0,2]$, 则

$$
\frac{p+\sqrt{4-2 p}}{2}=\frac{\frac{4-t^{2}}{2}+t}{2}=-\frac{-(t+1)^{2}+5}{4} \leqslant \frac{5}{4}
$$

所以 $\varphi_{\text {max }}=\frac{5}{4}$.

综上所述, $\varphi_{\min }=1$ 且 $\varphi_{\max }=\frac{5}{4}$.

解法二 (1) 过点 $A$ 的抛物线 $L$ 的切线方程为

$$
y=\frac{1}{2} p_{0} x-\frac{1}{4} p_{0}^{2}
$$

于是有 $q=\frac{1}{2} p_{0} p-\frac{1}{4} p_{0}^{2}$, 从而考虑方程 $x^{2}-p x+\frac{1}{2} p_{0} p-\frac{1}{4} p_{0}^{2}=0$ 的两根即可.

记方程左边为 $f(x)$, 则有

$$
f\left(\frac{1}{2} p_{0}\right)=0, f\left(-\frac{1}{2} p_{0}\right)=p_{0} p>0
$$

所以方程的一根为 $\frac{1}{2} p_{0}$, 另一根 $x^{\prime} \in\left(-\frac{1}{2}\left|p_{0}\right|, \frac{1}{2}\left|p_{0}\right|\right)$, 从而知 $\varphi(p, q)=\frac{1}{2}\left|p_{0}\right|$.

(2) 见解法一.

(3) 见解法一.

## 第 672 题 相切于抛物线

设抛物线 $C: y=x^{2}$ 的焦点为 $F$, 动点 $P$ 在直线 $l: x-y-2=0$ 上运动, 过点 $P$ 作抛物线 $C$ 的两条切线 $P A, P B$ 且与抛物线分别相切于点 $A, B$.

(1) 求 $\triangle A P B$ 的重心 $G$ 的轨迹方程;

(2)求证: $\angle P F A=\angle P F B$.

解析 解法一 (1) 设 $A\left(a, a^{2}\right), B\left(b, b^{2}\right)$,则

$$
P A: y+a^{2}=2 a x, P B: y+b^{2}=2 b x,
$$

于是 $P\left(\frac{a+b}{2}, a b\right)$.

设 $G(x, y)$, 则

$$
\left\{\begin{array}{l}
x=\frac{1}{3}\left(a+b+\frac{a+b}{2}\right)=\frac{a+b}{2} \\
y=\frac{1}{3}\left(a^{2}+b^{2}+a b\right)
\end{array}\right.
$$

又 $P$ 点在直线 $x-y-2=0$ 上, 于是

$$
\frac{a+b}{2}-a b-2=0
$$

消去 $a+b, a b$, 可得所求的轨迹方程为 $y=\frac{4}{3} x^{2}-\frac{1}{3} x+\frac{2}{3}$.

(2) 分别作焦点 $F$ 关于直线 $P A$ 和 $P B$ 的对称点 $F_{1}$ 和 $F_{2}$, 连结 $F_{1} A, F_{1} P, F_{2} B$, $F_{2} P, F_{1} F_{2}$, 如图.

由抛物线的光学性质 (因为从焦点射人的直线经抛物线反射后与对称轴平行,所以 $F A$ 关于切线 $A P$ 的对称直线平行于抛物线的对称轴) 可得 $A F_{1} / / O F / / B F_{2}$, $F_{1}, F_{2}$ 均在抛物线的准线上 (因为 $F A=A F_{1}$, 且 $A F_{1}$ 与 $y$ 轴平行), 于是 $\left|P F_{1}\right|=$ $|P F|=\left|P F_{2}\right|, \angle P F_{1} F_{2}=\angle P F_{2} F_{1}$, 从而

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-134.jpg?height=515&width=354&top_left_y=1649&top_left_x=1413)

$\angle A F_{1} P=\angle B F_{2} P=\angle A F P=\angle B F P$,

原命题得证.

## 解法二 $(1)$ 见解法一.

(2) 由 (1) 知 $F\left(0, \frac{1}{4}\right), A\left(a, a^{2}\right), B\left(b, b^{2}\right), P\left(\frac{a+b}{2}, a b\right)$.

所以

$$
\begin{aligned}
\cos \angle P F A & =\frac{\overrightarrow{F A} \cdot \overrightarrow{F P}}{|\overrightarrow{F A}| \cdot|\overrightarrow{F P}|} \\
& =\frac{1}{|P F|} \cdot \frac{\left(a, a^{2}-\frac{1}{4}\right) \cdot\left(\frac{a+b}{2}, a b-\frac{1}{4}\right)}{a^{2}+\frac{1}{4}} \\
& =\frac{a b+\frac{1}{4}}{|P F|}
\end{aligned}
$$

同理有

$$
\cos \angle P F B=\frac{a b+\frac{1}{4}}{|P F|}=\cos \angle P F A
$$

从而命题得证.

## 第 673 题 游刃有余

已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$, 点 $P\left(x_{0}, y_{0}\right)$ 是椭圆 $E$ 内部一点, 过 $P$ 作直线 $l$ 与椭圆 $E$ 交于 $A, B$ 两点, 设椭圆 $E$ 在 $A, B$ 处的切线交于点 $Q$, 求 $Q$ 点的轨迹方程, 并求 $\triangle Q A B$ 面积的最小值.

解析 设 $Q(m, n)$, 则直线 $A B$ :

$$
\frac{m x}{a^{2}}+\frac{n y}{b^{2}}=1
$$

因此

$$
\frac{m x_{0}}{a^{2}}+\frac{n y_{0}}{b^{2}}=1
$$

这样我们就得到了点 $Q$ 的轨迹为直线 $l: \frac{x_{0} x}{a^{2}}+\frac{y_{0} y}{b^{2}}=1$.

作仿射变换 $x^{\prime}=x, y^{\prime}=\frac{a}{b} y$, 则椭圆 $E$ 变为圆 $E^{\prime}: x^{\prime 2}+y^{\prime 2}=a^{2}$, 此时 $P^{\prime}\left(x_{0}, \frac{a}{b} y_{0}\right), Q^{\prime}$ 点的轨迹变为直线 $l^{\prime}: x_{0} x^{\prime}+\frac{a}{b} y_{0} y^{\prime}=a^{2}$, 且有

$$
S_{\triangle Q^{\prime} A^{\prime} B^{\prime}}=\frac{a}{b} S_{\triangle Q A B}
$$

设点 $Q^{\prime}$ 到圆 $E^{\prime}$ 的圆心 $O^{\prime}$ 的距离为 $d$, 则

$$
\begin{aligned}
S_{\triangle Q_{A} A^{\prime} B^{\prime}} & =\frac{1}{2} \sin \left(2 \angle A^{\prime} Q^{\prime} O^{\prime}\right) \cdot\left|Q^{\prime} A^{\prime}\right|^{2} \\
& =\frac{a \cdot \sqrt{d^{2}-a^{2}}}{d^{2}} \cdot\left(d^{2}-a^{2}\right) \\
& =a \cdot \sqrt{1-\frac{a^{2}}{d^{2}}} \cdot\left(d-\frac{a^{2}}{d}\right)
\end{aligned}
$$

这个关于 $d$ 的函数单调递增, 于是当 $d$ 取最小值 $\frac{a^{2}}{\sqrt{x_{0}^{2}+\frac{a^{2}}{b^{2}} y_{0}^{2}}}$ 时, $\triangle Q^{\prime} A^{\prime} B^{\prime}$ 的面积取得最小值, 对应的 $\triangle Q A B$ 面积的最小值为

$$
\frac{b}{a} \cdot \sqrt{\frac{\left(a^{2}-x_{0}^{2}-\frac{a^{2}}{b^{2}} y_{0}^{2}\right)^{3}}{x_{0}^{2}+\frac{a^{2}}{b^{2}} y_{0}^{2}}}=a b \sqrt{\frac{(1-k)^{3}}{k}}
$$

其中 $k=\frac{x_{0}^{2}}{a^{2}}+\frac{y_{0}^{2}}{b^{2}}$.

## 第 674 题 直线与圆

过直线 $l: x+y=2$ 上任意一点 $P$ 向圆 $C: x^{2}+y^{2}=1$ 作两条切线, 切点分别为 $A, B$. 线段 $A B$ 的中点为 $Q$, 则点 $Q$ 到直线 $l$ 的距离的取值范围是

解析 $\left[\frac{\sqrt{2}}{2}, \sqrt{2}\right)$.

解法一 设 $P(m, 2-m)$, 则切点弦 $A B$ 所在的直线方程为

$$
m x+(2-m) y=1,
$$

直线 $O Q$ 的方程为

$$
(2-m) x-m y=0,
$$

联立可解得

$$
Q\left(\frac{m}{m^{2}+(2-m)^{2}}, \frac{2-m}{m^{2}+(2-m)^{2}}\right)
$$

从而点 $Q$ 到 $l$ 的距离

$$
d=\sqrt{2}\left|\frac{1}{2(m-1)^{2}+2}-1\right|
$$

因此 $d$ 的取值范围是 $\left[\frac{\sqrt{2}}{2}, \sqrt{2}\right)$.

解法二 过点 $A, O$ 分别作 $Q H, O D$ 垂直于 $l$, 垂足为 $H, D$, 如图, 有

$$
\frac{Q H}{O D}=\frac{P Q}{P O}
$$

由直角三角形的射影定理知

$$
P Q \cdot P O=P B^{2}=P O^{2}-1,
$$

所以有

$$
Q H=\sqrt{2} \cdot \frac{P O^{2}-1}{P O^{2}}=\sqrt{2}\left(1-\frac{1}{P O^{2}}\right)
$$

因为 $P O \in[\sqrt{2},+\infty)$, 可以得到 $Q H \in\left[\frac{\sqrt{2}}{2}, \sqrt{2}\right)$.

事实上, $Q$ 点的轨迹是直线 $l$ 对圆 $C$ 的反演圆:

$$
x\left(x-\frac{1}{2}\right)+y\left(y-\frac{1}{2}\right)=0
$$

## 第 675 题 圆中的弦

如图, 已知动直线 $l$ 经过点 $P(4,0)$, 交抛物线 $y^{2}=2 a x(a>0)$ 于 $A, B$ 两点. 坐标原点 $O$ 是 $P Q$ 的中点, 设直线 $A Q, B Q$ 的斜率分别为 $k_{A Q}, k_{B Q}$.

(1) 证明: $k_{A Q}+k_{B Q}=0$;

(2) 当 $a=2$ 时, 是否存在垂直于 $x$ 轴的直线 $l^{\prime}$, 被以 $A P$ 为直径的圆截得的弦长为定值? 若存在, 请求出直线 $l^{\prime}$ 的方程; 若不存在, 请说明理由.

解析 (1) 已知 $P(4,0), Q(-4,0)$.

设 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 直线 $A B: x=m y+4$, 则

$$
k_{A Q}+k_{B Q}=0,
$$

即

$$
\frac{y_{1}}{x_{1}+4}+\frac{y_{2}}{x_{2}+4}=0
$$

也即

$$
y_{1}\left(x_{2}+4\right)+y_{2}\left(x_{1}+4\right)=0,
$$

等价于

$$
y_{1}\left(m y_{2}+8\right)+y_{2}\left(m y_{1}+8\right)=0,
$$

于是只需证

$$
m y_{1} y_{2}+4\left(y_{1}+y_{2}\right)=0
$$

联立直线与抛物线有

$$
y^{2}-2 a m y-8 a=0,
$$

所以

$$
y_{1} y_{2}=-8 a, y_{1}+y_{2}=2 a m \text {. }
$$

因此原命题得证.

(2) 假设存在这样的直线 $l^{\prime}: x=t$, 则 $A P$ 的中点 $M$ 到 $l^{\prime}$ 的距离为

$$
\frac{x_{1}+4}{2}-t
$$

因为

$$
|A P|=\sqrt{\left(x_{1}-4\right)^{2}+y_{1}^{2}}
$$

所以半径为

$$
\frac{1}{2}|A P|=\frac{1}{2} \sqrt{\left(x_{1}-4\right)^{2}+4 x_{1}}
$$

所以弦长

$$
\begin{aligned}
l & =\sqrt{\left(x_{1}-4\right)^{2}+4 x_{1}-\left(x_{1}+4-2 t\right)^{2}} \\
& =2 \sqrt{(t-3) x_{1}+4 t-t^{2}}
\end{aligned}
$$

为定值.

所以当 $t=3$ 时符合题意, 此时直线 $l^{\prime}$ 的方程为 $x=3$.

## 第 676 题面积之比

如图 1, 已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的长轴上一点 $M$ $(m, 0)$, 垂直于 $x$ 轴的直线 $l$ 与 $x$ 轴交于点 $N\left(\frac{a^{2}}{m}, 0\right)$. 过点 $M$且斜率不为 0 的直线与椭圆交于 $A, B$ 两点, 分别过 $A, B$ 作直线 $l$ 的垂线, 垂足为 $A_{1}, B_{1}$. 设 $\triangle M A A_{1}, \triangle M B B_{1}, \triangle A_{1} B_{1} M$ 的面积分别为 $S_{1}, S_{2}, S_{3}$, 求证: $\frac{S_{1} S_{2}}{S_{3}^{2}}$ 为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-138.jpg?height=292&width=595&top_left_y=454&top_left_x=1134)

图 1

## 解析 解法一

如图 2, 连结 $A N, B N, A B_{1}, B A_{1}$, 设 $A B_{1}$ 与 $M N$ 交于点 $T$.根据椭圆的极点极线性质, 有

$$
\frac{A M}{A A_{1}}=\frac{B M}{B B_{1}}
$$

因此

$$
\begin{aligned}
& M T=B B_{1} \cdot \frac{A M}{A B}=\frac{A A_{1} \cdot B B_{1}}{A A_{1}+B B_{1}} \\
& N T=A A_{1} \cdot \frac{B_{1} N}{A_{1} B_{1}}=A A_{1} \cdot \frac{B M}{A M}=\frac{A A_{1} \cdot B B_{1}}{A A_{1}+B B_{1}}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-138.jpg?height=297&width=592&top_left_y=874&top_left_x=1171)

图 2

因此 $T$ 点平分 $M N$. 进而可得 $B A_{1}$ 与 $M N$ 的交点也平分 $M N$, 因此 $A B_{1}, A_{1} B, M N$ 三线共点.所以

$$
\begin{aligned}
\frac{S_{1} S_{2}}{S_{3}^{2}} & =\frac{A A_{1} \cdot A_{1} N \cdot B B_{1} \cdot B_{1} N}{\left(M N \cdot A_{1} B_{1}\right)^{2}} \\
& =\frac{1}{4} \cdot \frac{A A_{1}}{T N} \cdot \frac{B B_{1}}{T N} \cdot \frac{A_{1} N \cdot B_{1} N}{A_{1} B_{1}^{2}} \\
& =\frac{1}{4} \cdot \frac{A_{1} B_{1}}{B_{1} N} \cdot \frac{A_{1} B_{1}}{A_{1} N} \cdot \frac{A_{1} N \cdot B_{1} N}{A_{1} B_{1}^{2}} \\
& =\frac{1}{4}
\end{aligned}
$$

因此原命题得证.

解法二 设直线 $A B: x=t y+m, A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$. 记 $n=\frac{a^{2}}{m}$, 联立直线 $A B$ 与椭圆方程可得

$$
\left(b^{2} t+a^{2}\right) y^{2}+2 b^{2} t m y+b^{2}\left(m^{2}-a^{2}\right)=0,
$$

而

$$
\begin{aligned}
\frac{S_{1} S_{2}}{S_{3}^{2}} & =\frac{-y_{1} y_{2}\left(n-x_{1}\right)\left(n-x_{2}\right)}{(n-m)^{2}\left(y_{1}-y_{2}\right)^{2}} \\
& =\frac{-y_{1} y_{2}\left(t y_{1}+m-n\right)\left(t y_{2}+m-n\right)}{(n-m)^{2}\left(y_{1}-y_{2}\right)^{2}} \\
& =\frac{-y_{1} y_{2}\left[t^{2} y_{1} y_{2}-t(n-m)\left(y_{1}+y_{2}\right)+(n-m)^{2}\right]}{(n-m)^{2}\left[\left(y_{1}+y_{2}\right)^{2}-4 y_{1} y_{2}\right]} \\
& =\frac{b^{2}\left(a^{2}-m^{2}\right)\left[t^{2} b^{2}\left(m^{2}-a^{2}\right)+t(n-m) \cdot 2 b^{2} t m+(n-m)^{2}\left(b^{2} t^{2}+a^{2}\right)\right]}{(n-m)^{2}\left[4 a^{2} b^{2}\left(b^{2} t^{2}+a^{2}\right)-4 a^{2} b^{2} m^{2}\right]} \\
& =\frac{a^{2}-m^{2}}{4 a^{2}(n-m)^{2}} \cdot \frac{b^{2} t^{2}\left(n^{2}-a^{2}\right)+a^{2}(n-m)^{2}}{b^{2} t^{2}+a^{2}-m^{2}},
\end{aligned}
$$

而

$$
\left(a^{2}-m^{2}\right)\left(n^{2}-a^{2}\right)=-m^{2} n^{2}+a^{2}\left(n^{2}+m^{2}\right)-a^{4}=a^{2}(n-m)^{2},
$$

因此可得 $\frac{S_{1} S_{2}}{S_{3}^{2}}$ 为定值 $\frac{1}{4}$.

## 第 677 题 参数方程

已知 $A, B$ 为双曲线 $C: \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(b>a>0)$ 上的两点, 且以线段 $A B$ 为直径的圆通过坐标原点 $O$,则 $\triangle A O B$ 面积的最小值为

解析 $\frac{a^{2} b^{2}}{b^{2}-a^{2}}$.

不妨设 $A\left(r_{1} \cos \theta, r_{1} \sin \theta\right), B\left(-r_{2} \sin \theta, r_{2} \cos \theta\right)$, 则有

$$
\left\{\begin{array}{l}
\frac{r_{1}^{2} \cos ^{2} \theta}{a^{2}}-\frac{r_{1}^{2} \sin ^{2} \theta}{b^{2}}=1 \\
\frac{r_{2}^{2} \sin ^{2} \theta}{a^{2}}-\frac{r_{2}^{2} \cos ^{2} \theta}{b^{2}}=1
\end{array}\right.
$$

于是

$$
\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}=\frac{1}{a^{2}}-\frac{1}{b^{2}}
$$

进而可得 $\triangle A O B$ 的面积

$$
S=\frac{1}{2} r_{1} r_{2}=\frac{1}{2} r_{1} r_{2} \cdot\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}\right) \cdot \frac{1}{\frac{1}{a^{2}}-\frac{1}{b^{2}}}=\frac{1}{2}\left(\frac{r_{2}}{r_{1}}+\frac{r_{1}}{r_{2}}\right) \cdot \frac{a^{2} b^{2}}{b^{2}-a^{2}} \geqslant \frac{a^{2} b^{2}}{b^{2}-a^{2}}
$$

等号当 $r_{1}=r_{2}$ 时取得.

因此所求面积的最小值为 $\frac{a^{2} b^{2}}{b^{2}-a^{2}}$.

## 第 678 题椭圆内接三角形

已知 $A$ 是椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的下顶点, 若以 $A$ 为直角顶点的椭圆内接等腰直角三角形有且仅有 3 个, 求椭圆离心率 $e$ 的取值范围.

解析 将坐标系 $x O y$ 的原点平移到点 $A$, 则椭圆方程变为

$$
\frac{x^{2}}{a^{2}}+\frac{(y-b)^{2}}{b^{2}}=1
$$

即

$$
\frac{x^{2}}{a^{2}}-\frac{2}{b} y+\frac{y^{2}}{b^{2}}=0
$$

此时不妨设以 $A$ 为直角顶点的椭圆内接等腰直角三角形为 $\triangle A B C$, 且 $B(r, \theta), C\left(r, \theta+\frac{\pi}{2}\right)$, 其中 $\theta$ 是第一象限的角. 代人椭圆方程可得

$$
\left\{\begin{array}{l}
\frac{r^{2} \cos ^{2} \theta}{a^{2}}-\frac{2 r \sin \theta}{b}+\frac{r^{2} \sin ^{2} \theta}{b^{2}}=0 \\
\frac{r^{2} \sin ^{2} \theta}{a^{2}}-\frac{2 r \cos \theta}{b}+\frac{r^{2} \cos ^{2} \theta}{b^{2}}=0
\end{array}\right.
$$

根据题意, 这个关于 $(r, \theta)$ 的方程组有且仅有 3 组解. 该方程组等价于

$$
r=\frac{\frac{2 \sin \theta}{b}}{\frac{\cos ^{2} \theta}{a^{2}}+\frac{\sin ^{2} \theta}{b^{2}}}=\frac{\frac{2 \cos \theta}{b}}{\frac{\sin ^{2} \theta}{a^{2}}+\frac{\cos ^{2} \theta}{b^{2}}}
$$

于是

$$
(\sin \theta-\cos \theta)\left(\frac{1+\sin \theta \cos \theta}{a^{2}}-\frac{\sin \theta \cos \theta}{b^{2}}\right)=0,
$$

即

$$
\theta=\frac{\pi}{4}
$$

或

$$
\sin 2 \theta=\frac{2 b^{2}}{a^{2}-b^{2}}
$$

这就意味着当 $\frac{2 b^{2}}{a^{2}-b^{2}}<1$ 时符合题意, 也即 $e>\frac{\sqrt{6}}{3}$ 时符合题意.

综上所述, 椭圆离心率 $e$ 的取值范围是 $\left(\frac{\sqrt{6}}{3}, 1\right)$.

## 第 679 题 化齐次联立处理垂直

已知 $P\left(x_{0}, y_{0}\right)$ 是一次曲线 $\Gamma: A x^{2}+B y^{2}+D x+E y+F=0$ 上一点, 过点 $P$ 作互相垂直的直线分别交 $\Gamma$ 于点 $A, B$, 求证:直线 $A B$ 过定点.

解析 由点 $P$ 在曲线 $\Gamma$ 上, 可得

$$
A x_{0}^{2}+B y_{0}^{2}+D x_{0}+E y_{0}+F=0
$$

将坐标系 $x O y$ 的原点平移到点 $P$ 位置, 得到坐标系 $x^{\prime} P y^{\prime}$, 则此时曲线 $\Gamma^{\prime}$ 的方程为

$$
A\left(x^{\prime}+x_{0}\right)^{2}+B\left(y^{\prime}+y_{0}\right)^{2}+D\left(x^{\prime}+x_{0}\right)+E\left(y^{\prime}+y_{0}\right)+F=0
$$

也即

$$
A x^{\prime 2}+B y^{\prime 2}+\left(D+2 A x_{0}\right) x+\left(E+2 B y_{0}\right) y=0
$$

设直线 $A^{\prime} B^{\prime}: m x^{\prime}+n y^{\prime}=1$, 与 $\Gamma^{\prime}$ 化齐次联立, 有

$$
A x^{\prime 2}+B y^{\prime 2}+\left[\left(D+2 A x_{0}\right) x^{\prime}+\left(E+2 B y_{0}\right) y^{\prime}\right] \cdot\left(m x^{\prime}+n y^{\prime}\right)=0
$$

由 $P A^{\prime} \perp P B^{\prime}$ 可得

$$
A+B+\left(D+2 A x_{0}\right) m+\left(E+2 B y_{0}\right) n=0
$$

也即

$$
\left(-\frac{D+2 A x_{0}}{A+B}\right) \cdot m+\left(-\frac{E+2 B y_{0}}{A+B}\right) \cdot n=1
$$

因此直线 $A^{\prime} B^{\prime}$ 恒过点 $Q^{\prime}\left(-\frac{E+2 A y_{0}}{A+B},-\frac{E+2 B y_{0}}{A+B}\right)$, 换算到原坐标系 $x O y$, 可得所求定点为

$$
Q\left(\frac{(B-A) x_{0}-D}{A+B}, \frac{(A-B) y_{0}-E}{A+B}\right)
$$

化齐次联立后的方程为

$$
p y^{2}+q x y+r x^{2}=0
$$

其中

$$
\begin{aligned}
& p=B+\left(E+2 B y_{0}\right) n \\
& q=\left(D+2 A x_{0}\right) n+\left(E+2 B y_{0}\right) m \\
& r=A+\left(D+2 A x_{0}\right) m
\end{aligned}
$$

因此若将 “过点 $P$ 作互相垂直的直线”改成“作斜率乘积为 $\lambda$ 的直线”, 则所求的定点为

$$
Q\left(-\frac{(A+B \lambda) x_{0}+D}{A-B \lambda}, \frac{(A+B \lambda) y_{0}+\lambda E}{A-B \lambda}\right)
$$

进一步,若斜率之和为 $\mu$,则所求的定点为

$$
Q\left(x_{0}-\frac{2}{\mu} y_{0}-\frac{E}{B \mu},-\frac{2 A}{B \mu} x_{0}-y_{0}-\frac{D+E \mu}{B \mu}\right)
$$

若斜率倒数之和为 $\delta$, 则所求的定点为

$$
Q\left(-x_{0}-\frac{2 B}{A \delta} y_{0}-\frac{D \delta+E}{A \delta},-\frac{2}{\delta} x_{0}+y_{0}-\frac{D}{A \delta}\right)
$$

## 第 680 题 环环相扣

已知 $A$ 是椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的右顶点, 过点 $A$ 作互相垂直的两条直线 $A P$ 和 $A Q$ 分别交椭圆于 $P, Q$ 两点.

(1) 求证: 直线 $P Q$ 过定点 $R$, 并求出定点 $R$ 的坐标;

(2)求 $\triangle A P Q$ 面积的最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-141.jpg?height=289&width=488&top_left_y=1346&top_left_x=1372)

解析 (1) 将坐标系平移至以 $A$ 为新坐标原点, 则

$$
E^{\prime}: \frac{x^{\prime 2}}{a^{2}}+\frac{y^{\prime 2}}{b^{2}}+\frac{2}{a} x^{\prime}=0
$$

设新坐标系下直线 $P^{\prime} Q^{\prime}$ 的方程为 $m x^{\prime}+n y^{\prime}=1$, 化齐次联立可得

$$
\frac{x^{\prime 2}}{a^{2}}+\frac{y^{\prime 2}}{b^{2}}+\frac{2}{a} x^{\prime}\left(m x^{\prime}+n y^{\prime}\right)=0
$$

由于 $A P \perp A Q$, 于是

$$
\frac{1}{a^{2}}+\frac{1}{b^{2}}+\frac{2 m}{a}=0
$$

于是 $m$ 为定值, 直线 $P^{\prime} Q^{\prime}$ 恒过定点 $R^{\prime}\left(\frac{1}{m}, 0\right)$, 即 $R^{\prime}\left(-\frac{2 a b}{a^{2}+b^{2}} \cdot b, 0\right)$.

因此在原坐标系下对应的 $R$ 点坐标为

$$
\left(\frac{a^{2}-b^{2}}{a^{2}+b^{2}} \cdot a, 0\right)
$$

(2) 考虑到 $R$ 点为定点, 于是

$$
\frac{S_{\triangle A P Q}}{S_{\triangle O P Q}}=\frac{A R}{O R}=\frac{2 b^{2}}{a^{2}-b^{2}}
$$

接下来计算 $\triangle O P Q$ 面积的最大值.

在仿射变换 $x^{\prime}=x, y^{\prime}=\frac{a}{b} y$ 下, 椭圆 $E$ 变为圆

$$
E^{\prime}: x^{\prime 2}+y^{\prime 2}=a^{2}
$$

设点 $O$ 到直线 $P^{\prime} Q^{\prime}$ 的距离为 $d$, 则 $d$ 的取值范围为 $(0, O R]$, 即 $\left(0, \frac{a^{2}-b^{2}}{a^{2}+b^{2}} \cdot a\right]$, 此时 $\triangle O P^{\prime} Q^{\prime}$ 的面积

$$
S=\frac{1}{2} \cdot d \cdot 2 \sqrt{a^{2}-d^{2}}=\sqrt{d^{2}\left(a^{2}-d^{2}\right)}
$$

情形一 $\frac{a^{2}-b^{2}}{a^{2}+b^{2}} \geqslant \frac{1}{\sqrt{2}}$, 即 $\frac{a}{b} \geqslant \sqrt{2}+1$, 当 $d^{2}=\frac{a^{2}}{2}$ 时 $S$ 取得最大值 $\frac{a^{2}}{2}$.

此时 $\triangle O P Q$ 的面积的最大值为

$$
\frac{b}{a} \cdot \frac{a^{2}}{2}=\frac{1}{2} a b
$$

进而对应 $\triangle A P Q$ 面积的最大值为

$$
\frac{1}{2} a b \cdot \frac{2 b^{2}}{a^{2}-b^{2}}=\frac{a b^{3}}{a^{2}-b^{2}}
$$

情形二 $\frac{a^{2}-b^{2}}{a^{2}+b^{2}}<\frac{1}{\sqrt{2}}$, 即 $\frac{a}{b}<\sqrt{2}+1$, 当 $d=\frac{a^{2}-b^{2}}{a^{2}+b^{2}} \cdot a$ 时 $S$ 取得最大值

$$
\frac{a^{2}-b^{2}}{a^{2}+b^{2}} \cdot a \cdot \sqrt{a^{2}-\left(\frac{a^{2}-b^{2}}{a^{2}+b^{2}}\right)^{2} \cdot a^{2}}=\frac{2 a^{3} b\left(a^{2}-b^{2}\right)}{\left(a^{2}+b^{2}\right)^{2}}
$$

此时 $\triangle O P Q$ 的面积的最大值为

$$
\frac{b}{a} \cdot \frac{2 a^{3} b\left(a^{2}-b^{2}\right)}{\left(a^{2}+b^{2}\right)^{2}}=\frac{2 a^{2} b^{2}\left(a^{2}-b^{2}\right)}{\left(a^{2}+b^{2}\right)^{2}}
$$

进而对应 $\triangle A P Q$ 的面积的最大值为

$$
\frac{2 a^{2} b^{2}\left(a^{2}-b^{2}\right)}{\left(a^{2}+b^{2}\right)^{2}} \cdot \frac{2 b^{2}}{a^{2}-b^{2}}=\frac{4 a^{2} b^{4}}{\left(a^{2}+b^{2}\right)^{2}}
$$

综上所述, $\triangle A P Q$ 面积的最大值为

$$
\left\{\begin{array}{l}
\frac{a b^{3}}{a^{2}-b^{2}}, \quad \frac{a}{b} \geqslant \sqrt{2}+1 \\
\frac{4 a^{2} b^{4}}{\left(a^{2}+b^{2}\right)^{2}}, \frac{a}{b}<\sqrt{2}+1
\end{array}\right.
$$

## 第 681 题 兵来将挡

已知椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0), A$ 为椭圆 $E$ 的右顶点, $M, N$ 是椭圆 $E$ 上不同于 $A$ 的两点, 且直线 $A M$ 和 $A N$ 的斜率之积为 $\lambda$.

(1) 求证: 直线 $M N$ 过定点 $R$;

(2) 若 $\lambda=-\frac{b^{2}}{a^{2}}, P$ 为椭圆 $E$ 上不同于 $M, N$ 的一点, 且 $|P M|=|P N|$, 求 $\triangle M N P$ 的面积的最小值.

解析 (1) 平移坐标系 $x O y$ 至以 $A$ 为坐标原点, 则

$$
E^{\prime}: \frac{\left(x^{\prime}+a\right)^{2}}{a^{2}}+\frac{y^{\prime 2}}{b^{2}}=1
$$

即

$$
E^{\prime}: \frac{x^{\prime 2}}{a^{2}}+\frac{y^{\prime 2}}{b^{2}}+\frac{2}{a} x^{\prime}=0
$$

设直线 $M^{\prime} N^{\prime}: m x^{\prime}+n y^{\prime}=1$, 与椭圆 $E^{\prime}$ 的方程化齐次联立, 得

$$
\frac{x^{\prime 2}}{a^{2}}+\frac{y^{\prime 2}}{b^{2}}+\frac{2}{a} x^{\prime}\left(m x^{\prime}+n y^{\prime}\right)=0
$$

## 高考数学满分学霸的解题笔记(一千零一题)

即

$$
\frac{1}{b^{2}} y^{\prime 2}+\frac{2 n}{a} x^{\prime} y^{\prime}+\left(\frac{1}{a^{2}}+\frac{2 m}{a}\right) x^{\prime 2}=0
$$

于是由直线 $A^{\prime} M^{\prime}$ 与直线 $A^{\prime} N^{\prime}$ 的斜率之积为 $\lambda$, 可得

$$
\frac{\frac{1}{a^{2}}+\frac{2 m}{a}}{\frac{1}{b^{2}}}=\lambda
$$

因此

$$
\frac{1}{m}=\frac{2 a b^{2}}{\lambda a^{2}-b^{2}}
$$

为定值, 进而直线 $M N$ 过定点

$$
R^{\prime}\left(\frac{2 a b^{2}}{\lambda a^{2}-b^{2}}, 0\right)
$$

回到原坐标, 定点为 $R\left(\frac{\lambda a^{2}+b^{2}}{\lambda a^{2}-b^{2}} \cdot a, 0\right)$.

注意到根据椭圆的垂径定理，椭圆 $E$ 上的任意一点与关于原点对称的两点的连线的斜率之积 (当斜率均存在时) 为 $-\frac{b^{2}}{a^{2}}$, 因此若 $\lambda=-\frac{b^{2}}{a^{2}}$, 则直线 $M N$ 恒过原点 $O$.

(2)当 $\lambda=-\frac{b^{2}}{a^{2}}$ 时, $R$ 即坐标原点 $O$. 此时 $O$ 点平分线段 $M N$, 因此

$$
O P \perp M N
$$

不妨设 $M\left(r_{1} \cos \theta, r_{1} \sin \theta\right), P\left(r_{2} \cos \left(\theta+\frac{\pi}{2}\right), r_{2} \sin \left(\theta+\frac{\pi}{2}\right)\right)$, 此时有

$$
\frac{\left(r_{1} \cos \theta\right)^{2}}{a^{2}}+\frac{\left(r_{1} \sin \theta\right)^{2}}{b^{2}}=1
$$

$$
\frac{\left[r_{2} \cos \left(\theta+\frac{\pi}{2}\right)\right]^{2}}{a^{2}}+\frac{\left[r_{2} \sin \left(\theta+\frac{\pi}{2}\right)\right]^{2}}{b^{2}}=1,
$$

因此

$$
\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}=\frac{1}{a^{2}}+\frac{1}{b^{2}}
$$

而 $\triangle P M N$ 的面积为

$$
\begin{aligned}
\frac{1}{2}|M N| \cdot|O P|= & r_{1} r_{2} \\
& =\frac{r_{1} r_{2} \cdot\left(\frac{1}{r_{1}^{2}}+\frac{1}{r_{2}^{2}}\right)}{\frac{1}{a^{2}}+\frac{1}{b^{2}}} \\
& =\frac{\frac{r_{2}}{r_{1}}+\frac{r_{1}}{r_{3}}}{\frac{1}{a^{2}}+\frac{1}{b^{2}}} \\
& \geqslant \frac{2 a^{2} b^{2}}{a^{2}+b^{2}}
\end{aligned}
$$

等号当 $r_{1}=r_{2}$ 时 $\left(\theta=-\frac{\pi}{4}\right)$ 取得.

因此所求的最小值为 $\frac{2 a^{2} b^{2}}{a^{2}+b^{2}}$.

## 第 682 题 萌萌的参数方程

已知 $M N$ 是过椭圆 $\frac{x^{2}}{9}+\frac{y^{2}}{5}=1$ 的左焦点 $F$ 的直线 ( $M, N$ 在椭圆上), $A(1,0)$是椭圆长轴上的一定点. 直线 $M A, N A$ 分别交椭圆于 $P, Q$ 两点, 求证: 直线 $P Q$ 与直线 $M N$ 的斜率之比为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-144.jpg?height=262&width=311&top_left_y=455&top_left_x=1412)

解析 解法一 设 $M\left(x_{1}, y_{1}\right), N\left(x_{2}, y_{2}\right), P\left(x_{3}, y_{3}\right), Q\left(x_{4}, y_{4}\right)$.

由 $M, F, N$ 三点共线, 有

$$
\frac{y_{1}}{x_{1}+2}=\frac{y_{2}}{x_{2}+2}
$$

化简得

$$
x_{1} y_{2}-x_{2} y_{1}=2\left(y_{1}-y_{2}\right)
$$

直线 $M A$ 的方程为 $x=\frac{x_{1}-1}{y_{1}} y+1$, 代人椭圆方程得

$$
\frac{5\left(x_{1}-1\right)^{2}+9 y_{1}^{2}}{y_{1}^{2}} \cdot y^{2}+\frac{10\left(x_{1}-1\right)}{y_{1}} \cdot y-40=0,
$$

将 $9 y_{1}^{2}=45-5 x_{1}^{2}$ 代人,有

$$
\frac{5-x_{1}}{y_{1}^{2}} \cdot y^{2}+\frac{x_{1}-1}{y_{1}} \cdot y-4=0
$$

从而

$$
y_{1} \cdot y_{3}=\frac{4 y_{1}^{2}}{x_{1}-5}
$$

即

$$
y_{3}=\frac{4 y_{1}}{x_{1}-5}
$$

将 $y_{3}$ 代人直线 $M A$ 的方程, 有

$$
x_{3}=\frac{5 x_{1}-9}{x_{1}-5}
$$

同理可得

$$
x_{4}=\frac{5 x_{2}-9}{x_{2}-5}, y_{4}=\frac{4 y_{2}}{x_{2}-5}
$$

因此直线 $P Q$ 的斜率为

$$
\frac{\frac{4 y_{1}}{x_{1}-5}-\frac{4 y_{2}}{x_{2}-5}}{\frac{5 x_{1}-9}{x_{1}-5}-\frac{5 x_{2}-9}{x_{2}-5}}=\frac{-20\left(y_{1}-y_{2}\right)-4\left(x_{1} y_{2}-x_{2} y_{1}\right)}{-16\left(x_{1}-x_{2}\right)}
$$

将(1)式代人, 即得直线 $P Q$ 与直线 $M N$ 的斜率之比为 $\frac{7}{4}$, 是定值.

解法二 首先对椭圆的参数方程, 有以下常用引理.

设点 $A(a \cos 2 \alpha, b \sin 2 \alpha), B(a \cos 2 \beta, b \sin 2 \beta)$, 则直线 $A B$ 的方程为

$$
A B: y=-\frac{b}{a} \cdot \frac{1}{\tan (\alpha+\beta)} x+b \cdot \frac{1+\tan \alpha \cdot \tan \beta}{\tan \alpha+\tan \beta},
$$

特别的, 若直线 $A B$ 过点 $(m, 0)$, 那么有

$$
\tan \alpha \cdot \tan \beta=\frac{m-a}{m+a}
$$

设 $M, N, P, Q$ 四点对应的参数分别为 $2 \theta_{1}, 2 \theta_{2}, 2 \theta_{3}, 2 \theta_{4}$, 则由引理可得

$$
\tan \theta_{1} \cdot \tan \theta_{3}=\tan \theta_{2} \cdot \tan \theta_{4}=-\frac{1}{2}, \tan \theta_{1} \cdot \tan \theta_{2}=-5
$$

从而

$$
\tan \theta_{2}=-\frac{5}{\tan \theta_{1}}, \tan \theta_{3}=-\frac{1}{2 \tan \theta_{1}}, \tan \theta_{4}=\frac{\tan \theta_{1}}{10}
$$

因此所求斜率之比为

$$
\frac{\tan \left(\theta_{1}+\theta_{2}\right)}{\tan \left(\theta_{3}+\theta_{4}\right)}=\frac{\tan \theta_{1}+\tan \theta_{2}}{1-\tan \theta_{1} \cdot \tan \theta_{2}} \cdot \frac{1-\tan \theta_{3} \cdot \tan \theta_{4}}{\tan \theta_{3}+\tan \theta_{4}}=\frac{7}{4}
$$

为定值, 原命题得证.

参数方程解法中的引理是在利用椭圆的参数方程解题时经常用到的结论, 可以有效地帮助我们处理横截距和斜率问题.

## 第 683 题 顶点弦代换

已知 $A, B$ 分别是椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的上顶点和下顶点, $F$ 为椭圆 $E$ 的右焦点. 过 $F$ 作直线 $l$ 分别与椭圆交于 $C, D$, 与 $y$ 轴交于点 $P$. 直线 $A C$ 和 $B D$ 交于点 $Q$, 求证: $\overrightarrow{O P} \cdot \overrightarrow{O Q}$ 为定值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-145.jpg?height=440&width=407&top_left_y=1297&top_left_x=1439)

解析 设直线 $l$ 的方程为 $x=t y+c$, 则点 $P$ 的坐标为 $\left(0,-\frac{c}{t}\right)$. 设点 $Q$ 的坐标为 $(m, n)$, 则

$$
\overrightarrow{O P} \cdot \overrightarrow{O Q}=-c \cdot \frac{n}{t}
$$

于是只需求出 $n$ 的值.

设 $D\left(x_{1}, y_{1}\right), C\left(x_{2}, y_{2}\right)$, 根据题意, 有

$$
\left\{\begin{array}{l}
\frac{y_{1}+b}{x_{1}}=\frac{n+b}{m} \\
\frac{y_{2}-b}{x_{2}}=\frac{n-b}{m}
\end{array}\right.
$$

于是

$$
\frac{n+b}{n-b}=\frac{x_{2}\left(y_{1}+b\right)}{x_{1}\left(y_{2}-b\right)}
$$

利用顶点弦代换, 将椭圆方程改写为

$$
x^{2}=\frac{a^{2}}{b^{2}}(b+y)(b-y)
$$

从而有

$$
\left(\frac{n+b}{n-b}\right)^{2}=\frac{x_{2}^{2}\left(b+y_{1}\right)^{2}}{x_{1}^{2}\left(b-y_{2}\right)^{2}}=\frac{\left(b+y_{1}\right)\left(b+y_{2}\right)}{\left(b-y_{1}\right)\left(b-y_{2}\right)}=\frac{b^{2}+b\left(y_{1}+y_{2}\right)+y_{1} y_{2}}{b^{2}-b\left(y_{1}+y_{2}\right)+y_{1} y_{2}}
$$

联立直线 $l$ 与椭圆 $E$ 的方程, 整理得

$$
\left(t^{2}+\frac{a^{2}}{b^{2}}\right) y^{2}+2 t c y-b^{2}=0
$$

从而

$$
\left(\frac{n+b}{n-b}\right)^{2}=\frac{b^{2} t^{2}+a^{2}-2 t b c-b^{2}}{b^{2} t^{2}+a^{2}+2 t b c-b^{2}}=\left(\frac{b t-c}{b t+c}\right)^{2}
$$

又 $\frac{n+b}{n-b}$ 与 $x_{1} x_{2}$ 异号, 也即与

$$
\left(t y_{1}+c\right)\left(t y_{2}+c\right)=t^{2} y_{1} y_{2}+t c\left(y_{1}+y_{2}\right)+c^{2}=\frac{a^{2}(c-b t)(c+b t)}{b^{2} t^{2}+a^{2}}
$$

异号, 因此

$$
\frac{n+b}{n-b}=\frac{b t-c}{b t+c}
$$

解得 $n=-\frac{b^{2} t}{c}$, 因此

$$
\overrightarrow{O P} \cdot \overrightarrow{O Q}=-c \cdot \frac{n}{t}=b^{2}
$$

为定值. 因此原命题得证.

## 第 684 题 定比点差法

设 $F_{1}, F_{2}$ 分别为植圆 $\frac{x^{2}}{3}+y^{2}=1$ 的左, 右焦点, 点 $A, B$ 在植圆上, 且 $\overrightarrow{F_{1} A}=5 \overrightarrow{F_{2} B}$, 则点 $A$ 的坐标是

解析 $(0, \pm 1)$.

如图, 延长 $A F_{1}$ 交椭圆于点 $C$, 则 $\overrightarrow{A F_{1}}=5 \overrightarrow{F_{1} C}$.

设 $A\left(x_{1}, y_{1}\right), C\left(x_{2}, y_{2}\right)$, 则根据定比分点坐标公式得点 $F_{1}$ 的坐标

$$
\left(\frac{x_{1}+5 x_{2}}{6}, \frac{y_{1}+5 y_{2}}{6}\right)=(-\sqrt{2}, 0)
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-146.jpg?height=256&width=382&top_left_y=1587&top_left_x=1388)

从而

$$
x_{1}+5 x_{2}=-6 \sqrt{2}, y_{1}+5 y_{2}=0 .
$$

另一方面,由

$$
\frac{x_{1}^{2}}{3}+y_{1}^{2}=1, \frac{25 x_{2}^{2}}{3}+25 y_{2}^{2}=25
$$

相减可得

$$
\frac{\left(x_{1}+5 x_{2}\right)\left(x_{1}-5 x_{2}\right)}{3}+\left(y_{1}+5 y_{2}\right)\left(y_{1}-5 y_{2}\right)=-24
$$

从而可得

$$
x_{1}-5 x_{2}=6 \sqrt{2}
$$

因此以上两式相加, 可得 $x_{1}=0$, 进而可得 $A=(0, \pm 1)$.

## 第 685 题 “定比点差法”证定点问题

已知椭圆 $\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$, 点 $P(4,0)$, 过点 $P$ 作椭圆的割线 $P A B$, 点 $C$为点 $B$ 关于 $x$ 轴的对称点. 求证: 直线 $A C$ 恒过定点.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-147.jpg?height=265&width=495&top_left_y=447&top_left_x=1348)

解析 因为 $A, B, P$ 三点共线, $A, C, M$ 三点也共线, 且 $A, B, C$ 三点都在椭圆上, 我们用定比点差法来解决这个问题.

设 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 则 $C\left(x_{2},-y_{2}\right)$, 设 $A C$ 与 $x$ 轴的交点为 $M(m, 0), \overrightarrow{A P}=\lambda \overrightarrow{P B}, \overrightarrow{A M}=\mu \overrightarrow{M C}$, 则

$$
P\left(\frac{x_{1}+\lambda x_{2}}{1+\lambda}, \frac{y_{1}+\lambda y_{2}}{1+\lambda}\right), M\left(\frac{x_{1}+\mu x_{2}}{1+\mu}, \frac{y_{1}-\mu y_{2}}{1+\mu}\right)
$$

于是有

$$
\begin{gathered}
x_{1}+\lambda x_{2}=4(1+\lambda), y_{1}+\lambda y_{2}=0 \\
x_{1}+\mu x_{2}=m(1+\mu), y_{1}-\mu y_{2}=0
\end{gathered}
$$

由点 $A, B$ 在椭圆上得

$$
\left\{\begin{array}{l}
\frac{x_{1}^{2}}{4}+\frac{y_{1}^{2}}{3}=1 \\
\frac{\mu^{2} x_{2}^{2}}{4}+\frac{\mu^{2} y_{2}^{2}}{3}=\mu^{2}
\end{array}\right.
$$

两式相减得

$$
\frac{\left(x_{1}+\mu x_{2}\right)\left(x_{1}-\mu x_{2}\right)}{4}+\frac{\left(y_{1}+\mu y_{2}\right)\left(y_{1}-\mu y_{2}\right)}{3}=1-\mu^{2} \quad \text { (3). }
$$

将(2)式代人 (3)式得

$$
x_{1}-\mu x_{2}=\frac{4(1-\mu)}{m}
$$

由(1)(2)得 $\mu=-\lambda$,代人(4)式得

$$
x_{1}+\lambda x_{2}=\frac{4(1+\lambda)}{m}
$$

与(1)式对比得 $m=1$, 即直线 $A C$ 恒过定点 $(1,0)$.

## 第 686 题 定比点差法

过点 $P(3,1)$ 的动直线 $l$ 与双曲线 $C: \frac{x^{2}}{3}-y^{2}=1$ 的左、右两支分别交于点 $A, B$, 在线段 $A B$ 上取不同于 $A, B$ 的点 $Q$, 满足 $|A P| \cdot|Q B|=|A Q| \cdot|P B|$, 求证: 点 $Q$ 总在某条定直线上.

解析 由于 $|A P| \cdot|Q B|=|A Q| \cdot|P B|$, 不妨设

$$
\overrightarrow{A P}=\lambda \overrightarrow{P B}, \overrightarrow{A Q}=-\lambda \overrightarrow{Q B}
$$

又 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 则利用定比点差法, 有

$$
P\left(\frac{x_{1}+\lambda x_{2}}{1+\lambda}, \frac{y_{1}+\lambda y_{2}}{1+\lambda}\right), Q\left(\frac{x_{1}-\lambda x_{2}}{1-\lambda}, \frac{y_{1}-\lambda y_{2}}{1-\lambda}\right)
$$

于是由

$$
\frac{x_{1}^{2}}{3}-y_{1}^{2}=1, \frac{\lambda^{2} x_{2}^{2}}{3}-\lambda^{2} y_{2}^{2}=\lambda^{2}
$$

两式相减得

$$
\frac{\left(x_{1}+\lambda x_{2}\right)\left(x_{1}-\lambda x_{2}\right)}{3}-\left(y_{1}+\lambda y_{2}\right)\left(y_{1}-\lambda y_{2}\right)=1-\lambda^{2},
$$

整理即得

$$
\frac{1}{3} \cdot \frac{x_{1}+\lambda x_{2}}{1+\lambda} \cdot \frac{x_{1}-\lambda x_{2}}{1-\lambda}-\frac{y_{1}+\lambda y_{2}}{1+\lambda} \cdot \frac{y_{1}-\lambda y_{2}}{1-\lambda}=1
$$

从而

$$
\frac{x_{1}-\lambda x_{2}}{1-\lambda}-\frac{y_{1}-\lambda y_{2}}{1-\lambda}-1=0
$$

因此点 $Q$ 在定直线 $x-y-1=0$ 上.

## 第 687 题 交点曲线系

已知圆 $A: x^{2}+y^{2}-6 y+m=0$ 和直线 $l: x+2 y-3=0$ 交于 $P, Q$ 两点, 且以 $P Q$ 为直径的圆 $M$ 过原点,求 $m$ 的值.

画出示意图如图.

取圆 $A$ 与直线 $l$ 的交点曲线系

$$
\Gamma(\lambda): x^{2}+y^{2}-6 y+m+\lambda(x+2 y-3)=0,
$$

其中 $\lambda$ 为参数.

整理上述方程得

$$
\Gamma(\lambda):\left(x+\frac{\lambda}{2}\right)^{2}+(y-3+\lambda)^{2}+m-3 \lambda-\frac{1}{4} \lambda^{2}-(3-\lambda)^{2}=0
$$

我们想使 $\Gamma(\lambda)$ 表示以 $P Q$ 为直径的圆,只需要圆心在直线 $x+2 y-3=0$ 上,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-148.jpg?height=407&width=396&top_left_y=1233&top_left_x=1369)
因此

$$
-\frac{\lambda}{2}+2 \cdot(3-\lambda)-3=0
$$

解得 $\lambda=\frac{6}{5}$.

又圆 $\Gamma\left(\frac{6}{5}\right)$ 经过原点 $(0,0)$, 所以

$$
m-3 \lambda=0,
$$

进而可得 $m=\frac{18}{5}$.

在本题中, 圆 $A$, 直线 $l$ 与圆 $M$ 三者交于点 $P, Q$, 因此可以考虑利用交点曲线系简化问题.

## 第 688 题 过三点的圆

已知抛物线 $y=x^{2}+b x+c$ 与坐标轴交于 $A, B, C$ 三点. 求证: $\triangle A B C$ 的外接圆恒过一定点 $P$.

## 解析 解法一

考虑抛物线 $F: x^{2}+b x-y+c=0$ 与平行曲线 $G: y(y-c)=0$ 形成的交点曲线系

$$
x^{2}+b x-y+c+\lambda y(y-c)=0
$$

即

$$
x^{2}+\lambda y^{2}+b x-(1+c \lambda) y+c=0
$$

其中 $\lambda$ 为参数. 当 $\lambda=1$ 时, 该方程即 $\triangle A B C$ 的外接圆方程

$$
x^{2}+y^{2}+b x-(1+c) y+c=0
$$

也即

$$
x \cdot b+(1-y) c+x^{2}+y^{2}-y=0
$$

恒过定点 $P(0,1)$.

解法二 设 $\triangle A B C$ 的外接圆交 $y$ 轴于另一点 $D$, 记 $A\left(x_{1}, 0\right), B\left(x_{2}, 0\right), C(0, c), D\left(0, y_{0}\right)$, 则根据圆幂定理有

$$
\overrightarrow{O A} \cdot \overrightarrow{O B}=\overrightarrow{O C} \cdot \overrightarrow{O D}
$$

即

$$
x_{1} \cdot x_{2}=c \cdot y_{0},
$$

因此 $y_{0}=1$ 为定值, 也即 $\triangle A B C$ 的外接圆恒过定点 $P(0,1)$.

## 第 689 题 双二次纠缠

当 $m, a, b$ 满足什么关系时, 椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 和抛物线 $y=x^{2}+m$ 有四个不同的交点? 并证明这四个交点共圆.

解析 联立椭圆方程与抛物线方程, 可得

$$
b^{2}(y-m)+a^{2} y^{2}=a^{2} b^{2}
$$

因此题意即关于 $y$ 的方程

$$
a^{2} y^{2}+b^{2} y-b^{2} m-a^{2} b^{2}=0
$$

有两个大于 $m$ 的解,即

$$
\left\{\begin{array}{l}
a^{2} m^{2}-a^{2} b^{2}>0 \\
-\frac{b^{2}}{2 a^{2}}>m \\
\Delta=b^{4}+4 a^{2}\left(b^{2} m+a^{2} b^{2}\right)>0
\end{array}\right.
$$

化简得 $b<2 a^{2}$, 且 $-a^{2}-\frac{b^{2}}{4 a^{2}}<m<-b$.

考虑椭圆与抛物线的交点曲线

$$
\left(b^{2} x^{2}+a^{2} y^{2}-a^{2} b^{2}\right)+\left(a^{2}-b^{2}\right)\left(x^{2}-y+m\right)=0,
$$

即

$$
x^{2}+y^{2}-\left(1-\frac{b^{2}}{a^{2}}\right) y-b^{2}+\left(1-\frac{b^{2}}{a^{2}}\right) m=0
$$

该方程表示的曲线为圆,因此椭圆与抛物线的四个交点共圆.
事实上,四个交点构成的四边形为等腰梯形,等腰梯形一定有外接圆.

## 第 690 题 祖晅原理

关于曲线 $C: x^{4}+y^{2}=1$ 的下列命题:

(1)曲线 $C$ 关于原点对称;

(2)曲线 $C$ 关于直线 $y=x$ 对称;

(3)曲线 $C$ 所围成的面积小于 $\pi$;

(4)曲线 $C$ 所围成的面积大于 $\pi$.

其中的真命题是 . (写出所有真命题的编号)

解析 (1)(4).

先考虑对称性, 再比较面积.

(1)由于对曲线 $C$ 上任意一点 $(x, y)$ 均有

$$
(-x)^{4}+(-y)^{2}=x^{4}+y^{2},
$$

于是曲线关于原点对称;

(2)由于并不是对曲线 $C$ 上任意一点 $(x, y)$ 均有

$$
y^{4}+x^{2}=1,
$$

如 $\left(\left(\frac{1}{2}\right)^{\frac{1}{4}},\left(\frac{1}{2}\right)^{\frac{1}{2}}\right)$, 于是曲线并不关于直线 $y=x$ 对称;

命题(3)(4)即比较曲线 $C$ 与圆 $x^{2}+y^{2}=1$ 围成的区域面积. 由于两者均分布在

$$
-1 \leqslant y \leqslant 1
$$

的区域内, 且当 $y= \pm 1$ 时,两条曲线对应的横坐标的值均为 0 ,因此可以利用祖脽原理将平行区域的面积比较问题转化为纵坐标一致的截线段长度的比较问题.

事实上,任何一条平行于 $x$ 轴的直线

$$
y=m,-1<m<1
$$

被两条曲线截得的线段长分别为 $2 \sqrt[4]{1-m^{2}}$ (曲线 $C$ ) 以及 $2 \sqrt{1-m^{2}}$ (圆),而前者任何时候都大于后者 (因为小于 1 的整数的算术平方根比自身大),因此根据祖㫿原理的推论可得曲线 $C$ 所围成的面积大于圆所围成的面积

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-150.jpg?height=325&width=496&top_left_y=1565&top_left_x=1256)

$\pi$, 如图 .

## 第 691 题 卡西尼卵形线

曲线 $C$ 是平面内与两个定点 $F_{1}(-1,0)$ 和 $F_{2}(1,0)$ 的距离之积等于常数 $a^{2}(a>1)$ 的点的轨迹. 给出下列三个结论:

(1) 曲线 $C$ 过坐标原点;

(2)曲线 $C$ 关于坐标原点对称;

(3)若点 $P$ 在曲线 $C$ 上, 则 $\triangle F_{1} P F_{2}$ 的面积不大于 $\frac{1}{2} a^{2}$.

其中所有正确结论的序号是 $\qquad$ .
解析 (2)(3).

我们很熟悉的问题是: “曲线 $C$ 是平面内与两个定点 $F_{1}(-1,0)$ 和 $F_{2}(1,0)$ 的距离之比等于常数 $\lambda(\lambda>$ 1) 的点的轨迹…." (见阿波罗尼斯圆). 研究这个问题所用的方法为用直译法写出轨迹方程, 然后通过研究代数方程来探索轨迹的几何性质.

理解题意后可以写出轨迹方程

$$
\sqrt{(x+1)^{2}+y^{2}} \cdot \sqrt{(x-1)^{2}+y^{2}}=a^{2}
$$

据此考查三个结论:

(1)曲线 $C$ 过坐标原点, 即原点坐标 $(0,0)$ 是方程的解, 显然不正确;

(2)曲线 $C$ 关于坐标原点对称, 即若 $(x, y) \in C$, 则 $(-x,-y) \in C$, 显然正确;

(3)选用合适的面积公式

$$
S_{\triangle F_{1} P F_{2}}=\frac{1}{2} \cdot\left|P F_{1}\right| \cdot\left|P F_{2}\right| \cdot \sin \angle F_{1} P F_{2} \leqslant \frac{1}{2} a^{2}
$$

因此(3)正确.

结论(3)可以引发我们进一步探索曲线 $C$ 的有界性.

有界性一 根据结论(3), 曲线 $C$ 被限制在直线 $y=\frac{1}{2} a^{2}$ 和 $y=-\frac{1}{2} a^{2}$ 之间;

有界性二 在 $x$ 轴上可以找到两点 $A(t, 0)(t>0)$ 和 $B(-t, 0)$ 使得 $(t-1)(t+1)=a^{2}$, 即

$$
t=\sqrt{a^{2}+1}
$$

容易证明曲线 $C$ 被限制在直线 $x=t$ 和 $x=-t$ 之间.

在此基础上结合结论(2)进一步思考曲线 $C$ 的封闭性.

因为曲线 $C$ 关于 $x$ 轴和 $y$ 轴对称, 因此我们只需要考虑曲线 $C$ 在第一象限中的情况.

因为 $a>1$, 所以在 $y$ 轴上可以找到两点 $E(0, s)$ 和 $F(0,-s)$ 满足

$$
\sqrt{1^{2}+s^{2}} \cdot \sqrt{1^{2}+s^{2}}=a^{2},
$$

其中 $s>0$.

考虑曲线在第一象限内的情况, 当 $x$ 的值给定时,

$$
\sqrt{(x+1)^{2}+y^{2}} \cdot \sqrt{(x-1)^{2}+y^{2}}
$$

关于 $y$ 单调递增且最小值为

$$
\sqrt{(x+1)^{2}+0^{2}} \cdot \sqrt{(x-1)^{2}+0^{2}}=\left|1-x^{2}\right|<a^{2}
$$

因此每个 $x$ 有且只有一个 $y$ 与之对应, 曲线 $C$ 在第一象限内可以看作是连接 $A$ 和 $E$ 的函数图象.

综上,就证明了曲线 $C$ 是一条封闭曲线.

事实上,当 $a>1, a=1, a<1$ 时, 曲线 $C$ 如图 1,2,3 所示:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-151.jpg?height=327&width=357&top_left_y=1809&top_left_x=454)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-151.jpg?height=327&width=357&top_left_y=1809&top_left_x=846)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-151.jpg?height=329&width=357&top_left_y=1808&top_left_x=1238)

图 3

平面上到两个定点 (距离为 $2 c)$ 的距离之积为定值 $\left(a^{2}\right)$ 的点的轨迹称为“卡西尼卵形线”, 这两个定点叫作焦点,随着 $a$ 与 $c$ 的大小关系变化卵形线的形状也会发生变化.

## 第 692 题 合理消参求轨迹

从 $O$ 点发出两条射线 $l_{1}, l_{2}$, 已知直线 $l$ 分别交 $l_{1}, l_{2}$ 于 $A, B$ 两点, 且 $S_{\triangle O A B}=c$ ( $c$ 为定值), 记 $A B$的中点为 $D$, 点 $D$ 随着 $A, B$ 的运动构成轨迹 $\Gamma$. 求证:

(1) 点 $D$ 的轨迹 $\Gamma$ 关于 $\angle A O B$ 的角平分线反射对称;

(2) 轨迹 $\Gamma$ 为双曲线.

解析 $(1)$ 根据条件的对称性即得.

(2) 以 $\angle A O B$ 的角平分线所在直线为 $x$ 轴建立如图所示的直角坐标系.

设 $\angle A O x=\angle B O x=\alpha, O A=a, O E=b, D(x, y)$,

则

$$
S_{\triangle O A B}=\frac{1}{2} a b \sin 2 \alpha=c
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-152.jpg?height=346&width=305&top_left_y=710&top_left_x=1458)

所以 $a b=\frac{2 c}{\sin 2 \alpha}$.

因为 $A(a \cos \alpha, a \sin \alpha), B(b \cos \alpha,-b \sin \alpha)$, 所以

$$
\left\{\begin{array}{l}
x=\frac{a \cos \alpha+b \cos \alpha}{2} \\
y=\frac{a \sin \alpha-b \sin \alpha}{2}
\end{array}\right.
$$

所以

$$
\left\{\begin{array}{l}
\frac{x}{\cos \alpha}=\frac{a+b}{2} \\
\frac{y}{\sin \alpha}=\frac{a-b}{2}
\end{array}\right.
$$

两式平方相减得 $\frac{x^{2}}{\cos ^{2} \alpha}-\frac{y^{2}}{\sin ^{2} \alpha}=a b=\frac{2 c}{\sin 2 \alpha}$,

所以, 点 $D$ 的轨迹为双曲线 (的一支), 且关于 $\angle A O B$ 的角平分线反射对称.

## 第 693 题 狡兔三窟

如图 1, 设 $F_{1}, F_{2}$ 是椭圆 $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 的焦点, 椭圆的弦 $A B$过焦点 $F_{1}$, 求 $\triangle A B F_{2}$ 面积的最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-152.jpg?height=264&width=439&top_left_y=2005&top_left_x=1285)

图 1

## 解析 解法一

考虑将椭圆变成圆解决问题, 如图 2 所示, 将所有点的纵坐标变为原来的 $\frac{a}{b}$ 倍, 则

$$
S_{\triangle A B F_{2}}=\frac{b}{a} \cdot S_{\triangle A^{\prime} B^{\prime} F_{2}}
$$

于是只需要求圆中 $\triangle A^{\prime} B^{\prime} F_{2}$ 的面积的最大值.

连结 $O A^{\prime}, O B^{\prime}$, 取 $A^{\prime} B^{\prime}$ 的中点 $M$, 设 $O M=d$, 则 $d \in(0, c]$, 其中 $c=$ $\sqrt{a^{2}-b^{2}}$, 且

$$
S_{\triangle A^{\prime} B^{\prime} F_{2}}=2 S_{\triangle A^{\prime} B^{\prime} O}=2 \cdot \sqrt{d^{2}\left(a^{2}-d^{2}\right)},
$$

若 $c \geqslant \frac{a}{\sqrt{2}}$, 即 $e \geqslant \frac{\sqrt{2}}{2}$, 则

$$
S_{\triangle A B F_{2}} \leqslant \frac{b}{a} \cdot 2 \cdot \frac{\left(a^{2}-d^{2}\right)+d^{2}}{2}=a b
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-153.jpg?height=363&width=372&top_left_y=288&top_left_x=1505)

图 2

若 $c<\frac{a}{\sqrt{2}}$, 即 $e<\frac{\sqrt{2}}{2}$, 则

$$
S_{\triangle A B F_{2}} \leqslant \frac{b}{a} \cdot 2 \cdot \sqrt{\left(a^{2}-c^{2}\right) c^{2}}=\frac{2 b^{2} c}{a}=\frac{2 b^{2} \sqrt{a^{2}-b^{2}}}{a}
$$

综上所述, 当 $a \geqslant \sqrt{2} b$ 时,所求面积的最大值为 $a b$; 当 $a<\sqrt{2} b$ 时, 所求面积的最大值为 $\frac{2 b^{2} \sqrt{a^{2}-b^{2}}}{a}$.

解法二 设 $A F_{1}=m, B F_{1}=n$, 则由椭圆的性质可得

$$
\frac{1}{m}+\frac{1}{n}=\frac{2 a}{b^{2}}
$$

于是

$$
m n=\frac{b^{2}}{2 a} \cdot A B
$$

根据海伦公式, 有

$$
\begin{aligned}
S_{\triangle A B F_{2}} & =\sqrt{2 a \cdot(2 a-A B) \cdot\left(2 a-B F_{2}\right) \cdot\left(2 a-A F_{2}\right)} \\
& =\sqrt{2 a(2 a-A B) \cdot m n} \\
& =b \cdot \sqrt{(2 a-A B) \cdot A B}
\end{aligned}
$$

当椭圆的通径 $\frac{2 b^{2}}{a} \leqslant a$, 即 $a \geqslant \sqrt{2} b$ 时, $S_{\triangle A B F_{2}} \leqslant a b$, 当 $A B=a$ 时面积有最大值;

当 $a<\sqrt{2} b$ 时, 当 $A B=\frac{2 b^{2}}{a}$ 时,面积取到最大值 $\frac{2 b^{2} \sqrt{a^{2}-b^{2}}}{a}$.

解法三 设 $A B$ 的倾斜角为 $\theta$, 则

$$
A B=\frac{2 a b^{2}}{b^{2}+c^{2} \sin ^{2} \theta}
$$

于是

$$
S_{\triangle A B F_{2}}=\frac{1}{2} \sin \theta \cdot 2 c \cdot \frac{2 a b^{2}}{b^{2}+c^{2} \sin ^{2} \theta}=\frac{2 a b^{2} c}{\frac{b^{2}}{\sin \theta}+c^{2} \sin \theta}
$$

当 $\frac{b}{c} \leqslant 1$, 即 $a \geqslant \sqrt{2} b$ 时, 面积的最大值为 $\frac{2 a b^{2} c}{2 b c}=a b ;$

当 $a<\sqrt{2} b$ 时, 当 $\sin \theta=1$ 时, 面积的最大值为 $\frac{2 b^{2} c}{a}$.

## 第 694 题 仿射变换

如图 1, 已知 $A, B, C$ 是椭圆 $E: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$ 上的三个定点, $O$ 为坐标原点, 且直线 $O C$ 平分弦 $A B . P$ 为椭圆 $E$ 上的动点, 直线 $P A$, $P B$ 分别交直线 $O C$ 于点 $M, N, \frac{|O M| \cdot|O N|}{|O C|^{2}}$ 是否为定值? 若为定值, 求出该定值并证明; 若不为定值, 请说明理由.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-154.jpg?height=264&width=447&top_left_y=435&top_left_x=1281)

图 1

解析 注意到 $O, M, N, C$ 四点共线, 因此在伸缩变换 $x=x^{\prime}, y=\frac{b}{a} y^{\prime} 下, \frac{|O M| \cdot|O N|}{|O C|^{2}}$ 的值不会改变.因此只需要求出在圆 $x^{\prime 2}+y^{\prime 2}=a^{2}$ 中对应的值即可.

由于圆的对称性, 可以旋转图形使得直线 $O C^{\prime}$ 与 $x$ 轴重合, 如图 2 所示.

设 $A^{\prime}\left(x_{1}, y_{1}\right), B^{\prime}\left(x_{1},-y_{1}\right), P^{\prime}\left(x_{2}, y_{2}\right)$, 则

$$
\begin{aligned}
\frac{\left|O M^{\prime}\right| \cdot\left|O N^{\prime}\right|}{\left|O C^{\prime}\right|^{2}} & =\left|\frac{\frac{x_{1} y_{2}-x_{2} y_{1}}{y_{2}-y_{1}} \cdot \frac{x_{1} y_{2}+x_{2} y_{1}}{y_{2}+y_{1}}}{a^{2}}\right| \\
& =\left|\frac{\left(a^{2}-y_{1}^{2}\right) y_{2}^{2}-\left(a^{2}-y_{2}^{2}\right) y_{1}^{2}}{a^{2}\left(y_{2}^{2}-y_{1}^{2}\right)}\right| \\
& =1
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-154.jpg?height=317&width=412&top_left_y=899&top_left_x=1353)

图 2

为定值. 因此在原问题中, $\frac{|O M| \cdot|O N|}{|O C|^{2}}$ 为定值 1 .

## 第 695 题 化扁为圆

长为 3 的线段 $A B$ 的两个端点 $A, B$ 分别在 $x$ 轴, $y$ 轴上移动, 点 $P$ 在直线 $A B$ 上且满足 $\overrightarrow{B P}=$ $2 \overrightarrow{P A}$.

(1)求点 $P$ 的轨迹方程;

(2) 记点 $P$ 轨迹为曲线 $C$, 过点 $Q(2,1)$ 任作直线 $l$ 交曲线 $C$ 于 $M, N$ 两点, 过点 $M$ 作斜率为 $-\frac{1}{2}$ 的直线 $l^{\prime}$ 交曲线 $C$ 于另一点 $R$, 求证: 直线 $N R$ 与直线 $O Q$ 的交点为定点 ( $O$ 为坐标原点), 并求出该定点.

解析 (1) 设 $P(x, y)$, 则 $A\left(\frac{3}{2} x, 0\right), B(0,3 y)$, 于是由 $|A B|=3$ 可得

$$
\left(\frac{3}{2} x\right)^{2}+(3 y)^{2}=9
$$

即 $\frac{x^{2}}{4}+y^{2}=1$.

(2)利用仿射变换 $\left\{\begin{array}{l}x^{\prime}=x, \\ y^{\prime}=2 y^{\prime}\end{array}\right.$ 将椭圆 $E: \frac{x^{2}}{4}+y^{2}=1$ 变为圆 $x^{\prime 2}+y^{\prime 2}=4, Q^{\prime}(2,2)$, $M^{\prime} R^{\prime}$ 的斜率为 -1 , 设直线 $N^{\prime} R^{\prime}$ 与直线 $O Q^{\prime}$ 的交点为 $T^{\prime}$, 把问题转化到圆中加以解决, 如图.

连结 $O R^{\prime}, O N^{\prime}, O M^{\prime}, R^{\prime} Q^{\prime}, M^{\prime} T^{\prime}$. 由于 $O Q^{\prime}$ 的斜率为 $1, R^{\prime} M^{\prime}$ 的斜率为 -1 , 于是 $O Q^{\prime}$ 平分弧 $R^{\prime} M^{\prime}$, 进而可得

$$
\angle R^{\prime} O Q^{\prime}=\angle T^{\prime} O M^{\prime}=\angle R^{\prime} N^{\prime} M^{\prime}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-154.jpg?height=330&width=330&top_left_y=2223&top_left_x=1438)

## 高考数学满分学霸的解题笔记(一千零一踣)

于是 $O, R^{\prime}, Q^{\prime}, N^{\prime}$ 四点共圆, $O, T^{\prime}, M^{\prime}, N^{\prime}$ 四点共圆, 有

$$
\angle R^{\prime} Q^{\prime} O=\angle O N^{\prime} R^{\prime}=\angle O M^{\prime} T^{\prime}=\angle O R^{\prime} T^{\prime}
$$

从而 $\triangle O T^{\prime} R^{\prime}$ 与 $\triangle O R^{\prime} Q^{\prime}$ 相似, 有

$$
\left|O T^{\prime}\right| \cdot\left|O Q^{\prime}\right|=\left|O R^{\prime}\right|^{2}=4,
$$

因此 $\left|O T^{\prime}\right|$ 为定值 $\sqrt{2}, T^{\prime}$ 为定点 $(1,1)$. 转化到原坐标, 所求定点 $T$ 为 $\left(1, \frac{1}{2}\right)$.

## 第 696 题 仿射变换证定点

如图 1, 已知椭圆 $E: \frac{x^{2}}{4}+\frac{y^{2}}{3}=1$, 过点 $P(2,1)$ 作直线与椭圆相交于 $M, N$ 两点, 过点 $N$ 作斜率为 $-\frac{3}{2}$ 的直线与椭圆交于另一点 $Q$, 求证: 直线 $M Q$ 过定点.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-155.jpg?height=391&width=445&top_left_y=717&top_left_x=1389)

图 1

解析 如图 2, 将椭圆 $E$ 通过仿射变换 $x^{\prime}=x, y^{\prime}=\frac{2}{\sqrt{3}} y$ 变成圆

$$
E^{\prime}: x^{\prime 2}+y^{\prime 2}=4
$$

则 $P^{\prime}\left(2, \frac{2}{\sqrt{3}}\right)$, 此时 $N^{\prime} Q^{\prime}$ 的斜率为

$$
-\frac{3}{2} \cdot \frac{2}{\sqrt{3}}=-\sqrt{3}
$$

因此点 $Q^{\prime}$ 是点 $N^{\prime}$ 关于直线 $O P^{\prime}$ 的对称点.

设直线 $O P^{\prime}$ 与圆 $E^{\prime}$ 交于 $A^{\prime}, B^{\prime}$, 则直线 $M^{\prime} Q^{\prime}$ 与直线 $O P^{\prime}$ 的交点 $R^{\prime}$ 满足 $R^{\prime} P^{\prime}$ 调和分割 $A^{\prime} B^{\prime}$.

由于

$$
\left|O P^{\prime}\right|=\sqrt{2^{2}+\left(\frac{2}{\sqrt{3}}\right)^{2}}=\frac{4}{\sqrt{3}}
$$

于是 $\left|O R^{\prime}\right|=\sqrt{3}$, 结合直线 $O P^{\prime}$ 的倾斜角为 $30^{\circ}$, 可得 $R^{\prime}\left(\frac{3}{2}, \frac{\sqrt{3}}{2}\right)$, 因此直线 $M Q$ 所过的定点坐标为 $\left(\frac{3}{2}, 1\right)$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-155.jpg?height=453&width=421&top_left_y=1508&top_left_x=1439)

图 2

不利用调和分割性质, 直接计算 $\left|O R^{\prime}\right|$ 过程如下:

作辅助线如图 3 所示.

则有

$$
\angle Q^{\prime} M^{\prime} O=\frac{\pi}{2}-\angle Q^{\prime} C^{\prime} M^{\prime}=\frac{\pi}{2}-\angle Q^{\prime} N^{\prime} P=\angle A^{\prime} P^{\prime} M^{\prime}
$$

所以

$$
\triangle O R^{\prime} M^{\prime} \backsim \triangle O M^{\prime} P
$$

从而有

$$
\frac{\left|O R^{\prime}\right|}{\left|O M^{\prime}\right|}=\frac{\left|O M^{\prime}\right|}{\left|O P^{\prime}\right|}, \Rightarrow\left|O R^{\prime}\right| \cdot\left|O P^{\prime}\right|=\left|O M^{\prime}\right|^{2}
$$

思考与总结

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-155.jpg?height=353&width=374&top_left_y=2118&top_left_x=1482)

图 3

## 第 697 题 旋转加伸缩

已知坐标平面上一点 $A(0,6)$, 点 $B$ 在 $x$ 轴上运动, $C$ 是坐标平面内一点且满足 $\angle A C B=120^{\circ}, C A$ $=C B$, 则线段 $O C$ 长度的最小值是 $\qquad$
解析 $\sqrt{3}$.

解法一 如图 1.

设 $B(t, 0)$, 则 $C$ 点是 $B$ 点绕点 $A$ 按逆时针方向旋转 $\pm 30^{\circ}$, 然后把到点 $A$ 的距离变成原来的 $\frac{1}{\sqrt{3}}$ 得到的点.

因此 $C$ 点的轨迹是 $x$ 轴经过相同的变换方式得到的. $x$ 轴绕 $A$ 点按逆时针方向旋转

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-156.jpg?height=258&width=264&top_left_y=574&top_left_x=1503)

图 1 $\pm 30^{\circ}$ 得到的曲线方程为

$$
y= \pm \frac{1}{\sqrt{3}} x+6-4 \sqrt{3}
$$

因此点 $C$ 的轨迹方程为

$$
y= \pm \frac{1}{\sqrt{3}} x+2
$$

因此线段 $O C$ 的最小值为点 $O$ 到这两条直线的距离的较小值, 为 $\sqrt{3}$.

## 解法二 如图 2.

设 $B(t, 0)$, 则 $C$ 点是 $B$ 点绕点 $A$ 按逆时针方向旋转 $\pm 30^{\circ}$, 然后把到点 $A$ 的距离变成原来的 $\frac{1}{\sqrt{3}}$ 得到的点.

设 $C(x, y)$, 则有

$(x+y \mathrm{i})-6 \mathrm{i}=(t-6 \mathrm{i}) \cdot \frac{1}{\sqrt{3}}\left[\cos \left( \pm 30^{\circ}\right)+\mathrm{i} \cdot \sin \left( \pm 30^{\circ}\right)\right]=\left(\frac{t}{2} \pm \sqrt{3}\right)+\mathrm{i}\left( \pm \frac{t}{2 \sqrt{3}}-3\right)$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-156.jpg?height=267&width=267&top_left_y=1218&top_left_x=1501)

图 2

解得

$$
(x, y)=\left(\frac{1}{2} t \pm \sqrt{3}, 3 \pm \frac{1}{2 \sqrt{3}} t\right)
$$

于是点 $C$ 的轨迹方程是

$$
x \mp \sqrt{3} y \pm 2 \sqrt{3}=0
$$

因此线段 $O C$ 的最小值为点 $O$ 到这两条直线的距离的较小值, 为 $\sqrt{3}$.

## 第七章 计数与概率

## 第 698 题 和谐数

具有下列条件的 $n$ 位十进制数称为 “ $n$ 位和谐数”:

(1) 首位为 1 ;

(2) 不含除 $1,2,3$ 之外的其他数字;

(3)每个数字都至少和一个奇偶性相同的数字相邻.

则“10 位和谐数”的个数为 $\qquad$个.

## 解析 2014.

满足条件(2)(2)且前两位为 $11,13,31,33$ 的 $n(n \geqslant 2)$ 位十进制数个数相同, 记为 $a_{n}$; 满足条件(2)(3)且前两位为 22 的 $n$ 位十进制数的个数记为 $b_{n}$, 则所求的 “ 10 位和谐数” 的个数为 $2 a_{10}$.

以 11 开头的 $n$ 位 “和谐数”, 第三位可能为 $1,3,2$, 其中第三位为 1,3 的 “和谐数”各有 $a_{n-1}$ 个; 第三位为 2 的“和谐数”第四位仍然为 2 , 共有 $b_{n-2}$ 个, 所以有 $a_{n}=2 a_{n-1}+b_{n-2}$;

再考虑以 22 开头的 $n$ 位 “和谐数”, 第三位可能为 $1,3,2$, 其中第三位为 1,3 时第四位可以为 1,3 , 共有 $4 a_{n-2}$ 个; 第三位为 2 时, 共有 $b_{n-1}$ 个, 于是有 $b_{n}=4 a_{n-2}+b_{n-1}$.

根据题意, 有 $a_{2}=b_{2}=1, a_{3}=2, b_{3}=1$, 且有

$$
\left\{\begin{array}{l}
a_{n}=2 a_{n-1}+b_{n-2}, \\
b_{n}=4 a_{n-2}+b_{n-1},
\end{array}\right.
$$

因此

| $n$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $a_{n}$ | 1 | 2 | 5 | 11 | 27 | 67 | 167 | 411 | 1007 |
| $b_{n}$ | 1 | 1 | 5 | 13 | 33 | 77 | 185 | 453 | 1121 |

从而 $2 a_{10}=2014$ 为所求.

思考与总结

用递推的计数方式往往可以降低问题的难度.

## 第 699 题 掷䐬子游戏

游戏规则如下: 如果某次随机地投郑出手中的股子后有 2 颗股子的点数之和为 7 , 则获胜. 现在手中恰好有 2 颗骰子, 但有两种奖励 (bonus) 可以领取, 请问选择哪种奖励获胜的概率大?

奖励 $A$ :额外的 2 次投郑机会;

奖励 $B:$ 额外的 1 颗骰子.
解析 选择奖励 $A$ 获胜的概率大.

选择奖例. 1 一次郑 2 颗骰子, 那么获胜的概率为 $\frac{6}{36}=\frac{1}{6}$. 于是, 那么郑三次骰子获胜的概率为

$$
1-\left(\frac{5}{6}\right)^{3}=\frac{91}{216} \approx 0.4213
$$

选择奖刐 13 点数之和为 7 有三种可能: $1+6,2+5,3+4$. 设掷出的三个骰子点数分别为 $1,6, x$, 那么若 $x \in\{1,6\}$, 则有 6 种可能; 若 $x \notin\{1,6\}$, 则有 $\mathrm{C}_{4}^{1} \mathrm{~A}_{3}^{3}=24$ 种可能. 类似可得其他两种情况的可能数, 因此获胜的概率为

$$
\frac{3 \times(6+24)}{6^{3}}=\frac{5}{12} \approx 0.4167
$$

综上,选择奖励 $A$ 获胜的概率大.

更加有趣的问题是, 如果可以选择两次奖励(相同的奖励可以叠加)后再进行投郑,那么应该如何选择呢? 此时有三种策略: 选择两次奖励 $A$; 选择两次奖励 $B$; 以及选择一次奖励 $A$ 和一次奖励 $B$.

选择两次奖劢 $A$ 如前所述, 获胜概率为

$$
1-\left(\frac{5}{6}\right)^{5}=\frac{4651}{7776} \approx 0.5981
$$

选择两次奖仿 $B \quad$ 按和为 7 分为一对和两对计算.

一对的情形以 $1+6$ 为例, 有如下几种情况.

(1)1116、1166、1666 型,共 14 种;

(2) $116 x$ 或 $166 x$ 型,共 96 种;

(3) $16 x x$ 型,共 48 种;

(4) $16 x y$ 型, 共 96 种;

因此该情形共 $3(14+96+48+96)=762$ 种; 两对的情形共 $3 \mathrm{~A}_{4}^{4}=72$ 种;

因此获胜的概率为

$$
\frac{762+72}{6^{4}}=\frac{139}{216} \approx 0.6435
$$

选择一次奖阴 $A$ 和一次奖励 $B$ 此时获胜的概率为

$$
1-\left(\frac{7}{12}\right)^{3}=\frac{1385}{1728} \approx 0.8015
$$

因此,选择一次奖励 $A$ 和一次奖励 $B$ 获胜的概率最大.

注 选择两次奖励 $B$ 后获胜概率有一个基于几何模型的算法,简便而直观.

考虑问题的反面, 用 1-6 六种不同的颜色给正四面体的 4 个顶点分别染色, 其中不

存在任何一条棱的两个端点颜色之和为 7. 很明显, 4 个顶点总共的颜色数为 $1 、 2$ 或 3.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-158.jpg?height=253&width=243&top_left_y=1761&top_left_x=1504)

(1) 1 种颜色, 有 6 种选色方案, 1 种染色方案;

(2) 种颜色, 有 12 种选色方案, 有 14 种染色方案;

(3) 3 种颜色, 有 8 种选色方案, 有 36 种染色方案.

因此不能获胜的概率为

$$
\frac{6+12 \times 14+8 \times 36}{6^{4}}=\frac{77}{216}
$$

从而可以获胜的概率为 $\frac{139}{216}$.

## 第 700 题 圆排列

(1)一个圆环形花坛, 分为 5 个区域 (如图所示), 每个区域种植一种花卉, 有 4 种不同颜色供选,要求相邻区域种植的花卉颜色不同, 求不同的花卉种植方法数.

(2)将第 (1) 题中的区域数由 5 个替换为 $n(n \geqslant 3)$ 个, 求不同的花卉种植方法数.

(3) 将第 (2)题中的花卉颜色数由 4 个替换为 $m$ 个, 求不同的花卉种植方法数.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-159.jpg?height=249&width=249&top_left_y=449&top_left_x=1591)

解析 $(1)$ 见第 $(3)$ 小题.

(2) 见第(3)小题.

(3) 直接处理问题 (3), 对区域的总数 $n$ 使用递推方法, 设不同的花卉种植方法数为 $a_{n}$, 则有 $a_{1}=m, a_{2}=$ $m(m-1)$.

递推方法一 选定起点, 将问题看成排成一个队列, 那么不同的方案数有 $m(m-1)^{n-1}$ 种. 然后再考虑将首尾“拼接”起来, 此时如果首尾的颜色不同, 那么对应 $a_{n}$ 种方法数; 如果首尾的颜色相同, 那么对应 $a_{n-1}$ 种方法数. 这样就得到了递推公式

$$
a_{n}+a_{n-1}=m(m-1)^{n-1}, n \geqslant 3
$$

递推方法二 选定起点, 考虑起点开始的三个区域, 则对应 $n+1$ 个区域的花卉种植方法可以用两种方式得到:

一种是在 $n$ 个区域的花卉种植方法的基础上,在第一、第二个区域之间插人一种不同颜色的花卉,此时得到的 $n+1$ 个区域的花卉种植方法的开头三个区域花卉各不相同;

另一种是在 $n-1$ 个区域的花卉种植方法的基础上,将第一个区域中部插人一种不同颜色的花卉,此时得到的 $n+1$ 个区域的花卉种植方法的开头三个区域花卉为 ABA 的形式,即第一、第三区域花卉相同.

因此可以得到递推公式

$$
a_{n+1}=(m-2) a_{n}+(m-1) a_{n-1}, n \geqslant 3
$$

从两个递推公式均可推出通项公式为

$$
a_{n}=\left\{\begin{array}{l}
m, n=1, \\
(m-1) \cdot(-1)^{n}+(m-1)^{n}, n=2,3, \cdots
\end{array}\right.
$$

## 第 701 题 离散型随机变量的期望

若离散型随机变量 $X, Y$ 满足 $2 \leqslant X \leqslant 3$, 且 $X Y=1$, 则 $E(X) E(Y)$ 的取值范围为

解析 $\left[1, \frac{25}{24}\right]$.

不影响问题的本质, 考虑随机变量 $X$ 的取值为有限个的情形. 设随机变量 $X$ 的分布列为

| $X$ | $x_{1}$ | $x_{2}$ | $\cdots$ | $x_{n}$ |
| :---: | :---: | :---: | :---: | :---: |
| $p(X)$ | $p_{1}$ | $p_{2}$ | $\cdots$ | $p_{n}$ |

其中 $p_{1}+p_{2}+\cdots+p_{n}=1$ 且 $p_{1}, p_{2}, \cdots, p_{n}>0$. 那么有

$$
\begin{aligned}
E(X) E(Y) & =\left(p_{1} x_{1}+p_{2} x_{2}+\cdots+p_{n} x_{n}\right)\left(p_{1} x_{1}^{-1}+p_{2} x_{2}^{-1}+\cdots+p_{n} x_{n}^{-1}\right) \\
& \geqslant\left(x_{1} p_{1} x_{2}^{2} \cdots x_{n}^{p_{n}}\right)\left(x_{1}^{-p_{1}} x_{2}^{-p_{2}} \cdots x_{n}^{-p_{n}}\right) \\
& =1,
\end{aligned}
$$

等号当 $x_{1}=x_{2}=\cdots=x_{n}$ 时取得, 因此 $E(X) E(Y)$ 的最小值为 1 .

考虑函数 $f\left(x_{i}\right)=E(X) E(Y)(i=1,2, \cdots, n)$ 的单调性, 可得当 $x_{i} \in\{2,3\}$ 时 $E(X) E(Y)$ 取得最大值. 这是由于 $a, b, p>0$ 时, 有

$$
(p x+a)\left(\frac{p}{x}+b\right)=p b x+\frac{p a}{x}+p^{2}+a b,
$$

而对勾函数 $y=p b x+\frac{p a}{x}$ 在限制区间上的最大值必然在区间端点处取得. 假设随机变量 $X$ 中取值 2,3 对应的概率分别为 $p, q$, 其中 $p+q=1$ 且 $p, q>0$, 那么

$$
\begin{aligned}
E(X) E(Y) & =(2 p+3 q)\left(\frac{p}{2}+\frac{q}{2}\right) \\
& =\frac{p^{2}+q^{2}+\frac{13}{6} p q}{p^{2}+q^{2}+2 p q} \\
& =1+\frac{\frac{1}{6}}{\frac{p}{q}+\frac{q}{p}+2} \\
& \leqslant 1+\frac{\frac{1}{6}}{2+2} \\
& =\frac{25}{24}
\end{aligned}
$$

等号当 $p=q$ 时取得,因此 $E(X) E(Y)$ 的最大值为 $\frac{25}{24}$.

综上所述, 考虑到连续性, $E(X) E(Y)$ 的取值范围为 $\left[1, \frac{25}{24}\right]$.

思考与总结

此题即康托洛维奇不等式, 设 $p_{i}>0, i=1,2, \cdots, n$ 且 $p_{1}+p_{2}+\cdots+p_{n}=1$, 又 $0<a_{1} \leqslant a_{2} \leqslant \cdots \leqslant a_{n}$, 则

$$
\sum_{i=1}^{n}\left(p_{i} a_{i}\right) \cdot \sum_{i=1}^{n} \frac{p_{i}}{a_{i}} \leqslant \frac{\left(a_{1}+a_{n}\right)^{2}}{4 a_{1} a_{n}} .
$$

## 第 702 题 给我一个合理的解释

设集合 $I=\{1,2,3,4,5\}$,选择 $I$ 的两个非空子集 $A, B$, 要使 $B$ 中最小的数大于 $A$ 中最大的数,则不同的选择方法共有种.

解析 49 .

考虑 $A$ 中最大的数为 $k$, 那么 $A$ 可以是 $1,2,3,4,5$ 中比 $k$ 小的数构成的集合的子集与 $\{k\}$ 的并集,而 $B$可以是 $1,2,3,4,5$ 中比 $k$ 大的数构成的集合的非空子集, 因此不同的选择方法数按 $k$ 分为 4 类, 总数为

$$
2^{0}\left(2^{4}-1\right)+2^{1}\left(2^{3}-1\right)+2^{2}\left(2^{2}-1\right)+2^{3}\left(2^{1}-1\right)=15+14+12+8=49 .
$$

一般的,对 $n$ 元集合,有

$$
2^{0}\left(2^{n-1}-1\right)+2^{1}\left(2^{n-2}-1\right)+\cdots+2^{n-1} \cdot\left(2^{1}-1\right)=(n-2) 2^{n-1}+1
$$

个不同的选择方法.

如下, 可以给通项一个解释.

先从 $\{1,2,3, \cdots, n\}$ 中随意选择一个数 $k$ 放人集合 $A$ 中, 然后从剩下的 $n-1$ 个数中挑出若干数, 其中比 $k$ 大的放在集合 $B$ 中,比 $k$ 小的放在集合 $A$ 中,共有 $n \cdot 2^{n-1}$ 种方法. 但是此时会有集合 $B$ 为空集的情形, 其个数分别为集合 $\{1,2,3, \cdots, n\}$ 的子集中最大元素为 $k$ 的子集数, 于是需要排除 $2^{n-1}$ 种方法 (即集合 $\{1,2, \cdots, n\}$ 的非空子集数), 总数为

$$
n \cdot 2^{n-1}-\left(2^{n}-1\right)=(n-2) \cdot 2^{n-1}+1
$$

## 第 703 题 四棱雉染色

用 6 种不同的颜色对正四棱雉 $P-A B C D$ 的 8 条棱染色, 每个顶点出发的棱的颜色各不相同, 不同的染色方案共有种。

解析 38880 .

先染从 $P$ 点出发的 4 条侧棱, 有 $\mathrm{A}_{6}^{4}=360$ 种不同的方案. 接下来考虑底面的染色.

情形一 没有额外的颜色, 有 2 种染色方案.

情形二 有 1 种额外的颜色, 分为 2 类:

(1) 染一条边, 有 $2 \cdot 4 \cdot 4=32$ 种方案

(2)染两条对边, 有 $2 \cdot 2 \cdot 4=16$ 种方案.

情形三 有 2 种额外的颜色, 分为 4 类:

(1) 染两条邻边, 有 $4 \cdot 2 \cdot 3=24$ 种方案;

(2) 染两条对边, 有 $2 \cdot 2 \cdot 4=16$ 种方案;

(3)染三条边, 有 $4 \cdot 2 \cdot 2=16$ 种方案

(4) 染四条边, 有 2 种方案.

因此不同的染色方案总数为

$$
360 \cdot[2+(32+16)+(24+16+16+2)]=38880
$$

## 第 704 题 格物致知

从集合 $\{1,2,3, \cdots, 30\}$ 中取出 5 个不同的数, 使这五个数构成等差数列, 则可以得到不同的等差数列的个数为个.

## 解析 196 .

先将问题削弱到取出 3 个不同的数. 此时有个不错的想法是只要确定数列的首项和末项, 那么数列的中间项就确定了. 为了使得数列的中间项为整数, 我们需要数列的首项和末项同时为奇数或同时为偶数. 于是所求的不同的等差数列个数为 $2 \mathrm{~A}_{15}^{2}=420$.

回到这个问题, 按奇偶划分就不能解决症结了. 实际上, 上面的做法中奇偶并不是本质, 本质是找到两
个数, 它们的差可以支持中间“分区” 为整数, 也就是差应该为 2 的倍数. 因此按 2 为模进行同余分划即可 (即按照奇数与偶数分成两个区).

那么按照这个思路, 首项和末项必须相差 4 的倍数, 我们应该按模 4 进行同余分划 (即按照 $4 k, 4 k+1$, $4 k+2,4 k+3$ 分成四个区, 每个区为一个同余类), 然后在每个同余类中找两个数分别作为首项和末项即可,于是所求的不同的等差数列个数为

$$
2 \mathrm{~A}_{8}^{2}+2 \mathrm{~A}_{7}^{2}=196
$$

思考与总结

古语有云: “格物致知. ”意思是探究事物的原理, 从而获得知识. 在这道题中,仔细挖掘“奇偶”背后的道理, 才能获得新的知识.

## 第 705 题 抓住本质减少讨论

设集合 $A=\left\{\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right) \mid x_{i} \in\{-1,0,1\}, i=1,2,3,4,5\right\}$,那么集合 $A$ 中满足条件“ $1 \leqslant\left|x_{1}\right|$ $+\left|x_{2}\right|+\left|x_{3}\right|+\left|x_{4}\right|+\left|x_{5}\right| \leqslant 3 ”$ 的元素个数为
A. 60 个
B. 90 个
C. 120 个
D. 130 个

## 解析 $\mathrm{D}$.

当 $x_{i} \neq 0$ 时, $\left|x_{i}\right|=1$, 要满足题中不等式, $x_{i}$ 中不是零的数只能有 1 个, 2 个或 3 个. 因此分三种情况讨论:

如果不是 0 的数有 1 个, 则这个数可以取 1 或 -1 , 满足条件的元素个数为

$$
\mathrm{C}_{5}^{1} \times 2^{1}=10 \text {; }
$$

如果不是 0 的数有 2 个, 则这两个数每个都有 2 种取法, 满足条件的元素个数为

$$
\mathrm{C}_{5}^{2} \times 2^{2}=40
$$

如果不是 0 的数有 3 个, 则这三个数每个都有 2 种取法, 满足条件的元素个数为

$$
\mathrm{C}_{5}^{3} \times 2^{3}=80
$$

故所有元素的个数为 $10+40+80=130$. 故选 D.

思考与总结

本题中 $x_{i}$ 的取值是零, 还是非零是本质的, 需要讨论; 是 1 还是 -1 是非本质的, 不需要讨论. 看出这一点, 就可以有效地减少讨论次数.

## 第 706 题 分类与分步

若集合

$$
\begin{aligned}
E= & \{(p, q, r, s) \mid 0 \leqslant p<s \leqslant 4,0 \leqslant q<s \leqslant 4,0 \leqslant r<s \leqslant 4 \text { 且 } p, q, r, s \in \mathbf{N}\}, \\
& F=\{(t, u, v, w) \mid 0 \leqslant t<u \leqslant 4,0 \leqslant v<w \leqslant 4 \text { 且 } t, u, v, w \in \mathbf{N}\},
\end{aligned}
$$

用 $\operatorname{card}(X)$ 表示集合 $X$ 中元素个数, 则 $\operatorname{card}(E)+\operatorname{card}(F)=$

解析 200.

集合 $E$ 中的元素个数可以按 $s$ 的取值分类计数, 而集合 $F$ 中的元素个数可以先在 $\{0,1,2,3,4\}$ 中选取
两组数 (每组数包含 2 个数字), 然后将两组数分别比较大小后分配给 $t, u, v, w$ 即可. 因此 $\operatorname{card}(E)+\operatorname{card}(F)=1^{3}+2^{3}+3^{3}+4^{3}+\mathrm{C}_{5}^{2} \cdot \mathrm{C}_{5}^{2}=200$.

解决计数问题的关键在于抓住问题的本质,然后用分类与分步规划出完成它的步骤.

在本题, 中集合 $E$ 中关键条件是 $s$ 为其中唯一的最大的数, $p, q, r$ 只要比 $s$ 小就可以,所以首先确定 $s$,而 $s$ 的大小会影响下一步的方法数, 所以需要先对 $s$ 进行分类, 之后分步即可; 集合 $F$ 中的元素可以分两组 $t, u$ 与 $u, w$ 分别考虑, 这是互相不影响的两步,而每步的方法数就相当于从 5 个数中任选 2 个, 于是本题的结论很容易就得到了.

## 第 707 题 双剑合璧

4 个相同的排球和 5 个相同的篮球装人 3 个不同的箱子,每箱至少有 1 个球, 求不同的装法总数.

解析 解法一 分为三类:

第一类 4 个排球都在同一个箱子里,此时将 5 个篮球补 3 个“虚拟篮球”, 然后在两个没有排球的箱子里各预置 1 个篮球, 用隔板法完成篮球数目的分配, 最后将每个箱子中的篮球数目都减去 1 (扣除“虚拟篮球”), 这样就得到了

$$
\mathrm{C}_{3}^{1} \cdot \mathrm{C}_{8-2-1}^{2}=30
$$

种不同的装法总数.

第二类 4 个排球装在两个箱子里 (不在同一个箱子里). 此时先用隔板法完成排球的分配. 接下来将 5 个篮球补 3 个“虚拟篮球”, 然后在那个没有排球的箱子里预置 1 个篮球, 用隔板法完成篮球数目的分配, 最后将每个箱子中的篮球数目都减去 1 (扣除“虚拟篮球”) , 这样就得到了

$$
\mathrm{C}_{3}^{2} \cdot \mathrm{C}_{3}^{1} \cdot \mathrm{C}_{8-1-1}^{2}=135
$$

种不同的装法总数.

第三类 4 个排球分布在三个箱子里. 此时用隔板法分别完成排球和篮球的分配. 这样就得到了

$$
\mathrm{C}_{3}^{2} \cdot \mathrm{C}_{8-1}^{2}=63
$$

种不同的装法总数.

因此总共有

$$
30+135+63=228
$$

种不同的装法总数.

解法二 利用容斥原理, 结合隔板法,所求装法总数为

$$
\mathrm{C}_{6}^{2} \mathrm{C}_{7}^{2}-\mathrm{C}_{3}^{1} \mathrm{C}_{5}^{1} \mathrm{C}_{6}^{1}+\mathrm{C}_{3}^{2} \mathrm{C}_{4}^{0} \mathrm{C}_{5}^{0}=228
$$

## 第 708 题各个击破

如图, 用四种不同颜色给图中的 $A, B, C, D, E, F$ 六个点涂色, 要求每个点涂一种颜色, 且图中每条线段的两个端点涂不同颜色, 则不同的涂色方法有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-163.jpg?height=249&width=230&top_left_y=2280&top_left_x=1612)

解析 264 .
解法一 选择 $A B C D$ 为一个单元进行讨论.

情形一 如果 $A B C D$ 涂 4 种颜色.

第一步涂 $A B C D$, 有 $\mathrm{A}_{4}^{4}=24$ 种涂色方式;

第二步涂 $E$, 有 2 种方式;

第三步涂 $F$ 也有 2 种方式 (因为 $E$ 必与 $B$ 或 $C$ 颜色相同).

所以共有

$$
24 \times 2 \times 2=96
$$

种涂色方式;

情形ニ 如果 $A B C D$ 涂 3 种颜色.

第一步涂 $A B C D$, 有

$$
\mathrm{C}_{4}^{3} \mathrm{C}_{3}^{1} \mathrm{C}_{2}^{1} \mathrm{~A}_{2}^{2}=48
$$

种方式 (选出三色、选出要用两次的颜色、选出涂同色的端点、涂剩下的端点);

第二步涂 $E, F$, 直接列举, 有 3 种方式. 共有 $48 \times 3=144$ 种涂色方式;

情形三 如果 $A B C D$ 涂 2 种颜色.

第一步涂 $A B C D$, 有 $\mathrm{A}_{4}^{2}=12$ 种方式;

第二步涂 $E, F$, 只有 2 种方式.

共有 $12 \times 2=24$ 种方式,

所以, 所有的涂色方式有 $96+144+24=264$ 种.

解法二 选择 $A D E F$ 为一个单元进行讨论.

情形一 如果 $A D E F$ 涂 4 种颜色.

第一步涂 $A D E F$, 有 $\mathrm{A}_{4}^{4}=24$ 种方式;

第二步涂 $B, C$, 直接列举知有 3 种方式.

共有 $24 \times 3=72$ 种方式,

情形二 如果 $A D E F$ 涂 3 种颜色.

第一步涂 $A D E F$, 有

$$
\mathrm{C}_{4}^{3} \mathrm{C}_{3}^{1} \mathrm{C}_{2}^{1} \mathrm{~A}_{2}^{2}=48
$$

种方式;

第二步涂 $B, C$, 有 4 种方式.

共有 $48 \times 4=192$ 种方式,

所以,所有的涂色方式有 $72+192=264$ 种.

当然, 还可以选择其他单元去讨论, 各个击破, 将一个复杂的讨论转化成简单的多次讨论, 得到结果.

## 第 709 题 计数的映射方法

已知集合 $A=\{1,2, \cdots, n\}$, 则定义在 $A$ 上的不减函数 $f: A \rightarrow A$ (即 $\forall x, y \in A, x \leqslant y$, 有 $f(x) \leqslant$ $f(y))$ 的个数为个.

解析 $\mathrm{C}_{2 n-1}^{n}$.

考虑 $(n+1) \times n$ 的网格, 每一个符合题意的不减函数都与其中的路径

$$
(1, f(1)) \rightarrow(2, f(2)) \rightarrow \cdots \rightarrow(n, f(n))
$$

一一对应, 将路径补充为

$$
(1,1) \rightarrow(1, f(1)) \rightarrow(2, f(2)) \rightarrow \cdots \rightarrow(n, f(n)) \rightarrow(n+1, n)
$$

且将该路径看作沿网格中的线段从 $(1,1)$ 运动到 $(n+1, n)$, 每次只能往右或者往上运动. 因此只需要在总共的 $2 n-1$ 次运动中确定向右运动的那 $n$ 次的位置即可, 答案为 $\mathrm{C}_{2 n-1}^{n}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-164.jpg?height=358&width=507&top_left_y=2222&top_left_x=1261)
利用映射将代数问题直观化有助于计数的顺利进行.

## 第 710 题 平分秋色

从数字 $1,2,3,4,5$ 中任意取 4 个组成四位数,则这些四位数的平均数是

解析 3333 .

解法一 显然共能组成 $A_{5}^{4}=120$ 个四位数, 设为 $\overline{a_{i} b_{i} c_{i} d_{i}}(i=1,2, \cdots, 120)$. 这 120 个数可以按 $\overline{a b c d}$ 与 $\overline{(6-a)(6-b)(6-c)(6-d)}$ 的方式两两配对, 如 1435 和 5231 . 因此所有四位数的平均数为

$$
\frac{6666 \times 60}{120}=3333
$$

解法二 显然共能组成 $\mathrm{A}_{5}^{4}=120$ 个四位数, 设为 $\overline{a_{i} b_{i} c_{i} d_{i}}(i=1,2, \cdots, 120)$. 这 120 个数依次写出:

| $a_{1}$ | $b_{1}$ | $c_{1}$ | $d_{1}$ |
| :---: | :---: | :---: | :---: |
| $a_{2}$ | $b_{2}$ | $c_{2}$ | $d_{2}$ |
| $\ldots$ | $\cdots$ | $\cdots$ | $\ldots$ |
| $a_{120}$ | $b_{120}$ | $c_{120}$ | $d_{120}$ |

每一列中 $1,2,3,4,5$ 的个数均为 24 , 于是每一位的平均数为

$$
\frac{24(1+2+3+4+5)}{120}=3
$$

因此所有四位数的平均数为 3333 .

## 第 711 题 长短不一

以正 12 边形的顶点为端点的线段中任选 3 条, 能构成三角形的三条边的概率为

解析 $\frac{223}{286}$.

正 12 边形共有 $\mathrm{C}_{12}^{2}=66$ 条线段, 设其外接圆半径为 1 , 则其中长度为

$$
2 \sin 15^{\circ}, 2 \sin 30^{\circ}, 2 \sin 45^{\circ}, 2 \sin 60^{\circ}, 2 \sin 75^{\circ}
$$

的线段各有 12 条, 长度为 $2 \sin 90^{\circ}$ 的线段有 6 条, 将这些边长分别记为 $a, b, c, d, e, f$, 则不能构成三角形的三条边的情形有

$$
a a c, a a d, a a e, a a f, a b d, a b e, a b f, a c e, a c f, b b f,
$$

因此所求的概率为

$$
1-\frac{\mathrm{C}_{12}^{2} \mathrm{C}_{42}^{1}+\mathrm{C}_{12}^{1} \mathrm{C}_{12}^{1} \mathrm{C}_{30}^{1}+\mathrm{C}_{12}^{1} \mathrm{C}_{12}^{1} \mathrm{C}_{18}^{1}+\mathrm{C}_{12}^{2} \mathrm{C}_{6}^{1}}{\mathrm{C}_{66}^{3}}=\frac{223}{286} .
$$

思考与总结

注意 $a=2 \sin 15^{\circ}=\sqrt{2-\sqrt{3}} \approx 0.52, e=2 \sin 75^{\circ}=\sqrt{2+\sqrt{3}} \approx 1.93$, 且有 $e-a=\sqrt{2+\sqrt{3}}-\sqrt{2-\sqrt{3}}=\sqrt{2}=c$.

## 第 712 题 各显身手

有 7 个编号分别为 $1,2,3,4,5,6,7$ 的小球, 其中编号为 1,2 的小球为红色, 编号为 3,4 的小球为黑色, 编号为 $5,6,7$ 的小球为白色, 将这些小球放人 5 个不同的盒子中, 每个盒子放 1 个或 2 个小球同色的球不能放在同一个盒子里,求不同的放置方法总数.

解析 解法一 根据容斥原理, 总数为

$$
\left[\frac{\mathrm{C}_{7}^{2} \mathrm{C}_{5}^{2}}{\mathrm{~A}_{2}^{2}}-\left(\mathrm{C}_{2}^{2}+\mathrm{C}_{2}^{2}+\mathrm{C}_{2}^{3}\right) \mathrm{C}_{5}^{2}+\left(\mathrm{C}_{2}^{2} \mathrm{C}_{2}^{2}+\mathrm{C}_{2}^{2} \mathrm{C}_{3}^{2}+\mathrm{C}_{2}^{2} \mathrm{C}_{3}^{2}\right)\right] \cdot \mathrm{A}_{5}^{5}=7440
$$

解法二 先放三个白球, 有 $\mathrm{A}_{5}^{3}=60$ 种放法;

再考虑两个红球如何放,以此分类.

第 1 类: 两个红球都放人空盒, 有 $2 \mathrm{~A}_{5}^{2}=40$ 种;

第 2 类: 两个红球中的一个放人空盒, 另一个放人已有白球的盒中, 有 $3 \cdot 2 \cdot 2 \cdot 2 \cdot 3=72$ 种;

第 3 类:两个红球都放人已有白球的盒中, 有 $\mathrm{A}_{3}^{2} \cdot \mathrm{A}_{2}^{2}=12$ 种;

综上,共有

$$
60 \cdot(40+72+12)=7440
$$

种放法.

解法三 先将球分成五堆,其中两堆有两个球, 这两个球的组合有六种,分别计数如下,

笴 1 类:红黑、红黑,有 2 种分堆方式;

笴 2 类: 红白、红白(黑白、黑白相同), 分别有 $3 \cdot 2=6$ 种;

笏, 3 类: 红黑、红白 (红黑、黑白相同), 分别有 $2 \cdot 2 \cdot 3=12$ 种;

第; 1 类: 红白、黑白, 有 $2 \cdot 3 \cdot 2 \cdot 2=24$ 种;

共有

$$
(2+2 \cdot 6+2 \cdot 12+24) \cdot \mathrm{A}_{5}^{5}=7440
$$

种放法.

## 第 713 题 $\quad$ 寻找对应关系

在 $6 \times 6$ 的表格中停放 3 辆完全相同的红色车和 3 辆完全相同的黑色车, 每一行、每一列只有一辆车, 每辆车占一格, 共有 $(\quad)$ 种亭放方法.
A. 720
B. 518400
C. 20
D. 14400

解析 D.

视 6 辆车均相同, 记停在第 $i$ 行的车在 $a_{i}$ 列, 如图对应的数列为

$$
a_{1}=2, a_{2}=3, a_{3}=5, a_{4}=6, a_{5}=4, a_{6}=1 ;
$$

于是每一种 $1,2, \cdots, 6$ 的排列 $\left(a_{1}, a_{2}, \cdots, a_{6}\right)$ 对应一种放法.

于是 $\mathrm{A}_{6}^{6} \cdot \mathrm{C}_{6}^{3} \cdot \mathrm{C}_{3}^{3}=14400$ 为所求. 故选 D.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-166.jpg?height=276&width=273&top_left_y=2124&top_left_x=1481)

## 第 714 题 数列中的计数

数列 $\left\{a_{n}\right\}$ 共有 11 项, $a_{1}=0, a_{11}=4$, 且 $\left|a_{k+1}-a_{k}\right|=1, k=1,2, \cdots, 10$, 满足这种条件的不同数列的个数为个.

解析 120 .

因为 $a_{k+1}-a_{k}=1$ 或 -1 , 假设共有 $x$ 个 1 , 则

$$
x+(-1)(10-x)=4,
$$

得 $x=7$. 所以 $\mathrm{C}_{10}^{7}=120$ 为所求.

## 第 715 题 上上下下

设数列 $a_{1}, a_{2}, a_{3}, \cdots, a_{21}$ 满足 $\left|a_{n+1}-a_{n}\right|=1(n=1,2,3, \cdots, 20)$, 且 $a_{1}, a_{7}, a_{21}$ 成等比数列. 若 $a_{1}=1$, $a_{21}=9$, 则满足条件的不同数列的个数为个.

解析 15099 .

设 $b_{n}=a_{n+1}-a_{n}, n=1,2, \cdots, 20$, 则数列 $a_{1}, a_{2}, a_{3}, \cdots, a_{21}$ 与有序数组

$$
\left(b_{1}, b_{2}, \cdots, b_{20}\right)
$$

一一对应, 且 $b_{i} \in\{1,-1\}(i=1,2, \cdots, 20)$. 根据题意, 有 $a_{7}=3$ 或 $a_{7}=-3$, 于是

$$
\left\{\begin{array}{l}
b_{1}+b_{2}+\cdots+b_{6}=2 \\
b_{7}+b_{8}+\cdots+b_{20}=6
\end{array}\right.
$$

或

$$
\left\{\begin{array}{l}
b_{1}+b_{2}+\cdots+b_{6}=-4 \\
b_{7}+b_{8}+\cdots+b_{20}=12
\end{array}\right.
$$

对应的个数为

$$
\mathrm{C}_{6}^{4} \mathrm{C}_{14}^{10}+\mathrm{C}_{6}^{1} \mathrm{C}_{14}^{13}=15099
$$

## 第 716 题 立体几何中的计数

在四面体的顶点和各棱中点共 10 个点中,两两连线共可组成的异面直线对数为

解析 255.

由这 10 个点组成的直线共有 33 条, 所有的直线对数为 $\mathrm{C}_{33}^{2}=528$, 接下来考虑其中共面的直线对.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-167.jpg?height=220&width=968&top_left_y=2266&top_left_x=414)

如图, 共面的直线对分为 5 类, 合计对数为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-167.jpg?height=213&width=202&top_left_y=2274&top_left_x=1420)

$$
4 \mathrm{C}_{9}^{2}+3 \mathrm{C}_{6}^{2}+6 \mathrm{C}_{4}^{2}+4 \mathrm{C}_{3}^{2}+12 \mathrm{C}_{3}^{2}=273
$$

因此所求的异面直线对数为 $528-273=255$.

## 第 717 题 系数的系数从哪里来

## 已知 $(1+x)^{50}=a_{0}+a_{1} x+a_{2} x^{2}+\cdots+a_{50} x^{50}$, 则 $a_{1}+2 a_{2}+3 a_{3}+\cdots+25 a_{25}$ 的值为

解析 解法一 根据已知, 有

$$
a_{k}=\mathrm{C}_{50}^{k}, k=0,1,2, \cdots, 50
$$

由组合恒等式

$$
\frac{\mathrm{C}_{n}^{m}}{\mathrm{C}_{n-1}^{m-1}}=\frac{n}{m}
$$

于是可得

$$
m \mathrm{C}_{n}^{m}=n \mathrm{C}_{n-1}^{m-1}
$$

这样就可以给二项式系数分别配上相应的系数.

将此恒等式应用到本题,所求代数式

$$
\sum_{k=1}^{25} k \mathrm{C}_{50}^{k}=\sum_{k=1}^{25} 50 \mathrm{C}_{49}^{k-1}=50 \cdot 2^{48}
$$

由此可以推广到

$$
\sum_{k=1}^{n} k \cdot \mathrm{C}_{n}^{k}=n \cdot 2^{n-1}
$$

解法二 对已知等式两侧分别求导得到所需要的系数

$$
50(1+x)^{49}=\sum_{k=1}^{50}\left(k \cdot a_{k} x^{k-1}\right)
$$

令 $x=1$, 可得

$$
50 \cdot 2^{49}=a_{1}+2 a_{2}+\cdots+25 a_{25}+26 a_{26}+\cdots+50 a_{50},
$$

注意到左侧系数的对称性, 可得

$$
\begin{aligned}
& a_{1}=50 a_{50} \\
& 2 a_{2}=49 a_{49} \\
& \cdots \\
& 25 a_{25}=26 a_{26}
\end{aligned}
$$

因此

$$
a_{1}+2 a_{2}+3 a_{3}+\cdots+25 a_{25}=50 \cdot 2^{48}
$$

## 第 718 题 谢尔宾斯基三角

如图 1, 由若干个小正方形组成的 $k$ 层三角形图阵, 第一层有 1 个小正方形, 第二层有 2 个小正方形, $\cdots$, 依此类推,第 $k$ 层有 $k$ 个小正方形. 除去最底下一层, 每个小正方形都放置在它下一层的两个小正方形之上. 现对第 $k$ 层的每个小正方形用数字进行标注, 从左到右依次记为 $x_{1}, x_{2}, \cdots, x_{k}$, 其中 $x_{i} \in$ $\{0,1\}(1 \leqslant i \leqslant k)$, 其他小正方形标注的数字是它下面的两个小正方形标注的数字之和, 依此规律, 记第一层的小正方形标注的数字为 $x_{0}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-169.jpg?height=178&width=178&top_left_y=716&top_left_x=1022)

第 $k$ 层

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-169.jpg?height=96&width=441&top_left_y=998&top_left_x=891)

图 1

(1) 当 $k=4$ 时, 若要求 $x_{0}$ 为 2 的倍数, 则有多少种不同的标注方法?

(2)当 $k=11$ 时, 若要求 $x_{0}$ 为 3 的倍数,则有多少种不同的标注方法?

解析 (1)类似于 “杨辉三角”, 我们容易知道

$$
x_{0}=\mathrm{C}_{k-1}^{0} x_{1}+\mathrm{C}_{k-1}^{1} x_{2}+\mathrm{C}_{k-1}^{2} x_{3}+\cdots+\mathrm{C}_{k-1}^{k-1} x_{k}
$$

如图 2 为 $k=4$ 时每个方格中的数相加的次数.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-169.jpg?height=183&width=82&top_left_y=1463&top_left_x=736)

第2层

第 3 层

第 4 层

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-169.jpg?height=194&width=200&top_left_y=1463&top_left_x=1088)

图 2

这样, 我们就可以得到不同的标注方法数为

$$
\mathrm{C}_{4}^{0}+\mathrm{C}_{4}^{2}+\mathrm{C}_{4}^{4}=8 .
$$

(2) 从第 (1) 小题可以看到, 第 $k$ 层各个方格中的数字本身可以替换为对应的模同余的余数.

因此, 当 $k=11$ 时, 可以如图 3 填数.

这样, 我们就可以得到不同的标注方法数为

$$
\left(\mathrm{C}_{4}^{0}+\mathrm{C}_{4}^{3}\right) \cdot 2^{7}=640
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-169.jpg?height=440&width=421&top_left_y=1707&top_left_x=1440)

图 3
如果把新的“杨辉三角”中所有的 0 用特别的颜色标记出来, 就会得到类似于“谢尔宾斯基三角”的美丽图案.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-170.jpg?height=545&width=410&top_left_y=210&top_left_x=1341)

## 第 719 题 侽然与必然

若甲乙对局时, 甲赢得单局比赛的概率为 $p(p>0.5$ ), 求证: 在 $2 n+1$ 局 $n+1$ 胜 (如 5 局 3 胜)制的比赛中, 甲最终胜出的概率随着 $n$ 的增大而增大.

解析 设在 $2 n+1$ 局 $n+1$ 胜 (如 5 局 3 胜) 制的比赛中, 甲最终胜出的概率为 $a_{n}$, 则

$$
a_{n}=\mathrm{C}_{2 n+1}^{n+1} p^{n+1}(1-p)^{n}+\mathrm{C}_{2 n+1}^{n+2} p^{n+2}(1-p)^{n-1}+\cdots+\mathrm{C}_{2 n+1}^{2 n+1} p^{2 n+1},
$$

在此基础上,利用全概率公式计算 $a_{n+1}$, 包含四种情形:

(1) 甲在前 $2 n+1$ 局比赛中赢了不足 $n$ 局, 则一定无法胜出;

(2) 甲在前 $2 n+1$ 局比赛中赢了 $n$ 局,则剩下的两局比赛都赢方能胜出,概率为

$$
\left[\mathrm{C}_{2 n+1}^{n} p^{n}(1-p)^{n+1}\right] \cdot p^{2}=\mathrm{C}_{2 n+1}^{n} p^{n+2}(1-p)^{n+1}
$$

(3) 甲在前 $2 n+1$ 局比赛中赢了 $n+1$ 局,则剩下的两局比赛不全输就能胜出,概率为

$$
\left[\mathrm{C}_{2 n+1}^{n+1} p^{n+1}(1-p)^{n}\right] \cdot\left[1-(1-p)^{2}\right]=\mathrm{C}_{2 n+1}^{n+1} p^{n+1}(1-p)^{n}-\mathrm{C}_{2 n+1}^{n+1} p^{n+1}(1-p)^{n+2}
$$

(4) 甲在前 $2 n+1$ 局比赛中已经赢了超过 $n+2$ 局, 则一定胜出, 概率为

$$
\mathrm{C}_{2 n+1}^{n+2} p^{n+2}(1-p)^{n-1}+\cdots+\mathrm{C}_{2 n+1}^{2 n+1} p^{2 n+1}
$$

这样我们就可以得到

$$
\begin{aligned}
a_{n+1}-a_{n} & =\mathrm{C}_{n+1}^{n} p^{n+2}(1-p)^{n+1}-\mathrm{C}_{2 n+1}^{n+1} p^{n+1}(1-p)^{n+2} \\
& =\mathrm{C}_{2 n+1}^{n} p^{n+1}(1-p)^{n+1} \cdot(2 p-1) \\
& >0,
\end{aligned}
$$

也即甲最终胜出的概率随着 $n$ 的增大而增大.

乒乓球赛制从 21 球改为 11 球是对中国参赛选手的一种压制, 这就是背后的原因.

## 第 720 题隔帊与对应

$\left(1+x+x^{2}+\cdots+x^{100}\right)^{3}$ 的展开式中包含 $x^{150}$ 的项的系数为
此问题等价于方程

$$
i+j+k=150,0 \leqslant i, j, k \leqslant 100
$$

的非负整数解 $(i, j, k)$ 的个数.

如果 $i, j, k$ 没有不大于 100 的限制, 那么此问题可以直接用隔板法与对应法解决, 将 $(i, j, k)$ 对应到 $\left(i^{\prime}\right.$, $\left.j^{\prime}, k^{\prime}\right)=(i+1, j+1, k+1)$, 则考虑 $i^{\prime}+j^{\prime}+k^{\prime}=153$ 的正整数解的个数即可, 直接用隔板法知, 共有 $\mathrm{C}_{152}^{2}$ 个.

再考虑不满足限制条件的解的个数, 即 $i, j, k$ 中有一个数大于 100 , (有且仅有一个!) 先考虑 $i \geqslant 101$ 的解的个数, 作对应

$$
(i, j, k) \rightarrow\left(i^{\prime}, j^{\prime}, k^{\prime}\right)=(i-100, j+1, k+1)
$$

则 $i^{\prime}+j^{\prime}+k^{\prime}=52$, 考虑此方程的正整数解的个数即可, 有 $\mathrm{C}_{51}^{2}$ 个, 所以所有不满足限制条件的解的个数为 $3 \mathrm{C}_{51}^{2}$.

综上知, $x^{150}$ 的系数为

$$
\mathrm{C}_{152}^{2}-3 \mathrm{C}_{51}^{2}=7651
$$

## 第 721 题 组合数求和

设 $S=\frac{1}{2017} \mathrm{C}_{2017}^{0}-\frac{1}{2016} \mathrm{C}_{2016}^{1}+\frac{1}{2015} \mathrm{C}_{2015}^{2}-\cdots-\frac{1}{1010} \mathrm{C}_{1010}^{1007}+\frac{1}{1009} \mathrm{C}_{1009}^{1008}$, 则 $S$ 的值是

解析 $\frac{1}{2017}$.

根据题意, 有

$$
\begin{aligned}
2017 S & =\mathrm{C}_{2017}^{0}-\left(1+\frac{1}{2016}\right) \mathrm{C}_{2016}^{1}+\left(1+\frac{2}{2015}\right) \mathrm{C}_{2015}^{2}-\cdots+\left(1+\frac{1008}{1009}\right) \mathrm{C}_{1009}^{1008} \\
& =\mathrm{C}_{2017}^{0}-\left(\mathrm{C}_{2016}^{1}+\mathrm{C}_{2015}^{0}\right)+\left(\mathrm{C}_{2015}^{2}+\mathrm{C}_{2014}^{1}\right)-\cdots+\left(\mathrm{C}_{1009}^{1008}+\mathrm{C}_{1008}^{1007}\right) \\
& =S_{2017}-\mathrm{S}_{2015},
\end{aligned}
$$

其中

$$
\begin{aligned}
& S_{2017}=C_{2017}^{0}-C_{2016}^{1}+C_{2015}^{2}-\cdots+\mathrm{C}_{1098}^{1008}, \\
& S_{2015}=\mathrm{C}_{2015}^{0}-\mathrm{C}_{2014}^{1}+\mathrm{C}_{2013}^{2}-\cdots-\mathrm{C}_{1008}^{1007},
\end{aligned}
$$

类似的定义

$S_{2 k}=\mathrm{C}_{2 k}^{0}-\mathrm{C}_{2 k-1}^{1}+\mathrm{C}_{2 k-2}^{2}-\cdots+(-1)^{k} \mathrm{C}_{k}^{k}$,

$$
S_{2 k+1}=\mathrm{C}_{2 k+1}^{0}-\mathrm{C}_{2 k}^{1}+\mathrm{C}_{2 k-1}^{2}-\cdots+(-1)^{k} \mathrm{C}_{k+1}^{k}
$$

那么由组合恒等式

$$
\mathrm{C}_{n}^{m}=\mathrm{C}_{n-1}^{m-1}+\mathrm{C}_{n-1}^{m}
$$

可得

$$
S_{2 k+1}-S_{2 k}=-S_{2 k-1}, S_{2 k+2}-S_{2 k+1}=-S_{2 k}
$$

因此有

$$
S_{n+2}=S_{n+1}-S_{n},
$$

于是数列 $\left\{S_{n}\right\}$ 是周期为 6 的数列. 考虑到 $S_{1}=1, S_{2}=0$, 因此

因此

$$
S_{n}: \underbrace{1,0,-1,-1,0,1,1}, \underbrace{1,0,-1,-1,0,1,1}, \cdots,
$$

$$
S_{2017}=S_{1}=1, S_{2015}=S_{5}=0
$$

所以 $S=\frac{1}{2017}$.

## 第 722 题 渐开数

“渐开数”是指:一个数从第二位起, 每一位数字都比其左边数字大的整数 (如 236), 那么任取一个三位数, 它是“渐开数”的概率为

## 解析 $\frac{7}{75}$.

我们先来看“渐开数”的特征, 任何一个“渐开数”的三个数字均不相同, 且不含零.

而任何三个不同的数字(不含零) 都能组成唯一的一个“渐开数”.

于是我们得到三位“渐开数”的个数为

$$
\mathrm{C}_{9}^{3}=84
$$

从而所求概率为

$$
\frac{\mathrm{C}_{9}^{3}}{999-100+1}=\frac{7}{75}
$$

思考与总结

本题的关键在于找到其中的对应关系, 很多与计数相关的问题都需要寻找对应关系,一个好的对应关系可以看清问题本质,减少不必要的讨论.

## 第 723 题 几何概型

已知函数 $f(x)=\left|1-x^{2}\right|$, 在 $[0,1]$ 上任取一数 $a$, 在 $[1,2]$ 上任取一数 $b$, 则满足 $f(a) \leqslant f(b)$ 的概率为 $\qquad$ .

解析 $\frac{6-\pi}{4}$.

根据题意, $f(a) \leqslant f(b)$ ，即

$$
\left|1-a^{2}\right| \leqslant\left|1-b^{2}\right|
$$

也即

$$
a^{2}+b^{2} \geqslant 2
$$

如图. 因此所求的概率为 $1+\frac{1}{2}-\frac{\pi}{4}=\frac{6-\pi}{4}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-172.jpg?height=352&width=287&top_left_y=1696&top_left_x=1483)

## 第 724 题 全概率公式

已知袋中有 10 个小球, 其中有 5 个红球、 3 个黄球和 2 个绿球. 每次从袋中不放回地取出一个球,问红球首先被全部取出的概率?

解析 最后一个球为红球、黄球、绿球的概率分别为

$$
\frac{5}{10}, \frac{3}{10}, \frac{2}{10}
$$

考虑最后一个球为黄球的情形, 此时忽略掉所有的黄球, 则红球首先被全部取出即最后一个球为绿球;类似的, 在最后一个球为绿球时忽略所有的绿球, 则红球首先被全部取出即最后一个球为黄球. 根据全概率公式, 红球首先被全部取出的概率为

$$
\frac{3}{10} \times \frac{2}{7}+\frac{2}{10} \times \frac{3}{8}=\frac{9}{56}
$$

思考与总结

一般地, 当红球、黄球、绿球的个数分别为 $a, b, c$ 时, 红球首先被全部取出的概率为

$$
\frac{b}{a+b+c} \cdot \frac{c}{a+c}+\frac{c}{a+b+c} \cdot \frac{b}{a+b}=\frac{b c(2 a+b+c)}{(a+b+c)(a+b)(a+c)}
$$

特别的, 如果 $a=b=c$, 那么所求概率为 $\frac{1}{3}$; 如果 $b=c=1$, 那么所求概率为 $\frac{2}{(a+2)(a+1)}$, 与常识一致.

## 第 725 题 “约不约”随机

设 $A, B, C, D$ 是空间四个不共面的点, 以 $\frac{1}{2}$ 的概率在每对点之间连一条边, 任意两对点之间是否连边是相互独立的,则 $A, B$ 可用空间折线 (一或若干条边组成的)连结的概率为

解析 $\frac{3}{4}$.

考虑反面:

解法一 以 $B, C$ 与 $B, D$ 是否连边分三种情况讨论:

(1) 若 $B, C$ 与 $B, D$ 都不连边,则一定满足情况,所求概率为

$$
\frac{1}{2} \times \frac{1}{2} \times \frac{1}{2}=\frac{1}{8}
$$

(2)若 $B, C$ 与 $B, D$ 都连边, 那么 $A, C$ 与 $A, D$ 都不连边, 所求概率为

$$
\left(\frac{1}{2}\right)^{5}=\frac{1}{32}
$$

(3) 若 $B, C$ 与 $B, D$ 恰有一组连边, 不妨考虑 $B, C$ 连边, $B, D$ 不连边, 则 $A, C$ 不连边, 且 $C, D$ 与 $A, D$ 不同时连边即可, 所求概率为

$$
\frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} \times\left(1-\frac{1}{4}\right)=\frac{3}{64}
$$

所以 $A, B$ 不能用空间折线连接的概率为

$$
\frac{1}{8}+\frac{1}{32}+2 \times \frac{3}{64}=\frac{1}{4}
$$

从而所求概率为 $1-\frac{1}{4}=\frac{3}{4}$.

解法二 按 $C, D$ 是否连边分两种情况讨论:

(1) 若 $C, D$ 不连边, 则满足条件的有三种情况: $(A, D) 、(B, D) 、(A, C)$ 与 $(B, C)$ 都不连边; 仅有一组连边;或有两组连边, 但 $A, D$ 与 $B, D$ 不同时连边, $A, C$ 与 $B, C$ 不同时连边均可.

故所求概率为

$$
\frac{1}{2} \times \frac{1}{2} \times\left[\left(\frac{1}{2}\right)^{4}+\mathrm{C}_{4}^{1} \times\left(\frac{1}{2}\right)^{4}+\mathrm{C}_{2}^{1} \times \mathrm{C}_{2}^{1} \times\left(\frac{1}{2}\right)^{4}\right]=\frac{9}{64}
$$

(2) 若 $C, D$ 连边, 也有三种情况: $(A, D) 、(B, D) 、(A, C) 、(B, C)$ 全不连边; 或只有一组连边, 或有两组连边, 但两组连边为 $(A D) 、(A C)$ 或 $(B C) 、(B D)$.

所求概率为

$$
\frac{1}{2} \times \frac{1}{2} \times\left[\frac{1}{16}+\mathrm{C}_{4}^{3} \times\left(\frac{1}{2}\right)^{4}+2 \times\left(\frac{1}{2}\right)^{4}\right]=\frac{7}{64}
$$

从而 $A, B$ 不能用折线连结的概率为

$$
\frac{9}{64}+\frac{7}{64}=\frac{1}{4}
$$

所求概率为 $1-\frac{1}{4}=\frac{3}{4}$.

## 第 726 题 概率的最值

某高校数学系计划在周六和周日各举行一次主题不同的心理测试活动, 分别由李老师和张老师负责. 已知该系共有 $n$ 位学生, 每次活动均需该系 $k$ 位学生参加 ( $n$ 和 $k$ 都是固定的正整数). 假设李老师和张老师分别将各自活动通知的信息独立、随机地发给该系 $k$ 位学生, 且所发信息都能被学生收到. 记该系收到李老师或张老师所发活动通知信息的学生人数为 $X$.

(1)求该系学生甲收到李老师或张老师所发活动通知信息的概率;

(2) 求使 $P(X=m)$ 取得最大值的整数 $m$.

解析 (1)根据独立事件的概率计算公式, 可得所求概率

$$
p=1-\left(1-\frac{k}{n}\right)^{2}=\frac{k(2 n-k)}{n^{2}}
$$

(2) $m$ 的可能取值为 $k, k+1, k+2, \cdots, \min \{2 k, n\}$, 同时收到李老师和张老师所发信息的人数为 $2 k-m$,只收到李老师所发信息以及只收到张老师所发信息的人数均为 $m-k$, 于是

$$
P(X=m)=\frac{\mathrm{C}_{n}^{k} \mathrm{C}_{k}^{2 k-m} \mathrm{C}_{n-k}^{m-k}}{\mathrm{C}_{n}^{k} \mathrm{C}_{n}^{C_{n}}}=\frac{\mathrm{C}_{k}^{2 k-m} \mathrm{C}_{n-k}^{m-k}}{\mathrm{C}_{n}^{k}}
$$

考虑

$$
\begin{aligned}
\frac{P(X=m+1)}{P(X=m)} & =\frac{\mathrm{C}_{k}^{2 k-m-1} \mathrm{C}_{n-k}^{m+1-k}}{\mathrm{C}_{n}^{m-k} \mathrm{C}_{n-k}^{m-k}} \\
& =\frac{(n-m)(2 k-m)}{(m+1-k)^{2}} \\
& =\frac{m^{2}+(-n-2 k) m+2 n k}{m^{2}+(2-2 k) m+(k-1)^{2}} \\
& =1-\frac{(n+2) m-2 n k+(k-1)^{2}}{m^{2}+(2-2 k) m+(k-1)^{2}}
\end{aligned}
$$

因为上式中的分母为正, 考虑 $(n+2) m-2 n k+(k-1)^{2}$ 的正负即可.

记 $\lambda=\frac{2 n k-(k-1)^{2}}{n+2}$, 则当 $m>\lambda$ 时,

$$
P(X=m+1)<P(X=m) \text {; }
$$

当 $m=\lambda$ 时,

$$
P(X=m+1)=P(X=m) \text {; }
$$

当 $m<\lambda$ 时,

$$
P(X=m+1)>P(X=m)
$$

因此当 $\lambda \in \mathbf{N}$ 时, 有

$$
P(X=\lambda+1)=P(X=\lambda),
$$

高考数学满分学霸的解题笔记(一个..........

且两者均为最大值, 此时 $m=\lambda, \lambda+1$;

当 $\lambda \notin \mathbf{N}$ 时, 有 $P(X=[\lambda]+1)$ 为最大值, 此时 $m=[\lambda]+1$, 其中 $[\lambda]$ 表示不超过 $\lambda$ 的最大整数.

## 第 727 题 交卷顺序

阶梯教室安装的连体课桌一行坐 6 个人, 考生只能从课桌两头走出考场, 考生交卷时间先后不一,如果坐在里面的考生要先交卷就需要打扰别人, 把一行考生中打扰别人交卷的人数视为随机变量 $X$,求 $X$ 的数学期望.

解析 设连体课桌一行坐 $n(n \geqslant 3)$ 个人, 则随机变量 $X$ 对应的取值为 $1,2, \cdots, n-2$.

当 $n=3$ 时, 将考生依次记为 $A B C$, 那么当第一个交卷的考生为 $A, C$ 时, $X=0$, 当第一个交卷的考生为 $B$ 时, $X=1$,于是

| $X$ | 0 | 1 |
| :---: | :---: | :---: |
| $P_{3}$ | $\frac{4}{3!}$ | $\frac{2}{3!}$ |

当 $n=4$ 时, 将考生依次记为 $A B C D$, 那么当第一个交卷的考生为 $A, D$ 时, 情况转化为 $n=3$ 的情形; 当第一个交卷的考生为 $B, C$ 时, 情况转化为 $n=3$ 的情形中每个 $X$ 都增加 1 , 于是有

$$
\begin{aligned}
& P_{4}(X=0)=\frac{2}{4} P_{3}(X=0)=\frac{8}{4!}, \\
& P_{4}(X=1)=\frac{2}{4} P_{3}(X=1)+\frac{2}{4} P_{3}(X=0)=\frac{12}{4!}, \\
& P_{4}(X=2)=\frac{2}{4} P_{3}(X=1)=\frac{4}{4!} .
\end{aligned}
$$

有

| $X$ | 0 | 1 | 2 |
| :---: | :---: | :---: | :---: |
| $P_{4}$ | $\frac{8}{4!}$ | $\frac{12}{4!}$ | $\frac{4}{4!}$ |

进而 $n=5$ 时, 对应的分布列为

| $X$ | 0 | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: | :---: |
| $P_{5}$ | $\frac{16}{5!}$ | $\frac{48}{5!}$ | $\frac{44}{5!}$ | $\frac{12}{5!}$ |

而 $n=6$ 时, 对应的分布列为

| $X$ | 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $P_{6}$ | $\frac{32}{6!}$ | $\frac{160}{6!}$ | $\frac{280}{6!}$ | $\frac{200}{6!}$ | $\frac{48}{6!}$ |

于是所求的数学期望为

$$
\frac{160+560+600+192}{6!}=\frac{21}{10}
$$

思考与总结

事实上,有

$$
P(X=k)=\sum_{1 \leqslant i_{1}<i_{2}<\cdots<i_{k} \leqslant n-2} \frac{\left(n-1-i_{1}\right)\left(n-1-i_{2}\right) \cdots\left(n-1-i_{k}\right) \cdot 2^{n-1-k}}{n!}
$$

## 第八章 平面几何

## 第 728 题 从“凸轮”到“勒洛”

如图 1,一个“凸轮”放置于直角坐标系 $x$ 轴上方, 其“底端”落在原点处,一顶点及中心在 $y$ 轴正半轴上, 它的外围由以正三角形的顶点为圆心,以正三角形的边长为半径的三段等弧组成.

今使“凸轮”沿 $x$ 轴正向滚动前进, 在滚动过程中, “凸轮”每时每刻都有一个“最高点”, 其中心也在不断移动位置,则在“凸轮”滚动一周的过程中,将其“最高点”和“中心点”所形成的图形按上下放置, 应大致为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-176.jpg?height=442&width=379&top_left_y=1069&top_left_x=100)

$\mathrm{D}$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-176.jpg?height=418&width=883&top_left_y=1084&top_left_x=824)

图 1

解析 A.

凸轮的滚动实际上由交替的滚动 (接触点不断变化)和转动 (接触点不变)形成. 滚动的部分如图 2.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-176.jpg?height=284&width=415&top_left_y=1699&top_left_x=390)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-176.jpg?height=281&width=418&top_left_y=1698&top_left_x=1002)

图 3

注意若不考虑其中的平动, 只考虑转动 (事实上, 滚动就是平动与转动的合成), 则旋转的中心为与 $x$ 轴接触的弧对应的圆心. 转动的部分如图 3.

注意转动的中心为与 $x$ 接触的凸轮内正三角形的顶点. 经过分析可知任何时候凸轮的宽度均相等, 且其中心离 $x$ 轴的距离在正三角形的内切圆半径和外接圆半径之间周期变化, 且在初始位置时取得最小值,如图 4. 这样就可得到正确答案是 A. 事实上, 这个凸轮就是著名的“勒洛三角形”.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-176.jpg?height=283&width=1121&top_left_y=2267&top_left_x=345)

图 4

## 第 729 题 “公转”与“自转”

如图 1, 一个直径为 1 的小圆, 沿着直径为 2 的大圆内壁按逆时针方向滚动, $M$ 和 $N$ 是小圆的一条固定直径的两个端点. 那么, 当小圆这样滚过大圆内壁的一周,点 $M, N$ 在大圆内所绘出的图形大致是什么?

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-177.jpg?height=287&width=316&top_left_y=457&top_left_x=1523)

图 1

解析 $\quad$ 这是一个动态几何问题, 涉及的运动很复杂.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-177.jpg?height=420&width=1428&top_left_y=887&top_left_x=318)

图 2

如图 2, 对于这个运动, 我们考虑将 $M N \rightarrow M_{1} N_{1}$ 的运动分解为如下步骤:

(1)小圆在大圆内的转动 (将小圆想象为一枚一元硬币, 数字始终朝正上方), 相当于“公转”;

(2)小圆自身的转动,相当于“自转”.

“公转”部分比较简单, 设旋转角为 $\theta_{1}$;

“自转”可以认为是“公转”引起的. 在“公转”过程中, 接触点经过的长度 (弧 $M M_{0}$ 的长度) 由“自转”提供 (弧 $M_{0} M_{1}$ 的长度), 因此弧 $M M_{0}$ 的长度与弧 $M_{0} M_{1}$ 的长度相等. (可以逆着滚动过程观察) 因为小圆的半径为大圆半径的 $\frac{1}{2}$, 因此 $\theta_{2}=2 \theta_{1}$, 于是点 $M_{1}$ 在直线 $M N$ 上.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-177.jpg?height=298&width=292&top_left_y=1447&top_left_x=1587)

图 3

又 $M_{1} N_{1}$ 为直径, 因此 $N N_{1} \perp M N$. 这样就得到了所求的轨迹, 如图 3.

接下来, 原问题给的是半径比为 $2: 1$ 的情形, 下面给出当半径比发生变化时的不同轨迹.

如半径比为 $3: 1$ 时, 如图 4, 而半径比为 $4: 1$ 时, 如图 5; 半径比是 $5: 2$ 时, 如图 6 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-177.jpg?height=298&width=305&top_left_y=2050&top_left_x=524)

图 4

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-177.jpg?height=300&width=292&top_left_y=2052&top_left_x=885)

图 5

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-177.jpg?height=300&width=292&top_left_y=2052&top_left_x=1240)

图 6

## 第 730 题 德艺双馨

在平面直角坐标系 $x O y$ 的第一象限内有一点 $P$, 满足 $O P=1$ 且直线 $O P$ 的倾斜角为 $30^{\circ}$, 过点 $P$任意作一条直线分别交 $x$ 轴、 $y$ 轴于点 $M, N$, 求 $O M+O N-M N$ 的最大值.

解析 先从几何层面分析最大值在何时取得, 然后从代数层面进行计算.

几何分析 过点 $P$ 作与 $x$ 轴, $y$ 轴均相切的圆 $I$ (取半径较小者), 设与 $x$ 轴, $y$ 轴分别相切于 $A, B$ 两点,圆 $I$ 的半径为 $r$, 如图.

当过点 $P$ 的直线 $M N$ 与圆 $I$ 相交时, 设与直线 $M N$ 平行的切线 $M^{\prime} N^{\prime}$ 分别交 $x$ 轴、 $y$ 轴于 $M^{\prime}, N^{\prime}$ 两点, 切点为 $T$. 那么有

$O M^{\prime}+O N^{\prime}-M^{\prime} N^{\prime}=O A+A M^{\prime}+O B+B N^{\prime}-\left(M^{\prime} T+N^{\prime} T\right)=2 r$.

作平行四边形 $M M^{\prime} Q N$, 则可得

$$
\begin{aligned}
O M^{\prime}+O N^{\prime}-(O M+O N) & =M M^{\prime}+N N^{\prime} \\
& =N Q+N N^{\prime} \\
& >N^{\prime} Q=M^{\prime} N^{\prime}-M N
\end{aligned}
$$

从而有 $O M+O N-M N<2 r$. 而当过点 $P$ 的直线与圆 $I$ 相切于 $P$ 点

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-178.jpg?height=428&width=512&top_left_y=740&top_left_x=1235)
时, 有 $O M+O N-M N=2 r$,

因此所求的最大值即 $2 r$.

代数计算 设 $\triangle M O N$ 内切圆的圆心为 $C(r, r)$, 而 $P\left(\cos 30^{\circ}, \sin 30^{\circ}\right)$, 于是

$$
\left(r-\cos 30^{\circ}\right)^{2}+\left(r-\sin 30^{\circ}\right)^{2}=r^{2},
$$

即

$$
r^{2}-2\left(\sin 30^{\circ}+\cos 30^{\circ}\right) r+1=0
$$

解得 $r=\sin 30^{\circ}+\cos 30^{\circ}-\sqrt{\sin 60^{\circ}}$, 从而题中所求为 $2 r=1+\sqrt{3}-\sqrt[4]{12}$.

思考与总结

当题中的 $\angle P O x$ 改为 $\theta$ 时, 有最大值

$$
m(\theta)=2(\sin \theta+\cos \theta-\sqrt{\sin 2 \theta}) ;
$$

当 $\theta$ 在 $\left[0, \frac{\pi}{2}\right]$ 内变化时, $m(\theta)$ 的取值范围为 $[2(\sqrt{2}-1), 2]$.

## 第 731 题 变化中的不变量

如图 1, 将边长为 1 的正方形纸片沿经过其中心的直线对折, 求对折后的纸片所能覆盖的最大面积.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-178.jpg?height=199&width=205&top_left_y=2114&top_left_x=1500)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-178.jpg?height=202&width=199&top_left_y=2374&top_left_x=1544)

图 2

$$
a+b+c=1, a^{2}+b^{2}=c^{2},
$$

消去 $c$ 得

$$
\frac{1}{2}=a+b-a b \geqslant 2 \sqrt{a b}-a b
$$

从而

$$
\sqrt{a b} \leqslant \frac{2-\sqrt{2}}{2}
$$

因此小三角形面积的最大值为

$$
\frac{1}{2}\left(\frac{2-\sqrt{2}}{2}\right)^{2}=\frac{3-2 \sqrt{2}}{4}
$$

当 $a=b=1-\frac{\sqrt{2}}{2}, c=\sqrt{2}-1$ 时取得. 因此所求的最大值为 $2-\sqrt{2}$.

## 思考与总结

因为折叠相当于正方形绕着其中心旋转一定的角度, 利用这个特点可以证明得到的小三角形全等.

## 第 732 题函数模型

如图 1, 已知等腰 $\triangle A B C$ 的底 $B C$ 长为 6 , 腰 $A B$ 长为 5 . 设 $D$ 是底边 $B C$ 上一点, 以 $A D$ 为边向两边作等边 $\triangle A D E$, 等边 $\triangle A D F$, 设 $D E, D F$ 分别交 $A B, A C$ 于点 $M, N$, 求证: 当 $D$ 位于 $B C$ 中点时 $D M+D N$ 取得最小值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-179.jpg?height=221&width=314&top_left_y=1244&top_left_x=1526)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-179.jpg?height=213&width=312&top_left_y=1530&top_left_x=1565)

图 2

如图 2, 作 $A H \perp B C$ 于点 $H$, 则 $\angle D A H=x$, 于是

$$
B D=3+4 \tan x, C D=3-4 \tan x
$$

而

$$
\frac{D M}{\sin B}=\frac{B D}{\sin \left(B+\frac{\pi}{6}-x\right)}, \frac{D N}{\sin C}=\frac{C D}{\sin \left(C+\frac{\pi}{6}+x\right)}
$$

于是

$$
\begin{aligned}
\frac{D M+D N}{\sin B} & =\frac{3+4 \tan x}{m \cos x-n \sin x}+\frac{3-4 \tan x}{m \cos x+n \sin x} \\
& =\frac{6 m \cos ^{2} x+8 n \sin ^{2} x}{\cos x\left(m^{2} \cos ^{2} x-n^{2} \sin ^{2} x\right)}
\end{aligned}
$$

其中 $m=\sin \left(B+\frac{\pi}{6}\right), n=\cos \left(B+\frac{\pi}{6}\right)$.

因此当 $x=0$ 时, $D M+D N$ 取得最小值, 此时 $D$ 位于 $B C$ 的中点.

解法二 在 $D E$ 上取 $D G=F N$, 则 $\triangle A D N$ 与 $\triangle A E G$ 全等, 如图 3.

因此

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-179.jpg?height=216&width=325&top_left_y=2312&top_left_x=1553)

图 3

$$
D M+D N=D M+G E=D E+G M=A D+G M,
$$

而当 $D$ 位于 $B C$ 中点时, $A D$ 和 $G M$ 同时取得最小值 (注意 $G$ 点的轨迹是延长线通过点 $A$ 的线段).

思考与总结

因为 $\angle C A G=\frac{\pi}{3}-\angle B A G$, 所以 $\angle B A G$ 为定值. 当 $A D$ 减小时, $\angle A G D$ 增大, 在 $\triangle G A D$ 中, $A G$ 减小;在 $\triangle M A G$ 中, $\angle G M A$ 增大,所以 $M G$ 减小.

## 第 733 题 圆上动点

在平面直角坐标系 $x O y$ 中, 点 $B$ 为曲线 $y=\sqrt{1-x^{2}}$ 上的动点, $A(2,0)$, 点 $C$ 位于第一象限且 $\triangle A B C$ 为等腰直角三角形, 且 $A$ 为直角顶点, 则线段 $O C$ 长度的最大值为

解析 $1+2 \sqrt{2}$.

解法一 分两类讨论.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-180.jpg?height=215&width=314&top_left_y=1114&top_left_x=563)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-180.jpg?height=213&width=327&top_left_y=1112&top_left_x=957)

图 2

当四边形 $O A C B$ 为凸四边形时, 如图 1, 根据广义托勒密定理, 有

$$
O C \cdot A B \leqslant O B \cdot A C+O A \cdot B C=A B+2 \sqrt{2} A B
$$

于是 $O C \leqslant 1+2 \sqrt{2}$, 等号当 $O, A, C, B$ 四点共圆时取得, 于是此时 $O C$ 的最大值为 $1+2 \sqrt{2}$. 当四边形 $O A C B$ 不是凸四边形时, 如图 2. 有

$$
O C \leqslant O B+B C=O B+\sqrt{2} A C<O B+\sqrt{2} O A=1+2 \sqrt{2}
$$

解法二 也可以利用轨迹, 如图 3 , 点 $C$ 的运动轨迹是以 $D(2,2)$ 为圆心的半圆弧

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-180.jpg?height=346&width=330&top_left_y=1376&top_left_x=1438)

图 3 (考虑 $\triangle O A B$ 绕 $A$ 点按顺时针方向旋转 $90^{\circ}$ 得到 $\triangle D A C$ ), 于是 $O C$ 的最大值为 $1+2 \sqrt{2}$.

## 第 734 题 正方形与抛物线

如图 1, 将一张边长为 1 的正方形纸 $A B C D$ 折叠, 使得点 $B$ 始终落在边 $A D$上,则折起部分面积的最小值为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-180.jpg?height=300&width=295&top_left_y=2053&top_left_x=1434)

图 1

解析 $\frac{3}{8}$.
如图 2 , 设 $A B^{\prime}=x(0 \leqslant x \leqslant 1)$.

则由相似三角形可得

$$
\frac{B E}{B B^{\prime}}=\frac{\frac{1}{2} B B^{\prime}}{A B}
$$

从而

$$
B E=\frac{B B^{\prime 2}}{2 A B}=\frac{1}{2}\left(1+x^{2}\right)
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-181.jpg?height=300&width=442&top_left_y=197&top_left_x=1419)

图 2

而继续由相似三角形可得

$$
\frac{B E-C F}{B E}=\frac{B C}{B G}
$$

从而

$$
B E-C F=B C \cdot \frac{B E}{B G}=\frac{A B^{\prime}}{A B}=x
$$

解得

$$
C F=\frac{1}{2}\left(1+x^{2}\right)-x
$$

因此

$$
S_{E B C F}=\frac{1}{2}(B E+C F) \cdot B C=\frac{1}{2}\left(x^{2}-x+1\right) \geqslant \frac{3}{8},
$$

等号当且仅当 $x=\frac{1}{2}$ 时取得.

## 第 735 题 $\quad$ 不动如山,动若雷震

已知 $\triangle A B C$ 满足 $\angle B A C=\frac{\pi}{3},(\overrightarrow{A B}+\overrightarrow{A C}) \cdot \overrightarrow{B C}=0$, 点 $M$ 在 $\triangle A B C$ 外, 且 $M B=2 M C=2$, 则 $M A$的取值范围是

## 解析 $[1,3]$.

解法一 易知 $\triangle A B C$ 为正三角形, 如图 1, 设 $M A=x, A B=B C=C A=t$, 那么应用托勒密定理可得.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-181.jpg?height=263&width=249&top_left_y=1902&top_left_x=630)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-181.jpg?height=309&width=290&top_left_y=1857&top_left_x=1115)

图 2

解法二 易知 $\triangle A B C$ 为正三角形, 如图 2, 先固定 $B, M$, 使得 $B M=2$, 然后让点 $C$ 在半径为 1 的圆 $M$ 上运动, 观察 $A$ 点的轨迹 (暂时忽略点 $M$ 在 $\triangle A B C$ 外的条件).

由平面几何知识容易得到点 $A$ 的轨迹是圆 $M$ 绕点 $B$ 按逆时针方向旋转 $60^{\circ}$ 后得到的圆 $N$, 据此容易求得 $M A$ 的取值范围是 $[1,3]$ (注意取得最值时点 $M$ 均在 $\triangle A B C$ 外部).

## 第九章 $\quad$ 立体几何

## 第 736 题 $\quad$ 无底三棱柱

设 $l_{1}, l_{2}, l_{3}$ 为空间中互相平行且两两间的距离分别为 $4,5,6$ 的直线. 给出下列三个结论:

(1) 存在 $A_{i} \in l_{i}(i=1,2,3)$, 使得 $\triangle A_{1} A_{2} A_{3}$ 是直角三角形;

(2) 存在 $A_{i} \in l_{i}(i=1,2,3)$, 使得 $\triangle A_{1} A_{2} A_{3}$ 是等边三角形;

(3)三条直线上存在四点 $A_{i}(i=1,2,3,4)$, 使得四面体 $A_{1} A_{2} A_{3} A_{4}$ 为在一个顶点处的三条棱两两互相垂直的四面体.

其中,所有正确结论的序号是

解析 (1)(2).

如图, 设直线 $l_{1}, l_{2}, l_{3}$ 分别为“无底之直三棱柱”的三条 “侧棱” $A D, B E, C F$, 且平面 $A B C$ 与侧棱垂直, $A B=4, B C=5, C A=6$.

(1) 当 $A_{1}=A$ (表示点 $A_{1}$ 与点 $A$ 重合, 下同) , $A_{2}=B, A_{3}=C$ 时, $\angle A_{1} A_{2} A_{3}<\frac{\pi}{2}$; 当 $A_{1}$ 向下运动, $A_{3}$ 向上运动时, $\angle A_{1} A_{2} A_{3}$ 趋于 $\pi$; 因此必然在某个时刻 $\angle A_{1} A_{2} A_{3}=\frac{\pi}{2}$,命题成立;

(2)取 $A_{2}=B, A_{1}$ 位于 $A$ 点上方且 $A_{1} A=3, A_{3}=C$, 则 $A_{1} A_{2}=A_{2} A_{3}=5, A_{1} A_{3}>6$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-182.jpg?height=452&width=316&top_left_y=1051&top_left_x=1449)
此时 $\angle A_{1} A_{2} A_{3}>\frac{\pi}{3}$; 让 $A_{1}, A_{3}$ 同时向上运动, 且保持 $A_{1} A_{2}=A_{3} A_{2}$, 则 $\angle A_{1} A_{2} A_{3}$ 趋于 0 , 必然存在某个时刻 $\angle A_{1} A_{2} A_{3}=\frac{\pi}{3}$, 命题成立;

(3) 显然四个点中有两个点位于同一条直线上, 设为 $A_{1}, A_{2}$, 另外两点分别落在其他两条直线上. $A_{3}, A_{4}$显然不可能为直角顶点, 因此 $A_{1}$ 或 $A_{2}$ 为直角顶点, 不妨设 $A_{1}$ 为直角顶点, 则 $A_{3} A_{1} \perp A_{1} A_{2}, A_{4} A_{1} \perp A_{1} A_{2}$,因此 $\angle A_{3} A_{1} A_{4}$ 为二面角的平面角, 且其大小与 $\triangle A B C$ 的某个内角相同, 不可能为 $\frac{\pi}{2}$. 因此不可能存在符合题意的四面体.

综上所述,命题(1)2正确.

## 第 737 题 $\quad$ 捚一扭

一个多面体的三视图如图 1 所示, 其中俯视图中内部的小正方形边长为 1 , 求该多面体的体积.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-182.jpg?height=414&width=470&top_left_y=2114&top_left_x=1260)

图 1
解析 根据题意,该多面体的直观图如图 2 所示, 为 $E F G H-A B C D$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-183.jpg?height=306&width=417&top_left_y=349&top_left_x=501)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-183.jpg?height=407&width=338&top_left_y=244&top_left_x=1195)

图 3

为了方便计算体积, 我们计算它的四分之一 $P F G-O B C$, 其中 $O, P$ 分别为下底面和上底面的中心, 如图 3.

根据题意, 有

$$
\begin{aligned}
V_{P F G-O B C} & =V_{O-P F G}+V_{F-C O B}+V_{G-O B C} \\
& =\frac{1}{3} \cdot S_{\triangle P F G} \cdot O P+\frac{1}{6} \cdot F G \cdot O B \cdot O P \cdot \sin \langle F G, O B\rangle+\frac{1}{3} \cdot S_{\triangle O B C} \cdot O P
\end{aligned}
$$

如图 4, 设 $A E=B F=x$, 则在直角 $\triangle A B E$ 中, 有

$$
x^{2}+(1+x)^{2}=9
$$

解得

$$
x=\frac{\sqrt{17}-1}{2}
$$

于是

$$
O B \cdot \sin \langle F G, O B\rangle=\frac{\sqrt{17}}{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-183.jpg?height=349&width=354&top_left_y=1004&top_left_x=1506)

图 4

因此

$$
V_{P F G-O B C}=\frac{5}{3}+\frac{\sqrt{17}}{6}
$$

进而可得

$$
V_{E F G H-A B C D}=4 V_{P F G-O B C}=\frac{20}{3}+\frac{2 \sqrt{17}}{3}
$$

## 第 738 题 从空间回到平面

已知点 $A, B$ 分别为异面直线 $a, b$ 上的点, 且直线 $A B$ 与 $a, b$ 均垂直, 动点 $P \in a, Q \in b, P A+Q B$ 为定值,则线段 $P Q$ 中点 $M$ 的轨迹是
A. 平行四边形
B. 圆
C. 椭圆
D. 双曲线

解析 $\mathrm{A}$.

作直线 $a, b$ 以及点 $P, Q$ 在线段 $A B$ 的中垂面上的投影, 记为直线 $a^{\prime}, b^{\prime}$ 以及点 $P^{\prime}, Q^{\prime}$, 则线段 $P^{\prime} Q^{\prime}$ 的中点即点 $M$, 这样就把空间的问题转化成平面上的问题, 如图.

设 $P A+Q B=2 m$, 而 $O E=O F=O G=O H=m$. 以 $P^{\prime}, Q^{\prime}$ 分别在射线 $O F, O E$ 上为例.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-183.jpg?height=278&width=518&top_left_y=2256&top_left_x=1345)

由

$$
O P^{\prime}+O Q^{\prime}=A P+B Q=2 m,
$$

以及 $O E+O F=2 m$, 可得 $F P^{\prime}=E Q^{\prime}$.

过点 $P^{\prime}$ 作直线 $E F$ 的平行线交直线 $b^{\prime}$ 于点 $R$, 则有

$$
F P^{\prime}=E R=E Q^{\prime},
$$

于是线段 $P^{\prime} Q^{\prime}$ 的中点 $M$ 在线段 $E F$ 上.

类似的, 可得其他情形时点 $M$ 的轨迹分别为线段 $F G, G H, H E$.

综上所述,线段 $P Q$ 中点 $M$ 的轨迹是矩形 $E F G H$. 故选 A.

## 思考与总结

也可以从向量说明点 $M$ 的轨迹, 在平面上有 $O P^{\prime}+O Q^{\prime}=2 m$ 为定值, 点 $M$ 满足

$$
\overrightarrow{O M}=\frac{1}{2}\left(\overrightarrow{O P^{\prime}}+\overrightarrow{O Q^{\prime}}\right)=\frac{\left|O P^{\prime}\right|}{2 m} \cdot\left(m \boldsymbol{e}_{1}\right)+\frac{\left|O Q^{\prime}\right|}{2 m} \cdot\left(m \boldsymbol{e}_{2}\right)
$$

其中 $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}$ 表示 $\overrightarrow{O P^{\prime}}, \overrightarrow{O Q^{\prime}}$ 方向上的单位向量. 于是由

$$
\frac{\left|O P^{\prime}\right|}{2 m}+\frac{\left|O Q^{\prime}\right|}{2 m}=1, \frac{\left|O P^{\prime}\right|}{2 m} \geqslant 0, \frac{\left|O Q^{\prime}\right|}{2 m} \geqslant 0
$$

知,点 $M$ 的轨迹为线段,线段端点为起点在 $O$ 的向量 $m \boldsymbol{e}_{1}, m \boldsymbol{e}_{2}$ 的终点.

## 第 739 题 立方㑛中的动点

已知棱长为 2 的正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的中心为 $O, P$ 是正方体表面上一点, 且直线 $O P$ 与直线 $A B_{1}$ 所成的角为 $\frac{\pi}{4}$, 求 $O P$ 的取值范围.

解析 如图 1, 设 $M, N, P, Q$ 分别为 $B_{1} C_{1}, A D, A_{1} D_{1}, B C$ 的中点, 则 $P$ 点的轨迹是以 $M N$ 为轴, $O$ 点为母线与轴的公共点, $\alpha=\frac{\pi}{4}$ 的圆锥面被正方体的表面截得的截线. 根据对称性, 只需要考虑平面 $A_{1} C_{1}$ 与平面 $C D_{1}$ 截圆锥而形成的截线.

显然 $E F, G H$ 是圆锥面的两条母线, 作与 $E F, G H, M P$ 均相切的圆, 设该圆与 $M P$ 相切于点 $K$. 考虑圆锥面的轴 $M N$ 与平面 $A_{1} C_{1}$ 形成的线面角大小 $\beta_{1}=\frac{\pi}{4}$, 于是平面 $A_{1} C_{1}$ 上的截线为抛物线 $S T$, 且以 $K$ 为焦点, 以底面 $A_{1} C_{1}$ 的中心 $E$ 为顶点. 容易求得 $S, T$ 为边 $C_{1} D_{1}, B_{1} A_{1}$ 上靠近点 $C_{1}, B_{1}$ 的四等分点, 如图 2 所示.

类似的, 由于圆锥面的轴 $M N$ 与平面 $C_{1} D$ 形成的线面角大小 $\beta_{2}=0$, 于是平面 $C_{1} D$上的截线为离心率等于 $\sqrt{2}$ 的双曲线. 显然双曲线与棱的公共点亦为抛物线与棱的公共点, 不难得知所求的取值范围即 $[O E, O S]$, 即 $\left[1, \frac{3}{2}\right]$.

## 第 740 题 阿波罗尼斯球

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-184.jpg?height=368&width=373&top_left_y=1549&top_left_x=1389)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-184.jpg?height=305&width=292&top_left_y=1960&top_left_x=1473)

图 2

在四面体 $A B C D$ 中, 已知 $A D \perp B C, A D=6$, 且 $\frac{A B}{B D}=\frac{A C}{C D}=2$, 则四面体 $A B C D$ 的体积的最大值为
解析 16 .

由于 $\frac{A B}{B D}=\frac{A C}{C D}=2$, 于是点 $B$, 点 $C$ 在以 $E F$ 为直径的球 $O$ 的表面上, 其中

$$
\overrightarrow{A E}=2 \overrightarrow{E D}, \overrightarrow{A F}=-2 \overrightarrow{F D}
$$

如图 1, 过 $B C$ 作与 $A D$ 垂直的平面得到圆 $H$, 则点 $H$ 必然在直线 $A D$ 上. 此时四面体 $A B C D$ 的体积为

$$
\frac{1}{3} S_{\triangle B C H} \cdot A D=B H^{2} \cdot \sin \angle B H C \leqslant 16
$$

等号当 $B H=4$ 且 $\angle B H C=90^{\circ}$ 时取得, 也即点 $H$ 与点 $O$ 重合, $\angle B O C$ 为直角时取得. 因此四面体 $A B C D$ 的体积的最大值为 16 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-185.jpg?height=453&width=145&top_left_y=197&top_left_x=1632)

图 1

此题为阿波罗尼斯圆的升级版本, 在平面上, 满足 $\frac{A B}{B D}=2$ 的动点 $B$ 的轨迹为阿波罗尼斯圆，如图 2 所示:

故点 $B$ 到 $A D$ 的距离的最大值为该圆的半径 4 , 当点 $H$ 与球心 $O$ 重合, 且二面角 $C-A D-B$ 为直二面角时, 四面体的体积取到最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-185.jpg?height=221&width=333&top_left_y=829&top_left_x=1524)

图 2

## 第 741 题 相对运动

棱长为 2 的正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 在空间直角坐标系 $O-x y z$ 中运动, 其中顶点 $A$ 保持在 $z$轴上, 顶点 $B_{1}$ 保持在平面 $x O y$ 上, 则 $O C$ 长度的最小值是

解析 $\sqrt{6}-\sqrt{2}$.

考虑让正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 静止, 坐标系运动. 由于 $O A \perp O B_{1}$, 于是 $O$ 点在以 $A B_{1}$ 为直径的球面上运动. 设该球面的球心为 $M$, 则其半径

$$
r=M A=\frac{1}{2} A B_{1}=\sqrt{2}
$$

而 $M C=\sqrt{6}$, 因此 $O C$ 长度的最小值为

$$
|M C-r|=\sqrt{6}-\sqrt{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-185.jpg?height=314&width=358&top_left_y=1591&top_left_x=1520)

## 第 742 题 小橄榄长成大南瓜

如图 1, 在长方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 中, $A B=B C=2, A A_{1}=1, E 、 F$ 为对角线 $B D_{1}$ 的两个三等分点, $G$ 为长方体表面上的动点, 则 $\angle E G F$ 的最大值为 . $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-185.jpg?height=221&width=382&top_left_y=2184&top_left_x=1456)

图 1

解析 $90^{\circ}$.

显然 $E F$ 是定长的线段,长度为

$$
\frac{1}{3} \sqrt{2^{2}+2^{2}+1}=1
$$

我们知道, 在平面上对定长的线段所张的角为定角的点的轨迹是两段圆弧, 即“等张角线”. 如图 2, 在平面“等张角线”逐步扩张的过程中, 对应的定角逐步减小(可以由正弦定理推得).

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-186.jpg?height=216&width=352&top_left_y=498&top_left_x=479)

图 2 平面等张角线

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-186.jpg?height=286&width=349&top_left_y=414&top_left_x=1024)

图 3 空间等张角面

于是空间的“等张角线”如图 3 所示, 由圆弧绕线段旋转而成, 类似于“橄榄”到球体再到“南瓜”, 它的任何一个轴截面都是平面等张角线.

回到原问题,想象一个“橄榄” (从线段 $E F$ 开始)逐步膨胀 (到球再到“南瓜”), 在膨胀过程中, 空间等张角面对应的定角持续减小, 因此第一次和长方体的表面相切时, 切点就是使得 $\angle E G F$ 最大的 $G$ 点的位置.

接下来, 由于长方体和空间等张角面均关于线段 $E F$ 的中点对称, 于是空间等张角面会依次与长方体的三组对面相切, 并且切点在长方体的某个对角面上, 因此逐一分析对角面 $B D D_{1} B_{1}, A_{1} B C D_{1}, A B C_{1} D_{1}$ 的情形即可, 如图 4.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-186.jpg?height=226&width=1140&top_left_y=1146&top_left_x=348)

图 4

如图 5, 对角面 $B D D_{1} B_{1}$ 对应的切点为上下底面的中心, 所得的 $\angle E G F=90^{\circ}$, 此时空间等张角面为球面；

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-186.jpg?height=134&width=311&top_left_y=1571&top_left_x=543)

图 5

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-186.jpg?height=224&width=260&top_left_y=1479&top_left_x=1049)

图 6

如图 6, 对角面 $A_{1} B C D_{1}$ 对应的切点分别在面对角线 $A_{1} B$ 和 $D_{1} C$ 上, 所得 $\angle E G F<90^{\circ}$, 此时空间等张角面是“南瓜面”; 与此同时对角面 $A B C_{1} D_{1}$ 的边 $A D_{1}$ 和 $B C_{1}$ 上也有切点.

综上, 所求 $\angle E G F$ 的最大值为 $90^{\circ}$, 当且仅当点 $G$ 位于上下底面的中心时取得最大值.

## 第 743 题 $\quad$ 运动中的不变量

如图 1, 直线 $m$ 与平面 $\alpha$ 垂直, 垂足是 $O$, 正四面体 $A B C D$ 的棱长为 4 , 点 $C$ 在平面 $\alpha$ 上运动, 点 $B$ 在直线 $m$ 上运动, 则点 $O$ 到直线 $A D$ 的距离的取值范围是
А. $\left[\frac{4 \sqrt{2}-5}{2}, \frac{4 \sqrt{2}+5}{2}\right]$
B. $[2 \sqrt{2}-2,2 \sqrt{2}+2]$
C. $\left[\frac{3-2 \sqrt{2}}{2}, \frac{3+2 \sqrt{2}}{2}\right]$
D. $[3 \sqrt{2}-2,3 \sqrt{2}+2]$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-186.jpg?height=249&width=451&top_left_y=2179&top_left_x=1281)

图 1

## 解析 B.

问题的关键是正确把握运动中的不变量. 事实上, 看起来非常复杂的 $B, C$ 两个点的运动, 在其运动过程中, $O B$ 与 $O C$ 的垂直关系是始终不变的. 因此, 我们可以将正四面体 $A B C D$ 固定下来,而点 $O$ 在以 $B C$ 为直径的球面上运动,如图 2.

接下来可以得到所求的点 $O$ 到直线 $A D$ 的距离的取值范围就是球心到直线 $A D$的距离减去球的半径, 与球心到直线 $A D$ 的距离加上球的半径之间, 不难求出该取值范围是 $[2 \sqrt{2}-2,2 \sqrt{2}+2]$. 故选 B.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-187.jpg?height=322&width=333&top_left_y=196&top_left_x=1522)

图 2

## 第 744 题 $\quad$ 正方使中的轨迹长度

已知正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的棱长为 1 , 动点 $P$ 在正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的表面上运动,且 $P A=r(0<r<\sqrt{3})$. 记点 $P$ 的轨迹的长度为 $f(r)$.

(1) 求 $f\left(\frac{1}{2}\right)$;

(2) 求出关于 $r$ 的方程 $f(r)=k$ 的解的个数的所有可能的值, 并说明理由.

解析 (1) 由于正方体绕其体对角线旋转 $120^{\circ}$ 后仍与自身重合, 于是 $f(r)$ 为点 $P$ 在正方体的侧面 $A B B_{1} A_{1}$ 与 $B C C_{1} B_{1}$ 上的轨迹长度之和的 3 倍. 将右侧面 $B C C_{1} B_{1}$ 翻折至与侧面 $A B B_{1} A_{1}$重合, 如图. 稍加探索可以发现 $r=1$ 和 $r=\sqrt{2}$ 是两个分界点.

当 $0<r \leqslant 1$ 时, 有 $f(r)=\frac{3 r \pi}{2}$, 于是 $f\left(\frac{1}{2}\right)=\frac{3 \pi}{4}$.

(2) 当 $\sqrt{2} \leqslant r<\sqrt{3}$ 时, 图中弧的半径为 $\sqrt{r^{2}-1}$, 所对的圆心角

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-187.jpg?height=347&width=660&top_left_y=1152&top_left_x=1197)

图 1 为 $\frac{\pi}{2}-2 \arccos \frac{1}{\sqrt{r^{2}-1}}$, 记 $\theta=\arccos \frac{1}{\sqrt{r^{2}-1}}$, 其中 $\theta \in\left[0, \frac{\pi}{4}\right)$,则对应的弧长

$$
l(\theta)=\left(\frac{\pi}{2}-2 \theta\right) \cdot \frac{1}{\cos \theta}
$$

其导函数

$$
l^{\prime}(\theta)=\frac{-2-2 \theta \tan \theta+\frac{\pi}{2} \tan \theta}{\cos \theta}<0
$$

于是随着 $r$ 的增大, $\theta$ 随之增大, 对应的弧长随之减小, $f(r)$ 随之减小.

当 $1<r<\sqrt{2}$ 时, 设 $\theta=\arccos \frac{1}{r}$, 其中 $\theta \in\left(0, \frac{\pi}{4}\right)$, 则弧长之和

$$
h(\theta)=\left(\frac{\pi}{2}-2 \theta\right) \cdot \frac{1}{\cos \theta}+\frac{\pi}{2} \cdot \tan \theta=\frac{\pi}{2} \cdot \frac{\sin \theta-\frac{4}{\pi} \theta+1}{\cos \theta}
$$

于是

$$
h^{\prime}(\theta)=\frac{\pi}{2} \cdot \frac{1+\sin \theta-\frac{4}{\pi}(\cos \theta+\theta \cdot \sin \theta)}{\cos ^{2} \theta}
$$

设

$$
\varphi(\theta)=1+\sin \theta-\frac{4}{\pi}(\cos \theta+\theta \cdot \sin \theta)
$$

则 $\varphi(0)=1-\frac{4}{\pi}<0, \varphi\left(\frac{\pi}{4}\right)=1-\frac{4}{\pi} \cdot \frac{\sqrt{2}}{2}>0$, 而

$$
\varphi^{\prime}(\theta)=\cos \theta \cdot\left(1-\frac{4}{\pi} \theta\right)>0
$$

因此 $\varphi(\theta)$ 在 $\left(0, \frac{\pi}{4}\right)$ 上先负后正, 对应的 $h(\theta)$ 在 $\left(0, \frac{\pi}{4}\right)$ 先递减再递增.

这样我们就可以勾勒出函数 $f(r)$ 的图象如图 2.

于是方程 $f(r)=k$ 的解的个数的所有可能值为 $0,2,3,4$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-188.jpg?height=426&width=439&top_left_y=205&top_left_x=1309)

图 2

## 第 745 题 解三角形

在空间中, 过点 $A$ 作平面 $\pi$ 的垂线, 垂足为 $B$, 记 $B=f_{\pi}(A)$, 设 $\alpha, \beta$ 是两个不同的平面, 对空间任意一点 $P, Q_{1}=f_{\beta}\left[f_{\alpha}(P)\right], Q_{2}=f_{\alpha}\left[f_{\beta}(P)\right]$, 恒有 $P Q_{1}=P Q_{2}$, 则

A. 平面 $\alpha$ 与平面 $\beta$ 垂直

B. 平面 $\alpha$ 与平面 $\beta$ 所成的 (锐) 二面角为 $45^{\circ}$

C. 平面 $\alpha$ 与平面 $\beta$ 平行

D. 平面 $\alpha$ 与平面 $\beta$ 所成的 (锐) 二面角为 $60^{\circ}$

## 解析 A.

将 $P$ 取在平面 $\alpha$ 内即得, 接下来我们证明这个结论.

如图, 只需要在过点 $P$ 且与直线 $\alpha \cap \beta$ 垂直的截面内思考问题. 设 $\angle P O_{\alpha}=x$, $\angle P O \beta=y, O P=1$, 则

$$
P M=\sin x, M Q_{1}=\cos x \sin (x+y),
$$

于是在 $\triangle P M Q_{1}$ 中应用余弦定理, 有

$$
P Q_{1}^{2}=\sin ^{2} x+[\cos x \sin (x+y)]^{2}-2 \sin x \cos x \sin (x+y) \cos (x+y),
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-188.jpg?height=332&width=367&top_left_y=1371&top_left_x=1386)

类似的, 可得

$$
P Q_{2}^{2}=\sin ^{2} y+[\cos y \sin (x+y)]^{2}-2 \sin y \cos y \sin (x+y) \cos (x+y),
$$

因此

$$
\sin ^{2} x-\sin ^{2} y+\left(\cos ^{2} x-\cos ^{2} y\right) \sin ^{2}(x+y)-(\sin 2 x-\sin 2 y) \sin (x+y) \cos (x+y)=0,
$$

即

$$
\left(\sin ^{2} x-\sin ^{2} y\right) \cos ^{2}(x+y)=0,
$$

于是可得 $x+y=\frac{\pi}{2}$, 因此 $\alpha \perp \beta$.

综上所述, 正确的选项为 A.

## 第 746 题

已知 $\triangle A B C$ 的周长为 $2 p$, 求以 $\triangle A B C$ 的某条边所在的直线为轴构成的旋转体的体积的最大值.
解析 设角 $A, B, C$ 所对的边长分别为 $a, b, c$. 不妨设旋转体的轴过 $A B$, 先固定边 $A B$ 的长 $c$, 则 $C$ 点在以 $A, B$ 为焦点, $2 p-c$ 为长轴长的椭圆上运动.

设点 $C$ 到直线 $A B$ 的距离为 $h$, 则构成的旋转体的体积

$$
V=\frac{1}{3} \pi h^{2} c
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-189.jpg?height=254&width=218&top_left_y=200&top_left_x=1655)

易知当 $a=b=p-\frac{1}{2} c$ 时, $h$ 取得最大值, 因此有

$$
V \leqslant \frac{1}{3} \pi\left[\left(p-\frac{1}{2} c\right)^{2}-\left(\frac{1}{2} c\right)^{2}\right] c=\frac{\pi}{3} p(p-c) c \leqslant \frac{\pi}{3} p\left(\frac{p}{2}\right)^{2}=\frac{\pi}{12} p^{3}
$$

等号当 $c=\frac{p}{2}, a=b=\frac{3}{4} p$ 时取得. 因此所求的最大值为 $\frac{\pi}{12} p^{3}$.

## 第 747 题 透过现象看本质

如图 1 所示, 在正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 中, 点 $E$ 是边 $B C$ 的中点. 点 $P$ 在直线 $B D_{1}$ (除 $B, D_{1}$ 两点) 上运动的过程中, 平面 $D E P$ 可能经过的该正方体的顶点是 $\qquad$ . (写出满足条件的所有顶点)

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-189.jpg?height=259&width=287&top_left_y=1002&top_left_x=1547)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-189.jpg?height=276&width=290&top_left_y=1334&top_left_x=1585)

图 2

解标 $A_{1}, B_{1}, D$.

将正方体的顶点逐一代人验证是得到答案的简捷方法,可得答案是 $A_{1}, B_{1}, D$.

如何确定平面 $D E P$ 可能经过的该正方体表面的所有的点呢? 先将问题从正方体中抽离出来, 也即 $\triangle A B C$ 中, $A B$ 为固定的线段, 点 $C$ 在与直线 $A B$ 异面的直线 $l$ 上运动,那么 $\triangle A B C$ 所在平面扫过的空间区域是什么样子的?

如图 2, 不难想象, $\triangle A B C$ 所在平面扫过的空间区域是过直线 $A B$ 且与直线 $l$ 平行的平面将空间划分成的两侧区域中的两侧 (不包含过 $A B$ 与 $l$ 平行的平面, 包含直线 $A B$ ). 回到本问题, 我们只需要过 $D E$ 作与 $B D_{1}$ 平行的平面 $\alpha$, 那么正方体的表面上除去平面 $\alpha$, 平面 $D E D_{1}$ 和平面 $D E B$ 上的点再加上点 $D, E$ 即为所求的所有点.

## 第 748 题 透视原理

如图 1, 平面 $\alpha$ 与平面 $\beta$ 垂直, 直线 $l$ 为两个平面的交线. $A, C$ 是平面 $\alpha$ 内不同的两点, $B, D$ 是平面 $\beta$ 内不同的两点,且 $A, B, C, D \notin l . M, N$ 分别是线段 $A B, C D$ 的中点. 下列判断中正确的是

A. 当 $|C D|=2|A B|$ 时, $M, N$ 两点不可能重合
B. $M, N$ 两点可能重合, 但此时直线 $A C$ 与直线 $l$ 不可能相交

C. 当 $A B$ 与 $C D$ 相交, 直线 $A C$ 平行于 $l$ 时, 直线 $B D$ 可以与 $l$ 相交

D. 当 $A B, C D$ 是异面直线时, $M N$ 可能与 $l$ 平行

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-189.jpg?height=224&width=376&top_left_y=2091&top_left_x=1459)

图 1
依次考虑四个选项.

对于选项 A, 如图 2, 取与 $l$ 平行的平面, 与平面 $\alpha$ 和平面 $\beta$ 分别相交, 在两条交线上取一条线段 $A B$, 然后将这条线段绕其中点 $M$ 旋转, 那么在旋转过程中必然可以找到长度是起始长度 2 倍的位置, 即线段 $C D$. 因此选项 $\mathrm{A}$ 错误.

对于选项 $\mathrm{B}$, 由对选项 $\mathrm{A}$ 的分析可知, 点 $M, N$ 可以重合, 如图 3, 若点 $M$ 与点 $N$ 重合, 那么 $A B$ 与 $C D$ 互相平分, 因此 $A D B C$ 为平行四边形. 对平行四边形所在平面与平面 $\alpha, \beta$ 应用引理即得

$$
A C / / B D / / l
$$

因此选项 B 正确.

对于选项 C, 若 $A B$ 与 $C D$ 相交, 那么它们构成一个平面, 对该平面与平面 $\alpha, \beta$应用引理即得

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-190.jpg?height=226&width=359&top_left_y=209&top_left_x=1391)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-190.jpg?height=229&width=374&top_left_y=529&top_left_x=1389)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-190.jpg?height=227&width=371&top_left_y=909&top_left_x=1382)

图 4

$$
A C / / l / / B D
$$

于是在平面 $\alpha$ 内, 过 $A^{\prime}$ 的平行线 $C A^{\prime}$ 与 $A A^{\prime}$ 重合, 于是点 $A$ 在平面 $A^{\prime} C B^{\prime} D$

因此选项 C 错误.

对于选项 D, 如图 4, 当 $M N$ 与 $l$ 平行时, 将线段 $A B$ 沿向量 $\overrightarrow{M N}$ 平移到 $A^{\prime} B^{\prime}$,则根据对选项 $\mathrm{B}$ 的分析, 有

$$
C A^{\prime} / / B^{\prime} D / / l,
$$

又

$$
A A^{\prime} / / B B^{\prime} / / M N / / l,
$$

内, 类似的, 点 $B$ 也在平面 $A^{\prime} C B^{\prime} D$ 内, 因此 $A B$ 与 $C D$ 共面.

条件“平面 $\alpha$ 与平面 $\beta$ 垂直”是多余的.

透视引理 三个平面两两相交, 则三条交线或者互相平行, 或者交于一点.

证明 设三个平面分别为 $\alpha, \beta, \gamma$, 且 $\alpha \cap \beta=c, \beta \cap \gamma=a, \gamma \cap \alpha=b$.

由于直线 $a$ 与直线 $b$ 共面, 于是 $a$ 与 $b$ 或者平行, 或者相交, 讨论如下.

情形一 当 $a / / b$ 时

此时

$$
\alpha \cap \beta \cap \gamma=\varnothing
$$

于是同在平面 $\alpha$ 内的直线 $b$ 与直线 $c$ 没有公共点, 因此 $b / / c$. 根据平行公理, 有

$$
a / / b / / c
$$

即三条交线互相平行.

情形二 当 $a \cap b=P$ 时

此时

$$
\alpha \cap \beta \cap \gamma=P
$$

于是

$$
(\gamma \cap \alpha) \cap(\alpha \cap \beta)=P
$$

即 $b \cap c=P$, 从而

$$
a \cap b \cap c=P
$$

即三条交线交于一点.

综上,引理得证.

## 第 749 题 直角三棱雉的性质

在三棱雉 $T-A B C$ 中, $T A, T B, T C$ 两两垂直, $T$ 在平面 $A B C$ 上的投影为 $D, O$ 为三棱雉 $T-A B C$内任意一点, 连结 $A O, B O, C O, T O$ 并延长交对面于 $A^{\prime}, B^{\prime}, C^{\prime}, T^{\prime}$, 给出下列命题:

(1) $T A \perp B C, T B \perp A C, T C \perp A B ;$

(2) $\triangle A B C$ 是锐角三角形;

(3) $\frac{1}{T D^{2}}=\frac{1}{T A^{2}}+\frac{1}{T B^{2}}+\frac{1}{T C^{2}}$

(4) $S_{\triangle A B C}^{2}=\frac{1}{3}\left(S_{\triangle T A B}^{2}+S_{\triangle T A C}^{2}+S_{\triangle T B C}^{2}\right)$ (注: $S_{\triangle A B C}$ 表示 $\triangle A B C$ 的面积);

(5) $\frac{O A^{\prime}}{A A^{\prime}}+\frac{O B^{\prime}}{B B^{\prime}}+\frac{O C^{\prime}}{C C^{\prime}}+\frac{O T^{\prime}}{T T^{\prime}}=1$.

其中正确的是 (写出所有正确命题的编号)

解析 (1)(2)(3).

(1)根据题意, 如图 1, 有 $T A \perp$ 平面 $T B C$, 于是 $T A \perp B C$. 同理, $T B \perp C A, T C \perp A B$,命题正确;

(2) 设 $T A=a, T B=b, T C=c$, 则

$$
\begin{aligned}
\cos \angle B A C & =\frac{A B^{2}+A C^{2}-B C^{2}}{2 A B \cdot A C} \\
& =\frac{\left(a^{2}+b^{2}\right)+\left(a^{2}+c^{2}\right)-\left(b^{2}+c^{2}\right)}{2 \sqrt{a^{2}+b^{2}} \cdot \sqrt{a^{2}+c^{2}}} \\
& =\frac{a^{2}}{\sqrt{a^{2}+b^{2}} \cdot \sqrt{a^{2}+c^{2}}} \\
& >0
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-191.jpg?height=327&width=306&top_left_y=1105&top_left_x=1568)

图 1

于是 $\angle B A C$ 为锐角. 同理, $\angle A B C$ 和 $\angle A C B$ 也为锐角, 命题正确;

(3)设 $\triangle A B C$ 的面积为 $S$, 三棱雉 $T-A B C$ 的体积为 $V$. 由(2)得

$$
\sin \angle B A C=\frac{\sqrt{a^{2} b^{2}+b^{2} c^{2}+c^{2} a^{2}}}{\sqrt{a^{2}+b^{2}} \cdot \sqrt{a^{2}+c^{2}}}
$$

于是

$$
S=\frac{1}{2} \cdot A B \cdot A C \cdot \sin \angle B A C=\frac{1}{2} \sqrt{a^{2} b^{2}+b^{2} c^{2}+c^{2} a^{2}}
$$

而

$$
V=\frac{1}{3} \cdot T C \cdot S_{\triangle T A B}=\frac{1}{6} a b c
$$

于是

$$
T D=\frac{V}{\frac{1}{3} S}=\frac{a b c}{\sqrt{a^{2} b^{2}+b^{2} c^{2}+c^{2} a^{2}}}
$$

从而

$$
\frac{1}{T D^{2}}=\frac{1}{a^{2}}+\frac{1}{b^{2}}+\frac{1}{c^{2}}
$$

因此命题正确;

(4)根据(3) 有

$$
S^{2}=\frac{1}{4}\left(a^{2} b^{2}+b^{2} c^{2}+c^{2} a^{2}\right)=S_{\triangle T A B}^{2}+S_{\triangle T B C}^{2}+S_{\triangle T C A}^{2}
$$

因此命题错误.

(5)根据空间向量的共面性质,在平面 $A B C$ 上的点 $P$ 满足

$$
\overrightarrow{T P}=\lambda \overrightarrow{T A}+\mu \overrightarrow{T B}+\nu \overrightarrow{T C}
$$

其中 $\lambda+\mu+\nu=1$.

于是若直线 $T P$ 上一点 $Q$ 满足 $\overrightarrow{T Q}=x \overrightarrow{T P}$, 那么

$$
\overrightarrow{T Q}=\lambda^{\prime} \overrightarrow{T A}+\mu^{\prime} \overrightarrow{T B}+\nu^{\prime} \overrightarrow{T C}
$$

其中 $\lambda^{\prime}+\mu^{\prime}+\nu^{\prime}=x$.

在本命题中, 令点 $P$ 与点 $T^{\prime}$ 重合, 点 $Q$ 与点 $O$ 重合, 则

$$
x=1-\frac{O T^{\prime}}{T T^{\prime}}
$$

而另一方面, 有

$$
\frac{O A^{\prime}}{A A^{\prime}}=\lambda^{\prime}, \frac{O B^{\prime}}{B B^{\prime}}=\mu^{\prime}, \frac{O C^{\prime}}{C C^{\prime}}=\nu^{\prime},
$$

如图 2. 因此命题正确.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-192.jpg?height=327&width=303&top_left_y=613&top_left_x=1461)

图 2

综上所述, 正确答案是(1)(2)(3).

## 第 750 题 从平面到空间

已知 $m, n$ 是异面垂直且距离为 $d$ 的两条直线, 长度为 $l$ 的线段 $P Q$ 的端点 $P, Q$ 分别在直线 $m, n$上滑动, 求线段 $P Q$ 的中点 $M$ 的轨迹.

解析 如图, 设 $m, n$ 的公垂线段为 $A B$, 过线段 $A B$ 的中点 $O$ 作 $A B$ 的法平面 $\alpha$, 分别作 $P, Q$ 在平面 $\alpha$ 上的投影 $P^{\prime}, Q^{\prime}$, 连结 $O P^{\prime}, O Q^{\prime}, O M, P^{\prime} Q^{\prime}$.

由于 $P P^{\prime}$ 与 $Q Q^{\prime}$ 平行且相等, 于是点 $M$ 同时平分 $P Q$ 与 $P^{\prime} Q^{\prime}$, 此时线段 $P^{\prime} Q^{\prime}$ 的长度仍为定值 $\sqrt{l^{2}-d^{2}}$.

此时问题已经转化为平面上的对应问题, 不难得到所求轨迹是以 $m, n$ 的公垂线段中点 $O$ 为圆心, $\frac{1}{2} \sqrt{l^{2}-d^{2}}$ 为半径的圆, 且该圆所在的平面与公垂线段

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-192.jpg?height=371&width=420&top_left_y=1476&top_left_x=1345)
垂直.

## 思考与总结

本题是下面这个平面轨迹问题的空间版本:

已知 $m, n$ 是互相垂直于点 $O$ 的两条直线, 长度为 $l$ 的线段 $P Q$ 的端点 $P, Q$ 分别在直线 $m, n$ 上滑动,求线段 $P Q$ 中点的轨迹.

由直角三角形斜边上的中线等于斜边的一半, 得 $O M=\frac{1}{2} P Q$ 为定值, 于是点 $M$ 的轨迹是以 $O$ 为圆心, $\frac{1}{2} l$ 为半径的圆.

## 第 751 题 独立的空间向量

如图 1, 已知平行六面体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的底面是菱形且从顶点 $C$出发的三条棱两两形成的角 $\angle C_{1} C B=\angle C_{1} C D=\angle B C D=60^{\circ}$,

(1) 证明: $C_{1} C \perp B D$;

(2) 当 $\frac{C D}{C C_{1}}$ 的值为多少时, 可使 $A_{1} C \perp$ 平面 $C_{1} B D ?$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-193.jpg?height=265&width=418&top_left_y=457&top_left_x=1418)

图 1

解析 (1) 如图 2, 连结 $A C$ 交 $B D$ 于点 $O$, 则由底面 $A B C D$ 为菱形可得对角线 $A C$ 与 $B D$ 互相垂直平分.

由 $\triangle C_{1} C D$ 与 $\triangle C_{1} C B$ 全等, 可得 $C_{1} D=C_{1} B$, 进而 $\triangle C_{1} B D$ 为等腰三角形, 于是 $C_{1} O \perp B D$ (三线合一).

综上, $B D \perp$ 平面 $C_{1} C A A_{1}$, 因此 $B D \perp C_{1} C$.

(2) 由于无论 $\frac{C D}{C C_{1}}$ 的值如何变化, $A_{1} C$ 始终与 $B D$ 保持垂直, 于是只需要使得

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-193.jpg?height=295&width=428&top_left_y=783&top_left_x=1451)

图 2 $A_{1} C$ 与平面 $C_{1} B D$ 内的其他与 $B D$ 不平行的直线 (如 $C_{1} O$ ) 垂直即可. 但接下来无论是对截面 $A A_{1} C_{1} C$ 进行分析 (几何) 还是建立空间直角坐标系进行研究 (代数) 运算量都较大, 我们可以采用同时融合几何与代数特性于一身的空间向量解决问题.

记 $\overrightarrow{C B}=\boldsymbol{a}, \overrightarrow{C D}=\boldsymbol{b}, \overrightarrow{C C_{1}}=\boldsymbol{c}$, 且它们的模分别为 $1,1, x$. 令 $\overrightarrow{C A_{1}} \cdot \overrightarrow{C_{1} D}=0$ 得

$$
(\boldsymbol{a}+\boldsymbol{b}+\boldsymbol{c}) \cdot(\boldsymbol{b}-\boldsymbol{c})=0
$$

即

$$
\boldsymbol{a} \cdot \boldsymbol{b}-\boldsymbol{a} \cdot \boldsymbol{c}+\boldsymbol{b} \cdot \boldsymbol{b}-\boldsymbol{c} \cdot \boldsymbol{c}=0
$$

由已知, 不难得到

$$
\frac{1}{2}-\frac{1}{2} x+1-x^{2}=0
$$

解得

$$
x=1
$$

建系坐标计算是利用空间向量解决立体几何问题的一种方式,但并不是唯一的方式. 空间向量完全可以脱离空间直角坐标系独立运作,尤其是当基本架构中的关键角度并非直角时,直接利用空间向量进行计算往往更为简便.

## 第 752 题 三射线定理

已知二面角 $\alpha-A B-\beta$ 为 $120^{\circ}, C D \subset \alpha, C D \perp A B, E F \subset \beta, E F$ 与 $A B$ 成 $30^{\circ}$ 角, 则异面直线 $C D$ 与 $E F$ 所成角的余弦值为

解析 $\frac{1}{4}$.
应用三射线定理, 有

$$
\cos \theta=\cos 30^{\circ} \cdot \cos 90^{\circ}+\sin 30^{\circ} \cdot \sin 90^{\circ} \cdot \cos 120^{\circ}=-\frac{1}{4}
$$

于是所求值为 $\frac{1}{4}$.

## 第 753 题 正方㑛中的不变量

如图 1, 在正方体 $A B C D-A^{\prime} B^{\prime} C^{\prime} D^{\prime}$ 中, 若点 $P$ (异于点 $B$ ) 是棱上一点, 则满足 $B P$ 和 $A C^{\prime}$ 所成的角为 $45^{\circ}$ 的点 $P$ 的个数为 $\qquad$个.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-194.jpg?height=299&width=316&top_left_y=697&top_left_x=1410)

图 1

## 解析 3.

如图 2 所示, 当动点 $M$ 在直线上运动时, 直线 $P M$ 与某固定方向所成的角会先由 $0^{\circ}$ (无法取得)增大到 $90^{\circ}$ 然后减小到 $0^{\circ}$ (无法取得).

于是我们可以将正方体的各个顶点 (除 $B$ 点外) 染色, 当其余顶点和点 $B$ 的连线与直线 $A C^{\prime}$ 所成的角大于等于 $45^{\circ}$ 时染为实心, 否则染为空心, 如图 3 所示.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-194.jpg?height=283&width=335&top_left_y=1067&top_left_x=1425)

当某条棱的两个端点为一空一实时, 根据零点的存在性定理以及之前的论述, 该棱上存在唯一一个符合题意的点; 当某条棱的两个端点均为实心时, 该棱上不存在符合题意的点; 当某条棱的两个端点均为空心时, 需要仔细考虑.

综上, 符合题意的点共有 3 个, 分别位于棱 $B^{\prime} C^{\prime}, C C^{\prime}, C^{\prime} D^{\prime}$ 上.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-194.jpg?height=332&width=333&top_left_y=1348&top_left_x=1429)

图 3

解题的思路与利用零点的存在性定理判断零点个数的思路是一致的.

## 第 754 题 空间向量的分解

如图 1, 在三棱雉 $P-A B C$ 中, $A B=A C=P B=P C=10, P A=8, B C=12$, 点 $M$ 在平面 $P B C$ 内, 且 $A M=7$, 设异面直线 $A M$ 与 $B C$ 所成角为 $\alpha$, 则 $\cos \alpha$ 的最大值为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-194.jpg?height=297&width=313&top_left_y=2160&top_left_x=1412)

图 1
解析 $\frac{1}{7}$.

首先确定 $M$ 点可能的位置. 由于 $A M$ 是定长线段,因此点 $M$ 的轨迹是平面 $P B C$ 上的圆, 圆心为点 $A$ 在平面 $P B C$ 上的投影, 如图 2.

接下来可以利用空间向量求 $\cos \alpha$ 的最大值, 利用 $M$ 点的轨迹的形成方式对向量 $\overrightarrow{A M}$ 进行适当的分解是解决问题的关键.

利用图形的对称性, 取 $B C$ 的中点 $N$, 连结 $P N, A N$. 不难计算得

$$
A N=P N=8
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-195.jpg?height=322&width=371&top_left_y=289&top_left_x=1504)

图 2

于是 $\triangle P A N$ 为正三角形, 记 $H$ 为点 $A$ 在平面 $P B C$ 上的投影, 则 $A H=4 \sqrt{3}$. 因此点 $M$ 的轨迹是半径为

$$
\sqrt{A M^{2}-A H^{2}}=1
$$

的圆, 这样就有

$$
\cos \alpha=\left|\frac{\overrightarrow{A M} \cdot \overrightarrow{B C}}{A M \cdot B C}\right|=\left|\frac{\overrightarrow{A H} \cdot \overrightarrow{B C}+\overrightarrow{H M} \cdot \overrightarrow{B C}}{A M \cdot B C}\right|,
$$

注意到 $A H \perp B C$,于是

$$
\overrightarrow{A H} \cdot \overrightarrow{B C}=0
$$

而 $\overrightarrow{H M}$ 与 $\overrightarrow{B C}$ 的夹角的取值范围是 $[0, \pi]$, 因此 $\cos \alpha$ 的最大值为

$$
\frac{H M \cdot B C}{A M \cdot B C}=\frac{1}{7}
$$

$\quad$ 从立体几何角度来看, 因为 $A M$ 是母线长为 7 , 底面半径为 1 的圆锥上的任意一条
母线, $B C$ 可以平移到圆锥的底面上,成为一条弦,要找到一条母线,使得该母线与弦的夹角
最小.
$\quad$ 因为任意一条弦与两条母线构成腰为 7 的等腰三角形, 故顶角最大时, 底角最小, 即与
$B C$ 平行的直径的端点对应的母线可以使得底角有最小值.

## 第 755 题 空间向量的基底

如图, 在四面体 $A B C D$ 中, $O, E$ 分别是 $B D, B C$ 的中点, $A O$ 垂直于平面 $B C D$,且 $C A=C B=C D=2, A B=\sqrt{2}$, 求异面直线 $A B$ 与 $E D$ 所成角的大小.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-195.jpg?height=256&width=314&top_left_y=1930&top_left_x=1524)

解析 解法一 记

$$
\overrightarrow{C A}=2 \boldsymbol{a}, \overrightarrow{C B}=2 \boldsymbol{b}, \overrightarrow{C D}=2 \boldsymbol{c}
$$

其中 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ 均为单位向量, 则

$$
\overrightarrow{C O}=\boldsymbol{b}+\boldsymbol{c}, \overrightarrow{C E}=\boldsymbol{b}, \overrightarrow{A O}=\boldsymbol{b}+\boldsymbol{c}-2 \boldsymbol{a},
$$

而 $A O$ 垂直于平面 $B C D$, 于是

$$
(\boldsymbol{b}+\boldsymbol{c}-2 \boldsymbol{a}) \cdot \boldsymbol{b}=(\boldsymbol{b}+\boldsymbol{c}-2 \boldsymbol{a}) \cdot \boldsymbol{c}=0
$$

即

$$
\boldsymbol{b} \cdot \boldsymbol{c}-2 \boldsymbol{a} \cdot \boldsymbol{b}+1=0, \boldsymbol{b} \cdot \boldsymbol{c}-2 \boldsymbol{a} \cdot \boldsymbol{c}+1=0
$$

又 $A B=\sqrt{2}$, 于是

$$
(2 \boldsymbol{a}-2 \boldsymbol{b}) \times(2 \boldsymbol{a}-2 \boldsymbol{b})=2,
$$

即

$$
\boldsymbol{a} \cdot \boldsymbol{b}=\frac{3}{4}
$$

由(1)(2得

$$
\boldsymbol{b} \cdot \boldsymbol{c}=\frac{1}{2}, \boldsymbol{a} \cdot \boldsymbol{c}=\frac{3}{4},
$$

又

$$
\overrightarrow{A B}=2 \boldsymbol{b}-2 \boldsymbol{a}, \overrightarrow{E D}=2 \boldsymbol{c}-\boldsymbol{b}
$$

于是异面直线 $A B$ 与 $E D$ 所成角 $\theta$ 满足

$$
\begin{aligned}
\cos \theta & =\frac{|(2 \boldsymbol{b}-2 \boldsymbol{a}) \cdot(2 \boldsymbol{c}-\boldsymbol{b})|}{\sqrt{2} \cdot \sqrt{(2 \boldsymbol{c}-\boldsymbol{b}) \cdot(2 \boldsymbol{c}-\boldsymbol{b})}} \\
& =\frac{|4 \boldsymbol{b} \cdot \boldsymbol{c}-2-4 \boldsymbol{a} \cdot \boldsymbol{c}+2 \boldsymbol{a} \cdot \boldsymbol{b}|}{\sqrt{2} \cdot \sqrt{4-4 \boldsymbol{b} \cdot \boldsymbol{c}+1}} \\
& =\frac{\sqrt{6}}{4}
\end{aligned}
$$

因此, 所求角为 $\arccos \frac{\sqrt{6}}{4}$.

解法二 根据题意, 有

$$
O A=O B=O D=1
$$

且 $A B=A D=\sqrt{2}$.

而 $B E=1, A E=\sqrt{2}, D E=\sqrt{3}$, 利用空间余弦定理, 可得

$$
\begin{aligned}
\cos \langle A B, E D\rangle & =\frac{\left|A D^{2}+B E^{2}-A E^{2}-B D^{2}\right|}{2 \cdot A B \cdot D E} \\
& =\frac{|2+1-2-4|}{2 \cdot \sqrt{2} \cdot \sqrt{3}} \\
& =\frac{\sqrt{6}}{4} .
\end{aligned}
$$

## 第 756 题 空间动态问题

如图 1 所示, 已知边长为 1 的正 $\triangle A^{\prime} B C$ 的顶点 $A^{\prime}$ 在平面 $\alpha$ 内, 顶点 $B, C$ 在平面 $\alpha$ 外的同一侧, 点 $B^{\prime}, C^{\prime}$ 分别为 $B, C$ 在平面 $\alpha$ 内的投影, 设 $B B^{\prime} \leqslant C C^{\prime}$, 直线 $C B^{\prime}$ 与平面 $A^{\prime} C C^{\prime}$ 所成的角为 $\varphi$. 若 $\triangle A^{\prime} B^{\prime} C^{\prime}$ 是以角 $A^{\prime}$ 为直角的直角三角形, 则 $\tan \varphi$ 的范围为 $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-196.jpg?height=245&width=317&top_left_y=2093&top_left_x=1394)

图 1

解析 $\left[\frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}\right)$.
解法一 如图 2 建立空间直角坐标系,设 $B(0, b, m), C(c, 0, n)$.可得

$$
\left\{\begin{array}{l}
b^{2}+m^{2}=c^{2}+n^{2}=1 \\
(0, b, m) \cdot(c, 0, n)=\frac{1}{2} \\
0<m \leqslant n
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-197.jpg?height=257&width=478&top_left_y=202&top_left_x=1399)

图 2

可得 $m$ 的范围是 $\left(\frac{1}{2}, \frac{\sqrt{2}}{2}\right]$, 则

$$
\tan \varphi=b=\sqrt{1-m^{2}}
$$

的取值范围为 $\left[\frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}\right)$.

解法二 由三余弦定理知

$$
\cos \angle B A^{\prime} z \cdot \cos \angle C A^{\prime} z=\cos \angle B A^{\prime} C=\frac{1}{2},
$$

而 $\angle B A^{\prime} z \geqslant \angle C A^{\prime} z$, 所以 $\cos \angle B A^{\prime} z \leqslant \cos \angle C A^{\prime} z$, 从而得到所求范围.

思考与总结

注意到 $\tan \varphi=\cos \angle B A^{\prime} B^{\prime}=\sin \angle B A^{\prime} z$. 考虑 $\angle B A^{\prime} z$ 为直线 $B A^{\prime}$ 与平面 $A C^{\prime}$ 所成的角, 显然其上确界 (无法取得) 为 $60^{\circ}$, 此时 $\sin \angle B A^{\prime} z=\frac{\sqrt{3}}{2}$; 其最小值当 $B B^{\prime}=C C^{\prime}$ 时取得, 为 $45^{\circ}$. 因此所求的范围为 $\left[\frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}\right)$

## 第 757 题 代表平面一出击

已知平面 $\alpha$ 和 $\beta$ 相交形成的四个二面角的其中一个为 $60^{\circ}$, 则在空间中过某定点 $P$ 与这两个平面所成的线面角均为 $30^{\circ}$ 的直线 $l$ 的条数为

## 解析 3.

如图,平面上的两条直线所成角大小为 $\theta$ 的平分线为互相垂直的两条直线,在运动过程中始终保持与两条直线所成的角相等, 且该角的取值范围分别为 $\left[\frac{\theta}{2}, \frac{\pi}{2}\right]$ 以及 $\left[\frac{\pi-\theta}{2}, \frac{\pi}{2}\right]$.

因此当 $\theta=60^{\circ}$,而与两条直线所成角均为 $60^{\circ}$ 时对应的直线为 3 条.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-197.jpg?height=344&width=383&top_left_y=1731&top_left_x=1496)

## 第 758 题 $\quad$ 年年岁岁花相似

如图 1, $A B$ 是圆 $O$ 的直径, $S A$ 与圆 $O$ 所在的平面垂直且 $S A=A B=2 . C$ 为圆 $O$上不同于 $A, B$ 的点, $M, N$ 分别为点 $A$ 在线段 $S B, S C$ 上的投影. 当三棱雉 $S-A M N$的体积最大时, $S C$ 与平面 $A B C$ 所成角的正弦值是 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-197.jpg?height=268&width=251&top_left_y=2269&top_left_x=1592)

图 1
解析 $\frac{\sqrt{3}}{2}$.

显然 $M$ 点为定点 (线段 $S B$ 的中点), 因此问题的关键在于确定 $N$ 点的轨迹.

根据题意有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-198.jpg?height=170&width=958&top_left_y=420&top_left_x=432)

因此 $A N \perp N M$, 即 $N$ 点的轨迹是以 $A M$ 为直径的圆 (不包含 $A, M$ 两点), 如图 2.

此时三棱锥 $S-A M N$ 的体积

$$
V=\frac{1}{6} A N \cdot N M \cdot S M=\frac{\sqrt{2}}{6} \cdot A N \cdot N M
$$

且 $A N^{2}+N M^{2}=A M^{2}=2$. 于是当 $A N=N M=1$ 时, 三棱雉 $S-A M N$ 的体积最大, 此时 $\angle A S N=\frac{\pi}{6}$, 因此所求正弦值为 $\cos \frac{\pi}{6}=\frac{\sqrt{3}}{2}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-198.jpg?height=283&width=250&top_left_y=572&top_left_x=1505)

图 2

有趣的是, 当 $C$ 在圆上运动时, $N$ 也在圆上运动; $S A, A C, C B$ 两两垂直, $A N, N M, M S$ 也两两垂直. 因此三棱雉 $S-A B C$ 与三棱雉 $S-M A N$ 是类似的, 这个作图过程可以无限进行下去.

## 第 759 题 镜面反射

在正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 中, 棱 $A B$ 的中点为 $P$. 若光线从点 $P$ 出发, 依次经过三个侧面 $B C C_{1} B_{1}, D C C_{1} D_{1}, A D D_{1} A_{1}$ 反射后, 落到侧面 $A B B_{1} A_{1}$ (不包括边界) 上, 求人射光线 $P Q$ 与侧面 $B C C_{1} B_{1}$ 所成角的正切值的取值范围.

解析 不妨设正方体的棱长为 2 .

如图, 将正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 依次按对应的顺序对称, 最后得到正方体 $A^{\prime} B^{\prime} C^{\prime} D^{\prime}$ $-A^{\prime}{ }_{1} B^{\prime}{ }_{1} C^{\prime}{ }_{1} D^{\prime}{ }_{1}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-198.jpg?height=510&width=1100&top_left_y=1784&top_left_x=372)

分别连结 $P A^{\prime}, P B^{\prime}, P B^{\prime}{ }_{1}, P A^{\prime}{ }_{1}$, 与侧面 $B C C_{1} B_{1}$ 依次交于 $E, F, G, H$ 四点, 则 $Q$ 点是四边形 $E F G H$内部(不包含边界)的一点,所求正切值

$$
\tan \theta=\frac{P B}{B Q}=\frac{1}{B Q}
$$

利用相似三角形,可得

$$
B F=\frac{4}{5}, B E=\frac{4}{3}, F G=\frac{2}{5}, E H=\frac{2}{3},
$$

于是 $B Q$ 满足

$$
\frac{4}{5}=B F<B Q<B H=\sqrt{B E^{2}+E H^{2}}=\frac{2 \sqrt{5}}{3},
$$

因此所求正切值的取值范围是 $\left(\frac{3 \sqrt{5}}{10}, \frac{5}{4}\right)$.

## 第 760 题 折叠中的二面角

如图 1, 已知 $\triangle A B C, D$ 是 $A B$ 的中点, 沿直线 $C D$ 将 $\triangle A C D$ 折成 $\triangle A^{\prime} C D$, 所成二面角 $A^{\prime}-C D-B$ 的平面角为 $\alpha$, 则
A. $\angle A^{\prime} D B \leqslant \alpha$
B. $\angle A^{\prime} D B \geqslant \alpha$
C. $\angle A^{\prime} C B \leqslant \alpha$
D. $\angle A^{\prime} C B \geqslant \alpha$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-199.jpg?height=332&width=330&top_left_y=833&top_left_x=1515)

图 1

## 解析 B.

得到答案是容易的, 可以取以下两种极端情形进行排除:

如图 2, 当 $\alpha=\pi$ 时,显然 $\angle A^{\prime} D B=\angle A D B=\pi$,而 $\angle A^{\prime} C B=\angle A C B<\pi$, 排除 D;

如图 2, 当 $\alpha=0$ 时, 显然 $\angle A^{\prime} D B=\angle A^{\prime \prime} D B>0$, 而 $\angle A^{\prime} C B=\angle A^{\prime \prime} C B>0$, 排除 A,C.

下面证明选项 B 是正确的.

如图 3 所示, 在平面 $A B C$ 内过点 $D$ 作线段 $M N$ 垂直于 $C D$, 且 $A B=M N, D$ 亦为 $M N$ 的中点. 设在折叠过程中, $M$ 的对应点为 $M^{\prime}$, 则根据二面角的平面角的定义有 $\alpha=$ $\angle M^{\prime} D N$.

若线段 $M N$ 与线段 $A B$ 重合,那么就有 $\angle M^{\prime} D N=\angle A^{\prime} D B$, 命题成立;

若线段 $M N$ 不与线段 $A B$ 重合, 那么 $A$ 和 $B$ 分别位于直线 $M N$ 两侧, 于是 $A^{\prime}$ 和 $B$ 分别位于平面 $M^{\prime} D N$ 两侧. 进而在 $\triangle A^{\prime} D B$ 和 $\triangle M^{\prime} D B$ 中, $M^{\prime} D=A^{\prime} D$ 且 $B A^{\prime}>$ $B M^{\prime}$, 于是 $\angle A^{\prime} D B>\angle M^{\prime} D B$. 而在 $\triangle M^{\prime} D B$ 和 $\triangle M^{\prime} D N$ 中, $D N=D B$ 且 $M^{\prime} B>$ $M^{\prime} N$, 于是 $\angle M^{\prime} D B>\angle M^{\prime} D N$, 于是命题成立.

其他解法 也可以利用三射线定理

$$
\cos \angle A^{\prime} D B=\cos \angle A^{\prime} D C \cos \angle B D C+\sin \angle A^{\prime} D C \sin \angle B D C \cos \alpha
$$

结合 $\angle A^{\prime} D C+\angle B D C=\pi$, 有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-199.jpg?height=351&width=316&top_left_y=1227&top_left_x=1552)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-199.jpg?height=387&width=318&top_left_y=1717&top_left_x=1551)

图 3

$$
1+\cos \angle A^{\prime} D B=(1+\cos \alpha) \cdot \sin \angle A^{\prime} D C \sin \angle B D C
$$

因此

$$
\cos \angle A^{\prime} D B \leqslant \cos \alpha,
$$

考虑到余弦函数在 $[0, \pi]$ 内单调递减, 于是命题成立.

## 第 761 题 又见三射线

如图 1, 已知 Rt $\triangle A B C$ 的两条直角边 $A C=2, B C=3, P$ 为悇边 $A B$ 上一点, 沿 $C P$ 将 $\triangle A B C$ 折成直二面角 $A-C P-B$, 当 $A B=\sqrt{7}$ 时, 二面角 $P-A C-B$ 的平面角的大小为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-200.jpg?height=188&width=289&top_left_y=443&top_left_x=1457)

图 1

解析 $\arctan \sqrt{2}$.

如图 2, 在平面 $P C B$ 内过点 $P$ 作直二面角 $A-C P-B$ 的棱 $C P$ 的垂线交边 $B C$ 于点 $E$, 则 $E P \perp$ 平面 $A C P$.

于是在平面 $P A C$ 中过点 $P$ 作二面角 $P-A C-B$ 的棱 $A C$ 的垂线, 垂足为 $D$, 连结 $D E$, 则 $\angle P D E$ 为二面角 $P-A C-B$ 的平面角, 且 $\tan \angle P D E=\frac{E P}{P D}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-200.jpg?height=186&width=273&top_left_y=799&top_left_x=1497)

图 2

根据三射线定理, 有

$$
\cos \angle A C B=\cos \angle A C P \cdot \cos \angle B C P
$$

于是

$$
\frac{A C^{2}+B C^{2}-A B^{2}}{2 \cdot A C \cdot B C}=\cos \angle A C P \cdot \sin \angle A C P
$$

解得

$$
\angle A C P=\frac{\pi}{4}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-200.jpg?height=227&width=294&top_left_y=1163&top_left_x=1476)

图 3

如图 3.

因此所求二面角 $P-A C-B$ 的平面角的大小为 $\arctan \sqrt{2}$.

## 第 762 题 投影的位置

如图 1, 在矩形 $A B C D$ 中, $A B=2, A D=4$, 点 $E$ 在线段 $A D$ 上且 $A E=3$, 现分别沿 $B E, C E$ 将 $\triangle A B E, \triangle D C E$ 翻折, 使点 $D$ 落在线段 $A E$ 上, 记为 $D^{\prime}$, 则此时二面角 $D^{\prime}-E C-B$ 的平面角的余弦值为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-200.jpg?height=199&width=304&top_left_y=1832&top_left_x=1449)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-200.jpg?height=200&width=336&top_left_y=2091&top_left_x=1436)

图 2

解析 $\frac{7}{8}$.

解法一 如图 2, 在线段 $A E$ 上取点 $F$, 使 $E F=D E=1$, 则折叠后 $D$ 点与 $F$ 点重合. 接下来需要分析 $D^{\prime}$ 在平面 $E C B$ 上投影的位置.

如图 3, 过点 $D$ 垂直于 $C E$ 的直线为 $B D$, 因此折叠后的 $\triangle D^{\prime} G B$ 垂直于 $C E$, 进而 $\angle D^{\prime} G B$ 为所求.

由余弦定理可得

$$
\cos \angle D^{\prime} G B=\frac{D^{\prime} G^{2}+B G^{2}-B D^{\prime 2}}{2 \cdot D^{\prime} G \cdot B G}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-200.jpg?height=177&width=396&top_left_y=2377&top_left_x=1373)

图 3
在折叠前的图形中,即为

$$
\cos \angle D^{\prime} G B=\frac{D G^{2}+B G^{2}-B F^{2}}{2 \cdot D G \cdot B G}=\frac{7}{8}
$$

因此所求余弦值为 $\frac{7}{8}$.

事实上, 点 $D^{\prime}$ 在平面 $E B C$ 上的投影 $H$ 是在折叠前的矩形中 $B D$ 与过点 $F$ 的 $B E$ 的垂线的交点, 如图 2.

这里提供了如何在折叠问题中寻找某点在未折平面上的投影的方法.在折叠前的平面图形中,过该点作折痕的垂线,则折叠过程中,该点在未折平面上的投影一定在垂线构成的平面内,于是投影一定在 (没有折起来的)垂线上. 所以在本题中, 因为点 $D, F$ 折叠后重合, 所以它的投影可以直接在平面图形中作出.

解法二 在三棱雉 $E-D^{\prime} B C$ 中, 设二面角 $D^{\prime}-E C-B$ 的平面角大小为 $\varphi$, 则

$$
\cos \angle D^{\prime} E B=\cos \angle D^{\prime} E C \cdot \cos \angle B E C+\sin \angle D^{\prime} E C \cdot \sin \angle B E C \cdot \cos \varphi
$$

即

$$
\cos \angle A E B=\cos \angle D E C \cdot \cos \angle B E C+\sin \angle D E C \cdot \sin \angle B E C \cdot \cos \varphi
$$

根据余弦定理, 有

$$
\cos \angle B E C=\frac{E B^{2}+E C^{2}-B C^{2}}{2 \cdot E B \cdot E C}=\frac{1}{\sqrt{65}}
$$

也即

$$
\frac{3}{\sqrt{13}}=\frac{1}{\sqrt{5}} \cdot \frac{1}{\sqrt{65}}+\frac{2}{\sqrt{5}} \cdot \frac{8}{\sqrt{65}} \cdot \cos \varphi
$$

解得

$$
\cos \varphi=\frac{7}{8}
$$

## 第 763 题 休积转化

如图 1, 正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的棱长为 2 , 动点 $E, F$ 在棱 $A_{1} B_{1}$ 上, 动点 $P, Q$ 分别在棱 $A D, C D$ 上, 若 $E F=1, A_{1} E=x, D Q=y, D P=z$, 且 $x, y, z>0$, 则四面体 $P E F Q$ 的体积
A. 与 $x, y, z$ 都有关
B. 与 $x$ 有关,与 $y, z$ 无关
C. 与 $y$ 有关,与 $x, z$ 无关
D. 与 $z$ 有关,与 $x, y$ 无关

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-201.jpg?height=284&width=295&top_left_y=1753&top_left_x=1529)

图 1

## 解析 D.

延长 $Q P$ 与 $B A$ 的延长线交于点 $R$, 如图 2.

根据题意, 四面体 $P E F Q$ 的体积

$$
V_{P-E F Q}=\frac{R P}{R Q} \cdot V_{R-E F Q}=\frac{R P}{R Q} \cdot V_{Q-E F R}=\frac{A P}{A D} \cdot V_{Q-E F R},
$$

而 $\triangle R E F$ 的面积及点 $Q$ 到平面 $E F R$ 的距离均为定值, 因此四面体 $P E F Q$ 的体积只与 $P$ 点的位置有关, 选项 $\mathrm{D}$ 正确.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-201.jpg?height=285&width=350&top_left_y=2097&top_left_x=1507)

图 2

## 第 764 题 异面直线所成角

如图 1, 四边形 $A B C D$ 和 $A D P Q$ 均为正方形, 它们所在的平面互相垂直, 动点 $M$ 在线段 $P Q$ 上, $E, F$ 分别为 $A B, B C$ 的中点. 设异面直线 $E M$ 与 $A F$ 所成的角为 $\alpha$, 则 $\cos \alpha$ 的最大值为 . $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-202.jpg?height=309&width=308&top_left_y=451&top_left_x=1414)

图 1

解析 $\frac{2}{5}$.

解法一 如图 2, 考虑三棱锥 $E-M N R$, 其中 $N$ 为 $B F$ 的中点, $R$ 为 $C D$ 的中点.设二面角 $M-E R-N$ 的平面角的大小为 $\varphi,\langle\overrightarrow{E M}, \overrightarrow{E N}\rangle=\theta$, 则

$$
\tan \varphi=-2, \cos \varphi=-\frac{1}{\sqrt{5}}
$$

因此根据三射线定理, 有

$$
\begin{aligned}
\cos \theta & =\cos \angle M E R \cdot \cos \angle N E R+\sin \angle M E R \cdot \sin \angle N E R \cdot \cos \varphi \\
& =\cos \angle M E R \cdot \frac{1}{\sqrt{5}}+\sin \angle M E R \cdot \frac{2}{\sqrt{5}} \cdot\left(-\frac{1}{\sqrt{5}}\right) \\
& =\frac{1}{\sqrt{5}} \cos \angle M E R-\frac{2}{5} \sin \angle M E R .
\end{aligned}
$$

注意到当点 $M$ 从点 $P$ 运动到点 $Q$ 时, $\angle M E R$ 单调递增且为第一象限角, 因此, 上式关于 $\angle M E R$ 单调递减.

当点 $M$ 与点 $P$ 重合时, $\cos \angle M E R=\frac{2}{3}$, 故

$$
\cos \theta=\frac{1}{\sqrt{5}} \cdot \frac{2}{3}-\frac{2}{5} \cdot \frac{\sqrt{5}}{3}=0
$$

当点 $M$ 与点 $Q$ 重合时, $\cos \angle M E R=0$, 故

$$
\cos \theta=\frac{1}{\sqrt{5}} \cdot 0-\frac{2}{5} \cdot 1=-\frac{2}{5}
$$

因此 $-\frac{2}{5} \leqslant \cos \theta \leqslant 0$, 故所求最大值为 $\frac{2}{5}$.

解法二以 $A$ 为原点, $A B, A D, A Q$ 为 $x$ 轴、 $y$ 轴、 $z$ 轴建立空间直角坐标系, 则有

$$
\overrightarrow{A F}=(2,1,0), E(1,0,0), M(0, m, 0)
$$

其中 $m \in[0,2]$, 从而有 $\overrightarrow{E M}=(-1, m, 2)$,

$$
\cos \alpha=\left|\frac{m-2}{\sqrt{5} \cdot \sqrt{5+m^{2}}}\right|,
$$

设 $t=2-m \in[0,2]$, 则有

$$
\cos \alpha=\frac{t}{\sqrt{5\left(9-4 t+t^{2}\right)}}=\frac{1}{\sqrt{5}} \cdot \frac{1}{\sqrt{9\left(\frac{1}{t}-\frac{2}{9}\right)^{2}+\frac{5}{9}}}
$$

因为 $\frac{1}{t} \in\left[\frac{1}{2},+\infty\right)$, 所以当 $\frac{1}{t}=\frac{1}{2}>\frac{2}{9}$ 时, $\cos \alpha$ 有最大值 $\frac{2}{5}$.

解法三 将两异面直线平移到共面, 如图 3, 其中 $N$ 为 $B F$ 的中点,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-203.jpg?height=306&width=292&top_left_y=350&top_left_x=608)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-203.jpg?height=303&width=311&top_left_y=351&top_left_x=1134)

图 4

注意到当点 $M$ 与点 $P$ 重合时, $E D \perp A F$, 于是 $\angle M E N=\frac{\pi}{2}$, 当点 $M$ 从点 $P$ 运动到点 $Q$ 时, $\angle M E N$ 单调递增, 因此当点 $M$ 与点 $Q$ 重合时, $\cos \angle M E N$ 取得最小值. 如图 4,

设 $A B=2$, 则在 $\triangle N M E$ 中, 可得

$$
M E=\sqrt{5}, E N=\frac{\sqrt{5}}{2}, M N=\frac{\sqrt{33}}{2}
$$

结合余弦定理,得

$$
\cos \angle M E N=\frac{M E^{2}+E N^{2}-M N^{2}}{2 \cdot M E \cdot N E}=-\frac{2}{5}
$$

所以所求最大值为 $\frac{2}{5}$.

## 第 765 题 空间余弦定理

已知空间四边形 $A B C D$ 中, $A B=2, B C=8, C D=10, A D=4$, 则 $\overrightarrow{A C} \cdot \overrightarrow{B D}=$

解析 -12 .

在 $\triangle A B C$ 中, 我们根据余弦定理可得

$$
\begin{aligned}
\overrightarrow{A B} \cdot \overrightarrow{A C} & =A B \cdot A C \cdot \cos A \\
& =A B \cdot A C \cdot \frac{A B^{2}+A C^{2}-B C^{2}}{2 \cdot A B \cdot A C} \\
& =\frac{1}{2}\left(A B^{2}+A C^{2}-B C^{2}\right)
\end{aligned}
$$

因此在空间四边形 $A B C D$ 中, 我们有

$$
\begin{aligned}
\overrightarrow{A C} \cdot \overrightarrow{B D} & =\overrightarrow{A C} \cdot(\overrightarrow{A D}-\overrightarrow{A B}) \\
& =\overrightarrow{A C} \cdot \overrightarrow{A D}-\overrightarrow{A C} \cdot \overrightarrow{A B} \\
& =\frac{1}{2}\left(A C^{2}+A D^{2}-C D^{2}\right)-\frac{1}{2}\left(A C^{2}+A B^{2}-B C^{2}\right) \\
& =\frac{\left(A D^{2}+B C^{2}\right)-\left(A B^{2}+C D^{2}\right)}{2} \\
& =-12
\end{aligned}
$$

## 第 766 题 空间向量显神威

一个正四面体的四个顶点到同一平面的距离分别为 $0,1,2,3$, 求正四面体的棱长.

解析 设正四面体为 $A B C D$, 且点 $D, A, B, C$ 到平面 $\alpha$ 的距离分别为 $0,1,2,3$. 分别记 $\overrightarrow{D A}, \overrightarrow{D B}, \overrightarrow{D C}$ 为 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{x}$, 平面 $\alpha$ 的法向量为 $\boldsymbol{n}$, 且有 $\boldsymbol{a}, \boldsymbol{n}$ 的模分别为 $t, s$. 考虑到

$$
\boldsymbol{a} \cdot \boldsymbol{a}=\boldsymbol{b} \cdot \boldsymbol{b}=\boldsymbol{c} \cdot \boldsymbol{c}=t^{2},
$$

且

$$
\boldsymbol{a} \cdot \boldsymbol{b}=\boldsymbol{b} \cdot \boldsymbol{c}=\boldsymbol{c} \cdot \boldsymbol{a}=\frac{1}{2} t^{2}
$$

因此设 $n=x a+y b+z \boldsymbol{c}$, 则有

$$
s=t \cdot \sqrt{x^{2}+y^{2}+z^{2}+x y+y z+z x}
$$

根据点 $A, B, C$ 到平面 $\alpha$ 的距离分别为 $1,2,3$, 可得

$$
\left\{\begin{array}{l}
\boldsymbol{a} \cdot \boldsymbol{n}=\lambda_{1} s \\
\boldsymbol{b} \cdot \boldsymbol{n}=\lambda_{2} s \\
\boldsymbol{c} \cdot \boldsymbol{n}=\lambda_{3} s
\end{array}\right.
$$

其中 $\left(\lambda_{1}, \lambda_{2}, \lambda_{3}\right)$ 有四种可能:

$$
(1,2,3),(-1,2,3),(1,-2,3),(1,2,-3)
$$

上述方程组即

$$
\left[\begin{array}{lll}
2 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 2
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{s}{t^{2}}\left[\begin{array}{l}
2 \lambda_{1} \\
2 \lambda_{2} \\
2 \lambda_{3}
\end{array}\right]
$$

这样就可以解得

$$
\frac{t^{2}}{s}(x, y, z)=(-1,1,3),(-4,2,4),(1,-5,5),(2,4,-6)
$$

进而可以求得

$$
t=\sqrt{10}, \sqrt{20}, \sqrt{26}, \sqrt{28}
$$

即

$$
t=\sqrt{10}, 2 \sqrt{5}, \sqrt{26}, 2 \sqrt{7},
$$

于是正四面体的棱长为 $\sqrt{10}, 2 \sqrt{5}, \sqrt{26}, 2 \sqrt{7}$.

## 第 767 题 投影长度

证明: 棱长为 1 的正四面体的棱在任一平面上的投影长度的平方之和为定值.

解析 先证明引理.

引理 已知非零空间向量 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ 两两垂直, $\boldsymbol{m}$ 为空间任意非零向量且与 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ 的夹角分别为 $\alpha, \beta, \gamma$, 则

$$
\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=1
$$

证明 不妨设 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}, \boldsymbol{m}$ 均为单位向量, 且 $\boldsymbol{m}=x \boldsymbol{a}+y \boldsymbol{b}+\boldsymbol{z}$, 则

$$
\cos \alpha=\boldsymbol{a} \cdot \boldsymbol{m}=\boldsymbol{a} \cdot(x \boldsymbol{a}+y \boldsymbol{b}+z \boldsymbol{c})=x,
$$

类似的, 有 $\cos \beta=y, \cos \gamma=z$, 于是

$$
\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=x^{2}+y^{2}+z^{2}=|\boldsymbol{m}|^{2}=1,
$$

引理得证.

将正四面体 $O A B C$ 放人棱长为 $\frac{\sqrt{2}}{2}$ 的正方体 $O G A F-E B H C$ 中研究, 如图.

记 $\overrightarrow{O E}=\boldsymbol{a}, \overrightarrow{O F}=\boldsymbol{b}, \overrightarrow{O G}=\boldsymbol{c}, \boldsymbol{m}$ 为投影面的单位法向量, 且与 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ 的夹角分别为 $\alpha$, $\beta, \gamma$, 则所求棱的投影长度的平方和

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-205.jpg?height=290&width=315&top_left_y=261&top_left_x=1551)

$$
\begin{aligned}
M & =\sum_{\varphi c}\left(O A^{2}-(\overrightarrow{O A} \cdot \boldsymbol{m})^{2}\right)+\sum_{\phi c}\left(A B^{2}-(\overrightarrow{A B} \cdot \boldsymbol{m})^{2}\right) \\
& =6-\sum_{c c}[(\boldsymbol{b}+\boldsymbol{c}) \cdot \boldsymbol{m}]^{2}-\sum_{c c}[(\boldsymbol{a}-\boldsymbol{b}) \cdot \boldsymbol{m}]^{2} \\
& =6-\sum_{\varphi c}\left(\frac{\sqrt{2}}{2} \cos \beta+\frac{\sqrt{2}}{2} \cos \gamma\right)^{2}-\sum_{\varphi c}\left(\frac{\sqrt{2}}{2} \cos \alpha-\frac{\sqrt{2}}{2} \cos \beta\right)^{2} \\
& =6-\sum_{\varphi c} \cos ^{2} \alpha-\sum_{\varphi c} \cos ^{2} \beta \\
& =4
\end{aligned}
$$

为定值, 因此原命题得证.

## 第 768 题 正方体的截面分析

如图 1, 正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的棱长为 $a$, 动点 $P$ 在对角线 $B D_{1}$ 上,过 $P$ 作垂直于 $B D_{1}$ 的平面 $\alpha$, 记这样得到的截面多边形 (含三角形) 的周长为 $L$,面积为 $S, B P=x$, 作出函数 $L(x)$ 与 $S(x)$ 的图象.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-205.jpg?height=318&width=359&top_left_y=1264&top_left_x=1485)

图 1

解析 为了看清楚截面,我们作沿着正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的体对角线 $B D_{1}$ 方向的正投影, 并将截面三角形的变化过程绘图如图 2.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-205.jpg?height=262&width=1164&top_left_y=1758&top_left_x=284)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-205.jpg?height=255&width=283&top_left_y=1759&top_left_x=1471)

运动的三个阶段可以借助图 3 帮助想象 $\left(B \rightarrow P \rightarrow Q \rightarrow D_{1}\right.$ 的三等分线段与 $B \rightarrow A \rightarrow D \rightarrow B$ 的等边三角形分别对应):

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-205.jpg?height=269&width=307&top_left_y=2169&top_left_x=395)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-205.jpg?height=282&width=335&top_left_y=2168&top_left_x=1308)

图 4

其中第二阶段 (六边形阶段)最为复杂,依靠图 4 可以证明此阶段周长为定值,而面积不为定值 (服从二次函数关系).
最后整理出所求的曲线如图 5.

其中

$$
L(x)= \begin{cases}3 \sqrt{6} x, & x \in\left[0, \frac{\sqrt{3}}{3} a\right) \\ 3 \sqrt{2} a, & x \in\left[\frac{\sqrt{3}}{3} a, \frac{2 \sqrt{3}}{3} a\right] \\ 9 \sqrt{2} a-3 \sqrt{6} x, & x \in\left(\frac{2 \sqrt{3}}{3} a, \sqrt{3} a\right]\end{cases}
$$

而

$$
S(x)= \begin{cases}\frac{3 \sqrt{3}}{2} x^{2}, & x \in\left[0, \frac{\sqrt{3}}{3} a\right) \\ -3 \sqrt{3}\left(x-\frac{\sqrt{3}}{2} a\right)^{2}+\frac{3 \sqrt{3}}{4} a^{2}, & x \in\left[\frac{\sqrt{3}}{3} a, \frac{2 \sqrt{3}}{3} a\right] \\ \frac{3 \sqrt{3}}{2}(x-\sqrt{3} a)^{2}, & x \in\left(\frac{2 \sqrt{3}}{3} a, \sqrt{3} a\right]\end{cases}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-206.jpg?height=590&width=592&top_left_y=199&top_left_x=1172)

图 5

换个角度观察变化可以使问题变得更清晰.

## 第 769 题 正方体的截面

如图 1, 已知正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的棱长为 $1, E, F$ 分别是棱 $A D$, $B_{1} C_{1}$ 上的动点, 设 $A E=x, B_{1} F=y$. 若棱 $D D_{1}$ 与平面 $B E F$ 有公共点, 则 $x+y$的取值范围是 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-206.jpg?height=308&width=358&top_left_y=1456&top_left_x=1371)

图 1

## 解析 $[1,2]$.

解法一 如图 2 所示, 设法作出完整的截面 $B E F$, 则该截面与上底面 $A_{1} C_{1}$ 的交线与直线 $B E$ 平行. 过点 $F$ 作与 $B E$ 平行的直线 $l$, 若直线 $l$ 与棱 $A_{1} D_{1}$ 相交且交点不为 $D_{1}$, 则截面 $B E F$ 为平行四边形, 如图 3 棱 $D D_{1}$ 与平面 $B E F$ 没有公共点; 若直线 $l$ 与棱 $A_{1} D_{1}$ 的延长线相交, 则截面 $B E F$ 为五边形, 棱 $D D_{1}$ 与平面 $B E F$ 有公共点,因此可得 $x+y \geqslant 1$.

又 $0 \leqslant x, y \leqslant 1$, 于是 $x+y$ 的取值范围是 $[1,2]$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-206.jpg?height=308&width=343&top_left_y=2176&top_left_x=538)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-206.jpg?height=319&width=352&top_left_y=2165&top_left_x=954)

图 3
解法二 建立空间直角坐标系 $D-A C D_{1}$, 则 $E(1-x, 0,0), B(1,1,0), F(1-y, 1,1)$, 于是

$$
\overrightarrow{E B}=(x, 1,0), \overrightarrow{F B}=(y, 0,-1)
$$

可得平面 $B E F$ 的法向量为 $(-1, x,-y)$, 因此平面 $B E F$ 的方程为

$$
-r+x s-y t=x-1
$$

根据题意, 当 $r=s=0$ 时, $t \in[0,1]$, 于是 $0 \leqslant \frac{1-x}{y} \leqslant 1$, 解得 $x+y \geqslant 1$. 又 $0 \leqslant x, y \leqslant 1$, 于是 $x+y$ 的取值范围是 $[1,2]$.

## 第 770 题 正四面㑛的投影

已知正四面体 $A B C D$ 的棱长为 1 , 棱 $A B / /$ 平面 $\alpha$, 则正四面体上的所有点在平面 $\alpha$ 内的投影构成的图形的面积的取值范围是

## 解析 $\left[\frac{\sqrt{2}}{4}, \frac{1}{2}\right]$.

如图, 不妨将四面体的棱 $A B$ 平移到平面 $\alpha$ 内, 设四面体的顶点 $C, D$ 在平面 $\alpha$ 内的投影分别为 $P, Q, P Q \cap A B=M$, 则 $M$ 是 $A B$ 的中点.

情形一 点 $P$ 和点 $Q$ 分别在 $A B$ 的两侧.

此时所求投影面积为

$$
\frac{1}{2} \cdot P Q \cdot A B \leqslant \frac{1}{2} \cdot C D \cdot A B=\frac{1}{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-207.jpg?height=292&width=464&top_left_y=1062&top_left_x=1397)

当且仅当 $C D / / \alpha$ 时取得等号.

情形二 点 $P$ 和点 $Q$ 在 $A B$ 的同一侧.

此时所求投影面积为

$$
\frac{1}{2} \cdot \max \{M P, M Q\} \cdot A B \geqslant \frac{1}{2} d(C D, A B) \cdot A B=\frac{\sqrt{2}}{4}
$$

当且仅当 $C D \perp \alpha$ 时取得等号. 因此所求投影面积的取值范围是 $\left[\frac{\sqrt{2}}{4}, \frac{1}{2}\right]$.

抓住运动中 $A B$ 与 $C D$ 的投影 $P Q$ 始终垂直这一不变量, 恰当地进行分类讨论.

## 第 771 题 泲贼先拾王

如图 1, 在棱长为 1 的正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 中, 若点 $E, F$ 分别为线段 $B D_{1}, C B_{1}$ 上的动点, 点 $G$ 为底面 $A B C D$ 上的动点, 则 $E F+E G$ 的最小值为 $\qquad$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-207.jpg?height=271&width=279&top_left_y=2095&top_left_x=1550)

图 1

解析 $\frac{2}{3}$.
解决多个动点的最值问题, 通常是先确定一部分点去考虑其他动点的最佳位置, 然后调整之前暂时确定的点的位置, 去研究整体的最佳状态, 这种方法称为局部调整法.

在本题中, 当 $E$ 点确定时, 点 $G, F$ 的最佳位置分别满足 $E G \perp$ 平面 $A B C D$ 以及 $E F$ $\perp B_{1} C$, 于是 $F$ 是四边形 $B_{1} B C C_{1}$ 的中心, 且点 $G$ 为点 $E$ 在平面 $B D$ 上的投影, 如图 2 .

于是只需要将 $\triangle D_{1} F B$ 绕 $B D_{1}$ 旋转至与平面 $B D_{1}$ 共面, 然后过点 $F$ 作 $B D$ 边上的垂线即得 $E F+E G$ 的最小值. 为了方便, 我们直接旋转 $\triangle D_{1} C_{1} B$, 如图 3.

这样就由 $\cos \angle D B D_{1}=\sqrt{\frac{2}{3}}$ 得到 $\cos \angle C_{1} B D=2 \cos ^{2} \angle D B D_{1}-1=\frac{1}{3}$, 于是

$$
F H=\sin \angle C_{1} B D \cdot F B=\frac{2 \sqrt{2}}{3} \cdot \frac{\sqrt{2}}{2}=\frac{2}{3},
$$

也即 $E F+E G$ 的最小值为 $\frac{2}{3}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=295&width=292&top_left_y=199&top_left_x=1457)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=221&width=230&top_left_y=523&top_left_x=1521)

图 3

## 第 772 题 $\quad$ 分步加工

某工件的三视图如图 1 所示, 现将该工件通过切割, 加工成一个体积尽可能大的长方体新工件, 并使新工件的一个面落在原工件的一个面内, 则原工件材料的利用率为 (材料利用率 $=$ 新工件的体积 $\div$ 原工件的体积）
A. $\frac{8}{9 \pi}$
B. $\frac{16}{9 \pi}$
C. $\frac{4(\sqrt{2}-1)^{3}}{\pi}$
D. $\frac{12(\sqrt{2}-1)^{3}}{\pi}$
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=228&width=412&top_left_y=1064&top_left_x=1312)

正视图

侧视图

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=137&width=153&top_left_y=1330&top_left_x=1352)

俯视图

图 1

解析 A.

为了能够从圆锥形的工料中加工出长方体形的工件, 需要首先将圆锥加工成一个圆柱, 然后将圆柱加工成长方体, 如图 2.

因此,我们可以分两步计算工件的材料利用率, 如图 3.

设圆柱的高为 $h$, 则第一步的材料利用率为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=238&width=576&top_left_y=1569&top_left_x=1176)

图 2

$$
\frac{\left(\pi\left(1-\frac{1}{2} h\right)^{2} \cdot h\right)}{\left(\frac{2}{3}\right) \pi} \leqslant \frac{4}{9}
$$

等号当且仅当 $1-\frac{1}{2} h=h$, 即 $h=\frac{2}{3}$ 时取得 (这里用到了三元的均值不等式).

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=259&width=263&top_left_y=2121&top_left_x=546)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-208.jpg?height=298&width=289&top_left_y=2080&top_left_x=978)

图 4

如图 4, 我们熟知第二步的材料利用率最高为 $\frac{2}{\pi}$.

综上,工件的材料利用率最高为
故选 A.

## 第 773 题 三视图还原一七字真言闯天下

如图 1, 网格纸上小正方形的边长为 1 , 实线画出的是某多面体的三视图, 则该多面体的各条棱中, 最长的棱的长度为
A. $6 \sqrt{2}$
B. $4 \sqrt{2}$
C. 6
D. 4

## 解析 C.

在正方体中还原直观图, 如图 2 所示.

显然有 $A C>C D=B D>A B=B C$, 因此只需要比较 $A C$ 与 $A D$ 的大小. 事实上, $A C=$ $4 \sqrt{2}$, 而 $A D=6$, 因此最长的棱为 $A D$, 长度为 6 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-209.jpg?height=312&width=320&top_left_y=609&top_left_x=1512)

운 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-209.jpg?height=298&width=269&top_left_y=931&top_left_x=1598)

图 2

## 第 774 题 形体分析与运动

已知 $A, B, C$ 是球 $O$ 的球面上的三点, $\angle A O B=\angle A O C=45^{\circ}$, 若三棱雉 $O-A B C$ 体积的最大值为 $\frac{2}{3}$, 则球 $O$ 的表面积为

解析 $16 \pi$.

解法一 不难得知 $\triangle A O B$ 与 $\triangle A O C$ 全等, 因此整个图形关于线段 $B C$ 的垂直平分面对称. 如图 1 , 取 $B C$ 的中点 $M$, 则

$$
V_{O-A B C}=\frac{1}{2} \cdot S_{\triangle O A M} \cdot B C
$$

进而选择合适的参数展开计算.

设 $\angle O A M=\alpha, \angle B A M=\beta, O A=O B=O C=r$, 则根据三射线定理, 有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-209.jpg?height=222&width=318&top_left_y=1769&top_left_x=1549)

图 1

$$
\cos \alpha \cdot \cos \beta=\cos \frac{3 \pi}{8}
$$

而

$$
\begin{aligned}
V_{O-A B C} & =\frac{1}{3} \cdot S_{\triangle C A M} \cdot B C \\
& =\frac{1}{6} \sin \alpha \cdot A O \cdot A M \cdot B C \\
& =\frac{4}{3} r^{3} \cdot \cos ^{2} \frac{3 \pi}{8} \cdot \sin \alpha \cdot \cos \beta \cdot \sin \beta \\
& =\frac{4}{3} r^{3} \cdot \cos ^{2} \frac{3 \pi}{8} \cdot \sqrt{\left(1-\cos ^{2} \alpha\right) \cdot \cos ^{2} \beta \cdot\left(1-\cos ^{2} \beta\right)} \\
& =\frac{4}{3} r^{3} \cdot \cos ^{2} \frac{3 \pi}{8} \cdot \sqrt{\left(\cos ^{2} \beta-\cos ^{2} \frac{3 \pi}{8}\right)\left(1-\cos ^{2} \beta\right)} \\
& \leqslant \frac{4}{3} r^{3} \cdot \cos ^{2} \frac{3 \pi}{8} \cdot \frac{1-\cos ^{2} \frac{3 \pi}{8}}{2}=\frac{1}{12} r^{3},
\end{aligned}
$$

其中均值不等式的等号当 $\cos 2 \beta=\cos ^{2} \frac{3 \pi}{8}$ 时取得.

因此不难得到 $r=2$,于是球 $O$ 的表面积为 $16 \pi$.

解法二 如图 2 , 根据题意, 在变化的过程中, $\triangle A O B$ 和 $\triangle A O C$ 保持不变, 而它们的夹角发生变化,抓住运动中的不变量分析问题.

设 $\angle B H C$ 为二面角 $B-O A-C$ 的平面角, 记为 $\theta$, 则

$$
V_{O-A B C}=\frac{1}{3} \cdot S_{\triangle B H C} \cdot O A=\frac{1}{12} r^{3} \cdot \sin \theta
$$

于是当平面 $O A C$ 与平面 $O A B$ 垂直时, 三棱雉 $O-A B C$ 的体积最大.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-210.jpg?height=244&width=265&top_left_y=960&top_left_x=1485)

图 2

因此不难得到 $r=2$, 于是球 $O$ 的表面积为 $16 \pi$.

## 第 775 题 $G P S$ 定位

如图 1 所示, $A D$ 与 $B C$ 是四面体 $A B C D$ 中互相垂直的棱, $B C=2$. 若 $A D=2 c$, 且 $A B+B D=A C+C D=2 a$, 其中 $a, c$ 为常数,则四面体 $A B C D$ 的体积的最大值是 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-210.jpg?height=342&width=216&top_left_y=1545&top_left_x=1504)

图 1

解析 $\frac{2 c}{3} \sqrt{a^{2}-c^{2}-1}$.

本问题中, $A B+B D=A C+C D=2 a$ 描述的事实为 $B$ 点和 $C$ 点到两定点 $A, D$ 的距离之和为 $2 a$, 于是点 $B, C$ 都在以 $A, D$ 为焦点的椭球上, 如图 2. 利用椭球, 不难对四面体 $A B-$ $C D$ 的顶点 $B$ 和 $C$ 进行“GPS 定位”.

由于 $A D \perp B C$, 于是 $B C$ 必然为某个垂直于 $A D$ 的平面截椭球形成的圆的弦, 且 $d(A D$, $B C)$ 即该圆的圆心到弦的距离.

我们知道, 当弦长固定时, 圆的半径越大, 圆心到弦的距离越大. 于是当 $B C$ 为过线段 $A D$ 中点的截面的弦时, 四面体 $A B C D$ 的体积最大, 此时由垂径定理不难得到

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-210.jpg?height=279&width=227&top_left_y=2033&top_left_x=1523)

图 2

$$
d(A D, B C)=\sqrt{a^{2}-c^{2}-1}
$$

进而可以计算得

$$
V_{A B C D}=\frac{2 c}{3} \sqrt{a^{2}-c^{2}-1}
$$

## 第 776 题 运动中的不变量

设 $P-A B C D$ 是一个高为 3 , 底面边长为 2 的正四棱雉, $M$ 是棱 $P C$ 的中点, 过 $A M$ 作平面与线段 $P B, P D$ 分别交于 $E, F$ (可以是线段的端点). 试求四棱雉 $P-$ $A E M F$ 的体积的最大值与最小值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-211.jpg?height=309&width=274&top_left_y=443&top_left_x=1571)

图 1

解析 $\left[\frac{4}{3}, \frac{3}{2}\right]$.

注意到 $A, M$ 为定点, 于是有

$$
V_{P-A E M F}=V_{A-P E F}+V_{M-P E F}=\frac{1}{3} \cdot \frac{3}{2} A H \cdot S_{\triangle P E F},
$$

因此只需要考虑 $S_{\triangle P F E}$ 的取值范围.

根据题意, $A M$ 与 $P H$ 的交点 $G$ 为 $\triangle P A C$ 的重心, 也为 $\triangle P B D$ 的重心.

设 $\overrightarrow{P F}=\lambda \overrightarrow{P D}, \overrightarrow{P E}=\mu \overrightarrow{P B}$, 其中 $\lambda, \mu \in(0,1]$,则

$$
S_{\triangle P F E}=\lambda \mu S_{\triangle P B D},
$$

由向量知识不难得到 $\frac{1}{\lambda}+\frac{1}{\mu}=3$, 因此 $\lambda \mu$ 的取值范围是 $\left[\frac{4}{9}, \frac{1}{2}\right]$, 进而 $V_{P-A E M F}$ 的取值范围是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-211.jpg?height=326&width=291&top_left_y=1032&top_left_x=1576)

图 2

$$
\left[\frac{2}{9} \cdot A H \cdot S_{\triangle P B D}, \frac{1}{4} \cdot A H \cdot S_{\triangle P B D}\right]
$$

考虑到 $V_{P-A B C D}=\frac{2}{3} \cdot A H \cdot S_{\triangle P B D}=4$, 于是

$$
A H \cdot S_{\triangle P B D}=6,
$$

所求的取值范围为 $\left[\frac{4}{3}, \frac{3}{2}\right]$.

## 第 777 题 体积转化

在棱长为 $a$ 的正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 中, $E$ 为棱 $A B$ 的中点.

(1) 求四面体 $E-B_{1} D_{1} C$ 的体积;

(2)求点 $C$ 到平面 $E A_{1} C_{1}$ 的距离.

解析 解法一 (1) 过点 $C$ 作 $C F / / B_{1} D_{1}$, 交 $A D$ 的延长线于点 $F$, 连结 $F B_{1}$, $F D, F E$, 如图 1 所示.

则有

$$
V_{E-B_{1} D_{1} C}=V_{D_{1}-B_{1} C}=V_{F-B_{1} C E}=V_{B_{1}-B C F}=\frac{1}{3} \cdot S_{\triangle E F C} \cdot a
$$

而

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-211.jpg?height=329&width=335&top_left_y=2171&top_left_x=1532)

图 1

$$
S_{\triangle E F C}=S_{A B C F}-S_{\triangle B C E}-S_{\triangle A E F}=\frac{3}{4} a^{2}
$$

所以所求体积为 $\frac{1}{4} a^{3}$.

## 思考与总结

我们熟知, 如果一条直线与一个平面平行, 则直线上任意一点到平面的距离相等, 我们常常利用这个结论对四面体转换端点, 从而使得体积更容易求得.

(2) 连结 $B D, A C$, 过点 $E$ 作 $E F / / A_{1} C_{1}$, 交 $B D, B C$ 于点 $H, F$, 连结 $F C_{1}$, 取上下底面的中心 $O, O_{1}$, 连结 $O O_{1}, O_{1} H$, 如图 2 所示.

因为点 $O$ 在 $A C$ 上, 且 $A C / / A_{1} C_{1}$, 所以点 $C$ 到平面 $E A_{1} C_{1}$ 的距离就等于点 $O$到平面 $E F C_{1} A_{1}$ 的距离. 因为 $E F \perp$ 平面 $B D O_{1}$, 所以过点 $O$ 在平面 $O H O_{1}$ 内作 $O_{1} H$的垂线, 则此垂线垂直于平面 $E F C_{1} A_{1}$, 由

$$
O O_{1}=a, O H=\frac{\sqrt{2}}{4} a
$$

可知所求距离为

$$
d=\frac{a \cdot \frac{\sqrt{2}}{4} a}{\sqrt{a^{2}+\frac{9}{8} a^{2}}}=\frac{a}{3}
$$

解法二 (1) 如图 3, 过点 $E$ 作 $E G / / B_{1} D_{1}$, 交 $C B$ 的延长线于点 $G$, 从而有

$V_{E-B_{1} D_{1} C}=V_{G-B_{1} D_{1} C}=V_{D_{1}-B_{1} C G}=\frac{1}{3} \cdot S_{\triangle B_{1} C G} \cdot a=\frac{1}{3} \cdot \frac{1}{2} \cdot \frac{3 a}{2} \cdot a \cdot a=\frac{1}{4} a^{3}$.

(2) 连结 $A C$, 因为 $A C / / A_{1} C_{1}$, 所以点 $C$ 到平面 $E A_{1} C_{1}$ 的距离就等于点 $A$ 到平面 $E A_{1} C_{1}$ 的距离 $d$, 如图 4.

考虑四面体 $A-A_{1} C_{1} E$ 的体积:

$$
V_{A-A_{1} E_{1}}=\frac{1}{3} \cdot S_{\triangle A_{1} C_{1} E} \cdot d=V_{C_{1}-A E A_{1}}=\frac{1}{3} \cdot \frac{1}{2} \cdot \frac{a}{2} \cdot a \cdot a=\frac{1}{12} a^{3},
$$

而在 $\triangle A_{1} C_{1} E$ 中, 有

$$
A_{1} C_{1}=\sqrt{2} a, A_{1} E=\frac{\sqrt{5}}{2} a, C_{1} E=\frac{3}{2} a
$$

由余弦定理得 $\cos \angle E A_{1} C_{1}=\frac{1}{\sqrt{10}}$, 从而有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-212.jpg?height=335&width=341&top_left_y=651&top_left_x=1414)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-212.jpg?height=346&width=346&top_left_y=1049&top_left_x=1420)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-212.jpg?height=330&width=346&top_left_y=1477&top_left_x=1417)

图 4

$$
S_{\triangle A_{1} C_{1} E}=\frac{1}{2} \cdot \sqrt{2} a \cdot \frac{\sqrt{2}}{2} a \cdot \frac{3}{\sqrt{10}}=\frac{3}{4} a^{2}
$$

所以

$$
d=\frac{\frac{1}{12} a^{3}}{\frac{1}{3} \cdot \frac{3}{4} a^{2}}=\frac{1}{3} a
$$

## 第 778 题 摆正位置

已知三棱雉 $S-A B C$ 的底面 $\triangle A B C$ 为正三角形, 点 $A$ 在侧面 $S B C$ 上的投影 $H$ 是 $\triangle S B C$ 的垂心,二面角 $H-A B-C$ 的平面角的大小为 $30^{\circ}$, 且 $S A=2$, 则此三棱雉的体积为
A. $\frac{1}{2}$
B. $\frac{\sqrt{3}}{2}$
C. $\frac{\sqrt{3}}{4}$
D. $\frac{3}{4}$

## 解析 D.

如图, 设 $S$ 在底面上的投影为 $O$, 延长 $S H, B H$ 分别交 $B C, S C$ 于 $P, Q$ 两点.

因为 $A H \perp$ 平面 $S B C$, 则平面 $A B Q \perp$ 平面 $S B C$;

由题意 $H$ 为 $\triangle S B C$ 的垂心, 则 $S C \perp B Q$, 且平面 $A B Q \cap$ 平面 $S B C=B Q$, 故 $S C$ $\perp$ 平面 $A B Q$, 因此 $S C \perp A B$, 所以 $O C \perp A B$, 同理有 $A O \perp B C$, 因此 $O$ 为 $\triangle A B C$ 的垂心, 即中心. 也即 $S-A B C$ 为正三棱雉.

取 $A B$ 的中点 $M$, 则 $\angle Q M C$ 为二面角 $H-A B-C$ 的平面角, $\angle Q M C=30^{\circ}$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-213.jpg?height=380&width=345&top_left_y=692&top_left_x=1521)
$\angle Q C M=60^{\circ}$.

于是 $O C=S C \cdot \cos \angle Q C M=2 \cdot \cos 60^{\circ}=1$, 底面 $\triangle A B C$ 的边长为 $\sqrt{3}$,因此三棱雉体积为 $\frac{3}{4}$. 故选 D.

## 第 779 题 对边描述的四面体

如图 1,四面体 $A B C D$ 中, $A B$ 和 $C D$ 为对棱. 设 $A B=a, C D=b$, 且异面直线 $A B$ 与 $C D$ 的距离为 $d$, 夹角为 $\theta$.

(1)若 $\theta=\frac{\pi}{2}$, 且棱 $A B$ 垂直于平面 $B C D$, 求四面体 $A B C D$ 的体积;

(2) 当 $\theta=\frac{\pi}{2}$ 时,证明: 四面体 $A B C D$ 的体积为一定值;

(3)求四面体 $A B C D$ 的体积.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-213.jpg?height=270&width=308&top_left_y=1523&top_left_x=1526)

图 1解析 (1) 如图 2,

在平面 $B C D$ 中, 作 $B M \perp C D$ 于点 $M$, 则 $B M=d$. 所以

$$
\begin{aligned}
V_{A-B C D} & =\frac{1}{3} \cdot A B \cdot S_{\triangle B C D} \\
& =\frac{1}{3} \cdot a \cdot \frac{1}{2} b \cdot d \\
& =\frac{1}{6} a b d
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-213.jpg?height=284&width=289&top_left_y=1893&top_left_x=1571)

图 2

(2) 如图 3 , 过点 $A$ 作 $A M \perp C D$ 于点 $M$, 连结 $B M$.

由 $C D \perp$ 平面 $A B M$, 可得平面 $A M B \perp$ 平面 $B C D$, 过点 $M$ 作 $M N \perp A B$ 于点 $N$, 则 $M N=d$, 因此有

$$
V_{A-B C D}=\frac{1}{3} S_{\triangle A M B} \cdot C D=\frac{1}{6} a b d .
$$

(3) 如图 4, 将四面体补成平行六面体 $A B G H-E C F D$, 则 $A B$ 与 $C D$ 的距离即平行六面体上下底面间的距离.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-213.jpg?height=284&width=292&top_left_y=2267&top_left_x=1569)

图 3
在底面平行四边形 $E C F D$ 中,

$$
E C=a, C D=b, \sin \angle D C E=\sin \theta,
$$

于是

$$
\begin{aligned}
S_{B C F D} & =2 S_{\triangle D C E} \\
& =2 \cdot \frac{1}{2} \sin \theta \cdot a b \\
& =a b \sin \theta
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-214.jpg?height=281&width=461&top_left_y=198&top_left_x=1308)

图 4

所以

$$
V_{A-B C D}=\frac{1}{6} V_{A B G H-B C F D}=\frac{1}{6} a b d \sin \theta
$$

## 第 780 题 安全系数

想象把一个半径为 1 的单位球放进另一个半径为 $r(r>0)$ 的大球中滚动,那么大球内壁中的任何一个点都可以被小球碾压, 也就是对球体而言, 表面 (面积为 $S=4 \pi r^{2}$ ) 上安全的区域面积 $P$ 为 0 , 于是我们说半径为 $r$ 的球的安全系数

$$
\lambda(r)=\frac{P}{S}=0
$$

而棱长为 $a$ 的正方体安全系数会好一些, 为

$$
\lambda(a)=4 \cdot \frac{a-1}{a^{2}}, a>2,
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-214.jpg?height=374&width=401&top_left_y=937&top_left_x=1327)

图 1

现在的问题是,相同表面积的正方体和正四面体,哪个安全系数高一些?

解析 和处理正方体的方式类似,正四面体的每个面的安全区域如图 2 所示:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-214.jpg?height=213&width=240&top_left_y=1593&top_left_x=513)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-214.jpg?height=279&width=268&top_left_y=1527&top_left_x=1066)

图 3

难点在于确定安全区域的宽度. 为此, 作单位球的外切正四面体, 如图 3, 那么切点到其所在的面的任意一边的距离即安全区域的宽度.

用体积法可以求得单位球的外切正四面体的棱长为 $2 \sqrt{6}$, 于是安全区域的宽度为 $\sqrt{2}$, 进而可得危险区域与整个区域的相似比为

$$
\left(\frac{\sqrt{3}}{2} a-3 \sqrt{2}\right): \frac{\sqrt{3}}{2} a=(a-2 \sqrt{6}): a
$$

于是安全系数为

$$
f(a)=1-\left(\frac{a-2 \sqrt{6}}{a}\right)^{2}=4 \sqrt{6} \cdot \frac{a-\sqrt{6}}{a^{2}},
$$

其中 $a \geqslant 2 \sqrt{6}$. 图 4 为正方体 $(f(a))$ 和正四面体 $(g(a))$ 的安全系数与棱长的函数关系图.

事实上, 直接比较两者的安全系数可知, 正四面体的安全系数高于正方体. 这也和我们的感觉保持一致, 地震的时候果然应该船在狭窄的空间比较安全啊!

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-214.jpg?height=388&width=472&top_left_y=2160&top_left_x=1297)

图 4

## 第 781 题 云手化劲

如图 1, 正四面体 $A B C D$ 的棱长为 1 , 平面 $\alpha$ 是与棱 $A B$ 平行的平面, $E, F$ 分别是棱 $A D$ 和 $B C$ 的中点, 以 $A B$ 为轴将正四面体 $A B C D$ 旋转一周, 线段 $E F$ 在平面 $\alpha$上的投影 $E_{1} F_{1}$ 的范围是 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-215.jpg?height=252&width=274&top_left_y=460&top_left_x=1548)

图 1

解析 $\left[\frac{1}{2}, \frac{\sqrt{2}}{2}\right]$.

可以直接通过一些特殊位置确定 $E F$ 长度的取值范围是 $\left[\frac{\sqrt{2}}{2} E F, E F\right]$, 但严格求解的难度不小. 我们可以通过一些常见的转化来将这个复杂的问题逐步简化.

第一步转化: 正四面体的问题往往可以在其 “外接正方体”中研究, 这样更有利于数量和位置关系的推断, 如图 2.

由于研究的是线段 $E F$ 在平面 $\alpha$ 上的投影,因此可以取平面 $\alpha$ 为底面 $A B$. 同时, 正四面体绕 $A B$ 转动, 可以转化为底面 $A B$ 绕直线 $A B$ 转动. 容易计算得 $E F=\frac{\sqrt{2}}{2}$, 于是问题的关键就是在转动中 $E F$ 与平面 $\alpha$ 形成的线面角的取值范围.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-215.jpg?height=285&width=334&top_left_y=1071&top_left_x=1531)

图 2

第; 肾输化: 在平面 $\alpha$ 的旋转过程中需要探索的线面角难以研究, 因此将其转化为平面 $\alpha$ 的法线与 $E F$ 形成的线线角的取值范围, 如图 3.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-215.jpg?height=271&width=337&top_left_y=1508&top_left_x=522)

图 3

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-215.jpg?height=252&width=282&top_left_y=1512&top_left_x=1163)

图 4

此时, 平面 $\alpha$ 的法线可以取遍正四面体的外接正方体的包含 $C D$ 的对角面内的直线.

然后从复杂的图形中将相关部分提炼出来. 我们知道, $E F$ 与对角面所成的角为 $\frac{\pi}{4}$, 因此, 平面 $\alpha$ 的法线与 $E F$ 的线线角的取值范围是 $\left[\frac{\pi}{4}, \frac{\pi}{2}\right]$, 如图 4.

因此转动中 $E F$ 与平面 $\alpha$ 形成的线面角的取值范围是 $\left[0, \frac{\pi}{4}\right]$, 于是所求的投影 $E_{1} F_{1}$ 的取值范围是 $\left[\frac{1}{2}, \frac{\sqrt{2}}{2}\right]$.

在立体几何问题的解决过程中, 掌握一些常见的转化手法 (如同太极云手), 就可以将问题逐步转化为简单而容易解决的问题, 达到举重若轻的效果了.

# 第 782 题 形象转化 

\begin{abstract}
有四根长度都为 2 的直铁条,若再选两根长度都为 $a$ 的直铁条,使这六根铁条端点处相连能够淿接成一个三棱锥形铁架, 则 $a$ 的取值范围是 $\qquad$
解析 $(0, \sqrt{6}+\sqrt{2})$.

两根长为 $a$ 的铁条可以相交, 也可以异面, 且只有这两种情况,下面分别考虑.

情形一 如果这两根铁条相交 (不妨作为侧棱), 则此三棱雉底面固定, 有一条侧棱的长度固定为 2 , 且此侧棱在底面上的投影一定在底面中线所在直线上, 让该侧棱在经过底面某条边的高且垂直于底面的平面中旋转.

边界情况为这六根铁条共面时,如图 1 所示:

根据三射线定理,长为 $a$ 的棱所对的内角单调变化.

由余弦定理易求得边界的值为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-216.jpg?height=267&width=377&top_left_y=719&top_left_x=1394)

图 1

$$
\sqrt{8 \pm 4 \sqrt{3}}=\sqrt{6} \pm \sqrt{2}
$$

所以此时 $a$ 的取值范围为

$$
(\sqrt{6}-\sqrt{2}, \sqrt{6}+\sqrt{2})
$$

情形ニ 如果这两根铁条异面, 可以看成两块等腰三角板 (边长为 $2,2, a$ ) 拼在一起 (如图加阴影的两个侧面), 像两个“翅膀”扇动起来, 使得“翅尖”连线与等腰三角形的底面边长相等.

不论 $a$ 多小,都可以构成三棱锥, 让“翅尖”互相靠近即可; 但 $a$ 不能太大, 否则即使“翅尖”距离达到最大值 (即翅膀展开成平面), “翅尖”之间的距离仍然小于等于 $a$, 如图 3 所示.

所以要构成三棱锥需要满足

$$
2 \sqrt{4-\left(\frac{a}{2}\right)^{2}}>a
$$

解得 $a<2 \sqrt{2}$.

综合两种情况知, $a$ 的取值范围为 $(0, \sqrt{6}+\sqrt{2})$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-216.jpg?height=254&width=246&top_left_y=1234&top_left_x=1525)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-216.jpg?height=148&width=224&top_left_y=1560&top_left_x=1544)

图 3

## 第 783 题 欧拉公式

利用欧拉公式(多面体的顶点数 $V$, 面数 $F$, 棱数 $E$ 满足 $V+F-E=2$ ) 推导:

(1) 正多面体不超过 5 种;

(2) 足球由 12 个正五边形和 20 个正六边形构成.

解析 (1) 假设正多面体的每个面都是正 $n$ 边形, 且每个顶点出发的棱数为 $m$, 那么

$$
2 E=n F=m V
$$

于是

$$
V=\frac{2 E}{m}, F=\frac{2 E}{n}
$$

代人欧拉公式, 有

$$
\frac{2 E}{m}+\frac{2 E}{n}-E=2
$$

也即

$$
\frac{1}{m}+\frac{1}{n}=\frac{1}{2}+\frac{1}{E}
$$

因此

$$
\frac{1}{m}+\frac{1}{n}>\frac{1}{2}
$$

结合 $m, n \geqslant 3$ 可知 $m, n$ 至少有一个是 3 , 因此所有可能的正整数解 $(m, n)$ 为

$$
(3,3),(3,4),(3,5),(4,3),(5,3),
$$

共 5 组, 因此正多面体不超过 5 种.

事实上,这五种正多面体都可以作出,分别为正四面体、正六面体、正八面体、正十二面体和正二十面体. (2)假设足球由 $x$ 个正五边形(黑色)和 $y$ 个正六边形构成,那么

$$
V=5 x, F=x+y, E=5 x+\frac{3}{2} y
$$

代人欧拉公式并化简可得.

另一方面, 考虑所有正五边形的边数之和, 有 $\left\{\begin{array}{l}2 x-y=4, \\ 5 x=3 y,\end{array}\right.$

从而根据两个方程可以解得

$$
x=12, y=20,
$$

因此命题得证.

## 第 784 题 四点共球

已知空间四边形 $A B C D$ 的四个顶点都在球 $O$ 的球面上, $E, F$ 分别是 $A B, C D$ 的中点, 且 $E F \perp A B$, $E F \perp C D$. 若 $A B=E F=4, C D=8$, 则球 $O$ 的半径为

解析 $\frac{\sqrt{65}}{2}$.

如图, 线段 $A B$ 和 $C D$ 分别是圆台两个底面的直径, $E F$ 是连结底面中心的线段.

根据题意, 球 $O$ 的半径 $r$ 满足

$$
r^{2}=O E^{2}+\left(\frac{1}{2} A B\right)^{2}=O F^{2}+\left(\frac{1}{2} C D\right)^{2}
$$

于是

$$
O E^{2}-O F^{2}=\left(\frac{1}{2} C D\right)^{2}-\left(\frac{1}{2} A B\right)^{2}=12
$$

因此点 $O$ 在线段 $E F$ 上,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-217.jpg?height=364&width=394&top_left_y=1839&top_left_x=1463)

$$
O E+O F=4, O E-O F=3,
$$

于是 $O F=\frac{1}{2}$, 进而所求半径

$$
r=\sqrt{O F^{2}+\left(\frac{1}{2} C D\right)^{2}}=\frac{\sqrt{65}}{2}
$$

## 第 785 题 四面㑛的外接平行六面体

在四面体 $A B C D$ 中, $A B=C D=5, A C=B D=\sqrt{34}, A D=B C=\sqrt{41}$, 则四面体 $A B C D$ 外接球的表面积是 $\qquad$
解析 $50 \pi$.

我们知道, 任何一个四面体都可以补成一个平行六面体, 称这个平行六面体是四面体的外接平行六面体.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-218.jpg?height=204&width=778&top_left_y=772&top_left_x=520)

特别地, 如果四面体的对棱分别相等, 那么其外接平行六面体为长方体; 如果四面体对棱分别垂直, 那么其外接平行六面体的每个面均为菱形;正四面体的外接平行六面体为正方体.

在本题中, 易得四面体 $A B C D$ 的外接平行六面体是长宽高分别为 $3,4,5$ 的长方体, 其外接球亦为该长方体的外接球. 于是外接球半径 $r$ 为长方体的体对角线长的一半,外接球的表面积为

$$
4 \pi r^{2}=\pi \cdot\left(3^{2}+4^{2}+5^{2}\right)=50 \pi
$$

## 第 786 题 长方体中的四面体

如图 1, 四面体 $O A B C$ 的三条棱 $O A, O B, O C$ 两两垂直, $O A=O B=2, O C=3, D$ 为四面体 $O A B C$ 外一点. 给出下列命题:

(1)不存在点 $D$, 使四面体 $A B C D$ 有三个面是直角三角形;

(2) 不存在点 $D$, 使四面体 $A B C D$ 是正三棱雉;

(3) 存在点 $D$, 使 $C D$ 与 $A B$ 垂直并且相等;

(4) 存在无数个点 $D$, 使 $O$ 在四面体 $A B C D$ 的外接球球面上.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-218.jpg?height=267&width=210&top_left_y=1496&top_left_x=1505)

图 1

其中真命题的序号是

## 解析 (3)(4).

先考虑(1), 因为点 $O$ 满足条件, 作 $O$ 点关于平面 $A B C$ 的对称点 $D$, 则 $D$ 满足要求, 且点 $D$ 在四面体外, (1)错误; 事实上, 对于任何一个锐角三角形, 都可以找到一个长方体, 使得这个锐角三角形的三边长与长方体的三条面对角线长对应相等, 从而可以构造出一个四面体, 顶点处的三条侧棱两两垂直, 且底面为该锐角三角形.

再考虑(2), 因为 $\triangle A B C$ 是等腰三角形, 腰长为 $\sqrt{13}$, 底边长为 $2 \sqrt{2}$, 所以直接构造一个正三棱锥, 使得它的侧棱长为 $\sqrt{13}$, 底面边长为 $2 \sqrt{2}$ 即可, 故(2)错误, 事实上, 只有当等腰三角形的腰长与上底边长的比值小于等于 $\frac{\sqrt{3}}{3}$ 时, 才找不到正三棱雉, 其他时候都可以.

对于(3)(4),我们熟知正四面体的问题一般都放人正方体中处理,这个四面体中三

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-218.jpg?height=309&width=314&top_left_y=2182&top_left_x=1437)

图 2 条棱两两垂直,所以可以放人长方体中处理, 如图 2:

## 高考数学满分学霸的解题笔记(一千零一题)

上底面的对角线 $C D$ 就满足: $C D \perp A B$, 且 $C D=A B$, 故 (3)正确, 这样的点 $D$ 有无穷多个, 过点 $C$ 作 $A B$的垂面 (即平面 $O C D$ ), 在平面内以 $C$ 为圆心、 $A B$ 为半径作圆, 则圆在四面体 $O A B C$ 外面的部分对应的点都满足要求.

作长方体的外接球, 也是四面体的外接球, 在球面上任取一点 $D$, 则点 $O$ 一定在四面体 $A B C D$ 的外接球球面上,这样的点 $D$ 有无穷多个, (4)正确.

## 第 787 题 㑛积转化

如图 1, 在三棱雉 $O-A B C$ 中, 三条棱 $O A, O B, O C$ 两两垂直, 且 $O A>O B>O C$,分别经过三条棱 $O A, O B, O C$ 作一个截面平分三棱雉的体积, 截面面积依次为 $S_{1}$, $S_{2}, S_{3}$, 则 $S_{1}, S_{2}, S_{3}$ 的大小关系为 $\qquad$ .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-219.jpg?height=215&width=279&top_left_y=721&top_left_x=1569)

图 1

## 解析 $S_{1}>S_{2}>S_{3}$.

三棱锥通常都可以放人长方体中进行分析, 因为三棱锥的三条棱两两垂直, 所以可以直接放人以 $O A, O B, O C$ 为同顶点的三条棱的长方体中.

先分析过棱 $O A$ 的截面, 此截面要平分三棱锥的体积, 故它与平面 $O B C$ 的交线平分 $\triangle O B C$ 的面积, 所以它就是长方体中包含 $O A$ 的对角面 $O A E F$ 在三棱雉内的部分,如图 2, 它的面积为此对角面 $O A E F$ 面积的 $\frac{1}{4}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-219.jpg?height=268&width=299&top_left_y=1026&top_left_x=1570)

图 2

故比较长方体的三个对角面的面积即可, 设

$$
O A=a, O B=b, O C=c,
$$

则包含 $O A$ 的对角面的面积为

$$
4 S_{1}=a \sqrt{b^{2}+c^{2}}=\sqrt{a^{2} b^{2}+a^{2} c^{2}}
$$

同理有

$$
4 S_{2}=b \sqrt{a^{2}+c^{2}}=\sqrt{a^{2} b^{2}+b^{2} c^{2}}, 4 S_{3}=c \sqrt{a^{2}+b^{2}}=\sqrt{a^{2} c^{2}+b^{2} c^{2}},
$$

因为 $a>b>c$, 所以有 $S_{1}>S_{2}>S_{3}$.

在解题过程中可以直接给 $O A, O B, O C$ 进行赋值, 比如 $3,2,1$, 之后再比较.

## 第 788 题 四面体的外接球

已知三棱锥 $P-A B C$ 的底面是边长为 2 的等边三角形, 若 $P A=P B=\sqrt{2}$, 二面角 $P-B A-C$ 的平面角的大小为 $60^{\circ}$, 则三棱雉 $P-A B C$ 的外接球半径 $R=$

解析 $\frac{\sqrt{13}}{3}$.
如图 1, 设 $M$ 为 $A B$ 的中点. 容易知道, 三棱雉 $P-A B C$ 的外接球的球心在平面 $P M C$ 中. 接下来, 我们在平面 $P M C$ 中研究外接球球心 $O$ 的位置. 如图 2.

事实上,点 $O$ 在任何一个面上的投影都是这个面的外心,于是点 $O$ 在底面 $A B C$ 上的投影位置是其中心 $Q$, 而在侧面 $P A B$ 上的投影位置就是 $M$ (注意到 $\triangle P A B$ 为直角三角形, $A B$ 为斜边).

接下来的计算很容易, $M Q=\frac{\sqrt{3}}{3}$, 而 $\angle O M Q=30^{\circ}$, 因此 $O Q=\frac{1}{3}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-220.jpg?height=236&width=307&top_left_y=309&top_left_x=1116)

图 1 进而

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-220.jpg?height=214&width=263&top_left_y=309&top_left_x=1486)

图 2

$$
R=O C=\sqrt{O Q^{2}+Q C^{2}}=\frac{\sqrt{13}}{3}
$$

在求解与四面体的外接球球心相关的问题时,需要牢牢记住外接球的球心在任何一个面上的投影都是这个面的外心. 此外还需注意直角三角形的外心就是斜边中点.

## 第 789 题各就各“位”

如图 1, 点 $M$ 是棱长为 2 的正方体 $A B C D-A_{1} B_{1} C_{1} D_{1}$ 的棱切球上的一点,点 $N$ 是 $\triangle A C B_{1}$ 的外接圆上的一点, 则线段 $M N$ 的取值范围是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-220.jpg?height=343&width=357&top_left_y=1254&top_left_x=1376)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-220.jpg?height=312&width=362&top_left_y=1650&top_left_x=1392)

图 2

解析 $[\sqrt{3}-\sqrt{2}, \sqrt{3}+\sqrt{2}]$.

如图 2, 棱切球的半径为 $\sqrt{2}$, 而球心到 $\triangle A C B_{1}$ 的外接圆上任意一点的距离均为 $\sqrt{3}$, 因此所求的取值范围是 $[\sqrt{3}-\sqrt{2}, \sqrt{3}+\sqrt{2}]$.

## 第十章 $\quad$ 代数变形

## 第 790 题 “存在”的反面

已知 $a_{1}+a_{2}+\cdots+a_{10}=30, a_{1} a_{2} \cdots a_{10}<21$, 求证: $a_{1}, a_{2}, \cdots, a_{10}$ 中必有一个小于 1 .

解析 用反证法.

设 $a_{1}, a_{2}, \cdots, a_{10} \geqslant 1$.

令 $b_{i}=a_{i}-1(i=1,2, \cdots, 10)$, 则

$$
\begin{aligned}
& b_{1}+b_{2}+\cdots+b_{10}=20 \\
& \left(b_{1}+1\right)\left(b_{2}+1\right) \cdots\left(b_{10}+1\right)<21
\end{aligned}
$$

而

$$
\left(b_{1}+1\right)\left(b_{2}+1\right) \cdots\left(b_{10}+1\right) \geqslant 1+\left(b_{1}+b_{2}+\cdots+b_{10}\right)=21
$$

矛盾.

因此原命题得证.

## 第 791 题 利用方程进行递推

已知实数 $a, b, x, y$ 满足

$$
\left\{\begin{array}{l}
a x+b y=3 \\
a x^{2}+b y^{2}=7 \\
a x^{3}+b y^{3}=16 \\
a x^{4}+b y^{4}=42
\end{array}\right.
$$

求 $a x^{5}+b y^{5}$ 的值.

解析 记 $A_{n}=a x^{n}+b y^{n}$, 其中 $n=1,2, \cdots$, 则

$$
A_{n}=(x+y) A_{n-1}-x y A_{n-2}, n \geqslant 3,
$$

分别取 $n=3,4$ 可得

$$
\left\{\begin{array}{l}
7(x+y)-3 x y=16 \\
16(x+y)-7 x y=42
\end{array}\right.
$$

解得

$$
\left\{\begin{array}{l}
x+y=-14 \\
x y=-38
\end{array}\right.
$$

因此

$$
A_{5}=-14 A_{4}+38 A_{3}=20
$$

在上述解法中可以注意到 $x+y$ 与 $x y$, 联想韦达定理, 可以改写解法如下.

设 $x, y$ 是方程

$$
t^{2}=\alpha \cdot t+\beta
$$

的两根, 则

$$
\begin{gathered}
a x^{n}=\alpha \cdot a x^{n-1}+\beta \cdot a x^{n-2} \\
b y^{n}=\alpha \cdot b y^{n-1}+\beta \cdot b y^{n-2}
\end{gathered}
$$

于是就有

$$
a x^{n}+b y^{n}=\alpha\left(a x^{n-1}+b y^{n-1}\right)+\beta\left(a x^{n-2}+b y^{n-2}\right),
$$

以下略.

## 第 792 题 比较大小

已知 $a>0, a^{2}-2 a b+c^{2}=0, b c>a^{2}$, 试比较 $a, b, c$ 的大小.

解析 根据题意, 有

$$
\left\{\begin{array}{l}
1-2 \cdot \frac{b}{a}+\left(\frac{c}{a}\right)^{2}=0 \\
\frac{b}{a} \cdot \frac{c}{a}>1
\end{array}\right.
$$

令 $\frac{b}{a}=x, \frac{c}{a}=y$, 则

$$
\left\{\begin{array}{l}
y^{2}-2 x+1=0 \\
x y>1
\end{array}\right.
$$

由于 $b=\frac{a^{2}+c^{2}}{2 a}>0$, 又 $b c>a^{2}>0$, 于是 $x>0, y>0$, 因此

$$
\left\{\begin{array}{l}
y=\sqrt{2 x-1} \\
y>\frac{1}{x}
\end{array}\right.
$$

如图作出可行域.

由图可得 $x>y>1$, 于是 $b>c>a$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-222.jpg?height=360&width=446&top_left_y=1639&top_left_x=1312)

利用函数图象将方程直观地表示出来, 通过函数图象与直线 $y=x$ 的位置关系判断大小.

## 第 793 题 换元与化齐次

已知正数 $a, b$ 满足 $a+b+\frac{1}{a}+\frac{9}{b}=10$, 则 $a+b$ 的取值范围是

解析 $[2,8]$.

设 $u=a+b$, 则

$$
\frac{1}{a}+\frac{9}{b}=10-u
$$

于是

$$
\left(\frac{1}{a}+\frac{9}{b}\right) \cdot(a+b)=u(10-u)
$$

即

$$
u(10-u)=10+\frac{b}{a}+\frac{9 a}{b} \geqslant 16
$$

解得

$$
2 \leqslant u \leqslant 8
$$

事实上, 当 $(a, b)=\left(\frac{1}{2}, \frac{3}{2}\right)$ 时, $a+b=2$; 当 $(a, b)=(2,6)$ 时, $a+b=8$.

结合连续性, 可得 $a+b$ 的取值范围是 $[2,8]$.

解决问题的关键是设法建立一个关于 $a+b$ 的不等式, 得到取值的必要条件后再加以论证.

## 第 794 题 消元

已知互不相等的四个实数 $a, b, c, d$ 满足

$$
a+\frac{1}{b}=b+\frac{1}{c}=c+\frac{1}{d}=d+\frac{1}{a}=x,
$$

求 $x$ 的所有可能的值.

解析 题中有 $a, b, c, d, x$ 共 5 个未知数, 给出了 4 个方程. 因此我们可以采用消元的策略, 得到关于 $x$和另外一个未知数 (不妨取 $a$ ) 的等式后求解. 依次消元, 根据条件有

$$
\begin{gathered}
d=x-\frac{1}{a} \\
c=x-\frac{1}{d}=\frac{a x^{2}-x-a}{a x-1} \\
b=x-\frac{1}{c}=\frac{a x^{3}-x^{2}-2 a x+1}{a x^{2}-x-a} \\
a=x-\frac{1}{b}=\frac{a x^{4}-x^{3}-3 a x^{2}+2 x+a}{a x^{3}-x^{2}-2 a x+1}
\end{gathered}
$$

整理得

$$
x\left(x^{2}-2\right)\left(a^{2}-x a+1\right)=0,
$$

于是

$$
x=0 \text { 或 } x= \pm \sqrt{2} \text { 或 } x=a+\frac{1}{a} \text {. }
$$

经验证, 只有 $x= \pm \sqrt{2}$ 符合题意.

接下来进行检验.

情形 $-x=0$. 此时 $a=-\frac{1}{b}=c$, 与题意不符;

情形二 $x= \pm \sqrt{2}$. 当 $(a, b, c, d)=(1, \sqrt{2}+1,-1, \sqrt{2}-1)$ 时, $x=\sqrt{2}$; 而当 $(a, b, c, d)=(-1,-\sqrt{2}-1$, $1,-\sqrt{2}+1)$ 时, $x=-\sqrt{2}$, 符合题意.

情形三 $\quad x=a+\frac{1}{a}$. 此时 $a=b$, 与题意不符.

综上所述, $x$ 的所有可能的值为 $\pm \sqrt{2}$.

遇到多个变元的问题时, 消元或者对称化都是有用的思考方向.

## 第 795 题 消元

已知 $x, y \in \mathbf{R}, \theta \in\left(\frac{\pi}{4}, \frac{\pi}{2}\right)$, 且满足

$$
\left\{\begin{array}{l}
\frac{\sin \theta}{x}=\frac{\cos \theta}{y} \\
\frac{\cos ^{2} \theta}{x^{2}}+\frac{\sin ^{2} \theta}{y^{2}}=\frac{10}{3\left(x^{2}+y^{2}\right)}
\end{array}\right.
$$

求 $\frac{x}{y}$ 的值.

解析 已知条件中有三个变量, 但只有两个方程, 欲求的式子中不含 $\theta$, 因此代数变形的策略应是想办法消去 $\theta$.

令 $\frac{x}{y}=t$, 则

$$
\sin \theta=t \cos \theta
$$

因此结合

$$
\sin ^{2} \theta+\cos ^{2} \theta=1
$$

得

$$
\sin ^{2} \theta=\frac{t^{2}}{t^{2}+1}, \cos ^{2} \theta=\frac{1}{t^{2}+1}
$$

代人第二个式子中有

$$
\frac{1}{t^{2}+1} \cdot \frac{x^{2}+y^{2}}{x^{2}}+\frac{t^{2}}{t^{2}+1} \cdot \frac{x^{2}+y^{2}}{y^{2}}=\frac{10}{3},
$$

进而有

$$
\frac{1}{t^{2}+1} \cdot \frac{t^{2}+1}{t^{2}}+\frac{t^{2}}{t^{2}+1} \cdot\left(t^{2}+1\right)=\frac{10}{3}
$$

化简得

$$
3 t^{4}-10 t^{2}+3=0
$$

解得

$$
t= \pm \frac{\sqrt{3}}{3} \text { 或 } t= \pm \sqrt{3} \text {. }
$$

由于 $t=\tan \theta \in(1,+\infty)$, 因此所求 $\frac{x}{y}$ 的值为 $\sqrt{3}$.

## 第 796 题 代数与几何

已知 $\ln a-\ln 3=\ln c, b d=-3$, 求 $(a-b)^{2}+(c-d)^{2}$ 的最小值.

解析 解法一 根据已知, 有 $a=3 c$ 且 $c>0$, 于是

$$
\begin{aligned}
(a-b)^{2}+(c-d)^{2} & =\left(3 c+\frac{3}{d}\right)^{2}+(c-d)^{2} \\
& =10 c^{2}+\left(\frac{18}{d}-2 d\right) c+\frac{9}{d^{2}}+d^{2} \\
& =10\left[c+\frac{1}{10}\left(\frac{9}{d}-d\right)\right]^{2}+\frac{9}{10}\left(d^{2}+\frac{1}{d^{2}}\right)+\frac{9}{5} \\
& \geqslant \frac{18}{5}
\end{aligned}
$$

等号当

$$
\left\{\begin{array}{l}
c+\frac{1}{10}\left(\frac{9}{d}-d\right)=0 \\
d^{2}=1 \\
c>0
\end{array}\right.
$$

时, 也即 $d=-1, c=\frac{4}{5}$ 时取得, 因此所求代数式的最小值为 $\frac{18}{5}$.

解法二 根据已知, 有 $a=3 c$ 且 $c>0$, 因此题中代数式为射线 $y=3 x(x>0)$ 上的点 $A(c, 3 c)$ 到函数 $y=-\frac{3}{x}$ 上的点 $B\left(d,-\frac{3}{d}\right)$ 的距离的平方.

由几何意义如图, 考虑函数 $y=-\frac{3}{x}$ 的斜率为 3 的切线, 切点 $T$ 的横坐标 $t$ 满足

$$
\frac{3}{t^{2}}=3
$$

取 $T(-1,3)$, 则过点 $T$ 作射线 $y=3 x(x>0)$ 的垂线, 可得所求代数式的最小值为

$$
d^{2}=\left(\frac{|3 \cdot(-1)-3|}{\sqrt{3^{2}+(-1)^{2}}}\right)^{2}=\frac{18}{5}
$$

## 第 797 题 单刀直入

设 $a$ 为实数, 若函数 $y=\frac{1}{x}$ 的图象上存在三个不同的点 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right), C\left(x_{3}, y_{3}\right)$ 满足

$$
x_{1}+y_{2}=x_{2}+y_{3}=x_{3}+y_{1}=a,
$$

则 $a$ 的值为

解析 $\pm 1$.

条件即

$$
x_{1}+\frac{1}{x_{2}}=x_{2}+\frac{1}{x_{3}}=x_{3}+\frac{1}{x_{1}}=a .
$$

这里共有 4 个未知数, 但只有 3 个方程, 可以考虑用消元的策略解决问题.

根据条件, 有

$$
x_{3}=\frac{a x_{1}-1}{x_{1}}
$$

从而

$$
x_{2}=a-\frac{1}{x_{3}}=\frac{\left(a^{2}-1\right) x_{1}-a}{a x_{1}-1},
$$

进而由 $x_{1}+\frac{1}{x_{2}}=a$ 可得

$$
x_{1}+\frac{a x_{1}-1}{\left(a^{2}-1\right) x_{1}-a}=a,
$$

整理得

$$
\left(a^{2}-1\right)\left(x_{1}^{2}+1-a x_{1}\right)=0,
$$

于是

$$
a= \pm 1 \text { 或 } a=x_{1}+\frac{1}{x_{1}} .
$$

一方面,若 $a=1$, 取 $x_{1}=-1$, 则 $x_{3}=2, x_{2}=\frac{1}{2}$, 于是 $a$ 可以取得 1 ; 类似的, 当 $x_{1}=1, x_{3}=-2, x_{2}=-\frac{1}{2}$时, $a$ 可以取得 -1 .

另一方面, 若 $a=x_{1}+\frac{1}{x_{1}}$, 则 $x_{2}=x_{1}$, 与“ $A, B, C$ 是不同的三点”矛盾.

综上所述, $a$ 的值为 $\pm 1$.

## 第 798 题 纠缠的三边

已知 $a, b, c$ 是三角形的三边长, 若 $|a-b| \leqslant|a-c|,|a-b| \leqslant|b-c|$, 则 $\frac{b}{a}$ 的取值范围是

解析 $\left(\frac{1}{2}, 2\right)$.

根据题意, 由于 $|a-c|<b$ 且 $|b-c|<a$, 于是有

$$
\left\{\begin{array}{l}
|a-b|<b \\
|a-b|<a
\end{array}\right.
$$

整理得 $\frac{1}{2}<\frac{b}{a}<2$. 而当 $(a, b, c) \rightarrow(1,2,3)$ 时, $\frac{b}{a} \rightarrow 2$; 当 $(a, b, c) \rightarrow(2,1,3)$ 时, $\frac{b}{a} \rightarrow \frac{1}{2}$,因此 $\frac{b}{a}$ 的取值范围是 $\left(\frac{1}{2}, 2\right)$.

## 第 799 题 消元与转化

证明: $(x, y)=(1,2)$ 是方程组 $\left\{\begin{array}{l}x(x+y)^{2}=9, \\ x\left(y^{3}-x^{3}\right)=7\end{array}\right.$ 的唯一实数解.

解析 根据题意, 显然有 $y>x>0$, 从而由第一个方程可得 $y=\frac{3}{\sqrt{x}}-x$, 代人第二个方程有

$$
x\left[\left(\frac{3}{\sqrt{x}}-x\right)^{3}-x^{3}\right]=7,
$$

令 $\sqrt{x}=m$ 并整理得

$$
2 m^{9}-9 m^{6}+27 m^{3}+7 m-27=0,
$$

即

$$
(m-1)\left(2 m^{8}+2 m^{7}+2 m^{6}-7 m^{5}-7 m^{4}-7 m^{3}+20 m^{2}+20 m+27\right)=0,
$$

显然有

$$
\left(2 m^{8}+20 m^{2}\right)+\left(2 m^{7}+20 m\right)+\left(2 m^{6}+27\right) \geqslant 2 \sqrt{40} m^{5}+2 \sqrt{40} m^{4}+2 \sqrt{54} m^{3},
$$

因此关于 $m$ 的方程有且只有实数根 $m=1$, 进而原命题得证.

## 第 800 题 复数的三角形式

已知两个非零复数 $x, y$ 的立方和为 0 , 则 $\left(\frac{x}{x-y}\right)^{2000}+\left(\frac{y}{y-x}\right)^{2000}$ 的值为

解析 $\frac{1}{2^{1999}}$ 或 -1 .

根据题意, 有 $x^{3}+y^{3}=0$, 于是

$$
(x+y)\left(x^{2}-x y+y^{2}\right)=0
$$

若 $x+y=0$, 则

$$
\left(\frac{x}{x-y}\right)^{2000}=\left(\frac{y}{y-x}\right)^{2000}=\frac{1}{2^{2000}},
$$

于是原式的值为 $\frac{1}{2^{1999}}$.

若 $x^{2}-x y+y^{2}=0$, 设 $z=\frac{x}{y}$, 则

$$
z^{2}-z+1=0
$$

进而 $z=\cos \frac{\pi}{3}+\mathrm{i} \cdot \sin \frac{\pi}{3}$ 或 $\bar{z}=\cos \frac{\pi}{3}+\mathrm{i} \cdot \sin \frac{\pi}{3}$, 进而

$$
\begin{aligned}
\left(\frac{x}{x-y}\right)^{2000}+\left(\frac{y}{y-x}\right)^{2000} & =\left(\frac{z}{z-1}\right)^{2000}+\left(\frac{1}{1-z}\right)^{2000} \\
& =\left(\frac{z^{2}}{z^{2}-z}\right)^{2000}+\left(\frac{1}{-z^{2}}\right)^{2000} \\
& =z^{4000}+\bar{z}^{4000} \\
& =2 \cos \frac{4000 \pi}{3} \\
& =-1
\end{aligned}
$$

综上所述, 所求代数式的值为 $\frac{1}{2^{1999}}$ 或 -1 .

## 第 801 题 逐步消元

已知函数 $f(x)=x^{2}+a x+b(a, b \in \mathbf{R})$ 在区间 $(0,1]$ 上有零点 $x_{0}$, 则 $a b\left(\frac{x_{0}}{4}+\frac{1}{9 x_{0}}\right)-\frac{1}{3}$ 的最大值是

解析 $\frac{1}{144}$.

根据题意, 有

$$
\begin{aligned}
a b\left(\frac{x_{0}}{4}+\frac{1}{9 x_{0}}-\frac{1}{3}\right) & =a \cdot\left(-x_{0}^{2}-a x_{0}\right) \cdot\left(\frac{x_{0}}{4}+\frac{1}{9 x_{0}}-\frac{1}{3}\right) \\
& =\frac{1}{36} a\left(-x_{0}-a\right)\left(3 x_{0}-2\right)^{2} \\
& \leqslant \frac{1}{36} \cdot \frac{x_{0}^{2}}{4} \cdot\left(3 x_{0}-2\right)^{2} \\
& =\frac{1}{144} \cdot\left[x_{0}\left(3 x_{0}-2\right)\right]^{2} \\
& \leqslant \frac{1}{144}
\end{aligned}
$$

等号当 $x_{0}=1, a=-\frac{1}{2}$ 时取得. 因此所求的最大值为 $\frac{1}{144}$.

## 第 802 题 步步为营

若二次函数 $f(x)=a x^{2}+b x+c(a, b, c>0)$ 有零点, 则 $\min \left\{\frac{b+c}{a}, \frac{c+a}{b}, \frac{a+b}{c}\right\}$ 的最大值为

解析 $\frac{5}{4}$.

不妨令 $b=2$, 则由二次函数 $f(x)=a x^{2}+b x+c$ 有零点可得 $a c \leqslant 1$, 此时

$$
\min \left\{\frac{b+c}{a}, \frac{c+a}{b}, \frac{a+b}{c}\right\}=\min \left\{\frac{a+c}{2}, \frac{c+2}{a}, \frac{a+2}{c}\right\} .
$$

注意到 $a, c$ 对称, 不妨设 $a \leqslant c$, 于是 $0<a \leqslant 1$, 且有

$$
\frac{c+2}{a} \geqslant \frac{a+2}{c}
$$

从而

$$
\min \left\{\frac{a+c}{2}, \frac{c+2}{a}, \frac{a+2}{c}\right\}=\min \left\{\frac{a+c}{2}, \frac{a+2}{c}\right\}
$$

进而当 $c \geqslant 2$ 时, 有

$$
\min \left\{\frac{a+c}{2}, \frac{a+2}{c}\right\}=\frac{a+2}{c} \leqslant \frac{\frac{1}{2}+2}{2}=\frac{5}{4}
$$

当 $a \leqslant c<2$ 时, 有

$$
\min \left\{\frac{a+c}{2}, \frac{a+2}{c}\right\}=\frac{a+c}{2}
$$

此时若 $0<a \leqslant \frac{1}{2}$, 则

$$
\frac{a+c}{2}<\frac{\frac{1}{2}+2}{2}=\frac{5}{4}
$$

若 $\frac{1}{2}<a<1$, 则

$$
\frac{a+c}{2} \leqslant \frac{a+\frac{1}{a}}{2}<\frac{5}{4}
$$

综上所述, 所求的最大值为 $\frac{5}{4}$. 当 $a: b: c=1: 4: 4$ 或 $a: b: c=4: 4: 1$ 时取到.

结合代数式的特点, 先利用齐次, 不妨设 $b=2$, 然后利用形式上的对称适当进行分类讨论.

## 第 803 题 不等式的证明

已知 $|a|,|b|,|c| \leqslant 1$, 求证 $: a b+b c+c a \geqslant-1$.

解析 解法一

不妨设 $b+c \geqslant 0$, 则由于 $|a| \leqslant 1$, 而 $a b+b c+c a=(b+c) a+b c$, 于是

$$
a b+b c+c a \geqslant-(b+c)+b c=(b-1)(c-1)-1 \geqslant-1
$$

解法二 根据题意, 有

$$
2(a b+b c+c a+1)=(a+1)(b+1)(c+1)-(a-1)(b-1)(c-1) \geqslant 0 .
$$

解法三 由于 $a+b, b+c, c+a$ 中必然有两个数乘积不小于 0 , 不妨设 $(a+b)(b+c) \geqslant 0$, 则

$$
a b+b c+c a=(a+b)(b+c)-b^{2} \geqslant-b^{2} \geqslant-1
$$

## 第 804 题 代数式的最值

已知 $2 x+y=1$, 求 $x+\sqrt{x^{2}+y^{2}}$ 的最值.
解析 解法一 令 $m=x+\sqrt{x^{2}+y^{2}}$, 则

$$
x=\frac{m^{2}-y^{2}}{2 m}
$$

因此

$$
2 \cdot \frac{m^{2}-y^{2}}{2 m}+y=1
$$

整理得

$$
y^{2}-m y+m-m^{2}=0
$$

从而判别式

$$
\Delta=m^{2}-4\left(m-m^{2}\right) \geqslant 0,
$$

解得

$$
m \geqslant \frac{4}{5}
$$

其中用到了 $m=x+\sqrt{x^{2}+y^{2}} \geqslant \sqrt{x^{2}+y^{2}}-\sqrt{x^{2}} \geqslant 0$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-230.jpg?height=352&width=265&top_left_y=558&top_left_x=1505)

图 1

解法二 情形一 如图 1,

当 $x \geqslant 0$ 时, 设 $P$ 为直线 $2 x+y=1$ 上的一点, 则

$$
x+\sqrt{x^{2}+y^{2}}=P O+P H
$$

根据“将军饮马”问题, $P O+P H$ 有最小值, 为点 $O$ 关于直线 $2 x+y=1$ 的对称点 $Q\left(\frac{4}{5}, \frac{2}{5}\right)$ 到 $y$ 轴的距离 $\frac{4}{5}$.

情形二 如图 2,

当 $x<0$ 时, 设 $P$ 为直线 $2 x+y=1$ 上的一点, 则

$$
x+\sqrt{x^{2}+y^{2}}=P O-P H
$$

而

$$
\mathrm{PO}>\mathrm{OH}=\mathrm{OB}+2 \mathrm{PH}>1+\mathrm{PH}
$$

于是

$$
P O-P H>1 \text {. }
$$

综合以上, 所求代数式的最小值为 $\frac{4}{5}$, 不存在最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-230.jpg?height=355&width=287&top_left_y=1332&top_left_x=1478)

图 2

解法三 设 $x=r \cos \theta, y=r \sin \theta, r>0$, 则条件转化为

$$
2 r \cos \theta+r \sin \theta=1
$$

所求代数式转化为

$$
r \cos \theta+r
$$

于是问题转化为求代数式

$$
\frac{\cos \theta+1}{2 \cos \theta+\sin \theta}
$$

的最值.

记 $m=\frac{\cos \theta+1}{2 \cos \theta+\sin \theta}$, 则

$$
\cos \theta+1=2 m \cos \theta+m \sin \theta
$$

整理得

$$
\sqrt{m^{2}+(2 m-1)^{2}} \sin (\theta+\varphi)=1
$$

于是

$$
m^{2}+(2 m-1)^{2} \geqslant 1
$$

解得

$$
m \geqslant \frac{4}{5}
$$

容易检验得 $\frac{4}{5}$ 可以取到, 为最小值, 而不存在最大值.

## 第 805 题 柳暗花明

已知函数 $f(x)=\frac{a}{x}-x$, 对任意 $x \in(0,1)$, 有 $f(x) \cdot f(1-x) \geqslant 1$ 恒成立, 则实数 $a$ 的取值范围为 $\qquad$ .

解析 $\left(-\infty,-\frac{1}{4}\right] \cup[1,+\infty)$.

解法一 原不等式即

$$
\left(\frac{a}{x}-x\right)\left[\frac{a}{1-x}-(1-x)\right] \geqslant 1
$$

如果我们视 $x$ 为变量, $a$ 为参数, 那么就会陷人一个研究四次函数的困境.

但是如果我们视 $a$ 为主元, $x$ 为参数去解这个不等式,那么就柳暗花明了.上式也即

$$
a^{2}-\left[x^{2}+(1-x)^{2}\right] \cdot a+x^{2}(1-x)^{2}-x(1-x) \geqslant 0,
$$

视其为关于 $a$ 的二次式, 其判别式

$$
\Delta=\left[x^{2}+(1-x)^{2}\right]^{2}-4 x^{2}(1-x)^{2}+4 x(1-x)=1
$$

于是该不等式等价于

$$
a \leqslant \frac{x^{2}+(1-x)^{2}-1}{2} \text { 或 } a \geqslant \frac{x^{2}+(1-x)^{2}+1}{2} \text {. }
$$

当 $x$ 在 $(0,1)$ 内变化时, $a$ 的取值区间

$$
\left(-\infty, \frac{x^{2}+(1-x)^{2}-1}{2}\right] \cup\left[\frac{x^{2}+(1-x)^{2}+1}{2},+\infty\right)
$$

也在变化. $a$ 的取值需要“以不变应万变”, 因此所求 $a$ 的取值范围就是这无数个区间的交集.由于

$$
\frac{1}{2} \leqslant x^{2}+(1-x)^{2}<1
$$

于是欲求的交集即 $\left(-\infty,-\frac{1}{4}\right] \cup[1,+\infty)$, 此即 $a$ 的取值范围.

解法二 通过换元法, 将四次问题转化为二次问题, 这也是处理高次问题的一个常见思路.不等式即

$$
\left(\frac{a}{x}-x\right)\left[\frac{a}{1-x}-(1-x)\right] \geqslant 1
$$

因为 $x \in(0,1)$, 所以上式可以变形为

$$
[x(1-x)]^{2}+(2 a-1) x(1-x)+a(a-1) \geqslant 0 .
$$

令 $t=x(1-x)$, 于是有 $-a \geqslant \frac{1}{4}$ 或 $-a+1 \leqslant 0$, 解得 $a \leqslant-\frac{1}{4}$ 或 $a \geqslant 1$.

解法三 记 $y=1-x \in(0,1)$, 则

$$
\begin{aligned}
f(x) \cdot f(1-x) & =f(x) f(y) \\
& =\left(\frac{a}{x}-x\right)\left(\frac{a}{y}-y\right) \\
& =\frac{x^{2} y^{2}-a\left(x^{2}+y^{2}\right)+a^{2}}{x y} \\
& =\frac{(x y)^{2}-a\left[(x+y)^{2}-2 x y\right]+a^{2}}{x y}
\end{aligned}
$$

令 $x y=t$, 则 $t \in\left(0, \frac{1}{4}\right]$, 令

$$
g(t)=f(x) \cdot f(1-x)=\frac{t^{2}-a(1-2 t)+a^{2}}{t} \geqslant 1
$$

即

$$
t^{2}+(2 a-1) t+a^{2}-a \geqslant 0
$$

情形一 若 $\frac{1}{2}-a \leqslant 0$, 即 $\frac{1}{2} \leqslant a$, 只需 $g(0) \geqslant 0$, 即

$$
a^{2}-a \geqslant 0
$$

解得 $a \geqslant 1$.

情形二 $\quad$ 若 $0<\frac{1}{2}-a \leqslant \frac{1}{4}$, 即 $\frac{1}{4} \leqslant a<\frac{1}{2}$, 只需

$$
g\left(\frac{1}{2}-a\right) \geqslant a
$$

无解.

情形三 若 $\frac{1}{2}-a>\frac{1}{4}$, 即 $a<\frac{1}{4}$, 只需 $g\left(\frac{1}{4}\right) \geqslant 0$, 即

$$
\left(a-\frac{1}{4}\right)^{2} \geqslant \frac{1}{4}
$$

解得 $a \leqslant-\frac{1}{4}$.

因此实数 $a$ 的取值范围为 $\left(-\infty,-\frac{1}{4}\right] \cup[1,+\infty)$.

## 第 806 题 代数式的取值范围

若实数 $x, y$ 满足 $x \geqslant-1, y \geqslant-1$, 且 $2^{x}+2^{y}=4^{x}+4^{y}$, 求 $2^{2 x-y}+2^{2 y-x}$ 的取值范围.

解析 解法一 设 $2^{x}=a, 2^{y}=b$, 则 $a, b \geqslant \frac{1}{2}$, 且

$$
a^{2}+b^{2}=a+b
$$

记所求代数式为 $M$,则

$$
M=\frac{b^{2}}{a}+\frac{a^{2}}{b}
$$

考虑对 $M$ 进行代数变形, 将 $M$ 化成齐次式有

$$
M=\frac{a^{3}+b^{3}}{a b} \cdot \frac{a+b}{a^{2}+b^{2}}
$$

令 $t=\frac{a}{b}$, 有

$$
M=\frac{\left(t^{3}+1\right)(t+1)}{t\left(t^{2}+1\right)}=\frac{(t+1)^{2}}{t} \cdot \frac{t^{2}-t+1}{t^{2}+1}=\left(t+\frac{1}{t}+2\right) \cdot\left(1-\frac{1}{t+\frac{1}{t}}\right)
$$

令 $s=t+\frac{1}{t}$, 于是得

$$
M=(s+2)\left(1-\frac{1}{s}\right)=1+s-\frac{2}{s}
$$

(1)式的限制条件为

$$
\left(a-\frac{1}{2}\right)^{2}+\left(b-\frac{1}{2}\right)^{2}=\frac{1}{2}
$$

于是点 $(a, b)$ 的轨迹为一个 $\frac{1}{4}$ 圆弧 (包括端点), 如图,

从而有 $\frac{a}{b} \in[\sqrt{2}-1, \sqrt{2}+1], s \in[2,2 \sqrt{2}]$.

代人(2)式得 $M$ 的范围是

$$
\left[2,1+\frac{3 \sqrt{2}}{2}\right]
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-233.jpg?height=251&width=223&top_left_y=713&top_left_x=1636)

解法二 设 $2^{x}=a, 2^{y}=b$, 则 $a, b \geqslant \frac{1}{2}$, 且

$$
a^{2}+b^{2}=a+b
$$

记所求代数式为 $M$,则

$$
M=\frac{b^{2}}{a}+\frac{a^{2}}{b}
$$

由(1)式知可以令

$$
\left\{\begin{array}{l}
a=\frac{1}{2}+\frac{\sqrt{2}}{2} \cos \theta, \\
b=\frac{1}{2}+\frac{\sqrt{2}}{2} \sin \theta
\end{array} \quad \theta \in\left[0, \frac{\pi}{2}\right]\right.
$$

代人 $M$ 中化简得

$$
M=\frac{[2+\sqrt{2}(\sin \theta+\cos \theta)] \cdot[3+\sqrt{2}(\sin \theta+\cos \theta)-2 \sin \theta \cos \theta]}{2[1+\sqrt{2}(\sin \theta+\cos \theta)+2 \sin \theta \cos \theta]}
$$

令 $t=\sin \theta+\cos \theta$, 则 $t=\sqrt{2} \sin \left(\theta+\frac{\pi}{4}\right) \in[1, \sqrt{2}]$, 且 $2 \sin \theta \cos \theta=t^{2}-1$.

代人(2)式得

$$
M=\frac{\sqrt{2}}{2}\left(\frac{4}{t}-t\right)+1 \in\left[2,1+\frac{3}{2} \sqrt{2}\right]
$$

其他解法 在本题中, 因为条件比较特殊, 也可以考虑对称性, 直接通过边界与对称点得到所求代数式的范围, 将 $M$ 进行变形

$$
M=\frac{a+b-b^{2}}{b}+\frac{a+b-a^{2}}{a}=\frac{a}{b}+\frac{b}{a}-(a+b)+2
$$

结合点 $(a, b)$ 在圆弧上容易得到

$$
\frac{a}{b}+\frac{b}{a} \in[2,2 \sqrt{2}], a+b \in\left[1+\frac{\sqrt{2}}{2}, 2\right]
$$

从而

$$
M \in\left[2,1+\frac{3}{2} \sqrt{2}\right]
$$

且边界恰好可以取到, 于是得到 $M$ 的取值范围. 但这种方法没有一般性, 条件稍作改变就无法奏效.

## 第 807 题 齐次化

已知正实数 $x, y$ 满足 $x^{3}+2 y^{3}=x-y$, 求使 $x^{2}+k y^{2} \leqslant 1$ 恒成立的 $k$ 的最大值.

解析 根据题意, 有

$$
x-y=x^{3}+2 y^{3}>0,
$$

于是

$$
\left(x^{2}+k y^{2}\right)(x-y) \leqslant x^{3}+2 y^{3},
$$

即

$$
-x^{2} y+k x y^{2}-k y^{3} \leqslant 2 y^{3},
$$

也即

$$
k \leqslant \frac{t^{2}+2}{t-1}
$$

其中 $t=\frac{x}{y}, t>1$. 而

$$
\frac{t^{2}+2}{t-1}=t-1+\frac{3}{t-1}+2 \geqslant 2+2 \sqrt{3}
$$

等号当 $t=1+\sqrt{3}$ 时取得. 因此所求 $k$ 的最大值为 $2+2 \sqrt{3}$.

## 第 808 题 代数变形

已知实数 $x, y$ 满足

$$
\left(\sqrt{x^{2}+2015}-y\right) \cdot\left(\sqrt{y^{2}+2015}-x\right)=2015
$$

求 $x+y$ 的值.

解析 解法一 根据已知, 有

$$
\sqrt{x^{2}+2015}-y=\frac{2015\left(\sqrt{y^{2}+2015}+x\right)}{y^{2}-x^{2}+2015}
$$

整理得

$$
\left(x^{2}-y^{2}\right)\left(y-\sqrt{x^{2}+2015}\right)+\frac{2015\left(x^{2}-y^{2}\right)}{\sqrt{x^{2}+2015}+\sqrt{y^{2}+2015}}-2015(x+y)=0,
$$

于是有 $x+y=0$, 或

$$
(x-y)\left(y-\sqrt{x^{2}+2015}\right)+\frac{2015(x-y)}{\sqrt{x^{2}+2015}+\sqrt{y^{2}+2015}}-2015=0
$$

类似的,考虑到 $x, y$ 的对称性,若 $x+y \neq 0$, 则必然亦有

$$
(y-x)\left(x-\sqrt{y^{2}+2015}\right)+\frac{2015(y-x)}{\sqrt{y^{2}+2015}+\sqrt{x^{2}+2015}}-2015=0,
$$

两式相加有

$$
(x-y)\left(y-x+\sqrt{y^{2}+2015}-\sqrt{x^{2}+2015}\right)-4030=0,
$$

即

## 高考数学满分学霸的解题笔记。

$$
-(x-y)^{2}\left(1+\frac{x+y}{\sqrt{x^{2}+2015}+\sqrt{y^{2}+2015}}\right)=4030,
$$

事实上, 有

$$
x+y \geqslant-\sqrt{x^{2}+2015}-\sqrt{y^{2}+2015}
$$

因此

$$
-(x-y)^{2}\left(1+\frac{x+y}{\sqrt{x^{2}+2015}+\sqrt{y^{2}+2015}}\right) \leqslant 0
$$

矛盾.

经验证, 当 $x+y=0$ 时原式成立, 因此 $x+y$ 的值为 0 .

## 思考与总结

此题是由 2009 年的一道初中竞赛题改编而来, 原题如下.

已知实数 $x, y$ 满足

$$
\left(\sqrt{x^{2}+2009}-x\right) \cdot\left(\sqrt{y^{2}+2009}-y\right)=2009
$$

求 $x+y$ 的值.

略解如下:

根据已知, 有

$$
\sqrt{x^{2}+2009}-x=\frac{2009}{\sqrt{y^{2}+2009}-y}=\sqrt{y^{2}+2009}+y
$$

于是有

$$
x+y=\frac{x^{2}-y^{2}}{\sqrt{x^{2}+2009}+\sqrt{y^{2}+2009}}
$$

于是 $x+y=0$,或

$$
x-y=\sqrt{x^{2}+2009}+\sqrt{y^{2}+2009} .
$$

考虑到 $x, y$ 的对称性,若 $x+y \neq 0$ 则必然亦有

$$
y-x=\sqrt{y^{2}+2009}+\sqrt{x^{2}+2009},
$$

两式相加得

$$
0=2 \sqrt{x^{2}+2009}+2 \sqrt{y^{2}+2009},
$$

矛盾.

经验证, 当 $x+y=0$ 时原式成立, 因此 $x+y$ 的值为 0 .

解法二 先证明

$$
\sqrt{x^{2}+2015}-y>0, \sqrt{y^{2}+2015}-x>0,
$$

具体过程从略.

再证明 $x+y=0$. 用反证法, 若不然, 当 $x+y>0$ 时, 不妨设 $x \geqslant y$, 则有

$$
x>0, x \geqslant y>-x
$$

于是 $y^{2} \leqslant x^{2}$, 有

$$
\sqrt{y^{2}+2015}-x \leqslant \sqrt{x^{2}+2015}-x
$$

而另一方面，

$$
\sqrt{x^{2}+2015}-y<\sqrt{x^{2}+2015}+x
$$

于是

$$
\text { 左边 }<\left(\sqrt{x^{2}+2015}+x\right) \cdot\left(\sqrt{x^{2}+2015}-x\right)=2015 \text {, }
$$

矛盾.

当 $x+y<0$ 时,同理可证.

经验证,当 $x+y=0$ 时原式成立,因此 $x+y$ 的值为 0 .

## 第 809 题 求通项公式

已知数列 $\left\{a_{n}\right\}$ 满足 $\frac{a_{n+1}+a_{n}-1}{a_{n+1}-a_{n}+1}=n$, 其中 $n \in \mathbf{N}^{*}$, 且 $a_{2}=6$, 求 $\left\{a_{n}\right\}$ 的通项公式.

解析 解法一 根据已知, 不难推得

$$
a_{n+1}=\frac{n+1}{n-1} a_{n}-\frac{n+1}{n-1}, n=2,3, \cdots
$$

且 $a_{1}=1$. 对于 $a_{n}=f(n) \cdot a_{n-1}+g(n)$ 类型的递推公式, 可以迭代得到通项

$$
a_{n}=\left[\prod_{k=2}^{n} f(k)\right] a_{1}+\left[\prod_{k=3}^{n} f(k)\right] g(2)+\cdots+f(n) g(n-1)+g(n)
$$

当 $n \geqslant 2, n \in \mathbf{N}^{*}$ 时, 由原式得

$$
\begin{aligned}
a_{n} & =\frac{n}{n-2} \cdot a_{n-1}-\frac{n}{n-2} \\
& =\frac{n}{n-2} \cdot \frac{n-1}{n-3} \cdot a_{n-2}-\frac{n}{n-2} \cdot \frac{n-1}{n-3}-\frac{n}{n-2} \\
& \cdots \\
& =\frac{n}{n-2} \cdot \frac{n-1}{n-3} \cdots \frac{3}{1} \cdot a_{2}-\frac{n}{n-2} \cdot \frac{n-1}{n-3} \cdots \frac{3}{1}-\cdots-\frac{n}{n-2} \cdot \frac{n-1}{n-3}-\frac{n}{n-2} \\
& =\frac{n \cdot(n-1)}{2 \cdot 1} \cdot 6-\frac{n \cdot(n-1)}{2 \cdot 1}-\cdots-\frac{n \cdot(n-1)}{(n-2) \cdot(n-3)}-\frac{n}{n-2} \\
& =3 n(n-1)-n(n-1) \cdot\left[\frac{1}{1 \cdot 2}+\cdots+\frac{1}{(n-3) \cdot(n-2)}\right]-\frac{n}{n-2} \\
& =3 n(n-1)-n(n-1) \cdot\left(1-\frac{1}{n-2}\right)-\frac{n}{n-2} \\
& =2 n^{2}-n,
\end{aligned}
$$

又 $a_{1}=1$ 符合该式,所以 $a_{n}=n(2 n-1), n \in \mathbf{N}^{*}$.

解法二 根据已知, 不难推得

$$
a_{n+1}=\frac{n+1}{n-1} a_{n}-\frac{n+1}{n-1}, n=2,3, \cdots
$$

且 $a_{1}=1$. 原式整理可得

$$
(n-1) a_{n+1}=(n+1) a_{n}-(n+1),
$$

可以设法将右侧多出来的 $n+1$ 进行裂项:

$$
(n-1) \cdot\left[a_{n+1}+k(n+1)+b\right]=(n+1) \cdot\left(a_{n}+k n+b\right),
$$

即

$$
(n-1) a_{n+1}=(n+1) a_{n}+k n+2 b+k,
$$

比较系数, 可得 $k=-1, b=0$. 因此

$$
\frac{a_{n+1}-(n+1)}{a_{n}-n}=\frac{n+1}{n-1}, n \geqslant 2
$$

利用累乘法求得 $a_{n}=n(2 n-1)$. 再验证 $a_{1}$ 即可.

解法三 根据已知, 不难推得
高考数学满分学霸的解题笔记(一千零一题)

$$
a_{n+1}=\frac{n+1}{n-1} a_{n}-\frac{n+1}{n-1}, n=2,3, \cdots
$$

且 $a_{1}=1$. 对于 $a_{n}=f(n) \cdot a_{n-1}+g(n)$ 类型的递推公式, 也可以运用与裂项法类似的设法拆项, 设

$$
f(n)=\frac{h(n)}{h(n-1)}
$$

此时递推公式可以改写为

$$
\frac{a_{n}}{h(n)}=\frac{a_{n-1}}{h(n-1)}+\frac{g(n)}{h(n)}
$$

即可构造辅助数列.

注意到

$$
\frac{n+1}{n-1}=\frac{(n+1) \cdot n}{n \cdot(n-1)}
$$

于是可得

$$
\frac{a_{n+1}}{n(n+1)}=\frac{a_{n}}{(n-1) n}-\frac{1}{(n-1) n}
$$

设 $b_{n}=\frac{a_{n}}{(n-1) \cdot n}, n \geqslant 2$, 则

$$
b_{n+1}=b_{n}-\frac{1}{(n-1) \cdot n}
$$

于是累加可得

$$
b_{n}=\frac{2 n-1}{n-1}, n=2,3, \cdots
$$

从而

$$
a_{n}=n(2 n-1), n=2,3, \cdots
$$

又 $a_{1}=1$ 符合该式, 所以 $a_{n}=n(2 n-1), n \in \mathbf{N}^{*}$.

## 第 810 题 见微知著

已知数列 $\left\{a_{n}\right\}$ 满足 $a_{n}=\frac{5 a_{n-1}-2}{a_{n-1}-5}, n \in \mathbf{N}^{*}, n \geqslant 2$, 且 $a_{1}+a_{2}+\cdots+a_{2000}=50$, 则 $a_{1}+a_{20}=$

解析 $\frac{1}{20}$.

利用不动点法直接求数列的通项太复杂, 我们不妨先写几项来寻找数列的规律. 令 $a_{1}=a$, 则

$$
a_{2}=\frac{5 a-2}{a-5}, a_{3}=\frac{5 \cdot \frac{5 a-2}{a-5}-2}{\frac{5 a-2}{a-5}-5}=a=a_{1}
$$

于是

$$
\begin{aligned}
& a_{2}=a_{4}=a_{6}=\cdots \\
& a_{1}=a_{3}=a_{5}=\cdots
\end{aligned}
$$

从而

$$
a_{1}+a_{20}=a_{1}+a_{2}=\frac{50}{1000}=\frac{1}{20} .
$$

事实上,在本题中,由递推公式可以得到

$$
a_{n} a_{n-1}-5\left(a_{n}+a_{n-1}\right)+2=0
$$

在这个式子中, $a_{n}$ 与 $a_{n-1}$ 是对称的,也就是说已知 $a_{n-1}$ 求得 $a_{n}$ 后再去求 $a_{n+1}$ 的结果必然是 $a_{n-1}$, 即 $a_{n+1}=a_{n-1}$, 从而得到数列的周期为 2 .

## 第 811 题 糖水不等式

求证: $\left(1-\frac{1}{2}\right)\left(1-\frac{1}{4}\right)\left(1-\frac{1}{6}\right) \cdots\left(1-\frac{1}{2 n}\right)<\sqrt{\frac{1}{2 n+1}}$.

解析 记不等式左边为 $I_{n}$, 有

$$
I_{n}=\frac{1}{2} \cdot \frac{3}{4} \cdot \frac{5}{6} \cdots \frac{2 n-1}{2 n}
$$

由糖水不等式知

$$
\frac{k}{k+1}<\frac{k+1}{k+2}, k=1,2, \cdots, 2 n-1
$$

于是有

$$
I_{n}<\frac{2}{3} \cdot \frac{4}{5} \cdot \frac{6}{7} \cdots \frac{2 n}{2 n+1}
$$

上式两边同乘 $I_{n}$ 得

$$
I_{n}^{2}<\left(\frac{1}{2} \cdot \frac{3}{4} \cdot \frac{5}{6} \cdots \frac{2 n-1}{2 n}\right) \cdot\left(\frac{2}{3} \cdot \frac{4}{5} \cdot \frac{6}{7} \cdots \frac{2 n}{2 n+1}\right)=\frac{1}{2 n+1}
$$

不等式得证.

## 第 812 题 神来之“函”

定义新运算 $m * n=\frac{m n+1}{m+n}$, 则 $(\cdots((100 * 99) * 98) * \cdots * 3) * 2$ 的值是

解析 $\frac{5051}{5049}$.

注意运算形式,有

$$
m * n+1=\frac{(m+1)(n+1)}{m+n}, m * n-1=\frac{(m-1)(n-1)}{m+n},
$$

于是

$$
\frac{m * n+1}{m * n-1}=\frac{m+1}{m-1} \cdot \frac{n+1}{n-1}
$$

这就意味着若设 $f(x)=\frac{x+1}{x-1}$, 则有

$$
f(m * n)=f(m) \cdot f(n)
$$

令所求式为 $A$, 则

$$
f(A)=f(100) \cdot f(99) \cdots f(2)=\frac{101!}{99!\cdot 2!}=5050
$$

于是可解得 $A=\frac{5051}{5049}$.

## 第 813 题 三角换元

解方程 $x^{3}-3 x=\sqrt{x+2}$.

解析 分别画出 $y=x^{3}-3 x$ 与 $y=\sqrt{x+2}$ 的图象, 如图,注意到

$$
4 \cdot\left(\frac{x}{2}\right)^{3}-3 \cdot \frac{x}{2}=\sqrt{\frac{\frac{x}{2}+1}{2}}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-239.jpg?height=304&width=363&top_left_y=745&top_left_x=1503)

联想余弦的三倍角和半角公式, 令 $\frac{x}{2}=\cos \theta, \theta \in[0, \pi]$, 则

$$
4 \cos ^{3} \theta-3 \cos \theta=\sqrt{\frac{1+\cos \theta}{2}}
$$

即

$$
\cos 3 \theta=\cos \frac{\theta}{2}
$$

解得

$$
3 \theta=\frac{\theta}{2} \text { 或 } 3 \theta=2 \pi-\frac{\theta}{2} \text { 或 } 3 \theta=2 \pi+\frac{\theta}{2},
$$

即

$$
\theta=0 \text {,或 } \frac{4 \pi}{7}, \text { 或 } \frac{4 \pi}{5},
$$

于是

$$
x=2 \text {, 或 } 2 \cos \frac{4 \pi}{7} \text {, 或 } 2 \cos \frac{4 \pi}{5} \text {. }
$$

## 第 814 题 三角恒等式

已知 $x, y \geqslant 0$, 且 $(1+x)(1+y)=2$, 求证: $\sqrt{1+x^{2}} \cdot \sqrt{1+y^{2}} \geqslant 4-2 \sqrt{2}$.

解析 解法一 条件即

$$
x+y+x y=1
$$

联想到三角恒等式

$$
\tan \frac{A}{2} \tan \frac{B}{2}+\tan \frac{B}{2} \tan \frac{C}{2}+\tan \frac{C}{2} \tan \frac{A}{2}=1
$$

其中角 $A, B, C$ 为 $\triangle A B C$ 的三个内角.

因此可以取 $\angle C=\frac{\pi}{2}, x=\tan \frac{A}{2}, y=\tan \frac{B}{2}$, 且 $\angle A+\angle B=\frac{\pi}{2}$, 于是

$$
\text { 左边 }=\frac{1}{\cos \frac{A}{2} \cdot \cos \frac{B}{2}}=\frac{2}{\cos \frac{A+B}{2}+\cos \frac{A-B}{2}} \geqslant \frac{2}{\cos \frac{\pi}{4}+1}=4-2 \sqrt{2} \text {, }
$$

因此原命题得证.

思考与总结

三角代换是处理形如 $a b+b c+c a=1$ 且 $a, b, c>0$ 的代数条件的重要方法.

解法二 令 $s=1+x, t=1+y$, 则有

$$
s>1, t>1, s t=2
$$

将 $x=s-1, y=t-1$ 代人所证不等式左边有

$$
\text { 左边 }=\sqrt{1+(s-1)^{2}} \cdot \sqrt{1+(t-1)^{2}}=\sqrt{2(s+t-2)^{2}} \geqslant \sqrt{2} \cdot(2 \sqrt{2}-2)=4-2 \sqrt{2} \text {. }
$$

当且仅当 $s=t=\sqrt{2}$, 即 $x=y=\sqrt{2}-1$ 时取到等号.

解法三 由题目条件得到

$$
y=\frac{1-x}{1+x}
$$

于是

$$
1+y^{2}=1+\left(\frac{1-x}{1+x}\right)^{2}=\frac{2\left(1+x^{2}\right)}{(1+x)^{2}}
$$

代人所证不等式左边得到

$$
\text { 左边 }=\frac{\sqrt{2} \cdot\left(1+x^{2}\right)}{1+x}=\sqrt{2}\left(1+x+\frac{2}{1+x}-2\right) \geqslant \sqrt{2}(2 \sqrt{2}-2) \text {. }
$$

当且仅当 $x=\sqrt{2}-1$ 时取到等号.

## 第 815 题 代数式的最值

已知 $a, b, c$ 为直角三角形的三边长, 则 $\frac{a^{3}+b^{3}+c^{3}}{a b c}$ 的最小值是

解析 $2+\sqrt{2}$.

不妨设 $c$ 为斜边, 即 $a^{2}+b^{2}=c^{2}$, 其中 $a, b, c>0$.

令 $a=c \cos \theta, b=c \sin \theta$, 则

$$
\begin{aligned}
\frac{a^{3}+b^{3}+c^{3}}{a b c} & =\frac{\sin ^{3} \theta+\cos ^{3} \theta+1}{\sin \theta \cdot \cos \theta} \\
& =\frac{(\sin \theta+\cos \theta)\left(\sin ^{2} \theta-\sin \theta \cdot \cos \theta+\cos ^{2} \theta\right)+1}{\sin \theta \cdot \cos \theta}
\end{aligned}
$$

令 $x=\sin \theta+\cos \theta, x \in(1, \sqrt{2}]$, 则 $\sin \theta \cdot \cos \theta=\frac{x^{2}-1}{2}$, 且

$$
\frac{a^{3}+b^{3}+c^{3}}{a b c}=\frac{-x^{2}+x+2}{x-1}=-x+\frac{2}{x-1}
$$

右侧函数显然单调递减, 因此原式的最小值为 $2+\sqrt{2}$.

## 第 816 题 - 般三次方程的解法

解关于 $x$ 的方程 $x^{3}+p x+q=0$.

解析 解决问题的关键是关于 $t+\frac{1}{t}$ 的恒等式

$$
\left(t+\frac{1}{t}\right)^{3}=t^{3}+\frac{1}{t^{3}}+3\left(t+\frac{1}{t}\right)
$$

简单的情形 如果 $p=-3$,那么我们可以换元 $x=t+\frac{1}{t}$, 将方程转化为

$$
t^{3}+\frac{1}{t^{3}}+q=0
$$

即

$$
\left(t^{3}\right)^{2}+q \cdot t^{3}+1=0
$$

进而利用二次方程的求根公式求得 $t^{3}$, 再求出 $t$ 后代回 $x=t+\frac{1}{t}$, 求根过程就完成了.

进一步的处理 现在面临的困难是如何处理 $p$, 解决的方法是对换元进行一个小小的改造. 由于

$$
\left(t+\frac{u}{t}\right)^{3}=t^{3}+\frac{u^{3}}{t^{3}}+3 u\left(t+\frac{u}{t}\right)
$$

因此令 $x=t+\frac{u}{t}$, 其中 $u$ 为待定系数, 那么原方程变为

$$
t^{3}+\frac{u^{3}}{t^{3}}+(3 u+p) \cdot\left(t+\frac{u}{t}\right)+q=0
$$

在这个方程中, 令 $u=-\frac{p}{3}$, 就会和之前一样变成一个关于 $t^{3}$ 的二次方程

$$
\left(t^{3}\right)^{2}+q \cdot t^{3}-\frac{p^{3}}{27}=0
$$

接下来的步骤与之前的相同.

事实上,任意三次方程 $x^{3}+a x^{2}+b x+c=0$ 都可以通过换元 $t=x+\frac{a}{3}$ 的方式转化为解方程 $x^{3}+p x+q$ $=0$, 因此掌握了这个方程的解法, 就等于掌握了一般三次方程的解法. 在一般三次方程的解法中, 我们用到的换元 $x=t+\frac{u}{t}$ 同样也是解高次方程的重要方法.

## 第 817 题 15 换元,妙化简

若正实数 $x, y$ 满足 $(2 x y-1)^{2}=(5 y+2)(y-2)$, 则 $x+\frac{1}{2 y}$ 的最大值为

解析 $\frac{3 \sqrt{2}}{2}-1$.
解法一 先进行常规的转化, 根据已知条件, 有

$$
\left(2 x-\frac{1}{y}\right)^{2}=\left(5+\frac{2}{y}\right)\left(1-\frac{2}{y}\right)
$$

此时可以考虑换元, 令 $2 x=m, \frac{1}{y}=n$, 则问题转化为求 $\frac{m+n}{2}$ 的最大值, 而条件转化为

$$
(m-n)^{2}=(5+2 n)(1-2 n),
$$

即

$$
m^{2}+5 n^{2}-2 m n+8 n-5=0
$$

接下来可以考虑判别式法, 但是估计运算量不小.

怎么办呢?

分析刚才换元中的不足之处, 有两点:

(1) 只是简单替换, 左右两边还是需要展开;

(2)右边有点像平方差公式, 没有利用好.

因此先利用换元 $\frac{2}{y}=n-2$ 处理右边, 此时

$$
\left(5+\frac{2}{y}\right)\left(1-\frac{2}{y}\right)=(3+n)(3-n)=9-n^{2} \text {, }
$$

而直接设 $2 x-\frac{1}{y}=m$ 处理左边, 此时问题转化为求

$$
\frac{1}{2}\left(2 x+\frac{1}{y}\right)=\frac{1}{2}(m+n-2)
$$

的最大值,条件转化为

$$
m^{2}+n^{2}=9 \text {, }
$$

其中 $m+\frac{1}{2} n-1>0$ 且 $n>2$.

此时

$$
\frac{1}{2}(m+n-2) \leqslant \sqrt{\frac{m^{2}+n^{2}}{2}}-1=\frac{3 \sqrt{2}}{2}-1
$$

等号当且仅当 $m=n=\frac{3}{\sqrt{2}}$ 时取得. 因此所求的最大值为 $\frac{3 \sqrt{2}}{2}-1$.

解法二 注意到

$$
x+\frac{1}{2 y}=\frac{2 x y+1}{2 y}
$$

于是结合已知条件得所求式子为

$$
\frac{ \pm \sqrt{(5 y+2)(y-2)}+2}{2 y}(y \geqslant 2)
$$

当 $2 x y-1 \leqslant 0$ 时, 有 $x \leqslant \frac{1}{2 y} \leqslant \frac{1}{4}$, 从而

$$
x+\frac{1}{2 y} \leqslant \frac{1}{4}+\frac{1}{4}=\frac{1}{2}
$$

当 $2 x y-1>0$ 时, 令

$$
t=\frac{\sqrt{(5 y+2)(y-2)}+2}{2 y}
$$

将 $y$ 看成自变量整理该式得

$$
\left(4 t^{2}-5\right) y^{2}+8(1-t) y+8=0
$$

这个关于 $y$ 的方程有解的必要条件是

$$
4 t^{2}-5=0
$$

或

$$
\left\{\begin{array}{l}
4 t^{2}-5 \neq 0 \\
\Delta=-32\left(2 t^{2}+4 t-7\right) \geqslant 0
\end{array}\right.
$$

解得

$$
t=\frac{\sqrt{5}}{2} \text { 或 } t \leqslant \frac{3 \sqrt{2}}{2}-1 \text {, }
$$

其中等号成立时 $y=8+6 \sqrt{2}$ 满足要求. 而

$$
\frac{1}{2}<\frac{\sqrt{5}}{2}<\frac{3 \sqrt{2}}{2}-1
$$

故所求代数式的最大值为 $\frac{3 \sqrt{2}}{2}-1$.

思考与总结

求最值的过程中用到了判别式法, 对于这种自变量有限制的情况用判别式法求值域需要特别慎重, 但对于求最值的问题, 可以借助于判别式法探索出必要条件, 再说明这个最值可以取到, 大家可以理解一下求值域与求最值的区别.

## 第 818 题 换元的妙用

已知实数 $a, b$ 满足 $a^{2} \geqslant 4 b$, 求 $(1-a)^{2}+(a-b)^{2}+(1-b)^{2}$ 的最小值.

解析 设 $a=x+y, b=x y$, 其中 $x, y \in \mathbf{R}$, 则

$$
\begin{aligned}
(1-a)^{2}+(a-b)^{2}+(1-b)^{2} & =2 a^{2}+2 b^{2}-2 a b-2 a-2 b+2 \\
& =2(x+y)^{2}+2 x^{2} y^{2}-2 x y(x+y)-2(x+y)-2 x y+2 \\
& =2\left(x^{2} y^{2}-x^{2} y-x y^{2}+x^{2}+y^{2}+x y-x-y+1\right) \\
& =2\left(x^{2}-x+1\right)\left(y^{2}-y+1\right) \\
& \geqslant 2 \cdot \frac{3}{4} \cdot \frac{3}{4}=\frac{9}{8}
\end{aligned}
$$

等号当且仅当 $x=y=\frac{1}{2}$, 即 $a=1, b=\frac{1}{4}$ 时取得.

思考与总结

利用换元处理掉题中难以直接应用的限制条件是解决问题的关键.

## 第 819 题 对称换元

已知 $a+b=6$, 则 $\left(a^{2}+4\right)\left(b^{2}+4\right)$ 的最小值是

解析 144 .

设 $a=3+x, b=3-x$, 则

$$
\begin{aligned}
\left(a^{2}+4\right)\left(b^{2}+4\right) & =\left(x^{2}+13+6 x\right)\left(x^{2}+13-6 x\right) \\
& =x^{4}+26 x^{2}+169-36 x^{2} \\
& =\left(x^{2}-5\right)^{2}+144,
\end{aligned}
$$

于是所求最小值为 144 , 当 $x= \pm \sqrt{5}$ 时取得.

## 第 820 题 三次方程的根

已知关于 $x$ 的方程 $x^{3}-3 x+4=0$ 的三个根分别为 $a, b, c$, 求 $(a-b)(b-c)(c-a)$ 的值.

解析 解法一 由于

$$
M=(a-b)(b-c)(c-a)=\sum a b^{2}-\sum a^{2} b
$$

于是

$$
\begin{aligned}
M^{2} & =\left(\sum a b^{2}\right)^{2}+\left(\sum a^{2} b\right)^{2}-2 \sum a b^{2} \cdot \sum a^{2} b \\
& =\sum\left(a^{4} b^{2}+a^{2} b^{4}\right)+2 \sum\left(a^{2} b^{3} c+a^{3} b^{2} c\right)-2 \sum a^{3} b^{3}-2 \sum a^{2} b^{2} c^{2}-2 \sum a^{4} b \\
& =p^{2} q^{2}-2 q^{3}+4 p q r-3 r^{2}-3 p^{3} r+2\left(p q r-3 r^{2}\right)-2\left[\left(q^{3}-3 p q r+3 r^{2}\right)+3 r^{2}+\left(p^{3} r-3 p q r+3 r^{2}\right)\right] \\
& =p^{2} q^{2}-4 q^{3}+18 p q r-27 r^{2}-4 p^{3} r
\end{aligned}
$$

其中

$$
\left\{\begin{array}{l}
p=a+b+c=0 \\
q=a b+b c+c a=-3 \\
r=a b c=-4
\end{array}\right.
$$

因此可得 $M= \pm 18 \mathrm{i}$.

解法二 根据韦达定理, 有

$$
\begin{gathered}
a+b=-c, a b=-\frac{4}{c}, \text { 于是 } \\
(b-c)(c-a)=(a+b) c-c^{2}-a b=-2 c^{2}+\frac{4}{c}=\frac{-2 c^{3}+4}{c}=-6+\frac{12}{c}=-12\left(\frac{1}{2}-\frac{1}{c}\right)
\end{gathered}
$$

而

$$
1-3 \cdot\left(\frac{1}{x}\right)^{2}+4 \cdot\left(\frac{1}{x}\right)^{3}=0
$$

因此

$$
4 t^{3}-3 t^{2}+1=4\left(t-\frac{1}{a}\right)\left(t-\frac{1}{b}\right)\left(t-\frac{1}{c}\right)
$$

令 $t=\frac{1}{2}$, 可得

$$
(a-b)^{2}(b-c)^{2}(c-a)^{2}=-12^{3} \cdot \frac{3}{16}=-324
$$

从而所求代数式的值为 $\pm 18 \mathrm{i}$.

解法三 根据题意

$$
x^{3}-3 x+4=(x-a)(x-b)(x-c)
$$

两边求导可得

$$
3 x^{2}-3=(x-a)(x-b)+(x-b)(x-c)+(x-c)(x-a)
$$

分别令 $x=a, b, c$, 将得到的式子相乘, 可得

$$
\left(3 a^{2}-3\right)\left(3 b^{2}-3\right)\left(3 c^{2}-3\right)=-(a-b)^{2}(b-c)^{2}(c-a)^{2}
$$

即

$$
27 \cdot(1-a)(1-b)(1-c) \cdot(-1-a)(-1-b)(-1-c)=-(a-b)^{2}(b-c)^{2}(c-a)^{2}
$$

因此

$$
\left.\left.27 \cdot\left(x^{3}-3 x+4\right)\right|_{x=1} \cdot\left(x^{3}-3 x+4\right)\right|_{x=-1}=-(a-b)^{2}(b-c)^{2}(c-a)^{2},
$$

从而可得所求代数式的值为 $\pm 18 \mathrm{i}$.

## 第 821 题 参差不齐

已知 $-6 \leqslant x_{i} \leqslant 10(i=1,2, \cdots, 10), \sum_{i=1}^{10} x_{i}=50$, 当 $\sum_{i=1}^{10} x_{i}^{2}$ 取得最大值时, 在 $x_{1}, x_{2}, \cdots, x_{10}$ 这 10 个数中等于 -6 的数共有
A. 1 个
B. 2 个
C. 3 个
D. 4 个

解析 $\mathrm{C}$.

解法一 当 $\sum_{i=1}^{10} x_{i}^{2}$ 取得最大值时, 在 $x_{i}$ 中存在两个数 $x_{i}, x_{j} \in(-6,10), x_{i} \leqslant x_{j}$, 则令 $x=\min \left\{10-x_{j}\right.$, $\left.x_{i}+6\right\}$, 则 $x>0$, 且 $x_{i}-x \geqslant-6, x_{j}+x \leqslant 10$, 且有

$$
\left(x_{i}-x\right)^{2}+\left(x_{j}+x\right)^{2}=x_{i}^{2}+x_{j}^{2}+2 x^{2}+2 x\left(x_{j}-x_{i}\right)>x_{i}^{2}+x_{j}^{2}
$$

矛盾, 所以 $x_{1}, x_{2}, \cdots, x_{10}$ 中至多只有一个数不等于 -6 或 10 .

假设其中有 $x$ 个 -6 ,则有 $9-x$ 个 10 ,剩下的一个数为

$$
50-(-6) x-10(9-x)=16 x-40 \in(-6,10)
$$

解得 $x=3$.

解法二 令 $y_{i}=x_{i}+6(i=1,2, \cdots, 10)$, 则

$$
0 \leqslant y_{i} \leqslant 16, \sum_{i=1}^{10} y_{i}=110
$$

于是

$$
\sum_{i=1}^{10} x_{i}^{2}=\sum_{i=1}^{10}\left(y_{i}-6\right)^{2}=\sum_{i=1}^{10} y_{i}^{2}-12 \sum_{i=1}^{10} y_{i}+360=\sum_{i=1}^{10} y_{i}^{2}-960
$$

若 $\sum_{i=1}^{10} x_{i}^{2}$ 取得最大值, 则 $\sum_{i=1}^{10} y_{i}^{2}$ 取得最大值, 不妨设 $y_{1} \geqslant y_{2} \geqslant y_{3} \geqslant \cdots \geqslant y_{10}$, 先用反证法证明 $y_{10}=0$;否则 $y_{10}>0$, 易知 $y_{9}<16:$

(1)若 $y_{9}+y_{10} \leqslant 16$, 则取 $z_{i}=y_{i}(i=1,2, \cdots, 8), z_{9}=y_{9}+y_{10}, z_{10}=0$, 则

$$
\sum_{i=1}^{10} z_{i}^{2}-\sum_{i=1}^{10} y_{i}^{2}=\left(y_{9}+y_{10}\right)^{2}-y_{9}^{2}-y_{10}^{2}=2 y_{9} y_{10}>0
$$

(2)若 $y_{9}+y_{10}>16$, 则取 $z_{i}=y_{i}(i=1,2, \cdots, 8), z_{9}=16, z_{10}=y_{9}+y_{10}-16$, 则

$$
\begin{aligned}
\sum_{i=1}^{10} z_{i}^{2}-\sum_{i=1}^{10} y_{i}^{2} & =16^{2}+\left(y_{9}+y_{10}-16\right)^{2}-y_{9}^{2}-y_{10}^{2} \\
& =\left(16+y_{9}\right)\left(16-y_{9}\right)+\left(y_{9}+2 y_{10}-16\right)\left(y_{9}-16\right) \\
& =2\left(16-y_{9}\right)\left(16-y_{10}\right) \\
& >0
\end{aligned}
$$

综合(1)(2)可知, 若 $\sum_{i=1}^{10} y_{i}^{2}$ 取得最大值, 则 $y_{10}=0$.

同理可推得 $y_{9}=0, y_{8}=0$, 而若 $y_{7}=0$, 则 $y_{1}+y_{2}+\cdots+y_{6}=110$, 而 $y_{1}+y_{2}+\cdots+y_{6} \leqslant 16 \times 6=96$, 矛盾,
所以 $y_{7}>0$.

令 $y_{1}=y_{2}=\cdots=y_{6}=16, y_{7}=14, y_{8}=y_{9}=y_{10}=0$, 满足题意, 所以 C 正确.

## 第 822 题常数变易

已知 $x^{2}+y^{2}=25$, 则 $\sqrt{8 y-6 x+50}+\sqrt{8 y+6 x+50}$ 的最大值为

解析 $6 \sqrt{10}$.

可以直接利用不等式

$$
\sqrt{8 y-6 x+50}+\sqrt{8 y+6 x+50} \leqslant \sqrt{2} \cdot \sqrt{16 y+100} \leqslant \sqrt{2} \cdot \sqrt{180}=6 \sqrt{10}
$$

等号当 $x=0, y=5$ 时取得. 从而可得所求代数式的最大值为 $6 \sqrt{10}$.

接下来给出一个几何解释.

将 $25=x^{2}+y^{2}$ 代人,有

$$
\sqrt{8 y-6 x+50}+\sqrt{8 y+6 x+50}=\sqrt{(x-3)^{2}+(y+4)^{2}}+\sqrt{(x+3)^{2}+(y+4)^{2}} .
$$

于是问题转化为圆 $x^{2}+y^{2}=25$ 上一点 $P$ 到点 $M(3,-4)$ 和 $N(-3,-4)$ 的距离之和 $P M+P N$ 的最大值.

猜想当 $P$ 点位于 $(0,5)$ 时取得最大值, 最大值为 $6 \sqrt{10}$, 证明如下.

以 $M, N$ 为焦点, $6 \sqrt{10}$ 为长轴长的椭圆方程为

$$
\frac{x^{2}}{90}+\frac{(y+4)^{2}}{81}=1
$$

因此若点 $(x, y)$ 在椭圆上, 就有

$$
x^{2}+y^{2}-25=90\left[1-\frac{(y+4)^{2}}{81}\right]+y^{2}-25=\frac{1}{9}(5-y)(85+y) \geqslant 0
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-246.jpg?height=314&width=306&top_left_y=1193&top_left_x=1443)

这就意味着除了点 $(0,5)$ 外, 圆 $x^{2}+y^{2}=25$ 上的其他点都在椭圆的内部, 于是 $P M+P N \leqslant 6 \sqrt{10}$.

综上所述,所求的最大值为 $6 \sqrt{10}$.

## 第 823 题 引入参数配方求最值

求函数 $f(x)=\sin x \cos x+\sin x+\frac{2}{5} \cos x(x \in \mathbf{R})$ 的值域.

解析 解法一 考虑引人参数使用拉格朗日配方法, 有

$$
\begin{aligned}
f(x) & =\lambda \sin ^{2} x+\sin x \cos x+\sin x+\lambda \cos ^{2} x+\frac{2}{5} \cos x-\lambda \\
& =\lambda\left(\sin x+\frac{\cos x+1}{2 \lambda}\right)^{2}+\frac{4 \lambda^{2}-1}{4 \lambda}\left(\cos x+\frac{4 \lambda-5}{20 \lambda^{2}-5}\right)^{2}-\frac{100 \lambda^{3}+4 \lambda-10}{100 \lambda^{2}-25}
\end{aligned}
$$

考虑到取等条件

$$
\cos x=\frac{5-4 \lambda}{20 \lambda^{2}-5}, \sin x=-\frac{\cos x+1}{2 \lambda}=\frac{2-10 \lambda}{20 \lambda^{2}-5}
$$

有

$$
\left(\frac{5-4 \lambda}{20 \lambda^{2}-5}\right)^{2}+\left(\frac{2-10 \lambda}{20 \lambda^{2}-5}\right)^{2}=1
$$

整理得

$$
100 \lambda^{4}-79 \lambda^{2}+20 \lambda-1=0
$$

解得

$$
\lambda=-1 \text { 或 } \frac{1}{5} \text { 或 } \frac{4-\sqrt{11}}{10} \text { 或 } \frac{4+\sqrt{11}}{10} .
$$

考虑到当两个完全平方式前的系数同号时配方才有意义, 有

$$
\lambda \cdot \frac{4 \lambda^{2}-1}{4 \lambda}>0
$$

即

$$
\lambda<-\frac{1}{2}
$$

或

$$
\lambda>\frac{1}{2}
$$

因此分别取

$$
\lambda=-1 \text { 或 } \lambda=\frac{4+\sqrt{11}}{10} \text {, }
$$

有

$$
\begin{aligned}
& \sin x \cos x+\sin x+\frac{2}{5} \cos x \\
= & -1\left(\sin x-\frac{1}{2} \cos x-\frac{1}{2}\right)^{2}-\frac{3}{4}\left(\cos x-\frac{3}{5}\right)^{2}+\frac{38}{25}
\end{aligned}
$$

以及

$$
\begin{aligned}
& \sin x \cos x+\sin x+\frac{2}{5} \cos x \\
= & \frac{4+\sqrt{11}}{10}[\sin x+(4-\sqrt{11}) \cos x+(4-\sqrt{11})]^{2}+\frac{-8+3 \sqrt{11}}{5}\left(\cos x+\frac{3-2 \sqrt{11}}{10}\right)^{2}-\frac{76+11 \sqrt{11}}{100}
\end{aligned}
$$

于是可得 $f(x)$ 的最大值和最小值分别为 $\frac{38}{25}$ 以及 $-\frac{76+11 \sqrt{11}}{100}$.

考虑到函数的连续性, 可得所求函数的值域为 $\left[-\frac{76+11 \sqrt{11}}{100}, \frac{38}{25}\right]$, 如图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-247.jpg?height=359&width=729&top_left_y=1783&top_left_x=673)

解法二 利用万能公式换元, 记 $y=f(x)$, 则

$$
y=\frac{2 t}{t^{2}+1} \cdot \frac{1-t^{2}}{1+t^{2}}+\frac{2 t}{1+t^{2}}+\frac{2}{5} \cdot \frac{1-t^{2}}{1+t^{2}}=-\frac{2}{5} \cdot \frac{t^{4}-10 t-1}{\left(t^{2}+1\right)^{2}}
$$

于是

$$
y^{\prime}=-\frac{4}{5} \cdot \frac{(2 t-1)\left(t^{2}+8 t+5\right)}{\left(t^{2}+1\right)^{3}}
$$

因此极值点为

$$
t=\frac{1}{2},-4 \pm \sqrt{11}
$$

进而可得极值依次为

$$
\frac{38}{25} \cdot \frac{-76 \mp 11 \sqrt{11}}{100}
$$

因此所求值域为 $\left[-\frac{76+11 \sqrt{11}}{100}, \frac{38}{25}\right]$.

## 第 824 题 三元不等式的齐次化

已知 $a, b, c, \in[0,1]$, 则 $\frac{a}{b c+1}+\frac{b}{c a+1}+\frac{c}{a b+1}$ 的取值范围是

解析 $[0,2]$.

由于 $a, b, c$ 轮换, 于是很有可能在边界或均值时取得最大值与最小值.

经过验证可得 $(a, b, c)=(0,0,0)$ 时, 原式取得可能的最小值为 0 ; 当 $(a, b, c)=(1,1,0)$ 时, 原式取得可能的最大值为 2 . 接下来我们尝试证明.

显然,原式为非负代数式,因此最小值为 0.

另一方面,根据已知有

$$
(1-a)(1-b) \geqslant 0
$$

于是

$$
a b+1 \geqslant a+b
$$

进而

$$
2(a b+1) \geqslant a+b+c
$$

因此

$$
\text { 左边 } \leqslant \sum_{c y c} \frac{2 a}{a+b+c}=2 \text {, }
$$

故原式最大值为 2.

## 第 825 题 守卫边疆

已知 $a, b, c, d$ 均为正实数, 求 $\frac{a}{a+b+c}+\frac{b}{b+c+d}+\frac{c}{c+d+a}+\frac{d}{d+a+b}$ 的取值范围.

解析 可以利用糖水不等式得到

$$
\sum_{c y c} \frac{a}{a+b+c}>\sum_{c c} \frac{a}{a+b+c+d}=1,
$$

同时

$$
\sum_{\text {cyc }} \frac{a}{a+b+c}<\sum_{c y c} \frac{d+a}{a+b+c+d}=2
$$

接下来的关键是确认 1,2 是题中代数式的下确界和上确界.

事实上, 当 $a, c, d \rightarrow 0$ 时, 原式趋于 1 ; 当 $a, b \rightarrow 0, c \rightarrow+\infty, d=1$ 时, 原式趋于 2 .

因此题中代数式的取值范围是 $(1,2)$.

## 第 826 题 拨云见日

已知实数 $x, y$ 满足 $x-3 \sqrt{x+1}=3 \sqrt{y+2}-y$, 求 $x+y$ 的最大值与最小值.

解析 令 $a=\sqrt{x+1}, b=\sqrt{y+2}$, 且 $a, b \geqslant 0$, 则 $x+y=a^{2}+b^{2}-3$, 且条件变为

$$
a^{2}-1-3 a=3 b-\left(b^{2}-2\right),
$$

即

$$
\left(a-\frac{3}{2}\right)^{2}+\left(b-\frac{3}{2}\right)^{2}=\frac{15}{2}
$$

它表示一段圆弧,如图.

显然圆弧上的点 $P$ 到原点的距离 $O P$ 的最大值为

$$
O D=O C+r=\frac{3 \sqrt{2}}{2}+\sqrt{\frac{15}{2}}=\frac{3 \sqrt{2}+\sqrt{30}}{2},
$$

其中 $r$ 为圆 $C$ 的半径. 而 $O P$ 的最小值为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-249.jpg?height=276&width=271&top_left_y=824&top_left_x=1592)

$$
O A=\frac{3+\sqrt{21}}{2}
$$

因此 $x+y$ 的最大值为 $9+3 \sqrt{15}$, 最小值为 $\frac{9+3 \sqrt{21}}{2}$.

## 第 827 题 构造新数列

实数 $a_{1}, a_{2}, \cdots, a_{2013}$ 满足 $a_{1}+a_{2}+\cdots+a_{2013}=0$, 且

$$
\left|a_{1}-2 a_{2}\right|=\left|a_{2}-2 a_{3}\right|=\cdots=\left|a_{2012}-2 a_{2013}\right|=\left|a_{2013}-2 a_{1}\right| .
$$

求证 $: a_{1}=a_{2}=\cdots=a_{2013}=0$.

解析 令 $b_{1}=a_{1}-2 a_{2}, b_{2}=a_{2}-2 a_{3}, \cdots, b_{2013}=a_{2013}-2 a_{1}$, 则

$$
\left|b_{1}\right|=\left|b_{2}\right|=\cdots=\left|b_{2013}\right|, b_{1}+b_{2}+\cdots+b_{2013}=0 .
$$

设 $\left|b_{1}\right|=\left|b_{2}\right|=\cdots=\left|b_{2013}\right|=m$, 则 $b_{1}, b_{2}, \cdots, b_{2013}$ 或者为 $m$ 或者为 $-m$,

设其中有 $x$ 个 $m, 2013-x$ 个 $-m$, 则

$$
b_{1}+b_{2}+\cdots+b_{2013}=m x+(-m)(2013-x)=m(2 x-2013)
$$

由于 $2 x-2013 \neq 0$, 因此 $m=0$.

于是

$$
b_{1}=b_{2}=\cdots=b_{2013}=0
$$

进而易得

$$
a_{1}=a_{2}=\cdots=a_{2013}=0
$$

## 第十一章 微积分初步

## 第 828 题 谁主沉浮

已知 $x>0$, 求证: $\left(\mathrm{e}^{x}-1\right) \cdot \ln (1+x)>x^{2}$.

解析 解法一 令 $f(x)=\frac{\ln (1+x)}{x}, x \in(0,+\infty)$, 因为

$$
f^{\prime}(x)=\frac{\frac{x}{x+1}-\ln (1+x)}{x^{2}}<0
$$

所以 $f(x)$ 在 $(0,+\infty)$ 上单调递减.

注意到同底数的指对函数之间互为反函数的关系, 我们有

$$
f\left(\mathrm{e}^{x}-1\right)=\frac{x}{\mathrm{e}^{x}-1}
$$

再注意到, 当 $x>0$ 时, $\mathrm{e}^{x}-1>x>\ln (1+x)>0$, 故有

$$
f(x)>f\left(\mathrm{e}^{x}-1\right)
$$

即

$$
\frac{\ln (1+x)}{x}>\frac{x}{\mathrm{e}^{x}-1}
$$

变形即得 $\left(\mathrm{e}^{x}-1\right) \cdot \ln (1+x)>x^{2}$.

解法二 如图.

取点 $A(x, 0)(x>0)$, 作直线 $l$ 与 $x$ 轴垂直, 分别交函数 $y$ $=\ln (1+x), y=x, y=\mathrm{e}^{x}-1$ 的图象于点 $B, C, D$,

设点 $E$ 与点 $D$ 关于直线 $y=x$ 对称, 则要证的结论等价于

$$
|A D| \cdot|A B|>|A C|^{2}
$$

由于函数 $y=\ln (1+x)$ 在其定义域 $(-1,+\infty)$ 上递增,故

$$
\frac{|A B|}{|A C|}=\frac{|A B|}{|A O|}=\tan \angle A O B>\tan \angle E O F=\frac{|E F|}{|O F|}=\frac{|A C|}{|A D|}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-250.jpg?height=592&width=666&top_left_y=1467&top_left_x=1089)

所以要证的结论成立.

解法三 易证, 当 $x>0$ 时,

$$
\mathrm{e}^{x}-1>x+\frac{x^{2}}{2}>0, \ln (1+x)>\frac{2 x}{x+2}>0
$$

所以

$$
\begin{aligned}
\left(\mathrm{e}^{x}-1\right) \cdot \ln (1+x) & >\left(x+\frac{x^{2}}{2}\right) \cdot \frac{2 x}{x+2} \\
& =\frac{x\left(x^{2}+2 x\right)}{x+2} \\
& =x^{2}
\end{aligned}
$$

放缩来自泰勒展开:

因为 $x \in(-\infty,+\infty)$ 时, 有

$$
\mathrm{e}^{x}=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots
$$

所以当 $x>0$ 时, 有

$$
\mathrm{e}^{x}-1>x+\frac{x^{2}}{2}>0
$$

因为 $x \in(-1,1)$ 时, 有

$$
\ln (1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots
$$

与

$$
\ln (1-x)=-x-\frac{x^{2}}{2}-\frac{x^{3}}{3}-\frac{x^{4}}{4}-\cdots
$$

同时成立,故 $x \in(-1,1)$ 时, 有

$$
\ln \frac{1+x}{1-x}=2\left(x+\frac{x^{3}}{3}+\frac{x^{5}}{5}+\cdots\right)
$$

所以若 $x \in(0,1)$, 则

$$
\ln \frac{1+x}{1-x}>2 x
$$

令 $t=\frac{1+x}{1-x}, x \in(0,1)$, 则 $x=\frac{t-1}{t+1}, t \in(1,+\infty)$,

此时有

$$
\ln t>\frac{2(t-1)}{t+1}
$$

所以当 $x>0$ 时,

$$
\ln (1+x)>\frac{2 x}{x+2}>0
$$

## 第 829 题 $f\left(x_{1}\right)=f\left(x_{2}\right)$ 的处理方法

已知函数 $f(x)=2 x-\frac{x^{2}}{\pi}+\cos x$. 设 $x_{1}, x_{2} \in(0, \pi), x_{1} \neq x_{2}$ 且 $f\left(x_{1}\right)=f\left(x_{2}\right)$. 若 $x_{1}, x_{0}, x_{2}$ 成等差数列, 则
A. $f^{\prime}\left(x_{0}\right)<0$
B. $f^{\prime}\left(x_{0}\right)=0$
C. $f^{\prime}\left(x_{0}\right)>0$
D. $f^{\prime}\left(x_{0}\right)$ 的符号不确定

७t A.

考虑到

$$
f^{\prime}\left(x_{0}\right)=f^{\prime}\left(\frac{x_{1}+x_{2}}{2}\right)=2-\frac{x_{1}+x_{2}}{\pi}-\sin \frac{x_{1}+x_{2}}{2},
$$

而根据题意有

$$
2 x_{1}-\frac{x_{1}^{2}}{\pi}+\cos x_{1}=2 x_{2}-\frac{x_{2}^{2}}{\pi}+\cos x_{2}
$$

于是

$$
2-\frac{x_{1}+x_{2}}{\pi}=-\frac{\cos x_{1}-\cos x_{2}}{x_{1}-x_{2}}=\frac{\sin \frac{x_{1}-x_{2}}{2}}{\frac{x_{1}-x_{2}}{2}} \cdot \sin \frac{x_{1}+x_{2}}{2}<\sin \frac{x_{1}+x_{2}}{2}
$$

因此可得 $f^{\prime}\left(x_{0}\right)<0$, 选 A. 最后附上该函数的图象.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-252.jpg?height=306&width=547&top_left_y=487&top_left_x=656)

在处理形如 $f\left(x_{1}\right)=f\left(x_{2}\right)$ 这样的等式时, 需要抓住 $x_{1}-x_{2}$ 这一关键要素进行代数变形 (尤其是因式分解).

## 第 830 题 不等式证明中的函数构造

证明下列不等式:

(1) 若 $\frac{1}{\mathrm{e}}<x<y<1$, 则 $\frac{y}{x}<\frac{1+\ln y}{1+\ln x}$;

(2) $\left(\frac{2}{1^{4}}+1\right)\left(\frac{2}{2^{4}}+1\right) \cdots\left(\frac{2}{n^{4}}+1\right)<\mathrm{e}^{4}$.

解析 (1) 由于 $\frac{y}{x}<\frac{1+\ln y}{1+\ln x}$ 等价于 $\frac{1+\ln x}{x}<\frac{1+\ln y}{y}$,

于是只需要证明函数 $f(x)=\frac{1+\ln x}{x}$ 在区间 $\left(\frac{1}{\mathrm{e}}, 1\right)$ 上单调递增.

因为函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{-\ln x}{x^{2}}
$$

于是函数 $f(x)$ 在 $(0,1)$ 上单调递增, 因此原命题得证.

(2) 等价于证明

$$
\ln \left(\frac{2}{1^{4}}+1\right)+\ln \left(\frac{2}{2^{4}}+1\right)+\cdots+\ln \left(\frac{2}{n^{4}}+1\right)<4
$$

而 $\ln (x+1)<x(x>0)$, 于是有

$$
\begin{aligned}
\text { 左边 } & <\frac{2}{1^{4}}+\frac{2}{2^{4}}+\frac{2}{3^{4}}+\frac{2}{4^{4}}+\cdots+\frac{2}{n^{4}} \\
& \leqslant 2+\frac{1}{8}+\frac{2}{1 \cdot 2 \cdot 3 \cdot 4}+\frac{2}{2 \cdot 3 \cdot 4 \cdot 5}+\cdots+\frac{2}{(n-2)(n-1) n(n+1)} \\
& =\frac{17}{8}+\frac{2}{3} \cdot\left[\frac{1}{1 \cdot 2 \cdot 3}-\frac{1}{(n-1) n(n+1)}\right] \\
& <\frac{17}{8}+\frac{1}{9}<4
\end{aligned}
$$

从而原命题得证.

因为不等式相当宽松, 也可以直接先将分母放缩成二次, 得到结果, 即

$$
\begin{aligned}
\text { 左边 } & <\frac{2}{1^{4}}+\frac{2}{2^{4}}+\frac{2}{3^{4}}+\frac{2}{4^{4}}+\cdots+\frac{2}{n^{4}} \\
& \leqslant \frac{2}{1^{2}}+\frac{2}{2^{2}}+\frac{2}{3^{2}}+\frac{2}{4^{2}}+\cdots+\frac{2}{n^{2}} \\
& <2\left(1+1-\frac{1}{2}+\frac{1}{2}-\frac{1}{3}+\cdots+\frac{1}{n-1}-\frac{1}{n}\right) \\
& =4-\frac{2}{n} \\
& <4
\end{aligned}
$$

## 第 831 题 顺藤摸瓜

已知函数 $f(x)=\ln (1+x)-\frac{x(1+\lambda x)}{1+x}$.

(1) 若 $x \geqslant 0$ 时, $f(x) \leqslant 0$, 求 $\lambda$ 的最小值;

(2) 设数列 $\left\{a_{n}\right\}$ 的通项是 $a_{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}$, 证明: $a_{2 n}-a_{n}+\frac{1}{4 n}>\ln 2$.

解析 解法一 (1) 对 $f(x)$ 求导得

$$
f^{\prime}(x)=\frac{x}{(1+x)^{2}}[-\lambda x+(1-2 \lambda)]
$$

又 $f(0)=0$, 所以 $\lambda$ 的讨论分界点为 $\lambda=0, \frac{1}{2}$.

情形一 $\lambda \leqslant 0$. 此时 $f^{\prime}(x)>0$, 于是 $f(x)$ 单调递增,

当 $x \geqslant 0$ 时有

$$
f(x)>f(0)=0,
$$

不符合题意.

情形二 $0<\lambda<\frac{1}{2}$. 此时在 $\left(0, \frac{1-2 \lambda}{\lambda}\right)$ 上, 有 $f^{\prime}(x)>0$, 于是在此区间上 $f(x)$ 单调递减,进而

$$
f(x)>f(0)=0,
$$

不符合题意.

情形三 $\lambda=\frac{1}{2}$. 此时当 $x \geqslant 0$ 时, 有

$$
f^{\prime}(x)=-\frac{x^{2}}{2(1+x)^{2}} \leqslant 0
$$

于是 $f(x)$ 单调递减, 因此

$$
f(x) \geqslant f(0)=0
$$

符合题意.

综上所述, $\lambda$ 的最小值为 $\frac{1}{2}$.

(2) 只需要证明

$$
\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}+\frac{1}{4 n}>\ln 2
$$

由第(1) 小题的结论, 当 $x \geqslant 0$ 时, 有

$$
\ln (1+x) \leqslant \frac{x\left(1+\frac{1}{2} x\right)}{1+x}
$$

令 $x=\frac{1}{k}$, 则有

$$
\begin{aligned}
\ln \frac{k+1}{k} & \leqslant \frac{\frac{1}{k}\left(1+\frac{1}{2 k}\right)}{1+\frac{1}{k}} \\
& =\frac{2 k+1}{2 k(k+1)} \\
& =\frac{1}{k+1}+\frac{1}{2 k(k+1)} \\
& =\frac{1}{k+1}+\frac{1}{2}\left(\frac{1}{k}-\frac{1}{k+1}\right)
\end{aligned}
$$

分别取 $k=n, n+1, n+2, \cdots, 2 n-1$ 累加得

$$
\ln \frac{n+1}{n}+\ln \frac{n+2}{n+1}+\cdots+\ln \frac{2 n}{2 n-1} \leqslant \frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}+\frac{1}{2}\left(\frac{1}{n}-\frac{1}{2 n}\right) .
$$

即

$$
\ln 2 \leqslant \frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}+\frac{1}{4 n}
$$

显然等号无法取得,所以原不等式得证.

解法二 (1) 同解法一.

(2) 只需要证明

$$
\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}+\frac{1}{4 n}>\ln 2
$$

也即

$$
\frac{1}{n}+\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}>\ln 2+\frac{3}{4 n}
$$

考虑函数 $g(x)=\frac{1}{x}$ 是单调递减的下凸函数, 于是利用积分放缩可得

$$
\begin{aligned}
\sum_{k=n}^{2 n} \frac{1}{k} & >\int_{n}^{2 n} g(x) \mathrm{d} x+\frac{g(n)+g(2 n)}{2} \\
& =\ln (2 n)-\ln n+\frac{\frac{1}{n}+\frac{1}{2 n}}{2} \\
& =\ln 2+\frac{3}{4 n}
\end{aligned}
$$

因此原命题得证.

## 第 832 题 切线放缩

求证: $\mathrm{e}^{x}-2 x \ln x-x>1$.
高考数学满分学霸的解题笔记

解析 题中不等式即

$$
\frac{\mathrm{e}^{x}-1}{x}>2 \ln x+1
$$

取左边函数在 $x=1$ 处的切线, 有

$$
\frac{\mathrm{e}^{x}-1}{x} \geqslant x+\mathrm{e}-2
$$

取右边函数在 $x=2$ 处的切线, 有

$$
2 \ln x+1 \leqslant x+2 \ln 2-1,
$$

因此

$$
\frac{\mathrm{e}^{x}-1}{x} \geqslant x+\mathrm{e}-2>x+2 \ln 2-1 \geqslant 2 \ln x+1,
$$

原不等式得证.

要证明 $\frac{\mathrm{e}^{x}-1}{x} \geqslant x+\mathrm{e}-2$, 只需要构造 $f(x)=\frac{\mathrm{e}^{x}-1}{x}-x$, 则

$$
f^{\prime}(x)=\frac{\left(\mathrm{e}^{x}-x-1\right)(x-1)}{x^{2}}
$$

从而知 $f(x)$ 在 $(0,1)$ 上单调递减, 在 $(1,+\infty)$ 上单调递增,

于是

$$
f(x) \geqslant f(1)=\mathrm{e}-2
$$

要证明 $2 \ln x+1 \leqslant x+2 \ln 2-1$, 只需要构造 $g(x)=2 \ln x+1-x$,则

$$
g^{\prime}(x)=\frac{2}{x}-1=\frac{2-x}{x}
$$

从而知

$$
g(x) \leqslant g(2)=2 \ln 2-1
$$

## 第 833 题 切线放缩

已知 $x_{1} \ln x_{1}=x_{2} \ln x_{2}=a\left(x_{1}<x_{2}\right), \mathrm{e}$ 是自然对数的底数. 求证: $x_{2}-x_{1}<2 a+1+\mathrm{e}^{-2}$.

解析 设函数 $f(x)=x \ln x$, 则其导函数

$$
f^{\prime}(x)=1+\ln x
$$

取其在 $x=\mathrm{e}^{-2}$ 和 $x=1$ 处的切线, 分别为 $l_{1}: y=-x-\mathrm{e}^{-2}$ 和 $l_{2}: y=x-1$, 如图 1.

直线 $y=a$ 与直线 $l_{1}$, 函数 $f(x)$ 的图象和直线 $l_{2}$ 分别交于 $x_{1}{ }^{\prime}, x_{1}, x_{2}, x_{2}{ }^{\prime}$, 则有

$$
x_{1}{ }^{\prime}<x_{1}<x_{2}<x_{2}{ }^{\prime},
$$

因此有

$$
x_{2}-x_{1}<x_{2}^{\prime}-x_{1}^{\prime}=(a+1)-\left(-a-\mathrm{e}^{-2}\right)=2 a+1+\mathrm{e}^{-2} .
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-255.jpg?height=246&width=355&top_left_y=2094&top_left_x=1506)

图 1

(1)类似的, 我们还可以用割线 $y=-x$ 和 $y=\frac{1}{\mathrm{e}-1}(x-1)$ 来估计 $x_{2}-x_{1}$ 的下界, 如图 2 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-256.jpg?height=233&width=306&top_left_y=359&top_left_x=568)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-256.jpg?height=235&width=290&top_left_y=355&top_left_x=940)

图 3

(2)我们也可以利用函数图象的外接曲线得到更加精确的界, 例如 $y=\frac{1}{2}(x-1)^{2}+x-1$ 和 $y=-\frac{2}{\mathrm{e}} \cdot$ $\sqrt{x}$, 如图 3.

## 第 834 题 切割线放缩

求证: $(x-1) \mathrm{e}^{x}-\ln x>-\frac{1}{2}$.

解析 解沄……情形一 $x \geqslant 1$ 。

此时利用切线放缩, 有

$$
\mathrm{e}^{x} \geqslant x+1
$$

于是

$$
\begin{aligned}
\text { 左边 } & \geqslant(x-1)(x+1)-\ln x \\
& >(x-1)(x+1)-(x-1) \\
& =x(x-1) \\
& >-\frac{1}{2} .
\end{aligned}
$$

情形二 $0<x<1$.

此时利用割线放缩, 有

$$
\mathrm{e}^{x}<(\mathrm{e}-1) x+1
$$

于是

$$
\begin{aligned}
\text { 左边 } & \geqslant(x-1)[(\mathrm{e}-1) x+1]-\ln x \\
& >(x-1)[(\mathrm{e}-1) x+1]-(x-1) \\
& =(\mathrm{e}-1) x(x-1) \\
& \geqslant-\frac{\mathrm{e}-1}{4} \\
& >-\frac{1}{2} .
\end{aligned}
$$

综上所述,原不等式得证.

可以证明

$$
(x-1) \mathrm{e}^{x}-\frac{1}{2} x^{2}>-1>\ln x-\frac{1}{2} x^{2}-\frac{1}{2}
$$

解法二 考虑证明

$$
\frac{(x-1) \mathrm{e}^{x}+1}{x^{2}} \geqslant \frac{1}{2} \geqslant \frac{\ln x+\frac{1}{2}}{x^{2}}
$$

即可.

思考与总结

事实上,可以证明

$$
\frac{(x-1) \mathrm{e}^{x}+1}{x^{2}} \geqslant 1 \geqslant \frac{\ln x+\frac{2}{\mathrm{e}}}{x^{e}}
$$

## 第 835 题 从图形角度看不等式

已知函数 $f(x)$ 满足 $f(x)=f^{\prime}(1) \mathrm{e}^{x-1}-f(0) x+\frac{1}{2} x^{2}$.

(1) 求 $f(x)$ 的解析式及单调区间;

(2) 若 $f(x) \geqslant \frac{1}{2} x^{2}+a x+b$, 求 $(a+1) b$ 的最大值.

解析 (1) 根据题意, 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=f^{\prime}(1) \mathrm{e}^{x-1}-f(0)+x
$$

分别令 $x=1$ 和 $x=0$, 可得 $f(x)=\mathrm{e}^{x}-x+\frac{1}{2} x^{2}$.

进而其导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}-1+x
$$

于是函数 $f(x)$ 的单调递增区间是 $(0,+\infty)$, 单调递减区间是 $(-\infty, 0)$.

(2) 根据题意, 有

$$
\mathrm{e}^{x} \geqslant(a+1) x+b
$$

取函数 $y=\mathrm{e}^{x}$ 的斜率为 $a+1$ 的切线, 设切点为 $t$, 则切线方程为

$$
y=\mathrm{e}^{t}(x-t)+\mathrm{e}^{t}
$$

其中 $\mathrm{e}^{t}=a+1$. 易知

$$
\mathrm{e}^{x} \geqslant \mathrm{e}^{t} x+(1-t) \mathrm{e}^{t},
$$

等号当且仅当 $x=t$ 时取得.

因此 $b \leqslant(1-t) \mathrm{e}^{t}$. 由于 $a+1=\mathrm{e}^{t}>0$, 于是

$$
(a+1) b \leqslant \mathrm{e}^{t} \cdot(1-t) \mathrm{e}^{t},
$$

记右侧函数为 $\varphi(t)$, 则其导函数

$$
\varphi^{\prime}(t)=\mathrm{e}^{2 t}(1-2 t)
$$

于是当 $t=\frac{1}{2}$ 时, $\varphi(t)$ 取得极大值, 亦为最大值 $\frac{1}{2} \mathrm{e}$.

于是 $(a+1) b$ 的最大值为 $\frac{1}{2} \mathrm{e}$, 此时 $a=\sqrt{\mathrm{e}}-1, b=\frac{1}{2} \sqrt{\mathrm{e}}$.

## 思考与总结

从图形的角度看待题中的不等式, 将含有两个变元的式子 $(a+1) b$ 转化为只含一个变元 $t$ 的式子.

## 第 836 题 以直代曲

求证: $\mathrm{e}^{x}-\ln x>2.3$.

解析 解法一 设函数 $f(x)=\mathrm{e}^{x}-\ln x$,

则 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}-\frac{1}{x}, x>0
$$

因此方程 $\mathrm{e}^{x}-\frac{1}{x}=0$ 的解为函数 $f(x)$ 的极小值点, 可以估计出极小值点约为 $\frac{1}{2}$.

取 $y=\mathrm{e}^{x}$ 在 $x=\frac{1}{2}$ 处的切线, 有

$$
\mathrm{e}^{x} \geqslant \mathrm{e}^{\frac{1}{2}}\left(x-\frac{1}{2}\right)+\mathrm{e}^{\frac{1}{2}}=\mathrm{e}^{\frac{1}{2}} x+\frac{1}{2} \cdot \mathrm{e}^{\frac{1}{2}},
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-258.jpg?height=270&width=271&top_left_y=756&top_left_x=1482)

取 $y=\ln x$ 斜率为 $\mathrm{e}^{\frac{1}{2}}$ 的切线, 切点横坐标为 $\mathrm{e}^{-\frac{1}{2}}$, 于是有

$$
\ln x \leqslant \mathrm{e}^{\frac{1}{2}}\left(x-\mathrm{e}^{-\frac{1}{2}}\right)-\frac{1}{2}=\mathrm{e}^{\frac{1}{2}} x-\frac{3}{2},
$$

因此

$$
\mathrm{e}^{x}-\ln x \geqslant \frac{1}{2} \cdot \mathrm{e}^{\frac{1}{2}}+\frac{2}{3}
$$

由于 $\mathrm{e}>2.56$, 于是 $\mathrm{e}^{\frac{1}{2}}>1.6$, 从而

$$
\frac{1}{2} \mathrm{e}^{\frac{1}{2}}+1.5>2.3
$$

## 思考与总结

该极值点即欧米加常数 $\Omega($ Omega constant $\approx 0.5671)$, 是超越方程 $x \mathrm{e}^{x}=1$ 的实数解, 满足

$$
\Omega+\ln \Omega=0, \Omega=u^{u^{u^{u^{\prime}}}},
$$

其中 $u=\frac{1}{\mathrm{e}}$, 被称为在指数函数中的黄金比例.

解法二 设函数 $f(x)=\mathrm{e}^{x}-\ln x$,

则 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}-\frac{1}{x}, x>0
$$

因此方程 $\mathrm{e}^{x}-\frac{1}{x}=0$ 的解为函数 $f(x)$ 的极小值点, 可以估计出极小值点约为 $\frac{1}{2}$. 虽然无法直接求出极小值点,但是可以利用求极值点的方程进行估计.

显然方程 $\mathrm{e}^{x}-\frac{1}{x}=0$ 的解唯一, 设为 $m$, 则

$$
\mathrm{e}^{m}=\frac{1}{m}, \ln m=-m
$$

从而 $f(x)$ 的极小值, 亦为最小值

$$
f(m)=\mathrm{e}^{m}-\ln m=\frac{1}{m}+m
$$

当 $x \in(0,1)$ 时, 有 $\ln x>\frac{1}{2}\left(x-\frac{1}{x}\right)$, 于是

$$
m=-\ln m<-\frac{1}{2}\left(m-\frac{1}{m}\right)
$$

从而 $0<m<\frac{1}{\sqrt{3}}$, 因此

$$
f(m)=\frac{1}{m}+m>\sqrt{3}+\frac{1}{\sqrt{3}}>2.3
$$

## 第 837 题 另类的比较大小

已知函数 $f(x)=\frac{x^{2}}{2}+a x+2 \ln x$ 在 $x=2$ 处取得极值.

(1) 求实数 $a$ 的值及函数 $f(x)$ 的单调区间;

(2) 方程 $f(x)=m$ 有 3 个实数解 $x_{1}, x_{2}, x_{3}\left(x_{1}<x_{2}<x_{3}\right)$, 求证: $x_{3}-x_{1}<2$.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{x^{2}+a x+2}{x}
$$

根据题意, $x=2$ 是函数 $f^{\prime}(x)$ 的零点, 因此 $a=-3$.

经验证, $a=-3$ 符合题意, 此时 $f(x)$ 的单调递增区间是 $(0,1)$ 和 $(2,+\infty)$,单调递减区间是 $(1,2)$.

(2) 只需要证明对任意 $x>0$,均有

$$
f(x+2)-f(x)>0,
$$

即

$$
\forall x>0, x-2+\ln \left(1+\frac{2}{x}\right)>0
$$

设函数

$$
g(x)=x-2+\ln \left(1+\frac{2}{x}\right)
$$

则 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{x^{2}+2 x-2}{x^{2}+2 x}
$$

因此 $g(x)$ 的最小值为 $g(\sqrt{3}-1)$.

接下来只需要证明 $g(\sqrt{3}-1)>0$.

解法一 由于

$$
\begin{aligned}
g(\sqrt{3}-1) & =\sqrt{3}-3+\ln (\sqrt{3}+1)-\ln (\sqrt{3}-1) \\
& >\sqrt{3}-3+\ln -(\sqrt{3}-2) \\
& =0,
\end{aligned}
$$

因此原命题得证.

解法二 由于

$$
g(\sqrt{3}-1)=\ln (2+\sqrt{3})+\sqrt{3}-3
$$

于是只需要证明

$$
\ln (2+\sqrt{3})>-\sqrt{3}+3
$$

即证明

$$
\ln (2-\sqrt{3})<\sqrt{3}-3
$$

注意到 $2-\sqrt{3} \approx \frac{1}{\mathrm{e}}$, 于是取 $y=\ln x$ 在 $x=\frac{1}{\mathrm{e}}$ 处的切线,

当 $x \neq \frac{1}{\mathrm{e}}$ 时有

$$
\ln x<\mathrm{e} \cdot\left(x-\frac{1}{\mathrm{e}}\right)-1
$$

于是

$$
\ln (2-\sqrt{3})<(2-\sqrt{3}) \mathrm{e}-2
$$

因此只需证明

$$
(2-\sqrt{3}) e<\sqrt{3}-1
$$

即

$$
\mathrm{e}<\frac{\sqrt{3}-1}{2-\sqrt{3}}=1+\sqrt{3}
$$

这显然成立,因此原命题得证.

注一 也可以利用 $x_{2}$ 作为过渡, 构造对称函数证明两个极值点偏移不等式

$$
x_{1}+x_{2}>2, x_{2}+x_{3}<4
$$

注ニ 也可以用

$$
\begin{aligned}
g(x) & =x-2+\ln \left(1+\frac{2}{x}\right) \\
& >x-2+\frac{2 \cdot \frac{2}{x}}{2+\frac{2}{x}} \\
& =x+1+\frac{2}{x+1}-3 \\
& >0 .
\end{aligned}
$$

## 第 838 题 以直代曲

已知 $x \in(0, \mathrm{e})$, 求证: $\frac{\left(\mathrm{e}^{2}-\mathrm{e}^{2} \ln x+x\right)^{2}}{\ln ^{2} x+2 \ln x+2}>\frac{\mathrm{e}^{2}}{5}$.

解析 $\quad$ 题中不等式等价于

$$
\left[\mathrm{e}^{\ln x-1}-\mathrm{e}(\ln x-1)\right]^{2}>\frac{1}{5}\left(\ln ^{2} x+2 \ln x+2\right),
$$

令 $t=\ln x-1(t<0)$, 则不等式等价于

$$
\left(\mathrm{e}^{t}-\mathrm{e} t\right)^{2}>\frac{1}{5} t^{2}+\frac{4}{5} t+1
$$

取函数 $y=\mathrm{e}^{t}-\mathrm{e} t$ 在 $t=0$ 处的切线, 有

$$
\mathrm{e}^{t}-\mathrm{e} t>(1-\mathrm{e}) t+1, t<0,
$$

因此

$$
\left(\mathrm{e}^{t}-\mathrm{e} t\right)^{2}>[(1-\mathrm{e}) t+1]^{2}=(\mathrm{e}-1)^{2} t^{2}-2(\mathrm{e}-1) t+1
$$

而当 $t<0$ 时, 有

$$
(\mathrm{e}-1)^{2} t^{2}>\frac{1}{5} t^{2},-2(\mathrm{e}-1) t>\frac{4}{5} t
$$

因此原不等式得证.

利用切线将曲线放缩成直线是处理函数不等式的重要方法.

## 第 839 题 壮士断腕

已知函数 $f(x)=\frac{1}{3} x^{3}+\frac{1}{2} b x^{2}+c x+d$ 在区间 $(0,1)$ 上既有极大值又有极小值, 则 $c^{2}+(1+b) c$ 的取值范围是 $\qquad$ .

解析 $\left(0, \frac{1}{16}\right)$.

虽然本题需要利用导数知识得到关于 $x$ 的方程

$$
x^{2}+b x+c=0
$$

在区间 $(0,1)$ 上有两根, 但是解决问题的关键是如何根据此含参二次方程的根的分布确定系数形成的代数式的取值范围.

如果我们直接将根的分布转化为对系数的要求:

$$
\left\{\begin{array}{l}
c>0 \\
1+b+c>0 \\
0<-\frac{b}{2}<1 \\
b^{2}-4 c>0
\end{array}\right.
$$

那么就需要面对一个复杂的规划问题,进而会付出沉重的代价.

那么怎样才能简化问题呢?

其实借助韦达定理,我们可以轻松地完成从根到系数的转化 (从系数到根的转化是由二次方程的求根公式承担的), 于是放弃所有原有参数, 选择用此二次方程的两个根 $x_{1}$ 和 $x_{2}$ 为参数描述问题. 此时, $x_{1}, x_{2} \in$ $(0,1)$, 而

$$
c=x_{1} \cdot x_{2}, b=-\left(x_{1}+x_{2}\right)
$$

代人欲求代数式整理得

$$
c^{2}+(1+b) c=x_{1} \cdot x_{2} \cdot\left(1-x_{1}\right) \cdot\left(1-x_{2}\right),
$$

借助均值不等式, 不难得到 $c^{2}+(1+b) c$ 的取值范围是 $\left(0, \frac{1}{16}\right)$.

事实上, 令方程左边为 $h(x)$, 则

$$
h(x)=\left(x-x_{1}\right) \cdot\left(x-x_{2}\right)
$$

如果观察到

$$
c^{2}+(1+b) c=h(0) \cdot h(1)
$$

那么可以更直接地得到它用 $x_{1}$ 与 $x_{2}$ 表达的式子.
根据具体的问题选取合适的参数是简便求解的基本出发点. 在这个问题中, 同学们应该有放弃所有原有参数而重新设参的勇气.

## 第 840 题 以直代曲

已知函数 $f(x)=n x-x^{n}, x \in \mathbf{R}$, 其中 $n \in \mathbf{N}^{*}$, 且 $n \geqslant 2$.

(1) 讨论 $f(x)$ 的单调性;

(2) 设曲线 $y=f(x)$ 与 $x$ 轴正半轴的交点为 $P$, 曲线在点 $P$ 处的切线方程为 $y=g(x)$, 求证: 对于任意的正实数 $x$, 都有 $f(x) \leqslant g(x)$;

(3) 若关于 $x$ 的方程 $f(x)=a$ ( $a$ 为实数) 有两个正实数根 $x_{1}, x_{2}$, 求证: $\left|x_{1}-x_{2}\right|<\frac{a}{1-n}+2$.

解析 (1) 根据题意, 有

$$
f^{\prime}(x)=n-n x^{n-1}
$$

于是当 $n$ 为奇数时, 函数 $f(x)$ 在 $(-\infty,-1)$ 上单调递减, 在 $(-1,1)$ 上单调递增, 在 $(1,+\infty)$ 上单调递减;

当 $n$ 为偶数时, 函数 $f(x)$ 在 $(-\infty, 1)$ 上单调递增, 在 $(1,+\infty)$ 上单调递减.

(2) 根据题意, 点 $P$ 的坐标为 $P\left(n^{\frac{1}{n-1}}, 0\right)$, 于是曲线在点 $P$ 处的切线方程为

$$
g(x)=\left(n-n^{2}\right)\left(x-n^{\frac{1}{n-1}}\right)
$$

进而

$$
g(x)-f(x)=x^{n}-n^{2} x+\left(n^{2}-n\right) \cdot \frac{\frac{1}{n^{n-1}}}{}
$$

其导函数为

$$
(g(x)-f(x))^{\prime}=n x^{n-1}-n^{2}
$$

于是函数 $g(x)-f(x)$ 在 $x=n^{\frac{1}{n-1}}$ 处取得极小值, 同时也为最小值 0 .

因此原命题得证.

(3) 显然符合题意的 $a>0$. 不妨设 $0<x_{1}<x_{2}<n^{\frac{1}{n-1}}$, 以下所有函数的定义域均默认为 $\left[0, n^{\frac{1}{n-1}}\right]$.

考虑函数 $f(x)$ 在 $x=0$ 处的切线

$$
h(x)=n x \text {, }
$$

由于

$$
h(x)-f(x)=x^{n} \geqslant 0,
$$

于是可得

$$
f(x) \leqslant h(x),
$$

如图.

因此我们可以利用这两条曲线对 $x_{1}, x_{2}$ 进行线性估计(以直代曲).

设

$$
f\left(x_{1}\right)=h\left(x_{3}\right)=g\left(x_{4}\right)=f\left(x_{2}\right)=a
$$

则有

$$
x_{3}<x_{1}<x_{2}<x_{4}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-262.jpg?height=350&width=442&top_left_y=2203&top_left_x=1327)

于是有

$$
\left|x_{1}-x_{2}\right|<x_{4}-x_{3}=\left(\frac{a}{n-n^{2}}+n^{\frac{1}{n-1}}\right)-\frac{a}{n}=\frac{a}{1-n}+n^{\frac{1}{n-1}},
$$

接下来只需要证明

$$
n^{\frac{1}{n-1}} \leqslant 2
$$

即

$$
n \leqslant 2^{n-1}
$$

事实上,根据二项式定理, 有

$$
2^{n-1}=(1+1)^{n-1} \geqslant 1+\mathrm{C}_{n-1}^{1}=n,
$$

等号当且仅当 $n=2$ 时取得. 因此原命题得证.

## 第 841 题 解高次不等式

已知函数 $f(x)=x^{3}+a x^{2}+b(a, b \in \mathbf{R})$.

(1) 试讨论 $f(x)$ 的单调性;

(2) 若 $b=c-a$ (实数 $c$ 是与 $a$ 无关的常数), 当函数 $f(x)$ 有三个不同的零点时, $a$ 的取值范围恰好是 $(-\infty,-3) \cup\left(1, \frac{3}{2}\right) \cup\left(\frac{3}{2},+\infty\right)$, 求 $c$ 的值.

解析 $(1)$ 根据已知有

$$
f^{\prime}(x)=3 x^{2}+2 a x
$$

于是

情形一 当 $a=0$ 时, $f(x)$ 在 $\mathbf{R}$ 上单调递增;

情形二 当 $a<0$ 时, $f(x)$ 在 $(-\infty, 0)$ 和 $\left(-\frac{2 a}{3},+\infty\right)$ 上单调递增, 在 $\left(0,-\frac{2 a}{3}\right)$ 上单调递减;

情形三 当 $a>0$ 时, $f(x)$ 在 $\left(-\infty,-\frac{2 a}{3}\right)$ 和 $(0,+\infty)$ 上单调递增, 在 $\left(-\frac{2 a}{3}, 0\right)$ 上单调递减.

(2) 函数 $f(x)$ 有三个不同零点等价于 $f(x)$ 的极大值与极小值异号, 即

$$
f(0) \cdot f\left(-\frac{2 a}{3}\right)<0
$$

也即

$$
(c-a)\left(\frac{4}{27} a^{3}+c-a\right)<0
$$

整理得

$$
(a-c)\left(a^{3}-\frac{27}{4} a+\frac{27}{4} c\right)>0
$$

该不等式的解为 $(-\infty,-3) \cup\left(1, \frac{3}{2}\right) \cup\left(\frac{3}{2},+\infty\right)$, 于是对应的四次不等式为

$$
(a+3)(a-1)\left(a-\frac{3}{2}\right)^{2}>0
$$

对比系数解得 $c=1$, 因此所求 $c$ 的值为 1 .

## 第 842 题 构造函数

已知定义在 $\mathbf{R}$ 上的奇函数 $f(x)$ 满足 $f^{\prime}(x)>-2$, 则不等式

$$
f(x-1)<x^{2}(3-2 \ln x)+3(1-2 x)
$$

的解集是 $\qquad$
解析 $(0,1)$.

所解不等式左边是一个抽象函数, 我们需要充分利用题目所给条件: $f(x)$ 为奇函数, 且 $f^{\prime}(x)>-2$.于是我们令 $g(x)=f(x)+2 x$, 则函数 $g(x)$ 为 $\mathbf{R}$ 上的单调递增函数, 且 $g(0)=0$.

根据题意, 将不等式整理为

$$
f(x-1)+2(x-1)<3 x^{2}-4 x+1-2 x^{2} \ln x
$$

即

$$
g(x-1)<3 x^{2}-4 x+1-2 x^{2} \ln x
$$

下面我们来研究不等号右边的函数的性质,

因为有对数函数, 所以我们先将右边变形为 $x^{2}\left(3-\frac{4}{x}+\frac{1}{x^{2}}-2 \ln x\right)$,

令

$$
h(x)=3-\frac{4}{x}+\frac{1}{x^{2}}-2 \ln x
$$

则 $h(x)$ 的导函数

$$
h^{\prime}(x)=-\frac{2(x-1)^{2}}{x^{3}} \leqslant 0
$$

于是 $h(x)$ 单调递减, 又注意到 $h(1)=0$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-264.jpg?height=290&width=265&top_left_y=1235&top_left_x=1507)

于是当 $0<x<1$ 时, $g(x-1)<0<x^{2} \cdot h(x)$; 当 $x \geqslant 1$ 时, $x^{2} \cdot h(x) \leqslant 0 \leqslant g(x-1)$. 示意图如图.

综上,所求的解集为 $(0,1)$.

## 第 843 题 函数与方程

已知 $f(x)=\left|x \mathrm{e}^{x}\right|$, 又 $g(x)=f^{2}(x)-t f(x)(t \in \mathbf{R})$, 若满足 $g(x)=-1$ 的 $x$ 有四个, 则 $t$ 的取值范围是 $\qquad$ .

解析 $\left(\mathrm{e}+\mathrm{e}^{-1},+\infty\right)$.

解法一 方程 $g(x)=-1$, 即

$$
f^{2}(x)-t f(x)+1=0
$$

也即

$$
t=f(x)+\frac{1}{f(x)}
$$

考虑复合函数

$$
y=u+\frac{1}{u}, u=\left|x \mathrm{e}^{x}\right|
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-264.jpg?height=301&width=377&top_left_y=2205&top_left_x=1394)

以及直线 $y=t$.
由于函数 $u=\left|x \mathrm{e}^{x}\right|$ 的图象如图,

因此函数 $y=u+\frac{1}{u}$ 的图象和直线 $y=t$ 有两个公共点, 且它们的横坐标 $u_{1}, u_{2}$ 满足

$$
0<u_{1}<\mathrm{e}^{-1}<u_{2},
$$

因此对应的 $t$ 的取值范围是 $\left(\mathrm{e}+\mathrm{e}^{-1},+\infty\right)$.

解法二 令 $u=f(x)$, 则有

$$
u^{2}-t u+1=0
$$

记此方程的两根为 $u_{1}, u_{2}$, 则方程 $g(x)=-1$ 的根即 $u_{i}=f(x), i=1,2$ 的根.

画出 $u=f(x)$ 的图象:

结合图象知 $u_{i}=f(x), i=1,2$ 有三个根时有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-265.jpg?height=214&width=379&top_left_y=508&top_left_x=1483)

$$
u_{1} \in\left(0, \mathrm{e}^{-1}\right), u_{2} \in\left(\mathrm{e}^{-1},+\infty\right),
$$

即一元二次方程 $u^{2}-t u+1=0$ 的两根分别在区间 $\left(0, \mathrm{e}^{-1}\right),\left(\mathrm{e}^{-1},+\infty\right)$ 上.

记 $g(x)=x^{2}-t x+1$,

因为 $g(0)=1>0$, 所以只需令

$$
g\left(\mathrm{e}^{-1}\right)<0,
$$

解得 $t>\mathrm{e}+\mathrm{e}^{-1}$.

## 第 844 题 复合函数的零点

已知函数 $f(x)=a x+\ln x-\frac{x^{2}}{x-\ln x}$ 有三个不同的零点 $x_{1}, x_{2}, x_{3}$ (其中 $x_{1}<x_{2}<x_{3}$ ), 则

$$
\left(1-\frac{\ln x_{1}}{x_{1}}\right)^{2}\left(1-\frac{\ln x_{2}}{x_{2}}\right)\left(1-\frac{\ln x_{3}}{x_{3}}\right)
$$

的值为
A. $1-a$
B. $a-1$
C. -1
D. 1

解析 D.

函数的零点即方程 $(a x+\ln x)(x-\ln x)=x^{2}$ 的解,

因为 $x>0$,所以方程可以变形为

$$
\left(a+\frac{\ln x}{x}\right)\left(1-\frac{\ln x}{x}\right)=1
$$

令 $t=\frac{\ln x}{x}$, 记函数 $g(x)=\frac{\ln x}{x}$, 则有

$$
g^{\prime}(x)=\frac{1-\ln x}{x^{2}}
$$

所以 $g(x)$ 在 $(1, \mathrm{e})$ 上单调递增, 在 $(\mathrm{e},+\infty)$ 上单调递减, $g(x)_{\max }=\frac{1}{\mathrm{e}}, g(x)$的图象如图.

所求方程的解相当于先求一元二次方程 $(a+t)(1-t)=1$ 的解 $t_{1}, t_{2}\left(t_{1} \leqslant t_{2}\right)$,再求方程 $g(x)=t_{i}, i=1,2$ 的解.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-265.jpg?height=241&width=393&top_left_y=2098&top_left_x=1462)

因为方程有三个不同零点, 所以 $t_{1}<t_{2} \leqslant \frac{1}{\mathrm{e}}$.

先考虑一元二次方程

$$
t^{2}+(a-1) t+1-a=0,
$$

由判别式 $\Delta>0$ 解得 $a>1$ 或 $a<-3$,

由事达定理知

$$
t_{1}+t_{2}=1-a, t_{1} t_{2}=1-a
$$

当 $a<-3$ 时, $t_{1}+t_{2}=1-a>4$ 与 $t_{1}<t_{2} \leqslant \frac{1}{\mathrm{e}}$ 矛盾,

所以

$$
a>1, t_{1}<0<t_{2}<\frac{1}{\mathrm{e}}
$$

于是知

$$
g\left(x_{1}\right)=t_{1}, g\left(x_{2}\right)=g\left(x_{3}\right)=t_{2} .
$$

所求代数式为

$$
\left(1-t_{1}\right)^{2}\left(1-t_{2}\right)\left(1-t_{2}\right)=\left[\left(1-t_{1}\right)\left(1-t_{2}\right)\right]^{2}=\left[1-\left(t_{1}+t_{2}\right)+t_{1} t_{2}\right]^{2}=1 .
$$

## 第 845 题 复合函数的联合图象

已知函数 $f(x)=\left\{\begin{array}{ll}\ln x, & x \geqslant 1, \\ 1-\frac{x}{2}, & x<1,\end{array}\right.$ 若 $F(x)=f(f(x)+1)+m$ 有两个零点 $x_{1}, x_{2}$, 则 $x_{1}+x_{2}$ 的取值范围是

解析 $[4-2 \ln 2,+\infty)$.

把问题转化为 $f(t)=-m, t=f(x)+1$. 如图, $x_{1}, x_{2}$ 为函数 $f(t)=-m$ 的解 $t=t_{i}$ 对应到 $f(x)+1=t_{i}$ 的解, 结合图象知 $t_{i}>\frac{3}{2}$ 时, 对应两个解 $x_{1}, x_{2}$.

不妨设 $x_{1}<x_{2}$, 于是

$$
1-\frac{x_{1}}{2}=\ln x_{2}=u
$$

其中 $u=t-1, u>\frac{1}{2}$, 有

$$
x_{1}+x_{2}=2-2 u+\mathrm{e}^{u},
$$

设 $\varphi(u)=2-2 u+\mathrm{e}^{u}$, 则其导函数

$$
\varphi^{\prime}(u)=\mathrm{e}^{u}-2
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-266.jpg?height=305&width=383&top_left_y=1317&top_left_x=1368)

因此所求的范围是 $[\varphi(\ln 2),+\infty)$, 即 $[4-2 \ln 2,+\infty)$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-266.jpg?height=338&width=357&top_left_y=1631&top_left_x=1373)

## 第 846 题 残缺的藏宝图

若函数 $f(x)=-\ln x+a x^{2}+b x-a-2 b$ 有两个极值点 $x_{1}, x_{2}$, 其中 $-\frac{1}{2}<a<0<b$, 且 $f\left(x_{2}\right)=x_{2}$ $>x_{1}$, 则方程 $2 a[f(x)]^{2}+b f(x)-1=0$ 的实根个数为 $\qquad$个.

解析 5.

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{2 a x^{2}+b x-1}{x}
$$

于是方程

$$
2 a[f(x)]^{2}+b f(x)-1=0
$$

的实根实际上就是复合函数 $f^{\prime}(f(x))$ 的零点, 其处理方法是从外向内逐层“剥开”.根据以上分析, 题中方程等价于

$$
f(x)=x_{1} \text { 或 } f(x)=x_{2},
$$

因此其实根个数就是函数 $f(x)$ 的图象与直线 $y=x_{1}$ 以及直线 $y=x_{2}$ 的交点个数的总和. 这样一来, 如何准确作出函数 $f(x)$ 的图象成了解决问题的关键.

如图 1, 由 $a<0$ 可以作出 $f^{\prime}(x)$ 的 “示性函数” (决定函数值正负性质的部分因式) $y=2 a x^{2}+b x-1$ 的草图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-267.jpg?height=317&width=350&top_left_y=410&top_left_x=1528)

图 1

又函数 $f(x)$ 的定义域为 $(0,+\infty)$, 其在区间端点处的函数值 $f\left(0^{+}\right)=+\infty, f(+\infty)=-\infty$. 此外题中告知 $f\left(x_{2}\right)=x_{2}>0$.

结合导函数图象与函数在 $0, x_{2},+\infty$ 处的取值可以作出函数 $f(x)$ 的部分图象 (缺失极值点 $x=x_{1}$ 处的信息). 据此“残图”可以确定直线 $y=x_{2}$ 与函数 $f(x)$ 的图象交点数为 2 .

为了确定函数 $f(x)$ 的图象中残缺的部分, 我们需要另外探寻一些特殊点. 先考虑方程

$$
2 a x^{2}+b x-1=0
$$

有

$$
x_{1}+x_{2}=-\frac{b}{2 a}, x_{1} x_{2}=-\frac{1}{2 a},
$$

进而可得

$$
x_{1}+x_{2} \in(0,+\infty), x_{1} x_{2} \in(1,+\infty)
$$

这样一来,我们可以断定 $x_{2}>1$, 因此选择 $x=1$ 为特殊点进行探索.

事实上, $f(1)=-b<0$, 于是我们“勘探”出在 $x=x_{2}$ 左侧的未知领域有一片 “绿洲”(函数值小于 0 的部分), 而 $x=x_{1}$ 就是这片“绿洲” 的“中心小镇”. 这样就有 $x_{1}>$ $0>f\left(x_{1}\right)$, 如图 2. 这样直线 $y=x_{1}$ 与函数 $y=f(x)$ 的图象有 3 个交点.

综上, 题中方程的实根个数为 5 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-267.jpg?height=333&width=372&top_left_y=1263&top_left_x=1506)

图 2

最后给出一个近似准确的图象, 其中 $a=-0.3, b=4.788$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-267.jpg?height=366&width=700&top_left_y=1793&top_left_x=678)

## 第 847 题 二阶不动点

设函数 $f(x)=\sqrt{\mathrm{e}^{x}+x-a}(a \in \mathbf{R})$. 若曲线 $y=\sin x$ 上存在点 $\left(x_{0}, y_{0}\right)$ 使得 $f\left(f\left(y_{0}\right)\right)=y_{0}$, 则 $a$ 的取值范围是 $\qquad$ .

解析 $[1, \mathrm{e}]$.

由于 $f(x)$ 单调递增, 于是问题等价于 $f(x)$ 的图象与直线 $y=x$ 在 $[0,1]$ 上有公共点,

即关于 $x$ 的方程

$$
\sqrt{\mathrm{e}^{x}+x-a}=x
$$

在 $[0,1]$ 上有解, 于是有

$$
a=\mathrm{e}^{x}-x^{2}+x, x \in[0,1]
$$

记 $g(x)=\mathrm{e}^{x}-x^{2}+x$, 则其导函数

$$
g^{\prime}(x)=\mathrm{e}^{x}-2 x+1>0
$$

所以 $g(x)$ 在 $[0,1]$ 上单调递增, 从而 $a$ 的取值范围是 $[g(0), g(1)]$, 也即 $[1, \mathrm{e}]$.

## 思考与总结

如图, 当 $a$ 分别取 1 和 $\mathrm{e}$ 时, 对应的 $y=f(x)$ 与 $x=f(y)$ 的图象.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-268.jpg?height=272&width=528&top_left_y=1280&top_left_x=650)

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-268.jpg?height=71&width=504&top_left_y=1678&top_left_x=654)

已知函数 $f(x)$ 在 $[0,+\infty)$ 上可导, 其导函数记作 $f^{\prime}(x), f(0)=-2$, 且 $f(x+\pi)=-\frac{1}{2} f(x)$. 当 $x$ $\in(0, \pi)$ 且 $x \neq \frac{\pi}{2}$ 时,

$$
f^{\prime}(x) \cdot \cos 2 x>f(x) \cdot \sin 2 x-f^{\prime}(x)
$$

若方程 $f(x)+k_{n} \frac{1}{\cos \theta}=0$ 在 $[0,+\infty)$ 上有 $n$ 个解, 则数列 $\left\{\frac{n}{k_{2 n}}\right\}$ 的前 $n$ 项和为 $\qquad$ .

解析 $(n-1) \cdot 2^{n}+1$.

观察题目的结构, 等式 $f(x+\pi)=-\frac{1}{2} f(x)$ 描述了类周期性, 表明了如何通过 $[0, \pi)$ 上的函数图象延拓出整个定义域上的图象. 于是描述导函数的不等式应该是为了描述与 $f(x)$ 有关的某个函数的单调性. 根据所求问题,可以猜测关键的函数为 $g(x)=\cos x \cdot f(x)$.

由于不等式

$$
f^{\prime}(x) \cdot \cos 2 x>f(x) \cdot \sin 2 x-f^{\prime}(x)
$$

即

$$
2 \cos x \cdot(\cos x \cdot f(x))^{\prime}>0
$$

于是令函数 $g(x)=\cos x \cdot f(x)$, 则 $g(x)$ 在 $\left[0, \frac{\pi}{2}\right)$ 上单调递增, 在 $\left[\frac{\pi}{2}, \pi\right)$ 上单调递减.

由 $f(0)=-2$, 且 $f(x+\pi)=-\frac{1}{2} f(x)$ 可得

$$
g(0)=-2, g(x+\pi)=\frac{1}{2} g(x)
$$

于是函数 $g(x)$ 的图象如图所示 (为了简单起见用折线代替了曲线, 虽然违反了可导,但是不影响公共点判断).

于是直线 $y=-k_{2 n}$ 与函数 $g(x)$ 的图象有 $2 n$ 个公共点, 因此

$$
k_{2 n}=\frac{1}{2^{n-1}}, n=1,2, \cdots
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-269.jpg?height=227&width=375&top_left_y=587&top_left_x=1488)

从而 $\frac{n}{k_{2 n}}=n \cdot 2^{n-1}$, 求和可得其前 $n$ 项和为 $(n-1) \cdot 2^{n}+1$.

## 第 849 题 花落谁家

## 已知函数

$$
f(x)=1+x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots+\frac{x^{2017}}{2017},
$$

函数

$$
g(x)=1-x+\frac{x^{2}}{2}-\frac{x^{3}}{3}+\frac{x^{4}}{4}+\cdots-\frac{x^{2017}}{2017}
$$

设 $F(x)=f(x+3) \cdot g(x-3)$, 且函数 $F(x)$ 的零点在区间 $[a, b](a<b, a, b \in \mathbf{Z})$ 内, 则 $b-a$ 的最小值为 $\qquad$ .

解析 9.

设函数

$$
h(x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots+\frac{x^{2017}}{2017}
$$

则 $f(x)=1+h(x), g(x)=1-h(x)$.

因此只需要考虑函数 $h(x)$ 的图象与直线 $y=1$ 以及 $y=-1$ 的公共点的横坐标的范围.

函数 $h(x)$ 的导函数

$$
h^{\prime}(x)=1-x+x^{2}-x^{3}+\cdots+x^{2016}= \begin{cases}\frac{1+x^{2017}}{1+x}, & x \neq-1 \\ 2017, \quad x=-1\end{cases}
$$

因此在 $\mathbf{R}$ 上, 函数 $h(x)$ 单调递增. 而

$$
\begin{aligned}
& h(-1)=-1-\frac{1}{2}-\frac{1}{3}-\frac{1}{4}-\cdots-\frac{1}{2017} \in(-\infty,-1) \\
& h(0)=0 \\
& h(1)=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots+\frac{1}{2017} \in(0,1) \\
& h(2)=2+2^{2}\left(-\frac{1}{2}+\frac{2}{3}\right)+2^{4}\left(-\frac{1}{4}+\frac{2}{5}\right)+\cdots+2^{2016}\left(-\frac{1}{2016}+\frac{2}{2017}\right) \in(2,+\infty)
\end{aligned}
$$

因此函数 $f(x)$ 的零点位于 $(-1,0)$ 内, 函数 $g(x)$ 的零点位于 $(1,2)$ 内, 进而函数 $F(x)$ 的零点分别位于 $(-4,-3)$ 和 $(4,5)$ 内, 于是 $b-a$ 的最小值为 9 .

## 第 850 题 举重若轻

已知函数

$$
f(x)=1+x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots-\frac{x^{2014}}{2014}+\frac{x^{2015}}{2015}
$$

若函数 $f(x)$ 的零点都在区间 $[a, b]$ (其中 $a<b$ 且 $a, b \in \mathbf{Z}$ ) 内, 则 $b-a$ 的最小值为

## 解析 1.

注意到

$$
f^{\prime}(x)=1-x+x^{2}-x^{3}+\cdots-x^{2013}+x^{2014}= \begin{cases}2015, & x=-1 \\ \frac{1+x^{2015}}{1+x}, & x \neq-1\end{cases}
$$

因此 $f(x)$ 在 $\mathbf{R}$ 上单调递增.

考虑到

$$
f(-1)<0, f(0)>0
$$

于是 $f(x)$ 的所有零点都在区间 $[-1,0]$ 内, 因此 $b-a$ 的最小值为 1 .

## 第 851 题 指数函数的凹凸性

设 $f_{n}(x)$ 是等比数列 $1, x, x^{2}, \cdots, x^{n}$ 的各项和, 其中 $x>0, n \in \mathbf{N}, n \geqslant 2$.

(1) 证明: 函数 $F_{n}(x)=f_{n}(x)-2$ 在 $\left(\frac{1}{2}, 1\right)$ 内有且仅有一个零点 (记为 $\left.x_{n}\right)$, 且 $x_{n}=\frac{1}{2}+\frac{1}{2} x_{n}^{n+1}$;

(2)设有一个与上述等比数列的首项、末项、项数分别相同的等差数列, 其各项和为 $g_{n}(x)$, 比较 $f_{n}(x)$ 和 $g_{n}(x)$ 的大小, 并加以证明.

解析 (1)根据已知, 有

$$
F_{n}(x)=x+x^{2}+\cdots+x^{n}-1
$$

于是

$$
F_{n}\left(\frac{1}{2}\right)=\frac{1}{2}+\frac{1}{2^{2}}+\cdots+\frac{1}{2^{n}}-1=-\frac{1}{2^{n}}<0
$$

而

$$
F_{n}(1)=n-1>0
$$

另一方面, 考虑到在 $\left(\frac{1}{2}, 1\right)$ 上,

$$
F^{\prime}{ }_{n}(x)=1+2 x+\cdots+n x^{n-1}>0
$$

因此函数 $F_{n}(x)$ 在 $\left(\frac{1}{2}, 1\right)$ 上单调递增.

综合以上, 函数 $F_{n}(x)$ 在 $\left(\frac{1}{2}, 1\right)$ 内有且仅有一个零点.

由

$$
x_{n}+x_{n}^{2}+\cdots+x_{n}^{n}-1=0
$$

可得

$$
\frac{x_{n}-x_{n}^{n+1}}{1-x_{n}}-1=0
$$

整理即得

$$
x_{n}=\frac{1}{2}+\frac{1}{2} x_{n}^{n+1}
$$

(2) 当 $x=1$ 时, $f_{n}(x)=g_{n}(x)$; 当 $x \neq 1$ 时, $f_{n}(x)<g_{n}(x)$, 证明如下.

根据题意描述, $n \geqslant 3$.

考虑

$$
h_{n}(x)=f_{n}(x)-g_{n}(x)=1+x+x^{2}+\cdots+x^{n}-\frac{n+1}{2}\left(1+x^{n}\right)
$$

的导数

$$
\begin{aligned}
h_{n}^{\prime}(x) & =1+2 x+\cdots+n x^{n-1}-\frac{n(n+1)}{2} \cdot x^{n-1} \\
& =x^{n-1}\left[1 \cdot\left(\frac{1}{x}\right)^{n-1}+2 \cdot\left(\frac{1}{x}\right)^{n-2}+\cdots+n-\frac{n(n+1)}{2}\right]
\end{aligned}
$$

于是函数 $h_{n}(x)$ 在 $(0,1)$ 上单调递增, 在 $(1,+\infty)$ 上单调递减. 考虑到 $h_{n}(1)=0$, 于是结论得证.

题 (2) 的几何意义为指数函数图象的割线恒在指数函数图象的上方. 因此也可以将 $x$ 视为常数, 证明当 $x \neq 1$ 时,

$$
x^{k} \leqslant 1+k \cdot \frac{x^{n}-1}{n}
$$

对 $k=0,1,2, \cdots, n$ 成立即可.

## 第 852 题 对称之美

已知函数 $g(x)=\frac{1}{3} x^{3}-\frac{1}{2} x^{2}+3 x-\frac{5}{12}+\cos \left(x-\frac{\pi+1}{2}\right)$, 求 $g\left(\frac{1}{2016}\right)+g\left(\frac{2}{2016}\right)+\cdots+g\left(\frac{2014}{2016}\right)$ $+g\left(\frac{2015}{2016}\right)$ 的值.

解析 观察所求式子中自变量的特点, 可知解决此题的关键是寻找对称中心. 我们可以利用导函数的对称轴去寻找 $g(x)$ 的对称中心, 但发现 $g(x)$ 没有对称中心. 观察 $g(x)$, 它是由一个三次函数和一个余弦函数相加得到的, 这两个函数都是中心对称的函数, 我们分别寻找它们的对称中心, 求出它们在各个点的函数值之和, 再相加即可.

令

$$
s(x)=\frac{1}{3} x^{3}-\frac{1}{2} x^{2}+3 x-\frac{5}{12}, v(x)=\cos \left(x-\frac{\pi+1}{2}\right)=\sin \left(x-\frac{1}{2}\right),
$$

则

$$
g(x)=s(x)+v(x)
$$

$s(x)$ 的导函数

$$
s^{\prime}(x)=x^{2}-x+3
$$

的对称轴为直线 $x=\frac{1}{2}$, 于是 $s(x)$ 关于点 $\left(\frac{1}{2}, s\left(\frac{1}{2}\right)\right)$ 成中心对称.
又由正弦函数的性质知, $v(x)$ 的一个对称中心是 $\left(\frac{1}{2}, 0\right)$.

于是有

$$
s(x)+s(1-x)=2 s\left(\frac{1}{2}\right)=2, v(x)+v(1-x)=0
$$

由倒序相加法知

$$
\sum_{i=1}^{2015} s\left(\frac{i}{2016}\right)=\frac{1}{2} \sum_{i=1}^{2015}\left[s\left(\frac{i}{2016}\right)+s\left(\frac{2016-i}{2016}\right)\right]=2015 .
$$

同理有

$$
\sum_{i=1}^{2015} v\left(\frac{i}{2016}\right)=0
$$

故所求的值为 $2015+0=2015$.

## 第 853 题 善挖线索汀构函数

设函数 $f(x)$ 在 $\mathbf{R}$ 上存在导函数 $f^{\prime}(x)$, 对任意 $x \in \mathbf{R}$, 有 $f(-x)+f(x)=x^{2}$, 且在 $(0,+\infty)$ 上 $f^{\prime}(x)>x$. 若 $f(2-a)-f(a) \geqslant 2-2 a$, 则实数 $a$ 的取值范围为

解析 $(-\infty,-1]$.

由题意知

$$
\forall x>0, f^{\prime}(x)-x>0
$$

于是构造函数

$$
g(x)=f(x)-\frac{1}{2} x^{2}
$$

由 $g^{\prime}(x)>0$ 知 $g(x)$ 在 $(0,+\infty)$ 上单调递增.

又由条件 $f(-x)+f(x)=x^{2}$ 知

$$
g(-x)+g(x)=0
$$

即 $g(x)$ 为奇函数.

因为 $f(x)$ 在 $\mathbf{R}$ 上存在导数, 所以 $g(x)$ 也在 $\mathbf{R}$ 上存在导数, 所以 $g(x)$ 在 $\mathbf{R}$ 上单调递增,

由 $f(2-a)-f(a) \geqslant 2-2 a$ 知

$$
g(2-a) \geqslant g(a)
$$

从而有

$$
2-a \geqslant a,
$$

解得 $a \leqslant 1$.

定义在 $\mathbf{R}$ 上的奇函数在 $(0,+\infty)$ 上单调递增, 并不能得到 $f(x)$ 在 $\mathbf{R}$ 上单调递增, 但加上连续的条件就可以得到了. 导数的正负可以得到原函数的单调性, 遇到与导数相关的不等式, 首先去看它在提示哪个函数的单调性(这就是题目给的线索), 再去构造相应的函数,一切便迎刃而解.

## 第 854 题 定积分的几何意义

已知函数 $f(x)=\sin (x-\varphi)$, 且 $\int_{0}^{\frac{2 \pi}{3}} f(x) \mathrm{d} x=0$, 则函数 $f(x)$ 的一条对称轴是
A. $x=\frac{5 \pi}{6}$
B. $x=\frac{7 \pi}{12}$
C. $x=\frac{\pi}{3}$
D. $x=\frac{\pi}{6}$

## 解析 A.

定积分表示曲边梯形的面积 (其中 $x$ 轴上方面积为正, $x$ 轴下方面积为负).

结合三角函数的图象知 $\int_{0}^{\frac{2 x}{3}} f(x) \mathrm{d} x=0$ 时, 有 $\left(\frac{\pi}{3}, 0\right)$ 是 $f(x)$ 的对称中心. 而 $f(x)$ 的周期为 $2 \pi$, 故 $f(x)$的对称轴为直线

$$
x=\frac{\pi}{3}+\frac{\pi}{2}+k \pi=k \pi+\frac{5 \pi}{6}, k \in \mathbf{Z}
$$

## 第 855 题 按部就班

设二次函数 $f(x)=a x^{2}+b x+c$ 的导函数为 $f^{\prime}(x)$, 对任意 $x \in \mathbf{R}$, 不等式 $f(x) \geqslant f^{\prime}(x)$ 恒成立, 则 $\frac{b^{2}}{a^{2}+2 c^{2}}$ 的最大值为

解析 $\sqrt{6}-2$.

由题意知

$$
\forall x \in \mathbf{R}, a x^{2}+(b-2 a) x+c-b \geqslant 0
$$

题中已说明 $f(x)$ 是二次函数, 故 $a \neq 0$,

所以有

$$
a>0, \Delta=(b-2 a)^{2}-4 a(c-b) \leqslant 0,
$$

整理得

$$
a>0, b^{2} \leqslant 4 a c-4 a^{2},
$$

从而有 $c \geqslant a$.

于是

$$
\frac{b^{2}}{a^{2}+2 c^{2}} \leqslant \frac{4 a c-4 a^{2}}{a^{2}+2 c^{2}}=\frac{4\left(\frac{c}{a}-1\right)}{2\left(\frac{c}{a}\right)^{2}+1}
$$

记 $t=\frac{c}{a}-1 \geqslant 0$, 因为考虑最大值,

所以只需要考虑 $t>0$, 有

$$
\frac{b^{2}}{a^{2}+2 c^{2}} \leqslant \frac{4 t}{2(t+1)^{2}+1}=\frac{4}{2 t+\frac{3}{t}+4} \leqslant \sqrt{6}-2
$$

当 $t=\frac{\sqrt{6}}{2}$ 时取到等号.

## 第 856 题 两次调整

已知 $b, c, d \in \mathbf{R}$, 函数 $f(x)=\frac{1}{3} x^{3}+\frac{1}{2} b x^{2}+c x+d$ 在 $(0,1)$ 上既有极大值又有极小值, 则 $c^{2}+(1+b) c$的取值范围是
A. $\left(0, \frac{1}{16}\right)$
B. $\left(0, \frac{1}{16}\right]$
C. $\left(0, \frac{1}{4}\right)$
D. $\left[0, \frac{1}{4}\right)$

解析 A.

事实上, 很容易将原问题转化为: 已知函数 $g(x)=x^{2}+b x+c$ 在区间 $(0,1)$ 上有两个不等实根, 求 $c^{2}+$ $(1+b) c$ 的取值范围.

不难发现

$$
c^{2}+(1+b) c=g(c)=g(0) \cdot g(1)
$$

仔细思考后采用后面的变形方式. 显然 $g(0) \cdot g(1)>0$, 且可以无限趋近于 0 ;

另一方面, 设

$$
g(x)=\left(x-x_{1}\right)\left(x-x_{2}\right)
$$

其中 $x_{1}, x_{2} \in(0,1)$ 且 $x_{1} \neq x_{2}$, 则有

$$
\begin{aligned}
g(0) \cdot g(1) & =x_{1} \cdot x_{2} \cdot\left(1-x_{1}\right) \cdot\left(1-x_{2}\right) \\
& \leqslant\left[\frac{x_{1}+\left(1-x_{1}\right)}{2}\right]^{2} \cdot\left[\frac{x_{2}+\left(1-x_{2}\right)}{2}\right]^{2} \\
& =\frac{1}{16}
\end{aligned}
$$

且 $g(0) \cdot g(1)$ 可以无限趋近于 $\frac{1}{16}$.

综上,正确的答案是 $\mathrm{A}$.

恰当地利用二次方程的根与系数的关系, 利用函数值作为中间桥梁, 可以避开对二次方程系数的范围的研究.

## 第 857 题 $f(x) \cdot \sin x$ 型函数

已知 $a>0$, 函数 $f(x)=\mathrm{e}^{a x} \sin x(x \in[0,+\infty))$, 记 $x_{n}$ 为 $f(x)$ 从小到大的第 $n\left(n \in \mathbf{N}^{*}\right)$ 个极值点.证明:

(1) 数列 $\left\{f\left(x_{n}\right)\right\}$ 是等比数列;

(2) 若 $a \geqslant \frac{1}{\sqrt{\mathrm{e}^{2}-1}}$, 则对一切 $n \in \mathbf{N}^{*}, x_{n}<\left|f\left(x_{n}\right)\right|$ 恒成立.

解析 (1) 根据题意, $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{a x}(a \sin x+\cos x)
$$

于是

$$
a \sin x_{n}+\cos x_{n}=0
$$

解得

$$
x_{n}=n \pi-\arctan \frac{1}{a}, n \in \mathbf{N}^{*}
$$

记 $\varphi=\arctan \frac{1}{a}$, 则

$$
f\left(x_{n}\right)=\mathrm{e}^{\alpha(n \pi-\varphi)} \sin (n \pi-\varphi),
$$

而

$$
\frac{f\left(x_{n+1}\right)}{f\left(x_{n}\right)}=\frac{\mathrm{e}^{a[(n+1) \pi-\varphi]} \sin [(n+1) \pi-\varphi]}{\mathrm{e}^{a(n \pi-\varphi)} \sin (n \pi-\varphi)}=-\mathrm{e}^{a \pi},
$$

因此数列 $\left\{f\left(x_{n}\right)\right\}$ 是公比为 $-\mathrm{e}^{a \pi}$ 的等比数列.

(2) 用分析法, 根据题意

$$
\begin{aligned}
x_{n}<\mid f\left(x_{n}\right) & |\Leftrightarrow n \pi-\varphi<| \mathrm{e}^{a(n \pi-\varphi)} \sin (n \pi-\varphi) \mid \\
& \Leftrightarrow n \pi-\varphi<\mathrm{e}^{a(n \pi-\varphi)} \frac{1}{\sqrt{1+a^{2}}} \\
& \Leftrightarrow \sqrt{1+a^{2}} \cdot(n \pi-\varphi)<\mathrm{e}^{a(n \pi-\varphi)},
\end{aligned}
$$

令 $t=a(n \pi-\varphi)$, 则只需要证明 $\sqrt{1+\frac{1}{a^{2}}} \cdot t<\mathrm{e}^{t}$.

由已知条件有 $\sqrt{1+\frac{1}{a^{2}}} \leqslant \mathrm{e}$, 因此只需要证明当 $t>0$ 时, $\mathrm{e}^{t}>\mathrm{e} \cdot t$.

令 $h(t)=\mathrm{e}^{t}-\mathrm{e} \cdot t, t>0$, 则 $h(t)$ 的导函数

$$
h^{\prime}(t)=\mathrm{e}^{t}-\mathrm{e},
$$

因此函数 $h(t)$ 在 $(0,1)$ 上单调递减, 在 $(1,+\infty)$ 上单调递增, 因此 $h(t) \geqslant h(1)=0$,接下来只需要证明等号无法同时取得.

事实上, 等号同时取得的条件为 $a=\frac{1}{\sqrt{\mathrm{e}^{2}-1}}$ 且 $a\left(n \pi-\arctan \frac{1}{a}\right)=1$, 即

$$
\arctan \sqrt{\mathrm{e}^{2}-1}+\sqrt{\mathrm{e}^{2}-1}=n \pi,
$$

而

$$
\frac{\pi}{3}<\arctan \sqrt{\mathrm{e}^{2}-1}<\frac{\pi}{2}, \frac{2 \pi}{3}<\sqrt{\mathrm{e}^{2}-1}<\frac{3 \pi}{2}
$$

因此

$$
\pi<\arctan \sqrt{\mathrm{e}^{2}-1}+\sqrt{\mathrm{e}^{2}-1}<2 \pi
$$

也即等号无法同时取得.

综上,原命题得证.

$g(x)=f(x) \cdot \sin x$ 类型的函数是一类重要的函数. 一方面有

$$
-|f(x)| \leqslant g(x) \leqslant|f(x)|,
$$

于是函数 $y=g(x)$ 的图象夹在 $y=|f(x)|$ 与 $y=-|f(x)|$ 的图象

之间. 另一方面, 注意到 $g^{\prime}(x)=f(x) \cdot \cos x+f^{\prime}(x) \cdot \sin x$,

## 思考与总结

于是函数 $g(x)$ 的图象与 $y= \pm f(x)$ 的图象相切于 $x=2 k \pi \pm \frac{\pi}{2}, k \in \mathbf{Z}$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-275.jpg?height=297&width=494&top_left_y=2146&top_left_x=1348)

## 第 858 题 遥遥相望

若关于 $x$ 的三次方程 $x^{3}+a x^{2}+b x+c=0$ 有三个不同的实数根 $x_{1}, x_{2}, x_{3}$, 且 $x_{1}<x_{2}<x_{3}, a, b$ 为常数, 当 $c$ 变化时, 求 $x_{3}-x_{1}$ 的取值范围.

解析 设 $f(x)=x^{3}+a x^{2}+b x$,

则 $f(x)$ 的图象跟直线 $y=-c$ 的公共点与原三次方程的根对应.

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=3 x^{2}+2 a x+b,
$$

根据题意, $f(x)$ 有两个极值点, 于是 $a^{2}-3 b>0$, 且极值点为

$$
x=\frac{-a \pm \sqrt{a^{2}-3 b}}{3}
$$

进而可得

$$
\frac{-a-\sqrt{a^{2}-3 b}}{3}<x_{2}<\frac{-a+\sqrt{a^{2}-3 b}}{3},
$$

根据三次方程的韦达定理, 有

$$
x_{1}+x_{2}+x_{3}=-a, x_{1} x_{2}+x_{2} x_{3}+x_{3} x_{1}=b,
$$

于是

$$
\begin{aligned}
x_{3}-x_{1} & =\sqrt{\left(x_{3}+x_{1}\right)^{2}-4 x_{1} x_{3}} \\
& =\sqrt{\left(-a-x_{2}\right)^{2}-4\left[b-\left(-a-x_{2}\right) x_{2}\right]} \\
& =\sqrt{-3 x_{2}^{2}-2 a x_{2}+a^{2}-4 b} \\
& =\sqrt{-3\left(x_{2}+\frac{a}{3}\right)^{2}+a^{2}-4 b+\frac{a^{2}}{3}}
\end{aligned}
$$

结合 $x_{2}$ 的取值范围,可得

$$
0 \leqslant\left(x_{2}+\frac{a}{3}\right)^{2}<\frac{a^{2}-3 b}{9}
$$

进而 $x_{3}-x_{1}$ 的取值范围是 $\left(\sqrt{a^{2}-3 b}, \sqrt{\frac{4\left(a^{2}-3 b\right)}{3}}\right]$.

## 第 859 题 三次函数的性质

```
设关于 \(x\) 的方程 \(x(x-3)^{2}=m\) 有三个不同的实数解 \(a, b, c\), 且 \(a<b<c\), 则下列命题中正确的
是
\( \qquad \)
.
(1) \(a b c\) 的取值范围是 \((0,4) ;\)
(2) \(a^{2}+b^{2}+c^{2}\) 为定值;
(3) \(c-a\) 有最小值, 没有最大值.
```

解析 (1)(2).

(1) 由于函数 $f(x)=x(x-3)^{2}$ 的极大值为 $f(1)=4$, 极小值为 $f(3)=0$, 于是 $m$ 的取值范围是 $(0,4)$.原方程即 $x^{3}-6 x^{2}+9 x-m=0$,
于是根据三次方程的韦达定理有

$$
\left\{\begin{array}{l}
a+b+c=6 \\
a b+b c+c a=9 \\
a b c=m
\end{array}\right.
$$

因此 $a b c$ 的取值范围即 $m$ 的取值范围, 为 $(0,4)$.

(2) $a^{2}+b^{2}+c^{2}=(a+b+c)^{2}-2(a b+b c+c a)=18$ 为定值.

(3)易得 $1<b<3$, 而 $a+c=6-b, a c=9-b(6-b)=b^{2}-6 b+9$,

于是

$$
\begin{aligned}
c-a & =\sqrt{(a+c)^{2}-4 a c} \\
& =\sqrt{(6-b)^{2}-4\left(b^{2}-6 b+9\right)} \\
& =\sqrt{-3 b^{2}+12 b},
\end{aligned}
$$

于是 $c-a$ 的取值范围是 $(3,2 \sqrt{3}]$, 因此 $c-a$ 没有最小值, 有最大值.

## 第 860 题 联动装置

已知 $f(x)=x^{3}-x$, 关于 $x$ 的方程 $f(x)=-\frac{1}{3} t$ 在 $[-1, t]$ 上有且只有一个实根, 则 $t$ 的取值范围是 $\qquad$ .

解析 $\left[-\frac{\sqrt{6}}{3}, 0\right) \cup\left(0, \frac{\sqrt{6}}{3}\right) \cup\left\{\frac{2 \sqrt{3}}{3}\right\}$.

利用直线 $y=-\frac{1}{3} x$ 建立动区间 $[-1, t]$ 和动直线 $y=-\frac{1}{3} t$ 之间的联系, 然后计算临界点, 分段讨论.

如图, 设直线 $y=-\frac{1}{3} x$ 与函数 $f(x)=x^{3}-x$ 的图象交于 $A, O, B$ 三点, 与函数 $y=f(x)$ 的水平切线交于 $M, N$ 两点. 不难计算得 $A\left(-\frac{\sqrt{6}}{3}, \frac{\sqrt{6}}{9}\right)$,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-277.jpg?height=345&width=489&top_left_y=1441&top_left_x=1374)
$B\left(\frac{\sqrt{6}}{3},-\frac{\sqrt{6}}{9}\right), M\left(-\frac{2 \sqrt{3}}{3}, \frac{2 \sqrt{3}}{9}\right), N\left(\frac{2 \sqrt{3}}{3}, \frac{2 \sqrt{3}}{9}\right)$.

利用图象可知:

情形 - 当 $-1<t<-\frac{\sqrt{6}}{3}$ 时, 方程没有实根；

情形二 当 $-\frac{\sqrt{6}}{3} \leqslant t<0$ 时，方程有 1 个实根；

情形三 当 $t=0$ 时, 方程有 2 个实根;

情形四 当 $0<t<\frac{\sqrt{6}}{3}$ 时,方程有 1 个实根；

情形五 当 $\frac{\sqrt{6}}{3} \leqslant t<\frac{2 \sqrt{3}}{3}$ 时, 方程有 2 个实根;

情形六 当 $t=\frac{2 \sqrt{3}}{3}$ 时,方程有 1 个实根;

情形七 当 $t>\frac{2 \sqrt{3}}{3}$ 时, 方程没有实根.
综上所述, $t$ 的取值范围是 $\left[-\frac{\sqrt{6}}{3}, 0\right) \cup\left(0, \frac{\sqrt{6}}{3}\right) \cup\left\{\frac{2 \sqrt{3}}{3}\right\}$.

## 第 861 题 充分条件与必要条件

“对任意 $x \in\left(0, \frac{\pi}{2}\right), k \sin x \cos x<x$ ”是“ $k<1$ ”的
A. 充分而不必要条件
B. 必要而不充分条件
C. 充分必要条件
D. 既不充分也不必要条件

## 解析 B.

记 $p: \forall x \in\left(0, \frac{\pi}{2}\right), k \sin x \cos x<x, q: k<1$, 则 $p$ 等价于

$$
\forall x \in\left(0, \frac{\pi}{2}\right), k \sin 2 x<2 x
$$

我们熟知对任意 $x>0$, 均有 $\sin x<x$, 因此 $k=1$ 符合条件, 但此时并不满足 $k<1$,因此 $p$ 是 $q$ 的不充分条件;

另一方面, 若 $k<1$, 则 $\forall x \in\left(0, \frac{\pi}{2}\right), k \sin 2 x<\sin 2 x<2 x$, 因此 $p$ 是 $q$ 的必要条件;综上, $p$ 是 $q$ 的必要不充分条件. 故选 B.

## 第 862 题 合㑛㳊击

定义在 $\mathbf{R}$ 上的可导函数 $f(x)$ 满足 $(x-314) f(2 x)-2 x f^{\prime}(2 x)>0$ 恒成立, 求证: $\forall x \in \mathbf{R}, f(x)<$ 0.

解析 $\quad$ 题中不等式即

$$
\left(-\frac{1}{2} x+314\right) f(x)+x f^{\prime}(x)<0
$$

对比可知 $a=-\frac{1}{2}, b=314$. 因此

$$
F(x)=\mathrm{e}^{-\frac{1}{2} x} \cdot x^{314} \cdot f(x)
$$

其导函数

$$
F^{\prime}(x)=\mathrm{e}^{-\frac{1}{2} x} \cdot x^{313} \cdot\left[\left(-\frac{1}{2} x+314\right) f(x)+x f^{\prime}(x)\right]
$$

根据题意

$$
\forall x \in \mathbf{R},\left(-\frac{1}{2} x+314\right) f(x)+x f^{\prime}(x)<0
$$

因此 $F(x)$ 在 $(-\infty, 0)$ 上单调递增, 在 $(0,+\infty)$ 上单调递减.

而 $F(0)=0$, 于是

$$
\forall x \in \mathbf{R}^{*}, F(x)<0
$$

即

$$
\forall x \in \mathbf{R}^{*}, f(x)<0
$$

又在题目条件中令 $x=0$ 可得 $f(0)<0$, 补充上述结论可得 $\forall x \in \mathbf{R}, f(x)<0$.

## 第 863 题 构造原函数

若 $f(x)=(x-a)(x-b)+(x-b)(x-c)+(x-c)(x-a)$, 其中 $a \leqslant b \leqslant c$, 对于下列结论:

(1) $f(b) \leqslant 0 ;$

(2)若 $b=\frac{a+c}{2}$, 则 $\forall x \in \mathbf{R}, f(x) \geqslant f(b)$;

(3)若 $b \leqslant \frac{a+c}{2}$, 则 $f(a) \leqslant f(c)$;

(4) $f(a)=f(c)$ 成立的充要条件为 $b=0$.

其中正确的是

解析 (1)(2) (3).

注意到

$$
f(x)=[(x-a)(x-b)(x-c)]^{\prime},
$$

于是 $f(b)$ 即函数

$$
F(x)=(x-a)(x-b)(x-c)
$$

在 $x=b$ 处的切线斜率, 结合三次函数图象的对称性易得. 例如对于(2), 根据三次函数图

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-279.jpg?height=282&width=307&top_left_y=959&top_left_x=1554)

图 1 象的对称性, $(b, 0)$ 为对称中心, 于是命题正确, 如图 1.

再比如对于(2), 根据三次函数图象的对称性, 若 $b<\frac{a+c}{2}$, 则对称中心必然在 $x$ 轴下方. 过对称中心作 $x$轴的平行线, 与三次函数图象交于除对称中心以外的两点, 设这两点的横坐标分别为 $a^{\prime}, c^{\prime}\left(a^{\prime}<c^{\prime}\right)$, 则

$$
F^{\prime}(a)<F^{\prime}\left(a^{\prime}\right)=F^{\prime}\left(c^{\prime}\right)<F^{\prime}(c)
$$

因此命题正确. 如图 2.

综上所述, 正确的结论是(1)(2)(3).

## 第 864 题 慧眼识函数

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-279.jpg?height=287&width=378&top_left_y=1482&top_left_x=1483)

图 2

已知 $f(x)$ 是定义在 $\mathbf{R}$ 上的可导函数, 且对任意的 $x>2$, 均有 $f(x)+2 f^{\prime}(x)<x f^{\prime}(x)$, 设 $a=$ $f(3), b=\frac{1}{2} f(4), c=(\sqrt{5}+2) f(\sqrt{5})$, 则 $a, b, c$ 从小到大的排列为

解析 $c, a, b$.

根据题意, 有

$$
\forall x>2, \frac{(x-2) f^{\prime}(x)-f(x)}{(x-2)^{2}}>0
$$

即在区间 $(2,+\infty)$ 上, 有函数 $g(x)=\frac{f(x)}{x-2}$ 的导函数 $g^{\prime}(x)>0$,

因此函数 $g(x)$ 在 $(2,+\infty)$ 上单调递增.

又 $a=g(3), b=g(4), c=g(\sqrt{5})$, 而 $\sqrt{5}<3<4$, 因此 $c<a<b$,

故正确的答案是 $c, a, b$.

## 第 865 题 有何“璇玑”

已知函数 $f(x)=x^{3}+a x+\frac{1}{4}, g(x)=-\ln x$.

(1) 当 $a$ 为何值时, $x$ 轴为曲线 $y=f(x)$ 的切线;

(2) 用 $\min \{m, n\}$ 表示 $m, n$ 中的最小值, 设函数 $h(x)=\min \{f(x), g(x)\}(x>0)$, 讨论 $h(x)$ 零点的个数.

解析 (1) 根据已知, $f^{\prime}(x)=3 x^{2}+a$.

若 $x$ 轴为曲线 $y=f(x)$ 的切线, 设切点横坐标为 $t$, 则有

$$
\left\{\begin{array}{l}
f(t)=0 \\
f^{\prime}(t)=0
\end{array}\right.
$$

即

$$
\left\{\begin{array}{l}
t^{3}+a t+\frac{1}{4}=0 \\
3 t^{2}+a=0
\end{array}\right.
$$

解得

$$
t=\frac{1}{2}, a=-\frac{3}{4}
$$

所以当 $a$ 的值为 $-\frac{3}{4}$ 时, $x$ 轴为曲线 $y=f(x)$ 的切线.

(2) 先分析 $f(x)$ 在 $(0,1)$ 上的零点个数, 这些零点均为函数 $h(x)$ 的零点.

由于方程 $x^{3}+a x+\frac{1}{4}=0$ 即

$$
-a=x^{2}+\frac{1}{4 x}
$$

因此 $f(x)$ 在 $(0,1)$ 上的零点个数即直线 $y=-a$ 与函数 $\varphi(x)=x^{2}+\frac{1}{4 x}(0<x<1)$ 图象的交点个数.

函数 $\varphi(x)$ 的导函数

$$
\varphi^{\prime}(x)=\frac{8 x^{3}-1}{4 x^{2}},
$$

因此 $\varphi(x)$ 在 $\left(0, \frac{1}{2}\right)$ 上单调递减, 在 $x=\frac{1}{2}$ 处取得极小值 $\frac{3}{4}$, 在 $\left(\frac{1}{2}, 1\right)$ 上单调递增, 如图.

因此函数 $f(x)$ 在 $(0,1)$ 上的零点个数是

$$
\left\{\begin{array}{l}
0,-a<\frac{3}{4}, \\
1,-a \geqslant \frac{5}{4} \text { 或 }-a=\frac{3}{4}, \\
2, \frac{3}{4}<-a<\frac{5}{4},
\end{array}\right.
$$

即

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-280.jpg?height=350&width=286&top_left_y=2001&top_left_x=1479)

$$
\left\{\begin{array}{l}
0, a>-\frac{3}{4}, \\
1, a \leqslant-\frac{5}{4} \text { 或 } a=-\frac{3}{4}, \\
2,-\frac{5}{4}<a<-\frac{3}{4},
\end{array}\right.
$$

接下来分析 $x=1$ 是否为函数 $h(x)$ 的零点.

由于 $f(1)=a+\frac{5}{4}$, 于是当 $a \geqslant-\frac{5}{4}$ 时, $x=1$ 是函数 $h(x)$ 的零点; 当 $a<-\frac{5}{4}$ 时, $x=1$ 不是函数 $h(x)$ 的零点.

综上, 函数 $h(x)$ 的零点个数为

$$
\left\{\begin{array}{l}
1, a<-\frac{5}{4} \text { 或 } a>-\frac{3}{4} ， \\
2, a=-\frac{5}{4} \text { 或 } a=-\frac{3}{4} ， \\
3,-\frac{5}{4}<a<-\frac{3}{4} .
\end{array}\right.
$$

## 第 866 题 换元法处理多参数问题

已知正数 $a, b, c$ 满足: $5 c-3 a \leqslant b \leqslant 4 c-a, c \ln b \geqslant a+c \ln c$, 则 $\frac{b}{a}$ 的取值范围是

解析 $[\mathrm{e}, 7]$.

题目条件中的不等式含有三个参数, 其中不等式 $5 c-3 a \leqslant b \leqslant 4 c-a$ 为齐次式, 而不等式 $c \ln b \geqslant a+c \ln c$可以转化成 $\ln \frac{b}{c} \geqslant \frac{a}{c}$,

于是我们令 $x=\frac{a}{c}, y=\frac{b}{c}$, 将条件转化为

$$
\left\{\begin{array}{l}
x+y \leqslant 4 \\
3 x+y \geqslant 5 \\
y \geqslant \mathrm{e}^{x}
\end{array}\right.
$$

它表示的平面区域如图.

因为目标函数 $\frac{b}{a}=\frac{y}{x}$ 为可行域中一点与原点连线的斜率，

所以点 $A\left(\frac{1}{2}, \frac{7}{2}\right)$ 对应目标函数的最大值 7 .

下面考虑目标函数的最小值:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-281.jpg?height=457&width=378&top_left_y=1709&top_left_x=1483)

容易求出过原点且与 $y=\mathrm{e}^{x}$ 相切的直线为 $y=\mathrm{e} x$, 切点坐标为 $M(1, \mathrm{e})$, 而点 $M$ 在可行域内, 且有 $\mathrm{e}^{x} \geqslant$ $\mathrm{e} x$, 故 $\frac{y}{x}$ 的最小值为 $\mathrm{e}$.

从而知所求的取值范围为 $[e, 7]$.

多参数问题具有某种对称性时, 常考虑用换元法将题目的条件与结论转化成更容易处理的形式.

## 第 867 题 按部就班

讨论函数 $f(x)=x^{2}+2(1-a) x-4 a$ 与函数 $g(x)=\frac{1}{x}-(a+1)^{2}$ 的图象的公切线条数.

解析 函数 $f(x)$ 的导函数为 $f^{\prime}(x)=2 x+2(1-a)$, 函数 $g(x)$ 的导函数 $g^{\prime}(x)=-\frac{1}{x^{2}}$,

设公切线在 $f(x)$ 和 $g(x)$ 图象上的切点横坐标分别为 $m, \frac{1}{n}(n \neq 0)$, 则切线方程为

$$
y=[2 m+2(1-a)](x-m)+m^{2}+2(1-a) m-4 a,
$$

同时亦为

$$
y=-n^{2}\left(x-\frac{1}{n}\right)+n-(a+1)^{2},
$$

因此有

$$
\left\{\begin{array}{l}
2 m+2-2 a=-n^{2}, \\
-m^{2}-4 a=2 n-(a+1)^{2},
\end{array}\right.
$$

即

$$
\left\{\begin{array}{l}
n^{2}+2 m=2(a-1) \\
m^{2}+2 n=(a-1)^{2}
\end{array}\right.
$$

且每一组解 $(m, n)$ 对应一条公切线.

由第一个等式可得

$$
m=-\frac{1}{2} n^{2}+(a-1)
$$

代人第二个等式并整理得

$$
a-1=\frac{1}{4} n^{2}+\frac{2}{n}
$$

设 $h(x)=\frac{1}{4} x^{2}+\frac{2}{x}$, 则其导函数

$$
h^{\prime}(x)=\frac{x^{3}-4}{2 x^{2}}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-282.jpg?height=361&width=295&top_left_y=1510&top_left_x=1456)

于是函数 $h(x)$ 在 $(-\infty, 0)$ 上单调递减, 在 $(0, \sqrt[3]{4})$ 上单调递减, 在 $(\sqrt[3]{4},+\infty)$ 上单调递增, 如图.

因此当 $a<1+\frac{3}{4^{\frac{1}{3}}}$ 时, 只有 1 条公切线; 当 $a=1+\frac{3}{4^{\frac{1}{3}}}$ 时, 有 2 条公切线; 当 $a>1+\frac{3}{4^{\frac{1}{3}}}$ 时, 有 3 条公切线.

思考与总结

解决切线问题的关键在于抓住切点列出方程 (组).

## 第 868 题 你切我切一起切

已知函数 $f(x)=m \ln x$ 与函数 $h(x)=\frac{x-1}{2 x}(x>0)$ 的图象有且只有一条公切线, 求实数 $m$ 的值.

解析 解法一 由于函数 $f(x), g(x)$ 的导函数分别为

$$
f^{\prime}(x)=\frac{m}{x}, g^{\prime}(x)=\frac{1}{2 x^{2}}
$$

设公切线与函数 $f(x)$, 函数 $g(x)$ 的图象分别相切于点 $(a, m \ln a)$ 与 $\left(b, \frac{1}{2}-\frac{1}{2 b}\right)$, 则

$$
\left\{\begin{array}{l}
\frac{m}{a}=\frac{1}{2 b^{2}} \\
-\frac{m}{a} \cdot a+m \ln a=-\frac{1}{2 b^{2}} \cdot b+\frac{1}{2}-\frac{1}{2 b}
\end{array}\right.
$$

从而 $b=\sqrt{\frac{a}{2 m}}$, 且

$$
-m+m \ln a=\frac{1}{2}-\sqrt{\frac{2 m}{a}},
$$

即

$$
(\ln a-1) m+\sqrt{\frac{2}{a}} \cdot \sqrt{m}-\frac{1}{2}=0
$$

于是

$$
\sqrt{m}= \begin{cases}\sqrt{\frac{\mathrm{e}}{8}} & a=\mathrm{e} \\ \frac{-\sqrt{\frac{2}{a}}+\sqrt{\frac{2}{a}+2 \ln a-2}}{2(\ln a-1)}, & a \neq \mathrm{e}\end{cases}
$$

即

$$
\frac{1}{\sqrt{2 m}}=x+\sqrt{x^{2}-2 \ln x-1}
$$

其中 $x=\sqrt{\frac{1}{a}}$. 记上述等式右边为 $\varphi(x)$, 对 $\varphi(x)$ 求导得

$$
\varphi^{\prime}(x)=1+\frac{x-\frac{1}{x}}{\sqrt{x^{2}-2 \ln x-1}}
$$

可以证明当 $x \in(0,1)$ 时, $\varphi^{\prime}(x)<0$; 当 $x \in(1,+\infty)$ 时, $\varphi^{\prime}(x)>0$ (可以利用 $\ln t$ 与 $1-\frac{1}{t}$ 的大小关系得到 $\ln x^{2}$ 与 $1-\frac{1}{x^{2}}$ 的大小关系, 从而得到结论).

从而有 $\varphi(x)$ 在 $(0,1)$ 上单调递减, 在 $(1,+\infty)$ 上单调递增.

当 $x=1$ 时, $\varphi(x)$ 取得最小值 $\varphi(1)=1$.

因此当 $m=\frac{1}{2}$ 时, 符合题意.

综上所述, 实数 $m$ 的值为 $\frac{1}{2}$, 对应的公切线方程为 $y=\frac{1}{2} x-\frac{1}{2}$.
解法二 $f(x)$ 在点 $(a, m \ln a)$ 处的切线为

$$
y=\frac{m}{a}(x-a)+m \ln a .
$$

而 $h(x)$ 在点 $\left(b, \frac{1}{2}-\frac{1}{2 b}\right)$ 处的切线为

$$
y=\frac{1}{2 b^{2}}(x-b)+\frac{1}{2}-\frac{1}{2 b}
$$

由这两条切线重合知

$$
\left\{\begin{array}{l}
\frac{m}{a}=\frac{1}{2 b^{2}} \\
-m+m \ln a=-\frac{1}{b}+\frac{1}{2}
\end{array}\right.
$$

问题即当 $m$ 在什么范围内时, 关于 $(a, b)$ 的方程有唯一一组解.

因为 $a$ 与 $b$ 的值一一对应, 如果在方程组中消去 $b$, 得到

$$
m \ln a+\sqrt{\frac{2 m}{a}}-m-\frac{1}{2}=0
$$

此方程组对 $a>0$ 有唯一解, 不好计算;

如果在方程组中消去 $a$, 得到

$$
m \ln (2 m)-m+2 m \ln b+\frac{1}{b}-\frac{1}{2}=0
$$

对 $b>0$ 有唯一解, 记左边为 $g(b)$, 则有

$$
g^{\prime}(b)=\frac{2 m b-1}{b^{2}}
$$

方程组有解时有 $m>0$, 所以 $g(b)$ 在 $\left(0, \frac{1}{2 m}\right)$ 上单调递减, 在 $\left(\frac{1}{2 m},+\infty\right)$ 上单调递增,

所以

$$
g(b)_{\min }=g\left(\frac{1}{2 m}\right)=m-\frac{1}{2}-m \ln (2 m),
$$

而当 $b \rightarrow 0$ 与 $b \rightarrow+\infty$ 时, 均有 $g(b) \rightarrow+\infty$, 所以当且仅当这个最小值等于 0 时方程 $g(b)=0$ 有唯一解.

最后解方程

$$
m-\frac{1}{2}-m \ln (2 m)=0,
$$

显然 $m=\frac{1}{2}$ 是它的解, 考虑

$$
h(m)=m-\frac{1}{2}-m \ln (2 m)
$$

有

$$
h^{\prime}(m)=-\ln (2 m),
$$

所以 $h(m)$ 在 $\left(0, \frac{1}{2}\right)$ 上单调递增, 在 $\left(\frac{1}{2},+\infty\right)$ 上单调递减,

所以 $\frac{1}{2}$ 是 $h(m)=0$ 的唯一解, 所以 $m=\frac{1}{2}$.

## 第 869 题从切线含义出发

已知不等式 $\ln (x+1)-1 \leqslant a x+b$ 对一切 $x>-1$ 都成立, 则 $\frac{b}{a}$ 的最小值是
解析 $1-\mathrm{e}$.

考虑不等式两边分别对应有函数 $f(x)=\ln (x+1)-1$ 与 $g(x)=a x+b$, 其中 $g(x)$ 的图象是一条直线, 且横截距为 $-\frac{b}{a}$,

所以求出当函数 $f(x)$ 的图象在直线 $g(x)$ 下方 (或 $g(x)$ 上方) 时, 直线的横截距的最大值即可.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-285.jpg?height=265&width=422&top_left_y=256&top_left_x=1457)

函数 $f(x)$ 的图象如图.

容易看出横截距的最大值为 $\mathrm{e}-1$, 所以 $\frac{b}{a}$ 的最小值为 $1-\mathrm{e}$.

严格的书写可以在不等式中令 $x=\mathrm{e}-1$, 于是题中不等式为

$$
a\left(\mathrm{e}-1+\frac{b}{a}\right) \geqslant 0
$$

不等式恒成立必有 $a>0$, 从而得到 $\frac{b}{a} \geqslant 1-\mathrm{e}$, 再去验证当 $\frac{b}{a}=1-\mathrm{e}$ 时, 不等式恒成立.

也可以直接取 $f(x)$ 在 $x=\mathrm{e}-1$ 处的切线, 结合对数函数的凹凸性知

$$
\ln (x+1)-1 \leqslant\left.[\ln (x+1)-1]^{\prime}\right|_{x=\mathrm{e}-1} \cdot[x-(\mathrm{e}-1)]=\frac{1}{\mathrm{e}}(x-\mathrm{e}+1)
$$

等号在 $x=\mathrm{e}-1$ 时可取到, 从而得到 $\frac{b}{a}$ 的最小值为 $1-\mathrm{e}$.

## 第 870 题 存在性问题的证明

已知函数 $f(x)=\mathrm{e}^{a x}-x$.

(1) 若曲线 $y=f(x)$ 在点 $(0, f(0))$ 处的切线 $l$ 与直线 $x+2 y+3=0$ 垂直, 求 $a$ 的值;

(2) 当 $a \neq 1$ 时,求证:存在实数 $x_{0}$ 使 $f\left(x_{0}\right)<1$.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=a \mathrm{e}^{a x}-1,
$$

于是

$$
f^{\prime}(0)=a-1=2
$$

因此 $a=3$.

(2) 情形 $-a \leqslant 0$. 此时取 $x_{0}=1$, 则有

$$
f\left(x_{0}\right)=\mathrm{e}^{a}-1<0<1,
$$

命题成立.

情形二 $a>0$ 且 $a \neq 1$. 此时命题等价于对于实数 $a>0$ 且 $a \neq 1$,

$$
\exists x \in \mathbf{R}, \mathrm{e}^{x}<\frac{1}{a} x+1
$$

考虑函数 $g(x)=\left(\frac{1}{a} x+1\right) \mathrm{e}^{-x}$, 则其导函数

$$
g^{\prime}(x)=\frac{1}{a}(1-a-x) \mathrm{e}^{-x}
$$

因此函数 $g(x)$ 的极大值, 亦为最大值

$$
g(1-a)=\frac{1}{a} \mathrm{e}^{a-1}=\frac{\mathrm{e}^{a}}{\mathrm{e} a}>1
$$

因此命题成立.

综上所述, 原命题得证.

## 思考与总结

情形二的另 一 种证明方法: 当 $a>0$ 时, $f^{\prime}(x)=a \mathrm{e}^{a x}-1$ 单调递增, 且 $f^{\prime}(0)=a-1$.

若 $a \in(0,1)$, 记 $f^{\prime}(x)$ 的唯一零点为 $m$, 因为 $f^{\prime}(0)<0=f^{\prime}(m) \Rightarrow m>0$, 在区间 $(0, m)$ 上 $f^{\prime}(x)<0$, 所以 $f(x)$ 单调递减, 而 $f(0)=1$, 所以 $f(x)<1$;

若 $a \in(1,+\infty)$, 则 $f^{\prime}(0)>0=f^{\prime}(m)$, 所以 $m<0$, 从而在区间 $(m, 0)$ 上有 $f^{\prime}(x)>0, f(x)$ 单调递增,所以 $f(x)<f(0)=1$.

综上知 $a \neq 1$ 时, 均存在实数 $x_{0}$, 使得 $f\left(x_{0}\right)<1$.

## 第 871 题 火眼金睛识原型

已知函数 $f(x)$ 满足 $x^{2} f^{\prime}(x)+2 x f(x)=\frac{\mathrm{e}^{x}}{x}, f(2)=\frac{\mathrm{e}^{2}}{8}$, 则 $x>0$ 时, $f(x)$
A. 有极大值, 无极小值
B. 有极小值, 无极大值
C. 既有极大值, 又有极小值
D. 既无极大值, 又无极小值

## 解析 D.

在已知条件中令 $x=2$, 可得 $f^{\prime}(2)=0$. 注意到

$$
\left(x^{2} f(x)\right)^{\prime}=x^{2} f^{\prime}(x)+2 x f(x)=\frac{\mathrm{e}^{x}}{x}
$$

于是由题中条件, 有

$$
x^{2} f^{\prime}(x)=\frac{\mathrm{e}^{x}}{x}-2 x f(x)
$$

进而

$$
x^{3} f^{\prime}(x)=\mathrm{e}^{x}-2 x^{2} f(x)
$$

两边求导可得

$$
\left(x^{3} f^{\prime}(x)\right)^{\prime}=\mathrm{e}^{x}-2 \cdot \frac{\mathrm{e}^{x}}{x}=\mathrm{e}^{x} \cdot \frac{x-2}{x},
$$

于是函数 $y=x^{3} f^{\prime}(x)$ 在 $(0,2)$ 上单调递减, 在 $(2,+\infty)$ 上单调递增.

结合该函数在 $x=2$ 处的函数值为 0 , 可得 $y=x^{3} f^{\prime}(x)$ 在 $(0,+\infty)$ 上没有变号零点,

于是 $y=f^{\prime}(x)$ 在 $(0,+\infty)$ 上也没有变号零点, 进而 $y=f(x)$ 在 $x>0$ 时既无极大值, 又无极小值, 选 D.

## 思考与总结

解决问题的关键在于合理利用条件得到关于 $f^{\prime}(x)$ 的单调性的信息, 进而对其零点作出判断.

## 第 872 题 合理消参

已知 $a$ 为常数, $f(x)=x(\ln x-a x)$ 有两个极值点 $x_{1}, x_{2}\left(x_{1}<x_{2}\right)$, 则
A. $f\left(x_{1}\right)>0, f\left(x_{2}\right)>-\frac{1}{2}$
B. $f\left(x_{1}\right)<0, f\left(x_{2}\right)<-\frac{1}{2}$
C. $f\left(x_{1}\right)>0, f\left(x_{2}\right)<-\frac{1}{2}$
D. $f\left(x_{1}\right)<0, f\left(x_{2}\right)>-\frac{1}{2}$

解析 D.

首先计算 $f^{\prime}(x)=\ln x-2 a x+1$, 设导函数的零点为 $x=t$, 则

$$
\ln t=2 a t-1
$$

我们熟知函数 $y=\ln x$ 在点 $(1,0)$ 处的切线为 $y=x-1$, 于是可知 $0<2 a<1$ 且 $0<$ $x_{1}<1<x_{2}$, 如图 1.

为了消去参数 $a$, 将 $a=\frac{\ln t+1}{2 t}$ 代人函数解析式中可得极值为 $\frac{1}{2} t \ln t-\frac{1}{2} t$, 记该函

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-287.jpg?height=309&width=330&top_left_y=736&top_left_x=1545)

图 1 数为 $\varphi(t)$, 注意到其导函数

$$
\varphi^{\prime}(t)=\frac{1}{2} \ln t
$$

于是其图象如图 2.

由此不难得到 $-\frac{1}{2}<f\left(x_{1}\right)<0$ 且 $-\frac{1}{2}<f\left(x_{2}\right)$, 选 D.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-287.jpg?height=199&width=434&top_left_y=1113&top_left_x=1444)

图 2

先利用半分离变量得到函数 $f(x)$ 的导函数 $f^{\prime}(x)$ 的零点分布情况, 然后消去参数计算极值的分布.

## 第 873 题 统一变量

已知函数 $f(x)=x^{2}+a \ln (x+1)$ 有两个相异极值点 $x_{1}, x_{2}$, 且 $x_{1}<x_{2}$, 求证: $0<\frac{f\left(x_{2}\right)}{x_{1}}<-\frac{1}{2}+$ $\ln 2$.

解析 根据已知,函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=2 x+\frac{a}{x+1}=\frac{1}{x+1} \cdot\left(2 x^{2}+2 x+a\right),
$$

由题意 $f(x)$ 有两个极值点, 于是

$$
\left\{\begin{array}{l}
\left.\left(2 x^{2}+2 x+a\right)\right|_{x=-1}>0 \\
\Delta=4-8 a>0
\end{array}\right.
$$

解得

$$
0<a<\frac{1}{2}
$$

由事达定理得

$$
x_{1}+x_{2}=-1, x_{1} x_{2}=\frac{a}{2}
$$

于是可以将 $\frac{f\left(x_{2}\right)}{x_{1}}$ 化为单一变量的函数. 为了避免出现根号, 可以选 $x_{2}$ 为变量, 即利用代换

$$
x_{1}=-1-x_{2}, a=2\left(-1-x_{2}\right) x_{2},
$$

得

$$
\frac{f\left(x_{2}\right)}{x_{1}}=-\frac{x_{2}^{2}}{1+x_{2}}+2 x_{2} \ln \left(x_{2}+1\right)
$$

并记右边关于 $x_{2}$ 的函数为 $g\left(x_{2}\right)$, 其中 $x_{2}=\frac{-1+\sqrt{1-2 a}}{2}$, 取值范围是 $\left(-\frac{1}{2}, 0\right)$.

不难注意到欲证明不等式即

$$
g(0)<g\left(x_{2}\right)<g\left(-\frac{1}{2}\right)
$$

因此我们只需要证明 $g\left(x_{2}\right)$ 在 $\left[-\frac{1}{2}, 0\right]$ 上单调递减.

事实上, 函数 $g\left(x_{2}\right)$ 的导函数

$$
\begin{aligned}
g\left(x_{2}\right)^{\prime} & =2 \ln \left(1+x_{2}\right)+\frac{x_{2}^{2}}{\left(1+x_{2}\right)^{2}} \\
& <2 x_{2}+\frac{x_{2}^{2}}{\left(1+x_{2}\right)^{2}} \\
& =\frac{x_{2}\left(2 x_{2}+1\right)\left(x_{2}+2\right)}{\left(1+x_{2}\right)^{2}} \\
& <0
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-288.jpg?height=383&width=812&top_left_y=826&top_left_x=934)

于是命题得证.

## 第 874 题 零点分段讨论与分析端点

设函数 $f(x)=\ln (x+1)+a\left(x^{2}-x\right)$, 其中 $a \in \mathbf{R}$.

(1) 讨论函数 $f(x)$ 的极值点个数, 并说明理由;

(2) 若 $\forall x>0, f(x) \geqslant 0$ 成立, 求 $a$ 的取值范围.

解析 (1) 根据题意, $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{1}{x+1} \cdot\left(2 a x^{2}+a x-a+1\right)
$$

记其中决定 $f^{\prime}(x)$ 符号的部分为

$$
h(x)=2 a x^{2}+a x-a+1
$$

考虑到二次项系数为 $2 a$,于是 $a=0$ 是一个讨论点;

而对称轴为 $x=-\frac{1}{4}$, 因此需要考虑判别式

$$
\Delta=a^{2}-4 \cdot 2 a \cdot(-a+1)=a(9 a-8),
$$

因此 $a=\frac{8}{9}$ 也是一个讨论点.

于是可以根据这些讨论点进行讨论, $h(x)$ 在每个讨论区间上的图象如图所示.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-288.jpg?height=246&width=1086&top_left_y=2316&top_left_x=365)

## 高考数学满分学霸的解题笔记(一千零一题)

于是不难得到:

当 $a<0$ 时, 函数 $f(x)$ 的极值点个数为 1 , 为极大值点;

当 $0 \leqslant a \leqslant \frac{8}{9}$ 时, 函数 $f(x)$ 的极值点个数为 0 ;

当 $a>\frac{8}{9}$ 时, 函数 $f(x)$ 的极值点个数为 2 , 其中有一个极大值点和一个极小值点.

(2) 按 $a$ 和 0,1 的大小关系展开讨论, 讨论中默认 $x>0$.

情形一 $a<0$.

令 $g(x)=\ln (x+1)-x$, 则 $g(x)$ 的导函数 $g^{\prime}(x)=\frac{1}{x+1}-1<0$, 因此 $g(x)$ 单调递减, 于是 $g(x)<g(0)$ $=0$.

因此 $f(x)<x+a\left(x^{2}-x\right)=x(a x+1-a)$, 取 $x=\frac{1-a}{-a}$, 则 $f(x)<0$, 不符合题意.

情形ニ $0 \leqslant a \leqslant 1$.

此时 $f^{\prime}(x)>0$, 因此 $f(x)$ 单调递增, 于是 $f(x)>f(0)=0$, 符合题意.

情形三 $a>1$.

此时在区间 $\left(0, \frac{-a+\sqrt{a^{2}+8 a(a-1)}}{4 a}\right)$ 上有 $f^{\prime}(x)<0$, 因此在该区间内 $f(x)$ 单调递减, 此时 $f(x)<$ $f(0)=0$, 不符合题意.

综上, $a$ 的取值范围是 $[0,1]$.

## 第 875 题 $\quad$ 明察秋毫

已知 $f(x)$ 为可导函数, $f^{\prime}(x)$ 为 $f(x)$ 的导函数, $f\left(\frac{1}{2}\right)=\ln 2-\frac{1}{2}$, 且

$$
x f^{\prime}(x)-f(x)=\frac{4 x^{2} \ln x}{4 x+\frac{1}{2 \ln 2-1}-1}
$$

则 $f(x)$
A. 有极大值, 无极小值
B. 有极小值, 无极大值
C. 既有极大值又有极小值
D. 既无极大值也无极小值

## 解析 D.

记 $\frac{1}{2 \ln 2-1}-1=m$, 则 $f\left(\frac{1}{2}\right)=\frac{1}{2(m+1)}$, 而

$$
x f^{\prime}(x)-f(x)=\frac{4 x^{2} \ln x}{4 x+m}
$$

问题本质是研究 $f^{\prime}(x)$ 的零点情况, 于是设法获得关于 $f^{\prime}(x)$ 以及其导函数 $f^{\prime \prime}(x)$ 的信息为第一要义.根据已知条件的结构, 我们可以察觉出其中有破绽 $\frac{f(x)}{x}$, 寻此破绽设法消去 $f(x)$ 就是解题的关键.首先, 两边同时除以 $x^{2}$, 有

$$
\left(\frac{f(x)}{x}\right)^{\prime}=\frac{4 \ln x}{4 x+m}
$$

进而移项整理得

$$
f^{\prime}(x)=\frac{f(x)}{x}+\frac{4 x \ln x}{4 x+m}
$$

两边求导, 可得

$$
f^{\prime \prime}(x)=\left(\frac{f(x)}{x}\right)^{\prime}+\frac{16 x+4 m(1+\ln x)}{(4 x+m)^{2}}
$$

将(1)代人,有

$$
f^{\prime \prime}(x)=\frac{4 \ln x}{4 x+m}+\frac{16 x+4 m(1+\ln x)}{(4 x+m)^{2}}
$$

整理得

$$
f^{\prime \prime}(x)=4(4 x+2 m) \cdot \frac{\ln x+1-\frac{m}{4 x+2 m}}{(4 x+m)^{2}}
$$

设(2)中分子部分为 $\varphi(x)$, 注意到 $\varphi\left(\frac{1}{2}\right)=0$ 且 $\varphi(x)$ 单调递增.

由 $\varphi(x)$ 的性质可得 $f^{\prime \prime}(x)$ 在 $\left(0, \frac{1}{2}\right)$ 上小于零, 在 $\left(\frac{1}{2},+\infty\right)$ 上大于零;

所以 $f^{\prime}(x)$ 在 $\left(0, \frac{1}{2}\right)$ 上单调递减, 在 $\left(\frac{1}{2},+\infty\right)$ 上单调递增,

又 $f^{\prime}\left(\frac{1}{2}\right)=0$, 于是 $f^{\prime}(x)$ 在 $(0,+\infty)$ 上非负；

进而可得函数 $f(x)$ 无极值点, 答案 D 正确.

## 第 876 题桥澡函数

已知函数 $f(x)=\frac{x-1}{\mathrm{e}^{x}}$.

(1) 求函数 $f(x)$ 的单调区间和极值;

(2) 若 $x_{1} \neq x_{2}$, 且 $f\left(x_{1}\right)=f\left(x_{2}\right)$, 求证: $x_{1}+x_{2}>4$.

解析 $(1)$ 对 $f(x)$ 求导得

$$
f^{\prime}(x)=\frac{2-x}{\mathrm{e}^{x}}
$$

所以 $f(x)$ 在 $(-\infty, 2)$ 上单调递增, 在 $(2,+\infty)$ 上单调递减, 有极大值 $f(2)=\mathrm{e}^{-2}$, 无极小值.

(2)我们知道对于二次函数来说, 如果两个自变量对应函数值相等, 那么这两个自变量的和为定值, 这是由二次函数的对称性与单调性决定的. 本题中函数的单调性与二次函数类似, 我们先从直观上理解一下第 (2) 题结论的含义:

由 (1)知, 在函数 $f(x)$ 的图象上, $x=2$ 相当于“山顶”, 在 $x=2$ 的两侧, 函数图象的“陡峭程度”是不同的 (因为分母 $\mathrm{e}^{x}$ 对应的值不同), 左侧更陡峭, 右侧更平缓, 所以这两侧对应的点如果在同一“海拔”上, 则右侧的点离“山顶”的“水平”距离更远, 好像两条下山的路, 更平缓的路更远一样.

要严格证明这个问题,我们可以将 $x=2$ 左侧的图象对称到右侧去,比较对称过去的函数与原来函数的大小关系得到结果. 函数 $f(x)$ 的草图如图.

令

$$
h(x)=f(4-x), x \geqslant 2
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-290.jpg?height=349&width=485&top_left_y=2247&top_left_x=1279)

$$
F(x)=f(x)-h(x)=\frac{x-1}{\mathrm{e}^{x}}-\frac{3-x}{\mathrm{e}^{4-x}}, x \geqslant 2,
$$

则

$$
F^{\prime}(x)=(2-x)\left(\mathrm{e}^{-x}-\mathrm{e}^{x-4}\right) \geqslant 0,
$$

所以 $F(x)$ 在 $[2,+\infty)$ 上单调递增, 而 $F(2)=0$, 所以 $F(x) \geqslant 0$, 即

$$
f(x)>h(x)=f(4-x)
$$

不妨设 $x_{1}<x_{2}$, 则有 $x_{1}<2<x_{2}$, 于是

$$
f\left(x_{2}\right)=f\left(x_{1}\right)=h\left(4-x_{1}\right)<f\left(4-x_{1}\right),
$$

而 $f(x)$ 在 $(2,+\infty)$ 上单调递减, 所以 $x_{2}>4-x_{1}$, 即 $x_{1}+x_{2}>4$.

'思考与总结

本题通过“桥梁” $h(x)$ 将不在同一个单调区间的自变量转移到同一个单调区间中, 从而可以通过函数值的大小关系得到自变量的大小关系,这个思路也是解决此类问题的常用思路.

## 第 877 题带发修行

已知函数 $f(x)=a \ln x-\frac{1}{2} x^{2}+b x$ 存在极小值, 且对于 $b$ 的所有可能取值, $f(x)$ 的极小值恒大于 0 ,则 $a$ 的最小值为 $\qquad$ .

## 解析 $-\mathrm{e}^{3}$.

根据题意, $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{-x^{2}+b x+a}{x}
$$

设函数 $f(x)$ 的极小值点为 $x=m$, 则 $-m^{2}+b m+a=0$, 且 $0<m<\sqrt{-a}$.

于是 $f(x)$ 的极小值

$$
\varphi(m)=a \ln m-\frac{1}{2} m^{2}+b m=a \ln m+\frac{1}{2} m^{2}-a,
$$

而 $\varphi(m)$ 的导函数

$$
\varphi^{\prime}(m)=\frac{a}{m}+m<0
$$

于是 $\varphi(m)$ 满足

$$
\varphi(\sqrt{-a})=a \ln \sqrt{-a}-\frac{3}{2} a \geqslant 0
$$

解得 $a \geqslant-\mathrm{e}^{3}$, 因此 $a$ 的最小值为 $-\mathrm{e}^{3}$.

## 第 878 题 极值的范围估计

已知函数 $f(x)=x^{2}-2 x+1+a \ln x$ 有两个极值点 $x_{1}, x_{2}$, 且 $x_{1}<x_{2}$, 则
A. $f\left(x_{2}\right)<-\frac{1+2 \ln 2}{4}$
B. $f\left(x_{2}\right)<\frac{1-2 \ln 2}{4}$
C. $f\left(x_{2}\right)>\frac{1+2 \ln 2}{4}$
D. $f\left(x_{2}\right)>\frac{1-2 \ln 2}{4}$
解析 D.

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{2 x^{2}-2 x+a}{x}
$$

根据题意, 可得当 $a<\frac{1}{2}$ 时, 函数 $f(x)$ 有两个极值点, 且 $x_{1}<\frac{1}{2}<x_{2}, x_{2}$ 的取值范围是 $\left(\frac{1}{2}, 1\right)$. 进而可得极大值

$$
M=f\left(x_{2}\right)=x_{2}^{2}-2 x_{2}+1+\left(2 x_{2}-2 x_{2}^{2}\right) \ln x_{2},
$$

令 $g(t)=t^{2}-2 t+1+\left(2 t-2 t^{2}\right) \ln t, t \in\left[\frac{1}{2}, 1\right]$, 则

$$
g^{\prime}(t)=2(1-2 t) \ln t \geqslant 0
$$

所以 $g(t)$ 在 $\left[\frac{1}{2}, 1\right]$ 上单调递增, 从而有

$$
g\left(\frac{1}{2}\right)=\frac{1-2 \ln 2}{4} \leqslant g(t) \leqslant g(1)=0
$$

因为 $x_{2}>\frac{1}{2}$, 所以 $f\left(x_{2}\right)>\frac{1-2 \ln 2}{4}$.

## 第 879 题 指数邂逅三角

已知 $f(x)=\mathrm{e}^{-|x|}+\cos \pi x$, 给出下列命题:

(1) $f(x)$ 的最大值为 2 ;

(2) $f(x)$ 在 $(-10,10)$ 内的零点之和为 0 ;

(2) $f(x)$ 的任何一个极大值都大于 1.

其中, 所有正确命题的序号是

解析 (1)(2).

对于命题(1), 由于

$$
f(x)=\mathrm{e}^{-|x|}+\cos \pi x \leqslant 2
$$

等号当且仅当 $x=0$ 时取得. 因此函数 $f(x)$ 的最大值为 2 .

对于命题(2), 由于 $f(x)$ 是偶函数, 且在区间 $(-10,10)$ 内存在零点, 于是 $f(x)$ 在 $(-10,10)$ 内的零点之和为 0.

对于命题 (3), 显然所有非零整数均不是函数 $f(x)$ 的极值点.

而 $x=0$ 是函数 $f(x)$ 的极大值, 且有 $f(0)=2>1$. 考虑到 $f(x)$ 是偶函数, 接下来考虑函数 $f(x)$ 在形如 $(2 k, 2 k+2](k \in \mathbf{N})$ 的区间内的极值点情况.

设 $x=t$ 是函数 $f(x)$ 的极值点, 则

$$
-\mathrm{e}^{-t}-\pi \sin \pi t=0
$$

如图.

由于在区间 $(2 k, 2 k+1)$ 上, 有 $f^{\prime}(x)<0$, 又

$$
f^{\prime}(2 k+1)<0, f^{\prime}\left(2 k+\frac{3}{2}\right)>0, f^{\prime}(2 k+2)<0
$$

因此函数 $f(x)$ 在区间 $(2 k, 2 k+1)$ 上不存在极值点,在区间

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-292.jpg?height=347&width=442&top_left_y=2114&top_left_x=1329)
$\left(2 k+1,2 k+\frac{3}{2}\right)$ 上存在一个极小值点, 在区间 $\left(2 k+\frac{3}{2}, 2 k+2\right]$ 上存在一个极

## 高考数学满分学霸的解题笔记，

大值点. 又由于

$$
f^{\prime \prime}(x)=\mathrm{e}^{-x}-\pi^{2} \cos \pi x
$$

在区间 $(2 k+1,2 k+2]$ 上单调递减, 于是函数 $f^{\prime \prime}(x)$ 在区间 $(2 k+1,2 k+2]$ 内至多只有一个零点, 进而函数 $f^{\prime}(x)$ 在区间 $(2 k+1,2 k+2]$ 内至多只有两个零点. 因此函数 $f(x)$ 在区间 $(2 k, 2 k+2](k \in \mathbf{N})$ 内的极大值存在且唯一.

另一方面,在每个区间 $(2 k, 2 k+2](k \in \mathbf{N})$ 内,均存在 $x_{0}=2 k+2$,

使得

$$
f\left(x_{0}\right)=\mathrm{e}^{-2 k-2}+1>1,
$$

于是函数 $f(x)$ 的每个极大值都大于 1.

思考与总结

对于命题(3),由于 $f(x)$ 是偶函数,所以只需考虑 $x \leqslant 0$ 的情形,

此时 $f(x)=\mathrm{e}^{x}+\cos \pi x$, 设 $t \in(-\infty, 0]$ 是 $f(x)$ 的一个极大值点, 则

$$
\begin{gathered}
f^{\prime}(t)=\mathrm{e}^{t}-\pi \sin \pi t=0 \\
f^{\prime \prime}(t)=\mathrm{e}^{t}-\pi^{2} \cos \pi t \leqslant 0
\end{gathered}
$$

因而 $\sin \pi t>0, \cos \pi t>0$.

从而得到

$$
\pi \geqslant \tan \pi t
$$

因此

$$
\begin{aligned}
f(t) & =\mathrm{e}^{t}+\cos \pi t \\
& =\pi \sin \pi t+\cos \pi t \\
& \geqslant \frac{\sin ^{2} \pi t}{\cos \pi t}+\cos \pi t \\
& =\frac{1}{\cos \pi t} \\
& \geqslant 1 .
\end{aligned}
$$

易知等号不能取到, 于是函数 $f(x)$ 的每个极大值都大于 1.

## 第 880 题 寻找分界点

已知函数 $f(x)=x^{2}-2 a x+4(a-1) \ln (x+1)$, 其中实数 $a<3$.

(1) 判断 $x=1$ 是否为函数 $f(x)$ 的极值点, 并说明理由;

(2) 若 $f(x) \leqslant 0$ 在区间 $[0,1]$ 上恒成立,求 $a$ 的取值范围.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{2}{x+1}(x-1)(x+2-a),
$$

由于

$$
a-2<1 \text {, }
$$

因此 $x=1$ 是函数 $f(x)$ 的极小值点.

(2) 由于 $f(0)=0$, 而

$$
f^{\prime}(0)=2(a-2)
$$

因此 $a=2$ 是讨论的分界点.

情形一 $\quad 2<a<3$.

此时在区间 $(0, a-2)$ 上, $f^{\prime}(x)>0$, 从而 $f(x)$ 单调递增.

又因为 $f(0)=0$, 所以有 $f(x)>0$, 不符合题意.

情形ニ $a \leqslant 2$.

此时在区间 $[0,1]$ 上, $f^{\prime}(x) \leqslant 0$, 从而 $f(x)$ 单调递减.

又因为 $f(0)=0$, 所以有 $f(x) \leqslant 0$, 符合题意.

综上所述, $a$ 的取值范围是 $(-\infty, 2]$.

## 第 881 题 逐层简化

已知函数 $f(x)=\frac{1-\ln x}{x^{2}}$.

(1) 求函数 $f(x)$ 的零点及单调区间;

(2) 求证: 曲线 $y=\frac{\ln x}{x}$ 存在斜率为 6 的切线, 且切点的纵坐标 $y_{0}<-1$.

解析 (1) $f(x)$ 的零点为 $x=\mathrm{e}$, 其导函数

$$
f^{\prime}(x)=\frac{2 \ln x-3}{x^{3}}
$$

于是其单调递减区间为 $\left(0, \mathrm{e}^{\frac{3}{2}}\right)$, 单调递增区间为 $\left(\mathrm{e}^{\frac{3}{2}},+\infty\right)$.

(2) 注意到函数 $y=\frac{\ln x}{x}$ 的导函数即为 $f(x)$, 画出函数草图如图.

由于当 $x>\mathrm{e}$ 时, $f(x)<0$, 且当 $x<\frac{1}{\mathrm{e}}$ 时, $f(x)>2 \mathrm{e}^{2}$,

因此在这两个区间上不存在符合题意的切线;

而在区间 $\left[\frac{1}{\mathrm{e}}, \mathrm{e}\right]$ 上,函数 $f(x)$ 从 $2 \mathrm{e}^{2}$ 单调递减到 0 ,

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-294.jpg?height=361&width=352&top_left_y=1343&top_left_x=1399)

因此在该区间上存在符合题意的切线.

设切点的横坐标为 $x_{0}$, 则

$$
\frac{1-\ln x_{0}}{x_{0}^{2}}=6 \quad \text { (1), } y_{0}=\frac{\ln x_{0}}{x_{0}}
$$

由(1)式得

$$
\ln x_{0}=1-6 x_{0}^{2}
$$

代人(2)式有

$$
y_{0}=\frac{1-6 x_{0}^{2}}{x_{0}}
$$

用分析法不难得知欲证 $y_{0}<-1$, 只需要证明 $x_{0}>\frac{1}{2}$.

考虑到函数 $f(x)$ 在区间 $\left[\frac{1}{\mathrm{e}}, \mathrm{e}\right]$ 上单调递减, 因此只需要证明

$$
f\left(x_{0}\right)<f\left(\frac{1}{2}\right),
$$

即 $6<4(1+\ln 2)$, 这显然成立, 因此原命题得证.

## 第 882 题 单调性的定义

已知函数 $f(x)=2^{x}, g(x)=x^{2}+a x$ (其中 $a \in \mathbf{R}$ ), 对于不相等的实数 $x_{1}, x_{2}$, 设 $m=\frac{f\left(x_{1}\right)-f\left(x_{2}\right)}{x_{1}-x_{2}}$, $n=\frac{g\left(x_{1}\right)-g\left(x_{2}\right)}{x_{1}-x_{2}}$. 现有如下命题:

(1)对于任意不相等的实数 $x_{1}, x_{2}$, 都有 $m>0$;

(2) 对于任意的 $a$ 及任意不相等的实数 $x_{1}, x_{2}$, 都有 $n>0$;

(3)对于任意的 $a$, 存在不相等的实数 $x_{1}, x_{2}$, 使得 $m=n$;

(4) 对于任意的 $a$, 存在不相等的实数 $x_{1}, x_{2}$, 使得 $m=-n$.其中的真命题有 $\qquad$ . (写出所有真命题的序号)

## 解析 (1)(4).

当 $x_{1}, x_{2}$ 为任意不相等的实数时, $m$ 恒正等价于函数 $f(x)$ 为单调递增函数, $m$ 恒负等价于函数 $f(x)$ 是单调递减函数, 于是(1)正确. 类似的, 可以判断(2)错误.

对于(3), $m=n$ 等价于

$$
f\left(x_{1}\right)-f\left(x_{2}\right)=g\left(x_{1}\right)-g\left(x_{2}\right),
$$

即

$$
f\left(x_{1}\right)-g\left(x_{1}\right)=f\left(x_{2}\right)-g\left(x_{2}\right),
$$

也即函数 $h(x)=f(x)-g(x)$ 与某条直线 (斜率为 0 ) 有两个不同交点, 等价于 $h(x)$ 不为单调函数, 也即 $h^{\prime}(x)$ 存在变号零点. 事实上,

$$
h(x)=2^{x}-x^{2}-a x,
$$

于是

$$
h^{\prime}(x)=2^{x} \ln 2-2 x-a,
$$

其零点为直线 $y=a$ 与曲线 $y=2^{x} \ln 2-2 x$ 的交点横坐标.

考虑到

$$
\left(2^{x} \ln 2-2 x\right)^{\prime}=2^{x} \ln ^{2} 2-2,
$$

于是 $y=2^{x} \ln 2-2 x$ 有最小值, 因此存在 $a$ 使得 $h^{\prime}(x)$ 没有零点, (3)错误.

对于(4), 采用与(3)类似的分析方法, 只需要判断函数 $k(x)=f(x)+g(x)$ 的导函数

$$
k^{\prime}(x)=2^{x} \ln 2+2 x+a
$$

是否存在变号零点.

考虑到 $y=2^{x} \ln 2+2 x$ 是值域为 $\mathbf{R}$ 的单调递增函数, 于是无论 $a$ 取何值, $k^{\prime}(x)$ 均存在变号零点, (4)正确.综上所述, 真命题有(1)(4).

思考与总结

所谓“变号零点”, 就是指在该零点附近左邻域与右邻域的函数值符号相反.

## 第 883 题 方程组解的存在性

已知函数 $f(x)=-2(x+a) \ln x+x^{2}-2 a x-2 a^{2}+a$, 其中 $a>0$.

(1) 设 $g(x)$ 是 $f(x)$ 的导函数, 讨论 $g(x)$ 的单调性;

(2) 证明: 存在 $a \in(0,1)$, 使得 $f(x) \geqslant 0$ 在区间 $(1,+\infty)$ 内恒成立, 且 $f(x)=0$ 在区间 $(1,+\infty)$ 内有唯一解.

解析 解法一 (1)根据已知, 有

$$
g(x)=f^{\prime}(x)=-2 \ln x+2 x-2-\frac{2 a}{x}-2 a,
$$

于是

$$
g^{\prime}(x)=\frac{2}{x^{2}}\left(x^{2}-x+a\right)
$$

于是按 $a$ 与 $\frac{1}{4}$ 的大小关系讨论如下.

当 $0<a<\frac{1}{4}$ 时, $g(x)$ 在 $\left(0, \frac{1-\sqrt{1-4 a}}{2}\right)$ 上单调递增, 在 $\left(\frac{1-\sqrt{1-4 a}}{2}, \frac{1+\sqrt{1-4 a}}{2}\right)$ 上单调递减, 在 $\left(\frac{1+\sqrt{1-4 a}}{2},+\infty\right)$ 上单调递增;

当 $a \geqslant \frac{1}{4}$ 时, $g(x)$ 在 $\mathbf{R}^{+}$上单调递增.

(2) 用分析法证明如下.

根据题意结合第 (1) 小题的结论, 函数 $f(x)$ 的图象应该如图所示.

考虑函数 $g(x)$, 由于 $g^{\prime}(1)=2 a>0$, 于是在 $(1,+\infty)$ 上 $g(x)$ 单调递增.

又 $g(1)=-4 a<0$, 因此 $g(x)$ 有唯一零点 $x=x_{0}$,

于是 $f(x)$ 在 $(1,+\infty)$ 上先单调递减, 再单调递增, 有极小值点 $x=x_{0}$, 则

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-296.jpg?height=267&width=396&top_left_y=1410&top_left_x=1373)

$$
\left\{\begin{array}{l}
-\ln x_{0}+x_{0}-1-a\left(\frac{1}{x_{0}}+1\right)=0 \\
-2\left(x_{0}+a\right) \ln x_{0}+x_{0}^{2}-2 a x_{0}-2 a^{2}+a=0
\end{array}\right.
$$

我们的目标是证明这个二元方程组有实数解, 且至少有一组解满足限制条件 $x_{0}>1$ 且 $0<a<1$.

由第一个方程可得

$$
-\ln x_{0}=-x_{0}+1+a\left(\frac{1}{x_{0}}+1\right)
$$

代人第二个方程, 可得

$$
x_{0}^{3}+(2 a-2) x_{0}^{2}-5 a x_{0}-2 a^{2}=0,
$$

因式分解, 可得

$$
\left(x_{0}+2 a\right)\left(x_{0}^{2}-2 x_{0}-a\right)=0
$$

于是

$$
a=x_{0}^{2}-2 x_{0},
$$

进而可得

$$
a=x_{0}^{2}-2 x_{0}=-\ln x_{0}+1,
$$

容易判断 $x_{0} \in(2, \mathrm{e})$, 于是 $a \in(0,1-\ln 2)$, 原命题得证.

解法二

(1)根据已知, 有

$$
g(x)=f^{\prime}(x)=-2 \ln x+2 x-2-\frac{2 a}{x}-2 a
$$

于是

$$
g^{\prime}(x)=\frac{2}{x^{2}}\left(x^{2}-x+a\right)
$$

于是按 $a$ 与 $\frac{1}{4}$ 的大小关系讨论如下.

情形一 当 $0<a<\frac{1}{4}$ 时, $g(x)$ 在 $\left(0, \frac{1-\sqrt{1-4 a}}{2}\right)$ 上单调递增, 在 $\left(\frac{1-\sqrt{1-4 a}}{2}, \frac{1+\sqrt{1-4 a}}{2}\right)$ 上单调递减, 在 $\left(\frac{1+\sqrt{1-4 a}}{2},+\infty\right)$ 上单调递增;

情形二 当 $a \geqslant \frac{1}{4}$ 时, $g(x)$ 在 $\mathbf{R}^{+}$上单调递增.

(2) 考虑到对于函数 $f(x)$, 若 $f\left(x_{0}\right)=0$ 且 $f^{\prime}\left(x_{0}\right)=0$, 则函数 $f(x) \cdot \varphi(x)$ 也满足

$$
[f(x) \cdot \varphi(x)]_{x=x_{0}}=0,[f(x) \cdot \varphi(x)]_{x=x_{0}}^{\prime}=0
$$

接下来“清君侧”即可. 考虑函数 $g(x)$, 由于 $g^{\prime}(1)=2 a>0$, 于是在 $(1,+\infty)$ 上 $g(x)$ 单调递增.又 $g(1)=-4 a<0, g(+\infty)>0$, 于是 $f(x)$ 在 $(1,+\infty)$ 上先单调递减, 再单调递增, 有极小值点.设 $f(x)$ 的极小值点为 $x=x_{0}$, 令 $h(x)=\frac{f(x)}{x+a}$, 即

$$
h(x)=-2 \ln x+x-3 a+\frac{a^{2}+a}{x+a}
$$

则有

$$
h^{\prime}(x)=\frac{(x+2 a)\left(x^{2}-2 x-a\right)}{x(x+a)^{2}}
$$

于是可得

$$
a=x_{0}^{2}-2 x_{0}
$$

进而由 $h\left(x_{0}\right)=0$ 可得

$$
a=x_{0}^{2}-2 x_{0}=-2 \ln x_{0}+1,
$$

容易判断 $x_{0} \in(2, \mathrm{e})$, 于是 $a \in(0,1-\ln 2)$, 原命题得证.

## 第 884 题画图也要有决倥

已知函数 $f(x)=a x-\mathrm{e}^{x}$, 若存在实数 $x$, 使得 $f(x) \geqslant 0$, 求 $a$ 的取值范围.

解析 解法 - 问题即

$$
\exists x \in \mathbf{R}, a x-\mathrm{e}^{x} \geqslant 0
$$

也即

$$
\left(\exists x>0, a \geqslant \frac{\mathrm{e}^{x}}{x}\right) \text { 或 }\left(\exists x<0, a<\frac{\mathrm{e}^{x}}{x}\right),
$$

接下来需要绘制 $g(x)=\frac{\mathrm{e}^{x}}{x}$ 的草图.

注意到函数 $g(x)$ 的定义域为 $(-\infty, 0) \cup(0,+\infty)$, 且函数 $g(x)$ 的导函数为

$$
g^{\prime}(x)=\frac{\mathrm{e}^{x}}{x^{2}} \cdot(x-1)
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-297.jpg?height=541&width=664&top_left_y=2034&top_left_x=1197)

图 1
于是函数 $g(x)$ 在 $(-\infty, 0)$ 和 $(0,1)$ 上单调递减, 在 $(1,+\infty)$ 上单调递增.

于是绘制草图, 如图 1. 需要注意的是代表定义域的四个区间端点处的函数值的估计. 五个要点任何一点没有注意到都容易引起错误.

进而不难得到 $a$ 的取值范围是 $(-\infty, 0) \cup[\mathrm{e},+\infty)$.

解法二 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=a-\mathrm{e}^{x}
$$

于是需要按 $a$ 分类讨论.
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-298.jpg?height=632&width=794&top_left_y=566&top_left_x=524)

图 2

当 $a<0$ 时, $f(x)$ 单调递减, 考虑到 $x \rightarrow-\infty$ 时, $f(x) \rightarrow+\infty$, 而当 $x \rightarrow+\infty$ 时, $f(x) \rightarrow-\infty$, 于是符合题意.

当 $a=0$ 时, $f(x)$ 单调递减, 考虑到 $x \rightarrow-\infty$ 时, $f(x) \rightarrow 0^{-}$, 而当 $x \rightarrow+\infty$ 时, $f(x) \rightarrow-\infty$, 于是不符合题意.

当 $a>0$ 时, 函数 $f(x)$ 有极大值, 同时也是最大值, 为 $f(\ln a)$ $=a(\ln a-1)$, 根据题意, 最大值不小于 0 , 于是可以解得 $a \geqslant \mathrm{e}$.

综上, $a$ 的取值范围是 $(-\infty, 0) \cup[e,+\infty)$.

解法三 问题即

$$
\exists x \in \mathbf{R}, a x \geqslant \mathrm{e}^{x},
$$

于是计算函数 $y=\mathrm{e}^{x}$ 过原点的切线, 作图如图 3.

不难得到 $a$ 的取值范围是 $(-\infty, 0) \cup[\mathrm{e},+\infty)$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-298.jpg?height=412&width=611&top_left_y=1458&top_left_x=1154)

图 3

## 第 885 题 天堑变通途

设函数 $f(x)=\ln x+\frac{a}{\mathrm{e} x}$.

(1) 讨论函数 $f(x)$ 的单调性；

(2) 若 $a=2$, 证明:对任意的 $x>0$, 都有 $f(x)>\mathrm{e}^{-x}$.

解析 (1) $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{1}{\mathrm{e} x^{2}} \cdot(\mathrm{e} x-a)
$$

## 高考数学满分学霸的解题笔记(一千考一賭)

情形一 当 $a \leqslant 0$ 时, 函数 $f(x)$ 在 $(0,+\infty)$ 上单调递增;

情形二 当 $a>0$ 时, 函数 $f(x)$ 在 $\left(0, \frac{a}{\mathrm{e}}\right)$ 上单调递减, 在 $\left(\frac{a}{\mathrm{e}},+\infty\right)$ 上单调递增.

(2) 题中的不等式即

$$
\ln x+\frac{2}{\mathrm{e} x}>\mathrm{e}^{-x}
$$

也即

$$
x \ln x+\frac{2}{\mathrm{e}}>\mathrm{e}^{-x} \cdot x
$$

设函数 $h(x)=x \ln x$, 那么我们有

$$
h\left(\mathrm{e}^{-x}\right)=-\mathrm{e}^{-x} \cdot x,
$$

于是该不等式即

$$
h(x)+h\left(\mathrm{e}^{-x}\right) \geqslant-\frac{2}{\mathrm{e}}
$$

发现题中指数部分和对数部分之间的关联后, 研究其中的桥梁一 $h(x)$ 就势在必行了. 事实上, $h(x)$ 的导函数

$$
h^{\prime}(x)=1+\ln x,
$$

于是函数 $h(x)$ 的草图如图, 在 $(0,+\infty)$ 上的最小值为

$$
h\left(\frac{1}{\mathrm{e}}\right)=-\frac{1}{\mathrm{e}}
$$

由于当 $x>0$ 时, $\mathrm{e}^{-x}$ 取遍所有 $(0,1)$ 上的实数, 于是 $h\left(\mathrm{e}^{-x}\right)$ 的取值范围是 $\left[-\frac{1}{\mathrm{e}}, 0\right)$. 这样我们就得到了

$$
h(x) \geqslant-\frac{1}{\mathrm{e}}, h\left(\mathrm{e}^{-x}\right) \geqslant-\frac{1}{\mathrm{e}}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-299.jpg?height=320&width=450&top_left_y=1048&top_left_x=1409)

但两个式子中的等号分别当且仅当 $x=\frac{1}{\mathrm{e}}$ 和 $x=1$ 时取得, 无法同时取得,

因此我们就得到了题中的不等式.

## 思考与总结

解题中用到了这个简单事实:

引理 一个复合函数 $f(g(x))$ 的取值范围是函数 $f(x)$ 的值域的子集, 特别的, 如果函数 $g(x)$ 的取值范围恰好与 $f(x)$ 的定义域相同, 那么复合函数 $f(g(x))$ 的取值范围就是函数 $f(x)$ 的值域.

利用引理,我们可以通过一种新颖的方式证明:

如果函数 $f(x)=x+\frac{1}{x}$, 其中 $x>0$ 有最小值 $m$, 那么 $m=2$.

证明 考虑函数 $[f(x)]^{2}$.

一方面, 其最小值为 $m^{2} ;$

另一方面,有

$$
[f(x)]^{2}=x^{2}+\frac{1}{x^{2}}+2=f\left(x^{2}\right)+2
$$

而当 $x$ 取遍所有正实数时, $x^{2}$ 也取遍所有正实数, 因此其最小值为 $m+2$;

综上,可以得到

$$
m^{2}=m+2 \text {, }
$$

解得 $m=2$, 其中 $m=-1$ 舍去.

## 第 886 题避繁就简

已知函数 $f(x)=a \ln x+\frac{1}{x}+\frac{1}{2 x^{2}}, a \in \mathbf{R}$.

(1) 讨论函数 $f(x)$ 的单调性;

(2) 证明: $(x-1)\left(\mathrm{e}^{-x}-x\right)+2 \ln x<\frac{2}{3}$.

解析 解法一 (1) $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{1}{x^{3}}\left(a x^{2}-x-1\right)
$$

进而可得：

情形一 当 $a \leqslant 0$ 时,函数 $f(x)$ 在 $\mathbf{R}^{+}$上单调递减;

情形二 当 $a>0$ 时, 函数 $f(x)$ 在 $\left(0, \frac{1+\sqrt{1+4 a}}{2 a}\right)$ 上单调递减, 在 $\left(\frac{1+\sqrt{1+4 a}}{2 a},+\infty\right)$ 上单调递增.

(2) 在题(1) 中取 $a=2$, 则可得

$$
2 \ln x+\frac{1}{x}+\frac{1}{2 x^{2}} \geqslant f(1)=\frac{3}{2},
$$

将其中的 $x$ 用 $\frac{1}{x}$ 替换, 可得

$$
-2 \ln x+x+\frac{x^{2}}{2} \geqslant \frac{3}{2}
$$

即

$$
2 \ln x \leqslant x+\frac{x^{2}}{2}-\frac{3}{2}
$$

将上述不等式代人欲证明不等式的左边, 有

$$
\begin{aligned}
(x-1)\left(\mathrm{e}^{-x}-x\right)+2 \ln x & <(x-1) \cdot \mathrm{e}^{-x}-x^{2}+x+\left(x+\frac{x^{2}}{2}-\frac{3}{2}\right) \\
& =(x-1) \cdot \mathrm{e}^{-x}-\frac{x^{2}}{2}+2 x-\frac{3}{2}
\end{aligned}
$$

设右侧函数为 $g(x)$, 则 $g(x)$ 的导函数

$$
g^{\prime}(x)=(2-x)\left(\mathrm{e}^{-x}+1\right)
$$

于是

$$
g(x) \leqslant g(2)=\frac{1}{\mathrm{e}^{2}}+\frac{1}{2}<\frac{2}{3},
$$

因此原不等式得证.

解法二 (1) 见解法一.

(2) 直接利用对数函数不等式

$$
\ln x \leqslant x-1
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-300.jpg?height=383&width=487&top_left_y=1866&top_left_x=1262)

进行放缩消去对数符号:

$$
\begin{aligned}
(x-1)\left(\mathrm{e}^{-x}-x\right)+2 \ln x & \leqslant(x-1)\left(\mathrm{e}^{-x}-x\right)+2(x-1) \\
& =(x-1) \cdot \mathrm{e}^{-x}+(2-x)(x-1)
\end{aligned}
$$

由于

$$
\left(\frac{x-1}{\mathrm{e}^{x}}\right)^{\prime}=\frac{2-x}{\mathrm{e}^{x}},
$$

## 高考数学满分学霸的解题笔记

于是其最大值为

$$
\left.\left(\frac{x-1}{\mathrm{e}^{x}}\right)\right|_{x=2}=\frac{1}{\mathrm{e}^{2}}
$$

因此欲证明不等式左边

$$
(x-1)\left(\mathrm{e}^{-x}-x\right)+2 \ln x \leqslant \frac{1}{\mathrm{e}^{2}}+\frac{1}{4}<\frac{2}{3}
$$

思考与总结

注一 可以看到不用题 (1) 的结论可以得到更好的结果. 左侧函数的最大值约为 0.218797 , 如图.

注二 更简单的作法:

$$
\begin{aligned}
(x-1)\left(\mathrm{e}^{-x}-x\right)+2 \ln x & \leqslant(x-1)\left(\mathrm{e}^{-x}-x\right)+2(x-1) \\
& =(x-1) \cdot\left(\mathrm{e}^{-x}-\frac{1}{\mathrm{e}}\right)+\left(2+\frac{1}{\mathrm{e}}-x\right)(x-1) \\
& <\frac{1}{4}\left(1+\frac{1}{\mathrm{e}}\right)^{2} \\
& <\frac{2}{3}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-301.jpg?height=470&width=539&top_left_y=613&top_left_x=1306)

## 第 887 题 谁是赢家

已知 $x \in\left(0, \frac{\pi}{2}\right)$, 求证: $\sin x \cdot \tan x>x^{2}$.

解析 解法一

记函数 $f(x)=\sin x \cdot \tan x-x^{2}$, 则当 $x \in\left(0, \frac{\pi}{2}\right)$ 时, 其导函数

$$
\begin{aligned}
f^{\prime}(x) & =\frac{2 \sin x \cos ^{2} x+\sin ^{3} x}{\cos ^{2} x}-2 x \\
& =\sin x\left(\frac{1}{\cos ^{2} x}+1\right)-2 x \\
& \geqslant \sin x \cdot \frac{2}{\cos x}-2 x \\
& =2(\tan x-x) \\
& >0,
\end{aligned}
$$

又 $f(0)=0$, 于是原不等式得证.

有趣的是, 当 $x \in\left(0, \frac{\pi}{2}\right)$ 时, 不等式

$$
\sin ^{3} x \cdot \tan x>x^{4}
$$

不再恒成立, 例如当 $x=\frac{\pi}{3}$ 时, 左边约为 1.125 , 右边约为 1.202 .

解法二 注意到当 $x \in\left(0, \frac{\pi}{2}\right)$ 时, 有

$$
\sin x>x-\frac{x^{3}}{6}
$$

以及

$$
\tan x>x+\frac{x^{3}}{3}
$$

于是

$$
\sin x \cdot \tan x>x^{2}+\frac{x^{4}}{6}\left(1-\frac{x^{2}}{3}\right)>x^{2},
$$

于是原不等式得证.

## 第 888 题 $\quad-$ 叶知秋

已知函数 $f(x)=\ln x+\frac{a}{x+1}$, 若 $f(x)$ 为单调递增函数, 试讨论关于 $x$ 的方程 $f(x)=x^{2}-2 x+3$ 的解的个数.

解析 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{x^{2}+(2-a) x+1}{x(x+1)^{2}}
$$

于是 $f(x)$ 为单调递增函数即

$$
\forall x>0, x^{2}+(2-a) x+1 \geqslant 0,
$$

分离变量可得 $a \leqslant 4$.

注意到当 $a=4$ 时, $x=1$ 是方程的解, 而此时 $y=x^{2}-2 x+3$ 取最小值, 于是尝试证明 $\ln x+\frac{a}{x+1} \leqslant x^{2}-$ $2 x+3$.

根据已知, 有

$$
\ln x+\frac{a}{x+1} \leqslant x-1+\frac{4}{x+1}=\frac{x^{2}+3}{x+1}
$$

而

$$
x^{2}-2 x+3-\frac{x^{2}+3}{x+1}=\frac{x(x-1)^{2}}{x+1} \geqslant 0
$$

因此

$$
\ln x+\frac{a}{x+1} \leqslant x^{2}-2 x+3,
$$

等号当且仅当 $a=4, x=1$ 时取得. 因此当 $a=4$ 时, 题中方程有 1 个解; 当 $a<4$ 时, 题中方程无解.

事实上,在本题中 $a=4$ 时的函数图象如图所示,和我们猜想的非常一致.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-302.jpg?height=380&width=401&top_left_y=2161&top_left_x=696)

## 第 889 题 $\pi$ 的估算

设 $n$ 为偶数, 且 $n \geqslant 6$. 记 $S_{n}$ 为单位圆的内接正 $n$ 边形的面积.

(1) 证明: $\frac{4}{3} S_{2 n}-\frac{1}{3} S_{n}<\pi<\frac{8}{3} S_{2 n}-2 S_{n}+\frac{1}{3} S_{\frac{n}{2}}$;

(2)已知 $1.732<\sqrt{3}<1.733,3.105<S_{24}<3.106$, 证明: $3.14<\pi<3.15$.

解析 (1) 容易计算得 $S_{n}=\frac{n}{2} \sin \frac{2 \pi}{n}$, 于是欲证明不等式即

$$
\frac{4}{3} n \sin \frac{\pi}{n}-\frac{1}{6} n \sin \frac{2 \pi}{n}<\pi<\frac{8}{3} n \sin \frac{\pi}{n}-n \sin \frac{2 \pi}{n}+\frac{1}{12} n \sin \frac{4 \pi}{n}
$$

也即

$$
\frac{4}{3} \sin \frac{\pi}{n}-\frac{1}{6} \sin \frac{2 \pi}{n}<\frac{\pi}{n}<\frac{8}{3} \sin \frac{\pi}{n}-\sin \frac{2 \pi}{n}+\frac{1}{12} \sin \frac{4 \pi}{n}
$$

记 $x=\frac{\pi}{n}$, 只需要证明当 $x \in\left(0, \frac{\pi}{6}\right)$ 时, 有

$$
\frac{4}{3} \sin x-\frac{1}{6} \sin 2 x<x<\frac{8}{3} \sin x-\sin 2 x+\frac{1}{12} \sin 4 x
$$

左侧不等式即

$$
3 x-4 \sin x+\frac{1}{2} \sin 2 x>0
$$

要此不等式成立只需要

$$
3+\left(2 \cos ^{2} x-1\right)-4 \cos x \geqslant 0
$$

也即 $2(\cos x-1)^{2} \geqslant 0$, 当 $x \in\left(0, \frac{\pi}{6}\right)$ 时, 显然成立.

接下来证明右侧不等式. 右侧不等式即

$$
8 \sin x-3 \sin 2 x+\frac{1}{4} \sin 4 x>3 x
$$

记函数

$$
f(x)=8 \cos x-6 \cos 2 x+\cos 4 x, x \in\left[0, \frac{\pi}{6}\right)
$$

则其导函数

$$
f^{\prime}(x)=8 \sin x(1-\cos x)\left(4 \cos ^{2} x+4 \cos x-1\right),
$$

于是 $f(x)$ 在 $\left(0, \frac{\pi}{6}\right)$ 上单调递增, 有

$$
f(x)>f(0)=3,
$$

于是右侧不等式成立.

综上,原命题得证.

(2) 在第 $(1)$ 小题中, 取 $n=12$ 即得.

这种估算 $\pi$ 的精度相当于用 $x=\frac{\pi}{30}$ 时, $\sin x \approx x$ 估算 $\pi$ 的精度.

## 第 890 题 百炼钢化为绕指柔

已知 $a, b>0$ 且 $a b=1$, 求证: $2^{a+b} \geqslant 2^{a}+2^{b}$.

解析 解法一 设 $2^{x}=t(1<t \leqslant 2)$, 则 $x=\frac{\ln t}{\ln 2}$,

欲证不等式即

$$
\frac{1}{t}+\frac{1}{2^{\frac{\ln ^{2}}{}}} \leqslant 1
$$

也即

$$
2^{\frac{\ln ^{2} 2}{n n}} \geqslant \frac{t}{t-1}
$$

整理为

$$
\frac{\ln 2}{\ln t}-\ln t+\ln (t-1) \geqslant 0
$$

设上式左边为 $f(t)$, 则 $f(t)$ 的导函数

$$
f^{\prime}(t)=\frac{\ln ^{2} t-(t-1) \ln ^{2} 2}{t(t-1) \ln ^{2} t}
$$

记分子为 $r(t)$, 则

$$
r^{\prime}(t)=\frac{2 \ln t}{t}-\ln ^{2} 2
$$

注意到

$$
r^{\prime \prime}(t)=\frac{2(1-\ln t)}{t^{2}}
$$

因此 $r^{\prime}(t)$ 在 $(1,2]$ 上单调递增, 有唯一零点, 因此 $r(t)$ 先单调递减, 后单调递增.

又 $r(1)=r(2)=0$, 因此在 $(1,2]$ 上 $r(t) \leqslant 0$, 因此 $f(t)$ 在 $(1,2]$ 上单调递减,

又 $f(2)=0$, 因此在 $(1,2]$ 上有 $f(t) \geqslant 0$, 原不等式得证.

解法二 不妨设 $a \geqslant b$, 则

$$
b=\frac{1}{a}, a \geqslant 1
$$

题中不等式转化为 $2^{\frac{1}{a}}\left(2^{a}-2^{a-\frac{1}{a}}-1\right) \geqslant 0$, 于是即证

$$
\forall a \geqslant 1,2^{a}-2^{a-\frac{1}{a}}-1 \geqslant 0
$$

设 $f(x)=2^{x}-2^{x-\frac{1}{x}}-1, x \geqslant 1$, 对此函数求导得

$$
f^{\prime}(x)=\ln 2 \cdot 2^{x^{-\frac{1}{x}}}\left(2^{\frac{1}{x}}-1-\frac{1}{x^{2}}\right)
$$

令 $g(m)=2^{m}-1-m^{2}, m \in[0,1]$, 则

$$
g^{\prime}(m)=2^{m} \cdot \ln 2-2 m
$$

其二阶导数为

$$
g^{\prime \prime}(m)=2^{m} \cdot(\ln 2)^{2}-2<0
$$

所以 $g^{\prime}(m)$ 在 $[0,1]$ 上单调递减. 又因为

$$
g^{\prime}(0)=\ln 2>0, g^{\prime}(1)=2 \ln 2-2<0
$$

所以 $g(m)$ 在 $[0,1]$ 上先单调递增, 后单调递减. 而

$$
g(0)=g(1)=0
$$

所以 $g(m) \geqslant 0$ 恒成立. 而当 $x \geqslant 1$ 时, $\frac{1}{x} \in(0,1]$, 所以

$$
\forall x \geqslant 1,2^{\frac{1}{x}}-1-\frac{1}{x^{2}} \geqslant 0
$$

从而有 $f^{\prime}(x) \geqslant 0, f(x)$ 在 $[1,+\infty)$ 上单调递增.

又因为 $f(1)=0$, 所以 $f(x) \geqslant f(1)=0$, 命题得证.

解法三 记 $f(x)=2^{x}-x^{2} \cdot 2^{\frac{1}{x}}$, 则 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{\ln 2}{x^{2} \cdot 2^{x+\frac{1}{x}}} \cdot\left(2^{x}-x^{2} \cdot 2^{\frac{1}{x}}\right)
$$

注意到当 $x \rightarrow 0^{+}$时, $f(x) \rightarrow 1$, 而 $f(1)=1$, 因此只需要说明函数 $f(x)$ 在 $(1,2]$ 上的极值不超过 1 .设 $m$ 为 $f(x)$ 在区间 $(0,1]$ 上的极值点, 则

$$
2^{m}-m^{2} \cdot 2^{\frac{1}{m}}=0
$$

其极值

$$
f(m)=\frac{1}{2^{m}}+\frac{1}{2^{\frac{1}{m}}}=\frac{1+m^{2}}{2^{m}}
$$

接下来尝试证明辅助命题

$$
\forall m \in(0,1], 2^{m} \geqslant m^{2}+1
$$

设 $g(m)=2^{m}-m^{2}-1$, 则

$$
g(0)=g(1)=0
$$

而 $g(x)$ 的导函数

$$
g^{\prime}(m)=2^{m} \ln 2-2 m
$$

其二阶导函数

$$
g^{\prime \prime}(m)=2^{m} \ln ^{2} 2-2
$$

于是 $g^{\prime}(m)$ 在 $(0,1]$ 上单调递减, 又 $g^{\prime}(0)>0, g^{\prime}(1)<0$, 因此 $g(m)$ 在 $(0,1]$ 上先单调递增, 后单调递减,于是辅助命题得证.

综上所述,原不等式得证.

## 第 891 题 投石问路

对任意的实数 $m, n$, 当 $0<n<m<\frac{1}{a}$ 时, 恒有 $\frac{\sqrt[m]{n}}{\sqrt[n]{m}}>\frac{n^{a}}{m^{a}}$ 成立, 则实数 $a$ 的最小值为

解析 解法一 先做一些初步估计,必要时再做细致的计算.

当 $a<1$ 时, 取 $m=1$, 则 $0<n<1$, 此时不等式为 $n>n^{a}$, 显然不成立;

当 $a=1$ 时, 有 $0<n<m<1$, 题中不等式即

$$
\frac{1}{m} \ln n-\frac{1}{n} \ln m>\ln n-\ln m
$$

即

$$
\frac{1}{m} \ln \frac{1}{n}-\frac{1}{n} \ln \frac{1}{m}<\ln \frac{1}{n}-\ln \frac{1}{m}
$$

也即

$$
\frac{\ln \frac{1}{n}}{\frac{1}{n}-1}<\frac{\ln \frac{1}{m}}{\frac{1}{m}-1}
$$

考虑函数 $f(x)=\frac{\ln x}{x-1}(x>1)$, 其导函数

$$
f^{\prime}(x)=\frac{\ln \frac{1}{x}-\frac{1}{x}+1}{(x-1)^{2}}<0
$$

因此题中不等式恒成立.

解法二 先做一些初步估计,必要时再做细致的计算.

当 $a<1$ 时, 取 $m=1$, 则 $0<n<1$, 此时不等式为 $n>n^{a}$, 显然不成立;

当 $a=1$ 时, 有 $0<n<m<1$, 题中不等式即

$$
m^{1-\frac{1}{n}}>n^{1-\frac{1}{m}}
$$

因为 $1-\frac{1}{n}<1-\frac{1}{m}$, 所以

$$
m^{1-\frac{1}{n}}>m^{1-\frac{1}{m}}>n^{1-\frac{1}{m}}
$$

综上所述, 实数 $a$ 的最小值为 1 .

## 第 892 题缩小包围圈

已知函数 $f(x)=\mathrm{e}^{x}\left(x^{2}+a x+a\right)$.

(1) 当 $a=1$ 时,求函数 $f(x)$ 的单调区间;

(2) 若关于 $x$ 的不等式 $f(x) \leqslant \mathrm{e}^{a}$ 在 $[a,+\infty)$ 上有解, 求实数 $a$ 的取值范围;

(3) 若曲线 $y=f(x)$ 存在两条互相垂直的切线, 求实数 $a$ 的取值范围. (只需直接写出结果)

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}(x+a)(x+2)
$$

当 $a=1$ 时, 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}(x+1)(x+2),
$$

于是函数 $f(x)$ 的单调递增区间为 $(-\infty,-2)$ 和 $(-1,+\infty)$; 单调递减区间为 $(-2,-1)$.

(2) 先考虑 $f(a)=\mathrm{e}^{a}\left(2 a^{2}+a\right)$, 显然当 $-1 \leqslant a \leqslant \frac{1}{2}$ 时, $f(a) \leqslant \mathrm{e}^{a}$, 接下来研究其他情形.

当 $a<-1$ 时, 函数 $f(x)$ 在 $(-\infty,-2)$ 和 $(-a,+\infty)$ 上单调递增; 在 $(-2,-a)$ 上单调递减, 因此函数 $f(x)$ 在 $[a,+\infty)$ 上的最小值必然为 $\min \{f(a), f(-a)\}$.

考虑到 $f(a)>\mathrm{e}^{a}$, 又

$$
f(-a)=\mathrm{e}^{-a} \cdot a<0<\mathrm{e}^{a},
$$

因此符合题意.

当 $a>\frac{1}{2}$ 时, 无论 $-a$ 与 -2 的大小关系如何, 均有函数 $f(x)$ 在 $[a,+\infty)$ 上单调递增.

又 $f(a)>\mathrm{e}^{a}$, 因此不符合题意.

综上所述, 实数 $a$ 的取值范围是 $\left(-\infty, \frac{1}{2}\right]$.
题(2)还可以利用

$$
x^{2}+a x+a \leqslant \mathrm{e}^{a-x} \leqslant 1
$$

得到必要条件 $a \leqslant \frac{1}{2}$, 再论证充分性.

(3) 由于 $f^{\prime}(x)$ 的取值无上界, 因此只需要存在负的函数值即可, 因此 $a$ 的取值范围是 $(-\infty, 2) \cup(2$, $+\infty)$

## 第 893 题 恠借东风

已知 $f(x)=\frac{x \ln x}{x-1}+a$, 其中 $a>0$.

(1) 求 $f(x)$ 的单调性;

(2) 若 $g(x)=\left(x^{2}-x\right) \cdot f(x)$, 且方程 $g(x)=m$ 有两个不同的实根 $x_{1}, x_{2}$, 求证: $x_{1}+x_{2}>1$.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{x-1-\ln x}{(x-1)^{2}}
$$

而我们熟知 $\ln x \leqslant x-1$,因此 $f^{\prime}(x) \geqslant 0$, 因此函数 $f(x)$ 在 $(0,1)$ 和 $(1,+\infty)$ 上单调递增.

(2) 用反证法. 假设 $x_{1}+x_{2} \leqslant 1$, 不妨设 $x_{1}<x_{2}$, 则有 $x_{1}, x_{2} \in(0,1)$ 且

$$
\left(x_{1}-x_{2}\right)\left(x_{1}+x_{2}-1\right) \geqslant 0
$$

也即

$$
0>x_{1}^{2}-x_{1}>x_{2}^{2}-x_{2},
$$

结合 $f(x)>0$, 可得

$$
\left(x_{2}^{2}-x_{2}\right) \cdot f\left(x_{2}\right)=\left(x_{1}^{2}-x_{1}\right) \cdot f\left(x_{1}\right) \geqslant\left(x_{2}^{2}-x_{2}\right) \cdot f\left(x_{1}\right),
$$

从而 $f\left(x_{2}\right) \leqslant f\left(x_{1}\right)$, 进而 $x_{2} \leqslant x_{1}$, 与 $x_{1}<x_{2}$ 矛盾.

综上,原命题得证.

注意到 $x^{2}-x$ 的对称轴恰好是 $x=\frac{1}{2}$, 结合第(1) 小题的提示可以迅速化简问题.

## 第 894 题 限制条件下的最值

已知 $m, n \geqslant 0$, 函数 $f(x)=\frac{1}{2}(m-2) x^{2}+(n-8) x+1$ 在区间 $\left[\frac{1}{2}, 2\right]$ 上单调递减, 则 $m n$ 的最大值是 $\qquad$ .

解析 18 .
由 $m, n \geqslant 0, f^{\prime}\left(\frac{1}{2}\right) \leqslant 0, f^{\prime}(2) \leqslant 0$ 得

$$
\left\{\begin{array}{l}
2 n+m \leqslant 18 \\
2 m+n \leqslant 12
\end{array}\right.
$$

规划如图.

可得 $m n$ 的最大值是 18 , 当 $m=3, n=6$ 时取到最大值.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-308.jpg?height=346&width=280&top_left_y=198&top_left_x=1484)

## 第 895 题 函数的单调性

若函数 $f(x)=x^{2} \cdot|x-a|$ 在区间 $[0,2]$ 上单调递增, 则实数 $a$ 的取值范围是

解析 $(-\infty, 0] \cup[3,+\infty)$.

若 $a \leqslant 0$, 则当 $x \in[0,2]$ 时, $f(x)=x^{2} \cdot(x-a)$, 单调递增, 符合题意.

若 $a>0$, 必然有 $a>2$ (否则 $f(0)=f(a)=0$, 不可能在 $[0, a]$ 上单调递增, 不符合题意).

于是当 $x \in[0,2]$ 时, 有

$$
f(x)=x^{2} \cdot(a-x),
$$

其导函数

$$
f^{\prime}(x)=x(2 a-3 x)
$$

因此有 $\frac{2 a}{3} \geqslant 2$, 从而 $a \geqslant 3$.

综上所述, $a$ 的取值范围是 $(-\infty, 0] \cup[3,+\infty)$.

## 第 896 题 构造函数证明不等式

已知 $a, b \in(0,1)$, 求证: $a^{a}+b^{b} \geqslant a^{b}+b^{a}$.

解析 当 $a=b$ 时, 不等式显然成立;

当 $a \neq b$ 时, 不妨设 $0<a<b<1$, 且令 $\varphi(x)=x^{a}-x^{b}$, 则只需要证明 $\varphi(x)$ 在区间 $[a, b]$ 上单调递减.

由于 $\varphi(x)$ 的导函数

$$
\varphi^{\prime}(x)=a x^{a-1}-b x^{b-1}=b x^{a-1}\left(\frac{a}{b}-x^{b-a}\right)
$$

而 $y=x^{b-a}$ 在 $(0,+\infty)$ 上单调递增, 于是只需要证明

$$
\forall b \in(a, 1), \frac{a}{b}-a^{b-a}<0
$$

也即

$$
\forall b \in(a, 1), b \ln a+\ln b-(a+1) \ln a>0
$$

令 $\mu(x)=x \ln a+\ln x-(a+1) \ln a$, 则其导函数

$$
\mu^{\prime}(x)=\ln a+\frac{1}{x}
$$

考虑 $\mu^{\prime}(a)=\ln a+\frac{1}{a}$, 我们熟知当 $a \in(0,1)$ 时, 有

$$
\ln a=-\ln \frac{1}{a}>-\left(\frac{1}{a}-1\right)=1-\frac{1}{a},
$$

于是 $\mu^{\prime}(a)>1$, 又 $\mu^{\prime}(x)$ 单调递减, 因此在区间 $(a, 1)$ 上, 函数 $\mu(x)$ 或者单调递增,或者先单调递增后单调递减. 又 $\mu(a)=0, \mu(1)=-a \ln a>0$, 于是在区间 $(a, 1)$ 上, 有 $\mu(x)>0$. 这样我们就证明了函数 $\varphi(x)$ 在区间 $[a, b]$ 上单调递减, 从而

$$
\varphi(a)>\varphi(b)
$$

即

$$
a^{a}-a^{b}>b^{a}-b^{b},
$$

原不等式成立.

综上所述,原不等式成立, 且等号当且仅当 $a=b$ 时取得.

构造合适的函数,利用函数的单调性简化问题.

## 第 897 题 规划中的换元

已知函数 $f(x)=\left(x^{2}+a x+b\right) \mathrm{e}^{x}$, 当 $b<1$ 时,函数 $f(x)$ 在 $(-\infty,-2)$ 和 $(1,+\infty)$ 上均为增函数,则 $\frac{a+b}{a-2}$ 的取值范围是

解析 $\left(-2, \frac{2}{3}\right]$.

对函数 $f(x)$ 求导得

$$
f^{\prime}(x)=\left[x^{2}+(a+2) x+(a+b)\right] \cdot \mathrm{e}^{x},
$$

由题意知二次函数 $y=x^{2}+(a+2) x+(a+b)$ 在 $(-\infty,-2)$ 与 $(1,+\infty)$ 上的函数值非负.

设 $m=a-2, n=a+b$, 则 $n-m=b+2<3$, 于是问题转化为

$$
\forall x \in(-\infty,-2) \cup(1,+\infty), g(x)=x^{2}+(m+4) x+n \geqslant 0,
$$

求 $\frac{n}{m}$ 的取值范围.

先考虑此二次函数的判别式

$$
\Delta=(m+4)^{2}-4 n>(m+4)^{2}-4(m+3)=(m+2)^{2} \geqslant 0,
$$

从而我们得到 $(m, n)$ 的限制条件为

$$
\left\{\begin{array}{l}
g(-2)=n-2 m-4 \geqslant 0 \\
g(1)=m+n+5 \geqslant 0 \\
n-m<3 \\
-2 \leqslant-\frac{m+4}{2} \leqslant 1
\end{array}\right.
$$

可行域如图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-309.jpg?height=470&width=418&top_left_y=1893&top_left_x=1463)

目标函数 $\frac{n}{m}$ 是可行域中的点 $(m, n)$ 的斜率, 求出交点即可得所求范围为 $\left(-2, \frac{2}{3}\right]$.

## 第 898 题 极值点排排队

函数 $f(x)=(x-a)^{2}(x+b) \mathrm{e}^{x}$, 其中 $a, b \in \mathbf{R}$.

(1) 当 $a=0, b=-3$ 时, 求函数 $f(x)$ 的单调区间;

(2) 当 $a=0$ 时, 若 $x=0$ 是 $f(x)$ 的极大值点, 求 $b$ 的取值范围;

(3) 若 $x=a$ 是 $f(x)$ 的极大值点, 设 $x_{1}, x_{2}, x_{3}$ 是 $f(x)$ 的 3 个极值点. 是否存在实数 $b$ 和 $x_{4}$, 使得 $x_{1}, x_{2}, x_{3}, x_{4}$ 的某个排列构成等差数列? 若存在, 求出所有的 $b$ 和对应的 $x_{4}$; 若不存在, 请说明理由.

解析 (1) 根据题意, 有

$$
f^{\prime}(x)=\mathrm{e}^{x} \cdot\left[2(x-a)(x+b)+(x-a)^{2}+(x-a)^{2}(x+b)\right],
$$

即

$$
f^{\prime}(x)=\mathrm{e}^{x} \cdot(x-a) \cdot\left[x^{2}+(-a+b+3) x-a b-a+2 b\right]
$$

关于 $x$ 的方程

$$
x^{2}+(-a+b+3) x-a b-a+2 b=0
$$

的判别式

$$
\Delta=(-a+b+3)^{2}-4(-a b-a+2 b)=(a+b-1)^{2}+8 .
$$

当 $a=0, b=-3$ 时, 有

$$
f^{\prime}(x)=\mathrm{e}^{x} \cdot x \cdot\left(x^{2}-6\right)
$$

于是函数 $f(x)$ 的单调递增区间是 $(-\sqrt{6}, 0)$ 和 $(\sqrt{6},+\infty)$, 单调递减区间是 $(-\infty,-\sqrt{6})$ 和 $(0, \sqrt{6})$.

(2) 当 $a=0$ 时,有

$$
f^{\prime}(x)=\mathrm{e}^{x} \cdot x \cdot\left[x^{2}+(b+3) x+2 b\right]
$$

由于 $\Delta>0$, 于是问题等价于关于 $x$ 的方程

$$
x^{2}+(b+3) x+2 b=0
$$

的两根分别位于 $x=0$ 两侧, 因此 $b$ 的取值范围是 $(-\infty, 0)$.

(3)根据题意, 不妨设

$$
x_{1}=\frac{a-b-3-\sqrt{\Delta}}{2}, x_{2}=\frac{a-b-3+\sqrt{\Delta}}{2}, x_{3}=a,
$$

记 $a=(1-\lambda) x_{1}+\lambda x_{2}$, 因为 $a$ 为极大值点, 所以 $a \in\left(x_{1}, x_{2}\right)$, 从而 $\lambda$ 的所有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-310.jpg?height=99&width=398&top_left_y=1840&top_left_x=1352)
可能取值为 $\frac{1}{3}, \frac{1}{2}, \frac{2}{3}$, 如图.

此时对应的方程为

$$
a=(1-\lambda) \cdot \frac{a-b-3-\sqrt{\Delta}}{2}+\lambda \cdot \frac{a-b-3+\sqrt{\Delta}}{2},
$$

即

$$
(a+b-1)+4=(2 \lambda-1) \sqrt{(a+b-1)^{2}+8}
$$

也即

$$
\left(\lambda^{2}-\lambda\right) t^{2}-2 t+8\left(\lambda^{2}-\lambda\right)-2=0
$$

解得

$$
t=\frac{1 \pm \sqrt{-8 m^{2}+2 m+1}}{m}
$$

其中 $t=a+b-1, m=\lambda^{2}-\lambda$. 而 $m$ 的所有可能取值为 $-\frac{2}{9},-\frac{1}{4}$, 于是所有可能的解为

$$
(\lambda, m, t)=\left(\frac{1}{3},-\frac{2}{9}, \frac{-9-\sqrt{13}}{2}\right),\left(\frac{2}{3},-\frac{2}{9}, \frac{-9+\sqrt{13}}{2}\right),\left(\frac{1}{2},-\frac{1}{4},-4\right)
$$

对应的 $b$ 和 $x_{4}$ 分别为

$$
\left(b, x_{4}\right)=\left(\frac{-7-\sqrt{13}}{2}-a, \frac{1+\sqrt{13}}{2}+a\right),\left(\frac{-7+\sqrt{13}}{2}-a, \frac{1-\sqrt{13}}{2}+a\right),(-3-a, \pm 2 \sqrt{6}+a) .
$$

注意在第一、第二种情况下, $a+x_{4}=x_{1}+x_{2}=a-b-3$, 在第三种情况下, $\left|x_{4}-a\right|=x_{2}-x_{1}=\sqrt{\Delta}=$ $\sqrt{t^{2}+8}=2 \sqrt{6}$, 由此可快速解出 $x_{4}$.

## 第 899 题 微妙的平衡

已知 $x \in\left(0, \frac{\pi}{2}\right)$.

(1)求证: $\sin x+\tan x>2 x$;

(2)求证: $2 \sin x+\tan x>3 x$.

解析 (1) 利用第 (2) 小题的结论, 有

$$
\sin x+\tan x+x>\sin x+\tan x+\sin x=2 \sin x+\tan x>3 x
$$

于是

$$
\sin x+\tan x>2 x,
$$

于是第(1)小题的结论得证.

(2) 令 $f(x)=2 \sin x+\tan x-3 x$, 则 $f(x)$ 的导函数

$$
f^{\prime}(x)=2 \cos x+\frac{1}{\cos ^{2} x}-3=\cos x+\cos x+\frac{1}{\cos ^{2} x}-3 \geqslant 0
$$

于是 $f(x)$ 在区间 $\left(0, \frac{\pi}{2}\right)$ 上单调递增, 因此 $f(x)>0$, 第 (2) 小题的结论得证.

用类似的方法, 容易得知当 $x \in\left(0, \frac{\pi}{2}\right)$ 时, 不等式 $3 \sin x+\tan x>4 x$ 不再恒成立.

## 第 900 题 按需构造

已知 $f(x)=\ln x-x^{2}+x$.

(1) 求函数 $f(x)$ 的单调区间;

(2) 证明: 当 $a \geqslant 2$ 时, 关于 $x$ 的不等式 $f(x)<\left(\frac{a}{2}-1\right) x^{2}+a x-1$ 恒成立;

(3) 若正实数 $x_{1}, x_{2}$ 满足

$$
f\left(x_{1}\right)+f\left(x_{2}\right)+2\left(x_{1}^{2}+x_{2}^{2}\right)+x_{1} x_{2}=0,
$$

证明: $x_{1}+x_{2}>\frac{\sqrt{5}-1}{2}$.
解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{2 x+1}{x} \cdot(1-x)
$$

于是函数 $f(x)$ 的单调递增区间是 $(0,1)$, 单调递减区间是 $(1,+\infty)$.

(2) 记 $g(x)=f(x)-\left(\frac{a}{2}-1\right) x^{2}-a x+1$, 则

$$
g(x)=\ln x-\frac{a}{2} x^{2}+(1-a) x+1, x>0,
$$

其导函数

$$
g^{\prime}(x)=\frac{x+1}{x} \cdot(1-a x)
$$

于是

$$
g(x) \leqslant g\left(\frac{1}{a}\right)=-\ln a+\frac{1}{2 a}
$$

由于要证明 $-\ln a+\frac{1}{2 a}<0$ 对 $a \geqslant 2$ 恒成立.

记函数 $\varphi(a)=-\ln a+\frac{1}{2 a}$, 其中 $a \geqslant 2$, 则其导函数

$$
\varphi^{\prime}(a)=-\frac{2 a+1}{2 a^{2}}<0
$$

于是 $\varphi(a)$ 单调递减，进而有

$$
\varphi(a) \leqslant \varphi(2)=-\ln 2+\frac{1}{4}=\frac{\ln \frac{\mathrm{e}}{16}}{4}<0
$$

于是原命题得证.

事实上, 只需要证明 $a=2$ 的情形即可.

(3)根据已知条件, 可得

$$
\left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{2}\right)-1=-1+x_{1} x_{2}-\ln x_{1} x_{2} .
$$

设 $\mu(x)=-1+x-\ln x$, 则其导函数

$$
\mu^{\prime}(x)=\frac{x-1}{x}
$$

于是可得 $\mu(x)$ 的最小值为 $\mu(1)=0$, 因此

$$
\left(x_{1}+x_{2}\right)^{2}+\left(x_{1}+x_{2}\right)-1 \geqslant 0
$$

解得 $x_{1}+x_{2}>\frac{\sqrt{5}-1}{2}$.

## 第 901 题 含参函数的最值

设函数 $f(x)=(x-1) \mathrm{e}^{x}-k x^{2}(k \in \mathbf{R})$.

(1) 当 $k=1$ 时,求函数 $f(x)$ 的单调区间;

(2) 当 $k \in\left(\frac{1}{2}, 1\right]$ 时, 求函数 $f(x)$ 在 $[0, k]$ 上的最大值 $M$.

解析 (1) 由题意可知, 函数 $f(x)=(x-1) \mathrm{e}^{x}-k x^{2}$, 其导函数

$$
\begin{aligned}
f^{\prime}(x) & =(x-1) \mathrm{e}^{x}+\mathrm{e}^{x}-2 k x \\
& =x \mathrm{e}^{x}-2 k x \\
& =x\left(\mathrm{e}^{x}-2 k\right)
\end{aligned}
$$

当 $k=1$ 时, 令 $f^{\prime}(x)=x\left(\mathrm{e}^{x}-2\right)=0$ 得

$$
x_{1}=0, x_{2}=\ln 2 ;
$$

当 $x<0$ 时, $f^{\prime}(x)>0$; 当 $0<x<\ln 2$ 时, $f^{\prime}(x)<0$; 当 $x>\ln 2$ 时, $f^{\prime}(x)>0$;

所以, 函数 $f(x)$ 的单调递增区间为 $(-\infty, 0)$ 和 $(\ln 2,+\infty)$, 单调递减区间为 $(0, \ln 2)$.

(2) 根据题意, 有 $f(x)$ 的导函数

$$
f^{\prime}(x)=x\left(\mathrm{e}^{x}-2 k\right)
$$

考虑到 $y=\mathrm{e}^{x}-2 k$ 在 $[0, k]$ 上单调递增, 因此需要考虑 $\mathrm{e}^{k}-2 k$ 的正负.

事实上, 有

$$
\left(e^{k}-2 k\right)^{\prime}=e^{k}-2,
$$

于是其极小值, 亦为最小值是

$$
\left.\left(\mathrm{e}^{k}-2 k\right)\right|_{k=\ln 2}=2-2 \ln 2>0,
$$

因此函数 $f(x)$ 在 $[0, k]$ 上先单调递减, 再单调递增, 其最大值为

$$
\max \{f(0), f(k)\}=\max \left\{-1,(k-1) \mathrm{e}^{k}-k^{3}\right\}
$$

作差比较,有

$$
\begin{aligned}
f(k)-f(0) & =(k-1) \mathrm{e}^{k}-k^{3}+1 \\
& =(1-k) \cdot \mathrm{e}^{k}\left[\mathrm{e}^{-k} \cdot\left(k^{2}+k+1\right)-1\right] .
\end{aligned}
$$

考虑到

$$
\left[\mathrm{e}^{-k} \cdot\left(k^{2}+k+1\right)\right]^{\prime}=\mathrm{e}^{-k} \cdot k(1-k) \geqslant 0
$$

于是

$$
\mathrm{e}^{-k}\left(k^{2}+k+1\right)>\left.\left[\mathrm{e}^{-k}\left(k^{2}+k+1\right)\right]\right|_{k=0}=1,
$$

所以有 $f(k)-f(0)>0$.

因此所求的最大值为 $M=(k-1) \mathrm{e}^{k}-k^{3}$.

## 第 902 题 按图索骥

已知 $f(x)$ 是定义在 $(0,+\infty)$ 上的可导函数, 满足 $f(x)>0$, 且 $f(x)+f^{\prime}(x)<0$.

(1) 讨论函数 $F(x)=\mathrm{e}^{x} f(x)$ 的单调性;

(2) 设 $0<x<1$, 比较 $x f(x)$ 与 $\frac{1}{x} f\left(\frac{1}{x}\right)$ 的大小.

解析 (1) 因为

$$
F^{\prime}(x)=\mathrm{e}^{x}\left[f(x)+f^{\prime}(x)\right]<0
$$

所以 $F(x)$ 在 $(0,+\infty)$ 上单调递减.

(2) 因为

$$
\frac{x f(x)}{\frac{1}{x} f\left(\frac{1}{x}\right)}=x^{2} \cdot \frac{f(x)}{f\left(\frac{1}{x}\right)}=\frac{x^{2} \cdot \mathrm{e}^{\frac{1}{x}}}{\mathrm{e}^{x}} \cdot \frac{\mathrm{e}^{x} f(x)}{\mathrm{e}^{\frac{1}{x}} f\left(\frac{1}{x}\right)}
$$

由 $f(x)$ 单调递减及 $x<\frac{1}{x}$, 得

$$
\mathrm{e}^{x} f(x)>\mathrm{e}^{\frac{1}{x}} f\left(\frac{1}{x}\right)
$$

当 $0<x<1$ 时, 记 $g(x)=2 \ln x+\frac{1}{x}-x$, 则

$$
g^{\prime}(x)=\frac{2}{x}-\frac{1}{x^{2}}-1=\frac{-(x-1)^{2}}{x^{2}}<0
$$

所以 $g(x)$ 是单调递减函数,故当 $0<x<1$ 时,

$$
g(x)>g(1)=0,
$$

即

$$
2 \ln x+\frac{1}{x}-x>0
$$

所以

$$
x^{2} \cdot \mathrm{e}^{\frac{1}{x}-x}>1
$$

综上所述，

$$
\frac{x f(x)}{\frac{1}{x} f\left(\frac{1}{x}\right)}>1
$$

也即

$$
x f(x)>\frac{1}{x} f(x)
$$

## 第 903 题 存在性与恒成立

已知 $f(x)=2 \ln (x+2)-(x+1)^{2}, g(x)=k(x+1)$.

(1) 求 $f(x)$ 的单调区间

(2) 当 $k=2$ 时,求证: $\forall x>-1, f(x)<g(x)$.

(3) 若存在 $x_{0}>-1$, 使得当 $x \in\left(-1, x_{0}\right)$ 时, 恒有 $f(x)>g(x)$ 成立, 试求 $k$ 的取值范围.

解析 (1) 根据题意, 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{2}{x+2}-2(x+1)=\frac{-2\left(x^{2}+3 x+1\right)}{x+2},
$$

因此函数 $f(x)$ 的单调递增区间是 $\left(-2, \frac{\sqrt{5}-3}{2}\right)$, 单调递减区间是 $\left(\frac{\sqrt{5}-3}{2},+\infty\right)$.

(2)欲证命题即

$$
\forall x>1,2 \ln x-(x-1)^{2}<2(x-1),
$$

也即

$$
\ln x<\frac{1}{2}\left(x^{2}-1\right)
$$

事实上,当 $x>1$ 时,我们有

$$
\ln x<x-1<(x-1) \cdot \frac{x+1}{2}=\frac{1}{2}\left(x^{2}-1\right),
$$

于是原命题成立.

(3)令

$$
h(x)=f(x)-g(x)=2 \ln x-(x-1)^{2}-k(x-1), x>1,
$$

则其导函数

$$
h^{\prime}(x)=\frac{2}{x}-2(x-1)-k=\frac{-2 x^{2}+(2-k) x+2}{x},
$$

于是 $h(1)=0, h^{\prime}(1)=2-k$,

因此 $k=2$ 为讨论的分界点.

情形 $-k \geqslant 2$. 根据第 $(2)$ 小题的结论, 有

$$
\forall x>1,2 \ln x-(x-1)^{2}-k(x-1) \leqslant 2 \ln x-(x-1)^{2}-2(x-1)<0 .
$$

情形二 $k<2$. 此时在区间 $\left(1, \frac{k-2-\sqrt{(2-k)^{2}+16}}{-4}\right)$ 上, 有 $h^{\prime}(x)>0, h(x)$ 单调递增, 结合 $h(1)=0$ 可得 $h(x)>0$.

综上所述, $k$ 的取值范围是 $(-\infty, 2)$.

## 第 904 题 必要条件探路

已知函数 $f(x)=\mathrm{e}^{x}+x^{2}-x, g(x)=x^{2}+a x+b$, 其中 $a, b$ 均为实数.

(1) 当 $a=1$ 时, 求函数 $F(x)=f(x)-g(x)$ 的单调区间;

(2) 若曲线 $y=f(x)$ 在点 $(0,1)$ 处的切线 $l$ 与曲线 $y=g(x)$ 切于点 $(1, c)$, 求 $a, b, c$ 的值;

(3) 若 $f(x) \geqslant g(x)$ 恒成立, 求 $a+b$ 的最大值.

解析 (1) 当 $a=1$ 时, 函数

$$
F(x)=f(x)-g(x)=\mathrm{e}^{x}-2 x-b,
$$

求导得 $F^{\prime}(x)=\mathrm{e}^{x}-2$,

所以 $F(x)$ 在 $(-\infty, \ln 2)$ 上单调递减, 在 $(\ln 2,+\infty)$ 上单调递增.

(2) 因为

$$
f^{\prime}(x)=\mathrm{e}^{x}+2 x-1, g^{\prime}(x)=2 x+a,
$$

所以由题意知

$$
\left\{\begin{array}{l}
g(1)=c=1+a+b \\
f^{\prime}(0)=0=g^{\prime}(1)=2+a=\frac{c-1}{1-0}=c-1
\end{array}\right.
$$

解得 $(a, b, c)=(-2,2,1)$.

(3) 因为

$$
f(x)-g(x)=\mathrm{e}^{x}-(a+1) x-b \geqslant 0
$$

先探索必要条件, 令 $x=1$ 得 $a+b \leqslant \mathrm{e}-1$.

如果 $a+b$ 可以取到 $\mathrm{e}-1$, 那么它就是所求最大值, 尝试构造:

若取 $(a, b)=(\mathrm{e}-1,0)$, 则

$$
f(x)-g(x)=\mathrm{e}^{x}-\mathrm{e} x \geqslant 0
$$

恒成立.

综上所述 $a+b$ 的最大值为 $\mathrm{e}-1$.
第 (3) 问常规做法如下.

因为

$$
f(x)-g(x)=\mathrm{e}^{x}-(a+1) x-b \geqslant 0
$$

恒成立,所以

$$
a+b \leqslant \mathrm{e}^{x}-(a+1) x+a
$$

恒成立, 令 $h(x)=\mathrm{e}^{x}-(a+1) x+a$, 要求 $h(x)$ 有最小值, 求导得

$$
h^{\prime}(x)=\mathrm{e}^{x}-(a+1)
$$

当 $a<-1$ 时, $x \rightarrow-\infty$ 时, 有 $h(x) \rightarrow-\infty, a+b$ 不可能取到最大值;

当 $a=-1$ 时, $x \rightarrow-\infty$ 时, 有 $h(x) \rightarrow-1$;

当 $a>-1$ 时, $h(x)$ 的最小值为

$$
h(\ln (a+1))=2 a+1-(a+1) \ln (a+1),
$$

下面求关于 $a$ 的函数

$$
m(a)=2 a+1-(a+1) \ln (a+1)
$$

的最大值即可,求导得

$$
m^{\prime}(a)=1-\ln (a+1),
$$

所以 $m(a)$ 的最大值为

$$
m(\mathrm{e}-1)=\mathrm{e}-1>-1,
$$

综上知 $a+b$ 的最大值为 $\mathrm{e}-1$. 此时 $a=\mathrm{e}-1, b=0$.

## 第 905 题 参数转化

已知 $f(x)=x-\frac{1}{x}-a \ln x$, 其中 $a \in \mathbf{R}$.

(1) 求 $f(x)$ 的单调区间;

(2) 当 $a \in\left[\frac{5}{2}, \frac{17}{4}\right]$ 时, 设 $f(x)$ 的极大值为 $M$, 极小值为 $N$, 求 $M-N$ 的取值范围.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{x^{2}-a x+1}{x^{2}}
$$

情形一 $a \leqslant 2$. 此时 $f(x)$ 的单调递增区间是 $(0,+\infty)$.

情形二 $a>2$. 此时 $f(x)$ 的单调递增区间是 $\left(0, x_{1}\right)$ 和 $\left(x_{2},+\infty\right)$, 单调递减区间是 $\left(x_{1}, x_{2}\right)$, 其中

$$
x_{1}=\frac{a-\sqrt{a^{2}-4}}{2}, x_{2}=\frac{a+\sqrt{a^{2}-4}}{2}
$$

(2)利用第(1)小题的结果,设关于 $x$ 的方程

$$
a=x+\frac{1}{x}
$$

的两根为 $x_{1}, x_{2}$ 且 $x_{1}<x_{2}$, 那么有

$$
x_{1}+x_{2}=a, x_{1} x_{2}=1
$$

且 $x_{2}$ 的取值范围是 $[2,4]$. 此时

$$
\begin{aligned}
M-N & =f\left(x_{1}\right)-f\left(x_{2}\right) \\
& =\left(x_{1}-\frac{1}{x_{1}}-a \ln x_{1}\right)-\left(x_{2}-\frac{1}{x_{2}}-a \ln x_{2}\right) \\
& =x_{1}-x_{2}+\frac{x_{1}-x_{2}}{x_{1} x_{2}}+a \ln \frac{x_{2}}{x_{1}} \\
& =2\left[\frac{1}{x_{2}}-x_{2}+\left(x_{2}+\frac{1}{x_{2}}\right) \ln x_{2}\right]
\end{aligned}
$$

其中用到了 $x_{1}=\frac{1}{x_{2}}$ 且 $a=x_{2}+\frac{1}{x_{2}}$. 设函数

$$
\varphi(x)=\frac{1}{x}-x+\left(x+\frac{1}{x}\right) \ln x
$$

则其导函数

$$
\varphi^{\prime}(x)=\frac{\left(x^{2}-1\right) \ln x}{x^{2}} \geqslant 0
$$

于是 $\varphi(x)$ 在 $(0,+\infty)$ 上单调递增, 因此所求的取值范围是 $[2 \varphi(2), 2 \varphi(4)]$, 即 $\left[5 \ln 2-3,17 \ln 2-\frac{15}{2}\right]$.

## 第 906 题 极值的存在性

已知函数 $f(x)=(x-a)^{2} \ln x, a \in \mathbf{R}$.

(1) 若 $a=3 \sqrt{\mathrm{e}}$, 求函数 $g(x)=\frac{f(x)}{x}$ 的单调区间;

(2) 若函数 $f(x)$ 既有极大值, 又有极小值,求实数 $a$ 的取值范围.

解析 (1) 函数 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{(x-3 \sqrt{\mathrm{e}})(x \ln x+x+3 \sqrt{\mathrm{e}} \ln x-3 \sqrt{\mathrm{e}})}{x^{2}},
$$

设 $\varphi(x)=x \ln x+x+3 \sqrt{\mathrm{e}} \ln x-3 \sqrt{\mathrm{e}}$, 则其导函数

$$
\varphi^{\prime}(x)=\ln x+\frac{3 \sqrt{\mathrm{e}}}{x}+2>1-\frac{1}{x}+\frac{3 \sqrt{\mathrm{e}}}{x}+2>0
$$

且注意到 $\varphi(\sqrt{\mathrm{e}})=0$, 因此可得函数 $g(x)$ 在 $(0, \sqrt{\mathrm{e}})$ 上单调递增, 在 $(\sqrt{\mathrm{e}}, 3 \sqrt{\mathrm{e}})$ 上单调递减, 在 $(3 \sqrt{\mathrm{e}},+\infty)$ 上单调递增.

(2)题意即 $f^{\prime}(x)$ 有两种变号零点 (由负到正,由正到负).

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{(x-a)(x+2 x \ln x-a)}{x}
$$

设 $\mu(x)=x+2 x \ln x$, 则其导函数

$$
\mu^{\prime}(x)=3+2 \ln x,
$$

于是函数 $\mu(x)$ 在 $\left(0, \mathrm{e}^{-\frac{3}{2}}\right)$ 上单调递减, 在 $\left(\mathrm{e}^{-\frac{3}{2}},+\infty\right)$ 上单调递增.

注意到

$$
\lim _{x \rightarrow 0} \mu(x)=0, \lim _{x \rightarrow+\infty} \mu(x)=+\infty
$$

且当 $a=1$ 时, $\mu(x)=a$ 的解恰为 $a$, 因此实数 $a$ 的取值范围是 $\left(\mu\left(\mathrm{e}^{-\frac{3}{2}}\right), 0\right) \cup(0,1) \cup(1,+\infty)$, 也即
$\left(-2 \mathrm{e}^{-\frac{3}{2}}, 0\right) \cup(0,1) \cup(1,+\infty)$.

思考与总结

第 (2) 问中,因为函数 $\mu(x)-a=x+2 x \ln x-a$ 先减后增, 且最小值为 $\mu\left(\mathrm{e}^{-\frac{3}{2}}\right)-a$, 对 $a$ 进行讨论: 若 $a$ $\leqslant 0$, 则 $x-a>0$, 从而有

$$
-a>0, \mu\left(\mathrm{e}^{-\frac{3}{2}}\right)-a<0
$$

若 $a>0$, 则 $x-a$ 在 $(0, a)$ 上为负, 在 $(a,+\infty)$ 上为正; 此时 $-a<0$, 所以 $\mu(x)-a$ 只有一个零点, 只要该零点不为 $a$, 即可保证 $f^{\prime}(x)$ 有两种变号零点, 得到 $a \neq 1$.

## 第 907 题 有关 $\max$ 不等式的处理技汅

若 $x, y>0$, 证明: $\max \left\{x^{y}, y^{x}\right\}>\frac{1}{2}$.

解析 不妨设 $x \leqslant y$. 当 $y \geqslant 1$ 时, 命题显然成立; 当 $0<x \leqslant y<1$ 时, 由于当 $y \rightarrow x$ 时, $x^{y}$ 和 $y^{x}$ 均趋于 $x^{x}$,且有

$$
x^{y} \leqslant x^{x} \leqslant y^{x}
$$

因此只需要证明

$$
x^{x}>\frac{1}{2}
$$

事实上, 考虑到

$$
\left(x^{x}\right)^{\prime}=\left(\mathrm{e}^{x \ln x}\right)^{\prime}=x^{x}(1+\ln x),
$$

于是当 $x=\frac{1}{\mathrm{e}}$ 时, $x^{x}$ 取得最小值为 $\left(\frac{1}{\mathrm{e}}\right)^{\frac{1}{e}}$.

接下来证明

$$
\left(\frac{1}{\mathrm{e}}\right)^{\frac{1}{\mathrm{e}}}>\frac{1}{2},
$$

用分析法, 只需要证明

$$
-\frac{1}{\mathrm{e}}>-\ln 2
$$

也即

$$
1<\ln 2^{\mathrm{e}}
$$

因此原命题得证.

利用不等式将有关 $\max$ 和 $\min$ 的函数进行放缩以减少变元, 这是处理此类函数的一般思路.

## 第 908 题 分离参数

设函数 $f(x)=\mathrm{e}^{x}(2 x-1)-a x+a$, 其中 $a<1$, 若存在唯一的整数 $x_{0}$ 使得 $f\left(x_{0}\right)<0$, 则 $a$ 的取值范围是
A. $\left[-\frac{3}{2 \mathrm{e}}, 1\right)$
B. $\left[-\frac{3}{2 \mathrm{e}}, \frac{3}{4}\right)$
C. $\left[\frac{3}{2 \mathrm{e}}, \frac{3}{4}\right)$
D. $\left[\frac{3}{2 \mathrm{e}}, 1\right)$

## 解析 D.

## 考虑将含参不等式

$$
\mathrm{e}^{x}(2 x-1)-a x+a<0
$$

分离为

$$
\mathrm{e}^{x}(2 x-1)<a(x-1)
$$

这样题意即曲线 $g(x)=\mathrm{e}^{x}(2 x-1)$ 在过定点 $(1,0)$ 且斜率为 $a$ 的直线 $y=a(x-1)$ 下方的部分在 $x$ 轴上的投影只包含唯一整数.

由于 $g(x)$ 的导函数

$$
g^{\prime}(x)=\mathrm{e}^{x}(2 x+1),
$$

于是 $g(x)$ 在 $x=-\frac{1}{2}$ 处取得极小值 $-\frac{2}{\sqrt{\mathrm{e}}}$, 如图. 结合图象可知, 符合题意的唯一整数为 0 .

设 $B(-1, g(-1)), C(0, g(0))$, 则 $a$ 的取值范围是从直线 $A B$ 的斜率到直线 $A C$ 斜

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-319.jpg?height=306&width=271&top_left_y=1106&top_left_x=1594)
率的左闭右开区间,也即 $\left[\frac{3}{2 \mathrm{e}}, 1\right)$.

## 第 909 题端点定乾坤

已知函数 $f(x)=\ln (1+x), g(x)=k x(k \in \mathbf{R})$.

(1) 证明: 当 $x>0$ 时, $f(x)<x$;

(2) 证明: 当 $k<1$ 时, 存在 $x_{0}>0$, 使得对任意的 $x \in\left(0, x_{0}\right)$, 恒有 $f(x)>g(x)$;

(3) 确定 $k$ 的所有可能取值, 使得存在 $t>0$, 对任意的 $x \in(0, t)$, 恒有 $|f(x)-g(x)|<x^{2}$.

解析 (1) 根据题意, 当 $x>0$ 时, 有

$$
(f(x)-x)^{\prime}=\frac{1}{1+x}-1=\frac{-x}{1+x}<0
$$

因此函数 $y=f(x)-x$ 在区间 $(0,+\infty)$ 上单调递减, 因此

$$
f(x)-x<f(0)-0=0
$$

原命题得证.

(2) 情形一 $\quad k \leqslant 0$.

取 $x_{0}=1$, 则在区间 $\left(0, x_{0}\right)$ 内, 恒有 $\ln (1+x)>0 \geqslant k x$, 命题成立.

情形ニ $0<k<1$.

考虑到

$$
(f(x)-g(x))^{\prime}=\frac{1}{x+1}-k
$$

于是当 $0<x<\frac{1}{k}-1$ 时必然有

$$
(f(x)-g(x))^{\prime}>0
$$

所以函数 $f(x)-g(x)$ 在 $\left(0, \frac{1}{k}-1\right)$ 上单调递增,

又 $f(0)-g(0)=0$, 于是取 $x_{0}=\frac{1}{k}-1$ 即可证明命题成立.

综上, 原命题得证.

(3) 根据题意在区间 $(0, t)$ 上, 有

$$
-x^{2}<f(x)-g(x)<x^{2}
$$

即

$$
\left\{\begin{array}{l}
\ln (1+x)-k x-x^{2}<0 \\
\ln (1+x)-k x+x^{2}>0
\end{array}\right.
$$

记 $h_{1}(x)=\ln (1+x)-k x-x^{2}, h_{2}(x)=\ln (1+x)-k x+x^{2}$,

此时注意到

$$
h_{1}(0)=h_{2}(0)=0
$$

于是考虑它们的导函数

$$
\begin{aligned}
& h_{1}^{\prime}(x)=\frac{1}{1+x}-k-2 x=-\frac{2 x^{2}+(2+k) x+k-1}{1+x} \\
& h_{2}^{\prime}(x)=\frac{1}{1+x}-k+2 x=\frac{2 x^{2}+(2-k) x-k+1}{1+x}
\end{aligned}
$$

注意到

$$
h_{1}^{\prime}(0)=h_{2}^{\prime}(0)=-k+1,
$$

于是按 $k$ 与 1 的大小讨论.

当 $k<1$ 时, 考虑函数 $h_{1}(x)$, 在区间 $\left(0, \frac{-(2+k)+\sqrt{(2+k)^{2}+8(1-k)}}{4}\right)$ 上有 $h_{1}^{\prime}(x)>0$, 于是 $h_{1}(x)$ 在该区间上单调递增, 从而在该区间上 $h_{1}(x)>h_{1}(0)=0$, 不符合题意;

当 $k>1$ 时, 考虑函数 $h_{2}(x)$, 在区间 $\left(0, \frac{-(2-k)+\sqrt{(2-k)^{2}+8(k-1)}}{4}\right)$ 上有 $h_{2}^{\prime}(x)<0$, 于是 $h_{2}(x)$ 在该区间上单调递减, 从而在该区间上 $h_{2}(x)<h_{2}(0)=0$, 不符合题意;

当 $k=1$ 时, 函数 $h_{1}(x)$ 和 $h_{2}(x)$ 的导函数分别为

$$
h_{1}^{\prime}(x)=-\frac{x(2 x+3)}{1+x}, h_{2}^{\prime}(x)=\frac{x(2 x+1)}{1+x}
$$

于是在区间 $(0,+\infty)$ 上有 $h_{1}^{\prime}(x)<0, h_{2}^{\prime}(x)>0$, 因此函数 $h_{1}(x)$ 单调递减, $h_{2}(x)$ 单调递增, 结合 $h_{1}(0)$ $=h_{2}(0)=0$, 有

$$
h_{1}(x)<0<h_{2}(x),
$$

符合题意.

综上, $k$ 的所有可能取值为 $k=1$.

## 第 910 题 引入参数

已知 $a, b$ 均为正实数, 且 $a^{4}+b^{2}=5$, 求 $a+b$ 的最大值.

## 解析 解法一 $^{2}$

先利用导数处理函数 $f(x)=x+\sqrt{5-x^{4}} . f(x)$ 的定义域为 $\left[-5^{\frac{1}{4}}, 5^{\frac{1}{4}}\right]$.

当 $x<0$ 时, $f(x)$ 单调递增;

当 $x \geqslant 0$ 时,导函数

$$
f^{\prime}(x)=1+\frac{1}{2}\left(5-x^{4}\right)^{-\frac{1}{2}} \cdot\left(-4 x^{3}\right)=\frac{1}{\sqrt{5-x^{4}}} \cdot\left(\sqrt{5-x^{4}}-2 x^{3}\right)
$$

令

$$
g(x)=\sqrt{5-x^{4}}-2 x^{3}, x \geqslant 0,
$$

则 $g(x)$ 单调递减, 且有唯一零点为 $x=1$.

于是函数 $f(x)$ 在 $x=1$ 处取得极大值, 亦为最大值 3 .

当然, 我们也可以求出 $f(x)$ 的最小值, 函数在定义域区间端点处取得最小值,经比较可得最小值为

$$
\left.y\right|_{x=-5} \frac{1}{4}=-5^{\frac{1}{4}}
$$

从而我们得到函数的值域为 $\left[-5^{\frac{1}{4}}, 3\right]$.

解法二 我们知道, 如果已知 $a^{2}+b^{2}=5$, 求 $a+b$ 的最大值, 可以通过

$$
a+b=1 \cdot a+1 \cdot b \leqslant \sqrt{1^{2}+1^{2}} \cdot \sqrt{a^{2}+b^{2}}
$$

求得,但这里是 $a^{4}$, 就需要引人参数借助二次函数求最值了.

$$
\begin{aligned}
a+b & =\frac{1}{\lambda} \cdot \lambda a+1 \cdot b \\
& \leqslant \sqrt{\left(\frac{1}{\lambda}\right)^{2}+1^{2}} \cdot \sqrt{(\lambda a)^{2}+b^{2}} \\
& =\sqrt{\frac{1}{\lambda^{2}}+1} \cdot \sqrt{\lambda^{2} a^{2}+5-a^{4}} \\
& =\sqrt{\frac{1}{\lambda^{2}}+1} \cdot \sqrt{-\left(a^{2}-\frac{1}{2} \lambda^{2}\right)^{2}+5+\frac{1}{4} \lambda^{4}} \\
& \leqslant \sqrt{\frac{1}{\lambda^{2}}+1} \cdot \sqrt{5+\frac{1}{4} \lambda^{4}},
\end{aligned}
$$

其中等号取得的条件为

$$
\left\{\begin{array}{l}
\frac{1}{\lambda}=\frac{\lambda a}{b} \\
a^{4}+b^{2}=5 \\
a^{2}=\frac{1}{2} \lambda^{2}
\end{array}\right.
$$

解得

$$
a=1, b=2, \lambda=\sqrt{2},
$$

于是所求代数式的最大值为

$$
\left.\sqrt{\frac{1}{\lambda^{2}}+1} \cdot \sqrt{5+\frac{1}{4} \lambda^{4}}\right|_{\lambda=\sqrt{2}}=3
$$

## 第 911 题 清君侧,部国难

已知 $f(x)=\frac{1+\ln x}{x-1}, g(x)=\frac{k}{x}\left(k \in \mathbf{N}^{*}\right)$. 若对任意 $c>1$, 均存在 $a, b$ 满足 $0<a<b<c$, 使得 $f(c)=$ $f(a)=g(b)$, 则 $k$ 的最大值为

解析 3.

先研究函数 $f(x)$, 其导函数

$$
f^{\prime}(x)=-\frac{1+x \ln x}{x(x-1)^{2}}
$$

又

$$
(1+x \ln x)^{\prime}=1+\ln x
$$

于是 $1+x \ln x$ 的最小值为

$$
1+\frac{1}{\mathrm{e}} \cdot \ln \frac{1}{\mathrm{e}}>0
$$

因此 $f(x)$ 在 $(0,1)$ 和 $(1,+\infty)$ 上分别单调递减.

根据题意, 函数 $g(x)=\frac{k}{x}$ 的图象夹在 $f(x)$ 图象在 $x<1$ 和 $x>1$ 的两个部分之间，也即

$$
\left\{\begin{array}{l}
\forall x \in(0,1), \frac{k}{x}>\frac{1+\ln x}{x-1} \\
\forall x \in(1,+\infty), \frac{k}{x}<\frac{1+\ln x}{x-1}
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-322.jpg?height=303&width=355&top_left_y=1110&top_left_x=1412)

即

$$
\forall x>0, x \neq 1,1+\ln x>\frac{k(x-1)}{x}
$$

也即

$$
\forall x>0, x \neq 1,1+\ln x+\frac{k}{x}-k>0,
$$

设不等式左边函数为 $h(x)$, 则 $h(x)$ 的导函数

$$
h^{\prime}(x)=\frac{x-k}{x^{2}}
$$

于是当 $x=k$ 时, $h(x)$ 有最小值

$$
h(k)=\ln k-k+2>0
$$

由

$$
(\ln k-k+2)^{\prime}=\frac{1}{k}-1 \leqslant 0
$$

于是 $h(k)$ 随着正整数 $k$ 的增大而减小, 不难验证得知 $k$ 的最大值为 3 .

从此题中可以看到, 处理包含对数函数 $\ln x$ 的问题时, 可以考虑先将与 $\ln x$ 相乘的因式消灭 (即“清君侧”), 从而避免求导后仍然包含对数符号而需要再次求导的问题(即“靖国难”).

## 第 912 题 柿子挑软的捏

已知函数 $f(x)=-\frac{\ln x}{x}+\mathrm{e}^{a x-1}$ 的最小值为 $a$, 求 $a$ 的最小值.

解析 由 $f(x) \geqslant a$ 知

$$
x \cdot \mathrm{e}^{a x-1}-\ln x-a x \geqslant 0
$$

令 $g(x)=x \mathrm{e}^{a x-1}-a x-\ln x$, 根据题意 $g(x)$ 的最小值为 0 .

考虑 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{1}{x}(a x+1)\left(x \mathrm{e}^{a x-1}-1\right)
$$

当 $a=0$ 时, 有

$$
g^{\prime}(x)=\frac{1}{x}\left(x \mathrm{e}^{-1}-1\right)
$$

于是 $g(x)$ 在 $x=\mathrm{e}$ 处取得极小值, 同时亦为最小值 $g(\mathrm{e})=0$, 符合题意.

同时, 由于 $a=0$ 时符合题意,因此无需考虑 $a>0$ 的情形.

当 $a<0$ 时, 设 $h(x)=x \mathrm{e}^{a x-1}-1$, 则 $h(x)$ 的导函数

$$
h^{\prime}(x)=(a x+1) \mathrm{e}^{a x-1},
$$

于是 $h(x)$ 在 $x=-\frac{1}{a}$ 处取得极大值, 同时也为最大值 $-\frac{1}{a}\left(\mathrm{e}^{-2}+a\right)$.

接下来考虑 $a=-\mathrm{e}^{-2}$ 的情形. 此时 $g^{\prime}(x)$ 有唯一零点 $x=\mathrm{e}^{2}$, 同时为 $g(x)$ 的极小值点, 亦为最小值点, 此时 $g(x)$ 的最小值为 $g\left(\mathrm{e}^{2}\right)=0$, 符合题意.

同时, 由于 $a=-\mathrm{e}^{-2}$ 时符合题意,因此无需考虑 $a>-\mathrm{e}^{-2}$ 的情形.

当 $a<-\mathrm{e}^{-2}$ 时, $h(x)<0$, 因此 $g^{\prime}(x)$ 有唯一零点 $x=-\frac{1}{a}$, 同时为 $g(x)$ 的极小值点, 亦为最小值点, 此时 $g(x)$ 的最小值为

$$
g\left(-\frac{1}{a}\right)=-\frac{1}{a} \cdot \mathrm{e}^{-2}+1-\ln \left(-\frac{1}{a}\right)=-\frac{1}{a} \cdot \mathrm{e}^{-2}-\ln \left(-\frac{1}{a} \cdot \mathrm{e}^{-2}\right)-1>0,
$$

其中用到了常用对数不等式

$$
\forall x \in(0,1), \ln x<x-1,
$$

不符合题意.

综上所述, $a$ 的最小值为 $-\mathrm{e}^{-2}$.

## 第 913 题 头转星移

已知函数 $f(x)=a x^{3}+b x^{2}+c x+d$ 在 $O, A$ 两点处取得极值, 其中 $O$ 是坐标原点, 点 $A$ 在曲线 $y=$ $x^{2} \sin x+x \cos x\left(x \in\left[\frac{\pi}{3}, \frac{2 \pi}{3}\right]\right)$ 上, 则曲线 $y=f(x)$ 的切线的斜率的最大值是

解析 $\frac{3 \pi}{4}$.
根据已知, $f(x)$ 的导函数 $f^{\prime}(x)=3 a x^{2}+2 b x+c$.

由于函数 $f(x)$ 在点 $O$ 处取得极值, 于是

$$
f(0)=f^{\prime}(0)=0,
$$

即 $c=d=0$, 因此

$$
f(x)=a x^{3}+b x^{2}
$$

由于点 $A$ 必然位于第一象限, 因此 $a<0$.

曲线 $y=f(x)$ 的切线的斜率的最大值, 即 $f^{\prime}(x)$ 的最大值, 为

$$
\max (k)=-\frac{b^{2}}{3 a}
$$

因此接下来的任务是建立 $\max (k)$ 与 $A$ 点的联系. 不难求得 $A$ 点的坐标为 $\left(-\frac{2 b}{3 a}, \frac{4 b^{3}}{27 a^{2}}\right)$, 因此直线 $O A$的斜率

$$
k_{\triangle A}=-\frac{2 b^{2}}{9 a}=\frac{2}{3} \max (k)
$$

于是只要求出 $k_{o A}$ 的最大值即可.

由于点 $A$ 在曲线 $y=x^{2} \sin x+x \cos x\left(x \in\left[\frac{\pi}{3}, \frac{2 \pi}{3}\right]\right)$ 上, 设点 $A$ 的横坐标为 $x$, 则

$$
k_{\text {CA }}=g(x)=x \sin x+\cos x,
$$

其导函数

$$
g^{\prime}(x)=x \cos x
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-324.jpg?height=369&width=484&top_left_y=936&top_left_x=1310)

于是当 $x=\frac{\pi}{2}$ 时, $k_{0 A}$ 取得最大值为 $g\left(\frac{\pi}{2}\right)=\frac{\pi}{2}$, 进而可知所求的最大值为 $\frac{3 \pi}{4}$.

## 第 914 题回到原点

若函数 $f(x)=x \ln x-a x^{2}-x+1$ 存在最大值, 求 $a$ 的取值范围.

解析 考虑 $f(x)$ 的导函数

$$
f^{\prime}(x)=\ln x-2 a x=x\left(\frac{\ln x}{x}-2 a\right),
$$

考虑函数 $y=\frac{\ln x}{x}$ 与直线 $y=2 a$ 的交点情况, 如图.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-324.jpg?height=199&width=393&top_left_y=1824&top_left_x=1399)

这里用到了 $\left(\frac{\ln x}{x}\right)^{\prime}=\frac{1-\ln x}{x^{2}}$.

当 $2 a \geqslant \frac{1}{\mathrm{e}}$ 时, $f^{\prime}(x) \leqslant 0$,无最大值;

当 $0<2 a<\frac{1}{\mathrm{e}}$ 时, 设两个交点满足

$$
0<x_{1}<\mathrm{e}<x_{2}
$$

则函数 $f(x)$ 有最大值只需要

$$
f\left(x_{2}\right) \geqslant \lim _{x \rightarrow 0^{+}} f(x)=1,
$$

即

$$
x_{2} \ln x_{2}-a x_{2}^{2}-x_{2}+1 \geqslant 1,
$$

由 $\frac{\ln x_{2}}{x_{2}}=2 a$, 于是上述不等式即

$$
x_{2} \geqslant \frac{1}{a}
$$

由于函数 $y=\frac{\ln x}{x}$ 在 $x>\mathrm{e}$ 上是单调递减函数,因此上述不等式等价于

$$
2 a=\frac{\ln x_{2}}{x_{2}} \leqslant-a \ln a,
$$

解得 $a \leqslant \frac{1}{\mathrm{e}^{2}}$. 因此所求 $a$ 的取值范围是 $\left(0, \frac{1}{\mathrm{e}^{2}}\right]$.

其中用到了 $\lim _{x \rightarrow 0+} x \ln x=0$, 该极限等价于

$$
\lim _{x \rightarrow+\infty} \frac{\ln x}{x}=0
$$

可以通过 $0<\frac{\ln x}{x}<\frac{\sqrt{x}}{x}$ 证明.

## 第 915 题 曲线救国

若对任意 $x \in[-2,1]$ 均有 $a x^{3}-x^{2}+4 x+3 \geqslant 0$, 则 $a$ 的取值范围是

解析 $[-6,-2]$.

解法一 原命题等价于

$$
\left\{\begin{array}{l}
\forall x \in(0,1], a \geqslant-\frac{3}{x^{3}}-\frac{4}{x^{2}}+\frac{1}{x} \\
\forall x \in[-2,0), a \leqslant-\frac{3}{x^{3}}-\frac{4}{x^{2}}+\frac{1}{x}
\end{array}\right.
$$

也即

$$
\left\{\begin{array}{l}
\forall x \geqslant 1, a \geqslant-3 x^{3}-4 x^{2}+x \\
\forall x \leqslant-\frac{1}{2}, a \geqslant-3 x^{3}-4 x^{2}+x
\end{array}\right.
$$

记函数 $f(x)=-3 x^{3}-4 x^{2}+x$, 则其导函数 $f^{\prime}(x)=-(9 x-1)(x+1)$,于是函数 $f(x)$ 在 $[1,+\infty)$ 上的最大值为 $f(1)=-6$; 在 $\left(-\infty,-\frac{1}{2}\right]$ 上的最小值为 $f(-1)=-2$.

因此 $a$ 的取值范围是 $[-6,-2]$.

解法二 设 $f(x)=a x^{3}-x^{2}+4 x+3$, 则

$$
\left\{\begin{array}{l}
f(-2)=-8 a-9 \geqslant 0 \\
f(1)=a+6 \geqslant 0
\end{array}\right.
$$

解得 $-6 \leqslant a \leqslant-\frac{9}{8}$. 考虑函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=3 a x^{2}-2 x+4,
$$

可得 $f^{\prime}(x)$ 在区间 $[-2,1]$ 上存在两个不同零点, 因此只需要这两个极值点处满足不等式即符合题意.记极值点为 $m$, 则

$$
3 a m^{2}-2 m+4=0
$$

于是

$$
3 f(m)=3 a^{3}-3 m^{2}+12 m+9=\left(2 m^{2}-4 m\right)-3 m^{2}+12 m+9=(9-m)(m+1)
$$

因此只需要 $m \geqslant-1$, 也即 $f^{\prime}(-1)=3 a+6 \leqslant 0$, 从而 $a \leqslant-2$.

综上所述, $a$ 的取值范围是 $[-6,-2]$.

## 思考与总结

在处理不等式时, 将判断 $a$ 转化为判断 $m$ 是解决问题的关键.

## 第 916 题 一数之差

已知函数 $f(x)=\ln (a x+1)+\frac{1-x}{1+x}(x \geqslant 0, a>0)$.

(1) 若 $f(x)$ 的最小值为 1 , 求实数 $a$ 的取值范围;

(2) 若 $f(x)$ 的最小值为 $\ln 2$, 求实数 $a$ 的取值范围.

解析 解法一 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{a x^{2}+a-2}{(a x+1)(1+x)^{2}}
$$

注意到 $f(0)=1$, 因此 $f^{\prime}(0) \geqslant 0$, 从而 $a \geqslant 2$, 否则在 $\left(0, \sqrt{\frac{2-a}{a}}\right)$ 上, $f(x)$ 单调递减,

又 $f(0)=1$, 不符合题意.

当 $a \geqslant 2$ 时, 有 $f(x)$ 在 $(0,+\infty)$ 上单调递增, 符合题意.

综上所述, 实数 $a$ 的取值范围是 $[2,+\infty)$.

(2)根据题意，有

$$
\forall x>0, a \geqslant \frac{2 \mathrm{e}^{\frac{x-1}{x+1}}-1}{x}
$$

且等号可以取得. 设右侧函数为 $\varphi(x)$, 则其导函数

$$
\varphi^{\prime}(x)=\frac{1-\mathrm{e}^{\frac{x-1}{x+1}} \cdot\left[1+\left(\frac{x-1}{x+1}\right)^{2}\right]}{x^{2}},
$$

令 $t=\frac{x-1}{x+1}$, 则 $t \in[-1,1)$, 设 $\mu(t)=\mathrm{e}^{t}\left(1+t^{2}\right)$, 则其导函数

$$
\mu^{\prime}(t)=\mathrm{e}^{t}(t+1)^{2} \geqslant 0
$$

于是 $\mu(t)$ 在 $[-1,1)$ 上单调递增, 结合 $\mu(0)=1$, 可得 $\varphi(x)$ 在 $(0,1)$ 上单调递增 (因为 $x \in(0,1)$ 时, $t \in$ $(-1,0)$, 从而有 $\mu(t)<\mu(0)=1$, 所以 $\varphi^{\prime}(x)>0$ ), 在 $(1,+\infty)$ 上单调递减 (因为 $x \in(1,+\infty)$ 时, $t \in(0,1)$,从而有 $\mu(t)>\mu(0)=1$, 所以 $\left.\varphi^{\prime}(x)<0\right)$, 且有极大值, 亦最大值 $\varphi(1)=1$.

因此 $a$ 的取值范围为 $\{1\}$.

解法二 (1) 见解法一.

(2)根据 (1), 必然有 $0<a<2$. 此时 $f(x)$ 的极小值, 亦为最小值为

$$
m=f\left(\sqrt{\frac{2-a}{a}}\right)=\ln (\sqrt{a(2-a)}+1)+\frac{\sqrt{a}-\sqrt{2-a}}{\sqrt{a}+\sqrt{2-a}}
$$

设 $t=\sqrt{a(2-a)}$, 则 $t \in(0,1]$.
情形一 当 $0<a<1$ 时, 有

$$
m=\ln (t+1)-\frac{\sqrt{2-2 t}}{\sqrt{2+2 t}}<\ln (t+1) \leqslant \ln 2,
$$

不符合题意.

情形二 当 $a \geqslant 1$ 时,有

$$
m=\ln (t+1)+\frac{\sqrt{2-2 t}}{\sqrt{2+2 t}}=\ln (t+1)+\frac{\sqrt{1-t}}{\sqrt{1+t}}
$$

有

$$
m^{\prime}=\frac{1}{t+1}\left[1-\frac{1}{2}\left(\frac{\sqrt{1+t}}{\sqrt{1-t}}+\frac{\sqrt{1-t}}{\sqrt{1+t}}\right)\right] \leqslant 0
$$

于是 $m$ 在 $(0,1]$ 上单调递减, 因此 $m \geqslant\left. m\right|_{t=1}=\ln 2$, 等号当且仅当 $t=1$, 即 $a=1$ 时取得.综上所述, 实数 $a$ 的取值范围是 $\{1\}$.

## 第 917 题 披着羊皮的狼

已知函数 $y=\left(a \cos ^{2} x-3\right) \sin x$ 的最小值为 -3 , 求 $a$ 的取值范围.

解析 问题即函数 $f(x)=-a x^{3}+(a-3) x$ 在区间 $[-1,1]$ 上的最小值为 -3 . 函数 $f(x)$ 的导函数为

$$
f^{\prime}(x)=-3 a x^{2}+(a-3)
$$

注意到 $f(1)=-3$, 于是 $f^{\prime}(1) \leqslant 0$, 可得 $a \geqslant-\frac{3}{2}$.

情形一 $-\frac{3}{2} \leqslant a \leqslant 3$.

此时恒有 $f^{\prime}(x) \leqslant 0$,函数 $f(x)$ 在区间 $[-1,1]$ 上单调递减, 符合题意.

情形ニ $a>3$.

此时函数 $f(x)$ 在区间 $[-1,1]$ 上有极小值点 $x=-\sqrt{\frac{a-3}{3 a}}$, 于是根据题意, 有

$$
f\left(-\sqrt{\frac{a-3}{3 a}}\right) \geqslant-3
$$

即

$$
-\frac{2(a-3)}{3} \cdot \sqrt{\frac{a-3}{3 a}} \geqslant-3
$$

整理得 $(a-12)\left(4 a^{2}+12 a+9\right) \leqslant 0$, 解得 $a \leqslant 12$.

综上所述, $a$ 的取值范围是 $\left[-\frac{3}{2}, 12\right]$.

## 第 918 题形异神似

已知函数 $f(x)=x^{2} \mathrm{e}^{x}-\ln x, g(x)=\left(\frac{2}{x}-1\right) \ln (x-2)+\frac{\ln x-1}{x}+1$, 求证: $f(x)$ 的最小值与 $g(x)$的最大值相等.
解析 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}\left(x^{2}+2 x\right)-\frac{1}{x}
$$

于是其极小值点 $x=m$ 满足

$$
\mathrm{e}^{m}\left(m^{2}+2 m\right)-\frac{1}{m}=0
$$

也即

$$
m+2 \ln m+\ln (m+2)=0
$$

函数 $f(x)$ 的极小值, 亦为最小值

$$
f(m)=m^{2} \mathrm{e}^{m}-\ln m=m^{2} \cdot \frac{1}{m^{2}(m+2)}-\ln m=\frac{1}{m+2}-\ln m
$$

另一方面, 令 $t=x-2>0$, 函数 $g(x)$ 的最大值即函数

$$
h(x)=\frac{-x \ln x+\ln (x+2)+x+1}{x+2}
$$

的最大值.

函数 $h(x)$ 的导函数

$$
h^{\prime}(x)=-\frac{x+2 \ln x+\ln (x+2)}{(x+2)^{2}}
$$

于是其极大值点 $x=n$ 满足

$$
n+2 \ln n+\ln (n+2)=0
$$

函数 $h(x)$ 的极大值, 亦为最大值

$$
\begin{aligned}
h(n) & =\frac{-n \ln n+\ln (n+2)+n+1}{n+2} \\
& =\frac{-n \ln n+(-n-2 \ln n)+n+1}{n+2} \\
& =\frac{1}{n+2}-\ln n .
\end{aligned}
$$

由于函数 $\varphi(x)=x+2 \ln x+\ln (x+2)$ 单调递增, 于是 $m=n$, 进而原命题得证.

## 第 919 题 先探索再证明

是否存在正整数 $a$, 使得 $\mathrm{e}^{x}-a x \geqslant x^{2} \ln x$ 对一切 $x>0$ 恒成立 $?$ 若存在, 求出 $a$ 的最大值; 若不存在, 请说明理由.

解析 令 $x=2$, 可得

$$
\mathrm{e}^{2}-2 a \geqslant 4 \ln 2
$$

于是 $a \leqslant \frac{1}{2} \mathrm{e}^{2}-2 \ln 2<3$.

下面证明 $a=2$ 时符合题意, 只需要证

$$
\forall x>0, \mathrm{e}^{x}-2 x \geqslant x^{2} \ln x,
$$

也即

$$
\forall x>0, \frac{\mathrm{e}^{x}}{x^{2}}-\frac{2}{x}-\ln x>0
$$

令 $\varphi(x)=\frac{\mathrm{e}^{x}}{x^{2}}-\frac{2}{x}-\ln x$, 则

$$
\varphi^{\prime}(x)=\frac{(x-2)\left(\mathrm{e}^{x}-x\right)}{x^{3}}
$$

于是 $\varphi(x)$ 的极小值, 亦为最小值

$$
\varphi(2)=\frac{1}{4} \mathrm{e}^{2}-1-\ln 2>0
$$

符合题意.

综上所述, 正整数 $a$ 的最大值为 2 .

主一 令 $x=1$ 可得 $a \leqslant e<3$;

注二 其中估算可以利用 $\frac{19}{7}<\mathrm{e}<\frac{20}{7}, \frac{2}{3}<\ln 2<\frac{3}{4}$.

## 第 920 题 构造函数证明不等式

(1) 求函数 $f(x)=x \ln x-(1-x) \ln (1-x)$ 在 $0<x \leqslant \frac{1}{2}$ 上的最大值.

(2) 已知 $0<x<1$, 求证: $x^{1-x}+(1-x)^{x} \leqslant \sqrt{2}$.

和杖 (1) 根据题意, 有

$$
f^{\prime}(x)=2+\ln \left(x-x^{2}\right)
$$

于是函数 $f(x)$ 在 $\left(0, \frac{1}{2}\right)$ 先单调递减, 再单调递增. 考虑到

$$
\lim _{x \rightarrow 0^{+}} f(x)=f\left(\frac{1}{2}\right)=0
$$

于是 $f(x)$ 的最大值为 0 , 当 $x=\frac{1}{2}$ 时取得.

(2) 记不等式左边为 $g(x)$, 则显然 $g(x)$ 关于 $x=\frac{1}{2}$ 对称, 且 $g\left(\frac{1}{2}\right)=\sqrt{2}$, 因此只需要证明函数 $g(x)$ 在 $\left(0, \frac{1}{2}\right]$ 上的最大值为 $g\left(\frac{1}{2}\right)$ 即可.

令 $h(x)=x^{1-x}$, 则

$$
h^{\prime}(x)=\left(\mathrm{e}^{(1-x) \ln x}\right)^{\prime}=x^{1-x} \cdot\left[-\ln x+(1-x) \cdot \frac{1}{x}\right]=\frac{1-x-x \ln x}{x^{x}}
$$

这样就有

$$
\begin{aligned}
g^{\prime}(x) & =(h(x)+h(1-x))^{\prime} \\
& =h^{\prime}(x)-h^{\prime}(1-x) \\
& =\frac{1-x-x \ln x}{x^{x}}-\frac{1-(1-x)-(1-x) \ln (1-x)}{(1-x)^{1-x}}
\end{aligned}
$$

可得当 $0<x \leqslant \frac{1}{2}$ 时, 有

$$
x \ln x-(1-x) \ln (1-x) \leqslant 0
$$

于是当 $0<x \leqslant \frac{1}{2}$ 时, 有

$$
-x \ln x \geqslant-(1-x) \ln (1-x),
$$

进而有

$$
1-x-x \ln x \geqslant 1-x-(1-x) \ln (1-x) \geqslant 1-(1-x)-(1-x) \ln (1-x)
$$

而当 $0<x<1$ 时, 有

$$
1-x-x \ln x>0,
$$

这样就得到了当 $0<x \leqslant \frac{1}{2}$ 时, 有

$$
1-x-x \ln x \geqslant 1-(1-x)-(1-x) \ln (1-x)>0
$$

另一方面, 当 $0<x \leqslant \frac{1}{2}$ 时, 有

$$
\mathrm{e}^{x \ln x} \leqslant \mathrm{e}^{(1-x) \ln (1-x)},
$$

即

$$
0<x^{x} \leqslant(1-x)^{(1-x)}
$$

综上, 有当 $0<x \leqslant \frac{1}{2}$ 时

$$
g^{\prime}(x)=\frac{1-x-x \ln x}{x^{x}}-\frac{1-(1-x)-(1-x) \ln (1-x)}{(1-x)^{1-x}} \geqslant 0
$$

进而可得 $g(x)$ 在 $\left(0, \frac{1}{2}\right]$ 上的最大值为 $g\left(\frac{1}{2}\right)=\sqrt{2}$, 原命题得证.

事实上,有不等式

$$
x^{1-x}+(1-x)^{x} \leqslant \sqrt{x}+\sqrt{1-x} \leqslant \sqrt{2}
$$

成立.

## 第 921 题 $\quad$ 该分离时就分离

已知 $(x-a)^{2} \cdot \ln x \leqslant 4 \mathrm{e}^{2}$ 对任意 $x \in(0,3 \mathrm{e}]$ 恒成立, 求 $a$ 的取值范围.

解析 题意即

$$
\forall x \in(1,3 \mathrm{e}],|x-a| \leqslant \frac{2 \mathrm{e}}{\sqrt{\ln x}}
$$

也即

$$
\forall x \in(1,3 \mathrm{e}],-\frac{2 \mathrm{e}}{\sqrt{\ln x}}+x \leqslant a \leqslant \frac{2 \mathrm{e}}{\sqrt{\ln x}}+x
$$

设左侧函数为 $f(x)$, 右侧函数为 $g(x)$.

一方面, $f(x)$ 单调递增, 在 $(1,3 \mathrm{e}]$ 上的最大值为

$$
f(3 e)=3 e^{-}-\frac{2 \mathrm{e}}{\sqrt{1+\ln 3}}
$$

另一方面, $g(x)$ 的导函数

$$
g^{\prime}(x)=1-\frac{2 \mathrm{e}}{2 x \ln x \cdot \sqrt{\ln x}}
$$

于是 $g(x)$ 在 $x=\mathrm{e}$ 处取得最小值

$$
g(\mathrm{e})=3 \mathrm{e} .
$$

因此 $a$ 的取值范围是 $\left[3 \mathrm{e}-\frac{2 \mathrm{e}}{\sqrt{1+\ln 3}}, 3 \mathrm{e}\right]$.

## 第 922 题 放缩与估计

设函数 $f(x)=\mathrm{e}^{x}-x, g(x)=-k x^{3}+k x^{2}-x+1$.

(1) 求 $f(x)$ 的最小值;

(2) 若使得对任意 $x \in[0,1]$ 均有 $f(x) \geqslant g(x)$ 成立的 $k$ 的最大值为 $\lambda$, 求证: $5<\lambda<5.2$.

## 解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}-1,
$$

于是当 $x=0$ 时, $f(x)$ 取得极小值, 亦为最小值 $f(0)=1$.

(2)题意等价于

$$
\forall x \in(0,1), k \leqslant \frac{\mathrm{e}^{x}-1}{x^{2}-x^{3}}
$$

记右侧函数为 $\varphi(x)$, 于是 $\lambda$ 为 $\varphi(x)$ 在 $(0,1)$ 上的下确界.

一方面, 有

$$
\lambda \leqslant \varphi\left(\frac{1}{2}\right)=8(\sqrt{\mathrm{e}}-1)<5.2
$$

另一方面,考虑证明在 $x \in(0,1)$ 上, 有 $\varphi(x)>5$, 即

$$
\forall x \in(0,1), \mathrm{e}^{x} \geqslant 5 x^{2}-5 x^{3}+1
$$

事实上,容易证明

$$
\forall x \in(0,1), \mathrm{e}^{x}>1+x+\frac{1}{2} x^{2}+\frac{1}{6} x^{3},
$$

因此只需要证明

$$
\forall x \in(0,1), 1+x+\frac{1}{2} x^{2}+\frac{1}{6} x^{3} \geqslant 5 x^{2}-5 x^{3}+1,
$$

也即

$$
\forall x \in(0,1), x\left(31 x^{2}-27 x+6\right) \geqslant 0
$$

而右侧二次函数部分的判别式 $\Delta=-15<0$, 因此不等式成立. 这就证明了 $\lambda>5$.综上所述,原命题得证.

$8(\sqrt{\mathrm{e}}-1)<5.2$ 即

$$
\mathrm{e}<\frac{1089}{400}=2.7225
$$

## 第 923 题极值点偏移不等式的几种常见处理方法

已知函数 $f(x)=a-\frac{1}{x}-\ln x$, 其中 $a \in \mathbf{R}$.

(1) 若 $a=2$, 求 $f(x)$ 在 $\left(1, \mathrm{e}^{2}\right)$ 上的零点个数;

(2) 若 $f(x)$ 恰有一个零点, 求 $a$ 的取值集合;

(3) 若 $f(x)$ 有两个零点 $x_{1} x_{2}$, 且 $x_{1}<x_{2}$, 求证: $2<x_{1}+x_{2}<3 \mathrm{e}^{a-1}-1$.

解析 解法一 (1) 记函数 $g(x)=\frac{1}{x}+\ln x$, 则

$$
g^{\prime}(x)=\frac{x-1}{x^{2}}
$$

于是可得函数 $g(x)$ 的图象如图.

于是当 $a=2$ 时, $f(x)$ 在 $\left(1, \mathrm{e}^{2}\right)$ 上有一个零点.

(2) 若 $f(x)$ 恰有一个零点, 则 $a$ 的取值集合为 $\{1\}$.

(3) 左边不等式 根据题意, 有

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-332.jpg?height=407&width=524&top_left_y=763&top_left_x=1243)

$$
\frac{1}{x_{1}}+\ln x_{1}=a, \frac{1}{x_{2}}+\ln x_{2}=a
$$

两式相减, 化简得

$$
x_{1} x_{2}=\frac{x_{2}-x_{1}}{\ln \frac{x_{2}}{x_{1}}}
$$

于是可得

$$
x_{1}=\frac{1-\frac{x_{1}}{x_{2}}}{\ln \frac{x_{2}}{x_{1}}}, x_{2}=\frac{\frac{x_{2}}{x_{1}}-1}{\ln \frac{x_{2}}{x_{1}}}
$$

令 $\frac{x_{2}}{x_{1}}=t$, 其中 $t>1$, 则

$$
x_{1}+x_{2}=\frac{1-\frac{1}{t}}{\ln t}+\frac{t-1}{\ln t}=\frac{t-\frac{1}{t}}{\ln t},
$$

因此只需要证明

$$
\forall t>1, t-\frac{1}{t}-2 \ln t>0
$$

考虑到

$$
\left(t-\frac{1}{t}-2 \ln t\right)^{\prime}=\left(\frac{1}{t}-1\right)^{2}>0
$$

于是左边不等式得证.

右边不等式 等价于

$$
\ln \frac{x_{1}+x_{2}+1}{3}+1-a<0
$$

将

$$
x_{1}+x_{2}=\frac{t^{2}-1}{t \ln t}, a=\frac{1}{x_{1}}+\ln x_{1}=\frac{t \ln t}{t-1}+\ln \frac{t-1}{t \ln t}
$$

代人该不等式左边得

$$
\ln \frac{t^{2}-1+t \ln t}{t-1}-\frac{t \ln t}{t-1}+1-\ln 3
$$

其导函数为

$$
\frac{t \ln ^{2} t-(t-1)^{2}}{\left(t^{2}-1+t \ln t\right)(t-1)^{2}}
$$

因此只需要证明

$$
\forall t>1, \sqrt{t} \ln t-t+1<0
$$

即

$$
\forall t>1,2 \ln \sqrt{t}<\sqrt{t}-\frac{1}{\sqrt{t}}
$$

根据第(1)小问, 于是右边不等式得证.

解法二 (1) 见解法一.

(2) 见解法一.

(3) 左边不等式 令 $g(x)=\frac{1}{x}+\ln x$, 则证明

$$
\forall t \in(0,1), g(1-t)>g(1+t)
$$

即可. 事实上, 有

$$
g(1-t)-g(1+t)=\frac{2 t}{1-t^{2}}+\ln \frac{1-t}{1+t}
$$

考虑到

$$
\left(\frac{2 t}{1-t^{2}}+\ln \frac{1-t}{1+t}\right)^{\prime}=\frac{4 t^{2}}{\left(1-t^{2}\right)^{2}}>0
$$

于是左边不等式得证.

右边不等式 令 $x_{0}=\mathrm{e}^{a-1}$, 则 $1+\ln x_{0}-a=0$, 于是可知 $x_{0}$ 是函数

$$
h(x)=1+x \ln x-a x
$$

的极小值点.

## 根据题意, 有

$$
x_{1}<x_{0}<x_{2}
$$

于是

$$
\frac{x_{1}}{x_{0}}<1<\frac{x_{2}}{x_{0}}
$$

应用我们熟知的不等式

$$
\forall x \in(0,1), \ln x<\frac{2(x-1)}{x+1}, \forall x>1, \ln x>\frac{2(x-1)}{x+1}
$$

可得

$$
\ln \frac{x_{1}}{x_{0}}<\frac{2\left(x_{1}-x_{0}\right)}{x_{1}+x_{0}}, \ln \frac{x_{2}}{x_{0}}>\frac{2\left(x_{2}-x_{0}\right)}{x_{2}+x_{0}}
$$

又

$$
\ln x_{1}=a-\frac{1}{x_{1}}=1+\ln x_{0}-\frac{1}{x_{1}}
$$

从而有

$$
\ln \frac{x_{1}}{x_{0}}=1-\frac{1}{x_{1}}
$$

同理有

$$
\ln \frac{x_{2}}{x_{0}}=1-\frac{1}{x_{2}}
$$

这样就有

$$
1-\frac{1}{x_{1}}<\frac{2\left(x_{1}-x_{0}\right)}{x_{1}+x_{0}}, 1-\frac{1}{x_{2}}>\frac{2\left(x_{2}-x_{0}\right)}{x_{2}+x_{0}}
$$

从而可得

$$
\left(3 x_{1}-1\right) x_{0}-x_{1}^{2}-x_{1}<0<\left(3 x_{2}-1\right) x_{0}-x_{2}^{2}-x_{2},
$$

即

$$
3\left(x_{2}-x_{1}\right) x_{0}-\left(x_{2}-x_{1}\right)\left(x_{2}+x_{1}+1\right)>0
$$

两边同除以 $x_{2}-x_{1}$, 即得

$$
x_{1}+x_{2}<3 x_{0}-1=3 \mathrm{e}^{a-1}-1,
$$

于是右边不等式得证.

## 第 924 题 分类讨论

已知函数 $f(x)=a \mathrm{e}^{x-1}-1, x \in$ R. 若方程 $f(x)+|x-a|=0$ 有且仅有两个不相等的实根, 则实数 $a$的取值范围为

## 解析 $\{-1\} \cup[0,1)$.

分别考虑函数

$$
g(x)=a \mathrm{e}^{x-1}-1+x-a, x \geqslant a
$$

和函数

$$
h(x)=a \mathrm{e}^{x-1}-x+a-1, x<a
$$

的零点个数. 注意到

$$
g^{\prime}(x)=a \mathrm{e}^{x-1}+1, h^{\prime}(x)=a \mathrm{e}^{x-1}-1
$$

且当 $a \leqslant 1$ 时 $g(1)=0$.

情形一 $a=0$.

此时如图 1 , 符合题意.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-334.jpg?height=325&width=507&top_left_y=1420&top_left_x=1261)

图 1

情形ニ $a>0$. 此时 $g^{\prime}(x)>0$, 而 $h^{\prime}(a)=a \mathrm{e}^{a-1}-1$ 有零点为 $a=1$, 因此需要进一步讨论.

(1) $0<a<1$.

此时 $h^{\prime}(x)<0$, 因此 $h(x)$ 单调递减, $g(x)$ 单调递增, 而

$$
g(a)=a e^{a-1}-1<0,
$$

于是 $g(x)$ 和 $h(x)$ 各有一个零点, 符合题意. 如图 2.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-334.jpg?height=325&width=401&top_left_y=2097&top_left_x=386)

图 2

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-334.jpg?height=322&width=418&top_left_y=2098&top_left_x=1019)

图 3

(2) $a=1$.

此时与(1)类似, $h(x)$ 单调递减, $g(x)$ 单调递增, 而

$$
g(a)=a \mathrm{e}^{a-1}-1=0
$$

于是 $g(x)$ 有一个零点为 $x=1, h(x)$ 没有零点, 不符合题意. 如图 3.

(3) $a>1$.

此时 $h(x)$ 先递减再递增, 且极小值点 $x_{0}$ 满足 $a \mathrm{e}^{x_{0}-1}-1=0$, 于是可得极小值为

$$
h\left(x_{0}\right)=a \mathrm{e}^{x_{0}-1}-1-x_{0}+a=a-x_{0}>0,
$$

因此 $g(x)$ 与 $h(x)$ 均没有零点, 不符合题意. 如图 4.

情形三 $a<0$.

此时 $h^{\prime}(x)<0$, 而

$$
g(a)=a \mathrm{e}^{a-1}-1<0,
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-335.jpg?height=415&width=464&top_left_y=303&top_left_x=1417)

图 4

因此函数 $h(x)$ 有一个零点. 另一方面, 注意到 $g(a)<0$ 且 $g(1)=0$, 于是 $g(x)$ 先递增后递减, 因此只有当 $x=1$ 为函数 $g(x)$ 的极大值点时符合题意, 如图 5 , 此时将 $x=1$ 代人 $a \mathrm{e}^{x-1}$ $+1=0$,

解得

$$
a=-1 \text {. }
$$

综上所述,所求实数 $a$ 的取值范围是 $\{-1\} \cup[0,1)$.

其他解法 当 $a>0$ 时, 将方程变形为

$$
\mathrm{e}^{x-1}=-\left|\frac{1}{a} x-1\right|+\frac{1}{a}
$$

注意以下事实:

(1) 等式右边图象的“顶点”为 $\left(a, \frac{1}{a}\right)$, 在双曲线 $y=\frac{1}{x}$ 上;

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-335.jpg?height=375&width=555&top_left_y=932&top_left_x=1328)

图 5

(2) 等式右边图象恒过点 $(-1,-1)$;

(3) 等式左边图象与双曲线 $y=\frac{1}{x}$ 的交点为 $(1,1)$, 并且该点与 $(-1,-1)$ 的连线与等式左边图象相切于点 $(1,1)$. 其他情形的讨论从略.

## 第 925 题 三次函数的图象

设 $x^{3}+a x+b=0$, 其中 $a, b$ 均为实数, 下列条件中, 使得该三次方程仅有一个实根的是 (写出所有正确条件的编号)

$$
\begin{aligned}
& \text { (1) } a=-3, b=-3 ; \\
& \text { (2) } a=-3, b=2 ; \\
& \text { (3) } a=-3, b>2 ; \\
& \text { (4) } a=0, b=2 ; \\
& \text { (5) } a=1, b=2
\end{aligned}
$$

## 解析 (1)(3)(4)(5).

将三次方程的实根看成是函数 $f(x)=x^{3}+a x$ 的图象与直线 $y=-b$ 的公共点的横坐标.

当 $a \geqslant 0$ 时, $f(x)$ 为单调递增函数, 且值域为 $\mathbf{R}$, 因此无论 $b$ 为何值, 直线 $y=-b$ 与函数 $f(x)=x^{3}+a x$的图象均有唯一公共点. 这样(4)和(5)显然正确;

注意到其他条件中 $a$ 的取值均为 -3 , 因此研究函数 $f(x)=x^{3}-3 x$.
函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=3(x+1)(x-1),
$$

于是函数 $f(x)$ 有极大值点 $x=-1$ 以及极小值点 $x=1$, 对应的极大值为 2 , 极小值为 -2 ,如图.

因此(1)和(3)正确,而(2)错误.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-336.jpg?height=265&width=273&top_left_y=200&top_left_x=1503)

## 第 926 题 估计零点的位置

已知函数 $f(x)=x-\mathrm{e}^{\frac{x}{a}}(a>0)$ 有两个相异零点 $x_{1}, x_{2}$ 且 $x_{1}<x_{2}$, 求证: $\frac{x_{1}}{x_{2}}<\frac{\mathrm{e}}{a}$.

解析 根据已知, 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=1-\frac{1}{a} \mathrm{e}^{\frac{x}{a}},
$$

于是函数 $f(x)$ 在 $(-\infty, a \ln a)$ 上单调递增, 在 $(a \ln a,+\infty)$ 上单调递减, $x=$ $a \ln a$ 是其极大值点, 同时也是最大值点, 而最大值为 $a(\ln a-1)$, 如图.

根据题意, $f(x)$ 有两个相异零点, 于是有

$$
a(\ln a-1)>0
$$

即 $a>$ e. 再由 $f(0)=-1$ 可得

$$
0<x_{1}<a \ln a<x_{2}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-336.jpg?height=355&width=426&top_left_y=1020&top_left_x=1350)

对于欲证明不等式, 无法直接利用(1)式估计左边, 因此利用函数 $f(x)$ 的解析式进行代换:

$$
\frac{x_{1}}{x_{2}}=\mathrm{e}^{\frac{1}{\alpha}\left(x_{1}-x_{2}\right)},
$$

于是只需要证明

$$
x_{2}-x_{1}>a \ln a-a \text { (2). }
$$

在(1)式中,我们已经有了 $x_{2}>a \ln a$, 于是一个自然的推测是尝试证明 $x_{1}<a$, 这只需要

$$
f(a)=a-\mathrm{e}>0
$$

成立即可

综上, 命题得证.

图中为 $a=1.5 \mathrm{e}$ 的情形,可以看到 $0<x_{1}<a<a \ln a<x_{2}$.

## 第 927 题 数形结合

已知函数 $f(x)=\ln x-a x^{2}$, 其中 $a>0$. 若存在 $x_{1}, x_{2} \in[1,3]$, 且 $x_{1}-x_{2} \geqslant 1$, 使得 $f\left(x_{1}\right)=f\left(x_{2}\right)$,求证: $\frac{\ln 3-\ln 2}{5} \leqslant a \leqslant \frac{\ln 2}{3}$.

## 高考数学满分学霸的解题笔记

解析 根据已知有

$$
\left\{\begin{array}{l}
\ln x_{1}-a x_{1}^{2}=0 \\
\ln x_{2}-a x_{2}^{2}=0
\end{array}\right.
$$

观察欲证不等式的形式,将(1)中的两式相减,可得

$$
a=\frac{\ln x_{1}-\ln x_{2}}{x_{1}^{2}-x_{2}^{2}}
$$

于是欲证不等式可以变形为

$$
\frac{\ln 9-\ln 4}{9-4} \leqslant \frac{\ln x_{1}^{2}-\ln x_{2}^{2}}{x_{1}^{2}-x_{2}^{2}} \leqslant \frac{\ln 4-\ln 1}{4-1}
$$

将(2)式中的代数式用图形表示,由

$$
1 \leqslant x_{2}^{2} \leqslant 4 \leqslant x_{1}^{2} \leqslant 9
$$

可得欲证不等式成立. 得到了几何图形的支持以后, 需要给出严格的证明.

接下来, 可以将解法改写.

由于函数 $f(x)$ 的导函数为

$$
f^{\prime}(x)=\frac{1-2 a x^{2}}{x}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-337.jpg?height=434&width=723&top_left_y=679&top_left_x=1151)

在区间 $[1,3]$ 上存在两个点 $f(x)$ 的函数值相同, 于是 $f(x)$ 必然存在区间上的极值点, 因此函数 $f(x)$ 在区间 $\left(1, \frac{\sqrt{2 a}}{2 a}\right)$ 上单调递增, 在区间 $\left(\frac{\sqrt{2 a}}{2 a}, 3\right)$ 上单调递减. 于是

$$
f(1) \leqslant f(2), f(2) \geqslant f(3)
$$

整理即得欲证不等式.

## 思考与总结

事实上, 可以根据几何图形证明一个更强的结论:

引理 当 $x_{1}^{2}$ 或 $x_{2}^{2}$ 增大时, $2 a$ 的取值 $\frac{\ln x_{1}^{2}-\ln x_{2}^{2}}{x_{1}^{2}-x_{2}^{2}}$ 均减小.

证明 记 $F=\frac{\ln u-\ln v}{u-v}$, 则

$$
F^{\prime}{ }_{u}=\frac{\ln \frac{v}{u}+1-\frac{v}{u}}{(u-v)^{2}},
$$

而

$$
\forall \frac{v}{u}>0, u \neq v, \ln \frac{v}{u}<\frac{v}{u}-1,
$$

于是 $F^{\prime}{ }_{u}<0$, 进而可得当 $x_{1}^{2}$ 增大时, $2 a$ 的取值减小. 同理可得当 $x_{2}^{2}$ 增大时, $2 a$ 的取值也减小. 这样一来, 对(3)式应用引理即有结论.

## 第 928 题 含参函数问题的三种处理方式

设函数 $f(x)=\frac{1}{x}, g(x)=a x^{2}+b x(a, b \in \mathbf{R}, a \neq 0)$. 若 $y=f(x)$ 的图象与 $y=g(x)$ 的图象有且仅有两个不同的公共点 $A\left(x_{1}, y_{1}\right)$ 和 $B\left(x_{2}, y_{2}\right)$, 则下列判断中正确的是
A. 当 $a<0$ 时, $x_{1}+x_{2}<0, y_{1}+y_{2}>0$
B. 当 $a<0$ 时, $x_{1}+x_{2}>0, y_{1}+y_{2}<0$
C. 当 $a>0$ 时, $x_{1}+x_{2}<0, y_{1}+y_{2}<0$
D. 当 $a>0$ 时, $x_{1}+x_{2}>0, y_{1}+y_{2}>0$

## 解析 B.

解法一 将右边化为常数 (往往取 0 ). 注意此时可以利用 “ 0 乘以任何数仍然为 0 ”对左边进行调整.对于本题, 可以将问题转化为函数

$$
h(x)=a x^{3}+b x^{2}-1
$$

有两个零点, 由于 $h(x)$ 的导函数

$$
h^{\prime}(x)=x(3 a x+2 b),
$$

由 $h(x)$ 有且仅有两个零点知 $h(x)$ 的极值点中必有一个为零点, 于是函数的两个极值点分别对应点 $(0$, $-1)$ 和 $\left(-\frac{2 b}{3 a}, 0\right)$, 因此对应的函数图象如图 1,2 .

当 $a>0$ 时, 如图 1 .

当 $a<0$ 时,如图 2 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-338.jpg?height=257&width=404&top_left_y=1371&top_left_x=147)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-338.jpg?height=237&width=390&top_left_y=1381&top_left_x=808)

图 2

由三次函数的图象画法可得当 $a>0$ 时, $x_{1}+x_{2}<0$, 且

$$
y_{1}+y_{2}=\frac{1}{x_{1}}+\frac{1}{x_{2}}=\frac{x_{1}+x_{2}}{x_{1} x_{2}}>0
$$

当 $a<0$ 时, $x_{1}+x_{2}>0$, 且

$$
y_{1}+y_{2}=\frac{1}{x_{1}}+\frac{1}{x_{2}}=\frac{x_{1}+x_{2}}{x_{1} x_{2}}<0
$$

因此正确的答案是 B.

## 解法二 根据题意, 有

$$
y_{1}+y_{2}=\frac{1}{x_{1}}+\frac{1}{x_{2}}=\frac{x_{1}+x_{2}}{x_{1} x_{2}}
$$

且 $x_{1}, x_{2}$ 是关于 $x$ 的方程

$$
a x^{3}+b x^{2}-1=0
$$

的实根, 不妨设

$$
a x^{3}+b x^{2}-1=a\left(x-x_{1}\right)^{2}\left(x-x_{2}\right),
$$

则根据三次方程的韦达定理, 有

$$
\left\{\begin{array}{l}
2 x_{1}+x_{2}=-\frac{b}{a} \\
x_{1}^{2}+2 x_{1} x_{2}=0 \\
x_{1}^{2} x_{2}=\frac{1}{a}
\end{array}\right.
$$

于是 $x_{1}=-2 x_{2}$, 进一步有 $x_{2}$ 与 $a$ 同号, $x_{1}+x_{2}=-x_{2}$ 与 $a$ 异号, $x_{1} x_{2}=-2 x_{2}^{2}$ 必然为负实数, $y_{1}+y_{2}$与 $a$ 同号, 选项 B 正确.

解法三 对于本题,考虑方程

$$
a x+b=\frac{1}{x^{2}}
$$

于是直线 $y=a x+b$ 与幂函数 $y=x^{-2}$ 的图象有两个公共点.

当 $a>0$ 时,如图 3 .

此时 $x_{1}+x_{2}<0$, 而

$$
y_{1}+y_{2}=\frac{1}{x_{1}}+\frac{1}{x_{2}}=\frac{x_{1}+x_{2}}{x_{1} x_{2}}>0
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-339.jpg?height=366&width=420&top_left_y=543&top_left_x=1458)

图 3

当 $a<0$ 时, 类似的, 有 $x_{1}+x_{2}>0$, 而

$$
y_{1}+y_{2}=\frac{1}{x_{1}}+\frac{1}{x_{2}}=\frac{x_{1}+x_{2}}{x_{1} x_{2}}<0,
$$

因此正确的答案是 B.

将一边化为含参直线, 另一边化为不含参的函数. 此时问题转化为直线与曲线的位置关系问题, 因此往往对曲线的凹凸性有要求. 在高考范围内, 只有基本初等函数和二次曲线的凹凸性可以直接使用.

解法四 让两边分别只含参数和变量, 考虑方程

$$
a=\frac{1}{x^{3}}-\frac{b}{x}
$$

令 $t=\frac{1}{x}$, 并记右侧函数为

$$
h(t)=t^{3}-b t,
$$

因此对应的函数图象如图 4.

于是当 $a>0$ 时, $y_{1}+y_{2}=t_{1}+t_{2}>0$, 而

$$
x_{1}+x_{2}=\frac{1}{t_{1}}+\frac{1}{t_{2}}=\frac{t_{1}+t_{2}}{t_{1} t_{2}}<0
$$

当 $a<0$ 时, $y_{1}+y_{2}=t_{1}+t_{2}<0$, 而

$$
x_{1}+x_{2}=\frac{1}{t_{1}}+\frac{1}{t_{2}}=\frac{t_{1}+t_{2}}{t_{1} t_{2}}>0
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-339.jpg?height=303&width=415&top_left_y=1770&top_left_x=1463)

图 4

因此正确的答案是 B.

## 第 929 题 不战而屈人之兵

已知函数 $f(x)=\ln (x+1)-a\left(\mathrm{e}^{\frac{x}{2}}-\frac{1}{4} x\right)+4$ 无零点, 求正实数 $a$ 的取值范围.
解析 $\quad$ 这是一个很好分离变量的零点问题,先尝试分离变量, 有

$$
a=\frac{\ln (x+1)+4}{\mathrm{e}^{\frac{x}{2}}-\frac{1}{4} x}
$$

右侧函数 (设为 $g(x)$ ) 求导后的分子部分为

$$
\frac{1}{1+x} \cdot\left(\mathrm{e}^{\frac{x}{2}}-\frac{1}{4} x\right)[\ln (x+1)+4] \cdot\left(\frac{1}{2} \mathrm{e}^{\frac{x}{2}}-\frac{1}{4}\right),
$$

容易发现 $x=0$ 为其零点,于是推测 $g(0)=4$ 是右侧函数的一个极值.

注意到函数 $y=\ln (x+1)+4$ 是上凸函数, 函数 $y=\mathrm{e}^{\frac{x}{2}}-\frac{1}{4} x$是下凸函数,因此所求的取值范围应该是 $a>4$, 如图所示.

接下来强硬地研究 $g(x)$ 可能会比较困难,因此考虑用“不战

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-340.jpg?height=315&width=662&top_left_y=560&top_left_x=1093)
而屈人之兵”的方式表达.

考虑到 $f(0)=4-a$, 因此 $a>4$, 否则 $f(0) \geqslant 0$, 而当 $x \rightarrow-1^{+}$(即从大于 -1 的方向逐渐趋于 -1 ) 时, $f(x) \rightarrow-\infty$. (严格意义上的证明需要取点, 如取 $x_{0}=-1+\mathrm{e}^{-4}$, 证明 $f\left(x_{0}\right)<0$; 也可以利用 $x \rightarrow+\infty$ 时, $f(x) \rightarrow-\infty$, 此时要注意利用

$$
\mathrm{e}^{x} \geqslant \mathrm{e}^{t}(x-t)+\mathrm{e}^{t}, t \in \mathbf{R}
$$

进行放缩后再取点. )

下面证明当 $a>4$ 时符合题意.

此时有

$$
f(x)<\ln (x+1)-4\left(\mathrm{e}^{\frac{x}{2}}-\frac{1}{4} x\right)+4,
$$

这里用到了

$$
\forall x \in \mathbf{R}, \mathrm{e}^{\frac{\pi}{2}}-\frac{1}{4} x>0
$$

设右侧函数为 $h(x)$, 则 $h(x)$ 的导函数

$$
h^{\prime}(x)=\frac{1}{x+1}-2 \mathrm{e}^{\frac{x}{2}}+1
$$

是一个单调递减函数, 而 $h^{\prime}(0)=0$, 于是 $h(x)$ 在 $x=0$ 处取得极大值 $h(0)=0$,

因此 $h(x) \leqslant 0$, 从而 $f(x)<0$, 于是 $f(x)$ 没有零点, 符合题意.

## 第 930 题 极值点偏移

已知 $b>a>0$, 且 $b \ln a-a \ln b=a-b$, 求证:

(1) $a+b-a b>1$;

(2) $a+b>2$;

(3) $\frac{1}{a}+\frac{1}{b}>2$.

解析 (1) 已知条件可以变形为

$$
\frac{\ln a+1}{a}=\frac{\ln b+1}{b}
$$

因此 $a, b$ 是函数 $f(x)=\frac{\ln x+1}{x}$ 的图象与直线 $y=m$ 的两个公共点的横坐标.

考虑函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=-\frac{\ln x}{x^{2}}
$$

于是函数 $f(x)$ 有极大值点 $x=1$, 因此有 $0<a<1<b$, 从而

$$
(a-1)(b-1)<0,
$$

即

$$
a+b-a b>1
$$

命题得证.

(2) 设 $b=a t, t>1$, 则有

$$
\frac{\ln a+1}{a}=\frac{\ln a+\ln t+1}{a t}
$$

解得

$$
\ln a=\frac{\ln t}{t-1}-1
$$

从而

$$
\ln b=\ln a+\ln t=\frac{t \ln t}{t-1}-1
$$

考虑到 $t>1$ 时, 有

$$
\ln t>2 \cdot \frac{t-1}{t+1}
$$

于是

$$
a+b>\mathrm{e}^{\frac{2}{+1}-1}+\mathrm{e}^{\frac{2 t}{\mathrm{e}+1}-1}=\mathrm{e}^{\frac{1-t}{1+t}}+\mathrm{e}^{\frac{i-1}{t+1}}>2
$$

于是 $a+b>2$, 命题得证.

(3) 将已知条件变形为

$$
\frac{1}{a}\left(-\ln \frac{1}{a}+1\right)=\frac{1}{b}\left(-\ln \frac{1}{b}+1\right)
$$

于是 $\frac{1}{a}$ 和 $\frac{1}{b}$ 是函数 $g(x)=x-x \ln x$ 的图象与直线 $y=n$ 的两个公共点的横坐标.

考虑函数 $g(x)$ 的导函数

$$
g^{\prime}(x)=-\ln x
$$

于是函数 $g(x)$ 有极大值点 $x=1$, 于是

$$
0<\frac{1}{b}<1<\frac{1}{a}
$$

对称化构造函数

$$
h(x)=g(2-x)-g(x)
$$

其中 $0<x<1$, 则其导函数

$$
h^{\prime}(x)=\ln (2-x)+\ln x=\ln (x(2-x))<0,
$$

于是 $h(x)$ 在 $(0,1]$ 上单调递减, 因此 $h(x)$ 在 $(0,1)$ 上有

$$
h(x)>h(1)=0,
$$

也即当 $0<x<1$ 时, $g(2-x)>g(x)$.

这样就有

$$
g\left(\frac{1}{a}\right)=g\left(\frac{1}{b}\right)<g\left(2-\frac{1}{b}\right)
$$

而 $g(x)$ 在 $(1,+\infty)$ 上单调递减, 于是

$$
\frac{1}{a}>2-\frac{1}{b}
$$

即

$$
\frac{1}{a}+\frac{1}{b}>2
$$

命题得证.

第 (2)小题也可以用与第 (3)小题类似的对称化构造的方法去证明.

## 第 931 题 对数值的估算

若函数 $f(x)=x^{2}+\frac{2}{x}-a \ln x(a>0)$ 存在唯一零点 $x_{0}$, 且 $m<x_{0}<n$, 其中 $m, n$ 为相邻的整数, 则 $m$ $+n=$

## 解析 5.

根据题意, 方程

$$
x^{2}+\frac{2}{x}-a \ln x=0
$$

有唯一解, 也即函数 $g(x)=\frac{x^{2}+\frac{2}{x}}{\ln x}$ 的图象与直线 $y=a$ 相切于点 $\left(x_{0}, a\right)$. 考虑到 $a>0$, 因此只需要估计函数 $g(x)$ 的导函数在 $x>1$ 时的零点位置即可.函数 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{\left(2 x^{3}-2\right) \ln x-\left(x^{3}+2\right)}{x^{2} \ln ^{2} x}
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-342.jpg?height=279&width=443&top_left_y=1457&top_left_x=1312)

设分子为 $\varphi(x)$, 则

$$
\varphi(2)=14 \ln 2-10<7 \sqrt{2}-10<0
$$

而

$$
\varphi(3)=52 \ln 3-29>0 .
$$

其中用到了

$$
\ln 2<\sqrt{2}-\frac{1}{\sqrt{2}}
$$

这是因为对 $\ln x$ 的常用估计：

$$
\forall x>1,2 \cdot \frac{x-1}{x+1}<\ln x<\sqrt{x}-\frac{1}{\sqrt{x}}
$$

这样就得到了

$$
2<x_{0}<3,
$$

从而 $m+n$ 的值为 5 .

## 第 932 题 一波三折

已知关于 $x$ 的方程 $x \ln x^{2}+a=x \ln a+x^{2}$ 有 4 个实数根, 求 $a$ 的取值范围.

解析 将问题转化为函数

$$
f(x)=\ln x^{2}-x+\frac{a}{x}-\ln a
$$

有 4 个零点. 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{-x^{2}+2 x-a}{x^{2}}
$$

情形一 $\quad x<0$.

此时 $f(x)$ 单调递减, 而 $f(x)$ 在 $(-\infty, 0)$ 上的值域为 $(-\infty,+\infty)$, 因此函数 $f(x)$ 在 $(-\infty, 0)$ 上必然有 1 个零点.

情形ニ $x>0$.

此时函数 $f(x)$ 在 $(0,+\infty)$ 上有 3 个零点, 因此其导函数至少有 2 个零点, 因此可得 $0<a<1$, 此时极小值点 $x=x_{1}$ 和极大值点 $\dot{x}=x_{2}$ 是方程

$$
x^{2}-2 x+a=0
$$

的两根, 且 $0<x_{1}<1<x_{2}$.

将 $a=-m^{2}+2 m$ 代人极值

$$
M=f(m)=\ln m^{2}-m+\frac{a}{m}-\ln a,
$$

可得

$$
M=\ln \frac{m}{2-m}+2(1-m)
$$

令 $t=\frac{m}{2-m}$, 则有

$$
M=\ln t-2 \cdot \frac{t-1}{t+1}
$$

于是可得

$$
\left.M\right|_{m=x_{1}}<0<\left.M\right|_{m=x_{2}},
$$

因此当 $0<a<1$ 时, 函数 $f(x)$ 在 $(0,+\infty)$ 上有 3 个零点.

综上所述, $a$ 的取值范围是 $(0,1)$.

## 第 933 题 方程组的解

关于 $x, y$ 的方程组 $\left\{\begin{array}{l}x^{2}+y^{3}=29, \\ \log _{3} x \cdot \log _{2} y=1\end{array}\right.$ 的不同实数解的组数是

## 解析 2

题中方程组可以变形为

$$
\left\{\begin{array}{l}
x^{2}+y^{3}=29 \\
\log _{3} x^{2} \cdot \log _{3} y^{3}=6
\end{array}\right.
$$

于是问题可以转化为求关于 $x, y$ 的方程组

$$
\left\{\begin{array}{l}
x+y=29 \\
\ln x \cdot \ln y=6 \ln 2 \cdot \ln 3
\end{array}\right.
$$

的实数解组数,即关于 $x$ 的方程

$$
\ln x \cdot \ln (29-x)=6 \ln 2 \cdot \ln 3
$$

的实数解个数.

显然, 有 $1<x<28$, 令 $f(x)=\ln x \cdot \ln (29-x)(x \in(1,28))$, 则其导函数

$$
f^{\prime}(x)=\frac{(29-x) \ln (29-x)-x \ln x}{x(29-x)}, 1<x<28
$$

考虑到函数 $y=x \ln x$ 在 $(1,28)$ 上单调递增, 于是函数 $y=(29-x) \ln (29-x)-x \ln x(1<x<28)$ 单调递减, 在区间 $(1,28)$ 上有唯一零点 $x=\frac{29}{2}$. 因而函数 $f(x)$ 在 $\left(1, \frac{29}{2}\right)$ 上单调递增, 在 $\left(\frac{29}{2}, 28\right)$ 上单调递减, 考虑到

$$
f(1)=0, f\left(\frac{29}{2}\right)=\ln ^{2} \frac{29}{2}>\ln 8 \cdot \ln 9=6 \ln 2 \cdot \ln 3, f(28)=0
$$

因此关于 $x$ 的方程

$$
\ln x \cdot \ln (29-x)=6 \ln 2 \cdot \ln 3
$$

的实数解个数为 2 .

综上所述, 题中方程组的不同实数解的组数为 2 .

## 第 934 题 合理解读条件

已知函数 $f(x)=2 \ln x-a x^{2}+1$, 存在实数 $m$, 使得方程 $f(x)=m$ 的两个实根 $\alpha, \beta$ 均在区间 $[1,4]$内, 且 $\beta-\alpha=1$, 求实数 $a$ 的取值范围.

解析 原问题即存在 $x \in[1,3]$ 使得 $f(x+1)=f(x)$.

上述方程即

$$
2 \ln (x+1)-a(x+1)^{2}+1=2 \ln x-a x^{2}+1
$$

整理得

$$
a=2 \cdot \ln \left(1+\frac{1}{x}\right) \cdot \frac{1}{2 x+1}
$$

上述等式右侧函数在区间 $[1,3]$ 上单调递减, 因此 $a$ 的取值范围是 $\left[\frac{4 \ln 2-2 \ln 3}{7}, \frac{2 \ln 2}{3}\right]$.

## 第 935 题 对称化构造

已知 $f(x)=x \ln x-\frac{k}{x}$ 有两个不同的零点 $x_{1}, x_{2}$, 且 $x_{1}<x_{2}$.

(1)求 $k$ 的取值范围;

(2) 求证: $1<x_{1}+x_{2}<\frac{2}{\sqrt{\mathrm{e}}}$.
解析 (1) 题意即关于 $x$ 的方程 $x^{2} \ln x=k$ 有两个实数根 $x_{1}, x_{2}$,

设函数 $g(x)=x^{2} \ln x$, 则其导函数

$$
g^{\prime}(x)=x(2 \ln x+1), x>0
$$

考虑到

$$
\lim _{x \rightarrow 0} x^{2} \ln x=\lim _{x \rightarrow+\infty} \frac{-\ln x}{x^{2}}=-\lim _{x \rightarrow+\infty} \frac{\ln x}{x^{2}}
$$

而当 $x>1$ 时, 有

$$
0<\frac{\ln x}{x^{2}}<\frac{x-1}{x^{2}}<\frac{1}{x}
$$

于是 $\lim _{x \rightarrow 0} x^{2} \ln x=0$, 如图.

不难得到 $k$ 的取值范围是 $\left(-\frac{1}{2 \mathrm{e}}, 0\right)$ ，而此时 $0<x_{1}<\frac{1}{\sqrt{\mathrm{e}}}<x_{2}<1$.

(2) 先证明右边的不等式. 由于函数 $g(x)$ 在 $\left(\frac{1}{\sqrt{\mathrm{e}}},+\infty\right)$ 上单调递增, 而 $x_{2}, \frac{2}{\sqrt{\mathrm{e}}}$ $-x_{1} \in\left(\frac{1}{\sqrt{\mathrm{e}}},+\infty\right)$, 因此只需要证明

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-345.jpg?height=337&width=405&top_left_y=658&top_left_x=1461)

$$
g\left(x_{1}\right)=g\left(x_{2}\right)<g\left(\frac{2}{\sqrt{\mathrm{e}}}-x_{1}\right)
$$

也即

$$
\forall x \in\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right), g(x)-g\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)<0
$$

记

$$
h(x)=g(x)-g\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right), x \in\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right)
$$

则

$$
\begin{aligned}
h^{\prime}(x) & =g^{\prime}(x)+g^{\prime}\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right) \\
& =x(2 \ln x+1)+\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)\left[2 \ln \left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)+1\right] \\
& =2\left[x \ln x+\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right) \ln \left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)+\frac{1}{\sqrt{\mathrm{e}}}\right]
\end{aligned}
$$

记

$$
m(x)=x \ln x+\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right) \ln \left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)+\frac{1}{\sqrt{\mathrm{e}}}, x \in\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right),
$$

则

$$
m^{\prime}(x)=\ln x-\ln \left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)<0
$$

而 $m^{\prime}\left(\frac{1}{\sqrt{\mathrm{e}}}\right)=0$, 所以 $m^{\prime}(x)>0$, 即 $h^{\prime}(x)>0$, 而 $h\left(\frac{1}{\sqrt{\mathrm{e}}}\right)=0$, 所以 $h(x)<0$.

类似的, 左边不等式的证明等价于

$$
\forall x \in\left(\frac{1}{\sqrt{\mathrm{e}}}, 1\right), g(x)-g(1-x)<0
$$

再证明 $g(x)-g(1-x)<0$ 对 $x \in\left(\frac{1}{2}, 1\right)$ 成立, 过程类似, 证明从略.

## 第 936 题 零点问题的转化

若函数 $f(x)=2 \mathrm{e}^{x}-a x^{2}+(a-2 \mathrm{e}) x$ 有三个不同的零点,则实数 $a$ 的取值范围是

解析 $(0,+\infty)$.

注意到 $x=1$ 是函数 $f(x)$ 的零点, 而 $x=0$ 不是函数 $f(x)$ 的零点, 于是问题等价于函数

$$
g(x)=\frac{\mathrm{e}^{x}-\mathrm{e} x}{x^{2}-x}, x \neq 0, x \neq 1
$$

的图象与直线 $y=\frac{1}{2} a$ 有两个公共点. 函数 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{\mathrm{e}^{x}\left(x^{2}-3 x+1\right)+\mathrm{e} x^{2}}{\left(x^{2}-x\right)^{2}}=\frac{\mathrm{e} x^{2}}{\left(x^{2}-x\right)^{2}} \cdot\left[\mathrm{e}^{x-1}\left(1-\frac{3}{x}+\frac{1}{x^{2}}\right)+1\right]
$$

设函数

$$
\varphi(x)=\mathrm{e}^{x-1}\left(1-\frac{3}{x}+\frac{1}{x^{2}}\right)
$$

则其导函数

$$
\varphi^{\prime}(x)=\mathrm{e}^{x-1}\left(1-\frac{3}{x}+\frac{4}{x^{2}}-\frac{2}{x^{3}}\right)=\frac{\mathrm{e}^{x-1}}{x^{3}}(x-1)\left(x^{2}-2 x+2\right),
$$

于是 $\varphi(x)$ 的最小值为 $\varphi(1)=-1$. 这样我们就得到了 $g(x)$ 在 $(-\infty, 0),(0,1),(1,+\infty)$ 上均单调. 显然在 $(-\infty, 0)$ 上 $g(x)>0$; 在 $(0,1)$ 上 $g(x)<0$; 在 $(1,+\infty)$ 上 $g(x)>0$. 于是当 $a \leqslant 0$ 时, 函数 $g(x)$ 的图象与直线 $y=\frac{1}{2} a$ 至多只有一个公共点, 不符合题意.

接下来我们证明当 $a>0$ 时, 函数 $g(x)$ 的图象与直线 $y=\frac{1}{2} a$ 恰好有两个公共点, 它们的横坐标分别位于区间 $(-\infty, 0)$ 和 $(1,+\infty)$ 上. 证明的关键在于在每个区间上, 对于任意给定的正数 $m$, 都存在比 $m$ 大的函数值以及比 $m$ 小的函数值.

在区间 $(-\infty, 0)$ 上,由于

$$
\frac{1}{x^{2}-x}<\frac{\mathrm{e}^{x}-\mathrm{e} x}{x^{2}-x}<\frac{1-\mathrm{e} x}{x^{2}-x}
$$

而在区间 $(-\infty, 0)$ 上, 函数 $y=\frac{1}{x^{2}-x}$ 可以取到比 $m$ 大的函数值, 而函数 $y=\frac{1-\mathrm{e} x}{x^{2}-x}$ 可以取到比 $m$ 小的函数值;

在区间 $(1,+\infty)$ 上,一方面由 $\mathrm{e}^{x}-\mathrm{e} x>0$ 积分两次可得

$$
\frac{\mathrm{e}^{x}-\mathrm{e} x}{x^{2}-x}>\frac{\frac{1}{6} \mathrm{e} x^{3}-\mathrm{e} x}{x^{2}-x},
$$

而在区间 $(1,+\infty)$ 上, 函数 $y=\frac{\frac{1}{6} \mathrm{e} x^{3}-\mathrm{e} x}{x^{2}-x}$ 可以取到比 $m$ 大的函数值;

另一方面, 在区间 $(1,2)$ 上, 有

$$
\frac{\mathrm{e}^{x}-\mathrm{e} x}{x^{2}-x}<\frac{\mathrm{e} x-\mathrm{e}}{x}
$$

而在区间 $(1,2)$ 上, 函数 $y=\frac{\mathrm{e} x-\mathrm{e}}{x}$ 可以取到比 $m$ 小的函数值.
综上, 实数 $a$ 的取值范围是 $(0,+\infty)$.

其他解法 分析 对 $\mathrm{e}^{x}-\mathrm{e} x>0$ 在 $[1, x]$ 上进行积分得

$$
\int_{1}^{x}\left(\mathrm{e}^{x}-\mathrm{e} x\right) \mathrm{d} x=\mathrm{e}^{x}-\frac{1}{2} \mathrm{e} x^{2}>0,
$$

再积分一次即可得到 $\mathrm{e}^{x}-\mathrm{e} x>\frac{1}{6} \mathrm{e} x^{3}-\mathrm{e} x$, 也可以直接证明此不等式, 但积分可以得到这个不等式, 我们希望分子是一个三次函数.

解 对 $f(x)$ 求导得

$$
f^{\prime}(x)=2 \mathrm{e}\left(\mathrm{e}^{x-1}-1\right)+a(1-2 x),
$$

从而有 $f^{\prime}(1)=-a, f^{\prime \prime}(x)=2\left(\mathrm{e}^{x}-a\right)$.

当 $a \leqslant 0$ 时, $f^{\prime \prime}(x)>0, f^{\prime}(x)$ 单调递增, 从而 $f(x)$ 最多有两个单调区间, 因此不可能有三个不同的零点;

当 $a>0$ 时, $f^{\prime}(x)$ 先减后增, 最小值为 $f^{\prime}(\ln a)$, 而 $f^{\prime}(1)=-a<0$, 所以 $f^{\prime}(x)$ 一定有两个零点,

记为 $m, n$, 且有 $m<1<n$.

而当 $x \rightarrow-\infty$ 时, $f^{\prime}(x)$ 可以取到正数; 当 $x \rightarrow+\infty$ 时, $f^{\prime}(x)$ 可以取到正数 (严格来说, 需要对 $\mathrm{e}^{x}$ 进行放缩以证明或者取出特殊点).

所以 $f(x)$ 在 $(-\infty, m)$ 上单调递增, 在 $(m, n)$ 上单调递减, 在 $(n,+\infty)$ 上单调递增, 而 $f(1)=0$, 所以 $f(m)>0, f(n)<0$, 而 $f(x)$ 在 $x \rightarrow-\infty$ 时可以取到负值, 在 $x \rightarrow+\infty$ 时可以取到正数 (仍然需要严格处理函数), 所以此时 $f(x)$ 一定有三个零点, 所以 $a$ 的取值范围是 $(0,+\infty)$.

## 第 937 题 紧密相连

设函数 $f(x)=\mathrm{e}^{x}-a x+a(a \in \mathbf{R})$, 其图象与 $x$ 轴交于 $A\left(x_{1}, 0\right), B\left(x_{2}, 0\right)$ 两点, 且 $x_{1}<x_{2}$.

(1) 求 $a$ 的取值范围;

(2) 求证: $f^{\prime}\left(\sqrt{x_{1} x_{2}}\right)<0$;

(3) 设点 $C$ 在函数 $y=f(x)$ 的图象上, 且 $\triangle A B C$ 为等腰直角三角形, 记 $\sqrt{\frac{x_{2}-1}{x_{1}-1}}=t$, 求 $(a-1)(t-1)$ 的值.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\mathrm{e}^{x}-a,
$$

显然有 $a>0$,于是函数 $f(x)$ 在 $(-\infty, \ln a)$ 上单调递减, 在 $(\ln a,+\infty)$ 上单调递增, 当 $x=\ln a$ 时函数 $f(x)$ 取得极小值, 亦为最小值

$$
f(\ln a)=a(2-\ln a),
$$

由最小值小于零得到 $a$ 的取值范围是 $\left(\mathrm{e}^{2},+\infty\right)$.

(2) 由题意, 有

$$
\left\{\begin{array}{l}
\mathrm{e}^{x_{1}}-a x_{1}+a=0, \\
\mathrm{e}^{x_{2}}-a x_{2}+a=0,
\end{array}\right.
$$

于是

$$
a=\frac{\mathrm{e}^{x_{2}}-\mathrm{e}^{x_{1}}}{x_{2}-x_{1}}
$$

因此欲证明不等式即

$$
\mathrm{e}^{\sqrt{x_{1} x_{2}}}-\frac{\mathrm{e}^{x_{2}}-\mathrm{e}^{x_{1}}}{x_{2}-x_{1}}<0
$$

由对数平均不等式以及均值不等式, 我们知道

$$
\frac{\mathrm{e}^{x_{2}}-\mathrm{e}_{x_{1}}}{x_{2}-x_{1}}=\frac{\mathrm{e}^{x_{2}}-\mathrm{e}^{x_{1}}}{\ln ^{x_{2}}-\ln \mathrm{e}^{x_{1}}}>\sqrt{\mathrm{e}^{x_{1}} \cdot \mathrm{e}^{x_{2}}}=\mathrm{e}^{\frac{x_{1}+x_{2}}{2}}>\mathrm{e}^{\sqrt{x_{1} x_{2}}},
$$

因此原命题得证.

## 思考与总结

也可以不用对数平均不等式, 直接证明

$$
\frac{\mathrm{e}^{x_{2}}-\mathrm{e}^{x_{1}}}{x_{2}-x_{1}}>\mathrm{e}^{\frac{x_{1}+x_{2}}{2}}
$$

对此式变形得

$$
\mathrm{e}^{\frac{x_{2}-x_{1}}{2}}-\mathrm{e}^{\frac{x_{1}-x_{2}}{2}}>x_{2}-x_{1}
$$

令 $t=\frac{x_{2}-x_{1}}{2}$, 则需要证明的不等式为

$$
\mathrm{e}^{t}-\mathrm{e}^{-t}-2 t>0, t>0
$$

将左边看成关于 $t$ 的函数直接求导便可证明此不等式.

(3) 如图, 根据题意, 点 $C$ 的横坐标为 $\frac{x_{1}+x_{2}}{2}$.

于是

$$
f\left(\frac{x_{1}+x_{2}}{2}\right)=\frac{x_{1}-x_{2}}{2}
$$

即

$$
\mathrm{e}^{\frac{x_{1}+x_{2}}{2}}-a \cdot \frac{x_{1}+x_{2}}{2}+a+\frac{x_{2}-x_{1}}{2}=0
$$

又

$$
\mathrm{e}^{\frac{x_{1}+x_{2}}{2}}=\sqrt{\mathrm{e}^{x_{1}} \cdot \mathrm{e}^{x_{2}}}=a \sqrt{\left(x_{1}-1\right)\left(x_{2}-1\right)}=a t\left(x_{1}-1\right)
$$

代人, 并整理得

$$
\text { at }\left(x_{1}-1\right)-\frac{a+1}{2}\left(x_{1}-1\right)-\frac{a-1}{2}\left(x_{2}-1\right)=0,
$$

因此

$$
a t-\frac{a+1}{2}-\frac{a-1}{2} t^{2}=0,
$$

也即

$$
\left(t^{2}-2 t+1\right) a=t^{2}-1,
$$

于是

$$
(a-1)(t-1)=2
$$

原命题得证.

## 第 938 题 构造函数看方程

已知 $x>0$, 考虑方程 $a^{x}=x^{a}$, 其中 $a>0$ 且 $a \neq 1$.

(1) 若方程只有一个实数解, 求 $a$ 的取值范围;

(2) 若方程有两个实数解 $x_{1}, x_{2}$, 求证: $x_{1}+x_{2}>2 \mathrm{e}$.

解析 $(1)$ 方程 $a^{x}=x^{a}$ 等价于

$$
\frac{\ln x}{x}=\frac{\ln a}{a},
$$

于是当 $a=\mathrm{e}$ 或 $0<a<1$ 时方程只有一个实数解.

因此 $a$ 的取值范围是 $(0,1) \cup\{\mathrm{e}\}$.

(2)根据第 (1)小题, 可得 $\frac{\ln a}{a} \in\left(0, \frac{1}{\mathrm{e}}\right)$. 由于

$$
\left\{\begin{array}{l}
a \ln x_{1}=x_{1} \ln a, \\
a \ln x_{2}=x_{2} \ln a,
\end{array}\right.
$$

于是

$$
a\left(\ln x_{1}-\ln x_{2}\right)=\left(x_{1}-x_{2}\right) \ln a,
$$

从而根据对数平均不等式得

$$
\frac{x_{1}+x_{2}}{2}>\frac{x_{1}-x_{2}}{\ln x_{1}-\ln x_{2}}=\frac{a}{\ln a}>\mathrm{e}
$$

原命题得证.

## 第 939 题 对称化构造

已知 $a>b>0, a^{b}=b^{a}$, 求证:

(1) $a>\mathrm{e}>b>1$;

(2) $a+b>2 \mathrm{e}$

(3) $a \cdot b>\mathrm{e}^{2}$.

解析 (1)根据题意, 有 $\frac{\ln a}{a}=\frac{\ln b}{b}$.

令 $f(x)=\frac{\ln x}{x}$, 则其导函数

$$
f^{\prime}(x)=\frac{1}{x^{2}} \cdot(1-\ln x)
$$

于是 $f(x)$ 在 $(0, \mathrm{e})$ 上单调递增, 在 $(\mathrm{e},+\infty)$ 上单调递减, 在 $x=\mathrm{e}$ 处取得极大值 $\frac{1}{\mathrm{e}}$, 如图.

因此可得 $a>\mathrm{e}>b>1$.

（2）显然只需要证明 $a<2 \mathrm{e}$ 的情形, 即证明 $b>2 \mathrm{e}-a$, 考虑到 $b, 2 \mathrm{e}-a$ 均位

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-349.jpg?height=307&width=447&top_left_y=2283&top_left_x=1416)
于 $f(x)$ 的单调递增区间 $(0, \mathrm{e})$ 内, 因此只需要证明

$$
f(b)>f(2 \mathrm{e}-a),
$$

也即

$$
f(a)>f(2 \mathrm{e}-a) .
$$

接下来我们证明

$$
\forall x \in(\mathrm{e}, 2 \mathrm{e}), f(x)-f(2 \mathrm{e}-x)>0
$$

设上述不等式左侧为 $g(x)$, 则其导函数

$$
\begin{aligned}
g^{\prime}(x) & =f^{\prime}(x)+f^{\prime}(2 \mathrm{e}-x) \\
& =\frac{1-\ln x}{x^{2}}+\frac{1-\ln (2 \mathrm{e}-x)}{(2 \mathrm{e}-x)^{2}} \\
& =\frac{1-\ln (2 \mathrm{e}-x)}{(2 \mathrm{e}-x)^{2}}-\frac{\ln x-1}{x^{2}}
\end{aligned}
$$

考虑到当 $x \in(\mathrm{e}, 2 \mathrm{e})$ 时,有

$$
\ln x+\ln (2 \mathrm{e}-x)=\ln [x \cdot(2 \mathrm{e}-x)]<\ln \mathrm{e}^{2}=2,
$$

于是

$$
1-\ln (2 \mathrm{e}-x)>\ln x-1>0,
$$

又当 $x \in(\mathrm{e}, 2 \mathrm{e})$ 时, 有

$$
(2 \mathrm{e}-x)^{2}<x^{2},
$$

于是当 $x \in(\mathrm{e}, 2 \mathrm{e})$ 时, 有 $g^{\prime}(x)>0$, 因此 $g(x)$ 在 $(\mathrm{e}, 2 \mathrm{e})$ 上单调递增, 结合 $g(\mathrm{e})=0$, 命题得证.

(3) 显然只需要证明 $a<\mathrm{e}^{2}$ 的情形, 与 (2)类似, 只需要证明

$$
\forall x>\mathrm{e}, f(x)-f\left(\frac{\mathrm{e}^{2}}{x}\right)>0
$$

设上述不等式左侧为 $h(x)$, 则其导函数

$$
\begin{aligned}
h^{\prime}(x) & =f^{\prime}(x)+\frac{\mathrm{e}^{2}}{x^{2}} \cdot f^{\prime}\left(\frac{\mathrm{e}^{2}}{x}\right) \\
& =\frac{1-\ln x}{x^{2}}+\frac{\ln x-1}{x} \\
& =\frac{x-1}{x^{2}} \cdot(\ln x-1) \\
& >0,
\end{aligned}
$$

因此 $h(x)$ 在 $\left(\mathrm{e}, \mathrm{e}^{2}\right)$ 上单调递增, 结合 $h(\mathrm{e})=0$, 命题得证.

## 第 940 题 三次函数的性质

已知函数 $f(x)=-\frac{1}{3} x^{3}+x^{2}-a x$ 有三个零点 $0, x_{1}, x_{2}$, 且 $x_{1}<x_{2}$. 若对任意的 $x \in\left[x_{1}, x_{2}\right], f(x)$ $>f(1)$ 恒成立, 求实数 $a$ 的取值范围.

解析 解法一 根据题意, 有

$$
f(x)=-\frac{1}{3} x\left(x^{2}-3 x+3 a\right)
$$

设 $g(x)=x^{2}-3 x+3 a$,则当其判别式

$$
\Delta=9-12 a>0
$$

时, 函数 $f(x)$ 有 3 个零点, 解得 $a<\frac{3}{4}$.

考虑到函数 $f(x)$ 关于点 $(1, f(1))$ 对称, 于是不等式 $f(x)>f(1)$ 的解集为

$$
(-\infty, 2-m) \cup(1, m)
$$

其中

$$
m>1, f(m)=f(1)
$$

根据题意, 区间 $\left[x_{1}, x_{2}\right]$ 是其子集, 因此

$$
1<x_{1}<x_{2}
$$

即 $f(1)<0$, 也即 $g(1)>0$, 得到

$$
3 a-2>0,
$$

解得 $a>\frac{2}{3}$.

综上所述, 实数 $a$ 的取值范围是 $\left(\frac{2}{3}, \frac{3}{4}\right)$.

解法二 考虑

$$
f(x)-f(1)=\frac{1}{3}(x-1)\left[x^{2}-2 x+(3 a-2)\right]<0,
$$

对 $x \in\left[x_{1}, x_{2}\right]$ 恒成立, 从而有 $1 \notin\left[x_{1}, x_{2}\right]$,

又因为 $x_{1}+x_{2}=3$, 所以有

$$
1<x_{1}<x_{2}
$$

记 $h(x)=x^{2}-2 x+(3 a-2)$, 则 $h(x)<0$ 对 $x \in\left[x_{1}, x_{2}\right]$ 成立, 其中 $x_{1}, x_{2}$ 是 $x^{2}-3 x+3 a=0$ 的两根,由 $1<x_{1}<x_{2}$ 知, 这只需要

$$
h\left(x_{2}\right)=x_{2}^{2}-2 x_{2}+(3 a-2)<0
$$

即可.

又因为

$$
3 a=x_{1} \cdot x_{2}=x_{2}\left(3-x_{2}\right),
$$

所以有

$$
x_{2}^{2}-2 x_{2}+x_{2}\left(3-x_{2}\right)-2<0,
$$

解得 $x_{2}<2$.

又因为 $x_{2}>\frac{3}{2}$, 所以 $x_{2} \in\left(\frac{2}{3}, 2\right)$, 从而

$$
a=\frac{1}{3} x_{2}\left(3-x_{2}\right) \in\left(\frac{2}{3}, \frac{3}{4}\right)
$$

## 第 941 题 指对纠缠

已知函数 $f(x)=\ln x+\frac{a}{x}$, 其中 $a>0$.

(1) 若函数 $f(x)$ 有零点, 求实数 $a$ 的取值范围;

(2)求证: 当 $a \geqslant \frac{2}{\mathrm{e}}, b \geqslant 1$ 时, $f(\ln b)>\frac{1}{b}$.

解析 解法一 (1) 根据已知, 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{x-a}{x^{2}}
$$

因此函数 $f(x)$ 在 $x=a$ 处取得极小值, 亦为最小值是

$$
f(a)=\ln a+1,
$$

考虑到

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow+\infty} f(x)=+\infty,
$$

所以

$$
\ln a+1 \leqslant 0, a>0
$$

因此符合题意的实数 $a$ 的取值范围是 $\left(0, \frac{1}{\mathrm{e}}\right]$.

(2) 问题即当 $a \geqslant \frac{2}{\mathrm{e}}$ 时, 有

$$
\forall x>0, \ln x+\frac{a}{x}>\frac{1}{\mathrm{e}^{x}}
$$

等价于证明

$$
\forall x>0, \ln x+\frac{2}{\mathrm{e} x}-\frac{1}{\mathrm{e}^{x}}>0
$$

考虑到 $x=1$ 时, 左边的值为 $\frac{1}{\mathrm{e}}$, 比较接近 0 , 尝试在 $x=1$ 处对指数部分进行切线放缩:

$$
\mathrm{e}^{x} \geqslant \mathrm{e} x
$$

等号当且仅当 $x=1$ 时取得, 于是

$$
\ln x+\frac{2}{\mathrm{e} x}-\frac{1}{\mathrm{e}^{x}} \geqslant \ln x+\frac{1}{\mathrm{e} x}
$$

设右边为函数 $\varphi(x)$, 则其导函数

$$
\varphi^{\prime}(x)=\frac{\mathrm{e} x-1}{\mathrm{e} x^{2}},
$$

于是 $\varphi(x)$ 在 $x=\frac{1}{\mathrm{e}}$ 处取得极小值, 亦为最小值

$$
\varphi\left(\frac{1}{\mathrm{e}}\right)=0
$$

这样就有

$$
\ln x+\frac{2}{\mathrm{e} x}-\frac{1}{\mathrm{e}^{x}} \geqslant \ln x+\frac{1}{\mathrm{e} x} \geqslant 0
$$

且等号无法同时取得, 原命题得证.

## 解法二 (1) 见解法一.

(2) 问题即当 $a \geqslant \frac{2}{\mathrm{e}}$ 时, 有

$$
\forall x>0, \ln x+\frac{a}{x}>\frac{1}{\mathrm{e}^{x}}
$$

等价于证明

$$
\forall x>0, \ln x+\frac{2}{\mathrm{e} x}-\frac{1}{\mathrm{e}^{x}}>0
$$

注意到不等式即

$$
x \ln x-\frac{x}{\mathrm{e}^{x}}+\frac{2}{\mathrm{e}}>0
$$

记 $\mu(x)=x \ln x$, 则该不等式即

$$
\mu(x)+\mu\left(\mathrm{e}^{-x}\right)>-\frac{2}{\mathrm{e}}
$$

由于函数 $\mu(x)$ 的导函数

$$
\mu^{\prime}(x)=1+\ln x
$$

于是 $\mu(x)$ 在 $x=\frac{1}{\mathrm{e}}$ 处取得极小值, 亦为最小值

$$
\mu\left(\frac{1}{\mathrm{e}}\right)=-\frac{1}{\mathrm{e}}
$$

这样我们就得到了 $\mu\left(\mathrm{e}^{-x}\right)$ 在 $x=1$ 处取得最小值 $-\frac{1}{\mathrm{e}}$. 因此

$$
\mu(x)+\mu\left(\mathrm{e}^{-x}\right) \geqslant-\frac{2}{\mathrm{e}}
$$

且等号无法取得, 原命题得证.

## 第 942 题 - 念之差

已知 $f(x)=\ln x-x^{3}+2 e x^{2}-a x$ 有 2 个零点, 求实数 $a$ 的取值范围.

解析 解法一 问题可以转化为函数

$$
g(x)=\frac{\ln x}{x}-x^{2}+2 \mathrm{e} x
$$

的图象与直线 $y=a$ 有两个公共点.

而 $g(x)$ 的导函数

$$
g^{\prime}(x)=2(\mathrm{e}-x)+\frac{1-\ln x}{x}
$$

于是函数 $g(x)$ 在 $(0, \mathrm{e})$ 上单调递增, 在 $(\mathrm{e},+\infty)$ 上单调递减, 在 $x=\mathrm{e}$ 处取得极大值, 亦为最大值

$$
g(\mathrm{e})=\mathrm{e}^{2}+\mathrm{e}^{-1}
$$

考虑到当 $0<x<1$ 时, 有

$$
f(x)<\ln x+2 \mathrm{e}+|a|
$$

于是取 $x_{1}=\min \left\{\mathrm{e}^{-2 \mathrm{e}-|a|}, 1\right\}$,则 $f\left(x_{1}\right)<0$;

而

$$
f(x)<x-x^{3}+2 \mathrm{e} x^{2}+|a| x,
$$

取 $x_{2}=\max \{2 \mathrm{e}, \sqrt{3|a|}\}$, 则有 $f\left(x_{2}\right)<0$,于是 $a$ 的取值范围是 $\left(-\infty, \mathrm{e}^{2}+\mathrm{e}^{-1}\right)$.

## 解法二 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{-3 x^{3}+4 e x^{2}+1}{x}-a,
$$

其极值点 $x=x_{0}$ 满足

$$
-3 x_{0}^{3}+4 \mathrm{e} x_{0}^{2}+1-a x_{0}=0,
$$

因此对应的极值为

$$
\begin{aligned}
f\left(x_{0}\right) & =\ln x_{0}-x_{0}^{3}+2 \mathrm{e} x_{0}^{2}-a x_{0} \\
& =\ln x_{0}+2 x_{0}^{3}-2 \mathrm{e} x_{0}^{2}-1 .
\end{aligned}
$$

记

$$
\varphi(x)=\ln x+2 x^{3}-2 \mathrm{e} x^{2}-1,
$$

则其导函数

$$
\varphi^{\prime}(x)=\frac{6 x^{3}-4 \mathrm{e} x^{2}+1}{x}, x>0
$$

于是函数 $\varphi(x)$ 先单调递增, 再单调递减, 然后单调递增. 不难证明它的极值小于 0 , 因此有唯一零点 $x$ $=\mathrm{e}$.

函数 $\varphi(x)$ 的图象如图 1.

考虑函数

$$
a(x)=\frac{-3 x^{3}+4 \mathrm{e} x^{2}+1}{x}
$$

函数 $a(x)$ 的导函数

$$
a^{\prime}(x)=\frac{-6 x^{3}+4 \mathrm{e} x^{2}-1}{x^{2}}
$$

因此其图象如图 2.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-354.jpg?height=295&width=262&top_left_y=527&top_left_x=1504)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-354.jpg?height=320&width=326&top_left_y=888&top_left_x=1440)

图 2

这样我们就得到了讨论的分界点 $a(\mathrm{e})=\mathrm{e}^{2}+\mathrm{e}^{-1}$, 分类讨论如下.

情形一 $a>\mathrm{e}^{2}+\mathrm{e}^{-1}$.

此时对应的极值点 (即 $a=a(x)$ 的解 $x_{i}$ ) 都小于 $\mathrm{e}$, 因此极值 $\left(\varphi\left(x_{i}\right)\right)$ 均小于 0 , 不符合题意;

情形ニ $a=\mathrm{e}^{2}+\mathrm{e}^{-1}$.

此时对应两个极值点小于 $e$, 最大的极值点为 $e$, 因此有两个极值小于 0 , 极大值亦最大值为 0 , 不符合题意;

情形三 $a<\mathrm{e}^{2}+\mathrm{e}^{-1}$.

此时最大的极值点大于 $e$, 对应的极大值亦最大值大于 0 , 且其他极值 (如果存在的话) 均小于 0 , 再结合函数的单调性和极限 (根据 $a$ 与 $a(x)$ 的大小关系), 可知函数 $f(x)$ 的零点个数为 2 个, 符合题意.

综上所述, 实数 $a$ 的取值范围是 $\left(-\infty, \mathrm{e}^{2}+\mathrm{e}^{-1}\right)$.

## 第 943 题 函数的最值

已知函数 $f(x)=\left(x^{2}+a x-a\right) \cdot \mathrm{e}^{1-x}$, 其中 $a \in \mathbf{R}$.

(1) 求函数 $f^{\prime}(x)$ 的零点个数;

(2) 证明: $a \geqslant 0$ 是函数 $f(x)$ 存在最小值的充分不必要条件.

解析 (1) 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=-(x-2)(x+a) \cdot \mathrm{e}^{1-x},
$$

因此当 $a \neq-2$ 时, 函数 $f^{\prime}(x)$ 的零点个数为 2 ; 当 $a=-2$ 时, 函数 $f^{\prime}(x)$ 的零点个数为 1 .

(2) 情形一 当 $a<-2$ 时, 函数 $f(x)$ 在 $(-\infty, 2)$ 上单调递减, 在 $(2,-a)$ 上单调递增, 在 $(-a,+\infty)$ 上单调递减.

考虑到 $f(2)=(4+a) \cdot \mathrm{e}^{-1}$, 而当 $x>-a$ 时,有

$$
f(x)=[x(x+a)-a] \cdot \mathrm{e}^{1-x}>0,
$$

因此当 $a \leqslant-4$ 时, 函数 $f(x)$ 存在最小值. (注意, $a \leqslant-4$ 只是函数有最小值的充分条件, 没有论证必要性)

情形二 当 $a=-2$ 时,函数 $f(x)$ 单调递减,没有最小值.
情形三 当 $a>-2$ 时, 函数 $f(x)$ 在 $(-\infty,-a)$ 上单调递减, 在 $(-a, 2)$ 上单调递增, 在 $(2,+\infty)$ 上单调递减.

考虑到 $f(-a)=-a \mathrm{e}^{1+a}$, 而当 $x>2$ 时, 有

$$
f(x)>(4+2 a-a) \cdot \mathrm{e}^{1-x}>0
$$

因此当 $a \geqslant 0$ 时,函数 $f(x)$ 存在最小值.

综上所述, $a \geqslant 0$ 是函数 $f(x)$ 存在最小值的充分不必要条件.

## 第 944 题 先构造再论证

已知 $f(x)=8 x^{3}+a x^{2}+b x$, 是否存在实数 $a, b$, 使得对任意 $x \in[-1,1]$, 均有 $|f(x)| \leqslant 2$. 若存在,求出 $a, b$ 的值;若不存在, 请说明理由.

解析 根据题意,有

$$
\left\{\begin{array}{l}
f(1)=a+b+8 \\
f(-1)=a-b-8 \\
f\left(\frac{1}{2}\right)=\frac{1}{4} a+\frac{1}{2} b+1 \\
f\left(-\frac{1}{2}\right)=\frac{1}{4} a-\frac{1}{2} b-1
\end{array}\right.
$$

于是

$$
\left\{\begin{array}{l}
a=\frac{1}{2} f(1)+\frac{1}{2} f(-1)=2 f\left(\frac{1}{2}\right)+2 f\left(-\frac{1}{2}\right) \\
b=\frac{1}{2} f(1)-\frac{1}{2} f(-1)-8=f\left(\frac{1}{2}\right)-f\left(-\frac{1}{2}\right)-2
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-355.jpg?height=426&width=296&top_left_y=1004&top_left_x=1591)

由第二个等式可得

$$
\frac{1}{2} f(1)-\frac{1}{2} f(-1)-f\left(\frac{1}{2}\right)+f\left(-\frac{1}{2}\right)=6
$$

而

$$
\begin{aligned}
& \frac{1}{2} f(1)-\frac{1}{2} f(-1)-f\left(\frac{1}{2}\right)+f\left(-\frac{1}{2}\right) \\
\leqslant & \frac{1}{2}|f(1)|+\frac{1}{2}|f(-1)|+\left|f\left(\frac{1}{2}\right)\right|+\left|f\left(-\frac{1}{2}\right)\right| \\
\leqslant & 6
\end{aligned}
$$

等号当且仅当 $f(1)=f\left(-\frac{1}{2}\right)=2, f(-1)=f\left(\frac{1}{2}\right)=-2$ 时取得,

因此 $a=0, b=-6$.

思考与总结

先构造出符合题意的三次函数, 再根据图形的特征进行论证.

## 第 945 题 三次函数的图象

函数 $f(x)=a x^{3}+b x^{2}+c x+d$ 的图象如图 1 所示,则下列结论中成立的是
A. $a>0, b<0, c>0, d>0$
B. $a>0, b<0, c<0, d>0$
C. $a<0, b<0, c>0, d>0$
D. $a>0, b<0, c>0, d<0$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-356.jpg?height=334&width=324&top_left_y=470&top_left_x=1413)

图 1

解析 A.

解法一 如图 2 , 根据函数 $f(x)$ 的图象在 $x=0$ 和 $x \rightarrow+\infty$ 的取值可以得到 $d>$ $0, a>0 ;$

根据导函数 $f^{\prime}(x)=3 a x^{2}+2 b x+c$ 的两根之和、两根之积均大于零可以得到 $b<$ $0, c>0$.

综上所述, 结论成立的是 A.

解法二 根据函数 $f(x)$ 的图象在 $x=0$ 和 $x \rightarrow+\infty$ 的取值可以得到 $d>0, a>0$;进而考虑直线 $y=d$ 与函数 $y=f(x)$ 图象的公共点的横坐标, 即方程

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-356.jpg?height=334&width=331&top_left_y=957&top_left_x=1442)

图 2

$$
a x^{2}+b x+c=0
$$

的两根均为正数. 因此 $b<0, c>0$.

综上所述, 结论成立的是 A.

## 第 946 题 摸着石头过河

已知函数 $f(x)=\frac{\ln x}{1+x}-\ln x+\ln (x+1)$, 是否存在实数 $a$, 使得关于 $x$ 的不等式 $f(x) \geqslant a$ 的解集为 $(0,+\infty)$ ? 若存在, 求 $a$ 的取值范围;若不存在, 请说明理由.

解析 不等式 $f(x) \geqslant a$ 即

$$
(x+1) \ln (x+1)-x \ln x \geqslant a(x+1),
$$

注意到

$$
\lim _{x \rightarrow 0^{+}} x \ln x=0,
$$

于是当 $x \rightarrow 0^{+}$时, 左边趋于 0 , 因此 $a \leqslant 0$. 下面进行讨论.

情形一 $a \leqslant 0$.

此时

$$
(x+1) \ln (x+1)-x \ln x=x \cdot \ln \frac{x+1}{x}+\ln (x+1)>0 \geqslant a(x+1)
$$

符合题意.

情形ニ $a>0$.
我们去寻找 $x_{0}$, 使 $\left(x_{0}+1\right) \ln \left(x_{0}+1\right)<\frac{a}{2}$ 和 $x_{0} \ln \frac{1}{x_{0}}<\frac{a}{2}$ 同时成立, 这样就有当 $x=x_{0}$ 时, 有

$$
\left(x_{0}+1\right) \ln \left(x_{0}+1\right)+x_{0} \ln \frac{1}{x_{0}}<\frac{a}{2}+\frac{a}{2}=a<a\left(x_{0}+1\right),
$$

不符合题意.

先寻找 $(x+1) \ln (x+1)<\frac{a}{2}$ 的充分条件.

由于

$$
(x+1) \ln (x+1)<x(x+1)=x^{2}+x,
$$

于是当 $0<x<\frac{-1+\sqrt{1+2 a}}{2}$ 时, 就有

$$
(x+1) \ln (x+1)<x^{2}+x<\frac{a}{2}
$$

再寻找 $x \ln \frac{1}{x}<\frac{a}{2}$ 的充分条件, 由于

$$
x \ln \frac{1}{x}<x \cdot 2\left(\frac{1}{\sqrt{x}}-1\right)=2 \sqrt{x}-2 x<2 \sqrt{x},
$$

于是当 $x<\frac{a^{2}}{16}$ 时, 就有

$$
x \ln \frac{1}{x}<2 \sqrt{x}<\frac{a}{2}
$$

综上,取

$$
x_{0}=\frac{1}{2} \min \left\{\frac{-1+\sqrt{1+2 a}}{2}, \frac{a^{2}}{16}\right\}
$$

即可, 所以 $a>0$ 时不满足条件.

综合以上两种情形, $a$ 的取值范围是 $(-\infty, 0]$.

## 第 947 题 两边夹

若不等式 $\left(\frac{1}{x-1}+a\right) \cdot \ln x>1$ 对一切 $x>0$ 且 $x \neq 1$ 均成立, 求实数 $a$ 的值.

解析 首先分析端点, 当 $x \rightarrow 0$ 和 $x \rightarrow+\infty$ 时, 可得 $0 \leqslant a \leqslant 1$.

于是可得

$$
\frac{1}{x-1}+a=\frac{a x-a+1}{x-1}
$$

的分子部分恒正,接下来利用它“清君侧”即可.

易知 $0 \leqslant a \leqslant 1$,于是原不等式等价于

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-357.jpg?height=116&width=624&top_left_y=2246&top_left_x=717)

注意到 $\varphi(1)=0$, 而其导函数

$$
\varphi^{\prime}(x)=\frac{\left[a^{2} x-(1-a)^{2}\right] \cdot(x-1)}{x(a x-a+1)^{2}}
$$

接下来根据 $a$ 与 $\frac{1}{2}$ 的大小关系展开讨论.
情形一 $a=\frac{1}{2}$.

此时在 $(0,+\infty)$ 上, $\varphi^{\prime}(x) \geqslant 0$, 于是 $\varphi(x)$ 在 $(0,+\infty)$ 上单调递增, 结合 $\varphi(1)=0$, 符合题意;

情形ニ $a=0$.

此时在 $(1,+\infty)$ 上, $\varphi^{\prime}(x)<0$, 于是在 $(1,+\infty)$ 上, $\varphi(x)<\varphi(1)=0$, 不符合题意;

情形三 $0<a<\frac{1}{2}$.

此时在 $\left(1,\left(\frac{1}{a}-1\right)^{2}\right)$ 上, $\varphi^{\prime}(x)<0$, 于是在 $\left(1,\left(\frac{1}{a}-1\right)^{2}\right)$ 上, $\varphi(x)<\varphi(1)=0$, 不符合题意;

情形四 $\quad \frac{1}{2}<a \leqslant 1$.

此时在 $\left(\left(\frac{1}{a}-1\right)^{2}, 1\right)$ 上, $\varphi^{\prime}(x)<0$, 于是在 $\left(\left(\frac{1}{a}-1\right)^{2}, 1\right)$ 上, $\varphi(x)>\varphi(1)=0$, 不符合题意.

综上, 实数 $a$ 的值为 $\frac{1}{2}$.

此时函数 $y=\left(\frac{1}{x-1}+\frac{1}{2}\right) \cdot \ln x-1$ 的图象如图:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-358.jpg?height=238&width=592&top_left_y=1175&top_left_x=627)

## 第 948 题 对数函数遇见恒成立

已知 $f(x)=x+x \ln x$, 若 $k \in \mathbf{Z}$, 且 $k(x-2)<f(x)$ 对任意 $x>2$ 恒成立, 则 $k$ 的最大值为

解析 4.

解法一 题意即

$$
\forall x>2, \ln x>(k-1)-\frac{2 k}{x}
$$

即

$$
\forall x \in\left(0, \frac{1}{2}\right), \ln x-2 k x+(k-1)<0
$$

记左侧为函数 $\varphi(x)$, 则

$$
\varphi^{\prime}(x)=\frac{1-2 k x}{x}
$$

于是 $\varphi(x)$ 在 $x=\frac{1}{2 k}$ 处取得极大值, 亦为最大值

$$
\varphi\left(\frac{1}{2 k}\right)=-1+\ln \frac{1}{2 k}+k-1
$$

于是命题转化为

$$
k-2-\ln (2 k)<0,
$$

容易验证 $k$ 的最大值为 4.

## 解法二 题意即

$$
\forall x>2, x \ln x+(1-k) x+2 k>0
$$

记左边为函数 $g(x)$, 则 $g^{\prime}(x)=2-k+\ln x$ 是增函数, 因为是考虑 $k$ 的最大值, 所以考虑 $g^{\prime}(x)$ 有零点的情况, 此时当 $x_{0}=\mathrm{e}^{k-2}$ 时, $g(x)$ 取到最小值

$$
g\left(x_{0}\right)=\mathrm{e}^{k-2} \cdot(k-2)+(1-k) \mathrm{e}^{k-2}+2 k=2 k-\mathrm{e}^{k-2},
$$

所以 $g\left(x_{0}\right)>0$ 即 $2 k-\mathrm{e}^{k-2}>0$, 所以 $k=4$ 为最大值.

解法三 题意即

$$
\forall x>2, k<\frac{x+x \ln x}{x-2},
$$

设右边为函数 $\varphi(x)$, 则

$$
\varphi^{\prime}(x)=\frac{x-2 \ln x-4}{(x-2)^{2}}
$$

由于

$$
(x-2 \ln x-4)^{\prime}=1-\frac{2}{x}>0
$$

于是 $\varphi^{\prime}(x)$ 有唯一零点 $x_{0} \in(8,10)$, 从而 $\varphi(x)$ 的极小值, 亦为最小值

$$
\varphi\left(x_{0}\right)=\frac{x_{0}+x_{0} \ln x_{0}}{x_{0}-2}=\frac{x_{0}+x_{0} \cdot \frac{1}{2}\left(x_{0}-4\right)}{x_{0}-2}=\frac{x_{0}}{2} \in(4,5)
$$

于是 $k$ 的最大值为 4 .

解法四 根据题意, 有

$$
\forall x>2, k<\frac{x+x \ln x}{x-2}
$$

记右侧为函数 $\varphi(x)$, 则其导函数

$$
\varphi^{\prime}(x)=\frac{x-2 \ln x-4}{(x-2)^{2}}
$$

因此 $\varphi(x)$ 在 $(2,+\infty)$ 上存在极小值点, 亦为最小值点, 记为 $x=m$, 可以估计 $m$ 在 8 附近, 可得必要条件

$$
k<\frac{8+8 \ln 8}{6}<\frac{8+24 \cdot \frac{3}{4}}{6}=\frac{13}{3}
$$

于是尝试证明 $k$ 的最大值为 4 , 只需要验证 $k$ 可以取到 4 .

当 $k=4$ 时, 欲证结论为

$$
\forall x>2,4(x-2)<x+x \ln x
$$

即

$$
\forall x>2, \ln x+\frac{8}{x}-3>0,
$$

记左侧为函数 $\mu(x)$, 则其导函数

$$
\mu^{\prime}(x)=\frac{x-8}{x^{2}}
$$

于是 $\mu(x)$ 在 $x=8$ 处取得极小值, 亦为最小值

$$
\mu(8)=\ln 8-2>0
$$

符合题意.
综上所述, $k$ 的最大值为 4 .

## 第 949 题 端点效应

若对任意实数 $x \in[0,1]$, 均有不等式 $\sqrt{1-x}+\sqrt{1+x} \leqslant 2-b x^{2}$ 恒成立, 则 $b$ 的最大值为

解析 $\frac{1}{4}$.

令 $f(x)=\sqrt{1-x}+\sqrt{1+x}-2+b x^{2}$, 接下来先通过端点分析得到 $b$ 取值的必要条件.

分析 $\quad$ 分析端点 $x=1$, 可得 $b \leqslant 2-\sqrt{2} ;$

而分析端点 $x=0$, 有 $f(0)=0$, 进而考虑其导数

$$
f^{\prime}(x)=-\frac{1}{2}(1-x)^{-\frac{1}{2}}+\frac{1}{2}(1+x)^{-\frac{1}{2}}+2 b x
$$

有

$$
f^{\prime}(0)=0,
$$

再求导, 有

$$
f^{\prime \prime}(x)=-\frac{1}{4}(1-x)^{-\frac{3}{2}}-\frac{1}{4}(1+x)^{-\frac{3}{2}}+2 b
$$

有

$$
f^{\prime \prime}(0)=-\frac{1}{2}+2 b
$$

我们知道, 必然有 $f^{\prime \prime}(0) \leqslant 0$ (否则在 0 的右邻域内有 $f^{\prime}(x)$ 单调递增, 因此 $f^{\prime}(x)>0$, 进而 $f(x)$ 单调递增, 矛盾), 从而解得 $b \leqslant \frac{1}{4}$.

论证 接下来证明 $b$ 可以取到 $\frac{1}{4}$, 用分析法.

$$
\begin{aligned}
& \sqrt{1-x}+\sqrt{1+x} \leqslant 2-\frac{1}{4} x^{2} \\
\Leftarrow & 2+2 \sqrt{1-x^{2}} \leqslant 4-x^{2}+\frac{1}{16} x^{4} \\
\Leftarrow & 2 \sqrt{1-x^{2}} \leqslant 2-x^{2} \\
\Leftarrow & 4\left(1-x^{2}\right) \leqslant\left(2-x^{2}\right)^{2} \\
\Leftarrow & 0 \leqslant x^{4} .
\end{aligned}
$$

因此 $b$ 的最大值为 $\frac{1}{4}$.

对含参不等式的恒成立问题, 通过对端点的分析得到参数取值的必要条件, 然后再进行论证 (在解答题的叙述中, 必要性也需要论证). 在解答题中,需要明确地指出邻域以否定 $f^{\prime \prime}(0)>0$ 的可能性.

## 第 950 题 分离对数函数

若不等式 $\frac{\ln x}{x+1}+\frac{1}{x}>\frac{\ln x}{x-1}+\frac{k}{x}$ 在 $x>0$ 且 $x \neq 1$ 时恒成立, 求 $k$ 的取值范围.

解析 $\quad$ 首先处理不等式,原不等式等价于

$$
\frac{\ln x}{x+1}+\frac{1}{x}-\frac{\ln x}{x-1}-\frac{k}{x}>0
$$

整理得

$$
-\frac{2}{x^{2}-1} \cdot \ln x+\frac{1-k}{x}>0
$$

提取因式,有

$$
-\frac{1}{x^{2}-1} \cdot\left[2 \ln x+(k-1)\left(x-\frac{1}{x}\right)\right]>0
$$

设

$$
f(x)=2 \ln x+(k-1) \cdot\left(x-\frac{1}{x}\right)
$$

则题中不等式等价于

$$
\left\{\begin{array}{l}
\forall x \in(0,1), f(x)>0, \\
\forall x \in(1,+\infty), f(x)<0 .
\end{array}\right.
$$

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{1}{x^{2}} \cdot\left[(k-1) x^{2}+2 x+k-1\right]
$$

注意到 $f(1)=0$, 而 $f^{\prime}(1)=2 k$, 于是按 $k$ 与 0,1 的大小关系讨论.

情形 $-k \geqslant 1$. 在区间 $(0,1)$ 上, $f^{\prime}(x)>0$, 进而有 $f(x)<f(1)=0$, 不符合题意;

情形二 $0<k<1$. 在区间 $\left(\frac{-2+\sqrt{4-4(k-1)^{2}}}{2(k-1)}, 1\right)$ 上, $f^{\prime}(x)>0$, 进而有 $f(x)<f(1)=0$, 不符合题意;

情形三 $k \leqslant 0$. 此时在区间 $(0,+\infty)$ 上均有 $f^{\prime}(x) \leqslant 0$, 因此函数 $f(x)$ 是 $(0,+\infty)$ 上的单调递减函数,结合 $f(1)=0$, 符合题意.

综上所述, $k$ 的取值范围是 $(-\infty, 0]$.

'思考与总结

在研究有关对数函数的不等式时, 先设法将与 $\ln x$ 相乘的因式去掉 (有时需要付出分类讨论的代价),这样往往能够使问题得到简化.

## 第 951 题 分析端点

已知函数 $f(x)=\ln \frac{1+x}{1-x}$, 设实数 $k$ 使得 $f(x)>k\left(x+\frac{x^{3}}{3}\right)$ 对 $x \in(0,1)$ 恒成立, 求 $k$ 的最大值.
解析 令 $h(x)=f(x)-k\left(x+\frac{x^{3}}{3}\right)$, 则 $h(x)$ 的导函数

$$
h^{\prime}(x)=\frac{2}{1-x^{2}}-k\left(1+x^{2}\right)=\frac{k x^{4}+(2-k)}{1-x^{2}}
$$

注意到 $h(0)=0$, 于是 $h(x)$ 在 $(0,1)$ 上恒有 $h(x)>0$ 的一个必要条件是

$$
h^{\prime}(0) \geqslant 0,
$$

即 $k \leqslant 2$. 证明如下:

若不然, $k>2$, 此时函数 $h(x)$ 在 $\left(0, \sqrt[4]{\frac{k-2}{k}}\right)$ 上单调递减 (注意, 其中 $\sqrt[4]{\frac{k-2}{k}}<1$ ), 于是

$$
h\left(\sqrt[4]{\frac{k-2}{k}}\right)<h(0)=0
$$

不符合题意.

下面证明 $k$ 可以取到 2:

当 $k=2$ 时, $h(x)$ 的导函数

$$
h^{\prime}(x)=\frac{2}{1-x^{2}}-2\left(1+x^{2}\right)=\frac{2 x^{4}}{1-x^{2}}
$$

当 $x \in(0,1)$ 时, 恒有 $h^{\prime}(x)>0$, 于是 $h(x)$ 在 $(0,1)$ 上单调递增, 从而

$$
h(x)>h(0)=0
$$

满足题意.

## 思考与总结

事实上, 我们对函数 $f(x)=\ln (1+x)$ 有泰勒展开式:

$$
\ln (1+x)=x+\frac{x^{2}}{2}+\frac{x^{3}}{3}+\cdots
$$

因此亦有 $\ln (1-x)=-x+\frac{x^{2}}{2}-\frac{x^{3}}{3}+\cdots$,

两式相减即得

$$
\ln \frac{1+x}{1-x}=2\left(x+\frac{x^{3}}{3}+\cdots\right)
$$

这是估算自然对数的重要公式.

## 第 952 题 充分条件先行

已知 $f(x)=a \ln x+\frac{1-a}{2} x^{2}-x$, 若存在 $x \geqslant 1$, 使得 $f(x)<\frac{a}{a-1}$, 则实数 $a$ 的取值范围是

解析 $(-1-\sqrt{2},-1+\sqrt{2}) \cup(1,+\infty)$.

由于 $f(1)=-\frac{1+a}{2}$, 解不等式

$$
f(1)<\frac{a}{a-1}
$$

即

$$
\frac{a^{2}+2 a-1}{2(a-1)}>0
$$

得 $-1-\sqrt{2}<a<-1+\sqrt{2}$ 或 $a>1$. 这是使得命题成立的充分条件.

考虑 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{a}{x}+(1-a) x-1=\frac{(x-1)[(1-a) x-a]}{x},
$$

当 $f(1) \geqslant \frac{a}{a-1}$ 时, 有 $a \leqslant-1-\sqrt{2}$ 或 $-1+\sqrt{2} \leqslant a<1$, 此时一定有 $1-a>0$.

如果 $\frac{a}{1-a} \leqslant 1$, 则 $f(x)$ 在 $(1,+\infty)$ 上单调递增, 命题不可能成立; 所以只能有 $\frac{a}{1-a}>1$, 此时 $\frac{1}{2}<a<1$, $f(x)$ 在 $(1,+\infty)$ 上有唯一的极小值点 $\frac{a}{1-a}$, 但极小值

$$
f\left(\frac{a}{1-a}\right)=a \ln \frac{a}{1-a}+\frac{a^{2}}{2(1-a)}-\frac{a}{1-a}>\frac{a}{a-1}
$$

不符合题意.

综上所述, $a$ 的取值范围是 $(-1-\sqrt{2},-1+\sqrt{2}) \cup(1,+\infty)$.

通过分析端点, 可以得到恒成立问题的必要条件以及存在性问题的充分条件.

## 第 953 题 抓住分界点

若对任意锐角 $x$, 均有 $\sin x+\tan x-2 x>m x^{2}$, 求实数 $m$ 的取值范围.

解析 考虑函数 $f(x)=\sin x+\tan x-2 x-m x^{2}$, 则其导函数

$$
f^{\prime}(x)=\cos x+\frac{1}{\cos ^{2} x}-2-2 m x
$$

其二阶导函数

$$
f^{\prime \prime}(x)=-\sin x+\frac{2 \sin x}{\cos ^{3} x}-2 m
$$

因此 $f(0)=f^{\prime}(0)=0, f^{\prime \prime}(0)=-2 m$, 得到 $m$ 的讨论分界点为 0 .

情形一 $m \leqslant 0$. 此时

$$
f(x) \geqslant \sin x+\tan x-2 x
$$

设右侧为函数 $\varphi(x)$, 则其导函数

$$
\varphi^{\prime}(x)=\cos x+\frac{1}{\cos ^{2} x}-2>\cos x+\frac{1}{\cos x}-2>0
$$

当 $x \in\left(0, \frac{\pi}{2}\right)$ 时, $\varphi(x)$ 单调递增, 因此

$$
\varphi(x)>\varphi(0)=0,
$$

符合题意.

情形ニ $m>0$. 此时

$$
f^{\prime \prime}(0)=-2 m<0 .
$$

当 $0<x \leqslant \frac{\pi}{3}$ 时, 有

$$
f^{\prime \prime}(x)<15 \sin x-2 m<15 x-2 m
$$

因此取 $x_{0}=\min \left\{\frac{\pi}{3}, \frac{2 m}{15}\right\}$, 则在区间 $\left(0, x_{0}\right)$ 上, 有 $f^{\prime \prime}(x)<0$, 进而结合 $f^{\prime}(0)=0$ 可得 $f^{\prime}(x)<0$, 结合 $f(0)=0$ 得 $f(x)<0$, 不符合题意.

综上所述, 实数 $m$ 的取值范围是 $(-\infty, 0]$.

## 第 954 题 指数函数遇到二次函数

已知 $f(x)=x \mathrm{e}^{x}+a x^{2}-x$, 当 $x \geqslant 0$ 时, $f^{\prime}(x)-f(x) \geqslant(4 a+1) x$ 恒成立, 求实数 $a$ 的取值范围.

解析 $\quad$ 题中不等式即

$$
\mathrm{e}^{x} \geqslant a x^{2}+2 a x+1
$$

令 $g(x)=\mathrm{e}^{x}-\left(a x^{2}+2 a x+1\right)$, 考虑到 $g(0)=0$, 而

$$
g^{\prime}(x)=\mathrm{e}^{x}-2 a x-2 a
$$

于是 $g^{\prime}(0)=1-2 a$, 得到讨论的分界点为 $\frac{1}{2}$.

情形一 $a>\frac{1}{2}$.

此时

$$
g^{\prime \prime}(x)=\mathrm{e}^{x}-2 a
$$

于是在区间 $(0, \ln 2 a)$ 上, $g^{\prime \prime}(x)<0, g^{\prime}(x)$ 单调递减, 结合 $g^{\prime}(0)<0$ 可得 $g^{\prime}(x)<0$, 于是 $g(x)$ 单调递减,结合 $g(0)=0$, 可得 $g(x)<0$, 不符合题意.

情形ニ $a \leqslant \frac{1}{2}$.

此时

$$
g(x) \geqslant \mathrm{e}^{x}-\frac{1}{2} x^{2}-x-1
$$

容易证明

$$
\mathrm{e}^{-x}\left(\frac{1}{2} x^{2}+x+1\right) \leqslant 1
$$

符合题意.

综合以上情形可得, $a$ 的取值范围是 $\left(-\infty, \frac{1}{2}\right]$.

## 第 955 题 界限分明

已知函数 $f(x)=\frac{\sin x}{2+\cos x}(x>0)$ 的图象恒在直线 $y=k x$ 下方, 求 $k$ 的取值范围.

解析 考虑函数

$$
\varphi(x)=\frac{\sin x}{2+\cos x}-k x
$$

则 $\varphi(0)=0$, 其导函数

$$
\varphi^{\prime}(x)=\frac{2 \cos x+1}{(2+\cos x)^{2}}-k
$$

于是由 $\varphi^{\prime}(0)=\frac{1}{3}-k$, 可以得到讨论分界点 $\frac{1}{3}$.

情形 $-k \geqslant \frac{1}{3}$.

此时

$$
\varphi(x) \leqslant \frac{\sin x}{2+\cos x}-\frac{1}{3} x
$$

右侧函数的导函数为

$$
\left.\varphi^{\prime}(x)\right|_{k=\frac{1}{3}}=-\frac{(1-\cos x)^{2}}{3(2+\cos x)^{2}} \leqslant 0
$$

于是 $\varphi(x)$ 在 $(0,+\infty)$ 上单调递减, 符合题意.

情形ニ $k<\frac{1}{3}$.

考虑 $x$ 为锐角的情形, 此时

$$
\begin{aligned}
\varphi(x) & >\frac{1}{3} \sin x-k x \\
& >\frac{1}{3}\left(x-\frac{x^{3}}{6}\right)-k x \\
& =x \cdot \frac{(6-18 k)-x^{2}}{18}
\end{aligned}
$$

于是当 $0<x<\sqrt{6-18 k}$ 时, $\varphi(x)>0$, 不符合题意.

综上所述, $k$ 的取值范围是 $\left[\frac{1}{3},+\infty\right)$.

情形二也可以不通过放缩得到矛盾:

由 $\varphi^{\prime}(0)=\frac{1}{3}-k>0$, 考虑 $\varphi^{\prime}(x)$ 在原点右边的第一个零点 $x_{0}\left(\varphi^{\prime}(x)\right.$ 的图象是一条连续不断的曲线, 如果 $x_{0}$ 不存在, 则 $\varphi^{\prime}(x)>0$ 恒成立, $\varphi(x)>\varphi(0)=0$ 矛盾), 则在区间 $\left(0, x_{0}\right)$ 内, 有 $\varphi^{\prime}(x)>0$, 从而在此区间内, 有 $\varphi(x)>\varphi(0)=0$, 矛盾.

## 第 956 题 指与对的放缩

已知 $a\left(x^{2}-1\right)-\frac{1}{x}-\ln x+\mathrm{e}^{1-x}>0$ 对任意 $x>1$ 恒成立,求 $a$ 的取值范围.

解析 设不等式左侧为函数 $\varphi(x)$, 则其导函数

$$
\varphi^{\prime}(x)=2 a x+\frac{1}{x^{2}}-\frac{1}{x}-\mathrm{e}^{1-x},
$$

考虑到当 $x \rightarrow+\infty$ 时 $\varphi(x)$ 的变化, 以及 $\varphi^{\prime}(1)=2 a-1$, 讨论的分界点为 0 和 $\frac{1}{2}$.

情形一 $a \leqslant 0$.

当 $x>1$ 时, 有

$$
\varphi(x) \leqslant-\frac{1}{x}-\ln x+\mathrm{e}^{1-x}<-\ln x+1
$$

取 $x=\mathrm{e}$ 即得 $\varphi(x)<0$, 不符合题意.

情形二 $0<a<\frac{1}{2}$.

我们熟知

$$
\forall x>1, \ln x<x-1
$$

于是

$$
\forall x>1, \mathrm{e}^{1-x}<\frac{1}{x}
$$

设函数

$$
\mu(x)=a\left(x^{2}-1\right)-\ln x
$$

则其导函数

$$
\mu^{\prime}(x)=\frac{2 a x^{2}-1}{x}
$$

于是在 $x \in\left(1, \sqrt{\frac{1}{2 a}}\right)$ 上, $\mu(x)$ 单调递减, 结合 $\mu(1)=0$, 可得在 $x \in\left(1, \sqrt{\frac{1}{2 a}}\right)$ 上, 有 $\mu(x)<0$, 进而有

$$
\varphi(x)<\mu(x)<0
$$

不符合题意.

情形三 $a \geqslant \frac{1}{2}$.

取 $y=\mathrm{e}^{1-x}$ 在 $x=1$ 处的切线 $y=2-x$, 易证

$$
\forall x>1, \mathrm{e}^{1-x}>2-x,
$$

于是此时

$$
\varphi(x) \geqslant \frac{1}{2}\left(x^{2}-1\right)-\frac{1}{x}-\ln x+2-x
$$

记上式右侧为函数 $v(x)$, 则其导函数

$$
v^{\prime}(x)=\frac{(x-1)^{2}(x+1)}{x^{2}}>0
$$

于是 $v(x)$ 在 $(1,+\infty)$ 上单调递增, 结合 $v(1)=0$ 可得当 $x>1$ 时, $v(x)>0$, 进而当 $x>1$ 时, 有

$$
\varphi(x) \geqslant v(x)>0
$$

符合题意.

综上所述, 实数 $a$ 的取值范围是 $\left[\frac{1}{2},+\infty\right)$.

## 第 957 题 零点问题转化

已知函数 $f(x)=\mathrm{e}^{x}-a x-1, g(x)=\ln x-a x+a$, 若存在 $x_{0} \in(1,2)$, 使得 $f\left(x_{0}\right) g\left(x_{0}\right)<0$, 则实数 $a$ 的取值范围是
解析 $\left(\ln 2, \frac{e^{2}-1}{2}\right)$.

解法一 考虑到 $f(1) g(1)=0$, 而

$$
f(2) g(2)=\left(\mathrm{e}^{2}-2 a-1\right)(\ln 2-a),
$$

因此讨论的分界点为 $a=\ln 2, \frac{\mathrm{e}^{2}-1}{2}$.

情形 $-a \leqslant \ln 2$.

此时在区间 $(1,2)$ 上, 函数 $f(x)$ 单调递增, 而 $f(1)>0$, 因此 $f(x)>0$;

函数 $g(x)$ 或者单调递增, 或者先递增后递减, 而 $g(1), g(2) \geqslant 0$, 因此 $g(x)>0$. 这样就有 $f(x) g(x) \geqslant$ 0 , 不符合题意.

情形ニ $\ln 2<a<\frac{\mathrm{e}^{2}-1}{2}$.

此时 $f(2)>0, g(2)<0$, 符合题意;

情形三 $a \geqslant \frac{\mathrm{e}^{2}-1}{2}$.

此时在区间 $(1,2)$ 上, 函数 $f(x)$ 或者单调递增,或者先递减再递增, 而 $f(1), f(2) \leqslant 0$, 因此 $f(x)<0$; 函数 $g(x)$ 单调递减(因为 $g^{\prime}(x)=\frac{1}{x}-a<0$ ), 而 $g(1)=0$, 因此 $g(x)<0$. 这样就有 $f(x) g(x) \geqslant 0$, 不符合题意.

综上所述, 实数 $a$ 的取值范围是 $\left(\ln 2, \frac{\mathrm{e}^{2}-1}{2}\right)$.

解法二 考虑函数

$$
h(x)=f(x) g(x)=x(x-1)\left(a-\frac{\mathrm{e}^{x}-1}{x}\right)\left(a-\frac{\ln x}{x-1}\right),
$$

要使得 $h(x)<0$ 在 $x \in(1,2)$ 上有解, 只需要 $a$ 的值介于

$$
u(x)=\frac{\mathrm{e}^{x}-1}{x}, v(x)=\frac{\ln x}{x-1}
$$

在某点 $x_{0}$ 处的函数值之间.

对它们分别求导得

$$
\begin{aligned}
& u^{\prime}(x)=\frac{\mathrm{e}^{x}(x-1)+1}{x^{2}}>0 \\
& v^{\prime}(x)=\frac{1-\frac{1}{x}-\ln x}{(x-1)^{2}}=\frac{\ln \frac{1}{x}-\left(\frac{1}{x}-1\right)}{(x-1)^{2}}<0
\end{aligned}
$$

而

$$
u(2)=\frac{1}{2}\left(\mathrm{e}^{2}-1\right), v(2)=\ln 2
$$

它们的草图如图.

所以 $a$ 的取值范围是

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-367.jpg?height=288&width=277&top_left_y=1946&top_left_x=1593)

$$
(v(2), u(2))=\left(\ln 2, \frac{1}{2}\left(\mathrm{e}^{2}-1\right)\right)
$$

## 第 958 题 构造函数估计对数值

将 $\mathrm{e}^{3}, 3^{\mathrm{e}}, \pi^{\mathrm{e}}, \mathrm{e}^{\pi}, 3^{\pi}, \pi^{3}$ 从小到大排列.

解析 首先由同底数及同指数幂的比较方法可得 $3^{\mathrm{e}}<\pi^{\mathrm{e}}<\pi^{3}$.

考虑到比较 $a^{b}$ 与 $b^{a}$ 的大小关系即比较 $\frac{\ln a}{a}$ 与 $\frac{\ln b}{b}$ 的大小关系,

因此构造辅助函数 $f(x)=\frac{\ln x}{x}$.

如图 1 为函数 $f(x)=\frac{\ln x}{x}$ 的图象, 它在 $(0, \mathrm{e})$ 上单调递增, 在 $(\mathrm{e},+\infty)$ 上

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-368.jpg?height=280&width=461&top_left_y=550&top_left_x=1326)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-368.jpg?height=115&width=436&top_left_y=1025&top_left_x=1350)

图 2

于是可得 $\mathrm{e}^{3}>3^{e}, \mathrm{e}^{\pi}>\pi^{e}, 3^{\pi}>\pi^{3}$, 结合之前已经得到的大小关系, 可以画数轴如图 2, 其中 $\mathrm{e}^{3} \in\left(3^{\mathrm{e}}, \pi^{3}\right), \mathrm{e}^{\pi} \in\left(\pi^{\mathrm{e}}, 3^{\pi}\right)$.

接下来的任务就是比较 $\mathrm{e}^{3}$ 与 $\pi^{\mathrm{e}}$ 的大小关系以及 $\mathrm{e}^{\pi}$ 与 $\pi^{3}$ 的大小关系.

与之前的手段类似, 转化为比较 $\ln \pi$ 与 $\frac{3}{\mathrm{e}}$ 以及 $\frac{\pi}{3}$ 的大小.

考虑到

$$
\frac{3}{\mathrm{e}}=1.10 \cdots, \frac{\pi}{3}=1.04 \cdots
$$

因此问题的关键在于如何估计 $\ln \pi$ 的大小.

考虑到

$$
\forall x>0,1-\frac{1}{x} \leqslant \ln x \leqslant x-1,
$$

因此

$$
1-\frac{\mathrm{e}}{\pi}<\ln \frac{\pi}{\mathrm{e}}<\frac{\pi}{\mathrm{e}}-1
$$

于是

$$
\text { 1. } 13<2-\frac{\mathrm{e}}{\pi}<\ln \pi<\frac{\pi}{\mathrm{e}}<1.16 \text {, }
$$

因此

$$
\pi^{e}>e^{3}, \pi^{3}>e^{\pi}
$$

进而

$$
3^{\mathrm{e}}<\mathrm{e}^{3}<\pi^{\mathrm{e}}<\mathrm{e}^{\pi}<\pi^{3}<3^{\pi}
$$

## 第 959 题 极值点偏移问题的齐次化方法

已知函数 $f(x)=\ln x-\frac{1}{x}$ 与 $g(x)=a x$ 的图象交于两点 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 求证: $x_{1} x_{2}>2 \mathrm{e}^{2}$.

解析 根据题意有 $\ln x_{1}-\frac{1}{x_{1}}=a x_{1}, \ln x_{2}-\frac{1}{x_{2}}=a x_{2}$, 两式分别相加、相减可得

$$
\ln \left(x_{1} x_{2}\right)-\frac{x_{1}+x_{2}}{x_{1} x_{2}}=a\left(x_{1}+x_{2}\right), \ln \frac{x_{1}}{x_{2}}+\frac{x_{1}-x_{2}}{x_{1} x_{2}}=a\left(x_{1}-x_{2}\right)
$$

进而消去 $a$, 有

$$
\ln \left(x_{1} x_{2}\right)-2 \cdot \frac{x_{1}+x_{2}}{x_{1} x_{2}}=\frac{x_{1}+x_{2}}{x_{1}-x_{2}} \cdot \ln \frac{x_{1}}{x_{2}}
$$

对于右边, 我们熟知对数函数的一个重要放缩:

$$
2 \cdot \frac{x-1}{x+1}<\ln x<\frac{1}{2}\left(x-\frac{1}{x}\right)(x>1)
$$

不妨假设 $\frac{x_{1}}{x_{2}}>1$, 应用于上式, 有

$$
\ln \left(x_{1} x_{2}\right)-2 \cdot \frac{x_{1}+x_{2}}{x_{1} x_{2}}>2
$$

对于左边, 应用均值不等式, 有

$$
\ln \left(x_{1} x_{2}\right)-2 \cdot \frac{x_{1}+x_{2}}{x_{1} x_{2}}<\ln \left(x_{1} x_{2}\right)-\frac{4}{\sqrt{x_{1} x_{2}}}
$$

综合以上两式可得

$$
\ln \left(x_{1} x_{2}\right)-\frac{4}{\sqrt{x_{1} x_{2}}}>2
$$

由于

$$
\ln \left(2 \mathrm{e}^{2}\right)-\frac{4}{\sqrt{2 \mathrm{e}^{2}}}=2+\ln 2-\frac{2 \sqrt{2}}{\mathrm{e}}<2
$$

而函数 $y=\ln x-\frac{4}{\sqrt{x}}$ 为 $\mathbf{R}^{+}$上的单调递增函数, 因此 $x_{1} x_{2}>2 \mathrm{e}^{2}$, 原命题得证.

$$
\forall x>1,2 \cdot \frac{x-1}{x+1}<\ln x<\frac{1}{2}\left(x-\frac{1}{x}\right)
$$

## 第 960 题 极值点偏移

已知 $0<x_{1}<x_{2}$ 且 $x_{1}+x_{2}=6, f(x)=\frac{x^{3}}{\mathrm{e}^{x}}$, 求证: $f\left(x_{1}\right)<f\left(x_{2}\right)$.

解析 解法一 只需要证明 $\ln f\left(x_{1}\right)<\ln f\left(x_{2}\right)$, 即

$$
3 \ln x_{1}-x_{1}<3 \ln x_{2}-x_{2}
$$

即

$$
\frac{x_{2}-x_{1}}{\ln x_{2}-\ln x_{1}}<3
$$

根据对数平均不等式, 有

$$
\frac{x_{2}-x_{1}}{\ln x_{2}-\ln x_{1}}<\frac{x_{1}+x_{2}}{2}<3
$$

因此原命题得证.

解法二 设 $g(x)=\ln f(x)=3 \ln x-x$, 则其导函数

$$
g^{\prime}(x)=\frac{3}{x}-1
$$

令 $h(x)=g(x)-g(6-x)$, 则其导函数

$$
h^{\prime}(x)=g^{\prime}(x)+g^{\prime}(6-x)=\frac{3}{x}+\frac{3}{6-x}-2 \geqslant \frac{(\sqrt{3}+\sqrt{3})^{2}}{x+(6-x)}-2=0
$$

其中用到柯西不等式.

因此 $h(x)$ 单调递增, 结合 $h(3)=0$, 因此当 $x \in(0,3)$ 时, $g(x)<g(6-x)$, 原命题得证.

## 第 961 题 对数平均值不等式

已知函数 $f(x)=x \ln x-\frac{a}{2} x^{2}-x$ 有两个极值点 $x_{1}, x_{2}$, 求证: $\frac{1}{\ln x_{1}}+\frac{1}{\ln x_{2}}>2 a \mathrm{e}$.

解析 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\ln x-a x
$$

于是

$$
\ln x_{1}-a x_{1}=\ln x_{2}-a x_{2}=0,
$$

即

$$
\frac{\ln x_{1}}{x_{1}}=\frac{\ln x_{2}}{x_{2}}=a
$$

令 $\varphi(x)=\frac{\ln x}{x}$, 则其导函数

$$
\varphi^{\prime}(x)=\frac{1-\ln x}{x^{2}},
$$

于是可得 $0<a<\frac{1}{\mathrm{e}}$, 且 $x_{1}, x_{2}$ 分别在 $x=\mathrm{e}$ 的两侧.

因此

$$
\begin{aligned}
\frac{1}{\ln x_{1}}+\frac{1}{\ln x_{2}} & =\frac{1}{a x_{1}}+\frac{1}{a x_{2}} \\
& =\frac{x_{1}+x_{2}}{2} \cdot \frac{2}{a x_{1} x_{2}} \\
& >\frac{2}{a \sqrt{x_{1} x_{2}}} \\
& >\frac{2}{a} \cdot \frac{\ln x_{1}-\ln x_{2}}{x_{1}-x_{2}} \\
& =2 \\
& >2 a \mathrm{e},
\end{aligned}
$$

原不等式得证.

也可以在函数 $\varphi(x)=\frac{\ln x}{x}$ 中, 令 $t=\frac{1}{\ln x}$, 从而得到 $t_{1}=\frac{1}{\ln x_{1}}$ 与 $t_{2}=\frac{1}{\ln x_{2}}$ 为函数

$$
h(t)=\frac{1}{t} \cdot \mathrm{e}^{-\frac{1}{t}}
$$

的两个零点, 通过证明

$$
h(t)-h(2-t)>0, t>1
$$

得到 $t_{1}+t_{2}>2>2 a e$.

## 第 962 题 极值点偏移问题的对称化方法

已知函数 $f(x)=x \ln x$ 与直线 $y=m$ 交于 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$ 两点.

(1)求证: $0<x_{1} x_{2}<\frac{1}{\mathrm{e}^{2}}$;

(2)求证: $\frac{2}{\mathrm{e}}<x_{1}+x_{2}<1$.

解析 (1) 由于函数 $f(x)$ 的导函数 $f^{\prime}(x)=1+\ln x$, 且

$$
\lim _{x \rightarrow 0^{+}} x \ln x=\lim _{x \rightarrow+\infty} \frac{1}{x} \ln \frac{1}{x}=-\lim _{x \rightarrow+\infty} \frac{\ln x}{x}=-\lim _{x \rightarrow+\infty} \frac{\ln x^{2}}{x^{2}}=-2 \lim _{x \rightarrow+\infty} \frac{\ln x}{x^{2}},
$$

而当 $x>1$ 时,有

$$
0<\frac{\ln x}{x^{2}}<\frac{x-1}{x^{2}}
$$

因此

$$
\lim _{x \rightarrow 0^{+}} x \ln x=-2 \lim _{x \rightarrow+\infty} \frac{\ln x}{x^{2}}=0
$$

其函数图象如图.

不妨设 $x_{1}<x_{2}$, 则有 $0<x_{1}<\frac{1}{\mathrm{e}}<x_{2}<1$.

由于 $x_{2}, \frac{1}{\mathrm{e}^{2} x_{1}}$ 均在区间 $\left(\frac{1}{\mathrm{e}},+\infty\right)$ 上,因此

$$
x_{1} x_{2}<\frac{1}{\mathrm{e}} \Leftarrow x_{2}<\frac{1}{\mathrm{e}^{2} x_{1}} \Leftarrow f\left(x_{2}\right)<f\left(\frac{1}{\mathrm{e}^{2} x_{1}}\right) \Leftarrow f\left(x_{1}\right)<f\left(\frac{1}{\mathrm{e}^{2} x_{1}}\right),
$$

因此只需要证明

$$
f\left(\frac{1}{\mathrm{e}^{2} x}\right)-f(x)>0, x \in\left(0, \frac{1}{\mathrm{e}}\right)
$$

令 $g(x)=f\left(\frac{1}{\mathrm{e}^{2} x}\right)-f(x)$, 则其导函数

$$
g^{\prime}(x)=(1+\ln x)\left(-1+\frac{1}{\mathrm{e}^{2} x^{2}}\right)
$$

显然 $g^{\prime}(x)$ 在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上恒负, 因此 $g(x)$ 在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上单调递减, 结合 $g\left(\frac{1}{\mathrm{e}}\right)=0$, 可得在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上 $g(x)$ $>0$, 命题得证.

也可以用极值点偏移问题的齐次化方法解决.

(2) 与 (1) 类似, 为了证明 $x_{1}+x_{2}>\frac{2}{\mathrm{e}}$, 只需证明

$$
f(x)-f\left(\frac{2}{\mathrm{e}}-x\right)>0, x \in\left(0, \frac{1}{\mathrm{e}}\right)
$$

令 $h(x)=f(x)-f\left(\frac{2}{\mathrm{e}}-x\right)$, 则其导函数

$$
h^{\prime}(x)=\ln [\mathrm{e} x \cdot(2-\mathrm{e} x)]
$$

显然 $h^{\prime}(x)$ 在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上恒负, 因此 $h(x)$ 在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上单调递减, 结合 $h\left(\frac{1}{\mathrm{e}}\right)=0$, 可得在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上, $h(x)$ $>0$, 左边不等式得证.

为了证明 $x_{1}+x_{2}<1$, 只需证明

$$
f(x)-f(1-x)<0, x \in\left(0, \frac{1}{\mathrm{e}}\right)
$$

令 $p(x)=f(x)-f(1-x)$, 则其导函数

$$
p^{\prime}(x)=\ln [\mathrm{e} x \cdot(\mathrm{e}-\mathrm{e} x)]
$$

显然 $p^{\prime}(x)$ 在 $\left(0, \frac{1}{2}\right)$ 上先负后正, 因此 $p(x)$ 先递减再递增, 因此在区间 $\left(0, \frac{1}{2}\right)$ 上 $p(x)<0$, 右边不等式得证.

综上所述,原命题成立.

## 第 963 题 极值点偏移与对称化构造

已知 $f(x)=x-1-\ln x$, 若两相异正实数 $x_{1}, x_{2}$ 满足 $f\left(x_{1}\right)=f\left(x_{2}\right)$, 求证: $f^{\prime}\left(x_{1}\right)+f^{\prime}\left(x_{2}\right)<0$.

解析 由于 $f(x)$ 的导函数 $f^{\prime}(x)=1-\frac{1}{x}$, 于是欲证不等式即 $\frac{1}{x_{1}}+\frac{1}{x_{2}}>2$.

问题转化为:

已知 $g(x)=\ln x+\frac{1}{x}-1$, 若实数 $x_{1}, x_{2}$ 满足 $0<x_{1}<1<x_{2}$ 且 $g\left(x_{1}\right)=$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-372.jpg?height=234&width=417&top_left_y=2178&top_left_x=1351)
$g\left(x_{2}\right)$, 求证: $x_{1}+x_{2}>2$.

我们利用对称化构造辅助命题:

$$
\forall x \in(0,1), g(1+x)<g(1-x)
$$

## 高考数学满分学霸的解题笔记(一千零一题)

引理的证明是容易的, 令函数

$$
h(x)=\ln (1-x)+\frac{1}{1-x}-\ln (1+x)-\frac{1}{1+x},
$$

则其导函数

$$
h^{\prime}(x)=\frac{x}{(1-x)^{2}}-\frac{x}{(1+x)^{2}}>0
$$

而 $h(0)=0$, 于是 $h(x)>0$, 即辅助命题得证.

应用辅助命题我们有

$$
g\left(x_{2}\right)=g\left(x_{1}\right)=g\left[1-\left(1-x_{1}\right)\right]>g\left(2-x_{1}\right),
$$

而 $g(x)$ 在 $(1,+\infty)$ 上单调递增, 于是 $x_{2}>2-x_{1}$, 即 $x_{1}+x_{2}>2$, 从而原命题得证.

## 第 964 题 极值点漂流

已知 $f(x)=x-\ln x$ 的图象与直线 $y=m$ 交于不同的两点 $\left(x_{1}, m\right)$ 和 $\left(x_{2}, m\right)$, 求证: $x_{1} x_{2}^{2}<2$.

解析 解法一 由于函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{x-1}{x}
$$

于是两个公共点分别位于直线 $x=1$ 的两侧, 只需要证明当 $0<x_{1}<1<x_{2}$ 时, $x_{1} x_{2}^{2}<2$, 也即

$$
1<x_{2}<\sqrt{\frac{2}{x_{1}}}
$$

于是问题转化为证明

$$
\forall x \in(0,1), f(x)-f\left(\sqrt{\frac{2}{x}}\right)<0
$$

令 $t=\sqrt{\frac{2}{x}}$, 则 $t>\sqrt{2}$, 欲证命题即

$$
\forall t>\sqrt{2}, 3 \ln t+\frac{2}{t^{2}}-t-\ln 2<0
$$

设左边为函数 $\varphi(t)$, 则导函数

$$
\varphi^{\prime}(t)=\frac{-(t+1)(t-2)^{2}}{t^{3}}<0
$$

于是

$$
\varphi(t)<\varphi(\sqrt{2})=\ln \sqrt{2}-\sqrt{2}+1<0
$$

因此命题得证.

解法二 设 $\frac{x_{2}}{x_{1}}=t$, 且 $t>1$, 则

$$
x_{1}=\frac{\ln t}{t-1}, x_{2}=\frac{t \ln t}{t-1}
$$

于是只需要证明

$$
\frac{\ln t}{t-1} \cdot \frac{t^{2} \ln ^{2} t}{(t-1)^{2}<2}
$$

也即

$$
\ln t<\frac{2^{\frac{1}{3}}(t-1)}{t^{\frac{2}{3}}}
$$

令 $t^{\frac{1}{3}}=x(x>1)$, 只需要证明

$$
2^{\frac{1}{3}}\left(x-\frac{1}{x^{2}}\right)-3 \ln x>0,
$$

记上述不等式左边为函数 $\varphi(x)$, 则

$$
\varphi^{\prime}(x)=\frac{2^{\frac{1}{3}} x^{3}-3 x^{2}+2 \cdot 2^{\frac{1}{3}}}{x^{3}}
$$

设其分子部分为 $\mu(x)$, 则

$$
\mu^{\prime}(x)=3 \cdot 2^{\frac{1}{3}} x^{2}-6 x
$$

于是其在 $(1,+\infty)$ 上的极小值, 亦为最小值为

$$
\mu\left(2^{\frac{2}{3}}\right)=0
$$

因此 $\varphi(x)$ 单调递增, 又 $\varphi(1)=0$, 因此命题得证.

解法三 我们可以证明一个更强的命题:

更强的命题 已知 $f(x)=x-\ln x$ 的图象与直线 $y=m$ 交于不同的两点 $\left(x_{1}, m\right)$ 和 $\left(x_{2}, m\right)$, 则 $x_{1} x_{2}\left(x_{1}\right.$ $\left.+x_{2}\right)<2$.

令 $t=\frac{x_{2}}{x_{1}}$, 则

$$
x_{1}=\frac{\ln t}{t-1}, x_{2}=\frac{t \ln t}{t-1}
$$

于是

$$
x_{1} x_{2}\left(x_{1}+x_{2}\right)=\frac{t(t+1) \ln ^{3} t}{(t-1)^{3}} .
$$

因此只需要证明

$$
\frac{t(t+1) \ln ^{3} t}{(t-1)^{3}}>2
$$

也即

$$
\ln t-(t-1)^{3} \sqrt{\frac{2}{t(t+1)}}<0
$$

记

$$
g(x)=\ln x-(x-1)^{3} \sqrt{\frac{2}{x(x+1)}}
$$

则

$$
\begin{aligned}
g^{\prime}(x) & =\frac{3 x^{\frac{1}{3}}(1+x)^{\frac{4}{3}}-2^{\frac{1}{3}}\left(x^{2}+4 x+1\right)}{3 x^{\frac{4}{3}}(1+x)^{\frac{4}{3}}} \\
& =\frac{A^{3}-B^{3}}{3 x^{\frac{4}{3}}(1+x)^{\frac{4}{3}} \cdot\left(A^{2}+A \cdot B+B^{2}\right)}
\end{aligned}
$$

其中

$$
\left\{\begin{array}{l}
A=3 x^{\frac{1}{3}}(1+x)^{\frac{4}{3}} \\
B=2^{\frac{1}{3}}\left(x^{2}+4 x+1\right)
\end{array}\right.
$$

而

$$
A^{3}-B^{3}=-(x-1)^{4}(x+2)(2 x+1)
$$

于是

$$
g^{\prime}(x)<0 \text {. }
$$

进而

$$
g(x)<g(1)<0 .
$$

命题得证.

## 第 965 题 极值点漂流

设 $x>1, f(x)=x \ln x, g(x)=x \mathrm{e}^{-x}, h(x)=\min \{f(x), g(x)\}$. 记 $p(x)=f(x)-g(x)$ 的零点为 $x_{0}$且 $h\left(x_{1}\right)=h\left(x_{2}\right)$, 比较 $2 x_{0}$ 与 $x_{1}+x_{2}$ 的大小.

解析 函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=1+\ln x,
$$

于是函数 $f(x)$ 在 $\left(0, \frac{1}{\mathrm{e}}\right)$ 上单调递减, 在 $\left(\frac{1}{\mathrm{e}},+\infty\right)$ 上单调递增.

函数 $g(x)$ 的导函数

$$
g^{\prime}(x)=\mathrm{e}^{-x}(1-x)
$$

于是函数 $g(x)$ 在 $(0,1)$ 上单调递增, 在 $(1,+\infty)$ 上单调递减.

画出 $f(x)$ 和 $g(x)$ 的草图, 可以猜测 $x_{1}+x_{2}>2 x_{0}$.

根据题意有 $\ln x_{0}=\mathrm{e}^{-x_{0}}$.

接下来我们证明 $x_{1}+x_{2}>2 x_{0}$.

不妨设 $1<x_{1}<x_{0}<x_{2}$. 欲证明 $x_{1}+x_{2}>2 x_{0}$, 只需要证明 $x_{2}>2 x_{0}-x_{1}$. 考虑到 $x_{2}$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-375.jpg?height=273&width=276&top_left_y=1160&top_left_x=1588)
和 $2 x_{0}-x_{1}$ 均在 $g(x)$ 的单调递减区间, 因此只需要

$$
g\left(x_{2}\right)<g\left(2 x_{0}-x_{1}\right),
$$

也即

$$
f\left(x_{1}\right)<g\left(2 x_{0}-x_{1}\right),
$$

于是只需要证明

$$
\forall x_{1} \in\left(1, x_{0}\right), x_{1} \ln x_{1}<\left(2 x_{0}-x_{1}\right) \mathrm{e}^{x_{1}-2 x_{0}} .
$$

设函数 $\varphi(x)=\mathrm{e}^{x-2 x_{0}}\left(\frac{2 x_{0}}{x}-1\right)-\ln x$, 则只需要证明该函数在 $x \in\left(1, x_{0}\right)$ 上有 $\varphi(x)>0$.

函数 $\varphi(x)$ 的导函数

$$
\varphi^{\prime}(x)=\frac{\mathrm{e}^{x-2 x_{0}}}{x^{2}} \cdot\left[-\left(x-x_{0}\right)^{2}+x_{0}\left(x_{0}-2\right)\right]-\frac{1}{x}<0,
$$

于是有

$$
\varphi(x)>\varphi\left(x_{0}\right)=0,
$$

命题得证.

## 第 966 题 构造二次函数

已知函数 $f(x)=\frac{(x-1) \ln x}{x}$, 且 $f\left(x_{1}\right)=f\left(x_{2}\right), x_{1} \neq x_{2}$, 求证: $x_{1}+x_{2}>2$.
解析 解法一 对 $f(x)$ 求导得

$$
f^{\prime}(x)=\frac{x^{2}-x+\ln x}{x^{2}}
$$

构造函数 $g(x)=(x-1)^{2}$ 即可.

考虑函数

$$
f(x)-g(x)=\frac{x-1}{x}\left(\ln x-x^{2}+x\right)
$$

记 $h(x)=\ln x-x^{2}+x$, 则

$$
h^{\prime}(x)=\frac{1}{x}-2 x+1=\frac{(1-x)(1+2 x)}{x}
$$

所以 $h(x)$ 在 $(0,1)$ 上单调递增, 在 $(1,+\infty)$ 上单调递减.

又因为 $h(1)=0$, 所以 $h(x) \leqslant 0$. 从而有当 $x \in(0,1)$ 时, $f(x)>g(x)$; 当 $x \in(1,+\infty)$ 时, $f(x)<g(x)$.

因为 $f\left(x_{1}\right)=f\left(x_{2}\right)>0$, 所以存在 $x_{3}<1<x_{4}$, 满足 $g\left(x_{3}\right)=g\left(x_{4}\right)=f\left(x_{1}\right)=f\left(x_{2}\right)$, 结合上面 $f(x)$ 与 $g(x)$ 的大小关系有 $x_{3}<x_{1}<1<x_{4}<x_{2}$, 从而有 $x_{1}+x_{2}>x_{3}+x_{4}=2$.

思考与总结

通过构造二次函数去证明极值点的偏移, 常用于证明偏移的点对应的是极值点的情况, 可以有效地减少运算量. 所构造的二次函数的极值点与题中函数的极值点重合, 通过二次函数的对称性, 以及它与函数在极值点两侧的位置关系得到想要的结果.

解法二 对 $f(x)$ 求导得

$$
f^{\prime}(x)=\frac{x^{2}-x+\ln x}{x^{2}}
$$

$f(x)$ 在 $(1,+\infty)$ 上单调递增, 不妨设 $x_{1}<x_{2}$, 证明 $f\left(x_{2}\right)=f\left(x_{1}\right)>f\left(2-x_{1}\right)$ 即可, 即证明

$$
\forall x \in(0,1), f(x)-f(2-x)>0
$$

记 $g(x)=f(x)-f(2-x)$, 因为

$$
\forall x \in(0,1), f^{\prime}(x)<0 ; \forall x>1, f^{\prime}(x)>0,
$$

所以

$$
\forall x \in(0,1), g^{\prime}(x)=f^{\prime}(x)+f^{\prime}(2-x)<0,
$$

从而有 $g(x)$ 在 $(0,1)$ 上单调递减, $g(x)>g(1)=0$.

## 第 967 题 公中捉鳖

已知 $x_{1}^{2} \ln x_{1}=x_{2}^{2} \ln x_{2}$, 且 $x_{1}<x_{2}$, 若整数 $k=\frac{5}{2}\left(x_{1}^{2}+x_{2}^{2}+2 x_{1} x_{2}\right)$, 求 $k$ 的值.

解析 问题即函数 $y=x^{2} \ln x$ 与 $y=a$ 的图象的两个公共点的横坐标设为 $x_{1}, x_{2}$, 估计 $x_{1}+x_{2}$ 的范围.

事实上,我们有

$$
1<x_{1}+x_{2}<\frac{2}{\sqrt{\mathrm{e}}}
$$

下面对此不等式进行证明:

由于 $f(x)=x^{2} \ln x$ 的导函数

$$
f^{\prime}(x)=x(1+2 \ln x)
$$

于是函数 $f(x)$ 在 $x=\frac{1}{\sqrt{\mathrm{e}}}$ 处取得极小值, 如图.

容易知道

$$
0<x_{1}<\frac{1}{\sqrt{\mathrm{e}}}<x_{2}<1
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-377.jpg?height=265&width=555&top_left_y=201&top_left_x=1313)

只需要证明

$$
1-x_{1}<x_{2}<\frac{2}{\sqrt{\mathrm{e}}}-x_{1}
$$

可以转化为证明

$$
\left\{\begin{array}{l}
\forall x \in\left(0, \frac{1}{2}\right), f(x)>f(1-x) \\
\forall x \in\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right), f(x)<f\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)
\end{array}\right.
$$

设 $\varphi(x)=f(x)-f(1-x), \mu(x)=f(x)-f\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)$, 则

$$
\begin{aligned}
& \varphi^{\prime}(x)=f^{\prime}(x)+f^{\prime}(1-x)=2 x \ln x+2(1-x) \ln (1-x)+1, \\
& \varphi^{\prime \prime}(x)=f^{\prime \prime}(x)-f^{\prime \prime}(1-x)=2 \ln x-2 \ln (1-x),
\end{aligned}
$$

在 $\left(0, \frac{1}{2}\right)$ 上, $\varphi^{\prime}(x)$ 单调递减, 结合 $\varphi^{\prime}\left(\frac{1}{2}\right)<0, \lim _{x \rightarrow 0^{+}} \varphi^{\prime}(x)=0$, 于是 $\varphi(x)$ 在 $\left(0, \frac{1}{2}\right)$ 上先单调递增, 后单调递减.

结合

$$
\lim _{x \rightarrow 0^{+}} \varphi(x)=\varphi\left(\frac{1}{2}\right)=0
$$

可得当 $x \in\left(0, \frac{1}{2}\right)$ 时, $\varphi(x)>0$, 而

$$
\begin{aligned}
& \mu^{\prime}(x)=f^{\prime}(x)+f^{\prime}\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)=\frac{2}{\sqrt{\mathrm{e}}}+x \ln x+\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right) \ln \left(\frac{2}{\sqrt{\mathrm{e}}}-x\right) \\
& \mu^{\prime \prime}(x)=f^{\prime \prime}(x)-f^{\prime \prime}\left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)=2 \ln x-2 \ln \left(\frac{2}{\sqrt{\mathrm{e}}}-x\right)
\end{aligned}
$$

于是 $\mu^{\prime}(x)$ 在 $\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right)$ 上单调递减, 结合 $\mu^{\prime}\left(\frac{1}{\sqrt{\mathrm{e}}}\right)>0$, 可得当 $x \in\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right)$ 时, $\mu^{\prime}(x)>0, \mu(x)$ 单调递增, 结合 $\mu\left(\frac{1}{\sqrt{\mathrm{e}}}\right)=0$, 可得当 $x \in\left(0, \frac{1}{\sqrt{\mathrm{e}}}\right)$ 时, $\mu(x)<0$.

综上所述,我们得到了

$$
k=\frac{5}{2}\left(x_{1}+x_{2}\right)^{2}
$$

的范围是 $\left(\frac{5}{2}, \frac{10}{\mathrm{e}}\right)$, 于是 $k$ 的值为 3 .

## 第 968 题 函数的叠加

已知函数 $f(x)=x^{2} \ln x+a\left(x^{2}-x\right)(a>0)$, 方程 $f(x)=m$ 有两个不相等的实数根 $x_{1}, x_{2}$, 求证: $x_{1}$ $+x_{2}>1$
解析 函数 $f(x)$ 由两个部分组成, 其中函数 $y=a\left(x^{2}-x\right)$ 的对称轴为 $x=\frac{1}{2}$,

而函数 $y=x^{2} \ln x$, 由于其导函数

$$
y^{\prime}=x(1+2 \ln x)
$$

于是其极值点为 $x=\frac{1}{\sqrt{\mathrm{e}}}$ 在 $\frac{1}{2}$ 的右侧.

因此合起来的函数 $f(x)$ 的极值点应该会右移, 可以从这个角度人手.

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=2 x \ln x+(2 a+1) x-a,
$$

其二阶导函数

$$
f^{\prime \prime}(x)=2 \ln x+2 a+3
$$

注意到 $f^{\prime \prime}(x)$ 单调递增有唯一零点, 因此 $f^{\prime}(x)$ 先递减后递增.

又考虑到

$$
\lim _{x \rightarrow 0} f^{\prime}(x)=-a<0, f^{\prime}(1)=a+1>0
$$

因此函数 $f^{\prime}(x)$ 有唯一零点 $x_{0} \in(0,1)$, 且在 $\left(0, x_{0}\right)$ 上有 $f^{\prime}(x)<0$, 在 $\left(x_{0},+\infty\right)$ 上有 $f^{\prime}(x)>0$.

进而 $f(x)$ 先递减后递增, 注意到

$$
\lim _{x \rightarrow 0} f(x)=0, f(1)=0,
$$

因此函数图象如图. 由于

$$
f^{\prime}\left(\frac{1}{2}\right)=\frac{1}{2}+\ln \frac{1}{2}<0
$$

于是 $f(x)$ 在 $\left(0, \frac{1}{2}\right]$ 上单调递减, 不妨设 $x_{1}<x_{2}$, 则有 $0<x_{1}<x_{2}<1$ 且 $x_{2}$ $>\frac{1}{2}$.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-378.jpg?height=371&width=398&top_left_y=1156&top_left_x=1372)

情形 $-\frac{1}{2} \leqslant x_{1}<x_{2}<1$, 此时命题显然成立;

情形二 $\quad 0<x_{1}<\frac{1}{2}<x_{2}<1$. 对称化构造函数, 接下来证明辅助命题

$$
\forall x \in\left(\frac{1}{2}, 1\right), f(x)<f(1-x)
$$

即

$$
\forall x \in\left(\frac{1}{2}, 1\right), x^{2} \ln x-(1-x)^{2} \ln (1-x)<0
$$

设 $g(x)=x^{2} \ln x-(1-x)^{2} \ln (1-x), x \in\left[\frac{1}{2}, 1\right)$, 则其导函数

$$
g^{\prime}(x)=1+2 x \ln x+2(1-x) \ln (1-x),
$$

其二阶导函数

$$
g^{\prime \prime}(x)=2 \ln x-2 \ln (1-x) \geqslant 0
$$

于是 $g^{\prime}(x)$ 单调递增, 考虑到

$$
g^{\prime}\left(\frac{1}{2}\right)<0, \lim _{x \rightarrow 1} g^{\prime}(x)=1
$$

于是 $g(x)$ 在 $\left(\frac{1}{2}, 1\right)$ 上先单调递减, 再单调递增, 又

$$
g\left(\frac{1}{2}\right)=0, \lim _{x \rightarrow 1} g(x)=0
$$

## 高考数学满分学霸的解题笔记(一千零一龄)

因此 $g(x)$ 在 $\left(\frac{1}{2}, 1\right)$ 上有 $g(x)<0$, 也即辅助命题得证.

应用辅助命题, 有

$$
f\left(x_{1}\right)=f\left(x_{2}\right)<f\left(1-x_{2}\right),
$$

又 $x_{1}, 1-x_{2} \in\left(0, \frac{1}{2}\right)$, 而 $f(x)$ 在 $\left(0, \frac{1}{2}\right)$ 上单调递减, 从而

$$
x_{1}>1-x_{2}
$$

即

$$
x_{1}+x_{2}>1
$$

综上所述,原命题得证.

## 第 969 题 极值点偏移法

证明: $\sqrt{7}^{\sqrt{8}}>\sqrt{8}^{\sqrt{7}}$. (参考数据: $2.64<\sqrt{7}<2.65,2.82<\sqrt{8}<2.83,2.71<\mathrm{e}<2.72$. )

解析 我们熟知由于函数 $y=\frac{\ln x}{x}$ 在 $(0, \mathrm{e})$ 上单调递增, 在 $(\mathrm{e},+\infty)$ 上单调递减, 于是当 $a, b$ 均在 $\mathrm{e}$ 的同一侧时, 很容易比较 $a^{b}$ 与 $b^{a}$ 的大小关系. 但是 $\sqrt{7}<\mathrm{e}<\sqrt{8}$, 因此我们需要构造极值点偏移不等式, 将它们转化到同一侧.

先给出引理: 如果 $0<x_{1}<\mathrm{e}<x_{2}$, 且 $\frac{\ln x_{1}}{x_{1}}=\frac{\ln x_{2}}{x_{2}}$, 那么

$$
\frac{1}{x_{1}}+\frac{1}{x_{2}}>\frac{2}{\mathrm{e}}
$$

设 $\frac{\ln m}{m}=\frac{\ln \sqrt{8}}{\sqrt{8}}$, 且 $0<m<$ e. 那么根据上述引理, 有

$$
m<\frac{1}{\frac{2}{\mathrm{e}}-\frac{1}{\sqrt{8}}}<\sqrt{7}
$$

再根据函数 $f(x)=\frac{\ln x}{x}$ 在 $(0, \mathrm{e})$ 上单调递增, 有

$$
\frac{\ln m}{m}<\frac{\ln \sqrt{7}}{\sqrt{7}}
$$

即

$$
\frac{\ln \sqrt{8}}{\sqrt{8}}<\frac{\ln \sqrt{7}}{\sqrt{7}}
$$

原不等式得证.

引理的证明中,可令

$$
t_{1}=\frac{1}{x_{1}}, t_{2}=\frac{1}{x_{2}}
$$

后, 从而转化为证明当 $t_{1} \ln t_{1}=t_{2} \ln t_{2}$ 时, $t_{1}+t_{2}>\frac{2}{\mathrm{e}}$. 具体过程略.

选择该极值点偏移不等式是在尝试 $x_{1} x_{2}>\mathrm{e}^{2}$ 以及 $x_{1}+x_{2}>2 \mathrm{e}$ 失败后吸取教训重新探索的.

## 第 970 题 偷梁换柱

求证: $\ln 2<\lg 5$.

解析 先利用换底公式统一底数, 原不等式等价于

$$
\ln 2<\frac{\ln 5}{\ln 2+\ln 5}
$$

即

$$
\ln ^{2} 2+\ln 2 \cdot \ln 5<\ln 5
$$

若考虑用

$$
\ln \frac{1+x}{1-x}=2\left(x+\frac{x^{3}}{3}+\frac{x^{5}}{5}+\cdots\right)
$$

对 $\ln 2$ 和 $\ln 5$ 进行估算, 则需要分别令 $x=\frac{1}{3}$ 和 $x=\frac{2}{3}$.

出于对后者的收玫速度不满, 令 $x=\ln 2, y=\ln \frac{5}{4}=\ln 5-2 \ln 2$, 则只需要证明

$$
x^{2}+x(2 x+y)<2 x+y
$$

即

$$
y>\frac{3 x^{2}-2 x}{1-x}
$$

设 $\varphi(x)=\frac{3 x^{2}-2 x}{1-x}$, 则 $\varphi(x)$ 在 $x \in\left(\frac{1}{2}, 1\right)$ 上单调递增, 因此只需要估计 $x$ 的上界以及 $y$ 的下界.

对于 $x$ 的上界, 由于

$$
\ln \frac{1+x}{1-x}=2\left(x+\frac{x^{3}}{3}+\frac{x^{5}}{5}+\cdots\right)<2\left[x+\frac{1}{3}\left(x^{3}+x^{5}+\cdots\right)\right]<2\left[x+\frac{x^{3}}{3\left(1-x^{2}\right)}\right]
$$

令 $x=\frac{1}{3}$, 可得 $\ln 2<\frac{25}{36}$.

对于 $y$ 的下界, 由于

$$
\ln \frac{1+x}{1-x}=2\left(x+\frac{x^{3}}{3}+\frac{x^{5}}{5}+\cdots\right)>2 x
$$

令 $x=\frac{1}{9}$, 可得 $\ln \frac{5}{4}>\frac{2}{9}$.

事实上, 我们有

$$
\varphi(x)<\varphi\left(\frac{25}{36}\right)=\frac{1}{9} \cdot \frac{75}{44}<\frac{2}{9}<\ln \frac{5}{4}=y
$$

因此原命题得证.

$\ln 2 \approx 0.69315$, 而 $\lg 5 \approx 0.69897$, 两者非常接近.

## 第 971 题 下界争霸赛

估计函数 $f(x)=x^{2} \mathrm{e}^{x}-\ln x$ 的下界.

解析 解法一 在 $x=0$ 处对 $\mathrm{e}^{x}$ 进行切线放缩.

由于 $\mathrm{e}^{x}>x+1$,于是

$$
f(x)>g(x)=x^{2}(x+1)-\ln x
$$

而 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{3 x^{2}+2 x^{2}-1}{x}
$$

因此可以解得极小值点

$$
x_{0}=\frac{1}{9}\left[-2+\left(\frac{227}{2}-\frac{9 \sqrt{633}}{2}\right)^{\frac{1}{3}}+\left(\frac{227}{2}+\frac{9 \sqrt{633}}{2}\right)^{\frac{1}{3}}\right]
$$

于是可得 $g(x)$ 的最小值为

$$
g\left(x_{0}\right)>1.0646
$$

这样就得到了 $f(x)$ 的下界 1.0646.

解法二 在 $x=1$ 处对 $\mathrm{e}^{x}$ 进行切线放缩.

由于 $\mathrm{e}^{x}>\mathrm{e} x$, 于是

$$
f(x)>g(x)=\mathrm{e} \cdot x^{3}-\ln x
$$

而 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{3 \mathrm{e} x^{3}-1}{x}
$$

因此可以解得极小值点

$$
x_{0}=\left(\frac{1}{3 \mathrm{e}}\right)^{\frac{1}{3}}
$$

于是可得 $g(x)$ 的最小值为

$$
g\left(x_{0}\right)=\frac{\ln 3+2}{3}>1.0328
$$

这样就得到了 $f(x)$ 的下界 1.0328 .

解法三 在 $x=\frac{1}{2}$ 处进行双切线放缩.

由于

$$
\mathrm{e}^{x} \geqslant \sqrt{\mathrm{e}} x+\frac{\sqrt{\mathrm{e}}}{2}
$$

且

$$
\ln x \leqslant 2 x-1-\ln 2
$$

于是

$$
f(x) \geqslant g(x)=\sqrt{\mathrm{e}} x^{3}+\frac{\sqrt{\mathrm{e}}}{2} x^{2}-2 x+1+\ln 2
$$

其在 $x>0$ 时的极小值点为

$$
x_{0}=\frac{-1+(24+\sqrt{\mathrm{e}})^{\frac{1}{2}}}{6}
$$

因此可得 $g(x)$ 在 $x>0$ 时的最小值为

$$
g\left(x_{0}\right)>1.1050
$$

这样就得到了 $f(x)$ 的下界 1.1050 .

解法四 在 $x=0$ 处对 $\mathrm{e}^{x}$ 进行二次逼近.

由于 $\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}$, 于是

$$
f(x)>g(x)=x^{2}\left(1+x+\frac{x^{2}}{2}\right)-\ln x
$$

对 $g(x)$ 求导得

$$
g^{\prime}(x)=\frac{2 x^{4}+3 x^{3}+x^{2}-1}{x}=\frac{(x+1)\left(x^{2}+x+1\right)(2 x-1)}{x}
$$

于是 $g(x)$ 的极小值点为 $x_{0}=\frac{1}{2}$, 因此可得 $g(x)$ 的极小值为

$$
g\left(\frac{1}{2}\right)=\frac{13}{32}+\ln 2>1.0994
$$

这样就得到了 $f(x)$ 的下界 1.0994.

## 第 972 题 估算范围

已知 $f(x)=\frac{a}{x}+\frac{x}{a}-\left(a-\frac{1}{a}\right) \ln x$, 求证: 存在一个长度大于 1 的闭区间 $D$ (闭区间 $[m, n]$ 的长度为 $n-m)$, 使得当 $a \in D$ 时, $f(x)$ 没有零点.

解析 将函数 $f(x)$ 改成写

$$
f(x)=\frac{1}{a}\left[x+\frac{a^{2}}{x}-\left(a^{2}-1\right) \ln x\right]
$$

由于 $a$ 的取值范围必然关于原点对称, 且 $a \neq 0$, 于是只需要考虑 $a>0$ 的情形.

## 估算法一

情形一 当 $0<a \leqslant 1$ 时, 此时

$$
\ln x \geqslant 1-\frac{1}{x}
$$

于是

$$
x+\frac{a^{2}}{x}-\left(a^{2}-1\right) \ln x \geqslant x+\frac{a^{2}}{x}+\left(1-a^{2}\right)\left(1-\frac{1}{x}\right)=x+\left(1-a^{2}\right)+\frac{2 a^{2}-1}{x},
$$

于是当 $\frac{\sqrt{2}}{2} \leqslant a \leqslant 1$ 时符合题意.

情形二 当 $a>1$ 时,考虑到

$$
x+\frac{a^{2}}{x}>x
$$

于是取函数 $y=\left(a^{2}-1\right) \ln x$ 在 $x=\mathrm{e}$ 处的切线, 则有

$$
\left(a^{2}-1\right) \ln x \leqslant \frac{a^{2}-1}{\mathrm{e}} \cdot x
$$

于是当 $1<a \leqslant \sqrt{\mathrm{e}+1}$ 时符合题意.

综上所述, 当 $a \in\left[\frac{\sqrt{2}}{2}, \sqrt{\mathrm{e}+1}\right]$ 时均符合题意,而此区间长度大于 1 , 于是原命题得证.

## 估算法二

函数 $f(x)$ 的导函数

$$
f^{\prime}(x)=\frac{(x+1)\left(x-a^{2}\right)}{a x^{2}}
$$

于是当 $x=a^{2}$ 时, 函数 $f(x)$ 取得极小值, 亦为最小值

$$
f\left(a^{2}\right)=\frac{1}{a}\left[a^{2}+1-\left(a^{2}-1\right) \cdot \ln a^{2}\right]
$$

设

$$
g(x)=x+1-(x-1) \cdot \ln x
$$

则 $g(x)$ 的导函数

$$
g^{\prime}(x)=\frac{1}{x}-\ln x
$$

因为 $g^{\prime}(x)$ 单调递减, 且

$$
g^{\prime}(1)>0, g^{\prime}(2)<0,
$$

所以 $g(x)$ 有唯一的零点 $m \in(1,2)$, 从而函数 $g(x)$ 在 $(0, m)$ 上单调递增, 在 $(m,+\infty)$ 上单调递减.由于

$$
g\left(\frac{1}{4}\right)=\frac{5-6 \ln 2}{4}>0
$$

且

$$
g(4)=5-6 \ln 2>0
$$

而区间 $\left[\frac{1}{2}, 2\right]$ 的长度大于 1 , 于是原命题得证.

精细的估计

由于

$$
\ln x>\frac{1}{2}\left(x-\frac{1}{x}\right), 0<x<1
$$

于是在估算法二中可以绕开对 $\ln 2$ 的估算, 将 $a$ 的可能取值区间的下界推进到方程

$$
x+1-(x-1) \cdot \frac{1}{2}\left(x-\frac{1}{x}\right)=0
$$

的较小根的算术平均数 $\sqrt{2-\sqrt{3}} \approx 0.5176$.

如果采用更好的估计 $\sqrt{x}-\frac{1}{\sqrt{x}}$, 那么就需要解一个四次方程, 把结果推进到

$$
\left[\frac{\sqrt{5+\sqrt{17}-\sqrt{26+10 \sqrt{17}}}}{2}, \frac{\sqrt{5+\sqrt{17}+\sqrt{26+10 \sqrt{17}}}}{2}\right]
$$

约为 $[0.4805,2.0810]$.

## 第 973 题 求和估计

已知 $S=\frac{\pi}{20000} \cdot\left(\sin \frac{\pi}{20000}+\sin \frac{2 \pi}{20000}+\sin \frac{3 \pi}{20000}+\cdots+\sin \frac{10000 \pi}{20000}\right)$, 推测下列各值中与 $S$ 最接近的是
A. 0.9988
B. 0.9999
C. 1.0001
D. 2.0002
解析 $\mathrm{C}$.

观察 $S$ 的形式, 我们将区间 $\left[0, \frac{\pi}{2}\right]$ 进行 10000 等分, 将得到的横坐标对应的函数 $f(x)=\sin x$ 图象上的点记为

$$
A_{k}, k=0,1,2, \cdots, 10000
$$

即 $A_{k}\left(\frac{k \pi}{20000}, \sin \frac{k \pi}{20000}\right)$, 过这些点作 $x$ 轴的平行线, 得到如图 1 的小矩形 (示意图,将区间 8 等分):

于是 $S$ 为这些小矩形的面积之和, 所以

$$
S>\int_{0}^{\frac{\pi}{2}} \sin x \mathrm{~d} x=1
$$

其次, 我们来估计多出的面积有多少, 这需要用到正弦函数图象特点 (即凹凸性) , 依次连结 $A_{k} A_{k+1}$, 得到很多小的直角三角形, 多出来的面积比这些小直角三角形的面积之和小,如图 2.

这些小的直角三角形有一条相等的边,故面积之和为

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-384.jpg?height=300&width=395&top_left_y=259&top_left_x=1412)

图 1

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-384.jpg?height=300&width=398&top_left_y=619&top_left_x=1410)

图 2

$$
\frac{1}{2} \times \frac{\pi}{20000} \times 1<10^{-4}
$$

综上, $1<S<1.0001, \mathrm{C}$ 正确.

## 第十二章 其他好题

## 第 974 题 数学归纳法

将 1 到 $n$ 这 $n$ 个正整数按下面的方法排成一个排列, 要求: 除左边的第一个数外, 每个数都与它左边 (未必相邻) 的某个数相差 1 , 将此种排列称为 “ $n$ 排列”. 比如 “ 2 排列” 为当 $n=2$ 时, 有 1,$2 ; 2,1$, 共有 2 种排列. “ 3 排列” 为当 $n=3$ 时, 有 $1,2,3 ; 2,1,3 ; 2,3,1 ; 3,2,1$, 共有 4 种排列.

(1) 请写出 “ 4 排列”的排列数;

(2) 问所有 “ $n$ 排列” 的结尾数只能是什么数? 请加以证明;

(3) 证明: “ $n$ 排列”共有 $2^{n-1}$ 个.

解析 (1) $1,2,3,4 ; 2,1,3,4 ; 2,3,1,4 ; 2,3,4,1 ; 3,2,1,4 ; 3,2,4,1 ; 3,4,2,1 ; 4,3,2,1$; 共有 8 个.

(2) “ $n$ 排列” 的结尾数只能是 1 和 $n$. 首先证明以下引理:

引理 任何“ $n+1$ 排列”中去掉数 $n+1$ 后的 $n$ 个数一定组成“ $n$ 排列”.

若“ $n+1$ 排列” 中 $n+1$ 排在 $n$ 的右边, 那么去掉这个数对其他所有数都没有影响, 因此组成“ $n$ 排列”;

若“ $n+1$ 排列” 中 $n+1$ 排在 $n$ 的左边, 那么 $n+1$ 只可能排在左边第一位, 此时去掉这个数对其他所有数都没有影响, 因此组成“ $n$ 排列”.

根据引理, 任何一个“ $n+1$ 排列” 都必然由某个 “ $n$ 排列”通过在适当的位置添加 $n+1$ 得到. 接下来用数学归纳法证明命题.

归纳基础显然成立.

假设任何“ $n$ 排列”的结尾是 1 或 $n$, 那么对于“ $n+1$ ”排列, 只有两种可能:

(1) 当“ $n$ 排列”以 $n$ 结尾时, 直接在结尾添加 $n+1$, 此时符合题意;

(2)当“ $n$ 排列”以 1 结尾时, 或者直接在结尾添加 $n+1$, 或者将 $n+1$ 添加在非结尾的位置, 此时 “ $n+1$ 排列”以 1 结尾, 符合题意.

因此命题得证.

(3) 用数学归纳法证明.

归纳基础显然成立.

假设“ $n$ 排列”共有 $2^{n-1}$ 个, 那么考虑“ $n+1$ 排列”可以通过两种方法得到:

(1) 直接在 “ $n$ 排列” 结尾添加 $n+1$, 因此以 $n+1$ 结尾的“ $n+1$ 排列” 有 $2^{n-1}$ 个;

(2) “ $n$ 排列” 的每个数都增加 1 , 然后在结尾添加 1 , 因此以 $n+1$ 结尾的 “ $n+1$ 排列” 有 $2^{n-1}$ 个.

因此命题得证.

## 第 975 题 算两次

某次测试成绩满分为 150 分, 设 $n$ 名学生的得分分别为 $a_{1}, a_{2}, \cdots, a_{n}\left(a_{i} \in \mathbf{N}, 1 \leqslant i \leqslant n\right), b_{k}(1 \leqslant k \leqslant$ 150) 为 $n$ 名学生中得分至少为 $k$ 分的人数. 设 $M$ 为 $n$ 名学生的平均成绩, 记 $N=\frac{b_{1}+b_{2}+\cdots+b_{150}}{n}$, 则 $M$ 与 $N$ 的大小关系为

解析 $M=N$.

我们需要搞清楚 $N$ 的含义, 将 $b_{k}$ 进行拆分, 记这 $n$ 名学生中得分为 $i$ 分的人数为 $c_{i}$, 则 $0 \leqslant i \leqslant 150$, 且

$$
c_{0}+c_{1}+c_{2}+\cdots+c_{150}=n
$$

由题意知

$$
b_{k}=c_{k}+c_{k+1}+\cdots+c_{150}
$$

于是

$$
\begin{aligned}
& b_{1}+b_{2}+\cdots+b_{150} \\
= & \left(c_{1}+c_{2}+\cdots+c_{150}\right)+\left(c_{2}+c_{3}+\cdots+c_{150}\right)+\cdots+c_{150} \\
= & c_{1}+2 c_{2}+3 c_{3}+\cdots+150 c_{150}
\end{aligned}
$$

这 $n$ 名同学的得分总和可以用两种方法计算得到,一种是将每名同学的得分直接相加, 即

$$
a_{1}+a_{2}+\cdots+a_{n}=n M
$$

另一种方法是先将得分按分数分类, 然后每个分数乘以得到这个分数的人数, 即

$$
0 \cdot c_{0}+1 \cdot c_{1}+2 \cdot c_{2}+\cdots+150 c_{150}=b_{1}+b_{2}+\cdots+b_{150}
$$

从而有

$$
n M=b_{1}+b_{2}+\cdots+b_{150}
$$

所以 $M=N$.

## 思考与总结

将一个量用两种不同的方法分别计算一次,由结果相同得到一个等式,这被称为“算两次”的思想, 在解决某些问题时非常有效.

## 第 976 题 数与形的完美融合

将一堆小球 (数量不小于 2) 分为两堆, 记录两堆所包含的小球数之积, 将这种操作称为 “分堆”, 将得到的积称为“分堆积”. 将 $n$ 个小球进行一次“分堆”, 对应的“分堆积”设为 $p_{1}$; 从得到的两堆小球中选出一堆进行“分堆”, 对应的“分堆积”设为 $p_{2}$; 再从得到的三堆小球中选出一堆进行“分堆”, 对应的“分堆积”设为 $p_{3}$; 依次进行下去, 直到最后得到 $n$ 堆小球 (每堆的小球数量均为 1 ) 为止. 设

$$
S(n)=p_{1}+p_{2}+\cdots+p_{n-1}
$$

证明: $S(n)$ 是一个与分堆的具体过程无关的定值.

## 解析 解法一

每次都分出只包含一个小球的堆, 那么有 $p_{k}=n-k$, 其中 $k=1,2, \cdots, n-1$. 于是

$$
\sum_{k=1}^{n-1} p_{k}=(n-1)+(n-2)+\cdots+1=\frac{1}{2} n(n-1)
$$

接下来用数学归纳法证明无论采用何种分法, 均有 $S(n)=\frac{1}{2} n(n-1)$, 其中 $n=2,3, \cdots$.

当 $n=2$ 时, 显然有 $S(2)=1$, 命题成立;

假设命题对 $n \leqslant k(k \geqslant 2, k \in \mathbf{N})$ 都成立, 则当 $n=k+1$ 时, 记 $S(1)=0$, 假设经过第 1 次分堆后两堆的小球数分别为 $p, n-p$, 则

$$
\begin{aligned}
S(n) & =p(n-p)+S(p)+S(n-p) \\
& =p(n-p)+\frac{1}{2} p(p-1)+\frac{1}{2}(n-p)(n-p-1) \\
& =\frac{1}{2}\left(2 p n-2 p^{2}+p^{2}-p+n^{2}-2 p n-n+p+p^{2}\right) \\
& =\frac{1}{2} n(n-1)
\end{aligned}
$$

因此命题也成立.

综上所述, 无论采用何种分法, 均有 $S(n)=\frac{1}{2} n(n-1)$, 其中 $n=2,3, \cdots$.

解法二 设 $T_{n}=\left\{A_{1}, A_{2}, \cdots, A_{n}\right\}$ 为 $n$ 元集合, 将第一次分堆视为对集合 $T_{n}$ 作分划, 设分划的结果为 $B_{s}, B_{t}$, 其中 $t+s=n$, 则满足 $x \in B_{s}$ 且 $y \in B_{t}$ 的二元集合 $\{x, y\}$ 的数目即为 $p_{1}$.

类似地持续进行分划, 直到所有集合均为单元素集为止, 则所有的二元集合 $\{x, y\}$ 的数目即为 $S(n)$, 且这些二元集合的数目恰好为集合 $T_{n}$ 的二元子集的个数, 因此

$$
S(n)=\mathrm{C}_{n}^{2}=\frac{1}{2} n(n-1)
$$

这个方法也有一个优美的几何解释:

如图 1, 分步将 $n$ 阶 (图中以 $n=10$ 为例) 完全图中的线逐步擦除即得.

解法三 设第一次分堆将 $n$ 个小球分成 $a_{1}$ 和 $a_{2}$ 两个部分, 那么

$$
n^{2}=\left(a_{1}+a_{2}\right)^{2}=a_{1}^{2}+a_{2}^{2}+2 a_{1} a_{2}
$$

可以将这个等式看作 $n^{2}$ “分裂” 为 $a_{1}^{2}$ 和 $a_{2}^{2}$, 与此同时产生 “余项” $2 a_{1} a_{2}$, 也即 $2 p_{1}$. 随着“分裂” 的持续进行直至最终的 $n$ 个 $1^{2}$, 所产生的“余项”之和为

$$
2 p_{1}+2 p_{2}+\cdots+2 p_{n-1}=2 S(n)
$$

因此我们有

$$
n^{2}=\underbrace{1^{2}+1^{2}+\cdots+1^{2}}_{n}+2 S(n),
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-387.jpg?height=423&width=461&top_left_y=1214&top_left_x=1397)

图 1

即

$$
S(n)=\frac{1}{2} n(n-1)
$$

这个方法有一个优美的几何解释:

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-387.jpg?height=521&width=524&top_left_y=1902&top_left_x=740)

图 2

如图 2, 所有矩形的面积之和即 $S(n)$.

## 第 977 题 构造与论证

将一个正整数 $n$ 表示为 $a_{1}+a_{2}+\cdots+a_{p}\left(p \in \mathbf{N}^{*}\right)$ 的形式, 其中 $a_{i} \in \mathbf{N}^{*}, i=1,2, \cdots, p$, 且 $a_{1} \leqslant a_{2} \leqslant$ $\cdots \leqslant a_{p}$, 记所有这样的表示法的种数为 $f(n)$, 如 $4=4,4=1+3,4=2+2,4=1+1+2,4=1+1+1+1$,故 $f(4)=5$.

(1) 写出 $f(3), f(5)$ 的值, 并说明理由;

(2) 对任意正整数 $n$, 比较 $f(n+1)$ 与 $\frac{1}{2}[f(n)+f(n+2)]$ 的大小, 并给出证明;

(3) 当正整数 $n \geqslant 6$ 时,求证: $f(n) \geqslant 4 n-13$.

解析 解法一 (1)因为

$$
3=3,3=1+2,3=1+1+1,
$$

所以 $f(3)=3$;

因为

$$
\begin{aligned}
& 5=5,5=1+4,5=2+3,5=1+1+3 \\
& 5=1+2+2,5=1+1+1+2,5=1+1+1+1+1
\end{aligned}
$$

所以 $f(5)=7$.

(2) 因为

$$
f(1)=1, f(2)=2, f(3)=3, f(4)=5, f(5)=7, f(6)=11, f(7)=15, \cdots,
$$

猜想

$$
f(n+1) \leqslant \frac{1}{2}[f(n)+f(n+2)]
$$

所以只需要证明

$$
f(n+2)-f(n+1) \geqslant f(n+1)-f(n)
$$

证明如下:

注意到在 $n$ 的所有表示法前加上 “ $1+$ ” 就可以得到 $(n+1)$ 的表示法中以 1 为第一项的表示法, 因此 $(n+$ 1) 的表示法中以 1 为第一项的有 $f(n)$ 种, 因此不以 1 为第一项的有 $f(n+1)-f(n)$ 种;

类似的, $(n+2)$ 的表示法中不以 1 为第一项的有 $f(n+2)-f(n+1)$ 种.

在 $(n+1)$ 的表示法中所有不以 1 为第一项的表示法中的最后一项加上 1 就可以得到 $(n+2)$ 的表示法中不以 1 为第一项的表示法,且这些表示法均不相同,所以

$$
f(n+2)-f(n+1) \geqslant f(n+1)-f(n)
$$

综上, 命题得证.

(3) 根据 (2) ,

$$
f(n+2)-f(n+1) \geqslant f(n+1)-f(n)
$$

而 $f(6)=11, f(7)=15$, 所以

$$
f(7)-f(6)=4, f(8)-f(7) \geqslant 4, f(9)-f(8) \geqslant 4, \cdots, f(n)-f(n-1) \geqslant 4
$$

其中 $k \in \mathbf{N}^{*}$, 累加有

$$
f(n)-f(6) \geqslant 4(n-6),
$$

即

$$
f(n) \geqslant 4 n-13
$$

解法二 $(1)$ 见解法一

(2) 见解法一

(3) 由于当 $n=6$ 时, $f(6)=11$, 命题成立;

因此只需要证明当 $n \geqslant 6$ 时,

$$
f(n+1)-f(n) \geqslant 4
$$

即可.

在 $(n+1)$ 的表示法中,以 1 为第一项的有 $f(n)$ 个;

考虑 $(n+1)$ 的表示法中不以 1 为第一项的, 至少有三类:

情形一 1 个数的,

$$
(n+1)=(n+1),
$$

共 1 个;

情形ニ 2 个数的,

$$
\begin{aligned}
& (n+1)=2+(n-1),(n+1)=3+(n-2), \cdots \\
& (n+1)=\left[\frac{n+1}{2}\right]+(n+1)-\left[\frac{n+1}{2}\right]
\end{aligned}
$$

至少有 2 个;

情形三 3 个数的,

$$
(n+1)=\left[\frac{n+1}{3}\right]+\left[\frac{n+1}{3}\right]+(n+1)-2\left[\frac{n+1}{3}\right], \cdots
$$

至少有 1 个.

从而

$$
f(n+1)-f(n) \geqslant 4
$$

累加得

$$
f(n) \geqslant 4 n-13
$$

## 第 978 题 幸运大转盘

已知两个半径不等的圆盘叠放在一起 (有一轴穿过它们的圆心), 两圆盘上分别有互相垂直的两条直径将其分为四个区域, 小圆盘上所写的实数分别记为 $x_{1}, x_{2}, x_{3}, x_{4}$, 大圆盘上所写的实数分别记为 $y_{1}, y_{2}, y_{3}, y_{4}$, 如图 1 所示. 将小圆盘逆时针旋转 $i(i=1,2,3,4)$ 次, 每次转动 $90^{\circ}$, 记 $T_{i}(i=1,2,3,4)$ 为转动 $i$ 次后各区域内两数乘积之和, 例如 $T_{1}=x_{1} y_{2}+x_{2} y_{3}+x_{3} y_{4}+x_{4} y_{1}$. 若

$$
x_{1}+x_{2}+x_{3}+x_{4}<0, y_{1}+y_{2}+y_{3}+y_{4}<0
$$

则以下结论正确的是
A. $T_{1}, T_{2}, T_{3}, T_{4}$ 中至少有一个为正数
B. $T_{1}, T_{2}, T_{3}, T_{4}$ 中至少有一个为负数
C. $T_{1}, T_{2}, T_{3}, T_{4}$ 中至多有一个为正数
D. $T_{1}, T_{2}, T_{3}, T_{4}$ 中至多有一个为负数

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-389.jpg?height=368&width=473&top_left_y=1810&top_left_x=1353)

图 1

## 解析 A.

因为

$$
T_{1}+T_{2}+T_{3}+T_{4}=\left(x_{1}+x_{2}+x_{3}+x_{4}\right)\left(y_{1}+y_{2}+y_{3}+y_{4}\right)>0
$$

所以 $T_{1}, T_{2}, T_{3}, T_{4}$ 中至少有一个为正数. 下面分别给出 $T_{1}, T_{2}, T_{3}, T_{4}$ 中有 $1,2,3,4$ 个正数的例子.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-390.jpg?height=344&width=349&top_left_y=194&top_left_x=197)

1 个正数

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-390.jpg?height=344&width=336&top_left_y=194&top_left_x=586)

2 个正数

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-390.jpg?height=344&width=334&top_left_y=194&top_left_x=961)

3 个正数

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-390.jpg?height=346&width=336&top_left_y=193&top_left_x=1345)

4 个正数

图 2

## 第 979 题 分数 $P K$

中国古代儒家要求学习掌握六种基本才艺:礼、乐、射、御、书、数,简称“六艺”.某中学为弘扬“六艺” 的传统文化, 分别进行了主题为“礼、乐、射、御、书、数” 的六场传统文化知识竟赛. 现有甲、乙、丙三位选手进入了前三名的最后角逐. 规定: 每场知识竞赛前三名的得分都分别为 $a, b, c$, 其中 $a>b>c$ 且 $a, b, c \in \mathbf{N}^{*}$; 选手最后得分为各场得分之和. 在六场比赛后, 已知甲最后得分为 26 分, 乙和丙最后得分都为 11 分, 且乙在其中一场比赛中获得第一名, 则下列说法正确的是
A. $a=4$
B. 甲可能有一场比赛获得第二名
C. 乙有四场比赛获得第三名
D. 丙可能有一场比赛获得第一名

解析 $\mathrm{C}$.

根据甲的得分可知 $a \geqslant 5$, 而

$$
a+b+c=\frac{26+11+11}{6}=8
$$

故

$$
a=5, b=2, c=1 \text {. }
$$

因此甲六场比赛的得分(不计次序) 为

$$
5,5,5,5,5,1,
$$

乙六场比赛的得分 (不计次序) 为

$$
5,2,1,1,1,1 \text {, }
$$

丙六场比赛的得分 (不计次序) 为

$$
2,2,2,2,2,1
$$

## 第 980 题 砝码称重

给定正整数 $n$, 已知用克数都是正整数的 $k$ 块砝码和一台天平, 可以称出质量为 $1,2,3, \cdots, n$ 克的所有物品. 求 $k$ 的最小值 $f(n)$.

解析 设这 $k$ 块砝码的质量数分别为 $a_{1}, a_{2}, \cdots, a_{k}$, 且

$$
1 \leqslant a_{1} \leqslant a_{2} \leqslant \cdots \leqslant a_{k}, a_{i} \in \mathbf{Z}, i=1,2, \cdots, k
$$

因为天平两端都可以放砝码, 故可称质量为

$$
\sum_{i=1}^{k} x_{i} a_{i}
$$

其中 $x_{i} \in\{-1,0,1\}, i=1,2, \cdots, k$.

若利用这 $k$ 块砝码可以称出质量为 $1,2,3, \cdots, n$ 的物品, 则上述表达式中含有 $1,2,3, \cdots, n$, 由对称性易知也含有 $0,-1,-2, \cdots,-n$, 即

$$
\{0, \pm 1, \pm 2, \cdots, \pm n\} \subseteq\left\{\sum_{i=1}^{k} x_{i} a_{i} \mid x_{i} \in\{-1,0,1\}, i=1,2, \cdots, k\right\}
$$

所以

$$
\left.2 n+1 \leqslant|\{0, \pm 1, \pm 2, \cdots, \pm n\}| \leqslant\left\{\sum_{i=1}^{k} x_{i} a_{i} \mid x_{i} \in\{-1,0,1\}, i=1,2, \cdots, k\right\}\right\} \leqslant 3^{k}
$$

即

$$
n \leqslant \frac{3^{k}-1}{2} .
$$

设

$$
\frac{3^{m-1}-1}{2}<n \leqslant \frac{3^{m}-1}{2}
$$

其中 $m \in \mathbf{N}^{*}$, 则 $k \geqslant m$.

当 $k=m$ 时, 取

$$
a_{1}=1, a_{2}=3, \cdots, a_{m}=3^{m-1},
$$

由三进制数的表示可知, 对任意 $p \in\left\{0,1,2, \cdots, 3^{m}-1\right\}$,都有

$$
p=\sum_{i=1}^{m} y_{i} 3^{i-1}
$$

其中 $y_{i} \in\{0,1,2\}$, 因此

$$
p-\frac{3^{m-1}-1}{2}=\sum_{i=1}^{m} y_{i} 3^{i-1}-\sum_{i=1}^{m} 3^{i-1}=\sum_{i=1}^{m}\left(y_{i}-1\right) 3^{i-1}
$$

令 $x_{i}=y_{i}-1$, 则 $x_{i} \in\{-1,0,1\}, i=1,2, \cdots, m$.

故对任意整数 $l \in\left[-\frac{3^{m}-1}{2}, \frac{3^{m}-1}{2}\right]$, 都有

$$
l=\sum_{i=1}^{m} x_{i} 3^{i-1}
$$

其中 $x_{i} \in\{-1,0,1\}, i=1,2, \cdots, m$.

由于 $n \leqslant \frac{3^{m}-1}{2}$, 因此, 对一切正整数 $l \in[-n, n]$,也有上述表示.

综上所述, $k$ 的最小值 $f(n)=m$, 其中 $\frac{3^{m-1}-1}{2}<n \leqslant \frac{3^{m}-1}{2}, m \in \mathbf{N}^{*}$.

可以进一步证明, 当且仅当 $n=\frac{3^{m}-1}{2}, m \in \mathbf{N}^{*}$ 时, 上述 $f(n)$ 块砝码的组成方式是唯一确定的.

## 第 981 题 新定义关系

据统计某超市两种蔬菜 $A, B$ 连续 $n$ 天的价格分别为 $a_{1}, a_{2}, \cdots, a_{n}$ 和 $b_{1}, b_{2}, \cdots, b_{n}$, 令

$$
M=\left\{m \mid a_{m}<b_{m}, m=1,2, \cdots, n\right\},
$$

若 $M$ 中元素个数大于 $\frac{3}{4} n$, 则称蔬菜 $A$ 在这 $n$ 天的价格低于蔬菜 $B$ 的价格, 记作 $A \leftarrow B$. 现有三种蔬菜 $A, B, C$, 下列说法正确的是

A. 若 $A \leftarrow B, B \leftarrow C$, 则 $A \leftarrow C$

B. 若 $A \leftarrow B, B \leftarrow C$ 同时不成立, 则 $A \leftarrow C$ 不成立
C. $A \leftarrow B, B \leftarrow A$ 可同时不成立
D. $A \leftarrow B, B \leftarrow A$ 可同时成立

## 解析 C.

设 $n=8$.

对于选项 $A$, 取

$$
\begin{aligned}
& \left(a_{1}, a_{2}, \cdots, a_{n}\right)=(5,5,5,5,5,5,5,5) \\
& \left(b_{1}, b_{2}, \cdots, b_{n}\right)=(6,6,6,6,6,6,6,3) \\
& \left(c_{1}, c_{2}, \cdots, c_{n}\right)=(7,7,7,7,7,7,4,4)
\end{aligned}
$$

可知 $\mathrm{A}$ 选项错误.

对于选项 $B$, 取

$$
\begin{aligned}
& \left(a_{1}, a_{2}, \cdots, a_{n}\right)=(5,5,5,5,5,5,5,5) \\
& \left(b_{1}, b_{2}, \cdots, b_{n}\right)=(4,4,4,4,7,7,7,7) \\
& \left(c_{1}, c_{2}, \cdots, c_{n}\right)=(6,6,6,6,6,6,6,6)
\end{aligned}
$$

可知 $\mathrm{B}$ 选项错误.

对于选项 C, 取

$$
\begin{aligned}
& \left(a_{1}, a_{2}, \cdots, a_{n}\right)=(5,5,5,5,5,5,5,5), \\
& \left(b_{1}, b_{2}, \cdots, b_{n}\right)=(4,4,4,4,7,7,7,7),
\end{aligned}
$$

可知 $\mathrm{C}$ 选项正确.

对于选项 D, 显然错误.

## 第 982 题翻杯子

对于 $n$ 维向量 $A=\left(a_{1}, a_{2}, \cdots, a_{n}\right)$, 若对任意 $i \in\{1,2, \cdots, n\}$ 均有 $a_{i}=0$ 或 $a_{i}=1$, 则称 $A$ 为 $n$ 维 $T$向量. 对于两个 $n$ 维 $T$ 向量 $A, B$, 定义 $d(A, B)=\sum_{i=1}^{n}\left|a_{i}-b_{i}\right|$.

(1) 若 $A=(1,0,1,0,1), B=(0,1,1,1,0)$, 求 $d(A, B)$ 的值;

(2) 现有一个 5 维 $T$ 向量序列: $A_{1}, A_{2}, A_{3}, \cdots$, 若 $A_{1}=(1,1,1,1,1)$, 且对任意正整数 $i$, 均有 $d\left(A_{i}\right.$, $\left.A_{i+1}\right)=2$, 求证: 该序列中不存在 5 维 $T$ 向量序列 $(0,0,0,0,0)$;

(3) 现有一个 12 维 $T$ 向量序列: $A_{1}, A_{2}, A_{3}, \cdots$, 若 $A_{1}=(\underbrace{1,1, \cdots, 1}_{12 \uparrow}), A_{j}=(\underbrace{0,0, \cdots, 0}_{12 \uparrow}), j \rightarrow \mathbf{N}^{*}$, 且存在正整数 $m$, 使得对任意正整数 $i$, 均有 $d\left(A_{i}, A_{i+1}\right)=m$, 求出所有可能的 $m$.
解析 $(1) 4$

(2) 用反证法, 若存在符合题意的序列且 $A_{k+1}=(0,0,0,0,0), k \in \mathbf{N}^{*}$. 设向量 $A_{1}$ 的每个分量变化的次数分别为

$$
2 k_{1}+1,2 k_{2}+1,2 k_{3}+1,2 k_{4}+1,2 k_{5}+1
$$

其中 $k_{1}, k_{2}, k_{3}, k_{4}, k_{5} \in \mathbf{N}$. 这样就有

$$
2 k=\left(2 k_{1}+1\right)+\left(2 k_{2}+1\right)+\left(2 k_{3}+1\right)+\left(2 k_{4}+1\right)+\left(2 k_{5}+1\right),
$$

左边为偶数, 右边为奇数, 矛盾. 因此原命题得证.

(3) 引理 1 对 $n$ 维 $T$ 向量序列, $m$ 取 $n$ 的正约数时符合题意.

引理 2 对 $n$ 维 $T$ 向量序列, 当 $n$ 为偶数时, $m=n-1$ 符合题意; 当 $n$ 为奇数时, $m=n-2$ 符合题意.

引理 3 对 $n$ 维 $T$ 向量序列, 当 $n$ 为偶数时, $m=2$ 符合题意, 进一步当 $m \leqslant n-2$ 也符合题意.

引理 1 对 $n$ 维 $T$ 向量序列, 当 $n$ 为奇数时, 那么 $m$ 必然为奇数.

引理 2 的证明 当 $n$ 为偶数时, 第 $i$ 次操作除 $i$ 分量外的其他所有分量,经过 $n$ 次操作后, 每个分量被操作了 $n-1$ 次, 恰好都发生改变;

当 $n$ 是奇数时, 第 $i$ 次操作除 $i, i+1$ 分量外的其他所有分量 (其中第 $n$ 次操作除第 $n$, 第 1 分量外的所有分量), 经过 $n$ 次操作后, 每个分量被操作了 $n-2$ 次, 恰好都发生改变.

引理 3 的证明 两次操作除了想要变换的两个分量之外都操作相同的分量 (即每次操作一个想变换的分量加上 $m-1$ 个相同分量), 这样两次操作就相当于一次 $m=2$ 的操作.

根据以上引理, 显然所有可能的 $m=1,2,3,4,5,6,7,8,9,10,11,12$.

## 第 983 题 左右不逢源

在 $1,2,3,4,5,6,7,8,9,10,11,12,13$ 共 13 个数中挑出 $k$ 个数, 使得这 $k$ 个数中任意两个的差都不是 5 和 8 , 则 $k$ 的最大值是

解析 6 .

如图. 将 13 个数排成一圈, 其中任何相邻的数都不能同时取.

从 1 开始按逆时针顺序把数染成实心和空心,

则所有空心圈对应的数符合题意, 共 6 个.

若 $k$ 超过 6 个,则必然会出现两个数相邻,

因此 $k$ 的最大值为 6 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-393.jpg?height=355&width=345&top_left_y=1609&top_left_x=1521)

## 第 984 题 模长的最大值

已知复数 $z$ 满足 $|z|=1$, 则 $\left|z^{3}+3 z+2 i\right|$ 的最大值是

解析 $3 \sqrt{3}$.

解法一 由于 $\left|z^{3}+3 z+2 \mathrm{i}\right|=\left|(z \mathrm{i})^{3}-3(z \mathrm{i})+2\right|$, 因此问题等价于已知 $|z|=1$, 求 $\left|z^{3}-3 z+2\right|$ 的最大值. 利用共轭复数, 有

$$
\begin{aligned}
\left|z^{3}-3 z+2\right|^{2} & =\left(z^{3}-3 z+2\right) \cdot\left(z^{3}-3 z+2\right) \\
& =14+2\left(z^{3}+z^{3}\right)-3\left(z^{2}+z^{2}\right)-6(z+z) \\
& =14+2(z+z) \cdot\left[(z+z)^{2}-3 z \cdot z\right]-3\left[(z+z)^{2}-2 z \cdot z\right]-6(z+z) \\
& =2 x^{3}-3 x^{2}-12 x+20,
\end{aligned}
$$

其中 $x=z+z=2 \operatorname{Re}(z)$, 且 $x \in[-2,2]$, 设 $f(x)=2 x^{3}-3 x^{2}-12 x+20$, 则

$$
f^{\prime}(x)=6(x+1)(x-2),
$$

于是当 $x=-1$ 时, $f(x)$ 取得最大值为 27 . 因此原式的最大值为 $3 \sqrt{3}$, 当 $z=-\frac{1}{2} \pm \frac{\sqrt{3}}{2} \mathrm{i}$ 时取得.

思考与总结

共地复数是处理有关复数的模的问题的一大利器.

解法二 由于 $\left|z^{3}+3 z+2 \mathrm{i}\right|=\left|(z \mathrm{i})^{3}-3(z \mathrm{i})+2\right|$, 因此问题等价于已知 $|z|=1$, 求 $\left|z^{3}-3 z+2\right|$ 的最大值. 根据题意, 有

$$
\begin{aligned}
\left|z^{3}-3 z+2\right| & =|z+2| \cdot|z-1|^{2} \\
& =\sqrt{(5+4 \cdot \operatorname{Re}(z)) \cdot(2-2 \cdot \operatorname{Re}(z)) \cdot(2-2 \cdot \operatorname{Re}(z))} \\
& \leqslant \sqrt{27}=3 \sqrt{3}
\end{aligned}
$$

等号当 $\operatorname{Re}(z)=-\frac{1}{2}$ 时取得. 因此所求的最大值为 $3 \sqrt{3}$.

对于模为 1 的复数 $z=\cos \theta+\mathrm{i} \cdot \sin \theta$ 与实数 $a$, 有

$$
|z+a|=\sqrt{(a+\cos \theta)^{2}+(\sin \theta)^{2}}=\sqrt{\left(a^{2}+1\right)+2 a \cdot \operatorname{Re}(z)}
$$

特别的, 当 $a=1$ 时,有

$$
|z+1|=2\left|\cos \frac{\theta}{2}\right|,
$$

当 $a=-1$ 时,有

$$
|z-1|=2\left|\sin \frac{\theta}{2}\right|
$$

## 第 985 题 复数模长的最值

已知复数 $z_{1}, z_{2}$ 满足 $\left|z_{1}+z_{2}\right|=20,\left|z_{1}^{2}+z_{2}^{2}\right|=16$, 则 $\left|z_{1}^{3}+z_{2}^{3}\right|$ 的最小值是

解析 3520 .

根据题意, 有

$$
\begin{aligned}
\left|z_{1}^{3}+z_{2}^{3}\right| & =\left|\left(z_{1}+z_{2}\right)\left(z_{1}^{2}-z_{1} z_{2}+z_{2}^{2}\right)\right| \\
& =\left|\left(z_{1}+z_{2}\right) \cdot \frac{3\left(z_{1}^{2}+z_{2}^{2}\right)-\left(z_{1}+z_{2}\right)^{2}}{2}\right| \\
& \geqslant\left|z_{1}+z_{2}\right| \cdot \frac{\left|z_{1}+z_{2}\right|^{2}-3\left|z_{1}^{2}+z_{2}^{2}\right|}{2} \\
& =3520,
\end{aligned}
$$

等号当 $\left(z_{1}+z_{2}\right)^{2}$ 与 $z_{1}^{2}+z_{2}^{2}$ 同向时取到. 因此所求的最小值为 3520 .

等号取到时, $z_{1} z_{2}$ 与 $z_{1}^{2}+z_{2}^{2}$ 共线, 从而有 $\left(z_{1}+z_{2}\right)^{2}$ 与 $\left(z_{1}-z_{2}\right)^{2}$ 共线, 所以 $z_{1}+z_{2}$ 与 $z_{1}-z_{2}$ 共线或垂直.

如果 $z_{1}+z_{2}$ 与 $z_{1}-z_{2}$ 共线, 那么可以得到 $z_{1}, z_{2}$ 共线, 容易证明此时无解;

如果 $z_{1}+z_{2}$ 与 $z_{1}-z_{2}$ 垂直,那么 $\left|z_{1}\right|=\left|z_{2}\right|$, 从而设

$$
z_{1}=r(\cos \alpha+\mathrm{i} \cdot \sin \alpha), z_{2}=r(\cos \beta+\mathrm{i} \cdot \sin \beta), r>0
$$

代人条件中整理得

$$
\left\{\begin{array}{l}
r \cdot \sqrt{2+2 \cos (\alpha-\beta)}=20 \\
r^{2} \cdot \sqrt{2+2 \cos (2 \alpha-2 \beta)}=16
\end{array}\right.
$$

解得

$$
\left\{\begin{array}{l}
r=8 \sqrt{3} \\
\cos (\alpha-\beta)=\frac{1}{24}
\end{array}\right.
$$

或

$$
\left\{\begin{array}{l}
r=4 \sqrt{13} \\
\cos (\alpha-\beta)=-\frac{1}{26}
\end{array}\right.
$$

验证知, 前者对应 $\left|z_{1}^{3}+z_{2}^{3}\right|$ 的最小值, 后者对应 $\left|z_{1}^{3}+z_{2}^{3}\right|$ 的最大值 4480 .

可以对 $z_{1}, z_{2}$ 进行具体取值, 比如取 $\beta=0$, 得到

$$
z_{1}=8 \sqrt{3}\left(\frac{1}{24} \pm \frac{5 \sqrt{23}}{24} \mathrm{i}\right), z_{2}=8 \sqrt{3}
$$

就是 $\left|z_{1}^{3}+z_{2}^{3}\right|$ 取最小值时的一组解. 同样地

$$
z_{1}=4 \sqrt{13}\left(-\frac{1}{26} \pm \frac{15 \sqrt{3}}{26} \mathrm{i}\right), z_{2}=4 \sqrt{13}
$$

就是 $\left|z_{1}^{3}+z_{2}^{3}\right|$ 取最大值时的一组解.

## 第 986 题 一箭双雕

已知实数列 $\left\{a_{n}\right\},\left\{b_{n}\right\}$ 的各项均不为 0 , 且

$$
\left\{\begin{array}{l}
a_{n}=a_{n-1} \cos \theta-b_{n-1} \sin \theta \\
b_{n}=a_{n-1} \sin \theta+b_{n-1} \cos \theta
\end{array}\right.
$$

$a_{1}=1, b_{1}=\tan \theta$, 其中 $\theta$ 为已知常数, 求数列 $\left\{a_{n}\right\}$ 和 $\left\{b_{n}\right\}$ 的通项公式.

解析 观察已知条件, 联想到复数的运算:

$$
a_{n}+b_{n} \mathrm{i}=\left(a_{n-1}+b_{n-1} \mathrm{i}\right) \cdot(\cos \theta+\mathrm{i} \cdot \sin \theta)
$$

将 $a_{n}$ 和 $b_{n}$ 分别看作复数 $z_{n}$ 的实部和虚部, 即设 $z_{n}=a_{n}+b_{n} \mathrm{i}\left(n \in \mathbf{N}^{*}\right)$, 则已知的两个递推式可以合并为

$$
z_{n}=z_{n-1} \cdot(\cos \theta+\mathrm{i} \cdot \sin \theta), n \geqslant 2, n \in \mathbf{N}^{*}
$$

于是复数数列 $\left\{z_{n}\right\}$ 是以 $z_{1}=1+\mathrm{i} \cdot \tan \theta$ 为首项, $\cos \theta+\mathrm{i} \cdot \sin \theta$ 为公比的等比数列, 易得

$$
\begin{aligned}
z_{n} & =(1+\mathrm{i} \cdot \tan \theta)(\cos \theta+\mathrm{i} \cdot \sin \theta)^{n-1} \\
& =\sec \theta \cdot(\cos \theta+\mathrm{i} \cdot \sin \theta) \cdot(\cos \theta+\mathrm{i} \cdot \sin \theta)^{n-1} \\
& =\sec \theta \cdot(\cos \theta+\mathrm{i} \cdot \sin \theta)^{n} \\
& =\sec \theta \cdot(\cos n \theta+\mathrm{i} \cdot \sin n \theta) \\
& =\sec \theta \cdot \cos n \theta+\mathrm{i} \cdot \sec \theta \cdot \sin n \theta .
\end{aligned}
$$

故有 $a_{n}=\sec \theta \cdot \cos n \theta, b_{n}=\sec \theta \cdot \sin n \theta$, 其中 $n \in \mathbf{N}^{*}$.

## 思考与总结

本题的顺利解决依赖于熟练掌握复数的乘法运算法则, 而复数的乘法法则

$$
(a+b \mathrm{i}) \cdot(c+d \mathrm{i})=(a c-b d)+(a d+b c) \mathrm{i}
$$

中还蕴含着一个重要的恒等式

$$
\left(a^{2}+b^{2}\right) \cdot\left(c^{2}+d^{2}\right)=(a c-b d)^{2}+(a d+b c)^{2},
$$

这个恒等式是在代数变形中常用的, 同时也是哈密顿发现四元数的重要铺路石.

## 第 987 题 复数方程

设 $a \geqslant 0$,在复数集 $\mathbf{C}$ 中解方程: $z^{2}+2|z|=a$.

解析 设 $z=r(\cos \theta+i \sin \theta)(r \geqslant 0, \theta \in[0,2 \pi))$, 则

$$
r^{2}(\cos 2 \theta+\mathrm{i} \cdot \sin 2 \theta)+2 r=a,
$$

于是

$$
\left\{\begin{array}{l}
r^{2} \cos 2 \theta+2 r=a \\
r^{2} \sin 2 \theta=0
\end{array}\right.
$$

情形一 $r=0$.

此时 $z=0$, 对应 $a=0$.

情形二 $\theta=0, \pi$.

此时 $r^{2}+2 r=a$, 解得 $r=\sqrt{a+1}-1$.

情形三 $\theta=\frac{\pi}{2}, \frac{3 \pi}{2}$.

此时 $-r^{2}+2 r=a$, 解得 $r=1 \pm \sqrt{1-a}(0 \leqslant a \leqslant 1)$.

综上所述, 原方程的解为

$$
\begin{cases}0, \pm 2 \mathrm{i}, & a=0 \\ \pm(\sqrt{a+1}-1),(1 \pm \sqrt{1-a}) \mathrm{i},-(1 \pm \sqrt{1-a}) \mathrm{i}, & 0<a<1 \\ \pm(\sqrt{2}-1), \pm \mathrm{i} & a=1 \\ \pm(\sqrt{a+1}-1) . & a>1\end{cases}
$$

本题也可以由 $z^{2}=a-2|z| \in \mathbf{R}$ 得到 $z$ 为实数或纯虚数, 从而求解. 需要注意的是 $a$ 的范围不同时, 解的个数不同,所以需要分类.

## 第 988 题 花落知多少

已知 $2^{2013}<5^{867}<2^{2014}, m, n$ 均为整数, 且 $1 \leqslant m \leqslant 2012$. 求满足

$$
5^{n}<2^{m}<2^{m+2}<5^{n+1}
$$

的有序整数对 $(m, n)$ 共有多少对?

解析 易知 $5^{n}$ 与 $5^{n+1}$ 之间只能有 2 个或 3 个 $2^{m}$ 形式的数. 因为 $2^{2013}<5^{867}<2^{2014}$, 所以当 $1 \leqslant m \leqslant 2012$时, 只需考虑以下 867 个区间:

$$
\left(5^{0}, 5^{1}\right),\left(5^{1}, 5^{2}\right), \cdots,\left(5^{866}, 5^{867}\right),
$$

设这些区间中有 2 个 $2^{m}$ 形式的数的区间个数为 $x$, 有 3 个 $2^{m}$ 形式的数的区间个数为 $y$, 则

$$
\left\{\begin{array}{l}
x+y=867 \\
2 x+3 y=2013
\end{array}\right.
$$

解得

$$
\left\{\begin{array}{l}
x=588 \\
y=279
\end{array}\right.
$$

所以满足 $5^{n}<2^{m}<2^{m+2}<5^{n+1}$ 的有序整数对 $(m, n)$ 共有 279 对.

## 第 989 题 数字黑洞-Kaprekar 常数

定义 $\overline{a b c}$ 是一个三位数, 其中各数位上的数字 $a, b, c \in\{0,1,2,3,4,5,6,7,8,9\}$ 且不全相同. 定义如下运算 $f:$ 把 $\overline{a b c}$ 的三个数字 $a, b, c$ 自左到右分别由大到小排列和由小到大排列 (若非零数字不足三位则在前面补 0), 然后用“较大数”减去“较小数”. 例如: $f(100)=100-001=099, f(102)=210-012=198$.如下定义一个三位数序列: 第一次实施运算 $f$ 的结果记为 $\overline{a_{1} b_{1} c_{1}}$, 对于 $n>1$ 且 $n \in \mathbf{N}, \overline{a_{n} b_{n} c_{n}}=$ $f\left(\overline{a_{n-1} b_{n-1} c_{n-1}}\right)$. 将 $\overline{a_{n} b_{n} c_{n}}$ 的三个数字中的最大数字与最小数字的差记为 $d_{n}$.

(1) 当 $\overline{a b c}=636$ 时, 求 $\overline{a_{1} b_{1} c_{1}}, \overline{a_{2} b_{2} c_{2}}$ 及 $d_{2}$ 的值;

(2) 若 $d_{1}=6$, 求证: 当 $n>1$ 时, $\boldsymbol{d}_{n}=5$;

(3)求证:对任意三位数 $\overline{a b c}$, 当 $n \geqslant 6$ 时, $\overline{a_{n} b_{n} c_{n}}=495$.

解析 (1) $\overline{a_{1} b_{1} c_{1}}=297, \overline{a_{2} b_{2} c_{2}}=693, d_{2}=6$;

(2)易知 $f\left(\overline{a_{n} b_{n} c_{n}}\right)=99 d_{n}$.

下面我们用数学归纳法来证明“当 $n>1$ 时, $d_{n}=5$ ”.

当 $n=2$ 时, 因为 $d_{1}=6$, 所以

$$
\overline{a_{2} b_{2} c_{2}}=f\left(\overline{a_{1} b_{1} c_{1}}\right)=594
$$

故 $d_{2}=5$.

所以当 $n=2$ 时, 要证的命题成立.

假设当 $n=k>1$ 时要证的命题成立, 即 $d_{k}=5$. 则当 $n=k+1$ 时,

$$
\overline{a_{k+1} b_{k+1} c_{k+1}}=f\left(\overline{a_{k} b_{k} c_{k}}\right) \doteq 99 d_{k}=495
$$

所以 $d_{k+1}=5$.

故当 $n=k+1$ 时, 要证的命题也成立.

综上所述,命题“当 $n>1$ 时, $d_{n}=5$ ”成立.

（3）易知, $d \in\{1,2,3,4,5,6,7,8,9\}$. 因为

$$
\overline{a_{1} b_{1} c_{1}}=f(\overline{a b c})=99 d=\overline{d 00}-\overline{00 d}
$$

所以 $a_{1}=d-1, b_{1}=9, c_{1}=10-d$, 故

$$
d_{1}= \begin{cases}10-d, & d \leqslant 5 \\ d-1, & d>5\end{cases}
$$

因此 $d_{1} \in\{5,6,7,8,9\}$.

若 $d_{1}=5$, 则 $\overline{a_{2} b_{2} c_{2}}=\overline{a_{3} b_{3} c_{3}}=\cdots=495$;

若 $d_{1}=6$, 则 $d_{2}=5$, 故 $\overline{a_{3} b_{3} c_{3}}=\overline{a_{4} b_{4} c_{4}}=\cdots=495$;

若 $d_{1}=7$, 则 $d_{2}=6, d_{3}=5$, 故 $\overline{a_{4} b_{4} c_{4}}=\overline{a_{5} b_{5} c_{5}}=\cdots=495$;

若 $d_{1}=8$, 则 $d_{2}=7, d_{3}=6, d_{4}=5$, 故 $\overline{a_{5} b_{5} c_{5}}=\overline{a_{6} b_{6} c_{6}}=\cdots=495$;

若 $d_{1}=9$, 则 $d_{2}=8, d_{3}=7, d_{4}=6, d_{5}=5$, 故 $\overline{a_{6} b_{6} c_{6}}=\overline{a_{7} b_{7} c_{7}}=\cdots=495$.

综上所述, 对任意三位数 $\overline{a b c}$, 当 $n \geqslant 6$ 时, 均有 $\overline{a_{n} b_{n} c_{n}}=495$.

这个问题叫做“Kaprekar 问题”,由印度数学家 Kaprekar 在 1949 年提出. 我们还可以证明, 对于各个数位上的数字不全相同的四位数来说, 最多进行 7 次题中所描述的操作,即可得到常数 6174.

## 第 990 题 步步为营

当平面上的点 $(x, y)$ 的坐标 $x, y$ 都为有理数时, 该点称为有理点, 设 $r$ 是给定的正实数,则圆 $(x-$ $1)^{2}+(y-\sqrt{2})^{2}=r^{2}$ 上的有理点
A. 最多有一个
B. 最多有两个
C. 最多有四个
D. 可以有无穷多个

解析 $\mathrm{B}$.

根据题意, 在考虑点的横纵坐标是否为有理数时, 题设是关于直线 $x=1$ 对称的. 这是因为如果 $A(x, y)$是符合题意的圆上的有理点,那么其关于直线 $x=1$ 对称的点 $A^{\prime}(2-x, y)$ 也必然是符合题意的圆上的有理点. 同时题设关于直线 $y=\sqrt{2}$ 不对称, 也就是关于直线 $y=\sqrt{2}$ 对称的两点不可能同时为有理点. 此时问题转化为

问题一 对称轴被圆所截形成的直径端点是否可能为有理点?

问题二 半圆弧 (不包含端点)上是否存在有理点? 如果存在,最多有几个?
问题 1 比较容易解决, 由于题设关于直线 $y=\sqrt{2}$ 不对称, 于是圆上横坐标为 1 的有理点最多只有一个. 对于问题 2 , 我们首先很容易确定存在性 (随意取一个有理点,然后作一个圆心为 $C(1, \sqrt{2})$ 且过该点的圆即可), 因此问题的关键是判断最多可以有几个有理点.

再进一步将问题分解,思考一个弱化的问题, 如果有两个有理点,会不会出现矛盾? 如果没有明显的矛盾,那么是否可以构造合适的例子?

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-399.jpg?height=369&width=341&top_left_y=195&top_left_x=1542)

事实上,如果在半圆弧上存在两个有理点 $A, B$, 那么不难推出下面两个结论:

结论一 弦 $A B$ 的中点 $M$ 也为有理点.

结论二 弦 $A B$ 的斜率存在且为非零有理数.

这两个结论可以通过垂径定理 (有关圆的最重要定理) 结合在一起: 由结论 1 以及圆心 $C$ 的坐标可得弦 $A B$ 的垂径斜率为无理数; 由结论 2 , 弦 $A B$ 的垂径斜率为有理数. 这样就推出了矛盾. 因此在半圆弧上不可能同时出现两个有理点.

接下来将以上结论综合起来:

$r \neq \sqrt{2}$ 时, 显然圆上最多有两个有理点, 且关于 $x=1$ 对称;

$r=\sqrt{2}$ 时, 用之前推导半圆弧上不可能同时出现两个有理点的同样方法可以推得半圆弧上不可能存在有理点, 于是圆上只有一个有理点 $(1,0)$.

综合以上, 我们可以知道选项 B 正确, 并且得到了一个更一般的结论: 圆上的有理点可能是一个, 也可能是两个. 此时不禁要问:圆上是否可能没有任何一个有理点呢?

问题的答案是肯定的, 取 $r=\sqrt{\mathrm{e}}$ 即可, 探索过程留给读者.

其他的思考方向:

方向一 圆上不可能同时存在三个有理点. 因为如果同时存在三个有理点,那么连结任何两个有理点的线段的垂直平分线方程必然为有理系数方程, 而两个二元一次有理系数方程的解一定为有理数对, 这与圆心的坐标不是有理数对矛盾.

方向二 假设圆上的有理点 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$, 那么有

$$
\left(x_{1}-1\right)^{2}+\left(y_{1}-\sqrt{2}\right)^{2}=\left(x_{2}-1\right)^{2}+\left(y_{2}-\sqrt{2}\right)^{2}
$$

整理得

$$
\left(x_{1}^{2}-2 x_{1}-x_{2}^{2}+2 x_{2}+y_{1}^{2}-y_{2}^{2}\right)-2 \sqrt{2}\left(y_{1}-y_{2}\right)=0 .
$$

由于 $x_{1}, y_{1}, x_{2}, y_{2}$ 均为有理数,于是

$$
\left\{\begin{array}{l}
x_{1}^{2}-2 x_{1}-x_{2}^{2}+2 x_{2}+y_{1}^{2}-y_{2}^{2}=0 \\
y_{1}-y_{2}=0
\end{array}\right.
$$

即

$$
x_{1}+x_{2}=2, y_{1}=y_{2} .
$$

这样我们就得到了圆上的任意两个有理点 (如果有两个或两个以上的有理点)的横坐标之和为 2 且纵坐标相同. 进而推知, 当 $x_{1}=1$ 时,圆上有唯一有理点 $\left(1, y_{1}\right)$, 其中 $y_{1} \in \mathbf{Q}$; 当 $x_{1} \neq 1, x_{1} \in \mathbf{Q}$ 且 $y_{1} \in \mathbf{Q}$ 时, 圆上有且只有两个有理点.

## 第 991 题 构造与论证

设 $a, d$ 是正整数,求证: 等差数列 $\{a+n d\}(n \in \mathbf{N})$ 中有无穷多项, 它们有相同的质因数.

## 解析 解法一

注意到

$$
a(1+d)^{n}=a+d \cdot a\left(\mathrm{C}_{n}^{1}+\mathrm{C}_{n}^{2} d+\cdots+\mathrm{C}_{n}^{n} d^{n-1}\right)
$$

因此当 $n=1,2, \cdots$ 时, $a(1+d)^{n}$ 均为题中等差数列的项. 这些项有相同的约数 $1+d$, 取 $1+d$ 的质约数即为满足题意的质因数, 命题得证.

解法二 因为任何两个公差为正整数的等差数列中如果有两项对应相同,那么就有无数项对应相同 （这是因为若

$$
a_{i}=b_{m}, a_{j}=b_{n}, i<j, m<n
$$

则 $a_{2 j-i}=b_{2 n-m}$,一直类推下去, 可以找到无穷多项), 因此只需要证明等差数列中有两项不互质.

情形一 当 $a \geqslant 2$ 时,有 $(a, a+d \cdot a)=a$ 满足条件;

情形二 当 $a=1$ 时,有 $(1+d, 1+d(2+d))=1+d$ 满足条件;

因此命题得证.

思考与总结

如果一个等差数列中有两项不互质, 将这两项分别作为第一、二项 (较小的作为首项) 得到一个新的数列, 这个数列中所有项均不互质, 且这个数列与原数列有无穷多项对应相同, 从而证明了命题.

## 第 992 题 降次与消元

求证:

(1) 方程 $x^{3}-x-1=0$ 恰有一个实根 $\omega$, 并且 $\omega$ 是无理数;

(2) $\omega$ 不是任何整数系数二次方程 $a x^{2}+b x+c=0(a, b, c \in \mathbf{Z}, a \neq 0)$ 的根.

解析 (1) 设函数 $f(x)=x^{3}-x-1$, 则

$$
f^{\prime}(x)=3 x^{2}-1
$$

当 $x \geqslant 1$ 时, $f^{\prime}(x) \geqslant 0$, 于是函数 $f(x)$ 单调递增, 注意到 $f(1)<0, f(2)=5$, 因此函数 $f(x)$ 在 $[1,+\infty)$上有一个实根, 且此根在区间 $(1,2)$ 上.

当 $x \leqslant-1$ 或 $0 \leqslant x<1$ 时, 有

$$
x^{3}-x-1=x\left(x^{2}-1\right)-1 \leqslant-1<0
$$

方程无实根.

当 $-1<x<0$ 时, 有

$$
x^{3}-x-1<-(x+1)<0
$$

方程无实根.
于是方程 $x^{3}-x-1=0$ 恰有一个实根.

下面用反证法证明该实根为无理数.

若实根 $\omega=\frac{q}{p}$, 其中 $p, q$ 为互质的正整数, 则

$$
q^{3}=p^{2}(p+q),
$$

于是 $p^{2} \mid q^{3}$, 可得 $p=1$, 这样就与 $\omega$ 在区间 $(1,2)$ 上矛盾.

因此 $\omega$ 为无理数.

(2)用反证法. 若不然,则有

$$
a \omega^{2}+b \omega+c=0
$$

于是

$$
\omega^{2}=-\frac{b}{a} \omega-\frac{c}{a}
$$

利用此式对

$$
\omega^{3}-\omega-1=0
$$

连续降次, 有

$$
-\frac{b}{a}\left(-\frac{b}{a} \omega-\frac{c}{a}\right)-\frac{c}{a} \omega-\omega-1=0,
$$

整理得

$$
\left(a^{2}+a c-b^{2}\right) \omega+\left(a^{2}-b c\right)=0
$$

从而

$$
\left\{\begin{array}{l}
a^{2}+a c-b^{2}=0 \\
a^{2}-b c=0
\end{array}\right.
$$

从中消元 $b$, 得

$$
a^{2}+a c-\left(\frac{a^{2}}{c}\right)^{2}=0
$$

即

$$
\left(\frac{a}{c}\right)^{3}-\frac{a}{c}-1=0
$$

由第(1)小题可知, 矛盾.

因此原命题得证.

## 第 993 题 构造与论证

非负有理数列 $A_{1}, A_{2}, A_{3}, \cdots$ 满足 $\forall m, n \in \mathbf{N}^{*}, A_{m}+A_{n}=A_{n n}$, 证明: 该数列中必然存在相同的数.

解析 用反证法. 若不然, 则令 $m=n=1$, 根据已知有

$$
A_{1}+A_{1}=A_{1}
$$

于是

$$
A_{1}=0,
$$

因此数列中其余各项均不为 0 .

令 $A_{2}=\frac{p}{q}, A_{3}=\frac{r}{s}$, 则由题中条件可知

$$
A_{m^{k}}=k A_{m},
$$

于是

但是 $2^{r} \neq 3^{t x}$, 矛盾.

$$
A_{2^{\mp}}=q r \cdot \frac{p}{q}=p r=p s \cdot \frac{r}{s}=A_{3^{\star}},
$$

因此原命题得证.

## 第 994 题 $\quad$ 代数与几何结合解决整点问题

在平面直角坐标系中, 如果 $x$ 和 $y$ 都是整数, 就称点 $(x, y)$ 是整点, 下列命题中正确的是 $\qquad$ . (写出所有正确命题的编号)

(1) 存在这样的直线, 既不与坐标轴平行又不经过任何整点;

(2)如果 $k$ 与 $b$ 都是无理数,则直线 $y=k x+b$ 不经过任何整点;

(3)直线 $l$ 经过无穷多个整点,当且仅当 $l$ 经过两个不同的整点;

(4)“直线 $y=k x+b$ 经过无穷多个整点”的充分必要条件是“ $k$ 与 $b$ 都是有理数”;

(5)存在恰经过一个整点的直线.

## 解析 (1)(3)(5).

这道题是整点问题,画出平面直角坐标系中的整点, 从几何与代数两方面去考虑这几个结论的正确性.对于不成立的结论, 只要举出反例即可, 对于成立的结论则需要给出证明.

考虑(1),画出原点附近的整点,如图 1 的直线既不与坐标轴平行, 又不经过任何整点, 比如直线 $y=x+\frac{1}{2}$, 这样的直线有无穷多条, (1)成立;

考虑(2), $k$ 为斜率, $b$ 为纵截距, 在 $y$ 轴上任取一个纵坐标为无理数的点, 考虑这个点与任何一个整点 (不在 $y$ 轴上) 的连线, 则该直线的斜率一定为无理数, 但这条直线上有且仅有一个整点. 例如过 $(0, \sqrt{2})$ 与 $(1,0)$ 两点的直线

$$
y=\sqrt{2}(1-x),
$$

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-402.jpg?height=341&width=330&top_left_y=1379&top_left_x=1461)

图 1

故(2)不正确, (5)正确, 对于(5)也可以考虑过任意一个整点, 且斜率为无理数的直线, 这条直线上一定没有其他整点, 否则两个整点的连线对应的斜率必为有理数, 故(5)正确;

考虑(3), 如图 2 , 当直线 $l$ 经过两个不同的整点 $A, B$ 时, 点 $A$ 关于点 $B$的对称点, 以及点 $B$ 关于点 $A$ 的对称点一定都是整点, 且在直线 $l$ 上, 类似这样的对称可以一直进行下去, 所以 $l$ 一定经过无穷多个整点. 反之显然,故(3)成立.

考虑(4), 当 $y=k x+b$ 经过无穷多个整点时, 由斜率公式知 $k$ 为有理数,从而 $b=y-k x$ 为有理数; 反之, $k, b$ 都是有理数时, 可以不经过任何整点,如(1)中的例子 $y=x+\frac{1}{2}$, 故(4)错误.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-402.jpg?height=350&width=513&top_left_y=1895&top_left_x=1279)

图 2

综上, 正确的命题为(1)(3)(5).
事实上, 对于直线 $y=k x+b$ 上的整点个数, 我们可以得到下面的结论:

| $k$ | $b$ | 整点个数 |
| :---: | :---: | :---: |
| 有理数 | 有理数 | 0 个或无穷多个 |
| 有理数 | 无理数 | 0 个 |
| 无理数 | 有理数 | 0 个或1个 |
| 无理数 | 无理数 | 0 个或1个 |

## 第 995 题 忽明忽暗

有编号为 $1,2,3, \cdots, 100$ 的 100 蓋灯和编号为 $1,2,3, \cdots, 100$ 的 100 个操作员. 100 㙉灯初始时都是关闭的, 100 个操作员顺次操作, 其中编号为 $k$ 的操作员把所有编号为 $k$ 的倍数的灯改变状态, 如编号为 3 的操作员把编号为 $3,6,9, \cdots, 99$ 的灯中关闭的灯打开, 打开的灯关闭. 那么最后亮着的灯有多少㙉?

解析 10 .

显然编号为 $k$ 的灯会被编号为 $k$ 的约数的操作员操作, 因此 $k$ 有奇数个约数时, 编号为 $k$ 的灯最后是亮着的. 而考虑到将一个数 $x$ 的约数按乘积为 $x$ 的方式配对, 可得 $x$ 共有奇数个约数当且仅当 $x$ 为完全平方数. 综上所述, 最后亮着的灯有 10 盏, 其编号分别为 $1,4,9,16,25,36,49,64,81,100$.

## 第 996 题 约数有多少

已知 $n \in \mathbf{N}^{*}$, 且 $1000 n$ 恰好有 1000 个约数, 则 $n$ 的约数个数的最小值为

解析 100 .

设 $n=p_{1}^{x_{1}} \cdot p_{2}^{x_{2}^{2}} \cdots p_{k_{k}}^{z_{k}}$, 其中 $p_{i}(i=1,2, \cdots, k)$ 都是互不相等质数, 且 $x_{i}(i=1,2, \cdots, k)$ 都是正整数, 于是

$$
1000 n=2^{3} \cdot 5^{3} \cdot p_{1}^{x_{1}} \cdot p_{2^{2}}^{x_{2}} \cdots p_{k_{k}}^{x_{k}}
$$

情形一 2 和 5 均不是 $n$ 的约数.

此时 $1000 n$ 的约数个数是

$$
(3+1)(3+1)\left(x_{1}+1\right)\left(x_{2}+1\right) \cdots\left(x_{k}+1\right)=1000,
$$

这不可能.

情形二 2 和 5 中的一个是 $n$ 的约数 (不妨设对应的 $p_{i}$ 为 $p_{1}$ ).

此时 $1000 n$ 的约数个数是

$$
(3+1)\left(x_{1}+3+1\right)\left(x_{2}+1\right) \cdots\left(x_{k}+1\right)=1000
$$

于是

$$
\left(x_{1}+4\right)\left(x_{2}+1\right) \cdots\left(x_{k}+1\right)=250
$$

此时 $n$ 的约数个数为

$$
\left(x_{1}+1\right)\left(x_{2}+1\right) \cdots\left(x_{k}+1\right)=\left(x_{1}+1\right) \cdot \frac{250}{x_{1}+4}=250-\frac{750}{x_{1}+4} \geqslant 100
$$

等号当 $x_{1}=1$ 时取得.

情形三 2 和 5 均为 $n$ 的约数 (不妨设对应的 $p_{i}$ 为 $p_{1}, p_{2}$ ).

此时 $1000 n$ 的约数个数是

$$
\left(x_{1}+3+1\right)\left(x_{2}+3+1\right) \cdots\left(x_{k}+1\right)=1000
$$

于是

$$
\left(x_{1}+4\right)\left(x_{2}+4\right) \cdots\left(x_{k}+1\right)=1000
$$

此时 $n$ 个约数个数为

$$
\begin{aligned}
\left(x_{1}+1\right)\left(x_{2}+1\right) \cdots\left(x_{k}+1\right) & =\left(x_{1}+1\right)\left(x_{2}+1\right) \cdot \frac{1000}{\left(x_{1}+4\right)\left(x_{2}+4\right)} \\
& =40\left(5-\frac{15}{x_{1}+4}\right)\left(5-\frac{15}{x_{2}+4}\right) \\
& \geqslant 160,
\end{aligned}
$$

等号当 $x_{1}=x_{2}=1$ 时取得.

综上所述, $n$ 的约数个数的最小值为 100 .

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-404.jpg?height=76&width=509&top_left_y=1132&top_left_x=709)

各项均为正整数的数列 $\left\{a_{n}\right\}$, 满足 $a_{n+1}=a_{n}+b_{n}$, 其中 $b_{n}$ 是 $a_{n}$ 的末位数字, 下列关于数列 $\left\{a_{n}\right\}$ 的说法中正确的是

A. 如果 $a_{1}$ 是 5 的倍数,那么数列 $\left\{a_{n}\right\}$ 与数列 $\left\{2^{n}\right\}$ 必有相同的项

B. 如果 $a_{1}$ 不是 5 的倍数,那么数列 $\left\{a_{n}\right\}$ 与数列 $\left\{2^{n}\right\}$ 必没有相同的项

C. 如果 $a_{1}$ 不是 5 的倍数, 那么数列 $\left\{a_{n}\right\}$ 与数列 $\left\{2^{n}\right\}$ 只有有限个相同的项

D. 如果 $a_{1}$ 不是 5 的倍数, 那么数列 $\left\{a_{n}\right\}$ 与数列 $\left\{2^{n}\right\}$ 有无穷多个相同的项

## 解析 $D$.

对选项 $\mathrm{A}:$ 如果 $a_{1}$ 是 5 的倍数,那么 $\left\{b_{n}\right\}$ 为 $0,0,0, \cdots$ 或 $5,0,0, \cdots$.

因为 2 的方幂不可能以 5 或 0 结尾, 因此 $\left\{a_{n}\right\}$ 中的任何一项都不在数列 $\left\{2^{n}\right\}$ 中.

对选项 B,C,D: 如果 $a_{1}$ 不是 5 的倍数, 那么 $\left\{b_{n}\right\}$ 从第二项起必然进入 $2,4,8,6,2,4,8,6, \cdots$ 的循环 (进入时的数字和 $b_{1}$ 有关), 必然存在 $a_{m}=4 k$, 其中 $k \in \mathbf{N}^{*}$.

此时取与 $2 k$ 尾数相同的 2 的方幂, 设为 $2^{p}$, 则有

$$
2^{p}=10 q+2 k
$$

其中 $p, q \in \mathbf{N}^{*}$, 这样就有 $a_{m}=4 k=2^{p+1}-20 q$,

也就是说 $a_{m}$ 经过 $q$ 轮 $+2+4+8+6$ 后必然得到 $2^{p+1}$.

由于符合要求的 $p$ 有无穷多个, 因此数列 $\left\{a_{n}\right\}$ 与数列 $\left\{2^{n}\right\}$ 有无穷多个相同的项.
本题的解题思路是: 循环一次 $(+2+4+8+6)$ 后, 数列中的数增加 20 .

如果每次增加的是 10 , 那么只要找个位数相同的 2 的较大的方幂即可.

现在考虑将所有的数除以 2 再寻找个位数相同的 2 的方幂, 对原来的数先做一个筛选, 即选择 4 的倍数, 这样除以 2 之后尾数仍然为 $2,4,6,8$ 中的某个, 问题解决.

## 第 998 题 二进制

已知数列 $\left\{a_{n}\right\}$ 的项数为 $n, a_{1}=a, a_{n}=1$ 且满足

$$
a_{i+1}= \begin{cases}\frac{a_{i}}{2}, & 2 \mid a_{i} \\ a_{i}-1, & 2 \nmid a_{i}\end{cases}
$$

其中 $i=1,2, \cdots, n-1$. 设 $M(a)$ 表示 $a_{1}$ 的取值集合, $\operatorname{card}(M(a))$ 表示 $M(a)$ 的元素个数.

(1) 若 $n=4$, 求 $\operatorname{card}(M(a))$;

(2) 求证: $n \leqslant a_{1} \leqslant 2^{n-1}$;

(3) 若 $a_{1} \leqslant 2015$, 求 $n$ 的最大值, 并直接写出 $n$ 取最大值时的 $\operatorname{card}(M(a))$.

解析 (1) 从 $a_{4}=1$ 开始往前倒推:

$a_{3}$ 的所有可能取值为 2 ;

$a_{2}$ 的所有可能取值为 3,$4 ;$

$a_{1}$ 的所有可能取值为 $6,5,8$.

于是 $\operatorname{card}(M(a))=3$.

(2) 从第 (1) 小题的倒推过程可以看出 $a_{n-1}=2$, 且如果 $p \leqslant a_{k} \leqslant q$, 其中 $2 \leqslant k \leqslant n-1$ 且 $k \in \mathbf{N}$, 那么

$$
p+1 \leqslant a_{k-1} \leqslant 2 q,
$$

这样倒推到首项, 就有

$$
n \leqslant a_{1} \leqslant 2^{n-1}
$$

(3) 如果说解决第 (2)小题时我们只需要对递推过程进行上下界分析而无需具体分析变化过程的细节的话, 第 (3) 小题就是要求我们理解递推过程的本质. 事实上,与十进制下的数除以 10 得到的结果 (如果能整除的话) 相当于抹去最后面的 “ 0 ”一样 (比如, $\frac{2310}{10}=231$ ), 除以 2 就相当于二进制下的偶数抹去最后面的 “ 0 ”, 比如 $(18)_{10}=(10010)_{2}$, 而 $\frac{18}{2}=9=(1001)_{2}$. 发掘出这样的直观解释后, 就可以得到项数 $n$ 与首项 $a$ 的关系了. 由于减去 1 相当于将“尾巴上”的 1 改为 0 ,除以 2 相当于将“尾巴上”的 0 抹去, 因此 $n$ 的值就是将首项 $a$ 改写为二进制数后的数位数与为 1 的数位数之和再减去 1 , 如当 $a=23$ 时, 数列 $\left\{a_{n}\right\}$ 为

$$
23,22,11,10,5,4,2,1
$$

共 8 项, 此时 $(23)_{10}=(10111)_{2}$, 共 5 位, 其中有 4 个数位为 1 .

回到第 (3) 小题中的特殊问题, 我们知道

$$
(2015)_{10}=(11111011111)_{2},
$$

当 $a \leqslant 2015$ 时, 数位数与为 1 的数位数之和至多为 21 , 因此 $n$ 的最大值为 20 . 而可以使得项数为 20 的
首项 $a$ 只可能是

$(11111011111)_{2},(11110111111)_{2},(11101111111)_{2},(11011111111)_{2},(10111111111)_{2}$,共 5 个, 于是 $\operatorname{card}(M(a))=5$.

## 第 999 题 连分数

若分数 ${ }_{q}^{p}$ ( $p, q$ 为正整数) 化成小数为 $0.198 \cdots$, 则当 $q$ 取最小值时, $p+q=$

解析 121.

解法一 注意到

$$
0.198=\frac{99}{500}=\frac{1}{5+\frac{1}{19+\frac{1}{1+\frac{1}{4}}}}
$$

于是取

$$
\frac{1}{5+\frac{1}{19+1}}=\frac{20}{101}
$$

可得满足条件的分数, 于是 $p+q=121$.

解法二 由 $\frac{p}{q}=0.198 \cdots<\frac{1}{5}$, 知

$$
q>5 p
$$

记 $q=5 p+m(m$ 为正整数 $)$, 于是

$$
\frac{p}{5 p+m}=0.198 \cdots,
$$

即

$$
0.198(5 p+m)<p<0.199(5 p+m)
$$

所以

$$
19.8 m<p<39.8 m
$$

当 $m=1$ 时, $20 \leqslant p \leqslant 39$, 取 $p=20$, 则 $q$ 最小为 101 , 而

$$
\frac{20}{101}=0.19801980 \cdots,
$$

符合要求.

故当 $q$ 最小时, $p+q=121$.

## 第 1000 题 费马小定理

求证: 存在无穷多个奇数 $m$, 使得 $8^{m}+9 m^{2}$ 为合数.

解析 由费马小定理, 有

$$
8^{16} \equiv 1(\bmod 17),
$$

于是当 $m \equiv 1(\bmod 16)$ 时,有

$$
8^{m} \equiv 8(\bmod 17)
$$

又当 $m \equiv 1(\bmod 17)$ 时, 有

$$
9 m^{2} \equiv 9(\bmod 17)
$$

因此当 $m \equiv 1(\bmod 16 \times 17)$ 时, $17 \mid 8^{m}+9 m^{2}$, 因此 $8^{m}+9 m^{2}$ 为合数.

而满足 $m \equiv 1(\bmod 16 \times 17)$ 的奇数有无穷多个,因此原命题得证.

## 第 1001 题 反客为主

已知 $x-4 \sqrt{y}=2 \sqrt{x-y}$, 则 $x$ 的取值范围是

解析 $\{0\} \cup[4,20]$.

显然 $x=0$ 时符合题意;

当 $x>0$ 时, 考虑到向量 $(\sqrt{x-y}, \sqrt{y})$ 的模为定值 $\sqrt{x}$, 因此以原点为起点, 向量 $(\sqrt{x-y}, \sqrt{y})$ 的终点是以原点为圆心, $\sqrt{x}$ 为半径的圆在第一象限的部分 (再加上弧的两个端点).

不难得到数量积

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-407.jpg?height=314&width=309&top_left_y=1005&top_left_x=1548)

$$
(2,4) \cdot(\sqrt{x-y}, \sqrt{y})
$$

的取值范围是

$$
(2,4) \cdot(\sqrt{x}, 0) \leqslant(2,4) \cdot(\sqrt{x-y}, \sqrt{y}) \leqslant \sqrt{x} \cdot \sqrt{20},
$$

这样就建立了不等式

$$
2 \sqrt{x} \leqslant x \leqslant \sqrt{20 x}
$$

解得 $4 \leqslant x \leqslant 20$.

综上所述, $x$ 的取值范围是 $\{0\} \cup[4,20]$.

其他解法 也可以通过不等式去求范围:

因为 $x=4 \sqrt{y}+2 \sqrt{x-y}$, 而

$$
4 \sqrt{y}+2 \sqrt{x-y} \leqslant \sqrt{4^{2}+2^{2}} \cdot \sqrt{y+x-}=\bar{y}=\sqrt{20 x}
$$

所以有 $x \leqslant 20$, 当且仅当 $4 x=5 y=80$ 时取等号.

又因为 $x \geqslant 0$, 对 $x=4 \sqrt{y}+2 \sqrt{x-y}$ 两边平方得

$$
x^{2}=4[x+3 y+4 \sqrt{y(x-y)}] \geqslant 4 x
$$

当且仅当 $y=0$ 时取等号, 从而有 $x=0$ 或 $x \geqslant 4$. 这些通过不等式求范围的过程本质上正是上面通过向量体现的几何意义.

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-408.jpg?height=260&width=836&top_left_y=1&top_left_x=193)

提供各种书籍的 PDF 电子版代找服务, 如果您找不到您想要的书的 PDF 电子版, 我们可以帮您找到, 如有需要, 请联系微信、QQ。
![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-408.jpg?height=922&width=388&top_left_y=504&top_left_x=841)

## PDF 代找说明:

本公司可以帮助您找到您想要的 PDF 电子书。质量都很清晰, 只要您提供给我们相关信息，一般都能找到，如果您有需求，请联系我们。

现已经帮助了很多人找到了大家需要的 PDF, 其实网上有很多 PDF, 大家如果在网上找不到的话, 可以联系我们, 大部分我们都可以找到。因PDF电子书都有版权, 请不要随意传播, 如果您有经济购买能力, 请尽量购买正版。

![](https://cdn.mathpix.com/cropped/2024_05_08_edae359ceea84e5dd2c6g-408.jpg?height=114&width=188&top_left_y=2196&top_left_x=177)

本公司只提供代找服务, 因寻找 PDF 电子书有一定难度，仅收取代找费用。如因 PDF 产生的版权纠纷, 与本公司无关, 我们仅仅只是帮助您寻找到您要的 PDF 而已。


[^0]:    解析 (2)(4).

