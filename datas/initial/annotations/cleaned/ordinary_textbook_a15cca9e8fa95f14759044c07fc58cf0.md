数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 第一届国际大都市竞赛数学试题评析 

吴尉迟 叶思冷岗松

(上海大学数学系, 200444)

第一届国际大都市竞赛 (IOM) 于 2016 年 9 月 4 日至 9 日在莫斯科举行. IOM 比赛是由俄罗斯创办的国际赛事, 此次比赛邀请了 22 个国际知名大都市参加, 其中中国仅北京参赛. 比赛共分四个学科: 数学、物理、化学、计算机.其中数学比赛采用标准 IMO 赛制, 分两天, 每天四个半小时三道题, 每题 7 分.本文介绍第一届 IOM 比赛的数学试题与解答.

## I. 试 题

1. 求所有的正整数 $n$, 使得存在 $n$ 个连续的正整数, 其和为完全平方数.
2. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是满足如下不等式的正整数:

$$
\sum_{i=1}^{n} \frac{1}{a_{i}} \leq \frac{1}{2}
$$

每年, 某机构要发布 $n$ 个指标的年度报告. 第 $i(i=1, \cdots, n)$ 个指标在集合 $\left\{1,2, \cdots, a_{i}\right\}$ 中取值. 我们称一个年度报告是 “乐观的” , 若至少有 $n-1$ 个指标比前一年的高. 证明: 该机构可以一直连续发布乐观的年度报告.

3. 设 $A_{1} A_{2} \cdots A_{n}$ 是内接于圆 $\odot O$ 的凸 $n$ 边形, 点 $O$ 是 $A_{1} A_{2} \cdots A_{n}$ 的内点;令 $B_{1}, B_{2}, \ldots, B_{n}$ 分别是边 $A_{1} A_{2}, A_{2} A_{3}, \cdots, A_{n} A_{1}$ 上的点 (均不与顶点重合), 证明:

$$
\frac{B_{1} B_{2}}{A_{1} A_{3}}+\frac{B_{2} B_{3}}{A_{2} A_{4}}+\cdots+\frac{B_{n} B_{1}}{A_{n} A_{2}}>1
$$

4. 凸四边形 $A B C D$ 中, $\angle A=\angle C=\frac{\pi}{2}$. 点 $E$ 在边 $A D$ 的延长线上, 且有 $\angle A B E=\angle A D C$. 点 $K$ 在 $C A$ 延长线上, 且有 $K A=A C$. 证明: $\angle A D B=$ $\angle A K E$.
5. 设 $r(x)$ 为奇数阶的实系数多项式. 证明: 仅存在有限多对实系数多项式收稿日期: 2017-09-14； 修订日期: 2017-10-20.
$p(x), q(x)$ 使得

$$
p(x)^{3}+q\left(x^{2}\right)=r(x) .
$$

6. 一个国家有 $n$ 个城市, 其中某些对城市间存在由 $A, B$ 两个公司运营的单程航班, 两个城市间的每个方向的航班都可以多于一趟.一个由 $A, B$ 两个字母组成的词 $w$ 称为 “可实施的” , 若存在一个连续的航班序列, 使得该序列上的航班公司名称依次排列组成词 $w$. 证明: 若任意 $2^{n}$ 长的单词可实施, 则任意有限长的词可实施.

注: 词的长度就是词中 $A, B$ 字母的个数, 如 $A A B A$ 的长度为 4 .

## II. 解 答

1. 求所有的正整数 $n$, 使得存在 $n$ 个连续的正整数, 其和为完全平方数.

解 对正整数 $t$, 令

$$
S(n, t)=(t+1)+(t+2)+\cdots+(t+n)=\frac{n(2 t+n+1)}{2} .
$$

(1) 当 $n$ 为奇数时, 只需令 $t=\frac{n-1}{2}$ 就有 $S(n, t)=n^{2}$;

(2) 当 $n$ 为偶数时, 设 $n=2^{s} m$, 其中 $s$ 是一个正整数, $m$ 是一个奇数.

注意到 $2 t+n+1$ 是奇数, 结合 $S(n, t)$ 的定义知:

$$
2^{s-1} \mid S(n, t) \text { 且 } 2^{s} \mid S(n, t) \text {. }
$$

因此

i) 当 $s$ 是偶数时, $S(n, t)$ 不是完全平方数;

ii) 当 $s$ 是奇数时, 任取奇数 $x>n$, 并令

$$
t=\frac{m x^{2}-n-1}{2} \in \mathbb{N}^{*}
$$

