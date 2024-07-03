数学新星网 当学生专栏

www.nsmath.cn/xszl

# 2020 IMO 预选题及其解答 

## 张潇瀚

(北京市实验中学，100037)

指导教师：陈晨（学而思数学竞赛主教练）

这是 2020 年 IMO 的预选题及解答. 每年的 IMO 六道试题都是各国领队从当年的 IMO 预选题中通过投票选出来的, 而预选题是由主办国成立一个选题委员会从各国提供的大量问题中遴选而得. 由于 IMO 的预选题有一年的保密期, 因此目前我们只能看到 2020 年及之前的预选题. 2020 年的预选题共有 32 道, 四个板块一般数字越大难度越大, IMO 的预选题是专家们通过讨论选择出来的, 绝大多数质量很高, 风格与 IMO 考题类似, 非常适合准备冬令营及以上考试的同学们参考并作为训练资料.

陈晨老师评析：A6, A8 是非常有趣的函数方程, 尤其 A8 非常有新意, C6 也非常有想法. G 组题目中规中矩, G9 非常有创意但是有点偏, 而且归为 $\mathrm{C}$ 组题目更合理. N2 的构造不错, N6 很有趣.

解答经由清华大学的孙孟越同学帮助修改润色, 我们已尽力将解答写得清晰易懂, 但仍不免有瑕疵，欢迎批评指正.

## I. 代数

A1 版本 1. 给定正整数 $n$, 并令 $N=2^{n}$. 试确定最小的实数 $a_{n}$ 使得对任意实数 $x$ 都有

$$
\sqrt[N]{\frac{x^{2 N}+1}{2}} \leq a_{n}(x-1)^{2}+x
$$

版本 2. 对任意正整数 $N$, 试确定最小的实数 $b_{N}$ 使得对任意实数 $x$ 都有

$$
\sqrt[N]{\frac{x^{2 N}+1}{2}} \leq b_{N}(x-1)^{2}+x
$$

版本 1 :

解:
首先, 我们证明 $a_{n}<\frac{N}{2}$ 时, 存在一个 $x$ 使得

$$
\sqrt[N]{\frac{x^{2 N}+1}{2}}>a_{n}(x-1)^{2}+x
$$

我们令 $x=1+t, t>0$. 只用找到 $t$ 满足

$$
\frac{(1+t)^{2 N}+1}{2}>\left(1+t+a_{n} t^{2}\right)^{N} .
$$

上式右端减去左端可以展开成关于 $t$ 的多项式, 按 $t$ 升幂排列的前几项为

$$
\left(N a_{n}-\frac{N^{2}}{2}\right) t^{2}+c_{3} t^{3}+\cdots .
$$

当 $t$ 是充分小的正数时, 上式和二次项的符号相同, 为负数, 故成立!

下证: $N=2^{n}$ 时,

$$
\sqrt[N]{\frac{1+x^{2 N}}{2}} \leq x+\frac{N}{2}(x-1)^{2}
$$

这样我们就得到 $a_{n}=\frac{N}{2}$.

证明 我们对 $n$ 归纳, $n=0$ 是等式.

假设 $N=2^{n}$ 时成立, $N=2^{n+1} \geq 2$ 时:

$$
\begin{aligned}
\left(x+N(x-1)^{2}\right)^{2} & =x^{2}+N^{2}(x-1)^{4}+N(x-1)^{2}\left(\frac{(x+1)^{2}-(x-1)^{2}}{2}\right) \\
& =x^{2}+\frac{N}{2}\left(x^{2}-1\right)^{2}+\left(N^{2}-\frac{N}{2}\right)(x-1)^{4} \\
& \geq x^{2}+\frac{N}{2}\left(x^{2}-1\right)^{2} \geq \sqrt[N]{\frac{1+x^{4 N}}{2}} .
\end{aligned}
$$

上面最后一步对 $x^{2}$ 用到了归纳假设. 又 $x+N(x-1)^{2}>0(x \geq 0$ 时显然,

$$
\begin{aligned}
x<0 \text { 时, } x+N(x-1)^{2} & \left.\geq x+(x-1)^{2}>0 .\right) \\
& \Longrightarrow x+N(x-1)^{2} \geq \sqrt[2 N]{\frac{1+x^{4 N}}{2}} .
\end{aligned}
$$

版本 2 :

解: 首先, 若 $x=-1$, 直接得 $b_{N} \geq \frac{1}{2}$.

若 $x \neq-1$, 可设 $x=\frac{1+d}{1-d}$. 则原不等式等价于

$$
(1+d)^{2 N}+(1-d)^{2 N} \leq 2\left(\left(4 b_{N}-1\right) d^{2}+1\right)^{N} .
$$

令 $d \rightarrow 0$, 得:

$$
2\left(\begin{array}{c}
2 N \\
2
\end{array}\right) \leq 2\left(\begin{array}{c}
N \\
1
\end{array}\right)\left(4 b_{N}-1\right) \Longrightarrow b_{N} \geq \frac{N}{2}
$$

其次, 对 $b_{N}=\frac{N}{2}$, 我们证明 (1) 成立.

(1) 两端都是关于 $d$ 的多项式, 并且 $d$ 的奇数次项系数都是 0 . 所以我们只用证明: 对 $1 \leq i \leq N,(1)$ 左式中 $d^{2 i}$ 系数不大于右式中该项系数.

即

$$
2\left(\begin{array}{c}
2 N \\
2 i
\end{array}\right) \leq(2 N-1)^{i} \cdot 2\left(\begin{array}{c}
N \\
i
\end{array}\right)
$$

展开, 等价于

$$
\frac{(2 N)(2 N-1)(2 N-2) \cdots(2 N-2 i+1)}{(2 i)(2 i-1)(2 i-2) \cdots 1} \leq(2 N-1)^{i} \frac{(2 N)(2 N-2) \cdots(2 N-2 i+2)}{(2 i)(2 i-2) \cdots 2} .
$$

约去两边的公因子得到

$$
\frac{(2 N-1)(2 N-3)(2 N-2 i+1)}{(2 i-1)(2 i-3) \cdots 1} \leq(2 N-1)^{i}
$$

上式左边分子不大于右边, 分母大于等于 1 . 故成立. 所以 $b_{N}=\frac{N}{2}$.

注：版本 1 很容易想到用归纳法解决. 版本 2 则非常困难，能想到要将 $x=1$ 换成一个系数为正的式子, 但换元 $x=\frac{1+d}{1-d}$ 不太明显.

A2 令 $\mathcal{A}$ 为全体以 $x, y, z$ 为三变量的整系数多项式构成的集合. 其子集 $\mathcal{B}$ 是由所有可以被表为

$$
(x+y+z) P(x, y, z)+(x y+y z+z x) Q(x, y, z)+x y z R(x, y, z)
$$

形式的多项式构成的集合, 其中 $P, Q, R \in \mathcal{A}$. 试确定最小的非负整数 $n$, 使得对任意满足 $i+j+k \geq n$ 的非负整数 $i, j, k, x^{i} y^{j} z^{k} \in \mathcal{B}$.

解: 首先, 我们证明: $x^{2} y \notin \mathcal{B}$.

用反证法, 设 $x^{2} y \in \mathcal{B}$. 设

$$
x^{2} y=(x+y+z) P(x, y, z)+(x y+y z+x z) Q(x, y, z)+x y z R(x, y, z)
$$

考虑 (1) 中 $x^{3}, y^{3}, z^{3}$ 的系数知 $P(x, y, z)$ 中没有 $x^{2}, y^{2}, z^{2}$ 项.

设 $P(x, y, z)$ 中的二次项部分是 $A x y+B x z+C y z . Q(x, y, z)$ 中的一次项部分是 $D x+E y+F z . R(x, y, z)$ 中的常数项是 $G$.

对比 (1) 式左右两边的所有三次项, 得 $x^{2} y=(x+y+z)(A x y+B x z+C y z)+(x y+x z+y z)(D x+E y+F z)+G x y z$对比此式左右的 $x y^{2}, x^{2} y, x z^{2}, x^{2} z, y^{2} z, y z^{2}$ 系数, 得

$$
A+E=0, A+D=1, B+F=0, B+D=0, C+E=0, C+F=0 \text {. }
$$

我们得到 $A+B+C+D+E+F$ 的两种表示

$$
\begin{aligned}
& (A+D)+(B+F)+(C+E)=1, \\
& (A+E)+(B+D)+(C+F)=0 .
\end{aligned}
$$

矛盾!

故 $n_{\min } \geq 4$. 下证 $n=4$ 成立.

由于对 $U, V \in \mathcal{A}$, 若 $U \in \mathcal{B}$, 必有 $U \cdot V \in \mathcal{B}$. 因此, 只需证

$$
x^{3} \in \mathcal{B}, x^{2} y z \in \mathcal{B}, x^{2} y^{2} \in \mathcal{B} .
$$

而

$$
\begin{aligned}
x^{3} & =(x+y+z) x^{2}-x(x y+x z+y z)+x y z \\
x^{2} y z & =x y z \cdot x \\
x^{2} y^{2} & =(x y+x z+y z) x y-(x+y) x y z
\end{aligned}
$$

故 (2) 成立, 因此 $n_{\min }=4$.

注: 很简单的多项式问题. 本题的一般形式如下: 称一个 $N$ 元整系数多项式 $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ 为好的, 如果其关于 $x_{1}, x_{2}, \ldots, x_{n}$ 对称且常数项是零, 令 $\mathcal{B}$为一切形如 $\sum_{i j}^{m} p_{i} q_{i}\left(q_{i}\right.$ 是整系数多项式, $p_{1}, \cdots p_{m}$ 是好多项式 $)$ 的多项式, 求最小的 $n$, 使得一切次数为 $n$ 的单项式属于 $\mathcal{B}$ (这个问题的答案是 $\left(\begin{array}{l}n \\ 2\end{array}\right)+1$ ).

A3 正实数 $a, b, c, d$ 满足 $(a+c)(b+d)=a c+b d$. 试确定

$$
\frac{a}{b}+\frac{b}{c}+\frac{c}{d}+\frac{d}{a}
$$

的最小可能值.

解法 1: 不妨设 $a c \geq b d$. 记 $x=\frac{a}{b}, y=\frac{c}{d}$. 则 $x y \geq 1$ 且

$$
(b x+d y)(b+d)=b d(x y+1)
$$

整理, 并使用均值不等式得

$$
\begin{aligned}
b d(x y+1-x-y)= & b^{2} x+d^{2} y \geq 2 \sqrt{x y} \cdot b d \Longrightarrow x y-x-y+1 \geq 2 \sqrt{x y} . \\
& \Longrightarrow(\sqrt{x y}-1)^{2} \geq x+y \geq 2 \sqrt{x y}
\end{aligned}
$$

将上式视为 $\sqrt{x y}$ 的二次不等式, 解得 $\sqrt{x y} \geq 2+\sqrt{3}$. 于是

$$
\begin{aligned}
\frac{a}{b}+\frac{b}{c}+\frac{c}{d}+\frac{d}{a} & \geq 2 \sqrt{\frac{a c}{b d}}+2 \sqrt{\frac{b d}{a c}} \\
& =2\left(\sqrt{x y}+\frac{1}{\sqrt{x y}}\right)
\end{aligned}
$$

$$
\geq 2(2+\sqrt{3}+2-\sqrt{3})=8
$$

又 $a=c=2+\sqrt{3}, b=d=1$ 时, 原式 $=8$. 故所求为 8 .

## 解法 2:

记 $a b=C, b c=A, c a=B$ 都是正数. 不妨设 $a c \geq b d$, 由齐次性, 可以不妨设 $a b c d=1$. 条件化为

$$
(a+c)\left(b+\frac{1}{a b c}\right)=a c+\frac{1}{a c} .
$$

等价于

$$
A+\frac{1}{A}+C+\frac{1}{C}=B+\frac{1}{B}
$$

所求式子化为

$$
\begin{aligned}
S & =\frac{c}{d}+\frac{a}{b}+\frac{b}{c}+\frac{d}{a} \\
& =\left(b c+\frac{1}{b c}\right) a c+\left(a b+\frac{1}{a b}\right) \frac{1}{a c} \\
& =\left(A+\frac{1}{A}\right) B+\left(C+\frac{1}{C}\right) \frac{1}{B} \\
& =\left(A+\frac{1}{A}\right)\left(B-\frac{1}{B}\right)+\left(B+\frac{1}{B}\right) \frac{1}{B} \\
& \geq 2\left(B-\frac{1}{B}\right)+\left(B+\frac{1}{B}\right) \frac{1}{B} \\
& =2 B+\left(1-\frac{1}{B}\right)^{2} .
\end{aligned}
$$

其中, 我们用到了 $B=a c \geq \sqrt{a b c d}=1$. 由于

$$
B+\frac{1}{B}=A+\frac{1}{A}+C+\frac{1}{C} \geq 4 \text {. }
$$

所以 $B \geq 2+\sqrt{3}$.

由于 $2 x$ 和 $\left(1-\frac{1}{x}\right)^{2}$ 都在 $[1, \infty)$ 上递增, 所以

$$
S \geq 2(2+\sqrt{3})+\left(1-\frac{1}{2+\sqrt{3}}\right)^{2}=8 .
$$

等号在 $a=c=1, b=d=2+\sqrt{3}$ 时可取到.

注: 两个解答都使用了换元, 解法 1 的换元由 $S$ 的形式引出; 解法 2 的换元由条件引出.

A4 实数 $a, b, c, d$ 满足 $a \geq b \geq c \geqslant d>0$ 且 $a+b+c+d=1$. 证明:

$$
(a+2 b+3 c+4 d) a^{a} b^{b} c^{c} d^{d}<1 .
$$

解法 1: 首先, 由 $a+b+c+d=1$ 与加权均值不等式, 知

$$
a^{a} b^{b} c^{c} d^{d} \leq a \cdot a+b \cdot b+c \cdot c+d \cdot d=\sum_{s y m} a^{2} .
$$

因此只需证 $(a+2 b+3 c+4 d) \sum_{\text {sym }} a^{2}<1$. 这等价于

$$
(a+2 b+3 c+4 d)\left(a^{2}+b^{2}+c^{2}+d^{2}\right)<(a+b+c+d)^{3} .
$$

两边减去 $(a+b+c+d)\left(a^{2}+b^{2}+c^{2}+d^{2}\right)$, 等价于

$$
(b+2 c+3 d)\left(a^{2}+b^{2}+c^{2}+d^{2}\right)<2(a+b+c+d) \sum_{\text {sym }} a b
$$

利用 $a \geq b \geq c \geq d$ 我们即有

$$
\begin{aligned}
& a^{2}(b+2 c+3 d) \leq a(2 a b+2 a c+2 a d)<2 a \sum_{\text {sym }} a b . \\
& b^{2}(b+2 c+3 d) \leq b(2 a b+2 b c+2 b d)<2 b \sum_{\text {sym }} a b . \\
& c^{2}(b+2 c+3 d) \leq c(2 a c+2 b c+2 d c)<2 c \sum_{\text {sym }} a b . \\
& d^{2}(b+2 c+3 d) \leq d(2 a d+2 b d+2 c d)<2 d \sum_{\text {sym }} a b .
\end{aligned}
$$

相加即得.

## 解法 2:

记 $t=a+2 b+3 c+4 d \leq a+3(b+c+d)=3-2 a$. 那么 $2-a-a t \geq$ $2-a-a(3-2 a)=2(a-1)^{2} \geq 0$. 于是

$$
a^{2-a-a t} b^{c+2 d} \geq b^{2-a-a t+c+2 d}=b^{t-a t}=b^{b t+c t+d t} \geq b^{b t} c^{c t} d^{d t}
$$

整理得到

$$
a^{a t} b^{b t} c^{c t} d^{d t} \leq a^{a+2 b+2 c+2 d} b^{c+2 d} .
$$

利用加权均值不等式, 得

$$
\begin{aligned}
a^{a} b^{b} c^{c} d^{d} & \leq a^{\frac{a+2 b+2 c+2 d}{t}} b^{\frac{c+2 d}{t}} \\
& \leq \frac{a+2 b+2 c+2 d}{t} \cdot a+\frac{c+2 d}{t} \cdot b
\end{aligned}
$$

$$
<\frac{(a+b+c+d)^{2}}{t}=\frac{1}{t}
$$

得证.

解法 3: 若 $0<a<\frac{1}{2}$, 则

$$
\begin{aligned}
(a+2 b+3 c+4 d) a^{a} b^{b} c^{c} d^{d} & \leq(a+3(b+c+d))\left(a^{2}+b^{2}+c^{2}+d^{2}\right) \\
& \leq(a+3(b+c+d))\left(a^{2}+a(b+c+d)\right) \\
& =(3-2 a) \cdot a<1 .
\end{aligned}
$$

若 $a \geq \frac{1}{2}$, 则

$$
\begin{aligned}
(a+2 b+3 c+4 d) a^{a} b^{b} c^{c} d^{d} & \leq(a+3(b+c+d))\left(a^{2}+b^{2}+c^{2}+d^{2}\right) \\
& <(a+3(b+c+d))\left(a^{2}+(b+c+d)^{2}\right) \\
& =(3-2 a)\left(2 a^{2}-2 a+1\right) \\
& =1-2(a-1)^{2}(2 a-1) \leq 1 .
\end{aligned}
$$

得证.

解法 4: 只需证明

$$
(a+3(b+c+d))\left(a^{2}+b^{2}+c^{2}+d^{2}\right) \leq(a+b+c+d)^{3} .
$$

这等价于

$\Longleftrightarrow 2(b+c+d)\left[a(b+c+d)-b^{2}-c^{2}-d^{2}\right]+2(a+b+c+d)(b c+c d+b d) \geq 0$.

由于 $a \geq b \geq c \geq d$, 上式显然成立.

注: 2020 年 IMO 第 2 题. 想到使用加权平均不等式是解题关键.

A5 一位魔术师想要表演下面这个魔术。她首先向观众公布一个正整数 $n$和 $2 n$ 个实数 $x_{1}<\cdots<x_{2 n}$. 然后一位观众秘密地选取一个 $n$ 次实系数多项式 $P(x)$, 计算出 $P\left(x_{1}\right), \cdots, P\left(x_{2 n}\right)$ 这 $2 n$ 个值, 并将它们按照不减的顺序写在黑板上. 在此之后魔术师要猜出这个秘密选取的多项式, 并将它公布给观众.

魔术师能否找到一种策略来完成这个魔术?

解: 我们说魔法师没有这样的策略.
事实上, 由于关于 $a_{0}, a_{1}, \ldots, a_{n}$ 的齐次线性方程组

