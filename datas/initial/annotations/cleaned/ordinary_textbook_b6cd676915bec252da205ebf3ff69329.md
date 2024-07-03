# 2016 USAMO 试题解答与评析 

## 王逸轩

(湖北省武钢三中, 430080)

本文给出今年美国数学奥林匹克 (USAMO) 试题的解答与评析, 供有兴致的读者参考.

第 1 题. 设 $X_{1}, X_{2}, \cdots, X_{100}$ 是集合 $S$ 的两两不同的非空子集. 集合 $X_{i}$ 与集合 $X_{i+1}$ 的交集是空集, 并且它们的并集不是全集 $S$, 即对任意 $i \in\{1,2, \cdots, 99\}$,都有 $X_{i} \cap X_{i+1}=\emptyset, X_{i} \cup X_{i+1} \neq S$. 求集合 $S$ 元素个数的最小值.

解 集合 $S$ 元素个数的最小值 $|S|_{\min }=8$.

一方面, 当 $|S|=8$ 时, 不妨设 $S=\{1,2,3,4,5,6,7,8\}$. 将元素按 $\bmod 8$ 理解, 即 $i+8=i$.

考察 $S$ 的一元集, 二元集, 三元集及形如 $\{i, i+1, i+2, i+3\}(1 \leq i \leq 8)$的共 $C_{8}^{1}+C_{8}^{2}+C_{8}^{3}+8=100$ 个子集. 令

$$
X_{2 i-1}=\{i, i+1, i+2, i+3\}, X_{2 i}=\{i+5, i+6, i+7\}, \quad(1 \leq i \leq 8),
$$

则当 $1 \leq i \leq 15$ 时, 已有 $X_{i} \cap X_{i+1}=\emptyset,\left|X_{i} \cup X_{i+1}\right|=7$, 故 $X_{i} \cup X_{i+1} \neq S$. 又

$$
X_{2 i+15}=\{i-1, i, i+3\}, X_{2 i+16}=\{i+2, i+5, i+6\}, \quad(1 \leq i \leq 8),
$$

则 $i=16$ 及 $17 \leq i \leq 31$ 时, $X_{i} \cap X_{i+1}=\emptyset,\left|X_{i} \cup X_{i+1}\right|=6$, 故 $X_{i} \cup X_{i+1} \neq S$.

$$
X_{2 i+31}=\{i-2, i, i+2\}, X_{2 i+32}=\{i+4, i+5\},(1 \leq i \leq 8),
$$

则 $i=32$ 及 $33 \leq i \leq 47$ 时, $X_{i} \cap X_{i+1}=\emptyset .\left|X_{i} \cup X_{i+1}\right|=6$ 或 5 , 故 $X_{i} \cup X_{i+1} \neq S$.

$$
X_{2 i+47}=\{i-2, i-1, i+1\}, X_{2 i+48}=\{i+3, i+5\},(1 \leq i \leq 8),
$$

则 $i=48$ 及 $49 \leq i \leq 63$ 时, $X_{i} \cap X_{i+1}=\emptyset$. $\left|X_{i} \cup X_{i+1}\right|=5$. 故 $X_{i} \cup X_{i+1} \neq S$.

$$
X_{2 i+63}=\{i-3, i-1, i\}, X_{2 i+64}=\{i+2\},(1 \leq i \leq 8) \text {, }
$$

则 $i=64$ 及 $65 \leq i \leq 79$ 时, $X_{i} \cap X_{i+1}=\emptyset, \mid X_{i} \cup X_{i+1}=5$ 或 4 , 故 $X_{i} \cup X_{i+1} \neq S$.

$$
X_{2 i+79}=\{i+3, i, i+5, i\}, X_{2 i+80}=\{i-1, i+2\},(1 \leq i \leq 8),
$$

则 $i=80$ 及 $81 \leq i \leq 95$ 时, $X_{i} \cap X_{i+1}=\emptyset,\left|X_{i} \cup X_{i+1}\right|=4$ 或 5 , 故 $X_{i} \cup X_{i+1} \neq S$.

$$
X_{i+96}=\{i, i+4\},(1 \leq i \leq 4)
$$

