# 再谈范数不等式 

冷岗松

在文 [1] 中, 我们介绍了范数不等式的意义及证明.

意犹未尽, 这篇短文里我们继续讨论一下范数不等式和幂平均不等式的关系.

所谓范数不等式是：设 $a_{1}, a_{2}, \cdots, a_{n}$ 是非负实数, 若 $0<r<s$, 则

$$
\left(\sum_{i=1}^{n} a_{i}^{s}\right)^{\frac{1}{s}} \leq\left(\sum_{i=1}^{n} a_{i}^{r}\right)^{\frac{1}{r}}
$$

等号当且仅当 $a_{1}, a_{2}, \cdots, a_{n}$ 中至少有 $n-1$ 个为零时成立.

所谓幂平均不等式是: 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是非负实数, 若 $0<r<s$, 则

$$
\left(\frac{\sum_{i=1}^{n} a_{i}^{s}}{n}\right)^{\frac{1}{s}} \geq\left(\frac{\sum_{i=1}^{n} a_{i}^{r}}{r}\right)^{\frac{1}{r}}
$$

等号成立当且仅当所有的 $a_{i}$ 都相等.

幂平均不等式说明如果把幂平均看作幂指数的函数, 则它是递增的.

我们指出: 范数不等式和幂平均不等式是一对反向不等式.

为了更好地看出这一点, 我们可把它们写在一个统一的命题中.

定理 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是非负实数且不全为零, 若 $0<r<s$, 则

$$
1 \leq \frac{\left(\sum_{i=1}^{n} a_{i}^{r}\right)^{\frac{1}{r}}}{\left(\sum_{i=1}^{n} a_{i}^{s}\right)^{\frac{1}{s}}} \leq n^{\frac{1}{r}-\frac{1}{s}}
$$

左侧等号成立当且仅当 $a_{1}, a_{2}, \cdots, a_{n}$ 中至少有 $n-1$ 个为零, 而右侧等号当且仅当所有的 $a_{i}$ 都相等时成立.

既然这是一对反向不等式, 我们一般会认为解决一个不等式时不可能同时用这两个 “冤家” . 但令人惊讶的是, 确有这样一个不等式证明需要同时多次用这两个不等式. 这个不等式被称作逆 Minkowski 不等式, 最先是 Tôyama 证明的 (详见[2]). Alzer 在 [3] 中给出了它的一个简单证明及加权版本, 它被我们用做 2012 年中国国家集训队测试题 (Alzer 等人文中的证明稍有缺陷, 被复旦大学的姚一隽教授订正).

问题 设 $m, n$ 是两个给定的大于 1 的整数, $r<s$ 是两个给定的正实数. 对任意不全
为 0 的非负实数 $a_{i j}(i=1,2, \cdots, m ; j=1,2, \cdots, n)$, 求

$$
f=\frac{\left[\sum_{j=1}^{n}\left(\sum_{i=1}^{m} a_{i j}^{s}\right)^{\frac{r}{s}}\right]^{\frac{1}{r}}}{\left[\sum_{i=1}^{m}\left(\sum_{j=1}^{n} a_{i j}^{r}\right)^{\frac{s}{r}}\right]^{\frac{1}{s}}}
$$

的最大值.

解 $f$ 的最大值为 $(\min \{m, n\})^{\frac{1}{r}-\frac{1}{s}}$.

令

$$
x_{j}=\left(\sum_{i=1}^{m} a_{i j}^{s}\right)^{\frac{1}{s}}, j=1,2, \cdots, n ; \quad y_{i}=\left(\sum_{j=1}^{n} a_{i j}^{r}\right)^{\frac{1}{r}}, i=1,2, \cdots, m .
$$

由范数不等式 (1) 得

$$
x_{j}^{r} \leq \sum_{i=1}^{m} a_{i j}^{r}, \quad j=1,2, \cdots, n
$$

再将此式结合幂平均不等式 (2) 可知

$$
\begin{aligned}
\left(\sum_{j=1}^{n} x_{j}^{r}\right)^{\frac{1}{r}} & \leq\left(\sum_{j=1}^{n} \sum_{i=1}^{m} a_{i j}^{r}\right)^{\frac{1}{r}} \\
& =\left(\frac{1}{m} \sum_{i=1}^{m} y_{i}^{r}\right)^{\frac{1}{r}} \cdot m^{\frac{1}{r}} \\
& \leq\left(\frac{1}{m} \sum_{i=1}^{m} y_{i}^{s}\right)^{\frac{1}{s}} \cdot m^{\frac{1}{r}} \\
& =\left(\sum_{i=1}^{m} y_{i}^{s}\right)^{\frac{1}{s}} \cdot m^{\frac{1}{r}-\frac{1}{s}} .
\end{aligned}
$$

又由幂平均不等式 (2) 和范数不等式 (1) 可知

$$
\begin{aligned}
\left(\sum_{j=1}^{n} x_{j}^{r}\right)^{\frac{1}{r}} & =\left(\frac{1}{n} \sum_{j=1}^{n} x_{j}^{r}\right)^{\frac{1}{r}} \cdot n^{\frac{1}{r}} \\
& \leq\left(\frac{1}{n} \sum_{j=1}^{n} x_{j}^{s}\right)^{\frac{1}{s}} \cdot n^{\frac{1}{r}} \\
& =\left(\sum_{j=1}^{n} \sum_{i=1}^{m} a_{i j}^{s}\right)^{\frac{1}{s}} \cdot n^{\frac{1}{r}-\frac{1}{s}} \\
& \leq\left(\sum_{i=1}^{m}\left(\sum_{j=1}^{n} a_{i j}^{r}\right)^{\frac{s}{r}}\right)^{\frac{1}{s}} \cdot n^{\frac{1}{r}-\frac{1}{s}} \\
& =\left(\sum_{i=1}^{m} y_{i}^{s}\right)^{\frac{1}{s}} \cdot n^{\frac{1}{r}-\frac{1}{s}} .
\end{aligned}
$$

所以

$$
f=\frac{\left(\sum_{j=1}^{n} x_{j}^{r}\right)^{\frac{1}{r}}}{\left(\sum_{i=1}^{m} y_{i}^{s}\right)^{\frac{1}{s}}} \leq(\min \{m, n\})^{\frac{1}{r}-\frac{1}{s}}
$$

当 $a_{i i}=1(i=1,2, \cdots, \min \{m, n\})$, 其他所有的 $a_{i i}=0$ 时, 上式等号成立. 故 $f$ 的最大值为 $(\min \{m, n\})^{\frac{1}{r}-\frac{1}{s}}$.

这是一个中等难度的问题, 当年的国家集训队队员有将近一半的同学得了满分.

## 参考文献

[1] 冷岗松, 关于正齐次不等式, 数学新星网/www.nsmath.cn.

[2] H. Tôyama, On the inequality of Ingham and Jessen, Proc. Japan Acad. 24(1948). no. 9, 10-12.

[3] H. Alzer and S. Ruscheweyh, A converse of Minkowski's inequality, Discrete Math. 216(2000), 253-256.

