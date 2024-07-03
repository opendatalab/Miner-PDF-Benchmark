数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 一个具有最优系数的双序列差分不等式 

## 李橙

(浙江省镇海中学, 315299)

指导教师: 陈科钧

2023 年韩国数学奥林匹克 (KMO) 第 6 题是一个关于双序列的差分不等式:

题 1 设正整数 $n \geq 3, a_{1}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$ 是两个实数序列. 证明:

$$
\sum_{i=1}^{n} a_{i}\left(b_{i}-b_{i+3}\right) \leq \frac{3 n}{8} \sum_{i=1}^{n}\left(\left(a_{i}-a_{i+1}\right)^{2}+\left(b_{i}-b_{i+1}\right)^{2}\right)
$$

其中 $a_{n+1}=a_{1}$, 且对 $i=1,2,3, b_{n+i}=b_{i}$.

本文给出这个不等式的最优系数的一个加强, 建立了如下定理:

定理 1 设 $n \geq 3$ 是给定的整数, $a_{1}, \cdots, a_{n}$ 和 $b_{1}, \cdots, b_{n}$ 是两个实数序列, 则

$$
\sum_{i=1}^{n} a_{i}\left(b_{i}-b_{i+3}\right) \leq \frac{3-4 \sin ^{2} \frac{\pi}{n}}{4 \sin \frac{\pi}{n}} \sum_{i=1}^{n}\left(\left(a_{i}-a_{i+1}\right)^{2}+\left(b_{i}-b_{i+1}\right)^{2}\right)
$$

其中 $a_{n+1}=a_{1}$, 且对 $i=1,2,3, b_{n+i}=b_{i}$. 上式系数是最优的.

这个结果可等价地描述如下 (只需令 $c_{i}=b_{i+1}-b_{i+2}$, 并注意到 $\left\{a_{i}\right\}_{i=1}^{n}$ 的平移不变性):

定理 2 设 $n \geq 3$ 是给定的整数, 实数序列 $a_{1}, \cdots, a_{n}$ 和 $c_{1}, \cdots, c_{n}$ 满足 $\sum_{i=1}^{n} a_{i}=0, \sum_{i=1}^{n} c_{i}=0$, 则

$$
\sum_{i=1}^{n} a_{i}\left(c_{i-1}+c_{i}+c_{i+1}\right) \leq \frac{3-4 \sin ^{2} \frac{\pi}{n}}{4 \sin \frac{\pi}{n}} \sum_{i=1}^{n}\left(\left(a_{i}-a_{i+1}\right)^{2}+c_{i}^{2}\right)
$$

其中 $a_{n+1}=a_{1}, c_{0}=c_{n}, c_{n+1}=c_{1}$, 当

$$
a_{i}=\cos \frac{2 \pi i}{n}, c_{i}=2 \sin \frac{\pi}{n} \cos \frac{2 i \pi}{n}, i=1,2, \cdots, n
$$

时等号成立。[^0]为此, 给出如下引理:

引理 1 (Fan 不等式) 设实数 $m_{1}, \cdots, m_{n}$ 满足 $\sum_{i=1}^{n} m_{i}=0$, 则

$$
\sum_{i=1}^{n} m_{i} m_{i+1} \leq \cos \frac{2 \pi}{n} \sum_{i=1}^{n} m_{i}^{2}
$$

等价地, 我们得到

$$
\sum_{i=1}^{n}\left(m_{i}-m_{i+1}\right)^{2} \geq 4 \sin ^{2} \frac{\pi}{n} \sum_{i=1}^{n} m_{i}^{2}
$$

其中 $m_{n+1}=m_{1}$.

证明 (镇海中学学生王海) 取 $n$ 维向量

$$
\overrightarrow{t_{i}}=\left(m_{i}, m_{i+1}, \cdots, m_{n}, m_{1}, \cdots, m_{i-1}\right), i=1,2, \cdots, n
$$

不妨令 $\sum_{i=1}^{n} m_{i}^{2}=1$, 这时对任意 $i,\left|\overrightarrow{t_{i}}\right|=1$. 再由 $\sum_{i=1}^{n} m_{i}=0$ 知 $\sum_{i=1}^{n} \vec{t}_{i}=\overrightarrow{0}$. 设

