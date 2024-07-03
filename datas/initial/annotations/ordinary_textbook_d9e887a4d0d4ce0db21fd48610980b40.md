数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 一个整点相关的椭圆面积最大值问题 

徐俊楠<br>(学而思网校, 北京, 102208)

在 $\mathbb{R}^{n}$ 中关于原点对称且不含原点以外的格点的凸集, 闵可夫斯基定理给出了其体积的上界 $2^{n} d(L)$, 其中 $d(L)$ 是格 $L$ 的行列式. 特别的, 对于整点格 $\mathbb{Z}^{n}$,体积上界为 $2^{n}$, 并且有简洁的初等证明。

定理 1 设 $S \subset \mathbb{R}^{n}$ 是一个关于原点对称且不含原点以外的整点的凸集, 则

$$
V(S) \leq 2^{n}
$$

证明 考察映射

$$
f: S \rightarrow \mathbb{R}^{n} /(2 \mathbb{Z})^{n},(x, y) \mapsto(x \bmod 2, y \bmod 2)
$$

则 $f$ 是单射. 若不然, 则存在 $\left(x_{1}, y_{1}\right) \neq\left(x_{2}, y_{2}\right)$, 使得 $f\left(x_{1}, y_{1}\right)=f\left(x_{2}, y_{2}\right)$.

由于 $S$ 关于原点对称， $\left(-x_{1},-y_{1}\right) \in S$. 由于 $S$ 是凸集，

$$
\frac{1}{2}\left(-x_{1},-y_{1}\right)+\frac{1}{2}\left(x_{2}, y_{2}\right)=\left(\frac{x_{2}-x_{1}}{2}, \frac{y_{2}-y_{1}}{2}\right) \in S
$$

根据 $f$ 的定义, $\left(\frac{x_{2}-x_{1}}{2}, \frac{y_{2}-y_{1}}{2}\right)$ 是一个整点, 矛盾. 而 $f$ 是局部保面积的, 故

$$
V(S) \leq V(f(S)) \leq 2^{n}
$$

如果对凸集有更多的限制, 是否会有更强的结论, 笔者提出如下问题:

问题 1 设 $E \subset \mathbb{R}^{2}$ 是一个以原点为中心且内部不含原点以外的整点的椭圆, 求其面积的最大值.

半平面内的三个点可以确定一个关于原点对称的二次曲线. 猜想当 $E$ 过 $(1,0),(0,1),(1,1)$ 时取到最大值, 记为 $\hat{E}$. 计算可得 $S_{\hat{E}}=\frac{2 \pi}{\sqrt{3}} \approx 3.6276$. (图 1)[^0]