则 $S(n, t)=2^{s-1} m^{2} x^{2}$ 是完全平方数.

综上, 满足条件的 $n$ 的解集为 $\left\{2^{s} m \mid m\right.$ 是任意奇数, $s$ 是 0 或者奇数 $\}$.

2. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是满足如下不等式的正整数:

$$
\sum_{i=1}^{n} \frac{1}{a_{i}} \leq \frac{1}{2}
$$

每年, 某机构要发布 $n$ 个指标的年度报告. 第 $i(i=1, \cdots, n)$ 个指标在集合 $\left\{1,2, \cdots, a_{i}\right\}$ 中取值. 我们称一个年度报告是 “乐观的”，若至少有 $n-1$ 个指标比前一年的高. 证明: 该机构可以一直连续发布乐观的年度报告.

证明 对 $\forall 1 \leq i \leq n$, 设 $k_{i}$ 是满足 $2^{k_{i}} \leq a_{i}<2^{k_{i}+1}$ 的正整数, 则

$$
\sum_{i=1}^{n} \frac{1}{2^{k_{i}}}<\sum_{i=1}^{n} \frac{2}{a_{i}} \leq 1
$$

下面我们证明: 可选取一个模 $2^{k_{i}}$ 的剩余类 $A_{i}$, 使得 $A_{1}, \cdots, A_{n}$ 两两不交.

不妨设 $k_{1} \leq k_{2} \leq \cdots \leq k_{n}, A_{1}, A_{2}, \cdots, A_{n}$ 按这个顺序对应选取. $A_{1}$ 可任意选取, 假设已经选取了满足要求的 $A_{1}, \cdots, A_{i-1}$. 注意到对 $\forall j<i$, 集合 $A_{j}$ 至多包含 $2^{k_{i}-k_{j}}$ 个不同的模 $2^{k_{i}}$ 的剩余类.

对每一个 $j(1 \leq j \leq i-1)$, 设 $A_{j}=\left\{p \cdot 2^{k_{j}}+t \mid p \in N^{*}, 1 \leq t \leq 2^{k_{j}}\right\}$. 注意到

$$
\begin{aligned}
& \left(p+2^{k_{i}-k_{j}}\right) \cdot 2^{k_{j}}+t \\
= & p \cdot 2^{k_{j}}+2^{k_{i}}+t \\
\equiv & p \cdot 2^{k_{j}}+t\left(\bmod 2^{k_{i}}\right)
\end{aligned}
$$

这说明序列 $\left\{p \cdot 2^{k_{j}}+t\right\}_{p \in N}$ 关于模 $2^{k_{i}}$ 是以 $2^{k_{i}-k_{j}}$ 为周期的, 从而 $A_{j}$ 的数至多分属于模 $2^{k_{i}}$ 的 $2^{k_{i}-k_{j}}$ 个不同的剩余类.

另一方面, 由 (1) 知

$$
\sum_{j=1}^{i-1} 2^{k_{i}-k_{j}}<2^{k_{i}} \sum_{j=1}^{i-1} 2^{-k_{j}}<2^{k_{i}} \sum_{j=1}^{n} \frac{1}{2^{k_{j}}} \leq 2^{k_{i}}
$$

故仍有未被选取的模 $2^{k_{i}}$ 剩余类, 从未被选取的模 $2^{k_{i}}$ 剩余类中任选一个作为 $A_{i}$即可.

回到原命题. 第一年, 我们令所有的指标都是 1 . 现考虑第 $m$ 年的报告, 若存在 $1 \leq j \leq n$ 使得 $m \in A_{j}$, 则将第 $j$ 个指标降到 1 , 其它指标在第 $m-1$ 年的基础上加 1 ; 若 $m$ 不属于任何 $A_{j}$, 则将第 $m-1$ 年的每一个指标数值加 1 .

由于 $A_{i}$ 是模 $2^{k_{i}}$ 的剩余类且剩余类 $A_{1}, \cdots, A_{n}$ 是两两不交的, 故存在唯一的 $1 \leq m_{i} \leq 2^{k_{i}}$, 使得 $m_{i} \in A_{i}, m_{i} \notin A_{j}(j \neq i)$. 从而在前 $m_{i}-1$ 年, 第 $i$ 个指标均加 1 , 在第 $m_{i}$ 年, 该指标变为 1 . 在第 $m_{i}+(k-1) 2^{k_{i}}+1\left(k \in N^{*}\right)$ 年到 $m_{i}+k 2^{k_{i}}-1$ 年, 第 $i$ 个指标均加 1 , 在第 $m_{i}-1+k 2^{k_{i}}$ 年, 该指标变为 1 . 故第 $i$个指标不会超过 $2^{k_{i}} \leq a_{i}$. 由于剩余类 $A_{1}, \cdots, A_{n}$ 是两两不交的, 故至多有一个指标在一年内下降. 得证.