$$
\overrightarrow{t_{i}} \cdot \overrightarrow{t_{i+1}}=\sum_{i=1}^{n} m_{i} m_{i+1}=\cos \theta, \theta \in(0, \pi]
$$

下证 $\theta \geq \frac{2 \pi}{n}$. 用反证法. 若 $\theta<\frac{2 \pi}{n}$, 由

$$
\left\{\begin{array}{lr}
\overrightarrow{t_{1}} \cdot \overrightarrow{t_{i}}=\cos \left\langle\overrightarrow{t_{1}}, \overrightarrow{t_{i}}\right\rangle \geq \cos (i-1) \theta, & 1 \leq i \leq \frac{n}{2} \\
\overrightarrow{t_{1}} \cdot \overrightarrow{t_{n-i}}=\cos \left\langle\overrightarrow{t_{1}}, \overrightarrow{t_{n-i}}\right\rangle \geq \cos (i+1) \theta, \quad 0 \leq i \leq \frac{n-1}{2}
\end{array}\right.
$$

当 $2 \nmid n$ 时有

$$
0 \overrightarrow{t_{1}} \cdot \sum_{i=1}^{n} \overrightarrow{t_{i}} \geq 1+2\left(\cos \theta+\cdots+\cos \frac{n-1}{2} \theta\right)=\frac{\sin \frac{n}{2} \theta}{\sin \frac{\theta}{2}}>0
$$

矛盾!

当 $2 \mid n$ 时有

$$
0 \overrightarrow{t_{1}} \cdot \sum_{i=1}^{n} \overrightarrow{t_{i}} \geq 1+2\left(\cos \theta+\cdots+\cos \frac{n-2}{2} \theta\right)+\cos \frac{n}{2} \theta=\frac{\sin \frac{n}{2} \theta \cos \frac{\theta}{2}}{\sin \frac{\theta}{2}}>0
$$

矛盾!

故 $\theta \geq \frac{2 \pi}{n}$,

$$
\sum_{i=1}^{n} m_{i} m_{i+1}=\cos \theta \leq \cos \frac{2 \pi}{n}=\cos \frac{2 \pi}{n} \sum_{i=1}^{n} m_{i}^{2},
$$

令 $m_{i}=A \cos \frac{2 i \pi}{n}+B \sin \frac{2 i \pi}{n}, i=1,2, \cdots, n$ 知不等式取等号.

引理 2 设整数 $n \geq 3, x_{1}, \cdots, x_{n} \in \mathbb{R}$ 满足 $\sum_{i=1}^{n} x_{i}=0$, 则

$$
\sum_{i=1}^{n}\left(x_{i}+x_{i+1}+x_{i+2}\right)^{2} \leq\left(3-4 \sin ^{2} \frac{\pi}{n}\right)^{2} \sum_{i=1}^{n} x_{i}^{2}
$$

下标模 $n$ 同余.

证明 由齐次性, 不妨令 $\sum_{i=1}^{n} x_{i}^{2}=1$.

$n=3$, 左右两边均为 0 .

$n=4$, 为恒等式.

$n=5$, 即为 Fan 不等式, 这里用到

$$
2+2 \cos \frac{2 \pi}{5}=\left(3-4 \sin ^{2} \frac{\pi}{5}\right)^{2}
$$

下面考虑 $n \geq 6$, 这时问题转化为在条件 $\sum_{i=1}^{n} x_{i}^{2}=1$ 和 $\sum_{i=1}^{n} x_{i}=0$ 下求 $\sum_{i=1}^{n}\left(x_{i}+x_{i+1}+x_{i+2}\right)^{2}$ 的最大值.

作 Lagrange 函数

$$
F=\sum_{i=1}^{n}\left(x_{i}+x_{i+1}+x_{i+2}\right)^{2}+\lambda \sum_{i=1}^{n} x_{i}+\mu\left(1-\sum_{i=1}^{n} x_{i}^{2}\right) \text {. }
$$

由条件极值的必要条件知

$$
x_{i-2}+2 x_{i-1}+(3-\mu) x_{i}+2 x_{i+1}+x_{i+2}+\frac{\lambda}{2}=0, i=1,2, \cdots, n \text {. }
$$

将这 $n$ 个式子相加, 得 $\lambda=0$, 从而

$$
x_{i-2}+2 x_{i-1}+(3-\mu) x_{i}+2 x_{i+1}+x_{i+2}=0 .
$$

$(*)$ 的特征根方程为 $x^{4}+2 x^{3}+(3-\mu) x^{2}+2 x+1=0$, 则

$$
x \neq 0 \Rightarrow\left(x+\frac{1}{x}+1\right)^{2}=\mu
$$

注意到此时 $\sum_{i=1}^{n}\left(x_{i}+x_{i+1}+x_{i+2}\right)^{2}=\mu$.

(1) $\left(x+\frac{1}{x}+1\right)^{2}=\mu$ 有重根, 则 $\mu=9$ 或 1 或 0 . 而 $\mu=9$ 时有 $x_{1}=x_{2}=\cdots=$ $x_{n}=0$, 矛盾!

(2) $\left(x+\frac{1}{x}+1\right)^{2}=\mu$ 无重根, 考虑以 $(*)$ 定义的递推数列, 为不全为 0 且周期为 $n$ 的数列, 记其特征根为 $t_{1}, t_{2}, t_{3}, t_{4}$, 则 $t_{i} \neq t_{j}, \forall 1 \leq i<j \leq 4$. 则

$$
x_{i}=A_{1} t_{1}^{i}+A_{2} t_{2}^{i}+A_{3} t_{3}^{i}+A_{4} t_{4}^{i}, A_{j} \in \mathbb{C}, j=1,2,3,4,
$$

其中至少有 1 个 $A_{j}$ 非 0 .

我们证明有 1 个特征根为 $n$ 次单位根.

否则, 对任意 $i=1,2, \cdots, n$,

$$
\begin{aligned}
x_{i+n} & =A_{1} t_{1}^{i+n}+A_{2} t_{2}^{i+n}+A_{3} t_{3}^{i+n}+A_{4} t_{4}^{i+n} \\
& =x_{i}=A_{1} t_{1}^{i}+A_{2} t_{2}^{i}+A_{3} t_{3}^{i}+A_{4} t_{4}^{i} .
\end{aligned}
$$

即

$$
A_{1} t_{1}^{i}\left(t_{1}^{n}-1\right)+A_{2} t_{2}^{i}\left(t_{2}^{n}-1\right)+A_{3} t_{3}^{i}\left(t_{3}^{n}-1\right)+A_{4} t_{4}^{i}\left(t_{4}^{n}-1\right)=0 .
$$

由于没有 $n$ 次单位根, 因此对任意 $j=1,2,3,4, t_{j}^{n}-1 \neq 0$, 若只有 1 个 $A_{j}$ 非 0 则矛盾!

不妨恰有 $A_{1}, \cdots, A_{s}$ 非 $0, s \in\{2,3,4\}$, 方程组

$$
A_{1} t_{1}^{i} y_{1}+A_{2} t_{2}^{i} y_{2}+\cdots+A_{s} t_{s}^{i} y_{s}=0(i=1,2 \cdots, n)
$$

有非零解, 这表明行列式

$$
\left|\begin{array}{cccc}
A_{1} t_{1} & A_{2} t_{2} & \cdots & A_{s} t_{s} \\
A_{1} t_{1}^{2} & A_{2} t_{2}^{2} & \cdots & A_{s} t_{s}^{2} \\
\cdots & \cdots & \cdots & \cdots \\
A_{1} t_{1}^{s} & A_{2} t_{2}^{s} & \cdots & A_{s} t_{s}^{s}
\end{array}\right|=A_{1} A_{2} \cdots A_{s} t_{1} t_{2} \cdots t_{s}\left|\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
t_{1} & t_{2} & \cdots & t_{s} \\
\cdots & \cdots & \cdots & \cdots \\
t_{1}^{s-1} & t_{2}^{s-1} & \cdots & t_{s}^{s-1}
\end{array}\right|=0 .
$$

但由范德蒙德行列式知

$$
\left|\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
t_{1} & t_{2} & \cdots & t_{s} \\
\cdots & \cdots & \cdots & \cdots \\
t_{1}^{s-1} & t_{2}^{s-1} & \cdots & t_{s}^{s-1}
\end{array}\right|=\prod_{1 \leq j<i \leq s}\left(t_{i}-t_{j}\right) \neq 0
$$

由对任意 $k, A_{k}, t_{k} \neq 0$ 知矛盾!

故该方程有 $n$ 次单位根, 因此

$$
x+\frac{1}{x}=2 \cos \frac{2 k \pi}{n}, k \in\{1,2, \cdots, n-1\} .
$$

这样

$$
\mu=\left(1+2 \cos \frac{2 k \pi}{n}\right)^{2} \leq\left(1+2 \cos \frac{2 \pi}{n}\right)^{2}=\left(3-4 \sin ^{2} \frac{\pi}{n}\right)^{2}
$$

又 $\left(3-4 \sin ^{2} \frac{\pi}{n}\right)^{2}>1>0$, 故

$$
F_{\max }=\left(3-4 \sin ^{2} \frac{\pi}{n}\right)^{2}
$$

得到

$$
\sum_{i=1}^{n}\left(x_{i}+x_{i+1}+x_{i+2}\right)^{2} \leq\left(3-4 \sin ^{2} \frac{\pi}{n}\right)^{2} \sum_{i=1}^{n} x_{i}^{2}
$$

令 $x_{i}=A \cos \frac{2 i \pi}{n}+B \sin \frac{2 i \pi}{n}, i=1,2, \cdots, n$ 时, $(*)$ 可取到等号.

下面完成定理 2 的证明.

证明 由引理 1 知

$$
\sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2} \geq 4 \sin ^{2} \frac{\pi}{n} \sum_{i=1}^{n} a_{i}^{2}
$$

