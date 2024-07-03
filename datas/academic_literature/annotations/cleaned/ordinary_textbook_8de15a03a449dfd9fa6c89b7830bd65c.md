数学新星网 $\%$ 解答展示

www.nsmath.cn/jdzs

# 第四十六期问题征解解答与点评 

张端阳

第一题 在 $\triangle A B C$ 中, $\Omega$ 是外接圆, $K$ 是 $A$ 的对径点, $L$ 是 $B C$ 边中线与 $\Omega$ 的不同于 $A$ 的交点. $\Omega$ 在 $K$ 处的切线交 $\triangle A B C$ 的 $A$ - 陪位中线于点 $P$, 直线 $P L$ 与 $\Omega$ 交于另一点 $N$. 设 $E$ 是 $B$ 关于 $A C$ 中点的对称点, $F$ 是 $C$ 关于 $A B$ 中点的对称点. 证明: $E, F, L, N$ 四点共圆.

(清华大学学生 严君啸 供题)

证明 (根据华南师大附中戴子一同学的解答整理):



由题意, $A E=A F=B C$ 且 $E, A, F$ 共线.

延长 $F E, L N$ 交于点 $X$, 只需证明

$$
X E \cdot X F=X L \cdot X N \text {. }
$$

设 $E F$ 与 $\Omega$ 的另一个交点是 $R$, 则

$$
X L \cdot X N=X A \cdot X R .
$$

又由 $A$ 是 $E F$ 的中点知

$$
X E \cdot X F=X A^{2}-A E^{2}
$$

所以只需证明

$$
X A^{2}-A E^{2}=X A \cdot X R
$$

即

$$
X A \cdot A R=B C^{2}
$$

设 $A P$ 与 $\Omega$ 交于点 $Q$, 由 $A L, A P$ 是等角线知 $Q L / / B C$. 设 $B C$ 的中点是 $M$,则 $Q, M, R$ 共线. 于是

$$
\begin{aligned}
X A \cdot A R & =Q L \cdot A R \cdot \frac{P A}{P Q}=Q L \cdot A R \cdot\left(\frac{K A}{K Q}\right)^{2} \\
& =Q L \cdot A R \cdot \frac{1}{\cos ^{2} \angle A K Q} \\
& =Q L \cdot \frac{1}{\cos \angle A L Q} \cdot A R \cdot \frac{1}{\cos \angle L A R} \\
& =2 L M \cdot 2 A M=4 B M \cdot C M=B C^{2} .
\end{aligned}
$$

综上, 命题得证.

评注 华南师大附中彭子晋, 东北师大附中吴竞航, 哈师大附中汤盛宣、郭旭,江苏省锡山高级中学孙昀, 賏州二中周胤帆, 深圳中学邓博文, 北大附中王子豪等同学也给出了本题的正确解答.

第二题 设素数 $p \equiv 1(\bmod 4)$, 非负实数 $x_{1}, x_{2}, \cdots, x_{p}$ 满足 $x_{1}+x_{2}+\cdots+x_{p}=$ 1. 证明:

$$
\sum_{1 \leq i<j \leq p}\left(\frac{i-j}{p}\right) x_{i} x_{j} \leq \frac{p-1}{2 p+6},
$$

其中 $\left(\frac{a}{p}\right)$ 为 Legendre 符号.

(海亮高级中学学生 陈镜之 供题)

## 证明 (根据供题者的解答整理):

记 $S=\left\{1 \leq i \leq p \mid x_{i}>0\right\}$. 取一组 $\left(x_{1}, x_{2}, \cdots, x_{p}\right)$, 使得在 $\sum_{1 \leq i<j \leq p}\left(\frac{i-j}{p}\right) x_{i} x_{j}$取到最大值的前提下, $|S|$ 取最小值.

下面证明, 此时对任意 $i, j \in S(i \neq j)$, 均有 $\left(\frac{i-j}{p}\right)=1 .(p \equiv 1(\bmod 4)$ 保证了 $\left.\left(\frac{i-j}{p}\right)=\left(\frac{j-i}{p}\right)\right)$

事实上, 若存在 $i_{0}, j_{0} \in S\left(i_{0} \neq j_{0}\right)$ 使得 $\left(\frac{i_{0}-j_{0}}{p}\right) \neq 1$, 则用 $\left(x_{1}^{\prime}, x_{2}^{\prime}, \cdots, x_{p}^{\prime}\right)$ 代替 $\left(x_{1}, x_{2}, \cdots, x_{p}\right)$, 其中 $x_{i_{0}}^{\prime}=x_{i_{0}}+\delta, x_{j_{0}}^{\prime}=x_{j_{0}}-\delta$, 其余不变.