则 $i=96$ 及 $97 \leq i \leq 99$ 时, $X_{i} \cap X_{i+1}=\emptyset,\left|X_{i} \cup X_{i+1}\right|=4$, 故 $X_{i} \cup X_{i+1} \neq S$.

且 $X_{1}, \cdots, X_{100}$ 确为这 100 个子集的排列 (互不相同), 故构造合条件.

另一方面, 我们证明 $|S| \leq 7$ 不合条件.

事实上, 若 $|S|<7$ 时符合条件, 在 $S$ 中添加 $(7-|S|)$ 个元素知 $\left|S^{\prime}\right|=7$ 时符合条件, 故只用证 $|S|=7$ 不合条件. 下用反证法.

由于 $X_{i}$ 非空, 且 $X_{i} \cup X_{i+1} \neq S$, 得对每个 $i$, 有

$$
\left|X_{i}\right|+\left|X_{i+1}\right|=\left|X_{i} \cup X_{i+1}\right| \leq 6
$$

故对每个 $j$, 有 $\left|X_{j}\right| \in\{1,2,3,4,5\}$.

下面我们说明至多 29 个 $X_{i}$, 满足 $\left|X_{i}\right| \in\{4,5\}$.

反证法, 设存在 $\left|X_{i_{1}}\right|,\left|X_{i_{2}}\right|, \cdots,\left|X_{i_{30}}\right| \in\{4,5\}$, 且 $i_{1}<i_{2}<\cdots<i_{30}$. 由 $\left|X_{i}\right|+\left|X_{i+1}\right| \leq 6$ 得

$$
\left|X_{i_{1}+1}\right|, \cdots,\left|X_{i_{29}+1}\right| \in\{1,2\}, \quad i_{1+1}<\cdots<i_{29+1} \leq i_{30}
$$

故有 29 个一元和二元子集. 而这样的子集总共只有 $C_{7}^{1}+C_{7}^{2}=28$ 个, 矛盾! 故 (1) 获证.

进而 100 个 $X_{i}(1 \leq i \leq 100)$ 中, 至多 $C_{7}^{1}$ 个一元集; 至多 $C_{7}^{2}$ 个二元集; 至多 $C_{7}^{3}$ 个三元集; 至多 29 个四元和五元集. 所以 $100 \leq 7+21+35+29=92$, 矛盾!

故假设不成立, 即 $|S| \leq 7$ 不合条件.

综上所述, $|S|_{\min }=8$.

评析 这题不难, 但需要细致分类. 用反证法, 恰当分析相邻两集合元素个数和 $\leq 6$; 用计数方法导出 $|S| \leq 7$ 矛盾; $|S|=8$ 时的构造, 需要对元素较少的 100 个集合在 $\bmod 8$ 意义下分类, 再分段进行构造即可 (尽量先确定多元素的集合).

第 2 题. 求证: 对任意正整数 $k$,

$$
\left(k^{2}\right) ! \cdot \prod_{j=0}^{k-1} \frac{j !}{(j+k) !}
$$

是一个整数.

证明 记 $\nu_{p}(x)$ 为 $x$ 中 $p$ 的幂次, 其中 $p$ 为素数, $x$ 为正整数.

原题只要证明对于一切素数 $p$, 若

$$
\nu_{p}\left(\left(k^{2}\right) ! \prod_{j=0}^{k-1} j !\right) \geq \nu_{p}\left(\prod_{j=0}^{k-1}(j+k) !\right)
$$

则有

$$
\prod_{j=0}^{k-1}(j+k) ! \mid \prod_{j=0}^{k-1} j ! \cdot\left(k^{2}\right) !
$$

即所求为整数.

事实上, 由于 $n$ ! 中 $p$ 的幂为 $\sum_{\alpha=1}^{+\infty}\left[\frac{n}{p^{\alpha}}\right]$, 故

$$
(1) \Leftrightarrow \sum_{\alpha=1}^{+\infty}\left(\left[\frac{k^{2}}{p^{\alpha}}\right]+\sum_{j=0}^{k-1}\left[\frac{j}{p^{\alpha}}\right]\right) \geq \sum_{\alpha=1}^{+\infty} \sum_{j=0}^{k-1}\left[\frac{j+k}{p^{\alpha}}\right]
$$

考虑局部, 对每个 $\alpha$, 若有

