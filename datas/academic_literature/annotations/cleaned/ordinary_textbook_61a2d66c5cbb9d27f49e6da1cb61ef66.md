# 对一道组合几何问题的再讨论 

䨉霄宇<br>(重庆市巴蜀中学校, 400013)<br>指导教师: 肖佳劼

2016 年中国国家队选拔考试第 5 题题面如下:

问题 1 设 $S \subset \mathbb{R}^{2}$ 有限且任意三点不共线, 满足 $\operatorname{conv} S$ (即 $S$ 的凸包) 为 2016 边形 $A_{1} A_{2} \cdots A_{2016}$. 函数 $f: S \rightarrow\{-2,-1,1,2\}$ 满足

$$
f\left(A_{i}\right)+f\left(A_{i+1008}\right)=0, i=1,2, \cdots, 1008
$$

求证: 对任意以 $S$ 为顶点集的 $\operatorname{conv} S$ 的三角剖分, 存在其中一个三角形的某两个顶点的函数值互为相反数.

我们在这篇文章中将用一个拓扑学的角度看待这个问题并给出一个新证明。

考虑映射 $\varphi:\{-2,-1,1,2\} \rightarrow \mathbb{Z}_{4} ，$

$$
-2 \mapsto \overline{0},-1 \mapsto \overline{1}, 1 \mapsto \overline{3}, 2 \mapsto \overline{2}
$$

其中 $\mathbb{Z}_{4}$ 为模 4 意义下的同余类构成的集合, $\bar{n}$ 为 $n$ 所在的同余类. 考虑 $g=\varphi f$.则

$$
f(A)+f(B)=0 \Leftrightarrow g(A)=g(B)+\overline{2} .
$$

在拓扑学中, 我们知道, 对于连续函数 $f:[0,1]^{n} \rightarrow S^{1}$, 存在连续函数(称为其提升) $\tilde{f}:[0,1]^{n} \rightarrow \mathbb{R}$, 使得

$$
f=\psi \tilde{f}
$$

其中 $S^{1}$ 为复平面上的单位圆且

$$
\psi: x \mapsto \mathrm{e}^{2 \pi \mathrm{i} x}
$$

修订日期: 2022-04-21.
在这里, 我们将 $\mathbb{Z}_{4}$ 看作是一个“离散” 的单位圆:



我们将按照三角剖分的边连线的图 $S$ 看作 “离散” 的 $[0,1]^{2}$, 并将没有相邻点 $A, B$ 使

$$
g(A)=g(B)+\overline{2}
$$

成立的函数 $g: S \rightarrow \mathbb{Z}_{4}$ 看作 “离散” 的“连续” 函数(因为相邻点映射到的数值“差” 不超过1). 我们如果能证明这样的“连续” (即相邻点映射到的数值之差不超过1) 的“提升”

$$
\tilde{g}: S \rightarrow \mathbb{Z}
$$

存在, 即

$$
g=\pi \tilde{g}
$$

其中 $\pi: \mathbb{Z} \rightarrow \mathbb{Z}_{4}$,

$$
n \mapsto \bar{n}
$$

是自然映射,则我们可以如下导出矛盾: 考察

$$
a_{i}=\tilde{g}\left(A_{i}\right)-\tilde{g}\left(A_{i+1008}\right), i \in \mathbb{Z},
$$

其中下标 $\bmod 2016$ 考虑. 则由 $\tilde{g}$ 的“连续性” 以及 $\pi a_{i}=\overline{2}$ 知 $a_{i}$ 是常数. 从而

$$
a_{1}=a_{1009} \equiv 2 \quad(\bmod 4)
$$

但是

$$
a_{1}+a_{1009}=0 \text {. }
$$

矛盾. 这样便可以完成原命题的证明. 下面就来给出这个证明.

证明 记 $\mathbb{Z}_{4}$ 为模 4 意义下的同余类构成的集合, 并以显然的方式定义加减法. 对 $n \in \mathbb{Z}$, 记 $\bar{n} \in \mathbb{Z}_{4}$ 为 $n$ 所在的同余类. 定义“自然映射” $\pi: \mathbb{Z} \rightarrow \mathbb{Z}_{4}$ 为

$$
n \mapsto \bar{n}
$$

则 $\pi$ 保持加减法.
定义 $\varphi:\{-2,-1,1,2\} \rightarrow \mathbb{Z}_{4}$,

$$
-2 \mapsto \overline{0},-1 \mapsto \overline{1}, 1 \mapsto \overline{3}, 2 \mapsto \overline{2},
$$

