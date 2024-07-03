# 佩尔方程研究 

## 段剑儒 尹龙晖

(湖南省雅礼中学, 410007)

指导教师: 申东

## I. 如何化归一般二次(双曲)不定方程?

给定一个二元二次双曲型不定方程 $A x^{2}+B x y+C y^{2}+D x+E y+F=0$,我们可以通过逐步配方换元化为方程

$$
a x^{2}-b y^{2}=c
$$

我们无法直接解这个方程, 转化为佩尔方程再去研究. 为了方便, 设 $a, b, c, d \in$ $\mathbb{N}^{+}, a b$ 不为完全平方数.

考虑

$$
a x^{2}-b y^{2}=1
$$

假设我们已得到它的一组特解 $\left(x_{0}, y_{0}\right)$, 我们作如下代换

$$
\left\{\begin{array}{l}
x=x_{0} u+b y_{0} v \\
y=y_{0} u+c x_{0} v
\end{array}\right.
$$

注意到这是个关于 $x, y, u, v$ 的关系式, 将 (3) 代入 (2), 得

$$
a\left(x_{0} u+b y_{0} v\right)^{2}-b\left(y_{0} u+c x_{0} v\right)^{2}=1
$$

即

$$
\left(a x_{0}^{2}-b y_{0}^{2}\right) u^{2}-a b\left(a x_{0}^{2}-b y_{0}^{2}\right) v^{2}=1
$$

由于 $\left(x_{0}, y_{0}\right)$ 是 $(2)$ 的一组解, 从而

$$
u^{2}-a b v^{2}=1
$$

(4) 是一个关于 $u, v$ 的一型佩尔方程, 它必有无穷多组解.

通过 (3), 我们发现 (4) 的每一组正整数解唯一刻画 (2) 的一组正整数解, 那么 (2) 的正整数解能否对应 (4) 的一组整解呢? 即 (2) 与 (4) 是否有更深的联系呢?
通过 (3), 我们反解出 $u, v$ 可得

$$
\left\{\begin{array}{l}
u=a x_{0} x-b y_{0} y \\
v=-y_{0} x+x_{0} y
\end{array}\right.
$$

消元过程中用到了 $a x_{0}^{2}-b y_{0}^{2}=1$. 下面证明, 当 $x, y$ 为正整数解时, 由 (5) 确定的 $u, v$ 总为非负整数, 这需要 $\left(x_{0}, y_{0}\right)$ 为 $(2)$ 的一组最小解, 定义为使得 $\sqrt{a} x+\sqrt{b} y$ 最小的正整数解. 任取另一组正整数解 $x^{\prime}, y^{\prime}$, 必有 $x^{\prime}>x_{0}, y^{\prime}>$ $y_{0}, \sqrt{a} x^{\prime}+\sqrt{b} y^{\prime}>\sqrt{a} x_{0}+\sqrt{b} y_{0}$.

(i) 当 $x=x_{0}, y=y_{0}$, 由 (5) 得 $u=1, v=0$.

(ii) 当 $x>x_{0}, y>y_{0}$ 时, 若 $u \leq 0$, 则 $a x_{0} x \leq b y_{0} y, x \leq \frac{b y_{0}}{a x_{0}} y$. 故在 (2) 中,

$$
1=a x^{2}-b y^{2} \leq a\left(\frac{b y_{0}}{a x_{0}} y\right)^{2}-b y^{2}=b y^{2}\left(\frac{b y_{0}^{2}}{a x_{0}^{2}}-1\right)=-\frac{b y_{0}^{2}}{a x_{0}^{2}}<0,
$$

矛盾! 若 $v \leq 0$, 则 $y \leq \frac{y_{0}}{x_{0}} x$, 于是

矛盾!

$$
1=a x^{2}-b y^{2} \geq a x^{2}-b\left(\frac{y_{0}}{x_{0}} x\right)^{2}=\frac{x^{2}}{x_{0}}\left(a x_{0}^{2}-b y_{0}^{2}\right)=\frac{x^{2}}{x_{0}^{2}}>1,
$$

因此总有 $u \geq 0, v \geq 0$. 故而通过对应关系 (3) 和 (5), 我们建立了方程 (2),(4) 在非负整数范围内的一一对应. 通过上述探索, 我们可以得出:

定理 1. 若方程 (2) 有解, 则它必有无穷多组解.

例 1 . 求 $3 x^{2}-2 y^{2}=1$ 的正整数解.

解 易知其基本解为 $x=1, y=1$. 作代换

$$
\left\{\begin{array}{l}
x=u+2 v \\
y=u+3 v
\end{array}\right.
$$

将原方程化为 $u^{2}-b v^{2}=1$, 其基本解为 $u=5, v=2$. 它的全部解由

$$
(5+2 \sqrt{6})^{n}=u+v \sqrt{6}, \quad n \in \mathbb{N}^{+}, u, v \in \mathbb{N}^{+}
$$

给出. 再由上述代换得到原方程全部正整数解.

再回到更一般的方程 $(1)$, 同样取特解 $\left(x_{0}, y_{0}\right)$ 满足 $a x_{0}^{2}-b_{0}^{2}=c$. 再令

$$
\left\{\begin{array}{l}
x=x_{0} u+b y_{0} v \\
y=y_{0} u+c x_{0} v
\end{array},\right.
$$

代入 (1) 得到 $u^{2}-a b v^{2}=1$. 常数 $c$ 被消去. 同样地, 通过 (3), 每一组 (4) 的解唯一确定一组 (1) 的解. 但是反解得

$$
\left\{\begin{array}{l}
u=\frac{1}{c}\left(a x_{0} x-b y_{0} y\right) \\
v=\frac{1}{c}\left(-y_{0} x+x_{0} y\right)
\end{array}\right.
$$

它不一定为整数, 这说明换元后不一定能求出 (1) 的全部解. 但证明了 (1) 有无穷多组解. 对特殊的 $c$, 我们有同余法.

例 2 . 求方程 $5 x^{2}-3 y^{2}=2$ 的正整数解.

解 易知其基本解为 $x=1, y=1$. 作代换

$$
\left\{\begin{array}{l}
x=u+3 v \\
y=u+5 v
\end{array}\right.
$$

方程化为 $u^{2}-15 v^{2}=1$. 它的基本解为 $u=4, v=1$. 又

$$
\left\{\begin{array}{l}
u=\frac{1}{2}(5 x-3 y) \\
v=\frac{1}{2}(-x+y)
\end{array}\right.
$$

注意到 $5 x^{2}-3 y^{2}=2$ 的解 $x, y$ 必同奇偶, 从而 $u, v$ 也为正整数, 故两方程解构成一一对应 (即同解). $u, v$ 由 $(4+\sqrt{15})^{n}=u+\sqrt{15} v$ 给出, 便得到全部解.

II. $a x^{2}-b y^{2}=1$ 与 $u^{2}-a b v^{2}=1$ 的深刻联系 $((a, b)=1$, 且 $a b$不为完全平方数).

在 I 中, 我们讨论了 (1), (2) 的化归问题. 但是在求解过程中, 先看出了 (1)的基本解, 换元后又要算 (2) 的基本解. 而 (1), (2) 本为同解方程, 他们的联系体现在基本解得联系上, 能否用 (1) 的基本解来表示 (2) 的基本解呢? 我们来逐步引出欲求结论.

引理 1. (1) 的全部正整数解与 (2) 的全部非负正整数解构成了一一对应.

引理 2. 设 (1) 的全部正整数解构成集合 $A=\left\{(x, y) \mid a x^{2}-b y^{2}=1, x, y \in\right.$ $\left.\mathbb{N}^{+}\right\}, B=\left\{(u, v) \mid u^{2}-a b v^{2}=1, u, v \in \mathbb{N}\right\}$. 设 $A$ 中元素按 $\sqrt{a} x+\sqrt{b} y$ 从小到大排为 $a_{1}, a_{2}, \cdots, B$ 中元素按 $u+\sqrt{a b} v$ 从小到大排为 $b_{1}, b_{2}, \cdots$. 则在 I 中 (3) 和 (5) 关系式下, 有 $a_{1} \leftrightarrow b_{1}, a_{2} \leftrightarrow b_{2}, \cdots$.

证明 若设 $b_{i}$ 对应 $a_{i^{\prime}}, b_{j}$ 对应 $b_{j^{\prime}}$, 其中 $1 \leq i<j$. 由 (3) 可以看出, 必有 $i^{\prime}<j^{\prime}$. 故这个映射具有单调增性, 证毕.
引理 3. 设 $x_{1}, x_{2}, y_{1}, y_{2} \in \mathbb{Z}, u_{1}, u_{2}, u_{3}, v_{1}, v_{2}, v_{3} \in \mathbb{Z} . a, b \in \mathbb{N}^{+}$且不为完全平方数. 若设

$$
\begin{aligned}
\left(x_{1} \sqrt{a}+y_{1} \sqrt{b}\right)\left(x_{2} \sqrt{a}+y_{2} \sqrt{b}\right) & =u_{1}+v_{1} \sqrt{a b} \\
\left(x_{1} \sqrt{a}+y_{1} \sqrt{b}\right)\left(x_{2}+y_{2} \sqrt{a b}\right) & =u_{2} \sqrt{a}+v_{2} \sqrt{b} \\
\left(x_{1}+y_{1} \sqrt{a b}\right)\left(x_{2}+y_{2} \sqrt{a b}\right) & =u_{3}+v_{3} \sqrt{a b}
\end{aligned}
$$

则

$$
\begin{aligned}
\left(x_{1} \sqrt{a}-y_{1} \sqrt{b}\right)\left(x_{2} \sqrt{a}-y_{2} \sqrt{b}\right) & =u_{1}-v_{1} \sqrt{a b} \\
\left(x_{1} \sqrt{a}-y_{1} \sqrt{b}\right)\left(x_{2}-y_{2} \sqrt{a b}\right) & =u_{2} \sqrt{a}+v_{2} \sqrt{b} \\
\left(x_{1}-y_{1} \sqrt{a b}\right)\left(x_{2}-y_{2} \sqrt{a b}\right) & =u_{3}-v_{3} \sqrt{a b} .
\end{aligned}
$$

证明 逐个验证即可.

由引理 3, 易得以下结果.

推论 1 .

$$
\begin{aligned}
\overline{(x \sqrt{a}+y \sqrt{b})^{2 n+1}} & =(\overline{x \sqrt{a}+y \sqrt{b}})^{2 n+1}=(x \sqrt{a}-y \sqrt{b})^{2 n+1}, \\
\overline{(x+y \sqrt{a b})^{n}} & =(\overline{x+y \sqrt{a b}})^{n}=(x-y \sqrt{a b})^{n}, \\
\overline{\left(x_{1}+y_{1} \sqrt{a b}\right)^{n}\left(x_{2} \sqrt{a}+y_{2} \sqrt{b}\right)^{2 m+1}} & =\left(\overline{x_{1}+y_{1} \sqrt{a b}}\right)^{n}\left(\overline{x_{2} \sqrt{a}+y_{2} \sqrt{b}}\right)^{2 m+1} \\
& =\left(x_{1}-y_{1} \sqrt{a b}\right)^{n}\left(x_{2} \sqrt{a}-y_{2} \sqrt{b}\right)^{2 m+1} .
\end{aligned}
$$

引理 4. 设 $\left(x_{0}, y_{0}\right)$ 是 $a x^{2}-b y^{2}=1$ 的基本解, 则它的全部正整数解由 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x+\sqrt{b} y\left(x, y \in \mathbb{N}^{+}, k \in \mathbb{N}^{+}\right)$给出.

证明 1. 设 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x+\sqrt{b} y\left(x, y \in \mathbb{N}^{+}, k \in \mathbb{N}^{+}\right)$, 由推论知 $\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x-\sqrt{b} y$, 则有 $a x^{2}-b y^{2}=\left(a x_{0}^{2}-b y_{0}^{2}\right)^{2 k-1}=1$. 故 $(x, y)$ 确为 $a x^{2}-b y^{2}=1$ 的一组解.

2. 设 $(x, y)$ 满足 $a x^{2}-b y^{2}=1$. 下面证明存在 $k \in \mathbb{N}^{+}$, 使

$$
\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x-\sqrt{b} y .
$$

显然, 对任意 $k \in \mathbb{N}^{+}$, 由根式相等的充要条件, $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k} \neq \sqrt{a} x-\sqrt{b} y$.若不存在 $k \in \mathbb{N}^{+}$, 使 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x-\sqrt{b} y$. 由于 $\sqrt{a} x+\sqrt{b} y>$ $\sqrt{a} x_{0}+\sqrt{b} y_{0}$, 设 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{n}<\sqrt{a} x+\sqrt{b} y<\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{n+1}$.

(1) 若 $n$ 为偶数, 设 $n=2 l$, 即 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 l}<\sqrt{a} x+\sqrt{b} y<\left(\sqrt{a} x_{0}+\right.$ $\left.\sqrt{b} y_{0}\right)^{2 l+1}$, 则 $1<(\sqrt{a} x+\sqrt{b} y)\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 l}<\sqrt{a} x_{0}+\sqrt{b} y_{0}$. 注意到 $(\sqrt{a} x+$
$\sqrt{b} y)\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 l}$ 次数为奇数次, 可设它展开式为 $u \sqrt{a}+v \sqrt{b}(u, v \in \mathbb{Z})$. 由推论知 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 l}=u \sqrt{a}-v \sqrt{b}$, 故

$$
u^{2} a-v^{2} b=\left(a x^{2}-b y^{2}\right)\left(a x_{0}^{2}-b y_{0}^{2}\right)^{2 l}=1 .
$$

从而, $u, v$ 是 $a x^{2}-b y^{2}=1$ 的一组整数解. 又知

$$
1<u \sqrt{a}-v \sqrt{b}<\sqrt{a} x_{0}+\sqrt{b} y_{0}, 0<u \sqrt{a}-v \sqrt{b}=\frac{1}{u \sqrt{a}+v \sqrt{b}}<1,
$$

两式相加得 $u \sqrt{a}>1$, 从而 $u>o$. 两式相减得 $v \sqrt{b}>1-1=0$, 即 $v>0$. 故 $(u, v)$ 是一组正整数解, 而 $u \sqrt{a}+v \sqrt{b}<\sqrt{a} x_{0}+\sqrt{b} y_{0}$ 与 $\left(x_{0}, y_{0}\right)$ 为最小解矛盾!

(2) 若 $n$ 为奇数, 设 $n=2 l-1$, 即 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 l-1}<\sqrt{a} x+\sqrt{b} y<$ $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 l}$, 从而