$$
\left[\frac{k^{2}}{p^{\alpha}}\right]+\sum_{j=0}^{k-1}\left[\frac{j}{p^{\alpha}}\right] \geq \sum_{j=0}^{k-1}\left[\frac{j+k}{p^{\alpha}}\right],
$$

则 (2) 成立, 故只要证明对一切 $x \in \mathbb{N}_{+}$,

$$
\left[\frac{k^{2}}{x}\right]+\sum_{j=0}^{k-1}\left[\frac{j}{x}\right] \geq \sum_{j=0}^{k-1}\left[\frac{j+k}{x}\right] .
$$

事实上, 作带余除法, 设 $k=l x+n$, 其中 $0 \leq r \leq x-1, l \in \mathbb{N}$. 则

$$
\begin{aligned}
\sum_{j=0}^{k-1}\left[\frac{j}{x}\right] & =\sum_{j=r}^{k-1}\left[\frac{j}{x}\right]=\sum_{j=0}^{l x-1}\left[\frac{j+r}{x}\right], \\
\sum_{j=0}^{k-1}\left[\frac{j+k}{x}\right] & =\sum_{j=0}^{l x-1}\left[\frac{j+r+l x}{x}\right]+\sum_{j=l x}^{l x+r-1}\left[\frac{j+r+l x}{x}\right] \\
& =\sum_{j=0}^{l x-1}\left[\frac{j+r}{x}\right]+l^{2} x+2 r l+\sum_{j=0}^{r-1}\left[\frac{r+j}{x}\right], \\
{\left[\frac{k^{2}}{x}\right] } & =l^{2} x+2 l r+\left[\frac{r^{2}}{x}\right] .
\end{aligned}
$$

故

$$
(3) \Leftrightarrow\left[\frac{r^{2}}{x}\right] \geq \sum_{j=0}^{r-1}\left[\frac{r+j}{x}\right]
$$

在 $2 r \leq x$ 时, (4) 右边为 0 , 成立.

在 $2 r>x$ 时, (4) 右边在 $j<x-r$ 时为 $0, j=x-r, x-r+1, \cdots, r-1$ 时为 1 . 故右边为 $2 r-x$.

故

$$
(4) \Leftrightarrow\left[\frac{r^{2}}{x}\right] \geq 2 r-x
$$

结合 $2 r-x \in \mathbb{Z}_{+}$知

$$
(4) \Leftrightarrow \frac{r^{2}}{x} \geq 2 r-x \Leftrightarrow(r-x)^{2} \geq 0 \text {. }
$$

成立.

从而 (4) 成立, 故命题获证.

评析 这题只要想到素因子幂次分析 (而不是组合意义), 抽象出局部不等式之后, 用带余除法化简. 和式运算后变为一个简单的不等式. 分类讨论即可. 证明整除还是要以素数幂分析为主要手段.

第 3 题. 设点 $O, I_{B}, I_{C}$ 分别是锐角三角形 $A B C$ 的外接圆圆心，角 $B$内的旁切圆圆心和角 $C$ 内的旁切圆圆心。在 $A C$ 边上取点 $E$ 和 $Y$ 使得 $\angle A B Y=\angle C B Y, B E \perp A C$. 在 $A B$ 边上取点 $F$ 和 $Z$ 使得 $\angle A C Z=\angle B C Z$, $C F \perp A B$. 直线 $I_{B} F$ 和 $I_{C} E$ 交于点 $P$. 求证: $P O \perp Y Z$.

证明 如图, 设 $P$ 在 $A B, A C$ 上投影为 $H, G$.设 $I_{B}$ 在 $A B$ 上投影为 $K$.

由 $P F I_{B}$ 共线, 设 $\frac{P F}{F I_{B}}=\lambda$.

由 $P E I_{C}$ 共线, 设 $\frac{P E}{E I_{C}}=\lambda^{\prime}$. 得

$$
\overrightarrow{A H}=\lambda \overrightarrow{A F}+(1-\lambda) \overrightarrow{A K}
$$

用 $a, b, c, R$ 分别表示 $|B C|,|A C|,|A B|$ 及外接圆半径, 由于 $I_{B} K=4 R \sin \frac{B}{2} \cos \frac{C}{2} \cos \frac{A}{2}$ 且


$A K=\tan \frac{A}{2} I_{B} K$, 所以

