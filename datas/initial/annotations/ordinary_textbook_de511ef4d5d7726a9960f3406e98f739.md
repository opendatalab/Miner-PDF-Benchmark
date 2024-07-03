# 一道 IMC 试题的推广 

鲁一逍

(上海市上海中学, 200231)

2006 年 IMC (国际大学生数学竞赛) 中有一道有趣的代数不等式试题, 它本质上可叙述为:

定理 1. 设 $(a, b, c)$ 和 $(d, e)$ 分别是一个三维实向量和一个二维实向量, 满足

$$
\left\{\begin{array}{l}
a^{2}+b^{2}+c^{2}=d^{2}+e^{2} \\
a^{4}+b^{4}+c^{4}=d^{4}+e^{4}
\end{array}\right.
$$

则 $|a|^{3}+|b|^{3}+|c|^{3} \leq|d|^{3}+|e|^{3}$.

对于定理 1 , 一个自然的问题是对 $n$ 维 $(n \geq 3)$ 实向量 $\left(x_{1}, \cdots, x_{n}\right)$ 和 $n-1$维实向量 $\left(y_{1}, y_{2}, \cdots, y_{n-1}\right)$ 是否有类似的结论呢? 也就是:

问题 1. 若 $n$ 维 $(n \geq 3)$ 实向量 $\left(x_{1}, \cdots, x_{n}\right)$ 和 $n-1$ 维实向量 $\left(y_{1}, y_{2}, \cdots, y_{n-1}\right)$满足

$$
\left\{\begin{array}{l}
x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=y_{1}^{2}+y_{2}^{2}+\cdots+y_{n-1}^{2} ; \\
x_{1}^{4}+x_{2}^{4}+\cdots+x_{n}^{4}=y_{1}^{4}+y_{2}^{4}+\cdots+y_{n-1}^{4},
\end{array}\right.
$$

是否一定有

$$
\left|x_{1}\right|^{3}+\left|x_{2}\right|^{3}+\cdots+\left|x_{n}\right|^{3} \leq\left|y_{1}\right|^{3}+\left|y_{2}\right|^{3}+\cdots+\left|y_{n-1}\right|^{3} ?
$$

可惜答案是否定的. 例如当 $n \geq 4$ 时, 下面的 $n$ 维实向量 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 和 $n-1$ 维实向量 $\left(y_{1}, y_{2}, \cdots, y_{n-1}\right)$ 就是反例:

$$
\begin{aligned}
& x_{1}=x_{2}=\sqrt{3}, \quad x_{3}=x_{4}=\cdots=x_{n}=0 \\
& y_{1}=y_{2}=1, \quad y_{3}=2, \quad y_{4}=\cdots=y_{n-1}=0 .
\end{aligned}
$$

但对于一般的 $n$ 维 $(n \geq 3)$ 实向量和二维实向量, 我们则有正面的回答, 即:

收稿日期: 2016-05-23; 修订日期: 2016-06-18;
定理 2. 设 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 是一个 $n$ 维 $(n \geq 3)$ 实向量, $\left(y_{1}, y_{2}\right)$ 是一个二维实向量, 且满足

$$
\left\{\begin{array}{l}
\left|x_{1}\right|^{t}+\left|x_{2}\right|^{t}+\cdots+\left|x_{n}\right|^{t}=\left|y_{1}\right|^{t}+\left|y_{2}\right|^{t} \\
\left|x_{1}\right|^{s}+\left|x_{2}\right|^{s}+\cdots+\left|x_{n}\right|^{s}=\left|y_{1}\right|^{s}+\left|y_{2}\right|^{s}
\end{array}\right.
$$

其中 $s>t>0$, 则对任意 $\lambda \in[t, s]$ 有

$$
\left|x_{1}\right|^{\lambda}+\left|x_{2}\right|^{\lambda}+\cdots+\left|x_{n}\right|^{\lambda} \leq\left|y_{1}\right|^{\lambda}+\left|y_{2}\right|^{\lambda} .
$$

证明 显然不妨设所有变元 $x_{1}, \cdots, x_{n}, y_{1}, y_{2}$ 均非负.

再不妨设 $t=1$, 否则可用 $x_{1}^{t}, x_{2}^{t}, \cdots, x_{n}^{t}, y_{1}^{t}, y_{2}^{t}$ 替代 $x_{1}, x_{2}, \cdots, x_{n}, y_{1}, y_{2}$, 再用 $\frac{s}{t}$ 替代 $s$ 便可. 这时条件 $(*)$ 变为

$$
\left\{\begin{array}{l}
x_{1}+x_{2}+\cdots+x_{n}=y_{1}+y_{2} \\
x_{1}^{s}+x_{2}^{s}+\cdots+x_{n}^{s}=y_{1}^{s}+y_{2}^{s}
\end{array}\right.
$$

其中 $s>1$.

这样问题转化为证明对任何 $\lambda \in[1, s]$, 有

$$
x_{1}^{\lambda}+x_{2}^{\lambda}+\cdots+x_{n}^{\lambda} \leq y_{1}^{\lambda}+y_{2}^{\lambda} .
$$

我们首先证明下面的引理.

引理 设 $n$ 维 $(n \geq 3)$ 实向量 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ 和 2 维实向量 $\left(y_{1}, y_{2}\right)$ 满足条件 $(1),(2)$, 则

$$
\max \left\{x_{1}, x_{2}, \cdots, x_{n}\right\} \geq \max \left\{y_{1}, y_{2}\right\}
$$

引理的证明 不妨设

$$
0 \leq x_{1} \leq x_{2} \leq \cdots \leq x_{n}, 0 \leq y_{1} \leq y_{2} .
$$

这样我们仅须证明 $x_{n} \geq y_{2}$.

用反证法. 假设 $x_{n}<y_{2}$, 由齐次性, 不妨设 $y_{2}=1$. 于是

$$
0 \leq x_{1} \leq x_{2} \leq \cdots \leq x_{n} \leq 1
$$

现考虑函数 $f(x)=x-x^{s}, x \in[0,1]$, 将 (1), (2) 两式相减便得

$$
f\left(x_{1}\right)+f\left(x_{2}\right)+\cdots+f\left(x_{n}\right)=f\left(y_{1}\right) .
$$

因 $s>1$, 所以

$$
f^{\prime \prime}(x)=-s(s-1) x^{s-2}<0, \quad \forall x \in(0,1) .
$$

这说明 $f(x)$ 是 $[0,1]$ 上的严格凹函数.

再注意到 $x_{1}+x_{2}+\cdots+x_{n}=y_{1}+1$ 及 $x_{n}<1$, 因此

$$
(1, y_{1}, \underbrace{0, \cdots, 0}_{n-1 \uparrow}) \succ\left(x_{n}, x_{n-1}, \cdots, x_{1}\right) .
$$

故由 Karamata 不等式 (也称控制不等式) 可得

$$
f\left(x_{1}\right)+f\left(x_{2}\right)+\cdots+f\left(x_{n}\right)>f(1)+f\left(y_{1}\right)+(n-2) f(0) .
$$

亦即 $f\left(x_{1}\right)+f\left(x_{2}\right)+\cdots+f\left(x_{n}\right)>f\left(y_{1}\right)$, 这与 (3) 式矛盾! 引理证完.

回到原题. 由齐次性不妨设 $x_{n}=1$, 且不妨设 $x_{1}, \cdots, x_{n-2}$ 中总有正数.

这时由 (1) 和引理可得 $y_{1}-x_{n-1}=x_{1}+\cdots+x_{n-2}+\left(x_{n}-y_{2}\right)>0$. 故

$$
y_{1}>x_{n-1} \text {. }
$$

记

$$
g(x)=x_{1}^{x}+x_{2}^{x}+\cdots+x_{n-1}^{x}-y_{1}^{x}-y_{2}^{x},
$$

则 $g(x)$ 可导且 $g(1)=g(s)=-1$.

故由洛尔定理知存在 $x_{0} \in(1, s)$ 使得 $g^{\prime}\left(x_{0}\right)=0$. 即

$$
x_{1}^{x_{0}} \ln x_{1}+\cdots+x_{n-1}^{x_{0}} \ln x_{n-1}-y_{1}^{x_{0}} \ln y_{1}-y_{2}^{x_{0}} \ln y_{2}=0 .
$$

再注意到 $\ln x_{1}, \cdots, \ln x_{n-1}, \ln y_{1}, \ln y_{2}$ 均为负数, 由 (4), (5) 便知对 $x>x_{0}$ 有

$$
\begin{aligned}
-y_{1}^{x} \ln y_{1}-y_{2}^{x} \ln y_{2} & >y_{1}^{x-x_{0}}\left(-y_{1}^{x_{0}} \ln y_{1}-y_{2}^{x_{0}} \ln y_{2}\right) \\
& >\left(-x_{1}^{x_{0}} \ln x_{1}-\cdots-x_{n-1}^{x_{0}} \ln x_{n-1}\right) x_{n-1}^{x-x_{0}} \\
& >-x_{1}^{x} \ln x_{1}-\cdots-x_{n-1}^{x} \ln x_{n-1} .
\end{aligned}
$$

设 $x=\left(x_{1}, x_{2}, \cdots, x_{n}\right), y=\left(y_{1}, y_{2}, \cdots, y_{n}\right)$ 是两个 $n$ 维向量, 满足

$$
x_{1}+x_{2}+\cdots+x_{n}=y_{1}+y_{2}+\cdots+y_{n} .
$$

将 $x, y$ 重排, 使得 $x_{1} \geq x_{2} \geq \cdots \geq x_{n}, y_{1} \geq y_{2} \geq \cdots \geq y_{n}$, 若此时满足

$$
x_{1}+x_{2}+\cdots+x_{k} \geq y_{1}+y_{2}+\cdots+y_{k}, \quad k=1,2, \cdots, n-1 .
$$

则称 $x$ 控制 $y$. 记作 $x \succ y$ 或 $\left(x_{1}, x_{2}, \cdots, x_{n}\right) \succ\left(y_{1}, y_{2}, \cdots, y_{n}\right)$.则

Karamata 不等式 设 $\varphi$ 是区间 $I$ 上的实值凸函数, 若 $\left(x_{1}, x_{2}, \cdots, x_{n}\right) \succ\left(y_{1}, y_{2}, \cdots, y_{n}\right)$,

$$
\sum_{i=1}^{n} \varphi\left(x_{i}\right) \geq \sum_{i=1}^{n} \varphi\left(y_{i}\right)
$$

且当 $\varphi$ 是严格凸函数时, 等号取到当且仅当 $x_{i}=y_{i},(i=1,2, \cdots, n)$. 这里 $x_{i}, y_{i} \in I$.

当 $\varphi$ 是凹函数时, 不等式符号反向.
这说明对任意 $x>x_{0}$ 有 $g^{\prime}(x)>0$.

同理对任意 $x<x_{0}$ 有 $g^{\prime}(x)<0$.

这说明在 $\left[1, x_{0}\right]$ 上 $g(x)$ 单调递减, 在 $\left(x_{0}, s\right]$ 上单调递增.

因此当 $1<\lambda<s$ 时, 总有 $g(\lambda)<g(1)$ 或 $g(\lambda)<g(s)$. 故 $g(\lambda)<-1$. 亦即

$$
x_{1}^{\lambda}+x_{2}^{\lambda}+\cdots+x_{n-1}^{\lambda}-y_{1}^{\lambda}-y_{2}^{\lambda}<-1 .
$$

这就是

$$
x_{1}^{\lambda}+x_{2}^{\lambda}+\cdots+x_{n-1}^{\lambda}+x_{n}^{\lambda}<y_{1}^{\lambda}+y_{2}^{\lambda}
$$

对所有 $\lambda \in[1, s]$ 均成立. 定理证完.

注意由本文的结果还可进一步推出在同样的条件下对 $\lambda \in[s,+\infty)$, 我们有

$$
x_{1}^{\lambda}+x_{2}^{\lambda}+\cdots+x_{n}^{\lambda} \geq y_{1}^{\lambda}+y_{2}^{\lambda} .
$$

致谢 本文是在冷岗松教授的精心指导下完成, 在此致谢!

