数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 年匈牙利 Kürschák 竞赛试题解析 

胡佳旭 呙允文

(湖南师范大学附属中学, 410006)

指导教师: 汤礼达

匈牙利是数学竞赛的发源地, 而 Kürschák 竞赛是全球范围内历史最悠久的数学竞赛. 2021 年 Kürschák 竞赛试题新颖且优雅, 每个题颇有启发意义, 具有较高的训练价值. 感谢微信公众号 “偽同文算學” 提供的试题. 直于水平, 不当之处, 敬请读者批评指正.

## I. 试 题

1. 在平面直角坐标系中, 已知原点 $O(0,0)$ 为以三点 $P_{i}\left(a_{i}, b_{i}\right)(i=0,1,2)$为顶点的三角形的一个内点. 证明: $\triangle P_{0} O P_{1}, \triangle P_{0} O P_{2}, \triangle P_{1} O P_{2}$ 的面积 (在这个顺序下) 可以构成一个等比数列当且仅当方程

$$
a_{0} x^{2}+a_{1} x+a_{2}=b_{0} x^{2}+b_{1} x+b_{2}=0
$$

有一个实解 $x$.

2. 设整数 $n \geq 3$, 某个国家有 $n$ 座机场, 且有 $n$ 个航空公司, 这些航空公司经营的都是双向航线. 对任意航空公司, 都存在奇数座机场 $c_{1}, c_{2}, \cdots, c_{m}$, 使得这个航空公司经营的航线恰好是 $c_{1}-c_{2}, c_{2}-c_{3}, \cdots, c_{m-1}-c_{m}$ 和 $c_{m}-c_{1}$.

证明: 存在一条由奇数条航班组成的封闭路径, 其中没有任何两条航班由同一家航空公司经营.

3. 在圆内接六边形 $A_{1} B_{3} A_{2} B_{1} A_{3} B_{2}$ 中三条对角线 $A_{1} B_{1}, A_{2} B_{2}, A_{3} B_{3}$ 交于一点. 对 $i=1,2,3$, 我们记 $A_{i} B_{i}$ 与 $A_{i+1} A_{i+2}$ 的交点分别 $C_{i}$, 过 $B_{i}, C_{i}$ 作与 $A_{i+1} A_{i+2}$ 相切的圆, 记这个圆与六边形的外接圆除了 $B_{i}$ 的另一个交点为 $D_{i}$ (以上所有下标都模 3 考虑, 即 $A_{4}=A_{1}, A_{5}=A_{2}$ ).

修订日期: 2022-01-18.
证明: $A_{1} D_{1}, A_{2} D_{2}, A_{3} D_{3}$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_38228299d8c97a37b6c8g-2.jpg?height=645&width=642&top_left_y=314&top_left_x=707)

## II. 解答与评注

题 1 在平面直角坐标系中, 已知原点 $O(0,0)$ 为以三点 $P_{i}\left(a_{i}, b_{i}\right)(i=0,1,2)$为顶点的三角形的一个内点. 证明: $\triangle P_{0} O P_{1}, \triangle P_{0} O P_{2}, \triangle P_{1} O P_{2}$ 的面积 (在这个顺序下) 可以构成一个等比数列当且仅当方程

$$
a_{0} x^{2}+a_{1} x+a_{2}=b_{0} x^{2}+b_{1} x+b_{2}=0
$$

有一个实解 $x$.

证明 考虑方程

$$
\overrightarrow{O P_{0}} \cdot x+\overrightarrow{O P_{1}} \cdot y+\overrightarrow{O P_{2}} \cdot z=\overrightarrow{0}
$$

由于点 $O$ 为 $\triangle P_{0} P_{1} P_{2}$ 内一点, 所以 $\overrightarrow{O P_{0}}, \overrightarrow{O P_{1}}, \overrightarrow{O P_{2}}$ 两两不共线. 因此方程 $(*)$的解集为

$$
\left\{\left(k x_{0}, k y_{0}, k z_{0}\right) \mid k \in \mathbb{R}\right\},
$$

其中 $x_{0}, y_{0}, z_{0}$ 是不全为 0 的实数. 注意到

$$
a_{0} x^{2}+a_{1} x+a_{2}=b_{0} x^{2}+b_{1} x+b_{2}=0
$$

有实解, 等价于线性方程组

