# 一道罗马尼亚不等式试题的新证明 

冷岗松

2004 年罗马尼亚国家队选拔考试 (Rom TST) 的 20 道试题中, 有四道题为 Gabriel Dospinescu 提供, 他当时还是著名的法国巴黎高等师范学校 (Ecole Normale Superieure) 数学系的学生 (现在是该校的教师了). 其中有一道带点组合味的代数不等式试题:

问题 (Rom TST, 2004) 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是实数, $S$ 是 $\{1,2, \cdots, n\}$ 的非空子集. 证明:

$$
\left(\sum_{i \in S} a_{i}\right)^{2} \leq \sum_{1 \leq i \leq j \leq n}\left(a_{i}+\cdots+a_{j}\right)^{2}
$$

(Gabriel Dospinescu)

这个问题的解法写起来很棘手, 我们最先见到的标准答案似乎太像一个证明梗要. 最近, Gabriel Dospinescu 和 Titu Andreescu 合著的书 [1, p.38-39] 中提供了一个详细的证明, 现介绍如下:

解法一 令 $s_{i}=a_{1}+a_{2}+\cdots+a_{i}, i=1,2, \cdots, n$, 并约定 $s_{0}=0$. 现将 $S$ 按由小到大划分成若干连续整数的段, 则 $\sum_{i \in S} a_{i}$ 可写为下面的形式:

$$
s_{j_{1}}-s_{i_{1}}+s_{j_{2}}-s_{i_{2}}+\cdots+s_{j_{k}}-s_{i_{k}},
$$

其中 $0 \leq i_{1}<i_{2}<\cdots<i_{k} \leq n, j_{1}<j_{2}<\cdots<j_{k}$ 且有 $i_{1}<j_{1}, \cdots, i_{k}<j_{k}$. 又不等式 $(*)$ 的右边可写为

$$
\sum_{i=1}^{n} s_{i}^{2}+\sum_{1 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2}=\sum_{0 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2}
$$

因此, 要证 $(*)$, 我们仅需证明

$$
\left(s_{j_{1}}-s_{i_{1}}+s_{j_{2}}-s_{i_{2}}+\cdots+s_{j_{k}}-s_{i_{k}}\right)^{2} \leq \sum_{0 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2}
$$

再令 $a_{1}=s_{i_{1}}, a_{2}=s_{j_{1}}, \cdots, a_{2 k-1}=s_{i_{k}}, a_{2 k}=s_{j_{k}}$, 并注意到一个明显的 $($ 但是重要的) 不等式

$$
\sum_{0 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2} \geq \sum_{1 \leq i<j \leq 2 k}\left(a_{i}-a_{j}\right)^{2}
$$

这样, 要证 (1), 我们仅需证明:

$$
\left(a_{1}-a_{2}+a_{3}-\cdots+a_{2 k-1}-a_{2 k}\right)^{2} \leq \sum_{1 \leq i<j \leq 2 k}\left(a_{i}-a_{j}\right)^{2}
$$

下证 (2) 式:

用 $k$ 次 Cauchy 不等式可得

$$
\left\{\begin{array}{l}
\left(a_{1}-a_{2}+a_{3}-\cdots+a_{2 k-1}-a_{2 k}\right)^{2} \leq k\left(\left(a_{1}-a_{2}\right)^{2}+\left(a_{3}-a_{4}\right)^{2}+\cdots+\left(a_{2 k-1}-a_{2 k}\right)^{2}\right) \\
\left(a_{1}-a_{2}+a_{3}-\cdots+a_{2 k-1}-a_{2 k}\right)^{2} \leq k\left(\left(a_{1}-a_{4}\right)^{2}+\left(a_{3}-a_{6}\right)^{2}+\cdots+\left(a_{2 k-1}-a_{2}\right)^{2}\right) \\
\cdots \\
\left(a_{1}-a_{2}+a_{3}-\cdots+a_{2 k-1}-a_{2 k}\right)^{2} \leq k\left(\left(a_{1}-a_{2 k}\right)^{2}+\left(a_{3}-a_{2}\right)^{2}+\cdots+\left(a_{2 k-1}-a_{2 k-2}\right)^{2}\right)
\end{array}\right.
$$

将上面 $k$ 个不等式相加, 约去 $k$ 后所得的右边显然不超过 $\sum_{1 \leq i<j \leq 2 k}\left(a_{i}-a_{j}\right)^{2}$, 这就完成了 (2) 式的证明.

下面介绍我们的新证明, 这个证明早在 2006 年就得到了.

解法二 记 $s_{i}=a_{1}+a_{2}+\cdots+a_{i}, i=1,2, \cdots, n$, 并约定 $s_{0}=0$. 对求和下标作平移变换知右边可写为

$$
\sum_{1 \leq i<j \leq n}\left(s_{j}-s_{i-1}\right)^{2}=\sum_{0 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2} .
$$

这样, 要证的不等式等价于

$$
\left(\sum_{i \in S}\left(s_{i}-s_{i-1}\right)\right)^{2} \leq \sum_{0 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2}
$$

注意到 (3) 式的左右两边关于 $s_{0}, s_{1}, \cdots, s_{n}$ 是平移不变的, 即用 $s_{i}-\frac{s_{0}+\cdots+s_{n}}{n+1}(i=$ $0,1, \cdots, n)$ 代替 $s_{i}$, 不等式不变. 因此不妨设 $s_{0}+s_{1}+\cdots+s_{n}=0$.

对任意 $S \subseteq\{1,2, \cdots, n\}$, 总可设

$$
\sum_{i \in S}\left(s_{i}-s_{i-1}\right)=\sum_{i=0}^{n} \lambda_{i} s_{i}
$$

其中 $\lambda_{i}=0, \pm 1$.

故要证 (3) 式, 只须证明:

$$
\left(\sum_{i=0}^{n} \lambda_{i} s_{i}\right)^{2} \leq \sum_{0 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2}
$$

事实上, (5) 式等价于

$$
\left(\sum_{i=0}^{n} \lambda_{i} s_{i}\right)^{2} \leq(n+1)\left(s_{0}^{2}+s_{1}^{2}+\cdots+s_{n}^{2}\right)-\left(s_{0}+s_{1}+\cdots+s_{n}\right)^{2}
$$

亦即

$$
\left(\sum_{i=0}^{n} \lambda_{i} s_{i}\right)^{2} \leq(n+1)\left(s_{0}^{2}+s_{1}^{2}+\cdots+s_{n}^{2}\right)
$$

这只要用 Cauchy 不等式并注意到 $\sum_{i=0}^{n} \lambda_{i}^{2} \leq n+1$ 立得上式成立. 故 (5) 式正确.

上面解法的关键是写出 (4) 式, 这是高明的形式设定. 这个想法源于当时湖南省雅礼中学的学生程有兴.

另一个值得注意的是尽管 $s_{0}=0,(3)$ 式却是关于 $s_{0}, s_{1}, \cdots, s_{n}$ 是平移不变的, 并不是关于 $s_{1}, s_{2}, \cdots, s_{n}$ 是平移不变的. 因此比 (3) 式弱的不等式

$$
\left(\sum_{i \in S}\left(s_{i}-s_{i-1}\right)\right)^{2} \leq \sum_{1 \leq i<j \leq n}\left(s_{j}-s_{i}\right)^{2}
$$

是不对的. 湖南师大附中的羊明亮老师特别提醒我们注意这一点, 这是很容易犯错误的.

## 参考文献

[1] Titu Andreescu, Gabriel Dospinescu, Problems from the Book, XYZ Press, LLC, 2008.