$$
\sqrt{a} x_{0}-\sqrt{b} y_{0}<(\sqrt{a} x+\sqrt{b} y)\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 l}<1 .
$$

记 $(\sqrt{a} x+\sqrt{b} y)\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 l}=u \sqrt{a}-v \sqrt{b}(u, v \in \mathbb{Z})$. 由推论得 $(\sqrt{a} x-$ $\sqrt{b} y)\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 l}=u \sqrt{a}+v \sqrt{b}$, 故

$$
u^{2} a-v^{2} b=\left(a x^{2}-b y^{2}\right)\left(a x_{0}^{2}-b y_{0}^{2}\right)^{2 l}=1 .
$$

因此 $(u, v)$ 是满足 $a x^{2}-b y^{2}=1$ 的一组整数解. 又有

$0<\sqrt{a} x_{0}-\sqrt{b} y_{0}<u \sqrt{a}-v \sqrt{b}<1,1<u \sqrt{a}+v \sqrt{b}<\sqrt{a} x_{0}-\sqrt{b} y_{0}$.

同样地, 两式相加减得 $u, v>0$. 故 $(u, v)$ 是一组正整数解, $u \sqrt{a}+v \sqrt{b}<$ $\sqrt{a} x_{0}+\sqrt{b} y_{0}$ 与 $\left(x_{0}, y_{0}\right)$ 为最小解矛盾!