这时 $\sum_{1 \leq i<j \leq p}\left(\frac{i-j}{p}\right) x_{i}^{\prime} x_{j}^{\prime}$ 是关于 $\delta$ 的二次函数, 二次项系数 $\left(\frac{i_{0}-j_{0}}{p}\right)(-1)=1$.所以最大值在 $\delta$ 位于边界, 即 $x_{i_{0}}^{\prime}$ 或 $x_{j_{0}}^{\prime}$ 中有一个为 0 时取得, 这与 $|S|$ 的最小性矛盾!
故

$$
\sum_{1 \leq i<j \leq p}\left(\frac{i-j}{p}\right) x_{i} x_{j}=\sum_{\substack{i, j \in S \\ i<j}} x_{i} x_{j} \leq \frac{|S|-1}{2|S|}\left(\sum_{i \in S} x_{i}\right)^{2}=\frac{|S|-1}{2|S|} .
$$

下面只需证明 $|S| \leq \frac{p+3}{4}$.

因为对任意 $i, j \in S(i \neq j)$, 均有 $\left(\frac{i-j}{p}\right)=1$, 所以在模 $p$ 的意义下,

$$
S+(-S)=\{a-b \mid a, b \in S\}
$$

包含于模 $p$ 的全体二次剩余并上 $\{0\}$. 结合 Cauchy-Davenport 定理得,

$$
\frac{p+1}{2} \geq|S+(-S)| \geq \min \{p,|S|+|-S|-1\}=2|S|-1
$$

故 $|S| \leq \frac{p+3}{4}$.

评注 (1). 本题源于对 2013 年韩国数学奥林匹克决赛第三题的讨论:

设整数 $n \geq 2$, 记 $T=\{(i, j)|1 \leq i<j \leq n, i| j\}$. 设非负实数 $x_{1}, x_{2}, \cdots, x_{n}$满足 $x_{1}+x_{2}+\cdots+x_{n}=1$. 求 $\sum_{(i, j) \in T} x_{i} x_{j}$ 的最大值.

深圳中学姜志城同学指出对于这类问题有一个一般的引理:

设 $G(V, E)$ 是一个简单图, $V=\{1,2, \cdots, n\}$. 设非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $x_{1}+x_{2}+\cdots+x_{n}=1$, 则

$$
\sum_{i j \in E} x_{i} x_{j} \leq \frac{s-1}{2 s}
$$

其中 $s$ 是 $G$ 中最大团的顶点数.

证明方法与解答前半部分的调整法一致.

(2). 本题在 $p=5, x_{1}=x_{2}=\frac{1}{2}, x_{3}=x_{4}=x_{5}=0$ 时可以取到等号.

在一般情形, 浙江省慈溪中学胡洁洋同学指出可以证明 $|S| \leq \sqrt{p}$, 从而本题可以加强为 $\frac{\sqrt{p}-1}{2 \sqrt{p}}$.

事实上, 设在模 $p$ 的意义下 $S=\left\{a_{1}, a_{2}, \cdots, a_{s}\right\}$, 其中 $1 \leq a_{1}<a_{2}<\cdots<a_{s} \leq$ $p$. 任取一个模 $p$ 的二次非剩余 $m$, 则对任意 $1 \leq i, j \leq s(i \neq j)$, 都有 $m\left(a_{i}-a_{j}\right)$ 是模 $p$ 的二次非剩余. 于是对任意 $0 \leq u \leq p-1, u+m a_{1}, u+m a_{2}, \cdots, u+m a_{s}$ 中至多有一个属于 $S$. 而当 $u$ 遍历 $0 \sim p-1$ 时, 对每个 $1 \leq i \leq s, u+m a_{i}$ 均遍历模 $p$ 的完全剩余系, 其中恰有 $s$ 个属于 $S$. 这样, $s \cdot s \leq p$, 故 $s \leq \sqrt{p}$.

(3). 华南师大附中戴子一, 北大附中王子豪等同学也给出了本题的正确解答.
第三题 设 $n$ 是正整数. 有一个 $n \times n$ 的棋盘, 初始时所有格都是白色的. 每次操作可以选择一个格子, 改变它及 ${ }^{1}$ 与它有公共边的所有格子的颜色 (白变黑、黑变白). 同一个格子不允许被选择两次.

我们要通过一系列操作使所有格都变成黑色, 设有 $a_{n}$ 种操作过程可以实现目标. (若两种操作过程可通过交换操作顺序得到, 则视为同一种) 证明:

(1) 对任意正整数 $n$, 都有 $a_{n} \geq 1$;

(2) 存在正实数 $c$, 使得对无穷多个 $n$ 有 $a_{n} \geq 2^{c n}$.

(北京大学学生 陈冠伊 供题)

## 证明 (根据供题者的解答整理):

(1) 我们将问题暂时抽象为一个更一般的简单图 $G(V, E)$ 上的操作问题: 每个顶点有黑白两色之分, 且每次可以对一个顶点操作, 改变它及与它相邻顶点的颜色, 并考虑有无将全白顶点变为全黑顶点的操作.

