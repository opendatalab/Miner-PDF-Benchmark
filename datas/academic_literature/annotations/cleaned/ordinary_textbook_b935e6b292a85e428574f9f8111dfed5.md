# 对一道 IMC 不等式最佳常数的探究 

廖昱博<br>(中国人民大学附属中学, 100080)<br>指导教师: 张端阳

在 2000 年 IMC (国际大学生数学竞赛) 第一天的比赛中, 第四题是一道不等式:

a) 证明: 若 $\left\{x_{i}\right\}$ 是递减的正项数列, 则

$$
\left(\sum_{i=1}^{n} x_{i}^{2}\right)^{1 / 2} \leq \sum_{i=1}^{n} \frac{x_{i}}{\sqrt{i}}
$$

b) 证明: 存在常数 $C$, 使得若 $\left\{x_{i}\right\}$ 是递减的正项数列, 则

$$
\sum_{m=1}^{\infty} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{\infty} x_{i}^{2}\right)^{1 / 2} \leq C \sum_{i=1}^{\infty} x_{i} .
$$

先将原解答抄录如下:

证明 a)

$$
\begin{aligned}
\left(\sum_{i=1}^{n} \frac{x_{i}}{\sqrt{i}}\right)^{2} & =\sum_{i, j}^{n} \frac{x_{i} x_{j}}{\sqrt{i} \sqrt{j}} \geq \sum_{i=1}^{n}\left(\frac{x_{i}}{\sqrt{i}} \sum_{j=1}^{i} \frac{x_{j}}{\sqrt{j}}\right) \\
& \geq \sum_{i=1}^{n}\left(\frac{x_{i}}{\sqrt{i}} \cdot i \frac{x_{i}}{\sqrt{i}}\right)=\sum_{i=1}^{n} x_{i}^{2} .
\end{aligned}
$$

b) 由 a),

$$
\begin{aligned}
\sum_{m=1}^{\infty} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{\infty} x_{i}^{2}\right)^{1 / 2} & \leq \sum_{m=1}^{\infty}\left(\frac{1}{\sqrt{m}} \sum_{i=m}^{\infty} \frac{x_{i}}{\sqrt{i-m+1}}\right) \\
& =\sum_{i=1}^{\infty}\left(x_{i} \sum_{m=1}^{i} \frac{1}{\sqrt{m} \sqrt{i-m+1}}\right)
\end{aligned}
$$

因为

$$
\sup _{i} \sum_{m=1}^{i} \frac{1}{\sqrt{m} \sqrt{i-m+1}} \leq \int_{0}^{i+1} \frac{1}{\sqrt{x} \sqrt{i+1-x}} \mathrm{~d} x=\pi
$$

修订日期: 2020-05-21.
所以可取 $C=\pi$.

注意到原解答 a) 中的放缩比较大, 事实上我们有更强的结果:

命题 若 $\left\{x_{i}\right\}$ 是递减的正项数列, 则

$$
\left(\sum_{i=1}^{n} x_{i}^{2}\right)^{1 / 2} \leq \sum_{i=1}^{n}(\sqrt{i}-\sqrt{i-1}) x_{i}
$$

证明 对 $n$ 用数学归纳法.

当 $n=1$ 时命题显然成立. 假设命题当 $n=k$ 时成立, 来看 $n=k+1$ 时的情形.

由归纳假设，

$$
\sum_{i=1}^{k} x_{i}^{2} \leq\left(\sum_{i=1}^{k}(\sqrt{i}-\sqrt{i-1}) x_{i}\right)^{2}
$$

所以为证

$$
\sum_{i=1}^{k+1} x_{i}^{2} \leq\left(\sum_{i=1}^{k+1}(\sqrt{i}-\sqrt{i-1}) x_{i}\right)^{2}
$$

只需证明

$$
x_{k+1}^{2} \leq\left(\sum_{i=1}^{k+1}(\sqrt{i}-\sqrt{i-1}) x_{i}\right)^{2}-\left(\sum_{i=1}^{k}(\sqrt{i}-\sqrt{i-1}) x_{i}\right)^{2},
$$

即

$$
x_{k+1}^{2} \leq(\sqrt{k+1}-\sqrt{k}) x_{k+1}\left(2 \sum_{i=1}^{k}(\sqrt{i}-\sqrt{i-1}) x_{i}+(\sqrt{k+1}-\sqrt{k}) x_{k+1}\right)
$$

即

$$
\sqrt{k} x_{k+1} \leq \sum_{i=1}^{k}(\sqrt{i}-\sqrt{i-1}) x_{i}
$$

这由 $x_{k+1}=\min \left\{x_{1}, x_{2}, \cdots, x_{k+1}\right\}$ 及

$$
\sqrt{k}=\sum_{i=1}^{k}(\sqrt{i}-\sqrt{i-1})
$$

即证.

归纳证毕.

注意到

$$
\sum_{i=1}^{n}(\sqrt{i}-\sqrt{i-1}) x_{i}=\sum_{i=1}^{n} \frac{x_{i}}{\sqrt{i}+\sqrt{i-1}}
$$

