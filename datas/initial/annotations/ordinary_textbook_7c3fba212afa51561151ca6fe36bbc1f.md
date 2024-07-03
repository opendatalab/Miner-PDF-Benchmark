# 一道国家队选拔考试题的加强 

廖昱博<br>(中国人民大学附属中学,100080)<br>指导教师: 张端阳

2004 年中国国家队选拔考试的第三题 (余红兵教授提供 [1]) 是一道困难的整变量不等式:

问题 1 设整数 $1<a_{1}<a_{2}<\cdots<a_{n}, a, b$ 是正整数, 满足

$\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n}}\right) \leq \frac{a}{b}<\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n-1}}\right)$.

求证:

$$
a_{1} a_{2} \cdots a_{n} \leq(4 a)^{2^{n}-1}
$$

最近我们得到了该问题的最佳形式:

定理 设整数 $1<a_{1}<a_{2}<\cdots<a_{n}, a, b$ 是正整数, 满足

$\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n}}\right) \leq \frac{a}{b}<\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n-1}}\right)$.

则

$$
a_{1} a_{2} \cdots a_{n} \leq \frac{(a+1)^{2^{n}}-(a+1)^{2^{n-1}}}{a}
$$

定理的证明借鉴了匈牙利数学家 Paul Erdös 已经被解决的一个猜想的证明思想, 这个猜想也是关于整变量不等式的, 曾被选作 1987 年中国国家队选拔考试的第三题:

问题 2 设数列 $\left\{r_{n}\right\}$ 满足 $r_{1}=2, r_{n}=r_{1} r_{2} \cdots r_{n-1}+1, n \geq 2$. 正整数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $\sum_{i=1}^{n} \frac{1}{a_{i}}<1$. 求证:

$$
\sum_{i=1}^{n} \frac{1}{a_{i}} \leq \sum_{i=1}^{n} \frac{1}{r_{i}}
$$

修订日期: 2020-06-03.
其证明可以在 [2] 中第 124 页找到.

定理的证明 设数列 $\left\{t_{n}\right\}$ 满足 $t_{n}=(a+1)^{2^{n-1}}+1, n \geq 1$. 容易验证

$$
t_{1} t_{2} \cdots t_{n}=\frac{(a+1)^{2^{n}}-1}{a}
$$

且.

$$
\left(1-\frac{1}{t_{1}}\right)\left(1-\frac{1}{t_{2}}\right) \cdots\left(1-\frac{1}{t_{n-1}}\right)\left(1-\frac{1}{t_{n}-1}\right)=\frac{a}{a+1} .
$$

下面对 $n$ 用第二数学归纳法.

当 $n=1$ 时, 由 $1-\frac{1}{a_{1}} \leq \frac{a}{b}<1$, 知 $1-\frac{1}{a_{1}} \leq \frac{a}{a+1}$, 所以 $a_{1} \leq a+1$ 成立.

假设结论对小于 $n$ 的正整数都成立, 来看 $n$ 时的情形.

假设此时结论不成立, 即

$$
a_{1} a_{2} \cdots a_{n}>\frac{(a+1)^{2^{n}}-(a+1)^{2^{n-1}}}{a} .
$$

任取 $1 \leq i \leq n-1$, 因为

$$
\begin{aligned}
\left(1-\frac{1}{a_{i+1}}\right) \cdots\left(1-\frac{1}{a_{n}}\right) & \leq \frac{a a_{1} a_{2} \cdots a_{i}}{b\left(a_{1}-1\right)\left(a_{2}-1\right) \cdots\left(a_{i}-1\right)} \\
& <\left(1-\frac{1}{a_{i+1}}\right)\left(1-\frac{1}{a_{i+2}}\right) \cdots\left(1-\frac{1}{a_{n-1}}\right),
\end{aligned}
$$

所以由归纳假设，

$$
a_{i+1} a_{i+2} \cdots a_{n} \leq \frac{\left(a a_{1} a_{2} \cdots a_{i}+1\right)^{2^{n-i}}-\left(a a_{1} a_{2} \cdots a_{i}+1\right)^{2^{n-i-1}}}{a a_{1} a_{2} \cdots a_{i}}
$$

进而

$$
a_{1} a_{2} \cdots a_{n} \leq \frac{\left(a a_{1} a_{2} \cdots a_{i}+1\right)^{2^{n-i}}-\left(a a_{1} a_{2} \cdots a_{i}+1\right)^{2^{n-i-1}}}{a} .
$$

若 $a_{1} a_{2} \cdots a_{i} \leq t_{1} t_{2} \cdots t_{i}$, 则由(1),

$$
a a_{1} a_{2} \cdots a_{i}+1 \leq(a+1)^{2^{i}}
$$

代入上式得，

