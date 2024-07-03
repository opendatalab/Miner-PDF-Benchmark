数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2017 年夏季上海新星数学奥林匹克试题解析 

吴尉迟 ${ }^{1}$ 施柯杰 ${ }^{2}$ 赵岩 $^{1}$

(1. 上海大学数学系, 200444；2. 复旦大学附属中学, 200433)

题 1. 设正整数 $n \geq 2$, 实数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $\sum_{i=1}^{n}\left|a_{i}\right|+\left|\sum_{i=1}^{n} a_{i}\right|=1$, 求 $\sum_{i=1}^{n} a_{i}^{2}$的最小值和最大值.

(中国人民大学附属中学 张端阳 供题)

解 一方面, 由柯西不等式,

$$
\sqrt{n \sum_{i=1}^{n} a_{i}^{2}} \geq \sum_{i=1}^{n}\left|a_{i}\right|, \sqrt{n \sum_{i=1}^{n} a_{i}^{2}} \geq\left|\sum_{i=1}^{n} a_{i}\right|
$$

将两式相加得, $2 \sqrt{n \sum_{i=1}^{n} a_{i}^{2}} \geq 1$, 所以

$$
\sum_{i=1}^{n} a_{i}^{2} \geq \frac{1}{4 n}
$$

当 $a_{1}=a_{2}=\cdots=a_{n}=\frac{1}{2 n}$ 时可以取到等号.

另一方面, 对 $1 \leq j \leq n$, 由三角不等式,

$$
1=\sum_{i=1}^{n}\left|a_{i}\right|+\left|\sum_{i=1}^{n} a_{i}\right| \geq\left|\sum_{i \neq j} a_{i}-a_{j}-\sum_{i=1}^{n} a_{i}\right|=2\left|a_{j}\right|
$$

所以 $\left|a_{j}\right| \leq \frac{1}{2}$. 从而

$$
\sum_{i=1}^{n} a_{i}^{2} \leq \frac{1}{2} \sum_{i=1}^{n}\left|a_{i}\right| \leq \frac{1}{2}
$$

当 $a_{1}=\frac{1}{2}, a_{2}=-\frac{1}{2}, a_{3}=\cdots=a_{n}=0$ 时取到等号.

综上, $\sum_{i=1}^{n} a_{i}^{2}$ 的最小值为 $\frac{1}{4 n}$, 最大值为 $\frac{1}{2}$.

评注 最小值在所有变量都相等时取得, 可以用 Cauchy 不等式得出结果. 求最大值时, 先可以考虑三个变量的情形, 容易发现在 $a_{1}=\frac{1}{2}, a_{2}=-\frac{1}{2}, a_{3}=0$ 取到极值, 这促使我们考查查局部的性质, 即 $\left|a_{j}\right| \leq \frac{1}{2}$; 另外, 可以通过正负分离, 将绝对值问题转化, 进而求出最大值.

收稿日期: 2017-06-05； 修订日期: 2017-07-06.
题 2. 设 $n$ 是正整数, 有 $2^{n}$ 个质量两两不同的砝码, 称最重的砝码为 1 号砝码, 第二重的为 2 号砝码, 以此类推. 每次称量是指将现有的砝码分成个数相同的两组放在天平上称重, 然后留下较重的那组 (如果两组的质量相同, 随意留下一组即可). 这样经过 $n$ 次称重, 还剩下一个砝码, 问: 该砝码号码最大是多少?

(中国人民大学附属中学 张端阳 供题)

解 设砝码的质量分别为 $a_{1}<a_{2}<\cdots<a_{2^{n}}$. 称每次称量重的一组为 “胜组” , 轻的一组为 “败组”. 对 $1 \leq k \leq n$, 设第 $k$ 次称量胜组的平均质量为 $b_{k}$,最后剩下砝码的质量为 $a_{*}$. 则因为每次称量胜组的质量不小于败组的质量, 所以 $b_{1} \leq b_{2} \leq \cdots \leq b_{n-1} \leq b_{n}=a_{*}$. 于是对 $1 \leq k \leq n$,