所以命题比 a) 强了近一倍. 这使我们有理由相信 b) 中的 $C$ 可改进为 $\frac{\pi}{2}$ 左右.
本文来证明 $C$ 的最佳值为 $\frac{\pi}{2}$, 即有

定理 设 $\left\{x_{i}\right\}$ 是递减的正项数列, 则使得

成立的最佳常数 $C$ 为 $\frac{\pi}{2}$.

$$
\sum_{m=1}^{\infty} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{\infty} x_{i}^{2}\right)^{1 / 2} \leq C \sum_{i=1}^{\infty} x_{i}
$$

先证明两个引理.

引理 1 给定正整数 $n$, 设正实数 $x_{1} \geq x_{2} \geq \cdots \geq x_{n}$, 则使得

$$
\sum_{m=1}^{n} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2} \leq C_{n} \sum_{i=1}^{n} x_{i}
$$

成立的最佳常数 $C_{n}$ 为

$$
\lambda_{n}=\max _{1 \leq i \leq n} \frac{1}{i} \sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}} .
$$

证明 一方面, 对 $1 \leq i \leq n$, 取 $x_{1}=x_{2}=\cdots=x_{i}=t, x_{i+1}=\cdots=x_{n} \rightarrow 0$,

则

$$
\begin{aligned}
\sum_{m=1}^{n} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2} & \rightarrow \sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}} t \\
\sum_{i=1}^{n} x_{i} & \rightarrow i t
\end{aligned}
$$

所以

$$
C_{n} \geq \frac{1}{i} \sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}}
$$

从而 $C_{n} \geq \lambda_{n}$.

另一方面, 我们证明

$$
\sum_{m=1}^{n} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2} \leq \lambda_{n} \sum_{i=1}^{n} x_{i}
$$

这有两种方法.

法 1 由命题,

$$
\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2} \leq \sum_{i=m}^{n}(\sqrt{i+1-m}-\sqrt{i-m}) x_{i}
$$

结合 Abel 变换得,

$$
\sum_{m=1}^{n} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2} \leq \sum_{m=1}^{n} \sum_{i=m}^{n} \frac{\sqrt{i+1-m}-\sqrt{i-m}}{\sqrt{m}} x_{i}
$$

$$
\begin{aligned}
& =\sum_{i=1}^{n}\left(\sum_{m=1}^{i} \frac{\sqrt{i+1-m}-\sqrt{i-m}}{\sqrt{m}}\right) x_{i} \\
& =\sum_{i=1}^{n-1}\left(\sum_{j=1}^{i} \sum_{m=1}^{j} \frac{\sqrt{j+1-m}-\sqrt{j-m}}{\sqrt{m}}\right)\left(x_{i}-x_{i+1}\right)+\sum_{j=1}^{n}\left(\sum_{m=1}^{j} \frac{\sqrt{j+1-m}-\sqrt{j-m}}{\sqrt{m}}\right) x_{n} \\
& =\sum_{i=1}^{n-1}\left(\sum_{m=1}^{i} \sum_{j=m}^{i} \frac{\sqrt{j+1-m}-\sqrt{j-m}}{\sqrt{m}}\right)\left(x_{i}-x_{i+1}\right)+\sum_{m=1}^{n}\left(\sum_{j=m}^{n} \frac{\sqrt{j+1-m}-\sqrt{j-m}}{\sqrt{m}}\right) x_{n} \\
& =\sum_{i=1}^{n-1}\left(\sum_{m=1}^{i} \frac{\sqrt{i+1-m}}{\sqrt{m}}\right)\left(x_{i}-x_{i+1}\right)+\sum_{m=1}^{n} \frac{\sqrt{n+1-m}}{\sqrt{m}} x_{n} \\
& \leq \sum_{i=1}^{n-1} \lambda_{n} i\left(x_{i}-x_{i+1}\right)+\lambda_{n} n x_{n} \\
& =\lambda_{n} \sum_{i=1}^{n} x_{i} .
\end{aligned}
$$

法 2 令

$$
F\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\sum_{m=1}^{n} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2}-\lambda_{n} \sum_{i=1}^{n} x_{i} .
$$

对 $1 \leq i \leq n$, 记

$$
f_{i}(t)=F(\underbrace{t, t, \cdots, t}_{i \uparrow}, x_{i+1}, \cdots, x_{n}) .
$$

如果证明了每个 $f_{i}(t)$ 均在 $(0,+\infty)$ 上单调不增, 则

$$
\begin{aligned}
F\left(x_{1}, x_{2}, x_{3}, \cdots, x_{n}\right) & \leq F\left(x_{2}, x_{2}, x_{3}, \cdots, x_{n}\right) \\
& \leq F\left(x_{3}, x_{3}, x_{3}, x_{4}, \cdots, x_{n}\right) \\
& \leq \cdots \cdots \\
& \leq F\left(x_{n}, x_{n}, \cdots, x_{n}\right) \\
& =\sum_{m=1}^{n} \sqrt{\frac{n+1-m}{m}} x_{n}-\lambda_{n} n x_{n} \\
& \leq 0
\end{aligned}
$$

引理得证.

下证 $f_{i}(t)$ 在 $(0,+\infty)$ 上单调不增.

