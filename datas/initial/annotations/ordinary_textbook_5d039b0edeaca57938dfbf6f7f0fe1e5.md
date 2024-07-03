数学新星网 $\%$ 邹瑾专栏

www.nsmath.cn/zjzl

# 2019 年中国西部数学邀请赛试题解答与评析 

邹瑾 罗振华

2019 年中国西部数学邀请赛于 8 月 13 日和 8 月 14 日的 $8: 30$ 至 $12: 30$ 在贵州遵义四中举行.

本次竞赛主试委员会主任是冷岗松 (上海大学), 委员名单如下: 熊斌 (华东师范大学)、刘诗雄 (华南师范大学中山附属中学)、冯志刚 (上海中学)、敟振华 (华东师范大学)、邹瑾 (高思教育)、何忆捷 (华东师范大学)、王广廷 (上海中学)、张端阳 (人大附中)、张甲 (郑州一中)、石泽晖 (吉林大学附属实验学校)、羊明亮 (浙江乐清知临中学)、罗振华 (华东师范大学)、周天佑.

下面介绍本次比赛的试题和解答.

## I. 试 题

1. 求所有的正整数 $n$, 使得 $3^{n}+n^{2}+2019$ 是一个完全平方数.

(邹瑾 供题)

2. 在锐角三角形 $A B C$ 中, $A B>A C$, 点 $O 、 H$ 分别为其外心和垂心, 点 $M$ 为边 $B C$ 的中点. 设 $A M$ 的延长线与 $\triangle B H C$ 的外接圆交于点 $K$, 直线 $H K$与 $B C$ 交于点 $N$. 证明: 若 $\angle B A M=\angle C A N$, 则 $A N \perp O H$.

(张甲供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_326d3794f59976bd1194g-01.jpg?height=491&width=414&top_left_y=2019&top_left_x=821)

修订日期: 2019-08-25.

3. 设 $S=\{(i, j) \mid i, j=1,2, \cdots, 100\}$ 是直角坐标平面上的 $100 \times 100$个整点构成的集合. 将 $S$ 中的每个点染为给定的四种颜色之一. 求以 $S$ 中四个颜色互不相同的点为顶点, 且边平行于坐标轴的矩形个数的最大可能值.

(翟振华 供题)

4. 设 $n(n \geq 2)$ 是给定的整数. 求最小的实数 $\lambda$, 使得对任意实数 $x_{1}, x_{2}, \cdots$, $x_{n} \in[0,1]$, 存在 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n} \in\{0,1\}$, 满足: 对任意 $1 \leq i \leq j \leq n$ 都有

$$
\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right| \leq \lambda
$$

(张端阳 供题)

5. 在锐角三角形 $A B C$ 中, $A B>A C$, 点 $O 、 H$ 分别为其外心和垂心. 过点 $H$ 作 $A B$ 的平行线交 $A C$ 于点 $M$, 过点 $H$ 作 $A C$ 的平行线交 $A B$ 于点 $N$. 设 $L$为 $H$ 关于 $M N$ 的对称点, 直线 $O L$ 与 $A H$ 交于点 $K$. 证明: $K 、 M 、 L 、 N$ 四点共圆.

(石泽晖供题)

![](https://cdn.mathpix.com/cropped/2024_02_26_326d3794f59976bd1194g-02.jpg?height=371&width=462&top_left_y=1299&top_left_x=797)

6. 设 $n(n \geq 2)$ 个正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 证明:

$$
\sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)^{2}\left(\frac{1}{i^{2}}+\frac{1}{j^{2}}\right) \geq 4(n-1) \sum_{i=1}^{n} \frac{a_{i}^{2}}{i^{2}} .
$$

(王广廷供题)

7. 证明: 对任意正整数 $k$, 至多存在有限个集合 $T$, 满足下列条件:

(1) $T$ 由有限个素数组成;

(2) $\prod_{p \in T} p \mid \prod_{p \in T}(p+k)$.

(羊明亮 供题)

8. 称形如 $\{x, 2 x, 3 x\}$ 的集合为 “好的”. 对给定的整数 $n(n \geq 3)$, 问: 由 $n$ 个正整数构成的集合最多能有多少个“好的”子集?

(羊明亮 供题)

## II. 解答与评注

题 1 求所有的正整数 $n$, 使得 $3^{n}+n^{2}+2019$ 是一个完全平方数.

解 若 $n$ 为奇数, 则 $3^{n}+n^{2}+2019 \equiv(-1)^{n}+n^{2}+3 \equiv 3(\bmod 4)$, 不可能是完全平方数. 故 $n$ 为偶数.

设 $n=2 m\left(m \in \mathbb{N}^{*}\right)$, 则

$$
3^{n}+n^{2}+2019=3^{2 m}+4 m^{2}+2019>\left(3^{m}\right)^{2},
$$

于是

$$
3^{2 m}+4 m^{2}+2019 \geq\left(3^{m}+1\right)^{2},
$$

即 $3^{m}-2 m^{2} \leq 1009$.

当 $m \geq 7$ 时, 我们用归纳法证明 $3^{m}>2 m^{2}+1009$, 当 $m=7$ 时, 结论成立.假设命题对 $m$ 成立, 即 $3^{m}>2 m^{2}+1009$. 当 $m+1$ 时,

$$
3^{m+1}>3\left(2 m^{2}+1009\right)=6 m^{2}+3027>2(m+1)^{2}+1009
$$

故命题对 $m+1$ 成立. 从而不等式获证.

因此 $m \leq 6$.

当 $m=1$ 时, $3^{2 m}+4 m^{2}+2019=2032$, 不是完全平方数.

当 $m=2$ 时, $3^{2 m}+4 m^{2}+2019=2116=46^{2}$, 满足题意.

