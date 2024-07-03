$$
\text { 数学新星网 } \% \text { 学生专栏 }
$$

www.nsmath.cn/xszl

# 2020 年哈佛一麻省邀请赛 (HMIC)试题解答与评析 

郭语涵 ${ }^{1}$ 梁敬勋 ${ }^{2}$<br>(1. 郑州市第一中学, 451152; 2. 浙江省杭州学军中学, 310012)

指导教师: 张甲 边红平

本文给出 2020 年哈佛-麻省邀请赛 (HMIC) 的试题与解答. 本次邀请赛试题设计新颖有趣, 蕴含高等背景, 值得欣赏、研究并细细品味. 其中第 1,3 题大约为 $\mathrm{CMO}$ 的 1, 4 题难度, 第 2 题大约为 CMO 的 2,5 题难度. 第 4,5 题难度较大, 可以作为国家集训队训练题. 解答中初等、高等方法相得益彰, 体现了数学竞赛的美妙. 不当之处, 敬请大家批评指正.

## I. 试 题

1. Sir Alex 执教于一支具有不同身高的 $n$ 人足球队. 他希望将这 $n$ 个球员排成一排, 使得对每个球员 $P$, 在他左边并比他高的人数与在他右边并比他矮的人数之和为偶数. 用关于 $n$ 的表达式表示所有可能的排列数.
2. 一些象和马放置在由边长为 1 的单位正方形构成单元格的无限大的棋盘上, 满足:

(1) 对每个象, 存在一个马与此象在同一对角线上 (在这两个棋子之间可以有别的棋子);

(2) 对每个马, 存在一个象与此马距离恰为 $\sqrt{5}$;

(3) 如果从棋盘上任意拿掉一枚棋子, 则上述条件至少有一个将不再满足.

设 $n$ 是棋盘上的棋子的总数, 求 $n$ 的所有可能值.

3. 设点 $O$ 与四面体 $P_{1} P_{2} P_{3} P_{4}$ 每个顶点等距, 假设存在一个点 $H$ 使得对 $i=1,2,3,4$ 都有直线 $P_{i} H$ 与其他三个顶点确定的平面垂直. 设直线 $P_{1} H$ 与由三

修订日期: 2020-05-20.
点 $P_{2}, P_{3}, P_{4}$ 确定的平面交于点 $A, P_{1} H$ 上存在一个点 $B \neq P_{1}$, 满足 $O P_{1}=O B$.证明: $H B=3 H A$.

4. 已知 Catalan 数 $C_{k}=\frac{1}{k+1} \mathrm{C}_{2 k}^{k}$, 其中 $p$ 为奇素数. 证明: 集合

$$
\left\{\sum_{k=1}^{p-1} C_{k} n^{k} \mid n \in\{1,2, \cdots, p-1\}\right\}
$$

中恰有一半的数能被 $p$ 整除.

5. 在同一平面上的一个三角形和一个圆, 证明: 三角形与圆的公共部分的面积不超过该三角形面积的三分之一加上圆面积的一半.

## II . 解答与评注

1. Sir Alex 执教于一支具有不同身高的 $n$ 人足球队. 他希望将这 $n$ 个球员排成一排, 使得对每个球员 $P$, 在他左边并比他高的人数与在他右边并比他矮的人数之和为偶数.用关于 $n$ 的表达式表示所有可能的排列数.

解 1 (郭语涵) 设 $n$ 人身高分别为 $1,2,3, \cdots, n$, 身高为 $i$ 的人站在从左数第 $f(i)$ 个位置. 对于身高为 $i, j$ 的两个人 $(i<j)$, 若 $f(i)>f(j)$, 称 $(i, j)$ 为一个反序对. (不考虑反序对内部 $i, j$ 的次序, 即 $(i, j)$ 与 $(j, i)$ 视为同样的反序对), 下面需要求出 $\{1,2, \cdots, n\} \rightarrow\{1,2, \cdots, n\}$ 的双射 $f$ 的个数, 满足对于任意的 $i \in\{1,2, \cdots, n\}$, 含 $i$ 的反序对的个数均为偶数.

对于任意的 $i \in\{1,2, \cdots, n-1\}$, 考虑 $i$ 与 $i+1$ 的位置.

注意到 $\{1,2, \cdots, n\}$ 中除了 $i$ 与 $i+1$ 以外的其它数要么均大于 $i$ 与 $i+1$,要么均小于 $i$ 与 $i+1$, 故对于位置在 $i$ 与 $i+1$ 的同侧的数 $j,(i, j)$ 与 $(i+1, j)$或者同时为反序对, 或者同时不为反序对.

对于位置在 $i$ 与 $i+1$ 异侧(即在它们之间)的数 $j,(i, j)$ 与 $(i+1, j)$ 必然一个为反序对,一个不为反序对.

所以含 $i$ 的反序对的个数与含 $i+1$ 的反序对的个数之和与位于 $i$ 与 $i+1$之间的位置个数模 2 同余. (即与 $|f(i)-f(i+1)|-1$ 模 2 同余).

设含 $i$ 的反序对的个数为 $x_{i}$, 则

$$
x_{i}+x_{i+1} \equiv|f(i)-f(i+1)|-1(\bmod 2),
$$

而注意到 $2 \mid x_{i}(i=1,2, \cdots, n)$ 等价于 $2 \mid x_{1}$, 且 $2 \mid x_{i}+x_{i+1},(i=1,2, \cdots, n-$ 1) 也等价于 $2 \mid x_{1}$, 且 2||$f(i)-f(i+1) \mid-1,(i=1,2, \cdots, n-1)$
注意到 1 是最矮的人, 故 $x_{1}=f(1)-1$. 于是(1)等价于 $f(1)$ 为奇数, 且 $f(i)$与 $f(i+1)$ 不同奇偶, $(i=1,2, \cdots, n-1)$. 也等价于 $f(i) \equiv i(\bmod 2),(i=$ $1,2, \cdots, n)$. 而 $1,2, \cdots, n$ 中的奇数有 $\left[\frac{n+1}{2}\right]$ 个, 偶数有 $\left[\frac{n}{2}\right]$ 个. 所以满足条件的双射 $f$ 的个数为 $\left[\frac{n+1}{2}\right] ! \cdot\left[\frac{n}{2}\right]$ !.