$a_{*} \geq b_{k} \geq$ 第 $k$ 次称量败组的平均质量 $\geq$ 第 $k$ 次称量败组的最小质量.

因为 $a_{1}, a_{2}, \cdots, a_{2^{n}}$ 两两不同, 所以 $a_{*}$ 比 $n$ 个败组的最小质量都大, 所以 $a_{*}$的号码至多是 $2^{n}-n$.

下面进行构造.

因为平移不变性, 所以 $a_{1}, a_{2}, \cdots, a_{2^{n}}$ 中有负数也无妨. 对 $1 \leq i \leq 2^{n}$, 令 $a_{i}=-2^{2^{n}-i}$. 因为 $a_{i}<a_{i+1}+a_{i+2}+\cdots+a_{2^{n}}$, 所以每次称量含所剩最小质量的那组必为败组. 对 $1 \leq k \leq n$, 在第 $k$ 次称量中, 我们让 $a_{k}$ 和当时质量最大的 $2^{n-k}-1$ 个砝码同组, 则它们是败组. 这样最后只剩下 $a_{n+1}$, 其号码为 $2^{n}-n$.

综上, 所求最大值为 $2^{n}-n$.

评注 (1). 本题的关键点在逆向思维. 注意到最后一次称量剩下的砝码质量 $a_{*}$ 比败组的大, 进而推导出 $a_{*} \geq$ 第 $k$ 次称量胜组的平均质量 $\geq$ 第 $k$ 次称量败组的平均质量 $\geq$ 第 $k$ 次称量败组的最小质量, 从而 $a_{*}$ 至少是第 $2^{n}-n$ 个, 然后构造证明可以取到.

(2). 本题结果和如下 “十项全能” 问题类似:

设正整数 $n \geq 2$. 在一次比赛中有 $2^{n}$ 名选手参加 $n$ 个项目, 每个项目各选手的实力互不相同. 每赛完一个项目将淘汰成绩较差的一半选手, 这样 $n$ 个项目赛完后便能决出冠军. 称一个选手是 “冠军侯选人”，如果可适当安排比赛项目的顺序, 使得这名选手能成为冠军, 求冠军候选人数目的最大值.

题 3. 已知锐角 $\triangle A B C(A B>A C)$, 外心为 $O$, 内心为 $I$, 优弧 $\widehat{A B C}$ 和 $\widehat{A C B}$ 中点分别为 $M, N$. 直线 $M N, B C$ 交于点 $K$. 证明: $\angle A O I$ 与 $\angle A K C$ 相等或互补.

(湖南雅礼中学 黎宇乔 供题)



图 1



图 2



图 3

证明 设直线 $M B$ 与 $C N$ 交于点 $I_{A}$.

由于 $\angle I_{A} B C=\angle M A C=\angle M C A=\angle M B A$, 所以 $M I_{A}$ 为 $\triangle A B C$ 的外角平分线. 同理 $C N$ 为 $\triangle A B C$ 的外角平分线. 故点 $I_{A}$ 为 $\triangle A B C$ 关于点 $A$ 的旁心. 从而 $\triangle A B I \sim \triangle A I_{A} C$. 所以

$$
A B \cdot A C=A I \cdot A I_{A} .
$$

设 $H$ 为点 $A$ 在 $B C$ 边上的垂足, 设 $M N$ 交 $A I_{A}$ 于点 $T$.

注意到 $\widehat{A M}=\widehat{C M}, \overparen{A N}=\widehat{B N}$, 所以 $\angle A N M=\angle M N I_{A}, \angle A M N=$ $\angle B M N$. 因此 $\triangle M N I_{A} \cong \triangle M N A$.

