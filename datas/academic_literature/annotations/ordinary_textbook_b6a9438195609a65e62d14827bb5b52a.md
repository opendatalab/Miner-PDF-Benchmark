# 好题与妙解 (二) 

## 2016 年新星寒假班中的若干问题

## 冷岗松

2016 年春节前, 在上海数学新星寒假班上, 我提供了一份题为 “数学问题精选 30 例” 的讲义提纲. 这些问题大多是从国内外最新的竞赛资料中挑选出来的代数问题. 本文对其中的 11 个问题进行讨论, 介绍其背景及解法, 其中有些解法是参加寒假班的学生们提供的.

题 1. 设 $a \geq b \geq c>0$, 证明: 对任何 $t \in\left[0, \frac{\pi}{4}\right]$ 有

$$
\frac{a-b}{a \sin t+b \cos t}+\frac{b-c}{b \sin t+c \cos t}+\frac{c-a}{c \sin t+a \cos t} \geq 0 .
$$

(Titu Andreescu, Math. Relf. 3(2015))

先看 Math. Relf. 上的解答.

证法一 去分母, 则不等式 (1) 等价于

$$
\begin{aligned}
& \left(a^{2} b+b^{2} c+c^{2} a-3 a b c\right) \sin t(\cos t-\sin t) \\
& +\left(a b^{2}+b c^{2}+c a^{2}-3 a b c\right) \cos t(\cos t-\sin t) \\
& +(a-b)(b-c)(a-c) \sin t \cos t \geq 0
\end{aligned}
$$

再由算术 - 几何平均值不等式易得

$$
\begin{aligned}
& a^{2} b+b^{2} c+c^{2} a-3 a b c \geq 0 \\
& a b^{2}+b c^{2}+c a^{2}-3 a b c \geq 0
\end{aligned}
$$

注意到 $\cos t \geq \sin t\left(t \in\left[0, \frac{\pi}{4}\right]\right)$, 由 (3), (4) 便知 (2) 成立, 从而 (1) 得证.

上述证法尽管篇幅不长, 但对代数变形技巧的要求是比较高的.

黄冈中学的陈耀斌同学提供了下面较自然且简单的解法.

证法二 应用 Cauchy不等式, 我们有

$$
\frac{a-b}{a \sin t+b \cos t}+\frac{b-c}{b \sin t+c \cos t}
$$

$$
\begin{aligned}
& =\frac{(a-b)^{2}}{(a-b)(a \sin t+b \cos t)}+\frac{(b-c)^{2}}{(b-c)(b \sin t+c \cos t)} \\
& \geq \frac{(a-c)^{2}}{(a-b)(a \sin t+b \cos t)+(b-c)(b \sin t+c \cos t)} .
\end{aligned}
$$

因此要证 (1), 只需证明:

$$
(a-b)(a \sin t+b \cos t)+(b-c)(b \sin t+c \cos t) \leq(a-c)(a \cos t+c \sin t),
$$

这等价于

$$
\left(a^{2}+b^{2}+c^{2}-a b-b c-c a\right)(\sin t-\cos t) \leq 0 .
$$

又注意到两个熟知的结果: $a^{2}+b^{2}+c^{2} \geq a b+b c+c a, \cos t \geq \sin t\left(t \in\left[0, \frac{\pi}{4}\right]\right)$,便知 (5) 显然成立. 因此 (1) 得证.

下面的解法由华南师大附中的任秋宇同学提供, 也是自然而有趣的.

证法三 易见不等式等价于

$$
\frac{a-b}{a \tan t+b}+\frac{b-c}{b \tan t+c}+\frac{c-a}{c \tan t+a} \geq 0 .
$$

记 $x=\tan t$, 则 $x \in[0,1]$. 这时 (6) 等价于

$$
\frac{a-b}{x a+b}+\frac{b-c}{x b+c} \geq \frac{a-b}{x c+a}+\frac{b-c}{x c+a} .
$$

进一步它等价于

$$
(b-c) \cdot \frac{a-x b-(1-x) c}{(x b+c)(x c-a)} \geq(a-b) \cdot \frac{-(1-x) a+b-x c}{(x a+b)(x c+a)} .
$$

记 $a-b=m \geq 0, b-c=n \geq 0$, 这时 (7) 可等价重写为

$$
m \cdot \frac{m+(1-x) n}{(x b+c)} \geq m \cdot \frac{-(1-x) m+x n}{(x a+b)} .
$$

下证 (8) 成立.

事实上, 若 (8) 式右边是非正的, 则结论成立.

否则, 由 $x b+c \leq x a+b$ 知要证 (8) 成立, 只须证

