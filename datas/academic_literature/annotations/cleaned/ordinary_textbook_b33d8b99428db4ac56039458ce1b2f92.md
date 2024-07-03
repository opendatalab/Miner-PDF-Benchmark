# 关于正齐次不等式 

## 冷岗松

什么样子的不等式叫做齐次不等式呢?

我们引用 Hardy 等人 [1] 的一句话作为回答: 如果一个不等式的两边都是某些变量组的同次齐次函数, 则称这个不等式是齐次不等式.

或许有人进一步问: 什么是齐次函数呢? 回答是: 如果函数 $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$满足对任意因子 $\lambda$, 存在实数 $k$ 使得

$$
f\left(\lambda x_{1}, \lambda x_{2}, \cdots, \lambda x_{n}\right)=\lambda^{k} f\left(x_{1}, x_{2}, \cdots, x_{n}\right),
$$

则称这个函数 $f$ 是关于变量 $x_{1}, x_{2}, \cdots, x_{n}$ 的 $k$ 次齐次函数.

中学里见的最多的是这样一类齐次不等式: 将关于非负变元 (正变元) $x_{1}, x_{2}$, $\cdots, x_{n}$ 的不等式中的所有变元 $x_{i}$ 都换为 $\alpha x_{i}$ (其中 $\alpha$ 为任意正数), 而不等式不变. 我们称这一类不等式为正齐次不等式.

对于正齐次不等式, 我们常常可以对这些变量作 “正规化” 处理, 即对这些变量加上另外的限制, 而使证明简化. 这些处理方法我们称为齐次化分析.

下面举几个例子证明齐次化分析的应用.

例 1 (范数不等式): 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是非负实数, 若 $0<r<s$, 则

$$
\left(\sum_{i=1}^{n} a_{i}^{s}\right)^{\frac{1}{s}} \leq\left(\sum_{i=1}^{n} a_{i}^{r}\right)^{\frac{1}{r}}
$$

等号成立当且仅当 $a_{1}, a_{2}, \cdots, a_{n}$ 中至少有 $n-1$ 个为零.

证明: 注意到对任意正数 $\alpha$, 用 $\alpha a_{i}$ 替代 $a_{i}(i=1,2, \cdots, n)$, 不等式 (1) 不变.故 (1) 式是一个正齐次不等式. 不妨设

$$
\sum_{i=1}^{n} a_{i}^{r}=1
$$

因此, 要证明 (1) 式成立只须证

$$
\sum_{i=1}^{n} a_{i}^{s} \leq 1
$$

事实上, 由 (2) 式知 $a_{i}^{r} \leq 1$, 又由 $0<r<s$ 知

$$
a_{i}^{s}=\left(a_{i}^{r}\right)^{\frac{s}{r}} \leq\left(a_{i}^{r}\right)^{1}=a_{i}^{r}
$$

故

$$
\sum_{i=1}^{n} a_{i}^{s} \leq \sum_{i=1}^{n} a_{i}^{r}=1
$$

因此 (3) 式得证.

注: (1) 式为什么叫范数不等式呢? 这是因为对任何 $x=\left(x_{1}, x_{2}, \cdots, x_{n}\right) \in$ $\mathbf{R}^{n}, x$ 的 $p$ 范数可定义为

$$
\|x\|_{p}=\left(\sum_{i=1}^{n}\left|x_{i}\right|^{p}\right)^{\frac{1}{p}}
$$

当 $p \geq 1$ 时, $\|x\|_{p}$ 就是通常意义下的范数; 上述不等式 (1) 就说明当 $p>0$ 时, $\|x\|_{p}$是 $p$ 的减函数.

下面的例 2 是著名的 Kantorovich 不等式 (俗称反向 Cauchy 不等式). 这里给出的证明选自 Pták [2] 发表在美国数学月刊上的一篇短文.

例 2 (Kantorovich 不等式): 设实数 $0<x_{1}<x_{2}<\cdots<x_{n}, \lambda_{1}, \lambda_{2}, \cdots, \lambda_{n} \geq$ 0 , 且 $\sum_{i=1}^{n} \lambda_{i}=1$, 则

$$
\left(\sum_{i=1}^{n} \lambda_{i} x_{i}\right)\left(\sum_{i=1}^{n} \lambda_{i} x_{i}^{-1}\right) \leq A^{2} G^{-2},
$$

其中 $A=\frac{1}{2}\left(x_{1}+x_{n}\right), G=\left(x_{1} x_{n}\right)^{\frac{1}{2}}$.