当 $m=3$ 或 6 时, $3^{2 m}+4 m^{2}+2019 \equiv 3(\bmod 9)$, 不是完全平方数.

当 $m=4$ 时, $3^{2 m}+4 m^{2}+2019 \equiv 6(\bmod 7)$, 不是完全平方数.

当 $m=5$ 时, $3^{2 m}+4 m^{2}+2019 \equiv 3(\bmod 5)$, 不是完全平方数.

综上可知, 满足条件的正整数只有 $n=4$.

评注 这是一道中等难度的不定方程问题, 得分率为 $50.6 \%$. 所求式模 4 后可得 $n$ 是偶数, 利用不等式估计可知 $n \leq 12$, 逐一检验后得到满足条件的只有 $n=4$.

题 2 在锐角三角形 $A B C$ 中, $A B>A C$, 点 $O 、 H$ 分别为其外心和垂心, 点 $M$ 为边 $B C$ 的中点. 设 $A M$ 的延长线与 $\triangle B H C$ 的外接圆交于点 $K$, 直线 $H K$与 $B C$ 交于点 $N$. 证明: 若 $\angle B A M=\angle C A N$, 则 $A N \perp O H$.

证法一 倍长 $A M$ 到 $K^{\prime}$, 则四边形 $A B K^{\prime} C$ 为平行四边形, 由 $B H \perp$ $A C, B K^{\prime} / / A C$ 知 $B H \perp B K^{\prime}$, 同理, $C K^{\prime} \perp C H$, 于是 $B, H, C, K^{\prime}$ 四点共圆, 故 $K^{\prime}$ 与 $K$ 重合, $K H$ 为此圆的直径.