$$
n(m+(1-x) n) \geq m(x n-(1-x) m),
$$

这等价于 $(1-x)\left(m n+m^{2}+n^{2}\right) \geq 0$, 它是显然成立的. 故 (8) 得证.

题 2. 设 $a, b, c \in \mathbf{R}^{+}$满足

$$
\frac{1}{a^{3}+b^{3}+1}+\frac{1}{b^{3}+c^{3}+1}+\frac{1}{c^{3}+a^{3}+1} \geq 1,
$$

证明:

$$
(a+b)(b+c)(c+a) \leq 6+\frac{2}{3}\left(a^{3}+b^{3}+c^{3}\right) .
$$

先看 Math Relf. 上的解答.

证法一 通过去分母及整理, 条件等价于

$$
2\left(1+a^{3}+b^{3}+c^{3}\right) \geq\left(a^{3}+b^{3}\right)\left(b^{3}+c^{3}\right)\left(c^{3}+a^{3}\right) .
$$

因为 $a^{3}+b^{3} \geq 2\left(\frac{a+b}{2}\right)^{3}$, 由 $(*)$ 可得

$$
2\left(1+a^{3}+b^{3}+c^{3}\right) \geq 8 x^{3},
$$

其中 $x=\frac{1}{8}(a+b)(b+c)(c+a)$.

因此

$$
2\left(a^{3}+b^{3}+c^{3}\right)+18-24 x \geq 8 x^{3}-24 x+16=8(x-1)^{2}(x+2) \geq 0
$$

故

$$
2\left(a^{3}+b^{3}+c^{3}\right)+18 \geq 24 x,
$$

这就是要证的不等式.

上述解法的关键是将条件改写为 $(*)$, 再由一个简单的局部不等式得到 (**). 此法并不容易想到.

下面是东北育才学校邱梓航同学的解法.

证法二 由 Hölder 不等式知

$$
\left(a^{3}+b^{3}+1\right)\left(1+1+c^{3}\right)(1+1+1) \geq(a+b+c)^{3} \text {, }
$$

因此

$$
\frac{1}{a^{3}+b^{3}+1} \leq \frac{3 c^{3}+6}{(a+b+c)^{3}}
$$

故

$$
\sum \frac{1}{a^{3}+b^{3}+1} \leq \frac{3\left(a^{3}+b^{3}+c^{3}\right)+18}{(a+b+c)^{3}} .
$$

这样由条件便得

$$
3\left(a^{3}+b^{3}+c^{3}\right)+18 \geq(a+b+c)^{3}
$$

再注意到恒等式

$$
(a+b+c)^{3}=a^{3}+b^{3}+c^{3}+3(a+b)(b+c)(c+a),
$$

由 (1) 便得所证不等式.

题 3. 设 $x_{1}, x_{2}, \cdots, x_{19}$ 是均不超过 93 的正整数, $y_{1}, y_{2}, \cdots, y_{93}$ 均是不超过

19 的正整数. 证明: 存在 $\left\{x_{i}\right\}_{i=1}^{19}$ 的一些数 (非空) 的和等于 $\left\{y_{j}\right\}_{j=1}^{93}$ 中一些数的和。

(MOSP, 2004；22 届前苏联, 1988)

证明 不妨设 $x_{1}+x_{2}+\cdots+x_{19}>y_{1}+y_{2}+\cdots+y_{93}$. 对任意 $1 \leq i \leq 19,1 \leq$ $j \leq 93$, 考虑和

$$
S_{i}=x_{1}+x_{2}+\cdots+x_{i}, \quad T_{j}=y_{1}+y_{2}+\cdots+y_{j} .
$$

对每个 $1 \leq j \leq 93$, 令 $f(j)$ 是使得 $T_{j} \leq S_{i}$ 成立的所有下标 $i$ 的最小者 (因 $T_{j} \leq T_{19}<S_{93}$, 这样的下标是存在的), 则

$$
S_{f(j)-1}<T_{j} \leq S_{f(j)}
$$

且 $f(j)$ 是 $j$ 的不减函数.

现考虑差 $S_{f(j)}-T_{j}(1 \leq j \leq 93)$. 因为

$$
93 \geq x_{f(j)}=S_{f(j)}-S_{f(j)-1}>S_{f(j)}-T_{j}>0
$$

所以 $S_{f(j)}-T_{j}$ 是小于 93 的非负整数.

若存在 $j(1 \leq j \leq 93)$ 使得 $S_{f(j)}-T_{j}=0$, 则结论已成立; 若对任意 $1 \leq j \leq 93, S_{f(j)}-T_{j}$ 均不等于 0 , 则 $S_{f(j)}-T_{j}$ 仅取 1 到 92 间的整数. 由抽屈原理知存在 $1 \leq i<k \leq 93$ 使得

