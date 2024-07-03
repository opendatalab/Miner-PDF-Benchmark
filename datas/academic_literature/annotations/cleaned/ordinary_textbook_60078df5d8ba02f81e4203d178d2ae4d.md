数学新星网 类教师专栏

www.nsmath.cn/jszl

# 2020 年 ELMO 试题解答与评析 

羊明亮<br>(浙江乐清知临中学, 325600)

2020 年 ELMO 于 6 月 20,21 日 $14: 00-18: 30$ 在线上举行. 本次赛题, 题目新颖, 难度较大, 是一套高质量的试题, 其中 $1,4,6$ 较容易, 适合全国高中数学联赛, $2,3,5$ 有一定难度, 是冬令营好的训练题, 值得一提是 3 , 设置独特, 很好地考察学生的几何能力. 笔者水平有限, 不当之处还请指正.

## I. 试 题

1. 试求所有的函数 $f: \mathbb{N}^{+} \rightarrow \mathbb{N}^{+}$满足:

$$
f^{f^{(x)}(y)}(z)=x+y+z+1, \quad \text { 对所有正整数 } x, y, z \text { 成立. }
$$

这里 $f^{1}(b)=f(b), f^{a+1}(b)=f\left(f^{a}(b)\right)$, 其中 $a, b \in \mathbb{N}^{+}$.

2. 定义斐波那契数为 $F_{1}=F_{2}=1, F_{n}=F_{n-1}+F_{n-2}, n \geq 3$. 设 $k$ 为正整数, 假设对任意的正整数 $m$, 都存在一个正整数 $n$, 使得 $m \mid F_{n}-k$, 问: $k$ 是否一定为斐波那契数?
3. Janabel 有一个作图工具: 给平面上两个不同的点 $u, v$, 他可以作出 $u v$的中垂线. 现给定一个由三条直线构成的三角形. 证明: 他可以仅用这个工具和一支铅笔作出该三角形的垂心.
4. 如图, 设 $H$ 为非等腰的锐角三角形 $A B C$ 的垂心, $A D$ 为 $B C$ 边上的高, $M$ 为 $B C$ 的中点, $D^{\prime}$ 为 $D$ 关于 $M$ 的对称点. 过点 $A$ 作 $B C$ 的平行线交直线 $D^{\prime} H$ 于点 $P$. 设 $\triangle A H P$ 的外接圆与 $\triangle B H C$ 的外接圆交于 $H, G$ 两点. 证明: $\angle M H G=90^{\circ}$.
5. 给定正整数 $m, n$, 求最小的正整数 $s$, 使得存在一个 $m \times n$ 的由正整数[^0]



构成的矩阵, 满足

(1) 每行的 $n$ 个数是以某种顺序排列的连续正整数.

(2) 每列的 $m$ 个数是以某种顺序排列的连续正整数.

(3) 矩阵中的每个数都不超过 $s$.

6. 对任意正整数 $n$, 定义: $\tau(n)$ 表示 $n$ 的正因子个数; $\sigma(n)$ 表示 $n$ 的所有正因子之和; $\varphi(n)$ 表示小于 $n$ 的与 $n$ 互素的正整数的个数.

Brandon 有一个计算器, 上面有三个按钮, 分别可以用 $\tau(n), \sigma(n), \varphi(n)$ 替换当前显示的 $n$. 给定大于 1 的整数 $a, b$. 证明: 如果计算器当前显示的数为 $a$,那么 Brandon 可以通过有限次 (可以为零次) 摁按钮, 使得计算器显示的数为 $b$.

## II . 解答与评注

题 1 试求所有的函数 $f: \mathbb{N}^{+} \rightarrow \mathbb{N}^{+}$满足:

$$
f^{f^{f(x)}(y)}(z)=x+y+z+1 \text {, 对所有正整数 } x, y, z \text { 成立. }
$$

这里 $f^{1}(b)=f(b), f^{a+1}(b)=f\left(f^{a}(b)\right)$, 其中 $a, b \in \mathbb{N}^{+}$.

解 1 记 $m=x+y+1, m$ 可取遍所有不小于 3 的正整数, 再记 $t=f^{f(x)}(y)$.则 $f^{t}(z)=z+m$, 对 $\forall z \in \mathbb{N}^{+}$成立. 从而

$$
f(z+m)=f\left(f^{t}(z)\right)=f^{t}(f(z))=f(z)+m \text {. }
$$

取 $z=1$, 则 $f(n)=n-1+f(1)$ 对 $n \geq 4$ 成立. 于是, 对 $\forall n \in \mathbb{N}^{+}(n \geq 4)$有 $f(n)=n-1+f(1)$, 从而 $f(6)=5+f(1)$. 又由(1)知 $f(6)=f(3)+3$, 于是 $f(3)=2+f(1)$. 同理: $f(5)=4+f(1)$ 且 $f(5)=3+f(2)$, 所以 $f(2)=f(1)+1$.
综上, 知对 $\forall n \in \mathbb{N}^{+}$有 $f(n)=n-1+f(1)$.

记 $c=f(1)-1$, 则

$$
\begin{aligned}
x+y+z+1 & =f^{f^{f(x)}(y)}(z)=f^{f^{x+c}(y)}(z) \\
& =z+c(y+(x+c) \cdot c) \\
& =c^{2} x+c y+z+c^{3}
\end{aligned}
$$

对 $\forall x, y, z \in \mathbb{N}^{+}$成立, 比较两边 $x, y$ 系数知 $c=1$, 即 $f(n)=n+1$, 对 $\forall n \in \mathbb{N}^{+}$.容易验证该函数符合条件.

