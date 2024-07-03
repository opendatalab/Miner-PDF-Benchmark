数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 一道不等式的最佳常数 

解尧平<br>(天津市实验中学, 300074)

笔者曾经在新星征解第 28 期中提供了如下不等式问题:

问题 1 已知 $x_{1} \geqslant x_{2} \geqslant \cdots \geqslant x_{n} \geqslant 0, y_{1} \geqslant y_{2} \geqslant \cdots \geqslant y_{n} \geqslant 0$, 且 $\sum_{i=1}^{n} x_{i}=$ $\sum_{i=1}^{n} y_{i}=n$. 证明:

$$
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right|<e^{\frac{n}{2}}
$$

黄嘉俊同学在文 [1] 中利用归纳法证明了如下结果:

问题 2 已知 $x_{1} \geqslant x_{2} \geqslant \cdots \geqslant x_{n} \geqslant 0, y_{1} \geqslant y_{2} \geqslant \cdots \geqslant y_{n} \geqslant 0$, 且 $\sum_{i=1}^{n} x_{i} \leqslant A$, $\sum_{i=1}^{n} y_{i} \leqslant A$. 证明:

$$
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right|<\left(\frac{A}{n}\right)^{n} e^{\frac{n}{e}} .
$$

近日, 笔者证明了下面一个更强的结果:

问题 3 已知 $x_{1} \geqslant x_{2} \geqslant \cdots \geqslant x_{n} \geqslant 0, y_{1} \geqslant y_{2} \geqslant \cdots \geqslant y_{n} \geqslant 0$, 且 $\sum_{i=1}^{n} x_{i}=$ $\sum_{i=1}^{n} y_{i}=n$. 证明:

$$
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right|<\lambda^{n}
$$

其中正实数 $\lambda$ 满足方程 $e \lambda \ln \lambda=1$, 并且常数 $\lambda$ 是最佳的.

证明 首先证明两个引理.

引理 1 对任意正实数 $k$, 均有 $k^{\frac{1}{k+1}} \leqslant \lambda$.

修订日期: 2019-07-04.
证明 设 $f(k)=k^{\frac{1}{k+1}}$, 则 $f^{\prime}(k)=k^{\frac{1}{k+1}} \frac{1+\frac{1}{k}-\ln k}{(k+1)^{2}}$.

令 $g(k)=1+\frac{1}{k}-\ln k$, 则 $g(k)$ 在区间 $(0, \infty)$ 上单调递减, 而由 $\lambda$ 的定义知 $g(e \lambda)=0$, 故 $f(k)$ 在区间 $(0, e \lambda)$ 上单调递增, 在区间 $(e \lambda, \infty)$ 上单调递减,因此 $f(k)_{\max }=f(e \lambda)=\lambda$.

引理 1 得证!

引理 2 若正实数 $\alpha, \beta, \gamma, a, b, c$ 满足

