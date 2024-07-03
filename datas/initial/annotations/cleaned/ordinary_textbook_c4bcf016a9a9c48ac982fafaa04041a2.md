# 关于 Ivan Borsenco 问题的探讨 

吴茁

(湖南省雅礼中学)

指导老师: 许鹏辉

Ivan Borsenco 在 [1] 中提出并证明了如下结论:

定理 1 设 $m, n$ 是正整数, $X=\left\{\left(x_{1}, x_{2}, \cdots, x_{m}\right) \mid x_{i}>0, \sum_{i=1}^{m} x_{i}=1\right\}, Y=$ $\left\{\left(y_{1}, y_{2}, \cdots, y_{m}\right) \left\lvert\, y_{i} \in\left\{0, \frac{1}{n}, \cdots, \frac{n-1}{n}, 1\right\}\right., \sum_{i=1}^{m} y_{i}=1\right\}$, 则对任意 $\left(x_{1}, x_{2}, \cdots, x_{m}\right) \in$ $X$, 存在 $\left(y_{1}, y_{2}, \cdots, y_{m}\right) \in Y$ 使得

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \leq \frac{m}{2 n}
$$

冷岗松老师指出, 如果将上述定理中的正实向量 $\left(x_{1}, x_{2}, \cdots, x_{m}\right)$ 换成一般的实向量, 则有下面的定理:

定理 2 设 $m, n$ 是正整数, $X=\left\{\left(x_{1}, x_{2}, \cdots, x_{m}\right) \mid \sum_{i=1}^{m} x_{i}=1, x_{i} \in \mathbf{R}\right\}$, $Y=\left\{\left(y_{1}, y_{2}, \cdots, y_{m}\right) \mid n y_{i} \in \mathbf{Z}, \sum_{i=1}^{m} y_{i}=1\right\}$, 则对任何 $\left(x_{1}, x_{2}, \cdots, x_{m}\right) \in X$, 存在 $\left(y_{1}, y_{2}, \cdots, y_{m}\right) \in Y$ 使得

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \leq \frac{m}{2 n}
$$

贺嘉帆在求解 Ivan Borsenco 问题时作代换 $a_{i}=n x_{i}, b_{i}=n y_{i}$, 将定理 1 写成了如下富于启发性且更简单的结果:

定理 3 设 $m, n$ 是正整数, $A=\left\{\left(a_{1}, a_{2}, \cdots, a_{m}\right) \mid a_{i}>0, \sum_{i=1}^{m} a_{i}=n\right\}, B=$ $\left\{\left(b_{1}, b_{2}, \cdots, b_{m}\right) \mid b_{i} \in\{0,1, \cdots, n\}, \sum_{i=1}^{m} b_{i}=n\right\}$, 则对任意 $\left(a_{1}, a_{2}, \cdots, a_{m}\right) \in A$, 存在 $\left(b_{1}, b_{2}, \cdots, b_{m}\right) \in B$ 使得

$$
\sum_{i=1}^{m}\left|a_{i}-b_{i}\right| \leq \frac{m}{2}
$$

我们进一步研究了上述问题, 去掉一些无关紧要的量, 得到了下面的结果:

定理 4 设 $m$ 是正整数, $x_{1}, x_{2}, \cdots, x_{m} \in \mathbf{R}$ 且 $\sum_{i=1}^{m} x_{i} \in \mathbf{Z}$, 则存在整数 $y_{1}, y_{2}, \cdots, y_{m}$ 使得

$$
\sum_{i=1}^{m} y_{i}=\sum_{i=1}^{m} x_{i} \quad \text { 且 } \quad \sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \leq \frac{m}{2} .
$$

进一步, 我们研究了上面估计的最优性, 最终证明了如下结果:

定理 5 给定正整数 $m$, 则对任意满足 $\sum_{i=1}^{m} x_{i} \in \mathbf{Z}$ 的实数 $x_{1}, x_{2}, \cdots, x_{m}$, 总存在 $m$ 个整数 $y_{1}, y_{2}, \cdots, y_{m}$ 满足

$$
\sum_{i=1}^{m} y_{i}=\sum_{i=1}^{m} x_{i} \quad \text { 且 } \quad \sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \leq C(m)
$$

的最小 $C(m)$ 的值为:

$$
C(m)= \begin{cases}\frac{m}{2}, & \text { 当 } m \text { 为偶数, } \\ \frac{m^{2}-1}{2 m}, & \text { 当 } m \text { 为奇数. }\end{cases}
$$

证明 首先证明存在满足条件的整数 $y_{1}, y_{2}, \cdots, y_{m}$.

记 $a_{i}=\left\lfloor x_{i}\right\rfloor, b_{i}=\left\{x_{i}\right\}, i=1,2, \cdots, m$. 则 $x_{i}=a_{i}+b_{i}$. 这时由 $\sum_{i=1}^{m} x_{i} \in \mathbf{Z}$ 知 $\sum_{i=1}^{m} b_{i}=\sum_{i=1}^{m} x_{i}-\sum_{i=1}^{m} a_{i} \in \mathbf{Z}$.

