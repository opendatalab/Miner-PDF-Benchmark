# 数学新星问题征解第十期解答 

2016.02

第一题. 设实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $x_{1}+x_{2}+\cdots+x_{n}=0$. 证明:

$$
\frac{(n-2) x_{1}^{2}+2 x_{1}}{(n-1) x_{1}^{2}+1}+\frac{(n-2) x_{2}^{2}+2 x_{2}}{(n-1) x_{2}^{2}+1}+\cdots+\frac{(n-2) x_{n}^{2}+2 x_{n}}{(n-1) x_{n}^{2}+1} \geq 0 .
$$

(辽宁省实验中学 赵斌 供题)

## 证法一 (根据湖南师大附中刘俊文同学的解答整理):

原不等式等价于

$$
\sum_{i=1}^{n}\left(\frac{(n-2) x_{i}^{2}+2 x_{i}}{(n-1) x_{i}^{2}+1}-1\right) \geq-n
$$

即

$$
\sum_{i=1}^{n} \frac{\left(x_{i}-1\right)^{2}}{(n-1) x_{i}^{2}+1} \leq n
$$

考虑到

$$
\frac{\left(x_{i}-1\right)^{2}}{(n-1) x_{i}^{2}+1}=\frac{n}{n-1}-\frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}}
$$

则

$$
\begin{aligned}
n-\sum_{i=1}^{n-1} \frac{\left(x_{i}-1\right)^{2}}{(n-1) x_{i}^{2}+1} & =n-\sum_{i=1}^{n-1}\left(\frac{n}{n-1}-\frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}}\right) \\
& =\sum_{i=1}^{n-1} \frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}} .
\end{aligned}
$$

故 (1) 式等价于

$$
\frac{\left(x_{n}-1\right)^{2}}{(n-1) x_{n}^{2}+1} \leq \sum_{i=1}^{n-1} \frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}}
$$

不妨设 $\left|x_{n}\right|=\max \left\{\left|x_{1}\right|,\left|x_{2}\right|, \cdots,\left|x_{n}\right|\right\}$, 则由 Cauchy 不等式, 得

$$
\begin{aligned}
\left((n-1) x_{n}^{2}+1\right) \sum_{i=1}^{n-1} \frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}} & \geq\left(\sum_{j=1}^{n-1} x_{j}^{2}+1\right) \sum_{i=1}^{n-1} \frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}} \\
& =\sum_{j=1}^{n-1}\left(x_{j}^{2}+\frac{1}{n-1}\right) \sum_{i=1}^{n-1} \frac{\left(x_{i}+\frac{1}{n-1}\right)^{2}}{x_{i}^{2}+\frac{1}{n-1}}
\end{aligned}
$$

$$
\begin{aligned}
& \geq\left(\sum_{i=1}^{n-1}\left(x_{i}+\frac{1}{n-1}\right)\right)^{2} \\
& =\left(1-x_{n}\right)^{2}
\end{aligned}
$$

故 (2) 式成立, 且仅当 $x_{1}=\cdots=x_{n}=0$ 或者 $\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$ 中有一个为 1 , 其余为 $-\frac{1}{n-1}$ 时, (2) 式取到等号. 从而本题得证.

## 证法二 (根据复旦附中吴嘉诚同学的解答整理):

原不等式等价于

$$
\sum_{i=1}^{n}\left(\frac{(n-2)(n-1) x_{i}^{2}+2(n-1) x_{i}}{(n-1) x_{i}^{2}+1}+1\right) \geq n
$$

整理, 即等价证明

$$
\sum_{i=1}^{n} \frac{\left((n-1) x_{i}+1\right)^{2}}{(n-1) x_{i}^{2}+1} \geq n
$$

不妨设 $\left|x_{n}\right|=\max \left\{\left|x_{1}\right|,\left|x_{2}\right|, \cdots,\left|x_{n}\right|\right\}$, 则由 Cauchy 不等式, 得

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{\left((n-1) x_{i}+1\right)^{2}}{(n-1) x_{i}^{2}+1} & =\sum_{i=1}^{n-1} \frac{\left((n-1) x_{i}+1\right)^{2}}{(n-1) x_{i}^{2}+1}+\frac{\left((n-1) x_{n}+1\right)^{2}}{(n-1) x_{n}^{2}+1} \\
& \geq \frac{\left((n-1) \sum_{i=1}^{n-1} x_{i}+n-1\right)^{2}}{(n-1) \sum_{i=1}^{n-1} x_{i}^{2}+(n-1)}+\frac{\left((n-1) x_{n}+1\right)^{2}}{(n-1) x_{n}^{2}+1} \\
& \geq \frac{(n-1)^{2}\left(1-x_{n}\right)^{2}}{(n-1)\left((n-1) x_{n}^{2}+1\right)}+\frac{\left((n-1) x_{n}+1\right)^{2}}{(n-1) x_{n}^{2}+1} \\
& =n .
\end{aligned}
$$

