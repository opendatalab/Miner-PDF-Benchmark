数学新星网 莫学生专栏

www.nsmath.cn/xszl

# 2019 年北大夏令营试题简析 

孙孟越 ${ }^{1}$ 唐龙天 ${ }^{2}$ 刘明扬 ${ }^{3}$ 甘润之 $^{4}$

(1. 清华大学, 100084;2. 成都七中嘉祥外国语学校, 610023;

3. 华南师范大学附属中学, 510630 ; 4. 华东师范大学第二附属中学, 201203)

炎热的八月, 北京大学举办了他的夏令营. 这里我们给出题目的解答以及一些简评.

北大的考试时间为 2019 年 8 月 5 日 $8: 00-12: 00$ 和 8 月 6 日 $8: 00-12: 00$.每天 4 个题. 解答人的姓名随解答给出.

## I. 试 题

1. 给定 $\triangle A E F$, 点 $B, D$ 分别在 $A E, A F$ 上. $B F, D E$ 交于点 $C, A C$ 与 $E F$不垂直. $A C, E F$ 交于点 $G . \triangle A E F$ 的内切圆 $\odot I$ 与边 $A E$ 切于点 $M$, 与边 $A F$切于点 $N . \triangle C E F$ 的内切圆 $\odot J$ 与边 $C E$ 切于点 $P$, 与边 $C F$ 切于点 $Q$. 取 $I J$中点 $S$. 设 $S$ 在 $A C$ 上投影为 $K$. 若 $M, N, P, Q$ 四点共圆, 求证: $I, K, J, G$ 四点共圆.
2. 给定奇素数 $p$. 定义 $f_{i}(n)$ 是满足 $a \equiv i b(\bmod p), 1 \leq a<b \leq n$ 的正整数对 $(a, b)$ 的对数. 对正整数 $k$, 求 $\max _{0 \leq i \leq p-1} f_{i}(k p)-\min _{0 \leq i \leq p-1} f_{i}(k p)$ 的值.
3. 对一条直线 $l$, 若其经过无穷个整点, 则称之为 好直线. 对平面上所有整点染色, 满足对任意平行于坐标轴的好直线 $l, l$ 上整点具有无穷多种颜色. 问:是否对任意这样的染色方式, 一定存在一条不平行于坐标轴的好直线, 其上整点具有无穷多种颜色?
4. 求证: 对任意 $n$ 次实系数多项式 $f(x)$, 总存在 $n$ 次实系数多项式 $g(x)$ 满足 $|g(z)|^{2}=|f(z)|^{2}+1$ 对所有单位圆上的复数 $z$ 成立.
5. 给定四边形 $A B C D, A D$ 延长线和 $B C$ 延长线交于点 $E, B A$ 延长线和 $C D$ 延长线交于点 $F$. 平面上的点 $P$ 满足 $P A \cdot P C=P B \cdot P D=P E \cdot P F$. 问:
这样的点 $P$ 是否一定存在? 若存在这样的 $P$, 是否唯一? 证明你的结论.
6. 设 $a_{1}, a_{2}, \cdots, a_{n}>0$, 定义

$$
\sigma\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\min \left\{\left|\sum_{k=1}^{n} e_{k} a_{k}\right|: e_{k}=1 \text { 或 }-1\right\} .
$$

求最小的正实数 $\lambda$, 使得

$$
\sigma\left(a_{1}, a_{2}, \cdots, a_{n}\right)\left(\sum_{k=1}^{n} a_{k}\right) \leq \lambda \sum_{k=1}^{n} a_{k}^{2}
$$

对所有正数 $a_{1}, a_{2}, \ldots, a_{n}$ 成立.

7. 给定正整数 $a \equiv b \equiv 1(\bmod 3)$. 求证: 存在无穷多个最终周期的素数列 $\left\{p_{n}\right\}$, 满足 $p_{n+1} \mid p_{n}^{2}+a p_{n}+b$ 对所有正整数 $n$ 成立.
8. 给定正整数 $n, k, n \geq 2$. 给定一个标号为 $1,2, \ldots, n$ 的树 $T$. 我们对正整数序列 $\left(a_{1}, a_{2}, \ldots, a_{k}\right)$ 进行操作, 这里的 $1 \leq a_{i} \leq n$. 选定一个 $1 \leq i \leq k-1$, 若 $a_{i}$ 和 $a_{i+1}$ 在树中有边相连, 则可以交换 $a_{i}, a_{i+1}$ 的位置. 若一个序列可以通过有限次交换变成另一个, 则称这两个序列等价. 记 $f(T)$ 是序列的等价类的个数,求 $f(T)$ 的所有可能值.

## II . 解答与评注

1. 给定 $\triangle A E F$, 点 $B, D$ 分别在 $A E, A F$ 上. $B F, D E$ 交于点 $C, A C$ 与 $E F$不垂直. $A C, E F$ 交于点 $G . \triangle A E F$ 的内切圆 $\odot I$ 与边 $A E$ 切于点 $M$, 与边 $A F$切于点 $N . \triangle C E F$ 的内切圆 $\odot J$ 与边 $C E$ 切于点 $P$, 与边 $C F$ 切于点 $Q$. 取 $I J$中点 $S$. 设 $S$ 在 $A C$ 上投影为 $K$. 若 $M, N, P, Q$ 四点共圆, 求证: $I, K, J, G$ 四点共圆。


证明 (唐龙天) 首先证明一个引理:

引理给定 $\triangle X Y Z$ 与 $\triangle X_{1} Y_{1} Z_{1}$, 满足 $X Y+X_{1} Y_{1}=X Z+X_{1} Z_{1}$, 设 $\angle Y X Z$角平分线与 $Y Z$ 交于点 $W$, 类似定义 $W_{1}$. 若 $\angle X W Z=\angle X_{1} W_{1} Z_{1}$, 则有 $X Y=$ $X Z, X_{1} Y_{1}=X_{1} Z_{1}$.

证明 注意到

$$
\begin{aligned}
X Y \gtreqless X Z & \Leftrightarrow \angle X Z Y \gtreqless \angle X Y Z \\
& \Leftrightarrow \angle Y X W+\angle Y W X \gtreqless \angle Z X W+\angle X W Z \\
& \Leftrightarrow \angle Y W X \gtreqless \angle X W Z,
\end{aligned}
$$

