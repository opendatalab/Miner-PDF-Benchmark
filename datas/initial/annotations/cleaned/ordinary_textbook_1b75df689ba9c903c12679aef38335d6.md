# 命题拾贝 

冷岗松

上海大学数学系

2015年5月・郑州
积小致巨，

以微致显.

一董仲舒

## 一. 命题拾贝

1. $m$ 维向量的逼近问题.

Ivan Borsenco (Math. Refl., 2012) 证明了如下结果:

## 定理：

设 $m, n$ 是正整数, $X=\left\{\left(x_{1}, x_{2}, \cdots, x_{m}\right) \mid x_{i}>0, \sum_{i=1}^{m} x_{i}=1\right\}$,

$Y=\left\{\left(y_{1}, y_{2}, \cdots, y_{m}\right) \left\lvert\, y_{i} \in\left\{0, \frac{1}{n}, \cdots, \frac{n-1}{n}, 1\right\}\right., \sum_{i=1}^{m} y_{i}=1\right\}$. 证明:

对任何 $\left(x_{1}, x_{2}, \cdots, x_{m}\right) \in X$, 存在 $\left(y_{1}, y_{2}, \cdots, y_{m}\right) \in Y$ 使得

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \leq \frac{m}{2 n}
$$

思考: $m$ 维正实向量 $\left(x_{1}, x_{2}, \cdots, x_{m}\right)$ 可否替代为一般的 $m$ 维实向量?

直接替代不行, 可举出反例: 令

$$
x_{1}=-\frac{m+1}{2 n}, x_{2}=\frac{m+1}{2 n}+1, x_{3}=\cdots=x_{m}=0 .
$$

这时由 $y_{1} \geq 0$ 知

$$
\left|y_{1}-x_{1}\right| \geq \frac{m+1}{2 n}>\frac{m}{2 n}
$$

因此

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \geq\left|y_{1}-x_{1}\right|>\frac{m}{2 n}
$$

矛盾!
进一步思考: 能否改变集合 $Y$ 以适应 $X$ 的变化?

这样, 就产生了下面关于一般的 $m$ 维实向量的逼近问题.

## 问题 1:

设 $m, n$ 是正整数,

$$
\begin{aligned}
& X=\left\{\left(x_{1}, x_{2}, \cdots, x_{m}\right) \mid x_{i} \in \mathbb{R}, \sum_{i=1}^{m} x_{i}=1\right\} \\
& Y=\left\{\left(y_{1}, y_{2}, \cdots, y_{m}\right) \mid n y_{i} \in \mathbb{Z}, \sum_{i=1}^{m} y_{i}=1\right\} .
\end{aligned}
$$

证明: 对任何 $\left(x_{1}, x_{2}, \cdots, x_{m}\right) \in X$, 存在 $\left(y_{1}, y_{2}, \cdots, y_{m}\right) \in Y$ 使得

$$
\sum_{i=1}^{m}\left|y_{i}-x_{i}\right| \leq \frac{m}{2 n}
$$

湖南雅礼中学的贺嘉帆同学 (2015 国家队队员) 在求解问题 1 时作代换 $a_{i}=n x_{i}, b_{i}=n y_{i}$, 将其写为一个简明的等价形式. 这诱发我们进一步研究这个问题 “系数” 的最优值, 这就产生了

## 问题 1':

设 $m, n$ 是正整数,

$$
\begin{aligned}
& A=\left\{\left(a_{1}, \cdots, a_{m}\right) \mid a_{i}>0, \sum_{i=1}^{m} a_{i}=n\right\}, \\
& B=\left\{\left(b_{1}, \cdots, b_{m}\right) \mid b_{i} \in\{0,1, \cdots, n\}, \sum_{i=1}^{m} b_{i}=n\right\} .
\end{aligned}
$$

求最小的常数 $c$, 使得对任意 $\left(a_{1}, \cdots, a_{m}\right) \in A$, 均存在 $\left(b_{1}, \cdots, b_{m}\right) \in B$满足

$$
\sum_{i=1}^{m}\left|a_{i}-b_{i}\right| \leq c m
$$

答案: $c_{\text {min }}=\frac{1}{2}$.

2. 从等差、等比数列到凸数列.

长沙市一中于杰延老师 (中等数学增刊 (2015)) 提出并证明了如下优雅的结论:

## 定理:

设 $a_{1}, a_{2}, \cdots, a_{n}$ 为递增的等差数列, $b_{1}, b_{2}, \cdots, b_{n}$ 为递增的等比数列, 且 $a_{1}=b_{1}>0$, 实数 $x$ 满足