$$
\left\{\begin{array}{l}
(b+c)(\alpha+\beta)=\alpha+\beta+\gamma \\
\alpha a+\gamma c=\beta b
\end{array},\right.
$$

则 $a^{\alpha} b^{\beta} c^{\gamma}<\lambda^{\alpha+\beta+\gamma}$.

证明 由齐次性, 不妨设 $\alpha+\beta+\gamma=1$, 经过化简, 结论等价于证明:

$$
b\left(\frac{1}{b(1-\gamma)}-1\right)^{\gamma}\left(\frac{1-\frac{\gamma}{b(1-\gamma)}}{\alpha}-1\right)^{\alpha}<\lambda
$$

其中 $\frac{\gamma}{1-\gamma}<b<\frac{1}{1-\gamma}$. 由引理 1 可知:

$$
\left(\frac{1-\frac{\gamma}{b(1-\gamma)}}{\alpha}-1\right)^{\alpha}=\left(\left(\frac{1-\frac{\gamma}{b(1-\gamma)}}{\alpha}-1\right)^{\frac{1}{1+\left(\frac{1-\frac{\gamma}{b(1-\gamma)}}{\alpha}-1\right)}}\right)^{1-\frac{\gamma}{b(1-\gamma)}} \leqslant \lambda^{1-\frac{\gamma}{b(1-\gamma)}}
$$

故只需证明:

$$
b\left(\frac{1}{b(1-\gamma)}-1\right)^{\gamma}<\lambda^{\frac{\gamma}{b(1-\gamma)}}
$$

令 $b_{1}=b(1-\gamma)$, 则 $\gamma<b_{1}<1$, 上式等价于:

$$
\left(\frac{b_{1}}{1-\gamma}\right)^{\frac{1}{\gamma}}\left(\frac{1}{b_{1}}-1\right)<\lambda^{\frac{1}{b_{1}}}
$$

设函数 $f(\gamma)=\left(\frac{b_{1}}{1-\gamma}\right)^{\frac{1}{\gamma}}$, 则求导可知 $f(\gamma)$ 在区间 $\left(0, b_{1}\right]$ 上单调递增, 故结合引理 1 可知:

$$
\begin{aligned}
\left(\frac{b_{1}}{1-\gamma}\right)^{\frac{1}{\gamma}}\left(\frac{1}{b_{1}}-1\right) & <\left(\frac{b_{1}}{1-b_{1}}\right)^{\frac{1}{b_{1}}}\left(\frac{1}{b_{1}}-1\right) \\
& =\left(\left(\frac{b_{1}}{1-b_{1}}\right)^{\frac{1}{1+\frac{b_{1}}{1-b_{1}}}}\right)^{\frac{1}{b_{1}}} \leq \lambda^{\frac{1}{b_{1}}} .
\end{aligned}
$$

引理 2 得证!

回到原题. 不失一般性, 可以不妨设 $(-1)^{i-1}\left(x_{u}-y_{u}\right)>0$, 其中 $\alpha_{1}+\cdots+$ $\alpha_{i-1}+1 \leq u \leq \alpha_{1}+\cdots+\alpha_{i}, i=1,2, \cdots, k$, 这里 $\alpha_{0}=0, \alpha_{1}, \cdots, \alpha_{k} \in \mathbb{N}^{*}, k \geqslant 2$,且 $\sum_{i=1}^{k} \alpha_{i}=n$.
由平均值不等式:

$$
\begin{aligned}
\prod_{i=1}^{n}\left|x_{i}-y_{i}\right| & =\prod_{i=1}^{k} \prod_{j=\alpha_{1}+\cdots+\alpha_{i-1}+1}^{\alpha_{1}+\cdots+\alpha_{i}}(-1)^{i-1}\left(x_{j}-y_{j}\right) \\
& \leqslant \prod_{i=1}^{k}\left(\frac{\sum_{j=\alpha_{1}+\cdots+\alpha_{i-1}+1}^{\alpha_{1}+\cdots+\alpha_{i}}(-1)^{i-1}\left(x_{j}-y_{j}\right)}{\alpha_{i}}\right)^{\alpha_{i}} .
\end{aligned}
$$

令 $x_{i}^{\prime}=\frac{\sum_{j=\alpha_{1}+\cdots+\alpha_{i-1}+1}^{\alpha_{1}+\cdots+\alpha_{i}}(-1)^{i-1}\left(x_{j}-y_{j}\right)}{\alpha_{i}}, z_{i}=\min \left\{x_{i}, y_{i}\right\}, w_{i}=\max \left\{x_{i}, y_{i}\right\}$, 则 $x_{i}^{\prime}>0$, 数列 $\left\{z_{i}\right\},\left\{w_{i}\right\}$ 均单调不增, 并且由之前设定的序关系可知

$$
z_{\alpha_{1}+\cdots+\alpha_{i}} \geqslant w_{\alpha_{1}+\cdots+\alpha_{i}+1} .
$$

因此对于任意 $\alpha_{1}+\cdots+\alpha_{t-1}+1 \leqslant u \leqslant \alpha_{1}+\cdots+\alpha_{t}$, 均有:

$$
\begin{aligned}
\sum_{i=t+1}^{k} x_{i}^{\prime} & =\sum_{i=t+1}^{k} \frac{\sum_{j=\alpha_{1}+\cdots+\alpha_{i-1}+1}^{\alpha_{1}+\cdots+\alpha_{i}}(-1)^{i-1}\left(x_{j}-y_{j}\right)}{\alpha_{i}} \\
& \leqslant \sum_{i=t+1}^{k}\left(w_{\alpha_{1}+\cdots+\alpha_{i-1}+1}-z_{\alpha_{1}+\cdots+\alpha_{i}}\right) \\
& \leqslant \sum_{i=t+1}^{k}\left(z_{\alpha_{1}+\cdots+\alpha_{i-1}}-z_{\alpha_{1}+\cdots+\alpha_{i}}\right) \\
& =z_{\alpha_{1}+\cdots+\alpha_{t}}-z_{\alpha_{1}+\cdots+\alpha_{k}} \leqslant z_{u} .
\end{aligned}
$$

于是

$$
\begin{aligned}
n & =\sum_{t=1}^{k} \sum_{i=\alpha_{1}+\cdots+\alpha_{t-1}+1}^{\alpha_{1}+\cdots+\alpha_{t}} \frac{x_{i}+y_{i}}{2} \\
& =\sum_{t=1}^{k} \sum_{i=\alpha_{1}+\cdots+\alpha_{t-1}+1}^{\alpha_{1}+\cdots+\alpha_{t}}\left(z_{i}+\frac{(-1)^{t-1}\left(x_{i}-y_{i}\right)}{2}\right) \\
& \geqslant \sum_{t=1}^{k} \sum_{i=\alpha_{1}+\cdots+\alpha_{t-1}+1}^{\alpha_{1}+\cdots+\alpha_{t}}\left(\frac{(-1)^{t-1}\left(x_{i}-y_{i}\right)}{2}+x_{t+1}^{\prime}+\cdots+x_{k}^{\prime}\right) \\
& =\sum_{t=1}^{k} \alpha_{t}\left(\frac{x_{t}^{\prime}}{2}+x_{t+1}^{\prime}+\cdots+x_{k}^{\prime}\right) .
\end{aligned}
$$

故现在我们有限定条件:

$$
\begin{aligned}
& \sum_{i=1}^{k} \alpha_{i}=n, \\
& \sum_{i=1}^{k} \alpha_{i} x_{i}^{\prime}(-1)^{i-1}=0
\end{aligned}
$$

$$
\sum_{i=1}^{k} \alpha_{i}\left(\frac{x_{i}^{\prime}}{2}+x_{i+1}^{\prime}+\cdots+x_{k}^{\prime}\right) \leqslant n .
$$

接下来只需证明:

$$
\sum_{i=1}^{k} \alpha_{i} \ln x_{i}^{\prime}<n \ln \lambda
$$

不妨考虑不等式 (3) 等号成立的情形(最优情况), 并且我们将 $\alpha_{i}$ 的取值范围扩充为全体非负实数.

当 $k=2$ 时, 可以解得 $\left\{\begin{array}{l}x_{1}^{\prime}=\frac{n}{\alpha_{1}}-1 \\ x_{2}^{\prime}=1\end{array}\right.$. 故结合引理 1 可得

$\alpha_{1} \ln x_{1}^{\prime}+\alpha_{2} \ln x_{2}^{\prime}=\alpha_{1} \ln \left(\frac{n}{\alpha_{1}}-1\right)=n \ln \left(\left(\frac{n}{\alpha_{1}}-1\right)^{\frac{1}{1+\left(\frac{n}{\alpha_{1}}-1\right)}}\right) \leqslant n \ln \lambda$.

当 $k \geqslant 3$ 时, 记点 $A_{i}=\left(x_{i}^{\prime}(-1)^{i}, \frac{x_{i}^{\prime}}{2}+x_{i+1}^{\prime}+\cdots+x_{k}^{\prime}, \ln x_{i}^{\prime}\right)$, 并设点集 $\left\{A_{1}, A_{2}, \cdots, A_{k}\right\}$ 的凸包为 $T$, 则由熟知结论:

$$
T=\left\{\left.\frac{\alpha_{1}^{\prime} \overrightarrow{O A}_{1}+\cdots+\alpha_{k}^{\prime} \overrightarrow{O A}_{k}}{\alpha_{1}^{\prime}+\cdots+\alpha_{k}^{\prime}} \right\rvert\, \alpha_{1}^{\prime}, \cdots, \alpha_{k}^{\prime} \in[0,+\infty)\right\}
$$

设

$$
T \cap\{(0,1, k) \mid k \in \mathbb{R}\}=\{(0,1, k) \mid k \in[u, v]\},
$$

则由等式 (1), (2), (3) 知 $\frac{\alpha_{1} \ln x_{1}^{\prime}+\cdots+\alpha_{k} \ln x_{k}^{\prime}}{\alpha_{1}+\cdots+\alpha_{k}}$ 的取值范围为 $[u, v]$, 故

$$
\max \left\{\sum_{i=1}^{k} \alpha_{i} \ln x_{i}^{\prime}\right\}=n v
$$

设点 $V(0,1, v)$, 则由凸包 $T$ 的凸性知点 $V$ 在凸包 $T$ 的边界上, 故存在点集 $\left\{A_{1}, A_{2}, \cdots, A_{k}\right\}$ 中的三个点 $A_{i_{1}}, A_{i_{2}}, A_{i_{3}}$, 使得点 $V$ 在 $\triangle A_{i_{1}} A_{i_{2}} A_{i_{3}}$ 的内部或边界上, 因此存在和为 $n$ 的非负实数 $\beta_{1}, \beta_{2}, \beta_{3}$, 使得

$$
(0, n, n v)=\beta_{1} O \vec{A}_{i_{1}}+\beta_{2} O \vec{A}_{i_{2}}+\beta_{3} O \vec{A}_{i_{3}}
$$

此时我们有:

$$
\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime}+\beta_{3} \ln x_{i_{3}}^{\prime}=\max \left\{\sum_{i=1}^{k} \alpha_{i} \ln x_{i}^{\prime}\right\} .
$$

故只需证明 $\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime}+\beta_{3} \ln x_{i_{3}}^{\prime} \leqslant n \ln \lambda$, 并说明原不等式等号无法取到即可.