由引理 2 知

$$
\sum_{i=1}^{n} c_{i}^{2} \geq \frac{1}{\left(3-4 \sin ^{2} \frac{\pi}{n}\right)^{2}} \sum_{i=1}^{n}\left(c_{i}+c_{i+1}+c_{i+2}\right)^{2}
$$

这样由算术-几何均值不等式

$$
\begin{aligned}
& \sum_{i=1}^{n} a_{i}\left(c_{i-1}+c_{i}+c_{i+1}\right) \\
\leq & \sin \frac{\pi}{n} \cdot\left(3-4 \sin ^{2} \frac{\pi}{n}\right) \sum_{i=1}^{n} a_{i}^{2}+\frac{1}{4 \sin \frac{\pi}{n}\left(3-4 \sin ^{2} \frac{\pi}{n}\right)} \sum_{i=1}^{n}\left(c_{i-1}+c_{i}+c_{i+1}\right)^{2} \\
\leq & \frac{3-4 \sin ^{2} \frac{\pi}{n}}{4 \sin \frac{\pi}{n}}\left[\sum_{i=1}^{n}\left(a_{i}-a_{i+1}\right)^{2}+\sum_{i=1}^{n} c_{i}^{2}\right]
\end{aligned}
$$

得到

$$
\lambda=\frac{3-4 \sin ^{2} \frac{\pi}{n}}{4 \sin \frac{\pi}{n}}
$$