故 $M N$ 为 $A I_{A}$ 的中垂线. 从而 $\angle A H B=\angle A T K=90^{\circ}$, 即 $A, T, H, K$ 共圆. 所以 $\angle A K C=\angle A T H$ (图 1 与图 2) 或 $\angle A K C=180^{\circ}-\angle A T H$ (图 3).

延长 $A O$ 交 $\odot O$ 于 $R$, 连结 $B R$. 则 $\triangle A B R \sim \triangle A H C$. 从而 $A O \cdot A H=$ $\frac{1}{2} A B \cdot A C$, 且 $\angle B A O=\angle H A C$, 由此得 $\angle O A I=\angle I A H$.

又因为 $T$ 为 $A I_{A}$ 中点, 结合 (1) 式得 $A I \cdot A T=A O \cdot A H$. 且 $\angle O A I=\angle I A H$,所以 $\triangle A O I \sim \triangle A T H$. 故 $\angle A O I=\angle A T H$.

因此 $\angle A O I=\angle A K C$ 或 $\angle A O I=180^{\circ}-\angle A K C$.

评注 此题要发现 $M B$ 和 $N C$ 的交点是 $\triangle A B C$ 的关于 $A$ 的旁心, 利用四点共圆和边成比例, 得到 $\triangle A O I \sim \triangle A T H$, 然后得到结论.

题 4. 已知正数 $a_{1}, a_{2}, \cdots, a_{n}$ 的和为 $n(n \geq 3)$, 并记 $s=a_{1}^{2}+a_{2}^{2}+\cdots+a_{n}^{2}$,证明:

$$
\sum_{i=1}^{n} \frac{1}{n-1+(n-2)\left(s-a_{i}^{2}\right)} \leq \frac{n}{(n-1)^{2}}
$$

(浙江杭州二中 赵斌 供题)
证明 原不等式等价于:

$$
\sum_{i=1}^{n} \frac{s-a_{i}^{2}}{n-1+(n-2)\left(s-a_{i}^{2}\right)} \geq \frac{n}{n-1}
$$

下证 (1). 由柯西不等式得,

$$
\left(n(n-1)+\sum_{i=1}^{n}(n-2)\left(s-a_{i}^{2}\right)\right)\left(\sum_{i=1}^{n} \frac{s-a_{i}^{2}}{n-1+(n-2)\left(s-a_{i}^{2}\right)}\right) \geq\left(\sum_{i=1}^{n} \sqrt{s-a_{i}^{2}}\right)^{2},
$$

化简便是

$$
\sum_{i=1}^{n} \frac{s-a_{i}^{2}}{n-1+(n-2)\left(s-a_{i}^{2}\right)} \geq \frac{\left(\sum_{i=1}^{n} \sqrt{s-a_{i}^{2}}\right)^{2}}{(n-1)(n+(n-2) s)}
$$

因此要证明 (1) 式只需证明

$$
\frac{\left(\sum_{i=1}^{n} \sqrt{s-a_{i}^{2}}\right)^{2}}{(n-1)(n+(n-2) s)} \geq \frac{n}{n-1}
$$

亦即只需证明

$$
\sum_{i=1}^{n}\left(s-a_{i}^{2}\right)+2 \sum_{1 \leq i<j \leq n} \sqrt{s-a_{i}^{2}} \cdot \sqrt{s-a_{j}^{2}} \geq n^{2}+n(n-2) s .
$$

再次利用柯西不等式得，

$$
\sqrt{s-a_{i}^{2}} \cdot \sqrt{s-a_{j}^{2}} \geq s-a_{i}^{2}-a_{j}^{2}+a_{i} a_{j}
$$

故