$$
S_{f(i)}-T_{i}=S_{f(k)}-T_{k} .
$$

亦即

$$
x_{f(j)+1}+x_{f(j)+2}+\cdots+x_{f(k)}=y_{i+1}+y_{i+2}+\cdots+y_{k} .
$$

结论成立.

评注. 此题是一个用组合方法来处理的代数问题. 解法的关键是找与 $T_{j}(1 \leq j \leq 93)$ 最接近的 $S_{f(j)}$, 从而差 $S_{f(j)}-T_{j}$ 的取值范围就很小了, 进而可由抽屉原理解决了.

题 4. 证明: 对任意正实数 $x_{1}, x_{2}, \cdots, x_{n}$. 若 $x_{1} x_{2} \cdots x_{n}=1$. 则

$$
n\left(\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)\right)^{\frac{1}{n}} \geq \sum_{i=1}^{n} x_{i}+\sum_{i=1}^{n} \frac{1}{x_{i}}
$$

(选自 $[1])$

先看 [1]中介绍的解答.
证法一 由算术 - 几何平均值不等式及条件可得

$\frac{x_{1}^{n}}{1+x_{1}^{n}}+\frac{x_{2}^{n}}{1+x_{2}^{n}}+\cdots+\frac{x_{n-1}^{n}}{1+x_{n-1}^{n}}+\frac{1}{1+x_{n}^{n}} \geq \frac{n x_{1} x_{2} \cdots x_{n-1}}{\sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)}}=\frac{n}{x_{n} \sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)}}$, $\frac{1}{1+x_{1}^{n}}+\frac{1}{1+x_{2}^{n}}+\cdots+\frac{1}{1+x_{n-1}^{n}}+\frac{x_{n}^{n}}{1+x_{n}^{n}} \geq \frac{n x_{n}}{\sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)}}$.

将上面两个不等式相加可得

$$
n \geq \frac{n}{x_{n} \sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)}}+\frac{n x_{n}}{\sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)}}
$$

亦即

$$
\sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)} \geq x_{n}+\frac{1}{x_{n}}
$$

同理对 $x_{n-1}, \cdots, x_{1}$ 写出类似于 $(*)$ 的局部不等式, 再将这 $n$ 个不等式相加便得所证结果.

这是一个技巧性很强的解法. 下面是上海中学学生高皓天 ( 2016 年国家集训队队员) 的解答.

证法二 一方面, 注意到

$$
\begin{aligned}
\text { 左边 } & =\left(\prod_{i=1}^{n} n\left(1+x_{i}^{n}\right)\right)^{\frac{1}{n}} \\
& =(\prod_{i=1}^{n}(\underbrace{1+\cdots+1}_{n \text { 个 }}+\underbrace{x_{i}^{n}+\cdots+x_{i}^{n}}_{n \text { 个 }}))^{\frac{1}{n}} .
\end{aligned}
$$

另一方面, 由 Hölder 不等式

$$
\begin{aligned}
& (1+\underbrace{x_{1}^{n}+x_{1}^{n}+\cdots+x_{1}^{n}}_{n-1 \text { 个 }}+x_{1}^{n}+\underbrace{1+\cdots+1}_{n-1 \text { 个 }}) \\
& \cdot(x_{2}^{n}+1+\underbrace{x_{2}^{n}+\cdots+x_{2}^{n}}_{n-2 \text { 个 }}+1+x_{2}^{n}+\underbrace{1+\cdots+1}_{n-2 \text { 个 }}) \\
& \cdot(x_{3}^{n}+x_{3}^{n}+1+\underbrace{x_{3}^{n}+\cdots+x_{3}^{n}}_{n-3 \text { 个 }}+1+1+x_{3}^{n}+\underbrace{1+\cdots+1}_{n-3 \text { 个 }}) \\
& \cdots \\
& \cdot(\underbrace{x_{n}^{n}+x_{n}^{n}+\cdots+x_{n}^{n}}_{n-1 \text { 个 }}+\underbrace{1+\cdots+1+1}_{n \text { 个 }}+x_{n}^{n}) \\
& \geq\left(x_{2} x_{3} \cdots x_{n}+x_{1} x_{3} \cdots x_{n}+\cdots+x_{1} x_{2} \cdots x_{n-1}+x_{1}+x_{2}+\cdots+x_{n}\right)^{n}
\end{aligned}
$$

$$
=\left(\sum_{i=1}^{n} \frac{1}{x_{i}}+\sum_{i=1}^{n} x_{i}\right)
$$

由 $(*)$ 和 $(* *)$ 便得所证结果.