证明: 注意到不等式是齐次的, 即将 $x_{i}$ 换为 $\alpha x_{i}$ (其中 $\left.\alpha>0, i=1,2, \cdots, n\right)$,不等式不变. 因此, 不妨设 $G=1$, 这样便有 $x_{n}=\frac{1}{x_{1}}$. 故对任何 $x \in\left[x_{1}, x_{n}\right]=$ $\left[x_{1}, \frac{1}{x_{1}}\right]$ 有

$$
x+\frac{1}{x} \leq x_{1}+\frac{1}{x_{1}} .
$$

由此知

$$
\sum_{i=1}^{n} \lambda_{i} x_{i}+\sum_{i=1}^{n} \lambda_{i} x_{i}^{-1}=\sum_{i=1}^{n} \lambda_{i}\left(x_{i}+\frac{1}{x_{i}}\right) \leq x_{1}+\frac{1}{x_{1}}=2 A
$$

再对上式左边用算术-几何平均值不等式便立得 (4) 式.

下面的例 3 是著名的 Carleman 不等式的一个加强, 它是 Holland 发表在 [3]中的结果. 所谓的 Carleman 不等式是指: 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是非负实数, 则

$$
\sum_{i=1}^{n} \sqrt[i]{a_{1} a_{2} \cdots a_{i}}<e \sum_{i=1}^{n} a_{i} .
$$

例 3 (2015年国家集训队选拔试题): 给定整数 $n \geq 2$, 设 $a_{1}, a_{2}, \cdots, a_{n}$ 为正实数, 证明:

$$
\left(\frac{\sum_{j=1}^{n} \sqrt[j]{a_{1} a_{2} \cdots a_{j}}}{\sum_{j=1}^{n} a_{j}}\right)^{\frac{1}{n}}+\frac{\sqrt[n]{a_{1} a_{2} \cdots a_{n}}}{\sum_{j=1}^{n} \sqrt[j]{a_{1} a_{2} \cdots a_{j}}} \leq \frac{n+1}{n}
$$

证明: 记 $\sqrt[j]{a_{1} a_{2} \cdots a_{j}}=x_{j}(j=1,2, \cdots, n)$, 并令 $x_{0}=1$, 则

$$
a_{j}=\frac{x_{j}^{j}}{x_{j-1}^{j-1}}, j=1,2, \cdots, n .
$$

由于不等式 (6) 左边关于 $a_{1}, a_{2}, \cdots, a_{n}$ 是齐次的, 故不妨设

$$
\sum_{j=1}^{n} x_{j}=\sum_{j=1}^{n} \sqrt[j]{a_{1} a_{2} \cdots a_{j}}=1 .
$$

这时, 原不等式 (6) 等价于

$$
\left(\sum_{j=1}^{n} \frac{x_{j}^{j}}{x_{j-1}^{j-1}}\right)^{-\frac{1}{n}}+x_{n} \leq \frac{n+1}{n}
$$

下证 (7) 式:

易知函数 $f(x)=x^{-\frac{1}{n}}$ 在 $(0,+\infty)$ 上是凸函数, 故

$$
\begin{aligned}
\left(\sum_{j=1}^{n} \frac{x_{j}^{j}}{x_{j-1}^{j-1}}\right)^{-\frac{1}{n}} & =\left(\sum_{j=1}^{n} x_{j} \cdot \frac{x_{j}^{j-1}}{x_{j-1}^{j-1}}\right)^{-\frac{1}{n}} \\
& \leq \sum_{j=1}^{n} x_{j}\left(\frac{x_{j}^{j-1}}{x_{j-1}^{j-1}}\right)^{-\frac{1}{n}}(\text { 加权 Jensen 不等式 }) \\
& =\sum_{j=1}^{n}\left(x_{j-1}\right)^{\frac{j-1}{n}}\left(x_{j}\right)^{1-\frac{j-1}{n}} \\
& \leq \sum_{j=1}^{n}\left(\frac{j-1}{n} x_{j-1}+\left(1-\frac{j-1}{n}\right) x_{j}\right)(\text { 加权均值不等式 }) \\
& =\frac{n+1}{n} \sum_{j=1}^{n} x_{j}+\sum_{j=1}^{n}\left(\frac{j-1}{n} x_{j-1}-\frac{j}{n} x_{j}\right) \\
& =\frac{n+1}{n}-x_{n} .
\end{aligned}
$$

这就是 (7) 式, 证毕.