$$
\begin{aligned}
& \sum_{i=1}^{n}\left(s-a_{i}^{2}\right)+2 \sum_{1 \leq i<j \leq n} \sqrt{s-a_{i}^{2}} \\
\geq & \sum_{i=1}^{n}\left(s-a_{i}^{2}\right)+2 \sum_{1 \leq i<j \leq n}\left(s-a_{i}^{2}-a_{j}^{2}+a_{i} a_{j}\right) \\
= & (n-1) s+(n-1)(n-2) s+2 \sum_{1 \leq i<j \leq n} a_{i} a_{j} \\
= & (n-1)^{2} s+\left(\sum_{i=1}^{n} a_{i}\right)^{2}-\sum_{i=1}^{n} a_{i}^{2} \\
= & n^{2}+n(n-2) s .
\end{aligned}
$$

故 (2) 式得证.

评注 此题要先把分式型的上界问题转化为分式型的下界问题, 柯西不等式一般有以下两种用法:

设 $a_{i}, b_{i}>0, i=1, \ldots, n$. 其一是

$$
\left(\sum_{i=1}^{n} \frac{a_{i}}{b_{i}}\right)\left(\sum_{i=1}^{n} a_{i} b_{i}\right) \geq\left(\sum_{i=1}^{n} a_{i}\right)^{2}
$$

其二是

$$
\left(\sum_{i=1}^{n} \frac{a_{i}}{b_{i}}\right)\left(\sum_{i=1}^{n} b_{i}\right) \geq\left(\sum_{i=1}^{n} \sqrt{a_{i}}\right)^{2} .
$$

本题的难点在于只能使用第二种. 再利用柯西不等式将根式 $\sqrt{s-a_{i}^{2}} \cdot \sqrt{s-a_{j}^{2}}$化简即得结果.

题 5. 证明: 存在正整数 $r$, 使得恰有 2017 个正整数对 $(x, y, n)(n \neq 1)$, 使得 $x^{n}-y^{n}=r$.

(北京大学 吴茁 供题)

证明 取 $r=2^{k}, k$ 待定. 考虑 $x^{n}-y^{n}=r$ 的一组解 $\left(x_{0}, y_{0}, n_{0}\right)$.

若 $n_{0}$ 有奇素因子 $p$. 设 $n_{0}=p l$, 则 $\left(x_{0}^{l}\right)^{p}-\left(y_{0}^{l}\right)^{p}=2^{k}$. 令 $a=x_{0}^{l}, b=y_{0}^{l}$, 则 $a^{p}-b^{p}=2^{k}$.

设 $(a, b)=2^{m} t, t$ 为奇数. 则可设 $a=2^{m} a_{1}, b=2^{m} b_{1}$, 即 $a_{1}^{p}-b_{1}^{p}=2^{k-m p}$. $\left(a_{1}, b_{1}\right)$ 为奇数. 模 2 知 $a_{1}, b_{1}$ 均为奇数.

于是 $\left(a_{1}-b_{1}\right)\left(a_{1}^{p-1}+\cdots+b_{1}^{p-1}\right)=2^{k-m p}$, 因此

$$
a_{1}^{p-1}+\cdots+b_{1}^{p-1} \equiv \underbrace{1+1+\cdots+1}_{p \uparrow} \equiv 1 \quad(\bmod 2) .
$$

故 $a_{1}^{p-1}+\cdots+b_{1}^{p-1}=1$. 而 $a_{1}^{p-1}+\cdots+b_{1}^{p-1} \geq p \geq 3$. 矛盾.

若 $4 \mid n_{0}$. 设 $n_{0}=4 s, u=x_{0}^{s}, v=y_{0}^{s}$, 则 $u^{4}-v^{4}=2^{k}$.

设 $(u, v)=2^{m^{\prime}} t^{\prime}, t^{\prime}$ 为奇数, 令 $u=2^{m^{\prime}} u_{1}, v=2^{m^{\prime}} v_{1}$, 则 $u_{1}, v_{1}$ 为奇数. 故 $u_{1}^{2}+v_{1}^{2} \equiv 2(\bmod 4)$. 注意到

