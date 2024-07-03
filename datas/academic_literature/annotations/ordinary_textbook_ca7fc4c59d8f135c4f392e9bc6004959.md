# 一个 Hardy 型不等式的证明 

牟晓生

(哈佛大学, xiaoshengmu@fas.harvard.edu)

最近, 山西大学附属中学王永喜老师证明了如下非常有意思的不等式:

$$
\sum_{k=1}^{n} \frac{k^{3}}{a_{1}^{3}+\cdots+a_{k}^{3}} \leq \frac{81}{32}\left(\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}\right)^{3} .
$$

其中 $a_{i}>0, i=1,2,3, \ldots, n$.

我们研究了这一不等式, 讨论了系数 $\frac{81}{32}$ 的最优性, 即考虑如下问题:

问题 设 $a_{i}>0, i=1,2,3, \ldots, n$, 则使不等式

$$
\sum_{k=1}^{n} \frac{k^{3}}{a_{1}^{3}+\cdots+a_{k}^{3}} \leq c \cdot\left(\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}\right)^{3}
$$

成立的最优常数 $c$ 为多少?

事实上, 我们将证明 $c=1$ 就够了. 注意到一定有 $c \geq 1$, 因此最优的常数就是 1 . 我们用归纳法证明下面更强的不等式:

$$
\sum_{k=1}^{n} \frac{k^{3}}{a_{1}^{3}+\cdots+a_{k}^{3}} \leq\left(\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}\right)^{3}-\frac{\lambda_{n}}{a_{1}^{3}+\cdots+a_{n}^{3}}, \forall n \geq 2
$$

其中 $\lambda_{n}>0$ 是只与 $n$ 有关的常数, 之后确定.

假设 (1) 式对 $n \geq 2$ 成立 (我们之后会回过头来检验 $n=2$ 的情况). 那么为证 $n+1$ 的情况, 只要证明

$$
\begin{aligned}
& \frac{\lambda_{n+1}+(n+1)^{3}}{a_{1}^{3}+\cdots+a_{n+1}^{3}} \\
\leq & \frac{\lambda_{n}}{a_{1}^{3}+\cdots+a_{n}^{3}}+\left[\left(\frac{1}{a_{1}}+\cdots+\frac{1}{a_{n+1}}\right)^{3}-\left(\frac{1}{a_{1}}+\cdots+\frac{1}{a_{n}}\right)^{3}\right] \\
= & \frac{\lambda_{n}}{a_{1}^{3}+\cdots+a_{n}^{3}}+\frac{3}{a_{n+1}}\left(\frac{1}{a_{1}}+\cdots+\frac{1}{a_{n}}\right)^{2}+\frac{3}{a_{n+1}^{2}}\left(\frac{1}{a_{1}}+\cdots+\frac{1}{a_{n}}\right)+\frac{1}{a_{n+1}^{3}} .
\end{aligned}
$$

收稿日期: 2016-05-12. 修订日期: 2016-09-28.
令 $S=a_{1}^{3}+\cdots+a_{n}^{3}$, 由 Hölder 不等式知

$$
\frac{1}{a_{1}}+\cdots+\frac{1}{a_{n}} \geq \frac{n^{\frac{4}{3}}}{S^{\frac{1}{3}}}
$$

代入到 $(2)$ 式, 只需证明

$$
\frac{\lambda_{n+1}+(n+1)^{3}}{S+a_{n+1}^{3}} \leq \frac{\lambda_{n}}{S}+\frac{3 n^{\frac{8}{3}}}{a_{n+1} S^{\frac{2}{3}}}+\frac{3 n^{\frac{4}{3}}}{a_{n+1}^{2} S^{\frac{1}{3}}}+\frac{1}{a_{n+1}^{3}} .
$$

令 $t=a_{n+1} / S^{\frac{1}{3}}$, 通分后等价于

$$
\lambda_{n+1}+(n+1)^{3} \leq \lambda_{n}+\left(\lambda_{n} t^{3}+\frac{3 n^{\frac{8}{3}}}{t}\right)+\left(3 n^{\frac{8}{3}} t^{2}+\frac{3 n^{\frac{4}{3}}}{t^{2}}\right)+\left(3 n^{\frac{4}{3}} t+\frac{1}{t^{3}}\right)+1
$$

由均值不等式可得

$$
\begin{gathered}
\lambda_{n} t^{3}+\frac{3 n^{\frac{8}{3}}}{t} \geq 4 \lambda_{n}^{\frac{1}{4}} n^{2} \\
3 n^{\frac{8}{3}} t^{2}+\frac{3 n^{\frac{4}{3}}}{t^{2}} \geq 6 n^{2} \\
3 n^{\frac{4}{3}} t+\frac{1}{t^{3}} \geq 4 n .
\end{gathered}
$$

