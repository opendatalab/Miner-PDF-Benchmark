# 第四十九期问题征解解答与点评 

## 张端阳

第一题 用 $\Omega(x)$ 表示正整数 $x$ 的最大素因子, 对正整数 $m, n$, 记

$$
f_{m, n}(x)=x^{\tau(\sigma(n) \varphi(n))+m}-1 .
$$

(1) 证明: 对任意正整数 $n$, 存在无穷多个正整数 $m$, 使得

$$
\Omega\left(f_{m, n}(x)\right)<\frac{1}{2}\left(f_{m, n}(x)\right)^{\frac{1}{2}}+\frac{3}{4}
$$

对任意大于 2 的整数 $x$ 成立;

(2) 证明: 对任意正整数 $m$, 存在无穷多个正整数 $n$, 使得

$$
\Omega\left(f_{m, n}(x)\right)<\left(f_{m, n}(x)\right)^{\frac{1}{2}}+\frac{3}{2}
$$

对任意大于 2 的整数 $x$ 成立.

(长沙一中学生 刘志源 供题)

## 证明 (根据北京一零一中学牟思特同学的解答整理):

(1) 取正整数 $m$, 使得 $6 \mid \tau(\sigma(n) \varphi(n))+m$, 这样的 $m$ 有无穷多个.

对这样的 $m$, 设 $\tau(\sigma(n) \varphi(n))+m=6 r$, 则

$$
f_{m, n}(x)=x^{6 r}-1=\left(x^{r}-1\right)\left(x^{r}+1\right)\left(x^{2 r}-x^{r}+1\right)\left(x^{2 r}+x^{r}+1\right) .
$$

所以

$$
\Omega\left(f_{m, n}(x)\right) \leq x^{2 r}+x^{r}+1 \leq \frac{1}{2}\left(x^{3 r}-1\right) \leq \frac{1}{2}\left(x^{6 r}-1\right)^{\frac{1}{2}}=\frac{1}{2}\left(f_{m, n}(x)\right)^{\frac{1}{2}},
$$

满足要求.

(2) 先证明两个引理.

引理 1 存在无穷多个正整数 $n$, 使得 $\sigma(n) \varphi(n)$ 不是完全平方数.

证明 取 $n$ 是素数, 则

$$
\sigma(n) \varphi(n)=(n+1)(n-1)=n^{2}-1
$$

不是完全平方数. 这样的 $n$ 有无穷多个.
引理 2 存在无穷多个正整数 $n$, 使得 $\sigma(n) \varphi(n)$ 是完全平方数.

证明 只需证明对任意正整数 $N$, 存在整数 $n>N$ 满足要求.

将素数从小到大排列为 $p_{1}, p_{2}, \cdots$.

取定正整数 $k$, 使得 $p_{k}>N$, 并待定充分大的正整数 $M$.

设

$$
\sigma\left(p_{k} \cdots p_{M}\right) \varphi\left(p_{k} \cdots p_{M}\right)=\prod_{i=k}^{M}\left(p_{i}+1\right)\left(p_{i}-1\right)
$$

的所有素因子为 $q_{1}<q_{2}<\cdots<q_{t}$, 则 $q_{t} \leq \frac{p_{M}+1}{2}$.

对 $\{k, k+1, \cdots, M\}$ 的任意非空子集 $I$, 记在 $\prod_{i \in I}\left(p_{i}+1\right)\left(p_{i}-1\right)$ 的素因数分解中, 指数为奇数的素数的下标集为 $T_{I}$, 则 $T_{I}$ 是 $\{1,2, \cdots, t\}$ 的子集.

由素数定理, 可取 $M$ 充分大, 使得区间 $\left(\frac{p_{M}+1}{2}, p_{M}\right)$ 中素数的个数超过 $k$. 结合 $q_{t} \leq \frac{p_{M}+1}{2}$ 知 $M \geq k+t$, 于是 $2^{M-k+1}-1>2^{t}$.

此时 $\{k, k+1, \cdots, M\}$ 的非空子集的个数多于 $\{1,2, \cdots, t\}$ 的子集的个数, 所以由抽屉原理, 存在 $\{k, k+1, \cdots, M\}$ 的不同的非空子集 $I, J$, 使得 $T_{I}=T_{J}$.

令

$$
n=\prod_{i \in I \triangle J} p_{i}
$$

其中 “ $\triangle$ ” 表示对称差, 则 $n \geq p_{k}>N$, 且 $\sigma(n) \varphi(n)$ 的素因数的指数均为偶数, 故 $\sigma(n) \varphi(n)$ 是完全平方数.

回到原题.

由引理 1,2 , 存在无穷多个正整数 $n$, 使得 $\tau(\sigma(n) \varphi(n))$ 是偶数, 也存在无穷多个正整数 $n$, 使得 $\tau(\sigma(n) \varphi(n))$ 是奇数. 这样对任意正整数 $m$, 存在无穷多个正整数 $n$, 使得 $\tau(\sigma(n) \varphi(n))+m$ 是偶数.

对这样的 $n$, 设 $\tau(\sigma(n) \varphi(n))+m=2 r$, 则

$$
f_{m, n}(x)=x^{2 r}-1=\left(x^{r}-1\right)\left(x^{r}+1\right) .
$$

所以

$$
\Omega\left(f_{m, n}(x)\right) \leq x^{r}+1<\left(x^{2 r}-1\right)^{\frac{1}{2}}+\frac{3}{2}=\left(f_{m, n}(x)\right)^{\frac{1}{2}}+\frac{3}{2},
$$

满足要求.

评注 (1). 引理 2 的证明方法在第 40 期征解第二题中也出现过.

(2). 邯郸市第一中学朱山珍和王浩宇同学指出, 证明 $\{\pi(2 n)-\pi(n)\}$ 无界有更初等的方法.
事实上, 假设对任意正整数 $n$, 区间 $(n, 2 n]$ 中素数的个数都不超过常数 $C$. 则

$$
\sum_{p \text { 为素数 }} \frac{1}{p}=\sum_{l=0}^{\infty} \sum_{\substack{p \text { 为素数 } \\ p \in\left(2^{2}, 2^{+1}\right]}} \frac{1}{p}<\sum_{l=0}^{\infty} \sum_{\substack{p \text { 为素数 } \\ p \in\left(2^{2}, 2^{+1}\right]}} \frac{1}{2^{l}} \leq \sum_{l=0}^{\infty} \frac{C}{2^{l}}=2 C,
$$

这与素数的倒数和发散矛盾!

(3). 复旦附中黄潮卿同学指出, 文章 《Power Values of Divisor Sums》 ${ }^{1}$ 中证明了对任意正整数 $k$, 存在无穷多个正整数 $n$, 使得 $\sigma(n)$ 是 $k$ 次幕. 更强地, Tristan Freiberg 于 2010 年 ${ }^{2}$ 证明了对任意正整数 $k$, 存在正实数 $x_{k}$, 使得对任意实数 $x \geq x_{k}$, 小于 $x$ 且使得 $\sigma(n)$ 是 $k$ 次幂的正整数 $n$ 的个数大于 $x^{0.7}$.

(4). 华南师范大学附属中学彭子晋, 福州延安中学李奕铭, 西工大附中杨泽宇, 深圳中学邓博文等同学也给出了本题的正确解答.

第二题 在 $\triangle A B C$ 中, $I$ 是内心, 内切圆与 $B C, C A, A B$ 分别切于点 $D, E, F$. $\odot(A B E), \odot(A C F)$ 的根轴与 $B C$ 交于点 $W$ 、与 $\odot(A B C)$ 交于另一点 $V$. 设 $Q$ 是 $I$ 关于 $W$ 的对称点, $M$ 是弧 $\overparen{B A C}$ 的中点, 直线 $M A, B C$ 交于点 $J$, 直线 $A D, V J$交于点 $S$. 证明: $\odot(M I S)$ 与 $\odot(I Q J)$ 相切.

(成都树德中学学生 李雨航 供题)

## 证明（根据雠州二中石芷润同学的整理):

先证明 $M, D, V$ 共线.

设 $\odot(A B E), \odot(A C F)$ 的第二个交点为 $U$, 则 $\triangle U F B \sim \triangle U C E$. 于是

$$
\frac{B V}{C V}=\frac{\sin \angle B A V}{\sin \angle C A V}=\frac{U F}{U C}=\frac{B F}{C E}=\frac{B D}{C D}
$$

从而 $D V$ 平分 $\angle B V C$, 故 $D V$ 经过弧 $\widehat{B A C}$ 的中点 $M$.

[^0]再证明 $M, I, W$ 共线.

易知 $\angle M B I=\frac{C}{2}, \angle M C I=\frac{B}{2}$, 所以

$$
\frac{S_{\triangle M B I}}{S_{\triangle M C I}}=\frac{M B \cdot B I \cdot \sin \angle M B I}{M C \cdot C I \cdot \sin \angle M C I}=\left(\frac{\sin \frac{C}{2}}{\sin \frac{B}{2}}\right)^{2} .
$$

