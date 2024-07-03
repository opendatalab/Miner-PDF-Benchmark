# 关于 Cîrtoaje 不等式的一个注记 

韩新森

(浙江省乐清市乐成寄宿中学, 325600)

Vasile Cîrtoaje 在 《Algebraic Inequalities》一书中证明了如下代数不等式:

定理 1 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且满足 $a_{1}+\cdots+a_{n}=n$. 证明:

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n \geq \frac{8(n-1)}{n^{2}}\left(1-a_{1} a_{2} \cdots a_{n}\right) .
$$

冷岗松教授问, 上面的不等式右边的系数是否可用某个绝对常数来代替?注意到 $\frac{8(n-1)}{n^{2}} \rightarrow 0$ (当 $n \rightarrow+\infty$ ), 所以当 $n$ 充分大时, 这种代替是有意义的.

本文回答了冷岗松教授的问题, 证明了如下定理:

定理 2 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是正实数且 $a_{1}+\cdots+a_{n}=n$. 证明:

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n \geq(2 \sqrt{2}-1)\left(1-a_{1} a_{2} \cdots a_{n}\right) .
$$

证明 记

$$
F\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}+\lambda \cdot a_{1} \cdot a_{2} \cdots a_{n},
$$

其中 $\lambda=2 \sqrt{2}-1$.

要证

$$
\frac{1}{a_{1}}+\frac{1}{a_{2}}+\cdots+\frac{1}{a_{n}}-n \geq(2 \sqrt{2}-1)\left(1-a_{1} a_{2} \cdots a_{n}\right),
$$

只需证

$$
F\left(a_{1}, a_{2}, \cdots, a_{n}\right) \geq n+\lambda .
$$

令 $\varepsilon=\frac{1}{n+\lambda}$. 下面分两种情况讨论.

情况一: 若存在 $k_{0}\left(1 \leq k_{0} \leq n\right)$, 使得 $a_{k_{0}}<\varepsilon$, 则显然有

$$
F\left(a_{1}, \cdots, a_{n}\right) \geq n+\lambda .
$$[^0]情况二: $a_{k} \geq \varepsilon(k=1, \cdots, n)$.

由题设条件: $a_{1}, \cdots, a_{n}>0$ 且 $a_{1}+\cdots+a_{n}=n$, 可得 $a_{k} \in[\varepsilon, n]$. 又由于 $F$ 为连续函数, 故 $F$ 在有界闭区间上可取到最小值, 设最小值点为 $\left(b_{1}, \cdots, b_{n}\right)$.于是只需证明 $F\left(b_{1}, \cdots, b_{n}\right) \geq n+\lambda$.

若存在 $k_{1}\left(1 \leq k_{1} \leq n\right)$, 使得 $b_{k_{1}}=\varepsilon$, 则显然有

$$
F\left(b_{1}, \cdots, b_{n}\right) \geq n+\lambda
$$

若对所有的 $k(1 \leq k \leq n)$, 均有 $b_{k}>\varepsilon$. 则任取 $i, j(1 \leq i<j \leq n)$ 使得 $a_{i}+a_{j}=b_{i}+b_{j}$; 取 $k(1 \leq k \leq n, k \neq i, j)$ 使得 $a_{k}=b_{k}$. 从而

$$
\begin{aligned}
F\left(a_{1}, a_{2}, \cdots, a_{n}\right) & =\sum_{k \neq i, j} \frac{1}{a_{k}}+\frac{a_{i}+a_{j}}{a_{i} a_{j}}+a_{i} a_{j} \cdot \lambda \cdot \prod_{k \neq i, j} a_{k} \\
& =\sum_{k \neq i, j} \frac{1}{b_{k}}+\frac{b_{i}+b_{j}}{a_{i} a_{j}}+a_{i} a_{j} \cdot \lambda \cdot \prod_{k \neq i, j} b_{k} .
\end{aligned}
$$

此时 $F\left(a_{1}, \cdots, a_{n}\right)$ 是关于 $a_{i} a_{j}$ 的函数, 其中

$$
a_{i} a_{j} \in\left[\varepsilon\left(b_{i}+b_{j}-\varepsilon\right),\left(\frac{b_{i}+b_{j}}{2}\right)^{2}\right], b_{i} b_{j}>\varepsilon\left(b_{i}+b_{j}-\varepsilon\right)
$$

由对勾函数的单调性及 $F$ 在 $\left(b_{1}, \cdots, b_{n}\right)$ 取到最小值可得

$$
\frac{b_{i}+b_{j}}{b_{i} b_{j}}=b_{i} b_{j} \cdot \lambda \cdot \prod_{k \neq i, j} b_{k} \text { 或 } b_{i} b_{j}=\left(\frac{b_{i}+b_{j}}{2}\right)^{2} .
$$

即 $\frac{1}{b_{i}}+\frac{1}{b_{j}}=\lambda \cdot \prod_{k=1}^{n} b_{k}$ 或 $b_{i}=b_{j}$ 两者必有一个成立. 由此可得 $b_{1}, \cdots, b_{n}$ 中至多有两种不同取值.