![](https://cdn.mathpix.com/cropped/2024_02_26_326d3794f59976bd1194g-04.jpg?height=540&width=468&top_left_y=201&top_left_x=794)

取 $K H$ 中点 $T$, 则 $T$ 是 $\triangle B H C$ 外接圆的圆心, 且它的半径与圆 $O$ 半径相同, 于是 $O, T$ 关于 $B C$ 对称, 故 $A H$ 平行且等于 $O T$, 从而四边形 $A O T H$ 为平行四边形, 可得 $A O / / K H$, 于是 $\angle O A M=\angle A K H$.

由 $A M, A N$ 是等角线, $A O, A H$ 也是等角线, 得 $\angle O A M=\angle H A N$, 于是 $\angle H A N=\angle A K H$.

结合 $\angle A H K=\angle N H A$ 可得 $\triangle A H K \sim \triangle N H A$, 于是

$$
A H^{2}=H N \cdot H K=H N^{2}+H N \cdot N K .
$$

结合圆幂定理知 $A H^{2}-H N^{2}=H N \cdot N K=B N \cdot N C=A O^{2}-O N^{2}$.

所以 $A N \perp O H$.

证法二 倍长 $A M$ 到 $K^{\prime}$, 则四边形 $A B K^{\prime} C$ 为平行四边形, 由 $B H \perp$ $A C, B K^{\prime} / / A C$ 知 $B H \perp B K^{\prime}$, 同理, $C K^{\prime} \perp C H$, 于是 $B, H, C, K^{\prime}$ 四点共圆, 故 $K^{\prime}$ 与 $K$ 重合, $K H$ 为此圆的直径.

![](https://cdn.mathpix.com/cropped/2024_02_26_326d3794f59976bd1194g-04.jpg?height=600&width=460&top_left_y=1750&top_left_x=798)

取 $K H$ 中点 $T$, 则 $T$ 是 $\triangle B H C$ 外接圆的圆心, 且它的半径与圆 $\mathrm{O}$ 半径相同,于是 $O, T$ 关于 $B C$ 对称, 故 $A H$ 平行且等于 $O T$, 从而四边形 $A O T H$ 为平行四边形, 可得 $A O / / K H$, 于是 $\angle O A M=\angle A K H$.
由 $A M, A N$ 是等角线, $A O, A H$ 也是等角线, 得 $\angle O A M=\angle H A N$, 于是 $\angle H A N=\angle A K H$.

设 $A N$ 与圆 $O$ 交于点 $P$, 连结 $P O, P H$, 由圆幂定理 $A N \cdot N P=B N \cdot N C=$ $H N \cdot N K$, 故 $A, H, P, K$ 四点共圆.

从而 $\angle A P H=\angle A K H=\angle O A M=\angle H A N=\angle H A P$, 于是 $A H=H P$.

再由 $O A=O P$ 可知 $O H$ 为 $A P$ 的垂直平分线.

所以 $A N \perp O H$.

评注 这是一道中等难度的几何问题, 得分率为 $40.8 \%$. 先要导出如 $\angle O A M=\angle A K H$ 等基本几何性质, 然后有两种方法来证明 $A N \perp O H$,法一利用圆幂定理计算线段的平方差来证垂直, 法二找到了一个以 $O H$ 为对称轴的图形来证直, 这都是此类问题的常见处理方法.

题 3 设 $S=\{(i, j) \mid i, j=1,2, \cdots, 100\}$ 是直角坐标平面上的 $100 \times 100$个整点构成的集合. 将 $S$ 中的每个点染为给定的四种颜色之一. 求以 $S$ 中四个颜色互不相同的点为顶点, 且边平行于坐标轴的矩形个数的最大可能值.

解 所求的最大值为 9375000 .

设四种颜色为 $A, B, C, D$. 令 $R_{i}=\{(x, i) \mid x=1,2, \cdots, 100\}$ 为整点正方形的第 $i$ 行, $T_{j}=\{(j, y) \mid y=1,2, \cdots, 100\}$ 为整点正方形的第 $j$ 列. 称以 $S$ 中四个颜色互不相同的点为顶点, 且边平行于坐标轴的矩形为“四色矩形”.

先证如下引理:

引理 若 $R_{i}, R_{j}$ 恰好在 $k$ 个位置上同色, 则这两行产生的四色矩形的个数不超过 $\frac{(100-k)^{2}}{4}$.

证明 若 $R_{i}, R_{j}$ 在某个位置上同色, 则这两个点不可能属于一个四色矩形.若 $(x, i),(x, j)$ 为 $A, B$ 两色, 则当且仅当 $(y, i),(y, j)$ 为 $C, D$ 两色时这四点构成四色矩形. 类似可得其他情况.

在 100 对格点 $(x, i),(x, j)$ 中 $(1 \leq x \leq 100)$, 设有 $l_{1}$ 对格点为 $A, B$ 两色, 有 $l_{2}$ 对格点为 $A, C$ 两色, 有 $l_{3}$ 对格点为 $A, D$ 两色, 有 $l_{4}$ 对格点为 $B, C$ 两色, 有 $l_{5}$对格点为 $B, D$ 两色, 有 $l_{6}$ 对格点为 $C, D$ 两色. 则 $l_{1}+l_{2}+\cdots+l_{6}=100-k$.

注意到 $R_{i}$ 与 $R_{j}$ 恰好生成 $l_{1} l_{6}+l_{2} l_{5}+l_{3} l_{4}$ 个四色矩形, 而

$$
\begin{aligned}
l_{1} l_{6}+l_{2} l_{5}+l_{3} l_{4} & \leq \frac{\left(l_{1}+l_{6}\right)^{2}}{4}+\frac{\left(l_{2}+l_{5}\right)^{2}}{4}+\frac{\left(l_{3}+l_{4}\right)^{2}}{4} \\
& \leq \frac{\left(l_{1}+l_{2}+l_{3}+l_{4}+l_{5}+l_{6}\right)^{2}}{4}=\frac{(100-k)^{2}}{4} .
\end{aligned}
$$

故引理获证.

回到原题. 设 $R_{i}$ 与 $R_{j}$ 在 $k_{i, j}$ 个位置上同色, 则 $\sum_{1 \leq i<j \leq 100} k_{i, j}$ 恰为横坐标相同的同色点对的个数. 我们从每一列出发对它进行计数, 设 $T_{j}$ 中 $A, B, C, D$ 四色各有 $a_{j}, b_{j}, c_{j}, d_{j}$ 个 $\left(a_{j}+b_{j}+c_{j}+d_{j}=100\right)$, 则 $T_{j}$ 中同色点对恰有 $\mathrm{C}_{a_{j}}^{2}+\mathrm{C}_{b_{j}}^{2}+\mathrm{C}_{c_{j}}^{2}+\mathrm{C}_{d_{j}}^{2}$个. 从而

$$
\begin{aligned}
\sum_{1 \leq i<j \leq 100} k_{i, j} & =\sum_{j=1}^{100}\left(\mathrm{C}_{a_{j}}^{2}+\mathrm{C}_{b_{j}}^{2}+\mathrm{C}_{c_{j}}^{2}+\mathrm{C}_{d_{j}}^{2}\right) \\
& =\sum_{j=1}^{100}\left[\frac{1}{2}\left(a_{j}^{2}+b_{j}^{2}+c_{j}^{2}+d_{j}^{2}\right)-\frac{1}{2}\left(a_{j}+b_{j}+c_{j}+d_{j}\right)\right] \\
& \geq \sum_{j=1}^{100}\left[\frac{1}{8}\left(a_{j}+b_{j}+c_{j}+d_{j}\right)^{2}-\frac{1}{2}\left(a_{j}+b_{j}+c_{j}+d_{j}\right)\right] \\
& =100 \cdot\left(\frac{1}{8} \cdot 100^{2}-\frac{1}{2} \cdot 100\right) \\
& =120000 .
\end{aligned}
$$

结合引理及上式可知四色矩形的个数不超过

$$
\begin{aligned}
\sum_{1 \leq i<j \leq 100} \frac{\left(100-k_{i, j}\right)^{2}}{4} & \leq \sum_{1 \leq i<j \leq 100} \frac{100 \cdot\left(100-k_{i, j}\right)}{4} \\
& =2500 \cdot \mathrm{C}_{100}^{2}-25 \sum_{1 \leq i<j \leq 100} k_{i, j} \\
& \leq 9375000
\end{aligned}
$$

下面构造一种染色方法使得图中恰有 9375000 个四色矩形.将 $100 \times 100$ 个整点等分为 16 个区域, 每个区域均为 $25 \times 25$ 个整点, 按下图将每个区域染色:

| $A$ | $B$ | $C$ | $D$ |
| :---: | :---: | :---: | :---: |
| $B$ | $A$ | $D$ | $C$ |
| $C$ | $D$ | $A$ | $B$ |
| $D$ | $C$ | $B$ | $A$ |

由上述染色方法, 当两行的第一个格点属于同一区域时, 这两行不生成四色矩形; 当两行的第一个格点不属于同一区域时, 那么这两行有 4 对区域构成同色矩形, 从而生成 $4 \times 25^{2}=2500$ 个四色矩形. 故图中共有 $2500 \times\left(25 \times 25 \times C_{4}^{2}\right)=$ 9375000 个同色矩形, 满足条件.

综上, 所求的最大值为 9375000 .

评注 这是一道非常困难的组合问题, 得分率为 $5.8 \%$. 考试中很多同学把答案猜错了(算成了6250000). 此题的入手点在于构造, 先把格点等分成 $4 \times 4$ 个区域, 再将这些区域适当 4 染色后就可以得到 9375000 个同色矩形. 证明基于同色
点对的估计, 引理提供了对每两行的四色矩形个数的估计, 先用算两次的方法及柯西不等式可以得到 $\sum_{1 \leq i<j \leq 100} k_{i, j}$ 的下界, 再结合引理及适当的不等式放缩就可以证得结果.

题 4 设 $n(n \geq 2)$ 是给定的整数. 求最小的实数 $\lambda$, 使得对任意实数 $x_{1}, x_{2}, \cdots, x_{n} \in[0,1]$, 存在 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n} \in\{0,1\}$, 满足: 对任意 $1 \leq i \leq j \leq n$ 都有

$$
\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right| \leq \lambda
$$

解 $\lambda$ 的最小值为 $\frac{n}{n+1}$.

一方面, 取 $x_{1}=x_{2}=\cdots=x_{n}=\frac{1}{n+1}$. 对任意 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n} \in\{0,1\}$, 我们证明存在 $1 \leq i \leq j \leq n$, 使得

