# Cîrtoaje 不等式的最佳常数 

张盛桐

(上海市上海中学, 200231)

Vasile Cîrtoaje 在《Algebraic Inequalities》一书中证明了如下代数不等式:

定理 1 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且满足 $a_{1}+\cdots+a_{n}=n$, 则

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n \geq \frac{8(n-1)}{n^{2}}\left(1-a_{1} a_{2} \cdots a_{n}\right) .
$$

韩新录同学在文 [1] 中证明了如下结果:

定理 2 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且 $a_{1}+\cdots+a_{n}=n$, 则

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n \geq(2 \sqrt{2}-1)\left(1-a_{1} a_{2} \cdots a_{n}\right) .
$$

我们证明了下面一个更强的结果 (只需注意到 $1.846>2 \sqrt{2}-1$ ):

定理 3 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且 $a_{1}+\cdots+a_{n}=n$, 则

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n \geq \lambda\left(1-a_{1} a_{2} \cdots a_{n}\right)
$$

其中,

$$
\lambda=\inf _{b>0} \frac{(b-1)^{2}}{b} \frac{1}{1-b \mathrm{e}^{1-b}} \approx 1.846
$$

证明 对每个 $n$, 考虑函数

$$
F_{n}\left(a_{1}, a_{2}, a_{3}, \cdots, a_{n}\right)=\frac{1}{a_{1}}+\cdots+\frac{1}{a_{n}}-n-\lambda\left(1-a_{1} a_{2} \cdots a_{n}\right),
$$

其中 $a_{1}+\cdots+a_{n}=n, a_{i}>0$.

由文 [1] 中的证明可知: $F_{n}$ 取到最大值 $\alpha_{n}$ 时, $\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$ 仅有两种取值, 不妨设 $a_{n}$ 出现了 $u_{n}$ 次, $b_{n}$ 出现了 $v_{n}$ 次, 则有 $u_{n} \cdot a_{n}+v_{n} \cdot b_{n}=n$ 且 $u_{n}+v_{n}=n$.

修订日期: 2018-09-28.
注意到

$$
F_{n}\left(a_{1}, \cdots, a_{n}\right)=F_{n+1}\left(a_{1}, \cdots, a_{n}, 1\right)
$$

故 $\alpha_{n} \geq \alpha_{n+1}$.

我们只需证对任意 $n$, 有 $\alpha_{n} \geq 0$.

假设结论不成立, 则存在实数 $\varepsilon>0$ 使得当 $n$ 足够大时, $\alpha_{n}<-\varepsilon$.

不失一般性, 设 $a_{n}<1, b_{n}>1$. 令 $c_{n}=\frac{u_{n}}{n}, d_{n}=\frac{v_{n}}{n}$. 从而我们得到四元组序列 $\left(a_{n}, b_{n}, c_{n}, d_{n}\right), n=1,2, \cdots$, 且有,

$$
c_{n}=\frac{b_{n}-1}{b_{n}-a_{n}}, \quad d_{n}=\frac{1-a_{n}}{b_{n}-a_{n}} .
$$

代入到 $F_{n}$,

$$
n \frac{\left(1-a_{n}\right)\left(b_{n}-1\right)}{a_{n} b_{n}} \leq \lambda\left(1-e^{n\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right)}\right)-\varepsilon .
$$

由于 $a_{n}, c_{n}, d_{n} \in[0,1]$ 和聚点原理知, 存在四元组序列的子序列, 不妨仍记为 $\left(a_{n}, b_{n}, c_{n}, d_{n}\right), n=1,2, \cdots$, 使得 $a_{n}$ 收玫到某个 $a \in[0,1], c_{n}$ 收玫到某个 $c \in[0,1], d_{n}$ 收玫到某个 $d \in[0,1]$, 且 $b_{n}$ 收敛到某个 $b$ 或 $b_{n} \rightarrow+\infty$.

我们分四种情况证明:

(i) $\boldsymbol{b}_{n} \rightarrow \infty$ 时. 当 $n$ 足够大时, (1) 可化为

$$
n \frac{1-a_{n}}{a_{n}} \leq \lambda\left(1-e^{n\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right)}\right)-\varepsilon^{\prime}
$$

因此 $n \frac{1-a_{n}}{a_{n}}<\lambda$, 且 $n\left(1-a_{n}\right)<\lambda$. 注意到

$$
n d_{n}=v_{n} \geq 1
$$

将 $d_{n}=\frac{1-a_{n}}{b_{n}-a_{n}}$ 代入得

$$
n\left(1-a_{n}\right) \geq b_{n}-a_{n} .
$$

从而可得 $\lambda+1>\lambda+a_{n}>n\left(1-a_{n}\right)+a_{n}>b_{n}$, 与 $b_{n} \rightarrow \infty$ 矛盾.

(ii) $\boldsymbol{b}_{\boldsymbol{n}} \rightarrow \boldsymbol{b}>\boldsymbol{1}$ 时. (1) 可化为

$$
n \frac{\left(1-a_{n}\right)(b-1)}{a_{n} b} \leq\left(\lambda-\varepsilon^{\prime}\right)\left(1-e^{n\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right)}\right) .
$$