3. 设 $A_{1} A_{2} \cdots A_{n}$ 是内接于圆 $\odot O$ 的凸 $n$ 边形, 点 $O$ 是 $A_{1} A_{2} \cdots A_{n}$ 的内点;令 $B_{1}, B_{2}, \ldots, B_{n}$ 分别是边 $A_{1} A_{2}, A_{2} A_{3}, \cdots, A_{n} A_{1}$ 上的点 (均不与顶点重合), 证明:

$$
\frac{B_{1} B_{2}}{A_{1} A_{3}}+\frac{B_{2} B_{3}}{A_{2} A_{4}}+\cdots+\frac{B_{n} B_{1}}{A_{n} A_{2}}>1 .
$$



证法一 我们先证明如下断言: $A_{1} A_{2} \cdots A_{n}$ 的周长 $P>4 R$, 其中 $R$ 是 $\odot O$的半径.

事实上, 连对角线 $A_{1} A_{3}, A_{1} A_{4}, \cdots, A_{1} A_{n-1}$, 从而将多边形分为 $n-2$ 个三角形. 这时, 圆心 $O$ 必属于某个三角形 $A_{1} A_{k} A_{k+1}$ 的内部 (或边界上), 从而 $\triangle A_{1} A_{k} A_{k+1}$ 是非针角三角形, 再由熟知的结论: 任何非钝角三角形的周长大于其外接圆半径的 4 倍, 可得

$$
\begin{aligned}
P & =\left(A_{1} A_{2}+\cdots+A_{k-1} A_{k}\right)+A_{k} A_{k+1}+\left(A_{k+1} A_{k+2}+\cdots+A_{n} A_{1}\right) \\
& \geq A_{1} A_{k}+A_{k} A_{k+1}+A_{k+1} A_{1}>4 R
\end{aligned}
$$

回到原命题. 设三角形 $B_{i} A_{i+1} B_{i+1}$ 的外接圆半径是 $R_{i}(i=1, \cdots, n)$ (这里约定 $A_{n+1}=A_{1}, A_{n+2}=A_{2}, B_{n+1}=B_{1}$ ). 注意到 $\triangle A_{i} A_{i+1} A_{i+2}$ 的外接圆半径为 $R$, 由正弦定理可得:

$$
\frac{B_{i} B_{i+1}}{A_{i} A_{i+2}}=\frac{2 R_{i} \sin \angle A_{i+1}}{2 R \sin \angle A_{i+1}}=\frac{R_{i}}{R}
$$

于是, 要证不等式等价于

$$
R_{1}+R_{2}+\cdots+R_{n}>R
$$

下证 (2).

因为任意三角形的边长小于其外接圆直径, 故 $B_{i} A_{i+1}+A_{i+1} B_{i+1} \leq 4 R$. 结合前面的断言可知

$R_{1}+\cdots+R_{n}>\frac{B_{1} A_{2}+A_{2} B_{2}}{4}+\frac{B_{2} A_{3}+A_{3} B_{2}}{4}+\cdots+\frac{B_{n} A_{1}+A_{1} B_{1}}{4}=\frac{P}{4}>R$,命题得证.

证法二 (孙孟越) 记弧 $\widehat{A_{i} A_{i+1}}(i=1,2, \cdots, n)$ (下标按 $\bmod n$ 理解) 的圆周角为 $\alpha_{i}, R$ 为外接圆的半径. 由于圆心 $O$ 在多边形的内部, 故 $\alpha_{i} \in\left(0, \frac{\pi}{2}\right)$, 且有 $\sum_{i=1}^{n} \alpha_{i}=\pi$.
用 $d(A, l)$ 表示点 $A$ 到直线 $l$ 的距离, 则

$$
\begin{aligned}
\left|B_{i} B_{i+1}\right| \geq d\left(B_{i}, A_{i+1} A_{i+2}\right) & =\left|B_{i} A_{i+1}\right| \sin \angle A_{i} A_{i+1} A_{i+2} \\
& =\left|B_{i} A_{i+1}\right| \cdot \frac{\left|A_{i} A_{i+2}\right|}{2 R}
\end{aligned}
$$