$$
\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right| \geq \frac{n}{n+1}
$$

事实上, 当存在某个 $1 \leq t \leq n$ 使得 $\varepsilon_{t}=1$ 时, 取 $i=j=t$, 则

$$
\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right|=\left|\varepsilon_{t}-x_{t}\right|=\left|1-\frac{1}{n+1}\right|=\frac{n}{n+1}
$$

当对任意 $1 \leq t \leq n$ 都有 $\varepsilon_{t}=0$ 时, 取 $i=1, j=n$, 则

$$
\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right|=\left|\sum_{k=1}^{n}\left(\varepsilon_{k}-x_{k}\right)\right|=n\left|0-\frac{1}{n+1}\right|=\frac{n}{n+1} .
$$

故 $\lambda \geq \frac{n}{n+1}$.

另一方面, 我们说明当 $\lambda=\frac{n}{n+1}$ 时, 对任意实数 $x_{1}, x_{2}, \cdots, x_{n} \in[0,1]$, 存在满足要求的 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n} \in\{0,1\}$.

记 $S_{0}=0, S_{1}=x_{1}, S_{2}=x_{1}+x_{2}, \cdots, S_{n}=x_{1}+x_{2}+\cdots+x_{n}$.

将区间 $[0,1)$ 等分成 $n+1$ 个小区间 $\left[0, \frac{1}{n+1}\right),\left[\frac{1}{n+1}, \frac{2}{n+1}\right), \cdots,\left[\frac{n}{n+1}, 1\right)$, 则其中一定有一个区间不含 $\left\{S_{1}\right\},\left\{S_{2}\right\}, \cdots,\left\{S_{n}\right\}$ （\{x\} 表示 $x$ 的小数部分）, 记此区间为 $\left[\alpha-\frac{1}{n+1}, \alpha\right)$.

下面给出 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}$ 的取法: 对任意 $1 \leq k \leq n$, 如果存在非负整数 $m$,使得

$$
S_{k-1} \leq m+\alpha-\frac{1}{n+1}<m+\alpha \leq S_{k}
$$

则取 $\varepsilon_{k}=1$; 否则取 $\varepsilon_{k}=0$. $\frac{n}{n+1}$.

下面验证这样的取法满足要求, 即对任意 $1 \leq i \leq j \leq n$ 都有 $\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right| \leq$
事实上, 由 $\alpha$ 的取法, 知存在非负整数 $m, l$ 使得

$$
m-1+\alpha \leq S_{i-1} \leq m+\alpha-\frac{1}{n+1}, \quad l-1+\alpha \leq S_{j} \leq l+\alpha-\frac{1}{n+1}
$$

所以

$$
x_{i}+\cdots+x_{j}=S_{j}-S_{i-1} \in\left[l-m-\frac{n}{n+1}, l-m+\frac{n}{n+1}\right] .
$$

由 $\varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}$ 的取法, 知在 $\varepsilon_{i}, \cdots, \varepsilon_{j}$ 中恰有 $l-m$ 个为 1 , 于是

$$
\varepsilon_{i}+\cdots+\varepsilon_{j}=l-m
$$

故

$$
\left(\varepsilon_{i}+\cdots+\varepsilon_{j}\right)-\left(x_{i}+\cdots+x_{j}\right) \in\left[-\frac{n}{n+1}, \frac{n}{n+1}\right],
$$

即

$$
\left|\sum_{k=i}^{j}\left(\varepsilon_{k}-x_{k}\right)\right| \leq \frac{n}{n+1}
$$

综上, $\lambda$ 的最小值为 $\frac{n}{n+1}$.

评注 这是一道比较困难的带有组合意味的不等式问题, 得分率为 $7.4 \%$. 本题最困难的一步在于把不等式左边看作 $x_{k}$ 的部分和的小数部分, 从而把问题转化成一个组合问题, 转化后的问题难度较原题大大降低. 这道题的手法与 2006 年第 67 届普特南大学生数学竞赛 B2 类似:

设 $X=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$ 是 $n$ 元实数集, 证明: 存在 $X$ 的非空子集 $S$ 和整数 $m$, 使得

$$
\left|m+\sum_{s \in S} s\right| \leq \frac{1}{n+1}
$$

题 5 在锐角三角形 $A B C$ 中, $A B>A C$, 点 $O 、 H$ 分别为其外心和垂心. 过点 $H$ 作 $A B$ 的平行线交 $A C$ 于点 $M$, 过点 $H$ 作 $A C$ 的平行线交 $A B$ 于点 $N$. 设 $L$ 为 $H$ 关于 $M N$ 的对称点, 直线 $O L$ 与 $A H$ 交于点 $K$. 证明: $K 、 M 、 L 、 N$ 四点共圆.

## 证法一