另一方面，

$$
\frac{B W}{C W}=\frac{S_{\triangle A B V}}{S_{\triangle A C V}}=\frac{A B \cdot B V}{A C \cdot C V}=\frac{A B}{A C} \cdot \frac{B D}{C D}=\frac{\sin C}{\sin B} \cdot \frac{\cot \frac{B}{2}}{\cot \frac{C}{2}}=\left(\frac{\sin \frac{C}{2}}{\sin \frac{B}{2}}\right)^{2} .
$$

由 $\frac{S_{\triangle M B I}}{S_{\triangle M C I}}=\frac{B W}{C W}$ 即知 $M, I, W$ 共线.



下面证明 $\odot(M I S)$ 与 $\odot(I Q J)$ 相切, 只需证明 $\angle S I Q=\angle S M I+\angle Q J I$, 即 $\angle M S I=\angle Q J I$.

由

$$
M D \cdot M V=M C^{2}=M A \cdot M J
$$

知 $D, V, J, A$ 共圆. 又由 $\angle I D J=\angle I A J=90^{\circ}$ 知 $I, D, J, A$ 共圆, 所以 $I, D, V, J, A$五点共圆, 记为 $\Gamma$, 其圆心为 $I J$ 的中点 $L$.

对 $\Gamma$ 的内接四边形 $A D V J, S, M, W$ 分别为其两组对边的交点和对角线的交点, 所以由 Brocard 定理, $L W \perp S M$. 因为 $L, W$ 分别为 $I J, I Q$ 的中点, 所以 $J Q \perp S M$.

熟知 $M W$ 是 $S$ 关于 $\Gamma$ 的极线, 所以 $M W$ 与 $\Gamma$ 的交点 $I$ 与 $S$ 的连线是 $\Gamma$ 的切线, 于是 $I J \perp I S$.

这样, $\angle M S I$ 与 $\angle Q J I$ 的两边分别对应垂直, 故 $\angle M S I=\angle Q J I$.

综上, 命题得证.

评注 (1). 宁波市第十五中学庄子曰同学指出, $\triangle A B C$ 的切聚点 (连接
三角形的三个旁心和内切圆在三个旁心对应边切点的三条直线的交点)在 $\odot(A B E), \odot(A C F)$ 的根轴上.

(2). 深圳高级中学丁立轩, 深圳中学刘晨奕、邓博文, 北京一零一中学牟思特, 江西省九江一中黄若宸, 华南师范大学附属中学彭子晋, 福州延安中学李奕铭,湖南师大附中袁纬轩, 貛州二中周胤帆, 上海市华育中学龚逸晨, 武汉市七一中学杨子奥, 西安高新一中田浩辰, 西工大附中杨泽宇, 重庆西南大学附属中学李铭皓等同学也给出了本题的正确解答.

第三题 设整数 $n \geq 2$, 实数 $a_{1}, a_{2}, \cdots, a_{n} \geq 1$, 满足对任意 $1 \leq i \leq n, \mid a_{i}-$ $a_{i+1} \mid \geq 1$, 其中 $a_{n+1}=a_{1}$. 证明:

$$
\sum_{i=1}^{n} \frac{a_{i}-1}{a_{i+1}} \geq\left\lceil\frac{n}{2}\right\rceil
$$

(中国人民大学附属中学 张端阳 供题)

## 证明 1 (根据北京大学廖昱博同学的解答整理):

对 $1 \leq i \leq n$, 记

$$
b_{i}=\frac{a_{i}-1}{a_{i+1}}-\frac{1}{2}\left(1+\log _{2} \frac{a_{i}}{a_{i+1}}\right),
$$

则

$$
\sum_{i=1}^{n} \frac{a_{i}-1}{a_{i+1}}=\sum_{i=1}^{n} b_{i}+\frac{n}{2}
$$

先证明三个结论:

(1) $b_{i} \geq 0$.

固定 $\frac{a_{i}}{a_{i+1}}$, 在保证 $\left|a_{i}-a_{i+1}\right| \geq 1$ 的前提下同时减小 $a_{i}, a_{i+1}$. 此时不等式左边变小而右边不变, 因此可设 $a_{i}=1$ 或 $a_{i+1}=1$ 或 $\left|a_{i}-a_{i+1}\right|=1$. 这都是一元不等式, 容易验证.

(2) 若 $a_{i+1}>a_{i} \geq 2$, 则

$$
b_{i} \geq \frac{1}{3}-\frac{1}{2}\left(1+\log _{2} \frac{2}{3}\right)>0.125
$$

同 (1) 中调整可设 $a_{i+1}=a_{i}+1$ 或 $a_{i}=2$, 之后容易验证.

(3) 若 $a_{i+1}<a_{i}$ 且 $a_{i} \geq t$, 则

$$
b_{i} \geq 1-\frac{1}{2}\left(1+\log _{2} \frac{t}{t-1}\right) .
$$

记

$$
f(x)=\frac{a_{i}-1}{x}-\frac{1}{2}\left(1+\log _{2} \frac{a_{i}}{x}\right), \quad 1 \leq x \leq a_{i}-1 .
$$

因为

$$
f^{\prime}(x)=-\frac{a_{i}-1}{x^{2}}+\frac{1}{2 \ln 2 \cdot x} \leq-\frac{1}{x}+\frac{1}{2 \ln 2 \cdot x}<0,
$$

所以可设 $a_{i+1}=a_{i}-1$, 之后容易验证.

特别地, 当 $t=3$ 时, $b_{i} \geq 1-\frac{1}{2}\left(1+\log _{2} \frac{3}{2}\right)>0.207$; 当 $t=4$ 时, $b_{i} \geq 1-$ $\frac{1}{2}\left(1+\log _{2} \frac{4}{3}\right)>0.292$.

回到原题. 当 $n$ 为偶数时, 由 (1) 即证. 下设 $n$ 是奇数.

当 $n=3$ 时, 不妨设 $a_{2}$ 位于 $a_{1}$ 和 $a_{3}$ 之间.

若 $a_{1}<a_{2}<a_{3}$, 则由对勾函数的单调性知可设 $a_{1}=a_{2}-1, a_{3}=a_{2}+1$, 此时

$$
\begin{aligned}
\frac{a_{1}-1}{a_{2}}+\frac{a_{2}-1}{a_{3}}+\frac{a_{3}-1}{a_{1}} & =\frac{a_{2}-2}{a_{2}}+\frac{a_{2}-1}{a_{2}+1}+\frac{a_{2}}{a_{2}-1} \\
& =2+\frac{a_{2}\left(a_{2}-1\right)\left(a_{2}-2\right)+2}{\left(a_{2}-1\right) a_{2}\left(a_{2}+1\right)} \geq 2 .
\end{aligned}
$$

若 $a_{1}>a_{2}>a_{3}$, 则 $\frac{a_{1}-1}{a_{2}} \geq 1, \frac{a_{2}-1}{a_{3}} \geq 1$, 相加即证.

当 $n \geq 5$ 时, 假设结论不成立, 则

$$
\sum_{i=1}^{n} \frac{a_{i}-1}{a_{i+1}}<\frac{n+1}{2}, \sum_{i=1}^{n} b_{i}<\frac{1}{2}
$$

将 $a_{1}, a_{2}, \cdots, a_{n}$ 分为递增段和递减段, 若 $a_{i}<a_{i+1}<\cdots<a_{i+m}$, 则称 $m$ 为该递增段的长度. 因为递减段中的 $\frac{a_{i}-1}{a_{i+1}} \geq 1$, 所以由反证假设,

$$
\text { 递减段的总长度 } \leq \frac{n-1}{2}<\text { 递增段的总长度. }
$$

于是存在一个递增段的长度大于其后面递减段的长度, 不妨设为

$$
a_{1}<a_{2}<\cdots<a_{s+1}>a_{s+2}>\cdots>a_{s+r+1},
$$

其中 $s>r$.

若 $s \geq 3$, 则由 (2), $b_{s-1}, b_{s}>0.125$; 由 (3) (取 $t=4$ ), $b_{s+1}>0.292$. 于是

$$
\sum_{i=1}^{n} b_{i} \geq b_{s-1}+b_{s}+b_{s+1}>\frac{1}{2}
$$

矛盾! 所以 $s=2, r=1$, 因此 $a_{1}<a_{2}<a_{3}>a_{4}<a_{5}$.

从上述证明也可以看出, 不存在 $i$ 使 $a_{i}<a_{i+1}<a_{i+2}<a_{i+3}$.

必有 $a_{5}>a_{6}$. 否则由 (2), $b_{2}, b_{5}>0.125$; 由 (3) (取 $t=3$ ), $b_{3}>0.207$. 由 (*)知 $a_{6}>a_{7}$ (当 $n=5$ 时已与 $a_{1}<a_{2}$ 矛盾), 再由 (3)(取 $t=4$ )知 $b_{6}>0.207$. 于是