将顶点标号为 $1,2, \cdots, p$, 且对 $1 \leq i \leq p$, 设顶点 $i$ 被操作了 $x_{i}$ 次. 则可以定义 $\mathbb{F}_{2}$ 上的矩阵 $A=\left\{a_{i j}\right\}(1 \leq i, j \leq p)$, 满足 $a_{i j}$ 非零当且仅当对顶点 $i$ 进行操作会改变顶点 $j$ 的颜色.

根据操作的性质, 此矩阵主对角元均为 1 (即 $a_{i i}=1$ ) 且关于主对角线对称 （即 $a_{i j}=a_{j i}$ ). 而一种操作序列可以与操作向量 $x=\left(x_{1}, x_{2}, \cdots, x_{p}\right)^{T} \in \mathbb{F}_{2}^{p}$ 一一对应, $x_{i}$ 非零当且仅当顶点 $i$ 被操作. 则最终的状态可以表示为

$$
y=A x=\left(y_{1}, y_{2}, \cdots, y_{p}\right)^{T} \in \mathbb{F}_{2}^{p}
$$

其中 $y_{i}$ 非零当且仅当顶点 $i$ 最终变为黑色. 记 $y_{0}=(1,1, \cdots, 1)^{T} \in \mathbb{F}_{2}^{p}$, 则只需证明加强命题: 只要 $\mathbb{F}_{2}$ 上的 $p \times p$ 方阵 $A$ 对角元全为 1 且对称, 则方程 $A x=y_{0}$ 至少有一个解.

事实上, 初等行变换将增广矩阵变为简化行阶梯形之后, 每一行为原先行的线性组合, 亦即若干个行的和（注意系数均为 $\mathbb{F}_{2}$ 的）, 只要简化行阶梯形中不出现形如 $(0, \cdots, 0,1)$ 的行, 方程便有解. 若这样的行出现, 则最后一位为奇数个 1 相加得到, 说明 $A$ 中存在奇数行之和为零向量. 特别地, 这奇数行与同它们编号相同的奇数列交出的子方阵的行和为零向量. 但是这个子方阵对角元全为 1 且对称, 其所有元素之和为奇数, 矛盾!

(2) 因为所有实现目标的操作对应的向量, 都由一个实现目标的操作对应的向量与一个保持棋盘颜色不变的操作对应的向量相加得到, 所以 $a_{n}$ 即保持棋盘颜色[^0]不变的操作方法数. 以下求这类操作方法的个数.

定义矩阵 $M=\left\{m_{i j}\right\}(1 \leq i, j \leq n)$ 如下:

$$
m_{i j}= \begin{cases}1, & |i-j| \leq 1 ; \\ 0, & \text { 其他. }\end{cases}
$$

设第一行的操作对应向量 $x^{(0)}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{T} \in \mathbb{F}_{2}^{n}$, 第一行的操作完毕之后, 第一行的状态为 $M x^{(0)}$. 而仅有第二行的操作能够改变第一行的元素, 且为一一对应的改变关系, 于是为使第一行在操作后不变, 第二行的操作应对应向量 $M x^{(0)}$.

第二行的操作完毕之后, 第二行的状态 (被第一行和第二行的操作影响) 为 $\left(M^{2}+I\right) x^{(0)}$. 而仅有第三行的操作能够改变第二行的元素, 且为一一对应的改变关系, 于是为使第二行在操作后不变, 第三行的操作应对应向量 $\left(M^{2}+I\right) x^{(0)}$.

一般地, 记第 $i$ 行的操作完毕之后, 第 $i$ 行的状态为 $x^{(i)}=f_{i}(M) x^{(0)}$, 则有如下递推公式 (注意系数均为 $\mathbb{F}_{2}$ 的):

$$
f_{1}(x)=x, f_{2}(x)=x^{2}-1, f_{i+2}(x)=x f_{i+1}(x)-f_{i}(x)(i \geq 1)
$$

最终使整个棋盘颜色不变的解即为满足 $0=x^{(n)}=f_{n}(M) x^{(0)}$ 的 $x^{(0)}$. 于是只要能对某些 $n$ 计算 $f_{n}(M)$ 的零化度 (零空间的维数), 问题就迎刃而解.

以下取 $n=3 \cdot 2^{k}-1$, 其中 $k$ 为大于 1 的整数. 我们先证明两个引理说明这样的 $n$ 符合题意.

引理 1 在 $\mathbb{F}_{2}$ 上, $f_{n}(x)=x^{2^{k}-1}(x-1)^{2^{k+1}}$.

证明 记 $x=u+\frac{1}{u}$, 则归纳易知 $f_{n}(x)=\frac{u^{n+1}-\frac{1}{u n+1}}{u-\frac{1}{u}}$. 于是只需在系数模 2 的意义下, 证明