![](https://cdn.mathpix.com/cropped/2024_02_26_326d3794f59976bd1194g-08.jpg?height=371&width=466&top_left_y=2256&top_left_x=795)
因为 $L$ 为 $H$ 关于 $M N$ 的对称点, $A N H M$ 是平行四边形, 所以 $\angle L N M=$ $\angle H N M=\angle A M N, L N=H N=A M$, 从而 $\triangle A M N \cong \triangle L N M$, 故 $A N M L$ 是等腰梯形,且有 $\angle N A M=\angle N L M$ 和 $A, N, M, L$ 四点共圆.

由垂心性质知 $\angle H B N=\angle H C M$, 又 $\angle B N H=\angle B A C=\angle C M H$, 所以 $\triangle B N H \sim \triangle C M H$, 则 $\frac{B N}{C M}=\frac{N H}{M H}$, 从而 $B N \cdot N A=C M \cdot M A$, 故点 $N$ 和点 $M$对圆 $O$ 的幕相同, 由圆幂定理可知 $O M=O N$.

设 $M N$ 的垂直平分线为 $l$, 由 $A N M L$ 是等腰梯形知 $A, L$ 关于直线 $l$ 轴对称, $N, M$ 关于直线 $l$ 轴对称, 又 $O$ 在 $l$ 上, 则有 $\angle K L M=\angle O A N=\angle K A M$, 故 $A, K, M, L$ 四点共圆.

则 $A, N, K, M, L$ 五点共圆, 所以 $K, M, L, N$ 四点共圆.

## 证法二

![](https://cdn.mathpix.com/cropped/2024_02_26_326d3794f59976bd1194g-09.jpg?height=374&width=466&top_left_y=1044&top_left_x=795)

因为 $L$ 为 $H$ 关于 $M N$ 的对称点, $A N H M$ 是平行四边形, 所以 $\angle L N M=$ $\angle H N M=\angle A M N, L N=H N=A M$, 从而 $\triangle A M N \cong \triangle L N M$, 故 $A N M L$ 是等腰梯形, 且有 $\angle N A M=\angle N L M$ 和 $A, N, M, L$ 四点共圆.

由垂心性质知 $\angle H B N=\angle H C M$, 又 $\angle B N H=\angle B A C=\angle C M H$, 所以 $\triangle B N H \sim \triangle C M H$, 从而 $\frac{B N}{C M}=\frac{N H}{M H}$, 故 $\frac{L N}{L M}=\frac{H N}{H M}=\frac{B N}{C M}$.

由 $\angle A N L=\angle A M L$ 知 $\angle L N B=\angle L M C$, 则 $\triangle L N B \sim \triangle L M C$, 于是 $\angle N B L=\angle M C L$, 从而点 $L$ 在圆 $O$ 上, 所以 $O A=O L$.

设 $A L$ 的垂直平分线为 $l$, 由 $A N M L$ 是等腰梯形知 $A, L$ 关于直线 $l$ 轴对称, $N, M$ 关于直线 $l$ 轴对称, 又 $O$ 在 $l$ 上, 所以 $\angle K L M=\angle O A N=\angle K A M$, 故 $A, K, M, L$ 四点共圆.

则 $A, N, K, M, L$ 五点共圆, 所以 $K, M, L, N$ 四点共圆.

评注 这是一道中等难度的几何问题, 得分率为 $52.3 \%$. 第一种方法利用相似三角形结合圆幂定理导出 $O M=O N$, 第二种方法利用相似三角形和四点共圆导出 $L$ 在 $\triangle A B C$ 的外接圆上, 之后两种方法都是利用图形的对称性来导角去证 $K, M, L, N$ 四点共圆.
题 6 设 $n(n \geq 2)$ 个正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 证明:

$$
\sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)^{2}\left(\frac{1}{i^{2}}+\frac{1}{j^{2}}\right) \geq 4(n-1) \sum_{i=1}^{n} \frac{a_{i}^{2}}{i^{2}} .
$$

证明 用数学归纳法证明不等式.

$n=2$ 时, 原不等式等价于

$$
\begin{aligned}
& \left(a_{1}+a_{2}\right)^{2}\left(1+\frac{1}{4}\right) \geq 4\left(a_{1}^{2}+\frac{a_{2}^{2}}{4}\right) \\
\Leftrightarrow & \frac{5}{4}\left(a_{1}+a_{2}\right)^{2} \geq 4 a_{1}^{2}+a_{2}^{2} \\
\Leftrightarrow & 5\left(a_{1}+a_{2}\right)^{2} \geq 16 a_{1}^{2}+4 a_{2}^{2} \\
\Leftrightarrow & a_{2}^{2}+10 a_{1} a_{2} \geq 11 a_{1}^{2},
\end{aligned}
$$

注意到 $a_{2} \geq a_{1}, a_{2}^{2} \geq a_{1}^{2}, a_{1} a_{2} \geq a_{1}^{2}$, 故上式成立, 从而 $n=2$ 时不等式成立.

假设不等式对 $n$ 成立, 即

$$
\sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)^{2}\left(\frac{1}{i^{2}}+\frac{1}{j^{2}}\right) \geq 4(n-1) \sum_{i=1}^{n} \frac{a_{i}^{2}}{i^{2}} .
$$

当 $n+1$ 时, 只需证明

$$
\begin{aligned}
& \sum_{1 \leq i<j \leq n+1}\left(a_{i}+a_{j}\right)^{2}\left(\frac{1}{i^{2}}+\frac{1}{j^{2}}\right)-\sum_{1 \leq i<j \leq n}\left(a_{i}+a_{j}\right)^{2}\left(\frac{1}{i^{2}}+\frac{1}{j^{2}}\right) \\
& \geq 4 n \sum_{i=1}^{n+1} \frac{a_{i}^{2}}{i^{2}}-4(n-1) \sum_{i=1}^{n} \frac{a_{i}^{2}}{i^{2}}
\end{aligned}
$$