故

$$
\frac{\left|B_{i} B_{i+1}\right|}{\left|A_{i} A_{i+2}\right|} \geq \frac{\left|B_{i} A_{i+1}\right|}{2 R}
$$

同理

$$
\frac{\left|B_{i} B_{i-1}\right|}{\left|A_{i-1} A_{i+1}\right|} \geq \frac{\left|B_{i} A_{i}\right|}{2 R}
$$

将上述两式相加可得

$$
\frac{\left|B_{i} B_{i-1}\right|}{\left|A_{i-1} A_{i+1}\right|}+\frac{\left|B_{i} B_{i+1}\right|}{\left|A_{i} A_{i+2}\right|} \geq \frac{\left|B_{i} A_{i}\right|+\left|B_{i} A_{i+1}\right|}{2 R}=\frac{\left|A_{i} A_{i+1}\right|}{2 R}=\sin \alpha_{i} .
$$

注意到一个熟知的结论:

$$
\sin \alpha>\frac{2}{\pi} \alpha, \forall \alpha \in\left(0, \frac{\pi}{2}\right)
$$

故对 (3) 式求和可得

$$
2 \sum_{i=1}^{n} \frac{\left|B_{i} B_{i+1}\right|}{\left|A_{i} A_{i+2}\right|} \geq \sum_{i=1}^{n} \sin \alpha_{i}>\frac{2}{\pi} \sum_{i=1}^{n} \alpha_{i}=2
$$

命题得证.

4. 凸四边形 $A B C D$ 中, $\angle A=\angle C=\frac{\pi}{2}$. 点 $E$ 在边 $A D$ 的延长线上, 且有 $\angle A B E=\angle A D C$. 点 $K$ 在 $C A$ 延长线上, 且有 $K A=A C$. 证明: $\angle A D B=$ $\angle A K E$.

证明 由条件知: 四边形 $A B C D$ 在以 $B D$ 为直径的圆上, 因此 $\angle A D B=\angle A C B$. 故要证 $\angle A D B=\angle A K E$, 只需证 $B C / / K E$.

注意到

$$
\angle B C D+\angle C D A=\angle B A D+\angle A B E<180^{\circ},
$$

故可设射线 $C B$ 和 $D A$ 有公共点 $F$.



又注意到

$$
\angle B F A=90^{\circ}-\angle A D C=90^{\circ}-\angle A B E=\angle B E A,
$$

结合 $\angle B A D=90^{\circ}$ 知 $F A=A E$, 又由于 $C A=A K$, 所以四边形 $F C E K$ 是平行四边形. 因此 $B C / / K E$.

5. 设 $r(x)$ 为奇数阶的实系数多项式. 证明: 仅存在有限多对实系数多项式 $p(x), q(x)$ 使得

$$
p(x)^{3}+q\left(x^{2}\right)=r(x) .
$$

证明 (施奕成) 先证明如下引理:

引理 对任意两个实系数多项式 $f(x), g(x), f(x) \neq \delta g(x)$ ( $\delta$ 为常数), 只有有限多个实数 $\lambda$ 使 $f(x)+\lambda g(x)$ 为完全平方式.

引理的证明 设 $(f(x), g(x))=\varphi(x)$.

(1) 若 $\varphi(x)$ 不是完全平方式. 设 $f(x)=\varphi(x) f_{1}(x), g(x)=\varphi(x) g_{1}(x), \varphi(x)=$ $\varphi_{1}(x) \varphi_{2}^{2}(x)$, 其中 $\varphi_{1}(x)$ 不含平方因式. 此时 $f_{1}(x), g_{1}(x)$ 无公因式. 若存在不同的实数 $\lambda, \mu$ 使得 $f(x)+\lambda g(x)$ 和 $f(x)+\mu g(x)$ 为完全平方式. 故可设

$$
f_{1}(x)+\lambda g_{1}(x)=\varphi_{1}(x) h_{\lambda}^{2}(x), f_{1}(x)+\mu g_{1}(x)=\varphi_{1}(x) h_{\mu}^{2}(x),
$$

其中 $h_{\lambda}(x)$ 和 $h_{\mu}(x)$ 为不同的实系数多项式. 将上述两式相减得

$$
(\lambda-\mu) g_{1}(x)=\varphi_{1}(x)\left(h_{\lambda}^{2}(x)-h_{\mu}^{2}(x)\right) .
$$