$$
\begin{aligned}
a_{1} a_{2} \cdots a_{n} & \leq \frac{\left((a+1)^{2^{i}}\right)^{2^{n-i}}-\left((a+1)^{2^{i}}\right)^{2^{n-i-1}}}{a} \\
& =\frac{(a+1)^{2^{n}}-(a+1)^{2^{n-1}}}{a},
\end{aligned}
$$

与反证假设矛盾! 故

$$
a_{1} a_{2} \cdots a_{i}>t_{1} t_{2} \cdots t_{i} .
$$

记 $t_{n}^{\prime}=\frac{a_{1} a_{2} \cdots a_{n}}{t_{1} t_{2} \cdots t_{n-1}}$, 则由

$$
a_{1} a_{2} \cdots a_{n}>\frac{(a+1)^{2^{n}}-(a+1)^{2^{n-1}}}{a}=t_{1} t_{2} \cdots t_{n-1}\left(t_{n}-1\right),
$$

得

$$
t_{n}^{\prime}>t_{n}-1>t_{n-1}>\cdots>t_{2}>t_{1}
$$

至此, 我们有

$$
\begin{gathered}
a_{1}>t_{1}, \\
a_{1} a_{2}>t_{1} t_{2}, \\
\cdots \\
a_{1} a_{2} \cdots a_{n-1}>t_{1} t_{2} \cdots t_{n-1}, \\
a_{1} a_{2} \cdots a_{n}=t_{1} t_{2} \cdots t_{n}^{\prime} .
\end{gathered}
$$

将以上 $n$ 个式子取倒数后再取对数得,

$$
\begin{aligned}
& \ln \frac{1}{a_{1}}<\ln \frac{1}{t_{1}}, \\
& \ln \frac{1}{a_{1}}+\ln \frac{1}{a_{2}}<\ln \frac{1}{t_{1}}+\ln \frac{1}{t_{2}}, \\
& \cdots \\
& \ln \frac{1}{a_{1}}+\ln \frac{1}{a_{2}}+\cdots+\ln \frac{1}{a_{n-1}}<\ln \frac{1}{t_{1}}+\ln \frac{1}{t_{2}}+\cdots+\ln \frac{1}{t_{n-1}}, \\
& \ln \frac{1}{a_{1}}+\ln \frac{1}{a_{2}}+\cdots+\ln \frac{1}{a_{n}}=\ln \frac{1}{t_{1}}+\ln \frac{1}{t_{2}}+\cdots+\ln \frac{1}{t_{n}^{\prime}} .
\end{aligned}
$$

又由 $a_{1}<a_{2}<\cdots<a_{n}$ 知

$$
\ln \frac{1}{a_{1}}>\ln \frac{1}{a_{2}}>\cdots>\ln \frac{1}{a_{n}}
$$

由 $t_{1}<t_{2}<\cdots<t_{n}^{\prime}$ 知

$$
\ln \frac{1}{t_{1}}>\ln \frac{1}{t_{2}}>\cdots>\ln \frac{1}{t_{n}^{\prime}}
$$

所以

$$
\left(\ln \frac{1}{a_{1}}, \ln \frac{1}{a_{2}}, \cdots, \ln \frac{1}{a_{n}}\right) \prec\left(\ln \frac{1}{t_{1}}, \ln \frac{1}{t_{2}}, \cdots, \ln \frac{1}{t_{n}^{\prime}}\right) .
$$

令函数 $f(x)=\ln \left(1-e^{x}\right)$, 则由

$$
f^{\prime \prime}(x)=-\frac{e^{x}}{\left(1-e^{x}\right)^{2}}<0
$$

知 $f(x)$ 在 $(-\infty, 0)$ 上是上凸函数. 于是由 Karamata 不等式,

$f\left(\ln \frac{1}{a_{1}}\right)+f\left(\ln \frac{1}{a_{2}}\right)+\cdots+f\left(\ln \frac{1}{a_{n}}\right) \geq f\left(\ln \frac{1}{t_{1}}\right)+f\left(\ln \frac{1}{t_{2}}\right)+\cdots+f\left(\ln \frac{1}{t_{n}^{\prime}}\right)$,
即

$$
\ln \left(1-\frac{1}{a_{1}}\right)+\cdots+\ln \left(1-\frac{1}{a_{n}}\right) \geq \ln \left(1-\frac{1}{t_{1}}\right)+\cdots+\ln \left(1-\frac{1}{t_{n}^{\prime}}\right) .
$$

所以结合(2),

$$
\begin{aligned}
\left(1-\frac{1}{a_{1}}\right) \cdots\left(1-\frac{1}{a_{n}}\right) & \geq\left(1-\frac{1}{t_{1}}\right)\left(1-\frac{1}{t_{2}}\right) \cdots\left(1-\frac{1}{t_{n}^{\prime}}\right) \\
& >\left(1-\frac{1}{t_{1}}\right)\left(1-\frac{1}{t_{2}}\right) \cdots\left(1-\frac{1}{t_{n-1}}\right)\left(1-\frac{1}{t_{n}-1}\right) \\
& =\frac{a}{a+1} .
\end{aligned}
$$