$$
\sum_{i=1}^{n} b_{i} \geq b_{2}+b_{3}+b_{5}+b_{6}>\frac{1}{2}
$$

矛盾!

下面只需证明 $b_{3}+b_{4}+b_{5}>0.375$, 再结合 $b_{2}>0.125$ 即得矛盾.
即证当 $x \geq 3, y \geq 1, z \geq 1$ 且 $x \geq y+1 \leq z \geq w+1$ 时,

$$
\frac{x-1}{y}+\frac{y-1}{z}+\frac{z-1}{w}-\frac{1}{2}\left(3+\log _{2} \frac{x}{w}\right)>0.375 .
$$

由对勾函数的单调性, 可设 $y=\min \{x, z\}-1$.

(1) 当 $y=x-1$ 时, 结合 (2)、(3),

由 $y<x \geq 3$ 知 $\frac{x-1}{y}-\frac{1}{2}\left(1+\log _{2} \frac{x}{y}\right)>0.207$;

由 $w<z \geq 3$ 知 $\frac{z-1}{w}-\frac{1}{2}\left(1+\log _{2} \frac{z}{w}\right)>0.207$;

由 $z>y \geq 2$ 知 $\frac{y-1}{z}-\frac{1}{2}\left(1+\log _{2} \frac{y}{z}\right)>0.125$.

相加即证.

(2) 当 $y=z-1$ 时, $x \geq z \geq 2, x \geq 3,1 \leq w \leq z-1$, 且只需证明

$$
\frac{x-1}{z-1}+\frac{z-2}{z}+\frac{z-1}{w}-\frac{1}{2}\left(3+\log _{2} \frac{x}{w}\right)>0.375 .
$$

对 $w$ 求导, 因为 $-\frac{z-1}{w^{2}}+\frac{1}{2 \ln 2 \cdot w}<0$, 所以可设 $w=z-1$. 此时只需证明

$$
\frac{x-1}{z-1}+\frac{z-2}{z}+1-\frac{1}{2}\left(3+\log _{2} \frac{x}{z-1}\right)>0.375 .
$$

对 $x$ 求导, 因为 $\frac{1}{z-1}-\frac{1}{2 \ln 2 \cdot x}>0$, 所以可设 $x=z$ 或 $x=3$. 这都是一元不等式, 容易验证.

综上, 命题得证.

## 证明 2 (根据华南师范大学附属中学彭子晋同学的解答整理):

记

$$
f_{n}\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\sum_{i=1}^{n} \frac{a_{i}-1}{a_{i+1}} .
$$

当 $n=2$ 时, 不妨设 $a_{1} \geq a_{2}$, 则 $f_{2}\left(a_{1}, a_{2}\right) \geq \frac{a_{1}-1}{a_{2}} \geq 1$.

当 $n=3$ 时, 不妨设 $a_{1} \geq a_{2} \geq a_{3}$ 或 $a_{1} \leq a_{2} \leq a_{3}$.

若为前者,

$$
f_{3}\left(a_{1}, a_{2}, a_{3}\right) \geq \frac{a_{1}-1}{a_{2}}+\frac{a_{2}-1}{a_{3}} \geq 2 .
$$

若为后者,

$$
f_{3}\left(a_{1}, a_{2}, a_{3}\right) \geq f_{3}\left(a_{1}, a_{2}, a_{2}+1\right) \geq f_{3}\left(a_{1}, a_{1}+1, a_{1}+2\right)>2
$$

下面对 $n$ 归纳. 假设 $n \geq 4$ 且不等式对 $2,3, \cdots, n-1$ 都成立, 来看 $n$ 时的情形.

注意到本题中变量是轮换的, 因此对 $a_{1}, a_{2}, \cdots$ 的讨论相当于对 $a_{i+1}, a_{i+2}, \cdots$的讨论.

我们定义若干个调整: (以下 $[i]$ 为标号, 不代表分类讨论）

[1] 若 $a_{1}<a_{2}>a_{3}$, 则

$$
\begin{aligned}
f_{n}\left(a_{1}, a_{2}, a_{3}, \cdots\right)= & \left(\frac{a_{1}-1}{a_{2}}+\frac{a_{2}}{a_{3}}\right)-\frac{1}{a_{3}}+\sum_{i=3}^{n} \frac{a_{i}-1}{a_{i+1}} \\
& \geq f_{n}\left(a_{1}, \max \left\{a_{1}, a_{3}\right\}+1, a_{3}, \cdots\right)
\end{aligned}
$$

[2] 若 $a_{1}>a_{2}<a_{3}$, 则

$$
\begin{aligned}
f_{n}\left(a_{1}, a_{2}, a_{3}, \cdots\right) & =\left(\frac{a_{1}-1}{a_{2}}+\frac{a_{2}}{a_{3}}\right)-\frac{1}{a_{3}}+\sum_{i=3}^{n} \frac{a_{i}-1}{a_{i+1}} \\
& \geq f_{n}\left(a_{1}, \min \left\{a_{1}, a_{3}\right\}-1, a_{3}, \cdots\right) .
\end{aligned}
$$

上面两个都是将 $f_{n}$ 看作 $a_{2}$ 的对勾函数而得到.

[3] 若 $a_{1}=a_{3}$, 则由 $n-2$ 时的归纳假设,

$$
\begin{aligned}
f_{n}\left(a_{1}, a_{2}, a_{3}, a_{4}, \cdots\right) & =f_{n-2}\left(a_{1}, a_{4}, \cdots\right)+\left(\frac{a_{1}-1}{a_{2}}+\frac{a_{2}-1}{a_{1}}\right) \\
& \geq\left\lceil\frac{n-2}{2}\right\rceil+1=\left\lceil\frac{n}{2}\right\rceil .
\end{aligned}
$$

此时命题得证, 下设不存在 $i$ 使 $a_{i}=a_{i+2}$.

[4] 若 $a_{1}<a_{2}<a_{3}>a_{4}$, 则由 [1] 知 $a_{3}=\max \left\{a_{2}, a_{4}\right\}+1$.

若 $a_{3}=a_{4}+1$, 则

$$
\begin{aligned}
f_{n}\left(a_{1}, a_{2}, a_{3}, a_{4}, \cdots\right) & \geq \frac{a_{1}-1}{a_{2}}+\frac{a_{3}-1}{a_{4}}+\sum_{i=4}^{n} \frac{a_{i}-1}{a_{i+1}} \\
& \geq \frac{a_{1}-1}{a_{4}}+1+\sum_{i=4}^{n} \frac{a_{i}-1}{a_{i+1}} \\
& \geq f_{n-2}\left(a_{1}, a_{4}, \cdots\right)+1 \geq\left\lceil\frac{n}{2}\right\rceil .
\end{aligned}
$$

若 $a_{3}=a_{2}+1$, 将

$$
f_{n}\left(a_{1}, a_{2}, a_{3}, a_{4}, \cdots\right)=f_{n}\left(a_{1}, a_{2}, a_{2}+1, a_{4}, \cdots\right)
$$

看作 $a_{2}$ 的对勾函数知不妨 $a_{2}=\max \left\{a_{1}+1, a_{4}\right\}$. 由 [3], 不妨 $a_{2}=a_{1}+1$.

综上, 若命题仍未得证, 则 $a_{3}=a_{2}+1=a_{1}+2$.

[5] 若 $a_{1}>a_{2}<a_{3}<a_{4}$, 则要么命题得证, 要么 $a_{4}=a_{3}+1=a_{2}+2$, 证明同 $[4]$.

[6] 若 $a_{1}<a_{2}, a_{2}=a_{3}+1, a_{3}<a_{4}$, 则

$$
\begin{aligned}
f_{n}\left(a_{1}, a_{2}, a_{3}, a_{4}, \cdots\right) & \geq \frac{a_{1}-1}{a_{2}}+\frac{a_{2}-1}{a_{3}}+\sum_{i=4}^{n} \frac{a_{i}-1}{a_{i+1}} \\
& \geq \frac{a_{1}-1}{a_{4}}+1+\sum_{i=4}^{n} \frac{a_{i}-1}{a_{i+1}} \\
& \geq f_{n-2}\left(a_{1}, a_{4}, \cdots\right)+1 \geq\left\lceil\frac{n}{2}\right\rceil,
\end{aligned}
$$

命题得证.

[7] 若 $a_{1}>a_{2}<a_{3}>a_{4}$, 由 [1],[2] 知 $a_{3}=a_{2}+1$ 或 $a_{3}=a_{4}+1, a_{1}=a_{2}+1$.

在后者中, 若命题仍未得证, 则由 [6], $a_{0}>a_{1}, a_{4}>a_{5}$. 将 $f_{n}$ 看作 $a_{3}$ 的对勾函数知 $a_{3}=a_{2}+1$ (此时 $a_{2}=a_{4}$, 由 [3] 知不成立) 或 $a_{4}=a_{5}+1$. 同理 $a_{0}=a_{1}+1$.

综上, 要么命题得证, 要么 $a_{3}=a_{2}+1$ 或 $a_{3}=a_{4}+1=a_{5}+2, a_{2}=a_{1}-1=$ $a_{0}-2$.

[8] 若存在一段 $t$ 项极大递增子列 $a_{1}<a_{2}<\cdots<a_{t}\left(a_{0}>a_{t}, a_{t}>a_{t+1}\right)$ 且 $t \geq 3$.

当 $t \geq 5$ 时, 由 [4],[5] 知要么命题得证, 要么 $a_{3}=a_{2}+1=a_{1}+2, a_{t}=$ $a_{t-1}+1=a_{t-2}+2$. 此时由递增关系得 $a_{2} \geq 2, a_{t-1} \geq 4$, 所以

$$
\begin{aligned}
& f_{n}\left(a_{1}, a_{2}, \cdots, a_{t}, \cdots\right) \\
= & f_{n-2}\left(a_{1}, a_{3}, a_{4}, \cdots, a_{t-2}, a_{t}, \cdots\right)+\frac{a_{2}^{2}-2}{a_{2}^{2}+a_{2}}+\frac{a_{t-1}^{2}-2}{a_{t-1}^{2}+a_{t-1}} \\
\geq & \left\lceil\frac{n-2}{2}\right\rceil+\frac{2^{2}-2}{2^{2}+2}+\frac{4^{2}-2}{4^{2}+4}>\left\lceil\frac{n}{2}\right\rceil,
\end{aligned}
$$

命题仍然得证.

当 $t=4$ 时, 由 [4],[5] 知 $a_{4}=a_{3}+1=a_{2}+2=a_{1}+3$.

当 $t=3$ 时, 由 [4],[5] 知 $a_{3}=a_{2}+1=a_{1}+2$.

[9] 若 $a_{2}=a_{1}+1, a_{3} \geq 2, a_{3}>\frac{a_{2}}{2}, a_{3}<a_{2}$, 则

$$
f_{n}\left(a_{1}, a_{2}, a_{3}, \cdots\right)>f_{n}\left(a_{1}, a_{3}-1, a_{3}, \cdots\right) .
$$

只需注意到

$$
\text { LHS }- \text { RHS }=\frac{a_{1}+2-a_{3}}{a_{3}\left(a_{1}+1\right)\left(a_{3}-1\right)}\left(2 a_{3}-a_{2}\right)>0 .
$$

回到原题. 若存在一组满足题意的 $a_{1}, a_{2}, \cdots, a_{n}$ 使得 $\sum_{i=1}^{n} \frac{a_{i}-1}{a_{i+1}}<\left\lceil\frac{n}{2}\right\rceil$, 则我们根据上述 [1] [9] 对其进行调整, 有限步调整后的 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 满足:

1) 任意极大递增子列长度至多为 4 , 即不存在 $a_{i}<a_{i+1}<a_{i+2}<a_{i+3}<a_{i+4}$.
2) 若 $a_{i}<a_{i+1}<a_{i+2}$, 则 $a_{i+2}=a_{i+1}+1=a_{i}+2$. (由 [8])
3) 若 $a_{k}>a_{k+1}, a_{k}=a_{k-1}+1$, 则 $a_{k+1} \leq \max \left\{2, \frac{a_{k}}{2}\right\}$. (由 [9])
4) 若 $a_{k}>a_{k+1}<a_{k+2}>a_{k+3}, a_{k+2} \neq a_{k+1}+1$, 则 $a_{k+2}=a_{k+3}+1=a_{k+4}+2$, $a_{k+1}=a_{k}+1=a_{k-1}+2$. (由 $[7]$ )

