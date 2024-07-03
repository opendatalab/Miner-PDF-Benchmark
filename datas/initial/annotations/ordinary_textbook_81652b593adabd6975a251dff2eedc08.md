数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2023 年百年老校竞赛不等式的来由与推广 

## 市乐刽

(福建省福州外国语学校, 350007)

指导教师: 卢伟

在 2023 年 8 月 2 日的百年老校数学竞赛第一天的考试第一题如下:

题 1 已知正实数 $x, y, z$ 满足 $x y z=1$. 证明:

$$
\frac{1}{1+x+y^{2}}+\frac{1}{1+y+z^{2}}+\frac{1}{1+z+x^{2}} \leq 1
$$

王彬老师对此题作了如下推广:

题 2 在题 1 的条件下，对 $0 \leq \alpha \leq \beta \leq \gamma \leq 2 \beta$, 证明:

$$
\sum_{\mathrm{cyc}} \frac{1}{x^{\alpha}+y^{\beta}+z^{\gamma}} \leq 1
$$

对于此推广, 我们用米尔黑德不等式给出另一种证明:

证明 待定系数 $k$, 由柯西不等式,

$$
\sum_{c y c} \frac{1}{x^{\alpha}+y^{\beta}+z^{\gamma}} \leq \sum_{c y c} \frac{\left(x^{2 k-\alpha}+y^{2 k-\beta}+z^{2 k-\gamma}\right)}{\left(x^{k}+y^{k}+z^{k}\right)^{2}} .
$$

故只需使:

$$
\frac{\sum_{c y c}\left(x^{2 k-\alpha}+y^{2 k-\beta}+z^{2 k-\gamma}\right)}{\left(x^{k}+y^{k}+z^{k}\right)^{2}} \leq 1 .
$$

这等价于

$$
\sum_{c y c} x^{2 k-\alpha}+\sum_{c y c} x^{2 k-\beta}+\sum_{c y c} x^{2 k-\gamma} \leq \sum_{c y c} x^{2 k}+2 \sum_{c y c} x^{k} y^{k}
$$

则只需使 $(2 k, 0,0) \succ\left(2 k-\frac{2}{3} \alpha, \frac{1}{3} \alpha, \frac{1}{3} \alpha\right)$.

$$
(k, k, 0) \succ\left(2 k-\frac{2}{3} \beta, \frac{1}{3} \beta, \frac{1}{3} \beta\right)(a) \text { 或 }(k, k, 0) \succ\left(\frac{1}{3} \beta, \frac{1}{3} \beta, 2 k-\frac{2}{3} \beta\right)
$$

修订日期: 2023-11-08,

$$
(k, k, 0) \succ\left(2 k-\frac{2}{3} \gamma, \frac{1}{3} \gamma, \frac{1}{3} \gamma\right)(c) \text { 或 }(k, k, 0)>\left(\frac{1}{3} \gamma, \frac{1}{3} \gamma, 2 k-\frac{2}{3} \gamma\right)
$$

当 $\beta \leq \gamma \leq \frac{3}{2} \beta$ 时, 存在 $\frac{1}{3} \gamma \leq k \leq \frac{1}{2} \beta$ 使得 $(b)(d)$ 成立;

当 $\frac{3}{2} \beta \leq \gamma \leq 2 \beta$ 时, 存在 $\frac{1}{3} \gamma \leq k \leq \frac{2}{3} \beta$ 使得 $(a)(d)$ 成立.

故 $\beta \leq \gamma \leq 2 \beta$ 时 $k$ 存在.

在考试中, 指数改成了 $0,1,2$. 我们依然用米尔黑德不等式, 其证明如下:

证明 由柯西不等式，

$$
\sum_{c y c} \frac{1}{1+x+y^{2}} \leq \frac{\sum_{c y c}\left(z^{2 k}+x^{2 k-1}+y^{2 k-2}\right)}{\left(x^{k}+y^{k}+z^{k}\right)}
$$

只需证右式 $\leq 1$.

展开后等价于

$$
2 \sum_{c y c} x^{k} y^{k} \geq \sum_{c y c} x^{2 k-1}+\sum_{c y c} x^{2 k-2}
$$

只需证明

$$
\begin{aligned}
& \sum_{c y c} x^{k} y^{k} \geq \sum_{c y c} x^{2 k-\frac{2}{3}} y^{\frac{1}{3}} z^{\frac{1}{3}}, \\
& \sum_{c y c} x^{k} y^{k} \geq \sum_{c y c} x^{2 k-\frac{4}{3}} y^{\frac{2}{3}} z^{\frac{2}{3}} .
\end{aligned}
$$