$$
|A H|=\lambda \cdot 2 R \cdot \sin B \cos A-(1-\lambda) \cdot 4 R \sin \frac{B}{2} \sin \frac{A}{2} \cos \frac{C}{2} .
$$

类似地,

$$
|A H|=\lambda^{\prime} \cdot 2 R \sin C \cos ^{2} A+\left(1-\lambda^{\prime}\right) 4 R \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2} .
$$

所以

$$
\begin{aligned}
d=|A H| & =\lambda \cdot 2 R \sin B \cos A-(1-\lambda) 4 R \sin \frac{B}{2} \sin \frac{A}{2} \cos \frac{C}{2} \\
& =\lambda^{\prime} 2 R \sin C \cos ^{2} A+\left(1-\lambda^{\prime}\right) 4 R \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2}
\end{aligned}
$$

类似地,

$$
\begin{aligned}
e=|A G| & =\lambda \cdot 2 R \sin B \cos ^{2} A+(1-\lambda) 4 R \sin \frac{B}{2} \sin \frac{A}{2} \cos \frac{C}{2} \\
& =\lambda^{\prime} 2 R \sin C \cos A-\left(1-\lambda^{\prime}\right) 4 R \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2}
\end{aligned}
$$

由 (1) $+(2)$ 得

$$
\lambda \cdot 2 R \cdot \sin B\left(\cos A+\cos ^{2} A\right)=\lambda^{\prime} 2 R \sin C\left(\cos A+\cos ^{2} A\right)
$$

故可设 $\lambda=\sin C \cdot K, \lambda^{\prime}=\sin B \cdot K$, 代入 (1) 整理, 得

$$
\begin{aligned}
& K\left(2 R \sin B \sin C \cos A(1-\cos A)+8 R \sin \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}\left(\cos ^{2} \frac{C}{2}+\cos ^{2} \frac{B}{2}\right)\right) \\
& =4 R \sin \frac{A}{2} \cdot \cos \frac{A}{2} .
\end{aligned}
$$

所以

$$
K=\frac{\cos \frac{A}{2}}{\sin B \sin C \cos A \cdot \sin \frac{A}{2}+\sin \frac{B}{2} \sin \frac{C}{2}(\cos C+\cos B+2)},
$$

代入 (1), (2) 式就得到 $d, e$ 表达式.

注意到

$$
\begin{aligned}
P O \perp Y Z & \Leftrightarrow-O Y^{2}+Y P^{2}=-O Z^{2}+Z P^{2} \\
& \Leftrightarrow Y P^{2}+R^{2}-O Y^{2}=Z P^{2}+R^{2}-O Z^{2} \\
& \Leftrightarrow Y G^{2}+P G^{2}+A Y \cdot C Y=Z H^{2}+H P^{2}+A Z \cdot B Z \\
& \Leftrightarrow Y G^{2}-\left(A P^{2}-P G^{2}\right)+A Y \cdot C Y=Z H^{2}-\left(A P^{2}-P H^{2}\right)+A Z \cdot B Z \\
& \Leftrightarrow Y G^{2}-A G^{2}+A Y \cdot C Y=Z H^{2}-A H^{2}+A Z \cdot B Z \\
& \Leftrightarrow A Y(G Y-A G+C Y)=A Z(B Z+Z H-A H) .
\end{aligned}
$$

由角平分线定理, 得 $\frac{A Y}{C Y}=\frac{A B}{C B}$, 故 $A Y=\frac{b \cdot c}{a+c}$. 同样 $A Z=\frac{b c}{b+a}$. 故

$$
P O \perp Y Z \Leftrightarrow(b+a)(b-2 A G)=(a+c)(c-2 A H) .
$$

前面解出

$A G=e$

$$
=\frac{\left(\sin C \cos A+2 \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2}\right) \cdot 2 R \cos \frac{A}{2} \sin B}{\sin B \sin C \cos A \cdot \sin \frac{A}{2}+\sin \frac{B}{2} \sin \frac{C}{2}(\cos C+\cos B+2)}-4 R \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2},
$$

$A H=d$

