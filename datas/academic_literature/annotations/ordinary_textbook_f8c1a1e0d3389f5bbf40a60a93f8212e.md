# 两道 IMO 预选题的新解法 

高轶寒

(南京外国语学校, 210018)

第 57 届 IMO 于 2016 年 7 月在香港举办. 此届 IMO 预选题中代数问题共有 8 道题, 其中编号为 A7, A8 两题似乎难度较大. 本短文介绍我的解法, 供有兴趣者参考.

A7. 求所有函数 $f: \mathbf{R} \rightarrow \mathbf{R}$ 使得 $f(0) \neq 0$, 且

$$
f^{2}(x+y)=2 f(x) f(y)+\max \left\{f\left(x^{2}\right)+f\left(y^{2}\right), f\left(x^{2}+y^{2}\right)\right\}
$$

对任意实数 $x, y$ 成立.

解 在给定的方程中令 $x=y=0$, 得

$$
f^{2}(0)+\max \{2 f(0), f(0)\}=0 .
$$

由于 $f(0) \neq 0, f^{2}(0)>0$, 所以由上式知 $f(0)<0$, 且有 $f^{2}(0)+f(0)=0$.由此得 $f(0)=-1$.

现令 $g(x)=f(x)+1$, 则 $g(0)=0$, 这时原方程变为:

$$
\begin{aligned}
& (g(x+y)-1)^{2} \\
& \quad=2(g(x)-1)(g(y)-1)+\max \left\{g\left(x^{2}\right)+g\left(y^{2}\right)-2, g\left(x^{2}+y^{2}\right)-1\right\} .
\end{aligned}
$$

下证 $g(x)$ 是奇函数, 即对 $\forall t \in \mathbf{R}$ 有 $g(t)=-g(-t)$.

在 (1) 中令 $y=0$ 并化简知 $g\left(x^{2}\right)=g^{2}(x)$. 故

$$
g\left(x^{2}\right)=g\left((-x)^{2}\right)=g^{2}(-x),
$$

即

$$
|g(x)|=|g(-x)|
$$

收稿日期: 2017-01-23； 修订日期: 2017-05-12.
假设 $g(x)$ 不是奇函数, 则若存在 $t$ 使得 $g(t) \neq-g(-t)$, 则由 (2) 知 $g(t)=$ $g(-t) \neq 0$. 在 (1) 中分别代入 $\left(\frac{t}{2}, \frac{t}{2}\right),\left(\frac{t}{2},-\frac{t}{2}\right),\left(-\frac{t}{2},-\frac{t}{2}\right)$, 并令

$$
\max \left\{2 g\left(\frac{t^{2}}{4}\right)-2, g\left(\frac{t^{2}}{2}\right)-1\right\}=A
$$

可得

$$
\begin{aligned}
(g(t)-1)^{2} & =2\left(g\left(\frac{t}{2}\right)-1\right)^{2}+A \\
(g(0)-1)^{2} & =2\left(g\left(\frac{t}{2}\right)-1\right)\left(g\left(-\frac{t}{2}\right)-1\right)+A \\
(g(-t)-1)^{2} & =2\left(g\left(-\frac{t}{2}\right)-1\right)^{2}+A
\end{aligned}
$$

由 $g(t)=g(-t)$ 及 $(3),(5)$ 知

$$
\left(g\left(\frac{t}{2}\right)-1\right)^{2}=\left(g\left(-\frac{t}{2}\right)-1\right)^{2}
$$

所以

$$
\left(g\left(\frac{t}{2}\right)-g\left(-\frac{t}{2}\right)\right)\left(g\left(\frac{t}{2}\right)+g\left(-\frac{t}{2}\right)-2\right)=0 .
$$

若 $g\left(\frac{t}{2}\right) \neq g\left(-\frac{t}{2}\right)$, 则由 $(2)$ 知, $g\left(\frac{t}{2}\right)=-g\left(-\frac{t}{2}\right)$, 故

$$
g\left(\frac{t}{2}\right)+g\left(-\frac{t}{2}\right)-2=-2 \neq 0
$$

矛盾!

所以 $g\left(\frac{t}{2}\right)=g\left(-\frac{t}{2}\right)$. 这时 (3),(4) 右边相等, 故

$$
(g(t)-1)^{2}=(g(0)-1)^{2}=1
$$