这里的 $\gtreqless$ 可以同时取 $>,=,<$ 中的任意一个.

同理, $\angle Y_{1} W_{1} X_{1} \gtreqless \angle X_{1} W_{1} Z_{1} \Leftrightarrow X_{1} Y_{1} \gtreqless X_{1} Z_{1}$. 由 $X Y+X_{1} Y_{1}=X Z+X_{1} Z_{1}$表明 $X Y=X Z, X_{1} Y_{1}=X_{1} Z_{1}$, 引理得证.

回到原题. 由 $M, N, Q, P$ 四点共圆

$$
\begin{aligned}
& \Rightarrow \angle A M N+\angle E M P=\angle C Q P+\angle B Q N, \\
& \Rightarrow 90^{\circ}-\frac{1}{2} \angle M A N+\angle E M P=90^{\circ}-\frac{1}{2} \angle P C Q+\angle B Q N, \\
& \Rightarrow \angle B Q N-\angle E M P=\frac{1}{2}(\angle P C Q-\angle M A N)=\frac{1}{2}(\angle M E P+\angle Q F N), \\
& \Rightarrow \angle E U P=\angle F V Q,
\end{aligned}
$$

其中, $U$ 是 $\angle M E P$ 角平分线与 $M P$ 的交点, $V$ 是 $\angle N F Q$ 角平分线和 $N Q$ 的交点.

而 $E P+F Q=E F=E M+F N$, 对 $\triangle E M P, \triangle F N Q$ 用引理知 $E P=$ $E M, F Q=F N$. 故知 $\odot I, \odot J$ 与 $E F$ 切于同一点 $T$, 则有 $C E+E F-C F=$ $2 E T=E A+E F-F A$.

故凹四边形 $A E C F$ 对边之和相等, 存在一个内切圆. 而这等价于四边形 $A B C D$ 有内切圆 $\omega$. 由于 $A C$ 与 $E F$ 不垂直, 我们可设 $I J$ 与 $A G$ 交于一点 $R$.

对 $\odot I, \odot J$, 圆 $\omega$ 用 Monge 定理, 知 $\odot I$ 与 $\odot J$ 内位似中心在直线 $A C$ 上. 故 $R$ 为 $\odot I$ 与 $\odot J$ 内位似中心, 而 $\odot I$ 与 $\odot J$ 切与点 $T$. 则 $T$ 为 $\odot I$ 与 $\odot J$ 外位似中心. 故 $I, R, J, T$ 构成调和点列(位似中心分圆心比都为两圆半径比).

结合 $S$ 为 $I J$ 中点 $\Rightarrow \overline{R S} \cdot \overline{R T}=\overline{R I} \cdot \overline{R J}$. 而 $\angle S K R=\angle G T R=90^{\circ}$, 故 $S, K, T, G$ 四点共圆 $\Rightarrow \overline{R S} \cdot \overline{R T}=\overline{R K} \cdot \overline{R G} \Rightarrow \overline{R K} \cdot \overline{R G}=\overline{R I} \cdot \overline{R J} \Rightarrow I, J, K, G$四点共圆.

评注 本题难度较大, 题目涉及两个重要的几何构型: 前半部分主要在证明
$A, B, C, D$ 有内切圆, 而这个几何构型也在 2015 年 $\mathrm{CMO}$ 第二题之中出现. 后一半主要用到 Monge 定理与内外位似中心，而这个几何构型则是在 2008 年 IMO 第 6 题中出现.

这里用到的 Monge 定理: 对三圆 $\Gamma_{1}, \Gamma_{2}, \Gamma_{3}$, 有 $\Gamma_{1}, \Gamma_{2}$ 的内位似中心, $\Gamma_{2}, \Gamma_{3}$ 的内位似中心, $\Gamma_{1}, \Gamma_{3}$ 的外位似中心三点共线. 证明由 Menelaus 定理容易得到.

2. 给定奇素数 $p$. 定义 $f_{i}(n)$ 是满足 $a \equiv i b(\bmod p), 1 \leq a<b \leq n$ 的正整数对 $(a, b)$ 的对数. 对正整数 $k$, 求 $\max _{0 \leq i \leq p-1} f_{i}(k p)-\min _{0 \leq i \leq p-1} f_{i}(k p)$ 的值.

解 (刘明扬) 对 $\forall n \in \mathbb{N}$, 记 $\bar{n}$ 为 $n$ 模 $p$ 的最小正剩余, 记 $n$ 所在的模 $p$ 剩余类为 $A_{n}$.

对 $b \in A_{m}(1 \leq m \leq p)$, 必有 $a \in A_{\overline{i m}}$. 设 $a=k_{1} p+\overline{i m}, b=k_{2} p+m$, 则若 $\overline{i m} \geq m$, 则 $\left(k_{1}, k_{2}\right)$ 满足要求当且仅当 $k_{1}<k_{2}$; 若 $\overline{i m}<m$, 则 $\left(k_{1}, k_{2}\right)$ 满足要求当且仅当 $k_{1} \leq k_{2}$.

而我们有: 满足 $k_{1}<k_{2}$ 的 $\left(k_{1}, k_{2}\right)$ 有 $\left(\begin{array}{l}k \\ 2\end{array}\right)$ 组, 满足 $k_{1} \leq k_{2}$ 的 $\left(k_{1}, k_{2}\right)$ 有 $\left(\begin{array}{l}k \\ 2\end{array}\right)+k$ 组. 因此

$$
f_{i}(k p)=\left(\left(\begin{array}{l}
k \\
2
\end{array}\right)+k\right) f_{i}(p)+\left(\begin{array}{l}
k \\
2
\end{array}\right)\left(p-f_{i}(p)\right)=k f_{i}(p)+p\left(\begin{array}{l}
k \\
2
\end{array}\right) .
$$

故

$$
f_{i_{1}}(k p)-f_{i_{2}}(k p)=k\left(f_{i_{1}}(p)-f_{i_{2}}(p)\right) .
$$

因此只需考虑 $f_{i}(p)$ 的最大和最小值.

注意到 $f_{1}(p)=0$, 故 $f_{i}(p)$ 最小值为 0 .