$$
\left\{\begin{array}{l}
a_{0} x+a_{1} y+a_{2} z=0 \\
b_{0} x+b_{1} y+b_{2} z=0
\end{array}\right.
$$

有形如 $\left(t^{2}, t, 1\right)$ 的解, 其中 $t \in \mathbb{R}$.
又由奔驰定理, 有

$$
\overrightarrow{O P_{0}} \cdot S_{\triangle P_{1} O P_{2}}+\overrightarrow{O P_{1}} \cdot S_{\triangle P_{0} O P_{2}}+\overrightarrow{O P_{2}} \cdot S_{\triangle P_{0} O P_{1}}=\overrightarrow{0}
$$

分别取上式在 $x$ 轴, $y$ 轴上的投影可得方程组, 即

$$
\left\{\begin{array}{l}
a_{0} \cdot S_{\triangle P_{1} O P_{2}}+a_{1} \cdot S_{\triangle P_{0} O P_{2}}+a_{2} \cdot S_{\triangle P_{0} O P_{1}}=0 \\
b_{0} \cdot S_{\triangle P_{1} O P_{2}}+b_{1} \cdot S_{\triangle P_{0} O P_{2}}+b_{2} \cdot S_{\triangle P_{0} O P_{1}}=0
\end{array} .\right.
$$

故可不妨设

$$
x_{0}=S_{\triangle P_{1} O P_{2}}, y_{0}=S_{\triangle P_{0} O P_{2}}, z_{0}=S_{\triangle P_{0} O P_{1}} \text {, }
$$

此时

$$
S_{\triangle P_{1} O P_{2}}, S_{\triangle P_{0} O P_{2}}, S_{\triangle P_{0} O P_{1}} \text { 构成等比数列 } \Leftrightarrow x_{0} z_{0}=y_{0}^{2}
$$

故原命题成立.

评注 本题是一道简单的代数题. 直接计算有点繁琐, 把原题中的方程看成线性方程组, 并用线性方程组的性质的求解, 能揭示其本质.

本题中用到的奔驰定理叙述如下:

设 $P$ 为 $\triangle A B C$ 内一点, 则有

$$
\overrightarrow{A P} \cdot S_{\triangle B P C}+\overrightarrow{B P} \cdot S_{\triangle C P A}+\overrightarrow{C P} \cdot S_{\triangle A P B}=\overrightarrow{0}
$$

它也是联赛一试中常用的结论, 为本题的线性方程组提供了一组特解.

题 2 设整数 $n \geq 3$, 某个国家有 $n$ 座机场, 且有 $n$ 个航空公司, 这些航空公司经营的都是双向航线. 对任意航空公司, 都存在奇数座机场 $c_{1}, c_{2}, \cdots, c_{m}$, 使得这个航空公司经营的航线恰好是 $c_{1}-c_{2}, c_{2}-c_{3}, \cdots, c_{m-1}-c_{m}$ 和 $c_{m}-c_{1}$.

证明: 存在一条由奇数条航班组成的封闭路径, 其中没有任何两条航班由同一家航空公司经营.

证明 (胡佳旭) 用图论语言叙述此题: $n$ 阶图 $G$ 的边有 $n$ 种颜色, 且每种颜色的边构成一个奇闭合迹, 其中 $G$ 可以有重边, 但无环. 本题即证: $G$ 中存在一条各边不同色的奇闭合迹.

取 $G$ 的边数最多的各边不同色的生成森林 $F$, 由 $F$ 至多有 $n-1$ 条边可知至少有一种颜色不在 $F$ 中出现.

由 $F$ 的最大性知, 加入任何该色边后将生成一个圈, 故任意该色边的两端点在同一棵树上, 进而该色奇闭合迹的顶点均在同一棵树上.

将此树看作二部图, 由奇闭合迹不是二部图知, 有一条该色边的两端点在同
一部集内, 加入此边后, 树上生成了一个各边不同色的奇圈, 这个圈即为所求, 故得证.

评注 本题即为 2020 年罗马尼亚大师杯的第三题. 因为难以从较小的情况发掘普遍性的结论, 所以不得不直接做一般性分析. 最初的想法会是每色各取一边, 则必有一个圈. 但这无法利用条件, 不好证明该圈的奇性, 那么我们退而求次, 用经典的树添边生成圈的方法来保证圈的一些有用性质. 考虑到树是二部图便会想到添一边在同一部集中，结合条件即知只需证明某个奇闭合迹的顶点在同一棵树上, 这时的极端分析已是水到渠成了.本题有一定难度.

题 3 在圆内接六边形 $A_{1} B_{3} A_{2} B_{1} A_{3} B_{2}$ 中三条对角线 $A_{1} B_{1}, A_{2} B_{2}, A_{3} B_{3}$交于一点. 对 $i=1,2,3$, 我们记 $A_{i} B_{i}$ 与 $A_{i+1} A_{i+2}$ 的交点分别 $C_{i}$, 过 $B_{i}, C_{i}$ 作与 $A_{i+1} A_{i+2}$ 相切的圆, 记这个圆与六边形的外接圆除了 $B_{i}$ 的另一个交点为 $D_{i}$ (以上所有下标都模 3 考虑, 即 $A_{4}=A_{1}, A_{5}=A_{2}$ ).

证明: $A_{1} D_{1}, A_{2} D_{2}, A_{3} D_{3}$ 三线共点.

![](https://cdn.mathpix.com/cropped/2024_02_26_38228299d8c97a37b6c8g-4.jpg?height=625&width=640&top_left_y=1298&top_left_x=708)

证明 (呙允文) 设直线 $C_{1} D_{1}$ 交 $\odot\left(A_{1} A_{2} A_{3}\right)$ 于另一点 $A_{1}^{\prime}$, 则有

$$
\begin{aligned}
& \angle A_{1}^{\prime} A_{1} B_{1}=\angle A_{1}^{\prime} D_{1} B_{1}=\angle A_{2} C_{1} B_{1} \\
\Rightarrow & A_{1} A_{1}^{\prime} / / A_{2} A_{3}, A_{1}^{\prime} A_{2}=A_{1} A_{3}, A_{1}^{\prime} A_{3}=A_{1} A_{2}
\end{aligned}
$$

因此有

$$
\frac{\sin \angle A_{2} A_{1} D_{1}}{\sin \angle A_{3} A_{1} D_{1}}=\frac{\sin \angle A_{2} A_{1}^{\prime} D_{1}}{\sin \angle A_{3} A_{1}^{\prime} D_{1}}=\frac{A_{2} C_{1}}{A_{3} C_{1}} \cdot \frac{A_{1}^{\prime} A_{3}}{A_{1}^{\prime} A_{2}}=\frac{A_{2} C_{1}}{A_{3} C_{1}} \cdot \frac{A_{1} A_{2}}{A_{1} A_{3}} .
$$

同理

$$
\frac{\sin \angle A_{1} A_{3} D_{3}}{\sin \angle A_{2} A_{3} D_{3}}=\frac{A_{1} C_{3}}{A_{2} C_{3}} \cdot \frac{A_{1} A_{3}}{A_{3} A_{2}}, \frac{\sin \angle A_{3} A_{2} D_{2}}{\sin \angle D_{2} A_{2} A_{1}}=\frac{A_{3} C_{2}}{A_{1} C_{2}} \cdot \frac{A_{3} A_{2}}{A_{1} A_{2}}
$$

故有

$$
\begin{aligned}
& \frac{\sin \angle A_{2} A_{1} D_{1}}{\sin \angle A_{3} A_{1} D_{1}} \cdot \frac{\sin \angle A_{1} A_{3} D_{3}}{\sin \angle A_{2} A_{3} D_{3}} \cdot \frac{\sin \angle A_{3} A_{2} D_{2}}{\sin \angle A_{1} A_{2} D_{2}} \\
& =\frac{A_{2} C_{1}}{A_{3} C_{1}} \cdot \frac{A_{1} C_{3}}{A_{2} C_{3}} \cdot \frac{A_{3} C_{2}}{A_{1} C_{2}} \cdot \frac{A_{1} A_{2}}{A_{1} A_{3}} \cdot \frac{A_{1} A_{3}}{A_{3} A_{2}} \cdot \frac{A_{3} A_{2}}{A_{1} A_{2}} \\
& =\frac{A_{2} C_{1}}{A_{3} C_{1}} \cdot \frac{A_{1} C_{3}}{A_{2} C_{3}} \cdot \frac{A_{3} C_{2}}{A_{1} C_{2}}
\end{aligned}
$$

由于 $A_{1} B_{1}, A_{2} B_{2}, A_{3} C_{3}$ 三线共点, 所以上式的值为 1 . 由角元 Ceva 定理知, $A_{1} D_{1}, A_{2} D_{2}, A_{3} D_{3}$ 共点.

评注 此题很好地体现了 Ceva 定理证明三线共点的作用, 难度并不大却较好考察了具有轮换性比例式的处理技巧。