$$
=\frac{\left(\sin B \cos A+2 \sin \frac{B}{2} \sin \frac{A}{2} \cos \frac{C}{2}\right) \cdot 2 R \cos \frac{A}{2} \sin C}{\sin B \sin C \cos A \cdot \sin \frac{A}{2}+\sin \frac{B}{2} \sin \frac{C}{2}(\cos C+\cos B+2)}-4 R \sin \frac{B}{2} \sin \frac{A}{2} \cos \frac{C}{2} .
$$

代入 (4) 式, 下面我们用 表示两边均约去关于 $B, C$ 对称部分后的结果 (不影响结论).

左边 $\sim(\sin B+\sin A)$.

$$
\begin{aligned}
& \left(\left(\sin B+4 \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2}\right)\left(\sin B \sin C \cos A \sin \frac{A}{2}+\sin \frac{B}{2} \sin \frac{C}{2}(\cos C+\cos B+2)\right)\right. \\
& \left.-2 \cos \frac{A}{2} \sin B\left(\sin C \cos A+2 \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2}\right)\right) \\
= & 2 \cos \frac{C}{2} \cos \frac{A-B}{2} \cdot 2\left(( \operatorname { s i n } \frac { B } { 2 } + 2 \operatorname { s i n } \frac { C } { 2 } \operatorname { s i n } \frac { A } { 2 } ) \left(\sin B \sin C \cos A \sin \frac{A}{2}\right.\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.\left.+\sin \frac{B}{2} \sin \frac{C}{2}(\cos C+\cos B+2)\right)-2 \cos \frac{A}{2} \sin \frac{B}{2}\left(\sin C \cos A+2 \sin \frac{C}{2} \sin \frac{A}{2} \cos \frac{B}{2}\right)\right) \\
\sim & \cos \frac{A-B}{2}\left(\left(\sin B \sin C \cos A \sin \frac{A}{2}+\sin \frac{B}{2} \sin \frac{C}{2}(\cos B+\cos C+2)\right) \cos \frac{A-C}{2}\right. \\
& \left.-4 \cos \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}\left(\cos \frac{C}{2} \cos A+\sin \frac{A}{2} \sin \frac{A+C}{2}\right)\right) \\
= & \cos \frac{A-B}{2} \cos \frac{A-C}{2} . \\
& \left(\sin B \sin C \cos A \sin \frac{A}{2}+\sin \frac{B}{2} \sin \frac{C}{2}(\cos B+\cos C+2)-4 \cos ^{2} \frac{A}{2} \sin \frac{B}{2} \sin \frac{C}{2}\right) .
\end{aligned}
$$

上式为关于 $B, C$ 对称式, 故 (4) 左边为关于 $B, C$ 对称式. 由对称性知 (4) 成立. 故命题证毕.

评析 这道几何题条件和结论均十分简洁. 用计算方法, 先等价转化为投影长度的关系, 再进一步用投影法计算. 虽然计算量巨大, 但熟悉三角形中基本量就不困难. 纯几何方法难以想到, 主要原因是由于这是一个探索中导出的结果.最后化为证明根轴, 用根心定理即证. 注意旁心, 高中点, 内心等等之间联系.

第 4 题. 求所有的函数 $f: \mathbb{R} \rightarrow \mathbb{R}$, 满足对任意实数 $x, y$, 都有

$$
(f(x)+x y) \cdot f(x-3 y)+(f(y)+x y) \cdot f(3 x-y)=(f(x+y))^{2} .
$$

证明 所求函数为 $f(x) \equiv 0$ 或 $f(x)=x^{2}(\forall x \in \mathbb{R})$.

原式中令 $x=y=0$ 得 $f^{2}(0)=0$, 故 $f(0)=0$.

令 $x=y$ 得

$$
\left(f(x)+x^{2}\right)(f(2 x)+f(-2 x))=f^{2}(2 x)
$$

令 $x=3 y$ 得

$$
\left(f(y)+3 y^{2}\right) f(8 y)=f^{2}(4 y)
$$

令 $y=3 x$ 得

$$
\left(f(x)+3 x^{2}\right) f(-8 x)=f^{2}(4 x) .
$$

比较 (2), (3) 知, 若存在 $a$, 使得 $f(8 a) \neq f(-8 a)$, 则

$$
f\left(a+3 a^{2}\right)=0, \text { 且 } f(4 a)=0 \text {. }
$$