综上即知所求 $f(x)=x+1$.

解 2 (缪立昂) 依题设

$$
f^{f^{f(x)}(y)}(z)=x+y+z+1
$$

我们在 $(*)$ 中取 $x=y=1$, 可得 $f^{f(1)}(1)(z)=z+3$.

(1) 若 $f(1)=1$, 则 $f(z)=z+3$. 取 $z=1$ 即知矛盾.

(2) 若 $f(1) \geq 2$, 我们在 $(*)$ 中取 $x=f^{f(1)-1}(1)$. 那么

$$
f^{f^{f(x)}(y)}(z)=y+z+f^{f(1)-1}(1)+1, f^{f^{f(x)}(y)}(z)=f^{f^{f(1)}(1)}(y)(z)=f^{y+3}(z),
$$

从而

$$
f^{y+3}(z)=y+z+f^{f(1)-1}(1)+1 .
$$

再在上式中分别取 $y=1,2$, 可得:

$$
f^{4}(z)=z+f^{f(1)-1}(1)+2, f^{5}(z)=z+f^{f(1)-1}(1)+3,
$$

即

$$
f\left(z+f^{f(1)-1}(1)+2\right)=z+f^{f(1)-1}(1)+3 .
$$

这说明: 对 $\forall z \geq f^{f(1)-1}(1)+3, z \in \mathbb{N}^{+}$有 $f(z)=z+1$. 于是, 在 $(*)$ 中取 $y, z \geq f^{f(1)-1}(1)+3$, 有

$$
z+y+f(x)=x+y+z+1
$$

所以 $f(x)=x+1$ 对 $x \in \mathbb{N}$ 成立. 容易验证满足条件.

综上所述, 所求函数为 $f(x)=x+1$.

评注 本题是一道典型的函数迭代题, 可先猜测答案, 然后通过迭代运算不断向目标逼近. 断定迭代是累加运算后, 转为求 $f(1)$ 的值即可.
题 2 定义斐波那契数为 $F_{1}=F_{2}=1, F_{n}=F_{n-1}+F_{n-2}, n \geq 3$. 设 $k$ 为正整数, 假设对任意的正整数 $m$, 都存在一个正整数 $n$, 使得 $m \mid F_{n}-k$, 问: $k$ 是否一定为斐波那契数?

解 1 (卢程达) 答案是肯定的. 理由如下:

假设 $k$ 不是斐波那契数. 对于给定的 $t \in \mathbb{N}^{+}$, 我们对 $s(s \in \mathbb{N})$ 归纳证明:

$$
F_{t-s} \equiv(-1)^{s-1} F_{t+s} \quad\left(\bmod F_{t}\right)
$$

其中, 由 $F_{n-2}=F_{n}-F_{n-1}$, 可将 $\left\{F_{n}\right\}$ 的下标向零及负整数延拓.

(1) 当 $s=0$ 时, 结论成立. 当 $s=1$ 时, $F_{t-1}=F_{t+1}-F_{t}$, 结论成立.

（2）假设结论对 $s=n-1, s=n$ 成立 $\left(n \in \mathbb{N}^{+}\right)$. 当 $s=n+1$ 时,

$$
\begin{aligned}
F_{t-(n+1)} & =F_{t-(n-1)}-F_{t-n} \\
& \equiv(-1)^{n-2} F_{t+n-1}-(-1)^{n-1} F_{t+n} \\
& \equiv(-1)^{n}\left(F_{t+n}+F_{t+n-1}\right) \\
& \equiv(-1)^{n} F_{t+n+1} \quad\left(\bmod F_{t}\right),
\end{aligned}
$$

故结论对 $s=n+1$ 成立.

(3) 综上, 由归纳原理知 $(*)$ 成立.

注意到 $F_{0}=0$, 由 $(*)$ 知

$$
F_{2 t} \equiv F_{0}=0 \quad\left(\bmod F_{t}\right)
$$

而

$$
F_{2 t+s} \equiv(-1)^{s-1} F_{2 t-s} \quad\left(\bmod F_{2 t}\right),
$$

从而

$$
\begin{aligned}
F_{2 t+s} \equiv(-1)^{s-1} F_{2 t-s} & \equiv(-1)^{s-1} F_{t+(t-s)} \\
& \equiv(-1)^{s-1}(-1)^{t-s-1} F_{s} \\
& \equiv(-1)^{t} F_{s} \quad\left(\bmod F_{t}\right) .
\end{aligned}
$$

故当 $2 \mid t$ 时, $F_{n}$ 在 $\bmod F_{t}$ 意义下以 $2 t$ 为周期. 故对 $\forall n \in \mathbb{N}^{+}, t$ 为偶数, $\exists u \in\{0,1, \cdots, t-1\}$ 使得

$$
F_{n} \equiv F_{u} \text { 或 }-F_{u} \quad\left(\bmod F_{t}\right) .
$$

取 $t$ 充分大使 $k<F_{t-2}$, 由题设, $\exists n \in \mathbb{N}^{+}$, 使得

$$
F_{t} \mid F_{n}-k,
$$

故

$$
k \equiv F_{u} \text { 或 }-F_{u}\left(\bmod F_{t}\right) .
$$