将这些代入到 (3) 式, 只要验证

$$
\lambda_{n+1}+(n+1)^{3} \leq \lambda_{n}+4 \lambda_{n}^{\frac{1}{4}} n^{2}+6 n^{2}+4 n+1, \quad \forall n \geq 2
$$

现在令 $\lambda_{n}=\frac{1}{16} n^{4}$, 那么 (4) 式变成

$$
\frac{3}{4} n^{3}+\frac{21}{8} n^{2}+\frac{3}{4} n-\frac{1}{16} \geq 0
$$

显然对 $n \geq 2$ 成立.

最后考虑 $n=2$. 此时 $\lambda_{n}=1$, 也即要证:

$$
\frac{1}{a_{1}^{3}}+\frac{8}{a_{1}^{3}+a_{2}^{3}} \leq\left(\frac{1}{a_{1}}+\frac{1}{a_{2}}\right)^{3}-\frac{1}{a_{1}^{3}+a_{2}^{3}} .
$$

这是因为

$$
\frac{9}{a_{1}^{3}+a_{2}^{3}} \leq \frac{9}{a_{1}^{2} a_{2}+a_{2}^{2} a_{1}} \leq \frac{9}{4 a_{1}^{2} a_{2}}+\frac{9}{4 a_{2}^{2} a_{1}}<\frac{3}{a_{1}^{2} a_{2}}+\frac{3}{a_{2}^{2} a_{1}}
$$

因此命题得证!

注 用同样的方法可以证明经典的 Hardy 不等式: 对 $p>1$ 我们有

$$
\sum_{k=1}^{n}\left(\frac{a_{1}+\cdots+a_{k}}{k}\right)^{p} \leq\left(\frac{p}{p-1}\right)^{p} \sum_{k=1}^{n} a_{k}^{p}-\frac{p}{p-1} n^{-(p-1)}\left(a_{1}+\cdots+a_{n}\right)^{p} .
$$

如果令 $a_{k}=b_{k}^{\frac{1}{p}}$ 再使 $p \rightarrow \infty$, 则得到 Carleman 不等式:

$$
\sum_{k=1}^{n}\left(b_{1} b_{2} \cdots b_{k}\right)^{\frac{1}{k}} \leq e \sum_{k=1}^{n} b_{k}-n\left(b_{1} b_{2} \cdots b_{n}\right)^{\frac{1}{n}}
$$

实际上 (5) 式对所有 $p<0$ 也成立. 特别地, 当 $p=-1$ 时有

$$
\sum_{k=1}^{n} \frac{k}{a_{1}+\cdots+a_{k}} \leq 2 \sum_{k=1}^{n} \frac{1}{a_{k}}
$$

令 $a_{k}=k$ 可知上面的常数 2 是最佳的.

受到 (1) 式与 (7) 式的启发, 我们可以考虑更一般的问题

$$
\sum_{k=1}^{n} \frac{k^{\beta}}{a_{1}^{\beta}+\cdots+a_{k}^{\beta}} \leq c(\beta)\left(\sum_{k=1}^{n} \frac{1}{a_{k}}\right)^{\beta} .
$$

我们已经知道了最佳常数 $c(1)=2, c(3)=1$. 实际上也有 $c(2)=1$ : 可以归纳证明对 $n \geq 2$ 有

$$
\sum_{k=1}^{n} \frac{k^{2}}{a_{1}^{2}+\cdots+a_{k}^{2}} \leq\left(\sum_{k=1}^{n} \frac{1}{a_{k}}\right)^{2}-\frac{1}{8} \cdot \frac{n^{3}}{a_{1}^{2}+\cdots+a_{n}^{2}} .
$$

用同样方法应该不难证明 $c(\beta)=1, \forall \beta \geq 2$. 然而确定 $c(\beta)$ 在区间 $(1,2)$ 上的值似乎很困难.

## 编者注:

山西大学附属中学王永喜老师也来信告诉编辑部, 他也得到了 $c(3)=1$ 的结果. 同时他还讨论证明了上述 Hardy 型不等式 (8), 得到常数 $c(m)$ 的一个估计: $c(m)=\frac{1}{m-1}\left(\frac{2 m}{m+1}\right)^{m+1}, m \geq 2$, 特此说明.[^0]


[^0]:    实际上 $\beta \geq 2-\epsilon$ 也足够了.