$$
\left\{\begin{array}{l}
a_{n}\left(x_{1}^{n}+x_{2}^{n}\right)+a_{n-1}\left(x_{1}^{n-1}+x_{2}^{n-1}\right)+\cdots+a_{1}\left(x_{1}+x_{2}\right)+2 a_{0}=0 \\
a_{n}\left(x_{3}^{n}+x_{4}^{n}\right)+a_{n-1}\left(x_{3}^{n-1}+x_{4}^{n-1}\right)+\cdots+a_{1}\left(x_{3}+x_{4}\right)+2 a_{0}=0 \\
\quad \vdots \\
a_{n}\left(x_{2 n-1}^{n}+x_{2 n}^{n}\right)+a_{n-1}\left(x_{2 n-1}^{n-1}+x_{2 n}^{n-1}\right)+\cdots+a_{1}\left(x_{2 n-1}+x_{2 n}\right)+2 a_{0}=0
\end{array}\right.
$$

的方程数小于未知数个数, 其必有非平凡解 $\left(a_{0}, a_{1}, a_{2}, \cdots, a_{n}\right)$. (非平凡解意味着不全为零的解)

我们就取

$$
f(x)=a_{0}+a_{1} x+\cdots+a_{n} x^{n}
$$

那么对 $k=1,2, \ldots, n, f\left(x_{2 k-1}\right)+f\left(x_{2 k}\right)=0$. 则由连续性, $f$ 在 $\left[x_{2 k-1}, x_{2 k}\right]$上必有实根. 由于区间 $\left[x_{2 k-1}, x_{2 k}\right]$ 对不同的 $k$ 不相交, 所以 $f$ 至少有 $n$ 个根,但 $f$ 至多 $n$ 次, 也不是零多项式. 于是 $f$ 是 $n$ 次多项式.

再令 $g(x)=-f(x)$, 则 $f, g$ 是不同的 $n$ 次多项式, 且

$$
\left\{f\left(x_{1}\right), f\left(x_{2}\right), \ldots, f\left(x_{2 n}\right)\right\}=\left\{g\left(x_{1}\right), g\left(x_{2}\right), \ldots, g\left(x_{2 n}\right)\right\} .
$$

因此魔法师无法通过观众在黑板上写的 $2 n$ 个值来判断观众所选的是 $f$ 还是 $g$, 因此他没有必胜策略.

注: 用 $n=1$ 容易看出魔法师没有策略. 第一想法可能是去让 $f\left(x_{i}\right)=$ $g\left(x_{2 n+1-i}\right)$, 但实际上使 $f\left(x_{2 i-1}\right)=g\left(x_{2 i}\right), f\left(x_{2 i}\right)=g\left(x_{2 i-1}\right)$ 书写起来更方便.

$\mathbf{A 6}$ 试确定所有函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$, 使得对任意 $a, b \in \mathbb{Z}$, 都有

$$
f^{a^{2}+b^{2}}(a+b)=a f(a)+b f(b)
$$

其中 $f^{n}$ 表示函数 $f$ 的 $n$ 次迭代, 即 $f^{0}(x)=x$ 且对 $n \geq 0, f^{n+1}(x)=f\left(f^{n}(x)\right)$.

解: 令 $a=0, b=-1$ 得 $f(-1)=0$.

因此, 对 $a \in \mathbb{N}^{*}$, 条件中取 $b=-1$ 得到

$$
f^{a^{2}+1}(a-1)=a f(a) .
$$

条件中取 $b=0$, 并用 $a-1$ 代替 $a$ 得到

$$
f^{(a-1)^{2}}(a-1)=(a-1) f(a-1) .
$$

结合两式得到

$$
f^{2 a}((a-1) f(a-1))=a f(a) .
$$

利用这个式子递推得到

$a f(a)=f^{2 a}((a-1) f(a-1))=f^{2 a+2(a-1)}((a-2) f(a-2))=\cdots=f^{2 a+2(a-1)+\cdots+2}(0)$.

即 $a f(a)=f^{a(a+1)}(0)$. 在原条件中取 $b=0$ 得到 $f^{a^{2}}(a)=f^{a(a+1)}(0)$.

情形 1 . 若存在 $m, n \in N, m \neq n$, 使 $f^{m}(0)=f^{n}(0)$.

则 $0, f(0), f^{2}(0), \cdots$ 从某一项起是周期的, 进而绝对值有上界 $M$.

但 $a f(a)=f^{a(a+1)}(0)$ 对所有正整数 $a$ 成立, 这推出当 $a>M$ 时, $|f(a)|<1$,又 $f(a) \in \mathbb{Z}$, 故 $f(a)=0$, 于是 $f^{a(a+1)}(0)=0$.

故存在正整数 $N$, 使

$$
\begin{array}{r}
f^{N^{2}+N}(0)=0, \\
f^{(N+1)^{2}+N+1}(0)=0, \\
f^{(N+2)^{2}+N+2}(0)=0 .
\end{array}
$$

于是

$$
f^{2 N+2}(0)=0, f^{2 N+4}(0)=0 \Longrightarrow f(f(0))=0 \text {. }
$$

由 $a f(a)=f^{a(a+1)}(0)$, 知对所有正整数 $a, f(a)=0$.

在原条件中令 $b=-a$, 得 $f(a)=f(-a)$. 可以得到对所有的非零整数 $a$ 有 $f(a)=0$. 最后, $f(0)=f^{3}(0)=f^{4}(2)=2 f(2)=0$.

得到 $\forall a \in \mathbb{Z}, f(a)=0$. 容易验证满足题意.

情形 2. 若对任意正整数 $m, n$, 有 $f^{m}(0) \neq f^{n}(0)$.

取一个 $a=f^{s}(0), s \in \mathbb{N}^{*}$. 由 $f^{a^{2}}(a)=f^{a(a+1)}(0)$ 得

$$
f^{a^{2}+s}(0)=f^{a^{2}+a}(0) \Longrightarrow a=s \Longrightarrow f^{s}(0)=s
$$

利用归纳法不难得到 $f(a)=a+1$ 对任意自然数 $a$ 成立. 并且对正整数 $a, b$有 $f^{a}(b)=a+b$.

再在原条件式中令 $a=-b, a \in \mathbb{N}^{*}$, 得

$$
2 a^{2}=a(a+1)+(-a) \cdot f(-a) \Longrightarrow f(-a)=1-a
$$

得到 $\forall a \in \mathbb{Z}, f(a)=a+1$. 容易验证满足题意.

综上, 所求为 $f(x) \equiv 0$ 和 $f(x) \equiv x+1$.

注：本题的创新之处在于去在迭代次数上做文章. 想到去研究迭代序列 $\left\{f^{(i)}(0)\right\}$ 是解题关键.

A7 给定正整数 $n$ 和 $k$, 证明: 对 $a_{1}, \cdots, a_{n} \in\left[1,2^{k}\right]$, 有

$$
\sum_{i=1}^{n} \frac{a_{i}}{\sqrt{a_{1}^{2}+\ldots+a_{i}^{2}}} \leq 4 \sqrt{k n}
$$

## 解法 1:

记 $A_{i}=\left\{i \mid 2^{i-1} \leq a_{i}<2^{i}\right\},(i=1,2, \cdots, k-1) . A_{k}=\left\{i \mid 2^{k-1} \leq a_{i} \leq 2^{k}\right\}$



我们有估计

$$
\sum_{i=1}^{n} \frac{a_{i}}{\sqrt{a_{1}^{2}+\cdots+a_{i}^{2}}} \leq \sum_{j=1}^{k} \sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}} .
$$

我们只需要对非空的 $A_{j}$ 估计下式即可.

我们利用柯西不等式得到

$$
\sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}}
$$

$\left(\sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}}\right)^{2} \leq\left(\sum_{s=1}^{\left|A_{j}\right|} \frac{1}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}}\right)\left(\sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}^{2}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}}\right)$

利用 $a_{i_{j, t}} \geq 2^{j-1}$ 可得到

$$
\begin{aligned}
\sum_{s=1}^{\left|A_{j}\right|} \frac{1}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}} & \leq \frac{1}{2^{j-1}} \sum_{s=1}^{\left|A_{j}\right|} \frac{1}{\sqrt{s}} \\
& \leq \frac{1}{2^{j-1}} \sum_{s=1}^{\left|A_{j}\right|} \frac{2}{\sqrt{s-1}+\sqrt{s}} \\
& =\frac{1}{2^{j-1}} \sum_{s=1}^{\left|A_{j}\right|} 2(\sqrt{s}-\sqrt{s-1})=\frac{1}{2^{j-2}} \sqrt{\left|A_{j}\right|}
\end{aligned}
$$

另一边

$$
\begin{aligned}
\sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}^{2}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}} & \leq a_{i_{j, 1}}+\sum_{s=2}^{\left|A_{j}\right|} \frac{2 a_{i_{j, s}}^{2}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s-1}}^{2}}+\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}} \\
& \leq a_{i_{j, 1}}+2 \sum_{s=2}^{\left|A_{j}\right|}\left(\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}-\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s-1}}^{2}}\right) \\
& \leq 2 \sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, 1}\left|A_{j}\right|}^{2}} \\
& \leq 2^{j+1} \sqrt{\left|A_{j}\right|} .
\end{aligned}
$$

最后一步我们用到了 $a_{i_{j, t}} \leq 2^{j}$.
于是我们有

$$
\sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}} \leq\left(\frac{1}{2^{j-2}} \sqrt{\left|A_{j}\right|} \cdot 2^{j+1} \sqrt{\left|A_{j}\right|}\right)^{1 / 2}=2 \sqrt{2\left|A_{j}\right|} .
$$

最后, 求和, 并利用柯西不等式得到

$\sum_{j=1}^{k} \sum_{s=1}^{\left|A_{j}\right|} \frac{a_{i_{j, s}}}{\sqrt{a_{i_{j, 1}}^{2}+\cdots+a_{i_{j, s}}^{2}}} \leq \sum_{j=1}^{k} 2 \sqrt{2\left|A_{j}\right|} \leq 2 \sqrt{2 k \sum_{j=1}^{k}\left|A_{j}\right|}=2 \sqrt{2 k n}$.

这比原题的常数略好一些.

## 解法 2:

对 $n$ 归纳, $n \leq 16$ 时, 等式左边 $\leq n \leq 4 \sqrt{k n}$. 故成立.

设小于 $n$ 时, 不等式成立. 考虑 $n$ 时.

1) 若 $n$ 是偶数, 设 $n=2 t$, 令 $x_{s}=\frac{a_{s}}{\sqrt{a_{1}^{2}+\cdots+a_{s}^{2}}}$. 利用熟知的不等式 $e^{-x^{2}} \geq$ $1-x^{2}>0$ 得到

$$
e^{-x_{t+1}^{2}-\cdots-x_{2 t}^{2}} \geq\left(1-x_{t+1}^{2}\right) \cdots\left(1-x_{2 t}^{2}\right)=\frac{a_{1}^{2}+\cdots+a_{t}^{2}}{a_{1}^{2}+\cdot+a_{2 t}^{2}} \geq \frac{1}{1+4^{k}}
$$

最后我们用到了 $1 \leq a_{s} \leq 2^{k}$, 知 $a_{t+1}^{2}+\cdots+a_{2 t}^{2} \leq 4^{k}\left(a_{1}^{2}+\cdots+a_{t}^{2}\right)$.

$$
\Longrightarrow x_{t+1}^{2}+\cdots+x_{2 t}^{2} \leq \ln \left(4^{k}+1\right) \leq k \ln 5 \leq 2 k
$$

于是利用柯西不等式得到

$$
x_{t+1}+\cdots+x_{2 t} \leq \sqrt{2 k t} .
$$

利用归纳假设知

$$
\sum_{l=1}^{2 t} x_{l} \leq 4 \sqrt{k t}+\sqrt{2 k t}=(2 \sqrt{2}+1) \sqrt{k n}<4 \sqrt{k n} .
$$

2) 若 $n=2 t+1$

类似地, 有

$e^{-x_{t+2}^{2}-\cdots-x_{2 t+1}^{2}} \geq\left(1-x_{t+2}^{2}\right) \cdots\left(1-x_{2 t+1}^{2}\right)=\frac{a_{1}^{2}+\cdots+a_{t+1}^{2}}{a_{1}^{2}+\cdot+a_{2 t+1}^{2}} \geq \frac{1}{1+4^{k}}$

最后我们用到了 $1 \leq a_{s} \leq 2^{k}$, 知 $a_{t+2}^{2}+\cdots+a_{2 t+1}^{2} \leq 4^{k}\left(a_{1}^{2}+\cdots+a_{t+1}^{2}\right)$. 类似地, 有

$$
x_{t+2}^{2}+\cdots+x_{2 t+1}^{2} \leq \ln \left(4^{k}+1\right) \leq 2 k
$$

以及由柯西不等式，

$$
x_{t+2}+\cdots+x_{2 t+1} \leq \sqrt{2 k t} .
$$

于是利用归纳假设得到

$$
\sum_{l=1}^{2 t+1} x_{l} \leq 4 \sqrt{k(t+1)}+\sqrt{2 k t} \leq 4 \sqrt{k(2 t+1)}
$$

这里我们用到了

$$
4 \sqrt{2 t+1}-\sqrt{2 t} \geq 3 \sqrt{2 t}=\sqrt{18 t} \geq \sqrt{16 t+16}=4 \sqrt{t+1}
$$

综上, 命题获证.

注: 非常困难、优美的不等式问题. $k=1$ 时命题也是不平凡的. 解法 1 的精髓是下面这个十分漂亮的裂项手法:

$$
\begin{aligned}
\frac{a_{j_{i, s}}^{2}}{2 \sqrt{a_{j_{i, 1}}^{2}+\cdots+a_{j_{i, s}}^{2}}} & \leq \frac{a_{j_{i, s}}^{2}}{\sqrt{a_{j_{i, 1}}^{2}+\cdots+a_{j_{i, s-1}}^{2}}+\sqrt{a_{j_{i, 1}}^{2}+\cdots+a_{j_{i, s}}^{2}}} \\
& =\sqrt{a_{j_{i, 1}}^{2}+\cdots+a_{j_{i, s}}^{2}}-\sqrt{a_{j_{i, 1}}^{2}+\cdots+a_{j_{i, s-1}}^{2}} .
\end{aligned}
$$

笔者尝试过多种裂项手法, 但只有这一种起到了效果 (事实上, 这一解法证明了比原题还要强的不等式).

解法 2 巧妙的用到了 $1-x_{r}^{2}=\frac{a_{1}^{2}+\cdots+a_{r-1}^{2}}{a_{1}^{2}+\cdots+a_{r}^{2}}$ 这一裂项手法.

A8 记正实数集为 $\mathbb{R}^{+}$. 试确定所有函数 $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$, 使得对任意正实数 $x$ 和 $y$, 均有

$$
f(x+f(x y))+y=f(x) f(y)+1 .
$$

解法 1: 首先, 若存在 $x_{1} \neq x_{2}$, 使 $f\left(x_{1}\right)=f\left(x_{2}\right)$,

那么条件中取 $x=1, y=x_{1}$ 得到

$$
f\left(1+f\left(x_{1}\right)\right)+x_{1}=f(1) f\left(x_{1}\right)+1 .
$$

取 $x=1, y=x_{2}$ 得到

$$
f\left(1+f\left(x_{2}\right)\right)+x_{2}=f(1) f\left(x_{2}\right)+1 .
$$

得 $x_{1}=x_{2}$, 矛盾. 故 $f$ 为单射.

其次, 若存在 $x_{1}>x_{2}>0$. 使 $f\left(x_{1}\right)<f\left(x_{2}\right)$. 取

$$
x=\frac{x_{1}\left(f\left(x_{1}\right)-f\left(x_{2}\right)\right)}{x_{2}-x_{1}}, y=\frac{x_{2}-x_{1}}{f\left(x_{1}\right)-f\left(x_{2}\right)} .
$$

代人条件式得

$$
f\left(\frac{x_{2} f\left(x_{1}\right)-x_{1} f\left(x_{2}\right)}{x_{2}-x_{1}}\right)+\frac{x_{2}-x_{1}}{f\left(x_{1}\right)-f\left(x_{2}\right)}=f\left(\frac{x_{1}}{y}\right) f(y)+1
$$

再取

$$
x=\frac{x_{2}\left(f\left(x_{1}\right)-f\left(x_{2}\right)\right)}{x_{2}-x_{1}}, y=\frac{x_{2}-x_{1}}{f\left(x_{1}\right)-f\left(x_{2}\right)} .
$$

代人条件式得

$$
f\left(\frac{x_{2} f\left(x_{1}\right)-x_{1} f\left(x_{2}\right)}{x_{2}-x_{1}}\right)+\frac{x_{2}-x_{1}}{f\left(x_{1}\right)-f\left(x_{2}\right)}=f\left(\frac{x_{2}}{y}\right) f(y)+1
$$

由 (1),(2) 两式, $f\left(\frac{x_{1}}{y}\right)=f\left(\frac{x_{2}}{y}\right)$. 这与 $f$ 为单射矛盾! 故 $f$ 不减.

故 $f$ 在 0 处的右极限存在, 且不小于 0 . 我们记 $\lim _{x \rightarrow 0^{+}} f(x)=A$, 那么 $A \geq 0$, 所以 $f$ 在 $A$ 处的右极限也存在, 记 $\lim _{x \rightarrow A^{+}} f(x)=B$.

对固定的 $y>0$, 原条件式两边都是关于 $x$ 不减的, 所以可以令 $x \rightarrow 0^{+}$, 极限存在, 且有

$$
B+y=A f(y)+1
$$

由 $y$ 的任意性, 我们知道 $f$ 一定是线性函数. 之后的事情是平凡的, 设 $f(x)=$ $m x+n$, 代人易知 $f(x) \equiv x+1$.

## 解法 2:

定义 $g(x)=f(x)-x-1$. 有

$$
g(x+f(x y))=f(x) f(y)-f(x y)-x-y
$$

于是原条件化为

$$
g(x+f(x y))=g(y+f(x y)) .
$$

记 $f(1)=t$, 有

$$
g(x+t)=g\left(\frac{1}{x}+t\right)
$$

由原式, $f(x) f(3)>2 \Longrightarrow f(x)>\frac{2}{f(3)}>0$, 所以 $f$ 有正的下界.

记 $f$ 的一个下界为 $M>0$. 那么对任意正实数 $y$,

$$
f(y)>\frac{y-1}{M} .
$$

我们证明, 对有限区间 $[p, q] \subseteq \mathbb{R}^{+}, f(x)$ 在区间 $[p, q]$ 上有界. 我们已经证明了下界存在, 只需证明上界存在.

任取 $z \in[p, q]$, 记 $f(z)=s$.

在原式中代人 $y=1$, 得

$$
f(x+f(x))=f(1) f(x)=t f(x) .
$$

在 (4) 式中令 $x=z$, 得 $f(z+s)=t s$.
在 (4) 式中令 $x=z+s$, 得

$$
f(z+s+t s)=f(z+s+f(z+s))=t f(z+s)=t^{2} s .
$$

在条件中取 $x=z, y=\frac{z+s}{z}$, 再利用 (3) 可得

$$
f(z+t s)=f(z+f(z+s))=s f\left(\frac{z+s}{z}\right)+1 \geq \frac{s^{2}}{M z} .
$$

在条件中取 $x=z+t s, y=\frac{z}{z+t s}$ 可得

$$
\begin{aligned}
t^{2} s=f(z+s+t s) & =f\left(\frac{z}{z+t s}\right) f(z+t s)+\frac{t s}{z+t s} \\
& \geq M f(z+t s) \geq M\left(\frac{s^{2}}{M z}-\frac{s}{z}\right) \\
& =\frac{s^{2}}{z}-\frac{M s}{z} \geq \frac{s^{2}}{q}-\frac{M s}{p} .
\end{aligned}
$$

于是

$$
s \leq q\left(\frac{M}{p}+t^{2}\right)
$$

即 $f(z)$ 有上界. 取 $p=t=f(1), q=t+1$, 则有 $f(x)$ 在 $[t, t+1]$ 上有界,推出 $g(x)$ 在 $[t, t+1]$ 上有界.

再由 (2) 知: $g(x)$ 在 $[t,+\infty)$ 上有界. 取 $C=\max \{t, 3\}$, 下证 $x \geq C$ 时, $g(x)=0$.

在 (1) 中代人 $y=x$, 得

$$
\begin{aligned}
g\left(x+f\left(x^{2}\right)\right) & =f(x)^{2}-f\left(x^{2}\right)-2 x \\
\Longleftrightarrow g\left(x+f\left(x^{2}\right)\right)+g\left(x^{2}\right) & =f(x)^{2}-(x+1)^{2} \\
& =g(x)(f(x)+x+1) .
\end{aligned}
$$

由 $f(x)+x+1 \geq C+1 \geq 4$,

$$
\Longrightarrow|g(x)| \leq \frac{1}{4}\left(\left|g\left(x+f\left(x^{2}\right)\right)\right|+\left|g\left(x^{2}\right)\right|\right)
$$

因为 $C \geq t$, 所以 $|g|$ 在 $[C,+\infty)$ 上存在一个有限的上确界 $S=\sup _{x \geq C}|g(x)|$.

由于 $x \geq C \geq 4$, 所以 $x^{2}, x+f\left(x^{2}\right)$ 都在 $[C, \infty)$ 之内. 两边取上确界知, $S \leq \frac{1}{2} S \Longrightarrow S=0$. 即 $x \geq C$ 时, $|g(x)| \leq 0$, 推出 $f(x)=x+1$.

对 $0<y<C$, 取 $x>\max \left\{C, \frac{C}{y}\right\}$. 则 $x>C, x y>C, x+f(x y)>C$, 利用条件得到

$$
f(y)(x+1)=(y+1)(x+1) \Longrightarrow f(y)=y+1 .
$$

综上, $f(x)=x+1, \forall x \in \mathbb{R}^{+}$.

注: 困难的函数方程问题. $F$ 的定义域不含 0 导致代入特殊值对此题无效.
解答 1 用极限得到了与直接带入 0 类似的效果; 方法 2 则对 $f(x)$ 进行上下界估计, 夹逼出 $f(x)=x+1$.

## II. 组合

$\mathrm{C} 1$ 给定正整数 $n$, 试确定满足

$$
a_{1} \leq 2 a_{2} \leq 3 a_{3} \leq \ldots \leq n a_{n}
$$

的 $1,2, \cdots, n$ 的置换 $a_{1}, a_{2}, \cdots, a_{n}$ 的个数.

## 解:

对每个 $n$, 记这种序列的个数是 $S_{n}$.

若 $a_{t}=n$, 则由于 $\min \left\{a_{t}, \ldots, a_{n}\right\} \leq t$, 存在 $t \leq i \leq n$ 使得 $a_{i}=t$. 由于 $n t=t a_{t} \leq i a_{i}=i t$, 于是 $i \geq n$. 故 $i=n$. 于是对 $t \leq j \leq n$, 都有 $n t=t a_{t} \leq j a_{j} \leq n a_{n}=n t$.

若 $t \leq n-2 \Longrightarrow n-1|t n \Longrightarrow n-1| t$, 矛盾. 故 $t \geq n-1$.

$t=n$ 时, 此时由于 $(n-1)^{2}<n^{2}$, 所以 $a_{1}, a_{2}, \ldots, a_{n-1}$ 是 $1,2, \ldots, n-1$ 的任一满足 $a_{1} \leq 2 a_{2} \leq \cdots \leq(n-1) a_{n-1}$ 的排列皆可. 也就是有 $S_{n-1}$ 种情况.

$t=n-1$ 时, 必有 $a_{n}=n-1$. 此时由于 $(n-2)^{2}<n(n-1)$, 所以 $a_{1}, a_{2}, \ldots, a_{n-2}$ 是 $1,2, \ldots, n-2$ 的任一满足 $a_{1} \leq 2 a_{2} \leq \cdots \leq(n-2) a_{n-2}$ 的排列皆可. 也就是有 $S_{n-2}$ 种情况.

于是 $S_{n}=S_{n-1}+S_{n-2}$. 而 $S_{1}=1, S_{2}=2$, 可得 $S_{n}$ 为 $F_{n+1}$. 这里的 $F_{n}$ 是满足 $F_{1}=F_{2}=1$ 的斐波那契数列.