故 (1) 式成立, 且仅当 $x_{1}=\cdots=x_{n}=0$ 或者 $\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$ 中有一个为 1 , 其余为 $-\frac{1}{n-1}$ 时, (1) 式取到等号. 从而本题得证.

评注 东北师大附中孙伟舰同学、湖南省雅礼中学胡东健、黄否、李师铨、王文瑞、尹龙晖、刘哲成、肖尧等同学也给出了本题的正确解答.

第二题. 证明: 方程 $p^{p}-(p-1)^{p-1}=n^{2}$ 没有 $p$ 为素数且 $n$ 为整数的解.

(广西南宁市第二中学学生 陈宝麟 供题)

## 证明 (根据东北师范大学附属中学孙伟舰同学的解答整理):

当 $p=2$ 时, $p^{p}-(p-1)^{p-1}=3$ 不是完全平方数.
下设 $p \geq 3$. 用反证法, 假设存在满足条件的 $p, n$, 使得

$$
p^{p}=(p-1)^{p-1}+n^{2} .
$$

由于 $p$ 是奇素数, 则 $(p-1)^{p-1} \equiv 0(\bmod 4)$, 从而 $n$ 为奇数, 故 $p^{p} \equiv n^{2} \equiv 1$ $(\bmod 4)$, 因此 $p \equiv 1(\bmod 4)$.

我们需要用到如下引理.

引理. 设素数 $p \equiv 1(\bmod 4)$, 则对任意正整数 $n$, 不定方程 $p^{n}=x^{2}+y^{2}$ 有且仅有一组使得 $(x, y)=1$ 的正整数解.

引理证明 当 $n=1$ 时, 由费马二平方和定理知, $p=x^{2}+y^{2}$ 有且仅有一组 $0<x<y$ 的正整数解 $\left(x_{1}, y_{1}\right)$.

注意到对任意正整数 $n$,

$$
x_{n}=\left|\frac{\left(x_{1}+y_{1} \mathrm{i}\right)^{n}+\left(x_{1}-y_{1} \mathrm{i}\right)^{n}}{2}\right|, \quad y_{n}=\left|\frac{\left(x_{1}+y_{1} \mathrm{i}\right)^{n}-\left(x_{1}-y_{1} \mathrm{i}\right)^{n}}{2 \mathrm{i}}\right|,
$$

是不定方程 $p^{n}=x^{2}+y^{2}$ 的解. 若 $\left(x_{n}, y_{n}\right)>1$, 则 $\left(x_{n}, y_{n}\right) \mid p^{n}$, 从而 $p \mid\left(x_{n}, y_{n}\right)$,即 $p \mid x_{n}$, 而

$$
\begin{aligned}
x_{n} & =\left|\frac{\left(x_{1}+y_{1} \mathrm{i}\right)^{n}+\left(x_{1}-y_{1} \mathrm{i}\right)^{n}}{2}\right|=\left|\sum_{k=0}^{\left[\frac{n}{2}\right]} \mathrm{C}_{n}^{2 k} x_{1}^{n-2 k}\left(y_{1} \mathrm{i}\right)^{2 k}\right| \\
& =\left|\sum_{k=0}^{\left[\frac{n}{2}\right]} \mathrm{C}_{n}^{2 k} x_{1}^{n-2 k}\left(-y_{1}^{2}\right)^{k}\right| \equiv \pm \sum_{k=0}^{\left[\frac{n}{2}\right]} \mathrm{C}_{n}^{2 k} x_{1}^{n-2 k}\left(x_{1}\right)^{2 k} \\
& = \pm x_{1}^{n} \sum_{k=0}^{\left[\frac{n}{2}\right]} \mathrm{C}_{n}^{2 k}= \pm 2^{n-1} x_{1}^{n} \not \equiv 0 \quad(\bmod p) .
\end{aligned}
$$

故 $p^{n}=x^{2}+y^{2}$ 有互质的正整数解 $\left(x_{n}, y_{n}\right)$.