事实上, 若 $b_{i}, b_{j}, b_{k}(1 \leq i<j<k \leq n)$ 互不相同, 则必有

$$
\frac{1}{b_{i}}+\frac{1}{b_{j}}=\frac{1}{b_{j}}+\frac{1}{b_{k}}=\frac{1}{b_{k}}+\frac{1}{b_{i}}=\lambda \cdot \prod_{l=1}^{n} b_{l}
$$

这说明 $b_{i}=b_{j}=b_{k}$, 这与 $b_{i}, b_{j}, b_{k}$ 互不相同矛盾. 故 $b_{1}, \cdots, b_{n}$ 中至多有两种不同取值.

设 $b_{1}, \cdots, b_{n}$ 中有 $u$ 个 $1-v t, v$ 个 $1+u t$. 其中 $u, v \in \mathbb{N}^{+}, u+v=n, t \in$ $\mathbb{R}$ 且 $0 \leq t<\frac{1}{v}$ (若 $u, v$ 中有 0 , 则 $b_{1}=\cdots=b_{n}=1$, 不等式显然成立). 此时 $F\left(b_{1}, \cdots, b_{n}\right)$ 可转化为

$$
f(t)=\frac{u}{1-v t}+\frac{v}{1+u t}+\lambda \cdot(1-v t)^{u} \cdot(1+u t)^{v}, \quad t \in\left[0, \frac{1}{v}\right) .
$$

故只需证

$$
f(t) \geq n+\lambda=u+v+\lambda \text {. }
$$

因为 $f$ 在 $\left[0, \frac{1}{v}\right)$ 上连续, 故只需证:

(1) $f(0) \geq n+\lambda$;

(2) $\lim _{t \rightarrow\left(\frac{1}{v}\right)^{-}} f(t) \geq n+\lambda$;

(3) 对 $t \in\left[0, \frac{1}{v}\right)$ 满足 $f^{\prime}(t)=0$, 有 $f(t) \geq n+\lambda$.

对 (1), $f(0)=u+v+\lambda=n+\lambda \geq n+\lambda$.

对 $(2)$, 当 $t \rightarrow\left(\frac{1}{v}\right)^{-}$时, $f(t) \rightarrow+\infty$, 故 $\lim _{t \rightarrow\left(\frac{1}{v}\right)^{-}} f(t) \geq n+\lambda$.

下证 (3). 注意到

$$
\begin{aligned}
f^{\prime}(t) & =\frac{u v}{(1-v t)^{2}}-\frac{u v}{(1-u t)^{2}}+\lambda \cdot(1-v t)^{u} \cdot(1+u t)^{v} \cdot\left(-\frac{u v}{1-v t}+\frac{u v}{1+u t}\right) \\
& =u v \cdot\left(\frac{1}{1-v t}-\frac{1}{1+u t}\right) \cdot\left(\frac{1}{1-v t}+\frac{1}{1+u t}-\lambda \cdot(1-v t)^{u} \cdot(1+u t)^{v}\right) .
\end{aligned}
$$

由 $f^{\prime}(t)=0$ 可得

$$
\frac{1}{1-v t}+\frac{1}{1+u t}=\lambda \cdot(1-v t)^{u} \cdot(1+u t)^{v} .
$$

故此时

$$
\begin{aligned}
f(t) & =\frac{u+1}{1-v t}+\frac{v+1}{1+u t} \\
& =\frac{u^{2}+u}{u-u v t}+\frac{v^{2}+v}{v+u v t} \\
& \geq \frac{\left(\sqrt{u^{2}+u}+\sqrt{v^{2}+v}\right)^{2}}{u+v} \quad \text { (Cauchy 不等式) } \\
& \geq \frac{(\sqrt{n(n-1)}+\sqrt{2 \cdot 1})^{2}}{u+v} \\
& =\frac{n^{2}-n+2+2 \sqrt{2 n^{2}-2 n}}{n} \\
& >\frac{n^{2}-n+2 \sqrt{2} n}{n} \\
& =n+2 \sqrt{2}-1 .
\end{aligned}
$$

其中, (1) 式成立是因为对 $g(x)=\sqrt{x(x+1)}, x>0$ 求导, 有

$$
g^{\prime}(x)=\frac{1}{2} \cdot \sqrt{\frac{(2 x+1)^{2}}{x(x+1)}}=\frac{1}{2} \cdot \sqrt{4+\frac{1}{x(x+1)}}
$$

关于 $x$ 单调递减, 即 $g$ 在 $(0, \infty)$ 下凸. 由优超不等式即得 $(1)$;

$(2) \Leftrightarrow \sqrt{2 n^{2}-2 n}>\sqrt{2} n-1 \Leftrightarrow 2 n^{2}-2 n>2 n^{2}-2 \sqrt{2} n+1 \Leftrightarrow 2(\sqrt{2}-1) n>1$,利用 $n=u+v \geq 2$ 即知该式成立

综合情况一, 情况二可可知定理 2 成立.


[^0]:    收稿日期: 2018-03-30； 修订日期: 2018-08-08.