还有一个简洁的用 Hölder 不等式导出局部不等式的方法.

证法三 由 Hölder 不等式

$$
\begin{aligned}
\sqrt[n]{\prod_{i=1}^{n}\left(1+x_{i}^{n}\right)} & =\sqrt[n]{\left(\prod_{j \neq i}\left(1+x_{j}^{n}\right)\right)\left(x_{i}^{n}+1\right)} \\
& \geq x_{i}+\prod_{j \neq i} x_{j}=x_{i}+\frac{1}{x_{i}}, \quad i=1,2, \cdots, n
\end{aligned}
$$

将上面 $n$ 个不等式相加便得所证结果.

题 5. 试求所有函数 $f: \mathbf{N}^{*} \rightarrow \mathbf{R}^{+}$, 满足

(i) $f(2)=2$;

(ii) 任取 $m, n \in \mathbf{N}^{*}, f(m, n)=f(m) f(n)$;

(iii) 任取 $m<n, f(m)<f(n)$.

这似乎是一个经典问题, 如 [2] 中就系统研究过这个问题. 这个问题是确定 $\mathbf{N}^{*} \rightarrow \mathbf{R}^{+}$上的函数, 且由条件 (ii) 易知 $f\left(2^{k}\right)=2^{k}$. 这诱发我们用极限推出 $\mathbf{N}^{*}$上也有 $f(x)=x$ 这一性质.

解 由条件 (ii) 可得 $f\left(2^{k}\right)=2^{k}, k \in \mathbf{N}^{*}$. 任取 $m \in \mathbf{N}^{*}$, 并设 $f(m)=l \in \mathbf{R}$.下证 $l=m$, 从而确定了满足题设条件的函数为 $f(x)=x, x \in \mathbf{N}^{*}$.

事实上, 对任意 $n \in \mathbf{N}^{*}$, 由条件 (ii) 有

$$
f\left(m^{n}\right)=l^{n} .
$$

又注意到存在 $k \in \mathbf{N}^{*}$ 使得

$$
2^{k} \leq m^{n}<2^{k+1}
$$

因此由条件 (iii) 便得

$$
f\left(2^{k}\right) \leq f\left(m^{n}\right)<f\left(2^{k+1}\right)
$$

亦即

$$
2^{k} \leq l^{n}<2^{k+1} \text {. }
$$

这样由 (1), (2) 有

$$
\frac{1}{2}<\left(\frac{m}{l}\right)^{n}<2, \quad \forall n \in \mathbf{N}^{*}
$$

如果 $m>l$, 令 $n \rightarrow+\infty$, 则 $\lim _{n \rightarrow \infty}\left(\frac{m}{l}\right)^{n}=+\infty$, 这与 (3) 右边的不等式矛盾;如果 $m<l$, 令 $n \rightarrow+\infty$, 则 $\lim _{n \rightarrow \infty}\left(\frac{m}{l}\right)^{n}=0$, 这与 (3) 左边的不等式矛盾. 这就证明了 $m=l$.

题 6. 求所有函数 $f: \mathbf{R} \rightarrow \mathbf{R}$ 满足

$$
f(x y) \leq y f(x)+f(y), \quad x, y \in \mathbf{R} .
$$

(2015, 希腊)

这是一个给定函数不等式求函数的问题, 解题过程中当尽量出现反向不等式, 把其转化成函数方程 (等式型) 来处理.

解 在条件中用 $-y$ 替代 $y$ 可得

$$
f(-x y) \leq-y f(x)+f(-y) .
$$

将 (1), (2) 相加可得

$$
f(x y)+f(-x y) \leq f(y)+f(-y), \quad x, y \in \mathbf{R} .
$$

在 (3) 中令 $y=1$ 可得

$$
f(x)+f(-x) \leq f(1)+f(-1), \quad x \in \mathbf{R} .
$$

在 (3) 中将 $x$ 用 $\frac{1}{y}$ 替代可得

$$
f(1)+f(-1) \leq f(y)+f(-y), \quad y \neq 0 .
$$

由 (4) 和 (5) 立得

$$
f(y)+f(-y)=f(1)+f(-1)=C, \quad y \neq 0 .
$$

这时由 (2) 便有

$$
C-f(x y) \leq-y f(x)+C-f(y),
$$

亦即

$$
y f(y)+f(y) \leq f(x y), \quad x, y \neq 0
$$

再由 (1) 和 (6) 可得

$$
f(x y)=y f(x)+f(y), \quad x, y \neq 0
$$

(7) 是关键的, 即将不等式 (1) 变成了等式. 在 (7) 中令 $x=y=1$ 得 $f(1)=0$.在 (7) 中交换 $x, y$ 可得

