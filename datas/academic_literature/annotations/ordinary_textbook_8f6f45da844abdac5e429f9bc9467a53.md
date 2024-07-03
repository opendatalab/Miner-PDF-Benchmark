# 数节数 

## 张瑞祥

我曾经写过一篇 “多项式方法” 的文章. 此方法的要点在于: 用一个辅助的多项式来获得某类几何对象 (通常排列在直线或低次代数曲线上) 的有效上界. 具体来说, 它通常涉及如下两步:

1. 假设我们要研究某个点集, 它排列在一些直线上, 则可考虑作一个多项式, 在该点集上恒为 0 .
2. 利用事实 “一个 $d$ 次多项式若在一条直线上 $(d+1)$ 个点处为 0 , 则它在这条直线上恒为 0 ”来得到有效的估计.

今天我们介绍这一方法的又一有利应用: 节 (joint) 数的上界估计.

定义 1 在三维空间 $\mathbb{R}^{3}$ 中任给 $n$ 条直线, 它们在点 $p$ 处形成一个 “节”, 则有 3 条给定的直线同时过 $p$ 且不共面.

对于节的研究, 最早见于图像处理相关文章 [1].

一个自然且有趣的问题是：设 $J$ 为节的集合，那么 $|J|$ 最大是多少?

显然的上界是 $\left(\begin{array}{l}n \\ 2\end{array}\right)$, 这也是二维中类似问题的答案. 而一个容易的下界则有数量级 $n^{\frac{3}{2}}$, 它由一个约 $\left(\frac{1}{\sqrt{3}} n^{\frac{1}{2}}\right) \times\left(\frac{1}{\sqrt{3}} n^{\frac{1}{2}}\right) \times\left(\frac{1}{\sqrt{3}} n^{\frac{1}{2}}\right)$ 的三维网格给出.

[1] 中已给出 $|J|$ 的一个上界估计, 证明其数量级不超过 $n^{\frac{7}{4}}$. 在 2008 年, Guth 和 Katz 在 [2] 中证明了上界也是 $n^{\frac{3}{2}}$ 数量级的, 从而在渐近意义下完全解决了这个问题. 他们的证明用到了多项式方法. 我们给出一个不同的证明, 但也将用到多项式方法.

以下证明中 $C$ 都是正的常数, 在不同地方出现时意义不必相同.

定理 (Guth-Katz ${ }^{[2]}$ ) 存在常数 $C$, 使 $|J| \leq C n^{\frac{3}{2}}$.

证明 我们找一个次数尽可能低的三元多项式 $Q(x, y, z) \not \equiv 0$ 在所有 $p \in J$上为 0 . 注意到一个次数 $\leq d$ 的三元多项式有 $\left(\begin{array}{c}d+3 \\ 3\end{array}\right) \geq \frac{1}{C} \cdot d^{3}$ 个独立的待定系数,[^0]而一个多项式在任一点 $p$ 处为 0 相当于关于其系数的一个一次齐次方程. 因此当 $\frac{1}{C} d^{3} \geq|J|$ 即 $d \geq C|J|^{\frac{1}{3}}$ 时, 我们可找到一个次数 $\leq d$ 的非零多项式在任意 $p \in J$ 上为 0 . 以下取 $d=\left\lceil C|J|^{\frac{1}{3}}\right\rceil$, 并记找到的多项式为 $Q(x, y, z)$, 则
- $\operatorname{deg} Q \leq C|J|^{\frac{1}{3}}$.
- $Q(p)=0, \forall p \in J$.

对于 $p \in J$ 和已给的直线 $p \in l$, 我们说三元组 $(p, l, Q)$ 是 “重要的”, 如果我们在 $p$ 处建立坐标系使 $l$ 为 $Z$ 轴方向, 则 $Q$ 在此坐标系表达式中最低次项与 $Z$ 相关. 否则我们称 $(p, l, Q)$ 是 “不重要的”.

注意到

(a) 对任意 $p \in J$ 及 $l_{1}, l_{2}, l_{3} \ni p$, 若 $l_{1}, l_{2}, l_{3}$ 不共面则 $p$ 至少关于 $Q$ 和其中一条线是重要的. 因若不然, 可以证明 $Q$ 在以 $p$ 为原点的坐标系中最低次项是一个与 $l_{1}, l_{2}, l_{3}$ 方向都无关的函数 (留作练习), 故只能是常数, 与 $Q(p)=0$ 矛盾.

另外, 我们有

(b) 任一条已给直线 $l$ 上只有 $\leq \operatorname{deg} Q$ 个重要的节, 即, 使 $(p, l, Q)$ 是重要的. 为此, 以 $l$ 为 $Z$ 轴建立直角坐标系, 设 $Q$ 在此坐标系下方程为 $\sum_{\alpha=\left(\alpha_{1}, \alpha_{2}\right)} P_{\alpha}(z) x^{\alpha_{1}} y^{\alpha_{2}}$.

设 $\alpha_{0}=\left(\alpha_{0_{1}}, \alpha_{0_{2}}\right)$ 使 $P_{\alpha_{0}}(2) \not \equiv 0$ 且 $\alpha_{0}$ 是使 $\alpha_{0_{1}}+\alpha_{0_{2}}$ 最小的. 则若 $z$ 不是 $p_{\alpha_{0}}$ 的根, $(p, l, Q)$ 一定不是重要的 (同样留作练习).

由 (a), (b), 有 $|J| \leq n \cdot \operatorname{deg} Q \leq C n \cdot|J|^{\frac{1}{3}}$. 故 $|J| \leq C n^{\frac{3}{2}}$. 证毕.

## 参考文献

[1] B. Chazelle, H. Edelsbmnner, L. Guibas, R. Pollack, R. Seidel, M. Sharir and J. Snoeyink, Counting and cutting cydes of lines and rods in space, Computational Geometry: Theory and Applications, 6(1992), no. 1, 305323.

[2] L. Guth and N. Katz, Algebraic methods in discrete analogs of the Kakeya problem, Advances in Mathematics, 225(2010), no. 5, 2828-2839.


[^0]:    收稿日期: 2018-06-17.