下证我们可以将 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 排列在圆周上, 分划为若干段, 每段 $\left(a_{i}, \cdots, a_{j}\right)$ (记作 $K(i, j)$ ) 属于以下七类之一:

(1) $j=i, a_{i}>a_{i+1}$;

(2) $j=i+1, a_{i}>a_{i+1}<a_{i+2}$;

(3) $j=i+2, a_{i+1}=a_{i}+1=a_{i-1}+2, a_{i+1}>a_{i+2}>a_{i+3}$;

(4) $j=i+2, a_{i+1}=a_{i}+1=a_{i-1}+2, a_{i+1}>a_{i+2}, a_{i+3}=a_{i+2}+1$;

(5) $j=i+2, a_{i+2}=a_{i+1}+1=a_{i}+2=a_{i-1}+3, a_{i+2}>a_{i+3}$;

(6) $j=i+1, a_{i}<a_{i+1}>a_{i+2}$;

(7) $j=i+3, a_{i+2}=a_{i+1}+1=a_{i}+2=a_{i-1}+3, a_{i+2}>a_{i+3}<a_{i+4}$.

首先, 对于 $\left\{a_{i}\right\}$ 中的每一个极大递增子列, 若其为 $a_{k}<a_{k+1}<a_{k+2}<a_{k+3}$,则取出一组 (5) 类的 $K(k+1, k+3)$

若其长度为 3 , 为 $a_{k}<a_{k+1}<a_{k+2}$, 则总可取出一组 (3) 类或 (4) 类的 $K(k+1, k+3)$.

已知以上的若干段 $K(i, j)$ 全部不交. 对每个 $a_{k}$, 若 $a_{k}<a_{k+1}$ 且 $a_{k}$ 不在任何一段分划中, 则由上知 $a_{k-1}>a_{k}$. 分类讨论:

若 $a_{k-1}$ 也不在任意分划中, 取出 (2) 类 $K(k-1, k)$ 包含 $a_{k}$ 和 $a_{k-1}$.

若 $a_{k-1}$ 在某个分划 $K(i, j)$ 中则必有 $j=k-1$, 故其必属于 (1)、(3)、(5)、(6)四类分划之一.

若 $a_{k-1}$ 在 (1) 类分划 $K(k-1, k-1)$ 中, 将其和 $a_{k}$ 合成为 (2) 类分划 $K(k-1, k)$.

若 $a_{k-1}$ 在 (3) 类分划 $K(k-3, k-1)$ 中, 将其和 $a_{k}$ 重新分划为 (6) 类 $K(k-$ $3, k-2)$ 和 (2) 类 $K(k-1, k)$.

若 $a_{k-1}$ 在 (5) 类分划 $K(k-3, k-1)$ 中, 将其和 $a_{k}$ 合成为 (7) 类分划 $K(k-3, k)$.

若 $a_{k-1}$ 在 (6) 类分划 $K(k-2, k-1)$ 中, 将其重新分为 (2) 类分划 $K(k-1, k)$和不在任何分划中的 $a_{k-2}$, 有 $a_{k-2}<a_{k-1}$ 且 $a_{k-2}$ 不在任何分划中, 即我们把试图加入 $a_{k}$ 的问题转化为 $a_{k-2}$ 的问题. 同理能将 $a_{k-2}$ 加入某个分划中, 或转化为 $a_{k-4}$的问题, 依此类推. 考虑 $n$ 的奇偶性和 (2)、(6) 类分划的条件知, 此过程会结束.

经过以上过程, 我们将任意满足 $a_{k}<a_{k+1}$ 的 $a_{k}$ 加入了分划, 余下的 $a_{k}$ 全部加入单独的 (1) 类分划 $K(k, k)$ 即可. 故 $(*)$ 操作的存在性得证.

要证原不等式, 只需对每一段分划求和, 即证

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq\left\lceil\frac{n}{2}\right\rceil
$$

若 $K(i, j)$ 为 (1)、(2) 类分划, 则

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \frac{a_{i}-1}{a_{i+1}} \geq 1
$$

若 $K(i, j)$ 为 (3) 类分划, 则

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \frac{a_{i+1}-1}{a_{i+2}}+\frac{a_{i+2}-1}{a_{i+3}} \geq 2
$$

若 $K(i, j)$ 为 (4) 类分划, 则当 $a_{i+2} \geq 2$ 时,

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}}=\frac{a_{i}-1}{a_{i}+1}+\frac{a_{i}}{a_{i+2}}+\frac{a_{i+2}-1}{a_{i+2}+1} \geq 2 \cdot \frac{a_{i+2}-1}{a_{i+2}+1}+1 \geq \frac{5}{3},
$$

其中用到 $a_{i} \geq a_{i+2}$. 当 $a_{i+2}<2$ 时,

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}}=\frac{a_{i}-1}{a_{i}+1}+\frac{a_{i}}{a_{i+2}}+\frac{a_{i+2}-1}{a_{i+2}+1} \geq \frac{2-1}{2+1}+\frac{2}{a_{i+2}}+\frac{a_{i+2}-1}{a_{i+2}+1} \geq \frac{5}{3},
$$

其中用到 $a_{i}=a_{i-1}+1 \geq 2$.

若 $K(i, j)$ 为 (5) 类分划, 则

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}}=\frac{a_{i}-1}{a_{i}+1}+\frac{a_{i}}{a_{i}+2}+\frac{a_{i}+1}{a_{i+3}} \geq \frac{a_{i}-1}{a_{i}+1}+\frac{a_{i}}{a_{i}+2}+\frac{2\left(a_{i}+1\right)}{a_{i}+2} \geq 2
$$