记 $k=\sum_{i=1}^{m} b_{i}$, 注意到 $b_{i} \geq 0$, 故 $k$ 是非负整数. 如果 $k=0$, 结论是平凡的. 因此我们仅须考察 $k$ 是正整数的情况.

不妨设 $b_{1} \geq b_{2} \geq \cdots, b_{m}$. 令

$$
y_{i}= \begin{cases}a_{i}+1, & i=1,2, \cdots, k \\ a_{i}, & i=k+1, \cdots, m .\end{cases}
$$

下证这样的整数 $y_{i}, i=1,2, \cdots, m$ 满足要求. 事实上,

$$
\sum_{i=1}^{m} y_{i}=k+\sum_{i=1}^{m} a_{i}=\sum_{i=1}^{m} b_{i}+\sum_{i=1}^{m} a_{i}=\sum_{i=1}^{m} x_{i} .
$$

另一方面, 由 $b_{1} \geq b_{2} \geq \cdots \geq b_{m}$ 可得

$$
\begin{gathered}
\sum_{i=1}^{k} b_{i} \geq \frac{k}{m} \sum_{i=1}^{m} b_{i}=\frac{k^{2}}{m} \\
\sum_{i=k+1}^{m} b_{i} \leq \frac{m-k}{m} \sum_{i=1}^{m} b_{i}=\frac{(m-k) k}{m}
\end{gathered}
$$

故

$$
\begin{aligned}
\sum_{i=1}^{m}\left|x_{i}-y_{i}\right| & =\sum_{i=1}^{k}\left(1-b_{i}\right)+\sum_{i=k+1}^{m} b_{i} \\
& =k+\sum_{i=k+1}^{m} b_{i}-\sum_{i=1}^{k} b_{i} \\
& \leq k+\frac{(m-k) k}{m}-\frac{k^{2}}{m} \\
& =2 \cdot \frac{k(m-k)}{m}
\end{aligned}
$$

又注意到

$$
k(m-k) \leq \begin{cases}\frac{m^{2}}{4}, & \text { 当 } m \text { 为偶数 }, \\ \frac{(m+1)(m-1)}{4}, & \text { 当 } m \text { 为奇数. }\end{cases}
$$

因此

$$
\sum_{i=1}^{m}\left|x_{i}-y_{i}\right| \leq C(m)= \begin{cases}\frac{m}{2}, & \text { 当 } m \text { 为偶数, } \\ \frac{m^{2}-1}{2 m}, & \text { 当 } m \text { 为奇数. }\end{cases}
$$

下面说明 $C(m)$ 的最优性.

(1) 当 $m$ 为偶数时:

取 $x_{i}=\frac{1}{2}, i=1,2, \cdots, m$, 则 $\sum_{i=1}^{m} x_{i}=\frac{m}{2} \in \mathbf{Z}$, 且对于任意 $y_{i} \in \mathbf{Z}$, 有

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right|=\sum_{i=1}^{m}\left|y_{i}-\frac{1}{2}\right| \geq \sum_{i=1}^{m} \frac{1}{2}=\frac{m}{2}
$$

故此时 $\frac{m}{2}$ 是最优的.

(2) 当 $m$ 为奇数时:

取 $x_{i}=\frac{m-1}{2 m}, i=1,2, \cdots, m$, 则 $\sum_{i=1}^{m} x_{i}=\frac{m-1}{2} \in \mathbf{Z}$,

i) 若所有的 $y_{i}(1 \leq i \leq m)$ 都属于 $\{0,1\}$, 则由 $\sum_{i=1}^{m} y_{i}=\sum_{i=1}^{m} x_{i}$ 知 $y_{i}$ 中恰有 $\frac{m-1}{2}$
个 1 , 这时

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right|=\frac{m-1}{2}\left(1-\frac{m-1}{2 m}\right)+\frac{m+1}{2} \cdot \frac{m-1}{2 m}=\frac{m^{2}-1}{2 m}
$$

ii) 若存在 $y_{i}(1 \leq i \leq m)$ 不属于 $\{0,1\}$, 不妨设 $y_{1} \notin\{0,1\}$. 注意到 $y_{1}$ 是整数且 $y_{1} \leq-1$ 或 $y_{1} \geq 2$ 有

$$
\left|y_{1}-\frac{m-1}{2 m}\right| \geq \frac{m-1}{2 m}+1
$$

故

$$
\begin{aligned}
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right| & =\left|y_{1}-x_{1}\right|+\sum_{i=2}^{m}\left|y_{i}-x_{i}\right| \\
& \geq\left|y_{1}-\frac{m-1}{2 m}\right|+\frac{m-1}{2 m} \cdot(m-1) \\
& \geq \frac{m-1}{2 m}+1+\frac{m-1}{2 m} \cdot(m-1) \\
& =\frac{m+1}{2} \\
& >\frac{m^{2}-1}{2 m} .
\end{aligned}
$$

这说明此时 $\frac{m^{2}-1}{2 m}$ 是最优的.

综上, 所求的最优值为 $C(m)$.

致谢谢谢我的两位师兄贺嘉帆, 谢昌志(2015年国家队队员)的指点和帮助.

## 参考文献

[1] Ivan Borsenco, Olympiad Problem O240, Math. Refl., 4(2012).