记 $A^{2}=x_{i+1}^{2}+\cdots+x_{n}^{2}$, 则

$$
f_{i}(t)=\sum_{m=1}^{i} \sqrt{\frac{(i+1-m) t^{2}+A^{2}}{m}}-\lambda_{n} i t+g\left(x_{i+1}, \cdots, x_{n}\right) \text {, }
$$

其中 $g\left(x_{i+1}, \cdots, x_{n}\right)$ 与 $t$ 无关. 所以

$$
\begin{aligned}
f_{i}^{\prime}(t) & =\sum_{m=1}^{i} \frac{2(i+1-m) t}{2 \sqrt{\frac{(i+1-m) t^{2}+A^{2}}{m}}}-\lambda_{n} i \\
& <\sum_{m=1}^{i} \frac{(i+1-m) t}{\sqrt{\frac{(i+1-m) t^{2}}{m}}}-\lambda_{n} i \\
& =\sum_{m=1}^{i} \sqrt{\frac{m}{i+1-m}}-\lambda_{n} i \\
& =\sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}}-\lambda_{n} i
\end{aligned}
$$

$$
\leq 0
$$

综上, 引理 1 得证.

引理 2. 对任意正整数 $i$, 均有

$$
\frac{1}{i} \sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}}<\frac{\pi}{2}
$$

证明 当 $i=1$ 时显然成立, 下设 $i \geq 2$.

因为函数 $y=\sqrt{\frac{i+1-x}{x}}$ 在 $(0, i+1)$ 上单调递减, 所以

$$
\sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}}=\sqrt{i}+\sum_{m=2}^{i} \sqrt{\frac{i+1-m}{m}}<\sqrt{i}+\int_{1}^{i+1} \sqrt{\frac{i+1-x}{x}} \mathrm{~d} x .
$$

令 $x=(i+1) \sin ^{2} \theta$, 记 $\alpha=\arcsin \frac{1}{\sqrt{i+1}}$, 则

$$
\begin{aligned}
\int_{1}^{i+1} \sqrt{\frac{i+1-x}{x}} \mathrm{~d} x & =\int_{\alpha}^{\frac{\pi}{2}} \frac{\cos \theta}{\sin \theta} \mathrm{d}(i+1) \sin ^{2} \theta \\
& =2(i+1) \int_{\alpha}^{\frac{\pi}{2}} \cos ^{2} \theta \mathrm{d} \theta \\
& =\left.(i+1)\left(\frac{1}{2} \sin 2 \theta+\theta\right)\right|_{\alpha} ^{\frac{\pi}{2}} \\
& =(i+1)\left(\frac{\pi}{2}-\frac{1}{2} \sin 2 \alpha-\alpha\right) \\
& <(i+1)\left(\frac{\pi}{2}-\sin \alpha \cos \alpha-\sin \alpha\right) \\
& =(i+1)\left(\frac{\pi}{2}-\frac{\sqrt{i}}{i+1}-\frac{1}{\sqrt{i+1}}\right) \\
& =(i+1) \frac{\pi}{2}-\sqrt{i}-\sqrt{i+1} .
\end{aligned}
$$

所以

$$
\sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}}<(i+1) \frac{\pi}{2}-\sqrt{i+1}<i \cdot \frac{\pi}{2}
$$

其中最后一步用到了 $i \geq 2$.

综上, 引理 2 得证.

现在我们来证明定理.

一方面, 由引理 1 和引理 2, 对任意正整数 $n$,

$$
\sum_{m=1}^{n} \frac{1}{\sqrt{m}}\left(\sum_{i=m}^{n} x_{i}^{2}\right)^{1 / 2} \leq \lambda_{n} \sum_{i=1}^{n} x_{i}<\frac{\pi}{2} \sum_{i=1}^{n} x_{i}
$$

令 $n \rightarrow \infty$ 即知 $C=\frac{\pi}{2}$ 时不等式成立.

另一方面, 取 $x_{1}=x_{2}=\cdots=x_{i}=t, x_{i+1}=x_{i+2}=\cdots=\varepsilon$, 则当 $\varepsilon \rightarrow 0$ 时,

$$
C \geq \frac{1}{i} \sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}}
$$

又类似引理 2 的证明,

$$
\begin{aligned}
\frac{1}{i} \sum_{m=1}^{i} \sqrt{\frac{i+1-m}{m}} & >\frac{1}{i} \int_{1}^{i+1} \sqrt{\frac{i+1-x}{x}} \mathrm{~d} x \\
& =\frac{i+1}{i}\left(\frac{\pi}{2}-\frac{1}{2} \sin 2 \alpha-\alpha\right) \\
& >\frac{i+1}{i}\left(\frac{\pi}{2}-\sin \alpha \cos \alpha-\tan \alpha\right) \\
& =\frac{i+1}{i}\left(\frac{\pi}{2}-\frac{\sqrt{i}}{i+1}-\frac{1}{\sqrt{i}}\right) \\
& \rightarrow \frac{\pi}{2}(i \rightarrow+\infty),
\end{aligned}
$$

所以 $C \geq \frac{\pi}{2}$.

综上, 定理证毕.