$$
a_{1}+a_{2}+\cdots+a_{n}=b_{1}+b_{2}+\cdots+b_{n}=n x .
$$

证明:

$$
\sum_{i=1}^{n}\left|b_{i}-x\right| \geq \sum_{i=1}^{n}\left|a_{i}-x\right|
$$

思考: 等差数列与等比数列从分析的观点看属于同一类, 上述结果仅仅反映了等差数列的极值性质. 能否把等比数列 $\left\{b_{n}\right\}$ 换成一般的凸数列?

这样, 就产生了

## 问题 2:

设 $a_{1}, a_{2}, \cdots, a_{n}$ 为递增的等差数列, $b_{1}, b_{2}, \cdots, b_{n}$ 为递增的凸数列, 即对任意 $1 \leq i \leq n-1$, 有 $b_{i+1} \leq \frac{b_{i}+b_{i+2}}{2}$, 且满足

(1) $a_{1}=b_{1}>0$

(2) $a_{1}+a_{2}+\cdots+a_{n}=b_{1}+b_{2}+\cdots+b_{n}=1$. 证明:

$$
\sum_{i=1}^{n}\left|b_{i}-\frac{1}{n}\right| \geq \sum_{i=1}^{n}\left|a_{i}-\frac{1}{n}\right|
$$

问题 2 也可重新表述为下面的形式:

## 问题 2':

给定实数 $a_{1}>0$ 和正整数 $n$, 对任何满足条件 $a_{1}+a_{2}+\cdots+a_{n}$

$=1$ 的递增凸数列 $a_{1}, a_{2}, \cdots, a_{n}$, 求 $\sum_{i=1}^{n}\left|a_{i}-\frac{1}{n}\right|$ 的最小值.

进一步, 我们还证明了在有限项的凸序列中以等差数列的方差最小. 也就产生了下面的

## 问题 3:

给定实数 $a_{1}>0$ 和正整数 $n$, 对任何满足条件 $a_{1}+a_{2}+\cdots+a_{n}$

$=1$ 的递增凸数列 $a_{1}, a_{2}, \cdots, a_{n}$, 求 $\sum_{i=1}^{n}\left|a_{i}-\frac{1}{n}\right|^{2}$ 的最小值.

3. 关于复数的算术一调和均值不等式.

Alzer (Analysis, 2002) 证明了关于复数的算术一几何均值不等式:

设 $\phi \in\left[0, \frac{\pi}{2}\right], W_{\phi}=\{z \in \mathbb{C},|\arg z| \leq \phi\}$, 则对所有 $z_{1}, z_{2}, \cdots$,

$z_{n} \in W_{\phi}$ 有

$$
\left|z_{1}+z_{2}+\cdots+z_{n}\right| \geq n \cos \phi \cdot\left|\sqrt[n]{z_{1} z_{2} \cdots z_{n}}\right| .
$$

思考: 如果把 $n$ 个复数限制在一个圆盘内, 它的算术一几何均值有何关系?
这就产生了

## 问题 4:

设 $z_{1}, z_{2}, \cdots, z_{n}$ 是复数, 满足 $\left|z_{i}-1\right| \leq r(0<r<1)$. 证明:

$$
\left|z_{1}+z_{2}+\cdots+z_{n}\right| \geq n \sqrt{1-r^{2}}\left|\sqrt[n]{z_{1} z_{2} \cdots z_{n}}\right| .
$$

再思考: 是否有几何一调和均值的类似结果?

这就产生了

## 问题 5:

设 $z_{1}, z_{2}, \cdots, z_{n}$ 是复数, 满足 $\left|z_{i}-1\right| \leq r(0<r<1)$. 证明:

$$
\left|\sqrt[n]{z_{1} z_{2} \cdots z_{n}} \cdot\left(\frac{1}{z_{1}}+\frac{1}{z_{2}}+\cdots+\frac{1}{z_{n}}\right)\right| \geq n \sqrt{1-r^{2}} .
$$

进一步思考: 是否有算术一调和均值的不等式呢?

这就产生了今年冬令营的第一题:

## 问题 6 (CMO, 2015):

设 $z_{1}, z_{2}, \cdots, z_{n}$ 是复数, 满足 $\left|z_{i}-1\right| \leq r(0<r<1)$. 证明:

$$
\left|\left(z_{1}+z_{2}+\cdots+z_{n}\right)\left(\frac{1}{z_{1}}+\frac{1}{z_{2}}+\cdots+\frac{1}{z_{n}}\right)\right| \geq n^{2}\left(1-r^{2}\right) .
$$

注意: 问题 6 尽管是问题 4 和问题 5 的推论, 但直接证明并不易且形式上比问题 4 和 5 更漂亮.
再进一步思考: 问题 6 的反问题?

这就产生了:

## 问题 7:

设 $z_{1}, z_{2}, \cdots, z_{n}$ 是复数, 满足 $\left|z_{i}-1\right| \leq r(0<r<1)$. 证明:

$$
\left|\left(z_{1}+z_{2}+\cdots+z_{n}\right)\left(\frac{1}{z_{1}}+\frac{1}{z_{2}}+\cdots+\frac{1}{z_{n}}\right)\right| \leq \frac{n^{2}}{1-r^{2}} .
$$

证明要点: 注意到 $1-r \leq\left|z_{i}\right| \leq 1+r$ 以及用 Kantorovic 不等式 (常称反向柯西不等式): 设 $0<a \leq a_{k} \leq b, k=1,2, \cdots n$, 则

$$
\left(\sum_{i=1}^{n} a_{i}\right)\left(\sum_{i=1}^{n} \frac{1}{a_{i}}\right) \leq \frac{n^{2}(a+b)^{2}}{4 a b}
$$

便可.

4. 逆算术一几何平均值不等式.

算术一几何平均值的逆的结果大多通过限制变元的特定范围 (通常是区间) 得到.

思考: 是否可在一个特殊序列, 例如凸 (凹) 序列上, 建立逆算术一几何平均值不等式呢?
这样, 就产生了

## 定理:

设 $\left\{a_{i}\right\}_{i=0}^{\infty}$ 是一个无穷非负实数序列, 满足

$$
a_{0}=0, \quad a_{i} \geq \frac{1}{2}\left(a_{i-1}+a_{i+1}\right), i=1,2, \cdots
$$

证明: 对任意正整数 $n$ 有

$$
\frac{A_{n}}{G_{n}} \leq \frac{n+1}{2(n !)^{\frac{1}{n}}}
$$

其中 $A_{n}, G_{n}$ 分别为 $a_{1}, a_{2}, \cdots, a_{n}$ 的算术平均值和几何平均值.
为了降低难度, 我们推出一个稍弱的结果作为 2015 年中国国家队选拔考试第四题:

## 问题 8 (2015, 中国国家队选拨考试):

设 $0<x_{1} \leq x_{2} \leq \cdots \leq x_{n}, x_{1} \geq \frac{x_{2}}{2} \geq \frac{x_{3}}{3} \geq \cdots \geq \frac{x_{n}}{n}$, 证明:

$$
\frac{A_{n}}{G_{n}} \leq \frac{n+1}{2(n !)^{\frac{1}{n}}}
$$

其中 $A_{n}, G_{n}$ 分别为 $x_{1}, x_{2}, \cdots, x_{n}$ 的算术平均值和几何平均值.
略解: 注意到条件可写为 $0<x_{1} \leq x_{2} \leq \cdots \leq x_{n}, \frac{1}{x_{1}} \leq \frac{2}{x_{2}} \leq \cdots \leq \frac{n}{x_{n}}$,于是由切比雪夫不等式有

$$
\left(\sum_{i=1}^{n} x_{i}\right)\left(\sum_{i=1}^{n} \frac{i}{x_{i}}\right) \leq n \sum_{i=1}^{n} i=\frac{n^{2}(n+1)}{2}
$$

再由几何一调和均值不等式有

$$
\frac{n}{\sum_{i=1}^{n} \frac{i}{x_{i}}} \leq \sqrt[n]{\prod_{i=1}^{n} \frac{x_{i}}{i}}
$$

故由 (1),(2) 整理便得所证结果.

5. 非周期条件下的逆 F-T-T 不等式.

Fan-Taussky-Todd (Monatsh. Math. 1955) 证明了如下结论:

## 定理:

设 $n(n \geq 2)$ 个实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足

$\begin{array}{ll}\text { (i) } \sum_{i=1}^{n} x_{i}=0 ; & \text { (ii) } \max _{1 \leq i \leq n}\left|x_{i}\right|=1 ; \quad \text { (iii) } x_{n+1}=x_{1} \text {. }\end{array}$

