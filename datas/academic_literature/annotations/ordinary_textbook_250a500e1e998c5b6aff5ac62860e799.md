# 一个复数不等式的证明 

李师铨

(湖南省雅礼中学, 410007)

数学新星问题征解第十二期中刊登了如下问题:

问题. 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是实数, 证明:

$$
\left(\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|\right)^{2} \geq(n-1) \sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|^{2}
$$

冷岗松教授猜想不等式 (1) 对复数 $x_{1}, x_{2}, \cdots, x_{n}$ 也成立, 我们证明了这个猜想, 得到如下结论:

命题. 设 $z_{1}, z_{2}, \cdots, z_{n} \in \mathbb{C}, n \geq 2$, 则

$$
\left(\sum_{1 \leq i<j \leq n}\left|z_{i}-z_{j}\right|\right)^{2} \geq(n-1) \sum_{1 \leq i<j \leq n}\left|z_{i}-z_{j}\right|^{2}
$$

证明 记 $w_{i}=z_{i}-z_{i-1}, i=1,2, \cdots, n$, 其中 $z_{0}=0$. 则 $z_{i}=\sum_{j=1}^{i} w_{j}$, 且

$$
\begin{gathered}
\left(\sum_{1 \leq i<j \leq n}\left|z_{i}-z_{j}\right|\right)^{2}=\left(\sum_{1 \leq i<j \leq n}\left|w_{j}+\cdots+w_{i+1}\right|\right)^{2} ; \\
(n-1)\left(\sum_{1 \leq i<j \leq n}\left|z_{i}-z_{j}\right|\right)^{2}=(n-1)\left(\sum_{1 \leq i<j \leq n}\left|w_{j}+\cdots+w_{i+1}\right|\right)^{2} .
\end{gathered}
$$

我们证明, 对任意固定的 $\left(j_{0}, i_{0}\right)\left(1 \leq i_{0}<j_{0} \leq n\right)$, 有

$$
\begin{gathered}
\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|\left(\sum_{1 \leq i<j \leq n}\left|w_{j}+\cdots+w_{i+1}\right|\right) \\
\geq(n-1)\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|^{2} .
\end{gathered}
$$

再将 (3) 式两边关于不同的 $\left(j_{0}, i_{0}\right)\left(1 \leq i_{0}<j_{0} \leq n\right)$ 求和, 便得到不等式 (2).

注意到 (3) 等价于

$$
\sum_{1 \leq i<j \leq n}\left|w_{j}+\cdots+w_{i+1}\right| \geq(n-1)\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|
$$

我们采用配对及三角不等式来证明 (4) 式.

首先, 将 $\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|$ 单独配成一对, 有

$$
\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right| \geq\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|
$$

对于 $2 \leq k \leq i_{0}\left(k \in \mathbb{N}_{+}\right)$, 将 $\left|w_{j_{0}}+\cdots+w_{k}\right|$ 与 $\left|w_{i_{0}}+\cdots+w_{k}\right|$ 配成一对,有

$$
\left|w_{j_{0}}+\cdots+w_{k}\right|+\left|w_{i_{0}}+\cdots+w_{k}\right| \geq\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|
$$

这样的对子有 $i_{0}-1$ 对;

对于 $i_{0}+1 \leq k \leq j_{0}-1\left(k \in \mathbb{N}_{+}\right)$, 将 $\left|w_{j_{0}}+\cdots+w_{k+1}\right|$ 与 $\left|w_{k}+\cdots+w_{i_{0}+1}\right|$配成一对, 有

$$
\left|w_{j_{0}}+\cdots+w_{k+1}\right|+\left|w_{k}+\cdots+w_{i_{0}+1}\right| \geq\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|
$$

这样的对子有 $j_{0}-i_{0}-1$ 对;

对于 $j_{0}+1 \leq k \leq n\left(k \in \mathbb{N}_{+}\right)$, 将 $\left|w_{k}+\cdots+w_{j_{0}+1}\right|$ 与 $\left|w_{k}+\cdots+w_{i_{0}+1}\right|$ 配成一对, 有

$$
\left|w_{k}+\cdots+w_{j_{0}+1}\right|+\left|w_{k}+\cdots+w_{i_{0}+1}\right| \geq\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|
$$

这样的对子有 $n-j_{0}$ 对.

按上面所叙述的方法, 我们将 $\sum_{1 \leq i<j \leq n}\left|w_{j}+\cdots+w_{i+1}\right|$ 中的项不重复 (可能遗漏) 地配成 $1+i_{0}-1+j_{0}-i_{0}-1+n-j_{0}=n-1$ 对, 每对均不小于 $\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|$, 从而有

$$
\sum_{1 \leq i<j \leq n}\left|w_{j}+\cdots+w_{i+1}\right| \geq(n-1)\left|w_{j_{0}}+\cdots+w_{i_{0}+1}\right|
$$

即 (4) 成立, 从而不等式 (2) 得证.