下面我们分两种情形进行讨论.

1)当 $\beta_{1}, \beta_{2}, \beta_{3}$ 中含有 0 时, 可以不妨设 $\beta_{3}=0$ 及 $i_{1}<i_{2}$, 则 $i_{1} \equiv i_{2}(\bmod 2)$,
因此 $\left\{\begin{array}{l}\beta_{1}+\beta_{2}=n \\ \beta_{1} x_{i_{1}}^{\prime}=\beta_{2} x_{i_{2}}^{\prime} \\ \beta_{1}\left(\frac{x_{i_{1}}}{2}+x_{i_{2}}^{\prime}\right)+\beta_{2} \frac{x_{i_{2}}^{\prime}}{2} \leqslant n\end{array} \quad\right.$, 由此可以解得 $\left\{\begin{array}{l}x_{i_{1}}^{\prime} \leqslant \frac{n}{\beta_{1}}-1 \\ x_{i_{2}}^{\prime} \leqslant 1\end{array}\right.$.

故类似 $k=2$ 的情形可得:

$$
\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime}+\beta_{3} \ln x_{i_{3}}^{\prime} \leqslant \beta_{1} \ln \left(\frac{n}{\beta_{1}}-1\right) \leqslant n \ln \lambda .
$$

2) 当 $\beta_{1}, \beta_{2}, \beta_{3}$ 中不含有 0 时, 可以不妨设 $i_{1}<i_{2}<i_{3}$.