最后, 请同学们考虑一下, 为什么 (6) 式是 Carleman 不等式 (5) 式的加强?
对齐次不等式的正规化处理, 大多数情况下仅限于正不等式 (即非负变量的不等式). 对于实变量, 须谨慎. 看下例:

例 4: 设 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n} \in \mathbf{R}$, 令

$$
c_{i}=\left|a b_{i}+a_{i} b-a_{i} b_{i}\right|, i=1,2, \cdots, n
$$

其中 $a=\frac{1}{n} \sum_{i=1}^{n} a_{i}, b=\frac{1}{n} \sum_{i=1}^{n} b_{i}$, 证明:

$$
\left(\sum_{i=1}^{n} c_{i}\right)^{2} \leq\left(\sum_{i=1}^{n} a_{i}^{2}\right)\left(\sum_{i=1}^{n} b_{i}^{2}\right)
$$

2012 年我给中国国家集训队提供了一道测试题, 其实例 4 就是那道测试题的实数版本. 那道测试题是: 设 $x_{1}, x_{2}, \cdots, x_{n}, y_{1}, y_{2}, \cdots, y_{n}$ 均为模等于 1 的复数, 令

$$
z_{i}=x y_{i}+y x_{i}-x_{i} y_{i}, i=1,2, \cdots, n
$$

其中 $x=\frac{1}{n} \sum_{i=1}^{n} x_{i}, y=\frac{1}{n} \sum_{i=1}^{n} y_{i}$. 证明: $\sum_{i=1}^{n}\left|z_{i}\right| \leq n$.

例 4 的难度不高, 仅是全国联赛中等难度水平, 但有些同学在求解时却错误用了齐次性. 由于不等式关于 $a_{1}, a_{2}, \cdots, a_{n}$ 和 $b_{1}, b_{2}, \cdots, b_{n}$ 都是齐次的, 因此不妨设 $\sum_{i=1}^{n} a_{i}=1$ 及 $\sum_{i=1}^{n} b_{i}=1$, 在这些条件下证完了这个问题. 实际上, 这个问题中关键的是 $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} b_{i}=0$ 的情况.

下面的证明是优雅的.

例 4 的证明: 令 $x_{i}=a_{i}-a, y_{i}=b_{i}-b, i=1,2, \cdots, n$, 则

$$
\sum_{i=1}^{n} x_{i}=0, \quad \sum_{i=1}^{n} y_{i}=0
$$

因此,

$$
\begin{aligned}
c_{i} & =\left|a b_{i}+a_{i} b-a_{i} b_{i}\right| \\
& =\left|a\left(y_{i}+b\right)+\left(x_{i}+a\right) b-\left(x_{i}+a\right)\left(y_{i}+b\right)\right| \\
& =\left|a b-x_{i} y_{i}\right| \leq|a b|+\left|x_{i} y_{i}\right| .
\end{aligned}
$$

故由 Cauchy 不等式可得

$$
\begin{aligned}
\left(\sum_{i=1}^{n} c_{i}\right)^{2} & \leq\left(n|a b|+\sum_{i=1}^{n}\left|x_{i} y_{i}\right|\right)^{2} \\
& \leq\left(n|a|^{2}+\sum_{i=1}^{n}\left|x_{i}\right|^{2}\right)\left(n|b|^{2}+\sum_{i=1}^{n}\left|y_{i}\right|^{2}\right) \\
& =\left(\sum_{i=1}^{n}\left(a^{2}+2 a x_{i}+x_{i}^{2}\right)\right)\left(\sum_{i=1}^{n}\left(b^{2}+2 b y_{i}+y_{i}^{2}\right)\right) \\
& =\left(\sum_{i=1}^{n}\left(a+x_{i}\right)^{2}\right)\left(\sum_{i=1}^{n}\left(b+y_{i}\right)^{2}\right) \\
& =\left(\sum_{i=1}^{n} a_{i}^{2}\right)\left(\sum_{i=1}^{n} b_{i}^{2}\right) .
\end{aligned}
$$

注：其实上面的证法对复数情况也完全适用.

## 参 考 文 献

[1] G.H. Hardy, J.E. Littlewood, G. Pólya, 不等式 (第 2 版) 中译本 $[\mathrm{M}]$, 越民义译, 人民邮电出版社, 2008 .

[2] V. Pták, The Kantorovich inequality [J], Amer. Math. Monthly, 102 (1995), 820-821.

[3] F. Holland, A strengthening of the Carleman-Hardy-Pólya inequality [J], Proc. Amer. Math. Soc., 135 (2007), 2915-2920.