$$
u_{1}^{4}-v_{1}^{4}=\left(u_{1}^{2}+v_{1}^{2}\right)\left(u_{1}^{2}-v_{1}^{2}\right)=2^{k-4 m^{\prime}},
$$

故 $u_{1}^{2}+v_{1}^{2}=2$, 即有 $u_{1}=v_{1}=1$, 矛盾.

故 $n_{0}=2, x^{2}-y^{2}=2^{k}$. 设 $x-y=2^{m}, x+y=2^{k-m}$. 则

$$
x=2^{k-m-1}+2^{m-1}, \quad y=2^{k-m-1}-2^{m-1} .
$$

有解当且仅当 $m \geq 1, k>2 m$.

令 $k=4035$, 则 $m=1, \cdots, 2017$ 为全部 2017 组解. 即 $r=2^{4035}$ 符合条件,证毕!

评注 为了满足恰有 2017 个正整数对 $(x, y, n)$, 我们的目标是找到合适的正整数 $r$ 使得 $n$ 只能为 2 (因为 $x^{2}-y^{2}=(x+y)(x-y)$ 便于讨论满足要求的整数对的个数). 基于这样的想法, 可考虑 $r$ 为素数幂, 可以验证当 $r$ 为 2 的幂次满足 $n$ 只能为 2 .
题 6. 设 $A=\{x+\mathrm{i} y|| x|\leq 1| y \mid, \leq 1, x, y \in \mathbf{R}\}, z_{1}, z_{2}, \cdots, z_{6}$ 均属于 $A$ 且满足 $z_{1}+z_{2}+\cdots+z_{6}=0$. 证明: 存在 $1 \leq i<j<k \leq 6$ 使得 $z_{i}+z_{j}+z_{k} \in A$.

(上海大学 冷岗松 供题)

解法一 我们先证明一个重要的引理:

引理 $x_{1}, \cdots, x_{6}$ 为 $[-1,1]$ 上的实数, 且和为 0 , 则 $x_{1}, \ldots, x_{6}$ 中存在 12 个三元数组使得每一个三元数组的和仍属于区间 $[-1,1]$.

引理证明 不妨设 $x_{1}, \ldots, x_{6}$ 中非负数的个数不少于负数的个数(否则用 $-x_{1}, \ldots,-x_{6}$ 代替 $x_{1}, \ldots, x_{6}$ 即可). 则有以下 4 中情况:

(1) 若 $x_{1}, \ldots, x_{6}$ 中有 6 个非负数, 此时 $x_{1}=\cdots=x_{6} . x_{1}, \ldots, x_{6}$ 中任意三个的和均属于 $[-1,1]$. 故有 $\left(\begin{array}{l}6 \\ 3\end{array}\right)=20>12$ 符合要求的三元组.

(2) 若 $x_{1}, \ldots, x_{6}$ 中有 5 个非负数. 设为 $x_{1}<0 \leq x_{2} \leq \cdots \leq x_{6}$. 对任意 $x_{i}, x_{j}, x_{k} \in\left\{x_{1}, \ldots, x_{6}\right\}$, 若 $x_{1} \notin\left\{x_{i}, x_{j}, x_{k}\right\}$, 则

$$
0 \leq x_{i}+x_{j}+x_{k} \leq x_{2}+\cdots+x_{6}=-x_{1} \leq 1
$$

若 $x_{1} \in\left\{x_{i}, x_{j}, x_{k}\right\}$, 则

$$
-1+0+0 \leq x_{i}+x_{j}+x_{k} \leq x_{1}+\cdots+x_{6}=0 .
$$

即 $x_{1}+x_{j}+x_{k} \in[-1,1]$, 符合要求. 故有 $\left(\begin{array}{l}6 \\ 3\end{array}\right)=20>12$ 符合要求的三元组.

(3) 若 $x_{1}, \ldots, x_{6}$ 中有 4 个非负数. 设为 $x_{1} \leq x_{2}<0 \leq x_{3} \leq \cdots \leq x_{6}$. 则对任意 $x_{i}, x_{j} \in\left\{x_{3}, \ldots, x_{6}\right\}$, 有