又 $\overline{i p}=p$, 而对 $1 \leq x \leq p-1, \overline{i x}+\overline{i(p-x)}=p$. 故 $\overline{i x}<x$ 和 $\overline{i(p-x)}<p-x$至多有一个成立. 这推出 $f_{i}(p) \leq \frac{p-1}{2}$. 由于 $p$ 是奇数, 所以 $f_{p-1}(p)=\frac{p-1}{2}$, 故 $f_{i}(p)$ 最大值为 $\frac{p-1}{2}$.

当 $k=1$ 时, 所求值为

$$
\max _{0 \leq i \leq p-1} f_{i}(p)-\min _{0 \leq i \leq p-1} f_{i}(p)=\frac{p-1}{2}
$$

故

$$
\max _{0 \leq i \leq p-1} f_{i}(k p)-\min _{0 \leq i \leq p-1} f_{i}(k p)=\frac{k(p-1)}{2}
$$

评注 首先可以把 $k p$ 个连续整数变成 $k$ 段, 每段为 $p$ 个整数. 可以看出要分 $a, b$ 是不是在同一段进行计数. 之后发现, 同一段的时候是要具体处理的. 进
一步, 用配对的方法可以证明 $f_{i}(p)$ 对 $i \not \equiv 0,1(\bmod p)$ 都有 $f_{i}(p)=\frac{p-1}{2}$. 整个题思路自然, 属于一个中等偏易的题.

3. 对一条直线 $l$, 若其经过无穷个整点, 则称之为好直线. 对平面上所有整点染色, 满足对任意平行于坐标轴的好直线 $l, l$ 上整点具有无穷多种颜色. 问:是否对任意这样的染色方式, 一定存在一条不平行于坐标轴的好直线, 其上整点具有无穷多种颜色?

解 答案是否定的, 即存在一种染色方式, 对任意不平行于坐标轴的好直线,其上都只有有限种颜色.

设 $T=\left\{(x, y)|x, y \in \mathbb{Z}| y \mid, \geq x^{2}\right.$ 或 $\left.|x| \geq y^{2}\right\}$. 对于 $T$ 中整点, 将其染成两两不同的颜色. 不在 $T$ 中的整点, 染成同一个颜色.

可以发现对任意平行于坐标轴的好直线, 其上只有有限个点不在 $T$ 中, 故其上整点有无穷个颜色. 对任意不平行于坐标轴的直线 $l: y=k x+b(k \neq 0)$, $l \cap T$ 中的点 $(x, y)$ 一定满足

$$
k x+b \geq x^{2},-(k x+b) \geq x^{2}, x \geq(k x+b)^{2},-x \geq(k x+b)^{2}
$$

这四个不等式之一. 由于 $k \neq 0$, 故这四个关于 $x$ 的不等式, 每一个的解集要么是有限闭区间(左右端点允许重合), 要么是空集. 故存在一个正数 $M$, 只要 $|x|>M$, 就有 $(x, k x+b) \notin l \cap T$. 由于整数的离散性, 知 $l \cap T$ 交集是有限集.所以 $l$ 上整点只有有限种颜色.

评注 这个题也可以把整点改成有理数点或者所有点, 只要把实数平面按照 $(\lfloor x\rfloor,\lfloor y\rfloor)$ 的值分成不同的方格即可.

此外, 这个题本质就是要构造这个 $T$, 任何平行于坐标轴的好直线和 $T$ 有无穷个交点, 任何不平行于坐标轴的直线和 $T$ 有有限个交点. 这也可以通过归纳构造完成。

有同学指出, 2013 年莫斯科数学奥林匹克中的一个题, 就是要求构造这个 $T$. 从这个意义上来说, 这个题“撞题”了. 我们这里 $T$ 的构造引自 2013 年题的标准答案.

4. 求证: 对任意 $n$ 次实系数多项式 $f(x)$, 总存在 $n$ 次实系数多项式 $g(x)$ 满足 $|g(z)|^{2}=|f(z)|^{2}+1$ 对所有单位圆上的复数 $z$ 成立.

## 证明 (孙孟越)

我们注意到一个关键的事实: $|z|=1 \Rightarrow \bar{z}=\frac{|z|^{2}}{z}=\frac{1}{z}$.
又由于 $f$ 是实系数多项式, 故

也有

$$
|f(z)|^{2}=f(z) \overline{f(z)}=f(z) f(\bar{z})=f(z) f\left(\frac{1}{z}\right) .
$$

$$
|g(z)|^{2}=g(z) g\left(\frac{1}{z}\right)
$$

故只需证明, 存在 $n$ 次实系数多项式 $g(x)$, 满足对任意复数 $x \neq 0$, 有

$$
g(x) g\left(\frac{1}{x}\right)=f(x) f\left(\frac{1}{x}\right)+1 .
$$

我们首先证明 $f(0) \neq 0$ 的情形.

若 $f$ 是常数 $a$, 则取 $g(x)=\sqrt{a^{2}+1} \cdot x^{n}$ 即可使 (1) 成立, 下设 $f$ 不是常数.

我们将 $f(x) f\left(\frac{1}{x}\right)$ 展开, 设实数 $a_{n}, a_{n-1}, \ldots, a_{-n}$ 满足

$f(x) f\left(\frac{1}{x}\right)+1=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{0}+\cdots+a_{-(n-1)} x^{-(n-1)}+a_{-n} x^{-n}$.

由于 $f(x)$ 的首项系数和常数项均非零, 可得 $a_{n} \neq 0$. 由于将 $x$ 换为 $\frac{1}{x}$, 左边不变, 故右边也不变, 故 $a_{m}=a_{-m}, m=1,2, \ldots, n$. 所以可以写为

$$
f(x) f\left(\frac{1}{x}\right)+1=a_{n}\left(x^{n}+x^{-n}\right)+a_{n-1}\left(x^{n-1}+x^{-(n-1)}\right)+\cdots+a_{0} .
$$

不难发现, 对正整数 $m$, 存在实系数多项式 $p_{m}(x)$ 满足 $p_{m}\left(x+x^{-1}\right)=x^{m}+x^{-m}$ 对任意复数 $x$ 成立 (归纳法可以证明).