注. 是一个不难的问题. 从证明过程中可以刻画出所有满足条件的置换, 它们是由若干个不相交的相邻对换得到的，比如 (1)(23)(4)(5)(67).

C2 在一个正 100 边形中, 它的 41 个顶点被染成了黑色, 其余 59 个被染成了白色. 证明: 存在 24 个以正 100 边形顶点为顶点的凸四边形 $Q_{1}, \cdots, Q_{24}$,使得

- $Q_{1}, \cdots, Q_{24}$ 两两不交, 且
- 每个 $Q_{i}$ 都是由三个某一种颜色的顶点和一个另一种颜色的顶点构成的.

解:

每次我们如下操作:

1) 先计算余下顶点中的白点多还是黑点多. (如果一样多, 视为白点多)
2) 黑点多时, 在余下顶点中找到连续的 4 个点, 使其中有三黑一白, 将它们作为一个 $Q_{i}$ 的四个顶点, 并将它们去掉. 而在白点多时, 则找三白一黑.

直到不可操作为止.

我们先说明: 不可能在停止时, 仅余一种颜色的点.

用反证法, 先假设仅余黑点. 设经 $k$ 次操作后, 仅余黑点. 由于 $41<59 \cdot 3$,之前必有一次操作是去掉了一黑三白的正整数. 设最后一次去掉一黑三白为第 $s$ 次操作. 那么第 $s+1, s+2, \ldots, k$ 次操作都是去掉三黑一白.

由于每次操作后剩下 4 的倍数个点, 所以第 $k$ 次后至少余下 4 个黑点. 于是, 第 $s$ 次操作前, 黑点个数 $=1+4+3(k-s)>3+k-s=$ 白点个数, 于是第 $s$ 次操作违规! 矛盾!

如果仅余白点, 由 $59<41 \cdot 3$, 也可以得到类似的矛盾. 因此, 命题 $(\star)$ 成立.

设操作的终止状态为 $T$, 由 $(\star), T$ 中有白点, 亦有黑点.

$T$ 中不能有连续的三个同色点 (否则必有一异色点与之相邻, 可以继续操作, 矛盾). 将 $T$ 视为若干段连续的白/黑点, 则白黑段数一样多.

若 $T$ 中有长为 1 的段, 由 $T$ 不可继续操作, 任一个长为 1 的黑段的左右两段均长为 1 的白段. (否则, (i)(1)(2)()ㅣ形式可以操作) 同样地, 任一个长为 1 的白段的左右两段均长为 1 的黑段.

因此 $T$ 是黑白相间的. 给这些顶点编号 $1,2, \ldots, 4 k$. 那么奇数编号都是一种颜色, 偶数编号都是另一种颜色.

这时将 $1,2,3,4 k-1$ 和 $4,4 k-2,4 k-3,4 k-4$ 和 $5,6,7,4 k-5$ 等等取出即可. 得到至少 $k-1$ 个 $Q_{i}$, 结合前面操作得到的 $25-k$ 个 $Q_{i}$, 共得至少 24 个 $Q_{i}$, 即结论.

若 $T$ 中的每一段的长度至少为 2 , 则由于不能有长度大于 2 的段, 所以 $T$中每段长为 2 . 因此 $T$ 是两黑两白相间.

不妨设模 4 余 1,2 的编号是一种颜色, 模 4 余 3,4 的编号是另一种颜色. 这时将 $1,2,4 k-2,4 k-1$ 和 $3,4,4 k-3,4 k-4$ 等等作为 $k-1$ 个 $Q_{i}$. 结合前面操作得到的 $25-k$ 个 $Q_{i}$, 共得 24 个 $Q_{i}$. 证毕.

## 解法 2:

称三个顶点有同一个颜色, 另一个顶点上有不同颜色的四边形为好的四边形.

我们证明断言, 如果一个凸 $4 k+1$ 边形 $G$ 的每个顶点都被染成黑色/白色,
且两种颜色均被用 $\geq k$ 次, 则返 $4 k+1$ 个点中的某 $4 k$ 个点可以被分成 $k$ 个不相交的好四边形的顶点.

(事实上, 若断言成立, 则原命题显然成立, 即去掉 3 个点即可)

使用归纳法证明此断言.

$k=1$ 时, 如果黑点个数为偶, 则去掉一个黑点, 反之去掉一个白点, 则余下四个点构成一个好四边形的顶点.

假设 $1,2, \cdots, k-1$ 时断言成立. 在 $k$ 时,

设黑点有 $b$ 个, 白点有 $w$ 个, 则有 $b+w=4 k+1$.

不失一般地, 我们可以假设 $k \leq b \leq 2 k, 2 k+1 \leq w \leq 3 k+1$.

任取一个黑色顶点, 记为 $V_{1}$, 作 $V_{1}$ 开始顺时针给所有顶点标号 $V_{2}, V_{3}, \cdots, V_{4 k+1}$

考查 $k$ 个顶点组 $\left(V_{2}, V_{3}, V_{4}, V_{5}\right),\left(V_{6}, V_{7}, V_{8}, V_{9}\right), \cdots\left(V_{4 k-2}, V_{4 k-1}, V_{4 k}, V_{4 k+1}\right)$.

因为这 $4 k$ 个点中白点多于黑点, 因此, 其中必有一组为三白一黑或四白.

若为后者, 顺着四白一直往下找, 必能出现连续四个顶点三白一黑的构型.

因此, 我们总能找到连续四点染色为三白一黑, 将这四点作为一个好四边形, 由 $2 k+1-3 \geq k-1, k-1 \geq k-1$, 余下 $4 k-3$ 点可应用归纳假设.

综上, 断言成立, 进而命题成立.

注. 一个简单的想法是去找到连续的四个点, 使得其中三白一黑或三黑一白.

C3 给定整数 $n \geq 2$. 在一道山坡上共有 $n^{2}$ 个站点, 这些站点的编号从山脚到山顶依次为 $1,2, \cdots, n^{2}$. 两家缆车公司 $A$ 和 $B$ 分别拥有 $k$ 座缆车, 它们的编号分别为 $1,2, \cdots, k$, 每座缆车都承担着从某个站点向一个更高的站点的交通. 对每个公司的缆车 $i$ 和 $j$, 若 $1 \leq i<j \leq k$, 则缆车 $j$ 的起点比 $i$ 的起点高, 缆车 $j$ 的终点亦比 $i$ 的终点高. 若存在某个公司的缆车线路, 使得可以从两个站点中较低的一个, 一路搭乘该公司的缆车到较高的站点(其间不允许步行),则我们称这两个站点是关于某个公司连结的.

试确定最小的 $k$, 使得总能有两个站点关于两个公司均是连结的.

解: $k$ 的最小值是 $n^{2}-n+1$.

首先, 我们证明: $k=n^{2}-n$ 并不足以保证.

令第一个公司的缆车为: $i \rightarrow i+1,1 \leq i \leq n^{2}$ 且 $n \nmid i$.

第二个公司的缆车为: $i \rightarrow i+n, 1 \leq i \leq n^{2}-n$.
这样两个公司各经营的缆车数目为 $n^{2}-n$, 且满足 “起点更高的, 终点更高”的要求.

又考虑到第二个公司, 只能保证标号模 $n$ 同余的缆车互相抵达, 而第一个公司只能保证标号差小于 $n$ 的车站相互抵达, 故没有两个车站被两个公司同时连接.

$$
\Longrightarrow k_{\min } \geq n^{2}-n+1
$$

若两个公司各自经营 $n^{2}-n+1$ 个车站.

考虑其中一个公司, 设其 $n^{2}-n+1$ 辆缆车为: $a_{i} \rightarrow b_{i}\left(i=1,2, \cdots, n^{2}-n+1\right)$, $a_{1} \leq a_{2} \leq \cdots \leq a_{n^{2}-n+1}, b_{1} \leq b_{2} \leq \cdots \leq b_{n^{2}-n+1}$.

这些站点可以用链进行连接, 链的相邻顶点代表着有车站相连. 我们每次从所有站点中取出一条最长的链 (术语是极大链), 然后去掉这些顶点. 重复这个过程, 直到所有顶点都被取出. 设取出了 $s$ 条链.

$$
\begin{aligned}
& \text { 记为 } C_{1,1} \rightarrow C_{1,2} \rightarrow \cdots \rightarrow C_{1, t_{1}} \\
& C_{2,1} \rightarrow C_{2,2} \rightarrow \cdots \rightarrow C_{2, t_{2}} \\
& C_{s, 1} \rightarrow C_{s, 2} \rightarrow \cdots \rightarrow C_{s, t_{s}}
\end{aligned}
$$

有 $t_{1}+t_{2}+\cdots+t_{s}=n^{2}$. 由于每次取出的都是极大的链, 所以 $C_{1, t_{1}}, C_{2, t_{2}}, \cdots C_{s, t_{s}}$均不属于集合 $\left\{a_{1}, a_{2}, \cdots a_{n^{2}-n+1}\right\}$, 故有 $s \leq n-1$. 由 $\left\lceil\frac{n^{2}}{n-1}\right\rceil=n+2$, 有一条长度至少为 $n+2$ 的链. 记为 $C_{1} \rightarrow C_{2} \rightarrow \cdots \rightarrow C_{t}, t \geq n+2$.

对这 $n^{2}$ 个车站按照第二家公司的缆车线路, 也划分为极大不交链的并, 可以得到至多 $n-1$ 条链.

故 $C_{1}, C_{2}, \cdots, C_{t}$ 中必有二个属于第二家公司的同一链. 进而这两个站点被两个公司同时连接.

综上, $k_{\min }=n^{2}-n+1$.

注. 本题是 2020 年 IMO 第 4 题. 因为 $n^{2}$ 特征明显, 容易想到用 $n \times n$方阵构造. 证明时的想法是将整个图划分为不交的极大链的并.

$\mathbf{C 4}$ 斐波那契数是按如下方式归纳定义的: $F_{0}=0, F_{1}=1$, 且对 $n \geq 1$, $F_{n+1}=F_{n}+F_{n-1}$. 给定整数 $n \geq 2$, 若集合 $S$ 满足对任意 $k=2,3, \cdots, n$, 总有 $x, y \in S$ 使得 $x-y=F_{k}$, 试确定 $S$ 中元素个数的最小值.

解:

所求为 $\left\lceil\frac{n}{2}\right\rceil+1$
首先给出构造

$$
S_{n}=\left\{0, F_{2}, F_{4}, F_{6}, F_{8}, \cdots, F_{2 \cdot\left\lceil\frac{n}{2}\right\rceil}\right\} .
$$

由于 $F_{2 k-1}=F_{2 k}-F_{2 k-2}, F_{2 k}=F_{2 k}-0$, 知 $S_{n}$ 满足题意.

下证 $|S| \geq\left\lceil\frac{n}{2}\right\rceil+1$

将 $S$ 的每个元素视作一个点, 对满足

$$
x-y \in\left\{F_{2}, F_{3}, F_{5}, F_{7}, \ldots, F_{2\left\lceil\frac{n}{2}\right\rceil-1}\right\} .
$$

的 $x, y \in S$, 我们在 $x, y$ 间连一条边. 那么显然没有自环, 并且我们得到了一个简单图. 这个图有至少 $\left\lceil\frac{n}{2}\right\rceil$ 条边.

又

$$
\begin{gathered}
F_{3}>F_{2} . \\
F_{5}>F_{3}+F_{2} . \\
\vdots \\
F_{2\left\lceil\frac{n}{2}\right\rceil-1}>F_{2\left\lceil\frac{n}{2}\right\rceil-3}+\cdots+F_{3}+F_{2} .
\end{gathered}
$$

故这个图中无圈, 故顶点数大于边数, 即 $|S|>\left\lceil\frac{n}{2}\right\rceil$.

综上 $|S|_{\min }=\left\lceil\frac{n}{2}\right\rceil+1$.

注. 核心点是想到利用图去证明.

C5 给定奇素数 $p$, 并令 $N=\frac{1}{4}\left(p^{3}-p\right)-1$. 将 $1,2, \cdots, N$ 这些数任意染成红蓝两色, 对任意正整数 $n \leq N$, 令 $r(n)$ 表示集合 $\{1,2, \cdots, n\}$ 中红色元素的比例. 证明: 存在一个正整数 $a \in\{1,2, \cdots, p-1\}$ 使得对 $n=1,2, \cdots, N$ 都有 $r(n) \neq a / p$.

解. 用反证法, 假设结论不成立. 对 $1 \leq a \leq p-1$, 设 $1 \leq n_{a} \leq N$, 使 $r\left(n_{a}\right)=\frac{a}{p}$. 显然 $p \mid n_{a}$. 设 $n_{a}=p t_{a}, t_{a} \in \mathbb{N}_{+}$且两两不同.

不妨设 $t_{1}<t_{p-1}$ (否则可以把所有元素的红蓝色对换, 不影响结论). 记 $A=\left\{a: t_{a}<t_{p-1}\right\}, B=\left\{b: t_{b} \geq t_{p-1}\right\}$. 有 $A \cup B=\{1, \cdots, p-1\}, A \cap B=\varnothing$,且 $1 \in A, p-1 \in B$. 令 $b=\min B$, 则有 $b>1$ 且 $\{1, \cdots, b-1\} \subseteq A$. 再令 $t_{a}=\max \left\{t_{1}, \cdots, t_{\left\lceil\frac{b}{2}\right\rceil}\right\}$, 有 $1 \leq a \leq\left\lceil\frac{b}{2}\right\rceil<b$ 且 $t_{a} \geq\left\lceil\frac{b}{2}\right\rceil$. 前式意味着 $a \in A$.

由 $a \in A, b \in B$ 知 $t_{a}<t_{p-1} \leq t_{b}$. 考虑 $X_{1}=\left\{1,2, \ldots, p t_{a}\right\}, X_{2}=$ $\left\{1,2, \ldots, p t_{p-1}\right\}, X_{3}=\left\{1,2, \ldots, p t_{b}\right\} . X_{1} \subseteq X_{2} \subseteq X_{3}$, 而 $X_{1}, X_{2}$ 中分别有
$(p-a) t_{a}, t_{p-1}$ 个蓝色数, 所以 $(p-a) t_{a} \leq t_{p-1}$. 而 $X_{1}, X_{2}$ 中分别有 $(p-1) t_{p-1}, b t_{b}$个红色数, 所以我们有 $(p-1) t_{p-1} \leq b t_{b}$. 因此

$$
(p-1)(p-a) t_{a} \leq b t_{b}=b \cdot \frac{n_{b}}{p} \leq b \cdot \frac{N}{p}<\frac{1}{4} b\left(p^{2}-1\right) .
$$

故

$$
\frac{1}{4} b(p+1)>(p-a) t_{a}>\left(p-\left\lceil\frac{b}{2}\right\rceil\right)\left\lceil\frac{b}{2}\right\rceil>\left(p-\frac{b}{2}\right) \frac{b}{2} .
$$

这推出 $p+1>2 p-b$, 即 $b>p-1$, 矛盾!

注. $p=3,5,7$ 时, $\frac{1}{4}\left(p^{3}-p\right)-1$ 是最优的, 因为 $N=\frac{1}{4}\left(p^{3}-p\right)$ 时有以下反例:

- $p=3, N=6$ 时, 染红 1,2 .
- $p=5, N=30$ 时, 染红 $1,2,3,4,6,7$.
- $p=7, N=84$ 时, 染红 $1,2,3,4,5,6,8,9,10,11,15,16$.

$p \geq 11$ 时, 可以证明 $\frac{1}{4}\left(p^{3}-p\right)-1$ 不是最佳的.

C6 现有 $4 n$ 枚硬币, 它们分别重 $1,2, \cdots, 4 n$. 每枚硬币均被涂上 $n$ 种颜色之一, 且每种颜色的硬币恰有 4 枚. 证明: 这些硬币能被划分成总重相同的两组, 每组恰含每种颜色的硬币各两枚.

解. 将重量之和为 $4 n+1$ 的两硬币用线相连, 并将颜色相同的硬币重叠放置. 得到 $n$ 阶图 $G$ (不一定是简单图). $G$ 每个顶点度数均为 4 .

因此对 $G$ 的每个连通分支 $G_{i}$, 其总边数均为偶数, 记为 $2 n_{i}$; 且存在 $G_{i}$ 的 Euler 回路 $e_{i 1} \cdots e_{i, 2 n_{i}}\left(e_{i, j}\right.$ 代表边 $)$. 设 $e_{i, j}$ 连接了硬币 $A_{i, j}, B_{i, j}$, 且 $B_{i, j}$ 与 $A_{i, j+1}$ 同色 (这里令 $B_{i, 2 n_{i}+1}=B_{i, 1}$ ). 则 $A_{i, j}, B_{i, j}$ 不重复地表示了所有的硬币.

将硬币对分为 $\left\{A_{i, j}, B_{i, j}: 2 \mid j\right\}$ 和 $\left\{A_{i, j}, B_{i, j}: 2 \nmid j\right\}$ 两组. 则每对 $A_{i, j}, B_{i, j+1}$ 均同色而分属不同组. 因此每组恰含每种颜色的硬币各两枚. 而每组由 $n$ 对相连的硬币组成. 回忆相连的定义, 知两组的总重量相同.

注. 将这个问题转化为图论问题是关键. 变成图论问题后, 意识到偶圈对证明是有利的, 于是联想到一笔画问题.

C7 考察一个行列数有限的方形表格, 其行 $r$ 与列 $c$ 交点处的格子被填入了实数 $a(r, c)$. 对由一些行组成的集合 $R$ 与由一些列组成的集合 $C$, 称 $(R, C)$
是鞍对, 若其满足以下两个条件:

(i) 对每个行 $r^{\prime}$, 存在 $r \in R$ 使得对于任意 $c \in C$ 有 $a(r, c) \geq a\left(r^{\prime}, c\right)$;

(ii) 对每个列 $c^{\prime}$, 存在 $c \in C$ 使得对于任意 $r \in R$ 有 $a(r, c) \leq a\left(r, c^{\prime}\right)$.

称鞍对 $(R, C)$ 为极小对, 若对于所有 $R^{\prime} \subseteq R$ 和 $C^{\prime} \subseteq C$ 的鞍对 $\left(R^{\prime}, C^{\prime}\right)$, 都有 $R^{\prime}=R$ 和 $C^{\prime}=C$. 证明：任意两个极小对都有相同的行数.

解. 反设不然. 设 $(R, C)$ 与 $\left(R^{\prime}, C^{\prime}\right)$ 都是鞍对, 且 $|R|>\left|R^{\prime}\right|$.

记条件 (i) 中的 $r$ 为 $\rho_{R}\left(r^{\prime}\right)$, 条件 (ii) 中的 $c$ 为 $\sigma_{C}\left(c^{\prime}\right)$. 定义 $\rho=\rho_{R} \circ \rho_{R^{\prime}}$, $\sigma=\sigma_{C} \circ \sigma_{C^{\prime}}$. 对 $r \in R$ 和 $c \in C$, 有

$$
a(r, \sigma(c)) \leq a\left(r, \sigma_{C^{\prime}}(c)\right) \leq a\left(\rho_{R^{\prime}}(r), \sigma_{C^{\prime}}(c)\right) \leq a\left(\rho_{R^{\prime}}(r), c\right) \leq a(\rho(r), c) .
$$

记 $\rho^{n}$ 为 $\rho$ 的 $n$ 次迭代. 由 $\rho(R) \subseteq R$ 知对 $n \in \mathbb{N}_{+}, \rho^{n+1}(R)=\rho^{n}(\rho(R)) \subseteq$ $\rho^{n}(R)$. 由于 $R$ 有限, 存在 $k_{1}$ 使 $n \geq k_{1}$ 时, $\rho^{n}(R)=\rho^{k_{1}}(R)$. 同理, 存在 $k_{2}$ 使 $n \geq k_{2}$ 时, $\sigma^{n}(R)=\sigma^{k_{2}}(R)$. 记 $k=\max \left\{k_{1}, k_{2}\right\}$.

由于 $\rho\left(\rho^{k}(R)\right)=\rho^{k+1}(R)=\rho^{k}(R)$. 因此 $\rho$ 在 $\rho^{k}(R)$ 上的限制是 $\rho^{k}(R)$ 到自身的一一对应. 记 $n=\left|\rho^{k}(R)\right|$. 对 $r \in \rho^{k}(R)$, 由抽居原理, 存在 $1 \leq m_{1}<$ $m_{2} \leq n+1$ 使 $\rho^{m_{1}}(r)=\rho^{m_{2}}(r)$. 因此 $\rho^{m_{2}-m_{1}}(r)=r$. 由 $1 \leq m_{2}-m_{1} \leq n$ 知 $\left(m_{2}-m_{1}\right) \mid k n !$. 故 $\rho^{k n !}(r)=r$. 同理, 对 $c \in \sigma^{k}(C), \sigma^{k n !}(c)=c$.

下证明 $\left(\rho^{k}(R), \sigma^{k}(C)\right)$ 是鞍对. 对行 $r^{\prime}$, 取 $r=\rho^{k n !}\left(\rho_{R}\left(r^{\prime}\right)\right) \in \rho^{k}(R)$. 对 $c \in \sigma^{k}(C)$, 反复运用 $(*)$ 式, 有

$$
\begin{aligned}
a(r, c) & =a\left(\rho^{k n !}\left(\rho_{R}\left(r^{\prime}\right)\right), c\right) \geq a\left(\rho^{k n !-1}\left(\rho_{R}\left(r^{\prime}\right)\right), \sigma(c)\right) \geq \cdots \\
& \geq a\left(\rho_{R}\left(r^{\prime}\right), \sigma^{k n !}(c)\right)=a\left(\rho_{R}\left(r^{\prime}\right), c\right) \geq a\left(r^{\prime}, c\right)
\end{aligned}
$$