从而, $\varphi_{1}(x) \mid g_{1}(x)$. 同理有, $\varphi_{1}(x) \mid f_{1}(x)$. 这与 $f_{1}(x), g_{1}(x)$ 无公因式矛盾. 故当 $\varphi(x)$ 不是完全平方式时, 至多有一个实数 $\lambda$ 使 $f(x)+\lambda g(x)$ 为完全平方式.

(2)若 $\varphi(x)$ 是完全平方式. 此时不妨设 $f(x), g(x)$ 无公因式. 设存在 5 个不同常数 $\lambda_{i}(i=1,2,3,4,5)$ 使得

$$
f(x)+\lambda_{i} g(x)=h_{i}^{2}(x), i=1,2,3,4,5 .
$$

两边求导得

$$
f^{\prime}(x)+\lambda_{i} g^{\prime}(x)=2 h_{i}^{\prime}(x) h_{i}(x), i=1,2,3,4,5 .
$$

所以 $h_{i}(x)$ 为 $f(x)+\lambda_{i} g(x)$ 及 $f^{\prime}(x)+\lambda_{i} g^{\prime}(x)$ 的公因式, 从而 $h_{i}(x)$ 为 $g^{\prime}(x)(f(x)+$ $\left.\lambda_{i} g(x)\right)-g(x)\left(f^{\prime}(x)+\lambda_{i} g^{\prime}(x)\right)$ 的因式.

注意到 $h_{1}(x), h_{2}(x), h_{3}(x), h_{4}(x), h_{5}(x)$ 两两无公因式, 所以

$$
h_{1}(x) h_{2}(x) h_{3}(x) h_{4}(x) h_{5}(x) \mid f(x) g^{\prime}(x)-f^{\prime}(x) g(x) .
$$

i) 若 $\operatorname{deg}\left(f g^{\prime}-f^{\prime} g\right) \neq 0$, 则 $\operatorname{deg}\left(f g^{\prime}-f^{\prime} g\right) \leq \operatorname{deg} f+\operatorname{deg} g-1$. 注意到至多有一个 $\lambda_{i}$ 使得 $f(x)$ 和 $-\lambda_{i} g(x)$ 最高次项系数相同且当 $f(x)$ 和 $-\lambda_{i} g(x)$ 最高次项系数不同时, 有

$$
\operatorname{deg} h_{i}=\frac{1}{2} \max \{\operatorname{deg} f, \operatorname{deg} g\}
$$

所以 $\operatorname{deg} h_{1} h_{2} h_{3} h_{4} h_{5} \geq 2 \max \{\operatorname{deg} f, \operatorname{deg} g\}>\operatorname{deg}\left(f g^{\prime}-f^{\prime} g\right)$, 矛盾!
ii) 若 $\operatorname{deg}\left(f g^{\prime}-f^{\prime} g\right)=0$, 又 $h_{1} h_{2} h_{3} h_{4} \mid f g^{\prime}-g f^{\prime}$, 故 $f g^{\prime}-g f^{\prime}=0$, 从而有

$$
\left(\frac{f(x)}{g(x)}\right)^{\prime}=0
$$

所以 $\frac{f(x)}{g(x)}$ 为常数, 矛盾!

故至多有 4 个不同的 $\lambda$ 使 $f+\lambda g$ 为完全平方式.

回到原题. 不妨设 $r(x)$ 为首一多项式 (若首项为 $c$, 将 $r(x), p(x), q(x)$ 变为 $\left.\frac{r(x)}{c}, \frac{p(x)}{\sqrt[3]{c}}, \frac{q(x)}{c}\right)$.

由条件知 $p(x)$ 是奇数阶的, 记 $r(x)=x a\left(x^{2}\right)+b\left(x^{2}\right), p(x)=x u\left(x^{2}\right)+v\left(x^{2}\right)$.代入得:

$$
x a\left(x^{2}\right)+b\left(x^{2}\right)=x^{3} u^{3}\left(x^{2}\right)+3 x u\left(x^{2}\right) v^{2}\left(x^{2}\right)+3 x^{2} u^{2}\left(x^{2}\right) v\left(x^{2}\right)+v^{3}\left(x^{2}\right)+q\left(x^{2}\right) .
$$

比较奇次项与偶次项可得

$$
\begin{gathered}
x u^{3}(x)+3 u(x) v^{2}(x)=a(x), \\
3 x u^{2}(x) v(x)+v^{3}(x)+q(x)=b(x),
\end{gathered}
$$

则由 (4) 得 $u(x) \mid a(x)$.

