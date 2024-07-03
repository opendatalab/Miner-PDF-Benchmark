# Figalli 不等式的最优系数 

黄嘉俊

(上海市上海中学, 200231)

2018 菲尔茨奖得主 Figalli 在文 [1] 中, 利用分析方法建立了下述不等式:

定理 1 设实数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 满足 $0<\lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{n}$. 记

$$
\lambda_{A}=\frac{1}{n} \sum_{k=1}^{n} \lambda_{k}, \lambda_{G}=\left(\prod_{k=1}^{n} \lambda_{k}\right)^{\frac{1}{n}},
$$

则

$$
7 n^{2}\left(\lambda_{A}-\lambda_{G}\right) \geq \frac{1}{\lambda_{n}} \sum_{k=1}^{n}\left(\lambda_{k}-\lambda_{G}\right)^{2}
$$

罗横溢和胡子轩在文 [2] 中, 用初等方法证明了上述不等式, 并且将系数 $7 n^{2}$ 改进到了 $5 n-4$.

我们将系数改进到了 $2 n$, 并且这个系数是最佳的, 具体的, 我们证明了如下结果:

定理 2 设实数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 满足 $0<\lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{n}$. 记

$$
\lambda_{A}=\frac{1}{n} \sum_{k=1}^{n} \lambda_{k}, \lambda_{G}=\left(\prod_{k=1}^{n} \lambda_{k}\right)^{\frac{1}{n}},
$$

则

$$
2 n\left(\lambda_{A}-\lambda_{G}\right) \geq \frac{1}{\lambda_{n}} \sum_{k=1}^{n}\left(\lambda_{k}-\lambda_{G}\right)^{2}
$$

且 $2 n$ 是最优的系数.

证明 我们先证明一个引理:

引理 设 $c \geq 1$, 则对任意 $x \in(0, c]$, 均有

$$
2 c(x-\ln x-1) \geq(x-1)^{2} .
$$

修订日期: 2018-12-28.
引理的证明 我们分两种情况证明.

若 $x \geq 1$, 则由 $x \leq c$ 知, 要证 $(2)$, 只需证

$$
2 x-2 \ln x-2 \geq x-2+\frac{1}{x}
$$

这等价于

$$
x-\frac{1}{x}-2 \ln x \geq 0
$$

令 $f(x)=x-\frac{1}{x}-2 \ln x$, 则 $f^{\prime}(x)=1+\frac{1}{x^{2}}-\frac{2}{x} \geq 0$. 故 $f(x) \geq f(1)=0$, 此时命题成立.

若 $0<x<1$, 由于 $c \geq 1$, 故要证 $(2)$, 只需证

$$
2 x-2 \ln x-2 \geq x^{2}-2 x+1 \text {. }
$$

令 $f(x)=-x^{2}+4 x-3-2 \ln x$, 则 $f^{\prime}(x)=-2 x+4-\frac{2}{x} \leq 0$, 故 $f(x) \geq f(1)=0$.此时命题成立.

综上知引理成立.

回到原题. 注意到 (1) 是齐次的, 故不妨设 $\lambda_{G}=1$, 即 $\lambda_{1} \lambda_{2} \cdots \lambda_{n}=1$. 则 (1)等价于

$$
2\left(\sum_{k=1}^{n} \lambda_{k}-n\right) \lambda_{n} \geq \sum_{k=1}^{n}\left(\lambda_{k}-1\right)^{2}
$$

注意到 $\sum_{k=1}^{n} \ln \lambda_{k}=0$, 上式等价于

$$
2 \sum_{k=1}^{n}\left(\lambda_{k}-\ln \lambda_{k}-1\right) \lambda_{n} \geq \sum_{k=1}^{n}\left(\lambda_{k}-1\right)^{2}
$$

从而只需证明局部不等式:

$$
2\left(\lambda_{k}-\ln \lambda_{k}-1\right) \lambda_{n} \geq\left(\lambda_{k}-1\right)^{2}
$$

由 $\lambda_{n}$ 的最大性和 $\lambda_{1} \lambda_{2} \cdots \lambda_{n}=1$ 知 $\lambda_{n} \geq 1$, 结合引理知, 上述局部不等式成立.从而 (1) 式成立.

下面说明系数 $2 n$ 是最优的.

设最优系数为 $c$.

取 $\lambda_{n}=x^{n}(x>1), \lambda_{1}=\lambda_{2}=\cdots=\lambda_{n-1}=1$, 则 $\lambda_{A}=\frac{x^{n}+n-1}{n}, \lambda_{G}=x$. 从而

$$
c \cdot \frac{x^{n}-n x+n-1}{n} \cdot x^{n} \geq(1-x)^{2}(n-1)+\left(x^{n}-x\right)^{2} \text {, }
$$

$$
\begin{aligned}
& \Rightarrow c \cdot \frac{x^{n}(x-1)^{2}\left(x^{n-2}+2 x^{n-3}+\cdots+n-1\right)}{n} \\
& \quad \geq(x-1)^{2}\left(n-1+\left(x^{n-1}+x^{n-2}+\cdots+x\right)^{2}\right)
\end{aligned}
$$

当 $n \geq 2$ 时, 令 $x \rightarrow 1^{+}$得

$$
c \cdot \frac{\frac{n(n-1)}{2}}{n} \geq n-1+(n-1)^{2}=n(n-1) \text {, }
$$

即 $c \geq 2 n$.

综上知定理成立.

致谢 作者感谢王广廷老师的指导!

## 参考文献

[1] Figalli, A.; Maggi, F.; Pratelli, A. A mass transportation approach to quantitative isoperimetric inequalities. Invent. Math. 182 (2010), no. 1, 167 - 211.

[2] 罗横溢, 胡子轩. Figalli不等式的初等证明 [J]. 数学新星网. 学生专栏, 2018-12-13 期.