又因为 $g(t) \neq 0$, 故 $g(t)=2$, 从而 $g(-t)=2$.

再在 (1) 中代入 $(t,-t)$ 知

$$
\begin{aligned}
1=(g(0)-1)^{2} & =2(g(t)-1)^{2}+\max \left\{2 g\left(t^{2}\right)-2, g\left(2 t^{2}\right)-1\right\} \\
& \geq 2(g(t)-1)^{2}+2 g\left(t^{2}\right)-2 \\
& =2 \times 1+2 \times 2^{2}-2=8>1,
\end{aligned}
$$

矛盾!

故这就说明了对 $\forall t \in \mathbf{R}, g(t)=-g(-t)$, 即 $g(x)$ 为奇函数.

再将 $(-x,-y)$ 代入 (1) 并由 $g(x)$ 是奇函数知

$$
(g(x+y)+1)^{2}=2(g(x)+1)(g(y)+1)
$$

$$
+\max \left\{g\left(x^{2}\right)+g\left(y^{2}\right)-2, g\left(x^{2}+y^{2}\right)-1\right\} .
$$

由 (1) 和 (6) 可得

$$
\begin{aligned}
& (g(x+y)+1)^{2}-2(g(x)+1)(g(y)+1) \\
= & (g(x+y)-1)^{2}-2(g(x)-1)(g(y)-1) .
\end{aligned}
$$

故

$$
g(x+y)=g(x)+g(y)
$$

又因为 $g\left(x^{2}\right)=g^{2}(x)$, 所以当 $x \geq 0$ 时, 有

$$
g(x) \geq 0 \text {. }
$$

由 (7), (8) 知, $g(x)=k x(k \in \mathbf{R})$. 再代入 $g\left(x^{2}\right)=g^{2}(x)$ 知, $k=k^{2}$, 即 $k=0$或 $k=1$.

所以 $g(x)=0$ 或 $g(x)=x$, 即 $f(x)=-1$ 或 $f(x)=x-1$ 是问题的解.

经检验, 这两个解均满足题意.

评注 上述解法的要点: 首先确定初始值 $f(0)=-1$. 再作平移变换 $g(x)=f(x)+1$, 使得初始值就变为 $g(0)=0$, 然后核心部分 (难点) 就是证明 $g(x)$ 是奇函数. 有了奇偶性便将问题转化成了 Cauchy 方程来处理了.

A8. 求最大的实数 $a$, 使得对所有 $n \geq 1$ 和任意满足 $0=x_{0}<x_{1}<\cdots<x_{n}$的实数 $x_{0}, x_{1}, \cdots, x_{n}$ 有

$$
\frac{1}{x_{1}-x_{0}}+\frac{1}{x_{2}-x_{1}}+\cdots+\frac{1}{x_{n}-x_{n-1}} \geq a\left(\frac{2}{x_{1}}+\frac{3}{x_{2}}+\cdots+\frac{n+1}{x_{n}}\right) .
$$

解 令 $a_{k}=x_{k}-x_{k-1}, k=1,2, \cdots, n$, 则 $a_{k}>0$.

这时问题转化为: 求最大的正常数 $a$, 使得对任意 $n \geq 1$ 和任意正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 有

$$
\sum_{i=1}^{n} \frac{1}{a_{i}} \geq a \sum_{i=1}^{n} \frac{i+1}{a_{1}+\cdots+a_{i}}
$$

下面首先证明当 $a=\frac{4}{9}$ 时上述不等式成立.

先构造一个数列 $\left\{c_{i}\right\}$, 其中 $c_{i}=\frac{i(i+1)}{2}$, 令 $T_{i}=\sum_{j=1}^{i} c_{j}$. 则

$$
T_{i}=\sum_{j=1}^{i} \frac{j(j+1)(j+2)-(j-1) j(j+1)}{6}=\frac{i(i+1)(i+2)}{6} .
$$

故