令 $u(x)=\lambda t(x) . \lambda$ 为常数, $t(x)$ 为首一多项式. 则由于 $t(x)$ 为 $a(x)$ 的因式,故 $t(x)$ 仅有有限个.

下面我们只需证明: 只有有限个 $\lambda$ 使 $u(x)=\lambda t(x)$ 且 (4) 有解.

对固定的 $t(x)$, 记 $a(x)=s(x) t(x)$. 此时,

$$
x \cdot \lambda^{3} t^{3}(x)+3 \lambda t(x) v^{2}(x)=t(x) s(x),
$$

化简得

$$
s(x)-x \cdot \lambda^{3} t^{2}(x)=(\sqrt{3 \lambda} v(x))^{2},
$$

从而仅需证仅有有限个 $\lambda$ 使 (6) 有解.

由引理知当 $s(x) \neq \delta x t^{2}(x)$ ( $\delta$ 为常数), 则必存在有限个 $\lambda$ 使得 $s(x)-$ $x \lambda^{3} t^{2}(x)$ 为完全平方式. 当 $s(x)=\delta x t^{2}(x)$ ( $\delta$ 为常数), 则由 (6) 知 $x t^{2}(x)$ 为完全平方式, 但该多项式次数为奇数, 矛盾!

故仅有有限个 $\lambda$ 使 (6) 有解.

6. 一个国家有 $n$ 个城市, 其中某些对城市间存在由 $A, B$ 两个公司运营的单程航班, 两个城市间的每个方向的航班都可以多于一趟.一个由 $A, B$ 两个字母组成的词 $w$ 称为 “可实施的”, 若存在一个连续的航班序列, 使得该序列上的航班公司名称依次排列组成词 $w$. 证明: 若任意 $2^{n}$ 长的单词可实施, 则任意有
限长的词可实施.

注: 词的长度就是词中 $A, B$ 字母的个数, 如 $A A B A$ 的长度为 4 .

证明 记所有的城市所组成的集合为 $S$. 令

$$
\begin{aligned}
& S_{A}=\{x \in S \mid \exists y \in S, \text { 使得 } y \xrightarrow{A} x\}, \\
& S_{B}=\{x \in S \mid \exists y \in S, \text { 使得 } y \xrightarrow{B} x\} .
\end{aligned}
$$

对一般的词 $w$, 可递归定义

$$
\begin{aligned}
& S_{w A}=\left\{x \in S \mid \exists y \in S_{w}, \text { 使得 } y \xrightarrow{A} x\right\}, \\
& S_{w B}=\left\{x \in S \mid \exists y \in S_{w}, \text { 使得 } y \xrightarrow{B} x\right\} .
\end{aligned}
$$

这样定义的集合均为 $S$ 的子集.

我们采用反证法. 假设存在不可实施的词. 令 $w=a_{1} a_{2} \cdots a_{N}$ 是最短的不可实施的词. 显然有 $N>2^{n}$. 令 $w_{i}=a_{1} a_{2} \cdots a_{i}$. 由于 $n$ 个城市共有 $2^{n}$ 个不同的子集且词 $w_{i}$ 有 $N>2^{n}$ 个, 由抽屉原理知, 存在 $1 \leq i<j \leq N$, 有 $S_{w_{i}}=S_{w_{j}}$.

考虑词 $w^{\prime}=a_{1} a_{2} \cdots a_{i-1} a_{i} a_{j+1} a_{j+2} \cdots a_{N}$, 由于 $w^{\prime}$ 长度小于 $N$, 故是可实施的. 设 $T$ 为词 $w^{\prime}$ 对应的一个连续的航班序列, 记 $T_{1}$ 是 $T$ 的前 $i$ 个航班序列, $T_{2}$是 $T$ 的后 $N-j$ 个航班序列; 记 $c$ 是 $T_{1}$ 的终点站. 由 $A_{w_{i}}$ 的递归定义知, $c \in A_{w_{i}}$.又由于 $S_{w_{i}}=S_{w_{j}}$, 故存在一个词为 $a_{1} a_{2} \cdots a_{j}$ 的连续航班序列 $T_{3}$, 以 $c$ 为其终点站. 故这时 $T_{3} T_{2}$ 是词 $w$ 对应的航班序列, 因此词 $w$ 可实施, 矛盾.

致谢 作者感谢华东师大二附中的孙孟越同学和华中师大一附中施奕成同学参与了问题的讨论, 感谢冯跃峰老师提供的宝贵修改意见.