其中用到 $a_{i} \geq 2$, 且由 3$)$ 得 $a_{i+3} \leq \frac{a_{i}+2}{2}$.

若 $K(i, j)$ 为 (6) 类分划, 则

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \frac{a_{i+1}-1}{a_{i+2}} \geq 1
$$

若 $K(i, j)$ 为 (7) 类分划, 则

$$
\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \sum_{i \leq k \leq i+2} \frac{a_{k}-1}{a_{k+1}} \geq 2
$$

这是因为 $\left(a_{i}, a_{i+1}, a_{i+2}\right)$ 可看作一个 (5) 类分划.

综上所述, (1) (7) 类分划的长度 (即 $j-i+1$ ) 分别为 $1,2,3,3,3,2,4$, 而贡献的 $\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}}$ 分别至少为 $1,2,2, \frac{5}{3}, 2,1,2$.

当 $n$ 为偶数时, 有

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \sum_{K(i, j)} \frac{j-i+1}{2}=\frac{n}{2}
$$

命题得证.

当 $n$ 为奇数时, 分类讨论:

若 $\left(a_{1}, \cdots, a_{n}\right)$ 的分划中存在 (1) 或 (3) 或 (5) 类分划, 因为它们对应的 $\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}}$至少为 $\frac{j-i+1}{2}+\frac{1}{2}$, 所以

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \sum_{K(i, j)} \frac{j-i+1}{2}+\frac{1}{2}=\frac{n+1}{2}
$$

命题得证.

若存在至少三个 (4) 类分划, 因它每个对应的 $\sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}}$ 至少为 $\frac{j-i+1}{2}+\frac{1}{6}$, 所以

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq \sum_{K(i, j)} \frac{j-i+1}{2}+3 \cdot \frac{1}{6}=\frac{n+1}{2},
$$

命题得证.

若不为以上情况, 由于 $n$ 为奇数, 必存在奇数个长度为奇数的分划. 因此只存
在一个 (4) 类分划, 其他为 (2) 或 (6) 或 (7) 类分划.

不妨记这个 (4) 类分划为 $K(1,3)$, 考虑 $a_{4}$ 所在的分划:

(1) $a_{4}$ 在 (2) 类分划 $K(4,5)$.

由 $[2]$ 知 $a_{5}=\min \left\{a_{4}, a_{6}\right\}-1$.

若 $a_{5}=a_{4}-1$, 则 $a_{3}=a_{5}$, 由 [3] 知不成立.

若 $a_{5}=a_{6}-1$, 则 $a_{1} \geq a_{3} \geq a_{5} \geq 1$, 所以

$$
\begin{aligned}
\sum_{1 \leq k \leq 5} \frac{a_{k}-1}{a_{k+1}} & =\frac{a_{1}-1}{a_{1}+1}+\frac{a_{1}}{a_{3}}+\frac{a_{3}-1}{a_{3}+1}+\frac{a_{3}}{a_{5}}+\frac{a_{5}-1}{a_{5}+1} \\
& \geq \frac{2-1}{2+1}+\frac{2}{a_{3}}+\frac{a_{3}-1}{a_{3}+1}+\frac{a_{3}}{a_{5}}+\frac{a_{5}-1}{a_{5}+1}
\end{aligned}
$$

把右式看作 $g\left(a_{5}\right)$, 在 $a_{5} \in\left[1, a_{3}\right]$ 时有 $g^{\prime}\left(a_{5}\right)<0$, 故 $g\left(a_{5}\right) \geq g\left(a_{3}\right) \geq 3$. 从而

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq 3+\quad \sum_{K(i, j)} \quad \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq 3+\frac{n-5}{2}=\frac{n+1}{2}
$$

命题得证.

(2) $a_{4}$ 在 (6) 类分划 $K(4,5)$.

由 [1] 和 2), 有 $a_{5}=a_{4}+1=a_{3}+2, a_{5}>a_{6}$. 所以

$$
\begin{aligned}
\sum_{1 \leq k \leq 5} \frac{a_{k}-1}{a_{k+1}} & =\frac{a_{1}-1}{a_{1}+1}+\frac{a_{1}}{a_{3}}+\frac{a_{3}-1}{a_{3}+1}+\frac{a_{3}}{a_{3}+2}+\frac{a_{3}+1}{a_{6}} \\
& \geq \frac{2-1}{2+1}+\frac{2}{a_{3}}+\frac{a_{3}-1}{a_{3}+1}+\frac{a_{3}}{a_{3}+2}+1 \geq 3,
\end{aligned}
$$

从而

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq 3+\sum_{\substack{K(i, j) \\(i, j) \neq(1,3),(4,5)}} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq 3+\frac{n-5}{2}=\frac{n+1}{2}
$$

命题得证.

(3) $a_{4}$ 在 (7) 类分划 $K(4,7)$.

有 $a_{6}=a_{5}+1=a_{4}+2=a_{3}+3 \geq 4$, 由结论 3$)$ 得 $a_{7} \leq \max \left\{2, \frac{a_{6}}{2}\right\}=\frac{a_{6}}{2}$. 所以

$$
\begin{aligned}
\sum_{1 \leq k \leq 7} \frac{a_{k}-1}{a_{k+1}} & \geq \sum_{1 \leq k \leq 6} \frac{a_{k}-1}{a_{k+1}}=\frac{a_{1}-1}{a_{1}+1}+\frac{a_{1}}{a_{3}}+\frac{a_{3}-1}{a_{3}+1}+\frac{a_{3}}{a_{3}+2}+\frac{a_{3}+1}{a_{3}+3}+\frac{a_{3}+2}{a_{7}} \\
& \geq \frac{2-1}{2+1}+\frac{2}{a_{3}}+\frac{a_{3}-1}{a_{3}+1}+\frac{a_{3}}{a_{3}+2}+\frac{a_{3}+1}{a_{3}+3}+\frac{2\left(a_{3}+2\right)}{a_{3}+3}>4
\end{aligned}
$$

从而

$$
\sum_{K(i, j)} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq 4+\sum_{\substack{K(i, j) \\(i, j) \neq(1,3),(4,7)}} \sum_{i \leq k \leq j} \frac{a_{k}-1}{a_{k+1}} \geq 4+\frac{n-7}{2}=\frac{n+1}{2}
$$

命题得证.

综上, 归纳证毕.

## 证明 3 (根据北京一零一中学牟思特同学的解答整理):

为方便叙述, 将所有 $a_{i}$ 减去 1 , 此时条件为 $a_{i} \geq 0,\left|a_{i}-a_{i+1}\right| \geq 1$, 要证明

$$
\sum_{i=1}^{n} \frac{a_{i}}{a_{i+1}+1} \geq\left\lceil\frac{n}{2}\right\rceil
$$

当 $n=2$ 时, 不妨设 $a_{1} \geq a_{2}$, 则 $a_{1} \geq a_{2}+1$, 此时

$$
\frac{a_{1}}{a_{2}+1}+\frac{a_{2}}{a_{1}+1} \geq \frac{a_{1}}{a_{2}+1} \geq 1
$$

当 $n=3$ 时, 若 $a_{1} \geq a_{2} \geq a_{3}$, 则 $a_{1} \geq a_{2}+1, a_{2} \geq a_{3}+1$, 所以

$$
\sum_{i=1}^{3} \frac{a_{i}}{a_{i+1}+1} \geq \frac{a_{1}}{a_{2}+1}+\frac{a_{2}}{a_{3}+1} \geq 1+1=2 .
$$

若 $a_{1} \leq a_{2} \leq a_{3}$, 则 $a_{1}+1 \leq a_{2}, a_{2}+1 \leq a_{3}$.

由于 $y=\frac{a_{2}}{x+1}+\frac{x}{a_{1}+1}$ 在 $\left[\sqrt{\left(a_{1}+1\right) a_{2}}-1,+\infty\right)$ 上单调递增, 且 $\sqrt{\left(a_{1}+1\right) a_{2}}-1<$ $a_{2}+1$, 于是可不妨设 $a_{3}=a_{2}+1$. 由于 $y=\frac{x}{a_{2}+1}+\frac{a_{2}+1}{x+1}$ 在 $\left[0, a_{2}\right]$ 上单调递减, 于是可不妨设 $a_{1}=a_{2}-1$. 此时

$$
\begin{aligned}
\sum_{i=1}^{3} \frac{a_{i}}{a_{i+1}+1} & =\frac{a_{1}}{a_{1}+2}+\frac{a_{1}+1}{a_{1}+3}+\frac{a_{1}+2}{a_{1}+1} \\
& =2+\frac{a_{1}^{2}+3 a_{1}+4}{\left(a_{1}+1\right)\left(a_{1}+3\right)}-\frac{2}{a_{1}+2} \\
& \geq 2+\frac{1}{a_{1}+2}\left(\frac{a_{1}^{2}+3 a_{1}+4}{a_{1}+2}-2\right) \geq 2
\end{aligned}
$$

