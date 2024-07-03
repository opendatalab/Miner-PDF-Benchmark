数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2021 北大金秋营一道代数题的最优系数 

陈博文

(北京大学, 100871)

本文给出 2021 年北大金秋营第二天代数题的解答, 并且给出了该题目的最优系数. 首先给出题目如下:

问题 1 设

$$
a=x^{2}(y-z)^{4}, b=y^{2}(z-x)^{4}, c=z^{2}(x-y)^{4}(x, y, z \geq 0),
$$

求证:

$$
(a+b+c)^{3} \geq 4.5(a \sqrt{b}+b \sqrt{c}+c \sqrt{a})^{2} .
$$

研究发现这里的最优系数不是 4.5 , 而是 6.48 . 笔者首先使用计算机猜出结果, 然后在初等数学的框架内给出了求出并证明 6.48 的方法.

通过和同学的讨论, 笔者得知了这个题目广为流传的一个解法. 将原题解答简略记录如下:

证明 为了消除题面中的根号, 轮换对称地令

$$
\left\{\begin{array}{l}
m=x(y-z)^{2} \\
n=y(z-x)^{2} \\
k=z(x-y)^{2}
\end{array}\right.
$$

则 $m, n, k \geq 0$, 且

$$
a=m^{2}, b=n^{2}, c=k^{2} .
$$

待证不等式化为

$$
\left(\sum m^{2}\right)^{3} \geq 4.5\left(\sum m^{2} n\right)^{2}
$$

Email: 1900010671@pku.edu.cn.

修订日期: 2022-03-01.
首先, 我们宣称如下的不等式成立:

$$
2 \sum m^{2} \geq\left(\sum m\right)^{2}
$$

这个不等式的证明方法很多. 由于不是文章的主体部分, 故一笔带过: 直接代入 $x, y, z$ 展开, 通过并不复杂的计算配成平方式:

$$
2 \sum m^{2}-\left(\sum m\right)^{2}=\prod(x-y)^{2} \geq 0 \text {. }
$$

现在, 把目光转回到(1). 尝试放缩:

$$
L H S \stackrel{(2)}{\geq}\left(\sum m^{2}\right)^{2}\left(\left(\sum m\right)^{2} / 2\right)
$$

注意到, $L H S$ 这一步放缩之后, 和 $R H S$ 都是平方的形式, 所以可以同时开方.这把我们带到了第二步. 下面只需证:

$$
\left(\sum m^{2}\right)\left(\sum m\right) \geq 3\left(\sum m^{2} n\right)
$$

这个不等式的次数已经很低 (3 次), 只需要展开观察系数, 就可以发现配成完全平方:

$$
\left(\sum m^{2}\right)\left(\sum m\right)-3\left(\sum m^{2} n\right)=\sum m(m-n)^{2} \geq 0
$$

证毕.

下面尝试对第二步加以改进(为了展现思考过程, 方便读者理解和学习计算方法, 这部分的计算会相对详细地写出). 事先不知道最优系数, 所以只能待定.考虑如下问题:

问题 2 已知

$$
2 \sum m^{2} \geq\left(\sum m\right)^{2} \quad(m, n, k \geq 0)
$$

求 $\lambda$ 的最大值, 使得

$$
\left(\sum m^{2}\right)\left(\sum m\right) \geq \lambda\left(\sum m^{2} n\right)
$$

恒成立。

既然已经证明了 $\lambda=3$ 成立, 接下来要考虑的就只有 $\lambda>3$ 的情形. 令

$$
F=F_{\lambda}(m, n, k)=\left(\sum m^{2}\right)\left(\sum m\right)-\lambda\left(\sum m^{2} n\right),
$$

对每个固定的 $\lambda$, 需要判定 $F \geq 0$ 是否恒成立.

首先, 可以对 $(m, n, k)$ 进行调整来缩减需要考虑的情况个数. 我们采用的调整方式是三者同时加上一个相等的数.
令

$$
f(d)=F(m+d, n+d, k+d),
$$

先求 $f$ 的定义域. 首先它包含 $d=0$ (因为调整前的 $m, n, k$ 满足条件), 从而不是空集.

$$
\left\{\begin{array}{l}
2 \sum(m+d)^{2} \geq\left(3 d+\sum m\right)^{2} \\
m+d \geq 0 \\
n+d \geq 0 \\
k+d \geq 0
\end{array}\right.
$$

第一个不等式形如 $3 d^{2}+A d+B \leq 0$, 解集为有限闭区间, 而后三个不等式解集是无穷闭区间, 故交集为有限闭区间.

$f(d)$ 是三次函数:

$$
f(d)=(9-3 \lambda) d^{3}+\left(\sum m\right)(9-3 \lambda) d^{2}+\cdots,
$$

因为 $3-\lambda<0, \sum(m+d) \geq 0$, 所以

$$
f^{\prime \prime}(d)=6(3-\lambda)\left(\sum(m+d)\right) \leq 0 .
$$

这样, $f$ 的最小值必然在端点取到. 通过调整把 $(m, n, k)$ 变成两个对应端点中的一个, $F$ 的值不增. 这个端点对应边界 $m, n, k$ 中至少一个为 0 , 或者 $\left.2 \sum m^{2}=\left(\sum m\right)^{2}\right)$.

接下来, 只需在边界上验证原不等式.

先考虑 $2 \sum m^{2}=\left(\sum m\right)^{2}$ 的情形. 沿用三元对称多项式的常用记号, 设

$$
\left\{\begin{array}{l}
p=m+n+k \\
q=m n+n k+k m \\
r=m n k
\end{array}\right.
$$

由齐次性不妨设 $p=2$, 则 $q=1$. 对 $r$ 的约束条件是: 一元三次方程

$$
t^{3}-2 t^{2}+t-r=0
$$

有三个非负实根 (允许重根). 通过画出图像 (这里略去) 得: $r \in\left[0, \frac{4}{27}\right]$. 代入 $F$的表达式:

$$
F \geq 0 \Leftrightarrow 4 \geq \lambda\left(\sum m^{2} n\right) \Leftrightarrow \lambda \leq 4 /\left(\sum m^{2} n\right)_{\max }
$$

令 $s=\sum m^{2} n$, 因为它是轮换不对称的三元多项式, 故设出对偶式 $t=\sum m n^{2}$.
显见

$$
s+t=\sum\left(m^{2} n+m n^{2}\right)=p q-3 r=2-3 r .
$$

而

$$
s-t=(m-n)(n-k)(m-k) \text {. }
$$

这是熟知的因式分解: 如果令 $m=n$, 则 $s-t=0$, 从而由多项式的因式定理, $s-t$ 含有因式 $m-n$. 由轮换对称性知还含有 $n-k, m-k$, 通过比较系数知前面的常数为 1 .

它平方之后就是轮换对称式, 可以方便处理：

$$
\begin{aligned}
(s-t)^{2} & =\prod(m-n)^{2} \\
& =\prod\left((m+n)^{2}-4 m n\right) \\
& =\prod\left((p-k)^{2}-4(q-k(m+n))\right) \\
& =\prod\left((p-k)^{2}-4(q-k(p-k))\right) \\
& =\prod(k(4-3 k)) \\
& =r(-27 r+4) .
\end{aligned}
$$

于是

$$
s=\frac{2-3 r+\sqrt{r(4-27 r)}}{2}
$$

$r \in\left[0, \frac{4}{27}\right] \Rightarrow s_{\max }=\left.s\right|_{r=\frac{1}{27}}=\frac{10}{9}$. 从而 $\lambda$ 的最优值为 3.6.

另外一个边界: 不妨设 $m=0$. 不等式较松, 可以通过简单放缩证明:

$$
\begin{aligned}
F_{3.6}(0, n, k) & =(n+k)\left(n^{2}+k^{2}\right)-3.6 n^{2} k \\
& =\left(n^{3} / 8+n^{3} / 8+k^{3}\right)+\left(n k^{2}+\frac{3}{4} n^{3}\right)-2.6 n^{2} k \\
& \geq \frac{3}{2} n^{2} k+\sqrt{3} n^{2} k-2.6 n^{2} k \\
& \geq 0 .
\end{aligned}
$$

这样, 对原题有

$$
\begin{aligned}
\left(\sum m^{2}\right)^{3} & \geq\left(\sum m^{2}\right)^{2} \cdot\left(\sum m\right)^{2} / 2 \\
& \geq 3.6^{2}\left(\sum m^{2} n\right)^{2} / 2 \\
& \geq 6.48\left(\sum m^{2} n\right)^{2} .
\end{aligned}
$$

下面讨论该系数是否已经是最优的.

熟知: 证明系数最优性的方式是寻求取等条件. 根据上面的过程, 设
$m_{0}>n_{0}>k_{0}$ 为 $t^{3}-2 t^{2}+t-\frac{1}{27}=0$ 的三根, 则

$$
2 \sum m_{0}^{2}=\left(\sum m_{0}\right)^{2}, \sum m_{0}^{2} n_{0}=\frac{10}{9}
$$

但遗憾的是, 第一个条件阻止了我们寻找到相应的 $x, y, z$. 这是因为:

$$
2 \sum m_{0}^{2}-\left(\sum m_{0}\right)^{2}=\prod(x-y)^{2}
$$

欲其成立, 必须 $x, y, z$ 中有两个相等. 但这样 $m, n, k$ 中就至少一个为零.

我们不会止步于此. 上面的分析已经提示我们在 $x=y=z$ 附近寻找. 也就是说, 考虑

$$
\left\{\begin{array}{l}
x=A(\epsilon) \cdot(1+\mu \epsilon) \\
y=A(\epsilon) \cdot(1+\nu \epsilon) \\
z=A(\epsilon) \cdot 1
\end{array}\right.
$$

待定系数知, 取

$$
\left\{\begin{array}{l}
x=\epsilon^{-\frac{2}{3}} \cdot 1 \\
y=\epsilon^{-\frac{2}{3}} \cdot\left(1-\sqrt{k_{0}} \epsilon\right) \\
z=\epsilon^{-\frac{2}{3}} \cdot\left(1+\sqrt{n_{0}} \epsilon\right)
\end{array}\right.
$$

时, 就有

$$
\left(x(y-z)^{2}, y(z-x)^{2}, z(x-y)^{2}\right) \rightarrow\left(m_{0}, n_{0}, k_{0}\right), \epsilon \rightarrow 0^{+} .
$$

至此, 最优系数已经确定为 6.48 .

注 1 有的读者可能已经发现, 上面所有放缩只依赖于不等式

$$
2 \sum m^{2} \geq\left(\sum m\right)^{2}
$$

而没有使用 $m, n, k$ 关于 $x, y, z$ 的具体表达式. 如果该读者碰巧在细心之外具有谨慎的特点, 就难免为此怀疑.

一般来说, 在考场上如果我们使用题目条件推出一个“更弱”的不等式, 并全程使用后者尝试证明结论, 往往会担心证不出来. 请看下面的例子:

假如有一道题: “已知 $a>\pi$, 求证 $f(a)>0$ ( $f$ 是给定的函数)." 小明为了计算简单起见, 尝试证明: “已知 $a>3$, 则 $f(a)>0$. "诚然 $a>\pi \Rightarrow a>3$, 如果这样能证出来, 自然没有逻辑错误. 但我们未免为小明担心, 它尝试证明的结论可能是错的: 如果 $f(3.05)<0$ 怎么办?

但这道题中, 这种后顾之忧是不存在的. 我们使用的其实是等价的命题! 也
就是说:

$$
\begin{aligned}
& 2 \sum m^{2}>\left(\sum m\right)^{2}, m>0, n>0, k>0 \\
& \Longrightarrow \exists x \geq 0, y \geq 0, z \geq 0, \text { s.t. }\left\{\begin{array}{l}
m=x(y-z)^{2} \\
n=y(z-x)^{2} \\
k=z(x-y)^{2}
\end{array}\right.
\end{aligned}
$$

这个结论可以使用数学分析工具加以解决：局部利用反函数定理, 然后加以延拓.

注 2 上述过程足够初等, 并且不用事先知道 6.48 这个数. 但如果没有 mathematica 辅助排除错误的猜想, 指明正确的道路, 是很难一步一步走下来的.因此, 单枪匹马使用纸笔做过类似尝试但失败的同学无需沮丧.

首先笔者通过数值计算给出值和取等条件, 确定最优值是有理数 (这已经很稀有了, 因为它很可能是一个乏味的无理数), 并且确定取等条件是 $x=y=z$ 附近.

其次, 利用 mathematica 验证其中一步放缩的正确性, 并给出其取等条件.验证了在

$$
2 \sum m^{2} \geq\left(\sum m\right)^{2} \quad(m, n, k \geq 0)
$$

条件下, 不等式

$$
\left(\sum m^{2}\right)\left(\sum m\right) \geq 3.6\left(\sum m^{2} n\right)
$$

是正确的, 并且取等条件是某个整系数三次方程的三个无理根(这提示我们考虑 $(p, q, r))$.

在上述的过程中, 利用 mathematica 协助计算, 这减轻了探索失误所需承受的代价, 实质上鼓励了更多尝试和探索.

注 3 由于笔者水平有限, 对于上述证明过程中自然生发出的一些问题, 自己却不能解决, 故在这里抛砖引玉, 供有兴趣的读者进一步研究之用.

1. 如何使用初等方法证明 5.1中的结论?
2. 如何不用条件 $2 \sum m^{2} \geq\left(\sum m\right)^{2}$, 而直接用原始条件(关于 $x, y, z$ 的表达式)来证明 $\left(\sum m^{2}\right)\left(\sum m\right) \geq 3.6\left(\sum m^{2} n\right)$ ?