但若 $k \equiv F_{u}\left(\bmod F_{t}\right)$, 由 $k<F_{t-2}, u \leq t-1$, 有 $\left|F_{u}-k\right|<F_{t}$, 知 $F_{u}=k$, 矛盾! 同理当 $k \equiv-F_{u}\left(\bmod F_{t}\right)$ 时, 由 $k<F_{t-2}, u \leq t-1$ 有 $\left|F_{u}+k\right|<F_{t}$, 知 $-F_{u}=k$, 矛盾!

综上, 知 $k$ 必为斐波那契数.

解 2 答案是肯定的. 理由如下:

假设 $k$ 不是斐波那契数. 我们依次证明如下三个结论:

(1) 存在 $n \in \mathbb{N}^{+}$, 使得 $k \mid F_{n}$.

(2)对任意的 $n, q \in \mathbb{N}^{+}, n, q \geq 1$, 有

$$
F_{n}=F_{q} \cdot F_{n+1-q}+F_{q-1} F_{n-q}\left(\text { 约定 } F_{0}=0\right) .
$$

(3)假设 $d$ 为最小的正整数, 使得 $k \mid F_{d}$, 则 $F_{d} \mid k$.

对于(1), 设 $F_{n} \equiv x_{n}(\bmod k)$, 其中, $0 \leq x_{n} \leq k-1$. 考察数组 $\left(x_{n}, x_{n+1}\right)$, 由 $x_{n}$ 仅有 $k$ 种取法知 $\left(x_{n}, x_{n+1}\right)$ 至多有 $k^{2}$ 种取法, 于是由抽屈原理, 知存在一组 $i, j \in \mathbb{N}^{+}(i<j)$, 使得 $x_{i}=x_{j}, x_{i+1}=x_{j+1}$, 即