评注 对于每个 $i$, 含 $i$ 的反序对有偶数个的限制条件并不好刻画, 但注意到对于 $i, i+1$, 其它数均同时大于或者小于它们, 结合 $i$ 与 $i+1$ 的特点便可以刻画出它们所在位置的限制条件, 然后证明充分必要性即可.

解 2 (梁敬勋) 记满足条件的排列数为 $f(n)$, 则 $f(1)=1$.

将 $n$ 个球员按身高从小到大编号为 $P_{1}, P_{2}, \cdots, P_{n}$, 由于 $P_{n}$ 右边的人数为偶数, 故他只能站在第 $n$, 第 $n-2, \cdots$ 这些位置, 共 $\left[\frac{n+1}{2}\right]$ 种.

对每个 $k \equiv n(\bmod 2), 1 \leq k \leq n$, 如下的双射说明 $P_{n}$ 站在第 $k$ 位的排法数恰为 $f(n-1)$ :

对 $n$ 的一个排列, 令 $P_{n}$ 出列, 并将 $P_{n}$ 右边的 $n-k$ 个人反序排列, 得到 $n-1$ 时的一个排列.

对每个球员, 称左侧比他高的人与右侧比他矮的人为他的 “逆序” . 我们验证新排列中每个人均有偶数个逆序:

只需考虑最后 $n-k$ 个人. 设其在旧排列中, 在左 $k-1$ 个人中, 有 $a$ 个逆序,在右 $n-k$ 个人中有 $b$ 个逆序, 则 $2 \mid a+b+1$.

在新排列中, 其有

$$
a+(n-k-b-1) \equiv a+b+1 \equiv 0(\bmod 2) .
$$

个逆序符合.

显然 $(*)$ 为双射. 故此时排法恰好 $f(n-1)$ 种. 故

$$
f(n)=\left[\frac{n+1}{2}\right] f(n-1) .
$$

$n=2 t-1$ 时, 计算得 $f(n)=t \cdot((t-1) !)^{2} \cdot n=2 t$ 时, $f(n)=(t !)^{2}$.

评注 试算小的 $n$ 容易发现 $P_{n}$ 的站法不影响 $P_{n-1}$ 的站法数. 如果这确实成立, 则可用乘法原理直接算 $f(n)$, 这自然引出 $(*)$ 这一对应.

2. 一些象和马放置在由边长为 1 的单位正方形构成单元格的无限大的棋盘上, 满足:

(1) 对每个象, 存在一个马与此象在同一对角线上 (在这两个棋子之间可以有别的棋子);

(2) 对每个马, 存在一个象与此马距离恰为 $\sqrt{5}$;

(3) 如果从棋盘上任意拿掉一枚棋子, 则上述条件至少有一个将不再满足.

设 $n$ 是棋盘上的棋子的总数, 求 $n$ 的所有可能值.

解 (郭语涵) 建立坐标系并记棋盘上的格子对应 $(x, y)$ (其中 $x, y \in \mathbb{Z}$ ),下先证:马与象个数相等.

对任一组马与象, 若它们距离恰为 $\sqrt{5}$, 则连一条红边. 若它们在同一条对角线上, 则连一条蓝边. 由题目条件, 每个马至少连出 1 条红边, 每个象至少连出 1 条蓝边, 且任去掉一个棋子后至少有一点不再成立. 若去掉象, 则必然是存在某个马不连出红边, 这意味着这个马仅与去掉的象连有红边. 也就是说, 不存在两个不同的象通过此方式对应同一个马, 故它们对应的马两两不同. 从而

象的个数 $\leq$ 马的个数

完全同理地考虑去掉任一个马, 得到

象的个数 $\geq$ 马的个数

从而象与马个数相等, 故必有 $2 \mid n$. 下面先构造 $4 \mid n$ 的情况.

$n=4$ 时, 如下图所示, 是符合题意的.

|  |  | 象 |  |
| :--- | :--- | :--- | :--- |
| 马 |  |  | 马 |
|  | 象 |  |  |

对于 $n=4 k\left(k \in \mathbb{N}^{*}\right)$, 只须把 $n=4$ 的构造每次向上平移 10 个单位长度, 并执行 $k-1$ 次, 得到的 $4 k$ 个点即符合题意, 因为每个马, 每个象都恰发出 1 条红边, 1 条蓝边.

下证:若存在则必有 $4 \mid n$. 由于(1) (2)均取等号, 故对于每个象, 存在唯一的马仅与该象连红边. 对于每个马, 存在唯一的象仅与该马连蓝边.

设 $n=2 m$, 则在这 $m$ 个马, $m$ 个象之间把上述的 $m$ 条红边和 $m$ 条蓝边留下, 其他边删掉. 则每个马, 每个象恰发出 1 条红边, 1 条蓝边. 按国际象棋盘黑白间隔染色, 则红边相连的两子异色, 蓝边相连的两子同色. 这 $m$ 个马, $m$ 个象之间用 $m$ 条红边一一对应相连, 故其中有 $m$ 个在黑格, $m$ 个在白格. 这 $m$ 个马, $m$个象之间用 $m$ 条蓝边一一对应相连, 故其中位于黑格与白格的棋子数均为偶数.

由上面两点知 $m$ 为偶数, 故 $4 \mid 2 m=n$.