取 $a_{i}=\cos \frac{2 i \pi}{n}, c_{i}=2 \sin \frac{\pi}{n} \cos \frac{2 i \pi}{n}, i=1,2, \cdots, n$, 知此时的 $\lambda$ 是最佳的.

注 上面引理 2 的系数是由 $a_{i}$ 与 $\left(c_{i-1}+c_{i}+c_{i+1}\right)$ 成比例及 Fan 不等式取等条件猜到的, 证明的关键在解出 $\mu$, 在此感谢镇海中学张泽霖、徐在䆜的关键性建议及田俊峰的讨论。

笔者在与镇海中学田俊峰 (2023 年中国国家集训队队员) 讨论引理 2 时得到了以下的更一般的结果:

定理 3 设实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $\sum_{k=1}^{n} x_{k}=0$, 整数 $n, t$ 满足 $2 \leq t \leqslant \frac{n}{2}$, 则

$$
\sum_{k=1}^{n}\left(x_{k}+x_{k+1}+\cdots+x_{k+t-1}\right)^{2} \leqslant \frac{\sin ^{2} \frac{t \pi}{n}}{\sin ^{2} \frac{\pi}{n}} \sum_{k=1}^{n} x_{k}^{2},
$$

当且仅当 $x_{k}=A \cos \frac{2 k \pi}{n}+B \sin \frac{2 k \pi}{n}, k=1,2, \cdots, n$ 时等号成立, 脚标均模 $n$ 理解.