故由 $f(x) \neq f(-x)$ 可推出 $f\left(\frac{x}{2}\right)=0$. 同样用 $-x$ 换 $x$, 得 $f\left(-\frac{x}{2}\right)=0$.

若存在 $a$, 使得 $f(a) \neq f(-a)$, 则 (1) 中令 $x=\frac{a}{2}$, 结合 $(*)$ 得

$$
f^{2}(a)=(f(a)+f(-a)) \cdot \frac{a^{2}}{4} .
$$

同样

$$
f^{2}(-a)=(f(a)+f(-a)) \cdot \frac{a^{2}}{4} .
$$

所以 $f(a)=-f(-a)$. 此时代入 (4) 得 $f^{2}(a)=0=f^{2}(-a)$, 则有 $f(a)=$ $f(-a)=0$. 矛盾!

故对任意 $a$, 均有 $f(a)=f(-a)$. 代入 (1), 得

$$
f(2 x)\left(f(2 x)-2 f(2 x)-2 x^{2}\right)=0 .
$$

$f(x)$ 恒为 0 时符合条件. 下设 $f(x)$ 不恒为 0 . 对于一切 $a$, 其中 $f(a) \neq 0$,则 $a \neq 0$.

由 $(2)$ 知若 $f(t) \neq 0$. 令 $y=\frac{t}{4}$ 有 $f(2 t) \neq 0$. 故归纳易知 $f(2 a), \cdots$, $f\left(2^{l} a\right) \neq 0\left(l \in \mathbb{Z}_{+}\right)$.

结合 $(5)$ 知

$$
f\left(2^{l+1} a\right)=2 f\left(2^{l} a\right)+2^{2 l+1} a^{2}
$$

对 $l \in \mathbb{N}$ 成立. 特别地,

$$
f(2 a)=2 f(a)+2 a^{2}, \quad f(4 a)=12 a^{2}+4 f(a), \quad f(8 a)=56 a^{2}+8 f(a) .
$$

在 $(2)$ 中令 $y=a$, 结合前述 $f(4 a), f(8 a)$ 的取值, 得

$$
\left(f(a)+3 a^{2}\right)\left(8 f(a)+56 a^{2}\right)=\left(4 f(a)+12 a^{2}\right)^{2} .
$$

所以 $f^{2}(a)+2 f(a)-3 a^{2}=0$. 即 $f(a)=a^{2}$ 或 $f(a)=-3 a^{2}$.

当 $f(a)=-3 a^{2}$ 时, $f(4 a)=0$. 与前述 $f(4 a) \neq 0$ 矛盾!

故 $f(a)=a^{2}$. 即对一切 $f(a) \neq 0$ 有 $f(a)=a^{2}$.

此时, 若存在 $x \neq 0$, 使得 $f(x)=0$. 取 $a$ 使得 $f(a) \neq 0$, 由前述知 $f\left(2^{l} a\right) \neq 0$ $(l \in \mathbb{N})$. 故 $f\left(2^{l} a\right)=2^{2 l} a^{2}$.

原式中考察 $\left(x, \frac{x-2^{l} a}{3}\right)$ 来替换 $(x, y)$, 得

$$
\begin{aligned}
& \frac{x\left(x-2^{l} a\right)}{3} \cdot 2^{2 l} a^{2} \\
& =f\left(x+\frac{x-2^{l} a}{3}\right)^{2}-\left(f\left(\frac{x-2^{l} a}{3}\right)+\frac{x\left(x-2^{l} a\right)}{3}\right) f\left(3 x-\frac{x-2^{l} a}{3}\right) \\
& =\lambda_{1} \cdot\left(\frac{4 x-2^{l} a}{3}\right)^{4}-\frac{x\left(x-2^{l} a\right)}{3} \lambda_{2} \cdot\left(\frac{8 x+2^{l} a}{3}\right)^{2}-\lambda_{2} \lambda_{3}\left(\frac{x-2^{l} a}{3}\right)^{2} \cdot\left(\frac{8 x+2^{l} a}{3}\right)^{2} .
\end{aligned}
$$

其中 $\lambda_{1}, \lambda_{2}, \lambda_{3} \in\{0,1\}$.