$$
f(y x)=x f(y)+f(x), \quad x, y \neq 0 .
$$

由 (7), (8) 可得

$$
y f(x)+f(y)=x f(y)+f(x), \quad x, y \neq 0 .
$$

进而有

$$
\frac{f(x)}{x-1}=\frac{f(y)}{y-1}, \quad x, y \neq 0,1
$$

这说明 $\frac{f(x)}{x-1}$ 是常数, 且注意 $f(1)=0$, 于是可设 $f(x)=a(x-1), x \neq 0$.

最后, 在 (1) 中令 $x=0$ 得到 $f(y) \geq(1-y) f(0), y \in \mathbf{R}$, 因此对所有 $y \neq 0$有 $a(y-1) \geq(1-y) f(0)$, 即 $(y-1)(a+f(0)) \geq 0, y \neq 0$, 这样必须 $a=-f(0)$.故所求的函数

$$
f(x)=f(0)(1-x), \quad x \in \mathbf{R} .
$$

易验证, $f(x)=f(0)(1-x)$ 满足条件 (1).

题 7. 设 $f: \mathbf{R} \rightarrow \mathbf{R}$ 满足

$$
f\left(f^{2}(x)+f(y)\right)=x f(x)+y .
$$

求 $f(x)$ 的解析式.

(2012，吉尔吉斯坦)

这是一个典型的函数方程问题. 其解法的要点是: 先取函数的零点值确定初始值 (定位), 再利用函数是单满射的性质作了一个 “回代变换” .

解 在条件 (1) 中令 $x=y=0$, 并记 $f(0)=s$, 则 $f\left(s^{2}+s\right)=0$. 这说明 $s^{2}+s$ 是 $f(x)$ 的零点.

在 (1) 中令 $x=s^{2}+s$, 则得

$$
f(f(y))=y, \quad y \in \mathbf{R} .
$$

现证明解 $f(x)$ 必须满足的一些性质:

(a) $f$ 是满射; 这由 (2) 立得.

(b) $f$ 是单射;

事实上, 若存在 $y_{1} \neq y_{2}$ 使得 $f\left(y_{1}\right)=f\left(y_{2}\right)$, 则由 (2) 知

$$
0=f\left(f\left(y_{1}\right)\right)-f\left(f\left(y_{2}\right)\right)=y_{1}-y_{2} \neq 0
$$

矛盾!

(c) $f(0)=0$;

事实上, 在 (2) 中令 $y=0$ 得

$$
f(s)=f(f(0))=0=f\left(s^{2}+s\right),
$$

再由 (b) 知 $s^{2}+s=s$, 故 $s=0$, 亦即 $f(0)=0$.

(d) 对任意实数 $x$ 有 $f^{2}(x)=x^{2}$;

在条件 (1) 中令 $y=0$ 得

$$
f\left(f^{2}(x)\right)=x f(x), \quad \forall x \in \mathbf{R}
$$

由 (a) 知对任意 $x \in \mathbf{R}$, 存在 $z \in \mathbf{R}$ 使得 $f(z)=x$.

这时由 (3), (2) 可得

$$
f\left(x^{2}\right)=f\left(f^{2}(z)\right)=z f(z)=f(f(z)) f(z)=x f(x)=f\left(f^{2}(x)\right),
$$

再由 (b) 知 $f^{2}(x)=x^{2},(\mathrm{~d})$ 得证.

现在我们可断言 $f(x)=x$ 或 $f(-x)=-x$ 是问题的解. 事实上, 由 (d) 知 $f^{2}(x)=x^{2}$. 若存在 $x \in \mathbf{R}$ 使 $f(x)=-x$, 且同时存在 $y \in \mathbf{R}$ 使 $f(y)=y$, 此时将 $f(x)=-x, f(y)=y$ 代入 (1) 得

$$
f\left(x^{2}+y\right)=y-x^{2}
$$

但由 (d) 知 $f\left(x^{2}+y\right)=x^{2}+y$ 或 $f\left(x^{2}+y\right)=-\left(x^{2}+y\right)$, 均与 (4) 矛盾! 这就证明了断言成立.

题 8. 设正整数 $n>3, x_{1}, x_{2}, \cdots, x_{n}$ 是 $n$ 个正数, 满足 $x_{1} x_{2} \cdots x_{n}=1$. 证明:

$$
\frac{1}{1+x_{1}+x_{1} x_{2}}+\frac{1}{1+x_{2}+x_{2} x_{3}}+\cdots+\frac{1}{1+x_{n}+x_{n} x_{1}}>1
$$

(2004，俄罗斯)