即证

$$
\sum_{i=1}^{n}\left(a_{i}+a_{n+1}\right)^{2}\left(\frac{1}{i^{2}}+\frac{1}{(n+1)^{2}}\right) \geq 4 \sum_{i=1}^{n} \frac{a_{i}^{2}}{i^{2}}+\frac{4 n a_{n+1}^{2}}{(n+1)^{2}}
$$

注意到对 $1 \leq i \leq n$, 有 $a_{i} a_{n+1} \geq a_{i}^{2}$, 从而

$$
\left(a_{i}+a_{n+1}\right)^{2}=a_{i}^{2}+a_{n+1}^{2}+2 a_{i} a_{n+1} \geq 3 a_{i}^{2}+a_{n+1}^{2} .
$$

则

$$
\text { (1)左 } \begin{aligned}
& \geq \sum_{i=1}^{n}\left(3 a_{i}^{2}+a_{n+1}^{2}\right)\left(\frac{1}{i^{2}}+\frac{1}{(n+1)^{2}}\right) \\
& =3 \sum_{i=1}^{n}\left(\frac{1}{i^{2}}+\frac{1}{(n+1)^{2}}\right) a_{i}^{2}+\left(\sum_{i=1}^{n} \frac{1}{i^{2}}+\frac{1}{(n+1)^{2}}\right) a_{n+1}^{2} .
\end{aligned}
$$

故只需

$$
\begin{aligned}
& 3 \sum_{i=1}^{n}\left(\frac{1}{i^{2}}+\frac{1}{(n+1)^{2}}\right) a_{i}^{2}+\left(\sum_{i=1}^{n} \frac{1}{i^{2}}+\frac{1}{(n+1)^{2}}\right) a_{n+1}^{2} \geq 4 \sum_{i=1}^{n} \frac{a_{i}^{2}}{i^{2}}+\frac{4 n a_{n+1}^{2}}{(n+1)^{2}} \\
\Leftrightarrow & \sum_{i=1}^{n}\left(\frac{3}{(n+1)^{2}}-\frac{1}{i^{2}}\right) a_{i}^{2}+\left(\sum_{i=1}^{n} \frac{1}{i^{2}}-\frac{3 n}{(n+1)^{2}}\right) a_{n+1}^{2} \geq 0 .
\end{aligned}
$$

注意到 $\sum_{i=1}^{n} \frac{1}{i^{2}}-\frac{3 n}{(n+1)^{2}} \geq 1-\frac{3 n}{(n+1)^{2}}>0,\left\{\frac{3}{(n+1)^{2}}-\frac{1}{i^{2}}\right\}$ 关于 $i$ 是单调递增的,
$a_{i}^{2}$ 关于 $i$ 也是单调递增的, 由切比雪夫不等式

$$
\begin{aligned}
\sum_{i=1}^{n}\left(\frac{3}{(n+1)^{2}}-\frac{1}{i^{2}}\right) a_{i}^{2} & \geq \frac{1}{n}\left[\sum_{i=1}^{n}\left(\frac{3}{(n+1)^{2}}-\frac{1}{i^{2}}\right)\right] \cdot\left(\sum_{i=1}^{n} a_{i}^{2}\right) \\
& =-\left(\sum_{i=1}^{n} \frac{1}{i^{2}}-\frac{3 n}{(n+1)^{2}}\right) \cdot\left(\frac{1}{n} \sum_{i=1}^{n} a_{i}^{2}\right) \\
& \geq-\left(\sum_{i=1}^{n} \frac{1}{i^{2}}-\frac{3 n}{(n+1)^{2}}\right) a_{n+1}^{2} .
\end{aligned}
$$

所以 (2) 成立. 故 $n+1$ 时不等式成立.

综上, 不等式获证.

评注 这是一道有一定难度的不等式问题, 得分率为 $20.7 \%$. 与 $n$ 有关的不等式很自然会想到数学归纳法, $n$ 过渡到 $n+1$ 需要证明不等式 (1), 先把 $a_{i} a_{n+1}$这种项放缩为 $a_{i}^{2}$, 从而只需证 (2), 再用切比雪夫不等式或比较系数就可以得证.考场上有同学给出了 (2) 很简洁的证明, 注意到它等价于

$$
\sum_{i=1}^{n} \frac{a_{n+1}^{2}-a_{i}^{2}}{i^{2}} \geq \sum_{i=1}^{n} \frac{3\left(a_{n+1}^{2}-a_{i}^{2}\right)}{(n+1)^{2}}
$$

而

$$
\sum_{i=1}^{n} \frac{a_{n+1}^{2}-a_{i}^{2}}{i^{2}} \geq a_{n+1}^{2}-a_{1}^{2} \geq \frac{3 n\left(a_{n+1}^{2}-a_{1}^{2}\right)}{(n+1)^{2}} \geq \sum_{i=1}^{n} \frac{3\left(a_{n+1}^{2}-a_{i}^{2}\right)}{(n+1)^{2}}
$$

故不等式成立.

题 7 证明: 对任意正整数 $k$, 至多存在有限个集合 $T$, 满足下列条件:

(1) $T$ 由有限个素数组成;

(2) $\prod_{p \in T} p \mid \prod_{p \in T}(p+k)$.

证明 用反证法. 假设存在无穷多个满足条件的 $T$. 由于有限集只有有限个子集, 故对任意正整数 $M$, 存在一个满足条件的 $T$, 其中有大于 $M$ 的元素. 否则所有这样的 $T$ 都是 $\{1,2, \cdots, M\}$ 的子集, 与有无穷多个矛盾.

取 $M=2 k^{2}+2 k$. 由上述推导可知可取一个满足条件的 $T$, 使得它有大于 $M$ 的元素. 设 $q$ 为 $T$ 中最大的元素.