故有 $f(x) f\left(\frac{1}{x}\right)+1$ 可以写为关于 $x+x^{-1}$ 的实系数多项式. 换言之, 存在实数 $b_{0}, b_{1}, b_{2}, \ldots, b_{n}$ 满足

$$
f(x) f\left(\frac{1}{x}\right)+1=b_{n}\left(x+x^{-1}\right)^{n}+b_{n-1}\left(x+x^{-1}\right)^{n-1}+\cdots+b_{0} .
$$

比较 $x^{n}$ 系数得到 $b_{n}=a_{n} \neq 0$. 记 $q(x)=b_{n} x^{n}+b_{n-1} x^{n-1}+\cdots+b_{0}$, 则 $q(x)$ 可以写为 $q(x)=b_{n}\left(x-\alpha_{1}\right)\left(x-\alpha_{2}\right) \cdots\left(x-\alpha_{n}\right)$, 这里的 $\alpha_{1}, \ldots, \alpha_{n}$ 是 $q(x)=0$ 的全体复数根. 所以

$$
f(x) f\left(\frac{1}{x}\right)+1=b_{n}\left(x+x^{-1}-\alpha_{1}\right)\left(x+x^{-1}-\alpha_{2}\right) \cdots\left(x+x^{-1}-\alpha_{n}\right) .
$$

下面我们证明: 对 $k=1,2, \ldots, n, \alpha_{k}$ 满足要么 $\alpha_{k}$ 不是实数, 要么 $\alpha_{k}$ 是实数且 $\left|\alpha_{k}\right|>2$.

若不然, 设 $-2 \leq \alpha_{k} \leq 2$, 则存在实数 $\theta$ 满足 $\alpha_{k}=2 \cos \theta$. 我们在 (2) 中取 $x=\cos \theta+i \sin \theta$. 这里的 $i$ 是虚数单位. 则有 $x+x^{-1}-\alpha_{k}=0$, 所以 (2) 右边是 0 , 但 (2) 左边 $=f(\cos \theta+i \sin \theta) f(\cos \theta-i \sin \theta)+1=|f(\cos \theta+i \sin \theta)|^{2}+1>0$.此为矛盾.

由于 $q(x)$ 是实系数多项式, 故复数根必然成对出现. 我们设 $q(x)$ 的实根为 $t_{1}, t_{2}, \ldots, t_{n-2 s}$, 共轭复数根为 $w_{1}, w_{2}, \ldots, w_{s}, \overline{w_{1}}, \overline{w_{2}}, \ldots, \overline{w_{s}}$.
对 $1 \leq k \leq n-2 s$, 定义 $\beta_{k}=\frac{t_{k}+\sqrt{t_{k}^{2}-4}}{2} \in \mathbb{R}$. 这里用到了 $\left|t_{k}\right|>2$. 则 $\beta_{k}+\beta_{k}^{-1}=t_{k}$.

对 $k=1,2, \ldots, s$, 定义 $\beta_{n-2 s+k}=\frac{w_{k}+\sqrt{w_{k}^{2}-4}}{2} \in \mathbb{C} \backslash \mathbb{R}, \beta_{n-s+k}=\overline{\beta_{n-2 s+k}}$. 其中,求平方根可以从两个平方根中任取一个, 则有

$$
\beta_{n-2 s+k}+\beta_{n-2 s+k}^{-1}=w_{k}, \quad \beta_{n-s+k}+\beta_{n-s+k}^{-1}=\overline{w_{k}} .
$$

待定实数 $C$, 我们取 $g(x)=C\left(x-\beta_{1}\right)\left(x-\beta_{2}\right) \cdots\left(x-\beta_{n}\right)$. 由于 $\beta_{1}, \beta_{2}, \cdots, \beta_{n}$ 中共轭复数也是成对出现的, 故 $g$ 是实系数多项式. 而

$$
\begin{aligned}
g(x) g\left(\frac{1}{x}\right) & =\left(\prod_{k=1}^{n}\left(-\beta_{k}\right)\right) C^{2} \prod_{k=1}^{n}\left(x+\frac{1}{x}-\beta_{k}-\beta_{k}^{-1}\right) \\
& =\left(\prod_{k=1}^{n}\left(-\beta_{k}\right)\right) C^{2} \prod_{k=1}^{n}\left(x+\frac{1}{x}-\alpha_{k}\right) \\
& =\left(\prod_{k=1}^{n}\left(-\beta_{k}\right)\right) \cdot \frac{C^{2}}{b_{n}} \cdot\left(f(x) f\left(\frac{1}{x}\right)+1\right) .
\end{aligned}
$$

我们取 $C^{2}=\frac{b_{n}}{\prod_{k=1}^{n}\left(-\beta_{k}\right)}$ 即可, 为此, 只要证明 $\prod_{k=1}^{n}\left(-\beta_{k}\right)$ 的符号与 $b_{n}$ 符号相同.

事实上, 共轭虚数根的乘积是正实数, 故 $\prod_{k=1}^{n}\left(-\beta_{k}\right)$ 的符号与 $\prod_{k=1}^{n-2 s}\left(-\beta_{k}\right)$ 符号相同, $\prod_{k=1}^{n}\left(-\alpha_{k}\right)$ 的符号与 $\prod_{k=1}^{n-2 s}\left(-t_{k}\right)$ 符号相同. 再注意 $\beta_{k}, t_{k}(1 \leq k \leq n-2 s)$ 的符号相同. 所以只要证明 $\prod_{k=1}^{n}\left(-\alpha_{k}\right)$ 与 $b_{n}$ 符号相同即可.

再次回到 $(2)$, 在 $(2)$ 中取 $x=i$, 得到

$$
b_{n} \prod_{k=1}^{n}\left(-\alpha_{k}\right)=f(i) f(-i)+1=|f(i)|^{2}+1>0 .
$$

故 $\prod_{k=1}^{n}\left(-\alpha_{k}\right)$ 与 $b_{n}$ 符号相同, 待定的实数 $C$ 存在, 此时命题成立.

对于 $f(0)=0$ 的 $f$. 设 $f(x)=x^{m} \tilde{f}(x), \tilde{f}(0) \neq 0$. 对 $\tilde{f}$ 用上述结论知, 存在 $n-m$ 次实系数多项式 $\tilde{g}(x)$ 使 (1) 成立. 我们取 $g(x)=x^{m} \cdot \tilde{g}(x)$ 即可使 (1) 成立, 且 $g$ 是 $n$ 次实系数多项式.