故 (i) 满足. 同理 (ii) 满足.

因此 $\left(\rho^{k}(R), \sigma^{k}(C)\right)$ 是鞍对. $\varnothing \neq \rho^{k}(R) \subseteq R, \varnothing \neq \sigma^{k}(C) \subseteq C$, 而

$$
\left|\rho^{k}(R)\right| \leq|\rho(R)|=\left|\rho_{R}\left(\rho_{R^{\prime}}(R)\right)\right| \leq\left|\rho_{R^{\prime}}(R)\right| \leq\left|R^{\prime}\right|<|R| .
$$

这与 $(R, C)$ 是极小对矛盾!

注. 困难的组合问题. 通过构造 $\rho, \sigma$, 我们找到对 $|\rho(R)|$ 的限制. 再利用 $\rho$ 迭代的像集不增, 我们反复迭代找出一个下界集合, $\rho$ 只能将它映为自身. 依此我们找到了 $(R, C)$ 的子集为鞍对.

C8 玩家 $A$ 和 $B$ 在黑板上玩一个游戏. 开始时, 黑板上有 2020 个数字 1.
每轮中玩家 $A$ 擦去黑板上的两个数 $x$ 和 $y$, 然后玩家 $B$ 在 $x+y$ 和 $|x-y|$ 中选一个写到黑板上. 若在某轮结束时, 满足下列条件之一:

(1) 黑板上有一个数大于其它全体数之和;

(2) 黑板上只剩若千个 0.

则此时游戏结束. 然后玩家 $B$ 需要给玩家 $A$ 等同于黑板上数的个数的曲奇, 玩家 $A$ 想获得尽可能多的曲奇, 而玩家 $B$ 想给出尽可能少的曲奇. 如果双方都按最佳策略进行游戏, 试确定玩家 $A$ 最终将获得的曲奇块数.

解. 首先我们证明, $A$ 有策略获得至少 7 块曲奇.

令 $A$ 如下操作: 若黑板上有两个相等的正数, 则选出它们. 这样, 黑板上的数将只有 0 或 2 的幂. 因此当 $A$ 无法继续操作时, 黑板上或者只有 0 , 满足条件 (1); 或者剩下若干个 0 和两两不等的 2 的幂, 满足条件 (2). 此时游戏结束.

记 $a_{n}$ 为第 $n$ 轮后黑板上所有数之和, $b_{n}$ 为此时 0 的个数, $c_{n}=S_{2}\left(a_{n}\right)+b_{n}$,其中用 $S_{2}(m)$ 表示 $m$ 在二进制下的各位数字之和. 在第 $(n+1)$ 轮, 若 $B$选 $x+y$, 则 $a_{n+1}=a_{n}, b_{n+1}=b_{n}$. 故此时 $c_{n+1}=c_{n}$. 而若 $B$ 选 $|x-y|$,则 $a_{n+1}=a_{n}-2^{k}, b_{n+1}=b_{n}+1\left(k \in \mathbb{N}_{+}\right)$. 由 $S_{2}\left(a_{n}\right)=S_{2}\left(a_{n+1}+2^{k}\right) \leq$ $S_{2}\left(a_{n+1}\right)+S_{2}\left(2^{k}\right)=S_{2}\left(a_{n+1}\right)+1$ 知此时 $c_{n+1} \geq c_{n}$. 综上, 不论 $B$ 如何选择, 总有 $\left\{c_{n}\right\}$ 单调不减.

设 $N$ 轮后游戏结束. 此时黑板上的正数只有互不相同的 2 的幂. 因此 $S_{2}\left(a_{N}\right)$ 等于黑板上正数个数. 故黑板上数的个数等于 $b_{N}+S_{2}\left(a_{N}\right)=c_{N} \geq c_{0}=$ $S_{2}(2020)=7$.

下面我们证明, $B$ 有策略使 $A$ 至多获得 7 块曲奇.

$n$ 轮后, 设黑板上的数为 $x_{n 1}, \cdots, x_{n l}$. 记

$$
\mathscr{S}_{n}=\left\{T \subseteq\{1, \cdots, l\}: \sum_{t \in T} x_{n t}=\sum_{t \notin T} x_{n t}\right\}, s_{n}=\left|\mathscr{S}_{n}\right|
$$

下面归纳证明, $B$ 总能保证 $256 \nmid s_{n} . s_{0}=\left(\begin{array}{l}2020 \\ 1010\end{array}\right)$. 由 Kummer 定理, $2^{7} \| s_{0}$.因此 $n=0$ 时成立. 设 $n=k-1$ 时结论成立. 不妨设第 $(k-1)$ 轮 $A$ 在 $x_{k-1,1}, \cdots, x_{k-1, l}$ 中选择了 $x_{k-1, l-1}, x_{k-1, l}$, 且 $x_{k-1, l} \leq x_{k-1, l-1}$. 记

$$
\mathscr{T}=\left\{T \in \mathscr{S}_{k-1}:\{l-1, l\} \subseteq T \text { 或 }\{l-1, l\} \cap T=\varnothing\right\} \text {. }
$$

若 $256 \nmid|\mathscr{T}|$, 则令 $B$ 选择 $x_{k-1, l-1}+x_{k-1, l}$. 黑板上数变为 $x_{k i}=x_{k-1, i}$ $(1 \leq i \leq l-2)$ 和 $x_{k, l-1}=x_{k-1, l-1}+x_{k-1, l}$. 容易验证映射 $\mathscr{T} \rightarrow \mathscr{S}_{k}, T \mapsto T \backslash\{l\}$是双射. 因此有 $s_{k}=|\mathscr{T}|$, 结论成立.
而若 256|| $\mathscr{T} \mid$, 则由 $256 \nmid s_{k-1}$ 知 $256 \nmid\left|\mathscr{S}_{k-1} \backslash \mathscr{T}\right|$. 令 $B$ 选择 $\left|x_{l}-x_{l-1}\right|$.黑板上数变为 $x_{k i}=x_{k-1, i}(1 \leq i \leq l-2)$ 和 $x_{k, l-1}=x_{k-1, l-1}-x_{k-1, l}$. 容易验证映射 $\mathscr{S}_{k-1} \backslash \mathscr{T} \rightarrow \mathscr{S}_{k}, T \mapsto T \backslash\{l\}$ 是双射. 因此有 $s_{k}=\left|\mathscr{S}_{n} \backslash \mathscr{T}\right|$, 结论成立.

综上, 由数学归纳法, $B$ 总能保证 $256 \nmid s_{n}$.

设 $N$ 轮后游戏结束. 此时不可能满足条件 (1) (否则 $s_{N}=0$, 有 $256 \mid s_{N}$ ).因此满足条件 (2), 黑板上只剩余 $m$ 个 0 . 有 $256 \nmid s_{N}=2^{m}$. 故 $m \leq 7$.

综上, 所求为 7 .

注. $A$ 的策略比较明显, $B$ 的策略也可以用使 $\sum_{i=1}^{k} \varepsilon_{i} x_{i}=0$ 等式成立的 $\varepsilon_{i} \in\{-1,1\}$ 组数来表示. 这一想法十分巧妙.

## III. 几何

$\mathbf{G} 1$ 等腰三角形 $A B C$ 满足 $B C=C A$. 点 $D$ 是边 $A B$ 上一点, 且满足 $A D<D B$. 点 $P$ 和 $Q$ 分别在边 $B C$ 和 $C A$ 上, 且满足 $\angle D P B=\angle D Q A=90^{\circ}$.线段 $P Q$ 的垂直平分线和线段 $C Q$ 交于点 $E$,三角形 $A B C$ 和 $C P Q$ 的外接圆交于异于 $C$ 的点 $F$. 若点 $P, E, F$ 共线, 证明: $\angle A C B=90^{\circ}$.



解法 1. 由于 $\angle F A Q=\angle F B P, \angle F P B=\angle F Q A$, 知 $\triangle F A Q \sim \triangle F B P$,由此得到 $\triangle F P Q \sim \triangle F B A$.

因为 $E$ 在 $P Q$ 中垂线上, $P, E, F$ 共线, 故 $Q P C F$ 是梯形,于是 $\triangle C P Q \cong$ $\triangle F Q P$. 故 $\triangle P C Q \sim \triangle A F B$. 于是

$$
\frac{P C}{C Q}=\frac{A F}{F B}=\frac{A Q}{B P} \Longrightarrow A Q \cdot Q C=B P \cdot P C
$$

又 $A Q+Q C=B P+P C$, 由韦达定理可以得到 $B P, C P$ 是 $A Q, Q C$ 的一个排列. 再由 $A D<D B, \angle A=\angle B$ 推出 $A Q<B P$. 于是 $A Q=C P, B P=C Q$.
在 $P D$ 上取一点 $S$, 使 $P S=D Q$. 由于 $\angle D Q C=\angle S P B=90^{\circ}$, 则有 $\triangle C P S \cong \triangle A Q D, \triangle B P S \cong \triangle C Q D$ 成立. 故有 $\angle C S B=\angle A D C=180^{\circ}-$ $\angle B D C$.

又 $D S \perp B C$, 由同一法不难证明, $S$ 为 $\triangle B C D$ 的垂心. 得 $C S \perp A B$, 是 $A B$ 的中垂线.

由于 $C P=P S$, 所以 $\angle P C S=45^{\circ}, \angle A B C=90^{\circ}$.



解法 2. 取 $A B$ 中点 $M$, 得 $\angle D M C=90^{\circ}$. 因此 $D, M, P, C, Q$ 共圆. 因为 $E$ 在 $P Q$ 中垂线上, 且 $P, E, F$ 共线. 故 $Q P C F$ 是等腰梯形. 又由 $\angle P C M=$ $\angle Q C M$ 得 $M$ 是弧 $P D Q$ 的中点. 因此 $M$ 是弧 $F D C$ 的中点. 于是 $M$ 在 $C F$ 中垂线上. 又因为 $M$ 也在 $A B$ 中垂线上, 且 $A B, C F$ 不平行. 故 $M$ 为 $A, B, C, F$ 所共圆圆心, 即 $\triangle A B C$ 外心. 故 $\angle A C B=90^{\circ}$.



注. 观察到本题的逆命题是平凡的, 可以复刻逆命题的证明以解决本题,解法 1 即是如此. 解法 2 注意到了 $F, C, P, Q, M$ 五点的对称性, 更为简洁.

$\mathbf{G} 2$ 设凸四边形 $A B C D$ 内部的一点 $P$ 满足

$$
\angle P A D: \angle P B A: \angle D P A=1: 2: 3=\angle C B P: \angle B A P: \angle B P C .
$$

$\angle A D P$ 和 $\angle P C B$ 的内角平分线交于三角形 $A B P$ 内的一点 $Q$. 证明: $A Q=$ $B Q$.



解法 1. 记 $\angle P A D=\alpha$. 由于 $\angle D P A>\angle D A P$, 可在 $A D$ 边上取一点 $E$,使得 $\angle A P E=\angle P A D$. 则有

$$
\angle D E P=\angle D P E=2 \alpha=\angle A B P .
$$

故 $D E=D P$, 且 $A, B, P, E$ 共圆. 故 $\angle A D P$ 的平分线是 $P E$ 的中垂线, 从而过 $\triangle A B P$ 外心. 同理, $\angle P C B$ 的平分线过 $\triangle A B P$ 外心. 因此 $Q$ 为 $\triangle A B P$ 外心. 故 $A Q=B Q$.



解法 2. 取 $\triangle A B P$ 的外心 $O$. 则

$$
\angle A O P=2 \angle A B P=\angle D A P+\angle D P A=180^{\circ}-\angle P D A \text {. }
$$

这推出了 $A, O, D, P$ 共圆. 又 $A O=P O$, 知 $D O$ 为 $\angle A D P$ 的角平分线. 同理, $C O$ 为 $\angle B C P$ 的角平分线. 因此 $Q=O$.


解法 3. 由于 $\angle C P B>\angle C B P$, 可延长 $C P$ 至 $N$ 使 $C N=B C$. 则

$$
\angle P N B=90^{\circ}-\frac{1}{2} \angle P C B=\angle P A B .
$$

于是 $P, M, A, B$ 共圆. 因此 $\angle B C P$ 的平分线为 $B N$ 中垂线过 $\triangle A B P$ 外心. 同理, $\angle B C P$ 的内角平分线过 $\triangle A B P$ 外心. 因此 $Q$ 为 $\triangle A B P$ 外心.



解法 4. 设 $A B$ 中点为 $M . \angle A D P$ 的角平分线和 $\angle B C P$ 的角平分线分别交直线 $A B$ 于 $E, F$, 交 $A B$ 中垂线于 $Q_{1}, Q_{2}$. 记 $A B=a, \angle P A D=\alpha$, $\angle C B P=\beta$. 则

$$
\begin{gathered}
A P=A B \cdot \frac{\sin \angle B A P}{\sin \angle A P B}=\frac{a \sin 2 \alpha}{\sin (2 \alpha+2 \beta)} \\
A D=A P \cdot \frac{\sin \angle A P D}{\sin \angle A D P}=\frac{a \sin 3 \alpha}{2 \cos 2 \alpha \sin (2 \alpha+2 \beta)}
\end{gathered}
$$

$A E=A D \cdot \frac{\sin \angle A D E}{\sin \angle A E D}=A D \cdot \frac{\sin \angle A D E}{\sin (\angle A D E+\angle D A E)}=\frac{a \sin 3 \alpha}{2 \cos (2 \beta-\alpha) \sin (2 \alpha+2 \beta)}$.

对于 $\alpha+\beta \geq 45^{\circ}$ 的情形,

$$
\begin{gathered}
M E=A E-A M=\frac{a \sin 3 \alpha}{\sin 3 \alpha+\sin (\alpha+4 \beta)}-\frac{a}{2}=\frac{a \cdot 2 \sin (\alpha-2 \beta) \cos (2 \alpha+2 \beta)}{2 \cos (2 \beta-\alpha) \sin (2 \alpha+2 \beta)} . \\
M Q_{1}=M E \cdot \cot (2 \beta-\alpha)=-\frac{a}{2} \cot (2 \alpha+2 \beta) .
\end{gathered}
$$

同理 $M Q_{2}=-\frac{a}{2} \cot (2 \alpha+2 \beta)$. 这推出 $M Q_{1}=M Q_{2}$. 而 $\alpha+\beta \leq 45^{\circ}$ 的证明是类似的, 留给读者作为练习. 故 $Q_{1}=Q_{2}=Q$.


注. 本题是 2020 年 IMO 第 1 题. 如何处理 $1,2,3$ 倍角是常用的知识, 笔者给出了三种处理方法.

G3 凸四边形 $A B C D$ 满足 $\angle A B C>90^{\circ}, \angle C D A>90^{\circ}$, 且 $\angle D A B=$ $\angle B C D$. 记 $E$ 和 $F$ 分别是点 $A$ 关于直线 $B C$ 和 $C D$ 的对称点. 设线段 $A E$ 和 $A F$ 分别交直线 $B D$ 于点 $K$ 和 $L$. 证明: 三角形 $B E K$ 外接圆和三角形 $D F L$外接圆相切。



解法 1. 记 $\triangle D F L, \triangle B E K$ 外接圆分别为 $\omega_{1}, \omega_{2}$. 在 $\omega_{1}$ 上取点 $T$ 使 $D$ 为弧 $T D F$ 中点. 有 $D T=D F=D A, \angle T L D=\angle T F D=\angle D T F=\angle A L D$. 又

$$
\angle D A L+\angle D T L<\angle D A L+\angle D T F=\angle D A L+\angle D L A<180^{\circ}
$$

因此 $\triangle D T L \cong \triangle D A L$. 因此 $T$ 为 $A$ 关于 $B D$ 的对称点. 同理, $T$ 在 $\omega_{2}$ 上, 且 $B$ 为弧 $T B E$ 中点.


过 $T$ 分别作 $\omega_{1}, \omega_{2}$ 切线 $T X, T Y$, 使得 $T X, T Y$ 的延长线与直线 $B D$ 相交.

$$
\begin{aligned}
\angle X T B+\angle Y T D & =\angle T K B+\angle T L D=180^{\circ}-\angle K T L=180^{\circ}-\angle K A L \\
& =\left(90^{\circ}-\angle E A C\right)+\left(90^{\circ}-\angle F A C\right) \\
& =\angle B C A+\angle D C A=\angle B C D=\angle B A D=\angle B T D .
\end{aligned}
$$

所以 $T X, T Y$ 是重合的, 结论成立.

注. 除了将 $A$ 点关于 $B D$ 对称得到切点 $T$, 也可以将两个外接圆关于 $B D$对称, 去证明对称后的两圆切于 $A$. 即证明 $\odot B A K$ 与 $\odot D A L$ 相切. 导角过程是类似的.

解法 2. 本解答中, 复平面上的点与其所对应复数用同一字母表示, 单位圆指圆 $|Z|=1$. 我们先不加证明地给出三个引理. 它们的证明分别可以参考陈锐韧等《2019 IMO 预选题及其解答》 G6 解 5 引理 3 和引理 1, 以及 G3 解 3 引理 2.

引理 1. $X Y$ 是复平面单位圆的弦, $Z$ 是复平面上的点. 则 $Z$ 关于 $X Y$ 的对称点为 $X+Y-X Y \bar{Z}$.

引理 2. $X Y$ 是复平面单位圆的弦. 则直线上的点 $Z$ 满足 $Z+X Y \bar{Z}=$ $X+Y$.

引理 3. 复平面上不共线的四点 $W, X, Y, Z$ 共圆当且仅当 $\frac{(W-Y)(X-Z)}{(W-X)(Y-Z)} \in \mathbb{R}$.

原问题的证明. 记 $A$ 关于 $B D$ 的对称点为 $T$. 以 $\triangle B C D$ 的外接圆圆心为原点, 半径为单位长建立复平面. 由 $\angle B T D=\angle B A D=\angle B C D$, 有 $T$ 在单位圆上. $|B|=|C|=|D|=|T|=1$. 故

$$
\bar{B}=\frac{1}{B}, \bar{C}=\frac{1}{C}, \bar{D}=\frac{1}{D}, \bar{T}=\frac{1}{D} .
$$

由引理 1 及 $(*), A=B+D-\frac{B D}{T}$, 进而

$$
E=B+C-B C \bar{A}=B+\frac{C T}{D}-\frac{B C}{D}, F=D+\frac{C T}{B}-\frac{C D}{B} .
$$

由 $E K \perp B C$, 有 $\frac{E-K}{B-C}$ 是纯虚数. 由 $K, B, D$ 共线, 有 $\frac{B-K}{B-D} \in \mathbb{R}$. 因此由引理 3 及 $(*),(* *)$,

$Z$ 在 $\triangle B E K$ 的外接圆上

$$
\begin{aligned}
& \Longleftrightarrow \frac{(Z-E)(B-K)}{(Z-B)(E-K)} \in \mathbb{R} \Longleftrightarrow \frac{(Z-E)(B-D)}{(Z-B)(B-C)} \text { 是纯虚数 } \\
& \Longleftrightarrow \frac{(Z-E)(B-D)}{(Z-B)(B-C)}+\overline{\left(\frac{(Z-E)(B-D)}{(Z-B)(B-C)}\right)}=0
\end{aligned}
$$

$$
\begin{aligned}
& \Longleftrightarrow \frac{(D Z-B D-C T+B C)(B-D)}{D(Z-B)(B-C)}+\frac{(B C T \bar{Z}-C T-B D+D T)(D-B)}{D T(B \bar{Z}-1)(C-B)}=0 \\
& \Longleftrightarrow B T(C+D) Z \bar{Z}-(B D+C T) Z-B T(B D+C T) \bar{Z}+\left(B^{2} D+C T^{2}\right)=0 \\
& \Longleftrightarrow \bar{Z}=\frac{(B D+C T) Z-\left(B^{2} D+C T^{2}\right)}{B T((C+D) Z-(B D+C T))} .
\end{aligned}
$$

同理,

$Z$ 在 $\triangle D F L$ 的外接圆上 $\Longleftrightarrow \bar{Z}=\frac{(B D+C T) Z-\left(B D^{2}+C T^{2}\right)}{D T((B+C) Z-(B D+C T))}$

联立两圆方程,

$$
\begin{aligned}
& \frac{(B D+C T) Z-\left(B^{2} D+C T^{2}\right)}{B T((C+D) Z-(B D+C T))}=\frac{(B D+C T) Z-\left(B D^{2}+C T^{2}\right)}{D T((B+C) Z-(B D+C T))} \\
& \quad \Longleftrightarrow C(D-B)(B D+C T)(Z-T)^{2}=0 .
\end{aligned}
$$

因此两圆相切于 $T$.

注. 此题中的二圆切点颇为明显, 看出后导角即可.

G4 在平面中有 $n \geq 6$ 个两两不交的圆盘 $D_{1}, D_{2}, \cdots, D_{n}$, 它们的半径分别为 $R_{1} \geq R_{2} \geq \cdots \geq R_{n}$. 对每个 $i=1,2, \cdots, n, P_{i}$ 是圆盘 $D_{i}$ 内任取的一点.令 $O$ 是平面内任意一点, 证明:

$$
O P_{1}+O P_{2}+\ldots+O P_{n} \geq R_{6}+R_{7}+\ldots+R_{n}
$$