下证方程仅有这组互质整数解. 若存在两组互质解 $(x, y),(z, w)$, 满足 $x<z<w<y, x^{2}+y^{2}=z^{2}+w^{2}$, 则 $(z+x)(z-x)=(y+w)(y-w)$. 设

$$
z-x=a c, \quad z+x=b d, \quad y-w=a d, \quad y+w=b c, \quad a, b, c, d \in \mathbb{N}^{*}
$$

从而

$$
x=\frac{b d-a c}{2}, y=\frac{b c+a d}{2}, z=\frac{a c+b d}{2}, w=\frac{b c-a d}{2} .
$$

则

$$
p^{n}=x^{2}+y^{2}=\frac{1}{4}\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right) \text {. }
$$

又 $a c+b d \neq b c+a d$, 则 $a \neq b, c \neq d$, 从而 $a^{2}+b^{2}, c^{2}+d^{2}>4$, 故 $p\left|\left(a^{2}+b^{2}\right), p\right|$ $\left(c^{2}+d^{2}\right)$. 于是 $a^{2} c^{2} \equiv b^{2} d^{2}(\bmod p)$, 即 $a c \equiv b d(\bmod p)$ 或 $a c \equiv-b d(\bmod p)$.因此 $p \mid x$ 或 $p \mid z$, 这与 $(x, y)=(z, w)=1$ 矛盾!
故 $p^{n}=x^{2}+y^{2}$ 只有一组互质的正整数解. 引理得证.

回到原题. 设 $p=x_{1}^{2}+y_{1}^{2}$, 由于 $p^{p}=\left((p-1)^{\frac{p-1}{2}}\right)^{2}+x^{2}$, 则

$$
\begin{aligned}
1 \equiv(p-1)^{p-1} & =\left(\frac{\left(x_{1}+y_{1} \mathrm{i}\right)^{p}+\left(x_{1}-y_{1} \mathrm{i}\right)^{p}}{2}\right)^{2} \\
& \equiv\left(2^{p-1} x_{1}^{p}\right)^{2} \equiv x_{1}^{2} \quad(\bmod p),
\end{aligned}
$$

或者

$$
\begin{aligned}
1 \equiv(p-1)^{p-1} & =\left(\frac{\left(x_{1}+y_{1} \mathrm{i}\right)^{p}-\left(x_{1}-y_{1} \mathrm{i}\right)^{p}}{2 \mathrm{i}}\right)^{2} \\
& \equiv-\left(2^{p-1} x_{1}^{p}\right)^{2} \equiv-x_{1}^{2} \equiv y_{1}^{2} \quad(\bmod p)
\end{aligned}
$$

又 $0<x_{1}<y_{1}<\sqrt{p}$, 则 $x_{1}=1$ 或者 $y_{1}=1$.

若 $x_{1}=1$, 则

$$
\begin{aligned}
(p-1)^{p-1} & =\left(\frac{(1+\sqrt{p-1} \mathrm{i})^{p}+(1-\sqrt{p-1 \mathrm{i}})^{p}}{2}\right)^{2} \\
& =\left(\sum_{k=0}^{\left[\frac{p}{2}\right]} \mathrm{C}_{p}^{2 k}(-1)^{k}(p-1)^{2 k}\right)^{2} \equiv 1 \quad(\bmod p-1),
\end{aligned}
$$

矛盾!

若 $y_{1}=1$, 则

$$
\begin{aligned}
(p-1)^{p-1} & =\left(\frac{(1+\sqrt{p-1} \mathrm{i})^{p}-(1-\sqrt{p-1} \mathrm{i})^{p}}{2 \mathrm{i}}\right)^{2} \\
& =\sum_{k=0}^{\left[\frac{p}{2}\right]} \frac{\mathrm{C}_{p}^{2 k+1}(i \sqrt{p-1})^{2 k+1}}{i}=\left(\sum_{k=0}^{\left[\frac{p}{2}\right]} \mathrm{C}_{p}^{2 k+1}(-1)^{k}(\sqrt{p-1})^{2 k+1}\right)^{2} \\
& =(p-1)\left(\sum_{k=0}^{\left[\frac{p}{2}\right]} \mathrm{C}_{p}^{2 k+1}(-1)^{k}(p-1)^{k}\right)^{2} \equiv p-1 \quad\left(\bmod (p-1)^{2}\right),
\end{aligned}
$$

矛盾!

综上, 方程 $p^{p}-(p-1)^{p-1}=n^{2}$ 没有 $p$ 为素数且 $n$ 为整数的解.