综上, 命题成立.

评注 第一步将之转化为证明 $f(x) f\left(\frac{1}{x}\right)+1=g(x) g\left(\frac{1}{x}\right)$. 之后, 我们分析左边这个 $f(x) f\left(\frac{1}{x}\right)+1=0$ 的根的位置, 这些根要么要么在实数轴上 $t$ 与 $\frac{1}{t}$ 成对出现, 要么满足 $z_{0}$ 和 $\frac{1}{z_{0}}, \overline{z_{0}}, \overline{\frac{1}{z_{0}}}$ 四者同时出现. 这恰恰是 $g$ 存在的条件, 我们就取 $g$ 的根为全体模长 $>1$ 的那些根即可. 然后去证明 $g(x) g\left(\frac{1}{x}\right)=f(x) f\left(\frac{1}{x}\right)+1$. 主要思路就是要考虑根的分布, 再稍加处理一些细节.

5. 给定四边形 $A B C D, A D$ 延长线和 $B C$ 延长线交于点 $E, B A$ 延长线和 $C D$ 延长线交于点 $F$. 平面上的点 $P$ 满足 $P A \cdot P C=P B \cdot P D=P E \cdot P F$. 问:这样的点 $P$ 是否一定存在? 若存在这样的 $P$, 是否唯一? 证明你的结论.

解 存在且唯一.

存在性: 取出完全四边形 $A B E C F D$ 的 Miquel 点 $T$. 则由 Miquel 点的性质知 $\angle T B E=\angle T F D, \angle T E B=\angle T D F \Rightarrow \triangle T E B \sim \triangle T D F \Rightarrow T E \cdot T F=$ $T D \cdot T B$. 并且有 $\angle B T D, \angle F T E$ 的内角平分线重合. 同理有 $T E \cdot T F=T A \cdot T C$,并且有 $\angle A T C, \angle F T E$ 的内角平分线重合, 故知 $T$ 点满足题目要求.



唯一性: 我们以 $T$ 点为原点建立复平面, 用大写字母对应的小写字母对应该点对应的复数.

由于 $\angle F T E, \angle A T C, \angle B T D$ 的内角平分线重合, 且

$$
T A \cdot T C=T B \cdot T D=T E \cdot T F
$$

知 $a \cdot c=b \cdot d=e \cdot f$, 我们可不妨设它们均等于 1 .

若存在不同于 $T$ 点的点 $P$ 满足要求, 由于 $p \neq 0$, 可以取 $m=\frac{1}{2}\left(p+\frac{1}{p}\right)$, $M$ 为复数 $m$ 对应的点, 由条件知

$$
|(p-a)(p-c)|=|(p-b)(p-d)|=|(p-e)(p-f)|,
$$

则有

$|(p-a)(p-c)|=|(p-b)(p-d)| \Longrightarrow\left|p^{2}-(a+c) p+1\right|=\left|p^{2}-(b+d) p+1\right|$.

这表明

$$
\left|m-\frac{a+c}{2}\right|=\left|\frac{p+\frac{1}{p}}{2}-\frac{a+c}{2}\right|=\left|\frac{p+\frac{1}{p}}{2}-\frac{b+d}{2}\right|=\left|m-\frac{b+d}{2}\right|,
$$

即 $M$ 点到 $A C$ 中点, $B D$ 中点距离相同.
同理即得 $M$ 点到 $A C$ 中点, $E F$ 中点的距离相同. 设 $A C$ 中点, $B D$ 中点, $E F$ 中点分别为 $X, Y, Z$. 故 $P$ 在 $X Y$ 中垂线上, 又在 $X Z$ 中垂线上.

但由 Newton 线定理知, $X, Y, Z$ 三点共线. 由于 $B E D F$ 不是平行四边形,所以 $Y, Z$ 不重合. 故 $X Y$ 中垂线和 $X Z$ 中垂线没有交点, 这与 $P$ 在这两条直线上相矛盾. 故原题中 $P$ 是存在且唯一的.

评注 这道题不是一个传统的几何题. 存在性比唯一性简单, 可以猜出 $P$ 同时是 $A B$ 到 $D C$ 的旋转位似中心, 也是 $B F$ 到 $D E$ 的旋转位似中心, 也是 $C F$到 $A E$ 的旋转位似中心, 那就猜到了是 Miquel 点. 唯一性的证明过程不容易,除了思路难以想到, 也有很多细节需要处理. 除了复数的证明, 也有通过三角计算的证明。这个题难度很大, 因为需要学生对 Miquel 点性质较为熟悉, 并且需要合适地选择唯一性的证法。这个题唯一性部分目前看来没有纯几何的证明，线路很窄, 没有看上去那么容易, 考生心态也容易受到影响.

6. 设 $a_{1}, a_{2}, \cdots, a_{n}>0$, 定义

$$
\sigma\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\min \left\{\left|\sum_{k=1}^{n} e_{k} a_{k}\right|: e_{k}=1 \text { 或 }-1\right\} \text {. }
$$

求最小的正实数 $\lambda$, 使得

$$
\sigma\left(a_{1}, a_{2}, \cdots, a_{n}\right)\left(\sum_{k=1}^{n} a_{k}\right) \leq \lambda \sum_{k=1}^{n} a_{k}^{2}
$$

对所有正数 $a_{1}, a_{2}, \ldots, a_{n}$ 成立.

## 解 (甘润知、孙孟越)

任取正数 $\varepsilon<\frac{1}{n}$. 取 $a_{1}=1, a_{2}=a_{3}=\cdots=a_{n}=\varepsilon$, 则

$$
\sigma\left(a_{1}, a_{2}, \ldots, a_{n}\right)=1-(n-1) \varepsilon .
$$

故有

$$
(1-(n-1) \varepsilon)(1+(n-1) \varepsilon) \leq \lambda\left(1+(n-1) \varepsilon^{2}\right) \Longleftrightarrow \lambda \geq 1-\frac{n(n-1) \varepsilon^{2}}{1+(n-1) \varepsilon^{2}} .
$$

