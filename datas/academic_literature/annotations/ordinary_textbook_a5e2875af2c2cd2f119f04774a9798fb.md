# 第一期 一个数论问题 

邓煜

(南加州大学, University of Southern California)

问题 给定 $d \geq 2$, 以 $\mathbb{R}^{d}$ 上除原点 $O$ 外的各整点为中心作半径为 $\varepsilon \in(0,1)$的球. 称整点 $X \neq O$ 为可连的, 如果线段 $O X$ 只与以 $X$ 自身为中心的球相交. 定义 $R=R_{d}(\varepsilon)$ 为可连整点到原点的最大距离, 及 $N=N_{d}(\varepsilon)$ 为可连整点的个数.则极限

$$
\lim _{\varepsilon \rightarrow 0} \varepsilon^{d-1} R_{d}(\varepsilon) \text { 和 } \quad \lim _{\varepsilon \rightarrow 0} \varepsilon^{d(d-1)} N_{d}(\varepsilon)
$$

是否存在？其值为何?

注 (1). 在 $d=2$ 时问题可看作经典的果园视线问题 (Orchard visibility problem) 的一个变种 (涉及看向整点而非任意点的视线), 此时结论是熟知的, 即

$$
\lim _{\varepsilon \rightarrow 0} \varepsilon R_{2}(\varepsilon)=1, \quad \lim _{\varepsilon \rightarrow 0} \varepsilon^{2} N_{2}(\varepsilon)=\frac{6}{\pi}
$$

前者可参见 T.T. Allen, Polya's orchard problem, Amer. Math. Monthly, 93(1986) 98-104, 后者只需利用坐标互素整点的比例是 $6 / \pi^{2}$ 这一事实即可.

(2). 在 $d=3$ 时也可证明极限存在, 且

$$
\lim _{\varepsilon \rightarrow 0} \varepsilon^{2} R_{3}(\varepsilon)=\frac{2}{\sqrt{3}}, \quad \lim _{\varepsilon \rightarrow 0} \varepsilon^{6} N_{3}(\varepsilon)=\frac{4+3 \ln 3}{6 \zeta(3)} .
$$

(3). 以上证明中关键性地用到了二维向量的外积是数量, 而三维向量的外积仍是三维向量的事实. 在四维以上这一性质不再成立, 便使问题更加困难. 对 $d \geq 4$ 我们只知道存在常数 $0<c_{1}<c_{2}<\infty$, 使得

$$
c_{1}<\varepsilon^{d-1} R_{d}(\varepsilon)<c_{2}, \quad c_{1}<\varepsilon^{d(d-1)} N_{d}(\varepsilon)<c_{2}
$$

因此若所论极限存在, 其必为有限正值.