下面用归纳法证明: 对 $i=0,1,2, \cdots, k, q-i k$ 都是 $T$ 中的元素.

$i=0$ 时命题成立.

假设命题对 $i$ 成立. 则 $i+1$ 时, 有

$$
q-i k \mid \prod_{p \in T}(p+k)
$$

而由归纳假设, $q-i k$ 是素数, 故存在 $p \in T$ 使得 $p+k$ 是 $q-i k$ 的倍数. 由于
$q>M$, 故

$$
2(q-i k)-(q+k)=q-(2 i+1) k>2 k^{2}+2 k-(2 k+1) k>0,
$$

从而

$$
p+k \leq q+k<2(q-i k)
$$

于是只可能 $q-i k=p+k$, 即 $p=q-(i+1) k$ 是 $T$ 中的元素. 故对 $i+1$ 命题成立.

因此, $q, q-k, q-2 k, \cdots, q-k^{2}$ 都是 $T$ 中元素. 注意到 $(k, k+1)=1$, 故 $q, q-k, q-2 k, \cdots, q-k^{2}$ 构成模 $k+1$ 的完系, 从而存在 $0 \leq i \leq k$ 使得 $q-i k$是 $k+1$ 的倍数. 由于 $q-i k \geq 2 k^{2}+2 k-k^{2}=k^{2}+2 k>k+1$, 且 $k+1>1$, 故 $q-i k$ 是合数, 矛盾!

综上, 这样的 $T$ 只有有限多个.

评注 这是一道有一定难度的数论问题, 得分率为 $15.1 \%$. 考虑反证法是比较自然的, 利用反证法假设可知 $T$ 中的最大元可以任意大, 从最大元开始可以找到充分长且每一项都是素数的等差数列, 利用完系的性质可知这个等差数列中一定有合数, 从而导出矛盾.

题 8 称形如 $\{x, 2 x, 3 x\}$ 的集合为 “好的”. 对给定的整数 $n(n \geq 3)$, 问：由 $n$个正整数构成的集合最多能有多少个“好的”子集?

解法一 所求的最大值为 $n-\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil$ (其中 $\lceil y\rceil$ 表示不小于实数 $y$ 的最小整数).

一方面, 对于任一 $n$ 元正整数集 $S$, 下面证明 $S$ 中“好的”子集不超过 $n-\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil$ 个.

记 $t=\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil\left(t \in \mathbb{N}^{*}\right)$, 则 $\frac{\sqrt{8 n+1}-1}{2} \leq t<\frac{\sqrt{8 n+1}+1}{2}$. 这等价于

$$
(2 t-1)^{2}<8 n+1 \leq(2 t+1)^{2} \Leftrightarrow \frac{1}{2} t(t-1)<n \leq \frac{1}{2} t(t+1) .
$$

故可设 $n=\frac{1}{2} t(t-1)+r$, 其中 $1 \leq r \leq t\left(r \in \mathbb{N}^{*}\right)$.

下面定义等价关系 $\sim$ : 数 $x, y$ 满足 $x \sim y$ 当且仅当存在 $\alpha \in \mathbb{Z}$, 使得 $x=2^{\alpha} y$.

对于奇数 $m$, 记 $S_{m}=\{x \mid x \in S, x \sim m\}$.

那么 $S$ 中每一元素均在某个 $S_{m}$ 中. 由 $S$ 为有限集知: 只有有限个 $m$ 使得 $S_{m}$ 非空. 设它们为 $m_{1}<m_{2}<\cdots<m_{k}$, 则有 $S=S_{m_{1}} \cup S_{m_{2}} \cup \cdots \cup S_{m_{k}}$.
下记 $T_{m_{i}}=\left\{x \mid x \in S_{m_{i}}, 2 x, 3 x \in S\right\}(1 \leq i \leq k)$.

那么, 由于 $S$ 中任一“好的”子集 $\{y, 2 y, 3 y\}$ 中的元素 $y$ 必为 $T_{m_{1}} \cup T_{m_{2}} \cup$ $\cdots \cup T_{m_{k}}$ 中的元素, 且这样“好的”子集与这样的 $y$ 一一对应. 故 $S$ 中恰有 $\left|T_{m_{1}} \cup T_{m_{2}} \cup \cdots \cup T_{m_{k}}\right|=\left|T_{m_{1}}\right|+\cdots+\left|T_{m_{k}}\right|$ 个“好的”子集.

下证

$$
\sum_{i=1}^{k}\left|T_{m_{i}}\right| \leq n-t
$$

注意到, 对 $x \in T_{m_{i}}$, 有 $2 x \in S$, 即 $2 x \in S_{m_{i}}$. 又 $S_{m_{i}}$ 中必存在 2 的幂次最小的一项 $x_{0}$, 即有 $\frac{x_{0}}{2} \notin T_{m_{i}}$. 故

$$
\left|T_{m_{i}}\right| \leq\left|S_{m_{i}}\right|-1
$$

并且, 对 $x \in T_{m_{i}}, 3 x \in S$. 则 $3 x \in S_{3 m_{i}}$, 故

$$
\left|S_{3 m_{i}}\right| \geq\left|T_{m_{i}}\right|
$$

因此, 我们有:

(i) 若 $k \geq t$, 则

$$
\sum_{i=1}^{k}\left|T_{m_{i}}\right| \leq \sum_{i=1}^{k}\left(\left|S_{m_{i}}\right|-1\right)=|S|-k=n-k \leq n-t
$$

(ii) 若 $k \leq t-1$, 且对 $1 \leq i \leq k,\left|T_{m_{i}}\right| \leq t-i-1$. 则