证明 由齐次性, 不妨设 $\sum_{k=1}^{n} x_{k}^{2}=1$. 这时问题转化为在条件 $\sum_{k=1}^{n} x_{k}=0$和 $\sum_{k=1}^{n} x_{k}^{2}=1$ 时, 求

$$
\sum_{k=1}^{n}\left(x_{k}+x_{k+1}+\cdots+x_{k+t-1}\right)^{2}
$$

的最大值.

注意到

$$
\sum_{k=1}^{n}\left(x_{k}+x_{k+1}+\cdots+x_{k+t-1}\right)^{2}=t \sum_{k=1}^{n} x_{k}^{2}+2 \sum_{j=1}^{t-1}\left[(t-j) \sum_{c=1}^{n} x_{c} x_{c+j}\right]
$$

我们只需考虑

$$
F=\sum_{j=1}^{t-1}\left[(t-j) \sum_{c=1}^{n} x_{c} x_{c+j}\right]
$$

的最大值.

我们对 $x_{1}, x_{2}, \cdots, x_{n}$ 使用离散傅里叶变换 (Discrete Fourier Transform): 记

$$
y_{p}=\frac{1}{\sqrt{n}} \sum_{k=1}^{n} w^{p k} x_{k} \text {, 其中 } w=e^{-\frac{2 \pi i}{n}}, p=1,2, \cdots, n \text {, }
$$

特别地, $y_{n}=\frac{1}{\sqrt{n}} \sum_{k=1}^{n} x_{k}=0$.

我们有逆变换:

$$
x_{p}=\frac{1}{\sqrt{n}} \sum_{k=1}^{n} w^{-p k} y_{k}
$$

且 $x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}$ 当且仅当 $y_{n-p}=\bar{y}_{p}, \forall p$ 成立. 由帕塞瓦尔 (Parseval) 等式知

$$
\sum_{k=1}^{n}\left|y_{k}\right|^{2}=\sum_{k=1}^{n-1}\left|y_{k}\right|^{2}=\sum_{k=1}^{n} x_{k}^{2}=1
$$

且我们注意到

$$
\begin{aligned}
\sum_{c=1}^{n} x_{c} x_{c+j} & =\frac{1}{n} \sum_{c=1}^{n} \sum_{s, t=1}^{n} w^{-s c} \cdot w^{-t(c+j)} y_{s} y_{t} \\
& =\frac{1}{n} \sum_{s, t=1}^{n} y_{s} y_{t} \cdot w^{-t j} \sum_{c=1}^{n} w^{-(s+t) c} \\
& =\sum_{p=1}^{n} y_{n-p} y_{p} w^{-p j} \\
& =\sum_{p=1}^{n}\left|y_{p}\right|^{2} w^{-p j}=\sum_{p=1}^{n-1}\left|y_{p}\right|^{2} \cos \frac{2 p j \pi}{n}
\end{aligned}
$$

故

$$
F=\sum_{j=1}^{t-1}\left[(t-j) \sum_{p=1}^{n-1}\left|y_{p}\right|^{2} \cos \frac{2 p j \pi}{n}\right]=\sum_{p=1}^{n-1}\left|y_{p}\right|^{2}\left(\sum_{j=1}^{t-1}(t-j) \cos \frac{2 p j \pi}{n}\right) .
$$

又由 Abel 和式变换及三角恒等式知,

$$
\begin{aligned}
\sum_{j=1}^{t-1}(t-j) \cos \frac{2 p j \pi}{n} & =\sum_{j=1}^{t-1}\left(\cos \frac{2 p \pi}{n}+\cdots+\cos \frac{2 j p \pi}{n}\right) \\
& =\sum_{j=1}^{t-1}\left(\frac{\sin (2 j+1) \frac{p \pi}{n}}{2 \sin \frac{p \pi}{n}}-\frac{1}{2}\right) \\
& =\frac{1}{2 \sin \frac{p \pi}{n}} \sum_{j=1}^{t-1} \sin (2 j+1) \frac{p \pi}{n}-\frac{t-1}{2} \\
& =\frac{\cos \frac{2 p \pi}{n}-\cos \frac{2 t p \pi}{n}}{4 \sin ^{2} \frac{p \pi}{n}}-\frac{t-1}{2}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{4 \sin ^{2} \frac{p \pi}{n}}\left(2 \sin ^{2} \frac{t p \pi}{n}-2 \sin ^{2} \frac{p \pi}{n}\right)-\frac{t-1}{2} \\
& =\frac{\sin ^{2} \frac{t p \pi}{n}}{2 \sin ^{2} \frac{p \pi}{n}}-\frac{t}{2} .
\end{aligned}
$$