并定义 $g=\varphi f$ 为 $\varphi$ 与 $f$ 的复合. 则对两点 $u, v \in S$ 有

$$
g(u)-g(v)=\overline{2} \Leftrightarrow f(u)=-f(v) .
$$

若结论不成立, 构造简单无向图 $G=(S, E), E \subseteq S^{2}$, 满足 $(u, v) \in E$ 当且仅当 $u v$ 是三角剖分中某个三角形的边. 易知 $G$ 连通. 由反证假设, 对每一条边 $e=(u, v) \in E$, 有

$$
f(u) \neq-f(v),
$$

从而存在(唯一的) $t(e) \in\{-1,0,1\}$ 满足

$$
g(v)-g(u)=\pi(t(e)) .
$$

对一条边 $e=(u, v) \in E$, 记

$$
e^{-1}=(v, u) \in E
$$

则易知

$$
t(e)+t\left(e^{-1}\right)=0 .
$$

若 $G$ 中有一个圈

$$
e_{1} e_{2} \cdots e_{m}
$$

满足

$$
\sum_{i=1}^{m} t\left(e_{i}\right) \neq 0
$$

设这个圈对应到的 $\mathbb{R}^{2}$ 中的不自交闭折线(由三角剖分的定义, 任意两条边只能相交在顶点上) 的内部是 $K(\neq \varnothing)$. 取一个反例使得 $K$ 的面积最小. 利用 $t(e)$的定义知

$$
\pi\left(\sum_{i=1}^{m} t\left(e_{i}\right)\right)=\sum_{i=1}^{m}\left(g\left(x_{i+1}\right)-g\left(x_{i}\right)\right)=\overline{0}
$$

其中 $e_{i}=\left(x_{i}, x_{i+1}\right), x_{n+1}=x_{1}$. 因此, $\sum_{i=1}^{m} t\left(e_{i}\right)$ 是 4 的倍数,

$$
4 \leq\left|\sum_{i=1}^{m} t\left(e_{i}\right)\right| \leq m
$$

则 $K$ 的边界被一条由 $E$ 中的边构成的通路(在 $\mathbb{R}^{2}$ 中对应的折线) “砍”成两半,否则 $K$ 的整个边界, 即 $e_{1}, e_{2}, \cdots, e_{m}$ 这所有 $m$ 条边在 $\mathbb{R}^{2}$ 中对应的线段, 会同
时包含于某个有界区域, 即三角剖分中的某个三角形的边界中, 与

$$
m \geq 4
$$

矛盾. 易知, 可设这个通路不自交, 且完全含在 $K$ 内 (两端点除外). 为了方便起见, 不妨设 $x_{1}$ 是这个通路的终点. 即, 存在 $1<i \leq n$ 以及若干条边

$$
f_{1}, f_{2}, \cdots, f_{\ell} \in E
$$

使得

$$
e_{1} e_{2} \cdots e_{i-1} f_{1} f_{2} \cdots f_{\ell}, e_{i} e_{i+1} \cdots e_{n} f_{\ell}^{-1} f_{\ell-1}^{-1} \cdots f_{1}^{-1}
$$

均为 $\left(G\right.$ 中的) 圈, 且它们在 $\mathbb{R}^{2}$ 中对应的不自交闭折线的内部 $K_{1}, K_{2}(\neq \varnothing)$ 满足

$$
K_{1} \cap K_{2}=\varnothing, K_{1}, K_{2} \subseteq K
$$

由此易知 $K_{1}, K_{2}$ 的面积均小于 $K$ 的面积, 则由最小性假设, 知

$$
\begin{aligned}
& t\left(e_{1}\right)+t\left(e_{2}\right)+\cdots+t\left(e_{i-1}\right)+t\left(f_{1}\right)+t\left(f_{2}\right)+\cdots+t\left(f_{\ell}\right) \\
= & t\left(e_{i}\right)+t\left(e_{i+1}\right)+\cdots+t\left(e_{n}\right)+t\left(f_{\ell}^{-1}\right)+t\left(f_{\ell-1}^{-1}\right)+\cdots+t\left(f_{1}^{-1}\right) \\
= & 0
\end{aligned}
$$

两式相加, 并利用 $t(e)+t\left(e^{-1}\right)=0$, 得

$$
\sum_{i=1}^{m} t\left(e_{i}\right)=0
$$

矛盾! 则对于 $G$ 中的所有圈

$$
e_{1} e_{2} \cdots e_{m}
$$

必有

$$
\sum_{i=1}^{m} t\left(e_{i}\right)=0
$$

我们再证明: 对图 $G$ 中的回路(顶点和边均可重) $e_{1} e_{2} \cdots e_{m}(m \geq 0)$ 必有