下面对 $n$ 归纳. 假设 $n \geq 4$ 且不等式对 $2,3, \cdots, n-1$ 都成立, 来看 $n$ 时的情形.

显然 $F=\sum_{i=1}^{n} \frac{a_{i}}{a_{i+1}+1}$ 存在最小值, 下设已在 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)$ 处取到最小值. 假设 $F<\left\lceil\frac{n}{2}\right\rceil$.

若 $a_{i-1}<a_{i}>a_{i+1}$, 则称 $a_{i}$ 为极大值点; 若 $a_{i-1}>a_{i}<a_{i+1}$, 则称 $a_{i}$ 为极小值点.

结论 1 若 $a_{i}$ 是极大值点, 则 $a_{i}=\max \left\{a_{i-1}, a_{i+1}\right\}+1$.

这由 $f(x)=\frac{a_{i-1}}{x+1}+\frac{x}{a_{i+1}+1}$ 在 $\left[\sqrt{a_{i-1}\left(a_{i+1}+1\right)}-1,+\infty\right)$ 上单调递增且

$$
\sqrt{a_{i-1}\left(a_{i+1}+1\right)}-1<\max \left\{a_{i-1}, a_{i+1}\right\}+1
$$

即证.

结论 2 若 $a_{i-1}<a_{i}<a_{i+1}$ 且 $a_{i+1}-a_{i}=1$, 则 $a_{i-1}=a_{i}-1$.

这由结论 1 中的 $f(x)$ 且

$$
\sqrt{a_{i-1}\left(a_{i+1}+1\right)}-1 \leq \sqrt{\left(a_{i}-1\right)\left(a_{i}+2\right)}-1<a_{i}
$$

即证.
结论 3 若 $a_{i-1}>a_{i}>a_{i+1}$ 且 $a_{i-1}-a_{i}=1$, 则 $a_{i+1}=a_{i}-1$.

这由结论 1 中的 $f(x)$ 且

$$
\sqrt{a_{i-1}\left(a_{i+1}+1\right)}-1 \leq \sqrt{a_{i}\left(a_{i}+1\right)}-1<a_{i}
$$

即证.

由结论 $1,2,3$ 得, 在每个极大值点左右两侧的序列中, 至少有一个构成公差为 $\pm 1$ 的等差数列.

结论 4 若 $a_{i}$ 是极小值点, 则 $a_{i}=\min \left\{a_{i-1}, a_{i+1}\right\}-1$.

这由 $f(x)=\frac{a_{i-1}}{x+1}+\frac{x}{a_{i+1}+1}$ 在 $\left[0, \sqrt{a_{i-1}\left(a_{i+1}+1\right)}-1\right]$ 上单调递减且

$$
\sqrt{a_{i-1}\left(a_{i+1}+1\right)}-1>\min \left\{a_{i-1}, a_{i+1}\right\}-1
$$

即证.

情形 1 存在 $i$ 使 $a_{i}<a_{i+1}<a_{i+2}$ 且 $a_{i+3}=a_{i+2}-1$.

此时 $\left|a_{i}-a_{i+3}\right| \geq 1$, 且

$$
\begin{aligned}
& \frac{a_{i}}{a_{i+1}+1}+\frac{a_{i+1}}{a_{i+2}+1}+\frac{a_{i+2}-a_{i}}{a_{i+3}+1} \\
\geq & \frac{a_{i+1}-1}{a_{i+1}+1}+\frac{a_{i+1}}{a_{i+2}+1}+\frac{a_{i+2}-\left(a_{i+1}-1\right)}{a_{i+2}} \\
\geq & \frac{a_{i+1}}{a_{i+2}+1}+1 \geq 1,
\end{aligned}
$$

其中第一步和第二步分别用到了

$$
\frac{1}{a_{i+1}+1} \geq \frac{1}{a_{i+3}+1} \text { 和 }\left(\frac{1}{a_{i+1}+1}-\frac{1}{a_{i+2}}\right)\left(a_{i+1}-1\right) \geq 0 .
$$

因此删去 $a_{i+1}, a_{i+2}$ 后由 $n-2$ 时的归纳假设知命题成立, 故可设不存在这样的 $i$.

若存在 $i$ 使 $a_{i+1}>a_{i}+1$ 且 $a_{i+2}<a_{i+1}$, 则 $a_{i+2}=a_{i+1}-1$. 否则由结论 2 知必有 $a_{i+2}>a_{i+1}+1>\cdots$. 设 $a_{i+k}$ 为极大值, 则 $a_{i+k}>a_{i+k-1}+1$, 结合结论 1 知 $a_{i+k+1}=a_{i+k}-1$, 得到情形 1 , 矛盾!

假若此时还存在 $j$ 使 $a_{j-1}<a_{j}<a_{j+1}$, 取 $j$ 使 $j-i$ 最小, 则 $a_{j}=a_{j-1}+$ $1, a_{j+1}=a_{j}+1$. 若 $a_{j-2}<a_{j-1}$, 则与 $j$ 的最小性矛盾; 若 $a_{j-2}=a_{j-1}+1$, 则

$$
\frac{a_{j-2}}{a_{j-1}+1}+\frac{a_{j-1}}{a_{j}+1}+\frac{a_{j}}{a_{j+1}+1} \geq 1+\frac{a_{j}}{a_{j+1}+1}=1+\frac{a_{j-2}}{a_{j+1}+1},
$$

因此删去 $a_{j-1}, a_{j}$ 后由 $n-2$ 时的归纳假设知命题成立. 故可设 $a_{j-2}>a_{j-1}+1$.设 $a_{j-2}$ 前的第一个极大值点为 $a_{t}$, 则 $a_{t}>a_{t+1}+1$, 由结论 1 知 $a_{t-1}=a_{t}-1$. 若 $a_{t-2}<a_{t-1}$, 则与 $j$ 的最小性矛盾; 若 $a_{t-2}=a_{t-1}+1$, 则

$$
\frac{a_{t-2}}{a_{t-1}+1}+\frac{a_{t-1}}{a_{t}+1}+\frac{a_{t}}{a_{t+1}+1} \geq 1+\frac{a_{t}}{a_{t+1}+1}=1+\frac{a_{t-2}}{a_{t+1}+1},
$$

因此删去 $a_{t-1}, a_{t}$ 后由 $n-2$ 时的归纳假设知命题成立. 故可设 $a_{t-2}>a_{t-1}+1$. 重
复上面的讨论, 知 $a_{j-1}$ 前的每一段数都先恰好增加 1 , 再减去若干个大于 1 的数,这与存在 $i$ 使 $a_{i+1}>a_{i}+1$ 矛盾!

情形 2 存在 $i$ 使 $a_{i+1}>a_{i}+1$.

由于不存在连续两个 $j$ 使 $a_{j}<a_{j+1}$, 所以至少有 $\left\lceil\frac{n}{2}\right\rceil$ 个 $j$ 使 $a_{j}>a_{j+1}$. 对这些 $j$ 有 $\frac{a_{j}}{a_{j+1}+1} \geq 1$, 将它们求和便有 $F \geq\left\lceil\frac{n}{2}\right\rceil$.

情形 3 若 $a_{i+1}>a_{i}$, 则 $a_{i+1}=a_{i}+1$.

对每个极小值点 $a_{t}$ 以及使得 $t^{\prime}-t$ 最小的极小值点 $a_{t^{\prime}}$, 称 $a_{t}, a_{t+1}, \cdots, a_{t^{\prime}-1}$ 构成一个“段”, 且该段的“值” 是 $\sum_{i=t}^{t^{\prime}-1} \frac{a_{i}}{a_{i+1}+1}$. 每个段中的项都是先加若干次 1 , 再减若干次. 设一个段的 “度” 是这个段中满足 $a_{i+1}>a_{i}$ 的 $i$ 的个数.

结论 5 不存在一个段的度大于等于 4 .

否则设 $a_{i+4}>a_{i+3}>a_{i+2}>a_{i+1}>a_{i}$, 记 $a_{i+1}=t \geq 1$, 计算知

$$
\frac{t}{t+2}+\frac{t+1}{t+3}+\frac{t+2}{t+4} \geq 1+\frac{t}{t+4}
$$

因此删去 $a_{i+2}, a_{i+3}$ 后由 $n-2$ 时的归纳假设知命题成立.

结论 $6.1 \frac{a_{i}}{a_{i+1}+1} \geq \frac{1}{2}+3\left(\frac{1}{a_{i+1}+2}-\frac{1}{a_{i}+2}\right)$.

若 $a_{i+1}>a_{i}$, 则 $a_{i+1}=a_{i}+1$, 此时只需证明

$$
\frac{a_{i}}{a_{i}+2} \geq \frac{1}{2}-\frac{3}{\left(a_{i}+2\right)\left(a_{i}+3\right)}
$$

容易验证成立.