(这里圆盘含其边界.)

解. 记 $D_{i}$ 的圆心为 $O_{i}$. 先证明一个结论.

结论. 对于每个 $i$, 至多存在 5 个不同的 $j \leq i$, 使

$$
\left|O O_{j}\right|<R_{j}+R_{i}
$$

结论的证明. 对任意两两不同的 $j_{1}, \cdots, j_{6} \leq i$, 不妨设射线 $O O_{j_{1}}, \cdots, O O_{j_{6}}$按顺时针排布. 由于

$$
\sum_{i=1}^{6} \angle O_{j_{i+1}} O O_{j_{i}}=360^{\circ}
$$

这里令 $O_{j_{7}}=O_{j_{1}}$, 不妨设 $\angle O_{j_{2}} O O_{j_{1}} \leq 60^{\circ}$. 则

$$
\max \left\{\left|O_{j_{2}} O\right|,\left|O_{j_{1}} O\right|\right\} \geq\left|O_{j_{1}} O_{j_{2}}\right| \geq R_{j_{1}}+R_{j_{2}} \geq \max \left\{R_{j_{1}}+R_{i}, R_{j_{2}}+R_{i}\right\}
$$

因此 $j_{1}, j_{2}$ 至少一个不满足 $(*)$ 式. 故结论成立.

原命题的证明. 记 $S_{i}=\left\{j: 1 \leq j \leq i,\left|O O_{j}\right| \geq R_{j}+R_{i}\right\}$. 由结论, $\left|S_{i}\right| \geq i-$ 5. 因此我们可依次从 $S_{6}, \cdots, S_{n}$ 中取出两两互异的元素 $j_{6} \in S_{6}, \cdots, j_{n} \in S_{n}$.
于是对 $6 \leq k \leq n$,

$$
\left|O P_{j_{k}}\right| \geq\left|O O_{j_{k}}\right|-R_{j_{k}} \geq R_{k}
$$

相加即得证.

注. 难度不小的组合几何问题. 虽然借助解决此类题的经验容易看到前面结论指出的这一关键点, 但此后如果没有想 $j_{6}, \cdots, j_{n}$ 的取法, 证明仍然是困难的.

$\mathbf{G} 5$ 设圆内接四边形 $A B C D$ 对边两两不平行. $K, L, M, N$ 分别在 $A B$, $B C, C D, D A$ 上, 使得四边形 $K L M N$ 为菱形, 且 $K L\|A C, L M\| B D$. $\omega_{1}, \omega_{2}, \omega_{3}, \omega_{4}$ 分别是 $\triangle A N K, \triangle B K L, \triangle C L M, \triangle D M N$ 的内切圆. 证明: $\omega_{1}$ 与 $\omega_{3}$ 的内公切线和 $\omega_{2}$ 与 $\omega_{4}$ 的内公切线共点.



解法 1. 记 $\omega_{1}, \omega_{2}, \omega_{3}, \omega_{4}$ 的圆心分别为 $I_{1}, I_{2}, I_{3}, I_{4}$. 设直线 $I_{1} I_{3}$, 直线 $I_{2} I_{4}$交于 $X$, 直线 $A D$, 直线 $B C$ 交于 $E$, 直线 $A B$, 直线 $C D$ 交于 $F$. 设 $\omega_{1}$ 切 $A D$于 $S, \omega_{3}$ 切 $C D$ 于 $T$.

由于 $K L\|A C, M L\| B D$,

$$
\frac{B L}{B C} \cdot A C=K L=L M=\frac{C L}{B C} \cdot B D \Longrightarrow \frac{C L}{B L}=\frac{C A}{B D}
$$

又由正弦定理,

$$
\frac{B F}{B D}=\frac{\sin \angle B D F}{\sin \angle B F D}=\frac{\sin \angle C A F}{\sin \angle C F A}=\frac{C F}{C A} \Longrightarrow \frac{C F}{B F}=\frac{C A}{B D}
$$

因此 $\frac{C F}{B F}=\frac{C L}{B L}$. 故 $F L$ 平分 $\angle B F C$. 因此 $B I_{2}, C I_{3}, F L$ 共 $\triangle B F C$ 的 $F$ 所对的旁心, 记为 $J$.

我们有

$$
\angle C L I_{3}=\frac{1}{2} \angle C L M=\frac{1}{2} \angle C B D=\frac{1}{2} \angle C A D \text {, }
$$

同理 $\angle I_{2} L B=\frac{1}{2} \angle A D B$. 故

$$
\begin{aligned}
\angle I_{3} L J & =\angle B L F-\angle C L I_{3} \\
& =\left(180^{\circ}-\angle L B F-\angle L F B\right)-\frac{1}{2} \angle C A D \\
& =\left(180^{\circ}-\angle C D A-\frac{1}{2} \angle A F D\right)-\frac{1}{2} \angle C A D \\
& =\left(180^{\circ}-\angle C D A-\frac{1}{2}\left(180^{\circ}-\angle B A D-\angle A D C\right)\right)-\frac{1}{2} \angle C A D \\
& =\frac{1}{2}\left(180^{\circ}-\angle A D C+\angle B A D-\angle C A D\right) \\
& =\frac{1}{2}(\angle A B C+\angle C A B)=\frac{1}{2}\left(180^{\circ}-\angle A C B\right)=90^{\circ}-\frac{1}{2} \angle A D B,
\end{aligned}
$$

同理 $\angle J L I_{2}=90^{\circ}-\frac{1}{2} \angle C A D$.

因此对 $\triangle B C J$ 由 Menelaus 定理,

$$
\begin{aligned}
& E, I_{2}, I_{3} \text { 共线 } \Longleftrightarrow \frac{B E}{E C} \cdot \frac{C I_{3}}{I_{3} J} \cdot \frac{J I_{2}}{I_{2} B}=1 \\
& \Longleftrightarrow \frac{B E}{E C} \cdot \frac{C L \frac{\sin \angle C L I_{3}}{\sin \angle C I_{3} L}}{L J \frac{\sin \angle I_{3} J J}{\sin \angle L I_{3} J}} \cdot \frac{J \frac{\sin \angle J L I_{2}}{\sin \angle J I_{2} L}}{L B \frac{\sin \angle I_{2} L B}{\sin \angle L I_{2} B}}=1 \\
& \Longleftrightarrow \frac{B E}{E C} \cdot \frac{C L}{L B} \cdot \frac{\sin \angle C L I_{3}}{\sin \angle I_{3} L J} \cdot \frac{\sin \angle J L I_{2}}{\sin \angle I_{2} L B}=1 \\
& \Longleftrightarrow \frac{B E}{E C} \cdot \frac{C F}{F B} \cdot \frac{\sin \angle C A D}{\sin \angle A D B}=1 \\
& \Longleftrightarrow \frac{B E}{E C} \cdot \frac{C F}{F B} \cdot \frac{C D}{A B}=1
\end{aligned}
$$

在 $\triangle B C F$ 中由 Ceva 定理, 有

$$
\frac{B E}{E C} \cdot \frac{C D}{D F} \cdot \frac{F A}{A B}=1 .
$$

而由 $\triangle B F C \sim \triangle D F A$,

$$
\frac{D F}{F A}=\frac{C F}{F B}
$$

两式相乘, 即得

$$
\frac{B E}{E C} \cdot \frac{C F}{F B} \cdot \frac{C D}{A B}=1 .
$$

因此 $E, I_{2}, I_{3}$ 共线. 同理 $E, I_{1}, I_{4}$ 共线, $F, I_{2}, I_{1}$ 共线, $F, I_{3}, I_{4}$ 共线.
设 $I_{4} B$ 与 $E F$ 交于 $U$, 因此

$$
\begin{gathered}
\frac{X I_{1}}{X I_{3}}=\frac{S_{\triangle I_{2} I_{1} I_{4}}}{S_{\triangle I_{2} I_{3} I_{4}}}=\frac{S_{\triangle I_{2} E I_{4}} \frac{I_{4} I_{1}}{I_{4} E}}{S_{\triangle I_{2} F I_{4}} \frac{I_{4} I_{3}}{I_{4} F}}=\frac{E U}{U F} \cdot \frac{I_{4} I_{1}}{I_{4} I_{3}} \cdot \frac{I_{4} F}{I_{4} E} \\
\frac{I_{1} S}{I_{3} T}=\frac{I_{1} E \sin \angle D E I_{4}}{I_{3} F \sin \angle D F I_{4}}=\frac{I_{1} E}{I_{3} F} \cdot \frac{I_{4} F}{I_{4} E} .
\end{gathered}
$$

而在 $\triangle E F I_{4}$ 中, 由 Ceva 定理知,

$$
\frac{E U}{U F} \cdot \frac{F I_{3}}{I_{3} I_{4}} \cdot \frac{I_{4} I_{1}}{I_{1} E}=1
$$

因此 $\frac{X I_{1}}{X I_{3}}=\frac{I_{1} S}{I_{3} T}$.

故 $\omega_{1}$ 与 $\omega_{3}$ 的两条内公切线过 $X$. 同理, $\omega_{2}$ 与 $\omega_{4}$ 的两条内公切线过 $X$. $\square$



解法 2. 以 $r_{\triangle X Y Z}$ 记 $\triangle X Y Z$ 的内切圆半径. 我们先证明一个引理.

引理. 在圆内接四边形 $A B C D$ 中, $I_{A}$ 为 $\triangle A B D$ 的内心, $I_{C}$ 为 $\triangle B C D$ 的内心, $I_{A} I_{C}, B D$ 交于 $X$. 则

$$
\frac{B X}{X D}=\frac{r_{\triangle A B C}}{r_{\triangle A C D}}
$$

引理的证明. 设 $I_{B}, I_{D}$ 分别为 $\triangle A B C, \triangle A C D$ 的内心. 由正弦定理,

$$
\begin{aligned}
\frac{B X}{X D} & =\frac{B I_{C} \frac{\sin \angle I_{B} B I_{C}}{\sin \angle B X I_{C}}}{D I_{A} \frac{\sin \angle D I_{A} X}{\sin \angle D X I_{A}}}=\frac{B I_{C} \sin \angle B I_{C} X}{D I_{A} \sin \angle D I_{A} X}=\frac{B I_{C} \frac{B I_{A}}{I_{A} I_{C}} \sin \angle B I_{C} X}{D I_{A} \frac{D I_{C}}{I_{A} I_{C}} \sin \angle I_{A} D I_{C}} \\
& =\frac{B I_{A}}{D I_{A}} \cdot \frac{B I_{C}}{D I_{C}} \cdot \frac{\sin \angle I_{A} B I_{C}}{\sin \angle I_{A} D I_{C}}=\frac{\sin \frac{1}{2} \angle A D B}{\sin \frac{1}{2} \angle A B D} \cdot \frac{\sin \frac{1}{2} \angle B D C}{\sin \frac{1}{2} \angle D B C} \cdot \frac{\sin \frac{1}{2} \angle A B C}{\sin \frac{1}{2} \angle A D C} .
\end{aligned}
$$

因此由正弦定理,

$$
\begin{aligned}
\frac{r_{\triangle A B C}}{r_{\triangle A C D}} & =\frac{I_{B} C \sin \frac{1}{2} \angle A C B}{I_{D} C \sin \frac{1}{2} \angle A C D}=\frac{A C \frac{\sin \angle I_{B} A C}{\sin \angle A I_{B} C} \sin \frac{1}{2} \angle A C B}{A C \frac{\sin \angle I_{D} A C}{\sin \angle A I_{D} C} \sin \frac{1}{2} \angle A C D} \\
& =\frac{\sin \frac{1}{2} \angle A C B}{\sin \frac{1}{2} \angle A C D} \cdot \frac{\sin \frac{1}{2} \angle B A C}{\sin \frac{1}{2} \angle D A C} \cdot \frac{\sin \frac{1}{2} \angle A B C}{\sin \frac{1}{2} \angle A D C}=\frac{B X}{X D}
\end{aligned}
$$

引理证毕.



原问题的证明. 设 $\omega_{1}, \omega_{3}$ 的内心分别为 $I_{1}, I_{3}$, 两圆的内公切线交于 $X$.过 $X$ 作 $N M$ 的平行线, 分别交 $N K, M L$ 于 $X_{1}, X_{3}$; 作 $N K$ 平行线, 分别交 $N M, K L$ 于 $X_{4}, X_{2}$.

$X$ 是 $\omega_{1}, \omega_{3}$ 的内位似中心. 由 $N K \| M L$, 有 $X_{1}, X_{3}$ 为该位似关系的对应点. 因此, $I_{1} X_{1} \| X_{3} I_{3}$, 且

$$
\frac{X_{1} X}{X X_{3}}=\frac{R\left(\omega_{1}\right)}{R\left(\omega_{3}\right)}
$$

平移 $\triangle C M L$, 使 $M, L$ 分别与 $N, K$ 重合, 设 $C, I_{3}$ 分别平移至了 $C^{\prime}, I_{3}^{\prime}$. 显然 $C^{\prime}$ 在 $A C$ 上. $\overrightarrow{I_{3} I_{3}^{\prime}}=\overrightarrow{L K}=\overrightarrow{X_{3} X_{1}}$. 因此四边形 $X_{1} I_{3}^{\prime} I_{3} X_{3}$ 为平行四边形. 因此 $X_{1} I_{3}^{\prime} \| X_{3} I_{3}$. 结合 $I_{1} X_{1} \| X_{3} I_{3}$ 有 $I_{1}, X_{1}, I_{3}^{\prime}$ 共线.

由 $\angle N C^{\prime} K=\angle M C L=180^{\circ}-\angle D A B$, 有 $A, N, C^{\prime}, K$ 共圆. 而 $I_{1}, I_{3}$ 分别为 $\triangle A N K, \triangle C^{\prime} N K$ 的内心. 因此由引理, 及 $\triangle D M N \sim \triangle N C^{\prime} A, \triangle B L K \sim$ $\triangle K C^{\prime} A$,

$$
\frac{X_{4} X}{X X_{2}}=\frac{N X_{1}}{X_{1} K}=\frac{r_{\triangle A N C^{\prime}}}{r_{\triangle A K C^{\prime}}}=\frac{\frac{N A}{D N} R\left(\omega_{4}\right)}{\frac{K A}{B K} R\left(\omega_{2}\right)}=\frac{R\left(\omega_{4}\right)}{R\left(\omega_{2}\right)}
$$

结合 $(*)$, 同理有 $\omega_{2}, \omega_{4}$ 的两条内公切线也交于 $X$.



解法 3. 我们先证明一个引理.

引理. $\triangle A B C$ 的内心为 $I . O$ 为平面上一点. 记 $B C=a, C A=b, A B=c$.则

$$
\overrightarrow{O I}=\frac{a \overrightarrow{O A}+b \overrightarrow{O B}+c \overrightarrow{O C}}{a+b+c}
$$

引理的证明. 设 $A D$ 为 $\triangle A B C$ 边 $B C$ 上角分线. 由向量的定比分点定理,

$$
\overrightarrow{O I}=\frac{I D}{A D} \overrightarrow{O A}+\frac{I A}{A D} \overrightarrow{O D}=\frac{I D}{A D} \overrightarrow{O A}+\frac{I A}{A D}\left(\frac{C D}{B C} \overrightarrow{O B}+\frac{B D}{B C} \overrightarrow{O C}\right)
$$

而由角分线定理，

$$
B D=\frac{a c}{b+c}, D C=\frac{a b}{b+c}, \frac{I D}{A D}=\frac{B D}{B D+c}=\frac{a}{a+b+c}, \frac{I A}{A D}=\frac{b+c}{a+b+c}
$$

代人即得欲证式. 引理证毕.

原结论的证明. 记 $A B=a, B C=b, C D=c, D A=d, A C=x, B D=y$.记 $\omega_{1}, \omega_{3}$ 的圆心分别为 $I_{1}, I_{3}$, 两圆内公切线的交点 $X$. 设 $A C, B D$ 交于 $E . O$为平面上任意一点.
在 $\triangle A B D$ 和 $\triangle B C D$ 中由余弦定理,

$$
y^{2}=a^{2}+d^{2}-2 a d \cos \angle D A B=b^{2}+c^{2}-2 b c \cos \angle B C D \text {. }
$$

因此

$$
\begin{aligned}
y^{2} & =\frac{b c}{b c+a d}\left(a^{2}+d^{2}-2 a d \cos \angle D A B\right)+\frac{a d}{b c+a d}\left(b^{2}+c^{2}+2 b c \cos \angle B A D\right) \\
& =\frac{(a b+c d)(a c+b d)}{b c+a d} .
\end{aligned}
$$

同理,

$$
x^{2}=\frac{(a d+b c)(a c+b d)}{a b+c d}
$$

故

$$
y(b c+a d)=x(a b+c d):=s
$$

与解法 2 的引理中计算 $\frac{B X}{X D}$ 的部分同理,

$$
\frac{A E}{E C}=\frac{A B \cdot A D \cdot \sin \angle B A D}{C B \cdot C D \cdot \sin \angle B C D}=\frac{a d}{b c} .
$$

因此

$$
\overrightarrow{O E}=\frac{b c}{a d+b c} \overrightarrow{O A}+\frac{a d}{a d+b c} \overrightarrow{O C}
$$

由 $N K\|D B\| M L, N M\|A C\| K L$,

$$
\frac{A N}{N D}=\frac{C M}{M D}=\frac{C L}{L B}=\frac{A K}{K B}
$$

设上比例为 $\lambda$. 有

$$
\frac{\lambda y}{1+\lambda}=\frac{A N}{A D} \cdot B D=N K=M N=\frac{D N}{D A} \cdot A C=\frac{x}{1+\lambda}
$$

解得 $\lambda=\frac{x}{y}$. 因此

$$
\begin{aligned}
& \overrightarrow{O N}=\frac{1}{1+\lambda} \overrightarrow{O A}+\frac{\lambda}{1+\lambda} \overrightarrow{O D}=\frac{y}{x+y} \overrightarrow{O A}+\frac{x}{x+y} \overrightarrow{O D} \\
& \overrightarrow{O K}=\frac{1}{1+\lambda} \overrightarrow{O A}+\frac{\lambda}{1+\lambda} \overrightarrow{O B}=\frac{y}{x+y} \overrightarrow{O A}+\frac{x}{x+y} \overrightarrow{O B}
\end{aligned}
$$

由引理和 $\triangle A B D \sim \triangle A K N$,

$$
\begin{aligned}
\overrightarrow{O I_{1}} & =\frac{A N \cdot \overrightarrow{O K}+N K \cdot \overrightarrow{O A}+K A \cdot \overrightarrow{O N}}{A N+N K+K A}=\frac{d \overrightarrow{O K}+y \overrightarrow{O A}+a \overrightarrow{O N}}{d+y+a} \\
& =\frac{d\left(\frac{y}{x+y} \overrightarrow{O A}+\frac{x}{x+y} \overrightarrow{O B}\right)+y \overrightarrow{O A}+a\left(\frac{y}{x+y} \overrightarrow{O A}+\frac{x}{x+y} \overrightarrow{O D}\right)}{d+y+a} \\
& =\frac{(a+d+x+y) y \overrightarrow{O A}+d x \overrightarrow{O B}+a x \overrightarrow{O D}}{(x+y)(a+d+y)} .
\end{aligned}
$$

同理,

$$
\overrightarrow{O I_{3}}=\frac{(b+c+x+y) y \overrightarrow{O C}+c x \overrightarrow{O B}+b x \overrightarrow{O D}}{(x+y)(b+c+y)}
$$

由于 $X$ 是 $\omega_{1}, \omega_{3}$ 的位似中心, 因此

$$
\begin{aligned}
\frac{I_{1} X}{X I_{3}} & =\frac{R\left(\omega_{1}\right)}{R\left(\omega_{3}\right)}=\frac{\frac{A N}{A D} r_{\triangle A B D}}{\frac{C M}{C D} r_{\triangle B C D}}=\frac{r_{\triangle A B D}}{r_{\triangle B C D}}=\frac{S_{\triangle A B D} /(a+d+y)}{S_{\triangle B C D} /(b+c+y)} \\
& =\frac{a d \sin \angle D A B /(a+d+y)}{b c \sin \angle D C B /(b+c+y)}=\frac{a d(b+c+y)}{b c(a+d+y)}
\end{aligned}
$$

故结合 $(*)$ 和 $(* *)$, 有

$$
\begin{aligned}
\overrightarrow{O X} & =\frac{X I_{3}}{I_{1} X+X I_{3}} \overrightarrow{O I_{1}}+\frac{I_{1} X}{I_{1} X+X I_{3}} \overrightarrow{O I_{3}} \\
& =\frac{b c y(a+d+x+y) \overrightarrow{O A}+c d x(a+b) \overrightarrow{O B}+a d y(b+c+x+y) \overrightarrow{O C}+a b x(c+d) \overrightarrow{O D}}{(x+y)(a b c+b c d+c d a+d a b+y(a d+b c))} \\
& =\frac{b c y(a+d) \overrightarrow{O A}+c d x(a+b) \overrightarrow{O B}+a d y(b+c) \overrightarrow{O C}+a b x(c+d) \overrightarrow{O D}+s(x+y) \overrightarrow{O E}}{(x+y)(a b c+b c d+c d a+d a b+s)}
\end{aligned}
$$

同理, $O$ 到 $\omega_{2}, \omega_{4}$ 的内公切线交点的向量亦为上式.