故我们只需考察 $\left|\frac{\sin \frac{t p \pi}{p}}{\sin \frac{n}{n}}\right|$ 对于 $p=1,2, \cdots, n-1$ 的最大值.

注意到

$$
\left|\frac{\sin \frac{t p \pi}{n}}{\sin \frac{p \pi}{n}}\right|=\left|\frac{\sin \frac{t(n-p) \pi}{n}}{\sin \frac{(n-p) \pi}{n}}\right|
$$

即对于 $\left|y_{p}\right|^{2},\left|y_{n-p}\right|^{2}$, 它们有相同的系数. 故只需考虑 $\frac{p \pi}{n} \leq \frac{\pi}{2}$, 即 $p \leq \frac{n}{2}$ 的情况.

为此给出以下引理:

引理 $f(\theta)=\frac{\sin t \theta}{\sin \theta}$ 在 $\theta \in\left(0, \frac{\pi}{2 t}\right]$ 时单调递减, 其中 $t$ 为大于等于 2 的正整数.

证明 我们只需说明 $f^{\prime}(\theta)=\frac{t \sin \theta \cos t \theta-\cos \theta \sin t \theta}{\sin ^{2} \theta}$ 在 $\left(0, \frac{\pi}{2 t}\right]$ 上均小于等于零.

$\theta=\frac{\pi}{2 t}$ 时, $f^{\prime}(\theta)=-\frac{\cos \theta}{\sin ^{2} \theta}<0$.

$\theta \in\left(0, \frac{\pi}{2 t}\right)$ 时,

$$
f^{\prime}(\theta)=\frac{\cos \theta \cos t \theta(t \cdot \tan \theta-\tan t \theta)}{\sin ^{2} \theta} .
$$

令 $g(\theta)=t \cdot \tan \theta-\tan t \theta$. 则

$$
g^{\prime}(\theta)=\frac{t}{\cos ^{2} \theta}-\frac{t}{\cos ^{2} t \theta}
$$

又由当 $\theta \in\left[0, \frac{\pi}{2 t}\right)$ 时, $\cos \theta \geq \cos t \theta>0$, 则对任意 $\theta \in\left[0, \frac{\pi}{2 t}\right), g^{\prime}(\theta) \leq 0$. 故 $g(\theta) \leq g(0)=0$, 且 $\theta \neq 0$ 时, $g(\theta)<0$, 则对任意 $\theta \in\left(0, \frac{\pi}{2 t}\right], f^{\prime}(\theta)<0$

故 $f(\theta)$ 在 $\left(0, \frac{\pi}{2 t}\right]$ 上单调递减.


且当 $\frac{t p \pi}{n}>\frac{\pi}{2}, p \leq \frac{n}{2}$ 时, $\sin \frac{p \pi}{n}>\sin \frac{\pi}{2 t},\left|\sin \frac{t p \pi}{n}\right| \leq 1$. 故

$$
\left|\frac{\sin \frac{t p \pi}{n}}{\sin \frac{p \pi}{n}}\right|<\frac{1}{\sin \frac{\pi}{2 t}} \leq\left|\frac{\sin \frac{t \pi}{n}}{\sin \frac{\pi}{n}}\right|
$$

则可知对任意 $1 \leq p \leq n-1,\left|y_{1}\right|^{2},\left|y_{n-1}\right|^{2}$ 的系数最大. 故

$$
F \leq \frac{\sin ^{2} \frac{t \pi}{n}}{2 \sin ^{2} \frac{\pi}{n}}-\frac{t}{2}
$$

代入原式知