$$
\left\{\begin{array}{l}
F_{i} \equiv F_{j} \quad(\bmod k), \\
F_{i+1} \equiv F_{j+1} \quad(\bmod k) .
\end{array}\right.
$$

取一组这样的 $i, j$, 使得 $j$ 为最小的, 则有 $i=1$. 否则, 若 $i \geq 2$, 有

$$
F_{i-1} \equiv F_{i+1}-F_{i} \equiv F_{j+1}-F_{j} \equiv F_{j-1} \quad(\bmod k)
$$

矛盾. 所以

$$
\left\{\begin{array}{l}
F_{j} \equiv F_{1} \equiv 1 \quad(\bmod k) \\
F_{j+1} \equiv F_{2} \equiv 1 \quad(\bmod k)
\end{array}\right.
$$

从而 $k \mid F_{j+1}-F_{j}$, 即 $k \mid F_{j-1}$, 从而(1)成立.

对于(2),

$$
\begin{aligned}
F_{n} & =F_{1} \cdot F_{n}+F_{0} \cdot F_{n-1} \\
& =F_{1} \cdot\left(F_{n-1}+F_{n-2}\right)+F_{0} \cdot F_{n-1} \\
& =F_{2} \cdot F_{n-1}+F_{1} \cdot F_{n-2} \\
& =\cdots
\end{aligned}
$$

$$
\begin{aligned}
& =F_{t} \cdot F_{n+1-t}+F_{t-1} \cdot F_{n-t} \\
& =F_{t} \cdot\left(F_{n-t}+F_{n-t-1}\right)+F_{t-1} \cdot F_{n-t} \\
& =F_{t+1} \cdot F_{n-t}+F_{t} \cdot F_{n-t-1} \\
& =\cdots \\
& =F_{q} \cdot F_{n+1-q}+F_{q-1} \cdot F_{n-q} .
\end{aligned}
$$

从而(2)成立.

对于(3), 取 $m=F_{d}$, 由题设, 存在 $n \in \mathbb{N}^{+}$, 使得

$$
F_{d} \mid F_{n}-k \text {. }
$$

设 $n=p d+r, 1 \leq r \leq d, p \in \mathbb{N}$, 在(2)中取 $q=d$, 则

$$
F_{n}=F_{d} \cdot F_{n+1-d}+F_{d-1} \cdot F_{n-d},
$$

故

$$
\begin{aligned}
F_{n} & \equiv F_{p d+r} \\
& \equiv F_{d} \cdot F_{(p-1) d+r+1}+F_{d-1} \cdot F_{(p-1) d+r} \\
& \equiv F_{d-1} \cdot F_{(p-1) d+r} \\
& \equiv \cdots \\
& \equiv F_{d-1}^{p} \cdot F_{r} \quad\left(\bmod F_{d}\right) .
\end{aligned}
$$

由于 $k \mid F_{d}$, 则

$$
F_{n} \equiv F_{d-1}^{p} \cdot F_{r} \quad(\bmod k),
$$

而由 $k \mid F_{d}$ 及 $(*)$ 知 $k \mid F_{n}$, 于是 $k \mid F_{d-1}^{p} \cdot F_{r}$. 又因为

$$
\operatorname{gcd}\left(F_{d}, F_{d-1}\right)=\operatorname{gcd}\left(F_{d-1}, F_{d-2}\right)=\cdots=\operatorname{gcd}\left(F_{2}, F_{1}\right)=1
$$

结合 $k \mid F_{d}$, 有 $\operatorname{gcd}\left(k, F_{d-1}\right)=1$. 从而 $k \mid F_{r}$, 再结合 $d$ 的最小性有, $r=d$, 再由 $F_{n} \equiv F_{d-1}^{p} \cdot F_{r}\left(\bmod F_{d}\right)$ 知 $F_{d} \mid F_{n}$. 由 $(*)$ 即有 $F_{d} \mid k$, 从而(3)成立.

此时, 由 $k\left|F_{d}, F_{d}\right| k$, 知 $k=F_{d}$, 矛盾.

综上所述, $k$ 一定为斐波那契数.

评注 两种解法分别从代数观点与数论观点出发, 寻求斐波那契数的性质.解法一, 洞察到了模意义下的递推性, 将数列中的项具体刻画出来; 解法二, 只用到了整除性, 关键是找到解答中的 $F_{d}$, 从而通过间隔同余零解决问题.
题 3 Janabel 有一个作图工具: 给平面上两个不同的点 $u, v$, 他可以作出 $u v$ 的中垂线. 现给定一个由三条直线构成的三角形. 证明: 他可以仅用这个工具和一支铅笔作出该三角形的垂心.

证明 1 (方星皓) 我们先证明如下引理.

引理 如图所示. 已知直线 $l_{1}$ 和 $l_{2}$ 满足 $l_{1} / / l_{2}$. $A$ 在 $l_{1}$ 上, $B$ 在 $l_{2}$ 上, 且 $A B$不与 $l_{1}$ 垂直, 则直线 $A B$ 可被作出.



引理的证明 作出 $A B$ 的中垂线分别交 $l_{1}, l_{2}$ 于点 $M, N$. 由 $l_{1} / / l_{2}$, 可知 $M N$的中垂线即为直线 $A B$, 从而从而引理获证.

下回到原题.



如图所示, 点出三角形的三个顶点 $A, B, C$, 我们证明如下结论:

(1) 可作出 $\triangle A B C$ 的外心 $O$,

(2) 可作出 $O$ 关于 $\triangle A B C$ 三边的对称点 $O_{A}, O_{B}, O_{C}$,

(3) 可作出 $\triangle A B C$ 的三条高线.

对 (1), 分别作出边 $B C, C A, A B$ 的中垂线 $l_{a}, l_{b}, l_{c}$, 它们的交点即为 $O$.

对 (2), 记 $B C$ 与 $l_{a}$ 的交点为 $M_{A}$, 作出 $M_{A} C$ 的中垂线 $l_{3}$ 与 $B C$ 交于 $D$, 作出 $M_{A} D$ 的中垂线 $l_{4}$ 与 $B C$ 交与点 $E$. 此时有: $l_{a} / / l_{3} / / l_{4}$. 故可利用引理, 作出 $O E$交 $l_{3}$ 于 $F$, 作出 $M_{A} F$ 交 $l_{4}$ 于 $G$, 作出 $G D$ 交 $l_{a}$ 于 $O_{A}$. 此时有

$$
O M_{A}=D F=M_{A} O_{A},
$$

即 $O_{A}$ 为 $O$ 关于 $B C$ 的对称点. 同理可作出 $O_{B}$ 与 $O_{C}$.

对 (3), 由于 $O_{B}$ 与 $O$ 关于 $A C$ 对称, $O_{C}$ 与 $O$ 关于 $A B$ 对称, 故有

$$
A O_{C}=A O=A O_{B}, M_{B} M_{C} \stackrel{\|}{=} \frac{1}{2} O_{B} O_{C}
$$

这里 $M_{B}, M_{C}$ 分别为 $A C$ 与 $l_{b}, A B$ 与 $l_{c}$ 的交点. 又 $M_{B} M_{C} \stackrel{\|}{=} \frac{1}{2} B C$, 故 $O_{B} O_{C} /$ $B C$. 结合 $A O_{C}=A O_{B}$, 知 $O_{B} O_{C}$ 的中垂线即为 $\triangle A B C$ 过点 $A$ 的高线. 同理有另两条高线, 交点即为垂心, 得证.

证明 2 (万林普) 点出三角形的三个顶点 $A, B, C$, 考虑证明如下事实:

(1) 可点出线段 $A B$ 的中点.

(2) 可作出 $\triangle A B C$ 的中位线.

(3) 可作出过 $\triangle A B C$ 的任一顶点且与对边平行的直线 $l_{A}, l_{B}, l_{C}$.

(4) 设 $l_{A}, l_{B}, l_{C}$ 围成三角形 $V_{A} V_{B} V_{C}$, 可作出 $\triangle V_{A} V_{B} V_{C}$ 的外心 $U$.

对 (1), 作出 $A B$ 的中垂线, 其与 $A B$ 交点即为中点.



对 (2), 点出 $A B$ 中点 $M_{C}, A C$ 中点 $M_{B}$, 分别作 $A M_{C}, A M_{B}$ 的中垂线交于 $O_{1}$. 点出 $B C$ 中点 $M_{A}$, 分别做 $M_{A} M_{B}, M_{B} M_{C}, M_{C} M_{A}$ 中垂线交于点 $V$, 则 $O_{1}, V$ 分别为 $\triangle A M_{B} M_{C}, \triangle M_{A} M_{B} M_{C}$ 的外心. 注意到 $M_{C} M_{A} \stackrel{\|}{=} A M_{B}$, 知

$$
\triangle A M_{B} M_{C} \cong \triangle M_{A} M_{C} M_{B}
$$

从而 $M_{B} M_{C}$ 垂直平分 $O_{1} V$, 故 $M_{B} M_{C}$ 可被作出.

对 (3), 点出 $B M_{C}$ 中点 $D, B M_{A}$ 中点 $E$, 作出 $\triangle B M_{A} M_{C}$ 的中位线 $D E$. 点出 $M_{B} C$ 中点 $F, M_{A} C$ 中点 $G$, 作出 $\triangle C M_{A} M_{B}$ 中位线 $F G$. 设 $D E$ 与 $F G$ 交于点 $T$, 点出 $E T, G T$ 的中点 $Q, P$. 作出 $\triangle E T G$ 的中位线 $P Q$ 交 $A B$ 于 $R$. 注意到四边形 $A D T F$ 为平行四边形, 则

$$
D T=A F=3 F C=3 D E\left(D E \stackrel{\|}{=} \frac{1}{4} A C\right)
$$

故

$$
E Q=\frac{1}{2} E T=\frac{1}{2}(D T-D E)=D E
$$



又 $B E / / R Q$, 则 $B R=B D$. 从而 $\triangle R D Q$ 顶点 $R$ 所对中位线即为 $l_{B}$.

对 (4), 作出 $\triangle V_{A} V_{B} V_{C}$ 三边中垂线, 相交的点即为 $U$.

注意到 $l_{A} / / B C, l_{B} / / C A, l_{C} / / A B$, 知 $\triangle A B C$ 为 $\triangle V_{A} V_{B} V_{C}$ 的中点三角形,从而 $B U \perp V_{A} V_{C}$. 又 $A C / / V_{A} V_{C}$, 故 $B U \perp A C$. 同理有

$$
A U \perp B C, C U \perp A B
$$

故 $U$ 为 $\triangle A B C$ 垂心, 得证.

证明 3 (王铭炜) 点出三角形的三个顶点 $A, B, C$. 作出 $A C$ 的中垂线, 分别与 $A C, A B$ 交于 $M_{B}, P$. 作出 $A B$ 的中垂线, 分别与 $A B, A C$ 交于 $M_{C}, Q$. 作出 $A Q$ 的中垂线, 分别与 $A C, A B$ 交于 $N_{B}, R$. 作出 $A P$ 的中垂线, 分别与 $A B, A C$交于 $N_{C}, S$.

分别作出 $R K, A K$ ( $K$ 为 $R N_{B}$ 与 $S N_{C}$ 的交点) 的中垂线, 交点记为 $O_{1}$. 分别作出 $S K, A K$ 的中垂线, 交点记为 $O_{2}$. 我们证明如下事实:



(1) $B, P, C, Q$ 四点共圆.

(2) $B C \perp A K$.

(3) $A K$ 为 $O_{1} O_{2}$ 的中垂线.

对 (1), 由

$$
\begin{aligned}
\angle A P C & =180^{\circ}-2 \angle P A C \\
& =180^{\circ}-2 \angle B A Q \\
& =\angle B Q A=\angle B Q C,
\end{aligned}
$$

得证.

对 (2), 与 (1) 同理, 会有 $R, Q, S, P$ 四点共圆. 从而

$$
\begin{aligned}
\angle A B S & =\angle P R S=\angle P Q S=\angle P Q C \\
& =\angle P B C=\angle A B C
\end{aligned}
$$

知 $R S / / B C$. 注意到 $K$ 为 $\triangle A R S$ 的垂心, 故 $A K \perp R S$, 因此 $A K \perp B C$.

对 (3), 考虑垂心组 $A K R S$, 知 $\odot A K R$ 与 $\odot A K S$ 为等圆. 从而 $A K$ 垂直平分 $O_{1} O_{2}$. 故 $A K$ 可被作出, 结合 (2) 知 $\triangle A B C$ 的顶点 $A$ 所对的高线 $h_{A}\left(h_{A}\right.$ 即为 $\left.A K\right)$ 可被作出. 同理可作出 $h_{B}, h_{C}$, 那么 $h_{A}, h_{B}, h_{C}$ 的交点即为 $\triangle A B C$ 的垂心, 命题获证.

评注 本题形式新颖, 需要对图形有较好的认知. 在想法上, 方法一与方法三由垂心联想垂心组, 通过等圆得到一些中垂线, 获得好的性质, 不同的是方法一基于原垂心组, 而方法三则是构造新的垂心组. 方法二是希望欲做的垂心是某一三角形的巧合点, 选择了从中点三角形入手, 转化命题. 在刻画上, 方法一与方法二脱开中垂线, 寄希望于找到一种更容易被利用的连线方式, 方法三直接从中垂线入手, 这一做法颇为不易.

题 4 如图, 设 $H$ 为非等腰的锐角三角形 $A B C$ 的垂心, $A D$ 为 $B C$ 边上的高, $M$ 为 $B C$ 的中点, $D^{\prime}$ 为 $D$ 关于 $M$ 的对称点. 过点 $A$ 作 $B C$ 的平行线交直线 $D^{\prime} H$ 于点 $P$. 设 $\triangle A H P$ 的外接圆与 $\triangle B H C$ 的外接圆交于 $H, G$ 两点. 证明: $\angle M H G=90^{\circ}$.

证明 1 (张盛博) 倍长 $A M$ 至点 $A^{\prime}$, 倍长 $H M$ 至点 $N$. 联结 $B A^{\prime}, D^{\prime} A^{\prime}, C A^{\prime}$, $P G, G A^{\prime}$. 由 $A, H, D$ 三点共线, $\angle A D M=90^{\circ}$, 及 $M$ 为 $D D^{\prime}$ 中点, 知 $A^{\prime}, N, D^{\prime}$三点共线, $\angle A^{\prime} D^{\prime} M=90^{\circ}, D^{\prime} N=D H, A^{\prime} N=A H$, 由 $M$ 分别为 $B C, A A^{\prime}$ 的中点, 知四边形 $A B A^{\prime} C$ 为平行四边形, 故 $\angle B A^{\prime} C=\angle B A C$. 由垂心的性质知



$\angle B A C+\angle B H C=180^{\circ}$, 故 $\angle B A^{\prime} C+\angle B H C=180^{\circ}$. 从而 $B, H, C, A^{\prime}$ 四点共圆. 又

$$
\begin{aligned}
\angle A^{\prime} G H & =180^{\circ}-\angle H B A^{\prime}=180^{\circ}-\left(\angle H B C+\angle A^{\prime} B C\right) \\
& =180^{\circ}-(\angle H B C+\angle A C B)=90^{\circ},
\end{aligned}
$$

且

$$
\angle P G H=180^{\circ}-\angle P A H=90^{\circ} \text {. }
$$

故 $P, G, A^{\prime}$ 三点共线且 $G H \perp P A^{\prime}$. 由 $A P / / B C, \angle D^{\prime} D H=\angle P A H=90^{\circ}$ 知 $\triangle A H P \sim \triangle D H D^{\prime}$. 从而

$$
\frac{D^{\prime} H}{P H}=\frac{D H}{A H}
$$

故

$$
\frac{D^{\prime} H}{P H}=\frac{D^{\prime} N}{A^{\prime} N}
$$

即 $N H / / P A^{\prime}$. 于是 $N H \perp G H$, 即 $M H \perp G H$, 所以 $\angle M H G=90^{\circ}$.

证明 2 (张洪铭) 记 $\odot B H C$ 的圆心为 $O_{2}, \odot A H P$ 的圆心为 $O_{1}, \odot A B C$ 的圆心为 $O$. 联结 $O O_{2}, O_{1} O_{2}$. 由 $H G$ 为 $\odot O_{1}$ 与 $\odot O_{2}$ 的公共弦知 $O_{1} O_{2} \perp H G$. 于是我们只需证明: $M H / / O_{1} O_{2}$.

设 $O O_{2}$ 交 $D^{\prime} H$ 于点 $N$, 由垂心的性质知 $O O_{2}$ 过点 $M$ 且 $O_{2}$ 与 $O$ 关于 $B C$对称, $A H=2 O M$. 故

$$
O_{2} M=O M=\frac{1}{2} A H
$$

由 $A P / / B C$ 及 $A D \perp B C$ 知 $\angle H A P=90^{\circ}$, 故 $O_{1}$ 为线段 $H P$ 中点.



结合

$$
N M \perp B C, A D \perp B C
$$

可得 $M N / / H D$. 又 $M$ 为 $D D^{\prime}$ 的中点, 知 $N$ 为 $D^{\prime} H$ 的中点. 于是

$$
\begin{aligned}
\frac{N H}{O_{1} H} & =\frac{\frac{1}{2} D^{\prime} H}{\frac{1}{2} H P}=\frac{D^{\prime} H}{H P} \\
& =\frac{D H}{A H} \quad\left(A P / / D D^{\prime}\right) \\
& \left.=\frac{2 M N}{2 O_{2} M} \quad \text { (由) }\right) \\
& =\frac{M N}{O_{2} M} .
\end{aligned}
$$

即有 $M H / / O_{1} O_{2}$. 从而由 $O_{1} O_{2} \perp H G$, 有 $M H \perp H G, \angle H M G=90^{\circ}$. 证毕.

评注 利用好垂心的基本性质和平行线之间的比例关系就能轻松解决本题,当中点出现时, 倍长中线得到平行四边形, 也是平面几何中的基本策略.

题 5. 给定正整数 $m, n$, 求最小的正整数 $s$, 使得存在一个 $m \times n$ 的由正整数构成的矩阵, 满足

(1) 每行的 $n$ 个数是以某种顺序排列的连续正整数.

(2) 每列的 $m$ 个数是以某种顺序排列的连续正整数.

(3) 矩阵中的每个数都不超过 $s$.

解 (邵方昊) 所求的最小值为 $m+n-d$, 其中 $d$ 表示 $m$ 和 $n$ 的最大公约数.

记 $(x, y)$ 表示正整数 $x$ 与 $y$ 的最大公约数, 第 $i$ 行中的最小元为 $a_{i}$, 第 $j$ 列中的最小元为 $b_{j}$, 其中 $i=1,2, \cdots, m, j=1,2, \cdots, n$.

一方面, 我们证明 $S \geq m+n-d$.
事实上, 不妨设 $a_{1}=b_{1}=1$. 考虑 $m \times n$ 矩阵中的所有元素构成的可重集合的生成函数为 $f(x)$. 依题设, 有

$$
\begin{aligned}
f(x) & =\left(1+x+\cdots+x^{n-1}\right) \sum_{i=1}^{m} x^{a_{i}} & & \text { (对行求和 ) } \\
& =\left(1+x+\cdots+x^{m-1}\right) \sum_{j=1}^{n} x^{b_{j}} & & \text { (对列求和 })
\end{aligned}
$$

注意到

$$
\begin{aligned}
& \left(1+x+\cdots+x^{n-1}, 1+x+\cdots+x^{m-1}\right) \\
= & \left(\frac{1-x^{n}}{1-x}, \frac{1-x^{m}}{1-x}\right) \\
= & \frac{1-x^{d}}{1-x} \\
= & 1+x+\cdots+x^{d-1} .
\end{aligned}
$$

结合

$$
\left(x, 1+x+\cdots+x^{m-1}\right)=(x, 1)=1
$$

知

$$
\left.\frac{1+x+\cdots+x^{m-1}}{1+x+\cdots+x^{d-1}} \right\rvert\, \sum_{i=1}^{m} x^{a_{i}-1}
$$

(*) 式的左边为 $1+x^{d}+\cdots+x^{d\left(\frac{m}{d}-1\right)}$, 次数为 $m-d$. 由多项式整除的性质知

$$
\max _{1 \leq i \leq m}\left\{a_{i}\right\}-1 \geq m-d \text {. }
$$

设

$$
a_{t}=\max _{1 \leq i \leq m}\left\{a_{i}\right\},
$$

依题设, 第 $t$ 行的最大数 $c \leq s$. 由 $c=n-1+a_{t}$ 得

$$
s \geq n-1+a_{t} \geq n+m-d .
$$

另一方面, 我们构造矩阵使得 $s=m+n-d$ 符合题意.

$$
\begin{gathered}
\text { 记 } \\
A_{n}=\left[\begin{array}{cccc}
1 & 2 & \cdots & n \\
2 & 3 & \cdots & 1 \\
\cdots & \cdots & \ddots & \vdots \\
n & 1 & \cdots & n-1
\end{array}\right], A_{n}+w=\left[\begin{array}{cccc}
1+w & 2+w & \cdots & n+w \\
2+w & 3+w & \cdots & 1+w \\
\cdots & \cdots & \ddots & \vdots \\
n+w & 1+w & \cdots & n-1+w
\end{array}\right]
\end{gathered}
$$

构造矩阵

$$
\underline{\bar{X}}=\left[\begin{array}{cccc}
A_{d} & A_{d}+d & \cdots & A_{d}+\left(\frac{n}{d}-1\right) d \\
A_{d}+d & A_{d}+2 d & \cdots & A_{d}+\left(\frac{n}{d}\right) d \\
\vdots & \vdots & \ddots & \vdots \\
A_{d}+\left(\frac{m}{d}-1\right) d & A_{d}+\left(\frac{m}{d}\right) d & \cdots & A_{d}+\left(\frac{m+n}{d}-2\right) d
\end{array}\right]
$$

这样的 $m \times n$ 矩阵 $\underline{X}$ 满足题意, 且其中的数都不超过 $m+n-d$.

综上所述, $s$ 的最小值为 $m+n-d$.

评注 算两次是处理矩阵问题的常见方法, 一般有两种形式: (1) 找对应关系进行计数; (2) 通过生成函数比较次数. 本解答中, 生成函数很好地体现了转化的思想, 通过一种特定的表示来避免具体取值的讨论, 进而刻画出整体的结果. 此外本题的构造具有普遍意义, 将矩阵划分为若干方阵, 体现了化繁为简的思想.

题 6. 对任意正整数 $n$, 定义: $\tau(n)$ 表示 $n$ 的正因子个数; $\sigma(n)$ 表示 $n$ 的所有正因子之和; $\varphi(n)$ 表示小于 $n$ 的与 $n$ 互素的正整数的个数.

Brandon 有一个计算器, 上面有三个按钮, 分别可以用 $\tau(n), \sigma(n), \varphi(n)$ 替换当前显示的 $n$. 给定大于 1 的整数 $a, b$. 证明：如果计算器当前显示的数为 $a$,那么 Brandon 可以通过有限次 (可以为零次) 摁按钮, 使得计算器显示的数为 $b$.

证明 (韩新秝) 注意到以下几个事实:

(1) $a$ 可以产生 2.

(2) $2^{b-1}$ 可产生 $b$.

(3) $2^{k+1}$ 可产生 $2^{k}$, 其中 $k \in \mathbb{N}$.

(4) $2^{k} \cdot m$ 可产生 $2^{k}$, 其中 $m, k \in \mathbb{N}^{+},(m, 2)=1$ 且 $m>1$.

对于 (1), 注意到 $2 \leq \tau(a)<a$ 在 $a \geq 3$ 时恒成立, 只需对 $a$ 反复进行 $\tau(n)$操作.

对于 (2), 注意到 $\tau\left(2^{b-1}\right)=b$ 即可.

对于 (3), 注意到 $\varphi\left(2^{k+1}\right)=2^{k}$.

对于 (4), 记 $m$ 的标准分解 $\prod_{i=1}^{s} p_{i}^{\alpha_{i}}$, 有:

$$
\varphi\left(2^{k} \cdot m\right)=\varphi\left(2^{k}\right) \cdot \varphi(m)=2^{k-1} \prod_{i=1}^{s} p_{i}^{\alpha_{i}-1}\left(p_{i}-1\right) .
$$

又 $2 \mid p_{i}-1(i=1,2, \cdots, s)$, 知

$$
V_{2}\left(\varphi\left(2^{k} \cdot m\right)\right) \geq k
$$

结合 $\varphi\left(2^{k} \cdot m\right)<2^{k} \cdot m$, 对 $2^{k} \cdot m$ 经有限次 $\varphi(n)$ 操作后会产生 $2^{l}(l \geq k)$, 由 (3)知可产生 $2^{k}$.

回到原题, 由 (1) 可不妨设 $a=2$. 假设 2 不能产生 $b$, 由 (2)(3)(4) 知 2 不能产生 $2^{b-1}$ 的倍数. 考虑每个可产生的数 $n$, 记 $n$ 的标准分解 $\prod_{i=1}^{s} p_{i}^{\alpha_{i}}$, 则有 $s \leq b$.否则

$$
V_{2}(\varphi(n))=V_{2}\left(\prod_{i=1}^{s} p_{i}^{\alpha_{i}-1}\left(p_{i}-1\right)\right) \geq V_{2}\left(\prod_{i=1}^{s}\left(p_{i}-1\right)\right) \geq s-1 \geq b
$$

矛盾！从而

$$
\frac{\varphi(n)}{n}=\prod_{i=1}^{s} \frac{p_{i}-1}{p_{i}} \geq \frac{1}{2^{s}} \geq \frac{1}{2^{b}}
$$

即

$$
\frac{\varphi(n)}{n} \geq \frac{1}{2^{b}}
$$

先现对 2 反复进行 $\sigma(n)$ 操作. 待定 $M_{1}, M_{2}$, 并使产生的数 $A$ 满足

$$
A>2^{M_{1} \cdot b} \cdot M_{2}
$$

对 $A$ 进行 $M_{1}$ 次 $\varphi(n)$ 操作, 由 $(*)$ 知产生的数均大于 $M_{2}$. 令 $M_{2}>2^{b}$, 即知产生的 $M_{1}$ 个数均不为 2 的幂. 同 (4) 知这 $M_{1}$ 次操作均保持所得数的 2 的幂不减.又这些数中无 $2^{b-1}$ 的倍数, 故使 2 的幂次增加的操作少于 $b$ 次.

待定 $M_{3}$ (充分大), 取 $M_{1}>b M_{3}$, 即知这 $M_{1}$ 步中存在连续 $M_{3}$ 步操作所得的数的 2 的幂次保持不变, 且不为 0 (因为不小于 3 的奇数进行 $\varphi(n)$ 操作会变为偶数, 含 2 的幂次改变). 注意到 $\forall k \geq 1, m>1,2 \nmid m$, 若 $V_{2}\left(\varphi\left(2^{k} \cdot m\right)\right)=k$,同 $(4)$ 知 $m$ 只含一种素因子 $p$, 且 $p \equiv 3(\bmod 4)$.

取 $M_{4}>2^{b}, M_{2}>2^{b} \cdot 3^{M_{4}}$. 若上述 $M_{3}$ 步中产生 $2^{k} \cdot 3^{l}$ 型数, 因为 $2^{k} \cdot 3^{l}>M_{2}$且 $k<b-1$, 则 $l>M_{4}$. 结合 $k \geq 1, \varphi\left(2^{u} \cdot 3^{v}\right)=2^{u} \cdot 3^{v-1}$ (其中 $u, v \in \mathbb{N}^{+}$) 知对任意正整数 $l_{0}<M_{4}$, 可对 $2^{k} \cdot 3^{l}$ 反复进行 $\varphi(n)$ 操作产生 $2^{k} \cdot 3^{l_{0}}$.

取 $l_{0}=2^{b}-1<M_{4}$, 此时 $\tau\left(2^{k} \cdot 3^{l_{0}}\right)=2^{b} \cdot(k+1)$, 与假设矛盾! 于是这 $M_{3}$步中均不产生 $2^{k} \cdot 3^{l}$ 型数.

对这 $M_{3}$ 个数中前 $M_{3}-2$ 个数中任一个, 设为 $2^{k} \cdot p^{l}\left(k, l \in \mathbb{N}^{+}\right)$, 则

$$
\varphi\left(2^{k} \cdot p^{l}\right)=2^{k} \cdot \frac{p-1}{2} \cdot p^{l-1}
$$

而 $\varphi\left(2^{k} \cdot p^{l}\right)$ 含 2 的幂次为 $k$ 且 $2^{k} \cdot \frac{p-1}{2} \cdot p^{l-1}$ 中只有一个奇素因子. 又 $1<\frac{p-1}{2}<p$,知 $l$ 仅能为 1 且 $\frac{p-1}{2}$ 为奇质数. 于是可不妨设前 $M_{3}-2$ 步中第 $i$ 步为 $2^{k} \cdot p_{i}$, 则有

$$
p_{i+1}=\frac{p_{i}-1}{2}\left(1 \leq i \leq M_{3}-3\right) .
$$

即

$$
p_{i}+1=2\left(p_{i+1}+1\right)
$$

对上式 $i=1,2,3, \cdots, M_{3}-3$ 进行累乘, 知

$$
p_{1}+1=2^{M_{3}-3}\left(p_{M_{3}-2}+1\right) \text {, }
$$

即 $p_{1}+1$ 为 $2^{M_{3}-3}$ 的倍数. 令 $M_{3}>b+3$, 有 $2^{b} \mid p_{1}+1$, 此时

$$
\sigma\left(2^{k} \cdot p_{1}\right)=\left(p_{1}+1\right)\left(2^{k+1}-1\right)
$$

是 $2^{b}$ 的倍数, 这与假设矛盾!

故假设不成立, 进而结论获证！

评注 本题需对三个数论函数的运算有一定程度的理解, 其基本思路和策略是:

(1) $\sigma(n)$ 和 $\varphi(n)$ 难以得到具体的值, 注意到 $\tau\left(2^{b-1}\right)=b$, 就可以得到 $b$.

(2) 要产生 2 的幂次, 用 $\varphi(n)$. 由 $\varphi\left(2^{k}\right)=2^{k-1}$ 可知, 2 的幂次可实现高次向低次转化. 当 $n$ 不是 2 的幂次时, 可让 2 的幂次在操作时不减.

(3) 不断地用 $\sigma(n)$ 操作, 得到一个充分大的数, 再用 $\varphi(n)$ 来得到一个 2 的高次幂的数.

(4) 对 $\varphi(n)$ 解决不了的情况再去考虑利用 $\sigma(n)$ 和 $\tau(n)$ 来处理.


[^0]:    修订日期: 2020-09-04.