注 1. 解法 2 事实上证明了一个更强的结论：四边形 $K L M N$ 是平行四边形而不一定是菱形时, 题目结论仍然成立.

注 2. 待证结论有点无从下手. 解法 1 借用了内外似中心的一点考虑, 发现了一个完全四边形; 解法 2 则简单粗暴, 用同一法和计算比例证明两组内公切线的两个交点重合; 解法 3 是向量法, 多个平行的条件让向量计算可行, 但熟悉圆内接四边形的 $(*)$ 与 $(* *)$ 二式也尤为关键.

G6 设锐角三角形 $A B C$ 满足 $A B<A C$, 其内心与 $A$-旁心分别为 $I$ 和 $I_{A}$. 设其内切圆切 $B C$ 于点 $D$. 直线 $A D$ 分别交直线 $B I_{A}$ 和直线 $C I_{A}$ 于点 $E$和 $F$. 证明: $\triangle A I D$ 的外接圆和 $\triangle I_{A} E F$ 的外接圆相切.


解. 作 $T$ 为完全四边形 $B C D E F I_{A}$ 的 Miquel 点. 有 $B, D, E, T$ 共圆, $B, I, C, I_{A}, T$ 共圆, $E, I_{A}, F, T$ 分别共圆. 因此

$$
\angle A D T=180^{\circ}-\angle T D E=180^{\circ}-\angle T B E=180^{\circ}-\angle T I I_{A}=\angle A I T \text {. }
$$

故 $A, I, D, T$ 共圆.

设 $\triangle I D T$ 外接圆与 $C B$ 的延长线交于 $P . \angle I T P=\angle I D P=90^{\circ}$ 和 $\angle I T I_{A}=\angle I B I_{A}=90^{\circ}$. 故 $P, T, I_{A}$ 共线.

过 $T$ 分别作 $\triangle A I D$ 外接圆和 $\triangle E I_{A} F$ 外接圆的切线 $T X, T Y$.

$$
\angle D T X+\angle Y T E=\angle D P T+\angle E I_{A} T=\angle D B E=\angle D T E .
$$

故 $T X, T Y$ 重合.



注. 本题关键在于切点为完全四边形 $B C D E F I_{A}$ 的 Miquel 点.

$\mathbf{G} 7$ 设点 $P$ 是锐角三角形 $A B C$ 外接圆上一点. $D, E, F$ 分别是 $P$ 关于 $\triangle A B C$ 平行于 $B C, C A, A B$ 的中位线的对称点. 记 $\triangle A D P, \triangle B E P, \triangle C F P$ 的外接圆分别为 $\omega_{A}, \omega_{B}, \omega_{C}$. 记 $A D, B E, C F$ 的垂直平分线围成的三角形的外接
圆为 $\omega$. 证明: $\omega_{A}, \omega_{B}, \omega_{C}, \omega$ 共点.



解. 记 $A D, B E, C F$ 的中垂线分别为 $l_{1}, l_{2}, l_{3}$. 设 $l_{2}, l_{3}$ 交于 $X, l_{3}, l_{1}$ 交于 $Y, l_{1}, l_{2}$ 交于 $Z ; \triangle A B C$ 边 $B C, C A, A B$ 中点分别为 $L, M, N$, 三条高为 $A R, B S, C T$, 垂心为 $H$. 有 $A, R ; B, S ; C, T$ 分别关于 $M N, N L, L M$ 对称. 设 $\omega_{A}, \omega_{B}, \omega_{C}$ 的圆心分别为 $U, V, W$. 由 $U, V, W$ 分别在 $A D, B E, C F$ 的中垂线上,有 $U, V, W$ 分别在 $l_{1}, l_{2}, l_{3}$ 上.

记 $K$ 为直线 $P H$ 与 $\triangle A B C$ 九点圆 $\gamma$ 的交点. 由于垂心 $H$ 是 $\triangle A B C$ 外接圆与九点圆的外位似中心, 结合圆幂定理有

$$
A H \cdot H R=2 P(H, \gamma)=K H \cdot H P
$$

其中 $P(H, \gamma)$ 表示 $H$ 关于 $\gamma$ 的幂. 因此 $A, K, R, P$ 共圆. 又由 $A R P D$ 为等腰梯形, 有 $A, K, R, D, P$ 五点共圆 $\omega_{A}$, 且圆心 $U$ 在 $N M$ 上. 同理, $B, K, S, E, P$共圆 $\omega_{B}$, 且圆心 $V$ 在 $N M$ 上; $C, K, T, F, P$ 共圆 $\omega_{C}$, 且圆心 $W$ 在 $M L$ 上. 因此 $\omega_{A}, \omega_{B}, \omega_{C}$ 共点 $K, P$. 因此 $U, V, W$ 共线. 记所共直线 $l$, 有 $K, P$ 关于 $l$ 对称.

以 $\langle\alpha, \beta\rangle$ 记 $\alpha$ 逆时针旋转至与 $\beta$ 平行位置所转过的劣角. 以 $\langle\vec{\alpha}, \vec{\beta}\rangle$ 记 $\vec{\alpha}$逆时针旋转至与 $\vec{\beta}$ 同向所转过的角. 反复运用轴对称关系, 垂直关系与共圆关系, 在 $\bmod 180^{\circ}$ 的意义下, 我们有

$$
\begin{aligned}
\langle K W, K U\rangle & =\langle K W, l\rangle-\langle K U, l\rangle=\frac{1}{2}(\langle\overrightarrow{K W}, \overrightarrow{P W}\rangle-\langle\overrightarrow{K U}, \overrightarrow{P U}\rangle) \\
& =\langle K T, P T\rangle-\langle K R, P R\rangle \\
& =(\langle K T, C T\rangle+\langle C T, P T\rangle)-(\langle K R, A R\rangle+\langle A R, P R\rangle)
\end{aligned}
$$

$$
\begin{aligned}
& =(\langle K P, C P\rangle-\langle T C, F C\rangle)-(\langle K P, A P\rangle-\langle R A, D A\rangle) \\
& =\langle A P, C P\rangle+\langle R A, T C\rangle+\langle F C, D A\rangle \\
& =\langle A B, C B\rangle+\langle H A, H C\rangle+\langle Y W, Y U\rangle=\langle Y W, Y U\rangle .
\end{aligned}
$$

因此 $K, Y, W, U$ 共圆. 同理, $K, X, V, W$ 共圆. 故 $K$ 为完全四边形 $U V W X Y Z$的 Miquel 点. 因此 $K, X, Z, Y$ 共圆.

综上, 四圆共点 $K$.



注. 极其困难的几何题. 笔者认为解此题的三个难点是：对 $H$, 九点圆, 外接圆关系的了解, 并用九点圆重新定义 $K$; 发现 $U V W X Y Z$ 是完全四边形，而 $K$ 为其 Miquel 点; 后面找好要导的角, 并在纷繁复杂的辅助线中找对导角的方向.

导角使用直线 (向量) 的有向夹角的好处有二：图形变化较多 (比如 $P$ 可以随意在圆周上运动), 在变化的过程中, 等角可能变成补角, 或出现其他类似的关系的变化 (例如 $W$ 若运动到 $K P$ 的另一侧, 则 $\angle P W K=2 \angle P T K$ 就不成立了), 而用有向夹角避免了这一问题, 更为严谨; 此外, 这样更容易描述不交的两线段之间的夹角, 而不必作出它们所在直线的交点, 这使导角的过程更为简洁易懂.

G8 设锐角三角形 $A B C$ 的外接圆为 $\Gamma$, 内心为 $I$. 过点 $B$ 的圆 $\omega_{B}$ 和过点 $C$ 的圆 $\omega_{C}$ 切于点 $I . \omega_{B}$ 分别交 $\Gamma$ 的劣弧 $A B$ 和线段 $A B$ 于 $P$ 和 $M$. 类似地, $\omega_{C}$ 分别交 $\Gamma$ 的劣弧 $A C$ 和线段 $A C$ 于 $Q$ 和 $N$. 射线 $P M$ 和射线 $Q N$ 交于点 $X$, 圆 $\omega_{B}$ 在 $B$ 处的切线和圆 $\omega_{C}$ 在 $C$ 处的切线交于点 $Y$. 证明: $A, X, Y$共线.



解. 我们先证明一个结论.

结论. $Y$ 在 $\Gamma$ 上.

结论的证明. 设 $\omega_{B}, \omega_{C}$ 的圆心分别为 $O_{B}, O_{C}$. 有

$$
\begin{aligned}
\angle B Y C & =360^{\circ}-\angle B O_{B} O_{C}-\angle O_{B} O_{C} C=2\left(\angle O_{B} I B+\angle O_{C} I C\right) \\
& =2\left(180^{\circ}-\angle B I C\right)=180^{\circ}-\angle B A C .
\end{aligned}
$$

故 $A, B, Y, C$ 共圆. 结论证毕.



原问题的证明. 我们用两种方法证明.
方法 1. 设 $\Gamma, \omega_{B}, \omega_{C}$ 的根心为 $D . \omega_{B}, \omega_{C}$ 在 $I$ 处的公切线分别交 $P M, N Q, B C$于 $X_{1}, X_{2}, S$.

$\angle P X_{1} S=180^{\circ}-\angle X_{1} M I-\angle X_{1} I M=180^{\circ}-\angle P B I-\angle M B I=180^{\circ}-\angle P B S$.

因此 $P, X_{1}, S, B$ 共圆. 同理, $Q, X_{2}, S, C$ 共圆. 因此由圆幂定理,

$$
D X_{1} \cdot D S=D P \cdot D B=D Q \cdot D C=D X_{2} \cdot D S
$$

故 $X_{1}=X_{2}=X$.

因此由圆幂定理,

$$
X M \cdot X P=X I^{2}=X N \cdot X Q .
$$

故 $P, M, N, Q$ 共圆.

延长 $P M, Q N$, 分别交 $\Gamma$ 于 $E, F$. 由 $\angle Y F Q=180^{\circ}-\angle Q C Y=\angle C N Q$,有 $N C \| F Y$. 同理, $M B \| E Y$. 由 $\angle X N M=\angle X P Q=\angle E F Q$, 有 $N M \| F E$.因此对 $\triangle A M N$ 和 $\triangle Y E F$ 由 Desagues 定理, $M E, N F, A Y$ 共点.



方法 2. 延长 $B I, C I$ 分别交 $\Gamma$ 于 $K, L$. 由于 $K$ 为弧 $A C$ 的中点, $\angle A L K=$ $\angle K L C$. 同理, $\angle A K L=\angle L K B$. 因此 $A, I$ 关于 $L K$ 对称.
设 $\omega_{B}, \omega_{C}$ 在 $I$ 处的公切线与 $K L$ 的交于 $X^{\prime}$.

$$
\angle X^{\prime} I P=\angle I B P=\angle K B P=\angle K L P=\angle X^{\prime} L P .
$$

故 $X^{\prime}, I, L, P$ 共圆. 因此

$$
\angle I P X^{\prime}=\angle I L X^{\prime}=\angle C L K=\angle C B K=\angle M B I=\angle M P I \text {. }
$$

因此 $P, M, X^{\prime}$ 共线. 同理, $Q, N, X^{\prime}$ 共线. 故 $X^{\prime}=X$.

因此 $X$ 在 $K L$ 上. 结合 $A, I$ 关于 $K L$ 对称, 有

$$
\angle X A K=\angle X I K=180^{\circ}-\angle X I B=\angle I B Y=\angle K A Y .
$$

故 $A, X, Y$ 共线.



注. 解法 1 反复利用圆幂和根心. 解法 2 的关键是 $K, X, L$ 共线.

G9 证明: 存在正常数 $c$, 使得下述结论成立:

设整数 $n \geq 2, \mathcal{S}$ 为平面上 $n$ 个点构成的集合, 使得其中任意两点间的距离至少为 1 . 则存在一条分割集合 $\mathcal{S}$ 的直线 $\ell$ 满足集合 $\mathcal{S}$ 中任意一点到 $\ell$ 的距离至少为 $c n^{-\frac{1}{3}}$.

(称直线 $\ell$ 分割集合 $\mathcal{S}$, 若 $\ell$ 与连接集合 $\mathcal{S}$ 中两点的某线段相交.)

解. 取 $c=\frac{1}{10}$. 我们证明, 此时命题成立.

反设不然. 则对任意一条分割 $\mathcal{S}$ 的直线 $\ell$, 均存在 $\mathcal{S}$ 中的点使其与 $l$ 的距离小于 $\frac{1}{10} n^{-\frac{1}{3}}$.

设 $d=\max _{X, Y \in \mathcal{S}}|X Y|, A, B \in \mathcal{S}$ 使 $|A B|=d$. 以 $A$ 为原点, $\overrightarrow{A B}$ 方向为 $x$ 轴
正方向建立平面直角坐标系. 设 $\mathcal{S}=\left\{X_{i}\left(x_{i}, y_{i}\right): 1 \leq i \leq n\right\}$, 其中 $0=x_{1} \leq$ $\cdots \leq x_{n}=d$. 对 $1 \leq i \leq n-1$, 对直线 $x=\frac{x_{i}+x_{i+1}}{2}$ 由反证假设, 有

$$
x_{i+1}-x_{i}<\frac{1}{5} n^{-\frac{1}{3}} .
$$

因此 $d<\frac{1}{5} n^{-\frac{1}{3}}(n-1)$.

设 $x_{t} \leq \frac{3}{5}<x_{t+1}$. 则结合 $(*)$,

$$
\frac{3}{5}<x_{t+1}<\frac{1}{5} n^{-\frac{1}{3}} t .
$$

故 $t>3 n^{\frac{1}{3}}$. 重新排列 $\left\{X_{i}\right\}_{1 \leq i \leq t}$ 为 $\left\{X_{i}^{\prime}\left(x_{i}^{\prime}, y_{i}^{\prime}\right)\right\}_{1 \leq i \leq t}$, 使 $y_{1}^{\prime} \leq \cdots \leq y_{t}^{\prime}$. 对 $1 \leq i \leq t-1$,

$$
y_{i+1}^{\prime}-y_{i}^{\prime}=\sqrt{\left|X_{i}^{\prime} X_{i+1}^{\prime}\right|^{2}-\left|x_{i}^{\prime}-x_{i+1}^{\prime}\right|^{2}} \geq \sqrt{1-\left(\frac{3}{5}\right)^{2}}=\frac{4}{5} .
$$

因此

$$
y_{t}^{\prime}-y_{1}^{\prime} \geq \frac{4}{5}(t-1)>\frac{12}{5} n^{\frac{1}{3}}-\frac{4}{5}
$$

不妨 $\left|y_{1}^{\prime}\right|>\left|y_{t}^{\prime}\right|$, 则有 $\left|y_{1}^{\prime}\right|>\frac{6}{5} n^{\frac{1}{3}}-\frac{2}{5}$. 故

$$
\begin{aligned}
\left|B X_{1}^{\prime}\right|^{2}-d^{2} & >\left(\frac{6}{5} n^{\frac{1}{3}}-\frac{2}{5}\right)^{2}+\left(d-\frac{3}{5}\right)^{2}-d^{2}=\frac{36}{25} n^{\frac{2}{3}}-\frac{24}{25} n^{\frac{1}{3}}-\frac{6}{5} d+\frac{13}{25} \\
& >\frac{36}{25} n^{\frac{2}{3}}-\frac{24}{25} n^{\frac{1}{3}}-\frac{6}{25} n^{-\frac{1}{3}}(n-1)+\frac{13}{25} \\
& =\frac{6}{5} n^{\frac{2}{3}}-\frac{24}{25} n^{\frac{1}{3}}+\frac{13}{25}+\frac{6}{25} n^{-\frac{1}{3}}>\frac{6}{5}\left(n^{\frac{1}{3}}-\frac{2}{5}\right)^{2}>0 .
\end{aligned}
$$

这与 $d$ 的定义矛盾!

注. 非常困难的组合几何问题. $C n^{-\frac{1}{2}}$ 是一个较好证明的结果. 开始设出的 $d$ 相当于把所有的点限制在了以 $A, B$ 为圆心 $d$ 为半径的两圆交出的 “東核形” $\Gamma$ 中. $\frac{3}{5}$ 可以先待定为 $u$ ( $\frac{3}{5}$ 不是最优的, 这里只是为了写起来方便). 解答中着重考察局部 $\Gamma \cap\{0 \leq x \leq u\}$, 得到了比较强的结果, 完成了这个问题.



## IV. 数论

$\mathbf{N} 1$ 给定正整数 $k$, 证明存在素数 $p$ 使得能够选取互异的正整数 $a_{1}, a_{2}, \cdots, a_{k+3}$ $\in\{1,2, \cdots, p-1\}$, 它们满足对任意 $i=1,2, \cdots, k, p$ 都整除 $a_{i} a_{i+1} a_{i+2} a_{i+3}-i$.

解: 因为素数有无穷多个, 可以取三个大于 $4 k+1$ 的互异素数 $q, r, t$.

令 $b_{1}=q, b_{2}=r, b_{3}=t, b_{4}=\frac{1}{q r t}$, 我们令 $b_{i} b_{i+1} b_{i+2} b_{i+3}=i$, 得到

对 $1 \leq s \leq k$,

$$
\begin{aligned}
b_{4 s+1} & =\frac{4 s-2}{4 s-3} \cdot \frac{4 s-6}{4 s-7} \cdots \frac{2}{1} \cdot q, \\
b_{4 s+2} & =\frac{4 s-1}{4 s-2} \cdot \frac{4 s-5}{4 s-6} \cdots \frac{3}{2} \cdot r, \\
b_{4 s+3} & =\frac{4 s}{4 s-1} \cdot \frac{4 s-4}{4 s-5} \cdots \frac{4}{3} \cdot t, \\
b_{4 s+4} & =\frac{4 s+1}{4 s} \cdot \frac{4 s-3}{4 s-4} \cdots \frac{5}{4} \cdot \frac{1}{q r t} .
\end{aligned}
$$

由于 $q, r, t$ 是大于 $4 k+1$ 的素数, 所以通过观察素数 $q, r, t$ 的幂次可以得到下面四个集合两两无交集.

$$
\left\{b_{4 s+1} \mid 0 \leq s \leq k\right\},\left\{b_{4 s+2} \mid 0 \leq s \leq k\right\},\left\{b_{4 s+3} \mid 0 \leq s \leq k\right\},\left\{b_{4 s+4} \mid 0 \leq s \leq k\right\}
$$

并且 $b_{i}<b_{i+4}$. 由这两点知, 对 $i \neq j, i, j \in\{1,2, \cdots, k+3\}$, 有 $b_{i} \neq b_{j}$.

我们记 $b_{i}=\frac{u_{i}}{v_{i}} .\left(i=1,2, \cdots, k+3, \operatorname{gcd}\left(u_{i}, v_{i}\right)=1\right)$.

由于素数有无穷多个, 我们可取一个素数 $p$, 使得 $p>\max _{i}\left\{u_{i}, v_{i}\right\}$ 且 $p>$ $\max _{i \neq j}\left|u_{i} v_{j}-u_{j} v_{i}\right|$. 由于 $u_{i} v_{j}-u_{j} v_{i} \neq 0$, 所以有 $p \nmid u_{i}, p \nmid v_{i}, p \nmid u_{i} v_{j}-u_{j} v_{i}$.

因为 $u_{i}, v_{i}$ 都与 $p$ 互质, 存在整数 $a_{i} \in\{1,2, \ldots, p-1\}$ 满足 $a_{i} v_{i} \equiv u_{i}$ $(\bmod p)$.

若对 $i \neq j$ 有 $a_{i}=a_{j}$, 则有

$$
u_{i} v_{j} \equiv\left(a_{i} v_{i}\right) v_{j} \equiv v_{i}\left(a_{j} v_{j}\right) \equiv v_{i} u_{j} \quad(\bmod p)
$$

这与 $p$ 的选取相矛盾. 所以 $a_{i}$ 两两不同.

并且我们有

$v_{k} v_{k+1} v_{k+2} v_{k+3} a_{k} a_{k+1} a_{k+2} a_{k+3} \equiv u_{k} u_{k+1} u_{k+2} u_{k+3} \equiv k v_{k} v_{k+1} v_{k+2} v_{k+3} \quad(\bmod p)$.

这里我们用到了 $b_{k} b_{k+1} b_{k+2} b_{k+3}=k$. 由于 $p$ 与 $v_{k} v_{k+1} v_{k+2} v_{k+3}$ 互质, 两边约去即得.

注. 简单的数论题. 利用 $a_{i} a_{i+1} a_{i+2} a_{i+3}=i$ 算出 $a_{i}$ 后设法将 $a_{i}$ 变为整数即可.
$\mathbf{N} 2$ 对任意素数 $p, p$-群岛联合王国是一个拥有 $p$ 座岛屿的国度, 这些岛屿编号为 $1,2, \cdots, p$. 两个不同的岛屿 $m$ 和 $n$ 之间有桥梁连通当且仅当 $p$ 整除 $\left(n^{2}-m+1\right)\left(m^{2}-n+1\right)$. 这些桥梁可能一座横跨于另一座之上, 但它们不会相交. 证明: 存在无穷多个素数 $p$, 使得在对应的 $p$-群岛联合王国中有两个岛之间没有一系列桥梁使之连通.

解法 1: 采用反证法. 假如只有有限多个这样的 $p$, 记全部这样的 $p$ 为 $p_{1}<p_{2}<\cdots<p_{k}$.