评注 湖南省雅礼中学刘哲成同学也给出了本题的正确解答.

第三题. 若正整数 $k$ 的任一素因子 $p$ 均满足 $p \equiv 1(\bmod 12)$. 证明: 存在无穷多组三元等差序列 $(x, y, z)$ 满足 $x y+k, y z+k, z x+k$ 均为完全平方数.

(浙江省富阳中学学生 黄吴中 供题)

## 证明 (根据湖南省雅礼中学邱添同学的解答整理):

我们先证明如下两个引理.
引理 1. 若 $p$ 为素数且 $p \equiv 1(\bmod 1) 2$, 则对任意 $\alpha \in \mathbb{N}_{+}$, 存在 $x \in \mathbb{N}_{+}$, 使得 $x^{2} \equiv 3\left(\bmod p^{\alpha}\right)$.

证明 对 $\alpha$ 归纳证明. 当 $\alpha=1$ 时, 由二次互反律知

$$
\left(\frac{3}{p}\right) \cdot\left(\frac{p}{3}\right)=(-1)^{\frac{3-1}{2} \cdot \frac{p-1}{2}}=1
$$

由于 $p \equiv 1(\bmod 3)$, 则 $\left(\frac{p}{3}\right)=1$, 从而 $\left(\frac{3}{p}\right)=1$, 即存在 $x \in \mathbb{N}_{+}$, 使得 $x^{2} \equiv 3$ $(\bmod p)$.

假设结论对 $\alpha$ 成立, 即存在 $x_{0} \in \mathbb{N}_{+}$, 使得 $x_{0}^{2} \equiv 3\left(\bmod p^{\alpha}\right)$. 下面考虑 $\alpha+1$ 的情形.

设 $x_{0}^{2}=p^{\alpha} \cdot t+3, t \in \mathbb{N}$, 取 $x=x_{0}+y \cdot p^{\alpha}, y \in \mathbb{N}$, 则

$$
\begin{aligned}
x^{2} & =x_{0}^{2}+2 x_{0} y p^{\alpha}+y^{2} p^{2 \alpha}=p^{\alpha}\left(t+2 x_{0} y\right)+y^{2} p^{2 \alpha}+3 \\
& \equiv p^{\alpha}\left(t+2 x_{0} y\right)+3 \quad\left(\bmod p^{\alpha+1}\right) .
\end{aligned}
$$

则 $x_{0}^{2} \equiv 3\left(\bmod p^{\alpha+1}\right)$ 当且仅当 $2 x_{0} y+t \equiv 0(\bmod p)$.

因为 $x_{0} \equiv 3\left(\bmod p^{\alpha}\right)$, 则 $(x, p)=1$, 又 $(2, p)=1$, 从而 $(2 x, p)=1$. 故 $2 x_{0} y+t \equiv 0(\bmod p)$ 必有解. 因此存在 $x \in \mathbb{N}_{+}$, 使得 $x^{2} \equiv 3\left(\bmod p^{\alpha+1}\right)$. 故结论对 $\alpha+1$ 成立.

综上, 引理得证.

引理 2. 方程 $x^{2}-3 y^{2}=k$ 有无穷多组正整数解.

证明 设 $k$ 的标准分解式为 $k=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{n}^{\alpha_{n}}$, 其中 $p_{1}, p_{2}, \cdots, p_{n}$ 为互不相同的素数, $\alpha_{i} \in \mathbb{N}_{+}, i=1,2, \cdots, n$. 因为 $p_{i} \equiv 1(\bmod 12), i=1,2, \cdots, n$, 则由引理 1 知, 存在 $x_{i} \in \mathbb{N}_{+}$, 使得 $x_{i}^{2} \equiv 3\left(\bmod p_{i}^{\alpha_{i}}\right)$.

考虑同余方程组 $x \equiv x_{i}\left(\bmod p_{i}^{\alpha_{i}}\right), i=1,2, \cdots, n$. 由于 $p_{1}^{\alpha_{1}}, p_{2}^{\alpha_{2}}, \cdots, p_{n}^{\alpha_{n}}$两两互素, 由孙子定理, 得此方程组必有解 $x \equiv a(\bmod k)$, 则 $a^{2} \equiv 3(\bmod k)$,从而 $a^{2}-3 x_{1} \equiv 0(\bmod k)$. 故存在 $x, y \in \mathbb{N}$, 使得 $x^{2}-3 y^{2} \equiv 0(\bmod k)$.