这只需使 $(k, k, 0) \succ\left(2 k-\frac{2}{3}, \frac{1}{3}, \frac{1}{3}\right) ; \quad(k, k, 0) \succ\left(2 k-\frac{4}{3}, \frac{2}{3}, \frac{2}{3}\right)$, 即 $k=\frac{2}{3}$.

通过米尔黑德不等式的限制条件, 发现用柯西不等式方法放缩, $\frac{2}{3}$ 是唯一的.

引理 $a, b, c \in \mathbb{R}_{+}, a b c=1$. 则 $f(x)=\sum_{c y c} a^{x}$ 在 $(-\infty, 0)$ 单调递减, 在 $(0,+\infty)$单调递增.

证明 $f^{\prime}(x)=a^{x} \ln a+b^{x} \ln b+c^{x} \ln c$.

不妨设 $x>0$ (否则将 $a, b, c$ 取倒数), $c<1 \leq b \leq a(c=1$ 时易证), 只需证明

$$
a^{x} \ln a+b^{x} \ln b+c^{x} \ln c \geq 0
$$

等价于

$$
\frac{a^{x} \ln a+b^{x} \ln b}{\ln a+\ln b} \geq c^{x} .
$$

由加权均值不等式,

$$
\frac{a^{x} \ln a+b^{x} \ln b}{\ln a+\ln b} \geq \frac{\ln a}{\ln a+\ln b} a^{x}+\frac{\ln b}{\ln a+\ln b} b^{x} \geq a^{x \cdot \frac{\ln a}{\ln a+\ln b}} b^{x \cdot \frac{\ln b}{\ln a+\ln b}}
$$

只须证明

$$
a^{\frac{\ln a}{\ln a+\ln b}} b^{\frac{\ln b}{\ln a+\ln b}} \geq c=(a b)^{-1} .
$$

对等式两边取对数, 只须证明

$$
\frac{\ln ^{2} a+\ln ^{2} b}{\ln a+\ln b} \geq-(\ln a+\ln b) .
$$

由于 $\ln a+\ln b=\ln a b>0$, 则原式成立.

题 2 也可以利用此引理及柯西不等式进行证明.

进一步, 我们推广到 $n$ 元弱形式:

题 3 已知 $x_{i} \in \mathbb{R}_{+}(1 \leq i \leq n) .0 \leq \alpha_{1} \leq \cdots \leq \alpha_{n} \leq\left(2-\frac{2}{n}\right) \alpha_{2}$. 证明:

$$
\sum_{i=1}^{n} \frac{1}{x_{1}{ }^{\alpha_{i}}+x_{2}^{\alpha_{i}}+\cdots+x_{n}{ }^{\alpha_{i}}} \leq 1
$$

证明 注意到

$$
\sum_{i=1}^{n} \frac{1}{x_{1}^{\alpha_{i}}+x_{2}{ }^{\alpha_{i}}+\cdots+x_{n}{ }^{\alpha_{i}}} \leq \sum_{i=1}^{n} \frac{x_{1}{ }^{2 k-\alpha_{i}}+x_{2}{ }^{2 k-\alpha_{i}}+\cdots+x_{n}{ }^{2 k-\alpha_{i}}}{\left(x_{1}{ }^{k}+x_{2}{ }^{k}+\cdots+x_{n}{ }^{k_{i}}\right)^{2}}
$$

只需证明右式 $\leq 1$.

这等价于

$$
\sum_{i=1}^{n} x_{i}^{2 k}+2 \sum_{1 \leq i<j \leq n} x_{i}^{k} x_{j}^{k} \geq \sum_{j=1}^{n} \sum_{i=1}^{n} x_{i}^{2 k-\alpha_{j}}
$$

由于

$$
\sum_{j=1, j \neq i}^{n} x_{i}^{k} x_{j}^{k} \geq(n-1) x_{j}^{\frac{n-2}{n-1} k}
$$

所以

$$
2 \sum_{1 \leq i<j \leq n} x_{i}^{k} x_{j}^{k} \geq(n-1) \sum_{i=1}^{n} x_{i}^{\frac{n-2}{n-1} k}
$$

故只需

$$
\begin{aligned}
& \sum_{i=1}^{n} x_{i}^{2 k} \geq \sum_{i=1}^{n} x_{i}^{2 k-\alpha_{1}} \\
& \sum_{i=1}^{n} x_{i}{ }^{\frac{n-2}{n-1} k} \geq \sum_{i=1}^{n} x_{i}{ }^{2 k-\alpha_{j}}(2 \leq j \leq n)
\end{aligned}
$$

(1): $(2 k, 0, \cdots, 0) \succ\left(2 k-\frac{n-1}{n} \alpha_{1}, \frac{\alpha_{1}}{n}, \cdots, \frac{\alpha_{1}}{n}\right)$, 即 $k \geq \frac{\alpha_{1}}{2}$.