$-1+0+0 \leq x_{1}+x_{i}+x_{j} \leq \frac{x_{1}+x_{2}}{2}+x_{i}+x_{j}=-\sum_{t=3}^{6} \frac{x_{t}}{2}+x_{i}+x_{j} \leq \frac{x_{i}+x_{j}}{2} \leq 1$.

故 $x_{1}+x_{i}+x_{j} \in[-1,1]$, 则

$$
x_{2}+x_{i}+x_{j}=-\left(x_{1}+\sum_{3 \leq t \leq 6, t \neq i, j} x_{t}\right) \in[-1,1]
$$

故有至少 $\left(\begin{array}{l}4 \\ 2\end{array}\right) \times 2=12$ 符合要求的三元组.

(4) 若 $x_{1}, \ldots, x_{6}$ 中有 3 个非负数. 设为 $x_{1} \leq x_{2} \leq x_{3}<0 \leq x_{4} \leq \cdots \leq x_{6}$,不妨设 $\left|x_{3}\right| \leq\left|x_{4}\right|$ (否则用 $-x_{1}, \ldots,-x_{6}$ 代替 $\left.x_{1}, \ldots, x_{6}\right)$. 注意到

$$
-1+0+0 \leq x_{2}+x_{5}+x_{6}=-x_{1}-x_{3}-x_{4} \leq 1-x_{3}+x_{3}=1
$$

即 $x_{2}+x_{5}+x_{6} \in[-1,1]$. 则对 $x_{4}, x_{5}, x_{6}$ 中任两个 $x_{i}, x_{j}$, 以及 $x_{1}, x_{2}$ 任一个 $x_{k}$.均有

$$
0+0-1 \leq x_{i}+x_{j}+x_{k} \leq x_{5}+x_{6}+x_{2} \leq 1,
$$

即 $x_{i}+x_{j}+x_{k} \in[-1,1]$.
对 $x_{4}, x_{5}, x_{6}$ 中任一个 $x_{i}$, 以及 $x_{1}, x_{2}$ 任一个 $x_{j}$. 均有

$$
x_{i}+x_{j}+x_{3}=-\left(\left(x_{4}+x_{5}+x_{6}-x_{i}\right)+\left(x_{1}+x_{2}-x_{j}\right)\right) \in[-1,1] .
$$

故有至少 $\left(\begin{array}{l}3 \\ 2\end{array}\right) \times\left(\begin{array}{l}2 \\ 1\end{array}\right)+\left(\begin{array}{l}3 \\ 1\end{array}\right) \times\left(\begin{array}{l}2 \\ 1\end{array}\right)=12$ 个符合要求的三元组.

综上, 总存在至少 12 个符合要求的三元组. 当 $x_{1}=x_{2}=-1, x_{3}=x_{4}=$ $x_{5}=x_{6}=\frac{1}{2}$ 时, 恰好只有 12 个符合要求的三元组, 故 12 是最优的. 引理证毕.

回到原题. 设 $z_{k}=a_{k}+\mathrm{i} b_{k}(k=1, \cdots, 6)$.

由条件知, $a_{k} \in[-1,1], \sum_{k=1}^{6} a_{k}=0$. 由引理知, 设

$$
\begin{aligned}
& A_{1}=\left\{(j, k, l) \mid 1 \leq j<k<l \leq 6, a_{j}+a_{k}+a_{l} \in[-1,1]\right\}, \\
& B_{1}=\left\{(j, k, l) \mid 1 \leq j<k \leq l \leq 6, b_{j}+b_{k}+b_{l} \in[-1,1]\right\},
\end{aligned}
$$

则 $\left|A_{1}\right| \geq 12,\left|B_{1}\right| \geq 12$.