$$
\frac{u^{n+1}-\frac{1}{u^{n+1}}}{u-\frac{1}{u}}=\left(u+\frac{1}{u}\right)^{2^{k}-1}\left(u+\frac{1}{u}-1\right)^{2^{k+1}}
$$

即

$$
u^{n+1}-\frac{1}{u^{n+1}}=\left(u+\frac{1}{u}\right)^{2^{k}}\left(u+\frac{1}{u}-1\right)^{2^{k+1}} .
$$

事实上, 由 $(x+y)^{2^{k}}=x^{2^{k}}+y^{2^{k}}$ 得,

$$
\begin{aligned}
\left(u+\frac{1}{u}\right)^{2^{k}}\left(u+\frac{1}{u}-1\right)^{2^{k+1}} & =\left(u+\frac{1}{u}\right)^{2^{k}}\left(\left(u+\frac{1}{u}\right)^{2^{k+1}}-1\right) \\
& =\left(u+\frac{1}{u}\right)^{3 \cdot 2^{k}}-\left(u+\frac{1}{u}\right)^{2^{k}} \\
& =\left(u^{2^{k}}+\frac{1}{u^{2^{k}}}\right)^{3}-\left(u^{2^{k}}+\frac{1}{u^{2^{k}}}\right)
\end{aligned}
$$

$$
=u^{3 \cdot 2^{k}}+\frac{1}{u^{3 \cdot 2^{k}}}=u^{n+1}-\frac{1}{u^{n+1}} .
$$

由此引理 1 证毕.

引理 $2 M$ 的特征多项式为 $f_{n}(x-1), M$ 与 $M-I$ 的零化度均为 1 , 且 $f_{n}(M)$的零化度至少为 $2\left(2^{k}-1\right)$.

证明 记 $M=M_{n}$, 考察 $g_{n}(x):=\operatorname{det}\left(x I_{n}-M_{n}\right)$ 的递推性质. 由行列式的定义及 Laplace 展开得,

$$
\begin{aligned}
g_{1}(x) & =x-1, g_{2}(x)=(x-1)^{2}-1, \\
g_{i+2}(x) & =(x-1) g_{i+1}(x)-g_{i}(x)(i \geq 1)
\end{aligned}
$$

于是 $\mathbb{F}_{2}$ 上的多项式序列 $\left\{f_{i}(x-1)\right\},\left\{g_{i}(x)\right\}$ 的初值和递推公式相同, 故为相同的多项式序列.

通过在前四行进行初等行变换, $M_{n}$ 的零化度可以转化为 $M_{n-3}$ 的零化度. 因为 $n \equiv 2(\bmod 3)$, 所以最终转化为 $M_{2}$ 的零化度, 即为 1 .

$M_{n}-I_{n}$ 的非零元仅为两条次对角线的元素, 可分别计算奇数行偶数列的子矩阵和偶数行奇数列的子矩阵的零化度, 由 $n$ 是奇数知结果也为 1 .

由上面的论证及引理 1 得,

$$
0=g_{n}(M)=f_{n}(M-I)=(M-I)^{2^{k}-1} M^{2^{k+1}}
$$

的零化度为 $n=\left(2^{k}-1\right)+2^{k+1}$. 熟知任意有限个方阵的零化度之和不小于它们相乘所得方阵的零化度, 所以 $(M-I)^{2^{k}-1} M^{2^{k}-1}$ 的零化度恰为 $n-\left(2^{k}+1\right)=2\left(2^{k}-1\right)$.又由引理 1 知 $(M-I)^{2^{k}-1} M^{2^{k}-1}$ 是 $f_{n}(M)$ 的因式, 所以 $f_{n}(M)$ 的零化度至少为 $2\left(2^{k}-1\right)$. 引理 2 得证.

回到原题. 设 $f_{n}(M)$ 的零化度为 $N$, 由引理 2 可得

$$
N \geq 2\left(2^{k}-1\right)>\frac{1}{2}\left(3 \cdot 2^{k}-1\right)=\frac{1}{2} n .
$$

因为使得整个棋盘颜色不变的操作有 $2^{N}$ 种, 所以 $a_{n}=2^{N} \geq 2^{\frac{1}{2} n}$, 故取 $c=\frac{1}{2}$即可.

第四题 设函数 $f: \mathbb{N}_{+} \rightarrow \mathbb{R}_{\geq 0}$, 满足 $f(1)=1$, 且对每个正整数 $n$, 都有

$$
f(n)=\sum_{p \text { 是素数 }} f(n p) \text {. }
$$

证明: 对任意正整数 $n, f\left(n^{2}\right) \geq f(n)^{2}$.

(南加州大学 邓显 供题)

## 证明 1 (根据海亮高级中学 ${ }^{2}$ 赵斌老师的解答整理):

设 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}$, 其中 $p_{1}, p_{2}, \cdots, p_{k}$ 是不同的素数, $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{k}$ 是正整数.