若 $a_{i+1}<a_{i}$, 则 $a_{i+1} \leq a_{i}-1$. 因为 $y=\frac{x}{a_{i+1}+1}+\frac{3}{x+2}$ 在 $\left[\sqrt{3\left(a_{i+1}+1\right)}-2,+\infty\right)$上单调递增, 且 $\sqrt{3\left(a_{i+1}+1\right)}-2 \leq a_{i+1}+1$, 所以可不妨设 $a_{i}=a_{i+1}+1$. 此时即证 $\frac{1}{2} \geq \frac{3}{\left(a_{i+1}+2\right)\left(a_{i+1}+3\right)}$, 容易验证成立.

当 $n$ 是偶数时,

$$
\sum_{i=1}^{n} \frac{a_{i}}{a_{i+1}+1} \geq \sum_{i=1}^{n}\left(\frac{1}{2}+3\left(\frac{1}{a_{i+1}+2}-\frac{1}{a_{i}+2}\right)\right)=\frac{n}{2}
$$

命题成立.

当 $n$ 是奇数时, 类似证明可得:

结论 6.2.1 若 $a_{i}>a_{i+1}, a_{i+1} \geq 1$, 则

$$
\frac{a_{i}}{a_{i+1}+1} \geq \frac{1}{2}+3\left(\frac{1}{a_{i+1}+2}-\frac{1}{a_{i}+2}\right)+\frac{1}{4} .
$$

结论 6.2.2 若 $a_{i}>a_{i+1}, a_{i} \geq 3$, 则

$$
\frac{a_{i}}{a_{i+1}+1} \geq \frac{1}{2}+3\left(\frac{1}{a_{i+1}+2}-\frac{1}{a_{i}+2}\right)+\frac{7}{20}
$$

结论 6.2.3 若 $a_{i}<a_{i+1}, a_{i} \geq 2$, 则

$$
\frac{a_{i}}{a_{i+1}+1} \geq \frac{1}{2}+3\left(\frac{1}{a_{i+1}+2}-\frac{1}{a_{i}+2}\right)+\frac{3}{20}
$$

由以上结论, 可设没有度为 3 的段, 否则求和后会比 $\frac{n}{2}$ 多出至少 $\frac{3}{20}+\frac{7}{20}=\frac{1}{2}$.

其次, 度为 2 的段至多有 1 个, 否则求和后会比 $\frac{n}{2}$ 多出至少 $\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$.

结合 $n$ 为奇数, 可不妨设 $a_{1}<a_{2}<a_{3}>a_{4}<a_{5}>a_{6}<a_{7} \cdots$, 知 $a_{2} \geq a_{4} \geq$ $a_{6} \geq \cdots \geq a_{n+1}$, 其中 $a_{n+1}=a_{1}$.

结论 6.3 对 $i \geq 2$,

$$
\frac{a_{2 i}}{a_{2 i+1}+1}+\frac{a_{2 i+1}}{a_{2 i+2}+1}=\frac{a_{2 i}}{a_{2 i}+2}+\frac{a_{2 i}+1}{a_{2 i+2}+1} \geq 1+\frac{3}{4}\left(a_{2 i}-a_{2 i+2}\right) .
$$

上式等价于

$$
\frac{a_{2 i}}{a_{2 i+2}} \geq\left(\frac{3}{4}-\frac{1}{a_{2 i+2}+1}\right)\left(a_{2 i}-a_{2 i+2}\right) \text {. }
$$

不妨设 $\frac{3}{4}-\frac{1}{a_{2 i+2}+1}>0$, 由 $0 \leq a_{2 i+2} \leq a_{2 i} \leq 1$, 容易验证

$$
\frac{a_{2 i}}{a_{2 i}+2} \geq \frac{3}{4}-\frac{1}{a_{2 i}+1} \geq \frac{3}{4}-\frac{1}{a_{2 i+2}+1} \geq\left(\frac{3}{4}-\frac{1}{a_{2 i+2}+1}\right)\left(a_{2 i}-a_{2 i+2}\right) .
$$

于是

$$
F \geq \frac{a_{1}}{a_{1}+2}+\frac{a_{1}+1}{a_{1}+3}+\frac{a_{1}+2}{a_{4}+1}+\frac{3}{4}\left(a_{4}-a_{1}\right)+\frac{n-3}{2} .
$$

设 $a_{1}=x, a_{4}=y$, 则 $0 \leq x \leq y \leq 1$, 容易验证

$$
\frac{x}{x+2}+\frac{x+1}{x+3}+\frac{x+2}{y+1}+\frac{3}{4}(y-x) \geq 2,
$$

所以 $F \geq \frac{n+1}{2}$.

综上, 归纳证毕.

评注 (1). 本题命制时受下题启发较大:

设整数 $n \geq 2$, 实数 $a_{1}, a_{2}, \cdots, a_{n} \geq 1$, 且满足 $\left|a_{i}-a_{i+1}\right| \leq 1,1 \leq i \leq n-1$.证明:

$$
\sum_{i=1}^{n} \frac{a_{i}}{a_{i+1}} \leq 2 n-H_{n}
$$

其中 $a_{n+1}=a_{1}, H_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}$.

印象里这种含局部绝对值条件的不等式都是 $\left|a_{i}-a_{i+1}\right| \leq 1$, 于是想看一下不等号反过来会如何.

(2). 在提交的解答中, 多数采用了归纳法, 但用归纳假设时并没有注意验证相邻两项之差不小于 1 的条件, 因此大多是伪证. 目前的三种做法思路相近, 都是通过调整将问题转化到每个递增、递减段上, 再通过局部不等式加强常数得以解决.我们基本保留了三份解答的原始面貌, 细节处理及详略各有千秋, 可互为参考.

(3). 当 $n$ 是偶数时, 华南师范大学附属中学戴子一同学给出了如下的简洁证法.
设 $a_{i_{1}}, a_{i_{2}}, \cdots, a_{i_{k}}$ 是所有不小于 2 的项, 其中 $1 \leq i_{1}<i_{2}<\cdots<i_{k} \leq n$. 注意到不能连续两项都小于 2 , 所以对 $j=1,2, \cdots, k, i_{j+1}-i_{j}=1$ 或 2 , 这里 $i_{k+1}=i_{1}$.

当 $i_{j+1}-i_{j}=1$ 时,

$$
\frac{a_{i_{j}}-1}{a_{i_{j+1}}} \geq \frac{1}{2} \cdot \frac{a_{i_{j}}}{a_{i_{j+1}}} .
$$

当 $i_{j+1}-i_{j}=2$ 时, 设 $a_{i_{j}}$ 与 $a_{i_{j+1}}$ 之间的项为 $b_{j}$, 我们证明

$$
\frac{a_{i_{j}}-1}{b_{j}}+\frac{b_{j}-1}{a_{i_{j+1}}} \geq \frac{1}{2}\left(\frac{a_{i_{j}}}{a_{i_{j+1}}}+1\right) .
$$

事实上, 由 $b_{j}-1<1 \leq \frac{1}{2} a_{i_{j}}$, 知可设 $a_{i_{j+1}}=b_{j}+1$; 由 $\frac{1}{b_{j}}>\frac{1}{2} \geq \frac{1}{2 a_{i_{j+1}}}$, 知可设 $a_{i_{j}}=b_{j}+1$. 此时即证

$$
1+\frac{b_{j}-1}{b_{j}+1} \geq \frac{1}{2}(1+1)=1,
$$

这显然成立.

这样, 因为使 $i_{j+1}-i_{j}=2$ 的 $j$ 有 $n-k$ 个, 所以

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{a_{i}-1}{a_{i+1}} & =\sum_{j: a_{i_{j+1}}-a_{i_{j}}=1} \frac{a_{i_{j}}-1}{a_{i_{j+1}}}+\sum_{j: i_{j+1}-i_{j}=2}\left(\frac{a_{i_{j}}-1}{b_{j}}+\frac{b_{j}-1}{a_{i_{j+1}}}\right) \\
& \geq \sum_{j: a_{i_{j+1}}-a_{i_{j}}=1} \frac{1}{2} \cdot \frac{a_{i_{j}}}{a_{i_{j+1}}}+\sum_{j: i_{j+1}-i_{j}=2} \frac{1}{2}\left(\frac{a_{i_{j}}}{a_{i_{j+1}}}+1\right) \\
& =\frac{1}{2}\left(\sum_{j=1}^{k} \frac{a_{i_{j}}}{a_{i_{j+1}}}+(n-k)\right) \\
& \geq \frac{1}{2}(k+(n-k))=\frac{n}{2},
\end{aligned}
$$

其中最后一步用到了均值不等式.

第四题 设整数 $c>5$. 定义平面上的“无限折线”为只有相邻线段相交 (于端点) 的射线 $A_{1} X, A_{k} Y$ 和线段 $A_{1} A_{2}, A_{2} A_{3}, \cdots, A_{k-1} A_{k}$ 组成的点集. 平面上有 $n$ 条无限折线产生了 $m$ 个交点(其中任意三条无限折线不共点), 将平面分成了 $n+m+1$ 个区域. 已知对其中任意两个区域, 最多有 $c$ 条无限折线, 两者的边界上均有某一段被其中一条折线包含. 定义一个区域的大小为其边界上不同折线的数量. 证明: 存在常数 $C$, 使得对任意正整数 $m, n$, 这些区域的大小的平方和不超过 $C\left(n^{2}+m\right)$.