综上, 任一组满足 $a x^{2}-b y^{2}=1$ 的正整数解必能表示成 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=$ $\sqrt{a} x+\sqrt{b} y$ 的形式, 从而式 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x+\sqrt{b} y$ 给出方程 $a x^{2}-b y^{2}=$ 1 的全部正整数解. 证毕.

引理 4 十分关键, 它使我们直接得到 $a x^{2}-b y^{2}=1$ 的全部解. 再通过与 $u^{2}-a b v^{2}=1$ 的联系, 得到如下定理.

定理 2. 设 $\left(x_{0}, y_{0}\right)$ 是 $a x^{2}-b y^{2}=1$ 的基本解, 则 $\left(a x_{0}^{2}+b y_{0}^{2}, 2 x_{0} y_{0}\right)$ 为 $u^{2}-a b v^{2}=1$ 的基本解.

证明 注意到 $\sqrt{a} x_{0}+\sqrt{b} y_{0}>1$, 故 $\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}=\sqrt{a} x+\sqrt{b} y$ 中得到的 $x, y$ 是随 $k$ 递增的. 由引理 2 , 令 $k=1$, 得 $a_{1}=\left(x_{0}, y_{0}\right)$; 令 $k=2$, 得 $a_{2}=\left(a x_{0}^{3}+3 x_{0} y_{0}^{2} b, b y_{0}^{3}+3 x_{0}^{2} y_{0} a\right)$. 由 (3), (5) 关系式, 分别解得 $b_{1}=(1,0)$ (舍去), $b_{2}=\left(a x_{0}^{2}+b y_{0}^{2}, 2 x_{0} y_{0}\right)$. 因为我们规定基本解为正整数解, 故方程 $u^{2}-a b v^{2}=1$的基本解为 $u=a x_{0}^{2}+b y_{0}^{2}, v=2 x_{0} y_{0}$. 证毕.
定理 3 设展开式