取 $t=3 p_{1} p_{2} \cdots p_{k}$ (若 $k=0$, 令 $t=3$ ), 任取一个 $t^{2}-t+1$ 的素因子 $p$, 则 $p$ 与 $t$ 互质, 推出 $p$ 不在 $3, p_{1}, p_{2}, \ldots, p_{k}$ 之中.

考虑 $p$-群岛联合王国.

由于 $p$ 是素数, $p \mid\left(n^{2}-m+1\right)\left(m^{2}-n+1\right)$ 可推出 $m \equiv n^{2}+1(\bmod p)$或 $n \equiv m^{2}+1(\bmod p)$.

我们在连接 $m, n$ 的边上画上箭头. 若 $p \mid n^{2}-m+1$ 就画一个 $n$ 指向 $m$的箭头, $p \mid m^{2}-n+1$ 就画一个 $m$ 指向 $n$ 的箭头. 这样每条边上至少有一个箭头, 至多有两个箭头.

我们可以发现, 在 $n^{2}+1 \not \equiv n(\bmod p)$ 时, $n$ 恰好指向一个点 $n^{2}+1(\bmod p)$,而在 $n^{2}+1 \equiv n(\bmod p)$ 时, $n$ 不指向任何点.

但注意 $n^{2}+1 \equiv n(\bmod p)$ 有两个模 $p$ 不同的解 $t$ 和 $p+1-t$. (如果这两者模 $p$ 相同, 意味着 $2 t \equiv 1(\bmod p)$, 于是 $0 \equiv 4 t^{2}-4 t+4 \equiv 1-2+4 \equiv 3$ $(\bmod p)$. 这与 $p \neq 3$ 相矛盾)

所以恰有 $p-2$ 个点指向了其他点, 也就是一共有 $p-2$ 个箭头. 那么至多有 $p-2$ 条桥梁. 这说明这些岛屿之间不连通.

任取属于不同连通分支的两个岛屿, 可知没有一条道路连接他们, 故 $p$ 符合题意. 但 $p \neq p_{1}, \cdots, p_{k}$. 与反证法假设矛盾! 原命题成立.

解法 2: 先证明：模 12 余 7 的素数有无穷多个.

用反证法, 假设模 12 余 7 的素数只有有限个, 记全体为 $p_{1}<p_{2}<\cdots<p_{k}$.考查 $\left(6 p_{1} \cdots p_{k}\right)^{2}-\left(6 p_{1} \cdots p_{k}\right)+1$ 的素因子 $p$,

有 $p \mid\left(12 p_{1} \cdots p_{k}-1\right)^{2}+3$, 这表明 $p>3$ 且

$$
\left(\frac{-1}{p}\right) \cdot\left(\frac{3}{p}\right)=1
$$

这个是 Legendre 符号.

又 $\left(6 p_{1} \cdots p_{k}\right)^{2}-\left(6 p_{1} \cdots p_{k}\right)+1 \equiv 3(\bmod 4)$, 故其必有一个模 4 余 3 的素
因子 $p_{0}$. 则有

$$
\left(\frac{-1}{p_{0}}\right)=-1
$$

并且由二次互反律知

$$
\left(\frac{3}{p_{0}}\right)\left(\frac{p_{0}}{3}\right)=(-1)^{\frac{p-1}{2}}=-1 .
$$

于是

$$
\left(\frac{3}{p_{0}}\right)=-1 \Longrightarrow\left(\frac{p_{0}}{3}\right)=1 \Longrightarrow p_{0} \equiv 1 \quad(\bmod 3) \text {. }
$$

$\Longrightarrow p_{0} \equiv 7(\bmod 12)$. 但 $p_{0}$ 与 $p_{1}, \ldots, p_{k}$ 均不同, 与模 12 余 7 素数有限多的假设相矛盾! 故 (1) 成立.

回到原题. 对每一个素数 $p \equiv 7(\bmod 12)$, 类似于上面推导可以得到 $\left(\frac{-3}{p}\right)=$ 1. 于是存在整数 $u$ 使得 $u^{2} \equiv-3(\bmod p)$.

取 $1 \leq s \leq p$ 使得 $u \equiv 2 s-1(\bmod p)$, 则有 $s^{2}-s+1 \equiv 0(\bmod p)$. 故 $s \neq 1$ 或 $p$. 有 $1<s<p$.

又

$$
(-1-s)(-1-(p+1-s)) \equiv-s^{2}+s+2 \equiv 3 \quad(\bmod p)
$$

并且 $\left(\frac{3}{p}\right)=-1$. 这推出

$$
\left(\frac{-1-s}{p}\right)=-1 \text { 或 }\left(\frac{-1-(p+1-s)}{p}\right)=-1
$$

若 $\left(\frac{-1-s}{p}\right)=-1$, 则与 $p-s$ 有路的仅有 $s$. (这是因为若 $p-s=m^{2}+1$ 会推出 $\left(\frac{-1-s}{p}\right)=\left(\frac{m^{2}}{p}\right)=1$, 矛盾. 而 $\left.(p-s)^{2}+1 \equiv s^{2}+1 \equiv s(\bmod p)\right)$.

而与 $s$ 有路的仅有 $p-s$. (这是因为 $s=m^{2}+1$ 的全部解为 $s$ 和 $p-s$. 而 $\left.s^{2}+1 \equiv s(\bmod p)\right)$.

于是 $s$ 与其余 $p-2$ 岛中任一岛均不连通.

若 $\left(\frac{-1-(p+1-s)}{p}\right)=-1$, 类似地, 与 $p+1-s$ 有路的只有 $s-1$, 与 $s-1$ 有路的只有 $p+1-s$. 所以 $s-1$ 被孤立了.

于是, $p$ 满足题意, 由 (1), 这样的 $p$ 有无穷个.

注: 解法 1 着重强调了 $n^{2}+1 \equiv n$ 会浪费边, 导致图不能连通. 解法 2 则细究该图结构, 利用二次剩余找到图中的一个孤立分支.

$\mathbf{N} 3$ 给定整数 $n \geq 2$, 是否存在非常数的正整数数列 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 使得其中任意两项的算术平均值等于其中若干项（一项或者多项）的几何平均值?
解: 不妨设 $n$ 张卡片上写的数为 $a_{1} \geq a_{2} \geq a_{3} \geq \cdots \geq a_{n}$, 且 $\left(a_{1}, a_{2}, \cdots a_{n}\right)=$ 1.

若 $a_{1}>1$, 取素数 $p \mid a_{1}$, 我们归纳证明: $p \mid a_{i}, i=1,2,3, \ldots, n$.

由 $p \mid a_{1}$, 归纳奠基是显然的.

现在设 $i \leq k$ 时都有 $p \mid a_{i}$, 考察 $a_{k+1}$. 设

$$
\frac{a_{1}+a_{k+1}}{2}=\left(a_{i_{1}} a_{i_{2}} \cdots a_{i_{m}}\right)^{\frac{1}{m}}
$$

若 $a_{k+1}=a_{k}$, 则由归纳假设知已成立. 若 $a_{k+1}<a_{k}$, 则 $i_{1}, i_{2}, \ldots, i_{m}$ 中存在一个不超过 $k$. (若不然, 上式右边不大于 $a_{k+1}$, 而上式左边严格大于 $a_{k+1}$, 矛盾.)

故由归纳假设知 $p \mid a_{i_{1}} a_{i_{2}} \cdots a_{i_{m}}$.

又 $\left(a_{i_{1}} a_{i_{2}} \cdots a_{i_{m}}\right)^{\frac{1}{m}}=\frac{a_{1}+a_{k+1}}{2}$ 是有理数, 由算术基本定理知, 其为一个整数,且是 $p$ 的倍数. 即

$$
p\left|\left(a_{i_{1}} a_{i_{2}} \cdots a_{i_{m}}\right)^{\frac{1}{m}}=\frac{a_{1}+a_{k+1}}{2} \Longrightarrow p\right| a_{k+1} .
$$

命题对 $k+1$ 成立, 故由归纳原理知 $p \mid a_{1}, a_{2}, \cdots, a_{n}$.

这与 $\left(a_{1}, a_{2}, \ldots, a_{n}\right)=1$ 的假设相矛盾.

于是 $a_{1}=1 \Longrightarrow a_{2}=a_{3}=\cdots=a_{n}=1$. 由此立刻得到问题对一切 $n \geq 2$是不存在的.

注: 2020 年 IMO 第 5 题. 此题关键是要想到用数论手段来证明.

$\mathbf{N} 4$ 对任意奇素数 $p$ 和正整数 $n$, 令 $d_{p}(n) \in\{0,1, \cdots, p-1\}$ 为 $n$ 除以 $p$ 的余数. 数列 $\left(a_{0}, a_{1}, a_{2}, \cdots\right)$ 若满足 $a_{0}$ 是与 $p$ 互素的正整数且对 $n \geq 0$, $a_{n+1}=a_{n}+d_{p}\left(a_{n}\right)$, 则我们称是其一个 $p$-数列.

$1)$ 是否存在无穷多个素数 $p$, 使得存在 $p$-数列 $\left(a_{0}, a_{1}, a_{2}, \cdots\right)$ 和 $\left(b_{0}, b_{1}, b_{2}, \cdots\right)$满足 $a_{n}>b_{n}$ 对无穷多个正整数 $n$ 成立, 且 $a_{n}<b_{n}$ 也对无穷多个正整数 $n$ 成立?

2) 是否存在无穷多个素数 $p$, 使得存在 $p$-数列 $\left(a_{0}, a_{1}, a_{2}, \cdots\right)$ 和 $\left(b_{0}, b_{1}, b_{2}, \cdots\right)$满足 $a_{0}<b_{0}$, 但对 $n \geq 1$ 都有 $a_{n}>b_{n}$ 成立?

解: (a) 由 Bertrand-Chebyshev 素数定理, 对 $\forall k \in \mathbb{N}^{*}$, 存在素数 $p \in$ $\left[2^{12 k+2}, 2^{12 k+3}\right)$.

由于 $7\left|2^{12 k+3}-1,5\right| 2^{12 k+3}-3$, 知 $p \leq 2^{12 k+3}-5$.

设 $s$ 是 2 对 $p$ 的阶, 即最小的满足 $2^{\alpha} \equiv 1(\bmod p)$ 的 $\alpha$.

$$
\begin{gathered}
\text { 令 } a_{0}=2^{12 k}, b_{0}=\frac{1}{2}(p+1) \text {. 则 } 2^{12 k+1}<b_{0}<2^{12 k+2} \text {. 则有 } \\
a_{1}=2^{12 k+1}, a_{2}=2^{12 k+2}, a_{3}=2^{12 k+3} . \\
b_{1}=p+1, b_{2}=p+2, b_{3}=p+4 .
\end{gathered}
$$

故有 $a_{3}>b_{3}, a_{0}<b_{0}$.

由于

$$
\begin{aligned}
& a_{n+1} \equiv 2 a_{n}(\bmod p) \\
& b_{n+1} \equiv 2 b_{n} \quad(\bmod p)
\end{aligned}
$$

且由于 $2^{s} \equiv 1(\bmod p)$, 所以 $a_{n}(\bmod p), b_{n}(\bmod p)$ 均以 $s$ 为循环. 并且 $a_{1} \equiv 2^{12 k+1} b_{1}(\bmod p)$ 知前者的循环节是后者的循环节的一个排列.

对任意正整数 $u$,

$$
\begin{aligned}
d_{p}\left(a_{u}\right)+d_{p}\left(a_{u+1}\right)+\cdots+d_{p}\left(a_{u+s-1}\right) & =d_{p}(1)+d_{p}(2)+d_{p}(4)+\cdots+d_{p}\left(2^{s-1}\right) \\
& =d_{p}\left(b_{u}\right)+d_{p}\left(b_{u+1}\right)+\cdots+d_{p}\left(b_{u+s-1}\right)
\end{aligned}
$$

这推出对任意正整数 $v, a_{s v}<b_{s v}, a_{s v+3}>b_{s v+3}$. 因此本小问的答案是肯定的.

(b) 取 $q$ 为一个大于 2 的素数, $p$ 为 $2^{q}-1$ 的素因子, 那么 $q$ 是 2 对 $p$ 的阶, 所以 $q \mid p-1$. 于是 $p>q$.

对于任意 $1 \leq x \leq p-1,\left\{d_{p}\left(2^{n} x\right)\right\}_{n}$ 的最小正周期是 $q$.

记

$$
S_{1}=\sum_{i=0}^{q-1} d_{p}\left(2^{i}\right), S_{-1}=\sum_{i=0}^{q-1} d_{p}\left(-2^{i}\right)
$$

由于 $d_{p}\left(2^{i}\right)+d_{p}\left(-2^{i}\right)=p$, 所以 $S_{1}+S_{-1}=p q$. 由于 $p, q$ 都是奇数, 所以 $S_{1} \neq S_{-1}$.

(情况 1) 若 $S_{1}>S_{-1}$, 令 $x_{0}=1, y_{0}=p-1$.

则对任意 $0 \leq r \leq q-1, M \in \mathbb{N}$,

$$
x_{q M+r}=S_{1} M+x_{r}, y_{q M+r}=S_{-1} M+y_{r} .
$$

由 $S_{1}>S_{-1}$, 故当 $u$ 充分大时, $x_{u}>y_{u}$. 又 $x_{0}<y_{0}$, 存在 $s \in \mathbb{N}$ 使 $s$ 是满足 $x_{s}<y_{s}$ 的最大正整数, 把 $x_{0}, \ldots, x_{s-1}$ 和 $y_{0}, \ldots, y_{s-1}$ 都删去, 使得 $x_{s}, y_{s}$ 是新的首项即可满足要求.

(情况 2) 若 $S_{1}<S_{-1}$, 令 $x_{0}=p-1, y_{0}=p+1$.

则对任意 $0 \leq r \leq q-1, M \in \mathbb{N}$,

$$
x_{q M+r}=S_{-1} M+x_{r}, y_{q M+r}=S_{1} M+y_{r} .
$$

由 $S_{1}<S_{-1}$, 故当 $u$ 充分大时, $x_{u}>y_{u}$. 又 $x_{0}<y_{0}$, 存在 $s \in \mathbb{N}$ 使 $s$ 是满足 $x_{s}<y_{s}$ 的最大正整数, 把 $x_{0}, \ldots, x_{s-1}$ 和 $y_{0}, \ldots, y_{s-1}$ 都删去, 使得 $x_{s}, y_{s}$ 是新的首项即可满足要求.

又由 $\left(2^{s}-1,2^{t}-1\right)=2^{(s, t)}-1$, 所以不同的 $q$ 对应不同的 $p$, 由于素数 $q$有无穷多个, 所以 $p$ 也有无穷多个.

综上, 本小问答案亦为存在无穷多个 $p$.

注: 比较容易注意到的是 $d_{p}\left(a_{n+1}\right) \equiv 2 d_{p}\left(a_{n}\right)(\bmod p)$. 应围绕一个周期内各值之和这一特征量来解题.

N5 试确定所有定义在正整数集上并在非负整数集上取值的，满足下列三个条件的所有函数 $f$ :

(1) 至少存在一个 $n$ 使得 $f(n) \neq 0$;

(2) 对任意正整数 $x$ 和 $y$, 都有 $f(x y)=f(x)+f(y)$;

(3) 存在无穷多个正整数 $n$, 使得对任意 $k<n$ 都有 $f(k)=f(n-k)$.

解法 1: 由 (2), 立知: 如果 $n$ 的素因数分解的是 $p_{1}^{\alpha} p_{2}^{\alpha_{2}} \cdots p_{s}^{\alpha_{s}}$, 则 $f(n)=$ $\alpha_{1} f\left(p_{1}\right)+\alpha_{2} f\left(p_{2}\right)+\cdots+\alpha_{s} f\left(p_{s}\right)$.

于是由 (1) 知, 存在一个素数的 $f$ 值非零. 设 $p$ 是最小的使 $f(p) \neq 0$ 的素数.

若存在满足 (3) 的 $n$, 使 $n$ 写成 $p^{\alpha} \cdot t$ 后有 $t \geq p$. 这里的 $p, t$ 互质.

则 $t=\frac{n}{p^{p_{p}(n)}}$, 并且由 $t \neq p$ 知 $t>p$.

设 $t=k p+s$, 这里 $k, s$ 是正整数, 且 $0<s<p$.

由

$$
f\left(p^{\alpha} \cdot s\right)=f\left(p^{\alpha} \cdot k p\right) \Longrightarrow f(s)=f(k)+f(p)>0 \text {. }
$$

故存在素数 $u \mid s$, 使 $f(u)>0$, 而 $u \leq s<p$, 这与 $p$ 的选取相矛盾.

因此对满足 (3) 的每个 $n$, 有: $\frac{n}{p^{v_{p}(n)}}<p$.

若存在素数 $q>p$, 使 $f(q) \neq 0$, 取 $q$ 就是最小的那个.

设 $v$ 使 $p^{v} \geq q+1$, 由于满足 (3) 的 $n$ 有无穷多个且 $\frac{n}{p^{v_{p}(n)}}$ 有界. 这说明 $v_{p}(n)$ 是无界的.

故存在 $n$ 满足 (3), 使 $v_{p}(n) \geq v$. 仍记 $n=p^{\alpha} \cdot t$. 我们已经证明 $t<p$, 并且我们选取了 $\alpha \geq v$.

做带余除法 $n=k_{1} q+s_{1}$, 由于 $n>q$ 并且 $n, q$ 互质, 我们可以选取 $k_{1}, s_{1}$
是正整数, 并且 $s_{1}<q$.

由条件 (3), $f\left(s_{1}\right)=f\left(k_{1} q\right)>0$. 所以 $s_{1}$ 有一个素因子的 $f$ 值大于 0 . 但 $s_{1}<q$, 所以这个素因子只能是 $p$. 即有 $p \mid s_{1}$.

故有 $p\left|n-s_{1}=q k_{1} \Longrightarrow p\right| k_{1}$. 记 $s_{1}=p s_{2}, k_{1}=p k_{2}$.

除以 $p$, 有

$$
\frac{n}{p}=k_{2} q+s_{2} .
$$

$f\left(s_{2} p\right)=f\left(k_{2} q p\right) \Longrightarrow f\left(s_{2}\right)=f\left(k_{2} q\right)>0$, 而 $s_{2}<s_{1}<q$, 类似地可推出 $p \mid s_{2}$,且有 $p \left\lvert\, \frac{n}{p}\right.$, 故有 $p \mid k_{2}$. 记 $s_{2}=p s_{3}, k_{2}=p k_{3}$.

再除以 $p$, 有

$$
\frac{n}{p^{2}}=k_{3} q+s_{3}
$$

$f\left(s_{3} p^{2}\right)=f\left(k_{3} q p^{2}\right) \Longrightarrow f\left(s_{3}\right)=f\left(k_{3} q\right)>0$, 类似地可推出 $p \mid s_{3}$, 且有 $p \left\lvert\, \frac{n}{p^{2}}\right.$,故有 $p \mid k_{3}$. 记 $s_{3}=p s_{4}, k_{3}=p k_{4}$.

一直继续下去. 由于 $p^{v} \mid n$, 所以我们可以得到 $s_{1}=p^{v} s_{v+1}$. 但 $0<s_{1}<$ $q<p^{v}$, 矛盾.

因此有且只有一个素数的 $f$ 值非零. 我们记 $f(p)=c \in \mathbb{N}^{*}$. 则

$$
f(n)=v_{p}(n) \cdot f(p)=c v_{p}(n) .
$$

我们来验证其满足题意. (1), (2) 是显然满足的.

又对 $\alpha \in \mathbb{N}^{*}$, 和 $1 \leq k \leq p^{\alpha}-1$,

$$
v_{p}(k)=v_{p}\left(p^{\alpha}-k\right) .
$$

因此 $p^{\alpha}, \forall \alpha \in \mathbb{N}^{*}$ 均满足 (3).

综上, 所求为: $f(n)=c v_{p}(n) . c$ 是任意的正整数, $p$ 是任意的素数.

## 解法 2:

如果一个素数 $p$ 满足 $f(p)>0$, 称之为好数.

记 $G$ 为所有好数构成的集合, 设 $G$ 的所有元素从小到大排列为 $p_{1}<p_{2}<$

由 (2) 知, $f(n)=\sum_{i} v_{p_{i}}(n) f\left(p_{i}\right)$.

令 $e(n)=\prod_{p \in G} p^{v_{p}(n)}$ 则 $f\left(\frac{n}{e(n)}\right)=0$. 于是 $f(n)=f(e(n))$.

我们还可以发现, 若 $e(a) \mid b$, 则有 $e(a) \mid e(b)$. (因为 $\frac{b}{e(b)}$ 中没有好的素因子,而 $e(a)$ 中只能有好的素因子, 所以 $e(a)$ 和 $\frac{b}{e(b)}$ 互质.) 再由 $e(b) \mid b$ 知, $e(a) \mid e(b)$等价于 $e(a) \mid b$.
引理: 如果一个正整数 $n$ 满足 (3), 则 $\forall 1 \leq k \leq n-1, e(k)=e(n-k)$.

采用反证法, 若存在 $k$ 使上式不成立, 取这样的最小的 $k$.

若 $f(k)=0 \Longrightarrow f(n-k)=0 \Longrightarrow e(k)=e(n-k)=1$ 矛盾!

故 $f(k) \neq 0, e(k) \neq 1$, 令 $t=\frac{k}{e(k)}$.