令 $y=2^{l}$, 则由抽屉原理知存在 $\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}\right) \in\{0,1\}^{3}$, 使得当 $\left(\lambda_{1}, \lambda_{2}, \lambda_{3}\right)=$ $\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}\right)$ 时, 有无穷多个 $y$ 满足等式 (6). 而 (6) 左右两侧关于 $y$ 为至多 4 次多
项式, 故恒等.

比较 4 次项有 $\lambda_{1}=\lambda_{2} \lambda_{3}$. 比较 3 次项有

$$
\frac{-x a^{3}}{3}=-\lambda_{1} \cdot \frac{16 x a^{3}}{3^{4}}+\frac{\lambda_{2} x a^{3}}{27}-\frac{\lambda_{2} \lambda_{3} 14 x a^{3}}{3^{4}} .
$$

由 $a, x \neq 0$, 所以

$$
27-16 \lambda_{1}-14 \lambda_{2} \lambda_{3}+3 \lambda_{2}=0 \text {. }
$$

只有 $\lambda_{1}=\lambda_{2}=\lambda_{3}=1$ (否则左边 $>0$ ).

此时由于恒等. 令 $y=\frac{x}{a}$ 知 (6) 成立. 而此时 (6) 左边为 0 , 右边为 $\left(\frac{4 x-x}{3}\right)^{4}=x^{4} \neq 0$. 矛盾!

故假设不成立. 即一切 $x \neq 0$ 有 $f(x) \neq 0$. 结合 $(* *)$ 得 $f(x)=x^{2}$ 总成立.

此时验证知原式左边 $=$ 右边 $=(x+y)^{4}$ 成立.

综上, $f(x) \equiv 0$ 或 $f(x) \equiv x^{2}$.

评析 函数方程先赋一些特征值进行探索, 猜想为偶函数 (由于对称性). 用反证法来证明, 进而导出 $f(2 x)$ 与 $f(x)$ 的关系, 证明 $f(x) \neq 0$ 时 $f(x)=x^{2}$. 最后, 用反证法说明对任意 $x \neq 0$, 均有 $f(x) \neq 0$ (不妨设 $f$ 不恒为 0 ). 这个题整体思路比较清晰, 但每一步的实施还是有难度.

第 5 题. 在三角形 $A B C$ 中, 点 $M$ 和点 $Q$ 分别在边 $A B$ 和 $A C$ 上, 点 $N$ 和点 $P$ 都在边 $B C$ 上, 使得五边形 $A M N P Q$ 的五条边长度相等. 记点 $S$ 为直线 $M N$ 和 $P Q$ 的交点, $l$ 为 $\angle M S Q$ 的角平分线. 求证: 直线 $O I$ 与 $l$ 平行. 其中 $O, I$分别是三角形 $A B C$ 的外接圆圆心和内切圆圆心.

证明 我们以 $\triangle A B C$ 的外接圆为单位圆建立复平面, 用相应的小写字母表示其对应复数.

设外接圆上分别不含 $A, B, C$ 的 $\overparen{B C}, \overparen{A C}, \overparen{A B}$ 中点分别为 $X, Y, Z$. 由 $I$ 为 $X Y Z$ 的垂心得 $I=x+y+z$.

由题意, 设 $A M=A Q=Q P=P N=N M=s$, 则 $|m-a|=s$. 且 $A M \perp O Z$, 故 $m-a=s z i$.

同理 $p-n=s x i, a-q=s y i$.

所以

$$
s(x+y+z) i=m-n+p-q=(m-n)-(q-p) .
$$

由于 $|m-n|=|q-p|$, 故 $(m-n)-(q-p)$ 对应的方向为 $\angle M S Q$ 的外平分线.
于是 $O I$ 对应方向与 $\angle M S Q$ 外平分线对应方向垂直, 因此命题证毕.

评析 本题利用复数算法, 由于相等量较多, 恰当设基本两会有意想不到的简化结果, 这种技巧值得注意.

几何方法相对困难, 主要是难找到切入点. 但如果熟知以下两个结论, 就十分容易.

(1) $A B C D$ 中 $A B=C D$, 则 $A D, B C$ 中点连线关于 $A B, C D$ 成等角 (复数易证);

(2) $\triangle A B C$ 不是等边三角形, 到三边有向距离和为常数的点轨迹为与 $O I$垂直的直线 ( $O, Z$ 分别为外心, 内心) (向量法可证).