(2): (i) $\left(\frac{n-2}{n-1} k, 0, \cdots, 0\right) \succ\left(2 k-\alpha_{j}+t, t, \cdots, t\right)$. 其中 $t=\frac{1}{n}\left(\alpha_{j}-\frac{n}{n-1} k\right)$

故 $\frac{\alpha_{n}}{2} \leq k \leq\left(1-\frac{1}{n}\right) \alpha_{2}$. 因此 $\alpha_{n} \leq\left(2-\frac{2}{n}\right) \alpha_{2}$.

(ii) $\left(\frac{n-2}{n-1} k, 0, \cdots, 0\right) \succ\left(t, \cdots, t, 2 k-\alpha_{j}+t\right)$

故 $\frac{(n-1)^{2}}{n(2 n-3)} \alpha_{n} \leq k \leq \frac{1}{2} \alpha_{2}$. 因此 $\alpha_{n} \leq \frac{n(2 n-3)}{2(n-1)^{2}} \alpha_{2}$.

而 $\frac{n(2 n-3)}{2(n-1)^{2}} \leq\left(2-\frac{2}{n}\right)$, 只需 $\frac{\alpha_{n}}{2} \leq k \leq\left(1-\frac{1}{n}\right) \alpha_{2}$.

当 $\alpha_{n} \leq\left(2-\frac{2}{n}\right) \alpha_{2}$ 时 $k$ 存在, 任取其一即可.
之后在数之谜上, 有网友指出此题由 Vasile 在 2005 年首先提出, 并且给出了如下推广, 但并未书写证明, 通过参考文章 [1] 中的待定系数法, 现整理如下:

题 $4 a, b, c \in \mathbb{R}_{+}, a b c=1, k \geq 0$. 证明:

$$
\frac{1}{1+a+b^{k}}+\frac{1}{1+b+c^{k}}+\frac{1}{1+c+a^{k}} \leq 1
$$

证明 不妨设 $k \geq 1$. (若 $0<k<1$, 换元即可) 对原式通分, 化简, 即证明下式:

$$
\sum_{c y c} a^{k+1} b+\sum_{c y c} a^{k} b^{k+1} \geq \sum_{c y c} a+\sum_{c y c} a^{k}
$$

待定系数 $\alpha,(0 \leq \alpha \leq 1)$. 只需使:

$$
\begin{aligned}
& \alpha \sum_{c y c} a^{k+1} b+(1-\alpha) \sum_{c y c} a^{k} b^{k+1} \geq \sum_{c y c} a^{k} \\
& (1-\alpha) \sum_{c y c} a^{k+1} b+\alpha \sum_{c y c} a^{k} b^{k+1} \geq \sum_{c y c} a .
\end{aligned}
$$

待定系数 $\lambda_{1}, \lambda_{2}, \mu_{1}, \mu_{2}\left(0 \leq \lambda_{1}, \mu_{2} \leq \alpha, 0 \leq \lambda_{2}, \mu_{1} \leq 1-\alpha\right)$, 使得

$$
\begin{gathered}
\lambda_{1} \sum_{c y c} a^{k+1} b+\left(\alpha-\lambda_{1}\right) \sum_{c y c} a^{k+1} b+\left(1-\alpha-\mu_{1}\right) \sum_{c y c} a^{k} b^{k+1} \\
+\mu_{1} \sum_{c y c} a^{k} b^{k+1} \geq \sum_{c y c} a^{k} ; \\
\lambda_{2} \sum_{c y c} a^{k+1} b+\left(1-\alpha-\lambda_{2}\right) \sum_{c y c} a^{k+1} b+\left(\alpha-\mu_{2}\right) \sum_{c y c} a^{k} b^{k+1} \\
+\mu_{2} \sum_{c y c} a^{k} b^{k+1} \geq \sum_{c y c} a .
\end{gathered}
$$

下面来看式 (1), 由加权均值不等式,

$$
\begin{aligned}
& L H S \geq \sum_{c y c}\left(a^{k+1} b\right)^{\lambda_{1}}\left(a c^{k+1}\right)^{\alpha-\lambda_{1}}\left(a^{k} b^{k+1}\right)^{1-\alpha-\mu_{1}}\left(c^{k} a^{k+1}\right)^{\mu_{1}} \\
= & \sum_{\text {cyc }} a^{\lambda_{1} k+\mu_{1}+\alpha(1-k)+k} b^{\lambda_{1}-\mu_{1}(k+1)-\alpha(k+1)+k+1} c^{-\lambda_{1}(k+1)+\mu_{1} k+\alpha(k+1)} .
\end{aligned}
$$

由引理, 只需

$$
a^{\lambda_{1} k+\mu_{1}+\alpha(1-k)+k} b^{\lambda_{1}-\mu_{1}(k+1)-\alpha(k+1)+k+1} c^{-\lambda_{1}(k+1)+\mu_{1} k+\alpha(k+1)}
$$