另一方面, $A_{1}, B_{1}$ 均为 $S=\{(j, k, l) \mid 1 \leq j<k<l \leq 6\}$ 的子集. 且

$$
|S|=\mathrm{C}_{6}^{3}=20<\left|A_{1}\right|+\left|B_{1}\right| \text {, }
$$

故 $A_{1}$ 与 $B_{1}$ 交非空. 即存在 $1 \leq j<k<l \leq 6$ 使 $a_{j}+a_{k}+a_{l}, b_{j}+b_{k}+b_{l}$ 均属于 $[-1,1]$. 则 $z_{j}+z_{k}+z_{l} \in A$. 结论成立.

解法二 假设结论不成立, 即对任意 $1 \leq i<j<k \leq 6$, 均有 $z_{i}+z_{j}+z_{k}$ 所表示的点在正方形 $A$ 的外部. 若以正方形的一边所在的直线为边界的开半平面不包含正方形 $A$, 我们称该开半平面为这条边的外侧. 以下, 我们称正方形 $A$ 上边的外侧为上侧, 下边的外侧为下侧, 左边的外侧为左侧, 右边的外侧为右侧.我们先证明如下引理:

引理 对于给定的 $1 \leq i<j \leq 6$, 不存在 $1 \leq k_{1}<k_{2} \leq 6, k_{1} \neq, i, j$, 且 $k_{2} \neq, i, j$, 使得 $z_{i}+z_{j}+z_{k_{1}}, z_{i}+z_{j}+z_{k_{1}}$ 分别在正方形的对边的外侧.

若引理不成立, 则 $\left|\operatorname{Re}\left(z_{k_{1}}-z_{k_{2}}\right)\right|>2$ 或 $\left|\operatorname{Im}\left(z_{k_{1}}-z_{k_{2}}\right)\right|>2$, 这与 $A$ 的定义矛盾.引理证毕.

由引理知 $z_{1}+z_{2}+z_{3}, z_{1}+z_{2}+z_{4}, z_{1}+z_{2}+z_{5}$ 有两项在正方形同一边外侧, 不妨设 $z_{1}+z_{2}+z_{3}, z_{1}+z_{2}+z_{4}$ 在正方形的下侧, 则 $z_{4}+z_{5}+z_{6}$ 在正方形上侧. 由于 $z_{1}+z_{2}+z_{4}$ 在正方形的下侧, $z_{4}+z_{5}+z_{6}$ 在正方形上侧, 结合引理知, $z_{1}+z_{4}+z_{5}, z_{1}+z_{4}+z_{6}, z_{2}+z_{4}+z_{5}, z_{2}+z_{4}+z_{6}$ 既不在正方形的上侧, 也不在正方形的下侧, 从而它们在正方形的左侧或右侧. 又由引理知, 它们在正方形同侧, 不妨设为左侧, 则 $z_{2}+z_{3}+z_{6}$ 在正方形右侧, 又 $z_{2}+z_{4}+z_{6}$ 在正方形左侧,由引理知这是矛盾的, 从而结论成立.
评注 此题是将下述问题中的圆 $A$ 替换为正方形得到的:

设 $A=\left\{x+\left.\mathrm{i} y|| x\right|^{2}+|y|^{2} \leq 1, x, y \in \mathbf{R}\right\}, z_{1}, z_{2}, \cdots, z_{6}$ 均属于 $A$ 且满足 $z_{1}+z_{2}+\cdots+z_{6}=0$. 证明: 存在 $1 \leq i<j<k \leq 6$ 使得 $z_{i}+z_{j}+z_{k} \in A$.

解法一的关键点在于要先考查 $z_{1}, z_{2}, \cdots, z_{6}$ 实部或者虚部的性质, 有了引理之后, 由抽屉原理即得结论. 解法二是乐清乐成寄宿中学韩新录同学的证明,利用三角不等式得到引理, 进而对三元和和正方形的相对位置进行对称分析, 证明简洁美观。