我们再分三种小情形进行讨论.

a) 当 $i_{1} \equiv i_{2} \not \equiv i_{3}(\bmod 2)$ 时,

故由 1) 可知 $\gamma_{1} \ln y_{1}^{\prime}+\gamma_{2} \ln y_{2}^{\prime} \leqslant n \ln \lambda$.

令 $\gamma_{1}=\beta_{1}+\beta_{2}, \gamma_{2}=\beta_{3}, y_{1}^{\prime}=\frac{\beta_{1} x_{i_{1}}^{\prime}+\beta_{2} x_{i_{2}}^{\prime}}{\beta_{1}+\beta_{2}}, y_{2}^{\prime}=x_{i_{3}}^{\prime}$, 则 $\left\{\begin{array}{l}\gamma_{1}+\gamma_{2}=n \\ \gamma_{1} y_{1}^{\prime}=\gamma_{2} y_{2}^{\prime} \\ \gamma_{1}\left(\frac{y_{1}^{\prime}}{2}+y_{2}^{\prime}\right)+\gamma_{2} \frac{y_{2}^{\prime}}{2} \leqslant n\end{array}\right.$

再由加权 Jensen 不等式可得

$$
\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime} \leqslant\left(\beta_{1}+\beta_{2}\right) \ln \frac{\beta_{1} x_{i_{1}}^{\prime}+\beta_{2} x_{i_{2}}^{\prime}}{\beta_{1}+\beta_{2}}=\gamma_{1} \ln y_{1}^{\prime} .
$$