$$
\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{n}=\left\{\begin{array}{cc}
\sqrt{a} x+\sqrt{b} y & n \text { 为正奇数, } \\
x+\sqrt{a b} y & n \text { 为正偶数. }
\end{array}\right.
$$

则当 $n$ 取全体正奇数时, $(x, y)$ 为 $a x^{2}-b y^{2}=1$ 的全部正整数解. 当 $n$ 取全体正偶数时, $(x, y)$ 为 $u^{2}-a b v^{2}=1$ 的全部正整数解.

证明 当 $n$ 取全体正奇数时, 由引理 4 知结论成立. 当 $n$ 取全体正偶数时,设 $n=2 k$, 则

$$
\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k}=\left(\left(a x_{0}^{2}+b y_{0}^{2}\right)+2 x_{0} y_{0} \sqrt{a b}\right)^{k}=x+\sqrt{a b} y .
$$

而 $x=a x_{0}^{2}+b y_{0}^{2}, y=2 x_{0} y_{0}$ 是 $u^{2}-a b v^{2}=1$ 的基本解, 故上式给出它的全部解,证毕.

利用定理 3 , 我们可以马上写出 $x, y, u, v$ 的显示表达.

满足 $a x^{2}-b y^{2}=1$ 的正整数解 $(x, y)$ :

