数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 一道新星征解题的简证 

黄嘉俊<br>(上海市上海中学, 200231)

新星问题征解第 28 期中的一道不等式题难度高且优美, 题目如下:

问题 已知 $x_{1} \geq x_{2} \geq \cdots \geq x_{n} \geq 0, y_{1} \geq y_{2} \geq \cdots \geq y_{n} \geq 0$, 且 $\sum_{i=1}^{n} x_{i}=$ $\sum_{i=1}^{n} y_{i}=n$, 证明:

$$
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right|<e^{\frac{n}{2}}
$$

(天津实验中学 解尧平 供题)

本短文给出上述问题的一个简洁的证明.

证明 我们用归纳法证明更强的命题:

则有

若 $x_{1} \geq x_{2} \geq \cdots \geq x_{n} \geq 0, y_{1} \geq y_{2} \geq \cdots \geq y_{n} \geq 0$, 且 $\sum_{i=1}^{n} x_{i} \leq A, \sum_{i=1}^{n} y_{i} \leq A$,

$$
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right|<\left(\frac{A}{n}\right)^{n} e^{\frac{n}{e}}
$$

我们对 $n$ 归纳.

当 $n=1$ 时, $(*)$ 成立.

设 $(*)$ 对小于 $n$ 的情形成立, 下证 $n$ 时的情形.

不妨设 $x_{n}>y_{n}$, 我们分两种情况.

1) 若 $x_{i}>y_{i}, \forall 1 \leq i \leq n$, 结合均值不等式知

$$
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right| \leq \prod_{i=1}^{n} x_{i} \leq\left(\frac{\sum_{i=1}^{n} x_{i}}{n}\right)^{n} \leq\left(\frac{A}{n}\right)^{n},
$$

得证.

2) 若存在 $1 \leq u \leq n-1$, 使得

$$
x_{n}>y_{n}, x_{n-1}>y_{n-1}, \cdots, x_{u+1}>y_{u+1} \text {, 但 } x_{u}<y_{u} \text {. }
$$

修订日期: 2019-03-03.
此时有

$$
\sum_{i=1}^{u}\left(x_{i}-x_{u}\right) \leq A-u x_{u}, \quad \sum_{i=1}^{u}\left(y_{i}-x_{u}\right) \leq A-u x_{u},
$$

且 $x_{i} \geq x_{u}, y_{i} \geq y_{u}, \forall 1 \leq i \leq u$. 故由归纳假设知,

另一方面，

$$
\prod_{i=1}^{u}\left|x_{i}-y_{i}\right| \leq\left(\frac{A-u x_{u}}{u}\right)^{u} e^{\frac{u}{e}}
$$

$$
\prod_{i=u+1}^{n}\left|x_{i}-y_{i}\right|=\prod_{i=u+1}^{n}\left(x_{i}-y_{i}\right) \leq \prod_{i=u+1}^{n} x_{i} \leq k^{n-u}
$$

其中 $k=\frac{\sum_{i=u+1}^{n} x_{i}}{n-u}$. 故要证 $(*)$, 只需证

$$
\left(\frac{A-u x_{u}}{u}\right)^{u} e^{\frac{u}{e}} k^{n-u} \leq\left(\frac{A}{n}\right)^{n} e^{\frac{n}{e}} .
$$

由 $x_{i}(1 \leq i \leq n)$ 的单调性知, $x_{u} \geq k, \frac{A}{n} \geq k$, 故只需证

$$
\left(\frac{A-u k}{u}\right)^{u} k^{n-u} \leq\left(\frac{A}{n}\right)^{n} e^{\frac{n-u}{e}} .
$$

记 $f(x)=x^{n-u}\left(\frac{A-u x}{u}\right)^{u}$, 则

$$
\begin{aligned}
f^{\prime}(x) & =(n-u) x^{n-u-1}\left(\frac{A-u x}{u}\right)^{u}-u x^{n-u}\left(\frac{A-u x}{u}\right)^{u-1} \\
& =x^{n-u-1}\left(\frac{A-u x}{u}\right)^{u-1}\left((n-u) \frac{A-u x}{u}-u x\right) \\
& =x^{n-u-1}\left(\frac{A-u x}{u}\right)^{u-1}\left((n-u) \frac{A}{u}-n x\right),
\end{aligned}
$$

故 $f$ 在 $\left[0, \frac{(n-u) A}{n u}\right]$ 单调递增, 在 $\left[\frac{(n-u) A}{n u}, \frac{A}{u}\right]$ 上单调递减.

对 $u$ 分两种情况.

i) 若 $n \leq 2 u$, 则 $\frac{(n-u) A}{n u} \leq \frac{A}{n}$, 从而

$$
f(k) \leq f\left(\frac{(n-u) A}{n u}\right)=\left(\frac{A}{n}\right)^{u}\left(\frac{(n-u) A}{n u}\right)^{n-u} \leq\left(\frac{A}{n}\right)^{u}\left(\frac{A}{n}\right)^{n-u}=\left(\frac{A}{n}\right)^{n}
$$

注意到 $e^{\frac{n-u}{e}}>1$, 从而 $(* *)$ 成立.

ii) 若 $n>2 u$, 则 $\frac{A}{n}<\frac{(n-u) A}{n u}$, 从而

$$
f(k) \leq f\left(\frac{A}{n}\right)=\left(\frac{A}{n}\right)^{n-u}\left(\frac{(n-u) A}{u n}\right)^{u}=\left(\frac{A}{n}\right)^{n}\left(\frac{n-u}{u}\right)^{u} .
$$

对 $f(x)=e^{\frac{1}{x} \ln x}$ 求导分析单调性便知, $x^{\frac{1}{x}} \leq e^{\frac{1}{e}}, \forall x>0$, 取 $t=\frac{n-u}{u}$ 便得

结合 (1) 知, 此时 $(* *)$ 成立.

$$
\left(\frac{n-u}{u}\right)^{\left(\frac{u}{n-u}\right)} \leq e^{\frac{1}{e}} \Leftrightarrow\left(\frac{n-u}{u}\right)^{u} \leq e^{\frac{n-u}{e}},
$$

结合 1), 2) 知 (*) 成立, 于是命题得证.

致谢作者感谢王广廷老师的指导!