在书 [3] 和 [4] 中介绍了该问题的如下十分巧妙的解法.

证法一 用如下方法减少各个加项:

$$
\begin{aligned}
& \frac{1}{1+x_{1}+x_{1} x_{2}}+\frac{1}{1+x_{2}+x_{2} x_{3}}+\cdots+\frac{1}{1+x_{n}+x_{n} x_{1}} \\
> & \frac{1}{1+x_{1}+x_{1} x_{2}+x_{1} x_{2} x_{3}+\cdots+x_{1} x_{2} \cdots x_{n-1}} \\
& +\frac{1}{1+x_{2}+x_{2} x_{3}+x_{2} x_{3} x_{4}+\cdots+x_{2} x_{3} \cdots x_{n}}+\cdots \\
& +\frac{1}{1+x_{n}+x_{n} x_{1}+x_{n} x_{1} x_{2}+\cdots+x_{n} x_{1} x_{2} \cdots x_{n-2}} .
\end{aligned}
$$

将第一个分式的分子分母同时乘以 $x_{n}$; 将第二个分式的分子分母同时乘以 $x_{n} x_{1} ; \cdots$; 将第 $n$ 个分式的分子分母同时乘以 $x_{n} x_{1} x_{2} \cdots x_{n-1}$, 并考虑到 $x_{1} x_{2} \cdots x_{n}=1$. 我们得到

$$
\frac{1}{1+x_{1}+x_{1} x_{2}}+\frac{1}{1+x_{2}+x_{2} x_{3}}+\cdots+\frac{1}{1+x_{n}+x_{n} x_{1}}
$$

$$
\begin{aligned}
> & \frac{x_{n}}{x_{n}+x_{n} x_{1}+x_{n} x_{1} x_{2}+x_{n} x_{1} x_{2} x_{3}+\cdots+x_{n} x_{1} x_{2} \cdots x_{n-1}} \\
& +\frac{x_{n} x_{1}}{x_{n} x_{1}+x_{n} x_{1} x_{2}+x_{n} x_{1} x_{2} x_{3}+x_{n} x_{1} x_{2} x_{3} x_{4}+\cdots+x_{n} x_{1} x_{2} x_{3} \cdots x_{n-1}+x_{n}} \\
& +\cdots+\frac{x_{n} x_{1} x_{2} x_{3} \cdots x_{n-1}}{x_{n} x_{1} x_{2} x_{3} \cdots x_{n-1}+x_{n}+x_{n} x_{1}+x_{n} x_{1} x_{2}+\cdots+x_{n} x_{1} x_{2} \cdots x_{n-2}} . \\
= & 1 .
\end{aligned}
$$

下面的解法是一个经典的代换 (代换的合理性请同学们思考): 令

$$
x_{i}=\frac{a_{i+1}}{a_{i}}, i=1,2, \cdots, n
$$

其中 $a_{n+1}=a_{1}$. 通过这个代换， “消化”了条件 $x_{1} x_{2} \cdots x_{n}=1$, 而将不等式齐次化了.

证法二 作代换

$$
x_{1}=\frac{a_{2}}{a_{1}}, x_{2}=\frac{a_{3}}{a_{1}}, \cdots, x_{n}=\frac{a_{1}}{a_{n}}
$$

则所证不等式等价于

$$
\frac{a_{1}}{a_{1}+a_{2}+a_{3}}+\frac{a_{2}}{a_{2}+a_{3}+a_{4}}+\cdots+\frac{a_{n}}{a_{n}+a_{1}+a_{2}}>1 .
$$

下证 $(*)$.

因 $n>3$, 所以对任何 $1 \leq i \leq n$ 有

$$
a_{i}+a_{i+1}+a_{i+2}<a_{1}+a_{2}+\cdots+a_{n} .
$$

其中 $a_{n+1}=a_{1}, a_{n+2}=a_{2}$. 故

$$
(*) \text { 式左边 }>\sum_{i=1}^{n} \frac{a_{i}}{a_{1}+a_{2}+\cdots+a_{n}}=1 \text {. }
$$

题 9. 设 $x_{1}, x_{2}, \cdots, x_{n}, y_{1}, y_{2}, \cdots, y_{n}$ 是实数满足

$$
\sum_{k=1}^{n} x_{k}^{2}=\sum_{k=1}^{n} y_{k}^{2}=1
$$

证明:

$$
\left(x_{1} y_{2}-x_{2} y_{1}\right)^{2} \leq 2\left(1-\sum_{k=1}^{n} x_{k} y_{k}\right)
$$

(2001, 韩国)

证明 应用拉格朗日恒等式, 我们有