记 $m=\alpha_{1}+\alpha_{2}+\cdots+\alpha_{k}$, 由条件,

$$
\begin{gathered}
f(1)=\sum_{q_{1}, q_{2}, \cdots, q_{2 m} \text { 是素数 }} f\left(q_{1} q_{2} \cdots q_{2 m}\right), \\
f(n)=\sum_{q_{1}, q_{2}, \cdots, q_{m} \text { 是素数 }} f\left(q_{1} q_{2} \cdots q_{m} p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}\right), \\
f\left(n^{2}\right)=f\left(p_{1}^{2 \alpha_{1}} p_{2}^{2 \alpha_{2}} \cdots p_{k}^{2 \alpha_{k}}\right) .
\end{gathered}
$$

故 $f\left(n^{2}\right) \geq f(n)^{2}$ 等价于

$$
\begin{aligned}
& f\left(p_{1}^{2 \alpha_{1}} p_{2}^{2 \alpha_{2}} \cdots p_{k}^{2 \alpha_{k}}\right) \sum_{q_{1}, q_{2}, \cdots, q_{2 m} \text { 是素数 }} f\left(q_{1} q_{2} \cdots q_{2 m}\right) \\
\geq & \left(\sum_{q_{1}, q_{2}, \cdots, q_{m} \text { 是素数 }} f\left(q_{1} q_{2} \cdots q_{m} p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}\right)\right)^{2} .
\end{aligned}
$$

由均值不等式, 这只需证明对任意 $0<c<1$ 及满足 $a b=\frac{1}{4}$ 的正实数 $a, b$, 都有

$$
\begin{aligned}
& c \sum_{\substack{q_{1}, q_{2}, \cdots, q_{m} \text { 是素数 }}} f\left(q_{1} q_{2} \cdots q_{m} p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}\right) \\
\leq & a f\left(p_{1}^{2 \alpha_{1}} p_{2}^{2 \alpha_{2}} \cdots p_{k}^{2 \alpha_{k}}\right)+b \sum_{q_{1}, q_{2}, \cdots, q_{2 m} \text { 是素数 }} f\left(q_{1} q_{2} \cdots q_{2 m}\right) .
\end{aligned}
$$

取 $l$ 充分大, 只需证明

$$
\begin{aligned}
& c \sum_{q_{1}, q_{2}, \cdots, q_{m} \text { 是素数 } r_{1}, r_{2}, \cdots, r_{l} \text { 是素数 }} f\left(q_{1} q_{2} \cdots q_{m} p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}} r_{1} r_{2} \cdots r_{l}\right) \\
& \leq a \sum_{\substack{r_{1}, r_{2}, \cdots, r_{l} \text { 是素数 }\\
}} f\left(p_{1}^{2 \alpha_{1}} p_{2}^{2 \alpha_{2}} \cdots p_{k}^{2 \alpha_{k}} r_{1} r_{2} \cdots r_{l}\right) \\
& \quad+b \sum_{\substack{ \\
q_{1}, q_{2}, \cdots, q_{2 m} \text { 是素数 } r_{1}, r_{2}, \cdots, r_{l} \text { 是素数 }}} f\left(q_{1} q_{2} \cdots q_{2 m} r_{1} r_{2} \cdots r_{l}\right) .
\end{aligned}
$$

对任意素数 $p_{1}, p_{2}, \cdots, p_{N}, N>k$, 考察 $f\left(p_{1}^{\beta_{1}} p_{2}^{\beta_{2}} \cdots p_{N}^{\beta_{N}}\right)$ (其中 $\beta_{1}+\beta_{2}+\cdots+$ $\left.\beta_{N}=2 m+l\right)$ 在上式左、右两边出现的次数.

在左边出现的次数为

$$
c \cdot \frac{(l+m) !}{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) ! \beta_{k+1} ! \cdots \beta_{N} !},
$$

其中若存在 $1 \leq i \leq k$ 使 $\beta_{i}<\alpha_{i}$, 则次数为 0 .

## ${ }^{2}$ 上期解答中写错了赵老师的工作单位, 在此更正

在右边出现的次数为

$$
a \cdot \frac{l !}{\left(\beta_{1}-2 \alpha_{1}\right) ! \cdots\left(\beta_{k}-2 \alpha_{k}\right) ! \beta_{k+1} ! \cdots \beta_{N} !}+b \cdot \frac{(l+2 m) !}{\beta_{1} ! \cdots \beta_{N} !} .
$$

故只需证明

$$
\begin{aligned}
& c \cdot \frac{(l+m) !}{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) ! \beta_{k+1} ! \cdots \beta_{N} !} \\
\leq & a \cdot \frac{l !}{\left(\beta_{1}-2 \alpha_{1}\right) ! \cdots\left(\beta_{k}-2 \alpha_{k}\right) ! \beta_{k+1} ! \cdots \beta_{N} !}+b \cdot \frac{(l+2 m) !}{\beta_{1} ! \cdots \beta_{N} !}
\end{aligned}
$$