故 $\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime}+\beta_{3} \ln x_{i_{3}}^{\prime} \leqslant \gamma_{1} \ln y_{1}^{\prime}+\gamma_{2} \ln y_{2}^{\prime} \leqslant n \ln \lambda$.

b) 当 $i_{1} \not \equiv i_{2} \equiv i_{3}(\bmod 2)$ 时, 与 a) 同理可推出结论.

c) 当 $i_{1} \equiv i_{3} \not \equiv i_{2}(\bmod 2)$ 时, 我们有:

$$
\begin{aligned}
& \beta_{1}+\beta_{2}+\beta_{3}=n, \\
& \beta_{1} x_{i_{1}}^{\prime}+\beta_{3} x_{i_{3}}^{\prime}=\beta_{2} x_{i_{2}}^{\prime}, \\
& \beta_{1}\left(\frac{x_{i_{1}}^{\prime}}{2}+x_{i_{2}}^{\prime}+x_{i_{3}}^{\prime}\right)+\beta_{2}\left(\frac{x_{i_{2}}^{\prime}}{2}+x_{i_{3}}^{\prime}\right)+\beta_{3} \frac{x_{i_{3}}^{\prime}}{2} \leqslant n .
\end{aligned}
$$

不妨考虑不等式 (6) 等号成立的情形(最优情形), 此时我们得到

$$
\left\{\begin{array}{l}
\left(x_{i_{2}}^{\prime}+x_{i_{3}}^{\prime}\right)\left(\beta_{1}+\beta_{2}\right)=\beta_{1}+\beta_{2}+\beta_{3} \\
\beta_{1} x_{i_{1}}^{\prime}+\beta_{3} x_{i_{3}}^{\prime}=\beta_{2} x_{i_{2}}^{\prime}
\end{array},\right.
$$

故由引理 2 :

$\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime}+\beta_{3} \ln x_{i_{3}}^{\prime}=\ln x_{i_{1}}^{\prime \beta_{1}} x_{i_{2}}^{\prime \beta_{2}} x_{i_{3}}^{\prime \beta_{3}}<\ln \lambda^{\beta_{1}+\beta_{2}+\beta_{3}}=n \ln \lambda$.

综上, 我们证明了不等式 $\beta_{1} \ln x_{i_{1}}^{\prime}+\beta_{2} \ln x_{i_{2}}^{\prime}+\beta_{3} \ln x_{i_{3}}^{\prime} \leqslant n \ln \lambda$, 并且根据取等条件可以推知原不等式无法取等. 由此我们证明了原不等式.
而另一方面, 令 $t=\left[\frac{n}{e \lambda+1}\right]$, 取 $x_{1}=x_{2}=\cdots=x_{t}=\frac{n}{t}, x_{t+1}=\cdots=x_{n}=$ $0, y_{1}=y_{2}=\cdots=y_{n}=1$, 则 $\lim _{n \rightarrow+\infty}\left(\prod_{i=1}^{n}\left|x_{i}-y_{i}\right|\right)^{\frac{1}{n}}=\lambda$, 故常数 $\lambda$ 是最佳的.

## 参考文献

[1] 黄嘉俊. 一道新星征解题的简证 [J]. 数学新星网. 学生专栏, 2019-4-13 期.