$$
\sum_{i=1}^{k}\left|T_{m_{i}}\right| \leq \sum_{i=1}^{k}(t-i-1) \leq \frac{1}{2}(t-1)(t-2)<n-t
$$

(iii) 若 $k \leq t-1$, 且存在 $1 \leq j \leq k$ 使得 $\left|T_{m_{j}}\right| \geq t-j$.

注意到

$$
S \supseteq\left(S_{m_{1}} \cup S_{m_{2}} \cup \cdots \cup S_{m_{j}} \cup S_{3 m_{j}} \cup S_{3 m_{j+1}} \cup \cdots \cup S_{3 m_{k}}\right)
$$

故

$$
\begin{aligned}
n & \geq \sum_{i=1}^{j}\left|S_{m_{i}}\right|+\sum_{i=j}^{k}\left|S_{3 m_{i}}\right| \\
& \geq \sum_{i=1}^{j}\left|T_{m_{i}}\right|+j+(t-j)+\sum_{i=j+1}^{k}\left|T_{m_{i}}\right| \\
& =\sum_{i=1}^{k}\left|T_{m_{i}}\right|+t
\end{aligned}
$$

所以

$$
\sum_{i=1}^{k}\left|T_{m_{i}}\right| \leq n-t
$$

综合 (i), (ii), (iii) 知 $S$ 中“好的”子集不超过 $n-t$ 个.

另一方面, 我们给出构造. 取 $n$ 元正整数集 $P$ 为如下 $t$ 个集合 $P_{1}, \cdots, P_{t}$
的并: 当 $1 \leq i \leq r$ 时, $P_{i}=\left\{2^{i} 3^{\beta} \mid 1 \leq \beta \leq t+1-i\right\}$; 当 $r+1 \leq i \leq t$ 时, $P_{i}=\left\{2^{i} 3^{\beta} \mid 1 \leq \beta \leq t-i\right\}$.

则 $|P|=\frac{1}{2} t(t-1)+r=n$, 且 $P$ 中形如 $\left\{2^{\alpha} 3^{\beta}, 2^{\alpha+1} 3^{\beta}, 2^{\alpha} 3^{\beta+1}\right\}$ 的子集中 $\alpha, \beta$ 可取 $1 \leq \alpha \leq r-1,1 \leq \beta \leq t-\alpha$ 或 $r \leq \alpha \leq t-1,1 \leq \beta \leq t-\alpha-1$. 这样的 $(\alpha, \beta)$ 共计

$$
(0+1+\cdots+t-2)+(r-1)=\frac{1}{2}(t-1)(t-2)+r-1=n-t \text { 个. }
$$

综上可知, 所求的最大值为 $n-\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil$.

解法二 所求的最大值为 $n-\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil$.

例子的构造与解法一相同.

下面证明好的子集至多 $n-\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil$ 个.

将 $n$ 个数对应 $n$ 个点, 若 $x, y$ 满足 $2 x=y$, 则由 $x$ 向 $y$ 连一条红边; 若 $3 x=y$, 则由 $x$ 向 $y$ 连一条蓝边. 则每个好的子集对应一个由一点发出一红一蓝两条边的图形.

易知红边与蓝边不重合, 所有红边构成若干条链, 所有蓝边亦构成若干条链(孤立点视为自成链), 且有

红边数 $=n-$ 红链的条数, 蓝边数 $=n-$ 蓝链的条数.

设图中有 $a$ 个不同时发出蓝边和红边的点, 那么其余 $n-a$ 个点都发出红边和蓝边.

对每个同时发出红边和蓝边的点我们进行如下操作: 若它所发出的红边的终点还射出红边就继续沿红边走下去, 这样最终一定能走到某个不发出红边的点, 蓝边也类似操作最终可以走到一个不发出蓝边的点. 将最初的点映射到它所发出的红边和蓝边走到终点的两点构成的无序点对. 下面证明这是一个单射.

设数 $x$ 红边走向的终点对应数 $u$, 蓝边走向的终点对应数 $v$, 把 $x, u, v$ 都写成 $2^{\alpha} 3^{\beta} m$ 的形式(其中 $\alpha, \beta$ 是非负整数, $m$ 与 6 互素), 设 $x=2^{\alpha_{1}} 3^{\beta_{1}} m_{1}, u=$ $2^{\alpha_{2}} 3^{\beta_{2}} m_{2}, v=2^{\alpha_{3}} 3^{\beta_{3}} m_{3}$, 则 $m_{1}=m_{2}=m_{3}, \alpha_{1}=\min \left\{\alpha_{2}, \alpha_{3}\right\}, \beta_{1}=\min \left\{\beta_{2}, \beta_{3}\right\}$.故 $x$ 由 $u$ 与 $v$ 唯一确定, 从而这是一个单射.

所以

$$
n-a \leq \frac{a(a-1)}{2}
$$

从而

$$
\frac{a(a+1)}{2} \geq n
$$

解得

$$
a \geq\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil
$$

所以好的子集的个数 $\leq n-a \leq n-\left\lceil\frac{\sqrt{8 n+1}-1}{2}\right\rceil$.

评注 这是一道比较困难的组合问题, 得分率为 $10.4 \%$. 本题的入手点在于把 $n$ 写成 $2^{\alpha} 3^{\beta} m$ (其中 $\alpha, \beta$ 是非负整数, $m$ 与 6 互素), 这就把问题转化成了在平面格点上取 $n$ 个点, 其中至多有多少个腰长为 1 且直角顶点在左下方的等腰直角三角形、很自然可以猜测当格点近似地取为等腰直角形的顶点时个数达到最大, 这就得到了本题的构造. 证明这里给了两种方法, 法一是分类讨论来证明不等式, 法二是通过建立单射产生不等式, 其中第二种方法十分巧妙.