$$
\left(x_{1} y_{2}-x_{2} y_{1}\right)^{2} \leq \sum_{1 \leq i<j \leq n}\left(x_{i} y_{j}-x_{j} y_{i}\right)^{2}
$$

$$
\begin{aligned}
& =\left(\sum_{k=1}^{n} x_{k}^{2}\right)\left(\sum_{k=1}^{n} y_{k}^{2}\right)-\left(\sum_{k=1}^{n} x_{k} y_{k}\right)^{2} \\
& =1-\left(\sum_{k=1}^{n} x_{k} y_{k}\right)^{2} \\
& =\left(1-\sum_{k=1}^{n} x_{k} y_{k}\right)\left(1+\sum_{k=1}^{n} x_{k} y_{k}\right)
\end{aligned}
$$

而由 Cauchy不等式知

$$
\left|\sum_{k=1}^{n} x_{k} y_{k}\right| \leq\left(\sum_{k=1}^{n} x_{k}^{2}\right)^{\frac{1}{2}}\left(\sum_{k=1}^{n} y_{k}^{2}\right)^{\frac{1}{2}}=1
$$

因此

$$
0 \leq 1+\sum_{k=1}^{n} x_{k} y_{k} \leq 2
$$

综合 (1), (2) 便得所证结果.

评注. 上述解法的关键在于想到拉格朗日恒等式, 从而把局部一项放大到一个整体和.

题 10. 给定 $n \in \mathbf{N}^{*}$, 复数集

$$
M=\left\{z \in \mathbf{C} \left\lvert\, \sum_{k=1}^{n} \frac{1}{|z-k|} \geq 1\right.\right\}
$$

在复平面上对应的区域面积为 $A$. 证明:

$$
A \geq \frac{\pi}{12}\left(11 n^{2}+1\right)
$$

(Jeremy Bern, Crux Math. 1994)

这是十分有趣的且有难度的一个问题. 因为 $M$ 不是易于计算面积的图形.因此我们希望找 $M$ 的一个易计算面积的特殊子集, 因为不等式的右边有 $\pi$, 自然希望找的特殊子集是一个圆, 注意到 $M$ 可写为

$$
M=\left\{z \in \mathbf{C} \left\lvert\, \frac{n}{\sum_{k=1}^{n} \frac{1}{|z-k|}} \geq n\right.\right\}
$$

$M$ 中的不等式说明 $|z-1|,|z-2|, \cdots,|z-n|$ 的调和平均值不超过 $n$, 故下面几个集合:

$$
\begin{aligned}
& M_{1}=\left\{z \in \mathbf{C} \mid \sqrt[n]{\prod_{k=1}^{n}|z-k|} \leq n\right\}, \\
& M_{2}=\left\{\left.z \in \mathbf{C}\left|\frac{1}{n} \sum_{k=1}^{n}\right| z-k \right\rvert\, \leq n\right\},
\end{aligned}
$$

$$
M_{3}=\left\{z \in \mathbf{C} \left\lvert\, \frac{\sqrt{\prod_{k=1}^{n}|z-k|^{2}}}{n} \leq n\right.\right\} .
$$

均是 $M$ 的子集. 但其中仅有 $M_{3}$ 是圆, 这样问题就转化为计算圆 $M_{3}$ 的面积, 是一个较简单的问题.

证明 设 $N=\left\{z \in \mathbf{C} \left\lvert\, \sqrt{\frac{\sum_{k=1}^{n}|z-k|^{2}}{n}} \leq n\right.\right\}$, 则对任意的 $z \in N$ 有

$$
\sqrt{\frac{\sum_{k=1}^{n}|z-k|^{2}}{n}} \leq n
$$

因此

$$
\frac{n}{\sum_{k=1}^{n} \frac{1}{|z-k|}} \leq \sqrt{\frac{\sum_{k=1}^{n}|z-k|^{2}}{n}} \leq n,
$$

即

$$
\sum_{k=1}^{n} \frac{1}{|z-k|} \geq 1
$$

这说明 $z \in M$. 因此 $N \subseteq M$.

又注意到

$$
\begin{aligned}
& \sqrt{\frac{\sum_{k=1}^{n}|z-k|^{2}}{n}} \leq n \Leftrightarrow \sum_{k=1}^{n}(z-k)(\bar{z}-k) \leq n^{3} \\
& \Leftrightarrow \sum_{k=1}^{n}\left(z \bar{z}-k z-k \bar{z}+k^{2}\right) \leq n^{3} \\
& \Leftrightarrow z \bar{z}-\frac{n+1}{2}(z+\bar{z})+\frac{1}{6}(n+1)(2 n+1) \leq n^{3} \\
& \Leftrightarrow\left(z-\frac{n+1}{2}\right)\left(\bar{z}-\frac{n+1}{2}\right) \leq \frac{11 n^{2}+1}{12} \\
& \Leftrightarrow\left|z-\frac{n+1}{2}\right|^{2} \leq \sqrt{\frac{11 n^{2}+1}{12}} .
\end{aligned}
$$