这样,

$$
\frac{a}{b} \geq\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n}}\right)>\frac{a}{a+1}
$$

从而 $b<a+1$, 这与 $\frac{a}{b}<1$ 矛盾!

另一方面, 当 $a_{i}=t_{i}(1 \leq i \leq n-1), a_{n}=t_{n}-1, b=a+1$ 时,

$$
\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n}}\right)=\frac{a}{b}<\left(1-\frac{1}{a_{1}}\right)\left(1-\frac{1}{a_{2}}\right) \cdots\left(1-\frac{1}{a_{n-1}}\right),
$$

且

$$
a_{1} a_{2} \cdots a_{n}=\frac{(a+1)^{2^{n}}-(a+1)^{2^{n-1}}}{a} .
$$

因此当给定 $n$ 和 $a$ 时, 定理的结果是最佳的.

综上, 定理得证.

值得一提的是, 用类似的思想也可以解决下面这道整变量不等式:

问题 3 设正整数 $a_{1}, a_{2}, \cdots, a_{n}$ 满足 $\prod_{i=1}^{n}\left(1+\frac{1}{a_{i}}\right)<2$. 求证:

$$
\prod_{i=1}^{n}\left(1+\frac{1}{a_{i}}\right) \leq 2-\frac{1}{2^{2^{n}-1}} .
$$

证明 设数列 $\left\{s_{n}\right\}$ 满足 $s_{n}=2^{2^{n-1}}, n \geq 1$. 容易验证

$$
\prod_{i=1}^{n}\left(1+\frac{1}{s_{i}}\right)=2-\frac{1}{s_{1} s_{2} \cdots s_{n}} .
$$

下面只需对 $n$ 用第二数学归纳法证明

$$
\prod_{i=1}^{n}\left(1+\frac{1}{a_{i}}\right) \leq \prod_{i=1}^{n}\left(1+\frac{1}{s_{i}}\right) .
$$

当 $n=1$ 时, 由 $1+\frac{1}{a_{1}}<2$, 知 $a_{1} \geq 2$, 所以

$$
1+\frac{1}{a_{1}} \leq 1+\frac{1}{2}=1+\frac{1}{s_{1}}
$$

成立.

假设结论对小于 $n$ 的正整数都成立, 来看 $n$ 时的情形.

假设此时结论不成立, 即

$$
\left(1+\frac{1}{a_{1}}\right)\left(1+\frac{1}{a_{2}}\right) \cdots\left(1+\frac{1}{a_{n}}\right)>\left(1+\frac{1}{s_{1}}\right)\left(1+\frac{1}{s_{2}}\right) \cdots\left(1+\frac{1}{s_{n}}\right) .
$$

由 $\left(1+\frac{1}{a_{1}}\right)\left(1+\frac{1}{a_{2}}\right) \cdots\left(1+\frac{1}{a_{n}}\right)<2$ 且 $a_{1}, a_{2}, \cdots, a_{n}$ 是正整数知,

$$
\left(1+\frac{1}{a_{1}}\right)\left(1+\frac{1}{a_{2}}\right) \cdots\left(1+\frac{1}{a_{n}}\right) \leq 2-\frac{1}{a_{1} a_{2} \cdots a_{n}} .
$$

又

$$
\left(1+\frac{1}{s_{1}}\right)\left(1+\frac{1}{s_{2}}\right) \cdots\left(1+\frac{1}{s_{n}}\right)=2-\frac{1}{s_{1} s_{2} \cdots s_{n}}
$$

所以

$$
\frac{1}{a_{1} a_{2} \cdots a_{n}}<\frac{1}{s_{1} s_{2} \cdots s_{n}}
$$

即

$$
a_{1} a_{2} \cdots a_{n}>s_{1} s_{2} \cdots s_{n} .
$$

另一方面, 我们证明 $a_{1} a_{2} \cdots a_{n} \leq s_{1} s_{2} \cdots s_{n}$, 从而得到矛盾.

不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 由归纳假设，

$$
\begin{aligned}
1+\frac{1}{a_{1}} & \leq 1+\frac{1}{s_{1}} \\
\left(1+\frac{1}{a_{1}}\right)\left(1+\frac{1}{a_{2}}\right) & \leq\left(1+\frac{1}{s_{1}}\right)\left(1+\frac{1}{s_{2}}\right), \\
& \ldots \\
\left(1+\frac{1}{a_{1}}\right)\left(1+\frac{1}{a_{2}}\right) \cdots\left(1+\frac{1}{a_{n-1}}\right) & \leq\left(1+\frac{1}{s_{1}}\right)\left(1+\frac{1}{s_{2}}\right) \cdots\left(1+\frac{1}{s_{n-1}}\right) .
\end{aligned}
$$