$$
\sum_{i=1}^{m} t\left(e_{i}\right)=0
$$

对 $m$ 归纳. $m=0$ 时显然. $m=1$ 不可能. $m=2$ 时利用 $t(e)+t\left(e^{-1}\right)=0$即证. 设 $<m$ 时成立, 考虑 $m$ 的情况 $(m \geq 3)$. 可设这个回路不是圈. 设

$$
e_{i}=\left(u_{i}, u_{i+1}\right), i=1,2, \cdots, m
$$

其中 $u_{1}, u_{2}, \cdots, u_{m} \in S, u_{m+1}=u_{1}$. 由于 $m \geq 3$, 且这个回路不是圈, 必存在
$1 \leq i<j \leq m$ 使

$$
u_{i}=u_{j} .
$$

对回路 $e_{i} e_{i+1} \cdots e_{j-1}$ 与回路 $e_{j} e_{j+1} \cdots e_{m} e_{1} e_{2} \cdots e_{i-1}$ 分别运用归纳假设并相加即可. (*) 得证.

现在, 对 $u, v \in S$, 设 $e_{1} e_{2} \cdots e_{m}$ 与 $f_{1} f_{2} \cdots f_{\ell}$ 为 $u$ 到 $v$ 的两条链(顶点和边均可重) $m, \ell \geq 0$, 则

$$
e_{1} e_{2} \cdots e_{m} f_{\ell}^{-1} f_{\ell-1}^{-1} \cdots f_{1}^{-1}
$$

为一个回路. 由 $(*)$,

$$
\sum_{i=1}^{m} t\left(e_{i}\right)=-\sum_{i=1}^{\ell} t\left(f_{i}^{-1}\right)=\sum_{i=1}^{\ell} t\left(f_{i}\right)
$$

现在取定 $u \in S$ 和 $x_{0} \in \pi^{-1}(g(u))$ ，则由上面的讨论，

$$
\tilde{g}(v)=x_{0}+\sum_{i=1}^{m} t\left(e_{i}\right)
$$

是一个良定义的函数, 其中 $v \in S, e_{1} e_{2} \cdots e_{m}$ 是任意一条从 $u$ 到 $v$ 的链(由连通性, 这条链存在), $m \geq 0$. 对一条边

$$
e=(v, w) \in E
$$

设 $e_{1} e_{2} \cdots e_{m}$ 是一条从 $u$ 到 $v$ 的链, 则 $e_{1} e_{2} \cdots e_{m} e$ 是一条从 $u$ 到 $w$ 的链. 由 $\tilde{g}$的定义中链的选择的任意性, 有

$$
\left\{\begin{array}{l}
\tilde{g}(v)=x_{0}+\sum_{i=1}^{m} t\left(e_{i}\right), \\
\tilde{g}(w)=x_{0}+\sum_{i=1}^{m} t\left(e_{i}\right)+t(e),
\end{array}\right.
$$

则

$$
t(e)+\tilde{g}(v)=\tilde{g}(w),
$$

故相邻两点的 $\tilde{g}$ 值之差不超过 1 . 另一方面, 由 $t, \tilde{g}$ 和 $x_{0}$ 的定义易知

$$
\pi(\tilde{g}(v))=g(v), \forall v \in S
$$

即

$$
\pi \tilde{g}=g
$$

记

$$
a_{i}=\tilde{g}\left(A_{i}\right)-\tilde{g}\left(A_{i+1008}\right),
$$

其中下标 $\bmod 2016$ 考虑. 则由前面的讨论, 由于

$$
f\left(A_{i}\right)=-f\left(A_{i+1008}\right),
$$

故

$$
\pi\left(a_{i}\right)=g\left(A_{i}\right)-g\left(A_{i+1008}\right)=\overline{2}
$$

从而

$$
4 \mid a_{i}-a_{i+1} .
$$

但是由于相邻点的 $\tilde{g}$ 值之差不超过 1 , 我们有

$$
\left|a_{i}-a_{i+1}\right| \leq 2<4 .
$$

由此可知

$$
a_{i}=a_{i+1}, \forall i \in \mathbb{Z}
$$

这说明

$$
a_{1}=a_{2}=\cdots=a_{1009}
$$

但是

$$
a_{1}+a_{1009}=0 .
$$

从而

$$
a_{1}=a_{1009}=0 .
$$

这与

$$
\pi\left(a_{1}\right)=\overline{2}
$$

矛盾!

致谢 作者感谢审稿人的细致反馈和冷岗松教授的热心关怀.