即

$$
\begin{aligned}
c & \leq \frac{a}{(l+1) \cdots(l+m)} \cdot \frac{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) !}{\left(\beta_{2}-2 \alpha_{1}\right) ! \cdots\left(\beta_{k}-2 \alpha_{k}\right) !} \\
& +b \cdot \frac{(l+2 m) !}{(l+m) !} \cdot \frac{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) !}{\beta_{1} ! \cdots \beta_{k} !}
\end{aligned}
$$

令 $l$ 充分大, 使得

$\frac{a}{(l+1) \cdots(l+m)}\left[\frac{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) !}{\left(\beta_{1}-2 \alpha_{1}\right) ! \cdots\left(\beta_{k}-2 \alpha_{k}\right) !}-\frac{\beta_{1} ! \cdots \beta_{k} !}{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) !}\right]>c-1$.

又由均值不等式,

$$
\begin{aligned}
& \quad \frac{a}{(l+1) \cdots(l+m)} \cdot \frac{\beta_{1} ! \cdots \beta_{k} !}{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) !} \\
& +b \cdot \frac{(l+2 m) !}{(l+m) !} \cdot \frac{\left(\beta_{1}-\alpha_{1}\right) ! \cdots\left(\beta_{k}-\alpha_{k}\right) !}{\beta_{1} ! \cdots \beta_{k} !} \\
& >2 \sqrt{a b}=1,
\end{aligned}
$$

故相加即证.

## 证明 2 (根据北京大学廖昱博同学的解答整理):

先证明两个引理.

引理 1 对任意整数 $n \geq 2$, 任意整数 $0 \leq i \leq n$, 均有

$$
\mathrm{C}_{n}^{i}\left(\mathrm{C}_{n-2}^{i}+t \mathrm{C}_{n}^{i}\right) \geq\left(\mathrm{C}_{n-1}^{i}\right)^{2},
$$

其中 $t=\frac{1}{4(n-1)}$, 并规定 $\mathrm{C}_{n-2}^{n-1}=\mathrm{C}_{n-2}^{n}=\mathrm{C}_{n-1}^{n}=0$.

证明 若 $i=n$, 则右边等于 0 , 结论成立.

若 $0 \leq i \leq n-1$, 则 $\mathrm{C}_{n}^{i}=\frac{n}{n-i} \mathrm{C}_{n-1}^{i}, \mathrm{C}_{n-2}^{i}=\frac{n-i-1}{n-1} \mathrm{C}_{n-1}^{i}$, 于是只需证明

$$
\frac{n}{n-i}\left(\frac{n-i-1}{n-1}+t \cdot \frac{n}{n-i}\right) \geq 1 .
$$

这等价于 $1-\frac{i}{n-1}+t \cdot \frac{n}{n-i} \geq 1-\frac{i}{n}$, 即 $t \cdot \frac{n}{n-i} \geq \frac{i}{n(n-1)}$, 即 $\frac{1}{4} n^{2} \geq i(n-i)$, 成立. 引理 1 证毕.

引理 2 若无穷非负实数列 $a_{0}, a_{1}, a_{2}, \cdots$ 满足对任意非负整数 $j, k$, 均有

$$
\sum_{i=0}^{k}(-1)^{i} \mathrm{C}_{k}^{i} a_{i+j} \geq 0
$$

则 $a_{0} a_{2} \geq a_{1}^{2}$.

证明 对任意取定的整数 $n \geq 2$, 记

$$
b_{n-k}=\sum_{i=0}^{k}(-1)^{i} \mathrm{C}_{k}^{i} a_{n-k+i}, 0 \leq k \leq n
$$

由条件知 $b_{0}, b_{1}, \cdots, b_{n} \geq 0$.

容易证明 $a_{n-k}=\sum_{i=0}^{k} \mathrm{C}_{k}^{i} b_{n-i}$, 所以

$$
a_{0}=\sum_{i=0}^{n} \mathrm{C}_{n}^{i} b_{n-i}, \quad a_{1}=\sum_{i=0}^{n} \mathrm{C}_{n-1}^{i} b_{n-i}, \quad a_{2}=\sum_{i=0}^{n} \mathrm{C}_{n-2}^{i} b_{n-i} .
$$

记 $t=\frac{1}{4(n-1)}$, 由引理 1 及柯西不等式,