设 $\left(x_{0}, y_{0}\right)$ 是满足 $x_{0}^{2}-3 y_{0}^{2}=m k(m \in \mathbb{Z})$ 且使 $m \neq 0$ 的 $m$ 的绝对值最小的一组解. 若 $|m| \geq 2$, 取 $r \equiv x_{0}(\bmod m), s \equiv y_{0}(\bmod m)$ 且 $-\frac{m}{2}<r, s \leq \frac{m}{2}$,则 $r^{2}-3 s^{2} \equiv x_{0}^{2}-3 y_{0}^{2} \equiv 0(\bmod m)$. 设 $r^{2}-3 s^{2}=m^{\prime} m(m \in \mathbb{Z})$, 注意到

$$
\left(r^{2}-3 s^{2}\right) \cdot\left(x_{0}^{2}-3 y_{0}^{2}\right)=\left(r x_{0}-3 s y_{0}\right)^{2}-3\left(r y_{0}-s x_{0}\right)^{2}
$$

故

$$
\left(\frac{r x_{0}-3 s y_{0}}{m}\right)^{2}-3\left(\frac{r y_{0}-s x_{0}}{m}\right)^{2}=m^{\prime} k .
$$

由于 $r x_{0}-3 s y_{0} \equiv x_{0}^{2}-3 y_{0}^{2} \equiv 0(\bmod m)$, 则 $\frac{r x_{0}-3 s y_{0}}{m}, \frac{r y_{0}-s x_{0}}{m} \in \mathbb{Z}$, 故 $x=$
$\left|\frac{r x_{0}-3 s y_{0}}{m}\right|, y=\left|\frac{r y_{0}-s x_{0}}{m}\right|$ 也是同余方程 $x^{2}-3 y^{2} \equiv 0(\bmod k)$ 的一组解.

若 $m^{\prime}=0$, 则 $r^{2}=3 s^{2}$, 即 $r=s=0$, 从而 $x_{0}=y_{0}=0$, 那么 $m=0$, 矛盾!

若 $m^{\prime} \neq 0$, 由 $-\frac{3}{4} m^{2} \leq r^{2}-3 s^{2}=m^{\prime} m \leq \frac{m^{2}}{4}$, 得 $\left|m^{\prime}\right| \leq \frac{3}{4}|m|<|m|$, 这与 $|m|$ 的最小性矛盾.

故 $|m|=1$. 若 $m=-1$, 由 $x_{0}^{2}-3 y_{0}^{2}=-k$ 两边取模 3 得 $x_{0}^{2} \equiv-1(\bmod 3)$,矛盾! 因此 $m=1$. 故而存在 $u, v \in \mathbb{N}_{+}$, 使得 $u^{2}-3 v^{2}=k$.

已知 Pell 方程 $x^{2}-3 y^{2}=1$ 的基本解为 $x=2, y=1$, 其全部解由 $x_{n}+\sqrt{3} y_{n}=(2+\sqrt{3})^{n}\left(x_{n}, y_{n} \in \mathbb{N}_{+}\right)$给出. 取 $x=u x_{n}+3 v y_{n}, y=v x_{n}+u y_{n}$,则

$$
x^{2}-3 y^{2}=\left(u^{2}-3 v^{2}\right) x_{n}^{2}-3\left(u^{2}-3 v^{2}\right) y_{n}^{2}=k\left(x_{n}^{2}-3 y_{n}^{2}\right)=k .
$$

由数组 $\left(x_{n}, y_{n}\right)$ 的无穷性知方程 $x^{2}-3 y^{2}=k$ 有无穷多组正整数解. 引理证毕.

回到原题. 取 $x=2 a-b, y=2 a, z=2 a+b$, 其中 $a, b$ 满足 $b^{2}-3 a^{2}=k$, 则

$$
x y+k=(a-b)^{2}, y z+k=(a+b)^{2}, x z+k=a^{2}
$$

均为完全平方数. 由引理 2 知这样的数组 $(x, y, z)$ 有无穷多组.

评注 东北师大附中孙伟舰、复旦附中吴嘉诚、大连育明高中王瑞、成都七中王怡欣、湖南省雅礼中学刘哲成、肖尧、段剑儒等同学也给出了本题的正确解答.