令 $\varepsilon \rightarrow 0^{+}$知 $\lambda \geq 1$. 下面证明 $\lambda$ 最小值是 1 .

不妨假设 $a_{1} \geq a_{2} \geq a_{3} \geq \cdots \geq a_{n}>0$. 我们考虑一种选择 $e_{i}$ 的方法: 取 $e_{1}=1$. 设 $e_{1}, e_{2}, \ldots, e_{k}$ 已经构造好, 来构造 $e_{k+1}$. 若前 $k$ 项和 $S_{k}=\sum_{i=1}^{k} e_{i} a_{i} \geq 0$,那么取 $e_{k+1}=-1$. 反之, 若前 $k$ 项和 $S_{k}=\sum_{i=1}^{k} e_{i} a_{i}<0$, 那么取 $e_{k+1}=1$. 由 $\sigma\left(a_{1}, a_{2}, \ldots, a_{n}\right)$ 的定义知, $\sigma\left(a_{1}, a_{2}, \ldots, a_{n}\right) \leq\left|S_{n}\right|$.

若 $S_{n}=0$, 则 $\sigma\left(a_{1}, a_{2}, \ldots, a_{n}\right)=0$, 命题显然成立. 下设 $S_{n} \neq 0$. 补充定义
$S_{0}=0$.

由于 $S_{0}=0$, 故存在一个 $0 \leq i \leq n$ 满足 $S_{i} S_{n} \leq 0$, 我们取 $m$ 是满足 $S_{i} S_{n} \leq 0$ 的 $i$ 里最大的那个. 则由 $S_{n}^{2}>0$ 知 $0 \leq m<n$, 我们有

$$
\left|S_{m+1}-S_{m}\right|=a_{m+1}, S_{m} S_{m+1} \leq 0 \Rightarrow\left|S_{m+1}\right|+\left|S_{m}\right|=a_{m+1}
$$

故

$$
\left|S_{m+1}\right| \leq a_{m+1}
$$

并且对于 $m<i<n$, 由 $m$ 的最大性知 $S_{i} S_{n}>0, S_{i+1} S_{n}>0$, 知 $S_{i} S_{i+1}>0$. 由 $e_{i+1}$ 的选取规则知 $\left|S_{i+1}\right|=\left|S_{i}\right|-a_{i+1}$. 故

$$
\left|S_{n}\right|=\left|S_{m+1}\right|-\sum_{m+1<k \leq n} a_{k}
$$

这里, 若 $m+1 \geq n$, 则和式 $\sum_{m+1<k \leq n} a_{k}=0$. 所以

$$
\begin{aligned}
& \sigma\left(a_{1}, a_{2}, \ldots, a_{n}\right)\left(a_{1}+a_{2}+\cdots+a_{n}\right) \\
\leq & \left|S_{n}\right|\left(a_{1}+a_{2}+\cdots+a_{n}\right) \\
= & \left(\left|S_{m+1}\right|-\sum_{m+1<k \leq n} a_{k}\right)\left(a_{1}+a_{2}+\cdots+a_{n}\right) \\
\leq & \left(a_{m+1}-\sum_{m+1<k \leq n} a_{k}\right)\left(a_{1}+a_{2}+\cdots+a_{n}\right) \\
= & \left(a_{m+1}-\sum_{m+1<k \leq n} a_{k}\right)\left(\sum_{1 \leq k \leq m+1} a_{k}+\sum_{m+1<k \leq n} a_{k}\right) \\
= & a_{m+1}\left(\sum_{1 \leq k \leq m+1} a_{k}\right)-\left(\sum_{m+1<k \leq n} a_{k}\right)\left(\sum_{1 \leq k \leq m} a_{k}\right)-\left(\sum_{m+1<k \leq n} a_{k}\right)^{2} \\
\leq & a_{m+1}\left(a_{1}+a_{2}+\cdots+a_{m+1}\right) \\
\leq & a_{1}^{2}+a_{2}^{2}+\cdots+a_{m+1}^{2} \\
\leq & a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2} .
\end{aligned}
$$

故 $\lambda$ 最小值是 1 .

评注 这里我们采用了贪心算法来构造 $\sigma\left(a_{1}, a_{2}, \ldots, a_{n}\right)$. 也可以用归纳法来构造: 仍设 $a_{1} \geq a_{2} \geq \cdots \geq a_{n}>0$, 利用归纳假设可以构造出 $e_{1}, e_{2}, \ldots, e_{n-1}$, 再选取合适的 $e_{n}$ 即可. 实质上得到的构造和我们这里用贪心算法相同, 不过论证的部分可以利用归纳假设, 占得了一点便宜.

7. 给定正整数 $a \equiv b \equiv 1(\bmod 3)$. 求证: 存在无穷多个最终周期的素数列 $\left\{p_{n}\right\}$, 满足 $p_{n+1} \mid p_{n}^{2}+a p_{n}+b$ 对所有正整数 $n$ 成立.

证明 (孙孟越) 我们先证明, 任取 $p_{1}$ 是素数, 存在一个最终周期的素数列满足条件.

我们按照如下的方式构造. 假设 $p_{1}, p_{2}, \ldots, p_{m}$ 已经构造好, 来构造 $p_{m+1}$.

若 $p_{m}^{2}+a p_{m}+b$ 是 3 的倍数, 取 $p_{m+1}=3$.

若 $p_{m}^{2}+a p_{m}+b$ 不是 3 的倍数, 但有模 3 余 1 的素因子, 我们取 $p_{m+1}$ 是 $p_{m}^{2}+a p_{m}+b$ 的最小的模 3 余 1 的素因子.

若 $p_{m}^{2}+a p_{m}+b$ 不是 3 的倍数, 也没有模 3 余 1 的素因子, 我们取 $p_{m+1}$ 是 $p_{m}^{2}+a p_{m}+b$ 的最小的模 3 余 2 的素因子 (由于 $p_{m}^{2}+a p_{m}+b$ 是大于 1 的正整数, 必然存在素因子).

下面证明构造出的 $\left\{p_{n}\right\}$ 是最终周期的. 用反证法, 假设 $\left\{p_{n}\right\}$ 不是最终周期的, 我们证明如下关于 $\left\{p_{n}\right\}$ 的性质.