$$
\begin{aligned}
a_{0}\left(a_{2}+t a_{0}\right) & =\left(\sum_{i=0}^{n} \mathrm{C}_{n}^{i} b_{n-i}\right)\left(\sum_{i=0}^{n}\left(\mathrm{C}_{n-2}^{i}+t \mathrm{C}_{n}^{i}\right) b_{n-i}\right) \\
& \geq\left(\sum_{i=0}^{n} \sqrt{\mathrm{C}_{n}^{i}\left(\mathrm{C}_{n-2}^{i}+t \mathrm{C}_{n}^{i}\right)} b_{n-i}\right)^{2} \\
& \geq\left(\sum_{i=0}^{n} \mathrm{C}_{n-1}^{i} b_{n-i}\right)^{2}=a_{1}^{2},
\end{aligned}
$$

即

$$
a_{0}\left(a_{2}+\frac{1}{4(n-1)} a_{0}\right) \geq a_{1}^{2}
$$

令 $n \rightarrow \infty$ 得, $a_{0} a_{2} \geq a_{1}^{2}$. 引理 2 证毕.

回到原题. 当 $n=1$ 时显然成立, 下设 $n \geq 2$.

定义无穷非负实数列 $\left\{a_{i}\right\}: a_{i}=f\left(n^{i}\right), i=0,1,2, \cdots$.

因为 $a_{0}=f(1)=1, a_{1}=f(n), a_{2}=f\left(n^{2}\right)$, 所以只需证明 $a_{0} a_{2} \geq a_{1}^{2}$. 由引理 2,只需验证对任意非负整数 $j, k$, 均有 $\sum_{i=0}^{k}(-1)^{i} \mathrm{C}_{k}^{i} f\left(n^{i+j}\right) \geq 0$.

下面对 $k$ 归纳证明更强的结论：对任意正整数 $j$, 均有

$$
\sum_{i=0}^{k}(-1)^{i} \mathrm{C}_{k}^{i} f\left(n^{i} \cdot j\right) \geq 0
$$

当 $k=0$ 时, 即为 $f(j) \geq 0$, 成立. 假设 $k-1$ 时成立, 来看 $k$ 时的情形.

记 $g(j)=\sum_{i=0}^{k-1}(-1)^{i} \mathrm{C}_{k-1}^{i} f\left(n^{i} \cdot j\right)$, 由归纳假设知 $g(j) \geq 0$.

对每个 $f$ 用条件得, $g(m)=\sum_{p \text { 是素数 }} g(m p)$, 所以对任意素数 $p$ 有 $g(m) \geq g(m p)$.将 $n$ 分解为素因子之积, 反复利用上式可知 $g(m) \geq g(m n)$. 故

$$
\sum_{i=0}^{k}(-1)^{i} \mathrm{C}_{k}^{i} f\left(n^{i} \cdot j\right)=\sum_{i=0}^{k}(-1)^{i}\left(\mathrm{C}_{k-1}^{i}+\mathrm{C}_{k-1}^{i-1}\right) f\left(n^{i} \cdot j\right)
$$

$$
\begin{aligned}
& =\sum_{i=0}^{k-1}(-1)^{i} \mathrm{C}_{k-1}^{i} f\left(n^{i} \cdot j\right)+\sum_{i=0}^{k-1}(-1)^{i+1} \mathrm{C}_{k-1}^{i} f\left(n^{i+1} \cdot j\right) \\
& =g(j)-g(j n) \geq 0
\end{aligned}
$$

归纳证毕.

## 证明 3 (根据供题者的解答整理):

设 $n$ 的素因子分解为 $n=q_{1} \cdots q_{m}$. 由条件易知对任意正整数 $r$, 有

$$
\sum_{p_{1}, \cdots, p_{r} \text { 是素数 }} f\left(p_{1} \cdots p_{r}\right)=1
$$

因此对正整数 $N$, 存在素数值随机变量 $X_{1}, \cdots, X_{N}$, 满足

$$
P\left(X_{1}=p_{1}, \cdots, X_{N}=p_{N}\right)=f\left(p_{1} \cdots p_{N}\right)
$$

对所有素数 $p_{1}, \cdots, p_{N}$ 成立.

取 $N>(2 m)^{2}$, 定义

$$
G_{N, n}(X)=G_{N, n}\left(X_{1}, \cdots, X_{N}\right)=\prod_{i=1}^{m}\left(\frac{1}{N} \sum_{j=1}^{N} \mathbf{1}_{q_{i}}\left(X_{j}\right)\right)
$$

其中 $\mathbf{1}_{q_{i}}\left(X_{j}\right)$ 在 $X_{j}=q_{i}$ 时取值为 1 , 否则取值为 0 .

显然 $G_{N, n^{2}}(X)=G_{N, n}(X)^{2}$, 由柯西不等式,

$$
\mathbb{E}\left[G_{N, n^{2}}(X)\right] \geq \mathbb{E}\left[G_{N, n}(X)\right]^{2}
$$

以下只需证明

$$
\lim _{N \rightarrow \infty} \mathbb{E}\left[G_{N, n}(X)\right]=f(n)
$$

这是因为同理可证此等式对 $n^{2}$ 成立, 再取极限即得 $f\left(n^{2}\right) \geq f(n)^{2}$.