因此

$$
n \frac{1-a_{n}}{a_{n}}<\lambda \frac{b}{b-1} .
$$

从而 $\frac{1-a_{n}}{a_{n}} \rightarrow 0$,则 $a=1$.

进一步, 当 $n$ 足够大时,

$$
n\left(1-a_{n}\right)=v_{n}\left(b_{n}-a_{n}\right)<\lambda \frac{b}{b-1}
$$

其中 $v_{n} \in \mathbb{Z}$.

这意味着 $v_{n}$ 是有界的. 我们可以选取 $\left(a_{n}, b_{n}, c_{n}, d_{n}\right)$ 的一个子列, 使得 $v_{n}$恒为 $v$.

易知 $v \geq 1$. 因此 (以下 LHS 表示不等式左边, RHS 表示不等式右边)

$$
\text { LHS }=n \frac{\left(1-a_{n}\right)(b-1)}{a_{n} b}=v \frac{\left(b_{n}-a_{n}\right)(b-1)}{a_{n} b} \rightarrow v \frac{(b-1)^{2}}{b} \text {. }
$$

我们再计算 RHS:

$$
\begin{aligned}
c_{n} \ln a_{n}+d_{n} \ln b_{n} & =\frac{\left(b_{n}-1\right) \ln a_{n}+\left(1-a_{n}\right) \ln b_{n}}{b_{n}-a_{n}} \\
& =\left(1-a_{n}\right)\left(\frac{\ln b}{b-1}-1\right)+o\left(1-a_{n}\right), \\
n\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right) & =n\left(1-a_{n}\right)\left(\frac{\ln b}{b-1}-1\right)+o\left(n\left(1-a_{n}\right)\right) \\
& \rightarrow v(\ln b-b+1) .
\end{aligned}
$$

故

$$
\lambda-\varepsilon^{\prime} \geq \frac{v(b-1)^{2}}{b\left(1-e^{v(\ln b+1-b)}\right)} \geq \frac{(b-1)^{2}}{b\left(1-e^{\ln b+1-b}\right)}
$$

这与 $\lambda$ 的定义矛盾.

(iii) $b_{n} \rightarrow 1$ 且 $a<1$ 时,

与情形 2 的证明类似, 我们同样可以得到结论.

(iv) $b_{n} \rightarrow 1$ 且 $a_{n} \rightarrow 1$ 时,

利用不等式 $1-e^{x} \leq-x$, 我们有, 当 $n$ 足够大时,

$$
n\left(1-a_{n}\right)\left(b_{n}-1\right) \leq\left(\lambda-\varepsilon^{\prime}\right)\left(-n\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right)\right)
$$

即

$$
\left(1-a_{n}\right)\left(b_{n}-1\right) \leq\left(\lambda-\varepsilon^{\prime}\right)\left(-\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right)\right)
$$

对 $\ln (1-x)$ 进行 Taylor 展开得:

$$
\begin{aligned}
-\left(c_{n} \ln a_{n}+d_{n} \ln b_{n}\right)= & \frac{\left(b_{n}-1\right)\left(\left(1-a_{n}\right)+\left(1-a_{n}\right)^{2} / 2+o\left(1-a_{n}\right)^{2}\right)}{b_{n}-a_{n}} \\
& +\frac{\left(1-a_{n}\right)\left(\left(1-b_{n}\right)+\left(1-b_{n}\right)^{2} / 2+o\left(1-b_{n}\right)^{2}\right)}{b_{n}-a_{n}} \\
= & \left(b_{n}-1\right)\left(1-a_{n}\right)(1 / 2+o(1)) .
\end{aligned}
$$

因此 $\lambda>2$, 矛盾.

我们再说明 $\lambda$ 在渐进意义下是最优的.

对固定的 $b>0$, 先取 $a_{1}=b, a_{2}=\cdots=a_{n}=\frac{n-b}{n-1}$.

$$
\begin{aligned}
& \text { 令 } n \rightarrow \infty \text { 可以得到 } \\
& \lim _{n \rightarrow \infty} \frac{\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n}{\left(1-a_{1} a_{2} \cdots a_{n}\right)}=\lim _{n \rightarrow \infty} \frac{\frac{1}{b}+(n-1)\left(\frac{n-1}{n-b}\right)-n}{1-b\left(1+\frac{1-b}{n-1}\right)^{n-1}} \\
& =\lim _{n \rightarrow \infty}\left(\frac{1}{b}+\frac{(b-2) n+1}{n-b}\right) \cdot \frac{1}{1-b \mathrm{e}^{1-b}} \\
& =\frac{(b-1)^{2}}{b} \cdot \frac{1}{1-b \mathrm{e}^{1-b}} \geq \lambda
\end{aligned}
$$

再对 $b$ 取下确界就可以得到结论.

## 参考文献

[1] 韩新炎. 关于 Cîrtoaje 不等式的一个注记 $[\mathrm{J}]$. 数学新星网. 学生专栏, 2018-10-05 期.