性质 1. 不存在正整数 $i<j$ 满足 $p_{i}=p_{j}$.

否则, 注意到 $p_{m+1}$ 可以由 $p_{m}$ 唯一确定, 归纳法不难证明 $p_{i+k}=p_{j+k}, k=$ $1,2, \ldots$ 即可. 故 $\left\{p_{n}\right\}$ 自第 $i$ 项起循环，以 $j-i$ 为一个周期.

此时 $\left\{p_{n}\right\}$ 是最终周期的, 与反证法假设矛盾.

性质 2. 不存在正整数 $i<j$ 满足 $p_{i}, p_{j}$ 都是模 3 余 1 的.

由于 $a \equiv b \equiv 1(\bmod 3)$, 则有 $p_{i}^{2}+a p_{i}+b \equiv 0(\bmod 3), p_{j}^{2}+a p_{j}+b \equiv 0$ $(\bmod 3)$. 故 $p_{i+1}=p_{j+1}=3$. 与性质 1 矛盾.

性质 3. 存在一个正整数 $T$, 满足对 $n \geq T, p_{n+1} \leq p_{n}+a+b$.

由性质 1,2 , 知除了至多两个 $p_{i}$, 其余 $p_{i}$ 都模 3 余 2 . 故存在正整数 $T$, 对任意 $n \geq T$, 有 $p_{n}$ 模 3 余 2 .

由我们的取法知, $p_{n}^{2}+a p_{n}+b$ 有且只有模 3 余 2 的素因子. 但我们有 $p_{n} \equiv 2$ $(\bmod 3)$, 那么就有 $p_{n}^{2}+a p_{n}+b \equiv 1(\bmod 3)$. 故 $p_{m}^{2}+a p_{m}+b$ 有偶数个模 3 余 2 的素因子, 故至少有两个模 3 余 2 的素因子. 由于 $p_{n+1}$ 为 $p_{n}^{2}+a p_{n}+b$ 的最小素因子. 故有

$$
p_{n+1} \leq \sqrt{p_{n}^{2}+a p_{n}+b}<p_{n}+a+b .
$$

性质 4. $\left\{p_{n}\right\}$ 有界.

取 $A=\max \left\{p_{1}, p_{2}, \ldots, p_{T}\right\}+a+b+3>3$.

当 $N=A$ ! 时, $N+2, N+3, \ldots, N+a+b+1$ 是连续 $a+b$ 个合数, 且有
$p_{i} \leq N+1, \forall 1 \leq i \leq T$.

而对 $n \geq T$, 若 $p_{n} \leq N+1$, 有 $p_{n+1} \leq N+a+b+1$. 但 $p_{n+1}$ 是素数, 所以 $p_{n+1}$ 不能为 $N+2, N+3, \ldots, N+a+b+1$ 中任意一个. 故有 $p_{n+1} \leq N+1$.

由归纳法可得 $p_{n} \leq N+1$ 对所有 $n$ 成立.

由性质 $4, p_{n}$ 只有有限多个取值, 这与性质 1 相矛盾. 故 $\left\{p_{n}\right\}$ 是最终周期的. 由于素数有无穷多个, $p_{1}$ 的值可以取到无穷多个, 故存在无穷多个这样的数列.

评注 这个模 3 余 1 的条件非常奇怪, 给了我们很大的提示, 主要是要想清楚最终的周期怎么生成. 为此, 可以去分析：当 $p_{n}$ 模 3 余 $0,1,2$ 时, $p_{n+1}$ 的取值情况. 最后发现, 实际上只需要处理 $p_{n}$ 从某项起全为模 3 余 2 的项的情况. 而这将导出我们的性质 3 . 由于存在任意长的连续合数, 合在一起导出性质 4 , 也可以得到最终周期.

8. 给定正整数 $n, k, n \geq 2$. 给定一个标号为 $1,2, \ldots, n$ 的树 $T$. 我们对正整数序列 $\left(a_{1}, a_{2}, \ldots, a_{k}\right)$ 进行操作, 这里的 $1 \leq a_{i} \leq n$. 选定一个 $1 \leq i \leq k-1$, 若 $a_{i}$ 和 $a_{i+1}$ 在树中有边相连, 则可以交换 $a_{i}, a_{i+1}$ 的位置. 若一个序列可以通过有限次交换变成另一个, 则称这两个序列等价. 记 $f(T)$ 是序列的等价类的个数,求 $f(T)$ 的所有可能值.

答案 若 $n=2$, 则 $f(T)$ 的所有可能值为 $k+1$. 若 $n>2, f(T)$ 的所有可能值为 $\frac{(n-1)^{k+1}-1}{n-2}$.

解 对于正整数 $m$. 假设所有长度为 $m$ 的等价类构成的集合为 $A_{m}$, 设 $\left|A_{m}\right|=t_{m}$. 设 $X_{i}$ 为所有 $i$ 开头的长度为 $m+1$ 序列的等价类构成的集合 $(1 \leq i \leq n)$.

对于任意两个长度为 $m$ 的序列, $a=\left(a_{1}, \ldots, a_{m}\right), b=\left(b_{1}, \ldots, b_{m}\right)$. 若有 $a$ 与 $b$ 等价, 则一定有 $\left(i, a_{1}, \ldots, a_{m}\right)$ 与 $\left(i, b_{1}, \ldots, b_{m}\right)$ 等价; 若 $\left(i, a_{1}, \ldots, a_{m}\right)$ 与 $\left(i, b_{1}, \ldots, b_{m}\right)$ 等价, 我们下面证明 $a$ 与 $b$ 等价.

考虑将 $\left(i, a_{1}, \ldots, a_{m}\right)$ 操作到 $\left(i, b_{1}, \ldots, b_{m}\right)$ 的操作过程, 记作 $F$. 在 $F$ 中去掉所有交换 $i$ 的操作变为操作过程 $F^{\prime}$. 由于交换 $i$ 和其它元素不改变除 $i$ 以外的相对顺序. 故对序列 $\left(i, a_{1}, \ldots, a_{m}\right)$ 按 $F^{\prime}$ 操作可始终固定 $i$ 不动得到 $\left(i, b_{1}, \ldots, b_{m}\right)$, 这告诉我们 $a$ 与 $b$ 等价.