$$
\begin{aligned}
& \sum_{i=t}^{n} \frac{(i+1)}{T_{i}^{2}}=\sum_{i=t}^{n} \frac{36(i+1)}{i^{2}(i+1)^{2}(i+2)^{2}} \\
& =\frac{9}{4} \sum_{i=t}^{n} \frac{4(i+1)}{\frac{i^{2}(i+1)^{2}(i+2)^{2}}{4}}=\frac{9}{4} \sum_{i=t}^{n} \frac{(i+2)^{2}-i^{2}}{\frac{1}{4} i^{2}(i+1)^{2}(i+2)^{2}} \\
& =\frac{9}{4} \sum_{i=t}^{n}\left(\frac{1}{c_{i}^{2}}-\frac{1}{c_{i+1}^{2}}\right)=\frac{9}{4}\left(\frac{1}{c_{t}^{2}}-\frac{1}{c_{n+1}^{2}}\right) .
\end{aligned}
$$

这时,

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{1}{a_{i}} & \geq \sum_{i=1}^{n}\left(\frac{1}{c_{i}^{2}}-\frac{1}{c_{n+1}^{2}}\right) \frac{c_{i}^{2}}{a_{i}}=\sum_{i=1}^{n}\left(\frac{4}{9} \sum_{j=i}^{n} \frac{j+1}{T_{j}^{2}}\right) \frac{c_{i}^{2}}{a_{i}} \\
& =\frac{4}{9} \cdot \sum_{i=1}^{n} \sum_{j=i}^{n} \frac{j+1}{T_{j}^{2}} \cdot \frac{c_{i}^{2}}{a_{i}}=\frac{4}{9} \cdot \sum_{j=1}^{n} \sum_{i=1}^{j} \frac{j+1}{T_{j}^{2}} \frac{c_{i}^{2}}{a_{i}} \\
& =\frac{4}{9} \sum_{j=1}^{n} \frac{j+1}{T_{j}^{2}} \sum_{i=1}^{j} \frac{c_{i}^{2}}{a_{i}} \geq \frac{4}{9} \sum_{j=1}^{n} \frac{j+1}{T_{j}^{2}} \frac{\left(\sum_{i=1}^{j} c_{i}\right)^{2}}{\sum_{i=1}^{j} a_{i}} \quad \text { (Cauchy 不等式) } \\
& =\frac{4}{9} \sum_{j=1}^{n} \frac{j+1}{a_{1}+a_{2}+\cdots+a_{j}} .
\end{aligned}
$$

再说明 $a=\frac{4}{9}$ 是最优的.

取 $a_{i}=i(i+1)$, 则

$$
\sum_{i=1}^{n} \frac{1}{a_{i}}=\sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{n+1}
$$

而

$$
\begin{aligned}
& a \sum_{i=1}^{n} \frac{i+1}{a_{1}+\cdots+a_{i}}=3 a \sum_{i=1}^{n} \frac{i+1}{i(i+1)(i+2)} \\
= & 3 a \sum_{i=1}^{n} \frac{1}{i(i+2)}=\frac{3 a}{2} \sum_{i=1}^{n}\left(\frac{1}{i}-\frac{1}{i+2}\right) \\
= & \frac{3 a}{2}\left(1+\frac{1}{2}-\frac{1}{n+1}-\frac{1}{n+2}\right) \\
= & \frac{3 a}{2}\left(\frac{3}{2}-\frac{1}{n+1}-\frac{1}{n+2}\right) .
\end{aligned}
$$

故要使所研究不等式成立, 必须

$$
a \leq \frac{1-\frac{1}{n+1}}{\frac{3}{2}\left(\frac{3}{2}-\frac{1}{n+1}-\frac{1}{n+2}\right)},
$$

令 $n \rightarrow \infty$ 得, $a \leq \frac{4}{9}$, 这就证明了 $\frac{4}{9}$ 是最优的.
综上所述, 满足要求的最大 $a$ 值为 $\frac{4}{9}$.

评注 $\mathrm{A} 8$ 本质上就是: 求最优的正常数 $a$, 使得

$$
\sum_{i=1}^{n} \frac{1}{a_{i}} \geq a \sum_{i=1}^{n} \frac{i+1}{a_{1}+\cdots+a_{i}}
$$

对任意正实数 $a_{1}, a_{2}, \cdots, a_{n}$ 成立. 这和早年 AMM 上的一个问题: 求最优的常数 $a$, 使得

$$
\sum_{i=1}^{n} \frac{1}{a_{i}} \geq a \sum_{i=1}^{n} \frac{i}{a_{1}+\cdots+a_{i}}
$$

十分类似, 但后者的答案是 $\frac{1}{2}$. 请读者细心比较一下它们的异同.