进而可以找出外接圆交点, 找到旋转相似, 利用对称性及位似证明平行. 更为本质的做法是直接只用证明 $\angle M S Q$ 外角平分线上点到 $\triangle A B C$ 三边距离和为常数, 用有向面积易证. 所以我们要注意几何结论的积累.

第 6 题. 给定整数 $n \geq k \geq 2$. 你和一个邪恶的巫师玩这样一个游戏: 巫师有 $2 n$ 张卡片, 每张卡片的正面上写有一个整数. 对任意 $i \in\{1,2, \cdots, n\}$, 都恰有两张卡片上正面写着 $i$.

初始时, 巫师将所有卡片正面朝下排成一行，而你并不知道卡片的顺序.

你可以重复进行如下操作: 你选择其中 $k$ 张卡片, 并把它们翻成正面朝上.如果其中有两张卡片上的整数相同, 则你获得游戏的胜利: 否则, 你闭上眼睛,由巫师将这 $k$ 张卡片重新排列顺序并将它们翻回正面朝下 (其余卡片位置不动). 然后你可以进行下一次操作.

我们称数对 $(n, k)$ 是 “可胜数对” , 如果存在一个正整数 $m$, 使得无论巫师如何操作, 你确保能在 $m$ 次操作内获胜.

求所有的”可胜数对" $(n, k)$.

解 所有可胜数对为 $(n, k) . n>k \geq 2, n, k \in \mathbb{Z}$.

一方面, 对于 $n=k \geq 2$ 时, 我们说明不是可胜的.

事实上, 我们指出: 可能每轮操作结束后, 均有 $n$ 张卡片, 数字为 $1 \sim n$ 的排列, 且不能确定任何一张卡片上的数字.

初始时 (1) 满足, 若前一轮满足.

下一轮中, 在余下 $n$ 张卡片中选数不妨设为 $1 \sim t$, 则这 $n$ 张卡片中选出 $n-t$ 张卡片可能数字恰为 $t+1 \sim n$. 故选出了 $n$ 张卡片为 $1 \sim n$ 排列. 在重新排列后, 无法确定卡片上的数字. (1) 仍满足.
故 (1) 始终满足, 每一轮均可能迭出 $n$ 张卡片为 $1 \sim n$ 排列. 故无法获胜.

另一方面, 当 $n>k \geq 2$ 时, 我们说明是可胜的.

事实上, 用反证法说明 $2(n+1)+1$ 轮内必胜.

我们说明若已确定 $i(0 \leq i \leq n)$ 张卡片上的数后. 可在两轮中确定另一张卡片上的数 (这里确定一张卡片上的数, 是指知道其上写的数, 且卡片不会再改变位置).

事实上, 不妨设第 $2 n-i+1, \cdots, 2 n$ 张卡片已确定.

翻开第 $1,2, \cdots, k$ 张卡片得到 $k$ 个不同数, 再翻开第 $1,2, \cdots, k-1, k+1$张卡片 (注意到 $k+1 \leq n<2 n-i+1$, 故后 $i$ 张卡片不改变位置).

第一轮操作后, $1 \sim k$ 张卡片上的数形成集合已知道. 而第二次操作知道 $1 \sim k-1$ 张卡片上的数, 故第 $k$ 张卡片上的数已知道, 且第二次操作不会变动第 $k$ 张卡片的位置.

故第 $k$ 张卡片上的数已确定, (2) 成立.

于是 $2(n+1)$ 轮后, 确定了 $n+1$ 张卡片上的数. 由抽庹原理知必有两张卡片 $A, B$ 上数一样. 第 $2(n+1)+1$ 轮选择的 $k$ 张卡片包含 $A, B$. 则已获胜, 与反证假设矛盾!

故假设不成立, 命题证毕.

综上, 所有可胜数对 $(n, k)$ 为 $n>k \geq 2$.

评析 本题不难却很好. 先猜出结论. 给出一个 “不变的性质” 说明 $n=k$时不行; $n>k$ 时, 化为说明可以依次定下 $n+1$ 张牌 (进而可用抽居原则). 只需注意连续两次操作即可定下 1 张牌 (注意范围), 只要猜出结论及证明方向就十分容易。