综上, 所求的 $n=4 k$, 其中 $k \in \mathbb{N}^{*}$.
评注 $n=4$ 的构造很容易, 进而可知 $n=4 k, k \in \mathbb{N}^{*}$ 均成立.

大胆猜测, 小心求证. 证明的过程需要对题目条件充分的利用. 由条件中蕴藏的对应关系得出马与象的个数相等, 再深入分析把它们对应起来的这些“特殊” 的红线与蓝线, 结合黑白间隔染色得出马与象均有偶数个, 从而完成证明.

3. 设点 $O$ 与四面体 $P_{1} P_{2} P_{3} P_{4}$ 每个顶点等距, 假设存在一个点 $H$ 使得对 $i=1,2,3,4$ 都有直线 $P_{i} H$ 与其他三个顶点确定的平面垂直. 设直线 $P_{1} H$ 与由三点 $P_{2}, P_{3}, P_{4}$ 确定的平面交于点 $A, P_{1} H$ 上存在一个点 $B \neq P_{1}$, 满足 $O P_{1}=O B$.证明: $H B=3 H A$.

![](https://cdn.mathpix.com/cropped/2024_02_26_68f6c261615e92661066g-05.jpg?height=557&width=629&top_left_y=892&top_left_x=722)

证明 (郭语涵) 因为 $P_{2} H \perp$ 面 $P_{1} P_{2} P_{3}, P_{1} H \perp$ 面 $P_{2} P_{3} P_{4}$, 所以 $P_{2} H \perp P_{3} P_{4}$, $P_{1} H \perp P_{3} P_{4}$. 故 $P_{3} P_{4} \perp P_{1} P_{2} H$. 从而 $P_{2} A \perp P_{3} P_{4}$. 同理, $P_{3} A \perp P_{2} P_{4}, P_{4} A \perp P_{2} P_{3}$, 故 $A$ 为 $\triangle P_{2} P_{3} P_{4}$ 的垂心.

由题意知 $O$ 为四面体 $P_{1} P_{2} P_{3} P_{4}$ 的外接球球心, $B$ 为直线 $P_{1} H$ 与外接球的另一个交点.

设 $A$ 关于直线 $P_{2} P_{3}$ 的对称点为 $A^{\prime}$. 则熟知 $A^{\prime}$ 在 $\triangle P_{2} P_{3} P_{4}$ 的外接圆上, 故 $A^{\prime}$ 在四面体 $P_{1} P_{2} P_{3} P_{4}$ 的外接球上. 由于 $A^{\prime}, P_{1}, P_{4}, B$ 均在球上且 $A^{\prime} P_{4} \bigcap P_{1} B=A$. 故

$$
A A^{\prime} \cdot A P_{4}=A P_{1} \cdot A B
$$

设直线 $P_{4} A$ 交 $P_{2} P_{3}$ 于 $T$, 则

$$
2 A T \cdot A P_{4}=A P_{1} \cdot A B
$$

注意到 $P_{1} H \perp P_{4} T$, 且由 $P_{4} H \perp$ 平面 $P_{1} P_{2} P_{3}$ 知 $P_{4} H \perp P_{1} T$, 故 $H$ 为 $\triangle P_{1} P_{4} T$ 的垂心. 从而 $\triangle H A T$ 与 $\triangle P_{4} A P_{1}$ 相似. 故 $H$ 与 $P_{1}$ 在平面 $P_{2} P_{3} P_{4}$ 的同侧, 且

$$
\frac{A H}{A T}=\frac{A P_{4}}{A P_{1}}
$$

即

$$
A T \cdot A P_{4}=A H \cdot A P_{1},
$$

代入 (1)得

$$
2 A H \cdot A P_{1}=A P_{1} \cdot A B,
$$

即 $2 A H=A B$. 考虑到 $B$ 与 $P_{1}$ 在平面 $P_{2} P_{3} P_{4}$ 的异侧(由 $\triangle P_{1} A A^{\prime}$ 与 $\triangle P_{4} A B$逆相似), 有 $B$ 与 $H$ 在平面 $P_{2} P_{3} P_{4}$ 的异侧, 故

$$
H B=H A+A B=3 H A \text {. }
$$

评注本题中关于 $H$ 的系统是很容易研究清楚的:

(1) $H$ 存在当且仅当 $P_{1} P_{2} P_{3} P_{4}$ 对棱垂直.

(2) $H$ 在面上的投影为垂心.

(3) $A H \cdot A P_{1}=A P_{2} \cdot A C$.

相对来说, $O$ 的表现比较复杂. 不过本题只研究外接球, 不涉及 $O$, 考虑面在球上的截面为圆即可很快做出.

4. 已知 Catalan 数 $C_{k}=\frac{1}{k+1} \mathrm{C}_{2 k}^{k}$, 其中 $p$ 为奇素数. 证明: 集合

$$
\left\{\sum_{k=1}^{p-1} C_{k} n^{k} \mid n \in\{1,2, \cdots, p-1\}\right\}
$$

中恰有一半的数能被 $p$ 整除.

## 证明 1 (郭语涵) 设

$$
f(n)=\sum_{k=1}^{p-1} C_{k} n^{k}(n \in \mathbb{Z})
$$

熟知

$$
C_{m}=\sum_{i=0}^{m-1} C_{i} C_{m-1-i}\left(m \in \mathbb{N}^{*}\right)
$$

且易证

$$
C_{\frac{p+1}{2}} \equiv C_{\frac{p+3}{2}} \equiv \cdots \equiv C_{p-2} \equiv 0(\bmod p), C_{p-1} \equiv-1(\bmod p)
$$

故当 $p$ 不能整除 $n$ 时,

$$
f(n) \equiv \sum_{k=1}^{\frac{p-1}{2}} C_{k} n^{k}-1(\bmod p)
$$

故

$$
\begin{aligned}
(f(n)+2)^{2} & \equiv\left(\sum_{k=0}^{\frac{p-1}{2}} C_{k} n^{k}\right)^{2} \\
& =\sum_{i=0}^{\frac{p-1}{2}} \sum_{j=0}^{i} C_{j} C_{i-j} n^{i}+\sum_{i=\frac{p+1}{2}}^{p-1} \sum_{j=i-\frac{p-1}{2}}^{\frac{p-1}{2}} C_{j} C_{i-j} n^{i} \\
& \equiv \sum_{i=0}^{p-2} \sum_{j=0}^{i} C_{j} C_{i-j} n^{i}+\left(C_{\frac{p-1}{2}}\right)^{2} n^{p-1} \text { (用到(2) } \\
& \left.\equiv \sum_{i=0}^{p-2} C_{i+1} n^{i}+\left(C_{\frac{p-1}{2}}\right)^{2} n^{p-1} \text { (用到(1) }\right) \\
& \left.\equiv \sum_{i=0}^{\frac{p-3}{2}} C_{i+1} n^{i}+\left(C_{\frac{p-1}{2}}\right)^{2} n^{p-1}-n^{p-2} \text { (用到(2) }\right) \\
& \equiv n^{-1}(f(n)+1)+\left(C_{\frac{p-1}{2}}\right)^{2}-n^{p-2}(\bmod p)
\end{aligned}
$$

又

$$
\begin{aligned}
C_{\frac{p-1}{2}} & =\frac{2}{p+1} \cdot \frac{(p-1)(p-2) \cdots\left(\frac{p+1}{2}\right)}{1 \cdot 2 \cdots \cdots\left(\frac{p-1}{2}\right)} \\
& \equiv(p+1)^{-1} \cdot 2(-1)^{\frac{p-1}{2}}(\bmod p)
\end{aligned}
$$

故 $\left(C_{\frac{p-1}{2}}\right)^{2} \equiv 4(\bmod p)$, 从而我们有

$$
(f(n)+2)^{2} \equiv n^{-1}(f(n)+1)-n^{p-2}+4(\bmod p)
$$

对任意不能被 $p$ 整除的 $n$ 均成立. 故

$$
n[f(n)]^{2}+4 n f(n)+4 n \equiv f(n)+1-n^{p-1}+4 n(\bmod p)
$$

即

$$
f(n)(n f(n)+4 n-1) \equiv 0(\bmod p)
$$

对任意不能被 $p$ 整除的 $n$ 均成立.令 $n=4^{-1}$, 则有

$$
4^{-1}\left[f\left(4^{-1}\right)\right]^{2} \equiv 0(\bmod p)
$$

故 $f\left(4^{-1}\right) \equiv 0(\bmod p)$. 结合 (3), 我们知存在多项式 $g$, 使得 $\operatorname{deg} g \leq \frac{p-3}{2}$, 且

$$
f(n) \equiv\left(n-4^{-1}\right) g(n)(\bmod p)
$$

对任意不能被 $p$ 整除的 $n$ 均成立.

故有

$$
\left(n-4^{-1}\right)^{2} g(n)(n g(n)+4) \equiv 0(\bmod p)
$$

对任意不能被 $p$ 整除的 $n$ 均成立.
从而当 $p$ 不能整除 $n, p$ 不能整除 $\left(n-4^{-1}\right)$ 时,

$$
g(n)(n g(n)+4) \equiv 0(\bmod p)
$$

成立, 即左边有 $p-2$ 个不同根. 注意到 $\operatorname{deg} g \leq \frac{p-3}{2}$, 故

$$
\operatorname{deg}(g(n)(n g(n)+4)) \leq p-2,
$$

由拉格朗日定理, 它不超过 $p-2$ 个根, 故等号成立, 即 $\operatorname{deg} g=\frac{p-3}{2}, g(n)$ 恰有 $\frac{p-3}{2}$ 个不同的根, 且 $g(n)(n g(n)+4)$ 的 $p-2$ 个根即构成

$$
\{0,1,2, \cdots, p-1\} \backslash\left\{0,4^{-1}\right\}
$$

故 $g(n)$ 的 $\frac{p-3}{2}$ 个不同根均不为 0 , 不为 $4^{-1}$. 而 $f(n)$ 比 $g(n)$ 多出 $4^{-1}$ 这个根, 故 $f(n)$ 恰有 $\frac{p-1}{2}$ 个不同的非零根.

评注证明本题需要熟悉Catalan数的递推公式, 并巧妙利用多项式的性质,结合拉格朗日定理得出根的数目. 其中的代数变形和同余分析需要一定的功力,值得细细体会。

证明 2 (梁敬勋) 注意到: $C_{p-1} \equiv-1(\bmod p)$, 且对 $1 \leq k \leq p-2$ 有

$$
\begin{aligned}
C_{k} & =\frac{1}{k+1}\left(\begin{array}{c}
2 k \\
k
\end{array}\right)=\frac{2^{k}}{k+1} \frac{(2 k-1) ! !}{k !} \\
& \equiv \frac{(-2)^{k}}{k+1} \frac{(p-1)(p-3) \cdots(p-2 k+1)}{k !} \\
& \equiv \frac{(-4)^{k}}{k+1} \frac{\frac{p-1}{2} \frac{p-3}{2} \cdots \frac{p-2 k+1}{2}}{k !} \cdot \frac{p+1}{2} \cdot 2 \\
& =2(-4)^{k}\left(\begin{array}{c}
\frac{p+1}{2} \\
k+1
\end{array}\right) \quad(\bmod p)
\end{aligned}
$$

成立. 故

$$
\begin{aligned}
S_{n} & =\sum_{k=1}^{p-1} C_{k} n^{k} \equiv \sum_{k=1}^{p-2} 2(-4)^{k}\left(\begin{array}{c}
\frac{p+1}{2} \\
k
\end{array}\right) n^{k}-n^{p-1} \\
& \equiv(-2 n)^{-1}\left(\sum_{k=2}^{p-1}(-4 n)^{k}\left(\begin{array}{c}
\frac{p+1}{2} \\
k
\end{array}\right)\right)-1 \\
& \equiv(-2 n)^{-1}\left((1-4 n)^{\frac{p+1}{2}}-\frac{p+1}{2}(-4 n)-1\right)-1 \quad(\bmod p) \\
& \equiv(-2 n)^{-1}\left((1-4 n)^{\frac{p+1}{2}}+2 n-1\right)-1 \quad(\bmod p)
\end{aligned}
$$

对一切 $n \in\{1,2, \cdots, p-1\}$ 成立. 故

$$
\begin{aligned}
S_{n} \equiv 0 \quad(\bmod p) & \Leftrightarrow(1-4 n)^{\frac{p+1}{2}} \equiv 1-4 n \quad(\bmod p) \\
& \Leftrightarrow(1-4 n)\left((1-4 n)^{\frac{p-1}{2}}-1\right) \equiv 0 \quad(\bmod p)
\end{aligned}
$$

$$
\Leftrightarrow\left(\frac{1-4 n}{p}\right)=0 \text { 或 } 1 .
$$

又 $1-4 n \not \equiv 1(\bmod p)$, 故当且仅当 $1-4 n$ 取 0 或除 1 外的平方剩余时 $p \mid S_{n}$. 故恰有一半的 $S_{n}$ 为 $p$ 的倍数.

评注本做法基于 Catalan 数的母函数. 熟悉相关知识的同学应该知道, $C_{k}=\frac{1}{k+1}\left(\begin{array}{c}2 k \\ k\end{array}\right)=2(-4)^{k}\left(\begin{array}{c}\frac{1}{2} \\ k+1\end{array}\right), \frac{1-\sqrt{1-4 x}}{2 x}$ 可充当其母函数. 根据本题的特点, $\sum_{k=1}^{p-1} C_{k} n^{k}$ 给人以一种在母函数中赋值的感觉. 但对一般的母函数我们难以分离出前 $p-1$ 项, 因此需要在模 $p$ 的意义下修改母函数, 化 $\left(\begin{array}{c}\frac{1}{2} \\ k+1\end{array}\right)$ 为 $\left(\begin{array}{c}\frac{1+p}{2} \\ k+1\end{array}\right)$, 这样就只有有限项求和。

5. 在同一平面上的一个三角形和一个圆, 证明: 三角形与圆的公共部分的面积不超过该三角形面积的三分之一加上圆面积的一半.

证明 1 (郭语涵) 首先给出一个引理.

引理 若三角形的一个顶点位于圆心, 则三角形与圆的公共部分面积不超过三角形面积的 $\frac{1}{3}$ 加上圆面积的 $\frac{1}{6}$.

若引理得证, 则对于原题, 设三角形为 $\triangle A B C$, 圆为圆 $O$, 若 $O$ 在 $\triangle A B C$内(含边界), 则

$$
\begin{aligned}
S_{\triangle A B C} \cap \odot O & =S_{\triangle O A B} \cap \odot O+S_{\triangle O B C} \cap \odot O+S_{\triangle O A C} \cap \odot O \\
& \leq \frac{1}{3} S_{\Delta O A B}+\frac{1}{6} S_{\odot O}+\frac{1}{3} S_{\triangle O B C}+\frac{1}{6} S_{\odot O}+\frac{1}{3} S_{\triangle O A C}+\frac{1}{6} S_{\odot O} \\
& =\frac{1}{3} S_{\triangle A B C}+\frac{1}{2} S_{\odot O}
\end{aligned}
$$

成立.

若 $O$ 在 $\triangle A B C$ 外, 则以下三个命题:

(1) $O$ 与 $A$ 在 $B C$ 异侧;(2) $O$ 与 $B$ 在 $A C$ 异侧;(3) $O$ 与 $C$ 在 $A B$ 异侧.中至少有一个是成立的(否则 $O$ 就在 $\triangle A B C$ 内).

不妨(1)成立, $O$ 与 $A$ 在 $B C$ 异侧. 设 $O$ 在直线 $B C$ 上的投影为 $O^{\prime}$, 以 $O^{\prime}$ 为圆心, 圆 $O$ 的半径为半径作圆 $O^{\prime}$. 对于位于直线 $B C$ 的含 $A$ 的那一侧的点 $P$, 显然有 $O^{\prime} P \leq O P$ 成立. 从而 $\triangle A B C$ 内任一点到 $O^{\prime}$ 的距离不大于到 $O$ 的距离.也就是说: $\triangle A B C$ 内的一点若在圆 $O$ 中,则也必定在圆 $O^{\prime}$ 中. 故将圆 $O$ 调整为圆 $O^{\prime}$, 三角形以及圆的面积均不变, 而公共面积不减. 若 $O^{\prime}$ 在线段 $B C$ 内, 则转化为 $O$ 在 $\triangle A B C$ 内 (含边界)的情况. 若 $O^{\prime}$ 在线段 $B C$ 延长线上:

![](https://cdn.mathpix.com/cropped/2024_02_26_68f6c261615e92661066g-10.jpg?height=462&width=506&top_left_y=203&top_left_x=775)

(1)如果 $\angle A C B \leq \frac{\pi}{2}$, 则 $O^{\prime}$ 可调为 $C$ (因为对 $\triangle A B C$ 内任一点 $P$, 有 $\left.C P \leq O^{\prime} P\right)$

(2)如果 $\angle A C B>\frac{\pi}{2}$, 由于 $O^{\prime}$ 也与 $B$ 在 $A C$ 异侧, 设 $O^{\prime}$ 在 $A C$ 上的射影为 $O^{\prime \prime}$, 若 $O^{\prime \prime}$ 在线段 $A C$ 上则已成立, 若 $O^{\prime \prime}$ 在 $C A$ 延长线上则转为(1).

若 $O^{\prime}$ 在线段 $C B$ 延长线上, 同理.

从而均可转化为 $O$ 在 $\triangle A B C$ 内 (含边界)的情况. 也就是说, 若引理得证, 从而原命题得证. 下面证明引理.
![](https://cdn.mathpix.com/cropped/2024_02_26_68f6c261615e92661066g-10.jpg?height=392&width=1054&top_left_y=1314&top_left_x=504)

引理的证明 如图, 设三角形为 $\triangle O A B$, 圆为圆 $O$. 若 $A B$ 不与圆 $O$ 相交,则可将直线 $A B$ 适当平移直到与圆 $O$ 相切, 平移后的直线分别交 $O A, O B$ 于 $A^{\prime}, B^{\prime}$, 则可将 $\triangle O A B$ 调整为 $\Delta O A^{\prime} B^{\prime}$, 三角形面积减小, 而圆面积与公共面积不变. 从而可转化为 $A B$ 与圆 $O$ 相交的情形. 故只需考虑 $A B$ 与圆 $O$ 相交的情形.

如图, 设交于 $E, F$, 不妨设圆 $O$ 半径为 $1, \angle A O E=\alpha, \angle E O F=\beta, \angle F O B=$ $\gamma$, 则我们只需证

$$
\frac{\alpha}{2}+\frac{\gamma}{2}+\frac{\sin \beta}{2} \leq \frac{1}{3}\left[\frac{1}{2} \frac{\sin \alpha \cos \frac{\beta}{2}}{\cos \left(\alpha+\frac{\beta}{2}\right)}+\frac{1}{2} \frac{\sin \gamma \cos \frac{\beta}{2}}{\cos \left(\gamma+\frac{\beta}{2}\right)}+\frac{\sin \beta}{2}\right]+\frac{\pi}{6}
$$

其中 $\alpha, \beta, \gamma>0, \alpha+\beta+\gamma<\pi$, 注意到

$$
\frac{\sin \alpha}{\cos \left(\alpha+\frac{\beta}{2}\right)}+\frac{\sin \gamma}{\cos \left(\gamma+\frac{\beta}{2}\right)}=\frac{2 \sin \left(\alpha+\gamma+\frac{\beta}{2}\right)-2 \sin \frac{\beta}{2} \cos (\alpha-\gamma)}{\cos (\alpha-\gamma)+\cos (\alpha+\beta+\gamma)}
$$

故若固定 $\alpha+\gamma$, 则上式关于 $\cos (\alpha-\gamma)$ 递减, 即 $(*)$ 右边关于 $\cos (\alpha-\gamma)$ 递减, 故 $\cos (\alpha-\gamma)$ 最大时 (即 $\alpha=\gamma$ 时), (*)右边最小, 故又可调整为 $\alpha=\gamma$ 的情形. 即只需证:

$$
\alpha+\frac{\sin \beta}{2} \leq \frac{1}{3}\left(\frac{\sin \alpha \cos \frac{\beta}{2}}{\cos \left(\alpha+\frac{\beta}{2}\right)}+\frac{\sin \beta}{2}\right)+\frac{\pi}{6}(\alpha, \beta>0,2 \alpha+\beta<\pi)
$$

上式等价于证明

$$
3 \alpha+\frac{\sin \beta}{2}-\frac{1}{\cot \alpha-\tan \frac{\beta}{2}} \leq \frac{\pi}{2}\left(\alpha, \beta>0, \alpha+\frac{\beta}{2}<\frac{\pi}{2}\right) .
$$

左边关于 $\alpha$ 的导数为

$$
3+\frac{-\frac{1}{\sin ^{2} \alpha}}{\left(\cot \alpha-\tan \frac{\beta}{2}\right)^{2}}=\frac{3 \cos ^{2}\left(\alpha+\frac{\beta}{2}\right)-\cos ^{2} \frac{\beta}{2}}{\cos ^{2}\left(\alpha+\frac{\beta}{2}\right)}
$$

设 $\alpha_{0}$ 满足 $\alpha_{0}+\frac{\beta}{2}<\frac{\pi}{2}, \alpha_{0}>0$ 且 $\sqrt{3} \cos \left(\alpha_{0}+\frac{\beta}{2}\right)=\cos \frac{\beta}{2}$, 则 $\alpha \in\left(0, \alpha_{0}\right)$ 时导数为正, 关于 $\alpha$ 递增; $\alpha \in\left(\alpha_{0}, \frac{\pi}{2}-\frac{\beta}{2}\right)$ 时导数为负, 关于 $\alpha$ 递减. 故该式左边在 $\alpha=\alpha_{0}$ 时最大. 仅需考虑 $\alpha=\alpha_{0}$ 时的情形. 即证:

$$
\alpha_{0}+\frac{\sin \beta}{2} \leq \frac{\sqrt{3}}{3} \sin \alpha_{0}+\frac{\sin \beta}{6}+\frac{\pi}{6},
$$

即:

$$
3 \alpha_{0}+\sin \beta \leq \sqrt{3} \sin \alpha_{0}+\frac{\pi}{2}
$$

注意到由

$$
\sqrt{3} \cos \left(\alpha_{0}+\frac{\beta}{2}\right)=\cos \frac{\beta}{2}
$$

知

$$
\tan \frac{\beta}{2}=\frac{\cos \alpha_{0}-\frac{\sqrt{3}}{3}}{\sin \alpha_{0}}
$$

从而 $\cos \alpha_{0}>\frac{\sqrt{3}}{3}$, 且

$$
\sin \beta=\frac{2 \tan \frac{\beta}{2}}{1+\tan ^{2} \frac{\beta}{2}}=\frac{2 \sin \alpha_{0}\left(\cos \alpha_{0}-\frac{\sqrt{3}}{3}\right)}{\sin ^{2} \alpha_{0}+\left(\cos \alpha_{0}-\frac{\sqrt{3}}{3}\right)^{2}}
$$

代入, 我们只需证:

$$
\frac{\sin \alpha_{0}\left(6 \cos \alpha_{0}-3 \sqrt{3}\right)}{2-\sqrt{3} \cos \alpha_{0}}+3 \alpha_{0}-\frac{\pi}{2} \leq 0\left(\alpha_{0} \in\left(0, \frac{\pi}{2}\right), \cos \alpha_{0}>\frac{\sqrt{3}}{3}\right)
$$

设上式左边为 $f\left(\alpha_{0}\right)$, 并记 $\cos \alpha_{0}=t$ 则

$$
\begin{aligned}
f^{\prime}\left(\alpha_{0}\right) & =\frac{\left(6 \cos 2 \alpha_{0}-3 \sqrt{3} \cos \alpha_{0}\right)\left(2-\sqrt{3} \cos \alpha_{0}\right)-\sqrt{3} \sin \alpha_{0}\left(3 \sin 2 \alpha_{0}-3 \sqrt{3} \sin \alpha_{0}\right)+3(2-\sqrt{3} t)^{2}}{(2-\sqrt{3} t)^{2}} \\
& =3 \cdot \frac{4\left(2 t^{2}-1\right)-2 \sqrt{3} t-2 \sqrt{3} t\left(2 t^{2}-1\right)-2 \sqrt{3} t\left(1-t^{2}\right)+3+4+3 t^{2}-4 \sqrt{3} t}{(2-\sqrt{3} t)^{2}}
\end{aligned}
$$

$$
=3 \cdot \frac{-2 \sqrt{3} t^{3}+11 t^{2}-6 \sqrt{3} t+3}{(2-\sqrt{3} t)^{2}}=\frac{3(-2 t+\sqrt{3})(\sqrt{3} t-1)(t-\sqrt{3})}{(2-\sqrt{3} t)^{2}} .
$$

注意到 $t>\frac{\sqrt{3}}{3}$ 且 $t \leq 1<\sqrt{3}$, 故

$t \in\left(\frac{\sqrt{3}}{3}, \frac{\sqrt{3}}{2}\right)$ 时 $\left(\alpha_{0} \in\left(\frac{\pi}{6}, \arccos \frac{\sqrt{3}}{3}\right)\right.$ 时 $), f^{\prime}\left(\alpha_{0}\right)<0, f\left(\alpha_{0}\right)$ 关于 $\alpha_{0}$ 递减;

$t \in\left(\frac{\sqrt{3}}{2}, 1\right)$ 时 $\left(\alpha_{0} \in\left(0, \frac{\pi}{6}\right)\right.$ 时 $), f^{\prime}\left(\alpha_{0}\right)>0, f\left(\alpha_{0}\right)$ 关于 $\alpha_{0}$ 递增.

从而 $\alpha_{0} \in\left(0, \arccos \frac{\sqrt{3}}{3}\right)$ 时, $f\left(\alpha_{0}\right) \leq f\left(\frac{\pi}{6}\right)=0$. 引理得证, 故原题也得证.

评注 本证法依赖于大胆猜测得到了引理, 引理的证明和原问题的证明均需要多次调整来简化情况, 其中对于 $\alpha$ 求导时需要适当调整形式方便刻画零点, 复杂的计算需要细心, 耐心.

证明 2 (梁敬勋) 记三角形为 $\triangle A B C$, 圆为 $\odot O$, 半径为 $r$.

首先不妨设 $O \in \triangle A B C$. 否则可作过 $O$ 的直线 $l$, 使 $\triangle A B C$ 在 $l$ 一侧, 则公共面积至多是 $l$ 分出的某个半圆, 即圆面积的一半.

分别用 $S_{1}, S_{2}, S, c$ 表示 $S_{\triangle A B C}, S_{\odot O}$, 公共面积与 $\odot O$ 在 $\triangle A B C$ 内部的总弧长. 要证

$$
\frac{1}{3} S_{1}+\frac{1}{2} S_{2}-S \geq 0
$$

固定 $A, B, C, O$, 调整 $r$, 将(1)式左边视为 $r$ 的函数 $f(r)$. 易见 $r$ 充分大时 $f(r)$为常数, 故仅需考虑 $r \in\left[0, r_{0}\right]$ 的情况, 此处 $r_{0}$ 为常数, 则此时连续函数 $f(r)$ 有最小值 $f\left(r_{1}\right)$. 仅需 $f\left(r_{1}\right) \geq 0$.

易见 $f(0) \geq 0$, 且可不妨设 $r_{1}<r_{0}$. 考虑 $f^{\prime}(r)$. 由于 $S_{2}=\pi r^{2}$, 且 $\frac{d s}{d r}=c$, 故

$$
f^{\prime}(r)=\pi r-c
$$

由 $f\left(r_{1}\right)$ 最小性知 $f^{\prime}\left(r_{1}\right)=0$, 即

$$
\pi r_{1}=c .
$$

下始终保持(3)成立.

接下来容易进行调整, 固定 $O, r, c$ 不变, 移动 $A, B, C$, 使 $\triangle A B C$ 每边与 $\odot O$ 相切或相交, 每个顶点在 $\odot O$ 边界或外部.

若某边与 $\odot O$ 相离, 则将其向 $O$ 移动直到第一次相切, 这不改变 $S, c$ 且使 $S_{1}$ 变小(注意 $O$ 在 $\triangle A B C$ 内).

若某点(不妨 $A$ )在 $\odot O$ 内, 则由(3)知 $B, C$ 在 $\odot O$ 外. 设 $B C$ 所在直线为 $l$,线段 $A C$ 与 $\odot O$ 交于 $Y$, 射线 $B A$ 与 $\odot O$ 交于 $Z$. 将 $A$ 移到 $Z, B$ 不动, $C$ 移到 $Z Y \cap l$, 则 $S$ 变大, $S_{1}-S$ 变小, $c$ 不变,

$$
\frac{1}{3} S_{1}+\frac{1}{2} S_{2}-S=\frac{1}{3}\left(S_{1}-S\right)-\frac{2}{3} S+\frac{1}{2} S_{2}
$$

变小.

![](https://cdn.mathpix.com/cropped/2024_02_26_68f6c261615e92661066g-13.jpg?height=328&width=560&top_left_y=430&top_left_x=751)

这样, 可认为 $\triangle A B C$ 每边均与 $\odot O$ 有 2 个交点, 交点可能重合.

![](https://cdn.mathpix.com/cropped/2024_02_26_68f6c261615e92661066g-13.jpg?height=403&width=508&top_left_y=889&top_left_x=774)

设线段 $B C$ 与 $\odot O$ 的 2 个交点所对圆心角为 $2 \alpha$, 类似定义 $2 \beta, 2 \gamma$, 则(3)保证 $\alpha+\beta+\gamma=\frac{\pi}{2}, \alpha, \beta, \gamma \geq 0$, 且此时易有

$$
S=\frac{1}{2} \pi r_{1}^{2}+\frac{1}{2} r_{1}^{2}(\sin 2 \alpha+\sin 2 \beta+\sin 2 \gamma) .
$$

再设 $O$ 到 $\triangle A B C$ 三边距离为 $x, y, z$, 用 $a, b, c, A, B, C, R$ 分别表示 $\triangle A B C$的三边长、三内角与外接圆半径, 则

$$
\begin{gathered}
x=r_{1} \cos \alpha, y=r_{1} \cos \beta, z=r_{1} \cos \gamma \\
2 S_{1}=a x+b y+c z=a b \sin C=4 R^{2} \sin A \sin B \sin C
\end{gathered}
$$

故

$$
2 R=\frac{r_{1}(\sin A \cos \alpha+\sin B \cos \beta+\sin C \cos \gamma)}{\sin A \sin B \sin C} .
$$

不妨 $r_{1}=1$. 由

$$
\begin{aligned}
& \sin 2 \alpha+\sin 2 \beta+\sin 2 \gamma \\
= & 2 \sin (\alpha+\beta) \cos (\alpha-\beta)+2 \sin \gamma \cos \gamma \\
= & 2 \cos \gamma(\cos (\alpha-\beta)+\cos (\alpha+\beta)) \\
= & 4 \cos \alpha \cos \beta \cos \gamma
\end{aligned}
$$

知

$$
S=\frac{1}{2} \pi+2 \cos \alpha \cos \beta \cos \gamma
$$

由(6, (7)知:

$$
\begin{aligned}
S_{1} & =2 R^{2} \sin A \sin B \sin C \\
& =\frac{(\sin A \cos \alpha+\sin B \cos \beta+\sin C \cos \gamma)^{2}}{2 \sin A \sin B \sin C} \\
& \geq \frac{9(\cos \alpha \cos \beta \cos \gamma)^{\frac{2}{3}}}{2(\sin A \sin B \sin C)^{\frac{1}{3}}} \quad(A M-G M)
\end{aligned}
$$

故

$$
\text { (1)左边 } \begin{aligned}
& \geq \frac{2 u^{2}}{2 v}+\frac{1}{2} \pi-\frac{1}{2} \pi-2 u^{3} \\
& =\frac{3 u^{2}}{2 v}-2 u^{3}=\frac{3 u^{2}}{2 v}\left(1-\frac{4}{3} u v\right)
\end{aligned}
$$

其中 $u^{3}=\cos \alpha \cos \beta \cos \gamma, v^{3}=\sin A \sin B \sin C$. 由于

$$
\begin{aligned}
& \sin A \sin B \sin C \\
= & \frac{1}{2}(\cos (A-B)-\cos (A+B)) \sin C \\
\leq & \frac{1}{2}(1+\cos C) \sin C \\
= & \frac{1}{2} \sqrt{(1+\cos C)(1+\cos C)(1+\cos C) 3(1-\cos C)} \cdot \frac{1}{\sqrt{3}} \\
\leq & \frac{1}{2}\left(\frac{6}{4}\right)^{2} \cdot \frac{1}{\sqrt{3}}(A M-G M) \\
= & \frac{3 \sqrt{3}}{8} .
\end{aligned}
$$

有 $v \leq \frac{\sqrt{3}}{2}$. 又 $\frac{\pi}{2}-\alpha, \frac{\pi}{2}-\beta, \frac{\pi}{2}-\gamma$ 也为一三角形三内角. 同上知 $u \leq \frac{\sqrt{3}}{2}$. 故 $u v \leq \frac{3}{4}$, 从而(1)成立.

命题得证！

评注 当 $\triangle A B C$ 为边长为 3 的正三角形, $\odot O$ 半径为 1 且 $O$ 为 $\triangle A B C$ 中心时(1)可取等号. 即便如此, 不难想象本题代数化后是不紧的, 因为取等条件非常苛刻, 必然是多次放缩后的结果。

(3)是本题的关键, 其抵消了含 $\pi$ 的项, 大大简化了 (2). 利用这种: “周长是面积的某种导数”的想法结合Brunn-Minkowski不等式还可以解决等周问题：周长相等的图形以圆面积最大.