$$
\sum_{k=1}^{n}\left(x_{k}+x_{k+1}+\cdots+x_{k+t-1}\right)^{2} \leq t+2\left(\frac{\sin ^{2} \frac{t \pi}{n}}{2 \sin ^{2} \frac{\pi}{n}}-\frac{t}{2}\right)=\frac{\sin ^{2} \frac{t \pi}{n}}{\sin ^{2} \frac{\pi}{n}}
$$

即

$$
\sum_{k=1}^{n}\left(x_{k}+x_{k+1}+\cdots+x_{k+t-1}\right)^{2} \leq \frac{\sin ^{2} \frac{t \pi}{n}}{\sin ^{2} \frac{\pi}{n}} \sum_{k=1}^{n} x_{k}^{2}
$$

接下来考察取等条件, 则有 $y_{2}=\cdots=y_{n-2}=0$. 则我们可以得到 $g(z) \mid f(z)$,
其中

$$
f(z)=\sum_{k=1}^{n} x_{k} \cdot z^{k}, \quad g(z)=z(z-1) \prod_{k=2}^{n-2}\left(z-w^{k}\right)
$$

这是由于 $f(0)=0, f(1)=\sum_{k=1}^{n} x_{k}=0$, 且 $y_{p}=\frac{1}{\sqrt{n}} \sum_{k=1}^{n} x_{k} \cdot w^{p k}, p=2, \cdots, n-2$ 均为 0 . 则我们可以知道取等的向量 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\top}$ 构成的向量空间维数是 2 .

我们考虑特解 $\vec{\alpha}=\left(\cos \frac{2 \pi}{n}, \cdots, \cos \frac{2 n \pi}{n}\right)^{\top}$ 和 $\vec{\beta}=\left(\sin \frac{2 \pi}{n}, \cdots, \sin \frac{2 n \pi}{n}\right)^{\top}$. 由于 $n \geq 4$, 我们容易知道 $\vec{\alpha}, \vec{\beta}$ 线性无关, 由向量的性质, 则

$$
\left(x_{1}, \cdots, x_{n}\right)^{\top}=A \vec{\alpha}+B \vec{\beta}, A, B \in \mathbb{R} .
$$

故 $x_{k}=A \cos \frac{2 k \pi}{n}+B \sin \frac{2 k \pi}{n}, k=1,2, \cdots, n$ 时等号成立.

注 该不等式可看作 Fan 不等式的推广, 且与 Fan 不等式取等相同, 实在让人感到惊讶. 从以上的方法可以看出, 离散傅里叶变换能很好地处理与交项求和有关的不等式问题.

若我们使用 Lagrange 乘子, 我们可以发现该不等式的系数实际上与以下矩阵的特征值有关:

$$
\left(\begin{array}{ccccccc}
t & t-1 & t-2 & \cdots & 1 & \cdots & t-1 \\
t-1 & t & t-1 & \cdots & \cdots & \cdots & t-2 \\
\cdots & t-1 & t & \cdots & \cdots & \cdots & \cdots \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
\cdots & \cdots & \cdots & \cdots & \cdots & t & t-1 \\
t-1 & \cdots & \cdots & 1 & \cdots & t-1 & t
\end{array}\right)
$$

该矩阵的最大特征值为 $t^{2}$, 次大特征值为 $\left(\frac{\sin \frac{t \pi}{n}}{\sin \frac{\pi}{n}}\right)^{2}$, 特征值 $t^{2}$ 对应系数 $t^{2}$, 但此时 $x_{1}=x_{2}=\cdots=x_{n}=0$, 故最优系数应为 $\left(\frac{\sin \frac{t \pi}{n}}{\sin \frac{\pi}{n}}\right)^{2}$.

致谢 最后, 感谢冷岗松教授和吴尉迟老师. 他们对本文进行了认真的修订, 提出了诸多建议, 使得这篇文章结构更为完善, 论证更为严谨.

## 参考文献

[1] 韩京俊. 代数不等式: 证明方法 [M]. 合肥: 中国科学技术大学出版社, 2023.3

[2] 丘维声. 高等代数 (第二版: 上册) [M]. 北京: 清华大学出版社, 2019

[3] 王康印. 2023 年韩国数学奥林匹克试题解析 [J]. 数学新星网. 学生专栏, 2023-06-07 期.


[^0]:    修订日期: 2023-09-12.