则 $J(x)=\max _{1 \leq i \leq n}\left|x_{i+1}-x_{i}\right|$ 的最小值是 $\begin{cases}\frac{4}{n}, & \text { 当 } n \text { 是偶数; } \\ \frac{4 n}{4 n+1}, & \text { 当 } n \text { 是奇数. }\end{cases}$
思考: 保持条件不变, 研究它的反问题, 即求 $\min _{1 \leq i \leq n}\left|x_{i+1}-x_{i}\right|$ 的最大值, 结果如何?

这是一个不难的问题, 答案为 $\begin{cases}2, & \text { 当 } n \text { 是偶数; } \\ 1, & \text { 当 } n \text { 是奇数. }\end{cases}$

进一步思考: 如果去掉周期条件 (iii), 继续考虑 F-T-T 不等式的反问题, 这就产生了

## 问题 9 (2014, 中国西部):

给定整数 $n \geq 2$, 设实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 (1) $\sum_{i=1}^{n} x_{i}=0$;

(2) $\left|x_{i}\right| \leq 1, i=1,2, \cdots, n$. 求 $\min _{1 \leq i \leq n-1}\left|x_{i+1}-x_{i}\right|$ 的最大值.

答案: $\begin{cases}2, & \text { 当 } n \text { 是偶数; } \\ \frac{2 n}{n+1}, & \text { 当 } n \text { 是奇数. }\end{cases}$

6. 图的最大独立子集问题.

Fajtlowicz 在他的一篇论文 (Graph theory and comput., 1978) 中证明了如下结论:

## 定理:

设 $G$ 是 $n$ 个顶点的简单图, 它的最大度为 $p$, 且不包含 $q$ 个顶点的团. 若 $p \geq q$, 则图 $G$ 的最大独立集的元素个数 $\alpha$ 满足

$$
\alpha \geq \frac{2 n}{p+q}
$$

Fajtlowicz 在他的另一片论文 (Combinatorica, 1984) 中讨论了上述估计等号成立的条件, 他证明了:

## 定理:

如果 $q \leq p$, 则 $\alpha=\frac{2 n}{p+q}$ 可推出 $3 q-2 p \leq 5$. 另外, 对于满足

$3 q_{1}-2 p_{1}=5$ 的正整数 $p_{1}$ 和 $q_{1}$, 存在一个唯一的连通图 $G$ 使得 $p=p_{1}, q=q_{1}$ 且 $\alpha=\frac{2 n}{p+q}$.
思考: 能否综合这两篇论文的结果, 产生一个关于图的最大独立子集的组合极值问题?

尝试了一些 $n, p, q$ 的值后, 我们决定选取 $n=30, p=5, q=5$. 编拟了如下问题:

设 $G$ 是 30 个顶点的简单图, 它的每个顶点的度都不超过 5 , 且 $G$的任何 5 点都存在两点没有连边. 求 $G$ 的最大独立子集元素个数的最小值.
随后, 我们反复思考的一个问题是: 如何构造一个可用 “几何语言” 描述的组合模型? 最后成功构造了这样一个平面上的 “五棱柱” (即将 $G$ 的 30 个顶点分成 3 组, 任何两组不连边, 在每组中画成五棱柱).


这样, 改变成非图论的语言, 这就产生了今年冬令营的第五题:

## 问题 10 (CMO, 2015):

某次会议共有 30 人参加, 其中每个人在其余人中至少有 5 个熟

人; 任意 5 个人中, 至少有两人不是熟人. 求最大的正整数 $k$, 使得在满足上述条件的 30 个人总存在 $k$ 个人, 两两不是熟人.

## 二. 问题的难度评估

1. 一些观点和看法.

(1) 难题 $\neq$ 好题;

(2) 偏题和太难的题缺乏教育功能;

(3) 培训中难题数量要控制在一个合适的比例;