因为 $e(k) \mid k$, 所以在 $[1, k]$ 与 $[n-k, n-1]$ 上, 分别有 $t$ 个 $e(k)$ 的倍数. 所以 $e(1), e(2), \ldots, e(k)$ 中有 $t$ 个 $e(k)$ 的倍数, $e(n-k), e(n-k+1), \ldots, e(n-1)$中有 $t$ 个 $e(k)$ 的倍数.

在 $[1, k-1]$ 上有 $t-1$ 个 $e(k)$ 的倍数. 所以 $e(1), e(2), \ldots, e(k-1)$ 中有 $t-1$ 个 $e(k)$ 的倍数.

由归纳假设知, $e(n-k+1), e(n-k+2), \ldots, e(n-1)$ 中也有 $t-1$ 个 $e(k)$的倍数. 所以 $e(n-k)$ 是 $e(k)$ 的倍数.

另一方面，

$$
f(e(k))=f(k)=f(n-k)=f(e(k))+f\left(\frac{n-k}{e(k)}\right) .
$$

因此, $\frac{n-k}{e(k)}$ 没有好素因子. 所以 $e(n-k) \mid e(k)$.

故 $e(n-k)=e(k)$, 矛盾! 引理成立.

回到原题, 若 $|G| \geq 2$, 取一个正整数 $n$ 满足条件 (3), 并且 $n>p_{1} p_{2}$

设 $\alpha$ 满足 $p_{1}^{\alpha}<n \leq p_{1}^{\alpha+1}<p_{1}^{\alpha} p_{2}$

$$
e\left(n-p_{1}^{\alpha}\right)=e\left(p_{1}^{\alpha}\right)=p_{1}^{\alpha} .
$$

因此, $p_{1}^{\alpha} \mid n$, 同理 $p_{2} \mid n$. 于是 $n \geq p_{1}^{\alpha} p_{2}$, 矛盾!

故 $|G|=1, f(n)=C v_{p}(n)$. 验证的过程同解法 1 .

解法 3: 我们有

$$
f(n-1)+f(n-2)+\cdots+f(n-k)=f(1)+\cdots+f(k)+f\left(\left(\begin{array}{c}
n-1 \\
k
\end{array}\right)\right) .
$$

因此对满足 (3) 的 $n,\left(\begin{array}{c}n-1 \\ k\end{array}\right)$ 没有满足 $f(p)>0$ 的素因子 $p$.

故对每个素数 $p$ 使 $f(p)>0$, 由 Lucas 定理, 满足 (3) 的 $n$ 必形如 $a \cdot p^{s}(a<$

p)

因此满足 $f(p)>0$ 的素数 $p$ 至多一个. 否则若有素数 $p \neq q$ 使得 $f(p), f(q)>$ 0 . 则 $a \cdot p^{s}=n=b q^{t}$. 当 $a$ 确定后, 这样的 $s$ 至多有有限多个. 所以这样的 $n$也至多有有限多个, 矛盾.

故 $f(n)=C v_{p}(n)$. 验证同解答 1 .

解法 4: 对素数 $p$ 定义 $g(p)=\frac{f(p)}{\ln p}$.
取一个满足 (3) 的正整数 $n$, 若存在素数 $p<n$ 使得 $f(p) \neq 0$, 记所有这样的 $p$ 为 $p_{1}, p_{2}, \ldots, p_{k}$.

不妨设 $g\left(p_{1}\right)=\max \left\{g\left(p_{i}\right)\right\}$.

设 $p_{1}^{\alpha_{1}} \leq n<p_{1}^{\alpha_{1}+1}$. 对 $k<p_{1}^{\alpha_{1}}$, 设 $e(k)=p_{1}^{\beta_{1}} \cdots p_{k}^{\beta_{k}}$. 这里, $e(k)$ 的定义同解答 2 .

有

$$
\begin{aligned}
f(k) & =\beta_{1} f\left(p_{1}\right)+\cdots+\beta_{k} f\left(p_{k}\right) \\
& =g\left(p_{1}\right) \beta_{1} \ln p_{1}+\cdots+g\left(p_{k}\right) \beta_{k} \ln p_{k} \\
& \leq g\left(p_{1}\right)\left(\beta_{1} \ln p_{1}+\cdots+\beta_{k} \ln p_{k}\right) \\
& \leq g\left(p_{1}\right) \ln k \\
& <g\left(p_{1}\right) \alpha_{1} \ln p_{1}=f\left(p_{1}^{\alpha_{1}}\right) .
\end{aligned}
$$

若 $p_{1}^{\alpha_{1}} \nmid n$, 设 $n=b_{1} p_{1}^{\alpha_{1}}+r_{1}, 0<r_{1}<p_{1}^{\alpha_{1}}$, 就有 $f\left(r_{1}\right)=f\left(b_{1} p_{1}^{\alpha_{1}}\right) \geq f\left(p_{1}^{\alpha_{1}}\right)$,矛盾!

故 $n=p_{1}^{\alpha_{1}} \cdot b_{1}$, 对某个 $b_{1}<p_{1}$. 于是 $n$ 的最大素因子是 $p_{1}$.

如果 $k \geq 2$, 那么我们考虑 $h(x)=f(x)-f\left(p_{1}\right) v_{p_{1}}(x)$. 那么 $h(x)$ 仍然满足条件 $(2),(3)$. 并且 $h\left(p_{i}\right) \neq 0, \forall i \neq 1$.

记 $G(x)=\frac{h(p)}{\ln p}$, 我们不妨设 $G\left(p_{2}\right)=\max _{i>1}\left\{G\left(p_{i}\right)\right\}$.

设 $p_{2}^{\alpha_{2}} \leq n<p_{2}^{\alpha_{2}+1}$. 对 $k<p_{2}^{\alpha_{2}}, e(k)=p_{1}^{\beta_{1}} \cdots p_{k}^{\beta_{k}}$, 我们有

$$
\begin{aligned}
h(k) & =\beta_{2} h\left(p_{2}\right)+\cdots+\beta_{k} h\left(p_{k}\right) \\
& =G\left(p_{2}\right) \beta_{2} \ln p_{2}+\cdots+G\left(p_{k}\right) \beta_{k} \ln p_{k} \\
& \leq G\left(p_{2}\right)\left(\beta_{2} \ln p_{2}+\cdots+\beta_{k} \ln p_{k}\right) \\
& \leq G\left(p_{2}\right) \ln k \\
& <G\left(p_{2}\right) \alpha_{2} \ln p_{2}=h\left(p_{2}^{\alpha_{2}}\right) .
\end{aligned}
$$

若 $p_{2}^{\alpha_{2}} \nmid n$, 可设 $n=b_{2} p_{2}^{\alpha_{2}}+r_{2}, 0<r_{2}<p_{2}^{\alpha_{2}}$, 就有 $h\left(r_{2}\right)=h\left(b_{2} p_{2}^{\alpha_{2}}\right) \geq h\left(p_{2}^{\alpha_{2}}\right)$,矛盾! 所以 $n=b_{2} p_{2}^{\alpha_{2}}$, 对某个 $b_{2}<p_{2}$.

于是 $n$ 的最大素因子是 $p_{2}$, 矛盾. 故 $k=1$. 这意味着 $h(x)$ 恒等于 0 . 即 $f(x)=f\left(p_{1}\right) v_{p_{1}}(x)$, 对所有 $x \leq n$ 成立. 所以对每个满足条件 (3) 的 $n$, 小于 $n$的素数至多有一个的 $f$ 值非零.

又由于这样的 $n$ 有无穷多个, 所以有且仅有一个素数 $p$ 使得 $f(p) \neq 0$, 记为 $p_{0}$. 并且有 $f(x)=f\left(p_{0}\right) v_{p_{0}}(x)$ 对 $x<n$ 成立, 于是 $f(x)=f\left(p_{0}\right) v_{p_{0}}(x)$, 对所有正整数 $x$ 成立. 验证同解答 1 .
注: 怎样利用好条件 (iii) 是最核心的问题.

N6 对正整数 $n$, 记 $d(n)$ 为 $n$ 的正约数个数, $\varphi(n)$ 为与 $n$ 互素的不超过 $n$ 的正整数个数. 是否存在常数 $C$ 使得

$$
\frac{\varphi(d(n))}{d(\varphi(n))} \leq C ?
$$

对任意 $n \geq 1$ 均成立?

解法 1: 我们证明这样的 $C$ 不存在. 不妨假设 $C>0$.

由素数定理, 对充分大的正整数 $s,(s, 2 s]$ 中素数个数大于 $\frac{s}{10 \ln s}$. 故我们可以取一个 $s$, 使得 $(s, 2 s]$ 中素数个数大于 $\log _{2}(C+1)+1$.

设 $1,2, \cdots, s$ 中的全体素数为 $p_{1}, p_{2}, \cdots, p_{t}$. 再设 $s+1, s+2, \cdots, 2 s$ 中的全体素数为 $q_{1}, q_{2}, \cdots, q_{r}$. 有 $2^{r-1}>C+1$.

由于 $p_{i}-1$ 和 $\frac{q_{j}-1}{2}$ 都不大于 $s$, 所以素因子都不大于 $s$, 故可以分解为这样的形式

$$
\left(p_{1}-1\right) \cdots\left(p_{t}-1\right)\left(q_{1}-1\right) \cdots\left(q_{r}-1\right)=p_{1}^{\alpha_{1}} \cdots p_{t}^{\alpha_{t}}
$$

令 $n=p_{1}^{2^{m}-1} p_{2}^{2^{m}-1} \cdots p_{t}^{2^{m}-1} q_{1} \cdots q_{r} . m$ 是待定的正整数.

此时

$$
\begin{aligned}
\varphi(d(n)) & =\varphi\left(2^{m t+r}\right)=2^{m t+r-1} \\
d(\varphi(n)) & =d\left(p_{1}^{2^{m}-2+\alpha_{1}} \cdots p_{t}^{2^{m}-2+\alpha_{t}}\right) \\
& =\left(2^{m}-1+\alpha_{1}\right) \cdots\left(2^{m}-1+\alpha_{t}\right)
\end{aligned}
$$

于是

$$
\frac{\varphi(d(n))}{d(\varphi(n))}=\frac{2^{m}}{2^{m}-1+\alpha_{1}} \cdots \frac{2^{m}}{2^{m}-1+\alpha_{t}} \cdot 2^{r-1}
$$

由

$$
\lim _{m \rightarrow+\infty} \frac{2^{m}}{2^{m}-1+\alpha_{i}}=1, i=1,2, \cdots t
$$

得

$$
\lim _{m \rightarrow+\infty} \frac{\varphi(d(n))}{d(\varphi(n))}=2^{r-1}
$$

故存在 $m$ 使得

$$
\frac{\varphi(d(n))}{d(\varphi(n))}>2^{r-1}-1>C
$$

此即矛盾. 故不存在这样的 $C$.

## 解法 2:

取 $m>5$ 充分大, $n=p_{1} p_{2} \cdots p_{\pi(m)} .\left(\pi(m)\right.$ 为不大于 $m$ 的素数个数, $p_{i}$ 为从小到大第 $i$ 小的素数) 则 $\varphi(d(n))=2^{\pi(m)-1}$.

$$
\varphi(n)=\prod_{k=1}^{\pi(m)}\left(p_{k}-1\right)=\prod_{s=1}^{\pi(m / 2)} p_{s}^{\alpha_{s}}
$$

由于每个 $p_{k}-1$ 至多有一个 $>\sqrt{m}$ 的素因子,

$$
\sum_{\left\{s: \sqrt{m}<p_{s} \leq m / 2\right\}} \alpha_{s} \leq \pi(m)
$$

记 $l$ 为 $\left(\sqrt{m}, \frac{m}{2}\right]$ 中的素数个数, 则由均值不等式及 $l \leq \pi(m / 2)$ 知

$$
\prod_{\left\{s: \sqrt{m}<p_{s} \leq m / 2\right\}}\left(\alpha_{s}+1\right) \leq\left(\frac{\pi(m)+\pi\left(\frac{m}{2}\right)}{l}\right)^{l} \leq e^{\left(\pi(m)+\pi\left(\frac{m}{2}\right)\right) / e} .
$$

这里用到了 $\left(\frac{A}{x}\right)^{x} \leq e^{A / e}$. (由熟知结论 $y^{1 / y} \leq e^{1 / e}$, 再令 $y=A / x$ 即得.)

又由于

$$
\alpha_{i} \leq \log _{2}(\varphi(n)) \leq \log _{2} n \leq \pi(m) \log _{2} m<m^{2}
$$

故有

$$
\prod_{\left\{s: p_{s} \leq \sqrt{m}\right\}}\left(\alpha_{s}+1\right) \leq\left(m^{2}\right)^{\sqrt{m}}=m^{2 \sqrt{m}}
$$

我们得到估计

$$
d(\varphi(n))=\prod_{\left\{s: p_{s} \leq m / 2\right\}}\left(\alpha_{s}+1\right) \leq e^{2 \sqrt{m} \ln m+\frac{\pi(m)+\pi\left(\frac{m}{2}\right)}{e}} .
$$

则有

$$
\limsup _{m \rightarrow+\infty} \frac{\ln (d(\varphi(n))}{m / \ln m} \leq \frac{3}{2 e}
$$

再由于

$$
\lim _{m \rightarrow+\infty} \frac{\ln (\varphi(d(n)))}{m / \ln m}=\ln 2 .
$$

以及

$$
\frac{3}{2 e}<\ln 2 .
$$

得 $m$ 充分大时,

$$
\frac{\ln (\varphi(d(n)))-\ln (d(\varphi(n)))}{m / \ln m}>\frac{1}{2}\left(\ln 2-\frac{3}{2 e}\right)>0 .
$$

这推出 $\ln (\varphi(d(n)))-\ln (d(\varphi(n)))$ 无上界, 即 $\frac{\varphi(d(n))}{d(\varphi(n))}$ 无上界.

注：思路分为两方面：(1) 使 $\varphi(d(n))$ 较大, 这可以通过让 $\forall p \mid n, v_{p}(n)+1$为 2 的幂来满足; $(2)$ 使 $d(\varphi(n))$ 较小, 主旨思想是让 $\varphi(n)$ 质因子集中分布, 且次数较大.

N7 由 $n \geq 3$ 个正整数构成的集合 $\mathcal{S}$ 中, 任意一个元素不等于其它两个不同元素的和. 证明: 可以将 $\mathcal{S}$ 中的元素排列成 $a_{1}, a_{2}, \cdots, a_{n}$, 使此排列满足对任意 $i=2,3, \cdots, n-1, a_{i}$ 均不整除 $a_{i-1}+a_{i+1}$.

解法 1: 我们归纳证明一个更强的命题.

存在排列 $a_{1}, a_{2}, \cdots, a_{n}$, 使得对任意 $1<i<n, a_{i} \nmid a_{i-1}+a_{i+1}$ 且 $a_{i} \nmid$ $a_{i-1}-a_{i+1}$.

$n=2$ 时, 命题是显然的. 现在设 $n=k$ 时成立, 考虑 $n=k+1$ 时.

设 $S$ 的最大元素为 $u$, 由归纳假设, $S \backslash\{u\}$ 的 $k$ 个元素可以排列为 $a_{1}, a_{2}, \cdots, a_{k}$,使 $\forall 2 \leq i \leq k-1, a_{i} \nmid a_{i-1}+a_{i+1}$ 且 $a_{i} \nmid a_{i-1}-a_{i+1}$.

我们证明, 存在 $0 \leq j \leq k$, 使 $a_{1}, a_{2}, \cdots, a_{j}, u, a_{j+1}, \cdots, a_{k}$ 满足条件. ( $j=$ 0 意味着 $u$ 放在最前面, $j=k$ 意味着 $u$ 放在最后面)

事实上, 对一个 $j$, 若上排列不满足条件, 必有

$$
a_{j} \mid u-a_{j-1} \text { 或 } a_{j} \mid u+a_{j-1} \text {. }
$$

或

$$
a_{j+1} \mid u-a_{j+2} \text { 或 } a_{j+1} \mid u+a_{j+2} \text {. }
$$

(这是因为 $u>a_{j}, a_{j+1}$, 所以 $u \nmid a_{j}-a_{j+1}$, 且 $a_{j}+a_{j+1}<2 u, u \neq a_{j}+a_{j+1}$,故 $\left.u \nmid a_{j}+a_{j+1}\right)$

若 (1) 成立, 将 $j$ 涂红, 若 (2) 成立, 将 $j+1$ 涂蓝. 那么只有 $1,2, \ldots, k$ 可能被涂色.

我们说: $\forall 1 \leq j \leq k, j$ 不会被既被涂红又被涂蓝.

用反证法, 假设存在 $j$, 使得 $j$ 被涂两色, 那么存在 $\varepsilon_{1}, \varepsilon_{2} \in\{-1,1\}$

$$
a_{j}\left|u+\varepsilon_{1} a_{j-1}, a_{j}\right| u+\varepsilon_{2} a_{j+1} \Longrightarrow a_{j} \mid a_{j-1}-\left(\varepsilon_{1} \varepsilon_{2}\right) a_{j+1}
$$

这与归纳假设矛盾! 因此, 每个 $j$ 至多被涂一种颜色.

我们希望寻找一个 $j$, 使得 $j$ 不被涂红, 且 $j+1$ 不被涂蓝. 这样的话

$$
a_{1}, a_{2}, \cdots, a_{j}, u, a_{j+1}, \cdots, a_{k}
$$

满足题意, 命题对 $k+1$ 成立, 由归纳原理知结论成立.

用反证法, 假设对任意 $0 \leq j \leq k$, 要么 $j$ 被涂红, 要么 $j+1$ 被涂蓝. 那么由于 0 没有被涂色, 所以 1 被涂成蓝色. 于是 2 被涂成蓝色, 以此类推.

但是 $k+1$ 没有被涂色, 所以 $j=k$ 不满足 “要么 $j$ 被涂红, 要么 $j+1$ 被涂蓝”, 矛盾.
解法 2: 我们证明一个更强的命题:

设 $S$ 是一个由 $n \geq 3$ 个不同正整数构成的集合, 则: 其所有元素可以排列成 $a_{1}, a_{2}, \cdots, a_{n}$, 使得如果有 $a_{i} \mid a_{i-1}+a_{i+1}$, 一定有 $a_{i}=\max \left\{a_{1}, a_{2}, \ldots a_{n}\right\}$.

由这个命题可以推出我们原命题. 因为若 $a_{i}>a_{i-1}, a_{i}>a_{i+1}, a_{i} \mid a_{i-1}+$ $a_{i+1}$, 可以推出 $a_{i}=a_{i-1}+a_{i+1}$. 这与题目条件相矛盾.

对 $a<b$, 定义 $f(a, b)$ 是属于 $\{1,2, \cdots, a\}$ 且满足 $a \mid b+f(a, b)$ 的唯一正整数. 因此, 如果 $a<b<c$ 且 $b \mid a+c$, 必有 $a=f(b, c)$.

因此, 我们只用证如下更强的引理：

设 $S$ 是由 $n \geq 3$ 个不同正整数构成的集合, $f$ 是一个函数, 对 $a<b \in S, f$会把 $(a, b)$ 映射到 $\{1,2, \cdots, a\}$ 中的某一值.

则 $S$ 的所有元素必可排成一列 $a_{1}, a_{2}, \cdots, a_{n}$ 使:

$1^{\circ}$ 存在 $j \in\{1,2, \cdots, n\}$, 使得 $a_{1}<a_{2}<\cdots<a_{j}, a_{j}>a_{j+1}>\cdots>a_{n}$.

$2^{\circ}$ 对 $a<b \in S$, 如果 $a, b$ 在排列中相邻, 则 $f(a, b)$ 与 $a$ 不相邻.

引理的证明:

$n=3$ 时, 把最大数放中间即可.

设命题对小于 $n$ 时成立, 考虑 $n$ 时.

设 $S$ 最小的 2 个元素为 $p<q$, 令 $S^{\prime}=S \backslash\{p\}$.

对 $S^{\prime}$ 中任意两个不同元素, 定义 $g(a, b)=\left\{\begin{array}{ll}q, & \text { 如果 } f(a, b)=p, \\ f(a, b), & \text { 其余情况 }\end{array}\right.$.

就有 $q \leq g(a, b) \leq a$ 对所有 $a, b \in S^{\prime}$ 成立.

由归纳假设, $S^{\prime}$ 的元素可以排成 $b_{1}, b_{2}, \cdots, b_{n-1}$, 满足 $1^{\circ}$ 和 $2^{\circ}$.

由 $1^{\circ}, b_{1}=q$ 或 $b_{n-1}=q$, 不妨假设 $b_{1}=q$. 由归纳假设, $g\left(b_{2}, b_{3}\right) \neq q$, 由 $g$的定义, $f\left(b_{2}, b_{3}\right) \neq p$ 或 $q$.

另一方面, $f\left(b_{n-1}, b_{n-2}\right)$ 与 $p, q$ 中至少一者不同, 设为 $r \in\{p, q\}$ 使得 $r \neq f\left(b_{n-1}, b_{n-2}\right)$. 考虑 $s=p+q-r$ 是 $\{p, q\}$ 中的另一元素. 我们可将 $S$ 的全部元素排为

$$
s, b_{2}, b_{3}, \cdots, b_{n-1}, r
$$

这就是一个满足 $1^{\circ}$ 与 $2^{\circ}$ 的排列.

综上, 引理成立.

注: 加强归纳可能有多种方法, 笔者给出了两种. 解法 2 表明了只要 $S$ 中最大元素不是 $S$ 中其他 2 个元素之和, 待证结论就正确.