由定义可得

$$
\mathbb{E}\left[G_{N, n}(X)\right]=\frac{1}{N^{m}} \sum_{1 \leq j_{1}, \cdots, j_{m} \leq N} P\left(X_{j_{i}}=q_{i}, 1 \leq i \leq m\right)
$$

右边求和共有 $N^{m}$ 项, 每项均属于 $[0,1]$, 其中满足各 $j_{i}(1 \leq i \leq m)$ 互不相同的项数为 $(N)_{m}:=N(N-1) \cdots(N-m+1)$. 于是有两 $j_{i}$ 相同的项数为

$$
N^{m}-(N)_{m}=N^{m}\left[1-\prod_{j=1}^{m-1}\left(1-\frac{j}{N}\right)\right] \leq N^{m} \sum_{j=1}^{m-1} \frac{j}{N}<m^{2} N^{m-1}
$$

对满足各 $j_{i}(1 \leq i \leq m)$ 互不相同的每一项, 记 $A=\left\{j_{1}, \cdots, j_{m}\right\} \subseteq$ $\{1,2, \cdots, N\}$, 则

$$
P\left(X_{j_{i}}=q_{i}, 1 \leq i \leq m\right)=\sum_{\left(p_{j}: j \notin A\right)} P\left(X_{j_{i}}=q_{i}, 1 \leq i \leq m ; X_{j}=p_{j}, \forall j \notin A\right)
$$

$$
\begin{aligned}
& =\sum_{\left(p_{j}: j \notin A\right)} f\left(q_{1} \cdots q_{m} \cdot \prod_{j \notin A} p_{j}\right) \\
& =f\left(q_{1} \cdots q_{m}\right)=f(n),
\end{aligned}
$$

最后一步用到了条件.

这样, 结合 $0 \leq f(n) \leq 1$ 得,

$$
\begin{aligned}
\left|\mathbb{E}\left[G_{N, n}(X)\right]-f(n)\right| & \leq\left(1-\frac{(N)_{m}}{N^{m}}\right) f(n)+\frac{N^{m}-(N)_{m}}{N^{m}} \\
& \leq 2 \cdot \frac{N^{m}-(N)_{m}}{N^{m}} \leq \frac{2 m^{2}}{N} \rightarrow 0(N \rightarrow \infty)
\end{aligned}
$$

综上, 命题得证.

评注 (1). 这里的 $f$ 本质上是满足

$$
\sum_{p} g(p)=1
$$

的完全积性函数 $g$ 的 “加权平均” 或凸组合. 严格地说, 存在满足上述条件的全体完全积性函数 $g$ 组成的集合 $\mathcal{M}$ 上的概率测度 $\mu$, 使得

$$
f(n)=\int_{\mathcal{M}} g(n) \mathrm{d} \mu(g)
$$

因为对任何 $g$ 都有 $g\left(n^{2}\right)=g(n)^{2}$, 所以由柯西不等式即得 $f\left(n^{2}\right) \geq f(n)^{2}$.

注意到证明中构造的随机变量 $\left(X_{j}\right)$ 的分布在任意重排

$$
\left(X_{1}, \cdots, X_{N}\right) \mapsto\left(X_{\pi(1)}, \cdots, X_{\pi(N)}\right)
$$

下不变, 实际上我们可以将它们延拓成无穷随机变量序列 $\left(X_{1}, X_{2}, \cdots\right)$ 并使其满足同样性质. 概率论中的 De Finetti-Hewitt-Savage 定理断言, 所有满足这一性质的无穷随机变量序列 $\left(X_{j}\right)$ 都可以被某些独立同分布随机变量序列“表示”. 亦即 $\left(X_{j}\right)$ 的联合分布 (作为概率测度) 可以写为独立同分布随机变量序列对应的 （乘积）概率测度的凸组合. 易知当各 $X_{j}$ 独立同分布时, 相应的 $f$ 是完全积性的, 因此一般的 $f$ 也可以写成完全积性函数的凸组合. 证明中定义的 $G_{N, n}(X)$ （是 $n$ 的完全积性函数, 对应于取定样本 $X$ 的经验分布) 与 $\mathbb{E}\left[G_{N, n}(X)\right]$ 可以看成这一过程的近似. 实际上 De Finetti-Hewitt-Savage 定理的一个证明就是通过对 $G_{N, n}(X)$ 在一定意义下取极限而得, 这一极限的存在性超出了高中数学的范围, 可参见 https://www.mathematik.uni-muenchen.de/ sorensen/Lehre/SoSe2015/ Rougerie/deF-Munich_v2-May15.pdf 的 28-34 页.

(2). 浙江省慈溪中学胡洁洋, 北大附中㫿晨昊等同学也给出了本题的正确解答.


[^0]:    1 问题中漏了“它及”二字, 在此更正