(4) 难度评估的两要素 $\left\{\begin{array}{l}\text { 学生的水平; } \\ \text { 数学上的难点. }\end{array}\right.$

2. 难度评估一例.

## 题 1 (2015年国家集训队):

设 $f_{1}(x), f_{2}(x), \cdots, f_{n}(x)$ 是定义在实数集上的实值有界函数, $a_{1}, a_{2}, \cdots, a_{n}$ 是不同的 $n$ 个实数. 证明: 存在实数 $x$ 使得

$$
\sum_{i=1}^{n} f_{i}(x)-\sum_{i=1}^{n} f_{i}\left(x-a_{i}\right)<1
$$

要评估这个试题的难度, 我们先看它的两个特例.

## 题 1 中 $n=1$ 的情况:

## 题 2:

设 $f(x)$ 是定义在实数集上的实值有界函数, $a \in \mathbb{R}$. 证明: 存在实数 $x$ 使得

$$
f(x)-f(x-a)<1
$$

略解: 由 $f(x)$ 有界, 存在正常数 $M$ 使得 $|f(x)| \leq M, \forall x \in \mathbb{R}$.

假设结论不成立, 则对任意实数 $x$, 均有 $f(x)-f(x-a) \geq 1$.

于是取 $x=j a, j \in \mathbb{N}^{*}$ 得 $f(j a)-f((j-1) a) \geq 1$.

故对任意 $k \in \mathbb{N}^{*}$, 有

$$
2 M \geq f(k a)-f(0)=\sum_{j=1}^{k}(f(j a)-f((j-1) a)) \geq \sum_{j=1}^{k} 1=k
$$

矛盾!
题 2 有三个难点 (相对联赛水平的学生来说):

(1) 取 $x=j a$ ，产生差分 (差分思想);

(2) 对差分求一个待定项数的和 (差分累加效应);

(3) 对和式 “算两次” .

同时, 题 2 方法的单一性, 增加了它的难度. 但上述难点除 (2) 外都是常用方法, 问题入手不难, 且没有有难度的代数变形(或计算),这又降低了问题的难度.

综上, 我们认为题 2 是一个全国联赛水平的中等难度的问题.
再看题 1 中 $n=2$ 的情况:

## 题 3:

设 $f(x), g(x)$ 是定义在实数集上的实值有界函数, $a, b$ 是不相等的两个实数. 证明: 存在实数 $x$ 使得

$$
f(x)+g(x)-f(x-a)-g(x-b)<1 .
$$

略解: 由 $f, g$ 的有界性知, 存在正常数 $M$ 使得 $|f(x)| \leq M,|g(x)| \leq M$.假设结论不成立, 则对任意 $x \in \mathbb{R}$ 有

$$
f(x)+g(x)-f(x-a)-g(x-b) \geq 1 .
$$

取 $x=i a+j b, i, j \in \mathbb{N}^{*}$ 得

$$
f(i a+j b)-f((i-1) a+j b)+g(i a+j b)-g(i a+(j-1) b) \geq 1
$$

对任意 $k \in \mathbb{N}^{*}$, 考虑二重和

$$
S(k)=\sum_{i=1}^{k} \sum_{j=1}^{k}(f(i a+j b)-f((i-1) a+j b)+g(i a+j b)-g(i a+(j-1) b))
$$

一方面有

$$
S(k) \geq \sum_{i=1}^{k} \sum_{j=1}^{k} 1=k^{2}
$$

另一方面

$$
\begin{aligned}
S(k) & =\sum_{j=1}^{k}\left(\sum_{i=1}^{k}(f(i a+j b)-f((i-1) a+j b))\right)+\sum_{i=1}^{k}\left(\sum_{j=1}^{k}(g(i a+j b)-g(i a+(j-1) b))\right) \\
& =\sum_{j=1}^{k}(f(k a+j b)-f(j b))+\sum_{i=1}^{k}(g(i a+k b)-g(i a)) \\
& \leq \sum_{j=1}^{k} 2 M+\sum_{i=1}^{k} 2 M=4 M k .
\end{aligned}
$$

故有 $4 M k \geq k^{2}$, 即 $k<4 M$, 矛盾!
题 3 仍有三个难点:

(1) 取 $x=i a+j b$, 产生两个差分;

(2) 对两个差分考虑一个待定项数的两重和;

(3) 两重和的 “算两次” 。

这里的每一个难点都高于题 2 , 都要有一定的想法支配. 因此, 我们认为题 3 是一个 CMO (冬令营) 水平的中等难度的问题.

## 题 1 的难度分析:

题 1 的三个难点:

(1) 取 $x=i_{1} a_{1}+i_{2} a_{2}+\cdots+i_{n} a_{n}$, 产生 $n$ 个差分;

(2) 对 $n$ 个差分考虑一个待定项数的 $n$ 重和;

(3) $n$ 重和的 “算两次” .

对于一般学生, 要攻克题 1 , 先研究它的特例: $n=1$ 和 $n=2$ 的情况, 即细致地做好题 2 和题 3 , 再把方法提升一下便可. 如果不研究特例, 步伐过大, 则要求很高的分析能力.综上, 我们认为题 1 是国家集训队水平的中等难度的问题.
谢谢大家!