第四题. 设 $I$ 是 $\triangle A B C$ 的内心, $I_{1}, I_{2}, I_{3}$ 分别是顶点 $A, B, C$ 所对的旁心.内切圆 $\odot I$ 分别与边 $B C, A C, A B$ 相切于点 $D, E, F$, 旁切圆 $\odot I_{1}, \odot I_{2}, \odot I_{3}$ 分别与边 $B C, A C, A B$ 相切于点 $D^{\prime}, E^{\prime}, F^{\prime}$. 设 $Q$ 是 $I_{2} E$ 和 $I_{3} F$ 的交点, $T$ 是 $\angle B A C$的角平分线与 $B C$ 的交点. 作 $T N \perp B C$ 交 $I D^{\prime}$ 于 $N, M$ 是 $Q I$ 的中点. 证明: $\angle B A N=\angle C A M$.

(云南师范大学附属中学学生 徐恺, 中国人民大学附属中学学生 杨泓暕 供题)

## 证明 (根据浙江省象山县第三中学黄子宸同学的解答整理):

设 $\triangle A B C, \triangle I_{1} I_{2} I_{3}$ 的外心分别为 $O, O_{m}$, 延长 $A I$ 交 $\odot O$ 于 $L$, 设 $O I$ 交 $I_{1} D, I_{2} E, I_{3} F$ 于 $Q_{1}, Q_{2}, Q_{3}$.

易知 $I, O, O_{m}$ 分别是 $\triangle I_{1} I_{2} I_{3}$ 的垂心, 九点圆圆心以及外心, 由欧拉线定理, $I, O, O_{m}$ 共线, 且 $O I=O O_{m}$. 又由鸡爪定理, $L I=L I_{1}$, 故 $O_{m} I_{1} / / O L$. 而 $O L \perp B C, I D \perp B C$, 则 $I D / / O L$. 因此 $O_{m} I_{1} / / I D$, 从而 $\frac{Q_{1} I}{Q_{1} O_{m}}=\frac{I D}{O_{m} I_{1}}=\frac{r}{R}$. 同
理 $\frac{Q_{2} I}{Q_{2} O_{m}}=\frac{r}{R}, \frac{Q_{3} I}{Q_{3} O_{m}}=\frac{r}{R}$. 因此 $Q_{1}, Q_{2}, Q_{3}$ 重合, 即 $I_{1} D, I_{2} E, I_{3} F$ 共点于 $O I$ 上一点 $Q$, 且 $Q$ 是 $\odot I, \odot O_{m}$ 的位似中心.

延长 $I_{1} A$ 交 $\odot O_{m}$ 于 $R$, 联结 $R Q$ 交 $\odot I$ 于 $G$, 连接 $A D^{\prime}$ 交 $\odot I$ 于 $K$,联结 $K I$ 交 $A N$ 于 $S$. 因为 $\odot I, \odot O_{m}$ 关于 $Q$ 位似, 且 $G, R, D, I_{1}$ 是位似对应点, 从而 $D G / / R I_{1}$, 即 $D G \perp E F$. 又由于 $\odot I_{1}, \odot I$ 关于 $A$ 位似, 因此 $I_{1} D^{\prime} / / I K$, 从而 $K, I, D$ 共线. 进而 $\angle G D E=90^{\circ}-\angle D E F=\angle K D F$, 故 $F K=G E, \angle K F E=\angle G E F$. 又 $R F=R E$, 得 $\triangle R F K \cong \triangle R E G$, 从而 $\angle K R I=\angle G R I$.

对 $\triangle A D^{\prime} N$ 和截线 $K S I$ 应用 Menelaus 定理, 得

$$
\frac{I S}{S K}=\frac{D^{\prime} A}{A K} \cdot \frac{I N}{N D^{\prime}}=\frac{I_{1} D^{\prime}}{I K} \cdot \frac{D T}{T D^{\prime}}=\frac{I_{1} D^{\prime}}{I D} \cdot \frac{I D}{I_{1} D^{\prime}}=1 .
$$

即 $I S=S K$, 又 $I$ 是 $\triangle I_{1} I_{2} I_{3}$ 垂心, 则易得 $I A=A R$, 且 $I M=M Q$, 从而 $N S A / / K R, Q G R / / M A$, 结合 $\angle K R I=\angle G R I$ 得 $\angle N A I=\angle M A I$. 故 $\angle B A N=\angle C A M$.

![](https://cdn.mathpix.com/cropped/2024_02_26_bafc67bda73ac5102164g-7.jpg?height=1048&width=1128&top_left_y=1229&top_left_x=455)

评注 东北师大附中郭鹏、复旦附中吴嘉诚、大连育明高中王瑞、杭州外国语学校林家声、湖南省雅礼中学王文瑞、陈欣品等同学也给出了本题的正确解答.