所以两个 $i(1 \leq i \leq n)$ 开头的长度为 $m+1$ 的序列等价当且仅当去掉开头
得到的两个长度为 $m$ 的序列等价. 由此我们可用去掉第一个元素的方法得到从 $X_{i}$ 到 $A_{m}$ 的双射.

至此, 我们证明了 $\left|X_{i}\right|=t_{m}$. 下面来计算 $\left|X_{i} \cap X_{j}\right|, i \neq j$.

对 $i \neq j$, 如果 $X_{i}$ 中某个元素的代表元 $c=\left(c_{1}, \ldots, c_{m+1}\right)$ 与 $X_{j}$ 中某个元素的代表元 $d=\left(d_{1}, \ldots, d_{m+1}\right)$ 等价.

考虑 $d_{1}$ 在 $c=\left(c_{1}, \ldots, c_{m+1}\right)$ 中的初始位置, 它在 $c_{1}$ 的后方, 经操作后, 它变到 $c_{1}$ 的前方. 由离散介值原理知存在一次操作交换 $c_{1}$ 与 $d_{1}$, 则有 $i, j$ 在 $T$ 中相连.

同理可知, 若 $d_{1}$ 在 $c$ 中的对应项是 $c_{p}(p \geq 2), c_{1}$ 在 $d$ 中的对应项是 $d_{q}(q \geq 2)$, 则 $d_{1}$ 与 $c_{1}, \ldots, c_{p-1}$ 均有边相连, $c_{1}$ 与 $d_{1}, \ldots, d_{q-1}$ 均有边相连. 所以可以进行操作, 把 $\left(c_{1}, \ldots, c_{m+1}\right)$ 变成 $\left(c_{1}, d_{1}, c_{2}, \ldots, c_{p-1}, c_{p+1}, \ldots, c_{m+1}\right)$.

同理可将 $\left(d_{1}, \ldots, d_{m+1}\right)$ 变成 $\left(d_{1}, c_{1}, d_{2}, \ldots, d_{q-1}, d_{q+1}, \ldots, d_{m+1}\right)$, 再交换 $c_{1}$与 $d_{1}$, 可知 $\left(c_{1}, d_{1}, c_{2}, \ldots, c_{p-1}, c_{p+1}, \ldots, c_{m+1}\right)$ 与 $\left(d_{1}, c_{1}, d_{2}, \ldots, d_{q-1}, d_{q+1}, \ldots, d_{m+1}\right)$等价. 只要 $m \geq 2$, 就可再去掉开头的两位 $c_{1}, d_{1}$, 可知 $\left(c_{2}, \ldots, c_{p-1}, c_{p+1}, \ldots, c_{m+1}\right)$与 $\left(d_{2}, \ldots, d_{q-1}, d_{q+1}, \ldots, d_{m+1}\right)$ 等价.

而对于在 $T$ 中有边的 $i, j$, 可以在 $A_{m-1}$ 任意一个等价类的元素可以在前面分别添加 $i, j$ 和 $j, i$, 可分别得到开头为 $i, j$ 的两个序列, 且它们等价. 由此得到 $X_{i} \cap X_{j}$ 到 $A_{m-1}$ 的一个双射.

至此, 我们证明了: 若 $m \geq 2, i \neq j$, 若 $i, j$ 在 $T$ 中相连, 则 $\left|X_{i} \cap X_{j}\right|=t_{m-1}$,若 $i, j$ 不在 $T$ 中相连, 则 $\left|X_{i} \cap X_{j}\right|=0$.

对于 $m \geq 2$, 由于 $T$ 是树, $T$ 中不存在 3 点两两相连, 即 $\forall 1 \leq i<j<k \leq n$,有 $\left|X_{i} \cap X_{j} \cap X_{k}\right|=0$. 由容斥原理, 结合树有 $n-1$ 条边,

$$
t_{m+1}=\left|\bigcup_{i=1}^{n} X_{i}\right|=\sum_{i=1}^{n}\left|X_{i}\right|-\sum_{1 \leq i<j \leq n}\left|X_{i} \cap X_{j}\right|=n t_{m}-(n-1) t_{m-1} .
$$

而 $t_{1}=n, t_{2}=n^{2}-n+1$, 通过递推式可求得

$$
f(T)=t_{k}= \begin{cases}k+1, & \text { 若 } n=2, \\ \frac{(n-1)^{k+1}-1}{n-2}, & \text { 若 } n \geq 3 .\end{cases}
$$

评注 这个题仔细想想会发现其实思路很自然，就是通过递推和对应来处理. 我们先刻画出了 $i$ 开头的两个序列等价的充要条件是去掉第一位等价. 再证明了, 对 $i \neq j, i$ 开头的序列和 $j$ 开头的序列等价, 当且仅当这两个序列都出现了 $i, j$, 且 $i, j$ 在树中连边, 且去掉这两个序列中所对应的 $i, j$ 后, 剩下 $k-2$
位仍然等价. 可以这样做下去, 比如对互不相等的 $i_{1}, i_{2}, i_{3}$, 有 $i_{1}$ 开头, $i_{2}$ 开头, $i_{3}$开头的三个序列等价, 当且仅当这三个序列都出现了 $i_{1}, i_{2}, i_{3}$, 且 $i_{1}, i_{2}, i_{3}$ 在树中两两连边, 且去掉这两个序列中所对应的 $i_{1}, i_{2}, i_{3}$ 后, 剩下 $k-3$ 位仍然等价. 对一般的图 $T$, 也可以一直做下去, 最后利用容斥原理可以算出答案.

这个题放在第八题, 而题面给人一种答案依赖于 $T$ 的错觉, 加之第 5 题上可能会浪费很多时间, 所以难度不小. 不过其递推的思路是很自然的, 是一道漂亮的题.

## III. 总评

本次考试的第 $4,5,8$ 题都不是太能做的题, 1 是在两道很难的陈题基础上改编的. 剩下的 $2,3,6,7$ 题属于能做的题. 一般而言, 把能做的题都做对, 就可以得到不错的成绩了. 本次大约有 350 个学生参加考试, 有 41 个同学获得一等奖,大约有 70 个同学获得二等奖.