化为 $a$ 的幂的指数不小于 $k$, 令

$$
\lambda_{1}-\mu_{1}(k+1)-\alpha(k+1)+k+1=-\lambda_{1}(k+1)+\mu_{1} k+\alpha(k+1),
$$

即

$$
\lambda_{1}(k+2)=\mu_{1}(2 k+1)+(2 \alpha-1)(k+1) .
$$

由 $a b c=1$, (3) $=a^{\lambda_{1}(k-1)+\mu_{1}(k+2)+2 \alpha-1}$.
由引理, 只需

$$
\lambda_{1}(k-1)+\mu_{1}(k+2)+2 \alpha-1 \geq k .
$$

将(4)代入得, 只需:

$$
\begin{aligned}
& \lambda_{1} \geq \frac{k^{2}-1+\alpha\left(2 k^{2}+2 k+2\right)}{3 k^{2}+3 k+3}, \\
& \mu_{1} \geq \frac{2 k^{2}+3 k+1-\alpha\left(2 k^{2}+2 k+2\right)}{3 k^{2}+3 k+3} .
\end{aligned}
$$

结合 $0 \leq \lambda_{1} \leq \alpha, 0 \leq \mu_{1} \leq 1-\alpha$, 只需

$$
\frac{k^{2}-1}{k^{2}+k+1} \leq \alpha \leq \frac{k^{2}+2}{k^{2}+k+1} .
$$

下面来看式(2), 由加权均值不等式,

$$
\begin{array}{r}
L H S \geq \sum_{c y c}\left(a^{k+1} b\right)^{\lambda_{2}}\left(a c^{k+1}\right)^{1-\alpha-\lambda_{2}}\left(a^{k} b^{k+1}\right)^{\alpha-\mu_{2}}\left(c^{k} a^{k+1}\right)^{\mu_{2}} \\
=\sum_{\text {cyc }} a^{\lambda_{2}(k+1)+\left(1-\alpha-\mu_{2}\right)+\left(\alpha-\mu_{2}\right) k+(k+1) \mu_{2}} b^{\lambda_{2}+\left(\alpha-\mu_{2}\right)(k+1)} c^{\left(1-\alpha-\lambda_{1}\right)(k+1)+\mu_{2} k}
\end{array}
$$

由引理, 只需

$$
a^{\lambda_{2}(k+1)+\left(1-\alpha-\mu_{2}\right)+\left(\alpha-\mu_{2}\right) k+(k+1) \mu_{2}} b^{\lambda_{2}+\left(\alpha-\mu_{2}\right)(k+1)} c^{\left(1-\alpha-\lambda_{2}\right)(k+1)+\mu_{2} k}
$$

化为 $a$ 的幂的指数不小于 1 .

$$
\lambda_{2}+\left(\alpha-\mu_{2}\right)(k+1)=\left(1-\alpha-\lambda_{2}\right)(k+1)+\mu_{2} k
$$

即

$$
\lambda_{2}(k+2)=\mu_{2}(2 k+1)+(1-2 \alpha)(k+1) .
$$

由 $a b c=1$, (6) $=a^{\lambda_{1}(k-1)+\mu_{1}(k+2)+2 \alpha-1}$.

由引理, 只需 $\lambda_{1}(k-1)+\mu_{1}(k+2)+2 \alpha-1 \geq k$.

将(7)代入得, 只需:

$$
\begin{aligned}
& \lambda_{2} \geq \frac{k^{2}+3 k+2-\alpha\left(2 k^{2}-6 k+2\right)}{3 k^{2}+3 k+3} \\
& \mu_{2} \geq \frac{1-k^{2}+\alpha\left(2 k^{2}+2 k+2\right)}{3 k^{2}+3 k+3}
\end{aligned}
$$

结合 $0 \leq \lambda_{2} \leq 1-\alpha, 0 \leq \mu_{2} \leq \alpha$, 只需

$$
\frac{1-k^{2}}{k^{2}+k+1} \leq \alpha \leq \frac{2 k^{2}+1}{k^{2}+k+1}
$$

由(5)(8)得: 只需 $\frac{k^{2}-1}{k^{2}+k+1} \leq \alpha \leq \frac{k^{2}+2}{k^{2}+k+1}$ 即可.

致谢 作者感谢卢伟老师的指导, 也感谢王彬老师的鼓励并帮助修改了文章.

## 参考文献

[1] 王彬. 第四届百年老校数学竞赛试题解析 [J], 数学新星网. 教师专栏, 2023.08.16 期.

[2] V. Cîrtoaje. Mathematical Inequalities Volume 3: Cyclic and Noncyclic inequalities, LAP LAMBERT Academic Publishing, 2018, P71.