![](https://cdn.mathpix.com/cropped/2024_02_26_98b546c7d609df3f9275g-2.jpg?height=688&width=782&top_left_y=190&top_left_x=640)

图 1. 过 $(1,0),(0,1),(1,1)$ 的椭圆

进一步在几何画板中探索发现, 当 $E$ 过 $(1,0),(k, 1),(k+1,1), k \in \mathbb{N}$ 时, 面积为定值, 且不含整点; 当 $k$ 取非整数值时, 面积方面的结论仍成立 (图 2 中第二个椭圆).

![](https://cdn.mathpix.com/cropped/2024_02_26_98b546c7d609df3f9275g-2.jpg?height=451&width=1148&top_left_y=1228&top_left_x=457)

图 2. 一些面积为 $\frac{2 \pi}{\sqrt{3}}$ 的椭圆

上述性质的表述提示我们考察椭圆在 $y=1$ 上的截距, 从这一角度入手验证性质并不困难：

引理 1 设 $E$ 是以原点为中心的椭圆, 方程为 $a x^{2}+b x y+c y^{2}=1, a, b, c \in \mathbb{R}$,则椭圆面积为 $S_{E}=\frac{2 \pi}{\sqrt{4 a c-b^{2}}}$.

证明 通过坐标变换将方程化为 $A x^{2}+C y^{2}=1, A, C \in \mathbb{R}_{+}$, 则 $b^{2}-4 a c=$ $-4 A C$. 而椭圆的半长轴与半短轴分别为 $\sqrt{\frac{1}{A}}, \sqrt{\frac{1}{C}}$, 故 $E$ 的面积为

$$
S_{E}=\frac{\pi}{\sqrt{A C}}=\frac{2 \pi}{\sqrt{4 a c-b^{2}}} .
$$

由引理 1 可以得到以下性质:

性质 1 设 $E$ 是以原点为中心的椭圆, 若其过 $\left(\frac{1}{t}, 0\right)$ 而与直线 $y=1$ 的两交
点距离为 $d$, 则椭圆面积 $S_{E}=\frac{2 \pi}{\sqrt{4 t^{2}-t^{4} d^{2}}}$.

证明 $E$ 过 $\left(\frac{1}{t}, 0\right)$, 故 $a=t^{2} . d$ 为方程 $a x^{2}+b x+c-1=0$ 的两根之差,即 $d=\frac{\sqrt{b^{2}-4 a c+4 a}}{a}$. 故 $4 a c-b^{2}=4 a-a^{2} d^{2}=4 t^{2}-t^{4} d^{2}$, 由引理 1 ,

$$
S_{E}=\frac{2 \pi}{\sqrt{4 a c-b^{2}}}=\frac{2 \pi}{\sqrt{4 t^{2}-t^{4} d^{2}}} .
$$

特别的, 当 $t=1, d=1$ 时, $S_{E}=\frac{2 \pi}{\sqrt{3}}$. 并且有

推论 1 设 $E$ 是问题 1 中的椭圆. 若 $E$ 过 $(1,0)$, 则 $E$ 的面积 $S_{E} \leq \frac{2 \pi}{\sqrt{3}}$.

证明 由性质 $1, S_{E}=\frac{2 \pi}{\sqrt{4-d^{2}}}$. 而 $E$ 内部没有原点以外的整点, 故 $d \leq 1$, 从而 $S_{E} \leq \frac{2 \pi}{\sqrt{3}}$.

然而用这一思路来给出一般情形的面积上界会遇到麻烦, 注意到

$$
S_{E}=\frac{2 \pi}{\sqrt{4 t^{2}-t^{4} d^{2}}}=\frac{2 \pi}{\sqrt{\frac{4}{d^{2}}-\left(t^{2} d-\frac{2}{d}\right)^{2}}}
$$

而 $d \in(0,1], t \in[1, \infty)$. 极值在 $t=\frac{\sqrt{2}}{d}$ 时取到, 与目标不符. 另一方面,过 $(1,1),(1,2),(2,3)$ 的椭圆面积仍为 $\frac{2 \pi}{\sqrt{3}}$ (图 3), 说明极大面积椭圆不一定要过 $(1,0)$ 或 $(0,1)$, 且在 $y=1$ 上的截距 $d \leq 1$ 也不一定要取等号.

![](https://cdn.mathpix.com/cropped/2024_02_26_98b546c7d609df3f9275g-3.jpg?height=834&width=596&top_left_y=1476&top_left_x=730)

图 3. 过 $(1,1),(1,2),(2,3)$ 的椭圆

笔者转而将性质 1 理解为一种“平移”面积不变性, 其本质为保面积的仿射变换:

$$
\left(\begin{array}{l}
x \\
y
\end{array}\right) \mapsto\left(\begin{array}{cc}
1 & -t \\
0 & 1
\end{array}\right)\left(\begin{array}{l}
x \\
y
\end{array}\right)=\left(\begin{array}{c}
x-t y \\
y
\end{array}\right)
$$

对称地有坚直方向的“平移”变换:

$$
\left(\begin{array}{l}
x \\
y
\end{array}\right) \mapsto\left(\begin{array}{cc}
1 & 0 \\
-t & 1
\end{array}\right)\left(\begin{array}{l}
x \\
y
\end{array}\right)=\left(\begin{array}{c}
x \\
y-t x
\end{array}\right)
$$

当 $t$ 为整数时, 变换还是保整点的. 于是笔者尝试通过变换将椭圆保面积保整点地变为 $\hat{E}$. 经过讨论, 苏宇坚老师给出了以下证明:

证明 (问题 1) 首先以原点为中心进行放缩变换, 使得原点是 $E$ 内部唯一整点, 而 $E$ 上有整点 $\left(x_{0}, y_{0}\right)$. 则 $\operatorname{gcd}\left(x_{0}, y_{0}\right)=1$, 否则 $\left(\frac{x_{0}}{\operatorname{gcd}\left(x_{0}, y_{0}\right)}, \frac{y_{0}}{\operatorname{gcd}\left(x_{0}, y_{0}\right)}\right)$ 是 $E$内部另一整点 ( $\operatorname{gcd}$ 表示最大公约数).

于是由裴蜀定理, 存在 $p, q \in \mathbb{Z}$, 使得 $p x_{0}+q y_{0}=1$.

考察变换 $T$ :

$$
\left(\begin{array}{l}
x \\
y
\end{array}\right) \mapsto\left(\begin{array}{cc}
p & q \\
-y_{0} & x_{0}
\end{array}\right)\left(\begin{array}{l}
x \\
y
\end{array}\right)=\left(\begin{array}{c}
p x+q y \\
-y_{0} x+x_{0} y
\end{array}\right)
$$

由于 $\operatorname{det}\left(\begin{array}{cc}p & q \\ -y_{0} & x_{0}\end{array}\right)=1$, 故 $T$ 是保面积的.

$T(E)$ 是一个以原点为中心, 过 $(1,0)$ 的椭圆, 且其内部没有除原点以外的整点, 否则由逆变换 $T^{-1}=\left(\begin{array}{cc}x_{0} & -q \\ y_{0} & p\end{array}\right)$ 的保整点性, $E$ 内部有原点以外的整点.故由推论 $1, S(E)=S(T(E)) \leq \frac{2 \pi}{\sqrt{3}}$.

我们可以进一步研究包含 $2 n+1$ 个整点的椭圆面积的最大值. 对于一般的情形, [1] 中介绍了有关以原点为中心的椭圆内整点数和本元整点数的上界的结论, 包括:

定义 $A(x)=\left|(m, n) \in \mathbb{Z}^{2}: a m^{2}+b m n+c n^{2} \leq x\right|$ 为椭圆内的整点数, 则有以下估计:

$$
A(x)=\frac{2 \pi}{\sqrt{4 a c-b^{2}}} x+P(x)
$$

其中余项 $P(x)$ 有上界:

$$
P(x) \ll x^{\frac{23}{73}}(\log x)^{\frac{315}{146}} .
$$

其方法远远超过初等范畴, 还是考察简单情况:
问题 2 设 $E \subset \mathbb{R}^{2}$ 是一个以原点为中心且内部含有不超过 3 个整点的椭圆，求其面积的最大值.

猜测 $E$ 过 $(1,0),(0,1),(2,2)$ 时取到最大值 (图 4), 经计算为 $S_{E}=\frac{8 \pi}{\sqrt{15}} \approx$ 6.4893 .

![](https://cdn.mathpix.com/cropped/2024_02_26_98b546c7d609df3f9275g-5.jpg?height=654&width=714&top_left_y=541&top_left_x=677)

图 4. 过 $(1,0),(0,1),(2,2)$ 的椭圆

然而此时椭圆上的整点 $\left(x_{0}, y_{0}\right)$ 不再有 $\operatorname{gcd}\left(x_{0}, y_{0}\right)=1$, 于是逆变换不再保整点, 前面的解法不适用于此.

在讨论中复旦附中的施方彦同学又提出了新的思路:

引理 2 设 $E$ 是以原点 $O$ 为中心的椭圆, 过 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right), C\left(x_{3}, y_{3}\right)$ 三点, 且 $A B, A C, B C$ 不过 $O$, 则椭圆面积为

$$
S_{E}=\frac{2 S_{1} S_{2} S_{3} \pi}{\sqrt{\left(S_{1}+S_{2}+S_{3}\right)\left(S_{1}+S_{2}-S_{3}\right)\left(S_{2}+S_{3}-S_{1}\right)\left(S_{3}+S_{1}-S_{2}\right)}},
$$

其中 $S_{1}=2 S_{\triangle O B C}=\left|x_{2} y_{3}-x_{3} y_{2}\right|, \quad S_{2}=2 S_{\triangle O C A}=\left|x_{3} y_{1}-x_{1} y_{3}\right|, \quad S_{3}=$ $2 S_{\triangle O A B}=\left|x_{1} y_{2}-x_{2} y_{1}\right|$.

证明 设椭圆方程为 $a x^{2}+b x y+c y^{2}=1, a, b, c \in \mathbb{R}$, 则 $a, b, c$ 可由 $A\left(x_{1}, y_{1}\right)$, $B\left(x_{2}, y_{2}\right), C\left(x_{3}, y_{3}\right)$ 解出. 由克莱默法则,

$$
a=\frac{D_{1}}{D}, \quad b=\frac{D_{2}}{D}, \quad c=\frac{D_{3}}{D}
$$

其中 $D_{1}=\left|\begin{array}{lll}1 & x_{1} y_{1} & y_{1}^{2} \\ 1 & x_{2} y_{2} & y_{2}^{2} \\ 1 & x_{3} y_{3} & y_{3}^{2}\end{array}\right|, \quad D_{2}=\left|\begin{array}{lll}x_{1}^{2} & 1 & y_{1}^{2} \\ x_{2}^{2} & 1 & y_{2}^{2} \\ x_{3}^{2} & 1 & y_{3}^{2}\end{array}\right|$,

$$
\begin{aligned}
D_{3}= & \left|\begin{array}{lll}
x_{1}^{2} & x_{1} y_{1} & 1 \\
x_{2}^{2} & x_{2} y_{2} & 1 \\
x_{3}^{2} & x_{3} y_{3} & 1
\end{array}\right|, D=\left|\begin{array}{lll}
x_{1}^{2} & x_{1} y_{1} & y_{1}^{2} \\
x_{2}^{2} & x_{2} y_{2} & y_{2}^{2} \\
x_{3}^{2} & x_{3} y_{3} & y_{3}^{2}
\end{array}\right| \\
& 4 D_{1} D_{3}-D_{2}^{2} \\
= & 4 \sum_{c y c} y_{1} y_{2} S_{3} \sum_{c y c} x_{1} x_{2} S_{3}-\left(\sum_{c y c}\left(x_{1} y_{2}+x_{2} y_{1}\right) S_{3}\right)^{2} \\
= & \sum_{c y c}\left[4 x_{1} x_{2} y_{1} y_{2}-\left(x_{1} y_{2}+x_{2} y_{1}\right)^{2}\right] S_{3}^{2} \\
& \quad+\sum_{c y c}\left[4 x_{1} x_{2} y_{1} y_{3}+4 x_{1} x_{3} y_{1} y_{2}-2\left(x_{1} y_{2}+x_{2} y_{1}\right)\left(x_{1} y_{3}+x_{3} y_{1}\right)\right] S_{2} S_{3} \\
= & \sum_{c y c}-\left(x_{1} y_{2}-x_{2} y_{1}\right)^{2} S_{3}^{2}+2 \sum_{c y c}\left(x_{1} y_{2}-x_{2} y_{1}\right)\left(x_{1} y_{3}-x_{3} y_{1}\right) S_{2} S_{3} \\
= & -\sum_{c y c} S_{3}^{4}+2 \sum_{c y c} S_{2}^{2} S_{3}^{2} \\
= & \left(S_{1}+S_{2}+S_{3}\right)\left(S_{1}+S_{2}-S_{3}\right)\left(S_{2}+S_{3}-S_{1}\right)\left(S_{3}+S_{1}-S_{2}\right) .
\end{aligned}
$$

利用范德蒙行列式来计算 $|D|$ :

$$
|D|=\left|x_{1}^{2} x_{2}^{2} x_{3}^{2}\left(\frac{y_{1}}{x_{1}}-\frac{y_{2}}{x_{2}}\right)\left(\frac{y_{2}}{x_{2}}-\frac{y_{3}}{x_{3}}\right)\left(\frac{y_{3}}{x_{3}}-\frac{y_{1}}{x_{1}}\right)\right|=S_{1} S_{2} S_{3} .
$$

于是椭圆面积

$$
\begin{aligned}
S_{E} & =\frac{2 \pi}{\sqrt{4 a c-b^{2}}}=\frac{2|D| \pi}{\sqrt{4 D_{1} D_{3}-D_{2}^{2}}} \\
& =\frac{2 S_{1} S_{2} S_{3} \pi}{\sqrt{\left(S_{1}+S_{2}+S_{3}\right)\left(S_{1}+S_{2}-S_{3}\right)\left(S_{2}+S_{3}-S_{1}\right)\left(S_{3}+S_{1}-S_{2}\right)}} .
\end{aligned}
$$

由引理 2 可以立刻推出性质 1:

证明 (性质 1 另证) 在引理 2 中取 $A, B, C$ 分别为 $\left(\frac{1}{t}, 0\right)$ 及椭圆与直线 $y=1$的两交点, 则 $S_{1}, S_{2}, S_{3}$ 分别为 $d, \frac{1}{t}, \frac{1}{t}$, 故 $S_{E}=\frac{2 \pi}{\sqrt{4 t^{2}-t^{4} d^{2}}}$.

由引理 2 还有一个副产物:

推论 2 设 $E$ 是以原点 $O$ 为中心的椭圆, 过 $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right), C\left(x_{3}, y_{3}\right)$三点, 且 $A B, A C, B C$ 不过 $O$, 则 $S_{\triangle O B C}, S_{\triangle O C A}, S_{\triangle O A B}$ 满足两个之和大于第三个.

为叙述方便, 对任意点 $A(x, y)$, 记 $A^{\prime}=(-x,-y)$ 为其关于原点的对称点.

跳离引理 2 的背景, 笔者还想到了推论 2 的以下证明:
证明 (推论 2 另证) 注意到将 $A$ 替换为 $A^{\prime}$, 三个三角形面积不变; 而总可以通过对 $A, B, C$ 适当的替换, 使得 $O A B C$ 为凸四边形, 于是

$$
S_{\triangle O A B}+S_{\triangle O B C}=S_{O A B C} \geq S_{\triangle O C A}
$$

同理可得另两式.

沿这一思路可以解决问题 2:

证明 (问题 2) 若 $E$ 上不足六个整点, 固定 $A, B$, 使得 $E$ 上除 $A, B, A^{\prime}, B^{\prime}$外没有整点, 将向量 $O C$ 放缩 $k$ 倍得到 $C_{k}$, 记过 $A, B, C_{k}$ 的关于原点对称的二次曲线为 $E_{k}$, 其中 $\frac{S_{3}}{S_{1}+S_{2}}<k<\frac{S_{3}}{\left|S_{1}-S_{2}\right|}$ 时 $E_{k}$ 为椭圆. $E_{k}$ 内的整点个数随 $k$ “连续"变化, 故存在

$$
\frac{S_{3}}{S_{1}+S_{2}}<k_{1}<1<k_{2}<\frac{S_{3}}{\left|S_{1}-S_{2}\right|}
$$

使得 $E_{k_{1}}$ 和 $E_{k_{2}}$ 内整点个数不变而 $E_{k_{1}}$ 和 $E_{k_{2}}$ 上有新的整点. 注意到

$$
S_{\triangle O C_{k} A}=k S_{\triangle O C A}, S_{\triangle O B C_{k}}=k S_{\triangle O B C}
$$

从而

$$
S\left(E_{k}\right)=\frac{2 S_{1} S_{2} S_{3} \pi}{\sqrt{\left(S_{1}+S_{2}+\frac{S_{3}}{k}\right)\left(S_{1}+S_{2}-\frac{S_{3}}{k}\right)\left(S_{2}+\frac{S_{3}}{k}-S_{1}\right)\left(\frac{S_{3}}{k}+S_{1}-S_{2}\right)}}
$$

其中记

$F(k)=\left(\frac{S_{3}}{k}\right)^{2}, G(k)=\left(S_{1}+S_{2}+\frac{S_{3}}{k}\right)\left(S_{1}+S_{2}-\frac{S_{3}}{k}\right)\left(S_{2}+\frac{S_{3}}{k}-S_{1}\right)\left(\frac{S_{3}}{k}+S_{1}-S_{2}\right)$.

则 $F(k)$ 关于 $k$ 单调下降; 而 $G(k)$ 是 $F(k)$ 的首项系数为负的二次函数, 关于 $F(k)$ 先升再降, 故关于 $k$ 先升再降; 进一步 $S\left(E_{k}\right)$ 关于 $G(k)$ 单调下降, 故关于 $k$ 先降再升, 从而必有 $\max \left\{S\left(E_{k_{1}}\right), S\left(E_{k_{2}}\right)\right\}>S(E)$. 故只需考虑 $E$ 上有至少六个整点的情况.

当 $A, B, C$ 皆为整点时, 由皮克定理, $S_{1}, S_{2}, S_{3}$ 都是正整数. 另一方面 $S_{1}$, $S_{2}, S_{3}$ 又受椭圆内整点数的限制. 考察整点凸多边形 $A B C A^{\prime} B^{\prime} C^{\prime}$, 其面积为 $S_{1}+S_{2}+S_{3}$.

同时其内部/边界的非顶点整点都是 $E$ 的内部整点, 即除了顶点外 $A B C$ $A^{\prime} B^{\prime} C^{\prime}$ 至多有 3 个内部/边界整点. 故由皮克定理 $S_{1}+S_{2}+S_{3} \leq \frac{6}{2}+3-1=5$.结合推论 2 知可重集 $\left\{S_{1}, S_{2}, S_{3}\right\}=\{1,1,1\}$ 或 $\{1,2,2\}$. 最大值在 $\left\{S_{1}, S_{2}, S_{3}\right\}=$ $\{1,2,2\}$ 时取到, 此时 $S_{E}=\frac{8 \pi}{\sqrt{15}}$.

问题 3 设 $E \subset \mathbb{R}^{2}$ 是一个以原点为中心且内部含有 5 个整点的椭圆, 求其
面积的最大值.

证明 类似问题 2 的分析, 可知 $S_{1}+S_{2}+S_{3} \leq \frac{6}{2}+5-1=7$. 只需比较 $\left\{S_{1}, S_{2}, S_{3}\right\}=\{1,3,3\},\{2,2,3\}$ 和 $\{2,2,2\}$.

第一种在 $A(0,1), B(1,0), C(3,3)$ 时可取到, 面积为 $\frac{18 \pi}{\sqrt{35}} \approx 9.5585$ (图 5); 第二种在 $A(1,0), B(0,2), C(1,3)$ 时可取到, 面积为 $\frac{8 \pi}{\sqrt{7}} \approx 9.4993$ (图 6); 第三种在 $A(2,0), B(0,2), C(2,2)$ 时可取到, 面积为 $\frac{4 \pi}{\sqrt{3}} \approx 7.2552$. 故椭圆面积的最大值为 $S_{E}=\frac{18 \pi}{\sqrt{35}}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_98b546c7d609df3f9275g-8.jpg?height=765&width=808&top_left_y=774&top_left_x=630)

图 5. 过 $(0,1),(1,0),(3,3)$ 的椭圆

![](https://cdn.mathpix.com/cropped/2024_02_26_98b546c7d609df3f9275g-8.jpg?height=683&width=596&top_left_y=1680&top_left_x=730)

图 6. 过 $(1,0),(0,2),(1,3)$ 的粗圆

本质上说, 上述方法利用的是椭圆及其某个内接整点六边形之间面积/包含整点数的双重关系. 当陏圆内整点数较大时, 内接整点六边形包含的整点数可
能不再与椭圆包含的整点数相等, 预计这将是这类方法的局限性, 有待继续研究探明.

## 参考文献

[1] W. G. Nowak. Primitive lattice points inside an ellipse [J]. Czechoslovak Mathematical Journal, 55(2):519-530, 2005.


[^0]:    修订日期: 2021-06-21.