又由反证假设,

$$
\left(1+\frac{1}{a_{1}}\right)\left(1+\frac{1}{a_{2}}\right) \cdots\left(1+\frac{1}{a_{n}}\right)>\left(1+\frac{1}{s_{1}}\right)\left(1+\frac{1}{s_{2}}\right) \cdots\left(1+\frac{1}{s_{n}}\right) .
$$

将以上 $n$ 个式子取对数得,

$$
\begin{aligned}
\ln \left(1+\frac{1}{a_{1}}\right) & \leq \ln \left(1+\frac{1}{s_{1}}\right), \\
\ln \left(1+\frac{1}{a_{1}}\right)+\ln \left(1+\frac{1}{a_{2}}\right) & \leq \ln \left(1+\frac{1}{s_{1}}\right)+\ln \left(1+\frac{1}{s_{2}}\right), \\
& \ldots \\
\ln \left(1+\frac{1}{a_{1}}\right)+\cdots+\ln \left(1+\frac{1}{a_{n-1}}\right) & \leq \ln \left(1+\frac{1}{s_{1}}\right)+\cdots+\ln \left(1+\frac{1}{s_{n-1}}\right),
\end{aligned}
$$

$$
\ln \left(1+\frac{1}{a_{1}}\right)+\cdots+\ln \left(1+\frac{1}{a_{n}}\right)>\ln \left(1+\frac{1}{s_{1}}\right)+\cdots+\ln \left(1+\frac{1}{s_{n}}\right) .
$$

由后两行, 知存在 $a_{n}^{\prime}>a_{n}$, 使得

$$
\ln \left(1+\frac{1}{a_{1}}\right)+\cdots+\ln \left(1+\frac{1}{a_{n}^{\prime}}\right)=\ln \left(1+\frac{1}{s_{1}}\right)+\cdots+\ln \left(1+\frac{1}{s_{n}}\right) .
$$

又由 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}<a_{n}^{\prime}$, 知

$$
\ln \left(1+\frac{1}{a_{1}}\right) \geq \ln \left(1+\frac{1}{a_{2}}\right) \geq \cdots \geq \ln \left(1+\frac{1}{a_{n}^{\prime}}\right)
$$

由 $s_{1} \leq s_{2} \leq \cdots \leq s_{n}$, 知

$$
\ln \left(1+\frac{1}{s_{1}}\right) \geq \ln \left(1+\frac{1}{s_{2}}\right) \geq \cdots \geq \ln \left(1+\frac{1}{s_{n}}\right)
$$

所以

$$
\left(\ln \left(1+\frac{1}{a_{1}}\right), \cdots, \ln \left(1+\frac{1}{a_{n}^{\prime}}\right)\right) \prec\left(\ln \left(1+\frac{1}{s_{1}}\right), \cdots, \ln \left(1+\frac{1}{s_{n}}\right)\right)
$$

令函数 $f(x)=\ln \left(e^{x}-1\right)$, 则由 $f^{\prime \prime}(x)=-\frac{e^{x}}{\left(e^{x}-1\right)^{2}}<0$, 知 $f(x)$ 在 $(0,+\infty)$ 上

是上凸函数. 于是由 Karamata 不等式,

$f\left(\ln \left(1+\frac{1}{a_{1}}\right)\right)+\cdots+f\left(\ln \left(1+\frac{1}{a_{n}^{\prime}}\right)\right) \geq f\left(\ln \left(1+\frac{1}{s_{1}}\right)\right)+\cdots+f\left(\ln \left(1+\frac{1}{s_{n}}\right)\right)$,

故

$$
\ln \frac{1}{a_{1}}+\ln \frac{1}{a_{2}}+\cdots+\ln \frac{1}{a_{n}^{\prime}} \geq \ln \frac{1}{s_{1}}+\ln \frac{1}{s_{2}}+\cdots+\ln \frac{1}{s_{n}},
$$

即

$$
\frac{1}{a_{1} a_{2} \cdots a_{n}^{\prime}} \geq \frac{1}{s_{1} s_{2} \cdots s_{n}}
$$

所以

$$
a_{1} a_{2} \cdots a_{n}<a_{1} a_{2} \cdots a_{n}^{\prime} \leq s_{1} s_{2} \cdots s_{n}
$$

综上, 命题得证.

## 参考文献

[1] 2004 年 IMO 中国国家集训队教练组. 走向IMO: 数学奥林匹克试题集锦 (2004) [M]. 华东师范大学出版社, 2004.

[2] 熊斌, 苏勇. 不等式的证明方法与技巧, 数学奥林匹克小丛书 (第三版) 高中卷 $[\mathrm{M}]$. 华东师范大学出版社, 2020 .