(上海中学学生 江城 供题)

## 证明 (根据供题者的解答整理):

记 $D=10^{6} c^{3}$.
设大小至少为 $s$ 的区域的个数为 $f_{s}$, 则所有区域的大小的平方和

$$
M=\sum_{s=1}^{n} s^{2}\left(f_{s}-f_{s+1}\right)=\sum_{s=1}^{n}(2 s-1) f_{s} \text {. }
$$

下面证明 $f_{s} \leq D\left(\frac{n}{s}+\frac{m}{s^{3}}\right)$, 这样

$$
M<2 \sum_{s=1}^{n} s f_{s} \leq 2 D \sum_{s=1}^{n}\left(n+\frac{m}{s^{2}}\right)<2 D\left(n^{2}+2 m\right)
$$

从而取 $C=4 D$ 即可.

当 $s \leq 50 c$ 时, $D>s^{3}$, 又 $f_{s} \leq n+m+1$, 所以结论显然成立. 下设 $s>50 c$.

首先叙述有重边的交叉数引理 (Crossing Lemma): 对于任何一个画在平面上的图, 若边的重数不超过 $t$, 则要么 $|E| \leq 20 t|V|$, 要么至少产生 $\frac{1}{1000} \cdot \frac{|E|^{3}}{t^{2}|V|^{2}}$ 个交点.

我们构造如下画在平面上的图:

(1) 点: 将每个大小至少为 $s$ 的区域作为图的一个顶点, 在区域中任选一点代表这个顶点, 则图的顶点数为 $f_{s}$.

(2) 边: 对于每条无限折线, 它被其他折线分成若干段, 考虑其中至少属于一个大小为 $s$ 的区域 (即作为区域的边界) 的段. 如果同一个区域有多个这样的段,那么任意保留一个.

设现在一条无限折线上的段为 $t_{1}, t_{2}, \cdots, t_{l}$. 对 $1 \leq i \leq l$, 在 $t_{i}$ 对应的区域的边界上任选一点 $T_{i}$, 并设代表该区域的点为 $U_{i}$. 对 $1 \leq i \leq l-1$, 先沿直线连接 $U_{i} T_{i}$, 然后沿无限折线从 $T_{i}$ 到 $T_{i+1}$, 最后沿直线连接 $T_{i+1} U_{i+1}$, 这样形成一条图中的边.

将 $l-1$ 对 $n$ 条无限折线求和, 知图的边数至少为 $\frac{1}{2} s f_{s}-n$, 这是因为一条边至多对应两个区域的边界, 从而所有 $l$ 的和至少为 $\frac{1}{2} s f_{s}$.

现在, 我们分析图中的重边和交点情况:

(3) 由 (2) 中的定义, $U_{i}, U_{i+1}$ 是不同区域内的点, 因此图中没有自环. 由条件,任意两点间的重边数不超过同时和它们边界有交的无限折线数, 因此不超过 $c$.

(4) 交点: 由画法, 边的交点只能在无限折线上 (边的剩余部分是区域内部一点往边界上若干个点连的直线段, 不可能相交), 因此是无限折线的交点, 最多 $m$个.

由交叉数引理得，

$$
\frac{1}{2} s f_{s}-n \leq 20 c f_{s}
$$

或

$$
m \geq \frac{1}{1000} \cdot \frac{\left(\frac{1}{2} s f_{s}-n\right)^{3}}{c^{2} f_{s}^{2}}
$$

由前者得 (利用 $s>50 c$ ) $f_{s} \leq 10 \cdot \frac{n}{s}$; 当 $f_{s}>10 \cdot \frac{n}{s}$ 时, $\frac{1}{2} s f_{s}-n>\frac{2}{5} s f_{s}$, 所以由后者得

$$
f_{s}<5^{6} c^{2} \cdot \frac{m}{s^{3}}
$$

故总有

$$
f_{s} \leq 10 \cdot \frac{n}{s}+5^{6} c^{2} \cdot \frac{m}{s^{3}}<D\left(\frac{n}{s}+\frac{m}{s^{3}}\right),
$$

这便得到我们要证的结论.

综上, 命题得证.

评注 (1). 我们给出交叉数引理的证明, 即若 $|E| \geq 20 t|V|$, 则

$$
\operatorname{cr}_{\mathcal{D}}(G) \geq \frac{1}{1000} \cdot \frac{|E|^{3}}{t^{2}|V|^{2}}
$$

其中 $\operatorname{cr}_{\mathcal{D}}(G)$ 表示图 $G$ 在画法 $\mathcal{D}$ 下的交叉数.

先证明一个引理.

引理 设 $G=(V, E)$ 是一个简单图, 则 $\operatorname{cr}_{\mathcal{D}}(G) \geq|E|-3|V|$.

证明 当 $|V| \leq 7$ 时,

$$
|E|-3|V| \leq \mathrm{C}_{|V|}^{2}-3|V|=\frac{1}{2}|V|(|V|-7) \leq 0 \leq \operatorname{cr}_{\mathcal{D}}(G) .
$$

下设 $|V| \geq 8$.

注意到至多将 $G$ 中 $\mathrm{cr}_{\mathcal{D}}(G)$ 条适当的边删去, 即可得到平面图 $G^{\prime}$. 由欧拉公式, $\left|V\left(G^{\prime}\right)\right|-\left|E\left(G^{\prime}\right)\right|+\left|F\left(G^{\prime}\right)\right|=2$, 因为每个面至少有 3 条边, 且每条边在两个面中, 所以 $\left|F\left(G^{\prime}\right)\right| \leq \frac{2}{3}\left|E\left(G^{\prime}\right)\right|$, 故 $\left|E\left(G^{\prime}\right)\right| \leq 3\left|V\left(G^{\prime}\right)\right|-6$. 进而

$$
|E|-\operatorname{cr}_{\mathcal{D}}(G) \leq\left|E\left(G^{\prime}\right)\right| \leq 3\left|V\left(G^{\prime}\right)\right|-6=3|V|-6,
$$

即

$$
\operatorname{cr}_{\mathcal{D}}(G) \geq|E|-3|V|+6>|E|-3|V| .
$$

引理得证.

考虑 $G$ 的随机子图 $H$, 其中 $G$ 的每个顶点以概率 $p$ 属于 $H$, 画法 $\mathcal{D}$ 限制在 $H$上为 $\mathcal{D}_{H}$.

对每个 $H$, 将其分拆成 $t$ 个简单图, 由引理得

$$
\operatorname{cr}_{\mathcal{D}_{H}}(H) \geq|E(H)|-3 t|V(H)|,
$$

进而

$$
\mathbb{E}\left[\operatorname{cr}_{\mathcal{D}_{H}}(H)\right] \geq \mathbb{E}[|E(H)|]-3 t \mathbb{E}[|V(H)|]
$$

注意到, 画法 $\mathcal{D}$ 的一个交叉点要在画法 $\mathcal{D}_{H}$ 中被保留, 当且仅当 $G$ 中产生该交叉点的四个顶点均在 $H$ 中（若有三线共点可稍微扰动）, 故

$$
\mathbb{E}\left[\operatorname{cr}_{\mathcal{D}_{H}}(H)\right]=p^{4} \operatorname{cr}_{\mathcal{D}}(G) .
$$

又显然

$$
\mathbb{E}[|E(H)|]=p^{2}|E|, \quad \mathbb{E}[V(H)]=p|V|,
$$

所以

$$
p^{4} \operatorname{cr}_{\mathcal{D}}(G) \geq p^{2}|E|-3 t p|V|
$$

即

$$
\operatorname{cr}_{\mathcal{D}}(G) \geq \frac{|E|}{p^{2}}-\frac{3 t|V|}{p^{3}}
$$

取 $p=20 t \cdot \frac{|V|}{|E|} \leq 1$, 即得 $\mathrm{cr}_{\mathcal{D}}(G) \geq \frac{1}{1000} \cdot \frac{|E|^{3}}{t^{2}|V|^{2}}$.

(2). 交叉数引理是 M.Ajtai,V.Chvátal,M.N.Newborn,E.Szemerédi 于 1982 年在文章 Crossing-Free Subgraphs中首先证明, 之后在 Szemerédi-Trotter 定理、Erdös 单位距离问题、Sum-Product 问题中都发挥了重要的作用.

(3). 北京大学关乃粼同学对本题的解答亦有贡献.


[^0]:    ${ }^{1}$ https://dspace.library.uu.nl/bitstream/handle/1874/272370/amer.math.monthly.119.05.373.pdf

    ${ }^{2}$ https://arxiv.org/pdf/1008.1978.pdf