$$
\begin{aligned}
& x=\frac{1}{2 \sqrt{a}}\left(\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}+\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 k-1}\right), \\
& y=\frac{1}{2 \sqrt{b}}\left(\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k-1}-\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 k-1}\right) .
\end{aligned}
$$

满足 $u^{2}-a b v^{2}=1$ 的正整数解 $(u, v)$ :

$$
\begin{aligned}
& u=\frac{1}{2}\left(\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k}+\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 k}\right), \\
& v=\frac{1}{2 \sqrt{a b}}\left(\left(\sqrt{a} x_{0}+\sqrt{b} y_{0}\right)^{2 k}-\left(\sqrt{a} x_{0}-\sqrt{b} y_{0}\right)^{2 k}\right) .
\end{aligned}
$$

利用上述定理 2 和定理 3 , 我们可以简化求基本解的计算.

例 3. 求佩尔方程 $x^{2}-55 y^{2}=1$ 的基本解.

解 先考虑 $5 u^{2}-11 v^{2}=1$ 的基本解, 易知, $u=3, v=2$ 是它的基本解. 由定理 2 , 知 $x=5 \times 3^{2}+11 \times 2^{2}=89, y=2 \times 3 \times 2=12$ 是 $x^{2}-55 y^{2}=1$ 的基本解.

例 4. 求方程 $a x^{2}-(a+2) y^{2}=1$ 及 $(a+2) x^{2}-a y^{2}=1$ 的整数解. 其中 $a>1, a \in \mathbb{N}^{+}$, 且 $a, a+2$ 不为完全平方数.

解 上述方程均无解, 若有解 $\left(x_{0}, y_{0}\right)$, 取它基本解, 则方程 $u^{2}-a(a+2) v^{2}=1$有基本解 $v=2 x_{0} y_{0}$. 而显然它的基本解为 $u=a+1, v=1$, 奇偶性不同, 矛盾!故上述方程无解.
至此, 两个方程之间的联系已探索完毕. 需要注意的是, 方程 $u^{2}-a b v^{2}=1$由于 $a b$ 的分解方式不同, 可与多个一般型双曲方程联系, 我们还可取 $u^{2}-a b v^{2}=$ 1 的基本解 $\left(u_{0}, v_{0}\right)$, 通过令

$$
\left\{\begin{array}{l}
u_{0}=a x_{0}^{2}+b y_{0}^{2} \\
v_{0}=2 x_{0} y_{0}
\end{array}\right.
$$

来判定 $a x^{2}-b y^{2}=1$ 是否有解. 这样, 我们将检验双曲型不定方程化为检验椭圆型方程, 验证在有限次内即可结束.

最基本地, 还是要找 (至少一组) 基本解, 如何寻找基本解的一般形式仍是较难的问题.

致谢. 作者感谢䨉振华教授细心审阅本文并提出宝贵建议.