这说明 $N$ 是复平面上以 $\frac{n+1}{2}$ 为圆心, 半径为 $\sqrt{\frac{11 n^{2}+1}{12}}$ 的一个圆, 其面积为 $\frac{\pi}{12}\left(11 n^{2}+1\right)$. 又 $N \subseteq M$, 故 $M$ 的面积 $A \geq \frac{\pi\left(11 n^{2}+1\right)}{12}$.

题 11. 设 $a_{1}, a_{1}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$ 为复数. 证明: 存在 $k \in\{1,2, \cdots, n\}$,使得

$$
\sum_{i=1}^{n}\left|a_{i}-a_{k}\right|^{2} \leq \sum_{i=1}^{n}\left|b_{i}-a_{k}\right|^{2}
$$

或

$$
\sum_{i=1}^{n}\left|b_{i}-b_{k}\right|^{2} \leq \sum_{i=1}^{n}\left|a_{i}-b_{k}\right|^{2}
$$

(王广廷, 2015 全国数学竟赛命题研讨会入选题)
证明 对任意 $j, k \in\{1,2, \cdots, n\}$, 记

$$
f_{j k}=\left(\left|b_{j}-a_{k}\right|^{2}-\left|a_{j}-a_{k}\right|^{2}\right)+\left(\left|a_{j}-b_{k}\right|^{2}-\left|b_{j}-b_{k}\right|^{2}\right) .
$$

要证明结论成立, 仅需证存在整数 $k(1 \leq k \leq n)$, 使得

$$
\sum_{j=1}^{n} f_{j k} \geq 0
$$

下面证明:

$$
\sum_{k=1}^{n} \sum_{j=1}^{n} f_{j k} \geq 0
$$

事实上,

$$
\begin{aligned}
f_{j k}= & \left(b_{j}-a_{k}\right)\left(\overline{b_{j}}-\overline{a_{k}}\right)-\left(a_{j}-a_{k}\right)\left(\overline{a_{j}}-\overline{a_{k}}\right)+ \\
& \left(a_{j}-b_{k}\right)\left(\overline{a_{j}}-\overline{b_{k}}\right)-\left(b_{j}-b_{k}\right)\left(\overline{b_{j}}-\overline{b_{k}}\right) \\
= & -b_{j} \overline{a_{k}}-a_{k} \overline{b_{j}}+a_{j} \overline{a_{k}}+a_{k} \overline{a_{j}}- \\
& a_{j} \overline{b_{k}}-b_{k} \overline{a_{j}}+b_{j} \overline{b_{k}}+b_{k} \overline{b_{j}} \\
= & \left(a_{j}-b_{j}\right)\left(\overline{a_{k}}-\overline{b_{k}}\right)+\left(\overline{a_{j}}-\overline{b_{j}}\right)\left(a_{k}-b_{k}\right) .
\end{aligned}
$$

记 $a_{j}-b_{j}=c_{j}(j=1,2, \cdots, n)$. 则

$$
\begin{aligned}
\sum_{k=1}^{n} \sum_{j=1}^{n} f_{j k} & =\sum_{k=1}^{n} \sum_{j=1}^{n}\left(c_{j} \overline{c_{k}}+\overline{c_{j}} c_{k}\right) \\
& =\left(\sum_{k=1}^{n} \overline{c_{k}}\right)\left(\sum_{k j=1}^{n} c_{j}\right)+\left(\sum_{k=1}^{n} c_{k}\right)\left(\sum_{j=1}^{n} \overline{c_{j}}\right) \\
& =2\left|c_{1}+c_{2}+\cdots+c_{n}\right|^{2} \geq 0 .
\end{aligned}
$$

式 (2) 成立.

由式 (2), 知必存在整数 $k(1 \leq k \leq n)$, 使得式 (1) 成立, 证毕.

## 参考文献

[1] T. Andreescu, V. Cirtoaje, G. Dospinescu and M. Lascu, Old and New inequalities, GIL Publishing House, 2004.

[2] 王伟叶, 熊斌, 函数迭代与函数方程, 上海科技教育出版社, 2010.

[3] 2004 年 IMO中国国家集训队教练组, 走向 IMO, 数学奥林匹克试题集锦 (2004), 华东师范大学出版社出版, 2004.

[4] H. X. 阿伽汉诺夫主编, 苏淳译, 全俄中学生数学奥林匹克.

